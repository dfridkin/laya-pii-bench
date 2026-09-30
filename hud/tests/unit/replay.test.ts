import { describe, expect, it } from "vitest";
import { activeIndex, duration, nextMatching, percentile, segments, stats, thresholdLabel, verdict, type Row } from "../../src/replay";

function row(i: number, t: number, latency: number, route: string, positive: boolean): Row {
  return {
    i, t, positive, verdict: verdict(route, positive),
    d: { route, triggers: [], calibrated_probs: { pii_present: { A: 0.1, B: 0.9 } },
         decision: { latency_ms: latency } } as never,
    unit: { id: `u${i}`, doc_id: `d${i % 2}`, start: 0, end: 10, truncated: false, gold: {} } as never,
    doc: { id: `d${i % 2}`, doc_type: "crf_page", lang: "en", text: "", spans: [] } as never,
  };
}
const rs = [row(0, 0, 100, "escalate", true), row(1, 100, 200, "forward", false),
            row(2, 300, 50, "forward", true), row(3, 350, 150, "redact", false)];

describe("replay engine", () => {
  it("verdicts", () => {
    expect(verdict("forward", true)).toBe("false forward");
    expect(verdict("forward", false)).toBe("correct");
    expect(verdict("redact", false)).toBe("over-redact");
    expect(verdict("escalate", false)).toBe("over-escalate");
    expect(verdict("redact", true)).toBe("correct");
    expect(verdict("escalate", true)).toBe("correct");
  });
  it("clock maps to the last started decision", () => {
    expect(activeIndex(rs, -1)).toBe(-1);
    expect(activeIndex(rs, 0)).toBe(0);
    expect(activeIndex(rs, 299)).toBe(1);
    expect(activeIndex(rs, 300)).toBe(2);
    expect(activeIndex(rs, 10_000)).toBe(3);
    expect(duration(rs)).toBe(500);
  });
  it("next false forward wraps and reports none", () => {
    expect(nextMatching(rs, 0, (r) => r.verdict === "false forward")).toBe(2);
    expect(nextMatching(rs, 2, (r) => r.verdict === "false forward")).toBe(2);
    expect(nextMatching(rs, 0, () => false)).toBe(-1);
  });
  it("stats over replayed rows", () => {
    const s = stats(rs, 2);
    expect(s.units).toBe(3);
    expect(s.docs).toBe(2);
    expect(s.p50).toBe(100);
    expect(s.forwardRate).toBeCloseTo(2 / 3);
    expect(s.falseForwards).toBe(1);
    expect(s.perSec).toBeCloseTo(3 / 0.35);
    expect(percentile([], 0.5)).toBeNaN();
  });
  it("segments clip spans to the unit and mark coded ids uncounted", () => {
    const r = row(0, 0, 1, "forward", true);
    (r as { doc: unknown }).doc = { id: "d", doc_type: "x", lang: "en", text: "Name Jo Doe id 1001-0023 end",
      spans: [{ start: 5, end: 11, category: "phi_direct" }, { start: 15, end: 24, category: "coded_id" }] };
    (r as { unit: unknown }).unit = { id: "u", doc_id: "d", start: 3, end: 20, truncated: false, gold: {} };
    const seg = segments(r);
    expect(seg.map((s) => s.text).join("")).toBe("e Jo Doe id 1001-");
    expect(seg.filter((s) => s.span).map((s) => [s.text, s.span?.counted])).toEqual([["Jo Doe", true], ["1001-", false]]);
  });
  it("edge label names the rule that routed the unit", () => {
    const r = row(0, 0, 1, "redact", true);
    expect(thresholdLabel(r, 0.05, 0.9)).toBe("t_low=0.0500 ≤ p=0.1000");
    expect(thresholdLabel(r, 0.2, 0.9)).toBe("p=0.1000 < t_low=0.2000");
    (r.d as { triggers: string[] }).triggers = ["role_patient"];
    expect(thresholdLabel(r, 0.2, 0.9)).toBe("role_patient → redact (p=0.1000)");
    expect(thresholdLabel(r, 0.05, 0.1)).toBe("p=0.1000 ≥ t_high=0.1000");
  });
});
