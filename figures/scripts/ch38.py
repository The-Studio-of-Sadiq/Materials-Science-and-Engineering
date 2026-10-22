"""Figures for Chapter 38 — Nanomaterials and Two-Dimensional Materials.

Run from the repository root:  python figures/scripts/ch38.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from math import gcd
from matplotlib.patches import Circle, Rectangle, RegularPolygon, Polygon, FancyArrowPatch, Ellipse
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D
from scipy.interpolate import PchipInterpolator
from scipy.spatial import cKDTree


def wavelength_rgb(nm):
    """Approximate visible-spectrum colour for a wavelength in nm (Bruton's piecewise model)."""
    w = float(nm)
    if 380 <= w < 440:
        r, g, b = -(w - 440) / 60, 0.0, 1.0
    elif 440 <= w < 490:
        r, g, b = 0.0, (w - 440) / 50, 1.0
    elif 490 <= w < 510:
        r, g, b = 0.0, 1.0, -(w - 510) / 20
    elif 510 <= w < 580:
        r, g, b = (w - 510) / 70, 1.0, 0.0
    elif 580 <= w < 645:
        r, g, b = 1.0, -(w - 645) / 65, 0.0
    elif 645 <= w <= 781:
        r, g, b = 1.0, 0.0, 0.0
    else:
        r, g, b = 0.0, 0.0, 0.0
    if 380 <= w < 420:
        f = 0.3 + 0.7 * (w - 380) / 40
    elif 700 < w <= 781:
        f = 0.3 + 0.7 * (781 - w) / 81
    else:
        f = 1.0
    return (r * f, g * f, b * f)


# ---------------------------------------------------------------- Figure 38.1
def surface_fraction_melting():
    fig, ax = new_fig(6.6, 4.2)
    d = np.logspace(0, 3, 600)
    f = np.where(d > 0.5, 1 - (1 - 0.5 / d)**3, 1.0)
    ax.axvspan(1, 10, color="#FBE3CF", alpha=0.6, lw=0)
    ax.text(3.6, 0.895, "surface dominated\n(1–10 nm)", ha="center", va="top", fontsize=8, color="#8A4A10")
    ax.semilogx(d, f, color=COLORS[0], lw=2)
    lab = {2: (8, 2), 5: (8, 2), 10: (7, 3), 20: (6, 4), 100: (-4, 7)}
    for dd in (2, 5, 10, 20, 100):
        ff = 1 - (1 - 0.5 / dd)**3
        ax.plot(dd, ff, "o", color=COLORS[0], ms=5, zorder=4)
        txt = f"{ff:.2f}" if ff >= 0.1 else (f"{ff:.3f}" if ff > 0.02 else f"{ff:.3f}")
        ax.annotate(txt, xy=(dd, ff), xytext=lab[dd], textcoords="offset points", fontsize=8,
                    color=COLORS[0], ha="left" if dd != 100 else "center", va="bottom")
    ax.set_xlim(1, 1000)
    ax.set_ylim(0, 1.0)
    ax.set_xlabel("particle diameter $d$ (nm)")
    ax.set_ylabel("fraction of atoms in 0.25 nm surface shell", color=COLORS[0])
    ax.tick_params(axis="y", colors=COLORS[0])
    ax.text(150, 0.12, r"$f=1-(1-2t/d)^3$, $t$ = 0.25 nm", color=COLORS[0], fontsize=8.5, ha="center")

    a2 = ax.twinx()
    a2.spines["right"].set_visible(True)
    r = d / 2 * 1e-9
    Tm = 1337 * (1 - 2 * 0.27 / (1.23e9 * r))
    m = Tm > 600
    a2.semilogx(d[m], Tm[m], color=COLORS[1], lw=2)
    a2.axhline(1337, color=COLORS[1], ls="--", lw=1)
    a2.text(990, 1347, "bulk Au $T_m$ = 1337 K", color=COLORS[1], fontsize=8, ha="right", va="bottom")
    for dd, txt, off in ((10, "1220 K", (8, -12)), (5, "1102 K", (8, -12)), (2.5, "867 K", (-38, -4))):
        T = 1337 * (1 - 0.54 / (1.23e9 * dd / 2 * 1e-9))
        a2.plot(dd, T, "s", color=COLORS[1], ms=5, zorder=4)
        a2.annotate(txt, xy=(dd, T), xytext=off, textcoords="offset points", fontsize=8, color=COLORS[1])
    # schematic measurements (Buffat-Borel-type): on the curve above ~5 nm, below it at 2-3 nm
    de = np.array([2.5, 3.0, 4.0, 5.0, 7.0, 10.0, 15.0, 25.0])
    Te = np.array([650, 760, 980, 1085, 1170, 1215, 1265, 1305])
    a2.plot(de, Te, "^", mfc="white", mec=COLORS[1], ms=6, mew=1.2, zorder=5)
    a2.set_ylim(600, 1400)
    from matplotlib.ticker import FixedLocator, FixedFormatter, NullFormatter
    ax.xaxis.set_major_locator(FixedLocator([1, 10, 100, 1000]))
    ax.xaxis.set_major_formatter(FixedFormatter(["1", "10", "100", "1000"]))
    ax.xaxis.set_minor_formatter(NullFormatter())
    a2.set_ylabel("melting temperature of Au (K)", color=COLORS[1])
    a2.tick_params(axis="y", colors=COLORS[1])
    handles = [Line2D([], [], color=COLORS[0], lw=2, marker="o", ms=5, label="surface-atom fraction (left)"),
               Line2D([], [], color=COLORS[1], lw=2, label="Gibbs–Thomson $T_m$, Au (right)"),
               Line2D([], [], ls="", marker="^", mfc="white", mec=COLORS[1], ms=6, label="measured $T_m$ (schematic)")]
    a2.legend(handles=handles, loc="center right", bbox_to_anchor=(1.0, 0.42), fontsize=8)
    save(fig, "38", "fig-38-1-surface-fraction-melting")


# ---------------------------------------------------------------- Figure 38.2
def _cube(ax, x, y, s, depth=(0.35, 0.25), h=None, w=None, fc="#CFE0F0"):
    w = s if w is None else w
    h = s if h is None else h
    dx, dy = depth
    ax.add_patch(Polygon([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], fc=fc, ec=INK, lw=0.8))
    ax.add_patch(Polygon([(x, y + h), (x + w, y + h), (x + w + dx, y + h + dy), (x + dx, y + h + dy)],
                         fc="#E4EEF7", ec=INK, lw=0.8))
    ax.add_patch(Polygon([(x + w, y), (x + w + dx, y + dy), (x + w + dx, y + h + dy), (x + w, y + h)],
                         fc="#B7CDE3", ec=INK, lw=0.8))


def dos_dimensionality_qd_colour():
    fig = plt.figure(figsize=(6.8, 4.8))
    E = np.linspace(0, 1, 2000)
    lefts = [0.07, 0.30, 0.53, 0.76]
    titles = ["3D (bulk)", "2D (quantum well)", "1D (quantum wire)", "0D (quantum dot)"]
    levels = np.array([0.12, 0.42, 0.78])
    for i, (l, t) in enumerate(zip(lefts, titles)):
        a = fig.add_axes([l, 0.66, 0.2, 0.25])
        if i == 0:
            g = np.sqrt(np.clip(E - 0.05, 0, None))
        elif i == 1:
            g = sum(np.where(E >= e0, 0.35, 0) for e0 in levels)
        elif i == 2:
            g = np.minimum(sum(np.where(E > e0, 0.07 / np.sqrt(np.clip(E - e0, 1e-4, None)), 0)
                               for e0 in levels), 1.15)
        if i < 3:
            a.plot(E, g, color=COLORS[0])
            a.fill_between(E, 0, g, color=COLORS[0], alpha=0.15)
        else:
            for e0 in levels:
                a.vlines(e0, 0, 1.0, color=COLORS[0], lw=2.2)
        a.set_xlim(0, 1); a.set_ylim(0, 1.75)
        a.set_xticks([]); a.set_yticks([])
        a.set_xlabel("$E$", fontsize=9, labelpad=1)
        if i == 0:
            a.set_ylabel("$g(E)$", fontsize=9)
        a.set_title(t, fontsize=8.5)
        s = fig.add_axes([l + 0.12, 0.815, 0.075, 0.10])
        s.set_xlim(0, 1.5); s.set_ylim(0, 1.5); s.set_aspect("equal"); s.axis("off")
        if i == 0:
            _cube(s, 0.1, 0.1, 0.9)
        elif i == 1:
            _cube(s, 0.0, 0.45, 1.0, h=0.15, depth=(0.4, 0.35))
        elif i == 2:
            _cube(s, 0.0, 0.5, 1.1, h=0.2, w=1.1, depth=(0.15, 0.12))
        else:
            s.add_patch(Circle((0.6, 0.6), 0.22, fc="#CFE0F0", ec=INK, lw=0.8))
    fig.text(0.01, 0.955, "(a)", fontsize=10, fontweight="bold")

    ax = fig.add_axes([0.10, 0.09, 0.62, 0.44])
    d = np.linspace(2.5, 8.0, 400)
    R = d / 2
    Eg, me, mh, er = 1.74, 0.13, 0.45, 10.6
    Eb = Eg + 0.376 / R**2 * (1 / me + 1 / mh) - 1.786 * 1.440 / (er * R)
    ax.plot(d, Eb, color=COLORS[0], lw=2, label="Brus equation")
    for dd in (4, 5, 7):
        Rr = dd / 2
        Ev = Eg + 0.376 / Rr**2 * (1 / me + 1 / mh) - 1.786 * 1.440 / (er * Rr)
        ax.plot(dd, Ev, "o", color=COLORS[0], ms=4)
        ax.annotate(f"{Ev:.2f} eV", xy=(dd, Ev), xytext=(6, 4), textcoords="offset points", fontsize=7.8,
                    color=COLORS[0])
    ax.annotate("Brus: 3.9 eV\nat 2.5 nm", xy=(3.38, 3.08), xytext=(3.65, 2.86), fontsize=7.8, color=COLORS[0],
                arrowprops=dict(arrowstyle="-|>", lw=0.8, color=COLORS[0], mutation_scale=8))
    pts_d = np.array([2.5, 5.0, 7.0])
    pts_E = np.array([2.50, 2.10, 1.95])
    ax.plot(pts_d, pts_E, "D", color=COLORS[1], ms=5, label="measured first exciton (typical)")
    for dd, ee in zip(pts_d, pts_E):
        ax.annotate(f"{ee:.2f} eV", xy=(dd, ee), xytext=(7, -10) if dd < 3 else ((-4, -14) if dd < 6 else (-8, -8)),
                    textcoords="offset points", fontsize=7.8, color=COLORS[1],
                    ha="left" if dd < 3 else ("center" if dd < 6 else "right"))
    ax.axhline(Eg, color="0.4", ls="--", lw=1)
    ax.text(7.95, Eg + 0.02, "bulk CdSe $E_g$ = 1.74 eV", ha="right", fontsize=8, color="0.3")
    ax.set_xlim(2.3, 8)
    ax.set_ylim(1.7, 3.1)
    ax.set_xlabel("CdSe dot diameter $d$ (nm)")
    ax.set_ylabel("emission energy (eV)")
    ax.legend(fontsize=7.8, loc="upper right")
    fig.text(0.01, 0.53, "(b)", fontsize=10, fontweight="bold")
    cb = fig.add_axes([0.735, 0.09, 0.025, 0.44])
    Es = np.linspace(1.7, 3.1, 300)
    img = np.array([wavelength_rgb(1239.84 / e) for e in Es])[:, None, :]
    cb.imshow(img, extent=(0, 1, 1.7, 3.1), origin="lower", aspect="auto")
    cb.set_xticks([])
    cb.yaxis.tick_right()
    cb.yaxis.set_label_position("right")
    wl = np.array([700, 650, 600, 550, 500, 450, 410])
    cb.set_yticks(1239.84 / wl)
    cb.set_yticklabels([str(v) for v in wl], fontsize=7.5)
    cb.set_ylim(1.7, 3.1)
    cb.set_ylabel("wavelength (nm)", fontsize=8.5)
    for sp in cb.spines.values():
        sp.set_visible(False)
    save(fig, "38", "fig-38-2-dos-dimensionality-qd-colour")


# ---------------------------------------------------------------- Figure 38.3
A_LAT = 0.246
ACC = A_LAT / np.sqrt(3)
A1 = A_LAT * np.array([np.sqrt(3) / 2, 0.5])
A2 = A_LAT * np.array([np.sqrt(3) / 2, -0.5])


def _graphene_atoms(irange, jrange):
    pts, sub = [], []
    for i in irange:
        for j in jrange:
            R = i * A1 + j * A2
            pts.append(R); sub.append(0)
            pts.append(R + np.array([ACC, 0])); sub.append(1)
    return np.array(pts), np.array(sub)


def _tube(ax, n, m, L, x0, y0, scale, title):
    Ch = n * A1 + m * A2
    C = np.linalg.norm(Ch)
    Rt = C / (2 * np.pi)
    ch_hat = Ch / C
    t_hat = np.array([-ch_hat[1], ch_hat[0]])
    pts, _ = _graphene_atoms(range(-40, 41), range(-40, 41))
    u = pts @ ch_hat
    v = pts @ t_hat
    keep = (u >= -1e-9) & (u < C - 1e-6) & (v >= 0) & (v <= L)
    u, v = u[keep], v[keep]
    phi = 2 * np.pi * u / C
    P3 = np.c_[v, Rt * np.sin(phi), Rt * np.cos(phi)]
    segs_f, segs_b = [], []
    for i, j in cKDTree(P3).query_pairs(ACC * 1.08):
        p, q = P3[i], P3[j]
        seg = [(x0 + scale * p[0], y0 + scale * p[1]), (x0 + scale * q[0], y0 + scale * q[1])]
        (segs_f if (p[2] + q[2]) > 0 else segs_b).append(seg)
    ax.add_collection(LineCollection(segs_b, colors="#B8C4D0", lw=0.6))
    ax.add_collection(LineCollection(segs_f, colors=INK, lw=0.9))
    ax.text(x0 + scale * L / 2, y0 - scale * Rt - 0.25, title, ha="center", va="top", fontsize=8)


def cnt_chiral_map():
    fig = plt.figure(figsize=(6.8, 5.3))
    ax = fig.add_axes([0.0, 0.40, 0.42, 0.56])
    ax.set_aspect("equal"); ax.axis("off")
    pts, sub = _graphene_atoms(range(-6, 12), range(-12, 8))
    xmin, xmax, ymin, ymax = -0.45, 1.45, -0.25, 1.3
    sel = (pts[:, 0] > xmin - 0.2) & (pts[:, 0] < xmax + 0.2) & (pts[:, 1] > ymin - 0.2) & (pts[:, 1] < ymax + 0.2)
    pts, sub = pts[sel], sub[sel]
    segs = [(pts[i], pts[j]) for i, j in cKDTree(pts).query_pairs(ACC * 1.05)]
    ax.add_collection(LineCollection(segs, colors="#9AA7B4", lw=0.8))
    ax.scatter(pts[:, 0], pts[:, 1], s=6, c=np.where(sub == 0, "#5A6E8C", "#9AA7B4"), zorder=2)
    ax.set_xlim(xmin, xmax); ax.set_ylim(ymin, ymax)
    O = np.array([0.0, 0.0])
    n, m = 4, 2
    Ch = n * A1 + m * A2
    dR = gcd(2 * m + n, 2 * n + m)
    T = (2 * m + n) // dR * A1 - (2 * n + m) // dR * A2

    def vec(v, col, lab, off, lw=1.8):
        ax.add_patch(FancyArrowPatch(O, O + v, arrowstyle="-|>", mutation_scale=12, color=col, lw=lw, zorder=5))
        ax.text(*(O + v + off), lab, color=col, fontsize=9.5, zorder=6,
                bbox=dict(fc="white", ec="none", pad=0.5, alpha=0.85))
    for ang in (30, 0):
        dvec = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
        ax.plot([0, 1.5 * dvec[0]], [0, 1.5 * dvec[1]], ls="--", color="0.45", lw=0.9, zorder=3)
    ax.text(0.98, 0.62, r"zigzag ($\theta=0$)", rotation=30, fontsize=8, color="0.3", zorder=6,
            bbox=dict(fc="white", ec="none", pad=0.3, alpha=0.85))
    ax.text(0.62, -0.14, r"armchair ($\theta=30^\circ$)", fontsize=8, color="0.3", zorder=6,
            bbox=dict(fc="white", ec="none", pad=0.3, alpha=0.85))
    vec(A1, COLORS[2], r"$\mathbf{a}_1$", (-0.05, 0.03))
    vec(A2, COLORS[2], r"$\mathbf{a}_2$", (-0.02, -0.12))
    vec(Ch, COLORS[1], r"$\mathbf{C}_h=4\mathbf{a}_1+2\mathbf{a}_2$", (-0.55, 0.06), lw=2.2)
    vec(T, COLORS[0], r"$\mathbf{T}$", (0.03, -0.05), lw=2.2)
    ax.plot(*O, "o", color=INK, ms=4, zorder=6)
    ax.text(-0.05, -0.1, "O", fontsize=9, ha="right")
    ax.text(-0.42, 1.22, r"$|\mathbf{a}_1|=|\mathbf{a}_2|=a=0.246$ nm", fontsize=8, zorder=6,
            bbox=dict(fc="white", ec="none", pad=0.5, alpha=0.85))
    ax.set_title("(a) chiral vector (4,2) on the graphene lattice", fontsize=9, loc="left")

    bx = fig.add_axes([0.44, 0.40, 0.56, 0.56])
    bx.set_aspect("equal"); bx.axis("off")
    rot = np.radians(-30)
    for nn in range(1, 14):
        for mm in range(0, nn + 1):
            p = nn * np.array([np.sqrt(3) / 2, 0.5]) + mm * np.array([np.sqrt(3) / 2, -0.5])
            p = np.array([p[0] * np.cos(rot) - p[1] * np.sin(rot), -(p[0] * np.sin(rot) + p[1] * np.cos(rot))])
            metallic = (nn - mm) % 3 == 0
            bx.add_patch(RegularPolygon(p, 6, radius=0.56, orientation=0,
                                        fc="#2E5E8C" if metallic else "white", ec="#2E5E8C", lw=0.8))
            dnm = A_LAT * np.sqrt(nn * nn + nn * mm + mm * mm) / np.pi
            if (nn, mm) in ((10, 0), (13, 0)):
                bx.text(p[0], p[1] - 0.75, f"({nn},{mm})\n{dnm:.2f} nm", ha="center", va="top", fontsize=7.3)
            if (nn, mm) == (10, 10):
                bx.annotate(f"(10,10)\n$d$ = {dnm:.2f} nm", xy=p, xytext=(p[0] - 1.6, p[1] + 1.9), fontsize=7.3,
                            ha="center", arrowprops=dict(arrowstyle="-", lw=0.6))
            if (nn, mm) == (4, 2):
                bx.annotate("(4,2)", xy=p, xytext=(p[0] - 2.0, p[1] + 2.2), fontsize=7.5, ha="center",
                            arrowprops=dict(arrowstyle="-", lw=0.6))
    bx.set_xlim(-0.8, 20.3)
    bx.set_ylim(-3.0, 12.0)
    bx.text(5.6, -2.9, r"zigzag $(n,0)$, $\theta=0$", ha="center", fontsize=8, color="0.3")
    bx.text(6.1, 5.0, r"armchair $(n,n)$, $\theta=30^\circ$", rotation=30, ha="center", fontsize=8, color="0.3")
    bx.add_patch(RegularPolygon((0.3, 11.0), 6, radius=0.5, fc="#2E5E8C", ec="#2E5E8C"))
    bx.text(1.1, 11.0, "metallic, $(n-m)$ mod 3 = 0", va="center", fontsize=7.8)
    bx.add_patch(RegularPolygon((0.3, 9.8), 6, radius=0.5, fc="white", ec="#2E5E8C"))
    bx.text(1.1, 9.8, "semiconducting", va="center", fontsize=7.8)
    bx.set_title(r"(b) chirality map, $0 \leq m \leq n \leq 13$", fontsize=9, loc="left")

    cx = fig.add_axes([0.02, 0.0, 0.96, 0.35])
    cx.set_aspect("equal"); cx.axis("off")
    cx.set_xlim(0, 15.5); cx.set_ylim(-2.2, 1.7)
    _tube(cx, 10, 0, 1.6, 0.3, 0.1, 2.6, "zigzag (10,0)\n$d$ = 0.78 nm, semiconducting")
    _tube(cx, 6, 6, 1.6, 5.5, 0.1, 2.6, "armchair (6,6)\n$d$ = 0.81 nm, metallic")
    _tube(cx, 8, 4, 1.6, 10.7, 0.1, 2.6, "chiral (8,4)\n$d$ = 0.83 nm, semiconducting")
    cx.set_title("(c) the three tube types (axis horizontal)", fontsize=9, loc="left")
    save(fig, "38", "fig-38-3-cnt-chiral-map")


# ---------------------------------------------------------------- Figure 38.4
def _honeycomb_top(ax, ca, cb, sa=40, sb=40, squash=1.0):
    pts, sub = _graphene_atoms(range(-4, 5), range(-4, 5))
    pts = pts / A_LAT
    pts[:, 1] *= squash
    sel = (abs(pts[:, 0]) < 1.42) & (abs(pts[:, 1]) < 1.15)
    pts, sub = pts[sel], sub[sel]
    cutoff = 0.6 if squash == 1.0 else 0.62
    segs = [(pts[i], pts[j]) for i, j in cKDTree(pts).query_pairs(cutoff)]
    ax.add_collection(LineCollection(segs, colors="0.45", lw=0.8))
    ax.scatter(pts[sub == 0, 0], pts[sub == 0, 1], s=sa, c=ca, ec=INK, lw=0.4, zorder=3)
    ax.scatter(pts[sub == 1, 0], pts[sub == 1, 1], s=sb, c=cb, ec=INK, lw=0.4, zorder=3)
    ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.3, 1.3)


