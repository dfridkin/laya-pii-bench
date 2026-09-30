# laya-pii-bench report

## 1. Run context

### A / qs_v1

| field | value |
|---|---|
| arm | A |
| question set | qs_v1 |
| splits | test, holdout |
| docs sha256 | `9a88ce5c4c5b4a8559ef9b624d720dd823dd4fb0fdbf68115fae84b6894fada5` |
| units sha256 | `62022ad2270a5f851f33eb910db19d6ca12afcf49be081c87ae1a189de297dde` |
| decisions sha256 | `61bc7991d612ce16006e0ace25314cd5bdbe434607bef55f9dc2c178b5f76d54` |
| calib hash / fit_on | `41df97bee458c285` / calib |
| calib commit (D-019) | `4abf11083d37` 2026-09-29T19:34:52-04:00 |
| temperature fallbacks (T = 1) | doc_kind:4: fit hit bound (20) |
| hardware | Apple M2, 8.0 GB, mps, Darwin 24.3.0 |
| laya version | 0.3.20 |
| checkpoints | english |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-09-30T03:25:12.301632+00:00 |

### A / qs_v2

| field | value |
|---|---|
| arm | A |
| question set | qs_v2 |
| splits | test, holdout |
| docs sha256 | `9a88ce5c4c5b4a8559ef9b624d720dd823dd4fb0fdbf68115fae84b6894fada5` |
| units sha256 | `62022ad2270a5f851f33eb910db19d6ca12afcf49be081c87ae1a189de297dde` |
| decisions sha256 | `d3fa9d456b47ffbe4a50de9b13be8ba48977b96879d1663b5cfe6e501292e6bc` |
| calib hash / fit_on | `cbcf796e5c2f1499` / calib |
| calib commit (D-019) | `4abf11083d37` 2026-09-29T19:34:52-04:00 |
| temperature fallbacks (T = 1) | has_staff_pii:2: fit hit bound (20) |
| hardware | Apple M2, 8.0 GB, mps, Darwin 24.3.0 |
| laya version | 0.3.20 |
| checkpoints | english |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-09-30T03:25:14.542878+00:00 |

### B1 / qs_v1

| field | value |
|---|---|
| arm | B1 |
| question set | qs_v1 |
| splits | test, holdout |
| docs sha256 | `9a88ce5c4c5b4a8559ef9b624d720dd823dd4fb0fdbf68115fae84b6894fada5` |
| units sha256 | `1e606484ae378207a173fb91a613195f4427e3bfb27c73d21d2cb87bae98e071` |
| decisions sha256 | `41138b416d668da920d19684790912d2704d9d0a463a3b6b2faab9fee9410094` |
| calib hash / fit_on | `52d77b199379560b` / calib |
| calib commit (D-019) | `4abf11083d37` 2026-09-29T19:34:52-04:00 |
| temperature fallbacks (T = 1) | doc_kind:4: fit hit bound (20); pii_present:2: fit hit bound (20); subject_role:4: fit hit bound (20) |
| hardware | Apple M2, 8.0 GB, mps, Darwin 24.3.0 |
| laya version | 0.3.20 |
| checkpoints | multilingual |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-09-30T03:25:15.849134+00:00 |

### B1 / qs_v2

| field | value |
|---|---|
| arm | B1 |
| question set | qs_v2 |
| splits | test, holdout |
| docs sha256 | `9a88ce5c4c5b4a8559ef9b624d720dd823dd4fb0fdbf68115fae84b6894fada5` |
| units sha256 | `1e606484ae378207a173fb91a613195f4427e3bfb27c73d21d2cb87bae98e071` |
| decisions sha256 | `c24e2ddb84b1a182737884bcdb5598715ff0d812cd29feffb401db28baf2fa81` |
| calib hash / fit_on | `b894b70b9bb76547` / calib |
| calib commit (D-019) | `4abf11083d37` 2026-09-29T19:34:52-04:00 |
| temperature fallbacks (T = 1) | has_coded_id:2: fit hit bound (20); has_phi_direct:2: fit hit bound (20); has_phi_quasi:2: fit hit bound (20); has_staff_pii:2: fit hit bound (20); pii_present:2: fit hit bound (20) |
| hardware | Apple M2, 8.0 GB, mps, Darwin 24.3.0 |
| laya version | 0.3.20 |
| checkpoints | multilingual |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-09-30T03:25:17.066398+00:00 |

### B2 / qs_v1

| field | value |
|---|---|
| arm | B2 |
| question set | qs_v1 |
| splits | test, holdout |
| docs sha256 | `9a88ce5c4c5b4a8559ef9b624d720dd823dd4fb0fdbf68115fae84b6894fada5` |
| units sha256 | `b24f0bbd4da5f5b2a6b217c146e82a1bf1b07e1cebea55068dfc76e3406ddf46` |
| decisions sha256 | `6de8a1079826349d43a07c673d57cba721b9dd02a5b59f0dfa7436843582545a` |
| calib hash / fit_on | `ebb6f90ddc687e2a` / calib |
| calib commit (D-019) | `4abf11083d37` 2026-09-29T19:34:52-04:00 |
| temperature fallbacks (T = 1) | doc_kind:4: fit hit bound (20); pii_present:2: fit hit bound (20); subject_role:4: fit hit bound (20) |
| hardware | Apple M2, 8.0 GB, mps, Darwin 24.3.0 |
| laya version | 0.3.20 |
| checkpoints | multilingual |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-09-30T03:25:18.032090+00:00 |

### B2 / qs_v2

| field | value |
|---|---|
| arm | B2 |
| question set | qs_v2 |
| splits | test, holdout |
| docs sha256 | `9a88ce5c4c5b4a8559ef9b624d720dd823dd4fb0fdbf68115fae84b6894fada5` |
| units sha256 | `b24f0bbd4da5f5b2a6b217c146e82a1bf1b07e1cebea55068dfc76e3406ddf46` |
| decisions sha256 | `150a10977a35f61b90e03cf77febfefbc2cdfb96b883a845d50ba111d5a6301a` |
| calib hash / fit_on | `68a089af2fb0ebf5` / calib |
| calib commit (D-019) | `4abf11083d37` 2026-09-29T19:34:52-04:00 |
| temperature fallbacks (T = 1) | has_coded_id:2: fit hit bound (20); has_phi_direct:2: fit hit bound (20); has_phi_quasi:2: fit hit bound (20); has_staff_pii:2: fit hit bound (20); pii_present:2: fit hit bound (20) |
| hardware | Apple M2, 8.0 GB, mps, Darwin 24.3.0 |
| laya version | 0.3.20 |
| checkpoints | multilingual |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-09-30T03:25:18.972421+00:00 |

### B3 / qs_v1 (doc-level, underpowered)

| field | value |
|---|---|
| arm | B3 |
| question set | qs_v1 |
| splits | test, holdout |
| docs sha256 | `9a88ce5c4c5b4a8559ef9b624d720dd823dd4fb0fdbf68115fae84b6894fada5` |
| units sha256 | `919a2d7f818d34571eef46ea12e7e272b73b281e63b73737d3deb5fb4671265b` |
| decisions sha256 | `004516e05ef93d5eacb9583d40b05b58bd5653b12c89210d0123b0b5999bcdee` |
| calib hash / fit_on | `9b5e40f5589275cc` / calib |
| calib commit (D-019) | `4abf11083d37` 2026-09-29T19:34:52-04:00 |
| temperature fallbacks (T = 1) | doc_kind:4: fit hit bound (20); pii_present:2: fit hit bound (20); subject_role:4: fit hit bound (20) |
| hardware | Apple M2, 8.0 GB, mps, Darwin 24.3.0 |
| laya version | 0.3.20 |
| checkpoints | multilingual |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-09-30T03:25:19.828990+00:00 |

### B3 / qs_v2 (doc-level, underpowered)

| field | value |
|---|---|
| arm | B3 |
| question set | qs_v2 |
| splits | test, holdout |
| docs sha256 | `9a88ce5c4c5b4a8559ef9b624d720dd823dd4fb0fdbf68115fae84b6894fada5` |
| units sha256 | `919a2d7f818d34571eef46ea12e7e272b73b281e63b73737d3deb5fb4671265b` |
| decisions sha256 | `12d374b103db6a1efda64bae5cdaab27b38a5220a74edffc5e14d577fda2d574` |
| calib hash / fit_on | `2301bb77da9dbf7e` / calib |
| calib commit (D-019) | `4abf11083d37` 2026-09-29T19:34:52-04:00 |
| temperature fallbacks (T = 1) | has_coded_id:2: fit hit bound (20); has_phi_direct:2: fit hit bound (20); has_phi_quasi:2: fit hit bound (20); has_staff_pii:2: fit hit bound (20); pii_present:2: fit hit bound (20) |
| hardware | Apple M2, 8.0 GB, mps, Darwin 24.3.0 |
| laya version | 0.3.20 |
| checkpoints | multilingual |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-09-30T03:25:20.681997+00:00 |

### B4 / qs_v1 (doc-level, underpowered)

| field | value |
|---|---|
| arm | B4 |
| question set | qs_v1 |
| splits | test, holdout |
| docs sha256 | `9a88ce5c4c5b4a8559ef9b624d720dd823dd4fb0fdbf68115fae84b6894fada5` |
| units sha256 | `58504d2de3e5c180f5e49bc843ee1b9b0e361f3b1e662375b6df8e127b054cd3` |
| decisions sha256 | `602b15214e7c15f4c26c64a5e93e8266a7da11905f33b79c877f41948c20cde5` |
| calib hash / fit_on | `24bca10e3ff59e18` / calib |
| calib commit (D-019) | `4abf11083d37` 2026-09-29T19:34:52-04:00 |
| temperature fallbacks (T = 1) | doc_kind:4: fit hit bound (20) |
| hardware | Apple M2, 8.0 GB, mps, Darwin 24.3.0 |
| laya version | 0.3.20 |
| checkpoints | multilingual |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-09-30T03:25:21.492895+00:00 |

### B4 / qs_v2 (doc-level, underpowered)

| field | value |
|---|---|
| arm | B4 |
| question set | qs_v2 |
| splits | test, holdout |
| docs sha256 | `9a88ce5c4c5b4a8559ef9b624d720dd823dd4fb0fdbf68115fae84b6894fada5` |
| units sha256 | `58504d2de3e5c180f5e49bc843ee1b9b0e361f3b1e662375b6df8e127b054cd3` |
| decisions sha256 | `945769af71f83099b99c8679b09350fef55b8ccdd07bbbe0f62cedac1c07470d` |
| calib hash / fit_on | `ac94d44f077d6424` / calib |
| calib commit (D-019) | `4abf11083d37` 2026-09-29T19:34:52-04:00 |
| temperature fallbacks (T = 1) | has_coded_id:2: fit hit bound (20); has_phi_direct:2: fit hit bound (20); has_staff_pii:2: fit hit bound (20) |
| hardware | Apple M2, 8.0 GB, mps, Darwin 24.3.0 |
| laya version | 0.3.20 |
| checkpoints | multilingual |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-09-30T03:25:22.298428+00:00 |

## 2. Headline operating point

### Key findings

- **The recall-first operating point is nearly degenerate.** At the calib-fit `t_low`, 8 of 10 arm x question-set runs forward under 5% of test units (A / qs_v1 0.45%, A / qs_v2 0.45%, B1 / qs_v1 0.15%, B1 / qs_v2 0.00%, B2 / qs_v1 0.94%, B2 / qs_v2 1.88%, B3 / qs_v1 (doc-level, underpowered) 1.60%, B4 / qs_v1 (doc-level, underpowered) 2.42%). The trivial policy "escalate everything" has recall 1 and forward rate 0, so high recall here says little about work saved. With few calib positives the recall target means "no calib misses": `t_low` is the lowest-scoring calib positive, a single unit.
- **Some checkpoints barely rank PII.** Test AUROC of calibrated p(pii) below 0.6: B1 / qs_v1 0.379, B1 / qs_v2 0.377, B2 / qs_v1 0.449, B2 / qs_v2 0.445, B3 / qs_v1 (doc-level, underpowered) 0.491, B3 / qs_v2 (doc-level, underpowered) 0.481, B4 / qs_v1 (doc-level, underpowered) 0.473, B4 / qs_v2 (doc-level, underpowered) 0.456. Their high recall comes from answering "PII present" to almost everything, not from detection (option-swap probe: `reports/audits/M6_pii_question_probe-20260929.md`).
- **The recall target does not transfer from calib to test** for B3 / qs_v2 (doc-level, underpowered) (0.929, exact upper 0.974), B4 / qs_v1 (doc-level, underpowered) (0.963, exact upper 0.992), B4 / qs_v2 (doc-level, underpowered) (0.925, exact upper 0.972); target 0.995.
- **Quasi-identifiers alone are the hardest positives.** AUROC quasi-only vs direct: A / qs_v1 0.706 vs 0.834, A / qs_v2 0.705 vs 0.832, B2 / qs_v1 0.427 vs 0.539, B2 / qs_v2 0.418 vs 0.540, B3 / qs_v1 (doc-level, underpowered) 0.493 vs 0.562, B3 / qs_v2 (doc-level, underpowered) 0.437 vs 0.551, B4 / qs_v2 (doc-level, underpowered) 0.430 vs 0.505. The pii_present prompt names names, contacts, MRNs and birth dates, not event dates or initials, which the gold counts (phi_quasi).
- **False forwards are not independent across arms.** Short documents fit in one unit for B2-B4, so those arms see identical text and repeat the same misses: d0352 in 6 runs, d0447 in 3 runs, d0418 in 3 runs (12 of 20 test false forwards).
- Truncated units were forwarded (the model never saw their tail): B2 / qs_v1 1, B2 / qs_v2 2.
- qs_v1 vs qs_v2 differences in the same arm are not a question-wording effect: pii_present has the same text in both, qs_v1 runs fp32 and qs_v2 fp16 (5 rows) on MPS, which moves long-input probabilities, and only qs_v1 has the role rule.

### Test (headline)

pii_present recall at the calib-fit `t_low` (95% document-level bootstrap CI). Exact lo / hi are Clopper-Pearson on unit counts (ignore clustering within documents); the recall target is `missed` when the exact upper bound is below it. `point - exact lo` above 0.01 flags D-008 for review on arm A only (D-008 amended). Negatives forwarded = forwarded PII-free units / PII-free units (the work saved). Route recall counts misses after routing (1 - false forwards / positives). t_high `none`: no threshold reached the precision target, so only the role rule redacts. Doc-level arms are underpowered (few units per document).

| arm / qs | t_low | t_high | recall | exact lo / hi | recall target | point - exact lo | route recall | forward rate | negatives forwarded | false forwards | AUROC p(pii) | PII share at p >= t_low | units / docs / positives |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A / qs_v1 | 0.0054 | none | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9747 / 1.0000 | not rejected (upper 1.0000) | 0.0253 **D-008 review** | 1.0000 | 0.0045 [0.0019, 0.0078] | 0.0048 | 0 | 0.7775 | 0.0721 | 2006 / 124 / 144 |
| A / qs_v2 | 0.0054 | none | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9747 / 1.0000 | not rejected (upper 1.0000) | 0.0253 **D-008 review** | 1.0000 | 0.0045 [0.0019, 0.0078] | 0.0048 | 0 | 0.7767 | 0.0721 | 2006 / 124 / 144 |
| B1 / qs_v1 | 0.0250 | 0.9999 | 0.9900 [0.9667, 1.0000] | 0.9455 / 0.9997 | not rejected (upper 0.9997) | 0.0445 | 0.9900 | 0.0015 [0.0000, 0.0049] | 0.0000 | 1 | 0.3788 | 0.1473 | 673 / 124 / 100 |
| B1 / qs_v2 | 0.0222 | 0.9999 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9638 / 1.0000 | not rejected (upper 1.0000) | 0.0362 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.3774 | 0.1486 | 673 / 124 / 100 |
| B2 / qs_v1 | 0.3457 | 0.9965 | 0.9773 [0.9405, 1.0000] | 0.9203 / 0.9972 | not rejected (upper 0.9972) | 0.0570 | 0.9886 | 0.0094 [0.0000, 0.0224] | 0.0086 | 1 | 0.4486 | 0.2730 | 320 / 124 / 88 |
| B2 / qs_v2 | 0.3465 | 0.9969 | 0.9773 [0.9405, 1.0000] | 0.9203 / 0.9972 | not rejected (upper 0.9972) | 0.0570 | 0.9773 | 0.0187 [0.0060, 0.0356] | 0.0172 | 2 | 0.4448 | 0.2739 | 320 / 124 / 88 |
| B3 / qs_v1 (doc-level, underpowered) | 0.1907 | 0.9786 | 0.9765 [0.9390, 1.0000] | 0.9176 / 0.9971 | not rejected (upper 0.9971) | 0.0589 | 0.9765 | 0.0160 [0.0000, 0.0363] | 0.0098 | 2 | 0.4912 | 0.4511 | 187 / 124 / 85 |
| B3 / qs_v2 (doc-level, underpowered) | 0.5142 | 0.9923 | 0.9294 [0.8690, 0.9775] | 0.8527 / 0.9737 | **missed** (upper 0.9737 < 0.995) | 0.0767 | 0.9294 | 0.0535 [0.0251, 0.0904] | 0.0392 | 6 | 0.4805 | 0.4463 | 187 / 124 / 85 |
| B4 / qs_v1 (doc-level, underpowered) | 0.4425 | 0.7362 | 0.9625 [0.9146, 1.0000] | 0.8943 / 0.9922 | **missed** (upper 0.9922 < 0.995) | 0.0682 | 0.9750 | 0.0242 [0.0000, 0.0565] | 0.0227 | 2 | 0.4729 | 0.6417 | 124 / 124 / 80 |
| B4 / qs_v2 (doc-level, underpowered) | 0.4841 | none | 0.9250 [0.8592, 0.9756] | 0.8439 / 0.9720 | **missed** (upper 0.9720 < 0.995) | 0.0811 | 0.9250 | 0.0565 [0.0242, 0.1048] | 0.0227 | 6 | 0.4564 | 0.6325 | 124 / 124 / 80 |


### Holdout (descriptive only, D-005)

All IRB letters (one document type, 30 documents, few positives), never part of the headline. With a forward rate of 0, recall here is vacuous. Known limitation (M4 S1): a fixed alt-text contact line appears only in PII-free letters, a possible shortcut cue.

| arm / qs | t_low | t_high | recall | exact lo / hi | recall target | point - exact lo | route recall | forward rate | negatives forwarded | false forwards | AUROC p(pii) | PII share at p >= t_low | units / docs / positives |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A / qs_v1 | 0.0054 | none | 1.0000 (no misses; CI n/a, see exact bounds) | 0.8316 / 1.0000 | not rejected (upper 1.0000) | 0.1684 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.5755 | 0.0678 | 295 / 30 / 20 |
| A / qs_v2 | 0.0054 | none | 1.0000 (no misses; CI n/a, see exact bounds) | 0.8316 / 1.0000 | not rejected (upper 1.0000) | 0.1684 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.5769 | 0.0678 | 295 / 30 / 20 |
| B1 / qs_v1 | 0.0250 | 0.9999 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.8316 / 1.0000 | not rejected (upper 1.0000) | 0.1684 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.2930 | 0.2020 | 99 / 30 / 20 |
| B1 / qs_v2 | 0.0222 | 0.9999 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.8316 / 1.0000 | not rejected (upper 1.0000) | 0.1684 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.2987 | 0.2020 | 99 / 30 / 20 |
| B2 / qs_v1 | 0.3457 | 0.9965 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.8316 / 1.0000 | not rejected (upper 1.0000) | 0.1684 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.3967 | 0.4000 | 50 / 30 / 20 |
| B2 / qs_v2 | 0.3465 | 0.9969 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.8316 / 1.0000 | not rejected (upper 1.0000) | 0.1684 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.4108 | 0.4000 | 50 / 30 / 20 |
| B3 / qs_v1 (doc-level, underpowered) | 0.1907 | 0.9786 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.8316 / 1.0000 | not rejected (upper 1.0000) | 0.1684 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.5909 | 0.6452 | 31 / 30 / 20 |
| B3 / qs_v2 (doc-level, underpowered) | 0.5142 | 0.9923 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.8316 / 1.0000 | not rejected (upper 1.0000) | 0.1684 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.6818 | 0.6452 | 31 / 30 / 20 |
| B4 / qs_v1 (doc-level, underpowered) | 0.4425 | 0.7362 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.8316 / 1.0000 | not rejected (upper 1.0000) | 0.1684 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.5700 | 0.6667 | 30 / 30 / 20 |
| B4 / qs_v2 (doc-level, underpowered) | 0.4841 | none | 1.0000 (no misses; CI n/a, see exact bounds) | 0.8316 / 1.0000 | not rejected (upper 1.0000) | 0.1684 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.6600 | 0.6667 | 30 / 30 / 20 |

## 3. Per-question

### A / qs_v1, test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 2006 | 0.9362 | 0.6155 | 0.9282 (B) |
| subject_role | 2006 | 0.7453 | 0.2501 | 0.9282 (none) |
| category | 2006 | 0.9103 | 0.3415 | 0.9143 (none) |
| doc_kind | 2006 | 0.2552 | 0.1485 | 0.3116 (narrative) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 23 | 121 |
| B | 7 | 1855 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 9 | 7 | 4 | 57 |
| staff | 3 | 6 | 1 | 25 |
| both | 7 | 6 | 0 | 19 |
| none | 79 | 262 | 41 | 1480 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 0 | 0 | 12 | 0 | 19 |
| quasi | 1 | 2 | 25 | 0 | 50 |
| coded | 0 | 0 | 15 | 0 | 23 |
| staff | 0 | 0 | 1 | 8 | 16 |
| none | 2 | 5 | 22 | 4 | 1801 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 58 | 2 | 10 | 555 |
| form_table | 29 | 5 | 9 | 495 |
| correspondence | 21 | 0 | 8 | 344 |
| protocol_text | 22 | 2 | 5 | 441 |

### A / qs_v1, holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 295 | 0.9322 | 0.4825 | 0.9322 (B) |
| subject_role | 295 | 0.7390 | 0.2348 | 0.9322 (none) |
| category | 295 | 0.9356 | 0.3545 | 0.9322 (none) |
| doc_kind | 295 | 0.0305 | 0.0197 | 1.0000 (correspondence) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 20 |
| B | 0 | 275 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 0 | 0 | 0 | 0 |
| staff | 0 | 3 | 0 | 17 |
| both | 0 | 0 | 0 | 0 |
| none | 11 | 43 | 6 | 215 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 0 | 0 | 0 | 0 | 0 |
| quasi | 0 | 0 | 0 | 0 | 0 |
| coded | 0 | 0 | 0 | 0 | 0 |
| staff | 0 | 0 | 1 | 1 | 18 |
| none | 0 | 0 | 0 | 0 | 275 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 0 | 0 | 0 | 0 |
| form_table | 0 | 0 | 0 | 0 |
| correspondence | 15 | 0 | 9 | 271 |
| protocol_text | 0 | 0 | 0 | 0 |

### A / qs_v2, test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 2006 | 0.9362 | 0.6155 | 0.9282 (B) |
| has_phi_direct | 2006 | 0.9611 | 0.6150 | 0.9845 (B) |
| has_phi_quasi | 2006 | 0.9397 | 0.7410 | 0.9487 (B) |
| has_coded_id | 2006 | 0.9397 | 0.7904 | 0.9457 (B) |
| has_staff_pii | 2006 | 0.5952 | 0.4230 | 0.9666 (B) |

Multi-label categories: micro-F1 0.2817, macro-F1 0.3713.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 23 | 121 |
| B | 7 | 1855 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 13 | 18 |
| B | 60 | 1915 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 64 | 39 |
| B | 82 | 1821 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 96 | 13 |
| B | 108 | 1789 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 49 | 18 |
| B | 794 | 1145 |

### A / qs_v2, holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 295 | 0.9322 | 0.4825 | 0.9322 (B) |
| has_phi_direct | 295 | 0.9932 | 0.4983 | 1.0000 (B) |
| has_phi_quasi | 295 | 0.9729 | 0.4931 | 1.0000 (B) |
| has_coded_id | 295 | 0.9729 | 0.4931 | 1.0000 (B) |
| has_staff_pii | 295 | 0.6237 | 0.5060 | 0.9322 (B) |

Multi-label categories: micro-F1 0.2367, macro-F1 0.0662.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 20 |
| B | 0 | 275 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 2 | 293 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 8 | 287 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 8 | 287 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 20 | 0 |
| B | 111 | 164 |

### B1 / qs_v1, test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 673 | 0.1605 | 0.1478 | 0.8514 (B) |
| subject_role | 673 | 0.1783 | 0.1227 | 0.8514 (none) |
| category | 673 | 0.4933 | 0.2283 | 0.8217 (none) |
| doc_kind | 673 | 0.2571 | 0.2423 | 0.3046 (form_table) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 95 | 5 |
| B | 560 | 13 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 12 | 17 | 1 | 12 |
| staff | 4 | 15 | 0 | 7 |
| both | 13 | 11 | 1 | 7 |
| none | 154 | 309 | 18 | 92 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 1 | 1 | 5 | 5 | 15 |
| quasi | 0 | 4 | 8 | 11 | 24 |
| coded | 2 | 2 | 9 | 1 | 15 |
| staff | 0 | 0 | 0 | 9 | 8 |
| none | 13 | 5 | 33 | 193 | 309 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 71 | 12 | 75 | 43 |
| form_table | 63 | 23 | 94 | 25 |
| correspondence | 45 | 6 | 55 | 11 |
| protocol_text | 67 | 13 | 46 | 24 |

### B1 / qs_v1, holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 99 | 0.2121 | 0.1820 | 0.7980 (B) |
| subject_role | 99 | 0.3030 | 0.1731 | 0.7980 (none) |
| category | 99 | 0.5960 | 0.2648 | 0.7980 (none) |
| doc_kind | 99 | 0.3535 | 0.1306 | 1.0000 (correspondence) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 20 | 0 |
| B | 78 | 1 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 0 | 0 | 0 | 0 |
| staff | 6 | 12 | 0 | 2 |
| both | 0 | 0 | 0 | 0 |
| none | 18 | 41 | 2 | 18 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 0 | 0 | 0 | 0 | 0 |
| quasi | 0 | 0 | 0 | 0 | 0 |
| coded | 0 | 0 | 0 | 0 | 0 |
| staff | 0 | 1 | 0 | 9 | 10 |
| none | 4 | 1 | 0 | 24 | 50 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 0 | 0 | 0 | 0 |
| form_table | 0 | 0 | 0 | 0 |
| correspondence | 31 | 8 | 35 | 25 |
| protocol_text | 0 | 0 | 0 | 0 |

### B1 / qs_v2, test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 673 | 0.1605 | 0.1478 | 0.8514 (B) |
| has_phi_direct | 673 | 0.1352 | 0.1317 | 0.9599 (B) |
| has_phi_quasi | 673 | 0.1798 | 0.1798 | 0.8945 (B) |
| has_coded_id | 673 | 0.1768 | 0.1763 | 0.8692 (B) |
| has_staff_pii | 673 | 0.1471 | 0.1470 | 0.9138 (B) |

Multi-label categories: micro-F1 0.1496, macro-F1 0.1481.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 95 | 5 |
| B | 560 | 13 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 24 | 3 |
| B | 579 | 67 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 61 | 10 |
| B | 542 | 60 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 68 | 20 |
| B | 534 | 51 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 46 | 12 |
| B | 562 | 53 |

### B1 / qs_v2, holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 99 | 0.2121 | 0.1820 | 0.7980 (B) |
| has_phi_direct | 99 | 0.0808 | 0.0748 | 1.0000 (B) |
| has_phi_quasi | 99 | 0.1010 | 0.0917 | 1.0000 (B) |
| has_coded_id | 99 | 0.0606 | 0.0571 | 1.0000 (B) |
| has_staff_pii | 99 | 0.2525 | 0.2350 | 0.7980 (B) |

Multi-label categories: micro-F1 0.1034, macro-F1 0.0877.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 20 | 0 |
| B | 78 | 1 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 91 | 8 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 89 | 10 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 93 | 6 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 20 | 0 |
| B | 74 | 5 |

### B2 / qs_v1, test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 320 | 0.2750 | 0.2317 | 0.7250 (B) |
| subject_role | 320 | 0.2094 | 0.1823 | 0.7250 (none) |
| category | 320 | 0.4156 | 0.2509 | 0.6937 (none) |
| doc_kind | 320 | 0.2906 | 0.2708 | 0.3312 (form_table) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 82 | 6 |
| B | 226 | 6 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 15 | 11 | 0 | 4 |
| staff | 2 | 15 | 0 | 9 |
| both | 12 | 12 | 1 | 7 |
| none | 46 | 140 | 10 | 36 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 3 | 0 | 5 | 5 | 14 |
| quasi | 0 | 2 | 7 | 13 | 13 |
| coded | 0 | 0 | 6 | 7 | 7 |
| staff | 0 | 0 | 2 | 9 | 5 |
| none | 2 | 2 | 11 | 94 | 113 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 40 | 2 | 41 | 9 |
| form_table | 23 | 10 | 62 | 11 |
| correspondence | 19 | 4 | 31 | 1 |
| protocol_text | 36 | 2 | 17 | 12 |

### B2 / qs_v1, holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 50 | 0.4000 | 0.2857 | 0.6000 (B) |
| subject_role | 50 | 0.4400 | 0.2920 | 0.6000 (none) |
| category | 50 | 0.5600 | 0.2854 | 0.6000 (none) |
| doc_kind | 50 | 0.5800 | 0.2447 | 1.0000 (correspondence) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 20 | 0 |
| B | 30 | 0 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 0 | 0 | 0 | 0 |
| staff | 3 | 16 | 0 | 1 |
| both | 0 | 0 | 0 | 0 |
| none | 2 | 22 | 0 | 6 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 0 | 0 | 0 | 0 | 0 |
| quasi | 0 | 0 | 0 | 0 | 0 |
| coded | 0 | 0 | 0 | 0 | 0 |
| staff | 0 | 1 | 1 | 13 | 5 |
| none | 0 | 0 | 0 | 15 | 15 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 0 | 0 | 0 | 0 |
| form_table | 0 | 0 | 0 | 0 |
| correspondence | 16 | 0 | 29 | 5 |
| protocol_text | 0 | 0 | 0 | 0 |

### B2 / qs_v2, test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 320 | 0.2750 | 0.2317 | 0.7250 (B) |
| has_phi_direct | 320 | 0.1469 | 0.1468 | 0.9156 (B) |
| has_phi_quasi | 320 | 0.2375 | 0.2324 | 0.8156 (B) |
| has_coded_id | 320 | 0.2250 | 0.2127 | 0.7812 (B) |
| has_staff_pii | 320 | 0.1969 | 0.1860 | 0.8187 (B) |

Multi-label categories: micro-F1 0.2626, macro-F1 0.2602.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 82 | 6 |
| B | 226 | 6 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 25 | 2 |
| B | 271 | 22 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 51 | 8 |
| B | 236 | 25 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 56 | 14 |
| B | 234 | 16 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 50 | 8 |
| B | 249 | 13 |

### B2 / qs_v2, holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 50 | 0.4000 | 0.2857 | 0.6000 (B) |
| has_phi_direct | 50 | 0.0200 | 0.0196 | 1.0000 (B) |
| has_phi_quasi | 50 | 0.0400 | 0.0385 | 1.0000 (B) |
| has_coded_id | 50 | 0.0400 | 0.0385 | 1.0000 (B) |
| has_staff_pii | 50 | 0.4400 | 0.3566 | 0.6000 (B) |

Multi-label categories: micro-F1 0.1878, macro-F1 0.1471.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 20 | 0 |
| B | 30 | 0 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 49 | 1 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 48 | 2 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 48 | 2 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 20 | 0 |
| B | 28 | 2 |

### B3 / qs_v1 (doc-level, underpowered), test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 187 | 0.4278 | 0.3216 | 0.5455 (B) |
| subject_role | 187 | 0.2941 | 0.2626 | 0.5455 (none) |
| category | 187 | 0.3369 | 0.2495 | 0.4973 (none) |
| doc_kind | 187 | 0.3155 | 0.3062 | 0.3957 (form_table) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 77 | 8 |
| B | 99 | 3 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 16 | 9 | 0 | 4 |
| staff | 1 | 18 | 2 | 4 |
| both | 12 | 12 | 1 | 6 |
| none | 22 | 53 | 7 | 20 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 2 | 1 | 6 | 6 | 12 |
| quasi | 0 | 3 | 7 | 10 | 13 |
| coded | 0 | 0 | 7 | 5 | 7 |
| staff | 0 | 1 | 2 | 8 | 4 |
| none | 0 | 2 | 14 | 34 | 43 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 27 | 0 | 19 | 4 |
| form_table | 4 | 8 | 54 | 8 |
| correspondence | 12 | 1 | 16 | 0 |
| protocol_text | 20 | 1 | 5 | 8 |

### B3 / qs_v1 (doc-level, underpowered), holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 31 | 0.6452 | 0.3922 | 0.6452 (A) |
| subject_role | 31 | 0.5806 | 0.2547 | 0.6452 (staff) |
| category | 31 | 0.7097 | 0.6760 | 0.6452 (staff) |
| doc_kind | 31 | 0.8387 | 0.3041 | 1.0000 (correspondence) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 20 | 0 |
| B | 11 | 0 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 0 | 0 | 0 | 0 |
| staff | 3 | 16 | 1 | 0 |
| both | 0 | 0 | 0 | 0 |
| none | 0 | 9 | 0 | 2 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 0 | 0 | 0 | 0 | 0 |
| quasi | 0 | 0 | 0 | 0 | 0 |
| coded | 0 | 0 | 0 | 0 | 0 |
| staff | 0 | 0 | 0 | 16 | 4 |
| none | 0 | 0 | 0 | 5 | 6 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 0 | 0 | 0 | 0 |
| form_table | 0 | 0 | 0 | 0 |
| correspondence | 1 | 0 | 26 | 4 |
| protocol_text | 0 | 0 | 0 | 0 |

### B3 / qs_v2 (doc-level, underpowered), test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 187 | 0.4385 | 0.3274 | 0.5455 (B) |
| has_phi_direct | 187 | 0.2620 | 0.2620 | 0.8556 (B) |
| has_phi_quasi | 187 | 0.3422 | 0.3169 | 0.6952 (B) |
| has_coded_id | 187 | 0.3690 | 0.3302 | 0.6310 (B) |
| has_staff_pii | 187 | 0.3369 | 0.3156 | 0.7005 (B) |

Multi-label categories: micro-F1 0.4171, macro-F1 0.4105.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 79 | 6 |
| B | 99 | 3 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 25 | 2 |
| B | 136 | 24 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 50 | 7 |
| B | 116 | 14 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 57 | 12 |
| B | 106 | 12 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 48 | 8 |
| B | 116 | 15 |

### B3 / qs_v2 (doc-level, underpowered), holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 31 | 0.6452 | 0.3922 | 0.6452 (A) |
| has_phi_direct | 31 | 0.0000 | 0.0000 | 1.0000 (B) |
| has_phi_quasi | 31 | 0.0323 | 0.0312 | 1.0000 (B) |
| has_coded_id | 31 | 0.0000 | 0.0000 | 1.0000 (B) |
| has_staff_pii | 31 | 0.6452 | 0.3922 | 0.6452 (A) |

Multi-label categories: micro-F1 0.2797, macro-F1 0.1961.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 20 | 0 |
| B | 11 | 0 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 31 | 0 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 30 | 1 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 31 | 0 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 20 | 0 |
| B | 11 | 0 |

### B4 / qs_v1 (doc-level, underpowered), test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 124 | 0.5887 | 0.3881 | 0.6452 (A) |
| subject_role | 124 | 0.3468 | 0.3168 | 0.3548 (none) |
| category | 124 | 0.2742 | 0.2345 | 0.2903 (none) |
| doc_kind | 124 | 0.2984 | 0.3371 | 0.5565 (form_table) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 72 | 8 |
| B | 43 | 1 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 17 | 7 | 0 | 4 |
| staff | 1 | 14 | 2 | 4 |
| both | 11 | 12 | 1 | 7 |
| none | 8 | 20 | 5 | 11 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 1 | 1 | 9 | 5 | 11 |
| quasi | 0 | 4 | 8 | 9 | 11 |
| coded | 0 | 0 | 9 | 6 | 4 |
| staff | 0 | 0 | 2 | 4 | 4 |
| none | 0 | 2 | 11 | 7 | 16 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 11 | 0 | 12 | 2 |
| form_table | 1 | 7 | 53 | 8 |
| correspondence | 1 | 0 | 13 | 0 |
| protocol_text | 4 | 0 | 6 | 6 |

### B4 / qs_v1 (doc-level, underpowered), holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 30 | 0.6667 | 0.4000 | 0.6667 (A) |
| subject_role | 30 | 0.5667 | 0.2232 | 0.6667 (staff) |
| category | 30 | 0.7000 | 0.6534 | 0.6667 (staff) |
| doc_kind | 30 | 0.8333 | 0.3030 | 1.0000 (correspondence) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 20 | 0 |
| B | 10 | 0 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 0 | 0 | 0 | 0 |
| staff | 3 | 16 | 1 | 0 |
| both | 0 | 0 | 0 | 0 |
| none | 0 | 9 | 0 | 1 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 0 | 0 | 0 | 0 | 0 |
| quasi | 0 | 0 | 0 | 0 | 0 |
| coded | 0 | 0 | 0 | 0 | 0 |
| staff | 0 | 0 | 0 | 16 | 4 |
| none | 0 | 0 | 0 | 5 | 5 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 0 | 0 | 0 | 0 |
| form_table | 0 | 0 | 0 | 0 |
| correspondence | 1 | 0 | 25 | 4 |
| protocol_text | 0 | 0 | 0 | 0 |

### B4 / qs_v2 (doc-level, underpowered), test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 124 | 0.5968 | 0.3917 | 0.6452 (A) |
| has_phi_direct | 124 | 0.3468 | 0.3447 | 0.7823 (B) |
| has_phi_quasi | 124 | 0.4758 | 0.4183 | 0.5484 (B) |
| has_coded_id | 124 | 0.5323 | 0.4414 | 0.5565 (A) |
| has_staff_pii | 124 | 0.4516 | 0.4125 | 0.5806 (B) |

Multi-label categories: micro-F1 0.5641, macro-F1 0.5534.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 73 | 7 |
| B | 43 | 1 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 25 | 2 |
| B | 79 | 18 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 49 | 7 |
| B | 58 | 10 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 58 | 11 |
| B | 47 | 8 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 44 | 8 |
| B | 60 | 12 |

### B4 / qs_v2 (doc-level, underpowered), holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 30 | 0.6667 | 0.4000 | 0.6667 (A) |
| has_phi_direct | 30 | 0.0000 | 0.0000 | 1.0000 (B) |
| has_phi_quasi | 30 | 0.0000 | 0.0000 | 1.0000 (B) |
| has_coded_id | 30 | 0.0000 | 0.0000 | 1.0000 (B) |
| has_staff_pii | 30 | 0.6667 | 0.4000 | 0.6667 (A) |

Multi-label categories: micro-F1 0.2857, macro-F1 0.2000.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 20 | 0 |
| B | 10 | 0 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 30 | 0 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 30 | 0 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 30 | 0 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 20 | 0 |
| B | 10 | 0 |

