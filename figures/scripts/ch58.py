"""Figures for Chapter 58 — Materials Selection and Design.

Run from the repository root:  python figures/scripts/ch58.py
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, box, arrow, save, COLORS, INK  # noqa: E402,F401
import numpy as np  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Ellipse, Polygon  # noqa: E402
from scipy.spatial import ConvexHull  # noqa: E402

BLUE, VERM, GREEN, PINK, ORANGE, SKY = COLORS[:6]
L10 = np.log10
BROWN = "#8B5A2B"


def _log_ticks(ax, axis, lo, hi, labels=None):
    """Decade ticks for an axis drawn in log10 data units."""
    ticks = list(range(lo, hi + 1))
    if labels is None:
        labels = [f"{10.0 ** t:g}" for t in ticks]
    minor = [L10(m * 10.0 ** t) for t in range(lo - 1, hi + 1) for m in range(2, 10)]
    if axis == "x":
        ax.set_xticks(ticks)
        ax.set_xticklabels(labels)
        ax.set_xticks(minor, minor=True)
    else:
        ax.set_yticks(ticks)
        ax.set_yticklabels(labels)
        ax.set_yticks(minor, minor=True)


def _ellipse(ax, x0, x1, y0, y1, color, pad=0.08, alpha=0.2, lw=1.1, ls="-"):
    """Shaded ellipse spanning [x0,x1]x[y0,y1] (linear values), drawn in log10 data units."""
    xc, yc = (L10(x0) + L10(x1)) / 2, (L10(y0) + L10(y1)) / 2
    w, h = L10(x1) - L10(x0) + 2 * pad, L10(y1) - L10(y0) + 2 * pad
    ax.add_patch(Ellipse((xc, yc), w, h, fc=color, alpha=alpha, ec="none"))
    ax.add_patch(Ellipse((xc, yc), w, h, fc="none", ec=color, lw=lw, ls=ls))
    return xc, yc


def _hull(ax, pts, color, pad=0.08, alpha=0.18):
    """Shaded convex envelope (in log space) around log10 points, padded."""
    pts = np.asarray(pts)
    ang = np.linspace(0, 2 * np.pi, 32, endpoint=False)
    cloud = np.vstack([pts + pad * np.c_[np.full(len(pts), np.cos(a)), np.full(len(pts), np.sin(a))]
                       for a in ang])
    poly = cloud[ConvexHull(cloud).vertices]
    ax.add_patch(Polygon(poly, closed=True, fc=color, alpha=alpha, lw=0))
    ax.add_patch(Polygon(poly, closed=True, fc="none", ec=color, lw=1.1))


# ---------------------------------------------------------------- Figure 58.1
def selection_procedure():
    fig = plt.figure(figsize=(6.8, 4.2))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 17)
    ax.set_ylim(2.55, 12.95)
    ax.axis("off")

    # main flow
    mx, mw = 6.3, 6.4
    flow = [
        ("Design requirement", 0.75, "#F2F2F2"),
        ("Translation: function, objective,\nconstraints, free variables", 1.05, "#EEF3F8"),
        ("Screening: eliminate on property limits\n(e.g. $T_{\\max}$ ≥ 150 °C, $K_{IC}$ ≥ 15 MPa m$^{1/2}$,\n"
         "recyclable)", 1.45, "#DCEBF7"),
        ("Ranking: performance index $M$\n(e.g. $E^{1/2}/\\rho$) on charts", 1.05, "#DCEBF7"),
        ("Documentation: supplier data, failure\nhistory, corrosion, joining, cost\nstability, availability",
         1.45, "#DCEBF7"),
        ("Final choice + process route", 0.75, "#E3F1EA"),
    ]
    gap = 0.62
    y = 12.3
    centers = []
    for txt, h, fc in flow:
        y -= h
        box(ax, mx, y, mw, h, txt, fc=fc, fontsize=7.8)
        centers.append((y, h))
        y -= gap
    for (y0, h0), (y1, h1) in zip(centers[:-1], centers[1:]):
        arrow(ax, mx + mw / 2, y0, mx + mw / 2, y1 + h1)

    # side inputs (right)
    sx, sw = 13.15, 3.8
    yr, hr = centers[3]
    yd, hd = centers[4]
    box(ax, sx, yr + hr / 2 + 0.12, sw, 0.62, "Shape factors (48.5)", fc="white", fontsize=7.5)
    box(ax, sx, yr + hr / 2 - 0.74, sw, 0.62, "Exchange constants (48.4)", fc="white", fontsize=7.3)
    box(ax, sx, yd + hd / 2 - 0.45, sw, 0.9, "Process and cost\nmodel (48.6)", fc="white", fontsize=7.5)
    for yy in (yr + hr / 2 + 0.43, yr + hr / 2 - 0.43):
        arrow(ax, sx, yy, mx + mw, yr + hr / 2 + (0.18 if yy > yr + hr / 2 else -0.18), color="0.3")
    arrow(ax, sx, yd + hd / 2, mx + mw, yd + hd / 2, color="0.3")

    # funnel between left column and the main flow
    ys_top = centers[2][0] + centers[2][1]
    ys_bot = centers[4][0]
    fx, fw = 5.0, 1.6
    ax.add_patch(Polygon([(fx - fw / 2, ys_top), (fx + fw / 2, ys_top), (fx + 0.12, ys_bot + 0.35),
                          (fx - 0.12, ys_bot + 0.35)], closed=True, fc="#F7E3B5", ec="#C98A00", lw=1))
    ax.plot([fx, fx], [ys_bot + 0.35, ys_bot - 0.25], color="#C98A00", lw=2)
    marks = [(ys_top - 0.3, "10$^4$–10$^5$\nmaterials"), (centers[3][0] + centers[3][1] + 0.31, "~10$^2$"),
             (centers[4][0] + centers[4][1] + 0.31, "~5"), (ys_bot - 0.55, "1")]
    for yy, t in marks:
        ax.text(fx, yy, t, ha="center", va="center", fontsize=7.4, color="#8a5a00",
                bbox=dict(fc="white", ec="none", pad=0.6, alpha=0.85))

    # left column: design stages
    lx, lw_ = 0.15, 3.65
    stages = [("Conceptual design\n(all materials,\napproximate data)", centers[1], centers[2]),
              ("Embodiment design\n(few classes, more\nprecise data)", centers[3], centers[3]),
              ("Detail design\n(one grade, supplier\ndata, tests)", centers[4], centers[5])]
    fcs = ["#FBEBDD", "#F6DCC4", "#F0C9A6"]
    for (t, top, bot), fc in zip(stages, fcs):
        y_top = top[0] + top[1]
        y_bot = bot[0]
        box(ax, lx, y_bot, lw_, y_top - y_bot, t, fc=fc, fontsize=7.6)
    ax.text(lx + lw_ / 2, 12.75, "stage of design", ha="center", va="top", fontsize=8, color="0.3",
            style="italic")
    ax.text(mx + mw / 2, 12.75, "selection procedure", ha="center", va="top", fontsize=8, color="0.3",
            style="italic")
    save(fig, "58", "fig-58-1-selection-procedure")


# ---------------------------------------------------------------- Figure 58.2
def _rot(ax, slope):
    """On-screen angle (deg) of a line of given slope in data units."""
    p0 = ax.transData.transform((0, 0))
    p1 = ax.transData.transform((1, slope))
    return np.degrees(np.arctan2(p1[1] - p0[1], p1[0] - p0[0]))


def ashby_modulus_density():
    fig, ax = new_fig(6.8, 5.0)
    ax.set_xlim(-2, L10(30))
    ax.set_ylim(-4, 3.3)
    # envelopes from the plan
    c = _ellipse(ax, 0.02, 0.3, 1e-3, 0.3, ORANGE)
    ax.text(c[0] + 0.15, c[1] - 0.4, "foams", ha="center", va="center", fontsize=8.5, color="#9a6400")
    c = _ellipse(ax, 0.9, 1.5, 1e-3, 0.1, PINK)
    ax.text(c[0], c[1], "elasto-\nmers", ha="center", va="center", fontsize=8, color="#a0507f")
    c = _ellipse(ax, 0.9, 2.2, 0.2, 5, BLUE)
    ax.text(L10(1.4), L10(0.12), "polymers", ha="center", va="center", fontsize=8.5, color=BLUE)
    c = _ellipse(ax, 0.4, 0.9, 6, 20, BROWN)
    ax.text(L10(0.33), L10(14), "woods,\nalong grain", ha="right", va="center", fontsize=8, color=BROWN)
    c = _ellipse(ax, 0.4, 0.9, 0.3, 1.5, BROWN, ls="--", alpha=0.1)
    ax.text(L10(0.33), L10(0.5), "woods,\nacross grain", ha="right", va="center", fontsize=8, color=BROWN)
    for n, r, e, off in (("PP", 0.905, 1.3, (-0.04, 0, "right")), ("PMMA", 1.18, 3.0, (-0.04, 0.07, "right")),
                         ("PEEK", 1.30, 3.8, (0.04, 0.06, "left"))):
        ax.plot(L10(r), L10(e), "o", color=BLUE, ms=3.5)
        ax.text(L10(r) + off[0], L10(e) + off[1], n, fontsize=7, ha=off[2], va="center", color=BLUE)
    ax.plot(L10(0.5), L10(11), "o", color=BROWN, ms=3.5)
    ax.text(L10(0.5) + 0.04, L10(11) - 0.02, "softwood", fontsize=7, ha="left", va="top", color=BROWN)

    comps = {"GFRP": (1.85, 20), "CFRP QI": (1.55, 60), "CFRP UD": (1.6, 140)}
    _hull(ax, [[L10(r), L10(e)] for r, e in comps.values()], "#555555", pad=0.08, alpha=0.15)
    coff = {"GFRP": (-0.06, -0.02, "right"), "CFRP QI": (-0.06, 0.0, "right"), "CFRP UD": (-0.06, 0.03, "right")}
    for n, (r, e) in comps.items():
        ax.plot(L10(r), L10(e), "D", color="#333333", ms=3.5)
        dx, dy, ha = coff[n]
        ax.text(L10(r) + dx, L10(e) + dy, n, fontsize=7, ha=ha, va="center", color="#333333")
    ax.text(L10(0.95), L10(300), "composites", fontsize=8.5, color="#333333", ha="center", fontweight="bold")
    _ellipse(ax, 2.3, 2.5, 26, 34, "#7F7F7F", pad=0.035, alpha=0.3)
    ax.plot(L10(2.4), L10(30), "o", color="#555555", ms=3)
    ax.text(L10(2.55), L10(19), "concrete", fontsize=7.2, ha="left", va="center", color="#555555")

    metals = {"Mg": (1.77, 45), "Al": (2.70, 69), "Ti": (4.43, 114), "steels": (7.85, 210), "Cu": (8.9, 120),
              "W": (19.3, 410)}
    _hull(ax, [[L10(r), L10(e)] for r, e in metals.values()], VERM, pad=0.08)
    moff = {"Mg": (0.02, -0.13, "center"), "Al": (0.05, -0.1, "left"), "Ti": (0.0, 0.11, "center"),
            "steels": (0.05, 0.0, "left"), "Cu": (0.04, -0.11, "left"), "W": (-0.04, 0.11, "right")}
    for n, (r, e) in metals.items():
        ax.plot(L10(r), L10(e), "o", color=VERM, ms=4)
        dx, dy, ha = moff[n]
        ax.text(L10(r) + dx, L10(e) + dy, n, fontsize=7.3, ha=ha, va="center")
    ax.text(L10(12), L10(40), "metals", fontsize=9, color=VERM, ha="center", fontweight="bold")

    cer = {"Al$_2$O$_3$": (3.90, 370), "SiC": (3.2, 410), "Si$_3$N$_4$": (3.2, 310), "diamond": (3.5, 1000)}
    _hull(ax, [[L10(r), L10(e)] for r, e in cer.values()], GREEN, pad=0.07)
    ceoff = {"Al$_2$O$_3$": (0.06, -0.06, "left"), "SiC": (-0.06, 0.06, "right"),
             "Si$_3$N$_4$": (-0.06, -0.06, "right"), "diamond": (0.06, 0.0, "left")}
    for n, (r, e) in cer.items():
        ax.plot(L10(r), L10(e), "s", color=GREEN, ms=3.8)
        dx, dy, ha = ceoff[n]
        ax.text(L10(r) + dx, L10(e) + dy, n, fontsize=7.3, ha=ha, va="center")
    ax.text(L10(2.75), L10(1150), "technical ceramics", fontsize=8.5, color="#00704f", ha="right",
            fontweight="bold", va="center")

    # guideline families (fan from a common point at lower right)
    px, py = L10(2.0), -3.75
    for n, lab in ((1, r"$E/\rho$ (ties)"), (2, r"$E^{1/2}/\rho$ (beams)"), (3, r"$E^{1/3}/\rho$ (panels)")):
        x1 = px + 0.45
        ax.plot([px, x1], [py, py + n * (x1 - px)], ls="--", color="0.4", lw=0.9)
        ax.text(x1 + 0.03, py + n * (x1 - px), f"{n}: {lab}", fontsize=7.2, color="0.3", ha="left",
                va="center")
    ax.text(px + 0.47, py + 1.75, "guideline slopes", fontsize=7.2, color="0.3", ha="left", va="bottom",
            style="italic")

    # selection line through Al, slope 2
    cal = L10(69) - 2 * L10(2.70)
    xx = np.array([-2, L10(30)])
    ax.plot(xx, 2 * xx + cal, "-", color=PINK, lw=1.5)
    x0 = L10(0.25)
    ax.annotate("", xy=(x0 - 0.3, 2 * x0 + cal + 0.75), xytext=(x0, 2 * x0 + cal),
                arrowprops=dict(arrowstyle="-|>", color=PINK, lw=1.4, mutation_scale=12))
    ax.text(x0 - 0.5, 2 * x0 + cal + 0.8, "search region:\nbetter beams", fontsize=8, color="#a0507f",
            ha="center", va="bottom")
    xl = L10(0.0125)
    ax.text(xl, 2 * xl + cal + 0.12, r"$E^{1/2}/\rho$ = that of Al", fontsize=7.3, color="#a0507f",
            rotation=_rot(ax, 2), rotation_mode="anchor", ha="left", va="bottom")

    _log_ticks(ax, "x", -2, 1, ["0.01", "0.1", "1", "10"])
    _log_ticks(ax, "y", -4, 3, ["10$^{-4}$", "10$^{-3}$", "0.01", "0.1", "1", "10", "100", "1000"])
    ax.set_xlim(-2, L10(30))
    ax.set_ylim(-4, 3.3)
    ax.set_xlabel(r"density $\rho$ (Mg/m$^3$)")
    ax.set_ylabel("Young's modulus E (GPa)")
    save(fig, "58", "fig-58-2-ashby-modulus-density")


# ---------------------------------------------------------------- Figure 58.3
def pareto_bonnet():
    fig, ax = new_fig(6.4, 4.2)
    mats = {"steel": (5.65, 6.28), "Al 6xxx": (10.9, 3.12), "Mg alloy": (11.8, 2.37), "CFRP": (56.5, 1.88)}
    C = np.array([v[0] for v in mats.values()])
    m = np.array([v[1] for v in mats.values()])
    # dominated region: up and to the right of the staircase front
    stair_x = [C[0], C[0]]
    stair_y = [10, m[0]]
    for i in range(1, 4):
        stair_x += [C[i], C[i]]
        stair_y += [m[i - 1], m[i]]
    stair_x += [100]
    stair_y += [m[3]]
    poly = list(zip(stair_x, stair_y)) + [(100, 10)]
    ax.add_patch(Polygon(poly, closed=True, fc="0.85", ec="none", alpha=0.6, zorder=0))
    ax.plot(stair_x, stair_y, "-", color="0.35", lw=1.2, zorder=1)
    ax.text(40, 6.0, "dominated region", fontsize=8.5, color="0.35", ha="center")
    ax.text(3.3, 1.1, "unattainable with\nthese materials", fontsize=8, color="0.5", ha="left", va="bottom")

    # penalty lines Z = C + alpha m through the optimum for each alpha
    Cc = np.logspace(np.log10(3), 2, 400)
    for alpha, col, (xl, yl, ha) in ((0.5, GREEN, (7.6, 1.55, "right")), (5, BLUE, (16.5, 1.5, "left")),
                                     (500, VERM, (30, 1.96, "left"))):
        Z = C + alpha * m
        i = np.argmin(Z)
        mm = (Z[i] - Cc) / alpha
        ok = mm > 0
        ax.plot(Cc[ok], mm[ok], "--", color=col, lw=1.3, zorder=2)
        lab = rf"$\alpha$ = {alpha:g} USD/kg" + "\n" + f"(selects {list(mats)[i].split()[0]})"
        ax.text(xl, yl, lab, color=col, fontsize=7.6, ha=ha, va="bottom")
    for (n, (c, mm)), off in zip(mats.items(), [(6, 4), (-8, 8), (6, 5), (6, 5)]):
        ax.plot(c, mm, "o", color=INK, ms=6.5, zorder=4)
        ax.annotate(f"{n}\n({c:g} USD, {mm:g} kg)", (c, mm), xytext=off, textcoords="offset points",
                    ha="left" if off[0] > 0 else "right", va="bottom", fontsize=7.4)
    ax.annotate("on the front but never selected\nby a linear penalty (non-convex point)",
                xy=(11.2, 3.2), xytext=(14, 4.4), fontsize=7.6, ha="left", va="center",
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.8))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(3, 100)
    ax.set_ylim(1, 10)
    ax.set_xticks([3, 5, 10, 20, 50, 100])
    ax.set_xticklabels(["3", "5", "10", "20", "50", "100"])
    ax.set_yticks([1, 2, 3, 5, 10])
    ax.set_yticklabels(["1", "2", "3", "5", "10"])
    ax.set_xlabel("material cost of one panel (USD)")
    ax.set_ylabel("panel mass (kg)")
    save(fig, "58", "fig-58-3-pareto-bonnet")


# ---------------------------------------------------------------- Figure 58.4
def cost_batch_size():
    fig, ax = new_fig(6.4, 4.0)
    n = np.logspace(0, 6, 500)
    routes = [("laser sintering", 13.33, 0, GREEN), ("CNC machining", 8.61, 1500, ORANGE),
              ("injection moulding", 0.46, 30000, BLUE)]
    costs = []
    for name, a, Ct, col in routes:
        c = a + Ct / n
        costs.append(c)
        ax.plot(n, c, color=col, lw=1.5)
    env = np.min(costs, axis=0)
    ax.plot(n, env, color=INK, lw=4, alpha=0.25, solid_capstyle="round", zorder=0)
    n1 = 1500 / (13.33 - 8.61)
    n2 = (30000 - 1500) / (8.61 - 0.46)
    for nn in (n1, n2):
        ax.axvline(nn, ls=":", color="0.4", lw=1)
    ax.text(n1 * 0.88, 40, f"n ≈ {round(n1, -1):.0f}", rotation=90, ha="right", va="center", fontsize=7.8,
            color="0.3")
    ax.text(n2 * 0.88, 40, f"n ≈ {round(n2, -2):.0f}", rotation=90, ha="right", va="center", fontsize=7.8,
            color="0.3")
    ax.text(2e5, 15.5, "laser sintering\n(no tooling): 13.3", color=GREEN, fontsize=7.8, va="bottom", ha="center")
    ax.text(1.3, 45, "CNC machining\n(fixtures 1 500 USD)", color=ORANGE, fontsize=7.8, ha="left", va="top")
    ax.text(9, 5500, "injection moulding\n(mould 30 000 USD)", color=BLUE, fontsize=7.8, ha="left", va="center")
    ax.text(2e5, 8.61 * 0.85, "8.61", color=ORANGE, fontsize=7.8, va="top", ha="center")
    ax.text(3e5, 0.46 * 1.25, "0.46", color=BLUE, fontsize=7.8, va="bottom", ha="center")
    ax.text(1.5e3, 1.0, "cheapest route\n(lower envelope)", fontsize=7.8, color="0.25", ha="center", va="top")
    ax.annotate("", xy=(7.5e3, 4.1), xytext=(2.3e3, 1.1), arrowprops=dict(arrowstyle="-|>", color="0.35", lw=0.8))
    ax.text(1.2, 0.15, "← tooling-dominated (slope −1)", fontsize=7.8, color="0.3", ha="left")
    ax.text(9e5, 0.15, "material + time dominated →", fontsize=7.8, color="0.3", ha="right")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1, 1e6)
    ax.set_ylim(0.1, 1e4)
    ax.set_xlabel("batch size n")
    ax.set_ylabel("cost per part (USD)")
    save(fig, "58", "fig-58-4-cost-batch-size")


# ---------------------------------------------------------------- Figure 58.5
def toughness_strength_chart():
    fig, ax = new_fig(6.8, 5.0)
    ax.set_xlim(0, L10(3000))
    ax.set_ylim(-2, L10(300))
    c = _ellipse(ax, 0.1, 10, 0.01, 0.1, ORANGE)
    ax.text(L10(2.5), L10(0.03), "foams", ha="center", va="center", fontsize=8.5, color="#9a6400")
    c = _ellipse(ax, 20, 100, 0.5, 5, BLUE)
    ax.text(L10(30), L10(0.9), "polymers", ha="center", va="center", fontsize=8.3, color=BLUE)
    c = _ellipse(ax, 30, 100, 5, 15, BROWN)
    ax.text(L10(28), L10(13), "woods,\nalong grain", ha="right", va="center", fontsize=8, color=BROWN)
    c = _ellipse(ax, 20, 100, 0.3, 1.5, "#7F7F7F", alpha=0.15)
    ax.text(L10(9), L10(0.35), "concrete\nand stone", ha="center", va="center", fontsize=8, color="#555555")
    c = _ellipse(ax, 50, 100, 0.6, 1.0, SKY, pad=0.06)
    ax.text(L10(150), L10(0.45), "glasses", ha="left", va="center", fontsize=8, color="#2a7fb0")

    cer = {"Al$_2$O$_3$": (300, 3.5), "SiC": (400, 3.5), "Si$_3$N$_4$": (700, 6), "ZrO$_2$": (900, 8)}
    _hull(ax, [[L10(s), L10(k)] for s, k in cer.values()], GREEN, pad=0.08)
    cof = {"Al$_2$O$_3$": (-0.05, 0.0, "right", "center"), "SiC": (0.0, -0.1, "center", "top"),
           "Si$_3$N$_4$": (-0.04, 0.07, "right", "bottom"), "ZrO$_2$": (0.05, -0.05, "left", "top")}
    for nme, (s, k) in cer.items():
        ax.plot(L10(s), L10(k), "s", color=GREEN, ms=3.8)
        dx, dy, ha, va = cof[nme]
        ax.text(L10(s) + dx, L10(k) + dy, nme, fontsize=7.2, ha=ha, va=va)
    ax.text(L10(2200), L10(3.0), "technical\nceramics", fontsize=8.3, color="#00704f", ha="center",
            fontweight="bold", va="center")
    comps = {"GFRP": (250, 20), "CFRP": (600, 30)}
    _hull(ax, [[L10(s), L10(k)] for s, k in comps.values()], "#555555", pad=0.08, alpha=0.15)
    for nme, (s, k) in comps.items():
        ax.plot(L10(s), L10(k), "D", color="#333333", ms=3.5)
    ax.text(L10(250), L10(20) - 0.14, "GFRP", fontsize=7.2, ha="center", va="top")
    ax.text(L10(600), L10(30) - 0.14, "CFRP", fontsize=7.2, ha="center", va="top")

    c = _ellipse(ax, 100, 550, 20, 45, PINK, pad=0.07)
    ax.text(L10(88), L10(30), "Al alloys", ha="right", va="center", fontsize=8, color="#a0507f")
    ax.plot(L10(350), L10(30), "o", color="#a0507f", ms=4)
    ax.text(L10(350), L10(30) + 0.07, "2024-T3", fontsize=7, ha="center", va="bottom", color="#a0507f")
    c = _ellipse(ax, 500, 1100, 50, 100, SKY, pad=0.07, alpha=0.25)
    ax.text(L10(740), L10(108), "Ti alloys", ha="center", va="bottom", fontsize=8, color="#2a7fb0")
    c = _ellipse(ax, 250, 2000, 30, 200, VERM, pad=0.08, alpha=0.12)
    ax.text(L10(1400), L10(36), "steels", ha="center", va="center", fontsize=8.5, color=VERM,
            fontweight="bold")
    for nme, s, k, off in (("pressure-vessel steel", 350, 150, (-0.05, 0.06, "right")),
                           ("Q&T", 1000, 60, (0.05, -0.04, "left")),
                           ("maraging", 1800, 90, (0.05, -0.07, "left"))):
        ax.plot(L10(s), L10(k), "o", color=VERM, ms=4.5, zorder=5)
        ax.text(L10(s) + off[0], L10(k) + off[1], nme, fontsize=7.2, ha=off[2], va="center", color=VERM)

    # guideline key (lower right)
    px, py = L10(110), L10(0.012)
    for slope, lab in ((1, r"slope 1: $K_{IC}/\sigma_f$ = const (yield before break)"),
                       (0.5, r"slope ½: $K_{IC}^2/\sigma_f$ = const (leak before break)")):
        x1 = px + 0.55
        ax.plot([px, x1], [py, py + slope * (x1 - px)], "--", color="0.4", lw=0.9)
        ax.text(x1 + 0.05, py + slope * (x1 - px), lab, fontsize=7, color="0.3", ha="left", va="center")
    # leak-before-break line through K^2/sigma = 64 MPa m
    s = np.logspace(0, L10(3000), 50)
    k = np.sqrt(64.3 * s)
    ax.plot(L10(s), L10(k), "-", color=INK, lw=1.4)
    ax.text(L10(3.0), L10(np.sqrt(64.3 * 3.0)) + 0.08, r"$K_{IC}^2/\sigma_f$ = 64 MPa m", fontsize=7.6,
            ha="left", va="bottom", rotation=_rot(ax, 0.5), rotation_mode="anchor")
    x0 = L10(60)
    y0 = L10(np.sqrt(64.3 * 60))
    ax.annotate("", xy=(x0 - 0.35, y0 + 0.5), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.3, mutation_scale=12))
    ax.text(x0 - 0.38, y0 + 0.55, "safer vessels", fontsize=8, ha="right", va="bottom")

    ax.set_xlim(0, L10(3000))
    ax.set_ylim(-2, L10(300))
    _log_ticks(ax, "x", 0, 3, ["1", "10", "100", "1000"])
    _log_ticks(ax, "y", -2, 2, ["0.01", "0.1", "1", "10", "100"])
    ax.set_xlim(0, L10(3000))
    ax.set_ylim(-2, L10(300))
    ax.set_xlabel(r"strength $\sigma_f$ (MPa)")
    ax.set_ylabel(r"fracture toughness $K_{IC}$ (MPa m$^{1/2}$)")
    save(fig, "58", "fig-58-5-toughness-strength-chart")


if __name__ == "__main__":
    selection_procedure()
    ashby_modulus_density()
    pareto_bonnet()
    cost_batch_size()
    toughness_strength_chart()
