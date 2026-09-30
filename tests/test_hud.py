"""M7: the HUD replay export uses real, provenance-checked routed decisions."""

from pathlib import Path

import pytest

from bench import hud
from bench.domain import Decision, Route, RoutedDecision, Scores

ROOT = Path(__file__).resolve().parent.parent
SCORES = sorted((ROOT / "scores").glob("*.json"))
needs_main = pytest.mark.skipif(
    not (SCORES and (ROOT / "data" / "docs.jsonl").exists() and (ROOT / "runs" / "A").exists()),
    reason="main corpus runs not present",
)
SRC = hud.Sources(
    ROOT / "runs", ROOT / "calib", ROOT / "data" / "units", ROOT / "data" / "docs.jsonl"
)


def _dec(latency: float) -> Decision:
    line = (ROOT / "fixtures/mini/decisions_mock.jsonl").read_text().splitlines()[0]
    return Decision.model_validate_json(line).model_copy(update={"latency_ms": latency})


def test_timeline_is_cumulative_recorded_latency() -> None:
    assert hud.timeline([_dec(5), _dec(7), _dec(1)]) == [0.0, 5.0, 12.0]
    assert hud.timeline([]) == []


@needs_main
def test_replay_matches_scores_and_run_order() -> None:
    p = ROOT / "scores" / "A__qs_v1.json"
    run, doc_ids = hud.replay_run(p, "test", SRC)
    s = Scores.model_validate_json(p.read_text())
    assert run.meta.dataset == "main" and run.label == "A / qs_v1"
    assert len(run.decisions) == s.splits["test"].headline.n_units
    assert all(r.split == "test" for r in run.decisions)
    assert run.calib.content_hash == s.context.calib_hash
    routed = [RoutedDecision.model_validate_json(x)
              for x in p.with_suffix(".routed.jsonl").read_text().splitlines()]  # fmt: skip
    assert [r.decision.unit_id for r in run.decisions] == [
        r.decision.unit_id for r in routed if r.split == "test"
    ]  # run order kept
    assert run.t_ms == hud.timeline([r.decision for r in run.decisions])
    assert {u.id for u in run.units} == {r.decision.unit_id for r in run.decisions}
    assert doc_ids == {u.doc_id for u in run.units}


@needs_main
def test_replay_refuses_files_other_than_the_scored_ones(tmp_path: Path) -> None:
    p = ROOT / "scores" / "A__qs_v1.json"
    other_docs = hud.Sources(SRC.runs_dir, SRC.calib_dir, SRC.units_dir,
                             ROOT / "fixtures" / "mini" / "docs.jsonl")  # fmt: skip
    with pytest.raises(hud.ReplayError, match="not the file"):
        hud.replay_run(p, "test", other_docs)
    with pytest.raises(hud.ReplayError, match="no 'train' split"):
        hud.replay_run(p, "train", SRC)
    runs = tmp_path / "runs" / "A" / "qs_v1"
    runs.mkdir(parents=True)
    src_run = ROOT / "runs" / "A" / "qs_v1"
    (runs / "meta.json").write_text((src_run / "meta.json").read_text())
    (runs / "decisions.jsonl").write_text((src_run / "decisions.jsonl").read_text() + "\n")
    tampered = hud.Sources(tmp_path / "runs", SRC.calib_dir, SRC.units_dir, SRC.docs)
    with pytest.raises(hud.ReplayError, match="not the file"):
        hud.replay_run(p, "test", tampered)


@needs_main
def test_build_stores_each_document_once(tmp_path: Path) -> None:
    paths = [ROOT / "scores" / f"A__{q}.json" for q in ("qs_v1", "qs_v2")]
    r = hud.build(paths, "test", SRC)
    assert [x.label for x in r.runs] == ["A / qs_v1", "A / qs_v2"]
    ids = [d.id for d in r.docs]
    assert len(ids) == len(set(ids)) == len({u.doc_id for x in r.runs for u in x.units})
    out = tmp_path / "replay.json"
    hud.write(r, out)
    assert out.stat().st_size > 0


@needs_main
def test_replay_refuses_an_edited_routed_file(tmp_path: Path) -> None:
    src = ROOT / "scores" / "A__qs_v1.json"
    (tmp_path / src.name).write_text(src.read_text())
    lines = src.with_suffix(".routed.jsonl").read_text().splitlines()
    r = RoutedDecision.model_validate_json(lines[0])
    flipped = Route.FORWARD if r.route is not Route.FORWARD else Route.ESCALATE
    lines[0] = r.model_copy(update={"route": flipped}).model_dump_json()  # same row count
    (tmp_path / src.with_suffix(".routed.jsonl").name).write_text("\n".join(lines) + "\n")
    with pytest.raises(hud.ReplayError, match="not the routed file"):
        hud.replay_run(tmp_path / src.name, "test", SRC)
