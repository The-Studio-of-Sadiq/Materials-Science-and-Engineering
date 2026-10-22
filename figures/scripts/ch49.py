"""Figures for Chapter 49 — Thin Films, Coatings and Electronic Materials Processing. Run from the repository root: python figures/scripts/ch49.py"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle, Polygon, Ellipse, FancyBboxPatch, Circle  # noqa: E402
from scipy.spatial import Voronoi  # noqa: E402

KB = 1.380649e-23
EV = 1.602177e-19
BLUE, VERM, GREEN, PINK, ORANGE, SKY = COLORS[:6]


# ---------------------------------------------------------------- Figure 49.1
def vacuum_regimes():
    fig = plt.figure(figsize=(6.6, 4.9))
    gs = fig.add_gridspec(2, 1, height_ratios=[3.2, 1.0], hspace=0.08)
    ax = fig.add_subplot(gs[0])
    axb = fig.add_subplot(gs[1], sharex=ax)

    p = np.logspace(-8, 5, 300)
    d = 0.37e-9
    lam = KB * 298 / (np.sqrt(2) * np.pi * d ** 2 * p)
    m = 18 * 1.66054e-27
    phi = p / np.sqrt(2 * np.pi * m * KB * 298)
    tau = 1e19 / phi

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1e-8, 1e5)
    ax.set_ylim(1e-8, 1e5)
    ax.plot(p, lam, color=BLUE, lw=2)
    ax.set_ylabel(r"N$_2$ mean free path $\lambda$ (m)", color=BLUE)
    ax.tick_params(axis="y", colors=BLUE)

    ax2 = ax.twinx()
    ax2.spines["right"].set_visible(True)
    ax2.set_yscale("log")
    ax2.set_ylim(1e-6, 1e7)
    ax2.plot(p, tau, color=VERM, lw=2)
    ax2.set_ylabel(r"H$_2$O monolayer time $\tau$ (s)", color=VERM)
    ax2.tick_params(axis="y", colors=VERM)

    # Kn = 1 line
    ax.axhline(0.5, color=INK, ls="--", lw=0.9)
    ax.text(0.05, 0.7, r"$\lambda$ = 0.5 m: Kn = 1 for a typical chamber", fontsize=8, ha="left", va="bottom")
    ax.text(1.5e-7, 2e-1, "ballistic\n(Kn ≫ 1)", fontsize=8, ha="center", va="top", color="0.3")
    ax.text(1.5e3, 3e-2, "continuum flow\n(Kn ≪ 1)", fontsize=8, ha="center", va="top", color="0.3")

    for pp, txt, dx, va in [(1e5, "68 nm", 0.25, "bottom"), (1.0, "6.8 mm", 2.5, "bottom"),
                            (1e-4, "68 m", 2.5, "bottom")]:
        lv = 6.764e-3 / pp
        ax.plot(pp, lv, "o", color=BLUE, ms=5, zorder=5, clip_on=False)
        ax.text(pp * dx, lv * 1.6, txt, color=BLUE, fontsize=8.5, ha="left" if dx > 1 else "right", va=va)
    for pp, txt in [(1e-4, "2.8 s"), (1e-7, "2800 s\n(46 min)")]:
        tv = 2.78e-4 / pp
        ax2.plot(pp, tv, "s", color=VERM, ms=5, zorder=5)
        ax2.text(pp * 1.8, tv * 1.6, txt, color=VERM, fontsize=8.5, ha="left", va="bottom")
    ax.text(3e-8, 3e3, r"$\lambda$", color=BLUE, fontsize=11)
    ax2.text(1.2e-2, 3e-4, r"$\tau$ (sticking 1, 10$^{19}$ sites/m$^2$)", color=VERM, fontsize=8.5,
             rotation=-26, ha="left", va="bottom")
    plt.setp(ax.get_xticklabels(), visible=False)

    # process bands
    bands = [("MBE", 1e-8, 1e-6, 4, BLUE), ("evaporation", 1e-5, 1e-3, 3, SKY),
             ("magnetron\nsputtering", 0.1, 1, 2, GREEN), ("LPCVD /\nPECVD", 10, 300, 1, ORANGE),
             ("APCVD", 7e4, 1e5, 0, VERM)]
    for name, a, b, row, c in bands:
        axb.add_patch(Rectangle((a, row - 0.35), b - a, 0.7, fc=c, ec=INK, lw=0.6, alpha=0.75))
        xt = np.sqrt(a * b)
        if name == "APCVD":
            axb.text(a / 1.4, row, name, ha="right", va="center", fontsize=8)
        elif name.startswith("magnetron") or name.startswith("LPCVD"):
            axb.text(b * 1.4, row, name.replace("\n", " "), ha="left", va="center", fontsize=8)
        else:
            axb.text(b * 1.4, row, name, ha="left", va="center", fontsize=8)
    axb.set_ylim(-0.7, 4.7)
    axb.set_yticks([])
    axb.spines["left"].set_visible(False)
    axb.set_xlabel("pressure (Pa)")
    axb.set_xticks([1e-8, 1e-6, 1e-4, 1e-2, 1, 1e2, 1e4])
    axb.text(1e-8, 4.85, "operating windows", fontsize=8, color="0.3", va="bottom")
    save(fig, "49", "fig-49-1-vacuum-regimes")


# ---------------------------------------------------------------- Figure 49.2
def cvd_grove_regimes():
    fig, ax = new_fig(6.4, 4.0)
    x = np.linspace(0.60, 0.95, 300)
    T = 1000 / x
    cg, n1 = 1e22, 5e28
    ks = 3.73e4 * np.exp(-1.6 * EV / (KB * T))
    conv = cg / n1 * 1e6 * 60  # m/s -> um/min factor applied to velocity

    def G(hg):
        return ks * hg / (ks + hg) * conv

    ax.plot(x, G(0.05), color=BLUE, lw=2.2, label=r"$h_g$ = 0.05 m/s")
    ax.plot(x, G(0.10), color=VERM, lw=1.6, label=r"$h_g$ = 0.10 m/s (more flow; limit 1.2 µm/min)")
    ax.plot(x, ks * conv, color=INK, ls="--", lw=0.9)
    ax.axhline(0.05 * conv, color=INK, ls="--", lw=0.9)
    ax.text(0.605, 0.05 * conv * 1.06, "transport limit 0.6 µm/min", fontsize=8, va="bottom")
    ax.text(0.835, 0.13, r"reaction-limited asymptote, $E_a$ = 1.6 eV", fontsize=8, rotation=-47,
            ha="center", va="center", rotation_mode="anchor")

    pts = [(800, 0.013), (900, 0.054), (1000, 0.154), (1100, 0.30), (1200, 0.43), (1300, 0.51)]
    for tc, g in pts:
        xx = 1000 / (tc + 273.15)
        ax.plot(xx, g, "o", color=BLUE, ms=5, mfc="white", mew=1.4, zorder=5)
        if tc == 800:
            ax.text(xx - 0.01, g, f"{g:g}", fontsize=7.5, color=BLUE, ha="right", va="center")
        else:
            ax.text(xx - 0.006, g / 1.2, f"{g:g}", fontsize=7.5, color=BLUE, ha="right", va="top")

    ax.set_yscale("log")
    ax.set_ylim(0.01, 1)
    ax.set_xlim(0.60, 0.95)
    ax.set_xlabel(r"1000/$T$ (K$^{-1}$)")
    ax.set_ylabel("growth rate $G$ (µm/min)")
    ax.set_yticks([0.01, 0.03, 0.1, 0.3, 1])
    ax.set_yticklabels(["0.01", "0.03", "0.1", "0.3", "1"])

    top = ax.secondary_xaxis("top", functions=(lambda v: 1000 / np.maximum(v, 1e-3) - 273.15,
                                               lambda c: 1000 / (np.asarray(c) + 273.15)))
    top.set_xticks([800, 900, 1000, 1100, 1200, 1300])
    top.set_xlabel("temperature (°C)")
    ax.spines["top"].set_visible(True)

    ax.axvspan(0.60, 1000 / (1150 + 273.15), color=ORANGE, alpha=0.10, lw=0)
    ax.axvspan(1000 / (1000 + 273.15), 0.95, color=GREEN, alpha=0.08, lw=0)
    ax.text(0.612, 0.16, "transport-limited:\nflow design matters", fontsize=8.5, va="center")
    ax.text(0.885, 0.42, "reaction-limited:\nLPCVD, conformal", fontsize=8.5, va="center", ha="center")
    ax.annotate(r"knee: $k_s = h_g$", xy=(1000 / 1373.15, 0.30), xytext=(0.74, 0.62), fontsize=8,
                arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK))
    ax.legend(loc="lower left", fontsize=8)
    save(fig, "49", "fig-49-2-cvd-grove-regimes")


# ---------------------------------------------------------------- Figure 49.3
ML = 0.22  # monolayer height in drawing units


def _substrate(ax, x0, w, y0):
    ax.add_patch(Rectangle((x0, y0 - 0.55), w, 0.55, fc="#BBBBBB", ec=INK, lw=0.7))
    for xx in np.arange(x0 + 0.11, x0 + w, 0.22):
        ax.add_patch(Circle((xx, y0 - 0.11), 0.09, fc="#9A9A9A", ec="none"))


def _layer(ax, x0, x1, y, fc):
    ax.add_patch(Rectangle((x0, y), x1 - x0, ML, fc=fc, ec=INK, lw=0.5))


def _island(ax, xc, r, y0, fc, aspect=1.0, clip=None):
    th = np.linspace(0, np.pi, 40)
    pts = np.column_stack([xc + r * np.cos(th), y0 + aspect * r * np.sin(th)])
    pg = Polygon(pts, closed=True, fc=fc, ec=INK, lw=0.6)
    ax.add_patch(pg)
    if clip is not None:
        pg.set_clip_path(Rectangle(clip[0], clip[1], clip[2], transform=ax.transData))


def _pyramid(ax, xc, wb, h, y0, fc):
    ax.add_patch(Polygon([(xc - wb / 2, y0), (xc + wb / 2, y0), (xc + wb * 0.12, y0 + h),
                          (xc - wb * 0.12, y0 + h)], closed=True, fc=fc, ec=INK, lw=0.6))


def growth_modes():
    fig, ax = schematic(6.8, 4.9, xlim=(-1.2, 14.6), ylim=(-1.9, 9.6))
    W = 4.0
    cols = [0.0, 4.9, 9.8]
    rows = [7.0, 4.2, 1.4]  # substrate top for coverage 0.5, 1.5, 4 ML
    fcs = ["#7FB7DE", "#E8A67A", "#8CCFB3"]
    for y in rows:
        for x0 in cols:
            _substrate(ax, x0, W, y)
    for y, lab in zip(rows, ["0.5 ML", "1.5 ML", "≈ 4 ML"]):
        ax.text(-0.25, y + 0.25, lab, ha="right", va="center", fontsize=9, weight="bold")
    ax.text(-0.25, 8.75, "coverage", ha="right", va="center", fontsize=8, color="0.3")

    # Frank-van der Merwe
    x0, fc = cols[0], fcs[0]
    for a, b in [(0.3, 1.3), (2.0, 3.0)]:
        _layer(ax, x0 + a, x0 + b, rows[0], fc)
    _layer(ax, x0, x0 + W, rows[1], fc)
    for a, b in [(0.6, 2.6)]:
        _layer(ax, x0 + a, x0 + b, rows[1] + ML, fc)
    for k in range(4):
        _layer(ax, x0, x0 + W, rows[2] + k * ML, fc)

    # Volmer-Weber: islands with volume = coverage
    x0, fc = cols[1], fcs[1]
    rng = np.random.default_rng(4)
    for y, cov, n in [(rows[0], 0.5, 3), (rows[1], 1.5, 3), (rows[2], 4.0, 3)]:
        area = cov * ML * W
        r = np.sqrt(2 * area / (n * np.pi * 0.9))
        xs = np.linspace(x0 + W / (2 * n), x0 + W - W / (2 * n), n)
        for xc in xs:
            _island(ax, xc, r, y, fc, aspect=0.9, clip=((x0, y), W, 3.0))
    # Stranski-Krastanov
    x0, fc = cols[2], fcs[2]
    _layer(ax, x0 + 0.2, x0 + 2.2, rows[0], fc)
    _layer(ax, x0 + 2.6, x0 + 3.6, rows[0], fc)
    _layer(ax, x0, x0 + W, rows[1], fc)
    _layer(ax, x0 + 1.0, x0 + 3.0, rows[1] + ML, fc)
    for k in range(2):
        _layer(ax, x0, x0 + W, rows[2] + k * ML, fc)
    for xc in [x0 + 1.0, x0 + 3.0]:
        _pyramid(ax, xc, 1.5, 0.6, rows[2] + 2 * ML, fc)

    titles = ["Frank–van der Merwe\n(layer)", "Volmer–Weber\n(island)", "Stranski–Krastanov\n(layer + island)"]
    crit = [r"$\gamma_s \geq \gamma_f + \gamma_i$", r"$\gamma_s < \gamma_f + \gamma_i$",
            "wetting layer +\nstrain relief"]
    ex = ["AlGaAs/GaAs", "Ag on glass", "Ge/Si, InAs/GaAs\nquantum dots"]
    for x0, t, c, e in zip(cols, titles, crit, ex):
        ax.text(x0 + W / 2, 9.45, t, ha="center", va="top", fontsize=9.5, weight="bold")
        ax.text(x0 + W / 2, 0.45, c, ha="center", va="top", fontsize=9.5)
        ax.text(x0 + W / 2, -0.75 if "\n" not in c else -1.05, e, ha="center", va="top", fontsize=8.5,
                style="italic", color="0.25")
    ax.text(cols[2] + 0.1, rows[2] + 2 * ML + 0.75, "", fontsize=7)
    ax.annotate("wetting layer", xy=(cols[2] + 3.9, rows[2] + ML), xytext=(cols[2] + 4.15, rows[2] + 1.1),
                fontsize=7.5, ha="left", arrowprops=dict(arrowstyle="-", lw=0.6))
    save(fig, "49", "fig-49-3-growth-modes")


# ---------------------------------------------------------------- Figure 49.4
def _zone_sketch(ax, zone, x0, y0, w, h, rng):
    """Film cross-section sketch inside the rectangle (x0, y0, w, h)."""
    fc = "#E7EEF6"
    ax.add_patch(Rectangle((x0, y0 - 0.12 * h), w, 0.12 * h, fc="0.7", ec=INK, lw=0.6))
    if zone == "1":
        n = 5
        for k in range(n):
            xc = x0 + (k + 0.5) * w / n
            hh = h * (0.8 + rng.uniform(-0.08, 0.06))
            wb, wt = 0.05 * w, 0.17 * w
            th = np.linspace(0, np.pi, 20)
            top = [(xc + wt / 2 * np.cos(t), y0 + hh + 0.07 * h * np.sin(t)) for t in th]
            pts = [(xc - wb / 2, y0), (xc + wb / 2, y0), (xc + wt / 2, y0 + hh)] + top[1:-1] + [(xc - wt / 2, y0 + hh)]
            ax.add_patch(Polygon(pts, closed=True, fc=fc, ec=INK, lw=0.6))
    elif zone == "T":
        x = x0
        while x < x0 + w - 1e-6:
            ww = min(rng.uniform(0.05, 0.09) * w, x0 + w - x)
            ax.add_patch(Rectangle((x, y0), ww, 0.85 * h, fc=fc, ec=INK, lw=0.45))
            x += ww
    elif zone == "2":
        edges = x0 + w * np.array([0, 0.27, 0.52, 0.78, 1.0])
        for a, b in zip(edges[:-1], edges[1:]):
            pts = [(a, y0), (b, y0), (b, y0 + 0.78 * h), ((a + b) / 2, y0 + 0.92 * h), (a, y0 + 0.78 * h)]
            ax.add_patch(Polygon(pts, closed=True, fc=fc, ec=INK, lw=0.7))
    else:
        ax.add_patch(Rectangle((x0, y0), w, 0.85 * h, fc=fc, ec=INK, lw=0.7))
        pts = np.column_stack([rng.uniform(x0 - w * 0.3, x0 + w * 1.3, 40),
                               rng.uniform(y0 - h * 0.3, y0 + h * 1.2, 40)])
        vor = Voronoi(pts)
        clip = Rectangle((x0, y0), w, 0.85 * h, transform=ax.transData)
        for (p, q) in vor.ridge_vertices:
            if p >= 0 and q >= 0:
                v = vor.vertices[[p, q]]
                ln, = ax.plot(v[:, 0], v[:, 1], color=INK, lw=0.6)
                ln.set_clip_path(clip)


def structure_zone_model():
    fig, ax = schematic(6.8, 5.0, xlim=(-0.9, 11.2), ylim=(-1.6, 7.5))
    rng = np.random.default_rng(7)
    # oblique floor: x = Ts/Tm in [0,1] -> 0..8 ; depth s (log p, 0.1 Pa front .. 4 Pa back) -> offset
    X0, WX, DX, DY = 0.0, 8.0, 2.4, 2.2

    def P(t, s):
        return X0 + WX * t + DX * s, DY * s

    def s_of_p(p):
        return np.log10(p / 0.1) / np.log10(40)

    s = np.linspace(0, 1, 60)
    b1 = 0.12 + 0.13 * s       # zone 1 / T boundary (zone 1 widens at high pressure)
    bT = 0.40 - 0.08 * s       # zone T / 2 (T widens at low pressure)
    b2 = 0.50 + 0.0 * s        # zone 2 / 3
    zc = [("#F2C9B6", 0.0 * s, b1), ("#F7DFA8", b1, bT), ("#BFE3D3", bT, b2), ("#C6DCF0", b2, 1.0 + 0 * s)]
    for c, lo, hi in zc:
        pts = [P(t, ss) for t, ss in zip(lo, s)] + [P(t, ss) for t, ss in zip(hi[::-1], s[::-1])]
        ax.add_patch(Polygon(pts, closed=True, fc=c, ec="none"))
    for bnd in (b1, bT, b2):
        ax.plot(*zip(*[P(t, ss) for t, ss in zip(bnd, s)]), color=INK, lw=0.8)
    corners = [P(0, 0), P(1, 0), P(1, 1), P(0, 1), P(0, 0)]
    ax.plot(*zip(*corners), color=INK, lw=1.0)

    # axes ticks
    for t in np.arange(0, 1.01, 0.1):
        x, y = P(t, 0)
        ax.plot([x, x], [y, y - 0.12], color=INK, lw=0.8)
        ax.text(x, y - 0.2, f"{t:.1f}", ha="center", va="top", fontsize=8)
    ax.text(4.9, -1.4, r"homologous temperature $T_s/T_m$ →", ha="left", va="center", fontsize=9.5)
    for pval in [0.1, 0.3, 1, 4]:
        x, y = P(1, s_of_p(pval))
        ax.plot([x, x + 0.12], [y, y], color=INK, lw=0.8)
        ax.text(x + 0.2, y, f"{pval:g}", ha="left", va="center", fontsize=8)
    xa, ya = P(1, 0.5)
    ax.text(xa + 1.0, ya, "Ar pressure (Pa)\n(ion energy\ndecreases →)", ha="left", va="center",
            fontsize=8, rotation=0)

    # zone labels on floor
    for t, ss, z in [(0.08, 0.85, "1"), (0.33, 0.25, "T"), (0.45, 0.6, "2"), (0.75, 0.75, "3")]:
        x, y = P(t, ss)
        ax.text(x, y, z, ha="center", va="center", fontsize=12, weight="bold")

    # cross-section sketches above the floor
    w, h = 2.05, 1.9
    sk = [("1", "Zone 1: tapered,\nvoided columns", -0.6, (0.08, 0.85)),
          ("T", "Zone T: dense\nfibrous grains", 1.95, (0.33, 0.25)),
          ("2", "Zone 2: straight\ncolumns", 4.5, (0.45, 0.6)),
          ("3", "Zone 3: equiaxed,\nrecrystallized", 7.05, (0.75, 0.75))]
    ybase = 4.3
    for z, lab, xx, (t, ss) in sk:
        _zone_sketch(ax, z, xx, ybase, w, h, rng)
        ax.text(xx + w / 2, ybase + h + 0.12, lab, ha="center", va="bottom", fontsize=8)
        xf, yf = P(t, ss)
        ax.annotate("", xy=(xf, yf), xytext=(xx + w / 2, ybase - 0.3),
                    arrowprops=dict(arrowstyle="-|>", lw=0.7, color="0.35", shrinkA=0, shrinkB=9))

    # material annotations: markers on the front (low-pressure) edge, staggered labels below
    ann = [("EB-PVD YSZ at 1000 °C: 0.43", 0.43, -0.85), ("Al at 25 °C: 0.32", 0.32, -1.2),
           ("TiN at 450 °C: 0.23", 0.23, -1.55)]
    for nm, val, yl in ann:
        x0, y0 = P(val, 0.0)
        ax.plot(x0, y0 + 0.02, marker="v", color=VERM, ms=6, zorder=6)
        ax.plot([x0, x0], [-0.5, yl], color=VERM, lw=0.7)
        ax.text(x0 + 0.06, yl, nm, fontsize=7.5, color=VERM, ha="left", va="center")
    save(fig, "49", "fig-49-4-structure-zone-model")


if __name__ == "__main__":
    vacuum_regimes()
    cvd_grove_regimes()
    growth_modes()
    structure_zone_model()
