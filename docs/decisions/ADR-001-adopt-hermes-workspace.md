# ADR-001: Adopt hermes-workspace over custom UI build

**Date:** 2026-05-11
**Status:** Accepted
**Deciders:** David Izzard

## Context

Paperclip-Atlas had a productivity-review scheduler that auto-created blocking issues on stale `in_progress` tickets (DAV-22 cascaded into DAV-23, 24, 25, 26 within hours). The trigger (`long_active_duration`) is not configurable. CEO-role auto-grants also forced `can_assign_tasks: true` with no toggle. These constraints made Paperclip unworkable as a daily driver.

We considered three paths forward:

1. **Custom build** — design and ship our own multi-agent web UI on top of Hermes
2. **`fathah/hermes-desktop`** — Electron single-agent app, similar surface to Paperclip
3. **`outsourc-e/hermes-workspace`** — multi-agent web UI, 3.9k stars, MIT license, actively maintained

## Decision

Adopt `outsourc-e/hermes-workspace` as the daily-driver UI.

## Rationale

- **Multi-agent native.** Supports Atlas, Karrigan, FamilyAI agents, and future iZZi customer agents on one surface. Single-agent options (Paperclip, hermes-desktop) require duplicating infrastructure per agent.
- **iZZi customer-zero fit.** What works for David's stack is exactly what future iZZi AI Systems customers will need. A custom build would be David-specific by default.
- **Time to value.** Custom build = weeks. Workspace adoption = single session.
- **Reversible.** A custom build remains possible later if Workspace hits a ceiling. The Workspace install does not foreclose that option.
- **Risk profile.** 3.9k stars + MIT license + active maintenance is a reasonable bet for a daily driver. We will re-evaluate after 2–3 sessions of daily use.

## Consequences

- Stage 2.7 (originally a Paperclip-Atlas UI proposal) is superseded — Workspace IS Stage 2.7 v0
- Workspace becomes part of the documented stack future iZZi customers inherit
- Need to document Workspace baseline configuration so the pattern is reproducible (`docs/workspace/baseline-config.md`)

## Re-evaluation triggers

- Workspace can't support a feature core to DavidOS or a customer (e.g., specific agent governance, custom skills, etc.)
- Maintenance velocity drops or repository becomes inactive
- Cost or hosting becomes a constraint we can't work around

## Related

- ADR-002 — Anthropic OAuth over API key
- ADR-003 — Paperclip frozen, Atlas as memo library
