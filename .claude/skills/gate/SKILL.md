---
name: gate
description: Independent acceptance review of a milestone gate using the gate-reviewer subagent.
argument-hint: "M<n>"
disable-model-invocation: true
---

# Gate review for $ARGUMENTS

1. Delegate to the `gate-reviewer` subagent with this task:
   "Review milestone $ARGUMENTS of laya-pii-bench. Read its gate in docs/MILESTONES.md, run every
   gate check yourself, inspect the code and outputs it depends on, and check the CLAUDE.md
   invariants relevant to this milestone. Return PASS or FAIL with evidence per check, plus any
   invariant violations."
2. Save the reviewer's full response to `reports/audits/$ARGUMENTS-gate-<YYYYMMDD-HHMM>.md`.
3. If FAIL: list the failing checks for the user and fix them (inside the milestone scope), then
   run this again. If PASS: mark the gate passed in `docs/STATUS.md` with the audit file name.
