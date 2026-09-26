# Milestones

Built backwards: scorer and report exist before the data that feeds them, so every upstream stage
targets a known contract. Each milestone ends at a **gate**: a list of checks that must all pass,
verified by `/gate M<n>` (independent reviewer subagent). Don't start M<n+1> until M<n>'s gate passes
and STATUS.md says so.

Gate format: each check is a command plus the expected result. "Evidence" = paste the command output
into the gate review.

---

## M0 Bootstrap

**Goal:** a working environment that can load Laya and time one call.

**Build**
- `pyproject.toml` deps resolve (`uv sync`).
- `bench/__init__.py`, `bench/cli.py` with a Typer app and a `hw` subcommand.
- `bench/hw.py`: writes `hw.json` (OS, arch, CPU, RAM, torch version, device chosen: cuda/mps/cpu,
  laya version, checkpoint revisions).
- `scripts/download_models.py`: pre-fetches `convaiinnovations/laya` (root) and the `multilingual`
  subfolder to the HF cache; prints revisions.
- `scripts/laya_smoke.py`: preloads the English checkpoint, runs one two-option choice question 20
  times, drops the first 5, prints p50/p95 ms and the answer.
- `tests/test_smoke.py`: CLI imports; `hw` writes valid JSON.

**Gate**
1. `make check` exits 0.
2. `uv run bench hw` writes `hw.json` with a non-empty `device` field.
3. `uv run python scripts/laya_smoke.py` prints an answer with probabilities summing to 1 ± 1e-3 and
   a p50 latency.
4. `docs/STATUS.md` records device and p50 from step 3.

---

## M1 Contracts + fixture

**Goal:** the domain model is the contract. Everything later validates against it.

**Build**
- `bench/domain.py` per `docs/specs/domain.md` (Document, Span, Negative, Chunk/Unit, GoldAnswers,
  QuestionSet, Answer, Decision, RunMeta, CalibParams, Scores).
- `bench/config.py`: typed loaders for `config/policy.yaml`, `config/gen_spec.yaml`,
  `config/arms.yaml`, `config/questions/*.yaml`. Unknown keys are errors.
- `bench/schema_export.py` + `make schema`: writes `schema/*.json`; `hud/src/types.gen.ts` generated
  from them (json-schema-to-typescript via npx).
- `fixtures/mini/docs.jsonl`: **10 hand-written documents** covering: dense PHI narrative, clean
  protocol text, staff-only delegation log, CRF table with subject IDs only, email thread with
  signature block, a doc with a span crossing a 256-token boundary, a hard-negative-only doc
  (protocol no., NCT, lot no., Kaplan-Meier), OCR-noisy MRN, pre-redacted `[REDACTED]` content,
  one German doc. Spans hand-labeled with exact offsets.
- `bench/validate.py` + `make fixture`: offset integrity, span/negative non-overlap, category and
  role enums, policy consistency.

**Gate**
1. `make check` exits 0 with ≥ 90% line coverage on `bench/domain.py`, `bench/config.py`,
   `bench/validate.py`.
2. `make fixture` reports 10/10 valid.
3. `schema/` and `hud/src/types.gen.ts` regenerate with no diff (`make schema && git diff --exit-code`).
4. After the gate: create `.locks/fixtures` (empty file). The protect hook then blocks edits to
   `fixtures/`.

---

## M2 Scorer + report on fixture

**Goal:** every metric exists and is proven correct on numbers a human can check.

**Build**
- `bench/label.py` (minimal for now): segmenter for `chunk` units + gold derivation per
  `docs/specs/gold-labels.md`. Run on fixture only.
- `fixtures/mini/decisions_mock.jsonl`: hand-written decisions with chosen probabilities.
- `bench/calibrate.py`: temperature fit per (question, option count) minimizing NLL; threshold sweep
  for `t_low` at target recall; writes `CalibParams` with a content hash.
- `bench/score.py`: all metrics in `docs/specs/metrics.md`, slices, document-level bootstrap CIs.
- `bench/report.py`: `reports/report.md` from scores.
- `tests/test_metrics_golden.py`: expected accuracy, macro-F1, confusion, ECE, Brier, recall at
  threshold, forward rate, computed by hand in the test file for the mock decisions.

**Gate**
1. `make check` exits 0; golden metric tests pass exactly (tolerance 1e-9).
2. `uv run bench score --decisions fixtures/mini/decisions_mock.jsonl ...` then `bench report`
   produce a report containing every section listed in `docs/specs/metrics.md`.
3. Scoring with a modified `calib/*.json` (hash mismatch) exits non-zero.

---

## M3 Runner, arm A on fixture

**Goal:** real Laya calls, honest timing, resumable.

**Build**
- `bench/laya_client.py`: wraps `Router`/`laya.load`, preload, device selection, `max_len` and
  `head_max_len` from arm config, warmup, per-call timing (`time.perf_counter_ns`), batch-1 and
  batched modes.
- `bench/questions.py`: builds Laya question dicts from `config/questions/*.yaml`; enforces
  invariant 5 (rejects `noul` for English checkpoint).
- `bench/run.py`: iterates units, writes `Decision` JSONL append-only; resume by skipping unit ids
  already present; `meta.json` with hw fingerprint, checkpoint revision, config hashes.
- Truncation detection: token count with the checkpoint tokenizer vs. state budget.

**Gate**
1. `uv run bench run --arm A --qs qs_v1 --docs fixtures/mini/docs.jsonl` completes; every decision
   validates against the schema.
