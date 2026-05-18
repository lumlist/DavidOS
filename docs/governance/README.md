# DavidOS Governance Tree

**Status:** Orientation document for `docs/governance/`. Created 2026-05-17.

> **GIP DIRECTION RATIFIED — v1 CORE IMPLEMENTATION SHIPPED; FOLLOW-ONS
> GATED.** The Governed Intent Protocol *direction* is ratified by
> [ADR-005](../decisions/ADR-005-governed-intent-protocol.md) (2026-05-17,
> L1 Full per [ADR-004](../decisions/ADR-004-workspace-native-approval-mechanism.md);
> indexed in `docs/decisions/approvals-log.md` entries R1-R6). The GIP spec
> (`gip-spec.md`), the agent/substrate registries, the v1 project manifest,
> and the Decision Protocol skill (Hermes-profile-local, audit-logged in
> the repo) are all built, committed/recorded, and pushed. Further GIP
> work — additional manifest types, the decision-log observability spine,
> validators, action-map / modifier fixes (incl. R4), tool integrations,
> /goal adoption, and any agents or workflows — remains **later lifecycle
> stages, not yet built and each separately gated**. Do not treat the
> absence of those remaining artifacts as approval to implement them ad
> hoc — follow the lifecycle below.

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
  design changes. **Lifecycle position: proposal → ADR → spec ✓ →
  registries ✓ → manifests ✓ → Decision Protocol skill ✓ (GIP v1 core
  chain shipped; follow-ons gated).**
- `registries/agent-registry.md`, `registries/substrate-registry.md` — the
  GIP agent and substrate registries. Inventory only — no grants,
  manifests, activation, or authority. Created/committed/pushed 2026-05-18
  (commit `2d913ea`; approvals-log 2026-05-18, L1 Light under ADR-005).
  **Lifecycle position: registries ✓.**
- `manifests/project-build-loop.manifest.md`, `manifests/README.md` — the
  v1 project manifest (the permission layer) and its orientation guard. A
  standing, bounded, reversible build-loop capability grant:
  principals=Atlas only, substrate=Hermes only, ceilings, non-grantable
  set always re-gates, /goal named but not enabled.
  Created/committed/pushed 2026-05-18 (commit `4e7c4bc`; approvals-log
  2026-05-18, L1 Full under ADR-005). **Lifecycle position: manifest ✓.**
- Decision Protocol skill — `davidos-decision-protocol`, authored
  **Hermes-profile-local** (NOT a repo file, per gip-spec §13 / C5):
  `~/.hermes/profiles/atlas/skills/devops/davidos-decision-protocol/`.
  Operationalizes gip-spec §6 (envelope + registries + manifest +
  action-map/modifiers/SCHEMA + §8 invariants → structured Decision;
  decide-only, no execution). Creation audit-logged in the repo:
  approvals-log 2026-05-18, L1 Full under ADR-005, commit `e3bd474`.
  **Lifecycle position: Decision Protocol skill ✓.**

## What is intentionally NOT here yet

The decision-log observability spine (`decision-log.md` — named by the v1
manifest's `decision_log_target` but deliberately not created; gip-spec
§11 schema only), additional manifest types (workflow / skill / script /
substrate — schema-defined, unpopulated in v1), validators, action-map /
modifier fixes (including the R4 spend/money + legal/privacy category
gap), and any tool integration. These are later lifecycle stages, gated on
approvals that have not been given. ADR-005, the agent/substrate
registries, the v1 project manifest, and the Decision Protocol skill are
no longer pending — they are built; their prior listing here is removed.
/goal is named as a manifest-bound future surface but is **not adopted or
enabled**. No agents or workflows are created — Karrigan/Hustler/Jeff/Steve
remain named-future stubs with zero authority. The remaining absences are
deliberate, not an omission.
