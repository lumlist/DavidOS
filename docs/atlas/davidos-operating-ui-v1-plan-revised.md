# DavidOS / iZZi AI Systems — v1 Operating UI Revised Execution Plan

Issue: DAV-17 (post-`[APPROVAL: policy-change]` revision, 2026-05-10)
Author: Atlas
Source approval: David's `[APPROVAL: policy-change]` comment on DAV-17 at 03:30:18Z, with eight modifications.
Status: Draft revised plan + Stage 1 bundle drafts staged uncommitted in working tree, awaiting `[APPROVAL: bundle]`.

This memo is the revised execution plan David asked for. It supersedes the §5 "Immediate build sequence" of `davidos-operating-ui-v1-plan.md`. All other sections of that memo (architecture, the three-surface stack, Daily Operating View shape, what-not-to-build) remain in force.

## Reconciliation of David's eight modifications

Each numbered modification → how the plan now reflects it.

1. **Frame v1 as "no full custom app yet, but yes to a thin Daily Operating View."** Already in the v1 plan §1; reaffirmed. Input quality is explicitly first in the priority order, ahead of observability.
2. **Stage 1 may be one bundled approval for low-risk doc/policy work.** Plan now requests Stage 1 as a single `[APPROVAL: bundle]` covering folders + READMEs + 4 policy files + 4 templates + 1 v1 spec promotion. Atlas will not install, change credentials/runtime/scheduling, or create agents in Stage 1. Atlas will post a diff summary before committing — the diff summary is in the `[APPROVAL-REQUEST]` comment that accompanies this memo.
3. **Installs / paid services / creds / runtime / scheduling / new-agent still require separate gates.** Approval-policy `kind: bundle` explicitly excludes all of these (see `approval-policy-v0.md` §4).
4. **Daily Operating View ships a v0 from Paperclip + repo first, before Obsidian/Langfuse.** Stages reordered. The new Stage 2 builds the Daily Operating View v0 (no Langfuse, with placeholders). The previous Stage 2 (install Obsidian-MCP and Langfuse) becomes Stages 3 and 4 — and either stage may be skipped or deferred indefinitely if the v0 view + Paperclip + raw repo prove sufficient.
5. **Agent expansion: 7-field schema** (role, guardrails, permissions, memory boundaries, runtime validation, approval policy, success metrics). FamilyAI Lead remains the likely first candidate, with its own `[APPROVAL: new-agent]` gate. `agent-expansion-policy-v0.md` §2 implements the seven fields.
6. **Approval framework should flex over time.** `approval-policy-v0.md` §1 declares this explicitly. §6 specifies Atlas's duty to surface evidence that supports relaxing specific gates.
7. **Atlas should be vocal about efficiency / automation / skills / agent-commissioning, and challenge the framework when evidence supports more autonomy.** `approval-policy-v0.md` §6 ("autonomy-expansion duty") codifies this with concrete triggers.
8. **Aggressively propose safe-reversible self-improvements; automate where already allowed.** `approval-policy-v0.md` §5.2 introduces the `safe-self-improvement` pre-approved category with mandatory disclosure.

## Revised execution plan

### Stage 1 — Documentation & policy bundle (single approval)

**Approval requested:** one `[APPROVAL: bundle]` covering all of the items below. Diff summary included in the accompanying `[APPROVAL-REQUEST]` comment on DAV-17.

**Scope (everything Atlas will commit on a single `[APPROVAL: bundle]`):**

