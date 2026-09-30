# M6 results review: laya-pii-bench (HEAD 54e3512)

Reviewer: results-analyst subagent, 2026-09-29, read-only. It recomputed all fits and headline
numbers from `runs/*/decisions.jsonl`, `data/units/*.jsonl`, `data/splits.json` and `calib/*.json`
using `bench.calibrate` functions. The builder transcribed this review, because the reviewer has
no write tool.

## Verdict: PASS WITH REQUIRED CAVEATS (one-line: NEEDS WORK)

**Integrity: PASS.** No leakage, no test peeking, and every headline number reproduces exactly.

**Presentation: must change before sharing.** The report is purely tables. Every headline row
shows recall of 0.925–1.000, and nothing tells a reader that:

- this recall comes from escalating almost everything, and
- the multilingual checkpoint ranks worse than chance.

A reader of `reports/report.md` alone would get the main result backwards. The required caveats
(B1, B2 and the majors) must be added through `bench/report.py`, not by hand-editing, and the
report regenerated.

## What checks out

- **Leakage: none.**
  - No site or subject crosses train/calib/test.
  - No high-identifying span value appears in two core splits.
  - The only exception is the first name "Laura" in train d0324 and test d0008/d0489. These are
    "Hi Laura" greetings at different sites (1003 vs 2002), a Faker first-name collision.
  - 15 holdout staff values also occur in other splits. This is expected under D-018 and only
    matters for arm C.
- **Calib fit on calib only.** For all 10 files:
  - `calib_doc_ids` equals the 96 calib-split docs exactly;
  - `t_low` recomputes from calib positives to 4 dp;
  - `content_hash`, `decisions_sha256` and `units_sha256` all match.
- **Freeze order (D-019).**
  - All 10 calib files were added in 4abf110 (2026-09-29 23:34:52Z) and are unchanged at HEAD.
  - Every scores file cites 4abf110 and was created at 03:07Z on 09-30. The scores commit 54e3512
    is a descendant.
  - All batch-1 runs ended before the freeze (the last at 23:30Z). Batched runs came after it but
    are speed-only.
- **Coverage.** `coverage_units == coverage_decided` in all 20 cells. There are 0 NaN
  probabilities and 0 `retried` decisions in any run.
- **Report matches scores JSON.** All 20 headline rows agree with `scores/*.json` (0 mismatches).
- **The recall-first threshold works as coded.** `fit_t_low` returns
  `sorted(p_pos)[floor(0.005·n_pos)]`. With at most 111 calib positives, this is the lowest calib
  positive.

## BLOCKER (for sharing)

### B1. The headline operating point is degenerate, and the report does not say so

- Test forward rates at the calib-fit `t_low`:

  | arm / qs | test forward rate |
  |---|---|
  | A (both qs) | 0.0045 (9 of 2006 units) |
  | B1 / qs_v1 | 0.0015 |
  | B1 / qs_v2 | 0 |
  | B2 | 0.009–0.019 |
  | B3 / B4 | 0.016–0.057 |

- Holdout forward rate is 0 for every arm, so holdout recall is vacuous.
- Arm A test escalates 1853 of 2006 units. "Escalate everything" scores recall 1.0 with forward
  rate 0, and every arm sits within noise of that trivial policy.
- The `precision` column is prevalence among non-forwarded units.
- A calib-only sweep for arm A shows no useful high-recall point:

  | calib recall target | calib forward rate |
  |---|---|
  | 0.995 | 0.001 |
  | 0.99 | 0.003 |
  | 0.98 | 0.015 |
  | 0.95 | 0.062 |
  | 0.90 | 0.315 |

- Fix: add an escalate-all baseline, specificity, and a caveat. Suggested wording: "Zero-shot Laya
  does not offer a useful high-recall forward threshold on this corpus."

### B2. The multilingual finding is missing from the report, and its calibration numbers mislead

- Discrimination AUROC of raw p(pii_present = A):

  | arm | calib | test | holdout |
  |---|---|---|---|
  | B1 | 0.366 | 0.379 | 0.293 |
  | B2 | 0.467 | 0.449 | 0.397 |
  | B3 | ~0.50 | 0.48–0.49 | — |
  | B4 | 0.54–0.56 | 0.46–0.47 | — |
  | A | 0.818 | 0.778 | 0.576 |

- B1 answers A for 97–99% of units. Mean p(A) is 0.84 for positives and 0.90 for negatives.
- The pii_present temperature fits for B1–B3 hit the bound (20), so T fell back to 1 and
  "ECE cal" equals raw. The fallback is shown only in the run-context row.
- Fix: add a findings paragraph linking the probe audit, report discrimination AUROC, and mark
  calibrated columns as raw when a fallback applied.

## MAJOR

### M1. `t_low` rests on a single unit, whose fp16/fp32 noise drives the qs_v1 vs qs_v2 differences

- In B3, unit d0124:section:4096:0 scores 0.1907 (fp32) vs 0.5142 (fp16). That one unit moves
  `t_low` and takes test false forwards from 2 to 6.
