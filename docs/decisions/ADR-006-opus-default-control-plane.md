# ADR-006: Opus-default control plane, Sonnet-delegated execution

**Date:** 2026-05-17
**Status:** Accepted
**Deciders:** David Izzard

## Context

ADR-002 moved the daily driver to Claude Pro/Max OAuth — a flat
subscription, not per-call metered billing. SOUL.md §5 ("Cost-aware.
Sonnet-class only … Never load Opus without David's explicit
approval") and its echoes in the root README and the Atlas identity
record were written against the prior per-call pricing model, where
Opus carried a ~5x marginal dollar cost. Under the ratified OAuth
path that marginal dollar cost is ≈ $0; the real constraint is the
5-hour rolling rate limit (ADR-002, "Rate limits are tolerable").

The "Sonnet-only, Opus-by-exception" rule therefore optimizes a cost
variable that is now near-zero, at the expense of the control plane's
judgment quality. It also created recurring per-session approval
ceremony (the §5 Opus ritual) and an internal contradiction:
action-map.md already states cost is measured "beyond Anthropic's
flat subscription," while SOUL.md §5 still asserted a per-call cost
frame. Delegated subagents were runtime-verified on 2026-05-17 to
execute on Sonnet 4.6 via `delegation.model`, confirming a native,
no-cost split already exists between control-plane and bounded
execution.

## Decision

Atlas, as the DavidOS control plane, defaults to Opus-class for
high-judgment reasoning. Bounded, well-specified execution is
delegated to Sonnet-class subagents. Sessions known in advance to be
execution-heavy may be deliberately launched on Sonnet-class. No
automated model router (LiteLLM, OpenRouter routing, custom gateway)
is introduced for v1. Model class is autonomy-invariant: it never
widens tool permissions, approval intensity, write authority, or
external-action authority.

## Rationale

- **Sonnet-default Atlas considered.** Rejected: the control plane
  would silently under-reason on structural decisions and cannot
  self-detect the miss from inside Sonnet; the cost saving it buys is
  ≈ $0 under OAuth.
- **Automated router considered.** Rejected: no evidence of need,
  reopens ADR-002's paused-OpenRouter decision, adds infra and
  failure surface — overengineering at MVP stage.
- **Primary factor.** At foundation stage DavidOS sessions are
  judgment-dominant; maximizing control-plane judgment is the
  highest-leverage variable and the cost objection is void.
- **Cost / risk trade-off.** Accepts higher rate-limit budget
  consumption on long sessions in exchange for full-judgment
  reasoning; mitigated by delegation and the ADR-002 hot-swap.
- **Reversibility.** Fully reversible — a one-line SOUL.md §5 revert
  plus identity-record/README reconcile; no infrastructure created.

## Consequences

- SOUL.md §5, the Atlas identity record, and the root README are
  reconciled to this policy (this ADR's companion edits, same write).
- The per-session Opus-approval ritual in the
  davidos-session-operations skill §3 becomes obsolete and must be
  updated as a downstream follow-on (not part of this change).
- The Hermes profile already defaults to Opus; no Hermes config
  change is required.
- Cron jobs must continue to set `model` explicitly (the
  creation-time pinning footgun is unchanged by this ADR).

## Re-evaluation triggers

- Rate limits hit during normal (non-edge) daily-driver use in
  roughly ≥30% of sessions over a ~5–10 session window (this also
  satisfies ADR-002's existing re-evaluation trigger).
- A genuine non-Anthropic or high-throughput-automation need emerges
  (ADR-002 trigger).
- The auth path changes away from flat-subscription OAuth, restoring
  a per-call cost model.

Default review window: 90 days unless triggers fire first.

## Related

- ADR-002 — Anthropic OAuth over API key. ADR-006 supersedes **only
  the model-policy / cost-reasoning portion** of ADR-002; ADR-002's
  auth decision (Claude Pro/Max OAuth as daily driver) stands
  unchanged.
- SOUL.md §5 — amended in the companion edit of this same write.
- `docs/atlas/identity/atlas-agent-record.json` — model field
  reconciled in the companion edit.
