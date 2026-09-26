import math
from pathlib import Path

import pytest

from bench import calibrate as cal
from bench.config import load_policy
from bench.domain import Answer, Decision, Unit
from tests.fixture_expected import FIXTURE_UNITS, fixture_units

ROOT = Path(__file__).resolve().parent.parent
POLICY = load_policy(ROOT / "config" / "policy.yaml")
MOCK = ROOT / "fixtures" / "mini" / "decisions_mock.jsonl"
HASHES = {"decisions": "d" * 64, "units": "u" * 64}


def units() -> dict[str, Unit]:
    return {u.id: u for u in fixture_units()}


def mock_decisions() -> list[Decision]:
    return [Decision.model_validate_json(x) for x in MOCK.read_text().splitlines()]


def test_temperature_golden_t_equals_2() -> None:
    # p = 0.9 on option 0 for every row, right 3 times out of 4: the NLL optimum calibrates
    # 0.9 to 0.75, i.e. 9^(1/T) = 3, so T = ln 9 / ln 3 = 2 exactly.
    t = cal.fit_temperature([[0.9, 0.1]] * 4, [0, 0, 0, 1])
    assert abs(t - 2.0) < 1e-6
    assert abs(cal.apply_temperature({"A": 0.9, "B": 0.1}, t)["A"] - 0.75) < 1e-6


def test_temperature_identity_and_eps() -> None:
    assert cal.apply_temperature({"A": 0.7, "B": 0.3}, 1.0) == pytest.approx({"A": 0.7, "B": 0.3})
    p = cal.apply_temperature({"A": 1.0, "B": 0.0}, 2.0)  # rounded zero is clipped to EPS
    assert 0 < p["B"] < 1e-2 and math.isclose(sum(p.values()), 1.0)


def test_underconfident_rows_get_t_below_1() -> None:
    t = cal.fit_temperature([[0.6, 0.4]] * 10, [0] * 10)
    assert t < 1.0


def test_t_low() -> None:
    pos = [0.9, 0.2, 0.5, 0.7, 0.3, 0.8, 0.6, 0.4]
    assert cal.fit_t_low(pos, 0.995) == 0.2  # 0 misses allowed of 8
    assert cal.fit_t_low(pos, 0.75) == 0.4  # floor(0.25 * 8) = 2 misses: 0.2, 0.3
    with pytest.raises(cal.CalibError):
        cal.fit_t_low([], 0.995)


def test_t_high() -> None:
    p = [0.1, 0.4, 0.6, 0.7, 0.9]
    y = [False, True, False, True, True]
    assert cal.fit_t_high(p, y, 0.98, 0.0) == 0.7  # {0.7, 0.9} both positive
    assert cal.fit_t_high(p, y, 0.7, 0.0) == 0.4  # all 5: 3/5 < 0.7; {0.4..0.9}: 3/4
    assert cal.fit_t_high(p, y, 0.98, 0.8) == 0.8  # never below t_low
    assert cal.fit_t_high([0.5], [False], 0.98, 0.1) is None  # unreachable
    # audit A3: p = 1.0 with precision 0.5 must not yield a reachable "unreachable" sentinel
    assert cal.fit_t_high([0.5, 1.0, 1.0], [True, False, True], 0.98, 0.5) is None


def test_gold_answer_mapping() -> None:
    gold, _ = FIXTURE_UNITS["fx05:chunk:512:0"]
    assert cal.gold_answer(gold, "category") == "coded"
    assert cal.gold_answer(gold, "has_staff_pii") == "A"
    assert cal.gold_answer(gold, "has_phi_direct") == "B"
    with pytest.raises(cal.CalibError):
        cal.gold_answer(gold, "mystery")


def test_fit_on_mock_and_hash_roundtrip(tmp_path: Path) -> None:
    params = cal.fit(mock_decisions(), units(), POLICY, "fixture_debug", input_hashes=HASHES)
    assert params.arm == "mock" and params.qs == "qs_v1" and params.fit_on == "fixture_debug"
    assert set(params.temperatures) == {
        "pii_present:2",
        "subject_role:4",
        "category:5",
        "doc_kind:4",
    }
    assert params.t_low <= params.t_high
    path = tmp_path / "mock__qs_v1.json"
    cal.write(params, path)
    assert cal.load_verified(path, allow_debug=True) == params
    with pytest.raises(cal.CalibError, match="allow-debug-calib"):
        cal.load_verified(path)
    tampered = params.model_copy(update={"t_low": params.t_low / 2})
    path.write_text(tampered.model_dump_json())
    with pytest.raises(cal.CalibHashError):
        cal.load_verified(path, allow_debug=True)


def test_fit_rejects_bad_inputs() -> None:
    decs = mock_decisions()
    with pytest.raises(cal.CalibError, match="no non-warmup"):
        cal.fit(
            [d for d in decs if d.warmup], units(), POLICY, "fixture_debug", input_hashes=HASHES
        )
    other = decs[2].model_copy(update={"arm": "other"})
    with pytest.raises(cal.CalibError, match="mix"):
        cal.fit([*decs[:2], other, *decs[3:]], units(), POLICY, "fixture_debug",
                input_hashes=HASHES)  # fmt: skip
    with pytest.raises(cal.CalibError, match="duplicate decision"):  # audit A9
        cal.fit([*decs, decs[2]], units(), POLICY, "fixture_debug", input_hashes=HASHES)
    orphan = decs[2].model_copy(update={"unit_id": "nope:chunk:512:0"})
    with pytest.raises(cal.CalibError, match="no unit"):
        cal.fit([*decs, orphan], units(), POLICY, "fixture_debug", input_hashes=HASHES)
    no_pii = decs[2].model_copy(
        update={"answers": [a for a in decs[2].answers if a.question != "pii_present"]}
    )
    with pytest.raises(cal.CalibError, match="pii_present"):
        cal.fit([*decs[3:], no_pii], units(), POLICY, "fixture_debug", input_hashes=HASHES)
    with pytest.raises(cal.CalibError, match="no rows"):
        cal.fit_temperature([], [])
    assert isinstance(decs[2].answers[0], Answer)
