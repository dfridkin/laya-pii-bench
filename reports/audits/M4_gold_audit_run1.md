# M4 gold-label audit, run 1 (gold-auditor subagent), 2026-09-27

Corpus data/docs.jsonl sha256 600fada2082c2ab8701365672ed53ca99a7d6858fa177d4bb7da3d4daf8a9999 (commit b985230).
Sample n=30, random.Random("M4-gold-audit-42").sample over sorted ids; records byte-identical to the corpus:
d0032 d0034 d0035 d0047 d0071 d0073 d0076 d0091 d0095 d0100 d0124 d0164 d0191 d0192 d0197 d0208 d0223 d0299
d0331 d0347 d0366 d0433 d0468 d0485 d0531 d0538 d0560 d0564 d0588 d0593.

**Verdict: CLEAN. Zero label errors.** 758 spans (coded_id 311, phi_quasi 369, phi_direct 13, staff_pii 68 incl.
5 role sponsor) and 181 negatives; every value == text[start:end].

## Method
1 offsets/values/overlaps; 2 world scan (552 persons: names, emails, phones, MRNs, streets, postcodes, subject ids,
rand nos, ISO DOBs; case-insensitive, wrap-tolerant) for occurrences outside spans; 3 pattern scan (year tokens,
capitalized words, honorifics) + inline-label read-through of every doc (repeated filler stripped); 4 world
cross-check: staff/sponsor spans belong to the doc's site with role matching job (CRA staff, sponsor contact
sponsor); patient ids/rand/initials resolve to world_refs subjects incl. OCR-damaged values; every DOB/event date
is a real date of a listed subject (except d0468, J2); table rows: date belongs to the row's subject (201 rows),
CRF initials match (111 rows); 5 category/role conventions; 6 pii_depth single compact block in band; D-015 tag
consistency; invariant 10. Units spot-check skipped (no data/units yet).

## Per-doc verdicts
d0032 conmed clean OK(J1) | d0034 narrative de 12/3 OK | d0035 protocol 0/12 OK | d0047 deviation 64/2 OK |
d0071 protocol 0/10 OK | d0073 lab 5/11 OK | d0076 deviation 60/5 OK | d0091 correspondence es 13/1 OK |
d0095 sae 6/7 OK | d0100 protocol 0/1 OK | d0124 crf 160/2 OK | d0164 deviation 98/5 OK | d0191 delegation 12/16
OK(J4) | d0192 correspondence 3/1 OK (depth early 10.4-10.7%) | d0197 delegation clean OK | d0208 narrative 4/24 OK
(depth middle 50.4-50.6%) | d0223 delegation 12/5 OK | d0299 protocol 0/14 OK | d0331 deviation 86/2 OK | d0347 lab
6/1 OK | d0366 crf 176/2 OK | d0433 delegation 12/13 OK | d0468 sae de 5/5 OK as label (J2, J3) | d0485 icf 4/2 OK
| d0531 icf de 4/4 OK (J3) | d0538 monitoring clean 0/10 OK (J1, J4, J5) | d0560 narrative 4/12 OK (depth early
11.0-11.3%) | d0564 protocol 0/1 OK | d0588 correspondence 11/1 OK (J1) | d0593 sae 4/5 OK.

## Judgment calls / generator-level concerns (no label changes)
J1 world_refs.subjects lists subjects whose data never appears (87 zero-span docs list subjects); conservative
for the M5 split; document meaning or trim.
J2 SAE view invents an AE when the subject has none (14/60 SAE forms), breaking generator.md cross-doc
consistency; safe_date doesn't exclude invented AE dates (0 collisions found in corpus).
J3 document dates ignore event order: 24 SAE reports dated before onset; 11/18 ICF pages signed before version date.
J4 eponym injector ignores sentence context ("renal function uses the Hodgkin formula").
J5 neutral placeholders distinctive/ungrammatical ("[name]", "Subject [not stated]", "(visit on a recent visit)",
"Residence: not recorded .") appear only in PII-absent/masked views: possible shortcut for arm C.
J6 de/es docs carry English filler sections and English AE terms: language cue correlated with PII blocks.
J7 ages <= 89 unlabeled even with sex/history (per convention; correct as specified).
J8 "Northvale" is both the CRO domain and a site institution.
J9 invariant 10 OK (fictional sponsor/compound/NCT99/EudraCT 2031/example domains; CAS invalid check digit;
MedDRA-like codes random, low risk; Faker names; generic boilerplate).
J10 conventions applied consistently (consent date phi_quasi; correspondence dates non_phi_date; CRA staff;
sponsor CTM sponsor; middle_x initials resolve; staff identity consistent across docs).
