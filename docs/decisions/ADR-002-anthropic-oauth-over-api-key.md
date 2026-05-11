# ADR-002: Anthropic OAuth (Claude Pro/Max) over API key for daily driver

**Date:** 2026-05-11
**Status:** Accepted
**Deciders:** David Izzard

## Context

Originally on OpenRouter (key `sk-or-v1-a21fbacc...d3d`) with provider routing pin (`extra_body: provider: order: ["Anthropic"]`). OpenRouter Logs showed every recent gateway-routed call going through Amazon Bedrock at $0.03–$0.10/call despite the pin. Bedrock routing was unpredictable and created cost surprises.

We decided to switch off OpenRouter and go direct to Anthropic. Two auth options:

1. **API key** — `sk-ant-...`, metered per call (~$3/M input, ~$15/M output, ~$0.05/typical call), backed by a topped-up balance with auto-reload
2. **Claude Pro/Max OAuth** — flat subscription, no per-call metering, subject to 5-hour rolling rate limits

## Decision

Adopt Claude Pro/Max OAuth as the daily-driver auth path. Keep `ANTHROPIC_API_KEY` configured in `.env` as a dormant fallback.

## Rationale

- **Cost certainty.** Subscription is flat; no anxiety about runaway sessions.
- **Existing entitlement.** David already has a Claude subscription; no incremental spend.
- **Income-constrained context.** On unemployment with ~$50k runway, foundation-first strategy. Predictable costs over metered.
- **Rate limits are tolerable.** Heavy sessions might hit Pro 5-hour caps; the fallback (hot-swap to API key via `hermes auth add anthropic`) takes <2 minutes.
- **Reversible.** API key path remains fully configured and tested. Switching costs are near zero.

## Consequences

- OpenRouter paused. Re-add when multi-provider routing is genuinely needed (e.g., non-Anthropic models, fallback automation).
- API balance ($15 with auto-reload at $5) sits dormant. Acceptable as insurance.
- Need to document the hot-swap procedure so a future rate-limit hit doesn't become a session-stopper.

## Re-evaluation triggers

- Rate limits hit repeatedly during normal daily-driver use (not edge-case heavy sessions)
- A use case emerges requiring high-throughput automation that subscription tier can't sustain
- Anthropic OAuth flow becomes unreliable or unsupported by Hermes

## Hot-swap procedure (rate limit fallback)

```bash
hermes auth add anthropic
# Choose API key option, paste sk-ant-... from .env
# Restart gateway
```

## Related

- ADR-001 — Adopt hermes-workspace
- ADR-003 — Paperclip frozen, Atlas as memo library
