# Architecture

> **Status: stub.** Created 2026-05-11 as part of the post-migration tidy. To be expanded with diagrams and component-level docs as the system evolves.

## Current stack

```
┌─────────────────────────────────────────────────────────────────────┐
│  Browser (local laptop)                                              │
│  └── localhost:3000 (via SSH tunnel)                                 │
└───────────────────────┬──────────────────────────────────────────────┘
                        │ ssh -L 3000:127.0.0.1:3000 hermes@VPS
                        ▼
┌─────────────────────────────────────────────────────────────────────┐
│  VPS  (DigitalOcean, 159.223.166.217)                                │
│                                                                      │
│  ┌──────────────────────────────┐  ┌─────────────────────────────┐  │
│  │ hermes-workspace  :3000      │──│ Hermes Gateway   :8642      │  │
│  │ (multi-agent web UI)         │  │ (agent runtime, REST)       │  │
│  └──────────────────────────────┘  └────────────┬────────────────┘  │
│                                                  │                   │
│                                                  ▼                   │
│                                    ┌─────────────────────────────┐  │
│                                    │ Anthropic API               │  │
│                                    │ Claude Pro/Max OAuth        │  │
│                                    │ Model: claude-sonnet-4-6    │  │
│                                    └─────────────────────────────┘  │
│                                                                      │
│  ┌──────────────────────────────┐                                    │
│  │ Hermes Dashboard :9119       │  (telemetry, status)               │
│  └──────────────────────────────┘                                    │
└─────────────────────────────────────────────────────────────────────┘
```

## Services on the VPS

| Service | Port | Started by | Purpose |
|---|---|---|---|
| hermes-workspace UI | 3000 | `cd ~/hermes-workspace && pnpm dev` | Multi-agent web UI |
| Hermes gateway | 8642 | `hermes gateway run` | Agent runtime, OpenAI-compatible API |
| Hermes dashboard | 9119 | `hermes dashboard` | Status and telemetry |

Each runs in its own SSH session. The gateway and dashboard are loopback-only by default.

## Auth

LLM auth is **Claude Pro/Max OAuth** (subscription, flat-rate). The API key `ANTHROPIC_API_KEY` is configured as a dormant fallback in `/home/hermes/.hermes/.env` for rate-limit overflow. See [ADR-002](../decisions/ADR-002-anthropic-oauth-over-api-key.md).

## Repos

The VPS hosts a working clone of `lumlist/DavidOS` at `/home/hermes/projects/personal-ai-workspace/`. Other DavidOS-ecosystem repos (`familyAI`, `DavidAIStory`) are not yet cloned to the VPS — they will be when work resumes on them.

## Decisions that shape this architecture

- [ADR-001](../decisions/ADR-001-adopt-hermes-workspace.md) — Adopt hermes-workspace over custom UI build
- [ADR-002](../decisions/ADR-002-anthropic-oauth-over-api-key.md) — Anthropic OAuth over API key for daily driver
- [ADR-003](../decisions/ADR-003-paperclip-frozen-atlas-memo-library.md) — Paperclip frozen; Atlas as memo library

## Open

- Approval mechanism (Workspace-native replacement for Paperclip `[APPROVAL: <kind>]` tags) — pending ADR-004
- Multi-VPS or replicated deploy — not needed until iZZi customer one ships
- Monitoring/alerting beyond Hermes dashboard — TBD
