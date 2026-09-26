"""Regression tests from the review of the audit fix batch
(reports/audits/M0-M3-fixbatch-review-20260926-fail.md)."""

import json
from pathlib import Path
from typing import Any

import pytest
from typer.testing import CliRunner

from bench import calibrate as cal
from bench import score as sc
from bench.cli import app
from bench.config import load_policy
from bench.domain import Answer, CalibParams, Decision, HwInfo, RunMeta
from bench.label import read_docs, write_units
from tests.fixture_expected import fixture_units

ROOT = Path(__file__).resolve().parent.parent
MINI = ROOT / "fixtures" / "mini"
MOCK = MINI / "decisions_mock.jsonl"
POLICY = load_policy(ROOT / "config" / "policy.yaml")
RUN = CliRunner()


def flipped_units(path: Path) -> Path:
    write_units(
        [u.model_copy(update={"gold": u.gold.model_copy(update={
            "pii_present": "B" if u.gold.pii_present == "A" else "A"})}) for u in fixture_units()],
        path,
    )  # fmt: skip
    return path


# --- R1: unreachable t_high must not crash calibrate ---------------------------------------------


def test_calibrate_cli_with_unreachable_t_high(tmp_path: Path) -> None:
    units = flipped_units(tmp_path / "flipped.jsonl")  # no threshold reaches 0.98 precision
    out = tmp_path / "c.json"
    r = RUN.invoke(app, ["calibrate", "--decisions", str(MOCK), "--units", str(units), "--out",
                         str(out), "--debug-fit-all", "--allow-no-meta"])  # fmt: skip
    assert r.exit_code == 0, r.output
    assert "t_high=none" in r.output
    assert json.loads(out.read_text())["t_high"] is None


# --- R2: decisions without run meta need an explicit, labeled override --------------------------


def test_meta_less_decisions_refused_without_override(tmp_path: Path) -> None:
    units = flipped_units(tmp_path / "flipped.jsonl")
    nometa = tmp_path / "nometa"
    nometa.mkdir()
    (nometa / "decisions.jsonl").write_text(MOCK.read_text())
    dec = str(nometa / "decisions.jsonl")
    r = RUN.invoke(app, ["calibrate", "--decisions", dec, "--units", str(units), "--out",
                         str(tmp_path / "c.json"), "--debug-fit-all"])  # fmt: skip
    assert r.exit_code == 2 and "no meta.json" in r.output and not (tmp_path / "c.json").exists()
    r = RUN.invoke(app, ["calibrate", "--decisions", dec, "--units", str(units), "--out",
                         str(tmp_path / "c.json"), "--debug-fit-all",
                         "--allow-no-meta"])  # fmt: skip
    assert r.exit_code == 0
    score_args = ["score", "--decisions", dec, "--units", str(units), "--calib",
                  str(tmp_path / "c.json"), "--out", str(tmp_path / "s.json"), "--docs",
                  str(MINI / "docs.jsonl"), "--allow-debug-calib"]  # fmt: skip
    r = RUN.invoke(app, score_args)
    assert r.exit_code == 2 and "no meta.json" in r.output
    r = RUN.invoke(app, [*score_args, "--allow-no-meta"])
    assert r.exit_code == 0
    caveats = json.loads((tmp_path / "s.json").read_text())["caveats"]
    assert any("no run meta.json" in c for c in caveats)


def test_no_meta_override_only_with_debug_flags(tmp_path: Path) -> None:
    r = RUN.invoke(app, ["calibrate", "--decisions", str(MOCK), "--units", "x", "--out",
                         str(tmp_path / "c.json"), "--allow-no-meta"])  # fmt: skip
    assert r.exit_code == 2  # --allow-no-meta without --debug-fit-all is not enough


# --- A1: calib doc ids come from the fit itself ---


def test_fit_records_calib_doc_ids_and_overlap_is_refused() -> None:
    decisions = [Decision.model_validate_json(x) for x in MOCK.read_text().splitlines()]
    units = {u.id: u for u in fixture_units()}
    params = cal.fit(decisions, units, POLICY, "calib",
                     input_hashes={"decisions": "d", "units": "u"})  # fmt: skip
    assert params.calib_doc_ids == [f"fx{i:02d}" for i in range(1, 11)]
    with pytest.raises(sc.ScoreError, match="used to fit calib"):
        sc.verify_provenance(params, "u", "docs", None, {"fx03"})


def test_calib_split_may_be_scored_descriptively(tmp_path: Path) -> None:
    # R3: the disjointness check skips a split named "calib" (wired in the CLI); test the rule
    params = cal.fit([Decision.model_validate_json(x) for x in MOCK.read_text().splitlines()],
                     {u.id: u for u in fixture_units()}, POLICY, "calib",
                     input_hashes={"decisions": "d", "units": "u"})  # fmt: skip
    split_docs = {"calib": set(params.calib_doc_ids), "test": {"zz01"}, "holdout": {"fx02"}}
    assert sc.disjointness_scope(split_docs) == {"zz01", "fx02"}
    with pytest.raises(sc.ScoreError, match="used to fit calib"):  # holdout overlaps calib
        sc.verify_provenance(params, "u", "docs", None, sc.disjointness_scope(split_docs))
    split_docs["holdout"] = {"zz02"}
    sc.verify_provenance(params, "u", "docs", None, sc.disjointness_scope(split_docs))


