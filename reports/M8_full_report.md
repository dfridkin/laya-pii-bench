# Laya Personally Identifiable Information (PII) Benchmark: Full Report (M8)

Oct 2, 2026 · Dmitriy Fridkin

*Exported from the shared report doc. The recall vs work-saved chart is not included here; its
data is the curve table in `reports/report.md` (rows at calib targets 0.90 to 0.995).*

## Summary

We tested whether Laya, a small open-source artificial intelligence (AI) model, can tell which chunks of clinical-trial paperwork contain personal data: names, contact details, record numbers, birth dates and the like. Each chunk is roughly a paragraph, about 200 words. All 1,600 documents were synthetic, with a made-up sponsor, sites and people.

The short answer: once trained on examples, Laya is a very good filter on these documents. But the test was easier than real life, so the result is not yet proven.

- **Off the shelf, Laya isn't useful here.** To catch 99.5% of personal data, it had to send 99.5% of the text to a person anyway.
- **After training (fine-tuning), it cleared 93% of the text as safe** and let 1 chunk with personal data through out of 419. Its ranking score, the area under the receiver operating characteristic curve (AUROC), was 0.9999. On that scale 0.5 is a coin flip and 1.0 is perfect.
- **A crude word-counting model came close.** Trained on the same examples, it scored 0.986 and cleared 51-61% of the text at the same safety level. That suggests the synthetic documents have obvious patterns that real ones won't.
- **The multilingual versions of Laya did no better than chance**, even when reading whole documents.
- **On an ordinary 8 GB M2 MacBook Air**, Laya takes about 0.7 seconds per chunk.

Laya only flags chunks. It doesn't point to the exact words or remove them. Its strength is reading context, so it fits best as a second opinion beside a rules-based scanner (see the Conclusion). It needs testing on real documents before anyone relies on it.

## What we tested

We asked Laya one main question per unit of text: does it contain personal identifiers of a patient or site staff member? Every document is synthetic: fictional sponsor, sites, compounds and people.

**Corpus.** 1,600 generated clinical-trial documents across 12 types (clinical study report (CSR) narratives, case report form (CRF) pages, serious adverse event (SAE) forms, lab reports, monitoring reports, protocol sections and others). The PII positions come from the generator itself, never from searching the text.

**Splits, by site so no person appears in two splits.**

| split | documents | used for |
| --- | --- | --- |
| train | 927 | fine-tuning arm C and the lexical baselines only |
| calib | 256 | fitting thresholds and temperatures |
| test | 337 | every headline number (5,713 units, 419 with PII) |
| holdout | 80 | institutional review board (IRB) letters only, descriptive |

**Arms.**

| arm | model | unit of text | notes |
| --- | --- | --- | --- |
| A | Laya English (ModernBERT-large, 421 million parameters), zero-shot | 256-token chunks | the baseline Laya setup |
| B1-B4 | Laya multilingual (mmBERT, 322 million parameters), zero-shot | 768 tokens to whole document | B3 and B4 score whole sections or documents, so they have few units and wide intervals |
| C | Laya English, fine-tuned on train-split units | 256-token chunks, same units as A | trained on two Kaggle T4 graphics processing units (GPUs), 3 epochs |
| LW, LC | word or character n-gram counts weighted by term frequency-inverse document frequency (TF-IDF), fed to a logistic regression | same units as A | lexical baselines trained on C's own training units |

**Routing.** Each unit gets a calibrated probability that it contains PII, written p(PII). Below a low threshold it is forwarded without review. Above a high threshold it is redacted. In between it goes to a person. The low threshold is fit on the calib split so that 99.5% of calib PII units are caught. The test split stayed sealed until scoring.

We ran two question sets. qs\_v1 is three questions plus a rule that always redacts units naming a patient. qs\_v2 asks five questions, adding per-category yes/no. The PII question is worded the same in both.

## Head-to-head on the test set

At the same 99.5% recall target, C passes 92.6% of units without review, 1.5 to 1.8 times more than the lexical baselines. Zero-shot Laya passes almost nothing.

| arm (qs\_v1) | AUROC p(PII) | units passed without review | clean units passed | PII units missed (of 419) | recall, exact 95% range | M2 median per unit |
| --- | --- | --- | --- | --- | --- | --- |
| C, fine-tuned Laya | 0.9999 | 92.6% | 99.9% | 1 | 99.76% (98.68-99.99%) | 708 milliseconds (ms) |
| LC, char n-gram baseline | 0.986 | 60.8% | 65.6% | 2 | 99.52% (98.29-99.94%) | central processing unit (CPU), not comparable |
| LW, word n-gram baseline | 0.985 | 51.2% | 55.2% | 1 | 99.76% (98.68-99.99%) | CPU, not comparable |
| A, zero-shot Laya | 0.786 | 0.5% | 0.6% | 0 | 100% (99.12-100%) | 622 ms |
| B4, best multilingual (picked on calib) | 0.466 | 0% | 0% | 0 of 215 docs | 100% (98.30-100%) | not re-timed |

