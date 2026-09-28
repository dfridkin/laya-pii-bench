"""Single CLI for every pipeline stage. Subcommands are added milestone by milestone."""

from __future__ import annotations

import hashlib
from datetime import UTC, datetime
from pathlib import Path
from typing import Annotated, Any, Literal

import typer

app = typer.Typer(no_args_is_help=True, add_completion=False, help="laya-pii-bench pipeline")


@app.callback()
def main() -> None:
    """laya-pii-bench pipeline. Each stage is a subcommand."""


@app.command()
def version() -> None:
    """Print the package version."""
    from bench import __version__

    typer.echo(__version__)


@app.command()
def hw(
    out: Annotated[Path, typer.Option(help="Where to write the fingerprint.")] = Path("hw.json"),
    models_lock: Annotated[
        Path, typer.Option(help="Checkpoint revisions from download_models.py.")
    ] = Path("models.lock.json"),
) -> None:
    """Write the hardware fingerprint (OS, CPU, RAM, torch, device, checkpoint revisions)."""
    from bench import hw as hw_mod

    info = hw_mod.write(out, models_lock)
    typer.echo(f"device={info.device} ({info.device_name}) torch={info.torch} -> {out}")


@app.command()
def validate(
    docs: Annotated[Path, typer.Argument(help="Documents JSONL to validate.")],
    policy: Annotated[Path, typer.Option(help="Label policy.")] = Path("config/policy.yaml"),
) -> None:
    """Validate documents: offsets, overlaps, enums, policy consistency."""
    from bench.config import load_policy
    from bench.validate import validate_file

    report = validate_file(docs, load_policy(policy))
    for r in report.results:
        for err in r.errors:
            typer.echo(f"line {r.line} ({r.doc_id or '?'}): {err}", err=True)
    typer.echo(f"{report.n_valid}/{len(report.results)} valid")
    if not report.ok:
        raise typer.Exit(1)


@app.command()
def schema(
    out: Annotated[Path, typer.Option(help="Directory for the JSON Schema.")] = Path("schema"),
) -> None:
    """Export the domain model as JSON Schema (input to the HUD's generated TS types)."""
    from bench.schema_export import export

    typer.echo(f"wrote {export(out)}")


@app.command("build-fixture")
def build_fixture(
    src: Annotated[Path, typer.Option(help="Hand-labeled sources.")] = Path("fixtures/mini/src"),
    out: Annotated[Path, typer.Option(help="Output JSONL.")] = Path("fixtures/mini/docs.jsonl"),
) -> None:
    """Resolve the hand-labeled fixture sources (inline sentinel markup) into docs JSONL."""
    from bench.fixture import write

    typer.echo(f"wrote {write(src, out)} docs -> {out}")


@app.command()
def gen(
    spec: Annotated[Path, typer.Option(help="Generator spec.")] = Path("config/gen_spec.yaml"),
    out: Annotated[Path, typer.Option(help="Documents JSONL.")] = Path("data/docs.jsonl"),
    policy: Annotated[Path, typer.Option(help="Label policy.")] = Path("config/policy.yaml"),
    verify_determinism: Annotated[
        bool, typer.Option(help="V6: generate twice and compare hashes.")
    ] = True,
) -> None:
    """Generate the synthetic corpus and data/gen_manifest.json; fails on any validator failure."""
    from bench import tokenize
    from bench.config import load_gen_spec, load_policy
    from bench.generate import corpus

    gs = load_gen_spec(spec)
    tok = tokenize.load("multilingual")

    def count(text: str) -> int:
        return len(tok(text))

    import hashlib

    pol = load_policy(policy)
    result = corpus.generate(gs, pol, count)
    rerun = None
    if verify_determinism:  # V6: an independent second generation must hash identically
        rerun = hashlib.sha256(
            corpus.serialize(corpus.generate(gs, pol, count).docs).encode()
        ).hexdigest()
    manifest = corpus.write(result, gs, spec, out, rerun)
    for v in manifest.validators:
        typer.echo(f"{v.name}: {'pass' if v.passed else f'FAIL ({v.failures})'}")
        for d in v.detail[:5]:
            typer.echo(f"  {d}")
    typer.echo(f"{manifest.n_docs} docs, sha256 {manifest.sha256[:16]} -> {out}")
    if not all(v.passed for v in manifest.validators):
        raise typer.Exit(1)


