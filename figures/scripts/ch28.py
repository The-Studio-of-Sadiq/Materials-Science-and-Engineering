"""Figures for Chapter 28 — Magnetism in Materials.

Run from the repository root:  python figures/scripts/ch28.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, save, COLORS, INK
import itertools as it
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, FancyArrowPatch, Circle
from scipy.optimize import brentq


def langevin(x):
    x = np.asarray(x, float)
    out = np.empty_like(x)
    small = np.abs(x) < 1e-4
    out[small] = x[small] / 3
    xs = x[~small]
    out[~small] = 1 / np.tanh(xs) - 1 / xs
    return out


# ---------------------------------------------------------------- Figure 28.1
def langevin_function():
    fig, ax = new_fig(6.4, 3.8)
    x = np.linspace(0, 10, 1000)
    ax.axvspan(0, 0.1, color=COLORS[4], alpha=0.35, lw=0)
    ax.axhline(1, color="0.5", lw=0.9, ls="--")
    ax.plot(x, langevin(x), color=COLORS[0], label=r"Langevin $L(x)=\coth x-1/x$ (classical)")
    ax.plot(x, np.tanh(x), color=COLORS[1], ls="--", label=r"Brillouin $B_{1/2}(x)=\tanh x$")
    xl = np.linspace(0, 3, 50)
    ax.plot(xl, xl / 3, color=INK, ls=":", lw=1.6, label=r"low-field tangent $x/3$ (Curie law)")
    ax.text(9.9, 1.02, r"saturation $M/M_s=1$", ha="right", va="bottom", fontsize=9, color="0.3")
    ax.annotate("room temperature, 1 T:\n" + r"$x\approx0.01$ (shaded, $x<0.1$)",
                xy=(0.08, 0.04), xytext=(1.0, 0.18), fontsize=9,
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.9, mutation_scale=9))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1.12)
    ax.set_xlabel(r"$x=\mu_0 m H/k_BT$")
    ax.set_ylabel(r"$M/M_s$")
    ax.legend(loc="lower right", fontsize=9)
    save(fig, "28", "fig-28-1-langevin-function")


# ---------------------------------------------------------------- Figure 28.2
def mean_field_ms(t):
    """Self-consistent M/Ms(0) for J = 1/2: m = tanh(m/t)."""
    if t >= 1:
        return 0.0
    return brentq(lambda m: m - np.tanh(m / t), 1e-9, 1.0 + 1e-12)


def kuzmin(t, s, p):
    """Kuz'min (2005) fit to measured Ms(T): m = [1 - s t^1.5 - (1-s) t^p]^(1/3)."""
    v = 1 - s * t**1.5 - (1 - s) * t**p
    return np.cbrt(np.clip(v, 0, None))


