# Agent Registry

**Status:** Implementation artifact. Created 2026-05-18.
**Approval class:** L1 Light (per ADR-005 lifecycle; `approvals-log.md`).

> **GIP DIRECTION RATIFIED — THIS IS INVENTORY, NOT A GRANT.** The Governed
> Intent Protocol direction is ratified by
> [ADR-005](../../decisions/ADR-005-governed-intent-protocol.md) (2026-05-17,
> L1 Full per [ADR-004](../../decisions/ADR-004-workspace-native-approval-mechanism.md);
> `../../decisions/approvals-log.md` R1-R6). This registry is the next
> lifecycle stage after the GIP spec
> ([governance/README.md](../README.md) L42-44). Manifests (the permission
> layer) and the Decision Protocol skill remain later, separately-gated
> stages.

---

## What this registry is — and is NOT

This is the **inventory of who may be named as a `principal`** in a
Governed Intent Envelope (gip-spec §4 field 2). It is a label-and-boundary
list for governance, routing, and audit.

It is **NOT**: an identity/SOUL layer, a credential store, a
relationship/CRM layer, a memory store, a permissions system, a manifest,
an activation mechanism, or an agent build. A registry row **grants
nothing**. Capability is granted only by a manifest (gip-spec §7), which is
not part of this artifact, and only David's logged L1 Full enacts a grant
(gip-spec §8 authority-expansion invariant). `status = named-future` is an
inventory state, never an activation.

Caps in force: anti-goals.md #7 (≤ 8 fields; no identity/credential/CRM
layer), #9 (Karrigan/Hustler/Jeff/Steve are named-future stubs only — no
per-agent build).

## Schema (exactly 8 fields)

| Field | Meaning | Allowed values |
|---|---|---|
| `id` | routing + log handle | identifier string |
| `role` | one-line UI/citation label | free text or `[unknown role]` |
| `primary_function` | what routing keys off to pick the agent | free text or `intent not yet captured` |
| `posture` | interaction style/cadence — orthogonal to authority; never a rung | `conversational` \| `advisory` \| `approval-disciplined` \| `(unset)` |
| `default_model_tier` | cost posture only | model-tier label or `(unset)` |
| `execution_authority` | authority-boundary primitive | `none` \| `bounded` \| `standard` |
| `allowed_tools_or_substrates` | routing + containment | substrate/tool list or `none` |
| `status` | inventory state — NOT activation | `active` \| `named-future` |

## Entries

| id | role | primary_function | posture | default_model_tier | execution_authority | allowed_tools_or_substrates | status |
|---|---|---|---|---|---|---|---|
| Atlas | Chief Systems Advisor | DavidOS control-plane reasoning & advisory | approval-disciplined | opus-default (ADR-006) | standard | hermes | active |
| Karrigan | input coach | [captured-intent] prompt / focus / UX coaching — see `docs/roadmap/2026-05-14-karrigan-intent-capture.md` (primary source; intent only, not authority) | (unset) | (unset) | none | none | named-future |
| Hustler | [unknown role] | intent not yet captured | (unset) | (unset) | none | none | named-future |
| Jeff | [unknown role] | intent not yet captured | (unset) | (unset) | none | none | named-future |
| Steve | future UI-agent (label reconciled from "Jobs" — commit 9cac8e3, approvals-log 2026-05-18) | intent not yet captured; deferred UI/operator-command-center domain per anti-goals.md #1 (do not design) | (unset) | (unset) | none | none | named-future |

## Zero-authority statement for named-future rows

Karrigan, Hustler, Jeff, and Steve are **named-future stubs only**. For
each: `execution_authority = none`, `allowed_tools_or_substrates = none`,
`status = named-future`. No manifest references them; they hold no tools,
no autonomy rung, no activation, no external-action authority, no memory
access. Karrigan's row points to a captured-intent primary source; that
intent is **not** converted here into authority or implementation. No role
or authority is invented for Hustler, Jeff, or Steve.

## How later stages consume this (pointers only — not built here)

- **Manifests** (gip-spec §7) will reference `id`s in
  `principals_allowed`; the registry is the closed vocabulary of who a
  manifest may name. The manifest carries the grant; this registry never
  does.
- **The Decision Protocol skill** (gip-spec §6, §13 — a Hermes-profile
  skill, not authored here) will resolve an envelope's `principal` against
  this registry to validate it is a known entity and read
  `posture`/tier as decision *inputs*, never as authority.

## Pointers

- [ADR-005 — Governed Intent Protocol](../../decisions/ADR-005-governed-intent-protocol.md)
- [gip-spec.md](../gip-spec.md) — §4 envelope, §6 decision contract, §7 manifest model, §8 invariants
- [anti-goals.md](../anti-goals.md) — #7 registry cap, #9 no per-agent build
- [governance/README.md](../README.md) — lifecycle
- [Karrigan intent capture](../../roadmap/2026-05-14-karrigan-intent-capture.md) — Karrigan primary-source intent (not authority)
