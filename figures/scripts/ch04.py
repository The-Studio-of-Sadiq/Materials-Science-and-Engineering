"""Figures for Chapter 4 — Reciprocal Space, Diffraction and Tensor Properties.

Run from the repository root:  python figures/scripts/ch04.py
"""
import itertools
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figstyle import COLORS, INK, new_fig, save  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Arc, Circle, Ellipse, FancyArrowPatch  # noqa: E402
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # noqa: E402

LAM = 1.5406  # Cu K-alpha1, Angstrom
GREY = "#9A9A9A"


# --------------------------------------------------------------------------- helpers
def _arrow3d(ax, p0, p1, color=INK, lw=1.6, label=None, loff=(0, 0, 0), fs=9):
    p0, p1 = np.asarray(p0, float), np.asarray(p1, float)
    d = p1 - p0
    ax.quiver(*p0, *d, color=color, lw=lw, arrow_length_ratio=0.12, normalize=False)
    if label:
        q = p1 + np.asarray(loff)
        ax.text(*q, label, color=color, fontsize=fs, ha="center", va="center")


def _cube3d(ax, L=1.0, o=(0, 0, 0), **kw):
    o = np.asarray(o, float)
    for a, b in itertools.combinations(itertools.product([0, 1], repeat=3), 2):
        a, b = np.array(a), np.array(b)
        if np.sum(np.abs(a - b)) == 1:
            p, q = o + a * L, o + b * L
            ax.plot(*zip(p, q), **kw)


def _clean3d(ax, lim, elev=18, azim=-60):
    ax.set_xlim(*lim)
    ax.set_ylim(*lim)
    ax.set_zlim(*lim)
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=elev, azim=azim)
    ax.set_axis_off()


