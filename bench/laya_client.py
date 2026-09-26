"""Thin wrapper over the installed laya runtime (docs/specs/laya-runtime.md).

Loads the checkpoint pinned in models.lock.json up front (no lazy loading), times `predict` alone
with `perf_counter_ns`, adapts results to `Answer`, and measures truncation exactly as laya builds
its input: `[CLS] head [SEP] options [SEP] state [SEP]` capped at `max_len`, so the room for the
state differs per question.
"""

from __future__ import annotations

import json
import math
import os
import time
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any, Protocol, cast, get_args

from bench.domain import Answer, Device

os.environ.setdefault("USE_TF", "0")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

LOADABLE = {"english": None, "multilingual": "multilingual"}  # checkpoint -> repo subfolder


class LayaError(RuntimeError):
    pass


class LayaLike(Protocol):
    """What the runner needs from a checkpoint; tests substitute a fake."""

    checkpoint: str
    revision: str
    device: Device

    def current_device(self) -> Device: ...
    def predict(self, state: str) -> tuple[dict[str, Any], int]: ...
    def predict_batch(self, states: Sequence[str]) -> tuple[list[dict[str, Any]], int]: ...
    def state_tokens(self, state: str) -> tuple[int, list[str]]: ...


def to_answers(
    result: Mapping[str, Any], questions: Mapping[str, Mapping[str, Any]]
) -> list[Answer]:
    """Adapt one laya result to `Answer`s, in question order. Checks keys and probability mass."""
    answers = cast(Mapping[str, Mapping[str, Any]], result["answers"])
    out: list[Answer] = []
    for qid, q in questions.items():
        a = answers[qid]
        if q["type"] == "noul":
            p_true = float(a["noul"])
            probs = {"false": 1.0 - p_true, "true": p_true}
        else:
            probs = {
                str(k): float(v) for k, v in cast(Mapping[str, float], a["probabilities"]).items()
            }
        want = (
            {"false", "true"}
            if q["type"] == "noul"
            else set(q["criteria"])
            if q["type"] == "choice"
            else {str(i) for i in range(len(q["criteria"]))}
        )
        if set(probs) != want:
            raise LayaError(f"{qid}: option keys {sorted(probs)} != expected {sorted(want)}")
        if not math.isclose(sum(probs.values()), 1.0, abs_tol=1e-3):
            raise LayaError(f"{qid}: probabilities sum to {sum(probs.values())}")
        choice = str(a["choice"]) if "choice" in a else max(probs, key=lambda k: probs[k])
        out.append(
            Answer(
                question=qid,
                choice=choice,
                probs=probs,
                confidence=float(a["confidence"]),
                answer_confidence=float(a["answer_confidence"])
                if "answer_confidence" in a
                else None,
            )
        )
    return out


class LayaClient:
    """Preloaded laya checkpoint bound to one arm's `max_len`/`head_max_len` and question set."""

    checkpoint: str
    revision: str
    device: Device

    def __init__(
        self,
        checkpoint: str,
        questions: Mapping[str, Mapping[str, Any]],
        max_len: int,
        head_max_len: int,
        models_lock: Path = Path("models.lock.json"),
        device: str | None = None,
    ) -> None:
        if checkpoint not in LOADABLE:
            raise LayaError(f"checkpoint {checkpoint!r} is not loadable yet (fine-tuned arm: M8)")
        import laya  # pyright: ignore[reportMissingTypeStubs]
        from laya import common  # pyright: ignore[reportMissingTypeStubs]

        entry: dict[str, str] = json.loads(models_lock.read_text())[checkpoint]
        self.checkpoint = checkpoint
        self.revision = entry["revision"]
        self.questions = {k: dict(v) for k, v in questions.items()}
        self.max_len, self.head_max_len = max_len, head_max_len
        load: Any = laya.load  # pyright: ignore[reportUnknownMemberType]
        self._agent: Any = load(entry["path"], device=device, subfolder=LOADABLE[checkpoint])
        self.device = self.current_device()
        self._tok: Any = self._agent.tok
        # Room for the state per question: build each question's input around an empty state.
        build: Any = getattr(common, "build_sequence")  # noqa: B009 (untyped laya API)
        self._room: dict[str, int] = {}
        for qid, q in self.questions.items():
            internal = self._agent._to_internal(q)  # pyright: ignore[reportPrivateUsage]
            seq, _ = cast(
                tuple[list[int], list[int]],
                build(self._tok, "", internal, max_len, head_max_len, state_ids=[]),
            )
            self._room[qid] = max(0, max_len - (len(seq) - 1) - 1)

    def current_device(self) -> Device:
        """laya may move the agent to cpu mid-run (e.g. on an MPS memory error)."""
        dev = str(self._agent.device.type)
        if dev not in get_args(Device):
            raise LayaError(f"unsupported device {dev!r}")
        return cast(Device, dev)

    def state_tokens(self, state: str) -> tuple[int, list[str]]:
        ids: list[int] = self._tok(
            state.replace(self._tok.mask_token, " "), add_special_tokens=False
        )["input_ids"]
        return len(ids), [q for q, room in self._room.items() if len(ids) > room]

    def predict(self, state: str) -> tuple[dict[str, Any], int]:
        t0 = time.perf_counter_ns()
        res: dict[str, Any] = self._agent.predict(
            state, self.questions, max_len=self.max_len, head_max_len=self.head_max_len
        )
        return res, time.perf_counter_ns() - t0

    def predict_batch(self, states: Sequence[str]) -> tuple[list[dict[str, Any]], int]:
        t0 = time.perf_counter_ns()
        res: list[dict[str, Any]] = self._agent.predict_batch(
            list(states),
            self.questions,
            batch_size=len(states),
            max_len=self.max_len,
            head_max_len=self.head_max_len,
        )
        return res, time.perf_counter_ns() - t0
