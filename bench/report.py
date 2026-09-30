"""Report stage: `reports/report.md` from scores (one section per docs/specs/metrics.md section)."""

from __future__ import annotations

from collections import Counter
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
from bench.score import D008_ARM, D008_GAP, d008_gap

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


FORWARD_USEFUL = 0.05  # below this test forward rate the operating point saves almost no work
AUROC_USELESS = 0.6  # below this pii_present discrimination the model barely ranks PII


def _recall_ci(h: Headline) -> str:
    if h.recall is not None and h.false_forwards == 0 and h.recall.point == 1.0:
        return "1.0000 (no misses; CI n/a, see exact bounds)"
    return _ci(h.recall)


def _target(h: Headline) -> str:
    if h.recall_target is None or h.recall_exact_hi is None:
        return "n/a"
    if h.recall_exact_hi < h.recall_target:
        return f"**missed** (upper {_f(h.recall_exact_hi)} < {h.recall_target:g})"
    return f"not rejected (upper {_f(h.recall_exact_hi)})"


def _d008(s: Scores, split: str, h: Headline) -> str:
    g = d008_gap(h)
    if g is None:
        return "n/a"
    flag = s.context.arm == D008_ARM and split == "test" and g > D008_GAP
    return f"{g:.4f}" + (" **D-008 review**" if flag else "")


def _headline_rows(all_scores: Sequence[Scores], split: str) -> list[Sequence[object]]:
    rows: list[Sequence[object]] = []
    for s in all_scores:
        if split not in s.splits:
            continue
        h = s.splits[split].headline
        rows.append((_label(s), _f(h.t_low), _f(h.t_high) if h.t_high is not None else "none",
                     _recall_ci(h), f"{_f(h.recall_exact_lo)} / {_f(h.recall_exact_hi)}",
                     _target(h), _d008(s, split, h), _f(h.route_recall), _ci(h.forward_rate),
                     _f(h.specificity), h.false_forwards, _f(h.auroc_pii), _f(h.precision),
                     f"{h.n_units} / {h.n_docs} / {h.n_positive}"))  # fmt: skip
    return rows


HEADLINE_COLS = ["arm / qs", "t_low", "t_high", "recall", "exact lo / hi", "recall target",
                 "point - exact lo", "route recall", "forward rate", "negatives forwarded",
                 "false forwards", "AUROC p(pii)", "PII share at p >= t_low",
                 "units / docs / positives"]  # fmt: skip


