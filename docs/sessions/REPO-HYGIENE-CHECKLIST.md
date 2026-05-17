# Repo Hygiene Checklist

> Run this checklist **at the end of any session that ships a structural change** — adopting/removing a tool, changing provider/auth, freezing a project, restructuring directories, or any commit that creates new "canonical truth" in a README or ADR.

The goal: prevent the **parallel-realities problem** — where today's truth lives in one set of files while yesterday's truth still sits unmodified in another set. The 2026-05-11 audit found ~25 files contradicting the day's commits because we didn't run a check like this.

---

## When to run

- After committing an ADR
- After a tool switch (provider, UI, runtime, host)
- After freezing or pausing a project
- After moving large amounts of content
- Before a long session break (going dark for >1 week)

> Start-of-work and pre-push git divergence is handled separately — see the Remote reconciliation step in `docs/atlas/context-refresh-protocol.md` (Level 1). This checklist remains end-of-session / structural-change only.

Skip for:
- Routine content writes inside an established structure
- Single-file edits that don't change canonical truth

## Quick-fire check (5 minutes)

For the change you just shipped, answer each:

1. **What's the new canonical truth?** (One sentence — e.g., "Paperclip is frozen; daily driver is hermes-workspace.")
2. **Where is the new truth recorded?** (Specific file paths.)
3. **Which existing files contradict the new truth?** Run:
   ```bash
   # Grep for terms that the new truth changes. Examples:
   grep -rl "paperclip\|OpenRouter\|127.0.0.1:3100\|Opus" docs/ --include="*.md" | grep -v archive/
   ```
4. **For each contradicting file:** archive, edit, or mark stale (banner at top). Don't leave silently wrong.
5. **Are there orphan references in the new canonical files?** Run:
   ```bash
   # Find paths/files referenced in your new docs that don't actually exist
   for f in README.md docs/sessions/NEXT-SESSION-OPEN.md docs/decisions/*.md; do
     echo "=== $f ==="
     grep -oP '\[`[^`]+`\]\([^)]+\)' "$f" | grep -oP '\([^)]+\)' | tr -d '()' | while read path; do
       [ -e "$path" ] || echo "  MISSING: $path"
     done
   done
   ```
6. **Are downstream repos aware?** (Cross-repo coherence — if DavidOS claims FamilyAI inherits something, does FamilyAI's repo reflect that?)
7. **Does the session memo (`docs/sessions/NEXT-SESSION-OPEN.md`) reflect the new state?**

## Common staleness signals (paste-and-grep)

Run these greps periodically to catch drift:

```bash
# Frozen tools that shouldn't appear as active
grep -rn "paperclip" docs/ --include="*.md" | grep -v -i "archive\|frozen\|adr-003\|hygiene"

# Paused providers
grep -rn "openrouter" docs/ --include="*.md" | grep -v -i "archive\|paused\|adr-002\|hygiene"

# Dead URLs from frozen services
grep -rn "127.0.0.1:3100\|127.0.0.1:3001" docs/ scripts/ --include="*.md" --include="*.py" --include="*.json" | grep -v -i "archive\|hygiene"

# Model policy violations (Opus without explicit approval context)
grep -rn "opus" docs/ --include="*.md" | grep -v -i "archive\|approval\|adr-002\|hygiene"

# Name typo (last name)
grep -rn "Mizzard" .
```

## If a check fails

- **A few files stale, structurally fine:** edit them in the same session
- **Many files stale (10+):** archive the obsolete cluster (`git mv` to `docs/<area>/archive/<era>/`), don't try to rewrite all in one pass
- **Cross-repo incoherence:** at minimum, add a one-line pointer in the downstream repo's most-read doc (often `README.md` or setup log)
- **Orphan reference in canonical file:** create a stub at the referenced path, or remove the reference

## Future automation

This checklist is the manual version. A future `scripts/repo-hygiene-check.py` could codify the greps and return a report. Not built yet — manual run is fine until the pattern stabilizes.
