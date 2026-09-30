# Status

Active milestone: **M7 HUD replay**
Last updated: 2026-09-30 (M6 gate passed)

| Milestone | State | Gate passed | Notes |
|---|---|---|---|
| M0 Bootstrap | done | 2026-09-25 (`reports/audits/M0-gate-20260925-2255.md`) | mps, p50 67.8 ms |
| M1 Contracts + fixture | done | 2026-09-26 (`reports/audits/M1-gate-20260926.md`) | fixture locked; gold audit 0 errors |
| M2 Scorer + report on fixture | done | 2026-09-26 (`reports/audits/M2-gate-20260926-pass.md`; review #1 FAIL fixed) | golden metrics exact; hash check exits 2 |
| M3 Runner, arm A on fixture | done | 2026-09-26 (`reports/audits/M3-gate-20260926-pass.md`; review #1 FAIL fixed) | real laya run on fixture; p50 ~500 ms/unit (qs_v1, mps) |
| M4 Generator | done | 2026-09-27 (`reports/audits/M4-gate-20260927.md`; gold: `M4_gold_audit_run4_final.md`; R4 fix after gate, D-020) | 600 docs, V1-V6 pass, deterministic; gold audit 0 errors |
| M5 Label + split | done | 2026-09-27 (`reports/audits/M5-gate-20260927-pass.md`; reviews #1, #2 FAIL fixed) | 600 docs split 350/96/124/30, no leaks, all classes in every split; calib freeze enforced |
| M6 Zero-shot arms, calibrate, score, report v1 | done | 2026-09-30 (`reports/audits/M6-gate-20260930.md`; results review `M6_results_review.md`) | 10 runs; calib frozen 4abf110; D-008 flagged; zero-shot operating point degenerate, multilingual no signal |
| M7 HUD replay | not started | | |
| M8 Fine-tuned arm C, report v2 | not started | | |

## Provisional defaults in use

None. D-001 (no), D-002 (M2 on-device; HF inference fallback), D-008 (amended), D-014 (top
probability) decided 2026-09-27.

## Audit C-items (before M6)

- C1 decided (D-019), built in M5. C2 done (invariant 6 reworded, D-014). C3 decided (D-008 amended).
- C4-C8 owned by Claude, no decision needed: C4 probe B3/B4 memory on the M2 before M6 (failure goes
  to the D-002 fallback); C5 align B2 target (1800 > 1792 budget) and keep long/xl overshoot as the
  truncated slice; C6 batch-1 vs batched side by side in score/report; C7 score writes a routed
  JSONL for the HUD; C8 `bench smoke`, split config section, `splits_to_run`, qs_v1 vs qs_v2
  comparison section, MPS autocast switch detection.

## M0 evidence

- Hardware (`hw.json`): Apple M2, 8.0 GB RAM, macOS Darwin 24.3.0, arm64, Python 3.12.8,
  torch 2.14.0, laya 0.3.20, **device: mps**.
- Checkpoint: `convaiinnovations/laya@55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851` (english and
  multilingual, pinned in `models.lock.json`).
- `scripts/laya_smoke.py` (english, 1 two-option choice question, max_len 512, head_max_len 192,
  20 calls, first 5 dropped, batch-1): answer `A`, probabilities `{A: 0.8575, B: 0.1425}`,
  sum 1.0000, **p50 67.8 ms**, p95 70.6 ms, load 29.8 s.

## M1 evidence

- `make check`: 104 passed, 2 skipped (model-marked); coverage domain 100%, config 100%, validate 99%
  (per-file >= 90% enforced in `make test`).
- `make fixture`: 10/10 valid. `make schema && git diff --exit-code`: no diff.
- Model-marked tests (`LAYA_SKIP_MODEL=0 USE_TF=0 uv run pytest -m model`): 2 passed, incl. fx06 address
  span on English tokens 245-262 (straddles the 256-token chunk boundary).
- Gold audit of all 10 fixture docs: 0 label errors (`reports/audits/M1_fixture_gold_audit.md`).
- `.locks/fixtures` created after the gate.

Deviations from the scaffold (accepted by gate review):
- `make schema` exports one combined `schema/domain.json`; the old glob input made json2ts write a
  directory instead of `hud/src/types.gen.ts`.
- Fixture gold is inline sentinel markup in `fixtures/mini/src/*.yaml`, resolved left to right by
  `bench/markup.py` (`bench build-fixture`); never located by string search.
- `Scores` deferred to M2 per `docs/specs/domain.md` (MILESTONES lists it under M1).
- `config/questions/qs_v2.yaml`: quoted `yes`/`no` criteria (YAML parsed them as booleans).
- `HwInfo` moved into `bench/domain.py`; `RunMeta.hw` is typed `HwInfo` instead of `dict`.
- Validator also rejects span/negative edges that cut inside a word (gate finding 3).

## M2 evidence

- `make check`: 148 passed, 3 skipped (model-marked; `-m model`: 3 passed). Golden metric tests
  (`tests/test_metrics_golden.py`) pass at tolerance 1e-9 against hand arithmetic on the mock
  decisions (identity calibration, t_low 0.25, t_high 0.85): accuracy 8/11, confusion [[6,2],[1,2]],
  macro-F1 (12/15 + 4/7)/2, ECE 3.08/11, Brier, AUROC 19/24, recall 7/8, forward rate 2/11,
  1 false forward (fx06 chunk 1, missed `address`). Temperature fit golden: T = 2 exactly.
- Gate 2: `bench label` (fixture, arm A, 11 units) -> `bench calibrate --debug-fit-all` ->
  `bench score --allow-debug-calib` -> `bench report` writes `reports/fixture/report.md` with all
  9 metrics.md sections (test asserts the headings against the spec).
- Gate 3: score with a calib file whose `t_low` was edited exits 2 ("content hash mismatch") and
  writes no scores (manual run + test).
- Gate review #1 FAILED (`reports/audits/M2-gate-20260926-fail.md`): calibrated AUROC was wrong
  on permuted-probability ties (key-order float noise in `apply_temperature`). Fixed with an
  order-independent `math.fsum`; golden tests added for exact ties at T != 1 and for qs_v2
  multi-label F1. The `fit_on: fixture_debug` widening and the confidence definition are now
  OPEN entries D-013 and D-014 in DECISIONS.md.
- One-time fixture unlock to add `fixtures/mini/decisions_mock.jsonl` (owner approved; logged in
  DECISIONS.md); lock recreated in the same commit.

Interpretations made in M2 (cheap to change; flag if you disagree):
- Routing: predicted role `both` forces REDACT like `patient` (PLAN says "role = patient"; `both`
  includes patient data). qs_v2 has no role question, so routing there is threshold-only.
- `category` gold uses only categories counted as PII; `categories_multi` is raw presence. Only
  differs if D-001 flips to "no": then `has_coded_id` can be A while `pii_present` is B.
- Temperature scaling acts on log of laya's 4-dp probabilities (zeros clipped to 1e-6).
- `t_high`: smallest observed p reaching the precision target; 1.0 if unreachable; never < t_low.
- Macro-F1 averages over labels present in gold or predictions; majority baseline is computed on
  the scored set; ECE/AUROC use max probability (laya's entropy `confidence` is stored, not used).
- `CalibParams.fit_on` gained `fixture_debug` (D-013, OPEN); `score` refuses it without `--allow-debug-calib`,
  and the report prints a DEBUG banner.
- Until `bench split` exists (M5): `calibrate` only runs with `--debug-fit-all`, and `score` treats
  every document as split `fixture`. Units are written to `<out>/{arm}.jsonl`.

## M3 evidence

- Gate review #1 FAILED (`reports/audits/M3-gate-20260926-fail.md`) on three latent invariant-9
  defects, now fixed with tests: decisions record `mode` (batch1/batched) and post-call `device`, and
  speed splits on mode (a batched tail never counts as batch-1); resume refuses a changed checkpoint
  revision or hw/runtime fingerprint; a mid-run laya fallback to cpu aborts and discards the batch.
  The fixture run was regenerated after the fix (pre-fix run moved to scratch, not edited).
- `make check`: 160 passed, 7 skipped; model-marked tests (7 passed) (`LAYA_SKIP_MODEL=0 USE_TF=0 uv run pytest -m
  model`) include the real-client tests (adapter, per-question state room, tokenizer agreement).
- Gate 1: `uv run bench label --docs fixtures/mini/docs.jsonl --arm A` (-> `data/mini/units/A.jsonl`),
  then `uv run bench run --arm A --qs qs_v1 --docs fixtures/mini/docs.jsonl` completed: 21 laya calls
  (10 warmup + 11 units), exit 0. All 21 decisions and `meta.json` validate against
  `schema/domain.json` (jsonschema: 0 errors) and the pydantic models.
- Gate 2: rerun logs `resumed: 11/11 already done` and `laya calls: 0`; the checkpoint isn't loaded.
- Gate 3: `runs/mini/A/qs_v1/meta.json` has the hw fingerprint (Apple M2, 8 GB), `device: mps`
  (actual), `warmup_calls: 10`, `checkpoint_rev: 55cf4c4e...`, config hashes (arm, qs, docs, units).
- Gate 4: `bench calibrate --debug-fit-all` -> `bench score --allow-debug-calib` -> `bench report`
  on the real decisions: `reports/fixture/report_armA_qs_v1.md`, all 9 sections, DEBUG banner.
  The milestone text says `--calib-from fixture`; the equivalent here is the D-013 debug pair.
- Timing: batch-1 p50 504 ms/unit, p95 588 ms (run 2; run 1: 497 / 651) (qs_v1, 4 questions, ~190-token chunks, mps).
  Controlled check with laya directly: 1 question/short state 61 ms (matches M0), 1 question/190
  tokens 125 ms, 4 questions/short 226 ms, 4 questions/190 tokens 515 ms. Latency scales with the
  number of questions (one sequence row each) and state length; runner overhead is negligible.
- Truncation: laya's real per-question state room for arm A is 420-476 tokens (qs_v1: 420-459,
  qs_v2: 449-476), above the spec's 320 (`max_len - head_max_len`), so `unit.truncated` from the
  label stage is conservative. The runner records exact `state_tokens` and `truncated_questions`
  per decision; the truncated slice uses either signal. laya's tokenizer matches the label stage's
  token counts on all 11 fixture units.
- Zero-shot arm A on the fixture is weak (expected per the model card): see the report.
- Warmup: 10 calls (spec default) on whole fixture documents, which laya truncates to `max_len`;
  the spec says "fixture units". Same input shapes, excluded from every metric; noted as a deviation.

## M4 evidence

- `make gen`: 600 docs, validators ASSEMBLY/V1/V2/V3/V4/V5/V6 all pass (`data/gen_manifest.json`);
  ~23 s on the M2 including the V6 second generation. Final corpus sha256 `3507af1fba6661b4...`,
  identical across separate `make gen` runs (gate 2). `bench validate data/docs.jsonl`: 600/600.
- Gold audit (gate 5): three runs on the same seeded 30-doc sample, each zero label errors; each run's
  generator-level judgment calls were fixed before the next (no label changes). Final corpus record:
  `reports/audits/M4_gold_audit_run3_final.md` (runs 1-2: `M4_gold_audit_run1.md`,
  `M4_gold_audit.md`). The final run also checked all 60 partial-redaction docs and all 1,268 CRF rows.
- Realized distributions equal gen_spec exactly (gate 3): doc types as specified; lang 540/24/18/18;
  buckets 210/210/132/48; hard_negative .25, headers_footers .40, line_wrap .30, ocr_noise .10,
  table .20, email_quoting on all 60 correspondence docs; 174 clean/pre-redacted docs; pii_depth
  20/20/20.
  Partial pre-redaction (gold audit N5, `gen_spec.partial_redaction_docs: 60`): 46 of the 60 flagged
  docs realize at least one placeholder (reported in the manifest); pre_redacted tag on 59 docs.
- Hypothesis tests (gate 4): sentinel resolve 600 examples (`tests/generate/test_render.py`), span
  remap 700 examples (`tests/generate/test_perturb.py`). `make check` 299 passed.
- Sub-steps: 4a world + providers + doc_plan (owner-approved), 4b renderer/variants/V1-V2, 4c all 12
  types (27 templates incl. de/es/pl), 4d hard negatives, 4e length/filler/depth, 4f perturbations,
  4g planner + manifest.

Design choices made in M4 (flag if you disagree):
- Content-adding steps (hard-negative paragraphs, filler, headers/footers, the depth PII block) are
  spliced into the raw rendered text before the one sentinel pass, so their labels need no remap;
  only character-level perturbations (line wrap, OCR noise, table restyle) run after resolve with
  span remap. Email quoting is native to the correspondence templates. (Spec said all perturbations
  after resolve; the audit showed the remap contract can't express inserted labeled content.)
- Every person (incl. sponsor/CRO contacts) belongs to one site, so each site has its own sponsor
  contact rather than a study-wide medical monitor (D-018).
- Person names are drawn to avoid every word the generator can emit (templates, filler grammar,
  month names, AE terms, ...), and family names are unique and >= 3 letters, so V2 is unambiguous.
- Document dates avoid any rendered form of a referenced subject's dates (07/08 vs 08/07).
- NCT ids start `NCT99`, EudraCT uses 2031, CAS-format numbers carry an invalid check digit.
- The M1 validator rule "hard_negative tag iff negatives" is now "tag -> negatives" (D-015).
- Site locales: 14 en, 4 de, 3 es, 3 pl sites (`world.site_locales`); non-English docs come from
  sites of their locale. M5 should stratify the site split on locale too, or the language slice
  may land in one split.
- Gold-audit fixes (no label changes): SAE forms report real, preferably serious, world AEs;
  deviation logs list only world deviations; CRF rows are distinct (subject, visit); document dates
  follow the events and avoid every rendered form of referenced (incl. PII-depth) subjects' dates;
  eponyms fit their sentence; non-English docs are native-only (no English filler, translated AE
  terms, localized headers); placeholders grammatical; CRO domain distinct from site names.

R4 fix after the gate (owner decision D-020): 100 PII-bearing docs show neutral alt text beside real
PII; the shortcut metric fell from 49/104 to 3/106 PII-free site docs (manifest; V5 fails above 5%),
confirmed independently by gold audit run 4 (`reports/audits/M4_gold_audit_run4_final.md`, zero label
errors). Gate re-run on the final corpus (sha256 `9a88ce5c4c5b4a85...`): `make gen` all validators
pass, identical across separate runs, 600/600 valid, fixture 10/10, `make check` 310 passed.

Known limitations (not label errors):
- S1: line-level alt residue in IRB letters ("Contact: IRB office, IRB office" in all 10 PII-free
  letters, none PII-bearing). IRB letters are holdout-only (D-005), so train/calib/test are
  unaffected; M6 should caveat holdout IRB results. Phrase-level metric residue: 3 de/pl emails.
- R1: partial redaction is per value, so a redacted name can sit next to the same person's labeled
  email/initials. Labels are correct; realism is imperfect.
- N7 accepted: a document date can equal another same-site subject's date (not tied to that subject
  in the text; not PII; V2 correctly scoped).

## M5 evidence

Sub-steps: 5a Splits/LabelManifest types + config/split.yaml (419bb58); 5b section/doc units, B2
target aligned (ebd70a5); 5c split stage (8b885c4); 5e calib freeze + split-aware
run/calibrate/score (1f46a93); 5f staff leakage check, real-corpus label/split, fixture regenerated
under D-001 (7faf571).

- Corpus 9a88ce5c (M4 final). `make label`: A 9590 units, B1 3209, B2 1548 (21 truncated), B3 891
  (1), B4 600 (51); 12 s.
- Gate 1: `make split` exits 0: `leakage` (site, subject; holdout has no subjects) and
  `staff_leakage` (world staff values unique to one site) both empty. Tests: test_split gate-1 and
  crossing-detection tests (site, subject, staff). Splits 350/96/124/30 docs; sites 15/4/5; locales
  train en326 de12 es8 pl4, calib en77 pl8 de8 es3, test en107 es7 pl6 de4; holdout = 30 IRB letters.
  Max document-share error 0.0047 (tolerance 0.05).
- Gate 2: label_manifest `missing` = []; minimum count of any gold class for any arm x qs x question:
  train 31, calib 8, test 10. Holdout: 55 missing classes reported in `holdout_missing` (D-005).
- Gate 3: `make label` twice, all five units files byte-identical (A 62022ad2, B1 1e606484,
  B2 b24f0bbd, B3 919a2d7f, B4 58504d2d). `make split` twice: splits 74291488, manifest 3146555d
  identical.
- Gate 4: data/label_manifest.json has units, truncated and split_span counts per arm x split, and
  gold class counts per arm x qs x question x split, with docs/policy/splits/units hashes.
- Gate 5 (fixture, mock decisions): uncommitted calib -> exit 2 "is not committed"; committed calib
  reindented (same content hash) -> exit 2 "differs from its committed version"; committed -> exit 0,
  scores record calib_commit 3b26c12f / 2026-09-27T22:16:16-04:00 = git log of the file. Tests:
  tests/test_freeze.py (8). Fixture arm A rerun (21 laya calls), calib frozen at cceb8775.
- Gate reviews: #1 FAIL (`reports/audits/M5-gate-20260927-fail.md`: D-013 flags reachable on the
  main corpus without meta or under another name; calib in another repo; skip-worktree) fixed in
  9ca1209. #2 FAIL (`M5-gate-20260927-fail2.md`: guard failed open outside the repo cwd and trusted
  caller-supplied doc text) fixed: the guard now decides by document id only (ids in the
  project-anchored data/docs.jsonl, or the generator's `d0000` format, so it fails closed without
  data/); calibrate lost its --docs option. Tests in tests/test_freeze.py run without data/.
- Split-aware stages: calibrate fits on calib-split units only (fit_on=calib); score scores test and
  holdout and checks the run's splits hash; run on main filters by splits_to_run and hashes splits;
  debug calib flags refused on the main dataset (D-013).

## M6 evidence

Sub-steps: 6a score/report additions (96a71da: C4 probe record, C6 batched speed input, C7 routed
JSONL, C8 autocast per decision, D-008 column, doc-level label, qs_v1 vs qs_v2 table); 6b latency
outlier caveat (87e74ce); 6c Makefile loops (859dcce); runner fixes during the runs (8e004bb MPS
release + caffeinate; 16d664a NaN retry + per-call release for B4; f262ce3; 1b0ba0b batched arms);
calib frozen 4abf110; scores + report 54e3512.

- C4: B4 longest unit fits on the M2 in isolation (reports/audits/C4_memprobe-20260928.md). In
  long runs B3/B4 grew the MPS cache until the process swapped (latency 3x, NaN); fixed by
  releasing the cache between calls (every 25; every call for B4), outside the timer.
- Gate 1: all 10 batch-1 runs cover 100% of calib/test/holdout units (A 3603, B1 1215, B2 593,
  B3 345, B4 250 per qs), finished, no retried decisions. Batched (speed only): A and B1 x 2 qs.
- Gate 2: all 10 calib files frozen in 4abf110 (fit_on=calib, 96 calib docs) before any scores;
  every scores file cites 4abf110, which is an ancestor of the scores commit 54e3512 and older
  than each created_at (checked by script against git).
- Gate 3: reports/report.md has sections 1-9 (headline with bootstrap CIs and exact bound,
  per-question, calibration raw vs calibrated, routing, speed with hardware label and batch-1 vs
  batched, slices, failures, caveats) and the qs_v1 vs qs_v2 table.
- Gate 4: **D-008 flagged for review**: arm A test recall 1.0000, exact 95% lower bound 0.9747,
  gap 0.0253 > 0.01 (144 positives; the bound cannot pass 0.99 at this n even with zero misses).
  B3 and B4 are labelled doc-level/underpowered in the report.
- Findings to carry: the multilingual checkpoint (B1-B4) answers pii_present "yes" to ~98% of
  units with at-or-below-chance ranking; not a harness bug (option-swap probe,
  reports/audits/M6_pii_question_probe-20260929.md). Arm A ranks PII (test AUROC 0.78; calib 0.82) but the
  recall-first t_low (0.0054) forwards only 0.45% of test units. Batch-8 is not faster than
  batch-1 on MPS (A 1.09-1.31x slower, B1 0.93-1.18x).
- Gate 5: `reports/audits/M6_results_review.md`: PASS WITH REQUIRED CAVEATS (integrity: no
  leakage, no test peeking, calib-only fits reproduced, freeze order verified, all 20 headline
  rows match). Required presentation fixes applied in bench/score.py and bench/report.py and the
  report regenerated: key-findings block (degenerate operating point, multilingual no-signal,
  target missed on test for B3/qs_v2 and B4, quasi-only hardest, truncated forwards, qs_v1 vs
  qs_v2 numerics), test headline with exact lo/hi, target check, negatives forwarded,
  discrimination AUROC; holdout in its own descriptive table (D-005); D-008 flag on arm A test
  only; `= raw (T fallback)` marks; length-bucketed latency and outliers; length-controlled drift
  caveat (arm A batch-1 1.48x/1.38x: timing upper bounds, not rerun); failure gallery bolds only
  counted spans. Probe audit corrected (addendum), probe script in scripts/.
- Known gaps: A/B1/B2 batch-1 metas have no `release_every` (runs predate the field: no release);
  B3 released every 25 calls (8e004bb) but its meta predates the field; B4 every call.
- Operational record (all timings kept honest): external memory pressure and a full disk polluted
  A/qs_v2, B2/qs_v2, B3 (x2) and partial B4 runs; each was moved to scratch and redone on a quiet
  machine. A/qs_v1 kept: 3 calls > 2 s of 3603. macOS idle/lid sleep froze runs (perf_counter
  excludes sleep, so recorded latencies were unaffected). laya returned transient NaN on long B4
  and batched B2 calls (clean in isolation); the runner now retries once and marks it.

## Audit fix batch (2026-09-26)

Fixes for `reports/audits/M0-M3-audit-20260926.md` section A, commits 1ff3956..8d6292b:
- A1 calib provenance: CalibParams records input hashes and calib doc ids; score refuses units/docs
  other than the run's, calib fit on other units, and calib/scored doc overlap (except the labeled
  fixture_debug fit). The audit's flipped-gold reproduction now exits 2.
