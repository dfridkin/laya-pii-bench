# Spec: metrics and report (`bench/score.py`, `bench/report.py`)

Scoring reads test (and holdout) decisions plus frozen calib params. It refuses to run if the calib
file hash doesn't match its recorded `content_hash`.

## Report sections (all required)

1. **Run context:** arms, question sets, dataset manifest hash, hardware fingerprint, laya version,
   checkpoint revisions, date.
2. **Headline operating point** per arm × qs: at calib-fit `t_low`, test `pii_present` recall
   (point + 95% bootstrap CI), forward rate, false-forward count, precision, and the same on holdout.
3. **Per-question:** accuracy, macro-F1, confusion matrix, majority-class baseline.
4. **Calibration:** ECE (15 bins) and Brier, raw vs calibrated; reliability diagram data; confidence
   AUROC for correctness.
5. **Routing:** counts per route, confusion of route vs gold pii_present, triggers histogram.
6. **Speed:** p50/p95/p99 per unit, units/sec, per-document wall time (sum over its units), batch-1
   vs batched; always labeled with hardware.
7. **Slices:** doc type, length bucket, PII depth, hard negatives, split spans, truncated, language,
   perturbation, value_kind of the missed span (for false forwards).
8. **Failure gallery:** every false forward on test, with unit text, gold spans highlighted in
   markdown, and the probabilities.
9. **Caveats:** sample sizes per slice; any slice with n < 30 marked.

## Bootstrap

Resample **documents**, not units (units within a doc are correlated). 2,000 resamples, seeded.

## Qs_v1 vs qs_v2

Compare `pii_present` identically across both; category evaluation differs (single vs multi-label,
report micro/macro F1 for multi-label).
