# Beacon Signal Engine — Build Spec

The Signal Engine is Beacon's differentiator: for every target it runs a miniature
AI-visibility audit **before** outreach and produces the verified finding that opens touch
#1. This document specs the build with **Clay** (research/enrichment orchestration) and
**n8n** (glue, API calls, artifact capture). Substitute equivalents freely — the logic is
what matters.

## Output contract

For each lead, the engine writes this object to the CRM before the lead is eligible to send:

```json
{
  "lead_id": "…",
  "probed_at": "2026-07-23T14:00:00Z",
  "findings": [
    {
      "id": "f_001",
      "type": "outdated | competitor | accuracy | absence",
      "platform": "chatgpt | perplexity | gemini | claude",
      "query": "Is <practice> a good place for <treatment>?",
      "description": "Full sentence, human-readable, safe to paste into an email.",
      "severity": 0,
      "screenshot_ref": "s3://beacon-artifacts/lead/f_001.png",
      "captured_at": "2026-07-23T14:00:11Z"
    }
  ],
  "top_finding": "f_001",
  "signal_status": "verified | soft | none"
}
```

**Enforcement rule (non-negotiable):** a finding is only valid with a non-null
`screenshot_ref` and `captured_at`. Beacon may only make company-specific claims that map to
a valid finding. `signal_status: "soft"` (findings exist but none artifact-backed) forces the
1b soft-angle opener; `"none"` deprioritizes or drops the lead.

## Pipeline stages

```
Clay table (1 row = 1 lead)
  → enrich (firmographics, flagship treatment, city, competitors)
  → n8n webhook: run visibility probe across 4 platforms
  → capture raw answer + timestamped screenshot per query
  → gap detection (classify + score)
  → write findings back to Clay row
  → sync qualified rows to CRM (Book-eligible only when signal_status ≠ none)
```

### Stage 1 — Enrichment (Clay)

Columns to resolve per lead: `practice_name`, `website`, `city`, `flagship_treatment`
(from services page / highest-margin inference), `competitor_1..3` (top local rivals),
`decision_maker`, `email`, `linkedin`, `region` (for GDPR/CASL logic).

### Stage 2 — Visibility probe (n8n, per platform)

For each platform, send a small, fixed query set. Use the official APIs; for platforms whose
consumer answer differs from the API, use a headless browser step (Playwright) so the
screenshot matches what a real buyer sees. **Run each query at low temperature, once, and
archive the raw response** — reproducibility matters because these become claims.

Query set (parameterized per lead):

1. `Is «practice_name» a good place for «flagship_treatment» in «city»?`
2. `Who are the best «flagship_treatment» providers in «city»?`
3. `What do people say about «practice_name»?`
4. `What services does «practice_name» offer?`

Capture per query: raw text answer, cited sources/links, and a full-page screenshot with a
visible timestamp. Store the screenshot to object storage; keep the URL as `screenshot_ref`.

### Stage 3 — Gap detection (n8n function + LLM classify)

Classify each answer against the target facts (from Stage 1 enrichment + the practice's own
site). Use a Claude call with a strict rubric; never let the classifier assert a gap the
screenshot doesn't support.

Gap taxonomy and severity (0–2):

| Type | Trigger | Severity |
|---|---|---|
| **accuracy** | AI states something factually wrong (wrong doctor, wrong location, wrong claim) | 2 |
| **outdated** | AI names a discontinued service or stale info | 2 |
| **competitor** | AI recommends a rival above/instead of them for their flagship | 1–2 |
| **absence** | AI can't describe them, or omits the flagship entirely | 1 |
| *(none)* | Answers are accurate and favorable | 0 |

Classifier prompt (core):

> You are auditing how an AI assistant answered questions about a medical-aesthetics
> practice. Given the AI's answer, the practice's verified facts, and the question, identify
> only gaps that are **explicitly present in the answer text provided**. For each gap return
> `{type, severity, description}` where `description` is a single email-safe sentence stating
> exactly what the answer showed. If the answer is accurate and favorable, return `[]`. Never
> infer a gap that is not literally in the answer text. Do not exaggerate severity.

### Stage 4 — Select `top_finding`

Rank findings by `severity` desc, then by type priority `accuracy > outdated > competitor >
absence`, then by platform reach (`chatgpt > gemini > perplexity > claude`). The winner
becomes `top_finding` and seeds the touch-1a subject/opener merge fields.

Set `signal_status`:
- `verified` — ≥1 finding with a valid `screenshot_ref`.
- `soft` — findings exist but none artifact-backed (rare; usually a capture failure → retry).
- `none` — no findings; route to soft-angle or deprioritize.

### Stage 5 — Write-back & handoff

Write the full object to the Clay row and sync to the CRM. Only rows with
`signal_status = verified` enter the primary (finding-led) send queue; `soft`/`none` rows go
to the soft-angle queue or nurture.

## Reliability & integrity controls

- **Reproducibility:** archive raw answers + prompts + timestamps; a claim must be traceable
  to a stored artifact months later.
- **Capture-failure retry:** if screenshot capture fails, retry once, then downgrade to
  `soft` rather than sending an unbacked claim.
- **Freshness:** findings older than **14 days** expire — re-probe before send, since AI
  answers drift.
- **Rate/cost control:** batch probes, cache per-practice results, cap platforms per lead if
  cost matters (ChatGPT + Perplexity is a viable minimum pair).
- **PII/scope:** store only business-facing data; never capture or infer patient information.
- **Human spot-check:** in Phase 1, Kara reviews a sample of findings to confirm accuracy
  before they're ever used in copy.

## Minimal viable version (build this first)

If you want signal on the board in week one without the full stack:

1. Clay table with enrichment + a single query (`Is «practice» good for «treatment» in
   «city»?`) against ChatGPT + Perplexity.
2. One n8n workflow: call both APIs, screenshot via Playwright, store to Drive/S3, Claude
   classify, write `top_finding` back.
3. Manual Kara review of the first ~40 findings to calibrate the classifier and the
   `description` phrasing.

Expand to four platforms, the full query set, and automated `top_finding` ranking once the
copy is converting.
