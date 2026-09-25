---
name: decide
description: Record an owner decision in docs/DECISIONS.md and apply its downstream consequences.
argument-hint: "D-<nnn> <answer>"
disable-model-invocation: true
---

# Record decision: $ARGUMENTS

## Current decisions

!`sed -n '/^| ID/,/^$/p' docs/DECISIONS.md`

## Procedure

1. Parse the ID and the owner's answer from `$ARGUMENTS`. If the answer is ambiguous, ask one
   clarifying question before writing anything.
2. Update the row: Status → DECIDED, Decision → the answer in plain words. Append a log line
   `YYYY-MM-DD D-nnn: <change> (by Dmitriy)`.
3. Apply consequences:
   - D-001 → set `coded_id_is_pii` in `config/policy.yaml`; if `data/units/` exists, rerun
     `make label` and everything after it that already ran (calibrate, score, report).
   - D-002 → record the target machine in STATUS.md; the headline speed table uses only runs whose
     `hw.json` matches it.
   - Others → follow the "Consequence if changed" column.
4. Remove the item from "Provisional defaults in use" in STATUS.md.
5. Commit: `decision: D-nnn <short>`.
