# M4 gold-label audit, run 4 (final corpus after D-020; gold-auditor subagent), 2026-09-27

Gate-5 record for the final corpus. Chain: run 1 -> run 2 -> run 3 (M4_gold_audit_run3_final.md, corpus 3507af1f,
zero errors, R1-R4) -> fixes b02159e (R2, R3), a2abb55 (R4, D-020) -> run 4 (this file).

Corpus data/docs.jsonl, 600 docs, sha256 9a88ce5c4c5b4a8559ef9b624d720dd823dd4fb0fdbf68115fae84b6894fada5 (matches
gen_manifest; all validators pass), HEAD a2abb55. Sample n=30, random.Random("M4-gold-audit-42").sample(sorted ids, 30),
same ids as runs 1-3 (contents regenerated): d0032 d0034 d0035 d0047 d0071 d0073 d0076 d0091 d0095 d0100 d0124 d0164
d0191 d0192 d0197 d0208 d0223 d0299 d0331 d0347 d0366 d0433 d0468 d0485 d0531 d0538 d0560 d0564 d0588 d0593.

**Verdict: CLEAN. Zero label errors.** Sample: 446 spans (phi_quasi 241, coded_id 136, staff_pii 56 [53 staff, 3
sponsor], phi_direct 13), 180 negatives. Partial-alt docs in sample: d0076 d0091 d0331 d0366 d0531. Units spot-check
not applicable (no data/units yet).

## Method
1 offsets/overlaps, all 600 docs: 0 failures. 2 world scan (every person token incl. drops, emails, phones,
initials forms, subject-id forms, rand nos, MRNs, streets, postcodes, every date surface of every same-site subject
date; OCR-normalised, wrap-tolerant; separate plain-initials scan); control run detects all 446 sample spans (22 plain
initials via the initials scan). Corpus-wide: 0 unlabeled names/ids/contacts; 211 raw date-collision hits all inside
non_phi_date negatives (sent/report/version/meeting/effective dates); 9 plain-initial hits are template tokens (HR, II,
AW). 3 pattern scan + inline read-through of all 30. 4 world cross-check of all 5,398 corpus spans: every span resolves
to a world value at the doc's own site with the category/role implied by value_kind; role sponsor iff sponsor_contact
(49); 2 age spans (94) phi_quasi; 66 age and 60 sex mentions match. 5 table rows: 1,003 id/initials+date lines bind to
one subject; all 2,075 CRF "Visit N" rows have labeled dates equal to that subject's Visit N date (incl. 991 rows with
no id/initials); 0 unlabeled CRF dates. 6 conventions as runs 1-3. 7 pii_depth: 60 (20/20/20), English long/xl prose,
single compact block in band, none partial-redact/alt. 8 D-015 tags: hard_negative 150 exact; pre_redacted exactly the
59 docs with a pre_redacted negative; languages 24/18/18 short site-facing; IRB/protocol no patient spans, protocol no
spans. 9 invariant 10: NCT99 x81, EudraCT 2031 x81, FTX- compounds only; 48 CAS all invalid check digit; example.org/com
only (+ OCR "examp1e"); sponsor Fenwick only; "Johnson" is a labeled Faker staff surname.

## Per-doc verdicts (spans/negatives)
d0032 conmed clean 0/1 OK | d0034 narrative de 12/3 OK | d0035 protocol 0/12 OK | d0047 deviation 16/2 OK |
d0071 protocol 0/10 OK | d0073 lab hard-neg 5/12 OK | d0076 deviation partial-alt OCR 8/6 OK | d0091 correspondence es
partial-alt 6/1 OK | d0095 SAE partial-redact 4/8 OK | d0100 protocol 0/1 OK | d0124 CRF 160/2 OK | d0164 deviation
24/6 OK | d0191 delegation partial-redact 9/16 OK | d0192 correspondence depth early 3/1 OK | d0197 delegation clean
0/2 OK | d0208 narrative depth middle xl 4/24 OK | d0223 delegation 12/5 OK | d0299 protocol xl 0/14 OK | d0331
deviation partial-alt 4/2 OK | d0347 lab partial-redact 5/2 OK | d0366 CRF partial-alt 134/2 OK | d0433 delegation
partial-redact OCR 10/10 OK | d0468 SAE de 5/5 OK | d0485 ICF 4/2 OK | d0531 ICF de partial-alt 3/3 OK | d0538
monitoring clean 0/8 OK | d0560 narrative depth early 4/12 OK | d0564 protocol 0/1 OK | d0588 correspondence
partial-redact 10/2 OK | d0593 SAE OCR 4/5 OK.

