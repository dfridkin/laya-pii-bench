# Spec: HUD replay (`hud/`)

A replay of recorded `Decision` data in the style of the Jev-plays-Doom demo (dark terminal
aesthetic, green active edges, amber decision nodes, judgments panel with probability bars).
Replay, not simulation: timings are the recorded `t_offset_ms` and `latency_ms`.

## Stack

TypeScript + Vite + `vite-plugin-singlefile` → `hud/dist/index.html` (one file, opens offline).
No framework required; if one is used, Preact. Types from `hud/src/types.gen.ts` (generated).

## Input

`hud/public/replay.json`, exported by `bench report --hud`:

```ts
interface Replay {
  meta: RunMeta; calib: CalibParams;
  docs: { id: string; doc_type: string; text: string; spans: Span[] }[];  // test docs only
  units: { id: string; doc_id: string; start: number; end: number; gold: GoldAnswers }[];
  decisions: RoutedDecision[];   // sorted by t_offset_ms
}
```

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

## Anti-patterns

- Animating with invented timings.
- Loading mock data in the shipped build (mock only in `hud/src/dev/`).
