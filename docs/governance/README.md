# DavidOS Governance Tree

**Status:** Orientation document for `docs/governance/`. Created 2026-05-17.

> **GIP DIRECTION RATIFIED — IMPLEMENTATION NOT YET BUILT.** The Governed
> Intent Protocol *direction* is ratified by
> [ADR-005](../decisions/ADR-005-governed-intent-protocol.md) (2026-05-17,
> L1 Full per [ADR-004](../decisions/ADR-004-workspace-native-approval-mechanism.md);
> indexed in `docs/decisions/approvals-log.md` entries R1-R6). The GIP spec (`gip-spec.md`) is built and committed;
> the registries, manifests, and Decision Protocol skill remain **later
> lifecycle stages,
> not yet built and each separately gated**. Do not
> treat the absence of those artifacts as approval to implement them
> ad hoc — follow the lifecycle below.

---

## What this tree is

`docs/governance/` is the canonical home for the DavidOS governance line:
the Governed Intent Protocol (GIP), the context-governance layer, and the
registries/manifests that will implement them.

It is deliberately a **separate tree from `docs/audits/`**. Audit-prep
artifacts (e.g. `docs/audits/preparation/2026-05-14-atlas-comprehensive-
fix-and-governance-proposal.md`) are byproducts of reviewing the v0.1
substrate. Governance is foundational architecture, not an audit
byproduct, and is filed accordingly.

## Lifecycle (artifact classes)

Governance moves through four distinct artifact classes. Each has a
different home and a different approval surface:

| Class | Lives in | Approval |
|---|---|---|
| **Proposal / spec** | `docs/governance/proposals/`, later `docs/governance/gip-spec.md` | Drafting is an Atlas-MAY action (ADR-004); placement is a repo write |
| **Architecture decision** | `docs/decisions/ADR-005-*.md` + a line in `docs/decisions/approvals-log.md` | L1 Full per action-map Cat 17 |
| **Implementation artifact** | `docs/governance/registries/`, `docs/governance/manifests/`, the Decision Protocol skill in the Hermes profile | Per action-map category |
| **Source-of-truth capture** | this README, the approvals-log | L2 / L1 Light |

The flow: **proposal → ADR (decision) → spec → registries → manifests →
Decision Protocol skill**. A document does not advance to the next stage
until the prior stage's approval has landed in `approvals-log.md`.

## Core principle: repo is the audit/change substrate, not the governance brain (C5)

GitHub / the repo is where changes and decisions are **recorded and
audited** — it is the durable change and audit substrate. It is **not**
the entity that makes governance decisions. Governance decisions are made
by the Decision Protocol (control plane) and ratified by David via
ADR-004. The repo's job is to make those decisions durable, diffable, and
auditable — nothing more. No automation in the repo (CI, hooks, bots) may
act as a decision-maker.

## Current contents

- `anti-goals.md` — the overbuild-prevention fence. What DavidOS will
  deliberately NOT build now. Read this before proposing any new build.
- `proposals/2026-05-17-mv-gip-proposal.md` — the Minimum Viable Governed
  Intent Protocol proposal (C1–C5 incorporated). **Direction ratified by
  ADR-005 (2026-05-17); implementation stages still separately gated.**
- `gip-spec.md` — the operator-usable GIP implementation reference.
  Consolidates the ADR-005-ratified direction by pointer; introduces no
  design changes. **Lifecycle position: proposal → ADR → spec ✓;
  registries next.**

## What is intentionally NOT here yet

ADR-005, registries (agent / substrate), manifests, the Decision Protocol
skill, validators, action-map / modifier fixes, and any tool integration.
These are later lifecycle stages, gated on approvals that have not been
given. Their absence is deliberate, not an omission.
