# laya-pii-bench report

## 1. Run context

### A / qs_v1

| field | value |
|---|---|
| arm | A |
| question set | qs_v1 |
| splits | test, holdout |
| docs sha256 | `55dbb36fe63f9c1b1d0cb485d6d63382e72cf168bd2fded2ee590dc1bad3bf05` |
| units sha256 | `34448a266437afdb7ff011330c0c6d583cc947c22ac0bf6e5c48f10a8a1bea37` |
| decisions sha256 | `93756859affdf29422d744413a7faabc4a00fb97ef51d23d16752182b791cfdf` |
| calib hash / fit_on | `288ba59c38d2f84f` / calib |
| calib commit (D-019) | `047aad790893` 2026-10-02T00:11:35-04:00 |
| temperature fallbacks (T = 1) | doc_kind:4: fit hit bound (20) |
| hardware | Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB, cuda, Linux 6.12.90+ |
| laya version | 0.3.20 |
| checkpoints | english |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-10-02T04:34:29.931771+00:00 |

### A / qs_v2

| field | value |
|---|---|
| arm | A |
| question set | qs_v2 |
| splits | test, holdout |
| docs sha256 | `55dbb36fe63f9c1b1d0cb485d6d63382e72cf168bd2fded2ee590dc1bad3bf05` |
| units sha256 | `34448a266437afdb7ff011330c0c6d583cc947c22ac0bf6e5c48f10a8a1bea37` |
| decisions sha256 | `f666240f2691f715589da214343636860fffd06fd8d26913eb93c06f77a8c096` |
| calib hash / fit_on | `3b308aff6a979319` / calib |
| calib commit (D-019) | `047aad790893` 2026-10-02T00:11:35-04:00 |
| temperature fallbacks (T = 1) | has_staff_pii:2: fit hit bound (20) |
| hardware | Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB, cuda, Linux 6.12.90+ |
| laya version | 0.3.20 |
| checkpoints | english |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-10-02T04:34:36.450678+00:00 |

### B1 / qs_v1

| field | value |
|---|---|
| arm | B1 |
| question set | qs_v1 |
| splits | test, holdout |
| docs sha256 | `55dbb36fe63f9c1b1d0cb485d6d63382e72cf168bd2fded2ee590dc1bad3bf05` |
| units sha256 | `bac3fbb8d1079e1953d43e2fccde3ad5ddf3d94db2ec21cda91c0485940227ba` |
| decisions sha256 | `9cac04e2ab4070bc96c80750648a325b0be9f47555f942db99fc49eb664aa265` |
| calib hash / fit_on | `79416e04b4d54010` / calib |
| calib commit (D-019) | `047aad790893` 2026-10-02T00:11:35-04:00 |
| temperature fallbacks (T = 1) | doc_kind:4: fit hit bound (20); pii_present:2: fit hit bound (20); subject_role:4: fit hit bound (20) |
| hardware | Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB, cuda, Linux 6.12.90+ |
| laya version | 0.3.20 |
| checkpoints | multilingual |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-10-02T04:34:39.323548+00:00 |

### B1 / qs_v2

| field | value |
|---|---|
| arm | B1 |
| question set | qs_v2 |
| splits | test, holdout |
| docs sha256 | `55dbb36fe63f9c1b1d0cb485d6d63382e72cf168bd2fded2ee590dc1bad3bf05` |
| units sha256 | `bac3fbb8d1079e1953d43e2fccde3ad5ddf3d94db2ec21cda91c0485940227ba` |
| decisions sha256 | `e9b31c2f45224c4b9eaaab265f75b761088f4a537e9840c1bd5f9a09169f2932` |
| calib hash / fit_on | `a5c68d1191d886a2` / calib |
| calib commit (D-019) | `047aad790893` 2026-10-02T00:11:35-04:00 |
| temperature fallbacks (T = 1) | has_coded_id:2: fit hit bound (20); has_phi_direct:2: fit hit bound (20); has_phi_quasi:2: fit hit bound (20); has_staff_pii:2: fit hit bound (20); pii_present:2: fit hit bound (20) |
| hardware | Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB, cuda, Linux 6.12.90+ |
| laya version | 0.3.20 |
| checkpoints | multilingual |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-10-02T04:34:41.819291+00:00 |

### B2 / qs_v1

| field | value |
|---|---|
| arm | B2 |
| question set | qs_v1 |
| splits | test, holdout |
| docs sha256 | `55dbb36fe63f9c1b1d0cb485d6d63382e72cf168bd2fded2ee590dc1bad3bf05` |
| units sha256 | `2b48e5b58cc96f2c81ee8b65163a6ab1c2ba4d5872716db81569cdb7bca67de6` |
| decisions sha256 | `cd404d84282e80ba643429af1236f60f22fdbe9f0e4fa3daadee21126f8bb7c6` |
| calib hash / fit_on | `86626c80002d062d` / calib |
| calib commit (D-019) | `047aad790893` 2026-10-02T00:11:35-04:00 |
| temperature fallbacks (T = 1) | doc_kind:4: fit hit bound (20); pii_present:2: fit hit bound (20); subject_role:4: fit hit bound (20) |
| hardware | Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB, cuda, Linux 6.12.90+ |
| laya version | 0.3.20 |
| checkpoints | multilingual |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-10-02T04:34:43.499065+00:00 |

### B2 / qs_v2

| field | value |
|---|---|
| arm | B2 |
| question set | qs_v2 |
| splits | test, holdout |
| docs sha256 | `55dbb36fe63f9c1b1d0cb485d6d63382e72cf168bd2fded2ee590dc1bad3bf05` |
| units sha256 | `2b48e5b58cc96f2c81ee8b65163a6ab1c2ba4d5872716db81569cdb7bca67de6` |
| decisions sha256 | `b5dfbd58cf7f722e2f9d3e4b06608b7ccec152abd2b475f7144accd29cec93a4` |
| calib hash / fit_on | `c871b4224f7c0eca` / calib |
| calib commit (D-019) | `047aad790893` 2026-10-02T00:11:35-04:00 |
| temperature fallbacks (T = 1) | has_coded_id:2: fit hit bound (20); has_phi_direct:2: fit hit bound (20); has_phi_quasi:2: fit hit bound (20); has_staff_pii:2: fit hit bound (20); pii_present:2: fit hit bound (20) |
| hardware | Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB, cuda, Linux 6.12.90+ |
| laya version | 0.3.20 |
| checkpoints | multilingual |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-10-02T04:34:45.153146+00:00 |

### B3 / qs_v1 (doc-level, underpowered)

| field | value |
|---|---|
| arm | B3 |
| question set | qs_v1 |
| splits | test, holdout |
| docs sha256 | `55dbb36fe63f9c1b1d0cb485d6d63382e72cf168bd2fded2ee590dc1bad3bf05` |
| units sha256 | `3171cc64cfe0d6e63c0b4ddeb6ac608cf66fce2ba97dcbbeed0ea7b62486ed5b` |
| decisions sha256 | `d6092a9f308cf8a1b3ff550e793de48be3e178d20067bf7ebe6c662576cf4767` |
| calib hash / fit_on | `53d8a53f43d9dd38` / calib |
| calib commit (D-019) | `047aad790893` 2026-10-02T00:11:35-04:00 |
| temperature fallbacks (T = 1) | doc_kind:4: fit hit bound (20); pii_present:2: fit hit bound (20); subject_role:4: fit hit bound (20) |
| hardware | Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB, cuda, Linux 6.12.90+ |
| laya version | 0.3.20 |
| checkpoints | multilingual |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-10-02T04:34:46.552396+00:00 |

### B3 / qs_v2 (doc-level, underpowered)

| field | value |
|---|---|
| arm | B3 |
| question set | qs_v2 |
| splits | test, holdout |
| docs sha256 | `55dbb36fe63f9c1b1d0cb485d6d63382e72cf168bd2fded2ee590dc1bad3bf05` |
| units sha256 | `3171cc64cfe0d6e63c0b4ddeb6ac608cf66fce2ba97dcbbeed0ea7b62486ed5b` |
| decisions sha256 | `28baf7740926bd85a2227ea03311d6bc9caea96b463b765b015fe0bc9c083b57` |
| calib hash / fit_on | `3b72ba16f52793d2` / calib |
| calib commit (D-019) | `047aad790893` 2026-10-02T00:11:35-04:00 |
| temperature fallbacks (T = 1) | has_coded_id:2: fit hit bound (20); has_phi_direct:2: fit hit bound (20); has_phi_quasi:2: fit hit bound (20); has_staff_pii:2: fit hit bound (20); pii_present:2: fit hit bound (20) |
| hardware | Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB, cuda, Linux 6.12.90+ |
| laya version | 0.3.20 |
| checkpoints | multilingual |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-10-02T04:34:47.930841+00:00 |

### B4 / qs_v1 (doc-level, underpowered)

| field | value |
|---|---|
| arm | B4 |
| question set | qs_v1 |
| splits | test, holdout |
| docs sha256 | `55dbb36fe63f9c1b1d0cb485d6d63382e72cf168bd2fded2ee590dc1bad3bf05` |
| units sha256 | `0bacb96a3e0c5e7e4e55e2b671c85df92e31d0919b861bfc9a386703c214e1a0` |
| decisions sha256 | `2aacf6ae0291b66a4a859f5e77ab4f240da4ca8e83364171ba0a2ad385a488a5` |
| calib hash / fit_on | `568089575b3bafa3` / calib |
| calib commit (D-019) | `047aad790893` 2026-10-02T00:11:35-04:00 |
| temperature fallbacks (T = 1) | doc_kind:4: fit hit bound (20) |
| hardware | Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB, cuda, Linux 6.12.90+ |
| laya version | 0.3.20 |
| checkpoints | multilingual |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-10-02T04:34:49.165733+00:00 |

### B4 / qs_v2 (doc-level, underpowered)

| field | value |
|---|---|
| arm | B4 |
| question set | qs_v2 |
| splits | test, holdout |
| docs sha256 | `55dbb36fe63f9c1b1d0cb485d6d63382e72cf168bd2fded2ee590dc1bad3bf05` |
| units sha256 | `0bacb96a3e0c5e7e4e55e2b671c85df92e31d0919b861bfc9a386703c214e1a0` |
| decisions sha256 | `5ac550431a8859bca8e4215d56ccfdc1a75113632929dab5444dc401a2c6e01d` |
| calib hash / fit_on | `f942cfef8068f118` / calib |
| calib commit (D-019) | `047aad790893` 2026-10-02T00:11:35-04:00 |
| temperature fallbacks (T = 1) | has_coded_id:2: fit hit bound (20); has_phi_direct:2: fit hit bound (20); has_staff_pii:2: fit hit bound (20) |
| hardware | Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB, cuda, Linux 6.12.90+ |
| laya version | 0.3.20 |
| checkpoints | multilingual |
| checkpoint revisions | 55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851 |
| date | 2026-10-02T04:34:50.370088+00:00 |

### C / qs_v1

| field | value |
|---|---|
| arm | C |
| question set | qs_v1 |
| splits | test, holdout |
| docs sha256 | `55dbb36fe63f9c1b1d0cb485d6d63382e72cf168bd2fded2ee590dc1bad3bf05` |
| units sha256 | `22fa9af3b4ac6fd43a9c18e06e13732fefa629902caa8facc3e885f84219e604` |
| decisions sha256 | `609cb5644398aeb8a7f6be7ef1982678254793f42455eeea9c74f2e225d669c3` |
| calib hash / fit_on | `c8bdfb9f3c48d975` / calib |
| calib commit (D-019) | `047aad790893` 2026-10-02T00:11:35-04:00 |
| temperature fallbacks (T = 1) | none |
| hardware | Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB, cuda, Linux 6.12.90+ |
| laya version | 0.3.20 |
| checkpoints | finetuned_english |
| checkpoint revisions | 6809676153aa2bb747a0054ed30835e45b3d8e976cdfe31fa956185e9aee661c |
| date | 2026-10-02T04:34:55.632837+00:00 |

### C / qs_v2

| field | value |
|---|---|
| arm | C |
| question set | qs_v2 |
| splits | test, holdout |
| docs sha256 | `55dbb36fe63f9c1b1d0cb485d6d63382e72cf168bd2fded2ee590dc1bad3bf05` |
| units sha256 | `22fa9af3b4ac6fd43a9c18e06e13732fefa629902caa8facc3e885f84219e604` |
| decisions sha256 | `c967f19a8d25baecd4e8088f8a462069f3cc8fb7d83807ef04c17af0e761b96f` |
| calib hash / fit_on | `5cbb5b26d7940c57` / calib |
| calib commit (D-019) | `047aad790893` 2026-10-02T00:11:35-04:00 |
| temperature fallbacks (T = 1) | none |
| hardware | Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB, cuda, Linux 6.12.90+ |
| laya version | 0.3.20 |
| checkpoints | finetuned_english |
| checkpoint revisions | 6809676153aa2bb747a0054ed30835e45b3d8e976cdfe31fa956185e9aee661c |
| date | 2026-10-02T04:35:00.706795+00:00 |

### LC / qs_v1

| field | value |
|---|---|
| arm | LC |
| question set | qs_v1 |
| splits | test, holdout |
| docs sha256 | `55dbb36fe63f9c1b1d0cb485d6d63382e72cf168bd2fded2ee590dc1bad3bf05` |
| units sha256 | `34448a266437afdb7ff011330c0c6d583cc947c22ac0bf6e5c48f10a8a1bea37` |
| decisions sha256 | `6e954c9233d6fdec4d897d12a5bacb4be17cbd3a88f837565a0aedf9946a4b2b` |
| calib hash / fit_on | `b1370c4efd20b125` / calib |
| calib commit (D-019) | `b9836b97914b` 2026-10-02T00:34:23-04:00 |
| temperature fallbacks (T = 1) | none |
| hardware | Apple M2, 8.0 GB, cpu, Darwin 24.3.0 |
| laya version | 0.3.20 |
| checkpoints | baseline-char |
| checkpoint revisions | char-tfidf-lr@2fdd6558eced |
| date | 2026-10-02T04:35:09.265661+00:00 |

### LW / qs_v1

| field | value |
|---|---|
| arm | LW |
| question set | qs_v1 |
| splits | test, holdout |
| docs sha256 | `55dbb36fe63f9c1b1d0cb485d6d63382e72cf168bd2fded2ee590dc1bad3bf05` |
| units sha256 | `34448a266437afdb7ff011330c0c6d583cc947c22ac0bf6e5c48f10a8a1bea37` |
| decisions sha256 | `d88b6ac265020ec731d2e0197077b02bfd0285df044db534594d95d6dc0774dc` |
| calib hash / fit_on | `1b886b103f8a4cff` / calib |
| calib commit (D-019) | `b9836b97914b` 2026-10-02T00:34:23-04:00 |
| temperature fallbacks (T = 1) | none |
| hardware | Apple M2, 8.0 GB, cpu, Darwin 24.3.0 |
| laya version | 0.3.20 |
| checkpoints | baseline-word |
| checkpoint revisions | word-tfidf-lr@2fdd6558eced |
| date | 2026-10-02T04:35:05.036085+00:00 |

## 2. Headline operating point

### Key findings

- **The recall-first operating point is nearly degenerate.** At the calib-fit `t_low`, 10 of 14 arm x question-set runs forward under 5% of test units (A / qs_v1 0.51%, A / qs_v2 0.53%, B1 / qs_v1 0.10%, B1 / qs_v2 0.26%, B2 / qs_v1 0.11%, B2 / qs_v2 0.11%, B3 / qs_v1 (doc-level, underpowered) 0.19%, B3 / qs_v2 (doc-level, underpowered) 0.19%, B4 / qs_v1 (doc-level, underpowered) 0.00%, B4 / qs_v2 (doc-level, underpowered) 0.00%). The trivial policy "escalate everything" has recall 1 and forward rate 0, so high recall here says little about work saved. With few calib positives the recall target means "no calib misses": `t_low` is the lowest-scoring calib positive, a single unit.
- **Some checkpoints barely rank PII.** Test AUROC of calibrated p(pii) below 0.6: B1 / qs_v1 0.399, B1 / qs_v2 0.399, B2 / qs_v1 0.436, B2 / qs_v2 0.436, B3 / qs_v1 (doc-level, underpowered) 0.456, B3 / qs_v2 (doc-level, underpowered) 0.456, B4 / qs_v1 (doc-level, underpowered) 0.466, B4 / qs_v2 (doc-level, underpowered) 0.466. Their high recall comes from answering "PII present" to almost everything, not from detection (option-swap probe: `reports/audits/M6_pii_question_probe-20260929.md`).
- **Trading recall for work saved (calib target 0.95):** A / qs_v1 forwards 5.9% at test recall 0.976 (10 false forwards), A / qs_v2 forwards 6.5% at test recall 0.971 (12 false forwards), B1 / qs_v1 forwards 1.2% at test recall 0.964 (11 false forwards), B1 / qs_v2 forwards 1.8% at test recall 0.951 (15 false forwards), B2 / qs_v1 forwards 2.3% at test recall 0.948 (12 false forwards), B2 / qs_v2 forwards 3.3% at test recall 0.923 (18 false forwards), B3 / qs_v1 (doc-level, underpowered) forwards 1.9% at test recall 0.965 (8 false forwards), B3 / qs_v2 (doc-level, underpowered) forwards 2.9% at test recall 0.948 (12 false forwards), B4 / qs_v1 (doc-level, underpowered) forwards 1.5% at test recall 0.981 (4 false forwards), B4 / qs_v2 (doc-level, underpowered) forwards 2.7% at test recall 0.967 (7 false forwards), C / qs_v1 forwards 92.8% at test recall 0.971 (12 false forwards), C / qs_v2 forwards 93.2% at test recall 0.931 (29 false forwards), LC / qs_v1 forwards 88.3% at test recall 0.950 (21 false forwards), LW / qs_v1 forwards 88.0% at test recall 0.938 (26 false forwards). See the curve table below.
- **Fine-tuning (arm C, qs_v1) raises test AUROC of p(pii) from 0.786 (zero-shot A) to 0.9999.** At the 0.995 calib target C forwards 92.6% of test units (A 0.5%). Route recall 0.9976: 1 of 419 PII units forwarded (exact 95% 0.9868 to 0.9999); the 0.995 target is not rejected, not demonstrated (D-008). C has no review band: `t_low` = `t_high` = 0.9697, so every unit is forwarded or redacted, and the operating point rests on the lowest-scoring calib positives (see the curve for stricter targets).
- **Fine-tuning (arm C, qs_v2) raises test AUROC of p(pii) from 0.786 (zero-shot A) to 0.9999.** At the 0.995 calib target C forwards 92.6% of test units (A 0.5%). Route recall 0.9952: 2 of 419 PII units forwarded (exact 95% 0.9829 to 0.9994); the 0.995 target is not rejected, not demonstrated (D-008). C has no review band: `t_low` = `t_high` = 0.9701, so every unit is forwarded or redacted, and the operating point rests on the lowest-scoring calib positives (see the curve for stricter targets).
- **Arm C is in-distribution evidence only.** It is trained and tested on the same synthetic generator (same templates, filler and Faker world; disjoint sites and persons). A bag-of-words classifier trained on the same units (char 2-5-gram TF-IDF + logistic regression, arm LC) reaches test AUROC 0.9864 and forwards 60.8% with 2 PII units forwarded at the same calib target, so most of the gain over zero-shot A reflects how learnable this corpus is, not general PII detection. C's margin over it is operational: at that target C forwards 92.6% of test units (1 PII units forwarded), so far fewer clean units go to review. C's advantage over the baseline is concentrated in hard negatives and name-only units, and C's misses are single quasi-identifiers embedded in boilerplate (strata in `reports/audits/M8_results_review.md`). These results do not transfer to real documents without an out-of-generator test.
- qs_v1 vs qs_v2 differences in the same arm are not a question-wording effect: pii_present has the same text in both; these runs ran on cuda; and only qs_v1 has the role rule.

### Arm comparison: A vs best B vs fine-tuned C (report v2)

Same test documents for every arm; A, C and the lexical baselines score identical units (same unit spec). Best B is chosen on the calibration split, never on test. The lexical baselines (M8 results review B1) are TF-IDF + logistic regression models trained on C's own training units, calibrated and scored like an arm (pii_present only, no role rule). Thresholds are fit on calibration at each recall target. Route recall = 1 - false forwards / PII units, with exact 95% bounds. M2 latency is the p50 of a timing-only run on a seeded sample of test units (D-022); accuracy runs ran on Kaggle T4 GPUs.

| qs | arm | route recall @ 99.5% target [exact 95%] | forwarded | negatives forwarded | false forwards | AUROC p(pii) | at 95% target | at 90% target | M2 p50 ms/unit |
|---|---|---|---|---|---|---|---|---|---|
| qs_v1 | A, zero-shot English | 1.0000 [0.9912, 1.0000] | 0.51% | 0.0055 | 0 | 0.7861 | 5.9% at recall 0.976 | 13.8% at recall 0.947 | not timed |
| qs_v1 | best B (B4), by calib AUROC 0.486 | 1.0000 [0.9830, 1.0000] | 0.00% | 0.0000 | 0 | 0.4662 | 1.5% at recall 0.981 | 4.5% at recall 0.944 | not timed |
| qs_v1 | LW, lexical baseline (word 1-2-gram) | 0.9976 [0.9868, 0.9999] | 51.18% | 0.5521 | 1 | 0.9848 | 88.0% at recall 0.938 | 89.6% at recall 0.883 | not timed |
| qs_v1 | LC, lexical baseline (char 2-5-gram) | 0.9952 [0.9829, 0.9994] | 60.79% | 0.6556 | 2 | 0.9864 | 88.3% at recall 0.950 | 90.6% at recall 0.876 | not timed |
| qs_v1 | C, fine-tuned English | 0.9976 [0.9868, 0.9999] | 92.58% | 0.9989 | 1 | 0.9999 | 92.8% at recall 0.971 | 92.8% at recall 0.969 | not timed |
| qs_v2 | A, zero-shot English | 1.0000 [0.9912, 1.0000] | 0.53% | 0.0057 | 0 | 0.7861 | 6.5% at recall 0.971 | 14.7% at recall 0.933 | not timed |
| qs_v2 | best B (B4), by calib AUROC 0.486 | 1.0000 [0.9830, 1.0000] | 0.00% | 0.0000 | 0 | 0.4662 | 2.7% at recall 0.967 | 7.7% at recall 0.912 | not timed |
| qs_v2 | C, fine-tuned English | 0.9952 [0.9829, 0.9994] | 92.63% | 0.9992 | 2 | 0.9999 | 93.2% at recall 0.931 | 93.3% at recall 0.912 | not timed |


### Test (headline)

pii_present recall at the calib-fit `t_low` (95% document-level bootstrap CI). Exact lo / hi are Clopper-Pearson on unit counts (ignore clustering within documents); the recall target is `missed` when the exact upper bound is below it. `point - exact lo` above 0.01 flags D-008 for review on arm A only (D-008 amended). Negatives forwarded = forwarded PII-free units / PII-free units (the work saved). Route recall counts misses after routing (1 - false forwards / positives). t_high `none`: no threshold reached the precision target, so only the role rule redacts. Doc-level arms are underpowered (few units per document).

| arm / qs | t_low | t_high | recall | exact lo / hi | recall target | point - exact lo | route recall | forward rate | negatives forwarded | false forwards | AUROC p(pii) | PII share at p >= t_low | units / docs / positives |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A / qs_v1 | 0.0084 | none | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9912 / 1.0000 | not rejected (upper 1.0000) | 0.0088 | 1.0000 | 0.0051 [0.0033, 0.0072] | 0.0055 | 0 | 0.7861 | 0.0737 | 5713 / 337 / 419 |
| A / qs_v2 | 0.0084 | none | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9912 / 1.0000 | not rejected (upper 1.0000) | 0.0088 | 1.0000 | 0.0053 [0.0034, 0.0073] | 0.0057 | 0 | 0.7861 | 0.0737 | 5713 / 337 / 419 |
| B1 / qs_v1 | 0.0683 | 1.0000 | 0.9967 [0.9897, 1.0000] | 0.9819 / 0.9999 | not rejected (upper 0.9999) | 0.0148 | 1.0000 | 0.0010 [0.0000, 0.0027] | 0.0012 | 0 | 0.3995 | 0.1594 | 1919 / 337 / 306 |
| B1 / qs_v2 | 0.0686 | 1.0000 | 0.9967 [0.9897, 1.0000] | 0.9819 / 0.9999 | not rejected (upper 0.9999) | 0.0148 | 0.9967 | 0.0026 [0.0005, 0.0050] | 0.0025 | 1 | 0.3994 | 0.1594 | 1919 / 337 / 306 |
| B2 / qs_v1 | 0.0578 | 0.9963 | 0.9957 [0.9861, 1.0000] | 0.9763 / 0.9999 | not rejected (upper 0.9999) | 0.0194 | 0.9957 | 0.0011 [0.0000, 0.0036] | 0.0000 | 1 | 0.4364 | 0.2547 | 912 / 337 / 233 |
| B2 / qs_v2 | 0.0578 | 0.9963 | 0.9957 [0.9861, 1.0000] | 0.9763 / 0.9999 | not rejected (upper 0.9999) | 0.0194 | 0.9957 | 0.0011 [0.0000, 0.0036] | 0.0000 | 1 | 0.4365 | 0.2547 | 912 / 337 / 233 |
| B3 / qs_v1 (doc-level, underpowered) | 0.0578 | 0.9963 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9841 / 1.0000 | not rejected (upper 1.0000) | 0.0159 | 1.0000 | 0.0019 [0.0000, 0.0059] | 0.0034 | 0 | 0.4563 | 0.4389 | 525 / 337 / 230 |
| B3 / qs_v2 (doc-level, underpowered) | 0.0578 | 0.9963 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9841 / 1.0000 | not rejected (upper 1.0000) | 0.0159 | 1.0000 | 0.0019 [0.0000, 0.0059] | 0.0034 | 0 | 0.4562 | 0.4389 | 525 / 337 / 230 |
| B4 / qs_v1 (doc-level, underpowered) | 0.3310 | 0.8038 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9830 / 1.0000 | not rejected (upper 1.0000) | 0.0170 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.4662 | 0.6380 | 337 / 337 / 215 |
| B4 / qs_v2 (doc-level, underpowered) | 0.3311 | 0.8038 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9830 / 1.0000 | not rejected (upper 1.0000) | 0.0170 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.4662 | 0.6380 | 337 / 337 / 215 |
| C / qs_v1 | 0.9697 | 0.9697 | 0.9952 [0.9878, 1.0000] | 0.9829 / 0.9994 | not rejected (upper 0.9994) | 0.0124 | 0.9976 | 0.9258 [0.9130, 0.9369] | 0.9989 | 1 | 0.9999 | 0.9905 | 5713 / 337 / 419 |
| C / qs_v2 | 0.9701 | 0.9701 | 0.9952 [0.9878, 1.0000] | 0.9829 / 0.9994 | not rejected (upper 0.9994) | 0.0124 | 0.9952 | 0.9263 [0.9135, 0.9374] | 0.9992 | 2 | 0.9999 | 0.9905 | 5713 / 337 / 419 |
| LC / qs_v1 | 0.0091 | 0.9871 | 0.9952 [0.9876, 1.0000] | 0.9829 / 0.9994 | not rejected (upper 0.9994) | 0.0124 | 0.9952 | 0.6079 [0.5855, 0.6308] | 0.6556 | 2 | 0.9864 | 0.1862 | 5713 / 337 / 419 |
| LW / qs_v1 | 0.0079 | 0.9874 | 0.9976 [0.9922, 1.0000] | 0.9868 / 0.9999 | not rejected (upper 0.9999) | 0.0108 | 0.9976 | 0.5118 [0.4868, 0.5361] | 0.5521 | 1 | 0.9848 | 0.1499 | 5713 / 337 / 419 |


### Recall vs forward rate on test (D-007 amended)

`t_low` fit on calib for each recall target, then applied to test with the same routing (role rule included). Test recall here is route recall: PII units not forwarded / PII units. Each point raises `t_high` to at least its `t_low`, as the headline fit does (D-007 note, M8). Forward rate is the share of test units passed without review; negatives forwarded is the share of PII-free units passed (the work saved). Saturated scores (arm C) leave few distinct thresholds, so neighbouring targets can coincide.

| arm / qs | calib target | t_low | test recall | exact lo / hi | forward rate | negatives forwarded | false forwards |
|---|---|---|---|---|---|---|---|
| A / qs_v1 | 0.9 | 0.0255 | 0.9475 | 0.9216 / 0.9668 | 13.76% | 0.1443 | 22 |
| A / qs_v1 | 0.95 | 0.0193 | 0.9761 | 0.9565 / 0.9885 | 5.90% | 0.0618 | 10 |
| A / qs_v1 | 0.98 | 0.0132 | 0.9905 | 0.9757 / 0.9974 | 1.93% | 0.0200 | 4 |
| A / qs_v1 | 0.99 | 0.0086 | 0.9952 | 0.9829 / 0.9994 | 0.58% | 0.0059 | 2 |
| A / qs_v1 | 0.995 | 0.0084 | 1.0000 | 0.9912 / 1.0000 | 0.51% | 0.0055 | 0 |
| A / qs_v2 | 0.9 | 0.0257 | 0.9332 | 0.9049 / 0.9551 | 14.65% | 0.1528 | 28 |
| A / qs_v2 | 0.95 | 0.0197 | 0.9714 | 0.9505 / 0.9851 | 6.46% | 0.0674 | 12 |
| A / qs_v2 | 0.98 | 0.0131 | 0.9881 | 0.9724 / 0.9961 | 2.03% | 0.0210 | 5 |
| A / qs_v2 | 0.99 | 0.0086 | 0.9952 | 0.9829 / 0.9994 | 0.61% | 0.0062 | 2 |
| A / qs_v2 | 0.995 | 0.0084 | 1.0000 | 0.9912 / 1.0000 | 0.53% | 0.0057 | 0 |
| B1 / qs_v1 | 0.9 | 0.6621 | 0.9020 | 0.8630 / 0.9329 | 3.60% | 0.0242 | 30 |
| B1 / qs_v1 | 0.95 | 0.4470 | 0.9641 | 0.9366 / 0.9819 | 1.20% | 0.0074 | 11 |
| B1 / qs_v1 | 0.98 | 0.2261 | 0.9935 | 0.9766 / 0.9992 | 0.31% | 0.0025 | 2 |
| B1 / qs_v1 | 0.99 | 0.1162 | 1.0000 | 0.9880 / 1.0000 | 0.16% | 0.0019 | 0 |
| B1 / qs_v1 | 0.995 | 0.0683 | 1.0000 | 0.9880 / 1.0000 | 0.10% | 0.0012 | 0 |
| B1 / qs_v2 | 0.9 | 0.6610 | 0.8758 | 0.8336 / 0.9106 | 5.00% | 0.0360 | 38 |
| B1 / qs_v2 | 0.95 | 0.4477 | 0.9510 | 0.9204 / 0.9723 | 1.77% | 0.0118 | 15 |
| B1 / qs_v2 | 0.98 | 0.2278 | 0.9869 | 0.9669 / 0.9964 | 0.52% | 0.0037 | 4 |
| B1 / qs_v2 | 0.99 | 0.1169 | 0.9967 | 0.9819 / 0.9999 | 0.31% | 0.0031 | 1 |
| B1 / qs_v2 | 0.995 | 0.0686 | 0.9967 | 0.9819 / 0.9999 | 0.26% | 0.0025 | 1 |
| B2 / qs_v1 | 0.9 | 0.6697 | 0.9099 | 0.8655 / 0.9433 | 4.50% | 0.0295 | 21 |
| B2 / qs_v1 | 0.95 | 0.5146 | 0.9485 | 0.9118 / 0.9731 | 2.30% | 0.0133 | 12 |
| B2 / qs_v1 | 0.98 | 0.2786 | 0.9871 | 0.9628 / 0.9973 | 0.44% | 0.0015 | 3 |
| B2 / qs_v1 | 0.99 | 0.0683 | 0.9957 | 0.9763 / 0.9999 | 0.11% | 0.0000 | 1 |
| B2 / qs_v1 | 0.995 | 0.0578 | 0.9957 | 0.9763 / 0.9999 | 0.11% | 0.0000 | 1 |
| B2 / qs_v2 | 0.9 | 0.6697 | 0.8798 | 0.8310 / 0.9186 | 6.25% | 0.0427 | 28 |
| B2 / qs_v2 | 0.95 | 0.5146 | 0.9227 | 0.8807 / 0.9536 | 3.29% | 0.0177 | 18 |
| B2 / qs_v2 | 0.98 | 0.2773 | 0.9828 | 0.9566 / 0.9953 | 0.55% | 0.0015 | 4 |
| B2 / qs_v2 | 0.99 | 0.0686 | 0.9957 | 0.9763 / 0.9999 | 0.11% | 0.0000 | 1 |
| B2 / qs_v2 | 0.995 | 0.0578 | 0.9957 | 0.9763 / 0.9999 | 0.11% | 0.0000 | 1 |
| B3 / qs_v1 (doc-level, underpowered) | 0.9 | 0.6697 | 0.9174 | 0.8740 / 0.9495 | 5.14% | 0.0271 | 19 |
| B3 / qs_v1 (doc-level, underpowered) | 0.95 | 0.4834 | 0.9652 | 0.9326 / 0.9849 | 1.90% | 0.0068 | 8 |
| B3 / qs_v1 (doc-level, underpowered) | 0.98 | 0.2306 | 0.9826 | 0.9561 / 0.9952 | 0.95% | 0.0034 | 4 |
| B3 / qs_v1 (doc-level, underpowered) | 0.99 | 0.0683 | 1.0000 | 0.9841 / 1.0000 | 0.19% | 0.0034 | 0 |
| B3 / qs_v1 (doc-level, underpowered) | 0.995 | 0.0578 | 1.0000 | 0.9841 / 1.0000 | 0.19% | 0.0034 | 0 |
| B3 / qs_v2 (doc-level, underpowered) | 0.9 | 0.6697 | 0.8870 | 0.8388 / 0.9248 | 7.62% | 0.0475 | 26 |
| B3 / qs_v2 (doc-level, underpowered) | 0.95 | 0.4834 | 0.9478 | 0.9106 / 0.9728 | 2.86% | 0.0102 | 12 |
| B3 / qs_v2 (doc-level, underpowered) | 0.98 | 0.2306 | 0.9783 | 0.9500 / 0.9929 | 1.14% | 0.0034 | 5 |
| B3 / qs_v2 (doc-level, underpowered) | 0.99 | 0.0686 | 1.0000 | 0.9841 / 1.0000 | 0.19% | 0.0034 | 0 |
| B3 / qs_v2 (doc-level, underpowered) | 0.995 | 0.0578 | 1.0000 | 0.9841 / 1.0000 | 0.19% | 0.0034 | 0 |
| B4 / qs_v1 (doc-level, underpowered) | 0.9 | 0.5258 | 0.9442 | 0.9045 / 0.9708 | 4.45% | 0.0246 | 12 |
| B4 / qs_v1 (doc-level, underpowered) | 0.95 | 0.4866 | 0.9814 | 0.9531 / 0.9949 | 1.48% | 0.0082 | 4 |
| B4 / qs_v1 (doc-level, underpowered) | 0.98 | 0.4247 | 0.9860 | 0.9598 / 0.9971 | 0.89% | 0.0000 | 3 |
| B4 / qs_v1 (doc-level, underpowered) | 0.99 | 0.3410 | 1.0000 | 0.9830 / 1.0000 | 0.00% | 0.0000 | 0 |
| B4 / qs_v1 (doc-level, underpowered) | 0.995 | 0.3310 | 1.0000 | 0.9830 / 1.0000 | 0.00% | 0.0000 | 0 |
| B4 / qs_v2 (doc-level, underpowered) | 0.9 | 0.5258 | 0.9116 | 0.8654 / 0.9460 | 7.72% | 0.0574 | 19 |
| B4 / qs_v2 (doc-level, underpowered) | 0.95 | 0.4868 | 0.9674 | 0.9341 / 0.9868 | 2.67% | 0.0164 | 7 |
| B4 / qs_v2 (doc-level, underpowered) | 0.98 | 0.4247 | 0.9814 | 0.9531 / 0.9949 | 1.19% | 0.0000 | 4 |
| B4 / qs_v2 (doc-level, underpowered) | 0.99 | 0.3414 | 1.0000 | 0.9830 / 1.0000 | 0.00% | 0.0000 | 0 |
| B4 / qs_v2 (doc-level, underpowered) | 0.995 | 0.3311 | 1.0000 | 0.9830 / 1.0000 | 0.00% | 0.0000 | 0 |
| C / qs_v1 | 0.9 | 0.9986 | 0.9690 | 0.9475 / 0.9834 | 92.82% | 0.9992 | 13 |
| C / qs_v1 | 0.95 | 0.9986 | 0.9714 | 0.9505 / 0.9851 | 92.81% | 0.9992 | 12 |
| C / qs_v1 | 0.98 | 0.9981 | 0.9928 | 0.9792 / 0.9985 | 92.65% | 0.9992 | 3 |
| C / qs_v1 | 0.99 | 0.9968 | 0.9952 | 0.9829 / 0.9994 | 92.63% | 0.9992 | 2 |
| C / qs_v1 | 0.995 | 0.9697 | 0.9976 | 0.9868 / 0.9999 | 92.58% | 0.9989 | 1 |
| C / qs_v2 | 0.9 | 0.9986 | 0.9117 | 0.8803 / 0.9371 | 93.30% | 0.9998 | 37 |
| C / qs_v2 | 0.95 | 0.9986 | 0.9308 | 0.9021 / 0.9532 | 93.16% | 0.9998 | 29 |
| C / qs_v2 | 0.98 | 0.9981 | 0.9761 | 0.9565 / 0.9885 | 92.82% | 0.9998 | 10 |
| C / qs_v2 | 0.99 | 0.9968 | 0.9881 | 0.9724 / 0.9961 | 92.72% | 0.9996 | 5 |
| C / qs_v2 | 0.995 | 0.9701 | 0.9952 | 0.9829 / 0.9994 | 92.63% | 0.9992 | 2 |
| LC / qs_v1 | 0.9 | 0.3102 | 0.8759 | 0.8405 / 0.9059 | 90.60% | 0.9679 | 52 |
| LC / qs_v1 | 0.95 | 0.1091 | 0.9499 | 0.9244 / 0.9687 | 88.27% | 0.9486 | 21 |
| LC / qs_v1 | 0.98 | 0.0489 | 0.9714 | 0.9505 / 0.9851 | 86.91% | 0.9356 | 12 |
| LC / qs_v1 | 0.99 | 0.0114 | 0.9952 | 0.9829 / 0.9994 | 68.63% | 0.7403 | 2 |
| LC / qs_v1 | 0.995 | 0.0091 | 0.9952 | 0.9829 / 0.9994 | 60.79% | 0.6556 | 2 |
| LW / qs_v1 | 0.9 | 0.2614 | 0.8831 | 0.8484 / 0.9122 | 89.64% | 0.9581 | 49 |
| LW / qs_v1 | 0.95 | 0.1047 | 0.9379 | 0.9104 / 0.9591 | 88.04% | 0.9452 | 26 |
| LW / qs_v1 | 0.98 | 0.0390 | 0.9809 | 0.9627 / 0.9917 | 85.23% | 0.9182 | 8 |
| LW / qs_v1 | 0.99 | 0.0099 | 0.9976 | 0.9868 / 0.9999 | 60.20% | 0.6494 | 1 |
| LW / qs_v1 | 0.995 | 0.0079 | 0.9976 | 0.9868 / 0.9999 | 51.18% | 0.5521 | 1 |


### Holdout (descriptive only, D-005)

All IRB letters (80 documents, 56 PII units of 724; one document type), never part of the headline. Forwarded: C / qs_v1 91.7%, C / qs_v2 91.9%, LC / qs_v1 64.2%, LW / qs_v1 55.9%. Weak evidence of transfer: holdout PII is names and e-mail addresses in letter headers; many letters name a PI who also appears in training documents (D-018: 33 of 56 positive units for arm C, `reports/audits/M8_results_review.md`); and the lexical baselines score AUROC LC 0.996, LW 0.996 here. Known limitation (M4 S1): a fixed alt-text contact line appears only in PII-free letters, a possible shortcut cue (C's holdout AUROC is unchanged without those units, same review).

| arm / qs | t_low | t_high | recall | exact lo / hi | recall target | point - exact lo | route recall | forward rate | negatives forwarded | false forwards | AUROC p(pii) | PII share at p >= t_low | units / docs / positives |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A / qs_v1 | 0.0084 | none | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9362 / 1.0000 | not rejected (upper 1.0000) | 0.0638 | 1.0000 | 0.0014 [0.0000, 0.0045] | 0.0015 | 0 | 0.6295 | 0.0775 | 724 / 80 / 56 |
| A / qs_v2 | 0.0084 | none | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9362 / 1.0000 | not rejected (upper 1.0000) | 0.0638 | 1.0000 | 0.0014 [0.0000, 0.0045] | 0.0015 | 0 | 0.6290 | 0.0775 | 724 / 80 / 56 |
| B1 / qs_v1 | 0.0683 | 1.0000 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9362 / 1.0000 | not rejected (upper 1.0000) | 0.0638 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.2767 | 0.2249 | 249 / 80 / 56 |
| B1 / qs_v2 | 0.0686 | 1.0000 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9362 / 1.0000 | not rejected (upper 1.0000) | 0.0638 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.2763 | 0.2249 | 249 / 80 / 56 |
| B2 / qs_v1 | 0.0578 | 0.9963 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9362 / 1.0000 | not rejected (upper 1.0000) | 0.0638 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.4247 | 0.4308 | 130 / 80 / 56 |
| B2 / qs_v2 | 0.0578 | 0.9963 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9362 / 1.0000 | not rejected (upper 1.0000) | 0.0638 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.4245 | 0.4308 | 130 / 80 / 56 |
| B3 / qs_v1 (doc-level, underpowered) | 0.0578 | 0.9963 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9362 / 1.0000 | not rejected (upper 1.0000) | 0.0638 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.5300 | 0.6667 | 84 / 80 / 56 |
| B3 / qs_v2 (doc-level, underpowered) | 0.0578 | 0.9963 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9362 / 1.0000 | not rejected (upper 1.0000) | 0.0638 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.5290 | 0.6667 | 84 / 80 / 56 |
| B4 / qs_v1 (doc-level, underpowered) | 0.3310 | 0.8038 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9362 / 1.0000 | not rejected (upper 1.0000) | 0.0638 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.5432 | 0.7000 | 80 / 80 / 56 |
| B4 / qs_v2 (doc-level, underpowered) | 0.3311 | 0.8038 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9362 / 1.0000 | not rejected (upper 1.0000) | 0.0638 | 1.0000 | 0.0000 [0.0000, 0.0000] | 0.0000 | 0 | 0.5428 | 0.7000 | 80 / 80 / 56 |
| C / qs_v1 | 0.9697 | 0.9697 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9362 / 1.0000 | not rejected (upper 1.0000) | 0.0638 | 1.0000 | 0.9171 [0.9018, 0.9303] | 0.9940 | 0 | 1.0000 | 0.9492 | 724 / 80 / 56 |
| C / qs_v2 | 0.9701 | 0.9701 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9362 / 1.0000 | not rejected (upper 1.0000) | 0.0638 | 1.0000 | 0.9185 [0.9032, 0.9315] | 0.9955 | 0 | 1.0000 | 0.9492 | 724 / 80 / 56 |
| LC / qs_v1 | 0.0091 | 0.9871 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9362 / 1.0000 | not rejected (upper 1.0000) | 0.0638 | 1.0000 | 0.6423 [0.5994, 0.6774] | 0.6961 | 0 | 0.9956 | 0.2162 | 724 / 80 / 56 |
| LW / qs_v1 | 0.0079 | 0.9874 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9362 / 1.0000 | not rejected (upper 1.0000) | 0.0638 | 1.0000 | 0.5594 [0.5126, 0.6005] | 0.6063 | 0 | 0.9957 | 0.1755 | 724 / 80 / 56 |

## 3. Per-question

### A / qs_v1, test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 5713 | 0.9319 | 0.5940 | 0.9267 (B) |
| subject_role | 5713 | 0.7329 | 0.2501 | 0.9267 (none) |
| category | 5713 | 0.9120 | 0.3458 | 0.9146 (none) |
| doc_kind | 5713 | 0.2486 | 0.1542 | 0.3413 (narrative) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 56 | 363 |
| B | 26 | 5268 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 26 | 12 | 10 | 176 |
| staff | 3 | 22 | 1 | 51 |
| both | 25 | 9 | 0 | 84 |
| none | 222 | 820 | 113 | 4139 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 0 | 1 | 46 | 0 | 67 |
| quasi | 5 | 3 | 80 | 2 | 138 |
| coded | 0 | 0 | 44 | 0 | 38 |
| staff | 0 | 1 | 4 | 21 | 38 |
| none | 11 | 11 | 56 | 5 | 5142 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 194 | 0 | 12 | 1744 |
| form_table | 74 | 19 | 28 | 1407 |
| correspondence | 59 | 3 | 34 | 899 |
| protocol_text | 56 | 0 | 11 | 1173 |

### A / qs_v1, holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 724 | 0.9227 | 0.4799 | 0.9227 (B) |
| subject_role | 724 | 0.7196 | 0.2177 | 0.9227 (none) |
| category | 724 | 0.9199 | 0.2570 | 0.9227 (none) |
| doc_kind | 724 | 0.0470 | 0.0299 | 1.0000 (correspondence) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 56 |
| B | 0 | 668 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 0 | 0 | 0 | 0 |
| staff | 0 | 3 | 0 | 53 |
| both | 0 | 0 | 0 | 0 |
| none | 20 | 115 | 15 | 518 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 0 | 0 | 0 | 0 | 0 |
| quasi | 0 | 0 | 0 | 0 | 0 |
| coded | 0 | 0 | 0 | 0 | 0 |
| staff | 0 | 0 | 1 | 2 | 53 |
| none | 0 | 2 | 2 | 0 | 664 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 0 | 0 | 0 | 0 |
| form_table | 0 | 0 | 0 | 0 |
| correspondence | 34 | 0 | 34 | 656 |
| protocol_text | 0 | 0 | 0 | 0 |

### A / qs_v2, test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 5713 | 0.9319 | 0.5940 | 0.9267 (B) |
| has_phi_direct | 5713 | 0.9587 | 0.6339 | 0.9800 (B) |
| has_phi_quasi | 5713 | 0.9421 | 0.7612 | 0.9443 (B) |
| has_coded_id | 5713 | 0.9303 | 0.7661 | 0.9457 (B) |
| has_staff_pii | 5713 | 0.5815 | 0.4153 | 0.9659 (B) |

Multi-label categories: micro-F1 0.2808, macro-F1 0.3790.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 56 | 363 |
| B | 26 | 5268 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 48 | 66 |
| B | 170 | 5429 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 205 | 113 |
| B | 218 | 5177 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 264 | 46 |
| B | 352 | 5051 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 138 | 57 |
| B | 2334 | 3184 |

### A / qs_v2, holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 724 | 0.9227 | 0.4799 | 0.9227 (B) |
| has_phi_direct | 724 | 0.9986 | 0.4997 | 1.0000 (B) |
| has_phi_quasi | 724 | 0.9765 | 0.4941 | 1.0000 (B) |
| has_coded_id | 724 | 0.9641 | 0.4909 | 1.0000 (B) |
| has_staff_pii | 724 | 0.6188 | 0.5109 | 0.9227 (B) |

Multi-label categories: micro-F1 0.2523, macro-F1 0.0703.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 56 |
| B | 0 | 668 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 1 | 723 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 17 | 707 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 26 | 698 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 54 | 2 |
| B | 274 | 394 |

### B1 / qs_v1, test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 1919 | 0.1641 | 0.1489 | 0.8405 (B) |
| subject_role | 1919 | 0.1662 | 0.1125 | 0.8405 (none) |
| category | 1919 | 0.4924 | 0.2279 | 0.8161 (none) |
| doc_kind | 1919 | 0.2626 | 0.2347 | 0.3246 (narrative) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 286 | 20 |
| B | 1584 | 29 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 37 | 51 | 5 | 38 |
| staff | 3 | 34 | 0 | 20 |
| both | 64 | 33 | 2 | 19 |
| none | 449 | 865 | 53 | 246 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 0 | 4 | 15 | 32 | 55 |
| quasi | 4 | 13 | 36 | 46 | 44 |
| coded | 0 | 2 | 27 | 10 | 19 |
| staff | 0 | 2 | 1 | 27 | 16 |
| none | 32 | 16 | 90 | 550 | 878 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 288 | 28 | 212 | 95 |
| form_table | 198 | 56 | 271 | 63 |
| correspondence | 144 | 33 | 96 | 44 |
| protocol_text | 176 | 34 | 117 | 64 |

### B1 / qs_v1, holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 249 | 0.2249 | 0.1836 | 0.7751 (B) |
| subject_role | 249 | 0.3293 | 0.1917 | 0.7751 (none) |
| category | 249 | 0.6265 | 0.2335 | 0.7751 (none) |
| doc_kind | 249 | 0.3253 | 0.1227 | 1.0000 (correspondence) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 56 | 0 |
| B | 193 | 0 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 0 | 0 | 0 | 0 |
| staff | 4 | 44 | 0 | 8 |
| both | 0 | 0 | 0 | 0 |
| none | 56 | 96 | 3 | 38 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 0 | 0 | 0 | 0 | 0 |
| quasi | 0 | 0 | 0 | 0 | 0 |
| coded | 0 | 0 | 0 | 0 | 0 |
| staff | 0 | 1 | 0 | 31 | 24 |
| none | 6 | 3 | 4 | 55 | 125 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 0 | 0 | 0 | 0 |
| form_table | 0 | 0 | 0 | 0 |
| correspondence | 84 | 27 | 81 | 57 |
| protocol_text | 0 | 0 | 0 | 0 |

### B1 / qs_v2, test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 1919 | 0.1647 | 0.1495 | 0.8405 (B) |
| has_phi_direct | 1919 | 0.1360 | 0.1348 | 0.9448 (B) |
| has_phi_quasi | 1919 | 0.1777 | 0.1774 | 0.8791 (B) |
| has_coded_id | 1919 | 0.1720 | 0.1712 | 0.8713 (B) |
| has_staff_pii | 1919 | 0.1485 | 0.1485 | 0.9088 (B) |

Multi-label categories: micro-F1 0.1619, macro-F1 0.1610.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 286 | 20 |
| B | 1583 | 30 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 94 | 12 |
| B | 1646 | 167 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 189 | 43 |
| B | 1535 | 152 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 194 | 53 |
| B | 1536 | 136 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 147 | 28 |
| B | 1606 | 138 |

### B1 / qs_v2, holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 249 | 0.2249 | 0.1836 | 0.7751 (B) |
| has_phi_direct | 249 | 0.0321 | 0.0311 | 1.0000 (B) |
| has_phi_quasi | 249 | 0.0643 | 0.0604 | 1.0000 (B) |
| has_coded_id | 249 | 0.0442 | 0.0423 | 1.0000 (B) |
| has_staff_pii | 249 | 0.2570 | 0.2331 | 0.7751 (B) |

Multi-label categories: micro-F1 0.1075, macro-F1 0.0922.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 56 | 0 |
| B | 193 | 0 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 241 | 8 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 233 | 16 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 238 | 11 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 54 | 2 |
| B | 183 | 10 |

### B2 / qs_v1, test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 912 | 0.2500 | 0.2105 | 0.7445 (B) |
| subject_role | 912 | 0.1612 | 0.1286 | 0.7445 (none) |
| category | 912 | 0.3991 | 0.2328 | 0.7105 (none) |
| doc_kind | 912 | 0.2818 | 0.2350 | 0.3421 (form_table) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 216 | 17 |
| B | 667 | 12 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 24 | 28 | 0 | 18 |
| staff | 4 | 34 | 0 | 11 |
| both | 58 | 39 | 2 | 15 |
| none | 172 | 391 | 29 | 87 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 0 | 4 | 20 | 31 | 45 |
| quasi | 3 | 10 | 30 | 19 | 22 |
| coded | 0 | 3 | 20 | 7 | 12 |
| staff | 0 | 1 | 2 | 25 | 10 |
| none | 13 | 1 | 43 | 282 | 309 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 159 | 8 | 86 | 29 |
| form_table | 70 | 22 | 198 | 22 |
| correspondence | 78 | 2 | 60 | 4 |
| protocol_text | 100 | 3 | 55 | 16 |

### B2 / qs_v1, holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 130 | 0.4308 | 0.3011 | 0.5692 (B) |
| subject_role | 130 | 0.4385 | 0.2148 | 0.5692 (none) |
| category | 130 | 0.5923 | 0.3960 | 0.5692 (none) |
| doc_kind | 130 | 0.5769 | 0.1829 | 1.0000 (correspondence) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 56 | 0 |
| B | 74 | 0 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 0 | 0 | 0 | 0 |
| staff | 3 | 46 | 1 | 6 |
| both | 0 | 0 | 0 | 0 |
| none | 13 | 47 | 3 | 11 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 0 | 0 | 0 | 0 | 0 |
| quasi | 0 | 0 | 0 | 0 | 0 |
| coded | 0 | 0 | 0 | 0 | 0 |
| staff | 0 | 0 | 0 | 36 | 20 |
| none | 1 | 0 | 0 | 32 | 41 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 0 | 0 | 0 | 0 |
| form_table | 0 | 0 | 0 | 0 |
| correspondence | 26 | 9 | 75 | 20 |
| protocol_text | 0 | 0 | 0 | 0 |

### B2 / qs_v2, test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 912 | 0.2500 | 0.2105 | 0.7445 (B) |
| has_phi_direct | 912 | 0.1678 | 0.1673 | 0.8904 (B) |
| has_phi_quasi | 912 | 0.2248 | 0.2186 | 0.8169 (B) |
| has_coded_id | 912 | 0.2368 | 0.2272 | 0.7917 (B) |
| has_staff_pii | 912 | 0.2127 | 0.2053 | 0.8213 (B) |

Multi-label categories: micro-F1 0.2690, macro-F1 0.2675.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 216 | 17 |
| B | 667 | 12 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 87 | 13 |
| B | 746 | 66 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 143 | 24 |
| B | 683 | 62 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 159 | 31 |
| B | 665 | 57 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 141 | 22 |
| B | 696 | 53 |

### B2 / qs_v2, holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 130 | 0.4308 | 0.3011 | 0.5692 (B) |
| has_phi_direct | 130 | 0.0154 | 0.0152 | 1.0000 (B) |
| has_phi_quasi | 130 | 0.0538 | 0.0511 | 1.0000 (B) |
| has_coded_id | 130 | 0.0308 | 0.0299 | 1.0000 (B) |
| has_staff_pii | 130 | 0.4462 | 0.3407 | 0.5692 (B) |

Multi-label categories: micro-F1 0.1968, macro-F1 0.1511.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 56 | 0 |
| B | 74 | 0 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 128 | 2 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 123 | 7 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 126 | 4 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 55 | 1 |
| B | 71 | 3 |

### B3 / qs_v1 (doc-level, underpowered), test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 525 | 0.4152 | 0.3039 | 0.5619 (B) |
| subject_role | 525 | 0.2038 | 0.1779 | 0.5619 (none) |
| category | 525 | 0.3752 | 0.2657 | 0.5143 (none) |
| doc_kind | 525 | 0.2781 | 0.2526 | 0.3962 (form_table) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 214 | 16 |
| B | 291 | 4 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 27 | 26 | 1 | 16 |
| staff | 2 | 36 | 0 | 10 |
| both | 59 | 39 | 1 | 13 |
| none | 66 | 168 | 18 | 43 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 0 | 3 | 26 | 24 | 47 |
| quasi | 4 | 12 | 30 | 14 | 22 |
| coded | 0 | 3 | 19 | 4 | 10 |
| staff | 0 | 0 | 0 | 28 | 9 |
| none | 2 | 5 | 40 | 85 | 138 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 78 | 2 | 55 | 14 |
| form_table | 13 | 14 | 169 | 12 |
| correspondence | 32 | 2 | 43 | 1 |
| protocol_text | 50 | 3 | 26 | 11 |

### B3 / qs_v1 (doc-level, underpowered), holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 84 | 0.6667 | 0.4000 | 0.6667 (A) |
| subject_role | 84 | 0.5714 | 0.2103 | 0.6667 (staff) |
| category | 84 | 0.6548 | 0.6212 | 0.6667 (staff) |
| doc_kind | 84 | 0.7024 | 0.2063 | 1.0000 (correspondence) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 56 | 0 |
| B | 28 | 0 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 0 | 0 | 0 | 0 |
| staff | 3 | 46 | 1 | 6 |
| both | 0 | 0 | 0 | 0 |
| none | 2 | 24 | 0 | 2 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 0 | 0 | 0 | 0 | 0 |
| quasi | 0 | 0 | 0 | 0 | 0 |
| coded | 0 | 0 | 0 | 0 | 0 |
| staff | 0 | 0 | 0 | 40 | 16 |
| none | 0 | 0 | 0 | 13 | 15 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 0 | 0 | 0 | 0 |
| form_table | 0 | 0 | 0 | 0 |
| correspondence | 6 | 2 | 59 | 17 |
| protocol_text | 0 | 0 | 0 | 0 |

### B3 / qs_v2 (doc-level, underpowered), test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 525 | 0.4152 | 0.3039 | 0.5619 (B) |
| has_phi_direct | 525 | 0.2514 | 0.2466 | 0.8095 (B) |
| has_phi_quasi | 525 | 0.3390 | 0.3087 | 0.6857 (B) |
| has_coded_id | 525 | 0.3543 | 0.3121 | 0.6495 (B) |
| has_staff_pii | 525 | 0.3352 | 0.3081 | 0.6952 (B) |

Multi-label categories: micro-F1 0.4256, macro-F1 0.4220.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 214 | 16 |
| B | 291 | 4 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 87 | 13 |
| B | 380 | 45 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 144 | 21 |
| B | 326 | 34 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 158 | 26 |
| B | 313 | 28 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 140 | 20 |
| B | 329 | 36 |

### B3 / qs_v2 (doc-level, underpowered), holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 84 | 0.6667 | 0.4000 | 0.6667 (A) |
| has_phi_direct | 84 | 0.0119 | 0.0118 | 1.0000 (B) |
| has_phi_quasi | 84 | 0.0357 | 0.0345 | 1.0000 (B) |
| has_coded_id | 84 | 0.0238 | 0.0233 | 1.0000 (B) |
| has_staff_pii | 84 | 0.6786 | 0.4660 | 0.6667 (A) |

Multi-label categories: micro-F1 0.2872, macro-F1 0.2007.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 56 | 0 |
| B | 28 | 0 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 83 | 1 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 81 | 3 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 82 | 2 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 55 | 1 |
| B | 26 | 2 |

### B4 / qs_v1 (doc-level, underpowered), test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 337 | 0.6053 | 0.3973 | 0.6380 (A) |
| subject_role | 337 | 0.2463 | 0.2287 | 0.3620 (none) |
| category | 337 | 0.2819 | 0.2494 | 0.2967 (direct) |
| doc_kind | 337 | 0.2493 | 0.2707 | 0.5638 (form_table) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 201 | 14 |
| B | 119 | 3 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 29 | 22 | 1 | 15 |
| staff | 2 | 28 | 0 | 7 |
| both | 60 | 39 | 1 | 11 |
| none | 28 | 55 | 14 | 25 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 0 | 4 | 36 | 26 | 34 |
| quasi | 4 | 11 | 31 | 11 | 21 |
| coded | 0 | 3 | 16 | 6 | 9 |
| staff | 0 | 0 | 1 | 18 | 6 |
| none | 1 | 4 | 30 | 15 | 50 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 36 | 1 | 28 | 6 |
| form_table | 7 | 8 | 163 | 12 |
| correspondence | 2 | 0 | 33 | 0 |
| protocol_text | 14 | 0 | 20 | 7 |

### B4 / qs_v1 (doc-level, underpowered), holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 80 | 0.7000 | 0.4118 | 0.7000 (A) |
| subject_role | 80 | 0.6000 | 0.2182 | 0.7000 (staff) |
| category | 80 | 0.6375 | 0.5827 | 0.7000 (staff) |
| doc_kind | 80 | 0.7250 | 0.2101 | 1.0000 (correspondence) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 56 | 0 |
| B | 24 | 0 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 0 | 0 | 0 | 0 |
| staff | 3 | 46 | 1 | 6 |
| both | 0 | 0 | 0 | 0 |
| none | 1 | 21 | 0 | 2 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 0 | 0 | 0 | 0 | 0 |
| quasi | 0 | 0 | 0 | 0 | 0 |
| coded | 0 | 0 | 0 | 0 | 0 |
| staff | 0 | 0 | 0 | 40 | 16 |
| none | 0 | 0 | 0 | 13 | 11 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 0 | 0 | 0 | 0 |
| form_table | 0 | 0 | 0 | 0 |
| correspondence | 4 | 2 | 58 | 16 |
| protocol_text | 0 | 0 | 0 | 0 |

### B4 / qs_v2 (doc-level, underpowered), test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 337 | 0.6053 | 0.3973 | 0.6380 (A) |
| has_phi_direct | 337 | 0.3739 | 0.3598 | 0.7033 (B) |
| has_phi_quasi | 337 | 0.4866 | 0.4149 | 0.5223 (B) |
| has_coded_id | 337 | 0.5193 | 0.4137 | 0.5401 (A) |
| has_staff_pii | 337 | 0.4599 | 0.4043 | 0.5608 (B) |

Multi-label categories: micro-F1 0.5868, macro-F1 0.5809.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 201 | 14 |
| B | 119 | 3 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 88 | 12 |
| B | 199 | 38 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 141 | 20 |
| B | 153 | 23 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 159 | 23 |
| B | 139 | 16 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 129 | 19 |
| B | 163 | 26 |

### B4 / qs_v2 (doc-level, underpowered), holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 80 | 0.7000 | 0.4118 | 0.7000 (A) |
| has_phi_direct | 80 | 0.0125 | 0.0123 | 1.0000 (B) |
| has_phi_quasi | 80 | 0.0250 | 0.0244 | 1.0000 (B) |
| has_coded_id | 80 | 0.0125 | 0.0123 | 1.0000 (B) |
| has_staff_pii | 80 | 0.7000 | 0.4489 | 0.7000 (A) |

Multi-label categories: micro-F1 0.2973, macro-F1 0.2052.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 56 | 0 |
| B | 24 | 0 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 79 | 1 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 78 | 2 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 79 | 1 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 55 | 1 |
| B | 23 | 1 |

### C / qs_v1, test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 5713 | 0.9988 | 0.9955 | 0.9267 (B) |
| subject_role | 5713 | 0.9975 | 0.9761 | 0.9267 (none) |
| category | 5713 | 0.9977 | 0.9853 | 0.9146 (none) |
| doc_kind | 5713 | 0.4558 | 0.3254 | 0.3413 (narrative) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 418 | 1 |
| B | 6 | 5288 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 222 | 0 | 1 | 1 |
| staff | 0 | 73 | 4 | 0 |
| both | 2 | 2 | 114 | 0 |
| none | 4 | 0 | 0 | 5290 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 112 | 0 | 0 | 2 | 0 |
| quasi | 0 | 225 | 1 | 1 | 1 |
| coded | 0 | 0 | 82 | 0 | 0 |
| staff | 0 | 0 | 0 | 63 | 1 |
| none | 0 | 6 | 0 | 1 | 5218 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 1886 | 43 | 0 | 21 |
| form_table | 951 | 576 | 0 | 1 |
| correspondence | 905 | 40 | 43 | 7 |
| protocol_text | 1110 | 31 | 0 | 99 |

### C / qs_v1, holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 724 | 0.9834 | 0.9471 | 0.9227 (B) |
| subject_role | 724 | 0.9793 | 0.4720 | 0.9227 (none) |
| category | 724 | 0.9738 | 0.6591 | 0.9227 (none) |
| doc_kind | 724 | 0.1105 | 0.0498 | 1.0000 (correspondence) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 56 | 0 |
| B | 12 | 656 |

Confusion, `subject_role`:

| gold \ pred | patient | staff | both | none |
|---|---|---|---|---|
| patient | 0 | 0 | 0 | 0 |
| staff | 0 | 45 | 11 | 0 |
| both | 0 | 0 | 0 | 0 |
| none | 4 | 0 | 0 | 664 |

Confusion, `category`:

| gold \ pred | direct | quasi | coded | staff | none |
|---|---|---|---|---|---|
| direct | 0 | 0 | 0 | 0 | 0 |
| quasi | 0 | 0 | 0 | 0 | 0 |
| coded | 0 | 0 | 0 | 0 | 0 |
| staff | 0 | 1 | 0 | 55 | 0 |
| none | 0 | 18 | 0 | 0 | 650 |

Confusion, `doc_kind`:

| gold \ pred | narrative | form_table | correspondence | protocol_text |
|---|---|---|---|---|
| narrative | 0 | 0 | 0 | 0 |
| form_table | 0 | 0 | 0 | 0 |
| correspondence | 568 | 72 | 80 | 4 |
| protocol_text | 0 | 0 | 0 | 0 |

### C / qs_v2, test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 5713 | 0.9988 | 0.9955 | 0.9267 (B) |
| has_phi_direct | 5713 | 0.9993 | 0.9909 | 0.9800 (B) |
| has_phi_quasi | 5713 | 0.9965 | 0.9836 | 0.9443 (B) |
| has_coded_id | 5713 | 0.9991 | 0.9957 | 0.9457 (B) |
| has_staff_pii | 5713 | 0.9996 | 0.9973 | 0.9659 (B) |

Multi-label categories: micro-F1 0.9835, macro-F1 0.9845.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 418 | 1 |
| B | 6 | 5288 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 110 | 4 |
| B | 0 | 5599 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 313 | 5 |
| B | 15 | 5380 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 308 | 2 |
| B | 3 | 5400 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 194 | 1 |
| B | 1 | 5517 |

### C / qs_v2, holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 724 | 0.9834 | 0.9471 | 0.9227 (B) |
| has_phi_direct | 724 | 1.0000 | 1.0000 | 1.0000 (B) |
| has_phi_quasi | 724 | 0.9268 | 0.4810 | 1.0000 (B) |
| has_coded_id | 724 | 1.0000 | 1.0000 | 1.0000 (B) |
| has_staff_pii | 724 | 1.0000 | 1.0000 | 0.9227 (B) |

Multi-label categories: micro-F1 0.6788, macro-F1 0.2500.

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 56 | 0 |
| B | 12 | 656 |

Confusion, `has_phi_direct`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 0 | 724 |

Confusion, `has_phi_quasi`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 53 | 671 |

Confusion, `has_coded_id`:

| gold \ pred | A | B |
|---|---|---|
| A | 0 | 0 |
| B | 0 | 724 |

Confusion, `has_staff_pii`:

| gold \ pred | A | B |
|---|---|---|
| A | 56 | 0 |
| B | 0 | 668 |

### LC / qs_v1, test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 5713 | 0.9667 | 0.8847 | 0.9267 (B) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 352 | 67 |
| B | 123 | 5171 |

### LC / qs_v1, holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 724 | 0.9710 | 0.9131 | 0.9227 (B) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 56 | 0 |
| B | 21 | 647 |

### LW / qs_v1, test

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 5713 | 0.9666 | 0.8840 | 0.9267 (B) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 351 | 68 |
| B | 123 | 5171 |

### LW / qs_v1, holdout

| question | n | accuracy | macro-F1 | majority baseline |
|---|---|---|---|---|
| pii_present | 724 | 0.9876 | 0.9582 | 0.9227 (B) |

Confusion, `pii_present`:

| gold \ pred | A | B |
|---|---|---|
| A | 54 | 2 |
| B | 7 | 661 |

### qs_v1 vs qs_v2

Same arm and split under both question sets. `pii_present` is the same question in both; categories are single-label in qs_v1 (`category`) and per-category yes/no in qs_v2.

| arm | split | qs | pii_present acc | pii_present macro-F1 | recall | forward rate | category macro-F1 (qs_v1) | categories micro / macro-F1 (qs_v2) |
|---|---|---|---|---|---|---|---|---|
| A | holdout | qs_v1 | 0.9227 | 0.4799 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0014 [0.0000, 0.0045] | 0.2570 | n/a |
| A | holdout | qs_v2 | 0.9227 | 0.4799 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0014 [0.0000, 0.0045] | n/a | 0.2523 / 0.0703 |
| A | test | qs_v1 | 0.9319 | 0.5940 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0051 [0.0033, 0.0072] | 0.3458 | n/a |
| A | test | qs_v2 | 0.9319 | 0.5940 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0053 [0.0034, 0.0073] | n/a | 0.2808 / 0.3790 |
| B1 | holdout | qs_v1 | 0.2249 | 0.1836 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | 0.2335 | n/a |
| B1 | holdout | qs_v2 | 0.2249 | 0.1836 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | n/a | 0.1075 / 0.0922 |
| B1 | test | qs_v1 | 0.1641 | 0.1489 | 0.9967 [0.9897, 1.0000] | 0.0010 [0.0000, 0.0027] | 0.2279 | n/a |
| B1 | test | qs_v2 | 0.1647 | 0.1495 | 0.9967 [0.9897, 1.0000] | 0.0026 [0.0005, 0.0050] | n/a | 0.1619 / 0.1610 |
| B2 | holdout | qs_v1 | 0.4308 | 0.3011 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | 0.3960 | n/a |
| B2 | holdout | qs_v2 | 0.4308 | 0.3011 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | n/a | 0.1968 / 0.1511 |
| B2 | test | qs_v1 | 0.2500 | 0.2105 | 0.9957 [0.9861, 1.0000] | 0.0011 [0.0000, 0.0036] | 0.2328 | n/a |
| B2 | test | qs_v2 | 0.2500 | 0.2105 | 0.9957 [0.9861, 1.0000] | 0.0011 [0.0000, 0.0036] | n/a | 0.2690 / 0.2675 |
| B3 | holdout | qs_v1 | 0.6667 | 0.4000 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | 0.6212 | n/a |
| B3 | holdout | qs_v2 | 0.6667 | 0.4000 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | n/a | 0.2872 / 0.2007 |
| B3 | test | qs_v1 | 0.4152 | 0.3039 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0019 [0.0000, 0.0059] | 0.2657 | n/a |
| B3 | test | qs_v2 | 0.4152 | 0.3039 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0019 [0.0000, 0.0059] | n/a | 0.4256 / 0.4220 |
| B4 | holdout | qs_v1 | 0.7000 | 0.4118 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | 0.5827 | n/a |
| B4 | holdout | qs_v2 | 0.7000 | 0.4118 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | n/a | 0.2973 / 0.2052 |
| B4 | test | qs_v1 | 0.6053 | 0.3973 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | 0.2494 | n/a |
| B4 | test | qs_v2 | 0.6053 | 0.3973 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.0000 [0.0000, 0.0000] | n/a | 0.5868 / 0.5809 |
| C | holdout | qs_v1 | 0.9834 | 0.9471 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9171 [0.9018, 0.9303] | 0.6591 | n/a |
| C | holdout | qs_v2 | 0.9834 | 0.9471 | 1.0000 (no misses; CI n/a, see exact bounds) | 0.9185 [0.9032, 0.9315] | n/a | 0.6788 / 0.2500 |
| C | test | qs_v1 | 0.9988 | 0.9955 | 0.9952 [0.9878, 1.0000] | 0.9258 [0.9130, 0.9369] | 0.9853 | n/a |
| C | test | qs_v2 | 0.9988 | 0.9955 | 0.9952 [0.9878, 1.0000] | 0.9263 [0.9135, 0.9374] | n/a | 0.9835 / 0.9845 |

## 4. Calibration

ECE uses 15 equal-width bins on the max probability. Brier is multi-class. Correctness AUROC: how well the max probability separates right from wrong answers (not PII discrimination; for p(pii) AUROC see section 2). `= raw (T fallback)`: the temperature fit hit its bound, so T = 1 and the calibrated columns equal raw; calibration did nothing there.

### A / qs_v1, test

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.1102 | 0.0179 | 0.1317 | 0.1084 | 0.7675 | 0.7675 |
| subject_role | 0.2364 | 0.0922 | 0.4891 | 0.4171 | 0.6449 | 0.6584 |
| category | 0.4426 | 0.0364 | 0.4031 | 0.1477 | 0.8149 | 0.8378 |
| doc_kind = raw (T fallback) | 0.4039 | 0.4039 | 1.0044 | 1.0044 | 0.4929 | 0.4929 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 33 | 0.5188 | 0.5152 | 17 | 0.5209 | 0.4706 |
| [0.533, 0.600) | 86 | 0.5661 | 0.3721 | 45 | 0.5665 | 0.4222 |
| [0.600, 0.667) | 131 | 0.6349 | 0.6031 | 55 | 0.6329 | 0.3818 |
| [0.667, 0.733) | 254 | 0.7063 | 0.7795 | 75 | 0.7030 | 0.5867 |
| [0.733, 0.800) | 735 | 0.7742 | 0.8966 | 109 | 0.7700 | 0.6514 |
| [0.800, 0.867) | 2742 | 0.8383 | 0.9697 | 258 | 0.8392 | 0.8140 |
| [0.867, 0.933) | 1688 | 0.8879 | 0.9704 | 1107 | 0.9107 | 0.9214 |
| [0.933, 1.000) | 44 | 0.9425 | 0.9545 | 4047 | 0.9612 | 0.9713 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 2 | 0.2648 | 0.0000 | 0 | n/a | n/a |
| [0.267, 0.333) | 263 | 0.3105 | 0.4259 | 55 | 0.3149 | 0.4364 |
| [0.333, 0.400) | 710 | 0.3713 | 0.5944 | 216 | 0.3707 | 0.4306 |
| [0.400, 0.467) | 1354 | 0.4360 | 0.6713 | 403 | 0.4374 | 0.5459 |
| [0.467, 0.533) | 1297 | 0.4998 | 0.7772 | 692 | 0.5016 | 0.6084 |
| [0.533, 0.600) | 1133 | 0.5648 | 0.8429 | 764 | 0.5665 | 0.6780 |
| [0.600, 0.667) | 637 | 0.6289 | 0.8352 | 749 | 0.6349 | 0.7490 |
| [0.667, 0.733) | 217 | 0.6922 | 0.8111 | 779 | 0.7007 | 0.8062 |
| [0.733, 0.800) | 68 | 0.7594 | 0.7941 | 858 | 0.7671 | 0.8520 |
| [0.800, 0.867) | 25 | 0.8286 | 0.7200 | 685 | 0.8315 | 0.8467 |
| [0.867, 0.933) | 4 | 0.8903 | 0.2500 | 402 | 0.8933 | 0.8209 |
| [0.933, 1.000) | 3 | 0.9401 | 0.0000 | 110 | 0.9586 | 0.7364 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 17 | 0.2588 | 0.1765 | 0 | n/a | n/a |
| [0.267, 0.333) | 219 | 0.3080 | 0.4658 | 2 | 0.3280 | 0.0000 |
| [0.333, 0.400) | 668 | 0.3717 | 0.7365 | 19 | 0.3681 | 0.2632 |
| [0.400, 0.467) | 1641 | 0.4371 | 0.9311 | 53 | 0.4415 | 0.3585 |
| [0.467, 0.533) | 2145 | 0.4988 | 0.9725 | 96 | 0.5001 | 0.4479 |
| [0.533, 0.600) | 916 | 0.5568 | 0.9771 | 96 | 0.5682 | 0.5521 |
| [0.600, 0.667) | 102 | 0.6196 | 0.9804 | 117 | 0.6360 | 0.5214 |
| [0.667, 0.733) | 5 | 0.6839 | 0.8000 | 185 | 0.7040 | 0.6811 |
| [0.733, 0.800) | 0 | n/a | n/a | 298 | 0.7690 | 0.7886 |
| [0.800, 0.867) | 0 | n/a | n/a | 564 | 0.8380 | 0.9007 |
| [0.867, 0.933) | 0 | n/a | n/a | 1618 | 0.9064 | 0.9580 |
| [0.933, 1.000) | 0 | n/a | n/a | 2665 | 0.9597 | 0.9794 |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 61 | 0.3123 | 0.1475 | 61 | 0.3123 | 0.1475 |
| [0.333, 0.400) | 320 | 0.3735 | 0.2437 | 320 | 0.3735 | 0.2437 |
| [0.400, 0.467) | 568 | 0.4357 | 0.2518 | 568 | 0.4357 | 0.2518 |
| [0.467, 0.533) | 661 | 0.5003 | 0.2799 | 661 | 0.5003 | 0.2799 |
| [0.533, 0.600) | 662 | 0.5664 | 0.2417 | 662 | 0.5664 | 0.2417 |
| [0.600, 0.667) | 685 | 0.6328 | 0.2569 | 685 | 0.6328 | 0.2569 |
| [0.667, 0.733) | 733 | 0.6992 | 0.2483 | 733 | 0.6992 | 0.2483 |
| [0.733, 0.800) | 705 | 0.7661 | 0.2355 | 705 | 0.7661 | 0.2355 |
| [0.800, 0.867) | 649 | 0.8317 | 0.2496 | 649 | 0.8317 | 0.2496 |
| [0.867, 0.933) | 496 | 0.8968 | 0.2500 | 496 | 0.8968 | 0.2500 |
| [0.933, 1.000) | 173 | 0.9541 | 0.2023 | 173 | 0.9541 | 0.2023 |

### A / qs_v1, holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.0801 | 0.0285 | 0.1542 | 0.1426 | 0.6295 | 0.6295 |
| subject_role | 0.2240 | 0.0728 | 0.4733 | 0.4029 | 0.6629 | 0.6819 |
| category | 0.4463 | 0.0209 | 0.4020 | 0.1484 | 0.7560 | 0.7598 |
| doc_kind = raw (T fallback) | 0.5990 | 0.5990 | 1.2214 | 1.2214 | 0.3025 | 0.3024 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.533, 0.600) | 1 | 0.5875 | 1.0000 | 0 | n/a | n/a |
| [0.600, 0.667) | 4 | 0.6398 | 1.0000 | 1 | 0.6512 | 1.0000 |
| [0.667, 0.733) | 12 | 0.7114 | 0.7500 | 2 | 0.7244 | 1.0000 |
| [0.733, 0.800) | 93 | 0.7724 | 0.8925 | 4 | 0.7654 | 1.0000 |
| [0.800, 0.867) | 373 | 0.8381 | 0.9169 | 16 | 0.8482 | 0.7500 |
| [0.867, 0.933) | 238 | 0.8867 | 0.9496 | 143 | 0.9095 | 0.8811 |
| [0.933, 1.000) | 3 | 0.9427 | 1.0000 | 558 | 0.9608 | 0.9373 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 39 | 0.3099 | 0.3846 | 9 | 0.3200 | 0.2222 |
| [0.333, 0.400) | 86 | 0.3684 | 0.6047 | 35 | 0.3730 | 0.4286 |
| [0.400, 0.467) | 167 | 0.4338 | 0.6766 | 47 | 0.4329 | 0.4894 |
| [0.467, 0.533) | 178 | 0.5006 | 0.6966 | 82 | 0.5038 | 0.6341 |
| [0.533, 0.600) | 138 | 0.5632 | 0.8261 | 91 | 0.5637 | 0.7473 |
| [0.600, 0.667) | 75 | 0.6300 | 0.8933 | 104 | 0.6342 | 0.6635 |
| [0.667, 0.733) | 28 | 0.6913 | 0.9286 | 105 | 0.6969 | 0.7238 |
| [0.733, 0.800) | 11 | 0.7670 | 0.7273 | 107 | 0.7674 | 0.8411 |
| [0.800, 0.867) | 2 | 0.8028 | 1.0000 | 80 | 0.8325 | 0.8500 |
| [0.867, 0.933) | 0 | n/a | n/a | 50 | 0.8938 | 0.9400 |
| [0.933, 1.000) | 0 | n/a | n/a | 14 | 0.9539 | 0.7857 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 17 | 0.3082 | 0.7059 | 0 | n/a | n/a |
| [0.333, 0.400) | 71 | 0.3787 | 0.7606 | 0 | n/a | n/a |
| [0.400, 0.467) | 245 | 0.4379 | 0.9184 | 6 | 0.4397 | 0.5000 |
| [0.467, 0.533) | 261 | 0.4996 | 0.9387 | 5 | 0.5031 | 0.6000 |
| [0.533, 0.600) | 118 | 0.5561 | 1.0000 | 7 | 0.5593 | 0.7143 |
| [0.600, 0.667) | 11 | 0.6168 | 1.0000 | 7 | 0.6370 | 0.8571 |
| [0.667, 0.733) | 1 | 0.6761 | 1.0000 | 13 | 0.7019 | 0.6923 |
| [0.733, 0.800) | 0 | n/a | n/a | 30 | 0.7675 | 0.7667 |
| [0.800, 0.867) | 0 | n/a | n/a | 91 | 0.8362 | 0.8681 |
| [0.867, 0.933) | 0 | n/a | n/a | 244 | 0.9057 | 0.9262 |
| [0.933, 1.000) | 0 | n/a | n/a | 321 | 0.9608 | 0.9720 |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 2 | 0.3131 | 0.0000 | 2 | 0.3131 | 0.0000 |
| [0.333, 0.400) | 32 | 0.3715 | 0.0312 | 32 | 0.3715 | 0.0312 |
| [0.400, 0.467) | 70 | 0.4310 | 0.0857 | 71 | 0.4315 | 0.0845 |
| [0.467, 0.533) | 103 | 0.5007 | 0.1068 | 102 | 0.5010 | 0.1078 |
| [0.533, 0.600) | 109 | 0.5654 | 0.0734 | 109 | 0.5654 | 0.0734 |
| [0.600, 0.667) | 88 | 0.6310 | 0.0455 | 88 | 0.6310 | 0.0455 |
| [0.667, 0.733) | 84 | 0.6991 | 0.0119 | 84 | 0.6990 | 0.0119 |
| [0.733, 0.800) | 78 | 0.7653 | 0.0128 | 78 | 0.7653 | 0.0128 |
| [0.800, 0.867) | 85 | 0.8342 | 0.0235 | 85 | 0.8341 | 0.0235 |
| [0.867, 0.933) | 49 | 0.8981 | 0.0000 | 49 | 0.8981 | 0.0000 |
| [0.933, 1.000) | 24 | 0.9552 | 0.0000 | 24 | 0.9552 | 0.0000 |

### A / qs_v2, test

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.1100 | 0.0184 | 0.1317 | 0.1085 | 0.7675 | 0.7675 |
| has_phi_direct | 0.2180 | 0.0061 | 0.1646 | 0.0637 | 0.8570 | 0.8570 |
| has_phi_quasi | 0.2632 | 0.0160 | 0.2410 | 0.0983 | 0.7680 | 0.7680 |
| has_coded_id | 0.2552 | 0.0207 | 0.2530 | 0.1197 | 0.7290 | 0.7290 |
| has_staff_pii = raw (T fallback) | 0.1294 | 0.1294 | 0.5366 | 0.5366 | 0.4337 | 0.4337 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 33 | 0.5187 | 0.5152 | 16 | 0.5199 | 0.5000 |
| [0.533, 0.600) | 85 | 0.5661 | 0.3647 | 45 | 0.5655 | 0.4222 |
| [0.600, 0.667) | 131 | 0.6344 | 0.6107 | 56 | 0.6325 | 0.3571 |
| [0.667, 0.733) | 256 | 0.7062 | 0.7734 | 76 | 0.7035 | 0.5921 |
| [0.733, 0.800) | 731 | 0.7741 | 0.8974 | 108 | 0.7705 | 0.6574 |
| [0.800, 0.867) | 2744 | 0.8382 | 0.9698 | 262 | 0.8396 | 0.8092 |
| [0.867, 0.933) | 1688 | 0.8879 | 0.9704 | 1106 | 0.9109 | 0.9231 |
| [0.933, 1.000) | 45 | 0.9423 | 0.9556 | 4044 | 0.9613 | 0.9713 |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 96 | 0.5177 | 0.4896 | 19 | 0.5184 | 0.6316 |
| [0.533, 0.600) | 245 | 0.5675 | 0.7020 | 48 | 0.5643 | 0.4792 |
| [0.600, 0.667) | 496 | 0.6409 | 0.8931 | 60 | 0.6343 | 0.4833 |
| [0.667, 0.733) | 1438 | 0.7056 | 0.9791 | 75 | 0.6997 | 0.6800 |
| [0.733, 0.800) | 2234 | 0.7655 | 0.9915 | 75 | 0.7702 | 0.7067 |
| [0.800, 0.867) | 1028 | 0.8260 | 0.9922 | 118 | 0.8352 | 0.7712 |
| [0.867, 0.933) | 167 | 0.8876 | 0.9760 | 324 | 0.9088 | 0.9012 |
| [0.933, 1.000) | 9 | 0.9453 | 1.0000 | 4994 | 0.9857 | 0.9864 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 197 | 0.5163 | 0.6091 | 49 | 0.5164 | 0.5306 |
| [0.533, 0.600) | 623 | 0.5705 | 0.8443 | 83 | 0.5653 | 0.5542 |
| [0.600, 0.667) | 1488 | 0.6374 | 0.9469 | 104 | 0.6357 | 0.7212 |
| [0.667, 0.733) | 2137 | 0.6996 | 0.9761 | 123 | 0.7002 | 0.7967 |
| [0.733, 0.800) | 1061 | 0.7602 | 0.9764 | 186 | 0.7698 | 0.8280 |
| [0.800, 0.867) | 192 | 0.8230 | 0.9896 | 316 | 0.8364 | 0.8987 |
| [0.867, 0.933) | 13 | 0.8851 | 1.0000 | 780 | 0.9059 | 0.9385 |
| [0.933, 1.000) | 2 | 0.9467 | 1.0000 | 4072 | 0.9774 | 0.9742 |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 214 | 0.5166 | 0.6075 | 59 | 0.5192 | 0.5763 |
| [0.533, 0.600) | 631 | 0.5716 | 0.8320 | 99 | 0.5663 | 0.5758 |
| [0.600, 0.667) | 1543 | 0.6374 | 0.9345 | 117 | 0.6337 | 0.6923 |
| [0.667, 0.733) | 2180 | 0.6988 | 0.9702 | 153 | 0.7038 | 0.8170 |
| [0.733, 0.800) | 937 | 0.7588 | 0.9712 | 228 | 0.7715 | 0.8728 |
| [0.800, 0.867) | 178 | 0.8247 | 0.9494 | 413 | 0.8374 | 0.8692 |
| [0.867, 0.933) | 29 | 0.8905 | 0.8276 | 1064 | 0.9057 | 0.9389 |
| [0.933, 1.000) | 1 | 0.9409 | 0.0000 | 3580 | 0.9719 | 0.9668 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 953 | 0.5167 | 0.5467 | 953 | 0.5167 | 0.5467 |
| [0.533, 0.600) | 1834 | 0.5659 | 0.6570 | 1834 | 0.5659 | 0.6570 |
| [0.600, 0.667) | 1381 | 0.6306 | 0.6749 | 1381 | 0.6306 | 0.6749 |
| [0.667, 0.733) | 846 | 0.6960 | 0.5508 | 846 | 0.6960 | 0.5508 |
| [0.733, 0.800) | 433 | 0.7633 | 0.3372 | 433 | 0.7633 | 0.3372 |
| [0.800, 0.867) | 182 | 0.8309 | 0.2143 | 182 | 0.8309 | 0.2143 |
| [0.867, 0.933) | 74 | 0.8936 | 0.1622 | 74 | 0.8936 | 0.1622 |
| [0.933, 1.000) | 10 | 0.9513 | 0.1000 | 10 | 0.9513 | 0.1000 |

### A / qs_v2, holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.0801 | 0.0285 | 0.1542 | 0.1426 | 0.6290 | 0.6290 |
| has_phi_direct | 0.2480 | 0.0238 | 0.1341 | 0.0068 | 0.9931 | 0.9931 |
| has_phi_quasi | 0.2921 | 0.0417 | 0.2106 | 0.0376 | 0.9685 | 0.9685 |
| has_coded_id | 0.2864 | 0.0497 | 0.2288 | 0.0638 | 0.8615 | 0.8615 |
| has_staff_pii = raw (T fallback) | 0.1532 | 0.1532 | 0.5214 | 0.5214 | 0.4293 | 0.4293 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.533, 0.600) | 1 | 0.5881 | 1.0000 | 0 | n/a | n/a |
| [0.600, 0.667) | 4 | 0.6396 | 1.0000 | 1 | 0.6522 | 1.0000 |
| [0.667, 0.733) | 12 | 0.7113 | 0.7500 | 2 | 0.7238 | 1.0000 |
| [0.733, 0.800) | 93 | 0.7724 | 0.8925 | 4 | 0.7652 | 1.0000 |
| [0.800, 0.867) | 374 | 0.8382 | 0.9171 | 17 | 0.8492 | 0.7059 |
| [0.867, 0.933) | 237 | 0.8868 | 0.9494 | 140 | 0.9094 | 0.8857 |
| [0.933, 1.000) | 3 | 0.9427 | 1.0000 | 560 | 0.9608 | 0.9375 |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 3 | 0.5118 | 1.0000 | 2 | 0.5203 | 1.0000 |
| [0.533, 0.600) | 12 | 0.5734 | 0.9167 | 0 | n/a | n/a |
| [0.600, 0.667) | 65 | 0.6449 | 1.0000 | 1 | 0.6022 | 1.0000 |
| [0.667, 0.733) | 198 | 0.7057 | 1.0000 | 5 | 0.7106 | 0.8000 |
| [0.733, 0.800) | 278 | 0.7643 | 1.0000 | 3 | 0.7787 | 1.0000 |
| [0.800, 0.867) | 135 | 0.8252 | 1.0000 | 9 | 0.8382 | 1.0000 |
| [0.867, 0.933) | 31 | 0.8906 | 1.0000 | 42 | 0.9132 | 1.0000 |
| [0.933, 1.000) | 2 | 0.9544 | 1.0000 | 662 | 0.9854 | 1.0000 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 19 | 0.5140 | 0.4737 | 6 | 0.5150 | 0.5000 |
| [0.533, 0.600) | 63 | 0.5725 | 0.9206 | 8 | 0.5629 | 0.3750 |
| [0.600, 0.667) | 194 | 0.6372 | 0.9897 | 8 | 0.6343 | 0.6250 |
| [0.667, 0.733) | 257 | 0.7001 | 1.0000 | 13 | 0.6994 | 0.9231 |
| [0.733, 0.800) | 155 | 0.7593 | 1.0000 | 16 | 0.7720 | 0.9375 |
| [0.800, 0.867) | 30 | 0.8226 | 1.0000 | 35 | 0.8383 | 0.9429 |
| [0.867, 0.933) | 6 | 0.8905 | 1.0000 | 106 | 0.9058 | 0.9811 |
| [0.933, 1.000) | 0 | n/a | n/a | 532 | 0.9787 | 1.0000 |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 28 | 0.5157 | 0.5714 | 7 | 0.5105 | 0.4286 |
| [0.533, 0.600) | 70 | 0.5723 | 0.9429 | 15 | 0.5667 | 0.5333 |
| [0.600, 0.667) | 206 | 0.6370 | 0.9660 | 15 | 0.6357 | 0.8667 |
| [0.667, 0.733) | 271 | 0.6983 | 0.9926 | 12 | 0.7056 | 0.8333 |
| [0.733, 0.800) | 114 | 0.7577 | 0.9912 | 26 | 0.7706 | 1.0000 |
| [0.800, 0.867) | 30 | 0.8252 | 1.0000 | 61 | 0.8392 | 0.9344 |
| [0.867, 0.933) | 5 | 0.9041 | 1.0000 | 126 | 0.9053 | 0.9683 |
| [0.933, 1.000) | 0 | n/a | n/a | 462 | 0.9714 | 0.9935 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 100 | 0.5174 | 0.5900 | 100 | 0.5174 | 0.5900 |
| [0.533, 0.600) | 218 | 0.5677 | 0.6789 | 218 | 0.5677 | 0.6789 |
| [0.600, 0.667) | 170 | 0.6313 | 0.7353 | 170 | 0.6313 | 0.7353 |
| [0.667, 0.733) | 111 | 0.6966 | 0.5586 | 111 | 0.6966 | 0.5586 |
| [0.733, 0.800) | 66 | 0.7620 | 0.4697 | 66 | 0.7620 | 0.4697 |
| [0.800, 0.867) | 40 | 0.8283 | 0.4500 | 40 | 0.8283 | 0.4500 |
| [0.867, 0.933) | 18 | 0.8923 | 0.2778 | 18 | 0.8923 | 0.2778 |
| [0.933, 1.000) | 1 | 0.9517 | 0.0000 | 1 | 0.9517 | 0.0000 |

### B1 / qs_v1, test

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.7398 | 0.7398 | 1.4105 | 1.4105 | 0.3955 | 0.3955 |
| subject_role = raw (T fallback) | 0.5073 | 0.5073 | 1.1733 | 1.1733 | 0.3941 | 0.3941 |
| category | 0.1788 | 0.1713 | 0.7157 | 0.7043 | 0.4769 | 0.4716 |
| doc_kind = raw (T fallback) | 0.3662 | 0.3662 | 1.0147 | 1.0147 | 0.4949 | 0.4948 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 13 | 0.5184 | 0.4615 | 13 | 0.5184 | 0.4615 |
| [0.533, 0.600) | 33 | 0.5731 | 0.5152 | 33 | 0.5731 | 0.5152 |
| [0.600, 0.667) | 28 | 0.6293 | 0.3571 | 28 | 0.6293 | 0.3571 |
| [0.667, 0.733) | 56 | 0.6991 | 0.2857 | 56 | 0.6991 | 0.2857 |
| [0.733, 0.800) | 68 | 0.7697 | 0.2500 | 68 | 0.7697 | 0.2500 |
| [0.800, 0.867) | 180 | 0.8407 | 0.2111 | 180 | 0.8407 | 0.2111 |
| [0.867, 0.933) | 546 | 0.9063 | 0.1484 | 546 | 0.9063 | 0.1484 |
| [0.933, 1.000) | 995 | 0.9586 | 0.1307 | 995 | 0.9586 | 0.1307 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 49 | 0.3119 | 0.2857 | 49 | 0.3119 | 0.2857 |
| [0.333, 0.400) | 143 | 0.3679 | 0.2657 | 143 | 0.3679 | 0.2657 |
| [0.400, 0.467) | 203 | 0.4353 | 0.2069 | 203 | 0.4353 | 0.2069 |
| [0.467, 0.533) | 218 | 0.5000 | 0.2477 | 218 | 0.5000 | 0.2477 |
| [0.533, 0.600) | 195 | 0.5667 | 0.1385 | 195 | 0.5667 | 0.1385 |
| [0.600, 0.667) | 178 | 0.6333 | 0.1685 | 178 | 0.6333 | 0.1685 |
| [0.667, 0.733) | 154 | 0.6979 | 0.1494 | 154 | 0.6979 | 0.1494 |
| [0.733, 0.800) | 130 | 0.7645 | 0.1692 | 130 | 0.7645 | 0.1692 |
| [0.800, 0.867) | 161 | 0.8319 | 0.0683 | 161 | 0.8319 | 0.0683 |
| [0.867, 0.933) | 170 | 0.9011 | 0.1529 | 170 | 0.9011 | 0.1529 |
| [0.933, 1.000) | 318 | 0.9748 | 0.1006 | 318 | 0.9748 | 0.1006 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 40 | 0.2513 | 0.4750 | 96 | 0.2491 | 0.4062 |
| [0.267, 0.333) | 186 | 0.3050 | 0.4086 | 406 | 0.3033 | 0.5123 |
| [0.333, 0.400) | 322 | 0.3682 | 0.5342 | 399 | 0.3647 | 0.5439 |
| [0.400, 0.467) | 271 | 0.4315 | 0.5609 | 305 | 0.4322 | 0.5311 |
| [0.467, 0.533) | 238 | 0.5003 | 0.5252 | 233 | 0.4989 | 0.4850 |
| [0.533, 0.600) | 197 | 0.5639 | 0.5127 | 145 | 0.5638 | 0.4276 |
| [0.600, 0.667) | 165 | 0.6300 | 0.4606 | 105 | 0.6331 | 0.4857 |
| [0.667, 0.733) | 141 | 0.6949 | 0.4823 | 78 | 0.6967 | 0.5000 |
| [0.733, 0.800) | 104 | 0.7666 | 0.4808 | 69 | 0.7705 | 0.3333 |
| [0.800, 0.867) | 92 | 0.8316 | 0.5109 | 32 | 0.8316 | 0.4375 |
| [0.867, 0.933) | 84 | 0.8989 | 0.3571 | 26 | 0.9081 | 0.3462 |
| [0.933, 1.000) | 79 | 0.9697 | 0.3671 | 25 | 0.9558 | 0.3200 |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 18 | 0.2591 | 0.3333 | 18 | 0.2591 | 0.3333 |
| [0.267, 0.333) | 116 | 0.3067 | 0.2328 | 116 | 0.3067 | 0.2328 |
| [0.333, 0.400) | 237 | 0.3676 | 0.2489 | 237 | 0.3676 | 0.2489 |
| [0.400, 0.467) | 234 | 0.4305 | 0.2308 | 234 | 0.4305 | 0.2308 |
| [0.467, 0.533) | 226 | 0.4987 | 0.2965 | 226 | 0.4987 | 0.2965 |
| [0.533, 0.600) | 189 | 0.5665 | 0.3016 | 189 | 0.5665 | 0.3016 |
| [0.600, 0.667) | 155 | 0.6320 | 0.2581 | 155 | 0.6320 | 0.2581 |
| [0.667, 0.733) | 113 | 0.7005 | 0.2743 | 114 | 0.7008 | 0.2719 |
| [0.733, 0.800) | 90 | 0.7674 | 0.3000 | 89 | 0.7678 | 0.3034 |
| [0.800, 0.867) | 96 | 0.8302 | 0.3750 | 96 | 0.8302 | 0.3750 |
| [0.867, 0.933) | 105 | 0.9023 | 0.3429 | 105 | 0.9023 | 0.3429 |
| [0.933, 1.000) | 340 | 0.9872 | 0.1882 | 340 | 0.9872 | 0.1882 |

### B1 / qs_v1, holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.6835 | 0.6835 | 1.3265 | 1.3265 | 0.2767 | 0.2767 |
| subject_role = raw (T fallback) | 0.3178 | 0.3178 | 0.9247 | 0.9247 | 0.4412 | 0.4412 |
| category | 0.1720 | 0.2212 | 0.5562 | 0.5868 | 0.5896 | 0.5906 |
| doc_kind = raw (T fallback) | 0.2694 | 0.2694 | 0.8424 | 0.8424 | 0.5220 | 0.5220 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.533, 0.600) | 1 | 0.5946 | 0.0000 | 1 | 0.5946 | 0.0000 |
| [0.600, 0.667) | 3 | 0.6346 | 0.6667 | 3 | 0.6346 | 0.6667 |
| [0.667, 0.733) | 5 | 0.7057 | 0.6000 | 5 | 0.7057 | 0.6000 |
| [0.733, 0.800) | 11 | 0.7722 | 0.2727 | 11 | 0.7722 | 0.2727 |
| [0.800, 0.867) | 34 | 0.8389 | 0.4706 | 34 | 0.8389 | 0.4706 |
| [0.867, 0.933) | 75 | 0.9079 | 0.2800 | 75 | 0.9079 | 0.2800 |
| [0.933, 1.000) | 120 | 0.9573 | 0.0917 | 120 | 0.9573 | 0.0917 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 4 | 0.3047 | 0.0000 | 4 | 0.3047 | 0.0000 |
| [0.333, 0.400) | 15 | 0.3657 | 0.4000 | 15 | 0.3657 | 0.4000 |
| [0.400, 0.467) | 38 | 0.4355 | 0.3947 | 38 | 0.4355 | 0.3947 |
| [0.467, 0.533) | 31 | 0.4990 | 0.3871 | 31 | 0.4990 | 0.3871 |
| [0.533, 0.600) | 29 | 0.5626 | 0.2414 | 29 | 0.5626 | 0.2414 |
| [0.600, 0.667) | 26 | 0.6353 | 0.4615 | 26 | 0.6353 | 0.4615 |
| [0.667, 0.733) | 25 | 0.6981 | 0.4000 | 25 | 0.6981 | 0.4000 |
| [0.733, 0.800) | 19 | 0.7730 | 0.3684 | 19 | 0.7730 | 0.3684 |
| [0.800, 0.867) | 18 | 0.8303 | 0.3333 | 18 | 0.8303 | 0.3333 |
| [0.867, 0.933) | 16 | 0.8977 | 0.2500 | 16 | 0.8977 | 0.2500 |
| [0.933, 1.000) | 28 | 0.9676 | 0.1071 | 28 | 0.9676 | 0.1071 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 7 | 0.2413 | 0.1429 | 16 | 0.2458 | 0.4375 |
| [0.267, 0.333) | 25 | 0.3059 | 0.5600 | 61 | 0.3058 | 0.5246 |
| [0.333, 0.400) | 50 | 0.3660 | 0.5200 | 52 | 0.3621 | 0.6538 |
| [0.400, 0.467) | 36 | 0.4254 | 0.6667 | 38 | 0.4292 | 0.6579 |
| [0.467, 0.533) | 35 | 0.4999 | 0.6857 | 29 | 0.5031 | 0.7931 |
| [0.533, 0.600) | 16 | 0.5589 | 0.6250 | 22 | 0.5609 | 0.5909 |
| [0.600, 0.667) | 24 | 0.6332 | 0.8333 | 12 | 0.6402 | 0.8333 |
| [0.667, 0.733) | 20 | 0.6932 | 0.6000 | 10 | 0.6968 | 0.7000 |
| [0.733, 0.800) | 11 | 0.7594 | 0.7273 | 5 | 0.7579 | 0.2000 |
| [0.800, 0.867) | 15 | 0.8281 | 0.8000 | 2 | 0.8169 | 1.0000 |
| [0.867, 0.933) | 7 | 0.8973 | 0.2857 | 2 | 0.8868 | 1.0000 |
| [0.933, 1.000) | 3 | 0.9609 | 1.0000 | 0 | n/a | n/a |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 4 | 0.2597 | 0.0000 | 4 | 0.2597 | 0.0000 |
| [0.267, 0.333) | 12 | 0.3013 | 0.1667 | 12 | 0.3013 | 0.1667 |
| [0.333, 0.400) | 41 | 0.3704 | 0.2927 | 41 | 0.3704 | 0.2927 |
| [0.400, 0.467) | 24 | 0.4334 | 0.2500 | 24 | 0.4334 | 0.2500 |
| [0.467, 0.533) | 28 | 0.5027 | 0.4286 | 28 | 0.5027 | 0.4286 |
| [0.533, 0.600) | 21 | 0.5726 | 0.4286 | 21 | 0.5726 | 0.4286 |
| [0.600, 0.667) | 26 | 0.6338 | 0.4231 | 26 | 0.6338 | 0.4231 |
| [0.667, 0.733) | 27 | 0.7046 | 0.3333 | 27 | 0.7046 | 0.3333 |
| [0.733, 0.800) | 21 | 0.7725 | 0.3333 | 21 | 0.7725 | 0.3333 |
| [0.800, 0.867) | 21 | 0.8319 | 0.3810 | 21 | 0.8319 | 0.3810 |
| [0.867, 0.933) | 7 | 0.8842 | 0.2857 | 7 | 0.8842 | 0.2857 |
| [0.933, 1.000) | 17 | 0.9621 | 0.1765 | 17 | 0.9621 | 0.1765 |

### B1 / qs_v2, test

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.7396 | 0.7396 | 1.4105 | 1.4105 | 0.3938 | 0.3938 |
| has_phi_direct = raw (T fallback) | 0.6770 | 0.6770 | 1.2202 | 1.2202 | 0.3148 | 0.3148 |
| has_phi_quasi = raw (T fallback) | 0.6464 | 0.6464 | 1.1987 | 1.1987 | 0.3315 | 0.3315 |
| has_coded_id = raw (T fallback) | 0.6455 | 0.6455 | 1.1765 | 1.1765 | 0.3828 | 0.3828 |
| has_staff_pii = raw (T fallback) | 0.6765 | 0.6765 | 1.2332 | 1.2332 | 0.3418 | 0.3418 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 13 | 0.5181 | 0.5385 | 13 | 0.5181 | 0.5385 |
| [0.533, 0.600) | 32 | 0.5725 | 0.5312 | 32 | 0.5725 | 0.5312 |
| [0.600, 0.667) | 29 | 0.6284 | 0.3448 | 29 | 0.6284 | 0.3448 |
| [0.667, 0.733) | 56 | 0.6990 | 0.2857 | 56 | 0.6990 | 0.2857 |
| [0.733, 0.800) | 68 | 0.7697 | 0.2500 | 68 | 0.7697 | 0.2500 |
| [0.800, 0.867) | 179 | 0.8406 | 0.2123 | 179 | 0.8406 | 0.2123 |
| [0.867, 0.933) | 548 | 0.9062 | 0.1478 | 548 | 0.9062 | 0.1478 |
| [0.933, 1.000) | 994 | 0.9587 | 0.1308 | 994 | 0.9587 | 0.1308 |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 50 | 0.5175 | 0.4800 | 50 | 0.5175 | 0.4800 |
| [0.533, 0.600) | 76 | 0.5710 | 0.4211 | 76 | 0.5710 | 0.4211 |
| [0.600, 0.667) | 147 | 0.6358 | 0.2653 | 147 | 0.6358 | 0.2653 |
| [0.667, 0.733) | 168 | 0.7015 | 0.1845 | 168 | 0.7015 | 0.1845 |
| [0.733, 0.800) | 293 | 0.7716 | 0.1331 | 293 | 0.7716 | 0.1331 |
| [0.800, 0.867) | 415 | 0.8363 | 0.0819 | 415 | 0.8363 | 0.0819 |
| [0.867, 0.933) | 527 | 0.9012 | 0.0778 | 527 | 0.9012 | 0.0778 |
| [0.933, 1.000) | 243 | 0.9527 | 0.0864 | 243 | 0.9527 | 0.0864 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 34 | 0.5156 | 0.4118 | 34 | 0.5156 | 0.4118 |
| [0.533, 0.600) | 80 | 0.5648 | 0.4125 | 80 | 0.5648 | 0.4125 |
| [0.600, 0.667) | 123 | 0.6346 | 0.3496 | 123 | 0.6346 | 0.3496 |
| [0.667, 0.733) | 172 | 0.7007 | 0.3081 | 172 | 0.7007 | 0.3081 |
| [0.733, 0.800) | 232 | 0.7693 | 0.2112 | 232 | 0.7693 | 0.2112 |
| [0.800, 0.867) | 411 | 0.8367 | 0.1387 | 411 | 0.8367 | 0.1387 |
| [0.867, 0.933) | 567 | 0.9019 | 0.1093 | 567 | 0.9019 | 0.1093 |
| [0.933, 1.000) | 300 | 0.9546 | 0.1000 | 300 | 0.9546 | 0.1000 |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 34 | 0.5183 | 0.4118 | 34 | 0.5183 | 0.4118 |
| [0.533, 0.600) | 90 | 0.5686 | 0.3778 | 90 | 0.5686 | 0.3778 |
| [0.600, 0.667) | 133 | 0.6360 | 0.3158 | 133 | 0.6360 | 0.3158 |
| [0.667, 0.733) | 157 | 0.7023 | 0.2166 | 157 | 0.7023 | 0.2166 |
| [0.733, 0.800) | 287 | 0.7702 | 0.1882 | 287 | 0.7702 | 0.1882 |
| [0.800, 0.867) | 403 | 0.8351 | 0.1017 | 403 | 0.8351 | 0.1017 |
| [0.867, 0.933) | 553 | 0.9002 | 0.1392 | 553 | 0.9002 | 0.1392 |
| [0.933, 1.000) | 262 | 0.9532 | 0.1298 | 262 | 0.9532 | 0.1298 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 36 | 0.5157 | 0.4722 | 36 | 0.5157 | 0.4722 |
| [0.533, 0.600) | 86 | 0.5678 | 0.4070 | 86 | 0.5678 | 0.4070 |
| [0.600, 0.667) | 102 | 0.6357 | 0.3333 | 102 | 0.6357 | 0.3333 |
| [0.667, 0.733) | 161 | 0.7044 | 0.2112 | 161 | 0.7044 | 0.2112 |
| [0.733, 0.800) | 255 | 0.7688 | 0.1529 | 255 | 0.7688 | 0.1529 |
| [0.800, 0.867) | 401 | 0.8349 | 0.1047 | 401 | 0.8349 | 0.1047 |
| [0.867, 0.933) | 589 | 0.9018 | 0.0866 | 589 | 0.9018 | 0.0866 |
| [0.933, 1.000) | 289 | 0.9536 | 0.1142 | 289 | 0.9536 | 0.1142 |

### B1 / qs_v2, holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.6835 | 0.6835 | 1.3265 | 1.3265 | 0.2763 | 0.2763 |
| has_phi_direct = raw (T fallback) | 0.7938 | 0.7938 | 1.3651 | 1.3651 | 0.1732 | 0.1732 |
| has_phi_quasi = raw (T fallback) | 0.7630 | 0.7630 | 1.3389 | 1.3389 | 0.1172 | 0.1172 |
| has_coded_id = raw (T fallback) | 0.7749 | 0.7749 | 1.3372 | 1.3372 | 0.1895 | 0.1895 |
| has_staff_pii = raw (T fallback) | 0.5686 | 0.5686 | 1.0965 | 1.0965 | 0.3568 | 0.3568 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.533, 0.600) | 1 | 0.5946 | 0.0000 | 1 | 0.5946 | 0.0000 |
| [0.600, 0.667) | 3 | 0.6345 | 0.6667 | 3 | 0.6345 | 0.6667 |
| [0.667, 0.733) | 5 | 0.7058 | 0.6000 | 5 | 0.7058 | 0.6000 |
| [0.733, 0.800) | 11 | 0.7720 | 0.2727 | 11 | 0.7720 | 0.2727 |
| [0.800, 0.867) | 34 | 0.8389 | 0.4706 | 34 | 0.8389 | 0.4706 |
| [0.867, 0.933) | 75 | 0.9079 | 0.2800 | 75 | 0.9079 | 0.2800 |
| [0.933, 1.000) | 120 | 0.9573 | 0.0917 | 120 | 0.9573 | 0.0917 |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 5 | 0.5225 | 0.0000 | 5 | 0.5225 | 0.0000 |
| [0.533, 0.600) | 10 | 0.5694 | 0.3000 | 10 | 0.5694 | 0.3000 |
| [0.600, 0.667) | 13 | 0.6274 | 0.0000 | 13 | 0.6274 | 0.0000 |
| [0.667, 0.733) | 15 | 0.7044 | 0.1333 | 15 | 0.7044 | 0.1333 |
| [0.733, 0.800) | 41 | 0.7725 | 0.0488 | 41 | 0.7725 | 0.0488 |
| [0.800, 0.867) | 55 | 0.8349 | 0.0000 | 55 | 0.8349 | 0.0000 |
| [0.867, 0.933) | 72 | 0.8984 | 0.0139 | 72 | 0.8984 | 0.0139 |
| [0.933, 1.000) | 38 | 0.9567 | 0.0000 | 38 | 0.9567 | 0.0000 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 6 | 0.5163 | 0.6667 | 6 | 0.5163 | 0.6667 |
| [0.533, 0.600) | 13 | 0.5704 | 0.3077 | 13 | 0.5704 | 0.3077 |
| [0.600, 0.667) | 16 | 0.6290 | 0.1875 | 16 | 0.6290 | 0.1875 |
| [0.667, 0.733) | 20 | 0.7071 | 0.0000 | 20 | 0.7071 | 0.0000 |
| [0.733, 0.800) | 35 | 0.7700 | 0.0857 | 35 | 0.7700 | 0.0857 |
| [0.800, 0.867) | 44 | 0.8366 | 0.0455 | 44 | 0.8366 | 0.0455 |
| [0.867, 0.933) | 75 | 0.9001 | 0.0000 | 75 | 0.9001 | 0.0000 |
| [0.933, 1.000) | 40 | 0.9548 | 0.0000 | 40 | 0.9548 | 0.0000 |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 3 | 0.5203 | 0.0000 | 3 | 0.5203 | 0.0000 |
| [0.533, 0.600) | 15 | 0.5601 | 0.2000 | 15 | 0.5601 | 0.2000 |
| [0.600, 0.667) | 11 | 0.6295 | 0.1818 | 11 | 0.6295 | 0.1818 |
| [0.667, 0.733) | 24 | 0.7007 | 0.1667 | 24 | 0.7007 | 0.1667 |
| [0.733, 0.800) | 39 | 0.7732 | 0.0000 | 39 | 0.7732 | 0.0000 |
| [0.800, 0.867) | 44 | 0.8352 | 0.0227 | 44 | 0.8352 | 0.0227 |
| [0.867, 0.933) | 82 | 0.8991 | 0.0122 | 82 | 0.8991 | 0.0122 |
| [0.933, 1.000) | 31 | 0.9551 | 0.0000 | 31 | 0.9551 | 0.0000 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 4 | 0.5157 | 0.5000 | 4 | 0.5157 | 0.5000 |
| [0.533, 0.600) | 11 | 0.5605 | 0.4545 | 11 | 0.5605 | 0.4545 |
| [0.600, 0.667) | 9 | 0.6339 | 0.4444 | 9 | 0.6339 | 0.4444 |
| [0.667, 0.733) | 24 | 0.7001 | 0.3333 | 24 | 0.7001 | 0.3333 |
| [0.733, 0.800) | 35 | 0.7728 | 0.2571 | 35 | 0.7728 | 0.2571 |
| [0.800, 0.867) | 62 | 0.8346 | 0.3548 | 62 | 0.8346 | 0.3548 |
| [0.867, 0.933) | 71 | 0.9081 | 0.1127 | 71 | 0.9081 | 0.1127 |
| [0.933, 1.000) | 33 | 0.9572 | 0.1818 | 33 | 0.9572 | 0.1818 |

### B2 / qs_v1, test

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.6320 | 0.6320 | 1.2085 | 1.2085 | 0.4489 | 0.4489 |
| subject_role = raw (T fallback) | 0.4983 | 0.4983 | 1.1566 | 1.1566 | 0.4539 | 0.4539 |
| category | 0.1755 | 0.1189 | 0.7820 | 0.7423 | 0.4874 | 0.4812 |
| doc_kind = raw (T fallback) | 0.3836 | 0.3836 | 1.0482 | 1.0482 | 0.4546 | 0.4546 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 11 | 0.5158 | 0.5455 | 11 | 0.5158 | 0.5455 |
| [0.533, 0.600) | 17 | 0.5612 | 0.4706 | 17 | 0.5612 | 0.4706 |
| [0.600, 0.667) | 19 | 0.6279 | 0.2632 | 19 | 0.6279 | 0.2632 |
| [0.667, 0.733) | 30 | 0.6981 | 0.2667 | 30 | 0.6981 | 0.2667 |
| [0.733, 0.800) | 48 | 0.7715 | 0.3958 | 48 | 0.7715 | 0.3958 |
| [0.800, 0.867) | 136 | 0.8390 | 0.2426 | 136 | 0.8390 | 0.2426 |
| [0.867, 0.933) | 341 | 0.9047 | 0.2141 | 341 | 0.9047 | 0.2141 |
| [0.933, 1.000) | 310 | 0.9547 | 0.2452 | 310 | 0.9547 | 0.2452 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 24 | 0.3148 | 0.2917 | 24 | 0.3148 | 0.2917 |
| [0.333, 0.400) | 79 | 0.3708 | 0.2025 | 79 | 0.3708 | 0.2025 |
| [0.400, 0.467) | 119 | 0.4340 | 0.2521 | 119 | 0.4340 | 0.2521 |
| [0.467, 0.533) | 107 | 0.4997 | 0.1589 | 107 | 0.4997 | 0.1589 |
| [0.533, 0.600) | 77 | 0.5654 | 0.1169 | 77 | 0.5654 | 0.1169 |
| [0.600, 0.667) | 75 | 0.6337 | 0.0933 | 75 | 0.6337 | 0.0933 |
| [0.667, 0.733) | 77 | 0.7019 | 0.1169 | 77 | 0.7019 | 0.1169 |
| [0.733, 0.800) | 68 | 0.7657 | 0.0882 | 68 | 0.7657 | 0.0882 |
| [0.800, 0.867) | 75 | 0.8346 | 0.0667 | 75 | 0.8346 | 0.0667 |
| [0.867, 0.933) | 77 | 0.9011 | 0.1948 | 77 | 0.9011 | 0.1948 |
| [0.933, 1.000) | 134 | 0.9730 | 0.1940 | 134 | 0.9730 | 0.1940 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 15 | 0.2525 | 0.2000 | 84 | 0.2490 | 0.3095 |
| [0.267, 0.333) | 76 | 0.3067 | 0.3026 | 283 | 0.2986 | 0.4417 |
| [0.333, 0.400) | 160 | 0.3701 | 0.4562 | 246 | 0.3630 | 0.4187 |
| [0.400, 0.467) | 118 | 0.4330 | 0.4237 | 115 | 0.4286 | 0.4174 |
| [0.467, 0.533) | 143 | 0.4983 | 0.3986 | 65 | 0.4983 | 0.3846 |
| [0.533, 0.600) | 109 | 0.5666 | 0.4587 | 49 | 0.5628 | 0.2857 |
| [0.600, 0.667) | 71 | 0.6333 | 0.4085 | 31 | 0.6342 | 0.3548 |
| [0.667, 0.733) | 50 | 0.7007 | 0.4400 | 15 | 0.6980 | 0.2667 |
| [0.733, 0.800) | 42 | 0.7658 | 0.4286 | 10 | 0.7618 | 0.5000 |
| [0.800, 0.867) | 54 | 0.8314 | 0.2778 | 8 | 0.8283 | 0.2500 |
| [0.867, 0.933) | 40 | 0.9020 | 0.3000 | 5 | 0.8871 | 0.0000 |
| [0.933, 1.000) | 34 | 0.9695 | 0.3529 | 1 | 0.9688 | 1.0000 |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 8 | 0.2595 | 0.3750 | 8 | 0.2595 | 0.3750 |
| [0.267, 0.333) | 39 | 0.3059 | 0.2051 | 39 | 0.3059 | 0.2051 |
| [0.333, 0.400) | 95 | 0.3700 | 0.2947 | 95 | 0.3700 | 0.2947 |
| [0.400, 0.467) | 112 | 0.4306 | 0.3125 | 112 | 0.4306 | 0.3125 |
| [0.467, 0.533) | 103 | 0.5016 | 0.3107 | 103 | 0.5016 | 0.3107 |
| [0.533, 0.600) | 82 | 0.5648 | 0.2439 | 82 | 0.5648 | 0.2439 |
| [0.600, 0.667) | 60 | 0.6350 | 0.4000 | 60 | 0.6350 | 0.4000 |
| [0.667, 0.733) | 63 | 0.6986 | 0.3968 | 63 | 0.6986 | 0.3968 |
| [0.733, 0.800) | 44 | 0.7639 | 0.3636 | 44 | 0.7639 | 0.3636 |
| [0.800, 0.867) | 39 | 0.8329 | 0.3590 | 39 | 0.8329 | 0.3590 |
| [0.867, 0.933) | 38 | 0.9009 | 0.2105 | 38 | 0.9009 | 0.2105 |
| [0.933, 1.000) | 229 | 0.9921 | 0.1921 | 229 | 0.9921 | 0.1921 |

### B2 / qs_v1, holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.4776 | 0.4776 | 0.9494 | 0.9494 | 0.4247 | 0.4247 |
| subject_role = raw (T fallback) | 0.2480 | 0.2480 | 0.7796 | 0.7796 | 0.5201 | 0.5202 |
| category | 0.1141 | 0.2273 | 0.5552 | 0.6205 | 0.5675 | 0.5648 |
| doc_kind = raw (T fallback) | 0.2203 | 0.2203 | 0.6314 | 0.6314 | 0.4390 | 0.4390 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.600, 0.667) | 2 | 0.6289 | 1.0000 | 2 | 0.6289 | 1.0000 |
| [0.667, 0.733) | 2 | 0.6846 | 0.0000 | 2 | 0.6846 | 0.0000 |
| [0.733, 0.800) | 6 | 0.7792 | 0.5000 | 6 | 0.7792 | 0.5000 |
| [0.800, 0.867) | 21 | 0.8487 | 0.5238 | 21 | 0.8487 | 0.5238 |
| [0.867, 0.933) | 57 | 0.9049 | 0.4386 | 57 | 0.9049 | 0.4386 |
| [0.933, 1.000) | 42 | 0.9499 | 0.3571 | 42 | 0.9499 | 0.3571 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 3 | 0.3009 | 0.0000 | 3 | 0.3009 | 0.0000 |
| [0.333, 0.400) | 10 | 0.3638 | 0.3000 | 10 | 0.3638 | 0.3000 |
| [0.400, 0.467) | 20 | 0.4381 | 0.6000 | 20 | 0.4381 | 0.6000 |
| [0.467, 0.533) | 11 | 0.4904 | 0.3636 | 11 | 0.4903 | 0.3636 |
| [0.533, 0.600) | 20 | 0.5644 | 0.3000 | 20 | 0.5644 | 0.3000 |
| [0.600, 0.667) | 13 | 0.6324 | 0.4615 | 13 | 0.6324 | 0.4615 |
| [0.667, 0.733) | 8 | 0.7012 | 0.5000 | 8 | 0.7013 | 0.5000 |
| [0.733, 0.800) | 11 | 0.7628 | 0.6364 | 11 | 0.7628 | 0.6364 |
| [0.800, 0.867) | 11 | 0.8353 | 0.3636 | 11 | 0.8353 | 0.3636 |
| [0.867, 0.933) | 13 | 0.8997 | 0.6154 | 13 | 0.8997 | 0.6154 |
| [0.933, 1.000) | 10 | 0.9675 | 0.3000 | 10 | 0.9675 | 0.3000 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 1 | 0.2469 | 0.0000 | 13 | 0.2537 | 0.6154 |
| [0.267, 0.333) | 12 | 0.3098 | 0.6667 | 41 | 0.2979 | 0.5366 |
| [0.333, 0.400) | 24 | 0.3644 | 0.5000 | 36 | 0.3606 | 0.5000 |
| [0.400, 0.467) | 15 | 0.4310 | 0.6000 | 23 | 0.4363 | 0.6957 |
| [0.467, 0.533) | 24 | 0.4991 | 0.5000 | 11 | 0.4886 | 0.6364 |
| [0.533, 0.600) | 11 | 0.5571 | 0.5455 | 3 | 0.5552 | 1.0000 |
| [0.600, 0.667) | 14 | 0.6320 | 0.6429 | 3 | 0.6269 | 1.0000 |
| [0.667, 0.733) | 15 | 0.7014 | 0.5333 | 0 | n/a | n/a |
| [0.733, 0.800) | 8 | 0.7681 | 0.8750 | 0 | n/a | n/a |
| [0.800, 0.867) | 4 | 0.8366 | 1.0000 | 0 | n/a | n/a |
| [0.867, 0.933) | 2 | 0.9100 | 1.0000 | 0 | n/a | n/a |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 4 | 0.3060 | 0.7500 | 4 | 0.3060 | 0.7500 |
| [0.333, 0.400) | 12 | 0.3688 | 0.5833 | 12 | 0.3689 | 0.5833 |
| [0.400, 0.467) | 16 | 0.4362 | 0.5625 | 16 | 0.4362 | 0.5625 |
| [0.467, 0.533) | 19 | 0.5040 | 0.7895 | 19 | 0.5040 | 0.7895 |
| [0.533, 0.600) | 15 | 0.5745 | 0.4667 | 15 | 0.5745 | 0.4667 |
| [0.600, 0.667) | 12 | 0.6382 | 0.5833 | 12 | 0.6382 | 0.5833 |
| [0.667, 0.733) | 14 | 0.7020 | 0.3571 | 14 | 0.7019 | 0.3571 |
| [0.733, 0.800) | 17 | 0.7665 | 0.7059 | 17 | 0.7665 | 0.7059 |
| [0.800, 0.867) | 6 | 0.8244 | 0.5000 | 6 | 0.8244 | 0.5000 |
| [0.867, 0.933) | 9 | 0.8882 | 0.6667 | 9 | 0.8882 | 0.6667 |
| [0.933, 1.000) | 6 | 0.9615 | 0.1667 | 6 | 0.9615 | 0.1667 |

### B2 / qs_v2, test

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.6319 | 0.6319 | 1.2085 | 1.2085 | 0.4489 | 0.4489 |
| has_phi_direct = raw (T fallback) | 0.6261 | 0.6261 | 1.1137 | 1.1137 | 0.4027 | 0.4027 |
| has_phi_quasi = raw (T fallback) | 0.5768 | 0.5768 | 1.0632 | 1.0632 | 0.4188 | 0.4188 |
| has_coded_id = raw (T fallback) | 0.5635 | 0.5635 | 1.0424 | 1.0424 | 0.4384 | 0.4384 |
| has_staff_pii = raw (T fallback) | 0.5921 | 0.5921 | 1.0840 | 1.0840 | 0.4330 | 0.4330 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 11 | 0.5157 | 0.5455 | 11 | 0.5157 | 0.5455 |
| [0.533, 0.600) | 17 | 0.5611 | 0.4706 | 17 | 0.5611 | 0.4706 |
| [0.600, 0.667) | 19 | 0.6277 | 0.2632 | 19 | 0.6277 | 0.2632 |
| [0.667, 0.733) | 30 | 0.6982 | 0.2667 | 30 | 0.6982 | 0.2667 |
| [0.733, 0.800) | 48 | 0.7714 | 0.3958 | 48 | 0.7714 | 0.3958 |
| [0.800, 0.867) | 136 | 0.8390 | 0.2426 | 136 | 0.8390 | 0.2426 |
| [0.867, 0.933) | 341 | 0.9047 | 0.2141 | 341 | 0.9047 | 0.2141 |
| [0.933, 1.000) | 310 | 0.9547 | 0.2452 | 310 | 0.9547 | 0.2452 |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 25 | 0.5142 | 0.3200 | 25 | 0.5142 | 0.3200 |
| [0.533, 0.600) | 47 | 0.5652 | 0.4043 | 47 | 0.5652 | 0.4043 |
| [0.600, 0.667) | 63 | 0.6382 | 0.2540 | 63 | 0.6382 | 0.2540 |
| [0.667, 0.733) | 103 | 0.7062 | 0.2039 | 103 | 0.7062 | 0.2039 |
| [0.733, 0.800) | 174 | 0.7700 | 0.1437 | 174 | 0.7700 | 0.1437 |
| [0.800, 0.867) | 224 | 0.8332 | 0.1116 | 224 | 0.8332 | 0.1116 |
| [0.867, 0.933) | 220 | 0.8983 | 0.1136 | 220 | 0.8983 | 0.1136 |
| [0.933, 1.000) | 56 | 0.9544 | 0.2500 | 56 | 0.9544 | 0.2500 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 13 | 0.5172 | 0.5385 | 13 | 0.5172 | 0.5385 |
| [0.533, 0.600) | 45 | 0.5669 | 0.3333 | 45 | 0.5669 | 0.3333 |
| [0.600, 0.667) | 72 | 0.6330 | 0.3750 | 72 | 0.6330 | 0.3750 |
| [0.667, 0.733) | 96 | 0.7008 | 0.2917 | 96 | 0.7008 | 0.2917 |
| [0.733, 0.800) | 166 | 0.7699 | 0.1988 | 166 | 0.7699 | 0.1988 |
| [0.800, 0.867) | 210 | 0.8355 | 0.1571 | 210 | 0.8355 | 0.1571 |
| [0.867, 0.933) | 235 | 0.8974 | 0.1915 | 235 | 0.8974 | 0.1915 |
| [0.933, 1.000) | 75 | 0.9499 | 0.2267 | 75 | 0.9499 | 0.2267 |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 15 | 0.5162 | 0.4667 | 15 | 0.5162 | 0.4667 |
| [0.533, 0.600) | 52 | 0.5666 | 0.4231 | 52 | 0.5666 | 0.4231 |
| [0.600, 0.667) | 56 | 0.6372 | 0.3750 | 56 | 0.6372 | 0.3750 |
| [0.667, 0.733) | 92 | 0.7021 | 0.2283 | 92 | 0.7021 | 0.2283 |
| [0.733, 0.800) | 164 | 0.7716 | 0.2073 | 164 | 0.7716 | 0.2073 |
| [0.800, 0.867) | 244 | 0.8342 | 0.2008 | 244 | 0.8342 | 0.2008 |
| [0.867, 0.933) | 227 | 0.8956 | 0.1938 | 227 | 0.8956 | 0.1938 |
| [0.933, 1.000) | 62 | 0.9521 | 0.2903 | 62 | 0.9521 | 0.2903 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 13 | 0.5212 | 0.4615 | 13 | 0.5212 | 0.4615 |
| [0.533, 0.600) | 52 | 0.5687 | 0.4038 | 52 | 0.5687 | 0.4038 |
| [0.600, 0.667) | 56 | 0.6347 | 0.3036 | 56 | 0.6347 | 0.3036 |
| [0.667, 0.733) | 93 | 0.7022 | 0.2581 | 93 | 0.7022 | 0.2581 |
| [0.733, 0.800) | 150 | 0.7709 | 0.1933 | 150 | 0.7709 | 0.1933 |
| [0.800, 0.867) | 241 | 0.8365 | 0.1494 | 241 | 0.8365 | 0.1494 |
| [0.867, 0.933) | 239 | 0.8989 | 0.1883 | 239 | 0.8989 | 0.1883 |
| [0.933, 1.000) | 68 | 0.9525 | 0.2353 | 68 | 0.9525 | 0.2353 |

### B2 / qs_v2, holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.4776 | 0.4776 | 0.9495 | 0.9495 | 0.4245 | 0.4245 |
| has_phi_direct = raw (T fallback) | 0.7888 | 0.7888 | 1.3059 | 1.3059 | 0.0234 | 0.0234 |
| has_phi_quasi = raw (T fallback) | 0.7594 | 0.7594 | 1.2543 | 1.2543 | 0.0685 | 0.0685 |
| has_coded_id = raw (T fallback) | 0.7596 | 0.7596 | 1.2569 | 1.2569 | 0.0933 | 0.0933 |
| has_staff_pii = raw (T fallback) | 0.3500 | 0.3500 | 0.7544 | 0.7544 | 0.5031 | 0.5031 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.600, 0.667) | 2 | 0.6287 | 1.0000 | 2 | 0.6287 | 1.0000 |
| [0.667, 0.733) | 2 | 0.6846 | 0.0000 | 2 | 0.6846 | 0.0000 |
| [0.733, 0.800) | 6 | 0.7792 | 0.5000 | 6 | 0.7792 | 0.5000 |
| [0.800, 0.867) | 22 | 0.8496 | 0.5455 | 22 | 0.8496 | 0.5455 |
| [0.867, 0.933) | 56 | 0.9055 | 0.4286 | 56 | 0.9055 | 0.4286 |
| [0.933, 1.000) | 42 | 0.9498 | 0.3571 | 42 | 0.9498 | 0.3571 |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 2 | 0.5147 | 0.0000 | 2 | 0.5147 | 0.0000 |
| [0.533, 0.600) | 5 | 0.5811 | 0.4000 | 5 | 0.5811 | 0.4000 |
| [0.600, 0.667) | 5 | 0.6474 | 0.0000 | 5 | 0.6474 | 0.0000 |
| [0.667, 0.733) | 11 | 0.7050 | 0.0000 | 11 | 0.7050 | 0.0000 |
| [0.733, 0.800) | 30 | 0.7676 | 0.0000 | 30 | 0.7676 | 0.0000 |
| [0.800, 0.867) | 39 | 0.8314 | 0.0000 | 39 | 0.8314 | 0.0000 |
| [0.867, 0.933) | 33 | 0.8921 | 0.0000 | 33 | 0.8921 | 0.0000 |
| [0.933, 1.000) | 5 | 0.9439 | 0.0000 | 5 | 0.9439 | 0.0000 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 5 | 0.5167 | 0.8000 | 5 | 0.5167 | 0.8000 |
| [0.533, 0.600) | 4 | 0.5794 | 0.0000 | 4 | 0.5794 | 0.0000 |
| [0.600, 0.667) | 6 | 0.6333 | 0.1667 | 6 | 0.6333 | 0.1667 |
| [0.667, 0.733) | 18 | 0.7059 | 0.0556 | 18 | 0.7059 | 0.0556 |
| [0.733, 0.800) | 25 | 0.7696 | 0.0400 | 25 | 0.7696 | 0.0400 |
| [0.800, 0.867) | 42 | 0.8356 | 0.0000 | 42 | 0.8356 | 0.0000 |
| [0.867, 0.933) | 25 | 0.8965 | 0.0000 | 25 | 0.8965 | 0.0000 |
| [0.933, 1.000) | 5 | 0.9456 | 0.0000 | 5 | 0.9456 | 0.0000 |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 3 | 0.5108 | 0.0000 | 3 | 0.5108 | 0.0000 |
| [0.533, 0.600) | 8 | 0.5637 | 0.2500 | 8 | 0.5637 | 0.2500 |
| [0.600, 0.667) | 4 | 0.6448 | 0.2500 | 4 | 0.6448 | 0.2500 |
| [0.667, 0.733) | 16 | 0.6983 | 0.0625 | 16 | 0.6983 | 0.0625 |
| [0.733, 0.800) | 29 | 0.7650 | 0.0000 | 29 | 0.7650 | 0.0000 |
| [0.800, 0.867) | 38 | 0.8396 | 0.0000 | 38 | 0.8396 | 0.0000 |
| [0.867, 0.933) | 27 | 0.8941 | 0.0000 | 27 | 0.8941 | 0.0000 |
| [0.933, 1.000) | 5 | 0.9458 | 0.0000 | 5 | 0.9458 | 0.0000 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 4 | 0.5173 | 0.5000 | 4 | 0.5173 | 0.5000 |
| [0.533, 0.600) | 2 | 0.5692 | 0.0000 | 2 | 0.5692 | 0.0000 |
| [0.600, 0.667) | 8 | 0.6273 | 0.5000 | 8 | 0.6273 | 0.5000 |
| [0.667, 0.733) | 14 | 0.6980 | 0.1429 | 14 | 0.6980 | 0.1429 |
| [0.733, 0.800) | 31 | 0.7679 | 0.5806 | 31 | 0.7679 | 0.5806 |
| [0.800, 0.867) | 31 | 0.8347 | 0.4516 | 31 | 0.8347 | 0.4516 |
| [0.867, 0.933) | 39 | 0.8935 | 0.4615 | 39 | 0.8935 | 0.4615 |
| [0.933, 1.000) | 1 | 0.9694 | 0.0000 | 1 | 0.9694 | 0.0000 |

### B3 / qs_v1 (doc-level, underpowered), test

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.4515 | 0.4515 | 0.9130 | 0.9130 | 0.4989 | 0.4989 |
| subject_role = raw (T fallback) | 0.4808 | 0.4808 | 1.1118 | 1.1118 | 0.5613 | 0.5613 |
| category | 0.1981 | 0.0964 | 0.8325 | 0.7615 | 0.5344 | 0.5267 |
| doc_kind = raw (T fallback) | 0.4468 | 0.4468 | 1.1282 | 1.1282 | 0.4213 | 0.4213 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 10 | 0.5166 | 0.2000 | 10 | 0.5166 | 0.2000 |
| [0.533, 0.600) | 11 | 0.5643 | 0.5455 | 11 | 0.5643 | 0.5455 |
| [0.600, 0.667) | 11 | 0.6290 | 0.3636 | 11 | 0.6290 | 0.3636 |
| [0.667, 0.733) | 19 | 0.7044 | 0.3158 | 19 | 0.7044 | 0.3158 |
| [0.733, 0.800) | 43 | 0.7712 | 0.6279 | 43 | 0.7712 | 0.6279 |
| [0.800, 0.867) | 100 | 0.8383 | 0.3600 | 100 | 0.8383 | 0.3600 |
| [0.867, 0.933) | 186 | 0.9028 | 0.3978 | 186 | 0.9028 | 0.3978 |
| [0.933, 1.000) | 145 | 0.9548 | 0.4345 | 145 | 0.9548 | 0.4345 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 14 | 0.3098 | 0.2857 | 14 | 0.3098 | 0.2857 |
| [0.333, 0.400) | 35 | 0.3751 | 0.1714 | 35 | 0.3751 | 0.1714 |
| [0.400, 0.467) | 54 | 0.4333 | 0.1852 | 54 | 0.4333 | 0.1852 |
| [0.467, 0.533) | 48 | 0.4957 | 0.1667 | 48 | 0.4957 | 0.1667 |
| [0.533, 0.600) | 51 | 0.5651 | 0.1569 | 51 | 0.5651 | 0.1569 |
| [0.600, 0.667) | 47 | 0.6317 | 0.2128 | 47 | 0.6317 | 0.2128 |
| [0.667, 0.733) | 52 | 0.6979 | 0.2115 | 52 | 0.6979 | 0.2115 |
| [0.733, 0.800) | 36 | 0.7660 | 0.1111 | 36 | 0.7660 | 0.1111 |
| [0.800, 0.867) | 44 | 0.8353 | 0.0682 | 44 | 0.8353 | 0.0682 |
| [0.867, 0.933) | 62 | 0.8992 | 0.2419 | 62 | 0.8992 | 0.2419 |
| [0.933, 1.000) | 82 | 0.9741 | 0.3415 | 82 | 0.9741 | 0.3415 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 6 | 0.2561 | 0.0000 | 174 | 0.2461 | 0.3333 |
| [0.267, 0.333) | 54 | 0.3052 | 0.2407 | 191 | 0.2950 | 0.4136 |
| [0.333, 0.400) | 80 | 0.3714 | 0.3375 | 76 | 0.3619 | 0.3947 |
| [0.400, 0.467) | 73 | 0.4338 | 0.4658 | 47 | 0.4255 | 0.4043 |
| [0.467, 0.533) | 65 | 0.5045 | 0.4154 | 21 | 0.4880 | 0.3333 |
| [0.533, 0.600) | 53 | 0.5610 | 0.3962 | 10 | 0.5663 | 0.2000 |
| [0.600, 0.667) | 34 | 0.6390 | 0.4118 | 5 | 0.6413 | 0.2000 |
| [0.667, 0.733) | 34 | 0.6999 | 0.3824 | 0 | n/a | n/a |
| [0.733, 0.800) | 26 | 0.7552 | 0.4615 | 0 | n/a | n/a |
| [0.800, 0.867) | 36 | 0.8303 | 0.3333 | 1 | 0.8252 | 1.0000 |
| [0.867, 0.933) | 34 | 0.8953 | 0.4118 | 0 | n/a | n/a |
| [0.933, 1.000) | 30 | 0.9650 | 0.3333 | 0 | n/a | n/a |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 8 | 0.2602 | 0.2500 | 8 | 0.2602 | 0.2500 |
| [0.267, 0.333) | 15 | 0.3105 | 0.2000 | 15 | 0.3105 | 0.2000 |
| [0.333, 0.400) | 32 | 0.3720 | 0.2188 | 32 | 0.3720 | 0.2188 |
| [0.400, 0.467) | 59 | 0.4303 | 0.4068 | 59 | 0.4303 | 0.4068 |
| [0.467, 0.533) | 47 | 0.5001 | 0.2340 | 47 | 0.5001 | 0.2340 |
| [0.533, 0.600) | 38 | 0.5619 | 0.3421 | 38 | 0.5619 | 0.3421 |
| [0.600, 0.667) | 38 | 0.6338 | 0.3158 | 38 | 0.6338 | 0.3158 |
| [0.667, 0.733) | 30 | 0.6956 | 0.4667 | 30 | 0.6956 | 0.4667 |
| [0.733, 0.800) | 21 | 0.7632 | 0.4286 | 21 | 0.7632 | 0.4286 |
| [0.800, 0.867) | 16 | 0.8291 | 0.5000 | 16 | 0.8291 | 0.5000 |
| [0.867, 0.933) | 26 | 0.9061 | 0.2308 | 26 | 0.9061 | 0.2308 |
| [0.933, 1.000) | 195 | 0.9942 | 0.1897 | 195 | 0.9942 | 0.1897 |

### B3 / qs_v1 (doc-level, underpowered), holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.2508 | 0.2508 | 0.5518 | 0.5518 | 0.5300 | 0.5300 |
| subject_role = raw (T fallback) | 0.1832 | 0.1832 | 0.5996 | 0.5996 | 0.5530 | 0.5532 |
| category | 0.1896 | 0.3650 | 0.5023 | 0.6737 | 0.6401 | 0.6414 |
| doc_kind = raw (T fallback) | 0.1700 | 0.1700 | 0.4780 | 0.4780 | 0.5525 | 0.5525 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.600, 0.667) | 2 | 0.6289 | 1.0000 | 2 | 0.6289 | 1.0000 |
| [0.667, 0.733) | 2 | 0.7118 | 0.5000 | 2 | 0.7118 | 0.5000 |
| [0.733, 0.800) | 3 | 0.7680 | 1.0000 | 3 | 0.7680 | 1.0000 |
| [0.800, 0.867) | 18 | 0.8435 | 0.6111 | 18 | 0.8435 | 0.6111 |
| [0.867, 0.933) | 41 | 0.9022 | 0.5854 | 41 | 0.9022 | 0.5854 |
| [0.933, 1.000) | 18 | 0.9461 | 0.8333 | 18 | 0.9461 | 0.8333 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 3 | 0.3073 | 0.3333 | 3 | 0.3073 | 0.3333 |
| [0.333, 0.400) | 5 | 0.3736 | 0.4000 | 5 | 0.3736 | 0.4000 |
| [0.400, 0.467) | 9 | 0.4335 | 0.6667 | 9 | 0.4335 | 0.6667 |
| [0.467, 0.533) | 9 | 0.4927 | 0.6667 | 9 | 0.4926 | 0.6667 |
| [0.533, 0.600) | 13 | 0.5643 | 0.3846 | 13 | 0.5643 | 0.3846 |
| [0.600, 0.667) | 7 | 0.6217 | 0.7143 | 7 | 0.6217 | 0.7143 |
| [0.667, 0.733) | 7 | 0.6993 | 0.2857 | 7 | 0.6993 | 0.2857 |
| [0.733, 0.800) | 9 | 0.7610 | 0.7778 | 9 | 0.7610 | 0.7778 |
| [0.800, 0.867) | 9 | 0.8297 | 0.6667 | 9 | 0.8297 | 0.6667 |
| [0.867, 0.933) | 9 | 0.9064 | 0.6667 | 9 | 0.9064 | 0.6667 |
| [0.933, 1.000) | 4 | 0.9645 | 0.5000 | 4 | 0.9645 | 0.5000 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 1 | 0.2469 | 0.0000 | 31 | 0.2478 | 0.5161 |
| [0.267, 0.333) | 8 | 0.3125 | 0.6250 | 37 | 0.2915 | 0.7027 |
| [0.333, 0.400) | 17 | 0.3738 | 0.4706 | 14 | 0.3557 | 0.7857 |
| [0.400, 0.467) | 9 | 0.4333 | 0.6667 | 2 | 0.4456 | 1.0000 |
| [0.467, 0.533) | 19 | 0.4980 | 0.7368 | 0 | n/a | n/a |
| [0.533, 0.600) | 7 | 0.5563 | 0.4286 | 0 | n/a | n/a |
| [0.600, 0.667) | 6 | 0.6353 | 0.8333 | 0 | n/a | n/a |
| [0.667, 0.733) | 7 | 0.6944 | 0.5714 | 0 | n/a | n/a |
| [0.733, 0.800) | 6 | 0.7635 | 1.0000 | 0 | n/a | n/a |
| [0.800, 0.867) | 2 | 0.8216 | 1.0000 | 0 | n/a | n/a |
| [0.867, 0.933) | 2 | 0.9100 | 1.0000 | 0 | n/a | n/a |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 3 | 0.3058 | 0.6667 | 3 | 0.3058 | 0.6667 |
| [0.333, 0.400) | 13 | 0.3782 | 0.6923 | 13 | 0.3782 | 0.6923 |
| [0.400, 0.467) | 13 | 0.4362 | 0.5385 | 13 | 0.4362 | 0.5385 |
| [0.467, 0.533) | 4 | 0.4968 | 0.7500 | 4 | 0.4968 | 0.7500 |
| [0.533, 0.600) | 13 | 0.5715 | 0.6923 | 13 | 0.5715 | 0.6923 |
| [0.600, 0.667) | 9 | 0.6322 | 0.8889 | 9 | 0.6322 | 0.8889 |
| [0.667, 0.733) | 6 | 0.6931 | 0.6667 | 6 | 0.6931 | 0.6667 |
| [0.733, 0.800) | 8 | 0.7753 | 0.7500 | 8 | 0.7753 | 0.7500 |
| [0.800, 0.867) | 7 | 0.8300 | 0.8571 | 7 | 0.8300 | 0.8571 |
| [0.867, 0.933) | 5 | 0.8901 | 0.8000 | 5 | 0.8901 | 0.8000 |
| [0.933, 1.000) | 3 | 0.9619 | 0.3333 | 3 | 0.9619 | 0.3333 |

### B3 / qs_v2 (doc-level, underpowered), test

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.4515 | 0.4515 | 0.9131 | 0.9131 | 0.4988 | 0.4988 |
| has_phi_direct = raw (T fallback) | 0.5272 | 0.5272 | 0.9852 | 0.9852 | 0.4232 | 0.4232 |
| has_phi_quasi = raw (T fallback) | 0.4465 | 0.4465 | 0.8765 | 0.8765 | 0.4605 | 0.4605 |
| has_coded_id = raw (T fallback) | 0.4299 | 0.4299 | 0.8596 | 0.8596 | 0.4912 | 0.4912 |
| has_staff_pii = raw (T fallback) | 0.4591 | 0.4591 | 0.8997 | 0.8997 | 0.4471 | 0.4471 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 10 | 0.5166 | 0.2000 | 10 | 0.5166 | 0.2000 |
| [0.533, 0.600) | 11 | 0.5641 | 0.5455 | 11 | 0.5641 | 0.5455 |
| [0.600, 0.667) | 11 | 0.6289 | 0.3636 | 11 | 0.6289 | 0.3636 |
| [0.667, 0.733) | 19 | 0.7046 | 0.3158 | 19 | 0.7046 | 0.3158 |
| [0.733, 0.800) | 43 | 0.7712 | 0.6279 | 43 | 0.7712 | 0.6279 |
| [0.800, 0.867) | 100 | 0.8383 | 0.3600 | 100 | 0.8383 | 0.3600 |
| [0.867, 0.933) | 186 | 0.9028 | 0.3978 | 186 | 0.9028 | 0.3978 |
| [0.933, 1.000) | 145 | 0.9548 | 0.4345 | 145 | 0.9548 | 0.4345 |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 17 | 0.5217 | 0.5294 | 17 | 0.5217 | 0.5294 |
| [0.533, 0.600) | 33 | 0.5635 | 0.3939 | 33 | 0.5635 | 0.3939 |
| [0.600, 0.667) | 52 | 0.6349 | 0.3462 | 52 | 0.6349 | 0.3462 |
| [0.667, 0.733) | 66 | 0.7055 | 0.2727 | 66 | 0.7055 | 0.2727 |
| [0.733, 0.800) | 106 | 0.7671 | 0.2075 | 106 | 0.7671 | 0.2075 |
| [0.800, 0.867) | 117 | 0.8359 | 0.1880 | 117 | 0.8359 | 0.1880 |
| [0.867, 0.933) | 100 | 0.8986 | 0.1900 | 100 | 0.8986 | 0.1900 |
| [0.933, 1.000) | 34 | 0.9560 | 0.3235 | 34 | 0.9560 | 0.3235 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 17 | 0.5182 | 0.6471 | 17 | 0.5182 | 0.6471 |
| [0.533, 0.600) | 30 | 0.5650 | 0.3333 | 30 | 0.5650 | 0.3333 |
| [0.600, 0.667) | 52 | 0.6337 | 0.5000 | 52 | 0.6337 | 0.5000 |
| [0.667, 0.733) | 71 | 0.7005 | 0.3099 | 71 | 0.7005 | 0.3099 |
| [0.733, 0.800) | 95 | 0.7680 | 0.2211 | 95 | 0.7680 | 0.2211 |
| [0.800, 0.867) | 129 | 0.8341 | 0.3488 | 129 | 0.8341 | 0.3488 |
| [0.867, 0.933) | 103 | 0.8956 | 0.3010 | 103 | 0.8956 | 0.3010 |
| [0.933, 1.000) | 28 | 0.9559 | 0.4286 | 28 | 0.9559 | 0.4286 |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 15 | 0.5193 | 0.5333 | 15 | 0.5193 | 0.5333 |
| [0.533, 0.600) | 40 | 0.5627 | 0.4250 | 40 | 0.5627 | 0.4250 |
| [0.600, 0.667) | 38 | 0.6363 | 0.3421 | 38 | 0.6363 | 0.3421 |
| [0.667, 0.733) | 61 | 0.7053 | 0.3443 | 61 | 0.7053 | 0.3443 |
| [0.733, 0.800) | 111 | 0.7705 | 0.3333 | 111 | 0.7705 | 0.3333 |
| [0.800, 0.867) | 117 | 0.8384 | 0.3248 | 117 | 0.8384 | 0.3248 |
| [0.867, 0.933) | 107 | 0.8954 | 0.3458 | 107 | 0.8954 | 0.3458 |
| [0.933, 1.000) | 36 | 0.9547 | 0.4167 | 36 | 0.9547 | 0.4167 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 13 | 0.5141 | 0.7692 | 13 | 0.5141 | 0.7692 |
| [0.533, 0.600) | 41 | 0.5664 | 0.5122 | 41 | 0.5664 | 0.5122 |
| [0.600, 0.667) | 42 | 0.6376 | 0.5000 | 42 | 0.6376 | 0.5000 |
| [0.667, 0.733) | 63 | 0.7052 | 0.2381 | 63 | 0.7052 | 0.2381 |
| [0.733, 0.800) | 103 | 0.7674 | 0.2427 | 103 | 0.7674 | 0.2427 |
| [0.800, 0.867) | 121 | 0.8334 | 0.3306 | 121 | 0.8334 | 0.3306 |
| [0.867, 0.933) | 109 | 0.8978 | 0.3028 | 109 | 0.8978 | 0.3028 |
| [0.933, 1.000) | 33 | 0.9565 | 0.3333 | 33 | 0.9565 | 0.3333 |

### B3 / qs_v2 (doc-level, underpowered), holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present = raw (T fallback) | 0.2508 | 0.2508 | 0.5519 | 0.5519 | 0.5290 | 0.5290 |
| has_phi_direct = raw (T fallback) | 0.7846 | 0.7846 | 1.2818 | 1.2818 | 0.0482 | 0.0482 |
| has_phi_quasi = raw (T fallback) | 0.7522 | 0.7522 | 1.2230 | 1.2230 | 0.0041 | 0.0041 |
| has_coded_id = raw (T fallback) | 0.7657 | 0.7657 | 1.2567 | 1.2567 | 0.0366 | 0.0366 |
| has_staff_pii = raw (T fallback) | 0.1310 | 0.1310 | 0.4420 | 0.4420 | 0.6319 | 0.6319 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.600, 0.667) | 2 | 0.6287 | 1.0000 | 2 | 0.6287 | 1.0000 |
| [0.667, 0.733) | 2 | 0.7118 | 0.5000 | 2 | 0.7118 | 0.5000 |
| [0.733, 0.800) | 3 | 0.7680 | 1.0000 | 3 | 0.7680 | 1.0000 |
| [0.800, 0.867) | 19 | 0.8448 | 0.6316 | 19 | 0.8448 | 0.6316 |
| [0.867, 0.933) | 40 | 0.9030 | 0.5750 | 40 | 0.9030 | 0.5750 |
| [0.933, 1.000) | 18 | 0.9461 | 0.8333 | 18 | 0.9461 | 0.8333 |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 2 | 0.5147 | 0.0000 | 2 | 0.5147 | 0.0000 |
| [0.533, 0.600) | 3 | 0.5841 | 0.3333 | 3 | 0.5841 | 0.3333 |
| [0.600, 0.667) | 3 | 0.6550 | 0.0000 | 3 | 0.6550 | 0.0000 |
| [0.667, 0.733) | 7 | 0.7123 | 0.0000 | 7 | 0.7123 | 0.0000 |
| [0.733, 0.800) | 26 | 0.7652 | 0.0000 | 26 | 0.7652 | 0.0000 |
| [0.800, 0.867) | 22 | 0.8342 | 0.0000 | 22 | 0.8342 | 0.0000 |
| [0.867, 0.933) | 18 | 0.8933 | 0.0000 | 18 | 0.8933 | 0.0000 |
| [0.933, 1.000) | 3 | 0.9480 | 0.0000 | 3 | 0.9480 | 0.0000 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 3 | 0.5120 | 0.6667 | 3 | 0.5120 | 0.6667 |
| [0.533, 0.600) | 3 | 0.5696 | 0.3333 | 3 | 0.5696 | 0.3333 |
| [0.600, 0.667) | 3 | 0.6460 | 0.0000 | 3 | 0.6460 | 0.0000 |
| [0.667, 0.733) | 16 | 0.7034 | 0.0000 | 16 | 0.7034 | 0.0000 |
| [0.733, 0.800) | 21 | 0.7727 | 0.0000 | 21 | 0.7727 | 0.0000 |
| [0.800, 0.867) | 25 | 0.8362 | 0.0000 | 25 | 0.8362 | 0.0000 |
| [0.867, 0.933) | 11 | 0.8910 | 0.0000 | 11 | 0.8910 | 0.0000 |
| [0.933, 1.000) | 2 | 0.9424 | 0.0000 | 2 | 0.9424 | 0.0000 |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 1 | 0.5093 | 0.0000 | 1 | 0.5093 | 0.0000 |
| [0.533, 0.600) | 4 | 0.5716 | 0.5000 | 4 | 0.5716 | 0.5000 |
| [0.600, 0.667) | 3 | 0.6390 | 0.0000 | 3 | 0.6390 | 0.0000 |
| [0.667, 0.733) | 12 | 0.6993 | 0.0000 | 12 | 0.6993 | 0.0000 |
| [0.733, 0.800) | 23 | 0.7719 | 0.0000 | 23 | 0.7719 | 0.0000 |
| [0.800, 0.867) | 23 | 0.8350 | 0.0000 | 23 | 0.8350 | 0.0000 |
| [0.867, 0.933) | 16 | 0.8977 | 0.0000 | 16 | 0.8977 | 0.0000 |
| [0.933, 1.000) | 2 | 0.9462 | 0.0000 | 2 | 0.9462 | 0.0000 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 1 | 0.5244 | 0.0000 | 1 | 0.5244 | 0.0000 |
| [0.533, 0.600) | 3 | 0.5613 | 0.3333 | 3 | 0.5613 | 0.3333 |
| [0.600, 0.667) | 5 | 0.6293 | 0.8000 | 5 | 0.6293 | 0.8000 |
| [0.667, 0.733) | 10 | 0.7082 | 0.5000 | 10 | 0.7082 | 0.5000 |
| [0.733, 0.800) | 25 | 0.7683 | 0.6000 | 25 | 0.7683 | 0.6000 |
| [0.800, 0.867) | 20 | 0.8344 | 0.8000 | 20 | 0.8344 | 0.8000 |
| [0.867, 0.933) | 20 | 0.8983 | 0.8000 | 20 | 0.8983 | 0.8000 |

### B4 / qs_v1 (doc-level, underpowered), test

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.2521 | 0.0659 | 0.6039 | 0.4789 | 0.5199 | 0.5199 |
| subject_role | 0.4532 | 0.0335 | 1.0941 | 0.7508 | 0.5246 | 0.5288 |
| category | 0.2893 | 0.0468 | 0.9526 | 0.7930 | 0.5274 | 0.5139 |
| doc_kind = raw (T fallback) | 0.5522 | 0.5522 | 1.2802 | 1.2802 | 0.3731 | 0.3728 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 9 | 0.5153 | 0.2222 | 24 | 0.5137 | 0.4167 |
| [0.533, 0.600) | 10 | 0.5613 | 0.5000 | 91 | 0.5765 | 0.6703 |
| [0.600, 0.667) | 9 | 0.6260 | 0.5556 | 159 | 0.6340 | 0.5849 |
| [0.667, 0.733) | 17 | 0.6994 | 0.4118 | 60 | 0.6884 | 0.6500 |
| [0.733, 0.800) | 37 | 0.7706 | 0.8108 | 3 | 0.7410 | 0.3333 |
| [0.800, 0.867) | 68 | 0.8361 | 0.6324 | 0 | n/a | n/a |
| [0.867, 0.933) | 109 | 0.9028 | 0.5505 | 0 | n/a | n/a |
| [0.933, 1.000) | 78 | 0.9544 | 0.6667 | 0 | n/a | n/a |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 0 | n/a | n/a | 122 | 0.2612 | 0.2623 |
| [0.267, 0.333) | 5 | 0.3173 | 0.4000 | 208 | 0.2847 | 0.2356 |
| [0.333, 0.400) | 25 | 0.3728 | 0.3600 | 5 | 0.3507 | 0.2000 |
| [0.400, 0.467) | 32 | 0.4355 | 0.2188 | 2 | 0.4086 | 0.5000 |
| [0.467, 0.533) | 33 | 0.4988 | 0.2121 | 0 | n/a | n/a |
| [0.533, 0.600) | 32 | 0.5670 | 0.1250 | 0 | n/a | n/a |
| [0.600, 0.667) | 30 | 0.6326 | 0.2333 | 0 | n/a | n/a |
| [0.667, 0.733) | 29 | 0.6996 | 0.2759 | 0 | n/a | n/a |
| [0.733, 0.800) | 22 | 0.7688 | 0.1364 | 0 | n/a | n/a |
| [0.800, 0.867) | 28 | 0.8391 | 0.1071 | 0 | n/a | n/a |
| [0.867, 0.933) | 37 | 0.8996 | 0.2973 | 0 | n/a | n/a |
| [0.933, 1.000) | 64 | 0.9767 | 0.3438 | 0 | n/a | n/a |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 6 | 0.2551 | 0.1667 | 273 | 0.2310 | 0.2821 |
| [0.267, 0.333) | 36 | 0.3049 | 0.1389 | 58 | 0.2854 | 0.2759 |
| [0.333, 0.400) | 51 | 0.3707 | 0.2941 | 5 | 0.3448 | 0.2000 |
| [0.400, 0.467) | 42 | 0.4337 | 0.3571 | 1 | 0.4480 | 1.0000 |
| [0.467, 0.533) | 39 | 0.5030 | 0.3590 | 0 | n/a | n/a |
| [0.533, 0.600) | 31 | 0.5654 | 0.2258 | 0 | n/a | n/a |
| [0.600, 0.667) | 25 | 0.6385 | 0.2800 | 0 | n/a | n/a |
| [0.667, 0.733) | 19 | 0.7037 | 0.2632 | 0 | n/a | n/a |
| [0.733, 0.800) | 16 | 0.7572 | 0.3125 | 0 | n/a | n/a |
| [0.800, 0.867) | 28 | 0.8345 | 0.3214 | 0 | n/a | n/a |
| [0.867, 0.933) | 23 | 0.8981 | 0.2174 | 0 | n/a | n/a |
| [0.933, 1.000) | 21 | 0.9648 | 0.3333 | 0 | n/a | n/a |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 4 | 0.2609 | 0.2500 | 4 | 0.2609 | 0.2500 |
| [0.267, 0.333) | 7 | 0.3058 | 0.1429 | 7 | 0.3058 | 0.1429 |
| [0.333, 0.400) | 20 | 0.3732 | 0.2500 | 20 | 0.3732 | 0.2500 |
| [0.400, 0.467) | 19 | 0.4233 | 0.3158 | 19 | 0.4233 | 0.3158 |
| [0.467, 0.533) | 19 | 0.5030 | 0.2632 | 19 | 0.5030 | 0.2632 |
| [0.533, 0.600) | 22 | 0.5622 | 0.4091 | 22 | 0.5622 | 0.4091 |
| [0.600, 0.667) | 19 | 0.6279 | 0.4737 | 19 | 0.6278 | 0.4737 |
| [0.667, 0.733) | 12 | 0.7007 | 0.5000 | 12 | 0.7007 | 0.5000 |
| [0.733, 0.800) | 11 | 0.7694 | 0.2727 | 11 | 0.7694 | 0.2727 |
| [0.800, 0.867) | 5 | 0.8369 | 0.6000 | 5 | 0.8368 | 0.6000 |
| [0.867, 0.933) | 15 | 0.9074 | 0.1333 | 15 | 0.9074 | 0.1333 |
| [0.933, 1.000) | 184 | 0.9939 | 0.1848 | 184 | 0.9939 | 0.1848 |

### B4 / qs_v1 (doc-level, underpowered), holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.2249 | 0.0687 | 0.4974 | 0.4297 | 0.5432 | 0.5432 |
| subject_role | 0.1897 | 0.3300 | 0.5791 | 0.7272 | 0.5482 | 0.5404 |
| category | 0.1860 | 0.4063 | 0.5218 | 0.7530 | 0.6193 | 0.6193 |
| doc_kind = raw (T fallback) | 0.1858 | 0.1858 | 0.4582 | 0.4581 | 0.5690 | 0.5690 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 0 | n/a | n/a | 1 | 0.5284 | 1.0000 |
| [0.533, 0.600) | 0 | n/a | n/a | 11 | 0.5787 | 0.7273 |
| [0.600, 0.667) | 2 | 0.6289 | 1.0000 | 57 | 0.6345 | 0.6491 |
| [0.667, 0.733) | 1 | 0.7082 | 0.0000 | 11 | 0.6765 | 0.9091 |
| [0.733, 0.800) | 4 | 0.7651 | 1.0000 | 0 | n/a | n/a |
| [0.800, 0.867) | 16 | 0.8429 | 0.6250 | 0 | n/a | n/a |
| [0.867, 0.933) | 41 | 0.9025 | 0.6341 | 0 | n/a | n/a |
| [0.933, 1.000) | 16 | 0.9447 | 0.8750 | 0 | n/a | n/a |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 0 | n/a | n/a | 39 | 0.2615 | 0.5897 |
| [0.267, 0.333) | 3 | 0.3073 | 0.3333 | 41 | 0.2781 | 0.6098 |
| [0.333, 0.400) | 5 | 0.3736 | 0.4000 | 0 | n/a | n/a |
| [0.400, 0.467) | 8 | 0.4330 | 0.7500 | 0 | n/a | n/a |
| [0.467, 0.533) | 8 | 0.4911 | 0.7500 | 0 | n/a | n/a |
| [0.533, 0.600) | 12 | 0.5653 | 0.4167 | 0 | n/a | n/a |
| [0.600, 0.667) | 7 | 0.6217 | 0.7143 | 0 | n/a | n/a |
| [0.667, 0.733) | 7 | 0.6925 | 0.2857 | 0 | n/a | n/a |
| [0.733, 0.800) | 10 | 0.7640 | 0.8000 | 0 | n/a | n/a |
| [0.800, 0.867) | 8 | 0.8279 | 0.6250 | 0 | n/a | n/a |
| [0.867, 0.933) | 8 | 0.9051 | 0.7500 | 0 | n/a | n/a |
| [0.933, 1.000) | 4 | 0.9645 | 0.5000 | 0 | n/a | n/a |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 1 | 0.2469 | 0.0000 | 79 | 0.2305 | 0.6329 |
| [0.267, 0.333) | 8 | 0.3125 | 0.6250 | 1 | 0.2850 | 1.0000 |
| [0.333, 0.400) | 17 | 0.3738 | 0.4706 | 0 | n/a | n/a |
| [0.400, 0.467) | 10 | 0.4346 | 0.7000 | 0 | n/a | n/a |
| [0.467, 0.533) | 17 | 0.4988 | 0.7059 | 0 | n/a | n/a |
| [0.533, 0.600) | 7 | 0.5563 | 0.4286 | 0 | n/a | n/a |
| [0.600, 0.667) | 6 | 0.6353 | 0.8333 | 0 | n/a | n/a |
| [0.667, 0.733) | 7 | 0.6966 | 0.5714 | 0 | n/a | n/a |
| [0.733, 0.800) | 3 | 0.7571 | 1.0000 | 0 | n/a | n/a |
| [0.800, 0.867) | 3 | 0.8168 | 1.0000 | 0 | n/a | n/a |
| [0.867, 0.933) | 1 | 0.9210 | 1.0000 | 0 | n/a | n/a |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.267, 0.333) | 3 | 0.3058 | 0.6667 | 3 | 0.3058 | 0.6667 |
| [0.333, 0.400) | 12 | 0.3779 | 0.6667 | 12 | 0.3779 | 0.6667 |
| [0.400, 0.467) | 12 | 0.4374 | 0.5833 | 12 | 0.4374 | 0.5833 |
| [0.467, 0.533) | 4 | 0.4968 | 0.7500 | 4 | 0.4968 | 0.7500 |
| [0.533, 0.600) | 13 | 0.5715 | 0.6923 | 13 | 0.5715 | 0.6923 |
| [0.600, 0.667) | 9 | 0.6339 | 1.0000 | 9 | 0.6339 | 1.0000 |
| [0.667, 0.733) | 4 | 0.6846 | 0.7500 | 4 | 0.6846 | 0.7500 |
| [0.733, 0.800) | 8 | 0.7737 | 0.7500 | 8 | 0.7737 | 0.7500 |
| [0.800, 0.867) | 6 | 0.8279 | 0.8333 | 6 | 0.8279 | 0.8333 |
| [0.867, 0.933) | 6 | 0.8866 | 0.8333 | 6 | 0.8866 | 0.8333 |
| [0.933, 1.000) | 3 | 0.9619 | 0.3333 | 3 | 0.9619 | 0.3333 |

### B4 / qs_v2 (doc-level, underpowered), test

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.2521 | 0.0659 | 0.6039 | 0.4789 | 0.5199 | 0.5199 |
| has_phi_direct = raw (T fallback) | 0.4060 | 0.4060 | 0.8671 | 0.8671 | 0.3718 | 0.3718 |
| has_phi_quasi | 0.3029 | 0.0341 | 0.7127 | 0.5044 | 0.4393 | 0.4393 |
| has_coded_id = raw (T fallback) | 0.2755 | 0.2755 | 0.6793 | 0.6793 | 0.4517 | 0.4517 |
| has_staff_pii = raw (T fallback) | 0.3293 | 0.3293 | 0.7361 | 0.7361 | 0.4589 | 0.4589 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 9 | 0.5153 | 0.2222 | 24 | 0.5137 | 0.4167 |
| [0.533, 0.600) | 10 | 0.5613 | 0.5000 | 91 | 0.5765 | 0.6703 |
| [0.600, 0.667) | 9 | 0.6258 | 0.5556 | 160 | 0.6342 | 0.5813 |
| [0.667, 0.733) | 17 | 0.6995 | 0.4118 | 59 | 0.6887 | 0.6610 |
| [0.733, 0.800) | 37 | 0.7705 | 0.8108 | 3 | 0.7410 | 0.3333 |
| [0.800, 0.867) | 68 | 0.8361 | 0.6324 | 0 | n/a | n/a |
| [0.867, 0.933) | 109 | 0.9028 | 0.5505 | 0 | n/a | n/a |
| [0.933, 1.000) | 78 | 0.9544 | 0.6667 | 0 | n/a | n/a |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 12 | 0.5204 | 0.5833 | 12 | 0.5204 | 0.5833 |
| [0.533, 0.600) | 21 | 0.5673 | 0.5238 | 21 | 0.5673 | 0.5238 |
| [0.600, 0.667) | 35 | 0.6350 | 0.5714 | 35 | 0.6350 | 0.5714 |
| [0.667, 0.733) | 46 | 0.7038 | 0.4783 | 46 | 0.7038 | 0.4783 |
| [0.733, 0.800) | 67 | 0.7693 | 0.3433 | 67 | 0.7693 | 0.3433 |
| [0.800, 0.867) | 77 | 0.8388 | 0.2597 | 77 | 0.8388 | 0.2597 |
| [0.867, 0.933) | 55 | 0.8991 | 0.2364 | 55 | 0.8991 | 0.2364 |
| [0.933, 1.000) | 24 | 0.9573 | 0.4167 | 24 | 0.9573 | 0.4167 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 12 | 0.5166 | 0.7500 | 292 | 0.5176 | 0.4863 |
| [0.533, 0.600) | 22 | 0.5647 | 0.4091 | 45 | 0.5415 | 0.4889 |
| [0.600, 0.667) | 37 | 0.6335 | 0.6486 | 0 | n/a | n/a |
| [0.667, 0.733) | 43 | 0.6989 | 0.5581 | 0 | n/a | n/a |
| [0.733, 0.800) | 67 | 0.7663 | 0.4179 | 0 | n/a | n/a |
| [0.800, 0.867) | 79 | 0.8324 | 0.4304 | 0 | n/a | n/a |
| [0.867, 0.933) | 59 | 0.8970 | 0.4576 | 0 | n/a | n/a |
| [0.933, 1.000) | 18 | 0.9558 | 0.5000 | 0 | n/a | n/a |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 7 | 0.5173 | 0.7143 | 7 | 0.5173 | 0.7143 |
| [0.533, 0.600) | 30 | 0.5680 | 0.4667 | 30 | 0.5680 | 0.4667 |
| [0.600, 0.667) | 28 | 0.6394 | 0.6786 | 28 | 0.6394 | 0.6786 |
| [0.667, 0.733) | 41 | 0.7009 | 0.5610 | 41 | 0.7009 | 0.5610 |
| [0.733, 0.800) | 61 | 0.7710 | 0.5410 | 61 | 0.7710 | 0.5410 |
| [0.800, 0.867) | 79 | 0.8305 | 0.5063 | 79 | 0.8305 | 0.5063 |
| [0.867, 0.933) | 68 | 0.8957 | 0.4118 | 68 | 0.8957 | 0.4118 |
| [0.933, 1.000) | 23 | 0.9588 | 0.5652 | 23 | 0.9588 | 0.5652 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 9 | 0.5172 | 0.7778 | 9 | 0.5172 | 0.7778 |
| [0.533, 0.600) | 26 | 0.5696 | 0.6154 | 26 | 0.5696 | 0.6154 |
| [0.600, 0.667) | 35 | 0.6327 | 0.5429 | 35 | 0.6327 | 0.5429 |
| [0.667, 0.733) | 52 | 0.7040 | 0.3846 | 52 | 0.7040 | 0.3846 |
| [0.733, 0.800) | 69 | 0.7675 | 0.3768 | 69 | 0.7675 | 0.3768 |
| [0.800, 0.867) | 69 | 0.8314 | 0.4493 | 69 | 0.8314 | 0.4493 |
| [0.867, 0.933) | 56 | 0.8977 | 0.4821 | 56 | 0.8977 | 0.4821 |
| [0.933, 1.000) | 21 | 0.9571 | 0.4286 | 21 | 0.9571 | 0.4286 |

### B4 / qs_v2 (doc-level, underpowered), holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.2249 | 0.0688 | 0.4974 | 0.4298 | 0.5428 | 0.5428 |
| has_phi_direct = raw (T fallback) | 0.7858 | 0.7858 | 1.2852 | 1.2852 | 0.0380 | 0.0380 |
| has_phi_quasi | 0.7526 | 0.4954 | 1.2238 | 0.5416 | 0.0064 | 0.0064 |
| has_coded_id = raw (T fallback) | 0.7776 | 0.7776 | 1.2614 | 1.2614 | 0.0380 | 0.0380 |
| has_staff_pii = raw (T fallback) | 0.1015 | 0.1015 | 0.4079 | 0.4079 | 0.6700 | 0.6700 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 0 | n/a | n/a | 1 | 0.5284 | 1.0000 |
| [0.533, 0.600) | 0 | n/a | n/a | 11 | 0.5787 | 0.7273 |
| [0.600, 0.667) | 2 | 0.6287 | 1.0000 | 57 | 0.6345 | 0.6491 |
| [0.667, 0.733) | 1 | 0.7082 | 0.0000 | 11 | 0.6764 | 0.9091 |
| [0.733, 0.800) | 4 | 0.7651 | 1.0000 | 0 | n/a | n/a |
| [0.800, 0.867) | 17 | 0.8443 | 0.6471 | 0 | n/a | n/a |
| [0.867, 0.933) | 40 | 0.9034 | 0.6250 | 0 | n/a | n/a |
| [0.933, 1.000) | 16 | 0.9447 | 0.8750 | 0 | n/a | n/a |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 1 | 0.5288 | 0.0000 | 1 | 0.5288 | 0.0000 |
| [0.533, 0.600) | 3 | 0.5841 | 0.3333 | 3 | 0.5841 | 0.3333 |
| [0.600, 0.667) | 3 | 0.6550 | 0.0000 | 3 | 0.6550 | 0.0000 |
| [0.667, 0.733) | 7 | 0.7123 | 0.0000 | 7 | 0.7123 | 0.0000 |
| [0.733, 0.800) | 26 | 0.7675 | 0.0000 | 26 | 0.7675 | 0.0000 |
| [0.800, 0.867) | 20 | 0.8350 | 0.0000 | 20 | 0.8350 | 0.0000 |
| [0.867, 0.933) | 18 | 0.8933 | 0.0000 | 18 | 0.8933 | 0.0000 |
| [0.933, 1.000) | 2 | 0.9464 | 0.0000 | 2 | 0.9464 | 0.0000 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 2 | 0.5149 | 0.5000 | 74 | 0.5191 | 0.0270 |
| [0.533, 0.600) | 3 | 0.5696 | 0.3333 | 6 | 0.5362 | 0.0000 |
| [0.600, 0.667) | 3 | 0.6460 | 0.0000 | 0 | n/a | n/a |
| [0.667, 0.733) | 16 | 0.7034 | 0.0000 | 0 | n/a | n/a |
| [0.733, 0.800) | 20 | 0.7729 | 0.0000 | 0 | n/a | n/a |
| [0.800, 0.867) | 24 | 0.8368 | 0.0000 | 0 | n/a | n/a |
| [0.867, 0.933) | 11 | 0.8910 | 0.0000 | 0 | n/a | n/a |
| [0.933, 1.000) | 1 | 0.9373 | 0.0000 | 0 | n/a | n/a |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 1 | 0.5093 | 0.0000 | 1 | 0.5093 | 0.0000 |
| [0.533, 0.600) | 3 | 0.5692 | 0.3333 | 3 | 0.5692 | 0.3333 |
| [0.600, 0.667) | 3 | 0.6390 | 0.0000 | 3 | 0.6390 | 0.0000 |
| [0.667, 0.733) | 12 | 0.6993 | 0.0000 | 12 | 0.6993 | 0.0000 |
| [0.733, 0.800) | 21 | 0.7729 | 0.0000 | 21 | 0.7729 | 0.0000 |
| [0.800, 0.867) | 23 | 0.8321 | 0.0000 | 23 | 0.8321 | 0.0000 |
| [0.867, 0.933) | 16 | 0.8977 | 0.0000 | 16 | 0.8977 | 0.0000 |
| [0.933, 1.000) | 1 | 0.9541 | 0.0000 | 1 | 0.9541 | 0.0000 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 1 | 0.5244 | 0.0000 | 1 | 0.5244 | 0.0000 |
| [0.533, 0.600) | 3 | 0.5613 | 0.3333 | 3 | 0.5613 | 0.3333 |
| [0.600, 0.667) | 4 | 0.6327 | 0.7500 | 4 | 0.6327 | 0.7500 |
| [0.667, 0.733) | 10 | 0.7082 | 0.5000 | 10 | 0.7082 | 0.5000 |
| [0.733, 0.800) | 23 | 0.7663 | 0.6522 | 23 | 0.7663 | 0.6522 |
| [0.800, 0.867) | 20 | 0.8343 | 0.8000 | 20 | 0.8343 | 0.8000 |
| [0.867, 0.933) | 19 | 0.8972 | 0.8421 | 19 | 0.8972 | 0.8421 |

### C / qs_v1, test

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.0009 | 0.0004 | 0.0021 | 0.0021 | 0.9889 | 0.9889 |
| subject_role | 0.0032 | 0.0009 | 0.0039 | 0.0040 | 0.9527 | 0.9591 |
| category | 0.0049 | 0.0012 | 0.0043 | 0.0044 | 0.6796 | 0.7014 |
| doc_kind | 0.0554 | 0.0575 | 0.6238 | 0.6242 | 0.6836 | 0.6836 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.533, 0.600) | 1 | 0.5467 | 1.0000 | 1 | 0.5499 | 1.0000 |
| [0.600, 0.667) | 1 | 0.6246 | 0.0000 | 1 | 0.6328 | 0.0000 |
| [0.667, 0.733) | 1 | 0.6976 | 0.0000 | 1 | 0.7097 | 0.0000 |
| [0.867, 0.933) | 2 | 0.8996 | 1.0000 | 2 | 0.9125 | 1.0000 |
| [0.933, 1.000) | 5708 | 0.9986 | 0.9991 | 5708 | 0.9991 | 0.9991 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.400, 0.467) | 1 | 0.4351 | 0.0000 | 1 | 0.4573 | 0.0000 |
| [0.467, 0.533) | 1 | 0.5074 | 0.0000 | 1 | 0.5326 | 0.0000 |
| [0.533, 0.600) | 2 | 0.5656 | 0.5000 | 1 | 0.5450 | 1.0000 |
| [0.600, 0.667) | 1 | 0.6021 | 0.0000 | 2 | 0.6130 | 0.0000 |
| [0.867, 0.933) | 2 | 0.9007 | 0.5000 | 1 | 0.8983 | 0.0000 |
| [0.933, 1.000) | 5706 | 0.9957 | 0.9984 | 5707 | 0.9981 | 0.9984 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.800, 0.867) | 1 | 0.8271 | 0.0000 | 0 | n/a | n/a |
| [0.867, 0.933) | 4 | 0.8964 | 0.5000 | 4 | 0.9109 | 0.2500 |
| [0.933, 1.000) | 5708 | 0.9938 | 0.9982 | 5709 | 0.9975 | 0.9982 |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 15 | 0.2655 | 0.4000 | 116 | 0.2654 | 0.3966 |
| [0.267, 0.333) | 4583 | 0.2863 | 0.3450 | 4501 | 0.2816 | 0.3444 |
| [0.333, 0.400) | 54 | 0.3611 | 0.4630 | 48 | 0.3640 | 0.4167 |
| [0.400, 0.467) | 21 | 0.4281 | 0.2857 | 14 | 0.4310 | 0.4286 |
| [0.467, 0.533) | 10 | 0.4987 | 0.6000 | 11 | 0.5011 | 0.5455 |
| [0.533, 0.600) | 8 | 0.5634 | 0.6250 | 5 | 0.5710 | 0.8000 |
| [0.600, 0.667) | 6 | 0.6427 | 0.6667 | 5 | 0.6313 | 0.6000 |
| [0.667, 0.733) | 3 | 0.7098 | 0.6667 | 4 | 0.7051 | 0.7500 |
| [0.733, 0.800) | 5 | 0.7737 | 0.8000 | 4 | 0.7597 | 0.5000 |
| [0.800, 0.867) | 4 | 0.8359 | 0.2500 | 7 | 0.8389 | 0.1429 |
| [0.867, 0.933) | 9 | 0.9041 | 0.2222 | 8 | 0.8993 | 0.3750 |
| [0.933, 1.000) | 995 | 0.9936 | 0.9668 | 990 | 0.9857 | 0.9697 |

### C / qs_v1, holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.0083 | 0.0090 | 0.0224 | 0.0226 | 0.9923 | 0.9923 |
| subject_role | 0.0144 | 0.0175 | 0.0387 | 0.0395 | 0.9865 | 0.9864 |
| category | 0.0201 | 0.0235 | 0.0508 | 0.0512 | 0.8956 | 0.9093 |
| doc_kind | 0.3007 | 0.2940 | 0.7846 | 0.7768 | 0.9485 | 0.9485 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 1 | 0.5324 | 0.0000 | 0 | n/a | n/a |
| [0.533, 0.600) | 2 | 0.5586 | 0.5000 | 3 | 0.5533 | 0.3333 |
| [0.600, 0.667) | 5 | 0.6263 | 0.4000 | 5 | 0.6346 | 0.4000 |
| [0.667, 0.733) | 2 | 0.6709 | 0.5000 | 2 | 0.6818 | 0.5000 |
| [0.733, 0.800) | 2 | 0.7480 | 0.5000 | 2 | 0.7620 | 0.5000 |
| [0.800, 0.867) | 3 | 0.8125 | 0.6667 | 3 | 0.8275 | 0.6667 |
| [0.867, 0.933) | 1 | 0.9062 | 1.0000 | 1 | 0.9187 | 1.0000 |
| [0.933, 1.000) | 708 | 0.9984 | 0.9944 | 708 | 0.9989 | 0.9944 |

Reliability data, `subject_role` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.800, 0.867) | 4 | 0.8321 | 0.5000 | 3 | 0.8598 | 0.6667 |
| [0.867, 0.933) | 3 | 0.8982 | 0.6667 | 3 | 0.9098 | 0.6667 |
| [0.933, 1.000) | 717 | 0.9950 | 0.9833 | 718 | 0.9977 | 0.9819 |

Reliability data, `category` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.533, 0.600) | 3 | 0.5564 | 1.0000 | 3 | 0.5678 | 1.0000 |
| [0.600, 0.667) | 4 | 0.6247 | 0.5000 | 3 | 0.6336 | 0.6667 |
| [0.667, 0.733) | 2 | 0.7163 | 1.0000 | 2 | 0.7038 | 0.5000 |
| [0.733, 0.800) | 1 | 0.7902 | 1.0000 | 1 | 0.7609 | 1.0000 |
| [0.800, 0.867) | 0 | n/a | n/a | 1 | 0.8219 | 1.0000 |
| [0.867, 0.933) | 2 | 0.8848 | 0.5000 | 2 | 0.9158 | 0.5000 |
| [0.933, 1.000) | 712 | 0.9932 | 0.9775 | 712 | 0.9972 | 0.9775 |

Reliability data, `doc_kind` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.200, 0.267) | 2 | 0.2653 | 0.0000 | 6 | 0.2648 | 0.0000 |
| [0.267, 0.333) | 574 | 0.2864 | 0.0000 | 576 | 0.2817 | 0.0000 |
| [0.333, 0.400) | 14 | 0.3558 | 0.0000 | 10 | 0.3577 | 0.0000 |
| [0.400, 0.467) | 3 | 0.4201 | 0.0000 | 3 | 0.4335 | 0.0000 |
| [0.467, 0.533) | 4 | 0.5022 | 0.0000 | 3 | 0.4917 | 0.0000 |
| [0.533, 0.600) | 2 | 0.5746 | 0.0000 | 2 | 0.5550 | 0.0000 |
| [0.600, 0.667) | 2 | 0.6459 | 0.0000 | 1 | 0.6058 | 0.0000 |
| [0.867, 0.933) | 2 | 0.9222 | 0.5000 | 2 | 0.8810 | 0.5000 |
| [0.933, 1.000) | 121 | 0.9934 | 0.6529 | 121 | 0.9848 | 0.6529 |

### C / qs_v2, test

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.0009 | 0.0004 | 0.0021 | 0.0021 | 0.9889 | 0.9889 |
| has_phi_direct | 0.0010 | 0.0003 | 0.0013 | 0.0013 | 0.8163 | 0.8163 |
| has_phi_quasi | 0.0018 | 0.0019 | 0.0067 | 0.0067 | 0.9923 | 0.9923 |
| has_coded_id | 0.0007 | 0.0004 | 0.0017 | 0.0017 | 0.9582 | 0.9582 |
| has_staff_pii | 0.0017 | 0.0007 | 0.0006 | 0.0006 | 0.8310 | 0.8310 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.533, 0.600) | 1 | 0.5398 | 1.0000 | 1 | 0.5425 | 1.0000 |
| [0.600, 0.667) | 1 | 0.6240 | 0.0000 | 1 | 0.6322 | 0.0000 |
| [0.667, 0.733) | 1 | 0.6992 | 0.0000 | 1 | 0.7114 | 0.0000 |
| [0.867, 0.933) | 2 | 0.8982 | 1.0000 | 2 | 0.9112 | 1.0000 |
| [0.933, 1.000) | 5708 | 0.9986 | 0.9991 | 5708 | 0.9991 | 0.9991 |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.800, 0.867) | 1 | 0.8628 | 0.0000 | 0 | n/a | n/a |
| [0.867, 0.933) | 0 | n/a | n/a | 1 | 0.8835 | 0.0000 |
| [0.933, 1.000) | 5712 | 0.9986 | 0.9995 | 5712 | 0.9993 | 0.9995 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.667, 0.733) | 2 | 0.7168 | 0.5000 | 2 | 0.7198 | 0.5000 |
| [0.867, 0.933) | 4 | 0.9097 | 0.5000 | 4 | 0.9127 | 0.5000 |
| [0.933, 1.000) | 5707 | 0.9984 | 0.9970 | 5707 | 0.9986 | 0.9970 |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.933, 1.000) | 5713 | 0.9984 | 0.9991 | 5713 | 0.9995 | 0.9991 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.533, 0.600) | 1 | 0.5499 | 1.0000 | 1 | 0.5571 | 1.0000 |
| [0.600, 0.667) | 1 | 0.6309 | 0.0000 | 1 | 0.6490 | 0.0000 |
| [0.733, 0.800) | 1 | 0.7799 | 1.0000 | 0 | n/a | n/a |
| [0.800, 0.867) | 0 | n/a | n/a | 1 | 0.8100 | 1.0000 |
| [0.933, 1.000) | 5710 | 0.9984 | 0.9998 | 5710 | 0.9994 | 0.9998 |

### C / qs_v2, holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.0091 | 0.0090 | 0.0224 | 0.0227 | 0.9923 | 0.9923 |
| has_phi_direct | 0.0014 | 0.0007 | 0.0000 | 0.0000 | n/a | n/a |
| has_phi_quasi | 0.0677 | 0.0687 | 0.1359 | 0.1361 | 0.9689 | 0.9689 |
| has_coded_id | 0.0016 | 0.0005 | 0.0000 | 0.0000 | n/a | n/a |
| has_staff_pii | 0.0020 | 0.0008 | 0.0000 | 0.0000 | n/a | n/a |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 1 | 0.5312 | 0.0000 | 0 | n/a | n/a |
| [0.533, 0.600) | 3 | 0.5723 | 0.6667 | 3 | 0.5531 | 0.3333 |
| [0.600, 0.667) | 4 | 0.6345 | 0.2500 | 5 | 0.6358 | 0.4000 |
| [0.667, 0.733) | 2 | 0.6699 | 0.5000 | 2 | 0.6806 | 0.5000 |
| [0.733, 0.800) | 3 | 0.7648 | 0.6667 | 2 | 0.7617 | 0.5000 |
| [0.800, 0.867) | 2 | 0.8157 | 0.5000 | 3 | 0.8251 | 0.6667 |
| [0.867, 0.933) | 1 | 0.9077 | 1.0000 | 1 | 0.9202 | 1.0000 |
| [0.933, 1.000) | 708 | 0.9984 | 0.9944 | 708 | 0.9989 | 0.9944 |

Reliability data, `has_phi_direct` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.933, 1.000) | 724 | 0.9986 | 1.0000 | 724 | 0.9993 | 1.0000 |

Reliability data, `has_phi_quasi` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.533, 0.600) | 1 | 0.5565 | 0.0000 | 1 | 0.5574 | 0.0000 |
| [0.600, 0.667) | 3 | 0.6503 | 0.6667 | 2 | 0.6446 | 0.5000 |
| [0.667, 0.733) | 1 | 0.7049 | 1.0000 | 2 | 0.6881 | 1.0000 |
| [0.733, 0.800) | 3 | 0.7531 | 0.3333 | 3 | 0.7565 | 0.3333 |
| [0.800, 0.867) | 3 | 0.8197 | 1.0000 | 3 | 0.8232 | 1.0000 |
| [0.867, 0.933) | 9 | 0.8940 | 0.3333 | 8 | 0.8925 | 0.3750 |
| [0.933, 1.000) | 704 | 0.9975 | 0.9389 | 705 | 0.9976 | 0.9376 |

Reliability data, `has_coded_id` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.933, 1.000) | 724 | 0.9984 | 1.0000 | 724 | 0.9995 | 1.0000 |

Reliability data, `has_staff_pii` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.933, 1.000) | 724 | 0.9980 | 1.0000 | 724 | 0.9992 | 1.0000 |

### LC / qs_v1, test

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.0394 | 0.0078 | 0.0504 | 0.0496 | 0.9578 | 0.9578 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 37 | 0.5175 | 0.5676 | 23 | 0.5186 | 0.4783 |
| [0.533, 0.600) | 61 | 0.5638 | 0.5902 | 47 | 0.5656 | 0.6170 |
| [0.600, 0.667) | 85 | 0.6314 | 0.5647 | 38 | 0.6396 | 0.5789 |
| [0.667, 0.733) | 88 | 0.7010 | 0.6591 | 59 | 0.6991 | 0.5593 |
| [0.733, 0.800) | 112 | 0.7645 | 0.7768 | 71 | 0.7723 | 0.7465 |
| [0.800, 0.867) | 102 | 0.8360 | 0.7745 | 87 | 0.8386 | 0.6667 |
| [0.867, 0.933) | 721 | 0.9133 | 0.9598 | 107 | 0.8997 | 0.7757 |
| [0.933, 1.000) | 4507 | 0.9609 | 0.9989 | 5281 | 0.9910 | 0.9911 |

### LC / qs_v1, holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.0627 | 0.0243 | 0.0384 | 0.0328 | 0.9827 | 0.9827 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 5 | 0.5174 | 0.2000 | 4 | 0.5218 | 0.2500 |
| [0.533, 0.600) | 11 | 0.5580 | 0.2727 | 9 | 0.5718 | 0.3333 |
| [0.600, 0.667) | 6 | 0.6364 | 0.1667 | 3 | 0.6391 | 0.0000 |
| [0.667, 0.733) | 16 | 0.7073 | 1.0000 | 5 | 0.7023 | 0.0000 |
| [0.733, 0.800) | 20 | 0.7706 | 0.9500 | 7 | 0.7754 | 1.0000 |
| [0.800, 0.867) | 27 | 0.8394 | 0.8889 | 14 | 0.8263 | 0.9286 |
| [0.867, 0.933) | 89 | 0.9134 | 1.0000 | 28 | 0.8975 | 1.0000 |
| [0.933, 1.000) | 550 | 0.9627 | 1.0000 | 654 | 0.9908 | 0.9954 |

### LW / qs_v1, test

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.0418 | 0.0114 | 0.0540 | 0.0529 | 0.9464 | 0.9464 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 30 | 0.5161 | 0.6333 | 20 | 0.5173 | 0.5500 |
| [0.533, 0.600) | 101 | 0.5695 | 0.7129 | 50 | 0.5707 | 0.6600 |
| [0.600, 0.667) | 90 | 0.6351 | 0.6778 | 71 | 0.6335 | 0.7746 |
| [0.667, 0.733) | 75 | 0.6993 | 0.5733 | 60 | 0.7008 | 0.6833 |
| [0.733, 0.800) | 83 | 0.7671 | 0.7229 | 64 | 0.7643 | 0.5312 |
| [0.800, 0.867) | 150 | 0.8393 | 0.8133 | 71 | 0.8340 | 0.6901 |
| [0.867, 0.933) | 874 | 0.9135 | 0.9611 | 116 | 0.9054 | 0.7414 |
| [0.933, 1.000) | 4310 | 0.9621 | 0.9988 | 5261 | 0.9899 | 0.9909 |

### LW / qs_v1, holdout

| question | ECE raw | ECE cal | Brier raw | Brier cal | correctness AUROC raw | correctness AUROC cal |
|---|---|---|---|---|---|---|
| pii_present | 0.0634 | 0.0251 | 0.0364 | 0.0264 | 0.9615 | 0.9615 |

Reliability data, `pii_present` (non-empty bins):

| bin | n raw | conf raw | acc raw | n cal | conf cal | acc cal |
|---|---|---|---|---|---|---|
| [0.467, 0.533) | 8 | 0.5222 | 0.6250 | 3 | 0.5159 | 0.3333 |
| [0.533, 0.600) | 10 | 0.5773 | 0.9000 | 6 | 0.5530 | 0.6667 |
| [0.600, 0.667) | 14 | 0.6394 | 0.8571 | 10 | 0.6282 | 1.0000 |
| [0.667, 0.733) | 21 | 0.6932 | 1.0000 | 11 | 0.7102 | 1.0000 |
| [0.733, 0.800) | 18 | 0.7650 | 0.9444 | 20 | 0.7768 | 0.9000 |
| [0.800, 0.867) | 25 | 0.8419 | 0.9200 | 14 | 0.8392 | 0.9286 |
| [0.867, 0.933) | 87 | 0.9144 | 1.0000 | 19 | 0.9097 | 0.8947 |
| [0.933, 1.000) | 541 | 0.9635 | 1.0000 | 641 | 0.9906 | 1.0000 |

## 5. Routing

### A / qs_v1, test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 65 | 354 | 419 |
| B | 29 | 335 | 4930 | 5294 |
| all | 29 | 400 | 5284 | 5713 |

| trigger | count |
|---|---|
| p_below_t_low | 29 |
| p_in_escalate_band | 5284 |
| role_both | 124 |
| role_patient | 276 |

### A / qs_v1, holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 0 | 56 | 56 |
| B | 1 | 35 | 632 | 668 |
| all | 1 | 35 | 688 | 724 |

| trigger | count |
|---|---|
| p_below_t_low | 1 |
| p_in_escalate_band | 688 |
| role_both | 15 |
| role_patient | 20 |

### A / qs_v2, test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 0 | 419 | 419 |
| B | 30 | 0 | 5264 | 5294 |
| all | 30 | 0 | 5683 | 5713 |

| trigger | count |
|---|---|
| p_below_t_low | 30 |
| p_in_escalate_band | 5683 |

### A / qs_v2, holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 0 | 56 | 56 |
| B | 1 | 0 | 667 | 668 |
| all | 1 | 0 | 723 | 724 |

| trigger | count |
|---|---|
| p_below_t_low | 1 |
| p_in_escalate_band | 723 |

### B1 / qs_v1, test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 112 | 194 | 306 |
| B | 2 | 502 | 1109 | 1613 |
| all | 2 | 614 | 1303 | 1919 |

| trigger | count |
|---|---|
| p_at_or_above_t_high | 1 |
| p_below_t_low | 2 |
| p_in_escalate_band | 1303 |
| role_both | 60 |
| role_patient | 553 |

### B1 / qs_v1, holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 4 | 52 | 56 |
| B | 0 | 59 | 134 | 193 |
| all | 0 | 63 | 186 | 249 |

| trigger | count |
|---|---|
| p_in_escalate_band | 186 |
| role_both | 3 |
| role_patient | 60 |

### B1 / qs_v2, test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 1 | 1 | 304 | 306 |
| B | 4 | 0 | 1609 | 1613 |
| all | 5 | 1 | 1913 | 1919 |

| trigger | count |
|---|---|
| p_at_or_above_t_high | 1 |
| p_below_t_low | 5 |
| p_in_escalate_band | 1913 |

### B1 / qs_v2, holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 0 | 56 | 56 |
| B | 0 | 0 | 193 | 193 |
| all | 0 | 0 | 249 | 249 |

| trigger | count |
|---|---|
| p_in_escalate_band | 249 |

### B2 / qs_v1, test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 1 | 88 | 144 | 233 |
| B | 0 | 201 | 478 | 679 |
| all | 1 | 289 | 622 | 912 |

| trigger | count |
|---|---|
| p_below_t_low | 1 |
| p_in_escalate_band | 622 |
| role_both | 31 |
| role_patient | 258 |

### B2 / qs_v1, holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 4 | 52 | 56 |
| B | 0 | 16 | 58 | 74 |
| all | 0 | 20 | 110 | 130 |

| trigger | count |
|---|---|
| p_in_escalate_band | 110 |
| role_both | 4 |
| role_patient | 16 |

### B2 / qs_v2, test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 1 | 0 | 232 | 233 |
| B | 0 | 0 | 679 | 679 |
| all | 1 | 0 | 911 | 912 |

| trigger | count |
|---|---|
| p_below_t_low | 1 |
| p_in_escalate_band | 911 |

### B2 / qs_v2, holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 0 | 56 | 56 |
| B | 0 | 0 | 74 | 74 |
| all | 0 | 0 | 130 | 130 |

| trigger | count |
|---|---|
| p_in_escalate_band | 130 |

### B3 / qs_v1 (doc-level, underpowered), test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 90 | 140 | 230 |
| B | 1 | 84 | 210 | 295 |
| all | 1 | 174 | 350 | 525 |

| trigger | count |
|---|---|
| p_below_t_low | 1 |
| p_in_escalate_band | 350 |
| role_both | 20 |
| role_patient | 154 |

### B3 / qs_v1 (doc-level, underpowered), holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 4 | 52 | 56 |
| B | 0 | 2 | 26 | 28 |
| all | 0 | 6 | 78 | 84 |

| trigger | count |
|---|---|
| p_in_escalate_band | 78 |
| role_both | 1 |
| role_patient | 5 |

### B3 / qs_v2 (doc-level, underpowered), test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 0 | 230 | 230 |
| B | 1 | 0 | 294 | 295 |
| all | 1 | 0 | 524 | 525 |

| trigger | count |
|---|---|
| p_below_t_low | 1 |
| p_in_escalate_band | 524 |

### B3 / qs_v2 (doc-level, underpowered), holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 0 | 56 | 56 |
| B | 0 | 0 | 28 | 28 |
| all | 0 | 0 | 84 | 84 |

| trigger | count |
|---|---|
| p_in_escalate_band | 84 |

### B4 / qs_v1 (doc-level, underpowered), test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 93 | 122 | 215 |
| B | 0 | 42 | 80 | 122 |
| all | 0 | 135 | 202 | 337 |

| trigger | count |
|---|---|
| p_in_escalate_band | 202 |
| role_both | 16 |
| role_patient | 119 |

### B4 / qs_v1 (doc-level, underpowered), holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 4 | 52 | 56 |
| B | 0 | 1 | 23 | 24 |
| all | 0 | 5 | 75 | 80 |

| trigger | count |
|---|---|
| p_in_escalate_band | 75 |
| role_both | 1 |
| role_patient | 4 |

### B4 / qs_v2 (doc-level, underpowered), test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 0 | 215 | 215 |
| B | 0 | 0 | 122 | 122 |
| all | 0 | 0 | 337 | 337 |

| trigger | count |
|---|---|
| p_in_escalate_band | 337 |

### B4 / qs_v2 (doc-level, underpowered), holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 0 | 56 | 56 |
| B | 0 | 0 | 24 | 24 |
| all | 0 | 0 | 80 | 80 |

| trigger | count |
|---|---|
| p_in_escalate_band | 80 |

### C / qs_v1, test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 1 | 418 | 0 | 419 |
| B | 5288 | 6 | 0 | 5294 |
| all | 5289 | 424 | 0 | 5713 |

| trigger | count |
|---|---|
| p_at_or_above_t_high | 421 |
| p_below_t_low | 5289 |
| role_both | 119 |
| role_patient | 228 |

### C / qs_v1, holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 56 | 0 | 56 |
| B | 664 | 4 | 0 | 668 |
| all | 664 | 60 | 0 | 724 |

| trigger | count |
|---|---|
| p_at_or_above_t_high | 59 |
| p_below_t_low | 664 |
| role_both | 11 |
| role_patient | 4 |

### C / qs_v2, test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 2 | 417 | 0 | 419 |
| B | 5290 | 4 | 0 | 5294 |
| all | 5292 | 421 | 0 | 5713 |

| trigger | count |
|---|---|
| p_at_or_above_t_high | 421 |
| p_below_t_low | 5292 |

### C / qs_v2, holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 56 | 0 | 56 |
| B | 665 | 3 | 0 | 668 |
| all | 665 | 59 | 0 | 724 |

| trigger | count |
|---|---|
| p_at_or_above_t_high | 59 |
| p_below_t_low | 665 |

### LC / qs_v1, test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 2 | 152 | 265 | 419 |
| B | 3471 | 0 | 1823 | 5294 |
| all | 3473 | 152 | 2088 | 5713 |

| trigger | count |
|---|---|
| p_at_or_above_t_high | 152 |
| p_below_t_low | 3473 |
| p_in_escalate_band | 2088 |

### LC / qs_v1, holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 1 | 55 | 56 |
| B | 465 | 0 | 203 | 668 |
| all | 465 | 1 | 258 | 724 |

| trigger | count |
|---|---|
| p_at_or_above_t_high | 1 |
| p_below_t_low | 465 |
| p_in_escalate_band | 258 |

### LW / qs_v1, test

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 1 | 94 | 324 | 419 |
| B | 2923 | 3 | 2368 | 5294 |
| all | 2924 | 97 | 2692 | 5713 |

| trigger | count |
|---|---|
| p_at_or_above_t_high | 97 |
| p_below_t_low | 2924 |
| p_in_escalate_band | 2692 |

### LW / qs_v1, holdout

| gold pii_present | forward | redact | escalate | total |
|---|---|---|---|---|
| A | 0 | 1 | 55 | 56 |
| B | 405 | 0 | 263 | 668 |
| all | 405 | 1 | 318 | 724 |

| trigger | count |
|---|---|
| p_at_or_above_t_high | 1 |
| p_below_t_low | 405 |
| p_in_escalate_band | 318 |

## 6. Speed

Per-unit latency is not comparable across arms (units range from 256-token chunks to whole documents); compare the per-document row or the length rows. Devices in these runs: cpu, cuda. Batched runs: none in these scores. Lexical baselines are scored in one CPU batch; their latency is not comparable.

### A / qs_v1

Hardware: **Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB RAM, device cuda (Tesla T4), torch 2.10.0+cu128**. Warmup calls excluded: 10. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 0.98x. laya autocast: batch-1 on, batched not run.

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 10427 | 131.6 | 137.2 | 142.8 | 129.6 | 7.71 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 673 | 1405.2 | 6027.2 | 6718.8 | 2008.6 | 0.50 |
| per unit, batch-1, <1k tokens | 10427 | 131.6 | 137.2 | 142.8 | 129.6 | 7.71 |

### A / qs_v2

Hardware: **Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB RAM, device cuda (Tesla T4), torch 2.10.0+cu128**. Warmup calls excluded: 10. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 1.03x. laya autocast: batch-1 on, batched not run.

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 10427 | 142.0 | 146.6 | 151.0 | 139.1 | 7.19 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 673 | 1488.4 | 6482.9 | 7279.2 | 2154.8 | 0.46 |
| per unit, batch-1, <1k tokens | 10427 | 142.0 | 146.6 | 151.0 | 139.1 | 7.19 |

### B1 / qs_v1

Hardware: **Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB RAM, device cuda (Tesla T4), torch 2.10.0+cu128**. Warmup calls excluded: 10. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 1.05x. laya autocast: batch-1 on, batched not run.

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 3509 | 156.6 | 161.3 | 169.3 | 143.0 | 6.99 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 673 | 547.8 | 2178.1 | 2448.0 | 745.5 | 1.34 |
| per unit, batch-1, <1k tokens | 3509 | 156.6 | 161.3 | 169.3 | 143.0 | 6.99 |

### B1 / qs_v2

Hardware: **Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB RAM, device cuda (Tesla T4), torch 2.10.0+cu128**. Warmup calls excluded: 10. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 1.05x. laya autocast: batch-1 on, batched not run.

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 3509 | 181.1 | 185.5 | 189.6 | 163.9 | 6.10 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 673 | 627.1 | 2523.0 | 2813.4 | 854.5 | 1.17 |
| per unit, batch-1, <1k tokens | 3509 | 181.1 | 185.5 | 189.6 | 163.9 | 6.10 |

### B2 / qs_v1

Hardware: **Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB RAM, device cuda (Tesla T4), torch 2.10.0+cu128**. Warmup calls excluded: 10. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 1.05x. laya autocast: batch-1 on, batched not run.

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 1700 | 368.1 | 438.2 | 484.9 | 305.2 | 3.28 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 673 | 555.8 | 2299.7 | 2544.0 | 771.0 | 1.30 |
| per unit, batch-1, <1k tokens | 501 | 113.4 | 201.0 | 205.9 | 118.9 | 8.41 |
| per unit, batch-1, 1-2k tokens | 1181 | 393.9 | 438.7 | 453.2 | 381.4 | 2.62 |
| per unit, batch-1, 2-4k tokens | 18 | 487.4 | 516.2 | 516.7 | 492.0 | 2.03 |

### B2 / qs_v2

Hardware: **Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB RAM, device cuda (Tesla T4), torch 2.10.0+cu128**. Warmup calls excluded: 10. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 1.05x. laya autocast: batch-1 on, batched not run.

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 1700 | 439.2 | 528.1 | 565.3 | 365.4 | 2.74 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 673 | 665.8 | 2772.8 | 3086.9 | 923.1 | 1.08 |
| per unit, batch-1, <1k tokens | 501 | 128.0 | 229.9 | 245.1 | 135.8 | 7.36 |
| per unit, batch-1, 1-2k tokens | 1181 | 465.7 | 528.8 | 542.9 | 459.7 | 2.18 |
| per unit, batch-1, 2-4k tokens | 18 | 569.6 | 591.3 | 600.5 | 570.4 | 1.75 |

### B3 / qs_v1 (doc-level, underpowered)

Hardware: **Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB RAM, device cuda (Tesla T4), torch 2.10.0+cu128**. Warmup calls excluded: 10. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 1.12x. laya autocast: batch-1 on, batched not run.

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 989 | 745.3 | 1396.1 | 1443.0 | 740.0 | 1.35 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 673 | 692.3 | 3350.1 | 3922.0 | 1087.5 | 0.92 |
| per unit, batch-1, <1k tokens | 326 | 99.6 | 190.9 | 197.7 | 110.1 | 9.08 |
| per unit, batch-1, 1-2k tokens | 78 | 387.1 | 496.8 | 506.7 | 383.0 | 2.61 |
| per unit, batch-1, 2-4k tokens | 585 | 1259.2 | 1420.6 | 1448.9 | 1138.7 | 0.88 |

### B3 / qs_v2 (doc-level, underpowered)

Hardware: **Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB RAM, device cuda (Tesla T4), torch 2.10.0+cu128**. Warmup calls excluded: 10. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 1.06x. laya autocast: batch-1 on, batched not run.

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 989 | 909.7 | 1679.9 | 1709.7 | 899.6 | 1.11 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 673 | 845.8 | 4045.0 | 4788.6 | 1321.9 | 0.76 |
| per unit, batch-1, <1k tokens | 326 | 110.7 | 220.9 | 234.7 | 126.5 | 7.90 |
| per unit, batch-1, 1-2k tokens | 78 | 463.7 | 571.7 | 590.5 | 458.1 | 2.18 |
| per unit, batch-1, 2-4k tokens | 585 | 1552.6 | 1691.1 | 1716.6 | 1389.2 | 0.72 |

### B4 / qs_v1 (doc-level, underpowered)

Hardware: **Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB RAM, device cuda (Tesla T4), torch 2.10.0+cu128**. Warmup calls excluded: 10. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 1.04x. laya autocast: batch-1 on, batched not run.

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 673 | 713.8 | 4791.9 | 4987.7 | 1485.8 | 0.67 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 673 | 713.8 | 4791.9 | 4987.7 | 1485.8 | 0.67 |
| per unit, batch-1, <1k tokens | 239 | 123.6 | 194.0 | 199.5 | 120.3 | 8.31 |
| per unit, batch-1, 1-2k tokens | 50 | 387.7 | 502.4 | 512.2 | 397.9 | 2.51 |
| per unit, batch-1, 2-4k tokens | 197 | 1034.6 | 1497.4 | 1528.9 | 1041.3 | 0.96 |
| per unit, batch-1, 4-8k tokens | 138 | 3860.7 | 4987.3 | 5143.8 | 3716.4 | 0.27 |
| per unit, batch-1, >8k tokens | 49 | 4765.2 | 4818.1 | 4844.0 | 4760.9 | 0.21 |

### B4 / qs_v2 (doc-level, underpowered)

Hardware: **Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB RAM, device cuda (Tesla T4), torch 2.10.0+cu128**. Warmup calls excluded: 10. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 1.04x. laya autocast: batch-1 on, batched not run.

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 673 | 849.6 | 5772.3 | 6049.2 | 1775.3 | 0.56 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 673 | 849.6 | 5772.3 | 6049.2 | 1775.3 | 0.56 |
| per unit, batch-1, <1k tokens | 239 | 142.6 | 220.6 | 231.7 | 136.6 | 7.32 |
| per unit, batch-1, 1-2k tokens | 50 | 461.0 | 566.8 | 587.9 | 466.8 | 2.14 |
| per unit, batch-1, 2-4k tokens | 197 | 1217.1 | 1809.5 | 1863.0 | 1240.0 | 0.81 |
| per unit, batch-1, 4-8k tokens | 138 | 4534.9 | 6041.9 | 6223.7 | 4440.8 | 0.23 |
| per unit, batch-1, >8k tokens | 49 | 5753.8 | 5809.6 | 5820.8 | 5748.4 | 0.17 |

### C / qs_v1

Hardware: **Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB RAM, device cuda (Tesla T4), torch 2.10.0+cu128**. Warmup calls excluded: 10. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 1.01x. laya autocast: batch-1 on, batched not run.

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 10427 | 127.3 | 130.7 | 132.8 | 125.0 | 8.00 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 673 | 1344.6 | 5885.5 | 6537.1 | 1936.7 | 0.52 |
| per unit, batch-1, <1k tokens | 10427 | 127.3 | 130.7 | 132.8 | 125.0 | 8.00 |

### C / qs_v2

Hardware: **Intel(R) Xeon(R) CPU @ 2.00GHz, 31.3 GB RAM, device cuda (Tesla T4), torch 2.10.0+cu128**. Warmup calls excluded: 10. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: 1.04x. laya autocast: batch-1 on, batched not run.

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 10427 | 137.5 | 140.8 | 142.2 | 134.5 | 7.43 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 673 | 1442.2 | 6313.9 | 7013.9 | 2084.1 | 0.48 |
| per unit, batch-1, <1k tokens | 10427 | 137.5 | 140.8 | 142.2 | 134.5 | 7.43 |

### LC / qs_v1

Hardware: **Apple M2, 8.0 GB RAM, device cpu (Apple MPS), torch 2.14.0**. Warmup calls excluded: 0. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: n/a. laya autocast: batch-1 unknown, batched not run.

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 10427 | 0.9 | 0.9 | 0.9 | 0.9 | 1083.77 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 673 | 10.1 | 42.4 | 47.1 | 14.3 | 69.95 |
| per unit, batch-1, <1k tokens | 10427 | 0.9 | 0.9 | 0.9 | 0.9 | 1083.77 |

### LW / qs_v1

Hardware: **Apple M2, 8.0 GB RAM, device cpu (Apple MPS), torch 2.14.0**. Warmup calls excluded: 0. Batch-1 outliers (> 5x the median of similar-length calls): 0. Batch-1 ms/token, end of run vs start: n/a. laya autocast: batch-1 unknown, batched not run.

| mode | n | p50 ms | p95 ms | p99 ms | mean ms | per sec |
|---|---|---|---|---|---|---|
| per unit, batch-1 | 10427 | 0.1 | 0.1 | 0.1 | 0.1 | 10478.21 |
| per unit, batched | 0 | not run |  |  |  |  |
| per document (sum of units, batch-1; incl. calib docs) | 673 | 1.0 | 4.4 | 4.9 | 1.5 | 676.31 |
| per unit, batch-1, <1k tokens | 10427 | 0.1 | 0.1 | 0.1 | 0.1 | 10478.21 |

## 7. Slices

Recall marked `*`: fewer than 30 positives in the slice. Forward rate marked `*`: fewer than 30 PII-free units.

### A / qs_v1, test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log | 263 | 27 | 42 | 1.0000 | 0.0152 | 0 | 0.8479 |
| doc_type | crf_page | 371 | 42 | 101 | 1.0000 | 0.0054 | 0 | 0.7278 |
| doc_type | csr_patient_narrative | 964 | 42 | 72 | 1.0000 | 0.0041 | 0 | 0.9357 |
| doc_type | delegation_log | 151 | 14 | 14 | 1.0000 * | 0.0132 | 0 | 0.9470 |
| doc_type | deviation_log | 203 | 23 | 23 | 1.0000 * | 0.0099 | 0 | 0.8916 |
| doc_type | icf_signature_page | 52 | 19 | 17 | 1.0000 * | 0.0000 | 0 | 0.7885 |
| doc_type | lab_report | 188 | 29 | 34 | 1.0000 | 0.0053 | 0 | 0.8404 |
| doc_type | monitoring_visit_report | 986 | 29 | 47 | 1.0000 | 0.0000 | 0 | 0.9533 |
| doc_type | protocol_section | 1240 | 41 | 0 | n/a | 0.0056 | 0 | 0.9992 |
| doc_type | sae_cioms | 300 | 36 | 38 | 1.0000 | 0.0033 | 0 | 0.8733 |
| doc_type | site_correspondence | 995 | 35 | 31 | 1.0000 | 0.0060 | 0 | 0.9698 |
| hard_negative | no | 4393 | 260 | 302 | 1.0000 | 0.0052 | 0 | 0.9356 |
| hard_negative | yes | 1320 | 77 | 117 | 1.0000 | 0.0045 | 0 | 0.9197 |
| lang | de | 33 | 22 | 26 | 1.0000 * | 0.0606 * | 0 | 0.3636 |
| lang | en | 5655 | 298 | 373 | 1.0000 | 0.0048 | 0 | 0.9383 |
| lang | es | 7 | 6 | 6 | 1.0000 * | 0.0000 * | 0 | 0.4286 |
| lang | pl | 18 | 11 | 14 | 1.0000 * | 0.0000 * | 0 | 0.1667 |
| length_bucket | long | 2513 | 80 | 70 | 1.0000 | 0.0032 | 0 | 0.9721 |
| length_bucket | medium | 1466 | 119 | 218 | 1.0000 | 0.0082 | 0 | 0.8595 |
| length_bucket | short | 287 | 108 | 99 | 1.0000 | 0.0105 | 0 | 0.7003 |
| length_bucket | xl | 1447 | 30 | 32 | 1.0000 | 0.0041 | 0 | 0.9813 |
| perturbation | email_quoting | 995 | 35 | 31 | 1.0000 | 0.0060 | 0 | 0.9698 |
| perturbation | headers_footers | 2405 | 132 | 156 | 1.0000 | 0.0046 | 0 | 0.9422 |
| perturbation | line_wrap | 1852 | 105 | 151 | 1.0000 | 0.0059 | 0 | 0.9266 |
| perturbation | none | 1421 | 93 | 104 | 1.0000 | 0.0049 | 0 | 0.9303 |
| perturbation | ocr_noise | 567 | 39 | 45 | 1.0000 | 0.0088 | 0 | 0.9206 |
| perturbation | table | 659 | 75 | 115 | 1.0000 | 0.0121 | 0 | 0.8240 |
| pii_depth | early | 282 | 8 | 11 | 1.0000 * | 0.0035 | 0 | 0.9645 |
| pii_depth | late | 582 | 16 | 21 | 1.0000 * | 0.0017 | 0 | 0.9656 |
| pii_depth | middle | 327 | 10 | 11 | 1.0000 * | 0.0031 | 0 | 0.9694 |
| pii_depth | none | 4522 | 303 | 376 | 1.0000 | 0.0057 | 0 | 0.9228 |
| pre_redacted | no | 5297 | 303 | 355 | 1.0000 | 0.0051 | 0 | 0.9379 |
| pre_redacted | yes | 416 | 34 | 64 | 1.0000 | 0.0048 | 0 | 0.8558 |
| split_span | no | 5695 | 337 | 402 | 1.0000 | 0.0051 | 0 | 0.9345 |
| split_span | yes | 18 | 17 | 17 | 1.0000 * | 0.0000 * | 0 | 0.1111 |
| truncated | no | 5713 | 337 | 419 | 1.0000 | 0.0051 | 0 | 0.9319 |

Value kinds of missed spans (false forwards):

none

### A / qs_v1, holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 724 | 80 | 56 | 1.0000 | 0.0014 | 0 | 0.9227 |
| hard_negative | no | 571 | 62 | 42 | 1.0000 | 0.0018 | 0 | 0.9264 |
| hard_negative | yes | 153 | 18 | 14 | 1.0000 * | 0.0000 | 0 | 0.9085 |
| lang | en | 724 | 80 | 56 | 1.0000 | 0.0014 | 0 | 0.9227 |
| length_bucket | medium | 596 | 47 | 34 | 1.0000 | 0.0000 | 0 | 0.9430 |
| length_bucket | short | 128 | 33 | 22 | 1.0000 * | 0.0078 | 0 | 0.8281 |
| perturbation | headers_footers | 307 | 35 | 25 | 1.0000 * | 0.0000 | 0 | 0.9186 |
| perturbation | line_wrap | 185 | 26 | 19 | 1.0000 * | 0.0054 | 0 | 0.8973 |
| perturbation | none | 290 | 28 | 19 | 1.0000 * | 0.0000 | 0 | 0.9345 |
| perturbation | ocr_noise | 48 | 7 | 6 | 1.0000 * | 0.0000 | 0 | 0.8750 |
| pii_depth | none | 724 | 80 | 56 | 1.0000 | 0.0014 | 0 | 0.9227 |
| pre_redacted | no | 675 | 75 | 51 | 1.0000 | 0.0015 | 0 | 0.9244 |
| pre_redacted | yes | 49 | 5 | 5 | 1.0000 * | 0.0000 | 0 | 0.8980 |
| split_span | no | 724 | 80 | 56 | 1.0000 | 0.0014 | 0 | 0.9227 |
| truncated | no | 724 | 80 | 56 | 1.0000 | 0.0014 | 0 | 0.9227 |

Value kinds of missed spans (false forwards):

none

### A / qs_v2, test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log | 263 | 27 | 42 | 1.0000 | 0.0152 | 0 | 0.8479 |
| doc_type | crf_page | 371 | 42 | 101 | 1.0000 | 0.0054 | 0 | 0.7278 |
| doc_type | csr_patient_narrative | 964 | 42 | 72 | 1.0000 | 0.0041 | 0 | 0.9357 |
| doc_type | delegation_log | 151 | 14 | 14 | 1.0000 * | 0.0132 | 0 | 0.9470 |
| doc_type | deviation_log | 203 | 23 | 23 | 1.0000 * | 0.0099 | 0 | 0.8916 |
| doc_type | icf_signature_page | 52 | 19 | 17 | 1.0000 * | 0.0000 | 0 | 0.7885 |
| doc_type | lab_report | 188 | 29 | 34 | 1.0000 | 0.0106 | 0 | 0.8404 |
| doc_type | monitoring_visit_report | 986 | 29 | 47 | 1.0000 | 0.0000 | 0 | 0.9533 |
| doc_type | protocol_section | 1240 | 41 | 0 | n/a | 0.0056 | 0 | 0.9992 |
| doc_type | sae_cioms | 300 | 36 | 38 | 1.0000 | 0.0033 | 0 | 0.8733 |
| doc_type | site_correspondence | 995 | 35 | 31 | 1.0000 | 0.0060 | 0 | 0.9698 |
| hard_negative | no | 4393 | 260 | 302 | 1.0000 | 0.0055 | 0 | 0.9356 |
| hard_negative | yes | 1320 | 77 | 117 | 1.0000 | 0.0045 | 0 | 0.9197 |
| lang | de | 33 | 22 | 26 | 1.0000 * | 0.0606 * | 0 | 0.3636 |
| lang | en | 5655 | 298 | 373 | 1.0000 | 0.0050 | 0 | 0.9383 |
| lang | es | 7 | 6 | 6 | 1.0000 * | 0.0000 * | 0 | 0.4286 |
| lang | pl | 18 | 11 | 14 | 1.0000 * | 0.0000 * | 0 | 0.1667 |
| length_bucket | long | 2513 | 80 | 70 | 1.0000 | 0.0032 | 0 | 0.9721 |
| length_bucket | medium | 1466 | 119 | 218 | 1.0000 | 0.0089 | 0 | 0.8595 |
| length_bucket | short | 287 | 108 | 99 | 1.0000 | 0.0105 | 0 | 0.7003 |
| length_bucket | xl | 1447 | 30 | 32 | 1.0000 | 0.0041 | 0 | 0.9813 |
| perturbation | email_quoting | 995 | 35 | 31 | 1.0000 | 0.0060 | 0 | 0.9698 |
| perturbation | headers_footers | 2405 | 132 | 156 | 1.0000 | 0.0050 | 0 | 0.9422 |
| perturbation | line_wrap | 1852 | 105 | 151 | 1.0000 | 0.0065 | 0 | 0.9266 |
| perturbation | none | 1421 | 93 | 104 | 1.0000 | 0.0049 | 0 | 0.9303 |
| perturbation | ocr_noise | 567 | 39 | 45 | 1.0000 | 0.0088 | 0 | 0.9206 |
| perturbation | table | 659 | 75 | 115 | 1.0000 | 0.0121 | 0 | 0.8240 |
| pii_depth | early | 282 | 8 | 11 | 1.0000 * | 0.0035 | 0 | 0.9645 |
| pii_depth | late | 582 | 16 | 21 | 1.0000 * | 0.0017 | 0 | 0.9656 |
| pii_depth | middle | 327 | 10 | 11 | 1.0000 * | 0.0031 | 0 | 0.9694 |
| pii_depth | none | 4522 | 303 | 376 | 1.0000 | 0.0060 | 0 | 0.9228 |
| pre_redacted | no | 5297 | 303 | 355 | 1.0000 | 0.0053 | 0 | 0.9379 |
| pre_redacted | yes | 416 | 34 | 64 | 1.0000 | 0.0048 | 0 | 0.8558 |
| split_span | no | 5695 | 337 | 402 | 1.0000 | 0.0053 | 0 | 0.9345 |
| split_span | yes | 18 | 17 | 17 | 1.0000 * | 0.0000 * | 0 | 0.1111 |
| truncated | no | 5713 | 337 | 419 | 1.0000 | 0.0053 | 0 | 0.9319 |

Value kinds of missed spans (false forwards):

none

### A / qs_v2, holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 724 | 80 | 56 | 1.0000 | 0.0014 | 0 | 0.9227 |
| hard_negative | no | 571 | 62 | 42 | 1.0000 | 0.0018 | 0 | 0.9264 |
| hard_negative | yes | 153 | 18 | 14 | 1.0000 * | 0.0000 | 0 | 0.9085 |
| lang | en | 724 | 80 | 56 | 1.0000 | 0.0014 | 0 | 0.9227 |
| length_bucket | medium | 596 | 47 | 34 | 1.0000 | 0.0000 | 0 | 0.9430 |
| length_bucket | short | 128 | 33 | 22 | 1.0000 * | 0.0078 | 0 | 0.8281 |
| perturbation | headers_footers | 307 | 35 | 25 | 1.0000 * | 0.0000 | 0 | 0.9186 |
| perturbation | line_wrap | 185 | 26 | 19 | 1.0000 * | 0.0054 | 0 | 0.8973 |
| perturbation | none | 290 | 28 | 19 | 1.0000 * | 0.0000 | 0 | 0.9345 |
| perturbation | ocr_noise | 48 | 7 | 6 | 1.0000 * | 0.0000 | 0 | 0.8750 |
| pii_depth | none | 724 | 80 | 56 | 1.0000 | 0.0014 | 0 | 0.9227 |
| pre_redacted | no | 675 | 75 | 51 | 1.0000 | 0.0015 | 0 | 0.9244 |
| pre_redacted | yes | 49 | 5 | 5 | 1.0000 * | 0.0000 | 0 | 0.8980 |
| split_span | no | 724 | 80 | 56 | 1.0000 | 0.0014 | 0 | 0.9227 |
| truncated | no | 724 | 80 | 56 | 1.0000 | 0.0014 | 0 | 0.9227 |

Value kinds of missed spans (false forwards):

none

### B1 / qs_v1, test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log | 92 | 27 | 21 | 1.0000 * | 0.0000 | 0 | 0.2283 |
| doc_type | crf_page | 166 | 42 | 62 | 1.0000 | 0.0120 | 0 | 0.4157 |
| doc_type | csr_patient_narrative | 309 | 42 | 56 | 1.0000 | 0.0000 | 0 | 0.1909 |
| doc_type | delegation_log | 51 | 14 | 14 | 1.0000 * | 0.0000 | 0 | 0.2745 |
| doc_type | deviation_log | 76 | 23 | 18 | 0.9444 * | 0.0000 | 0 | 0.2237 |
| doc_type | icf_signature_page | 23 | 19 | 14 | 1.0000 * | 0.0000 * | 0 | 0.5652 |
| doc_type | lab_report | 74 | 29 | 23 | 1.0000 * | 0.0000 | 0 | 0.3108 |
| doc_type | monitoring_visit_report | 314 | 29 | 43 | 1.0000 | 0.0000 | 0 | 0.1401 |
| doc_type | protocol_section | 391 | 41 | 0 | n/a | 0.0000 | 0 | 0.0077 |
| doc_type | sae_cioms | 106 | 36 | 32 | 1.0000 | 0.0000 | 0 | 0.2736 |
| doc_type | site_correspondence | 317 | 35 | 23 | 1.0000 * | 0.0000 | 0 | 0.0726 |
| hard_negative | no | 1470 | 260 | 227 | 0.9956 | 0.0007 | 0 | 0.1565 |
| hard_negative | yes | 449 | 77 | 79 | 1.0000 | 0.0022 | 0 | 0.1893 |
| lang | de | 22 | 22 | 19 | 1.0000 * | 0.0000 * | 0 | 0.6818 |
| lang | en | 1880 | 298 | 273 | 0.9963 | 0.0011 | 0 | 0.1537 |
| lang | es | 6 | 6 | 5 | 1.0000 * | 0.0000 * | 0 | 0.6667 |
| lang | pl | 11 | 11 | 9 | 1.0000 * | 0.0000 * | 0 | 0.6364 |
| length_bucket | long | 796 | 80 | 59 | 1.0000 | 0.0000 | 0 | 0.0817 |
| length_bucket | medium | 534 | 119 | 140 | 0.9929 | 0.0037 | 0 | 0.2772 |
| length_bucket | short | 137 | 108 | 78 | 1.0000 | 0.0000 | 0 | 0.5182 |
| length_bucket | xl | 452 | 30 | 29 | 1.0000 * | 0.0000 | 0 | 0.0686 |
| perturbation | email_quoting | 317 | 35 | 23 | 1.0000 * | 0.0000 | 0 | 0.0726 |
| perturbation | headers_footers | 797 | 132 | 111 | 1.0000 | 0.0013 | 0 | 0.1531 |
| perturbation | line_wrap | 619 | 105 | 115 | 0.9913 | 0.0000 | 0 | 0.1826 |
| perturbation | none | 476 | 93 | 74 | 1.0000 | 0.0021 | 0 | 0.1597 |
| perturbation | ocr_noise | 188 | 39 | 32 | 1.0000 | 0.0000 | 0 | 0.1755 |
| perturbation | table | 263 | 75 | 79 | 0.9873 | 0.0000 | 0 | 0.3118 |
| pii_depth | early | 90 | 8 | 8 | 1.0000 * | 0.0000 | 0 | 0.1111 |
| pii_depth | late | 182 | 16 | 18 | 1.0000 * | 0.0000 | 0 | 0.0989 |
| pii_depth | middle | 103 | 10 | 11 | 1.0000 * | 0.0000 | 0 | 0.1165 |
| pii_depth | none | 1544 | 303 | 269 | 0.9963 | 0.0013 | 0 | 0.1781 |
| pre_redacted | no | 1773 | 303 | 263 | 0.9962 | 0.0011 | 0 | 0.1534 |
| pre_redacted | yes | 146 | 34 | 43 | 1.0000 | 0.0000 | 0 | 0.2945 |
| split_span | no | 1902 | 337 | 290 | 0.9966 | 0.0011 | 0 | 0.1577 |
| split_span | yes | 17 | 14 | 16 | 1.0000 * | 0.0000 * | 0 | 0.8824 |
| truncated | no | 1919 | 337 | 306 | 0.9967 | 0.0010 | 0 | 0.1641 |

Value kinds of missed spans (false forwards):

none

### B1 / qs_v1, holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 249 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.2249 |
| hard_negative | no | 197 | 62 | 42 | 1.0000 | 0.0000 | 0 | 0.2132 |
| hard_negative | yes | 52 | 18 | 14 | 1.0000 * | 0.0000 | 0 | 0.2692 |
| lang | en | 249 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.2249 |
| length_bucket | medium | 197 | 47 | 34 | 1.0000 | 0.0000 | 0 | 0.1726 |
| length_bucket | short | 52 | 33 | 22 | 1.0000 * | 0.0000 | 0 | 0.4231 |
| perturbation | headers_footers | 107 | 35 | 25 | 1.0000 * | 0.0000 | 0 | 0.2336 |
| perturbation | line_wrap | 67 | 26 | 19 | 1.0000 * | 0.0000 | 0 | 0.2836 |
| perturbation | none | 98 | 28 | 19 | 1.0000 * | 0.0000 | 0 | 0.1939 |
| perturbation | ocr_noise | 15 | 7 | 6 | 1.0000 * | 0.0000 * | 0 | 0.4000 |
| pii_depth | none | 249 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.2249 |
| pre_redacted | no | 232 | 75 | 51 | 1.0000 | 0.0000 | 0 | 0.2198 |
| pre_redacted | yes | 17 | 5 | 5 | 1.0000 * | 0.0000 * | 0 | 0.2941 |
| split_span | no | 249 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.2249 |
| truncated | no | 249 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.2249 |

Value kinds of missed spans (false forwards):

none

### B1 / qs_v2, test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log | 92 | 27 | 21 | 1.0000 * | 0.0000 | 0 | 0.2283 |
| doc_type | crf_page | 166 | 42 | 62 | 1.0000 | 0.0241 | 0 | 0.4217 |
| doc_type | csr_patient_narrative | 309 | 42 | 56 | 1.0000 | 0.0000 | 0 | 0.1909 |
| doc_type | delegation_log | 51 | 14 | 14 | 1.0000 * | 0.0000 | 0 | 0.2745 |
| doc_type | deviation_log | 76 | 23 | 18 | 0.9444 * | 0.0132 | 1 | 0.2237 |
| doc_type | icf_signature_page | 23 | 19 | 14 | 1.0000 * | 0.0000 * | 0 | 0.5652 |
| doc_type | lab_report | 74 | 29 | 23 | 1.0000 * | 0.0000 | 0 | 0.3108 |
| doc_type | monitoring_visit_report | 314 | 29 | 43 | 1.0000 | 0.0000 | 0 | 0.1401 |
| doc_type | protocol_section | 391 | 41 | 0 | n/a | 0.0000 | 0 | 0.0077 |
| doc_type | sae_cioms | 106 | 36 | 32 | 1.0000 | 0.0000 | 0 | 0.2736 |
| doc_type | site_correspondence | 317 | 35 | 23 | 1.0000 * | 0.0000 | 0 | 0.0726 |
| hard_negative | no | 1470 | 260 | 227 | 0.9956 | 0.0020 | 1 | 0.1571 |
| hard_negative | yes | 449 | 77 | 79 | 1.0000 | 0.0045 | 0 | 0.1893 |
| lang | de | 22 | 22 | 19 | 1.0000 * | 0.0000 * | 0 | 0.6818 |
| lang | en | 1880 | 298 | 273 | 0.9963 | 0.0027 | 1 | 0.1543 |
| lang | es | 6 | 6 | 5 | 1.0000 * | 0.0000 * | 0 | 0.6667 |
| lang | pl | 11 | 11 | 9 | 1.0000 * | 0.0000 * | 0 | 0.6364 |
| length_bucket | long | 796 | 80 | 59 | 1.0000 | 0.0000 | 0 | 0.0817 |
| length_bucket | medium | 534 | 119 | 140 | 0.9929 | 0.0094 | 1 | 0.2790 |
| length_bucket | short | 137 | 108 | 78 | 1.0000 | 0.0000 | 0 | 0.5182 |
| length_bucket | xl | 452 | 30 | 29 | 1.0000 * | 0.0000 | 0 | 0.0686 |
| perturbation | email_quoting | 317 | 35 | 23 | 1.0000 * | 0.0000 | 0 | 0.0726 |
| perturbation | headers_footers | 797 | 132 | 111 | 1.0000 | 0.0013 | 0 | 0.1531 |
| perturbation | line_wrap | 619 | 105 | 115 | 0.9913 | 0.0016 | 1 | 0.1826 |
| perturbation | none | 476 | 93 | 74 | 1.0000 | 0.0063 | 0 | 0.1597 |
| perturbation | ocr_noise | 188 | 39 | 32 | 1.0000 | 0.0000 | 0 | 0.1755 |
| perturbation | table | 263 | 75 | 79 | 0.9873 | 0.0038 | 1 | 0.3156 |
| pii_depth | early | 90 | 8 | 8 | 1.0000 * | 0.0000 | 0 | 0.1111 |
| pii_depth | late | 182 | 16 | 18 | 1.0000 * | 0.0000 | 0 | 0.0989 |
| pii_depth | middle | 103 | 10 | 11 | 1.0000 * | 0.0000 | 0 | 0.1165 |
| pii_depth | none | 1544 | 303 | 269 | 0.9963 | 0.0032 | 1 | 0.1788 |
| pre_redacted | no | 1773 | 303 | 263 | 0.9962 | 0.0028 | 1 | 0.1540 |
| pre_redacted | yes | 146 | 34 | 43 | 1.0000 | 0.0000 | 0 | 0.2945 |
| split_span | no | 1902 | 337 | 290 | 0.9966 | 0.0026 | 1 | 0.1583 |
| split_span | yes | 17 | 14 | 16 | 1.0000 * | 0.0000 * | 0 | 0.8824 |
| truncated | no | 1919 | 337 | 306 | 0.9967 | 0.0026 | 1 | 0.1647 |

Value kinds of missed spans (false forwards):

| value_kind | false forwards |
|---|---|
| event_date | 1 |
| initials | 1 |

### B1 / qs_v2, holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 249 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.2249 |
| hard_negative | no | 197 | 62 | 42 | 1.0000 | 0.0000 | 0 | 0.2132 |
| hard_negative | yes | 52 | 18 | 14 | 1.0000 * | 0.0000 | 0 | 0.2692 |
| lang | en | 249 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.2249 |
| length_bucket | medium | 197 | 47 | 34 | 1.0000 | 0.0000 | 0 | 0.1726 |
| length_bucket | short | 52 | 33 | 22 | 1.0000 * | 0.0000 | 0 | 0.4231 |
| perturbation | headers_footers | 107 | 35 | 25 | 1.0000 * | 0.0000 | 0 | 0.2336 |
| perturbation | line_wrap | 67 | 26 | 19 | 1.0000 * | 0.0000 | 0 | 0.2836 |
| perturbation | none | 98 | 28 | 19 | 1.0000 * | 0.0000 | 0 | 0.1939 |
| perturbation | ocr_noise | 15 | 7 | 6 | 1.0000 * | 0.0000 * | 0 | 0.4000 |
| pii_depth | none | 249 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.2249 |
| pre_redacted | no | 232 | 75 | 51 | 1.0000 | 0.0000 | 0 | 0.2198 |
| pre_redacted | yes | 17 | 5 | 5 | 1.0000 * | 0.0000 * | 0 | 0.2941 |
| split_span | no | 249 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.2249 |
| truncated | no | 249 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.2249 |

Value kinds of missed spans (false forwards):

none

### B2 / qs_v1, test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log | 48 | 27 | 12 | 1.0000 * | 0.0000 | 0 | 0.2500 |
| doc_type | crf_page | 76 | 42 | 23 | 0.9565 * | 0.0132 | 1 | 0.3289 |
| doc_type | csr_patient_narrative | 145 | 42 | 45 | 1.0000 | 0.0000 | 0 | 0.2897 |
| doc_type | delegation_log | 26 | 14 | 14 | 1.0000 * | 0.0000 * | 0 | 0.5385 |
| doc_type | deviation_log | 41 | 23 | 13 | 1.0000 * | 0.0000 * | 0 | 0.2927 |
| doc_type | icf_signature_page | 19 | 19 | 14 | 1.0000 * | 0.0000 * | 0 | 0.6842 |
| doc_type | lab_report | 42 | 29 | 21 | 1.0000 * | 0.0000 * | 0 | 0.5000 |
| doc_type | monitoring_visit_report | 137 | 29 | 37 | 1.0000 | 0.0000 | 0 | 0.2628 |
| doc_type | protocol_section | 174 | 41 | 0 | n/a | 0.0000 | 0 | 0.0115 |
| doc_type | sae_cioms | 60 | 36 | 32 | 1.0000 | 0.0000 * | 0 | 0.5000 |
| doc_type | site_correspondence | 144 | 35 | 22 | 1.0000 * | 0.0000 | 0 | 0.1458 |
| hard_negative | no | 703 | 260 | 177 | 0.9944 | 0.0014 | 1 | 0.2447 |
| hard_negative | yes | 209 | 77 | 56 | 1.0000 | 0.0000 | 0 | 0.2679 |
| lang | de | 22 | 22 | 19 | 1.0000 * | 0.0000 * | 0 | 0.6818 |
| lang | en | 873 | 298 | 200 | 0.9950 | 0.0011 | 1 | 0.2314 |
| lang | es | 6 | 6 | 5 | 1.0000 * | 0.0000 * | 0 | 0.6667 |
| lang | pl | 11 | 11 | 9 | 1.0000 * | 0.0000 * | 0 | 0.6364 |
| length_bucket | long | 350 | 80 | 53 | 1.0000 | 0.0000 | 0 | 0.1543 |
| length_bucket | medium | 255 | 119 | 80 | 0.9875 | 0.0039 | 1 | 0.3216 |
| length_bucket | short | 108 | 108 | 77 | 1.0000 | 0.0000 | 0 | 0.6389 |
| length_bucket | xl | 199 | 30 | 23 | 1.0000 * | 0.0000 | 0 | 0.1156 |
| perturbation | email_quoting | 144 | 35 | 22 | 1.0000 * | 0.0000 | 0 | 0.1458 |
| perturbation | headers_footers | 380 | 132 | 87 | 0.9885 | 0.0026 | 1 | 0.2368 |
| perturbation | line_wrap | 291 | 105 | 82 | 1.0000 | 0.0000 | 0 | 0.2749 |
| perturbation | none | 229 | 93 | 62 | 1.0000 | 0.0000 | 0 | 0.2620 |
| perturbation | ocr_noise | 93 | 39 | 27 | 1.0000 * | 0.0000 | 0 | 0.2796 |
| perturbation | table | 135 | 75 | 47 | 1.0000 | 0.0000 | 0 | 0.3407 |
| pii_depth | early | 39 | 8 | 8 | 1.0000 * | 0.0000 | 0 | 0.2051 |
| pii_depth | late | 79 | 16 | 16 | 1.0000 * | 0.0000 | 0 | 0.2025 |
| pii_depth | middle | 45 | 10 | 10 | 1.0000 * | 0.0000 | 0 | 0.2222 |
| pii_depth | none | 749 | 303 | 199 | 0.9950 | 0.0013 | 1 | 0.2590 |
| pre_redacted | no | 836 | 303 | 205 | 0.9951 | 0.0012 | 1 | 0.2428 |
| pre_redacted | yes | 76 | 34 | 28 | 1.0000 * | 0.0000 | 0 | 0.3289 |
| split_span | no | 912 | 337 | 233 | 0.9957 | 0.0011 | 1 | 0.2500 |
| truncated | no | 898 | 336 | 225 | 0.9956 | 0.0011 | 1 | 0.2428 |
| truncated | yes | 14 | 14 | 8 | 1.0000 * | 0.0000 * | 0 | 0.7143 |

Value kinds of missed spans (false forwards):

| value_kind | false forwards |
|---|---|
| event_date | 1 |
| initials | 1 |

### B2 / qs_v1, holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 130 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.4308 |
| hard_negative | no | 101 | 62 | 42 | 1.0000 | 0.0000 | 0 | 0.4158 |
| hard_negative | yes | 29 | 18 | 14 | 1.0000 * | 0.0000 * | 0 | 0.4828 |
| lang | en | 130 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.4308 |
| length_bucket | medium | 97 | 47 | 34 | 1.0000 | 0.0000 | 0 | 0.3505 |
| length_bucket | short | 33 | 33 | 22 | 1.0000 * | 0.0000 * | 0 | 0.6667 |
| perturbation | headers_footers | 55 | 35 | 25 | 1.0000 * | 0.0000 | 0 | 0.4545 |
| perturbation | line_wrap | 36 | 26 | 19 | 1.0000 * | 0.0000 * | 0 | 0.5278 |
| perturbation | none | 52 | 28 | 19 | 1.0000 * | 0.0000 | 0 | 0.3654 |
| perturbation | ocr_noise | 9 | 7 | 6 | 1.0000 * | 0.0000 * | 0 | 0.6667 |
| pii_depth | none | 130 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.4308 |
| pre_redacted | no | 121 | 75 | 51 | 1.0000 | 0.0000 | 0 | 0.4215 |
| pre_redacted | yes | 9 | 5 | 5 | 1.0000 * | 0.0000 * | 0 | 0.5556 |
| split_span | no | 130 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.4308 |
| truncated | no | 130 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.4308 |

Value kinds of missed spans (false forwards):

none

### B2 / qs_v2, test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log | 48 | 27 | 12 | 1.0000 * | 0.0000 | 0 | 0.2500 |
| doc_type | crf_page | 76 | 42 | 23 | 0.9565 * | 0.0132 | 1 | 0.3289 |
| doc_type | csr_patient_narrative | 145 | 42 | 45 | 1.0000 | 0.0000 | 0 | 0.2897 |
| doc_type | delegation_log | 26 | 14 | 14 | 1.0000 * | 0.0000 * | 0 | 0.5385 |
| doc_type | deviation_log | 41 | 23 | 13 | 1.0000 * | 0.0000 * | 0 | 0.2927 |
| doc_type | icf_signature_page | 19 | 19 | 14 | 1.0000 * | 0.0000 * | 0 | 0.6842 |
| doc_type | lab_report | 42 | 29 | 21 | 1.0000 * | 0.0000 * | 0 | 0.5000 |
| doc_type | monitoring_visit_report | 137 | 29 | 37 | 1.0000 | 0.0000 | 0 | 0.2628 |
| doc_type | protocol_section | 174 | 41 | 0 | n/a | 0.0000 | 0 | 0.0115 |
| doc_type | sae_cioms | 60 | 36 | 32 | 1.0000 | 0.0000 * | 0 | 0.5000 |
| doc_type | site_correspondence | 144 | 35 | 22 | 1.0000 * | 0.0000 | 0 | 0.1458 |
| hard_negative | no | 703 | 260 | 177 | 0.9944 | 0.0014 | 1 | 0.2447 |
| hard_negative | yes | 209 | 77 | 56 | 1.0000 | 0.0000 | 0 | 0.2679 |
| lang | de | 22 | 22 | 19 | 1.0000 * | 0.0000 * | 0 | 0.6818 |
| lang | en | 873 | 298 | 200 | 0.9950 | 0.0011 | 1 | 0.2314 |
| lang | es | 6 | 6 | 5 | 1.0000 * | 0.0000 * | 0 | 0.6667 |
| lang | pl | 11 | 11 | 9 | 1.0000 * | 0.0000 * | 0 | 0.6364 |
| length_bucket | long | 350 | 80 | 53 | 1.0000 | 0.0000 | 0 | 0.1543 |
| length_bucket | medium | 255 | 119 | 80 | 0.9875 | 0.0039 | 1 | 0.3216 |
| length_bucket | short | 108 | 108 | 77 | 1.0000 | 0.0000 | 0 | 0.6389 |
| length_bucket | xl | 199 | 30 | 23 | 1.0000 * | 0.0000 | 0 | 0.1156 |
| perturbation | email_quoting | 144 | 35 | 22 | 1.0000 * | 0.0000 | 0 | 0.1458 |
| perturbation | headers_footers | 380 | 132 | 87 | 0.9885 | 0.0026 | 1 | 0.2368 |
| perturbation | line_wrap | 291 | 105 | 82 | 1.0000 | 0.0000 | 0 | 0.2749 |
| perturbation | none | 229 | 93 | 62 | 1.0000 | 0.0000 | 0 | 0.2620 |
| perturbation | ocr_noise | 93 | 39 | 27 | 1.0000 * | 0.0000 | 0 | 0.2796 |
| perturbation | table | 135 | 75 | 47 | 1.0000 | 0.0000 | 0 | 0.3407 |
| pii_depth | early | 39 | 8 | 8 | 1.0000 * | 0.0000 | 0 | 0.2051 |
| pii_depth | late | 79 | 16 | 16 | 1.0000 * | 0.0000 | 0 | 0.2025 |
| pii_depth | middle | 45 | 10 | 10 | 1.0000 * | 0.0000 | 0 | 0.2222 |
| pii_depth | none | 749 | 303 | 199 | 0.9950 | 0.0013 | 1 | 0.2590 |
| pre_redacted | no | 836 | 303 | 205 | 0.9951 | 0.0012 | 1 | 0.2428 |
| pre_redacted | yes | 76 | 34 | 28 | 1.0000 * | 0.0000 | 0 | 0.3289 |
| split_span | no | 912 | 337 | 233 | 0.9957 | 0.0011 | 1 | 0.2500 |
| truncated | no | 898 | 336 | 225 | 0.9956 | 0.0011 | 1 | 0.2428 |
| truncated | yes | 14 | 14 | 8 | 1.0000 * | 0.0000 * | 0 | 0.7143 |

Value kinds of missed spans (false forwards):

| value_kind | false forwards |
|---|---|
| event_date | 1 |
| initials | 1 |

### B2 / qs_v2, holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 130 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.4308 |
| hard_negative | no | 101 | 62 | 42 | 1.0000 | 0.0000 | 0 | 0.4158 |
| hard_negative | yes | 29 | 18 | 14 | 1.0000 * | 0.0000 * | 0 | 0.4828 |
| lang | en | 130 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.4308 |
| length_bucket | medium | 97 | 47 | 34 | 1.0000 | 0.0000 | 0 | 0.3505 |
| length_bucket | short | 33 | 33 | 22 | 1.0000 * | 0.0000 * | 0 | 0.6667 |
| perturbation | headers_footers | 55 | 35 | 25 | 1.0000 * | 0.0000 | 0 | 0.4545 |
| perturbation | line_wrap | 36 | 26 | 19 | 1.0000 * | 0.0000 * | 0 | 0.5278 |
| perturbation | none | 52 | 28 | 19 | 1.0000 * | 0.0000 | 0 | 0.3654 |
| perturbation | ocr_noise | 9 | 7 | 6 | 1.0000 * | 0.0000 * | 0 | 0.6667 |
| pii_depth | none | 130 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.4308 |
| pre_redacted | no | 121 | 75 | 51 | 1.0000 | 0.0000 | 0 | 0.4215 |
| pre_redacted | yes | 9 | 5 | 5 | 1.0000 * | 0.0000 * | 0 | 0.5556 |
| split_span | no | 130 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.4308 |
| truncated | no | 130 | 80 | 56 | 1.0000 | 0.0000 | 0 | 0.4308 |

Value kinds of missed spans (false forwards):

none

### B3 / qs_v1 (doc-level, underpowered), test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log | 32 | 27 | 12 | 1.0000 * | 0.0000 * | 0 | 0.3750 |
| doc_type | crf_page | 48 | 42 | 23 | 1.0000 * | 0.0208 * | 0 | 0.4167 |
| doc_type | csr_patient_narrative | 79 | 42 | 43 | 1.0000 | 0.0000 | 0 | 0.5190 |
| doc_type | delegation_log | 15 | 14 | 14 | 1.0000 * | 0.0000 * | 0 | 0.9333 |
| doc_type | deviation_log | 26 | 23 | 13 | 1.0000 * | 0.0000 * | 0 | 0.5000 |
| doc_type | icf_signature_page | 19 | 19 | 14 | 1.0000 * | 0.0000 * | 0 | 0.6842 |
| doc_type | lab_report | 30 | 29 | 21 | 1.0000 * | 0.0000 * | 0 | 0.6667 |
| doc_type | monitoring_visit_report | 70 | 29 | 36 | 1.0000 | 0.0000 | 0 | 0.4857 |
| doc_type | protocol_section | 90 | 41 | 0 | n/a | 0.0000 | 0 | 0.0000 |
| doc_type | sae_cioms | 38 | 36 | 32 | 1.0000 | 0.0000 * | 0 | 0.7632 |
| doc_type | site_correspondence | 78 | 35 | 22 | 1.0000 * | 0.0000 | 0 | 0.2821 |
| hard_negative | no | 407 | 260 | 174 | 1.0000 | 0.0025 | 0 | 0.4029 |
| hard_negative | yes | 118 | 77 | 56 | 1.0000 | 0.0000 | 0 | 0.4576 |
| lang | de | 22 | 22 | 19 | 1.0000 * | 0.0000 * | 0 | 0.6818 |
| lang | en | 486 | 298 | 197 | 1.0000 | 0.0021 | 0 | 0.3951 |
| lang | es | 6 | 6 | 5 | 1.0000 * | 0.0000 * | 0 | 0.6667 |
| lang | pl | 11 | 11 | 9 | 1.0000 * | 0.0000 * | 0 | 0.6364 |
| length_bucket | long | 187 | 80 | 53 | 1.0000 | 0.0000 | 0 | 0.2781 |
| length_bucket | medium | 140 | 119 | 78 | 1.0000 | 0.0071 | 0 | 0.5357 |
| length_bucket | short | 108 | 108 | 77 | 1.0000 | 0.0000 | 0 | 0.6389 |
| length_bucket | xl | 90 | 30 | 22 | 1.0000 * | 0.0000 | 0 | 0.2444 |
| perturbation | email_quoting | 78 | 35 | 22 | 1.0000 * | 0.0000 | 0 | 0.2821 |
| perturbation | headers_footers | 216 | 132 | 87 | 1.0000 | 0.0046 | 0 | 0.3935 |
| perturbation | line_wrap | 168 | 105 | 78 | 1.0000 | 0.0060 | 0 | 0.4286 |
| perturbation | none | 135 | 93 | 62 | 1.0000 | 0.0000 | 0 | 0.4370 |
| perturbation | ocr_noise | 57 | 39 | 26 | 1.0000 * | 0.0000 | 0 | 0.4386 |
| perturbation | table | 87 | 75 | 47 | 1.0000 | 0.0115 | 0 | 0.5057 |
| pii_depth | early | 21 | 8 | 8 | 1.0000 * | 0.0000 * | 0 | 0.3810 |
| pii_depth | late | 40 | 16 | 16 | 1.0000 * | 0.0000 * | 0 | 0.4000 |
| pii_depth | middle | 24 | 10 | 10 | 1.0000 * | 0.0000 * | 0 | 0.4167 |
| pii_depth | none | 440 | 303 | 196 | 1.0000 | 0.0023 | 0 | 0.4182 |
| pre_redacted | no | 480 | 303 | 202 | 1.0000 | 0.0021 | 0 | 0.4000 |
| pre_redacted | yes | 45 | 34 | 28 | 1.0000 * | 0.0000 * | 0 | 0.5778 |
| split_span | no | 525 | 337 | 230 | 1.0000 | 0.0019 | 0 | 0.4152 |
| truncated | no | 525 | 337 | 230 | 1.0000 | 0.0019 | 0 | 0.4152 |

Value kinds of missed spans (false forwards):

none

### B3 / qs_v1 (doc-level, underpowered), holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 84 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.6667 |
| hard_negative | no | 66 | 62 | 42 | 1.0000 | 0.0000 * | 0 | 0.6364 |
| hard_negative | yes | 18 | 18 | 14 | 1.0000 * | 0.0000 * | 0 | 0.7778 |
| lang | en | 84 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.6667 |
| length_bucket | medium | 51 | 47 | 34 | 1.0000 | 0.0000 * | 0 | 0.6667 |
| length_bucket | short | 33 | 33 | 22 | 1.0000 * | 0.0000 * | 0 | 0.6667 |
| perturbation | headers_footers | 36 | 35 | 25 | 1.0000 * | 0.0000 * | 0 | 0.6944 |
| perturbation | line_wrap | 27 | 26 | 19 | 1.0000 * | 0.0000 * | 0 | 0.7037 |
| perturbation | none | 30 | 28 | 19 | 1.0000 * | 0.0000 * | 0 | 0.6333 |
| perturbation | ocr_noise | 7 | 7 | 6 | 1.0000 * | 0.0000 * | 0 | 0.8571 |
| pii_depth | none | 84 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.6667 |
| pre_redacted | no | 78 | 75 | 51 | 1.0000 | 0.0000 * | 0 | 0.6538 |
| pre_redacted | yes | 6 | 5 | 5 | 1.0000 * | 0.0000 * | 0 | 0.8333 |
| split_span | no | 84 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.6667 |
| truncated | no | 84 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.6667 |

Value kinds of missed spans (false forwards):

none

### B3 / qs_v2 (doc-level, underpowered), test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log | 32 | 27 | 12 | 1.0000 * | 0.0000 * | 0 | 0.3750 |
| doc_type | crf_page | 48 | 42 | 23 | 1.0000 * | 0.0208 * | 0 | 0.4167 |
| doc_type | csr_patient_narrative | 79 | 42 | 43 | 1.0000 | 0.0000 | 0 | 0.5190 |
| doc_type | delegation_log | 15 | 14 | 14 | 1.0000 * | 0.0000 * | 0 | 0.9333 |
| doc_type | deviation_log | 26 | 23 | 13 | 1.0000 * | 0.0000 * | 0 | 0.5000 |
| doc_type | icf_signature_page | 19 | 19 | 14 | 1.0000 * | 0.0000 * | 0 | 0.6842 |
| doc_type | lab_report | 30 | 29 | 21 | 1.0000 * | 0.0000 * | 0 | 0.6667 |
| doc_type | monitoring_visit_report | 70 | 29 | 36 | 1.0000 | 0.0000 | 0 | 0.4857 |
| doc_type | protocol_section | 90 | 41 | 0 | n/a | 0.0000 | 0 | 0.0000 |
| doc_type | sae_cioms | 38 | 36 | 32 | 1.0000 | 0.0000 * | 0 | 0.7632 |
| doc_type | site_correspondence | 78 | 35 | 22 | 1.0000 * | 0.0000 | 0 | 0.2821 |
| hard_negative | no | 407 | 260 | 174 | 1.0000 | 0.0025 | 0 | 0.4029 |
| hard_negative | yes | 118 | 77 | 56 | 1.0000 | 0.0000 | 0 | 0.4576 |
| lang | de | 22 | 22 | 19 | 1.0000 * | 0.0000 * | 0 | 0.6818 |
| lang | en | 486 | 298 | 197 | 1.0000 | 0.0021 | 0 | 0.3951 |
| lang | es | 6 | 6 | 5 | 1.0000 * | 0.0000 * | 0 | 0.6667 |
| lang | pl | 11 | 11 | 9 | 1.0000 * | 0.0000 * | 0 | 0.6364 |
| length_bucket | long | 187 | 80 | 53 | 1.0000 | 0.0000 | 0 | 0.2781 |
| length_bucket | medium | 140 | 119 | 78 | 1.0000 | 0.0071 | 0 | 0.5357 |
| length_bucket | short | 108 | 108 | 77 | 1.0000 | 0.0000 | 0 | 0.6389 |
| length_bucket | xl | 90 | 30 | 22 | 1.0000 * | 0.0000 | 0 | 0.2444 |
| perturbation | email_quoting | 78 | 35 | 22 | 1.0000 * | 0.0000 | 0 | 0.2821 |
| perturbation | headers_footers | 216 | 132 | 87 | 1.0000 | 0.0046 | 0 | 0.3935 |
| perturbation | line_wrap | 168 | 105 | 78 | 1.0000 | 0.0060 | 0 | 0.4286 |
| perturbation | none | 135 | 93 | 62 | 1.0000 | 0.0000 | 0 | 0.4370 |
| perturbation | ocr_noise | 57 | 39 | 26 | 1.0000 * | 0.0000 | 0 | 0.4386 |
| perturbation | table | 87 | 75 | 47 | 1.0000 | 0.0115 | 0 | 0.5057 |
| pii_depth | early | 21 | 8 | 8 | 1.0000 * | 0.0000 * | 0 | 0.3810 |
| pii_depth | late | 40 | 16 | 16 | 1.0000 * | 0.0000 * | 0 | 0.4000 |
| pii_depth | middle | 24 | 10 | 10 | 1.0000 * | 0.0000 * | 0 | 0.4167 |
| pii_depth | none | 440 | 303 | 196 | 1.0000 | 0.0023 | 0 | 0.4182 |
| pre_redacted | no | 480 | 303 | 202 | 1.0000 | 0.0021 | 0 | 0.4000 |
| pre_redacted | yes | 45 | 34 | 28 | 1.0000 * | 0.0000 * | 0 | 0.5778 |
| split_span | no | 525 | 337 | 230 | 1.0000 | 0.0019 | 0 | 0.4152 |
| truncated | no | 525 | 337 | 230 | 1.0000 | 0.0019 | 0 | 0.4152 |

Value kinds of missed spans (false forwards):

none

### B3 / qs_v2 (doc-level, underpowered), holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 84 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.6667 |
| hard_negative | no | 66 | 62 | 42 | 1.0000 | 0.0000 * | 0 | 0.6364 |
| hard_negative | yes | 18 | 18 | 14 | 1.0000 * | 0.0000 * | 0 | 0.7778 |
| lang | en | 84 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.6667 |
| length_bucket | medium | 51 | 47 | 34 | 1.0000 | 0.0000 * | 0 | 0.6667 |
| length_bucket | short | 33 | 33 | 22 | 1.0000 * | 0.0000 * | 0 | 0.6667 |
| perturbation | headers_footers | 36 | 35 | 25 | 1.0000 * | 0.0000 * | 0 | 0.6944 |
| perturbation | line_wrap | 27 | 26 | 19 | 1.0000 * | 0.0000 * | 0 | 0.7037 |
| perturbation | none | 30 | 28 | 19 | 1.0000 * | 0.0000 * | 0 | 0.6333 |
| perturbation | ocr_noise | 7 | 7 | 6 | 1.0000 * | 0.0000 * | 0 | 0.8571 |
| pii_depth | none | 84 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.6667 |
| pre_redacted | no | 78 | 75 | 51 | 1.0000 | 0.0000 * | 0 | 0.6538 |
| pre_redacted | yes | 6 | 5 | 5 | 1.0000 * | 0.0000 * | 0 | 0.8333 |
| split_span | no | 84 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.6667 |
| truncated | no | 84 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.6667 |

Value kinds of missed spans (false forwards):

none

### B4 / qs_v1 (doc-level, underpowered), test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log | 27 | 27 | 12 | 1.0000 * | 0.0000 * | 0 | 0.4444 |
| doc_type | crf_page | 42 | 42 | 23 | 1.0000 * | 0.0000 * | 0 | 0.4524 |
| doc_type | csr_patient_narrative | 42 | 42 | 39 | 1.0000 | 0.0000 * | 0 | 0.8810 |
| doc_type | delegation_log | 14 | 14 | 14 | 1.0000 * | 0.0000 * | 0 | 1.0000 |
| doc_type | deviation_log | 23 | 23 | 13 | 1.0000 * | 0.0000 * | 0 | 0.5652 |
| doc_type | icf_signature_page | 19 | 19 | 14 | 1.0000 * | 0.0000 * | 0 | 0.6842 |
| doc_type | lab_report | 29 | 29 | 21 | 1.0000 * | 0.0000 * | 0 | 0.6897 |
| doc_type | monitoring_visit_report | 29 | 29 | 25 | 1.0000 * | 0.0000 * | 0 | 0.8621 |
| doc_type | protocol_section | 41 | 41 | 0 | n/a | 0.0000 | 0 | 0.0000 |
| doc_type | sae_cioms | 36 | 36 | 32 | 1.0000 | 0.0000 * | 0 | 0.8056 |
| doc_type | site_correspondence | 35 | 35 | 22 | 1.0000 * | 0.0000 * | 0 | 0.6286 |
| hard_negative | no | 260 | 260 | 163 | 1.0000 | 0.0000 | 0 | 0.5923 |
| hard_negative | yes | 77 | 77 | 52 | 1.0000 | 0.0000 * | 0 | 0.6494 |
| lang | de | 22 | 22 | 19 | 1.0000 * | 0.0000 * | 0 | 0.6818 |
| lang | en | 298 | 298 | 182 | 1.0000 | 0.0000 | 0 | 0.5973 |
| lang | es | 6 | 6 | 5 | 1.0000 * | 0.0000 * | 0 | 0.6667 |
| lang | pl | 11 | 11 | 9 | 1.0000 * | 0.0000 * | 0 | 0.6364 |
| length_bucket | long | 80 | 80 | 43 | 1.0000 | 0.0000 | 0 | 0.5375 |
| length_bucket | medium | 119 | 119 | 77 | 1.0000 | 0.0000 | 0 | 0.6218 |
| length_bucket | short | 108 | 108 | 77 | 1.0000 | 0.0000 | 0 | 0.6389 |
| length_bucket | xl | 30 | 30 | 18 | 1.0000 * | 0.0000 * | 0 | 0.6000 |
| perturbation | email_quoting | 35 | 35 | 22 | 1.0000 * | 0.0000 * | 0 | 0.6286 |
| perturbation | headers_footers | 132 | 132 | 81 | 1.0000 | 0.0000 | 0 | 0.5985 |
| perturbation | line_wrap | 105 | 105 | 71 | 1.0000 | 0.0000 | 0 | 0.6190 |
| perturbation | none | 93 | 93 | 58 | 1.0000 | 0.0000 | 0 | 0.6022 |
| perturbation | ocr_noise | 39 | 39 | 25 | 1.0000 * | 0.0000 * | 0 | 0.6154 |
| perturbation | table | 75 | 75 | 47 | 1.0000 | 0.0000 * | 0 | 0.5733 |
| pii_depth | early | 8 | 8 | 8 | 1.0000 * | 0.0000 * | 0 | 1.0000 |
| pii_depth | late | 16 | 16 | 16 | 1.0000 * | 0.0000 * | 0 | 1.0000 |
| pii_depth | middle | 10 | 10 | 10 | 1.0000 * | 0.0000 * | 0 | 1.0000 |
| pii_depth | none | 303 | 303 | 181 | 1.0000 | 0.0000 | 0 | 0.5611 |
| pre_redacted | no | 303 | 303 | 189 | 1.0000 | 0.0000 | 0 | 0.5941 |
| pre_redacted | yes | 34 | 34 | 26 | 1.0000 * | 0.0000 * | 0 | 0.7059 |
| split_span | no | 337 | 337 | 215 | 1.0000 | 0.0000 | 0 | 0.6053 |
| truncated | no | 307 | 307 | 197 | 1.0000 | 0.0000 | 0 | 0.6059 |
| truncated | yes | 30 | 30 | 18 | 1.0000 * | 0.0000 * | 0 | 0.6000 |

Value kinds of missed spans (false forwards):

none

### B4 / qs_v1 (doc-level, underpowered), holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 80 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.7000 |
| hard_negative | no | 62 | 62 | 42 | 1.0000 | 0.0000 * | 0 | 0.6774 |
| hard_negative | yes | 18 | 18 | 14 | 1.0000 * | 0.0000 * | 0 | 0.7778 |
| lang | en | 80 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.7000 |
| length_bucket | medium | 47 | 47 | 34 | 1.0000 | 0.0000 * | 0 | 0.7234 |
| length_bucket | short | 33 | 33 | 22 | 1.0000 * | 0.0000 * | 0 | 0.6667 |
| perturbation | headers_footers | 35 | 35 | 25 | 1.0000 * | 0.0000 * | 0 | 0.7143 |
| perturbation | line_wrap | 26 | 26 | 19 | 1.0000 * | 0.0000 * | 0 | 0.7308 |
| perturbation | none | 28 | 28 | 19 | 1.0000 * | 0.0000 * | 0 | 0.6786 |
| perturbation | ocr_noise | 7 | 7 | 6 | 1.0000 * | 0.0000 * | 0 | 0.8571 |
| pii_depth | none | 80 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.7000 |
| pre_redacted | no | 75 | 75 | 51 | 1.0000 | 0.0000 * | 0 | 0.6800 |
| pre_redacted | yes | 5 | 5 | 5 | 1.0000 * | 0.0000 * | 0 | 1.0000 |
| split_span | no | 80 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.7000 |
| truncated | no | 80 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.7000 |

Value kinds of missed spans (false forwards):

none

### B4 / qs_v2 (doc-level, underpowered), test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log | 27 | 27 | 12 | 1.0000 * | 0.0000 * | 0 | 0.4444 |
| doc_type | crf_page | 42 | 42 | 23 | 1.0000 * | 0.0000 * | 0 | 0.4524 |
| doc_type | csr_patient_narrative | 42 | 42 | 39 | 1.0000 | 0.0000 * | 0 | 0.8810 |
| doc_type | delegation_log | 14 | 14 | 14 | 1.0000 * | 0.0000 * | 0 | 1.0000 |
| doc_type | deviation_log | 23 | 23 | 13 | 1.0000 * | 0.0000 * | 0 | 0.5652 |
| doc_type | icf_signature_page | 19 | 19 | 14 | 1.0000 * | 0.0000 * | 0 | 0.6842 |
| doc_type | lab_report | 29 | 29 | 21 | 1.0000 * | 0.0000 * | 0 | 0.6897 |
| doc_type | monitoring_visit_report | 29 | 29 | 25 | 1.0000 * | 0.0000 * | 0 | 0.8621 |
| doc_type | protocol_section | 41 | 41 | 0 | n/a | 0.0000 | 0 | 0.0000 |
| doc_type | sae_cioms | 36 | 36 | 32 | 1.0000 | 0.0000 * | 0 | 0.8056 |
| doc_type | site_correspondence | 35 | 35 | 22 | 1.0000 * | 0.0000 * | 0 | 0.6286 |
| hard_negative | no | 260 | 260 | 163 | 1.0000 | 0.0000 | 0 | 0.5923 |
| hard_negative | yes | 77 | 77 | 52 | 1.0000 | 0.0000 * | 0 | 0.6494 |
| lang | de | 22 | 22 | 19 | 1.0000 * | 0.0000 * | 0 | 0.6818 |
| lang | en | 298 | 298 | 182 | 1.0000 | 0.0000 | 0 | 0.5973 |
| lang | es | 6 | 6 | 5 | 1.0000 * | 0.0000 * | 0 | 0.6667 |
| lang | pl | 11 | 11 | 9 | 1.0000 * | 0.0000 * | 0 | 0.6364 |
| length_bucket | long | 80 | 80 | 43 | 1.0000 | 0.0000 | 0 | 0.5375 |
| length_bucket | medium | 119 | 119 | 77 | 1.0000 | 0.0000 | 0 | 0.6218 |
| length_bucket | short | 108 | 108 | 77 | 1.0000 | 0.0000 | 0 | 0.6389 |
| length_bucket | xl | 30 | 30 | 18 | 1.0000 * | 0.0000 * | 0 | 0.6000 |
| perturbation | email_quoting | 35 | 35 | 22 | 1.0000 * | 0.0000 * | 0 | 0.6286 |
| perturbation | headers_footers | 132 | 132 | 81 | 1.0000 | 0.0000 | 0 | 0.5985 |
| perturbation | line_wrap | 105 | 105 | 71 | 1.0000 | 0.0000 | 0 | 0.6190 |
| perturbation | none | 93 | 93 | 58 | 1.0000 | 0.0000 | 0 | 0.6022 |
| perturbation | ocr_noise | 39 | 39 | 25 | 1.0000 * | 0.0000 * | 0 | 0.6154 |
| perturbation | table | 75 | 75 | 47 | 1.0000 | 0.0000 * | 0 | 0.5733 |
| pii_depth | early | 8 | 8 | 8 | 1.0000 * | 0.0000 * | 0 | 1.0000 |
| pii_depth | late | 16 | 16 | 16 | 1.0000 * | 0.0000 * | 0 | 1.0000 |
| pii_depth | middle | 10 | 10 | 10 | 1.0000 * | 0.0000 * | 0 | 1.0000 |
| pii_depth | none | 303 | 303 | 181 | 1.0000 | 0.0000 | 0 | 0.5611 |
| pre_redacted | no | 303 | 303 | 189 | 1.0000 | 0.0000 | 0 | 0.5941 |
| pre_redacted | yes | 34 | 34 | 26 | 1.0000 * | 0.0000 * | 0 | 0.7059 |
| split_span | no | 337 | 337 | 215 | 1.0000 | 0.0000 | 0 | 0.6053 |
| truncated | no | 307 | 307 | 197 | 1.0000 | 0.0000 | 0 | 0.6059 |
| truncated | yes | 30 | 30 | 18 | 1.0000 * | 0.0000 * | 0 | 0.6000 |

Value kinds of missed spans (false forwards):

none

### B4 / qs_v2 (doc-level, underpowered), holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 80 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.7000 |
| hard_negative | no | 62 | 62 | 42 | 1.0000 | 0.0000 * | 0 | 0.6774 |
| hard_negative | yes | 18 | 18 | 14 | 1.0000 * | 0.0000 * | 0 | 0.7778 |
| lang | en | 80 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.7000 |
| length_bucket | medium | 47 | 47 | 34 | 1.0000 | 0.0000 * | 0 | 0.7234 |
| length_bucket | short | 33 | 33 | 22 | 1.0000 * | 0.0000 * | 0 | 0.6667 |
| perturbation | headers_footers | 35 | 35 | 25 | 1.0000 * | 0.0000 * | 0 | 0.7143 |
| perturbation | line_wrap | 26 | 26 | 19 | 1.0000 * | 0.0000 * | 0 | 0.7308 |
| perturbation | none | 28 | 28 | 19 | 1.0000 * | 0.0000 * | 0 | 0.6786 |
| perturbation | ocr_noise | 7 | 7 | 6 | 1.0000 * | 0.0000 * | 0 | 0.8571 |
| pii_depth | none | 80 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.7000 |
| pre_redacted | no | 75 | 75 | 51 | 1.0000 | 0.0000 * | 0 | 0.6800 |
| pre_redacted | yes | 5 | 5 | 5 | 1.0000 * | 0.0000 * | 0 | 1.0000 |
| split_span | no | 80 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.7000 |
| truncated | no | 80 | 80 | 56 | 1.0000 | 0.0000 * | 0 | 0.7000 |

Value kinds of missed spans (false forwards):

none

### C / qs_v1, test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log | 263 | 27 | 42 | 1.0000 | 0.8403 | 0 | 1.0000 |
| doc_type | crf_page | 371 | 42 | 101 | 0.9901 | 0.7305 | 1 | 0.9973 |
| doc_type | csr_patient_narrative | 964 | 42 | 72 | 0.9861 | 0.9243 | 0 | 1.0000 |
| doc_type | delegation_log | 151 | 14 | 14 | 1.0000 * | 0.9073 | 0 | 1.0000 |
| doc_type | deviation_log | 203 | 23 | 23 | 1.0000 * | 0.8867 | 0 | 1.0000 |
| doc_type | icf_signature_page | 52 | 19 | 17 | 1.0000 * | 0.6538 | 0 | 0.9808 |
| doc_type | lab_report | 188 | 29 | 34 | 1.0000 | 0.8085 | 0 | 0.9894 |
| doc_type | monitoring_visit_report | 986 | 29 | 47 | 1.0000 | 0.9523 | 0 | 1.0000 |
| doc_type | protocol_section | 1240 | 41 | 0 | n/a | 1.0000 | 0 | 1.0000 |
| doc_type | sae_cioms | 300 | 36 | 38 | 1.0000 | 0.8700 | 0 | 0.9967 |
| doc_type | site_correspondence | 995 | 35 | 31 | 1.0000 | 0.9678 | 0 | 0.9980 |
| hard_negative | no | 4393 | 260 | 302 | 0.9934 | 0.9306 | 1 | 0.9991 |
| hard_negative | yes | 1320 | 77 | 117 | 1.0000 | 0.9098 | 0 | 0.9977 |
| lang | de | 33 | 22 | 26 | 1.0000 * | 0.1818 * | 0 | 0.9697 |
| lang | en | 5655 | 298 | 373 | 0.9946 | 0.9337 | 1 | 0.9993 |
| lang | es | 7 | 6 | 6 | 1.0000 * | 0.1429 * | 0 | 1.0000 |
| lang | pl | 18 | 11 | 14 | 1.0000 * | 0.1111 * | 0 | 0.8889 |
| length_bucket | long | 2513 | 80 | 70 | 0.9857 | 0.9713 | 0 | 0.9992 |
| length_bucket | medium | 1466 | 119 | 218 | 0.9954 | 0.8520 | 1 | 0.9993 |
| length_bucket | short | 287 | 108 | 99 | 1.0000 | 0.6411 | 0 | 0.9861 |
| length_bucket | xl | 1447 | 30 | 32 | 1.0000 | 0.9779 | 0 | 1.0000 |
| perturbation | email_quoting | 995 | 35 | 31 | 1.0000 | 0.9678 | 0 | 0.9980 |
| perturbation | headers_footers | 2405 | 132 | 156 | 0.9936 | 0.9343 | 0 | 0.9988 |
| perturbation | line_wrap | 1852 | 105 | 151 | 1.0000 | 0.9174 | 0 | 0.9989 |
| perturbation | none | 1421 | 93 | 104 | 0.9904 | 0.9275 | 1 | 0.9993 |
| perturbation | ocr_noise | 567 | 39 | 45 | 1.0000 | 0.9171 | 0 | 0.9965 |
| perturbation | table | 659 | 75 | 115 | 1.0000 | 0.8225 | 0 | 0.9970 |
| pii_depth | early | 282 | 8 | 11 | 1.0000 * | 0.9610 | 0 | 1.0000 |
| pii_depth | late | 582 | 16 | 21 | 1.0000 * | 0.9639 | 0 | 1.0000 |
| pii_depth | middle | 327 | 10 | 11 | 1.0000 * | 0.9602 | 0 | 0.9969 |
| pii_depth | none | 4522 | 303 | 376 | 0.9947 | 0.9162 | 1 | 0.9987 |
| pre_redacted | no | 5297 | 303 | 355 | 0.9944 | 0.9320 | 1 | 0.9987 |
| pre_redacted | yes | 416 | 34 | 64 | 1.0000 | 0.8462 | 0 | 1.0000 |
| split_span | no | 5695 | 337 | 402 | 0.9950 | 0.9285 | 1 | 0.9988 |
| split_span | yes | 18 | 17 | 17 | 1.0000 * | 0.0556 * | 0 | 1.0000 |
| truncated | no | 5713 | 337 | 419 | 0.9952 | 0.9258 | 1 | 0.9988 |

Value kinds of missed spans (false forwards):

| value_kind | false forwards |
|---|---|
| initials | 1 |

### C / qs_v1, holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 724 | 80 | 56 | 1.0000 | 0.9171 | 0 | 0.9834 |
| hard_negative | no | 571 | 62 | 42 | 1.0000 | 0.9212 | 0 | 0.9825 |
| hard_negative | yes | 153 | 18 | 14 | 1.0000 * | 0.9020 | 0 | 0.9869 |
| lang | en | 724 | 80 | 56 | 1.0000 | 0.9171 | 0 | 0.9834 |
| length_bucket | medium | 596 | 47 | 34 | 1.0000 | 0.9396 | 0 | 0.9866 |
| length_bucket | short | 128 | 33 | 22 | 1.0000 * | 0.8125 | 0 | 0.9688 |
| perturbation | headers_footers | 307 | 35 | 25 | 1.0000 * | 0.9055 | 0 | 0.9707 |
| perturbation | line_wrap | 185 | 26 | 19 | 1.0000 * | 0.8919 | 0 | 0.9892 |
| perturbation | none | 290 | 28 | 19 | 1.0000 * | 0.9345 | 0 | 0.9897 |
| perturbation | ocr_noise | 48 | 7 | 6 | 1.0000 * | 0.8750 | 0 | 1.0000 |
| pii_depth | none | 724 | 80 | 56 | 1.0000 | 0.9171 | 0 | 0.9834 |
| pre_redacted | no | 675 | 75 | 51 | 1.0000 | 0.9185 | 0 | 0.9822 |
| pre_redacted | yes | 49 | 5 | 5 | 1.0000 * | 0.8980 | 0 | 1.0000 |
| split_span | no | 724 | 80 | 56 | 1.0000 | 0.9171 | 0 | 0.9834 |
| truncated | no | 724 | 80 | 56 | 1.0000 | 0.9171 | 0 | 0.9834 |

Value kinds of missed spans (false forwards):

none

### C / qs_v2, test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log | 263 | 27 | 42 | 1.0000 | 0.8403 | 0 | 1.0000 |
| doc_type | crf_page | 371 | 42 | 101 | 0.9901 | 0.7305 | 1 | 0.9973 |
| doc_type | csr_patient_narrative | 964 | 42 | 72 | 0.9861 | 0.9263 | 1 | 1.0000 |
| doc_type | delegation_log | 151 | 14 | 14 | 1.0000 * | 0.9073 | 0 | 1.0000 |
| doc_type | deviation_log | 203 | 23 | 23 | 1.0000 * | 0.8867 | 0 | 1.0000 |
| doc_type | icf_signature_page | 52 | 19 | 17 | 1.0000 * | 0.6538 | 0 | 0.9808 |
| doc_type | lab_report | 188 | 29 | 34 | 1.0000 | 0.8085 | 0 | 0.9894 |
| doc_type | monitoring_visit_report | 986 | 29 | 47 | 1.0000 | 0.9523 | 0 | 1.0000 |
| doc_type | protocol_section | 1240 | 41 | 0 | n/a | 1.0000 | 0 | 1.0000 |
| doc_type | sae_cioms | 300 | 36 | 38 | 1.0000 | 0.8733 | 0 | 0.9967 |
| doc_type | site_correspondence | 995 | 35 | 31 | 1.0000 | 0.9678 | 0 | 0.9980 |
| hard_negative | no | 4393 | 260 | 302 | 0.9934 | 0.9313 | 2 | 0.9991 |
| hard_negative | yes | 1320 | 77 | 117 | 1.0000 | 0.9098 | 0 | 0.9977 |
| lang | de | 33 | 22 | 26 | 1.0000 * | 0.1818 * | 0 | 0.9697 |
| lang | en | 5655 | 298 | 373 | 0.9946 | 0.9342 | 2 | 0.9993 |
| lang | es | 7 | 6 | 6 | 1.0000 * | 0.1429 * | 0 | 1.0000 |
| lang | pl | 18 | 11 | 14 | 1.0000 * | 0.1111 * | 0 | 0.8889 |
| length_bucket | long | 2513 | 80 | 70 | 0.9857 | 0.9721 | 1 | 0.9992 |
| length_bucket | medium | 1466 | 119 | 218 | 0.9954 | 0.8520 | 1 | 0.9993 |
| length_bucket | short | 287 | 108 | 99 | 1.0000 | 0.6446 | 0 | 0.9861 |
| length_bucket | xl | 1447 | 30 | 32 | 1.0000 | 0.9779 | 0 | 1.0000 |
| perturbation | email_quoting | 995 | 35 | 31 | 1.0000 | 0.9678 | 0 | 0.9980 |
| perturbation | headers_footers | 2405 | 132 | 156 | 0.9936 | 0.9347 | 1 | 0.9988 |
| perturbation | line_wrap | 1852 | 105 | 151 | 1.0000 | 0.9185 | 0 | 0.9989 |
| perturbation | none | 1421 | 93 | 104 | 0.9904 | 0.9275 | 1 | 0.9993 |
| perturbation | ocr_noise | 567 | 39 | 45 | 1.0000 | 0.9171 | 0 | 0.9965 |
| perturbation | table | 659 | 75 | 115 | 1.0000 | 0.8225 | 0 | 0.9970 |
| pii_depth | early | 282 | 8 | 11 | 1.0000 * | 0.9610 | 0 | 1.0000 |
| pii_depth | late | 582 | 16 | 21 | 1.0000 * | 0.9639 | 0 | 1.0000 |
| pii_depth | middle | 327 | 10 | 11 | 1.0000 * | 0.9633 | 0 | 0.9969 |
| pii_depth | none | 4522 | 303 | 376 | 0.9947 | 0.9166 | 2 | 0.9987 |
| pre_redacted | no | 5297 | 303 | 355 | 0.9944 | 0.9326 | 2 | 0.9987 |
| pre_redacted | yes | 416 | 34 | 64 | 1.0000 | 0.8462 | 0 | 1.0000 |
| split_span | no | 5695 | 337 | 402 | 0.9950 | 0.9291 | 2 | 0.9988 |
| split_span | yes | 18 | 17 | 17 | 1.0000 * | 0.0556 * | 0 | 1.0000 |
| truncated | no | 5713 | 337 | 419 | 0.9952 | 0.9263 | 2 | 0.9988 |

Value kinds of missed spans (false forwards):

| value_kind | false forwards |
|---|---|
| initials | 1 |
| zip | 1 |

### C / qs_v2, holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 724 | 80 | 56 | 1.0000 | 0.9185 | 0 | 0.9834 |
| hard_negative | no | 571 | 62 | 42 | 1.0000 | 0.9212 | 0 | 0.9825 |
| hard_negative | yes | 153 | 18 | 14 | 1.0000 * | 0.9085 | 0 | 0.9869 |
| lang | en | 724 | 80 | 56 | 1.0000 | 0.9185 | 0 | 0.9834 |
| length_bucket | medium | 596 | 47 | 34 | 1.0000 | 0.9413 | 0 | 0.9866 |
| length_bucket | short | 128 | 33 | 22 | 1.0000 * | 0.8125 | 0 | 0.9688 |
| perturbation | headers_footers | 307 | 35 | 25 | 1.0000 * | 0.9088 | 0 | 0.9707 |
| perturbation | line_wrap | 185 | 26 | 19 | 1.0000 * | 0.8973 | 0 | 0.9892 |
| perturbation | none | 290 | 28 | 19 | 1.0000 * | 0.9345 | 0 | 0.9897 |
| perturbation | ocr_noise | 48 | 7 | 6 | 1.0000 * | 0.8750 | 0 | 1.0000 |
| pii_depth | none | 724 | 80 | 56 | 1.0000 | 0.9185 | 0 | 0.9834 |
| pre_redacted | no | 675 | 75 | 51 | 1.0000 | 0.9200 | 0 | 0.9822 |
| pre_redacted | yes | 49 | 5 | 5 | 1.0000 * | 0.8980 | 0 | 1.0000 |
| split_span | no | 724 | 80 | 56 | 1.0000 | 0.9185 | 0 | 0.9834 |
| truncated | no | 724 | 80 | 56 | 1.0000 | 0.9185 | 0 | 0.9834 |

Value kinds of missed spans (false forwards):

none

### LC / qs_v1, test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log | 263 | 27 | 42 | 1.0000 | 0.4677 | 0 | 0.9049 |
| doc_type | crf_page | 371 | 42 | 101 | 1.0000 | 0.2857 | 0 | 0.9137 |
| doc_type | csr_patient_narrative | 964 | 42 | 72 | 0.9861 | 0.6058 | 1 | 0.9606 |
| doc_type | delegation_log | 151 | 14 | 14 | 1.0000 * | 0.5563 | 0 | 1.0000 |
| doc_type | deviation_log | 203 | 23 | 23 | 1.0000 * | 0.5172 | 0 | 0.9458 |
| doc_type | icf_signature_page | 52 | 19 | 17 | 1.0000 * | 0.2885 | 0 | 0.8846 |
| doc_type | lab_report | 188 | 29 | 34 | 1.0000 | 0.4309 | 0 | 0.8936 |
| doc_type | monitoring_visit_report | 986 | 29 | 47 | 1.0000 | 0.6349 | 0 | 0.9665 |
| doc_type | protocol_section | 1240 | 41 | 0 | n/a | 0.7129 | 0 | 0.9984 |
| doc_type | sae_cioms | 300 | 36 | 38 | 1.0000 | 0.5933 | 0 | 0.9733 |
| doc_type | site_correspondence | 995 | 35 | 31 | 0.9677 | 0.6905 | 1 | 0.9849 |
| hard_negative | no | 4393 | 260 | 302 | 0.9934 | 0.6144 | 2 | 0.9702 |
| hard_negative | yes | 1320 | 77 | 117 | 1.0000 | 0.5864 | 0 | 0.9553 |
| lang | de | 33 | 22 | 26 | 1.0000 * | 0.0000 * | 0 | 0.7879 |
| lang | en | 5655 | 298 | 373 | 0.9946 | 0.6141 | 2 | 0.9685 |
| lang | es | 7 | 6 | 6 | 1.0000 * | 0.0000 * | 0 | 0.8571 |
| lang | pl | 18 | 11 | 14 | 1.0000 * | 0.0000 * | 0 | 0.7778 |
| length_bucket | long | 2513 | 80 | 70 | 0.9714 | 0.6673 | 2 | 0.9825 |
| length_bucket | medium | 1466 | 119 | 218 | 1.0000 | 0.4993 | 0 | 0.9393 |
| length_bucket | short | 287 | 108 | 99 | 1.0000 | 0.2160 | 0 | 0.8780 |
| length_bucket | xl | 1447 | 30 | 32 | 1.0000 | 0.6925 | 0 | 0.9848 |
| perturbation | email_quoting | 995 | 35 | 31 | 0.9677 | 0.6905 | 1 | 0.9849 |
| perturbation | headers_footers | 2405 | 132 | 156 | 0.9872 | 0.6067 | 2 | 0.9672 |
| perturbation | line_wrap | 1852 | 105 | 151 | 1.0000 | 0.4827 | 0 | 0.9644 |
| perturbation | none | 1421 | 93 | 104 | 1.0000 | 0.7037 | 0 | 0.9662 |
| perturbation | ocr_noise | 567 | 39 | 45 | 1.0000 | 0.3880 | 0 | 0.9471 |
| perturbation | table | 659 | 75 | 115 | 1.0000 | 0.4203 | 0 | 0.9211 |
| pii_depth | early | 282 | 8 | 11 | 1.0000 * | 0.6809 | 0 | 0.9858 |
| pii_depth | late | 582 | 16 | 21 | 0.9524 * | 0.6134 | 1 | 0.9794 |
| pii_depth | middle | 327 | 10 | 11 | 1.0000 * | 0.5994 | 0 | 0.9786 |
| pii_depth | none | 4522 | 303 | 376 | 0.9973 | 0.6033 | 1 | 0.9631 |
| pre_redacted | no | 5297 | 303 | 355 | 0.9972 | 0.6126 | 1 | 0.9673 |
| pre_redacted | yes | 416 | 34 | 64 | 0.9844 | 0.5481 | 1 | 0.9591 |
| split_span | no | 5695 | 337 | 402 | 0.9950 | 0.6098 | 2 | 0.9668 |
| split_span | yes | 18 | 17 | 17 | 1.0000 * | 0.0000 * | 0 | 0.9444 |
| truncated | no | 5713 | 337 | 419 | 0.9952 | 0.6079 | 2 | 0.9667 |

Value kinds of missed spans (false forwards):

| value_kind | false forwards |
|---|---|
| person_name | 2 |

### LC / qs_v1, holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 724 | 80 | 56 | 1.0000 | 0.6423 | 0 | 0.9710 |
| hard_negative | no | 571 | 62 | 42 | 1.0000 | 0.6392 | 0 | 0.9702 |
| hard_negative | yes | 153 | 18 | 14 | 1.0000 * | 0.6536 | 0 | 0.9739 |
| lang | en | 724 | 80 | 56 | 1.0000 | 0.6423 | 0 | 0.9710 |
| length_bucket | medium | 596 | 47 | 34 | 1.0000 | 0.7097 | 0 | 0.9815 |
| length_bucket | short | 128 | 33 | 22 | 1.0000 * | 0.3281 | 0 | 0.9219 |
| perturbation | headers_footers | 307 | 35 | 25 | 1.0000 * | 0.5831 | 0 | 0.9674 |
| perturbation | line_wrap | 185 | 26 | 19 | 1.0000 * | 0.5027 | 0 | 0.9676 |
| perturbation | none | 290 | 28 | 19 | 1.0000 * | 0.7310 | 0 | 0.9759 |
| perturbation | ocr_noise | 48 | 7 | 6 | 1.0000 * | 0.5833 | 0 | 0.9792 |
| pii_depth | none | 724 | 80 | 56 | 1.0000 | 0.6423 | 0 | 0.9710 |
| pre_redacted | no | 675 | 75 | 51 | 1.0000 | 0.6430 | 0 | 0.9689 |
| pre_redacted | yes | 49 | 5 | 5 | 1.0000 * | 0.6327 | 0 | 1.0000 |
| split_span | no | 724 | 80 | 56 | 1.0000 | 0.6423 | 0 | 0.9710 |
| truncated | no | 724 | 80 | 56 | 1.0000 | 0.6423 | 0 | 0.9710 |

Value kinds of missed spans (false forwards):

none

### LW / qs_v1, test

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | conmed_log | 263 | 27 | 42 | 1.0000 | 0.4106 | 0 | 0.9011 |
| doc_type | crf_page | 371 | 42 | 101 | 1.0000 | 0.2264 | 0 | 0.9084 |
| doc_type | csr_patient_narrative | 964 | 42 | 72 | 1.0000 | 0.5104 | 0 | 0.9575 |
| doc_type | delegation_log | 151 | 14 | 14 | 1.0000 * | 0.4503 | 0 | 1.0000 |
| doc_type | deviation_log | 203 | 23 | 23 | 1.0000 * | 0.4729 | 0 | 0.9409 |
| doc_type | icf_signature_page | 52 | 19 | 17 | 1.0000 * | 0.2500 | 0 | 0.8846 |
| doc_type | lab_report | 188 | 29 | 34 | 1.0000 | 0.3617 | 0 | 0.9043 |
| doc_type | monitoring_visit_report | 986 | 29 | 47 | 1.0000 | 0.5385 | 0 | 0.9675 |
| doc_type | protocol_section | 1240 | 41 | 0 | n/a | 0.6137 | 0 | 0.9992 |
| doc_type | sae_cioms | 300 | 36 | 38 | 1.0000 | 0.4967 | 0 | 0.9733 |
| doc_type | site_correspondence | 995 | 35 | 31 | 0.9677 | 0.5568 | 1 | 0.9869 |
| hard_negative | no | 4393 | 260 | 302 | 0.9967 | 0.5204 | 1 | 0.9706 |
| hard_negative | yes | 1320 | 77 | 117 | 1.0000 | 0.4833 | 0 | 0.9530 |
| lang | de | 33 | 22 | 26 | 1.0000 * | 0.0000 * | 0 | 0.7879 |
| lang | en | 5655 | 298 | 373 | 0.9973 | 0.5171 | 1 | 0.9683 |
| lang | es | 7 | 6 | 6 | 1.0000 * | 0.0000 * | 0 | 0.8571 |
| lang | pl | 18 | 11 | 14 | 1.0000 * | 0.0000 * | 0 | 0.7778 |
| length_bucket | long | 2513 | 80 | 70 | 0.9857 | 0.5599 | 1 | 0.9829 |
| length_bucket | medium | 1466 | 119 | 218 | 1.0000 | 0.4229 | 0 | 0.9372 |
| length_bucket | short | 287 | 108 | 99 | 1.0000 | 0.1672 | 0 | 0.8815 |
| length_bucket | xl | 1447 | 30 | 32 | 1.0000 | 0.5867 | 0 | 0.9848 |
| perturbation | email_quoting | 995 | 35 | 31 | 0.9677 | 0.5568 | 1 | 0.9869 |
| perturbation | headers_footers | 2405 | 132 | 156 | 0.9936 | 0.5073 | 1 | 0.9672 |
| perturbation | line_wrap | 1852 | 105 | 151 | 1.0000 | 0.4293 | 0 | 0.9654 |
| perturbation | none | 1421 | 93 | 104 | 1.0000 | 0.5947 | 0 | 0.9648 |
| perturbation | ocr_noise | 567 | 39 | 45 | 1.0000 | 0.1711 | 0 | 0.9489 |
| perturbation | table | 659 | 75 | 115 | 1.0000 | 0.3566 | 0 | 0.9256 |
| pii_depth | early | 282 | 8 | 11 | 1.0000 * | 0.5709 | 0 | 0.9823 |
| pii_depth | late | 582 | 16 | 21 | 1.0000 * | 0.4983 | 0 | 0.9777 |
| pii_depth | middle | 327 | 10 | 11 | 1.0000 * | 0.4832 | 0 | 0.9755 |
| pii_depth | none | 4522 | 303 | 376 | 0.9973 | 0.5119 | 1 | 0.9635 |
| pre_redacted | no | 5297 | 303 | 355 | 1.0000 | 0.5175 | 0 | 0.9672 |
| pre_redacted | yes | 416 | 34 | 64 | 0.9844 | 0.4399 | 1 | 0.9591 |
| split_span | no | 5695 | 337 | 402 | 0.9975 | 0.5134 | 1 | 0.9666 |
| split_span | yes | 18 | 17 | 17 | 1.0000 * | 0.0000 * | 0 | 0.9444 |
| truncated | no | 5713 | 337 | 419 | 0.9976 | 0.5118 | 1 | 0.9666 |

Value kinds of missed spans (false forwards):

| value_kind | false forwards |
|---|---|
| person_name | 1 |

### LW / qs_v1, holdout

| dimension | value | units | docs | positives | recall | forward rate | false fwd | pii acc |
|---|---|---|---|---|---|---|---|---|
| doc_type | irb_letter | 724 | 80 | 56 | 1.0000 | 0.5594 | 0 | 0.9876 |
| hard_negative | no | 571 | 62 | 42 | 1.0000 | 0.5517 | 0 | 0.9912 |
| hard_negative | yes | 153 | 18 | 14 | 1.0000 * | 0.5882 | 0 | 0.9739 |
| lang | en | 724 | 80 | 56 | 1.0000 | 0.5594 | 0 | 0.9876 |
| length_bucket | medium | 596 | 47 | 34 | 1.0000 | 0.6174 | 0 | 0.9899 |
| length_bucket | short | 128 | 33 | 22 | 1.0000 * | 0.2891 | 0 | 0.9766 |
| perturbation | headers_footers | 307 | 35 | 25 | 1.0000 * | 0.4853 | 0 | 0.9870 |
| perturbation | line_wrap | 185 | 26 | 19 | 1.0000 * | 0.4703 | 0 | 0.9946 |
| perturbation | none | 290 | 28 | 19 | 1.0000 * | 0.6586 | 0 | 0.9828 |
| perturbation | ocr_noise | 48 | 7 | 6 | 1.0000 * | 0.2083 | 0 | 1.0000 |
| pii_depth | none | 724 | 80 | 56 | 1.0000 | 0.5594 | 0 | 0.9876 |
| pre_redacted | no | 675 | 75 | 51 | 1.0000 | 0.5585 | 0 | 0.9867 |
| pre_redacted | yes | 49 | 5 | 5 | 1.0000 * | 0.5714 | 0 | 1.0000 |
| split_span | no | 724 | 80 | 56 | 1.0000 | 0.5594 | 0 | 0.9876 |
| truncated | no | 724 | 80 | 56 | 1.0000 | 0.5594 | 0 | 0.9876 |

Value kinds of missed spans (false forwards):

none

## 8. Failure gallery

### A / qs_v1, test: 0 false forward(s)

### A / qs_v1, holdout: 0 false forward(s)

### A / qs_v2, test: 0 false forward(s)

### A / qs_v2, holdout: 0 false forward(s)

### B1 / qs_v1, test: 0 false forward(s)

### B1 / qs_v1, holdout: 0 false forward(s)

### B1 / qs_v2, test: 1 false forward(s)

**d0854:chunk:1024:1** route forward (p_below_t_low); p(pii) raw 0.0161, calibrated 0.0161; gold role both, category quasi; missed event_date, initials

>            minor     **N-H**
> 10   \#20030002       **17-Nov-2025**       fasting status not recorded            
>                       major     **B.H.**
> 
> Deviations are reviewed monthly by the investigator and reported to the
> sponsor within 5 working days.
> 
> Data Handling and Record Keeping
> Edit checks identify missing, inconsistent or out-of-range values at entry.
> Medical history and adverse events are coded with standard terminology before
> database lock. Data are entered into a validated electronic data capture
> system with an audit trail. Access to the database is restricted to authorised
> personnel according to the access matrix.
> 
> Medical history and adverse events are coded with a standard dictionary during
> the study. Reconciliation of laboratory data with the clinical database is
> performed before each data cut. Reconciliation of laboratory data with the
> clinical database is performed periodically. Edit checks flag missing,
> inconsistent or out-of-range values during cleaning.
> 
> Monitoring Procedures
> On-site and remote monitoring visits are scheduled based on enrollment and
> risk indicators. On-site and remote monitoring visits are scheduled according
> to the monitoring plan. The investigator site file is reviewed for
> completeness at each visit. Findings are documented in the visit report and
> followed up until closure.
> 
> Findings are documented in the visit report and followed up until resolution.
> Queries are raised in the data capture system and resolved by site staff
> within ten working days. The investigator site file is reviewed for currency
> of essential documents at each visit.
> 
> Queries are raised in the data capture system and answered by the site within
> five working days. The investigator site file is reviewed for completeness at
> each visit. The investigator site file is reviewed for currency of essential
> documents at each visit. The investigator site file is reviewed for
> completeness at each visit. Findings are documented in the visit report and
> followed up until closure. On-site and remote monitoring visits are scheduled
> based on enrollment and risk indicators.
> 
> Findings are documented in the visit report and followed up until closure.
> Queries are raised in the data capture system and resolved by site staff
> within ten working days. Queries are raised in the data capture system and
> resolved by site staff within five working days. Protocol deviations are
> assessed for impact on participant safety and data integrity. Source data
> verification focuses on eligibility, informed consent, primary endpoints and
> serious adverse events. On-site and remote monitoring visits are scheduled
> according to the monitoring plan.
> 
> Good Clinical Practice
> Participants may withdraw consent at any time without penalty. Confidentiality
> of participant information is protected at all times. The sponsor may conduct
> audits of study sites and vendors to verify compliance.
> 
> Confidentiality of participant information is protected at all times. The
> study will be conducted in accordance with the principles of good clinical
> practice and applicable regulatory requirements. The sponsor may conduct
> audits of study sites and vendors to verify compliance. The sponsor reserves
> the right to conduct audits of study sites and vendors to verify compliance.
> 
> Confidentiality of participant information is protected at all times. The
> sponsor may conduct audits of study sites and vendors to verify compliance.
> The protocol and any amendments are approved by the ethics committee before
> implementation. Participants may withdraw consent at any time without penalty.
> Essential documents are retained for at least 15 years after the end of the
> study or longer if required by local regulations.
> 
> Storage and Handling
> Unused product is returned to the sponsor after reconciliation. Tablet counts

### B1 / qs_v2, holdout: 0 false forward(s)

### B2 / qs_v1, test: 1 false forward(s)

**d1294:section:2048:0** route forward (p_below_t_low); p(pii) raw 0.0176, calibrated 0.0176; gold role patient, category quasi; missed event_date, initials

> Fenwick Therapeutics \| Protocol FTX-8191-011 \| Confidential
> 
> CRF Page 19: Vital Signs
> Protocol FTX-8191-011    Site 1017
> 
> Subject \| Initials \| Visit \| Visit date \| SBP \| DBP \| HR \| Temp
> 1017-0002 \| **MD** \| Visit 4 \| **06/19/2025** \| 128 \| 64 \| 97 \| 36.8
> 1017-0003 \| **PN** \| Visit 2 \| **14-Feb-2025** \| 109 \| 95 \| 84 \| 37.0
> Subj 1017-0003 \| **P-N** \| Visit 3 \| **March 1, 2025** \| 130 \| 62 \| 95 \| 36.6
> \#10170004 \| **MF** \| Visit 2 \| **April 18, 2025** \| 125 \| 94 \| 87 \| 37.4
> \#10170004 \| **M-F** \| Visit 5 \| **27JUN2025** \| 118 \| 80 \| 72 \| 36.5
> \#10170005 \| **F.J.** \| Visit 3 \| **18OCT2025** \| 119 \| 94 \| 68 \| 36.7
> \#10170005 \| **FJ** \| Visit 5 \| **11-Dec-2025** \| 165 \| 65 \| 67 \| 36.5
> 1017-0006 \| **AB** \| Visit 3 \| **12-Oct-2025** \| 146 \| 92 \| 68 \| 36.9
> \#10170007 \| **EP** \| Visit 2 \| **April 12, 2025** \| 136 \| 72 \| 60 \| 37.4
> Subj 1017-0007 \| **E-P** \| Visit 4 \| **2025-05-21** \| 147 \| 92 \| 62 \| 36.9
> Subj 1017-0007 \| **E-P** \| Visit 5 \| **19-Jun-2025** \| 142 \| 82 \| 70 \| 37.5
> Subj 1017-0008 \| **MP** \| Visit 2 \| **2025-09-09** \| 148 \| 87 \| 83 \| 36.9
> Subj 1017-0008 \| **M.P.** \| Visit 3 \| **09/21/2025** \| 121 \| 94 \| 94 \| 36.6
> 1017-0008 \| **M-P** \| Visit 4 \| **10/21/2025** \| 145 \| 88 \| 98 \| 36.6
> Subj 1017-0008 \| **M.P.** \| Visit 5 \| **11/16/2025** \| 162 \| 70 \| 76 \| 37.5
> \#10170009 \| **J-A** \| Visit 2 \| **01MAY2025** \| 119 \| 81 \| 90 \| 36.7
> 1017-0010 \| **CG** \| Visit 2 \| **2025-09-25** \| 112 \| 76 \| 64 \| 37.7
> 1017-0011 \| **P-B** \| Visit 2 \| **24JAN2025** \| 115 \| 70 \| 78 \| 37.3
> Subj 1017-0011 \| **PXB** \| Visit 3 \| **02/05/2025** \| 125 \| 68 \| 74 \| 37.0
> Subj 1017-0012 \| **T-C** \| Visit 3 \| **06SEP2025** \| 151 \| 89 \| 76 \| 37.2
> 1017-0012 \| **T.C.** \| Visit 5 \| **02-Nov-2025** \| 113 \| 93 \| 73 \| 36.3
> 1017-0013 \| **AÁ** \| Visit 2 \| **14FEB2025** \| 111 \| 78 \| 88 \| 36.3
> \#10170013 \| **A.Á.** \| Visit 3 \| **2025-02-28** \| 106 \| 96 \| 71 \| 36.2
> 1017-0013 \| **A.Á.** \| Visit 5 \| **28-Apr-2025** \| 126 \| 90 \| 78 \| 36.3
> Subj 1017-0014 \| **RF** \| Visit 2 \| **07/22/2025** \| 113 \| 66 \| 57 \| 37.2
> 1017-0015 \| **SXP** \| Visit 2 \| **08/26/2025** \| 162 \| 68 \| 80 \| 36.1
> 1017-0015 \| **SP** \| Visit 3 \| **09/10/2025** \| 125 \| 71 \| 92 \| 37.3
> Subj 1017-0015 \| **SXP** \| Visit 4 \| **09OCT2025** \| 144 \| 68 \| 59 \| 36.5
> 
> Measurements taken seated after 5 minutes of rest. Repeat any systolic value above 160 mmHg within 15 minutes.
> Entered by: site staff
> Source verified against medical record (source on file) for subject \#10170002.
> 
> Handling of Missing Data
> Categorical variables are presented as counts and percentages of the analysis set. Subgroup analyses by geographic region are exploratory and not adjusted for multiplicity. Categorical variables are presented as counts and percentages within each treatment group. Categorical variables are presented as counts and percentages of the analysis set.
> 
> Categorical variables are presented as counts and percentages within each treatment group. Missing data are not imputed unless stated otherwise under a missing-at-random assumption. All tests are two-sided with a significance level of 2.5 percent unless otherwise specified. Categorical variables are presented as counts and percentages within each treatment group.
> 
> Sensitivity analyses explore the robustness of the primary result to protocol deviations. All tests are two-sided with a significance level of 5 percent unless otherwise specified. Continuous variables are summarised with the number of observations, mean, standard deviation, median and range. Subgroup analyses by baseline severity are exploratory and not adjusted for multiplicity.
> 
> The statistical analysis plan is finalised before database lock and describes all derived variables. The statistical analysis plan is finalised before database lock and specifies all derived variables. Categorical variables are presented as counts and percentages within each treatment group. Subgroup analyses by age group are descriptive and not adjusted for multiplicity.
> 
> 

### B2 / qs_v1, holdout: 0 false forward(s)

### B2 / qs_v2, test: 1 false forward(s)

**d1294:section:2048:0** route forward (p_below_t_low); p(pii) raw 0.0176, calibrated 0.0176; gold role patient, category quasi; missed event_date, initials

> Fenwick Therapeutics \| Protocol FTX-8191-011 \| Confidential
> 
> CRF Page 19: Vital Signs
> Protocol FTX-8191-011    Site 1017
> 
> Subject \| Initials \| Visit \| Visit date \| SBP \| DBP \| HR \| Temp
> 1017-0002 \| **MD** \| Visit 4 \| **06/19/2025** \| 128 \| 64 \| 97 \| 36.8
> 1017-0003 \| **PN** \| Visit 2 \| **14-Feb-2025** \| 109 \| 95 \| 84 \| 37.0
> Subj 1017-0003 \| **P-N** \| Visit 3 \| **March 1, 2025** \| 130 \| 62 \| 95 \| 36.6
> \#10170004 \| **MF** \| Visit 2 \| **April 18, 2025** \| 125 \| 94 \| 87 \| 37.4
> \#10170004 \| **M-F** \| Visit 5 \| **27JUN2025** \| 118 \| 80 \| 72 \| 36.5
> \#10170005 \| **F.J.** \| Visit 3 \| **18OCT2025** \| 119 \| 94 \| 68 \| 36.7
> \#10170005 \| **FJ** \| Visit 5 \| **11-Dec-2025** \| 165 \| 65 \| 67 \| 36.5
> 1017-0006 \| **AB** \| Visit 3 \| **12-Oct-2025** \| 146 \| 92 \| 68 \| 36.9
> \#10170007 \| **EP** \| Visit 2 \| **April 12, 2025** \| 136 \| 72 \| 60 \| 37.4
> Subj 1017-0007 \| **E-P** \| Visit 4 \| **2025-05-21** \| 147 \| 92 \| 62 \| 36.9
> Subj 1017-0007 \| **E-P** \| Visit 5 \| **19-Jun-2025** \| 142 \| 82 \| 70 \| 37.5
> Subj 1017-0008 \| **MP** \| Visit 2 \| **2025-09-09** \| 148 \| 87 \| 83 \| 36.9
> Subj 1017-0008 \| **M.P.** \| Visit 3 \| **09/21/2025** \| 121 \| 94 \| 94 \| 36.6
> 1017-0008 \| **M-P** \| Visit 4 \| **10/21/2025** \| 145 \| 88 \| 98 \| 36.6
> Subj 1017-0008 \| **M.P.** \| Visit 5 \| **11/16/2025** \| 162 \| 70 \| 76 \| 37.5
> \#10170009 \| **J-A** \| Visit 2 \| **01MAY2025** \| 119 \| 81 \| 90 \| 36.7
> 1017-0010 \| **CG** \| Visit 2 \| **2025-09-25** \| 112 \| 76 \| 64 \| 37.7
> 1017-0011 \| **P-B** \| Visit 2 \| **24JAN2025** \| 115 \| 70 \| 78 \| 37.3
> Subj 1017-0011 \| **PXB** \| Visit 3 \| **02/05/2025** \| 125 \| 68 \| 74 \| 37.0
> Subj 1017-0012 \| **T-C** \| Visit 3 \| **06SEP2025** \| 151 \| 89 \| 76 \| 37.2
> 1017-0012 \| **T.C.** \| Visit 5 \| **02-Nov-2025** \| 113 \| 93 \| 73 \| 36.3
> 1017-0013 \| **AÁ** \| Visit 2 \| **14FEB2025** \| 111 \| 78 \| 88 \| 36.3
> \#10170013 \| **A.Á.** \| Visit 3 \| **2025-02-28** \| 106 \| 96 \| 71 \| 36.2
> 1017-0013 \| **A.Á.** \| Visit 5 \| **28-Apr-2025** \| 126 \| 90 \| 78 \| 36.3
> Subj 1017-0014 \| **RF** \| Visit 2 \| **07/22/2025** \| 113 \| 66 \| 57 \| 37.2
> 1017-0015 \| **SXP** \| Visit 2 \| **08/26/2025** \| 162 \| 68 \| 80 \| 36.1
> 1017-0015 \| **SP** \| Visit 3 \| **09/10/2025** \| 125 \| 71 \| 92 \| 37.3
> Subj 1017-0015 \| **SXP** \| Visit 4 \| **09OCT2025** \| 144 \| 68 \| 59 \| 36.5
> 
> Measurements taken seated after 5 minutes of rest. Repeat any systolic value above 160 mmHg within 15 minutes.
> Entered by: site staff
> Source verified against medical record (source on file) for subject \#10170002.
> 
> Handling of Missing Data
> Categorical variables are presented as counts and percentages of the analysis set. Subgroup analyses by geographic region are exploratory and not adjusted for multiplicity. Categorical variables are presented as counts and percentages within each treatment group. Categorical variables are presented as counts and percentages of the analysis set.
> 
> Categorical variables are presented as counts and percentages within each treatment group. Missing data are not imputed unless stated otherwise under a missing-at-random assumption. All tests are two-sided with a significance level of 2.5 percent unless otherwise specified. Categorical variables are presented as counts and percentages within each treatment group.
> 
> Sensitivity analyses explore the robustness of the primary result to protocol deviations. All tests are two-sided with a significance level of 5 percent unless otherwise specified. Continuous variables are summarised with the number of observations, mean, standard deviation, median and range. Subgroup analyses by baseline severity are exploratory and not adjusted for multiplicity.
> 
> The statistical analysis plan is finalised before database lock and describes all derived variables. The statistical analysis plan is finalised before database lock and specifies all derived variables. Categorical variables are presented as counts and percentages within each treatment group. Subgroup analyses by age group are descriptive and not adjusted for multiplicity.
> 
> 

### B2 / qs_v2, holdout: 0 false forward(s)

### B3 / qs_v1 (doc-level, underpowered), test: 0 false forward(s)

### B3 / qs_v1 (doc-level, underpowered), holdout: 0 false forward(s)

### B3 / qs_v2 (doc-level, underpowered), test: 0 false forward(s)

### B3 / qs_v2 (doc-level, underpowered), holdout: 0 false forward(s)

### B4 / qs_v1 (doc-level, underpowered), test: 0 false forward(s)

### B4 / qs_v1 (doc-level, underpowered), holdout: 0 false forward(s)

### B4 / qs_v2 (doc-level, underpowered), test: 0 false forward(s)

### B4 / qs_v2 (doc-level, underpowered), holdout: 0 false forward(s)

### C / qs_v1, test: 1 false forward(s)

**d0693:chunk:512:6** route forward (p_below_t_low); p(pii) raw 0.0030, calibrated 0.0020; gold role patient, category quasi; missed initials

>  \| 64 \| 79 \| 37.5
> ---- \| **JXM** \| Visit 5 \| ---- \| 128 \| 78 \| 98 \| 37.0
> 
> Measurements taken seated after 5 minutes of rest. Repeat any systolic value above 160 mmHg within 15 minutes.
> Entered by: site staff
> Source verified against medical record (source on file) for subject (see first row).
> 
> Data Management
> Access to the database is restricted to authorised personnel with role-based permissions. Reconciliation of safety data with the clinical database is performed periodically. Data are entered into a validated electronic data capture system with an audit trail. Data are entered into a validated clinical database with an audit trail. Access to the database is restricted to authorised personnel according to the access matrix. Medical history and adverse events are coded with standard terminology before database lock.
> 
> Edit checks flag missing, inconsistent or out-of-range values at entry. Medical history and adverse events are coded with a standard dictionary before database lock. Medical history and adverse events are coded with a standard dictionary before database lock.
> 
> Reconciliation of laboratory data with the clinical database is performed periodically. Data are entered into a validated clinical database with an audit trail. Medical history and adverse events are coded with a standard

### C / qs_v1, holdout: 0 false forward(s)

### C / qs_v2, test: 2 false forward(s)

**d0625:chunk:512:24** route forward (p_below_t_low); p(pii) raw 0.9566, calibrated 0.9647; gold role patient, category quasi; missed zip

>  **10504**.
> Medical history was notable for hypertension. Concomitant medications at baseline were reviewed by the investigator.
> 
> Adverse Event
> No adverse events were reported during the treatment period.
> 
> Page 6
> 
> Fenwick Therapeutics \| Protocol FTX-9990-002 \| Confidential
> 
> Data Handling and Record Keeping
> Edit checks flag missing, inconsistent or out-of-range values at entry. Data are entered into a validated clinical database with an audit trail. Reconciliation of laboratory data with the clinical database is performed periodically. Data are entered into a validated clinical database with an audit trail. Access to the database is restricted to authorised personnel with role-based permissions.
> 
> Data are entered into a validated electronic data capture system with an audit trail. Reconciliation of laboratory data with the clinical database is performed periodically. Data are entered into a validated electronic data capture system with an audit trail. Edit checks flag missing, inconsistent or out-of-range values at entry.
> 
> Edit checks identify missing, inconsistent or out-of-range values at entry. Access to the database is restricted to authorised personnel with role-based permissions. Medical history and adverse events are coded with standard terminology before database lock. Edit checks identify

**d0693:chunk:512:6** route forward (p_below_t_low); p(pii) raw 0.0030, calibrated 0.0020; gold role patient, category quasi; missed initials

>  \| 64 \| 79 \| 37.5
> ---- \| **JXM** \| Visit 5 \| ---- \| 128 \| 78 \| 98 \| 37.0
> 
> Measurements taken seated after 5 minutes of rest. Repeat any systolic value above 160 mmHg within 15 minutes.
> Entered by: site staff
> Source verified against medical record (source on file) for subject (see first row).
> 
> Data Management
> Access to the database is restricted to authorised personnel with role-based permissions. Reconciliation of safety data with the clinical database is performed periodically. Data are entered into a validated electronic data capture system with an audit trail. Data are entered into a validated clinical database with an audit trail. Access to the database is restricted to authorised personnel according to the access matrix. Medical history and adverse events are coded with standard terminology before database lock.
> 
> Edit checks flag missing, inconsistent or out-of-range values at entry. Medical history and adverse events are coded with a standard dictionary before database lock. Medical history and adverse events are coded with a standard dictionary before database lock.
> 
> Reconciliation of laboratory data with the clinical database is performed periodically. Data are entered into a validated clinical database with an audit trail. Medical history and adverse events are coded with a standard

### C / qs_v2, holdout: 0 false forward(s)

### LC / qs_v1, test: 2 false forward(s)

**d0734:chunk:512:1** route forward (p_below_t_low); p(pii) raw 0.0337, calibrated 0.0046; gold role staff, category staff; missed person_name

> 
> \> Thanks, **Michele**
> 
> Handling of Missing Data
> Missing data are handled by multiple imputation under a missing-at-random assumption. All tests are two-sided with a significance level of 5 percent unless otherwise specified. The statistical analysis plan is finalised before database lock and describes all derived variables. All tests are two-sided with a significance level of 5 percent unless otherwise specified. Sensitivity analyses assess the robustness of the primary result to alternative assumptions.
> 
> Continuous variables are summarised with the number of observations, mean, standard deviation, median and range. Missing data are handled by multiple imputation in the primary analysis. All tests are two-sided with a significance level of 5 percent unless otherwise specified. The statistical analysis plan is finalised before database lock and specifies all derived variables.
> 
> Investigational Product Management
> Investigational product is stored in a secure, temperature-monitored area with access limited to authorised staff. Tablet counts are reconciled against the dosing diary to assess compliance. Tablet counts are reconciled against the dosing diary to assess compliance.
> 
> Tablet counts are reconciled against the dosing diary to assess compliance. Unused product is destroyed according to local procedures after reconciliation. Dispensing and returns are

**d0784:chunk:512:24** route forward (p_below_t_low); p(pii) raw 0.0430, calibrated 0.0069; gold role staff, category staff; missed person_name

>  was reviewed by **Dr. Morse**.
> 
> Follow-up information is provided until the event resolves or the participant is lost to follow-up. The investigator assesses intensity using the common terminology criteria and documents the assessment in the source record. The responsible physician assesses intensity using the common terminology criteria and documents the assessment in the source record. All serious adverse events must be reported to the sponsor within 24 hours of the site becoming aware of the event.
> 
> The sponsor reviews each report for expectedness against the reference safety information. Events that start after the first dose and until 28 days after the last dose are summarised as treatment-emergent. The investigator assesses severity using the common terminology criteria and documents the assessment in the source record. The responsible physician assesses intensity using the common terminology criteria and documents the assessment in the source record. The sponsor reviews each report for expectedness against the reference safety information.
> 
> Ethical and Regulatory Considerations
> The sponsor reserves the right to conduct audits of study sites and vendors to verify compliance. The sponsor may conduct audits of study sites and vendors to verify compliance. The informed consent form and any amendments must be approved by the ethics committee before implementation. Confidentiality of participant information is protected in line with applicable

### LC / qs_v1, holdout: 0 false forward(s)

### LW / qs_v1, test: 1 false forward(s)

**d0734:chunk:512:1** route forward (p_below_t_low); p(pii) raw 0.0301, calibrated 0.0041; gold role staff, category staff; missed person_name

> 
> \> Thanks, **Michele**
> 
> Handling of Missing Data
> Missing data are handled by multiple imputation under a missing-at-random assumption. All tests are two-sided with a significance level of 5 percent unless otherwise specified. The statistical analysis plan is finalised before database lock and describes all derived variables. All tests are two-sided with a significance level of 5 percent unless otherwise specified. Sensitivity analyses assess the robustness of the primary result to alternative assumptions.
> 
> Continuous variables are summarised with the number of observations, mean, standard deviation, median and range. Missing data are handled by multiple imputation in the primary analysis. All tests are two-sided with a significance level of 5 percent unless otherwise specified. The statistical analysis plan is finalised before database lock and specifies all derived variables.
> 
> Investigational Product Management
> Investigational product is stored in a secure, temperature-monitored area with access limited to authorised staff. Tablet counts are reconciled against the dosing diary to assess compliance. Tablet counts are reconciled against the dosing diary to assess compliance.
> 
> Tablet counts are reconciled against the dosing diary to assess compliance. Unused product is destroyed according to local procedures after reconciliation. Dispensing and returns are

### LW / qs_v1, holdout: 0 false forward(s)

## 9. Caveats

- A / qs_v1: Accuracy run on Tesla T4 (Kaggle, D-022), not the Apple M2. Accuracy does not depend on the hardware (D-002); this run's latency is not the M2 headline (see the timing-only run where present).
- A / qs_v1: test: slice recall from fewer than 30 positives: doc_type=delegation_log (14), doc_type=deviation_log (23), doc_type=icf_signature_page (17), lang=de (26), lang=es (6), lang=pl (14), pii_depth=early (11), pii_depth=late (21), pii_depth=middle (11), split_span=yes (17)
- A / qs_v1: test: slice forward rate from fewer than 30 negatives: lang=de (7), lang=es (1), lang=pl (4), split_span=yes (1)
- A / qs_v1: holdout: slice recall from fewer than 30 positives: hard_negative=yes (14), length_bucket=short (22), perturbation=headers_footers (25), perturbation=line_wrap (19), perturbation=none (19), perturbation=ocr_noise (6), pre_redacted=yes (5)
- A / qs_v2: Accuracy run on Tesla T4 (Kaggle, D-022), not the Apple M2. Accuracy does not depend on the hardware (D-002); this run's latency is not the M2 headline (see the timing-only run where present).
- A / qs_v2: test: slice recall from fewer than 30 positives: doc_type=delegation_log (14), doc_type=deviation_log (23), doc_type=icf_signature_page (17), lang=de (26), lang=es (6), lang=pl (14), pii_depth=early (11), pii_depth=late (21), pii_depth=middle (11), split_span=yes (17)
- A / qs_v2: test: slice forward rate from fewer than 30 negatives: lang=de (7), lang=es (1), lang=pl (4), split_span=yes (1)
- A / qs_v2: holdout: slice recall from fewer than 30 positives: hard_negative=yes (14), length_bucket=short (22), perturbation=headers_footers (25), perturbation=line_wrap (19), perturbation=none (19), perturbation=ocr_noise (6), pre_redacted=yes (5)
- B1 / qs_v1: Accuracy run on Tesla T4 (Kaggle, D-022), not the Apple M2. Accuracy does not depend on the hardware (D-002); this run's latency is not the M2 headline (see the timing-only run where present).
- B1 / qs_v1: test: slice recall from fewer than 30 positives: doc_type=conmed_log (21), doc_type=delegation_log (14), doc_type=deviation_log (18), doc_type=icf_signature_page (14), doc_type=lab_report (23), doc_type=site_correspondence (23), lang=de (19), lang=es (5), lang=pl (9), length_bucket=xl (29), perturbation=email_quoting (23), pii_depth=early (8), pii_depth=late (18), pii_depth=middle (11), split_span=yes (16)
- B1 / qs_v1: test: slice forward rate from fewer than 30 negatives: doc_type=icf_signature_page (9), lang=de (3), lang=es (1), lang=pl (2), split_span=yes (1)
- B1 / qs_v1: holdout: slice recall from fewer than 30 positives: hard_negative=yes (14), length_bucket=short (22), perturbation=headers_footers (25), perturbation=line_wrap (19), perturbation=none (19), perturbation=ocr_noise (6), pre_redacted=yes (5)
- B1 / qs_v1: holdout: slice forward rate from fewer than 30 negatives: perturbation=ocr_noise (9), pre_redacted=yes (12)
- B1 / qs_v2: Accuracy run on Tesla T4 (Kaggle, D-022), not the Apple M2. Accuracy does not depend on the hardware (D-002); this run's latency is not the M2 headline (see the timing-only run where present).
- B1 / qs_v2: test: slice recall from fewer than 30 positives: doc_type=conmed_log (21), doc_type=delegation_log (14), doc_type=deviation_log (18), doc_type=icf_signature_page (14), doc_type=lab_report (23), doc_type=site_correspondence (23), lang=de (19), lang=es (5), lang=pl (9), length_bucket=xl (29), perturbation=email_quoting (23), pii_depth=early (8), pii_depth=late (18), pii_depth=middle (11), split_span=yes (16)
- B1 / qs_v2: test: slice forward rate from fewer than 30 negatives: doc_type=icf_signature_page (9), lang=de (3), lang=es (1), lang=pl (2), split_span=yes (1)
- B1 / qs_v2: holdout: slice recall from fewer than 30 positives: hard_negative=yes (14), length_bucket=short (22), perturbation=headers_footers (25), perturbation=line_wrap (19), perturbation=none (19), perturbation=ocr_noise (6), pre_redacted=yes (5)
- B1 / qs_v2: holdout: slice forward rate from fewer than 30 negatives: perturbation=ocr_noise (9), pre_redacted=yes (12)
- B2 / qs_v1: Accuracy run on Tesla T4 (Kaggle, D-022), not the Apple M2. Accuracy does not depend on the hardware (D-002); this run's latency is not the M2 headline (see the timing-only run where present).
- B2 / qs_v1: test: slice recall from fewer than 30 positives: doc_type=conmed_log (12), doc_type=crf_page (23), doc_type=delegation_log (14), doc_type=deviation_log (13), doc_type=icf_signature_page (14), doc_type=lab_report (21), doc_type=site_correspondence (22), lang=de (19), lang=es (5), lang=pl (9), length_bucket=xl (23), perturbation=email_quoting (22), perturbation=ocr_noise (27), pii_depth=early (8), pii_depth=late (16), pii_depth=middle (10), pre_redacted=yes (28), truncated=yes (8)
- B2 / qs_v1: test: slice forward rate from fewer than 30 negatives: doc_type=delegation_log (12), doc_type=deviation_log (28), doc_type=icf_signature_page (5), doc_type=lab_report (21), doc_type=sae_cioms (28), lang=de (3), lang=es (1), lang=pl (2), truncated=yes (6)
- B2 / qs_v1: holdout: slice recall from fewer than 30 positives: hard_negative=yes (14), length_bucket=short (22), perturbation=headers_footers (25), perturbation=line_wrap (19), perturbation=none (19), perturbation=ocr_noise (6), pre_redacted=yes (5)
- B2 / qs_v1: holdout: slice forward rate from fewer than 30 negatives: hard_negative=yes (15), length_bucket=short (11), perturbation=line_wrap (17), perturbation=ocr_noise (3), pre_redacted=yes (4)
- B2 / qs_v2: Accuracy run on Tesla T4 (Kaggle, D-022), not the Apple M2. Accuracy does not depend on the hardware (D-002); this run's latency is not the M2 headline (see the timing-only run where present).
- B2 / qs_v2: test: slice recall from fewer than 30 positives: doc_type=conmed_log (12), doc_type=crf_page (23), doc_type=delegation_log (14), doc_type=deviation_log (13), doc_type=icf_signature_page (14), doc_type=lab_report (21), doc_type=site_correspondence (22), lang=de (19), lang=es (5), lang=pl (9), length_bucket=xl (23), perturbation=email_quoting (22), perturbation=ocr_noise (27), pii_depth=early (8), pii_depth=late (16), pii_depth=middle (10), pre_redacted=yes (28), truncated=yes (8)
- B2 / qs_v2: test: slice forward rate from fewer than 30 negatives: doc_type=delegation_log (12), doc_type=deviation_log (28), doc_type=icf_signature_page (5), doc_type=lab_report (21), doc_type=sae_cioms (28), lang=de (3), lang=es (1), lang=pl (2), truncated=yes (6)
- B2 / qs_v2: holdout: slice recall from fewer than 30 positives: hard_negative=yes (14), length_bucket=short (22), perturbation=headers_footers (25), perturbation=line_wrap (19), perturbation=none (19), perturbation=ocr_noise (6), pre_redacted=yes (5)
- B2 / qs_v2: holdout: slice forward rate from fewer than 30 negatives: hard_negative=yes (15), length_bucket=short (11), perturbation=line_wrap (17), perturbation=ocr_noise (3), pre_redacted=yes (4)
- B3 / qs_v1 (doc-level, underpowered): Accuracy run on Tesla T4 (Kaggle, D-022), not the Apple M2. Accuracy does not depend on the hardware (D-002); this run's latency is not the M2 headline (see the timing-only run where present).
- B3 / qs_v1 (doc-level, underpowered): Doc-level arm: underpowered (D-008 amended); 337 test documents, few units each, so recall intervals are wide.
- B3 / qs_v1 (doc-level, underpowered): test: slice recall from fewer than 30 positives: doc_type=conmed_log (12), doc_type=crf_page (23), doc_type=delegation_log (14), doc_type=deviation_log (13), doc_type=icf_signature_page (14), doc_type=lab_report (21), doc_type=site_correspondence (22), lang=de (19), lang=es (5), lang=pl (9), length_bucket=xl (22), perturbation=email_quoting (22), perturbation=ocr_noise (26), pii_depth=early (8), pii_depth=late (16), pii_depth=middle (10), pre_redacted=yes (28)
- B3 / qs_v1 (doc-level, underpowered): test: slice forward rate from fewer than 30 negatives: doc_type=conmed_log (20), doc_type=crf_page (25), doc_type=delegation_log (1), doc_type=deviation_log (13), doc_type=icf_signature_page (5), doc_type=lab_report (9), doc_type=sae_cioms (6), lang=de (3), lang=es (1), lang=pl (2), pii_depth=early (13), pii_depth=late (24), pii_depth=middle (14), pre_redacted=yes (17)
- B3 / qs_v1 (doc-level, underpowered): holdout: slice recall from fewer than 30 positives: hard_negative=yes (14), length_bucket=short (22), perturbation=headers_footers (25), perturbation=line_wrap (19), perturbation=none (19), perturbation=ocr_noise (6), pre_redacted=yes (5)
- B3 / qs_v1 (doc-level, underpowered): holdout: slice forward rate from fewer than 30 negatives: doc_type=irb_letter (28), hard_negative=no (24), hard_negative=yes (4), lang=en (28), length_bucket=medium (17), length_bucket=short (11), perturbation=headers_footers (11), perturbation=line_wrap (8), perturbation=none (11), perturbation=ocr_noise (1), pii_depth=none (28), pre_redacted=no (27), pre_redacted=yes (1), split_span=no (28), truncated=no (28)
- B3 / qs_v2 (doc-level, underpowered): Accuracy run on Tesla T4 (Kaggle, D-022), not the Apple M2. Accuracy does not depend on the hardware (D-002); this run's latency is not the M2 headline (see the timing-only run where present).
- B3 / qs_v2 (doc-level, underpowered): Doc-level arm: underpowered (D-008 amended); 337 test documents, few units each, so recall intervals are wide.
- B3 / qs_v2 (doc-level, underpowered): test: slice recall from fewer than 30 positives: doc_type=conmed_log (12), doc_type=crf_page (23), doc_type=delegation_log (14), doc_type=deviation_log (13), doc_type=icf_signature_page (14), doc_type=lab_report (21), doc_type=site_correspondence (22), lang=de (19), lang=es (5), lang=pl (9), length_bucket=xl (22), perturbation=email_quoting (22), perturbation=ocr_noise (26), pii_depth=early (8), pii_depth=late (16), pii_depth=middle (10), pre_redacted=yes (28)
- B3 / qs_v2 (doc-level, underpowered): test: slice forward rate from fewer than 30 negatives: doc_type=conmed_log (20), doc_type=crf_page (25), doc_type=delegation_log (1), doc_type=deviation_log (13), doc_type=icf_signature_page (5), doc_type=lab_report (9), doc_type=sae_cioms (6), lang=de (3), lang=es (1), lang=pl (2), pii_depth=early (13), pii_depth=late (24), pii_depth=middle (14), pre_redacted=yes (17)
- B3 / qs_v2 (doc-level, underpowered): holdout: slice recall from fewer than 30 positives: hard_negative=yes (14), length_bucket=short (22), perturbation=headers_footers (25), perturbation=line_wrap (19), perturbation=none (19), perturbation=ocr_noise (6), pre_redacted=yes (5)
- B3 / qs_v2 (doc-level, underpowered): holdout: slice forward rate from fewer than 30 negatives: doc_type=irb_letter (28), hard_negative=no (24), hard_negative=yes (4), lang=en (28), length_bucket=medium (17), length_bucket=short (11), perturbation=headers_footers (11), perturbation=line_wrap (8), perturbation=none (11), perturbation=ocr_noise (1), pii_depth=none (28), pre_redacted=no (27), pre_redacted=yes (1), split_span=no (28), truncated=no (28)
- B4 / qs_v1 (doc-level, underpowered): Accuracy run on Tesla T4 (Kaggle, D-022), not the Apple M2. Accuracy does not depend on the hardware (D-002); this run's latency is not the M2 headline (see the timing-only run where present).
- B4 / qs_v1 (doc-level, underpowered): Doc-level arm: underpowered (D-008 amended); 337 test documents, few units each, so recall intervals are wide.
- B4 / qs_v1 (doc-level, underpowered): test: slice recall from fewer than 30 positives: doc_type=conmed_log (12), doc_type=crf_page (23), doc_type=delegation_log (14), doc_type=deviation_log (13), doc_type=icf_signature_page (14), doc_type=lab_report (21), doc_type=monitoring_visit_report (25), doc_type=site_correspondence (22), lang=de (19), lang=es (5), lang=pl (9), length_bucket=xl (18), perturbation=email_quoting (22), perturbation=ocr_noise (25), pii_depth=early (8), pii_depth=late (16), pii_depth=middle (10), pre_redacted=yes (26), truncated=yes (18)
- B4 / qs_v1 (doc-level, underpowered): test: slice forward rate from fewer than 30 negatives: doc_type=conmed_log (15), doc_type=crf_page (19), doc_type=csr_patient_narrative (3), doc_type=delegation_log (0), doc_type=deviation_log (10), doc_type=icf_signature_page (5), doc_type=lab_report (8), doc_type=monitoring_visit_report (4), doc_type=sae_cioms (4), doc_type=site_correspondence (13), hard_negative=yes (25), lang=de (3), lang=es (1), lang=pl (2), length_bucket=xl (12), perturbation=email_quoting (13), perturbation=ocr_noise (14), perturbation=table (28), pii_depth=early (0), pii_depth=late (0), pii_depth=middle (0), pre_redacted=yes (8), truncated=yes (12)
- B4 / qs_v1 (doc-level, underpowered): holdout: slice recall from fewer than 30 positives: hard_negative=yes (14), length_bucket=short (22), perturbation=headers_footers (25), perturbation=line_wrap (19), perturbation=none (19), perturbation=ocr_noise (6), pre_redacted=yes (5)
- B4 / qs_v1 (doc-level, underpowered): holdout: slice forward rate from fewer than 30 negatives: doc_type=irb_letter (24), hard_negative=no (20), hard_negative=yes (4), lang=en (24), length_bucket=medium (13), length_bucket=short (11), perturbation=headers_footers (10), perturbation=line_wrap (7), perturbation=none (9), perturbation=ocr_noise (1), pii_depth=none (24), pre_redacted=no (24), pre_redacted=yes (0), split_span=no (24), truncated=no (24)
- B4 / qs_v2 (doc-level, underpowered): Accuracy run on Tesla T4 (Kaggle, D-022), not the Apple M2. Accuracy does not depend on the hardware (D-002); this run's latency is not the M2 headline (see the timing-only run where present).
- B4 / qs_v2 (doc-level, underpowered): Doc-level arm: underpowered (D-008 amended); 337 test documents, few units each, so recall intervals are wide.
- B4 / qs_v2 (doc-level, underpowered): test: slice recall from fewer than 30 positives: doc_type=conmed_log (12), doc_type=crf_page (23), doc_type=delegation_log (14), doc_type=deviation_log (13), doc_type=icf_signature_page (14), doc_type=lab_report (21), doc_type=monitoring_visit_report (25), doc_type=site_correspondence (22), lang=de (19), lang=es (5), lang=pl (9), length_bucket=xl (18), perturbation=email_quoting (22), perturbation=ocr_noise (25), pii_depth=early (8), pii_depth=late (16), pii_depth=middle (10), pre_redacted=yes (26), truncated=yes (18)
- B4 / qs_v2 (doc-level, underpowered): test: slice forward rate from fewer than 30 negatives: doc_type=conmed_log (15), doc_type=crf_page (19), doc_type=csr_patient_narrative (3), doc_type=delegation_log (0), doc_type=deviation_log (10), doc_type=icf_signature_page (5), doc_type=lab_report (8), doc_type=monitoring_visit_report (4), doc_type=sae_cioms (4), doc_type=site_correspondence (13), hard_negative=yes (25), lang=de (3), lang=es (1), lang=pl (2), length_bucket=xl (12), perturbation=email_quoting (13), perturbation=ocr_noise (14), perturbation=table (28), pii_depth=early (0), pii_depth=late (0), pii_depth=middle (0), pre_redacted=yes (8), truncated=yes (12)
- B4 / qs_v2 (doc-level, underpowered): holdout: slice recall from fewer than 30 positives: hard_negative=yes (14), length_bucket=short (22), perturbation=headers_footers (25), perturbation=line_wrap (19), perturbation=none (19), perturbation=ocr_noise (6), pre_redacted=yes (5)
- B4 / qs_v2 (doc-level, underpowered): holdout: slice forward rate from fewer than 30 negatives: doc_type=irb_letter (24), hard_negative=no (20), hard_negative=yes (4), lang=en (24), length_bucket=medium (13), length_bucket=short (11), perturbation=headers_footers (10), perturbation=line_wrap (7), perturbation=none (9), perturbation=ocr_noise (1), pii_depth=none (24), pre_redacted=no (24), pre_redacted=yes (0), split_span=no (24), truncated=no (24)
- C / qs_v1: Accuracy run on Tesla T4 (Kaggle, D-022), not the Apple M2. Accuracy does not depend on the hardware (D-002); this run's latency is not the M2 headline (see the timing-only run where present).
- C / qs_v1: test: slice recall from fewer than 30 positives: doc_type=delegation_log (14), doc_type=deviation_log (23), doc_type=icf_signature_page (17), lang=de (26), lang=es (6), lang=pl (14), pii_depth=early (11), pii_depth=late (21), pii_depth=middle (11), split_span=yes (17)
- C / qs_v1: test: slice forward rate from fewer than 30 negatives: lang=de (7), lang=es (1), lang=pl (4), split_span=yes (1)
- C / qs_v1: holdout: slice recall from fewer than 30 positives: hard_negative=yes (14), length_bucket=short (22), perturbation=headers_footers (25), perturbation=line_wrap (19), perturbation=none (19), perturbation=ocr_noise (6), pre_redacted=yes (5)
- C / qs_v1: Fine-tuned on 4067 train-split units from 859 documents: every PII unit plus 3 clean units per PII unit, so training prevalence is 25.0%; test prevalence is 7.3%. 792 of 859 training documents are English; no training documents of type irb_letter. Same generator as the test set (templates, filler, Faker world; disjoint sites and persons): in-distribution evidence only.
- C / qs_v2: Accuracy run on Tesla T4 (Kaggle, D-022), not the Apple M2. Accuracy does not depend on the hardware (D-002); this run's latency is not the M2 headline (see the timing-only run where present).
- C / qs_v2: test: slice recall from fewer than 30 positives: doc_type=delegation_log (14), doc_type=deviation_log (23), doc_type=icf_signature_page (17), lang=de (26), lang=es (6), lang=pl (14), pii_depth=early (11), pii_depth=late (21), pii_depth=middle (11), split_span=yes (17)
- C / qs_v2: test: slice forward rate from fewer than 30 negatives: lang=de (7), lang=es (1), lang=pl (4), split_span=yes (1)
- C / qs_v2: holdout: slice recall from fewer than 30 positives: hard_negative=yes (14), length_bucket=short (22), perturbation=headers_footers (25), perturbation=line_wrap (19), perturbation=none (19), perturbation=ocr_noise (6), pre_redacted=yes (5)
- C / qs_v2: Fine-tuned on 4067 train-split units from 859 documents: every PII unit plus 3 clean units per PII unit, so training prevalence is 25.0%; test prevalence is 7.3%. 792 of 859 training documents are English; no training documents of type irb_letter. Same generator as the test set (templates, filler, Faker world; disjoint sites and persons): in-distribution evidence only.
- LC / qs_v1: Lexical baseline, not a Laya arm: TF-IDF + logistic regression trained on arm C's own training units (pii_present only; no role rule, no other questions). Latency is CPU batch scoring, amortized per unit, and not comparable to the model arms.
- LC / qs_v1: test: slice recall from fewer than 30 positives: doc_type=delegation_log (14), doc_type=deviation_log (23), doc_type=icf_signature_page (17), lang=de (26), lang=es (6), lang=pl (14), pii_depth=early (11), pii_depth=late (21), pii_depth=middle (11), split_span=yes (17)
- LC / qs_v1: test: slice forward rate from fewer than 30 negatives: lang=de (7), lang=es (1), lang=pl (4), split_span=yes (1)
- LC / qs_v1: holdout: slice recall from fewer than 30 positives: hard_negative=yes (14), length_bucket=short (22), perturbation=headers_footers (25), perturbation=line_wrap (19), perturbation=none (19), perturbation=ocr_noise (6), pre_redacted=yes (5)
- LW / qs_v1: Lexical baseline, not a Laya arm: TF-IDF + logistic regression trained on arm C's own training units (pii_present only; no role rule, no other questions). Latency is CPU batch scoring, amortized per unit, and not comparable to the model arms.
- LW / qs_v1: test: slice recall from fewer than 30 positives: doc_type=delegation_log (14), doc_type=deviation_log (23), doc_type=icf_signature_page (17), lang=de (26), lang=es (6), lang=pl (14), pii_depth=early (11), pii_depth=late (21), pii_depth=middle (11), split_span=yes (17)
- LW / qs_v1: test: slice forward rate from fewer than 30 negatives: lang=de (7), lang=es (1), lang=pl (4), split_span=yes (1)
- LW / qs_v1: holdout: slice recall from fewer than 30 positives: hard_negative=yes (14), length_bucket=short (22), perturbation=headers_footers (25), perturbation=line_wrap (19), perturbation=none (19), perturbation=ocr_noise (6), pre_redacted=yes (5)
