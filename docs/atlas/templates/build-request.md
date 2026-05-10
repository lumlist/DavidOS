# Build Request — Issue Description Template

Paste the contents of this file into the description of a new Paperclip issue when the issue is fundamentally a "I want this thing built" issue.

---

## Outcome

<One sentence: what does the world look like when this is done?>

## Smallest viable scope

<The minimum thing that would deliver the outcome. Resist the temptation to scope-creep at intake — separate "phase 1 must-haves" from "phase 2 nice-to-haves" below.>

## Out of scope (explicitly)

<What this issue does NOT include. Adjacent things that look like they belong here but don't.>

## Success criteria

- <Criterion 1, ideally measurable>
- <Criterion 2>
- <Criterion 3>

## Risk class

- [ ] Reversible — git revert / config rollback returns the system to prior state
- [ ] Hard to reverse — possible but expensive (data migrations, cancelled subscriptions)
- [ ] Irreversible — permanent (deletes, account creation, public commits to canonical artifacts)

## Approval gates anticipated

List the `[APPROVAL: <kind>]` gates this build is expected to need: `code-change`, `install`, `paid-service`, `credential`, `runtime-config`, `production`, `scheduling`, `new-agent`, etc. Lets David budget approval attention up front.

## Dependencies

<Other issues / approvals / installs / decisions that must complete first.>

## Acceptance / done definition

<The specific check that proves the outcome was achieved.>
