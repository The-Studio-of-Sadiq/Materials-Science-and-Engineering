"""Figures for Chapter 45 — Surfaces, Interfaces and Tribology.

Run from the repository root:  python figures/scripts/ch45.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, Ellipse, Wedge, Arc, FancyBboxPatch
from scipy.special import erfc, erfinv

STEEL = "#B9BEC4"
SOFT = "#D9C7A3"
OIL = "#F6D88B"


# ---------------------------------------------------------------- Figure 45.1
def _cube(ax, x, y, z, fc, ec="#333333", ox=0.45, oy=0.32, lw=0.5):
    """Draw a unit cube at lattice (x, y, z) in cabinet projection (top, front, right faces)."""
    P = lambda a, b, c: (a + ox * b, c + oy * b)
    def shade(f):
        r, g, b_ = [int(fc[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        return (r * f, g * f, b_ * f)
    front = [P(x, y, z), P(x + 1, y, z), P(x + 1, y, z + 1), P(x, y, z + 1)]
    top = [P(x, y, z + 1), P(x + 1, y, z + 1), P(x + 1, y + 1, z + 1), P(x, y + 1, z + 1)]
    right = [P(x + 1, y, z), P(x + 1, y + 1, z), P(x + 1, y + 1, z + 1), P(x + 1, y, z + 1)]
    ax.add_patch(Polygon(front, fc=shade(0.80), ec=ec, lw=lw))
    ax.add_patch(Polygon(right, fc=shade(0.62), ec=ec, lw=lw))
    ax.add_patch(Polygon(top, fc=shade(1.0), ec=ec, lw=lw))


def surface_tsk():
    fig = plt.figure(figsize=(6.8, 3.7))
    ax = fig.add_axes([0.0, 0.0, 0.60, 1.0])
    ax.set_aspect("equal"); ax.axis("off")
    NX, NY = 8, 6
    cubes = {}
    base = "#C8D3DE"
    for x in range(NX):
        for y in range(NY):
            cubes[(x, y, -1)] = base
            cubes[(x, y, 0)] = base
    vac = (2, 1, 0)                     # terrace vacancy on the lower terrace
    cubes.pop(vac)
    # upper terrace: y >= 4 for x < 5, y >= 3 for x >= 5  -> kink at x = 5
    up = "#E5C79A"
    for x in range(NX):
        for y in range(NY):
            if (y >= 4 and x < 5) or (y >= 3 and x >= 5):
                cubes[(x, y, 1)] = up
    adat = (5, 0, 1)                    # adatom on lower terrace
    stepad = (2, 3, 1)                  # step adatom touching the step riser
    cubes[adat] = "#D55E00"
    cubes[stepad] = "#009E73"
    kink = (5, 3, 1)
    cubes[kink] = "#CC79A7"
    for key in sorted(cubes, key=lambda k: (-k[1], k[0], k[2])):
        _cube(ax, *key, fc=cubes[key] if cubes[key].startswith("#") else base)
    ox, oy = 0.45, 0.32
    P = lambda a, b, c: (a + ox * b, c + oy * b)

    def lab(pt, txt, xyt, color=INK):
        ax.annotate(txt, xy=pt, xytext=xyt, fontsize=7.3, color=color, ha="center", va="center",
                    arrowprops=dict(arrowstyle="-", lw=0.6, color=color))
    lab(P(adat[0] + 0.5, 0.0, 1.5), "adatom\n5 of 6 broken", (3.0, -1.5), COLORS[1])
    lab(P(vac[0] + 0.5, 1.5, 0.75), "terrace\nvacancy", (-0.6, 2.9))
    lab(P(stepad[0] + 0.5, 3.0, 1.7), "step adatom\n4 of 6", (0.6, 4.9), COLORS[2])
    lab(P(kink[0] + 0.4, 3.0, 2.0), "kink\n3 of 6", (5.2, 5.4), COLORS[3])
    lab(P(7.6, 3.0, 1.8), "step-edge atom\n2 of 6", (12.4, 3.3))
    lab(P(7.5, 5.5, 2.0), "upper terrace\n1 of 6", (11.4, 5.6))
    lab(P(7.6, 0.5, 1.0), "lower terrace\natom 1 of 6", (12.4, 0.9))
    ax.text(5.6, -2.5, "simple cubic (100) vicinal surface: broken bonds per site", fontsize=7.3,
            ha="center", color="#444444")
    ax.set_xlim(-1.8, 13.8); ax.set_ylim(-2.8, 6.6)
    ax.text(-1.7, 6.4, "(a) terrace–step–kink", fontsize=9, weight="bold", va="top")

    # (b) Wulff construction
    bx = fig.add_axes([0.61, 0.04, 0.38, 0.92])
    bx.set_aspect("equal"); bx.axis("off")
    g10, g11 = 1.0, 1.12

    def gamma(th):
        f1 = g10 * (np.abs(np.cos(th)) + np.abs(np.sin(th)))
        f2 = g11 * (np.abs(np.cos(th - np.pi / 4)) + np.abs(np.sin(th - np.pi / 4)))
        return np.minimum(f1, f2)
    th = np.linspace(0, 2 * np.pi, 1441)
    g = gamma(th)
    # Wulff shape: octagon with {10} planes at g10 and {11} planes at g11
    a = g10; b = g11 * np.sqrt(2)
    verts = []
    for sx in (1, -1):
        pass
    octo = np.array([[a, b - a], [b - a, a], [-(b - a), a], [-a, b - a], [-a, -(b - a)], [-(b - a), -a],
                     [b - a, -a], [a, -(b - a)]])
    bx.add_patch(Polygon(octo, fc=COLORS[0], alpha=0.22, ec=COLORS[0], lw=1.6))
    # sample Wulff planes
    for t in np.radians(np.arange(0, 360, 15)):
        r = gamma(t)
        p = r * np.array([np.cos(t), np.sin(t)])
        d = np.array([-np.sin(t), np.cos(t)])
        L = 0.7
        bx.plot([p[0] - L * d[0], p[0] + L * d[0]], [p[1] - L * d[1], p[1] + L * d[1]], color="#9A9A9A", lw=0.5)
        bx.plot([0, p[0]], [0, p[1]], color="#C8C8C8", lw=0.4)
    bx.plot(g * np.cos(th), g * np.sin(th), color=COLORS[1], lw=1.8)
    bx.plot(0, 0, "k.", ms=3)
    bx.set_xlim(-1.75, 1.75); bx.set_ylim(-2.0, 1.75)
    bx.text(1.62, 0.0, "{10}\ncusp", fontsize=7, ha="left", va="center", color=COLORS[1])
    c45 = gamma(np.pi / 4)
    bx.annotate("{11} cusp", xy=(c45 * np.cos(np.pi / 4), c45 * np.sin(np.pi / 4)), xytext=(1.25, 1.5),
                fontsize=7, color=COLORS[1], ha="center", arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[1]))
    bx.text(-1.7, 1.62, "γ(θ) polar plot", fontsize=7.3, color=COLORS[1], va="center")
    bx.text(0, 0.18, "equilibrium\nshape", fontsize=7.3, color=COLORS[0], ha="center", va="bottom")
    bx.text(0, -1.78, "Wulff planes normal to the radius at distance γ(θ)\nclose-packed, low-γ facets dominate",
            fontsize=7, ha="center", va="center", color="#444444")
    bx.text(-1.72, 1.92, "(b) Wulff construction", fontsize=9, weight="bold", va="top")
    save(fig, "45", "fig-45-1-terrace-step-kink")


# ---------------------------------------------------------------- Figure 45.2
def _drop(ax, xc, yb, R, theta_deg, fc="#9CC9F0", ec="#2C6FAE", lw=1.2, alpha=1.0):
    """Spherical-cap drop of radius R on the line y = yb with contact angle theta; returns base half-width."""
    th = np.radians(theta_deg)
    yc = yb - R * np.cos(th)
    a0 = np.arcsin(np.clip((yb - yc) / R, -1, 1))
    ang = np.linspace(a0, np.pi - a0, 200)
    xs = xc + R * np.cos(ang)
    ys = yc + R * np.sin(ang)
    ax.add_patch(Polygon(np.c_[xs, ys], closed=True, fc=fc, ec=ec, lw=lw, alpha=alpha))
    return R * np.sin(th)


def wetting():
    fig = plt.figure(figsize=(6.8, 4.5))
    # --- top: Young
    ax = fig.add_axes([0.0, 0.50, 0.62, 0.49])
    ax.set_xlim(0, 10); ax.set_ylim(-1.35, 3.3); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(Rectangle((0.3, -0.6), 9.4, 0.6, fc=STEEL, ec="none"))
    theta = 70
    half = _drop(ax, 5.4, 0.0, 2.35, theta)
    xl = 5.4 - half
    t = np.radians(theta)
    L = 1.7
    ax.annotate("", xy=(xl + L * np.cos(t), L * np.sin(t)), xytext=(xl, 0),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.6))
    ax.text(xl + L * np.cos(t) - 0.15, L * np.sin(t) + 0.1, "γ$_{LV}$", fontsize=9, color=COLORS[0],
            va="bottom", ha="right")
    ax.annotate("", xy=(xl - 1.8, 0.05), xytext=(xl, 0.05),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.6))
    ax.text(xl - 1.5, 0.22, "γ$_{SV}$", fontsize=9, color=COLORS[1], ha="center")
    ax.annotate("", xy=(xl + 1.6, 0.05), xytext=(xl, 0.05),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[2], lw=1.6))
    ax.text(xl + 1.7, 0.22, "γ$_{SL}$", fontsize=9, color=COLORS[2], ha="left")
    ax.add_patch(Arc((xl, 0), 1.3, 1.3, theta1=0, theta2=theta, color=INK, lw=1))
    ax.text(xl + 0.72, 0.62, "θ", fontsize=10)
    ax.text(5.9, 1.25, "liquid", fontsize=8, ha="center", color="#1B4F80")
    ax.text(9.6, 0.25, "vapour", fontsize=8, ha="right", color="#555555")
    ax.text(9.0, -0.3, "solid", fontsize=8, ha="center", va="center")
    ax.text(5.0, -1.05, "γ$_{SV}$ = γ$_{SL}$ + γ$_{LV}$ cos θ", fontsize=9, ha="center", va="center")
    ax.text(0.3, 3.2, "Young: smooth solid", fontsize=9, weight="bold", va="top")

    # examples
    ex = fig.add_axes([0.63, 0.52, 0.36, 0.46])
    ex.set_xlim(0, 4.0); ex.set_ylim(0, 5.6); ex.set_aspect("equal"); ex.axis("off")
    for k, (th_, lab, R) in enumerate([(20, "glass + water  θ ≈ 20°", 3.4), (95, "PE + water  θ ≈ 95°", 0.62),
                                        (110, "PTFE + water  θ ≈ 110°", 0.58)]):
        y0 = 4.5 - k * 1.85
        ex.add_patch(Rectangle((0.3, y0 - 0.22), 3.4, 0.22, fc=STEEL, ec="none"))
        _drop(ex, 2.0, y0, R, th_, lw=1.0)
        ex.text(2.0, y0 - 0.5, lab, fontsize=7.5, ha="center", va="center")

    # --- bottom: Wenzel and Cassie
    specs = [("(a) Wenzel: liquid fills the texture\nr = 1.5, θ = 110° → θ* = 121°", "W"),
             ("(b) Cassie–Baxter: air trapped under drop\nf = 0.1, θ = 110° → θ* = 159°", "C")]
    for k, (title, mode) in enumerate(specs):
        bx = fig.add_axes([0.005 + k * 0.40, 0.01, 0.39, 0.45])
        bx.set_xlim(0, 10); bx.set_ylim(-1.5, 5.0); bx.set_aspect("equal"); bx.axis("off")
        bx.add_patch(Rectangle((0.2, -1.4), 9.6, 0.6, fc=STEEL, ec="none"))
        pw, ps = (0.5, 0.5) if mode == "W" else (0.16, 0.34)
        if mode == "W":
            half = _drop(bx, 5.0, 0.0, 2.0, 121)
        else:
            half = _drop(bx, 5.0, 0.0, 2.1, 159)
        x = 0.2
        while x + pw <= 9.8:
            bx.add_patch(Rectangle((x, -0.8), pw, 0.8, fc=STEEL, ec="none"))
            g0, g1 = x + pw, x + pw + ps
            if mode == "W" and g0 >= 5.0 - half - 0.05 and g1 <= 5.0 + half + 0.05:
                bx.add_patch(Rectangle((g0, -0.8), ps, 0.8, fc="#9CC9F0", ec="none"))
            x += pw + ps
        if mode == "C":
            bx.annotate("air pockets", xy=(5.0 + 0.25, -0.4), xytext=(8.4, 1.6), fontsize=7, color="#555555",
                        ha="center", arrowprops=dict(arrowstyle="-", lw=0.6, color="#777777"))
        bx.text(5.0, 4.95, title, fontsize=7.6, ha="center", va="top")
    # lotus inset
    li = fig.add_axes([0.81, 0.03, 0.18, 0.40])
    li.set_xlim(0, 4); li.set_ylim(-0.6, 4.4); li.set_aspect("equal"); li.axis("off")
    li.add_patch(Rectangle((0, -0.5), 4, 0.5, fc="#8FBF7F", ec="none"))
    for xc in np.arange(0.4, 4.0, 0.8):
        li.add_patch(Ellipse((xc, 0.35), 0.55, 0.9, fc="#A9D39A", ec="#4F7F3F", lw=0.6))
        for a in np.linspace(0.3, np.pi - 0.3, 6):
            x0, y0 = xc + 0.27 * np.cos(a), 0.35 + 0.45 * np.sin(a)
            li.plot([x0, x0 + 0.08 * np.cos(a)], [y0, y0 + 0.08 * np.sin(a)], color="#4F7F3F", lw=0.6)
    _drop(li, 2.0, 0.85, 0.95, 160, lw=0.9)
    li.text(2.0, 4.3, "lotus leaf:\nmicro-papillae\n+ nano-wax", fontsize=6.6, ha="center", va="top")
    save(fig, "45", "fig-45-2-wetting-regimes")


# ---------------------------------------------------------------- Figure 45.3
def hertz():
    nu = 0.3
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.8, 3.7), gridspec_kw=dict(width_ratios=[1, 1.1]))
    fig.subplots_adjust(wspace=0.3, left=0.08, right=0.98, bottom=0.14, top=0.90)
    r = np.linspace(-1.5, 1.5, 601)
    p = np.sqrt(np.clip(1 - r ** 2, 0, None))
    ax.fill_between(r, 0, p, color=COLORS[0], alpha=0.15)
    ax.plot(r, p, color=COLORS[0], lw=2)
    ax.axhline(2 / 3, color="#888888", ls=":", lw=0.9)
    ax.text(1.48, 2 / 3 + 0.02, "$p_m$ = 2$p_0$/3", fontsize=7.5, ha="right", va="bottom", color="#555555")
    ax.set_xlim(-1.5, 1.5); ax.set_ylim(0, 1.25)
    ax.set_xlabel("$r/a$")
    ax.set_ylabel("Contact pressure $p/p_0$")
    ax.set_title("(a) surface pressure", fontsize=9)
    ax.text(0, 1.05, "$p = p_0\\sqrt{1-r^2/a^2}$", fontsize=9, ha="center")
    ax.text(0, 0.30, "steel ball R = 6.35 mm\nF = 500 N\na = 0.274 mm\n$p_0$ = 3.17 GPa",
            fontsize=7.5, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#999999", lw=0.6))

    z = np.linspace(1e-4, 3, 600)
    sz = 1 / (1 + z ** 2)
    sr = (1 + nu) * (1 - z * np.arctan(1 / z)) - 0.5 / (1 + z ** 2)
    tau = 0.5 * np.abs(sz - sr)
    bx.plot(sz, z, color=COLORS[0], lw=2, label="$|\\sigma_z|/p_0$")
    bx.plot(np.abs(sr), z, color=COLORS[2], lw=2, label="$|\\sigma_r|/p_0$")
    bx.plot(tau, z, color=COLORS[1], lw=2.2, label="$\\tau_{\\max}/p_0$")
    k = np.argmax(tau)
    bx.plot(tau[k], z[k], "o", color=COLORS[1], ms=5)
    bx.axhline(z[k], color=COLORS[1], ls="--", lw=0.9)
    bx.text(0.98, z[k] - 0.04, "yield and rolling-contact\nfatigue start here", fontsize=7.5, ha="right",
            va="bottom", color=COLORS[1], bbox=dict(fc="white", ec="none", pad=0.5, alpha=0.85))
    bx.annotate(f"{tau[k]:.2f} $p_0$ at z = {z[k]:.2f}a", xy=(tau[k], z[k]), xytext=(0.36, 1.25),
                fontsize=7.5, color=COLORS[1], arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[1]))
    bx.text(0.80, 0.05, "0.8", fontsize=7, color=COLORS[2], ha="center", va="top", alpha=0)
    bx.set_xlim(0, 1.0); bx.set_ylim(3, 0)
    bx.set_xlabel("Stress / $p_0$ (compressive magnitudes)")
    bx.set_ylabel("Depth $z/a$")
    bx.legend(loc="lower right", fontsize=8)
    bx.set_title("(b) stresses on the axis, ν = 0.3", fontsize=9)
    bx.text(0.98, 2.15, "example: τ$_{max}$ = 0.98 GPa\nat 0.13 mm depth", fontsize=7.3, ha="right", alpha=0)
    save(fig, "45", "fig-45-3-hertz-subsurface-stress")


# ---------------------------------------------------------------- Figure 45.4
def _rough(x, base, amp, seed, n=6):
    rng = np.random.default_rng(seed)
    y = np.full_like(x, base)
    for k in range(1, n + 1):
        y += amp / k * np.sin(k * 1.7 * x + rng.uniform(0, 6.28))
    return y


def wear_mechanisms():
    fig, axs = plt.subplots(2, 2, figsize=(6.8, 5.0))
    fig.subplots_adjust(left=0.01, right=0.99, top=0.95, bottom=0.01, wspace=0.04, hspace=0.14)
    for ax in axs.flat:
        ax.set_xlim(0, 10); ax.set_ylim(0, 6.5); ax.set_aspect("equal"); ax.axis("off")
    HARD = "#9AA3AD"
    x = np.linspace(0, 10, 500)

    # (a) adhesive
    ax = axs[0, 0]
    yl = _rough(x, 2.2, 0.12, 1)
    yu = _rough(x, 4.3, 0.12, 2)
    # lower asperity peak and upper asperity peak meeting at x~5
    yl += 0.9 * np.exp(-((x - 5.0) / 0.55) ** 2)
    yu -= 0.9 * np.exp(-((x - 5.0) / 0.55) ** 2)
    ax.fill_between(x, 0, yl, color=SOFT, lw=0)
    ax.plot(x, yl, color=INK, lw=0.8)
    ax.fill_between(x, yu, 6.0, color=HARD, lw=0)
    ax.plot(x, yu, color=INK, lw=0.8)
    ax.add_patch(Ellipse((5.0, 3.25), 0.9, 0.35, fc="#E8B46E", ec=INK, lw=0.6))
    ax.plot([4.2, 5.8], [3.0, 3.0], color=COLORS[1], lw=1.2, ls="--")
    ax.annotate("shear plane in softer body", xy=(5.75, 3.0), xytext=(6.3, 3.55), fontsize=6.8, color=COLORS[1],
                va="center", arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[1]))
    ax.text(5.0, 3.62, "junction", fontsize=6.8, ha="center", va="bottom", alpha=0)
    # transferred fragment stuck to hard surface
    ax.add_patch(Polygon([[1.6, 4.25], [2.6, 4.2], [2.4, 3.85], [1.8, 3.9]], fc=SOFT, ec=INK, lw=0.7))
    ax.annotate("transferred\nfragment", xy=(2.1, 3.95), xytext=(1.5, 2.95), fontsize=6.8, ha="center",
                arrowprops=dict(arrowstyle="-", lw=0.6))
    ax.add_patch(Polygon([[7.9, 2.75], [8.5, 2.85], [8.6, 3.05], [8.0, 3.1]], fc=SOFT, ec=INK, lw=0.7))
    ax.text(8.3, 1.6, "loose flake", fontsize=6.8, ha="center", va="bottom")
    ax.plot([8.25, 8.25], [1.95, 2.75], color=INK, lw=0.6)
    ax.annotate("", xy=(9.5, 5.3), xytext=(7.3, 5.3), arrowprops=dict(arrowstyle="-|>", lw=1.2))
    ax.text(5.0, 5.2, "harder body (sliding)", fontsize=7, ha="center", va="center")
    ax.text(5.0, 0.8, "softer body", fontsize=7, ha="center")
    ax.text(5.0, 6.45, "(a) adhesive: galling, scuffing", fontsize=8.3, ha="center", va="top", weight="bold")

    # (b) abrasive: two-body (left) and three-body (right)
    ax = axs[0, 1]
    xa = np.linspace(0.2, 4.7, 300)
    ax.fill_between(xa, 0, 2.2, color=SOFT, lw=0)
    # grooves / ploughing ridges in soft surface
    ys = np.full_like(xa, 2.2)
    ys -= 0.35 * np.exp(-((xa - 2.1) / 0.25) ** 2)
    ys += 0.15 * np.exp(-((xa - 1.65) / 0.12) ** 2) + 0.15 * np.exp(-((xa - 2.55) / 0.12) ** 2)
    ax.fill_between(xa, 0, ys, color=SOFT, lw=0)
    ax.fill_between(xa, ys, 2.2, where=ys > 2.2, color=SOFT, lw=0)
    ax.plot(xa, ys, color=INK, lw=0.8)
    # hard rough counterface with sharp asperities
    tooth_x = [0.2, 1.4, 2.1, 2.8, 3.6, 4.0, 4.7]
    top = [[0.2, 4.0]]
    for k, xx in enumerate(np.arange(0.2, 4.7, 0.9)):
        top += [[xx, 3.2], [xx + 0.45, 2.45 if abs(xx + 0.45 - 2.1) < 0.3 else 2.9], [xx + 0.9, 3.2]]
    top += [[4.7, 3.2], [4.7, 4.0]]
    ax.add_patch(Polygon(top, fc=HARD, ec=INK, lw=0.7))
    ax.annotate("", xy=(4.4, 4.4), xytext=(2.4, 4.4), arrowprops=dict(arrowstyle="-|>", lw=1.1))
    ax.annotate("ploughing\nridges", xy=(1.65, 2.33), xytext=(0.9, 1.1), fontsize=6.6, ha="center",
                arrowprops=dict(arrowstyle="-", lw=0.6))
    ax.add_patch(Polygon([[3.0, 2.2], [3.35, 2.75], [3.55, 2.55], [3.25, 2.2]], fc=SOFT, ec=INK, lw=0.6))
    ax.text(3.7, 1.6, "chip\n(microcutting)", fontsize=6.6, ha="center")
    ax.text(2.45, 5.0, "two-body", fontsize=7.5, ha="center", weight="bold")
    # three-body
    xb = np.linspace(5.3, 9.8, 200)
    ax.fill_between(xb, 0, 2.2, color=SOFT, lw=0)
    ax.plot(xb, np.full_like(xb, 2.2), color=INK, lw=0.8)
    ax.add_patch(Rectangle((5.3, 3.05), 4.5, 1.0, fc=HARD, ec=INK, lw=0.7))
    rng = np.random.default_rng(4)
    for xx in np.arange(5.6, 9.6, 0.62):
        rr = rng.uniform(0.3, 0.42)
        ang = rng.uniform(0, 1)
        poly = [[xx + rr * np.cos(a + ang), 2.62 + rr * np.sin(a + ang)] for a in np.linspace(0, 2 * np.pi, 6)[:-1]]
        ax.add_patch(Polygon(poly, fc="#555555", ec=INK, lw=0.5))
    ax.annotate("", xy=(9.6, 4.4), xytext=(7.6, 4.4), arrowprops=dict(arrowstyle="-|>", lw=1.1))
    ax.text(7.55, 5.0, "three-body", fontsize=7.5, ha="center", weight="bold")
    ax.text(7.55, 1.3, "loose hard particles\nroll and slide", fontsize=6.6, ha="center")
    ax.text(5.0, 5.75, "$H_{\\rm abrasive}/H_{\\rm surface}$ > 1.2: severe", fontsize=7.3, ha="center", va="center")
    ax.text(5.0, 6.45, "(b) abrasive", fontsize=8.3, ha="center", va="top", weight="bold")

    # (c) surface fatigue
    ax = axs[1, 0]
    ax.add_patch(Rectangle((0.2, 0.2), 9.6, 2.9, fc=STEEL, ec="none"))
    ax.plot([0.2, 9.8], [3.1, 3.1], color=INK, lw=0.8)
    ax.add_patch(Circle((4.0, 4.6), 1.5, fc="#D4D9DF", ec=INK, lw=0.9))
    ax.add_patch(Arc((4.0, 4.6), 1.8, 1.8, theta1=200, theta2=290, color=INK, lw=0.8))
    ax.annotate("", xy=(6.6, 4.6), xytext=(5.6, 4.6), arrowprops=dict(arrowstyle="-|>", lw=1.1))
    ax.text(6.1, 4.85, "rolling", fontsize=7, ha="center")
    # contact zone and depth of max shear
    ax.plot([3.55, 4.45], [3.1, 3.1], color=COLORS[1], lw=2.5)
    ax.plot([0.3, 9.7], [2.55, 2.55], color=COLORS[1], lw=0.8, ls="--")
    ax.text(0.35, 2.62, "z ≈ 0.5a: max shear", fontsize=6.6, color=COLORS[1], va="bottom")
    # subsurface crack growing parallel then branching up to spall
    ax.plot([5.6, 7.4], [2.55, 2.55], color=INK, lw=1.4)
    ax.plot([7.4, 7.9], [2.55, 3.1], color=INK, lw=1.4)
    ax.plot([5.6, 5.3], [2.55, 2.85], color=INK, lw=1.0)
    ax.add_patch(Circle((5.9, 2.55), 0.08, fc="#444444", ec="none"))
    ax.text(6.4, 2.3, "subsurface crack at inclusion", fontsize=6.6, ha="center", va="top")
    # spall pit further along
    ax.add_patch(Polygon([[8.3, 3.1], [8.5, 2.6], [9.3, 2.55], [9.5, 3.1]], fc="white", ec=INK, lw=0.9))
    ax.text(8.9, 3.25, "spall pit", fontsize=6.8, ha="center", va="bottom")
    ax.text(5.0, 1.1, "race", fontsize=7, ha="center")
    ax.text(5.0, 6.45, "(c) surface fatigue: RCF, pitting", fontsize=8.3, ha="center", va="top", weight="bold")

    # (d) tribochemical / fretting
    ax = axs[1, 1]
    # left: oxide film formed and scraped
    ax.add_patch(Rectangle((0.2, 0.6), 4.5, 2.4, fc=STEEL, ec="none"))
    ax.add_patch(Rectangle((0.2, 3.0), 4.5, 0.18, fc="#B5651D", ec="none"))
    ax.add_patch(Rectangle((2.3, 3.0), 1.4, 0.18, fc="white", ec="none"))
    ax.add_patch(Polygon([[2.4, 3.18], [2.4, 4.0], [3.8, 4.0], [3.8, 3.4], [3.0, 3.18]], fc=HARD, ec=INK, lw=0.7))
    ax.annotate("", xy=(1.6, 4.4), xytext=(3.4, 4.4), arrowprops=dict(arrowstyle="-|>", lw=1.0))
    for (px, py) in [(1.6, 3.35), (1.9, 3.5), (1.35, 3.6)]:
        ax.add_patch(Polygon([[px, py], [px + 0.18, py + 0.05], [px + 0.1, py + 0.16]], fc="#B5651D", ec="none"))
    ax.text(2.45, 2.0, "oxide forms between\npasses, scraped off\nas debris", fontsize=6.6, ha="center")
    # right: fretting joint
    ax.add_patch(Rectangle((5.3, 0.6), 4.5, 1.9, fc=STEEL, ec="none"))
    ax.add_patch(Rectangle((5.8, 2.75), 3.5, 1.4, fc=HARD, ec=INK, lw=0.7))
    rng = np.random.default_rng(9)
    for _ in range(26):
        px, py = rng.uniform(5.9, 9.2), rng.uniform(2.52, 2.72)
        ax.add_patch(Circle((px, py), 0.07, fc="#8B3A1A", ec="none"))
    ax.annotate("", xy=(8.0, 4.5), xytext=(7.1, 4.5), arrowprops=dict(arrowstyle="<|-|>", lw=1.0))
    ax.text(7.55, 4.75, "± 1–100 µm", fontsize=6.8, ha="center", va="bottom")
    ax.text(7.55, 1.4, "fretting: trapped oxide\ndebris, crack initiation", fontsize=6.6, ha="center")
    ax.text(5.0, 6.45, "(d) corrosive / tribochemical", fontsize=8.3, ha="center", va="top", weight="bold")
    save(fig, "45", "fig-45-4-wear-mechanisms")


# ---------------------------------------------------------------- Figure 45.5
def stribeck():
    Hn = np.logspace(0, 4, 600)                # Hersey number, arbitrary units
    lam = 0.25 * Hn ** 0.6                      # film parameter (calibrated)
    f = 1 / (1 + (lam / 1.6) ** 6)              # fraction of load carried by asperities
    mu_h = 0.0016 * (Hn / 120) ** 0.5
    mu = 0.10 * f + mu_h * (1 - f) + 0.0004
    fig = plt.figure(figsize=(6.6, 4.4))
    ax = fig.add_axes([0.11, 0.12, 0.85, 0.56])
    ax.loglog(Hn, mu, color=COLORS[0], lw=2.2)
    ax.set_xlim(1, 1e4); ax.set_ylim(1e-3, 0.3)
    ax.set_xlabel("Hersey number $\\eta N/P$ (arbitrary units)")
    ax.set_ylabel("Friction coefficient $\\mu$")
    to_l = lambda h: 0.25 * np.asarray(h) ** 0.6
    to_h = lambda l: (np.asarray(l) / 0.25) ** (1 / 0.6)
    H1, H3 = to_h(1), to_h(3)
    for Hx, lab in [(H1, "λ = 1"), (H3, "λ = 3")]:
        ax.axvline(Hx, color="#777777", ls="--", lw=0.9)
    ax.axvspan(1, H1, color=COLORS[1], alpha=0.08, lw=0)
    ax.axvspan(H1, H3, color=COLORS[4], alpha=0.10, lw=0)
    ax.axvspan(H3, 1e4, color=COLORS[2], alpha=0.08, lw=0)
    ax.text(np.sqrt(1 * H1), 0.2, "boundary", fontsize=8.5, ha="center", weight="bold", color="#8A3B00")
    ax.text(np.sqrt(H1 * H3), 0.2, "mixed", fontsize=8.5, ha="center", weight="bold", color="#7A5600")
    ax.text(np.sqrt(H3 * 1e4), 0.2, "hydrodynamic (full film)", fontsize=8.5, ha="center", weight="bold",
            color="#00704F")
    top = ax.secondary_xaxis("top", functions=(to_l, to_h))
    top.set_xlabel("film parameter λ", fontsize=8.5)
    top.set_xticks([0.3, 1, 3, 10, 30])
    top.set_xticklabels(["0.3", "1", "3", "10", "30"], fontsize=8)
    # example markers
    def mark(h, txt, dx, dy, ha="left"):
        m = np.interp(np.log(h), np.log(Hn), mu)
        ax.plot(h, m, "o", color=INK, ms=4.5, zorder=5)
        ax.annotate(txt, xy=(h, m), xytext=(h * dx, m * dy), fontsize=7.3, ha=ha, va="center",
                    arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
    mark(2.5, "piston ring at top\ndead centre (boundary)", 0.55, 0.3)
    mark(9.5, "engine valve train\n(boundary/mixed)", 4.0, 0.55)
    mark(2500, "crankshaft journal\nbearing (hydrodynamic)", 0.9, 3.2, ha="right")
    ax.annotate("EHL in rolling contacts:\nλ ≈ 1–3", xy=(np.sqrt(H1 * H3), 0.0016), xytext=(300, 0.0014),
                fontsize=7.3, ha="center", color="#7A5600", va="center",
                arrowprops=dict(arrowstyle="-", lw=0.6, color="#7A5600"))
    # inset sketches above the regions
    def sketch(x0, w, mode):
        s = fig.add_axes([x0, 0.80, w, 0.17])
        s.set_xlim(0, 10); s.set_ylim(0, 4); s.axis("off")
        xx = np.linspace(0, 10, 300)
        lower = _rough(xx, 1.0, 0.18, 3)
        if mode == "B":
            gapy = 0.0
        elif mode == "M":
            gapy = 0.35
        else:
            gapy = 1.0
        upper = _rough(xx, 2.0 + gapy, 0.18, 5)
        upper = np.maximum(upper, lower + 0.06) if mode != "H" else upper
        if mode == "H":
            upper = upper + np.linspace(0.6, -0.1, xx.size)
        s.fill_between(xx, 0, lower, color=STEEL, lw=0)
        s.fill_between(xx, upper, 4, color=STEEL, lw=0)
        s.fill_between(xx, lower, upper, color=OIL, lw=0)
        s.plot(xx, lower, color=INK, lw=0.7); s.plot(xx, upper, color=INK, lw=0.7)
        if mode == "B":
            for xc in np.arange(0.4, 10, 0.55):
                yv = np.interp(xc, xx, lower)
                s.plot([xc, xc], [yv, yv + 0.22], color=COLORS[1], lw=0.9)
        txt = {"B": "asperity contact,\nadsorbed films", "M": "partial film,\nsome contacts",
               "H": "fluid wedge,\nfull separation"}[mode]
        s.set_title(txt, fontsize=7, pad=1)
    bx0, bx1 = ax.get_position().x0, ax.get_position().x1
    pos = lambda h: bx0 + (np.log10(h) / 4) * (bx1 - bx0)
    sketch(pos(1) + 0.01, pos(H1) - pos(1) - 0.02, "B")
    sketch(pos(H1) + 0.005, pos(H3) - pos(H1) - 0.01, "M")
    sketch(pos(H3) + 0.10, 0.20, "H")
    save(fig, "45", "fig-45-5-stribeck-curve")


# ---------------------------------------------------------------- Figure 45.6
def carburizing():
    Cs, C0, D = 1.0, 0.20, 8.1e-12
    x = np.linspace(0, 2.5e-3, 500)
    fig = plt.figure(figsize=(6.8, 3.9))
    ax = fig.add_axes([0.08, 0.13, 0.56, 0.83])
    cols = [COLORS[2], COLORS[0], COLORS[3]]
    prof = {}
    for th, c in zip([3.2, 13, 30], cols):
        t = th * 3600
        C = C0 + (Cs - C0) * erfc(x / (2 * np.sqrt(D * t)))
        prof[th] = C
        ax.plot(x * 1e3, C, color=c, lw=2, label=f"C, {th:g} h at 925 °C")
    ax.axhline(0.40, color="#777777", ls="--", lw=0.9)
    z = erfinv(0.75)
    for th in (3.2, 13):
        d = 2 * z * np.sqrt(D * th * 3600) * 1e3
        ax.plot([d, d], [0, 0.40], color="#777777", ls=":", lw=0.9)
        ax.plot(d, 0.40, "o", color=INK, ms=4)
        ax.text(d + 0.03, 0.03, f"{d:.1f} mm", fontsize=7.5)
    ax.text(2.45, 0.42, "0.40 % C", fontsize=7.5, ha="right", va="bottom", color="#555555")
    ax.set_xlim(0, 2.5); ax.set_ylim(0, 1.1)
    ax.set_xlabel("Depth below surface (mm)")
    ax.set_ylabel("Carbon (wt %)")
    # hardness for 13 h case
    hx = ax.twinx()
    hx.spines["right"].set_visible(True)
    C13 = prof[13]
    s = np.clip((C13 - 0.20) / 0.45, 0, 1)
    HV = 350 + 400 / (1 + np.exp(-(C13 - 0.40) / 0.047))   # tempered martensite HV vs local carbon
    hx.plot(x * 1e3, HV, color=COLORS[1], lw=2.2, ls="-.", label="hardness, 13 h case (Q+T)")
    hx.axhline(550, color=COLORS[1], ls="--", lw=0.8)
    xe = np.interp(-550, -HV, x * 1e3)
    hx.plot(xe, 550, "s", color=COLORS[1], ms=5)
    hx.text(xe + 0.05, 560, f"effective case depth ≈ {xe:.1f} mm", fontsize=7.5, color=COLORS[1],
            va="bottom")
    hx.set_ylim(200, 800)
    hx.set_ylabel("Hardness (HV)", color=COLORS[1])
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = hx.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, loc="upper right", fontsize=7.6)
    # inset residual stress
    ins = fig.add_axes([0.81, 0.30, 0.18, 0.42])
    xd = np.linspace(0, 2.5, 200)
    rs = -300 * np.exp(-(xd / 0.9) ** 2) + 80 * (1 - np.exp(-(xd / 1.3) ** 2))
    ins.plot(xd, rs, color=INK, lw=1.5)
    ins.axhline(0, color="#888888", lw=0.6)
    ins.fill_between(xd, rs, 0, where=rs < 0, color=COLORS[0], alpha=0.2, lw=0)
    ins.set_xlim(0, 2.5); ins.set_ylim(-350, 150)
    ins.set_xlabel("depth (mm)", fontsize=7, labelpad=1)
    ins.set_ylabel("σ$_{res}$ (MPa)", fontsize=7, labelpad=1)
    ins.tick_params(labelsize=6.5)
    ins.text(0.1, -330, "compressive\ncase", fontsize=6.5, color=COLORS[0], va="bottom")
    ins.text(2.4, 115, "tensile core", fontsize=6.5, ha="right", va="center")
    ins.set_title("residual stress", fontsize=7.5, pad=3)
    ins.spines["top"].set_visible(True); ins.spines["right"].set_visible(True)
    save(fig, "45", "fig-45-6-carburized-case-profile")


if __name__ == "__main__":
    surface_tsk()
    wetting()
    hertz()
    wear_mechanisms()
    stribeck()
    carburizing()
