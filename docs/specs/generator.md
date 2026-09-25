# Spec: synthetic document generator (`bench/generate/`)

Job: documents where every PII value has an exact character offset, at controlled distributions,
reproducible from a seed. Realism matters only as far as it keeps the task from being trivially
separable.

## World first, documents as views

```
World (seeded)
 ├─ Study ×3          protocol no (FTX-4471-012), NCT, EudraCT, compound code, sponsor
 ├─ Site ×8/study     site no, institution, address, PI, coordinator, CRA
 ├─ Subject ×~15/site subject ID, rand no, name, initials, DOB, MRN, ZIP, sex
 └─ Events            visits, AEs/SAEs, conmeds, labs, deviations
        ↓
DocSpec (doc_type, lang, length_bucket, pii_density, pii_depth, tags)
        ↓
Template → Render → Perturb → Validate → docs.jsonl
```

The same subject appears across SAE form, narrative, and deviation log with consistent dates.
Splits group on `world_refs.site`.

## Layout

```
bench/generate/
  world.py         # World, Study, Site, Subject, Event models + seeded builder
  providers.py     # Faker providers: subject_id, mrn (per-site format), rand_no, lot_no, ...
  variants.py      # surface-form variant generators (names, dates, initials, IDs, ages)
  render.py        # Jinja env, pii() and neg() globals, sentinel resolve
  negatives.py     # hard-negative registry + injector
  assemble.py      # length buckets, filler blocks, PII-depth placement
  perturb.py       # perturbations + span remap
  validate.py      # V1..V6
  templates/<doc_type>/*.j2
  filler/          # grammar files for clean filler blocks
```

## Sentinels (the only labeling path)

Templates call `pii(value, category, role, value_kind)` and `neg(value, kind)`. Each call appends a
slot and returns `⟦sN⟧` / `⟦nN⟧`. After rendering, one left-to-right pass replaces sentinels and
records offsets:

```python
SENTINEL = re.compile(r"⟦([sn])(\d+)⟧")

def resolve(raw: str, slots: list[Slot], negs: list[NegSlot]) -> tuple[str, list[Span], list[Negative]]:
    out, spans, negatives, pos, last = [], [], [], 0, 0
    for m in SENTINEL.finditer(raw):
        lit = raw[last:m.start()]; out.append(lit); pos += len(lit)
        kind, idx = m.group(1), int(m.group(2))
        slot = slots[idx] if kind == "s" else negs[idx]
        out.append(slot.value)
        rec = (Span if kind == "s" else Negative)(start=pos, end=pos + len(slot.value), **slot.meta)
        (spans if kind == "s" else negatives).append(rec)
        pos += len(slot.value); last = m.end()
    out.append(raw[last:])
    return "".join(out), spans, negatives
```

Anti-pattern: `str.format` then searching for values. Values collide ("Maria" in "Mariana", repeated
dates, subject IDs vs lot numbers).

## Surface-form variation (`value_kind` + `surface` recorded)

| Value | Variants |
|---|---|
| Name | `Maria Gonzalez`, `GONZALEZ, Maria`, `M. Gonzalez`, `Ms. Gonzalez`, `Dr. Gonzalez` (staff) |
| Initials | `MG`, `M.G.`, `M-G`, `MXG` |
| Date | `14-Mar-1958`, `03/14/1958`, `1958-03-14`, `14MAR1958`, `March 14, 1958`, DE/ES/PL locale forms |
| Subject ID | `1001-0023`, `Subj 1001-0023`, `#10010023` |
| MRN | per-site format (`MRN 00482913`, `H-2291-4471`) |
| Phone / email | locale-aware; institutional vs personal domains |
| Age | `67`, `67 y/o`, `aged 67`, and `>89` edge case |

Locales: `en_US`, `de_DE`, `es_ES`, `pl_PL`.

## Hard negatives (target 25% of docs, recorded with offsets)

- Study identifiers: protocol no., NCT, EudraCT, amendment no. (also in repeated headers/footers)
- ID look-alikes: lot/batch, site no., MedDRA codes, CAS numbers, kit numbers
- Non-PHI dates: document effective date, approval date, database lock date
- Eponyms: Kaplan-Meier, Cockcroft-Gault, Wilcoxon, Hodgkin, Bonferroni
- Clinical numerics: doses, reference ranges, visit windows (`Day 15 ±2`)
- Pre-redacted content: `[REDACTED]`, `XX-XXXX`, `***`

## Length and depth

Docs are assembled from PII-bearing blocks and clean filler blocks. Pick `length_bucket`, render
required blocks, add filler until target token count (counted with the English and multilingual
tokenizers; bucket uses the multilingual count). For `pii_depth` docs (60 sparse long docs), place
the single PII block at 0–20% / 40–60% / 80–100% of tokens. XL docs (> 8,192 tokens) exist to test
truncation flagging.

Filler default: grammar-generated boilerplate (eligibility, statistical methods, safety language).
An LLM-written filler bank is allowed only if every block passes V2 plus an NER scan and the bank
is frozen by hash (needs a DECISIONS entry). Never copy real protocol text.

## Perturbations (after resolve, with span remap)

Every transform returns `(position, delta)` edits; spans and negatives shift accordingly. A span
that gains an inserted newline grows but stays labeled. OCR noise that changes a span's characters
updates the span (still PII).

| Perturbation | Rate (gen_spec) |
|---|---|
| Line wrap at fixed width | 0.30 |
| OCR noise (`l↔1`, `O↔0`, drops) | 0.10 |
| Table rendering (pipe / tab / fixed width) | 0.20 |
| Repeated headers/footers | 0.40 |
| Email quoting + signatures | site_correspondence only |

## Validators (generation fails loudly)

- V1 Offset integrity: `text[start:end]` equals the recorded value for every span and negative.
- V2 No unlabeled world PII: every world PII value, in every variant form, found outside a labeled
  span fails the doc.
- V3 Negatives don't overlap spans.
- V4 Token budget matches bucket.
- V5 Distribution check vs `gen_spec.yaml`.
- V6 Determinism: same seed → identical `sha256` of output.

## Output

`data/docs.jsonl` (one `Document` per line) + `data/gen_manifest.json` (seed, counts per dimension,
validator results, sha256).

## Optional paraphrase pass (D-011, deferred)

Send pre-resolve text with sentinels to a local LLM, require every sentinel exactly once, reject
otherwise, then resolve normally. Run V2 on output.