def ms_and_inverse_chi():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.8, 3.9), gridspec_kw=dict(wspace=0.32))
    # (a)
    t = np.linspace(0.005, 0.99999, 400)
    m = np.array([mean_field_ms(ti) for ti in t])
    ax1.plot(np.r_[0, t, 1, 1.1], np.r_[1, m, 0, 0], color=INK, label=r"mean field, $J=\frac{1}{2}$")
    tp = np.array([0.1, 0.25, 0.4, 0.55, 0.7, 0.8, 0.88, 0.94, 0.98])
    ax1.plot(tp, kuzmin(tp, 0.35, 4.0), "o", color=COLORS[0], ms=5, label="Fe")
    ax1.plot(tp + 0.012, kuzmin(tp + 0.012, 0.15, 2.5), "s", color=COLORS[1], ms=4.5, label="Ni")
    ax1.text(0.04, 0.6, "Bloch $T^{3/2}$\nat low $T$", fontsize=8.5, color="0.25")
    ax1.annotate("", xy=(0.12, 0.97), xytext=(0.15, 0.72),
                 arrowprops=dict(arrowstyle="-|>", color="0.3", lw=0.8, mutation_scale=8))
    ax1.axvspan(0.95, 1.0, color=COLORS[4], alpha=0.3, lw=0)
    ax1.text(0.93, 0.1, "critical\nregion\nnear $T_C$", fontsize=8.5, ha="right", color="0.25")
    ax1.set_xlim(0, 1.1)
    ax1.set_ylim(0, 1.08)
    ax1.set_xlabel(r"$T/T_C$")
    ax1.set_ylabel(r"$M_s(T)/M_s(0)$")
    ax1.legend(loc="lower left", bbox_to_anchor=(0.0, 0.08), fontsize=8.5)
    ax1.set_title("(a)", loc="left", fontsize=10)

    # (b) 1/chi in arbitrary units, same Curie constant for all three
    TC, TN, th = 630.0, 400.0, 500.0
    T = np.linspace(0, 1200, 300)
    ax2.axvspan(0, TC, color=COLORS[0], alpha=0.08, lw=0)
    ax2.plot(T, T, color=COLORS[2])
    Tf = T[T >= TC]
    ax2.plot(Tf, Tf - TC, color=COLORS[0])
    ax2.plot([TC - 120, TC], [-120, 0], color=COLORS[0], ls=":", lw=1)
    Ta = T[T >= TN]
    ax2.plot(Ta, Ta + th, color=COLORS[1])
    ax2.plot([-th, TN], [0, TN + th], color=COLORS[1], ls=":", lw=1)
    ax2.plot([TN], [TN + th], "o", color=COLORS[1], ms=4)
    ax2.plot([-th], [0], "o", color=COLORS[1], ms=4, mfc="white")
    ax2.plot([TC], [0], "o", color=COLORS[0], ms=4, mfc="white")
    ax2.text(TN + 40, TN + th - 40, r"$T_N$", color=COLORS[1], fontsize=9, va="top")
    ax2.text(TC + 30, -40, r"$\theta\approx T_C$", color=COLORS[0], fontsize=9, va="top")
    ax2.text(-th, -40, r"$-\theta$", color=COLORS[1], fontsize=9, va="top", ha="center")
    ax2.text(1180, 1540, "antiferro-\nmagnet", color=COLORS[1], fontsize=8.5, ha="right", va="top")
    ax2.text(1180, 1010, "paramagnet\n(Curie)", color=COLORS[2], fontsize=8.5, ha="right", va="top")
    ax2.text(1180, 430, "ferro-\nmagnet", color=COLORS[0], fontsize=8.5, ha="right", va="top")
    ax2.text(TC / 2, 1720, "ferromagnetic\n" + r"($T<T_C$)", ha="center", va="top", fontsize=8.5, color=COLORS[0])
    ax2.axhline(0, color=INK, lw=0.6)
    ax2.axvline(0, color=INK, lw=0.6)
    ax2.spines["left"].set_visible(False)
    ax2.set_xlim(-600, 1200)
    ax2.set_ylim(-250, 1800)
    ax2.set_xticks([-500, 0, 400, 800, 1200])
    ax2.set_yticks([])
    ax2.set_xlabel(r"$T$ (K)")
    ax2.set_ylabel(r"$1/\chi$ (arb. units)")
    ax2.set_title("(b)", loc="left", fontsize=10)
    # inset: chi(T) of the antiferromagnet
    ins = ax2.inset_axes([0.04, 0.6, 0.25, 0.27])
    chiN = 1 / (TN + th)
    Tab = np.linspace(TN, 1200, 100)
    ins.plot(Tab, 1 / (Tab + th), color=COLORS[1], lw=1.3)
    Tb = np.linspace(0, TN, 100)
    tt = Tb / TN
    chipar = chiN * (1 - np.exp(-3.0 * tt**2)) / (1 - np.exp(-3.0))
    ins.plot(Tb, chipar, color=COLORS[1], lw=1.3, ls="--")
    ins.plot(Tb, np.full_like(Tb, chiN), color=COLORS[1], lw=1.3, ls="-.")
    ins.text(30, chiN * 1.04, r"$\chi_\perp$", fontsize=8, va="bottom")
    ins.text(330, chiN * 0.2, r"$\chi_\parallel$", fontsize=8, ha="left")
    ins.set_xlim(0, 1200)
    ins.set_ylim(0, chiN * 1.4)
    ins.set_xticks([TN])
    ins.set_xticklabels([r"$T_N$"], fontsize=8)
    ins.set_yticks([])
    ins.set_ylabel(r"$\chi$", fontsize=8, labelpad=1)
    ins.set_title(r"AFM $\chi(T)$", fontsize=8, pad=2)
    save(fig, "28", "fig-28-2-ms-and-inverse-chi")


# ---------------------------------------------------------------- Figure 28.3
def _spinel_sites():
    """Ideal spinel (u = 3/8, origin choice 1: A at 0,0,0), fractional coords in eighths."""
    F = [(0, 0, 0), (0, 4, 4), (4, 0, 4), (4, 4, 0)]
    A = {tuple((np.array(b) + f) % 8) for b in [(0, 0, 0), (6, 2, 2)] for f in F}
    Bb = [(3, 3, 3), (1, 5, 7), (5, 7, 1), (7, 1, 5)]
    B = {tuple((np.array(b) + f) % 8) for b in Bb for f in F}
    O = set()
    for p in it.product(range(4), repeat=3):
        if sorted(q % 2 for q in p) in ([1, 1, 1], [0, 0, 1]):
            O.add(tuple((2 * np.array(p) - 1) % 8))
    return A, B, O