### qs_v1 vs qs_v2

Same arm and split under both question sets. `pii_present` is the same question in both; categories are single-label in qs_v1 (`category`) and per-category yes/no in qs_v2.

| arm | split | qs | pii_present acc | pii_present macro-F1 | recall | forward rate | category macro-F1 (qs_v1) | categories micro / macro-F1 (qs_v2) |
|---|---|---|---|---|---|---|---|---|
| A | holdout | qs_v1 | 0.9322 | 0.4825 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | 0.3545 | n/a |
| A | holdout | qs_v2 | 0.9322 | 0.4825 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | n/a | 0.2367 / 0.0662 |
| A | test | qs_v1 | 0.9362 | 0.6155 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0045 [0.0019, 0.0078] | 0.3415 | n/a |
| A | test | qs_v2 | 0.9362 | 0.6155 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0045 [0.0019, 0.0078] | n/a | 0.2817 / 0.3713 |
| B1 | holdout | qs_v1 | 0.2121 | 0.1820 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | 0.2648 | n/a |
| B1 | holdout | qs_v2 | 0.2121 | 0.1820 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | n/a | 0.1034 / 0.0877 |
| B1 | test | qs_v1 | 0.1605 | 0.1478 | 0.9900 [0.9667, 1.0000] | 0.0015 [0.0000, 0.0049] | 0.2283 | n/a |
| B1 | test | qs_v2 | 0.1605 | 0.1478 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | n/a | 0.1496 / 0.1481 |
| B2 | holdout | qs_v1 | 0.4000 | 0.2857 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | 0.2854 | n/a |
| B2 | holdout | qs_v2 | 0.4000 | 0.2857 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | n/a | 0.1878 / 0.1471 |
| B2 | test | qs_v1 | 0.2750 | 0.2317 | 0.9773 [0.9405, 1.0000] | 0.0094 [0.0000, 0.0224] | 0.2509 | n/a |
| B2 | test | qs_v2 | 0.2750 | 0.2317 | 0.9773 [0.9405, 1.0000] | 0.0187 [0.0060, 0.0356] | n/a | 0.2626 / 0.2602 |
| B3 | holdout | qs_v1 | 0.6452 | 0.3922 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | 0.6760 | n/a |
| B3 | holdout | qs_v2 | 0.6452 | 0.3922 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | n/a | 0.2797 / 0.1961 |
| B3 | test | qs_v1 | 0.4278 | 0.3216 | 0.9765 [0.9390, 1.0000] | 0.0160 [0.0000, 0.0363] | 0.2495 | n/a |
| B3 | test | qs_v2 | 0.4385 | 0.3274 | 0.9294 [0.8690, 0.9775] | 0.0535 [0.0251, 0.0904] | n/a | 0.4171 / 0.4105 |
| B4 | holdout | qs_v1 | 0.6667 | 0.4000 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | 0.6534 | n/a |
| B4 | holdout | qs_v2 | 0.6667 | 0.4000 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | n/a | 0.2857 / 0.2000 |
| B4 | test | qs_v1 | 0.5887 | 0.3881 | 0.9625 [0.9146, 1.0000] | 0.0242 [0.0000, 0.0565] | 0.2345 | n/a |
| B4 | test | qs_v2 | 0.5968 | 0.3917 | 0.9250 [0.8592, 0.9756] | 0.0565 [0.0242, 0.1048] | n/a | 0.5641 / 0.5534 |

## 4. Calibration

ECE uses 15 equal-width bins on the max probability. Brier is multi-class. AUROC scores correctness by the max probability (for pii_present discrimination see section 2). `= raw (T fallback)`: the temperature fit hit its bound, so T = 1 and the calibrated columns equal raw; calibration did nothing there.

### A / qs_v1, test

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.1091 | 0.0162 | 0.1308 | 0.1063 | 0.7451 | 0.7451 |
| subject_role | 0.2519 | 0.1227 | 0.4834 | 0.4111 | 0.6557 | 0.6635 |
| category | 0.4396 | 0.0275 | 0.4019 | 0.1491 | 0.8297 | 0.8483 |
| doc_kind = raw (T fallback) | 0.3956 | 0.3956 | 0.9947 | 0.9947 | 0.5094 | 0.5094 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 21 | 0.5171 | 0.6190 | 11 | 0.5182 | 0.6364 |
| [0.533, 0.600) | 31 | 0.5705 | 0.5484 | 19 | 0.5588 | 0.4737 |
| [0.600, 0.667) | 39 | 0.6377 | 0.6154 | 19 | 0.6397 | 0.6316 |
| [0.667, 0.733) | 78 | 0.7070 | 0.7564 | 20 | 0.6997 | 0.6500 |
| [0.733, 0.800) | 265 | 0.7751 | 0.9094 | 35 | 0.7666 | 0.7143 |
| [0.800, 0.867) | 982 | 0.8382 | 0.9735 | 77 | 0.8399 | 0.7403 |
| [0.867, 0.933) | 572 | 0.8884 | 0.9633 | 380 | 0.9108 | 0.9289 |
| [0.933, 1.000) | 18 | 0.9472 | 0.9444 | 1445 | 0.9620 | 0.9702 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 81 | 0.3130 | 0.4691 | 13 | 0.3155 | 0.5385 |
| [0.333, 0.400) | 268 | 0.3713 | 0.5373 | 79 | 0.3702 | 0.4557 |
| [0.400, 0.467) | 464 | 0.4350 | 0.7026 | 177 | 0.4352 | 0.4689 |
| [0.467, 0.533) | 451 | 0.5001 | 0.8137 | 267 | 0.5008 | 0.6442 |
| [0.533, 0.600) | 402 | 0.5640 | 0.8582 | 275 | 0.5664 | 0.7527 |
| [0.600, 0.667) | 221 | 0.6295 | 0.8462 | 253 | 0.6348 | 0.7905 |
| [0.667, 0.733) | 82 | 0.6924 | 0.7927 | 315 | 0.7001 | 0.8317 |
| [0.733, 0.800) | 20 | 0.7645 | 0.8000 | 273 | 0.7656 | 0.8828 |
| [0.800, 0.867) | 11 | 0.8197 | 0.6364 | 221 | 0.8323 | 0.8552 |
| [0.867, 0.933) | 6 | 0.8992 | 0.0000 | 102 | 0.8939 | 0.7843 |
| [0.933, 1.000) | 0 | n/a | n/a | 31 | 0.9636 | 0.5806 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 3 | 0.2580 | 0.3333 | 0 | n/a | n/a |
| [0.267, 0.333) | 75 | 0.3111 | 0.4133 | 0 | n/a | n/a |
| [0.333, 0.400) | 222 | 0.3713 | 0.7207 | 5 | 0.3776 | 0.2000 |
| [0.400, 0.467) | 582 | 0.4368 | 0.9141 | 12 | 0.4444 | 0.0833 |
| [0.467, 0.533) | 782 | 0.4985 | 0.9795 | 30 | 0.5015 | 0.4667 |
| [0.533, 0.600) | 308 | 0.5590 | 0.9870 | 38 | 0.5654 | 0.4737 |
| [0.600, 0.667) | 29 | 0.6210 | 0.9655 | 44 | 0.6318 | 0.5909 |
| [0.667, 0.733) | 5 | 0.6903 | 0.8000 | 54 | 0.7001 | 0.6852 |
| [0.733, 0.800) | 0 | n/a | n/a | 80 | 0.7688 | 0.7625 |
| [0.800, 0.867) | 0 | n/a | n/a | 182 | 0.8386 | 0.8901 |
| [0.867, 0.933) | 0 | n/a | n/a | 529 | 0.9077 | 0.9263 |
| [0.933, 1.000) | 0 | n/a | n/a | 1032 | 0.9621 | 0.9845 |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 15 | 0.3169 | 0.2667 | 15 | 0.3169 | 0.2667 |
| [0.333, 0.400) | 116 | 0.3735 | 0.2241 | 116 | 0.3735 | 0.2241 |
| [0.400, 0.467) | 191 | 0.4346 | 0.2932 | 191 | 0.4346 | 0.2932 |
| [0.467, 0.533) | 246 | 0.4995 | 0.2358 | 246 | 0.4995 | 0.2358 |
| [0.533, 0.600) | 255 | 0.5672 | 0.2196 | 255 | 0.5672 | 0.2196 |
| [0.600, 0.667) | 255 | 0.6324 | 0.2784 | 256 | 0.6325 | 0.2773 |
| [0.667, 0.733) | 215 | 0.6995 | 0.2651 | 215 | 0.6998 | 0.2651 |
| [0.733, 0.800) | 246 | 0.7667 | 0.2358 | 245 | 0.7669 | 0.2367 |
| [0.800, 0.867) | 230 | 0.8308 | 0.3174 | 230 | 0.8308 | 0.3174 |
| [0.867, 0.933) | 183 | 0.8969 | 0.2186 | 183 | 0.8969 | 0.2186 |
| [0.933, 1.000) | 54 | 0.9525 | 0.2407 | 54 | 0.9525 | 0.2407 |

### A / qs_v1, holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.0903 | 0.0345 | 0.1443 | 0.1278 | 0.5755 | 0.5755 |
| subject_role | 0.2414 | 0.0988 | 0.4665 | 0.4037 | 0.6335 | 0.6470 |
| category | 0.4576 | 0.0410 | 0.3909 | 0.1261 | 0.7142 | 0.7288 |
| doc_kind = raw (T fallback) | 0.6155 | 0.6155 | 1.2329 | 1.2329 | 0.3230 | 0.3225 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.600, 0.667) | 3 | 0.6446 | 1.0000 | 0 | n/a | n/a |
| [0.667, 0.733) | 8 | 0.7132 | 0.8750 | 1 | 0.7004 | 1.0000 |
| [0.733, 0.800) | 38 | 0.7792 | 0.9211 | 3 | 0.7699 | 1.0000 |
| [0.800, 0.867) | 155 | 0.8389 | 0.9226 | 8 | 0.8455 | 0.8750 |
| [0.867, 0.933) | 88 | 0.8894 | 0.9545 | 54 | 0.9127 | 0.9444 |
| [0.933, 1.000) | 3 | 0.9412 | 1.0000 | 229 | 0.9618 | 0.9301 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 14 | 0.3082 | 0.2143 | 4 | 0.3111 | 0.0000 |
| [0.333, 0.400) | 27 | 0.3649 | 0.6667 | 13 | 0.3703 | 0.3846 |
| [0.400, 0.467) | 67 | 0.4316 | 0.7313 | 16 | 0.4271 | 0.6875 |
| [0.467, 0.533) | 79 | 0.5014 | 0.7975 | 40 | 0.4991 | 0.7000 |
| [0.533, 0.600) | 53 | 0.5703 | 0.7170 | 43 | 0.5680 | 0.6512 |
| [0.600, 0.667) | 33 | 0.6265 | 0.7879 | 33 | 0.6349 | 0.8485 |
| [0.667, 0.733) | 15 | 0.6946 | 1.0000 | 47 | 0.6996 | 0.7872 |
| [0.733, 0.800) | 6 | 0.7653 | 0.8333 | 46 | 0.7704 | 0.7609 |
| [0.800, 0.867) | 1 | 0.8027 | 1.0000 | 29 | 0.8298 | 0.8276 |
| [0.867, 0.933) | 0 | n/a | n/a | 19 | 0.8969 | 0.8947 |
| [0.933, 1.000) | 0 | n/a | n/a | 5 | 0.9522 | 1.0000 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 4 | 0.3186 | 0.7500 | 0 | n/a | n/a |
| [0.333, 0.400) | 28 | 0.3726 | 0.8929 | 0 | n/a | n/a |
| [0.400, 0.467) | 92 | 0.4378 | 0.9022 | 0 | n/a | n/a |
| [0.467, 0.533) | 109 | 0.4967 | 0.9450 | 2 | 0.4998 | 0.5000 |
| [0.533, 0.600) | 56 | 0.5552 | 1.0000 | 2 | 0.5594 | 0.5000 |
| [0.600, 0.667) | 5 | 0.6191 | 1.0000 | 6 | 0.6308 | 1.0000 |
| [0.667, 0.733) | 1 | 0.6853 | 1.0000 | 5 | 0.7098 | 0.6000 |
| [0.733, 0.800) | 0 | n/a | n/a | 15 | 0.7719 | 1.0000 |
| [0.800, 0.867) | 0 | n/a | n/a | 24 | 0.8352 | 0.9167 |
| [0.867, 0.933) | 0 | n/a | n/a | 79 | 0.9078 | 0.8861 |
| [0.933, 1.000) | 0 | n/a | n/a | 162 | 0.9622 | 0.9753 |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 5 | 0.3214 | 0.0000 | 5 | 0.3214 | 0.0000 |
| [0.333, 0.400) | 16 | 0.3756 | 0.0625 | 16 | 0.3756 | 0.0625 |
| [0.400, 0.467) | 24 | 0.4317 | 0.0000 | 24 | 0.4317 | 0.0000 |
| [0.467, 0.533) | 38 | 0.4974 | 0.1053 | 38 | 0.4974 | 0.1053 |
| [0.533, 0.600) | 35 | 0.5618 | 0.0000 | 35 | 0.5618 | 0.0000 |
| [0.600, 0.667) | 41 | 0.6325 | 0.0732 | 41 | 0.6325 | 0.0732 |
| [0.667, 0.733) | 41 | 0.7021 | 0.0244 | 41 | 0.7021 | 0.0244 |
| [0.733, 0.800) | 33 | 0.7712 | 0.0000 | 33 | 0.7712 | 0.0000 |
| [0.800, 0.867) | 35 | 0.8323 | 0.0000 | 35 | 0.8323 | 0.0000 |
| [0.867, 0.933) | 18 | 0.8991 | 0.0000 | 18 | 0.8991 | 0.0000 |
| [0.933, 1.000) | 9 | 0.9506 | 0.0000 | 9 | 0.9507 | 0.0000 |

### A / qs_v2, test

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.1091 | 0.0164 | 0.1308 | 0.1062 | 0.7442 | 0.7442 |
| has_phi_direct | 0.2194 | 0.0128 | 0.1617 | 0.0591 | 0.8828 | 0.8828 |
| has_phi_quasi | 0.2623 | 0.0194 | 0.2403 | 0.0965 | 0.7697 | 0.7697 |
| has_coded_id | 0.2624 | 0.0369 | 0.2466 | 0.1085 | 0.7345 | 0.7345 |
| has_staff_pii = raw (T fallback) | 0.1432 | 0.1432 | 0.5307 | 0.5307 | 0.4397 | 0.4397 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 23 | 0.5182 | 0.6087 | 13 | 0.5205 | 0.6923 |
| [0.533, 0.600) | 29 | 0.5740 | 0.5517 | 17 | 0.5597 | 0.4118 |
| [0.600, 0.667) | 39 | 0.6379 | 0.6154 | 18 | 0.6416 | 0.6111 |
| [0.667, 0.733) | 76 | 0.7062 | 0.7500 | 23 | 0.7014 | 0.6522 |
| [0.733, 0.800) | 267 | 0.7747 | 0.9139 | 33 | 0.7680 | 0.7273 |
| [0.800, 0.867) | 979 | 0.8380 | 0.9724 | 75 | 0.8394 | 0.7467 |
| [0.867, 0.933) | 574 | 0.8881 | 0.9634 | 380 | 0.9105 | 0.9263 |
| [0.933, 1.000) | 19 | 0.9463 | 0.9474 | 1447 | 0.9619 | 0.9703 |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 36 | 0.5185 | 0.5278 | 9 | 0.5198 | 0.5556 |
| [0.533, 0.600) | 84 | 0.5683 | 0.6786 | 15 | 0.5716 | 0.4000 |
| [0.600, 0.667) | 172 | 0.6405 | 0.8953 | 21 | 0.6283 | 0.6190 |
| [0.667, 0.733) | 495 | 0.7043 | 0.9859 | 25 | 0.7005 | 0.6400 |
| [0.733, 0.800) | 796 | 0.7662 | 0.9925 | 29 | 0.7666 | 0.8276 |
| [0.800, 0.867) | 372 | 0.8253 | 0.9919 | 47 | 0.8366 | 0.6383 |
| [0.867, 0.933) | 46 | 0.8906 | 1.0000 | 110 | 0.9091 | 0.9182 |
| [0.933, 1.000) | 5 | 0.9594 | 1.0000 | 1750 | 0.9852 | 0.9903 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 59 | 0.5186 | 0.4915 | 10 | 0.5147 | 0.6000 |
| [0.533, 0.600) | 208 | 0.5648 | 0.7981 | 25 | 0.5671 | 0.3600 |
| [0.600, 0.667) | 513 | 0.6364 | 0.9649 | 43 | 0.6384 | 0.6047 |
| [0.667, 0.733) | 761 | 0.6985 | 0.9763 | 61 | 0.7036 | 0.7213 |
| [0.733, 0.800) | 395 | 0.7595 | 0.9772 | 70 | 0.7676 | 0.8429 |
| [0.800, 0.867) | 61 | 0.8223 | 0.9672 | 78 | 0.8407 | 0.9103 |
| [0.867, 0.933) | 7 | 0.8915 | 0.7143 | 285 | 0.9050 | 0.9579 |
| [0.933, 1.000) | 2 | 0.9567 | 1.0000 | 1434 | 0.9773 | 0.9742 |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 67 | 0.5160 | 0.5821 | 18 | 0.5184 | 0.5000 |
| [0.533, 0.600) | 238 | 0.5725 | 0.8824 | 38 | 0.5612 | 0.5789 |
| [0.600, 0.667) | 529 | 0.6369 | 0.9357 | 42 | 0.6355 | 0.7857 |
| [0.667, 0.733) | 759 | 0.6997 | 0.9802 | 62 | 0.7022 | 0.8226 |
| [0.733, 0.800) | 329 | 0.7585 | 0.9605 | 115 | 0.7682 | 0.9217 |
| [0.800, 0.867) | 73 | 0.8272 | 0.9589 | 202 | 0.8388 | 0.9010 |
| [0.867, 0.933) | 9 | 0.8933 | 1.0000 | 434 | 0.9053 | 0.9562 |
| [0.933, 1.000) | 2 | 0.9725 | 1.0000 | 1095 | 0.9680 | 0.9744 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 358 | 0.5160 | 0.5084 | 358 | 0.5160 | 0.5084 |
| [0.533, 0.600) | 623 | 0.5662 | 0.6902 | 623 | 0.5662 | 0.6902 |
| [0.600, 0.667) | 496 | 0.6303 | 0.7137 | 496 | 0.6303 | 0.7137 |
| [0.667, 0.733) | 281 | 0.6956 | 0.5587 | 281 | 0.6956 | 0.5587 |
| [0.733, 0.800) | 141 | 0.7602 | 0.3191 | 141 | 0.7602 | 0.3191 |
| [0.800, 0.867) | 67 | 0.8264 | 0.3134 | 67 | 0.8264 | 0.3134 |
| [0.867, 0.933) | 36 | 0.8882 | 0.1389 | 36 | 0.8882 | 0.1389 |
| [0.933, 1.000) | 4 | 0.9443 | 0.0000 | 4 | 0.9443 | 0.0000 |

### A / qs_v2, holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.0903 | 0.0345 | 0.1443 | 0.1278 | 0.5769 | 0.5769 |
| has_phi_direct | 0.2429 | 0.0223 | 0.1307 | 0.0083 | 0.9974 | 0.9974 |
| has_phi_quasi | 0.2918 | 0.0488 | 0.2083 | 0.0374 | 0.9416 | 0.9416 |
| has_coded_id | 0.2968 | 0.0728 | 0.2225 | 0.0530 | 0.8027 | 0.8027 |
| has_staff_pii = raw (T fallback) | 0.1505 | 0.1505 | 0.5231 | 0.5231 | 0.4374 | 0.4374 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.600, 0.667) | 3 | 0.6448 | 1.0000 | 0 | n/a | n/a |
| [0.667, 0.733) | 8 | 0.7136 | 0.8750 | 1 | 0.6984 | 1.0000 |
| [0.733, 0.800) | 38 | 0.7793 | 0.9211 | 3 | 0.7726 | 1.0000 |
| [0.800, 0.867) | 156 | 0.8389 | 0.9231 | 8 | 0.8453 | 0.8750 |
| [0.867, 0.933) | 87 | 0.8897 | 0.9540 | 54 | 0.9128 | 0.9444 |
| [0.933, 1.000) | 3 | 0.9414 | 1.0000 | 229 | 0.9618 | 0.9301 |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 3 | 0.5150 | 0.3333 | 2 | 0.5272 | 0.5000 |
| [0.533, 0.600) | 1 | 0.5799 | 1.0000 | 0 | n/a | n/a |
| [0.600, 0.667) | 21 | 0.6433 | 1.0000 | 1 | 0.6238 | 0.0000 |
| [0.667, 0.733) | 87 | 0.7066 | 1.0000 | 0 | n/a | n/a |
| [0.733, 0.800) | 113 | 0.7646 | 1.0000 | 1 | 0.7845 | 1.0000 |
| [0.800, 0.867) | 52 | 0.8260 | 1.0000 | 3 | 0.8555 | 1.0000 |
| [0.867, 0.933) | 18 | 0.8876 | 1.0000 | 14 | 0.9158 | 1.0000 |
| [0.933, 1.000) | 0 | n/a | n/a | 274 | 0.9852 | 1.0000 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 10 | 0.5168 | 0.4000 | 3 | 0.5235 | 0.0000 |
| [0.533, 0.600) | 22 | 0.5764 | 0.9545 | 4 | 0.5824 | 0.7500 |
| [0.600, 0.667) | 77 | 0.6408 | 1.0000 | 3 | 0.6130 | 0.3333 |
| [0.667, 0.733) | 110 | 0.6996 | 0.9909 | 4 | 0.7134 | 1.0000 |
| [0.733, 0.800) | 55 | 0.7573 | 1.0000 | 7 | 0.7648 | 0.8571 |
| [0.800, 0.867) | 16 | 0.8158 | 1.0000 | 17 | 0.8489 | 1.0000 |
| [0.867, 0.933) | 5 | 0.8802 | 1.0000 | 34 | 0.9129 | 1.0000 |
| [0.933, 1.000) | 0 | n/a | n/a | 223 | 0.9777 | 0.9955 |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 7 | 0.5112 | 0.4286 | 3 | 0.5222 | 0.0000 |
| [0.533, 0.600) | 28 | 0.5773 | 0.9286 | 4 | 0.5541 | 0.7500 |
| [0.600, 0.667) | 92 | 0.6396 | 1.0000 | 1 | 0.6467 | 1.0000 |
| [0.667, 0.733) | 111 | 0.6994 | 0.9910 | 6 | 0.7029 | 0.8333 |
| [0.733, 0.800) | 43 | 0.7636 | 0.9767 | 15 | 0.7615 | 0.9333 |
| [0.800, 0.867) | 14 | 0.8240 | 1.0000 | 29 | 0.8348 | 1.0000 |
| [0.867, 0.933) | 0 | n/a | n/a | 71 | 0.9017 | 1.0000 |
| [0.933, 1.000) | 0 | n/a | n/a | 166 | 0.9660 | 0.9880 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 42 | 0.5171 | 0.5952 | 42 | 0.5171 | 0.5952 |
| [0.533, 0.600) | 90 | 0.5698 | 0.6667 | 90 | 0.5698 | 0.6667 |
| [0.600, 0.667) | 61 | 0.6287 | 0.7541 | 61 | 0.6287 | 0.7541 |
| [0.667, 0.733) | 43 | 0.6941 | 0.6744 | 43 | 0.6941 | 0.6744 |
| [0.733, 0.800) | 29 | 0.7637 | 0.3448 | 29 | 0.7637 | 0.3448 |
| [0.800, 0.867) | 18 | 0.8247 | 0.6111 | 18 | 0.8247 | 0.6111 |
| [0.867, 0.933) | 9 | 0.8987 | 0.2222 | 9 | 0.8987 | 0.2222 |
| [0.933, 1.000) | 3 | 0.9446 | 0.3333 | 3 | 0.9446 | 0.3333 |

### B1 / qs_v1, test

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.7482 | 0.7482 | 1.4231 | 1.4231 | 0.3587 | 0.3587 |
| subject_role = raw (T fallback) | 0.4953 | 0.4953 | 1.1482 | 1.1482 | 0.4285 | 0.4285 |
| category | 0.1715 | 0.1781 | 0.7060 | 0.6988 | 0.4944 | 0.4896 |
| doc_kind = raw (T fallback) | 0.3594 | 0.3594 | 1.0035 | 1.0035 | 0.4924 | 0.4924 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 4 | 0.5136 | 0.7500 | 4 | 0.5136 | 0.7500 |
| [0.533, 0.600) | 14 | 0.5752 | 0.6429 | 14 | 0.5752 | 0.6429 |
| [0.600, 0.667) | 10 | 0.6393 | 0.4000 | 10 | 0.6393 | 0.4000 |
| [0.667, 0.733) | 17 | 0.6928 | 0.2353 | 17 | 0.6928 | 0.2353 |
| [0.733, 0.800) | 33 | 0.7745 | 0.2121 | 33 | 0.7745 | 0.2121 |
| [0.800, 0.867) | 52 | 0.8400 | 0.3077 | 52 | 0.8400 | 0.3077 |
| [0.867, 0.933) | 192 | 0.9049 | 0.1615 | 192 | 0.9049 | 0.1615 |
| [0.933, 1.000) | 351 | 0.9587 | 0.0969 | 351 | 0.9587 | 0.0969 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 18 | 0.3098 | 0.3333 | 18 | 0.3099 | 0.3333 |
| [0.333, 0.400) | 54 | 0.3702 | 0.2222 | 54 | 0.3702 | 0.2222 |
| [0.400, 0.467) | 68 | 0.4341 | 0.2500 | 68 | 0.4341 | 0.2500 |
| [0.467, 0.533) | 75 | 0.4993 | 0.1733 | 75 | 0.4993 | 0.1733 |
| [0.533, 0.600) | 81 | 0.5700 | 0.1852 | 81 | 0.5700 | 0.1852 |
| [0.600, 0.667) | 48 | 0.6373 | 0.1667 | 48 | 0.6373 | 0.1667 |
| [0.667, 0.733) | 54 | 0.6963 | 0.1111 | 54 | 0.6963 | 0.1111 |
| [0.733, 0.800) | 48 | 0.7670 | 0.1250 | 48 | 0.7670 | 0.1250 |
| [0.800, 0.867) | 53 | 0.8350 | 0.2642 | 53 | 0.8350 | 0.2642 |
| [0.867, 0.933) | 66 | 0.8983 | 0.1818 | 66 | 0.8983 | 0.1818 |
| [0.933, 1.000) | 108 | 0.9746 | 0.1019 | 108 | 0.9746 | 0.1019 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 13 | 0.2537 | 0.3846 | 25 | 0.2495 | 0.3600 |
| [0.267, 0.333) | 61 | 0.3062 | 0.4754 | 141 | 0.3058 | 0.5177 |
| [0.333, 0.400) | 137 | 0.3679 | 0.4672 | 149 | 0.3646 | 0.4765 |
| [0.400, 0.467) | 107 | 0.4351 | 0.5234 | 101 | 0.4282 | 0.6337 |
| [0.467, 0.533) | 79 | 0.5014 | 0.6076 | 76 | 0.4975 | 0.4079 |
| [0.533, 0.600) | 61 | 0.5685 | 0.5082 | 50 | 0.5651 | 0.5200 |
| [0.600, 0.667) | 44 | 0.6270 | 0.3636 | 41 | 0.6298 | 0.4634 |
| [0.667, 0.733) | 47 | 0.6957 | 0.6170 | 24 | 0.7050 | 0.3333 |
| [0.733, 0.800) | 37 | 0.7618 | 0.4054 | 24 | 0.7632 | 0.4583 |
| [0.800, 0.867) | 29 | 0.8402 | 0.3793 | 18 | 0.8311 | 0.5556 |
| [0.867, 0.933) | 29 | 0.9007 | 0.5517 | 7 | 0.8922 | 0.4286 |
| [0.933, 1.000) | 29 | 0.9760 | 0.4138 | 17 | 0.9683 | 0.4118 |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 9 | 0.2604 | 0.3333 | 9 | 0.2604 | 0.3333 |
| [0.267, 0.333) | 51 | 0.3090 | 0.2353 | 51 | 0.3090 | 0.2353 |
| [0.333, 0.400) | 92 | 0.3700 | 0.2500 | 92 | 0.3700 | 0.2500 |
| [0.400, 0.467) | 79 | 0.4332 | 0.2152 | 79 | 0.4332 | 0.2152 |
| [0.467, 0.533) | 64 | 0.4980 | 0.2656 | 64 | 0.4980 | 0.2656 |
| [0.533, 0.600) | 72 | 0.5630 | 0.3472 | 72 | 0.5630 | 0.3472 |
| [0.600, 0.667) | 57 | 0.6323 | 0.2632 | 57 | 0.6322 | 0.2632 |
| [0.667, 0.733) | 41 | 0.7013 | 0.2683 | 41 | 0.7013 | 0.2683 |
| [0.733, 0.800) | 34 | 0.7664 | 0.2647 | 34 | 0.7664 | 0.2647 |
| [0.800, 0.867) | 31 | 0.8305 | 0.3548 | 31 | 0.8305 | 0.3548 |
| [0.867, 0.933) | 37 | 0.9037 | 0.3243 | 37 | 0.9038 | 0.3243 |
| [0.933, 1.000) | 106 | 0.9885 | 0.1698 | 106 | 0.9885 | 0.1698 |

### B1 / qs_v1, holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.7023 | 0.7023 | 1.3349 | 1.3349 | 0.2711 | 0.2711 |
| subject_role = raw (T fallback) | 0.3399 | 0.3398 | 0.9496 | 0.9496 | 0.4696 | 0.4696 |
| category | 0.1843 | 0.2241 | 0.5741 | 0.5923 | 0.5788 | 0.5763 |
| doc_kind = raw (T fallback) | 0.3311 | 0.3311 | 0.8765 | 0.8765 | 0.4103 | 0.4103 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.533, 0.600) | 1 | 0.5810 | 0.0000 | 1 | 0.5810 | 0.0000 |
| [0.600, 0.667) | 2 | 0.6303 | 1.0000 | 2 | 0.6303 | 1.0000 |
| [0.667, 0.733) | 3 | 0.6877 | 0.3333 | 3 | 0.6877 | 0.3333 |
| [0.733, 0.800) | 7 | 0.7688 | 0.2857 | 7 | 0.7688 | 0.2857 |
| [0.800, 0.867) | 11 | 0.8439 | 0.4545 | 11 | 0.8439 | 0.4545 |
| [0.867, 0.933) | 29 | 0.9054 | 0.2414 | 29 | 0.9054 | 0.2414 |
| [0.933, 1.000) | 46 | 0.9613 | 0.0870 | 46 | 0.9613 | 0.0870 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 2 | 0.3246 | 0.5000 | 2 | 0.3247 | 0.5000 |
| [0.333, 0.400) | 13 | 0.3706 | 0.3077 | 13 | 0.3706 | 0.3077 |
| [0.400, 0.467) | 12 | 0.4322 | 0.2500 | 12 | 0.4322 | 0.2500 |
| [0.467, 0.533) | 10 | 0.5054 | 0.3000 | 10 | 0.5054 | 0.3000 |
| [0.533, 0.600) | 11 | 0.5723 | 0.2727 | 11 | 0.5723 | 0.2727 |
| [0.600, 0.667) | 11 | 0.6331 | 0.4545 | 11 | 0.6331 | 0.4545 |
| [0.667, 0.733) | 8 | 0.7035 | 0.5000 | 8 | 0.7035 | 0.5000 |
| [0.733, 0.800) | 9 | 0.7731 | 0.2222 | 9 | 0.7731 | 0.2222 |
| [0.800, 0.867) | 6 | 0.8383 | 0.3333 | 6 | 0.8383 | 0.3333 |
| [0.867, 0.933) | 3 | 0.8917 | 0.3333 | 3 | 0.8917 | 0.3333 |
| [0.933, 1.000) | 14 | 0.9777 | 0.1429 | 14 | 0.9777 | 0.1429 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 0 | n/a | n/a | 1 | 0.2529 | 0.0000 |
| [0.267, 0.333) | 9 | 0.3125 | 0.4444 | 24 | 0.3064 | 0.5417 |
| [0.333, 0.400) | 20 | 0.3629 | 0.6000 | 16 | 0.3719 | 0.4375 |
| [0.400, 0.467) | 11 | 0.4425 | 0.3636 | 17 | 0.4220 | 0.6471 |
| [0.467, 0.533) | 16 | 0.4918 | 0.5625 | 18 | 0.4933 | 0.7778 |
| [0.533, 0.600) | 14 | 0.5772 | 0.8571 | 5 | 0.5835 | 0.2000 |
| [0.600, 0.667) | 6 | 0.6181 | 0.6667 | 8 | 0.6300 | 0.8750 |
| [0.667, 0.733) | 9 | 0.7130 | 0.4444 | 2 | 0.6945 | 0.5000 |
| [0.733, 0.800) | 4 | 0.7782 | 1.0000 | 5 | 0.7580 | 0.6000 |
| [0.800, 0.867) | 4 | 0.8399 | 0.5000 | 2 | 0.8210 | 1.0000 |
| [0.867, 0.933) | 5 | 0.8975 | 0.8000 | 1 | 0.8749 | 0.0000 |
| [0.933, 1.000) | 1 | 0.9543 | 0.0000 | 0 | n/a | n/a |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 1 | 0.2553 | 1.0000 | 1 | 0.2553 | 1.0000 |
| [0.267, 0.333) | 4 | 0.3164 | 0.5000 | 4 | 0.3164 | 0.5000 |
| [0.333, 0.400) | 10 | 0.3679 | 0.1000 | 10 | 0.3679 | 0.1000 |
| [0.400, 0.467) | 12 | 0.4256 | 0.5833 | 12 | 0.4256 | 0.5833 |
| [0.467, 0.533) | 11 | 0.5064 | 0.3636 | 11 | 0.5064 | 0.3636 |
| [0.533, 0.600) | 13 | 0.5641 | 0.3077 | 13 | 0.5641 | 0.3077 |
| [0.600, 0.667) | 8 | 0.6266 | 0.6250 | 8 | 0.6266 | 0.6250 |
| [0.667, 0.733) | 10 | 0.7058 | 0.4000 | 10 | 0.7058 | 0.4000 |
| [0.733, 0.800) | 8 | 0.7655 | 0.5000 | 8 | 0.7655 | 0.5000 |
| [0.800, 0.867) | 9 | 0.8299 | 0.2222 | 9 | 0.8299 | 0.2222 |
| [0.867, 0.933) | 7 | 0.9033 | 0.1429 | 7 | 0.9033 | 0.1429 |
| [0.933, 1.000) | 6 | 0.9735 | 0.0000 | 6 | 0.9735 | 0.0000 |

### B1 / qs_v2, test

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.7463 | 0.7463 | 1.4237 | 1.4237 | 0.3595 | 0.3595 |
| has_phi_direct = raw (T fallback) | 0.6755 | 0.6755 | 1.2225 | 1.2225 | 0.3116 | 0.3116 |
| has_phi_quasi = raw (T fallback) | 0.6455 | 0.6455 | 1.2071 | 1.2071 | 0.3297 | 0.3297 |
| has_coded_id = raw (T fallback) | 0.6376 | 0.6376 | 1.1688 | 1.1688 | 0.3619 | 0.3619 |
| has_staff_pii = raw (T fallback) | 0.6807 | 0.6807 | 1.2390 | 1.2390 | 0.2965 | 0.2965 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 3 | 0.5114 | 0.6667 | 3 | 0.5114 | 0.6667 |
| [0.533, 0.600) | 13 | 0.5749 | 0.6154 | 13 | 0.5749 | 0.6154 |
| [0.600, 0.667) | 11 | 0.6315 | 0.6364 | 11 | 0.6315 | 0.6364 |
| [0.667, 0.733) | 19 | 0.6969 | 0.1579 | 19 | 0.6969 | 0.1579 |
| [0.733, 0.800) | 28 | 0.7760 | 0.2143 | 28 | 0.7760 | 0.2143 |
| [0.800, 0.867) | 60 | 0.8383 | 0.2667 | 60 | 0.8383 | 0.2667 |
| [0.867, 0.933) | 190 | 0.9067 | 0.1632 | 190 | 0.9067 | 0.1632 |
| [0.933, 1.000) | 349 | 0.9589 | 0.1003 | 349 | 0.9589 | 0.1003 |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 21 | 0.5158 | 0.4286 | 21 | 0.5158 | 0.4286 |
| [0.533, 0.600) | 41 | 0.5684 | 0.4146 | 41 | 0.5684 | 0.4146 |
| [0.600, 0.667) | 39 | 0.6327 | 0.2821 | 39 | 0.6327 | 0.2821 |
| [0.667, 0.733) | 71 | 0.7029 | 0.1972 | 71 | 0.7029 | 0.1972 |
| [0.733, 0.800) | 83 | 0.7708 | 0.0602 | 83 | 0.7708 | 0.0602 |
| [0.800, 0.867) | 135 | 0.8387 | 0.0963 | 135 | 0.8387 | 0.0963 |
| [0.867, 0.933) | 186 | 0.8995 | 0.0699 | 186 | 0.8995 | 0.0699 |
| [0.933, 1.000) | 97 | 0.9523 | 0.0928 | 97 | 0.9523 | 0.0928 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 12 | 0.5165 | 0.5000 | 12 | 0.5165 | 0.5000 |
| [0.533, 0.600) | 32 | 0.5672 | 0.5000 | 32 | 0.5672 | 0.5000 |
| [0.600, 0.667) | 47 | 0.6382 | 0.3830 | 47 | 0.6382 | 0.3830 |
| [0.667, 0.733) | 58 | 0.6999 | 0.2759 | 58 | 0.6999 | 0.2759 |
| [0.733, 0.800) | 73 | 0.7646 | 0.1781 | 73 | 0.7646 | 0.1781 |
| [0.800, 0.867) | 130 | 0.8363 | 0.1154 | 130 | 0.8363 | 0.1154 |
| [0.867, 0.933) | 192 | 0.9007 | 0.1042 | 192 | 0.9007 | 0.1042 |
| [0.933, 1.000) | 129 | 0.9539 | 0.1318 | 129 | 0.9539 | 0.1318 |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 18 | 0.5137 | 0.5556 | 18 | 0.5137 | 0.5556 |
| [0.533, 0.600) | 36 | 0.5655 | 0.3333 | 36 | 0.5655 | 0.3333 |
| [0.600, 0.667) | 41 | 0.6355 | 0.3171 | 41 | 0.6355 | 0.3171 |
| [0.667, 0.733) | 73 | 0.6968 | 0.2877 | 73 | 0.6968 | 0.2877 |
| [0.733, 0.800) | 86 | 0.7675 | 0.1395 | 86 | 0.7675 | 0.1395 |
| [0.800, 0.867) | 133 | 0.8350 | 0.1203 | 133 | 0.8350 | 0.1203 |
| [0.867, 0.933) | 183 | 0.9009 | 0.1038 | 183 | 0.9009 | 0.1038 |
| [0.933, 1.000) | 103 | 0.9529 | 0.1553 | 103 | 0.9529 | 0.1553 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 17 | 0.5150 | 0.6471 | 17 | 0.5150 | 0.6471 |
| [0.533, 0.600) | 31 | 0.5729 | 0.4516 | 31 | 0.5729 | 0.4516 |
| [0.600, 0.667) | 45 | 0.6355 | 0.2444 | 45 | 0.6355 | 0.2444 |
| [0.667, 0.733) | 57 | 0.7028 | 0.2456 | 57 | 0.7028 | 0.2456 |
| [0.733, 0.800) | 78 | 0.7695 | 0.1667 | 78 | 0.7695 | 0.1667 |
| [0.800, 0.867) | 140 | 0.8357 | 0.0714 | 140 | 0.8357 | 0.0714 |
| [0.867, 0.933) | 190 | 0.8995 | 0.0842 | 190 | 0.8995 | 0.0842 |
| [0.933, 1.000) | 115 | 0.9521 | 0.0870 | 115 | 0.9521 | 0.0870 |

