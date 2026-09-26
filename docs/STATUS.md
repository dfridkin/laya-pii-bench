# Status

Active milestone: **M1 Contracts + fixture**
Last updated: 2026-09-25 (M0 gate passed)

| Milestone | State | Gate passed | Notes |
|---|---|---|---|
| M0 Bootstrap | done | 2026-09-25 (`reports/audits/M0-gate-20260925-2255.md`) | mps, p50 67.8 ms |
| M1 Contracts + fixture | not started | | |
| M2 Scorer + report on fixture | not started | | |
| M3 Runner, arm A on fixture | not started | | |
| M4 Generator | not started | | |
| M5 Label + split | not started | | |
| M6 Zero-shot arms, calibrate, score, report v1 | not started | | |
| M7 HUD replay | not started | | |
| M8 Fine-tuned arm C, report v2 | not started | | |

## Provisional defaults in use

- D-001 coded IDs counted as PII.
- D-002 dev hardware only.

## M0 evidence

- Hardware (`hw.json`): Apple M2, 8.0 GB RAM, macOS Darwin 24.3.0, arm64, Python 3.12.8,
  torch 2.14.0, laya 0.3.20, **device: mps**.
- Checkpoint: `convaiinnovations/laya@55cf4c4ebb4ebe31b2550e8bdf3bd21b99753851` (english and
  multilingual, pinned in `models.lock.json`).
- `scripts/laya_smoke.py` (english, 1 two-option choice question, max_len 512, head_max_len 192,
  20 calls, first 5 dropped, batch-1): answer `A`, probabilities `{A: 0.8575, B: 0.1425}`,
  sum 1.0000, **p50 67.8 ms**, p95 70.6 ms, load 29.8 s.

## Later (out of M0 scope, noted for the owning milestone)

- M3: laya 0.3.20 rounds `probabilities` to 4 dp in `_decode_answers`. Invariant 4 stores "raw"
  probabilities; decide whether 4 dp is enough for calibration/ECE or whether to read logits.
- M3: for `choice`, laya's `confidence` is normalized entropy and `answer_confidence` is max(p)
  (the quantity temperature scaling fits). Invariant 6 says gate on `confidence`; confirm which
  one the router gates on before building `score` routing. Store both.
- M3: checkpoint warns `choice:11+` temperature out of range (clamped to 0.5). Irrelevant while
  every question has <= 10 options; keep it that way.
- M3: `models.lock.json` stores absolute HF cache paths (one machine). Resolve path at load time
  from repo + revision instead (download_models.py writes it; fix there, not by hand).
- M3: runner warmup follows spec default (10 calls on fixture units), not the M0 smoke's 5.
- M6/B4: dev box has 8 GB RAM; 8192-token multilingual runs may be memory-bound on MPS.

## Next action

Run `/milestone M1`.

## Session log

Append one line per session: `YYYY-MM-DD M<n>: what moved, what's blocked`.

- 2026-09-25 M0: hw fingerprint, bench hw, laya_smoke (mps p50 67.8 ms); gate PASS (independent review).
