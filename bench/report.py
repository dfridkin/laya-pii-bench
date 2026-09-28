"""Report stage: `reports/report.md` from scores (one section per docs/specs/metrics.md section)."""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from pathlib import Path

from bench.domain import (
    CalibrationMetrics,
    Headline,
    Interval,
    LatencyStats,
    QuestionMetrics,
    Route,
    Scores,
)
from bench.score import D008_GAP, d008_gap

SECTIONS = (
    "Run context",
    "Headline operating point",
    "Per-question",
    "Calibration",
    "Routing",
    "Speed",
    "Slices",
    "Failure gallery",
    "Caveats",
)


def _f(x: float | None, nd: int = 4) -> str:
    return "n/a" if x is None else f"{x:.{nd}f}"


def _ci(i: Interval | None) -> str:
    if i is None:
        return "n/a"
    if i.lo is None or i.hi is None:
        return f"{_f(i.point)} (CI n/a)"
    return f"{_f(i.point)} [{_f(i.lo)}, {_f(i.hi)}]"


def _table(header: Sequence[str], rows: Iterable[Sequence[object]]) -> list[str]:
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return [*out, ""]


def _label(s: Scores) -> str:
    tag = " (doc-level, underpowered)" if s.context.doc_level else ""
    return f"{s.context.arm} / {s.context.qs}{tag}"


def _gap(h: Headline) -> str:
    """D-008: point recall minus its exact 95% lower bound, flagged above the review gap."""
    g = d008_gap(h)
    if g is None:
        return "n/a"
    return f"{g:.4f}" + (" **review**" if g > D008_GAP else "")


def _run_context(all_scores: Sequence[Scores]) -> list[str]:
    out: list[str] = []
    for s in all_scores:
        c = s.context
        hw = f"{c.hw.cpu}, {c.hw.ram_gb} GB, {c.hw.device}, {c.hw.os}" if c.hw else "not recorded"
        out += [f"### {_label(s)}", ""]
        out += _table(
            ["field", "value"],
            [
                ("arm", c.arm),
                ("question set", c.qs),
                ("splits", ", ".join(c.splits)),
                ("docs sha256", f"`{c.docs_sha256}`"),
                ("units sha256", f"`{c.units_sha256}`"),
                ("decisions sha256", f"`{c.decisions_sha256}`"),
                ("calib hash / fit_on", f"`{c.calib_hash[:16]}` / {c.calib_fit_on}"),
                ("calib commit (D-019)", f"`{c.calib_commit[:12]}` {c.calib_committed_at}"),
                (
                    "temperature fallbacks (T = 1)",
                    "; ".join(f"{k}: {v}" for k, v in c.calib_temperature_fallbacks.items())
                    or "none",
                ),
                ("hardware", hw),
                ("laya version", c.laya_version),
                ("checkpoints", ", ".join(c.checkpoints)),
                ("checkpoint revisions", ", ".join(c.checkpoint_revs)),
                ("date", c.created_at),
            ],
        )
    return out


def _headline(all_scores: Sequence[Scores]) -> list[str]:
    rows: list[Sequence[object]] = []
    for s in all_scores:
        for split, sp in s.splits.items():
            h = sp.headline
            rows.append(
                (
                    _label(s),
                    split,
                    _f(h.t_low),
                    _f(h.t_high) if h.t_high is not None else "none",
                    _ci(h.recall),
                    _f(h.recall_exact_lo),
                    _gap(h),
                    _f(h.route_recall),
                    _ci(h.forward_rate),
                    h.false_forwards,
                    _f(h.precision),
                    f"{h.n_units} / {h.n_docs} / {h.n_positive}",
                )
            )
    return [
        "pii_present recall at the calib-fit `t_low` (95% document-level bootstrap CI). The exact "
        "lower bound is Clopper-Pearson on unit counts (ignores clustering within documents; "
        "informative when there are no misses). Route recall counts misses after routing "
        "(1 - false forwards / positives). t_high `none`: no threshold reached the precision "
        f"target, so only the role rule redacts. `point - exact lo` above {D008_GAP} flags "
        "D-008 for review. Doc-level arms are underpowered (few units per document).",
        "",
        *_table(
            [
                "arm / qs",
                "split",
                "t_low",
                "t_high",
                "recall",
                "recall exact lo",
                "point - exact lo",
                "route recall",
                "forward rate",
                "false forwards",
                "precision",
                "units / docs / positives",
            ],
            rows,
        ),
    ]


def _confusion(m: QuestionMetrics) -> list[str]:
    labels = m.confusion.labels
    return _table(
        ["gold \\ pred", *labels],
        [(g, *m.confusion.counts[i]) for i, g in enumerate(labels)],
    )


