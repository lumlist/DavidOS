# Atlas Identity — Archive & Memo Library

**Status as of 2026-05-11:** Atlas is no longer a preloaded runtime persona. The files in this directory are an **archive and memo library** used to re-spawn an Atlas-equivalent agent on demand inside hermes-workspace.

## Why this changed

Atlas originally ran as the daily-driver agent inside Paperclip. On 2026-05-11 we migrated off Paperclip (productivity-review scheduler auto-block loop, no config toggle to disable). The replacement surface — hermes-workspace — supports multi-agent profiles, so Atlas no longer needs to be the single always-on persona. We get more flexibility by treating Atlas memos as **inputs** to fresh sessions rather than a permanent loaded state.

## Files in this directory

- **`atlas-agent-record.json`** — Atlas agent identity, capabilities, model configuration as it existed in Paperclip. Source of truth for re-spawning the persona.
- **`dav-17-comments.json`** — 44 substantive comments from DAV-17 representing Atlas's working memory and reasoning patterns. Use as context when re-spawning.

## How to re-spawn Atlas in Workspace

1. Open a new Workspace session at `localhost:3000`
2. Attach or paste relevant contents from `atlas-agent-record.json` (identity + capability config)
3. Optionally attach `dav-17-comments.json` excerpts for tone/working-memory anchoring
4. Prefix the session with: *"You are Atlas, an AI agent employed by David Izzard. Operate per the attached identity record."*
5. Continue work

## Canonical handoff

The most complete Atlas debrief is at `docs/sessions/submitted/2026-05-11T03-27-debrief.md`. Read this first if you need Atlas's last-known understanding of David's projects, priorities, and open threads.

## Linked decisions

- See `docs/decisions/ADR-003-paperclip-frozen-atlas-memo-library.md` for the rationale behind this change.
