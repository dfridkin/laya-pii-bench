# laya-pii-bench report

> **DEBUG REPORT.** Calibration was not fit on a calib split (fit_on = fixture_debug). Numbers are in-sample pipeline checks, not benchmark results.

## 1. Run context

### mock / qs_v1

| field | value |
|---|---|
| arm | mock |
| question set | qs_v1 |
| splits | fixture |
| docs sha256 | `427b466abb995d4d7566741e2eca660e61726727e652e74319f6381ad52acd27` |
| units sha256 | `11a4901b0d0b5da77f3e23857eaea26d4f8d40468e227694700334e2b92988a9` |
| decisions sha256 | `0af837472a733cd02faae60c09b4573cc761b6575855262c60617df8a375ed5c` |
| calib hash / fit_on | `18402b8afa93edf8` / fixture_debug |
| calib commit (D-019) | `3b26c12fc123` 2026-09-27T22:16:16-04:00 |
| temperature fallbacks (T = 1) | doc_kind:4: calib accuracy 1.0 |
| hardware | not recorded |
| laya version | unknown |
| checkpoints | english |
| checkpoint revisions | MOCK |
| date | 2026-09-28T02:16:30+00:00 |

## 2. Headline operating point

pii_present recall at the calib-fit `t_low` (95% document-level bootstrap CI). The exact lower bound is Clopper-Pearson on unit counts (ignores clustering within documents; informative when there are no misses). Route recall counts misses after routing (1 - false forwards / positives). t_high `none`: no threshold reached the precision target, so only the role rule redacts.

| arm / qs | split | t_low | t_high | recall | recall exact lo | route recall | forward rate | false forwards | precision | units / docs / positives |
|---|---|---|---|---|---|---|---|---|---|---|
| mock / qs_v1 | fixture | 0.1404 | 0.6614 | 1.0000 [1.0000, 1.0000] | 0.5904 | 1.0000 | 0.0909 [0.0000, 0.3000] | 0 | 0.7000 | 11 / 10 / 7 |

## 3. Per-question

### mock / qs_v1, fixture

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 11 | 0.8182 | 0.8036 | 0.6364 (A) |
| subject_role | 11 | 0.7273 | 0.7143 | 0.3636 (none) |
| category | 11 | 0.7273 | 0.5778 | 0.4545 (direct) |
| doc_kind | 11 | 1.0000 | 1.0000 | 0.3636 (form_table) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 6 | 1 |
| B | 1 | 3 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 1 | 1 | 0 | 0 |
| staff | 0 | 2 | 0 | 0 |
| both | 1 | 0 | 2 | 0 |
| none | 1 | 0 | 0 | 3 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 4 | 0 | 0 | 0 | 1 |
| quasi | 0 | 0 | 0 | 0 | 0 |
| coded | 0 | 0 | 1 | 1 | 0 |
| staff | 0 | 0 | 0 | 1 | 0 |
| none | 0 | 1 | 0 | 0 | 2 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 4 | 0 | 0 | 0 |
| form_table | 0 | 4 | 0 | 0 |
| correspondence | 0 | 0 | 1 | 0 |
| protocol_text | 0 | 0 | 0 | 2 |

## 4. Calibration

ECE uses 15 equal-width bins on the max probability. Brier is multi-class. AUROC scores correctness by the max probability.

### mock / qs_v1, fixture

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.2927 | 0.2585 | 0.2651 | 0.2592 | 0.7778 | 0.7778 |
| subject_role | 0.0273 | 0.0000 | 0.4473 | 0.4463 | 0.5000 | 0.5000 |
| category | 0.1273 | 0.0000 | 0.4727 | 0.4525 | 0.5000 | 0.5000 |
| doc_kind | 0.1500 | 0.1500 | 0.0300 | 0.0300 | n/a | n/a |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.533, 0.600) | 1 | 0.5600 | 0.0000 | 1 | 0.5817 | 0.0000 |
| [0.600, 0.667) | 2 | 0.6200 | 1.0000 | 2 | 0.6614 | 1.0000 |
| [0.667, 0.733) | 2 | 0.7150 | 1.0000 | 0 | n/a | n/a |
| [0.733, 0.800) | 1 | 0.7900 | 0.0000 | 2 | 0.7786 | 1.0000 |
| [0.800, 0.867) | 1 | 0.8300 | 1.0000 | 1 | 0.8596 | 0.0000 |
| [0.867, 0.933) | 3 | 0.8867 | 1.0000 | 2 | 0.9141 | 1.0000 |
| [0.933, 1.000) | 1 | 0.9700 | 1.0000 | 3 | 0.9631 | 1.0000 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.667, 0.733) | 11 | 0.7000 | 0.7273 | 11 | 0.7273 | 0.7273 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.600, 0.667) | 11 | 0.6000 | 0.7273 | 0 | n/a | n/a |
| [0.667, 0.733) | 0 | n/a | n/a | 11 | 0.7273 | 0.7273 |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.800, 0.867) | 11 | 0.8500 | 1.0000 | 11 | 0.8500 | 1.0000 |

