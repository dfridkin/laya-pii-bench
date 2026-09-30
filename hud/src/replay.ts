// Replay engine: pure functions over a recorded run (docs/specs/hud.md). No DOM here.
import type { Replay, ReplayRun, ReplayDoc, ReplayUnit, RoutedDecision } from "./types.gen";

export type Verdict = "correct" | "false forward" | "over-redact" | "over-escalate";

export interface Row {
  i: number;
  t: number; // replay clock start (ms): cumulative recorded latency in run order
  d: RoutedDecision;
  unit: ReplayUnit;
  doc: ReplayDoc;
  positive: boolean; // gold pii_present = A
  verdict: Verdict;
}

/** forward+PII: false forward (the costly miss); redact of PII-free text: over-redact; escalate
 * of PII-free text: over-escalate (a human reviews it, work not saved); otherwise correct. */
export function verdict(route: string, positive: boolean): Verdict {
  if (route === "forward") return positive ? "false forward" : "correct";
  if (positive) return "correct";
  return route === "redact" ? "over-redact" : "over-escalate";
}

export function rows(replay: Replay, run: ReplayRun): Row[] {
  const units = new Map(run.units.map((u) => [u.id, u]));
  const docs = new Map(replay.docs.map((d) => [d.id, d]));
  return run.decisions.map((d, i) => {
    const unit = units.get(d.decision.unit_id);
    if (!unit) throw new Error(`replay: no unit ${d.decision.unit_id}`);
    const doc = docs.get(unit.doc_id);
    if (!doc) throw new Error(`replay: no doc ${unit.doc_id}`);
    const positive = unit.gold.pii_present === "A";
    return { i, t: run.t_ms[i] ?? 0, d, unit, doc, positive, verdict: verdict(d.route, positive) };
  });
}

/** Total replay length: the last decision's start plus its recorded latency. */
export function duration(rs: Row[]): number {
  const last = rs[rs.length - 1];
  return last ? last.t + last.d.decision.latency_ms : 0;
}

/** Index of the decision active at clock t (the last one started), -1 before the first. */
export function activeIndex(rs: Row[], t: number): number {
  let lo = 0;
  let hi = rs.length - 1;
  let ans = -1;
  while (lo <= hi) {
    const mid = (lo + hi) >> 1;
    if ((rs[mid] as Row).t <= t) {
      ans = mid;
      lo = mid + 1;
    } else hi = mid - 1;
  }
  return ans;
}

/** Next row after `from` (wrapping) that passes `keep`; -1 if none. */
export function nextMatching(rs: Row[], from: number, keep: (r: Row) => boolean): number {
  for (let k = 1; k <= rs.length; k++) {
    const j = (from + k) % rs.length;
    if (keep(rs[j] as Row)) return j;
  }
  return -1;
}

export function percentile(xs: number[], p: number): number {
  if (!xs.length) return NaN;
  const s = [...xs].sort((a, b) => a - b);
  const pos = (s.length - 1) * p;
  const lo = Math.floor(pos);
  const hi = Math.ceil(pos);
  return (s[lo] as number) + ((s[hi] as number) - (s[lo] as number)) * (pos - lo);
}

export interface Stats {
  docs: number;
  units: number;
  p50: number;
  perSec: number;
  forwardRate: number;
  falseForwards: number;
}

/** Top-bar numbers over the rows replayed so far (0..upto inclusive). */
export function stats(rs: Row[], upto: number): Stats {
  const seen = rs.slice(0, upto + 1);
  const lat = seen.map((r) => r.d.decision.latency_ms);
  const total = lat.reduce((a, b) => a + b, 0);
  return {
    docs: new Set(seen.map((r) => r.doc.id)).size,
    units: seen.length,
    p50: percentile(lat, 0.5),
    perSec: total > 0 ? seen.length / (total / 1000) : 0,
    forwardRate: seen.length ? seen.filter((r) => r.d.route === "forward").length / seen.length : 0,
    falseForwards: seen.filter((r) => r.verdict === "false forward").length,
  };
}

/** Plain-language threshold edge label, e.g. "p=0.1200 < t_low=0.0800". */
export function thresholdLabel(r: Row, t_low: number, t_high: number | null | undefined): string {
  const p = r.d.calibrated_probs["pii_present"]?.["A"] ?? NaN;
  const f = (x: number) => x.toFixed(4);
  const role = r.d.triggers.find((t) => t.startsWith("role_"));
  if (role && !(t_high != null && p >= t_high)) return `${role} → redact (p=${f(p)})`;
  if (t_high != null && p >= t_high) return `p=${f(p)} ≥ t_high=${f(t_high)}`;
  if (p < t_low) return `p=${f(p)} < t_low=${f(t_low)}`;
  return `t_low=${f(t_low)} ≤ p=${f(p)}`;
}

/** The unit's text split into plain and gold-span pieces (spans clipped to the unit). */
export function segments(r: Row): { text: string; span?: { category: string; counted: boolean } }[] {
  const { start, end } = r.unit;
  const text = r.doc.text;
  const spans = r.doc.spans
    .filter((s) => s.end > start && s.start < end)
    .sort((a, b) => a.start - b.start);
  const out: { text: string; span?: { category: string; counted: boolean } }[] = [];
  let pos = start;
  for (const s of spans) {
    const a = Math.max(s.start, start);
    const b = Math.min(s.end, end);
    if (a < pos) continue; // overlapping spans are invalid gold (validator); skip defensively
    if (a > pos) out.push({ text: text.slice(pos, a) });
    // coded ids are not PII under D-001: shown, but not as counted identifiers
    out.push({ text: text.slice(a, b), span: { category: s.category, counted: s.category !== "coded_id" } });
    pos = b;
  }
  if (pos < end) out.push({ text: text.slice(pos, end) });
  return out;
}

export async function decodeGzipJson<T>(bytes: ArrayBuffer): Promise<T> {
  const stream = new Blob([bytes]).stream().pipeThrough(new DecompressionStream("gzip"));
  return JSON.parse(await new Response(stream).text()) as T;
}