@app.command()
def label(
    docs: Annotated[Path, typer.Option(help="Documents JSONL.")] = Path("data/docs.jsonl"),
    policy: Annotated[Path, typer.Option(help="Label policy.")] = Path("config/policy.yaml"),
    arms: Annotated[Path, typer.Option(help="Arms config.")] = Path("config/arms.yaml"),
    arm: Annotated[list[str] | None, typer.Option(help="Arm(s) to label.")] = None,
    out: Annotated[
        Path | None, typer.Option(help="Directory for {arm}.jsonl (default: by dataset).")
    ] = None,
) -> None:
    """Segment documents into units and derive gold answers (chunk units only until M5)."""
    from bench import tokenize
    from bench.config import load_arms, load_policy
    from bench.label import label_docs, read_docs, write_units
    from bench.paths import units_dir

    out = out or units_dir(docs)

    cfg, pol, documents = load_arms(arms), load_policy(policy), read_docs(docs)
    for name in arm or [n for n, a in cfg.arms.items() if a.enabled]:
        spec = cfg.arms[name]
        tok = tokenize.load(spec.checkpoint)
        units = label_docs(documents, spec, pol, tok, tok.name)
        write_units(units, out / f"{name}.jsonl")
        n_trunc = sum(u.truncated for u in units)
        typer.echo(f"{name}: {len(units)} units ({n_trunc} truncated) -> {out / name}.jsonl")


def _run_meta(decisions: Path) -> Any:
    from bench.domain import RunMeta

    meta_path = decisions.parent / "meta.json"
    return RunMeta.model_validate_json(meta_path.read_text()) if meta_path.exists() else None


def _load_splits(splits: Path) -> Any:
    from bench.domain import Splits

    if not splits.exists():
        typer.echo(f"error: {splits} not found: run `bench split` first", err=True)
        raise typer.Exit(2)
    return Splits.model_validate_json(splits.read_text())


def _refuse_main_corpus(unit_doc_ids: set[str], flags: str) -> None:
    """D-013: fixture-only flags are refused for main-corpus units (by id; bench/guard.py)."""
    from bench.guard import main_doc_ids

    hits = main_doc_ids(unit_doc_ids)
    if hits:
        typer.echo(
            f"error: {flags} is fixture-only and these units are main-corpus documents "
            f"(e.g. {hits[0]}); refused (D-013)",
            err=True,
        )
        raise typer.Exit(2)


@app.command()
def calibrate(
    decisions: Annotated[Path, typer.Option(help="Decisions JSONL for one arm x qs.")],
    units: Annotated[Path, typer.Option(help="Units JSONL (gold answers).")],
    out: Annotated[Path, typer.Option(help="Calib params JSON to write.")],
    policy: Annotated[Path, typer.Option(help="Label policy.")] = Path("config/policy.yaml"),
    splits: Annotated[Path, typer.Option(help="Splits (fit on calib only).")] = Path(
        "data/splits.json"
    ),
    debug_fit_all: Annotated[
        bool, typer.Option(help="Fixture only: fit on every unit (no calib split). Labeled.")
    ] = False,
    allow_no_meta: Annotated[
        bool,
        typer.Option(
            help="Fixture only (with --debug-fit-all): decisions without a run meta.json."
        ),
    ] = False,
) -> None:
    """Fit temperatures and routing thresholds on the calib split only (invariant 3); write
    hashed params. Commit them with `make freeze-calib` before scoring (D-019)."""
    from bench import calibrate as cal
    from bench.config import load_policy
    from bench.label import read_units
    from bench.score import read_decisions, sha256_file

    meta = _run_meta(decisions)
    if meta is None and not (debug_fit_all and allow_no_meta):
        typer.echo(
            f"error: no meta.json next to {decisions}; units provenance can't be checked "
            "(fixture-only override: --debug-fit-all --allow-no-meta)",
            err=True,
        )
        raise typer.Exit(2)
    hashes = {"decisions": sha256_file(decisions), "units": sha256_file(units)}
    unit_list = read_units(units)
    if debug_fit_all or allow_no_meta:
        _refuse_main_corpus({u.doc_id for u in unit_list}, "--debug-fit-all/--allow-no-meta")
    if meta is not None:
        if meta.config_hashes.get("units") != hashes["units"]:
            typer.echo(
                f"error: {units} differs from the units this run was produced from", err=True
            )
            raise typer.Exit(2)
        if debug_fit_all and meta.dataset == "main":  # D-013
            typer.echo("error: --debug-fit-all is refused on the main dataset (D-013)", err=True)
            raise typer.Exit(2)
    unit_map = {u.id: u for u in unit_list}
    rows = read_decisions(decisions)
    fit_on: Literal["calib", "fixture_debug"] = "fixture_debug"
    if not debug_fit_all:
        sp = _load_splits(splits)
        if meta is not None and meta.config_hashes.get("splits") not in (None, sha256_file(splits)):
            typer.echo(f"error: {splits} differs from the splits this run used", err=True)
            raise typer.Exit(2)
        calib_units = {k: u for k, u in unit_map.items() if sp.doc_split.get(u.doc_id) == "calib"}
        rows = [d for d in rows if d.warmup or d.unit_id in calib_units]
        unit_map = calib_units
        fit_on = "calib"
    try:
        params = cal.fit(rows, unit_map, load_policy(policy), fit_on, input_hashes=hashes)
    except cal.CalibError as e:
        typer.echo(f"error: {e}", err=True)
        raise typer.Exit(2) from e
    cal.write(params, out)
    typer.echo(
        f"{params.arm}/{params.qs}: t_low={params.t_low:.4f} "
        f"t_high={'none' if params.t_high is None else f'{params.t_high:.4f}'} "
        f"fit_on={params.fit_on} calib docs={len(params.calib_doc_ids)} "
        f"hash={params.content_hash[:12]} -> {out}"
    )


