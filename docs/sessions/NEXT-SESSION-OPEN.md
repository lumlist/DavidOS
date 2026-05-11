# Next Session — Open

**Last updated:** 2026-05-11 (afternoon session)
**Last session ended:** in progress — see end-of-session debrief in `docs/sessions/submitted/`

---

## Current stack (post-migration)

| Layer | Tool | Notes |
|---|---|---|
| Daily driver UI | hermes-workspace (outsourc-e/hermes-workspace v2.3.0) | Web UI at `localhost:3000`, multi-agent capable |
| Agent runtime | Hermes v0.13.0 | Gateway on `:8642`, dashboard on `:9119` |
| Auth | Claude Pro/Max OAuth | Flat subscription, not metered API |
| Host | DigitalOcean VPS `159.223.166.217` | SSH user: `hermes` |
| Repos in scope | DavidOS, FamilyAI, DavidAIStory | All under `github.com/lumlist` |

**Access pattern:** `ssh -L 3000:127.0.0.1:3000 hermes@159.223.166.217` then `localhost:3000` in browser.

**Three SSH sessions to maintain:**
1. `hermes gateway run` (gateway, :8642)
2. `hermes dashboard` (dashboard, :9119)
3. `cd ~/hermes-workspace && pnpm dev` (Workspace UI, :3000)

---

## What changed this session

- **Migrated off Paperclip.** Productivity-review scheduler auto-blocking loop (DAV-22 → DAV-23/24/25/26 cascade) was unfixable in config. Paperclip data archived at `/home/hermes/.paperclip-davidos/`, recoverable but frozen.
- **Adopted hermes-workspace.** Stage 2.7 UI is now this Workspace, not a Paperclip-Atlas custom build.
- **Switched off OpenRouter → Anthropic direct.** OpenRouter was routing through Bedrock at $0.03–$0.10/call despite provider-pin (pin only works via `-z` CLI, not gateway). OpenRouter paused, re-add when multi-provider routing actually needed.
- **Auth via Claude Pro/Max OAuth, not API key.** API key + $15 balance is dormant fallback.
- **Atlas → memo library.** Atlas agent record + 44 DAV-17 comments archived in `docs/atlas/identity/`. Treat as durable inputs to re-spawn Atlas when needed, not a preloaded persona.

---

## Active services on VPS

```
hermes gateway run                       :8642  (API_SERVER_ENABLED=true)
hermes dashboard                         :9119
cd ~/hermes-workspace && pnpm dev        :3000  (Workspace UI)
```

**Health check (any SSH session):**
```bash
ss -tlnp 2>/dev/null | grep -E "8642|9119|3000"
curl -s http://127.0.0.1:8642/v1/models | head -c 300
```

---

## Strategic decisions standing

- **Sequencing:** DavidOS foundation → FamilyAI MVP → iZZi Builder Services consulting → Looksmaxxing app + others
- **iZZi customer-zero pattern:** Every Workspace/Hermes config decision should be reusable for future iZZi AI Systems customers OR explicitly David-specific
- **Karrigan agent:** Deferred until personal-agent governance pattern exists in Workspace
- **Sonnet-class only.** No Opus without explicit approval.
- **Models:** OAuth auth means usage counts against Claude Pro/Max subscription rate limits (5-hour rolling window). If rate-limited during heavy sessions, hot-swap to API key auth: `hermes auth add anthropic`, choose API key option.

---

## Open threads / Next session entry points

- **Hermes Agent update available** (`9a63b5f → 825bd50`). Take between milestones, not mid-task.
- **DavidOS foundation deliverable** — next concrete commit not yet decided. Candidates: Workspace skill for daily-briefing pattern; FamilyAI MVP scoping doc; iZZi Builder Services one-pager.
- **Atlas re-spawn dry run** — validate "memo library" pattern works by spawning fresh Workspace session and feeding it `docs/atlas/` files.
- **Workspace baseline configuration** — profile name, default model, theme, permissions. Document in `docs/workspace/baseline-config.md`.

---

## Reference paths

- `/home/hermes/projects/personal-ai-workspace/` — DavidOS repo, HEAD on `origin/main`
- `/home/hermes/.hermes/config.yaml` — provider: anthropic, OAuth
- `/home/hermes/.hermes/.env` — `API_SERVER_ENABLED=true`, `ANTHROPIC_API_KEY` (dormant fallback)
- `~/hermes-workspace/` — Workspace install, `.env` has `HERMES_API_URL` + `HERMES_DASHBOARD_URL`
- `docs/atlas/identity/atlas-agent-record.json` — Atlas archive
- `docs/atlas/identity/dav-17-comments.json` — 44 Atlas comments archive
- `docs/sessions/submitted/2026-05-11T03-27-debrief.md` — canonical Atlas debrief
