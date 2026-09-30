// HUD replay view (docs/specs/hud.md). Replays recorded decisions; never simulates.
import "./style.css";
import embedded from "../data/replay.json.gz?inline";
import type { Replay, ReplayRun } from "./types.gen";
import {
  activeIndex,
  decodeGzipJson,
  duration,
  nextMatching,
  rows as buildRows,
  segments,
  stats,
  thresholdLabel,
  type Row,
} from "./replay";

const SPEEDS = [0.25, 0.5, 1, 2, 4, 8, 16];
const ROUTES = ["forward", "redact", "escalate"] as const;

interface State {
  replay: Replay;
  run: ReplayRun;
  rows: Row[];
  clock: number;
  playing: boolean;
  speed: number;
  docType: string; // "" = all
  calibrated: boolean;
  idx: number;
}

const $ = <T extends HTMLElement>(sel: string): T => {
  const el = document.querySelector<T>(sel);
  if (!el) throw new Error(`missing ${sel}`);
  return el;
};
const esc = (s: string) =>
  s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c] ?? c);
const fmt = (x: number, nd = 1) => (Number.isFinite(x) ? x.toFixed(nd) : "n/a");
const clockText = (ms: number) => {
  const s = Math.floor(ms / 1000);
  return `${String(Math.floor(s / 60)).padStart(2, "0")}:${String(s % 60).padStart(2, "0")}`;
};

/** Rows of the run, optionally one doc type, re-timed on their own recorded latencies. */
function rowsFor(replay: Replay, run: ReplayRun, docType: string): Row[] {
  const all = buildRows(replay, run);
  const kept = docType ? all.filter((r) => r.doc.doc_type === docType) : all;
  let t = 0;
  return kept.map((r, i) => {
    const out = { ...r, i, t };
    t += r.d.decision.latency_ms;
    return out;
  });
}

function shell(replay: Replay): void {
  const types = [...new Set(replay.docs.map((d) => d.doc_type))].sort();
  $("#app").innerHTML = `
  <header class="top" data-testid="topbar">
    <span class="brand">laya-pii-bench ▸ replay</span>
    <label>run <select id="run" data-testid="run-select">${replay.runs
      .map((r, i) => `<option value="${i}">${esc(r.label)} (${esc(r.split)})</option>`)
      .join("")}</select></label>
    <span class="stat">docs <b id="s-docs">0</b></span>
    <span class="stat">units <b id="s-units">0</b></span>
    <span class="stat">p50 <b id="s-p50">-</b> ms</span>
    <span class="stat">units/s <b id="s-rate">-</b></span>
    <span class="stat">forward <b id="s-fwd">-</b></span>
    <span class="stat">false forwards <b id="s-ff" data-testid="false-forwards">0</b></span>
    <span class="stat">replay <b id="s-clock" data-testid="clock">00:00</b> / <span id="s-dur">00:00</span></span>
    <label class="file">load replay <input id="file" type="file" accept=".json,.gz" /></label>
  </header>
  <nav class="controls">
    <button id="play" data-testid="play">▶ play</button>
    <button id="prev" data-testid="step-back" title="previous unit">◀ step</button>
    <button id="next" data-testid="step" title="next unit">step ▶</button>
    <label>speed <select id="speed" data-testid="speed">${SPEEDS.map(
      (s) => `<option value="${s}"${s === 1 ? " selected" : ""}>${s}×</option>`,
    ).join("")}</select></label>
    <input id="scrub" data-testid="scrub" type="range" min="0" max="1000" value="0" />
    <button id="nextff" data-testid="next-ff">next false forward ⏭</button>
    <label>doc type <select id="doctype" data-testid="doctype"><option value="">all</option>${types
      .map((t) => `<option>${esc(t)}</option>`)
      .join("")}</select></label>
    <label><input id="cal" type="checkbox" checked /> calibrated</label>
    <span id="msg" class="msg" data-testid="msg"></span>
  </nav>
  <main class="grid">
    <section class="stream" id="stream" data-testid="stream"></section>
    <section class="graph"><svg id="graph" data-testid="graph" viewBox="0 0 640 340"></svg></section>
    <section class="judgments" id="judgments" data-testid="judgments"></section>
    <section class="report" id="report" data-testid="report"></section>
  </main>`;
}

