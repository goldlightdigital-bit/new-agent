# Beacon — Outbound Appointment-Setting Agent

**Beacon** is an AI appointment-setting agent for **Gold Light Digital**, an AI Visibility
& Trust consultancy for regulated industries (HealthTech, MedTech, Pharma, Medical
Aesthetics, Nutraceuticals, FinTech).

Its one job: **book qualified 25-minute discovery calls** with the right decision-makers by
running research-heavy, compliant outbound. Its differentiator: it runs a miniature
AI-visibility audit on each prospect *before* reaching out, and opens with one real,
screenshot-backed observation of how AI platforms currently misrepresent their brand.

> The guiding principle: **Gold Light sells trust, so the outreach itself is the first proof
> of the product.** Quality over volume; verified claims only; a human gate wherever the
> brand is exposed.

## Documents

| File | What it is |
|---|---|
| [`system-prompt.md`](./system-prompt.md) | The complete production system prompt for the agent brain — role, method, TRUST rubric, reply handling, guardrails, output contract. |
| [`sequence-medical-aesthetics.md`](./sequence-medical-aesthetics.md) | Full 5-touch cadence copy (email + LinkedIn) for the medical-aesthetics vertical, with finding-led and soft-angle variants and objection responses. |
| [`signal-engine-build.md`](./signal-engine-build.md) | Technical build spec for the AI-visibility "wedge" — Clay + n8n pipeline, probe queries, gap taxonomy, artifact capture, integrity controls. |

The interactive visual blueprint (architecture, cadence, autonomy tiers, stack, KPIs) is
published as an Artifact — regenerate or update it from the conversation that created it.

## Core concepts at a glance

- **The wedge** — probe ChatGPT · Perplexity · Gemini · Claude about the prospect, capture
  dated screenshots, lead with the strongest verified finding. No artifact → no claim.
- **TRUST rubric** — Target fit · Risk exposure · Urgency trigger · Stakeholder authority ·
  Timing & means. Scored 0–2 each; total routes Book (7–10) / Nurture (4–6) / Release (0–3).
- **5-touch cadence** over ~18 days, stopping on any reply/booking/opt-out.
- **Three autonomy phases** — Co-pilot (human approves every send) → Supervised → Autonomous,
  each with an explicit graduation gate.

## Recommended stack (boutique default, ~$250–450/mo)

Google Workspace (Gmail + Calendar) · dedicated warmed sending domain · Smartlead
(sequencer + warmup) · LinkedIn Sales Navigator + Apollo (sourcing) · Clay (research +
Signal Engine) · ChatGPT/Perplexity/Gemini/Claude APIs (probing) · HubSpot Free (CRM) ·
Cal.com (booking) · Claude Agent SDK + n8n (agent brain + glue) · Slack/Gmail drafts
(human approvals).

## Compliance guardrails (hard rules)

Verified claims only · stays in the visibility/trust lane (no medical, clinical, legal, or
financial advice) · CAN-SPAM / GDPR / CASL · dedicated-domain sender health with
circuit-breakers · Kara's brand voice · escalate to human on anything sensitive or
low-confidence.