- pii_present has the same text in both sets, yet per-unit |Δp| between qs_v1 and qs_v2 reaches:

  | arm | max |Δp| |
  |---|---|
  | A | 0.02 |
  | B1 | 0.07 |
  | B2 | 0.11 |
  | B4 | 0.35 |
  | B3 | 0.48 |

- qs_v2 has no role rule, so its routing is threshold-only.
- Fix: caveat the comparison table. With fewer than 200 calib positives, the 0.995 target means
  zero calib misses; consider recording this in D-007.

### M2. Test recall is below the calib target for B3/B4 qs_v2

| arm / qs | test recall | Clopper-Pearson 95% upper |
|---|---|---|
| B3 / qs_v2 | 79/85 = 0.929 | 0.974 |
| B4 / qs_v2 | 74/80 = 0.925 | 0.972 |
| B4 / qs_v1 | 77/80 | 0.992 |

All three upper bounds are below 0.995. Fix: add a "target met?" column and a caveat.

### M3. Arm A batch-1 latency drifts within the run (MPS cache growth before 8e004bb)

- Median latency for fixed-length arm A units, first eighth vs last eighth of each run:

  | run | first eighth | last eighth | change |
  |---|---|---|---|
  | A/qs_v1 batch-1 | 616 ms | 905 ms | +47% |
  | A/qs_v2 batch-1 | 717 ms | 987 ms | +38% |
  | batched runs | — | — | flat |

- The batched comparison is therefore confounded.
- Fix: rerun for timing, or caveat A batch-1 as an upper bound. Record `release_every` in meta
  for every run.

### M4. The B4 "outlier" caveat blames the wrong cause

- Every flagged call is a document of at least 6,297 tokens. Token count and latency correlate at
  0.94–0.96, so this is length scaling, not interference.
- Fix: bucket the outlier test by length, report latency by length bucket, and drop the
  "swapping?" wording.

### M5. The holdout sits in the headline table, and the D-008 flag is applied beyond arm A

- D-005 says the holdout is descriptive only, never in the headline.
- Holdout forward rate is 0, and it has 30 docs and 20 positives, all IRB letters.
- M4 limitation S1 (the IRB alt-text line) may act as a shortcut cue.
- Arm A holdout discrimination is 0.576.
- The D-008 trigger applies to arm A test only.
- Fix: give the holdout its own descriptive table, flag D-008 on arm A test only, and add the
  holdout caveats.

### M6. The question wording and the gold construct differ

- The prompt's examples omit dates and initials, but gold counts phi_quasi alone.
- 42% of arm A test positives are quasi-only.
- Arm A AUROC by positive type: quasi-only 0.706, staff 0.828, direct 0.834.
- 9 of the 20 false forwards are quasi-only CRF pages.
- Fix: caveat and a breakdown by positive type. A wording change needs a DECISIONS entry and a
  rerun.

### M7. Gate evidence is uncommitted, and the probe audit overstates its result

- STATUS is uncommitted.
- The probe's AUROC 0.87 comes from n=40. The full calib AUROC is 0.82 and test is 0.78, and
  "t_low handles it" is contradicted by B1.
- The probe script is not in the repo.
- D-008: at zero misses the lower bound reaches 0.99 only with at least 368 positives, about 2.5x
  arm A's test positives.

## MINOR

- m1. Rename and explain the precision column.
- m2. Zero-miss CIs print as "[1.0000, 1.0000]".
- m3. B2–B4 batched rows need a "not run" reason.
- m4. Batched latency is amortized per unit; label it so.
- m5. Per-unit latency is not comparable across arms; point to the per-document row, whose
  n=250 includes calib docs.
- m6. Truncated units can be forwarded: B2 test forwarded 1–2 of 6, all gold negatives.
- m7. The failure gallery bolds coded subject ids, which are not PII under D-001.
- m8. Arm A accuracy is 0.936 against a majority baseline of 0.928, with macro-F1 0.62.
- m9. Short docs give identical units across B2–B4. d0352 accounts for 6 of the 20 false forwards.
- m10. `release_every` is missing from the A/B1/B2/B3 run metas.

## False forwards (all 20 read)

There are 8 distinct documents.

| cause group | count |
|---|---|
| Non-English docs with direct patient PII (d0352 es SAE, 6; d0447 de narrative, 3; d0447 is the worst miss) | 9 |
| Quasi-only CRF pages (d0418, d0062, d0150, d0082) | 8 |
| de correspondence (d0377) | 2 |
| Staff contact in a long monitoring report (d0310) | 1 |

- Language: 11 of 20 are non-English, while non-English docs are 17 of 124 test docs.
- None are truncated, and none come from pii_depth docs.

## Required before M6 closes

1. Update `bench/report.py` and regenerate the report to add:
   - findings and caveats;
   - discrimination AUROC;
   - the escalate-all baseline and specificity;
   - the holdout in its own table;
   - the D-008 flag on arm A test only;
   - latency bucketed by length.
2. Caveat or rerun arm A batch-1 timing.
3. Commit STATUS, correct the probe audit, and add its script to `scripts/`.
4. Owner: flag D-007 and D-008 for review.
