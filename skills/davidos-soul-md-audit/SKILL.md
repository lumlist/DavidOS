---
name: davidos-soul-md-audit
description: Structural audit of SOUL.md against five falsifiable tests (token weight, duplication, pointer integrity, behavior drift, coverage). Produces a structured findings report with proposed edits. Per SOUL.md §10 Living-Document Protocol. Invoke when David asks for an audit, when a §7.3 Drift flag is accepted, or quarterly.
optimization_status: STUB — tag for optimization after first 1-2 invocations. Tests A-E are Opus's construction; charter-active Atlas should review them for completeness during first invocation.
---

# davidos-soul-md-audit

> **Optimization tag:** v0.1 stub from Opus structural review (`docs/audits/preparation/2026-05-14-opus-soul-md-structure-review-output.md`). After first 1–2 real audits, calibrate: (a) Are tests A–E the right tests? Atlas may surface a missing Test F. (b) Are the thresholds right (§6 > 50%, total > 2,000 words)? (c) Should the test order be different? (d) Should any test auto-invoke a follow-up skill (e.g., Test D drift → `davidos-leverage-assessment` on the proposed correction)?

## When to load

Per SOUL.md §10 invocation triggers:
- David explicitly invokes: "audit SOUL.md" / "run the soul audit" / "check the charter"
- A §7.3 Drift flag has fired and David has accepted invocation
- Quarterly review is due: last audit date + 90 days

## Inputs Atlas should confirm

1. **Scope** — full audit (all five tests) or targeted (one or two tests)? Default: full.
2. **Output destination** — proposed edits go where? Default: a dated findings file at `docs/audits/soul-md-audits/YYYY-MM-DD-soul-md-audit.md` plus inline summary to David.
3. **Comparison baseline** — for behavior drift (Test D), how many recent approvals-log entries to check? Default: last 5.

## The five tests

### Test A — Token weight check

**What it measures:** Whether SOUL.md is becoming bloated relative to its load-every-session role.

**Mechanical procedure:**
1. `wc -w SOUL.md` for total
2. Per-section word count via section-header parsing
3. Compute §6 ratio of total

**Flags:**
- **AMBER** if §6 > 45% of total OR total > 1,800 words
- **RED** if §6 > 50% of total OR total > 2,000 words

**Reporting:** Word counts per section, ratio, change since last audit if available.

### Test B — Duplication check

**What it measures:** Rules defined in two canonical places, creating drift risk.

**Mechanical procedure:**
1. Grep SOUL.md for key rule phrases (the four-condition test, the 80%/80% thresholds, "always ask," "advisory vs. decisive," etc.)
2. Grep canonical pointer files (`action-map.md`, `modifiers.md`, `SCHEMA.md`, `ADR-004`, `hermes-config.md`) for the same phrases
3. Identify any rule defined identically (good — these are duplications) or contradictorily (drift) in two places

**Flags:**
- **RED** for any rule defined contradictorily in two places
- **AMBER** for any rule duplicated identically (low-grade waste, propose consolidation)

**Reporting:** Table of duplications with proposed canonical home.

### Test C — Pointer integrity check

**What it measures:** Whether every file path / section reference in SOUL.md still resolves.

**Mechanical procedure:**
1. Extract every `docs/...md` reference and every `§X.Y` reference from SOUL.md
2. For each: verify file exists; if a specific line or section is cited, verify it's still there
3. For ADR references (e.g., "ADR-004 L66–L75"), verify the cited line range still contains the cited content

**Flags:**
- **RED** for any broken file pointer
- **AMBER** for any pointer where cited content has moved within the file (line numbers drifted)

**Reporting:** Each broken pointer with the current state of the referenced location.

### Test D — Behavior drift check

**What it measures:** Whether Atlas's recent behavior matches SOUL.md §6 rules.

**Mechanical procedure:**
1. Read last N entries from `docs/decisions/approvals-log.md` (default N=5)
2. For each entry, classify against §6:
   - Did this action belong in the four-condition act-without-asking set? (Should Atlas have acted silently?)
   - Did Atlas use the right approval intensity (Light/Full per ADR-004)?
   - If Atlas asked when he shouldn't have, OR acted when he should have asked — flag.

**Flags:**
- **RED** for any unilateral action that should have been gated
- **AMBER** for any over-asked action (efficiency drift but not safety drift)

**Reporting:** Each flagged entry with the SOUL.md or ADR-004 rule it diverged from.

### Test E — Coverage check

**What it measures:** Whether SOUL.md + AGENTS.md (when it exists) cover all 11 charter outcomes and all 7 consolidated principles.

**Mechanical procedure:**
1. Read `docs/charter/outcomes-and-frustrations-2026-05-13.md` for the 11 outcomes
2. Read `docs/audits/preparation/2026-05-13-task2-consolidated-principles.md` for the 7 principles
3. For each outcome and each principle, identify which SOUL.md section (or AGENTS.md section, when it exists) addresses it
4. Flag any uncovered outcomes or principles

**Flags:**
- **RED** for any uncovered outcome
- **AMBER** for any principle that's covered weakly (one passing mention, not operationalized)

**Reporting:** Coverage matrix with citations.

## Output format

The audit produces a single dated file at `docs/audits/soul-md-audits/YYYY-MM-DD-soul-md-audit.md` containing:

1. **Summary verdict** — overall RED / AMBER / GREEN and 1-paragraph headline
2. **Per-test results** — A through E, with flags raised and evidence
3. **Proposed edits** — concrete diffs Atlas proposes for David's review
4. **Confidence tags** per §7.2 on every claim
5. **What this audit didn't check** — explicit out-of-scope statement

## Improvement loop

Per SOUL.md §10:
- Audit findings produce **proposed** edits — never silently applied
- Edits to SOUL.md are L1 Full per action-map.md Category 16
- Approved edits update SOUL.md and the audit's last-reviewed timestamp
- David-rejected findings are logged as deliberate positions, not silently dropped

## Reference

- `SOUL.md` §10 — Living-Document Protocol (the source of this skill's mandate)
- `docs/audits/preparation/2026-05-14-opus-soul-md-structure-review-output.md` — the Opus review that designed tests A–E
- `docs/autonomy/action-map.md` Category 16 — SOUL.md edits are L1 Full
- `docs/decisions/ADR-004-workspace-native-approval-mechanism.md` — approval intensity scheme
