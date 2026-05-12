# Atlas Identity — Archive & Memo Library

**Status as of 2026-05-11:** Atlas is no longer a preloaded runtime persona. The files in this directory are an **archive and memo library** used to re-spawn an Atlas-equivalent agent on demand inside hermes-workspace. See [ADR-003](../../decisions/ADR-003-paperclip-frozen-atlas-memo-library.md) for the rationale.

## Files in this directory

| File | Purpose |
|---|---|
| `atlas-agent-record.json` | Atlas's Paperclip-era identity record. Fields under `adapter`, `runtime_config`, and `heartbeat` are historical only. The `id`, `name`, `role`, `description`, `model`, and `capabilities` fields remain load-bearing for re-spawn. |
| `dav-17-comments.json` | 44 substantive Atlas comments from DAV-17. Working memory and reasoning patterns. Use as context when re-spawning. |
| `README.md` (this file) | Active re-spawn procedure |

The forward-looking, schema-conformant configuration lives at [`docs/workspace/agents/atlas.agent.json`](../../workspace/agents/atlas.agent.json). It conforms to hermes-workspace's `WorkspaceAgentDirectory` schema. As of 2026-05-11, the gateway does not yet expose `/api/workspace/agents`, so this file is not auto-loaded — it serves as the canonical "who is Atlas" record and is ready for registration when Hermes ships the API.

## How to re-spawn Atlas

Two paths. Pick based on session weight.

### Path 1 — Personality (recommended for most sessions)

Atlas is registered as a Hermes personality in `~/.hermes/config.yaml` under the `personalities:` block. Activate per-session in Workspace's personality switcher, or set as the default by changing `personality: <current>` to `personality: atlas` in the config and restarting the gateway.

Once active, Atlas's system prompt automatically instructs the model to load the memo library above before responding substantively. You don't need to attach files manually — Atlas knows to fetch them.

Verification: ask the new session a question like *"What does ADR-003 require of you?"* — Atlas should reference the file and quote its substance.

### Path 2 — Manual context-pack attachment (for one-off heavy sessions)

When you want a higher-effort spawn (e.g., a multi-hour architecture session) and want to be sure Atlas has every relevant artifact loaded as an attachment rather than relying on file reads:

1. Open a new Workspace session at `localhost:3000`
2. Attach the contents of:
   - `docs/atlas/identity/atlas-agent-record.json`
   - `docs/atlas/identity/dav-17-comments.json`
   - `docs/atlas/atlas-operating-spec.md`
   - The three ADRs (`docs/decisions/ADR-001..003.md`)
3. Prefix the session with: *"You are Atlas, Chief Systems Advisor for iZZi AI Systems. Operate per the attached identity record and policy memos."*
4. Continue with your work

This is heavier (uses more context window upfront) but guarantees the memos are loaded into the model's working memory rather than fetched on demand. Use sparingly.

## Canonical handoff

The most complete Atlas debrief is at [`docs/sessions/submitted/2026-05-11T03-27-debrief.md`](../../sessions/submitted/2026-05-11T03-27-debrief.md). Read this first if you need Atlas's last-known understanding of David's projects, priorities, and open threads.

## When to update this directory

- **Atlas's role definition changes** → update `atlas-operating-spec.md` (in the parent `docs/atlas/` directory) and bump the date below
- **A session produces substantively new Atlas reasoning** worth preserving → append to `dav-17-comments.json` or create a dated successor file
- **The Hermes API ships agent registration** → migrate `docs/workspace/agents/atlas.agent.json` from forward-looking artifact to live config, update this README

## Linked decisions

- [ADR-001](../../decisions/ADR-001-adopt-hermes-workspace.md) — hermes-workspace as daily driver
- [ADR-002](../../decisions/ADR-002-anthropic-oauth-over-api-key.md) — Anthropic OAuth, Sonnet-only
- [ADR-003](../../decisions/ADR-003-paperclip-frozen-atlas-memo-library.md) — Paperclip frozen, Atlas as memo library

---

*Last updated: 2026-05-11. If this date is older than a month and the system has changed, treat the procedure as suspect and verify against the current ADRs.*