def two_d_materials_family():
    fig = plt.figure(figsize=(6.8, 5.2))
    names = ["graphene", "h-BN", r"MoS$_2$", "black phosphorus", r"Ti$_3$C$_2$T$_x$ (MXene)"]
    C, B, N, MO, S, P, TI, O = "#444444", "#F4A6A6", "#5B7DD8", "#7A5BA6", "#E8D25A", "#E07B39", "#9DB4C0", "#D9534F"
    w = 0.19
    for i, name in enumerate(names):
        l = 0.01 + i * 0.198
        top = fig.add_axes([l, 0.68, w, 0.21]); top.set_aspect("equal"); top.axis("off")
        side = fig.add_axes([l, 0.48, w, 0.18]); side.set_aspect("equal"); side.axis("off")
        side.set_xlim(-1.5, 1.5); side.set_ylim(-0.9, 0.9)
        fig.text(l + w / 2, 0.925, name, ha="center", fontsize=8.5)
        xs = np.arange(-1.3, 1.31, 0.29)
        if i in (0, 1):
            _honeycomb_top(top, C if i == 0 else B, C if i == 0 else N)
            cols = [C if i == 0 else (B if k % 2 == 0 else N) for k in range(len(xs))]
            side.plot([xs[0], xs[-1]], [0, 0], color="0.45", lw=0.8)
            side.scatter(xs, np.zeros_like(xs), s=30, c=cols, ec=INK, lw=0.4, zorder=3)
            side.text(0, -0.6, "one atom thick" if i == 0 else "B (pink), N (blue)", ha="center", fontsize=7)
        elif i == 2:
            _honeycomb_top(top, MO, S, sa=55, sb=35)
            xm = np.arange(-1.2, 1.3, 0.6)
            for xmo in xm:
                for xsx in (xmo - 0.3, xmo + 0.3):
                    for ys in (0.4, -0.4):
                        side.plot([xmo, xsx], [0, ys], color="0.45", lw=0.8)
            sx = np.unique(np.r_[xm - 0.3, xm + 0.3])
            sx = sx[abs(sx) < 1.55]
            side.scatter(sx, 0.4 * np.ones_like(sx), s=30, c=S, ec=INK, lw=0.4, zorder=3)
            side.scatter(sx, -0.4 * np.ones_like(sx), s=30, c=S, ec=INK, lw=0.4, zorder=3)
            side.scatter(xm, np.zeros_like(xm), s=45, c=MO, ec=INK, lw=0.4, zorder=3)
            side.text(1.72, 0.4, "S", fontsize=7, va="center"); side.text(1.72, 0.0, "Mo", fontsize=7, va="center")
            side.set_xlim(-1.6, 2.1)
            side.text(0, -0.82, "S–Mo–S sandwich", ha="center", fontsize=7)
        elif i == 3:
            _honeycomb_top(top, P, P, squash=0.75)
            xp, yp = [], []
            for k in range(-3, 4):
                base = k * 0.62
                xp += [base - 0.13, base + 0.13]
                yp += [0.25 if k % 2 == 0 else -0.25] * 2
            xp, yp = np.array(xp), np.array(yp)
            sel = abs(xp) < 1.5
            side.plot(xp[sel], yp[sel], color="0.45", lw=0.8, zorder=1)
            side.scatter(xp[sel], yp[sel], s=30, c=P, ec=INK, lw=0.4, zorder=3)
            side.text(0, -0.75, "puckered layer", ha="center", fontsize=7)
        else:
            tri = []
            for a_ in range(-4, 5):
                for b_ in range(-4, 5):
                    p = a_ * np.array([1, 0]) * 0.5 + b_ * np.array([0.5, np.sqrt(3) / 2]) * 0.5
                    if abs(p[0]) < 1.45 and abs(p[1]) < 1.15:
                        tri.append(p)
            tri = np.array(tri)
            segs = [(tri[i_], tri[j_]) for i_, j_ in cKDTree(tri).query_pairs(0.51)]
            top.add_collection(LineCollection(segs, colors="0.6", lw=0.6))
            top.scatter(tri[:, 0], tri[:, 1], s=40, c=TI, ec=INK, lw=0.4, zorder=3)
            cpos = tri + np.array([0.25, 0.144])
            cpos = cpos[(abs(cpos[:, 0]) < 1.45) & (abs(cpos[:, 1]) < 1.15)]
            top.scatter(cpos[:, 0], cpos[:, 1], s=14, c=C, zorder=4)
            top.set_xlim(-1.5, 1.5); top.set_ylim(-1.2, 1.2)
            layers = [(0.78, O, 22, 0.0), (0.55, TI, 40, 0.2), (0.3, C, 16, 0.4), (0.0, TI, 40, 0.0),
                      (-0.3, C, 16, 0.2), (-0.55, TI, 40, 0.4), (-0.78, O, 22, 0.2)]
            for (yy, col, sz, off) in layers:
                xx = np.arange(-1.3, 1.35, 0.6) + off
                xx = xx[abs(xx) < 1.45]
                side.scatter(xx, np.full_like(xx, yy), s=sz, c=col, ec=INK, lw=0.3, zorder=3)
            for yy, t in ((0.78, "T$_x$"), (0.55, "Ti"), (0.3, "C"), (0.0, "Ti"), (-0.3, "C"), (-0.55, "Ti"),
                          (-0.78, "T$_x$")):
                side.text(1.5, yy, t, fontsize=6.3, va="center")
            side.set_xlim(-1.5, 1.95)
    fig.text(0.003, 0.785, "top", rotation=90, fontsize=8, color="0.4", va="center")
    fig.text(0.003, 0.57, "side", rotation=90, fontsize=8, color="0.4", va="center")

    ax = fig.add_axes([0.06, 0.08, 0.90, 0.34])
    vis = np.array([wavelength_rgb(1239.84 / e) for e in np.linspace(1.65, 3.1, 200)])[None, :, :]
    ax.imshow(vis, extent=(1.65, 3.1, -0.1, 6.3), aspect="auto", alpha=0.3, zorder=0)
    ax.text(2.375, 6.55, "visible light (1.65–3.1 eV)", ha="center", fontsize=8, color="0.3")
    cat = {"metal": COLORS[7], "semimetal": COLORS[3], "semiconductor": COLORS[0], "insulator": COLORS[1]}
    entries = [("graphene (zero-gap semimetal)", 0.0, 0.0, "semimetal"),
               (r"MXene Ti$_3$C$_2$T$_x$ (metal)", 0.0, 0.0, "metal"),
               ("phosphorene: 0.3 eV bulk → ≈1.8 eV monolayer", 0.3, 1.8, "semiconductor"),
               (r"MoS$_2$: 1.25 eV bulk (indirect) → 1.9 eV monolayer (direct)", 1.25, 1.9, "semiconductor"),
               (r"WSe$_2$ monolayer ≈1.65 eV", 1.65, 1.65, "semiconductor"),
               ("h-BN ≈6.0 eV", 6.0, 6.0, "insulator")]
    for k, (nm, lo, hi, c) in enumerate(entries):
        y = 5.5 - k
        col = cat[c]
        if hi > lo:
            ax.plot([lo, hi], [y, y], color=col, lw=6, solid_capstyle="round", alpha=0.85, zorder=2)
            ax.plot([hi], [y], "o", color=col, ms=8, mec=INK, mew=0.6, zorder=3)
            ax.text(hi + 0.13, y, nm, va="center", fontsize=8, zorder=4)
        else:
            ax.plot([lo], [y], "o", color=col, ms=8, mec=INK, mew=0.6, zorder=3)
            ax.text(lo + 0.13 if lo < 5 else lo - 0.13, y, nm, va="center", ha="left" if lo < 5 else "right",
                    fontsize=8, zorder=4)
    # Dirac-cone icon next to graphene
    yc = 5.5
    cx0 = 2.25
    ax.plot([cx0 - 0.13, cx0, cx0 + 0.13], [yc + 0.38, yc, yc + 0.38], color=COLORS[1], lw=1.2, zorder=4)
    ax.plot([cx0 - 0.13, cx0, cx0 + 0.13], [yc - 0.38, yc, yc - 0.38], color=COLORS[0], lw=1.2, zorder=4)
    ax.add_patch(Ellipse((cx0, yc + 0.38), 0.26, 0.12, fill=False, ec=COLORS[1], lw=0.9, zorder=4))
    ax.add_patch(Ellipse((cx0, yc - 0.38), 0.26, 0.12, fill=False, ec=COLORS[0], lw=0.9, zorder=4))
    ax.text(cx0 + 0.2, yc, "Dirac cone", fontsize=7, va="center", color="0.3")
    ax.set_xlim(-0.15, 6.3)
    ax.set_ylim(-0.1, 6.9)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("band gap (eV)")
    handles = [Line2D([], [], marker="o", ls="", color=v, mec=INK, ms=7, label=k_) for k_, v in cat.items()]
    ax.legend(handles=handles, loc="upper right", bbox_to_anchor=(1.0, 0.86), fontsize=8, ncol=1)
    save(fig, "38", "fig-38-4-2d-materials-family")