### B1 / qs_v2, holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.6871 | 0.6871 | 1.3337 | 1.3337 | 0.2766 | 0.2766 |
| has_phi_direct = raw (T fallback) | 0.7332 | 0.7332 | 1.2728 | 1.2728 | 0.1126 | 0.1126 |
| has_phi_quasi = raw (T fallback) | 0.7319 | 0.7319 | 1.2838 | 1.2838 | 0.0989 | 0.0989 |
| has_coded_id = raw (T fallback) | 0.7379 | 0.7379 | 1.2573 | 1.2573 | 0.2599 | 0.2599 |
| has_staff_pii = raw (T fallback) | 0.5569 | 0.5569 | 1.0783 | 1.0783 | 0.3376 | 0.3376 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.533, 0.600) | 2 | 0.5781 | 0.5000 | 2 | 0.5781 | 0.5000 |
| [0.667, 0.733) | 4 | 0.6844 | 0.5000 | 4 | 0.6844 | 0.5000 |
| [0.733, 0.800) | 7 | 0.7725 | 0.2857 | 7 | 0.7725 | 0.2857 |
| [0.800, 0.867) | 11 | 0.8432 | 0.4545 | 11 | 0.8432 | 0.4545 |
| [0.867, 0.933) | 30 | 0.9061 | 0.2333 | 30 | 0.9061 | 0.2333 |
| [0.933, 1.000) | 45 | 0.9614 | 0.0889 | 45 | 0.9614 | 0.0889 |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 1 | 0.5088 | 1.0000 | 1 | 0.5088 | 1.0000 |
| [0.533, 0.600) | 7 | 0.5567 | 0.2857 | 7 | 0.5567 | 0.2857 |
| [0.600, 0.667) | 3 | 0.6511 | 0.3333 | 3 | 0.6511 | 0.3333 |
| [0.667, 0.733) | 16 | 0.7011 | 0.1250 | 16 | 0.7011 | 0.1250 |
| [0.733, 0.800) | 15 | 0.7748 | 0.1333 | 15 | 0.7748 | 0.1333 |
| [0.800, 0.867) | 23 | 0.8354 | 0.0000 | 23 | 0.8354 | 0.0000 |
| [0.867, 0.933) | 22 | 0.8984 | 0.0000 | 22 | 0.8984 | 0.0000 |
| [0.933, 1.000) | 12 | 0.9527 | 0.0000 | 12 | 0.9527 | 0.0000 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 7 | 0.5176 | 0.7143 | 7 | 0.5176 | 0.7143 |
| [0.600, 0.667) | 8 | 0.6291 | 0.3750 | 8 | 0.6291 | 0.3750 |
| [0.667, 0.733) | 13 | 0.7079 | 0.0000 | 13 | 0.7079 | 0.0000 |
| [0.733, 0.800) | 13 | 0.7647 | 0.0000 | 13 | 0.7647 | 0.0000 |
| [0.800, 0.867) | 19 | 0.8419 | 0.1053 | 19 | 0.8419 | 0.1053 |
| [0.867, 0.933) | 27 | 0.9056 | 0.0000 | 27 | 0.9056 | 0.0000 |
| [0.933, 1.000) | 12 | 0.9545 | 0.0000 | 12 | 0.9545 | 0.0000 |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 3 | 0.5184 | 0.3333 | 3 | 0.5184 | 0.3333 |
| [0.533, 0.600) | 5 | 0.5790 | 0.2000 | 5 | 0.5790 | 0.2000 |
| [0.600, 0.667) | 4 | 0.6268 | 0.5000 | 4 | 0.6268 | 0.5000 |
| [0.667, 0.733) | 17 | 0.6994 | 0.0000 | 17 | 0.6994 | 0.0000 |
| [0.733, 0.800) | 13 | 0.7647 | 0.0000 | 13 | 0.7647 | 0.0000 |
| [0.800, 0.867) | 26 | 0.8407 | 0.0385 | 26 | 0.8407 | 0.0385 |
| [0.867, 0.933) | 20 | 0.8960 | 0.0500 | 20 | 0.8960 | 0.0500 |
| [0.933, 1.000) | 11 | 0.9539 | 0.0000 | 11 | 0.9539 | 0.0000 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 6 | 0.5200 | 0.5000 | 6 | 0.5200 | 0.5000 |
| [0.533, 0.600) | 3 | 0.5825 | 0.3333 | 3 | 0.5825 | 0.3333 |
| [0.600, 0.667) | 2 | 0.6221 | 0.5000 | 2 | 0.6221 | 0.5000 |
| [0.667, 0.733) | 14 | 0.7032 | 0.2857 | 14 | 0.7032 | 0.2857 |
| [0.733, 0.800) | 11 | 0.7739 | 0.0909 | 11 | 0.7739 | 0.0909 |
| [0.800, 0.867) | 24 | 0.8266 | 0.4583 | 24 | 0.8266 | 0.4583 |
| [0.867, 0.933) | 27 | 0.9030 | 0.1481 | 27 | 0.9030 | 0.1481 |
| [0.933, 1.000) | 12 | 0.9540 | 0.0000 | 12 | 0.9540 | 0.0000 |

### B2 / qs_v1, test

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.6113 | 0.6113 | 1.1852 | 1.1852 | 0.4476 | 0.4476 |
| subject_role = raw (T fallback) | 0.4483 | 0.4483 | 1.0845 | 1.0845 | 0.5250 | 0.5250 |
| category | 0.1772 | 0.1318 | 0.7745 | 0.7461 | 0.4900 | 0.4859 |
| doc_kind = raw (T fallback) | 0.3703 | 0.3703 | 1.0251 | 1.0251 | 0.4609 | 0.4608 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 2 | 0.5183 | 0.5000 | 2 | 0.5183 | 0.5000 |
| [0.533, 0.600) | 7 | 0.5703 | 0.5714 | 7 | 0.5703 | 0.5714 |
| [0.600, 0.667) | 8 | 0.6319 | 0.2500 | 8 | 0.6319 | 0.2500 |
| [0.667, 0.733) | 9 | 0.7072 | 0.5556 | 9 | 0.7072 | 0.5556 |
| [0.733, 0.800) | 10 | 0.7758 | 0.4000 | 10 | 0.7758 | 0.4000 |
| [0.800, 0.867) | 48 | 0.8382 | 0.3333 | 48 | 0.8382 | 0.3333 |
| [0.867, 0.933) | 126 | 0.9044 | 0.2063 | 126 | 0.9044 | 0.2063 |
| [0.933, 1.000) | 110 | 0.9563 | 0.2727 | 110 | 0.9563 | 0.2727 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 10 | 0.3131 | 0.3000 | 10 | 0.3131 | 0.3000 |
| [0.333, 0.400) | 27 | 0.3680 | 0.1852 | 27 | 0.3680 | 0.1852 |
| [0.400, 0.467) | 38 | 0.4286 | 0.2368 | 38 | 0.4286 | 0.2368 |
| [0.467, 0.533) | 42 | 0.5003 | 0.1190 | 42 | 0.5003 | 0.1190 |
| [0.533, 0.600) | 34 | 0.5604 | 0.2059 | 34 | 0.5604 | 0.2059 |
| [0.600, 0.667) | 22 | 0.6306 | 0.1818 | 22 | 0.6306 | 0.1818 |
| [0.667, 0.733) | 15 | 0.6909 | 0.1333 | 15 | 0.6909 | 0.1333 |
| [0.733, 0.800) | 32 | 0.7694 | 0.2500 | 32 | 0.7694 | 0.2500 |
| [0.800, 0.867) | 18 | 0.8338 | 0.2778 | 18 | 0.8338 | 0.2778 |
| [0.867, 0.933) | 36 | 0.9001 | 0.1944 | 36 | 0.9001 | 0.1944 |
| [0.933, 1.000) | 46 | 0.9728 | 0.2609 | 46 | 0.9728 | 0.2609 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 5 | 0.2455 | 0.6000 | 13 | 0.2463 | 0.3846 |
| [0.267, 0.333) | 36 | 0.3124 | 0.3333 | 75 | 0.2985 | 0.4133 |
| [0.333, 0.400) | 43 | 0.3652 | 0.4419 | 66 | 0.3652 | 0.4545 |
| [0.400, 0.467) | 49 | 0.4350 | 0.4694 | 54 | 0.4270 | 0.3704 |
| [0.467, 0.533) | 39 | 0.4992 | 0.4103 | 47 | 0.4928 | 0.5106 |
| [0.533, 0.600) | 37 | 0.5645 | 0.3514 | 18 | 0.5572 | 0.3333 |
| [0.600, 0.667) | 33 | 0.6330 | 0.5455 | 12 | 0.6366 | 0.5000 |
| [0.667, 0.733) | 24 | 0.6981 | 0.4167 | 15 | 0.6999 | 0.4000 |
| [0.733, 0.800) | 10 | 0.7680 | 0.4000 | 7 | 0.7509 | 0.2857 |
| [0.800, 0.867) | 15 | 0.8376 | 0.3333 | 5 | 0.8175 | 0.4000 |
| [0.867, 0.933) | 17 | 0.8967 | 0.4706 | 4 | 0.8902 | 0.0000 |
| [0.933, 1.000) | 12 | 0.9749 | 0.1667 | 4 | 0.9753 | 0.2500 |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 3 | 0.2589 | 0.0000 | 3 | 0.2589 | 0.0000 |
| [0.267, 0.333) | 19 | 0.3114 | 0.3158 | 19 | 0.3114 | 0.3158 |
| [0.333, 0.400) | 29 | 0.3706 | 0.3103 | 29 | 0.3706 | 0.3103 |
| [0.400, 0.467) | 39 | 0.4336 | 0.2821 | 39 | 0.4336 | 0.2821 |
| [0.467, 0.533) | 36 | 0.5004 | 0.3611 | 36 | 0.5004 | 0.3611 |
| [0.533, 0.600) | 23 | 0.5658 | 0.3913 | 23 | 0.5658 | 0.3913 |
| [0.600, 0.667) | 26 | 0.6332 | 0.3462 | 26 | 0.6332 | 0.3462 |
| [0.667, 0.733) | 20 | 0.6969 | 0.3000 | 20 | 0.6969 | 0.3000 |
| [0.733, 0.800) | 22 | 0.7671 | 0.2727 | 22 | 0.7671 | 0.2727 |
| [0.800, 0.867) | 14 | 0.8376 | 0.2143 | 14 | 0.8376 | 0.2143 |
| [0.867, 0.933) | 14 | 0.9012 | 0.3571 | 14 | 0.9012 | 0.3571 |
| [0.933, 1.000) | 75 | 0.9910 | 0.2133 | 75 | 0.9910 | 0.2133 |

### B2 / qs_v1, holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.4972 | 0.4972 | 0.9926 | 0.9926 | 0.3967 | 0.3967 |
| subject_role = raw (T fallback) | 0.3519 | 0.3519 | 0.8933 | 0.8933 | 0.3182 | 0.3182 |
| category | 0.1662 | 0.1771 | 0.6078 | 0.6225 | 0.5536 | 0.5617 |
| doc_kind = raw (T fallback) | 0.2644 | 0.2644 | 0.6742 | 0.6742 | 0.3448 | 0.3448 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.600, 0.667) | 1 | 0.6610 | 0.0000 | 1 | 0.6610 | 0.0000 |
| [0.667, 0.733) | 1 | 0.7292 | 0.0000 | 1 | 0.7292 | 0.0000 |
| [0.733, 0.800) | 2 | 0.7586 | 0.5000 | 2 | 0.7586 | 0.5000 |
| [0.800, 0.867) | 6 | 0.8334 | 0.6667 | 6 | 0.8334 | 0.6667 |
| [0.867, 0.933) | 24 | 0.9034 | 0.4167 | 24 | 0.9034 | 0.4167 |
| [0.933, 1.000) | 16 | 0.9544 | 0.3125 | 16 | 0.9544 | 0.3125 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.333, 0.400) | 5 | 0.3786 | 0.8000 | 5 | 0.3786 | 0.8000 |
| [0.400, 0.467) | 6 | 0.4428 | 0.3333 | 6 | 0.4428 | 0.3333 |
| [0.467, 0.533) | 4 | 0.5022 | 0.7500 | 4 | 0.5022 | 0.7500 |
| [0.533, 0.600) | 8 | 0.5605 | 0.5000 | 8 | 0.5605 | 0.5000 |
| [0.600, 0.667) | 5 | 0.6287 | 0.6000 | 5 | 0.6287 | 0.6000 |
| [0.667, 0.733) | 3 | 0.7008 | 0.3333 | 3 | 0.7009 | 0.3333 |
| [0.733, 0.800) | 4 | 0.7706 | 0.0000 | 4 | 0.7706 | 0.0000 |
| [0.800, 0.867) | 3 | 0.8420 | 0.3333 | 3 | 0.8420 | 0.3333 |
| [0.867, 0.933) | 3 | 0.8812 | 0.3333 | 3 | 0.8812 | 0.3333 |
| [0.933, 1.000) | 9 | 0.9844 | 0.3333 | 9 | 0.9844 | 0.3333 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 1 | 0.3331 | 1.0000 | 11 | 0.3085 | 0.5455 |
| [0.333, 0.400) | 9 | 0.3666 | 0.4444 | 11 | 0.3735 | 0.3636 |
| [0.400, 0.467) | 7 | 0.4440 | 0.5714 | 14 | 0.4356 | 0.6429 |
| [0.467, 0.533) | 6 | 0.4970 | 0.3333 | 4 | 0.5001 | 0.7500 |
| [0.533, 0.600) | 12 | 0.5683 | 0.6667 | 2 | 0.5813 | 0.5000 |
| [0.600, 0.667) | 3 | 0.6271 | 0.3333 | 4 | 0.6304 | 0.7500 |
| [0.667, 0.733) | 2 | 0.6907 | 1.0000 | 1 | 0.6757 | 1.0000 |
| [0.733, 0.800) | 4 | 0.7771 | 0.7500 | 3 | 0.7584 | 0.3333 |
| [0.800, 0.867) | 3 | 0.8414 | 0.6667 | 0 | n/a | n/a |
| [0.867, 0.933) | 3 | 0.9181 | 0.3333 | 0 | n/a | n/a |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.333, 0.400) | 5 | 0.3670 | 0.6000 | 5 | 0.3671 | 0.6000 |
| [0.400, 0.467) | 3 | 0.4467 | 1.0000 | 3 | 0.4467 | 1.0000 |
| [0.467, 0.533) | 6 | 0.4851 | 0.5000 | 6 | 0.4851 | 0.5000 |
| [0.533, 0.600) | 7 | 0.5609 | 0.8571 | 7 | 0.5610 | 0.8571 |
| [0.600, 0.667) | 9 | 0.6272 | 0.5556 | 9 | 0.6272 | 0.5556 |
| [0.667, 0.733) | 4 | 0.7012 | 0.7500 | 4 | 0.7013 | 0.7500 |
| [0.733, 0.800) | 8 | 0.7561 | 0.3750 | 8 | 0.7562 | 0.3750 |
| [0.800, 0.867) | 2 | 0.8217 | 0.5000 | 2 | 0.8218 | 0.5000 |
| [0.867, 0.933) | 3 | 0.9123 | 0.6667 | 3 | 0.9123 | 0.6667 |
| [0.933, 1.000) | 3 | 0.9872 | 0.0000 | 3 | 0.9872 | 0.0000 |

### B2 / qs_v2, test

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.6125 | 0.6125 | 1.1880 | 1.1880 | 0.4475 | 0.4475 |
| has_phi_direct = raw (T fallback) | 0.6474 | 0.6474 | 1.1205 | 1.1205 | 0.4781 | 0.4781 |
| has_phi_quasi = raw (T fallback) | 0.5667 | 0.5667 | 1.0560 | 1.0560 | 0.4388 | 0.4388 |
| has_coded_id = raw (T fallback) | 0.5685 | 0.5685 | 1.0211 | 1.0211 | 0.5178 | 0.5178 |
| has_staff_pii = raw (T fallback) | 0.6127 | 0.6127 | 1.1056 | 1.1056 | 0.4491 | 0.4491 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 2 | 0.5127 | 0.5000 | 2 | 0.5127 | 0.5000 |
| [0.533, 0.600) | 8 | 0.5718 | 0.5000 | 8 | 0.5718 | 0.5000 |
| [0.600, 0.667) | 7 | 0.6405 | 0.4286 | 7 | 0.6405 | 0.4286 |
| [0.667, 0.733) | 7 | 0.6975 | 0.4286 | 7 | 0.6975 | 0.4286 |
| [0.733, 0.800) | 11 | 0.7699 | 0.4545 | 11 | 0.7699 | 0.4545 |
| [0.800, 0.867) | 49 | 0.8378 | 0.3061 | 49 | 0.8378 | 0.3061 |
| [0.867, 0.933) | 125 | 0.9067 | 0.2240 | 125 | 0.9067 | 0.2240 |
| [0.933, 1.000) | 111 | 0.9566 | 0.2613 | 111 | 0.9566 | 0.2613 |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 7 | 0.5168 | 0.2857 | 7 | 0.5168 | 0.2857 |
| [0.533, 0.600) | 14 | 0.5684 | 0.2857 | 14 | 0.5684 | 0.2857 |
| [0.600, 0.667) | 23 | 0.6322 | 0.1304 | 23 | 0.6322 | 0.1304 |
| [0.667, 0.733) | 41 | 0.7007 | 0.1707 | 41 | 0.7007 | 0.1707 |
| [0.733, 0.800) | 60 | 0.7696 | 0.1000 | 60 | 0.7696 | 0.1000 |
| [0.800, 0.867) | 80 | 0.8361 | 0.1125 | 80 | 0.8361 | 0.1125 |
| [0.867, 0.933) | 78 | 0.8979 | 0.1795 | 78 | 0.8979 | 0.1795 |
| [0.933, 1.000) | 17 | 0.9535 | 0.1176 | 17 | 0.9535 | 0.1176 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 8 | 0.5176 | 0.5000 | 8 | 0.5176 | 0.5000 |
| [0.533, 0.600) | 15 | 0.5630 | 0.5333 | 15 | 0.5630 | 0.5333 |
| [0.600, 0.667) | 18 | 0.6303 | 0.3333 | 18 | 0.6303 | 0.3333 |
| [0.667, 0.733) | 35 | 0.7036 | 0.2571 | 35 | 0.7036 | 0.2571 |
| [0.733, 0.800) | 44 | 0.7730 | 0.1818 | 44 | 0.7730 | 0.1818 |
| [0.800, 0.867) | 90 | 0.8341 | 0.1556 | 90 | 0.8341 | 0.1556 |
| [0.867, 0.933) | 86 | 0.8933 | 0.2209 | 86 | 0.8933 | 0.2209 |
| [0.933, 1.000) | 24 | 0.9538 | 0.3333 | 24 | 0.9538 | 0.3333 |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 11 | 0.5136 | 0.3636 | 11 | 0.5136 | 0.3636 |
| [0.533, 0.600) | 9 | 0.5739 | 0.1111 | 9 | 0.5739 | 0.1111 |
| [0.600, 0.667) | 28 | 0.6329 | 0.3571 | 28 | 0.6329 | 0.3571 |
| [0.667, 0.733) | 37 | 0.6978 | 0.1622 | 37 | 0.6978 | 0.1622 |
| [0.733, 0.800) | 59 | 0.7705 | 0.2203 | 59 | 0.7705 | 0.2203 |
| [0.800, 0.867) | 82 | 0.8376 | 0.1341 | 82 | 0.8376 | 0.1341 |
| [0.867, 0.933) | 72 | 0.8957 | 0.2778 | 72 | 0.8957 | 0.2778 |
| [0.933, 1.000) | 22 | 0.9520 | 0.3182 | 22 | 0.9520 | 0.3182 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 9 | 0.5169 | 0.5556 | 9 | 0.5169 | 0.5556 |
| [0.533, 0.600) | 13 | 0.5705 | 0.2308 | 13 | 0.5705 | 0.2308 |
| [0.600, 0.667) | 18 | 0.6357 | 0.2778 | 18 | 0.6357 | 0.2778 |
| [0.667, 0.733) | 34 | 0.7012 | 0.2059 | 34 | 0.7012 | 0.2059 |
| [0.733, 0.800) | 47 | 0.7735 | 0.1489 | 47 | 0.7735 | 0.1489 |
| [0.800, 0.867) | 82 | 0.8353 | 0.1829 | 82 | 0.8353 | 0.1829 |
| [0.867, 0.933) | 96 | 0.8983 | 0.1771 | 96 | 0.8983 | 0.1771 |
| [0.933, 1.000) | 21 | 0.9500 | 0.1905 | 21 | 0.9500 | 0.1905 |

### B2 / qs_v2, holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.4979 | 0.4979 | 0.9922 | 0.9922 | 0.4108 | 0.4108 |
| has_phi_direct = raw (T fallback) | 0.7963 | 0.7963 | 1.3393 | 1.3393 | 0.0204 | 0.0204 |
| has_phi_quasi = raw (T fallback) | 0.7639 | 0.7639 | 1.3127 | 1.3127 | 0.0208 | 0.0208 |
| has_coded_id = raw (T fallback) | 0.7457 | 0.7457 | 1.2587 | 1.2587 | 0.0260 | 0.0260 |
| has_staff_pii = raw (T fallback) | 0.4106 | 0.4106 | 0.8409 | 0.8409 | 0.3523 | 0.3523 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.600, 0.667) | 1 | 0.6507 | 0.0000 | 1 | 0.6507 | 0.0000 |
| [0.733, 0.800) | 3 | 0.7504 | 0.3333 | 3 | 0.7504 | 0.3333 |
| [0.800, 0.867) | 6 | 0.8389 | 0.6667 | 6 | 0.8389 | 0.6667 |
| [0.867, 0.933) | 23 | 0.9026 | 0.3913 | 23 | 0.9026 | 0.3913 |
| [0.933, 1.000) | 17 | 0.9531 | 0.3529 | 17 | 0.9531 | 0.3529 |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.533, 0.600) | 1 | 0.5525 | 0.0000 | 1 | 0.5525 | 0.0000 |
| [0.600, 0.667) | 2 | 0.6351 | 0.5000 | 2 | 0.6351 | 0.5000 |
| [0.667, 0.733) | 5 | 0.7076 | 0.0000 | 5 | 0.7076 | 0.0000 |
| [0.733, 0.800) | 12 | 0.7677 | 0.0000 | 12 | 0.7677 | 0.0000 |
| [0.800, 0.867) | 14 | 0.8366 | 0.0000 | 14 | 0.8366 | 0.0000 |
| [0.867, 0.933) | 13 | 0.8960 | 0.0000 | 13 | 0.8960 | 0.0000 |
| [0.933, 1.000) | 3 | 0.9612 | 0.0000 | 3 | 0.9612 | 0.0000 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 2 | 0.5094 | 0.5000 | 2 | 0.5094 | 0.5000 |
| [0.533, 0.600) | 2 | 0.5764 | 0.5000 | 2 | 0.5764 | 0.5000 |
| [0.600, 0.667) | 2 | 0.6612 | 0.0000 | 2 | 0.6612 | 0.0000 |
| [0.667, 0.733) | 6 | 0.7092 | 0.0000 | 6 | 0.7092 | 0.0000 |
| [0.733, 0.800) | 10 | 0.7694 | 0.0000 | 10 | 0.7694 | 0.0000 |
| [0.800, 0.867) | 9 | 0.8261 | 0.0000 | 9 | 0.8261 | 0.0000 |
| [0.867, 0.933) | 13 | 0.8960 | 0.0000 | 13 | 0.8960 | 0.0000 |
| [0.933, 1.000) | 6 | 0.9451 | 0.0000 | 6 | 0.9451 | 0.0000 |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 4 | 0.5113 | 0.5000 | 4 | 0.5113 | 0.5000 |
| [0.600, 0.667) | 3 | 0.6492 | 0.0000 | 3 | 0.6492 | 0.0000 |
| [0.667, 0.733) | 5 | 0.7002 | 0.0000 | 5 | 0.7002 | 0.0000 |
| [0.733, 0.800) | 12 | 0.7594 | 0.0000 | 12 | 0.7594 | 0.0000 |
| [0.800, 0.867) | 10 | 0.8286 | 0.0000 | 10 | 0.8286 | 0.0000 |
| [0.867, 0.933) | 14 | 0.8920 | 0.0000 | 14 | 0.8920 | 0.0000 |
| [0.933, 1.000) | 2 | 0.9528 | 0.0000 | 2 | 0.9528 | 0.0000 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.533, 0.600) | 2 | 0.5612 | 1.0000 | 2 | 0.5612 | 1.0000 |
| [0.600, 0.667) | 1 | 0.6325 | 0.0000 | 1 | 0.6325 | 0.0000 |
| [0.667, 0.733) | 4 | 0.7119 | 0.2500 | 4 | 0.7119 | 0.2500 |
| [0.733, 0.800) | 15 | 0.7739 | 0.5333 | 15 | 0.7739 | 0.5333 |
| [0.800, 0.867) | 12 | 0.8288 | 0.5833 | 12 | 0.8288 | 0.5833 |
| [0.867, 0.933) | 12 | 0.8970 | 0.3333 | 12 | 0.8970 | 0.3333 |
| [0.933, 1.000) | 4 | 0.9632 | 0.0000 | 4 | 0.9632 | 0.0000 |

### B3 / qs_v1 (doc-level, underpowered), test

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.4353 | 0.4353 | 0.8790 | 0.8790 | 0.5359 | 0.5359 |
| subject_role = raw (T fallback) | 0.3990 | 0.3990 | 1.0165 | 1.0165 | 0.5295 | 0.5295 |
| category | 0.2344 | 0.0993 | 0.8650 | 0.7812 | 0.5159 | 0.5136 |
| doc_kind = raw (T fallback) | 0.4201 | 0.4201 | 1.0932 | 1.0932 | 0.4162 | 0.4164 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 3 | 0.5171 | 0.3333 | 3 | 0.5171 | 0.3333 |
| [0.533, 0.600) | 5 | 0.5608 | 0.4000 | 5 | 0.5608 | 0.4000 |
| [0.600, 0.667) | 5 | 0.6460 | 0.0000 | 5 | 0.6460 | 0.0000 |
| [0.667, 0.733) | 9 | 0.6941 | 0.5556 | 9 | 0.6941 | 0.5556 |
| [0.733, 0.800) | 10 | 0.7707 | 0.5000 | 10 | 0.7707 | 0.5000 |
| [0.800, 0.867) | 46 | 0.8380 | 0.4348 | 46 | 0.8380 | 0.4348 |
| [0.867, 0.933) | 59 | 0.9073 | 0.3898 | 59 | 0.9073 | 0.3898 |
| [0.933, 1.000) | 50 | 0.9556 | 0.4800 | 50 | 0.9556 | 0.4800 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 3 | 0.2965 | 0.0000 | 3 | 0.2965 | 0.0000 |
| [0.333, 0.400) | 13 | 0.3648 | 0.3846 | 13 | 0.3648 | 0.3846 |
| [0.400, 0.467) | 22 | 0.4381 | 0.4091 | 22 | 0.4381 | 0.4091 |
| [0.467, 0.533) | 24 | 0.4991 | 0.0833 | 24 | 0.4991 | 0.0833 |
| [0.533, 0.600) | 15 | 0.5627 | 0.3333 | 15 | 0.5627 | 0.3333 |
| [0.600, 0.667) | 9 | 0.6272 | 0.2222 | 9 | 0.6272 | 0.2222 |
| [0.667, 0.733) | 10 | 0.6943 | 0.2000 | 10 | 0.6943 | 0.2000 |
| [0.733, 0.800) | 16 | 0.7733 | 0.3125 | 16 | 0.7733 | 0.3125 |
| [0.800, 0.867) | 22 | 0.8423 | 0.3636 | 22 | 0.8423 | 0.3636 |
| [0.867, 0.933) | 22 | 0.8989 | 0.2727 | 22 | 0.8989 | 0.2727 |
| [0.933, 1.000) | 31 | 0.9721 | 0.3548 | 31 | 0.9721 | 0.3548 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 2 | 0.2425 | 0.5000 | 54 | 0.2491 | 0.2593 |
| [0.267, 0.333) | 15 | 0.3131 | 0.1333 | 68 | 0.3013 | 0.4265 |
| [0.333, 0.400) | 31 | 0.3650 | 0.2903 | 38 | 0.3565 | 0.3684 |
| [0.400, 0.467) | 24 | 0.4315 | 0.3333 | 11 | 0.4227 | 0.2727 |
| [0.467, 0.533) | 23 | 0.4977 | 0.5217 | 6 | 0.4966 | 0.1667 |
| [0.533, 0.600) | 23 | 0.5695 | 0.3913 | 2 | 0.5907 | 0.0000 |
| [0.600, 0.667) | 15 | 0.6301 | 0.3333 | 3 | 0.6247 | 0.0000 |
| [0.667, 0.733) | 19 | 0.6891 | 0.4737 | 2 | 0.7125 | 0.5000 |
| [0.733, 0.800) | 8 | 0.7620 | 0.2500 | 1 | 0.7819 | 1.0000 |
| [0.800, 0.867) | 8 | 0.8287 | 0.3750 | 1 | 0.8149 | 0.0000 |
| [0.867, 0.933) | 8 | 0.9013 | 0.1250 | 1 | 0.9083 | 0.0000 |
| [0.933, 1.000) | 11 | 0.9828 | 0.1818 | 0 | n/a | n/a |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 1 | 0.2610 | 0.0000 | 1 | 0.2610 | 0.0000 |
| [0.267, 0.333) | 9 | 0.3076 | 0.2222 | 9 | 0.3076 | 0.2222 |
| [0.333, 0.400) | 17 | 0.3735 | 0.4118 | 17 | 0.3735 | 0.4118 |
| [0.400, 0.467) | 17 | 0.4319 | 0.4706 | 17 | 0.4320 | 0.4706 |
| [0.467, 0.533) | 15 | 0.4974 | 0.4000 | 15 | 0.4974 | 0.4000 |
| [0.533, 0.600) | 11 | 0.5632 | 0.4545 | 11 | 0.5632 | 0.4545 |
| [0.600, 0.667) | 13 | 0.6366 | 0.2308 | 13 | 0.6366 | 0.2308 |
| [0.667, 0.733) | 10 | 0.7013 | 0.3000 | 10 | 0.7013 | 0.3000 |
| [0.733, 0.800) | 6 | 0.7623 | 0.5000 | 6 | 0.7624 | 0.5000 |
| [0.800, 0.867) | 14 | 0.8365 | 0.3571 | 14 | 0.8365 | 0.3571 |
| [0.867, 0.933) | 6 | 0.9036 | 0.3333 | 6 | 0.9036 | 0.3333 |
| [0.933, 1.000) | 68 | 0.9936 | 0.2206 | 68 | 0.9936 | 0.2206 |

### B3 / qs_v1 (doc-level, underpowered), holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.2570 | 0.2570 | 0.5698 | 0.5698 | 0.5909 | 0.5909 |
| subject_role = raw (T fallback) | 0.2358 | 0.2358 | 0.5983 | 0.5983 | 0.5598 | 0.5598 |
| category | 0.2056 | 0.4022 | 0.4956 | 0.6539 | 0.5404 | 0.5505 |
| doc_kind = raw (T fallback) | 0.2552 | 0.2552 | 0.3412 | 0.3412 | 0.6385 | 0.6385 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.733, 0.800) | 1 | 0.7432 | 1.0000 | 1 | 0.7432 | 1.0000 |
| [0.800, 0.867) | 9 | 0.8319 | 0.5556 | 9 | 0.8319 | 0.5556 |
| [0.867, 0.933) | 15 | 0.9015 | 0.6000 | 15 | 0.9015 | 0.6000 |
| [0.933, 1.000) | 6 | 0.9498 | 0.8333 | 6 | 0.9498 | 0.8333 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.333, 0.400) | 1 | 0.3942 | 1.0000 | 1 | 0.3942 | 1.0000 |
| [0.400, 0.467) | 5 | 0.4407 | 0.6000 | 5 | 0.4407 | 0.6000 |
| [0.467, 0.533) | 1 | 0.4914 | 1.0000 | 1 | 0.4914 | 1.0000 |
| [0.533, 0.600) | 4 | 0.5572 | 0.2500 | 4 | 0.5571 | 0.2500 |
| [0.600, 0.667) | 2 | 0.6301 | 0.5000 | 2 | 0.6301 | 0.5000 |
| [0.667, 0.733) | 4 | 0.6989 | 0.2500 | 4 | 0.6990 | 0.2500 |
| [0.733, 0.800) | 4 | 0.7708 | 0.5000 | 4 | 0.7708 | 0.5000 |
| [0.800, 0.867) | 7 | 0.8380 | 0.7143 | 7 | 0.8380 | 0.7143 |
| [0.867, 0.933) | 1 | 0.8949 | 1.0000 | 1 | 0.8949 | 1.0000 |
| [0.933, 1.000) | 2 | 0.9704 | 1.0000 | 2 | 0.9703 | 1.0000 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 0 | n/a | n/a | 7 | 0.2511 | 0.7143 |
| [0.267, 0.333) | 2 | 0.3293 | 1.0000 | 17 | 0.2979 | 0.5882 |
| [0.333, 0.400) | 5 | 0.3637 | 0.6000 | 5 | 0.3595 | 1.0000 |
| [0.400, 0.467) | 7 | 0.4440 | 0.7143 | 1 | 0.4180 | 1.0000 |
| [0.467, 0.533) | 3 | 0.5001 | 0.6667 | 1 | 0.4931 | 1.0000 |
| [0.533, 0.600) | 4 | 0.5618 | 0.5000 | 0 | n/a | n/a |
| [0.600, 0.667) | 5 | 0.6363 | 0.6000 | 0 | n/a | n/a |
| [0.667, 0.733) | 1 | 0.7008 | 1.0000 | 0 | n/a | n/a |
| [0.733, 0.800) | 2 | 0.7549 | 1.0000 | 0 | n/a | n/a |
| [0.800, 0.867) | 1 | 0.8358 | 1.0000 | 0 | n/a | n/a |
| [0.867, 0.933) | 1 | 0.9243 | 1.0000 | 0 | n/a | n/a |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.400, 0.467) | 4 | 0.4292 | 0.7500 | 4 | 0.4292 | 0.7500 |
| [0.467, 0.533) | 5 | 0.4905 | 0.6000 | 5 | 0.4905 | 0.6000 |
| [0.533, 0.600) | 3 | 0.5468 | 1.0000 | 3 | 0.5468 | 1.0000 |
| [0.600, 0.667) | 3 | 0.6329 | 0.6667 | 3 | 0.6329 | 0.6667 |
| [0.667, 0.733) | 7 | 0.6905 | 1.0000 | 7 | 0.6905 | 1.0000 |
| [0.733, 0.800) | 4 | 0.7481 | 1.0000 | 4 | 0.7481 | 1.0000 |
| [0.800, 0.867) | 1 | 0.8016 | 1.0000 | 1 | 0.8016 | 1.0000 |
| [0.867, 0.933) | 3 | 0.9172 | 1.0000 | 3 | 0.9173 | 1.0000 |
| [0.933, 1.000) | 1 | 0.9999 | 0.0000 | 1 | 0.9999 | 0.0000 |

### B3 / qs_v2 (doc-level, underpowered), test

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.4359 | 0.4359 | 0.8993 | 0.8993 | 0.5087 | 0.5087 |
| has_phi_direct = raw (T fallback) | 0.5110 | 0.5110 | 0.9446 | 0.9446 | 0.4537 | 0.4537 |
| has_phi_quasi = raw (T fallback) | 0.4507 | 0.4507 | 0.8547 | 0.8547 | 0.5321 | 0.5321 |
| has_coded_id = raw (T fallback) | 0.3999 | 0.3999 | 0.7879 | 0.7879 | 0.5345 | 0.5345 |
| has_staff_pii = raw (T fallback) | 0.4443 | 0.4443 | 0.8693 | 0.8693 | 0.4434 | 0.4434 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 2 | 0.5115 | 0.5000 | 2 | 0.5115 | 0.5000 |
| [0.533, 0.600) | 7 | 0.5769 | 0.5714 | 7 | 0.5769 | 0.5714 |
| [0.600, 0.667) | 6 | 0.6327 | 0.3333 | 6 | 0.6327 | 0.3333 |
| [0.667, 0.733) | 6 | 0.6919 | 0.5000 | 6 | 0.6919 | 0.5000 |
| [0.733, 0.800) | 6 | 0.7705 | 0.6667 | 6 | 0.7705 | 0.6667 |
| [0.800, 0.867) | 34 | 0.8452 | 0.4412 | 34 | 0.8452 | 0.4412 |
| [0.867, 0.933) | 66 | 0.9050 | 0.3636 | 66 | 0.9050 | 0.3636 |
| [0.933, 1.000) | 60 | 0.9569 | 0.4833 | 60 | 0.9569 | 0.4833 |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 5 | 0.5097 | 0.6000 | 5 | 0.5097 | 0.6000 |
| [0.533, 0.600) | 12 | 0.5640 | 0.5000 | 12 | 0.5640 | 0.5000 |
| [0.600, 0.667) | 20 | 0.6391 | 0.2500 | 20 | 0.6391 | 0.2500 |
| [0.667, 0.733) | 32 | 0.6964 | 0.1562 | 32 | 0.6964 | 0.1562 |
| [0.733, 0.800) | 35 | 0.7692 | 0.2857 | 35 | 0.7692 | 0.2857 |
| [0.800, 0.867) | 39 | 0.8326 | 0.2308 | 39 | 0.8326 | 0.2308 |
| [0.867, 0.933) | 36 | 0.8962 | 0.2778 | 36 | 0.8962 | 0.2778 |
| [0.933, 1.000) | 8 | 0.9521 | 0.1250 | 8 | 0.9521 | 0.1250 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 8 | 0.5163 | 0.1250 | 8 | 0.5163 | 0.1250 |
| [0.533, 0.600) | 10 | 0.5643 | 0.7000 | 10 | 0.5643 | 0.7000 |
| [0.600, 0.667) | 18 | 0.6325 | 0.5000 | 18 | 0.6325 | 0.5000 |
| [0.667, 0.733) | 22 | 0.7132 | 0.1818 | 22 | 0.7132 | 0.1818 |
| [0.733, 0.800) | 37 | 0.7658 | 0.1892 | 37 | 0.7658 | 0.1892 |
| [0.800, 0.867) | 40 | 0.8324 | 0.3500 | 40 | 0.8324 | 0.3500 |
| [0.867, 0.933) | 44 | 0.8975 | 0.3864 | 44 | 0.8975 | 0.3864 |
| [0.933, 1.000) | 8 | 0.9500 | 0.6250 | 8 | 0.9500 | 0.6250 |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 8 | 0.5158 | 0.6250 | 8 | 0.5159 | 0.6250 |
| [0.533, 0.600) | 8 | 0.5722 | 0.2500 | 8 | 0.5722 | 0.2500 |
| [0.600, 0.667) | 27 | 0.6364 | 0.4074 | 27 | 0.6364 | 0.4074 |
| [0.667, 0.733) | 33 | 0.7005 | 0.3333 | 33 | 0.7005 | 0.3333 |
| [0.733, 0.800) | 31 | 0.7632 | 0.1613 | 31 | 0.7632 | 0.1613 |
| [0.800, 0.867) | 43 | 0.8303 | 0.4186 | 43 | 0.8303 | 0.4186 |
| [0.867, 0.933) | 26 | 0.8944 | 0.4231 | 26 | 0.8944 | 0.4231 |
| [0.933, 1.000) | 11 | 0.9471 | 0.5455 | 11 | 0.9471 | 0.5455 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 9 | 0.5186 | 0.6667 | 9 | 0.5186 | 0.6667 |
| [0.533, 0.600) | 11 | 0.5690 | 0.3636 | 11 | 0.5690 | 0.3636 |
| [0.600, 0.667) | 22 | 0.6377 | 0.2727 | 22 | 0.6377 | 0.2727 |
| [0.667, 0.733) | 26 | 0.6986 | 0.4231 | 26 | 0.6986 | 0.4231 |
| [0.733, 0.800) | 31 | 0.7680 | 0.2903 | 31 | 0.7680 | 0.2903 |
| [0.800, 0.867) | 45 | 0.8321 | 0.3111 | 45 | 0.8321 | 0.3111 |
| [0.867, 0.933) | 34 | 0.8967 | 0.3235 | 34 | 0.8967 | 0.3235 |
| [0.933, 1.000) | 9 | 0.9502 | 0.2222 | 9 | 0.9502 | 0.2222 |