def spinel_sublattices():
    A, B, O = _spinel_sites()

    def images(S, lo, hi):
        pts = []
        for p in S:
            for sh in it.product((-8, 0, 8), repeat=3):
                q = np.array(p) + np.array(sh)
                if np.all(q >= np.array(lo) - 1e-9) and np.all(q <= np.array(hi) + 1e-9):
                    pts.append(q)
        return pts

    lo, hi = (0, 0, 0), (8, 4, 4)       # two adjacent octants along x
    Ain = images(A, lo, hi)
    Bin = images(B, lo, hi)
    Oin = images(O, (-1, -1, -1), (9, 5, 5))

    # orthographic view
    az, el = np.radians(-60), np.radians(22)
    R1 = np.array([[np.cos(az), -np.sin(az), 0], [np.sin(az), np.cos(az), 0], [0, 0, 1]])
    R2 = np.array([[1, 0, 0], [0, np.cos(el), -np.sin(el)], [0, np.sin(el), np.cos(el)]])
    Rm = R2 @ np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]]) @ R1  # x->screen-ish

    def P(p):
        v = Rm @ (np.asarray(p, float) - np.array([4, 2, 2]))
        return v[0], v[1], v[2]

    fig = plt.figure(figsize=(6.8, 3.9))
    ax = fig.add_axes([0.0, 0.0, 0.58, 1.0])
    ax.set_aspect("equal")
    ax.axis("off")
    # cube edges of both octants
    for x0 in (0, 4):
        corners = np.array(list(it.product((x0, x0 + 4), (0, 4), (0, 4))))
        for i, j in it.combinations(range(8), 2):
            if np.sum(np.abs(corners[i] - corners[j]) > 0) == 1:
                a, b = P(corners[i]), P(corners[j])
                ax.plot([a[0], b[0]], [a[1], b[1]], color="0.55", lw=0.8, zorder=1)

    items = []
    # A at centre of the right octant (6,2,2): tetrahedral bonds
    ac = np.array([6, 2, 2])
    tet = [q for q in Oin if np.isclose(np.linalg.norm(q - ac), np.sqrt(3))]
    # one B at (3,3,3): octahedral bonds
    bc = np.array([3, 3, 3])
    octa = [q for q in Oin if np.isclose(np.linalg.norm(q - bc), 2.0)]
    for q in tet:
        items.append(("bond", ac, q, COLORS[0]))
    for q in octa:
        items.append(("bond", bc, q, COLORS[1]))
    Oshow = [q for q in Oin if np.all(q >= -1e-9) and np.all(q <= np.array(hi) + 1e-9)]
    extra = [q for q in octa + tet if not any(np.allclose(q, o) for o in Oshow)]
    for q in Oshow:
        items.append(("O", q))
    for q in extra:
        items.append(("Ox", q))
    for q in Ain:
        items.append(("A", q))
    for q in Bin:
        items.append(("B", q))

    def depth(it_):
        if it_[0] == "bond":
            return (P(it_[1])[2] + P(it_[2])[2]) / 2 - 0.01
        return P(it_[1])[2]

    for k, itm in enumerate(sorted(items, key=depth)):
        kind = itm[0]
        zz = 2 + 0.01 * k
        if kind == "bond":
            a, b = np.array(P(itm[1])[:2]), np.array(P(itm[2])[:2])
            d = b - a
            ln = max(np.hypot(*d), 1e-6)
            a2 = a + d * min(0.27 / ln, 0.45)
            b2 = b - d * min(0.46 / ln, 0.45)
            ax.plot([a2[0], b2[0]], [a2[1], b2[1]], color=itm[3], lw=2.4, zorder=zz, solid_capstyle="butt")
            continue
        x, y, _ = P(itm[1])
        if kind == "O":
            ax.add_patch(Circle((x, y), 0.46, fc="white", ec=INK, lw=1.1, zorder=zz))
        elif kind == "Ox":
            ax.add_patch(Circle((x, y), 0.46, fc="white", ec="0.6", lw=0.9, ls="--", zorder=zz))
        elif kind == "A":
            ax.add_patch(Circle((x, y), 0.27, fc=COLORS[0], ec=INK, lw=0.8, zorder=zz))
        elif kind == "B":
            ax.add_patch(Circle((x, y), 0.27, fc="#F4B183", ec=INK, lw=0.8, zorder=zz))
    allp = np.array([P(q)[:2] for q in Oin])
    for c, lab, dx, dy in ((ac, "A site:\n4 O (tetrahedral)", -1.6, -2.9), (bc, "B site:\n6 O (octahedral)", 3.0, 2.6)):
        x0, y0, _ = P(c)
        ax.annotate(lab, xy=(x0, y0), xytext=(x0 + dx, y0 + dy), fontsize=8.5, ha="center",
                    va="top" if dy < 0 else "bottom", zorder=20,
                    arrowprops=dict(arrowstyle="-", color="0.3", lw=0.8, shrinkB=4))
    ax.set_xlim(allp[:, 0].min() - 1.0, allp[:, 0].max() + 1.0)
    ax.set_ylim(allp[:, 1].min() - 2.6, allp[:, 1].max() + 0.8)
    yb = allp[:, 1].min() - 1.6
    xb = allp[:, 0].min() - 0.3
    ax.add_patch(Circle((xb, yb), 0.45, fc="white", ec=INK, lw=1.1))
    ax.text(xb + 0.7, yb, r"O$^{2-}$", va="center", fontsize=9)
    ax.add_patch(Circle((xb + 3.4, yb), 0.33, fc=COLORS[0], ec=INK, lw=0.8))
    ax.text(xb + 3.9, yb, "A (tetra)", va="center", fontsize=9)
    ax.add_patch(Circle((xb + 7.6, yb), 0.33, fc="#F4B183", ec=INK, lw=0.8))
    ax.text(xb + 8.1, yb, "B (octa)", va="center", fontsize=9)
    ax.text(allp[:, 0].mean(), allp[:, 1].max() + 0.4, r"two octants of the spinel cell, $a\approx0.84$ nm",
            ha="center", fontsize=9)

    # right: moment bar diagrams
    bx = fig.add_axes([0.6, 0.06, 0.4, 0.88])
    bx.set_xlim(0, 10)
    bx.set_ylim(-6.5, 11)
    bx.axis("off")
    bx.axhline(0, xmin=0.02, xmax=0.98, color="0.6", lw=0.7)

    def moment(x, y0, L, color, label, side="right"):
        bx.add_patch(FancyArrowPatch((x, y0), (x, y0 + L), arrowstyle="-|>", mutation_scale=12,
                                     lw=2.2, color=color, shrinkA=0, shrinkB=0))
        if label:
            bx.text(x + (0.25 if side == "right" else -0.25), y0 + L / 2, label, fontsize=8,
                    ha="left" if side == "right" else "right", va="center")

    bx.text(2.4, 10.4, r"Fe$_3$O$_4$", ha="center", fontsize=9.5, weight="bold")
    moment(0.7, 0, -5, COLORS[0], "A: Fe$^{3+}$\n5", side="right")
    moment(2.2, 0, 5, COLORS[1], "B: Fe$^{3+}$\n5")
    moment(3.4, 5, 4, COLORS[1], "B: Fe$^{2+}$\n4")
    moment(4.3, 0, 4, INK, "")
    bx.text(4.3, 4.4, r"net $4\mu_B$", ha="center", fontsize=8.5, weight="bold")

    x = 0.3
    bx.text(7.6, 10.4, r"Ni$_{1-x}$Zn$_x$Fe$_2$O$_4$", ha="center", fontsize=9.5, weight="bold")
    mA = 5 * (1 - x)
    moment(6.0, 0, -mA, COLORS[0], "A: Fe$^{3+}_{1-x}$\n" + f"{mA:.1f}")
    mB1, mB2 = 5 * (1 + x), 2 * (1 - x)
    moment(7.6, 0, mB1, COLORS[1], "B: Fe$^{3+}_{1+x}$\n" + f"{mB1:.1f}")
    moment(8.8, mB1, mB2, COLORS[1], "B: Ni$^{2+}$\n" + f"{mB2:.1f}")
    net = 2 + 8 * x
    moment(9.7, 0, net, INK, "")
    bx.text(9.7, net + 0.35, "net\n" + rf"${net:.1f}\mu_B$", ha="center", fontsize=8.5, weight="bold")
    bx.text(7.6, -6.3, r"$x=0.3$ shown: net $=2+8x$" + "\n(Zn$^{2+}$ on A, no moment)",
            ha="center", fontsize=8, color="0.25")
    bx.text(2.4, -6.3, r"moments in $\mu_B$" + "\nper formula unit", ha="center", fontsize=8, color="0.25")
    save(fig, "28", "fig-28-3-spinel-sublattices")


