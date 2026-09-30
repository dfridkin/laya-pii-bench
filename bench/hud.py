"""HUD replay export (docs/specs/hud.md, M7): real routed decisions, never mock data.

`bench report --hud` writes one `Replay` holding every scored run's decisions on one split (test by
default), with the documents stored once. Provenance is checked before anything is written: the
scores must name the run's decisions, units and docs by hash, and the calib file must be the one
the scores cite. The replay clock is the cumulative recorded latency in run order.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

from bench.calibrate import load_verified
from bench.domain import (
    Decision,
    Replay,
    ReplayDoc,
    ReplayRun,
    ReplayUnit,
    RoutedDecision,
    RunMeta,
    Scores,
)
from bench.label import read_docs, read_units


class ReplayError(RuntimeError):
    pass


@dataclass(frozen=True)
class Sources:
    runs_dir: Path = Path("runs")
    calib_dir: Path = Path("calib")
    units_dir: Path = Path("data/units")
    docs: Path = Path("data/docs.jsonl")


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def timeline(decisions: Sequence[Decision]) -> list[float]:
    """Start time of each decision: the sum of the recorded latencies before it."""
    out: list[float] = []
    t = 0.0
    for d in decisions:
        out.append(t)
        t += d.latency_ms
    return out


def replay_run(scores_path: Path, split: str, src: Sources) -> tuple[ReplayRun, set[str]]:
    s = Scores.model_validate_json(scores_path.read_text(encoding="utf-8"))
    c = s.context
    if split not in s.splits:
        raise ReplayError(f"{scores_path}: no {split!r} split")
    run_dir = src.runs_dir / c.arm / c.qs
    decisions_path = run_dir / "decisions.jsonl"
    units_path = src.units_dir / f"{c.arm}.jsonl"
    checks = {
        decisions_path: c.decisions_sha256,
        units_path: c.units_sha256,
        src.docs: c.docs_sha256,
    }
    for path, want in checks.items():
        if not path.exists() or _sha(path) != want:
            raise ReplayError(f"{path} is not the file {scores_path} was scored from")
    calib = load_verified(src.calib_dir / f"{c.arm}__{c.qs}.json", allow_debug=False)
    if calib.content_hash != c.calib_hash:
        raise ReplayError(f"calib for {c.arm}/{c.qs} is not the one {scores_path} cites")
    routed_path = scores_path.with_suffix(".routed.jsonl")
    lines = routed_path.read_text(encoding="utf-8").splitlines()
    routed = [RoutedDecision.model_validate_json(line) for line in lines if line.strip()]
    routed = [r for r in routed if r.split == split]
    if len(routed) != s.splits[split].headline.n_units:
        raise ReplayError(f"{routed_path}: {len(routed)} {split} decisions, scores say "
                          f"{s.splits[split].headline.n_units}")  # fmt: skip
    units = {u.id: u for u in read_units(units_path)}
    needed = [units[r.decision.unit_id] for r in routed]
    meta = RunMeta.model_validate_json((run_dir / "meta.json").read_text(encoding="utf-8"))
    run = ReplayRun(
        label=f"{c.arm} / {c.qs}", split=split, meta=meta, calib=calib,
        scores_sha256=_sha(scores_path),
        units=[ReplayUnit(id=u.id, doc_id=u.doc_id, start=u.start, end=u.end,
                          truncated=u.truncated, gold=u.gold) for u in needed],
        decisions=routed, t_ms=timeline([r.decision for r in routed]),
    )  # fmt: skip
    return run, {u.doc_id for u in needed}


def build(scores_paths: Sequence[Path], split: str = "test", src: Sources | None = None) -> Replay:
    src = src or Sources()
    runs: list[ReplayRun] = []
    doc_ids: set[str] = set()
    for p in sorted(scores_paths):
        run, ids = replay_run(p, split, src)
        runs.append(run)
        doc_ids |= ids
    if not runs:
        raise ReplayError("no scored runs")
    docs = [ReplayDoc(id=d.id, doc_type=d.doc_type, lang=d.lang, text=d.text, spans=d.spans)
            for d in read_docs(src.docs) if d.id in doc_ids]  # fmt: skip
    return Replay(created_at=datetime.now(UTC).isoformat(timespec="seconds"), docs=docs, runs=runs)


def write(replay: Replay, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(replay.model_dump(mode="json"), separators=(",", ":")),
                   encoding="utf-8")  # fmt: skip
