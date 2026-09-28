# laya-pii-bench

Benchmark of the open-weight Laya decision model (Convai Innovations, Apache 2.0) as a local PII
**classifier** on synthetic pharma clinical-trial documents. Classifier accuracy only: no span
extraction, no redaction. Route decisions (forward / redact / escalate) are computed from stored
probabilities so the HUD and forward-rate metric can use them.

Owner: Dmitriy Fridkin. Python 3.12 pipeline (uv), TypeScript HUD (Vite, single-file build).

## Read first, every session

1. `docs/STATUS.md` : current milestone, what's done, what's next. Source of truth for progress.
2. `docs/MILESTONES.md` : scope and acceptance gate for each milestone. Work only inside the active one.
3. `docs/DECISIONS.md` : decided and open decisions. Never silently resolve an OPEN one.
4. The spec in `docs/specs/` for whatever you are touching.

## Commands

```bash
make bootstrap        # one-time: uv sync, model download, hw fingerprint
make check            # ruff + pyright + pytest (must pass before any commit)
make fixture          # validate hand-labeled fixture docs
make gen label split  # data stages
make run ARM=A QS=qs_v1
make calibrate score report
make pipeline         # full end to end, all arms in config/arms.yaml
make smoke            # 20-doc end-to-end run on arm A, minutes not hours
make hud              # build HUD from latest replay
uv run bench --help   # every stage is a subcommand of one Typer CLI
```

Always run Python through `uv run`. Set `USE_TF=0` (already in Makefile and settings env) or
`laya.load()` can hang on TensorFlow import.

## Architecture (stage contracts)

Every stage reads files and writes files. No stage calls another stage in-process.

| Stage | Reads | Writes |
|---|---|---|
| gen | config/gen_spec.yaml, templates | data/docs.jsonl, data/gen_manifest.json |
| label | docs, config/policy.yaml, config/arms.yaml | data/units/{arm}.jsonl |
| split | docs | data/splits.json |
| run | units, splits, arm, question set | runs/{arm}/{qs}/decisions.jsonl + meta.json (`{qs}__batch{n}` for batched) |
| calibrate | calib-split decisions, units | calib/{arm}__{qs}.json (hashed, frozen; records input hashes + calib doc ids) |
| score | test-split decisions + frozen calib, units, docs, run meta | scores/{arm}__{qs}.json |
| report | scores, decisions | reports/report.md, hud/public/replay.json |

Named datasets other than `data/docs.jsonl` (e.g. the fixture, `--docs fixtures/mini/docs.jsonl`)
are namespaced: `data/{name}/units/`, `runs/{name}/{arm}/{qs}` (`bench/paths.py`).

Domain types live in `bench/domain.py` (pydantic v2). JSON Schema exported to `schema/` and
converted to TS types for the HUD. Change a type there first, then everything downstream.

## Invariants (a violation is a bug, not a style issue)

1. **Gold spans come only from the sentinel renderer.** Never locate PII by searching the rendered
   text. See `docs/specs/generator.md`.
2. **Split by site** (`study/site`), never by chunk or unit. No subject or staff person in two of
   train/calib/test. Sponsor-level docs (no site, no subjects) are grouped per document; all IRB
   letters are the holdout (D-005, D-016, D-018).
3. **Test split is sealed** until the score stage. Temperatures and thresholds are fit on calib
   only, written to `calib/`, hashed, and the hash is checked by `score`.
4. **Runner stores raw probabilities.** Routing and thresholds are applied in `score`, so thresholds
   can be re-swept without re-running inference.
5. **No `noul` questions on the English checkpoint.** Use two-option `choice` with neutral keys
   `A`/`B` (known label-following bug). See `docs/specs/laya-runtime.md`.
6. **Gate on calibrated probability, never `action.act_probability`** (no signal in current release).
   Routing thresholds apply to calibrated p(pii_present = A); calibration metrics use the top
   probability (laya `answer_confidence`). laya's entropy `confidence` is stored, never gated on (D-014).
7. **Truncation is never silent.** Count tokens with each checkpoint's own tokenizer; a unit over
   budget is flagged `truncated=true` and reported as its own slice.
8. **Multilingual long context:** always pass `model="multilingual"` and an explicit `max_len`.
9. **Timing is honest:** preload checkpoints, discard warmup calls, report batch-1 and batched
   separately, attach `hw.json` fingerprint to every run.
10. **Fictional world only.** Sponsor, compound codes, sites, and people are synthetic. No real
    protocol text, investigator names, or compound codes.
11. **Generated artifacts are never hand-edited** (`data/`, `runs/`, `calib/`, `scores/`). A hook
    blocks it. Fix the generator or stage and rerun.
12. **Determinism:** every stochastic step takes a seed from config; same seed, same bytes.

## Working rules

- Plan backwards from the milestone gate: write the acceptance test first, then the code that
  satisfies it.
- Domain model first. New concepts get a pydantic type before they get logic.
- Keep modules small and typed. `pyright` strict on `bench/`.
- Tests: pytest, `tests/` mirrors `bench/`. Property tests (hypothesis) for the renderer, span
  remap, and metrics.
- Commit at the end of each milestone step with message `M<n>: <what>`; update `docs/STATUS.md`
  in the same commit.
- When a gate needs a decision marked OPEN in `docs/DECISIONS.md`, stop and ask. Use the provisional
  default only for code that is cheap to redo, and say so in STATUS.
- Long jobs (`run`, `gen` at full size): run in the background and poll the log; don't block the
  session.
- Prefer delegating read-heavy review to the subagents in `.claude/agents/`.

## Anti-patterns

- Labeling spans by string search after rendering.
- Fitting thresholds or temperatures on test, or peeking at test metrics to pick an arm.
- Splitting by chunk (leaks the same patient across splits and inflates fine-tuned scores).
- Routing inside the runner.
- Measuring latency on the first call or with lazy checkpoint loading.
- LLM-generated documents labeled by an LLM (circular gold).
- "Fixing" a failing validator by loosening it without a DECISIONS.md entry.

## Workflow shortcuts

- `/progress` : where are we (`/status` is a built-in Claude Code command)
- `/milestone M<n>` : execute a milestone to its gate
- `/gate M<n>` : independent acceptance review
- `/decide D-<nnn> <answer>` : record a decision and apply its consequences
- `/pipeline smoke|full` : run the pipeline and summarize