# ---------------------------------------------------------------- Figure 28.4
def domain_subdivision():
    W, Hh = 1.4, 2.0
    gap = 1.25
    fig, ax = schematic(6.8, 3.7, xlim=(-0.6, 4 * W + 3 * gap + 0.6), ylim=(-1.75, Hh + 0.85))
    xs = [i * (W + gap) for i in range(4)]
    dom_fc = ["#DCE9F5", "#F8E0CF"]

    def darrow(x, y0, y1, color=INK, lw=1.6):
        ax.add_patch(FancyArrowPatch((x, y0), (x, y1), arrowstyle="-|>", mutation_scale=11,
                                     lw=lw, color=color, shrinkA=0, shrinkB=0, zorder=5))

    def loop(x0, x1, ytop, h, color="0.35"):
        """Field line leaving top at x0 and entering at x1 (top side, arc of height h)."""
        t = np.linspace(0, np.pi, 60)
        xc, r = (x0 + x1) / 2, (x1 - x0) / 2
        ax.plot(xc - r * np.cos(t), ytop + h * np.sin(t), color=color, lw=0.9)
        # arrowhead at the apex pointing from x0 to x1
        ax.annotate("", xy=(xc + 0.02 * np.sign(x1 - x0), ytop + h), xytext=(xc - 0.02 * np.sign(x1 - x0), ytop + h),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=0.8, mutation_scale=7))

    # (a) single domain, field lines loop from top (N) round to bottom (S)
    x = xs[0]
    ax.add_patch(Rectangle((x, 0), W, Hh, fc=dom_fc[0], ec=INK, lw=1.0))
    darrow(x + W / 2, 0.3, Hh - 0.3, lw=2.2)
    ax.text(x + 0.1, Hh - 0.08, "N", ha="left", va="top", fontsize=9, weight="bold")
    ax.text(x + 0.1, 0.08, "S", ha="left", va="bottom", fontsize=9, weight="bold")
    for k, s in enumerate((0.25, 0.5)):
        for side in (-1, 1):
            xa = x + W / 2 + side * (0.15 + 0.15 * k)
            xo = x + W / 2 + side * (W / 2 + s)
            # leave the top face vertically, swing outside, enter the bottom face vertically
            ang = np.linspace(0, np.pi, 80)
            px = xa + (xo - xa) * np.sin(ang) ** 0.4
            cs = np.cos(ang)
            py = Hh / 2 + (Hh / 2 + 0.2 + 0.18 * k) * np.sign(cs) * np.abs(cs) ** 0.4
            px = np.r_[xa, px, xa]
            py = np.r_[Hh, py, 0]
            ax.plot(px, py, color="0.35", lw=0.9)
            i = 41
            ax.annotate("", xy=(px[i + 1], py[i + 1]), xytext=(px[i - 1], py[i - 1]),
                        arrowprops=dict(arrowstyle="-|>", color="0.35", lw=0.8, mutation_scale=7))

    # (b) two domains
    x = xs[1]
    for j in range(2):
        ax.add_patch(Rectangle((x + j * W / 2, 0), W / 2, Hh, fc=dom_fc[j], ec=INK, lw=1.0))
    darrow(x + W / 4, 0.3, Hh - 0.3, lw=2.0)
    darrow(x + 3 * W / 4, Hh - 0.3, 0.3, lw=2.0)
    loop(x + W / 4, x + 3 * W / 4, Hh, 0.35)
    loop(x + 3 * W / 4, x + W / 4, 0, -0.35)
    # (c) four stripes
    x = xs[2]
    for j in range(4):
        ax.add_patch(Rectangle((x + j * W / 4, 0), W / 4, Hh, fc=dom_fc[j % 2], ec=INK, lw=1.0))
        xc = x + (j + 0.5) * W / 4
        if j % 2 == 0:
            darrow(xc, 0.3, Hh - 0.3, lw=1.8)
        else:
            darrow(xc, Hh - 0.3, 0.3, lw=1.8)
    for j in (0, 2):
        loop(x + (j + 0.5) * W / 4, x + (j + 1.5) * W / 4, Hh, 0.17)
        loop(x + (j + 1.5) * W / 4, x + (j + 0.5) * W / 4, 0, -0.17)
    # (d) two slabs + closure triangles
    x = xs[3]
    h2 = W / 2
    top = Polygon([(x, Hh), (x + W, Hh), (x + W / 2, Hh - h2)], closed=True, fc="#E3F1E6", ec=INK, lw=1.0)
    bot = Polygon([(x, 0), (x + W, 0), (x + W / 2, h2)], closed=True, fc="#E3F1E6", ec=INK, lw=1.0)
    left = Polygon([(x, 0), (x + W / 2, h2), (x + W / 2, Hh - h2), (x, Hh)], closed=True, fc=dom_fc[0], ec=INK, lw=1.0)
    right = Polygon([(x + W, 0), (x + W / 2, h2), (x + W / 2, Hh - h2), (x + W, Hh)], closed=True, fc=dom_fc[1], ec=INK, lw=1.0)
    for p in (left, right, top, bot):
        ax.add_patch(p)
    darrow(x + W / 4, 0.55, Hh - 0.55, lw=1.8)
    darrow(x + 3 * W / 4, Hh - 0.55, 0.55, lw=1.8)
    ax.add_patch(FancyArrowPatch((x + 0.3, Hh - 0.17), (x + W - 0.3, Hh - 0.17), arrowstyle="-|>",
                                 mutation_scale=10, lw=1.6, color=INK, zorder=5))
    ax.add_patch(FancyArrowPatch((x + W - 0.3, 0.17), (x + 0.3, 0.17), arrowstyle="-|>",
                                 mutation_scale=10, lw=1.6, color=INK, zorder=5))

    labels = ["(a) $E_{ms}$ large,\nno wall energy",
              "(b) $E_{ms}$ about\nhalved, one wall",
              "(c) $E_{ms}$ small,\nthree walls",
              "(d) $E_{ms}\\approx0$; walls +\nsmall magnetoelastic\nenergy of closure\ndomains"]
    for x, lab in zip(xs, labels):
        ax.text(x + W / 2, -0.62, lab, ha="center", va="top", fontsize=8.5)
    save(fig, "28", "fig-28-4-domain-subdivision")