- A2 exact recall bound: Clopper-Pearson lower bound beside the doc bootstrap (fixture: bootstrap
  [1.0, 1.0] vs exact lower 0.6306 on 8 positives); bootstrap CI n/a below 2 documents.
- A3 `t_high` is None when unreachable (1.0 was reachable). A4 degenerate temperatures fall back to
  T = 1 and are reported (fixture arm A: `subject_role:4` fit hit the upper bound 20).
- A5 edge tests kill all 9 mutants that survived the audit (verified on a scratch copy).
- A6 truncated slice uses the runner's measurement; A7 chunk starts word-aligned, whitespace-only
  tails merged (fixture units unchanged). A8 route-level recall in the headline.
- A9 runner: torn final line repaired, atomic meta, meta-less run dirs refused, score rejects rows
  whose mode doesn't match the run, calibrate rejects duplicate unit decisions.
- A10 checkpoints resolve repo + locked revision at load; download_models keeps the lock unless
  --update; units record `english@<revision>`.
- A11 reliability for every question, clean no-scores error, perturbation keys from validator tags,
  multilingual client model test; CLAUDE.md contract table and invariant 2 updated.
- Fixture artifacts regenerated through the stages (pre-audit copies in the session scratchpad):
  model answers byte-identical to the pre-audit run; p50 490 ms/unit.
