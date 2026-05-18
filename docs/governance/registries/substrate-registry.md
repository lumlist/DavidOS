# Substrate Registry

**Status:** Implementation artifact. Created 2026-05-18.
**Approval class:** L1 Light (per ADR-005 lifecycle; `approvals-log.md`).

> **GIP DIRECTION RATIFIED — THIS IS INVENTORY, NOT A GRANT.** The Governed
> Intent Protocol direction is ratified by
> [ADR-005](../../decisions/ADR-005-governed-intent-protocol.md) (2026-05-17,
> L1 Full per [ADR-004](../../decisions/ADR-004-workspace-native-approval-mechanism.md);
> `../../decisions/approvals-log.md` R1-R6). This registry is the next
> lifecycle stage after the GIP spec
> ([governance/README.md](../README.md) L42-44). Manifests and the
> Decision Protocol skill remain later, separately-gated stages.

---

## What this registry is

This is the **inventory of the T1–T6 tool/substrate tier hierarchy** —
what executes or serves work, at which tier, in which decision direction,
and whether it has a real adapter. It is governance/routing inventory, not
a permission, credential, or manifest layer. A registry row **grants
nothing**.

Caps in force: anti-goals.md #7 (≤ 6 fields + tier; not an
identity/credential/CRM layer), #6 (exactly one real adapter — Hermes).

## Invariants preserved (gip-spec §10; MV-GIP proposal §11)

- **Hermes is the only real v1 adapter.** All other rows: `adapter = none`.
- **T3/T4 are invoked through T2 (Hermes), never directly.** Claude Code,
  Codex, and Ruflo have no own adapter seam.
- **T5/T6 make no decisions.** NotebookLM, Obsidian, and the future UI have
  `decision_direction = none`.
- **Decisions flow down the tier hierarchy only; results/audit flow up. No
  substrate produces a Decision. T4 can never short-circuit to T1.**

## Schema (exactly 6 fields)

| Field | Meaning | Allowed values |
|---|---|---|
| `id` | substrate handle | identifier string |
| `tier` | position in the T1–T6 hierarchy | `T1`–`T6` |
| `role` | one-line label | free text |
| `decision_direction` | who emits vs. receives Decisions | `emit` \| `receive-only` \| `none` |
| `adapter` | real v1 enforcement adapter? | `REAL` (Hermes only) \| `none` \| `n/a` |
| `status` | inventory state | `active` \| `unimplemented` |

## Entries

| id | tier | role | decision_direction | adapter | status |
|---|---|---|---|---|---|
| DavidOS/Atlas | T1 | control plane | emit | n/a | active |
| Hermes | T2 | execution/orchestration | receive-only | REAL | active |
| Claude Code | T3 | build/dev tool (invoked through T2) | receive-only | none | unimplemented |
| Codex | T3 | build/dev tool (invoked through T2) | receive-only | none | unimplemented |
| Ruflo | T4 | future bounded multi-agent build-execution layer (NOT governance brain; invoked through T2) | receive-only | none | unimplemented |
| NotebookLM | T5 | knowledge/research resource | none | none | unimplemented |
| Obsidian | T5 | knowledge/research resource | none | none | unimplemented |
| Future UI | T6 | reader / operator surface (makes no decisions) | none | none | unimplemented |

## How the Decision Protocol consumes this (pointer only — not built here)

The Decision Protocol skill (gip-spec §6, §10 — a Hermes-profile skill,
not authored here) will resolve an envelope's `substrate` against this
registry to validate it is a known substrate and enforce the tier-aware
decision-direction invariant. This registry is input to that decision,
never authority.

## Pointers

- [ADR-005 — Governed Intent Protocol](../../decisions/ADR-005-governed-intent-protocol.md)
- [gip-spec.md](../gip-spec.md) — §6 decision contract, §10 tier hierarchy, §8 invariants
- [anti-goals.md](../anti-goals.md) — #6 one real adapter, #7 registry cap
- [governance/README.md](../README.md) — lifecycle
