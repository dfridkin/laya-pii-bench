SHELL := /bin/bash
export USE_TF := 0
export TOKENIZERS_PARALLELISM := false

ARM ?= A
QS ?= qs_v1
ARMS ?= A B1 B2 B3 B4
QSETS ?= qs_v1 qs_v2
BENCH := uv run bench

.PHONY: bootstrap check lint type test schema fixture gen label split run run-all \
        calibrate score report hud pipeline smoke hw clean-generated

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
	@for f in $(COV_GATED); do [ ! -e $$f ] || uv run coverage report --include=$$f --fail-under=90 >/dev/null \
	  || { uv run coverage report --include=$$f; echo "coverage < 90% on $$f"; exit 1; }; done
	@uv run coverage report --include='$(shell echo $(COV_GATED) | tr ' ' ',')'

hw:
	$(BENCH) hw --out hw.json

schema:
	$(BENCH) schema --out schema/
	npx --yes json-schema-to-typescript@15 -i 'schema/*.json' -o hud/src/types.gen.ts --declareExternallyReferenced

fixture:
	$(BENCH) validate fixtures/mini/docs.jsonl

gen:
	$(BENCH) gen --spec config/gen_spec.yaml --out data/docs.jsonl

label:
	$(BENCH) label --docs data/docs.jsonl --policy config/policy.yaml --arms config/arms.yaml --out data/units/

split:
	$(BENCH) split --docs data/docs.jsonl --out data/splits.json

run:
	$(BENCH) run --arm $(ARM) --qs $(QS)

run-all:
	@for a in $(ARMS); do for q in $(QSETS); do $(BENCH) run --arm $$a --qs $$q || exit 1; done; done

calibrate:
	$(BENCH) calibrate --all

score:
	$(BENCH) score --all

report:
	$(BENCH) report --out reports/report.md --hud hud/public/replay.json

hud:
	cd hud && npm install && npm run build

pipeline: gen label split run-all calibrate score report

smoke:
	$(BENCH) smoke --docs 20 --arm A --qs qs_v1

clean-generated:
	rm -rf data runs calib scores hw.json
