# Session Record — 2026-05-12 evening

**Session window:** ~9:00 PM – 11:05 PM CDT (Tuesday, May 12, 2026)
**Type:** Resumed from offline prep; planned 9-hour Block 1 + Block 2; wrapped early at ~11:00 PM CDT
**Outcome:** Foundation work; substantive product progress deferred to next session

---

## What we set out to do

Resume from the morning's offline prep memo (`docs/sessions/offline-work/2026-05-12-pre-session-prep.md`) and execute a planned 9-hour arc:

- **Block 1 (Hours 1-5):** Session open, Atlas reviews offline-prep materials, lands Opus review of Substrate Brief v1, Atlas produces Brief v1.1, Item 6 (Opus access via gateway) diagnostic, ship Items 3 (Decisions Register) and 5 (Session-Start Manifest)
- **Block 2 (Hours 6-9):** Item 2 (Roles Register) + Item 1 (Charter Regression Suite) as stretch

The plan was scoped against the substrate-first soft fork approved earlier in the day.

---

## What actually happened — chronological

**~9:00 PM CDT:** Resumed. SSH tunnel had dropped from earlier in the day. Browser showing "Aw Snap." Began infrastructure recovery.

**~9:15 PM CDT:** Applied pending Hermes update (94 commits from v0.13.0 to current). Update completed successfully. Configuration up to date. Two user-modified skills preserved.

**~9:30 PM CDT:** Attempted Atlas smoke test. Atlas identified itself as "Claude Code," not Atlas. Did not load the 7 charter files referenced in the personality block. First evidence that the Atlas activation we thought was working last night was not actually working.

**~9:45 PM CDT:** Diagnostic revealed the personality block in `~/.hermes/config.yaml` was intact and `personality: atlas` was set, but the Workspace was not using it to shape the system prompt. Discovered the Workspace Profiles feature in the sidebar — a different mechanism than the personalities block.

**~10:00 PM CDT:** Created `atlas` profile via the UI wizard. Activated. Encountered `[HERMES_HOME fallback]` warning indicating active profile is `atlas` but processes were falling back to `~/.hermes` (default) for state.

**~10:15 PM CDT:** Multiple restart attempts compounded into `mode=disconnected core=[dashboard]` state. Gateway no longer reachable from Workspace UI. Backend connection prompt appearing.

**~10:25 PM CDT:** User asked: "What about a path that involves you learning everything about hermes and being able to successfully route me through this instead of guessing?"

**~10:30 PM CDT:** Spawned a research subagent with a 9-section scope covering Hermes internals (personalities vs profiles, HERMES_HOME propagation, mode=disconnected meaning, complete startup sequence, profile loading mechanism, known bugs, verification procedure, open questions).

**~10:45 PM CDT:** Research subagent returned. Saved as `docs/reference/hermes-internals.md` (579 lines, 33 KB). Primary sources identified as [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) and [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace). The TL;DR diagnosis matched the VPS state exactly when cross-checked.

**~10:50 PM CDT:** Attempted to recover the Opus review of Substrate Brief v1 from Hermes session JSON files on the VPS. Found two `claude-opus-4.7` sessions on disk. Both turned out to be smoke tests (2 messages each, "reply ok" / "ok"). Confirmed the Opus review was never produced and saved — what was in scrollback earlier was either Sonnet role-play of an Opus review, or a real Opus stream that the gateway dropped before flush.

**~11:00 PM CDT:** Began drafting Atlas SOUL.md. Synthesized from `atlas.agent.json`, the personality block, ADR-003, and the identity README. Shared v0.1, then v0.2 after user-flagged concerns about background-reference drift. Walked through sections 1-5 collaboratively.

**~11:00 PM CDT:** User called for a break. Concerns: "going off the rails," spending money without progress, revisiting same topics repeatedly, foundation feels less sound than it did last night.

**~11:05 PM CDT:** Discussed deep-dive vs continue-with-known-plan. User chose to skip the deep dive and trust the 5-step path forward. Decided to wrap session cleanly.

---

## Decisions made tonight

