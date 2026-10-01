# M8 gold audit of the scaled corpus (D-022), 2026-09-30

An independent gold-auditor subagent worked read-only on corpus e9a9f05069534427 (1,600 docs). The
builder transcribed this summary.

## Verdict: PASS. Zero label errors and zero unlabeled PII.

### Sample

44 stratified docs, 37 of them from the new ids above d0600. The sample covers:

- all 12 doc types, all 4 languages and all length buckets;
- partial-redaction, partial-alt and pii_depth docs (early, middle, late);
- 7 OCR-noise and 18 hard-negative docs;
- 7 deviation logs (all 107 were also checked).

### Checks run over all 1,600 docs

- **Offsets.** Every span and negative matches its value (0 failures).
- **World cross-check.** All 14,947 spans match a world value with the right category and role
  (0 failures).
- **Unlabeled-PII scan.** OCR-normalised: names, given/family names, initials, contacts, ids,
  MRNs, streets, postcodes, subject dates and ages over 89. Found 0.
- **Dates outside spans/negatives.** 0.
- **CRF visit dates vs the world.** 2,054 dated rows, 0 mismatches.
- **Unit gold recomputed from spans and policy.** 1,261 units, 0 mismatches.
- **Deviation logs.** Every row is a real deviation in order. 33 short logs are truncated to
  their earliest rows; no rows are invented.
- **Invariant 10 (fictional world).** Holds.

## Concerns raised, and fixes applied before training (commit "M8: 8c")

1. **OCR name guard checked single edits.** Two drops in one word could still form a name
   ("Samples" -> "Sales" in d0611; harmless there, as no world person has that name). The guard
   now checks each word after all its edits and drops them all if the result is a name token.
2. **Garbled depth blocks.** 74 of 160 "Note to file" blocks rendered alt text in disabled
   slots, e.g. "(subject the participant) attended the visit on the participant", a possible
   training cue. The block now renders with its four categories enabled. 0 such blocks remain.
3. **Place name "Klinikum Birkenau".** It echoed Auschwitz-Birkenau. Composed place names now skip
   a denylist of atrocity-site stems. 0 remain.

## Not changed, but noted

- Conmed padding rows reuse the subject's real dates, which gives implausible drug/indication
  pairs. The labels are correct.
- Standing conventions stay as before: ages of 89 or under are not labeled; report and quote
  dates are non_phi_date.

## Corpus after the fixes

- Corpus: 55dbb36fe63f9c1b. V1–V6 pass, labels deterministic, split leak-free and class-complete.
- Split: train/calib/test/holdout = 927/256/337/80 docs; PII units 1,017/308/419/56 (arm A).
- Training data: 32,536 records, verified train-only.
