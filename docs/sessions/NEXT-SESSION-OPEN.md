# Next Session — Open

**Last updated:** 2026-05-11 (evening session close)
**Last session:** 2026-05-11 afternoon/evening — Paperclip→Workspace migration, repo cleanup, ADR-004, Atlas registration. See `docs/sessions/submitted/` for the session-end debrief.

---

## Current stack (post-migration, validated this session)

| Layer | Tool | Notes |
|---|---|---|
| Daily driver UI | hermes-workspace v2.3.0 | `localhost:3000` via SSH tunnel. Validated end-to-end with Atlas spawn. |
| Agent runtime | Hermes v0.13.0 | Gateway `:8642`, dashboard `:9119`. Update to `e855825` pending. |
| Auth | Claude Pro/Max OAuth | Flat subscription. ANTHROPIC_API_KEY dormant fallback in ~/.hermes/.env. |
| LLM | Sonnet 4.6 (Anthropic direct) | Per ADR-002. |
| Host | DigitalOcean VPS `159.223.166.217` | SSH user: `hermes` |
| Atlas | Registered as Hermes personality | Activates per-session in Workspace. Memo-library re-spawn validated. |

**Access:** `ssh -L 3000:127.0.0.1:3000 hermes@159.223.166.217` then `localhost:3000`

**Three SSH sessions to maintain:**
1. `hermes gateway run` (`:8642`)
2. `hermes dashboard` (`:9119`)
3. `cd ~/hermes-workspace && pnpm dev` (`:3000`)

**Health check (any free SSH session):**
```bash
ss -tlnp 2>/dev/null | grep -E "8642|9119|3000"
```

---

## Open threads — pick at session start

### Priority 1: M6b — iZZi Builder Services research + scoping

**What it is:** Research-led shaping of iZZi Builder Services. Direction is consulting + tooling combo targeting some mix of (A) solo founders building AI products who are technically capable but overwhelmed by tool sprawl, (B) non-technical founders/operators who want an AI workspace, (C) small businesses (5-50 people) needing an "AI lead" without deep tooling experience.

**Two phases:**
1. AI-assisted research — landscape scan of current AI consulting/tooling offerings, pricing benchmarks, what's working and what's commoditized, where the wedge is between targets A/B/C
2. Scoped one-pager — informed by phase 1, commit to a target customer/wedge/pricing/sequence, draft, commit, move project-registry.md from Exploring → Active

**Why this is queued and not done:** Open-ended scoping deserves a fresh focused session, not tail-end attention. The Phase 1 research has compounding value — keeps the strategy open to amendment based on what we learn rather than committing prematurely.

**Estimated time:** 90-120 min (research ~45 min, scoping ~30 min, drafting ~45 min)

### Priority 2: Atlas charter update — wire in ADR-004

ADR-004 (Workspace-native approval mechanism) shipped this session. Atlas's personality charter in `~/.hermes/config.yaml` doesn't yet instruct him to use the two-intensity approval format. Small paste-and-run edit to add an "Approval discipline" section pointing at ADR-004. Atlas picks up the ADR via boot-time context load even without the charter update, so this is enhancement not blocker. ~10 min.

### Priority 3: Hermes Agent update available

`9a63b5f → e855825`. Routine. Take at session start before substantive work so a restart doesn't interrupt anything. ~5-10 min.

### Priority 4: Recurring threads

- FamilyAI product sprint — `docs/product/07-recommended-mvp.md` deliberately withheld pending founder review. Real product work, separate from M6b infrastructure.
- ADR-005 candidate — retro-ADR for Stage 1 folder layout (`raw/wiki/output/archive/daily/atlas` curation scheme). Listed in `docs/decisions/README.md` pending list.
- Workspace baseline-config.md TBDs — workspace name (rename to "DavidOS"?), profile name, mobile pairing decision.

---

## Strategic position (unchanged unless flagged)

- **Foundation-first sequencing:** DavidOS → FamilyAI → iZZi Builder Services → downstream
- **iZZi customer-zero:** every config/architectural decision evaluated for reusability vs David-specific. In-session priority is always David's optimal system; reusability is harvested at session end.
- **Sonnet-class only.** No Opus without explicit approval.
- **Approval discipline:** ADR-004 active. See `docs/decisions/approvals-log.md` for current approvals.

---

## Reference paths

- Repo: `/home/hermes/projects/personal-ai-workspace/` (HEAD `1493b6e`)
- Hermes config: `~/.hermes/config.yaml` (atlas personality added today)
- Workspace install: `~/hermes-workspace/`
- Canonical docs map: see root [README](../../README.md)
- Approvals: [`docs/decisions/approvals-log.md`](../decisions/approvals-log.md)
- Hygiene checklist: [`docs/sessions/REPO-HYGIENE-CHECKLIST.md`](./REPO-HYGIENE-CHECKLIST.md)

---

*If this date is older than two weeks, run the hygiene checklist before trusting the state above.*
