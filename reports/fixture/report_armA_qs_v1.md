# laya-pii-bench report

> **DEBUG REPORT.** Calibration was not fit on a calib split (fit_on = fixture_debug). Numbers are in-sample pipeline checks, not benchmark results.

## 1. Run context

### A / qs_v1

| field | value |
|---|---|
| arm | A |
| question set | qs_v1 |
| splits | fixture |
| docs sha256 | `427b466abb995d4d7566741e2eca660e61726727e652e74319f6381ad52acd27` |
| units sha256 | `11a4901b0d0b5da77f3e23857eaea26d4f8d40468e227694700334e2b92988a9` |
| decisions sha256 | `cf2e9c9aff43224ae2aa527c3d1d4a0ff2cfc771216dc04d14276615a40b4562` |
| calib hash / fit_on | `0f68f19efeb046d1` / fixture_debug |
| calib commit (D-019) | `cceb8775ce2c` 2026-09-27T22:16:36-04:00 |
| temperature fallbacks (T = 1) | pii_present:2: fit hit bound (20); subject_role:4: fit hit bound (20) |
| hardware | Apple M2, 8.0 GB, mps, Darwin 24.3.0 |
| laya version | 0.3.20 |
| checkpoints | english |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-09-28T02:16:36+00:00 |

## 2. Headline operating point

### Key findings


### Test (headline)

pii_present recall at the calib-fit `t_low` (95% document-level bootstrap CI). Exact lo / hi are Clopper-Pearson on unit counts (ignore clustering within documents); the recall target is `missed` when the exact upper bound is below it. `point - exact lo` above 0.01 flags D-008 for review on arm A only (D-008 amended). Negatives forwarded = forwarded PII-free units / PII-free units (the work saved). Route recall counts misses after routing (1 - false forwards / positives). t_high `none`: no threshold reached the precision target, so only the role rule redacts. Doc-level arms are underpowered (few units per document).

| arm / qs | t_low | t_high | recall | exact lo / hi | recall target | point - exact lo | route recall | forward rate | negatives forwarded | false forwards | AUROC p(pii) | PII share at p >= t_low | units / docs / positives |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|


### Holdout (descriptive only, D-005)

All IRB letters (one document type, 30 documents, few positives), never part of the headline. With a forward rate of 0, recall here is vacuous. Known limitation (M4 S1): a fixed alt-text contact line appears only in PII-free letters, a possible shortcut cue.

| arm / qs | t_low | t_high | recall | exact lo / hi | recall target | point - exact lo | route recall | forward rate | negatives forwarded | false forwards | AUROC p(pii) | PII share at p >= t_low | units / docs / positives |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## 3. Per-question

### A / qs_v1, fixture

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 11 | 0.4545 | 0.4500 | 0.6364 (A) |
| subject_role | 11 | 0.2727 | 0.2667 | 0.3636 (none) |
| category | 11 | 0.4545 | 0.5000 | 0.4545 (direct) |
| doc_kind | 11 | 0.5455 | 0.4970 | 0.3636 (form_table) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 2 | 5 |
| B | 1 | 3 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 0 | 0 | 0 | 2 |
| staff | 0 | 1 | 0 | 1 |
| both | 2 | 0 | 0 | 1 |
| none | 2 | 0 | 0 | 2 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 0 | 0 | 2 | 0 | 3 |
| quasi | 0 | 0 | 0 | 0 | 0 |
| coded | 0 | 0 | 1 | 0 | 1 |
| staff | 0 | 0 | 0 | 1 | 0 |
| none | 0 | 0 | 0 | 0 | 3 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 3 | 0 | 0 | 1 |
| form_table | 1 | 0 | 1 | 2 |
| correspondence | 0 | 0 | 1 | 0 |
| protocol_text | 0 | 0 | 0 | 2 |

## 4. Calibration

ECE uses 15 equal-width bins on the max probability. Brier is multi-class. AUROC scores correctness by the max probability (for pii_present discrimination see section 2). `= raw (T fallback)`: the temperature fit hit its bound, so T = 1 and the calibrated columns equal raw; calibration did nothing there.

