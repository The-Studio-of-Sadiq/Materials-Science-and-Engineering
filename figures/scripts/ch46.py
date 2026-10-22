"""Figures for Chapter 46 — Casting, Forming and Powder Processing.

Run from the repository root:  python figures/scripts/ch46.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle, Ellipse, FancyBboxPatch
from scipy.interpolate import PchipInterpolator
from scipy.spatial import Voronoi

from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK

BLUE, ORANGE, GREEN, PINK, YELLOW, SKY = COLORS[:6]


# ---------------------------------------------------------------- helpers
def _schem(w, h, xlim, ylim):
    """schematic() with the axes filling the whole figure."""
    fig, ax = schematic(w, h, xlim=xlim, ylim=ylim)
    fig.subplots_adjust(left=0.005, right=0.995, bottom=0.005, top=0.995)
    return fig, ax


def _voronoi_grains(ax, n, rng, xlim=(0, 1), ylim=(0, 1), flatten=1.0, lw=0.7, color=INK):
    """Draw a Voronoi grain structure filling the box; flatten < 1 squashes grains vertically
    (pancaked grains): cells are built equiaxed in a y-stretched space and mapped back."""
    m = int(n / flatten)
    pts = np.column_stack([rng.uniform(-0.2, 1.2, m), rng.uniform(-0.2, 1.2 / flatten, m)])
    vor = Voronoi(pts)
    x0, x1 = xlim
    y0, y1 = ylim
    for (i, j) in vor.ridge_vertices:
        if i < 0 or j < 0:
            continue
        p, q = vor.vertices[i], vor.vertices[j]
        X = np.array([p[0], q[0]])
        Y = np.array([p[1], q[1]]) * flatten
        ax.plot(x0 + X * (x1 - x0), y0 + Y * (y1 - y0), color=color, lw=lw, solid_capstyle="round")
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)


def _micro_axes(fig, rect, title=None):
    ax = fig.add_axes(rect)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(True)
        s.set_color(INK)
        s.set_linewidth(0.9)
    ax.set_facecolor("#F7F3EA")
    if title:
        ax.set_title(title, fontsize=8.5, pad=3)
    return ax


# ---------------------------------------------------------------- 38.1
def fig_process_routes():
    fig, ax = _schem(6.8, 4.6, xlim=(0, 17.4), ylim=(0.0, 11.6))
    box(ax, 0.06, 3.9, 1.5, 3.6, "Liquid\nmetal", fc="#F6D7C3", fontsize=9.5)

    lanes = [
        ("Casting", 9.3, "#FBE7DA",
         ["mould\nfilling", "solidifi-\ncation", "shake-out,\nfettling", "HIP\n(optional)", "machining"],
         "dendritic, segregated;  shrinkage, gas pores, segregation"),
        ("Deformation", 5.5, "#E3EEF8",
         ["ingot / CC\nslab, billet", "homogenize\nor reheat", "hot rolling,\nforging,\nextrusion", "cold work", "anneal or\nheat treat"],
         "wrought, recrystallized, textured;  laps, edge cracks"),
        ("Powder", 1.7, "#E2F2EA",
         ["atomization", "compaction\nor MIM\nmoulding", "sintering\nor HIP", "sizing,\nfinishing"],
         "fine grains;  porosity 0–15 %"),
    ]
    bw, bh, gap, x0 = 2.2, 1.75, 0.24, 1.95
    ends = {}
    for name, y, fc, steps, note in lanes:
        ax.text(x0, y + bh + 0.22, name, fontsize=10, fontweight="bold", color=INK, va="bottom")
        # feed arrow from liquid metal
        ax.annotate("", xy=(x0, y + bh / 2), xytext=(1.56, 5.7),
                    arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.0, mutation_scale=10,
                                    connectionstyle="arc3,rad=0", shrinkA=0, shrinkB=0))
        for k, s in enumerate(steps):
            x = x0 + k * (bw + gap)
            box(ax, x, y, bw, bh, s, fc=fc, fontsize=7.9)
            if k:
                arrow(ax, x - gap, y + bh / 2, x, y + bh / 2)
        ax.text(x0 + (bw / 2 + 0.2 if name == "Powder" else 0.05), y - 0.18, note, fontsize=8.3, style="italic", color="#444444", va="top")
        ends[name] = (x0 + len(steps) * (bw + gap) - gap, y + bh / 2)

    # destination boxes
    jx = 14.25
    box(ax, jx, 3.9, 2.9, 3.6, "Ch 39\njoining", fc="#EFE6F3", fontsize=9.5)
    box(ax, jx, 8.75, 2.9, 2.4, "Ch 40\nadditive\nmanufacturing", fc="#FFF4D6", fontsize=8.6)
    # casting -> AM and joining
    xc, yc = ends["Casting"]
    arrow(ax, xc, yc + 0.3, jx, 10.3, color=ORANGE)
    arrow(ax, xc, yc - 0.35, jx, 7.2, color=PINK)
    # deformation -> joining
    xd, yd = ends["Deformation"]
    arrow(ax, xd, yd, jx, yd, color=PINK)
    # powder -> joining, and powder feedstock from atomization to AM
    xp, yp = ends["Powder"]
    arrow(ax, xp, yp, jx, 4.2, color=PINK)
    xa = x0 + bw / 2
    ax.plot([xa, xa, 17.32, 17.32], [1.7, 0.35, 0.35, 8.0], color=ORANGE, lw=1.1)
    arrow(ax, 17.32, 8.0, 16.95, 8.75, color=ORANGE)
    ax.text(16.85, 0.45, "powder feedstock", fontsize=8, color=ORANGE, ha="right", va="bottom")
    save(fig, "46", "fig-46-1-process-routes")


# ---------------------------------------------------------------- 38.2
def fig_feeding_and_defects():
    fig = plt.figure(figsize=(6.8, 5.0))
    ax = fig.add_axes([0.02, 0.36, 0.96, 0.62])
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-95, 425)
    ax.set_ylim(-50, 168)

    sand = "#EADFC8"
    ax.add_patch(Rectangle((-95, -50), 520, 218, fc=sand, ec="none", zorder=0))
    ax.text(150, 150, "sand mould", fontsize=8.5, color="#7A6A4A", va="top", ha="center")

    # plate 250 x 50 and riser D = H = 110 at right
    metal = "#F4C9A6"
    ax.add_patch(Rectangle((0, 0), 250, 50, fc=metal, ec=INK, lw=1.2, zorder=2))
    ax.add_patch(Rectangle((250, 0), 110, 110, fc=metal, ec=INK, lw=1.2, zorder=2))
    ax.plot([250, 250], [0.6, 49.4], color=metal, lw=2.2, zorder=3)  # open connection
    # chill block at the far left end
    ax.add_patch(Rectangle((-16, -4), 16, 58, fc="#9AA3AD", ec=INK, lw=1.0, zorder=3))
    ax.text(-8, 60, "chill", ha="center", fontsize=8.5)
    # tapered sprue, runner and gate (left)
    ax.add_patch(Polygon([[-78, 140], [-52, 140], [-60, -22], [-70, -22]], fc=metal, ec=INK, lw=1.0, zorder=2))
    ax.add_patch(Polygon([[-84, 140], [-46, 140], [-52, 152], [-78, 152]], fc=metal, ec=INK, lw=1.0, zorder=2))
    ax.add_patch(Rectangle((-70, -32), 110, 10, fc=metal, ec=INK, lw=1.0, zorder=2))
    ax.add_patch(Rectangle((30, -22), 10, 22.5, fc=metal, ec=INK, lw=1.0, zorder=2))
    ax.plot([30.6, 39.4], [0, 0], color=metal, lw=2.2, zorder=3)
    ax.text(-45, 100, "sprue\n(tapered)", ha="left", fontsize=8.3, va="center")
    ax.text(-20, -44, "runner", ha="center", fontsize=8.3)
    ax.text(45, -15, "gate", ha="left", fontsize=8.3)

    # isochrones: smooth freezing-time field over plate + riser (Chvorinov-like, t ~ d_eff^2)
    x = np.linspace(0, 360, 721)
    y = np.linspace(0, 110, 221)
    X, Y = np.meshgrid(x, y)
    inside = (Y <= 50) | (X >= 250)
    walls = [Y, np.where(X < 250, np.abs(50 - Y), np.hypot(X - 250, 50 - Y)), np.where(X >= 250, 110 - Y, 1e3), 360 - X, (X + 3) / 1.8,
             np.where(Y > 50, (np.maximum(X - 250, 0) + 1e-3) / np.clip((Y - 50) / 30, 1e-3, 1), 1e3)]
    inv = sum(1.0 / np.maximum(w, 0.5) ** 2 for w in walls)
    d_eff = 1 / np.sqrt(inv)
    g = np.where(X < 250, 0.80 + 0.20 * (X / 250) ** 2, 1.0)
    T = 13.0 * (d_eff / 20.0) ** 2 * g
    T = np.where(inside, T, np.nan)
    cs = ax.contour(X, Y, T, levels=[2, 4, 6, 8], colors=BLUE, linestyles="--", linewidths=1.0, zorder=4)
    # label each isochrone where it crosses the plate mid-plane
    for lev in [2, 4, 6, 8]:
        row = T[np.argmin(np.abs(y - 25))]
        ix = np.where(np.isfinite(row) & (row >= lev))[0]
        if len(ix):
            xl = x[ix[0]]
            ax.text(xl, 25, f"{lev}", fontsize=7.5, color=BLUE, ha="center", va="center", zorder=6,
                    bbox=dict(boxstyle="round,pad=0.1", fc=metal, ec="none"))
    ax.text(366, 18, "dashed:\nisochrones\n(min)", fontsize=7.8, color=BLUE, zorder=6, va="center")
    # shrinkage pipe in the riser top
    ax.add_patch(Polygon([[283, 110], [327, 110], [310, 80], [305, 58], [300, 80]], fc="white", ec=INK, lw=0.9, zorder=5))
    ax.annotate("shrinkage\npipe", xy=(312, 90), xytext=(372, 80), fontsize=8.5, ha="left", va="center",
                arrowprops=dict(arrowstyle="-", color=INK, lw=0.7))
    ax.annotate("", xy=(240, 60), xytext=(130, 60),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.6, mutation_scale=12))
    ax.text(185, 64, "directional solidification", fontsize=8.3, color=ORANGE, ha="center")
    # labels
    ax.text(215, -14, "plate 250 × 50 mm,  $M_c$ = 17.9 mm,  $t_f$ ≈ 8 min", ha="center", fontsize=8.8, va="top")
    ax.text(305, 116, "riser $D=H$ = 110 mm\n$M_r$ = 22 mm,  $t_f$ ≈ 12 min", ha="center", fontsize=8.5,
            va="bottom")
    # inset markers on the section
    marks = {"b": (190, 44), "d": (35, -9)}
    for k, (mx, my) in marks.items():
        ax.add_patch(Circle((mx, my), 7, fc="white", ec=INK, lw=0.8, zorder=6))
        ax.text(mx, my, k, ha="center", va="center", fontsize=8, zorder=7)

    # ---- insets (standalone mini-sketches)
    rng = np.random.default_rng(3)
    w, h, y0 = 0.225, 0.29, 0.03
    titles = ["(a) microshrinkage at an\nunfed T-junction hot spot", "(b) round gas pores\nnear the top surface",
              "(c) hot tear at a corner\nrestrained by a core", "(d) oxide bifilm\nentrained at the gate"]
    axs = []
    for i in range(4):
        a = fig.add_axes([0.02 + i * 0.245, y0, w, h])
        a.set_xlim(0, 10)
        a.set_ylim(0, 10)
        a.set_aspect("equal")
        a.set_xticks([])
        a.set_yticks([])
        for s in a.spines.values():
            s.set_color(INK)
            s.set_linewidth(0.8)
        a.set_facecolor(sand)
        a.text(5, -0.6, titles[i], ha="center", va="top", fontsize=8)
        axs.append(a)
    # (a) T-junction with jagged interdendritic cavities
    a = axs[0]
    a.add_patch(Polygon([[0, 3], [10, 3], [10, 6.3], [6.3, 6.3], [6.3, 10], [3.7, 10], [3.7, 6.3], [0, 6.3]],
                        fc=metal, ec=INK, lw=1.0))
    for _ in range(14):
        cx, cy = rng.normal(5, 0.55), rng.normal(5.2, 0.45)
        ang = rng.uniform(0, 2 * np.pi, 7)
        ang.sort()
        r = rng.uniform(0.12, 0.42, 7)
        a.add_patch(Polygon(np.column_stack([cx + r * np.cos(ang), cy + r * np.sin(ang)]), fc="#333333", ec="none"))
    a.add_patch(Circle((5, 5.2), 1.9, fc="none", ec=ORANGE, ls="--", lw=0.8))
    a.text(8.3, 8.6, "hot\nspot", fontsize=7.5, ha="center", color=ORANGE)
    # (b) round pores under the top skin
    a = axs[1]
    a.add_patch(Rectangle((0, 0), 10, 7.5, fc=metal, ec="none"))
    a.plot([0, 10], [7.5, 7.5], color=INK, lw=1.0)
    for _ in range(11):
        r = rng.uniform(0.18, 0.55)
        a.add_patch(Circle((rng.uniform(0.8, 9.2), rng.uniform(5.0, 6.8)), r, fc="white", ec=INK, lw=0.7))
    a.text(5, 8.6, "top surface", ha="center", fontsize=7.5)
    a.text(5, 2.4, "smooth, round\n(H rejected on freezing)", ha="center", fontsize=7.3, color="#555555")
    # (c) branched hot tear at a corner restrained by a core
    a = axs[2]
    a.add_patch(Polygon([[0, 0], [10, 0], [10, 10], [5, 10], [5, 4.5], [0, 4.5]], fc=metal, ec=INK, lw=1.0))
    a.add_patch(Rectangle((0, 4.5), 5, 5.5, fc="#D9CBB0", ec=INK, lw=0.8, hatch="...."))
    a.text(2.5, 7.4, "core", ha="center", fontsize=7.8, bbox=dict(fc="white", ec="none", pad=1))
    xs = [5.0, 5.6, 6.0, 6.7, 7.0, 7.8]
    ys = [4.5, 3.9, 3.0, 2.6, 1.7, 1.2]
    a.plot(xs, ys, color="#222222", lw=1.5)
    a.plot([6.0, 6.7, 6.9], [3.0, 3.5, 4.3], color="#222222", lw=1.0)
    a.plot([7.0, 6.5, 6.6], [1.7, 1.1, 0.6], color="#222222", lw=1.0)
    a.annotate("", xy=(5.4, 6.0), xytext=(9.6, 6.0), arrowprops=dict(arrowstyle="<|-|>", color=ORANGE, lw=1.3, mutation_scale=10))
    a.text(7.6, 7.0, "contraction\nhindered", fontsize=7.3, ha="center", color=ORANGE)
    # (d) folded oxide film near the gate
    a = axs[3]
    a.add_patch(Rectangle((0, 0), 10, 10, fc=metal, ec="none"))
    t = np.linspace(0, 1, 60)
    xx = 1.2 + 7.5 * t
    yy = 5 + 1.6 * np.sin(2 * np.pi * t * 1.3) * (1 - t * 0.4)
    a.plot(xx, yy, color="#3A3A3A", lw=1.2)
    a.plot(xx, yy - 0.35, color="#3A3A3A", lw=1.2)
    a.fill_between(xx, yy - 0.35, yy, color="#BBBBBB")
    a.text(5, 1.6, "doubled oxide skin\n= ready-made crack", ha="center", fontsize=7.3, color="#555555")
    a.annotate("", xy=(3.0, 9.6), xytext=(3.0, 7.8), arrowprops=dict(arrowstyle="<|-", color=INK, lw=0.9))
    a.text(3.4, 9.0, "turbulent jet", fontsize=7.3)
    save(fig, "46", "fig-46-2-feeding-and-defects")


# ---------------------------------------------------------------- 38.3
def _flc(e2, flc0, a_left, c_right, delta=0.03):
    s = np.sqrt(e2 ** 2 + delta ** 2) - delta
    left = flc0 + a_left * s
    right = flc0 + c_right * (1 - np.exp(-s / 0.15))
    return np.where(e2 < 0, left, right)


def fig_forming_limit_diagram():
    fig, ax = new_fig(6.4, 4.6)
    e2 = np.linspace(-0.40, 0.40, 400)
    dc = _flc(e2, 0.32, 0.847, 0.208)
    # zones
    ax.fill_between(e2, 0, np.clip(dc - 0.10, 0, None), color="#DDEFD9", zorder=0)
    ax.fill_between(e2, dc - 0.10, dc, color="#FFF0C4", zorder=0)
    ax.fill_between(e2, dc, 0.75, color="#F8D9D2", zorder=0)
    ax.text(-0.37, 0.22, "safe", fontsize=9.5, color="#2E7031")
    ax.text(0.405, 0.40, "marginal\n(10 % margin)", fontsize=8.5, color="#8A6A00", ha="left", va="center")
    ax.text(-0.17, 0.66, "failure (necking / split)", fontsize=9.5, color="#9A3324")

    # strain paths
    ax.plot([0, -0.30], [0, 0.60], ls="--", color="#555555", lw=1.0)
    ax.plot([0, 0], [0, 0.70], ls="--", color="#555555", lw=1.0)
    ax.plot([0, 0.35], [0, 0.35], ls="--", color="#555555", lw=1.0)
    ax.text(-0.235, 0.45, "uniaxial\n($\\varepsilon_2=-\\varepsilon_1/2$)", fontsize=8.3, rotation=0, ha="right")
    ax.text(0.012, 0.44, "plane strain", fontsize=8.3, ha="left", rotation=90)
    ax.text(0.24, 0.19, "equibiaxial", fontsize=8.3, rotation=34, ha="left")

    ax.plot(e2, dc, color=BLUE, lw=2.2)
    m = (e2 > -0.30) & (e2 < 0.36)
    al = _flc(e2, 0.21, 0.75, 0.16)
    dp = _flc(e2, 0.18, 0.70, 0.12)
    ax.plot(e2[m], al[m], color=ORANGE, lw=1.9)
    ax.plot(e2[m], dp[m], color=GREEN, lw=1.9)
    ax.text(-0.395, 0.655, "DC04, 1.0 mm\n$\\mathrm{FLC_0}$ = 0.32", fontsize=8.5, color=BLUE, va="top")
    ax.text(0.37, 0.27, "Al 6016-T4\n$\\mathrm{FLC_0}$ ≈ 0.21", fontsize=8.5, color=ORANGE, va="bottom")
    ax.text(0.37, 0.155, "DP600\n$\\mathrm{FLC_0}$ ≈ 0.18", fontsize=8.5, color=GREEN, va="top")

    # grid measurements from a stamped panel (DC04)
    rng = np.random.default_rng(7)
    pts = []
    for beta, n, lo, hi in [(-0.45, 14, 0.04, 0.32), (-0.2, 12, 0.04, 0.30), (0.0, 10, 0.05, 0.20),
                            (0.3, 10, 0.03, 0.22), (0.8, 8, 0.03, 0.15)]:
        e1 = rng.uniform(lo, hi, n)
        pts.append(np.column_stack([beta * e1 + rng.normal(0, 0.008, n), e1]))
    pts = np.vstack(pts)
    marg = np.column_stack([rng.normal(0.0, 0.02, 4), [0.25, 0.27, 0.285, 0.30]])
    ax.scatter(pts[:, 0], pts[:, 1], s=10, color=INK, zorder=5, label="grid measurements (stamped panel)")
    ax.scatter(marg[:, 0], marg[:, 1], s=22, facecolor=YELLOW, edgecolor=INK, lw=0.8, zorder=6,
               label="near plane strain, in marginal zone")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2, fontsize=8, handletextpad=0.3)

    ax.set_xlim(-0.40, 0.40)
    ax.set_ylim(0, 0.70)
    ax.set_xlabel("minor true strain $\\varepsilon_2$")
    ax.set_ylabel("major true strain $\\varepsilon_1$")

    # inset: circle grid -> ellipses
    ins = fig.add_axes([0.64, 0.71, 0.27, 0.17])
    ins.set_aspect("equal")
    ins.axis("off")
    ins.set_xlim(0, 11)
    ins.set_ylim(-0.6, 4.6)
    for i in range(2):
        for j in range(2):
            ins.add_patch(Circle((0.9 + 1.6 * i, 0.9 + 1.6 * j), 0.7, fc="none", ec=INK, lw=0.9))
            ins.add_patch(Ellipse((6.9 + 1.5 * i, 0.7 + 2.0 * j), 1.15, 1.8, fc="none", ec=INK, lw=0.9))
    ins.annotate("", xy=(5.9, 1.7), xytext=(4.2, 1.7), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.0))
    ins.text(5.05, 2.0, "stamp", fontsize=7.5, ha="center")
    ins.text(1.7, -0.5, "printed circles", fontsize=7.5, ha="center", va="top")
    ins.text(7.6, -0.5, "ellipses → $\\varepsilon_1, \\varepsilon_2$", fontsize=7.5, ha="center", va="top")
    save(fig, "46", "fig-46-3-forming-limit-diagram")


# ---------------------------------------------------------------- 38.4
def fig_tmcp_schedule():
    fig = plt.figure(figsize=(6.8, 5.0))
    ax = fig.add_axes([0.10, 0.415, 0.86, 0.565])
    # temperature-time trace
    t = [0, 0.6, 3.0]
    T = [400, 1200, 1200]
    # roughing passes 1150 -> 1000 (stepwise; small chill at each pass)
    tr = 3.4
    temps = [1150, 1110, 1075, 1040, 1000]
    t.append(tr); T.append(1160)
    for k, Tk in enumerate(temps):
        ta = tr + 0.5 * k
        t += [ta, ta + 0.06, ta + 0.44]
        T += [Tk, Tk - 25, Tk - 30 if k < len(temps) - 1 else Tk - 20]
    # hold (delay) to below T_nr
    t += [8.6]
    T += [935]
    # finishing passes 930 -> 800
    tf0 = 8.7
    ftemps = [930, 900, 870, 840, 810]
    for k, Tk in enumerate(ftemps):
        ta = tf0 + 0.35 * k
        t += [ta, ta + 0.05, ta + 0.30]
        T += [Tk, Tk - 18, Tk - 22]
    t += [10.6, 10.6 + 300 / 20 / 60]   # 800 -> 500 at 20 K/s (15 s)
    T += [800, 500]
    tt = np.linspace(10.85, 15, 30)
    t += list(tt)
    T += list(500 - 110 * (1 - np.exp(-(tt - 10.85) / 3.0)))
    ax.plot(t, T, color=INK, lw=1.8, zorder=4)

    for y, lab in [(1150, "Nb(C,N) solution ≈ 1150 °C"), (950, "$T_{nr}$ ≈ 950 °C"),
                   (780, "$A_{r3}$ ≈ 780 °C"), (680, "$A_{r1}$ ≈ 680 °C")]:
        ax.axhline(y, ls="--", color="#888888", lw=0.9, zorder=1)
        ax.text(15.0, y + 8, lab, fontsize=8.3, ha="right", va="bottom", color="#555555")
    ax.axvspan(3.3, 5.9, color="#FBE3D3", zorder=0)
    ax.axvspan(8.6, 10.5, color="#DDEBF7", zorder=0)
    ax.text(4.6, 540, "roughing:\nrecrystallizing passes", ha="center", fontsize=8.3, va="bottom")
    ax.text(9.55, 1000, "finishing:\npancaking\n(below $T_{nr}$)", ha="center", fontsize=8.3, va="bottom")
    ax.text(1.5, 1215, "reheat 1200 °C", ha="center", fontsize=8.3, va="bottom")
    ax.text(7.25, 1000, "hold\n(delay)", ha="center", fontsize=8.3)
    ax.annotate("accelerated cooling\n≈ 20 K/s, 800 → 500 °C", xy=(10.75, 600), xytext=(13.1, 575),
                fontsize=8.3, ha="center", va="center", arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.0))
    ax.text(13.6, 462, "air cool", fontsize=8.3, ha="center", va="bottom")
    ax.set_xlim(0, 15)
    ax.set_ylim(400, 1320)
    ax.set_xlabel("time (min, schematic)")
    ax.set_ylabel("temperature (°C)")
    # stage markers
    marks = [(1.8, 1200, "1"), (5.95, 990, "2"), (10.45, 790, "3"), (11.7, 472, "4")]
    for mx, my, s in marks:
        ax.add_patch(Ellipse((mx, my), 0.42, 45, fc="white", ec=INK, lw=0.9, zorder=6))
        ax.text(mx, my, s, ha="center", va="center", fontsize=8, zorder=7)

    # micro-sketch insets
    rng = np.random.default_rng(11)
    titles = ["1  coarse equiaxed\naustenite (reheat)", "2  recrystallized\naustenite ≈ 40 µm",
              "3  pancaked austenite,\ndeformation bands", "4  ferrite 3–5 µm\n+ some bainite"]
    for i in range(4):
        a = _micro_axes(fig, [0.10 + i * 0.222, 0.065, 0.19, 0.16])
        a.text(0.5, 1.04, titles[i], transform=a.transAxes, ha="center", va="bottom", fontsize=8)
        if i == 0:
            _voronoi_grains(a, 22, rng)
        elif i == 1:
            _voronoi_grains(a, 90, rng)
        elif i == 2:
            _voronoi_grains(a, 14, rng, flatten=0.28, lw=0.6)
            for k in range(14):
                x0 = rng.uniform(-0.1, 1.0)
                y0 = rng.uniform(0.05, 0.95)
                a.plot([x0, x0 + 0.12], [y0, y0 + 0.05], color="#7A5C3A", lw=0.6)
            a.set_xlim(0, 1)
            a.set_ylim(0, 1)
        else:
            a.set_facecolor("#FAFAF5")
            _voronoi_grains(a, 420, rng, lw=0.45)
            for k in range(6):
                c = rng.uniform(0.1, 0.9, 2)
                a.add_patch(Ellipse(c, 0.11, 0.06, angle=rng.uniform(0, 180), fc="#555555", ec="none"))
    fig.text(0.53, 0.015, "normalized C–Mn steel for comparison: ferrite 15–25 µm", fontsize=8.3,
             ha="center", style="italic", color="#555555")
    save(fig, "46", "fig-46-4-tmcp-schedule")


# ---------------------------------------------------------------- 38.5
def fig_compaction_curve():
    rho_s = 7.87
    # smooth compaction law fitted to 6.4 / 7.0 / 7.2 g/cm3 at 400 / 600 / 800 MPa,
    # apparent density 3.0 g/cm3 at P = 0:  D = Dm - (Dm - D0) exp[-(P/P0)^m]
    D0, Dm, P0, m = 3.0 / rho_s, 0.9691, 277.8, 0.8446

    def f(P):
        return rho_s * (Dm - (Dm - D0) * np.exp(-(np.asarray(P) / P0) ** m))
    P = np.linspace(0, 1000, 400)
    fe = f(P)
    femo = fe - (0.15 + 0.05 * P / 1000)

    fig = plt.figure(figsize=(6.8, 4.2))
    ax = fig.add_axes([0.09, 0.12, 0.56, 0.80])
    ax.plot(P, fe, color=BLUE, lw=2.0, label="water-atomized iron")
    ax.plot(P, femo, color=ORANGE, lw=2.0, label="pre-alloyed Fe–Mo")
    ax.scatter([400, 600, 800], f([400, 600, 800]), color=BLUE, zorder=5, s=22)
    ax.axhline(rho_s, ls="--", color="#666666", lw=1.0)
    ax.text(990, rho_s + 0.03, "pore-free iron 7.87 g/cm³", ha="right", va="bottom", fontsize=8.5, color="#555555")
    ax.axvspan(400, 800, color="#EEF3F8", zorder=0)
    ax.text(600, 7.62, "typical pressing\n400–800 MPa", ha="center", va="center", fontsize=8, color="#555555")
    kw = dict(fontsize=8.3, arrowprops=dict(arrowstyle="-", color="#555555", lw=0.7))
    ax.annotate("rearrangement", xy=(105, f(105)), xytext=(150, 4.65), va="center", **kw)
    ax.annotate("plastic deformation\nof contacts", xy=(260, f(260)), xytext=(330, 5.35), ha="center", va="center", **kw)
    ax.annotate("work hardening", xy=(900, f(900)), xytext=(880, 6.9), ha="center", va="center", **kw)
    ax.set_xlim(0, 1000)
    ax.set_ylim(4.5, 8.1)
    ax.set_xlabel("compaction pressure (MPa)")
    ax.set_ylabel("green density (g/cm³)")
    ax.legend(loc="upper left", fontsize=8.5, bbox_to_anchor=(0.0, 0.93))
    ax.set_title("(a)", loc="left", fontsize=10)
    r = ax.secondary_yaxis("right", functions=(lambda d: 100 * d / rho_s, lambda p: p * rho_s / 100))
    r.set_ylabel("relative density (%)")

    # (b) Heckel inset
    ib = fig.add_axes([0.44, 0.22, 0.18, 0.24])
    Pi = np.linspace(100, 1000, 100)
    D = f(Pi) / rho_s
    H = np.log(1 / (1 - D))
    ib.plot(Pi, H, color=BLUE, lw=1.6)
    sel = (Pi >= 200) & (Pi <= 800)
    k, b = np.polyfit(Pi[sel], H[sel], 1)
    ib.plot([200, 800], [k * 200 + b, k * 800 + b], ls="--", color=INK, lw=1.0)
    ib.set_xlabel("P (MPa)", fontsize=8, labelpad=1)
    ib.set_ylabel("ln[1/(1−D)]", fontsize=8, labelpad=1)
    ib.tick_params(labelsize=7.5)
    ib.set_xticks([200, 600, 1000])
    ib.set_title("(b) Heckel plot", fontsize=8.5, pad=2)
    ib.text(980, k * 350 + b, "linear fit\n200–800 MPa", fontsize=7.3, ha="right", va="top")
    ib.patch.set_alpha(0.95)

    # (c) density contours in a single-action pressed cylinder
    ic = fig.add_axes([0.75, 0.12, 0.23, 0.74])
    ic.set_aspect("equal")
    ic.axis("off")
    ic.set_title("(c) single-action\npressing", fontsize=9, pad=2)
    R, Hc = 1.0, 2.0
    r_ = np.linspace(-R, R, 200)
    z_ = np.linspace(0, Hc, 300)
    RR, ZZ = np.meshgrid(r_, z_)
    zeta = 1 - ZZ / Hc  # distance from upper punch
    rho = 7.15 - 0.55 * zeta ** 1.2 * (0.55 + 0.65 * (RR / R) ** 2) + 0.12 * (RR / R) ** 2 * (1 - zeta) ** 3
    ic.add_patch(Rectangle((-R, 0), 2 * R, Hc, fc="#F2F2F2", ec=INK, lw=1.0))
    cf = ic.contourf(RR, ZZ, rho, levels=np.arange(6.5, 7.35, 0.1), cmap="Blues", alpha=0.85)
    cs = ic.contour(RR, ZZ, rho, levels=[6.7, 6.9, 7.1], colors=INK, linewidths=0.7)
    ic.clabel(cs, fmt="%.1f", fontsize=7.3, inline=True)
    # die and punches
    ic.add_patch(Rectangle((-R - 0.25, -0.05), 0.25, Hc + 0.45, fc="#9AA3AD", ec=INK, lw=0.8))
    ic.add_patch(Rectangle((R, -0.05), 0.25, Hc + 0.45, fc="#9AA3AD", ec=INK, lw=0.8))
    ic.add_patch(Rectangle((-R, Hc), 2 * R, 0.30, fc="#C4CBD3", ec=INK, lw=0.8))
    ic.add_patch(Rectangle((-R, -0.30), 2 * R, 0.30, fc="#C4CBD3", ec=INK, lw=0.8))
    ic.annotate("", xy=(0, Hc + 0.32), xytext=(0, Hc + 0.85), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.3))
    ic.text(0.08, Hc + 0.62, "moving punch", fontsize=7.8, ha="left")
    ic.text(0, -0.42, "fixed lower punch", fontsize=7.8, ha="center", va="top")
    ic.text(0.0, -0.78, "contours: green density, g/cm³\ndensest under the punch,\nleast dense at bottom corner",
            fontsize=7.5, ha="center", va="top", color="#444444")
    ic.set_xlim(-1.45, 1.45)
    ic.set_ylim(-1.55, 3.0)
    save(fig, "46", "fig-46-5-compaction-curve")


# ---------------------------------------------------------------- 38.6
def fig_pm_routes():
    fig, ax = _schem(6.8, 5.2, xlim=(0, 17.4), ylim=(-0.9, 13.0))
    rng = np.random.default_rng(5)
    # top row: powder types
    ptypes = [("water-atomized\nirregular, 20–200 µm", "irr"), ("gas-atomized\nspherical, 10–150 µm", "sph"),
              ("reduced sponge\nporous, irregular", "sponge"), ("carbonyl\nspheres, 1–10 µm", "fine")]
    for i, (lab, kind) in enumerate(ptypes):
        cx = 2.2 + i * 4.35
        cy = 12.15
        if kind == "sph":
            for k in range(6):
                ax.add_patch(Circle((cx - 0.95 + k * 0.38, cy + rng.uniform(-0.3, 0.3)),
                                    rng.uniform(0.15, 0.32), fc="#C9D3DE", ec=INK, lw=0.7))
        elif kind == "fine":
            for k in range(30):
                ax.add_patch(Circle((cx - 1.0 + rng.uniform(0, 2.0), cy + rng.uniform(-0.45, 0.45)),
                                    0.07, fc="#C9D3DE", ec=INK, lw=0.5))
        else:
            for k in range(5):
                n = 9
                ang = np.sort(rng.uniform(0, 2 * np.pi, n))
                rr = rng.uniform(0.16, 0.38, n)
                c0 = (cx - 0.9 + k * 0.45, cy + rng.uniform(-0.3, 0.3))
                ax.add_patch(Polygon(np.column_stack([c0[0] + rr * np.cos(ang), c0[1] + rr * np.sin(ang)]),
                                     fc="#C9D3DE", ec=INK, lw=0.7))
                if kind == "sponge":
                    for _ in range(3):
                        ax.add_patch(Circle((c0[0] + rng.uniform(-0.1, 0.1), c0[1] + rng.uniform(-0.1, 0.1)),
                                            0.045, fc="white", ec="none"))
        ax.text(cx, 11.45, lab, ha="center", va="top", fontsize=7.8)

    cols = [
        ("Press-and-sinter", 0.1, "#E3EEF8", [
            "mix with graphite,\nCu and lubricant",
            "die compaction\n400–800 MPa\n(green 86–92 %)",
            "sinter 1120–1300 °C\n(86–92 %)",
            "sizing, hardening\nor oil impregnation"]),
        ("MIM", 4.1, "#FBE7DA", [
            "compound with binder\n(60 vol% powder)",
            "injection mould\n(cavity ≈ 18 %\noversize)",
            "debind\n(\"brown\" part)",
            "sinter ≈ 1350 °C\n(95–99 %; ≈ 15 %\nlinear shrinkage)"]),
        ("Powder HIP", 8.1, "#E2F2EA", [
            "fill and evacuate\nsteel can (≈ 65 %)",
            "HIP 100–200 MPa,\n0.7–0.9 $T_m$ (100 %;\n≈ 13 % linear\nshrinkage)",
            "remove can,\nmachine"]),
    ]
    bw, bh, gy, ytop = 3.75, 1.75, 0.32, 9.45
    for title, x, fc, steps in cols:
        ax.text(x + bw / 2, ytop + 0.2, title, ha="center", va="bottom", fontsize=9, fontweight="bold")
        for k, s in enumerate(steps):
            yb = ytop - (k + 1) * bh - k * gy
            box(ax, x, yb, bw, bh, s, fc=fc, fontsize=7.8)
            if k:
                arrow(ax, x + bw / 2, yb + bh + gy, x + bw / 2, yb + bh)
    # side panel: liquid-phase sintering of WC-Co
    sx, sy, sw, sh = 12.1, 1.17, 5.25, 8.95
    ax.add_patch(FancyBboxPatch((sx, sy), sw, sh, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc="#FAF6EE", ec=INK, lw=0.9))
    ax.text(sx + sw / 2, sy + sh - 0.2, "Liquid-phase sintering\nof WC–Co, 1350–1500 °C", ha="center",
            va="top", fontsize=8.5, fontweight="bold")
    rr = np.random.default_rng(2)
    cy = sy + 5.0
    for dx, packed in [(sx + 1.3, False), (sx + 3.95, True)]:
        ax.add_patch(Rectangle((dx - 1.05, cy - 1.15), 2.1, 2.3, fc="#E9E1F2" if packed else "white",
                               ec=INK, lw=0.7))
        for k in range(9):
            sc = 0.80 if packed else 1.0
            px = dx + (-0.64 + (k % 3) * 0.64) * sc
            py = cy + (-0.72 + (k // 3) * 0.72) * sc
            ang = np.linspace(0, 2 * np.pi, 7)[:-1] + rr.uniform(0, 1)
            rad = 0.25 if not packed else 0.29
            ax.add_patch(Polygon(np.column_stack([px + rad * np.cos(ang), py + rad * np.sin(ang)]),
                                 fc="#7B8794", ec=INK, lw=0.5))
            if not packed and k % 2 == 0:
                ax.add_patch(Circle((px + 0.31, py + 0.31), 0.09, fc="#B07CC6", ec="none"))
        ax.text(dx, cy - 1.3, "dense WC grains\nin Co binder" if packed else "WC + Co powder\n(green)", ha="center",
                va="top", fontsize=7.6)
    arrow(ax, sx + 2.42, cy, sx + 2.83, cy)
    ax.text(sx + sw / 2, sy + 0.3, "Co-rich liquid wets WC: capillary\nrearrangement, solution–\nreprecipitation;"
            " 17–20 % linear\nshrinkage, full density", ha="center", va="bottom", fontsize=7.6)

    # density scale bar 60-100 %
    bx0, bx1, by = 1.6, 16.6, -0.05
    xs = np.linspace(bx0, bx1, 200)
    for i in range(len(xs) - 1):
        frac = i / (len(xs) - 1)
        ax.add_patch(Rectangle((xs[i], by), xs[1] - xs[0] + 0.01, 0.3, fc=plt.cm.Greys(0.10 + 0.55 * frac),
                               ec="none"))
    ax.add_patch(Rectangle((bx0, by), bx1 - bx0, 0.3, fc="none", ec=INK, lw=0.8))

    def dx_(p):
        return bx0 + (p - 60) / 40 * (bx1 - bx0)
    for p in range(60, 101, 10):
        ax.plot([dx_(p)] * 2, [by - 0.12, by], color=INK, lw=0.8)
        ax.text(dx_(p), by - 0.18, f"{p} %", ha="center", va="top", fontsize=7.8)
    ax.text(bx0 - 0.15, by + 0.15, "relative\ndensity", ha="right", va="center", fontsize=7.8)
    yb = by + 0.48
    ax.plot([dx_(86), dx_(92)], [yb, yb], color=BLUE, lw=4, solid_capstyle="butt")
    ax.text(dx_(89), yb + 0.15, "press-and-sinter", ha="center", va="bottom", fontsize=7.8, color=BLUE)
    ax.plot([dx_(95), dx_(99)], [yb, yb], color=ORANGE, lw=4, solid_capstyle="butt")
    ax.text(dx_(96.6), yb + 0.15, "MIM", ha="center", va="bottom", fontsize=7.8, color=ORANGE)
    ax.plot([dx_(100)], [yb], marker="v", color=GREEN, ms=7)
    ax.text(dx_(100), yb + 0.2, "HIP", ha="center", va="bottom", fontsize=7.8, color=GREEN)
    ax.plot([dx_(65)], [yb], marker="v", color=GREEN, ms=7, mfc="white")
    ax.text(dx_(65) + 0.15, yb + 0.12, "HIP can fill", ha="left", va="bottom", fontsize=7.8, color=GREEN)
    ax.plot([dx_(60)], [yb], marker="v", color=ORANGE, ms=7, mfc="white")
    ax.text(dx_(60) - 0.15, yb + 0.12, "MIM feedstock", ha="right", va="bottom", fontsize=7.8, color=ORANGE)
    save(fig, "46", "fig-46-6-pm-routes")


if __name__ == "__main__":
    fig_process_routes()
    fig_feeding_and_defects()
    fig_forming_limit_diagram()
    fig_tmcp_schedule()
    fig_compaction_curve()
    fig_pm_routes()
