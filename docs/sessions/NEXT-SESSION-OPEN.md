# Next Session — Open

**Last updated:** 2026-05-13 03:39 AM CDT (post-wrap charter capture)
**Last session:** [2026-05-12 evening](./2026-05-12-session-record.md) — infrastructure recovery + Hermes internals research + Atlas SOUL.md drafting (paused mid-review). No substrate items shipped. Atlas activation deferred to this session.

---

## ⚠ Before Step 1: Review the new charter primary source

At the very end of last night's session, David captured a verbatim 11-point outcome list, 3 frustrations, and 3 clarifying responses. This is the **first primary-source charter document** for DavidOS and likely changes the shape of the SOUL.md, the Substrate Brief, and the 5-step path.

**Read first:** [`docs/charter/outcomes-and-frustrations-2026-05-13.md`](../charter/outcomes-and-frustrations-2026-05-13.md)

**Decide before continuing to Step 1:**
1. Which of the 11 outcomes belong in SOUL.md (as identity/principles) versus in the Charter Regression Suite (as testable system properties) versus in the Substrate Brief (as build items)?
2. Does the 5-step path need reordering to better serve David's stated priority sequence — foundation now → first revenue business soon → broader idea portfolio later?
3. Does a "Phase State / Operating Mode" substrate item need to exist so Atlas knows which phase he's advising in (foundation / first-revenue / portfolio)?
4. Is "milestone tracking" a missing substrate item or covered by Decisions Register + Session-Start Manifest?
5. Is "zero-setup session resumption" sufficiently addressed by Session-Start Manifest, or does it need its own item?

**Do not skip this review.** Step 1 SOUL.md finishing will be biased by whatever framing exists at the moment we resume. If the charter document changes the framing, we want it changing the SOUL.md, not getting added afterward.

---

## Primary pickup — Step 1: Get Atlas charter-active

**Goal:** Make Atlas's SOUL.md the actual system prompt the model reads at session start. Verify with an unfalsifiable canary check.

**Why this first:** Foundation for everything downstream. Every subsequent step (substrate items, brief review, project intake) requires an advisor that operates from the charter rather than role-playing it. The 2026-05-12 session record documents the discovery that Atlas was never charter-active in the project's prior sessions — every prior "Atlas" response was Sonnet 4.6 with the default generic Hermes SOUL.md. This session changes that.

**Expected duration:** 60-90 minutes if it lands cleanly.

### Pre-flight context to load at session start

1. [`docs/reference/hermes-internals.md`](../reference/hermes-internals.md) — the authoritative 579-line reference produced by the research subagent on 2026-05-12. Read at minimum the TL;DR (lines 10-23) and Sections 2 (Personalities vs Profiles), 5 (Startup Sequence), and 8 (Verification Procedure).
2. [`docs/sessions/2026-05-12-session-record.md`](./2026-05-12-session-record.md) — what happened last night, what was discovered, where SOUL.md drafting paused.
3. [`docs/decisions/approvals-log.md`](../decisions/approvals-log.md) — last 6 entries are the 2026-05-12 evening session decisions (research subagent, SOUL.md assembly approach, v0.2 revisions, activation deferred, deep-dive skipped).
4. [`docs/decisions/ADR-001`](../decisions/ADR-001-adopt-hermes-workspace.md) through [`ADR-004`](../decisions/ADR-004-workspace-native-approval-mechanism.md) — the four foundation decisions.
5. **SOUL.md draft v0.2** — held in the operator's workspace, not in this repo. Resume editing from there.

### Step 1 sub-tasks

1. **Finish SOUL.md draft v0.2 review** — sections 1-5 (title/canary, identity, user context, file load, operating principles) were reviewed and approved on 2026-05-12. Sections 6-8 (Boundaries, Voice, Verification) remain. Walk through each, confirm or revise, lock the document.
2. **Stop services cleanly** on the VPS — Ctrl+C on the pnpm dev terminal cascades and kills gateway + dashboard + workspace UI. Confirm no `hermes-agent`, `pnpm`, or `vite` processes remain via `ps aux | grep -E "hermes|pnpm|vite" | grep -v grep`.
3. **Write SOUL.md to `~/.hermes/profiles/atlas/SOUL.md`** with the canary string embedded.
4. **Ensure profile `.env` has `API_SERVER_ENABLED=true`** — copy from `~/.hermes/.env` or write directly.
5. **Create `~/.local/bin/atlas` wrapper** — bash script that sets `HERMES_HOME=$HOME/.hermes/profiles/atlas` and execs `hermes "$@"`.
6. **Start services in correct order** — gateway with explicit HERMES_HOME, dashboard with same, then pnpm dev in workspace UI directory.
7. **Verify endpoints** — `curl http://127.0.0.1:8642/health` and `curl http://127.0.0.1:9119/api/status` both healthy; gateway process environ contains `HERMES_HOME=/home/hermes/.hermes/profiles/atlas`.
8. **Run the canary verification** — fresh `/new` chat in Workspace, ask Atlas to quote the canary string verbatim. Charter-active if he returns `ATLAS-CHARTER-7734-ACTIVE`; still generic if he says `NOT FOUND` or anything else.
9. **Commit the activated SOUL.md to DavidOS** — once verified, the finished SOUL.md gets committed (the in-progress draft was deliberately held out of git).