# --------------------------------------------------------------------------- 4.1
def fcc_reciprocal_brillouin():
    fig = plt.figure(figsize=(6.8, 2.9))
    axs = [fig.add_axes([0.00 + 0.335 * i, 0.0, 0.33, 0.86], projection="3d") for i in range(3)]

    # (a) FCC direct lattice
    ax = axs[0]
    _cube3d(ax, 1.0, color=INK, lw=0.9)
    corners = np.array(list(itertools.product([0, 1], repeat=3)), float)
    faces = np.array([[0.5, 0.5, 0], [0.5, 0.5, 1], [0.5, 0, 0.5], [0.5, 1, 0.5], [0, 0.5, 0.5], [1, 0.5, 0.5]])
    ax.scatter(*corners.T, s=34, color="#B8C7D9", edgecolor=INK, lw=0.6, depthshade=False)
    ax.scatter(*faces.T, s=34, color=COLORS[0], edgecolor=INK, lw=0.6, depthshade=False)
    a1, a2, a3 = (0, 0.5, 0.5), (0.5, 0, 0.5), (0.5, 0.5, 0)
    for v, lab, off in [(a1, r"$\mathbf{a}_1$", (0.0, -0.12, 0.12)), (a2, r"$\mathbf{a}_2$", (0.16, 0.0, 0.10)),
                        (a3, r"$\mathbf{a}_3$", (0.10, 0.0, -0.13))]:
        _arrow3d(ax, (0, 0, 0), v, color=COLORS[1], lw=2.0, label=lab, loff=off, fs=10)
    ax.text(1.05, 0.0, -0.05, r"$x$", fontsize=8, color=GREY)
    ax.text(0, 1.0, -0.14, r"$y$", fontsize=8, color=GREY)
    ax.text(-0.05, 0, 1.1, r"$z$", fontsize=8, color=GREY)
    _clean3d(ax, (-0.05, 1.05))
    ax.set_title("(a) FCC direct lattice, edge $a$\n" + r"$\mathbf{a}_1=\frac{a}{2}(0,1,1)$ etc.", fontsize=9, pad=-6)

    # (b) BCC reciprocal lattice, cube edge 4pi/a  (units 2pi/a: cube [0,2]^3)
    ax = axs[1]
    _cube3d(ax, 2.0, color=INK, lw=0.9)
    rc = np.array(list(itertools.product([0, 2], repeat=3)), float)
    ax.scatter(*rc.T, s=34, color="#F2C49B", edgecolor=INK, lw=0.6, depthshade=False)
    ax.scatter([1], [1], [1], s=48, color=COLORS[1], edgecolor=INK, lw=0.6, depthshade=False)
    labs = {(0, 0, 0): "000", (2, 0, 0): "200", (0, 2, 0): "020", (0, 0, 2): "002",
            (2, 2, 0): "220", (2, 0, 2): "202", (0, 2, 2): "022", (2, 2, 2): "222"}
    for p, s in labs.items():
        off = np.array([0.0, 0.0, 0.22 if p[2] == 2 else -0.26])
        ax.text(*(np.array(p, float) + off), s, fontsize=7.5, ha="center", color=INK)
    ax.text(1.0, 1.0, 1.28, "111", fontsize=8, ha="center", color=COLORS[1], weight="bold")
    for v, lab in [((-1, 1, 1), r"$\mathbf{b}_1$"), ((1, -1, 1), r"$\mathbf{b}_2$"), ((1, 1, -1), r"$\mathbf{b}_3$")]:
        end = np.array([1, 1, 1]) + np.array(v)
        _arrow3d(ax, (1, 1, 1), end, color=COLORS[0], lw=1.8)
    for pos, lab in [((0.62, 1.38, 1.95), r"$\mathbf{b}_1$"), ((1.62, 0.52, 1.22), r"$\mathbf{b}_2$"),
                     ((1.75, 1.75, 0.62), r"$\mathbf{b}_3$")]:
        ax.text(*pos, lab, color=COLORS[0], fontsize=9.5, ha="center")
    _clean3d(ax, (-0.1, 2.1))
    ax.set_title("(b) reciprocal lattice: BCC, edge $4\\pi/a$\n" + r"$\mathbf{b}_1=\frac{2\pi}{a}(\bar1,1,1)$ etc. (from 111)",
                 fontsize=9, pad=-6)

    # (c) First Brillouin zone (truncated octahedron), units 2pi/a
    ax = axs[2]
    ax.computed_zorder = False
    verts = set()
    for p in itertools.permutations((0, 0.5, 1)):
        for s in itertools.product([1, -1], repeat=3):
            verts.add(tuple(np.round(np.array(p) * np.array(s), 6) + 0.0))
    V = np.array(sorted(verts))
    normals = [np.array(n, float) for n in itertools.product([1, -1], repeat=3)]
    normals += [np.array(n, float) for n in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]
    polys, cols = [], []
    for n in normals:
        d = V @ n
        F = V[np.isclose(d, d.max())]
        c = F.mean(axis=0)
        u = F[0] - c
        u /= np.linalg.norm(u)
        w = np.cross(n / np.linalg.norm(n), u)
        ang = np.arctan2((F - c) @ w, (F - c) @ u)
        polys.append(F[np.argsort(ang)])
        cols.append("#CFE0F1" if len(F) == 6 else "#F6D9BF")
    pc = Poly3DCollection(polys, facecolors=cols, edgecolors="#555555", linewidths=0.6, alpha=0.30, zorder=1)
    ax.add_collection3d(pc)
    pts = {r"$\Gamma$": (0, 0, 0), "X": (1, 0, 0), "L": (0.5, 0.5, 0.5), "K": (0.75, 0.75, 0), "W": (1, 0.5, 0)}
    path = [pts[r"$\Gamma$"], pts["X"], pts["W"], pts["L"], pts[r"$\Gamma$"], pts["K"]]
    ax.plot(*np.array(path).T, ls="--", color=COLORS[1], lw=1.5, zorder=3)
    for k, p in pts.items():
        ax.scatter(*p, s=22, color=COLORS[1] if k != r"$\Gamma$" else INK, depthshade=False, zorder=5)
    offs = {r"$\Gamma$": (-0.05, -0.22, 0.02), "X": (0.06, -0.16, -0.06), "L": (0.0, 0.0, 0.17),
            "K": (0.10, 0.10, -0.12), "W": (0.12, 0.10, 0.10)}
    for k, p in pts.items():
        ax.text(*(np.array(p) + np.array(offs[k])), k, fontsize=10, ha="center", color=INK, weight="bold", zorder=6)
    _clean3d(ax, (-0.95, 0.95), elev=24, azim=28)
    ax.set_title("(c) first Brillouin zone of FCC\n(truncated octahedron)", fontsize=9, pad=-6)
    fig.text(0.835, 0.02, r"X $=\frac{2\pi}{a}(1,0,0)$,  L $=\frac{\pi}{a}(1,1,1)$" + "\nhexagons ⊥ ⟨111⟩ (blue), squares ⊥ ⟨100⟩ (tan)\n"
             "dashed: Γ–X–W–L–Γ–K", fontsize=7.5, ha="center", va="bottom", color=INK)
    save(fig, "04", "fig-4-1-fcc-reciprocal-brillouin")


