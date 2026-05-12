# Workspace Baseline Configuration

> **Status: initial baseline.** Created 2026-05-11. Update as configuration choices solidify with daily use.

The default configuration David applies to a fresh hermes-workspace install. Captured here so:
1. A re-install (or recovery from a corrupted state) is reproducible
2. Future iZZi customers can inherit a known-good starting point and customize from there

## Install reference

- Repo: [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) v2.3.0
- Local clone path on VPS: `/home/hermes/hermes-workspace/`
- Install steps captured in `~/hermes-workspace/README.md`

## Active config

### Identity

| Setting | Value | Notes |
|---|---|---|
| Workspace name | "Hermes Workspace" (default, not yet customized) | TBD whether to rename to "DavidOS" |
| User profile name | TBD | Set in Workspace → Profiles |
| Avatar | TBD | |

### Model and provider

| Setting | Value | Source |
|---|---|---|
| Provider | `anthropic` | `~/.hermes/config.yaml` |
| Base URL | `https://api.anthropic.com` | Same |
| Default model | `claude-sonnet-4-6` | Same |
| Auth method | Claude Pro/Max OAuth | [ADR-002](../decisions/ADR-002-anthropic-oauth-over-api-key.md) |
| `max_tokens` | 16000 | Increased from default to handle longer responses without 402 |
| API key fallback | `ANTHROPIC_API_KEY` in `~/.hermes/.env` (dormant) | Rate-limit overflow only |

### Gateway flags

| Setting | Value | Notes |
|---|---|---|
| `API_SERVER_ENABLED` | `true` | Required for Workspace UI to reach gateway |
| Gateway port | `8642` (loopback) | |
| Dashboard port | `9119` (loopback) | |
| Workspace UI port | `3000` (loopback) | Accessed via SSH tunnel |
| `API_SERVER_KEY` / `GATEWAY_ALLOW_ALL_USERS` | Not set | Loopback-only deploy; add when exposing externally |

### Theme and UI

| Setting | Value | Notes |
|---|---|---|
| Theme | Dark (default) | |
| Sidebar collapsed | No | |
| Mobile pairing | Not configured | |

### Agent roster

| Agent | Status | Config file |
|---|---|---|
| (none registered yet) | — | `docs/workspace/agents/` (to be created when first persona is registered) |

The Atlas agent record exists in archive form at [`docs/atlas/identity/atlas-agent-record.json`](../atlas/identity/atlas-agent-record.json) but is not registered as a runtime persona ([ADR-003](../decisions/ADR-003-paperclip-frozen-atlas-memo-library.md)).

## Session hygiene patterns

Workspace surfaces context-window warnings at ~40% usage. Patterns adopted:

- For substantive tasks, **start a fresh session** rather than reusing a long one
- Enable auto-compaction in Settings → Config as a safety net
- For long-running work, use the canonical session memo (`docs/sessions/NEXT-SESSION-OPEN.md`) as the durable handoff between Workspace sessions

## Re-install checklist

If Workspace needs to be reinstalled, the steps that worked on 2026-05-11:

1. `git clone https://github.com/outsourc-e/hermes-workspace ~/hermes-workspace`
2. `cd ~/hermes-workspace && pnpm install`
3. `pnpm approve-builds` (approve all four: esbuild, electron, winstaller, unrs-resolver)
4. Create `~/hermes-workspace/.env` with:
   ```
   HERMES_API_URL=http://127.0.0.1:8642
   HERMES_DASHBOARD_URL=http://127.0.0.1:9119
   ```
5. Ensure Hermes side: `API_SERVER_ENABLED=true` in `~/.hermes/.env`
6. Start three services in three SSH sessions: `hermes gateway run`, `hermes dashboard`, `cd ~/hermes-workspace && pnpm dev`
7. SSH-tunnel from laptop: `ssh -L 3000:127.0.0.1:3000 hermes@VPS`
8. Browse to `localhost:3000`
9. Authorize via Claude Pro/Max OAuth on first agent invocation

## Open

- Whether to rename Workspace from "Hermes Workspace" to "DavidOS"
- Whether to register Atlas as an always-available agent profile or keep memo-library pattern
- When to enable API key (`API_SERVER_KEY`) — only when exposing beyond loopback
- Whether to enable auto-compaction by default
