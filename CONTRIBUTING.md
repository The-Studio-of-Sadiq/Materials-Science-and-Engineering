# House Style — Materials Science and Engineering

The master outline is [`TOC.md`](TOC.md). It is fixed: 11 parts, 59 chapters. Do not skip, merge or rename listed topics; every bullet in the TOC must be covered by a section or subsection of its chapter.

## Files

- Chapters: `Chapters/CHAPTER N.md` (no zero padding). Part openers: `Parts/PART N.md` (N = 1..11).
- Markdown only. Math is GitHub-style LaTeX: `$...$` inline, `$$...$$` display (display math on its own lines). Never `\(...\)` or `\[...\]`.
- In tables, never put a raw `|` inside math; use `\lvert ... \rvert` or `\Vert`.
- Use `\mathrm{}` for units in math, e.g. `$\rho=1.68\times10^{-8}\ \Omega\,\mathrm{m}$`. Prefer plain text units outside math.
- **No exercises, problems, quizzes or answer sections.** Worked examples inside the text are welcome.

## Chapter layout

```
# Chapter N — Title

*Part X · Part title*

Opening paragraph that starts from an engineering problem (a failed part, a design choice).

> **Question 1?**
> **Question 2?**

| Concept | Engineering destination |
|---|---|
| ... | ... |

**Roadmap.** Short arrow-chain through the sections (N.1 → N.2–N.3 → ...).

---

## N.1 Section title
...
---
## N.2 ...
...
## What remains open

| Open question | Where it is answered |
|---|---|

**Next:** one sentence pointing to the next chapter.
```

Use `### ` subsections freely inside sections. Separate `## ` sections with `---`.

## Voice and method

1. **Start from the engineering problem**, not a definition: a bridge girder that cracked in winter, a turbine blade that crept, a hip implant that loosened, a pipeline that corroded, a polymer part that warped out of the mould. Draw examples from every engineering field (mechanical, civil, aerospace, chemical, biomedical, energy, electronics), not one.
2. **Structure → property → performance.** Every property is traced to the structure (atomic, micro, macro) that produces it and to the processing that set that structure. Then to the component or system consequence.
3. **Every concept gets an engineering destination.** The opening table maps concepts to where an engineer uses them.
4. **Status box after every important law or rule**, using exactly one of four labels:
   - **Fundamental** — follows from underlying physics (e.g. thermodynamics, Bloch's theorem, linear elasticity from energy).
   - **Derived** — a mathematical or physical consequence of more basic results.
   - **Approximate** — valid under stated simplifying assumptions (state them and the domain).
   - **Empirical** — fitted to observation (Hall–Petch, Paris law, Basquin, Coffin–Manson, Larson–Miller, Abrams' law for concrete, WLF fitted constants, Archard wear...).

   Format:
   ```
   > **Status of the principle: Name**
   > *Empirical.* One sentence on why and where it holds.
   ```
5. **Show why an approximation works, then where it fails.** A failure of a simple rule is missing physics or a changed regime, never an arbitrary exception.
6. **Real numbers.** Give representative property values (with units) in tables: steel yield strengths, Al alloy tempers, alumina toughness, PMMA Tg, CFRP ply stiffnesses, concrete strength classes, corrosion rates. Values must be correct to typical handbook accuracy; say "typical" or give ranges where they vary with grade or processing. Recompute every worked example.
7. **Worked examples** as `**Worked example — title.**` paragraphs with full numbers.
8. **Respect the boundaries** (see the table at the end of `TOC.md`). This book is self-contained for materials science, but the laws of thermodynamics, bonding and electrochemistry fundamentals belong to the Advanced Chemistry book and quantum foundations to Engineering Physics: recap them in a paragraph where needed, do not re-derive them. Add a short `> **Boundary.**` note where a chapter touches those.
9. Do not overclaim. State domains of validity.

## Figure markers

Planned figures are recorded in the chapter as an HTML comment on its own line, at the exact point the figure should appear (invisible in the PDF until the figure exists):

```
<!-- FIGURE 5.3 | figures/ch05/fig-5-3-cte-mismatch.png | plot | Caption sentence. | Content: what is drawn, axes, data ranges, labels. -->
```

Fields: number, target path, kind (`plot`, `schematic`, `crystal`, `micrograph-style`, `band-diagram`, `flowchart`, `map` for Ashby-style property maps, `table-graphic`), caption, and a brief content spec for whoever draws it.

Figures are drawn by `figures/scripts/chNN.py` (shared style in `figures/scripts/figstyle.py`) and saved to the marker's path. `node scripts/insert-figures.mjs` then places each drawn figure directly below its marker; the marker stays as the figure's specification:

```
<!-- FIGURE 5.3 | ... -->

![Figure 5.3 — Caption](../figures/ch05/fig-5-3-cte-mismatch.png)

*Figure 5.3 — Caption.*
```

The full plan is collected in [`FIGURES.md`](FIGURES.md) (`node scripts/figure-plan.mjs`).