## Label errors
Zero.

## (a) Partial-alt docs (all 100)
Flag set replays exactly from corpus.plan (100); no overlap with partial-redact or depth. 23 (type, lang) strata;
every stratum with PII-free site docs has >= 1. Dropped categories: coded_id 32, staff_pii 20, phi_quasi 19,
phi_direct 7; 22 single-category docs dropped nothing. 0 spans outside the post-drop enabled set; 0 spans of the
dropped category; 0 alt-phrase occurrences overlap a span; all spans resolve. No leak of the dropped category (0
unlabeled names/ids/contacts/initials; 21 date hits all non_phi_date negatives). "Each doc still has PII" not fully:
d0104 (IRB, all 5 values drawn alt) and d0518 (de correspondence) came out PII-free (gold correctly empty); d0270 drew
no alt. 97/100 show alt beside real PII, matching the manifest (realized 97 / none_drawn 3).

## (b) R4 metric recomputed independently
Phrase inventory from templates (154 alt strings incl. pick options), render.py ALT defaults, age() alts. Counting on
rendered text only (whitespace/separators normalised): 530 site docs, 424 PII-bearing, 106 PII-free.
Phrase level: 3/106 (2.8%), same docs as the manifest: d0472 (de correspondence), d0518 (de correspondence
partial-alt that came out PII-free), d0580 (pl correspondence "(patrz zapytanie)"). gen_meta.alt_phrases honest (4
logged phrases absent from text only through later OCR damage; "over 89" not logged but only in PII-bearing docs).
Context level (stricter, phrase + preceding template literal on the line): 14/106 (13.2%): 10 IRB letters (9 clean +
d0104) contain "Contact: IRB office, IRB office" (0 PII-bearing); "IRB Chair, IRB Chair" in 10 PII-free and 2
PII-bearing letters; d0314 (de ICF, "Geburtsdatum: ____________", stratum of 2); the 3 correspondence docs.
Run 3's CRF "for subject (see first row)" residue gone at both levels.

## (c) R1-R3
R1 unchanged by design (also for alt text), labels correct, accepted. R2 resolved (manifest realized vs none_drawn;
independent count 46 realized, 14 none; every placeholder a pre_redacted negative, none overlaps a span). R3 resolved
(age() consumes _redact_next via _off; other helpers call _off immediately). R4 resolved at phrase level (3/106 < 5% V5
guard, confirmed independently); context-level residue S1.

## New concerns (no label changes)
S1 line-level alt shortcut in IRB letters ("Contact: IRB office, IRB office" in all 10 PII-free letters, 0
PII-bearing); IRB letters are holdout-only (D-005), so train/calib/test unaffected; holdout IRB results could be
inflated. Fix options: alt neighbouring slots on the same line together; extend V5 to phrase+context.
S2 partial-alt can produce PII-free docs (d0104, d0518): 97 not 100 PII-bearing.
S3 D-020 says "staff first" but the drop rotates within a stratum (staff dropped in 20 of 78 drops).
S4 admin dates can equal a non-referenced same-site subject's date (e.g. d0588 2025-06-20); non_phi_date negatives,
not patient dates in context; same accepted convention as N7.
Suspicious (label-affecting): none.