### B3 / qs_v2 (doc-level, underpowered), holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.2679 | 0.2679 | 0.5721 | 0.5721 | 0.6818 | 0.6818 |
| has_phi_direct = raw (T fallback) | 0.7957 | 0.7957 | 1.2785 | 1.2785 | n/a | n/a |
| has_phi_quasi = raw (T fallback) | 0.7486 | 0.7486 | 1.2103 | 1.2103 | 0.1000 | 0.1000 |
| has_coded_id = raw (T fallback) | 0.7583 | 0.7583 | 1.1674 | 1.1674 | n/a | n/a |
| has_staff_pii = raw (T fallback) | 0.1596 | 0.1596 | 0.4704 | 0.4704 | 0.6955 | 0.6955 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.733, 0.800) | 1 | 0.7419 | 1.0000 | 1 | 0.7419 | 1.0000 |
| [0.800, 0.867) | 7 | 0.8361 | 0.5714 | 7 | 0.8361 | 0.5714 |
| [0.867, 0.933) | 15 | 0.9038 | 0.5333 | 15 | 0.9038 | 0.5333 |
| [0.933, 1.000) | 8 | 0.9545 | 0.8750 | 8 | 0.9545 | 0.8750 |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.600, 0.667) | 1 | 0.6320 | 0.0000 | 1 | 0.6320 | 0.0000 |
| [0.667, 0.733) | 8 | 0.7072 | 0.0000 | 8 | 0.7072 | 0.0000 |
| [0.733, 0.800) | 8 | 0.7758 | 0.0000 | 8 | 0.7758 | 0.0000 |
| [0.800, 0.867) | 10 | 0.8484 | 0.0000 | 10 | 0.8484 | 0.0000 |
| [0.867, 0.933) | 3 | 0.9128 | 0.0000 | 3 | 0.9128 | 0.0000 |
| [0.933, 1.000) | 1 | 0.9481 | 0.0000 | 1 | 0.9481 | 0.0000 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.533, 0.600) | 1 | 0.5988 | 0.0000 | 1 | 0.5988 | 0.0000 |
| [0.600, 0.667) | 1 | 0.6641 | 0.0000 | 1 | 0.6641 | 0.0000 |
| [0.667, 0.733) | 9 | 0.7046 | 0.1111 | 9 | 0.7046 | 0.1111 |
| [0.733, 0.800) | 8 | 0.7676 | 0.0000 | 8 | 0.7676 | 0.0000 |
| [0.800, 0.867) | 7 | 0.8407 | 0.0000 | 7 | 0.8407 | 0.0000 |
| [0.867, 0.933) | 3 | 0.8991 | 0.0000 | 3 | 0.8991 | 0.0000 |
| [0.933, 1.000) | 2 | 0.9399 | 0.0000 | 2 | 0.9399 | 0.0000 |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 1 | 0.5146 | 0.0000 | 1 | 0.5146 | 0.0000 |
| [0.533, 0.600) | 1 | 0.5913 | 0.0000 | 1 | 0.5913 | 0.0000 |
| [0.600, 0.667) | 3 | 0.6285 | 0.0000 | 3 | 0.6285 | 0.0000 |
| [0.667, 0.733) | 4 | 0.7095 | 0.0000 | 4 | 0.7095 | 0.0000 |
| [0.733, 0.800) | 10 | 0.7516 | 0.0000 | 10 | 0.7516 | 0.0000 |
| [0.800, 0.867) | 8 | 0.8176 | 0.0000 | 8 | 0.8176 | 0.0000 |
| [0.867, 0.933) | 4 | 0.9053 | 0.0000 | 4 | 0.9053 | 0.0000 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.667, 0.733) | 7 | 0.7148 | 0.4286 | 7 | 0.7148 | 0.4286 |
| [0.733, 0.800) | 12 | 0.7688 | 0.5833 | 12 | 0.7688 | 0.5833 |
| [0.800, 0.867) | 7 | 0.8270 | 0.8571 | 7 | 0.8270 | 0.8571 |
| [0.867, 0.933) | 5 | 0.9017 | 0.8000 | 5 | 0.9017 | 0.8000 |

### B4 / qs_v1 (doc-level, underpowered), test

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.2568 | 0.1205 | 0.6152 | 0.4883 | 0.5529 | 0.5529 |
| subject_role | 0.3259 | 0.0657 | 0.9165 | 0.7341 | 0.5858 | 0.5699 |
| category | 0.3020 | 0.0595 | 0.9603 | 0.7999 | 0.4920 | 0.4856 |
| doc_kind = raw (T fallback) | 0.5326 | 0.5326 | 1.1791 | 1.1791 | 0.4080 | 0.4088 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 2 | 0.5137 | 0.5000 | 7 | 0.5159 | 0.4286 |
| [0.533, 0.600) | 5 | 0.5608 | 0.4000 | 20 | 0.5656 | 0.4500 |
| [0.600, 0.667) | 8 | 0.6359 | 0.2500 | 36 | 0.6368 | 0.7222 |
| [0.667, 0.733) | 7 | 0.6925 | 0.5714 | 45 | 0.6964 | 0.5111 |
| [0.733, 0.800) | 8 | 0.7690 | 0.6250 | 15 | 0.7625 | 0.7333 |
| [0.800, 0.867) | 28 | 0.8404 | 0.7143 | 1 | 0.8383 | 1.0000 |
| [0.867, 0.933) | 37 | 0.9081 | 0.5135 | 0 | n/a | n/a |
| [0.933, 1.000) | 29 | 0.9586 | 0.6897 | 0 | n/a | n/a |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 0 | n/a | n/a | 18 | 0.2624 | 0.3333 |
| [0.267, 0.333) | 2 | 0.2913 | 0.0000 | 93 | 0.2907 | 0.3441 |
| [0.333, 0.400) | 7 | 0.3605 | 0.2857 | 10 | 0.3555 | 0.3000 |
| [0.400, 0.467) | 21 | 0.4441 | 0.3333 | 1 | 0.4170 | 0.0000 |
| [0.467, 0.533) | 15 | 0.4909 | 0.2000 | 0 | n/a | n/a |
| [0.533, 0.600) | 11 | 0.5627 | 0.2727 | 2 | 0.5369 | 1.0000 |
| [0.600, 0.667) | 9 | 0.6401 | 0.3333 | 0 | n/a | n/a |
| [0.667, 0.733) | 5 | 0.6873 | 0.2000 | 0 | n/a | n/a |
| [0.733, 0.800) | 10 | 0.7690 | 0.4000 | 0 | n/a | n/a |
| [0.800, 0.867) | 9 | 0.8381 | 0.6667 | 0 | n/a | n/a |
| [0.867, 0.933) | 14 | 0.8997 | 0.3571 | 0 | n/a | n/a |
| [0.933, 1.000) | 21 | 0.9717 | 0.4286 | 0 | n/a | n/a |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 1 | 0.2458 | 1.0000 | 63 | 0.2381 | 0.2540 |
| [0.267, 0.333) | 13 | 0.3014 | 0.1538 | 50 | 0.2909 | 0.3400 |
| [0.333, 0.400) | 23 | 0.3604 | 0.3043 | 6 | 0.3616 | 0.0000 |
| [0.400, 0.467) | 10 | 0.4311 | 0.1000 | 2 | 0.4391 | 0.0000 |
| [0.467, 0.533) | 9 | 0.4979 | 0.4444 | 0 | n/a | n/a |
| [0.533, 0.600) | 16 | 0.5682 | 0.2500 | 2 | 0.5781 | 0.5000 |
| [0.600, 0.667) | 12 | 0.6230 | 0.3333 | 0 | n/a | n/a |
| [0.667, 0.733) | 14 | 0.6928 | 0.5000 | 1 | 0.7268 | 0.0000 |
| [0.733, 0.800) | 7 | 0.7670 | 0.1429 | 0 | n/a | n/a |
| [0.800, 0.867) | 8 | 0.8287 | 0.2500 | 0 | n/a | n/a |
| [0.867, 0.933) | 5 | 0.9062 | 0.0000 | 0 | n/a | n/a |
| [0.933, 1.000) | 6 | 0.9831 | 0.1667 | 0 | n/a | n/a |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 1 | 0.2610 | 0.0000 | 1 | 0.2610 | 0.0000 |
| [0.267, 0.333) | 6 | 0.3126 | 0.1667 | 6 | 0.3126 | 0.1667 |
| [0.333, 0.400) | 8 | 0.3721 | 0.1250 | 8 | 0.3721 | 0.1250 |
| [0.400, 0.467) | 8 | 0.4181 | 0.3750 | 8 | 0.4181 | 0.3750 |
| [0.467, 0.533) | 13 | 0.4972 | 0.6923 | 13 | 0.4972 | 0.6923 |
| [0.533, 0.600) | 5 | 0.5623 | 0.8000 | 5 | 0.5622 | 0.8000 |
| [0.600, 0.667) | 5 | 0.6378 | 0.0000 | 5 | 0.6378 | 0.0000 |
| [0.667, 0.733) | 4 | 0.6889 | 0.2500 | 4 | 0.6889 | 0.2500 |
| [0.733, 0.800) | 3 | 0.7551 | 0.6667 | 3 | 0.7551 | 0.6667 |
| [0.800, 0.867) | 4 | 0.8355 | 0.0000 | 4 | 0.8355 | 0.0000 |
| [0.867, 0.933) | 4 | 0.9103 | 0.2500 | 4 | 0.9103 | 0.2500 |
| [0.933, 1.000) | 63 | 0.9946 | 0.2381 | 63 | 0.9946 | 0.2381 |

### B4 / qs_v1 (doc-level, underpowered), holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.2502 | 0.0840 | 0.5431 | 0.4397 | 0.5700 | 0.5700 |
| subject_role | 0.2489 | 0.2775 | 0.6170 | 0.7075 | 0.5430 | 0.5566 |
| category | 0.2311 | 0.4399 | 0.5131 | 0.7139 | 0.4974 | 0.5132 |
| doc_kind = raw (T fallback) | 0.2444 | 0.2444 | 0.3366 | 0.3366 | 0.6640 | 0.6640 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.533, 0.600) | 0 | n/a | n/a | 1 | 0.5878 | 1.0000 |
| [0.600, 0.667) | 0 | n/a | n/a | 13 | 0.6413 | 0.5385 |
| [0.667, 0.733) | 0 | n/a | n/a | 14 | 0.6952 | 0.7143 |
| [0.733, 0.800) | 2 | 0.7690 | 1.0000 | 2 | 0.7480 | 1.0000 |
| [0.800, 0.867) | 7 | 0.8318 | 0.5714 | 0 | n/a | n/a |
| [0.867, 0.933) | 15 | 0.9015 | 0.6000 | 0 | n/a | n/a |
| [0.933, 1.000) | 6 | 0.9498 | 0.8333 | 0 | n/a | n/a |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 0 | n/a | n/a | 3 | 0.2659 | 0.3333 |
| [0.267, 0.333) | 0 | n/a | n/a | 26 | 0.2884 | 0.5769 |
| [0.333, 0.400) | 1 | 0.3942 | 1.0000 | 1 | 0.3789 | 1.0000 |
| [0.400, 0.467) | 5 | 0.4407 | 0.6000 | 0 | n/a | n/a |
| [0.467, 0.533) | 1 | 0.4914 | 1.0000 | 0 | n/a | n/a |
| [0.533, 0.600) | 4 | 0.5572 | 0.2500 | 0 | n/a | n/a |
| [0.600, 0.667) | 2 | 0.6301 | 0.5000 | 0 | n/a | n/a |
| [0.667, 0.733) | 4 | 0.6989 | 0.2500 | 0 | n/a | n/a |
| [0.733, 0.800) | 4 | 0.7708 | 0.5000 | 0 | n/a | n/a |
| [0.800, 0.867) | 6 | 0.8373 | 0.6667 | 0 | n/a | n/a |
| [0.867, 0.933) | 1 | 0.8949 | 1.0000 | 0 | n/a | n/a |
| [0.933, 1.000) | 2 | 0.9704 | 1.0000 | 0 | n/a | n/a |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 0 | n/a | n/a | 20 | 0.2442 | 0.7000 |
| [0.267, 0.333) | 2 | 0.3293 | 1.0000 | 9 | 0.2838 | 0.6667 |
| [0.333, 0.400) | 5 | 0.3637 | 0.6000 | 1 | 0.3642 | 1.0000 |
| [0.400, 0.467) | 7 | 0.4440 | 0.7143 | 0 | n/a | n/a |
| [0.467, 0.533) | 4 | 0.5081 | 0.7500 | 0 | n/a | n/a |
| [0.533, 0.600) | 4 | 0.5618 | 0.5000 | 0 | n/a | n/a |
| [0.600, 0.667) | 4 | 0.6336 | 0.5000 | 0 | n/a | n/a |
| [0.667, 0.733) | 1 | 0.7008 | 1.0000 | 0 | n/a | n/a |
| [0.733, 0.800) | 1 | 0.7708 | 1.0000 | 0 | n/a | n/a |
| [0.800, 0.867) | 1 | 0.8358 | 1.0000 | 0 | n/a | n/a |
| [0.867, 0.933) | 1 | 0.9243 | 1.0000 | 0 | n/a | n/a |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.400, 0.467) | 3 | 0.4327 | 0.6667 | 3 | 0.4327 | 0.6667 |
| [0.467, 0.533) | 5 | 0.4905 | 0.6000 | 5 | 0.4905 | 0.6000 |
| [0.533, 0.600) | 3 | 0.5464 | 1.0000 | 3 | 0.5464 | 1.0000 |
| [0.600, 0.667) | 3 | 0.6329 | 0.6667 | 3 | 0.6329 | 0.6667 |
| [0.667, 0.733) | 7 | 0.6905 | 1.0000 | 7 | 0.6905 | 1.0000 |
| [0.733, 0.800) | 4 | 0.7481 | 1.0000 | 4 | 0.7481 | 1.0000 |
| [0.800, 0.867) | 1 | 0.8016 | 1.0000 | 1 | 0.8016 | 1.0000 |
| [0.867, 0.933) | 3 | 0.9172 | 1.0000 | 3 | 0.9173 | 1.0000 |
| [0.933, 1.000) | 1 | 0.9999 | 0.0000 | 1 | 0.9999 | 0.0000 |

### B4 / qs_v2 (doc-level, underpowered), test

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.2712 | 0.0905 | 0.6207 | 0.4873 | 0.5373 | 0.5373 |
| has_phi_direct = raw (T fallback) | 0.4234 | 0.4234 | 0.8488 | 0.8488 | 0.4548 | 0.4548 |
| has_phi_quasi | 0.3085 | 0.0672 | 0.7019 | 0.5068 | 0.5261 | 0.5261 |
| has_coded_id = raw (T fallback) | 0.2285 | 0.2285 | 0.6025 | 0.6025 | 0.5438 | 0.5438 |
| has_staff_pii = raw (T fallback) | 0.3304 | 0.3304 | 0.7506 | 0.7506 | 0.4258 | 0.4258 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 1 | 0.5215 | 1.0000 | 8 | 0.5222 | 0.5000 |
| [0.533, 0.600) | 7 | 0.5741 | 0.4286 | 13 | 0.5614 | 0.3846 |
| [0.600, 0.667) | 5 | 0.6367 | 0.2000 | 37 | 0.6366 | 0.6757 |
| [0.667, 0.733) | 7 | 0.6959 | 0.4286 | 50 | 0.6994 | 0.5800 |
| [0.733, 0.800) | 3 | 0.7812 | 0.6667 | 14 | 0.7628 | 0.7143 |
| [0.800, 0.867) | 27 | 0.8408 | 0.7778 | 2 | 0.8231 | 0.5000 |
| [0.867, 0.933) | 37 | 0.9071 | 0.5405 | 0 | n/a | n/a |
| [0.933, 1.000) | 37 | 0.9586 | 0.6216 | 0 | n/a | n/a |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 5 | 0.5116 | 0.6000 | 5 | 0.5116 | 0.6000 |
| [0.533, 0.600) | 12 | 0.5684 | 0.4167 | 12 | 0.5684 | 0.4167 |
| [0.600, 0.667) | 12 | 0.6358 | 0.2500 | 12 | 0.6358 | 0.2500 |
| [0.667, 0.733) | 18 | 0.7017 | 0.3333 | 18 | 0.7017 | 0.3333 |
| [0.733, 0.800) | 26 | 0.7655 | 0.4231 | 26 | 0.7655 | 0.4231 |
| [0.800, 0.867) | 18 | 0.8352 | 0.2222 | 18 | 0.8352 | 0.2222 |
| [0.867, 0.933) | 26 | 0.8983 | 0.3846 | 26 | 0.8983 | 0.3846 |
| [0.933, 1.000) | 7 | 0.9540 | 0.1429 | 7 | 0.9540 | 0.1429 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 3 | 0.5228 | 0.0000 | 46 | 0.5196 | 0.5000 |
| [0.533, 0.600) | 8 | 0.5666 | 0.6250 | 76 | 0.5554 | 0.4605 |
| [0.600, 0.667) | 15 | 0.6321 | 0.6000 | 2 | 0.6076 | 0.5000 |
| [0.667, 0.733) | 14 | 0.7063 | 0.4286 | 0 | n/a | n/a |
| [0.733, 0.800) | 24 | 0.7637 | 0.3750 | 0 | n/a | n/a |
| [0.800, 0.867) | 29 | 0.8360 | 0.3793 | 0 | n/a | n/a |
| [0.867, 0.933) | 25 | 0.9012 | 0.6000 | 0 | n/a | n/a |
| [0.933, 1.000) | 6 | 0.9573 | 0.6667 | 0 | n/a | n/a |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 7 | 0.5155 | 0.4286 | 7 | 0.5155 | 0.4286 |
| [0.533, 0.600) | 7 | 0.5784 | 0.2857 | 7 | 0.5784 | 0.2857 |
| [0.600, 0.667) | 24 | 0.6346 | 0.6667 | 24 | 0.6346 | 0.6667 |
| [0.667, 0.733) | 23 | 0.7019 | 0.4783 | 23 | 0.7019 | 0.4783 |
| [0.733, 0.800) | 14 | 0.7625 | 0.4286 | 14 | 0.7625 | 0.4286 |
| [0.800, 0.867) | 19 | 0.8351 | 0.5263 | 19 | 0.8351 | 0.5263 |
| [0.867, 0.933) | 22 | 0.8932 | 0.5909 | 22 | 0.8932 | 0.5909 |
| [0.933, 1.000) | 8 | 0.9459 | 0.6250 | 8 | 0.9459 | 0.6250 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 7 | 0.5227 | 0.7143 | 7 | 0.5227 | 0.7143 |
| [0.533, 0.600) | 10 | 0.5668 | 0.4000 | 10 | 0.5668 | 0.4000 |
| [0.600, 0.667) | 13 | 0.6461 | 0.5385 | 13 | 0.6461 | 0.5385 |
| [0.667, 0.733) | 19 | 0.6950 | 0.5263 | 19 | 0.6950 | 0.5263 |
| [0.733, 0.800) | 21 | 0.7631 | 0.4762 | 21 | 0.7631 | 0.4762 |
| [0.800, 0.867) | 21 | 0.8275 | 0.3333 | 21 | 0.8275 | 0.3333 |
| [0.867, 0.933) | 25 | 0.8935 | 0.4400 | 25 | 0.8935 | 0.4400 |
| [0.933, 1.000) | 8 | 0.9519 | 0.2500 | 8 | 0.9519 | 0.2500 |

### B4 / qs_v2 (doc-level, underpowered), holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | AUROC raw | AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.2484 | 0.1282 | 0.5450 | 0.4321 | 0.6600 | 0.6600 |
| has_phi_direct = raw (T fallback) | 0.8004 | 0.8004 | 1.2920 | 1.2920 | n/a | n/a |
| has_phi_quasi | 0.7831 | 0.5424 | 1.2409 | 0.5892 | n/a | n/a |
| has_coded_id = raw (T fallback) | 0.7629 | 0.7629 | 1.1800 | 1.1800 | n/a | n/a |
| has_staff_pii = raw (T fallback) | 0.1407 | 0.1407 | 0.4544 | 0.4544 | 0.6600 | 0.6600 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.533, 0.600) | 0 | n/a | n/a | 1 | 0.5854 | 1.0000 |
| [0.600, 0.667) | 0 | n/a | n/a | 11 | 0.6451 | 0.4545 |
| [0.667, 0.733) | 0 | n/a | n/a | 15 | 0.6936 | 0.7333 |
| [0.733, 0.800) | 1 | 0.7419 | 1.0000 | 3 | 0.7531 | 1.0000 |
| [0.800, 0.867) | 6 | 0.8365 | 0.6667 | 0 | n/a | n/a |
| [0.867, 0.933) | 15 | 0.9026 | 0.5333 | 0 | n/a | n/a |
| [0.933, 1.000) | 8 | 0.9545 | 0.8750 | 0 | n/a | n/a |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.667, 0.733) | 8 | 0.7072 | 0.0000 | 8 | 0.7072 | 0.0000 |
| [0.733, 0.800) | 8 | 0.7758 | 0.0000 | 8 | 0.7758 | 0.0000 |
| [0.800, 0.867) | 10 | 0.8461 | 0.0000 | 10 | 0.8461 | 0.0000 |
| [0.867, 0.933) | 3 | 0.9128 | 0.0000 | 3 | 0.9128 | 0.0000 |
| [0.933, 1.000) | 1 | 0.9481 | 0.0000 | 1 | 0.9481 | 0.0000 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 0 | n/a | n/a | 11 | 0.5258 | 0.0000 |
| [0.533, 0.600) | 1 | 0.5988 | 0.0000 | 19 | 0.5521 | 0.0000 |
| [0.600, 0.667) | 1 | 0.6641 | 0.0000 | 0 | n/a | n/a |
| [0.667, 0.733) | 8 | 0.7068 | 0.0000 | 0 | n/a | n/a |
| [0.733, 0.800) | 8 | 0.7676 | 0.0000 | 0 | n/a | n/a |
| [0.800, 0.867) | 7 | 0.8366 | 0.0000 | 0 | n/a | n/a |
| [0.867, 0.933) | 3 | 0.8991 | 0.0000 | 0 | n/a | n/a |
| [0.933, 1.000) | 2 | 0.9399 | 0.0000 | 0 | n/a | n/a |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 1 | 0.5146 | 0.0000 | 1 | 0.5146 | 0.0000 |
| [0.600, 0.667) | 3 | 0.6285 | 0.0000 | 3 | 0.6285 | 0.0000 |
| [0.667, 0.733) | 4 | 0.7095 | 0.0000 | 4 | 0.7095 | 0.0000 |
| [0.733, 0.800) | 11 | 0.7535 | 0.0000 | 11 | 0.7535 | 0.0000 |
| [0.800, 0.867) | 7 | 0.8200 | 0.0000 | 7 | 0.8200 | 0.0000 |
| [0.867, 0.933) | 4 | 0.9053 | 0.0000 | 4 | 0.9053 | 0.0000 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.667, 0.733) | 6 | 0.7176 | 0.5000 | 6 | 0.7176 | 0.5000 |
| [0.733, 0.800) | 12 | 0.7664 | 0.5833 | 12 | 0.7664 | 0.5833 |
| [0.800, 0.867) | 7 | 0.8270 | 0.8571 | 7 | 0.8270 | 0.8571 |
| [0.867, 0.933) | 5 | 0.9017 | 0.8000 | 5 | 0.9017 | 0.8000 |

## 5. Routing

### A / qs_v1, test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 24 | 120 | 144 |
| B | 9 | 120 | 1733 | 1862 |
| all | 9 | 144 | 1853 | 2006 |

| trigger | count |
|---|---|
| p_below_t_low | 9 |
| p_in_escalate_band | 1853 |
| role_both | 46 |
| role_patient | 98 |

### A / qs_v1, holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 0 | 20 | 20 |
| B | 0 | 17 | 258 | 275 |
| all | 0 | 17 | 278 | 295 |

| trigger | count |
|---|---|
| p_in_escalate_band | 278 |
| role_both | 6 |
| role_patient | 11 |

### A / qs_v2, test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 0 | 144 | 144 |
| B | 9 | 0 | 1853 | 1862 |
| all | 9 | 0 | 1997 | 2006 |

| trigger | count |
|---|---|
| p_below_t_low | 9 |
| p_in_escalate_band | 1997 |

### A / qs_v2, holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 0 | 20 | 20 |
| B | 0 | 0 | 275 | 275 |
| all | 0 | 0 | 295 | 295 |

| trigger | count |
|---|---|
| p_in_escalate_band | 295 |

### B1 / qs_v1, test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 1 | 31 | 68 | 100 |
| B | 0 | 172 | 401 | 573 |
| all | 1 | 203 | 469 | 673 |

| trigger | count |
|---|---|
| p_below_t_low | 1 |
| p_in_escalate_band | 469 |
| role_both | 20 |
| role_patient | 183 |

### B1 / qs_v1, holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 6 | 14 | 20 |
| B | 0 | 20 | 59 | 79 |
| all | 0 | 26 | 73 | 99 |

| trigger | count |
|---|---|
| p_in_escalate_band | 73 |
| role_both | 2 |
| role_patient | 24 |

### B1 / qs_v2, test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 0 | 100 | 100 |
| B | 0 | 0 | 573 | 573 |
| all | 0 | 0 | 673 | 673 |

| trigger | count |
|---|---|
| p_in_escalate_band | 673 |

### B1 / qs_v2, holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 0 | 20 | 20 |
| B | 0 | 0 | 79 | 79 |
| all | 0 | 0 | 99 | 99 |

| trigger | count |
|---|---|
| p_in_escalate_band | 99 |

### B2 / qs_v1, test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 1 | 30 | 57 | 88 |
| B | 2 | 56 | 174 | 232 |
| all | 3 | 86 | 231 | 320 |

| trigger | count |
|---|---|
| p_below_t_low | 3 |
| p_in_escalate_band | 231 |
| role_both | 11 |
| role_patient | 75 |

### B2 / qs_v1, holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 3 | 17 | 20 |
| B | 0 | 2 | 28 | 30 |
| all | 0 | 5 | 45 | 50 |

| trigger | count |
|---|---|
| p_in_escalate_band | 45 |
| role_patient | 5 |

### B2 / qs_v2, test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 2 | 0 | 86 | 88 |
| B | 4 | 0 | 228 | 232 |
| all | 6 | 0 | 314 | 320 |

| trigger | count |
|---|---|
| p_below_t_low | 6 |
| p_in_escalate_band | 314 |

### B2 / qs_v2, holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 0 | 20 | 20 |
| B | 0 | 0 | 30 | 30 |
| all | 0 | 0 | 50 | 50 |

| trigger | count |
|---|---|
| p_in_escalate_band | 50 |

### B3 / qs_v1 (doc-level, underpowered), test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 2 | 34 | 49 | 85 |
| B | 1 | 31 | 70 | 102 |
| all | 3 | 65 | 119 | 187 |

| trigger | count |
|---|---|
| p_at_or_above_t_high | 6 |
| p_below_t_low | 3 |
| p_in_escalate_band | 119 |
| role_both | 10 |
| role_patient | 51 |

### B3 / qs_v1 (doc-level, underpowered), holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 4 | 16 | 20 |
| B | 0 | 0 | 11 | 11 |
| all | 0 | 4 | 27 | 31 |

| trigger | count |
|---|---|
| p_in_escalate_band | 27 |
| role_both | 1 |
| role_patient | 3 |

### B3 / qs_v2 (doc-level, underpowered), test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 6 | 1 | 78 | 85 |
| B | 4 | 0 | 98 | 102 |
| all | 10 | 1 | 176 | 187 |

| trigger | count |
|---|---|
| p_at_or_above_t_high | 1 |
| p_below_t_low | 10 |
| p_in_escalate_band | 176 |

### B3 / qs_v2 (doc-level, underpowered), holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 0 | 20 | 20 |
| B | 0 | 0 | 11 | 11 |
| all | 0 | 0 | 31 | 31 |

| trigger | count |
|---|---|
| p_in_escalate_band | 31 |

### B4 / qs_v1 (doc-level, underpowered), test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 2 | 37 | 41 | 80 |
| B | 1 | 15 | 28 | 44 |
| all | 3 | 52 | 69 | 124 |

| trigger | count |
|---|---|
| p_at_or_above_t_high | 14 |
| p_below_t_low | 3 |
| p_in_escalate_band | 69 |
| role_both | 8 |
| role_patient | 37 |

### B4 / qs_v1 (doc-level, underpowered), holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 6 | 14 | 20 |
| B | 0 | 0 | 10 | 10 |
| all | 0 | 6 | 24 | 30 |

| trigger | count |
|---|---|
| p_at_or_above_t_high | 2 |
| p_in_escalate_band | 24 |
| role_both | 1 |
| role_patient | 3 |

### B4 / qs_v2 (doc-level, underpowered), test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 6 | 0 | 74 | 80 |
| B | 1 | 0 | 43 | 44 |
| all | 7 | 0 | 117 | 124 |

| trigger | count |
|---|---|
| p_below_t_low | 7 |
| p_in_escalate_band | 117 |

### B4 / qs_v2 (doc-level, underpowered), holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 0 | 20 | 20 |
| B | 0 | 0 | 10 | 10 |
| all | 0 | 0 | 30 | 30 |

| trigger | count |
|---|---|
| p_in_escalate_band | 30 |

## 6. Speed

Per-unit latency is not comparable across arms (units range from 256-token chunks to whole documents); compare the per-document row or the length rows. Batched runs were made for arms A and B1 only: batches of eight 2k-8k-token states exceed the 8 GB M2 (swapping, NaN).

### A / qs_v1

Hardware: **Apple M2, 8.0 GB RAM, device mps (Apple MPS), torch 2.14.0**. Warmup calls excluded: 40. Batch-1 outliers (> 5x the median of similar-length calls): 1. Batch-1 ms/token, end of run vs start: 1.48x. laya autocast: batch-1 off, batched off (on MPS, fp16 autocast starts at 5 question rows, so qs_v2 runs fp16 and qs_v1 fp32).

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 3603 | 685.8 | 969.6 | 1064.2 | 710.9 | 1.41 |
| per unit, batched (amortized: batch time / batch size) | 3603 | 902.1 | 1412.6 | 1526.6 | 985.9 | 1.01 |
| per document (sum of units, batch-1; incl. calib docs) | 250 | 8076.2 | 30341.6 | 39449.5 | 10245.0 | 0.10 |
| per unit, batch-1, <1k tokens | 3603 | 685.8 | 969.6 | 1064.2 | 710.9 | 1.41 |

### A / qs_v2

Hardware: **Apple M2, 8.0 GB RAM, device mps (Apple MPS), torch 2.14.0**. Warmup calls excluded: 20. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 1.38x. laya autocast: batch-1 on, batched on (on MPS, fp16 autocast starts at 5 question rows, so qs_v2 runs fp16 and qs_v1 fp32).

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 3603 | 928.3 | 1078.3 | 1305.2 | 881.5 | 1.13 |
| per unit, batched (amortized: batch time / batch size) | 3603 | 1014.1 | 1178.3 | 1619.8 | 1046.6 | 0.96 |
| per document (sum of units, batch-1; incl. calib docs) | 250 | 10221.6 | 36889.4 | 49450.5 | 12704.5 | 0.08 |
| per unit, batch-1, <1k tokens | 3603 | 928.3 | 1078.3 | 1305.2 | 881.5 | 1.13 |

### B1 / qs_v1

Hardware: **Apple M2, 8.0 GB RAM, device mps (Apple MPS), torch 2.14.0**. Warmup calls excluded: 20. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 0.96x. laya autocast: batch-1 off, batched off (on MPS, fp16 autocast starts at 5 question rows, so qs_v2 runs fp16 and qs_v1 fp32).

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 1215 | 1088.4 | 1146.4 | 1200.8 | 990.4 | 1.01 |
| per unit, batched (amortized: batch time / batch size) | 1215 | 1011.2 | 1139.8 | 1342.6 | 1033.8 | 0.97 |
| per document (sum of units, batch-1; incl. calib docs) | 250 | 3851.5 | 14389.9 | 16929.0 | 4813.4 | 0.21 |
| per unit, batch-1, <1k tokens | 1215 | 1088.4 | 1146.4 | 1200.8 | 990.4 | 1.01 |

### B1 / qs_v2

Hardware: **Apple M2, 8.0 GB RAM, device mps (Apple MPS), torch 2.14.0**. Warmup calls excluded: 20. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 0.90x. laya autocast: batch-1 on, batched on (on MPS, fp16 autocast starts at 5 question rows, so qs_v2 runs fp16 and qs_v1 fp32).

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 1215 | 1056.4 | 1206.7 | 1515.6 | 974.4 | 1.03 |
| per unit, batched (amortized: batch time / batch size) | 1215 | 1241.6 | 1432.1 | 1974.0 | 1278.3 | 0.78 |
| per document (sum of units, batch-1; incl. calib docs) | 250 | 3756.7 | 14431.3 | 16844.0 | 4735.6 | 0.21 |
| per unit, batch-1, <1k tokens | 1215 | 1056.4 | 1206.7 | 1515.6 | 974.4 | 1.03 |

### B2 / qs_v1

Hardware: **Apple M2, 8.0 GB RAM, device mps (Apple MPS), torch 2.14.0**. Warmup calls excluded: 10. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 1.15x. laya autocast: batch-1 off, batched not run (on MPS, fp16 autocast starts at 5 question rows, so qs_v2 runs fp16 and qs_v1 fp32).

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 593 | 2544.6 | 4104.7 | 4583.7 | 2280.0 | 0.44 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 250 | 4254.3 | 15799.8 | 23391.3 | 5408.2 | 0.18 |
| per unit, batch-1, <1k tokens | 182 | 797.4 | 1749.2 | 2114.2 | 892.3 | 1.12 |
| per unit, batch-1, 1-2k tokens | 403 | 2745.8 | 4246.1 | 4709.4 | 2887.5 | 0.35 |
| per unit, batch-1, 2-4k tokens | 8 | 3162.3 | 3703.7 | 3754.7 | 3249.4 | 0.31 |

### B2 / qs_v2

Hardware: **Apple M2, 8.0 GB RAM, device mps (Apple MPS), torch 2.14.0**. Warmup calls excluded: 10. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 0.99x. laya autocast: batch-1 on, batched not run (on MPS, fp16 autocast starts at 5 question rows, so qs_v2 runs fp16 and qs_v1 fp32).

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 593 | 2024.0 | 2312.1 | 2540.6 | 1645.2 | 0.61 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 250 | 3002.1 | 11941.1 | 13571.1 | 3902.5 | 0.26 |
| per unit, batch-1, <1k tokens | 182 | 636.4 | 1091.4 | 1117.9 | 641.0 | 1.56 |
| per unit, batch-1, 1-2k tokens | 403 | 2136.6 | 2316.0 | 2539.9 | 2081.3 | 0.48 |
| per unit, batch-1, 2-4k tokens | 8 | 2519.3 | 2562.5 | 2567.8 | 2525.6 | 0.40 |

### B3 / qs_v1 (doc-level, underpowered)

Hardware: **Apple M2, 8.0 GB RAM, device mps (Apple MPS), torch 2.14.0**. Warmup calls excluded: 10. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 1.07x. laya autocast: batch-1 off, batched not run (on MPS, fp16 autocast starts at 5 question rows, so qs_v2 runs fp16 and qs_v1 fp32).

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 345 | 3980.1 | 7169.9 | 8051.5 | 3832.7 | 0.26 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 250 | 3670.7 | 16928.8 | 20078.9 | 5289.2 | 0.19 |
| per unit, batch-1, <1k tokens | 112 | 620.4 | 1063.5 | 1239.7 | 639.3 | 1.56 |
| per unit, batch-1, 1-2k tokens | 26 | 1916.1 | 2669.3 | 2771.4 | 2011.7 | 0.50 |
| per unit, batch-1, 2-4k tokens | 207 | 6359.9 | 7451.4 | 8932.1 | 5789.3 | 0.17 |

### B3 / qs_v2 (doc-level, underpowered)

Hardware: **Apple M2, 8.0 GB RAM, device mps (Apple MPS), torch 2.14.0**. Warmup calls excluded: 10. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 1.20x. laya autocast: batch-1 on, batched not run (on MPS, fp16 autocast starts at 5 question rows, so qs_v2 runs fp16 and qs_v1 fp32).

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 345 | 4512.9 | 8729.9 | 9496.7 | 4342.8 | 0.23 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 250 | 4497.2 | 18643.7 | 21595.2 | 5993.1 | 0.17 |
| per unit, batch-1, <1k tokens | 112 | 741.7 | 1358.5 | 1492.8 | 783.0 | 1.28 |
| per unit, batch-1, 1-2k tokens | 26 | 2367.9 | 3153.4 | 3360.3 | 2376.0 | 0.42 |
| per unit, batch-1, 2-4k tokens | 207 | 6831.3 | 8950.9 | 9680.8 | 6516.0 | 0.15 |

### B4 / qs_v1 (doc-level, underpowered)

