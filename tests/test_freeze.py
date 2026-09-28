"""M5 gate 5 (D-019): score refuses calib that isn't committed unmodified at HEAD and records the
commit; calibrate fits on the calib split only and score scores the sealed splits (D-013)."""

import json
import subprocess
from datetime import datetime
from pathlib import Path

import pytest
from typer.testing import CliRunner

from bench import freeze
from bench import score as sc
from bench.cli import app
from bench.domain import CalibParams, HwInfo, RunMeta, Scores, Split, Splits
from bench.label import read_docs, write_units
from tests.fixture_expected import fixture_units
from tests.gitutil import commit_file, git, init_repo

ROOT = Path(__file__).resolve().parent.parent
MINI = ROOT / "fixtures" / "mini"
DOCS = MINI / "docs.jsonl"
MOCK = MINI / "decisions_mock.jsonl"
RUN = CliRunner()
HW = HwInfo(os="o", arch="a", cpu="c", ram_gb=8, python="p", torch="t", laya="l", device="mps",
            device_name="n", checkpoints={}, created_at="x")  # fmt: skip


def _splits(path: Path) -> Path:
    """Site 1001 is calib, everything else test (a toy stand-in for `bench split`)."""
    doc_split: dict[str, Split] = {
        d.id: "calib" if d.world_refs.site == "1001" else "test" for d in read_docs(DOCS)
    }
    sp = Splits(seed=0, docs_sha256=sc.sha256_file(DOCS), config_sha256="x", doc_split=doc_split,
                groups={}, counts={s: sum(v == s for v in doc_split.values())
                                   for s in ("train", "calib", "test", "holdout")})  # fmt: skip
    path.write_text(sp.model_dump_json())
    return path


def _run(tmp: Path, dataset: str = "mini", with_splits: bool = True) -> dict[str, Path]:
    run_dir = tmp / "run"
    run_dir.mkdir()
    units = tmp / "units.jsonl"
    write_units(fixture_units(), units)
    (run_dir / "decisions.jsonl").write_text(MOCK.read_text())
    splits = _splits(tmp / "splits.json")
    hashes = {"units": sc.sha256_file(units), "docs": sc.sha256_file(DOCS)}
    if with_splits:
        hashes["splits"] = sc.sha256_file(splits)
    meta = RunMeta(arm="mock", qs="qs_v1", dataset=dataset, hw=HW, device="mps",
                   checkpoint="english", checkpoint_rev="r", config_hashes=hashes,
                   batch_size=1, warmup_calls=2, sessions=1, started_at="x",
                   finished_at="y")  # fmt: skip
    (run_dir / "meta.json").write_text(meta.model_dump_json())
    calib_dir = tmp / "repo"
    calib_dir.mkdir()
    return {"dec": run_dir / "decisions.jsonl", "units": units, "splits": splits,
            "calib": calib_dir / "mock__qs_v1.json", "out": tmp / "s.json"}  # fmt: skip


def _calibrate(p: dict[str, Path], *extra: str) -> str:
    args = ["calibrate", "--decisions", str(p["dec"]), "--units", str(p["units"]),
            "--out", str(p["calib"]), "--splits", str(p["splits"]), *extra]  # fmt: skip
    r = RUN.invoke(app, args)
    return f"{r.exit_code}:{r.output}"


def _score(p: dict[str, Path]) -> tuple[int, str]:
    r = RUN.invoke(app, ["score", "--decisions", str(p["dec"]), "--units", str(p["units"]),
                         "--calib", str(p["calib"]), "--out", str(p["out"]), "--docs", str(DOCS),
                         "--splits", str(p["splits"])])  # fmt: skip
    return r.exit_code, r.output


@pytest.fixture
def run(tmp_path: Path) -> dict[str, Path]:
    p = _run(tmp_path)
    assert _calibrate(p).startswith("0:"), _calibrate(p)
    return p


def test_calibrate_fits_on_calib_split_only(run: dict[str, Path]) -> None:
    params = CalibParams.model_validate_json(run["calib"].read_text())
    calib_docs = {d for d, s in Splits.model_validate_json(run["splits"].read_text())
                  .doc_split.items() if s == "calib"}  # fmt: skip
    assert params.fit_on == "calib"
    assert params.calib_doc_ids and set(params.calib_doc_ids) <= calib_docs