# ---------------------------------------------------------------- Figure 38.5
def hall_petch_inverse():
    fig, ax = new_fig(6.6, 4.4)
    s0, ky = 25.0, 0.11
    x = np.linspace(0, 15000, 600)
    xd = 1 / np.sqrt(20e-9)
    # zones
    zx = [(0, 1 / np.sqrt(100e-9), "#E8F1F8", "pile-up\nregime\n($d$ > 100 nm)"),
          (1 / np.sqrt(100e-9), 1 / np.sqrt(12e-9), "#FFF3DC", "boundary-emitted\ndislocations"),
          (1 / np.sqrt(12e-9), 15000, "#FBE3E3", "grain-boundary\nsliding /\ninverse Hall–Petch")]
    for a, b, c, t in zx:
        ax.axvspan(a, b, color=c, lw=0, zorder=0)
        ax.text((a + b) / 2, 1560, t, ha="center", va="top", fontsize=8, color="0.25")
    m = x <= xd
    ax.plot(x[m], s0 + ky * x[m], color=COLORS[0], lw=2, label=r"Hall–Petch $\sigma_y=25+0.11\,d^{-1/2}$")
    ax.plot(x[~m & (x <= 1 / np.sqrt(5e-9))], s0 + ky * x[~m & (x <= 1 / np.sqrt(5e-9))], color=COLORS[0],
            lw=2, ls="--", label="extrapolation")
    for dd, lab, off in ((10e-6, "60", (4, -12)), (1e-6, "135", (4, -12)), (100e-9, "373", (5, -12)),
                         (20e-9, "803", (6, -12)), (10e-9, "1125", (-30, 2)), (5e-9, "1581", (-30, 0))):
        xx = 1 / np.sqrt(dd)
        ax.plot(xx, s0 + ky * xx, "o", color=COLORS[0], ms=4, zorder=4)
        ax.annotate(lab, xy=(xx, s0 + ky * xx), xytext=off, textcoords="offset points", fontsize=7.8,
                    color=COLORS[0])
    # schematic experimental band
    xb = np.array([0, 1 / np.sqrt(100e-9), 1 / np.sqrt(25e-9), 1 / np.sqrt(18e-9), 1 / np.sqrt(14e-9),
                   1 / np.sqrt(12e-9), 1 / np.sqrt(9e-9), 1 / np.sqrt(7e-9), 1 / np.sqrt(5e-9)])
    yb = s0 + ky * xb
    yb[3:] = [830, 905, 950, 920, 840, 720]
    xs = np.linspace(0, xb[-1], 400)
    yc = PchipInterpolator(xb, yb)(xs)
    ax.fill_between(xs, yc - 70, yc + 70, color=COLORS[1], alpha=0.25, lw=0, zorder=2,
                    label="measured nanocrystalline Cu (schematic)")
    ax.plot(xs, yc, color=COLORS[1], lw=1.0, zorder=3)
    ax.annotate("peak ≈ 0.9–1.0 GPa\nat $d$ ≈ 10–15 nm", xy=(1 / np.sqrt(12e-9), 955), xytext=(5600, 1180),
                fontsize=8, color=COLORS[1], arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[1]))
    xt = 1 / np.sqrt(25e-9)
    ax.plot(xt, 900, "*", ms=11, color=COLORS[2], mec=INK, mew=0.5, zorder=5)
    ax.annotate("nanotwinned Cu ≈ 0.9 GPa\n(twin spacing ≈ 25 nm)", xy=(xt, 900), xytext=(1500, 1000),
                fontsize=8, color=COLORS[2], ha="center", arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[2]))
    ax.set_xlim(0, 15000)
    ax.set_ylim(0, 1600)
    ax.set_xlabel(r"$d^{-1/2}$ (m$^{-1/2}$)")
    ax.set_ylabel("yield strength of Cu (MPa)")
    ax.legend(loc="lower right", fontsize=8, framealpha=0.9, frameon=True, edgecolor="none")
    top = ax.twiny()
    top.spines["top"].set_visible(True)
    top.set_xlim(0, 15000)
    dl = [(10e-6, "10 µm"), (1e-6, "1 µm"), (100e-9, "100 nm"), (20e-9, "20 nm"), (10e-9, "10 nm"), (5e-9, "5 nm")]
    top.set_xticks([1 / np.sqrt(v) for v, _ in dl])
    top.set_xticklabels([t for _, t in dl], fontsize=8)
    top.set_xlabel("grain size $d$", fontsize=9)
    labs = top.get_xticklabels()
    labs[0].set_horizontalalignment("right")
    labs[1].set_horizontalalignment("left")
    save(fig, "38", "fig-38-5-hall-petch-inverse")


