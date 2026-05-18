# DavidOS Manifests — the Permission Layer

**Status:** Orientation document for `docs/governance/manifests/`. Created 2026-05-18.

> **GIP DIRECTION RATIFIED — MANIFESTS ARE THE PERMISSION LAYER.** Ratified
> by [ADR-005](../../decisions/ADR-005-governed-intent-protocol.md). This
> tree is the lifecycle stage after the registries. The Decision Protocol
> skill that consumes manifests is a later, separately-gated stage and is
> not built yet.

---

## What a manifest is

A manifest is a small declared-context file carrying a **scoped capability
grant**. The grant IS the pre-authorization — the generalized form of the
cron "approve-the-actor-once" pattern. A manifest answers: *for this
bounded context, which principals may do which things, on which paths, up
to which ceilings, without re-asking each time.* (gip-spec §7.)

## Registries vs. manifests

- **Registries** (`../registries/`) are **inventory**: who and what exist
  (agents, substrates). A registry row grants nothing.
- **Manifests** (here) are **authority**: what a principal may actually do
  in a bounded context. Only a manifest can pre-authorize.

Registry = noun list. Manifest = verb grant. The Decision Protocol consumes
both; only the manifest carries authority.

## No manifest means no standing grant

If no manifest authorizes an action, there is **no pre-authorization** —
the action re-gates through the normal approval surface (ADR-004). Absence
of a manifest is never implicit permission.

## Non-grantable actions always re-gate

Some actions can never be pre-authorized by any manifest: external
sends/outreach, spend / money movement / account creation, legal/privacy
conclusions, identity/structural edits (SOUL.md, ADRs, autonomy files,
registries, manifests), Hermes config changes, memory writes (elevated
per gip-spec §7 C4), personal/health/financial-sensitive data actions,
agent activation, workflow creation, /goal runs or adoption, and the
creation or widening of any capability grant. These always re-gate at the
rung the policy kernel sets (L1 Light, L1 Full, or L0). No agent — Atlas
included — may author or widen a grant; only David's logged L1 Full does
(gip-spec §8).

## The Decision Protocol skill is later and separately gated

The skill that reads manifests and emits Decisions is authored in the
Hermes profile (gip-spec §13), after the manifest is written, committed,
and pushed. It is a separate approval gate. Until it exists, a manifest is
a durable declared grant with no automated consumer.

## /goal is not enabled

`/goal` is a Hermes future command surface (R3). It is named as a
manifest-bound future surface only. It is **not enabled, not adopted, and
cannot run** under any current manifest. Future /goal use is a separate
L1 Full, manifest-bound approval.

## Current contents

- `project-build-loop.manifest.md` — the v1 project manifest: the standing,
  bounded, reversible build-loop capability grant for Atlas on Hermes.
  Created 2026-05-18 (approvals-log, L1 Full under ADR-005). Review/expiry
  2026-08-17.

## What is intentionally NOT here yet

Additional manifest types (workflow / skill / script / substrate) are
schema-defined by gip-spec §7 but **deliberately unpopulated** in v1
(gip-spec §7: "v1 populates exactly ONE manifest"). The Decision Protocol
skill, the decision-log spine artifact (`decision-log.md` — named by the
v1 manifest's `decision_log_target` but **not created**), validators, and
any consumer tooling are later, separately-gated stages. Their absence is
deliberate.

## Pointers

- [gip-spec.md](../gip-spec.md) — §7 manifest model, §8 invariants
- [ADR-005](../../decisions/ADR-005-governed-intent-protocol.md)
- [anti-goals.md](../anti-goals.md) — overbuild fence
- [governance/README.md](../README.md) — lifecycle