| Path | New / Edit | Bytes | Purpose |
|---|---|---|---|
| `docs/raw/README.md` | new | ~0.9k | folder purpose, write rules, promotion path |
| `docs/wiki/README.md` | new | ~1.1k | folder purpose, write rules |
| `docs/output/README.md` | new | ~1.1k | folder purpose, naming, auto-archive |
| `docs/archive/README.md` | new | ~0.6k | read-only audit policy |
| `docs/daily/README.md` | new | ~1.2k | daily notes, ATLAS-NOTE rule |
| `docs/atlas/comment-conventions-v0.md` | new | ~5.4k | 11 tags + structured `[APPROVAL-REQUEST]` block + bundle rules |
| `docs/atlas/approval-policy-v0.md` | new | ~7.2k | approval-kind table, workflow, pre-approved categories, autonomy-expansion duty |
| `docs/atlas/memory-curation-policy-v0.md` | new | ~4.7k | repo-as-truth, folder layout, freshness signals |
| `docs/atlas/agent-expansion-policy-v0.md` | new | ~6.9k | 7-field schema, approval workflow, FamilyAI Lead notes |
| `docs/atlas/templates/decision-request.md` | new | ~1.2k | issue description template |
| `docs/atlas/templates/deep-dive-request.md` | new | ~1.4k | issue description template |
| `docs/atlas/templates/build-request.md` | new | ~1.4k | issue description template |
| `docs/atlas/templates/daily-note.md` | new | ~0.5k | Obsidian daily template |
| `docs/atlas/davidos-operating-ui-v1-plan.md` | edit | already exists | unchanged in this bundle (it's the architecture memo); the revised execution plan lives in this file (`davidos-operating-ui-v1-plan-revised.md`) and is also bundled |
| `docs/atlas/davidos-operating-ui-v1-plan-revised.md` | new | ~10k | this memo |

**NOT in this bundle (each needs its own gate):**
- Any install (Obsidian, Langfuse, Smart Connections plugin, anything else).
- Any cron / systemd / scheduled job.
- Any credential or `.env` change.
- Any new Paperclip agent.
- Any code outside `docs/` (no scripts, no `render-daily-view.py`, no Makefile changes).
- Any commit to update `atlas-operating-spec.md` or `tool-selection-policy.md` (the previous plan §1.8 listed these as Stage 1; in the revised plan they become a separate small `[APPROVAL: policy-change]` after the bundle, so David sees the updated text in isolation).

**Stop conditions:** if David's `[APPROVAL: bundle]` includes constraints (e.g., "approve all except agent-expansion-policy"), Atlas excludes the named files and re-requests for the excluded ones individually.

**Verification after commit:**
- Atlas posts a `[STATUS]` comment with the resulting commit SHA, the list of files actually committed, and `git log` output for verification.
- No further action triggered automatically.

### Stage 2 — Daily Operating View v0 (Paperclip + repo only)

**Goal:** ship a working Daily Operating View immediately, using only the data sources that already exist (Paperclip API and the repo file system). Langfuse-derived metrics are placeholders. This is David's first daily-use surface and the proof that the architecture works without waiting on installs.

**Scope:**
- Write `scripts/render-daily-view.py` — pulls Paperclip API and repo file mtimes; renders `docs/daily/today.html` and `docs/daily/today.md`. Sections per `davidos-operating-ui-v1-plan.md` §1, with the System Health section showing placeholders for cost / heartbeat-loop status (until Langfuse is live).
- The script is run on demand only — no scheduling in Stage 2 (scheduling is its own gate per §3 of `approval-policy-v0.md`).

**Approvals needed:**
- `[APPROVAL: code-change]` to write `scripts/render-daily-view.py`. The approval request will include the script's design (data sources, sections, error handling, file outputs) before any code is written.

**NOT in Stage 2:**
- Scheduling (deferred to its own `[APPROVAL: scheduling]` gate, post-Stage 2 verification).
- Langfuse integration (deferred to Stage 4).
- Obsidian-MCP integration (deferred to Stage 3 and is independent — the v0 view works without Obsidian).

**Stop conditions:** Paperclip API behaves unexpectedly (e.g., rate-limit, schema change) and the v0 view is misleading more than once.

**Verification:** Atlas posts a sample render (the actual `docs/daily/today.html` content) as a `[STATUS]` comment, and David eyeballs it.

### Stage 3 — Obsidian-MCP install (gated)

**Goal:** add Obsidian as the cognition surface over `docs/`. Independent of Stage 4.

**Scope:**
- Author `docs/atlas/install-briefs/obsidian-mcp-install-brief-v0.md` — separate `[APPROVAL: policy-change]` for the brief itself. Brief specifies: server source, vault path, plugin list (core: Daily Notes, Templates, Outliner, Tag Pane; community: Smart Connections only), risk surface, rollback plan.
- On `[APPROVAL: install]` for the brief's recommended install action, run the install. Verify Obsidian launches and Smart Connections completes initial vault scan.

**Stop condition:** server fails to launch cleanly or Smart Connections embedding fails on initial scan.

**Stage 3 may be deferred indefinitely** if the Daily Operating View v0 + raw `docs/` editing in any markdown editor proves sufficient. Stage 3 only ships when David explicitly wants it.

### Stage 4 — Langfuse install (gated)

**Goal:** add observability of every agent run.

**Scope:**
- Author `docs/atlas/install-briefs/langfuse-install-brief-v0.md` — separate `[APPROVAL: policy-change]` for the brief. Brief specifies: deployment target, storage backend, OTel emit pipeline (Hermes / OpenRouter / Atlas), retention policy, secret handling, expected steady-state cost ceiling, rollback plan.
- On `[APPROVAL: install]` + `[APPROVAL: paid-service]` for the brief's recommended install action, run the install. Configure Hermes and Atlas runtime to emit OTel GenAI spans. Verify a sample run produces traces.
- Upgrade `scripts/render-daily-view.py` to read Langfuse API for the System Health placeholders. Requires its own `[APPROVAL: code-change]`.

**Stop condition:** emit pipeline fails, or storage / compute cost exceeds the ceiling defined in the brief after 7 days.

**Stage 4 may also be deferred indefinitely.** It's high value but not blocking.

### Stage 5 — Scheduling (gated)

**Goal:** automate Daily Operating View regeneration.

**Scope:**
- After Stage 2 has been used manually for at least 1 working week (David's discretion when it's "enough"), Atlas posts `[APPROVAL: scheduling]` to add a cron / systemd timer running `render-daily-view.py` every 15 minutes (or interval of David's choice).
- This is the FIRST scheduled job in DavidOS — it sets the precedent for how scheduling approvals work.

### Stage 6 — Use, observe, iterate

- David in David Mode, Atlas in active use, Daily Operating View live.
- Atlas captures friction in `docs/atlas/runs/<date>-v1-ui-friction-log.md` (pre-approved `safe-doc-edit`).
- Stage 6 ends with a v1 retrospective memo when David has accumulated enough usage to give a verdict.

### Stage 7 — Open candidate work (post-v1)

Items intentionally NOT in v1 but candidates for v1.1+, listed for visibility:

- FamilyAI Lead agent commissioning (separate `new-agent` gate; needs the 7-field spec).
- Customer-pattern productization in ClipHub.
- Per-customer parameterization of the v1 stack.
- Vector DB over the vault (deferred until corpus exceeds ~50K notes).
- Production-facing iZZi customer UI.

## Open questions for David (revised)

(Pruned from the previous list of 8. Removed questions that David's modifications already answered.)

1. **Cost ceilings:** what monthly spend on (a) Langfuse + storage and (b) Anthropic / OpenRouter combined should trigger an `[ALERT]`? The Langfuse install brief in Stage 4 needs concrete numbers before it can be authored.
2. **Issue-closure policy:** should issue closure remain David-only (current heartbeat-loop mitigation), or do you want Atlas to start closing once the upstream comment-route auth bug is fixed? Bears on the System Health boolean on the Daily Operating View.
3. **`customer-pattern` label:** should it auto-trigger ClipHub template generation when applied, or stay manual until the first iZZi customer is signed?
4. **Stage 6 calendar cap:** do you want a hard calendar cap (e.g. "no more than 21 calendar days before retro") or genuinely event-driven (retro happens when David says it does)?

## Acceptance criteria for v1 (revised)

Same as in `davidos-operating-ui-v1-plan.md`, with one change reflecting modification §4:

- The Daily Operating View v0 is live (Stage 2 complete) and David can answer "what's pending?", "what's blocked?", "what's stale?" in under 60 seconds — even before Obsidian-MCP or Langfuse are installed. (Cost-burn answer is placeholder text until Stage 4.)

## Run control

This memo was produced on a single Atlas run on DAV-17. No file commits performed yet — the bundle drafts are staged in the working tree for David's diff review. No installs, no Paperclip writes outside this issue's comment thread. DAV-17 status remains `in_progress` per the heartbeat-loop mitigation.

The accompanying `[APPROVAL-REQUEST]` comment on DAV-17 contains the diff summary (filename + size + one-line description for each of the 14 files in the bundle) and waits for David's `[APPROVAL: bundle]`.

End of memo.