function renderStream(st: State): void {
  $("#stream").innerHTML = st.rows
    .map(
      (r) =>
        `<div class="row ${r.positive ? "pii" : "clean"} v-${r.verdict.replace(" ", "-")}" data-i="${r.i}">` +
        `<span class="route r-${r.d.route}">${r.d.route[0]?.toUpperCase()}</span>` +
        `<span class="uid">${esc(r.unit.id)}</span><span class="gold">${r.positive ? "PII" : "clean"}</span></div>`,
    )
    .join("");
}

function renderGraph(st: State, r: Row | undefined): void {
  const qs = r ? r.d.decision.answers.map((a) => a.question) : [];
  const qy = (k: number) => 40 + k * (260 / Math.max(1, qs.length - 1 || 1));
  const routeY: Record<string, number> = { forward: 70, redact: 170, escalate: 270 };
  const role = r?.d.triggers.some((t) => t.startsWith("role_"));
  const used = (q: string) => q === "pii_present" || (q === "subject_role" && !!role);
  const edges = qs
    .map(
      (q, k) =>
        `<line x1="150" y1="${qy(k)}" x2="300" y2="170" class="edge ${used(q) ? "on" : ""}" />`,
    )
    .join("");
  const label = r ? thresholdLabel(r, st.run.calib.t_low, st.run.calib.t_high) : "";
  const trig = r ? r.d.triggers.join(", ") : "";
  const routeEdges = ROUTES.map((rt) => {
    const on = r?.d.route === rt;
    return `<line x1="380" y1="170" x2="500" y2="${routeY[rt]}" class="edge ${on ? "on" : ""} ${on ? "dash" : ""}" />`;
  }).join("");
  const nodes = qs
    .map(
      (q, k) =>
        `<g class="node q ${used(q) ? "on" : ""}"><rect x="10" y="${qy(k) - 14}" width="140" height="28" rx="4"/>` +
        `<text x="80" y="${qy(k) + 4}">${esc(q)}</text></g>`,
    )
    .join("");
  const routes = ROUTES.map(
    (rt) =>
      `<g class="node route ${r?.d.route === rt ? "on" : ""}" data-testid="route-${rt}"><rect x="500" y="${routeY[rt]! - 16}" width="130" height="32" rx="4"/>` +
      `<text x="565" y="${routeY[rt]! + 5}">${rt.toUpperCase()}</text></g>`,
  ).join("");
  $("#graph").innerHTML =
    edges +
    routeEdges +
    nodes +
    `<g class="node policy"><rect x="300" y="146" width="80" height="48" rx="6"/><text x="340" y="174">policy</text></g>` +
    routes +
    `<text x="565" y="${r ? (routeY[r.d.route] ?? 170) + 34 : 0}" class="elabel" data-testid="edge-label">${esc(label)}</text>` +
    `<text x="320" y="325" class="trig">${esc(trig)}</text>`;
}

function renderJudgments(st: State, r: Row | undefined): void {
  if (!r) {
    $("#judgments").innerHTML = `<p class="dim">no unit yet: press play or step</p>`;
    return;
  }
  $("#judgments").innerHTML = r.d.decision.answers
    .map((a) => {
      const probs = st.calibrated ? (r.d.calibrated_probs[a.question] ?? a.probs) : a.probs;
      const top = Object.entries(probs).reduce((x, y) => (y[1] > x[1] ? y : x));
      const bars = Object.entries(probs)
        .map(
          ([k, p]) =>
            `<div class="bar ${k === top[0] ? "chosen" : ""}"><span class="k">${esc(k)}</span>` +
            `<span class="b"><i style="width:${(p * 100).toFixed(1)}%"></i></span><span class="p">${p.toFixed(3)}</span></div>`,
        )
        .join("");
      return `<div class="q"><h4>${esc(a.question)} <small>confidence ${a.confidence.toFixed(3)} · top p ${(a.answer_confidence ?? NaN).toFixed(3)}</small></h4>${bars}</div>`;
    })
    .join("");
}

