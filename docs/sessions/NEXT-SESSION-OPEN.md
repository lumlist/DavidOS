# Next Session — Open

**Last updated:** 2026-05-17 (post GIP-ratification arc)
**Repo state at handoff:** `main` aligned with `origin/main`, clean tree, HEAD `961b356`.
**Last session:** the GIP governance arc (David-approved Opus) — ratified the
Governed Intent Protocol *direction*, stood up the governance tree, closed the
approvals-log source-of-truth desync, shipped + validated fetch-before-work
reconciliation discipline, and persisted the bounded Nemanja influence digest.

This file is a **session-handoff pointer, not a governance source of truth.**
It points at canonical files; it does not restate them. If this file and a
canonical file disagree, the canonical file wins.

---

## ⚠ Required first action next session

Run the fetch-before-work reconciliation BEFORE any substantive work
(mandated: `docs/atlas/context-refresh-protocol.md` §3a / Level 1):

```
cd /home/hermes/projects/personal-ai-workspace
git fetch origin
git status -sb
git rev-list --left-right --count HEAD...@{u}
git log --oneline -5
```

Read `N M`: `0 0` aligned (proceed); `0 N` behind-only (FF-safe);
`N 0` ahead-only (safe); `N M` both nonzero = DIVERGED → STOP, characterize
read-only, do not rebase/merge/push/modify, surface to David.
Do no substantive work, commits, or pushes until reconciliation passes.

---

## State of play (verified at handoff)

- **Atlas charter-active.** SOUL.md v1.1 is the live system prompt; canary
  `ATLAS-CHARTER-7734-ACTIVE` confirmed loaded. Step-1 activation work is
  DONE — do not re-run it.
- **GIP direction RATIFIED.** ADR-005 Accepted. Implementation NOT built;
  each later stage separately gated.
  → `docs/decisions/ADR-005-governed-intent-protocol.md`
  → `docs/governance/README.md` (lifecycle + tree orientation)
  → `docs/governance/proposals/2026-05-17-mv-gip-proposal.md` (full §1–§20)
- **Governance source-of-truth desync CLOSED.** approvals-log entries
  R1–R6 index the GIP decision; commit `6352682`.
- **fetch-before-work discipline shipped + validated.**
  → `docs/atlas/context-refresh-protocol.md` §3a; commit `8a8bf56`.
- **Bounded Nemanja digest persisted** as implementation-input only — does
  NOT reopen ADR-005 or the proposal.
  → `docs/charter/influences/nemanja-mirkovic-2026-05-14/atlas-digest.md`
- **ADR-005 index row resolved.** Present at `docs/decisions/README.md`
  line 21. The ADR-005 L104–106 follow-up is CLOSED — do not re-flag it.

---

## Primary pickup — decide the next GIP lifecycle stage

The GIP *direction* is ratified; nothing is implemented. The next session's
job is to **decide and get approval for the next lifecycle stage** — not to
implement inside this handoff.

Canonical lifecycle: `docs/governance/README.md` (proposal → ADR → spec →
registries → manifests → Decision Protocol skill). Dependency order:
MV-GIP proposal §16. Each stage advances only after its approval lands in
`approvals-log.md`.

Candidate next stage (for David's decision, not pre-decided here):
`docs/governance/gip-spec.md`, then agent/substrate registries, then one
project manifest + manifest SCHEMA, then the Decision Protocol skill in the
Hermes profile. BEFORE-bucket action-map fixes (1,3,5,7,16) are independent
and could sequence in parallel — see proposal §15.

Run the gated arc: scoped analysis → chat-only proposal → pre-write plan →
(separate approval) write → verify → (separate approval) commit → push.

---

## Explicitly OUT OF SCOPE

- Ad-hoc GIP implementation (no spec/registry/manifest/skill authored
  without its own gate — `docs/governance/README.md` L11–13).
- Relitigating ADR-005 or the ratified GIP direction (SOUL.md §6/§10;
  ADR-005 "superseded framing").
- Broad Nemanja reanalysis — digest is final, implementation-input only.
- UI build, council build, tool-integration build (Ruflo/Claude
  Code/Codex/NotebookLM/Obsidian adapters) — proposal §19.
- iZZi generalization — second-pass per SOUL.md §5.
- izzi-foundation, Aion, Jobs, Skeptic repos — repo-scope principle.

---

## Open threads carried forward (verified current only)

1. `docs/atlas/atlas-operating-spec.md` still carries Paperclip-era
   references. SOUL.md §4 still instructs Atlas to load it and flags it as
   historical/mechanism-layer-being-rewritten. Decide if/when to clean it;
   not a blocker. [verified — SOUL.md §4]
2. Approval-fatigue detection is a **deferred design consideration**, not an
   active next task. It is a named deferred gap in GIP (ADR-005 "cost/risk";
   proposal §19), to be designed only when the observability-spine schema
   stage is reached. Tracked for future design, not open work now.

(No other 2026-05-12/13-era threads survive — Step-1, 5-step path,
Substrate Brief v1, M6b, Charter Regression Suite framing are all
superseded by the governance line.)

---

## Stack state (corrected)

| Layer | Tool | Notes |
|---|---|---|
| Daily driver UI | hermes-workspace | `localhost:3000` via SSH tunnel |
| Agent runtime | Hermes | Gateway `:8642`, dashboard `:9119` |
| Auth | Claude Pro/Max OAuth | ADR-002. Sonnet default; Opus only with explicit logged approval |
| Host | DigitalOcean VPS `159.223.166.217` | SSH user: `hermes` |
| Atlas | **Charter-active.** SOUL.md v1.1 live at `~/.hermes/profiles/atlas/SOUL.md`; canary verified. |
| Repo | DavidOS clone `/home/hermes/projects/personal-ai-workspace` | `main` @ `961b356`, aligned with origin |

**Access:** `ssh -L 3000:127.0.0.1:3000 hermes@159.223.166.217` then `localhost:3000`

---

## Note on this file

This is a session-handoff pointer. Canonical sources of truth are the ADRs,
`approvals-log.md`, the governance tree, and `context-refresh-protocol.md`.
Preferred practice: refresh this file at session wrap when the next pickup
changes materially, so it does not drift behind the repo.
