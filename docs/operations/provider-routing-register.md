# Provider Routing Register

**Date:** 2026-05-28
**Policy authority:** [ADR-007: Provider Routing and Cost Boundaries](../decisions/ADR-007-provider-routing-and-cost-boundaries.md)

## Purpose

This register operationalizes ADR-007. It tracks provider routes, intended
models/classes, auth mechanisms, billing lanes, verification state,
blockers, and next checks for DavidOS agent/tool surfaces.

No secret values belong in this file.

The standing policy is capability-maximizing, subscription-first routing:
use the smartest appropriate model for the judgment/task complexity, but
keep provider selection inside verified or intended subscription-covered
lanes by default. API / extra-usage spend is exception-only.

OpenAI/Codex billing is described here as the **intended
subscription-covered OpenAI/Codex route** unless and until billing-surface
evidence proves the exact subscription treatment.

## Verification Standard

Provider verification must include:

- main model route;
- auxiliary routes;
- compression;
- web extraction;
- delegation;
- fallback providers;
- credential pools;
- profile env files;
- process env names.

Verifying only the main model route is insufficient.

For Hermes/Atlas, a route is not considered clean if any active runtime
config, auth provider, credential pool, fallback provider, profile env
file, or process env name exposes Anthropic, Claude, API-billed, or
extra-usage routing not explicitly approved by David.

## Exception Gate Summary

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

## Route Register