def _per_question(all_scores: Sequence[Scores]) -> list[str]:
    out: list[str] = []
    for s in all_scores:
        for split, sp in s.splits.items():
            out += [f"### {_label(s)}, {split}", ""]
            out += _table(
                ["question", "n", "accuracy", "macro-F1", "majority baseline"],
                [
                    (
                        q,
                        m.n,
                        _f(m.accuracy),
                        _f(m.macro_f1),
                        f"{_f(m.majority_baseline_accuracy)} ({m.majority_class})",
                    )
                    for q, m in sp.per_question.items()
                ],
            )
            if sp.multilabel:
                ml = sp.multilabel
                out += [f"Multi-label categories: micro-F1 {_f(ml.micro_f1)}, macro-F1 "
                        f"{_f(ml.macro_f1)}.", ""]  # fmt: skip
            for q, m in sp.per_question.items():
                out += [f"Confusion, `{q}`:", "", *_confusion(m)]
    return out + _qs_comparison(all_scores)


def _qs_comparison(all_scores: Sequence[Scores]) -> list[str]:
    """qs_v1 vs qs_v2 on the same arm and split (metrics spec): pii_present identically; the
    category question as qs_v1 single-label macro-F1 vs qs_v2 multi-label micro/macro-F1."""
    by: dict[tuple[str, str], dict[str, Scores]] = {}
    for s in all_scores:
        for split in s.splits:
            by.setdefault((s.context.arm, split), {})[s.context.qs] = s
    rows: list[Sequence[object]] = []
    for (arm, split), qs in sorted(by.items()):
        if len(qs) < 2:
            continue
        for name in sorted(qs):
            sp = qs[name].splits[split]
            pii, h = sp.per_question.get("pii_present"), sp.headline
            cat = sp.per_question.get("category")
            ml = sp.multilabel
            rows.append((arm, split, name, _f(pii.accuracy) if pii else "n/a",
                         _f(pii.macro_f1) if pii else "n/a", _ci(h.recall), _ci(h.forward_rate),
                         _f(cat.macro_f1) if cat else "n/a",
                         f"{_f(ml.micro_f1)} / {_f(ml.macro_f1)}" if ml else "n/a"))  # fmt: skip
    if not rows:
        return []
    return [
        "### qs_v1 vs qs_v2",
        "",
        "Same arm and split under both question sets. `pii_present` is the same question in both; "
        "categories are single-label in qs_v1 (`category`) and per-category yes/no in qs_v2.",
        "",
        *_table(
            [
                "arm",
                "split",
                "qs",
                "pii_present acc",
                "pii_present macro-F1",
                "recall",
                "forward rate",
                "category macro-F1 (qs_v1)",
                "categories micro / macro-F1 (qs_v2)",
            ],
            rows,
        ),
    ]


def _calibration(all_scores: Sequence[Scores]) -> list[str]:
    out: list[str] = [
        "ECE uses 15 equal-width bins on the max probability. Brier is multi-class. AUROC scores "
        "correctness by the max probability.",
        "",
    ]
    for s in all_scores:
        for split, sp in s.splits.items():
            out += [f"### {_label(s)}, {split}", ""]
            out += _table(
                ["question", "ECE raw", "ECE cal", "Brier raw", "Brier cal", "AUROC raw",
                 "AUROC cal"],
                [
                    (q, _f(c.ece_raw), _f(c.ece_calibrated), _f(c.brier_raw),
                     _f(c.brier_calibrated), _f(c.auroc_raw), _f(c.auroc_calibrated))
                    for q, c in sp.calibration.items()
                ],
            )  # fmt: skip
            out += _reliability(sp.calibration)
    return out


def _reliability(cal: dict[str, CalibrationMetrics]) -> list[str]:
    out: list[str] = []
    for q, c in cal.items():
        rows = [
            (f"[{r.lo:.3f}, {r.hi:.3f})", r.n, _f(r.mean_confidence), _f(r.accuracy),
             c.reliability_calibrated[i].n, _f(c.reliability_calibrated[i].mean_confidence),
             _f(c.reliability_calibrated[i].accuracy))
            for i, r in enumerate(c.reliability_raw)
            if r.n or c.reliability_calibrated[i].n
        ]  # fmt: skip
        out += [
            f"Reliability data, `{q}` (non-empty bins):",
            "",
            *_table(["bin", "n raw", "conf raw", "acc raw", "n cal", "conf cal", "acc cal"], rows),
        ]
    return out


def _routing(all_scores: Sequence[Scores]) -> list[str]:
    out: list[str] = []
    for s in all_scores:
        for split, sp in s.splits.items():
            r = sp.routing
            out += [f"### {_label(s)}, {split}", ""]
            out += _table(
                ["gold pii_present", *[x.value for x in Route], "total"],
                [
                    (g, *[r.by_gold_pii[g][x] for x in Route], sum(r.by_gold_pii[g].values()))
                    for g in ("A", "B")
                ]
                + [("all", *[r.counts[x] for x in Route], sum(r.counts.values()))],
            )
            out += _table(["trigger", "count"], sorted(r.triggers.items()))
    return out