# --- A6, A8: truncation slice source; route-level recall ---


def _decision(uid: str, p: float, role: str | None, **kw: Any) -> Decision:
    answers = [Answer(question="pii_present", choice="A" if p > 0.5 else "B",
                      probs={"A": p, "B": 1 - p}, confidence=0.5)]  # fmt: skip
    if role is not None:
        roles = ["patient", "staff", "both", "none"]
        answers.append(Answer(question="subject_role", choice=role,
                              probs={r: 0.7 if r == role else 0.1 for r in roles},
                              confidence=0.5))  # fmt: skip
    return Decision(unit_id=uid, arm="t", qs="q", checkpoint="c", checkpoint_rev="r",
                    max_len=512, answers=answers, latency_ms=1.0, t_offset_ms=0.0, batch_size=1,
                    **kw)  # fmt: skip


CAL = CalibParams(
    arm="t", qs="q", temperatures={"pii_present:2": 1.0, "subject_role:4": 1.0}, t_low=0.5,
    t_high=0.9, recall_target=0.995, precision_target=0.98, fit_on="calib", decisions_sha256="d",
    units_sha256="u", calib_doc_ids=[], content_hash="x",
)  # fmt: skip


def test_truncated_slice_uses_runner_measurement_both_ways() -> None:
    docs = {d.id: d for d in read_docs(MINI / "docs.jsonl")}
    units = {u.id: u for u in fixture_units()}
    a, b = "fx01:chunk:512:0", "fx02:chunk:512:0"
    units[a] = units[a].model_copy(update={"truncated": True})  # label says truncated...
    decisions = [
        _decision(a, 0.9, None, state_tokens=300, truncated_questions=[]),  # ...runner: not cut
        _decision(b, 0.1, None, state_tokens=600, truncated_questions=["pii_present"]),  # cut
    ]
    rows = sc.build_rows(decisions, units, docs, CAL, POLICY)
    trunc = {r.value: r.n_units for r in sc.slices(rows, 0.5) if r.dimension == "truncated"}
    assert trunc == {"no": 1, "yes": 1}
    by_unit = {r.unit.id: sc._truncated(r) for r in rows}  # pyright: ignore[reportPrivateUsage]
    assert by_unit == {a: False, b: True}
    # decisions without runner data (e.g. mock) fall back to the label flag
    legacy = sc.build_rows([_decision(a, 0.9, None)], units, docs, CAL, POLICY)
    assert sc._truncated(legacy[0])  # pyright: ignore[reportPrivateUsage]


def test_route_recall_counts_role_redacted_positive_as_caught() -> None:
    docs = {d.id: d for d in read_docs(MINI / "docs.jsonl")}
    units = {u.id: u for u in fixture_units()}
    # fx04 (gold A) below t_low but predicted role patient -> REDACT: a threshold miss, not a
    # false forward. fx01 (gold A) above t_low.
    decisions = [_decision("fx04:chunk:512:0", 0.2, "patient"),
                 _decision("fx01:chunk:512:0", 0.8, "both")]  # fmt: skip
    h = sc.headline(sc.build_rows(decisions, units, docs, CAL, POLICY), CAL, POLICY)
    assert h.recall is not None and h.recall.point == 0.5
    assert h.false_forwards == 0 and h.route_recall == 1.0


# --- A9: score CLI rejects rows whose mode doesn't match the run --------------------------------


def test_score_cli_rejects_foreign_mode_rows(tmp_path: Path) -> None:
    run_dir = tmp_path / "run"
    run_dir.mkdir()
    units = tmp_path / "units.jsonl"
    write_units(fixture_units(), units)
    rows = [Decision.model_validate_json(x) for x in MOCK.read_text().splitlines()]
    rows[5] = rows[5].model_copy(update={"mode": "batched"})
    (run_dir / "decisions.jsonl").write_text("".join(d.model_dump_json() + "\n" for d in rows))
    hw = HwInfo(os="o", arch="a", cpu="c", ram_gb=8, python="p", torch="t", laya="l",
                device="mps", device_name="n", checkpoints={}, created_at="x")  # fmt: skip
    meta = RunMeta(arm="mock", qs="qs_v1", dataset="mini", hw=hw, device="mps",
                   checkpoint="english", checkpoint_rev="r",
                   config_hashes={"units": sc.sha256_file(units),
                                  "docs": sc.sha256_file(MINI / "docs.jsonl")},
                   batch_size=1, warmup_calls=2, sessions=1, started_at="x",
                   finished_at="y")  # fmt: skip
    (run_dir / "meta.json").write_text(meta.model_dump_json())
    c = tmp_path / "c.json"
    dec = str(run_dir / "decisions.jsonl")
    r = RUN.invoke(app, ["calibrate", "--decisions", dec, "--units", str(units), "--out", str(c),
                         "--debug-fit-all"])  # fmt: skip
    assert r.exit_code == 0, r.output
    r = RUN.invoke(app, ["score", "--decisions", dec, "--units", str(units), "--calib", str(c),
                         "--out", str(tmp_path / "s.json"), "--docs", str(MINI / "docs.jsonl"),
                         "--allow-debug-calib"])  # fmt: skip
    assert r.exit_code == 2 and "don't match the run's mode" in r.output


