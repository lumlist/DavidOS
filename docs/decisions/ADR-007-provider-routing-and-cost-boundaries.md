# ADR-007: Provider Routing and Cost Boundaries

**Date:** 2026-05-28
**Status:** Accepted
**Deciders:** David Izzard

## Context

FastDraft #2 was paused after Hermes/Atlas was found to be drawing from
Anthropic extra-usage / API-adjacent routes rather than staying inside the
intended subscription-covered lane. The immediate risk was not model
quality; it was silent provider/billing drift.

David's policy decision is capability-maximizing, subscription-first
routing:

- Use the smartest model appropriate for the judgment or task complexity.
- Provider selection must stay inside intended subscription-covered lanes
  by default.
- API / extra-usage spend is exception-only and requires explicit David
  approval before execution.

This narrows ADR-006. ADR-006 established an Opus-default control-plane
posture under the then-assumed Anthropic Max / OAuth subscription frame.
That model-quality principle remains useful, but its provider/cost posture
must not be read as permission for Hermes/Atlas to use Anthropic API,
Anthropic extra usage, or any other billable provider route by default.

## Decision

DavidOS adopts capability-maximizing, subscription-first provider routing.

"Best model" means the best model available inside the approved billing
lane for the relevant surface. It does not mean "any technically available
model" and does not authorize silent fallback to API-billed or extra-usage
routes.

Provider routing defaults to verified or intended subscription-covered
lanes. If a route cannot be verified as subscription-covered, it is
unavailable by default until David explicitly approves an exception.

Hermes/Atlas uses the intended subscription-covered OpenAI/Codex route by
default. If future billing-surface evidence shows OpenAI/Codex routing is
not subscription-covered as intended, Hermes/Atlas pauses high-token work
and provider routing is remediated before continuing.

Hidden fallback routes are not acceptable. Provider routing must be
documented in `docs/operations/provider-routing-register.md`.

Provider verification must include the main model route, auxiliary routes,
compression, web extraction, delegation, fallback providers, credential
pools, profile env files, and process env names. Verifying only the main
model route is insufficient.

## Routing table

| Surface | Default route | Model / class | Billing lane | Status |
|---|---|---|---|---|
| Hermes/Atlas | OpenAI/Codex | GPT-5.5 or best available OpenAI/Codex model | Intended subscription-covered OpenAI/Codex route | Active after remediation |
| Codex/Ari | OpenAI/Codex | Best available OpenAI/Codex model appropriate to task | Intended subscription-covered OpenAI/Codex route | Target route |
| Claude Code | Anthropic via claude.ai OAuth | Best appropriate Claude model available under Max | Anthropic Max subscription via claude.ai OAuth | Allowed for Claude Code |
| Ruflo | Anthropic via Claude Code | Best appropriate Claude model available through Claude Code | Anthropic Max subscription via Claude Code | Pending final verification |
| Gemini / AI Studio / NotebookLM | Google AI Pro surfaces | Best appropriate Google model available under subscription | Google AI Pro subscription lane | Pending route-specific verification before automated use |
| Perplexity | Perplexity Pro / manual | Best appropriate Perplexity model available under Pro/manual use | Perplexity Pro / manual subscription lane | API route requires exception gate |
| Anthropic API / extra usage | Forbidden for Hermes/Atlas by default | n/a | API / extra-usage spend | Not allowed without explicit exception approval |

## Fallback hierarchy

For Hermes/Atlas and other automated agent routes:

1. Primary: intended subscription-covered OpenAI/Codex route.
2. Secondary: Google/Gemini top model only after route-specific
   verification confirms it can be used through David's Google AI Pro /
   subscription-covered lane without paid API / extra usage.
3. Safety fallback: disable the specific route or workflow if no verified
   subscription-safe route is available.
4. Forbidden fallback: Anthropic API, Anthropic extra usage, Perplexity
   API, Google paid API, OpenAI API, or any unapproved API-billed /
   extra-usage provider route.

## Exception gate

Any API / extra-usage spend requires explicit David approval before
execution.

The approval request must state:

1. Provider/model.
2. Reason the subscription route is insufficient.
3. Expected cost/risk.
4. Cap or stopping condition.
5. Reversibility.
6. Explicit request for David approval before execution.

