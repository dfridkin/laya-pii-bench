# M8 results review: laya-pii-bench (HEAD f7d5ce4)

Reviewer: results-analyst subagent, 2026-10-02. Read-only; no models loaded. It recomputed from
runs/{A,C}, data/units, docs, splits, calib/C__* and finetune/data, and fit scikit-learn baselines
(scripts in the session scratchpad: load.py, shortcut.py, hard.py, dup.py). The builder
transcribed this text.

## Verdict: PASS WITH REQUIRED CAVEATS (one-line: NEEDS WORK)

**Integrity: PASS.**
- C's training data is train-only.
- No identifier memorisation was found.
- Calib was frozen before scoring.
- C's headline numbers reproduce.

**Interpretation: must change before sharing.**
- On this corpus, PII vs clean is learnable from surface form.
- C's misses sit exactly where the template cue fails.
- C's curve is inert by construction, and its definition changed after C's test results were
  visible.

## What checks out

- **Training data.** 32,536 records from 4,067 units in 859 documents, all train-split. Every text
  is byte-identical to its unit. The manifest hashes match the scored docs, units and splits.
  Training is a fixed 3 epochs with no model selection; the temperature hold-out is 10% of train
  documents.
- **Splits.** No subject appears in two splits. The only site key shared across splits is
  */SPONSOR: 186 protocol_section docs with no spans, grouped per document (D-005).
- **Units.** A and C units are identical (25,636; 0 differences).
- **Freeze (D-019).** Calib was committed in 047aad7. Every score cites it, and the scores were
  created after it. C's checkpoint sha 6809676153aa matches the pin (4db54bd) and both run metas.
- **AUROC reproduces** (calib / test / holdout):
  - C: 0.99993 / 0.99987 / 1.00000
  - A (qs_v1): 0.742 / 0.786 / 0.629
- **Operating point reproduces.** Forward rate is 92.58% (qs_v1) and 92.63% (qs_v2). Two PII units
  score below t_low: d0693:chunk:512:6 (p 0.002, initials) and d0625:chunk:512:24 (p 0.964, zip).
  The role rule rescues d0625 in qs_v1 only.

## Check 1: leakage and memorisation (PASS)

Share of distinct test PII values also present in train docs:

| value kind | in train |
|---|---|
| person_name | 1.2% (3 of 242: Faker first-name greetings at other sites) |
| subject_id, MRN, email, phone, DOB, address, zip, rand_no | 0% |
| event_date | 71% (small value space, not identity) |
| initials | 55% (small value space, not identity) |

C's recall does not depend on having seen the values:

| test PII units | C recall |
|---|---|
| no value seen in training | 123 / 124 |
| some values seen | 254 / 254 |
| all values seen | 40 / 41 |

The single miss, "JXM", is a set of initials that does appear in training.

**Holdout (D-018).** 33 of 56 positive units name a PI that C saw in training. Seen and unseen
names score the same (p ≥ 0.9973).

## BLOCKER (for sharing)

### B1. The near-perfect result is largely learnable from the generator's surface form

**Lexical baselines.** Trained on C's own 4,067 units, with the threshold fit on calib at the 0.995
target:

| baseline | test AUROC | holdout AUROC | at the 0.995 target |
|---|---|---|---|
| word 1–2-gram TF-IDF + logistic regression | 0.9930 | 0.9987 | 1 miss, 70.6% forwarded |
| char 2–5-gram TF-IDF + logistic regression | 0.9936 | 0.9997 | 2 misses, 66.7% forwarded |

**Novelty score.** A no-learning score (the share of a unit's word 8-grams not found in training
text) reaches test AUROC 0.953:
- Clean test units are 0.930 contained in training text on average, and 85% are at least 0.9
  contained.
- PII units are 0.435 contained, and still 0.506 with their PII values removed.

**C's errors fall where the template cue fails:**

| stratum | n | C | baseline (LR) |
|---|---|---|---|
| PII embedded in boilerplate | 35 | 2 missed (recall 33/35, exact 95% CI 0.81–0.99) | 60% missed |
| PII in novel text | 384 | 0 missed | |
| clean but novel text | 301 | 1.0% escalated | 15% |
| clean boilerplate | 4,517 | 0 escalated | |

**C does beat the baseline on hard cases:**

| slice | n | C | baseline (LR) |
|---|---|---|---|
| coded-id-only negatives, escalated | 69 | 1.4% | 20% |
| non_phi_date negatives | 80 | 1.3% | 34% |
| compound-code negatives | 65 | 1.5% | 29% |
| pre-redacted / alt negatives, escalated | 14 | 0% | 64% |
| name-only positives, missed | 30 | 0% | 57% |

