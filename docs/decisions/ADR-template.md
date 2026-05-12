# ADR-NNN: <short kebab-case title>

**Date:** YYYY-MM-DD
**Status:** Proposed | Accepted | Deprecated | Superseded by ADR-XXX
**Deciders:** David Izzard

## Context

What is the situation that requires a decision? Include relevant constraints, observations, and prior context. Keep this 2-4 paragraphs. Cite specific evidence (file paths, commit SHAs, dates, costs) where useful.

## Decision

The decision in one or two sentences. Be specific and actionable.

## Rationale

Why this choice over the alternatives. List 3-5 bullets:

- **Alternative A considered.** Why rejected.
- **Alternative B considered.** Why rejected.
- **Primary factor for chosen path.** What makes it the right call right now.
- **Cost / risk trade-off.** What we're giving up.
- **Reversibility.** Can this be undone if it turns out wrong?

## Consequences

What changes as a result. Include:

- New things that need to exist or be maintained
- Old things that become obsolete (and where they get archived)
- Downstream effects on other repos, agents, customers
- Anything that should be added to operating principles

## Re-evaluation triggers

The signals that would make us revisit this decision:

- Trigger 1 (be specific — what would we observe?)
- Trigger 2
- Trigger 3

Default review window: 90 days unless triggers fire first.

## Related

- ADR-XXX — link to related decisions
- `docs/...` — link to relevant docs

---

**How to use this template:**

1. Copy this file to `docs/decisions/ADR-NNN-short-title.md` (pick the next NNN by checking the highest existing number)
2. Fill in every section. If a section truly doesn't apply, write "N/A — <one-line reason>" rather than deleting the header
3. Update `docs/decisions/README.md` index with the new ADR
4. Commit with message: `docs(adr): NNN — <short title>`
