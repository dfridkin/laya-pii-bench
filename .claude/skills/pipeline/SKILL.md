---
name: pipeline
description: Run the benchmark pipeline (smoke or full) through make targets and summarize results.
argument-hint: "smoke|full"
disable-model-invocation: true
---

# Pipeline run: $ARGUMENTS

Requires milestones through M6 (full) or M3 (smoke) to have passed their gates. Check
`docs/STATUS.md` first and stop if they haven't.

- `smoke`: `make smoke` (20 docs, arm A, qs_v1). Expect minutes.
- `full`: run in order, stopping at the first failure, each long step in the background with a log
  under `runs/logs/`:
  1. `make gen` → check `data/gen_manifest.json` validators all pass
  2. `make label split`
  3. `make run-all` (poll the log; report progress per arm)
  4. `make calibrate` then `make freeze-calib` (commits calib files; `bench score` refuses
     uncommitted calib, D-019)
  5. `make score report`
  6. Delegate to the `results-analyst` subagent; save its review to
     `reports/audits/pipeline_<YYYYMMDD-HHMM>.md`.

Finish with a summary under 12 lines: headline recall + CI and forward rate per arm, p50 latency
with hardware label, anything the analyst flagged, and the report path.