Hardware: **Apple M2, 8.0 GB RAM, device mps (Apple MPS), torch 2.14.0**. Warmup calls excluded: 10. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 1.31x. laya autocast: batch-1 off, batched not run (on MPS, fp16 autocast starts at 5 question rows, so qs_v2 runs fp16 and qs_v1 fp32).

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 250 | 5532.3 | 38867.8 | 47166.2 | 10332.0 | 0.10 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 250 | 5532.3 | 38867.8 | 47166.2 | 10332.0 | 0.10 |
| per unit, batch-1, <1k tokens | 93 | 913.3 | 3407.3 | 4119.9 | 1195.3 | 0.84 |
| per unit, batch-1, 1-2k tokens | 9 | 2470.1 | 5491.2 | 5786.3 | 3241.2 | 0.31 |
| per unit, batch-1, 2-4k tokens | 90 | 7047.0 | 12606.6 | 15488.5 | 7673.8 | 0.13 |
| per unit, batch-1, 4-8k tokens | 40 | 25637.3 | 43228.2 | 47833.1 | 26790.2 | 0.04 |
| per unit, batch-1, >8k tokens | 18 | 35949.3 | 47777.9 | 48680.9 | 37800.8 | 0.03 |

### B4 / qs_v2 (doc-level, underpowered)

Hardware: **Apple M2, 8.0 GB RAM, device mps (Apple MPS), torch 2.14.0**. Warmup calls excluded: 10. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 1.56x. laya autocast: batch-1 on, batched not run (on MPS, fp16 autocast starts at 5 question rows, so qs_v2 runs fp16 and qs_v1 fp32).

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 250 | 5923.7 | 37433.3 | 43250.8 | 10468.6 | 0.10 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 250 | 5923.7 | 37433.3 | 43250.8 | 10468.6 | 0.10 |
| per unit, batch-1, <1k tokens | 93 | 1061.4 | 3353.1 | 4064.9 | 1300.6 | 0.77 |
| per unit, batch-1, 1-2k tokens | 9 | 3291.1 | 5542.5 | 5841.7 | 3536.1 | 0.28 |
| per unit, batch-1, 2-4k tokens | 90 | 7682.3 | 12146.4 | 13570.1 | 7912.5 | 0.13 |
| per unit, batch-1, 4-8k tokens | 40 | 26160.4 | 41902.0 | 45693.4 | 27152.6 | 0.04 |
| per unit, batch-1, >8k tokens | 18 | 36991.7 | 43039.5 | 45553.3 | 37008.3 | 0.03 |

## 7. Slices

Slices with n < 30 are marked `*`.

### A / qs_v1, test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log | 97 | 8 | 10 | 1.0000 | 0.0103 | 0 | 0.8866 |
| doc_type | crf_page | 113 | 14 | 26 | 1.0000 | 0.0000 | 0 | 0.7788 |
| doc_type | csr_patient_narrative | 276 | 14 | 23 | 1.0000 | 0.0000 | 0 | 0.9312 |
| doc_type | delegation_log | 43 | 5 | 5 | 1.0000 | 0.0233 | 0 | 0.9535 |
| doc_type | deviation_log | 106 | 10 | 8 | 1.0000 | 0.0000 | 0 | 0.9245 |
| doc_type | icf_signature_page * | 28 | 7 | 6 | 1.0000 | 0.0357 | 0 | 0.9286 |
| doc_type | lab_report | 76 | 11 | 16 | 1.0000 | 0.0132 | 0 | 0.8289 |
| doc_type | monitoring_visit_report | 349 | 11 | 19 | 1.0000 | 0.0000 | 0 | 0.9456 |
| doc_type | protocol_section | 470 | 16 | 0 | n/a | 0.0021 | 0 | 1.0000 |
| doc_type | sae_cioms | 75 | 14 | 18 | 1.0000 | 0.0533 | 0 | 0.7867 |
| doc_type | site_correspondence | 373 | 14 | 13 | 1.0000 | 0.0000 | 0 | 0.9651 |
| hard_negative | no | 1512 | 91 | 94 | 1.0000 | 0.0053 | 0 | 0.9444 |
| hard_negative | yes | 494 | 33 | 50 | 1.0000 | 0.0020 | 0 | 0.9109 |
| lang | de * | 7 | 4 | 5 | 1.0000 | 0.0000 | 0 | 0.2857 |
| lang | en | 1975 | 107 | 123 | 1.0000 | 0.0046 | 0 | 0.9453 |
| lang | es * | 12 | 7 | 8 | 1.0000 | 0.0000 | 0 | 0.4167 |
| lang | pl * | 12 | 6 | 8 | 1.0000 | 0.0000 | 0 | 0.3333 |
| length_bucket | long | 743 | 24 | 21 | 1.0000 | 0.0000 | 0 | 0.9758 |
| length_bucket | medium | 538 | 41 | 64 | 1.0000 | 0.0093 | 0 | 0.8829 |
| length_bucket | short | 134 | 46 | 45 | 1.0000 | 0.0224 | 0 | 0.7463 |
| length_bucket | xl | 591 | 13 | 14 | 1.0000 | 0.0017 | 0 | 0.9780 |
| perturbation | email_quoting | 373 | 14 | 13 | 1.0000 | 0.0000 | 0 | 0.9651 |
| perturbation | headers_footers | 752 | 52 | 64 | 1.0000 | 0.0013 | 0 | 0.9309 |
| perturbation | line_wrap | 621 | 31 | 37 | 1.0000 | 0.0048 | 0 | 0.9436 |
| perturbation | none | 524 | 30 | 26 | 1.0000 | 0.0076 | 0 | 0.9561 |
| perturbation | ocr_noise | 200 | 14 | 25 | 1.0000 | 0.0050 | 0 | 0.8950 |
| perturbation | table | 239 | 27 | 40 | 1.0000 | 0.0084 | 0 | 0.8410 |
| pii_depth | early | 277 | 7 | 10 | 1.0000 | 0.0000 | 0 | 0.9639 |
| pii_depth | late | 61 | 2 | 2 | 1.0000 | 0.0000 | 0 | 0.9672 |
| pii_depth | middle | 63 | 2 | 3 | 1.0000 | 0.0000 | 0 | 0.9524 |
| pii_depth | none | 1605 | 113 | 129 | 1.0000 | 0.0056 | 0 | 0.9296 |
| pre_redacted | no | 1852 | 109 | 123 | 1.0000 | 0.0038 | 0 | 0.9406 |
| pre_redacted | yes | 154 | 15 | 21 | 1.0000 | 0.0130 | 0 | 0.8831 |
| split_span | no | 1999 | 124 | 137 | 1.0000 | 0.0045 | 0 | 0.9395 |
| split_span | yes * | 7 | 6 | 7 | 1.0000 | 0.0000 | 0 | 0.0000 |
| truncated | no | 2006 | 124 | 144 | 1.0000 | 0.0045 | 0 | 0.9362 |

Value kinds of missed spans (false forwards):

none

### A / qs_v1, holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 295 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.9322 |
| hard_negative | no | 234 | 23 | 15 | 1.0000 | 0.0000 | 0 | 0.9359 |
| hard_negative | yes | 61 | 7 | 5 | 1.0000 | 0.0000 | 0 | 0.9180 |
| lang | en | 295 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.9322 |
| length_bucket | medium | 250 | 19 | 15 | 1.0000 | 0.0000 | 0 | 0.9400 |
| length_bucket | short | 45 | 11 | 5 | 1.0000 | 0.0000 | 0 | 0.8889 |
| perturbation | headers_footers | 119 | 12 | 7 | 1.0000 | 0.0000 | 0 | 0.9412 |
| perturbation | line_wrap | 79 | 9 | 7 | 1.0000 | 0.0000 | 0 | 0.9114 |
| perturbation | none | 109 | 10 | 6 | 1.0000 | 0.0000 | 0 | 0.9450 |
| perturbation | ocr_noise | 36 | 4 | 3 | 1.0000 | 0.0000 | 0 | 0.9167 |
| pii_depth | none | 295 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.9322 |
| pre_redacted | no | 283 | 29 | 19 | 1.0000 | 0.0000 | 0 | 0.9329 |
| pre_redacted | yes * | 12 | 1 | 1 | 1.0000 | 0.0000 | 0 | 0.9167 |
| split_span | no | 295 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.9322 |
| truncated | no | 295 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.9322 |

Value kinds of missed spans (false forwards):

none

### A / qs_v2, test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log | 97 | 8 | 10 | 1.0000 | 0.0103 | 0 | 0.8866 |
| doc_type | crf_page | 113 | 14 | 26 | 1.0000 | 0.0000 | 0 | 0.7788 |
| doc_type | csr_patient_narrative | 276 | 14 | 23 | 1.0000 | 0.0000 | 0 | 0.9312 |
| doc_type | delegation_log | 43 | 5 | 5 | 1.0000 | 0.0233 | 0 | 0.9535 |
| doc_type | deviation_log | 106 | 10 | 8 | 1.0000 | 0.0000 | 0 | 0.9245 |
| doc_type | icf_signature_page * | 28 | 7 | 6 | 1.0000 | 0.0357 | 0 | 0.9286 |
| doc_type | lab_report | 76 | 11 | 16 | 1.0000 | 0.0132 | 0 | 0.8289 |
| doc_type | monitoring_visit_report | 349 | 11 | 19 | 1.0000 | 0.0000 | 0 | 0.9456 |
| doc_type | protocol_section | 470 | 16 | 0 | n/a | 0.0021 | 0 | 1.0000 |
| doc_type | sae_cioms | 75 | 14 | 18 | 1.0000 | 0.0533 | 0 | 0.7867 |
| doc_type | site_correspondence | 373 | 14 | 13 | 1.0000 | 0.0000 | 0 | 0.9651 |
| hard_negative | no | 1512 | 91 | 94 | 1.0000 | 0.0053 | 0 | 0.9438 |
| hard_negative | yes | 494 | 33 | 50 | 1.0000 | 0.0020 | 0 | 0.9130 |
| lang | de * | 7 | 4 | 5 | 1.0000 | 0.0000 | 0 | 0.2857 |
| lang | en | 1975 | 107 | 123 | 1.0000 | 0.0046 | 0 | 0.9453 |
| lang | es * | 12 | 7 | 8 | 1.0000 | 0.0000 | 0 | 0.4167 |
| lang | pl * | 12 | 6 | 8 | 1.0000 | 0.0000 | 0 | 0.3333 |
| length_bucket | long | 743 | 24 | 21 | 1.0000 | 0.0000 | 0 | 0.9744 |
| length_bucket | medium | 538 | 41 | 64 | 1.0000 | 0.0093 | 0 | 0.8829 |
| length_bucket | short | 134 | 46 | 45 | 1.0000 | 0.0224 | 0 | 0.7463 |
| length_bucket | xl | 591 | 13 | 14 | 1.0000 | 0.0017 | 0 | 0.9797 |
| perturbation | email_quoting | 373 | 14 | 13 | 1.0000 | 0.0000 | 0 | 0.9651 |
| perturbation | headers_footers | 752 | 52 | 64 | 1.0000 | 0.0013 | 0 | 0.9309 |
| perturbation | line_wrap | 621 | 31 | 37 | 1.0000 | 0.0048 | 0 | 0.9436 |
| perturbation | none | 524 | 30 | 26 | 1.0000 | 0.0076 | 0 | 0.9561 |
| perturbation | ocr_noise | 200 | 14 | 25 | 1.0000 | 0.0050 | 0 | 0.8900 |
| perturbation | table | 239 | 27 | 40 | 1.0000 | 0.0084 | 0 | 0.8410 |
| pii_depth | early | 277 | 7 | 10 | 1.0000 | 0.0000 | 0 | 0.9603 |
| pii_depth | late | 61 | 2 | 2 | 1.0000 | 0.0000 | 0 | 0.9672 |
| pii_depth | middle | 63 | 2 | 3 | 1.0000 | 0.0000 | 0 | 0.9524 |
| pii_depth | none | 1605 | 113 | 129 | 1.0000 | 0.0056 | 0 | 0.9302 |
| pre_redacted | no | 1852 | 109 | 123 | 1.0000 | 0.0038 | 0 | 0.9406 |
| pre_redacted | yes | 154 | 15 | 21 | 1.0000 | 0.0130 | 0 | 0.8831 |
| split_span | no | 1999 | 124 | 137 | 1.0000 | 0.0045 | 0 | 0.9395 |
| split_span | yes * | 7 | 6 | 7 | 1.0000 | 0.0000 | 0 | 0.0000 |
| truncated | no | 2006 | 124 | 144 | 1.0000 | 0.0045 | 0 | 0.9362 |

Value kinds of missed spans (false forwards):

none

### A / qs_v2, holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 295 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.9322 |
| hard_negative | no | 234 | 23 | 15 | 1.0000 | 0.0000 | 0 | 0.9359 |
| hard_negative | yes | 61 | 7 | 5 | 1.0000 | 0.0000 | 0 | 0.9180 |
| lang | en | 295 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.9322 |
| length_bucket | medium | 250 | 19 | 15 | 1.0000 | 0.0000 | 0 | 0.9400 |
| length_bucket | short | 45 | 11 | 5 | 1.0000 | 0.0000 | 0 | 0.8889 |
| perturbation | headers_footers | 119 | 12 | 7 | 1.0000 | 0.0000 | 0 | 0.9412 |
| perturbation | line_wrap | 79 | 9 | 7 | 1.0000 | 0.0000 | 0 | 0.9114 |
| perturbation | none | 109 | 10 | 6 | 1.0000 | 0.0000 | 0 | 0.9450 |
| perturbation | ocr_noise | 36 | 4 | 3 | 1.0000 | 0.0000 | 0 | 0.9167 |
| pii_depth | none | 295 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.9322 |
| pre_redacted | no | 283 | 29 | 19 | 1.0000 | 0.0000 | 0 | 0.9329 |
| pre_redacted | yes * | 12 | 1 | 1 | 1.0000 | 0.0000 | 0 | 0.9167 |
| split_span | no | 295 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.9322 |
| truncated | no | 295 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.9322 |

Value kinds of missed spans (false forwards):

none

### B1 / qs_v1, test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log | 32 | 8 | 4 | 1.0000 | 0.0000 | 0 | 0.1250 |
| doc_type | crf_page | 54 | 14 | 17 | 1.0000 | 0.0000 | 0 | 0.3889 |
| doc_type | csr_patient_narrative | 90 | 14 | 15 | 1.0000 | 0.0000 | 0 | 0.2111 |
| doc_type | delegation_log * | 15 | 5 | 5 | 1.0000 | 0.0000 | 0 | 0.3333 |
| doc_type | deviation_log | 37 | 10 | 6 | 1.0000 | 0.0000 | 0 | 0.2162 |
| doc_type | icf_signature_page * | 10 | 7 | 6 | 1.0000 | 0.0000 | 0 | 0.6000 |
| doc_type | lab_report * | 27 | 11 | 9 | 1.0000 | 0.0000 | 0 | 0.3333 |
| doc_type | monitoring_visit_report | 111 | 11 | 15 | 0.9333 | 0.0090 | 1 | 0.1351 |
| doc_type | protocol_section | 150 | 16 | 0 | n/a | 0.0000 | 0 | 0.0000 |
| doc_type | sae_cioms | 30 | 14 | 13 | 1.0000 | 0.0000 | 0 | 0.4000 |
| doc_type | site_correspondence | 117 | 14 | 10 | 1.0000 | 0.0000 | 0 | 0.0769 |
| hard_negative | no | 507 | 91 | 68 | 1.0000 | 0.0000 | 0 | 0.1558 |
| hard_negative | yes | 166 | 33 | 32 | 0.9688 | 0.0060 | 1 | 0.1747 |
| lang | de * | 4 | 4 | 4 | 1.0000 | 0.0000 | 0 | 0.5000 |
| lang | en | 656 | 107 | 86 | 0.9884 | 0.0015 | 1 | 0.1463 |
| lang | es * | 7 | 7 | 5 | 1.0000 | 0.0000 | 0 | 0.5714 |
| lang | pl * | 6 | 6 | 5 | 1.0000 | 0.0000 | 0 | 1.0000 |
| length_bucket | long | 235 | 24 | 16 | 1.0000 | 0.0000 | 0 | 0.0723 |
| length_bucket | medium | 192 | 41 | 39 | 1.0000 | 0.0000 | 0 | 0.2292 |
| length_bucket | short | 60 | 46 | 34 | 1.0000 | 0.0000 | 0 | 0.5667 |
| length_bucket | xl | 186 | 13 | 11 | 0.9091 | 0.0054 | 1 | 0.0699 |
| perturbation | email_quoting | 117 | 14 | 10 | 1.0000 | 0.0000 | 0 | 0.0769 |
| perturbation | headers_footers | 254 | 52 | 42 | 0.9762 | 0.0039 | 1 | 0.1732 |
| perturbation | line_wrap | 202 | 31 | 28 | 0.9643 | 0.0050 | 1 | 0.1535 |
| perturbation | none | 172 | 30 | 19 | 1.0000 | 0.0000 | 0 | 0.1337 |
| perturbation | ocr_noise | 68 | 14 | 15 | 1.0000 | 0.0000 | 0 | 0.2206 |
| perturbation | table | 94 | 27 | 25 | 1.0000 | 0.0000 | 0 | 0.2872 |
| pii_depth | early | 87 | 7 | 7 | 1.0000 | 0.0000 | 0 | 0.1034 |
| pii_depth | late * | 19 | 2 | 2 | 1.0000 | 0.0000 | 0 | 0.1053 |
| pii_depth | middle * | 20 | 2 | 2 | 1.0000 | 0.0000 | 0 | 0.1500 |
| pii_depth | none | 547 | 113 | 89 | 0.9888 | 0.0018 | 1 | 0.1718 |
| pre_redacted | no | 621 | 109 | 84 | 0.9881 | 0.0016 | 1 | 0.1465 |
| pre_redacted | yes | 52 | 15 | 16 | 1.0000 | 0.0000 | 0 | 0.3269 |
| split_span | no | 669 | 124 | 97 | 0.9897 | 0.0015 | 1 | 0.1555 |
| split_span | yes * | 4 | 3 | 3 | 1.0000 | 0.0000 | 0 | 1.0000 |
| truncated | no | 673 | 124 | 100 | 0.9900 | 0.0015 | 1 | 0.1605 |

Value kinds of missed spans (false forwards):

| value_kind | false forwards |
|---|---|
| email | 1 |
| person_name | 1 |

### B1 / qs_v1, holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 99 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.2121 |
| hard_negative | no | 78 | 23 | 15 | 1.0000 | 0.0000 | 0 | 0.2051 |
| hard_negative | yes * | 21 | 7 | 5 | 1.0000 | 0.0000 | 0 | 0.2381 |
| lang | en | 99 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.2121 |
| length_bucket | medium | 82 | 19 | 15 | 1.0000 | 0.0000 | 0 | 0.1829 |
| length_bucket | short * | 17 | 11 | 5 | 1.0000 | 0.0000 | 0 | 0.3529 |
| perturbation | headers_footers | 40 | 12 | 7 | 1.0000 | 0.0000 | 0 | 0.2000 |
| perturbation | line_wrap * | 26 | 9 | 7 | 1.0000 | 0.0000 | 0 | 0.3077 |
| perturbation | none | 37 | 10 | 6 | 1.0000 | 0.0000 | 0 | 0.1622 |
| perturbation | ocr_noise * | 12 | 4 | 3 | 1.0000 | 0.0000 | 0 | 0.2500 |
| pii_depth | none | 99 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.2121 |
| pre_redacted | no | 95 | 29 | 19 | 1.0000 | 0.0000 | 0 | 0.2105 |
| pre_redacted | yes * | 4 | 1 | 1 | 1.0000 | 0.0000 | 0 | 0.2500 |
| split_span | no | 99 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.2121 |
| truncated | no | 99 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.2121 |

Value kinds of missed spans (false forwards):

none

### B1 / qs_v2, test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log | 32 | 8 | 4 | 1.0000 | 0.0000 | 0 | 0.1250 |
| doc_type | crf_page | 54 | 14 | 17 | 1.0000 | 0.0000 | 0 | 0.3889 |
| doc_type | csr_patient_narrative | 90 | 14 | 15 | 1.0000 | 0.0000 | 0 | 0.2111 |
| doc_type | delegation_log * | 15 | 5 | 5 | 1.0000 | 0.0000 | 0 | 0.3333 |
| doc_type | deviation_log | 37 | 10 | 6 | 1.0000 | 0.0000 | 0 | 0.2162 |
| doc_type | icf_signature_page * | 10 | 7 | 6 | 1.0000 | 0.0000 | 0 | 0.6000 |
| doc_type | lab_report * | 27 | 11 | 9 | 1.0000 | 0.0000 | 0 | 0.3333 |
| doc_type | monitoring_visit_report | 111 | 11 | 15 | 1.0000 | 0.0000 | 0 | 0.1351 |
| doc_type | protocol_section | 150 | 16 | 0 | n/a | 0.0000 | 0 | 0.0000 |
| doc_type | sae_cioms | 30 | 14 | 13 | 1.0000 | 0.0000 | 0 | 0.4000 |
| doc_type | site_correspondence | 117 | 14 | 10 | 1.0000 | 0.0000 | 0 | 0.0769 |
| hard_negative | no | 507 | 91 | 68 | 1.0000 | 0.0000 | 0 | 0.1558 |
| hard_negative | yes | 166 | 33 | 32 | 1.0000 | 0.0000 | 0 | 0.1747 |
| lang | de * | 4 | 4 | 4 | 1.0000 | 0.0000 | 0 | 0.5000 |
| lang | en | 656 | 107 | 86 | 1.0000 | 0.0000 | 0 | 0.1463 |
| lang | es * | 7 | 7 | 5 | 1.0000 | 0.0000 | 0 | 0.5714 |
| lang | pl * | 6 | 6 | 5 | 1.0000 | 0.0000 | 0 | 1.0000 |
| length_bucket | long | 235 | 24 | 16 | 1.0000 | 0.0000 | 0 | 0.0723 |
| length_bucket | medium | 192 | 41 | 39 | 1.0000 | 0.0000 | 0 | 0.2292 |
| length_bucket | short | 60 | 46 | 34 | 1.0000 | 0.0000 | 0 | 0.5667 |
| length_bucket | xl | 186 | 13 | 11 | 1.0000 | 0.0000 | 0 | 0.0699 |
| perturbation | email_quoting | 117 | 14 | 10 | 1.0000 | 0.0000 | 0 | 0.0769 |
| perturbation | headers_footers | 254 | 52 | 42 | 1.0000 | 0.0000 | 0 | 0.1732 |
| perturbation | line_wrap | 202 | 31 | 28 | 1.0000 | 0.0000 | 0 | 0.1535 |
| perturbation | none | 172 | 30 | 19 | 1.0000 | 0.0000 | 0 | 0.1337 |
| perturbation | ocr_noise | 68 | 14 | 15 | 1.0000 | 0.0000 | 0 | 0.2206 |
| perturbation | table | 94 | 27 | 25 | 1.0000 | 0.0000 | 0 | 0.2872 |
| pii_depth | early | 87 | 7 | 7 | 1.0000 | 0.0000 | 0 | 0.1034 |
| pii_depth | late * | 19 | 2 | 2 | 1.0000 | 0.0000 | 0 | 0.1053 |
| pii_depth | middle * | 20 | 2 | 2 | 1.0000 | 0.0000 | 0 | 0.1500 |
| pii_depth | none | 547 | 113 | 89 | 1.0000 | 0.0000 | 0 | 0.1718 |
| pre_redacted | no | 621 | 109 | 84 | 1.0000 | 0.0000 | 0 | 0.1465 |
| pre_redacted | yes | 52 | 15 | 16 | 1.0000 | 0.0000 | 0 | 0.3269 |
| split_span | no | 669 | 124 | 97 | 1.0000 | 0.0000 | 0 | 0.1555 |
| split_span | yes * | 4 | 3 | 3 | 1.0000 | 0.0000 | 0 | 1.0000 |
| truncated | no | 673 | 124 | 100 | 1.0000 | 0.0000 | 0 | 0.1605 |

Value kinds of missed spans (false forwards):

none

### B1 / qs_v2, holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 99 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.2121 |
| hard_negative | no | 78 | 23 | 15 | 1.0000 | 0.0000 | 0 | 0.2051 |
| hard_negative | yes * | 21 | 7 | 5 | 1.0000 | 0.0000 | 0 | 0.2381 |
| lang | en | 99 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.2121 |
| length_bucket | medium | 82 | 19 | 15 | 1.0000 | 0.0000 | 0 | 0.1829 |
| length_bucket | short * | 17 | 11 | 5 | 1.0000 | 0.0000 | 0 | 0.3529 |
| perturbation | headers_footers | 40 | 12 | 7 | 1.0000 | 0.0000 | 0 | 0.2000 |
| perturbation | line_wrap * | 26 | 9 | 7 | 1.0000 | 0.0000 | 0 | 0.3077 |
| perturbation | none | 37 | 10 | 6 | 1.0000 | 0.0000 | 0 | 0.1622 |
| perturbation | ocr_noise * | 12 | 4 | 3 | 1.0000 | 0.0000 | 0 | 0.2500 |
| pii_depth | none | 99 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.2121 |
| pre_redacted | no | 95 | 29 | 19 | 1.0000 | 0.0000 | 0 | 0.2105 |
| pre_redacted | yes * | 4 | 1 | 1 | 1.0000 | 0.0000 | 0 | 0.2500 |
| split_span | no | 99 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.2121 |
| truncated | no | 99 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.2121 |

Value kinds of missed spans (false forwards):

none

### B2 / qs_v1, test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log * | 17 | 8 | 2 | 1.0000 | 0.0000 | 0 | 0.1176 |
| doc_type | crf_page * | 23 | 14 | 7 | 1.0000 | 0.0435 | 0 | 0.3043 |
| doc_type | csr_patient_narrative | 43 | 14 | 15 | 0.9333 | 0.0233 | 0 | 0.3953 |
| doc_type | delegation_log * | 8 | 5 | 5 | 1.0000 | 0.0000 | 0 | 0.6250 |
| doc_type | deviation_log * | 18 | 10 | 6 | 1.0000 | 0.0000 | 0 | 0.3333 |
| doc_type | icf_signature_page * | 7 | 7 | 6 | 1.0000 | 0.0000 | 0 | 0.8571 |
| doc_type | lab_report * | 15 | 11 | 9 | 1.0000 | 0.0000 | 0 | 0.6000 |
| doc_type | monitoring_visit_report | 49 | 11 | 15 | 1.0000 | 0.0000 | 0 | 0.3061 |
| doc_type | protocol_section | 67 | 16 | 0 | n/a | 0.0000 | 0 | 0.0000 |
| doc_type | sae_cioms * | 18 | 14 | 13 | 0.9231 | 0.0556 | 1 | 0.6667 |
| doc_type | site_correspondence | 55 | 14 | 10 | 1.0000 | 0.0000 | 0 | 0.1636 |
| hard_negative | no | 239 | 91 | 62 | 0.9839 | 0.0084 | 1 | 0.2678 |
| hard_negative | yes | 81 | 33 | 26 | 0.9615 | 0.0123 | 0 | 0.2963 |
| lang | de * | 4 | 4 | 4 | 0.7500 | 0.0000 | 0 | 0.5000 |
| lang | en | 303 | 107 | 74 | 1.0000 | 0.0033 | 0 | 0.2508 |
| lang | es * | 7 | 7 | 5 | 0.8000 | 0.1429 | 1 | 0.5714 |
| lang | pl * | 6 | 6 | 5 | 1.0000 | 0.1667 | 0 | 1.0000 |
| length_bucket | long | 104 | 24 | 16 | 1.0000 | 0.0000 | 0 | 0.1635 |
| length_bucket | medium | 88 | 41 | 27 | 1.0000 | 0.0114 | 0 | 0.3409 |
| length_bucket | short | 46 | 46 | 34 | 0.9412 | 0.0435 | 1 | 0.6522 |
| length_bucket | xl | 82 | 13 | 11 | 1.0000 | 0.0000 | 0 | 0.1341 |
| perturbation | email_quoting | 55 | 14 | 10 | 1.0000 | 0.0000 | 0 | 0.1636 |
| perturbation | headers_footers | 124 | 52 | 38 | 0.9474 | 0.0081 | 1 | 0.2984 |
| perturbation | line_wrap | 94 | 31 | 28 | 1.0000 | 0.0106 | 0 | 0.3298 |
| perturbation | none | 81 | 30 | 19 | 1.0000 | 0.0123 | 0 | 0.2469 |
| perturbation | ocr_noise | 33 | 14 | 11 | 1.0000 | 0.0000 | 0 | 0.3030 |
| perturbation | table | 45 | 27 | 16 | 1.0000 | 0.0000 | 0 | 0.3556 |
| pii_depth | early | 38 | 7 | 7 | 1.0000 | 0.0000 | 0 | 0.1842 |
| pii_depth | late * | 8 | 2 | 2 | 1.0000 | 0.0000 | 0 | 0.2500 |
| pii_depth | middle * | 9 | 2 | 2 | 1.0000 | 0.0000 | 0 | 0.2222 |
| pii_depth | none | 265 | 113 | 77 | 0.9740 | 0.0113 | 1 | 0.2906 |
| pre_redacted | no | 291 | 109 | 72 | 0.9722 | 0.0069 | 1 | 0.2440 |
| pre_redacted | yes * | 29 | 15 | 16 | 1.0000 | 0.0345 | 0 | 0.5862 |
| split_span | no | 320 | 124 | 88 | 0.9773 | 0.0094 | 1 | 0.2750 |
| truncated | no | 314 | 123 | 85 | 0.9765 | 0.0064 | 1 | 0.2675 |
| truncated | yes * | 6 | 6 | 3 | 1.0000 | 0.1667 | 0 | 0.6667 |

Value kinds of missed spans (false forwards):

| value_kind | false forwards |
|---|---|
| dob | 1 |
| event_date | 1 |
| initials | 1 |
| person_name | 1 |
| phone | 1 |

### B2 / qs_v1, holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 50 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.4000 |
| hard_negative | no | 39 | 23 | 15 | 1.0000 | 0.0000 | 0 | 0.3846 |
| hard_negative | yes * | 11 | 7 | 5 | 1.0000 | 0.0000 | 0 | 0.4545 |
| lang | en | 50 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.4000 |
| length_bucket | medium | 39 | 19 | 15 | 1.0000 | 0.0000 | 0 | 0.3846 |
| length_bucket | short * | 11 | 11 | 5 | 1.0000 | 0.0000 | 0 | 0.4545 |
| perturbation | headers_footers * | 21 | 12 | 7 | 1.0000 | 0.0000 | 0 | 0.3333 |
| perturbation | line_wrap * | 14 | 9 | 7 | 1.0000 | 0.0000 | 0 | 0.5000 |
| perturbation | none * | 17 | 10 | 6 | 1.0000 | 0.0000 | 0 | 0.3529 |
| perturbation | ocr_noise * | 7 | 4 | 3 | 1.0000 | 0.0000 | 0 | 0.4286 |
| pii_depth | none | 50 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.4000 |
| pre_redacted | no | 48 | 29 | 19 | 1.0000 | 0.0000 | 0 | 0.3958 |
| pre_redacted | yes * | 2 | 1 | 1 | 1.0000 | 0.0000 | 0 | 0.5000 |
| split_span | no | 50 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.4000 |
| truncated | no | 50 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.4000 |

Value kinds of missed spans (false forwards):

none

### B2 / qs_v2, test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log * | 17 | 8 | 2 | 1.0000 | 0.0000 | 0 | 0.1176 |
| doc_type | crf_page * | 23 | 14 | 7 | 1.0000 | 0.1304 | 0 | 0.3043 |
| doc_type | csr_patient_narrative | 43 | 14 | 15 | 0.9333 | 0.0465 | 1 | 0.3953 |
| doc_type | delegation_log * | 8 | 5 | 5 | 1.0000 | 0.0000 | 0 | 0.6250 |
| doc_type | deviation_log * | 18 | 10 | 6 | 1.0000 | 0.0000 | 0 | 0.3333 |
| doc_type | icf_signature_page * | 7 | 7 | 6 | 1.0000 | 0.0000 | 0 | 0.8571 |
| doc_type | lab_report * | 15 | 11 | 9 | 1.0000 | 0.0000 | 0 | 0.6000 |
| doc_type | monitoring_visit_report | 49 | 11 | 15 | 1.0000 | 0.0000 | 0 | 0.3061 |
| doc_type | protocol_section | 67 | 16 | 0 | n/a | 0.0000 | 0 | 0.0000 |
| doc_type | sae_cioms * | 18 | 14 | 13 | 0.9231 | 0.0556 | 1 | 0.6667 |
| doc_type | site_correspondence | 55 | 14 | 10 | 1.0000 | 0.0000 | 0 | 0.1636 |
| hard_negative | no | 239 | 91 | 62 | 0.9839 | 0.0167 | 1 | 0.2678 |
| hard_negative | yes | 81 | 33 | 26 | 0.9615 | 0.0247 | 1 | 0.2963 |
| lang | de * | 4 | 4 | 4 | 0.7500 | 0.2500 | 1 | 0.5000 |
| lang | en | 303 | 107 | 74 | 1.0000 | 0.0099 | 0 | 0.2508 |
| lang | es * | 7 | 7 | 5 | 0.8000 | 0.1429 | 1 | 0.5714 |
| lang | pl * | 6 | 6 | 5 | 1.0000 | 0.1667 | 0 | 1.0000 |
| length_bucket | long | 104 | 24 | 16 | 1.0000 | 0.0000 | 0 | 0.1635 |
| length_bucket | medium | 88 | 41 | 27 | 1.0000 | 0.0341 | 0 | 0.3409 |
| length_bucket | short | 46 | 46 | 34 | 0.9412 | 0.0652 | 2 | 0.6522 |
| length_bucket | xl | 82 | 13 | 11 | 1.0000 | 0.0000 | 0 | 0.1341 |
| perturbation | email_quoting | 55 | 14 | 10 | 1.0000 | 0.0000 | 0 | 0.1636 |
| perturbation | headers_footers | 124 | 52 | 38 | 0.9474 | 0.0242 | 2 | 0.2984 |
| perturbation | line_wrap | 94 | 31 | 28 | 1.0000 | 0.0106 | 0 | 0.3298 |
| perturbation | none | 81 | 30 | 19 | 1.0000 | 0.0247 | 0 | 0.2469 |
| perturbation | ocr_noise | 33 | 14 | 11 | 1.0000 | 0.0000 | 0 | 0.3030 |
| perturbation | table | 45 | 27 | 16 | 1.0000 | 0.0000 | 0 | 0.3556 |
| pii_depth | early | 38 | 7 | 7 | 1.0000 | 0.0000 | 0 | 0.1842 |
| pii_depth | late * | 8 | 2 | 2 | 1.0000 | 0.0000 | 0 | 0.2500 |
| pii_depth | middle * | 9 | 2 | 2 | 1.0000 | 0.0000 | 0 | 0.2222 |
| pii_depth | none | 265 | 113 | 77 | 0.9740 | 0.0226 | 2 | 0.2906 |
| pre_redacted | no | 291 | 109 | 72 | 0.9722 | 0.0172 | 2 | 0.2440 |
| pre_redacted | yes * | 29 | 15 | 16 | 1.0000 | 0.0345 | 0 | 0.5862 |
| split_span | no | 320 | 124 | 88 | 0.9773 | 0.0187 | 2 | 0.2750 |
| truncated | no | 314 | 123 | 85 | 0.9765 | 0.0127 | 2 | 0.2675 |
| truncated | yes * | 6 | 6 | 3 | 1.0000 | 0.3333 | 0 | 0.6667 |

Value kinds of missed spans (false forwards):

| value_kind | false forwards |
|---|---|
| address | 1 |
| dob | 2 |
| event_date | 2 |
| initials | 2 |
| mrn | 1 |
| person_name | 2 |
| phone | 1 |
| zip | 1 |

### B2 / qs_v2, holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 50 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.4000 |
| hard_negative | no | 39 | 23 | 15 | 1.0000 | 0.0000 | 0 | 0.3846 |
| hard_negative | yes * | 11 | 7 | 5 | 1.0000 | 0.0000 | 0 | 0.4545 |
| lang | en | 50 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.4000 |
| length_bucket | medium | 39 | 19 | 15 | 1.0000 | 0.0000 | 0 | 0.3846 |
| length_bucket | short * | 11 | 11 | 5 | 1.0000 | 0.0000 | 0 | 0.4545 |
| perturbation | headers_footers * | 21 | 12 | 7 | 1.0000 | 0.0000 | 0 | 0.3333 |
| perturbation | line_wrap * | 14 | 9 | 7 | 1.0000 | 0.0000 | 0 | 0.5000 |
| perturbation | none * | 17 | 10 | 6 | 1.0000 | 0.0000 | 0 | 0.3529 |
| perturbation | ocr_noise * | 7 | 4 | 3 | 1.0000 | 0.0000 | 0 | 0.4286 |
| pii_depth | none | 50 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.4000 |
| pre_redacted | no | 48 | 29 | 19 | 1.0000 | 0.0000 | 0 | 0.3958 |
| pre_redacted | yes * | 2 | 1 | 1 | 1.0000 | 0.0000 | 0 | 0.5000 |
| split_span | no | 50 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.4000 |
| truncated | no | 50 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.4000 |

Value kinds of missed spans (false forwards):

none