@app.command("freeze-calib")
def freeze_calib(
    paths: Annotated[list[Path], typer.Argument(help="Calib params JSON files to commit.")],
) -> None:
    """Commit calib files (content hashes in the message) so `score` can verify them (D-019)."""
    from bench import calibrate as cal
    from bench import freeze

    try:
        for p in paths:
            cal.load_verified(p, allow_debug=True)  # only intact, hash-valid params get frozen
        sha = freeze.freeze(paths)
    except (cal.CalibError, freeze.FreezeError) as e:
        typer.echo(f"error: {e}", err=True)
        raise typer.Exit(2) from e
    typer.echo(
        "nothing to commit" if sha is None else f"frozen {len(paths)} calib file(s) at {sha}"
    )


@app.command("split")
def split_cmd(
    docs: Annotated[Path, typer.Option(help="Documents JSONL.")] = Path("data/docs.jsonl"),
    out: Annotated[Path, typer.Option(help="Splits JSON.")] = Path("data/splits.json"),
    units: Annotated[Path | None, typer.Option(help="Units dir (default: by dataset).")] = None,
    config: Annotated[Path, typer.Option(help="Split config.")] = Path("config/split.yaml"),
    arms: Annotated[Path, typer.Option(help="Arms config.")] = Path("config/arms.yaml"),
    qs_dir: Annotated[Path, typer.Option(help="Question sets.")] = Path("config/questions"),
    policy: Annotated[Path, typer.Option(help="Label policy.")] = Path("config/policy.yaml"),
    gen_spec: Annotated[Path, typer.Option(help="Generator spec (world, for staff).")] = Path(
        "config/gen_spec.yaml"
    ),
) -> None:
    """Assign documents to train/calib/test/holdout (site-grouped, class-complete) and write the
    label manifest. Exits 1 on any leak or any gold class missing from train/calib/test."""
    from bench import split as sp
    from bench.config import load_arms, load_gen_spec, load_question_sets, load_split
    from bench.generate.render import template_vocabulary
    from bench.generate.world import build as build_world
    from bench.label import read_docs, read_units
    from bench.paths import units_dir
    from bench.score import sha256_file

    cfg = load_split(config)
    arm_cfg = load_arms(arms, qs_dir)
    udir = units or units_dir(docs)
    enabled = [a for a, spec in arm_cfg.arms.items() if spec.enabled]
    missing_units = [a for a in enabled if not (udir / f"{a}.jsonl").exists()]
    if missing_units:
        typer.echo(
            f"error: no units for {missing_units} in {udir}: run `bench label` first", err=True
        )
        raise typer.Exit(2)
    documents = read_docs(docs)
    units_by_arm = {a: read_units(udir / f"{a}.jsonl") for a in enabled}
    qsets = {
        q: s for q, s in load_question_sets(qs_dir).items() if q in arm_cfg.defaults.question_sets
    }
    splits, summary = sp.build(documents, units_by_arm, qsets, cfg, sha256_file(docs),
                               sha256_file(config))  # fmt: skip
    out.parent.mkdir(parents=True, exist_ok=True)
    body = splits.model_dump_json(indent=2) + "\n"
    out.write_text(body, encoding="utf-8")
    man = sp.manifest(units_by_arm, splits, qsets, sha256_file(docs), sha256_file(policy),
                      sp.sha256_text(body),
                      {a: sha256_file(udir / f"{a}.jsonl") for a in enabled})  # fmt: skip
    man_path = out.parent / "label_manifest.json"
    man_path.write_text(man.model_dump_json(indent=2) + "\n", encoding="utf-8")
    typer.echo(f"splits {dict(splits.counts)} -> {out}; manifest -> {man_path}")
    typer.echo(f"search: {summary}")
    for a, st in man.arms.items():
        typer.echo(f"  {a}: {st.n_units} units {dict(st.by_split)} truncated {dict(st.truncated)}")
    world = build_world(load_gen_spec(gen_spec), frozenset(template_vocabulary()))
    leaks = sp.leakage(splits, documents) + sp.staff_leakage(
        splits, documents, sp.staff_sites(world)
    )
    for x in leaks:
        typer.echo(f"LEAK {x}", err=True)
    for x in man.missing:
        typer.echo(f"MISSING {x}", err=True)
    typer.echo(f"holdout classes missing (reported, D-005): {len(man.holdout_missing)}")
    if leaks or man.missing:
        raise typer.Exit(1)


