# Governance and Self-Improvement — Pointer for Phase 1 / Karrigan

**Date:** 2026-05-14
**Author:** Atlas (claude-opus-4-7)
**Status:** Pointer doc. Substance lives in the proposal at the path below.
**Audience:** Karrigan (when he ships), early Phase 1 surface.

---

## What this is

A one-screen pointer flagging that the v0.1 autonomy substrate has been audited (12 findings from Sonnet, 7 additional from Opus) and a comprehensive proposal exists for both static fixes and dynamic governance mechanisms.

Karrigan should surface the governance section (Part B) early in Phase 1 — *before* he ships any operational work that depends on the substrate's calibration loops being in place.

## Where the substance lives

**Primary doc:**
[`docs/audits/preparation/2026-05-14-atlas-comprehensive-fix-and-governance-proposal.md`](../audits/preparation/2026-05-14-atlas-comprehensive-fix-and-governance-proposal.md)

- Part A: 16 numbered fixes covering 19 audit findings, grouped by file (action-map.md, modifiers.md, SCHEMA.md, cross-file), each with proposed L1 intensity per ADR-004 + SCHEMA §4b, reasoning, and dependency notes.
- Part B: governance and self-improvement design — three-tier audit cadence, approval-log calibration, evolution policy, learning propagation tiers, the router skill, Karrigan integration hook, and five other high-leverage items.
- Suggested sequencing: seven approval batches, ADR-005 first as the umbrella.
- Open questions: five items requiring David's call.

## What Karrigan should do with this

1. **Read Part B before doing operational work.** The governance mechanisms (Tier 1/2/3 audits, calibration via approvals log, the router skill, the learning propagation tiers) are load-bearing for the substrate's ability to evolve safely. Operational work that lands before these mechanisms exists will not have the audit trail it needs to calibrate.

2. **Surface section B.6 (Karrigan integration hook) explicitly to David.** Three pre-arrival decisions — principal-parameter refactor (Fix 15), reserved Karrigan Actor modifier row, independent vs Atlas-routed approval surface — should be made before Karrigan ships, not retrofitted after.

3. **Surface section B.5 (router as skill, Fix 19) as the load-bearing Phase 1 keystone.** The router is named in three canonical files but doesn't exist. Without it, the substrate is honor-system and the audit hooks (SCHEMA §6) have no consumer.

4. **Note Atlas's recommendation on minimum-viable feedback loops** (Part B opening): build the cheapest version of each governance loop first, let observation drive investment, do not build the comprehensive review apparatus speculatively.

## What this doc is NOT

Not an approval. Not a fix. Not a plan with dates. It's a pointer.

The proposal itself (Part A + Part B) is the next surface for David's approval cycle. Karrigan's job here is to make sure Part B doesn't get lost behind the more visceral 19-finding fix list in Part A.

---

**One-line summary:** Static fixes for the v0.1 substrate are necessary but not sufficient; the dynamic governance mechanisms in Part B are what make the substrate able to evolve without re-drifting. Karrigan to surface this early.
