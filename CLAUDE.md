# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Marketing website for **Gold Light Digital** — an AI Visibility & Trust consultancy
(founder: Kara Reagan) serving regulated industries (HealthTech, MedTech & Pharma,
Medical Aesthetics, Nutraceuticals, FinTech). The site explains the "AI visibility
gap," the firm's services (AI Visibility Snapshot, AI Brand Visibility Audit, and
ongoing monitoring), the process, and how to get in touch.

It is a **static, dependency-free website** — plain HTML, CSS, and vanilla JS. No
build step, no framework, no package manager.

## Setup & running

No install step. Open `index.html` directly, or serve locally:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Structure

- `index.html` — single-page site (hero, how-we-work, services, compliance, pricing, industries, about, contact, footer).
- `privacy.html` / `terms.html` — Privacy Policy and Terms & Conditions pages (linked from the footer).
- `css/styles.css` — all styles; design tokens live in `:root` at the top.
- `js/main.js` — sticky header, mobile nav toggle, and scroll-reveal (all progressive enhancement).
- `assets/favicon.svg` — brand favicon.
- `build-standalone.py` — regenerates the paste-ready single-file builds. Run after editing any HTML/CSS/JS.
- `*-standalone.html` — generated, self-contained single-file versions of each page (CSS/JS/favicon inlined) for website builders that only accept a single code block. Do not hand-edit; run `python3 build-standalone.py`.

## Legal pages

`privacy.html` and `terms.html` are **general-purpose templates, not legal advice** (each carries a `TEMPLATE NOTICE` comment). Before relying on them: replace the Governing Law jurisdiction placeholder in `terms.html`, confirm the copy matches actual data practices/tools, and have counsel review. Update the visible "Last updated" date when the content changes.

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