# ---------------------------------------------------------------- Figure 28.5
def bloch_wall():
    fig = plt.figure(figsize=(6.8, 4.8))
    # top: arrows
    ax = fig.add_axes([0.02, 0.56, 0.96, 0.42])
    ax.set_xlim(-6.2, 6.2)
    ax.set_ylim(-2.12, 1.45)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.axvspan(-np.pi / 2, np.pi / 2, color=COLORS[4], alpha=0.25, lw=0)
    ax.text(0, 1.33, r"wall, width $\delta=\pi\Delta$", ha="center", fontsize=9)
    xs = np.linspace(-5.6, 5.6, 15)
    L = 1.0
    ox, oy = -0.55, -0.38        # oblique direction for "out of page" (z)
    for xv in xs:
        th = 2 * np.arctan(np.exp(xv))
        dy, dz = L * np.cos(th), L * np.sin(th)
        tipx, tipy = xv + dz * ox, dy + dz * oy
        tailx, taily = xv - 0.5 * (tipx - xv), -0.5 * (tipy)
        ax.add_patch(FancyArrowPatch((xv - 0.5 * dz * ox, -0.5 * dy - 0.5 * dz * oy),
                                     (xv + 0.5 * dz * ox, 0.5 * dy + 0.5 * dz * oy),
                                     arrowstyle="-|>", mutation_scale=11, lw=1.8,
                                     color=COLORS[0] if dy > 0.05 else (COLORS[1] if dy < -0.05 else COLORS[2]),
                                     shrinkA=0, shrinkB=0))
        ax.plot([xv], [0], "o", ms=2, color="0.4")
    ax.text(-5.9, -0.82, "domain 1: $M$ up", fontsize=8.5, ha="left")
    ax.text(5.9, -0.82, "domain 2: $M$ down", fontsize=8.5, ha="right")
    # axes triad
    cx, cy = -5.5, -1.75
    ax.annotate("", xy=(cx + 0.55, cy), xytext=(cx, cy), arrowprops=dict(arrowstyle="-|>", lw=0.8, color="0.3"))
    ax.annotate("", xy=(cx, cy + 0.45), xytext=(cx, cy), arrowprops=dict(arrowstyle="-|>", lw=0.8, color="0.3"))
    ax.annotate("", xy=(cx + 0.7 * ox, cy + 0.7 * oy), xytext=(cx, cy),
                arrowprops=dict(arrowstyle="-|>", lw=0.8, color="0.3"))
    ax.text(cx + 0.6, cy, "$x$", fontsize=8, va="center")
    ax.text(cx + 0.05, cy + 0.45, "$y$", fontsize=8)
    ax.text(cx + 0.75 * ox - 0.05, cy + 0.75 * oy, "$z$", fontsize=8, ha="right", va="top")
    ax.text(-4.2, -1.75, "$M$ rotates in the $y$–$z$ plane of the wall; at the centre it points out of the page ($z$)",
            fontsize=8, va="center", ha="left", color="0.25")

    # bottom: theta(x)
    bx = fig.add_axes([0.1, 0.09, 0.52, 0.4])
    u = np.linspace(-5, 5, 400)
    th = np.degrees(2 * np.arctan(np.exp(u)))
    bx.axvspan(-np.pi / 2, np.pi / 2, color=COLORS[4], alpha=0.25, lw=0)
    bx.plot(u, th, color=COLORS[0])
    ut = np.linspace(-np.pi / 2 - 0.6, np.pi / 2 + 0.6, 10)
    bx.plot(ut, 90 + np.degrees(ut), color=INK, ls="--", lw=1)
    bx.axhline(0, color="0.6", lw=0.7)
    bx.axhline(180, color="0.6", lw=0.7)
    bx.annotate("", xy=(np.pi / 2, 20), xytext=(-np.pi / 2, 20),
                arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=0.9, mutation_scale=8))
    bx.text(0, 26, r"$\delta=\pi\Delta$", ha="center", fontsize=9)
    bx.text(-4.8, 150, r"$\theta=2\arctan(e^{x/\Delta})$" + "\n" + r"$\Delta=\sqrt{A/K}$", fontsize=9)
    bx.set_xlim(-5, 5)
    bx.set_ylim(-5, 190)
    bx.set_yticks([0, 45, 90, 135, 180])
    bx.set_xlabel(r"$x/\Delta$")
    bx.set_ylabel(r"$\theta$ (degrees)")

    # side table
    tx = fig.add_axes([0.66, 0.09, 0.33, 0.4])
    tx.axis("off")
    rows = [("Material", r"$\delta=\pi\sqrt{A/K}$"),
            ("Fe", "≈ 66 nm"),
            ("Nd$_2$Fe$_{14}$B", "≈ 4 nm"),
            ("Permalloy", "order of µm")]
    for i, (a, b) in enumerate(rows):
        y = 0.85 - i * 0.2
        w = "bold" if i == 0 else "normal"
        tx.text(0.02, y, a, fontsize=9, weight=w, va="center")
        tx.text(0.58, y, b, fontsize=9, weight=w, va="center")
    tx.plot([0, 1], [0.75, 0.75], color=INK, lw=0.7)
    tx.set_xlim(0, 1)
    tx.set_ylim(0, 1)
    save(fig, "28", "fig-28-5-bloch-wall")