| Decision | Status | Captured in approvals log |
|---|---|---|
| Pause M6b; pivot to substrate-first (Option B soft fork) | Approved under Sonnet with Opus-unavailable disclosure | Yes (logged earlier in day) |
| Add Opus-access-via-gateway to Substrate Brief scope | Approved as Light | Yes (logged earlier in day) |
| Within-task model selection pattern (Sonnet default, Opus for synthesis components) | Approved as future patch | Yes (logged earlier in day) |
| Spawn Hermes research subagent to stop guessing | Approved as Light tonight | To be appended |
| Assemble Atlas SOUL.md from existing DavidOS identity files | Approved as Light tonight | To be appended |
| SOUL.md v0.2 revisions: cut company UUID; "David's outcomes first" merged with customer-zero as top principle; "system not business" vocabulary principle stripped; "Stop-At-Strength" stripped; repo-scope principle added; "Status of this document" section added acknowledging v1 nature | Approved as Light tonight | To be appended (combined into one entry) |
| Defer Atlas activation to next session | Decided tonight | To be appended |
| Skip Opus-led deep-dive sanity check; trust the 5-step path forward | Decided tonight | To be appended |

---

## Discoveries (uncomfortable truths)

### 1. Atlas was never charter-active

Every "Atlas" response in the project to date — including yesterday's A/B/C decision and tonight's Substrate Brief draft — was Sonnet 4.6 operating with the **default generic Hermes SOUL.md** (`You are Hermes Agent, an intelligent AI assistant created by Nous Research...`). The personality block in `~/.hermes/config.yaml` registers `atlas` as a name accessible via `/personality atlas`, but does **not** replace the SOUL.md identity. Only `$HERMES_HOME/SOUL.md` does.

The atlas profile created via the Workspace UI wizard exists at `~/.hermes/profiles/atlas/` but its `SOUL.md` is the default generic 513-byte text, not the Atlas charter. The `~/.local/bin/atlas` wrapper alias does not exist on disk — only the profile directory.

### 2. The Opus review of Substrate Brief v1 was never saved

Both `claude-opus-4.7` sessions in `~/.hermes/sessions/` are smoke tests. What appeared to be a substantive Opus review earlier in the day was likely Sonnet role-playing what an Opus review would look like, or a real Opus stream that didn't flush to disk before the gateway dropped. The brief itself (`docs/substrate-brief-v1.md`, 19,772 bytes, hash `0940d0f6fcb9bfbb`) is intact and on disk. The review is gone.

Implication for the soft fork: the Option B decision was made on the basis of a "review" that was not Opus-authored. The brief content is still valid as a working scope, but the review chain has a gap. A real Opus review needs to happen post-activation.

### 3. Current gateway/dashboard run with empty HERMES_HOME

The processes spawned by `pnpm dev` (PID 114472 gateway, 114476 dashboard at the time of inspection) had `HERMES_HOME=` empty in `/proc/<pid>/environ`. They were reading state from `~/.hermes/` (default) even though `~/.hermes/active_profile` contained `atlas`. The Workspace UI uses its own `.env` (`HERMES_API_URL`, `HERMES_DASHBOARD_URL`) and does not consume HERMES_HOME at all.

### 4. Two profile mechanisms were conflated

