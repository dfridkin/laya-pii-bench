# Plan

## Goal

Measure how accurately and how fast the open-weight Laya model classifies whether a document unit
contains PII/PHI, on synthetic clinical-trial documentation, and at what operating point it could
safely forward clean units without extraction.

## Process

```
Generate → Label → Split → (Fine-tune, arm C only) → Run arms → Calibrate → Score → Report + HUD
```

Zero-shot arms skip fine-tuning and read the split directly.

## Arms (`config/arms.yaml`)

| Arm | Checkpoint | Unit | max_len |
|---|---|---|---|
| A | laya (English) | 256-token chunk, 32 overlap | 512 |
| B1 | laya-multilingual | 768-token chunk | 1024 |
| B2 | laya-multilingual | ~2k section | 2048 |
| B3 | laya-multilingual | ~4k section / short doc | 4096 |
| B4 | laya-multilingual | whole doc | 8192 |
| C | laya fine-tuned (train split) | 256-token chunk | 512 |

Each arm runs both question sets (`qs_v1`, `qs_v2`) and is scored raw and temperature-calibrated.

## Question sets

- `qs_v1`: 4 questions in one pass: `pii_present`, `subject_role`, `category` (precedence-flattened),
  `doc_kind`.
- `qs_v2`: `pii_present` + 5 per-category two-option choices (multi-label).

## Routing (score stage, not runner)

- p(pii) < `t_low` and role ≠ patient → FORWARD
- p(pii) ≥ `t_high` or role = patient → REDACT
- otherwise → ESCALATE

`t_low` fit on calib for ≥ 0.995 recall. `t_high` fit on calib for ≥ 0.98 precision.

## Dataset

600 synthetic documents, 12 doc types, 4 languages, 4 length buckets, ~25% hard negatives,
60 sparse long docs with controlled PII depth. Splits grouped by site.

## Headline result

At the calib-fit `t_low`: test recall on `pii_present` (with bootstrap CI), forward rate, count of
false forwards, p50 latency per unit and per document, on labeled hardware.

## Out of scope

Span extraction, redaction quality, end-to-end LLM forwarding, real documents.
