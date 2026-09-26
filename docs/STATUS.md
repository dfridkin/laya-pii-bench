# Status

Active milestone: **M2 Scorer + report on fixture**
Last updated: 2026-09-26 (M2 built, gate review pending)

| Milestone | State | Gate passed | Notes |
|---|---|---|---|
| M0 Bootstrap | done | 2026-09-25 (`reports/audits/M0-gate-20260925-2255.md`) | mps, p50 67.8 ms |
| M1 Contracts + fixture | done | 2026-09-26 (`reports/audits/M1-gate-20260926.md`) | fixture locked; gold audit 0 errors |
| M2 Scorer + report on fixture | built, gate review pending | | golden metrics exact; hash check exits 2 |
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

## M1 evidence

- `make check`: 104 passed, 2 skipped (model-marked); coverage domain 100%, config 100%, validate 99%
  (per-file >= 90% enforced in `make test`).
- `make fixture`: 10/10 valid. `make schema && git diff --exit-code`: no diff.
- Model-marked tests (`LAYA_SKIP_MODEL=0 USE_TF=0 uv run pytest -m model`): 2 passed, incl. fx06 address
  span on English tokens 245-262 (straddles the 256-token chunk boundary).
- Gold audit of all 10 fixture docs: 0 label errors (`reports/audits/M1_fixture_gold_audit.md`).
- `.locks/fixtures` created after the gate.

Deviations from the scaffold (accepted by gate review):
- `make schema` exports one combined `schema/domain.json`; the old glob input made json2ts write a
  directory instead of `hud/src/types.gen.ts`.
- Fixture gold is inline sentinel markup in `fixtures/mini/src/*.yaml`, resolved left to right by
  `bench/markup.py` (`bench build-fixture`); never located by string search.
- `Scores` deferred to M2 per `docs/specs/domain.md` (MILESTONES lists it under M1).
- `config/questions/qs_v2.yaml`: quoted `yes`/`no` criteria (YAML parsed them as booleans).
- `HwInfo` moved into `bench/domain.py`; `RunMeta.hw` is typed `HwInfo` instead of `dict`.
- Validator also rejects span/negative edges that cut inside a word (gate finding 3).

## M2 evidence

- `make check`: 146 passed, 3 skipped (model-marked; `-m model`: 3 passed). Golden metric tests
  (`tests/test_metrics_golden.py`) pass at tolerance 1e-9 against hand arithmetic on the mock
  decisions (identity calibration, t_low 0.25, t_high 0.85): accuracy 8/11, confusion [[6,2],[1,2]],
  macro-F1 (12/15 + 4/7)/2, ECE 3.08/11, Brier, AUROC 19/24, recall 7/8, forward rate 2/11,
  1 false forward (fx06 chunk 1, missed `address`). Temperature fit golden: T = 2 exactly.
- Gate 2: `bench label` (fixture, arm A, 11 units) -> `bench calibrate --debug-fit-all` ->
  `bench score --allow-debug-calib` -> `bench report` writes `reports/fixture/report.md` with all
  9 metrics.md sections (test asserts the headings against the spec).
- Gate 3: score with a calib file whose `t_low` was edited exits 2 ("content hash mismatch") and
  writes no scores (manual run + test).
- One-time fixture unlock to add `fixtures/mini/decisions_mock.jsonl` (owner approved; logged in
  DECISIONS.md); lock recreated in the same commit.

Interpretations made in M2 (cheap to change; flag if you disagree):
- Routing: predicted role `both` forces REDACT like `patient` (PLAN says "role = patient"; `both`
  includes patient data). qs_v2 has no role question, so routing there is threshold-only.
- `category` gold uses only categories counted as PII; `categories_multi` is raw presence. Only
  differs if D-001 flips to "no".
- Temperature scaling acts on log of laya's 4-dp probabilities (zeros clipped to 1e-6).
- `t_high`: smallest observed p reaching the precision target; 1.0 if unreachable; never < t_low.
- Macro-F1 averages over labels present in gold or predictions; majority baseline is computed on
  the scored set; ECE/AUROC use max probability (laya's entropy `confidence` is stored, not used).
- `CalibParams.fit_on` gained `fixture_debug`; `score` refuses it without `--allow-debug-calib`,
  and the report prints a DEBUG banner.
- Until `bench split` exists (M5): `calibrate` only runs with `--debug-fit-all`, and `score` treats
  every document as split `fixture`. Units are written to `<out>/{arm}.jsonl`.

## Questions for the owner (not blocking; candidates for DECISIONS entries)

- Staff initials (fx03) labeled `staff_pii`; domain.md says "name + contact". Confirm for the generator.
- CRO monitor (CRA) labeled role `staff` per domain.md; if CRO/sponsor staff should be `sponsor` (maps to
  subject_role none), gold changes.
- Relative timing ("Day 53", "discharged after nine days") left unlabeled; spec is silent.
- Sponsor-level docs (protocol sections) have no site; fixture uses `site: SPONSOR`. M5 split needs a rule
  for them (they'd all land in one group).
- `config/arms.yaml` B2: `target_tokens: 1800` exceeds the state budget 2048-256 = 1792, so full-size
  sections would be flagged truncated. Lower to <= 1792 or accept.

## Later (out of current scope, noted for the owning milestone)

- M5: `bench split` + split-aware `calibrate`/`score` (calib-only fit, test/holdout scoring); section
  and doc units in `label`. Makefile `calibrate`/`score` targets (`--all`) need that too.
- M6: bootstrap CIs are percentile intervals on document resamples; forward rate and recall only.
- M7: `bench report --hud` currently prints a note and writes nothing.

- M2/M3: fx06 boundary check assumes raw-text English tokens without special tokens; the M2 segmenter
  must count the same way, or re-tune fx06 (needs an owner OK: fixtures are locked).
- M3: re-run model-marked tests (fx06 boundary, laya result shape) whenever laya or the tokenizer changes.
- M4: `Document.gen_meta` allows `list[str]` only; section offsets (`gen_meta.sections`) need `list[int]`.
- M4: generator OCR substitutions (l/1, O/0, drops) don't include Z/2 as used in fx08; extend or accept.
- M4: NCT ids like NCT0999xxxx are above today's issued range but could be issued later; consider a
  clearly invalid prefix. EudraCT uses year 2031 (safe).
- `bench build-fixture` writes via Bash, so the Edit/Write lock hook doesn't block it; output is fully
  determined by the locked sources.
- `bench/validate.py` doc_kind_map branch is unreachable (Policy validator guarantees completeness).

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

Run `/gate M2`, then close out M2.

## Session log

Append one line per session: `YYYY-MM-DD M<n>: what moved, what's blocked`.

- 2026-09-25 M0: hw fingerprint, bench hw, laya_smoke (mps p50 67.8 ms); gate PASS (independent review).
- 2026-09-26 M1: domain, config, validate, schema, 10-doc fixture; gate PASS, gold audit 0 errors; fixtures locked.
