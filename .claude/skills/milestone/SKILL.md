---
name: milestone
description: Execute one benchmark milestone (M0-M8) end to end, from scope to passed gate and commit.
argument-hint: "M<n>"
disable-model-invocation: true
---

# Execute milestone $ARGUMENTS

## Current state

!`sed -n '1,30p' docs/STATUS.md`

!`git log --oneline -8 2>/dev/null || echo "(no git history yet)"`

## Procedure

1. **Load scope.** Read the `$ARGUMENTS` section of `docs/MILESTONES.md` and every spec it links.
   Read `docs/DECISIONS.md`. If the previous milestone's gate is not marked passed in STATUS.md,
   stop and tell the user.
2. **Check decisions.** List any OPEN decision this milestone depends on. If the gate depends on it
   and the work is expensive to redo, ask the user before building. Otherwise proceed on the
   provisional default and note it in STATUS.md.
3. **Plan backwards.** Write the plan as a task list: gate checks first (as failing tests or
   commands), then the smallest set of modules that makes them pass. Domain types before logic.
4. **Build in sub-steps.** After each sub-step: `make check`, then commit `$ARGUMENTS: <what>`.
   Long runs go to the background with a log file; poll it.
5. **Run the gate.** Execute every gate check in `docs/MILESTONES.md` for `$ARGUMENTS` and capture
   the output.
6. **Independent review.** Invoke `/gate $ARGUMENTS` (spawns the `gate-reviewer` subagent, which
   hasn't seen your work). Fix anything it rejects, then rerun it.
7. **Close out.** Update `docs/STATUS.md` (milestone row, provisional defaults, next action, session
   log line) and commit `$ARGUMENTS: gate passed`.
8. **Report** to the user in under 10 lines: what exists now, gate evidence summary, anything
   provisional, next milestone.

## Rules

- Stay inside this milestone's scope. Note out-of-scope ideas in STATUS.md under "Later".
- Never weaken a validator, gate check, or test to get green. If a check is wrong, say so and ask.
- Follow the invariants in CLAUDE.md; a hook blocks edits to generated artifacts.