# --- small gaps ---


def test_perturbation_slice_keys_pinned() -> None:
    assert sc.PERTURBATION_TAGS == (
        "email_quoting", "headers_footers", "line_wrap", "ocr_noise", "table",
    )  # fmt: skip


def test_lower_bound_fallback_with_accuracy_below_one() -> None:
    # 3 confident right + 1 exact tie scored wrong: NLL keeps falling as T -> 0 (the tie stays
    # at 0.5), so the fit lands on the lower bound although accuracy is 3/4
    t, reason = cal.fit_or_fallback([[0.9, 0.1]] * 3 + [[0.5, 0.5]], [0, 0, 0, 1])
    assert t == 1.0 and reason is not None and reason.startswith("fit hit bound")
    # a genuinely interior optimum is kept (golden case: T = 2)
    t2, reason2 = cal.fit_or_fallback([[0.9, 0.1]] * 4, [0, 0, 0, 1])
    assert reason2 is None and abs(t2 - 2.0) < 1e-6


def test_pinned_without_cache_dir_gives_bootstrap_hint(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    import huggingface_hub.constants as hc

    from bench.models import pinned

    monkeypatch.setattr(hc, "HF_HUB_CACHE", str(tmp_path / "missing"))
    with pytest.raises(FileNotFoundError, match="make bootstrap"):
        pinned("english", ROOT / "models.lock.json")


# --- R4: torn-tail repair ---


def test_valid_unterminated_last_line_is_kept(tmp_path: Path) -> None:
    from bench.run import read_existing, repair_torn_tail

    path = tmp_path / "decisions.jsonl"
    text = MOCK.read_text()
    path.write_text(text.rstrip("\n"))  # complete record, newline lost
    assert repair_torn_tail(path) == 0
    assert path.read_text() == text and len(read_existing(path)) == 13
    path.write_text(text + text.splitlines()[3][:30])  # genuinely torn
    assert repair_torn_tail(path) == 30 and path.read_text() == text


# --- review 2 follow-ups ---


def test_refused_resume_leaves_torn_file_untouched(tmp_path: Path) -> None:
    from bench.run import RunError
    from tests.test_run import go, spec

    go(spec(tmp_path))
    path = tmp_path / "decisions.jsonl"
    torn = path.read_bytes() + b'{"unit_id": "fx0'
    path.write_bytes(torn)
    changed = {"arm": "a", "question_set": "OTHER", "docs": "d", "units": "u"}
    with pytest.raises(RunError, match="different settings"):
        go(spec(tmp_path, hashes=changed))
    assert path.read_bytes() == torn  # repair only after resuming is allowed


def test_flat_objective_falls_back() -> None:
    # identical probabilities across options: NLL is log 2 for every T, so any T "fits"; the bound
    # is exactly as good as the fit and must count as a bound hit (needs the 1e-9 tolerance)
    t, reason = cal.fit_or_fallback([[0.5, 0.5]] * 3, [0, 1, 0])
    assert t == 1.0 and reason is not None and reason.startswith("fit hit bound")


def test_run_meta_without_hashes_is_refused() -> None:
    params = cal.fit([Decision.model_validate_json(x) for x in MOCK.read_text().splitlines()],
                     {u.id: u for u in fixture_units()}, POLICY, "calib",
                     input_hashes={"decisions": "d", "units": "u"})  # fmt: skip
    with pytest.raises(sc.ScoreError, match="no units hash"):
        sc.verify_provenance(params, "u", "docs", {}, set())


def test_no_meta_override_requires_fixture_debug_calib(tmp_path: Path) -> None:
    units = tmp_path / "units.jsonl"
    write_units(fixture_units(), units)
    params = cal.fit([Decision.model_validate_json(x) for x in MOCK.read_text().splitlines()],
                     {u.id: u for u in fixture_units()}, POLICY, "calib",
                     input_hashes={"decisions": sc.sha256_file(MOCK),
                                   "units": sc.sha256_file(units)})  # fmt: skip
    c = tmp_path / "c.json"
    cal.write(params, c)  # a real (fit_on="calib") calib
    r = RUN.invoke(app, ["score", "--decisions", str(MOCK), "--units", str(units), "--calib",
                         str(c), "--out", str(tmp_path / "s.json"), "--docs",
                         str(MINI / "docs.jsonl"), "--allow-debug-calib",
                         "--allow-no-meta"])  # fmt: skip
    assert r.exit_code == 2 and "no meta.json" in r.output
