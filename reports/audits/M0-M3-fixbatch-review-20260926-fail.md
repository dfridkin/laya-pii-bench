# Review of audit fix batch A1-A11 (gate-reviewer subagent), 2026-09-26

HEAD cd73202 (commits 1ff3956..cd73202). Verdict: FAIL (one regression, one A1 bypass, test gaps).

## Gate re-run: no regression
make check 188 passed / 8 skipped; model tests 8 passed; make fixture 10/10; make schema && git diff
--exit-code clean; `bench run` fixture rerun "resumed: 11/11", "laya calls: 0" (decisions sha unchanged);
calibrate/score/report into scratch identical to committed reports/fixture/report_armA_qs_v1.md except
timestamps (headline `0.4366 | 0.5512 | 1.0000 [1.0000, 1.0000] | 0.6306 | 1.0000 | 0.0909 [0.0000,
0.3000] | 0 | 0.8000 | 11 / 10 / 8`, fallback `subject_role:4: fit hit bound (20)`); no-scores report exits 2.

## Per finding (mutation-tested on a git-archive copy)
A1 PARTIAL: flipped units vs run meta / calib units / run-dir calibrate all exit 2, mutants killed.
   Bypass reproduced: decisions copied to a dir without meta.json, calibrate + score both on flipped
   units -> score exit 0. Mutant `calib_doc_ids=[]` in fit survived (overlap test uses hand-built params).
A2 FIXED (0.6306 = 0.025^(1/8); mutants killed). A3 FIXED in logic, CLI regression R1.
A4 FIXED; gap: lower-bound hit with accuracy < 1 untested (mutant survived).
A5 FIXED (all audit mutants killed). A6 PARTIAL: code right, zero tests (reverting `_truncated` survived).
A7 FIXED. A8 PARTIAL: `route_recall = hits/n_pos` mutant survived. A9 PARTIAL: CLI wiring of
   verify_run_rows untested (replacing with pass survived); mode check only with meta; Decision.mode still
   defaults (replacement of "make mode required" not recorded). A10 FIXED; gaps: `@revision` tokenizer
   name and download_models --update untested. A11 PARTIAL: PERTURBATION_TAGS unpinned.

## Regressions / new problems
R1 high: `bench calibrate` crashes (TypeError formatting None) when t_high is None, after writing the
   calib file (exit 1); no CLI test.
R2 medium: no meta.json -> no provenance check in score/calibrate (runner refuses meta-less dirs, they don't).
R3 medium (M5): calib/scored disjointness applies to every scored split; scoring the calib split
   descriptively would be refused. Restrict to test/holdout or document.
R4 low: torn-line repair drops a valid complete last line lacking "\n", and runs before resume checks.
R5 low: `pinned()` raises raw CacheNotFound when the HF cache dir is missing.
R6 low: whitespace-tail merge can exceed `size` by whitespace tokens (conservative truncation flag).
R7 low docs: STATUS still lists the models.lock absolute-path issue as open; Span.value (D-016) not yet
   in bench/domain.py nor listed as pending M4 work.
No problems: t_high None through route_unit/headline/report/schema/TS; D-005, D-016..D-018 reflected in
CLAUDE.md, MILESTONES, generator spec; invariants 1, 2, 3, 4, 5, 11 OK.

## Required fixes
1 R1 + CLI test (unreachable t_high -> exit 0, `t_high: null`). 2 R2: refuse meta-less decisions or require
an explicit labeled override; test the meta-less flipped case. 3 A1: test via calibrate.fit + overlap.
4 A6 tests both directions. 5 A8 test (role-redacted positive below t_low). 6 A9 CLI wiring test; record
mode decision. 7 R3. 8 pin PERTURBATION_TAGS and english@<rev>; lower-bound fallback test; CacheNotFound
hint; STATUS doc fixes.
