# Addendum to M6_pii_question_probe-20260929.md (results review M7)

Corrections, per `M6_results_review.md` M7:

- Arm A AUROC 0.87-0.90 in the probe is from n = 40 balanced calib units. Over the full calib split
  it is 0.82 and on test 0.78 (scores/A__qs_v1.json `auroc_pii`).
- "the calib-fit t_low handles it" was wrong: t_low is the lowest calib positive, and arm A then
  forwards only 0.45% of test units (report section 2, key findings). The low p(yes) scale is
  absorbed by the threshold, but no useful high-recall forward threshold exists.
- The probe script is now `scripts/pii_question_probe.py` (seed 0, same sampling), so the audit
  can be reproduced.
