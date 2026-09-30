# M6 diagnostic: pii_present wording and option order (calib split only)

Why: after calibration, the multilingual arms (B1-B4) predicted "A" (PII present) for ~98% of calib
units with mean p(A) ~0.85 for both gold classes, and their pii_present temperature fits hit the
bound (T -> fallback 1). Question: a pipeline bug (key mapping, prompt) or the checkpoint?

Probe (`scratchpad/qprobe.py`): 40 calib-split units per arm (20 gold yes, 20 gold no, seed 0),
pii_present alone, three variants: original wording; options swapped (A = no, B = yes); "real"
removed from "a real individual". Test split untouched.

| arm (checkpoint) | variant | AUROC p(yes) | share picking A | mean p(yes) gold yes / no |
|---|---|---|---|---|
| A (english) | original | 0.873 | 0.10 | 0.349 / 0.147 |
| A (english) | swapped | 0.895 | 0.93 | 0.309 / 0.121 |
| A (english) | no "real" | 0.878 | 0.07 | 0.368 / 0.150 |
| B1 (multilingual) | original | 0.283 | 0.97 | 0.828 / 0.920 |
| B1 (multilingual) | swapped | 0.468 | 0.05 | 0.773 / 0.833 |
| B1 (multilingual) | no "real" | 0.270 | 0.97 | 0.812 / 0.919 |

Findings:
- Not a pipeline bug: both checkpoints follow option meaning, not position (swapping flips the
  share picking A), so key mapping and prompt assembly are correct.
- English: strong ranking signal (AUROC ~0.88) with a low p(yes) scale; the calib-fit t_low handles
  it. "real individual" (fictional world, invariant 10) does not change it.
- Multilingual: answers "yes" to nearly everything and ranks at or below chance on this data
  (n=40, noisy). This is a model finding for the report, not something to fix in the benchmark.
- No question-set change: qs_v1/qs_v2 stay as decided.