2. Rerunning the same command makes **0** Laya calls (log line `resumed: N/N already done`).
3. `meta.json` contains hw fingerprint, warmup count, and checkpoint revision.
4. `bench score` + `bench report` run end to end on these real decisions (fixture has no calib
   split: use `--calib-from fixture` debug flag, clearly labeled in the report).
   *Implemented as `bench calibrate --debug-fit-all` + `bench score --allow-debug-calib` (D-013).*

---

## M4 Generator

**Goal:** 600 documents with exact gold, at controlled distributions, reproducible.
Spec: `docs/specs/generator.md`. This is the largest milestone; build in the listed sub-steps and
commit after each.

**Build (sub-steps)**
- 4a World model + Faker providers (subject ID, MRN, rand no., lot no., site-specific formats).
- 4b Sentinel renderer + validators V1 (offsets) and V2 (no unlabeled world PII). Two templates:
  `csr_patient_narrative`, `protocol_section`.
- 4c Remaining 10 templates.
- 4d Hard-negative registry and injector.
- 4e Length buckets and PII-depth placement with a grammar-generated filler bank.
- 4f Perturbations with span remap (line wrap, OCR noise, tables, headers/footers, email quoting).
- 4g Full generation, manifest, distribution check.

**Gate**
1. `make gen` produces `data/docs.jsonl` with exactly 600 docs and 0 validator failures (V1–V6).
2. Running `make gen` twice produces identical `sha256` of `data/docs.jsonl`.
3. Realized distributions (doc type, lang, length bucket, hard-negative rate, perturbation rates)
   within ±3 percentage points of `gen_spec.yaml` (or exact counts where specified).
4. Hypothesis tests on renderer and span remap pass (≥ 500 examples each).
5. `gold-auditor` subagent reviews a seeded random sample of 30 docs and reports zero label errors.
   Its report is saved to `reports/audits/M4_gold_audit.md`.

---

## M5 Label + split

**Goal:** gold answers for every arm's unit type; leak-free splits.

**Build**
- `bench/label.py` full: units for chunk (256/768), section (2k), doc (4k/8k) per arm config;
  gold answers per `docs/specs/gold-labels.md`; `truncated` flag; `split_span` flag.
- `bench/split.py`: site-grouped stratified split + holdout doc type.
- Calib freeze (D-019): stop ignoring `calib/` and `scores/` in `.gitignore`; `make freeze-calib`
  commits calib files with their content hashes in the message; `bench score` refuses a calib file
  that isn't committed and unmodified at HEAD and records the calib commit sha and time in
  `RunContext`. Split-aware `calibrate` (fit on calib only) and `score` (test/holdout).

**Gate**
1. No site id and no subject id appears in more than one of train/calib/test (test asserts).
   Holdout (all IRB letters, D-005) is exempt from site grouping and contains no subject ids.
   No staff person id appears in more than one of train/calib/test (D-018).
2. Each of train/calib/test has ≥ 1 example of every gold class for every question in both
   question sets (report counts; if a class is missing in calib, stop and ask). Holdout class
   counts are reported, missing classes marked (D-005).
3. Label stage is deterministic (hash check).
4. Unit counts per arm and per split written to `data/label_manifest.json`.
5. `bench score` with an uncommitted or locally modified calib file exits non-zero; with a
   committed one, the scores record its commit sha (D-019; tested on the fixture).

---

## M6 Zero-shot arms, calibrate, score, report v1

**Goal:** first real results.

**Build**
- Run arms A, B1, B2, B3, B4 × qs_v1, qs_v2 on train? **No: calib + test + holdout only**
  (train is reserved for fine-tuning; zero-shot arms never need it).
- Calibrate on calib; freeze; score on test and holdout.
- `results-analyst` subagent sanity review.

**Gate**
1. All 10 run dirs have `decisions.jsonl` covering 100% of their calib/test/holdout units.
2. `calib/*.json` files committed **before** any `scores/*.json` exists (git log order checked):
   every scores file cites a calib commit that is an ancestor of the commit adding the scores and
   older than the scores' `created_at` (D-019).
3. `reports/report.md` includes headline operating point, per-question metrics, calibration
   raw vs. calibrated, speed table with hardware label, all slices, bootstrap CIs.
4. If any headline recall CI half-width > 0.01, STATUS flags D-008 for review.
5. `results-analyst` review saved to `reports/audits/M6_results_review.md`.

---

## M7 HUD replay

**Goal:** the Jev-Doom-style decision visualization, replaying real runs.
Spec: `docs/specs/hud.md`.

**Gate**
1. `make hud` builds `hud/dist/index.html` as a single self-contained file.
2. It loads `replay.json` exported from a real M6 run (not mock data).
3. Scrub, play/pause, speed control, and "jump to next false-forward" all work (Playwright test or
   manual checklist with screenshots saved to `reports/audits/M7_hud/`).

---

## M8 Fine-tuned arm C, report v2

**Goal:** the realistic production candidate.

**Build**
- `finetune/`: adapt the Laya fine-tune notebook into a script; dataset built from **train split
  units only**, both question sets; temperatures refit on calib afterwards.
- Train where a GPU is available (Kaggle 2×T4 is the documented path); record where in STATUS.

**Gate**
1. Training data manifest proves train-split-only (assert against `splits.json`).
2. Arm C runs, calibrates, scores; report v2 compares A vs. best B vs. C on the same test units.
3. Checkpoint revision/hash recorded in `runs/C/*/meta.json`.
