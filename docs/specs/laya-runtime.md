# Spec: Laya runtime (`bench/laya_client.py`, `bench/questions.py`)

Facts verified from the model card (huggingface.co/convaiinnovations/laya, laya 0.3.20, Sept 2026).
Re-check the card when upgrading `laya`.

## Checkpoints

| Name | Load | Backbone | Context |
|---|---|---|---|
| english | `laya.load("convaiinnovations/laya")` | ModernBERT-large, 421M | 512 (head_max_len 192) |
| multilingual | `laya.load("convaiinnovations/laya", subfolder="multilingual")` | mmBERT-base, 322M | 1024 default, up to 8192 via `max_len` |

Router usage for long docs:
```python
router.predict(state, questions, model="multilingual", max_len=8192)
```
Always name `model="multilingual"` for long mostly-English text, or the Router picks English.
Published accuracy degrades past ~4k tokens; measure, don't assume.

## Question shapes

```python
{"type": "choice", "instructions": "...", "criteria": {"A": "desc", "B": "desc"}}
{"type": "score", "instructions": "...", "criteria": ["low", "mid", "high"]}
{"type": "noul", "instructions": "..."}   # DO NOT USE on English checkpoint (D-006)
```

All questions in one call are answered in a single forward pass. Results:
`result["answers"][key]["choice"]`, probabilities per option, `confidence`.
Record the full probability dict per option (write a small adapter; the exact result keys are
whatever the installed laya version returns: inspect once in M0 and pin in a test).

## Known limits that shape the design

- Base checkpoints are near chance zero-shot on the typed-decisions benchmark; fine-tuning is where
  accuracy comes from (arm C).
- Ships over-confident: fit one temperature per (question, option count) on calib.
- `action.act_probability` has no usable signal; gate on `confidence`.
- Many options per question dilute the head budget; keep ≤ 10 options. qs_v2 splits multi-label
  into two-option questions for this reason.
- `laya.load()` can hang if TensorFlow is installed: run with `USE_TF=0`.

## Device

Order: cuda → mps → cpu. Record the chosen device and torch version in `hw.json`. If mps errors on
an op, fall back to cpu and record the fallback. ONNX Runtime (`laya[onnx]`) is an optional later
arm for CPU latency, not a replacement.

## Timing protocol

1. Preload the checkpoint(s) used by the arm (`Router(preload=True)` or `laya.load`).
2. Warmup: `warmup_calls` (default 10) on fixture units; mark `warmup=true`, excluded from metrics.
3. Measure each call with `time.perf_counter_ns()` around `predict` only (not tokenization done
   by our code, not I/O).
4. Batch-1 mode is the headline. Batched mode (if the installed API supports batching states)
   is reported separately.
