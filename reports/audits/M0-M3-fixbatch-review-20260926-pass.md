# Review 2 of audit fix batch (gate-reviewer subagent), 2026-09-26

HEAD 7385bdb (fixes 1a217c6, 7385bdb on top of review 1). Verdict: PASS. No blocking regressions.

## Gate re-run
make check: pyright 0 errors, 200 passed, 8 skipped, coverage TOTAL 99%. Model tests: 8 passed. make fixture:
10/10. make schema && git diff --exit-code: clean. `bench run` fixture rerun: "resumed: 11/11 already done",
"laya calls: 0", decisions/meta sha unchanged. calibrate/score/report on runs/mini/A/qs_v1 into scratch: "t_low=0.4366
t_high=0.5512 fit_on=fixture_debug hash=d7f5dfe943ab"; "recall@t_low=1.0000 forward_rate=0.0909 false_forwards=0";
report identical to committed except date; fallback "subject_role:4: fit hit bound (20)".

## Per item (mutation-tested on a git-archive copy)
R1 FIXED (t_high=none, rc 0; mutant killed). R2 FIXED (calibrate/score meta checks and caveat mutants killed).
R3 FIXED (disjointness_scope; mutants killed). R4 FIXED; ordering mutant survived (follow-up 1). R5 FIXED.
R7 FIXED (STATUS, Span.value pending M4a, A9 mode decision recorded). A1 calib_doc_ids covered. A4 covered and
sound: 1428 random fits, 0 interior optima wrongly flagged; strict-< mutant survived (follow-up 3). A6, A8, A9
wiring, A11 covered. A10 covered by model-marked test (killed with LAYA_SKIP_MODEL=0). Provenance core covered.

## Attacks
Meta-less flipped units without override: calibrate and score rc 2, no calib written. With both override flags:
rc 0, DEBUG banner + no-meta caveat. Real run decisions copied without meta: rc 2 without flags; with flags only a
DEBUG-labeled report. Real run dir (meta present) with flipped units: calibrate and score rc 2 (units differ);
--allow-no-meta has no effect when meta exists.

## Invariants
1, 2/3, 4, 5, 11 OK.

## Follow-ups (non-blocking)
1 R4 ordering untested. 2 --allow-no-meta tied to flags, not to fit_on == fixture_debug (would bypass the DEBUG
banner once M5 writes fit_on="calib"); calibrate's `and debug_fit_all` clause redundant. 3 A4 1e-9 tolerance
untested (flat NLL). 4 hand-written meta without units/docs hashes silently skips provenance.

## Resolution (commit after this review)
All four follow-ups closed with tests; each corresponding mutant verified killed on a scratch copy.