### Verification standard

**Step 1 is not complete until the canary check returns the verbatim string.** Do not move to Step 2 until that happens. If the canary fails, troubleshoot using the Hermes internals reference rather than guessing.

---

## After Step 1 lands — the 5-step path

Approved on 2026-05-12 (deep-dive declined; trust path forward):

| # | Step | Duration estimate | Why it matters |
|---|------|---|---|
| 1 | Atlas charter-active | 60-90 min | This session. Blocks everything else. |
| 2 | Atlas reviews Substrate Brief v1 → produces v1.1 | 2-3 hr | Fills the gap from the lost Opus review. First real test of whether charter-active Atlas adds value. |
| 3 | Ship Decisions Register + polish Approvals Log | 2-3 hr | Stops session-over-session re-litigation of the same decisions (a pattern observed on 2026-05-12 evening). |
| 4 | Ship Roles Register + Session-Start Manifest | 2-3 hr | Makes sessions begin from a known state rather than reconstructed-from-memory. |
| 5 | Build Project Intake | 4-6 hr (1-2 sessions) | The inflection point: dropping a new business idea into the system reliably. |

**Pace:** 5-7 focused sessions over 1-2 weeks if no major drift. Each session 2-4 hours, not 9-hour marathons.

---

## What is NOT on the agenda this session

- M6b iZZi Builder Services work — paused per Option B soft fork until substrate ships
- Project Intake design — Step 5, not Step 1
- Charter Regression Suite content — Step 4, not Step 1
- Anything in izzi-foundation, Aion, Jobs, or Skeptic repos — explicitly out of scope per repo-scope principle

If a thought lands that belongs in one of these, capture it as a one-line note for later and continue with Step 1.

---

## Open threads carried forward

Captured for visibility; not blockers:

1. **`docs/atlas/atlas-operating-spec.md`** still has Paperclip references. Atlas's SOUL.md instructs him to load it. Decide next session whether to clean it before activation or accept the partial-staleness as documented.
2. **Within-task model selection pattern** approved as future patch — lands after Opus access is wired in the Substrate Brief.
3. **What goes in the Charter Regression Suite specifically** — open question; would the "Atlas never charter-active" failure have been caught automatically? Worth designing the suite around concrete failure modes already observed.
4. **Substrate Brief v1 (213 lines) on disk in VPS clone** but not yet pushed to GitHub remote. Will be reviewed and revised by charter-active Atlas in Step 2, then committed as v1.1.

---

## Stack state (carried forward from 2026-05-12 wrap)

| Layer | Tool | Notes |
|---|---|---|
| Daily driver UI | hermes-workspace | `localhost:3000` via SSH tunnel |
| Agent runtime | Hermes v0.13.0 + ~94 commits applied 2026-05-12 | Gateway `:8642`, dashboard `:9119` |
| Auth | Claude Pro/Max OAuth | Per ADR-002. Sonnet default; Opus only with explicit approval |
| Host | DigitalOcean VPS `159.223.166.217` | SSH user: `hermes` |
| Atlas | Profile directory exists at `~/.hermes/profiles/atlas/`. SOUL.md is the default generic text. `~/.local/bin/atlas` wrapper does not exist. Activation pending. |  |

**Access:** `ssh -L 3000:127.0.0.1:3000 hermes@159.223.166.217` then `localhost:3000`

**Three SSH sessions to maintain after Step 1 activation:**
1. `HERMES_HOME=~/.hermes/profiles/atlas hermes gateway run` (`:8642`)
2. `HERMES_HOME=~/.hermes/profiles/atlas hermes dashboard --no-open` (`:9119`)
3. `cd ~/hermes-workspace && pnpm dev` (`:3000`)

**Health check (any free SSH session):**
```bash
curl -s http://127.0.0.1:8642/health
curl -s http://127.0.0.1:9119/api/status | head -c 300
cat /proc/$(cat ~/.hermes/profiles/atlas/gateway.pid)/environ 2>/dev/null | tr '\0' '\n' | grep HERMES_HOME
```
