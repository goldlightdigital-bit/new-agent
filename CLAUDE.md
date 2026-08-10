# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Multi-page marketing website for **Gold Light Digital** — an AI Visibility &
Compliance advisory (founder: Kara Reagan) for **regulated industries**: HealthTech,
MedTech, Pharma, Medical Aesthetics & Dermatology, Nutraceuticals, and FinTech. The
site positions the offer ladder (free **AI Visibility Snapshot** → **AI Visibility
Audit**, from **$8,500** → monthly **AI Trust Governance Program**), the 4 Pillars
framework (Accuracy, Authority, Consistency, Credibility Signals), a compliance lens
(HIPAA / FDA / SEC exposure, four-level flag scale), the anonymized dermal-filler
case study as the cross-vertical proof point, an About page, and how to book a call.

**Positioning guardrails (important):** the site leads with the **regulated-industries
compliance** angle across all six verticals — HIPAA / FDA / SEC framing is in scope.
Still, the firm **audits and advises; it is not a law firm** — never state a legal
determination; flag risk and recommend the client's counsel (see the Services page
"Note on Legal Counsel"). The Audit shows "Starting at $8,500"; the Governance
Program shows "Monthly retainer" (no fixed figure). Marketing voice is first-person
**plural ("we")** everywhere except the **About/bio**, which stays first-person
singular (Kara). *(This reverses the earlier aesthetics-only / no-HIPAA / hidden-
pricing guardrails at Kara's explicit direction — see the Aug 2026 copy rewrite.)*

It is a **static, dependency-free website** — plain HTML, CSS, and vanilla JS. No
build step, no framework, no package manager. Pages are deployed individually into
Go High Level via Custom HTML (paste the matching `*-standalone.html`).

## Setup & running

No install step. Open `index.html` directly, or serve locally:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Structure

- `index.html` — **Home** (hero, stat callout row, "Why This Matters Now", services teaser, "Who We Serve" six-vertical grid `#industries`, case-study teaser `#results`, closing CTA `#contact`).
- `services.html` — **Services** (three tiers in full detail + "A Note on Legal Counsel"). `about.html` — **About** (Kara's bio + how-I-work). `case-study.html` — **Case Study** (dermal-filler audit, the numbers, what-we-found / what-changed).
- `privacy.html` / `terms.html` / `accessibility.html` — Privacy Policy, Terms & Conditions, and Accessibility Statement pages.
- All pages share one header/footer; cross-page nav links use absolute production URLs (`https://goldlightdigitalmarketing.com/{home,services,case-study,about,privacy,terms,accessibility}`), and the Home page uses `#industries` / `#contact` anchors for its own sections.
- `css/styles.css` — all styles; design tokens live in `:root` at the top. v2 consulting-rebuild components are in a clearly-marked section near the end.
- `js/main.js` — sticky header, mobile nav toggle, scroll-reveal, and cookie-consent banner (all progressive enhancement). The banner stores the visitor's choice under the `gld-cookie-consent` localStorage key (`accepted`/`declined`); any analytics added later should gate on that value.
- `assets/` — `favicon.svg`, `hero-skin.png` (hero image), `kara-reagan.png` (bio photo).
- `build-standalone.py` — regenerates the paste-ready single-file builds. Run after editing any HTML/CSS/JS.
- `*-standalone.html` — generated, self-contained single-file versions of each page (CSS/JS/favicon inlined) for website builders that only accept a single code block. Do not hand-edit; run `python3 build-standalone.py`.
- `webinars-standalone.html` — a **standalone** embed for the "webinars" page (hosted on the Go High Level site via a Custom HTML element). It is **independent of the main site**: its own teal/gold/cream palette and Poppins type, all CSS inlined and namespaced under `.glr-` with a theme-proofing layer so it can't collide with the host theme. Hand-maintained (not produced by `build-standalone.py`); has `REPLACE` comments for video URLs, thumbnails, and the email form.

## Legal pages

`privacy.html`, `terms.html`, and `accessibility.html` are **general-purpose templates, not legal advice** (each carries a `TEMPLATE NOTICE` comment). Before relying on them: confirm the copy matches actual data practices/tools and site conformance, and have counsel review. Terms are set to **California** governing law and the Privacy Policy includes a **CCPA/CPRA** section stating no sale/sharing of personal info — update these if the operating jurisdiction changes. Update the visible "Last updated" date when content changes.

## Brand system

Keep these consistent with Gold Light Digital's existing assets:

- **Colors:** base `#12151d`, warm dark `#1c1a12`, gold `#e8c15c`, off-white `#f5f3ee`, muted `#a9adb8`, faint `#8b8f99`.
- **Type:** Fraunces (serif display / headlines), Inter (sans body). The brand's
  graphic template uses Georgia/Arial; Fraunces + Inter are the web-font equivalents.
- **Logo mark:** gold dot + uppercase, letter-spaced "GOLD LIGHT DIGITAL" wordmark.

## Conventions

- Vanilla everything — no dependencies. Prefer adding a CSS custom property over hard-coding a color.
- Copy is compliance-aware, precise, and never alarmist (matches Kara's established voice).
- Every interactive feature degrades gracefully and respects `prefers-reduced-motion`.
- Keep the site accessible: semantic landmarks, skip link, visible focus states, ARIA on the nav toggle.

## Working in this repository

- Keep this file up to date as tooling and structure are introduced.
- Prefer documenting non-obvious decisions here rather than leaving them implicit in the code.
