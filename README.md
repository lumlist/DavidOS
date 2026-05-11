# DavidOS

Personal AI operating system for David Izzard. Foundation layer for FamilyAI, iZZi Builder Services, and downstream projects.

## Current stack

| Layer | Tool |
|---|---|
| Daily driver UI | hermes-workspace (outsourc-e/hermes-workspace v2.3.0) |
| Agent runtime | Hermes v0.13.0 |
| LLM auth | Claude Pro/Max OAuth |
| Host | DigitalOcean VPS |
| Repos in scope | DavidOS, FamilyAI, DavidAIStory |

## Access

```bash
ssh -L 3000:127.0.0.1:3000 hermes@159.223.166.217
# then browse to localhost:3000
```

Three services run on the VPS in separate SSH sessions:

```bash
hermes gateway run                         # :8642
hermes dashboard                           # :9119
cd ~/hermes-workspace && pnpm dev          # :3000 (Workspace UI)
```

## Documentation map

- **`docs/sessions/NEXT-SESSION-OPEN.md`** — current state and next session entry points
- **`docs/sessions/submitted/`** — debriefs from completed sessions
- **`docs/atlas/`** — Atlas memo library (archive, not active runtime)
- **`docs/decisions/`** — Architecture Decision Records (ADRs)
- **`docs/architecture/`** — stack diagrams and infrastructure docs
- **`docs/workspace/`** — Workspace baseline configuration and patterns

## Operating principles

- iZZi customer-zero pattern: every config/architectural decision should be reusable across future iZZi AI Systems customers OR explicitly David-specific
- Sonnet-class only; no Opus without explicit approval
- Foundation-first strategy: DavidOS → FamilyAI → iZZi Builder Services → downstream projects

## Vision and design principles

See [`david-ai-workspace-v0.md`](./david-ai-workspace-v0.md) for the founding concept document — purpose, design principles, core life areas, and agent roles. That doc is the durable "why"; this README is the current "how."

## History

- **2026-05-11** — Migrated off Paperclip; adopted hermes-workspace; switched from OpenRouter to Anthropic direct via Claude Pro/Max OAuth. See `docs/decisions/`.