**Required:**
1. Add the baselines, computed in a stage, as rows of the arm comparison.
2. Rewrite C's key finding with an in-distribution caveat:
   > "Arm C is trained and tested on the same synthetic generator (same templates, filler and
   > Faker world; disjoint sites and persons). A bag-of-words classifier trained on the same units
   > reaches test AUROC 0.993, so most of the gain over zero-shot A reflects how learnable this
   > corpus is, not general PII detection. C's advantage over that baseline is concentrated in
   > hard negatives and name-only units. Both of C's misses are single quasi-identifiers embedded
   > in boilerplate (recall 33/35 on PII in boilerplate, exact 95% CI 0.81–0.99). These results do
   > not transfer to real documents without an out-of-generator test."
3. Next: a counterfactual insert/remove probe. The real fix is an out-of-generator test set; the
   D-011 condition ("results look template-trivial") now holds for C.

## MAJOR

### M1. The C curve is inert by construction, and its definition changed after C's test results

- `fit_t_high` clamps `t_high` to at least `t_low`, so C has `t_high = t_low = 0.9697`.
- `curve()` keeps `t_high` fixed while `t_low` rises. The units in between are redacted, so every
  curve row equals the headline point.
- f7d5ce4 changed curve recall to route recall after C's decisions existed.

The real sweep on qs_v1 (forward if p < t_low):

| calib target | t_low | p-recall | misses |
|---|---|---|---|
| 0.90 | 0.9986 | 0.912 | 37 (93.3% forwarded) |
| 0.95 | 0.9986 | 0.931 | 29 |
| 0.98 | 0.9981 | 0.976 | 10 |
| 0.99 | 0.9968 | 0.986 | 6 |
| 0.995 | 0.9697 | 0.995 | 2 |

**Fix:** set `t_high` per point to at least `t_low`; state that C's probabilities saturate (5,708
of 5,713 units at top p ≥ 0.933); record the definition change in DECISIONS.

### M2. The operating point rests on one calib unit and has no escalate band

- `t_low` is the second-lowest calib positive (d1097:chunk:512:9, p 0.962).
- The test miss d0625 (p 0.964) sits just below it.
- At the 0.99-target threshold, misses rise from 2 to 6.
- Because `t_low = t_high`, C has no review band.

### M3. The C key-finding bullets overstate and mix metrics

- The bullet says AUROC 1.000; the table says 0.9999.
- It pairs p-recall with route-recall counts. State route recall per question set:
  - qs_v1: 0.9976, exact 0.9868–0.9999. The patient-role rule rescues one unit.
  - qs_v2: 0.9952, exact 0.9829–0.9994.
- D-008 wording: "1 miss in 419 (exact 95% lower bound 0.987); the 99.5% target is not rejected,
  not demonstrated."

### M4. Holdout is weak evidence of transfer

- The baseline also scores 0.999–1.000 on the holdout.
- Holdout PII is names and e-mails only.
- 33 of 56 positive units name a PI seen in training (D-018).
- 12 of 668 clean letter-header units score p ≥ 0.5.
- The preamble is stale:
  - It says 30 docs and a forward rate of 0; the holdout now has 80 docs, and C forwards 91.7% of
    them.
  - The S1 alt-line cue persists, but holdout AUROC stays 1.000 without those units, so it is not
    driving the result.

### M5. Missing caveats

- C's training sampling: training prevalence is 25%, against 7.3% on test.
- Training is 97% English (3,965 of 4,067 units), with no IRB letters.
- The accuracy runs were on Kaggle 2x T4 (accuracy is hardware-independent; D-002, D-022).

## MINOR

- Recall slices should be flagged as small when they have fewer than 30 positives (forward-rate
  slices: fewer than 30 negatives). Examples: depth early 11, middle 11, late 21; delegation_log 14;
  icf 17; deviation_log 23.
- The speed prose is stale for CUDA runs: it mentions 8 GB, MPS fp16 and "batched for A and B1".
- Calibration table: "AUROC raw/cal" is the correctness AUROC of the confidence. Label it that way.
- The calib files carry `calib_auroc_pii`, written by code committed after the freeze (f7d5ce4).
  This is hash-compatible by design; note it in STATUS.
- Manifest `duplicates_removed` equals `n_units` (the shared pii_present record); document it.

## False forwards (test)

| unit | qs | p | missed value | context |
|---|---|---|---|---|
| d0693:chunk:512:6 | qs_v1, qs_v2 | 0.002 | initials "JXM" | CRF vitals table tail, then boilerplate |
| d0625:chunk:512:24 | qs_v2 only | 0.9647 | zip "10504" | lone zip, then filler; rescued in qs_v1 by the role rule |
