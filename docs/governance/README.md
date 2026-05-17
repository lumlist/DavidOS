# DavidOS Governance Tree

**Status:** Orientation document for `docs/governance/`. Created 2026-05-17.

> **NOT APPROVED ARCHITECTURE.** Nothing in this tree is in force until
> ADR-005 is created and the relevant `docs/decisions/approvals-log.md`
> entries are appended. Until then, every document here — including the
> MV-GIP proposal — is a **working draft awaiting David's L1 Full
> approval per [ADR-004](../decisions/ADR-004-workspace-native-approval-mechanism.md)**.
> Do not implement against these documents.

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
- `proposals/2026-05-17-mv-gip-proposal.md` — the working-draft Minimum
  Viable Governed Intent Protocol proposal (C1–C5 incorporated).
  **Awaiting ADR-005 + approvals-log entries before it is in force.**

## What is intentionally NOT here yet

ADR-005, registries (agent / substrate), manifests, the Decision Protocol
skill, validators, action-map / modifier fixes, and any tool integration.
These are later lifecycle stages, gated on approvals that have not been
given. Their absence is deliberate, not an omission.