### B3 / qs_v1 (doc-level, underpowered), test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log * | 10 | 8 | 2 | 1.0000 | 0.0000 | 0 | 0.2000 |
| doc_type | crf_page * | 16 | 14 | 7 | 0.8571 | 0.0625 | 1 | 0.2500 |
| doc_type | csr_patient_narrative * | 25 | 14 | 13 | 1.0000 | 0.0400 | 0 | 0.5600 |
| doc_type | delegation_log * | 5 | 5 | 5 | 1.0000 | 0.0000 | 0 | 1.0000 |
| doc_type | deviation_log * | 11 | 10 | 6 | 1.0000 | 0.0000 | 0 | 0.4545 |
| doc_type | icf_signature_page * | 7 | 7 | 6 | 1.0000 | 0.0000 | 0 | 0.8571 |
| doc_type | lab_report * | 11 | 11 | 9 | 1.0000 | 0.0000 | 0 | 0.8182 |
| doc_type | monitoring_visit_report * | 25 | 11 | 14 | 1.0000 | 0.0000 | 0 | 0.5600 |
| doc_type | protocol_section | 34 | 16 | 0 | n/a | 0.0000 | 0 | 0.0000 |
| doc_type | sae_cioms * | 14 | 14 | 13 | 0.9231 | 0.0714 | 1 | 0.8571 |
| doc_type | site_correspondence * | 29 | 14 | 10 | 1.0000 | 0.0000 | 0 | 0.3103 |
| hard_negative | no | 139 | 91 | 60 | 0.9833 | 0.0072 | 1 | 0.4173 |
| hard_negative | yes | 48 | 33 | 25 | 0.9600 | 0.0417 | 1 | 0.4583 |
| lang | de * | 4 | 4 | 4 | 1.0000 | 0.0000 | 0 | 0.5000 |
| lang | en | 170 | 107 | 71 | 0.9859 | 0.0059 | 1 | 0.4000 |
| lang | es * | 7 | 7 | 5 | 0.8000 | 0.1429 | 1 | 0.5714 |
| lang | pl * | 6 | 6 | 5 | 1.0000 | 0.1667 | 0 | 1.0000 |
| length_bucket | long | 54 | 24 | 15 | 1.0000 | 0.0000 | 0 | 0.2778 |
| length_bucket | medium | 48 | 41 | 25 | 0.9600 | 0.0208 | 1 | 0.5000 |
| length_bucket | short | 46 | 46 | 34 | 0.9706 | 0.0435 | 1 | 0.6522 |
| length_bucket | xl | 39 | 13 | 11 | 1.0000 | 0.0000 | 0 | 0.2821 |
| perturbation | email_quoting * | 29 | 14 | 10 | 1.0000 | 0.0000 | 0 | 0.3103 |
| perturbation | headers_footers | 75 | 52 | 37 | 0.9459 | 0.0267 | 2 | 0.4533 |
| perturbation | line_wrap | 52 | 31 | 25 | 1.0000 | 0.0192 | 0 | 0.5192 |
| perturbation | none | 47 | 30 | 19 | 1.0000 | 0.0000 | 0 | 0.3830 |
| perturbation | ocr_noise * | 20 | 14 | 11 | 0.9091 | 0.0500 | 1 | 0.5000 |
| perturbation | table * | 29 | 27 | 16 | 1.0000 | 0.0000 | 0 | 0.5172 |
| pii_depth | early * | 19 | 7 | 7 | 1.0000 | 0.0000 | 0 | 0.3684 |
| pii_depth | late * | 5 | 2 | 2 | 1.0000 | 0.0000 | 0 | 0.4000 |
| pii_depth | middle * | 5 | 2 | 2 | 1.0000 | 0.0000 | 0 | 0.4000 |
| pii_depth | none | 158 | 113 | 74 | 0.9730 | 0.0190 | 2 | 0.4367 |
| pre_redacted | no | 169 | 109 | 71 | 0.9718 | 0.0118 | 2 | 0.3846 |
| pre_redacted | yes * | 18 | 15 | 14 | 1.0000 | 0.0556 | 0 | 0.8333 |
| split_span | no | 187 | 124 | 85 | 0.9765 | 0.0160 | 2 | 0.4278 |
| truncated | no | 187 | 124 | 85 | 0.9765 | 0.0160 | 2 | 0.4278 |

Value kinds of missed spans (false forwards):

| value_kind | false forwards |
|---|---|
| dob | 1 |
| event_date | 2 |
| initials | 2 |
| person_name | 1 |
| phone | 1 |

### B3 / qs_v1 (doc-level, underpowered), holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 31 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6452 |
| hard_negative | no * | 24 | 23 | 15 | 1.0000 | 0.0000 | 0 | 0.6250 |
| hard_negative | yes * | 7 | 7 | 5 | 1.0000 | 0.0000 | 0 | 0.7143 |
| lang | en | 31 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6452 |
| length_bucket | medium * | 20 | 19 | 15 | 1.0000 | 0.0000 | 0 | 0.7500 |
| length_bucket | short * | 11 | 11 | 5 | 1.0000 | 0.0000 | 0 | 0.4545 |
| perturbation | headers_footers * | 13 | 12 | 7 | 1.0000 | 0.0000 | 0 | 0.5385 |
| perturbation | line_wrap * | 9 | 9 | 7 | 1.0000 | 0.0000 | 0 | 0.7778 |
| perturbation | none * | 10 | 10 | 6 | 1.0000 | 0.0000 | 0 | 0.6000 |
| perturbation | ocr_noise * | 4 | 4 | 3 | 1.0000 | 0.0000 | 0 | 0.7500 |
| pii_depth | none | 31 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6452 |
| pre_redacted | no | 30 | 29 | 19 | 1.0000 | 0.0000 | 0 | 0.6333 |
| pre_redacted | yes * | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 1.0000 |
| split_span | no | 31 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6452 |
| truncated | no | 31 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6452 |

Value kinds of missed spans (false forwards):

none

### B3 / qs_v2 (doc-level, underpowered), test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log * | 10 | 8 | 2 | 1.0000 | 0.0000 | 0 | 0.2000 |
| doc_type | crf_page * | 16 | 14 | 7 | 0.5714 | 0.2500 | 3 | 0.3125 |
| doc_type | csr_patient_narrative * | 25 | 14 | 13 | 0.9231 | 0.1200 | 1 | 0.5600 |
| doc_type | delegation_log * | 5 | 5 | 5 | 1.0000 | 0.0000 | 0 | 1.0000 |
| doc_type | deviation_log * | 11 | 10 | 6 | 1.0000 | 0.0000 | 0 | 0.5455 |
| doc_type | icf_signature_page * | 7 | 7 | 6 | 1.0000 | 0.0000 | 0 | 0.8571 |
| doc_type | lab_report * | 11 | 11 | 9 | 1.0000 | 0.0000 | 0 | 0.8182 |
| doc_type | monitoring_visit_report * | 25 | 11 | 14 | 1.0000 | 0.0000 | 0 | 0.5600 |
| doc_type | protocol_section | 34 | 16 | 0 | n/a | 0.0294 | 0 | 0.0000 |
| doc_type | sae_cioms * | 14 | 14 | 13 | 0.9231 | 0.0714 | 1 | 0.8571 |
| doc_type | site_correspondence * | 29 | 14 | 10 | 0.9000 | 0.0345 | 1 | 0.3103 |
| hard_negative | no | 139 | 91 | 60 | 0.9500 | 0.0432 | 3 | 0.4245 |
| hard_negative | yes | 48 | 33 | 25 | 0.8800 | 0.0833 | 3 | 0.4792 |
| lang | de * | 4 | 4 | 4 | 0.5000 | 0.5000 | 2 | 0.5000 |
| lang | en | 170 | 107 | 71 | 0.9577 | 0.0353 | 3 | 0.4118 |
| lang | es * | 7 | 7 | 5 | 0.8000 | 0.1429 | 1 | 0.5714 |
| lang | pl * | 6 | 6 | 5 | 1.0000 | 0.1667 | 0 | 1.0000 |
| length_bucket | long | 54 | 24 | 15 | 1.0000 | 0.0185 | 0 | 0.2778 |
| length_bucket | medium | 48 | 41 | 25 | 0.9600 | 0.0625 | 1 | 0.5417 |
| length_bucket | short | 46 | 46 | 34 | 0.8529 | 0.1304 | 5 | 0.6522 |
| length_bucket | xl | 39 | 13 | 11 | 1.0000 | 0.0000 | 0 | 0.2821 |
| perturbation | email_quoting * | 29 | 14 | 10 | 0.9000 | 0.0345 | 1 | 0.3103 |
| perturbation | headers_footers | 75 | 52 | 37 | 0.9189 | 0.0533 | 3 | 0.4667 |
| perturbation | line_wrap | 52 | 31 | 25 | 1.0000 | 0.0385 | 0 | 0.5192 |
| perturbation | none | 47 | 30 | 19 | 0.9474 | 0.0638 | 1 | 0.4043 |
| perturbation | ocr_noise * | 20 | 14 | 11 | 1.0000 | 0.0000 | 0 | 0.5500 |
| perturbation | table * | 29 | 27 | 16 | 0.9375 | 0.0345 | 1 | 0.5172 |
| pii_depth | early * | 19 | 7 | 7 | 1.0000 | 0.0000 | 0 | 0.3684 |
| pii_depth | late * | 5 | 2 | 2 | 1.0000 | 0.0000 | 0 | 0.4000 |
| pii_depth | middle * | 5 | 2 | 2 | 1.0000 | 0.0000 | 0 | 0.4000 |
| pii_depth | none | 158 | 113 | 74 | 0.9189 | 0.0633 | 6 | 0.4494 |
| pre_redacted | no | 169 | 109 | 71 | 0.9155 | 0.0533 | 6 | 0.3964 |
| pre_redacted | yes * | 18 | 15 | 14 | 1.0000 | 0.0556 | 0 | 0.8333 |
| split_span | no | 187 | 124 | 85 | 0.9294 | 0.0535 | 6 | 0.4385 |
| truncated | no | 187 | 124 | 85 | 0.9294 | 0.0535 | 6 | 0.4385 |

Value kinds of missed spans (false forwards):

| value_kind | false forwards |
|---|---|
| address | 1 |
| dob | 2 |
| email | 1 |
| event_date | 6 |
| initials | 5 |
| mrn | 1 |
| person_name | 3 |
| phone | 2 |
| zip | 1 |

### B3 / qs_v2 (doc-level, underpowered), holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 31 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6452 |
| hard_negative | no * | 24 | 23 | 15 | 1.0000 | 0.0000 | 0 | 0.6250 |
| hard_negative | yes * | 7 | 7 | 5 | 1.0000 | 0.0000 | 0 | 0.7143 |
| lang | en | 31 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6452 |
| length_bucket | medium * | 20 | 19 | 15 | 1.0000 | 0.0000 | 0 | 0.7500 |
| length_bucket | short * | 11 | 11 | 5 | 1.0000 | 0.0000 | 0 | 0.4545 |
| perturbation | headers_footers * | 13 | 12 | 7 | 1.0000 | 0.0000 | 0 | 0.5385 |
| perturbation | line_wrap * | 9 | 9 | 7 | 1.0000 | 0.0000 | 0 | 0.7778 |
| perturbation | none * | 10 | 10 | 6 | 1.0000 | 0.0000 | 0 | 0.6000 |
| perturbation | ocr_noise * | 4 | 4 | 3 | 1.0000 | 0.0000 | 0 | 0.7500 |
| pii_depth | none | 31 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6452 |
| pre_redacted | no | 30 | 29 | 19 | 1.0000 | 0.0000 | 0 | 0.6333 |
| pre_redacted | yes * | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 1.0000 |
| split_span | no | 31 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6452 |
| truncated | no | 31 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6452 |

Value kinds of missed spans (false forwards):

none

### B4 / qs_v1 (doc-level, underpowered), test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log * | 8 | 8 | 2 | 1.0000 | 0.0000 | 0 | 0.2500 |
| doc_type | crf_page * | 14 | 14 | 7 | 0.8571 | 0.0714 | 1 | 0.2143 |
| doc_type | csr_patient_narrative * | 14 | 14 | 12 | 0.9167 | 0.0714 | 0 | 0.8571 |
| doc_type | delegation_log * | 5 | 5 | 5 | 1.0000 | 0.0000 | 0 | 1.0000 |
| doc_type | deviation_log * | 10 | 10 | 6 | 1.0000 | 0.0000 | 0 | 0.5000 |
| doc_type | icf_signature_page * | 7 | 7 | 6 | 1.0000 | 0.0000 | 0 | 0.8571 |
| doc_type | lab_report * | 11 | 11 | 9 | 1.0000 | 0.0000 | 0 | 0.8182 |
| doc_type | monitoring_visit_report * | 11 | 11 | 10 | 1.0000 | 0.0000 | 0 | 0.9091 |
| doc_type | protocol_section * | 16 | 16 | 0 | n/a | 0.0000 | 0 | 0.0000 |
| doc_type | sae_cioms * | 14 | 14 | 13 | 0.9231 | 0.0714 | 1 | 0.8571 |
| doc_type | site_correspondence * | 14 | 14 | 10 | 1.0000 | 0.0000 | 0 | 0.6429 |
| hard_negative | no | 91 | 91 | 57 | 0.9825 | 0.0110 | 1 | 0.5824 |
| hard_negative | yes | 33 | 33 | 23 | 0.9130 | 0.0606 | 1 | 0.6061 |
| lang | de * | 4 | 4 | 4 | 0.7500 | 0.0000 | 0 | 0.5000 |
| lang | en | 107 | 107 | 66 | 0.9848 | 0.0093 | 1 | 0.5701 |
| lang | es * | 7 | 7 | 5 | 0.8000 | 0.1429 | 1 | 0.5714 |
| lang | pl * | 6 | 6 | 5 | 1.0000 | 0.1667 | 0 | 1.0000 |
| length_bucket | long * | 24 | 24 | 12 | 1.0000 | 0.0000 | 0 | 0.5000 |
| length_bucket | medium | 41 | 41 | 25 | 0.9600 | 0.0244 | 1 | 0.5366 |
| length_bucket | short | 46 | 46 | 34 | 0.9412 | 0.0435 | 1 | 0.6522 |
| length_bucket | xl * | 13 | 13 | 9 | 1.0000 | 0.0000 | 0 | 0.6923 |
| perturbation | email_quoting * | 14 | 14 | 10 | 1.0000 | 0.0000 | 0 | 0.6429 |
| perturbation | headers_footers | 52 | 52 | 34 | 0.9118 | 0.0385 | 2 | 0.5769 |
| perturbation | line_wrap | 31 | 31 | 22 | 1.0000 | 0.0323 | 0 | 0.7419 |
| perturbation | none | 30 | 30 | 18 | 1.0000 | 0.0000 | 0 | 0.5333 |
| perturbation | ocr_noise * | 14 | 14 | 10 | 0.9000 | 0.0714 | 1 | 0.6429 |
| perturbation | table * | 27 | 27 | 16 | 1.0000 | 0.0000 | 0 | 0.5556 |
| pii_depth | early * | 7 | 7 | 7 | 1.0000 | 0.0000 | 0 | 1.0000 |
| pii_depth | late * | 2 | 2 | 2 | 1.0000 | 0.0000 | 0 | 1.0000 |
| pii_depth | middle * | 2 | 2 | 2 | 1.0000 | 0.0000 | 0 | 1.0000 |
| pii_depth | none | 113 | 113 | 69 | 0.9565 | 0.0265 | 2 | 0.5487 |
| pre_redacted | no | 109 | 109 | 67 | 0.9552 | 0.0183 | 2 | 0.5413 |
| pre_redacted | yes * | 15 | 15 | 13 | 1.0000 | 0.0667 | 0 | 0.9333 |
| split_span | no | 124 | 124 | 80 | 0.9625 | 0.0242 | 2 | 0.5887 |
| truncated | no | 111 | 111 | 71 | 0.9577 | 0.0270 | 2 | 0.5766 |
| truncated | yes * | 13 | 13 | 9 | 1.0000 | 0.0000 | 0 | 0.6923 |

Value kinds of missed spans (false forwards):

| value_kind | false forwards |
|---|---|
| dob | 1 |
| event_date | 2 |
| initials | 2 |
| person_name | 1 |
| phone | 1 |

### B4 / qs_v1 (doc-level, underpowered), holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 30 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6667 |
| hard_negative | no * | 23 | 23 | 15 | 1.0000 | 0.0000 | 0 | 0.6522 |
| hard_negative | yes * | 7 | 7 | 5 | 1.0000 | 0.0000 | 0 | 0.7143 |
| lang | en | 30 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6667 |
| length_bucket | medium * | 19 | 19 | 15 | 1.0000 | 0.0000 | 0 | 0.7895 |
| length_bucket | short * | 11 | 11 | 5 | 1.0000 | 0.0000 | 0 | 0.4545 |
| perturbation | headers_footers * | 12 | 12 | 7 | 1.0000 | 0.0000 | 0 | 0.5833 |
| perturbation | line_wrap * | 9 | 9 | 7 | 1.0000 | 0.0000 | 0 | 0.7778 |
| perturbation | none * | 10 | 10 | 6 | 1.0000 | 0.0000 | 0 | 0.6000 |
| perturbation | ocr_noise * | 4 | 4 | 3 | 1.0000 | 0.0000 | 0 | 0.7500 |
| pii_depth | none | 30 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6667 |
| pre_redacted | no * | 29 | 29 | 19 | 1.0000 | 0.0000 | 0 | 0.6552 |
| pre_redacted | yes * | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 1.0000 |
| split_span | no | 30 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6667 |
| truncated | no | 30 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6667 |

Value kinds of missed spans (false forwards):

none

### B4 / qs_v2 (doc-level, underpowered), test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log * | 8 | 8 | 2 | 1.0000 | 0.0000 | 0 | 0.2500 |
| doc_type | crf_page * | 14 | 14 | 7 | 0.5714 | 0.2143 | 3 | 0.2143 |
| doc_type | csr_patient_narrative * | 14 | 14 | 12 | 0.9167 | 0.1429 | 1 | 0.8571 |
| doc_type | delegation_log * | 5 | 5 | 5 | 1.0000 | 0.0000 | 0 | 1.0000 |
| doc_type | deviation_log * | 10 | 10 | 6 | 1.0000 | 0.0000 | 0 | 0.6000 |
| doc_type | icf_signature_page * | 7 | 7 | 6 | 1.0000 | 0.0000 | 0 | 0.8571 |
| doc_type | lab_report * | 11 | 11 | 9 | 1.0000 | 0.0000 | 0 | 0.8182 |
| doc_type | monitoring_visit_report * | 11 | 11 | 10 | 1.0000 | 0.0000 | 0 | 0.9091 |
| doc_type | protocol_section * | 16 | 16 | 0 | n/a | 0.0000 | 0 | 0.0000 |
| doc_type | sae_cioms * | 14 | 14 | 13 | 0.9231 | 0.0714 | 1 | 0.8571 |
| doc_type | site_correspondence * | 14 | 14 | 10 | 0.9000 | 0.0714 | 1 | 0.6429 |
| hard_negative | no | 91 | 91 | 57 | 0.9649 | 0.0220 | 2 | 0.5934 |
| hard_negative | yes | 33 | 33 | 23 | 0.8261 | 0.1515 | 4 | 0.6061 |
| lang | de * | 4 | 4 | 4 | 0.5000 | 0.5000 | 2 | 0.5000 |
| lang | en | 107 | 107 | 66 | 0.9545 | 0.0280 | 3 | 0.5794 |
| lang | es * | 7 | 7 | 5 | 0.8000 | 0.1429 | 1 | 0.5714 |
| lang | pl * | 6 | 6 | 5 | 1.0000 | 0.1667 | 0 | 1.0000 |
| length_bucket | long * | 24 | 24 | 12 | 1.0000 | 0.0000 | 0 | 0.5000 |
| length_bucket | medium | 41 | 41 | 25 | 0.9200 | 0.0488 | 2 | 0.5610 |
| length_bucket | short | 46 | 46 | 34 | 0.8824 | 0.1087 | 4 | 0.6522 |
| length_bucket | xl * | 13 | 13 | 9 | 1.0000 | 0.0000 | 0 | 0.6923 |
| perturbation | email_quoting * | 14 | 14 | 10 | 0.9000 | 0.0714 | 1 | 0.6429 |
| perturbation | headers_footers | 52 | 52 | 34 | 0.9118 | 0.0577 | 3 | 0.5769 |
| perturbation | line_wrap | 31 | 31 | 22 | 1.0000 | 0.0323 | 0 | 0.7419 |
| perturbation | none | 30 | 30 | 18 | 0.9444 | 0.0333 | 1 | 0.5667 |
| perturbation | ocr_noise * | 14 | 14 | 10 | 0.9000 | 0.0714 | 1 | 0.6429 |
| perturbation | table * | 27 | 27 | 16 | 0.9375 | 0.0370 | 1 | 0.5556 |
| pii_depth | early * | 7 | 7 | 7 | 1.0000 | 0.0000 | 0 | 1.0000 |
| pii_depth | late * | 2 | 2 | 2 | 1.0000 | 0.0000 | 0 | 1.0000 |
| pii_depth | middle * | 2 | 2 | 2 | 1.0000 | 0.0000 | 0 | 1.0000 |
| pii_depth | none | 113 | 113 | 69 | 0.9130 | 0.0619 | 6 | 0.5575 |
| pre_redacted | no | 109 | 109 | 67 | 0.9104 | 0.0550 | 6 | 0.5505 |
| pre_redacted | yes * | 15 | 15 | 13 | 1.0000 | 0.0667 | 0 | 0.9333 |
| split_span | no | 124 | 124 | 80 | 0.9250 | 0.0565 | 6 | 0.5968 |
| truncated | no | 111 | 111 | 71 | 0.9155 | 0.0631 | 6 | 0.5856 |
| truncated | yes * | 13 | 13 | 9 | 1.0000 | 0.0000 | 0 | 0.6923 |

Value kinds of missed spans (false forwards):

| value_kind | false forwards |
|---|---|
| address | 1 |
| dob | 2 |
| email | 1 |
| event_date | 6 |
| initials | 5 |
| mrn | 1 |
| person_name | 3 |
| phone | 2 |
| zip | 1 |

### B4 / qs_v2 (doc-level, underpowered), holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 30 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6667 |
| hard_negative | no * | 23 | 23 | 15 | 1.0000 | 0.0000 | 0 | 0.6522 |
| hard_negative | yes * | 7 | 7 | 5 | 1.0000 | 0.0000 | 0 | 0.7143 |
| lang | en | 30 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6667 |
| length_bucket | medium * | 19 | 19 | 15 | 1.0000 | 0.0000 | 0 | 0.7895 |
| length_bucket | short * | 11 | 11 | 5 | 1.0000 | 0.0000 | 0 | 0.4545 |
| perturbation | headers_footers * | 12 | 12 | 7 | 1.0000 | 0.0000 | 0 | 0.5833 |
| perturbation | line_wrap * | 9 | 9 | 7 | 1.0000 | 0.0000 | 0 | 0.7778 |
| perturbation | none * | 10 | 10 | 6 | 1.0000 | 0.0000 | 0 | 0.6000 |
| perturbation | ocr_noise * | 4 | 4 | 3 | 1.0000 | 0.0000 | 0 | 0.7500 |
| pii_depth | none | 30 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6667 |
| pre_redacted | no * | 29 | 29 | 19 | 1.0000 | 0.0000 | 0 | 0.6552 |
| pre_redacted | yes * | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 1.0000 |
| split_span | no | 30 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6667 |
| truncated | no | 30 | 30 | 20 | 1.0000 | 0.0000 | 0 | 0.6667 |

Value kinds of missed spans (false forwards):

none

## 8. Failure gallery

### A / qs_v1, test: 0 false forward(s)

### A / qs_v1, holdout: 0 false forward(s)

### A / qs_v2, test: 0 false forward(s)

### A / qs_v2, holdout: 0 false forward(s)

### B1 / qs_v1, test: 1 false forward(s)

**d0310:chunk:1024:15** route forward (p_below_t_low); p(pii) raw 0.0226, calibrated 0.0226; gold role staff, category staff; missed email, person_name

>  study. Edit checks identify missing, inconsistent or out-of-range values
> during cleaning. Edit checks flag missing, inconsistent or out-of-range values
> at entry. Edit checks identify missing, inconsistent or out-of-range values at
> entry.
> 
> Access to the database is restricted to authorised personnel with role-based
> permissions. Access to the database is restricted to authorised personnel
> according to the access matrix. Data are entered into a validated clinical
> database with an audit trail.
> 
> Edit checks flag missing, inconsistent or out-of-range values at entry. Edit
> checks identify missing, inconsistent or out-of-range values during cleaning.
> Medical history and adverse events are coded with a standard dictionary during
> the study. Data are entered into a validated clinical database with an audit
> trail. Edit checks flag missing, inconsistent or out-of-range values during
> cleaning.
> 
> 3. Action Items
> The site will resolve open queries before the next visit and send confirmation
> to **Ms. Pitts** at **m.pitts@halcyon-cro.example.com**.
> 
> Page 12
> 

### B1 / qs_v1, holdout: 0 false forward(s)

### B1 / qs_v2, test: 0 false forward(s)

### B1 / qs_v2, holdout: 0 false forward(s)

### B2 / qs_v1, test: 1 false forward(s)

**d0352:section:2048:0** route forward (p_below_t_low); p(pii) raw 0.0499, calibrated 0.0499; gold role both, category direct; missed dob, event_date, initials, person_name, phone

> Fenwick Therapeutics \| Protocolo FTX-5142-018 \| Confidencial
> 
> CIOMS I: notificación de sospecha de reacción adversa
> N.º de control: FEN-2025342    Protocolo: FTX-5142-018    Centro: 3003
> 
> I. Información de la reacción
> 1. Iniciales: **PA**    1a. Sujeto: \#30030005
> 2. Fecha de nacimiento: **7 de agosto de 1961**    2a. Edad: 63 años    3. Sexo: F
> 4-6. Inicio de la reacción: **18/04/2025**
> 7+13. Descripción: fatiga, grado 2; requirió hospitalización.
> 
> V. Notificador
> 24b. **A. Marcos**, Centro de Investigación Clínica Llanodorado, tel. **+34 555 019 6055**
> 25a. Fecha de este informe: 01/05/2025
> 
> Página 1
> 

### B2 / qs_v1, holdout: 0 false forward(s)

### B2 / qs_v2, test: 2 false forward(s)

**d0352:section:2048:0** route forward (p_below_t_low); p(pii) raw 0.0471, calibrated 0.0471; gold role both, category direct; missed dob, event_date, initials, person_name, phone

> Fenwick Therapeutics \| Protocolo FTX-5142-018 \| Confidencial
> 
> CIOMS I: notificación de sospecha de reacción adversa
> N.º de control: FEN-2025342    Protocolo: FTX-5142-018    Centro: 3003
> 
> I. Información de la reacción
> 1. Iniciales: **PA**    1a. Sujeto: \#30030005
> 2. Fecha de nacimiento: **7 de agosto de 1961**    2a. Edad: 63 años    3. Sexo: F
> 4-6. Inicio de la reacción: **18/04/2025**
> 7+13. Descripción: fatiga, grado 2; requirió hospitalización.
> 
> V. Notificador
> 24b. **A. Marcos**, Centro de Investigación Clínica Llanodorado, tel. **+34 555 019 6055**
> 25a. Fecha de este informe: 01/05/2025
> 
> Página 1
> 

**d0447:section:2048:0** route forward (p_below_t_low); p(pii) raw 0.2966, calibrated 0.2966; gold role both, category direct; missed address, dob, event_date, initials, mrn, person_name, zip

> Fenwick Therapeutics \| Prüfplan FTX-5142-018 \| Vertraulich
> 
> Patientennarrativ: Prüfungsteilnehmer Subj 3005-0010
> Prüfplan FTX-5142-018, Prüfzentrum 3005
> 
> Demografie und Ausgangsbefund
> **P. Rohleder** (**P-R**), 75 Jahre, geb. **18. Juli 1949**, Patientennummer **70322471**, wurde am **15. April 2025** randomisiert (Randomisierungsnummer R-65247) und erhielt am selben Tag die erste Dosis FTX-5142. Wohnort: **Baumring 1-8, Niederheide** **30576**.
> Die Begleitmedikation wurde von **SCHMIDTKE, Dieter** überprüft.
> 
> Unerwünschtes Ereignis
> Während der Behandlungsphase wurden keine unerwünschten Ereignisse gemeldet.
> 
> Ereigniszeitanalysen verwenden die Kaplan-Meier-Methode; die Kreatinin-Clearance wird nach Cockcroft-Gault berechnet. Prüfpräparat FTX-5142, Charge LT-255487-A, wurde aus Kit K-954687 im Visitenfenster Day 29 ±3 ausgegeben. Prüfplan FTX-5142-018 (NCT99608180; EudraCT 2031-854061-77), Amendment A5, gültig ab 2025-04-03.
> 
> Verlauf
> Die Teilnahme wurde gemäß Prüfplan fortgesetzt.
> 
> Seite 1
> 

### B2 / qs_v2, holdout: 0 false forward(s)

### B3 / qs_v1 (doc-level, underpowered), test: 2 false forward(s)

**d0352:section:4096:0** route forward (p_below_t_low); p(pii) raw 0.0499, calibrated 0.0499; gold role both, category direct; missed dob, event_date, initials, person_name, phone

> Fenwick Therapeutics \| Protocolo FTX-5142-018 \| Confidencial
> 
> CIOMS I: notificación de sospecha de reacción adversa
> N.º de control: FEN-2025342    Protocolo: FTX-5142-018    Centro: 3003
> 
> I. Información de la reacción
> 1. Iniciales: **PA**    1a. Sujeto: \#30030005
> 2. Fecha de nacimiento: **7 de agosto de 1961**    2a. Edad: 63 años    3. Sexo: F
> 4-6. Inicio de la reacción: **18/04/2025**
> 7+13. Descripción: fatiga, grado 2; requirió hospitalización.
> 
> V. Notificador
> 24b. **A. Marcos**, Centro de Investigación Clínica Llanodorado, tel. **+34 555 019 6055**
> 25a. Fecha de este informe: 01/05/2025
> 
> Página 1
> 

**d0418:section:4096:0** route forward (p_below_t_low); p(pii) raw 0.1351, calibrated 0.1351; gold role both, category quasi; missed event_date, initials

> Fenwick Therapeutics \| Protocol FTX-5142-018 \| Confidential
> 
> CRF Page 14: Vital Signs
> Protocol FTX-5142-018    Site 3005
> 
> Subject \| Initials \| Visit \| Visit date \| SBP \| DBP \| HR \| Temp
> 3005-0001 \| **J-B** \| Visit 2 \| **June 18, 2025** \| 149 \| 75 \| 81 \| 36.6
> 3005-0001 \| **J-B** \| Visit 3 \| **29JUN2025** \| 120 \| 64 \| 69 \| 37.5
> \#30050001 \| **J.B.** \| Visit 4 \| **30-Jul-2025** \| 107 \| 94 \| 92 \| 37.4
> \#300S0001 \| **J-B** \| Visit 5 \| **08/27/2025** \| 132 \| 81 \| 58 \| 36.4
> 3005-0002 \| **S.H.** \| Visit 2 \| **06-May-2025** \| 113 \| 77 \| 59 \| 37.5
> Subj 3005-0002 \| **S-H** \| Visit 3 \| **2025-05-20** \| 111 \| 67 \| 98 \| 37.2
> Subj 3005-0002 \| **S-H** \| Visit 4 \| **06/18/2025** \| 118 \| 79 \| 81 \| 37.2
> 3005-0002 \| **S-H** \| Visit 5 \| **13JUL2025** \| 109 \| 78 \| 61 \| 37.6
> 3005-0003 \| **S.S.** \| Visit 2 \| **23-Sep-2025** \| 127 \| 96 \| 62 \| 36.9
> Subj 3005-0003 \| **S.S.** \| Visit 3 \| **10/06/2025** \| 162 \| 91 \| 63 \| 37.7
> \#30050003 \| **SS** \| Visit 4 \| **November 6, 2025** \| 164 \| 62 \| 58 \| 37.5
> \#30050003 \| **SXS** \| Visit S \| **04DECZ025** \| 111 \| 85 \| 65 \| 37.2
> Subj 3005-0004 \| **E-W** \| Visit Z \| **2025-08-18** \| 126 \| 81 \| 64 \| 37.0
> \#30050004 \| **E.W.** \| Visit 3 \| **August 28, 2025** \| 135 \| 72 \| 60 \| 37.5
> Subj 3005-0004 \| **EXW** \| Visit 4 \| **09/28/2025** \| 143 \| 98 \| 89 \| 37.2
> 3005-0004 \| **E-W** \| Viit 5 \| **25OCT2O25** \| 124 \| 72 \| 80 \| 37.7
> Subj 3005-0005 \| **LXK** \| Visit 2 \| **June 10, 2025** \| 112 \| 83 \| 88 \| 36.8
> Subj 3005-0005 \| **LXK** \| Visit 3 \| **June 25, 20Z5** \| 152 \| 97 \| 67 \| 37.1
> Subj 3005-0005 \| **L-K** \| Visit 4 \| **25-Jul-2025** \| 155 \| 62 \| 93 \| 37.1
> 3005-0005 \| **L-K** \| Visit 5 \| **08/22/2025** \| 146 \| 70 \| 72 \| 37.2
> Subj 3005-0006 \| **G.P.** \| Visit 2 \| **24-Jul-2025** \| 134 \| 77 \| 86 \| 37.0
> Subj 3005-0006 \| **GXP** \| Visit 3 \| **August 11, 2025** \| 158 \| 65 \| 58 \| 37.7
> \#30050006 \| **GXP** \| Visit 4 \| **09/06/2025** \| 106 \| 76 \| 77 \| 36.9
> 3005-0006 \| **G-P** \| Visit 5 \| **04OCT2025** \| 158 \| 85 \| 78 \| 36.7
> 3005-0007 \| **E-M** \| Visit 2 \| **2025-05-19** \| 118 \| 74 \| 82 \| 37.7
> 3005-0007 \| **EXM** \| Visit 3 \| **June 2, 2025** \| 111 \| 74 \| 82 \| 37.7
> \#30050007 \| **EM** \| Visit 4 \| **30JUN20Z5** \| 143 \| 67 \| 92 \| 37.3
> \#30050007 \| **E-M** \| Visit 5 \| **27JUL2025** \| 110 \| 80 \| 94 \| 36.3
> Subj 3005-0008 \| **S-K** \| Visit 3 \| **2025-08-03** \| 134 \| 86 \| 78 \| 36.5
> 3005-0008 \| **SXK** \| Visit 4 \| **2025-09-01** \| 121 \| 71 \| 67 \| 37.0
> \#30050008 \| **SXK** \| Visit 5 \| **01-Oct-2025** \| 161 \| 68 \| 83 \| 36.7
> Subj 3005-0009 \| **D.E.** \| Visit 2 \| **May 2, 2025** \| 125 \| 81 \| 90 \| 36.3
> 3005-0009 \| **DE** \| Visit 4 \| **06/14/2025** \| 153 \| 62 \| 86 \| 37.6
> \#30050010 \| **PR** \| Visit 2 \| **27APR2025** \| 153 \| 92 \| 88 \| 37.7
> Subj 3005-0010 \| **P.R.** \| Visit 3 \| **13-May-2025** \| 112 \| 76 \| 98 \| 36.7
> \#30050010 \| **P-R** \| Visit 4 \| **11JUN2025** \| 106 \| 79 \| 95 \| 37.4
> \#30050011 \| **D.R.** \| Visit 2 \| **22MAR2025** \| 120 \| 69 \| 68 \| 36.4
> Subj 3005-0011 \| **DR** \| Visit 3 \| **03-Apr-2025** \| 136 \| 94 \| 74 \| 36.7
> Subj 3005-0011 \| **D.R.** \| Visit 4 \| **2025-04-30** \| 162 \| 66 \| 81 \| 36.7
> \#30050011 \| **D-R** \| Visit 5 \| **31MAY2025** \| 149 \| 83 \| 58 \| 37.5
> 300S-0012 \| **JXG** \| Visit 2 \| **02/24/2025** \| 136 \| 71 \| 65 \| 36.2
> Subj 3005-0012 \| **JG** \| Visit 3 \| **March 6, 2025** \| 156 \| 63 \| 62 \| 36.2
> \#30050012 \| **J-G** \| Visit 4 \| **05-Apr-2025** \| 161 \| 86 \| 86 \| 36.8
> \#3005001Z \| **JXG** \| Visit 5 \| **01-May-2025** \| 116 \| 98 \| 93 \| 37.0
> Subj 3005-0013 \| **S-E** \| Viit 2 \| **July 23, 2025** \| 147 \| 87 \| 63 \| 37.8
> Subj 3005-0013 \| **S-E** \| Visit 3 \| **04AUG2025** \| 139 \| 78 \| 66 \| 37.2
> 3005-0013 \| **S.E.** \| Visit 5 \| **09/30/2025** \| 123 \| 82 \| 84 \| 36.9
> \#30050014 \| **SXG** \| Visit 2 \| **February 9, 2025** \| 144 \| 68 \| 89 \| 37.0
> \#30050014 \| **S.G.** \| Visit 3 \| **21-Feb-2025** \| 147 \| 69 \| 81 \| 36.4
> 3005-0014 \| **SG** \| Visit 4 \| **22MAR2025** \| 125 \| 93 \| 69 \| 36.1
> \#30050014 \| **SG** \| Visit 5 \| **18APR2025** \| 138 \| 77 \| 59 \| 37.6
> Subj 3005-0015 \| **D.M.** \| Visit 2 \| **09-May-2025** \| 151 \| 96 \| 69 \| 37.3
> \#30050015 \| **DXM** \| Visit 3 \| **May 25, 2O25** \| 132 \| 84 \| 78 \| 37.3
> 3005-0O15 \| **D.M.** \| Visit 4 \| **June 20, 2025** \| 107 \| 62 \| 55 \| 37.1
> 
> Measurements taken seated after 5 minutes of rest. Repeat any systolic value above 16O mmHg within 15 minutes.
> Entered by: **AXW**
> Source verified against medical record (source on file) for subject 3005-0001.
> 
> Events are coded to MedDRA preferred term 10586823; the target dose is 150 mg. Agreement between central and local readigs is shown in Bland-Altman plots. Secondary endpoints are compard with the Wilcoxon test with Bonferroni correction; sparse tables use Fisher's exact test.
> 
> Database Procedures
> Access to the database is restricted to authorised personnel with role-based permissions. Edit checks identify missing, inconsistent or out-of-range values during cleaning. Reconciliation of safety data with the clinical database is performed periodically. Edit checks identify missing, inconsistent or out-of-range values during cleaning. Access to the database is restricted to authorised personnel with role-based permissions.
> 
> Data are entered into a validated c1inical database with an audit trail. Edit checks identify missing, inconsistent or out-of-range vlues at entry. Medical history and adverse evets are coded with a standard dictionary before database lock. Medical history and adverse events are coded with standard terminology before database lock.
> 
> Source Data Verification
> Queries are raised in the data capture system and resolved by site staff within ten working days. Protocol deviations are classified as minor or major. The investigator site file is reviewed for completeness at each visit. Source data verification prioritises eligibility, informed consent, primary endpoints and serious aderse events. Queries are raised in the data capture system and answered by the site within ten working days.
> 
> Protocol deviations are assessed for impact on participant safety and data integrity. The investigator site file is reviewed for currency of essential documents at each visit. Protocol deviations are classified as minor or majr.
> 
> On-site and remote monitoring visits are scheduled based on enrollment and risk indicators. The investigator site file is reviewed for completeness at each visit. Findings are documented in the visit report and followed up until closure.
> 
> Analysis Methods
> Sensitivity analyses assess the robustness of the primary result to protocol deviations. All tests are two-sided with a significance level of 5 percent unless otherwise specified. Subgroup analyses by geograhic region are exploratory and not adjusted for multiplicity.
> 
> Subgroup analyses by age group are descriptive and not adjusted for multiplicity. All tests are two-sided with a significance level of 5 pecnt unless otherwise spcified. Continuous variables are summaised with the nmber of observations, mean, standard deviation, median and range. Sensitivity analyses assess the robstness of the primary result to alternative assumptions. The statistical analyss plan is finalised befre database lock and specifies all derived variab1es.
> 
> Categorical vriables are presented as counts and percentages within each treatment group. Subgroup analyses by baseline severity are descriptive and not adjusted for multiplicity. Categorical variables are presented as counts and percentages of the analysis set.
> 
> Page 1
> 
> Fenwick Therapeutics \| Protocol FTX-5142-018 \| Confidential
> 
> Categorical variables are presented as counts and percentages of the analysis set. All tests are two-sided with a significance level of 2.5 percent unless otherwise specified. Sensitivity aalses asess the robustness of the primary resu1t to alternative assumptions. Continuous variables are summarised wih the number of observations, mean, standard deviation, median and range. All tests are two-sided with a significance level of 5 percent unless otherwise specified. Categorical variables are presented as counts and percentages of the analysis set.
> 
> Drug Accountabiliy
> Investigational product is stored in a secure, temperature-monitored area with access limited to authorised staff. Dispensing and returns are recorded on the accountability log at every dispensing visit. Temperature excursions must be reported to the sponsor before further use of the affected supply. Unused product is returned to the sponsor after reconciliation. Dispensing and returns are recorded on the accountability log at every dispensing visit. Unused product is destroyed according to local procedures after reconciliation.
> 
> Investigtional product is stored in a secure, temperature-monitored area with access limited to authorised staff. Temperature excursions must be reported to the sponsor immediately. Temperature excursions are reported to the sponsor immediately. Temperature excursions must be reported to the sponsor before further use of the affected suply.
> 
> Tablet counts are reconciled against the dosing dary to assess compliance. Tablet counts are reconciled against the dosing diary to assss compliance. Dispensing and returns are recorded on the accountability log at every dispensing visit. Temperature excursons are reported to the sponsor immediately. Investigational product is stored in a secure, temerature-monitored area with access limited to authorised staff.
> 
> 