# --------------------------------------------------------------------------- 4.2
def _lattice2d(ax, xr, yr, s=14, color=INK):
    xs = np.arange(int(np.floor(xr[0])), int(np.ceil(xr[1])) + 1)
    ys = np.arange(int(np.floor(yr[0])), int(np.ceil(yr[1])) + 1)
    X, Y = np.meshgrid(xs, ys)
    ax.scatter(X.ravel(), Y.ravel(), s=s, color=color, zorder=3)


def _vec(ax, p0, p1, color, lw=1.6, ls="-"):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=11, color=color, lw=lw,
                                 linestyle=ls, shrinkA=0, shrinkB=2, zorder=5))


def ewald_sphere():
    fig, axs = plt.subplots(1, 3, figsize=(6.8, 3.4), gridspec_kw=dict(width_ratios=[1.0, 1.05, 1.0]))
    # (a) X-ray single crystal: lambda/a = 0.43, reflection 2-bar 1 0 on the sphere
    ax = axs[0]
    k = 1 / 0.43
    G = np.array([-2.0, 1.0])
    g = np.linalg.norm(G)
    phi = np.arctan2(G[1], G[0])
    alpha = phi - np.arccos(-g / (2 * k))
    kv = k * np.array([np.cos(alpha), np.sin(alpha)])
    C = -kv
    _lattice2d(ax, (-4, 1), (-3, 2), s=10)
    ax.add_patch(Circle(C, k, fill=False, color=COLORS[0], lw=1.4))
    _vec(ax, C, (0, 0), COLORS[1])
    _vec(ax, C, G, COLORS[2])
    _vec(ax, (0, 0), G, INK, lw=1.3)
    # Bragg plane: perpendicular bisector of G (passes through C)
    n = G / g
    t = np.array([-n[1], n[0]])
    m = G / 2
    seg = np.array([m - 1.9 * t, m + 4.3 * t])
    ax.plot(seg[:, 0], seg[:, 1], ls=":", color=GREY, lw=1.2)
    ax.text(*(m + 4.0 * t + np.array([0.2, 0.0])), "Bragg\nplane", fontsize=7, color=GREY, ha="left", va="center")
    ax.scatter(*C, s=22, facecolor="white", edgecolor=COLORS[0], lw=1.2, zorder=6)
    ang1 = np.degrees(np.arctan2(kv[1], kv[0]))
    kp = G - C
    ang2 = np.degrees(np.arctan2(kp[1], kp[0]))
    ax.add_patch(Arc(C, 1.4, 1.4, theta1=ang1, theta2=ang2, color=INK, lw=0.9))
    mid = np.radians(0.5 * (ang1 + ang2))
    ax.text(C[0] + 0.95 * np.cos(mid), C[1] + 0.95 * np.sin(mid), r"$2\theta$", fontsize=9, ha="center", va="center")
    ax.text(-0.75, -0.95, r"$\mathbf{k}$", color=COLORS[1], fontsize=10)
    ax.text(-2.45, -0.2, r"$\mathbf{k}'$", color=COLORS[2], fontsize=10)
    ax.text(-0.7, 0.8, r"$\mathbf{G}$", fontsize=10, ha="center")
    for p, s in [((0, 0), "000"), ((-2, 1), r"$\bar2$10"), ((-1, 0), r"$\bar1$00"), ((0, 1), "010")]:
        ax.text(p[0] + 0.1, p[1] + 0.12, s, fontsize=6.5, color=INK)
    ax.text(-4.2, -4.95, r"radius $2\pi/\lambda$, $\lambda/a$ = 0.43" + "\n" + r"spacing $2\pi/a$", fontsize=7.5,
            color=COLORS[0], va="bottom")
    ax.set_xlim(-4.3, 1.4)
    ax.set_ylim(-5.0, 2.4)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("(a) X-rays, single crystal", fontsize=9)

    # (b) electrons: nearly flat sphere, rods
    ax = axs[1]
    R = 80.0
    xs = np.arange(-5, 6)
    for row in [-1, 0, 1]:
        for x in xs:
            ax.plot([x, x], [row - 0.28, row + 0.28], color=INK, lw=1.8, solid_capstyle="round", zorder=3)
    xx = np.linspace(-5.6, 5.6, 300)
    ax.plot(xx, R - np.sqrt(R ** 2 - xx ** 2), color=COLORS[0], lw=1.4, zorder=4)
    _vec(ax, (0, 3.0), (0, 0.05), COLORS[1])
    ax.text(0.25, 2.6, r"beam $\mathbf{k}$" + "\n" + r"$|\mathbf{k}|\approx 80\,|\mathbf{G}_{111}|$", fontsize=7.5,
            color=COLORS[1], va="top")
    ax.text(-5.7, 1.55, "Ewald sphere,\nnearly flat", fontsize=7.5, color=COLORS[0], va="bottom")
    ax.annotate("", xy=(-4.6, 0.12), xytext=(-4.6, 1.5), arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=0.8))
    ax.text(-5.7, -1.75, "rods ∥ foil normal (thin-foil\nshape effect) cut the sphere:\n"
            "a whole plane of points\nappears at once as spots", fontsize=7.5, color=INK, va="top")
    ax.set_xlim(-6, 6)
    ax.set_ylim(-4.3, 3.2)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("(b) electrons, 200 kV, thin foil", fontsize=9)

    # (c) powder: Cu K-alpha on Cu (units 2pi/a)
    ax = axs[2]
    k = 3.615 / 1.5406
    C = np.array([-k, 0.0])
    ax.add_patch(Circle(C, k, fill=False, color=COLORS[0], lw=1.4))
    _vec(ax, C, (0, 0), COLORS[1], lw=1.3)
    ax.scatter([0], [0], s=14, color=INK, zorder=6)
    ax.scatter(*C, s=22, facecolor="white", edgecolor=COLORS[0], lw=1.2, zorder=6)
    lines = []
    for (lab, N), col, la in zip([("111", 3), ("200", 4), ("220", 8)], [COLORS[2], COLORS[3], COLORS[4]], [72, 40, 20]):
        g = np.sqrt(N)
        ax.add_patch(Circle((0, 0), g, fill=False, color=col, lw=1.0, ls="--"))
        xi = -g * g / (2 * k)
        yi = np.sqrt(g * g - xi * xi)
        for sgn in (1, -1):
            ax.plot([C[0], xi], [C[1], sgn * yi], color=col, lw=1.0)
            ax.scatter([xi], [sgn * yi], s=12, color=col, zorder=6)
        tth = 2 * np.degrees(np.arcsin(g / (2 * k)))
        ax.text(g * np.cos(np.radians(la)) + 0.08, g * np.sin(np.radians(la)) + 0.05, lab, fontsize=7.5, color=col,
                ha="left", va="bottom")
        lines.append((f"{lab}: 2θ = {tth:.1f}°", col))
    for i, (s, col) in enumerate(lines):
        ax.text(-5.0, -3.0 - 0.55 * i, s, fontsize=7.5, color=col)
    ax.add_patch(Arc(C, 1.4, 1.4, theta1=0, theta2=43.3, color=INK, lw=0.9))
    ax.text(C[0] + 0.85, C[1] + 0.3, r"$2\theta$", fontsize=8)
    ax.text(-5.0, 3.55, "cones of half-angle 2θ", fontsize=7.5, va="top")
    ax.set_xlim(-5.1, 3.2)
    ax.set_ylim(-4.3, 3.6)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("(c) X-rays, powder (Cu Kα on Cu)", fontsize=9)
    fig.tight_layout(w_pad=0.6)
    save(fig, "04", "fig-4-2-ewald-sphere")