- `make check` 188 passed, 8 skipped; model tests 8 passed.
- Review of the batch FAILED (`reports/audits/M0-M3-fixbatch-review-20260926-fail.md`): calibrate
  crashed on `t_high: None` (R1), meta-less decisions bypassed provenance (R2), the disjointness
  check would have refused scoring a calib split (R3), torn-line repair dropped a valid last line
  and ran before resume checks (R4), missing HF cache gave a raw error (R5), and six fixes had no
  test that noticed their removal. All fixed; the A4 bound check now compares objective values
  (a flat objective stopped the optimizer at T = 0.06, short of the 0.05 bound). All 12 surviving
  mutants from the review are now killed. `make check` 200 passed; model tests 8 passed.
- Review 2 PASSED (`reports/audits/M0-M3-fixbatch-review-20260926-pass.md`); its four
  non-blocking follow-ups are closed with tests (R4 ordering, `--allow-no-meta` only with a
  fixture_debug calib, flat-objective tolerance, run meta must carry units/docs hashes).
  `make check` 204 passed.
- Fixture commands that use the meta-less mock decisions now also need `--allow-no-meta`
  (`bench calibrate --debug-fit-all --allow-no-meta`, `bench score --allow-debug-calib
  --allow-no-meta`); runs produced by `bench run` have meta.json and don't.