def test_uncommitted_calib_is_refused(run: dict[str, Path]) -> None:
    code, out = _score(run)  # not even in a repository
    assert code == 2 and "not inside a git repository" in out and not run["out"].exists()
    init_repo(run["calib"].parent)
    code, out = _score(run)  # in a repository, untracked
    assert code == 2 and "not committed" in out and not run["out"].exists()


def test_modified_calib_is_refused(run: dict[str, Path]) -> None:
    commit_file(run["calib"])
    body = json.loads(run["calib"].read_text())
    run["calib"].write_text(json.dumps(body, indent=4))  # same content hash, different bytes
    code, out = _score(run)
    assert code == 2 and "differs from its committed version" in out and not run["out"].exists()


def test_committed_calib_is_scored_with_its_commit(run: dict[str, Path]) -> None:
    sha = commit_file(run["calib"])
    code, out = _score(run)
    assert code == 0, out
    s = Scores.model_validate_json(run["out"].read_text())
    assert s.context.calib_commit == sha and s.context.calib_committed_at
    # M6 gate 2: the calib commit is strictly older than the scores (sub-second created_at)
    assert datetime.fromisoformat(s.context.calib_committed_at) < datetime.fromisoformat(
        s.context.created_at
    )
    assert list(s.splits) == ["test"]  # the sealed split only: no calib, no fixture-wide score
    assert not any("not verified" in c for c in s.caveats)


def test_score_refuses_splits_other_than_the_runs(run: dict[str, Path]) -> None:
    commit_file(run["calib"])
    sp = Splits.model_validate_json(run["splits"].read_text())
    run["splits"].write_text(sp.model_copy(update={"seed": 1}).model_dump_json())
    code, out = _score(run)
    assert code == 2 and "differs from the splits this run used" in out


def test_debug_fit_refused_on_main_dataset(tmp_path: Path) -> None:
    p = _run(tmp_path, dataset="main")
    out = _calibrate(p, "--debug-fit-all", "--docs", str(MINI / "docs.jsonl"))
    assert out.startswith("2:") and "D-013" in out and not p["calib"].exists()


def test_freeze_commits_with_content_hash(run: dict[str, Path]) -> None:
    repo = init_repo(run["calib"].parent)
    git(repo, "config", "user.name", "t")
    git(repo, "config", "user.email", "t@example.invalid")
    git(repo, "config", "commit.gpgsign", "false")
    r = RUN.invoke(app, ["freeze-calib", str(run["calib"])])
    assert r.exit_code == 0, r.output
    h = json.loads(run["calib"].read_text())["content_hash"]
    msg = subprocess.run(["git", "log", "-1", "--format=%B"], cwd=repo, capture_output=True,
                         text=True, check=True).stdout  # fmt: skip
    assert h in msg
    assert freeze.require_committed(run["calib"])[0] == git(repo, "rev-parse", "HEAD")
    assert freeze.freeze([run["calib"]]) is None  # nothing new to commit


def test_freeze_refuses_tampered_params(run: dict[str, Path]) -> None:
    body = json.loads(run["calib"].read_text())
    body["t_low"] = 0.01
    run["calib"].write_text(json.dumps(body))
    r = RUN.invoke(app, ["freeze-calib", str(run["calib"])])
    assert r.exit_code == 2 and "hash" in r.output