# --------------------------------------------------------------------------- 4.3
CM = {"Cu": ([13.338, 7.1676, 5.6158, 1.6735], [3.5828, 0.247, 11.3966, 64.8126], 1.191),
      "Fe": ([11.7695, 7.3573, 3.5222, 2.3045], [4.7611, 0.3072, 15.3535, 76.8805], 1.0369)}


def _f(el, s):
    a, b, c = CM[el]
    return sum(ai * np.exp(-bi * s * s) for ai, bi in zip(a, b)) + c


def _mult(hkl):
    out = set()
    for p in itertools.permutations(hkl):
        for sg in itertools.product([1, -1], repeat=3):
            out.add(tuple(x * y for x, y in zip(p, sg)))
    return len(out)


def _powder(el, a, lattice, B):
    rows = []
    for hkl in [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 0, 0), (2, 1, 1), (2, 2, 0), (3, 1, 0), (3, 1, 1), (2, 2, 2), (4, 0, 0)]:
        h, k, l = hkl
        N = h * h + k * k + l * l
        st = LAM / (2 * a / np.sqrt(N))
        if st >= 1:
            continue
        th = np.arcsin(st)
        s = st / LAM
        if lattice == "fcc":
            F = 4 * _f(el, s) if len({h % 2, k % 2, l % 2}) == 1 else 0.0
        else:
            F = 2 * _f(el, s) if (h + k + l) % 2 == 0 else 0.0
        Lp = (1 + np.cos(2 * th) ** 2) / (np.sin(th) ** 2 * np.cos(th))
        I = F * F * _mult(hkl) * Lp * np.exp(-2 * B * s * s)
        rows.append(dict(hkl="".join(map(str, hkl)), N=N, tth=np.degrees(2 * th), I=I))
    m = max(r["I"] for r in rows)
    for r in rows:
        r["I"] *= 100 / m
    return rows