## Questions for the owner (not blocking; candidates for DECISIONS entries)

(CRA role and sponsor-level docs answered: D-017, D-005 amended.)

- Staff initials (fx03) labeled `staff_pii`; domain.md says "name + contact". Confirm for the generator.
- Relative timing ("Day 53", "discharged after nine days") left unlabeled; spec is silent.
- ~~`config/arms.yaml` B2 target 1800 > budget~~: fixed in M5 (1792, audit C5).
- **M6: D-007 recall target and D-008 need an owner review** (M6 results review B1, M1, M7):
  - With under 200 calib positives per arm, the 0.995 target means "no calib misses", so `t_low`
    is the single lowest-scoring calib positive. The resulting operating point forwards 0-2% of
    test units (arm A 0.45%): recall is bought by escalating nearly everything, and no zero-shot
    arm has a useful high-recall forward threshold on this corpus.
  - D-008 is flagged (gate 4): arm A exact lower bound 0.9747 at 144 positives; reaching 0.99 at
    zero misses needs >= 368 positives (~2.5x the test split). A larger corpus fixes the bound, not
    the operating point.
  - Options to weigh: report a recall-vs-forward-rate curve as the headline instead of one point;
    lower the target for zero-shot arms; grow the corpus; or accept that zero-shot Laya is a
    triage aid only and let arm C (M8) carry the operating point.
