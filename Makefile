SHELL := /bin/bash
export USE_TF := 0
export TOKENIZERS_PARALLELISM := false

ARM ?= A
QS ?= qs_v1
ARMS ?= A B1 B2 B3 B4
QSETS ?= qs_v1 qs_v2
BENCH := uv run bench

.PHONY: bootstrap check lint type test schema fixture gen label split run run-all \
        calibrate calibrate-all freeze-calib score score-all report hud pipeline smoke hw clean-generated

bootstrap:
	./scripts/bootstrap.sh

check: lint type test

lint:
	uv run ruff check bench tests scripts
	uv run ruff format --check bench tests scripts

type:
	uv run pyright

# M1 gate: >= 90% line coverage on the contract modules, each file checked on its own.
COV_GATED := bench/domain.py bench/config.py bench/validate.py

test:
	LAYA_SKIP_MODEL=$${LAYA_SKIP_MODEL:-1} uv run pytest --cov=bench --cov-report=
	@for f in $(COV_GATED); do uv run coverage report --include=$$f --fail-under=90 >/dev/null \
	  || { uv run coverage report --include=$$f; echo "coverage < 90% on $$f"; exit 1; }; done
	@uv run coverage report --include='$(shell echo $(COV_GATED) | tr ' ' ',')'

hw:
	$(BENCH) hw --out hw.json

schema:
	$(BENCH) schema --out schema/
	mkdir -p hud/src
	npx --yes json-schema-to-typescript@15 -i schema/domain.json -o hud/src/types.gen.ts \
	  --unreachableDefinitions --additionalProperties false

fixture:
	$(BENCH) validate fixtures/mini/docs.jsonl

gen:
	$(BENCH) gen --spec config/gen_spec.yaml --out data/docs.jsonl

label:
	$(BENCH) label --docs data/docs.jsonl --policy config/policy.yaml --arms config/arms.yaml

split:
	$(BENCH) split --docs data/docs.jsonl --out data/splits.json  # after label: reads units for class coverage

run:
	$(BENCH) run --arm $(ARM) --qs $(QS)

BATCHED_ARMS ?= A B1 B2   # B3/B4 batch-1 only: batching 4k-8k units exceeds 8 GB (audit C4)
BATCH ?= 8
RELEASE_EACH_CALL ?= B4  # 8k context: free the MPS cache after every call (M6: NaN, swap stalls)

run-all:  # batch-1 for every arm x qs, then the batched speed runs; each run resumes. caffeinate:
	# macOS idle sleep otherwise freezes long runs (perf_counter doesn't count sleep, so timings hold)
	@caffeinate -i -w $$$$ & for a in $(ARMS); do for q in $(QSETS); do \
	  $(BENCH) run --arm $$a --qs $$q $$(case $$a in $(RELEASE_EACH_CALL)) echo --release-every 1;; esac) \
	  || exit 1; done; done
	@for a in $(BATCHED_ARMS); do for q in $(QSETS); do \
	  $(BENCH) run --arm $$a --qs $$q --batch-size $(BATCH) || exit 1; done; done

calibrate-all:
	@for a in $(ARMS); do for q in $(QSETS); do $(MAKE) --no-print-directory calibrate ARM=$$a QS=$$q \
	  || exit 1; done; done

score-all:
	@for a in $(ARMS); do for q in $(QSETS); do $(MAKE) --no-print-directory score ARM=$$a QS=$$q \
	  || exit 1; done; done

calibrate:  # fits on the calib split only; then `make freeze-calib` (D-019)
	$(BENCH) calibrate --decisions runs/$(ARM)/$(QS)/decisions.jsonl --units data/units/$(ARM).jsonl \
	  --out calib/$(ARM)__$(QS).json

freeze-calib:  # commit calib/*.json with content hashes; score refuses uncommitted calib
	$(BENCH) freeze-calib calib/*.json

BATCHED_RUN = runs/$(ARM)/$(QS)__batch$(BATCH)/decisions.jsonl

score:
	$(BENCH) score --decisions runs/$(ARM)/$(QS)/decisions.jsonl --units data/units/$(ARM).jsonl \
	  --calib calib/$(ARM)__$(QS).json --out scores/$(ARM)__$(QS).json \
	  $(if $(wildcard $(BATCHED_RUN)),--batched-decisions $(BATCHED_RUN))

report:
	$(BENCH) report --scores-dir scores --out reports/report.md

hud:
	cd hud && npm install && npm run build

pipeline: gen label split run-all calibrate-all freeze-calib score-all report

smoke:
	$(BENCH) smoke --docs 20 --arm A --qs qs_v1

clean-generated:
	rm -rf data runs calib scores hw.json