### B3 / qs_v1 (doc-level, underpowered), holdout: 0 false forward(s)

### B3 / qs_v2 (doc-level, underpowered), test: 6 false forward(s)

**d0062:section:4096:0** route forward (p_below_t_low); p(pii) raw 0.4012, calibrated 0.4012; gold role patient, category quasi; missed event_date, initials

> CRF Page 15: Vital Signs
> Protocol FTX-9990-002    Site 2003
> 
> Subject \| Initials \| Visit \| Visit date \| SBP \| DBP \| HR \| Temp
> Subj 2003-0001 \| **TW** \| Visit 5 \| **2025-05-12** \| 141 \| 85 \| 84 \| 37.0
> \#20030004 \| **K.C.** \| Visit 5 \| **15SEP2025** \| 135 \| 89 \| 95 \| 36.1
> Subj 2003-0006 \| **AXC** \| Visit 2 \| **2025-08-07** \| 111 \| 70 \| 61 \| 37.2
> Subj 2003-0008 \| **LXH** \| Visit 2 \| **2025-03-20** \| 159 \| 63 \| 94 \| 36.2
> Subj 2003-0010 \| **SO** \| Visit 4 \| **03JUL2025** \| 143 \| 69 \| 76 \| 37.7
> 2003-0014 \| **EH** \| Visit 5 \| **06/14/2025** \| 119 \| 89 \| 77 \| 36.6
> 
> Measurements taken seated after 5 minutes of rest. Repeat any systolic value above 160 mmHg within 15 minutes.
> Entered by: site staff
> Source verified against medical record (source on file) for subject Subj 2003-0001.
> 
> Laboratory Assessments
> Blood samples are collected after an overnight fast and processed within two hours. Samples are shipped at ambient temperature to the central laboratory with the requisition form. Clinically significant laboratory abnormalities are recorded as adverse events. Reference ranges are provided by the laboratory and updated when changed.
> 
> Blood samples are collected after an overnight fast and processed according to the laboratory manual. Clinically significant laboratory abnormalities are recorded as adverse events. Blood samples are collected after an overnight fast and processed within two hours. Clinically significant laboratory abnormalities should be recorded as adverse events.
> 
> Blood samples are collected after an overnight fast and processed within two hours. Blood samples are collected in the morning and processed within two hours. Blood samples are collected after an overnight fast and processed within two hours. Reference ranges are provided by the laboratory and updated when changed. Samples are shipped frozen on dry ice to the central laboratory with the requisition form. Reference ranges are provided by the laboratory and filed in the investigator site file.
> 
> Good Clinical Practice
> The study will be conducted in accordance with the principles of good clinical practice and applicable regulatory requirements. The sponsor may conduct audits of study sites and vendors to verify compliance. Confidentiality of participant information is protected at all times.
> 
> Confidentiality of participant information is protected at all times. Essential documents are retained for at least 25 years after the end of the study or longer if required by local regulations. The sponsor reserves the right to conduct audits of study sites and vendors to verify compliance. The informed consent form and any amendments must be approved by the ethics committee before implementation.
> 
> Participants may withdraw consent at any time without consequences for their medical care. Participants may withdraw consent at any time without consequences for their medical care. Essential documents are retained for at least 25 years after the end of the study or longer if required by local regulations. Participants may withdraw consent at any time without consequences for their medical care. The protocol and any amendments are approved by the ethics committee before implementation.
> 
> Essential documents are retained for at least 15 years after the end of the study or longer if required by local regulations. The sponsor reserves the right to conduct audits of study sites and vendors to verify compliance. The protocol and any amendments must be approved by the ethics committee before implementation. Confidentiality of participant information is protected in line with applicable data protection law. Essential documents are retained for at least 15 years after the end of the study as required.
> 

**d0082:section:4096:0** route forward (p_below_t_low); p(pii) raw 0.4550, calibrated 0.4550; gold role patient, category quasi; missed event_date, initials

> Fenwick Therapeutics \| Protocol FTX-5142-018 \| Confidential
> 
> CRF Page 14: Vital Signs
> Protocol FTX-5142-018    Site 3003
> 
> Subject \| Initials \| Visit \| Visit date \| SBP \| DBP \| HR \| Temp
> \#30030002 \| **S-I** \| Visit 3 \| **08/23/2025** \| 130 \| 79 \| 84 \| 36.1
> \#30030007 \| **YXC** \| Visit 4 \| **09/18/2025** \| 154 \| 91 \| 96 \| 36.2
> \#30030013 \| **PR** \| Visit 4 \| **July 20, 2025** \| 153 \| 78 \| 59 \| 37.6
> 3003-0014 \| **A-B** \| Visit 4 \| **03-Aug-2025** \| 107 \| 97 \| 55 \| 37.6
> Subj 3003-0015 \| **C-L** \| Visit 2 \| **04/17/2025** \| 152 \| 77 \| 58 \| 36.3
> 
> Measurements taken seated after 5 minutes of rest. Repeat any systolic value above 160 mmHg within 15 minutes.
> Entered by: site staff
> Source verified against medical record (source on file) for subject \#30030002.
> 
> Drug Accountability
> Dispensing and returns are recorded on the accountability log at each visit. Temperature excursions must be reported to the sponsor immediately. Tablet counts are compared with the dosing diary to assess compliance. Investigational product is stored in a secure, temperature-monitored area with access limited to authorised staff. Tablet counts are reconciled against the dosing diary to assess compliance. Investigational product is stored in a secure, temperature-monitored area with access limited to authorised staff.
> 
> Tablet counts are reconciled against the dosing diary to assess compliance. Dispensing and returns are recorded on the accountability log at every dispensing visit. Unused product is returned to the sponsor after reconciliation. Dispensing and returns are recorded on the accountability log at each visit. Tablet counts are compared with the dosing diary to assess compliance.
> 
> Dispensing and returns are recorded on the accountability log at every dispensing visit. Dispensing and returns are recorded on the accountability log at each visit. Investigational product is stored in a secure, temperature-monitored area with access limited to authorised staff. Investigational product is stored in a secure, temperature-monitored area with access limited to authorised staff.
> 
> Reporting of Safety Events
> Pregnancy in a participant is reported using the pregnancy notification form within 24 hours. Follow-up information must be provided until the event resolves or the participant is lost to follow-up. The sponsor evaluates each report for expectedness against the reference safety information.
> 
> Non-serious adverse events are recorded in the electronic data capture system throughout the treatment period. Non-serious adverse events are recorded in the electronic data capture system at each visit. Events that begin after the first dose and up to 30 days after the last dose are considered treatment-emergent. Pregnancy in a participant is reported on the dedicated form within one working day. Events that start after the first dose and up to 30 days after the last dose are summarised as treatment-emergent.
> 
> Follow-up information must be provided until the event stabilises or the participant is lost to follow-up. Follow-up information must be provided until the event stabilises or the participant is lost to follow-up. Non-serious adverse events are recorded in the electronic data capture system at each visit. The sponsor reviews each report for expectedness against the reference safety information. All serious adverse events are reported to the sponsor within 48 hours of the investigator becoming aware of the event. Non-serious adverse events are recorded in the electronic data capture system at each visit.
> 
> All serious adverse events must be reported to the sponsor within 48 hours of the investigator becoming aware of the event. Events that start after the first dose and up to 30 days after the last dose are considered treatment-emergent. The sponsor reviews each report for expectedness against the reference safety information.
> 
> Page 1
> 

**d0150:section:4096:0** route forward (p_below_t_low); p(pii) raw 0.3739, calibrated 0.3739; gold role patient, category quasi; missed event_date, initials

> CRF Page 26: Vital Signs
> Protocol FTX-8191-011    Site 1005
> 
> Subject	Initials	Visit	Visit date	SBP	DBP	HR	Temp
> 1005-0001	**J.K.**	Visit 2	**2025-06-24**	158	62	98	37.6
> \#10050001	**JK**	Visit 4	**August 5, 2025**	160	70	55	36.3
> \#10050001	**J.K.**	Visit 5	**2025-08-31**	123	95	59	36.8
> 1005-0002	**D.W.**	Visit 2	**2025-06-18**	151	74	70	36.1
> 1005-0002	**D-W**	Visit 3	**02JUL2025**	132	70	71	36.8
> Subj 1005-0002	**DW**	Visit 4	**27-Jul-2025**	129	74	94	36.4
> Subj 1005-0002	**D.W.**	Visit 5	**August 26, 2025**	137	76	59	36.7
> Subj 1005-0003	**R.S.**	Visit 2	**08/16/2025**	115	78	70	36.6
> Subj 1005-0003	**RS**	Visit 3	**2025-08-27**	163	80	75	37.4
> 1005-0003	**R-S**	Visit 5	**October 22, 2025**	145	86	63	37.6
> Subj 1005-0004	**A-J**	Visit 2	**2025-02-28**	147	86	73	36.7
> 1005-0004	**AJ**	Visit 3	**13-Mar-2025**	156	79	83	37.2
> \#10050004	**AJ**	Visit 4	**April 9, 2025**	150	64	60	37.7
> 1005-0004	**A.J.**	Visit 5	**08-May-2025**	136	66	96	36.5
> Subj 1005-0005	**A-S**	Visit 3	**23MAR2025**	119	87	90	37.0
> Subj 1005-0005	**AS**	Visit 4	**04/19/2025**	119	85	83	36.6
> 1005-0006	**TXP**	Visit 2	**April 19, 2025**	135	68	55	37.7
> Subj 1005-0006	**TP**	Visit 5	**25JUN2025**	125	69	92	36.7
> 1005-0007	**AXG**	Visit 2	**2025-02-12**	162	86	79	36.9
> Subj 1005-0007	**AXG**	Visit 3	**February 24, 2025**	140	76	60	36.3
> \#10050007	**AG**	Visit 4	**March 23, 2025**	120	88	88	36.5
> Subj 1005-0007	**A-G**	Visit 5	**April 20, 2025**	154	84	67	36.6
> Subj 1005-0008	**F-T**	Visit 2	**07-Jun-2025**	121	81	78	37.4
> \#10050008	**F-T**	Visit 3	**2025-06-24**	129	83	88	37.6
> Subj 1005-0008	**FT**	Visit 5	**August 19, 2025**	154	96	66	36.4
> 1005-0009	**S-P**	Visit 3	**September 28, 2025**	117	86	58	36.8
> 1005-0009	**SP**	Visit 4	**October 23, 2025**	139	96	59	37.3
> Subj 1005-0009	**SP**	Visit 5	**2025-11-21**	151	87	56	37.0
> \#10050010	**EK**	Visit 4	**10/22/2025**	106	86	92	37.7
> 1005-0010	**E-K**	Visit 5	**November 17, 2025**	118	97	62	37.6
> \#10050011	**H-L**	Visit 2	**February 27, 2025**	112	93	80	36.5
> \#10050011	**HXL**	Visit 3	**2025-03-12**	160	77	78	36.2
> \#10050011	**HXL**	Visit 5	**09MAY2025**	113	65	77	37.7
> \#10050012	**D-S**	Visit 3	**05/01/2025**	126	75	59	36.8
> \#10050012	**D-S**	Visit 5	**25-Jun-2025**	125	94	96	36.1
> \#10050013	**S.K.**	Visit 2	**2025-02-18**	146	70	69	36.3
> \#10050013	**S.K.**	Visit 3	**04-Mar-2025**	124	81	92	36.6
> Subj 1005-0013	**S.K.**	Visit 4	**04/01/2025**	154	88	71	36.9
> Subj 1005-0013	**SXK**	Visit 5	**2025-04-26**	150	88	81	37.2
> \#10050014	**AŻ**	Visit 2	**05APR2025**	140	81	60	37.2
> Subj 1005-0014	**A-Ż**	Visit 4	**May 18, 2025**	145	74	78	37.3
> Subj 1005-0014	**AXŻ**	Visit 5	**06/16/2025**	158	70	95	36.4
> \#10050015	**J-C**	Visit 2	**06/02/2025**	119	81	78	37.5
> \#10050015	**J.C.**	Visit 3	**19JUN2025**	121	82	93	36.8
> 1005-0015	**JC**	Visit 4	**2025-07-18**	128	81	97	36.6
> 1005-0015	**JC**	Visit 5	**August 14, 2025**	165	81	85	37.0
> 
> Measurements taken seated after 5 minutes of rest. Repeat any systolic value above 160 mmHg within 15 minutes.
> Entered by: site staff
> Source verified against medical record (source on file) for subject \#10050001.
> 
> Investigational product FTX-8191 lot LT-246523-C was dispensed from kit K-042791 within the Day 8 ±1 visit window. Time-to-event endpoints are estimated with the Kaplan-Meier method and compared with a Mantel-Haenszel test stratified by region. Agreement between central and local readings is shown in Bland-Altman plots.
> 
> Safety Reporting
> The investigator assesses intensity using the common terminology criteria and documents the assessment in the source record. Follow-up information must be provided until the event resolves or the participant is lost to follow-up. Non-serious adverse events are recorded in the electronic data capture system at each visit.
> 
> Non-serious adverse events are recorded in the electronic data capture system at each visit. All serious adverse events must be reported to the sponsor within 24 hours of the investigator becoming aware of the event. Follow-up information must be provided until the event stabilises or the participant is lost to follow-up.
> 
> The sponsor reviews each report for expectedness against the reference safety information. Pregnancy occurring during the study is reported on the dedicated form within 24 hours. Follow-up information must be provided until the event stabilises or the participant is lost to follow-up. The responsible physician assesses severity using the common terminology criteria and documents the assessment in the source record. Any serious adverse events are reported to the sponsor within 24 hours of the investigator becoming aware of the event. The sponsor reviews each report for expectedness against the reference safety information.
> 
> All serious adverse events are reported to the sponsor within 48 hours of the investigator becoming aware of the event. Non-serious adverse events are recorded in the electronic data capture system throughout the treatment period. The sponsor evaluates each report for expectedness against the reference safety information.
> 
> Handling of Missing Data
> Missing data are handled by multiple imputation under a missing-at-random assumption. Categorical variables are presented as counts and percentages within each treatment group. Missing data are handled by multiple imputation in the primary analysis. Subgroup analyses by geographic region are exploratory and not adjusted for multiplicity. The statistical analysis plan is finalised before database lock and describes all derived variables. Continuous variables are summarised with the number of observations, mean, standard deviation, median and range.
> 
> Subgroup analyses by geographic region are descriptive and not adjusted for multiplicity. Missing data are not imputed unless stated otherwise in the primary analysis. Sensitivity analyses assess the robustness of the primary result to alternative assumptions.
> 
> Continuous variables are summarised with the number of observations, mean, standard deviation, median and range. The statistical analysis plan is finalised before database lock and specifies all derived variables. All tests are two-sided with a significance level of 5 percent unless otherwise specified. All tests are two-sided with a significance level of 2.5 percent unless otherwise specified. Missing data are not imputed unless stated otherwise under a missing-at-random assumption. Missing data are not imputed unless stated otherwise under a missing-at-random assumption.
> 
> Good Clinical Practice
> The protocol and any amendments must be approved by the ethics committee before implementation. The sponsor may conduct audits of study sites and vendors to verify compliance. The protocol and any amendments are approved by the ethics committee before implementation. Participants may withdraw consent at any time without consequences for their medical care.
> 
> Participants may withdraw consent at any time without consequences for their medical care. Participants may withdraw consent at any time without penalty. Essential documents are retained for at least 15 years after the end of the study as required. Participants may withdraw consent at any time without consequences for their medical care. Participants may withdraw consent at any time without consequences for their medical care.
> 
> Participants may withdraw consent at any time without consequences for their medical care. Confidentiality of participant information is protected in line with applicable data protection law. Essential documents are retained for at least 25 years after the end of the study as required. The informed consent form and any amendments are approved by the ethics committee before implementation.
> 
> The informed consent form and any amendments are approved by the ethics committee before implementation. Confidentiality of participant information is protected in line with applicable data protection law. The sponsor may conduct audits of study sites and vendors to verify compliance. Participants may withdraw consent at any time without penalty. Essential documents are retained for at least 15 years after the end of the study as required.
> 
> Laboratory Assessments
> Blood samples are collected in the morning and processed within two hours. Clinically significant laboratory abnormalities should be recorded as adverse events. Blood samples are collected after an overnight fast and processed according to the laboratory manual. Samples are shipped frozen on dry ice to the central laboratory with the requisition form. Blood samples are collected after an overnight fast and processed according to the laboratory manual.
> 
> Blood samples are collected in the morning and processed according to the laboratory manual. Reference ranges are provided by the laboratory and updated when changed. Clinically significant laboratory abnormalities should be recorded as adverse events. Blood samples are collected after an overnight fast and processed within two hours.
> 
> Data Management
> Data are entered into a validated electronic data capture system with an audit trail. Reconciliation of laboratory data with the clinical database is performed before each data cut. Medical history and adverse events are coded with a standard dictionary during the study. Access to the database is restricted to authorised personnel according to the access matrix. Access to the database is restricted to authorised personnel according to the access matrix.
> 
> Edit checks flag missing, inconsistent or out-of-range values during cleaning. Reconciliation of laboratory data with the clinical database is performed before each data cut. Reconciliation of laboratory data with the clinical database is performed periodically. Data are entered into a validated clinical database with an audit trail.
> 
> Reconciliation of safety data with the clinical database is performed before each data cut. Edit checks identify missing, inconsistent or out-of-range values at entry. Edit checks flag missing, inconsistent or out-of-range values at entry. Data are entered into a validated clinical database with an audit trail.
> 
> Reconciliation of safety data with the clinical database is performed before each data cut. Reconciliation of laboratory data with the clinical database is performed periodically. Medical history and adverse events are coded with standard terminology before database lock. Data are entered into a validated clinical database with an audit trail.
> 

**d0352:section:4096:0** route forward (p_below_t_low); p(pii) raw 0.0471, calibrated 0.0471; gold role both, category direct; missed dob, event_date, initials, person_name, phone

> Fenwick Therapeutics \| Protocolo FTX-5142-018 \| Confidencial
> 
> CIOMS I: notificación de sospecha de reacción adversa
> N.º de control: FEN-2025342    Protocolo: FTX-5142-018    Centro: 3003
> 
> I. Información de la reacción
> 1. Iniciales: **PA**    1a. Sujeto: \#30030005
> 2. Fecha de nacimiento: **7 de agosto de 1961**    2a. Edad: 63 años    3. Sexo: F
> 4-6. Inicio de la reacción: **18/04/2025**
> 7+13. Descripción: fatiga, grado 2; requirió hospitalización.
> 
> V. Notificador
> 24b. **A. Marcos**, Centro de Investigación Clínica Llanodorado, tel. **+34 555 019 6055**
> 25a. Fecha de este informe: 01/05/2025
> 
> Página 1
> 

**d0377:section:4096:0** route forward (p_below_t_low); p(pii) raw 0.3661, calibrated 0.3661; gold role both, category quasi; missed email, event_date, person_name, phone

> Von: **Dieter Schmidtke** \<**d.schmidtke@niederheide-crc.example.org**\>
> An: **Riza Scheel** \<**r.scheel@fenwick-tx.example.com**\>
> Betreff: AW: Datenklärung zu Teilnehmer 3005-0010
> Hallo **Riza**,
> 
> die offenen Fragen wurden bearbeitet und die Einträge im eCRF korrigiert.
> Die korrigierten Seiten liegen im Prüfarztordner; die Quelldokumente wurden erneut abgeglichen. Bitte geben Sie kurz Bescheid, ob weitere Anfragen offen sind.
> Teilnehmer \#30050010: Daten der Visite 2 (**27. April 2025**) korrigiert.
> Die Papierquelle für diesen Teilnehmer liegt im Teilnehmerordner.
> 
> Viele Grüße
> **Dieter Schmidtke**
> Klinikum Niederheide
> Tel. **+49 555 017 9336**
> 
> \> Am 2025-05-28 schrieb **Riza Scheel**:
> \> Hallo **Dieter**, bitte prüfen Sie die offenen Anfragen.
> \> Danke, **Riza**
> 
> Ereigniszeitanalysen verwenden die Kaplan-Meier-Methode; die Kreatinin-Clearance wird nach Cockcroft-Gault berechnet. Prüfplan FTX-5142-018 (NCT99608180; EudraCT 2031-854061-77), Amendment A1, gültig ab 05.10.2025. Prüfpräparat FTX-5142, Charge LT-230007-D, wurde aus Kit K-283296 im Visitenfenster Day 85 ±1 ausgegeben.
> 

**d0447:section:4096:0** route forward (p_below_t_low); p(pii) raw 0.2966, calibrated 0.2966; gold role both, category direct; missed address, dob, event_date, initials, mrn, person_name, zip

> Fenwick Therapeutics \| Prüfplan FTX-5142-018 \| Vertraulich
> 
> Patientennarrativ: Prüfungsteilnehmer Subj 3005-0010
> Prüfplan FTX-5142-018, Prüfzentrum 3005
> 
> Demografie und Ausgangsbefund
> **P. Rohleder** (**P-R**), 75 Jahre, geb. **18. Juli 1949**, Patientennummer **70322471**, wurde am **15. April 2025** randomisiert (Randomisierungsnummer R-65247) und erhielt am selben Tag die erste Dosis FTX-5142. Wohnort: **Baumring 1-8, Niederheide** **30576**.
> Die Begleitmedikation wurde von **SCHMIDTKE, Dieter** überprüft.
> 
> Unerwünschtes Ereignis
> Während der Behandlungsphase wurden keine unerwünschten Ereignisse gemeldet.
> 
> Ereigniszeitanalysen verwenden die Kaplan-Meier-Methode; die Kreatinin-Clearance wird nach Cockcroft-Gault berechnet. Prüfpräparat FTX-5142, Charge LT-255487-A, wurde aus Kit K-954687 im Visitenfenster Day 29 ±3 ausgegeben. Prüfplan FTX-5142-018 (NCT99608180; EudraCT 2031-854061-77), Amendment A5, gültig ab 2025-04-03.
> 
> Verlauf
> Die Teilnahme wurde gemäß Prüfplan fortgesetzt.
> 
> Seite 1
> 

### B3 / qs_v2 (doc-level, underpowered), holdout: 0 false forward(s)

### B4 / qs_v1 (doc-level, underpowered), test: 2 false forward(s)

**d0352:doc:8192:0** route forward (p_below_t_low); p(pii) raw 0.0499, calibrated 0.2720; gold role both, category direct; missed dob, event_date, initials, person_name, phone

> Fenwick Therapeutics \| Protocolo FTX-5142-018 \| Confidencial
> 
> CIOMS I: notificación de sospecha de reacción adversa
> N.º de control: FEN-2025342    Protocolo: FTX-5142-018    Centro: 3003
> 
> I. Información de la reacción
> 1. Iniciales: **PA**    1a. Sujeto: \#30030005
> 2. Fecha de nacimiento: **7 de agosto de 1961**    2a. Edad: 63 años    3. Sexo: F
> 4-6. Inicio de la reacción: **18/04/2025**
> 7+13. Descripción: fatiga, grado 2; requirió hospitalización.
> 
> V. Notificador
> 24b. **A. Marcos**, Centro de Investigación Clínica Llanodorado, tel. **+34 555 019 6055**
> 25a. Fecha de este informe: 01/05/2025
> 
> Página 1
> 

**d0418:doc:8192:0** route forward (p_below_t_low); p(pii) raw 0.0747, calibrated 0.3014; gold role both, category quasi; missed event_date, initials

> Fenwick Therapeutics \| Protocol FTX-5142-018 \| Confidential
> 
> CRF Page 14: Vital Signs
> Protocol FTX-5142-018    Site 3005
> 
> Subject \| Initials \| Visit \| Visit date \| SBP \| DBP \| HR \| Temp
> 3005-0001 \| **J-B** \| Visit 2 \| **June 18, 2025** \| 149 \| 75 \| 81 \| 36.6
> 3005-0001 \| **J-B** \| Visit 3 \| **29JUN2025** \| 120 \| 64 \| 69 \| 37.5
> \#30050001 \| **J.B.** \| Visit 4 \| **30-Jul-2025** \| 107 \| 94 \| 92 \| 37.4
> \#300S0001 \| **J-B** \| Visit 5 \| **08/27/2025** \| 132 \| 81 \| 58 \| 36.4
> 3005-0002 \| **S.H.** \| Visit 2 \| **06-May-2025** \| 113 \| 77 \| 59 \| 37.5
> Subj 3005-0002 \| **S-H** \| Visit 3 \| **2025-05-20** \| 111 \| 67 \| 98 \| 37.2
> Subj 3005-0002 \| **S-H** \| Visit 4 \| **06/18/2025** \| 118 \| 79 \| 81 \| 37.2
> 3005-0002 \| **S-H** \| Visit 5 \| **13JUL2025** \| 109 \| 78 \| 61 \| 37.6
> 3005-0003 \| **S.S.** \| Visit 2 \| **23-Sep-2025** \| 127 \| 96 \| 62 \| 36.9
> Subj 3005-0003 \| **S.S.** \| Visit 3 \| **10/06/2025** \| 162 \| 91 \| 63 \| 37.7
> \#30050003 \| **SS** \| Visit 4 \| **November 6, 2025** \| 164 \| 62 \| 58 \| 37.5
> \#30050003 \| **SXS** \| Visit S \| **04DECZ025** \| 111 \| 85 \| 65 \| 37.2
> Subj 3005-0004 \| **E-W** \| Visit Z \| **2025-08-18** \| 126 \| 81 \| 64 \| 37.0
> \#30050004 \| **E.W.** \| Visit 3 \| **August 28, 2025** \| 135 \| 72 \| 60 \| 37.5
> Subj 3005-0004 \| **EXW** \| Visit 4 \| **09/28/2025** \| 143 \| 98 \| 89 \| 37.2
> 3005-0004 \| **E-W** \| Viit 5 \| **25OCT2O25** \| 124 \| 72 \| 80 \| 37.7
> Subj 3005-0005 \| **LXK** \| Visit 2 \| **June 10, 2025** \| 112 \| 83 \| 88 \| 36.8
> Subj 3005-0005 \| **LXK** \| Visit 3 \| **June 25, 20Z5** \| 152 \| 97 \| 67 \| 37.1
> Subj 3005-0005 \| **L-K** \| Visit 4 \| **25-Jul-2025** \| 155 \| 62 \| 93 \| 37.1
> 3005-0005 \| **L-K** \| Visit 5 \| **08/22/2025** \| 146 \| 70 \| 72 \| 37.2
> Subj 3005-0006 \| **G.P.** \| Visit 2 \| **24-Jul-2025** \| 134 \| 77 \| 86 \| 37.0
> Subj 3005-0006 \| **GXP** \| Visit 3 \| **August 11, 2025** \| 158 \| 65 \| 58 \| 37.7
> \#30050006 \| **GXP** \| Visit 4 \| **09/06/2025** \| 106 \| 76 \| 77 \| 36.9
> 3005-0006 \| **G-P** \| Visit 5 \| **04OCT2025** \| 158 \| 85 \| 78 \| 36.7
> 3005-0007 \| **E-M** \| Visit 2 \| **2025-05-19** \| 118 \| 74 \| 82 \| 37.7
> 3005-0007 \| **EXM** \| Visit 3 \| **June 2, 2025** \| 111 \| 74 \| 82 \| 37.7
> \#30050007 \| **EM** \| Visit 4 \| **30JUN20Z5** \| 143 \| 67 \| 92 \| 37.3
> \#30050007 \| **E-M** \| Visit 5 \| **27JUL2025** \| 110 \| 80 \| 94 \| 36.3
> Subj 3005-0008 \| **S-K** \| Visit 3 \| **2025-08-03** \| 134 \| 86 \| 78 \| 36.5
> 3005-0008 \| **SXK** \| Visit 4 \| **2025-09-01** \| 121 \| 71 \| 67 \| 37.0
> \#30050008 \| **SXK** \| Visit 5 \| **01-Oct-2025** \| 161 \| 68 \| 83 \| 36.7
> Subj 3005-0009 \| **D.E.** \| Visit 2 \| **May 2, 2025** \| 125 \| 81 \| 90 \| 36.3
> 3005-0009 \| **DE** \| Visit 4 \| **06/14/2025** \| 153 \| 62 \| 86 \| 37.6
> \#30050010 \| **PR** \| Visit 2 \| **27APR2025** \| 153 \| 92 \| 88 \| 37.7
> Subj 3005-0010 \| **P.R.** \| Visit 3 \| **13-May-2025** \| 112 \| 76 \| 98 \| 36.7
> \#30050010 \| **P-R** \| Visit 4 \| **11JUN2025** \| 106 \| 79 \| 95 \| 37.4
> \#30050011 \| **D.R.** \| Visit 2 \| **22MAR2025** \| 120 \| 69 \| 68 \| 36.4
> Subj 3005-0011 \| **DR** \| Visit 3 \| **03-Apr-2025** \| 136 \| 94 \| 74 \| 36.7
> Subj 3005-0011 \| **D.R.** \| Visit 4 \| **2025-04-30** \| 162 \| 66 \| 81 \| 36.7
> \#30050011 \| **D-R** \| Visit 5 \| **31MAY2025** \| 149 \| 83 \| 58 \| 37.5
> 300S-0012 \| **JXG** \| Visit 2 \| **02/24/2025** \| 136 \| 71 \| 65 \| 36.2
> Subj 3005-0012 \| **JG** \| Visit 3 \| **March 6, 2025** \| 156 \| 63 \| 62 \| 36.2
> \#30050012 \| **J-G** \| Visit 4 \| **05-Apr-2025** \| 161 \| 86 \| 86 \| 36.8
> \#3005001Z \| **JXG** \| Visit 5 \| **01-May-2025** \| 116 \| 98 \| 93 \| 37.0
> Subj 3005-0013 \| **S-E** \| Viit 2 \| **July 23, 2025** \| 147 \| 87 \| 63 \| 37.8
> Subj 3005-0013 \| **S-E** \| Visit 3 \| **04AUG2025** \| 139 \| 78 \| 66 \| 37.2
> 3005-0013 \| **S.E.** \| Visit 5 \| **09/30/2025** \| 123 \| 82 \| 84 \| 36.9
> \#30050014 \| **SXG** \| Visit 2 \| **February 9, 2025** \| 144 \| 68 \| 89 \| 37.0
> \#30050014 \| **S.G.** \| Visit 3 \| **21-Feb-2025** \| 147 \| 69 \| 81 \| 36.4
> 3005-0014 \| **SG** \| Visit 4 \| **22MAR2025** \| 125 \| 93 \| 69 \| 36.1
> \#30050014 \| **SG** \| Visit 5 \| **18APR2025** \| 138 \| 77 \| 59 \| 37.6
> Subj 3005-0015 \| **D.M.** \| Visit 2 \| **09-May-2025** \| 151 \| 96 \| 69 \| 37.3
> \#30050015 \| **DXM** \| Visit 3 \| **May 25, 2O25** \| 132 \| 84 \| 78 \| 37.3
> 3005-0O15 \| **D.M.** \| Visit 4 \| **June 20, 2025** \| 107 \| 62 \| 55 \| 37.1
> 
> Measurements taken seated after 5 minutes of rest. Repeat any systolic value above 16O mmHg within 15 minutes.
> Entered by: **AXW**
> Source verified against medical record (source on file) for subject 3005-0001.
> 
> Events are coded to MedDRA preferred term 10586823; the target dose is 150 mg. Agreement between central and local readigs is shown in Bland-Altman plots. Secondary endpoints are compard with the Wilcoxon test with Bonferroni correction; sparse tables use Fisher's exact test.
> 
> Database Procedures
> Access to the database is restricted to authorised personnel with role-based permissions. Edit checks identify missing, inconsistent or out-of-range values during cleaning. Reconciliation of safety data with the clinical database is performed periodically. Edit checks identify missing, inconsistent or out-of-range values during cleaning. Access to the database is restricted to authorised personnel with role-based permissions.
> 
> Data are entered into a validated c1inical database with an audit trail. Edit checks identify missing, inconsistent or out-of-range vlues at entry. Medical history and adverse evets are coded with a standard dictionary before database lock. Medical history and adverse events are coded with standard terminology before database lock.
> 
> Source Data Verification
> Queries are raised in the data capture system and resolved by site staff within ten working days. Protocol deviations are classified as minor or major. The investigator site file is reviewed for completeness at each visit. Source data verification prioritises eligibility, informed consent, primary endpoints and serious aderse events. Queries are raised in the data capture system and answered by the site within ten working days.
> 
> Protocol deviations are assessed for impact on participant safety and data integrity. The investigator site file is reviewed for currency of essential documents at each visit. Protocol deviations are classified as minor or majr.
> 
> On-site and remote monitoring visits are scheduled based on enrollment and risk indicators. The investigator site file is reviewed for completeness at each visit. Findings are documented in the visit report and followed up until closure.
> 
> Analysis Methods
> Sensitivity analyses assess the robustness of the primary result to protocol deviations. All tests are two-sided with a significance level of 5 percent unless otherwise specified. Subgroup analyses by geograhic region are exploratory and not adjusted for multiplicity.
> 
> Subgroup analyses by age group are descriptive and not adjusted for multiplicity. All tests are two-sided with a significance level of 5 pecnt unless otherwise spcified. Continuous variables are summaised with the nmber of observations, mean, standard deviation, median and range. Sensitivity analyses assess the robstness of the primary result to alternative assumptions. The statistical analyss plan is finalised befre database lock and specifies all derived variab1es.
> 
> Categorical vriables are presented as counts and percentages within each treatment group. Subgroup analyses by baseline severity are descriptive and not adjusted for multiplicity. Categorical variables are presented as counts and percentages of the analysis set.
> 
> Page 1
> 
> Fenwick Therapeutics \| Protocol FTX-5142-018 \| Confidential
> 
> Categorical variables are presented as counts and percentages of the analysis set. All tests are two-sided with a significance level of 2.5 percent unless otherwise specified. Sensitivity aalses asess the robustness of the primary resu1t to alternative assumptions. Continuous variables are summarised wih the number of observations, mean, standard deviation, median and range. All tests are two-sided with a significance level of 5 percent unless otherwise specified. Categorical variables are presented as counts and percentages of the analysis set.
> 
> Drug Accountabiliy
> Investigational product is stored in a secure, temperature-monitored area with access limited to authorised staff. Dispensing and returns are recorded on the accountability log at every dispensing visit. Temperature excursions must be reported to the sponsor before further use of the affected supply. Unused product is returned to the sponsor after reconciliation. Dispensing and returns are recorded on the accountability log at every dispensing visit. Unused product is destroyed according to local procedures after reconciliation.
> 
> Investigtional product is stored in a secure, temperature-monitored area with access limited to authorised staff. Temperature excursions must be reported to the sponsor immediately. Temperature excursions are reported to the sponsor immediately. Temperature excursions must be reported to the sponsor before further use of the affected suply.
> 
> Tablet counts are reconciled against the dosing dary to assess compliance. Tablet counts are reconciled against the dosing diary to assss compliance. Dispensing and returns are recorded on the accountability log at every dispensing visit. Temperature excursons are reported to the sponsor immediately. Investigational product is stored in a secure, temerature-monitored area with access limited to authorised staff.
> 
> Reporting of Safety Events
> The investigator assesses intensity using the common terminology citeria and documents the assessment in te source record. Pregnancy in a participant is reported using the pregnancy notification form within 24 hours. Pregnancy in a participant is reported using the pregnancy notification form within one working day. The responsible physician assesses intensity using the common terminology criteria and documents the assessment in the source record. The resonsible physician assesses intensity using the common terminology criteria and documets the assessment in the source record.
> 
> Pregnancy in a participant is reported using the pregnancy notification form withn 24 hours. Evets that start after the first dose and until 28 days after the last dose are considered treatment-emergent. Follow-up information is provided until the event stabilises or the participant is lost to follow-up. Events that begin after the first dose and up to 28 days after the last dose are summarised as treatment-emergent. Non-serious adverse events are recorded in the case report form throughout the treatment period.
> 
> Any serious adverse events are reported to the sponsor within 24 hours of the site becoming aware of the event. All serios adverse events must be reported to the sponsor within 48 hours of the investigator becoming aware of the event. Non-serious adverse events are recored in te case reprt form throughout the treatment period.
> 
> Page 2
> 

### B4 / qs_v1 (doc-level, underpowered), holdout: 0 false forward(s)

### B4 / qs_v2 (doc-level, underpowered), test: 6 false forward(s)

**d0062:doc:8192:0** route forward (p_below_t_low); p(pii) raw 0.4012, calibrated 0.4674; gold role patient, category quasi; missed event_date, initials

> CRF Page 15: Vital Signs
> Protocol FTX-9990-002    Site 2003
> 
> Subject \| Initials \| Visit \| Visit date \| SBP \| DBP \| HR \| Temp
> Subj 2003-0001 \| **TW** \| Visit 5 \| **2025-05-12** \| 141 \| 85 \| 84 \| 37.0
> \#20030004 \| **K.C.** \| Visit 5 \| **15SEP2025** \| 135 \| 89 \| 95 \| 36.1
> Subj 2003-0006 \| **AXC** \| Visit 2 \| **2025-08-07** \| 111 \| 70 \| 61 \| 37.2
> Subj 2003-0008 \| **LXH** \| Visit 2 \| **2025-03-20** \| 159 \| 63 \| 94 \| 36.2
> Subj 2003-0010 \| **SO** \| Visit 4 \| **03JUL2025** \| 143 \| 69 \| 76 \| 37.7
> 2003-0014 \| **EH** \| Visit 5 \| **06/14/2025** \| 119 \| 89 \| 77 \| 36.6
> 
> Measurements taken seated after 5 minutes of rest. Repeat any systolic value above 160 mmHg within 15 minutes.
> Entered by: site staff
> Source verified against medical record (source on file) for subject Subj 2003-0001.
> 
> Laboratory Assessments
> Blood samples are collected after an overnight fast and processed within two hours. Samples are shipped at ambient temperature to the central laboratory with the requisition form. Clinically significant laboratory abnormalities are recorded as adverse events. Reference ranges are provided by the laboratory and updated when changed.
> 
> Blood samples are collected after an overnight fast and processed according to the laboratory manual. Clinically significant laboratory abnormalities are recorded as adverse events. Blood samples are collected after an overnight fast and processed within two hours. Clinically significant laboratory abnormalities should be recorded as adverse events.
> 
> Blood samples are collected after an overnight fast and processed within two hours. Blood samples are collected in the morning and processed within two hours. Blood samples are collected after an overnight fast and processed within two hours. Reference ranges are provided by the laboratory and updated when changed. Samples are shipped frozen on dry ice to the central laboratory with the requisition form. Reference ranges are provided by the laboratory and filed in the investigator site file.
> 
> Good Clinical Practice
> The study will be conducted in accordance with the principles of good clinical practice and applicable regulatory requirements. The sponsor may conduct audits of study sites and vendors to verify compliance. Confidentiality of participant information is protected at all times.
> 
> Confidentiality of participant information is protected at all times. Essential documents are retained for at least 25 years after the end of the study or longer if required by local regulations. The sponsor reserves the right to conduct audits of study sites and vendors to verify compliance. The informed consent form and any amendments must be approved by the ethics committee before implementation.
> 
> Participants may withdraw consent at any time without consequences for their medical care. Participants may withdraw consent at any time without consequences for their medical care. Essential documents are retained for at least 25 years after the end of the study or longer if required by local regulations. Participants may withdraw consent at any time without consequences for their medical care. The protocol and any amendments are approved by the ethics committee before implementation.
> 
> Essential documents are retained for at least 15 years after the end of the study or longer if required by local regulations. The sponsor reserves the right to conduct audits of study sites and vendors to verify compliance. The protocol and any amendments must be approved by the ethics committee before implementation. Confidentiality of participant information is protected in line with applicable data protection law. Essential documents are retained for at least 15 years after the end of the study as required.
> 

