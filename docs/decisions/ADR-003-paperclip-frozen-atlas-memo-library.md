# ADR-003: Paperclip frozen; Atlas treated as memo library

**Date:** 2026-05-11
**Status:** Accepted
**Deciders:** David Izzard

## Context

Paperclip-Atlas was the daily-driver agent surface from inception through 2026-05-10. Two structural issues made it unsustainable:

1. **Productivity-review scheduler auto-block loop.** Trigger `long_active_duration` fires on stale `in_progress` issues and auto-creates blocking recovery/review issues (DAV-22 spawned DAV-23, 24, 25, 26 within hours). Not configurable in Paperclip settings.
2. **CEO-role auto-grants.** `can_assign_tasks: true` cannot be toggled off; `can_create_agents: true` is toggleable but the broader role behavior is rigid.

These constraints turned Paperclip into an environment that worked against the user rather than for them.

Atlas itself (the persona, capabilities, working memory) is valuable independent of Paperclip. The Atlas agent record and 44 DAV-17 comments represent substantive context worth preserving.

## Decision

1. **Freeze Paperclip.** Stop using as daily driver. Keep data directory `/home/hermes/.paperclip-davidos/` on disk for recoverability.
2. **Archive Atlas identity assets to DavidOS repo.** `atlas-agent-record.json` and `dav-17-comments.json` committed under `docs/atlas/identity/`.
3. **Treat Atlas as a memo library, not a preloaded runtime persona.** Re-spawn Atlas on demand in hermes-workspace by feeding it the relevant archive files as session context.

## Rationale

- **Continuity preserved.** Atlas's substantive contributions (44 DAV-17 comments, identity config, capability profile) survive the Paperclip exit.
- **Flexibility gained.** Atlas is no longer the only viable agent. Workspace supports parallel agents — future personas (Karrigan, FamilyAI agents, iZZi customer agents) can coexist.
- **Cost discipline.** A preloaded Atlas persona consuming context on every session is expensive. On-demand re-spawn is selective.
- **Aligns with iZZi customer-zero pattern.** "Persona as memo library you re-spawn" is a reusable architectural pattern across future customers.

## Consequences

- Need a documented re-spawn procedure (added to `docs/atlas/identity/README.md`)
- Atlas's "always-on" awareness is gone; each session starts fresh and must be primed
- DAV-22 (Paperclip-specific productivity-review issue) should be closed or repurposed
- If a similar auto-scheduling problem appears in Workspace, we'll need to re-architect rather than tolerate

## Recovery path (if ever needed)

```bash
npx paperclipai@2026.428.0 run \
  --data-dir /home/hermes/.paperclip-davidos \
  --instance davidos \
  --bind loopback
```

## Re-evaluation triggers

- Workspace cannot provide multi-agent or persona-spawning patterns that Paperclip-Atlas did
- A specific Atlas capability proves irreplaceable in Workspace
- Paperclip ships a fix for the productivity-review scheduler

## Related

- ADR-001 — Adopt hermes-workspace
- ADR-002 — Anthropic OAuth over API key
- `docs/atlas/identity/README.md` — re-spawn procedure
- `docs/sessions/submitted/2026-05-11T03-27-debrief.md` — canonical Atlas debrief
