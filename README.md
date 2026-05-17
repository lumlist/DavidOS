# DavidOS

Personal AI operating system for David Izzard. A tool-agnostic AIOS control plane (ADR-005); FamilyAI and downstream projects are built through it, not beneath it.

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

- [`docs/sessions/NEXT-SESSION-OPEN.md`](docs/sessions/NEXT-SESSION-OPEN.md) — current state and next session entry points
- [`docs/sessions/REPO-HYGIENE-CHECKLIST.md`](docs/sessions/REPO-HYGIENE-CHECKLIST.md) — run after structural changes to prevent stale docs
- [`docs/sessions/submitted/`](docs/sessions/submitted/) — debriefs from completed sessions
- [`docs/atlas/`](docs/atlas/) — Atlas memo library (archive, not active runtime)
- [`docs/decisions/`](docs/decisions/) — Architecture Decision Records (ADRs)
- [`docs/architecture/`](docs/architecture/) — stack diagrams and infrastructure docs
- [`docs/workspace/`](docs/workspace/) — Workspace baseline configuration and patterns
- [`docs/project-registry.md`](docs/project-registry.md) — active projects, business idea pipeline
- [`docs/tool-stack-inventory.md`](docs/tool-stack-inventory.md) — broader tool inventory and model policy

## Operating principles

- iZZi customer-zero pattern: David's outcome comes first; never trade it for reusability. Classify each decision as David-specific, reusable, or both. Generalization is a second-pass concern, never a first-pass constraint (SOUL.md §5).
- Sonnet is the default; Opus only for high-judgment work, with explicit approval logged in approvals-log.md (ADR-002; SOUL.md §5).
- DavidOS is the tool-agnostic AIOS control plane (ADR-005); the current build sequence is the GIP governance lifecycle — see docs/governance/README.md

## Vision and design principles

See [`david-ai-workspace-v0.md`](./david-ai-workspace-v0.md) for the founding concept document — purpose, design principles, core life areas, and agent roles. That doc is the durable "why"; this README is the current "how."

## History

- **2026-05-11** — Migrated off Paperclip; adopted hermes-workspace; switched from OpenRouter to Anthropic direct via Claude Pro/Max OAuth. See `docs/decisions/`.
