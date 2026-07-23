# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Status

This repository (`new-agent`) currently holds the **design** for **Beacon**, an outbound
appointment-setting AI agent for **Gold Light Digital** — an AI Visibility & Trust
consultancy for regulated industries. No application code has been committed yet; the work so
far is specification and copy. Update this file as implementation begins.

## Overview

Beacon runs research-heavy, compliant outbound to book qualified 25-minute discovery calls
with decision-makers in regulated industries (HealthTech, MedTech, Pharma, Medical
Aesthetics, Nutraceuticals, FinTech). Its differentiator ("the wedge") is running a
miniature AI-visibility audit on each prospect — querying ChatGPT, Perplexity, Gemini, and
Claude — and opening outreach with one verified, screenshot-backed finding.

Guiding principle: **Gold Light sells trust, so the outreach itself is the first proof of
the product** — quality over volume, verified claims only, human-in-the-loop where the brand
is exposed.

## Where things live

- **`docs/beacon/README.md`** — index and concepts at a glance.
- **`docs/beacon/system-prompt.md`** — the production system prompt for the agent brain.
- **`docs/beacon/sequence-medical-aesthetics.md`** — full 5-touch outbound copy for the
  first vertical.
- **`docs/beacon/signal-engine-build.md`** — build spec for the AI-visibility pipeline
  (Clay + n8n).
- The interactive visual blueprint is published as a Claude Artifact (architecture, cadence,
  TRUST rubric, autonomy tiers, stack, KPIs).

## When implementation begins, document here

- **Setup** — how to install dependencies and configure a local environment.
- **Common commands** — build, run, test, lint, and format commands (with exact invocations).
- **Architecture** — key modules, directories, and how they fit together.
- **Conventions** — coding style, naming, commit message format, and project-specific patterns.

## Working in This Repository

- Keep this file up to date as tooling and structure are introduced, so it always reflects how to build, test, and run the project.
- Prefer documenting non-obvious decisions here rather than leaving them implicit in the code.
