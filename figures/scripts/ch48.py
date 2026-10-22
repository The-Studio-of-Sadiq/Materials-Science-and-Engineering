"""Figures for Chapter 48 — Additive Manufacturing.

Run from the repository root:  python figures/scripts/ch48.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle, Ellipse, FancyArrowPatch
from matplotlib.colors import ListedColormap

from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK

BLUE, ORANGE, GREEN, PINK, YELLOW, SKY = COLORS[:6]
POWDER = "#D9D2C3"
METAL = "#9AA5B1"


def _panel(fig, rect, xlim=(0, 10), ylim=(0, 12)):
    ax = fig.add_axes(rect)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    return ax


def _powder(ax, x0, x1, y0, y1, rng, r=0.09, fc=POWDER):
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fc=fc, ec="none"))
    n = int((x1 - x0) * (y1 - y0) / (r * r * 4))
    xs = rng.uniform(x0 + r, x1 - r, n)
    ys = rng.uniform(y0 + r, y1 - r, n)
    ax.scatter(xs, ys, s=0.6, color="#A89F8C", lw=0)


# ---------------------------------------------------------------- 40.1
def fig_am_process_families():
    fig = plt.figure(figsize=(6.8, 5.3))
    rng = np.random.default_rng(1)
    rects = [[0.0, 0.52, 0.33, 0.46], [0.335, 0.52, 0.33, 0.46], [0.67, 0.52, 0.33, 0.46],
             [0.12, 0.02, 0.33, 0.46], [0.55, 0.02, 0.33, 0.46]]
    axs = [_panel(fig, r, xlim=(-0.5, 10.5), ylim=(-1.2, 13.4)) for r in rects]
    titles = ["(a) PBF-LB", "(b) DED", "(c) binder jetting", "(d) material extrusion",
              "(e) vat photopolymerization (DLP)"]
    layers = ["layer ≈ 30 µm", "layer ≈ 1 mm", "layer ≈ 50 µm", "layer ≈ 0.2 mm", "layer ≈ 50 µm"]
    for ax, t, l in zip(axs, titles, layers):
        ax.text(5, 12.3, t, ha="center", va="bottom", fontsize=8.5, fontweight="bold")
        ax.text(5, -0.2, l, ha="center", va="top", fontsize=8.3, color=BLUE)

    # (a) PBF-LB
    a = axs[0]
    a.add_patch(Rectangle((0.3, 0.5), 9.4, 5.6, fc="none", ec=INK, lw=0.8))
    _powder(a, 0.4, 3.0, 2.0, 5.4, rng)                     # supply
    a.add_patch(Rectangle((0.4, 1.4), 2.6, 0.6, fc=METAL, ec=INK, lw=0.6))
    a.annotate("", xy=(1.7, 2.0), xytext=(1.7, 0.7), arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK))
    a.add_patch(Rectangle((3.2, 0.5), 0.15, 5.6, fc=INK))
    _powder(a, 3.4, 9.6, 2.6, 5.4, rng)                     # build bed
    a.add_patch(Rectangle((3.4, 2.0), 6.2, 0.6, fc=METAL, ec=INK, lw=0.6))
    a.annotate("", xy=(4.0, 0.7), xytext=(4.0, 2.0), arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK))
    # part with supports
    a.add_patch(Polygon([[5.0, 3.4], [8.4, 3.4], [8.4, 5.4], [5.0, 5.4]], fc="#6E7C8A", ec=INK, lw=0.6))
    for xx in np.arange(5.2, 8.4, 0.4):
        a.plot([xx, xx], [2.6, 3.4], color="#6E7C8A", lw=0.7)
    a.add_patch(Rectangle((2.6, 5.4), 0.5, 0.7, fc="#444444"))      # recoater blade
    a.annotate("", xy=(4.3, 5.75), xytext=(3.2, 5.75), arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK))
    a.text(2.85, 6.3, "recoater", fontsize=7, ha="center")
    # galvo scanner and beam
    a.add_patch(Rectangle((5.6, 10.0), 1.6, 0.9, fc="#555555"))
    a.text(6.4, 11.2, "galvo scanner", fontsize=7, ha="center")
    a.add_patch(Polygon([[6.3, 10.0], [6.5, 10.0], [7.1, 5.45], [7.0, 5.45]], fc="#E8473E", ec="none"))
    a.add_patch(Ellipse((7.05, 5.4), 0.6, 0.25, fc="#FFB000", ec="none"))
    a.text(8.0, 8.4, "laser", fontsize=7.5, color="#C0392B")
    a.annotate("", xy=(9.5, 7.2), xytext=(4.5, 7.2), arrowprops=dict(arrowstyle="-|>", lw=0.8, color=SKY))
    a.text(5.0, 7.45, "Ar flow", fontsize=7, color=SKY, ha="center")
    a.text(1.7, 4.0, "powder\nsupply", fontsize=6.8, ha="center")
    a.text(6.7, 4.3, "part", fontsize=7, color="white", ha="center")
    a.text(4.3, 1.15, "build plate\non piston", fontsize=6.6, ha="left", va="center")

    # (b) DED
    a = axs[1]
    a.add_patch(Rectangle((0.8, 0.8), 8.4, 1.0, fc=METAL, ec=INK, lw=0.6))
    a.text(5, 1.3, "substrate", fontsize=7, ha="center", va="center")
    for k in range(6):
        a.add_patch(Rectangle((3.6, 1.8 + k * 0.75), 2.8, 0.75, fc="#7C8A97", ec="#4A5560", lw=0.5))
        a.plot([3.6, 3.6], [1.8 + k * 0.75, 2.55 + k * 0.75], color="#4A5560", lw=0.3)
    a.add_patch(Ellipse((5.0, 6.35), 1.2, 0.45, fc="#FFB000", ec="none"))
    # nozzle with coaxial powder streams
    a.add_patch(Polygon([[3.6, 9.6], [6.4, 9.6], [5.5, 7.4], [4.5, 7.4]], fc="#B0B7BE", ec=INK, lw=0.7))
    a.add_patch(Polygon([[4.9, 10.8], [5.1, 10.8], [5.08, 6.5], [4.92, 6.5]], fc="#E8473E", ec="none"))
    for s in [-1, 1]:
        xs = np.linspace(5 + s * 0.6, 5 + s * 0.12, 12)
        ys = np.linspace(7.4, 6.5, 12)
        a.scatter(xs, ys, s=1.5, color="#6B5B45")
    a.text(5.0, 11.1, "laser / arc", fontsize=7, ha="center", color="#C0392B")
    a.text(7.6, 8.4, "coaxial\npowder\n(or wire)", fontsize=7, ha="center")
    a.text(7.4, 3.5, "deposited\nlayers", fontsize=7, ha="center")
    # robot arm hint
    a.plot([3.6, 1.8, 0.7], [9.3, 10.4, 9.0], color="#777777", lw=2.2, solid_capstyle="round")
    a.add_patch(Circle((1.8, 10.4), 0.3, fc="#777777"))
    a.text(0.4, 10.9, "robot arm", fontsize=6.8, ha="left", va="bottom", color="#555555")

    # (c) binder jetting
    a = axs[2]
    a.add_patch(Rectangle((0.6, 0.5), 8.8, 5.6, fc="none", ec=INK, lw=0.8))
    _powder(a, 0.7, 9.3, 1.2, 5.4, rng)
    a.add_patch(Rectangle((0.7, 0.6), 8.6, 0.6, fc=METAL, ec=INK, lw=0.6))
    a.add_patch(Polygon([[3.0, 3.6], [6.5, 3.6], [6.5, 5.4], [3.0, 5.4]], fc="#C29A6B", ec="none", alpha=0.85))
    a.add_patch(Rectangle((3.8, 6.6), 2.6, 0.9, fc="#555555"))
    a.text(6.6, 7.05, "inkjet\nprinthead", fontsize=7, ha="left", va="center")
    for xx in np.linspace(4.2, 6.0, 4):
        for yy in [6.15, 5.75]:
            a.add_patch(Circle((xx, yy), 0.12, fc="#8B5A2B"))
    a.text(4.75, 4.3, "bound part", fontsize=6.8, ha="center", color="white")
    a.add_patch(Rectangle((1.2, 5.4), 0.5, 0.6, fc="#444444"))
    a.text(1.45, 6.2, "recoater", fontsize=7, ha="center", va="bottom")
    # inset: sinter furnace
    a.add_patch(Rectangle((0.6, 9.8), 2.0, 1.0, fc="#C29A6B", ec=INK, lw=0.5))
    a.text(1.6, 9.6, "green part", fontsize=6.8, ha="center", va="top")
    a.annotate("", xy=(4.7, 10.3), xytext=(3.0, 10.3), arrowprops=dict(arrowstyle="-|>", lw=0.9, color=INK))
    a.add_patch(Rectangle((4.9, 9.2), 4.8, 2.3, fc="#F6E2D3", ec=INK, lw=0.7))
    a.add_patch(Rectangle((6.3, 9.55), 1.7, 0.85, fc="#7C8A97", ec=INK, lw=0.5))
    a.text(7.3, 11.0, "sinter furnace", fontsize=6.8, ha="center", va="center")
    a.text(7.3, 9.0, "≈ 17 % linear shrinkage", fontsize=6.8, ha="center", va="top")

    # (d) material extrusion
    a = axs[3]
    a.add_patch(Rectangle((0.8, 0.6), 8.4, 0.7, fc="#AAB4BE", ec=INK, lw=0.6))
    rows = 5
    for k in range(rows):
        for j in range(6):
            a.add_patch(Ellipse((2.6 + j * 0.95, 1.65 + k * 0.62), 1.02, 0.70, fc="#5B9BD5", ec="#2F5D8A", lw=0.5))
    # nozzle depositing the top bead
    a.add_patch(Polygon([[5.4, 9.0], [7.2, 9.0], [7.2, 6.4], [6.6, 5.6], [6.0, 5.6], [5.4, 6.4]],
                        fc="#B0B7BE", ec=INK, lw=0.7))
    a.add_patch(Rectangle((5.2, 6.6), 2.2, 1.4, fc="#E57373", ec=INK, lw=0.6))
    a.text(7.6, 7.3, "heater", fontsize=6.8, va="center")
    a.add_patch(Rectangle((6.15, 9.0), 0.3, 2.4, fc="#5B9BD5", ec=INK, lw=0.5))
    a.text(6.0, 11.0, "filament", fontsize=7, ha="right")
    a.add_patch(Ellipse((5.45, 5.2), 1.02, 0.70, fc="#5B9BD5", ec="#2F5D8A", lw=0.5))
    a.annotate("", xy=(3.6, 6.0), xytext=(5.2, 6.0), arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK))
    a.text(2.0, 7.4, "voids between\nrounded beads", fontsize=6.8, ha="center")
    a.annotate("", xy=(3.08, 1.97), xytext=(2.4, 6.7), arrowprops=dict(arrowstyle="-", lw=0.5, color="#555555"))

    # (e) vat photopolymerization, bottom-up DLP
    a = axs[4]
    a.add_patch(Polygon([[1.0, 5.0], [1.0, 2.6], [9.0, 2.6], [9.0, 5.0]], fc="none", ec=INK, lw=0.9))
    a.add_patch(Rectangle((1.05, 2.65), 7.9, 1.9, fc="#F3E9A6", ec="none"))
    a.add_patch(Rectangle((1.0, 2.35), 8.0, 0.3, fc="#CFE8F7", ec=INK, lw=0.6))
    a.text(9.2, 2.45, "window", fontsize=6.8, va="center", ha="left")
    a.add_patch(Rectangle((2.6, 0.1), 4.8, 1.3, fc="#555555"))
    a.text(5.0, 0.75, "UV projector", fontsize=7, ha="center", va="center", color="white")
    a.add_patch(Polygon([[4.4, 1.4], [5.6, 1.4], [6.4, 2.35], [3.6, 2.35]], fc="#B39DDB", alpha=0.7, ec="none"))
    # build platform and part, hanging upside down
    a.add_patch(Rectangle((2.6, 7.6), 4.8, 0.5, fc=METAL, ec=INK, lw=0.6))
    a.add_patch(Rectangle((4.8, 8.1), 0.4, 2.8, fc=METAL, ec=INK, lw=0.6))
    a.add_patch(Polygon([[3.4, 7.6], [6.6, 7.6], [6.3, 2.7], [3.7, 2.7]], fc="#8E7CC3", ec=INK, lw=0.6))
    a.annotate("", xy=(7.8, 10.6), xytext=(7.8, 8.6), arrowprops=dict(arrowstyle="-|>", lw=1.0, color=INK))
    a.text(8.05, 9.4, "lift", fontsize=7, va="center")
    a.text(1.4, 4.2, "resin", fontsize=7)
    a.text(5.0, 5.5, "part", fontsize=7, ha="center", color="white")
    save(fig, "48", "fig-48-1-am-process-families")


# ---------------------------------------------------------------- 40.2
def fig_process_window():
    h, t = 0.14, 0.03
    fig = plt.figure(figsize=(6.8, 4.4))
    ax = fig.add_axes([0.09, 0.12, 0.62, 0.82])
    v = np.linspace(200, 2500, 600)
    P = np.linspace(50, 450, 500)
    V, PP = np.meshgrid(v, P)
    E = PP / (V * h * t)
    reg = np.full(E.shape, 1)                   # 1 = dense
    reg[E < 47] = 0                             # lack of fusion
    reg[E > 78] = 2                             # keyhole
    reg[(PP > 400) & (E >= 47)] = 2
    reg[(V > 1750) & (PP > 230 + 0.06 * (V - 1750)) & (E < 78)] = 3   # balling / humping
    reg[(PP < 120) & (E <= 78)] = 0
    cmap = ListedColormap(["#F8D9D2", "#DDEFD9", "#DCE6F4", "#FBE7C6"])
    ax.pcolormesh(V, PP, reg, cmap=cmap, vmin=-0.5, vmax=3.5, shading="auto", rasterized=True)
    for Ev in [30, 56, 120]:
        ax.plot(v, Ev * v * h * t, ls="--", color="#555555", lw=1.0)
    ax.text(2420, 30 * 2420 * h * t - 14, "30 J/mm³", fontsize=8, ha="right", va="top", color="#555555",
            rotation=13)
    ax.text(1700, 56 * 1700 * h * t + 6, "56 J/mm³", fontsize=8, ha="right", va="bottom", color="#555555",
            rotation=26)
    ax.text(600, 120 * 600 * h * t + 6, "120 J/mm³", fontsize=8, ha="right", va="bottom", color="#555555",
            rotation=58)
    ax.text(330, 395, "keyhole\nporosity", fontsize=9.5, ha="left", color="#2F4F7F")
    ax.text(1850, 100, "lack of fusion", fontsize=9.5, ha="center", color="#9A3324")
    ax.text(2200, 415, "balling /\nhumping", fontsize=9.5, ha="center", color="#8A5A00")
    ax.text(1480, 372, "dense\n(> 99.5 %)", fontsize=9.5, ha="center", color="#2E7031", rotation=0)
    ax.plot(1200, 280, "o", color=INK, ms=6, zorder=5)
    ax.annotate("", xy=(1500, 280), xytext=(1215, 280),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.6, mutation_scale=12))
    ax.text(1170, 296, "worked example\n280 W, 1200 mm/s", fontsize=8, ha="right", va="bottom")
    ax.text(1520, 288, "1500 mm/s:\nLOF", fontsize=8, color=ORANGE, va="bottom")
    ax.set_xlim(200, 2500)
    ax.set_ylim(50, 450)
    ax.set_xlabel("scan speed $v$ (mm/s)")
    ax.set_ylabel("laser power $P$ (W)")
    ax.set_title("Ti–6Al–4V, PBF-LB, 30 µm layers, 0.14 mm hatch (schematic boundaries)", fontsize=8.5, loc="left")

    # melt-pool sketches
    names = [("conduction mode", "cond"), ("keyhole: deep pool,\ntrapped pore", "key"),
             ("lack of fusion:\ngap between tracks", "lof")]
    for i, (name, kind) in enumerate(names):
        a = fig.add_axes([0.75, 0.68 - i * 0.29, 0.24, 0.22])
        a.set_aspect("equal")
        a.axis("off")
        a.set_xlim(0, 6)
        a.set_ylim(-3.6, 0.6)
        a.add_patch(Rectangle((0, -3.4), 6, 3.4, fc="#E6EAEE", ec="none"))
        a.plot([0, 6], [0, 0], color=INK, lw=0.8)
        th = np.linspace(np.pi, 2 * np.pi, 60)
        if kind == "cond":
            a.add_patch(Polygon(np.column_stack([3 + 1.4 * np.cos(th), 0.75 * np.sin(th)]), fc="#F2A65A", ec=INK, lw=0.7))
        elif kind == "key":
            pts = np.column_stack([3 + 0.9 * np.cos(th), 3.0 * np.sin(th)])
            a.add_patch(Polygon(pts, fc="#F2A65A", ec=INK, lw=0.7))
            a.add_patch(Polygon([[2.85, 0], [3.15, 0], [3.05, -2.1], [2.95, -2.1]], fc="white", ec=INK, lw=0.5))
            a.add_patch(Circle((3.0, -2.65), 0.22, fc="white", ec=INK, lw=0.6))
        else:
            for cx in [1.0, 3.0, 5.0]:
                a.add_patch(Polygon(np.column_stack([cx + 0.95 * np.cos(th), 0.45 * np.sin(th)]), fc="#D7C2A8",
                                    ec=INK, lw=0.6))
            for cx in [2.0, 4.0]:
                a.add_patch(Polygon([[cx - 0.45, -0.25], [cx, -0.48], [cx + 0.45, -0.25], [cx + 0.25, -0.9],
                                     [cx - 0.1, -0.75], [cx - 0.3, -0.95]], fc="white", ec=INK, lw=0.5))
                a.add_patch(Circle((cx + 0.02, -0.58), 0.12, fc="#BBBBBB", ec=INK, lw=0.3))
        a.text(3, -3.5, name, fontsize=7.8, ha="center", va="top")
    save(fig, "48", "fig-48-2-process-window")


# ---------------------------------------------------------------- 40.3
def fig_g_r_solidification_map():
    fig, ax = new_fig(6.4, 4.8)
    R = np.logspace(-6, 1, 300)
    ax.set_xscale("log")
    ax.set_yscale("log")
    # morphology regions by G/R (K s / m^2), generic alloy
    b = [1e10, 1e9, 1e6]   # planar|cellular, cellular|columnar, columnar|equiaxed
    cols = ["#E8F1FA", "#DDEFD9", "#FFF4D6", "#F8DED5"]
    Rr = np.logspace(-7, 2, 400)
    ax.fill_between(Rr, b[0] * Rr, 1e9, color=cols[0], zorder=0)
    ax.fill_between(Rr, b[1] * Rr, b[0] * Rr, color=cols[1], zorder=0)
    ax.fill_between(Rr, b[2] * Rr, b[1] * Rr, color=cols[2], zorder=0)
    ax.fill_between(Rr, 1, b[2] * Rr, color=cols[3], zorder=0)
    for bb in b:
        ax.plot(Rr, bb * Rr, color="#777777", lw=0.9)
    ax.text(2e-6, 2.5e7, "planar", fontsize=9)
    ax.text(4e-5, 2.0e5, "cellular", fontsize=9)
    ax.text(2.5e-4, 1.4e3, "columnar\ndendritic", fontsize=9, ha="center", va="center")
    ax.text(1.0, 2.0e2, "equiaxed\ndendritic", fontsize=9, ha="center", va="bottom")
    rot = 39
    ax.text(3e-6, 4.6e4, "$G/R$ = 10$^{10}$", fontsize=7.5, color="#555555", rotation=rot, ha="left", va="bottom")
    ax.text(3e-6, 4.6e3, "10$^{9}$", fontsize=7.5, color="#555555", rotation=rot, ha="left", va="bottom")
    ax.text(2.5e-3, 3.6e3, "10$^{6}$ K s/m²", fontsize=7.5, color="#555555", rotation=rot, ha="left", va="bottom")
    # cooling-rate lines G*R
    for gr in [1, 1e2, 1e4, 1e6]:
        ax.plot(R, gr / R, ls="--", color=BLUE, lw=0.9)
    for gr, r_, lab in [(1, 2.2e-6, "$GR$ = 1 K/s"), (1e2, 2.2e-5, "10$^2$"), (1e4, 2.2e-4, "10$^4$"),
                        (1e6, 3e-2, "10$^6$ K/s")]:
        ax.text(r_, gr / r_ * 1.25, lab, fontsize=7.5, color=BLUE, rotation=-rot, ha="left", va="bottom")
    ax.annotate("", xy=(4e-2, 1.5e3), xytext=(4e-3, 1.5e2),
                arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.0))
    ax.text(3.5e-3, 1.25e2, "finer structure\n(higher $GR$)", fontsize=7.5, color=BLUE, ha="right", va="bottom")

    def ell(r0, r1, g0, g1, lab, c, lx, ly, ha="center"):
        cx, cy = np.sqrt(r0 * r1), np.sqrt(g0 * g1)
        t = np.linspace(0, 2 * np.pi, 100)
        xr, yr = np.log10(r1 / r0) / 2, np.log10(g1 / g0) / 2
        xs = 10 ** (np.log10(cx) + xr * np.cos(t))
        ys = 10 ** (np.log10(cy) + yr * np.sin(t))
        ax.fill(xs, ys, color=c, alpha=0.30, zorder=2)
        ax.plot(xs, ys, color=c, lw=1.4, zorder=3)
        ax.text(lx, ly, lab, fontsize=8.3, color=c, ha=ha, va="center", zorder=4, fontweight="bold")
    ell(1e-5, 1e-4, 1e2, 1e3, "sand casting", "#8B5A2B", 3.2e-5, 3.2e2)
    ell(4e-6, 2.5e-5, 1e3, 1e4, "directional\nsolidification", "#6A3D9A", 2.8e-5, 7e3, ha="left")
    ell(1e-3, 1e-2, 1e4, 1e5, "arc welding", ORANGE, 1.15e-2, 2.5e4, ha="left")
    ell(1e-3, 1e-2, 1e4, 1e6, "DED / WAAM", PINK, 8e-4, 6e5, ha="right")
    ell(1e-2, 1.6, 1e5, 1e7, "PBF-LB", GREEN, 0.12, 2.5e7)
    ax.plot(1.2, 2.2e6, "*", color=INK, ms=11, zorder=6)
    ax.annotate("worked example\n$G$ = 2.2×10$^6$ K/m, $R$ = 1.2 m/s\n$\\dot T$ = 2.7×10$^6$ K/s",
                xy=(1.2, 2.2e6), xytext=(8.0, 2.2e3), fontsize=7.8, ha="right", zorder=6,
                arrowprops=dict(arrowstyle="-", color=INK, lw=0.7))
    ax.annotate("", xy=(0.9, 1.7e6), xytext=(1.6e-2, 6e6),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.3, connectionstyle="arc3,rad=-0.25"), zorder=6)
    ax.text(1.4e-2, 9e6, "pool bottom\n(low $R$, high $G/R$)", fontsize=7.5, ha="right", va="bottom")
    ax.text(0.2, 2.6e5, "top centreline\n($R$ ≈ $v$)", fontsize=7.5, ha="center", va="top", zorder=6)
    ax.set_xlim(1e-6, 10)
    ax.set_ylim(1e2, 1e8)
    ax.set_xlabel("solidification rate $R$ (m/s)")
    ax.set_ylabel("thermal gradient $G$ (K/m)")
    save(fig, "48", "fig-48-3-g-r-solidification-map")


# ---------------------------------------------------------------- 40.4
def fig_am_defects():
    fig = plt.figure(figsize=(6.8, 4.4))
    rng = np.random.default_rng(4)
    ax = fig.add_axes([0.01, 0.05, 0.50, 0.88])
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-60, 1080)
    ax.set_ylim(-60, 1110)
    ax.add_patch(Rectangle((0, 0), 1000, 1000, fc="#E9EBEE", ec=INK, lw=0.9))
    # columnar prior grains along build direction
    xs = np.cumsum(rng.uniform(70, 150, 12))
    xs = xs[xs < 990]
    yy = np.linspace(0, 1000, 30)
    for x0 in xs:
        wav = x0 + 12 * np.sin(yy / 90 + x0) + 0.04 * yy
        ax.plot(wav, yy, color="#8792A0", lw=0.9)
    # melt-pool boundaries: stacked arcs (30 um layers, 140 um hatch)
    th = np.linspace(np.pi * 1.06, np.pi * 1.94, 30)
    for k, yl in enumerate(np.arange(60, 1000, 30)):
        off = 70 * (k % 2)
        for xc in np.arange(-70 + off, 1070, 140):
            px = xc + 80 * np.cos(th)
            py = yl + 75 * np.sin(th) + 30
            m = (px > 0) & (px < 1000) & (py > 0)
            ax.plot(px[m], py[m], color="#B6BCC4", lw=0.45)
    # rough top surface with partly fused particles
    xt = np.linspace(0, 1000, 200)
    ytop = 1000 + 10 * np.sin(xt / 23) + 6 * rng.standard_normal(200)
    ax.fill_between(xt, 1000, ytop, color="#E9EBEE", zorder=2)
    ax.plot(xt, ytop, color=INK, lw=0.9, zorder=3)
    for xp in [90, 260, 420, 610, 780, 930]:
        r = rng.uniform(15, 22)
        ax.add_patch(Circle((xp, 1010 + r * 0.6), r, fc="#D5D9DE", ec=INK, lw=0.6, zorder=3))
    ax.add_patch(Rectangle((-5, 990), 10, 20, fc="#E9EBEE", ec="none", zorder=2))
    # lack-of-fusion void ~200 um wide with an unmelted particle
    lof = np.array([[300, 545], [340, 560], [380, 552], [420, 566], [470, 555], [500, 548], [470, 532],
                    [430, 540], [400, 528], [350, 536], [320, 530]])
    ax.add_patch(Polygon(lof, fc="#2B2B2B", ec=INK, lw=0.6, zorder=4))
    ax.add_patch(Circle((395, 547), 13, fc="#C9CDD2", ec=INK, lw=0.6, zorder=5))
    # keyhole pores ~50 um at melt-pool bottoms
    for (x, y) in [(640, 236), (220, 806), (780, 686)]:
        ax.add_patch(Circle((x, y), 25, fc="#2B2B2B", ec="none", zorder=4))
    # gas pores ~10 um
    for _ in range(14):
        ax.add_patch(Circle((rng.uniform(40, 960), rng.uniform(40, 950)), 5, fc="#2B2B2B", ec="none", zorder=4))
    # labels
    kw = dict(fontsize=7.8, arrowprops=dict(arrowstyle="-", color=ORANGE, lw=0.8), color=INK, zorder=6,
              bbox=dict(fc="white", ec="none", pad=0.8, alpha=0.85))
    ax.annotate("lack-of-fusion void\n(~200 µm) with\nunmelted particle", xy=(470, 552), xytext=(560, 430), **kw)
    ax.annotate("keyhole pore\n(~50 µm)", xy=(640, 236), xytext=(700, 90), **kw)
    ax.annotate("gas pores\n(~10 µm)", xy=(rng.uniform(0, 1) * 0 + 140, 300), xytext=(40, 120), **kw)
    ax.annotate("melt-pool\nboundaries", xy=(560, 878), xytext=(600, 760), **kw)
    ax.annotate("columnar prior grains", xy=(xs[1] + 30, 640), xytext=(20, 660), **kw)
    ax.annotate("partly fused particles,\nRa ≈ 10 µm", xy=(610, 1030), xytext=(560, 1065), **kw)
    ax.annotate("", xy=(1050, 600), xytext=(1050, 300), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.2))
    ax.text(1062, 450, "build direction", rotation=90, fontsize=7.8, va="center")
    ax.plot([20, 220], [-30, -30], color=INK, lw=2)
    ax.text(120, -40, "200 µm", ha="center", va="top", fontsize=7.8)
    ax.text(500, -40, "polished section, 1 mm field", ha="left", va="top", fontsize=7.8, color="#555555")
    ax.add_patch(Circle((140, 300), 5, fc="#2B2B2B", ec="none", zorder=4))

    # ---- right: temperature-gradient mechanism
    titles = ["(1) heating: hot top layer expands,\nrestrained → compressive yielding",
              "(2) cooling: top layer contracts,\nleft in tension; layers below in compression"]
    for i in range(2):
        a = fig.add_axes([0.55, 0.58 - i * 0.30, 0.44, 0.27])
        a.set_aspect("equal")
        a.axis("off")
        a.set_xlim(0, 12)
        a.set_ylim(-0.5, 5.6)
        a.add_patch(Rectangle((0.5, 0), 11, 0.8, fc=METAL, ec=INK, lw=0.6))
        for k in range(3):
            a.add_patch(Rectangle((2, 0.8 + k * 0.6), 8, 0.6, fc="#C9D0D7", ec=INK, lw=0.5))
        top = Rectangle((2, 2.6), 8, 0.6, fc="#F2A65A" if i == 0 else "#F6C08B", ec=INK, lw=0.6)
        a.add_patch(top)
        if i == 0:
            a.annotate("", xy=(1.0, 2.9), xytext=(2.5, 2.9), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.2))
            a.annotate("", xy=(11.0, 2.9), xytext=(9.5, 2.9), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.2))
            a.text(6.3, 3.75, "laser heat", fontsize=7.5, ha="left", color="#C0392B")
            a.annotate("", xy=(6, 3.25), xytext=(6, 4.2), arrowprops=dict(arrowstyle="-|>", color="#C0392B", lw=1.2))
            a.text(6, 2.9, "− (yields)", fontsize=7.5, ha="center", va="center")
        else:
            a.annotate("", xy=(3.5, 2.9), xytext=(1.6, 2.9), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.2))
            a.annotate("", xy=(8.5, 2.9), xytext=(10.4, 2.9), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.2))
            a.text(6, 2.9, "+  tension", fontsize=7.5, ha="center", va="center")
            a.text(6, 1.7, "−  compression", fontsize=7.5, ha="center", va="center")
        a.text(6, 4.6, titles[i], fontsize=7.6, ha="center", va="bottom")
    # cantilever distortion after cutting from the plate
    a = fig.add_axes([0.55, 0.02, 0.44, 0.24])
    a.set_aspect("equal")
    a.axis("off")
    a.set_xlim(0, 12)
    a.set_ylim(-0.6, 4.4)
    a.add_patch(Rectangle((0.5, 0), 11, 0.6, fc=METAL, ec=INK, lw=0.6))
    a.add_patch(Rectangle((1.5, 0.6), 1.2, 2.2, fc="#C9D0D7", ec=INK, lw=0.5))
    for xx in np.arange(3.0, 10.4, 0.5):
        a.plot([xx, xx], [0.6, 2.1], color="#9AA3AD", lw=0.6, ls=":")
    a.add_patch(Rectangle((2.7, 2.2), 7.8, 0.6, fc="#C9D0D7", ec="#888888", lw=0.5, ls="--"))
    x = np.linspace(2.7, 10.5, 40)
    defl = 0.012 * (x - 2.7) ** 2
    a.fill_between(x, 2.2 + defl, 2.8 + defl, color="#F6C08B", ec=INK, lw=0.6)
    a.plot([2.6, 3.0], [1.6, 1.4], color=ORANGE, lw=1.0)
    a.text(3.2, 1.25, "cut supports", fontsize=7.3, color=ORANGE, va="top")
    a.text(6.5, 4.1, "(3) after cutting from the plate the cantilever curls up", fontsize=7.6, ha="center", va="top")
    save(fig, "48", "fig-48-4-am-defects")


# ---------------------------------------------------------------- 40.5
def _sn(N, S4, Se, tau=0.75):
    lg = np.log10(N)
    return Se + (S4 - Se) * np.exp(-(lg - 4) / tau)


def fig_ti64_fatigue_postprocessing():
    fig = plt.figure(figsize=(6.8, 4.3))
    ax = fig.add_axes([0.09, 0.12, 0.62, 0.84])
    N = np.logspace(4, 8, 200)
    curves = [("as built, as-built surface", 640, 250, PINK, "-"),
              ("stress relieved, as-built surface", 680, 300, ORANGE, "-"),
              ("HIP, as-built surface", 700, 350, YELLOW, "-"),
              ("machined, not HIPed (internal LOF)", 840, 450, SKY, "-"),
              ("HIP + machined", 900, 550, BLUE, "-"),
              ("wrought, mill annealed", 920, 575, INK, "--")]
    for lab, S4, Se, c, ls in curves:
        S = _sn(N, S4, Se)
        if "not HIPed" in lab:
            ax.fill_between(N, _sn(N, S4 - 90, Se - 70), _sn(N, S4 + 60, Se + 50), color=c, alpha=0.22, lw=0)
        ax.plot(N, S, color=c, ls=ls, lw=2.0, label=f"{lab} (~{Se} MPa)")
    ax.axhline(312, xmin=0.0, xmax=1.0, color="#555555", lw=1.0, ls=":")
    ax.axhline(416, xmin=0.0, xmax=1.0, color="#555555", lw=1.0, ls=":")
    ax.text(1.15e4, 318, "Murakami: 312 MPa\n(100 µm surface LOF)", fontsize=7.3, ha="left", va="bottom", color="#444444", bbox=dict(fc="white", ec="none", pad=0.5, alpha=0.85), zorder=6)
    ax.text(1.15e4, 422, "Murakami: 416 MPa\n(30 µm internal pore)", fontsize=7.3, ha="left", va="bottom", color="#444444", bbox=dict(fc="white", ec="none", pad=0.5, alpha=0.85), zorder=6)
    ax.set_xscale("log")
    ax.set_xlim(1e4, 1e8)
    ax.set_ylim(100, 1000)
    ax.set_xlabel("cycles to failure $N$")
    ax.set_ylabel("maximum stress (MPa), $R$ = 0.1")
    ax.legend(loc="upper right", fontsize=7.4, handlelength=1.8)
    ax.text(1.15e4, 120, "schematic, typical PBF-LB Ti–6Al–4V", fontsize=7.5, color="#555555")

    # fractograph sketches
    rng = np.random.default_rng(9)
    titles = ["surface LOF defect\nwith unmelted particles", "internal ~30 µm pore\n(fish-eye)",
              "α-lath boundaries\n(defect-free)"]
    for i in range(3):
        a = fig.add_axes([0.765, 0.69 - i * 0.31, 0.22, 0.22])
        a.set_aspect("equal")
        a.axis("off")
        a.set_xlim(-1.15, 1.15)
        a.set_ylim(-1.15, 1.15)
        a.add_patch(Circle((0, 0), 1.0, fc="#D9DDE2", ec=INK, lw=0.8))
        if i == 0:
            o = np.array([0, 0.98])
        elif i == 1:
            o = np.array([0.15, 0.25])
        else:
            o = np.array([-0.3, -0.2])
        # river lines and beach marks from origin
        for ang in np.linspace(0, 2 * np.pi, 22, endpoint=False):
            e = o + 2.2 * np.array([np.cos(ang), np.sin(ang)])
            ln = np.linspace(0, 1, 30)
            p = o[None, :] + ln[:, None] * (e - o)[None, :]
            m = np.hypot(p[:, 0], p[:, 1]) < 0.97
            a.plot(p[m, 0], p[m, 1], color="#9AA3AD", lw=0.4)
        for r in [0.35, 0.6, 0.85]:
            t = np.linspace(0, 2 * np.pi, 100)
            p = o[None, :] + r * np.column_stack([np.cos(t), np.sin(t)])
            m = np.hypot(p[:, 0], p[:, 1]) < 0.97
            pp = p.copy()
            pp[~m] = np.nan
            a.plot(pp[:, 0], pp[:, 1], color="#7A8490", lw=0.6)
        if i == 0:
            a.add_patch(Polygon([[-0.3, 0.95], [0.3, 0.95], [0.2, 0.8], [-0.05, 0.75], [-0.25, 0.82]],
                                fc="#333333", ec="none"))
            for dx in [-0.15, 0.1]:
                a.add_patch(Circle((dx, 0.86), 0.06, fc="#BBBBBB", ec=INK, lw=0.3))
        elif i == 1:
            a.add_patch(Circle(o, 0.09, fc="#333333"))
            a.add_patch(Circle(o, 0.3, fc="none", ec="#555555", lw=0.6))
        else:
            for k in range(6):
                a.plot([o[0] - 0.12 + 0.05 * k, o[0] - 0.02 + 0.05 * k], [o[1] - 0.12, o[1] + 0.12], color="#333333", lw=0.7)
        a.text(0, -1.2, titles[i], fontsize=7.3, ha="center", va="top")
    fig.text(0.875, 0.985, "crack origins", fontsize=8.5, ha="center", va="top", fontweight="bold")
    save(fig, "48", "fig-48-5-ti64-fatigue-postprocessing")


# ---------------------------------------------------------------- 40.6
def _cube_edges():
    c = np.array([[x, y, z] for x in (0, 1) for y in (0, 1) for z in (0, 1)], float)
    e = [(i, j) for i in range(8) for j in range(i + 1, 8) if np.sum(np.abs(c[i] - c[j])) == 1]
    return c, e


def _proj(p):
    p = np.atleast_2d(p)
    return np.column_stack([p[:, 0] + 0.45 * p[:, 1], p[:, 2] + 0.28 * p[:, 1]])


def fig_lattice_scaling():
    Es = 114.0
    fig = plt.figure(figsize=(6.8, 4.6))
    ax = fig.add_axes([0.10, 0.12, 0.56, 0.82])
    rho = np.logspace(-2, 0, 200)
    ax.axhspan(0.1, 2.0, color="#F6E3C6", zorder=0)
    ax.axhspan(15, 20, color="#E3D3EE", zorder=0)
    ax.text(0.0115, 0.6, "trabecular bone 0.1–2 GPa", fontsize=8.3, va="center")
    ax.text(0.0115, 25, "cortical bone 15–20 GPa", fontsize=8.3, va="bottom")
    rv = rho <= 1 / 3
    ax.plot(rho[rv], Es * rho[rv] ** 2, color=BLUE, lw=2.0, label="bending-dominated  $E^*=E_s\\bar\\rho^{\\,2}$")
    ax.plot(rho[~rv], Es * rho[~rv] ** 2, color=BLUE, lw=1.2, ls=':')
    ax.plot(rho[rv], Es * rho[rv] / 3, color=ORANGE, lw=2.0, label="stretch-dominated  $E^*=E_s\\bar\\rho/3$")
    ax.plot(rho[~rv], Es * rho[~rv] / 3, color=ORANGE, lw=1.2, ls=':')
    ax.plot(1, Es, "s", color=INK, ms=6)
    ax.text(0.9, Es, "solid Ti–6Al–4V\n114 GPa", fontsize=8, ha="right", va="center")
    ax.axvspan(0.3, 1.0, color="#EEEEEE", zorder=0)
    ax.text(0.55, 0.02, "scaling laws\nunreliable\n(ρ̄ > 0.3)", fontsize=7.6, ha="center", color="#666666")
    # worked example
    for r_, e_, c in [(0.2, Es * 0.04, BLUE), (0.3, Es * 0.09, BLUE), (0.2, Es * 0.2 / 3, ORANGE)]:
        ax.plot(r_, e_, "o", color=c, ms=7, mec=INK, zorder=5)
    ax.annotate("4.6 GPa", xy=(0.2, 4.56), xytext=(0.07, 7.5), fontsize=8, arrowprops=dict(arrowstyle="-", lw=0.6))
    ax.annotate("10.3 GPa", xy=(0.3, 10.26), xytext=(0.36, 4.0), fontsize=8, arrowprops=dict(arrowstyle="-", lw=0.6))
    ax.annotate("7.6 GPa", xy=(0.2, 7.6), xytext=(0.25, 2.6), fontsize=8, arrowprops=dict(arrowstyle="-", lw=0.6))
    # measured PBF lattice data (typical, below the bending line)
    rng = np.random.default_rng(3)
    rr = np.logspace(np.log10(0.05), np.log10(0.4), 14)
    ee = Es * rr ** 2 * rng.uniform(0.45, 0.85, rr.size)
    ax.scatter(rr, ee, s=16, facecolor="white", edgecolor=BLUE, lw=1.0, zorder=4,
               label="typical PBF strut lattices (measured)")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.01, 1)
    ax.set_ylim(0.01, 200)
    ax.set_xlabel("relative density $\\bar\\rho = \\rho^*/\\rho_s$")
    ax.set_ylabel("lattice modulus $E^*$ (GPa), Ti–6Al–4V")
    ax.legend(loc="upper left", fontsize=7.8)
    sec = ax.secondary_yaxis("right", functions=(lambda e: e / Es, lambda r: r * Es))
    sec.set_ylabel("$E^*/E_s$")

    # unit-cell sketches
    c, edges = _cube_edges()
    names = ["BCC strut cell\n(bending)", "octet truss\n(stretch)", "gyroid sheet\n(intermediate)"]
    for i in range(3):
        a = fig.add_axes([0.80, 0.69 - i * 0.31, 0.17, 0.22])
        a.set_aspect("equal")
        a.axis("off")
        a.set_xlim(-0.15, 1.6)
        a.set_ylim(-0.15, 1.45)
        if i < 2:
            for (p, q) in edges:
                pq = _proj(np.array([c[p], c[q]]))
                a.plot(pq[:, 0], pq[:, 1], color="#AAAAAA", lw=0.6)
        if i == 0:
            for p in c:
                pq = _proj(np.array([p, [0.5, 0.5, 0.5]]))
                a.plot(pq[:, 0], pq[:, 1], color=BLUE, lw=1.6)
        elif i == 1:
            fcs = [[0.5, 0.5, 0], [0.5, 0.5, 1], [0.5, 0, 0.5], [0.5, 1, 0.5], [0, 0.5, 0.5], [1, 0.5, 0.5]]
            pts = np.vstack([c, fcs])
            for p in range(len(pts)):
                for q in range(p + 1, len(pts)):
                    d = np.linalg.norm(pts[p] - pts[q])
                    if abs(d - np.sqrt(0.5)) < 1e-6:
                        pq = _proj(pts[[p, q]])
                        a.plot(pq[:, 0], pq[:, 1], color=ORANGE, lw=1.1)
        else:
            g = np.linspace(0, 4 * np.pi, 240)
            X, Y = np.meshgrid(g, g)
            F = np.sin(X) * np.cos(Y) + np.sin(Y) * np.cos(np.pi / 4) + np.sin(np.pi / 4) * np.cos(X)
            a.contourf(X / (4 * np.pi) * 1.3, Y / (4 * np.pi) * 1.3, F, levels=[-0.3, 0.3], colors=[GREEN])
            a.contour(X / (4 * np.pi) * 1.3, Y / (4 * np.pi) * 1.3, F, levels=[-0.3, 0.3], colors=INK,
                      linewidths=0.5)
        a.text(0.7, -0.2, names[i], fontsize=7.8, ha="center", va="top")
    save(fig, "48", "fig-48-6-lattice-scaling")


if __name__ == "__main__":
    fig_am_process_families()
    fig_process_window()
    fig_g_r_solidification_map()
    fig_am_defects()
    fig_ti64_fatigue_postprocessing()
    fig_lattice_scaling()