# ---------------------------------------------------------------- Figure 28.6
def hysteresis_loop():
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.8, 4.0), gridspec_kw=dict(width_ratios=[1.45, 1], wspace=0.3))
    Bs = 1.6
    w = 1 / 1.2
    h = np.linspace(-3, 3, 600)
    up = Bs * np.tanh((h + 1) / w)     # descending branch (coming from +Hs)
    lo = Bs * np.tanh((h - 1) / w)     # ascending branch
    ax.fill_between(h, lo, up, color=COLORS[0], alpha=0.12, lw=0)
    ax.plot(h, up, color=COLORS[0])
    ax.plot(h, lo, color=COLORS[0])
    Br = Bs * np.tanh(1 / w)
    # initial curve: Rayleigh near origin, joining the loop at high field
    hi = np.linspace(0, 3, 300)
    ini = Bs * np.tanh(0.3 * hi + 0.9 * hi**2)
    ax.plot(hi, ini, color=INK, ls="--", lw=1.4)
    # minor (Rayleigh) loop at Hm = 0.5 Hc whose tips lie on the initial curve
    Hm = 0.5
    Bm = Bs * np.tanh(0.3 * Hm + 0.9 * Hm**2)
    a = 0.3 * Bs
    eta = (Bm / Hm - a) / Hm
    hm = np.linspace(-Hm, Hm, 100)
    ax.plot(hm, (a + eta * Hm) * hm + eta / 2 * (Hm**2 - hm**2), color=COLORS[1], lw=1.3)
    ax.plot(hm, (a + eta * Hm) * hm - eta / 2 * (Hm**2 - hm**2), color=COLORS[1], lw=1.3)
    ax.text(-0.6, -0.72, "minor loop", fontsize=8, color=COLORS[1], ha="center")
    # key points
    ax.plot([0, 0], [Br, -Br], "o", color=INK, ms=4)
    ax.plot([-1, 1], [0, 0], "o", color=INK, ms=4)
    ax.text(-0.12, Br + 0.08, r"$B_r$", ha="right", fontsize=9.5)
    ax.text(0.12, -Br - 0.12, r"$-B_r$", ha="left", va="top", fontsize=9.5)
    ax.text(-1.08, 0.08, r"$-H_c$", ha="right", fontsize=9.5)
    ax.text(1.1, -0.18, r"$H_c$", ha="left", fontsize=9.5)
    ax.axhline(Bs, color="0.6", lw=0.7, ls=":")
    ax.axhline(-Bs, color="0.6", lw=0.7, ls=":")
    ax.text(-2.95, Bs + 0.05, r"$B_s$", fontsize=9.5, va="bottom")
    ax.text(2.95, -Bs - 0.05, r"$-B_s$", fontsize=9.5, va="top", ha="right")
    # initial curve regions
    ax.annotate("reversible wall\nbowing ($\\mu_i$)", xy=(0.25, Bs * np.tanh(0.3 * .25 + .9 * .0625)),
                xytext=(1.2, -0.85), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
    ax.annotate("irreversible\njumps ($\\mu_{max}$)", xy=(0.82, Bs * np.tanh(0.3 * .82 + .9 * .82**2)),
                xytext=(1.55, 0.35), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
    ax.annotate("rotation", xy=(1.9, Bs * np.tanh(0.3 * 1.9 + .9 * 1.9**2)),
                xytext=(2.0, 1.05), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
    ax.text(-0.65, -1.15, "W = ∮H dB\nper cycle", ha="center", va="center", fontsize=8.5, color=COLORS[0])
    ax.axhline(0, color=INK, lw=0.6)
    ax.axvline(0, color=INK, lw=0.6)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-1.95, 1.95)
    ax.set_xlabel(r"$H/H_c$")
    ax.set_ylabel(r"$B$ (T)")
    ax.set_title("(a)", loc="left", fontsize=10)
    # Barkhausen inset
    ins = ax.inset_axes([0.04, 0.55, 0.27, 0.28])
    rng = np.random.default_rng(3)
    steps_h = np.sort(rng.uniform(0, 1, 14))
    steps_b = np.cumsum(rng.exponential(1, 14))
    steps_b /= steps_b[-1]
    ins.step(np.r_[0, steps_h, 1], np.r_[0, steps_b, 1], where="post", color=INK, lw=0.9)
    ins.plot([0, 1], [0, 1], color=COLORS[0], lw=0.8, ls=":")
    ins.set_xticks([])
    ins.set_yticks([])
    ins.set_title("Barkhausen jumps", fontsize=7, pad=2)
    for s in ("top", "right"):
        ins.spines[s].set_visible(True)

    # (b) soft vs hard
    hs = np.linspace(-40, 40, 400)
    soft = 1.0 * np.tanh((hs + 10) / 3), 1.0 * np.tanh((hs - 10) / 3)
    bx.plot(hs, soft[0], color=COLORS[2])
    bx.plot(hs, soft[1], color=COLORS[2])
    bx.set_xlim(-40, 40)
    bx.set_xlabel(r"$H$ (A/m), soft", color=COLORS[2])
    bx.tick_params(axis="x", colors=COLORS[2])
    bx.set_ylim(-1.95, 1.95)
    bx.set_ylabel(r"$B$ or $J$ (T)")
    bx2 = bx.twiny()
    Hh_ = np.linspace(-4, 4, 400)
    hard_dn = 1.3 * np.tanh((Hh_ + 1.0) / 0.08)
    hard_up = 1.3 * np.tanh((Hh_ - 1.0) / 0.08)
    bx2.plot(Hh_, hard_dn, color=COLORS[3])
    bx2.plot(Hh_, hard_up, color=COLORS[3])
    bx2.set_xlim(-4, 4)
    bx2.spines["top"].set_visible(True)
    bx2.set_xlabel(r"$H$ (MA/m), hard ($J$ loop)", color=COLORS[3])
    bx2.tick_params(axis="x", colors=COLORS[3])
    bx.axhline(0, color=INK, lw=0.6)
    bx.axvline(0, color=INK, lw=0.6)
    bx.text(-38, 1.55, "soft:\n$H_c\\approx10$ A/m", fontsize=8, color=COLORS[2])
    bx.text(38, -1.55, "hard:\n$H_c\\approx1$ MA/m", fontsize=8, color=COLORS[3], ha="right", va="bottom")
    bx.text(0.5, 0.02, "x-scales differ by $10^5$", transform=bx.transAxes, fontsize=7.5,
            ha="center", color="0.3")
    bx.set_title("(b)", loc="left", fontsize=10, pad=24)
    save(fig, "28", "fig-28-6-hysteresis-loop")


if __name__ == "__main__":
    langevin_function()
    ms_and_inverse_chi()
    spinel_sublattices()
    domain_subdivision()
    bloch_wall()
    hysteresis_loop()