function renderReport(r: Row | undefined): void {
  if (!r) {
    $("#report").innerHTML = "";
    return;
  }
  const body = segments(r)
    .map((s) =>
      s.span
        ? `<mark class="${esc(s.span.category)} ${s.span.counted ? "" : "uncounted"}" title="${esc(s.span.category)}">${esc(s.text)}</mark>`
        : esc(s.text),
    )
    .join("");
  const trunc = r.unit.truncated ? `<span class="chip warn">truncated</span>` : "";
  $("#report").innerHTML =
    `<div class="head"><span class="chip v-${r.verdict.replace(" ", "-")}" data-testid="verdict">${r.verdict}</span>` +
    `<span class="chip">${esc(r.d.route)}</span><span class="chip">${esc(r.doc.doc_type)} · ${esc(r.doc.lang)}</span>${trunc}` +
    `<span class="dim" data-testid="unit-id">${esc(r.unit.id)}</span>` +
    `<span class="dim">gold: ${esc(r.unit.gold.pii_present === "A" ? "PII" : "clean")}, role ${esc(r.unit.gold.subject_role)}</span></div>` +
    `<pre class="text">${body}</pre>`;
}

function update(st: State, force = false): void {
  const i = activeIndex(st.rows, st.clock);
  const changed = i !== st.idx || force;
  st.idx = i;
  $("#s-clock").textContent = clockText(st.clock);
  const scrub = $<HTMLInputElement>("#scrub");
  const dur = duration(st.rows) || 1;
  if (document.activeElement !== scrub) scrub.value = String(Math.round((st.clock / dur) * 1000));
  if (!changed) return;
  const r = i >= 0 ? st.rows[i] : undefined;
  const s = stats(st.rows, i);
  $("#s-docs").textContent = String(i >= 0 ? s.docs : 0);
  $("#s-units").textContent = `${i + 1} / ${st.rows.length}`;
  $("#s-p50").textContent = fmt(s.p50);
  $("#s-rate").textContent = fmt(s.perSec, 2);
  $("#s-fwd").textContent = i >= 0 ? `${(s.forwardRate * 100).toFixed(1)}%` : "-";
  const ff = $("#s-ff");
  ff.textContent = String(i >= 0 ? s.falseForwards : 0);
  ff.classList.toggle("alarm", i >= 0 && s.falseForwards > 0);
  document.querySelectorAll(".row.active").forEach((e) => e.classList.remove("active"));
  document.querySelectorAll(".row.past").forEach((e) => {
    if (Number((e as HTMLElement).dataset.i) > i) e.classList.remove("past");
  });
  for (let k = 0; k <= i; k++) {
    const e = document.querySelector(`.row[data-i="${k}"]`);
    if (e && !e.classList.contains("past")) e.classList.add("past");
  }
  const row = document.querySelector(`.row[data-i="${i}"]`);
  if (row) {
    row.classList.add("active");
    // scroll the stream only (scrollIntoView would also scroll the page and hide the top bar)
    const box = $("#stream");
    const el = row as HTMLElement;
    if (el.offsetTop < box.scrollTop || el.offsetTop > box.scrollTop + box.clientHeight - 20) {
      box.scrollTop = el.offsetTop - box.clientHeight / 2;
    }
  }
  renderGraph(st, r);
  renderJudgments(st, r);
  renderReport(r);
}

