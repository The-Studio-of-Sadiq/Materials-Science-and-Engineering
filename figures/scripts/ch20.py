"""Figures for Chapter 20 — Polymer Physics and Morphology.

Run from the repository root:  python figures/scripts/ch20.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.patches import Circle, Polygon, Rectangle, FancyArrowPatch
from matplotlib.colors import ListedColormap

from figstyle import new_fig, schematic, save, COLORS, INK


# ---------------------------------------------------------------- helpers
def _scalebar(ax, x, y, length, label, fontsize=8, lw=2.0, color=INK):
    ax.plot([x, x + length], [y, y], color=color, lw=lw, solid_capstyle="butt")
    ax.text(x + length / 2, y + 0.02 * (ax.get_ylim()[1] - ax.get_ylim()[0]), label,
            ha="center", va="bottom", fontsize=fontsize, color=color)


def _nerf_chain(n, l=0.154, theta=np.deg2rad(109.5), dihedrals=None):
    """Cartesian positions of a chain from bond length, bond angle and dihedrals (NeRF)."""
    pos = np.zeros((n + 1, 3))
    pos[1] = [l, 0, 0]
    pos[2] = pos[1] + l * np.array([-np.cos(theta), np.sin(theta), 0])
    for i in range(3, n + 1):
        a, b, c = pos[i - 3], pos[i - 2], pos[i - 1]
        bc = (c - b) / np.linalg.norm(c - b)
        nn = np.cross(b - a, bc)
        nn /= np.linalg.norm(nn)
        m = np.column_stack([bc, np.cross(nn, bc), nn])
        phi = dihedrals[i]
        d2 = np.array([-l * np.cos(theta), l * np.sin(theta) * np.cos(phi), l * np.sin(theta) * np.sin(phi)])
        pos[i] = c + m @ d2
    return pos


# ---------------------------------------------------------------- 20.1
def random_walk_chain():
    b, NK = 1.26, 710
    best = None
    for seed in range(400):
        rng = np.random.default_rng(seed)
        v = rng.normal(size=(NK, 3))
        v /= np.linalg.norm(v, axis=1)[:, None]
        r = np.vstack([[0, 0, 0], np.cumsum(v * b, axis=0)])
        R3 = np.linalg.norm(r[-1])
        R2 = np.linalg.norm(r[-1, :2])
        Rg = np.sqrt(((r - r.mean(0)) ** 2).sum(1).mean())
        score = abs(R3 - 34) + abs(Rg - 14) + abs(R2 - 31)
        if best is None or score < best[0]:
            best = (score, r, R3, Rg)
    _, r, R3, Rg = best
    r = r - r.mean(0)
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(6.8, 3.7), gridspec_kw=dict(width_ratios=[1.15, 1]))
    seg = np.stack([r[:-1, :2], r[1:, :2]], axis=1)
    lc = LineCollection(seg, cmap="coolwarm", lw=1.0)
    lc.set_array(np.linspace(0, 1, len(seg)))
    ax.add_collection(lc)
    ax.plot(*r[0, :2], "o", color="#3B4CC0", ms=5)
    ax.plot(*r[-1, :2], "o", color="#B40426", ms=5)
    ax.annotate("", xy=r[-1, :2], xytext=r[0, :2],
                arrowprops=dict(arrowstyle="-|>", lw=1.6, color=INK, mutation_scale=12))
    mid = (r[0, :2] + r[-1, :2]) / 2
    ax.text(mid[0] + 1.5, mid[1] - 1.0, "$\\mathbf{R}$\n$\\sqrt{\\langle R^2\\rangle}\\approx 34$ nm",
            fontsize=8.5, ha="left", va="top", bbox=dict(fc="white", ec="none", alpha=0.8, pad=1))
    th = np.linspace(0, 2 * np.pi, 200)
    ax.plot(Rg * np.cos(th), Rg * np.sin(th), "--", color=INK, lw=1.0)
    ax.plot(0, 0, "+", color=INK, ms=8, mew=1.5)
    ax.text(Rg * 0.72, Rg * 0.72, "$R_g \\approx 14$ nm", fontsize=8.5, ha="left", va="bottom")
    lim = 30
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal")
    ax.axis("off")
    _scalebar(ax, -28, -28, 10, "10 nm")
    ax.text(-lim, lim, "PE, $M$ = 100 kg/mol: 7130 C–C bonds\n= 710 Kuhn segments, $b$ = 1.26 nm\ncontour length 897 nm",
            fontsize=7.8, va="top")
    ax.text(r[0, 0] - 1.5, r[0, 1], "start", color="#3B4CC0", fontsize=7.5, ha="right", va="center",
            bbox=dict(fc="white", ec="none", alpha=0.8, pad=0.5))
    ax.text(r[-1, 0] + 1.5, r[-1, 1], "end", color="#B40426", fontsize=7.5, ha="left", va="center",
            bbox=dict(fc="white", ec="none", alpha=0.8, pad=0.5))
    ax.set_title("(a) random-walk coil (2D projection)", fontsize=9.5)

    # right panel: real backbone with trans/gauche states, overlaid Kuhn segments
    n = 40
    dih = np.full(n + 1, np.pi)
    gauche = {12: np.deg2rad(60), 27: np.deg2rad(-60)}
    for k, v in gauche.items():
        dih[k] = v
    p = _nerf_chain(n, dihedrals=dih)
    rot = -np.deg2rad(35.25)
    Rm = np.array([[np.cos(rot), -np.sin(rot)], [np.sin(rot), np.cos(rot)]])
    p2 = p[:, :2] @ Rm.T
    ax2.plot(p2[:, 0], p2[:, 1], color="#555555", lw=1.2, zorder=2)
    ax2.plot(p2[:, 0], p2[:, 1], "o", color=INK, ms=2.5, zorder=3)
    for k in gauche:
        ax2.plot(p2[k - 1:k + 1, 0], p2[k - 1:k + 1, 1], color=COLORS[1], lw=2.6, zorder=2)
    kpts = p2[::10]
    for i in range(len(kpts) - 1):
        ax2.annotate("", xy=kpts[i + 1], xytext=kpts[i],
                     arrowprops=dict(arrowstyle="-|>", lw=1.4, color=COLORS[0], alpha=0.85,
                                     shrinkA=0, shrinkB=0, mutation_scale=10))
    ax2.set_aspect("equal")
    ax2.axis("off")
    xmin, xmax = p2[:, 0].min(), p2[:, 0].max()
    ymin, ymax = p2[:, 1].min(), p2[:, 1].max()
    padx = 0.35
    ax2.set_xlim(xmin - padx, xmax + padx)
    ax2.set_ylim(ymin - 0.9, ymax + 0.9)
    # labels
    k = 5
    ax2.annotate("trans (t)", xy=p2[k], xytext=(p2[k, 0] - 0.1, p2[k, 1] + 0.6), fontsize=8,
                 arrowprops=dict(arrowstyle="-", lw=0.6, color=INK), ha="center")
    for k, lab in zip(gauche, ["gauche$^+$", "gauche$^-$"]):
        q = (p2[k - 1] + p2[k]) / 2
        ax2.annotate(lab, xy=q, xytext=(q[0] + 0.5, q[1] - 0.6), fontsize=8, color=COLORS[1],
                     arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[1]))
    q = (kpts[0] + kpts[1]) / 2
    ax2.text(q[0], q[1] - 0.35, "Kuhn segment $b$", color=COLORS[0], fontsize=8, ha="center", va="top")
    ax2.text(xmin - padx, ymin - 0.85, "C–C bond 0.154 nm\nvalence angle 109.5°", fontsize=7.8, va="bottom")
    _scalebar(ax2, xmax - 0.5, ymin - 0.75, 0.5, "0.5 nm")
    ax2.set_title("(b) real backbone and Kuhn segments", fontsize=9.5)
    fig.tight_layout()
    save(fig, "20", "fig-20-1-random-walk-chain")


# ---------------------------------------------------------------- 20.2
def rubber_stress_strain():
    G = 920 * 8.314 * 298 / 5.0 / 1e6           # 0.456 MPa
    fig, ax = new_fig(6.4, 4.0)
    lam = np.linspace(1, 7, 400)
    sg = G * (lam - lam ** -2)
    ax.plot(lam, sg, color=COLORS[0], label="Gaussian affine theory, $\\sigma = G(\\lambda-\\lambda^{-2})$, $G$ = 0.46 MPa")

    def expt(l):
        red = 0.25 * (1 - np.exp(-((l - 1) / 1.2) ** 2))
        up = 0.5 * (np.exp(1.5 * (l - 5)) - np.exp(-6))
        return G * (l - l ** -2) * (1 - red) + up

    le = np.r_[np.linspace(1.1, 4.5, 14), np.linspace(4.8, 6.5, 7)]
    ax.plot(le, expt(le), "o", mfc="white", mec=COLORS[1], mew=1.3, ms=5,
            label="natural rubber, representative experiment (Treloar type)")
    l2 = np.linspace(1, 6.6, 300)
    ax.plot(l2, expt(l2), color=COLORS[1], lw=0.8, alpha=0.6)
    ax.plot([2], [G * 1.75], "s", color=COLORS[0], ms=5)
    ax.annotate("0.80 MPa at $\\lambda$ = 2", xy=(2, G * 1.75), xytext=(2.15, 0.15), fontsize=8.5,
                arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK))
    ax.annotate("crosslink fluctuations\n(10–25 % below theory)", xy=(3.8, expt(3.8)), xytext=(4.25, 0.45),
                fontsize=8.5, arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK))
    ax.annotate("finite extensibility\n+ strain crystallization", xy=(6.0, expt(6.0)), xytext=(4.6, 5.5),
                fontsize=8.5, ha="center", arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK))
    ax.set_xlim(1, 7)
    ax.set_ylim(0, 8)
    ax.set_xlabel("stretch ratio $\\lambda$")
    ax.set_ylabel("nominal stress $\\sigma$ (MPa)")
    ax.legend(loc="upper left", fontsize=8)
    # inset: force at fixed lambda vs absolute temperature
    ins = ax.inset_axes([0.11, 0.37, 0.29, 0.29])
    T = np.linspace(0, 400, 50)
    sT = G * (T / 298) * (3 - 1 / 9)
    ins.plot(T, sT, "--", color=INK, lw=0.9)
    Tm = np.linspace(273.15, 373.15, 20)
    ins.plot(Tm, G * (Tm / 298) * (3 - 1 / 9), color=COLORS[0], lw=2.2)
    ins.set_xlim(0, 400)
    ins.set_ylim(0, 2.0)
    ins.set_xticks([0, 100, 200, 300, 400])
    ins.tick_params(labelsize=7)
    ins.set_xlabel("$T$ (K)", fontsize=7.5, labelpad=1)
    ins.set_ylabel("$\\sigma$ at $\\lambda$=3 (MPa)", fontsize=7.5, labelpad=1)
    ins.text(395, 0.08, "solid: 0–100 °C\ndashed: extrapolation\nthrough origin (0 K)", fontsize=6.5,
             ha="right", va="bottom")
    ins.patch.set_alpha(0.9)
    save(fig, "20", "fig-20-2-rubber-stress-strain")


# ---------------------------------------------------------------- 20.3
# Approximate mean-field (SCFT, Matsen–Bates) boundaries for the left half f <= 0.5,
# given as f(chiN).  All boundaries meet at the mean-field critical point (0.5, 10.495).
_ODT = ([10.495, 10.9, 12.0, 14.0, 17.3, 22.5, 30.5, 43.5, 55.0],
        [0.500, 0.450, 0.400, 0.350, 0.300, 0.250, 0.200, 0.150, 0.120])
_SC = ([10.495, 12.3, 15.5, 20.0, 28.0, 38.0, 55.0],
       [0.500, 0.400, 0.330, 0.270, 0.220, 0.195, 0.175])
_CG = ([10.495, 11.6, 13.5, 17.0, 22.0, 30.0, 40.0, 55.0],
       [0.500, 0.452, 0.415, 0.375, 0.350, 0.335, 0.325, 0.320])
_GL = ([10.495, 11.6, 13.5, 17.0, 22.0, 30.0, 40.0, 55.0],
       [0.500, 0.452, 0.425, 0.395, 0.375, 0.360, 0.348, 0.338])


def _fb(chiN, curve):
    x, y = curve
    return np.interp(chiN, x, y, left=0.5, right=y[-1])


def _phase(f, chiN):
    ff = np.minimum(f, 1 - f)
    out = np.zeros_like(f, dtype=int)            # 0 disordered
    odt = _fb(chiN, _ODT)
    sc, cg, gl = _fb(chiN, _SC), _fb(chiN, _CG), _fb(chiN, _GL)
    ordered = (ff >= odt) & (chiN >= 10.495)
    out[ordered & (ff < sc)] = 1                 # spheres
    out[ordered & (ff >= sc) & (ff < cg)] = 2    # cylinders
    out[ordered & (ff >= cg) & (ff < gl)] = 3    # gyroid
    out[ordered & (ff >= gl)] = 4                # lamellae
    return out


def _morph_icon(ax, kind, x0, y0, s):
    """Small pseudo-3D icon of an ordered morphology in a box of size s at (x0, y0)."""
    dark, light = "#1F4E79", "#CFE0EE"
    d = 0.28 * s
    front = [(x0, y0), (x0 + s, y0), (x0 + s, y0 + s), (x0, y0 + s)]
    top = [(x0, y0 + s), (x0 + s, y0 + s), (x0 + s + d, y0 + s + d), (x0 + d, y0 + s + d)]
    side = [(x0 + s, y0), (x0 + s + d, y0 + d), (x0 + s + d, y0 + s + d), (x0 + s, y0 + s)]
    for poly, c in ((front, light), (top, "#E3EDF6"), (side, "#B9CFE3")):
        ax.add_patch(Polygon(poly, closed=True, fc=c, ec=INK, lw=0.6))
    if kind == "L":
        for i in range(3):
            xa = x0 + (0.12 + 0.3 * i) * s
            w = 0.14 * s
            ax.add_patch(Polygon([(xa, y0), (xa + w, y0), (xa + w, y0 + s), (xa, y0 + s)], fc=dark, ec="none"))
            ax.add_patch(Polygon([(xa, y0 + s), (xa + w, y0 + s), (xa + w + d, y0 + s + d), (xa + d, y0 + s + d)],
                                 fc="#3A6A96", ec="none"))
    elif kind == "C":
        for i in range(3):
            for j in range(3):
                cx = x0 + (0.2 + 0.3 * i + (0.15 if j % 2 else 0)) * s
                cy = y0 + (0.2 + 0.3 * j) * s
                if cx < x0 + 0.92 * s:
                    ax.add_patch(Circle((cx, cy), 0.08 * s, fc=dark, ec="none"))
        for i in range(3):
            cx = x0 + (0.2 + 0.3 * i) * s
            ax.plot([cx, cx + d], [y0 + s, y0 + s + d], color=dark, lw=2.2, solid_capstyle="round")
    elif kind == "S":
        for (u, v) in [(0.22, 0.22), (0.78, 0.22), (0.22, 0.78), (0.78, 0.78), (0.5, 0.5)]:
            ax.add_patch(Circle((x0 + u * s, y0 + v * s), 0.1 * s, fc=dark, ec="none"))
    elif kind == "G":
        pts = [(0.2, 0.25), (0.5, 0.45), (0.8, 0.25), (0.5, 0.8), (0.15, 0.7), (0.85, 0.7)]
        P = [(x0 + u * s, y0 + v * s) for u, v in pts]
        for a, bb in [(0, 1), (1, 2), (1, 3), (3, 4), (3, 5), (0, 4), (2, 5)]:
            ax.plot([P[a][0], P[bb][0]], [P[a][1], P[bb][1]], color=dark, lw=2.4, solid_capstyle="round")


def block_copolymer_phase_diagram():
    fig = plt.figure(figsize=(6.8, 4.4))
    ax = fig.add_axes([0.09, 0.12, 0.66, 0.82])
    f = np.linspace(0, 1, 801)
    cn = np.linspace(0, 50, 501)
    F, CN = np.meshgrid(f, cn)
    ph = _phase(F, CN)
    cmap = ListedColormap(["#FFFFFF", "#DCEAF5", "#FBE3CF", "#E3D3EC", "#D8EFD9"])
    ax.imshow(ph, origin="lower", extent=(0, 1, 0, 50), aspect="auto", cmap=cmap, vmin=-0.5, vmax=4.5,
              interpolation="nearest")
    ax.contour(F, CN, ph, levels=[0.5, 1.5, 2.5, 3.5], colors=INK, linewidths=0.9)
    labels = [("disordered", 0.3, 5.0, 10), ("S\n(bcc)", 0.115, 47, 8.5), ("C\n(hex)", 0.275, 30, 9),
              ("L", 0.5, 30, 11), ("S\n(bcc)", 0.885, 47, 8.5), ("C\n(hex)", 0.725, 30, 9)]
    for t, x, y, fs in labels:
        ax.text(x, y, t, ha="center", va="center", fontsize=fs, weight="bold" if t == "L" else None)
    for x in (0.336, 0.664):
        ax.annotate("G", xy=(x, 40), xytext=(0.43 if x < 0.5 else 0.57, 45), fontsize=9,
                    ha="center", va="center", arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
    ax.plot(0.5, 10.495, "o", color=INK, ms=4)
    ax.annotate("$(\\chi N)_{ODT}$ = 10.5 at $f$ = 0.5", xy=(0.5, 10.5), xytext=(0.58, 2.5), fontsize=8.5,
                arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK))
    # application markers
    ax.annotate("", xy=(0.3, 44), xytext=(0.2, 44), arrowprops=dict(arrowstyle="|-|", lw=1.2, color=COLORS[1],
                                                                     mutation_scale=4))
    ax.text(0.03, 41.2, "SBS TPE: $f_{PS}$ ≈ 0.2–0.3\n→ PS spheres/cylinders", fontsize=7.8, color=COLORS[1],
            va="top", bbox=dict(fc="white", ec="none", alpha=0.85, pad=1))
    ax.plot(0.5, 30 - 6, "D", color=COLORS[0], ms=5)
    ax.annotate("PS-b-PMMA lithography,\n$f$ ≈ 0.5 → lamellae,\nperiod 25–40 nm", xy=(0.5, 24),
                xytext=(0.97, 10.5), fontsize=7.8, color=COLORS[0], ha="right", va="center",
                arrowprops=dict(arrowstyle="-|>", lw=0.8, color=COLORS[0]))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 50)
    ax.set_xlabel("volume fraction of block A, $f_A$")
    ax.set_ylabel("segregation strength $\\chi N$")
    # morphology icons
    axr = fig.add_axes([0.77, 0.08, 0.22, 0.88])
    axr.set_xlim(0, 1)
    axr.set_ylim(0, 4)
    axr.set_aspect("equal")
    axr.axis("off")
    names = [("S", "spheres (bcc)"), ("C", "cylinders (hex)"), ("G", "gyroid"), ("L", "lamellae")]
    for i, (k, nm) in enumerate(names):
        y0 = 3.12 - i * 1.0
        _morph_icon(axr, k, 0.18, y0, 0.48)
        axr.text(0.5, y0 - 0.1, nm, ha="center", va="top", fontsize=8)
    save(fig, "20", "fig-20-3-block-copolymer-phase-diagram")


# ---------------------------------------------------------------- 20.4
def _zigzag_c(x, y, z0, z1, ang, amp=0.043, step=0.1275):
    zs = np.arange(z0, z1 + 1e-9, step)
    off = np.array([amp if i % 2 == 0 else -amp for i in range(len(zs))])
    return x + off * np.cos(ang), y + off * np.sin(ang), zs


def semicrystalline_hierarchy():
    fig, axs2 = plt.subplots(2, 2, figsize=(6.8, 5.6))
    axs = axs2.ravel()
    for a in axs:
        a.set_aspect("equal")
        a.axis("off")

    # (1) orthorhombic PE unit cell, oblique projection
    ax = axs[0]
    a_, b_, c_ = 0.741, 0.494, 0.255
    ncell = 3

    def P(x, y, z):
        return x + 0.6 * y * np.cos(np.deg2rad(35)), z + 0.6 * y * np.sin(np.deg2rad(35))

    H = c_ * ncell
    corners = [(0, 0), (a_, 0), (a_, b_), (0, b_)]
    for zc in [0, H]:
        xs, ys = zip(*[P(x, y, zc) for x, y in corners + [corners[0]]])
        ax.plot(xs, ys, color="#888888", lw=0.8)
    for zc in [c_, 2 * c_]:
        xs, ys = zip(*[P(x, y, zc) for x, y in corners + [corners[0]]])
        ax.plot(xs, ys, color="#BBBBBB", lw=0.6, ls=":")
    for x, y in corners:
        xs, ys = zip(P(x, y, 0), P(x, y, H))
        ax.plot(xs, ys, color="#888888", lw=0.8)
    chains = [(0, 0, 0.73), (a_, 0, 0.73), (a_, b_, 0.73), (0, b_, 0.73), (a_ / 2, b_ / 2, -0.73)]
    for x, y, ang in chains:
        X, Y, Z = _zigzag_c(x, y, -0.04, H + 0.04, ang)
        pts = np.array([P(xx, yy, zz) for xx, yy, zz in zip(X, Y, Z)])
        col = COLORS[1] if (x, y) == (a_ / 2, b_ / 2) else INK
        ax.plot(pts[:, 0], pts[:, 1], color=col, lw=1.4)
        ax.plot(pts[:, 0], pts[:, 1], "o", color=col, ms=3)
    ax.annotate("", xy=P(a_, 0, -0.1), xytext=P(0, 0, -0.1),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, color=INK, mutation_scale=8))
    ax.text(*P(a_ / 2, 0, -0.16), "$a$ = 0.741 nm", ha="center", va="top", fontsize=8)
    ax.annotate("", xy=P(a_ + 0.08, b_, 0), xytext=P(a_ + 0.08, 0, 0),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, color=INK, mutation_scale=8))
    xb, yb = P(a_ + 0.1, b_ / 2, 0)
    ax.text(xb + 0.06, yb - 0.04, "$b$ = 0.494 nm", fontsize=8, ha="left", va="center")
    ax.annotate("", xy=(-0.1, c_), xytext=(-0.1, 0),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, color=INK, mutation_scale=7))
    ax.text(-0.16, c_ / 2, "$c$ = 0.255 nm\n(chain axis)", fontsize=8, ha="right", va="center")
    ax.text(-0.95, 1.5, "orthorhombic PE: 2 chains/cell,\nall-trans zig-zag along $c$\n(3 cells stacked along $c$)",
            fontsize=7.5, va="top")
    ax.set_xlim(-1.0, 1.75)
    ax.set_ylim(-0.6, 1.55)
    _scalebar(ax, 1.05, -0.5, 0.5, "0.5 nm", fontsize=7.5)
    ax.set_title("(1) unit cell  (~0.5 nm)", fontsize=9.5)

    # (2) chain-folded lamellae with amorphous layer
    ax = axs[1]
    L, Am, W = 17.0, 5.0, 22.0
    y1a, y1b = 0, L
    y2a, y2b = L + Am, 2 * L + Am
    for ya, yb in ((y1a, y1b), (y2a, y2b)):
        ax.add_patch(Rectangle((0, ya), W, yb - ya, fc="#DCEAF5", ec="none", zorder=0))
    ax.add_patch(Rectangle((0, y1b), W, Am, fc="#F2F2F2", ec="none", zorder=0))
    sp = 1.2
    xs = np.arange(0.8, W - 0.3, sp)
    th = np.linspace(0, np.pi, 20)
    for ya, yb in ((y1a, y1b), (y2a, y2b)):
        for x in xs:
            ax.plot([x, x], [ya, yb], color=INK, lw=0.7)
        for i in range(0, len(xs) - 1, 2):
            cx = (xs[i] + xs[i + 1]) / 2
            if not (ya == y1a and 3 <= i <= 8) and not (ya == y1a and 12 <= i <= 13):
                ax.plot(cx + sp / 2 * np.cos(th), yb + 0.6 * np.sin(th), color=INK, lw=0.7)
        for i in range(1, len(xs) - 1, 2):
            cx = (xs[i] + xs[i + 1]) / 2
            ax.plot(cx + sp / 2 * np.cos(th), ya - 0.6 * np.sin(th), color=INK, lw=0.7)
    t = np.linspace(0, 1, 80)
    # loose loop (non-adjacent re-entry) into the amorphous layer
    xl = xs[4] + (xs[9] - xs[4]) * t
    yl = y1b + 4.0 * np.sin(np.pi * t) + 0.5 * np.sin(5 * np.pi * t) * np.sin(np.pi * t)
    ax.plot(xl, yl, color=COLORS[2], lw=1.5)
    # tie molecule crossing to the next lamella
    xt = xs[13] + 1.4 * np.sin(np.pi * t) * np.sin(3 * np.pi * t)
    yt = y1b + (y2a - y1b) * t
    ax.plot(xt, yt, color=COLORS[1], lw=2.0)
    # cilium on top face
    xc = xs[15] + np.r_[0, 0.5, -0.1, 0.8, 0.5]
    yc = y2b + np.r_[0, 1.0, 2.0, 2.8, 3.8]
    ax.plot(xc, yc, color=COLORS[3], lw=1.5)
    # labels on the right with leaders
    xr = W + 2.0
    ax.annotate("cilium", xy=(xc[-2], yc[-2]), xytext=(xr, y2b + 3.5), fontsize=7.5, color=COLORS[3],
                va="center", arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[3]))
    ax.annotate("adjacent re-entry\nfold", xy=((xs[18] + xs[19]) / 2 if len(xs) > 19 else xs[-1], y2b + 0.5),
                xytext=(xr, y2b - 2.5), fontsize=7.5, va="center",
                arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
    ax.annotate("tie molecule", xy=(xt[45], yt[45]), xytext=(xr, y1b + Am / 2 + 1.5), fontsize=7.5,
                color=COLORS[1], va="center", arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[1]))
    ax.annotate("loose loop", xy=(xl[62], yl[62]), xytext=(xr, y1b - 2.0), fontsize=7.5,
                color=COLORS[2], va="center", arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[2]))
    ax.text(xr, y1a + L / 2 - 3, "crystalline\nlamella", fontsize=7.5, va="center", color="#1F4E79")
    # dimensions on the left
    xd = -1.0
    ax.annotate("", xy=(xd, y2b), xytext=(xd, y2a), arrowprops=dict(arrowstyle="<|-|>", lw=0.8, mutation_scale=7))
    ax.text(xd - 0.5, (y2a + y2b) / 2, "$l$ ≈\n10–20 nm", fontsize=7.5, ha="right", va="center")
    ax.annotate("", xy=(xd, y2a), xytext=(xd, y1b), arrowprops=dict(arrowstyle="<|-|>", lw=0.8, mutation_scale=7))
    ax.text(xd - 0.5, (y1b + y2a) / 2, "amorphous\n≈ 5 nm", fontsize=7.5, ha="right", va="center")
    xd3 = -16.5
    ax.annotate("", xy=(xd3, y2b), xytext=(xd3, y1b), arrowprops=dict(arrowstyle="<|-|>", lw=0.8, mutation_scale=7))
    ax.text(xd3 - 0.6, (y1b + y2b) / 2, "long period ≈ 20–30 nm", fontsize=7.5, ha="right", va="center",
            rotation=90)
    ax.set_xlim(-23, W + 13)
    ax.set_ylim(-5, 2 * L + Am + 6)
    _scalebar(ax, -12, -3.5, 10, "10 nm", fontsize=7.5)
    ax.set_title("(2) chain-folded lamellae  (~10 nm)", fontsize=9.5)

    # (3) radiating, branching lamellar fibrils
    ax = axs[2]
    rng = np.random.default_rng(5)
    ax.add_patch(Circle((0, 0), 5.0, fc="#EFEFEF", ec="none", zorder=0))

    def grow(x, y, ang, length, depth):
        n = 12
        pts = [(x, y)]
        for _ in range(n):
            ang += rng.normal(0, 0.05)
            x += length / n * np.cos(ang)
            y += length / n * np.sin(ang)
            pts.append((x, y))
        pts = np.array(pts)
        ax.plot(pts[:, 0], pts[:, 1], color="#1F4E79", lw=2.2 - 0.5 * depth, solid_capstyle="round")
        if depth < 2:
            k = rng.integers(4, 9)
            sgn = rng.choice([-1, 1])
            grow(pts[k, 0], pts[k, 1], ang + sgn * rng.uniform(0.25, 0.45), length * (1 - k / n) * 0.95,
                 depth + 1)

    for ang in np.linspace(0, 2 * np.pi, 15)[:-1]:
        grow(0.25 * np.cos(ang), 0.25 * np.sin(ang), ang + rng.normal(0, 0.05), 4.6, 0)
    ax.annotate("lamellar fibril\n(edge-on lamella stack)", xy=(3.2, 2.6), xytext=(5.6, 4.6), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
    ax.annotate("branch point", xy=(-2.3, -1.2), xytext=(-7.5, -4.2), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
    ax.annotate("amorphous polymer\nbetween fibrils", xy=(-2.9, 2.6), xytext=(-8.8, 4.6), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
    ax.text(0.0, -5.3, "nucleus at centre; growth radially outward", ha="center", va="top", fontsize=7.5)
    ax.set_xlim(-9.5, 9.5)
    ax.set_ylim(-7.0, 5.8)
    _scalebar(ax, 5.5, -4.6, 2.0, "1 µm", fontsize=7.5)
    ax.set_title("(3) branching lamellar fibrils  (~1 µm)", fontsize=9.5)

    # (4) impinging spherulites between crossed polarizers
    ax = axs[3]
    Wd, Hd = 150.0, 110.0
    seeds = np.array([[28, 28], [82, 18], [136, 40], [70, 70], [20, 88], [118, 96], [-12, 45], [160, 100]])
    nx, ny = 600, 440
    X, Y = np.meshgrid(np.linspace(0, Wd, nx), np.linspace(0, Hd, ny))
    d = np.stack([(X - sx) ** 2 + (Y - sy) ** 2 for sx, sy in seeds])
    idx = d.argmin(0)
    phi = np.arctan2(Y - seeds[idx, 1], X - seeds[idx, 0])
    rr = np.sqrt(d.min(0))
    I = np.sin(2 * phi) ** 2 * (0.8 + 0.2 * np.cos(rr / 2.0) ** 2) * (1 - np.exp(-rr / 3))
    ax.imshow(I, origin="lower", extent=(0, Wd, 0, Hd), cmap="gray", vmin=0, vmax=1.05)
    ax.contour(X, Y, idx, levels=np.arange(len(seeds)) + 0.5, colors="#E8C547", linewidths=0.8)
    ax.add_patch(Rectangle((0, 0), Wd, Hd, fill=False, ec=INK, lw=0.8))
    m = (seeds[0] + seeds[3]) / 2
    ax.annotate("weak plane: impurities,\nlow-M chains", xy=(m[0], m[1]), xytext=(Wd / 2, -10),
                fontsize=7.5, ha="center", va="top",
                arrowprops=dict(arrowstyle="-|>", lw=0.9, color=COLORS[1]))
    ax.text(Wd + 5, Hd, "polarizer ↔\nanalyser ↕", fontsize=7, va="top")
    ax.text(Wd + 5, Hd - 30, "dark\nMaltese\ncross\nalong P, A", fontsize=7, va="top")
    _scalebar(ax, Wd + 5, 8, 50, "50 µm", fontsize=7.5)
    ax.set_xlim(-2, Wd + 58)
    ax.set_ylim(-36, Hd + 4)
    ax.set_title("(4) spherulites, crossed polars  (~50 µm)", fontsize=9.5)

    fig.tight_layout(h_pad=0.6, w_pad=0.4)
    for i, j in ((0, 1), (2, 3)):
        b0, b1 = axs[i].get_position(), axs[j].get_position()
        fig.text((b0.x1 + b1.x0) / 2, (b0.y0 + b0.y1) / 2, "›", fontsize=20, ha="center", va="center",
                 color="#888888")
    save(fig, "20", "fig-20-4-semicrystalline-hierarchy")


# ---------------------------------------------------------------- 20.5
def glass_transition():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(6.8, 3.6), gridspec_kw=dict(width_ratios=[1.1, 1]))
    am, ag = 5.5e-4, 2.0e-4
    V0, Ts, Tf = 0.956, 100.0, 106.0
    T = np.linspace(20, 180, 200)
    Vm = lambda t: V0 + am * (t - Ts)
    Tl = np.linspace(Ts, 180, 50)
    ax.plot(Tl, Vm(Tl), color=INK, label="melt (equilibrium)")
    Te = np.linspace(20, Ts, 50)
    ax.plot(Te, Vm(Te), ":", color="#777777", lw=1.2, label="extrapolated liquid")
    Tg_s = np.linspace(20, Ts, 50)
    ax.plot(Tg_s, V0 + ag * (Tg_s - Ts), color=COLORS[0], label="glass, 1 K/min ($T_g$ = 100 °C)")
    Vf0 = Vm(Tf)
    Tg_f = np.linspace(20, Tf, 50)
    ax.plot(Tg_f, Vf0 + ag * (Tg_f - Tf), color=COLORS[1], label="glass, 100 K/min ($T_g$ = 106 °C)")
    ax.fill_between(Te, Vm(Te), V0 + ag * (Te - Ts), color=COLORS[0], alpha=0.12)
    ax.annotate("free volume frozen in", xy=(88, 0.951), xytext=(112, 0.945), fontsize=7.5, color=COLORS[0],
                va="center", arrowprops=dict(arrowstyle="-|>", lw=0.8, color=COLORS[0]))
    for tg, c in ((Ts, COLORS[0]), (Tf, COLORS[1])):
        ax.plot([tg, tg], [0.938, Vm(tg)], "--", color=c, lw=0.7)
    v80 = Vf0 + ag * (80 - Tf)
    ax.annotate("", xy=(80, v80 - 0.0045), xytext=(80, v80 + 0.0001),
                arrowprops=dict(arrowstyle="-|>", lw=1.2, color=COLORS[3], mutation_scale=9))
    ax.text(66, 0.9575, "physical aging", fontsize=7.5, color=COLORS[3], ha="center", va="bottom")
    ax.set_xlim(20, 180)
    ax.set_ylim(0.938, 1.002)
    ax.set_xlabel("temperature (°C)")
    ax.set_ylabel("specific volume (cm$^3$/g)")
    ax.legend(loc="upper left", fontsize=7.3)
    ax.set_title("(a) polystyrene-like glass", fontsize=9.5)

    C1, C2 = 17.44, 51.6
    dT = np.linspace(0, 100, 300)
    wlf = -C1 * dT / (C2 + dT)
    ax2.plot(dT, wlf, color=COLORS[0], label="WLF, $C_1$ = 17.44, $C_2$ = 51.6 K")
    Tg = 373.15
    target = -C1 * 100 / (C2 + 100)
    Ea = -target * 2.303 * 8.314 / (1 / Tg - 1 / (Tg + 100))
    arr = -Ea / (2.303 * 8.314) * (1 / Tg - 1 / (Tg + dT))
    ax2.plot(dT, arr, "--", color=COLORS[1],
             label=f"Arrhenius, $E_a$ ≈ {Ea / 1e3:.0f} kJ/mol\n(matched at $T_g$ + 100 K)")
    for x, y in ((10, -2.83), (20, -4.87), (30, -6.41)):
        ax2.plot(x, y, "o", color=COLORS[0], ms=5)
        ax2.text(x - 0.8, y - 0.3, f"{y:.2f}".replace("-", "−"), fontsize=8, ha="right", va="top")
    ax2.set_xlim(0, 100)
    ax2.set_ylim(-12.5, 0.5)
    ax2.set_xlabel("$T - T_g$ (K)")
    ax2.set_ylabel("$\\log_{10} a_T$")
    ax2.legend(loc="upper right", fontsize=7.5)
    ax2.set_title("(b) WLF shift factor above $T_g$", fontsize=9.5)
    fig.tight_layout()
    save(fig, "20", "fig-20-5-glass-transition")


# ---------------------------------------------------------------- 20.6
def _rods(ax, centres, angles, length, color=INK, lw=1.0):
    for (x, y), a in zip(centres, angles):
        dx, dy = 0.5 * length * np.cos(a), 0.5 * length * np.sin(a)
        ax.plot([x - dx, x + dx], [y - dy, y + dy], color=color, lw=lw, solid_capstyle="round")


def lcp_order():
    fig, axs = plt.subplots(1, 4, figsize=(6.8, 2.9), gridspec_kw=dict(width_ratios=[1, 1, 1, 1.05]))
    rng = np.random.default_rng(11)
    Lr = 1.2
    for a in axs[:3]:
        a.set_xlim(0, 4)
        a.set_ylim(-0.9, 4)
        a.set_aspect("equal")
        a.axis("off")
        a.add_patch(Rectangle((0, 0), 4, 4, fill=False, ec="#999999", lw=0.8))

    # (1) isotropic
    ax = axs[0]
    n = 34
    c = rng.uniform(0.6, 3.4, size=(n, 2))
    _rods(ax, c, rng.uniform(0, np.pi, n), Lr)
    ax.text(2, -0.15, "isotropic: $\\phi < \\phi^*$ ≈ 0.08\n$S$ = 0", ha="center", va="top", fontsize=8)
    ax.set_title("(1) isotropic solution", fontsize=9)

    # (2) nematic polydomain
    ax = axs[1]
    seeds = np.array([[1.0, 3.0], [3.0, 3.1], [1.2, 0.9], [3.1, 1.0]])
    dirs = np.deg2rad([20, 110, 150, 60])
    cols = [COLORS[0], COLORS[1], COLORS[2], COLORS[3]]
    gx, gy = np.meshgrid(np.linspace(0.3, 3.7, 9), np.linspace(0.3, 3.7, 9))
    pts = np.c_[gx.ravel(), gy.ravel()] + rng.normal(0, 0.08, size=(81, 2))
    dom = np.argmin(((pts[:, None, :] - seeds[None]) ** 2).sum(-1), axis=1)
    for k in range(4):
        sel = dom == k
        ang = dirs[k] + rng.normal(0, np.deg2rad(18), sel.sum())
        _rods(ax, pts[sel], ang, 0.55, color=cols[k], lw=1.2)
    for k in range(4):
        x, y = seeds[k]
        ax.annotate("", xy=(x + 0.45 * np.cos(dirs[k]), y + 0.45 * np.sin(dirs[k])),
                    xytext=(x - 0.45 * np.cos(dirs[k]), y - 0.45 * np.sin(dirs[k])),
                    arrowprops=dict(arrowstyle="-|>", lw=1.6, color=INK, mutation_scale=9))
    ax.text(seeds[0, 0] + 0.35, seeds[0, 1] + 0.42, "$\\mathbf{n}$", fontsize=10)
    ax.plot([2.1], [2.05], "o", ms=6, mfc="white", mec=INK, mew=1.2)
    ax.text(2, -0.15, "nematic domains, $S$ ≈ 0.7\n○ = disclination", ha="center", va="top", fontsize=8)
    ax.set_title("(2) nematic dope", fontsize=9)

    # (3) aligned fibre
    ax = axs[2]
    ax.add_patch(Rectangle((1.0, 0), 2.0, 4, fc="#F2F2F2", ec=INK, lw=0.9))
    m = 30
    cx = rng.uniform(1.2, 2.8, m)
    cy = rng.uniform(0.6, 3.4, m)
    _rods(ax, np.c_[cx, cy], np.pi / 2 + rng.normal(0, np.deg2rad(8), m), Lr, lw=1.1)
    ax.annotate("", xy=(3.5, 3.6), xytext=(3.5, 0.4), arrowprops=dict(arrowstyle="-|>", lw=1.2, color=INK))
    ax.text(3.6, 2.0, "fibre\naxis", fontsize=7.5, va="center")
    ax.text(2, -0.15, "spun fibre: $S$ > 0.9\nPPTA fibre, $E$ ≈ 70–130 GPa", ha="center", va="top", fontsize=8)
    ax.set_title("(3) after spinning", fontsize=9)

    # (4) order parameter vs volume fraction
    ax = axs[3]
    phi = np.linspace(0, 0.3, 300)
    ps = 0.08
    S = np.where(phi < ps, 0.0, 0.8 + 0.6 * (phi - ps))
    ax.plot(phi[phi < ps], S[phi < ps], color=COLORS[0])
    ax.plot(phi[phi >= ps], np.minimum(S[phi >= ps], 0.95), color=COLORS[0])
    ax.plot([ps, ps], [0, 0.8], ":", color=COLORS[0])
    ax.set_xlim(0, 0.3)
    ax.set_ylim(0, 1.0)
    ax.set_xlabel("rod volume fraction $\\phi$", fontsize=8.5)
    ax.set_ylabel("order parameter $S$", fontsize=8.5)
    ax.tick_params(labelsize=7.5)
    ax.text(ps + 0.01, 0.4, "$\\phi^*$ ≈ 8/$x$\n(first-order\njump)", fontsize=7.5)
    ax.set_title("(4) $S$ vs $\\phi$, $x$ ≈ 100", fontsize=9)
    ax.set_aspect(0.3 / 1.0 * 1.25)
    fig.tight_layout(w_pad=0.6)
    save(fig, "20", "fig-20-6-lcp-order")


if __name__ == "__main__":
    random_walk_chain()
    rubber_stress_strain()
    block_copolymer_phase_diagram()
    semicrystalline_hierarchy()
    glass_transition()
    lcp_order()
