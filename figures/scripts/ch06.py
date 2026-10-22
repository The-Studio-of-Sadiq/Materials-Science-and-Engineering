"""Figures for Chapter 6 — Thermodynamics of Materials.

Run from the repository root:  python figures/scripts/ch06.py
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figstyle import COLORS, INK, new_fig, save  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Arc, FancyArrowPatch, Polygon, Rectangle  # noqa: E402
from scipy.ndimage import gaussian_filter  # noqa: E402
from scipy.optimize import brentq  # noqa: E402

GREY = "#9A9A9A"
R = 8.314


def _xlnx(x):
    x = np.clip(x, 1e-300, 1)
    return x * np.log(x)


def _gmix(x, w):
    """Regular-solution Delta G_mix / RT for Omega/RT = w."""
    return w * x * (1 - x) + _xlnx(x) + _xlnx(1 - x)


def _binodal(w):
    """Binodal composition (x < 0.5) of a symmetric regular solution, Omega/RT = w > 2."""
    f = lambda x: np.log(x / (1 - x)) + w * (1 - 2 * x)  # noqa: E731
    return brentq(f, 1e-12, 0.5 - 1e-9)


def _arr(ax, p0, p1, color=INK, lw=1.0, ms=8, style="-|>", z=5):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle=style, mutation_scale=ms, color=color, lw=lw,
                                 shrinkA=0, shrinkB=0, zorder=z))


# --------------------------------------------------------------------------- 6.1
def regular_solution_curves():
    fig = plt.figure(figsize=(6.8, 4.0))
    ax = fig.add_axes([0.09, 0.13, 0.58, 0.82])
    x = np.linspace(1e-6, 1 - 1e-6, 2001)
    cases = [(-2.0, COLORS[3], "Ω/RT = −2: ordering tendency"), (0.0, COLORS[0], "Ω/RT = 0: ideal"),
             (1.5, COLORS[2], "Ω/RT = 1.5"), (2.0, COLORS[4], "Ω/RT = 2: critical (flat bottom)"),
             (3.0, COLORS[1], "Ω/RT = 3: two minima")]
    for w, col, lab in cases:
        ax.plot(x, _gmix(x, w), color=col, lw=1.9, label=lab)
    # Omega/RT = 3 features
    xb = _binodal(3.0)
    gb = _gmix(xb, 3.0)
    ax.plot([0, 1], [gb, gb], color=COLORS[1], lw=1.0, ls="--")
    ax.plot([xb, 1 - xb], [gb, gb], "o", color=COLORS[1], ms=5, zorder=5)
    xs = 0.5 - 0.5 * np.sqrt(1 - 4 / (2 * 3.0))
    for xx in (xs, 1 - xs):
        ax.plot(xx, _gmix(xx, 3.0), "D", color=INK, ms=5, zorder=6)
    ax.annotate(f"minima x = {xb:.3f}, {1 - xb:.3f}\nΔG/RT = {gb:.3f}".replace("-", "−") + " (common tangent)", xy=(1 - xb, gb),
                xytext=(0.46, 0.30), fontsize=7.5, color=COLORS[1], va="top",
                arrowprops=dict(arrowstyle="-", color=COLORS[1], lw=0.7))
    ax.annotate(f"inflections (spinodal)\nx = {xs:.3f}, {1 - xs:.3f}", xy=(xs, _gmix(xs, 3.0)), xytext=(0.02, 0.20),
                fontsize=7.5, arrowprops=dict(arrowstyle="-", color=INK, lw=0.7))
    ax.text(0.5, _gmix(0.5, 3.0) + 0.02, f"+{_gmix(0.5, 3.0):.3f}", fontsize=7.5, ha="center", va="bottom",
            color=COLORS[1])
    ax.text(0.5, -np.log(2) + 0.02, "−ln 2 = −0.693", fontsize=7.5, ha="center", va="bottom", color=COLORS[0])
    ax.text(0.5, _gmix(0.5, -2.0) + 0.02, f"{_gmix(0.5, -2.0):.3f}", fontsize=7.5, ha="center", va="bottom",
            color=COLORS[3])
    ax.axhline(0, color=GREY, lw=0.6)
    ax.set_xlim(0, 1)
    ax.set_ylim(-1.25, 0.32)
    ax.set_xlabel(r"mole fraction $x_B$")
    ax.set_ylabel(r"$\Delta G_{\mathrm{mix}}/RT$")
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1.0), fontsize=7.8, handlelength=1.6)
    # side panel: enthalpy and entropy terms for Omega/RT = 3
    a2 = fig.add_axes([0.765, 0.13, 0.225, 0.40])
    a2.plot(x, 3.0 * x * (1 - x), color=COLORS[1], lw=1.4, ls="--", label=r"$\Delta H_{\mathrm{mix}}/RT$")
    a2.plot(x, _xlnx(x) + _xlnx(1 - x), color=COLORS[0], lw=1.4, ls=":", label=r"$-T\Delta S_{\mathrm{mix}}/RT$")
    a2.plot(x, _gmix(x, 3.0), color=INK, lw=1.4, label="sum")
    a2.axhline(0, color=GREY, lw=0.5)
    a2.set_xlim(0, 1)
    a2.set_ylim(-0.8, 0.85)
    a2.set_xticks([0, 0.5, 1])
    a2.tick_params(labelsize=7.5)
    a2.set_title("Ω/RT = 3, the two terms", fontsize=8)
    a2.legend(fontsize=6.6, loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=1, handlelength=1.5)
    save(fig, "06", "fig-6-1-regular-solution-curves")


# --------------------------------------------------------------------------- 6.2
def common_tangent():
    A, xa0, B = 3.0, 0.26, 6.0
    xa, xb = 0.30, 0.65
    m = 2 * A * (xa - xa0)
    xb0 = xb - m / (2 * B)
    Ga = lambda x: A * (x - xa0) ** 2  # noqa: E731
    cb = Ga(xa) + m * (xb - xa) - B * (xb - xb0) ** 2
    Gb = lambda x: B * (x - xb0) ** 2 + cb  # noqa: E731
    tang = lambda x: Ga(xa) + m * (x - xa)  # noqa: E731
    x0 = 0.45
    ymin, ymax = -0.21, 0.52
    fig, ax = new_fig(6.4, 4.6)
    xx = np.linspace(0.0, 0.60, 300)
    ax.plot(xx, Ga(xx), color=COLORS[0], lw=2.0)
    xx2 = np.linspace(0.36, 1.0, 300)
    ax.plot(xx2, Gb(xx2), color=COLORS[1], lw=2.0)
    ax.text(0.07, Ga(0.07) + 0.01, "α", color=COLORS[0], fontsize=13, ha="right")
    xbl = xb0 + np.sqrt((0.45 - cb) / B)
    ax.text(xbl + 0.02, 0.45, "β", color=COLORS[1], fontsize=13, ha="left")
    ax.plot([0, 1], [tang(0), tang(1)], color=INK, lw=1.2)
    ax.plot([xa, xb], [Ga(xa), Gb(xb)], "o", color=INK, ms=6, zorder=5)
    ax.plot(0, tang(0), "s", color=INK, ms=6, clip_on=False, zorder=6)
    ax.plot(1, tang(1), "s", color=INK, ms=6, clip_on=False, zorder=6)
    ax.text(0.015, tang(0) - 0.012, r"$\mu_A$ (intercept at $x_B$ = 0)", fontsize=9, va="top")
    ax.text(0.985, tang(1) + 0.015, r"$\mu_B$", fontsize=11, ha="right", va="bottom")
    for xv, lab in [(xa, r"$x_\alpha$ = 0.30"), (xb, r"$x_\beta$ = 0.65")]:
        ax.plot([xv, xv], [ymin, tang(xv)], color=GREY, lw=0.7, ls=":")
        ax.text(xv, ymin + 0.005, lab, fontsize=8.5, ha="center", va="bottom",
                bbox=dict(fc="white", ec="none", pad=0.5))
    # alloy x0
    ax.plot([x0, x0], [ymin + 0.06, Ga(x0)], color=COLORS[2], lw=1.0, ls="--")
    ax.plot(x0, Ga(x0), "o", color=COLORS[0], ms=5, zorder=5)
    ax.plot(x0, tang(x0), "o", color=INK, ms=5, zorder=5)
    _arr(ax, (x0 + 0.012, Ga(x0)), (x0 + 0.012, tang(x0)), color=COLORS[2], lw=1.2, ms=8, style="<|-|>")
    ax.text(x0 + 0.025, 0.5 * (Ga(x0) + tang(x0)) - 0.005, "energy gained\nby separating\ninto α + β",
            fontsize=7.8, color=COLORS[2], ha="left", va="center")
    # parallel tangent at x0 for nucleation driving force
    sl = 2 * A * (x0 - xa0)
    xn = xb0 + sl / (2 * B)
    pt = lambda x: Ga(x0) + sl * (x - x0)  # noqa: E731
    xp = np.linspace(0.38, xn + 0.03, 50)
    ax.plot(xp, pt(xp), color=COLORS[3], lw=1.1, ls="--")
    ax.plot(xn, Gb(xn), "o", color=COLORS[1], ms=5, zorder=5)
    _arr(ax, (xn, pt(xn)), (xn, Gb(xn)), color=COLORS[3], lw=1.3, ms=8, style="<|-|>")
    ax.annotate(r"$\Delta G_n$: driving force for nucleating β" + "\n(x ≈ %.2f) from supersaturated α (Ch 9)" % xn,
                xy=(xn - 0.005, 0.5 * (pt(xn) + Gb(xn))), xytext=(0.03, 0.50), fontsize=7.8, color=COLORS[3],
                ha="left", va="top", arrowprops=dict(arrowstyle="-", color=COLORS[3], lw=0.7))
    ax.text(0.47, pt(0.47) + 0.03, "tangent to α at $x_0$", fontsize=7.5, color=COLORS[3], ha="right",
            va="bottom")
    ax.text(0.80, tang(0.80) - 0.02, "common tangent", fontsize=7.5, color=INK, ha="left", va="top")
    # lever-rule bar
    yb = ymin + 0.075
    fb = (x0 - xa) / (xb - xa)
    ax.plot([xa, xb], [yb, yb], color=INK, lw=2.0)
    ax.add_patch(Polygon([(x0, yb - 0.004), (x0 - 0.012, yb - 0.03), (x0 + 0.012, yb - 0.03)], fc=COLORS[2],
                         ec="none"))
    ax.text(x0 - 0.012, yb + 0.008, r"$x_0$ = 0.45", fontsize=8, ha="right", va="bottom", color=COLORS[2])
    ax.text(0.69, yb - 0.003, r"lever rule: $f_\beta=\frac{x_0-x_\alpha}{x_\beta-x_\alpha}$ = %.2f" % fb,
            fontsize=8.5, ha="left", va="center")
    ax.set_xlim(0, 1)
    ax.set_ylim(ymin, ymax)
    ax.set_yticks([])
    ax.set_xlabel(r"mole fraction $x_B$")
    ax.set_ylabel("molar Gibbs energy G (arbitrary units)")
    save(fig, "06", "fig-6-2-common-tangent")


# --------------------------------------------------------------------------- 6.3
def _morph(kind, seed=4, n=90):
    rng = np.random.default_rng(seed)
    if kind == "spinodal":
        f = gaussian_filter(rng.normal(size=(n, n)), 3.0, mode="wrap")
        return f > np.quantile(f, 0.70)
    img = np.zeros((n, n), bool)
    Y, X = np.mgrid[0:n, 0:n]
    for _ in range(14):
        cx, cy = rng.uniform(5, n - 5, 2)
        r = rng.uniform(3.0, 5.0)
        img |= (X - cx) ** 2 + (Y - cy) ** 2 < r * r
    return img


def miscibility_gap_spinodal():
    Om = 18008.0
    fig = plt.figure(figsize=(6.8, 5.0))
    ax1 = fig.add_axes([0.10, 0.62, 0.62, 0.34])
    ax2 = fig.add_axes([0.10, 0.09, 0.62, 0.48], sharex=ax1)
    T = 700.0
    x = np.linspace(1e-6, 1 - 1e-6, 2000)
    G = Om * x * (1 - x) + R * T * (_xlnx(x) + _xlnx(1 - x))
    ax1.plot(x, G, color=COLORS[0], lw=2.0)
    xb = _binodal(Om / (R * T))
    gb = Om * xb * (1 - xb) + R * T * (_xlnx(xb) + _xlnx(1 - xb))
    ax1.plot([0, 1], [gb, gb], color=INK, lw=1.0, ls="--")
    ax1.plot([xb, 1 - xb], [gb, gb], "o", color=INK, ms=5, zorder=5)
    xs = 0.5 - 0.5 * np.sqrt(1 - 2 * R * T / Om)
    for xx in (xs, 1 - xs):
        ax1.plot(xx, Om * xx * (1 - xx) + R * T * (_xlnx(xx) + _xlnx(1 - xx)), "D", color=COLORS[1], ms=5, zorder=5)
    ax1.text(xs + 0.02, Om * xs * (1 - xs) + R * T * (_xlnx(xs) + _xlnx(1 - xs)) - 30, f"spinodal\n{xs:.3f}",
             fontsize=7.5, color=COLORS[1], va="top")
    ax1.text(1 - xs - 0.02, Om * xs * (1 - xs) + R * T * (_xlnx(xs) + _xlnx(1 - xs)) - 30, f"spinodal\n{1 - xs:.3f}",
             fontsize=7.5, color=COLORS[1], va="top", ha="right")
    ax1.text(0.5, Om / 4 - R * T * np.log(2) + 25, f"+{Om / 4 - R * T * np.log(2):.0f} J mol$^{{-1}}$", fontsize=7.5,
             ha="center", va="bottom")
    ax1.text(xb, gb - 60, f"{xb:.3f}", fontsize=7.5, ha="center", va="top")
    ax1.text(1 - xb, gb - 60, f"{1 - xb:.3f}", fontsize=7.5, ha="center", va="top")
    ax1.text(0.02, 610, "T = 700 K,  Ω = 18.0 kJ mol$^{-1}$", fontsize=8, ha="left", va="top")
    ax1.axhline(0, color=GREY, lw=0.5)
    ax1.set_ylim(-700, 650)
    ax1.set_ylabel(r"$\Delta G_{\mathrm{mix}}$ (J mol$^{-1}$)")
    plt.setp(ax1.get_xticklabels(), visible=False)
    # lower panel
    Ts = np.linspace(380, Om / (2 * R) - 0.01, 400)
    xbs = np.array([_binodal(Om / (R * t)) for t in Ts])
    xss = 0.5 - 0.5 * np.sqrt(1 - 2 * R * Ts / Om)
    Tc = Om / (2 * R)
    ax2.fill_betweenx(Ts, xss, 1 - xss, color="#F6D9BF", lw=0)
    ax2.fill_betweenx(Ts, xbs, xss, color="#DCE6F0", lw=0)
    ax2.fill_betweenx(Ts, 1 - xss, 1 - xbs, color="#DCE6F0", lw=0)
    ax2.plot(np.r_[xbs, 0.5, (1 - xbs)[::-1]], np.r_[Ts, Tc, Ts[::-1]], color=COLORS[0], lw=2.0, label="binodal")
    ax2.plot(np.r_[xss, 0.5, (1 - xss)[::-1]], np.r_[Ts, Tc, Ts[::-1]], color=COLORS[1], lw=1.6, ls="--",
             label="spinodal")
    for t in (500, 700, 900, 1000):
        ax2.plot([_binodal(Om / (R * t))], [t], "o", color=COLORS[0], ms=4)
        ax2.plot([0.5 - 0.5 * np.sqrt(1 - 2 * R * t / Om)], [t], "o", color=COLORS[1], ms=4)
    ax2.plot(0.5, Tc, "^", color=INK, ms=6)
    ax2.text(0.5, Tc + 12, f"$T_c$ = Ω/2R = {Tc:.0f} K", fontsize=8, ha="center", va="bottom")
    ax2.text(0.5, 560, "unstable:\nspinodal\ndecomposition", fontsize=8, ha="center", va="center")
    ax2.annotate("metastable:\nnucleation and growth", xy=(0.915, 660), xytext=(0.985, 1140), fontsize=7.5, ha="right",
                 va="top", arrowprops=dict(arrowstyle="-", color=INK, lw=0.6))
    ax2.axhline(700, color=GREY, lw=0.6, ls=":")
    for xa, mk in ((0.15, "s"), (0.30, "s")):
        ax2.plot(xa, 700, mk, color=INK, ms=6, zorder=6)
    ax2.text(0.15, 715, "x = 0.15", fontsize=7.5, ha="center", va="bottom")
    ax2.text(0.30, 715, "x = 0.30", fontsize=7.5, ha="center", va="bottom")
    ax2.text(0.03, 990, "one phase", fontsize=8, va="top")
    ax2.legend(loc="upper left", fontsize=8)
    ax2.set_xlim(0, 1)
    ax2.set_ylim(400, 1150)
    ax2.set_xlabel(r"mole fraction $x$ (e.g. $x_{\mathrm{Ni}}$ in Au–Ni model)")
    ax2.set_ylabel("T (K)")
    for xx in (xb, xs, 1 - xs, 1 - xb):
        ax2.plot([xx, xx], [700, 1150], color=GREY, lw=0.6, ls=":", clip_on=True)
        ax1.plot([xx, xx], [-700, 650], color=GREY, lw=0.6, ls=":")
    # morphology sketches
    for k, (kind, title, yy) in enumerate([("nucleation", "x = 0.15: discrete\nprecipitates (x ≈ 0.94)", 0.40),
                                            ("spinodal", "x = 0.30: interconnected\nspinodal structure", 0.09)]):
        a = fig.add_axes([0.80, yy, 0.17, 0.17])
        a.imshow(_morph(kind), cmap="Greys", vmin=-0.4, vmax=1.6, interpolation="bilinear")
        a.set_xticks([])
        a.set_yticks([])
        for sp in a.spines.values():
            sp.set_visible(True)
            sp.set_color(GREY)
        a.set_title(title, fontsize=7.5)
    ax2.annotate("", xy=(1.13, 0.53), xycoords="axes fraction", xytext=(0.15, 700), textcoords="data",
                 arrowprops=dict(arrowstyle="-", color=GREY, lw=0.6))
    ax2.annotate("", xy=(1.13, 0.10), xycoords="axes fraction", xytext=(0.30, 700), textcoords="data",
                 arrowprops=dict(arrowstyle="-", color=GREY, lw=0.6))
    save(fig, "06", "fig-6-3-miscibility-gap-spinodal")


# --------------------------------------------------------------------------- 6.4
def _drop(ax, x0, w, theta, label, sub):
    th = np.radians(theta)
    Rr = w / np.sin(th)
    yc = -Rr * np.cos(th)
    a = np.linspace(np.pi / 2 - th, np.pi / 2 + th, 200)
    X, Y = x0 + Rr * np.cos(a), yc + Rr * np.sin(a)
    ax.add_patch(Polygon(np.c_[X, Y], closed=True, fc="#BFD7EA", ec=COLORS[0], lw=1.4, zorder=2))
    ax.add_patch(Rectangle((x0 - 2.0, -0.45), 4.0, 0.45, fc="#D9D9D9", ec=INK, lw=0.8, zorder=1))
    cx = x0 + w
    L = 0.9
    _arr(ax, (cx, 0), (cx + L, 0), color=COLORS[2], lw=1.4, ms=9)
    _arr(ax, (cx, 0), (cx - L, 0), color=COLORS[3], lw=1.4, ms=9)
    # tangent direction of the liquid surface at the right contact line (pointing away along lv)
    t = np.array([-np.cos(th), np.sin(th)])
    _arr(ax, (cx, 0), (cx + L * t[0], L * t[1]), color=COLORS[1], lw=1.4, ms=9)
    ax.text(cx + L + 0.05, 0.05, r"$\gamma_{sv}$", fontsize=8.5, color=COLORS[2], va="bottom")
    ax.text(cx - L, -0.08, r"$\gamma_{sl}$", fontsize=8.5, color=COLORS[3], va="top", ha="center")
    ax.text(cx + L * t[0] * 1.1, L * t[1] * 1.1 + 0.03, r"$\gamma_{lv}$", fontsize=8.5, color=COLORS[1],
            ha="center", va="bottom")
    ax.add_patch(Arc((cx, 0), 0.7, 0.7, theta1=180 - theta, theta2=180, color=INK, lw=0.9))
    ax.text(cx - 0.45 * np.cos(np.radians(theta / 2)), 0.45 * np.sin(np.radians(theta / 2)),
            "θ", fontsize=8.5, ha="right", va="bottom")
    ax.text(x0, -0.6, label, fontsize=7.5, ha="center", va="top")
    ax.text(x0, -1.0, sub, fontsize=7.5, ha="center", va="top", color="#555555")


def _arcpts(p, q, alpha, n=30):
    """Circular arc from p to q whose end tangents deviate by alpha (rad) from the chord (alpha>0 bulges left of p->q)."""
    p, q = np.asarray(p, float), np.asarray(q, float)
    if abs(alpha) < 1e-6:
        return np.linspace(p, q, n)
    c = np.linalg.norm(q - p)
    u = (q - p) / c
    nrm = np.array([-u[1], u[0]])
    Rr = c / (2 * np.sin(alpha))
    h = (c / 2) / np.tan(alpha)
    ctr = (p + q) / 2 - nrm * h
    a0 = np.arctan2(*(p - ctr)[::-1])
    a1 = np.arctan2(*(q - ctr)[::-1])
    da = (a1 - a0 + np.pi) % (2 * np.pi) - np.pi
    a = a0 + np.linspace(0, 1, n) * da
    return ctr + abs(Rr) * np.c_[np.cos(a), np.sin(a)]


def _junction(ax, cx, cy, phi, film=False, d=0.55, L=1.5):
    dirs = [np.radians(a) for a in (90, 210, 330)]
    for a in dirs:
        ax.plot([cx, cx + L * np.cos(a)], [cy, cy + L * np.sin(a)], color=INK, lw=1.2, zorder=1)
    corners = [np.array([cx + d * np.cos(a), cy + d * np.sin(a)]) for a in dirs]
    alpha = np.radians((phi - 60) / 2)
    pts = []
    for k in range(3):
        p, q = corners[k], corners[(k + 1) % 3]
        # bulge outward: p->q runs counter-clockwise, outward normal is to the right, i.e. alpha<0 in _arcpts
        pts.append(_arcpts(p, q, -alpha))
    poly = np.vstack(pts)
    ax.add_patch(Polygon(poly, closed=True, fc="#BFD7EA", ec=COLORS[0], lw=1.2, zorder=3))
    if film:
        for a in dirs:
            e = np.array([np.cos(a), np.sin(a)])
            nn = np.array([-e[1], e[0]])
            p0 = np.array([cx, cy]) + d * e
            p1 = np.array([cx, cy]) + L * e
            ax.add_patch(Polygon([p0 + 0.05 * nn, p1 + 0.05 * nn, p1 - 0.05 * nn, p0 - 0.05 * nn], fc="#BFD7EA",
                                 ec=COLORS[0], lw=0.8, zorder=2))


def interfaces_wetting():
    fig = plt.figure(figsize=(6.8, 5.0))
    axa = fig.add_axes([0.0, 0.52, 0.48, 0.45])
    axb = fig.add_axes([0.50, 0.52, 0.50, 0.45])
    axc = fig.add_axes([0.10, 0.08, 0.76, 0.38])
    for a in (axa, axb):
        a.set_aspect("equal")
        a.axis("off")
    _drop(axa, 0.0, 1.3, 30, "θ = 30°: wetting", "(solder on clean Cu)")
    _drop(axa, 4.6, 0.75, 120, "θ = 120°: non-wetting", "(water on PTFE)")
    axa.text(-2.0, 2.15, r"(a) Young: $\gamma_{sv}=\gamma_{sl}+\gamma_{lv}\cos\theta$", fontsize=9, va="top")
    axa.set_xlim(-2.1, 6.8)
    axa.set_ylim(-1.5, 2.2)
    # (b) dihedral angles
    cases = [(1.0, 120, r"$\gamma_{gb}/\gamma_{sl}$ = 1.0" + "\nφ = 120°\nisolated pockets", False),
             (1.8, 52, r"$\gamma_{gb}/\gamma_{sl}$ = 1.8" + "\nφ = 52°\nchannels on\ntriple lines", False),
             (2.0, 0, r"$\gamma_{gb}/\gamma_{sl}\geq$ 2" + "\nφ = 0: film,\nliquid-metal\nembrittlement", True)]
    for k, (rat, phi, lab, film) in enumerate(cases):
        cx = 1.7 + 3.4 * k
        _junction(axb, cx, 0.4, phi, film=film)
        axb.text(cx, -1.05, lab, fontsize=7.5, ha="center", va="top")
    axb.text(0.1, 2.35, r"(b) dihedral angle: $\gamma_{gb}=2\gamma_{sl}\cos(\varphi/2)$", fontsize=9, va="top")
    axb.set_xlim(0, 10.2)
    axb.set_ylim(-3.1, 2.4)
    # (c) Gibbs-Thomson
    r = np.linspace(1, 30, 400)
    gam, Vm, T = 0.2, 1.0e-5, 573.0
    c = np.exp(2 * gam * Vm / (r * 1e-9 * R * T))
    axc.plot(r, c, color=COLORS[0], lw=2.0)
    for rr in (2, 5, 20):
        cc = np.exp(2 * gam * Vm / (rr * 1e-9 * R * T))
        axc.plot(rr, cc, "o", color=COLORS[0], ms=5)
    axc.set_xlim(0, 30)
    axc.set_ylim(1.0, 2.4)
    axc.set_xlabel("particle radius r (nm)")
    axc.set_ylabel(r"$c(r)/c_\infty$", color=COLORS[0])
    axc.text(29.5, 2.35, "solubility next to a precipitate in Al at 300 °C:\n"
             "γ = 0.2 J m$^{-2}$, $V_m$ = 1.0×10$^{-5}$ m$^3$ mol$^{-1}$\n"
             r"c/c$_\infty$ = 1.52 (r = 2 nm), 1.18 (5 nm), 1.04 (20 nm)",
             fontsize=7.5, ha="right", va="top", color=COLORS[0])
    a2 = axc.twinx()
    a2.spines["right"].set_visible(True)
    dT = 141.0 / r
    a2.plot(r, dT, color=COLORS[1], lw=1.6, ls="--")
    for rr in (5, 10):
        a2.plot(rr, 141.0 / rr, "s", color=COLORS[1], ms=5)
        a2.text(rr + 0.6, 141.0 / rr, f"{141.0 / rr:.0f} K at {rr} nm", fontsize=7.5, color=COLORS[1], va="center")
    a2.set_ylim(0, 100)
    a2.set_ylabel(r"Sn: $\Delta T_m$ = 1.41×10$^{-7}$ K m / r  (K)", color=COLORS[1])
    axc.text(-0.08, 1.03, "(c) Gibbs–Thomson", fontsize=9, transform=axc.transAxes, va="bottom")
    save(fig, "06", "fig-6-4-interfaces-wetting")


# --------------------------------------------------------------------------- 6.5
def brouwer_diagram():
    A = 1e-2               # acceptor concentration [A'] (arbitrary units)
    p1, p2 = -26.0, 1.5    # log pO2 at the I/II and II/III boundaries
    KR = (A / 2) * A ** 2 * 10 ** (p1 / 2)     # n = [A'] at p1 in region II
    Ki = A * A * 10 ** ((p1 - p2) / 4)          # p = [A'] at p2 in region II
    lp = np.linspace(-30, 5, 1400)
    n_, p_, v_ = [], [], []
    for L in lp:
        po = 10 ** L
        # electroneutrality 2[V] + p = n + [A'], with [V] = KR/(n^2 pO2^1/2) and p = Ki/n
        f = lambda ln: 2 * KR / (np.exp(2 * ln) * po ** 0.5) + Ki / np.exp(ln) - np.exp(ln) - A  # noqa: E731
        n = np.exp(brentq(f, -80, 10))
        n_.append(n)
        p_.append(Ki / n)
        v_.append(KR / (n * n * po ** 0.5))
    n_, p_, v_ = map(np.array, (n_, p_, v_))
    fig = plt.figure(figsize=(6.8, 4.8))
    ax = fig.add_axes([0.10, 0.11, 0.74, 0.80])
    ax.axvspan(-21, np.log10(0.21), color="#E8F1E4", zorder=0)
    ax.text(-10.8, -11.6, "SOFC electrolyte window (YSZ, 800 °C):\n$p_{O_2}$ = 10$^{-21}$ to 0.21 atm",
            fontsize=7.8, ha="center", va="bottom", color="#2E7D32")
    lv, ln_, lpp = np.log10(v_), np.log10(n_), np.log10(p_)
    ax.plot(lp, lv, color=COLORS[0], lw=2.0)
    ax.plot(lp, ln_, color=COLORS[1], lw=2.0)
    ax.plot(lp, lpp, color=COLORS[2], lw=2.0)
    ax.axhline(np.log10(A), color=INK, lw=1.0, ls=":")
    ax.text(-20.5, np.log10(A) + 0.12, "[A′] (fixed by doping)", fontsize=8, ha="left", va="bottom")
    for x in (p1, p2):
        ax.axvline(x, color=GREY, lw=0.9, ls="--")
    V = r"[\mathrm{V_O^{\bullet\bullet}}]"
    ax.text(-28, 0.35, "I\n" + rf"$n=2{V}$", fontsize=8.5, ha="center", va="bottom")
    ax.text(-12.25, 0.35, "II\n" + rf"$2{V}=[A']$", fontsize=8.5, ha="center", va="bottom")
    ax.text(3.25, 0.35, "III\n" + r"$p=[A']$", fontsize=8.5, ha="center", va="bottom")

    def lab(xv, arr, txt, col, dy, va):
        ax.text(xv, np.interp(xv, lp, arr) + dy, txt, color=col, fontsize=8.5, ha="center", va=va)
    lab(-28.2, lv, "−1/6", COLORS[0], -0.25, "top")
    lab(-19.0, lv, rf"${V}$: 0", COLORS[0], -0.2, "top")
    lab(3.6, lv, "−1/2", COLORS[0], -0.3, "top")
    lab(-28.0, ln_, r"$n$: −1/6", COLORS[1], 0.2, "bottom")
    lab(-16.0, ln_, r"$n$: −1/4", COLORS[1], 0.25, "bottom")
    lab(3.3, ln_, "0", COLORS[1], 0.2, "bottom")
    lab(-27.6, lpp, r"$p$: +1/6", COLORS[2], 0.3, "bottom")
    lab(-6.0, lpp, r"$p$: +1/4", COLORS[2], 0.25, "bottom")
    lab(3.3, lpp, "0", COLORS[2], -0.2, "top")
    ax.set_xlim(-30, 5)
    ax.set_ylim(-16, 0.3)
    ax.set_xlabel(r"$\log_{10}\, p_{O_2}$ (atm)")
    ax.set_ylabel("log$_{10}$ concentration (arbitrary units)")
    # total conductivity on a secondary axis
    a2 = ax.twinx()
    a2.spines["right"].set_visible(True)
    mu_i, mu_e, mu_h = 1.0, 3.0, 3.0
    sig = np.log10(2 * v_ * mu_i + n_ * mu_e + p_ * mu_h)
    a2.plot(lp, sig, color=INK, lw=1.5, ls="-.")
    a2.set_ylim(sig.min() - 0.3, sig.min() + 3.2)
    a2.set_ylabel(r"log$_{10}$ total conductivity σ (arb.), dash-dot")
    i0 = np.searchsorted(lp, -11)
    a2.text(-11, sig[i0] + 0.05, "ionic plateau", fontsize=7.8, ha="center", va="bottom")
    i1 = np.searchsorted(lp, -25.0)
    a2.text(-24.6, sig[i1] + 0.05, "σ: n-type", fontsize=7.8, ha="left", va="bottom")
    a2.text(4.9, sig[-1] + 0.05, "σ: p-type", fontsize=7.8, ha="right", va="bottom")
    save(fig, "06", "fig-6-5-brouwer-diagram")


# --------------------------------------------------------------------------- 6.6
ELL = [  # (label, dH, dS-slope, colour, label T (degC), label dy, va)
    ("4Cu + O$_2$ = 2Cu$_2$O", -337.0, 0.140, "#B5651D", 20, 8, "bottom"),
    ("2Ni + O$_2$ = 2NiO", -471.0, 0.172, "#4D9A6B", 1250, 8, "bottom"),
    ("2Fe + O$_2$ = 2FeO", -519.2, 0.1251, "#8B0000", 20, -8, "top"),
    ("2H$_2$ + O$_2$ = 2H$_2$O(g)", -492.9, 0.1094, "#56B4E9", 20, 6, "bottom"),
    ("4/3Cr + O$_2$ = 2/3Cr$_2$O$_3$", -746.8, 0.1702, "#009E73", 20, 8, "bottom"),
    ("Si + O$_2$ = SiO$_2$", -902.0, 0.174, "#CC79A7", 20, 8, "bottom"),
    ("Ti + O$_2$ = TiO$_2$", -941.0, 0.178, "#7F7F7F", 20, -8, "top"),
    ("4/3Al + O$_2$ = 2/3Al$_2$O$_3$", -1117.0, 0.208, "#0072B2", 20, 8, "bottom"),
    ("2Mg + O$_2$ = 2MgO", -1202.0, 0.216, "#E69F00", 20, 8, "bottom")]


def ellingham_diagram():
    fig = plt.figure(figsize=(6.8, 5.0))
    ax = fig.add_axes([0.10, 0.10, 0.66, 0.84])
    ax.set_xlim(-273.15, 2200)
    ax.set_ylim(-1200, 0)
    TC = np.linspace(0, 2200, 300)
    TK = TC + 273.15
    xr = 2200
    TKr = xr + 273.15
    gfe = -519.2 + 0.1251 * TK
    ax.fill_between(TC, gfe, 0, color="#FBE9E7", zorder=0)
    ax.text(560, -120, "above the Fe/FeO line:\noxidizing to Fe", fontsize=7.5, color="#8B0000", ha="center")
    Tb = 1363.0
    for name, H, S, col, xl, dy, va in ELL:
        g = H + S * TK
        if "Mg" in name:
            gb_ = H + S * Tb
            S2 = S + 2 * (128.0 / Tb)  # entropy of vaporization of 2 Mg
            g = np.where(TK <= Tb, g, gb_ + S2 * (TK - Tb))
            ax.plot(Tb - 273.15, gb_, "o", color=col, ms=4)
            ax.text(Tb - 273.15 + 30, gb_ - 25, "Mg boils\n1090 °C", fontsize=7, color=col, va="top")
        ls = "--" if "H$_2$" in name else "-"
        ax.plot(TC, g, color=col, lw=1.7, ls=ls)
        ax.text(xl, H + S * (xl + 273.15) + dy, name, fontsize=7.2, color=col, va=va, ha="left",
                rotation=np.degrees(np.arctan(S)), rotation_mode="anchor", transform_rotates_text=True)
    HCO, SCO = -223.4, -0.1753
    gco = HCO + SCO * TK
    gco2 = -394 - 0.001 * TK
    ax.plot(TC, gco, color=INK, lw=1.9)
    ax.plot(TC, gco2, color=INK, lw=1.2, ls=":")
    ax.text(2190, HCO + SCO * (2190 + 273.15) + 10, "2C + O$_2$ = 2CO", fontsize=7.5, ha="right", va="bottom",
            rotation=np.degrees(np.arctan(SCO)), rotation_mode="anchor", transform_rotates_text=True)
    ax.text(2190, -394 + 8, "C + O$_2$ = CO$_2$", fontsize=7.5, ha="right", va="bottom")
    # crossings with C/CO
    lines = []
    for k, (name, H, S, col, *_r) in enumerate(ELL):
        for key, ox in (("Fe", "FeO"), ("Cr", "Cr$_2$O$_3$"), ("Si", "SiO$_2$"), ("Ti", "TiO$_2$"), ("Al", "Al$_2$O$_3$")):
            if name.split("+")[0].strip().endswith(key):
                Tx = (H - HCO) / (SCO - S)
                ax.plot(Tx - 273.15, H + S * Tx, "o", color=col, mec=INK, ms=6, zorder=6)
                lines.append(f"{ox}: {Tx - 273.15:.0f} °C")
    ax.text(1530, -800, "C/CO line crosses\n" + "\n".join(lines), fontsize=7.5, va="top", ha="left",
            bbox=dict(fc="white", ec=GREY, lw=0.6, pad=3))
    # pO2 nomogram: pivot O at T = 0 K, Delta G = 0
    x0 = -273.15
    ax.plot(x0, 0, "o", color=INK, ms=6, clip_on=False, zorder=7)
    ax.text(x0 + 25, -15, "O", fontsize=10, weight="bold", va="top")
    for e in range(0, -52, -2):
        g_r = R * TKr * np.log(10.0 ** e) / 1000
        if g_r >= -1200:
            ax.plot([xr, xr + 30], [g_r, g_r], color=INK, lw=0.8, clip_on=False)
            if e % 4 == 0:
                ax.text(xr + 40, g_r, f"10$^{{{e}}}$" if e else "1", fontsize=6.8, va="center", clip_on=False)
        else:
            tc = -1200e3 / (R * np.log(10.0 ** e)) - 273.15
            ax.plot([tc, tc], [-1200, -1180], color=INK, lw=0.8)
            if e % 6 == 0:
                ax.text(tc, -1172, f"10$^{{{e}}}$", fontsize=6.8, ha="center", va="bottom")
    ax.text(xr + 20, 12, r"$p_{O_2}$ (atm)", fontsize=7.5, clip_on=False, va="bottom")
    # construction through Cr/Cr2O3 at 1100 C
    TK1 = 1373.15
    g1 = -746.8 + 0.1702 * TK1
    ax.plot([x0, xr], [0, g1 / TK1 * TKr], color="#009E73", lw=0.9, ls="--")
    ax.plot(1100, g1, "s", color="#009E73", ms=5, zorder=7)
    pO2 = np.exp(g1 * 1000 / (R * TK1))
    mant, ex = f"{pO2:.0e}".split("e")
    ax.text(1120, -1025, f"line O → Cr$_2$O$_3$ at 1100 °C (■)\ngives $p_{{O_2}}$ ≈ {mant}×10$^{{{int(ex)}}}$ atm",
            fontsize=7.2, color="#007A5A", va="top", ha="left")
    # H2/H2O nomogram: pivot H at T = 0 K, Delta G = Delta H(H2O)
    HH, SH = -492.9, 0.1094
    ax.plot(x0, HH, "o", color="#56B4E9", ms=6, clip_on=False, zorder=7)
    ax.text(x0 + 25, HH - 12, "H", fontsize=10, weight="bold", color="#2A7FB8", va="top")
    gl = []
    for e in range(-2, 11):
        g_r = HH + TKr * (SH - 2 * R / 1000 * np.log(10.0 ** e))
        if -1200 <= g_r <= 0:
            gl.append(g_r)
            ax.plot([xr + 230, xr + 260], [g_r, g_r], color="#2A7FB8", lw=0.8, clip_on=False)
            if e % 2 == 0:
                ax.text(xr + 270, g_r, f"10$^{{{e}}}$", fontsize=6.8, va="center", color="#2A7FB8", clip_on=False)
    ax.plot([xr + 245, xr + 245], [min(gl), max(gl)], color="#2A7FB8", lw=0.6, clip_on=False)
    ax.text(xr + 230, 50, r"$p_{H_2}/p_{H_2O}$", fontsize=7.5, color="#2A7FB8", clip_on=False, va="bottom")
    ax.set_xticks([0, 500, 1000, 1500, 2000])
    ax.set_xlabel("temperature (°C)   [pivots O and H at T = 0 K]")
    ax.set_ylabel(r"$\Delta G^\circ$ (kJ per mol O$_2$)")
    ax.spines["right"].set_visible(True)
    save(fig, "06", "fig-6-6-ellingham-diagram")


if __name__ == "__main__":
    regular_solution_curves()
    common_tangent()
    miscibility_gap_spinodal()
    interfaces_wetting()
    brouwer_diagram()
    ellingham_diagram()
