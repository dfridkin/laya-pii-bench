# M4 gold-label audit, final corpus (gold-auditor subagent), 2026-09-27

Corpus data/docs.jsonl, 600 docs, sha256 766bdf4589ff2240556a63dcfb0a7bbeeed359f2da156580e032e744bf537e4a, HEAD 71f265a.
Sample n=30, random.Random("M4-gold-audit-42").sample over sorted ids (same ids as run 1, reports/audits/M4_gold_audit_run1.md):
d0032 d0034 d0035 d0047 d0071 d0073 d0076 d0091 d0095 d0100 d0124 d0164 d0191 d0192 d0197 d0208 d0223 d0299
d0331 d0347 d0366 d0433 d0468 d0485 d0531 d0538 d0560 d0564 d0588 d0593. Audited on data/docs.jsonl directly.

**Verdict: CLEAN. Zero label errors.** 761 spans (coded_id 311, phi_quasi 369, phi_direct 13, staff_pii 68: 63
staff, 5 sponsor), 175 negatives (16 kinds); every value == text[start:end]; no overlaps.

## Method
1 offsets/overlaps. 2 world scan: every person's forms (all name surfaces + bare given name, emails, phones, MRNs,
streets, postcodes, subject-id forms, rand nos, dotted/dashed/middle_x initials, every date form of every subject's
DOB/enrolment/visit/AE/conmed/deviation dates), case-insensitive, whitespace/wrap tolerant; OCR-variant pass (l/1,
O/0, Z/2, S/5, B/8 + single drops) on 25 site docs; control run fires (d0433 "Augusta Jesse1"). 3 pattern scan
(digit runs, months, @, honorifics, ID-like tokens, non-vocabulary capitalised words) + inline-label read-through.
4 world cross-check: every span resolves to an entity of the doc's site (incl. OCR-damaged values); role matches job;
352 row-bound dates/initials in 11 tabular docs belong to their row's subject; AE term/onset/recovery/grade/
relatedness/age/sex/DOB/MRN/rand match the world in sampled SAE and narrative docs. 5 conventions. 6 pii_depth.
7 D-015 tags. 8 invariant 10. 9 corpus-wide J1-J8 checks. Units spot-check skipped (no data/units yet).

## Per-doc verdicts (spans/negatives)
d0032 conmed clean 0/1 OK | d0034 narrative de 12/3 OK | d0035 protocol 0/12 OK | d0047 deviation 64/2 OK |
d0071 protocol 0/10 OK | d0073 lab 5/12 OK | d0076 deviation 60/5 OK | d0091 correspondence es 13/1 OK |
d0095 sae 6/7 OK | d0100 protocol 0/1 OK | d0124 crf 160/2 OK | d0164 deviation 98/5 OK | d0191 delegation 12/14 OK |
d0192 correspondence depth early 3/1 OK (10.4-10.7%) | d0197 delegation clean 0/2 OK | d0208 narrative depth middle
xl 4/24 OK (50.8-51.0%) | d0223 delegation 12/5 OK | d0299 protocol xl 0/14 OK | d0331 deviation 86/2 OK |
d0347 lab 6/1 OK | d0366 crf 176/2 OK | d0433 delegation 12/12 OK | d0468 sae de 5/5 OK | d0485 icf 4/2 OK |
d0531 icf de 4/3 OK | d0538 monitoring clean 0/8 OK | d0560 narrative depth early 4/12 OK (11.0-11.3%) |
d0564 protocol 0/1 OK | d0588 correspondence 11/1 OK | d0593 sae 4/5 OK.

## Other checks
Negatives: protocol_no 99, site_no 17, eponym 14, non_phi_date 13, compound_code 9, nct_id 4, eudract_no 4,
report_no 3, cas_no 2, meddra_code 2, dose 2, amendment_no 2, reference_range 1, lot_no 1, kit_no 1, visit_window 1;
none is person data. hard_negative on exactly 150/600 docs, all with injector negatives, none untagged with them;
pre_redacted on all 13 redacted docs. Invariant 10 OK corpus-wide (all 41 CAS numbers invalid check digit; no real
sponsors/drugs/NCT0/non-example domains; protocol text generic).

## J1-J8 status
J1 resolved by documentation (domain.md defines WorldRefs.subjects as a conservative superset; 87 zero-span docs list
subjects, intended). J2 resolved (60/60 SAE use subjects with world AEs; onset matches 54/54 normal-mode forms;
grade 60/60; recovery 34/34). J3 partly resolved: SAE report after onset 60/60; ICF version before signature 19/19;
correspondence sent after visit 2 in 70/70 non-depth cases; NOT for pii_depth correspondence (10 depth docs have
sent <= depth subject's visit 2; e.g. d0192 email Feb 2 2025 vs note visit 04/24/2025). J4 resolved (all eponyms in
fitting context, 4 languages). J5 partly resolved: no brackets or ungrammatical forms; placeholder families now in
343/426 PII-bearing and 91/104 PII-free site docs; residuals "Subject not stated" only in 13 clean conmed/lab views,
"Principal Investigator (Principal Investigator)" in 25 docs. J6 resolved (no English filler or AE terms in 60
non-English docs; residual English running header in 24/60, roughly independent of PII). J7 unchanged, correct as
specified (3 age spans 93/92/95; no unlabeled age >= 90). J8 resolved (halcyon-cro.example.com; no collisions).

## New generator-level concerns (no label changes)
N1 49/60 CIOMS forms report a non-serious AE (fallback to any AE of the subject); prefer a site subject with a serious AE.
N2 deviation logs pad with invented "visit outside window" deviations (286/1017 rows are world deviations); exact
   repeats occur (d0164 rows 8-10); cross-document consistency class of J2; labels unaffected (real visit dates).
N3 CRF rows drawn with replacement: 263 duplicate subject/visit rows with conflicting vitals in 21/70 CRF pages.
N4 depth narratives headed "Subject number not assigned" but the note gives the number (d0208, d0560); plus the J3
   residual above.
N5 pre-redaction tokens ([REDACTED], XX-XXXX, ***) occur only in the 13 PII-free redacted views: a perfect "no PII"
   cue; consider partial redactions in PII-bearing docs.
N6 English header/footer in non-English docs (J6 residual), low risk.
N7 document dates can equal another same-site subject's date (not tied to that subject in text; not PII; V2 scoped
   correctly); safe_date avoids the view's subjects, not the whole site.

Suspicious (label-affecting): none. d0433 "M-H" matches coordinator and IRB chair initials, both role staff.