def cu_fe_powder_patterns():
    fig, axs = plt.subplots(2, 1, figsize=(6.6, 4.8), sharex=True)
    data = [("Cu", 3.615, "fcc", 0.55, "Cu (FCC, a = 0.3615 nm): h, k, l unmixed", COLORS[1], ("100", "110")),
            ("Fe", 2.8665, "bcc", 0.35, "α-Fe (BCC, a = 0.2867 nm): h + k + l even", COLORS[0], ("100", "111"))]
    for ax, (el, a, lat, B, title, col, absent) in zip(axs, data):
        rows = _powder(el, a, lat, B)
        for r in rows:
            if r["tth"] > 122:
                continue
            if r["I"] > 0.01:
                ax.vlines(r["tth"], 0, r["I"], color=col, lw=2.4)
                ax.text(r["tth"], r["I"] + 3, f"{r['hkl']}\nN={r['N']}", ha="center", va="bottom", fontsize=7.5)
            elif r["hkl"] in absent:
                ax.vlines(r["tth"], 0, 38, color=GREY, lw=1.0, ls="--")
                ax.text(r["tth"], 40, f"{r['hkl']}\nabsent:\nF = 0", ha="center", va="bottom", fontsize=7, color=GREY)
        ax.set_ylim(0, 135)
        ax.set_ylabel("relative intensity")
        ax.set_title(title, fontsize=9.5, loc="left")
        ax.set_yticks([0, 50, 100])
    axs[1].set_xlim(20, 122)
    axs[1].set_xlabel(r"diffraction angle $2\theta$ (°), Cu K$\alpha$ ($\lambda$ = 0.15406 nm)")
    tbl = ("Cu 111 (worked example)\n"
           r"$f$ = 22.1,  $|F|^2=(4f)^2$ = 7.80×10$^3$" + "\n"
           r"$p$ = 8,  $L_p$ = 12.08,  $e^{-2M}$ = 0.939" + "\n"
           r"$I \propto |F|^2\,p\,L_p\,e^{-2M}$ = 7.08×10$^5$")
    axs[0].text(57, 112, tbl, fontsize=7.5, va="top", ha="left",
                bbox=dict(boxstyle="round,pad=0.35", fc="#F6F6F6", ec=GREY, lw=0.7))
    fig.tight_layout(h_pad=0.6)
    save(fig, "04", "fig-4-3-cu-fe-powder-patterns")