All arms are scored on the same 337 test documents. A, C, LW and LC see identical units. B4 judges whole documents, so its counts are per document.

On qs\_v2, C passes 92.6% and misses 2 units: 99.52% recall (98.29-99.94%). The extra miss is a lone Zone Improvement Plan (ZIP) code that qs\_v1's patient rule caught. Under both question sets the 99.5% target is neither confirmed nor rejected: the lower bound is below 99.5% and the upper bound above it.

## Recall vs work saved

C's work saved barely moves as the recall target tightens. The baselines give up a third of theirs for the last half point of recall.

*Chart: "Fine-tuned Laya skips review for 92.6% of text at the strictest setting" (in the shared doc; data in `reports/report.md`, curve table).*

Each point is a threshold fit on calib for one recall target, then applied to test. C's flat line reflects saturated scores: it has very few distinct thresholds to choose from.

## Arm C in detail

C's operating point is all-or-nothing and rests on one or two calibration units. Its misses are confident ones, not borderline calls.

**No review band.** C's scores pile up at the extremes: 5,708 of 5,713 test units have a top probability of 0.933 or more. The low and high thresholds land on the same value (0.9697), so every unit is either passed or redacted and nothing reaches a person. The low threshold is the second-lowest scoring PII unit in calib (p 0.962). One calibration unit more or less would move it.

**The misses.**

| unit | question sets | p(PII) | what was missed | context |
| --- | --- | --- | --- | --- |
| d0693, chunk 6 | qs\_v1, qs\_v2 | 0.002 | initials "JXM" | tail of a CRF vitals table, then boilerplate |
| d0625, chunk 24 | qs\_v2 only | 0.965 | ZIP code "10504" | a lone ZIP code followed by filler; qs\_v1's patient rule redacted it |

Both are a single quasi-identifier surrounded by template text. The first is the worrying kind: C was certain there was nothing there.

**Not memorisation.** C catches 123 of 124 test PII units whose values never appear in training, and 294 of 295 that do. No subject identifiers (IDs), record numbers, emails, phones, addresses or birth dates are shared between train and test.

**Holdout (80 IRB letters, 56 PII units).** C scores AUROC 1.000, passes 91.7% of units and misses none. This is weak evidence of transfer:

- the letters' PII is only names and emails in headers;
- 33 of the 56 PII units name an investigator C saw in training;
- the lexical baselines also score 0.996 here.

## How much is the corpus doing

Most of C's jump from AUROC 0.786 to 0.9999 comes from how predictable the generator's text is. A bag-of-words model with no language understanding gets to 0.986.

C is trained and tested on the same generator: the same templates, filler text and fake-name world, with different sites and people. Clean text in test is mostly boilerplate already seen in training. On average 93% of a clean test unit's 8-word phrases appear in training text, against 44% for a PII unit. A score that only measures "how novel is this text" reaches AUROC 0.953 with no learning at all.

C still beats the baselines where it matters most. In the results review's own baseline analysis:

| hard case (test) | units | C wrong | baseline wrong |
| --- | --- | --- | --- |
| clean units with only coded IDs, sent to review | 69 | 1.4% | 20% |
| clean units with non-personal dates, sent to review | 80 | 1.3% | 34% |
| clean units with compound codes, sent to review | 65 | 1.5% | 29% |
| pre-redacted clean units, sent to review | 14 | 0% | 64% |
| PII units with a name only, missed | 30 | 0% | 57% |
| PII embedded in boilerplate, missed | 35 | 6% (2) | 60% |

That baseline (test AUROC 0.993) was fit in the review's own scripts, not by the pipeline. LW and LC are the pipeline's versions.

C's two misses are exactly where the template cue fails: PII sitting inside boilerplate. Real documents won't share this generator's boilerplate, so how C handles them is untested.

## Speed on the Apple M2

On an 8 GB Apple M2 laptop, Laya handles about 1.4 to 1.6 units a second, one unit at a time. Fine-tuning does not change the model's size, so C should cost the same as A.

| arm | median per unit | 95th percentile | units per second |
| --- | --- | --- | --- |
| A, zero-shot | 622 ms | 685 ms | 1.6 |
| C, fine-tuned | 708 ms | 726 ms | 1.4 |