- **M6: pii_present prompt vs gold construct** (review M6): the prompt names names, contacts,
  MRNs and birth dates; gold also counts quasi-identifiers alone (event dates, initials, ZIP),
  42% of arm A test positives, AUROC 0.71 vs 0.83 for direct. A wording change is a new question
  set (qs_v3) and a rerun, not an M6 edit.

## Later (out of current scope, noted for the owning milestone)

- M5: D-019 needs `.gitignore` to stop ignoring calib/ and scores/ (still ignored).
- M5: stratify the site split on site locale too (language slice), and on doc-type mix.

- Done (audit A9): instead of making `Decision.mode` required (the locked mock decisions lack it),
  `score` rejects any row whose mode doesn't match its run's `meta.json`; meta-less run dirs are
  refused by the runner, and by calibrate/score unless `--allow-no-meta` (fixture debug only).
- Before M6 qs_v2 speed: laya can silently turn MPS autocast off mid-run (fp32, no device change;
  agent.py ~640). Record amp/dtype per decision or abort on change. qs_v1 (4 rows) never uses amp.
- Spec wording: laya-runtime.md says "fall back to cpu and record"; the runner aborts instead
  (stricter). Update the spec or confirm.

- M6: laya enables MPS mixed precision only at >= 5 rows (`mps_amp_min_rows`), so qs_v1 (4 questions)
  runs fp32 and qs_v2 (5 questions) mixed precision. Label this in the speed comparison.
