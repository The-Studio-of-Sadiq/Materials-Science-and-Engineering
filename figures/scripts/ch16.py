"""Figures for Chapter 16 — Non-Ferrous Alloys.

Run from the repository root:  python figures/scripts/ch16.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, FancyBboxPatch, Circle
from matplotlib.collections import LineCollection
from scipy.spatial import Voronoi

from figstyle import new_fig, save, COLORS, INK, arrow

RNG = np.random.default_rng(16)


# ---------------------------------------------------------------- 16.1
def fig_6061_ageing():
    """Yield strength of 6061 vs artificial ageing time at three temperatures."""
    fig, ax = new_fig(6.4, 3.9)
    t = np.logspace(-1, 3, 600)
    s_start = 145.0   # T4-like naturally aged start
    s_over = 95.0     # asymptote for heavily overaged material
    # (T label, peak time h, peak MPa, left width, right width, colour)
    cases = [("160 °C", 20.0, 285.0, 0.65, 1.70, COLORS[0]),
             ("175 °C", 8.0, 280.0, 0.62, 1.60, COLORS[2]),
             ("190 °C", 3.4, 265.0, 0.60, 1.50, COLORS[1])]
    for lab, tp, sp, wl, wr, c in cases:
        x = np.log10(t / tp)
        left = s_start + (sp - s_start) * np.exp(-x ** 2 / (2 * wl ** 2))
        right = s_over + (sp - s_over) * np.exp(-x ** 2 / (2 * wr ** 2))
        s = np.where(x < 0, left, right)
        ax.plot(t, s, color=c, label=lab)
        ax.plot(tp, sp, "o", color=c, ms=5)
    ax.annotate("peak ≈ 285 MPa, 20 h", xy=(20, 285), xytext=(80, 293), fontsize=8,
                color=COLORS[0], va="center",
                arrowprops=dict(arrowstyle="-", color=COLORS[0], lw=0.8))
    ax.annotate("peak ≈ 280 MPa, 8 h", xy=(8, 280), xytext=(1.5, 297), fontsize=8,
                color=COLORS[2], va="center", ha="center",
                arrowprops=dict(arrowstyle="-", color=COLORS[2], lw=0.8))
    ax.annotate("peak ≈ 265 MPa, 3.4 h", xy=(3.4, 265), xytext=(0.35, 268), fontsize=8,
                color=COLORS[1], ha="center",
                arrowprops=dict(arrowstyle="-", color=COLORS[1], lw=0.8))
    ax.axhline(276, ls="--", color="0.35", lw=1.0)
    ax.text(0.105, 278, "T6 design value 276 MPa", fontsize=7.8, color="0.3", va="bottom")
    ax.axhline(55, ls="--", color="0.35", lw=1.0)
    ax.text(0.105, 60, "O temper 55 MPa", fontsize=8, color="0.3", va="bottom")
    ax.text(0.105, s_start - 6, "start ≈ 145 MPa\n(T4-like, naturally aged)", fontsize=8,
            color="0.3", va="top")
    # regime labels
    ax.text(0.30, 228, "underaged\n(β″ small, sheared)", fontsize=8.5, ha="center", color=INK)
    ax.text(14, 232, "peak T6\n(β″ needles)", fontsize=8.5, ha="center", color=INK)
    ax.text(250, 112, "overaged\n(β′, β; Orowan bypass)", fontsize=8.5, ha="center", color=INK)
    ax.set_xscale("log")
    ax.set_xlim(0.1, 1000)
    ax.set_ylim(40, 305)
    ax.set_xlabel("Ageing time (h)")
    ax.set_ylabel("0.2 % yield strength (MPa)")
    ax.legend(title="Ageing at", loc="lower center", fontsize=8, title_fontsize=8,
              bbox_to_anchor=(0.45, 0.08), ncol=3)
    save(fig, "16", "fig-16-1-6061-ageing-curves")


# ---------------------------------------------------------------- 16.2
def fig_cu_zn():
    """Cu-rich Cu–Zn phase diagram plus strength/ductility of annealed α brass."""
    fig = plt.figure(figsize=(6.8, 4.0))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.75, 1], wspace=0.55)
    ax = fig.add_subplot(gs[0])
    # boundaries (wt% Zn, °C)
    liq_a = np.array([[0, 1085], [10, 1045], [20, 995], [30, 935], [37.5, 902]])
    sol_a = np.array([[0, 1085], [10, 1040], [20, 985], [28, 935], [32.5, 902]])
    liq_b = np.array([[37.5, 902], [44, 884], [50, 868]])
    sol_b = np.array([[36.8, 902], [44, 878], [50, 862]])
    a_solv = np.array([[32.5, 902], [35.0, 800], [37.2, 700], [38.4, 600], [39.0, 454],
                       [37.2, 380], [35.0, 300]])
    b_solv = np.array([[36.8, 902], [39.2, 800], [41.7, 700], [43.6, 600], [45.3, 454],
                       [46.0, 380], [46.4, 300]])

    def sm(p, n=60):
        x = np.interp(np.linspace(0, 1, n), np.linspace(0, 1, len(p)), p[:, 0])
        y = np.interp(np.linspace(0, 1, n), np.linspace(0, 1, len(p)), p[:, 1])
        return x, y
    for p in (liq_a, sol_a, liq_b, sol_b, a_solv, b_solv):
        ax.plot(*sm(p), color=INK, lw=1.3)
    ax.plot([32.5, 37.5], [902, 902], color=INK, lw=1.3)   # peritectic line
    # order–disorder line (β / β′)
    ax.plot([39.0, 45.3], [454, 454], color=INK, lw=1.0, ls="--")
    ax.plot([45.3, 50], [454, 468], color=INK, lw=1.0, ls="--")
    # light fill of the α field (solvus + solidus)
    ax_, ay_ = sm(a_solv[::-1])
    sx_, sy_ = sm(sol_a[::-1])
    ax.add_patch(Polygon(np.r_[[[0, 300]], np.c_[ax_, ay_], np.c_[sx_, sy_]], closed=True,
                         fc=COLORS[5], alpha=0.12, lw=0))
    kw = dict(fontsize=9.5, ha="center", va="center", color=INK)
    ax.text(14, 650, "α (FCC)", **kw)
    ax.text(41.5, 600, "α+β", fontsize=8.5, ha="center", va="center")
    ax.text(47.6, 720, "β\n(BCC)", **kw)
    ax.text(41.5, 340, "α + β′", **kw)
    ax.text(48.4, 380, "β′", **kw)
    ax.text(38, 1040, "L", **kw)
    ax.text(18, 1060, "α + L", fontsize=8, ha="center", color=INK)
    ax.annotate("β + L", xy=(46, 876), xytext=(46, 975), fontsize=8, ha="center",
                arrowprops=dict(arrowstyle="-", lw=0.7, color=INK))
    ax.text(29.3, 880, "903 °C", fontsize=7.5, color=INK, ha="right")
    ax.text(38.3, 440, "454 °C", fontsize=7.5, color=INK, ha="right", va="top")
    ax.text(49.8, 488, "468 °C", fontsize=7, color=INK, ha="right")
    ax.annotate("β ⇌ β′ order–disorder\n(dashed)", xy=(43, 455), xytext=(17, 505),
                fontsize=7.5, ha="center", va="center",
                arrowprops=dict(arrowstyle="-", lw=0.7, color=INK))
    for xz, lab in ((30, "C26000\ncartridge brass"), (40, "C28000\nMuntz metal")):
        ax.axvline(xz, color=COLORS[1], ls="--", lw=1.0)
    ax.text(29.5, 1095, "C26000\n(70/30)", fontsize=7.5, color=COLORS[1], ha="right", va="top")
    ax.text(40.5, 1095, "C28000\n(60/40)", fontsize=7.5, color=COLORS[1], ha="left", va="top")
    ax.set_xlim(0, 50)
    ax.set_ylim(300, 1100)
    ax.set_xlabel("Zn (wt%)")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("(a) Cu–Zn, copper-rich side", fontsize=9.5, loc="left")

    # (b) properties of annealed brass
    bx = fig.add_subplot(gs[1])
    z = np.linspace(0, 40, 200)
    uts = np.interp(z, [0, 10, 20, 30, 35, 40], [220, 265, 305, 340, 350, 365])
    el = np.interp(z, [0, 10, 20, 30, 35, 40], [45, 52, 59, 65, 57, 45])
    from scipy.ndimage import gaussian_filter1d
    uts = gaussian_filter1d(uts, 4, mode="nearest")
    el = gaussian_filter1d(el, 6, mode="nearest")
    bx.plot(z, uts, color=COLORS[0])
    bx.set_xlim(0, 40)
    bx.set_ylim(200, 380)
    bx.set_xlabel("Zn (wt%)")
    bx.set_ylabel("UTS (MPa)", color=COLORS[0])
    bx.tick_params(axis="y", colors=COLORS[0])
    bx2 = bx.twinx()
    bx2.spines["right"].set_visible(True)
    bx2.plot(z, el, color=COLORS[1], ls="-")
    bx2.set_ylim(40, 70)
    bx2.set_ylabel("Elongation (%)", color=COLORS[1])
    bx2.tick_params(axis="y", colors=COLORS[1])
    bx.text(31, 366, "UTS", color=COLORS[0], fontsize=8.5, ha="right")
    bx2.text(14, 46, "elongation", color=COLORS[1], fontsize=8.5)
    bx.axvline(30, color="0.6", ls=":", lw=1)
    bx.set_title("(b) annealed brass", fontsize=9.5, loc="left")
    save(fig, "16", "fig-16-2-cu-zn-diagram")


# ---------------------------------------------------------------- 16.3
def _clip_lines(ax, segs, poly_xy, color, lw):
    pg = Polygon(poly_xy, closed=True, fc="none", ec="none")
    ax.add_patch(pg)
    lc = LineCollection(segs, colors=color, linewidths=lw)
    ax.add_collection(lc)
    lc.set_clip_path(pg)


def _hatch_segs(cx, cy, ang, spacing, half):
    d = np.array([np.cos(ang), np.sin(ang)])
    nrm = np.array([-d[1], d[0]])
    segs = []
    for k in np.arange(-half, half + spacing, spacing):
        p = np.array([cx, cy]) + k * nrm
        segs.append([p - half * d, p + half * d])
    return segs


def _voronoi_cells(pts, box):
    """Finite Voronoi polygons for pts (mirror trick), clipped implicitly by box."""
    x0, x1, y0, y1 = box
    mir = [pts,
           np.c_[2 * x0 - pts[:, 0], pts[:, 1]], np.c_[2 * x1 - pts[:, 0], pts[:, 1]],
           np.c_[pts[:, 0], 2 * y0 - pts[:, 1]], np.c_[pts[:, 0], 2 * y1 - pts[:, 1]]]
    allp = np.vstack(mir)
    vor = Voronoi(allp)
    cells = []
    for i in range(len(pts)):
        reg = vor.regions[vor.point_region[i]]
        cells.append(vor.vertices[reg])
    return cells


def _order(poly):
    poly = np.asarray(poly, float)
    c = poly.mean(axis=0)
    return poly[np.argsort(np.arctan2(poly[:, 1] - c[1], poly[:, 0] - c[0]))]


def _clip_convex(subject, clip):
    """Sutherland–Hodgman: intersection of polygon subject with convex polygon clip (CCW)."""
    out = [tuple(p) for p in subject]
    n = len(clip)
    for i in range(n):
        a, b = clip[i], clip[(i + 1) % n]
        inp, out = out, []
        if not inp:
            break

        def inside(p):
            return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]) >= 0

        def cross(p, q):
            x1, y1, x2, y2 = p[0], p[1], q[0], q[1]
            x3, y3, x4, y4 = a[0], a[1], b[0], b[1]
            den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
            return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
        for j in range(len(inp)):
            p, q = inp[j - 1], inp[j]
            if inside(q):
                if not inside(p):
                    out.append(cross(p, q))
                out.append(q)
            elif inside(p):
                out.append(cross(p, q))
    return np.array(out)


def _micro_axes(ax, w, title):
    ax.set_xlim(0, w)
    ax.set_ylim(0, w)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(True)
        s.set_color(INK)
        s.set_linewidth(0.8)
    ax.set_facecolor("#F4F1EA")
    ax.set_title(title, fontsize=8, loc="left", pad=3)


def _scale_bar(ax, w, length=50):
    x0 = w * 0.06
    y0 = w * 0.07
    ax.add_patch(Rectangle((x0 - w * 0.02, y0 - w * 0.03), length + w * 0.04, w * 0.13,
                           fc="white", ec="none", alpha=0.9, zorder=5))
    ax.plot([x0, x0 + length], [y0, y0], color="k", lw=2.2, zorder=6, solid_capstyle="butt")
    ax.text(x0 + length / 2, y0 + w * 0.015, f"{length} μm", fontsize=7, ha="center",
            va="bottom", zorder=6)


def fig_ti64():
    """Pseudo-binary Ti-6Al-xV section and the three classic microstructures."""
    fig = plt.figure(figsize=(6.8, 5.0))
    ax = fig.add_axes([0.09, 0.10, 0.54, 0.82])
    v = np.linspace(0, 15, 200)
    transus = 1045 - 11.0 * v - 0.6 * v ** 2
    ax.fill_between(v, transus, 1100, color=COLORS[5], alpha=0.15, lw=0)
    ax.plot(v, transus, color=INK, lw=1.6)
    # α / (α+β) boundary near the Ti-6Al axis
    va = np.linspace(0, 1.6, 50)
    ta = 1000 - 400 * (va / 1.6) ** 0.7
    ax.plot(va, ta, color=INK, lw=1.2)
    ms = 880 - 20 * v
    ax.plot(v, ms, color=INK, lw=1.0, ls="--")
    ax.text(12.4, 640, "$M_s$", fontsize=9)
    ax.text(11.5, 1050, "β", fontsize=12, ha="center")
    ax.text(10.5, 760, "α + β", fontsize=11, ha="center")
    ax.text(0.5, 640, "α", fontsize=10, ha="center")
    ax.text(13.6, 835, "β transus", fontsize=8.5, rotation=-37, ha="center")
    ax.axvline(4, color=COLORS[1], ls="--", lw=1.1)
    ax.text(4.2, 608, "Ti-6Al-4V", color=COLORS[1], fontsize=8.5)
    ax.plot(4, 995, "o", color=INK, ms=4)
    ax.annotate("transus ≈ 995 °C", xy=(4, 995), xytext=(5.0, 1010), fontsize=8,
                arrowprops=dict(arrowstyle="-", lw=0.7))
    # processing steps
    steps = [(1050, "(a) 1050 °C, β anneal,\n     slow cool → lamellar", COLORS[0], 1065),
             (950, "(b) work 930 °C, recrystallize 950 °C", COLORS[2], 950),
             (900, "(c) work + anneal 900 °C\n     → equiaxed (mill anneal)", COLORS[3], 880),
             (700, "(b) then age 700 °C → bimodal", COLORS[2], 700)]
    for T, lab, c, ty in steps:
        ax.plot(4, T, "s", color=c, ms=6, zorder=5)
        ax.annotate(lab, xy=(4, T), xytext=(5.0, ty), fontsize=7.6, color=c, va="center",
                    arrowprops=dict(arrowstyle="-|>", lw=0.9, color=c, shrinkA=0, shrinkB=4,
                                    mutation_scale=8),
                    bbox=dict(fc="white", ec="none", alpha=0.85, pad=0.5))
    ax.plot(4, 930, "s", color=COLORS[2], ms=4.5, zorder=5)
    ax.set_xlim(0, 15)
    ax.set_ylim(600, 1100)
    ax.set_xlabel("β-stabilizer content, V (wt%)  [6 wt% Al]")
    ax.set_ylabel("Temperature (°C)")

    # micrographs
    h = 0.255
    pos = [0.71, 0.66, h * 0.98, h], [0.71, 0.365, h * 0.98, h], [0.71, 0.07, h * 0.98, h]
    # (a) lamellar: 300 μm field, prior-β grains ~500 μm
    m1 = fig.add_axes(pos[0])
    W = 300.0
    _micro_axes(m1, W, "(a) lamellar (β-annealed)")
    gseeds = np.array([[-150, 120], [260, 380], [330, -40], [120, 500]])
    gcells = _voronoi_cells(np.vstack([gseeds, [[-500, -500], [800, 800], [-500, 800], [800, -500]]]),
                            (-1500, 1800, -1500, 1800))[:4]
    for gc in gcells:
        # colonies inside each prior-β grain: colony cells intersected with the grain
        cseeds = RNG.uniform(-100, 400, size=(45, 2))
        ccells = _voronoi_cells(cseeds, (-300, 700, -300, 700))
        for cs, cc in zip(cseeds, ccells):
            inter = _clip_convex(_order(cc), _order(gc))
            if len(inter) < 3:
                continue
            segs = _hatch_segs(cs[0], cs[1], RNG.uniform(0, np.pi), 7.0, 200)
            _clip_lines(m1, segs, inter, "#6B5B45", 0.9)
        m1.add_patch(Polygon(gc, closed=True, fc="none", ec="#F4F1EA", lw=5, zorder=3))
        m1.add_patch(Polygon(gc, closed=True, fc="none", ec="#3A2E20", lw=0.8, zorder=4))
    m1.text(W * 0.97, W * 0.93, "grain-boundary α", fontsize=6.5, ha="right",
            bbox=dict(fc="white", ec="none", pad=0.6), zorder=6)
    _scale_bar(m1, W)

    # (b) bimodal: 100 μm field
    m2 = fig.add_axes(pos[1])
    W = 120.0
    _micro_axes(m2, W, "(b) bimodal")
    # transformed-β matrix as small lamellar colonies
    cseeds = RNG.uniform(-10, W + 10, size=(55, 2))
    ccells = _voronoi_cells(cseeds, (-40, W + 40, -40, W + 40))
    for cs, cc in zip(cseeds, ccells):
        segs = _hatch_segs(cs[0], cs[1], RNG.uniform(0, np.pi), 2.6, 40)
        _clip_lines(m2, segs, cc, "#6B5B45", 0.6)
    # ~30 % equiaxed primary α, ~15 μm
    n_alpha, placed = 0, []
    target = 0.30 * W * W
    area = 0.0
    tries = 0
    while area < target and tries < 3000:
        tries += 1
        c = RNG.uniform(5, W - 5, 2)
        r = RNG.uniform(6.0, 8.5)
        if all(np.hypot(*(c - p)) > r + q + 1.5 for p, q in placed):
            placed.append((c, r))
            area += np.pi * r * r
    for c, r in placed:
        k = 9
        th = np.linspace(0, 2 * np.pi, k, endpoint=False) + RNG.uniform(0, 1)
        rr = r * RNG.uniform(0.85, 1.1, k)
        m2.add_patch(Polygon(np.c_[c[0] + rr * np.cos(th), c[1] + rr * np.sin(th)],
                             closed=True, fc="#FBF8F1", ec="#3A2E20", lw=0.8, zorder=3))
    m2.text(W * 0.97, W * 0.93, "primary α ~15 μm", fontsize=6.5, ha="right",
            bbox=dict(fc="white", ec="none", pad=0.6), zorder=6)
    _scale_bar(m2, W)

    # (c) equiaxed: α ~10 μm with intergranular β
    m3 = fig.add_axes(pos[2])
    W = 120.0
    _micro_axes(m3, W, "(c) equiaxed (mill annealed)")
    m3.set_facecolor("#FBF8F1")
    g = np.mgrid[0:W + 12:10, 0:W + 12:10].reshape(2, -1).T.astype(float)
    g[:, 0] += (np.round(g[:, 1] / 10) % 2) * 5
    g += RNG.normal(0, 2.0, g.shape)
    cells = _voronoi_cells(g, (-20, W + 20, -20, W + 20))
    for cc in cells:
        m3.add_patch(Polygon(cc, closed=True, fc="none", ec="#3A2E20", lw=0.7))
    # β at triple points
    from scipy.spatial import Voronoi as V2
    vv = V2(g).vertices
    sel = vv[RNG.random(len(vv)) < 0.45]
    for p in sel:
        m3.add_patch(Circle(p, RNG.uniform(1.0, 1.8), fc="#3A2E20", ec="none"))
    m3.text(W * 0.97, W * 0.93, "α ~10 μm; dark: β", fontsize=6.5, ha="right",
            bbox=dict(fc="white", ec="none", pad=0.6), zorder=6)
    _scale_bar(m3, W)
    save(fig, "16", "fig-16-3-ti64-microstructures")


# ---------------------------------------------------------------- 16.4
def fig_turbine_history():
    """Metal temperature capability vs turbine entry temperature, 1940–2020."""
    fig, ax = new_fig(6.4, 4.0)
    pts = [(1945, 800, "wrought"), (1952, 840, None), (1960, 870, None),
           (1962, 905, "cast"), (1970, 950, None),
           (1975, 975, "DS"), (1982, 1000, "SX 1st gen"), (1990, 1030, "SX 2nd (3 % Re)"),
           (1995, 1060, "SX 3rd (6 % Re)"), (2005, 1090, "SX 4th/5th (Ru)")]
    yr = np.array([p[0] for p in pts], float)
    tm = np.array([p[1] for p in pts], float)
    cols = {"wrought": COLORS[0], "cast": COLORS[2], "DS": COLORS[4], "SX": COLORS[1]}

    def col(i):
        y = yr[i]
        return (cols["wrought"] if y <= 1960 else cols["cast"] if y <= 1970
                else cols["DS"] if y < 1980 else cols["SX"])
    yy = np.linspace(1945, 2015, 300)
    tm_line = np.interp(yy, np.r_[yr, 2015], np.r_[tm, 1100])
    from scipy.interpolate import PchipInterpolator
    tet = PchipInterpolator([1945, 1955, 1965, 1975, 1985, 1995, 2005, 2015],
                            [800, 870, 1000, 1180, 1340, 1480, 1580, 1650])(yy)
    ax.fill_between(yy, tm_line, tet, color=COLORS[5], alpha=0.18, lw=0)
    ax.plot(yy, tet, color=COLORS[1], lw=2.0)
    ax.plot(yy, tm_line, color="0.45", lw=1.0, ls="-")
    for i, (y, T, lab) in enumerate(pts):
        ax.plot(y, T, "o", color=col(i), ms=5.5, zorder=4, mec="white", mew=0.6)
    lab_pos = {"wrought": (1946, 760, "left"), "cast": (1964, 870, "left"),
               "DS": (1974, 935, "left"), "SX 1st gen": (1983, 960, "left"),
               "SX 2nd (3 % Re)": (1991, 990, "left"), "SX 3rd (6 % Re)": (1996, 1020, "left"),
               "SX 4th/5th (Ru)": (2006, 1050, "left")}
    for y, T, lab in pts:
        if lab:
            lx, ly, ha = lab_pos[lab]
            ax.text(lx, ly, lab, fontsize=7.5, ha=ha, va="center", color=INK)
    ax.text(1947, 715, "conventionally cast", fontsize=7.5, alpha=0)  # spacer
    ax.axhline(1455, ls=":", color=INK, lw=1.2)
    ax.text(1941, 1468, "melting point of Ni, 1455 °C", fontsize=8, va="bottom")
    ax.text(2014, 1690, "turbine entry\ntemperature", fontsize=8.5, color=COLORS[1],
            ha="right", va="bottom")
    ax.text(1997, 1260, "film cooling + TBC", fontsize=9.5, ha="center", color="#1B5E86",
            style="italic")
    ax.text(2019, 1120, "metal capability\n(1000 h rupture,\n137 MPa)", fontsize=7.8,
            ha="right", va="bottom", color="0.3")
    ax.set_xlim(1940, 2020)
    ax.set_ylim(700, 1800)
    ax.set_xlabel("Year of introduction")
    ax.set_ylabel("Temperature (°C)")
    save(fig, "16", "fig-16-4-turbine-temperature-history")


# ---------------------------------------------------------------- 16.5
def _airfoil(n=120):
    """Closed airfoil outline (cambered turbine-blade-like section), chord along x."""
    x = (1 - np.cos(np.linspace(0, np.pi, n))) / 2
    t = 0.30
    yt = 5 * t * (0.2969 * np.sqrt(x) - 0.1260 * x - 0.3516 * x ** 2 + 0.2843 * x ** 3
                  - 0.1036 * x ** 4)
    m, p = 0.16, 0.40
    yc = np.where(x < p, m / p ** 2 * (2 * p * x - x ** 2),
                  m / (1 - p) ** 2 * ((1 - 2 * p) + 2 * p * x - x ** 2))
    dyc = np.where(x < p, 2 * m / p ** 2 * (p - x), 2 * m / (1 - p) ** 2 * (p - x))
    th = np.arctan(dyc)
    xu, yu = x - yt * np.sin(th), yc + yt * np.cos(th)
    xl, yl = x + yt * np.sin(th), yc - yt * np.cos(th)
    return x, yc, yt, np.r_[xu, xl[::-1]], np.r_[yu, yl[::-1]]


def fig_blade_coating():
    """Cooled SX blade cross-section and TBC layer stack with temperature profile."""
    fig = plt.figure(figsize=(6.8, 4.4))
    # ---- left: blade cross-section
    ax = fig.add_axes([0.0, 0.05, 0.40, 0.88])
    ax.set_aspect("equal")
    ax.axis("off")
    x, yc, yt, X, Y = _airfoil()
    S = 4.0
    ax.add_patch(Polygon(np.c_[X * S, Y * S], closed=True, fc="#C9CED6", ec=INK, lw=1.2))
    ax.add_patch(Polygon(np.c_[X * S, Y * S], closed=True, fc="none", ec=COLORS[4], lw=3.2,
                         alpha=0.9))
    # cooling passages
    for xc in (0.10, 0.25, 0.42, 0.60, 0.76):
        yci = np.interp(xc, x, yc) * S
        ti = np.interp(xc, x, yt) * S
        hh = max(ti * 1.25, 0.10)
        ww = 0.42 if xc > 0.1 else 0.30
        ax.add_patch(FancyBboxPatch((xc * S - ww / 2, yci - hh / 2), ww, hh,
                                    boxstyle="round,pad=0,rounding_size=0.08",
                                    fc="#E8F2FA", ec=INK, lw=0.8))
    # film-cooling holes (leading edge and pressure side)
    for xc, side in ((0.03, 1), (0.03, -1), (0.12, -1), (0.30, -1), (0.48, -1), (0.20, 1)):
        yci = np.interp(xc, x, yc) * S
        ti = np.interp(xc, x, yt) * S
        y_in = yci + side * ti * 0.55
        y_out = yci + side * (ti * 1.0 + 0.02)
        ax.annotate("", xy=(xc * S + 0.18, y_out + side * 0.18), xytext=(xc * S, y_in),
                    arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=0.9,
                                    mutation_scale=6, shrinkA=0, shrinkB=0))
    ax.set_xlim(-0.7, 4.3)
    ax.set_ylim(-1.7, 2.5)
    ax.text(-0.65, 2.45, "(a) cooled single-crystal blade", fontsize=9, va="top")
    ax.text(-0.65, 1.85, "hot gas ≈ 1500 °C", fontsize=8.5, color=COLORS[1], ha="left")
    for yy in (1.55, 1.30):
        ax.annotate("", xy=(0.9, yy), xytext=(-0.6, yy),
                    arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.0, mutation_scale=8))
    ax.annotate("cooling air ≈ 650 °C\n(internal passages)", xy=(2.4, 0.45), xytext=(2.7, -1.25),
                fontsize=8, color=COLORS[0], ha="center",
                arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[0]))
    ax.annotate("film-cooling\nholes", xy=(0.55, -0.40), xytext=(-0.6, -1.25), fontsize=8,
                color=COLORS[0], ha="left",
                arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[0]))
    ax.annotate("TBC + bond coat", xy=(3.0, 0.72), xytext=(2.6, 1.6), fontsize=8,
                color="#A0700A", ha="left",
                arrowprops=dict(arrowstyle="-", lw=0.7, color="#A0700A"))
    xs_ = 0.50 * S
    ys_ = np.interp(xs_, X[:len(X) // 2] * S, Y[:len(Y) // 2] * S)
    ax.add_patch(Rectangle((xs_ - 0.16, ys_ - 0.2), 0.32, 0.30, fc="none", ec=INK, lw=0.8,
                           ls="--"))
    ax.text(xs_ - 0.2, ys_ + 0.16, "(b)", fontsize=7.5, ha="right")

    # ---- right: layer stack, depth vertical, gas on top
    bx = fig.add_axes([0.43, 0.12, 0.27, 0.74])
    layers = [(0.0, 4.0, "#F3E3B5"), (4.0, 4.35, "#7D7D7D"), (4.35, 6.0, "#B9C7D6"),
              (6.0, 10.0, "#D7DADF")]
    Tmin, Tmax = 900, 1300
    for d0, d1, c in layers:
        bx.add_patch(Rectangle((Tmin, d0), Tmax - Tmin, d1 - d0, fc=c, ec=INK, lw=0.6))
    for xc in np.linspace(Tmin + 12, Tmax - 12, 16):
        w = 9
        bx.add_patch(Polygon([[xc - w, 3.95], [xc + w, 3.95], [xc + w * 0.9, 0.35],
                              [xc, 0.05], [xc - w * 0.9, 0.35]], closed=True,
                             fc="#FBF1D2", ec="#B08A30", lw=0.5))
    for xc in np.arange(Tmin + 15, Tmax - 10, 26):
        for dc in np.arange(7.0, 9.9, 0.62):
            bx.add_patch(Rectangle((xc, dc), 19, 0.45, fc="#9AA2AE", ec="none"))
    dprof = [0.0, 4.0, 4.35, 6.0, 10.0]
    Tprof = [1250, 1050, 1045, 1030, 950]
    bx.plot(Tprof, dprof, color=COLORS[1], lw=2.4, zorder=6)
    bx.plot(Tprof, dprof, "o", color=COLORS[1], ms=4, zorder=6)
    for T, d, ha, dx in ((1250, 0.0, "right", -12), (1050, 4.0, "left", 12),
                         (1030, 6.0, "left", 12), (950, 10.0, "left", 12)):
        bx.text(T + dx, d + (0.35 if d < 9 else -0.4), f"{T} °C", fontsize=7.5,
                color=COLORS[1], ha=ha, va="center", zorder=7,
                bbox=dict(fc="white", ec="none", alpha=0.85, pad=0.3))
    bx.annotate("", xy=(1250, 2.0), xytext=(1050, 2.0),
                arrowprops=dict(arrowstyle="<|-|>", color=COLORS[1], lw=1.0, mutation_scale=8))
    bx.text(1150, 2.3, "ΔT ≈ 200 K", fontsize=8, ha="center", color=COLORS[1],
            bbox=dict(fc="white", ec="none", alpha=0.85, pad=0.3), zorder=7)
    bx.set_xlim(Tmin, Tmax)
    bx.set_ylim(10.0, -0.3)
    bx.set_yticks([])
    bx.spines["left"].set_visible(False)
    bx.xaxis.set_ticks_position("top")
    bx.xaxis.set_label_position("top")
    bx.spines["top"].set_visible(True)
    bx.spines["bottom"].set_visible(False)
    bx.set_xticks([900, 1000, 1100, 1200, 1300])
    bx.tick_params(labelsize=8)
    bx.set_xlabel("Temperature (°C)", fontsize=8.5)
    bx.text(Tmin, 10.3, "(b) coating stack, not to scale\n(hot gas above, cooling air below)",
            fontsize=8, va="top", ha="left")
    # labels on the right: black = layer, red = failure mode
    lx = 1320
    red = "#8B1A1A"
    rows = [(0.35, "CMAS infiltration (surface)", red),
            (1.7, "7YSZ TBC 150–250 μm\n(EB-PVD columns, k ≈ 1 W/m K)", INK),
            (3.25, "sintering of TBC\n(loss of strain tolerance)", red),
            (4.17, "TGO α-Al₂O₃ 1–10 μm: growth, spallation", None),
            (5.25, "bond coat 50–100 μm\n(Pt-aluminide or MCrAlY)", INK),
            (8.0, "SX superalloy wall 1–2 mm\nγ/γ′ cuboids ≈ 0.4 μm\n(magnified)", INK)]
    for d, lab, c in rows:
        if c is None:
            t = bx.text(lx, d, "TGO α-Al₂O₃ 1–10 μm: ", fontsize=7.2, va="center", ha="left",
                        clip_on=False)
            bx.annotate("growth, spallation", xycoords=t, xy=(1, 0.5), va="center",
                        ha="left", fontsize=7.2, color=red)
        else:
            bx.text(lx, d, lab, fontsize=7.2, va="center", ha="left", color=c, clip_on=False)
    save(fig, "16", "fig-16-5-blade-coating-stack")


# ---------------------------------------------------------------- 16.6
def fig_specific_strength():
    """Specific yield strength vs temperature for alloy families."""
    fig, ax = new_fig(6.6, 4.3)
    fams = [  # name, T points, lower, upper, colour, text position, leader target
        ("Mg alloys", [20, 100, 150, 200, 250], [110, 100, 85, 60, 35], [150, 135, 110, 80, 45],
         "#D4C200", (90, 45), (200, 68)),
        ("Al alloys|(7075-T6, 2618)", [20, 100, 150, 200, 250, 300],
         [150, 140, 125, 90, 55, 25], [185, 175, 155, 120, 75, 35], COLORS[0],
         (140, 16), (282, 38)),
        ("steels (4340,|maraging, Cr-Mo)", [20, 200, 300, 400, 500, 600],
         [120, 112, 105, 95, 75, 40], [230, 215, 200, 175, 130, 60], "0.40",
         (470, 25), (540, 75)),
        ("Ti alloys (Ti-6-4, near-α)", [20, 200, 300, 400, 500, 600],
         [190, 155, 140, 125, 110, 80], [215, 185, 170, 160, 145, 110], COLORS[3],
         (420, 245), (330, 165)),
        ("γ-TiAl", [20, 500, 750, 850, 950], [100, 100, 100, 75, 40], [120, 120, 118, 95, 55],
         COLORS[4], (690, 62), (720, 103)),
        ("Ni superalloys (718, SX cast)", [20, 400, 650, 750, 850, 900, 1000, 1100],
         [105, 105, 108, 112, 100, 88, 60, 25], [130, 122, 115, 118, 108, 95, 68, 35],
         COLORS[2], (900, 160), (820, 112)),
        ("refractory (C103, TZM, W)", [1000, 1100, 1200, 1300, 1400], [25, 22, 20, 18, 15],
         [60, 52, 45, 38, 32], COLORS[7], (1200, 85), (1200, 40)),
    ]
    for name, T, lo, hi, c, (lx, ly), (tx, ty) in fams:
        Tg = np.linspace(T[0], T[-1], 120)
        l = np.interp(Tg, T, lo)
        h = np.interp(Tg, T, hi)
        ax.fill_between(Tg, l, h, color=c, alpha=0.28, lw=0)
        ax.plot(Tg, l, color=c, lw=0.9)
        ax.plot(Tg, h, color=c, lw=0.9)
        ax.annotate(name.replace("|", chr(10)), xy=(tx, ty), xytext=(lx, ly), fontsize=7.8, ha="center", va="center",
                    color=INK, arrowprops=dict(arrowstyle="-", lw=0.7, color=c,
                                               shrinkA=2, shrinkB=0))
    for v in (199, 179, 178):
        ax.plot(20, v, "o", color=INK, ms=3.5, zorder=5)
    ax.annotate("20 °C worked example:\nTi-6-4 199, 7075-T6 179,\n4340 178", xy=(22, 190),
                xytext=(80, 275), fontsize=7.5, va="center",
                arrowprops=dict(arrowstyle="-", lw=0.7))
    ax.set_xlim(0, 1400)
    ax.set_ylim(0, 300)
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Specific 0.2 % yield strength,\n$\\sigma_y/\\rho$  (MPa per Mg m$^{-3}$)")
    save(fig, "16", "fig-16-6-specific-strength-temperature")


if __name__ == "__main__":
    fig_6061_ageing()
    fig_cu_zn()
    fig_ti64()
    fig_turbine_history()
    fig_blade_coating()
    fig_specific_strength()