def _findings(all_scores: Sequence[Scores]) -> list[str]:
    """Plain-language findings computed from the scores (M6 results review): what the operating
    point is worth, not only what it catches."""
    test = [(s, s.splits["test"].headline) for s in all_scores if "test" in s.splits]
    if not test:
        return []
    out: list[str] = []
    low = [(s, h) for s, h in test if h.forward_rate.point < FORWARD_USEFUL]
    if low:
        out.append(
            "- **The recall-first operating point is nearly degenerate.** At the calib-fit "
            f"`t_low`, {len(low)} of {len(test)} arm x question-set runs forward under "
            f"{FORWARD_USEFUL:.0%} of test units ("
            + ", ".join(f"{_label(s)} {h.forward_rate.point:.2%}" for s, h in low)
            + '). The trivial policy "escalate everything" has recall 1 and forward rate 0, '
            "so high recall here says little about work saved. With few calib positives the "
            'recall target means "no calib misses": `t_low` is the lowest-scoring calib '
            "positive, a single unit."
        )
    weak = [(s, h) for s, h in test if h.auroc_pii is not None and h.auroc_pii < AUROC_USELESS]
    if weak:
        out.append(
            "- **Some checkpoints barely rank PII.** Test AUROC of calibrated p(pii) below "
            f"{AUROC_USELESS}: "
            + ", ".join(f"{_label(s)} {h.auroc_pii:.3f}" for s, h in weak if h.auroc_pii)
            + '. Their high recall comes from answering "PII present" to almost everything, '
            "not from detection (option-swap probe: "
            "`reports/audits/M6_pii_question_probe-20260929.md`)."
        )
    missed = [(s, h) for s, h in test
              if h.recall_exact_hi is not None and h.recall_target is not None
              and h.recall_exact_hi < h.recall_target]  # fmt: skip
    if missed:
        out.append(
            "- **The recall target does not transfer from calib to test** for "
            + ", ".join(
                f"{_label(s)} ({h.recall.point if h.recall else 0:.3f}, exact upper "
                f"{h.recall_exact_hi:.3f})"
                for s, h in missed
            )
            + f"; target {missed[0][1].recall_target:g}."
        )
    kinds = [(s, h) for s, h in test
             if (q := h.auroc_by_kind.get("quasi_only")) is not None
             and (d := h.auroc_by_kind.get("direct")) is not None and q < d - 0.05]  # fmt: skip
    if kinds:
        out.append(
            "- **Quasi-identifiers alone are the hardest positives.** AUROC quasi-only vs direct: "
            + ", ".join(
                f"{_label(s)} {h.auroc_by_kind['quasi_only'] or 0:.3f} vs "
                f"{h.auroc_by_kind['direct'] or 0:.3f}"
                for s, h in kinds
            )
            + ". The pii_present prompt names names, contacts, MRNs and birth dates, not event "
            "dates or initials, which the gold counts (phi_quasi)."
        )
    ff: Counter[str] = Counter(
        f.doc_id for s in all_scores if "test" in s.splits for f in s.splits["test"].failures
    )
    shared = [(d, n) for d, n in ff.most_common() if n >= 3]
    if shared:
        out.append(
            "- **False forwards are not independent across arms.** Short documents fit in one "
            "unit for B2-B4, so those arms see identical text and repeat the same misses: "
            + ", ".join(f"{d} in {n} runs" for d, n in shared)
            + f" ({sum(n for _, n in shared)} of {sum(ff.values())} test false forwards)."
        )
    at95 = [(s, c) for s in all_scores if "test" in s.splits
            for c in s.splits["test"].curve if abs(c.target - 0.95) < 1e-9]  # fmt: skip
    if at95:
        out.append(
            "- **Trading recall for work saved (calib target 0.95):** "
            + ", ".join(
                f"{_label(s)} forwards {c.forward_rate:.1%} at test recall "
                f"{_f(c.recall, 3)} ({c.false_forwards} false forwards)"
                for s, c in at95
            )
            + ". See the curve table below."
        )
    trunc = [(s, h) for s, h in test if h.truncated_forwarded]
    if trunc:
        out.append(
            "- Truncated units were forwarded (the model never saw their tail): "
            + ", ".join(f"{_label(s)} {h.truncated_forwarded}" for s, h in trunc)
            + "."
        )
    by_arm_qs = {(s.context.arm, s.context.qs): h for s, h in test}
    for (arm, qs), h3 in sorted(by_arm_qs.items()):
        h1 = by_arm_qs.get((arm, "qs_v1"))
        if qs != "qs_v3" or h1 is None or h1.auroc_pii is None or h3.auroc_pii is None:
            continue
        q1, q3 = h1.auroc_by_kind.get("quasi_only"), h3.auroc_by_kind.get("quasi_only")
        out.append(
            f"- **qs_v3 (D-021) changes only the pii_present wording, and on arm {arm} it hurts:** "
            f"test AUROC {h3.auroc_pii:.3f} vs {h1.auroc_pii:.3f} with qs_v1"
            + (f" (quasi-only positives {q3:.3f} vs {q1:.3f})" if q1 and q3 else "")
            + ". The longer instruction raises p(PII) for PII-free units as much as for PII "
            "units, with or without dates in the text, so separation collapses: the prompt, not "
            "only the checkpoint, limits zero-shot detection "
            "(`reports/audits/M6_qs_v3_result-20260930.md`)."
        )
    if {"qs_v1", "qs_v2"} <= {s.context.qs for s in all_scores}:
        out.append(
            "- qs_v1 vs qs_v2 differences in the same arm are not a question-wording effect: "
            "pii_present has the same text in both, qs_v1 runs fp32 and qs_v2 fp16 (5 rows) on "
            "MPS, which moves long-input probabilities, and only qs_v1 has the role rule."
        )
    return out