# --------------------------------------------------------------------------- 4.4
def williamson_hall():
    tt = np.array([44.67, 65.02, 82.33, 98.94, 116.37])
    beta = np.array([0.63, 0.81, 1.02, 1.29, 1.71])
    th = np.radians(tt / 2)
    x = 4 * np.sin(th)
    y = np.radians(beta) * np.cos(th)
    slope, icpt = np.polyfit(x, y, 1)
    fig, ax = new_fig(6.4, 4.0)
    xx = np.linspace(0, 3.6, 50)
    ax.plot(xx, icpt + slope * xx, color=COLORS[0], lw=1.6, label="least-squares fit")
    ax.axhline(icpt, color=COLORS[2], ls="--", lw=1.2)
    ax.plot(xx, 0.0045 * xx, color=COLORS[3], ls="--", lw=1.2)
    ax.plot(x, y, "o", color=COLORS[1], ms=7, mec=INK, mew=0.6, zorder=5)
    for xi, yi, lab in zip(x, y, ["110", "200", "211", "220", "310"]):
        ax.text(xi + 0.04, yi - 0.0011, lab, fontsize=8.5, ha="left", va="top")
    ax.plot([0], [icpt], "s", color=COLORS[0], ms=6, zorder=5)
    ax.annotate(r"intercept $K\lambda/D$ = %.5f" % icpt + "\n" + r"$\Rightarrow D$ = 0.9×0.15406/%.5f = %.1f nm"
                % (icpt, 0.9 * 0.15406 / icpt), xy=(0, icpt), xytext=(1.40, 0.0012), fontsize=8.5,
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.8))
    ax.text(2.85, 0.0160, r"slope = $\varepsilon$ = %.5f = %.2f %%" % (slope, slope * 100),
            fontsize=8.5, color=COLORS[0], rotation=0, ha="right")
    ax.text(3.58, icpt - 0.0006, "size only (no strain)", fontsize=8.5, color=COLORS[2], ha="right", va="top")
    ax.text(2.72, 0.0106, "strain only\n(slope 0.0045)", fontsize=8.5, color=COLORS[3], ha="left", va="top")
    ax.set_xlim(0, 3.6)
    ax.set_ylim(0, 0.018)
    ax.set_xlabel(r"$4\sin\theta$")
    ax.set_ylabel(r"$\beta\cos\theta$ (rad)")
    ax.set_title("Ball-milled α-Fe, Cu Kα, instrument-corrected FWHM", fontsize=9.5, loc="left")
    # inset: peak components
    ins = ax.inset_axes([0.04, 0.60, 0.36, 0.36])
    t = np.linspace(-3, 3, 400)
    g_ins = np.exp(-t ** 2 / (2 * 0.25 ** 2))
    lor = 1 / (1 + (t / 0.45) ** 2)
    strain = np.exp(-t ** 2 / (2 * 0.6 ** 2))
    conv = np.convolve(np.convolve(g_ins, lor, "same"), strain, "same")
    conv /= conv.max()
    ins.plot(t, g_ins, color=GREY, lw=1.0, label="instrument")
    ins.plot(t, lor, color=COLORS[2], lw=1.0, label=r"size ($\propto 1/\cos\theta$)")
    ins.plot(t, strain, color=COLORS[3], lw=1.0, label=r"strain ($\propto\tan\theta$)")
    ins.plot(t, conv, color=INK, lw=1.6, label="measured peak")
    ins.set_xticks([])
    ins.set_yticks([])
    ins.set_xlabel(r"$2\theta$", fontsize=7.5, labelpad=1)
    ins.legend(fontsize=6.2, loc="upper right", handlelength=1.2, borderaxespad=0.1)
    ins.set_xlim(-3, 3)
    ins.set_ylim(0, 1.6)
    ins.spines["top"].set_visible(True)
    ins.spines["right"].set_visible(True)
    fig.tight_layout()
    save(fig, "04", "fig-4-4-williamson-hall")


