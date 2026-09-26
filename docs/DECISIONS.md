# Decisions

Status values: DECIDED, OPEN (provisional default in use), SUPERSEDED.
Claude Code: never change a DECIDED entry without the owner's explicit instruction. Resolve OPEN
entries only via `/decide`.

| ID | Topic | Status | Decision | Consequence if changed |
|---|---|---|---|---|
| D-001 | Coded subject IDs (`1001-0023`, randomization nos.) count toward `pii_present`? | OPEN | Provisional: **yes** (`policy.coded_id_is_pii: true`), recall-first | Rerun `label` onward. Generator unaffected. |
| D-002 | Target hardware for headline latency | OPEN | Provisional: dev on Apple Silicon (MPS, fall back CPU). Report labels hardware; no cross-hardware claims | Rerun `run` for timing only; accuracy unaffected |
| D-003 | Stack | DECIDED | Python 3.12 + uv for pipeline; TypeScript + Vite single-file HUD | |
| D-004 | Scope | DECIDED | Classifier accuracy only. No extractor, no redaction step | |
| D-005 | Split key | DECIDED (amended 2026-09-26) | Holdout = all IRB letters (30 docs, 5%), regardless of site; IRB letters name no subjects. Remaining docs: site-level docs grouped by site (`study/site` key, B3), sponsor-level docs (no site, no subjects, e.g. protocol sections) each their own group; groups stratified 55/15/20 train/calib/test so every split gets every doc type. No site or subject in more than one of train/calib/test. Holdout is a descriptive generalization check, never in the headline | Rerun split onward |
| D-006 | Binary questions on English checkpoint | DECIDED | Two-option `choice` with neutral keys `A`/`B`, never `noul` | |
| D-007 | Headline operating point | DECIDED (provisional value) | `t_low` fit on calib for ≥0.995 `pii_present` recall | Rescore only |
| D-008 | Dataset size | DECIDED | 600 docs. Scale to 1,000+ if test recall CI half-width > 0.01 | Rerun gen onward |
| D-009 | Gold labeling mechanism | DECIDED | Sentinel renderer; offsets recorded at resolve time | |
| D-010 | Fictional world | DECIDED | Sponsor "Fenwick Therapeutics", compound prefix `FTX-`; all persons Faker-generated | |
| D-011 | Paraphrase pass | DEFERRED | Off. Revisit only if zero-shot results look template-trivial (M6 review) | |
| D-012 | Fine-tune arm C | DECIDED | Adapt Laya's Kaggle fine-tune notebook; train split only | |
| D-013 | `CalibParams.fit_on` for the fixture (no calib split exists) | DECIDED | Allow `fit_on: fixture_debug`, produced only by `bench calibrate --debug-fit-all` and accepted by `bench score` only with `--allow-debug-calib`; report prints a DEBUG banner. `--allow-no-meta` (meta-less decisions) is accepted only with a fixture_debug calib. When `bench split` lands (M5), these flags must refuse non-fixture inputs or be removed | Remove the literal and the flags; fixture reports then need another honest label |
| D-014 | Which confidence invariant 6 means for choice questions: laya `confidence` (1 - normalized entropy) or `answer_confidence` (max p, what temperature scaling fits) | OPEN | Provisional: routing gates on calibrated p(pii_present = A) per PLAN; ECE/AUROC use max p; laya `confidence` is stored in decisions but unused by metrics | Rescore only |
| D-015 | Generator document plan (audit B2) | DECIDED | ~30% of docs PII-free at doc level (70 protocol sections + ~20% of site-level docs rendered without person data); `hard_negative` tag = docs chosen by the hard-negative injector (25%), header/footer identifiers are labeled negatives but don't set the tag; de/es/pl only for site-facing types (narrative, SAE, site correspondence, ICF, lab), exact counts 24/18/18; long/XL only for prose types (protocol, narrative, monitoring report, site correspondence), forms and logs short/medium; the 60 pii_depth docs come from long/XL prose docs. Encoded as a per-type `doc_plan` block in gen_spec.yaml (drafted in M4a for owner review) | Rerun gen onward |
| D-016 | Contract details for M4/M5 (audit B3) | DECIDED | `Span.value: str \| None` (generator always fills it; validate checks `text[start:end] == value` when present; fixture stays valid). Split group key = `world_refs.study + "/" + world_refs.site`; generator keeps site numbers unique within a study | Types change first; rerun gen onward |
| D-017 | Sponsor/CRO persons (audit B4; also the CRA-role question) | DECIDED | Sponsor-role spans are `staff_pii` and count as PII; `policy.role_map.sponsor = staff`, so their subject_role answer is `staff` (qs_v1: "monitors, or other site staff"). CRAs stay role `staff` | Rerun label onward |
| D-018 | Staff identity across splits (audit B5) | DECIDED | Each staff person belongs to exactly one site in the world model (no CRA across sites, no PI across studies); M5 gate 1 also checks staff person ids across train/calib/test. Holdout IRB letters may name their site's PI; report a caveat that arm C may have seen those names | Rerun gen onward |

## Log

Append entries as `YYYY-MM-DD D-nnn: <change> (by <who>)`.

- 2026-09-25 D-001..D-012 created from planning conversation (by Dmitriy + Claude).
- 2026-09-26 Fixture lock: one-time exception to add `fixtures/mini/decisions_mock.jsonl` for M2 (owner approved in session). `.locks/fixtures` removed and recreated around that single new file; `fixtures/mini/src/` and `docs.jsonl` unchanged (by Dmitriy + Claude).
- 2026-09-26 D-013, D-014 opened (M2 gate review #1): fit_on widening recorded; confidence definition question surfaced (by Claude, pending owner).
- 2026-09-26 D-005 amended (audit B1): sponsor-level docs grouped per doc and stratified; holdout = all 30 IRB letters (5%, was stated as 10%), exempt from site grouping, no subjects in IRB letters; M5 gates 1-2 apply to train/calib/test, holdout class counts reported (by Dmitriy).
- 2026-09-26 D-015 decided (audit B2): generator document plan (by Dmitriy).
- 2026-09-26 D-016, D-017, D-018 decided (audit B3-B5); policy.role_map.sponsor none -> staff (by Dmitriy).
- 2026-09-26 D-013 provisional text extended: `--allow-no-meta` tied to fixture_debug calib (fix-batch review 2 follow-up; by Claude, pending owner).
- 2026-09-26 D-013 confirmed as written, incl. `--allow-no-meta` only with a fixture_debug calib; OPEN -> DECIDED (by Dmitriy).