def _lat(name: str, x: LatencyStats | None) -> Sequence[object]:
    if x is None:
        return (name, 0, "n/a", "n/a", "n/a", "n/a", "n/a")
    return (name, x.n, _f(x.p50_ms, 1), _f(x.p95_ms, 1), _f(x.p99_ms, 1), _f(x.mean_ms, 1),
            _f(x.units_per_sec, 2))  # fmt: skip


def _speed(all_scores: Sequence[Scores]) -> list[str]:
    out: list[str] = []
    for s in all_scores:
        sp = s.speed
        out += [f"### {_label(s)}", "", f"Hardware: **{sp.hardware}**. "
                f"Warmup calls excluded: {sp.warmup_excluded}. laya autocast: batch-1 "
                f"{sp.batch1_autocast}, batched {sp.batched_autocast} (on MPS, fp16 autocast "
                "starts at 5 question rows, so qs_v2 runs fp16 and qs_v1 fp32).", ""]  # fmt: skip
        out += _table(
            ["mode", "n", "p50 ms", "p95 ms", "p99 ms", "mean ms", "per sec"],
            [
                _lat("per unit, batch-1", sp.batch1),
                _lat("per unit, batched", sp.batched),
                _lat("per document (sum of units, batch-1)", sp.per_doc_ms),
            ],
        )
    return out


def _slices(all_scores: Sequence[Scores]) -> list[str]:
    out: list[str] = ["Slices with n < 30 are marked `*`.", ""]
    for s in all_scores:
        for split, sp in s.splits.items():
            out += [f"### {_label(s)}, {split}", ""]
            out += _table(
                ["dimension", "value", "units", "docs", "positives", "recall", "forward rate",
                 "false fwd", "pii acc"],
                [
                    (r.dimension, r.value + (" *" if r.small_sample else ""), r.n_units, r.n_docs,
                     r.n_positive, _f(r.recall), _f(r.forward_rate), r.false_forwards,
                     _f(r.pii_accuracy))
                    for r in sp.slices
                ],
            )  # fmt: skip
            kinds = sp.false_forward_value_kinds
            out += ["Value kinds of missed spans (false forwards):", ""]
            out += (
                _table(["value_kind", "false forwards"], sorted(kinds.items()))
                if kinds
                else ["none", ""]
            )
    return out


def _failures(all_scores: Sequence[Scores]) -> list[str]:
    out: list[str] = []
    for s in all_scores:
        for split, sp in s.splits.items():
            out += [f"### {_label(s)}, {split}: {len(sp.failures)} false forward(s)", ""]
            for f in sp.failures:
                p = f.calibrated_probs["pii_present"]
                raw = f.raw_probs["pii_present"]
                out += [
                    f"**{f.unit_id}** route {f.route.value} ({', '.join(f.triggers)}); "
                    f"p(pii) raw {_f(raw['A'])}, calibrated {_f(p['A'])}; gold role "
                    f"{f.gold.subject_role}, category {f.gold.category}; missed "
                    f"{', '.join(f.missed_value_kinds) or 'n/a'}",
                    "",
                    f.text_markdown,
                    "",
                ]
    return out


def _caveats(all_scores: Sequence[Scores]) -> list[str]:
    out: list[str] = []
    for s in all_scores:
        out += [f"- {_label(s)}: {c}" for c in s.caveats] or [f"- {_label(s)}: none"]
    return [*out, ""]


def render(all_scores: Sequence[Scores]) -> str:
    if not all_scores:
        raise ValueError("no scores to report")
    lines = ["# laya-pii-bench report", ""]
    if any(s.context.calib_fit_on != "calib" for s in all_scores):
        lines += [
            "> **DEBUG REPORT.** Calibration was not fit on a calib split (fit_on = "
            "fixture_debug). Numbers are in-sample pipeline checks, not benchmark results.",
            "",
        ]
    builders = (
        _run_context,
        _headline,
        _per_question,
        _calibration,
        _routing,
        _speed,
        _slices,
        _failures,
        _caveats,
    )
    for i, (title, build) in enumerate(zip(SECTIONS, builders, strict=True), start=1):
        lines += [f"## {i}. {title}", "", *build(all_scores)]
    return "\n".join(lines).rstrip() + "\n"


def read_scores(paths: Iterable[Path]) -> list[Scores]:
    return [Scores.model_validate_json(p.read_text(encoding="utf-8")) for p in sorted(paths)]


def write(all_scores: Sequence[Scores], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(all_scores), encoding="utf-8")
