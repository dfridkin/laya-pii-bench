# M4 gold-label audit, run 3 (final corpus; gold-auditor subagent), 2026-09-27

This is the gate-5 record for the final corpus. Chain: run 1 (reports/audits/M4_gold_audit_run1.md, corpus 600fada2,
zero errors, J1-J10) -> fixes 666f076, 71f265a -> run 2 (reports/audits/M4_gold_audit.md, corpus 766bdf45, zero
errors, N1-N7) -> fixes 4155f53 -> run 3 (this file). Audits are write-once, hence the separate file.

Corpus data/docs.jsonl, 600 docs, sha256 3507af1fba6661b47508f114e1810422bd122556fa964027e60223d66ac32477 (matches
gen_manifest), HEAD 4155f53. Sample n=30, random.Random("M4-gold-audit-42").sample(sorted ids, 30), same ids as runs
1-2, sample lines byte-identical to the corpus.

**Verdict: CLEAN. Zero label errors.** Sample: 511 spans (phi_quasi 271, coded_id 165, staff_pii 62 [57 staff,
5 sponsor], phi_direct 13), 180 negatives (protocol_no 99, site_no 17, non_phi_date 14, eponym 13, compound_code 9,
pre_redacted 8, cas_no 3, reference_range 3, report_no 3, nct_id 2, eudract_no 2, meddra_code 2, dose 2, lot_no 1,
kit_no 1, visit_window 1). value == text[start:end], no overlaps: sample and all 600 docs.

## Method
1 offsets/overlaps (sample + corpus). 2 world scan (all person tokens, emails, phones, MRNs, streets, postcodes, subject
ids, rand nos, ISO DOBs; wrap-tolerant) on sample + all 60 partial-redaction docs; OCR-variant pass (l/1, i/1, o/0,
s/5, b/8, z/2, single drops); control run with labels stripped fires on every name/id incl. "Jesse1". 3 pattern scan +
inline read-through of all 30. 4 corpus-wide world cross-check: all 1,128 staff_pii spans resolve to a person at the
doc's own site, role sponsor iff sponsor_contact (CRA staff); every patient span in all 600 docs resolves to a
world_refs subject incl. OCR-damaged values and Polish month names (by hand); age 94 spans correct (phi_quasi).
5 table rows: sample 140 row-bound dates belong to their row's subject; corpus-wide all 1,268 labeled CRF rows match
the subject's Visit N date and initials (incl. rows with redacted id). 6 conventions as runs 1-2. 7 pii_depth: 60/60
single compact block in band; demographics match (48/48). 8 D-015 tags: hard_negative exactly 150 (all with injector
negatives, none untagged); pre_redacted exactly the 59 docs with a pre_redacted negative; languages 24/18/18, all
short, site-facing; long/XL prose only; IRB and protocol docs no patient data. 9 invariant 10: NCT99, EudraCT 2031,
FTX only; all 51 CAS invalid check digit; example.org/.com only (one OCR "examp1e"); no real sponsor/drug names.

## Per-doc verdicts (spans/negatives)
d0032 conmed clean 0/1 OK | d0034 narrative de 12/3 OK | d0035 protocol 0/12 OK | d0047 deviation 16/2 (8 world
deviations) OK | d0071 protocol 0/10 OK | d0073 lab 5/12 OK | d0076 deviation 10/7 OK | d0091 correspondence es 13/1
OK | d0095 SAE partial 4/8 (initials+onset redacted; serious AE) OK | d0100 protocol 0/1 OK | d0124 CRF 160/2 (53
distinct rows) OK | d0164 deviation 24/6 (no repeats) OK | d0191 delegation partial 9/16 OK | d0192 correspondence
depth early 3/1 (sent May 21 after depth visit Apr 24) OK | d0197 delegation clean 0/2 OK | d0208 narrative depth
middle xl 4/24 ("Subject number on file") OK | d0223 delegation 12/5 OK | d0299 protocol xl 0/14 OK | d0331 deviation
16/2 OK | d0347 lab partial 6/1 (no value drawn for redaction) OK | d0366 CRF 176/2 OK | d0433 delegation partial
10/10 OK | d0468 SAE de 5/5 (serious) OK | d0485 ICF 4/2 OK | d0531 ICF de 4/3 OK | d0538 monitoring clean 0/8 OK |
d0560 narrative depth early 4/12 OK | d0564 protocol 0/1 OK | d0588 correspondence partial 10/2 OK | d0593 SAE 4/5 OK.

## Label errors
Zero.

## Partial-redaction docs (all 60 checked)
No span value contains placeholder characters; every [REDACTED]/XX-XXXX/*** (incl. OCR forms [REDCTED], [REACTED],
[REDACTD]) is a pre_redacted negative; none overlaps a span; every placeholder sits in a PII slot; zero unlabeled world
values in the 60 docs (other mentions of the same person are labeled, e.g. d0324); remaining spans correct (60/60);
CRF rows with a redacted id still bind by initials + Visit N date. Shortfall: 14 of 60 flagged docs contain no
placeholder (per-value rate 0.2; d0149 d0217 d0219 d0281 d0302 d0337 d0347 d0356 d0397 d0414 d0451 d0488 d0530
d0599): effective 46; V5 counts the flag.

## N1-N6, J3, J5 status (corpus-wide)
N1 resolved (58/60 serious; 2 at sites with no serious AE, documented fallback; first date = onset 43/44, 1 OCR).
N2 resolved (all rows are world deviations; 3 non-matches OCR; duplicates only in 8 clean views rendering identically).
N3 resolved (0 duplicate subject/visit pairs; 1,268 rows consistent). N4 resolved (0 "number not assigned"). N5 resolved
in substance (placeholders in 46 PII-bearing + 13 PII-free docs). N6 resolved (0/60 non-English docs with English
header/footer). J3 resolved (SAE 60/60; correspondence 60/60 incl. 17/17 depth; ICF 30/30). J5 partly resolved: role
duplication gone; but 49 of 104 PII-free site docs contain an alt phrase that never appears in a PII-bearing doc (CRF
"for subject (see first row)" 18, IRB "To: the Principal Investigator"/"Contact: IRB office" 9, ICF/delegation
underscore blanks 9, non-English correspondence alts); cause: alt text only renders where a category is off, i.e.
clean views. Reverse cue (alt phrases only in depth narratives, which always carry PII) benign. N7 accepted.

## New concerns (no label changes)
R1 per-value redaction is inconsistent within a doc (redacted name beside the same person's labeled email/initials,
e.g. d0477, d0191); low risk. R2 partial_redact flag vs actual placeholders (above). R3 latent state leak in
DocCtx.age(): when age > 89 and _on triggers a redaction, age() returns "over 89" without _off, leaving _redact_next
set for the next alt; label-neutral (can only turn alt text into a placeholder), not exercised in this corpus.
R4 J5 exclusivity (above): the most material remaining shortcut risk.

Suspicious (label-affecting): none. Residual OCR-scan hits "enry" (from "entry", d0593) and "yers" (from "years",
d0233) are filler words, not PII.