@app.command("run")
def run_cmd(
    arm: Annotated[str, typer.Option(help="Arm name from config/arms.yaml.")],
    qs: Annotated[str, typer.Option(help="Question set id (config/questions/{qs}.yaml).")],
    docs: Annotated[Path, typer.Option(help="Documents JSONL.")] = Path("data/docs.jsonl"),
    units: Annotated[Path | None, typer.Option(help="Units JSONL (default: by dataset).")] = None,
    out: Annotated[Path | None, typer.Option(help="Run directory (default: by dataset).")] = None,
    batch_size: Annotated[int, typer.Option(help="1 = headline batch-1 mode.")] = 1,
    warmup_docs: Annotated[Path, typer.Option(help="Warmup text source.")] = Path(
        "fixtures/mini/docs.jsonl"
    ),
    arms: Annotated[Path, typer.Option(help="Arms config.")] = Path("config/arms.yaml"),
    qs_dir: Annotated[Path, typer.Option(help="Question sets.")] = Path("config/questions"),
    models_lock: Annotated[Path, typer.Option(help="Pinned checkpoints.")] = Path(
        "models.lock.json"
    ),
    splits: Annotated[Path, typer.Option(help="Splits (main dataset only).")] = Path(
        "data/splits.json"
    ),
) -> None:
    """Run one arm x question set over units: raw probabilities, honest timing, resumable."""
    import json

    from bench import hw as hw_mod
    from bench.config import load_arms, load_question_set
    from bench.label import read_docs, read_units
    from bench.laya_client import LayaClient
    from bench.paths import dataset_name, run_dir, units_dir
    from bench.questions import build
    from bench.run import RunSpec
    from bench.run import run as do_run
    from bench.score import sha256_file

    cfg = load_arms(arms, qs_dir)
    if arm not in cfg.arms or not cfg.arms[arm].enabled:
        raise typer.BadParameter(f"arm {arm!r} is not an enabled arm in {arms}")
    spec_arm, dataset = cfg.arms[arm], dataset_name(docs)
    if batch_size < 1:
        raise typer.BadParameter("batch size must be >= 1")
    units = units or units_dir(docs) / f"{arm}.jsonl"
    if not units.exists():
        typer.echo(
            f"{units} not found: run `bench label --docs {docs} --arm {arm}` first", err=True
        )
        raise typer.Exit(2)
    out = out or run_dir(docs, arm, qs, batch_size)
    qs_path = qs_dir / f"{qs}.yaml"
    qset = load_question_set(qs_path)
    questions = build(qset, spec_arm.checkpoint)  # rejects noul on English before loading
    doc_map = {d.id: d for d in read_docs(docs)}
    unit_list = read_units(units)
    missing = sorted({u.doc_id for u in unit_list} - set(doc_map))
    if missing:
        raise typer.BadParameter(f"units reference docs not in {docs}: {missing[:3]}")
    split_hash: dict[str, str] = {}
    if dataset != "main":
        from bench.guard import main_doc_ids

        hits = main_doc_ids(u.doc_id for u in unit_list)
        if hits:
            typer.echo(
                f"error: {docs} holds main-corpus documents (e.g. {hits[0]}); run them as "
                "data/docs.jsonl so the split filter applies (D-013)",
                err=True,
            )
            raise typer.Exit(2)
    if dataset == "main":  # only the configured splits; train is never run zero-shot
        sp = _load_splits(splits)
        if sp.docs_sha256 != sha256_file(docs):
            typer.echo(f"error: {splits} was built from different documents", err=True)
            raise typer.Exit(2)
        keep = set(cfg.defaults.splits_to_run)
        unit_list = [u for u in unit_list if sp.doc_split[u.doc_id] in keep]
        split_hash = {"splits": sha256_file(splits)}
    texts = {u.id: doc_map[u.doc_id].text[u.start : u.end] for u in unit_list}
    arm_json = json.dumps(spec_arm.model_dump(mode="json"), sort_keys=True).encode()
    hashes = {
        "arm": hashlib.sha256(arm_json).hexdigest(),
        "question_set": sha256_file(qs_path),
        "docs": sha256_file(docs),
        "units": sha256_file(units),
        **split_hash,
    }
    spec = RunSpec(
        arm=arm, qs=qset, questions=questions, checkpoint=spec_arm.checkpoint,
        max_len=spec_arm.max_len, dataset=dataset, out_dir=out, batch_size=batch_size,
        warmup_calls=cfg.defaults.warmup_calls, config_hashes=hashes,
    )  # fmt: skip
    device = None if cfg.defaults.device == "auto" else cfg.defaults.device
    out.mkdir(parents=True, exist_ok=True)
    log_file = (out / "run.log").open("a", encoding="utf-8")

    def log(msg: str) -> None:
        line = f"{datetime.now(UTC).isoformat(timespec='seconds')} {msg}"
        typer.echo(line)
        log_file.write(line + "\n")
        log_file.flush()

    def factory() -> LayaClient:
        return LayaClient(spec_arm.checkpoint, questions, spec_arm.max_len,
                          spec_arm.head_max_len, models_lock, device)  # fmt: skip

    try:
        do_run(spec, unit_list, texts, [d.text for d in read_docs(warmup_docs)], factory,
               hw_mod.collect(models_lock), log)  # fmt: skip
    finally:
        log_file.close()


