"""Runner behaviour with a fake laya client: resume, warmup, meta, truncation, batching."""

from collections.abc import Sequence
from pathlib import Path
from typing import Any

import pytest

from bench.config import load_question_set
from bench.domain import Decision, Device, HwInfo, QuestionSet, RunMeta
from bench.laya_client import LayaError, to_answers
from bench.questions import QuestionError, build
from bench.run import RunError, RunSpec, read_existing, run
from tests.fixture_expected import fixture_units

ROOT = Path(__file__).resolve().parent.parent
QS = load_question_set(ROOT / "config" / "questions" / "qs_v1.yaml")
QUESTIONS = build(QS, "english")
UNITS = fixture_units()
TEXTS = {u.id: f"text of {u.id} " * 3 for u in UNITS}
HW = HwInfo(
    os="x", arch="arm64", cpu="c", ram_gb=8.0, python="3.12", torch="t", laya="0.3.20",
    device="mps", device_name="Apple MPS", checkpoints={"english": "rev"}, created_at="now",
)  # fmt: skip


def fake_result(state: str) -> dict[str, Any]:
    p = 0.9 if "fx0" in state else 0.3
    answers: dict[str, Any] = {}
    for qid, q in QUESTIONS.items():
        keys = list(q["criteria"])
        probs = {k: (p if i == 0 else (1 - p) / (len(keys) - 1)) for i, k in enumerate(keys)}
        answers[qid] = {
            "type": "choice",
            "choice": keys[0],
            "probabilities": probs,
            "confidence": 0.5,
            "answer_confidence": p,
            "action": {"act_probability": 0.5},
        }
    return {"answers": answers}


class FakeClient:
    checkpoint = "english"
    revision = "rev-abc"

    def __init__(self, device: Device = "mps", cut_over: int = 10_000) -> None:
        self.device: Device = device
        self.calls = 0
        self.cut_over = cut_over

    def predict(self, state: str) -> tuple[dict[str, Any], int]:
        self.calls += 1
        return fake_result(state), 5_000_000

    def predict_batch(self, states: Sequence[str]) -> tuple[list[dict[str, Any]], int]:
        self.calls += 1
        return [fake_result(s) for s in states], 8_000_000

    def state_tokens(self, state: str) -> tuple[int, list[str]]:
        n = len(state.split())
        return n, (["pii_present"] if n > self.cut_over else [])


def spec(
    out: Path, batch_size: int = 1, warmup: int = 3, hashes: dict[str, str] | None = None
) -> RunSpec:
    return RunSpec(
        arm="A", qs=QS, questions=QUESTIONS, checkpoint="english", max_len=512, dataset="mini",
        out_dir=out, batch_size=batch_size, warmup_calls=warmup,
        config_hashes=hashes or {"arm": "a", "question_set": "q", "docs": "d", "units": "u"},
    )  # fmt: skip


def go(
    s: RunSpec, client: FakeClient | None = None, log: list[str] | None = None
) -> tuple[int, FakeClient]:
    c = client or FakeClient()
    n = run(s, UNITS, TEXTS, ["warm text"], lambda: c, HW, (log if log is not None else []).append)
    return n, c


def test_first_run_then_resume_makes_zero_calls(tmp_path: Path) -> None:
    log: list[str] = []
    n, c = go(spec(tmp_path), log=log)
    assert n == c.calls == 3 + len(UNITS)
    assert "resumed: 0/11 already done" in log
    decisions = read_existing(tmp_path / "decisions.jsonl")
    assert [d.warmup for d in decisions].count(True) == 3
    live = [d for d in decisions if not d.warmup]
    assert [d.unit_id for d in live] == [u.id for u in UNITS]
    assert all(d.batch_size == 1 and d.latency_ms == 5.0 and d.state_tokens for d in live)
    assert live[0].answers[0].answer_confidence == 0.9

    log2: list[str] = []
    factory_called: list[bool] = []

    def factory() -> FakeClient:
        factory_called.append(True)
        return FakeClient()

    n2 = run(spec(tmp_path), UNITS, TEXTS, ["warm"], factory, HW, log2.append)
    assert n2 == 0 and not factory_called  # no load, no warmup, no calls
    assert "resumed: 11/11 already done" in log2 and "laya calls: 0" in log2


def test_meta_contents_and_partial_resume(tmp_path: Path) -> None:
    go(spec(tmp_path))
    meta = RunMeta.model_validate_json((tmp_path / "meta.json").read_text())
    assert meta.hw == HW and meta.warmup_calls == 3 and meta.checkpoint_rev == "rev-abc"
    assert meta.device == "mps" and meta.sessions == 1 and meta.finished_at
    # drop the last 4 decisions (simulated crash) and resume
    lines = (tmp_path / "decisions.jsonl").read_text().splitlines()
    (tmp_path / "decisions.jsonl").write_text("\n".join(lines[:-4]) + "\n")
    log: list[str] = []
    n, _ = go(spec(tmp_path), log=log)
    assert n == 3 + 4 and "resumed: 7/11 already done" in log
    meta2 = RunMeta.model_validate_json((tmp_path / "meta.json").read_text())
    assert meta2.sessions == 2 and meta2.started_at == meta.started_at
    live = [d for d in read_existing(tmp_path / "decisions.jsonl") if not d.warmup]
    assert sorted(d.unit_id for d in live) == sorted(u.id for u in UNITS)