Without that approval, the route is unavailable.

## Current Hermes/Atlas remediation evidence

As of 2026-05-28, the Atlas Hermes profile has been remediated so active
runtime/auth paths use OpenAI/Codex only:

- Main Hermes/Atlas route:
  - provider: `openai-codex`
  - model: `gpt-5.5`
  - base_url: `https://chatgpt.com/backend-api/codex`
- `auxiliary.web_extract`:
  - provider: `openai-codex`
  - model: `gpt-5.5`
  - base_url: `https://chatgpt.com/backend-api/codex`
- `auxiliary.compression`:
  - provider: `openai-codex`
  - model: `gpt-5.5`
  - base_url: `https://chatgpt.com/backend-api/codex`
- `delegation`:
  - provider: `openai-codex`
  - model: `gpt-5.5`
  - base_url: `https://chatgpt.com/backend-api/codex`
- `fallback_providers`: `[]`
- Atlas auth provider keys: `openai-codex` only.
- Atlas credential pool keys: `openai-codex` only.
- Atlas profile `.env`: absent.
- Current process environment: no `ANTHROPIC*` / `CLAUDE*` variable names.
- No active Atlas runtime/auth route points to Anthropic, Claude, or
  `https://api.anthropic.com`.

This evidence verifies that Hermes/Atlas is Anthropic-free by default at
the Atlas profile/runtime-auth layer. It does not by itself prove exact
OpenAI subscription billing treatment; the OpenAI/Codex route is therefore
described as the intended subscription-covered OpenAI/Codex route unless
and until billing-surface evidence proves the exact treatment.

## Relationship to ADR-006

ADR-007 narrows ADR-006 only for provider-routing and cost-boundary
posture.

ADR-006 remains active for:

- model-class invariance;
- governance-authority boundaries;
- the principle that model intelligence does not widen tool permissions,
  approval intensity, write authority, or external-action authority.

ADR-007 supersedes any reading of ADR-006 that would allow Hermes/Atlas to
default to Anthropic API, Anthropic extra usage, or any unverified
API-billed provider route for control-plane work.

## Consequences

- Capability maximization remains the goal, but only inside approved
  billing lanes.
- Provider route is now a governance/cost boundary, not a purely technical
  preference.
- Hidden fallback routes are prohibited.
- Provider verification must include main model route, auxiliary routes,
  compression, web extraction, delegation, fallback providers, credential
  pools, profile env files, and process env names. Verifying only the main
  model route is insufficient.
- If billing route cannot be verified, the route is unavailable by default.
- If future billing evidence shows the OpenAI/Codex route is not
  subscription-covered as intended, Hermes/Atlas pauses high-token work and
  provider routing is remediated before continuing.
- Provider routing must be tracked in
  `docs/operations/provider-routing-register.md`.
- FastDraft and other high-token workflows must not resume from a paused
  provider-routing state until runtime/auth route verification is clean.
- API / extra-usage spend requires an explicit exception gate and David's
  approval before execution.

## Re-evaluation triggers

Re-evaluate this ADR if any of the following occur:

- OpenAI/Codex billing-surface evidence shows the route is not
  subscription-covered as intended.
- Hermes/Atlas gains or changes provider credentials.
- Hermes changes provider resolution, fallback behavior, or credential pool
  semantics.
- A high-token task requires a model unavailable inside the approved
  subscription lane.
- Ruflo's final route verification changes its billing/provider posture.
- Google/Gemini automated use becomes desirable and needs route-specific
  subscription verification.
- Perplexity API use becomes desirable.
- Anthropic API / extra usage is proposed for Hermes/Atlas.

Default review window: 2026-08-28 unless triggers fire first.

## Related

- ADR-002 — Anthropic OAuth over API key. Still relevant for Claude Code /
  Anthropic Max subscription routing, but not a default Hermes/Atlas API
  route.
- ADR-004 — Workspace-native approval mechanism. API / extra-usage spend
  uses an explicit approval gate and is logged in
  `docs/decisions/approvals-log.md`.
- ADR-006 — Opus-default control plane, Sonnet-delegated execution.
  Narrowed by this ADR only for provider-routing and cost-boundary posture.
- `docs/operations/provider-routing-register.md` — operational register for
  current provider routes, billing lanes, verification state, and blockers.
