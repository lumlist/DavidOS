# daily/

**Purpose:** David's daily notes — the structured-but-low-effort input layer that feeds the Daily Operating View.

**Naming convention:** `YYYY-MM-DD.md`, one per day. The current day's note is also reachable via `today.md` (a symlink or generated mirror — to be decided in Stage 2 / 3).

**Template:** see `docs/atlas/templates/daily-note.md`. Sections: Top of mind / Decisions I want made today / Things I'm waiting on / What I learned yesterday / Cost-energy check (1-5).

**Write permission:**
- David writes freely.
- Atlas may **append** `[ATLAS-NOTE]` blocks (clearly labeled, dated) to an existing day's note when surfacing a non-urgent observation. Atlas does not edit David's text in place.
- The Daily Operating View renderer (Stage 3) reads from `today.md` and from the most recent dated file.

**Auto-archive:** files older than 90 days are eligible for automatic move to `archive/daily/<year>/`. Deterministic, reversible, logged in git — no separate approval.

**Out of scope here:** decision memos (use `output/<issue-id>-decision-*.md`), durable reference (use `wiki/` after promotion), Atlas operating notes (use `atlas/`).
