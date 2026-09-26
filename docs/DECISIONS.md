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
| D-005 | Split key | DECIDED | Group by `world_refs.site`; 55/15/20 train/calib/test + 10% holdout doc type (IRB letters) | |
| D-006 | Binary questions on English checkpoint | DECIDED | Two-option `choice` with neutral keys `A`/`B`, never `noul` | |
| D-007 | Headline operating point | DECIDED (provisional value) | `t_low` fit on calib for ≥0.995 `pii_present` recall | Rescore only |
| D-008 | Dataset size | DECIDED | 600 docs. Scale to 1,000+ if test recall CI half-width > 0.01 | Rerun gen onward |
| D-009 | Gold labeling mechanism | DECIDED | Sentinel renderer; offsets recorded at resolve time | |
| D-010 | Fictional world | DECIDED | Sponsor "Fenwick Therapeutics", compound prefix `FTX-`; all persons Faker-generated | |
| D-011 | Paraphrase pass | DEFERRED | Off. Revisit only if zero-shot results look template-trivial (M6 review) | |
| D-012 | Fine-tune arm C | DECIDED | Adapt Laya's Kaggle fine-tune notebook; train split only | |
| D-013 | `CalibParams.fit_on` for the fixture (no calib split exists) | OPEN | Provisional: allow `fit_on: fixture_debug`, produced only by `bench calibrate --debug-fit-all` and accepted by `bench score` only with `--allow-debug-calib`; report prints a DEBUG banner. When `bench split` lands (M5), both flags must refuse non-fixture inputs or be removed | Remove the literal and the flags; fixture reports then need another honest label |
| D-014 | Which confidence invariant 6 means for choice questions: laya `confidence` (1 - normalized entropy) or `answer_confidence` (max p, what temperature scaling fits) | OPEN | Provisional: routing gates on calibrated p(pii_present = A) per PLAN; ECE/AUROC use max p; laya `confidence` is stored in decisions but unused by metrics | Rescore only |

## Log

Append entries as `YYYY-MM-DD D-nnn: <change> (by <who>)`.

- 2026-09-25 D-001..D-012 created from planning conversation (by Dmitriy + Claude).
- 2026-09-26 Fixture lock: one-time exception to add `fixtures/mini/decisions_mock.jsonl` for M2 (owner approved in session). `.locks/fixtures` removed and recreated around that single new file; `fixtures/mini/src/` and `docs.jsonl` unchanged (by Dmitriy + Claude).
- 2026-09-26 D-013, D-014 opened (M2 gate review #1): fit_on widening recorded; confidence definition question surfaced (by Claude, pending owner).
