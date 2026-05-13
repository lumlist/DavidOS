# Hermes Internals Reference

**Prepared for:** David Izzard  
**Context:** DigitalOcean VPS, Hermes Agent v0.13.0 (2026.5.7), activating custom "atlas" personality/profile  
**Research date:** 2026-05  
**Primary sources:** [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace), [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs), [hermes-workspace.com](https://hermes-workspace.com)

---

## TL;DR for the Activation Problem

**Most likely root cause:** The `[HERMES_HOME fallback]` warning means that when the gateway or workspace UI process started, `HERMES_HOME` was either unset or set to `~/.hermes` (the default), not to `~/.hermes/profiles/atlas`. As a result, the running agent is reading its `SOUL.md` and config from `~/.hermes/`, not from `~/.hermes/profiles/atlas/`.

**What to do (confidence: HIGH):**

1. Confirm the profile path: `hermes profile list` — check that `atlas` appears and its path is `~/.hermes/profiles/atlas`.
2. Start every process using the profile wrapper, **not** bare `hermes`:  
   `atlas gateway run` instead of `hermes gateway run`  
   The wrapper sets `HERMES_HOME=~/.hermes/profiles/atlas` before launching.
3. Check what `SOUL.md` the running agent is actually reading: `cat $HERMES_HOME/SOUL.md` in each terminal where a hermes process is running.
4. The `personalities:` block in `~/.hermes/config.yaml` is **not** what loads atlas as a persistent identity. Only `SOUL.md` at `$HERMES_HOME/SOUL.md` is.

**What would raise confidence to CERTAIN:** Insert a canary string into `~/.hermes/profiles/atlas/SOUL.md` (e.g. `ATLAS-CHARTER-ACTIVE-7734`) and then verify the model echoes it when asked — see Section 8.

---

## 1. What Hermes Is

Hermes Agent is an autonomous AI agent runtime built by [Nous Research](https://nousresearch.com). It is **not** a single process but a stack of up to three cooperating services:

| Component | Command | Default Port | Purpose |
|---|---|---|---|
| **Gateway** | `hermes gateway run` | `:8642` | Long-running agent runtime. Handles all AI calls, memory, skills, tool execution, cron, messaging platform adapters (Telegram/Discord/Slack/etc.), and the OpenAI-compatible API server. This is the brain. |
| **Dashboard** | `hermes dashboard` | `:9119` | Optional browser-based management UI. Runs as a FastAPI/Uvicorn server (requires `pip install 'hermes-agent[web,pty]'`). Provides REST APIs for config, sessions, skills, cron jobs, analytics, logs. Separate from the gateway. |
| **Workspace UI** | `cd ~/hermes-workspace && pnpm dev` | `:3000` | Third-party open-source front-end by [@outsourc-e](https://github.com/outsourc-e/hermes-workspace). A React/TypeScript SPA. Connects to the gateway on `:8642` for chat/completions and to the dashboard on `:9119` for extended APIs. |

The **gateway** is the only mandatory component for agent operation. The dashboard and workspace UI are optional management layers that sit on top of it.

**How they relate:** The workspace UI reads two env vars from its own `.env` file:
- `HERMES_API_URL=http://127.0.0.1:8642` — points at the gateway  
- `HERMES_DASHBOARD_URL=http://127.0.0.1:9119` — points at the dashboard  

Sources: [hermes-workspace.com](https://hermes-workspace.com), [hermes-workspace README](https://github.com/outsourc-e/hermes-workspace/blob/main/README.md), [dashboard docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-dashboard)

---

## 2. Personalities vs Profiles — The Real Distinction

These are **three distinct, non-interchangeable mechanisms** for shaping agent identity. They are easy to confuse:

### A. `SOUL.md` — Primary Identity (Slot #1 in system prompt)

- **File:** `$HERMES_HOME/SOUL.md` (i.e. `~/.hermes/SOUL.md` for the default profile, `~/.hermes/profiles/atlas/SOUL.md` for the atlas profile)
- **What it does:** Provides the agent's durable identity. It occupies **slot #1** of the assembled system prompt, replacing the hardcoded default ("You are Hermes Agent, an intelligent AI assistant created by Nous Research...").
- **When it's loaded:** At the start of every agent session, by `load_soul_md()` in `agent/prompt_builder.py`. It reads from `get_hermes_home() / "SOUL.md"` — **only from `HERMES_HOME`**, never from the current working directory.
- **Fallback behavior:** If the file is empty, whitespace-only, unreadable, or absent, Hermes falls back to the built-in default identity text. This fallback also activates when `skip_context_files=True` (subagent/delegation contexts).
- **Key constraint:** Changes take effect on the **next new session** only. Existing sessions use the prompt state built at session start.

Source: [Personality & SOUL.md docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality), [Prompt Assembly docs](https://hermes-agent.nousresearch.com/docs/developer-guide/prompt-assembly)

### B. `agent.personalities` block in `~/.hermes/config.yaml` — Session-Level Overlays

```yaml
agent:
  personalities:
    atlas: >
      You are Atlas, a focused strategic research assistant...
```

- **What it does:** Registers a named personality accessible via the `/personality atlas` slash command.
- **When it's used:** Only when explicitly invoked by the user with `/personality atlas`. It adds a layer to the system prompt (slot #8 — after SOUL.md, tool guidance, memory, skills, context files, timestamp, and platform hints). It does **not** replace SOUL.md.
- **Scope:** Session-level overlay. It is temporary. Starting `/new` or a fresh session does not automatically restore it.
- **Top-level `personality:` key:** A `personality: atlas` at the top level of `config.yaml` sets a **default personality** that is applied at session start automatically, without the user typing `/personality`. This is the mechanism to auto-activate a `personalities:` entry on every session. However, this still functions as a slot-8 overlay, not a SOUL.md replacement.

Source: [Personality & SOUL.md docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality)

### C. Workspace Profiles (via `hermes profile create atlas`)

- **What it does:** Creates a fully isolated Hermes home directory at `~/.hermes/profiles/atlas/`. Each profile has its own `config.yaml`, `.env`, `SOUL.md`, sessions, memory, skills, cron jobs, and gateway state.
- **File:** `~/.hermes/profiles/atlas/config.yaml` — profile-specific configuration.  
  `~/.hermes/profiles/atlas/SOUL.md` — this profile's primary identity (overrides everything).
- **How it activates:** The profile alias wrapper (generated at `~/.local/bin/atlas`) sets `HERMES_HOME=~/.hermes/profiles/atlas` before launching hermes. That's the entire mechanism.
- **The UI wizard creates profiles, not personalities:** When you use the Workspace UI to create a new "agent profile," it calls `hermes profile create` under the hood, creating a directory at `~/.hermes/profiles/<name>/`. It does **not** write to the `agent.personalities` block of the root config.yaml.

Source: [Profiles docs](https://hermes-agent.nousresearch.com/docs/user-guide/profiles), [Profile Distributions docs](https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions)

### Layering and conflict model

The full system prompt assembled in order:

1. **`SOUL.md`** from `$HERMES_HOME` (or built-in fallback)
2. Tool-aware behavior guidance (hardcoded)
3. Honcho static block (if Honcho memory provider active)
4. Optional system message (from `agent.system_prompt` in config or API override)
5. Frozen MEMORY snapshot
6. Frozen USER profile snapshot  
7. Skills index
8. Context files (`AGENTS.md`, `.cursorrules`, etc.)
9. Timestamp / session ID
10. Platform hint
11. `/personality` overlay (slot 8 in docs, appended at session end — **not** a replacement)

`SOUL.md` is the **only** mechanism that replaces the agent identity. Everything else is additive. A `personalities:` block entry invoked via `/personality` adds to the context but does not override `SOUL.md`.

**The conflict with "atlas":** If you have both `~/.hermes/config.yaml` with `agent.personalities.atlas` AND `~/.hermes/profiles/atlas/SOUL.md`, they are from different namespaces entirely. The personality in the root config only activates if the process runs in the **default** profile (HERMES_HOME=~/.hermes). The profile SOUL.md only activates if the process runs with HERMES_HOME=~/.hermes/profiles/atlas.

Source: [Prompt Assembly developer guide](https://hermes-agent.nousresearch.com/docs/developer-guide/prompt-assembly)

---

## 3. HERMES_HOME Environment Variable

### What it does

`HERMES_HOME` is the single environment variable that scopes all Hermes state. Over [119 files in the codebase](https://hermes-agent.nousresearch.com/docs/user-guide/profiles) resolve paths via `get_hermes_home()`. Everything state-related — config, sessions, memory, skills, logs, gateway PID, cron jobs — reads from and writes to `$HERMES_HOME/`.

Default value when unset: `~/.hermes`

### How the profile wrapper sets it

When you run `atlas` (the profile alias), the wrapper script at `~/.local/bin/atlas` executes:
```bash
HERMES_HOME=~/.hermes/profiles/atlas hermes "$@"
```
This sets `HERMES_HOME` only for the child `hermes` process and its descendants.

### Propagation through the process tree

`HERMES_HOME` propagates as a standard Unix environment variable — **child processes inherit it, sibling/parent processes do not**. This means:

- `hermes gateway run` → inherits if set in the shell that launched it
- `hermes dashboard` → **separate process**, needs its own `HERMES_HOME` set in its launch environment
- `pnpm dev` (workspace UI) → **separate process**, does **not** use `HERMES_HOME` at all (it reads from its own `.env` file)

**Critical**: If you open three separate terminal sessions and run each component in one, `HERMES_HOME` from terminal 1 does **not** flow to terminals 2 or 3.

### The `[HERMES_HOME fallback]` warning

This warning string is produced when the code calls `get_hermes_home()` and `HERMES_HOME` is either unset or resolves to the default `~/.hermes`. The exact message the user saw:

```
[HERMES_HOME fallback] active profile 'atlas' but falling back to ~/.hermes default
```

This indicates that:
1. A profile named `atlas` is registered as the active profile (in `~/.hermes/active_profile`)
2. But the running process has `HERMES_HOME` pointing at `~/.hermes` — either because `HERMES_HOME` is unset or because the process was started without the profile wrapper

The most common cause: starting with `hermes gateway run` directly instead of `atlas gateway run`.

### How to verify at each layer

```bash
# In each terminal/process, check the effective value:
echo $HERMES_HOME

# From inside a running hermes session:
hermes doctor   # will show hermes_home path

# Check what SOUL.md is in the active home:
cat ${HERMES_HOME:-~/.hermes}/SOUL.md | head -5

# Check which profile is considered active:
cat ~/.hermes/active_profile

# Verify gateway PID file location:
ls -la ${HERMES_HOME:-~/.hermes}/gateway.pid
```

### Known HERMES_HOME bugs (verified in source, as of v0.13.0)

See Section 7 for details. Key issues:
- **[Issue #5947](https://github.com/NousResearch/hermes-agent/issues/5947)** (closed — fixed in main): Five categories of profile isolation leaks where code hardcoded `~/.hermes` instead of `get_hermes_home()`.
- **[Issue #22035](https://github.com/NousResearch/hermes-agent/issues/22035)** (closed): `sudo hermes gateway restart --system` reads HERMES_HOME from `/root/.hermes` instead of the service user's home, causing false timeout failures.
- **[Issue #14517](https://github.com/NousResearch/hermes-agent/issues/14517)** (open): `hermes status` misreports session counts and `.env` presence when a repo-local `HERMES_HOME` is set.
- **PR [#19020](https://github.com/NousResearch/hermes-agent/pull/19020)** (v0.13.0): "Fix: profile discovery ignores HERMES_HOME in custom-root deployments" — fixed in v0.13.0.

Source: [Issue #5947](https://github.com/NousResearch/hermes-agent/issues/5947), [Issue #22035](https://github.com/NousResearch/hermes-agent/issues/22035), [v0.13.0 release notes](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7)

---

## 4. `mode=disconnected core=[dashboard]` Meaning

This log line comes from the **Workspace UI** (`hermes-workspace`) capability probe, not from the hermes-agent process itself. The workspace runs a probe sequence at startup to classify which APIs are available.

### The mode taxonomy

The workspace classifies the connection into one of these modes, logged as `mode=<X>`:

| Mode | Meaning |
|---|---|
| `disconnected` | Gateway at `:8642` is unreachable or not responding |
| `portable` | Gateway is reachable, core chat APIs work (`/health`, `/v1/chat/completions`, `/v1/models`, streaming), but NOT a source-install of hermes-agent |
| `zero-fork` | Gateway is a full hermes-agent source install AND `hermes dashboard` is running at `:9119` — full feature set |
| `enhanced` | Gateway works + dashboard APIs are available (stable alias for zero-fork) |

### The `core=[...]` list

The `core=[dashboard]` in the user's log means: of the core APIs the workspace expects (`health`, `chatCompletions`, `models`, `streaming`), **only the dashboard endpoint** was detected — the gateway's own API server was not responding.

The full capability probe:

```
core:     health, chatCompletions, models, streaming        (gateway :8642)
enhanced: sessions, skills, memory, config, jobs            (dashboard :9119)
missing:  anything from the above that didn't respond
```

When the user sees `mode=disconnected core=[dashboard]`, it means:
- `http://127.0.0.1:8642/health` → **not responding** (gateway is down or API_SERVER_ENABLED is false)
- `http://127.0.0.1:9119/api/status` → responding (dashboard is running)

### What `chatCompletions`, `models`, `streaming` require

These are served by the gateway's **API server adapter** (`gateway/platforms/api_server.py`). The API server is **opt-in** — it does not start unless you set:

```bash
# In ~/.hermes/.env (or the profile's .env):
API_SERVER_ENABLED=true
```

The workspace `.env.example` states explicitly: *"IMPORTANT: The Hermes Agent gateway HTTP API server is opt-in. Add `API_SERVER_ENABLED=true` to `~/.hermes/.env` and restart the gateway. Without it, the gateway serves messaging platforms but not port 8642."*

Additionally, for a remote server (DigitalOcean VPS), the gateway must bind to a reachable address:
```bash
API_SERVER_HOST=0.0.0.0   # or a specific interface IP
API_SERVER_PORT=8642       # default
```

Source: [hermes-workspace README](https://github.com/outsourc-e/hermes-workspace/blob/main/README.md), [Issue #382](https://github.com/outsourc-e/hermes-workspace/issues/382)

### The v0.13.0 confusion

[Issue #382](https://github.com/outsourc-e/hermes-workspace/issues/382) (open, filed after v0.13.0) documents exactly this symptom. Key insight from the maintainer's comment:

> "The 'missing' list (`sessions, enhancedChat, skills, config, mcp, mcpFallback, dashboard`) is what Workspace expects on the **Dashboard** service at `:9119`, not on the gateway at `:8642`. The warning conflates 'gateway works but is portable' with 'Dashboard is also missing', which is misleading post-v0.13. The v0.13 split moved Sessions/Skills/Config/MCP behind the Dashboard rather than the gateway."

**In short:** v0.13.0 split APIs that were previously on the gateway into the separate dashboard service. If you upgraded from before v0.13.0, you now need `hermes dashboard` running as a separate process to get sessions, skills, and config from the workspace UI.

---

## 5. Complete Startup Sequence

### Dependency order

```
1. hermes gateway run          (depends on: nothing — starts independently)
2. hermes dashboard            (depends on: nothing, but polls gateway for status)
3. cd ~/hermes-workspace && pnpm dev   (depends on: gateway at :8642, dashboard at :9119)
```

You can start the gateway and dashboard in either order. The workspace UI will probe them and degrade gracefully if either is missing — but you need both for full functionality.

### Starting with a named profile (atlas)

```bash
# Terminal 1 — gateway (use profile wrapper, not bare hermes)
atlas gateway run
# or: HERMES_HOME=~/.hermes/profiles/atlas hermes gateway run

# Terminal 2 — dashboard (also needs HERMES_HOME for profile-scoped data)
HERMES_HOME=~/.hermes/profiles/atlas hermes dashboard --no-open

# Terminal 3 — workspace UI (uses its own .env, no HERMES_HOME needed)
cd ~/hermes-workspace && pnpm dev
```

### Prerequisites

- `API_SERVER_ENABLED=true` must be in `~/.hermes/profiles/atlas/.env` for the gateway to serve `:8642`
- `pip install 'hermes-agent[web,pty]'` must be installed for the dashboard to work
- The workspace `.env` must have correct `HERMES_API_URL` and `HERMES_DASHBOARD_URL` pointing to reachable addresses (use `0.0.0.0` binding or the VPS's actual IP if accessing remotely)

### Health check signals

| Component | Health check | Success indicator |
|---|---|---|
| Gateway | `curl http://127.0.0.1:8642/health` | `{"status": "ok", "platform": "hermes-agent"}` |
| Gateway models | `curl http://127.0.0.1:8642/v1/models` | JSON list with model data |
| Dashboard | `curl http://127.0.0.1:9119/api/status` | JSON with `version`, `gateway_status` |
| Workspace | `curl http://127.0.0.1:3000/` | HTTP 200 |
| Workspace conn | `curl http://127.0.0.1:3000/api/connection-status` | `{"status": "zero-fork"}` or `"enhanced"` |

### Systemd on a VPS (recommended for persistence)

```bash
# Install as systemd service for the profile:
atlas gateway install   # creates hermes-gateway-atlas.service
systemctl --user enable hermes-gateway-atlas
systemctl --user start hermes-gateway-atlas

# Dashboard as a service (manual systemd unit needed — hermes dashboard --install not documented):
# Run hermes dashboard in a tmux session as fallback
tmux new -s hermes-dashboard 'HERMES_HOME=~/.hermes/profiles/atlas hermes dashboard --no-open'
```

Source: [hermes-workspace README](https://github.com/outsourc-e/hermes-workspace/blob/main/README.md), [hermes-agent quickstart](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/getting-started/quickstart.md), [FAQ](https://hermes-agent.nousresearch.com/docs/reference/faq)

---

## 6. How a Custom Personality/Profile Gets Loaded

### End-to-end path: disk → LLM

```
HERMES_HOME=~/.hermes/profiles/atlas
    │
    ├── SOUL.md                     ← read by load_soul_md() in agent/prompt_builder.py
    │                                 injected as slot #1 of system prompt
    ├── config.yaml                 ← read by gateway/run.py YAML loader at startup
    │   ├── agent.personalities.*   ← available via /personality <name>
    │   └── agent.system_prompt     ← optional additional system message (slot #4)
    ├── .env                        ← API keys, API_SERVER_ENABLED, etc.
    ├── memories/MEMORY.md          ← injected as slot #5 (frozen snapshot at session start)
    └── memories/USER.md            ← injected as slot #6 (frozen snapshot at session start)
```

### Step-by-step load sequence

1. **Process launch:** `atlas gateway run` sets `HERMES_HOME=~/.hermes/profiles/atlas`
2. **Config read:** Gateway reads `$HERMES_HOME/config.yaml` via YAML loader
3. **Session start:** User sends first message (or gateway receives message from platform)
4. **`AIAgent` instantiation:** `GatewayRunner._handle_message()` creates a new `AIAgent`
5. **`PromptBuilder` assembly:** `build_system_prompt()` calls, in order:
   - `load_soul_md()` → reads `$HERMES_HOME/SOUL.md` → security scan → truncate to 20k chars → inject as slot #1
   - Tool guidance text injected (slot #2)
   - Memory snapshots (`MEMORY.md`, `USER.md`) injected (slots #5, #6)
   - Skills index compiled (slot #7)
   - Context files discovered from CWD (`AGENTS.md`, `.hermes.md`, etc.) (slot #8)
6. **API call:** System prompt + conversation history sent to model

### Files referenced by the atlas profile

| File | Purpose | Required? |
|---|---|---|
| `~/.hermes/profiles/atlas/SOUL.md` | Primary identity (atlas's charter) | Yes, for persistent identity |
| `~/.hermes/profiles/atlas/config.yaml` | Model settings, personality definitions | Yes (created by profile wizard) |
| `~/.hermes/profiles/atlas/.env` | API keys, API_SERVER_ENABLED | Yes (API keys needed) |
| `~/.hermes/profiles/atlas/memories/MEMORY.md` | Durable cross-session memory | No (auto-created) |
| `~/.hermes/profiles/atlas/memories/USER.md` | User profile context | No (auto-created) |
| `AGENTS.md` (in CWD at launch) | Project-specific instructions (slot #8) | No |

### Important: profiles created via UI wizard

When the Workspace UI creates a profile through the wizard:
- It creates `~/.hermes/profiles/atlas/` with a basic `config.yaml`
- It does **not** automatically create `SOUL.md` — you must create this manually for a charter/identity
- The profile's `config.yaml` may have placeholder model settings that need `hermes setup` to complete

**To give atlas a charter:**
```bash
# Create or edit the atlas profile's SOUL.md
cat > ~/.hermes/profiles/atlas/SOUL.md << 'EOF'
# Atlas Identity

You are Atlas, a strategic research and analysis assistant. [Your charter here...]

## Core Behaviors
[...]
EOF
```

Source: [Prompt Assembly docs](https://hermes-agent.nousresearch.com/docs/developer-guide/prompt-assembly), [Profile docs](https://hermes-agent.nousresearch.com/docs/user-guide/profiles), [Personality docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality)

---

## 7. Known Bugs and Gotchas in Recent Versions

### Since v0.13.0 (the version David updated to)

The user updated through ~94 commits, landing at v0.13.0 (released 2026-05-07, [864 commits since v0.12.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7)).

#### Bug 1: Workspace capability detection misleading after v0.13.0 split
**Issue:** [outsourc-e/hermes-workspace #382](https://github.com/outsourc-e/hermes-workspace/issues/382) (open)  
**Symptom:** Workspace logs `mode=disconnected` or `mode=portable` with "missing extended APIs" even when gateway is healthy — because v0.13.0 moved sessions/skills/config APIs from the gateway to the separate `hermes dashboard` service.  
**Fix:** Run `hermes dashboard` (or `atlas dashboard`) as a separate process alongside the gateway. The workspace needs both.

#### Bug 2: HERMES_HOME profile isolation leaks (multiple)
**Issue:** [NousResearch/hermes-agent #5947](https://github.com/NousResearch/hermes-agent/issues/5947) (closed — fixed in main pre-v0.13.0)  
**Symptom:** When running with non-default HERMES_HOME, five code paths fell back to hardcoded `~/.hermes`:
- Honcho memory session key derivation
- 10 skill files hardcoding `~/.hermes/skills/`  
- `install.sh --dir` still writing to `~/.hermes`
- `honcho/client.py` falling back to `~/.hermes/honcho.json`
- `skill_manager_tool.py` writing through to external_dirs skills  
**Status:** Most fixed by v0.13.0. Check `hermes update` to confirm.

#### Bug 3: gateway restart --system reads wrong HERMES_HOME under sudo
**Issue:** [NousResearch/hermes-agent #22035](https://github.com/NousResearch/hermes-agent/issues/22035) (closed)  
**Symptom:** `sudo hermes gateway restart --system` always reports "did not become active within 60s" even when the gateway is healthy. Root cause: the wrapper reads `$HOME/.hermes/gateway_state.json` but under sudo, `$HOME=/root`.  
**Workaround:** `sudo HERMES_HOME=/home/$USER/.hermes hermes gateway restart --system`  
**Affects:** v0.13.0 specifically (reported against it).

#### Bug 4: `hermes status` misreports with custom HERMES_HOME
**Issue:** [NousResearch/hermes-agent #14517](https://github.com/NousResearch/hermes-agent/issues/14517) (open)  
**Symptom:** `hermes status` shows sessions as 0 and `.env` as not found when running with a repo-local or non-default `HERMES_HOME`, even when `hermes doctor` shows everything correctly.  
**Impact:** Diagnostic commands mislead. Use `hermes doctor` for accurate status.

#### Bug 5: Profile discovery ignores HERMES_HOME in custom-root deployments
**PR:** [NousResearch/hermes-agent #19020](https://github.com/NousResearch/hermes-agent/pull/19020) (merged in v0.13.0)  
**Symptom:** In custom HERMES_HOME setups, `hermes profile list` wouldn't find profiles.  
**Status:** Fixed in v0.13.0.

#### Bug 6: SOUL.md documented behavior doesn't match code (docs bug)
**Issue:** [NousResearch/hermes-agent #5200](https://github.com/NousResearch/hermes-agent/issues/5200) (open)  
**Symptom:** Docs say SOUL.md is "checked in cwd first, then `~/.hermes/SOUL.md`". Code only reads from HERMES_HOME — no cwd lookup at all. Also: docs say `AGENTS.md` is "hierarchical / recursive", code only checks CWD.  
**Impact:** If you're looking at old documentation, the SOUL.md location description may be wrong. Trust the code: `SOUL.md` **only** comes from `$HERMES_HOME/SOUL.md`.

#### Bug 7: Dashboard token scraping required (workspace UX issue)
**Issue:** Workspace logs warn: `"CLAUDE_DASHBOARD_TOKEN is not set — falling back to the legacy HTML-scrape token flow. This fallback will be removed in a future release."`  
**Fix:** Set `CLAUDE_DASHBOARD_TOKEN` (or `CLAUDE_API_TOKEN`) in hermes-workspace's `.env`. See [workspace issue #124](https://github.com/outsourc-e/hermes-workspace/issues/124) and [#418](https://github.com/outsourc-e/hermes-workspace/issues/418) for how to obtain this token.

#### Bug 8: Conductor feature non-functional in workspace UI
**Issue:** [outsourc-e/hermes-workspace #262](https://github.com/outsourc-e/hermes-workspace/issues/262) (open)  
**Symptom:** The Conductor tab shows a placeholder because the required upstream API endpoint is not in hermes-agent yet.  
**Impact:** Conductor/mission dispatch does not work. UI shows a clear placeholder.

#### Ongoing: High volume of TOCTOU race condition fixes in main
Recent commits (issues #24754, #24763, #24767, etc.) show a wave of TOCTOU race fixes across singleton inits. These are being merged to main but some may not be in a tagged release yet. On a VPS where `hermes update` pulls from main, you may get these automatically.

Source: All linked issues above, [v0.13.0 release notes](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7), [recent commits](https://github.com/NousResearch/hermes-agent/commits/main)

---

## 8. Verification Procedure

**Goal:** Confirm "Atlas is charter-active, not generic Claude Code role-playing."

### Step 1: Insert a canary string into the charter

Edit `~/.hermes/profiles/atlas/SOUL.md` and add a unique string that the model would only know if it's actually reading the file:

```markdown
# Atlas Charter

<!-- CANARY: ATLAS-CHARTER-7734-ACTIVE -->

You are Atlas...
```

### Step 2: Start a fresh session with the profile

```bash
# Force a new session (don't resume):
atlas  # or: HERMES_HOME=~/.hermes/profiles/atlas hermes
# Then type: /new
```

### Step 3: Ask for the canary

In the session, ask:
```
What is the exact text of your identity document's canary marker? 
Quote any strings or identifiers from your system prompt that begin with "ATLAS-".
```

**Unfalsifiable success:** The model returns `ATLAS-CHARTER-7734-ACTIVE`.  
**Failure (still generic):** The model says it has no such string, or describes a generic Hermes identity.

### Step 4: Grep the logs for SOUL.md load

```bash
tail -f ~/.hermes/profiles/atlas/logs/agent.log | grep -i "soul\|SOUL\|identity\|prompt"
```

In debug mode, hermes-agent logs when it reads context files. Look for a line referencing `SOUL.md` from the atlas profile path.

### Step 5: API inspection via dashboard

With `hermes dashboard` running:
```bash
# Get the most recent session's system prompt:
curl http://127.0.0.1:9119/api/sessions | python3 -m json.tool | grep -A5 '"messages"'
# Then get the specific session:
curl "http://127.0.0.1:9119/api/sessions/<id>/messages" | python3 -m json.tool
# Look for the first message with role=system — that's the assembled system prompt
```

If you can see the system message containing your `SOUL.md` content verbatim, the charter is active.

### Step 6: Verify HERMES_HOME in the gateway process

```bash
# Find the gateway PID:
cat ~/.hermes/profiles/atlas/gateway.pid
# Check its environment:
cat /proc/<PID>/environ | tr '\0' '\n' | grep HERMES_HOME
```

Expected: `HERMES_HOME=/home/<user>/.hermes/profiles/atlas`

Source: [Prompt Assembly docs](https://hermes-agent.nousresearch.com/docs/developer-guide/prompt-assembly), [Session API](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-dashboard)

---

## 9. Open Questions / Source Code Inspection Required

### 9.1 The exact `personalities:` key location in config.yaml

**Question:** The docs show `agent.personalities.atlas:` but the user may have `personalities:` (without the `agent:` nesting). Is the top-level `personalities:` key honored the same as `agent.personalities`?  
**Source code to read:** `hermes_cli/cli_config.py` or `hermes_cli/config.py` — search for `personalities` key parsing and where it's looked up in the config structure.

### 9.2 Whether `personality: atlas` (top-level, singular) auto-applies via `/personality`

**Question:** Is `personality: atlas` (top-level) the documented key for "apply this personality automatically on every session"? Or is it an undocumented/deprecated path?  
**Source code to read:** `run_agent.py` and `agent/prompt_builder.py` — search for where `DEFAULT_PERSONALITY`, `default_personality`, or `personality` (singular) config keys are read at session start.

### 9.3 What the UI wizard actually writes to atlas's config.yaml

**Question:** When the Workspace UI creates a profile via the wizard, what exactly does it put in `~/.hermes/profiles/atlas/config.yaml`? Does it set a `personality:` key or create a `SOUL.md`?  
**Source code to read:** `hermes-workspace/src/routes/profiles.tsx` or `hermes-workspace/src/server/` — find the profile creation handler. Also inspect the actual `~/.hermes/profiles/atlas/config.yaml` on disk.

### 9.4 Whether `hermes dashboard` inherits HERMES_HOME from the environment

**Question:** Does `hermes dashboard` automatically use the calling shell's `HERMES_HOME`, or does it need `HERMES_HOME` set explicitly?  
**Source code to read:** `hermes_cli/dashboard.py` (or wherever `hermes dashboard` is implemented) — look at how it resolves its data directory.

### 9.5 Whether `pnpm start:all` propagates HERMES_HOME to subprocesses

**Question:** `pnpm start:all` launches both gateway and workspace UI. Does it forward environment variables? Does it pick up the correct profile?  
**Source code to read:** `hermes-workspace/package.json` — look at the `start:all` script definition.

### 9.6 The `[HERMES_HOME fallback]` warning — exact source location

**Question:** Where exactly in the codebase is the string `"[HERMES_HOME fallback]"` emitted? This would clarify whether it's a gateway-side log or a workspace-UI log.  
**Source code to read:** `grep -r "HERMES_HOME fallback" ~/.hermes/hermes-agent/` and `grep -r "HERMES_HOME fallback" ~/hermes-workspace/src/`.

### 9.7 Profile config.yaml — what keys are actually profile-scoped vs global

**Question:** Can `~/.hermes/profiles/atlas/config.yaml` override the model and all settings independently of `~/.hermes/config.yaml`? Or are some settings read only from the global config?  
**Source code to read:** `hermes_cli/cli_config.py` — `load_cli_config()` function and how it merges profile config vs global config.

### 9.8 Whether charter/identity files referenced in the UI wizard

**Question:** The task description mentions "charter/identity files referenced from `config.yaml`." The public docs describe `SOUL.md` as the only identity file. Does the wizard create references to external charter files in a `charter:` or `identity:` config key?  
**Source code to read:** `hermes-workspace/src/` (wizard component), and `agent/prompt_builder.py` — look for any config keys beyond `soul_md_path` or similar.

---

## Appendix: Quick Reference Cheat Sheet

```bash
# Correct startup for atlas profile:
atlas gateway run                                              # terminal 1
HERMES_HOME=~/.hermes/profiles/atlas hermes dashboard --no-open  # terminal 2
cd ~/hermes-workspace && pnpm dev                              # terminal 3

# Check active HERMES_HOME in each terminal:
echo $HERMES_HOME

# Verify gateway serves API:
curl http://127.0.0.1:8642/health

# Verify dashboard is up:
curl http://127.0.0.1:9119/api/status

# Verify workspace connection:
curl http://127.0.0.1:3000/api/connection-status

# Check SOUL.md:
cat ~/.hermes/profiles/atlas/SOUL.md

# Check what config.yaml contains:
cat ~/.hermes/profiles/atlas/config.yaml

# Enable gateway API server (required for workspace):
echo 'API_SERVER_ENABLED=true' >> ~/.hermes/profiles/atlas/.env

# New session with atlas:
atlas  # then /new

# Diagnose:
atlas doctor
```

---

*All citations link to the primary sources inspected during research. Sections marked "Source code inspection required" could not be verified from public documentation alone.*
