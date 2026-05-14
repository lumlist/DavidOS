# DavidOS Action Map — v0.1

**Status:** Canonical action-category-to-autonomy-rung map for DavidOS. Authored 2026-05-14 by David (operator) with Sonnet/Computer drafting support. Conforms to the schema at `SCHEMA.md`.

**Version:** 0.1 (initial population, pre-activation)

**Coverage:** 22 categories across five domains: file and repo operations, shell and code execution, Atlas-internal operations, external-reaching operations, structural and identity operations.

**Use:** Read the [README.md](README.md) for orientation. The `davidos-router` skill (to be built in Phase 1) consults this file and `modifiers.md` to compute the final rung per request.

**Companion files:** `SCHEMA.md` (rung and field definitions), `modifiers.md` (actor/context rules), `README.md` (orientation).

**Design reasoning:** `../audits/preparation/2026-05-13-autonomy-map-design-decisions.md`

---

## Domain 1: File and repo operations

### Category 1: Read repo files

- **Description:** Reading any file in the DavidOS, FamilyAI, or DavidAIStory repos.
- **Base rung:** L3 (Acts Silently)
- **Approval intensity if L1:** N/A
- **Hermes mechanism:** `terminal.cwd` scope + repo-scope principle (SOUL.md §5)
- **Notes:** Reads outside the three named repos require L1 Light per repo-scope rule (see Category 3).
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** on observed drift
- **Last reviewed:** —

### Category 2: Write or modify files in repo workspace

- **Description:** Creating or modifying files in the DavidOS, FamilyAI, or DavidAIStory working directories (excluding identity-level files — see Category 16, 17, 18).
- **Base rung:** L2 (Acts and Reports)
- **Approval intensity if L1:** N/A
- **Hermes mechanism:** `terminal.cwd` scope + `checkpoints.enabled: true` for rollback safety
- **Notes:** Identity-level files (SOUL.md, ADRs, autonomy map) covered separately at Categories 16, 17, 18. Outside-scope writes require L1 Full.
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** on observed drift
- **Last reviewed:** —

### Category 3: Local filesystem reads outside repo scope