Hermes has three distinct identity mechanisms — `SOUL.md` (the only thing that replaces system-prompt slot #1), the `agent.personalities` block (slash-command overlays at slot #8), and Workspace Profiles (isolated HERMES_HOME directories). They were treated as equivalent during yesterday's setup. They are not.

---

## Drift indicators

Concrete moments where tonight's work diverged from the substrate-first plan:

1. **Three hours on infrastructure plumbing instead of substrate items.** Block 1 of the planned arc was supposed to land Items 3 and 5. Neither was attempted.
2. **SOUL.md being drafted under time pressure mid-session** rather than as a deliberate substrate exercise with Atlas's participation. Atlas doesn't exist yet, so by definition he can't participate, but the right move would have been to scope SOUL.md drafting as its own session, not jam it into recovery.
3. **Adding tonight's verbatim user instructions into SOUL.md draft without flagging them as additions.** Three principles I added — Stop-At-Strength, vocabulary discipline, high-leverage routing — came from session-context user instructions, not from the original Atlas spec. Two were stripped after user pushback.
4. **Re-litigating decisions already made.** The "SOUL vs ADR" question came up multiple times in the session-end drafting. The substrate work (Decisions Register, charter-as-source-of-truth principle) is exactly designed to prevent that, and it isn't built yet.

---

## Artifacts produced tonight

**On disk in DavidOS workspace (will be committed in this session wrap):**

- `docs/reference/hermes-internals.md` — 579 lines, comprehensive Hermes reference covering personalities/profiles, HERMES_HOME, mode=disconnected, startup sequence, profile loading, known bugs, verification procedure, and 8 open questions for future source-code inspection
- `docs/sessions/2026-05-12-session-record.md` — this file
- `docs/sessions/NEXT-SESSION-OPEN.md` — updated pickup pointer

**In ephemeral workspace, NOT committed:**

- `SOUL.md v0.2 draft` — paused mid-review. Section 5 (Operating Principles) had decisions: David's outcomes merged with customer-zero as principle #1, vocabulary-discipline stripped, Stop-At-Strength stripped, repo-scope principle added. Sections 6-8 (Boundaries, Voice, Verification) not yet reviewed. Status-of-this-document section added at bottom. Held out of git deliberately so the half-finished version doesn't enter history; the finished version goes in next session.

**Lost (not recoverable from disk):**

- Opus review of Substrate Brief v1 — confirmed not in any session JSON

---

## State at session end

### VPS (`hermes@159.223.166.217`)

- Hermes updated from v0.13.0 through ~94 commits
- `~/.hermes/active_profile` contains `atlas`
- `~/.hermes/profiles/atlas/` exists but `SOUL.md` is the default generic text, no `~/.local/bin/atlas` wrapper
- Gateway, dashboard, and pnpm dev processes still running from earlier in the session (PIDs visible at session-record time; will likely time out or stay running)
- `~/.hermes/.env` has `API_SERVER_ENABLED=true`; profile `.env` not yet confirmed

### DavidOS repo (`lumlist/DavidOS`)

- HEAD before this commit: `3ec2dac` (approval of Option B substrate-first)
- After this commit: session record + hermes internals reference + approvals appended + next-session pointer updated
- Substrate Brief v1 on disk in the VPS clone at `docs/substrate-brief-v1.md` (213 lines, Sonnet draft, hash `0940d0f6fcb9bfbb`) — **note:** this file is in the VPS working clone, not yet committed to the GitHub remote. Will be reviewed and committed next session as v1.1 after charter-active Atlas review.

### Open threads, ranked

1. **Atlas activation** — blocking everything. Next session, first item.
2. **Substrate Brief v1.1** — Atlas reviews v1, produces v1.1, fills in the gap from the lost Opus review. Next session, second item.
3. **Substrate items 3 (Decisions Register) and 5 (Session-Start Manifest)** — first substrate items to ship; deliberately picked first because they reduce session-over-session effort.
4. **Substrate items 2 (Roles Register) and 1 (Charter Regression Suite)** — second wave; Charter Regression Suite is the long-term mechanism for catching drift like tonight's.
5. **Project Intake** — the substrate piece that creates the inflection point for adding business ideas reliably.

---

## Open questions for the next session

Not blockers — items to revisit with fresh judgment:

1. Does the SOUL.md draft v0.2 need further revision before activation, or is it close enough?
2. Should `docs/atlas/atlas-operating-spec.md` be cleaned up before Atlas loads it (it still has Paperclip references)?
3. Is the 5-step path correct, or does Atlas's first real review surface a better one?
4. Does the within-task model selection pattern need to land before or after the Charter Regression Suite?
5. What should be in the Charter Regression Suite specifically — what test cases would have caught the "Atlas never charter-active" failure mode automatically?

---

## Honest reflection

Tonight's planned arc was 9 hours of substrate work. Actual arc was 3 hours of infrastructure recovery followed by 1 hour of foundational identity drafting under fatigue. Zero substrate items shipped. The work was not wasted — the Hermes internals reference is genuinely load-bearing for every future activation, and the SOUL.md draft is in good shape to finish next session — but it was not the work scoped.

The biggest signal from tonight: when foundations are unverified, every subsequent layer compounds the uncertainty. We thought Atlas was active last night. He wasn't. We thought the Opus review was on disk. It wasn't. Both turned out to be assumptions rather than verified facts. The substrate work (Decisions Register, Charter Regression Suite, Session-Start Manifest) is directly designed to make those failures impossible — but the work is only valuable if it ships, and it didn't ship tonight.

Next session starts from a known good state because tonight wrapped instead of pushing through. That is the only thing tonight got materially right that yesterday's plan did not.