def test_refuses_changed_config_or_device(tmp_path: Path) -> None:
    go(spec(tmp_path))
    lines = (tmp_path / "decisions.jsonl").read_text().splitlines()
    (tmp_path / "decisions.jsonl").write_text("\n".join(lines[:-1]) + "\n")
    changed = {"arm": "a", "question_set": "OTHER", "docs": "d", "units": "u"}
    with pytest.raises(RunError, match="question_set"):
        go(spec(tmp_path, hashes=changed))
    with pytest.raises(RunError, match="batch_size"):
        go(spec(tmp_path, batch_size=2))
    with pytest.raises(RunError, match="device changed"):
        go(spec(tmp_path), FakeClient(device="cpu"))


def test_torn_line_and_stray_units(tmp_path: Path) -> None:
    go(spec(tmp_path))
    path = tmp_path / "decisions.jsonl"
    good = path.read_text()
    path.write_text(good + '{"unit_id": "fx0')
    with pytest.raises(RunError, match="torn write"):
        go(spec(tmp_path))
    stray = Decision.model_validate_json(good.splitlines()[-1]).model_copy(
        update={"unit_id": "zz:chunk:512:0"}
    )
    path.write_text(good + stray.model_dump_json() + "\n")
    with pytest.raises(RunError, match="not in this run"):
        go(spec(tmp_path))


def test_truncation_recorded_and_warned(tmp_path: Path) -> None:
    log: list[str] = []
    go(spec(tmp_path, warmup=0), FakeClient(cut_over=2), log=log)
    live = read_existing(tmp_path / "decisions.jsonl")
    assert all(d.truncated_questions == ["pii_present"] for d in live)
    assert any(line.startswith("WARN fx01:chunk:512:0: state cut") for line in log)


def test_batched_mode_splits_latency(tmp_path: Path) -> None:
    n, c = go(spec(tmp_path, batch_size=4, warmup=0))
    assert n == c.calls == 3  # 11 units in batches of 4
    live = read_existing(tmp_path / "decisions.jsonl")
    assert [d.batch_size for d in live] == [4] * 8 + [3] * 3
    assert live[0].latency_ms == 2.0 and live[-1].latency_ms == pytest.approx(8 / 3)


def test_warmup_needs_texts(tmp_path: Path) -> None:
    with pytest.raises(RunError, match="warmup"):
        run(spec(tmp_path), UNITS, TEXTS, [], FakeClient, HW, print)


# --- questions and adapter ---------------------------------------------------------------------


def test_noul_rejected_on_english_only() -> None:
    qs = QuestionSet.model_validate(
        {"id": "q", "questions": {"n": {"type": "noul", "instructions": "?"}}}
    )
    for ckpt in ("english", "finetuned_english"):
        with pytest.raises(QuestionError, match="invariant 5"):
            build(qs, ckpt)
    assert build(qs, "multilingual") == {"n": {"type": "noul", "instructions": "?"}}
    sc = QuestionSet.model_validate(
        {
            "id": "s",
            "questions": {"s": {"type": "score", "instructions": "?", "criteria": ["lo", "hi"]}},
        }
    )
    assert build(sc, "english")["s"]["criteria"] == ["lo", "hi"]


def test_adapter_checks_keys_and_mass() -> None:
    res = fake_result("fx01")
    answers = to_answers(res, QUESTIONS)
    assert [a.question for a in answers] == list(QUESTIONS)
    bad = fake_result("fx01")
    bad["answers"]["pii_present"]["probabilities"] = {"A": 0.9, "C": 0.1}
    with pytest.raises(LayaError, match="option keys"):
        to_answers(bad, QUESTIONS)
    bad["answers"]["pii_present"]["probabilities"] = {"A": 0.9, "B": 0.3}
    with pytest.raises(LayaError, match="sum"):
        to_answers(bad, QUESTIONS)
    noul = {"answers": {"n": {"type": "noul", "noul": 0.25, "confidence": 0.75}}}
    [a] = to_answers(noul, {"n": {"type": "noul", "instructions": "?"}})
    assert a.probs == {"false": 0.75, "true": 0.25} and a.choice == "false"
    assert a.answer_confidence is None
    score_res = {
        "answers": {
            "s": {"type": "score", "probabilities": {"0": 0.2, "1": 0.8}, "confidence": 0.3}
        }
    }
    [s] = to_answers(
        score_res, {"s": {"type": "score", "instructions": "?", "criteria": ["lo", "hi"]}}
    )
    assert s.choice == "1"