**d0150:doc:8192:0** route forward (p_below_t_low); p(pii) raw 0.3739, calibrated 0.4580; gold role patient, category quasi; missed event_date, initials

> CRF Page 26: Vital Signs
> Protocol FTX-8191-011    Site 1005
> 
> Subject	Initials	Visit	Visit date	SBP	DBP	HR	Temp
> 1005-0001	**J.K.**	Visit 2	**2025-06-24**	158	62	98	37.6
> \#10050001	**JK**	Visit 4	**August 5, 2025**	160	70	55	36.3
> \#10050001	**J.K.**	Visit 5	**2025-08-31**	123	95	59	36.8
> 1005-0002	**D.W.**	Visit 2	**2025-06-18**	151	74	70	36.1
> 1005-0002	**D-W**	Visit 3	**02JUL2025**	132	70	71	36.8
> Subj 1005-0002	**DW**	Visit 4	**27-Jul-2025**	129	74	94	36.4
> Subj 1005-0002	**D.W.**	Visit 5	**August 26, 2025**	137	76	59	36.7
> Subj 1005-0003	**R.S.**	Visit 2	**08/16/2025**	115	78	70	36.6
> Subj 1005-0003	**RS**	Visit 3	**2025-08-27**	163	80	75	37.4
> 1005-0003	**R-S**	Visit 5	**October 22, 2025**	145	86	63	37.6
> Subj 1005-0004	**A-J**	Visit 2	**2025-02-28**	147	86	73	36.7
> 1005-0004	**AJ**	Visit 3	**13-Mar-2025**	156	79	83	37.2
> \#10050004	**AJ**	Visit 4	**April 9, 2025**	150	64	60	37.7
> 1005-0004	**A.J.**	Visit 5	**08-May-2025**	136	66	96	36.5
> Subj 1005-0005	**A-S**	Visit 3	**23MAR2025**	119	87	90	37.0
> Subj 1005-0005	**AS**	Visit 4	**04/19/2025**	119	85	83	36.6
> 1005-0006	**TXP**	Visit 2	**April 19, 2025**	135	68	55	37.7
> Subj 1005-0006	**TP**	Visit 5	**25JUN2025**	125	69	92	36.7
> 1005-0007	**AXG**	Visit 2	**2025-02-12**	162	86	79	36.9
> Subj 1005-0007	**AXG**	Visit 3	**February 24, 2025**	140	76	60	36.3
> \#10050007	**AG**	Visit 4	**March 23, 2025**	120	88	88	36.5
> Subj 1005-0007	**A-G**	Visit 5	**April 20, 2025**	154	84	67	36.6
> Subj 1005-0008	**F-T**	Visit 2	**07-Jun-2025**	121	81	78	37.4
> \#10050008	**F-T**	Visit 3	**2025-06-24**	129	83	88	37.6
> Subj 1005-0008	**FT**	Visit 5	**August 19, 2025**	154	96	66	36.4
> 1005-0009	**S-P**	Visit 3	**September 28, 2025**	117	86	58	36.8
> 1005-0009	**SP**	Visit 4	**October 23, 2025**	139	96	59	37.3
> Subj 1005-0009	**SP**	Visit 5	**2025-11-21**	151	87	56	37.0
> \#10050010	**EK**	Visit 4	**10/22/2025**	106	86	92	37.7
> 1005-0010	**E-K**	Visit 5	**November 17, 2025**	118	97	62	37.6
> \#10050011	**H-L**	Visit 2	**February 27, 2025**	112	93	80	36.5
> \#10050011	**HXL**	Visit 3	**2025-03-12**	160	77	78	36.2
> \#10050011	**HXL**	Visit 5	**09MAY2025**	113	65	77	37.7
> \#10050012	**D-S**	Visit 3	**05/01/2025**	126	75	59	36.8
> \#10050012	**D-S**	Visit 5	**25-Jun-2025**	125	94	96	36.1
> \#10050013	**S.K.**	Visit 2	**2025-02-18**	146	70	69	36.3
> \#10050013	**S.K.**	Visit 3	**04-Mar-2025**	124	81	92	36.6
> Subj 1005-0013	**S.K.**	Visit 4	**04/01/2025**	154	88	71	36.9
> Subj 1005-0013	**SXK**	Visit 5	**2025-04-26**	150	88	81	37.2
> \#10050014	**AŻ**	Visit 2	**05APR2025**	140	81	60	37.2
> Subj 1005-0014	**A-Ż**	Visit 4	**May 18, 2025**	145	74	78	37.3
> Subj 1005-0014	**AXŻ**	Visit 5	**06/16/2025**	158	70	95	36.4
> \#10050015	**J-C**	Visit 2	**06/02/2025**	119	81	78	37.5
> \#10050015	**J.C.**	Visit 3	**19JUN2025**	121	82	93	36.8
> 1005-0015	**JC**	Visit 4	**2025-07-18**	128	81	97	36.6
> 1005-0015	**JC**	Visit 5	**August 14, 2025**	165	81	85	37.0
> 
> Measurements taken seated after 5 minutes of rest. Repeat any systolic value above 160 mmHg within 15 minutes.
> Entered by: site staff
> Source verified against medical record (source on file) for subject \#10050001.
> 
> Investigational product FTX-8191 lot LT-246523-C was dispensed from kit K-042791 within the Day 8 ±1 visit window. Time-to-event endpoints are estimated with the Kaplan-Meier method and compared with a Mantel-Haenszel test stratified by region. Agreement between central and local readings is shown in Bland-Altman plots.
> 
> Safety Reporting
> The investigator assesses intensity using the common terminology criteria and documents the assessment in the source record. Follow-up information must be provided until the event resolves or the participant is lost to follow-up. Non-serious adverse events are recorded in the electronic data capture system at each visit.
> 
> Non-serious adverse events are recorded in the electronic data capture system at each visit. All serious adverse events must be reported to the sponsor within 24 hours of the investigator becoming aware of the event. Follow-up information must be provided until the event stabilises or the participant is lost to follow-up.
> 
> The sponsor reviews each report for expectedness against the reference safety information. Pregnancy occurring during the study is reported on the dedicated form within 24 hours. Follow-up information must be provided until the event stabilises or the participant is lost to follow-up. The responsible physician assesses severity using the common terminology criteria and documents the assessment in the source record. Any serious adverse events are reported to the sponsor within 24 hours of the investigator becoming aware of the event. The sponsor reviews each report for expectedness against the reference safety information.
> 
> All serious adverse events are reported to the sponsor within 48 hours of the investigator becoming aware of the event. Non-serious adverse events are recorded in the electronic data capture system throughout the treatment period. The sponsor evaluates each report for expectedness against the reference safety information.
> 
> Handling of Missing Data
> Missing data are handled by multiple imputation under a missing-at-random assumption. Categorical variables are presented as counts and percentages within each treatment group. Missing data are handled by multiple imputation in the primary analysis. Subgroup analyses by geographic region are exploratory and not adjusted for multiplicity. The statistical analysis plan is finalised before database lock and describes all derived variables. Continuous variables are summarised with the number of observations, mean, standard deviation, median and range.
> 
> Subgroup analyses by geographic region are descriptive and not adjusted for multiplicity. Missing data are not imputed unless stated otherwise in the primary analysis. Sensitivity analyses assess the robustness of the primary result to alternative assumptions.
> 
> Continuous variables are summarised with the number of observations, mean, standard deviation, median and range. The statistical analysis plan is finalised before database lock and specifies all derived variables. All tests are two-sided with a significance level of 5 percent unless otherwise specified. All tests are two-sided with a significance level of 2.5 percent unless otherwise specified. Missing data are not imputed unless stated otherwise under a missing-at-random assumption. Missing data are not imputed unless stated otherwise under a missing-at-random assumption.
> 
> Good Clinical Practice
> The protocol and any amendments must be approved by the ethics committee before implementation. The sponsor may conduct audits of study sites and vendors to verify compliance. The protocol and any amendments are approved by the ethics committee before implementation. Participants may withdraw consent at any time without consequences for their medical care.
> 
> Participants may withdraw consent at any time without consequences for their medical care. Participants may withdraw consent at any time without penalty. Essential documents are retained for at least 15 years after the end of the study as required. Participants may withdraw consent at any time without consequences for their medical care. Participants may withdraw consent at any time without consequences for their medical care.
> 
> Participants may withdraw consent at any time without consequences for their medical care. Confidentiality of participant information is protected in line with applicable data protection law. Essential documents are retained for at least 25 years after the end of the study as required. The informed consent form and any amendments are approved by the ethics committee before implementation.
> 
> The informed consent form and any amendments are approved by the ethics committee before implementation. Confidentiality of participant information is protected in line with applicable data protection law. The sponsor may conduct audits of study sites and vendors to verify compliance. Participants may withdraw consent at any time without penalty. Essential documents are retained for at least 15 years after the end of the study as required.
> 
> Laboratory Assessments
> Blood samples are collected in the morning and processed within two hours. Clinically significant laboratory abnormalities should be recorded as adverse events. Blood samples are collected after an overnight fast and processed according to the laboratory manual. Samples are shipped frozen on dry ice to the central laboratory with the requisition form. Blood samples are collected after an overnight fast and processed according to the laboratory manual.
> 
> Blood samples are collected in the morning and processed according to the laboratory manual. Reference ranges are provided by the laboratory and updated when changed. Clinically significant laboratory abnormalities should be recorded as adverse events. Blood samples are collected after an overnight fast and processed within two hours.
> 
> Data Management
> Data are entered into a validated electronic data capture system with an audit trail. Reconciliation of laboratory data with the clinical database is performed before each data cut. Medical history and adverse events are coded with a standard dictionary during the study. Access to the database is restricted to authorised personnel according to the access matrix. Access to the database is restricted to authorised personnel according to the access matrix.
> 
> Edit checks flag missing, inconsistent or out-of-range values during cleaning. Reconciliation of laboratory data with the clinical database is performed before each data cut. Reconciliation of laboratory data with the clinical database is performed periodically. Data are entered into a validated clinical database with an audit trail.
> 
> Reconciliation of safety data with the clinical database is performed before each data cut. Edit checks identify missing, inconsistent or out-of-range values at entry. Edit checks flag missing, inconsistent or out-of-range values at entry. Data are entered into a validated clinical database with an audit trail.
> 
> Reconciliation of safety data with the clinical database is performed before each data cut. Reconciliation of laboratory data with the clinical database is performed periodically. Medical history and adverse events are coded with standard terminology before database lock. Data are entered into a validated clinical database with an audit trail.
> 

**d0352:doc:8192:0** route forward (p_below_t_low); p(pii) raw 0.0471, calibrated 0.2725; gold role both, category direct; missed dob, event_date, initials, person_name, phone

> Fenwick Therapeutics \| Protocolo FTX-5142-018 \| Confidencial
> 
> CIOMS I: notificación de sospecha de reacción adversa
> N.º de control: FEN-2025342    Protocolo: FTX-5142-018    Centro: 3003
> 
> I. Información de la reacción
> 1. Iniciales: **PA**    1a. Sujeto: \#30030005
> 2. Fecha de nacimiento: **7 de agosto de 1961**    2a. Edad: 63 años    3. Sexo: F
> 4-6. Inicio de la reacción: **18/04/2025**
> 7+13. Descripción: fatiga, grado 2; requirió hospitalización.
> 
> V. Notificador
> 24b. **A. Marcos**, Centro de Investigación Clínica Llanodorado, tel. **+34 555 019 6055**
> 25a. Fecha de este informe: 01/05/2025
> 
> Página 1
> 

**d0377:doc:8192:0** route forward (p_below_t_low); p(pii) raw 0.3661, calibrated 0.4553; gold role both, category quasi; missed email, event_date, person_name, phone

> Von: **Dieter Schmidtke** \<**d.schmidtke@niederheide-crc.example.org**\>
> An: **Riza Scheel** \<**r.scheel@fenwick-tx.example.com**\>
> Betreff: AW: Datenklärung zu Teilnehmer 3005-0010
> Hallo **Riza**,
> 
> die offenen Fragen wurden bearbeitet und die Einträge im eCRF korrigiert.
> Die korrigierten Seiten liegen im Prüfarztordner; die Quelldokumente wurden erneut abgeglichen. Bitte geben Sie kurz Bescheid, ob weitere Anfragen offen sind.
> Teilnehmer \#30050010: Daten der Visite 2 (**27. April 2025**) korrigiert.
> Die Papierquelle für diesen Teilnehmer liegt im Teilnehmerordner.
> 
> Viele Grüße
> **Dieter Schmidtke**
> Klinikum Niederheide
> Tel. **+49 555 017 9336**
> 
> \> Am 2025-05-28 schrieb **Riza Scheel**:
> \> Hallo **Dieter**, bitte prüfen Sie die offenen Anfragen.
> \> Danke, **Riza**
> 
> Ereigniszeitanalysen verwenden die Kaplan-Meier-Methode; die Kreatinin-Clearance wird nach Cockcroft-Gault berechnet. Prüfplan FTX-5142-018 (NCT99608180; EudraCT 2031-854061-77), Amendment A1, gültig ab 05.10.2025. Prüfpräparat FTX-5142, Charge LT-230007-D, wurde aus Kit K-283296 im Visitenfenster Day 85 ±1 ausgegeben.
> 

**d0418:doc:8192:0** route forward (p_below_t_low); p(pii) raw 0.4244, calibrated 0.4751; gold role both, category quasi; missed event_date, initials

> Fenwick Therapeutics \| Protocol FTX-5142-018 \| Confidential
> 
> CRF Page 14: Vital Signs
> Protocol FTX-5142-018    Site 3005
> 
> Subject \| Initials \| Visit \| Visit date \| SBP \| DBP \| HR \| Temp
> 3005-0001 \| **J-B** \| Visit 2 \| **June 18, 2025** \| 149 \| 75 \| 81 \| 36.6
> 3005-0001 \| **J-B** \| Visit 3 \| **29JUN2025** \| 120 \| 64 \| 69 \| 37.5
> \#30050001 \| **J.B.** \| Visit 4 \| **30-Jul-2025** \| 107 \| 94 \| 92 \| 37.4
> \#300S0001 \| **J-B** \| Visit 5 \| **08/27/2025** \| 132 \| 81 \| 58 \| 36.4
> 3005-0002 \| **S.H.** \| Visit 2 \| **06-May-2025** \| 113 \| 77 \| 59 \| 37.5
> Subj 3005-0002 \| **S-H** \| Visit 3 \| **2025-05-20** \| 111 \| 67 \| 98 \| 37.2
> Subj 3005-0002 \| **S-H** \| Visit 4 \| **06/18/2025** \| 118 \| 79 \| 81 \| 37.2
> 3005-0002 \| **S-H** \| Visit 5 \| **13JUL2025** \| 109 \| 78 \| 61 \| 37.6
> 3005-0003 \| **S.S.** \| Visit 2 \| **23-Sep-2025** \| 127 \| 96 \| 62 \| 36.9
> Subj 3005-0003 \| **S.S.** \| Visit 3 \| **10/06/2025** \| 162 \| 91 \| 63 \| 37.7
> \#30050003 \| **SS** \| Visit 4 \| **November 6, 2025** \| 164 \| 62 \| 58 \| 37.5
> \#30050003 \| **SXS** \| Visit S \| **04DECZ025** \| 111 \| 85 \| 65 \| 37.2
> Subj 3005-0004 \| **E-W** \| Visit Z \| **2025-08-18** \| 126 \| 81 \| 64 \| 37.0
> \#30050004 \| **E.W.** \| Visit 3 \| **August 28, 2025** \| 135 \| 72 \| 60 \| 37.5
> Subj 3005-0004 \| **EXW** \| Visit 4 \| **09/28/2025** \| 143 \| 98 \| 89 \| 37.2
> 3005-0004 \| **E-W** \| Viit 5 \| **25OCT2O25** \| 124 \| 72 \| 80 \| 37.7
> Subj 3005-0005 \| **LXK** \| Visit 2 \| **June 10, 2025** \| 112 \| 83 \| 88 \| 36.8
> Subj 3005-0005 \| **LXK** \| Visit 3 \| **June 25, 20Z5** \| 152 \| 97 \| 67 \| 37.1
> Subj 3005-0005 \| **L-K** \| Visit 4 \| **25-Jul-2025** \| 155 \| 62 \| 93 \| 37.1
> 3005-0005 \| **L-K** \| Visit 5 \| **08/22/2025** \| 146 \| 70 \| 72 \| 37.2
> Subj 3005-0006 \| **G.P.** \| Visit 2 \| **24-Jul-2025** \| 134 \| 77 \| 86 \| 37.0
> Subj 3005-0006 \| **GXP** \| Visit 3 \| **August 11, 2025** \| 158 \| 65 \| 58 \| 37.7
> \#30050006 \| **GXP** \| Visit 4 \| **09/06/2025** \| 106 \| 76 \| 77 \| 36.9
> 3005-0006 \| **G-P** \| Visit 5 \| **04OCT2025** \| 158 \| 85 \| 78 \| 36.7
> 3005-0007 \| **E-M** \| Visit 2 \| **2025-05-19** \| 118 \| 74 \| 82 \| 37.7
> 3005-0007 \| **EXM** \| Visit 3 \| **June 2, 2025** \| 111 \| 74 \| 82 \| 37.7
> \#30050007 \| **EM** \| Visit 4 \| **30JUN20Z5** \| 143 \| 67 \| 92 \| 37.3
> \#30050007 \| **E-M** \| Visit 5 \| **27JUL2025** \| 110 \| 80 \| 94 \| 36.3
> Subj 3005-0008 \| **S-K** \| Visit 3 \| **2025-08-03** \| 134 \| 86 \| 78 \| 36.5
> 3005-0008 \| **SXK** \| Visit 4 \| **2025-09-01** \| 121 \| 71 \| 67 \| 37.0
> \#30050008 \| **SXK** \| Visit 5 \| **01-Oct-2025** \| 161 \| 68 \| 83 \| 36.7
> Subj 3005-0009 \| **D.E.** \| Visit 2 \| **May 2, 2025** \| 125 \| 81 \| 90 \| 36.3
> 3005-0009 \| **DE** \| Visit 4 \| **06/14/2025** \| 153 \| 62 \| 86 \| 37.6
> \#30050010 \| **PR** \| Visit 2 \| **27APR2025** \| 153 \| 92 \| 88 \| 37.7
> Subj 3005-0010 \| **P.R.** \| Visit 3 \| **13-May-2025** \| 112 \| 76 \| 98 \| 36.7
> \#30050010 \| **P-R** \| Visit 4 \| **11JUN2025** \| 106 \| 79 \| 95 \| 37.4
> \#30050011 \| **D.R.** \| Visit 2 \| **22MAR2025** \| 120 \| 69 \| 68 \| 36.4
> Subj 3005-0011 \| **DR** \| Visit 3 \| **03-Apr-2025** \| 136 \| 94 \| 74 \| 36.7
> Subj 3005-0011 \| **D.R.** \| Visit 4 \| **2025-04-30** \| 162 \| 66 \| 81 \| 36.7
> \#30050011 \| **D-R** \| Visit 5 \| **31MAY2025** \| 149 \| 83 \| 58 \| 37.5
> 300S-0012 \| **JXG** \| Visit 2 \| **02/24/2025** \| 136 \| 71 \| 65 \| 36.2
> Subj 3005-0012 \| **JG** \| Visit 3 \| **March 6, 2025** \| 156 \| 63 \| 62 \| 36.2
> \#30050012 \| **J-G** \| Visit 4 \| **05-Apr-2025** \| 161 \| 86 \| 86 \| 36.8
> \#3005001Z \| **JXG** \| Visit 5 \| **01-May-2025** \| 116 \| 98 \| 93 \| 37.0
> Subj 3005-0013 \| **S-E** \| Viit 2 \| **July 23, 2025** \| 147 \| 87 \| 63 \| 37.8
> Subj 3005-0013 \| **S-E** \| Visit 3 \| **04AUG2025** \| 139 \| 78 \| 66 \| 37.2
> 3005-0013 \| **S.E.** \| Visit 5 \| **09/30/2025** \| 123 \| 82 \| 84 \| 36.9
> \#30050014 \| **SXG** \| Visit 2 \| **February 9, 2025** \| 144 \| 68 \| 89 \| 37.0
> \#30050014 \| **S.G.** \| Visit 3 \| **21-Feb-2025** \| 147 \| 69 \| 81 \| 36.4
> 3005-0014 \| **SG** \| Visit 4 \| **22MAR2025** \| 125 \| 93 \| 69 \| 36.1
> \#30050014 \| **SG** \| Visit 5 \| **18APR2025** \| 138 \| 77 \| 59 \| 37.6
> Subj 3005-0015 \| **D.M.** \| Visit 2 \| **09-May-2025** \| 151 \| 96 \| 69 \| 37.3
> \#30050015 \| **DXM** \| Visit 3 \| **May 25, 2O25** \| 132 \| 84 \| 78 \| 37.3
> 3005-0O15 \| **D.M.** \| Visit 4 \| **June 20, 2025** \| 107 \| 62 \| 55 \| 37.1
> 
> Measurements taken seated after 5 minutes of rest. Repeat any systolic value above 16O mmHg within 15 minutes.
> Entered by: **AXW**
> Source verified against medical record (source on file) for subject 3005-0001.
> 
> Events are coded to MedDRA preferred term 10586823; the target dose is 150 mg. Agreement between central and local readigs is shown in Bland-Altman plots. Secondary endpoints are compard with the Wilcoxon test with Bonferroni correction; sparse tables use Fisher's exact test.
> 
> Database Procedures
> Access to the database is restricted to authorised personnel with role-based permissions. Edit checks identify missing, inconsistent or out-of-range values during cleaning. Reconciliation of safety data with the clinical database is performed periodically. Edit checks identify missing, inconsistent or out-of-range values during cleaning. Access to the database is restricted to authorised personnel with role-based permissions.
> 
> Data are entered into a validated c1inical database with an audit trail. Edit checks identify missing, inconsistent or out-of-range vlues at entry. Medical history and adverse evets are coded with a standard dictionary before database lock. Medical history and adverse events are coded with standard terminology before database lock.
> 
> Source Data Verification
> Queries are raised in the data capture system and resolved by site staff within ten working days. Protocol deviations are classified as minor or major. The investigator site file is reviewed for completeness at each visit. Source data verification prioritises eligibility, informed consent, primary endpoints and serious aderse events. Queries are raised in the data capture system and answered by the site within ten working days.
> 
> Protocol deviations are assessed for impact on participant safety and data integrity. The investigator site file is reviewed for currency of essential documents at each visit. Protocol deviations are classified as minor or majr.
> 
> On-site and remote monitoring visits are scheduled based on enrollment and risk indicators. The investigator site file is reviewed for completeness at each visit. Findings are documented in the visit report and followed up until closure.
> 
> Analysis Methods
> Sensitivity analyses assess the robustness of the primary result to protocol deviations. All tests are two-sided with a significance level of 5 percent unless otherwise specified. Subgroup analyses by geograhic region are exploratory and not adjusted for multiplicity.
> 
> Subgroup analyses by age group are descriptive and not adjusted for multiplicity. All tests are two-sided with a significance level of 5 pecnt unless otherwise spcified. Continuous variables are summaised with the nmber of observations, mean, standard deviation, median and range. Sensitivity analyses assess the robstness of the primary result to alternative assumptions. The statistical analyss plan is finalised befre database lock and specifies all derived variab1es.
> 
> Categorical vriables are presented as counts and percentages within each treatment group. Subgroup analyses by baseline severity are descriptive and not adjusted for multiplicity. Categorical variables are presented as counts and percentages of the analysis set.
> 
> Page 1
> 
> Fenwick Therapeutics \| Protocol FTX-5142-018 \| Confidential
> 
> Categorical variables are presented as counts and percentages of the analysis set. All tests are two-sided with a significance level of 2.5 percent unless otherwise specified. Sensitivity aalses asess the robustness of the primary resu1t to alternative assumptions. Continuous variables are summarised wih the number of observations, mean, standard deviation, median and range. All tests are two-sided with a significance level of 5 percent unless otherwise specified. Categorical variables are presented as counts and percentages of the analysis set.
> 
> Drug Accountabiliy
> Investigational product is stored in a secure, temperature-monitored area with access limited to authorised staff. Dispensing and returns are recorded on the accountability log at every dispensing visit. Temperature excursions must be reported to the sponsor before further use of the affected supply. Unused product is returned to the sponsor after reconciliation. Dispensing and returns are recorded on the accountability log at every dispensing visit. Unused product is destroyed according to local procedures after reconciliation.
> 
> Investigtional product is stored in a secure, temperature-monitored area with access limited to authorised staff. Temperature excursions must be reported to the sponsor immediately. Temperature excursions are reported to the sponsor immediately. Temperature excursions must be reported to the sponsor before further use of the affected suply.
> 
> Tablet counts are reconciled against the dosing dary to assess compliance. Tablet counts are reconciled against the dosing diary to assss compliance. Dispensing and returns are recorded on the accountability log at every dispensing visit. Temperature excursons are reported to the sponsor immediately. Investigational product is stored in a secure, temerature-monitored area with access limited to authorised staff.
> 
> Reporting of Safety Events
> The investigator assesses intensity using the common terminology citeria and documents the assessment in te source record. Pregnancy in a participant is reported using the pregnancy notification form within 24 hours. Pregnancy in a participant is reported using the pregnancy notification form within one working day. The responsible physician assesses intensity using the common terminology criteria and documents the assessment in the source record. The resonsible physician assesses intensity using the common terminology criteria and documets the assessment in the source record.
> 
> Pregnancy in a participant is reported using the pregnancy notification form withn 24 hours. Evets that start after the first dose and until 28 days after the last dose are considered treatment-emergent. Follow-up information is provided until the event stabilises or the participant is lost to follow-up. Events that begin after the first dose and up to 28 days after the last dose are summarised as treatment-emergent. Non-serious adverse events are recorded in the case report form throughout the treatment period.
> 
> Any serious adverse events are reported to the sponsor within 24 hours of the site becoming aware of the event. All serios adverse events must be reported to the sponsor within 48 hours of the investigator becoming aware of the event. Non-serious adverse events are recored in te case reprt form throughout the treatment period.
> 
> Page 2
> 

**d0447:doc:8192:0** route forward (p_below_t_low); p(pii) raw 0.2966, calibrated 0.4300; gold role both, category direct; missed address, dob, event_date, initials, mrn, person_name, zip

> Fenwick Therapeutics \| Prüfplan FTX-5142-018 \| Vertraulich
> 
> Patientennarrativ: Prüfungsteilnehmer Subj 3005-0010
> Prüfplan FTX-5142-018, Prüfzentrum 3005
> 
> Demografie und Ausgangsbefund
> **P. Rohleder** (**P-R**), 75 Jahre, geb. **18. Juli 1949**, Patientennummer **70322471**, wurde am **15. April 2025** randomisiert (Randomisierungsnummer R-65247) und erhielt am selben Tag die erste Dosis FTX-5142. Wohnort: **Baumring 1-8, Niederheide** **30576**.
> Die Begleitmedikation wurde von **SCHMIDTKE, Dieter** überprüft.
> 
> Unerwünschtes Ereignis
> Während der Behandlungsphase wurden keine unerwünschten Ereignisse gemeldet.
> 
> Ereigniszeitanalysen verwenden die Kaplan-Meier-Methode; die Kreatinin-Clearance wird nach Cockcroft-Gault berechnet. Prüfpräparat FTX-5142, Charge LT-255487-A, wurde aus Kit K-954687 im Visitenfenster Day 29 ±3 ausgegeben. Prüfplan FTX-5142-018 (NCT99608180; EudraCT 2031-854061-77), Amendment A5, gültig ab 2025-04-03.
> 
> Verlauf
> Die Teilnahme wurde gemäß Prüfplan fortgesetzt.
> 
> Seite 1
> 

### B4 / qs_v2 (doc-level, underpowered), holdout: 0 false forward(s)

## 9. Caveats

- A / qs_v1: D-008 review: test recall 1.0000 minus its exact 95% lower bound 0.9747 = 0.0253 > 0.01 (144 positives).
- A / qs_v1: Batch-1 latency per token drifted to 1.48x its start by the end of the run at similar unit lengths (e.g. MPS allocator growth; the runner releases it between calls since 8e004bb): treat batch-1 p50/p95 as upper bounds.
- A / qs_v1: test: slices with n < 30: doc_type=icf_signature_page (n=28), lang=de (n=7), lang=es (n=12), lang=pl (n=12), split_span=yes (n=7)
- A / qs_v1: holdout: slices with n < 30: pre_redacted=yes (n=12)
- A / qs_v2: D-008 review: test recall 1.0000 minus its exact 95% lower bound 0.9747 = 0.0253 > 0.01 (144 positives).
- A / qs_v2: Batch-1 latency per token drifted to 1.38x its start by the end of the run at similar unit lengths (e.g. MPS allocator growth; the runner releases it between calls since 8e004bb): treat batch-1 p50/p95 as upper bounds.
- A / qs_v2: test: slices with n < 30: doc_type=icf_signature_page (n=28), lang=de (n=7), lang=es (n=12), lang=pl (n=12), split_span=yes (n=7)
- A / qs_v2: holdout: slices with n < 30: pre_redacted=yes (n=12)
- B1 / qs_v1: test: slices with n < 30: doc_type=delegation_log (n=15), doc_type=icf_signature_page (n=10), doc_type=lab_report (n=27), lang=de (n=4), lang=es (n=7), lang=pl (n=6), pii_depth=late (n=19), pii_depth=middle (n=20), split_span=yes (n=4)
- B1 / qs_v1: holdout: slices with n < 30: hard_negative=yes (n=21), length_bucket=short (n=17), perturbation=line_wrap (n=26), perturbation=ocr_noise (n=12), pre_redacted=yes (n=4)
- B1 / qs_v2: test: slices with n < 30: doc_type=delegation_log (n=15), doc_type=icf_signature_page (n=10), doc_type=lab_report (n=27), lang=de (n=4), lang=es (n=7), lang=pl (n=6), pii_depth=late (n=19), pii_depth=middle (n=20), split_span=yes (n=4)
- B1 / qs_v2: holdout: slices with n < 30: hard_negative=yes (n=21), length_bucket=short (n=17), perturbation=line_wrap (n=26), perturbation=ocr_noise (n=12), pre_redacted=yes (n=4)
- B2 / qs_v1: test: slices with n < 30: doc_type=conmed_log (n=17), doc_type=crf_page (n=23), doc_type=delegation_log (n=8), doc_type=deviation_log (n=18), doc_type=icf_signature_page (n=7), doc_type=lab_report (n=15), doc_type=sae_cioms (n=18), lang=de (n=4), lang=es (n=7), lang=pl (n=6), pii_depth=late (n=8), pii_depth=middle (n=9), pre_redacted=yes (n=29), truncated=yes (n=6)
- B2 / qs_v1: holdout: slices with n < 30: hard_negative=yes (n=11), length_bucket=short (n=11), perturbation=headers_footers (n=21), perturbation=line_wrap (n=14), perturbation=none (n=17), perturbation=ocr_noise (n=7), pre_redacted=yes (n=2)
- B2 / qs_v2: test: slices with n < 30: doc_type=conmed_log (n=17), doc_type=crf_page (n=23), doc_type=delegation_log (n=8), doc_type=deviation_log (n=18), doc_type=icf_signature_page (n=7), doc_type=lab_report (n=15), doc_type=sae_cioms (n=18), lang=de (n=4), lang=es (n=7), lang=pl (n=6), pii_depth=late (n=8), pii_depth=middle (n=9), pre_redacted=yes (n=29), truncated=yes (n=6)
- B2 / qs_v2: holdout: slices with n < 30: hard_negative=yes (n=11), length_bucket=short (n=11), perturbation=headers_footers (n=21), perturbation=line_wrap (n=14), perturbation=none (n=17), perturbation=ocr_noise (n=7), pre_redacted=yes (n=2)
- B3 / qs_v1 (doc-level, underpowered): Doc-level arm: underpowered (D-008 amended); 124 test documents, few units each, so recall intervals are wide.
- B3 / qs_v1 (doc-level, underpowered): test: slices with n < 30: doc_type=conmed_log (n=10), doc_type=crf_page (n=16), doc_type=csr_patient_narrative (n=25), doc_type=delegation_log (n=5), doc_type=deviation_log (n=11), doc_type=icf_signature_page (n=7), doc_type=lab_report (n=11), doc_type=monitoring_visit_report (n=25), doc_type=sae_cioms (n=14), doc_type=site_correspondence (n=29), lang=de (n=4), lang=es (n=7), lang=pl (n=6), perturbation=email_quoting (n=29), perturbation=ocr_noise (n=20), perturbation=table (n=29), pii_depth=early (n=19), pii_depth=late (n=5), pii_depth=middle (n=5), pre_redacted=yes (n=18)
- B3 / qs_v1 (doc-level, underpowered): holdout: slices with n < 30: hard_negative=no (n=24), hard_negative=yes (n=7), length_bucket=medium (n=20), length_bucket=short (n=11), perturbation=headers_footers (n=13), perturbation=line_wrap (n=9), perturbation=none (n=10), perturbation=ocr_noise (n=4), pre_redacted=yes (n=1)
- B3 / qs_v2 (doc-level, underpowered): Doc-level arm: underpowered (D-008 amended); 124 test documents, few units each, so recall intervals are wide.
- B3 / qs_v2 (doc-level, underpowered): test: slices with n < 30: doc_type=conmed_log (n=10), doc_type=crf_page (n=16), doc_type=csr_patient_narrative (n=25), doc_type=delegation_log (n=5), doc_type=deviation_log (n=11), doc_type=icf_signature_page (n=7), doc_type=lab_report (n=11), doc_type=monitoring_visit_report (n=25), doc_type=sae_cioms (n=14), doc_type=site_correspondence (n=29), lang=de (n=4), lang=es (n=7), lang=pl (n=6), perturbation=email_quoting (n=29), perturbation=ocr_noise (n=20), perturbation=table (n=29), pii_depth=early (n=19), pii_depth=late (n=5), pii_depth=middle (n=5), pre_redacted=yes (n=18)
- B3 / qs_v2 (doc-level, underpowered): holdout: slices with n < 30: hard_negative=no (n=24), hard_negative=yes (n=7), length_bucket=medium (n=20), length_bucket=short (n=11), perturbation=headers_footers (n=13), perturbation=line_wrap (n=9), perturbation=none (n=10), perturbation=ocr_noise (n=4), pre_redacted=yes (n=1)
- B4 / qs_v1 (doc-level, underpowered): Doc-level arm: underpowered (D-008 amended); 124 test documents, few units each, so recall intervals are wide.
- B4 / qs_v1 (doc-level, underpowered): Batch-1 latency per token drifted to 1.31x its start by the end of the run at similar unit lengths (e.g. MPS allocator growth; the runner releases it between calls since 8e004bb): treat batch-1 p50/p95 as upper bounds.
- B4 / qs_v1 (doc-level, underpowered): test: slices with n < 30: doc_type=conmed_log (n=8), doc_type=crf_page (n=14), doc_type=csr_patient_narrative (n=14), doc_type=delegation_log (n=5), doc_type=deviation_log (n=10), doc_type=icf_signature_page (n=7), doc_type=lab_report (n=11), doc_type=monitoring_visit_report (n=11), doc_type=protocol_section (n=16), doc_type=sae_cioms (n=14), doc_type=site_correspondence (n=14), lang=de (n=4), lang=es (n=7), lang=pl (n=6), length_bucket=long (n=24), length_bucket=xl (n=13), perturbation=email_quoting (n=14), perturbation=ocr_noise (n=14), perturbation=table (n=27), pii_depth=early (n=7), pii_depth=late (n=2), pii_depth=middle (n=2), pre_redacted=yes (n=15), truncated=yes (n=13)
- B4 / qs_v1 (doc-level, underpowered): holdout: slices with n < 30: hard_negative=no (n=23), hard_negative=yes (n=7), length_bucket=medium (n=19), length_bucket=short (n=11), perturbation=headers_footers (n=12), perturbation=line_wrap (n=9), perturbation=none (n=10), perturbation=ocr_noise (n=4), pre_redacted=no (n=29), pre_redacted=yes (n=1)
- B4 / qs_v2 (doc-level, underpowered): Doc-level arm: underpowered (D-008 amended); 124 test documents, few units each, so recall intervals are wide.
- B4 / qs_v2 (doc-level, underpowered): Batch-1 latency per token drifted to 1.56x its start by the end of the run at similar unit lengths (e.g. MPS allocator growth; the runner releases it between calls since 8e004bb): treat batch-1 p50/p95 as upper bounds.
- B4 / qs_v2 (doc-level, underpowered): test: slices with n < 30: doc_type=conmed_log (n=8), doc_type=crf_page (n=14), doc_type=csr_patient_narrative (n=14), doc_type=delegation_log (n=5), doc_type=deviation_log (n=10), doc_type=icf_signature_page (n=7), doc_type=lab_report (n=11), doc_type=monitoring_visit_report (n=11), doc_type=protocol_section (n=16), doc_type=sae_cioms (n=14), doc_type=site_correspondence (n=14), lang=de (n=4), lang=es (n=7), lang=pl (n=6), length_bucket=long (n=24), length_bucket=xl (n=13), perturbation=email_quoting (n=14), perturbation=ocr_noise (n=14), perturbation=table (n=27), pii_depth=early (n=7), pii_depth=late (n=2), pii_depth=middle (n=2), pre_redacted=yes (n=15), truncated=yes (n=13)
- B4 / qs_v2 (doc-level, underpowered): holdout: slices with n < 30: hard_negative=no (n=23), hard_negative=yes (n=7), length_bucket=medium (n=19), length_bucket=short (n=11), perturbation=headers_footers (n=12), perturbation=line_wrap (n=9), perturbation=none (n=10), perturbation=ocr_noise (n=4), pre_redacted=no (n=29), pre_redacted=yes (n=1)