### A / qs_v1, fixture

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.3499 | 0.3499 | 0.6963 | 0.6963 | 0.6333 | 0.6333 |
| subject_role = raw (T fallback) | 0.4157 | 0.4157 | 1.0079 | 1.0079 | 0.4167 | 0.4167 |
| category | 0.2764 | 0.1339 | 0.7743 | 0.7645 | 0.5000 | 0.5333 |
| doc_kind | 0.2689 | 0.2593 | 0.4425 | 0.4419 | 1.0000 | 1.0000 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.600, 0.667) | 1 | 0.6230 | 0.0000 | 1 | 0.6230 | 0.0000 |
| [0.667, 0.733) | 2 | 0.6773 | 0.5000 | 2 | 0.6773 | 0.5000 |
| [0.733, 0.800) | 3 | 0.7750 | 0.6667 | 3 | 0.7750 | 0.6667 |
| [0.800, 0.867) | 4 | 0.8542 | 0.2500 | 4 | 0.8542 | 0.2500 |
| [0.867, 0.933) | 1 | 0.8707 | 1.0000 | 1 | 0.8707 | 1.0000 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.400, 0.467) | 3 | 0.4504 | 0.3333 | 3 | 0.4504 | 0.3333 |
| [0.467, 0.533) | 1 | 0.4759 | 0.0000 | 1 | 0.4759 | 0.0000 |
| [0.533, 0.600) | 1 | 0.5810 | 0.0000 | 1 | 0.5810 | 0.0000 |
| [0.600, 0.667) | 2 | 0.6163 | 0.5000 | 2 | 0.6163 | 0.5000 |
| [0.667, 0.733) | 1 | 0.6815 | 1.0000 | 1 | 0.6815 | 1.0000 |
| [0.733, 0.800) | 1 | 0.7689 | 0.0000 | 1 | 0.7689 | 0.0000 |
| [0.867, 0.933) | 1 | 0.9055 | 0.0000 | 1 | 0.9054 | 0.0000 |
| [0.933, 1.000) | 1 | 0.9389 | 0.0000 | 1 | 0.9389 | 0.0000 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 0 | n/a | n/a | 2 | 0.2549 | 0.5000 |
| [0.267, 0.333) | 2 | 0.3099 | 0.5000 | 4 | 0.2961 | 0.5000 |
| [0.333, 0.400) | 1 | 0.3409 | 0.0000 | 3 | 0.3443 | 0.3333 |
| [0.400, 0.467) | 3 | 0.4313 | 0.6667 | 2 | 0.4330 | 0.5000 |
| [0.467, 0.533) | 3 | 0.5087 | 0.3333 | 0 | n/a | n/a |
| [0.600, 0.667) | 1 | 0.6513 | 1.0000 | 0 | n/a | n/a |
| [0.733, 0.800) | 1 | 0.7389 | 0.0000 | 0 | n/a | n/a |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 1 | 0.3319 | 0.0000 | 0 | n/a | n/a |
| [0.333, 0.400) | 3 | 0.3483 | 0.0000 | 4 | 0.3560 | 0.0000 |
| [0.467, 0.533) | 1 | 0.5099 | 0.0000 | 0 | n/a | n/a |
| [0.533, 0.600) | 1 | 0.5854 | 1.0000 | 1 | 0.5362 | 0.0000 |
| [0.600, 0.667) | 0 | n/a | n/a | 1 | 0.6256 | 1.0000 |
| [0.667, 0.733) | 1 | 0.7078 | 1.0000 | 0 | n/a | n/a |
| [0.733, 0.800) | 1 | 0.7573 | 1.0000 | 1 | 0.7548 | 1.0000 |
| [0.800, 0.867) | 0 | n/a | n/a | 1 | 0.8017 | 1.0000 |
| [0.933, 1.000) | 3 | 0.9596 | 1.0000 | 3 | 0.9751 | 1.0000 |

## 5. Routing

### A / qs_v1, fixture

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 3 | 4 | 7 |
| B | 1 | 2 | 1 | 4 |
| all | 1 | 5 | 5 | 11 |

| trigger | count |
|---|---|
| p_at_or_above_t_high | 2 |
| p_below_t_low | 1 |
| p_in_escalate_band | 5 |
| role_patient | 4 |

## 6. Speed

Per-unit latency is not comparable across arms (units range from 256-token chunks to whole documents); compare the per-document row or the length rows. Batched runs were made for arms A and B1 only: batches of eight 2k-8k-token states exceed the 8 GB M2 (swapping, NaN).