@app.command()
def score(
    decisions: Annotated[Path, typer.Option(help="Decisions JSONL for one arm x qs.")],
    units: Annotated[Path, typer.Option(help="Units JSONL (gold answers).")],
    calib: Annotated[Path, typer.Option(help="Frozen calib params JSON (hash-checked).")],
    out: Annotated[Path, typer.Option(help="Scores JSON to write.")],
    docs: Annotated[Path, typer.Option(help="Documents JSONL.")] = Path("data/docs.jsonl"),
    policy: Annotated[Path, typer.Option(help="Label policy.")] = Path("config/policy.yaml"),
    hw: Annotated[
        Path | None,
        typer.Option(help="Hardware fingerprint, only if the run has no meta.json next to it."),
    ] = None,
    allow_debug_calib: Annotated[
        bool, typer.Option(help="Accept fit_on=fixture_debug calib (fixture runs only).")
    ] = False,
    allow_no_meta: Annotated[
        bool,
        typer.Option(help="Fixture only (with --allow-debug-calib): decisions without meta.json."),
    ] = False,
    splits: Annotated[Path, typer.Option(help="Splits (scores test and holdout).")] = Path(
        "data/splits.json"
    ),
) -> None:
    """Score decisions against gold with frozen calib params. Refuses a calib hash mismatch and a
    calib file that isn't committed unmodified at HEAD (D-019)."""
    from bench import calibrate as cal
    from bench import freeze
    from bench import score as sc
    from bench.config import load_policy
    from bench.domain import HwInfo
    from bench.label import read_docs, read_units
    from bench.score import sha256_file as sha256_file_

    try:
        params = cal.load_verified(calib, allow_debug=allow_debug_calib)
    except cal.CalibError as e:
        typer.echo(f"error: {e}", err=True)
        raise typer.Exit(2) from e
    if allow_debug_calib or allow_no_meta or params.fit_on != "calib":
        _refuse_main_corpus(
            {u.doc_id for u in read_units(units)}, "--allow-debug-calib/--allow-no-meta"
        )
    from bench.domain import RunMeta

    meta_path = decisions.parent / "meta.json"
    extra_caveats: list[str] = []
    if not meta_path.exists():
        if not (allow_no_meta and params.fit_on == "fixture_debug"):
            typer.echo(
                f"error: no meta.json next to {decisions}; units/docs provenance can't be checked "
                "(fixture-only override: --allow-debug-calib --allow-no-meta)",
                err=True,
            )
            raise typer.Exit(2)
        extra_caveats.append(
            "Decisions have no run meta.json (--allow-no-meta): units/docs were not checked "
            "against the run that produced them."
        )
    hw_info: HwInfo | None = None
    run_hashes: dict[str, str] | None = None
    run_batch_size = None
    if meta_path.exists():  # the run's own hardware, with the device it actually used
        meta = RunMeta.model_validate_json(meta_path.read_text())
        hw_info = meta.hw.model_copy(update={"device": meta.device})
        run_hashes = meta.config_hashes
        run_batch_size: int | None = meta.batch_size
        if meta.dataset == "main" and params.fit_on == "fixture_debug":  # D-013
            typer.echo("error: a fixture_debug calib is refused on the main dataset", err=True)
            raise typer.Exit(2)
        if params.fit_on == "calib" and run_hashes.get("splits") != sha256_file_(splits):
            typer.echo(f"error: {splits} differs from the splits this run used", err=True)
            raise typer.Exit(2)
    elif hw is not None and hw.exists():
        hw_info = HwInfo.model_validate_json(hw.read_text())
    documents = read_docs(docs)
    if params.fit_on == "fixture_debug":
        split_docs = {"fixture": {d.id for d in documents}}
    else:  # the sealed splits: test (headline) and holdout (IRB letters), never calib or train
        sp = _load_splits(splits)
        if sp.docs_sha256 != sha256_file_(docs):
            typer.echo(f"error: {splits} was built from different documents", err=True)
            raise typer.Exit(2)
        split_docs = {
            s: {d for d, x in sp.doc_split.items() if x == s} for s in ("test", "holdout")
        }
        unit_docs = {u.doc_id for u in read_units(units)}
        split_docs = {k: v for k, v in split_docs.items() if v & unit_docs}
    hashes = {k: sc.sha256_file(p) for k, p in (("docs", docs), ("units", units),
                                                ("decisions", decisions))}  # fmt: skip
    scored = sc.disjointness_scope(split_docs)
    try:
        sc.verify_provenance(params, hashes["units"], hashes["docs"], run_hashes, scored)
        rows = sc.read_decisions(decisions)
        if run_batch_size is not None:
            sc.verify_run_rows(rows, run_batch_size)
        commit = freeze.require_committed(calib)  # last check: every other refusal comes first
        scores = sc.score(rows, read_units(units), documents, params,
                          load_policy(policy), split_docs, hw_info, hashes,
                          extra_caveats, commit)  # fmt: skip
    except (sc.ScoreError, freeze.FreezeError) as e:
        typer.echo(f"error: {e}", err=True)
        raise typer.Exit(2) from e
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(scores.model_dump_json(indent=2) + "\n", encoding="utf-8")
    for name, sp in scores.splits.items():
        h = sp.headline
        rec = "n/a" if h.recall is None else f"{h.recall.point:.4f}"
        typer.echo(f"{name}: recall@t_low={rec} forward_rate={h.forward_rate.point:.4f} "
                   f"false_forwards={h.false_forwards} -> {out}")  # fmt: skip


@app.command()
def report(
    scores: Annotated[list[Path] | None, typer.Option(help="Scores JSON files.")] = None,
    scores_dir: Annotated[Path, typer.Option(help="Used when --scores is not given.")] = Path(
        "scores"
    ),
    out: Annotated[Path, typer.Option(help="Report markdown.")] = Path("reports/report.md"),
    hud: Annotated[Path | None, typer.Option(help="HUD replay export (M7).")] = None,
) -> None:
    """Render the markdown report from scores."""
    from bench import report as rep

    paths = scores or sorted(scores_dir.glob("*.json"))
    if not paths:
        typer.echo(f"error: no scores given and none in {scores_dir}/", err=True)
        raise typer.Exit(2)
    rep.write(rep.read_scores(paths), out)
    typer.echo(f"wrote {out} from {len(paths)} scores file(s)")
    if hud is not None:
        typer.echo(f"note: HUD replay export arrives in M7; {hud} not written", err=True)


if __name__ == "__main__":
    app()
