"""Figures for Chapter 29 — Magnetic Materials for EEE.

Run from the repository root:  python figures/scripts/ch29.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon, Rectangle, FancyArrowPatch
from scipy.spatial import cKDTree

MU0 = 4e-7 * np.pi


# ---------------------------------------------------------------- Figure 29.1
def hc_js_map():
    fig, ax = new_fig(6.8, 4.6)
    ax.axvspan(3, 4, color="0.85", alpha=0.6, lw=0)          # 1-10 kA/m (log10 units)
    ax.text(3.5, 2.42, "semi-hard", ha="center", va="top", fontsize=8.5, color="0.35", rotation=0)
    # (name, Hc range A/m, Js range T, colour index, label offset in (log10, T))
    # (name, Hc range A/m, Js range T, colour index, label position (log10 Hc, T), ha)
    soft = [
        ("Co-based\namorphous", (0.3, 1), (0.55, 0.8), 3, (-0.75, 0.47), "center"),
        ("nanocrystalline", (0.5, 1.5), (1.18, 1.3), 2, (-0.05, 1.39), "center"),
        ("80Ni permalloy", (0.5, 2), (0.7, 0.8), 0, (0.05, 0.93), "center"),
        ("Fe-based\namorphous", (2, 4), (1.5, 1.6), 1, (0.15, 1.55), "right"),
        ("GO SiFe", (5, 10), (1.98, 2.06), 4, (0.55, 2.02), "right"),
        ("NO SiFe", (30, 80), (1.6, 2.05), 5, (1.7, 1.83), "center"),
        ("pure Fe", (20, 80), (2.1, 2.2), 7, (2.05, 2.15), "left"),
        ("FeCo", (30, 160), (2.3, 2.4), 3, (2.35, 2.35), "left"),
        ("MnZn ferrite", (5, 20), (0.45, 0.53), 2, (1.0, 0.62), "center"),
        ("NiZn ferrite", (20, 300), (0.25, 0.40), 0, (2.65, 0.32), "left"),
        ("powder\ncores", (100, 500), (0.75, 1.5), 1, (2.35, 1.12), "center"),
    ]
    hard = [
        ("AlNiCo", (4.5e4, 1.4e5), (0.7, 1.3), 4, (4.9, 1.0), "center"),
        ("hard\nferrite", (2.0e5, 4.0e5), (0.36, 0.46), 3, (5.45, 0.2), "center"),
        ("SmCo", (8e5, 2.0e6), (0.85, 1.15), 0, (6.1, 1.0), "center"),
        ("NdFeB", (8.8e5, 3.0e6), (1.2, 1.45), 1, (6.2, 1.62), "center"),
    ]
    for group in (soft, hard):
        for name, (h0, h1), (j0, j1), ci, (lx, ly), ha in group:
            x0, x1 = np.log10(h0), np.log10(h1)
            xc, yc = (x0 + x1) / 2, (j0 + j1) / 2
            w = max(x1 - x0, 0.25) * 1.15
            h = max(j1 - j0, 0.06) * 1.25
            ax.add_patch(Ellipse((xc, yc), w, h, fc=COLORS[ci], ec=COLORS[ci], alpha=0.35, lw=1.0))
            ax.add_patch(Ellipse((xc, yc), w, h, fc="none", ec=COLORS[ci], lw=1.0))
            ax.text(lx, ly, name, ha=ha, va="center", fontsize=7.5, color=INK)
    ax.text(-0.9, 2.42, "SOFT", fontsize=12, weight="bold", color="0.3", va="top")
    ax.text(5.6, 2.42, "HARD", fontsize=12, weight="bold", color="0.3", va="top")
    ax.annotate("", xy=(2.6, 0.15), xytext=(-0.8, 0.15),
                arrowprops=dict(arrowstyle="-|>", color="0.35", lw=1.0, mutation_scale=10))
    ax.text(0.9, 0.06, "higher resistivity → higher frequency (ferrites, amorphous, powder)",
            fontsize=7.5, color="0.3", ha="center", va="center")
    ax.set_xlim(-1, 7)
    ax.set_ylim(0, 2.5)
    ax.set_xticks(range(-1, 8))
    ax.set_xticklabels([r"$10^{%d}$" % k for k in range(-1, 8)])
    ax.set_xlabel(r"coercivity $H_c$ (soft) or $H_{cJ}$ (magnets)  (A/m, log scale)")
    ax.set_ylabel(r"$J_s$ (soft) or $B_r$ (magnets)  (T)")
    save(fig, "29", "fig-29-1-hc-js-map")


# ---------------------------------------------------------------- Figure 29.2
def lamination_eddy_currents():
    fig = plt.figure(figsize=(6.8, 3.4))
    # --- left: 3-D sheet sketch (oblique projection: x thickness, y width, z flux direction)
    ax = fig.add_axes([0.0, 0.05, 0.36, 0.9])
    ax.set_aspect("equal")
    ax.axis("off")
    ox, oy = 0.55, 0.38   # oblique axis for z (into page, along flux)
    d, Wd, Lz = 0.7, 3.0, 2.6

    def P(x, y, z):
        return (x + z * ox, y + z * oy)

    front = [P(0, 0, 0), P(d, 0, 0), P(d, Wd, 0), P(0, Wd, 0)]
    top = [P(0, Wd, 0), P(d, Wd, 0), P(d, Wd, Lz), P(0, Wd, Lz)]
    side = [P(d, 0, 0), P(d, 0, Lz), P(d, Wd, Lz), P(d, Wd, 0)]
    ax.add_patch(Polygon(side, fc="#C9D6E3", ec=INK, lw=1.0))
    ax.add_patch(Polygon(top, fc="#E4ECF4", ec=INK, lw=1.0))
    ax.add_patch(Polygon(front, fc="#F3F6FA", ec=INK, lw=1.0))
    # eddy loops on the front (x-y) face: nested rectangles, current +y on one side, -y on the other
    for k, s in enumerate((0.1, 0.22)):
        xs0, xs1 = s, d - s
        ys0, ys1 = 0.2 + s, Wd - 0.2 - s
        ax.plot([xs0, xs1, xs1, xs0, xs0], [ys0, ys0, ys1, ys1, ys0], color=COLORS[1], lw=1.0)
        ax.annotate("", xy=(xs0, Wd / 2 + 0.25), xytext=(xs0, Wd / 2 - 0.25),
                    arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.0, mutation_scale=8))
        ax.annotate("", xy=(xs1, Wd / 2 - 0.25), xytext=(xs1, Wd / 2 + 0.25),
                    arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.0, mutation_scale=8))
    # flux arrow along z
    bx0, by0 = P(d + 0.15, 0.45, 0.3)
    bx1, by1 = P(d + 0.15, 0.45, Lz - 0.2)
    ax.add_patch(FancyArrowPatch(P(d / 2, Wd + 0.0, 0.3), P(d / 2, Wd + 0.0, Lz - 0.2), arrowstyle="-|>",
                                 mutation_scale=12, lw=1.8, color=COLORS[0]))
    tx, ty = P(d / 2, Wd + 0.15, Lz / 2)
    ax.text(tx - 0.05, ty + 0.12, r"$B(t)$", color=COLORS[0], fontsize=9, ha="right")
    ax.annotate("", xy=(d, -0.25), xytext=(0, -0.25),
                arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=0.8, mutation_scale=7))
    ax.text(d / 2, -0.32, r"$d$", ha="center", va="top", fontsize=9)
    # axes triad
    cx, cy = -0.9, 0.0
    for (dx, dy, lab) in ((0.5, 0, "x"), (0, 0.5, "y"), (0.5 * ox, 0.5 * oy, "z")):
        ax.annotate("", xy=(cx + dx, cy + dy), xytext=(cx, cy),
                    arrowprops=dict(arrowstyle="-|>", color="0.3", lw=0.8, mutation_scale=7))
        ax.text(cx + dx * 1.25, cy + dy * 1.25, f"${lab}$", fontsize=8, ha="center", va="center")
    ax.text(0.05, Wd - 0.15, "eddy\nloops", fontsize=7.5, color=COLORS[1], ha="right", va="top",
            transform=ax.transData)
    ax.set_xlim(-1.3, d + Lz * ox + 0.3)
    ax.set_ylim(-0.75, Wd + Lz * oy + 0.3)
    ax.set_title("(a) one lamination", fontsize=9.5)

    # --- middle: J_y(x) profile
    bx = fig.add_axes([0.42, 0.22, 0.22, 0.6])
    x = np.linspace(-0.5, 0.5, 10)
    bx.plot(x, x, color=COLORS[1])
    bx.fill_between(x, 0, x, color=COLORS[1], alpha=0.15)
    bx.axhline(0, color=INK, lw=0.6)
    bx.axvline(0, color=INK, lw=0.6, ls=":")
    bx.set_xticks([-0.5, 0, 0.5])
    bx.set_xticklabels([r"$-d/2$", "0", r"$+d/2$"])
    bx.set_yticks([])
    bx.set_xlabel(r"$x$")
    bx.set_ylabel(r"$J_y$")
    bx.text(-0.48, 0.42, r"$J_y=\sigma x\,\dfrac{dB}{dt}$", fontsize=9)
    bx.set_title("(b) current density", fontsize=9.5)

    # --- right: solid vs laminated
    cx_ = fig.add_axes([0.68, 0.05, 0.32, 0.9])
    cx_.set_aspect("equal")
    cx_.axis("off")
    cx_.set_xlim(0, 5.2)
    cx_.set_ylim(-0.9, 3.6)
    # solid block
    cx_.add_patch(Rectangle((0.1, 0.2), 2.0, 2.6, fc="#E4ECF4", ec=INK, lw=1.0))
    cx_.add_patch(Rectangle((0.35, 0.45), 1.5, 2.1, fc="none", ec=COLORS[1], lw=1.4))
    cx_.annotate("", xy=(0.35, 1.7), xytext=(0.35, 1.3),
                 arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.2, mutation_scale=9))
    cx_.annotate("", xy=(1.85, 1.3), xytext=(1.85, 1.7),
                 arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.2, mutation_scale=9))
    cx_.text(1.1, 3.0, "solid core", ha="center", fontsize=8.5)
    # laminated stack
    n = 6
    x0 = 2.9
    t = 2.0 / n
    for i in range(n):
        xl = x0 + i * t
        cx_.add_patch(Rectangle((xl, 0.2), t * 0.82, 2.6, fc="#E4ECF4", ec=INK, lw=0.8))
        cx_.add_patch(Rectangle((xl + t * 0.82, 0.2), t * 0.18, 2.6, fc="#F2C14E", ec="none"))
        cx_.add_patch(Rectangle((xl + 0.06, 0.4), t * 0.82 - 0.12, 2.2, fc="none", ec=COLORS[1], lw=0.8))
    cx_.text(x0 + 1.0, 3.0, "laminated stack", ha="center", fontsize=8.5)
    cx_.annotate("insulating\ncoating", xy=(x0 + 3 * t - 0.02, 0.25), xytext=(x0 + 1.0, -0.15),
                 fontsize=7.5, ha="center", va="top",
                 arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
    cx_.text(1.1, -0.45, r"$P_{cl}\propto d^2$", ha="center", va="center", fontsize=10, weight="bold")
    cx_.text(2.55, 1.5, "⊙ $B$", ha="center", va="center", fontsize=9, color=COLORS[0])
    cx_.set_title("(c) solid vs laminated", fontsize=9.5, y=0.9)
    save(fig, "29", "fig-29-2-lamination-eddy-currents")


# ---------------------------------------------------------------- Figure 29.3
def loss_separation():
    fig, ax = new_fig(6.4, 3.8)
    Wh = 0.030
    Ccl = 0.0062 / 50
    Cex = 0.012 / np.sqrt(50)
    f = np.linspace(0, 500, 400)
    ex = Cex * np.sqrt(f)
    cl = Ccl * f
    ax.fill_between(f, 0, Wh, color=COLORS[0], alpha=0.55, lw=0, label=r"hysteresis $W_h$ (constant)")
    ax.fill_between(f, Wh, Wh + ex, color=COLORS[2], alpha=0.55, lw=0, label=r"excess $C_{ex}f^{1/2}$")
    ax.fill_between(f, Wh + ex, Wh + ex + cl, color=COLORS[1], alpha=0.55, lw=0, label=r"classical eddy $C_{cl}f$")
    ax.plot(f, Wh + ex + cl, color=INK, lw=1.4, label="total $P/f$")
    for fm in (50, 400):
        tot = Wh + Cex * np.sqrt(fm) + Ccl * fm
        ax.plot([fm, fm], [0, tot], color=INK, lw=0.7, ls=":")
        ax.plot([fm], [tot], "o", color=INK, ms=4)
        lab = {50: "0.048", 400: "0.113"}[fm]
        if fm == 50:
            ax.text(fm + 6, tot + 0.002, f"{lab} J/kg\nat {fm} Hz", fontsize=8, va="bottom")
        else:
            ax.text(fm - 8, tot - 0.006, f"{lab} J/kg\nat {fm} Hz", fontsize=8, va="top", ha="right")
    ax.text(390, 0.015, "0.030", fontsize=8, ha="right", va="center", color="white", weight="bold")
    ax.text(395, Wh + Cex * np.sqrt(400) / 2, "0.034", fontsize=8, ha="right", va="center", color=INK)
    ax.text(395, Wh + Cex * np.sqrt(400) + Ccl * 400 / 2, "0.049", fontsize=8, ha="right", va="center", color=INK)
    ax.text(10, 0.115, "0.35 mm NO steel, 1.5 T (illustrative)", fontsize=8.5, color="0.3", va="top")
    ax.set_xlim(0, 500)
    ax.set_ylim(0, 0.12)
    ax.set_xlabel(r"frequency $f$ (Hz)")
    ax.set_ylabel(r"energy per cycle $P/f$ (J/kg)")
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 0.92), fontsize=8.5)
    save(fig, "29", "fig-29-3-loss-separation")


# ---------------------------------------------------------------- Figure 29.4
def _voronoi_image(seeds, nx, ny, xmax, ymax):
    xs = np.linspace(0, xmax, nx)
    ys = np.linspace(0, ymax, ny)
    X, Y = np.meshgrid(xs, ys)
    _, lab = cKDTree(seeds).query(np.c_[X.ravel(), Y.ravel()])
    lab = lab.reshape(ny, nx)
    edge = np.zeros_like(lab, bool)
    edge[:, 1:] |= lab[:, 1:] != lab[:, :-1]
    edge[1:, :] |= lab[1:, :] != lab[:-1, :]
    edge[:, :-1] |= edge[:, 1:]
    edge[:-1, :] |= edge[1:, :]
    return X, Y, lab, edge


def goss_texture():
    fig = plt.figure(figsize=(6.8, 3.6))
    # ---- left: sheet + bcc cube in Goss orientation
    ax = fig.add_axes([0.0, 0.02, 0.38, 0.92])
    ax.set_aspect("equal")
    ax.axis("off")
    # sample frame: RD = (1,0,0), TD = (0,1,0), ND = (0,0,1); oblique projection
    def P(v):
        rd, td, nd = v
        return np.array([rd + 0.5 * td, 0.32 * td + nd])

    Ls, Ws, T = 4.2, 3.2, 0.35
    c = [np.array(p) for p in [(0, 0, 0), (Ls, 0, 0), (Ls, Ws, 0), (0, Ws, 0)]]
    up = [p + np.array([0, 0, T]) for p in c]
    ax.add_patch(Polygon([P(p) for p in (c[0], c[1], up[1], up[0])], fc="#D5DEE8", ec=INK, lw=0.9))
    ax.add_patch(Polygon([P(p) for p in (c[1], c[2], up[2], up[1])], fc="#C2CFDC", ec=INK, lw=0.9))
    ax.add_patch(Polygon([P(p) for p in up], fc="#EEF3F8", ec=INK, lw=0.9, alpha=0.9))
    # cube axes in sample frame for Goss {110}<001>
    s = 1 / np.sqrt(2)
    e100 = np.array([0, s, s])
    e010 = np.array([0, -s, s])
    e001 = np.array([1, 0, 0])
    a = 1.15
    origin = np.array([1.2, 2.2, T + 0.0])
    verts = {}
    for i in (0, 1):
        for j in (0, 1):
            for k in (0, 1):
                verts[(i, j, k)] = origin + a * (i * e100 + j * e010 + k * e001)
    # shift so the cube sits with its lowest edge on the sheet surface
    edges = []
    for key, v in verts.items():
        for dim in range(3):
            if key[dim] == 0:
                k2 = list(key); k2[dim] = 1
                edges.append((v, verts[tuple(k2)]))
    for v0, v1 in edges:
        p0, p1 = P(v0), P(v1)
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=COLORS[0], lw=1.3)
    for v in verts.values():
        p = P(v)
        ax.plot(*p, "o", color=COLORS[0], ms=4)
    ctr = origin + a * (e100 + e010 + e001) / 2
    ax.plot(*P(ctr), "o", color=COLORS[1], ms=5)
    # (110) plane of the cube (contains [001] and [1-10]) is parallel to the sheet: shade it
    plane = [origin, origin + a * e001, origin + a * (e001 + e100 + e010), origin + a * (e100 + e010)]
    # that plane contains [001] and [110]; the plane parallel to sheet contains [001] and [1-10]
    plane = [origin + a * e100, origin + a * (e100 + e001), origin + a * (e010 + e001), origin + a * e010]
    ax.add_patch(Polygon([P(p) for p in plane], fc=COLORS[4], ec="none", alpha=0.35))
    # direction arrows on the sheet surface
    base = np.array([0.3, 0.5, T])
    def sarrow(vec, color, label, off=(0, 0)):
        p0, p1 = P(base), P(base + vec)
        ax.add_patch(FancyArrowPatch(tuple(p0), tuple(p1), arrowstyle="-|>", mutation_scale=10, lw=1.4,
                                     color=color, shrinkA=0, shrinkB=0))
        ax.text(p1[0] + off[0], p1[1] + off[1], label, color=color, fontsize=8, ha="center", va="center")
    sarrow(np.array([1.6, 0, 0]), INK, "RD", (0.3, -0.12))
    sarrow(np.array([0, 1.2, 0]), INK, "TD", (0.1, 0.18))
    sarrow(np.array([0, 0, 0.9]), INK, "ND", (0, 0.15))
    hard = np.array([1, np.sqrt(2), 0]) / np.sqrt(3) * 2.9
    p0, p1 = P(np.array([0.5, 0.25, T])), P(np.array([0.5, 0.25, T]) + hard)
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=COLORS[1], lw=1.2, ls="--")
    ax.text(p1[0] + 0.1, p1[1] - 0.05, "⟨111⟩ hard,\n55° to RD", color=COLORS[1], fontsize=7.5,
            ha="left", va="top")
    pe1 = P(origin + a * (e100 + e010 + e001))
    ax.text(pe1[0] + 0.15, pe1[1], "[001] easy axis ∥ RD", fontsize=7.5, color=COLORS[0], ha="left", va="center")
    pp = P(origin + a * e010)
    ax.text(pp[0] - 0.05, pp[1] + 0.3, "(110) ∥ sheet", fontsize=7.5, color="#9A6A00", ha="right", va="bottom")
    ax.set_xlim(-0.2, 6.3)
    ax.set_ylim(-0.5, 3.6)
    ax.set_title("(a) Goss texture {110}⟨001⟩", fontsize=9.5)

    # ---- middle: GO sheet plan view, grains 5-30 mm, stripe domains, laser scribes
    rng = np.random.default_rng(7)
    bx = fig.add_axes([0.40, 0.12, 0.29, 0.74])
    Xm, Ym = 60.0, 40.0
    seeds = np.c_[rng.uniform(0, Xm, 9), rng.uniform(0, Ym, 9)]
    X, Y, lab, edge = _voronoi_image(seeds, 600, 400, Xm, Ym)
    tilt = np.radians(rng.uniform(-4, 4, len(seeds)))
    wdom = rng.uniform(1.4, 2.2, len(seeds))
    stripe = np.sin((np.sin(tilt[lab]) * X + np.cos(tilt[lab]) * Y) * np.pi / wdom[lab]) > 0
    img = np.where(stripe, 0.78, 0.92)
    img[edge] = 0.15
    bx.imshow(img, cmap="gray", vmin=0, vmax=1, origin="lower", extent=(0, Xm, 0, Ym), interpolation="nearest")
    for xl in np.arange(5, Xm, 5):
        bx.plot([xl, xl], [0, Ym], color=COLORS[1], lw=0.8, ls="--")
    bx.plot([3, 23], [2.5, 2.5], color=INK, lw=2.5, solid_capstyle="butt")
    bx.text(13, 3.5, "20 mm", ha="center", va="bottom", fontsize=8, color=INK,
            bbox=dict(fc="white", ec="none", pad=0.5, alpha=0.8))
    bx.set_xticks([]); bx.set_yticks([])
    for sp in bx.spines.values():
        sp.set_visible(True)
    bx.annotate("", xy=(Xm, -3), xytext=(Xm - 11, -3), annotation_clip=False,
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.0, mutation_scale=9))
    bx.text(Xm - 12, -3, "RD", ha="right", va="center", fontsize=8)
    bx.text(0, -3, "- - laser scribes, ~5 mm", ha="left", va="center", fontsize=7.5, color=COLORS[1])
    bx.set_title("(b) GO steel: grains 5–30 mm,\nstripe domains along RD", fontsize=9)

    # ---- right: NO sheet, equiaxed grains ~100-150 um with random easy axes
    cx = fig.add_axes([0.715, 0.12, 0.28, 0.74])
    Xn, Yn = 900.0, 600.0
    # quasi-uniform seeds (jittered grid) give equiaxed ~120 um grains
    gx, gy = np.meshgrid(np.arange(60, Xn, 125), np.arange(60, Yn, 125))
    seeds = np.c_[gx.ravel(), gy.ravel()] + rng.normal(0, 30, (gx.size, 2))
    X, Y, lab, edge = _voronoi_image(seeds, 450, 300, Xn, Yn)
    shade = rng.uniform(0.82, 0.95, len(seeds))
    img = shade[lab]
    img[edge] = 0.15
    cx.imshow(img, cmap="gray", vmin=0, vmax=1, origin="lower", extent=(0, Xn, 0, Yn), interpolation="nearest")
    ang = rng.uniform(0, 2 * np.pi, len(seeds))
    for (sx, sy), th in zip(seeds, ang):
        if 30 < sx < Xn - 30 and 30 < sy < Yn - 30:
            cx.annotate("", xy=(sx + 35 * np.cos(th), sy + 35 * np.sin(th)),
                        xytext=(sx - 35 * np.cos(th), sy - 35 * np.sin(th)),
                        arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.0, mutation_scale=7))
    cx.plot([40, 240], [-40, -40], color=INK, lw=2.5, solid_capstyle="butt", clip_on=False)
    cx.text(140, -60, "200 µm", ha="center", va="top", fontsize=8)
    cx.set_xticks([]); cx.set_yticks([])
    for sp in cx.spines.values():
        sp.set_visible(True)
    cx.set_xlim(0, Xn); cx.set_ylim(0, Yn)
    cx.set_title("(c) NO steel: grains 100–150 µm,\nrandom easy axes", fontsize=9)
    save(fig, "29", "fig-29-4-goss-texture")


# ---------------------------------------------------------------- Figure 29.5
def ferrite_permeability_spectra():
    fig, ax = new_fig(6.4, 4.0)
    f = np.logspace(4, 9, 600)
    K = 1.87e10       # gamma / 3 pi, Hz/T
    mats = [("MnZn, $\\mu_i$ = 10 000", 10000, 0.5, COLORS[0]),
            ("MnZn, $\\mu_i$ = 2000", 2000, 0.5, COLORS[2]),
            ("NiZn, $\\mu_i$ = 100", 100, 0.35, COLORS[1])]
    for name, mui, Js, col in mats:
        fr = K * Js / (mui - 1)
        u = f / fr
        mu1 = 1 + (mui - 1) / (1 + u**2)
        mu2 = (mui - 1) * u / (1 + u**2)
        ax.loglog(f, mu1, color=col, label=name + rf", $f_r$ = {fr/1e6:.2g} MHz")
        ax.loglog(f, mu2, color=col, ls="--")
        ax.plot([fr], [mui], "o", mfc="white", mec=col, ms=5)
    fs = np.logspace(5.3, 9, 50)
    ax.loglog(fs, 1 + K * 0.5 / fs, color="0.4", ls=":", lw=1.4)
    ax.text(1.2e7, 4e3, "Snoek limit\n" + r"$(\mu_i-1)f_r\approx9.3$ GHz" + "\n(0.5 T)",
            fontsize=8, color="0.3", ha="left", va="bottom")
    # EMI-bead region for NiZn: mu'' > mu' above f_r
    frN = K * 0.35 / 99
    ax.axvspan(frN * 1.02, 1e9, ymin=0, ymax=1, color=COLORS[1], alpha=0.08, lw=0)
    ax.text(2.6e8, 250, "EMI-bead\nregion:\nNiZn $\\mu''>\\mu'$", fontsize=8, color=COLORS[1], ha="center")
    ax.plot([], [], color="0.3", label=r"$\mu'$ (solid)")
    ax.plot([], [], color="0.3", ls="--", label=r"$\mu''$ (dashed)")
    ax.set_xlim(1e4, 1e9)
    ax.set_ylim(1, 2e4)
    ax.set_xlabel("frequency $f$ (Hz)")
    ax.set_ylabel(r"$\mu'$, $\mu''$")
    ax.legend(loc="lower left", fontsize=7.8)
    save(fig, "29", "fig-29-5-ferrite-permeability-spectra")


# ---------------------------------------------------------------- Figure 29.6
def _magnet(H, Br, mur, HcJ, w):
    """Intrinsic J(H) (T) with linear recoil and a sigmoid knee at -HcJ (H in A/m)."""
    J = (Br + MU0 * (mur - 1) * H) / (1 + np.exp(-(H + HcJ) / w))
    return J, J + MU0 * H


def demagnetization_curves():
    fig, ax = new_fig(6.8, 4.6)
    H = np.linspace(-2.0e6, 0, 4000)
    k = 1e3
    for BH in (100e3, 200e3, 300e3):
        Hh = np.linspace(-2.0e6, -20e3, 400)
        ax.plot(Hh / k, BH / -Hh, color="0.75", lw=0.9)
        ax.text(-1990, BH / 1.99e6 + 0.012, f"$BH$ = {BH/1e3:.0f} kJ/m³", fontsize=7.5, color="0.45", ha="left", va="bottom")
    mats = [
        ("NdFeB N42, 20 °C", 1.30, 1.05, 1.10e6, 12e3, COLORS[0]),
        ("NdFeB N42, 150 °C", 1.097, 1.05, 2.15e5, 6e3, COLORS[3]),
        ("Sm$_2$Co$_{17}$", 1.10, 1.03, 1.60e6, 20e3, COLORS[2]),
        ("hard ferrite", 0.40, 1.10, 2.85e5, 8e3, COLORS[4]),
    ]
    for name, Br, mur, HcJ, w, col in mats:
        J, B = _magnet(H, Br, mur, HcJ, w)
        m = B >= 0
        ax.plot(H[m] / k, B[m], color=col, label=name)
        ax.plot(H / k, J, color=col, ls="--", lw=1.2)
    # AlNiCo 5: strongly curved normal curve, Hc ~ 50 kA/m
    Hc_a, Br_a = 50e3, 1.27
    h = np.linspace(0, 1, 300)
    Ba = Br_a * (1 - h**8)
    Ha = -h * Hc_a
    ax.plot(Ha / k, Ba, color=COLORS[1], label="AlNiCo 5")
    ax.plot(Ha / k, Ba - MU0 * Ha, color=COLORS[1], ls="--", lw=1.2)
    # load line, permeance coefficient 5
    Hl = np.linspace(-1.5 / (5 * MU0), 0, 10)
    ax.plot(Hl / k, -5 * MU0 * Hl, color=INK, lw=1.0, label=r"load line $B/\mu_0H=-5$")
    # operating points
    for Br, col, lab in ((1.30, COLORS[0], "20 °C"), (1.097, COLORS[3], "150 °C")):
        Bm = Br / (1 + 1.05 / 5)
        Hm = -Bm / (5 * MU0)
        ax.plot([Hm / k], [Bm], "o", color=col, ms=5, zorder=5)
    ax.annotate("operating points: 1.07 T, −171 kA/m (20 °C);\n0.91 T, −144 kA/m (150 °C)", xy=(-178, 1.09), xytext=(-1480, 1.40), va="center",
                fontsize=7.5, arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
    ax.annotate("knee at 150 °C\n" + r"($H_{cJ}\approx210$ kA/m)", xy=(-200, 0.80), xytext=(-620, 1.15),
                fontsize=7.5, color=COLORS[3], arrowprops=dict(arrowstyle="-|>", color=COLORS[3], lw=0.8,
                                                              mutation_scale=8))
    ax.plot([], [], color="0.3", label="normal $B$–$H$ (solid)")
    ax.plot([], [], color="0.3", ls="--", label="intrinsic $J$–$H$ (dashed)")
    ax.set_xlim(-2000, 0)
    ax.set_ylim(0, 1.5)
    ax.set_xlabel(r"$H$ (kA/m)")
    ax.set_ylabel(r"$B$, $J$ (T)")
    ax.spines["right"].set_visible(True)
    ax.spines["left"].set_visible(False)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), fontsize=7.8, ncol=3)
    save(fig, "29", "fig-29-6-demagnetization-curves")


if __name__ == "__main__":
    hc_js_map()
    lamination_eddy_currents()
    loss_separation()
    goss_texture()
    ferrite_permeability_spectra()
    demagnetization_curves()
