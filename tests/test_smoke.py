import json
import os
from pathlib import Path

import pytest
from typer.testing import CliRunner

from bench.cli import app

ROOT = Path(__file__).resolve().parent.parent


def test_cli_imports_and_lists_hw() -> None:
    result = CliRunner().invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "hw" in result.stdout


def test_hw_writes_valid_json(tmp_path: Path) -> None:
    out = tmp_path / "hw.json"
    result = CliRunner().invoke(app, ["hw", "--out", str(out)])
    assert result.exit_code == 0, result.output
    data = json.loads(out.read_text())
    assert data["device"] in {"cuda", "mps", "cpu"}
    for key in ("os", "arch", "cpu", "ram_gb", "python", "torch", "laya"):
        assert data[key], key
    assert data["ram_gb"] > 0
    assert isinstance(data["checkpoints"], dict)


def test_hw_reads_checkpoint_revisions(tmp_path: Path) -> None:
    lock = tmp_path / "models.lock.json"
    lock.write_text(json.dumps({"english": {"repo": "r", "subfolder": "", "revision": "abc"}}))
    out = tmp_path / "hw.json"
    result = CliRunner().invoke(app, ["hw", "--out", str(out), "--models-lock", str(lock)])
    assert result.exit_code == 0, result.output
    data = json.loads(out.read_text())
    assert data["checkpoints"] == {"english": "abc"}


def test_hw_missing_lock_is_empty(tmp_path: Path) -> None:
    out = tmp_path / "hw.json"
    missing = tmp_path / "nope.json"
    result = CliRunner().invoke(app, ["hw", "--out", str(out), "--models-lock", str(missing)])
    assert result.exit_code == 0, result.output
    assert json.loads(out.read_text())["checkpoints"] == {}


@pytest.mark.model
def test_laya_choice_result_shape() -> None:
    """Pin the result keys of the installed laya version (docs/specs/laya-runtime.md)."""
    os.environ.setdefault("USE_TF", "0")
    import laya

    lock = json.loads((ROOT / "models.lock.json").read_text())
    agent = laya.load(lock["english"]["path"])
    q = {
        "pii": {
            "type": "choice",
            "instructions": "Does this text contain a person's name?",
            "criteria": {"A": "yes", "B": "no"},
        }
    }
    res = agent.predict("Patient Jane Doe was seen on day 3.", q, max_len=512, head_max_len=192)
    ans = res["answers"]["pii"]
    assert ans["type"] == "choice"
    assert ans["choice"] in {"A", "B"}
    assert set(ans["probabilities"]) == {"A", "B"}
    assert abs(sum(ans["probabilities"].values()) - 1.0) < 1e-3
    assert 0.0 <= ans["confidence"] <= 1.0
    assert "answer_confidence" in ans
    assert "act_probability" in ans["action"]