Both runs timed the same 1,000 test units, with qs\_v1 and 10 warm-up calls discarded. C ran directly after A and the order was not swapped. Same architecture, same 16-bit floating-point (F16) weights, so part of C's 14% gap is likely heat build-up, not the model.

For scale, the Kaggle T4 GPU ran the same units at about 130 ms each. Those runs were for accuracy, not the speed headline.

## Caveats and limits

The biggest limit is that every number here comes from one synthetic generator.

- **In-distribution only.** C was trained and tested on the same templates and fake world. No real or independently written documents were scored.
- **Training mix differs from test.** C trained on every PII unit plus 3 clean units per PII unit, so 25% of its training units had PII against 7.3% in test.
- **Mostly English, no IRB letters.** 792 of C's 859 training documents are English. German, Spanish and Polish test slices are small (6 to 26 PII units each).
- **Small slices.** Recall for several document types and PII-depth groups rests on fewer than 30 PII units. Treat those slice numbers as rough.
- **Classifier only.** We judged whether a unit contains PII, not where. Nothing here finds or redacts spans.
- **Hardware split.** Accuracy runs ran on Kaggle T4 GPUs and speed runs on the M2. Accuracy does not depend on the hardware.
- **Curve definition changed after C's results were visible.** Both changes were disclosed and approved in the project's decision log (entry D-007). Neither moved a threshold or the headline point.

## Provenance

Every number above can be regenerated from the repo (laya-pii-bench, commit e7bd6ad) and was checked by an independent gate review.

| item | identifier |
| --- | --- |
| corpus (1,600 docs) | Secure Hash Algorithm 256 (SHA-256) fingerprint 55dbb36f... |
| C training data (32,536 records, train split only) | manifest sha256 2fdd6558... |
| C checkpoint weights | sha256 6809676153aa... (pinned in models.lock.json) |
| calibration, frozen before scoring | commits 047aad7 (Laya arms), b9836b9 (baselines) |
| scores and report | commit 27af1a6, `reports/report.md` |
| results review | `reports/audits/M8_results_review.md` |
| gate review (PASS) | `reports/audits/M8-gate-20261002.md` |

The test split stayed sealed until scoring. Thresholds and temperatures were fit on calib only, committed, then hash-checked by the scorer. Best B was picked on calib, never on test.

## Conclusion

Fine-tuned Laya is worth taking forward, but as a context reader inside a larger pipeline, not as the whole personal-data scanner.

**What Laya is good at.** It reads a whole chunk and judges whether, taken together, the text identifies someone. Rule-based tools can't do that. "The 34-year-old site pharmacist who moved from the Lyon clinic last month" names no one, yet points to one person. Laya can also say whose data it is, patient or staff, which matters when the two are handled differently.

**What it can't do.** It doesn't mark the exact words to remove, so it can't redact on its own. And when it misses, it can be confidently wrong: it rated the initials it missed as 0.2% likely to be personal data, so a "send unsure cases to a person" rule would not have caught them.

**The pipeline we recommend.**

1. Run a rules-based scanner, such as Microsoft Presidio, on every chunk. Pattern rules backed by nearby trigger words ("date of birth (DOB)", "medical record number (MRN)", "initials") reliably catch structured identifiers: subject numbers, record numbers, emails, phone numbers, ZIP codes and initials. A name-finding model, known as named entity recognition (NER), or a list of known site staff covers names. The scanner also does the redaction, because it knows exactly where each item sits.
2. Run fine-tuned Laya on every chunk as a second opinion.
3. Let disagreements decide what a person reads:

| rules scanner | Laya | what happens |
| --- | --- | --- |
| finds something | says personal data | redact automatically |
| finds nothing | says clean | pass through, no review |
| finds nothing | says personal data | a person reviews it: likely context-only personal data, or a scanner miss |
| finds something | says clean | redact anyway; spot-check if false alarms are costly |

Neither tool is the only safety net, and human time goes to the small share of text where they disagree.

**Whether Laya earns its place is still open.** A rules scanner plus a good clinical name model might catch nearly everything on real documents. If so, Laya adds cost (about 0.7 seconds per chunk) for little gain, and the simpler setup wins.

**Next steps.**

1. Test on a sample of real, approved documents. That result decides everything above.
2. Compare three setups on the same documents: the rules scanner alone; the scanner plus Laya with disagreement review; and the scanner plus random human spot-checks. Measure identifiers missed and review time. Keep Laya only if it catches what the scanner misses or clearly cuts review time.
3. Drop the multilingual Laya models for this task, and don't use Laya without fine-tuning.