def _headline(all_scores: Sequence[Scores]) -> list[str]:
    return [
        "### Key findings",
        "",
        *_findings(all_scores),
        "",
        "### Test (headline)",
        "",
        "pii_present recall at the calib-fit `t_low` (95% document-level bootstrap CI). Exact "
        "lo / hi are Clopper-Pearson on unit counts (ignore clustering within documents); the "
        "recall target is `missed` when the exact upper bound is below it. `point - exact lo` "
        f"above {D008_GAP} flags D-008 for review on arm {D008_ARM} only (D-008 amended). "
        "Negatives forwarded = forwarded PII-free units / PII-free units (the work saved). "
        "Route recall counts misses after routing (1 - false forwards / positives). t_high "
        "`none`: no threshold reached the precision target, so only the role rule redacts. "
        "Doc-level arms are underpowered (few units per document).",
        "",
        *_table(HEADLINE_COLS, _headline_rows(all_scores, "test")),
        "",
        "### Recall vs forward rate on test (D-007 amended)",
        "",
        "`t_low` fit on calib for each recall target, then applied to test with the same routing "
        "(role rule included). Forward rate is the share of test units passed without review; "
        "negatives forwarded is the share of PII-free units passed (the work saved).",
        "",
        *_table(
            [
                "arm / qs",
                "calib target",
                "t_low",
                "test recall",
                "exact lo / hi",
                "forward rate",
                "negatives forwarded",
                "false forwards",
            ],
            [
                (
                    _label(s),
                    f"{c.target:g}",
                    _f(c.t_low),
                    _f(c.recall),
                    f"{_f(c.recall_exact_lo)} / {_f(c.recall_exact_hi)}",
                    f"{c.forward_rate:.2%}",
                    _f(c.negatives_forwarded),
                    c.false_forwards,
                )
                for s in all_scores
                if "test" in s.splits
                for c in s.splits["test"].curve
            ],
        ),
        "",
        "### Holdout (descriptive only, D-005)",
        "",
        "All IRB letters (one document type, 30 documents, few positives), never part of the "
        "headline. With a forward rate of 0, recall here is vacuous. Known limitation (M4 S1): a "
        "fixed alt-text contact line appears only in PII-free letters, a possible shortcut cue.",
        "",
        *_table(HEADLINE_COLS, _headline_rows(all_scores, "holdout")),
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
                         _f(pii.macro_f1) if pii else "n/a", _recall_ci(h), _ci(h.forward_rate),
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
        "correctness by the max probability (for pii_present discrimination see section 2). "
        "`= raw (T fallback)`: the temperature fit hit its bound, so T = 1 and the calibrated "
        "columns equal raw; calibration did nothing there.",
        "",
    ]
    for s in all_scores:
        fell = {k.split(":", 1)[0] for k in s.context.calib_temperature_fallbacks}
        for split, sp in s.splits.items():
            out += [f"### {_label(s)}, {split}", ""]
            out += _table(
                ["question", "ECE raw", "ECE cal", "Brier raw", "Brier cal", "AUROC raw",
                 "AUROC cal"],
                [
                    (q + (" = raw (T fallback)" if q in fell else ""), _f(c.ece_raw),
                     _f(c.ece_calibrated), _f(c.brier_raw), _f(c.brier_calibrated),
                     _f(c.auroc_raw), _f(c.auroc_calibrated))
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
        drift = "n/a" if sp.batch1_drift is None else f"{sp.batch1_drift:.2f}x"
        bauto = sp.batched_autocast if sp.batched is not None else "not run"
        out += [f"### {_label(s)}", "", f"Hardware: **{sp.hardware}**. "
                f"Warmup calls excluded: {sp.warmup_excluded}. Batch-1 outliers (> 5x the median "
                f"of similar-length calls): {sp.batch1_outliers}. Batch-1 ms/token, end of run vs "
                f"start: {drift}. laya autocast: batch-1 {sp.batch1_autocast}, batched "
                f"{bauto} (on MPS, fp16 autocast starts at 5 question rows, so "
                "qs_v2 runs fp16 and qs_v1 fp32).", ""]  # fmt: skip
        batched = (_lat("per unit, batched (amortized: batch time / batch size)", sp.batched)
                   if sp.batched is not None else
                   ("per unit, batched", 0, "not run", "", "", "", ""))  # fmt: skip
        out += _table(
            ["mode", "n", "p50 ms", "p95 ms", "p99 ms", "mean ms", "per sec"],
            [
                _lat("per unit, batch-1", sp.batch1),
                batched,
                _lat("per document (sum of units, batch-1; incl. calib docs)", sp.per_doc_ms),
                *(_lat(f"per unit, batch-1, {k} tokens", v)
                  for k, v in sp.batch1_by_length.items()),
            ],
        )  # fmt: skip
    return [
        "Per-unit latency is not comparable across arms (units range from 256-token chunks to "
        "whole documents); compare the per-document row or the length rows. Batched runs were "
        "made for arms A and B1 only: batches of eight 2k-8k-token states exceed the 8 GB M2 "
        "(swapping, NaN).",
        "",
        *out,
    ]


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