def test_calib_committed_in_another_repo_is_refused(
    run: dict[str, Path], tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    commit_file(run["calib"])
    project = tmp_path / "project"
    project.mkdir()
    git(project, "init", "-q")
    monkeypatch.setattr(freeze, "project_root", lambda: project)
    code, out = _score(run)
    assert code == 2 and "not in the project repository" in out and not run["out"].exists()


def test_skip_worktree_does_not_hide_an_edit(run: dict[str, Path]) -> None:
    commit_file(run["calib"])
    repo = run["calib"].parent
    git(repo, "update-index", "--skip-worktree", run["calib"].name)
    body = json.loads(run["calib"].read_text())
    run["calib"].write_text(json.dumps(body, indent=4))
    assert git(repo, "diff", "--name-only") == ""  # git itself no longer sees the edit
    code, out = _score(run)
    assert code == 2 and "differs from its committed version" in out


def test_staged_but_uncommitted_calib_is_refused(run: dict[str, Path]) -> None:
    repo = init_repo(run["calib"].parent)
    git(repo, "add", run["calib"].name)
    code, out = _score(run)
    assert code == 2 and "not committed" in out


# --- D-013: fixture-only flags never reach the main corpus ---

MAIN = ROOT / "data" / "docs.jsonl"
needs_main = pytest.mark.skipif(
    not (ROOT / "data" / "units" / "B4.jsonl").exists(), reason="main corpus not generated"
)


def test_score_refuses_debug_calib_on_main_run_meta(tmp_path: Path) -> None:
    p = _run(tmp_path, dataset="main")
    assert _calibrate(p, "--debug-fit-all", "--docs", str(DOCS)).startswith("2:")
    (tmp_path / "fx").mkdir()
    q = _run(tmp_path / "fx")  # a fixture_debug calib from a fixture run
    assert _calibrate(q, "--debug-fit-all", "--docs", str(DOCS)).startswith("0:")
    commit_file(q["calib"])
    p["calib"] = q["calib"]
    r = RUN.invoke(app, ["score", "--decisions", str(p["dec"]), "--units", str(p["units"]),
                         "--calib", str(p["calib"]), "--out", str(p["out"]), "--docs", str(DOCS),
                         "--allow-debug-calib"])  # fmt: skip
    assert r.exit_code == 2 and "fixture_debug calib is refused on the main dataset" in r.output


def _main_copy(tmp: Path) -> tuple[Path, Path, Path]:
    """Main-corpus docs copied under another name, a slice of its units, and meta-less decisions."""
    copy = tmp / "renamed" / "docs.jsonl"
    copy.parent.mkdir(parents=True)
    copy.write_bytes(MAIN.read_bytes())
    units = tmp / "units.jsonl"
    lines = (ROOT / "data" / "units" / "B4.jsonl").read_text().splitlines()[:20]
    units.write_text("\n".join(lines) + "\n")
    dec = tmp / "nometa" / "decisions.jsonl"
    dec.parent.mkdir()
    dec.write_text(MOCK.read_text())
    return copy, units, dec


@needs_main
def test_calibrate_refuses_debug_flags_on_main_corpus_without_meta(tmp_path: Path) -> None:
    copy, units, dec = _main_copy(tmp_path)
    for docs in (MAIN, copy):
        r = RUN.invoke(app, ["calibrate", "--decisions", str(dec), "--units", str(units),
                             "--out", str(tmp_path / "c.json"), "--docs", str(docs),
                             "--debug-fit-all", "--allow-no-meta"])  # fmt: skip
        assert r.exit_code == 2 and "D-013" in r.output and not (tmp_path / "c.json").exists()


@needs_main
def test_score_refuses_debug_flags_on_main_corpus_without_meta(
    run: dict[str, Path], tmp_path: Path
) -> None:
    commit_file(run["calib"])  # a real, committed calib; the units are the problem
    copy, units, dec = _main_copy(tmp_path)
    for docs in (MAIN, copy):
        r = RUN.invoke(app, ["score", "--decisions", str(dec), "--units", str(units), "--calib",
                             str(run["calib"]), "--out", str(tmp_path / "s.json"), "--docs",
                             str(docs), "--allow-debug-calib", "--allow-no-meta"])  # fmt: skip
        assert r.exit_code == 2 and "D-013" in r.output and not (tmp_path / "s.json").exists()


@needs_main
def test_run_refuses_main_corpus_under_another_name(tmp_path: Path) -> None:
    copy, units, _ = _main_copy(tmp_path)
    r = RUN.invoke(app, ["run", "--arm", "B4", "--qs", "qs_v1", "--docs", str(copy), "--units",
                         str(units), "--out", str(tmp_path / "run")])  # fmt: skip
    assert r.exit_code == 2 and "main-corpus documents" in r.output
    assert not (tmp_path / "run").exists()
