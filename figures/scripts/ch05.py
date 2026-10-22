"""Figures for Chapter 5 — Defects and Microstructure.

Run from the repository root:  python figures/scripts/ch05.py
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figstyle import COLORS, INK, new_fig, save  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle  # noqa: E402
from scipy.spatial import cKDTree  # noqa: E402

GREY = "#9A9A9A"
HOST = "#C8C8C8"
KB = 8.617e-5


def _atom(ax, p, r, fc, ec=INK, lw=0.6, ls="-", z=3, alpha=1.0):
    ax.add_patch(Circle(p, r, fc=fc, ec=ec, lw=lw, ls=ls, zorder=z, alpha=alpha))


def _arr(ax, p0, p1, color=INK, lw=1.0, ms=8, z=6, style="-|>"):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle=style, mutation_scale=ms, color=color, lw=lw,
                                 shrinkA=0, shrinkB=0, zorder=z))


def _lead(ax, xy, xytext, text, fs=8, ha="center", va="center", color=INK):
    ax.annotate(text, xy=xy, xytext=xytext, fontsize=fs, ha=ha, va=va, color=color, zorder=8,
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7, shrinkA=1, shrinkB=2))


def _perp(ax, x, y, s=0.22, color=INK, lw=1.4, rot=0.0):
    """Dislocation symbol ⊥ centred at (x, y), rotated by rot degrees."""
    c, si = np.cos(np.radians(rot)), np.sin(np.radians(rot))
    R = np.array([[c, -si], [si, c]])
    for seg in (np.array([[-s, 0], [s, 0]]), np.array([[0, 0], [0, 1.3 * s]])):
        q = seg @ R.T + [x, y]
        ax.plot(q[:, 0], q[:, 1], color=color, lw=lw, zorder=7, solid_capstyle="butt")


# --------------------------------------------------------------------------- 5.1
def point_defects():
    fig = plt.figure(figsize=(6.8, 5.0))
    axa = fig.add_axes([0.0, 0.47, 0.5, 0.50])
    axb = fig.add_axes([0.5, 0.47, 0.5, 0.50])
    axc = fig.add_axes([0.0, 0.0, 0.5, 0.40])
    axl = fig.add_axes([0.52, 0.0, 0.48, 0.45])
    for ax in (axa, axb, axc, axl):
        ax.set_aspect("equal")
        ax.axis("off")

    # (a) metal: triangular lattice
    ax = axa
    h = np.sqrt(3) / 2
    P = np.array([[i + 0.5 * (j % 2), j * h] for j in range(7) for i in range(10)], float)
    keep = np.ones(len(P), bool)
    tree = cKDTree(P)

    def site(x, y):
        return tree.query([x, y])[1]

    defects = []  # (position, strength, kind)
    iv = site(1.5, 3 * h)
    keep[iv] = False
    defects.append((P[iv].copy(), -0.06, "vac"))
    isub_s = site(7, 4 * h)
    defects.append((P[isub_s].copy(), -0.06, "small"))
    isub_l = site(6.5, 1 * h)
    defects.append((P[isub_l].copy(), +0.08, "large"))
    p_int = np.array([4.0, 4 * h + h / 3 * 2 - h / 3])  # centroid of a triangle
    p_int = (P[site(4, 4 * h)] + P[site(5, 4 * h)] + P[site(4.5, 5 * h)]) / 3
    defects.append((p_int, +0.22, "self"))
    p_c = (P[site(2, 1 * h)] + P[site(3, 1 * h)] + P[site(2.5, 0)]) / 3
    defects.append((p_c, +0.08, "C"))
    Q = P.copy()
    for d, s, kind in defects:
        v = P - d
        r = np.linalg.norm(v, axis=1)
        m = (r > 1e-6) & (r < 2.3)
        r0 = r[m].min()
        Q[m] += (s * (r0 / r[m]) ** 2)[:, None] * v[m] / r[m][:, None]
    radius = np.full(len(P), 0.40)
    color = np.array([HOST] * len(P), dtype=object)
    radius[isub_s], color[isub_s] = 0.30, "#56B4E9"
    radius[isub_l], color[isub_l] = 0.50, "#E07B6A"
    for k in range(len(P)):
        if keep[k]:
            _atom(ax, Q[k], radius[k], color[k])
    _atom(ax, P[iv], 0.40, "white", ec=GREY, ls="--", lw=0.8)
    _atom(ax, p_int, 0.34, HOST)
    _atom(ax, p_c, 0.14, "#222222")
    # displacement arrows on nearest neighbours
    for d, s, kind in defects:
        v = P - d
        r = np.linalg.norm(v, axis=1)
        nn = np.where((r > 1e-6) & (r < 1.05) & keep)[0]
        for k in nn:
            u = v[k] / r[k]
            sgn = 1 if s > 0 else -1
            base = Q[k] + u * (0.12 if sgn > 0 else 0.30)
            _arr(ax, base, base + sgn * u * 0.26, color="#B22222", lw=0.9, ms=6)
    _lead(ax, P[iv] + [0, 0.4], (1.0, 6.75), "vacancy\n(relax in)", fs=7.5)
    _lead(ax, p_int + [0, 0.35], (4.6, 6.75), "self-interstitial\n(pushed out)", fs=7.5)
    _lead(ax, P[isub_s] + [0.2, 0.25], (8.4, 6.75), "small solute\n(pulled in)", fs=7.5)
    _lead(ax, P[isub_l] + [0.2, -0.45], (7.2, -1.15), "large solute\n(pushed out)", fs=7.5)
    _lead(ax, p_c + [0, -0.18], (2.5, -1.15), "interstitial solute\n(C in Fe)", fs=7.5)
    ax.set_xlim(-0.6, 10.1)
    ax.set_ylim(-1.8, 7.4)
    ax.set_title("(a) elemental metal", fontsize=9.5, loc="left", y=0.98)

    # (b) rock salt: NaCl (left) and AgBr (right)
    ax = axb
    nx, ny = 11, 6
    cat, an = [], []
    for i in range(nx):
        for j in range(ny):
            (cat if (i + j) % 2 == 0 else an).append((i, j))
    rc, ra = 0.24, 0.40
    removed = {(2, 2), (3, 2), (6, 2), (9, 3)}
    special = {(5, 1): "Ca"}
    for (i, j) in an:
        if (i, j) in removed:
            continue
        _atom(ax, (i, j), ra, "#F4B183")
        ax.text(i, j, "−", ha="center", va="center", fontsize=8, zorder=5)
    for (i, j) in cat:
        if (i, j) in removed:
            continue
        if (i, j) in special:
            _atom(ax, (i, j), 0.27, "#009E73")
            ax.text(i, j, "2+", ha="center", va="center", fontsize=6, zorder=5, color="white", weight="bold")
            continue
        _atom(ax, (i, j), rc, "#8FB8DE")
        ax.text(i, j, "+", ha="center", va="center", fontsize=7, zorder=5)
    for (i, j) in removed:
        r = rc if (i + j) % 2 == 0 else ra
        _atom(ax, (i, j), r, "white", ec=GREY, ls="--", lw=0.8)
    # Frenkel interstitial
    pi_ = (8.5, 3.5)
    _atom(ax, pi_, rc, "#8FB8DE")
    ax.text(*pi_, "+", ha="center", va="center", fontsize=7, zorder=5)
    _arr(ax, (9 - 0.12, 3 + 0.12), (8.5 + 0.17, 3.5 - 0.17), color="#B22222", lw=1.0, ms=7)
    ax.plot([7.5, 7.5], [-0.6, 5.6], color=GREY, lw=0.8, ls=":")
    ax.text(3.0, 5.75, "NaCl", fontsize=8.5, ha="center", va="bottom", weight="bold")
    ax.text(9.0, 5.75, "AgBr", fontsize=8.5, ha="center", va="bottom", weight="bold")
    _lead(ax, (2, 2 - 0.25), (1.0, -1.25), r"$\mathrm{V}_{\mathrm{Na}}'$", fs=9.5)
    _lead(ax, (3, 2 - 0.42), (2.6, -1.25), r"$\mathrm{V}_{\mathrm{Cl}}^{\bullet}$", fs=9.5)
    ax.text(1.4, -1.95, "Schottky pair", fontsize=7.5, ha="center")
    _lead(ax, (5, 1 - 0.3), (4.6, -1.25), r"$\mathrm{Ca}_{\mathrm{Na}}^{\bullet}$", fs=9.5)
    _lead(ax, (6, 2 + 0.25), (5.0, 6.55), r"$\mathrm{V}_{\mathrm{Na}}'$ (compensates Ca)", fs=8.5)
    _lead(ax, (8.5, 3.5 + 0.25), (8.6, 6.55), r"$\mathrm{Ag}_i^{\bullet}$", fs=9.5)
    _lead(ax, (9, 3 - 0.25), (9.6, -1.25), r"$\mathrm{V}_{\mathrm{Ag}}'$", fs=9.5)
    ax.text(9.1, -1.95, "Frenkel pair", fontsize=7.5, ha="center")
    ax.text(5.2, -1.95, "aliovalent dopant", fontsize=7.5, ha="center")
    ax.set_xlim(-0.6, 10.6)
    ax.set_ylim(-2.3, 7.2)
    ax.set_title("(b) ionic crystal (rock salt)", fontsize=9.5, loc="left", y=0.98)

    # (c) fluorite ZrO2
    ax = axc
    vac = (3, 2)
    for i in range(7):
        for j in range(5):
            if (i, j) == vac:
                _atom(ax, (i, j), 0.34, "white", ec=GREY, ls="--", lw=0.8)
                continue
            _atom(ax, (i, j), 0.34, "#F4B183")
    ysites = {(2.5, 2.5), (3.5, 1.5)}
    for i in range(6):
        for j in range(4):
            if (i + j) % 2 == 0:
                p = (i + 0.5, j + 0.5)
                if p in ysites:
                    _atom(ax, p, 0.27, "#009E73")
                else:
                    _atom(ax, p, 0.22, "#8FB8DE")
    _lead(ax, (2.5, 2.5 + 0.27), (1.4, 4.85), r"$\mathrm{Y}_{\mathrm{Zr}}'$", fs=9.5)
    _lead(ax, (3.5, 1.5 + 0.27), (5.2, 4.85), r"$\mathrm{Y}_{\mathrm{Zr}}'$", fs=9.5)
    _lead(ax, (3, 2 - 0.34), (2.0, -1.0), r"$\mathrm{V}_{\mathrm{O}}^{\bullet\bullet}$", fs=9.5)
    ax.text(6.6, -1.0, "large: O,  small: Zr", fontsize=7.5, ha="right", va="center", color=INK)
    ax.set_xlim(-0.6, 6.6)
    ax.set_ylim(-1.5, 5.4)
    ax.set_title(r"(c) Y$_2$O$_3$ in fluorite ZrO$_2$", fontsize=9.5, loc="left", y=0.98)

    # legend
    ax = axl
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.text(0.2, 6.7, "Kröger–Vink notation  " + r"$\mathrm{M}_{\mathrm{S}}^{\mathrm{C}}$", fontsize=9.5,
            weight="bold", va="top")
    rows = ["M  species on the site (element; V = vacancy;\n    e, h = electron, hole)",
            "S  site in the perfect crystal (element;\n    i = interstitial position)",
            "C  charge relative to the perfect lattice:\n" + r"    $\bullet$ positive,  $'$ negative,  $\times$ neutral"]
    for k, t in enumerate(rows):
        ax.text(0.2, 5.6 - 1.35 * k, t, fontsize=8, va="top")
    ax.text(0.2, 1.45, r"null $\rightleftharpoons \mathrm{V_{Na}'}+\mathrm{V_{Cl}^{\bullet}}$" + "\n"
            r"$\mathrm{Y_2O_3}\rightarrow 2\mathrm{Y_{Zr}'}+3\mathrm{O_O^{\times}}+\mathrm{V_O^{\bullet\bullet}}$",
            fontsize=8.5, va="top", color=COLORS[0])
    save(fig, "05", "fig-5-1-point-defects")


# --------------------------------------------------------------------------- 5.2
def vacancy_arrhenius():
    fig, ax = new_fig(6.4, 4.2)
    metals = [("Al", 0.67, 933, COLORS[4]), ("Cu", 1.28, 1356, COLORS[1]), ("Ni", 1.79, 1728, COLORS[2]),
              ("W", 3.6, 3695, COLORS[0])]
    ax.axhspan(-4, -3, xmin=0, xmax=1, color="#E9E9E9", zorder=0)
    ax.text(3.45, -3.5, "measured c$_v$ of most metals near $T_m$ (10$^{-4}$–10$^{-3}$)", fontsize=7.5,
            ha="right", va="center", color="#555555")
    for name, H, Tm, col in metals:
        x = np.linspace(1000 / Tm, 3.5, 200)
        y = -H / (KB * 1000 / x) / np.log(10)
        ax.plot(x, y, color=col, lw=1.8)
        y_m = -H / (KB * Tm) / np.log(10)
        ax.plot(1000 / Tm, y_m, "o", color=col, ms=6, zorder=5)
        ax.text(1000 / Tm - 0.04, y_m + 0.25, f"$T_m$", fontsize=7.5, color=col, ha="right", va="bottom")
        # direct label along the line
        xl = {"Al": 2.4, "Cu": 2.25, "Ni": 1.75, "W": 0.82}[name]
        yl = -H / (KB * 1000 / xl) / np.log(10)
        dy, va = (-0.5, "top") if name == "Ni" else (0.2, "bottom")
        ax.text(xl + (0.22 if name == "Ni" else 0.06), yl + dy, f"{name} ({H} eV)", color=col, fontsize=8.5, ha="left", va=va,
                weight="bold")
    # NaCl Schottky
    x = np.linspace(1000 / 1074, 3.5, 200)
    y = -2.3 / (2 * KB * 1000 / x) / np.log(10)
    ax.plot(x, y, color=COLORS[3], lw=1.6, ls="--")
    ax.plot(1000 / 1074, -2.3 / (2 * KB * 1074) / np.log(10), "o", color=COLORS[3], ms=6, mfc="white", zorder=5)
    ax.text(1.95, -2.3 / (2 * KB * 1000 / 1.95) / np.log(10) - 0.35, r"NaCl Schottky, $e^{-2.3\,\mathrm{eV}/2k_BT}$",
            color=COLORS[3], fontsize=8.5, va="top", ha="left")
    ax.plot([1000 / 1074, 3.5], [-4, -4], color=COLORS[3], ls=":", lw=1.6)
    ax.text(3.45, -4.15, "cation vacancies from 100 ppm Ca$^{2+}$ in NaCl (extrinsic)", color=COLORS[3],
            fontsize=7.5, ha="right", va="top")
    # Cu at 1273 K with entropy factor
    xc = 1000 / 1273
    ax.plot(xc, np.log10(3.8e-5), "D", color=COLORS[1], ms=6, mec=INK, zorder=6)
    ax.annotate("Cu, 1000 °C, with $e^{\\Delta S_v/k_B}$ = 4.48:\n$c_v$ = 3.8×10$^{-5}$", xy=(xc, np.log10(3.8e-5)),
                xytext=(1.05, -1.2), fontsize=7.5, color=COLORS[1], va="top",
                arrowprops=dict(arrowstyle="-", color=COLORS[1], lw=0.7))
    ax.set_xlim(0.2, 3.5)
    ax.set_ylim(-22, -1)
    ax.set_yticks(range(-22, -1, 2))
    ax.set_xlabel("1000/T (K$^{-1}$)")
    ax.set_ylabel(r"$\log_{10} c_v$   ($c_v=e^{-\Delta H_v/k_BT}$, prefactor 1)")
    top = ax.secondary_xaxis("top", functions=(lambda x: 1000 / np.maximum(x, 1e-3) - 273.15,
                                               lambda t: 1000 / (t + 273.15)))
    ticksC = [2000, 1000, 600, 400, 200, 100, 25]
    top.set_xlabel("temperature (°C)")
    top.xaxis.set_major_locator(plt.FixedLocator(ticksC))
    save(fig, "05", "fig-5-2-vacancy-arrhenius")


# --------------------------------------------------------------------------- 5.3
def _edge_positions(nx=6, rows=(-4, 3), b=1.0, nu=0.3):
    pos = {}
    for i in range(-nx, nx + 1):
        for j in range(rows[0], rows[1] + 1):
            x, y = float(i), j + 0.5
            r2 = x * x + y * y
            th = np.arctan2(y, x)
            ux = b / (2 * np.pi) * (th + x * y / (2 * (1 - nu) * r2))
            uy = -b / (2 * np.pi) * ((1 - 2 * nu) / (4 * (1 - nu)) * np.log(r2) + (x * x - y * y) / (4 * (1 - nu) * r2))
            pos[(i, j)] = np.array([x + ux, y + uy])
    return pos


def _above(i, j):
    """Neighbour above atom (i, j) in the dislocated crystal."""
    if j == -1 and i <= 0:
        return (i - 1, 0)
    return (i, j + 1)


def _below(i, j):
    if j == 0 and i <= -1:
        return (i + 1, -1)
    if j == 0 and i == 0:
        return None
    return (i, j - 1)


def _oblique(p):
    x, y, z = p
    return np.array([x + 0.42 * y, z + 0.30 * y])


def dislocations_burgers():
    fig = plt.figure(figsize=(6.8, 5.0))
    ax1 = fig.add_axes([0.0, 0.53, 0.5, 0.44])
    ax2 = fig.add_axes([0.5, 0.53, 0.5, 0.44])
    ax3 = fig.add_axes([0.0, 0.0, 0.5, 0.46])
    ax4 = fig.add_axes([0.5, 0.0, 0.5, 0.46])
    for ax in (ax1, ax2, ax3, ax4):
        ax.set_aspect("equal")
        ax.axis("off")
    rows = (-4, 3)
    # (a) edge dislocation, real crystal
    pos = _edge_positions(rows=rows)
    ax = ax1
    for (i, j), p in pos.items():
        if (i + 1, j) in pos:
            q = pos[(i + 1, j)]
            ax.plot([p[0], q[0]], [p[1], q[1]], color="#BBBBBB", lw=0.8, zorder=1)
        a = _above(i, j)
        if a in pos and j < rows[1]:
            q = pos[a]
            ax.plot([p[0], q[0]], [p[1], q[1]], color="#BBBBBB", lw=0.8, zorder=1)
    P = np.array(list(pos.values()))
    ax.scatter(P[:, 0], P[:, 1], s=16, color="#555555", zorder=2)
    # extra half-plane highlight
    hp = np.array([pos[(0, j)] for j in range(0, rows[1] + 1)])
    ax.plot(hp[:, 0], hp[:, 1], color=COLORS[0], lw=2.2, zorder=3)
    ax.scatter(hp[:, 0], hp[:, 1], s=20, color=COLORS[0], zorder=4)
    _perp(ax, 0.0, -0.05, s=0.28, color="#B22222", lw=2.0)
    # Burgers circuit: 4 up, 5 right, 4 down, 4 left (closes)
    path = [(-2, -3)]
    cur = (-2, -3)
    for step in ["u"] * 4 + ["r"] * 5 + ["d"] * 4 + ["l"] * 4:
        i, j = cur
        cur = {"u": _above(i, j), "d": _below(i, j), "r": (i + 1, j), "l": (i - 1, j)}[step]
        path.append(cur)
    C = np.array([pos[k] for k in path])
    ax.plot(C[:, 0], C[:, 1], color=COLORS[1], lw=1.8, zorder=5)
    for k0, k1 in [(1, 2), (6, 7), (11, 12), (15, 16)]:
        _arr(ax, C[k0], C[k1], color=COLORS[1], lw=1.8, ms=10)
    ax.plot(*C[0], "s", color=COLORS[1], ms=6, zorder=6)
    ax.text(C[0][0] - 0.25, C[0][1] - 0.3, "S = F", fontsize=8, color=COLORS[1], ha="right", va="top")
    ax.text(0.0, 4.2, "4 up, 5 right, 4 down, 4 left: circuit closes", fontsize=7.5, color=COLORS[1], ha="center")
    ax.text(0.45, 2.6, "extra\nhalf-plane", fontsize=7.5, color=COLORS[0], ha="left")
    ax.set_xlim(-6.9, 6.5)
    ax.set_ylim(-4.7, 4.8)
    ax.set_title("(a) edge dislocation: real crystal", fontsize=9.5, loc="left")

    # perfect reference crystal
    ax = ax2
    for i in range(-6, 7):
        ax.plot([i, i], [rows[0] + 0.5, rows[1] + 0.5], color="#BBBBBB", lw=0.8, zorder=1)
    for j in range(rows[0], rows[1] + 1):
        ax.plot([-6, 6], [j + 0.5, j + 0.5], color="#BBBBBB", lw=0.8, zorder=1)
    X, Y = np.meshgrid(np.arange(-6, 7), np.arange(rows[0], rows[1] + 1) + 0.5)
    ax.scatter(X, Y, s=16, color="#555555", zorder=2)
    S = np.array([-2.0, -2.5])
    pts = [S]
    for d, n in [((0, 1), 4), ((1, 0), 5), ((0, -1), 4), ((-1, 0), 4)]:
        for _ in range(n):
            pts.append(pts[-1] + np.array(d, float))
    Cp = np.array(pts)
    ax.plot(Cp[:, 0], Cp[:, 1], color=COLORS[1], lw=1.8, zorder=5)
    for k0, k1 in [(1, 2), (6, 7), (11, 12), (15, 16)]:
        _arr(ax, Cp[k0], Cp[k1], color=COLORS[1], lw=1.8, ms=10)
    ax.plot(*S, "s", color=COLORS[1], ms=6, zorder=6)
    F = Cp[-1]
    ax.plot(*F, "o", color=COLORS[1], ms=6, zorder=6)
    _arr(ax, F, S, color="#B22222", lw=2.2, ms=12, z=7)
    ax.text(S[0] - 0.2, S[1] - 0.3, "S", fontsize=8, color=COLORS[1], ha="right", va="top")
    ax.text(F[0] + 0.1, F[1] - 0.3, "F", fontsize=8, color=COLORS[1], ha="left", va="top")
    ax.text(-1.5, -4.1, r"$\mathbf{b}$ = FS, ⊥ line", fontsize=8.5, color="#B22222", ha="center", va="top")
    ax.text(0.0, 4.2, "same steps in a perfect crystal: fails to close by b", fontsize=7.5, color=COLORS[1],
            ha="center")
    ax.set_xlim(-6.5, 6.5)
    ax.set_ylim(-4.7, 4.8)
    ax.set_title("perfect reference crystal", fontsize=9.5, loc="left")

    # (b) screw dislocation block (oblique projection)
    ax = ax3
    Wd, D, H, b = 4.0, 4.0, 2.4, 0.6
    xc, yc = 2.0, 2.0

    def phi(x, y):
        a = np.degrees(np.arctan2(y - yc, x - xc))
        return np.mod(a + 90.0, 360.0)

    def ztop(x, y):
        return H - b + b * phi(x, y) / 360.0

    # top surface quads, painter's order (back to front)
    n = 40
    xs = np.linspace(0, Wd, n + 1)
    ys = np.linspace(0, D, n + 1)
    quads = []
    for iy in range(n - 1, -1, -1):
        for ix in range(n):
            x0, x1, y0, y1 = xs[ix], xs[ix + 1], ys[iy], ys[iy + 1]
            xm, ym = 0.5 * (x0 + x1), 0.5 * (y0 + y1)
            if abs(xm - xc) < 1e-9:
                continue
            # evaluate z on the same side of the cut as the quad centre
            def zt(x, y):
                if y < yc and (x - xc) * (xm - xc) < 0:
                    x = xc + 1e-6 * np.sign(xm - xc)
                return ztop(x, y)
            corners = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
            pr = np.array([_oblique((cx, cy, zt(cx, cy))) for cx, cy in corners])
            shade = 0.80 + 0.15 * phi(xm, ym) / 360.0
            quads.append(Polygon(pr, closed=True, fc=(shade, shade, min(1, shade + 0.05)), ec="none", zorder=1))
    for q in quads:
        ax.add_patch(q)
    # step face along the cut (x = xc, 0 <= y <= yc), facing +x
    sf = np.array([_oblique(p) for p in [(xc, 0, H - b), (xc, yc, H - b + b / 2 * 0 + 0.0), (xc, yc, H),
                                         (xc, 0, H)]])
    ax.add_patch(Polygon(sf, closed=True, fc="#9DB4CC", ec=INK, lw=0.8, zorder=2))

    def side_profile(xy_list, zfun):
        return np.array([_oblique((x, y, zfun(x, y))) for x, y in xy_list])

    # front face y = 0: left part and right part
    xl = np.linspace(0, xc - 1e-6, 30)
    xr = np.linspace(xc + 1e-6, Wd, 30)
    for xx in (xl, xr):
        topp = side_profile([(x, 0.0) for x in xx], ztop)
        bot = side_profile([(x, 0.0) for x in xx[::-1]], lambda x, y: ztop(x, y) - H)
        ax.add_patch(Polygon(np.vstack([topp, bot]), closed=True, fc="#DCE6F0", ec=INK, lw=0.9, zorder=3))
        for kk in range(1, 4):
            tr = side_profile([(x, 0.0) for x in xx], lambda x, y, kk=kk: ztop(x, y) - kk * b)
            ax.plot(tr[:, 0], tr[:, 1], color="#7A8FA6", lw=0.8, zorder=4)
    # right face x = Wd
    yy = np.linspace(0, D, 40)
    topp = side_profile([(Wd, y) for y in yy], ztop)
    bot = side_profile([(Wd, y) for y in yy[::-1]], lambda x, y: ztop(x, y) - H)
    ax.add_patch(Polygon(np.vstack([topp, bot]), closed=True, fc="#C5D3E2", ec=INK, lw=0.9, zorder=3))
    for kk in range(1, 4):
        tr = side_profile([(Wd, y) for y in yy], lambda x, y, kk=kk: ztop(x, y) - kk * b)
        ax.plot(tr[:, 0], tr[:, 1], color="#7A8FA6", lw=0.8, zorder=4)
    # top outline (back and left edges)
    for edge in ([(x, D) for x in np.linspace(0, Wd, 30)], [(0, y) for y in np.linspace(0, D, 30)]):
        e = side_profile(edge, ztop)
        ax.plot(e[:, 0], e[:, 1], color=INK, lw=0.9, zorder=3)
    # dislocation line
    lt = _oblique((xc, yc, ztop(xc + 0.01, yc + 0.01)))
    lb = _oblique((xc, yc, ztop(xc + 0.01, yc + 0.01) - H))
    ax.plot([lt[0], lb[0]], [lt[1], lb[1]], color="#B22222", lw=1.6, ls="--", zorder=5)
    up = _oblique((xc, yc, H + 0.9))
    ax.plot([lt[0], up[0]], [lt[1], up[1]], color="#B22222", lw=2.0, zorder=6)
    ax.text(up[0] + 0.1, up[1], "screw dislocation line", fontsize=7.5, color="#B22222", va="center")
    # circuit on top surface
    rr = 1.25
    pts = [(xc + 0.04, yc - rr), (xc + rr, yc - rr), (xc + rr, yc + rr), (xc - rr, yc + rr), (xc - rr, yc - rr),
           (xc - 0.04, yc - rr)]
    dense = []
    for (a0, b0), (a1, b1) in zip(pts[:-1], pts[1:]):
        for t in np.linspace(0, 1, 25):
            dense.append((a0 + t * (a1 - a0), b0 + t * (b1 - b0)))
    cc = side_profile(dense, lambda x, y: ztop(x, y) + 0.02)
    ax.plot(cc[:, 0], cc[:, 1], color=COLORS[1], lw=1.8, zorder=7)
    _arr(ax, cc[60], cc[64], color=COLORS[1], lw=1.8, ms=9, z=8)
    p_end = _oblique((xc - 0.04, yc - rr, H))
    p_start = _oblique((xc + 0.04, yc - rr, H - b))
    _arr(ax, p_end, p_start, color="#B22222", lw=2.0, ms=10, z=9)
    ax.text(p_end[0] - 1.0, 0.5 * (p_end[1] + p_start[1]) + 0.15, r"$\mathbf{b}$ ∥ line", fontsize=8.5,
            color="#B22222", ha="right", va="center")
    ax.text(0.2, -0.75, "front-right quarter sheared down by b;\nplanes form one helical ramp", fontsize=7.5,
            va="top")
    ax.set_xlim(-0.6, 6.4)
    ax.set_ylim(-1.7, 4.6)
    ax.set_title("(b) screw dislocation", fontsize=9.5, loc="left")

    # (c) loop in slip plane (top view) + surface step
    ax = ax4
    ax.add_patch(Rectangle((-2.6, -2.2), 5.2, 4.4, fc="#F3F3F3", ec=GREY, lw=0.8, zorder=0))
    R = 1.45
    t = np.linspace(0, 2 * np.pi, 200)
    ax.plot(R * np.cos(t), R * np.sin(t), color="#B22222", lw=2.0, zorder=3)
    ax.text(0, 0, "slipped\n(by b)", fontsize=7.5, ha="center", va="center", color="#555555")
    _arr(ax, (-0.55, -0.65), (0.55, -0.65), color=INK, lw=2.0, ms=11)
    ax.text(0.0, -0.85, r"$\mathbf{b}$", fontsize=10, ha="center", va="top")
    _perp(ax, R, 0, s=0.18, color=INK, lw=1.6, rot=-90)
    _perp(ax, -R, 0, s=0.18, color=INK, lw=1.6, rot=90)
    ax.text(R + 0.35, 0.0, "edge\n(b ⊥ line)", fontsize=7.5, ha="left", va="center")
    ax.text(-R - 0.35, 0.0, "edge", fontsize=7.5, ha="right", va="center")
    ax.text(0, R + 0.15, "screw (b ∥ line)", fontsize=7.5, ha="center", va="bottom")
    ax.text(0, -R - 0.15, "screw", fontsize=7.5, ha="center", va="top")
    for ang in (45, 135, 225, 315):
        a = np.radians(ang)
        p = np.array([np.cos(a), np.sin(a)])
        _arr(ax, R * p * 1.03, R * p * 1.32, color=COLORS[0], lw=1.2, ms=8)
    ax.text(1.32, 1.32, "mixed", fontsize=7.5, ha="left", va="bottom", color=INK)
    ax.text(-2.5, 2.05, "glide\nexpansion\nunder τ", fontsize=7.5, color=COLORS[0], va="top")
    _arr(ax, (-1.0, 2.55), (1.0, 2.55), color=INK, lw=1.2, ms=9)
    ax.text(1.1, 2.55, "τ on crystal above the plane", fontsize=7.5, va="center")
    ax.text(-2.5, -2.35, "top view of slip plane", fontsize=7.5, va="top", color="#555555")
    # surface step sketch
    ox, oy = 3.3, -2.0
    w, hh = 2.6, 1.0
    sh = 0.35
    ax.add_patch(Polygon([(ox, oy), (ox + w, oy), (ox + w, oy + hh), (ox, oy + hh)], fc="#DCE6F0", ec=INK, lw=0.8))
    ax.add_patch(Polygon([(ox + sh, oy + hh), (ox + w + sh, oy + hh), (ox + w + sh, oy + 2 * hh),
                          (ox + sh, oy + 2 * hh)], fc="#C5D3E2", ec=INK, lw=0.8))
    ax.plot([ox - 0.15, ox + w + 0.5], [oy + hh, oy + hh], color="#B22222", lw=0.8, ls="--")
    ax.annotate("", xy=(ox + w + sh, oy + hh + 0.5), xytext=(ox + w, oy + hh + 0.5),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=0.8, shrinkA=0, shrinkB=0, mutation_scale=6))
    ax.text(ox + w / 2, oy + 2 * hh + 0.12, "loop has exited:\nslip step of\nheight b at surface",
            fontsize=7.5, ha="center", va="bottom")
    ax.text(ox + w + sh + 0.08, oy + hh + 0.5, "b", fontsize=8.5, va="center")
    ax.set_xlim(-2.7, 6.4)
    ax.set_ylim(-2.8, 3.0)
    ax.set_title("(c) dislocation loop: edge, screw and mixed", fontsize=9.5, loc="left")
    save(fig, "05", "fig-5-3-dislocations-burgers")


# --------------------------------------------------------------------------- 5.4
def _rs(u):
    u = np.clip(u, 1e-9, None)
    return np.where(u < 1, u * (1 - np.log(u)), 1.0)


def gb_energy_misorientation():
    g_m, th_m = 0.60, 15.0
    th = np.linspace(0.0, 75, 3001)
    gamma = g_m * _rs(th / th_m)
    cusps = [("Σ9", 38.94, 0.50, 5.0), ("Σ11", 50.48, 0.30, 4.5), ("Σ3", 70.53, 0.03, 8.7)]
    for name, t0, gc, w in cusps:
        f = gc + (g_m - gc) * _rs(np.abs(th - t0) / w)
        gamma = np.minimum(gamma, f)
    fig, ax = new_fig(6.4, 4.0)
    ax.axvspan(0, 15, color="#EEF3F8", zorder=0)
    ax.text(7.5, 0.77, "low-angle\n(dislocation walls)", ha="center", va="top", fontsize=8.5)
    ax.text(45, 0.77, "high-angle", ha="center", va="top", fontsize=8.5)
    ax.plot(th, gamma, color=COLORS[0], lw=2.0)
    ax.text(10.5, 0.36, r"Read–Shockley" + "\n" + r"$\gamma=\gamma_0\theta(A-\ln\theta)$", fontsize=8.5,
            color=COLORS[0], ha="left")
    ax.text(25, 0.62, "general boundaries ≈ 0.6 J m$^{-2}$", fontsize=8, color=INK, ha="left", va="bottom")
    for name, t0, gc, w in cusps:
        ax.plot([t0, t0], [0, gc], color=GREY, lw=0.7, ls=":")
        lab = {"Σ9": "Σ9\n38.9°", "Σ11": "Σ11\n50.5°", "Σ3": "Σ3 coherent twin\n70.5° about ⟨110⟩"}[name]
        if name == "Σ3":
            ax.text(t0 - 1.0, 0.10, lab, fontsize=7.5, ha="right", va="bottom")
        else:
            ax.text(t0 + 0.6, gc - 0.01, lab, fontsize=7.5, ha="left", va="top")
    ax.set_xlim(0, 75)
    ax.set_ylim(0, 0.8)
    ax.set_xlabel("misorientation θ about a ⟨110⟩ tilt axis (degrees)")
    ax.set_ylabel(r"boundary energy (J m$^{-2}$), Cu-like")
    # inset: low-angle tilt boundary
    ins = ax.inset_axes([0.25, 0.05, 0.36, 0.42])
    ins.set_aspect("equal")
    ins.axis("off")
    ang = np.radians(8)
    for side in (-1, 1):
        for k in range(-6, 7):
            y0 = k * 0.5
            xx = np.linspace(0.12 * side, side * 2.0, 2)
            ins.plot(xx, y0 + np.tan(ang) * np.abs(xx), color="#888888", lw=0.7)
    ins.plot([0, 0], [-3.0, 3.0], color=GREY, lw=0.6, ls=":")
    for k in range(-2, 3):
        _perp(ins, 0, k * 1.0 - 0.1, s=0.14, color="#B22222", lw=1.4)
    ins.annotate("", xy=(0.35, 1.0), xytext=(0.35, 0.0),
                 arrowprops=dict(arrowstyle="<->", color=INK, lw=0.8, shrinkA=0, shrinkB=0, mutation_scale=6))
    ins.text(0.45, 0.5, "D = b/θ", fontsize=7.5, va="center")
    ins.text(0, -2.7, "θ = 2°, D = 8.2 nm for Al\n(tilt exaggerated)", fontsize=7.5, ha="center", va="top")
    ins.set_xlim(-2.1, 2.1)
    ins.set_ylim(-3.6, 3.1)
    save(fig, "05", "fig-5-4-gb-energy-misorientation")


# --------------------------------------------------------------------------- 5.5
def _dots(ax, P, color, s=10, z=2):
    P = np.asarray(P)
    if len(P):
        ax.scatter(P[:, 0], P[:, 1], s=s, color=color, zorder=z, linewidths=0)


def phase_boundaries():
    fig = plt.figure(figsize=(6.8, 5.0))
    axs = [fig.add_axes([0.01 + 0.33 * i, 0.55, 0.31, 0.40]) for i in range(3)]
    MAT, PPT = "#8C8C8C", "#E07B2A"
    for ax in axs:
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_xlim(-4.6, 4.6)
        ax.set_ylim(-4.6, 4.9)
        ax.axvline(0, color=GREY, lw=0.6, ls=":", ymax=0.93)
    ny = range(-4, 5)
    # (a) coherent
    ax = axs[0]
    sp, lam = 1.07, 1.3
    M = [(x, y) for x in np.arange(-4, 0) for y in ny]
    Pp = []
    for x in np.arange(0.5, 4.6, sp):
        f = 1 + (sp - 1) * (1 - np.exp(-x / lam))
        for y in ny:
            if abs(y * f) <= 4.4:
                Pp.append((x, y * f))
    _dots(ax, M, MAT)
    _dots(ax, Pp, PPT)
    for y in ny:
        xx = np.linspace(0, 4.4, 30)
        f = 1 + (sp - 1) * (1 - np.exp(-xx / lam))
        yy = y * f
        m = np.abs(yy) <= 4.4
        ax.plot(np.r_[-4, xx[m]], np.r_[y, yy[m]], color="#BBBBBB", lw=0.6, zorder=1)
    ax.text(0, 4.85, "(a) coherent", fontsize=9, ha="center", va="top", weight="bold")
    ax.text(0, -4.7, "δ < ~1 %, γ$_{int}$ < 0.2 J m$^{-2}$", fontsize=7.5, ha="center", va="top")
    # (b) semicoherent
    ax = axs[1]
    sp = 7 / 6
    _dots(ax, M, MAT)
    prow = [k * sp for k in range(-3, 4)]
    for yp in prow:
        j = int(np.round(yp))
        xx = np.linspace(0, 4.4, 30)
        yy = yp + (j - yp) * np.exp(-xx / 0.6)
        ax.plot(np.r_[-4, xx], np.r_[j, yy], color="#BBBBBB", lw=0.6, zorder=1)
        _dots(ax, [(x, yp + (j - yp) * np.exp(-x / 0.6)) for x in np.arange(0.5, 4.6, sp)], PPT)
    partners = {int(np.round(yp)) for yp in prow}
    for y in ny:
        if y not in partners:
            ax.plot([-4, -0.25], [y, y], color="#BBBBBB", lw=0.6, zorder=1)
            _perp(ax, -0.18, y, s=0.32, color="#B22222", lw=1.6, rot=90)
    ax.text(0, 4.85, "(b) semicoherent", fontsize=9, ha="center", va="top", weight="bold")
    ax.text(0, -4.7, "misfit dislocations, S = b/|δ|\nγ/γ′ in Ni superalloy: δ = 0.3 %, S ≈ 85 nm",
            fontsize=7.5, ha="center", va="top")
    # (c) incoherent
    ax = axs[2]
    rng = np.random.default_rng(3)
    Mj = [(x + rng.normal(0, 0.12) * (x > -1.2), y + rng.normal(0, 0.12) * (x > -1.2)) for x, y in M]
    _dots(ax, Mj, MAT)
    a = np.radians(27)
    R = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
    pts = []
    for i in range(-8, 9):
        for j in range(-8, 9):
            p = R @ (np.array([i, j]) * 0.83) + [2.4, 0.2]
            if 0.35 < p[0] < 4.5 and abs(p[1]) < 4.4:
                if p[0] < 1.0:
                    p = p + rng.normal(0, 0.12, 2)
                pts.append(p)
    _dots(ax, pts, PPT)
    ax.text(0, 4.85, "(c) incoherent", fontsize=9, ha="center", va="top", weight="bold")
    ax.text(0, -4.7, "no lattice continuity\nγ$_{int}$ ≈ 0.5–1 J m$^{-2}$", fontsize=7.5, ha="center", va="top")

    # bottom: Al-4Cu sequence
    axq = fig.add_axes([0.0, 0.20, 1.0, 0.27])
    axq.set_aspect("equal")
    axq.axis("off")
    axq.set_xlim(0, 20)
    axq.set_ylim(-0.6, 4.2)
    centres = [2.3, 7.3, 12.3, 17.3]
    titles = ["GP zone\n(one Cu layer, coherent)", "θ″\n(coherent plate)", "θ′\n(semicoherent plate)",
              "θ, Al$_2$Cu\n(incoherent, equiaxed)"]
    for cx, tt in zip(centres, titles):
        X, Y = np.meshgrid(np.arange(cx - 1.75, cx + 1.8, 0.35), np.arange(0.2, 3.0, 0.35))
        axq.scatter(X, Y, s=3, color="#B5B5B5", zorder=1, linewidths=0)
        axq.text(cx, 3.15, tt, fontsize=7.5, ha="center", va="bottom")
    cy = 1.6
    c0 = centres[0]
    axq.scatter(np.arange(c0 - 0.7, c0 + 0.71, 0.35), np.full(5, cy), s=12, color=PPT, zorder=3)
    c1 = centres[1]
    axq.add_patch(Rectangle((c1 - 1.05, cy - 0.27), 2.1, 0.54, fc=PPT, ec="none", alpha=0.85, zorder=2))
    c2 = centres[2]
    axq.add_patch(Rectangle((c2 - 1.45, cy - 0.35), 2.9, 0.7, fc=PPT, ec="none", alpha=0.85, zorder=2))
    for xe in (c2 - 1.45, c2 + 1.45):
        _perp(axq, xe + (0.18 if xe < c2 else -0.18), cy, s=0.16, color="#B22222", lw=1.4,
              rot=90 if xe < c2 else -90)
    c3 = centres[3]
    th = np.linspace(0, 2 * np.pi, 60)
    rr = 1.05 + 0.10 * np.sin(3 * th) + 0.06 * np.cos(5 * th)
    axq.add_patch(Polygon(np.c_[c3 + rr * np.cos(th), cy + 0.95 * rr * np.sin(th)], fc=PPT, ec="none", alpha=0.85,
                          zorder=2))
    for xa in (4.4, 9.4, 14.4):
        _arr(axq, (xa, cy), (xa + 0.8, cy), color=INK, lw=1.2, ms=9)
    _arr(axq, (0.6, -0.25), (19.4, -0.25), color=INK, lw=1.0, ms=9)
    axq.text(10, -0.35, "ageing time / particle size", fontsize=8, ha="center", va="top")

    # strength vs ageing time
    axy = fig.add_axes([0.10, 0.03, 0.84, 0.12])
    t = np.linspace(-1, 3.2, 300)
    ys = 0.25 + 0.75 * np.exp(-((t - 1.3) / 0.9) ** 2)
    axy.plot(t, ys, color=COLORS[0], lw=1.8)
    axy.axvline(1.3, color=GREY, lw=0.7, ls=":")
    axy.text(0.6, 1.12, "peak strength: θ″ + θ′", fontsize=7.5, va="top", ha="right")
    axy.set_yticks([])
    axy.set_xticks([])
    axy.set_ylabel("yield\nstrength", fontsize=8)
    axy.set_xlabel("log ageing time", fontsize=8, labelpad=1)
    axy.set_xlim(-1, 3.2)
    axy.set_ylim(0, 1.15)
    save(fig, "05", "fig-5-5-phase-boundaries")


# --------------------------------------------------------------------------- 5.6
def _make_micro(seed, nseed, W, Hh, lloyd=3):
    rng = np.random.default_rng(seed)
    S = rng.uniform([0, 0], [W, Hh], (nseed, 2))
    gx, gy = np.meshgrid(np.linspace(0, W, 300), np.linspace(0, Hh, 210))
    G = np.c_[gx.ravel(), gy.ravel()]
    for _ in range(lloyd):
        lab = cKDTree(S).query(G)[1]
        for k in range(nseed):
            m = lab == k
            if m.any():
                S[k] = G[m].mean(axis=0)
    return S


def stereology_grid():
    W, Hh = 500.0, 350.0  # micrometres
    ylines = np.linspace(Hh * 0.1, Hh * 0.9, 5)
    best = None
    xs = np.linspace(0, W, 20001)
    for seed in range(200):
        nseed = 262 + seed % 12
        S = _make_micro(seed, nseed, W, Hh)
        tree = cKDTree(S)
        count = 0
        for yl in ylines:
            lab = tree.query(np.c_[xs, np.full_like(xs, yl)])[1]
            count += int(np.sum(lab[1:] != lab[:-1]))
        if best is None or abs(count - 125) < abs(best[2] - 125):
            best = (seed, S, count)
        if count == 125:
            break
    seed, S = best[0], best[1]
    tree = cKDTree(S)
    # grid of 20 x 20 points
    gxs = np.linspace(W / 40, W - W / 40, 20)
    gys = np.linspace(Hh / 40, Hh - Hh / 40, 20)
    GX, GY = np.meshgrid(gxs, gys)
    glab = tree.query(np.c_[GX.ravel(), GY.ravel()])[1]
    rng = np.random.default_rng(seed + 100)
    order = rng.permutation(len(S))
    pearl = set()
    n_in = 0
    # raster for area fraction
    rx, ry = np.meshgrid(np.linspace(0, W, 1000), np.linspace(0, Hh, 700))
    rlab = tree.query(np.c_[rx.ravel(), ry.ravel()])[1].reshape(rx.shape)
    counts = np.bincount(glab, minlength=len(S))
    for k in order:
        if n_in + counts[k] <= 72:
            pearl.add(k)
            n_in += counts[k]
            if n_in == 72 and np.isin(rlab, list(pearl)).mean() > 0.16:
                break
    ispearl = np.isin(rlab, list(pearl))
    area_frac = ispearl.mean()
    # image: ferrite light (slight per-grain tint), pearlite dark with lamellae
    tint = 0.90 + 0.06 * np.random.default_rng(1).random(len(S))
    img = tint[rlab]
    ang = np.random.default_rng(2).uniform(0, np.pi, len(S))
    lam = np.cos(2 * np.pi * (rx * np.cos(ang[rlab]) + ry * np.sin(ang[rlab])) / 2.5)
    img = np.where(ispearl, 0.33 + 0.10 * lam, img)
    edge = np.zeros_like(rlab, bool)
    edge[:, 1:] |= rlab[:, 1:] != rlab[:, :-1]
    edge[1:, :] |= rlab[1:, :] != rlab[:-1, :]
    img = np.where(edge, 0.12, img)

    fig = plt.figure(figsize=(6.8, 4.1))
    ax = fig.add_axes([0.0, 0.17, 0.70, 0.80])
    ax.imshow(img, cmap="gray", vmin=0, vmax=1, extent=(0, W, 0, Hh), origin="lower", interpolation="nearest")
    xs = np.linspace(0, W, 20001)
    total = 0
    for yl in ylines:
        lab = tree.query(np.c_[xs, np.full_like(xs, yl)])[1]
        ch = np.where(lab[1:] != lab[:-1])[0]
        total += len(ch)
        ax.plot([0, W], [yl, yl], color=COLORS[4], lw=1.0)
        xc = 0.5 * (xs[ch] + xs[ch + 1])
        ax.vlines(xc, yl - 5, yl + 5, color=COLORS[1], lw=1.4)
    inp = np.isin(glab, list(pearl))
    ax.scatter(GX.ravel()[~inp], GY.ravel()[~inp], s=4, facecolor="none", edgecolor="#0072B2", lw=0.5)
    ax.scatter(GX.ravel()[inp], GY.ravel()[inp], s=9, color="#56B4E9", edgecolor="white", lw=0.4, zorder=4)
    ax.add_patch(Rectangle((W - 140, 1), 120, 28, fc="white", ec="none", alpha=0.9, zorder=5))
    ax.add_patch(Rectangle((W - 130, 19), 100, 6, fc=INK, ec=INK, lw=0.6, zorder=6))
    ax.text(W - 80, 4, "100 µm", color=INK, fontsize=8, ha="center", va="bottom", zorder=6)
    ax.set_xlim(0, W)
    ax.set_ylim(0, Hh)
    ax.axis("off")
    PL = total / 2.5
    Lbar = 1000 / PL
    G = -6.6439 * np.log10(Lbar / 1000) - 3.288
    fig.text(0.005, 0.135, f"5 test lines, $L_T$ = 2.5 mm:  N = {total} boundary intersections (ticks)  →  "
             f"$P_L$ = {PL:.0f} mm$^{{-1}}$,  $\\bar L$ = {Lbar:.0f} µm,  $S_V$ = 2$P_L$ = {2 * PL / 1000:.2f} µm$^{{-1}}$,"
             f"  G = {G:.1f}", fontsize=7.8, va="top")
    fig.text(0.005, 0.07, f"400-point grid: {int(inp.sum())} points in pearlite (filled)  →  "
             f"$P_P$ = {int(inp.sum())}/400 = {inp.mean():.2f} ± 0.02 = $V_V$   "
             f"(area fraction of this field {area_frac:.2f})", fontsize=7.8, va="top")
    # side panel: sphere sections
    axs = fig.add_axes([0.72, 0.20, 0.27, 0.77])
    axs.set_aspect("equal")
    axs.axis("off")
    axs.add_patch(Circle((0, 0), 1.0, fc="#DCE6F0", ec=INK, lw=1.0))
    hs = [0.0, 0.45, 0.75, 0.93]
    for k, hh in enumerate(hs):
        w = np.sqrt(1 - hh ** 2)
        axs.plot([-1.35, 1.35], [hh, hh], color=COLORS[1], lw=0.9, ls="--")
        axs.plot([-w, w], [hh, hh], color=COLORS[1], lw=2.0)
        axs.add_patch(Circle((2.4, 1.15 - 0.62 * k), w * 0.28, fc="#DCE6F0", ec=COLORS[1], lw=1.0))
    axs.text(2.4, 1.6, "sections", fontsize=7.5, ha="center", va="bottom")
    axs.annotate("", xy=(-1.0, -1.25), xytext=(1.0, -1.25),
                 arrowprops=dict(arrowstyle="<->", color=INK, lw=0.8, shrinkA=0, shrinkB=0, mutation_scale=7))
    axs.text(0, -1.33, "true diameter D", fontsize=7.5, ha="center", va="top")
    axs.text(-1.3, -1.85, "random planes cut most\nspheres below their\nequator, so sections\nlook smaller:\n"
             "mean section dia. = πD/4\nmean intercept " + r"$\bar L$ = 2D/3", fontsize=7.5, va="top")
    axs.set_xlim(-1.4, 3.0)
    axs.set_ylim(-4.0, 1.9)
    save(fig, "05", "fig-5-6-stereology-grid")


if __name__ == "__main__":
    point_defects()
    vacancy_arrhenius()
    dislocations_burgers()
    gb_energy_misorientation()
    phase_boundaries()
    stereology_grid()
