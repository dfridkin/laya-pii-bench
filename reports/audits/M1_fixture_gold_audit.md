# M1 fixture gold audit (gold-auditor subagent), 2026-09-26

Sample: n=10 (all docs), fx01..fx10 in fixtures/mini/docs.jsonl (as of commit 1016ec7)
Errors: 0
Verdict: CLEAN, zero label errors.

## How checked
- Offsets: every span/negative dumped with `text[start:end]` and neighbouring chars; all start and
  end on a delimiter (space, newline, punctuation, `<`/`>`, `(`); no partial-word cuts.
- `uv run pytest tests/test_fixture.py`: 14 passed (incl. fx06 token-256 straddle check).
- No units exist for the fixture yet; unit spot-check not applicable. No files edited.

## Per-doc verdicts
| doc | type | spans / negs | verdict |
|---|---|---|---|
| fx01 | csr_patient_narrative | 14 / 0 | CLEAN. Name, initials, DOB, MRN, 3 event dates, rand no, address, ZIP, phone, "Ms. Kowalczyk", "Dr. Samuel Okafor" covered. Age 64 correctly unlabeled; initials and DOB consistent. |
| fx02 | protocol_section | 0 / 0 | CLEAN. No PII; "medical monitor"/"investigator" generic. |
| fx03 | delegation_log | 12 / 0 | CLEAN. 4 staff: name, initials, contact all labeled. Site name correctly unlabeled. |
| fx04 | crf_page | 3 / 0 | CLEAN. 3 subject IDs, coded_id/patient. "Visit 3" not a date. |
| fx05 | site_correspondence | 13 / 0 | CLEAN. Every mention of Priya/Tom (full, greeting first names, sign-offs, quote, email, phone) and all 3 subject IDs labeled. "Tue, 12 Aug 2025" correspondence date correctly unlabeled. |
| fx06 | monitoring_visit_report | 4 / 0 | CLEAN. 3 staff names + patient address (phi_direct/patient). Later generic role mentions fine. |
| fx07 | protocol_section | 0 / 13 | CLEAN. Protocol no, NCT, EudraCT, 2 non-PHI dates, 4 eponyms, compound code, lot, kit, visit window. |
| fx08 | lab_report | 3 / 0 | CLEAN. Subject ID, OCR-noisy MRN (phi_direct), collection date (phi_quasi). OCR noise outside spans not PII. |
| fx09 | sae_cioms | 0 / 6 | CLEAN. 4 redaction placeholders, compound code, report version date as negatives. Age 58/sex/country correctly unlabeled. |
| fx10 | csr_patient_narrative (de) | 8 / 0 | CLEAN. Subject ID, name, DOB, address, 2 event dates, investigator, "Herr Hoffmeister". "Tag 53" consistent (12.05 + 52 d = 03.07). Hospital name not PII. |

## Invariant 10
Fictional sponsor/compound/protocol codes; `.example.org`/`.example.com` emails; 555 phones; generic
boilerplate, not real protocol text. Caveat: judgment call 6.

## Judgment calls (policy ambiguous, not errors)
1. fx03 staff initials labeled staff_pii; domain.md says "name + contact" only. Sensible; record in spec
   so generated delegation logs match.
2. fx01 address (phi_direct) and ZIP (phi_quasi) are separate spans. Generator should split the same way.
3. Tom Becker (CRA at a CRO) labeled role=staff per domain.md; a CRO monitor could arguably be
   role=sponsor (maps to none), changing subject_role gold. Worth one spec line.
4. fx09 "**-***-2025" leaves year (non-PII, fine); report version date labeled non_phi_date on a
   single-patient SAE follow-up is arguable but spec-consistent.
5. fx10 relative timing ("Tag 53", "nach neun Tagen entlassen") implies discharge date; spec silent.
6. fx07 NCT09990421 valid format, above today's issued range (~NCT07xxxxxx) but could be issued in future.
   EudraCT 2031-... safely fictional. Low risk.
7. fx05 "Query 2291" could be a `query_no` hard negative. Not an error.
8. fx08 OCR MRN uses Z<->2, not in generator.md's list (l<->1, O<->0, drops). Harmless for fixture.

## Text-quality nit
fx10 "Der Prüfarzt, Dr. med. Katrin Albers" should be "Die Prüfärztin" (female investigator).
