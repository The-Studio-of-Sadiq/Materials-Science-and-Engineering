"""Figures for Chapter 22 — Composite Micromechanics and Lamina Behaviour.

Run from the repository root:  python figures/scripts/ch22.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, FancyArrowPatch, Rectangle
from matplotlib.path import Path
import matplotlib.transforms as mtransforms

from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK

# T300/epoxy and E-glass/epoxy ply data (Table 22.3)
T300 = dict(E1=181.0, E2=10.3, G12=7.17, n12=0.28, a1=0.02, a2=22.5)
GLASS = dict(E1=38.6, E2=8.27, G12=4.14, n12=0.26)

FIBRE = "#3A3A3A"
MATRIX = "#F3E9C6"
MATRIX_TOP = "#F8F1D9"
MATRIX_SIDE = "#E6D9AE"


# ---------------------------------------------------------------- helpers
def _P(x, y, z, k=0.55, ang=35.0):
    """Oblique projection: x to the right, y up, z into the page (drawn up-right)."""
    a = np.radians(ang)
    return x + k * z * np.cos(a), y + k * z * np.sin(a)


def _poly(ax, pts, **kw):
    p = Polygon(np.array(pts), closed=True, **kw)
    ax.add_patch(p)
    return p


def _block(ax, x0, y0, z0, w, h, d, fc=(MATRIX, MATRIX_TOP, MATRIX_SIDE), ec=INK, lw=1.0, z=1):
    """Draw a box; return the three visible face patches (front, top, right)."""
    front = [_P(x0, y0, z0), _P(x0 + w, y0, z0), _P(x0 + w, y0 + h, z0), _P(x0, y0 + h, z0)]
    top = [_P(x0, y0 + h, z0), _P(x0 + w, y0 + h, z0), _P(x0 + w, y0 + h, z0 + d), _P(x0, y0 + h, z0 + d)]
    side = [_P(x0 + w, y0, z0), _P(x0 + w, y0, z0 + d), _P(x0 + w, y0 + h, z0 + d), _P(x0 + w, y0 + h, z0)]
    pf = _poly(ax, front, fc=fc[0], ec=ec, lw=lw, zorder=z)
    pt = _poly(ax, top, fc=fc[1], ec=ec, lw=lw, zorder=z)
    ps = _poly(ax, side, fc=fc[2], ec=ec, lw=lw, zorder=z)
    return pf, pt, ps


def _clip(artist, patch):
    artist.set_clip_path(patch)
    return artist


def _proj_circle(cx, cy, cz, r, plane, n=24):
    t = np.linspace(0, 2 * np.pi, n)
    if plane == "front":
        pts = [_P(cx + r * np.cos(a), cy + r * np.sin(a), cz) for a in t]
    elif plane == "top":
        pts = [_P(cx + r * np.cos(a), cy, cz + r * np.sin(a)) for a in t]
    else:  # side
        pts = [_P(cx, cy + r * np.cos(a), cz + r * np.sin(a)) for a in t]
    return np.array(pts)


# ---------------------------------------------------------------- 22.1
def composite_architectures():
    fig, axs = plt.subplots(2, 3, figsize=(6.8, 3.85))
    rng = np.random.default_rng(3)
    W, H, D = 2.8, 1.5, 2.2
    for i, ax in enumerate(axs.flat):
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_xlim(-0.5, 5.1)
        ax.set_ylim((-1.0, 2.6) if i < 3 else (-1.15, 2.45))

    # (a) particulate --------------------------------------------------
    ax = axs[0, 0]
    pf, pt, ps = _block(ax, 0, 0, 0, W, H, D)
    for face, patch in (("front", pf), ("top", pt), ("side", ps)):
        npart = {"front": 22, "top": 26, "side": 16}[face]
        for _ in range(npart):
            r = rng.uniform(0.06, 0.13)
            if face == "front":
                c = _proj_circle(rng.uniform(0, W), rng.uniform(0, H), 0, r, "front")
            elif face == "top":
                c = _proj_circle(rng.uniform(0, W), H, rng.uniform(0, D), r, "top")
            else:
                c = _proj_circle(W, rng.uniform(0, H), rng.uniform(0, D), r, "side")
            p = Polygon(c, closed=True, fc="#7A7A7A", ec="none", zorder=2)
            ax.add_patch(p)
            _clip(p, patch)
    ax.text(1.6, -0.45, "(a) particulate", ha="center", fontsize=9, fontweight="bold")
    ax.text(1.6, -0.85, "Al–SiCp, filled polymers, concrete", ha="center", fontsize=7.6)

    # (b) short fibre ---------------------------------------------------
    ax = axs[0, 1]
    pf, pt, ps = _block(ax, 0, 0, 0, W, H, D)
    L = 0.55
    for _ in range(55):  # top face: fibres in x-z plane, partly aligned with x (flow)
        x, z = rng.uniform(-0.2, W), rng.uniform(0, D)
        ang = rng.normal(0, 25) if rng.random() < 0.75 else rng.uniform(-90, 90)
        a = np.radians(ang)
        p0, p1 = _P(x, H, z), _P(x + L * np.cos(a), H, z + L * np.sin(a))
        ln, = ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=FIBRE, lw=0.9, zorder=2, solid_capstyle="round")
        _clip(ln, pt)
    for _ in range(40):  # front face: fibres cut obliquely -> short dashes and dots
        x, y = rng.uniform(0, W), rng.uniform(0.05, H - 0.05)
        if rng.random() < 0.7:
            a = np.radians(rng.normal(0, 15))
            l = rng.uniform(0.2, 0.5)
            ln, = ax.plot([x, x + l * np.cos(a)], [y, y + l * np.sin(a) * 0.3], color=FIBRE, lw=0.9, zorder=2)
        else:
            ln, = ax.plot([x], [y], "o", color=FIBRE, ms=1.8, zorder=2)
        _clip(ln, pf)
    for _ in range(30):  # side face: mostly fibre ends (dots)
        y, z = rng.uniform(0.05, H - 0.05), rng.uniform(0, D)
        q = _P(W, y, z)
        ln, = ax.plot([q[0]], [q[1]], "o", color=FIBRE, ms=1.8, zorder=2)
        _clip(ln, ps)
    a0, a1 = _P(0.2, H + 0.0, D + 0.55), _P(2.6, H, D + 0.55)
    ax.annotate("", xy=a1, xytext=a0, arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.4, mutation_scale=11))
    ax.text((a0[0] + a1[0]) / 2, a0[1] + 0.12, "flow", color=COLORS[0], fontsize=8, ha="center")
    ax.text(1.6, -0.45, "(b) short fibre", ha="center", fontsize=9, fontweight="bold")
    ax.text(1.6, -0.85, "glass-filled PA66, SMC", ha="center", fontsize=7.6)

    # (c) unidirectional ------------------------------------------------
    ax = axs[0, 2]
    pf, pt, ps = _block(ax, 0, 0, 0, W, H, D)
    for z in np.linspace(0.08, D - 0.08, 14):  # top face: lines along x
        p0, p1 = _P(0, H, z), _P(W, H, z)
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=FIBRE, lw=0.8, zorder=2)
    for y in np.linspace(0.08, H - 0.08, 10):  # front face: lines along x
        ax.plot([0, W], [y, y], color=FIBRE, lw=0.8, zorder=2)
    for y in np.linspace(0.08, H - 0.08, 10):  # side face: fibre ends
        for z in np.linspace(0.08, D - 0.08, 14):
            q = _P(W, y, z)
            ax.plot(q[0], q[1], "o", color=FIBRE, ms=1.6, zorder=2)
    o = (4.15, 0.1)
    ax.annotate("", xy=(o[0] + 0.7, o[1] - 0.0), xytext=o, arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.2, mutation_scale=9))
    ax.text(o[0] + 0.78, o[1], "1", color=COLORS[1], fontsize=9, va="center", fontweight="bold")
    q = (o[0] + 0.55 * 1.3 * np.cos(np.radians(35)), o[1] + 0.55 * 1.3 * np.sin(np.radians(35)))
    ax.annotate("", xy=q, xytext=o, arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.2, mutation_scale=9))
    ax.text(q[0] + 0.07, q[1] + 0.05, "2", color=COLORS[1], fontsize=9, fontweight="bold")
    ax.annotate("", xy=(o[0], o[1] + 0.8), xytext=o, arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.2, mutation_scale=9))
    ax.text(o[0] + 0.08, o[1] + 0.85, "3", color=COLORS[1], fontsize=9, fontweight="bold", ha="left")
    ax.text(1.6, -0.45, "(c) unidirectional", ha="center", fontsize=9, fontweight="bold")
    ax.text(1.6, -0.85, "UD prepreg ply", ha="center", fontsize=7.6)

    # (d) woven fabric (plain weave) -------------------------------------
    ax = axs[1, 0]
    Hw = 0.7
    pf, pt, ps = _block(ax, 0, 0, 0, W, Hw, D)
    n_x, n_z = 6, 5
    dx, dz = W / n_x, D / n_z
    warp_c, weft_c = "#9DB7D5", "#D9A87E"
    for i in range(n_x):
        for j in range(n_z):
            over_warp = (i + j) % 2 == 0
            x0, z0 = i * dx, j * dz
            if over_warp:   # warp tow (along x) on top: lines along x
                pts = [_P(x0, Hw, z0 + 0.06 * dz), _P(x0 + dx, Hw, z0 + 0.06 * dz),
                       _P(x0 + dx, Hw, z0 + 0.94 * dz), _P(x0, Hw, z0 + 0.94 * dz)]
                _poly(ax, pts, fc=warp_c, ec=INK, lw=0.5, zorder=2)
                for f in (0.3, 0.5, 0.7):
                    a, b = _P(x0, Hw, z0 + f * dz), _P(x0 + dx, Hw, z0 + f * dz)
                    ax.plot([a[0], b[0]], [a[1], b[1]], color="#4C6A8C", lw=0.4, zorder=3)
            else:           # weft tow (along z) on top: lines along z
                pts = [_P(x0 + 0.06 * dx, Hw, z0), _P(x0 + 0.94 * dx, Hw, z0),
                       _P(x0 + 0.94 * dx, Hw, z0 + dz), _P(x0 + 0.06 * dx, Hw, z0 + dz)]
                _poly(ax, pts, fc=weft_c, ec=INK, lw=0.5, zorder=2)
                for f in (0.3, 0.5, 0.7):
                    a, b = _P(x0 + f * dx, Hw, z0), _P(x0 + f * dx, Hw, z0 + dz)
                    ax.plot([a[0], b[0]], [a[1], b[1]], color="#8C5A2E", lw=0.4, zorder=3)
    # front face: weft tows in section (ellipses) and a crimped warp tow
    xs = np.linspace(0, W, 300)
    yc = Hw / 2 + 0.17 * np.cos(np.pi * xs / dx)
    for i in range(n_x):
        xc = (i + 0.5) * dx
        yy = Hw / 2 - 0.15 * np.cos(np.pi * xc / dx)
        e = Polygon(np.column_stack([xc + 0.42 * dx * np.cos(np.linspace(0, 2 * np.pi, 30)),
                                     yy + 0.11 * np.sin(np.linspace(0, 2 * np.pi, 30))]),
                    closed=True, fc=weft_c, ec=INK, lw=0.5, zorder=2)
        ax.add_patch(e)
        _clip(e, pf)
    band = Polygon(np.concatenate([np.column_stack([xs, yc + 0.07]), np.column_stack([xs[::-1], yc[::-1] - 0.07])]),
                   closed=True, fc=warp_c, ec=INK, lw=0.5, zorder=3)
    ax.add_patch(band)
    _clip(band, pf)
    p = _P(W + 0.1, Hw, D * 0.5)
    q = _P(0.2, Hw, D)
    ax.text(q[0], q[1] + 0.12, "warp", color="#4C6A8C", fontsize=8)
    q = _P(2.0, Hw, D)
    ax.text(q[0], q[1] + 0.12, "weft", color="#8C5A2E", fontsize=8)
    ax.annotate("crimp", xy=(0.25 * dx * 2, Hw / 2 + 0.2), xytext=(-0.25, -0.25), fontsize=7.5, color=INK,
                arrowprops=dict(arrowstyle="-", lw=0.6, color="0.3"))
    ax.text(1.6, -0.6, "(d) woven fabric", ha="center", fontsize=9, fontweight="bold")
    ax.text(1.6, -1.0, "woven fabric ply", ha="center", fontsize=7.6)

    # (e) laminate: slightly exploded stack of four plies ---------------------
    ax = axs[1, 2 - 1]
    t, gap, Dl = 0.11, 0.42, 1.7
    angles = [0, 45, -45, 90]  # top to bottom
    cols = ["#C9D9EA", "#F1D7B5", "#D7EBC9", "#E8CFE0"]
    nply = len(angles)
    for k in range(nply - 1, -1, -1):  # draw bottom ply first
        y0 = (nply - 1 - k) * (t + gap)
        base_z = 10 + (nply - 1 - k) * 2
        pf_, pt_, ps_ = _block(ax, 0, y0, 0, W, t, Dl, fc=(cols[k], cols[k], cols[k]), lw=0.8, z=base_z)
        th = np.radians(angles[k])
        dvec = np.array([np.cos(th), np.sin(th)])
        nvec = np.array([-np.sin(th), np.cos(th)])
        for off in np.arange(-3.0, 3.0, 0.15):
            base = np.array([W / 2, Dl / 2]) + off * nvec
            p0 = _P(base[0] - 4 * dvec[0], y0 + t, base[1] - 4 * dvec[1])
            p1 = _P(base[0] + 4 * dvec[0], y0 + t, base[1] + 4 * dvec[1])
            ln, = ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color="#555555", lw=0.45, zorder=base_z + 0.5)
            _clip(ln, pt_)
        lab = f"{angles[k]:+d}°".replace("-", "−") if angles[k] not in (0, 90) else f"{angles[k]}°"
        ax.text(-0.1, y0 + t / 2, lab, ha="right", va="center", fontsize=8)
    ax.text(1.6, -0.6, "(e) laminate", ha="center", fontsize=9, fontweight="bold")
    ax.text(1.6, -1.0, "laminate [0/+45/−45/90]", ha="center", fontsize=7.6)

    # (f) sandwich ----------------------------------------------------------
    ax = axs[1, 2]
    tf, c = 0.14, 1.0
    face_c = ("#5F6B7A", "#7F8B99", "#55606D")
    _block(ax, 0, 0, 0, W, tf, D, fc=face_c, lw=0.8, z=1)
    pf, pt, ps = _block(ax, 0, tf, 0, W, c, D, fc=("#F6E7B0", "#FAF0CC", "#EADAA0"), lw=0.8, z=1.1)
    # honeycomb cell walls in section on the front and side faces
    cell = 0.28
    for x in np.arange(0.0, W + 0.01, cell):
        ax.plot([x, x], [tf, tf + c], color="#9C8640", lw=0.7, zorder=1.2)
    for z in np.arange(0.0, D + 0.01, cell):
        a, b = _P(W, tf, z), _P(W, tf + c, z)
        ax.plot([a[0], b[0]], [a[1], b[1]], color="#9C8640", lw=0.7, zorder=1.2)
    # upper face cut back to reveal hexagons on the core top
    zc = 1.05
    for i in range(-1, 12):
        for j in range(-1, 8):
            cx = i * 1.5 * 0.17 + 0.05
            cz = j * np.sqrt(3) * 0.17 + (0.0 if i % 2 == 0 else np.sqrt(3) / 2 * 0.17)
            hexa = [_P(cx + 0.17 * np.cos(a), tf + c, cz + 0.17 * np.sin(a)) for a in np.radians(np.arange(0, 360, 60))]
            hp = Polygon(np.array(hexa), closed=True, fc="none", ec="#9C8640", lw=0.6, zorder=1.3)
            ax.add_patch(hp)
            _clip(hp, pt)
    _block(ax, 0, tf + c, zc, W, tf, D - zc, fc=face_c, lw=0.8, z=1.5)
    q = _P(W, tf + c + tf, D)
    ax.text(q[0] + 0.1, q[1] + 0.15, "face sheet", fontsize=7.5, va="center")
    q = _P(W, tf + c / 2, D)
    ax.text(q[0] + 0.1, q[1] - 0.3, "honeycomb\ncore", fontsize=7.5, va="center")
    ax.text(1.6, -0.6, "(f) sandwich", ha="center", fontsize=9, fontweight="bold")
    ax.text(1.6, -1.0, "sandwich panel", ha="center", fontsize=7.6)

    fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.11, wspace=0.08, hspace=0.12)
    fig.patches.append(FancyArrowPatch((0.08, 0.045), (0.92, 0.045), transform=fig.transFigure,
                                       arrowstyle="-|>", mutation_scale=14, color=INK, lw=1.3))
    fig.text(0.08, 0.065, "isotropic, modest reinforcement", fontsize=8.5, ha="left", va="bottom")
    fig.text(0.92, 0.065, "anisotropic, maximum reinforcement along fibres", fontsize=8.5, ha="right", va="bottom")
    save(fig, "22", "fig-22-1-composite-architectures")


# ---------------------------------------------------------------- 22.2
def micromechanics_moduli():
    Ef, nf, Em, nm = 72.0, 0.22, 3.5, 0.35
    Gf, Gm = Ef / (2 * (1 + nf)), Em / (2 * (1 + nm))
    V = np.linspace(0, 0.8, 300)

    def ht(Pf, Pm, xi, v):
        eta = (Pf / Pm - 1) / (Pf / Pm + xi)
        return Pm * (1 + xi * eta * v) / (1 - eta * v)

    E1 = V * Ef + (1 - V) * Em
    E2R = 1 / (V / Ef + (1 - V) / Em)
    E2H = ht(Ef, Em, 2.0, V)
    G12H = ht(Gf, Gm, 1.0, V)

    fig, ax = new_fig(6.4, 4.4)
    ax.plot(V, E1, color=COLORS[0], label=r"$E_1$ rule of mixtures (Voigt)")
    ax.plot(V, E2H, color=COLORS[1], label=r"$E_2$ Halpin–Tsai, $\xi=2$")
    ax.plot(V, E2R, color=COLORS[1], ls=(0, (4, 2)), lw=1.4, label=r"$E_2$ inverse rule (Reuss bound)")
    ax.plot(V, G12H, color=COLORS[2], ls="--", label=r"$G_{12}$ Halpin–Tsai, $\xi=1$")
    ax.add_patch(Rectangle((0.575, 12), 0.05, 4, fc=COLORS[4], alpha=0.35, ec="none", zorder=0))
    ax.annotate("typical measured $E_2$,\n12–16 GPa", xy=(0.575, 14.5), xytext=(0.36, 22.5), fontsize=8,
                ha="center", arrowprops=dict(arrowstyle="-", lw=0.6, color="0.35"))
    ax.axvline(0.6, color="0.45", ls=":", lw=1.0)
    vals = [(44.6, COLORS[0]), (14.9, COLORS[1]), (8.2, COLORS[1]), (4.46, COLORS[2])]
    for v, c in vals:
        ax.plot(0.6, v, "o", color=c, ms=5, zorder=5)
    ax.text(0.615, 44.6 - 1.2, "44.6", fontsize=8, color=COLORS[0], va="top")
    ax.text(0.615, 14.9 - 1.6, "14.9", fontsize=8, color=COLORS[1], va="top")
    ax.text(0.615, 8.2 - 0.5, "8.2", fontsize=8, color=COLORS[1], va="top")
    ax.text(0.615, 4.46 - 0.7, "4.46 GPa", fontsize=8, color=COLORS[2], va="top")
    ax.set_xlim(0, 0.8)
    ax.set_ylim(0, 60)
    ax.set_xlabel(r"fibre volume fraction $V_f$")
    ax.set_ylabel("modulus (GPa)")
    ax.legend(loc="upper left", fontsize=8.2)
    ax.text(0.79, 31, "E-glass/epoxy:\n$E_f$ = 72 GPa, $\\nu_f$ = 0.22\n$E_m$ = 3.5 GPa, $\\nu_m$ = 0.35",
            fontsize=7.6, ha="right", va="bottom", color="0.3", bbox=dict(fc="white", ec="none", pad=1))
    # process windows above the axes
    trans = mtransforms.blended_transform_factory(ax.transData, ax.transAxes)
    wins = [(0.30, 0.45, "hand lay-up 0.30–0.45", 1.03, "left"), (0.50, 0.60, "RTM / infusion 0.50–0.60", 1.09, "left"),
            (0.55, 0.65, "prepreg 0.55–0.65", 1.15, "right")]
    for a, b, lab, yy, side in wins:
        ax.plot([a, b], [yy, yy], transform=trans, color=COLORS[3], lw=4, solid_capstyle="butt", clip_on=False)
        if side == "left":
            ax.text(a - 0.01, yy, lab, transform=trans, fontsize=7.5, va="center", ha="right", clip_on=False)
        else:
            ax.text(b + 0.01, yy, lab, transform=trans, fontsize=7.5, va="center", ha="left", clip_on=False)
    ax.text(0.0, 1.15, "process windows:", transform=trans, fontsize=7.5, va="center", ha="left", color=COLORS[3])
    save(fig, "22", "fig-22-2-micromechanics-moduli")


# ---------------------------------------------------------------- 22.3
def shear_lag_critical_length():
    fig = plt.figure(figsize=(6.8, 4.3))
    gs = fig.add_gridspec(2, 2, height_ratios=[3, 1.25], width_ratios=[1, 1], hspace=0.12, wspace=0.32)
    ax = fig.add_subplot(gs[0, 0])
    axt = fig.add_subplot(gs[1, 0], sharex=ax)
    axr = fig.add_subplot(gs[:, 1])

    s = np.linspace(0, 1, 601)
    cases = [(0.5, COLORS[2], r"$L=0.5\,l_c$"), (1.0, COLORS[1], r"$L=l_c$"), (3.0, COLORS[0], r"$L=3\,l_c$")]
    for r, c, lab in cases:
        prof = np.minimum(2 * r * np.minimum(s, 1 - s), 1.0)
        ax.plot(s, prof, color=c, label=lab)
    bL2 = 6.0
    cox = 1 - np.cosh(bL2 * (1 - 2 * s)) / np.cosh(bL2)
    ax.plot(s, cox, ":", color=INK, lw=1.4, label="Cox elastic (cosh)")
    ax.axhline(1.0, color="0.6", lw=0.6)
    ax.text(0.5, 1.03, r"$\sigma_{fu}$", ha="center", fontsize=8.5, color="0.35")
    ax.annotate("", xy=(0, 0.88), xytext=(1 / 6, 0.88), arrowprops=dict(arrowstyle="<|-|>", lw=0.8, mutation_scale=7, color=COLORS[0]))
    ax.text(1 / 12, 0.80, r"$l_c/2$", ha="center", fontsize=8, color=COLORS[0])
    ax.set_ylim(0, 1.12)
    ax.set_ylabel(r"$\sigma_f/\sigma_{fu}$")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2, fontsize=7.4, handlelength=1.8, columnspacing=1.0)
    plt.setp(ax.get_xticklabels(), visible=False)
    pass

    for r, c, ls in ((3.0, COLORS[0], "-"), (1.0, COLORS[1], "--")):
        x1 = min(1 / (2 * r), 0.5)
        tau = np.where(s < x1, 1.0, np.where(s > 1 - x1, -1.0, 0.0))
        axt.plot(s, tau, color=c, ls=ls, lw=1.4, drawstyle="steps-mid")
    axt.axhline(0, color="0.6", lw=0.6)
    axt.set_ylim(-1.5, 1.5)
    axt.set_yticks([-1, 0, 1])
    axt.set_yticklabels([r"$-\tau$", "0", r"$+\tau$"])
    axt.set_ylabel("interface\nshear", fontsize=8.5)
    axt.set_xlabel("position along fibre $x/L$")
    axt.set_xlim(0, 1)

    # right: efficiencies
    lc, inv_beta = 0.333, 0.02789
    L = np.logspace(np.log10(0.05), 1, 400)
    eta_s = np.where(L < lc, L / (2 * lc), 1 - lc / (2 * L))
    bL = L / inv_beta / 2
    eta_L = 1 - np.tanh(bL) / bL
    axr.axvspan(0.2, 0.5, color=COLORS[4], alpha=0.22, lw=0)
    axr.text(0.316, 0.04, "typical fibre length\nafter injection\nmoulding", ha="center", fontsize=7.4, va="bottom")
    axr.plot(L, eta_L, color=COLORS[3], label=r"stiffness $\eta_L$ (Cox, $1/\beta$ = 28 μm)")
    axr.plot(L, eta_s, color=COLORS[0], label=r"strength $\eta$ (Kelly–Tyson, $l_c$ = 0.33 mm)")
    for x, y in ((0.3, 0.45), (0.333, 0.5), (3.0, 0.94)):
        axr.plot(x, y, "o", color=COLORS[0], ms=4.5, zorder=5)
    for x, y in ((0.1, 0.47), (0.3, 0.81), (1.0, 0.94)):
        axr.plot(x, y, "s", color=COLORS[3], ms=4.5, zorder=5)
    axr.annotate("0.45", xy=(0.3, 0.45), xytext=(0.55, 0.36), fontsize=7.6, color=COLORS[0],
                 arrowprops=dict(arrowstyle="-", lw=0.5, color=COLORS[0]))
    axr.annotate("0.94", xy=(3.0, 0.94), xytext=(3.0, 0.78), fontsize=7.6, color=COLORS[0], ha="center",
                 arrowprops=dict(arrowstyle="-", lw=0.5, color=COLORS[0]))
    axr.annotate("0.81", xy=(0.3, 0.81), xytext=(0.6, 0.72), fontsize=7.6, color=COLORS[3],
                 arrowprops=dict(arrowstyle="-", lw=0.5, color=COLORS[3]))
    axr.annotate("0.47", xy=(0.1, 0.47), xytext=(0.06, 0.58), fontsize=7.6, color=COLORS[3],
                 arrowprops=dict(arrowstyle="-", lw=0.5, color=COLORS[3]))
    axr.axvline(lc, color="0.55", ls=":", lw=0.9)
    axr.text(lc * 1.06, 0.27, r"$l_c$", fontsize=8.5, color="0.35")
    axr.set_xscale("log")
    axr.set_xlim(0.05, 10)
    axr.set_ylim(0, 1.08)
    axr.set_xticks([0.1, 0.3, 1, 3, 10])
    axr.set_xticklabels(["0.1", "0.3", "1", "3", "10"])
    axr.set_xlabel("fibre length $L$ (mm)")
    axr.set_ylabel("efficiency factor")
    axr.text(0.055, 1.075, "stiffness $\\eta_L$\n(Cox, $1/\\beta$ = 28 μm)", color=COLORS[3], fontsize=7.6, va="top")
    axr.text(1.15, 0.6, "strength $\\eta$\n(Kelly–Tyson,\n$l_c$ = 0.33 mm)", color=COLORS[0], fontsize=7.6, va="top")
    axr.set_title("E-glass in PA66, $d$ = 10 μm", fontsize=9.5)
    save(fig, "22", "fig-22-3-shear-lag-critical-length")


# ---------------------------------------------------------------- 22.4
def _stress_element(ax, cx, cy, a, ang_deg, labels, color):
    """Square element of half-size a rotated by ang; labels = (normal-1, normal-2, shear)."""
    th = np.radians(ang_deg)
    R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    sq = np.array([[-a, -a], [a, -a], [a, a], [-a, a]]) @ R.T + [cx, cy]
    _poly(ax, sq, fc="#F5F5F5", ec=INK, lw=1.0, zorder=3)
    e1, e2 = R @ [1, 0], R @ [0, 1]
    c = np.array([cx, cy])
    L = 0.75 * a
    kw = dict(arrowstyle="-|>", color=color, lw=1.2, mutation_scale=9)
    for sgn in (1, -1):
        p = c + sgn * a * e1
        ax.annotate("", xy=p + sgn * L * e1, xytext=p, arrowprops=kw, zorder=4)
        p = c + sgn * a * e2
        ax.annotate("", xy=p + sgn * L * e2, xytext=p, arrowprops=kw, zorder=4)
    # shear arrows along faces
    sk = dict(arrowstyle="-|>", color=COLORS[3], lw=1.1, mutation_scale=8)
    off = 0.15 * a
    for sgn in (1, -1):
        p = c + sgn * (a + off) * e1
        ax.annotate("", xy=p + sgn * 0.6 * a * e2, xytext=p - sgn * 0.6 * a * e2, arrowprops=sk, zorder=4)
        p = c + sgn * (a + off) * e2
        ax.annotate("", xy=p + sgn * 0.6 * a * e1, xytext=p - sgn * 0.6 * a * e1, arrowprops=sk, zorder=4)
    t1 = c + (a + L + 0.35) * e1
    t2 = c + (a + L + 0.3) * e2
    ax.text(*t1, labels[0], fontsize=9, ha="center", va="center", color=color)
    ax.text(*t2, labels[1], fontsize=9, ha="center", va="center", color=color)
    t3 = c + (a + 0.55) * e1 + 0.95 * a * e2
    ax.text(*t3, labels[2], fontsize=9, ha="left", va="center", color=COLORS[3])


def lamina_axes():
    fig, ax = schematic(6.8, 4.6, xlim=(0, 15), ylim=(0, 10.2))
    # ply
    x0, y0, w, h = 0.8, 2.6, 7.6, 5.0
    ply = Rectangle((x0, y0), w, h, fc="#F3E9C6", ec=INK, lw=1.2, zorder=1)
    ax.add_patch(ply)
    th = np.radians(30)
    d, n = np.array([np.cos(th), np.sin(th)]), np.array([-np.sin(th), np.cos(th)])
    cen = np.array([x0 + w / 2, y0 + h / 2])
    for s in np.arange(-8, 8, 0.28):
        p0, p1 = cen + s * n - 10 * d, cen + s * n + 10 * d
        ln, = ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color="#8A7A50", lw=0.55, zorder=2)
        ln.set_clip_path(ply)
    # axes at the ply centre
    o = cen
    kx = dict(arrowstyle="-|>", color=INK, lw=1.5, mutation_scale=12)
    ax.annotate("", xy=o + [3.3, 0], xytext=o, arrowprops=kx, zorder=5)
    ax.annotate("", xy=o + [0, 2.25], xytext=o, arrowprops=kx, zorder=5)
    ax.text(*(o + [3.45, -0.05]), "$x$", fontsize=12, va="center", zorder=6)
    ax.text(*(o + [0.25, 2.2]), "$y$", fontsize=12, ha="left", va="center", zorder=6)
    k1 = dict(arrowstyle="-|>", color=COLORS[1], lw=1.8, mutation_scale=12)
    ax.annotate("", xy=o + 3.3 * d, xytext=o, arrowprops=k1, zorder=5)
    ax.annotate("", xy=o + 2.6 * n, xytext=o, arrowprops=k1, zorder=5)
    ax.text(*(o + 3.55 * d), "1", fontsize=12, color=COLORS[1], fontweight="bold", ha="center", va="center", zorder=6)
    ax.text(*(o + 2.85 * n), "2", fontsize=12, color=COLORS[1], fontweight="bold", ha="center", va="center", zorder=6)
    t = np.linspace(0, th, 40)
    ax.plot(o[0] + 1.6 * np.cos(t), o[1] + 1.6 * np.sin(t), color=COLORS[1], lw=1.1, zorder=5)
    ax.annotate("", xy=(o[0] + 1.6 * np.cos(th), o[1] + 1.6 * np.sin(th)),
                xytext=(o[0] + 1.6 * np.cos(th - 0.08), o[1] + 1.6 * np.sin(th - 0.08)),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.0, mutation_scale=8), zorder=5)
    ax.text(o[0] + 1.85 * np.cos(th / 2), o[1] + 1.85 * np.sin(th / 2), r"$\theta=+30^\circ$", fontsize=9,
            color=COLORS[1], va="center", zorder=6,
            bbox=dict(fc="#F3E9C6", ec="none", pad=0.5))
    # uniaxial load sigma_x on the ply edges
    for yy in np.linspace(y0 + 0.6, y0 + h - 0.6, 5):
        ax.annotate("", xy=(x0 - 0.65, yy), xytext=(x0, yy),
                    arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.1, mutation_scale=8))
        ax.annotate("", xy=(x0 + w + 0.65, yy), xytext=(x0 + w, yy),
                    arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.1, mutation_scale=8))
    ax.text(x0 + w + 0.75, y0 + h - 0.6, r"$\sigma_x$", color=COLORS[0], fontsize=10, va="center")
    # sheared outline (exaggerated)
    g = 0.10
    sh = np.array([[x0, y0], [x0 + w, y0], [x0 + w, y0 + h], [x0, y0 + h]])
    sh2 = sh.copy()
    sh2[:, 0] += -g * (sh[:, 1] - (y0 + h / 2)) * 1.0
    _poly(ax, sh2, fill=False, ec=COLORS[0], lw=1.0, ls="--", zorder=3)
    ax.text(x0 + w / 2, y0 - 0.35, "off-axis load produces shear strain $\\gamma_{xy}$: extension–shear coupling",
            fontsize=8.5, color=COLORS[0], ha="center", va="top")
    ax.text(x0 + w / 2, y0 + h + 0.25, "unidirectional ply, top view (dashed: sheared shape, exaggerated)",
            fontsize=8, color="0.3", ha="center", va="bottom")

    # stress elements
    _stress_element(ax, 11.6, 8.3, 0.75, 0, (r"$\sigma_x$", r"$\sigma_y$", r"$\tau_{xy}$"), COLORS[0])
    ax.text(11.6, 6.35, "structural axes $x$–$y$", fontsize=8, ha="center")
    _stress_element(ax, 11.6, 4.3, 0.75, 30, (r"$\sigma_1$", r"$\sigma_2$", r"$\tau_{12}$"), COLORS[1])
    ax.text(11.6, 2.25, "material axes 1–2", fontsize=8, ha="center")

    # thickness inset (edge view)
    bx, by = 10.4, 0.35
    ax.add_patch(Rectangle((bx, by + 0.45), 2.6, 0.45, fc="#F3E9C6", ec=INK, lw=1.0))
    for xx in np.linspace(bx + 0.12, bx + 2.48, 12):
        ax.plot(xx, by + 0.675, "o", color="#8A7A50", ms=1.8)
    ax.annotate("", xy=(bx + 2.8, by + 0.9), xytext=(bx + 2.8, by + 0.45),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, mutation_scale=6, shrinkA=0, shrinkB=0))
    ax.text(bx + 2.95, by + 0.675, "0.125 mm", fontsize=7.6, va="center")
    ax.annotate("", xy=(bx - 0.35, by + 1.6), xytext=(bx - 0.35, by + 0.45),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.3, mutation_scale=9))
    ax.text(bx - 0.55, by + 1.45, "3", color=COLORS[1], fontsize=10, fontweight="bold", ha="right", va="center")
    ax.text(bx + 1.3, by + 0.05, "edge view (fibres along 1, end-on)", fontsize=7.4, ha="center", va="center")
    save(fig, "22", "fig-22-4-lamina-axes")


# ---------------------------------------------------------------- 22.5
def _Ex(p, th):
    c, s = np.cos(th), np.sin(th)
    return 1 / (c ** 4 / p["E1"] + (1 / p["G12"] - 2 * p["n12"] / p["E1"]) * s * s * c * c + s ** 4 / p["E2"])


def _Gxy(p, th):
    c, s = np.cos(th), np.sin(th)
    E1, E2, G, n = p["E1"], p["E2"], p["G12"], p["n12"]
    return 1 / (2 * (2 / E1 + 2 / E2 + 4 * n / E1 - 1 / G) * s * s * c * c + (s ** 4 + c ** 4) / G)


def off_axis_moduli():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(6.8, 3.9), gridspec_kw=dict(width_ratios=[1.45, 1], wspace=0.3))
    th = np.radians(np.linspace(0, 90, 361))
    deg = np.degrees(th)
    ax.plot(deg, _Ex(T300, th), color=COLORS[0], label="T300/epoxy")
    ax.plot(deg, _Ex(GLASS, th), color=COLORS[1], label="E-glass/epoxy")
    tc = np.array([0, 5, 10, 15, 30, 45, 60, 90])
    ax.plot(tc, _Ex(T300, np.radians(tc)), "o", color=COLORS[0], ms=3.5)
    tg = np.array([0, 15, 30, 45, 60, 90])
    ax.plot(tg, _Ex(GLASS, np.radians(tg)), "s", color=COLORS[1], ms=3.5)
    ax.annotate("5° misalignment:\n−15 % stiffness", xy=(5, 154), xytext=(14, 160), fontsize=8,
                arrowprops=dict(arrowstyle="-|>", lw=0.8, mutation_scale=8), va="center")
    ax.annotate("15°: 72.6 GPa", xy=(15, 72.6), xytext=(22, 92), fontsize=8,
                arrowprops=dict(arrowstyle="-", lw=0.6, color="0.4"))
    ax.text(88, 13.5, "10.3", fontsize=7.6, color=COLORS[0], ha="right", va="bottom")
    ax.text(88, 3.2, "8.27", fontsize=7.6, color=COLORS[1], ha="right", va="top")
    ax.set_xlim(0, 90)
    ax.set_ylim(0, 200)
    ax.set_xticks([0, 15, 30, 45, 60, 75, 90])
    ax.set_xlabel(r"fibre angle $\theta$ (°)")
    ax.set_ylabel(r"off-axis modulus $E_x$ (GPa)")
    ax.legend(loc="center right", fontsize=8, bbox_to_anchor=(1.0, 0.36))
    # polar inset
    ins = fig.add_axes([0.33, 0.52, 0.2, 0.34], projection="polar")
    tt = np.linspace(0, 2 * np.pi, 721)
    ins.plot(tt, _Ex(T300, tt), color=COLORS[0], lw=1.2)
    ins.fill(tt, _Ex(T300, tt), color=COLORS[0], alpha=0.15)
    ins.set_rmax(190)
    ins.set_rticks([])
    ins.set_xticks(np.radians([0, 90, 180, 270]))
    ins.set_xticklabels(["0°", "90°", "", ""], fontsize=7)
    ins.tick_params(pad=-2)
    ins.grid(color="0.85", lw=0.5)
    ins.set_title("$E_x(\\theta)$ polar, T300", fontsize=7.5, pad=2)

    ax2.plot(deg, _Gxy(T300, th), color=COLORS[0], label="T300/epoxy")
    ax2.plot(deg, _Gxy(GLASS, th), color=COLORS[1], ls="--", lw=1.4, label="E-glass/epoxy")
    for t, v in ((0, 7.17), (30, 8.76), (45, 9.46)):
        ax2.plot(t, v, "o", color=COLORS[0], ms=3.5)
    ax2.text(0.8, 7.17 - 0.35, "7.17", fontsize=7.6, color=COLORS[0], va="top")
    ax2.text(30, 8.76 - 0.4, "8.76", fontsize=7.6, color=COLORS[0], ha="center", va="top")
    ax2.text(45, 9.46 + 0.25, "9.46", fontsize=7.6, color=COLORS[0], ha="center", va="bottom")
    ax2.set_xlim(0, 90)
    ax2.set_ylim(0, 12)
    ax2.set_xticks([0, 15, 30, 45, 60, 75, 90])
    ax2.set_xlabel(r"fibre angle $\theta$ (°)")
    ax2.set_ylabel(r"in-plane shear modulus $G_{xy}$ (GPa)")
    ax2.legend(loc="lower center", fontsize=8)
    ax2.text(45, 11.3, "single ply; symmetric about 45°", fontsize=7.6, ha="center", color="0.3")
    save(fig, "22", "fig-22-5-off-axis-moduli")


# ---------------------------------------------------------------- 22.6
def ply_thermal_expansion():
    a1, a2 = T300["a1"], T300["a2"]
    fig, (ax, axi) = plt.subplots(1, 2, figsize=(6.8, 3.9), gridspec_kw=dict(width_ratios=[1.55, 1], wspace=0.08))
    t = np.linspace(0, 90, 361)
    c, s = np.cos(np.radians(t)), np.sin(np.radians(t))
    ax_ = a1 * c ** 2 + a2 * s ** 2
    ay_ = a1 * s ** 2 + a2 * c ** 2
    axy = 2 * (a1 - a2) * s * c
    for v, lab in ((23, "aluminium 23"), (12, "steel 12"), (1.2, "Invar 1.2")):
        ax.axhline(v, color="0.6", lw=0.7, ls=":")
        ax.text(89, v + 0.5, lab, fontsize=7.3, color="0.4", ha="right", va="bottom")
    ax.axhline(0, color="0.4", lw=0.6)
    ax.plot(t, ax_, color=COLORS[0], label=r"$\alpha_x$")
    ax.plot(t, ay_, color=COLORS[1], label=r"$\alpha_y$")
    ax.plot(t, axy, color=COLORS[2], ls="--", label=r"$\alpha_{xy}$ (shear)")
    for tt, v in ((30, 5.6), (45, 11.3), (60, 16.9)):
        ax.plot(tt, v, "o", color=COLORS[0], ms=3.5, zorder=5)
    ax.text(31, 4.3, "5.6", fontsize=7.5, color=COLORS[0], va="top")
    ax.text(47, 7.6, "11.3", fontsize=7.5, color=COLORS[0], va="top")
    ax.text(59, 17.4, "16.9", fontsize=7.5, color=COLORS[0], va="bottom", ha="right")
    ax.plot(45, -22.5, "o", color=COLORS[2], ms=3.5)
    ax.text(45, -21.0, "−22.5", fontsize=7.5, color=COLORS[2], ha="center", va="bottom")
    ax.plot(30, -19.5, "o", color=COLORS[2], ms=3.5)
    ax.text(28.5, -21.0, "−19.5", fontsize=7.5, color=COLORS[2], ha="right", va="top")
    ax.set_xlim(0, 90)
    ax.set_ylim(-25, 25)
    ax.set_xticks([0, 15, 30, 45, 60, 75, 90])
    ax.set_xlabel(r"fibre angle $\theta$ (°)")
    ax.set_ylabel("expansion coefficient (ppm/K)")
    ax.legend(loc="upper left", fontsize=8, bbox_to_anchor=(0.0, 0.84))
    ax.text(2, -24, r"T300/epoxy: $\alpha_1$ = 0.02, $\alpha_2$ = 22.5 ppm/K", fontsize=7.5, color="0.3")

    # inset: free thermal distortion of a 30° ply
    axi.set_aspect("equal")
    axi.axis("off")
    axi.set_xlim(-1.75, 1.75)
    axi.set_ylim(-3.05, 1.9)
    sq = np.array([[-1, -1], [1, -1], [1, 1], [-1, 1]], float)
    th = np.radians(30)
    cc, ss = np.cos(th), np.sin(th)
    exx, eyy, gxy = a1 * cc ** 2 + a2 * ss ** 2, a1 * ss ** 2 + a2 * cc ** 2, 2 * (a1 - a2) * ss * cc
    k = 0.008  # exaggeration: strain = k * alpha (ppm/K)
    F = np.eye(2) + k * np.array([[exx, gxy / 2], [gxy / 2, eyy]])
    def_ = sq @ F.T
    p0 = Polygon(sq * 0.8, closed=True, fill=False, ec="0.4", ls="--", lw=1.0, zorder=5)
    axi.add_patch(p0)
    p1 = Polygon(def_ * 0.8, closed=True, fc="#F3E9C6", ec=COLORS[1], lw=1.4, alpha=0.9)
    axi.add_patch(p1)
    dvec, nvec = np.array([cc, ss]), np.array([-ss, cc])
    for s_ in np.arange(-2, 2.01, 0.22):
        a, b = s_ * nvec - 3 * dvec, s_ * nvec + 3 * dvec
        pts = np.array([a, b]) @ F.T * 0.8
        ln, = axi.plot(pts[:, 0], pts[:, 1], color="#8A7A50", lw=0.5)
        ln.set_clip_path(p1)
    axi.annotate("", xy=1.25 * dvec, xytext=-0.0 * dvec, arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.2, mutation_scale=8))
    axi.text(*(1.42 * dvec), "1", color=COLORS[0], fontsize=9, fontweight="bold", ha="center", va="center")
    axi.annotate("", xy=1.15 * nvec, xytext=0 * nvec, arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.2, mutation_scale=8))
    axi.text(*(1.32 * nvec), "2", color=COLORS[0], fontsize=9, fontweight="bold", ha="center", va="center")
    axi.text(0, 1.55, "30° ply heated by $\\Delta T$\n(free, exaggerated)", ha="center", fontsize=7.8)
    axi.text(0, -1.3, "dashed: before heating;\nexpands mostly across\nthe fibres, and shears", ha="center", va="top", fontsize=7.6)
    axi.text(0, -3.05, r"moisture: replace $\alpha$ by $\beta$, $\Delta T$ by $\Delta M$" "\n" r"($\beta_2\approx0.6$)",
             ha="center", va="bottom", fontsize=7.4, color="0.3")
    save(fig, "22", "fig-22-6-ply-thermal-expansion")


if __name__ == "__main__":
    composite_architectures()
    micromechanics_moduli()
    shear_lag_critical_length()
    lamina_axes()
    off_axis_moduli()
    ply_thermal_expansion()