- M6: 500 ms/unit on the dev M2 means full runs take hours; run them in the background.
- M5: `bench run` on the main dataset exits 2 until `bench split` exists.

- M5: `bench split` + split-aware `calibrate`/`score` (calib-only fit, test/holdout scoring); section
  and doc units in `label`. Makefile `calibrate`/`score` targets (`--all`) need that too.
- M6: bootstrap CIs are percentile intervals on document resamples; forward rate and recall only.
- M7: `bench report --hud` currently prints a note and writes nothing.
- Report: reliability table could add a calibrated mean-confidence column; add a test for the
  multi-label line.

- M2/M3: fx06 boundary check assumes raw-text English tokens without special tokens; the M2 segmenter
  must count the same way, or re-tune fx06 (needs an owner OK: fixtures are locked).
- M3: re-run model-marked tests (fx06 boundary, laya result shape) whenever laya or the tokenizer changes.
- `bench build-fixture` writes via Bash, so the Edit/Write lock hook doesn't block it; output is fully
  determined by the locked sources.
- `bench/validate.py` doc_kind_map branch is unreachable (Policy validator guarantees completeness).

- M3: laya 0.3.20 rounds `probabilities` to 4 dp in `_decode_answers`. Invariant 4 stores "raw"
  probabilities; decide whether 4 dp is enough for calibration/ECE or whether to read logits.
