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

## Log

Append entries as `YYYY-MM-DD D-nnn: <change> (by <who>)`.

- 2026-09-25 D-001..D-012 created from planning conversation (by Dmitriy + Claude).
