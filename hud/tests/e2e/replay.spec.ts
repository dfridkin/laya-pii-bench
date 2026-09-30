// M7 gate: the built single-file HUD replays a real M6 export; controls work.
import { expect, test, type Page } from "@playwright/test";
import { readFileSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const HUD = resolve(here, "../..");
const DIST = `file://${resolve(HUD, "dist/index.html")}`;
const SHOTS = resolve(HUD, "../reports/audits/M7_hud");
mkdirSync(SHOTS, { recursive: true });

interface Run {
  label: string;
  meta: { dataset: string };
  decisions: {
    route: string;
    calibrated_probs: Record<string, Record<string, number>>;
    decision: {
      unit_id: string;
      latency_ms: number;
      answers: { question: string; probs: Record<string, number> }[];
    };
  }[];
  units: { id: string; doc_id: string; start: number; end: number; gold: { pii_present: string } }[];
}
interface Doc { id: string; doc_type: string; text: string; spans: { start: number; end: number; category: string }[] }
const replay = JSON.parse(readFileSync(resolve(HUD, "public/replay.json"), "utf-8")) as {
  runs: Run[];
  docs: Doc[];
};

const falseForwards = (r: Run) => {
  const gold = new Map(r.units.map((u) => [u.id, u.gold.pii_present]));
  return r.decisions.filter((d) => d.route === "forward" && gold.get(d.decision.unit_id) === "A");
};

async function open(page: Page, runLabel?: string): Promise<void> {
  const external: string[] = [];
  page.on("request", (req) => {
    if (!req.url().startsWith("data:") && !req.url().startsWith("file:")) external.push(req.url());
  });
  await page.goto(DIST);
  await expect(page.locator("body")).toHaveAttribute("data-ready", "1", { timeout: 30_000 });
  await expect(page.getByTestId("error")).toHaveCount(0);
  expect(external, "single file: no network requests").toEqual([]);
  if (runLabel) {
    const i = replay.runs.findIndex((r) => r.label === runLabel);
    await page.getByTestId("run-select").selectOption(String(i));
  }
}

test("loads the real M6 replay", async ({ page }) => {
  expect(replay.runs.length).toBeGreaterThan(0);
  for (const r of replay.runs) expect(r.meta.dataset, "exported from a real run").toBe("main");
  await open(page);
  await expect(page.getByTestId("run-select").locator("option")).toHaveCount(replay.runs.length);
  // at replay time 0 the first recorded decision is active; step moves to the second
  const [first, second] = replay.runs[0]!.decisions.map((d) => d.decision.unit_id);
  await expect(page.getByTestId("unit-id")).toHaveText(first!);
  await page.screenshot({ path: `${SHOTS}/01-loaded-first-unit.png` });
  await page.getByTestId("step").click();
  await expect(page.getByTestId("unit-id")).toHaveText(second!);
});

test("play, pause and speed", async ({ page }) => {
  await open(page);
  const clock = page.getByTestId("clock");
  await page.getByTestId("speed").selectOption("16");
  await page.getByTestId("play").click();
  await expect(page.getByTestId("play")).toHaveAttribute("data-state", "playing");
  await page.waitForTimeout(2500);
  const playing = await clock.textContent();
  expect(playing).not.toBe("00:00"); // 16x: ~40 s of recorded time in 2.5 s
  await page.screenshot({ path: `${SHOTS}/02-playing-16x.png` });
  await page.getByTestId("play").click();
  await expect(page.getByTestId("play")).toHaveAttribute("data-state", "paused");
  const paused = await clock.textContent();
  await page.waitForTimeout(1500);
  await expect(clock).toHaveText(paused!);
  // speed changes the rate: 1x advances far less than 16x over the same wall time
  const secs = (t: string | null) => {
    const [m, s] = (t ?? "0:0").split(":").map(Number);
    return (m ?? 0) * 60 + (s ?? 0);
  };
  const before = secs(paused);
  await page.getByTestId("speed").selectOption("1");
  await page.getByTestId("play").click();
  await page.waitForTimeout(2500);
  await page.getByTestId("play").click();
  const slow = secs(await clock.textContent()) - before;
  expect(slow).toBeLessThanOrEqual(4);
  expect(secs(playing)).toBeGreaterThan(20);
});

test("scrub moves the replay clock and the active unit", async ({ page }) => {
  await open(page);
  const run = replay.runs[0]!;
  const lat = run.decisions.map((d) => d.decision.latency_ms);
  const total = lat.reduce((a, b) => a + b, 0);
  await page.getByTestId("scrub").fill("500");
  // expected active unit: last decision starting at or before half the recorded time
  let t = 0;
  let expected = 0;
  for (let i = 0; i < lat.length; i++) {
    if (t <= total / 2) expected = i;
    t += lat[i]!;
  }
  const want = run.decisions[expected]!.decision.unit_id;
  const got = await page.getByTestId("unit-id").textContent();
  const idx = run.decisions.findIndex((d) => d.decision.unit_id === got);
  expect(Math.abs(idx - expected), `scrub to 50% lands near ${want}`).toBeLessThanOrEqual(2);
  await page.screenshot({ path: `${SHOTS}/03-scrubbed-50pct.png` });
});

test("next false forward jumps to a real false forward", async ({ page }) => {
  const withFF = replay.runs
    .map((r) => ({ r, ff: falseForwards(r) }))
    .sort((a, b) => b.ff.length - a.ff.length)[0]!;
  expect(withFF.ff.length).toBeGreaterThan(0);
  await open(page, withFF.r.label);
  // expected: the recorded false forwards in run order after the first unit (active at t=0)
  const expected = withFF.ff.map((d) => d.decision.unit_id).filter(
    (id) => id !== withFF.r.decisions[0]!.decision.unit_id,
  );
  for (const want of expected.slice(0, 3)) {
    await page.getByTestId("next-ff").click();
    await expect(page.getByTestId("verdict")).toHaveText("false forward");
    await expect(page.getByTestId("unit-id")).toHaveText(want);
  }
  await expect(page.getByTestId("false-forwards")).toHaveClass(/alarm/);
  await expect(page.getByTestId("route-forward")).toHaveClass(/on/);
  await page.screenshot({ path: `${SHOTS}/04-false-forward.png` });

  const none = replay.runs.find((r) => falseForwards(r).length === 0);
  if (none) {
    await page.getByTestId("run-select").selectOption(String(replay.runs.indexOf(none)));
    await page.getByTestId("next-ff").click();
    await expect(page.getByTestId("msg")).toHaveText("no false forwards in this run");
    await page.screenshot({ path: `${SHOTS}/05-no-false-forwards.png` });
  }
});

test("doc type filter restricts the stream to that type", async ({ page }) => {
  await open(page);
  const run = replay.runs[0]!;
  const docType = new Map(replay.docs.map((d) => [d.id, d.doc_type]));
  const unitDoc = new Map(run.units.map((u) => [u.id, u.doc_id]));
  const crf = run.decisions.filter((d) => docType.get(unitDoc.get(d.decision.unit_id)!) === "crf_page");
  await page.getByTestId("doctype").selectOption("crf_page");
  await expect(page.locator("#stream .row")).toHaveCount(crf.length);
  const shown = await page.locator("#stream .row .uid").allTextContents();
  expect(shown).toEqual(crf.map((d) => d.decision.unit_id));
  await page.getByTestId("step").click();
  await expect(page.getByTestId("report")).toContainText("crf_page");
  await page.screenshot({ path: `${SHOTS}/06-filter-crf.png` });
});

test("raw vs calibrated toggle and gold span highlighting", async ({ page }) => {
  await open(page);
  const d = replay.runs[0]!.decisions[0]!;
  const bar = page.locator(".judgments .q").first().locator(".bar").first().locator(".p");
  await expect(bar).toHaveText(d.calibrated_probs["pii_present"]!["A"]!.toFixed(3));
  await page.locator("#cal").uncheck();
  const raw = d.decision.answers.find((a) => a.question === "pii_present")!.probs["A"]!;
  await expect(bar).toHaveText(raw.toFixed(3));
  // a PII unit: every highlighted span is a gold span of the document
  const run = replay.runs[0]!;
  const doc = new Map(replay.docs.map((x) => [x.id, x]));
  const k = run.decisions.findIndex((x) => {
    const u = run.units.find((y) => y.id === x.decision.unit_id)!;
    return u.gold.pii_present === "A";
  });
  const u = run.units.find((y) => y.id === run.decisions[k]!.decision.unit_id)!;
  const gold = doc.get(u.doc_id)!.spans.filter((s) => s.end > u.start && s.start < u.end)
    .map((s) => doc.get(u.doc_id)!.text.slice(Math.max(s.start, u.start), Math.min(s.end, u.end)));
  for (let i = 0; i < k; i++) await page.getByTestId("step").click();
  await expect(page.getByTestId("unit-id")).toHaveText(u.id);
  const marks = await page.locator("#report mark").allTextContents();
  expect(marks.length).toBe(gold.length);
  expect(marks).toEqual(gold);
  await page.screenshot({ path: `${SHOTS}/07-raw-probs-gold-spans.png` });
});

test("load replay opens another export", async ({ page }) => {
  await open(page);
  await page.locator("#file").setInputFiles(resolve(HUD, "public/replay.json"));
  await expect(page.getByTestId("run-select").locator("option")).toHaveCount(replay.runs.length);
  await expect(page.getByTestId("unit-id")).toHaveText(replay.runs[0]!.decisions[0]!.decision.unit_id);
});