- M3: for `choice`, laya's `confidence` is normalized entropy and `answer_confidence` is max(p)
  (the quantity temperature scaling fits). Invariant 6 says gate on `confidence`; confirm which
  one the router gates on before building `score` routing. Store both.
- M3: checkpoint warns `choice:11+` temperature out of range (clamped to 0.5). Irrelevant while
  every question has <= 10 options; keep it that way.
- M6/B4: dev box has 8 GB RAM; 8192-token multilingual runs may be memory-bound on MPS.

## Next action

Owner decisions pending before relying on M6 numbers (see "Questions for the owner"): D-007/D-008
review (degenerate zero-shot operating point; D-008 flagged), and the pii_present prompt vs gold
construct. Neither blocks M7. Next milestone: `/milestone M7` (HUD replay from
`scores/*.routed.jsonl`, audit C7). Long runs: keep the Mac awake and other apps closed.

## Session log

Append one line per session: `YYYY-MM-DD M<n>: what moved, what's blocked`.

- 2026-09-25 M0: hw fingerprint, bench hw, laya_smoke (mps p50 67.8 ms); gate PASS (independent review).
- 2026-09-26 M1: domain, config, validate, schema, 10-doc fixture; gate PASS, gold audit 0 errors; fixtures locked.
- 2026-09-26 M2: label/calibrate/score/report + golden metrics; review #1 FAIL (calibrated tie noise) fixed; review #2 PASS. D-013, D-014 opened.
- 2026-09-26 M3: laya client, runner (resume, warmup, meta), real arm-A fixture run (p50 ~500 ms/unit on mps); review #1 FAIL (batched tail, resume provenance, cpu fallback) fixed; review #2 PASS.
- 2026-09-26 audit: three independent audits of M0-M3; 2 blockers (split design, calib/scores untracked), 2 high code defects (calib provenance, recall CI). M4 on hold pending decisions.
- 2026-09-26 audit fixes A1-A11 applied with tests; fixture artifacts regenerated (answers identical). Review pending.
- 2026-09-26 audit fix batch: review 1 FAIL (R1-R7 + test gaps) fixed; review 2 PASS; follow-ups closed. Ready for M4.
- 2026-09-26 C1 decided as D-019 (calib freeze in git, enforced by score); added to M5 build + gate, M6 gate 2 made checkable.
- 2026-09-27 M4: generator built (4a-4g); make gen 600 docs, V1-V6 pass, deterministic; gold audit + gate review pending.
- 2026-09-27 M4: gold audit runs 1-3 zero label errors; generator realism fixes between runs; final corpus 3507af1f; gate review next.
- 2026-09-27 M4: gate PASS (independent review); spec/DECISIONS/MILESTONES updated for F2-F4; R4 decision pending.
- 2026-09-27 M4: R4 shortcut fixed (D-020), gold audit run 4 zero label errors; corpus 9a88ce5c; ready for M5.
- 2026-09-27 decisions: D-001 no, D-002 M2 on-device (+HF fallback), D-014 top probability, D-008 amended (C3), invariant 6 reworded (C2).
- 2026-09-27 M5: label (all arms) + split built; gates 1-5 evidence recorded; C1 (D-019 freeze) built.
- 2026-09-27 M5: gate reviews #1, #2 FAIL (D-013 guard bypasses, calib freeze gaps) fixed; review #3 PASS. Next: C4-C8, then M6.
- 2026-09-30 M6: 10 zero-shot runs (A, B1-B4 x qs_v1/qs_v2) + batched A/B1; calib frozen 4abf110; scores + report v1; results review and gate PASS. Runner hardened (MPS release, NaN retry, caffeinate). D-008 flagged; D-007 and prompt questions to owner.
