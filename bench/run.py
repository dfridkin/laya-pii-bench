"""Run stage: one arm x question set over units, append-only and resumable.

Writes `decisions.jsonl` (one `Decision` per unit, raw probabilities, no routing: invariant 4) and
`meta.json` (`RunMeta`) into the run directory. Timing protocol (invariant 9): the checkpoint is
loaded before any timed call, `warmup_calls` warmup calls on fixture text are recorded with
`warmup=true`, and only `predict` is inside the timer. A rerun skips units already decided; when
nothing is left it makes no laya calls and doesn't load the checkpoint.
"""

from __future__ import annotations

import os
import time
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Literal

from pydantic import ValidationError

from bench.domain import Decision, Device, HwInfo, QuestionSet, RunMeta, Unit
from bench.laya_client import LayaLike, to_answers

Log = Callable[[str], None]


class RunError(RuntimeError):
    pass


@dataclass(frozen=True)
class RunSpec:
    arm: str
    qs: QuestionSet
    questions: Mapping[str, Mapping[str, Any]]  # laya question dicts, from bench.questions.build
    checkpoint: str
    max_len: int
    dataset: str
    out_dir: Path
    batch_size: int
    warmup_calls: int
    config_hashes: Mapping[str, str]


def read_existing(path: Path) -> list[Decision]:
    if not path.exists():
        return []
    out: list[Decision] = []
    with path.open(encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            if not line.strip():
                continue
            try:
                out.append(Decision.model_validate_json(line))
            except ValidationError as e:
                raise RunError(
                    f"{path}:{lineno} is not a valid Decision (torn write?). Move the run "
                    "directory aside and rerun; decisions are never edited in place."
                ) from e
    return out


def _now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def _check_resume(prev: RunMeta, spec: RunSpec) -> None:
    mine = {"arm": spec.arm, "qs": spec.qs.id, "batch_size": spec.batch_size}
    theirs = {"arm": prev.arm, "qs": prev.qs, "batch_size": prev.batch_size}
    if mine != theirs or dict(spec.config_hashes) != prev.config_hashes:
        changed = sorted(
            k for k in set(spec.config_hashes) | set(prev.config_hashes)
            if spec.config_hashes.get(k) != prev.config_hashes.get(k)
        )  # fmt: skip
        raise RunError(
            f"{spec.out_dir} was produced with different settings ({mine} vs {theirs}; changed "
            f"hashes: {changed}). Use a fresh run directory."
        )


def _check_same_machine(prev: HwInfo, now: HwInfo) -> None:
    """Refuse to resume on a different machine, runtime or checkpoint set (invariant 9)."""
    a, b = prev.model_dump(exclude={"created_at"}), now.model_dump(exclude={"created_at"})
    changed = sorted(k for k in a if a[k] != b[k])
    if changed:
        raise RunError(
            f"hardware/runtime fingerprint changed since the run started ({changed}); timings "
            "would mix. Use a fresh run directory."
        )


class _Writer:
    """Append-only JSONL; each batch is flushed and fsynced so a crash loses at most one batch."""

    def __init__(self, path: Path) -> None:
        self._f = path.open("a", encoding="utf-8")

    def write(self, decisions: Sequence[Decision]) -> None:
        self._f.write("".join(d.model_dump_json() + "\n" for d in decisions))
        self._f.flush()
        os.fsync(self._f.fileno())

    def close(self) -> None:
        self._f.close()


def run(
    spec: RunSpec,
    units: Sequence[Unit],
    texts: Mapping[str, str],
    warmup_texts: Sequence[str],
    client_factory: Callable[[], LayaLike],
    hw: HwInfo,
    log: Log,
) -> int:
    """Decide every unit not yet in the run directory. Returns the number of laya calls made."""
    spec.out_dir.mkdir(parents=True, exist_ok=True)
    decisions_path, meta_path = spec.out_dir / "decisions.jsonl", spec.out_dir / "meta.json"
    prev = RunMeta.model_validate_json(meta_path.read_text()) if meta_path.exists() else None
    if prev is not None:
        _check_resume(prev, spec)
        _check_same_machine(prev.hw, hw)
    unit_ids = {u.id for u in units}
    done = {d.unit_id for d in read_existing(decisions_path) if not d.warmup}
    stray = sorted(done - unit_ids)
    if stray:
        raise RunError(f"{decisions_path} has decisions for units not in this run, e.g. {stray[0]}")
    log(f"resumed: {len(done)}/{len(units)} already done")
    todo = [u for u in units if u.id not in done]
    if not todo:
        log("laya calls: 0")
        return 0
    if spec.warmup_calls and not warmup_texts:
        raise RunError("warmup requested but no warmup texts")

    t_load = time.perf_counter()
    client = client_factory()  # preload before any timed call
    log(f"loaded {client.checkpoint}@{client.revision[:12]} on {client.device} "
        f"in {time.perf_counter() - t_load:.1f}s")  # fmt: skip
    if prev is not None and prev.device != client.device:
        raise RunError(f"device changed from {prev.device} to {client.device}; timings would mix")
    if prev is not None and prev.checkpoint_rev != client.revision:
        raise RunError(
            f"checkpoint revision changed from {prev.checkpoint_rev} to {client.revision}; "
            "use a fresh run directory"
        )
    mode: Literal["batch1", "batched"] = "batch1" if spec.batch_size == 1 else "batched"

    def check_device() -> Device:
        dev = client.current_device()
        if dev != client.device:
            log(f"ERROR laya moved from {client.device} to {dev} mid-run; batch discarded")
            raise RunError(
                f"laya fell back from {client.device} to {dev} mid-run; timings would mix. "
                "Resume on the original device or start a fresh run with device set explicitly."
            )
        return dev

    meta = RunMeta(
        arm=spec.arm,
        qs=spec.qs.id,
        dataset=spec.dataset,
        hw=hw,
        device=client.device,
        checkpoint=client.checkpoint,
        checkpoint_rev=client.revision,
        config_hashes=dict(spec.config_hashes),
        batch_size=spec.batch_size,
        warmup_calls=spec.warmup_calls,
        sessions=prev.sessions + 1 if prev else 1,
        started_at=prev.started_at if prev else _now(),
        finished_at=None,
    )
    meta_path.write_text(meta.model_dump_json(indent=2) + "\n")

    def decision(
        unit_id: str,
        res: Mapping[str, Any],
        latency_ms: float,
        t_offset_ms: float,
        batch_size: int,
        device: Device,
        warmup: bool = False,
        state_tokens: int | None = None,
        cut: Sequence[str] = (),
    ) -> Decision:
        return Decision(
            unit_id=unit_id,
            arm=spec.arm,
            qs=spec.qs.id,
            checkpoint=client.checkpoint,
            checkpoint_rev=client.revision,
            max_len=spec.max_len,
            answers=to_answers(res, spec.questions),
            latency_ms=latency_ms,
            t_offset_ms=t_offset_ms,
            batch_size=batch_size,
            mode=mode,
            device=device,
            warmup=warmup,
            state_tokens=state_tokens,
            truncated_questions=list(cut),
        )

    writer = _Writer(decisions_path)
    calls = 0
    t0 = time.perf_counter_ns()
    try:
        for i in range(spec.warmup_calls):
            text = warmup_texts[i % len(warmup_texts)]
            start = time.perf_counter_ns()
            res, ns = client.predict(text)
            calls += 1
            dev = check_device()
            warm = decision(f"warmup:{i}", res, ns / 1e6, (start - t0) / 1e6, 1, dev, warmup=True)
            writer.write([warm])
        for b in range(0, len(todo), spec.batch_size):
            batch = todo[b : b + spec.batch_size]
            states = [texts[u.id] for u in batch]
            seen = [client.state_tokens(s) for s in states]  # outside the timer
            start = time.perf_counter_ns()
            if spec.batch_size == 1:
                one, ns = client.predict(states[0])
                results = [one]
            else:
                results, ns = client.predict_batch(states)
            calls += 1
            dev = check_device()
            out: list[Decision] = []
            for u, res, (n_tok, cut) in zip(batch, results, seen, strict=True):
                if cut and not u.truncated:
                    log(
                        f"WARN {u.id}: state cut for {cut} ({n_tok} tokens) "
                        "but unit.truncated=false"
                    )
                if u.truncated and not cut:
                    log(f"note {u.id}: unit.truncated=true but no question cut the state")
                out.append(
                    decision(u.id, res, ns / 1e6 / len(batch), (start - t0) / 1e6, len(batch),
                             dev, state_tokens=n_tok, cut=cut)
                )  # fmt: skip
            writer.write(out)
            if (b // spec.batch_size) % 25 == 0:
                log(f"progress: {len(done) + b + len(batch)}/{len(units)}")
    finally:
        writer.close()
    meta_path.write_text(
        meta.model_copy(update={"finished_at": _now()}).model_dump_json(indent=2) + "\n"
    )
    log(f"laya calls: {calls} ({spec.warmup_calls} warmup)")
    return calls