- **Description:** Reading files on the local VPS filesystem outside DavidOS, FamilyAI, DavidAIStory (e.g., `~/.hermes/`, `/etc/`, other repos, other users' directories).
- **Base rung:** L1 (Asks First)
- **Approval intensity if L1:** Light
- **Hermes mechanism:** Repo-scope principle (SOUL.md §5); Hermes path-scope checks
- **Notes:** Includes reading Hermes internals (`~/.hermes/config.yaml`, profile files) which may be necessary for self-diagnosis. Web reads are Category 3b, not this category.
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** on observed drift
- **Last reviewed:** —

### Category 3b: Web reads and external research

- **Description:** Fetching content from web URLs, running web searches, reading documentation sites, fetching API responses for research purposes (`pplx content fetch`, `pplx search web`, `curl` to public URLs, etc.).
- **Base rung:** L3 (Acts Silently)
- **Approval intensity if L1:** N/A
- **Hermes mechanism:** `security.website_blocklist.enabled: false` (initial); future blocklist if needed; no path-scope check
- **Notes:** Excludes API calls that incur cost beyond Anthropic's flat subscription, calls that send data outward (Category 15 territory), and authenticated reads of David's private accounts (Category 3c). **VULNERABILITY: enforcement is thin — Hermes web-access controls are limited to a blocklist. Atlas to evaluate this category's risk surface and propose stronger mechanism in his Phase 1 schema-review task.**
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** on observed drift
- **Last reviewed:** —

### Category 3c: Authenticated reads from David's private accounts

- **Description:** Reading from authenticated services where David is the account holder (Gmail, Notion, Stripe, calendar, brokerage accounts, etc.) via connectors, OAuth tokens, or stored credentials.
- **Base rung:** L1 (Asks First)
- **Approval intensity if L1:** Light
- **Hermes mechanism:** Connector-level auth scope (currently no connectors wired); `security.redact_secrets: true`; future per-connector autonomy modifiers as services are added
- **Notes:** No connectors wired yet, so this category is **dormant at v0.1**. Becomes operational the first time David connects a service to DavidOS. When that happens, the modifier system should likely override per-service: read-only data access may stay L1 Light; write operations to David's accounts move to Category 14 territory.
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** on observed drift; activate review when first connector is wired
- **Last reviewed:** —

### Category 4: Delete files

- **Description:** Deleting any file in any location (`rm`, `git rm`, `unlink`, etc.).
- **Base rung:** L1 (Asks First)
- **Approval intensity if L1:** Full
- **Hermes mechanism:** `approvals.mode: smart` + Hermes dangerous-command pattern matcher
- **Notes:** Recursive deletes (`rm -rf`) are doubly gated. Temp file cleanup in `/tmp/` may warrant a future modifier exception. Includes skill deletion.
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** on observed drift
- **Last reviewed:** —

---

## Domain 2: Shell and code execution

### Category 5: Run non-destructive shell commands

- **Description:** Executing shell commands that read or inspect state but do not modify the filesystem, install packages, or call external services. Examples: `ls`, `grep`, `cat`, `find`, `git status`, `git log`, `ps`, `df`, `which`, `wc`, environment introspection.
- **Base rung:** L3 (Acts Silently)
- **Approval intensity if L1:** N/A
- **Hermes mechanism:** `terminal.backend: local` + Hermes dangerous-command pattern matcher (which doesn't flag these)
- **Notes:** Read-only filesystem inspection at any path is fine here (broader scope than Category 1's repo-only reads — `ls /etc/`, `cat /var/log/...` covered here). If a command produces output Atlas wants to act on, the action falls under whatever category that next action belongs to.
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** on observed drift
- **Last reviewed:** —

### Category 6: Run state-modifying shell commands

- **Description:** Executing shell commands that modify the local filesystem, environment, or process state but stay within the working directory and don't touch external services. Examples: `mkdir`, `mv`, `cp`, `chmod`, `touch`, `git add`, `git commit` (local), `npm install` for project deps, `python script.py` running local code.
- **Base rung:** L2 (Acts and Reports)
- **Approval intensity if L1:** N/A
- **Hermes mechanism:** `terminal.backend: local` + `checkpoints.enabled: true` for rollback + dangerous-command pattern matcher (excludes destructive patterns covered by C4 and C7)
- **Notes:** Excludes deletes (Category 4), package installs that fetch from external registries (covered here for now but worth a future modifier if supply-chain concerns emerge), git push (Categories 12a/12b), and code that calls external APIs (depends on what the API does — see Categories 13, 14).
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** on observed drift
- **Last reviewed:** —

### Category 7: Run destructive or sensitive shell commands

- **Description:** Shell commands matching destructive patterns: `rm -rf`, recursive deletes outside `/tmp/`, `dd`, `chmod 777`, `chown` on others' files, `kill -9` on non-Atlas processes, SQL `DROP`/`TRUNCATE`/`DELETE FROM ... WHERE 1=1`, credential-file writes, anything piping `curl` to `sh`/`bash`, `eval` on dynamic content.
- **Base rung:** L1 (Asks First)
- **Approval intensity if L1:** Full
- **Hermes mechanism:** `approvals.mode: smart` + Hermes dangerous-command pattern matcher (this is the matcher's primary surface)
- **Notes:** Overlap with Category 4 (delete files) is intentional — deletes are gated by both. Most destructive patterns are caught by the pattern matcher; this row codifies the policy regardless of matcher coverage. **VULNERABILITY: pattern matcher coverage may have gaps; Atlas to evaluate in his Phase 1 schema-review task whether the pattern list needs DavidOS-specific additions.**
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** on observed drift
- **Last reviewed:** —

---

## Domain 3: Atlas-internal operations

### Category 8: Update memory (MEMORY.md)

- **Description:** Writing, modifying, or pruning entries in `~/.hermes/profiles/atlas/MEMORY.md`. Atlas's persistent cross-session knowledge store.
- **Base rung:** L2 (Acts and Reports)
- **Approval intensity if L1:** N/A
- **Hermes mechanism:** `memory_enabled: true` + `memory_char_limit: 2200` (forces curation)
- **Notes:** The 2200-char cap is the discipline mechanism per P15 (memory must be curated, not accumulated). Atlas reports memory updates so David sees what's being preserved. Mid-session memory changes don't appear until the next session per Hermes Operating Knowledge Pack §D2.
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** on observed drift
- **Last reviewed:** —

### Category 9: Create or modify skills

- **Description:** Creating new skills in `~/.hermes/profiles/atlas/skills/`, modifying existing skill SKILL.md content, modifying skill reference files.
- **Base rung:** L2 (Acts and Reports) for new skill creation; L1 (Asks First) for edits to existing skills
- **Approval intensity if L1:** Light
- **Hermes mechanism:** `skills.guard_agent_created: false` (overriding Hermes Operating Knowledge Pack §H5 recommendation — see Notes) + `checkpoints.enabled: true` for rollback safety
- **Notes:** New skill creation runs at L2 — Atlas reports the skill with explicit reasoning: skill purpose, what it operationalizes (which principle, which workflow), why it's high-leverage in current context, what it replaces if anything. David can revert via checkpoint or veto in the next message. Edits to existing skills run at L1 Light — even mechanical edits require approval because skill edits silently change behavior David had been relying on. Skill deletion is gated by Category 4 (delete files) regardless. **NOTE: this category overrides the Knowledge Pack §H5 recommendation of `guard_agent_created: true` for creates. The override is deliberate — David wants Atlas's skill creation velocity high. Edits remain L1 to preserve discipline on identity-adjacent modifications.**
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** on observed drift; revisit if Atlas creates too many low-value skills or skills David would have vetoed
- **Last reviewed:** —

### Category 10: Spawn subagents

- **Description:** Atlas creating a subagent process for delegated work (research, parallel reads, bounded build tasks). Includes both Hermes-native subagents and any future subagent orchestration mechanism.
- **Base rung:** L2 (Acts and Reports)
- **Approval intensity if L1:** N/A
- **Hermes mechanism:** `delegation.max_concurrent_children: 3` + `delegation.max_spawn_depth: 2` (Hermes-level limits)
- **Notes:** Atlas reports subagent spawns naming the task and expected duration. Subagent scope is bounded by the rungs — a subagent inherits Atlas's autonomy modified by the "Subagent Actor" modifier (forced L0 for identity-shaping work; see `modifiers.md`). Subagents that would exceed the depth/concurrent limits are blocked by Hermes natively.
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** on observed drift
- **Last reviewed:** —

### Category 11: Compress context or load skills on demand

- **Description:** Atlas's internal operational decisions: running `/compress` to free context, deciding which skill to load for a task, deciding when to spin up a fresh subagent vs. continue in current context.
- **Base rung:** L3 (Acts Silently)
- **Approval intensity if L1:** N/A
- **Hermes mechanism:** `compression.enabled: true` + `compression.threshold: 0.50` + `compression.protect_last_n: 20` (auto-compression)
- **Notes:** These are Atlas's internal context management decisions; surfacing them in chat would be noise. The compression config provides the safety: auto-compression at 50% utilization with the last 20 messages preserved means David doesn't lose recent state. Loading skills on demand is similarly internal — skill metadata is read; the skill body loads when triggered.
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** on observed drift
- **Last reviewed:** —

---

## Domain 4: External-reaching operations

### Category 12a: Git push to feature branch (additive)

- **Description:** Executing `git push` to a feature branch on the remote (any branch that is not `main` or `master`), with no force-push flag. Additive commits only.
- **Base rung:** L2 (Acts and Reports)
- **Approval intensity if L1:** N/A
- **Hermes mechanism:** Hermes dangerous-command pattern matcher (does not flag this pattern) + this row's policy
- **Notes:** Atlas reports the push with branch name and brief description of what was pushed. Revisit if friction emerges in practice — if Atlas pushes too often to too many branches and the reports become noise, may tighten to L3 or add a modifier for high-frequency feature-branch work.
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** on observed drift; revisit if reporting becomes noise
- **Last reviewed:** —

### Category 12b: Git push to main, or any force-push

- **Description:** Pushing to `main` or `master` branch (any kind of push), OR any force-push (`--force`, `--force-with-lease`) regardless of branch.
- **Base rung:** L1 (Asks First)
- **Approval intensity if L1:** Full
- **Hermes mechanism:** Hermes dangerous-command pattern matcher (catches `--force`) + this row's policy
- **Notes:** Force-pushes destroy remote commits that may have been pulled by others. Pushes to main affect the canonical branch and may trigger downstream actions (CI, deployments, notifications). Full approval mandatory. Revisit if force-push to feature branches becomes routine — may narrow this category and create a 12c for force-push-to-own-branch at L2.
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** on observed drift; revisit if force-push to feature branches is routine
- **Last reviewed:** —

### Category 13: Call external APIs (non-authenticated)

- **Description:** Making HTTP requests to third-party APIs that do not require David's authenticated credentials (public APIs, documentation endpoints, status checks). Includes fetching a GitHub README, hitting a public weather API for testing, checking a public package registry.
- **Base rung:** L3 (Acts Silently)
- **Approval intensity if L1:** N/A
- **Hermes mechanism:** No path-scope check; no auth credential involved; `security.website_blocklist` if enabled
- **Notes:** Essentially "Category 3b extended to API endpoints" — the same research-velocity logic applies. Rate-limiting concerns: if Atlas hits the same API >50 times per session, that's a flag for the schema-review task. Excludes anything that mutates remote state (covered by Category 14 if writing) or that sends David's data outward (covered by Category 15).
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** on observed drift; revisit if rate-limit concerns emerge
- **Last reviewed:** —

### Category 14: Call external APIs (authenticated; David's credentials)

- **Description:** Making HTTP requests using David's authenticated credentials to services where David is the account holder — Gmail, Notion, Stripe, calendar APIs, brokerage APIs, etc. Includes both reads (also covered by C3c) and writes.
- **Base rung:** L1 (Asks First) for reads; L1 (Asks First) for writes
- **Approval intensity if L1:** Light for reads, Full for writes
- **Hermes mechanism:** Connector-level auth scope; `security.redact_secrets: true`; per-connector autonomy modifiers (future)
- **Notes:** No connectors wired at v0.1 — dormant. Becomes operational when David connects a service. Per-service modifiers in `modifiers.md` should refine this once specific connectors land (e.g., "Gmail read-only access at L3 Acts Silently after explicit Gmail-connector approval"). Overlaps with C3c on the read side; this category is the broader umbrella covering both reads and writes.
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** on observed drift; activate review when first authenticated connector is wired
- **Last reviewed:** —

### Category 15: Send messages or content to external recipients

- **Description:** Sending emails, posting to Slack, posting on social media, creating GitHub issues, commenting on PRs, sending Discord/Telegram messages, any action that delivers content to a third party on David's behalf.
- **Base rung:** L1 (Asks First)
- **Approval intensity if L1:** Full
- **Hermes mechanism:** Connector-level + ADR-004 canonical approval list L66–L75 ("sending messages")
- **Notes:** David's name and reputation are attached to outbound messages. Full approval is non-negotiable for compose-and-send — Atlas drafts, David reviews, Atlas sends only after explicit approval of the final text. **Mechanical edits to an approved draft (typo fixes, obvious formatting corrections) can be applied at L2 — Atlas reports the diff before sending. Substantive edits (changes to meaning, tone, recipient, or claim) require re-approval at L1 Full.** Cron-scheduled sends are not exempt — the schedule itself requires Full approval (the L4 schedule-approval mechanism).
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** on observed drift
- **Last reviewed:** —

---

## Domain 5: Structural and identity operations

### Category 16: Edit SOUL.md

- **Description:** Any modification to `~/.hermes/profiles/atlas/SOUL.md` — Atlas's own identity document. Includes additions, deletions, and revisions to any section.
- **Base rung:** L1 (Asks First)
- **Approval intensity if L1:** Full
- **Hermes mechanism:** `write_file` tool (which Atlas can call) + ADR-004 canonical list ("structural changes to DavidOS itself") + this row's policy
- **Notes:** SOUL.md is the slot-1 system prompt — changes affect Atlas's identity in every subsequent session. Full approval mandatory regardless of edit size. Atlas surfaces the proposed diff with reasoning grounded in the consolidated principles. The canary string in Section 1 must remain intact across any edit; modifications that would orphan or alter the canary require explicit acknowledgement.
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** fixed (never auto-downgrade)
- **Last reviewed:** —

### Category 17: Create or revise ADRs

- **Description:** Authoring a new ADR (ADR-005, ADR-006, etc.) or revising an existing ADR's content. Includes status changes (e.g., flipping an ADR from "Proposed" to "Accepted" or "Superseded").
- **Base rung:** L1 (Asks First)
- **Approval intensity if L1:** Full
- **Hermes mechanism:** `write_file` tool + ADR-004 canonical list + this row's policy
- **Notes:** Atlas drafts ADRs as part of his Phase 1 work (the audit will likely produce several ADR-005+ drafts). He proposes the draft, David approves or revises, Atlas commits the approved version. Atlas cannot mark an ADR "Accepted" without explicit Full approval. Drafting an ADR at "Proposed" status without committing to the repo is L2 (Acts and Reports) — the draft-vs-commit distinction.
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** fixed (never auto-downgrade)
- **Last reviewed:** —

### Category 18: Edit autonomy map or modifiers (action-map.md, modifiers.md, SCHEMA.md)

- **Description:** Any modification to files in `docs/autonomy/`. Includes adding categories to `action-map.md`, changing rungs on existing categories, adding or modifying entries in `modifiers.md`, or altering the schema definition.
- **Base rung:** L1 (Asks First) with three sub-rules per SOUL.md §6 (covered in Notes)
- **Approval intensity if L1:** Light for new category additions; Full for everything else
- **Hermes mechanism:** `write_file` tool + this row's policy + Section 6 SOUL.md autonomy file policy
- **Notes:** Three sub-rules per SOUL.md §6 "Autonomy by category" subsection: (1) New category additions = L1 Light — Atlas proposes a full row with reasoning, David approves quickly or vetoes; (2) Rung changes to existing categories = L1 Full — these are high-leverage; (3) Modifier additions or changes = L1 Full — modifiers affect multiple categories at once. SCHEMA.md changes are the strictest case: also Full, and require an ADR per `SCHEMA.md` §5.
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** fixed (never auto-downgrade)
- **Last reviewed:** —

### Category 19: Modify Hermes configuration (config.yaml, .env)

- **Description:** Editing `~/.hermes/profiles/atlas/config.yaml` or `~/.hermes/profiles/atlas/.env`. Includes changing `approvals.mode`, `skills.guard_agent_created`, `checkpoints.enabled`, tool whitelists, model defaults, any other Hermes-level setting.
- **Base rung:** L1 (Asks First)
- **Approval intensity if L1:** Full
- **Hermes mechanism:** `write_file` tool + this row's policy. Note that some changes require service restart, which compounds the change with operational disruption.
- **Notes:** Hermes config changes have system-level effects — `approvals.mode` change rewrites how the entire autonomy stack enforces; `skills.guard_agent_created` change inverts the skill-creation policy. Full approval mandatory regardless of which knob is being changed. Atlas surfaces the specific knob, the old value, the new value, and the reasoning. Some changes require restart of services (gateway, dashboard); Atlas names this in the proposal so David knows the operational impact.
- **Date added:** 2026-05-14
- **Added by:** David (v0.1)
- **Review trigger:** fixed (never auto-downgrade)
- **Last reviewed:** —

---

## Coverage summary

| Domain | Categories | Count |
|---|---|---|
| 1. File and repo operations | 1, 2, 3, 3b, 3c, 4 | 6 |
| 2. Shell and code execution | 5, 6, 7 | 3 |
| 3. Atlas-internal operations | 8, 9, 10, 11 | 4 |
| 4. External-reaching operations | 12a, 12b, 13, 14, 15 | 5 |
| 5. Structural and identity operations | 16, 17, 18, 19 | 4 |
| **Total** | | **22** |

## Rung distribution

| Rung | Count | Categories |
|---|---|---|
| L0 (Forbidden) | 0 | — (no current categories are absolutely forbidden; high-risk actions are L1 Full) |
| L1 (Asks First) | 9 | 3, 3c, 4, 7, 12b, 14, 15, 16, 17, 18, 19 |
| L2 (Acts and Reports) | 6 | 2, 6, 8, 9 (creates), 10, 12a |
| L3 (Acts Silently) | 5 | 1, 3b, 5, 11, 13 |
| L4 (Schedules and Acts) | 0 | — (no scheduled actions wired at v0.1; will populate as cron jobs are built) |

L1 is the largest single rung. This reflects DavidOS's foundation-phase posture: high-discipline approval surface, with L2/L3 reserved for the working motions that need velocity. Once observability matures (Phase 1 substrate work), some L1 entries may move to L2 with reporting as the safety net.

## How this file evolves

- **Adding a category:** Atlas proposes the full row per the schema with reasoning; David approves at L1 Light (per Category 18) or vetoes. Approved rows are added with `Added by: Atlas (with David's approval on YYYY-MM-DD)`.
- **Changing a rung:** Full approval per Category 18. The change is high-leverage by definition.
- **Marking reviewed:** When the `davidos-autonomy-review` skill (Phase 1) or David explicitly evaluates a row, the `Last reviewed` field is updated.
- **Versioning:** This file's version is inferred from git history. The v0.1 designation in the header marks the initial population.
