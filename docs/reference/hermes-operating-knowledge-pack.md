# Hermes Operating Knowledge Pack

**Prepared for:** David Izzard — DavidOS / Atlas Profile  
**Context:** DigitalOcean VPS, Hermes Agent v0.13.0 (2026.5.7), NousResearch/Hermes architecture  
**Research date:** 2026-05  
**Complements:** [`hermes-internals.md`](./hermes-internals.md) — that file covers profiles, HERMES_HOME, SOUL.md identity mechanics, and v0.13.0 bugs. This pack covers **capabilities, operating rules, and build-ability**.  
**Primary sources:** [Hermes docs](https://hermes-agent.nousresearch.com/docs/), [Configuration docs](https://hermes-agent.nousresearch.com/docs/user-guide/configuration), [Tips docs](https://hermes-agent.nousresearch.com/docs/guides/tips), [Skills docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills), [FAQ](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/faq.md), [v0.13.0 release notes](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7), [Paperclip adapter](https://github.com/NousResearch/hermes-paperclip-adapter), consolidated principles at `docs/audits/preparation/2026-05-13-task2-consolidated-principles.md`

---

## CRITICAL QUESTION RESOLVED FIRST

### Can Hermes Build?

**Yes — but with precise caveats.**

"Build" in Hermes's model means different things at different layers:

| "Build" action | Hermes can do this? | Mechanism | Requires approval by default? |
|---|---|---|---|
| Write files to disk | **YES** — natively | `write_file` tool | **Yes** for sensitive paths; see `approvals` config |
| Run shell scripts | **YES** — natively | `terminal` tool (local, Docker, SSH, Modal, etc.) | **Yes** for flagged dangerous patterns |
| Execute arbitrary code | **YES** — natively | `execute_code` tool (Python, JS in session context) | Yes, subject to toolset config |
| Scaffold project directories | **YES** — natively | `write_file` + `terminal` together | Same as above |
| Create/modify databases | **YES** — via terminal | `terminal` runs `psql`, `sqlite3`, migrations, etc. | Yes for destructive SQL patterns |
| Commit to git | **YES** — via terminal | `terminal` runs `git` commands | Yes for push/force operations |
| Create persistent state in Hermes | **YES** — MEMORY.md + skill_manage | `memory_manage` + `skill_manage` tools | No (memory writes are direct) |
| Spawn subagents to do work in parallel | **YES** — natively since v0.12+ | `delegate_task` tool, multi-agent Kanban | No for dispatch; some operations gate |
| Run cron/scheduled jobs | **YES** — natively | `cron` tool, built-in gateway scheduler | No for schedule creation |
| Write to `~/.hermes/skills/` | **YES** — via `skill_manage` | `skill_manage create/edit/patch/delete` | Gated if `skills.guard_agent_created: true` (default: **false**) |
| Create skills from experience | **YES** — autonomously | The learning loop fires `skill_manage` after complex tasks | No by default |
| Design/recommend only | **NO** — this is NOT Hermes's model | Hermes takes action; it does not merely advise | N/A |

**The precise answer to "Can Hermes build?":**

> Hermes **can write files, run scripts, execute code, scaffold projects, run database commands, commit to git, create/modify its own skills, spawn subagents, and create persistent state** — all natively via tools. It is **not** a design-only recommender. It is an **actor**. Whether it acts without your approval depends on the `approvals` configuration (see Section H). On a default install, destructive/sensitive operations prompt for approval; routine writes and reads do not.

Sources: [Hermes docs — execute_code](https://hermes-agent.nousresearch.com/docs/), [Configuration — approvals](https://hermes-agent.nousresearch.com/docs/user-guide/configuration), [Configuration — code_execution](https://hermes-agent.nousresearch.com/docs/user-guide/configuration), [Tips — execute_code for batch](https://hermes-agent.nousresearch.com/docs/guides/tips)

---

## A. HERMES CAPABILITY MAP

### A1. Core Capabilities

| Capability | Status | Mechanism | Notes |
|---|---|---|---|
| **Chat / conversational AI** | Native | System prompt + LLM | Slot-assembled; session-persistent |
| **File read** | Native | `read_file` tool | Capped at `file_read_max_chars: 100000` (~25-35k tokens) by default |
| **File write** | Native | `write_file` tool | Post-write lint for Python/JSON/YAML/TOML (v0.13.0+) |
| **File patch** | Native | `patch` tool | Diff-style targeted updates |
| **Shell / terminal** | Native | `terminal` tool | 6 backends: local, Docker, SSH, Modal, Daytona, Singularity |
| **Code execution** | Native | `execute_code` tool | Python (+ JS) in session dir (`project` mode) or temp (`strict` mode) |
| **Web search** | Configurable | `web_search` tool | Backends: Firecrawl, SearXNG, Tavily, Exa, Parallel |
| **Web extract / browse** | Configurable | `web_extract`, `browser_navigate` | Firecrawl or browser automation |
| **Vision** | Configurable | `vision` tool | Multimodal models; image paste via Ctrl+V in CLI |
| **Scheduling (cron)** | Native | `cron` tool + gateway scheduler | `no_agent` watchdog mode (v0.13.0); delivers to any platform |
| **Agent spawning (delegation)** | Native | `delegate_task` tool | Up to `max_concurrent_children: 3` (configurable), depth 1–3 |
| **Multi-agent Kanban** | Native (v0.13.0+) | `/kanban` command + board | Durable board, heartbeat, reclaim, zombie detection, per-task retries |
| **Persistent Goals** | Native (v0.13.0+) | `/goal` command | Ralph loop — agent stays on target across turns |
| **Memory (MEMORY.md)** | Native | `memory_manage` tool | ~2200 chars limit; agent-curated; frozen snapshot at session start |
| **User profile (USER.md)** | Native | Honcho dialectic modeling | ~1375 chars; cross-session recall |
| **Skills** | Native | `skill_manage` + skills index | ~80+ bundled; agent creates them autonomously |
| **MCP client** | Configurable | `mcp` toolset | SSE + stdio transport; OAuth forwarding (v0.13.0+) |
| **Git operations** | Via terminal | `terminal` runs `git` | No native git toolset; runs git via shell |
| **Image generation** | Configurable | `image_gen` tool | Plugin-based; various providers |
| **TTS / STT / Voice** | Configurable | `tts`, `stt` tools | 8 TTS providers; Edge voice (322 voices); local Whisper |
| **Session search** | Native | `session_search` auxiliary | FTS5 cross-session recall with LLM summarization |
| **Context compression** | Native | `/compress` + auto | Fires at configurable threshold; preserves recent tail |
| **Checkpoints** | Configurable | `checkpoints` config | Filesystem snapshots before destructive ops (v0.13.0+: v2 rewrite) |
| **Autonomous skill improvement** | Native | Background self-improvement loop | Agent reviews and patches its own skills during use |

Sources: [Hermes main docs](https://hermes-agent.nousresearch.com/docs/), [Configuration docs](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)

### A2. What "Build" Means in Hermes's Actual Model

Hermes is not a recommender. Its model is: **receive task → plan using tools → execute tools → verify → persist artifacts**. The execution layer is real and immediate.

**What Hermes can build concretely:**

```
Code projects:
  - Write source files, configs, tests, Makefiles, Dockerfiles
  - Run build commands (make, pip install, npm build, cargo build)
  - Commit to git (write → stage → commit → push via terminal)

Databases:
  - Run psql/sqlite3/mysql via terminal
  - Write and execute migration scripts
  - Schema creation, table operations, data seeding
  - NOT: native DB connection (always via terminal subprocess)

Agent infrastructure:
  - Create/edit skills in ~/.hermes/skills/ (via skill_manage)
  - Write AGENTS.md, SOUL.md context files (via write_file)
  - Configure cron jobs (via cron tool)
  - Spawn subagents for parallel workstreams (delegate_task)

Persistent state:
  - MEMORY.md (facts, cross-session knowledge)
  - USER.md (user profile modeling)
  - Skills (procedural knowledge)
  - Session DB (conversation history with FTS5 search)
```

**What Hermes does NOT build autonomously (without approval by default):**

- Recursive deletions (`rm -rf`, `DROP TABLE`)
- Curl-to-shell pipes
- Operations on shell RC files and credential files
- Files outside the working directory tree (sensitive-write checks)

Sources: [Configuration — approvals](https://hermes-agent.nousresearch.com/docs/user-guide/configuration), [Tips — security](https://hermes-agent.nousresearch.com/docs/guides/tips), [v0.13.0 release notes](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7)

---

## B. CONFIGURATION MAP

### B1. File Locations

| File | Purpose | Scope |
|---|---|---|
| `$HERMES_HOME/config.yaml` | All non-secret configuration | Profile-scoped |
| `$HERMES_HOME/.env` | API keys, secrets, feature flags | Profile-scoped |
| `$HERMES_HOME/auth.json` | OAuth tokens (Nous Portal, etc.) | Profile-scoped (shared across profiles for Nous OAuth in v0.13.0+) |
| `$HERMES_HOME/SOUL.md` | Primary agent identity (slot #1 system prompt) | Profile-scoped |
| `$HERMES_HOME/memories/MEMORY.md` | Persistent facts memory | Profile-scoped |
| `$HERMES_HOME/memories/USER.md` | User profile model | Profile-scoped |
| `$HERMES_HOME/skills/` | All skills (bundled + hub + agent-created) | Profile-scoped |
| `$HERMES_HOME/cron/` | Cron job definitions | Profile-scoped |
| `$HERMES_HOME/sessions/` | Session database | Profile-scoped |
| `$HERMES_HOME/logs/` | `errors.log`, `gateway.log` (secrets auto-redacted) | Profile-scoped |

**For the atlas profile:** replace `$HERMES_HOME` with `~/.hermes/profiles/atlas/`. See [hermes-internals.md](./hermes-internals.md) §3 for HERMES_HOME mechanics.

### B2. Configuration Precedence

```
Priority 1 (highest): CLI arguments — e.g. hermes chat --model anthropic/claude-opus-4.7
Priority 2:           $HERMES_HOME/config.yaml — primary config for all non-secret settings
Priority 3:           $HERMES_HOME/.env — fallback for env vars; required for secrets
Priority 4 (lowest):  Built-in defaults — hardcoded safe defaults
```

When both `config.yaml` and `.env` set the same non-secret key, **config.yaml wins**. ([Configuration docs](https://hermes-agent.nousresearch.com/docs/user-guide/configuration))

### B3. Key config.yaml Namespaces

| Namespace | Controls |
|---|---|
| `model` | Default model, provider, base_url, context_length |
| `terminal` | Backend (local/docker/ssh/modal/daytona/singularity), cwd, timeout |
| `agent` | `max_turns` (default 90), `disabled_toolsets`, `reasoning_effort`, `tool_use_enforcement` |
| `skills` | `guard_agent_created`, `config.*` (per-skill settings), `external_dirs` |
| `memory` | `memory_enabled`, `memory_char_limit` (2200), `user_char_limit` (1375) |
| `approvals` | `mode`: `manual` / `smart` / `off` |
| `checkpoints` | `enabled`, `max_snapshots` |
| `delegation` | `max_concurrent_children`, `max_spawn_depth`, model/provider overrides for subagents |
| `compression` | `enabled`, `threshold` (0.50), `protect_last_n` (20) |
| `security` | `redact_secrets` (ON by default since v0.13.0), `website_blocklist`, `tirith_enabled` |
| `code_execution` | `mode` (project/strict), `timeout` (300s), `max_tool_calls` (50) |
| `auxiliary` | Per-task model overrides: `compression`, `vision`, `web_extract`, `approval`, `session_search` |
| `worktree` | Git worktree isolation per CLI session (default: false) |
| `display` | `tool_progress`, `show_cost`, `streaming`, `skin` |

### B4. Key Environment Variables

| Variable | Purpose | Where to set |
|---|---|---|
| `HERMES_HOME` | Scopes all state to a directory | Shell / systemd unit (DO NOT set in .env) |
| `API_SERVER_ENABLED` | Enables gateway HTTP API on :8642 | `$HERMES_HOME/.env` |
| `API_SERVER_HOST` | Bind address for gateway API (default: 127.0.0.1) | `.env` |
| `OPENROUTER_API_KEY` / `ANTHROPIC_API_KEY` | LLM provider credentials | `.env` |
| `FIRECRAWL_API_KEY` | Web backend | `.env` |
| `HERMES_YOLO_MODE` | Equivalent to `approvals.mode: off` | `.env` (danger!) |
| `MESSAGING_CWD` | Working directory for gateway sessions | `.env` |
| `TERMINAL_BACKEND` | Override terminal backend | `.env` |
| `HERMES_STREAM_READ_TIMEOUT` | Streaming timeout override | `.env` |

### B5. Inspecting Current Configuration

```bash
# View effective config:
hermes config show

# View specific value:
hermes config show | grep approvals

# Edit:
hermes config edit

# Set a value:
hermes config set agent.max_turns 120

# Check for missing required options:
hermes config check

# Migrate config after update:
hermes config migrate

# Full system health:
hermes doctor
```

Source: [Configuration docs](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)

---

## C. TOOL AND PERMISSION MAP

### C1. Tools Hermes Ships With (Default Toolsets)

| Toolset | Key tools |
|---|---|
| `terminal` | Run shell commands, scripts, background processes |
| `file` | `read_file`, `write_file`, `patch`, `find_files`, `list_directory` |
| `web` | `web_search`, `web_extract` |
| `browser` | `browser_navigate`, `browser_snapshot`, `browser_click`, `browser_type` |
| `code_execution` | `execute_code` (Python/JS in sandboxed context) |
| `vision` | Analyze images, video (v0.13.0+: `video_analyze`) |
| `memory` | `memory_manage` (read/write MEMORY.md and USER.md) |
| `skills` | `skills_list`, `skill_view`, `skill_manage` |
| `mcp` | Connect to any MCP server |
| `creative` | TTS, STT, image generation |
| `productivity` | Calendar, email, etc. (platform-dependent) |

Disable globally: `agent.disabled_toolsets: [web, browser]` in config.yaml.  
Disable per session: `hermes chat -t "terminal,file,skills"` (whitelist only named toolsets).

### C2. Adding Tools

1. **MCP servers**: Add to `mcp_servers:` in config.yaml. Any MCP-compatible server (filesystem, databases, APIs, etc.) integrates immediately.
2. **Skills**: Skills can invoke any tool Hermes has access to. They are context documents that guide the agent's use of existing tools — they don't add new tool binaries, but can orchestrate complex multi-tool workflows.
3. **External skills directories**: `skills.external_dirs` adds read-only skill discovery paths.
4. **Skills Hub**: `hermes skills install <source>/<skill>` installs community/official skills.
5. **Custom providers** (`custom_providers` in config.yaml): Adds new LLM endpoints.

Source: [Skills docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills), [Configuration docs](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)

### C3. Permission and Approval Mechanics

**Three approval modes** (set via `approvals.mode` in config.yaml):

| Mode | Behavior | Use case |
|---|---|---|
| `manual` | **Default**. Prompts before any flagged command. Options: once / session / always / deny. | Production, sensitive systems |
| `smart` | Auxiliary LLM assesses danger; low-risk auto-approved with session-level persistence | Trusted workflows with oversight |
| `off` | No checks. Equivalent to `HERMES_YOLO_MODE=true` | Sandboxed environments only |

**What triggers an approval prompt (default `manual` mode):**

- Recursive deletes: `rm -rf`, `rmdir /s`, etc.
- Destructive SQL: `DROP TABLE`, `DELETE FROM` (without WHERE), `TRUNCATE`
- Piping curl to shell: `curl ... | bash`
- Writing to shell RC files (`.bashrc`, `.zshrc`)
- Writing to credential files (`.env`, `auth.json`, SSH keys)
- Reading from `/etc/passwd`, `/etc/shadow`
- Any pattern matching Hermes's curated dangerous command list

**Important: Container backends skip dangerous-command checks** — Docker, Singularity, Modal, and Daytona bypass the approval system because the container is the security boundary. If you use `terminal.backend: docker`, lock down the image.

**Skill guard**: `skills.guard_agent_created: true` adds an approval prompt when the agent tries to create/edit/delete skills via `skill_manage`. Default is **false** (agent writes skills freely).

**What Hermes does WITHOUT approval in default mode:**

- Reading any file in the working directory
- Writing new files (non-sensitive paths)
- Running non-dangerous shell commands
- Web search and extraction
- Creating/updating memory (MEMORY.md, USER.md)
- Creating/editing skills (unless `guard_agent_created: true`)
- Spawning subagents
- Creating cron jobs
- Running Python via `execute_code`

Source: [Configuration — approvals](https://hermes-agent.nousresearch.com/docs/user-guide/configuration), [Tips — security](https://hermes-agent.nousresearch.com/docs/guides/tips), [v0.13.0 release notes](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7)

### C4. "Hermes Can Call X" vs "Will Call X Without Approval"

| Tool/Action | Can call? | Will call without approval? |
|---|---|---|
| Write non-sensitive file | Yes | **Yes** |
| Write .env, .bashrc, credentials | Yes | No — triggers approval |
| Run `rm -rf` | Yes | No — triggers approval |
| Run `git add && git commit` | Yes | **Yes** |
| Run `git push` | Yes | Depends on `git push --force` pattern |
| Execute Python via `execute_code` | Yes | **Yes** |
| Web search | Yes | **Yes** |
| Create memory entry | Yes | **Yes** |
| Create/edit a skill | Yes | **Yes** (unless guard enabled) |
| Spawn subagent | Yes | **Yes** |
| Create a cron job | Yes | **Yes** |
| Run Docker command | Yes | **Yes** (if Docker backend in use) |
| Run database commands | Yes (via terminal) | Depends on SQL patterns — DDL drops trigger approval |

---

## D. MEMORY AND SKILLS MAP

### D1. Context Files and Their Roles

| File | Location | Slot in system prompt | What it controls | Loaded how |
|---|---|---|---|---|
| `SOUL.md` | `$HERMES_HOME/SOUL.md` | Slot #1 (replaces built-in identity) | Primary identity/charter | At session start by `load_soul_md()` |
| `MEMORY.md` | `$HERMES_HOME/memories/MEMORY.md` | Slot #5 | Persistent facts (agent-curated; ~2200 chars) | Frozen snapshot at session start |
| `USER.md` | `$HERMES_HOME/memories/USER.md` | Slot #6 | User profile model (Honcho; ~1375 chars) | Frozen snapshot at session start |
| `AGENTS.md` | CWD at launch (hierarchical) | Slot #8 | Project-specific instructions, conventions | CWD discovery + lazy subdirectory loading |
| `.hermes.md` / `HERMES.md` | CWD → git root | Slot #8 (highest priority) | Project instructions | Walk to git root |
| `CLAUDE.md` | CWD only | Slot #8 (fallback) | Claude Code context compatibility | Detected automatically |
| `.cursorrules` | CWD only | Slot #8 (fallback) | Cursor IDE rules | Detected automatically |
| `.cursor/rules/*.mdc` | CWD only | Slot #8 (fallback) | Cursor rule files | Detected automatically |
| `AGENTS.md` (subdirectory) | Lazily from tool call paths | Injected into tool results | Per-directory conventions | Loaded lazily, not at session start |

**Loading priority for project context (slot #8):** `.hermes.md` → `HERMES.md` → `AGENTS.md` → `CLAUDE.md` → `.cursorrules`. Only one file type is loaded; the first match wins.

**Memory is a frozen snapshot** — changes made during a session don't appear in the system prompt until the next session. The agent writes to disk immediately, but the prompt isn't invalidated mid-session. ([Tips docs](https://hermes-agent.nousresearch.com/docs/guides/tips))

### D2. Skills Folder Structure

```
~/.hermes/skills/
├── .bundled_manifest          # tracks seeded bundled skills by content hash
├── .hub/
│   ├── lock.json              # hub installation state
│   ├── quarantine/            # quarantined skills
│   └── audit.log              # security audit log
├── mlops/
│   └── axolotl/
│       ├── SKILL.md           # main instructions (required)
│       ├── references/        # additional docs
│       ├── templates/         # output formats
│       ├── scripts/           # helper scripts
│       └── assets/            # supplementary files
└── devops/
    └── deploy-k8s/
        └── SKILL.md
```

Source: [Skills docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)

### D3. Skill Authoring (SKILL.md Format)

```markdown
---
name: my-skill
description: Brief description of what this skill does
version: 1.0.0
platforms: [linux]                    # optional: restrict to OS
metadata:
  hermes:
    tags: [python, automation]
    category: devops
    fallback_for_toolsets: [web]      # hide when web toolset available
    requires_toolsets: [terminal]     # hide when terminal unavailable
    config:
      - key: api_endpoint
        description: API server URL
        default: "http://localhost:8080"
---

# Skill Title

## When to Use
[Trigger conditions]

## Procedure
[Step-by-step instructions]

## Pitfalls
[Known failure modes]

## Verification
[How to confirm it worked]
```

### D4. Skill Discovery: How Hermes Decides Which Skill to Load

1. At session start, the skills index (~3k tokens) is compiled and injected into slot #7 of the system prompt. This lists all available skills by name, description, and category.
2. When the agent encounters a task, it matches the task against skill descriptions in the index.
3. When a match is found, the agent calls `skill_view(name)` to load the full SKILL.md content.
4. Conditional skills (`fallback_for_toolsets`, `requires_toolsets`) are hidden/shown based on active tool availability — the model never sees hidden skills.
5. Skills invoked via slash commands (`/skill-name`) bypass the matching step and load immediately.

Source: [Skills docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)

### D5. Key Slash Commands

| Command | Effect |
|---|---|
| `/skills` or `/skills list` | List installed skills |
| `/skills browse` | Browse Skills Hub |
| `/skills search <query>` | Search hub |
| `/skills install <source>/<name>` | Install a skill |
| `/usage` | Show token consumption for current session |
| `/insights` | 30-day usage pattern overview |
| `/verbose` | Cycle tool output display: off → new → all → verbose |
| `/compress` | Compress conversation history (run before hitting context limits) |
| `/goal <description>` | Set persistent cross-turn goal (Ralph loop, v0.13.0+) |
| `/model` | Switch model mid-session |
| `/new` | Start a new session |
| `/personality <name>` | Apply a named personality overlay (slot #11) |
| `/kanban` | Multi-agent Kanban board commands |
| `/reasoning [level]` | Control reasoning effort level |
| `/title <name>` | Name the current session for later resume |
| `hermes -c` | Resume last session |
| `hermes -r "title"` | Resume session by title |

---

## E. PAPERCLIP INTEGRATION MAP

### E1. What Paperclip Is

[Paperclip](https://paperclip.ing) is a managed agent orchestration platform. The [hermes-paperclip-adapter](https://github.com/NousResearch/hermes-paperclip-adapter) (MIT license) integrates Hermes Agent as a "managed employee" in a Paperclip company.

### E2. How the Adapter Works

The adapter spawns Hermes CLI in single-query mode (`hermes chat -q`). Hermes processes the task using its full tool suite, then exits. The adapter:

1. Captures stdout/stderr and parses token usage, session IDs, and cost
2. Parses raw output into structured `TranscriptEntry` objects (tool cards with status icons)
3. Post-processes Hermes ASCII formatting into clean GFM markdown
4. Reclassifies benign stderr (MCP init, structured logs)
5. Tags sessions as `tool` source (separate from interactive usage)
6. Reports results back to Paperclip with cost and usage

**Session persistence** works via Hermes's `--resume` flag — each Paperclip heartbeat picks up where the last left off, maintaining conversation context, memories, and tool state.

### E3. Capabilities the Adapter Adds

| Capability | Detail |
|---|---|
| Skills integration | Scans both Paperclip-managed and Hermes-native skills (`~/.hermes/skills/`); sync/list/resolve APIs |
| Comment-driven wakes | Agents wake to respond to issue comments, not just task assignments |
| Auto model detection | Reads `~/.hermes/config.yaml` to pre-populate UI with configured model |
| Filesystem checkpoints | Optional `--checkpoints` for rollback safety |
| Thinking effort control | Passes `--reasoning-effort` for thinking/reasoning models |
| Structured transcript parsing | Typed `TranscriptEntry` objects for Paperclip's UI (tool cards, expand/collapse) |

### E4. Paperclip Status for DavidOS

**ADR-003 has frozen Paperclip adoption for DavidOS.** This is the correct operational choice. The Paperclip adapter is the **reference implementation** for how external orchestration systems should invoke Hermes — the adapter pattern (single-query mode, session resume, structured transcript parsing) is an architectural pattern David can adopt for custom integrations without Paperclip itself.

**What Paperclip's adapter tells us about Hermes's build capability:** The adapter treats Hermes as a full build agent — it assigns issues, Hermes uses all 30+ tools to complete work, and reports back. This confirms Hermes's build-layer competence.

Source: [Paperclip adapter README](https://github.com/NousResearch/hermes-paperclip-adapter)

---

## F. BEST-PRACTICES OPERATING GUIDE

### F1. From the Official Tips Docs

**Effective prompting for build-style work:**

- Provide context up front: file paths, error messages, expected behavior. Front-load the request.
- Say `"find and fix the failing test"` rather than dictating every step. Hermes has file search, terminal access, and code execution — let it explore.
- For 5+ step workflows you'll repeat, ask Hermes to create a skill: `"save what you just did as a skill called deploy-staging."` Next time: `/deploy-staging`.
- Use `execute_code` for batch operations. `"Write a Python script to rename all .jpeg files to .jpg and run it"` is cheaper than individual file operations.
- Use `delegate_task` for parallel research or independent workstreams — each subagent runs with its own context; only final summaries return to the main session.

**Context files for recurring instructions:**

- Put project-level rules in `AGENTS.md` (FastAPI backend, testing conventions, never commit .env). It's injected automatically every session.
- Use SOUL.md for durable identity/behavior. Use AGENTS.md for project-specific instructions. Keep both focused and concise — every character costs tokens.

**Performance and cost:**

- Run `/compress` before hitting context limits; use `/usage` to monitor.
- Don't change the model or system prompt mid-session — this breaks the provider's prompt cache and makes subsequent messages significantly more expensive.
- Use frontier models for architecture decisions; switch to faster models for boilerplate, formatting, or renaming.
- Delegate parallel workstreams to subagents to dramatically reduce the main session's token usage.

Source: [Tips docs](https://hermes-agent.nousresearch.com/docs/guides/tips)

### F2. Anti-Patterns the Docs Explicitly Warn Against

| Anti-pattern | Why it's bad | Source |
|---|---|---|
| Setting `GATEWAY_ALLOW_ALL_USERS=true` on a bot with terminal access | Anyone who finds the bot has shell access to your VPS | [Tips — security](https://hermes-agent.nousresearch.com/docs/guides/tips) |
| Choosing "always" for dangerous command approvals immediately | Permanently allowlists a destructive pattern | [Tips — security](https://hermes-agent.nousresearch.com/docs/guides/tips) |
| Running without Docker/Singularity on untrusted code | Destructive commands can harm the host | [Tips — security](https://hermes-agent.nousresearch.com/docs/guides/tips) |
| Changing model mid-session | Breaks prompt cache; significantly more expensive | [Tips — performance](https://hermes-agent.nousresearch.com/docs/guides/tips) |
| Not running `hermes config check` after updates | May miss new required config options | [Configuration docs](https://hermes-agent.nousresearch.com/docs/user-guide/configuration) |
| Relying on `hermes status` for diagnosis (v0.13.0) | Known bug: misreports with custom HERMES_HOME | [Issue #14517](https://github.com/NousResearch/hermes-agent/issues/14517) |

### F3. Recommended Workflow Patterns for DavidOS

**Pattern: Build-and-capture**
1. Ask Hermes to complete a build task (scaffold project, write code, set up DB)
2. If it uses 5+ steps, immediately follow up: `"Save what you just did as a skill"`
3. The skill becomes reusable infrastructure, not one-off labor (aligns with P4: every workflow produces a reusable asset)

**Pattern: Goal-driven deep work**
1. Set a persistent goal: `/goal Build the DavidOS information model schema`
2. Hermes stays locked on this across turns, surviving `/compress` and context pressure
3. Use when the task requires multiple turns without distraction

**Pattern: Parallel research via delegation**
1. `"Research these three topics in parallel, delegate each as a subagent, and return a synthesis"`
2. Reduces main session token usage; each subagent runs independently
3. Use for DavidOS bottleneck analysis, technology evaluation, competitive research

**Pattern: Cron-based maintenance**
1. Create cron jobs for recurring DavidOS housekeeping (memory consolidation, skill review, log analysis)
2. `no_agent` cron mode (v0.13.0+) runs scripts without LLM cost when no reasoning is needed
3. Deliver results to Telegram home channel via `/sethome`

---

## G. KNOWN LIMITATIONS AND FAILURE MODES

### G1. From GitHub Issues (v0.13.0+)

| Issue | Symptom | Status | Impact for DavidOS |
|---|---|---|---|
| [#14517](https://github.com/NousResearch/hermes-agent/issues/14517) (open) | `hermes status` misreports session counts and .env presence with custom HERMES_HOME | Open | Use `hermes doctor` instead of `hermes status` for atlas profile |
| [#5200](https://github.com/NousResearch/hermes-agent/issues/5200) (open) | Docs say SOUL.md checks CWD; code only reads from HERMES_HOME | Open (docs bug) | Trust the code, not the docs; SOUL.md is only ever from $HERMES_HOME |
| [#262](https://github.com/outsourc-e/hermes-workspace/issues/262) (open) | Conductor tab shows placeholder; required API endpoint not yet in hermes-agent | Open | Conductor/mission dispatch does not work |
| Memory is a frozen snapshot | Changes during session don't appear until next session | By design | Plan memory updates for between sessions, not during |
| `max_turns: 90` default | Agent silently stops at 90 iterations; generates a summary | By design | Increase for long build tasks: `agent.max_turns: 150` |
| Parallel subagents share one Docker container | Can collide on filesystem writes | By design | Use unique working directories per subagent |
| Skills index is ~3k tokens always | Even if you have many skills, index grows | By design | Be selective; disable unused skills per platform |
| [#25332](https://github.com/NousResearch/hermes-agent/issues/25332) (P1) | Gateway memory leak on cached agent and session expiry | Fix in main (post-v0.13.0) | May affect long-running VPS gateway; update from main |
| [#25315](https://github.com/NousResearch/hermes-agent/issues/25315) (P1) | Gateway memory leak — _evict_cached_agent + _session_messages never cleared | Fix in main | Same — update frequently |
| [#12586](https://github.com/NousResearch/hermes-agent/issues/12586) | Context compaction summaries emit function-call-shaped pseudo tool calls with truncated arguments | P2, open | After `/compress`, carefully check that tool state is clean before issuing build commands |
| TOCTOU race fixes wave | Multiple concurrent singleton init races | Fixes in main, post-v0.13.0 PRs | On VPS with `hermes update` from main, these are auto-applied |

### G2. What Hermes Does Well vs. Poorly

**Does well:**
- File I/O and code scaffolding (native, fast, reliable)
- Python execution via `execute_code`
- Multi-step terminal workflows with error recovery
- Memory curation and skill creation over time (learning loop is real)
- Session search / FTS5 recall
- Cron scheduling with delivery to messaging platforms
- Context compression (auto-fires; generally preserves key context)
- Multi-agent Kanban with reliability primitives (v0.13.0+)

**Does poorly or unreliably:**
- Very long sessions (100+ turns) — context pressure and memory leak risks
- Parallel subagents on Docker backend (container sharing)
- Conductor feature (not functional — UI placeholder only)
- `hermes status` with custom HERMES_HOME (use `hermes doctor`)
- Memory updates mid-session (frozen snapshot; writes to disk but not visible until next session)
- Gemini parallel tool call parsing (Issue #25333 — JSON parser drops some tool calls)

Sources: [v0.13.0 release notes](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7), [GitHub open issues](https://github.com/NousResearch/hermes-agent/issues)

---

## H. SECURITY AND AUTONOMY BOUNDARIES

### H1. Default Autonomy Posture

Hermes ships with **`approvals.mode: manual`** — meaning it prompts before executing any command matching the dangerous-pattern list. This is the correct default for a VPS with real consequences.

**Secret redaction is ON by default since v0.13.0** — API keys and secrets are redacted from logs automatically. Previously this was off. ([v0.13.0 release notes](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7))

### H2. Increasing / Decreasing Autonomy

```yaml
# More autonomous (trust the agent more):
approvals:
  mode: smart      # LLM-assessed risk; low-risk auto-approved

# Maximum autonomy (sandbox only!):
approvals:
  mode: off        # no checks at all
# OR: HERMES_YOLO_MODE=true in .env

# More controlled:
approvals:
  mode: manual     # default — prompt for every flagged command

skills:
  guard_agent_created: true   # prompt before agent creates/edits skills

checkpoints:
  enabled: true    # snapshot filesystem before destructive ops
  max_snapshots: 20
```

### H3. What Hermes WILL NOT do without approval (default manual mode):

- Recursive deletes
- Drop/truncate SQL operations
- Curl-to-shell pipes
- Write to shell RC files or credential files
- Write to SSH key files
- Actions blocked by the website blocklist (if configured)
- Any pattern on the curated dangerous-command list

### H4. What Hermes WILL do without approval (potentially surprising):

- Create and edit files in the working directory tree
- Run Python via `execute_code` (scripts run immediately)
- Write to MEMORY.md and USER.md (memory changes are silent)
- Create and edit skills via `skill_manage` (unless guard enabled)
- Spawn subagents (`delegate_task`)
- Create cron jobs
- Git add/commit (but not push with `--force`)
- Run `npm install`, `pip install`, `apt install` — package installs are NOT on the dangerous list by default
- Web search and content extraction

### H5. Recommended Security Configuration for DavidOS VPS

```yaml
# $HERMES_HOME/config.yaml
approvals:
  mode: smart      # LLM-assesses risk; reduces friction while maintaining oversight

skills:
  guard_agent_created: true    # require approval before Hermes modifies its own skills

checkpoints:
  enabled: true
  max_snapshots: 20

security:
  redact_secrets: true         # already on by default in v0.13.0+
  website_blocklist:
    enabled: false             # enable + add internal VPS admin URLs if needed

terminal:
  backend: local               # or docker for untrusted code

# $HERMES_HOME/.env
GATEWAY_ALLOW_ALL_USERS=false  # Never set true if terminal access is enabled
TELEGRAM_ALLOWED_USERS=<david's telegram user ID>
```

**Do not use `approvals.mode: off` on the VPS unless you are running an ephemeral sandbox.** A single misunderstood instruction can delete production data.

Sources: [Configuration — security](https://hermes-agent.nousresearch.com/docs/user-guide/configuration), [Tips — security](https://hermes-agent.nousresearch.com/docs/guides/tips), [v0.13.0 release notes](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7)

---

## I. RECOMMENDED DAVIDOS CONFIGURATION CHANGES

*Based on Sections A–H, cross-referenced against [consolidated principles](../audits/preparation/2026-05-13-task2-consolidated-principles.md).*

### I1. What Should Become a Skill

| Skill to create | Why | Aligns with principle |
|---|---|---|
| `davidos-session-open` | Standard session startup procedure: load current context, check bottleneck status, load memory, set working goal | P3 (router), P7 (bottleneck) |
| `davidos-router` | Given an incoming request: emit work type, required context, risk tier, tool, output format, approval requirement | P3 (strong router) |
| `davidos-asset-capture` | After any completed workflow: identify what reusable asset was produced; save to the right library | P4 (every workflow produces an asset) |
| `davidos-evaluation` | For any important output: compare against expected baseline; log input/output/confidence | P5 (evaluation) |
| `davidos-memory-consolidate` | Periodic: consolidate MEMORY.md; remove stale entries; add session learnings | P1 (information architecture) |
| `davidos-bottleneck-check` | Weekly: which of the 7 bottlenecks is currently binding? Update the bottleneck document | P7 (binding bottleneck) |
| `davidos-approval-classify` | For any action Atlas wants to take: classify against ADR-004 canonical list; determine rung | P6 (graduated autonomy) |

**How to create these:** Ask Atlas in a session: `"Create a skill called davidos-router that implements the following routing procedure..."` Then verify with `/skills list`.

### I2. What Should Become AGENTS.md Context

The `AGENTS.md` at the DavidOS repo root should contain (injected at every session start):

```markdown
# DavidOS Project Context

## System Identity
- This is DavidOS — a personal AI operating system for David Izzard.
- Atlas is the primary agent profile (HERMES_HOME=~/.hermes/profiles/atlas).
- The governing charter is at docs/charter/outcomes-and-frustrations-2026-05-13.md.

## Architecture Principles (from consolidated-principles.md)
1. Information architecture before agents — define schema before building
2. Named layers; no layer owns strategy
3. Strong router before more agents
4. Every workflow produces a reusable asset; otherwise it is labor
5. Without evaluation you have production volume, not compounding
6. Graduate autonomy by risk; never automate values, taste, or irreversible bets
7. Build around the binding bottleneck, not the most annoying feature

## Approval Rules (ADR-004)
- Any action requiring approval: consult docs/decisions/approvals-log.md
- Default to Light approval for exploratory work; Full approval for consequential changes

## Output Conventions
- Decisions go in docs/decisions/
- Session outputs go in docs/sessions/submitted/
- All workflows should produce a named reusable asset
```

### I3. What Should Become SOUL.md Behavior

The atlas SOUL.md should encode (these are identity-level behaviors, not project-level):

- The Atlas name, purpose, and operating stance
- The epistemic honesty rule: surface confidence, distinguish "I don't know" from fabrication (addresses the O11/no-bullshit gap from consolidated principles)
- The "inventive and commercial lens" rule: every output should consider monetization angles (addresses O7/O8 gap)
- The autonomy defaults: what Atlas initiates vs. waits for approval on
- The evaluation habit: every important output is assessed against explicit criteria before delivery

### I4. What Should Become Memory

| Memory item | Type | Where |
|---|---|---|
| David's VPS architecture (IP, services, ports, paths) | Fact | MEMORY.md |
| David's preferred models for different task types | Preference | MEMORY.md |
| Active HERMES_HOME path for atlas | Fact | MEMORY.md |
| DavidOS repo path on VPS | Fact | MEMORY.md |
| Current binding bottleneck (from P7 check) | State | MEMORY.md |
| David's communication style preferences | Profile | USER.md |
| David's commercial goals / income targets | Profile | USER.md |

**To add:** During a session, say `"Add to memory: the DavidOS repo lives at /path/to/repo and the atlas profile gateway runs as hermes-gateway-atlas.service"`.

### I5. What Should Become a Workflow

| Workflow | Description | Implementation |
|---|---|---|
| Weekly bottleneck review | Run `/davidos-bottleneck-check`, update bottleneck doc, decide next priority | Cron job or manual trigger |
| Session open / close ritual | Open: load context + set goal. Close: produce asset + update memory | Skills (I1) |
| Asset capture after build | After any build: identify reusable output; save to library | Skill (I1) |
| ADR creation | When a significant architectural decision is made, create ADR in standard format | Skill |
| Memory consolidation | Periodic: trim stale MEMORY.md entries, add recent learnings | Cron `no_agent` mode |

### I6. What Should Become an Evaluation Test

Based on P5 (evaluation) from consolidated principles and the O11 no-bullshit gap:

| Evaluation test | What it checks | How to implement |
|---|---|---|
| Atlas identity canary | Does Atlas's SOUL.md load correctly? (See hermes-internals.md §8) | Insert canary string; verify echo |
| Router quality | Given 10 sample requests, does the router correctly classify work type, risk tier, and approval requirement? | Manual test set |
| Asset production rate | For last 5 workflows, did each produce a named reusable asset? | Audit docs/sessions/ |
| Memory accuracy | Is MEMORY.md current? No stale entries older than 30 days that have been superseded? | Periodic review |
| Bottleneck currency | Is the bottleneck document current (updated in last 7 days)? | Date check |
| Approval compliance | Were all ADR-004 canonical actions gated through the approval log? | Audit approvals-log.md |

---

## J. WEEKLY REFRESH PROCESS

### J1. What to Check and How Often

| Check | Frequency | How |
|---|---|---|
| Hermes release notes / changelog | Weekly | `gh api repos/NousResearch/hermes-agent/releases/latest` or [GitHub releases](https://github.com/NousResearch/hermes-agent/releases) |
| Open P0/P1 issues | Weekly | `gh api "repos/NousResearch/hermes-agent/issues?labels=P0,P1&state=open"` |
| `hermes update` | Weekly | `atlas hermes update` — pulls latest main, syncs skills |
| `hermes config check` | After each update | `hermes config check` — detects missing required options |
| hermes-workspace issues | Bi-weekly | [outsourc-e/hermes-workspace issues](https://github.com/outsourc-e/hermes-workspace/issues) |
| Paperclip adapter (historical reference) | Monthly | [hermes-paperclip-adapter](https://github.com/NousResearch/hermes-paperclip-adapter) — monitor for patterns, even if not adopting |
| Skills Hub for new relevant skills | Monthly | `hermes skills check` + `hermes skills browse` |
| Memory consolidation | Weekly | Ask Atlas to "consolidate memory and remove stale entries" |

### J2. Signals That This Knowledge Pack Is Stale

- `hermes --version` shows a version tag later than `v2026.5.7`
- `hermes config check` reports missing options not documented here
- A new config section appears under `hermes config show` that isn't listed in Section B3
- An approval behavior changes (check [security docs](https://hermes-agent.nousresearch.com/docs/user-guide/security))
- The Conductor feature becomes functional (Issue [#262](https://github.com/outsourc-e/hermes-workspace/issues/262) closed)
- `skills.guard_agent_created` default changes
- A new terminal backend is added

### J3. Refresh Procedure

```bash
# 1. Update Hermes:
atlas hermes update

# 2. Check for config changes:
hermes config check
hermes config migrate   # if check reports gaps

# 3. Check release notes:
gh api repos/NousResearch/hermes-agent/releases/latest --jq '.body' | head -50

# 4. Check open P0/P1 issues:
gh api "repos/NousResearch/hermes-agent/issues?state=open&per_page=10&sort=updated" \
  --jq '[.[] | select(.labels[].name | test("P0|P1")) | {number, title}]'

# 5. Update this pack's version note and any changed sections.
```

---

## OPERATIONAL RULES FOR DAVIDOS

### 1. What Hermes Can Do (Definitive List)

- **Files**: Read, write, patch, find, list — any file accessible to the process user
- **Shell**: Execute any command in the terminal backend (local/Docker/SSH/Modal)
- **Code**: Run Python and JS via `execute_code`; write and execute scripts
- **Build**: Scaffold projects, write source files, run build tools, commit to git
- **Databases**: Run psql/sqlite3/mysql via terminal; schema operations; migrations
- **Web**: Search (multiple backends), extract page content, browse with browser automation, vision
- **Memory**: Read/write MEMORY.md and USER.md (persistent across sessions)
- **Skills**: Create, edit, delete, and invoke skills; autonomously create skills after complex tasks
- **Scheduling**: Create and run cron jobs; deliver to any messaging platform
- **Delegation**: Spawn isolated subagents (up to 3 concurrent, depth 1–3)
- **Multi-agent Kanban**: Durable board with heartbeat, reclaim, retry (v0.13.0+)
- **Persistent Goals**: `/goal` keeps agent on target across turns (v0.13.0+)
- **MCP**: Connect to any MCP server for extended tool capabilities
- **Voice**: TTS/STT in voice mode
- **Session search**: FTS5 recall of past conversations

### 2. What Hermes Can Do Reliably (Production-Ready Subset)

- File read/write/patch (stable, post-write lint in v0.13.0)
- Single-session Python/JS via `execute_code`
- Terminal command execution (local or SSH)
- Web search and extraction
- Git operations (add, commit, push — non-destructive paths)
- Memory curation and skill creation (learning loop is stable)
- Cron scheduling and delivery
- Context compression with `/compress`
- Session resume (`hermes -c`)
- Subagent delegation for research/parallel workstreams

### 3. What Hermes Should Not Do (Anti-Patterns + Dangers)

- **Set `approvals.mode: off` on a live VPS** without sandboxing
- **Set `GATEWAY_ALLOW_ALL_USERS=true`** on a bot with terminal access
- **Choose "always" for dangerous command approvals** until you understand the pattern
- **Rely on `hermes status`** for diagnosis with atlas profile — use `hermes doctor`
- **Run destructive operations mid-session without checkpoints** enabled
- **Work in extremely long sessions (100+ turns)** without `/compress` — memory leak risk
- **Skip `hermes config check` after `hermes update`**
- **Use Conductor** — not functional (UI placeholder only)
- **Trust memory mid-session** — memory writes are immediate to disk but the session snapshot is frozen at start

### 4. What Requires David Approval (Operational Gates)

**Always gate (default `manual` approval system):**
- Recursive deletes
- SQL DROP / TRUNCATE / DELETE without WHERE
- Curl-to-shell
- RC file or credential file writes
- Any action on ADR-004's canonical "requires approval" list

**Consider gating via `skills.guard_agent_created: true`:**
- Atlas creating or modifying its own skills

**Gate manually (process discipline, not Hermes mechanism):**
- Changes to SOUL.md (identity-level changes)
- Changes to ADR documents
- New cron jobs that will run unattended
- Subagent spawns targeting external services (not just local files)

### 5. What Should Become a Skill (Specific for DavidOS)

1. `davidos-router` — request classification (work type, context, risk tier, tool, approval)
2. `davidos-session-open` — standard session startup ritual
3. `davidos-asset-capture` — identify and save reusable output after any workflow
4. `davidos-evaluation` — evaluate important output against explicit criteria
5. `davidos-bottleneck-check` — identify and document binding bottleneck
6. `davidos-approval-classify` — classify actions against ADR-004 list
7. `davidos-memory-consolidate` — periodic memory pruning and reinforcement
8. Any 5+ step workflow David repeats more than twice

### 6. What Should Become AGENTS.md Context

- DavidOS's 7 architectural principles (from consolidated-principles.md)
- Project directory structure and file conventions
- ADR-004 approval rules and canonical list reference
- Atlas profile identity context and operating stance
- Active bottleneck status (updated weekly by `davidos-bottleneck-check`)
- Current sprint focus / active goals

### 7. What Should Become SOUL.md Behavior

- Atlas's name, charter, and strategic orientation
- **Epistemic honesty rule**: distinguish confident knowledge from inference; say "I don't know" rather than fabricating; surface uncertainty explicitly (addresses O11 no-bullshit gap from consolidated principles)
- **Inventive-commercial lens**: every output surfaces whether there's an approach David hasn't considered; every significant workflow surfaces potential monetization angles (addresses O7/O8 gaps)
- **Autonomy defaults**: what Atlas initiates vs. waits for David's explicit instruction
- **Evaluation habit**: important outputs are assessed before delivery

### 8. What Should Become Memory

- VPS architecture facts (IPs, service names, ports, file paths)
- Atlas profile path and gateway service name
- David's preferred models per task type
- DavidOS repo path and active branch conventions
- Current binding bottleneck (P7 — updated weekly)
- Active sprint goals
- David's commercial goals and income targets
- API keys / tool integrations that are active vs. not yet configured

### 9. What Should Become a Workflow

| Workflow | Trigger | Output |
|---|---|---|
| Session open ritual | Every new Atlas session | Goal set; current context loaded; bottleneck noted |
| Session close ritual | End of productive session | Asset captured; memory updated; next action noted |
| Weekly bottleneck check | Weekly cron | Bottleneck document updated; next priority clear |
| ADR creation | Any significant architectural decision | ADR file created; approvals-log entry added |
| Build task capture | After any 5+ step build | Skill created; asset logged in library |
| Memory consolidation | Monthly cron (`no_agent` mode) | MEMORY.md trimmed; stale entries removed |

### 10. What Should Become an Evaluation Test

| Test | Success criterion | When to run |
|---|---|---|
| Atlas identity canary | ATLAS canary string echoed from SOUL.md | After any restart or update |
| Router classification accuracy | 9/10 sample requests correctly classified | Weekly |
| Asset production rate | 4/5 last workflows produced named reusable asset | Weekly audit |
| Memory currency | No MEMORY.md entry stale > 30 days without review | Monthly |
| Bottleneck document currency | Bottleneck doc updated in last 7 days | Weekly |
| Approval compliance | All ADR-004 canonical actions logged in approvals-log.md | Monthly audit |
| No-bullshit check | Last 3 Atlas outputs include explicit confidence markers where appropriate | Per session |

---

## Reference: Quick Diagnostic Commands

```bash
# Atlas profile health:
HERMES_HOME=~/.hermes/profiles/atlas hermes doctor

# Gateway status:
curl http://127.0.0.1:8642/health
curl http://127.0.0.1:9119/api/status

# SOUL.md active:
cat ~/.hermes/profiles/atlas/SOUL.md | head -5

# Config effective values:
HERMES_HOME=~/.hermes/profiles/atlas hermes config show

# Recent issues (P0/P1):
gh api "repos/NousResearch/hermes-agent/issues?state=open&per_page=20&sort=updated" \
  --jq '[.[] | select(.labels[]?.name | test("P0|P1")) | {number, title}]'

# Check for config gaps after update:
HERMES_HOME=~/.hermes/profiles/atlas hermes config check

# Skills list:
HERMES_HOME=~/.hermes/profiles/atlas hermes skills list

# Update:
HERMES_HOME=~/.hermes/profiles/atlas hermes update
```

---

*All citations link to primary sources. Claims that could not be verified from sources are marked INFERENCE. For identity mechanics (HERMES_HOME, SOUL.md loading, v0.13.0 profile bugs), see the companion file [hermes-internals.md](./hermes-internals.md).*
