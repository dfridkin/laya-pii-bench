import { defineConfig } from "vite";
import { viteSingleFile } from "vite-plugin-singlefile";

// One self-contained file (docs/specs/hud.md): scripts, styles and the gzipped replay are inlined.
export default defineConfig({
  plugins: [viteSingleFile()],
  assetsInclude: ["**/*.gz"],
  publicDir: false, // public/replay.json is the export input; the build embeds data/replay.json.gz
  build: { assetsInlineLimit: 100_000_000, chunkSizeWarningLimit: 100_000 },
});