| Surface / agent / tool | Intended provider | Intended model/class | Auth mechanism | Billing lane | API/extra usage allowed by default? | Current verification status | Last verified | Evidence / notes | Blocker / next check |
|---|---|---|---|---|---|---|---|---|---|
| Hermes/Atlas main | OpenAI/Codex | GPT-5.5 or best available OpenAI/Codex model | Atlas Hermes profile `auth.json`; `active_provider: openai-codex` | Intended subscription-covered OpenAI/Codex route | No | Verified at Atlas profile/runtime-auth layer | 2026-05-28 | Main route verified as `openai-codex` / `gpt-5.5` / `https://chatgpt.com/backend-api/codex`; Atlas auth provider keys: `openai-codex` only; Atlas credential pool keys: `openai-codex` only; Atlas profile `.env` absent; process env has no `ANTHROPIC*` / `CLAUDE*` names; `fallback_providers: []` | Billing-surface proof of exact OpenAI subscription treatment still pending; if evidence contradicts intended subscription coverage, pause high-token work and remediate |
| Atlas `auxiliary.web_extract` | OpenAI/Codex | GPT-5.5 or best available OpenAI/Codex model | Atlas Hermes profile config + `openai-codex` auth | Intended subscription-covered OpenAI/Codex route | No | Verified at Atlas active runtime config layer | 2026-05-28 | `auxiliary.web_extract.provider: openai-codex`; `model: gpt-5.5`; `base_url: https://chatgpt.com/backend-api/codex`; `api_key` empty | Same OpenAI/Codex billing-surface caveat as Hermes/Atlas main |
| Atlas `auxiliary.compression` | OpenAI/Codex | GPT-5.5 or best available OpenAI/Codex model | Atlas Hermes profile config + `openai-codex` auth | Intended subscription-covered OpenAI/Codex route | No | Verified at Atlas active runtime config layer | 2026-05-28 | `auxiliary.compression.provider: openai-codex`; `model: gpt-5.5`; `base_url: https://chatgpt.com/backend-api/codex`; `api_key` empty | Same OpenAI/Codex billing-surface caveat as Hermes/Atlas main; compression must not fall back to Anthropic/API routes |
| Atlas delegation | OpenAI/Codex | GPT-5.5 or best available OpenAI/Codex model | Atlas Hermes profile config + `openai-codex` auth | Intended subscription-covered OpenAI/Codex route | No | Verified at Atlas active runtime config layer | 2026-05-28 | `delegation.provider: openai-codex`; `model: gpt-5.5`; `base_url: https://chatgpt.com/backend-api/codex`; `api_key` empty | Same OpenAI/Codex billing-surface caveat as Hermes/Atlas main; delegation must not fall back to Anthropic/API routes |
| Codex/Ari | OpenAI/Codex | Best available OpenAI/Codex model appropriate to task | Codex/OpenAI route used by Ari | Intended subscription-covered OpenAI/Codex route | No | Target route; not fully re-verified in this register gate | 2026-05-28 | FastDraft #2 Research Brief was written locally by Ari/Codex and verified separately; this row records intended provider policy, not a fresh billing-surface proof | Verify Ari/Codex auth and billing route by names/shapes before new high-token Ari work if route ambiguity appears |
| Claude Code | Anthropic via claude.ai OAuth | Best appropriate Claude model available under Max | Claude Code / claude.ai OAuth | Anthropic Max subscription via claude.ai OAuth | No API/extra usage by default | Previously accepted target route; not re-verified in this register gate | 2026-05-28 | Claude Code is allowed to use Anthropic Max via claude.ai OAuth; this does not authorize Hermes/Atlas Anthropic API use | Re-verify with `claude auth status` when Claude Code routing/billing matters |
| Ruflo | Anthropic via Claude Code | Best appropriate Claude model available through Claude Code | Ruflo via Claude Code | Anthropic Max subscription via Claude Code | No API/extra usage by default | Pending final verification | 2026-05-28 | Target route is Anthropic Max via Claude Code, not direct Anthropic API | Verify Ruflo execution path and billing/auth route before automated Ruflo use |
| Gemini / AI Studio / NotebookLM | Google AI Pro surfaces | Best appropriate Google model available under subscription | Google AI Pro / product UI or verified subscription-covered route | Google AI Pro subscription lane | No API/extra usage by default | Pending route-specific verification before automated use | 2026-05-28 | Google/Gemini is the secondary fallback only if verification confirms use through David's Google AI Pro / subscription-covered lane without paid API / extra usage | Do not use Google paid API keys or Gemini API unless explicit exception gate is approved |
| Perplexity | Perplexity Pro / manual | Best appropriate Perplexity model available under Pro/manual use | Perplexity Pro/manual surface | Perplexity Pro / manual subscription lane | No API usage by default | Policy route only; automated/API route not approved | 2026-05-28 | Perplexity is allowed as Pro/manual by default; Perplexity API requires exception gate | Do not use Perplexity API without explicit approval |
| Anthropic API / extra usage | None for Hermes/Atlas | n/a | n/a | API / extra-usage spend | No | Forbidden by default for Hermes/Atlas | 2026-05-28 | Atlas active runtime/auth paths contain no Anthropic provider, credential pool, fallback, profile env, process env, Claude route, or `https://api.anthropic.com` route after remediation | Any proposed Anthropic API / extra-usage use requires exception gate and explicit David approval |
| Google paid API | None by default | n/a | n/a | Paid API / extra-usage spend | No | Forbidden unless exception-approved | 2026-05-28 | Google/Gemini fallback must be Google AI Pro / subscription-covered; paid Google API is not an approved fallback | Any Google paid API use requires exception gate and explicit David approval |
| OpenAI API outside Codex route | None by default | n/a | n/a | Paid API / extra-usage spend | No | Forbidden unless exception-approved | 2026-05-28 | OpenAI/Codex route is intended subscription-covered; separate OpenAI API billing is not approved by default | Any OpenAI API use outside the Codex route requires exception gate and explicit David approval |

## Current Atlas remediation evidence

As of 2026-05-28, Hermes/Atlas active runtime/auth paths are verified as:

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

This verifies Atlas is Anthropic-free by default at the active
runtime/auth layer. It does not prove exact OpenAI subscription billing
treatment; OpenAI/Codex remains recorded as the intended
subscription-covered OpenAI/Codex route until billing-surface evidence
proves the exact treatment.

## Maintenance rule

Update this register whenever:

- a provider route changes;
- credentials are added, removed, or refreshed in a way that affects route
  availability;
- fallback behavior changes;
- billing-surface evidence changes the subscription/extra-usage judgment;
- a pending route is verified or rejected;
- an exception gate approves temporary API / extra-usage spend.

Do not record secret values in this file.