# --------------------------------------------------------------------------- 4.5
def quartz_conductivity_quadric():
    kpar, kperp = 10.4, 6.2
    fig, ax = new_fig(6.0, 5.4)
    th = np.linspace(0, 2 * np.pi, 721)
    k = kperp * np.sin(th) ** 2 + kpar * np.cos(th) ** 2
    for r in (2, 4, 6, 8, 10):
        ax.add_patch(Circle((0, 0), r, fill=False, color="#E6E6E6", lw=0.7, zorder=0))
        ang = np.radians(-100)
        ax.text(r * np.sin(ang) - 0.1, r * np.cos(ang) - 0.1, f"{r}", fontsize=7, color=GREY, ha="center", va="top")
    ax.axvline(0, color=GREY, lw=0.8, zorder=0)
    ax.axhline(0, color=GREY, lw=0.8, zorder=0)
    ax.plot(k * np.sin(th), k * np.cos(th), color=COLORS[0], lw=2.0,
            label=r"$k(\theta)=k_\perp\sin^2\theta+k_\parallel\cos^2\theta$ (W m$^{-1}$ K$^{-1}$)")
    sc = 25.0
    ax.add_patch(Ellipse((0, 0), 2 * sc / np.sqrt(kperp), 2 * sc / np.sqrt(kpar), fill=False, ls="--",
                         color=COLORS[1], lw=1.4))
    ax.plot([], [], color=COLORS[1], lw=1.4, ls="--", label=r"representation quadric, radius $1/\sqrt{k}$ (×25)")
    ax.annotate("", xy=(0, 13.6), xytext=(0, 11.4), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.2))
    ax.text(-0.3, 13.2, "c axis", fontsize=9, ha="right")
    ax.text(-0.3, kpar + 0.15, r"$k_\parallel$ = 10.4", fontsize=8.5, color=COLORS[0], va="bottom", ha="right")
    ax.text(-kperp - 0.15, 0.25, r"$k_\perp$ = 6.2", fontsize=8.5, color=COLORS[0], ha="right")
    # 45 deg point
    k45 = 0.5 * (kpar + kperp)
    d45 = np.array([np.sin(np.radians(45)), np.cos(np.radians(45))])
    ax.plot(*(k45 * d45), "o", color=COLORS[0], ms=6, zorder=6)
    ax.text(k45 * d45[0] + 0.75, k45 * d45[1] - 0.35, r"$k$(45°) = 8.3", fontsize=8.5, color=COLORS[0], va="top")
    # gradient and flux arrows
    L = 12.0
    phi = np.degrees(np.arctan(kperp / kpar))
    dq = np.array([np.sin(np.radians(phi)), np.cos(np.radians(phi))])
    ax.annotate("", xy=L * d45, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=COLORS[2], lw=2.0))
    ax.annotate("", xy=L * dq, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=COLORS[3], lw=2.0))
    ax.text(*(L * d45 + np.array([0.3, -0.1])), r"$-\nabla T$" + "\n(plate normal,\n45° from c)", fontsize=8.5,
            color=COLORS[2], ha="left", va="center")
    ax.text(*(L * dq + np.array([0.25, 0.25])), r"heat flux $\mathbf{q}$, " + f"{phi:.1f}° from c", fontsize=8.5,
            color=COLORS[3], ha="left", va="bottom")
    ax.add_patch(Arc((0, 0), 18.0, 18.0, theta1=45, theta2=90 - phi, color=INK, lw=1.0))
    mid = np.radians(0.5 * (45 + 90 - phi))
    ax.text(10.0 * np.cos(mid) + 0.2, 10.0 * np.sin(mid) + 0.1, f"{45 - phi:.1f}°", fontsize=8.5, ha="left", va="bottom")
    ax.add_patch(Arc((0, 0), 5.0, 5.0, theta1=90 - phi, theta2=90, color=INK, lw=0.8))
    m2 = np.radians(90 - phi / 2)
    ax.text(3.1 * np.cos(m2), 3.1 * np.sin(m2), f"{phi:.1f}°", fontsize=7.5, ha="center", va="bottom")
    ax.legend(loc="upper center", fontsize=7.8, bbox_to_anchor=(0.5, -0.0), ncol=1)
    # inset cubic
    ins = ax.inset_axes([0.0, 0.02, 0.24, 0.24])
    ins.add_patch(Circle((0, 0), 1, fill=False, color=COLORS[0], lw=1.4))
    ins.annotate("", xy=(0.8, 0.8), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=COLORS[2], lw=1.6))
    ins.annotate("", xy=(0.62, 0.62), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=COLORS[3], lw=1.0))
    ins.set_xlim(-1.3, 1.3)
    ins.set_ylim(-1.3, 1.3)
    ins.set_aspect("equal")
    ins.axis("off")
    ins.text(0, 1.18, "cubic crystal (e.g. Cu):\nsphere, flux ∥ gradient", fontsize=7, ha="center", va="bottom")
    ax.set_xlim(-13.0, 13.0)
    ax.set_ylim(-11.5, 14.0)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("α-quartz, plane containing the c axis", fontsize=9.5, loc="left")
    save(fig, "04", "fig-4-5-quartz-conductivity-quadric")


# --------------------------------------------------------------------------- 4.6
ELASTIC = {"W": (522, 204, 161), "Al": (108, 61, 28.5), "Si": (166, 64, 79.6), "Fe": (231, 135, 116),
           "Ni": (247, 147, 125), "Cu": (168, 121, 75.4)}


def _compl(c11, c12, c44):
    d = (c11 - c12) * (c11 + 2 * c12)
    return (c11 + c12) / d, -c12 / d, 1 / c44


