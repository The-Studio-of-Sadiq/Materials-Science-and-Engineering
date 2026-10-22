"""Figures for Chapter 21 — Polymer Rheology, Mechanics and Processing.

Run from the repository root:  python figures/scripts/ch21.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle, Ellipse, FancyBboxPatch
from scipy.optimize import least_squares

from figstyle import new_fig, schematic, save, box, arrow, COLORS, INK


# ---------------------------------------------------------------- 21.1
def _cross(g, eta0, lam, n):
    return eta0 / (1 + (lam * g) ** (1 - n))


def flow_curves():
    fig, ax = new_fig(6.4, 4.2)
    g = np.logspace(-1, 5, 400)
    melts = [("HDPE, 190 °C", 2e4, 1.47, 0.40, COLORS[0]),
             ("PP, 230 °C", 3e3, (3e3 / 8000) ** (1 / 0.65), 0.35, COLORS[1]),
             ("PC, 300 °C", 600, 1e-3, 0.70, COLORS[2]),
             ("PET, 280 °C", 300, 5e-4, 0.60, COLORS[3])]
    for name, e0, lam, n, c in melts:
        eta = _cross(g, e0, lam, n)
        ax.loglog(g, eta, color=c, label=f"{name}: $\\eta_0$ = {e0:,.0f} Pa·s, $n$ = {n}")
    # PP power-law asymptote and die worked-example point
    gp = np.logspace(1, 4.5, 50)
    ax.loglog(gp, 8000 * gp ** (0.35 - 1), "--", color=COLORS[1], lw=1.0)
    ax.annotate("PP power law: slope $n-1$ = −0.65\n($K$ = 8000 Pa·s$^n$)", xy=(40, 8000 * 40 ** -0.65),
                xytext=(9e2, 2.6e3), fontsize=7.8, color=COLORS[1], va="center",
                arrowprops=dict(arrowstyle="-|>", lw=0.7, color=COLORS[1]))
    ax.plot(480, 145, "o", mfc="white", mec=COLORS[1], mew=1.5, ms=6, zorder=5)
    ax.annotate("sheet die: 480 s$^{-1}$, 145 Pa·s", xy=(480, 145), xytext=(1.5, 60), fontsize=8,
                arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK))
    bands = [(1, 10, "compression moulding"), (100, 1000, "extrusion"), (1e3, 1e5, "injection moulding")]
    for (a, b, lab), c in zip(bands, ["#9E9E9E", "#6E6E6E", "#3E3E3E"]):
        ax.axvspan(a, b, ymin=0, ymax=0.075, color=c, alpha=0.35, lw=0)
        ax.text(np.sqrt(a * b), 10 ** (1 + 0.0375 * 4), lab.replace("\n", " "), ha="center", va="center",
                fontsize=7.2)
    ax.set_xlim(0.1, 1e5)
    ax.set_ylim(10, 1e5)
    ax.set_xlabel("shear rate $\\dot\\gamma$ (s$^{-1}$)")
    ax.set_ylabel("shear viscosity $\\eta$ (Pa·s)")
    ax.legend(loc="upper right", fontsize=7.8)
    save(fig, "21", "fig-21-1-flow-curves")


# ---------------------------------------------------------------- 21.2
def viscosity_vs_m():
    fig, ax = new_fig(6.4, 4.2)
    Mc, etac = 3.5e4, 6.0
    M1 = np.logspace(3, np.log10(Mc), 50)
    M2 = np.logspace(np.log10(Mc), 6, 50)
    ax.loglog(M1, etac * M1 / Mc, color=COLORS[0], label="Rouse: $\\eta_0 \\propto M_w$")
    ax.loglog(M2, etac * (M2 / Mc) ** 3.4, color=COLORS[1], label="entangled: $\\eta_0 \\propto M_w^{3.4}$")
    ax.loglog(np.logspace(np.log10(Mc), 5, 10), etac * np.logspace(np.log10(Mc), 5, 10) / Mc, ":",
              color=COLORS[0], lw=1.0)
    rng = np.random.default_rng(4)
    Ms = np.array([2.5e3, 5e3, 1.0e4, 2.0e4, 3.7e4, 5.0e4, 1.1e5, 2.0e5, 4.0e5, 6.7e5, 9.0e5])
    model = np.where(Ms < Mc, etac * Ms / Mc, etac * (Ms / Mc) ** 3.4)
    data = model * 10 ** rng.normal(0, 0.12, len(Ms))
    ax.loglog(Ms, data, "o", mfc="white", mec=INK, mew=1.1, ms=5.5, label="narrow PS standards (representative)")
    ax.axvline(Mc, color="#888888", lw=0.8, ls="--")
    ax.text(Mc * 1.08, 2e6, "$M_c$ ≈ 35 000 g/mol", fontsize=8, color="#555555", va="bottom")
    # doubling annotation
    a, b = 2e5, 4e5
    ea, eb = etac * (a / Mc) ** 3.4, etac * (b / Mc) ** 3.4
    ax.plot([a, b], [ea, ea], color=INK, lw=0.8)
    ax.plot([b, b], [ea, eb], color=INK, lw=0.8)
    ax.text(b * 1.12, np.sqrt(ea * eb), "doubling $M_w$\n→ $\\eta_0$ × 10.6", fontsize=8, va="center")
    ax.text(2.0e3, 1.2, "slope 1", fontsize=8, color=COLORS[0], rotation=20)
    ax.text(1.0e5, 5.0e3, "slope 3.4", fontsize=8, color=COLORS[1], rotation=50)
    ax.set_xlim(1e3, 1e6)
    ax.set_ylim(1e-1, 1e7)
    ax.set_xlabel("weight-average molar mass $M_w$ (g/mol)")
    ax.set_ylabel("zero-shear viscosity $\\eta_0$ (Pa·s)\npolystyrene, 217 °C")
    ax.legend(loc="lower right", fontsize=8)
    # inset: tube model
    ins = ax.inset_axes([0.03, 0.50, 0.44, 0.42])
    ins.set_xlim(0, 10)
    ins.set_ylim(0, 5.2)
    ins.set_aspect("equal")
    ins.set_xticks([])
    ins.set_yticks([])
    for s in ins.spines.values():
        s.set_visible(True)
        s.set_color("#999999")
    ins.set_facecolor("white")
    t = np.linspace(0, 1, 300)
    xc = 0.8 + 8.4 * t
    yc = 2.6 + 1.0 * np.sin(2 * np.pi * 1.3 * t) + 0.25 * np.sin(2 * np.pi * 4 * t)
    dx, dy = np.gradient(xc), np.gradient(yc)
    nn = np.hypot(dx, dy)
    nx, ny = -dy / nn, dx / nn
    w = 0.55
    ins.plot(xc + w * nx, yc + w * ny, color="#AAAAAA", lw=0.8, ls="--")
    ins.plot(xc - w * nx, yc - w * ny, color="#AAAAAA", lw=0.8, ls="--")
    rngi = np.random.default_rng(2)
    obs = rngi.uniform([0.2, 0.3], [9.8, 4.9], size=(70, 2))
    keep = []
    for p in obs:
        dmin = np.min(np.hypot(xc - p[0], yc - p[1]))
        if dmin > w + 0.12:
            keep.append(p)
    keep = np.array(keep)
    ins.plot(keep[:, 0], keep[:, 1], "o", color="#777777", ms=2.5)
    wig = 0.15 * np.sin(2 * np.pi * 14 * t)
    ins.plot(xc + wig * nx, yc + wig * ny, color=COLORS[1], lw=2.0)
    ins.annotate("", xy=(xc[-1] + 0.6, yc[-1] + 0.3), xytext=(xc[-1] - 0.1, yc[-1]),
                 arrowprops=dict(arrowstyle="-|>", lw=1.2, color=INK, mutation_scale=8))
    ins.text(5.0, 4.95, "reptation along contour", fontsize=7, ha="center", va="top")
    ins.text(5.0, 0.15, "obstacles = neighbouring chains;\ntube diameter ≈ 5–8 nm", fontsize=6.6, ha="center",
             va="bottom")
    save(fig, "21", "fig-21-2-viscosity-vs-m")


# ---------------------------------------------------------------- 21.3
def pipe_regression():
    fig, ax = new_fig(6.4, 4.2)
    t50 = 50 * 8766.0
    t = np.logspace(0, 6, 200)
    s20 = 13 * t ** (np.log10(10 / 13) / np.log10(t50))
    ax.loglog(t, s20, color=COLORS[0], label="PE100, 20 °C (ductile)")
    t60 = np.logspace(0, 4.5, 100)
    ax.loglog(t60, 9.0 * t60 ** -0.026, color=COLORS[4], label="PE100, 60 °C (ductile)")
    t80 = np.logspace(0, 4, 100)
    k80 = np.log10(5 / 6.5) / 4
    ax.loglog(t80, 6.5 * t80 ** k80, color=COLORS[1], label="PE100, 80 °C: no knee")
    tk = 1000.0
    td = np.logspace(0, 3, 50)
    ax.loglog(td, 6.0 * td ** -0.03, color=COLORS[3], label="older unimodal PE, 80 °C")
    sk = 6.0 * tk ** -0.03
    tb = np.logspace(3, np.log10(tk * (sk / 2.1) ** 4), 50)
    ax.loglog(tb, sk * (tb / tk) ** -0.25, color=COLORS[3], ls="--")
    ax.plot(tk, sk, "o", color=COLORS[3], ms=5)
    ax.text(tk * 0.7, sk * 0.83, "knee", fontsize=8, color=COLORS[3], ha="right")
    ax.axvline(t50, color="#888888", lw=0.9, ls="--")
    ax.text(t50 * 0.88, 2.2, "50 years\n4.38×10$^5$ h", fontsize=8, ha="right", va="bottom", color="#555555")
    ax.plot(t50, 10, "s", color=COLORS[0], ms=6)
    ax.annotate("MRS = 10 MPa", xy=(t50, 10), xytext=(2e4, 15.5), fontsize=8.5,
                arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK))
    ax.text(3, 12.6, "ductile ballooning", fontsize=8.5, color="#333333", style="italic")
    ax.annotate("slow crack growth (brittle),\nslope ≈ −0.25", xy=(6e3, sk * (6e3 / tk) ** -0.25),
                xytext=(2e1, 2.25), fontsize=8.5, color=COLORS[3],
                arrowprops=dict(arrowstyle="-|>", lw=0.8, color=COLORS[3]))
    ax.set_xlim(1, 1e6)
    ax.set_ylim(2, 20)
    ax.set_yticks([2, 3, 4, 5, 6, 8, 10, 15, 20])
    ax.set_yticklabels(["2", "3", "4", "5", "6", "8", "10", "15", "20"])
    ax.set_xlabel("time to failure (h)")
    ax.set_ylabel("hoop stress (MPa)")
    ax.legend(loc="lower left", fontsize=8, bbox_to_anchor=(0.0, 0.08))
    save(fig, "21", "fig-21-3-pipe-regression")


# ---------------------------------------------------------------- 21.4
def _pc_curve(e):
    e = np.asarray(e, float)
    s = np.empty_like(e)
    up = e <= 6
    s[up] = 62 * (1 - (1 - e[up] / 6) ** 2.2)
    d = (e > 6) & (e <= 12)
    s[d] = 52 + 10 * (0.5 + 0.5 * np.cos(np.pi * (e[d] - 6) / 6))
    p = (e > 12) & (e <= 100)
    s[p] = 52 + 0.01 * (e[p] - 12)
    h = e > 100
    s[h] = 52.9 + 12.1 * ((e[h] - 100) / 20) ** 2
    return s


def _pp_curve(e):
    e = np.asarray(e, float)
    s = np.where(e <= 10, 33 * (1 - (1 - e / 10) ** 2), 33 - 4 * (1 - np.exp(-(e - 10) / 12)))
    return s


def _specimen(ax, x, y, w, h, neck=None, label=""):
    """Dog-bone outline; neck=(start, end) fraction of gauge length that is drawn (thinner)."""
    gw = 0.45 * h
    pts_top, pts_bot = [], []
    xs = np.linspace(0, 1, 120)
    for u in xs:
        if u < 0.15 or u > 0.85:
            half = h / 2
        elif u < 0.2:
            half = h / 2 - (h / 2 - gw / 2) * (u - 0.15) / 0.05
        elif u > 0.8:
            half = gw / 2 + (h / 2 - gw / 2) * (u - 0.8) / 0.05
        else:
            half = gw / 2
            if neck is not None:
                a, b = neck
                ua = 0.2 + 0.6 * a
                ub = 0.2 + 0.6 * b
                tr = 0.025
                if ua <= u <= ub:
                    half = gw / 4
                elif ua - tr < u < ua:
                    half = gw / 2 - (gw / 4) * (u - (ua - tr)) / tr
                elif ub < u < ub + tr:
                    half = gw / 4 + (gw / 4) * (u - ub) / tr
        pts_top.append((x + u * w, y + half))
        pts_bot.append((x + u * w, y - half))
    poly = pts_top + pts_bot[::-1]
    ax.add_patch(Polygon(poly, closed=True, fc="#EAF1F8", ec=INK, lw=0.8))
    if label:
        ax.text(x + w / 2, y - h / 2 - 0.02, label, ha="center", va="top", fontsize=6.8)


def yield_craze():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(6.8, 3.9), gridspec_kw=dict(width_ratios=[1.05, 1]))
    e = np.linspace(0, 120, 600)
    ax.plot(e, _pc_curve(e), color=COLORS[0], label="polycarbonate, 23 °C")
    ax.plot(120, _pc_curve([120])[0], "x", color=COLORS[0], ms=7, mew=2)
    ep = np.linspace(0, 150, 600)
    ax.plot(ep, _pp_curve(ep), color=COLORS[1], label="polypropylene")
    ax.annotate("", xy=(150, 29.2), xytext=(140, 29.2),
                arrowprops=dict(arrowstyle="-|>", lw=1.0, color=COLORS[1], mutation_scale=8))
    es = np.linspace(0, 2, 30)
    ax.plot(es, 22.5 * es, color=COLORS[3], label="polystyrene (brittle)")
    ax.plot(2, 45, "x", color=COLORS[3], ms=7, mew=2)
    ax.annotate("yield 62 MPa", xy=(6, 62), xytext=(14, 72), fontsize=7.8,
                arrowprops=dict(arrowstyle="-|>", lw=0.7, color=INK))
    ax.text(55, 54, "neck propagates (cold drawing)", fontsize=7.8, ha="center", va="bottom", color=COLORS[0])
    ax.text(118, 66, "strain\nhardening", fontsize=7.8, ha="right", va="bottom", color=COLORS[0])
    ax.text(5, 41, "PS: brittle at\n45 MPa, 2 %", fontsize=7.8, color=COLORS[3], va="center")
    ax.set_xlim(0, 150)
    ax.set_ylim(0, 80)
    ax.set_xlabel("engineering strain (%)")
    ax.set_ylabel("engineering stress (MPa)")
    ax.legend(loc="lower right", fontsize=7.8, bbox_to_anchor=(1.0, 0.0))
    ax.set_title("(a) yielding and cold drawing", fontsize=9.5)
    # specimen sketches (axes-fraction coordinates via inset)
    sk = ax.inset_axes([0.30, 0.38, 0.6, 0.25])
    sk.set_xlim(0, 3.4)
    sk.set_ylim(-0.12, 0.6)
    sk.axis("off")
    _specimen(sk, 0.0, 0.32, 0.95, 0.3, None, "elastic")
    _specimen(sk, 1.2, 0.32, 0.95, 0.3, (0.45, 0.55), "neck\nforms")
    _specimen(sk, 2.4, 0.32, 0.95, 0.3, (0.1, 0.9), "neck\npropagates")

    # (b) craze structure
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 8.6)
    ax2.set_aspect("equal")
    ax2.axis("off")
    ytop, ybot = 5.2, 2.8
    tipx = 8.2
    # bulk polymer
    ax2.add_patch(Rectangle((0.3, ytop), 9.4, 1.5, fc="#D9D9D9", ec="none"))
    ax2.add_patch(Rectangle((0.3, ybot - 1.5), 9.4, 1.5, fc="#D9D9D9", ec="none"))
    # craze region (wedge-shaped toward tip)
    xs = np.linspace(1.3, tipx, 200)
    open_ = (ytop - ybot) * np.sqrt(np.clip((tipx - xs) / (tipx - 1.3), 0, 1))
    top = (ytop + ybot) / 2 + open_ / 2
    bot = (ytop + ybot) / 2 - open_ / 2
    ax2.fill_between(xs, bot, top, color="white")
    ax2.fill_between([0.3, 1.3], [ybot, ybot], [ytop, ytop], color="white")
    ax2.plot(xs, top, color=INK, lw=0.8)
    ax2.plot(xs, bot, color=INK, lw=0.8)
    ax2.plot([0.3, 1.3], [ytop, ytop], color=INK, lw=0.8)
    ax2.plot([0.3, 1.3], [ybot, ybot], color=INK, lw=0.8)
    # fibrils
    for xf in np.arange(1.6, tipx - 0.15, 0.32):
        o = (ytop - ybot) * np.sqrt(max((tipx - xf) / (tipx - 1.3), 0))
        yt, yb = (ytop + ybot) / 2 + o / 2, (ytop + ybot) / 2 - o / 2
        ax2.plot([xf, xf], [yb, yt], color="#555555", lw=1.6)
    # broken fibrils / crack on the left
    for xf in np.arange(0.45, 1.3, 0.32):
        ax2.plot([xf, xf], [ytop - 0.35, ytop], color="#555555", lw=1.6)
        ax2.plot([xf, xf], [ybot, ybot + 0.35], color="#555555", lw=1.6)
    # meniscus fingers at the tip
    for k, yy in enumerate(np.linspace(3.75, 4.25, 3)):
        ax2.add_patch(Ellipse((tipx + 0.05, yy), 0.28, 0.14, fc="white", ec=INK, lw=0.6))
    # stress arrows
    for xx in (4.5, 7.0):
        ax2.annotate("", xy=(xx, 8.2), xytext=(xx, 6.9), arrowprops=dict(arrowstyle="-|>", lw=1.0, color=INK))
        ax2.annotate("", xy=(xx, 0.1), xytext=(xx, 1.1), arrowprops=dict(arrowstyle="-|>", lw=1.0, color=INK))
    ax2.text(9.6, 7.6, "$\\sigma$", fontsize=11, ha="right")
    ax2.text(5.0, 6.0, "bulk polymer", ha="center", fontsize=8)
    ax2.text(5.0, 1.8, "bulk polymer", ha="center", fontsize=8)
    ax2.annotate("fibrils 5–30 nm dia.,\nspacing 20–50 nm;\nvoids between", xy=(3.2, 4.0), xytext=(0.3, 0.45),
                 fontsize=7.3, va="bottom", arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
    ax2.annotate("craze tip:\nmeniscus\ninstability", xy=(tipx + 0.15, 4.0), xytext=(8.5, 1.3), fontsize=7.3,
                 ha="center", va="bottom", arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
    ax2.annotate("", xy=(1.8, ytop), xytext=(1.8, ybot),
                 arrowprops=dict(arrowstyle="<|-|>", lw=0.7, color=COLORS[0], mutation_scale=7))
    ax2.text(1.95, 3.55, "0.5–5 µm", fontsize=7, color=COLORS[0], rotation=90, va="center",
             bbox=dict(fc="white", ec="none", pad=0.5))
    ax2.annotate("craze → crack when\nfibrils break", xy=(0.8, 4.0), xytext=(0.3, 7.95), fontsize=7.3,
                 va="top", arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
    ax2.set_title("(b) craze cross-section", fontsize=9.5)
    fig.tight_layout()
    save(fig, "21", "fig-21-4-yield-craze")


# ---------------------------------------------------------------- 21.5
def _frame(ax, x, y, w, h, title):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc="#FAFAFA", ec="#999999", lw=0.8))
    ax.text(x + 0.15, y + h - 0.15, title, fontsize=7.8, weight="bold", va="top")


def processing_routes():
    fig, ax = schematic(6.8, 5.4, xlim=(0, 20), ylim=(0, 15.9))
    melt = "#E69F00"
    steel = "#B8C4CE"

    # ---------------- centre: single-screw extruder
    bx0, bx1, by = 3.2, 15.0, 7.6
    R = 0.75
    ax.add_patch(Rectangle((bx0, by - R), bx1 - bx0, 2 * R, fc=steel, ec=INK, lw=0.9))
    ax.add_patch(Rectangle((bx0, by - R + 0.18), bx1 - bx0, 2 * R - 0.36, fc="white", ec="none"))
    # hopper
    ax.add_patch(Polygon([(bx0 + 0.2, by + R + 1.2), (bx0 + 1.6, by + R + 1.2), (bx0 + 1.1, by + R),
                          (bx0 + 0.7, by + R)], closed=True, fc="#DDE6EE", ec=INK, lw=0.9))
    for k in range(6):
        ax.add_patch(Circle((bx0 + 0.55 + 0.17 * k, by + R + 0.95 - 0.05 * (k % 2)), 0.07, fc="#666666", ec="none"))
    ax.text(bx0 + 0.9, by + R + 1.35, "hopper (pellets)", fontsize=7, ha="center", va="bottom")
    # heater bands
    for xh in np.arange(bx0 + 2.4, bx1 - 0.6, 1.4):
        ax.add_patch(Rectangle((xh, by + R), 0.9, 0.2, fc="#C0392B", ec="none"))
        ax.add_patch(Rectangle((xh, by - R - 0.2), 0.9, 0.2, fc="#C0392B", ec="none"))
    ax.text(bx0 + 4.6, by + R + 0.28, "barrel heaters", fontsize=7, color="#C0392B", ha="center", va="bottom")
    # screw: root radius increases through compression zone
    Li = bx1 - bx0 - 0.3
    xf0, xf1, xc1 = bx0 + 0.2, bx0 + 0.2 + 0.4 * Li, bx0 + 0.2 + 0.7 * Li
    xs = np.linspace(xf0, bx1 - 0.1, 300)
    rmin, rmax = 0.22, 0.47
    root = np.where(xs < xf1, rmin, np.where(xs < xc1, rmin + (rmax - rmin) * (xs - xf1) / (xc1 - xf1), rmax))
    ax.fill_between(xs, by - root, by + root, color="#7F8C8D", lw=0)
    # melt fill in compression/metering zones
    ax.fill_between(xs[xs > xf1 + 0.8], (by + root)[xs > xf1 + 0.8], by + R - 0.18, color=melt, alpha=0.45, lw=0)
    ax.fill_between(xs[xs > xf1 + 0.8], by - R + 0.18, (by - root)[xs > xf1 + 0.8], color=melt, alpha=0.45, lw=0)
    for xfl in np.arange(xf0 + 0.15, bx1 - 0.2, 0.42):
        ax.plot([xfl, xfl + 0.18], [by - R + 0.2, by + R - 0.2], color="#4D5656", lw=1.1)
    for xz in (xf1, xc1):
        ax.plot([xz, xz], [by - R - 0.45, by + R + 0.05], color=INK, lw=0.6, ls=":")
    zones = [((xf0 + xf1) / 2, "feed\ndeep flights ($h$)"), ((xf1 + xc1) / 2, "compression\n$h$ → $h$/3"),
             ((xc1 + bx1) / 2, "metering\nshallow ($h$/3)")]
    for xz, lab in zones:
        ax.text(xz, by - R - 0.3, lab, ha="center", va="top", fontsize=7)
    ax.text(bx0 - 0.15, by, "drive", fontsize=7, ha="right", va="center")
    ax.text(bx0 + 8.6, by + R + 1.3, "single-screw extruder,  $L/D$ = 30", ha="center", va="bottom",
            fontsize=8.5, weight="bold")
    # die adapter / outlet
    ax.add_patch(Polygon([(bx1, by - R), (bx1 + 0.7, by - 0.3), (bx1 + 0.7, by + 0.3), (bx1, by + R)],
                         closed=True, fc=steel, ec=INK, lw=0.9))
    ox, oy = bx1 + 0.7, by
    ax.add_patch(Circle((ox, oy), 0.12, fc=melt, ec=INK, lw=0.6))

    # frames
    W, H = 6.35, 4.9
    fr = {"a": (0.15, 10.85), "d": (6.82, 10.85), "e": (13.5, 10.85),
          "b": (0.15, 0.1), "c": (6.82, 0.1), "f": (13.5, 0.1)}
    titles = {"a": "(a) pipe extrusion", "d": "(d) blown film", "e": "(e) melt spinning",
              "b": "(b) injection moulding", "c": "(c) blow moulding (EBM)", "f": "(f) thermoforming"}
    for k, (x, y) in fr.items():
        _frame(ax, x, y, W, H, titles[k])
    # distribution "bus" from the extruder outlet to every route
    gc = "#777777"
    xt, ytb, ybb = 16.45, 10.62, 5.22
    ax.plot([ox + 0.12, xt], [oy, oy], color=gc, lw=1.1)
    ax.plot([xt, xt], [ybb, ytb], color=gc, lw=1.1)
    ax.plot([3.3, 16.7], [ytb, ytb], color=gc, lw=1.1)
    ax.plot([3.3, 16.7], [ybb, ybb], color=gc, lw=1.1)
    for tx in (3.3, 10.0, 16.7):
        ax.annotate("", xy=(tx, 10.85), xytext=(tx, ytb), arrowprops=dict(arrowstyle="-|>", lw=1.1, color=gc,
                                                                         mutation_scale=9, shrinkA=0, shrinkB=0))
        ax.annotate("", xy=(tx, 5.0), xytext=(tx, ybb), arrowprops=dict(arrowstyle="-|>", lw=1.1, color=gc,
                                                                        mutation_scale=9, shrinkA=0, shrinkB=0))
    ax.text(xt + 0.15, oy + 0.15, "melt", fontsize=7, color=gc, va="bottom")

    # (a) pipe: die, vacuum calibrator, cooling bath, puller
    x0, y0 = fr["a"]
    yc = y0 + 2.2
    ax.add_patch(Rectangle((x0 + 0.3, yc - 0.75), 0.9, 1.5, fc=steel, ec=INK, lw=0.8))
    ax.add_patch(Rectangle((x0 + 1.2, yc - 0.45), 4.9, 0.9, fc=melt, ec=INK, lw=0.6, alpha=0.8))
    ax.add_patch(Rectangle((x0 + 1.2, yc - 0.2), 4.9, 0.4, fc="#FAFAFA", ec=INK, lw=0.4))
    ax.add_patch(Rectangle((x0 + 1.5, yc - 0.65), 1.2, 1.3, fill=False, ec=COLORS[0], lw=1.0, ls="--"))
    ax.add_patch(Rectangle((x0 + 3.0, yc - 0.9), 2.2, 1.8, fc="#D6EAF8", ec=COLORS[0], lw=0.8, alpha=0.7))
    ax.add_patch(Circle((x0 + 5.75, yc + 0.6), 0.18, fc="#666666"))
    ax.add_patch(Circle((x0 + 5.75, yc - 0.6), 0.18, fc="#666666"))
    ax.text(x0 + 0.75, yc - 0.85, "die", fontsize=6.8, ha="center", va="top")
    ax.text(x0 + 2.1, yc + 0.75, "vacuum\ncalibrator", fontsize=6.8, ha="center", va="bottom", color=COLORS[0])
    ax.text(x0 + 4.1, yc + 1.0, "cooling bath", fontsize=6.8, ha="center", va="bottom", color=COLORS[0])
    ax.text(x0 + 5.75, yc - 0.85, "puller", fontsize=6.8, ha="center", va="top")
    ax.text(x0 + 3.2, y0 + 0.25, "pipe, profile, cable insulation", fontsize=6.8, ha="center", va="bottom",
            style="italic")

    # (d) blown film
    x0, y0 = fr["d"]
    cx = x0 + 2.2
    ax.add_patch(Rectangle((cx - 0.8, y0 + 0.4), 1.6, 0.5, fc=steel, ec=INK, lw=0.8))
    ax.text(cx, y0 + 0.3, "annular die", fontsize=6.8, ha="center", va="top")
    yy = np.linspace(y0 + 0.9, y0 + 3.15, 60)
    s_ = (yy - yy[0]) / (yy[-1] - yy[0])
    rad = 0.45 + (1.12 - 0.45) * (1 - np.exp(-s_ / 0.25))
    ax.fill_betweenx(yy, cx - rad, cx + rad, color="#EAF2F8")
    ax.plot(cx - rad, yy, color=COLORS[0], lw=1.0)
    ax.plot(cx + rad, yy, color=COLORS[0], lw=1.0)
    ax.plot([cx - 1.12, cx - 0.1], [y0 + 3.15, y0 + 3.75], color=COLORS[0], lw=1.0)
    ax.plot([cx + 1.12, cx + 0.1], [y0 + 3.15, y0 + 3.75], color=COLORS[0], lw=1.0)
    ax.add_patch(Circle((cx - 0.17, y0 + 3.88), 0.15, fc="#666666"))
    ax.add_patch(Circle((cx + 0.17, y0 + 3.88), 0.15, fc="#666666"))
    ax.add_patch(Rectangle((cx - 1.15, y0 + 0.95), 0.4, 0.22, fc="#5DADE2", ec=INK, lw=0.5))
    ax.add_patch(Rectangle((cx + 0.75, y0 + 0.95), 0.4, 0.22, fc="#5DADE2", ec=INK, lw=0.5))
    ax.plot([cx - 1.2, cx + 1.2], [y0 + 1.9, y0 + 1.9], color="#999999", lw=0.6, ls=":")
    ax.text(cx + 1.3, y0 + 1.06, "air ring", fontsize=6.8, va="center")
    ax.text(cx + 1.3, y0 + 1.9, "frost line", fontsize=6.8, va="center", color="#777777")
    ax.text(cx + 0.45, y0 + 3.88, "nip rolls", fontsize=6.8, va="center")
    ax.text(x0 + 4.0, y0 + 2.85, "BUR = 2.5\nDDR = 19", fontsize=7.5, va="center", color=COLORS[1])

    # (e) melt spinning
    x0, y0 = fr["e"]
    cx = x0 + 2.4
    ax.add_patch(Rectangle((cx - 0.9, y0 + 3.9), 1.8, 0.35, fc=steel, ec=INK, lw=0.8))
    ax.text(cx + 1.0, y0 + 4.07, "spinneret", fontsize=6.8, va="center")
    for k in range(5):
        xk = cx - 0.6 + 0.3 * k
        ax.plot([xk, cx - 0.05 + 0.025 * k], [y0 + 3.9, y0 + 1.75], color=melt, lw=0.9)
    for yq in (y0 + 3.4, y0 + 2.9, y0 + 2.4):
        ax.annotate("", xy=(cx - 0.75, yq), xytext=(cx - 1.6, yq),
                    arrowprops=dict(arrowstyle="-|>", lw=0.8, color=COLORS[5], mutation_scale=7))
    ax.text(cx - 1.65, y0 + 2.2, "quench\nair", fontsize=6.8, ha="left", va="top", color=COLORS[0])
    ax.add_patch(Circle((cx + 0.05, y0 + 1.5), 0.28, fc="#BBBBBB", ec=INK, lw=0.7))
    ax.add_patch(Circle((cx + 1.0, y0 + 1.0), 0.28, fc="#BBBBBB", ec=INK, lw=0.7))
    ax.plot([cx + 0.3, cx + 0.8], [y0 + 1.4, y0 + 1.15], color=melt, lw=0.9)
    ax.text(cx + 0.5, y0 + 0.55, "godets", fontsize=6.8, ha="center", va="top")
    ax.add_patch(Rectangle((cx + 2.0, y0 + 0.45), 0.9, 0.7, fc="#DDE6EE", ec=INK, lw=0.7))
    ax.plot([cx + 1.25, cx + 2.0], [y0 + 0.9, y0 + 0.8], color=melt, lw=0.9)
    ax.text(cx + 2.45, y0 + 1.25, "take-up\n3000 m/min", fontsize=6.8, ha="center", va="bottom")

    # (b) injection moulding
    x0, y0 = fr["b"]
    yc = y0 + 2.75
    ax.add_patch(Rectangle((x0 + 0.3, yc - 0.45), 3.0, 0.9, fc=steel, ec=INK, lw=0.8))
    ax.add_patch(Rectangle((x0 + 0.5, yc - 0.18), 2.3, 0.36, fc="#7F8C8D", ec="none"))
    ax.add_patch(Rectangle((x0 + 2.8, yc - 0.25), 0.5, 0.5, fc=melt, ec="none", alpha=0.7))
    ax.add_patch(Polygon([(x0 + 3.3, yc - 0.45), (x0 + 3.65, yc - 0.12), (x0 + 3.65, yc + 0.12),
                          (x0 + 3.3, yc + 0.45)], closed=True, fc=steel, ec=INK, lw=0.8))
    ax.annotate("", xy=(x0 + 1.8, yc + 0.75), xytext=(x0 + 0.6, yc + 0.75),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, color=INK, mutation_scale=7))
    ax.text(x0 + 1.2, yc + 0.85, "reciprocating screw", fontsize=6.6, ha="center", va="bottom")
    ax.add_patch(Rectangle((x0 + 3.65, yc - 1.1), 0.9, 2.2, fc="#AEB6BF", ec=INK, lw=0.8))
    ax.add_patch(Rectangle((x0 + 4.55, yc - 1.1), 0.9, 2.2, fc="#AEB6BF", ec=INK, lw=0.8))
    ax.add_patch(Rectangle((x0 + 4.25, yc - 0.7), 0.6, 1.4, fc=melt, ec=INK, lw=0.5, alpha=0.8))
    ax.text(x0 + 4.55, yc + 1.2, "two-plate mould", fontsize=6.6, ha="center", va="bottom")
    ax.annotate("", xy=(x0 + 5.75, yc), xytext=(x0 + 6.15, yc),
                arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK, mutation_scale=7))
    ax.text(x0 + 5.95, yc - 0.2, "clamp", fontsize=6.4, ha="center", va="top")
    segs = [("fill 1 s", 1, "#F5B041"), ("pack 3 s", 3, "#EB984E"), ("cool 4–17 s", 10, "#5DADE2"),
            ("eject 2 s", 2, "#AAB7B8")]
    xb, scale = x0 + 0.3, 5.6 / 16
    for lab, d, c in segs:
        ax.add_patch(Rectangle((xb, y0 + 0.75), d * scale, 0.42, fc=c, ec=INK, lw=0.5))
        short = {"fill 1 s": "F", "pack 3 s": "P", "cool 4–17 s": "cool", "eject 2 s": "E"}[lab]
        ax.text(xb + d * scale / 2, y0 + 0.96, short, fontsize=6.3, ha="center", va="center")
        xb += d * scale
    ax.text(x0 + 0.3, y0 + 1.25, "cycle (PP, 2–4 mm wall)", fontsize=6.6, va="bottom")
    ax.text(x0 + 0.3, y0 + 0.65, "fill 1 s, pack 3 s, cool 4–17 s, eject 2 s", fontsize=6.3, va="top")

    # (c) extrusion blow moulding: three steps
    x0, y0 = fr["c"]
    for i, step in enumerate(["parison", "closing", "inflation"]):
        cx = x0 + 1.35 + 1.9 * i
        top = y0 + 4.0
        gap = 0.55 if i == 0 else 0.0
        for sgn in (-1, 1):
            xo = cx + sgn * (0.42 + gap / 2)
            ax.add_patch(Rectangle((xo - (0.5 if sgn < 0 else 0), y0 + 0.9), 0.5, 2.9, fc="#AEB6BF", ec=INK,
                                   lw=0.7))
        if i < 2:
            ax.add_patch(Rectangle((cx - 0.17, y0 + 1.2), 0.34, top - y0 - 1.2, fc=melt, ec=INK, lw=0.5,
                                   alpha=0.8))
        else:
            bottle = [(cx - 0.12, top), (cx - 0.12, y0 + 3.5), (cx - 0.4, y0 + 3.1), (cx - 0.4, y0 + 1.25),
                      (cx + 0.4, y0 + 1.25), (cx + 0.4, y0 + 3.1), (cx + 0.12, y0 + 3.5), (cx + 0.12, top)]
            ax.add_patch(Polygon(bottle, closed=True, fc=melt, ec=INK, lw=0.6, alpha=0.8))
            ax.annotate("", xy=(cx, y0 + 2.4), xytext=(cx, top + 0.25),
                        arrowprops=dict(arrowstyle="-|>", lw=0.8, color=COLORS[0], mutation_scale=7))
        if i == 1:
            ax.plot([cx - 0.3, cx + 0.3], [y0 + 1.2, y0 + 1.2], color=INK, lw=1.4)
        ax.text(cx, y0 + 0.75, step, fontsize=6.6, ha="center", va="top")
    ax.text(x0 + 5.4, y0 + 4.25, "air", fontsize=6.6, color=COLORS[0])

    # (f) thermoforming with plug assist over a female mould
    x0, y0 = fr["f"]
    cx = x0 + 3.1
    mould = [(cx - 2.2, y0 + 0.6), (cx + 2.2, y0 + 0.6), (cx + 2.2, y0 + 2.6), (cx + 1.3, y0 + 2.6),
             (cx + 1.05, y0 + 1.15), (cx - 1.05, y0 + 1.15), (cx - 1.3, y0 + 2.6), (cx - 2.2, y0 + 2.6)]
    ax.add_patch(Polygon(mould, closed=True, fc="#AEB6BF", ec=INK, lw=0.8))
    sheet_x = [cx - 2.4, cx - 1.3, cx - 0.75, cx + 0.75, cx + 1.3, cx + 2.4]
    sheet_y = [y0 + 2.75, y0 + 2.75, y0 + 1.75, y0 + 1.75, y0 + 2.75, y0 + 2.75]
    ax.plot(sheet_x, sheet_y, color=melt, lw=2.2)
    ax.add_patch(Rectangle((cx - 0.7, y0 + 1.85), 1.4, 1.2, fc="#D5D8DC", ec=INK, lw=0.7))
    ax.add_patch(Rectangle((cx - 0.12, y0 + 3.05), 0.24, 0.9, fc="#D5D8DC", ec=INK, lw=0.7))
    ax.text(cx + 0.25, y0 + 3.85, "plug assist", fontsize=6.6, va="center")
    for sgn in (-1, 1):
        ax.add_patch(Rectangle((cx + sgn * 2.4 - (0.5 if sgn < 0 else 0) + (0 if sgn < 0 else -0.0), y0 + 2.78),
                               0.5, 0.3, fc="#566573", ec=INK, lw=0.5))
    ax.text(cx - 2.6, y0 + 3.25, "clamp", fontsize=6.4, va="bottom")
    ax.annotate("", xy=(cx, y0 + 0.2), xytext=(cx, y0 + 1.1),
                arrowprops=dict(arrowstyle="-|>", lw=0.8, color=COLORS[0], mutation_scale=7))
    ax.text(cx + 0.15, y0 + 0.45, "vacuum", fontsize=6.6, color=COLORS[0], va="center")
    ax.text(cx - 2.95, y0 + 0.35, "female mould", fontsize=6.6, va="center")
    ax.text(cx + 3.1, y0 + 3.3, "heated sheet", fontsize=6.6, color="#B9770E", va="center", ha="right")
    save(fig, "21", "fig-21-5-processing-routes")


# ---------------------------------------------------------------- 21.6
def _rise(t, ti, tau, m):
    x = np.clip(t - ti, 0, None) / tau
    return 1 - np.exp(-x ** m)


def _soft(t, ML, M0=4.0, k=2.5):
    return (M0 - ML) * np.exp(-k * t)


def _conv(t, p):
    D, ti, tau, m, Dr, tr, taur = p
    rev = Dr * _rise(t, tr, taur, 2.0)
    return 2.0 + _soft(t, 2.0) + D * _rise(t, ti, tau, m) - rev


def cure_curve():
    # fit the conventional curve to the targets ts2 = 2.5 min, t90 = 7 min, MH = 16 at 12 min, 13.5 at 30 min
    def res(p):
        t = np.linspace(0, 30, 3001)
        M = _conv(t, p)
        imax = M.argmax()
        MH = M[imax]
        ML = M[(t > 0.5) & (t < 2.0)].min()
        ts2 = t[np.argmax(M > ML + 2.0)]
        t90 = t[np.argmax(M > ML + 0.9 * (MH - ML))]
        return [(MH - 16) * 2, (t[imax] - 12) / 2, (M[-1] - 13.5) * 2, (ts2 - 2.5) * 3, (t90 - 7.0) * 2,
                (ML - 2.0) * 3]

    p0 = [15.0, 1.4, 3.5, 1.5, 3.0, 8.0, 12.0]
    sol = least_squares(res, p0, bounds=([10, 0.5, 1, 1, 0, 2, 2], [22, 3, 10, 3, 8, 16, 40]))
    p = sol.x
    t = np.linspace(0, 30, 3001)
    M1 = _conv(t, p)
    MH = M1.max()
    ML = M1[(t > 0.5) & (t < 2.0)].min()
    ts2 = t[np.argmax(M1 > ML + 2.0)]
    t90 = t[np.argmax(M1 > ML + 0.9 * (MH - ML))]
    # EV system: ts2 = 3.5 min, plateau at 14, no reversion
    M2 = 2.0 + _soft(t, 2.0) + 12.0 * _rise(t, 2.25, 3.4, 1.7)
    # peroxide-cured EPDM: slow, marching modulus to 15 at 30 min
    M3 = 2.5 + _soft(t, 2.5, M0=4.2) + 9.6 * _rise(t, 1.0, 6.0, 1.2) + 0.1 * np.clip(t - 3, 0, None)
    fig, ax = new_fig(6.4, 4.0)
    ax.plot(t, M1, color=COLORS[0], label="NR, conventional sulfur system")
    ax.plot(t, M2, color=COLORS[2], label="NR, efficient vulcanization (EV) system")
    ax.plot(t, M3, color=COLORS[1], ls="--", label="EPDM, peroxide cure (marching modulus)")
    for x, lab in ((ts2, f"$t_{{s2}}$ ≈ {ts2:.1f} min"), (t90, f"$t_{{90}}$ ≈ {t90:.0f} min")):
        ax.axvline(x, color="#777777", ls="--", lw=0.8)
        ax.text(x + 0.25, 19.3, lab, fontsize=8, va="top")
    ax.axhline(MH, xmin=0, xmax=12 / 30, color=COLORS[0], lw=0.6, ls=":")
    ax.axhline(ML, xmin=0, xmax=3 / 30, color=COLORS[0], lw=0.6, ls=":")
    ax.text(0.2, MH + 0.25, f"$M_H$ = {MH:.0f} dN·m", fontsize=8, color=COLORS[0], va="bottom")
    ax.text(3.2, ML - 0.1, f"$M_L$ = {ML:.0f} dN·m", fontsize=8, color=COLORS[0], va="center")
    ax.text(ts2 / 2, 6.0, "scorch\nsafety", fontsize=8, ha="center", style="italic")
    ax.text(3.6, 12.5, "cure", fontsize=8.5, ha="center", style="italic")
    ax.annotate("reversion", xy=(24, M1[t >= 24][0]), xytext=(22.5, 17.3), fontsize=8.5, style="italic",
                ha="center", arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK))
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 20)
    ax.set_xlabel("time at 160 °C (min)")
    ax.set_ylabel("torque (dN·m)")
    ax.legend(loc="lower right", fontsize=8)
    print(f"  cure-curve fit: MH={MH:.2f}, ML={ML:.2f}, ts2={ts2:.2f}, t90={t90:.2f}, M(30)={M1[-1]:.2f}, "
          f"tmax={t[M1.argmax()]:.1f}; EV ts2={t[np.argmax(M2 > M2[(t > .5) & (t < 2)].min() + 2)]:.2f}, "
          f"EV MH={M2.max():.1f}; EPDM M(30)={M3[-1]:.1f}")
    save(fig, "21", "fig-21-6-cure-curve")


if __name__ == "__main__":
    flow_curves()
    viscosity_vs_m()
    pipe_regression()
    yield_craze()
    processing_routes()
    cure_curve()