# ---------------------------------------------------------------- Figure 38.6
def synthesis_routes():
    fig = plt.figure(figsize=(6.8, 5.6))
    ax = fig.add_axes([0.11, 0.03, 0.88, 0.86])
    ax.set_yscale("log")
    ylo, yhi = 0.1, 1e6           # nm
    ax.set_ylim(ylo, yhi)
    ax.set_xlim(0, 12.6)
    ax.set_xticks([])
    for sp in ("top", "right", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.set_yticks([0.1, 1, 10, 100, 1e3, 1e4, 1e5, 1e6])
    ax.set_yticklabels(["0.1 nm\natoms", "1 nm", "10 nm", "100 nm", "1 µm", "10 µm", "100 µm", "1 mm\nbulk"],
                       fontsize=8)
    ax.set_ylabel("length scale (log)")
    ax.axhspan(1, 100, color="#FBE3CF", alpha=0.7, lw=0, zorder=0)
    ax.text(0.1, 1.12, "nanoscale\n1–100 nm", ha="left", va="bottom", fontsize=8.5, color="#8A4A10",
            fontweight="bold")
    ax.axvline(4.3, color="0.6", lw=0.8, ls=":")
    fig.text(0.11 + 0.88 * 2.15 / 12.6, 0.935, "TOP-DOWN\nbreak or carve bulk material", ha="center",
             fontsize=8.5, color=COLORS[0], fontweight="bold")
    fig.text(0.11 + 0.88 * 8.45 / 12.6, 0.935, "BOTTOM-UP\nassemble atoms and molecules", ha="center",
             fontsize=8.5, color=COLORS[1], fontweight="bold")

    def route(x, start, lo, hi, name, prod, col, icon, icon_y=None):
        down = start > hi
        end = lo if down else hi
        ax.plot([x, x], [lo, hi], color=col, lw=7, solid_capstyle="butt", alpha=0.45, zorder=2)
        ax.annotate("", xy=(x, end), xytext=(x, start),
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=1.4, mutation_scale=11, shrinkA=0, shrinkB=0),
                    zorder=3)
        if down:
            ax.text(x - 0.12, start / 1.6, name, rotation=90, ha="right", va="top", fontsize=7.8, color=INK)
        else:
            ax.text(x - 0.12, start * 1.3, name, rotation=90, ha="right", va="bottom", fontsize=7.8, color=INK)
        ax.text(x + 0.13, np.sqrt(lo * hi), prod, rotation=90, ha="left", va="center", fontsize=7.2, color=col)
        if down:
            icon(x - 0.36, np.sqrt(lo * hi) if icon_y is None else icon_y)
        else:
            icon(x, hi * 2.6 if icon_y is None else icon_y)

    def pts_to(x, y, dx, fy):
        return (x + dx, y * fy)

    def ic_grains(x, y):
        for dx, fy in ((-0.1, 1.0), (0.1, 1.0), (0.0, 1.35)):
            ax.plot(*pts_to(x, y, dx, fy), marker="h", ms=6, mfc="#DCE6F0", mec=INK, mew=0.5, ls="")

    def ic_particles(x, y):
        for dx, fy in ((-0.12, 1.0), (0.0, 1.0), (0.12, 1.0), (0.06, 1.4), (-0.06, 1.4)):
            ax.plot(*pts_to(x, y, dx, fy), marker="o", ms=4.5, mfc="#E9D3B0", mec=INK, mew=0.5, ls="")

    def ic_dot(x, y):
        ax.plot(x, y, marker="o", ms=7, mfc="#E0505A", mec=INK, mew=0.5, ls="")
        ax.plot(x, y, marker="o", ms=11, mfc="none", mec="0.4", mew=0.6, ls="")

    def ic_sheet(x, y):
        ax.plot(x, y, marker="h", ms=9, mfc="#B9C7D6", mec=INK, mew=0.5, ls="")

    def ic_tube(x, y):
        ax.plot([x - 0.18, x + 0.18], [y, y], color="#555555", lw=3.5, solid_capstyle="round")

    def ic_wire(x, y):
        ax.plot([x, x], [y, y * 2.4], color="#5A8F5A", lw=2.2)
        ax.plot(x, y * 2.4, marker="o", ms=5, mfc="#E5C547", mec=INK, mew=0.5)

    def ic_film(x, y):
        for k in range(3):
            ax.add_patch(Rectangle((x - 0.2, y * 1.25**k), 0.4, y * 1.25**k * 0.18, fc=["#9DB4C0", "#C9D6DF", "#9DB4C0"][k],
                                   ec=INK, lw=0.4))

    def ic_pattern(x, y):
        for dx in (-0.15, 0.0, 0.15):
            ax.add_patch(Rectangle((x + dx - 0.04, y), 0.08, y * 1.2, fc="#9AA7B4", ec=INK, lw=0.4))

    def ic_micelle(x, y):
        for a in np.linspace(0, 2 * np.pi, 9)[:-1]:
            ax.plot(x + 0.12 * np.cos(a), y * 10**(0.09 * np.sin(a)), marker="o", ms=2.6, color=COLORS[0], ls="")

    B, U = COLORS[0], COLORS[1]
    top = 1e6
    route(0.55, top, 10, 30, "high-energy ball milling", "10–30 nm grains", B, ic_grains)
    route(1.55, top, 100, 300, "severe plastic deformation (ECAP, HPT)", "100–300 nm grains", B, ic_grains)
    route(2.55, top, 10, 20, "lithography + etching", "10–20 nm features", B, ic_pattern)
    route(3.55, top, 0.34, 1.0, "exfoliation (tape, liquid phase)", "graphene flakes", B, ic_sheet)

    bot = 0.1
    route(4.75, bot, 7, 80, "gas-phase / flame pyrolysis", "fumed silica,\ncarbon black", U, ic_particles)
    route(5.75, bot, 2, 10, "hot-injection colloidal", "quantum dots,\n±5 %", U, ic_dot)
    route(6.75, bot, 2, 50, "sol–gel, hydrothermal", "oxide particles,\naerogels", U, ic_particles)
    route(7.75, bot, 1, 50, "CVD on catalysts", "CNT;\ngraphene on Cu", U, ic_tube)
    route(8.75, bot, 5, 200, "VLS growth", "nanowires", U, ic_wire)
    route(9.75, bot, 0.1, 10, "ALD", "atomic layers", U, ic_film)
    route(10.75, bot, 10, 20, "electrodeposition", "nc-Ni, nt-Cu", U, ic_grains)
    route(11.75, bot, 5, 50, "self-assembly", "BCP domains,\nmicelles", U, ic_micelle)
    save(fig, "38", "fig-38-6-synthesis-routes")


if __name__ == "__main__":
    surface_fraction_melting()
    dos_dimensionality_qd_colour()
    cnt_chiral_map()
    two_d_materials_family()
    hall_petch_inverse()
    synthesis_routes()