def _E(c, J):
    S11, S12, S44 = _compl(*c)
    return 1 / (S11 - 2 * (S11 - S12 - 0.5 * S44) * J)


def _hill(c):
    c11, c12, c44 = c
    S11, S12, S44 = _compl(*c)
    K = (c11 + 2 * c12) / 3
    GV = (c11 - c12 + 3 * c44) / 5
    GR = 5 / (4 * (S11 - S12) + 3 * S44)
    EV, ER = 9 * K * GV / (3 * K + GV), 9 * K * GR / (3 * K + GR)
    return 0.5 * (EV + ER)


def _surface(ax, c, color, title):
    u, v = np.meshgrid(np.linspace(0, 2 * np.pi, 90), np.linspace(0, np.pi, 60))
    n1, n2, n3 = np.cos(u) * np.sin(v), np.sin(u) * np.sin(v), np.cos(v)
    J = n1 ** 2 * n2 ** 2 + n2 ** 2 * n3 ** 2 + n3 ** 2 * n1 ** 2
    E = _E(c, J)
    ax.plot_surface(E * n1, E * n2, E * n3, color=color, alpha=0.85, linewidth=0, shade=True, rstride=2, cstride=2)
    lim = 300
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=22, azim=-55)
    ax.set_axis_off()
    ax.set_title(title, fontsize=8, pad=-2)


def cubic_youngs_modulus():
    fig = plt.figure(figsize=(6.8, 4.0))
    ax = fig.add_axes([0.09, 0.13, 0.56, 0.80])
    psi = np.linspace(0, np.pi / 2, 400)
    s, c_ = np.sin(psi), np.cos(psi)
    J = s ** 4 / 4 + s ** 2 * c_ ** 2
    order = ["W", "Ni", "Fe", "Si", "Cu", "Al"]
    cols = dict(zip(order, [COLORS[7], COLORS[2], COLORS[0], COLORS[3], COLORS[1], COLORS[4]]))
    for el in order:
        E = _E(ELASTIC[el], J)
        ax.plot(np.degrees(psi), E, color=cols[el], lw=1.8)
        yl = E[-1]
        ax.text(91.2, yl, el, color=cols[el], fontsize=9, va="center", weight="bold")
    for el, val in [("Cu", _hill(ELASTIC["Cu"])), ("Fe", _hill(ELASTIC["Fe"]))]:
        ax.axhline(val, color=cols[el], ls="--", lw=1.0)
        dy, va = (4, "bottom") if el == "Fe" else (-4, "top")
        ax.text(2, val + dy, f"{el} polycrystal (Hill) {val:.0f} GPa", fontsize=7.5, color=cols[el], va=va)
    ax.axvline(np.degrees(np.arccos(1 / np.sqrt(3))), color=GREY, lw=0.7, ls=":")
    ax.set_xticks([0, 15, 30, np.degrees(np.arccos(1 / np.sqrt(3))), 75, 90])
    ax.set_xticklabels(["[001]\n0°", "15°", "30°", "[111]\n54.7°", "75°", "[110]\n90°"])
    ax.set_xlim(0, 90)
    ax.set_ylim(0, 450)
    ax.set_ylabel("Young's modulus E (GPa)")
    ax.set_xlabel(r"direction in the (1$\bar1$0) plane, angle from [001]")
    a3 = fig.add_axes([0.72, 0.50, 0.28, 0.44], projection="3d")
    _surface(a3, ELASTIC["Cu"], "#E8A27A", "Cu: E(n) surface\nlobes ⟨111⟩, dimples ⟨100⟩")
    b3 = fig.add_axes([0.72, 0.04, 0.28, 0.44], projection="3d")
    _surface(b3, ELASTIC["W"], "#9AA3AD", "W: sphere (A ≈ 1)\n(drawn at half the scale of Cu)")
    for a_, lim in ((a3, 200), (b3, 420)):
        a_.patch.set_alpha(0)
        a_.set_xlim(-lim, lim)
        a_.set_ylim(-lim, lim)
        a_.set_zlim(-lim, lim)
    save(fig, "04", "fig-4-6-cubic-youngs-modulus")


if __name__ == "__main__":
    fcc_reciprocal_brillouin()
    ewald_sphere()
    cu_fe_powder_patterns()
    williamson_hall()
    quartz_conductivity_quadric()
    cubic_youngs_modulus()
