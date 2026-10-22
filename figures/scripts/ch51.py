"""Figures for Chapter 51 — Joining, Packaging, and Interconnect Materials.

Run from the repository root:  python figures/scripts/ch51.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle, Ellipse, FancyArrowPatch, Arc

RED = "#C0392B"
CU = "#D9822B"
SI = "#B9C4CF"
SOLDER = "#C8CCD2"
UF = "#E9DFC4"
EMC = "#4A4A4A"


def leader(ax, text, xy, xytext, fs=7.5, color=INK, **kw):
    ax.annotate(text, xy=xy, xytext=xytext, fontsize=fs, color=color,
                arrowprops=dict(arrowstyle="-", lw=0.5, color="0.35"), **kw)


# ---------------------------------------------------------------- Figure 51.1
def _joint_panel(ax, aged, rng):
    W, H = 10.0, 12.0
    ax.set_xlim(0, W); ax.set_ylim(0, H); ax.set_aspect("equal")
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(True); s.set_color(INK)
    c_cu, c_31, c_65, c_sn = "#6E6E6E", "#8C8C8C", "#A9A9A9", "#D2D2D2"
    ycu = 3.0
    ax.add_patch(Rectangle((0, 0), W, H, fc=c_sn, ec="none"))
    x = np.linspace(0, W, 400)
    if not aged:
        t31 = 0.3 + 0.03 * np.sin(x * 3)
        # scalloped Cu6Sn5: mean ~2 um, scallops protrude into solder
        centers = np.cumsum(rng.uniform(1.2, 2.0, 10)) - 0.6
        top = np.full_like(x, 0.6)
        for c in centers:
            r = rng.uniform(0.6, 1.0)
            top = np.maximum(top, 1.0 + 1.6 * np.sqrt(np.clip(1 - ((x - c) / r) ** 2, 0, 1)))
        y31 = ycu + t31
        y65 = y31 + top
    else:
        t31 = 2.0 + 0.08 * np.sin(x * 2.1)
        y31 = ycu + t31
        y65 = y31 + 3.5 + 0.35 * np.sin(x * 1.3 + 0.5) + 0.15 * np.sin(x * 4.1)
    ax.fill_between(x, 0, ycu, color=c_cu, lw=0)
    ax.fill_between(x, ycu, y31, color=c_31, lw=0)
    ax.fill_between(x, y31, y65, color=c_65, lw=0)
    ax.plot(x, y31, color="#555555", lw=0.5)
    ax.plot(x, y65, color="#555555", lw=0.6)
    # beta-Sn matrix with Ag3Sn particles and Cu6Sn5 rods
    n_ag = 70 if not aged else 22
    for _ in range(n_ag):
        px, py = rng.uniform(0.2, W - 0.2), rng.uniform(np.max(y65) + 0.3, H - 0.3)
        r = rng.uniform(0.05, 0.12) if not aged else rng.uniform(0.15, 0.32)
        ax.add_patch(Circle((px, py), r, fc="white", ec="#999999", lw=0.3))
    for _ in range(9 if not aged else 5):
        px, py = rng.uniform(0.5, W - 1), rng.uniform(np.max(y65) + 0.6, H - 0.8)
        ang = rng.uniform(0, np.pi)
        L = rng.uniform(0.6, 1.3) * (1 if not aged else 1.4)
        ax.plot([px, px + L * np.cos(ang)], [py, py + L * np.sin(ang)], color=c_65, lw=2.5 if not aged else 3.5,
                solid_capstyle="round")
    if aged:
        for _ in range(26):
            vx = rng.uniform(0.2, W - 0.2)
            vy = ycu + rng.choice([0.08, 0.1, rng.uniform(0.2, 1.4)])
            ax.add_patch(Circle((vx, vy), rng.uniform(0.06, 0.13), fc="black", ec="none"))
    return ycu, y31, y65


def solder_imc():
    fig, axs = plt.subplots(1, 2, figsize=(6.8, 4.2))
    rng = np.random.default_rng(12)
    titles = ["(a) As reflowed", "(b) After 1000 h at 150 °C"]
    for k, ax in enumerate(axs):
        aged = k == 1
        ycu, y31, y65 = _joint_panel(ax, aged, rng)
        ax.set_title(titles[k], fontsize=9)
        # scale bar
        ax.add_patch(Rectangle((4.2, 10.45), 5.6, 1.25, fc="white", ec=INK, lw=0.5, zorder=5))
        ax.plot([4.5, 9.5], [11.35, 11.35], color="black", lw=3, zorder=6)

        ax.text(7.0, 11.1, "5 µm", fontsize=8, ha="center", va="top", zorder=6)
        ax.text(0.3, 1.5, "Cu pad", fontsize=8, color="white")
        ax.text(0.3, 9.6, "β-Sn", fontsize=8)
    # labels with leaders, panel (a)
    a, b = axs
    leader(a, "Cu$_3$Sn ≈ 0.3 µm", (1.6, 3.15), (-4.6, 3.6))
    leader(a, "scalloped\nCu$_6$Sn$_5$ ≈ 2 µm", (2.4, 4.3), (-4.6, 5.3))
    leader(a, "Ag$_3$Sn\nparticles", (1.6, 8.0), (-4.6, 8.0))
    leader(a, "Cu$_6$Sn$_5$ rods", (3.5, 9.0), (-4.6, 10.4))
    leader(b, "Cu$_3$Sn ≈ 2 µm", (9.0, 4.0), (10.6, 4.0))
    leader(b, "Cu$_6$Sn$_5$ ≈ 3.5 µm", (9.0, 6.6), (10.6, 6.6))
    leader(b, "Kirkendall\nvoids", (9.2, 3.1), (10.6, 2.0))
    leader(b, "coarsened\nAg$_3$Sn", (9.0, 9.3), (10.6, 9.3))
    b.text(10.6, 5.3, "total ≈ 5.5 µm", fontsize=7.5, color="0.3")
    # diffusion arrows (b)
    b.annotate("", xy=(0.9, 8.6), xytext=(0.9, 3.3),
               arrowprops=dict(arrowstyle="-|>", lw=2.0, color=COLORS[1], mutation_scale=10))
    b.text(1.15, 8.0, "Cu (fast)", fontsize=7.5, color=COLORS[1], fontweight="bold")
    b.annotate("", xy=(3.9, 5.6), xytext=(3.9, 8.6),
               arrowprops=dict(arrowstyle="-|>", lw=1.0, color=COLORS[0], mutation_scale=8))
    b.text(4.1, 6.3, "Sn (slow)", fontsize=7.5, color=COLORS[0], fontweight="bold")
    b.annotate("", xy=(6.0, 3.1), xytext=(6.0, 6.2),
               arrowprops=dict(arrowstyle="-|>", lw=1.0, color="black", mutation_scale=8, ls="--"))
    b.text(6.25, 4.3, "vacancies\n→ Cu", fontsize=7, color="black")
    fig.tight_layout(w_pad=6.5)
    save(fig, "51", "fig-51-1-solder-joint-imc-kirkendall")


# ---------------------------------------------------------------- Figure 51.2
def flip_chip():
    fig, ax = schematic(6.8, 3.8, xlim=(-175, 650), ylim=(-130, 215))
    IMC = "#8B5A2B"
    # substrate (bottom)
    ax.add_patch(Rectangle((0, -95), 470, 45, fc="#7A9A6A", ec=INK, lw=0.6))   # core
    ax.add_patch(Rectangle((0, -50), 470, 36, fc="#B5C99A", ec=INK, lw=0.6))   # build-up
    for y in (-44, -26):
        for xx in range(15, 460, 75):
            ax.add_patch(Rectangle((xx, y), 40, 4, fc=CU, ec="none"))
    ax.text(465, -62, "substrate core", fontsize=7, color="white", va="center", ha="right")
    ax.text(8, -34, "build-up layers", fontsize=7, va="center")
    # solder mask with openings
    ax.add_patch(Rectangle((0, -14), 470, 14, fc="#3E7D3E", ec=INK, lw=0.6))
    gap = 80
    # underfill with fillet
    fil = [[0, 0], [490, 0], [478, 8], [466, 25], [457, 50], [452, gap], [0, gap]]
    ax.add_patch(Polygon(fil, fc=UF, ec=INK, lw=0.5))
    rng = np.random.default_rng(3)
    for _ in range(190):
        px, py = rng.uniform(4, 470), rng.uniform(3, gap - 3)
        if px > 452 and py > 60 - (px - 452) * 3:
            continue
        ax.add_patch(Circle((px, py), rng.uniform(1.2, 2.8), fc="white", ec="#AA9F80", lw=0.3, zorder=2))
    # die (face down): passivation/polyimide, BEOL with low-k, Si
    ax.add_patch(Rectangle((0, gap), 450, 8, fc="#F0E68C", ec=INK, lw=0.4))
    ax.add_patch(Rectangle((0, gap + 8), 450, 14, fc="#C9B3E0", ec=INK, lw=0.4, hatch="---"))
    ax.add_patch(Rectangle((0, gap + 22), 450, 60, fc=SI, ec=INK, lw=0.8))
    ax.text(120, gap + 52, "Si die (face down)", fontsize=8.5, ha="center", va="center")
    # solder bumps
    for xb in (70, 220):
        ax.add_patch(Rectangle((xb - 50, -4), 100, 4, fc=CU, ec="none", zorder=3))                 # substrate pad
        ax.add_patch(Ellipse((xb, 39), 104, 80, fc=SOLDER, ec=INK, lw=0.6, zorder=3))
        ax.add_patch(Rectangle((xb - 34, gap - 8), 68, 8, fc="#5F7A8A", ec="none", zorder=4))      # UBM
        ax.add_patch(Rectangle((xb - 38, gap), 76, 5, fc="#A0A0A0", ec="none", zorder=4))           # Al pad
        ax.add_patch(Rectangle((xb - 34, gap - 11), 68, 3, fc=IMC, ec="none", zorder=4))
        ax.add_patch(Rectangle((xb - 40, 0), 80, 3, fc=IMC, ec="none", zorder=4))
    ax.text(220, 36, "SAC bump\n≈ 100 µm", fontsize=7, ha="center", va="center", zorder=5)
    # copper pillars
    for xp in (310, 360, 410):
        ax.add_patch(Rectangle((xp - 18, -4), 36, 4, fc=CU, ec="none", zorder=3))
        ax.add_patch(Polygon([[xp - 15, 3], [xp + 15, 3], [xp + 14, 25], [xp - 14, 25]],
                             fc=SOLDER, ec=INK, lw=0.5, zorder=3))                              # SnAg cap
        ax.add_patch(Rectangle((xp - 16, 0), 32, 3, fc=IMC, ec="none", zorder=4))
        ax.add_patch(Rectangle((xp - 14, 25), 28, 2.5, fc=IMC, ec="none", zorder=4))
        ax.add_patch(Rectangle((xp - 14, 27.5), 28, 4.5, fc="#4F6D7A", ec="none", zorder=4))     # Ni
        ax.add_patch(Rectangle((xp - 14, 32), 28, 46, fc=CU, ec=INK, lw=0.5, zorder=4))          # pillar
        ax.add_patch(Rectangle((xp - 17, gap - 2), 34, 7, fc="#A0A0A0", ec="none", zorder=4))
    # mismatch stress
    ax.annotate("", xy=(410, gap + 40), xytext=(410, gap + 6),
                arrowprops=dict(arrowstyle="-|>", lw=2.2, color=RED, mutation_scale=12), zorder=6)
    ax.text(400, gap + 52, "mismatch stress\ntransmitted to low-k", fontsize=7, color=RED, ha="right",
            va="center", zorder=6)
    # left-column labels (bump stack)
    lx = -170
    leader(ax, "Al pad", (36, gap + 3), (lx, 165), fs=7.2, va="center")
    leader(ax, "UBM Ti / Ni / Cu\n(0.1 / 2 / 0.5 µm)", (40, gap - 4), (lx, 122), fs=7.2, va="center")
    leader(ax, "Cu$_6$Sn$_5$ IMC\n(both interfaces)", (45, gap - 10), (lx, 72), fs=7.2, va="center")
    leader(ax, "SAC solder bump", (25, 40), (lx, 28), fs=7.2, va="center")
    leader(ax, "solder mask", (10, -7), (lx, -8), fs=7.2, va="center")
    # right-column labels
    rx = 498
    leader(ax, "BEOL with low-k\ndielectrics", (445, gap + 15), (rx, 180), fs=7.2, va="center")
    leader(ax, "passivation +\npolyimide", (445, gap + 4), (rx, 138), fs=7.2, va="center")
    leader(ax, "Cu pillar ≈ 40 µm tall", (423, 60), (rx, 103), fs=7.2, va="center")
    leader(ax, "Ni barrier", (423, 30), (rx, 75), fs=7.2, va="center")
    leader(ax, "thin SnAg cap + IMC", (424, 14), (rx, 47), fs=7.2, va="center")
    leader(ax, "underfill: epoxy +\n50–70 wt% silica,\nfillet at die edge", (470, 10), (rx, -5), fs=7.2,
           va="center")
    # pitch arrows (in the core)
    yp = -86
    for (xa, xb, t) in [(70, 220, "bump pitch 150 µm"), (310, 360, "pillar pitch 50 µm")]:
        ax.annotate("", xy=(xa, yp), xytext=(xb, yp), arrowprops=dict(arrowstyle="<|-|>", lw=0.7, color="white",
                                                                      mutation_scale=7))
        ax.text((xa + xb) / 2, yp + 3, t, fontsize=6.8, color="white", ha="center", va="bottom")
    # CTE line at top
    ax.text(235, -115, "CTE (ppm/K):  Si 2.6   Cu 17   solder 22   underfill 25–30   substrate 15–17",
            fontsize=7.3, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="0.6", lw=0.6))
    save(fig, "51", "fig-51-2-flip-chip-cu-pillar-underfill")


# ---------------------------------------------------------------- Figure 51.3
def power_module():
    fig, ax = schematic(6.8, 5.0, xlim=(0, 13.6), ylim=(0, 10))
    x0, x1 = 0.3, 6.3
    # (name, y0, h, colour, x-range)
    layers = [
        ("heat sink", 0.4, 1.0, "#9AA7B0", (x0, x1)),
        ("TIM", 1.4, 0.3, "#E0C9A6", (x0 + 0.2, x1 - 0.2)),
        ("baseplate", 1.7, 1.1, "#C77B30", (x0 + 0.2, x1 - 0.2)),
        ("subst. solder", 2.8, 0.3, SOLDER, (x0 + 0.7, x1 - 0.7)),
        ("bottom Cu", 3.1, 0.45, CU, (x0 + 0.7, x1 - 0.7)),
        ("ceramic", 3.55, 0.55, "#F4F1E8", (x0 + 0.5, x1 - 0.5)),
    ]
    gel = Rectangle((x0 + 0.35, 2.8), x1 - x0 - 0.7, 4.6, fc="#CFE8F5", ec="none", alpha=0.6, zorder=0)
    ax.add_patch(gel)
    for name, y, h, c, (a, b) in layers:
        ax.add_patch(Rectangle((a, y), b - a, h, fc=c, ec=INK, lw=0.6))
    for a, b in [(x0 + 0.7, 4.0), (4.3, x1 - 0.7)]:
        ax.add_patch(Rectangle((a, 4.1), b - a, 0.45, fc=CU, ec=INK, lw=0.6))
    ax.add_patch(Rectangle((1.4, 4.55), 2.2, 0.25, fc=SOLDER, ec=INK, lw=0.5))
    ax.add_patch(Rectangle((1.4, 4.8), 2.2, 0.5, fc="#556070", ec=INK, lw=0.6))
    ax.text(2.5, 5.05, "SiC / Si die", fontsize=7, ha="center", va="center", color="white")
    # housing walls
    ax.add_patch(Rectangle((x0 + 0.2, 2.8), 0.15, 4.8, fc="0.3", ec="none"))
    ax.add_patch(Rectangle((x1 - 0.35, 2.8), 0.15, 4.8, fc="0.3", ec="none"))
    ax.text(3.3, 7.0, "silicone gel encapsulant", fontsize=7.5, ha="center", color="#2B5C7A")
    # bond wires from die to right Cu island
    for dx in (0.0, 0.25, 0.5):
        t = np.linspace(0, 1, 50)
        xs = 1.9 + dx + (4.7 - 1.9) * t
        ys = 5.3 + 1.2 * np.sin(np.pi * t) - (5.3 - 4.55) * t
        ax.plot(xs, ys, color="#888888", lw=1.8)
    # labels with horizontal leaders
    lx = 6.9
    rows = [
        (6.35, "Al heavy bond wires, 300–500 µm dia.", (4.3, 6.1)),
        (5.6, "die: SiC 0.2 mm (CTE 4, k 370) or Si (2.6, 150)", (3.6, 5.05)),
        (4.95, "die attach: SAC 50–100 µm (k 58) or sintered Ag 30 µm (k ≈ 200)", (3.6, 4.68)),
        (4.35, "top Cu 0.3 mm, patterned; CTE 17, k 390", (5.6, 4.33)),
        (3.8, "ceramic (see table): Al$_2$O$_3$ / AlN / Si$_3$N$_4$", (5.8, 3.82)),
        (3.3, "bottom Cu 0.3 mm", (5.6, 3.32)),
        (2.85, "substrate solder 100–200 µm", (5.6, 2.95)),
        (2.25, "baseplate 3 mm: Cu (CTE 17) or AlSiC (CTE 7)", (6.1, 2.25)),
        (1.55, "TIM grease 50–100 µm, k 1–5 W/m K", (6.1, 1.55)),
        (0.9, "heat sink", (6.3, 0.9)),
    ]
    for y, t, xy in rows:
        ax.annotate(t, xy=xy, xytext=(lx, y), fontsize=7.0, va="center",
                    arrowprops=dict(arrowstyle="-", lw=0.5, color="0.4", shrinkA=1, shrinkB=0))
    # ceramic table (top right)
    rowsT = [("ceramic", "t (mm)", "k (W/m K)", "CTE (ppm/K)"),
             ("Al$_2$O$_3$ 96 %", "0.38", "24", "6.8–7.1"),
             ("AlN", "0.63", "170", "4.5–4.7"),
             ("Si$_3$N$_4$", "0.32", "90", "2.6–3.2")]
    tx = [7.0, 9.1, 10.5, 12.4]
    for i, r in enumerate(rowsT):
        for j, c in enumerate(r):
            ax.text(tx[j], 9.4 - i * 0.42, c, fontsize=7, ha="left" if j == 0 else "center",
                    fontweight="bold" if i == 0 else "normal")
    ax.plot([7.0, 13.2], [9.2, 9.2], color="0.5", lw=0.5)
    # failure-site markers and legend
    fails = [(3.3, 6.45, "1"), (1.2, 4.68, "2"), (4.15, 3.72, "3"), (0.75, 2.95, "4"), (3.3, 1.55, "5")]
    for x, y, n in fails:
        ax.add_patch(Circle((x, y), 0.19, fc=RED, ec="white", lw=0.8, zorder=6))
        ax.text(x, y, n, fontsize=6.5, color="white", ha="center", va="center", zorder=7, fontweight="bold")
    ax.text(0.3, 9.6, "Likely failure sites\n1  wire lift-off\n2  die-attach fatigue\n"
                      "3  ceramic conchoidal crack at Cu edge\n4  baseplate-solder fatigue\n5  TIM pump-out",
            fontsize=7.0, va="top", color=RED, linespacing=1.25)
    ax.text(4.8, 9.6, "not to scale", fontsize=7, style="italic", color="0.4", va="top")
    save(fig, "51", "fig-51-3-power-module-stack")


# ---------------------------------------------------------------- Figure 51.4
def fr4_z():
    fig, ax = new_fig(6.4, 4.2)
    T = np.linspace(25, 288, 500)

    def exp_pct(T, Tg, a1, a2):
        return 100 * np.where(T <= Tg, a1 * (T - 25), a1 * (Tg - 25) + a2 * (T - Tg)) * 1e-6
    ax.axvspan(217, 260, color=COLORS[4], alpha=0.15, lw=0)
    ax.text(238.5, 4.85, "lead-free\nreflow", ha="center", va="top", fontsize=8)
    curves = [("standard FR-4 (T$_g$ 140 °C, 60/280 ppm/K)", 140, 60, 280, COLORS[1]),
              ("high-T$_g$ filled FR-4 (T$_g$ 170 °C, 50/250 ppm/K)", 170, 50, 250, COLORS[0]),
              ("low-loss hydrocarbon/ceramic (≈ 32 ppm/K)", 1e9, 32, 32, COLORS[2]),
              ("copper (17 ppm/K)", 1e9, 17, 17, "0.3")]
    for lab, Tg, a1, a2, c in curves:
        e = exp_pct(T, Tg, a1, a2)
        ax.plot(T, e, color=c, label=lab, ls="--" if c == "0.3" else "-")
        if Tg < 300:
            eg = exp_pct(np.array([Tg]), Tg, a1, a2)[0]
            ax.plot(Tg, eg, "o", mfc="white", mec=c, ms=6, mew=1.4)
            ax.text(Tg, eg + 0.12, "T$_g$", fontsize=7.5, color=c, ha="center", va="bottom")
        e260 = exp_pct(np.array([260.0]), Tg, a1, a2)[0]
        ax.plot(260, e260, "s", color=c, ms=3.5)
        ax.text(256, e260 + 0.08, f"{e260:.2f} %", fontsize=7.5, color=c, ha="right", va="bottom",
                bbox=dict(fc="white", ec="none", pad=0.5, alpha=0.85))
        print(f"{e260:.3f} % at 260 C")
    ax.set_xlim(25, 288); ax.set_ylim(0, 5)
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("z-axis expansion from 25 °C (%)")
    ax.legend(loc="upper left", fontsize=7.5)

    # inset: plated through-hole cross-section
    ins = ax.inset_axes([0.04, 0.17, 0.24, 0.40])
    ins.set_xlim(0, 10); ins.set_ylim(0, 12); ins.set_aspect("equal"); ins.axis("off")
    ins.add_patch(Rectangle((0, 2), 10, 8, fc="#C8D9A8", ec=INK, lw=0.5))
    ins.add_patch(Rectangle((3.6, 2), 2.8, 8, fc="white", ec="none"))
    for xx in (3.3, 6.4):
        ins.add_patch(Rectangle((xx, 2), 0.3, 8, fc=CU, ec="none"))
    for y in (1.6, 10):
        ins.add_patch(Rectangle((1.6, y), 2.0, 0.4, fc=CU, ec="none"))
        ins.add_patch(Rectangle((6.4, y), 2.0, 0.4, fc=CU, ec="none"))
    for xx in (1.6, 8.3):
        ins.annotate("", xy=(xx, 11.6), xytext=(xx, 8.2), arrowprops=dict(arrowstyle="-|>", lw=0.8, color=COLORS[1], mutation_scale=6))
        ins.annotate("", xy=(xx, 0.4), xytext=(xx, 3.8), arrowprops=dict(arrowstyle="-|>", lw=0.8, color=COLORS[1], mutation_scale=6))
    for (x, y) in [(3.45, 6.0), (6.55, 6.0), (3.45, 10.1), (6.55, 1.9)]:
        ins.plot(x, y, marker="x", color=RED, ms=6, mew=1.6)
    ins.text(5.0, 6.0, "PTH\nbarrel", fontsize=6, ha="center", va="center")
    ax.text(0.29, 0.40, "resin expands in z;\nbarrel cracks (×) at mid-\nheight and pad knee", fontsize=7,
             ha="left", va="center", transform=ax.transAxes)
    save(fig, "51", "fig-51-4-fr4-z-axis-expansion")


# ---------------------------------------------------------------- Figure 51.5
def _dnp_side(ax, shear, title):
    ax.set_xlim(-6.3, 6.3); ax.set_ylim(-1.6, 3.2); ax.set_aspect("equal"); ax.axis("off")
    h = 0.6
    ax.add_patch(Rectangle((-6.0, -1.0), 12.0, 1.0, fc="#C8D9A8", ec=INK, lw=0.7))
    ax.add_patch(Rectangle((-4.6, h), 9.2, 1.0, fc="#EDE7D9", ec=INK, lw=0.7))
    ax.text(0, h + 0.5, r"ceramic component, CTE $\alpha_c$", fontsize=7.5, ha="center", va="center")
    ax.text(-5.8, -0.72, r"PCB, CTE $\alpha_b>\alpha_c$", fontsize=7.5, va="center")
    xs = np.array([-4.0, -2.0, 0.0, 2.0, 4.0])
    for x in xs:
        dx = shear * x
        ax.add_patch(Polygon([[x - 0.35 + dx, 0], [x + 0.35 + dx, 0], [x + 0.35, h], [x - 0.35, h]],
                             fc=SOLDER, ec=INK, lw=0.7))
        if shear and x != 0:
            ax.annotate("", xy=(x + dx * 3.0, -0.3), xytext=(x, -0.3),
                        arrowprops=dict(arrowstyle="-|>", lw=1.0, color=COLORS[1], mutation_scale=7))
    ax.plot([0, 0], [-1.2, h + 1.25], color="0.4", lw=0.8, ls="-.")
    ax.text(0, h + 1.35, "neutral point", fontsize=7, ha="center", va="bottom")
    ax.set_title(title, fontsize=8.5, loc="left")
    return h


def dnp():
    fig = plt.figure(figsize=(6.8, 4.8))
    a1 = fig.add_axes([0.0, 0.52, 0.62, 0.44])
    a2 = fig.add_axes([0.0, 0.03, 0.62, 0.44])
    h = _dnp_side(a1, 0.0, "(a) reference temperature")
    a1.annotate("", xy=(4.0, h + 1.15), xytext=(0, h + 1.15),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.7, mutation_scale=7))
    a1.text(2.0, h + 1.2, "$L_D$ (DNP)", fontsize=7.5, ha="center", va="bottom")
    a1.annotate("", xy=(4.75, 0), xytext=(4.75, h), arrowprops=dict(arrowstyle="<|-|>", lw=0.6, mutation_scale=6))
    a1.text(4.85, h / 2, "h", fontsize=8, va="center")
    _dnp_side(a2, 0.09, r"(b) after heating by $\Delta T$ (board expands more)")
    a2.text(4.4, -1.45, r"$\Delta u=\Delta\alpha\,\Delta T\,L_D$", fontsize=8, ha="center", color=COLORS[1])
    a2.annotate(r"$\gamma\approx\Delta\alpha\,\Delta T\,L_D/h$", xy=(-4.15, 0.3), xytext=(-6.2, 2.4), fontsize=8,
                arrowprops=dict(arrowstyle="-", lw=0.5))
    # plan-view inset: BGA strain map
    ip = fig.add_axes([0.66, 0.50, 0.32, 0.44])
    n = 8
    g = np.arange(n) - (n - 1) / 2
    X, Y = np.meshgrid(g, g)
    r = np.sqrt(X**2 + Y**2)
    xx, yy = np.meshgrid(np.linspace(-4.2, 4.2, 200), np.linspace(-4.2, 4.2, 200))
    ip.contourf(xx, yy, np.sqrt(xx**2 + yy**2), levels=12, cmap="YlOrRd", alpha=0.45)
    ip.scatter(X, Y, s=28, c="white", edgecolors=INK, linewidths=0.5, zorder=3)
    corners = [(g[0], g[0]), (g[0], g[-1]), (g[-1], g[0]), (g[-1], g[-1])]
    for cx, cy in corners:
        ip.scatter([cx], [cy], s=110, facecolors="none", edgecolors=RED, linewidths=2.2, zorder=4)
    ip.plot(0, 0, "+", color=INK, ms=8)
    ip.set_aspect("equal"); ip.set_xticks([]); ip.set_yticks([])
    ip.set_title("BGA plan view: strain ∝ DNP;\ncorner balls (red) fail first", fontsize=7.5)
    # table
    it = fig.add_axes([0.64, 0.03, 0.35, 0.40]); it.axis("off")
    it.set_xlim(0, 1); it.set_ylim(0, 1)
    it.text(0, 0.98, "Worked examples (Section 22.9)", fontsize=7.5, fontweight="bold", va="top")
    txt = ("Flip-chip Si die, no underfill\n"
           "  Δα 14.4 ppm/K, ΔT 100 K,\n  L$_D$ 5 mm, h 75 µm\n  γ ≈ 0.096\n\n"
           "2512 resistor on FR-4\n"
           "  Δα 9.2 ppm/K, ΔT 165 K,\n  L$_D$ 3.2 mm, h ≈ 100 µm\n  γ ≈ 0.049")
    it.text(0, 0.86, txt, fontsize=7.2, va="top")
    save(fig, "51", "fig-51-5-dnp-shear-strain")


# ---------------------------------------------------------------- Figure 51.6
def psat_iapws(TC):
    """Saturation pressure of water (MPa), IAPWS-IF97 region 4."""
    n = [0.11670521452767e4, -0.72421316703206e6, -0.17073846940092e2, 0.12020824702470e5,
         -0.32325550322333e7, 0.14915108613530e2, -0.48232657361591e4, 0.40511340542057e6,
         -0.23855557567849, 0.65017534844798e3]
    T = np.asarray(TC) + 273.15
    th = T + n[8] / (T - n[9])
    A = th**2 + n[0] * th + n[1]
    B = n[2] * th**2 + n[3] * th + n[4]
    C = n[5] * th**2 + n[6] * th + n[7]
    return (2 * C / (-B + np.sqrt(B**2 - 4 * A * C))) ** 4


def _pkg(ax, stage):
    ax.set_xlim(0, 10); ax.set_ylim(-0.5, 6.5); ax.set_aspect("equal"); ax.axis("off")
    emc_c = "#5A5A5A" if stage < 2 else "#7A6A5A"
    body = Rectangle((1.0, 1.0), 8.0, 3.6, fc=emc_c, ec=INK, lw=0.8)
    ax.add_patch(body)
    # leads
    for sx in (-1, 1):
        xe = 1.0 if sx < 0 else 9.0
        ax.plot([xe, xe + sx * 0.6, xe + sx * 0.6, xe + sx * 0.9], [2.6, 2.6, 0.4, 0.4], color="#B0B0B0", lw=2.2)
    pad_y = 2.4
    dome = 0.0
    if stage >= 2:
        dome = 0.45 if stage == 2 else 0.7
    # die pad
    ax.add_patch(Rectangle((2.6, pad_y), 4.8, 0.25, fc="#B0B0B0", ec=INK, lw=0.5, zorder=3))
    ax.add_patch(Rectangle((3.4, pad_y + 0.25), 3.2, 0.5, fc=SI, ec=INK, lw=0.5, zorder=3))
    # wires
    t = np.linspace(0, 1, 30)
    for sx in (-1, 1):
        x0 = 5.0 + sx * 1.4
        x1 = 5.0 + sx * 3.9
        ax.plot(x0 + (x1 - x0) * t, pad_y + 0.75 + 0.7 * np.sin(np.pi * t) - (pad_y + 0.75 - 2.6) * t,
                color="#E0C068", lw=1.0, zorder=3)
    if stage == 3:
        # break the right-hand wire at the pad end
        ax.plot([8.75], [2.6], marker="x", color=RED, ms=7, mew=2, zorder=6)
    if stage >= 1:
        # delamination gap under the pad
        w = 1.8 if stage == 1 else 4.8
        x0 = 2.6 if stage == 1 else 2.6
        xs = np.linspace(x0, x0 + w, 40)
        if stage == 1:
            ys = pad_y - 0.22 * np.sin(np.pi * (xs - x0) / w)
            ax.fill_between(xs, ys, pad_y, color="white", zorder=2)
        else:
            ys = pad_y - dome * np.sin(np.pi * (xs - x0) / w)
            ax.fill_between(xs, ys, pad_y, color="#CFE8F5", zorder=2)
            ax.text(5.0, pad_y - dome / 2 - 0.05, "steam", fontsize=6.5, ha="center", va="center", zorder=5)
    if stage == 3:
        ax.plot([2.6, 2.1, 1.9, 1.6], [pad_y - 0.3, 1.8, 1.4, 1.0], color="white", lw=1.4, zorder=5)
        ax.plot([7.4, 7.9, 8.2, 8.3], [pad_y - 0.3, 1.9, 1.3, 1.0], color="white", lw=1.4, zorder=5)
    if stage >= 2:
        # bulging package bottom
        xs = np.linspace(1.0, 9.0, 60)
        ax.fill_between(xs, 1.0 - 0.25 * np.sin(np.pi * (xs - 1) / 8), 1.0, color=emc_c, zorder=1)
    rng = np.random.default_rng(5)
    if stage == 0:
        for _ in range(60):
            side = rng.integers(4)
            d = abs(rng.normal(0, 0.45))
            if side == 0:
                p = (rng.uniform(1, 9), 4.6 - d)
            elif side == 1:
                p = (rng.uniform(1, 9), 1.0 + d)
            elif side == 2:
                p = (1.0 + d, rng.uniform(1, 4.6))
            else:
                p = (9.0 - d, rng.uniform(1, 4.6))
            ax.add_patch(Circle(p, 0.09, fc="#56B4E9", ec="none", zorder=4))
    if stage == 1:
        for _ in range(14):
            ax.add_patch(Circle((rng.uniform(2.7, 7.3), pad_y - rng.uniform(0.05, 0.3)), 0.08, fc="#56B4E9",
                                ec="none", zorder=4))
        for _ in range(25):
            ax.add_patch(Circle((rng.uniform(1.2, 8.8), rng.uniform(1.1, 4.5)), 0.07, fc="#56B4E9",
                                ec="none", zorder=4, alpha=0.7))


def popcorn():
    fig = plt.figure(figsize=(6.8, 4.6))
    titles = ["(1) Storage: moisture\nabsorbed from all surfaces",
              "(2) Reflow heating to 260 °C:\nwater at pad/EMC interface,\ndelamination at pad edge",
              "(3) Vapour pressure up to\n4.7 MPa inflates a dome;\nEMC above T$_g$ is soft",
              "(4) Crack runs from pad\ncorner to package bottom;\nwire bond broken"]
    notes = ["D ≈ 10$^{-12}$ m$^2$/s,\nsaturation in days", "delamination starts\nat the pad edge",
             "", ""]
    for k in range(4):
        a = fig.add_axes([0.005 + k * 0.25, 0.47, 0.24, 0.40])
        _pkg(a, k)
        a.set_title(titles[k], fontsize=7.5)
        if notes[k]:
            a.text(5, -0.4, notes[k], fontsize=7, ha="center", va="top", color="#1F6FA0")
    # inset plot: saturated vapour pressure
    p = fig.add_axes([0.12, 0.08, 0.5, 0.30])
    T = np.linspace(100, 260, 200)
    P = psat_iapws(T)
    p.axhspan(0.32, 0.65, color=COLORS[1], alpha=0.15, lw=0)
    p.annotate("pressure that bends the EMC under a 5 mm pad\n(0.5 mm thick) to its strength above T$_g$ (10–20 MPa)",
               xy=(130, 0.5), xytext=(103, 3.9), fontsize=7, va="center", color="#8A3A00",
               arrowprops=dict(arrowstyle="-|>", lw=0.6, color="#8A3A00", mutation_scale=7))
    p.plot(T, P, color=COLORS[0])
    for Tm in (220, 260):
        Pm = float(psat_iapws(Tm))
        p.plot(Tm, Pm, "o", color=COLORS[0], ms=4)
        p.text(Tm - 3, Pm + 0.15, f"{Pm:.1f} MPa at {Tm} °C", fontsize=7.5, ha="right")
        print(Tm, Pm)
    p.set_xlim(100, 260); p.set_ylim(0, 5)
    p.set_xlabel("Temperature (°C)")
    p.set_ylabel("p$_{sat}$ H$_2$O (MPa)")
    fig.text(0.66, 0.30, "Saturated water vapour pressure\nroughly doubles between SnPb\n(220 °C) and lead-free (260 °C)\n"
                         "peak reflow, pushing packages\nup one or two MSL levels.", fontsize=7.5, va="center")
    save(fig, "51", "fig-51-6-popcorn-cracking")


if __name__ == "__main__":
    solder_imc()
    flip_chip()
    power_module()
    fr4_z()
    dnp()
    popcorn()
