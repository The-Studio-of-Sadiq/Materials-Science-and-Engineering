// Shared index of the book's Markdown sources, used by the PDF builder and the figure-plan script.
import { readFileSync, readdirSync, existsSync } from "node:fs";
import { join, dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

export const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
export const BOOK_TITLE = "Materials Science and Engineering";
export const BOOK_SUBTITLE = "Structure, Thermodynamics, Kinetics, Properties, Processing and Design";

/** First chapter of each part; part N runs up to the chapter before part N+1 starts. */
export const PART_STARTS = { 1: 1, 2: 6, 3: 11, 4: 15, 5: 19, 6: 24, 7: 29, 8: 34, 9: 38, 10: 42 };

export function partOfChapter(n) {
  let part = 1;
  for (const [p, start] of Object.entries(PART_STARTS)) if (n >= start) part = Number(p);
  return part;
}

/**
 * Every book file in reading order: each part opener followed by its chapters.
 * id: "1".."49" for chapters, "P1".."P10" for part openers.
 */
export function listParts() {
  const parts = [];
  const chDir = join(ROOT, "Chapters");
  for (const f of readdirSync(chDir)) {
    const m = /^CHAPTER (\d+)\.md$/i.exec(f);
    if (m) {
      const n = Number(m[1]);
      parts.push({ kind: "chapter", id: String(n), order: n * 10 + 1, file: join(chDir, f) });
    }
  }
  const pDir = join(ROOT, "Parts");
  if (existsSync(pDir)) {
    for (const f of readdirSync(pDir)) {
      const m = /^PART (\d+)\.md$/i.exec(f);
      if (m) {
        const n = Number(m[1]);
        parts.push({ kind: "part", id: `P${n}`, order: (PART_STARTS[n] ?? 999) * 10, file: join(pDir, f) });
      }
    }
  }
  parts.sort((a, b) => a.order - b.order);
  for (const p of parts) {
    const text = readFileSync(p.file, "utf8");
    p.title = (/^#\s+(.+)$/m.exec(text)?.[1] ?? p.id).trim();
    p.relPath = p.file.slice(ROOT.length + 1).replace(/\\/g, "/");
  }
  return parts;
}

/** Find a file by id: "5", "05", "chapter 5", "P2", "part 2". */
export function findPart(id) {
  const raw = String(id).trim().toLowerCase();
  const pm = /^(?:part|p)\s*(\d+)$/.exec(raw);
  const norm = pm ? `P${Number(pm[1])}` : String(Number(raw.replace(/^(chapter|ch)\s*/, "")));
  return listParts().find((p) => p.id === norm);
}

export function readPart(part) {
  return readFileSync(part.file, "utf8");
}

/** Planned-figure markers: <!-- FIGURE n | path | kind | caption | content --> */
export function figureMarkers(part, text = readPart(part)) {
  const out = [];
  for (const m of text.matchAll(/<!--\s*FIGURE\s+([\s\S]*?)-->/g)) {
    const [number, path, kind, caption, ...rest] = m[1].split("|").map((s) => s.trim());
    const line = text.slice(0, m.index).split("\n").length;
    out.push({ number, path, kind, caption, content: rest.join(" | ").replace(/^Content:\s*/i, ""), line });
  }
  return out;
}
