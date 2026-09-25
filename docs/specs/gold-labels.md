# Spec: units and gold labels (`bench/label.py`)

All rules are parameterized by `config/policy.yaml`. The label stage is deterministic.

## Segmentation

- `chunk`: fixed token windows (`size`, `overlap` from arm config), cut on the arm checkpoint's
  tokenizer, mapped back to char offsets via offset mapping. Prefer to end on whitespace within the
  last 8 tokens.
- `section`: split on section headers emitted by the generator (`gen_meta.sections` offsets), merge
  adjacent sections up to the token budget.
- `doc`: whole document.

State budget = `max_len - head_max_len` (English default 512-192=320; multilingual 1024-256=768,
and larger when `max_len` is raised). If a unit's token count exceeds the state budget, set
`truncated=true`. Never drop the unit.

## Gold derivation

- **Membership:** a span belongs to a unit if any character overlaps. Set `split_span=true` if any
  span crosses the unit boundary.
- **pii_present:** `A` if any member span's category is in `policy.pii_categories`, else `B`.
  `coded_id` is in that set iff `policy.coded_id_is_pii` (D-001).
- **subject_role:** from member span roles (only categories counted as PII): patient, staff,
  both, none. Sponsor-role spans map to none.
- **category:** single choice using `policy.category_precedence`
  (direct > quasi > coded > staff > none).
- **categories_multi:** one boolean per category (for qs_v2).
- **doc_kind:** from `policy.doc_kind_map[doc_type]`.

## Checks

- Per split and question, every class present (M5 gate).
- Gold answer distribution per arm written to `data/label_manifest.json`.