## 5. Routing

### mock / qs_v1, fixture

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 6 | 1 | 7 |
| B | 1 | 1 | 2 | 4 |
| all | 1 | 7 | 3 | 11 |

| trigger | count |
|---|---|
| p_at_or_above_t_high | 6 |
| p_below_t_low | 1 |
| p_in_escalate_band | 3 |
| role_both | 2 |
| role_patient | 3 |

## 6. Speed

### mock / qs_v1

Hardware: **unknown hardware (no hw.json)**. Warmup calls excluded: 2.

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 11 | 60.2 | 67.5 | 69.8 | 61.2 | 16.34 |
| per unit, batched | 0 | n/a | n/a | n/a | n/a | n/a |
| per document (sum of units, batch-1) | 10 | 60.0 | 102.5 | 128.6 | 67.3 | 14.85 |

## 7. Slices

Slices with n < 30 are marked `*`.

### mock / qs_v1, fixture

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | crf_page * | 1 | 1 | 0 | n/a | 0.0000 | 0 | 1.0000 |
| doc_type | csr_patient_narrative * | 2 | 2 | 2 | 1.0000 | 0.0000 | 0 | 1.0000 |
| doc_type | delegation_log * | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 1.0000 |
| doc_type | lab_report * | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 1.0000 |
| doc_type | monitoring_visit_report * | 2 | 1 | 2 | 1.0000 | 0.0000 | 0 | 0.5000 |
| doc_type | protocol_section * | 2 | 2 | 0 | n/a | 0.5000 | 0 | 1.0000 |
| doc_type | sae_cioms * | 1 | 1 | 0 | n/a | 0.0000 | 0 | 0.0000 |
| doc_type | site_correspondence * | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 1.0000 |
| hard_negative | no * | 9 | 8 | 7 | 1.0000 | 0.1111 | 0 | 0.8889 |
| hard_negative | yes * | 2 | 2 | 0 | n/a | 0.0000 | 0 | 0.5000 |
| lang | de * | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 1.0000 |
| lang | en * | 10 | 9 | 6 | 1.0000 | 0.1000 | 0 | 0.8000 |
| length_bucket | short * | 11 | 10 | 7 | 1.0000 | 0.0909 | 0 | 0.8182 |
| perturbation | email_quoting * | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 1.0000 |
| perturbation | none * | 7 | 6 | 4 | 1.0000 | 0.1429 | 0 | 0.7143 |
| perturbation | ocr_noise * | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 1.0000 |
| perturbation | table * | 2 | 2 | 1 | 1.0000 | 0.0000 | 0 | 1.0000 |
| pii_depth | none * | 11 | 10 | 7 | 1.0000 | 0.0909 | 0 | 0.8182 |
| pre_redacted | no * | 10 | 9 | 7 | 1.0000 | 0.1000 | 0 | 0.9000 |
| pre_redacted | yes * | 1 | 1 | 0 | n/a | 0.0000 | 0 | 0.0000 |
| split_span | no * | 10 | 10 | 6 | 1.0000 | 0.1000 | 0 | 0.8000 |
| split_span | yes * | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 1.0000 |
| truncated | no * | 11 | 10 | 7 | 1.0000 | 0.0909 | 0 | 0.8182 |

Value kinds of missed spans (false forwards):

none

## 8. Failure gallery

### mock / qs_v1, fixture: 0 false forward(s)

## 9. Caveats

- mock / qs_v1: Decisions have no run meta.json (--allow-no-meta): units/docs were not checked against the run that produced them.
- mock / qs_v1: Calibration fit_on=fixture_debug: temperatures and thresholds were fit on the scored units themselves. Calibrated metrics and routing are in-sample; this is a pipeline check, not a benchmark result.
- mock / qs_v1: No holdout split was scored.
- mock / qs_v1: fixture: slices with n < 30: doc_type=crf_page (n=1), doc_type=csr_patient_narrative (n=2), doc_type=delegation_log (n=1), doc_type=lab_report (n=1), doc_type=monitoring_visit_report (n=2), doc_type=protocol_section (n=2), doc_type=sae_cioms (n=1), doc_type=site_correspondence (n=1), hard_negative=no (n=9), hard_negative=yes (n=2), lang=de (n=1), lang=en (n=10), length_bucket=short (n=11), perturbation=email_quoting (n=1), perturbation=none (n=7), perturbation=ocr_noise (n=1), perturbation=table (n=2), pii_depth=none (n=11), pre_redacted=no (n=10), pre_redacted=yes (n=1), split_span=no (n=10), split_span=yes (n=1), truncated=no (n=11)
