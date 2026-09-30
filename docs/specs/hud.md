# Spec: HUD replay (`hud/`)

A replay of recorded `Decision` data in the style of the Jev-plays-Doom demo (dark terminal
aesthetic, green active edges, amber decision nodes, judgments panel with probability bars).
Replay, not simulation: timings are the recorded `t_offset_ms` and `latency_ms`.

## Stack

TypeScript + Vite + `vite-plugin-singlefile` → `hud/dist/index.html` (one file, opens offline).
No framework required; if one is used, Preact. Types from `hud/src/types.gen.ts` (generated).

## Input

`hud/public/replay.json`, exported by `bench report --hud` (`bench/hud.py`, type `Replay` in
`bench/domain.py`, TS in `hud/src/types.gen.ts`). One bundle holds every scored run (the arm/qs
selector), with documents stored once:

```ts
interface Replay {
  created_at: string;
  docs: ReplayDoc[];             // every document a run refers to (test split by default)
  runs: {
    label: string; split: string; meta: RunMeta; calib: CalibParams; scores_sha256: string;
    units: ReplayUnit[];         // id, doc_id, start, end, truncated, gold
    decisions: RoutedDecision[]; // run order, warmups excluded
    t_ms: number[];              // replay clock: cumulative recorded latency in run order
  }[];
}
```

The export refuses runs whose decisions, units, docs or calib differ (by hash) from what the scores
were computed on. Replay time is the sum of recorded `latency_ms` in run order: raw `t_offset_ms`
restarts per session and includes other splits' units, so it is not used as the clock. Nothing is
invented.

The build embeds the export gzipped (`hud/data/replay.json.gz`, decompressed in the browser with
`DecompressionStream`), so `hud/dist/index.html` is one offline file; "load replay" opens any
other export (`.json` or `.json.gz`).

## Layout (desktop, dark)

- **Top bar:** docs, units, p50 ms, units/sec, forward %, false forwards (red when > 0), elapsed
  replay time, arm/qs selector.
- **Left column:** unit stream; each row colored by gold (PII / clean), marked by route.
- **Center graph:** question nodes (`pii_present`, `subject_role`, `category`, `doc_kind`) →
  policy node → route nodes (FORWARD / REDACT / ESCALATE). Edges light on the active unit;
  threshold triggers shown as dashed edge labels (`p=0.12 < t_low=0.08`).
- **Judgments panel:** per-question probability bars, chosen option bold, confidence, raw vs
  calibrated toggle.
- **Situation report:** the unit text with gold spans highlighted and a verdict chip (correct /
  false forward / over-redact).

## Controls

Play/pause, speed (0.25×–16×), scrub bar, step, "next false forward", filter by doc type.

## Tests

`make hud`: vitest on the replay engine (`hud/tests/unit`), then Playwright on the built file
(`hud/tests/e2e`), checking the real export against the UI, with screenshots in
`reports/audits/M7_hud/`.

## Anti-patterns

- Animating with invented timings.
- Loading mock data in the shipped build (mock only in `hud/src/dev/`).