### A / qs_v1

Hardware: **Apple M2, 8.0 GB RAM, device mps (Apple MPS), torch 2.14.0**. Warmup calls excluded: 10. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: n/a. laya autocast: batch-1 unknown, batched unknown (on MPS, fp16 autocast starts at 5 question rows, so qs_v2 runs fp16 and qs_v1 fp32).

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 11 | 494.8 | 577.4 | 619.6 | 476.8 | 2.10 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 10 | 497.4 | 804.2 | 987.1 | 524.4 | 1.91 |

## 7. Slices

Slices with n < 30 are marked `*`.

### A / qs_v1, fixture

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | crf_page * | 1 | 1 | 0 | n/a | 0.0000 | 0 | 1.0000 |
| doc_type | csr_patient_narrative * | 2 | 2 | 2 | 1.0000 | 0.0000 | 0 | 0.5000 |
| doc_type | delegation_log * | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 1.0000 |
| doc_type | lab_report * | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 0.0000 |
| doc_type | monitoring_visit_report * | 2 | 1 | 2 | 1.0000 | 0.0000 | 0 | 0.0000 |
| doc_type | protocol_section * | 2 | 2 | 0 | n/a | 0.5000 | 0 | 1.0000 |
| doc_type | sae_cioms * | 1 | 1 | 0 | n/a | 0.0000 | 0 | 0.0000 |
| doc_type | site_correspondence * | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 0.0000 |
| hard_negative | no * | 9 | 8 | 7 | 1.0000 | 0.0000 | 0 | 0.4444 |
| hard_negative | yes * | 2 | 2 | 0 | n/a | 0.5000 | 0 | 0.5000 |
| lang | de * | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 0.0000 |
| lang | en * | 10 | 9 | 6 | 1.0000 | 0.1000 | 0 | 0.5000 |
| length_bucket | short * | 11 | 10 | 7 | 1.0000 | 0.0909 | 0 | 0.4545 |
| perturbation | email_quoting * | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 0.0000 |
| perturbation | none * | 7 | 6 | 4 | 1.0000 | 0.1429 | 0 | 0.4286 |
| perturbation | ocr_noise * | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 0.0000 |
| perturbation | table * | 2 | 2 | 1 | 1.0000 | 0.0000 | 0 | 1.0000 |
| pii_depth | none * | 11 | 10 | 7 | 1.0000 | 0.0909 | 0 | 0.4545 |
| pre_redacted | no * | 10 | 9 | 7 | 1.0000 | 0.1000 | 0 | 0.5000 |
| pre_redacted | yes * | 1 | 1 | 0 | n/a | 0.0000 | 0 | 0.0000 |
| split_span | no * | 10 | 10 | 6 | 1.0000 | 0.1000 | 0 | 0.5000 |
| split_span | yes * | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 0.0000 |
| truncated | no * | 11 | 10 | 7 | 1.0000 | 0.0909 | 0 | 0.4545 |

Value kinds of missed spans (false forwards):

none

## 8. Failure gallery

### A / qs_v1, fixture: 0 false forward(s)

## 9. Caveats

- A / qs_v1: Calibration fit_on=fixture_debug: temperatures and thresholds were fit on the scored units themselves. Calibrated metrics and routing are in-sample; this is a pipeline check, not a benchmark result.
- A / qs_v1: No holdout split was scored.
- A / qs_v1: fixture: slices with n < 30: doc_type=crf_page (n=1), doc_type=csr_patient_narrative (n=2), doc_type=delegation_log (n=1), doc_type=lab_report (n=1), doc_type=monitoring_visit_report (n=2), doc_type=protocol_section (n=2), doc_type=sae_cioms (n=1), doc_type=site_correspondence (n=1), hard_negative=no (n=9), hard_negative=yes (n=2), lang=de (n=1), lang=en (n=10), length_bucket=short (n=11), perturbation=email_quoting (n=1), perturbation=none (n=7), perturbation=ocr_noise (n=1), perturbation=table (n=2), pii_depth=none (n=11), pre_redacted=no (n=10), pre_redacted=yes (n=1), split_span=no (n=10), split_span=yes (n=1), truncated=no (n=11)