function selectRun(st: State, runIdx: number): void {
  st.run = st.replay.runs[runIdx] as ReplayRun;
  st.rows = rowsFor(st.replay, st.run, st.docType);
  st.clock = 0;
  st.idx = -2;
  $("#s-dur").textContent = clockText(duration(st.rows));
  renderStream(st);
  update(st, true);
}

function jumpTo(st: State, i: number): void {
  const r = st.rows[i];
  if (!r) return;
  st.clock = r.t;
  update(st);
}

function wire(st: State): void {
  const play = $<HTMLButtonElement>("#play");
  const setPlaying = (p: boolean) => {
    st.playing = p;
    play.textContent = p ? "❚❚ pause" : "▶ play";
    play.dataset.state = p ? "playing" : "paused";
  };
  setPlaying(false);
  play.onclick = () => setPlaying(!st.playing);
  $<HTMLButtonElement>("#next").onclick = () => jumpTo(st, Math.min(st.idx + 1, st.rows.length - 1));
  $<HTMLButtonElement>("#prev").onclick = () => jumpTo(st, Math.max(st.idx - 1, 0));
  $<HTMLSelectElement>("#speed").onchange = (e) => {
    st.speed = Number((e.target as HTMLSelectElement).value);
  };
  $<HTMLInputElement>("#scrub").oninput = (e) => {
    st.clock = (Number((e.target as HTMLInputElement).value) / 1000) * duration(st.rows);
    update(st);
  };
  $<HTMLButtonElement>("#nextff").onclick = () => {
    const j = nextMatching(st.rows, st.idx, (r) => r.verdict === "false forward");
    $("#msg").textContent = j < 0 ? "no false forwards in this run" : "";
    if (j >= 0) {
      setPlaying(false);
      jumpTo(st, j);
    }
  };
  $<HTMLSelectElement>("#run").onchange = (e) => {
    setPlaying(false);
    selectRun(st, Number((e.target as HTMLSelectElement).value));
  };
  $<HTMLSelectElement>("#doctype").onchange = (e) => {
    st.docType = (e.target as HTMLSelectElement).value;
    setPlaying(false);
    selectRun(st, Number($<HTMLSelectElement>("#run").value));
  };
  $<HTMLInputElement>("#cal").onchange = (e) => {
    st.calibrated = (e.target as HTMLInputElement).checked;
    update(st, true);
  };
  $<HTMLInputElement>("#file").onchange = async (e) => {
    const f = (e.target as HTMLInputElement).files?.[0];
    if (!f) return;
    const buf = await f.arrayBuffer();
    const replay = f.name.endsWith(".gz")
      ? await decodeGzipJson<Replay>(buf)
      : (JSON.parse(new TextDecoder().decode(buf)) as Replay);
    start(replay);
  };
  let last = performance.now();
  const tick = (now: number) => {
    const dt = now - last;
    last = now;
    if (st.playing) {
      st.clock = Math.min(st.clock + dt * st.speed, duration(st.rows));
      if (st.clock >= duration(st.rows)) setPlaying(false);
      update(st);
    }
    requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
}

let current: State | undefined;

function start(replay: Replay): void {
  if (!replay.runs.length) throw new Error("replay has no runs");
  shell(replay);
  const st: State = {
    replay,
    run: replay.runs[0] as ReplayRun,
    rows: [],
    clock: 0,
    playing: false,
    speed: 1,
    docType: "",
    calibrated: true,
    idx: -2,
  };
  current = st;
  wire(st);
  selectRun(st, 0);
  document.body.dataset.ready = "1";
}

async function boot(): Promise<void> {
  const buf = await (await fetch(embedded)).arrayBuffer();
  start(await decodeGzipJson<Replay>(buf));
}

boot().catch((err: unknown) => {
  $("#app").innerHTML = `<pre class="error" data-testid="error">${esc(String(err))}</pre>`;
});

export { current };
