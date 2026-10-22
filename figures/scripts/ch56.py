"""Figures for Chapter 56 — Computational Materials Science: Simulation Across Scales.

Run from the repository root:  python figures/scripts/ch56.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyBboxPatch, Polygon
from matplotlib.transforms import Affine2D
from scipy import ndimage
from scipy.optimize import brentq
from scipy.spatial import cKDTree

KB = 8.617e-5


# ---------------------------------------------------------------- Figure 56.1
def length_time_scales():
    fig = plt.figure(figsize=(6.8, 4.8))
    ax = fig.add_axes([0.10, 0.11, 0.80, 0.86])
    cx = fig.add_axes([0.915, 0.11, 0.035, 0.86])
    regions = [
        # name, (logL0, logL1), (logt0, logt1), colour, label position, label kw
        ("continuum FEM", (-3, 1), (0, 8.5), "#999999", (-1.0, 7.6), {}),
        ("crystal-plasticity\nFEM", (-6, -2), (0, 7.5), COLORS[3], (-4.6, 6.4), {}),
        ("phase-field", (-8, -3), (-6, 5), COLORS[2], (-4.6, 3.3), {}),
        ("kinetic Monte Carlo", (-9, -6), (-12, 4), COLORS[4], (-7.5, 2.4), {}),
        ("discrete dislocation\ndynamics", (-7, -4.3), (-9, -3), COLORS[1], (-5.65, -7.4), {}),
        ("classical MD", (-9, -7), (-15, -6), COLORS[0], (-8.0, -7.6), {}),
        ("DFT", (-10, -8.7), (-15, -11), COLORS[7], (-9.35, -11.6), {}),
    ]
    for name, (l0, l1), (t0, t1), c, (lx, ly), kw in regions:
        ax.add_patch(Rectangle((l0, t0), l1 - l0, t1 - t0, fc=c, ec=c, alpha=0.18, lw=1.2))
        ax.add_patch(Rectangle((l0, t0), l1 - l0, t1 - t0, fc="none", ec=c, lw=1.2))
        ax.text(lx, ly, name, ha="center", va="center", fontsize=8.3, color=c if c != "#999999" else "0.3",
                fontweight="bold")
    ax.add_patch(Rectangle((-9.75, -14.6), 0.85, 3.2, fc="none", ec=INK, lw=0.8, hatch="////", alpha=0.6))
    ax.annotate("ab-initio MD", xy=(-9.3, -13.2), xytext=(-8.5, -14.3), fontsize=7.8, va="center",
                arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
    # ICME arrow through the empty lower-right corner
    ax.annotate("", xy=(0.6, -1.5), xytext=(-6.6, -14.3),
                arrowprops=dict(arrowstyle="<|-|>", lw=1.5, color=INK, mutation_scale=13))
    ang = np.degrees(np.arctan2((-1.5 + 14.3) * 0.86 * 4.8 / 24, (0.6 + 6.6) * 0.80 * 6.8 / 11))
    ax.text(-2.75, -8.6, "ICME: information passed upward,\nvalidation passed downward",
            rotation=ang, ha="center", va="center", fontsize=8.3)
    ax.set_xlim(-10, 1)
    ax.set_ylim(-15, 9)
    ax.set_xticks(range(-10, 2))
    ax.set_xticklabels([f"10$^{{{k}}}$" for k in range(-10, 2)], fontsize=8.5)
    ax.set_yticks(range(-15, 10, 3))
    ax.set_yticklabels([f"10$^{{{k}}}$" for k in range(-15, 10, 3)], fontsize=8.5)
    ax.set_xlabel("length scale (m)")
    ax.set_ylabel("time scale (s)")
    # reference marks
    for lt, lab in [(np.log10(3.15e7), "1 year"), (np.log10(3600), "1 hour"), (-12, "1 ps")]:
        ax.axhline(lt, color="0.85", lw=0.6, ls=":", zorder=0)
        ax.text(0.95, lt + 0.15, lab, fontsize=7, color="0.5", ha="right", va="bottom")
    # CALPHAD band
    cx.set_xlim(0, 1); cx.set_ylim(-15, 9)
    cx.add_patch(Rectangle((0, -15), 1, 24, fc=COLORS[5], alpha=0.35, ec=COLORS[5]))
    cx.text(0.5, -3, "CALPHAD — thermodynamics: all scales (equilibrium, no length or time)",
            rotation=90, ha="center", va="center", fontsize=8, color="#1F5F8B")
    cx.axis("off")
    save(fig, "56", "fig-56-1-length-time-scales")


# ---------------------------------------------------------------- Figure 56.2
def kmc_residence_time():
    fig, ax = schematic(6.8, 5.0, xlim=(0, 13.6), ylim=(0, 10))
    ax.text(0.1, 9.85, "(a) vacancy and its possible jumps", fontsize=9.5, va="top")
    # lattice
    ox, oy, s = 0.7, 5.3, 0.9
    for i in range(5):
        for j in range(5):
            x, y = ox + i * s, oy + j * s
            if (i, j) == (2, 2):
                ax.add_patch(Circle((x, y), 0.3, fc="white", ec=INK, lw=1.0, ls="--"))
            elif (i, j) == (3, 2):
                ax.add_patch(Circle((x, y), 0.3, fc=COLORS[4], ec=INK, lw=0.6))
            else:
                ax.add_patch(Circle((x, y), 0.3, fc="#B8C4D0", ec=INK, lw=0.5))
    vx, vy = ox + 2 * s, oy + 2 * s
    for (di, dj), lab in [((-1, 0), "$r_1$"), ((1, 0), "$r_2$"), ((0, 1), "$r_3$"), ((0, -1), "$r_4$")]:
        x0, y0 = vx + di * s, vy + dj * s
        ax.annotate("", xy=(vx + di * 0.32, vy + dj * 0.32), xytext=(x0 - di * 0.3, y0 - dj * 0.3),
                    arrowprops=dict(arrowstyle="-|>", lw=1.3, color=COLORS[1], mutation_scale=9))
    ax.text(vx, vy - 0.02, "V", ha="center", va="center", fontsize=8)
    ax.text(ox + 4 * s + 0.45, vy, "solute\nneighbour", fontsize=7.5, va="center", color="#9A6A00")
    # energy profile
    ex0, ex1, ey0 = 0.4, 5.6, 1.2
    xs = np.linspace(0, 3, 400)
    E = 0.70 * (1 - np.cos(2 * np.pi * xs)) / 2
    E[xs > 2] = (0.55 * (1 - np.cos(2 * np.pi * xs)) / 2)[xs > 2]     # solute-assisted lower barrier
    sx = ex0 + (ex1 - ex0) * xs / 3
    sy = ey0 + E / 0.70 * 2.2
    ax.plot(sx, sy, color=INK, lw=1.4)
    ax.plot([ex0, ex1], [ey0, ey0], color="0.6", lw=0.6)
    ax.annotate("", xy=(ex0 - 0.05, ey0 + 2.9), xytext=(ex0 - 0.05, ey0 - 0.1),
                arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK, mutation_scale=7))
    ax.text(ex0 - 0.15, ey0 + 1.5, "E", fontsize=8.5, ha="right", va="center")
    ax.text((ex0 + ex1) / 2, ey0 - 0.15, "reaction coordinate (lattice sites at minima)", ha="center",
            va="top", fontsize=7.8)
    xsad = ex0 + (ex1 - ex0) * 1.5 / 3
    ax.annotate("", xy=(xsad, ey0 + 2.2), xytext=(xsad, ey0),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, color=COLORS[1], mutation_scale=7))
    ax.text(xsad + 0.1, ey0 + 1.05, "$E_a$ = 0.70 eV", fontsize=8, color=COLORS[1], bbox=dict(fc="white", ec="none", pad=0.5))
    ax.text(ex0 + (ex1 - ex0) * 2.5 / 3, ey0 + 1.95, "solute jump:\nlower barrier", fontsize=7.3,
            ha="center", color="#9A6A00")
    ax.text(ex0 + 0.05, ey0 + 2.75, "ν = 10$^{13}$ s$^{-1}$,  $r_i=\\nu\\,\\exp(-E_{a,i}/k_BT)$",
            fontsize=8, va="bottom")

    # (b) residence-time selection
    ax.text(6.9, 9.85, "(b) residence-time event selection", fontsize=9.5, va="top")
    bx0, by, bh = 7.1, 7.6, 0.7
    widths = [1.15, 2.9, 1.15, 1.15]   # r2 (solute neighbour) is larger
    cols = ["#9DC3E6", COLORS[4], "#9DC3E6", "#9DC3E6"]
    x = bx0
    for k, (w, c) in enumerate(zip(widths, cols)):
        ax.add_patch(Rectangle((x, by), w, bh, fc=c, ec=INK, lw=0.8))
        ax.text(x + w / 2, by + bh / 2, f"$r_{k + 1}$", ha="center", va="center", fontsize=9)
        x += w
    R = sum(widths)
    ax.annotate("", xy=(bx0, by - 0.35), xytext=(bx0 + R, by - 0.35),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, color=INK, mutation_scale=7))
    ax.text(bx0 + R / 2, by - 0.42, "$R=\\sum_i r_i$", ha="center", va="top", fontsize=8.5)
    xsel = bx0 + 2.6
    ax.annotate("", xy=(xsel, by + bh), xytext=(xsel, by + bh + 0.85),
                arrowprops=dict(arrowstyle="-|>", lw=1.3, color=COLORS[1], mutation_scale=10))
    ax.text(xsel, by + bh + 0.9, "$u_1R$ selects event 2", ha="center", va="bottom", fontsize=8.3,
            color=COLORS[1])
    ax.text(bx0, 6.0, "then advance the clock:", fontsize=8.5, va="center")
    ax.text(bx0 + 3.2, 5.35, "$\\Delta t=-\\ln(u_2)/R$", fontsize=11, ha="center", va="center")
    ax.text(bx0, 4.7, "$u_1, u_2$: uniform random numbers in (0, 1]", fontsize=7.8, va="center",
            color="0.35")

    # (c) table
    ax.text(6.9, 3.75, "(c) Cu vacancy, 12 neighbours, $E_a$ = 0.70 eV", fontsize=9.5, va="top")
    rows = [("T (K)", "R (s$^{-1}$)", "Δt = 1/R")]
    for T in (300, 600, 900):
        Rt = 12 * 1e13 * np.exp(-0.70 / (KB * T))
        dt = 1 / Rt
        if dt > 1e-3:
            sdt = f"{dt * 1e3:.1f} ms"
        elif dt > 1e-9:
            sdt = f"{dt * 1e9:.1f} ns"
        else:
            sdt = f"{dt * 1e12:.0f} ps"
        mant, ex = f"{Rt:.2e}".split("e")
        rows.append((f"{T}", f"{float(mant):.2f}×10$^{{{int(ex)}}}$", sdt))
    xcols = [7.7, 9.9, 12.3]
    ytop = 3.05
    for r_i, row in enumerate(rows):
        y = ytop - r_i * 0.62
        for xc_, cell in zip(xcols, row):
            ax.text(xc_, y, cell, ha="center", va="center", fontsize=8.5,
                    fontweight="bold" if r_i == 0 else "normal")
    ax.plot([7.0, 13.3], [ytop - 0.31, ytop - 0.31], color=INK, lw=0.8)
    ax.plot([7.0, 13.3], [ytop + 0.31, ytop + 0.31], color=INK, lw=0.8)
    ax.plot([7.0, 13.3], [ytop - 3 * 0.62 - 0.31] * 2, color=INK, lw=0.8)
    save(fig, "56", "fig-56-2-kmc-residence-time")


# ---------------------------------------------------------------- Figure 56.3
def _arm_mask(X, Y, ox, oy, dx, dy, length, halfw, rtip):
    along = (X - ox) * dx + (Y - oy) * dy
    perp = np.abs(-(X - ox) * dy + (Y - oy) * dx)
    w = np.minimum(halfw, np.sqrt(np.clip(2 * rtip * (length - along), 0, None)))
    return (along >= -halfw) & (along <= length) & (perp <= w)


def _dendrite(n=400, L=200.0, seed=3):
    rng = np.random.default_rng(seed)
    xs = np.linspace(0, L, n)
    X, Y = np.meshgrid(xs, xs)
    cx = cy = L / 2
    solid = np.zeros_like(X, dtype=bool)
    for ang in (0, 90, 180, 270):
        a = np.radians(ang + 2.0)
        dx, dy = np.cos(a), np.sin(a)
        Lp = 88 + rng.uniform(-3, 3)
        solid |= _arm_mask(X, Y, cx, cy, dx, dy, Lp, 4.0, 2.5)
        lam2 = 9.0
        s = 10.0
        while s < Lp - 12:
            for side in (-1, 1):
                ls = min(0.55 * (Lp - s - 8), 36) * rng.uniform(0.75, 1.1)
                if ls < 3:
                    continue
                ox = cx + dx * s
                oy = cy + dy * s
                sdx, sdy = -dy * side, dx * side
                # keep secondaries out of the neighbouring quadrant's primary
                ls = min(ls, s * 0.95)
                solid |= _arm_mask(X, Y, ox, oy, sdx, sdy, ls, 2.0, 1.4)
            s += lam2 * rng.uniform(0.85, 1.15)
    solid |= (X - cx) ** 2 + (Y - cy) ** 2 < 6 ** 2
    h = L / (n - 1)
    d_out = ndimage.distance_transform_edt(~solid) * h
    d_in = ndimage.distance_transform_edt(solid) * h
    c = np.where(solid, 2.0 + 0.7 * np.exp(-d_in / 1.5),
                 4.0 + 4.0 * np.exp(-d_out / 7.0))
    # extra enrichment where liquid is enclosed between arms
    crowd = ndimage.uniform_filter(solid.astype(float), size=int(14 / h))
    c = np.where(solid, c, c + 1.5 * crowd * np.exp(-d_out / 10))
    c = ndimage.gaussian_filter(c, 0.8)
    return xs, np.clip(c, 2, 8), solid


def phase_field():
    fig = plt.figure(figsize=(6.8, 3.5))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.15, 1], wspace=0.55)
    ax = fig.add_subplot(gs[0])
    x = np.linspace(-5, 5, 500)
    phi = 0.5 * (1 - np.tanh(x))
    k = 0.2
    lD = 1.5
    cl = 1 + (1 - k) / k * np.exp(-np.clip(x - 1.0, 0, None) / lD)    # liquid ahead of interface (c/c0)
    cl_int = 1 / k
    c = phi * 1.0 + (1 - phi) * cl
    ax.plot(x, phi, color=COLORS[0], lw=2.0)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-0.05, 1.12)
    ax.set_xlabel("distance $x/\\delta$")
    ax.set_ylabel("order parameter φ", color=COLORS[0])
    ax.tick_params(axis="y", colors=COLORS[0])
    ax.text(-4.8, 1.03, "solid φ = 1", fontsize=8.5, color=COLORS[0])
    ax.text(2.0, 0.03, "liquid φ = 0", fontsize=8.5, color=COLORS[0])
    ax.annotate("", xy=(-1, 0.93), xytext=(1, 0.93),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, color=INK, mutation_scale=7))
    ax.axvline(-1, color="0.75", lw=0.6, ls=":")
    ax.axvline(1, color="0.75", lw=0.6, ls=":")
    ax.text(0, 0.95, "2δ", fontsize=8.5, ha="center", va="bottom")

    ax.set_title("(a) diffuse interface: φ = ½[1 − tanh(x/δ)]", fontsize=9.5, loc="left")
    tx = ax.twinx()
    tx.spines["right"].set_visible(True)
    tx.plot(x, c, color=COLORS[1], lw=1.6, ls="--")
    tx.set_ylim(0, 5.6)
    tx.set_ylabel("composition $c/c_0$", color=COLORS[1])
    tx.tick_params(axis="y", colors=COLORS[1])
    tx.text(0.25, 5.05, "solute pile-up\n$c_L \\rightarrow c_0/k$ (k = 0.2)", fontsize=8, color=COLORS[1])

    bx = fig.add_subplot(gs[1])
    xs, c, solid = _dendrite()
    im = bx.imshow(c, origin="lower", extent=[0, 200, 0, 200], cmap="viridis", vmin=2, vmax=8,
                   interpolation="bilinear")
    bx.set_xticks([]); bx.set_yticks([])
    for sp in bx.spines.values():
        sp.set_visible(True)
    bx.add_patch(Rectangle((140, 8), 50, 4, fc="white", ec="none"))
    bx.text(165, 15, "50 μm", color="white", ha="center", va="bottom", fontsize=8.5)
    bx.set_title("(b) Al–Cu dendrite, 200 × 200 μm", fontsize=10, loc="left")
    bx.text(103, 175, "primary arm", color="white", fontsize=7.5, ha="left")
    bx.annotate("secondary\narms", xy=(68, 78), xytext=(10, 25), color="white", fontsize=7.5,
                arrowprops=dict(arrowstyle="-", color="white", lw=0.7))
    cb = fig.colorbar(im, ax=bx, fraction=0.046, pad=0.03)
    cb.set_label("Cu (wt%)", fontsize=9)
    save(fig, "56", "fig-56-3-phase-field")


# ---------------------------------------------------------------- Figure 56.4
def _voronoi_rve(n=44, ngr=100, seed=7):
    rng = np.random.default_rng(seed)
    seeds = rng.random((ngr, 3))
    g = (np.arange(n) + 0.5) / n
    X, Y, Z = np.meshgrid(g, g, g, indexing="ij")
    _, lab = cKDTree(seeds).query(np.c_[X.ravel(), Y.ravel(), Z.ravel()])
    lab = lab.reshape(n, n, n)
    # orientation: angle theta between c-axis and load axis x, azimuth phi in the basal plane
    cvec = rng.normal(size=(ngr, 3))
    cvec /= np.linalg.norm(cvec, axis=1)[:, None]
    theta = np.degrees(np.arccos(np.abs(cvec[:, 0])))
    phi = rng.uniform(0, 30, ngr)
    t = theta / 90
    rgb = np.c_[1 - t, t * (1 - phi / 30), t * (phi / 30)]
    rgb = rgb / rgb.max(axis=1)[:, None]
    rgb = 0.25 + 0.75 * rgb
    return lab, theta, rgb, rng


def _faces(field):
    """Return front (x,z at y=0), right (y,z at x=max) and top (x,y at z=max) slices."""
    front = field[:, 0, :].swapaxes(0, 1)       # rows z, cols x
    right = field[-1, :, :].swapaxes(0, 1)      # rows z, cols y
    top = field[:, :, -1].swapaxes(0, 1)        # rows y, cols x
    return front, right, top


def _draw_cube(ax, faces_rgb, ox=0.0, oy=0.0, depth=0.55):
    cs, sn = depth * np.cos(np.radians(35)), depth * np.sin(np.radians(35))
    mats = [
        Affine2D(np.array([[1, 0, ox], [0, 1, oy], [0, 0, 1]])),
        Affine2D(np.array([[cs, 0, ox + 1], [sn, 1, oy], [0, 0, 1]])),
        Affine2D(np.array([[1, cs, ox], [0, sn, oy + 1], [0, 0, 1]])),
    ]
    for img, m in zip(faces_rgb, mats):
        ax.imshow(img, origin="lower", extent=[0, 1, 0, 1], interpolation="nearest",
                  transform=m + ax.transData)
    # outline
    P = lambda x, y, z: (ox + x + cs * y, oy + z + sn * y)
    edges = [((0, 0, 0), (1, 0, 0)), ((1, 0, 0), (1, 0, 1)), ((1, 0, 1), (0, 0, 1)), ((0, 0, 1), (0, 0, 0)),
             ((1, 0, 0), (1, 1, 0)), ((1, 1, 0), (1, 1, 1)), ((1, 1, 1), (1, 0, 1)),
             ((0, 0, 1), (0, 1, 1)), ((0, 1, 1), (1, 1, 1))]
    for a, b in edges:
        (x0, y0), (x1, y1) = P(*a), P(*b)
        ax.plot([x0, x1], [y0, y1], color=INK, lw=0.8)
    return P


def _with_boundaries(lab2d, img):
    b = np.zeros(lab2d.shape, bool)
    b[:-1, :] |= lab2d[:-1, :] != lab2d[1:, :]
    b[:, :-1] |= lab2d[:, :-1] != lab2d[:, 1:]
    out = img.copy()
    out[b] = out[b] * 0.55
    return out


def cpfem_polycrystal():
    lab, theta, rgb, rng = _voronoi_rve()
    n = lab.shape[0]
    # grain-level von Mises stress at 5 % strain (CP-Ti-like): hard grains = c-axis near load axis
    sig_g = 255 + 135 * np.cos(np.radians(theta)) ** 4 + rng.normal(0, 12, theta.size)
    S = sig_g[lab]
    Smin = ndimage.minimum_filter(S, size=5)
    S = S + 0.75 * (S - Smin)                       # hot spots on hard-grain boundaries
    S = ndimage.gaussian_filter(S, 0.8)
    S = np.clip(S, 150, 450)

    fig = plt.figure(figsize=(6.8, 3.3))
    axa = fig.add_axes([0.0, 0.08, 0.33, 0.84])
    axb = fig.add_axes([0.33, 0.08, 0.33, 0.84])
    cax = fig.add_axes([0.375, 0.10, 0.22, 0.035])
    axc = fig.add_axes([0.77, 0.24, 0.215, 0.58])
    lf, lr, lt = _faces(lab)
    cmap = plt.get_cmap("inferno")
    norm = plt.Normalize(150, 450)
    for ax, mode in [(axa, "ipf"), (axb, "stress")]:
        ax.set_xlim(-0.35, 1.75); ax.set_ylim(-0.25, 1.65); ax.set_aspect("equal"); ax.axis("off")
        if mode == "ipf":
            imgs = [_with_boundaries(l2, rgb[l2]) for l2 in (lf, lr, lt)]
        else:
            sf, sr, st = _faces(S)
            imgs = [_with_boundaries(l2, cmap(norm(s2))[..., :3]) for l2, s2 in zip((lf, lr, lt), (sf, sr, st))]
        P = _draw_cube(ax, imgs, ox=0.0, oy=0.0)
        # load arrows along x
        for yy in (0.25, 0.75):
            ax.annotate("", xy=(-0.33, yy), xytext=(-0.04, yy),
                        arrowprops=dict(arrowstyle="-|>", lw=1.4, color=COLORS[0], mutation_scale=10))
        for yy in (0.45, 0.95):
            x0, y0 = P(1, 0.5, yy)
            ax.annotate("", xy=(x0 + 0.33, y0), xytext=(x0 + 0.04, y0),
                        arrowprops=dict(arrowstyle="-|>", lw=1.4, color=COLORS[0], mutation_scale=10))
    axa.set_title("(a) ~100 grains, IPF colours", fontsize=9.5)
    axb.set_title("(b) von Mises stress at 5 % strain", fontsize=9.5)
    axa.text(0.1, -0.12, "red: c-axis ∥ load (x)", fontsize=7, color="0.3")
    cb = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), cax=cax, orientation="horizontal")
    cb.set_ticks([150, 300, 450])
    cb.ax.tick_params(labelsize=7.5)
    cb.set_label("σ$_{vM}$ (MPa)", fontsize=8, labelpad=1)
    # label a hard and a soft grain on the front face of (b)
    areas = np.bincount(lf.ravel(), minlength=theta.size)
    cand = np.where(areas > 0.012 * lf.size)[0]
    hard = cand[np.argmin(theta[cand])]
    soft = cand[np.argmax(theta[cand])]
    for gidx, txt, off in [(hard, "hard", (-0.05, 0.35)), (soft, "soft", (0.05, -0.32))]:
        zz, xx = np.nonzero(lf == gidx)
        px, py = (xx.mean() + 0.5) / n, (zz.mean() + 0.5) / n
        axb.annotate(txt, xy=(px, py), xytext=(px + off[0], py + off[1]), fontsize=8.5,
                     color="white" if txt == "soft" else INK, fontweight="bold", ha="center",
                     bbox=dict(boxstyle="round,pad=0.15", fc="black" if txt == "soft" else "white",
                               ec="none", alpha=0.75),
                     arrowprops=dict(arrowstyle="-", color="white", lw=1.0))
    # (c) macroscopic curve
    e = np.linspace(0, 0.05, 200)
    E = 105e3
    sig = np.minimum(E * e, 300 + 120 * (1 - np.exp(-np.clip(e - 300 / E, 0, None) / 0.015)))
    sig = np.where(E * e < 300, E * e, 300 + 120 * (1 - np.exp(-(e - 300 / E) / 0.015)))
    axc.plot(e * 100, sig, color=COLORS[1], lw=1.6, label="CPFEM")
    ee = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]) / 100
    se = np.where(E * ee < 300, E * ee, 300 + 125 * (1 - np.exp(-(ee - 300 / E) / 0.014)))
    se = se + np.array([6, -5, 4, -6, 5, -3, 6, -4, 3, -5])
    axc.plot(ee * 100, se, "o", color=INK, ms=3.5, mfc="white", label="experiment")
    axc.set_xlim(0, 5); axc.set_ylim(0, 500)
    axc.set_xlabel("strain (%)", fontsize=8.5)
    axc.set_ylabel("stress (MPa)", fontsize=8.5)
    axc.tick_params(labelsize=7.5)
    axc.legend(fontsize=7.3, loc="lower right")
    axc.set_title("(c) macroscopic", fontsize=9.5)
    save(fig, "56", "fig-56-4-cpfem-polycrystal")


# ---------------------------------------------------------------- Figure 56.5
def regular_solution():
    R, W = 8.314, 20000.0
    Tc = W / (2 * R)
    x = np.linspace(1e-4, 1 - 1e-4, 2000)

    def G(x, T):
        return W * x * (1 - x) + R * T * (x * np.log(x) + (1 - x) * np.log(1 - x))

    def binodal(T):
        return brentq(lambda z: np.log(z / (1 - z)) - W * (2 * z - 1) / (R * T), 1e-9, 0.4999)

    fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.8, 3.7))
    temps = [(800, COLORS[0]), (1000, COLORS[1]), (Tc, COLORS[2]), (1400, COLORS[3])]
    for T, c in temps:
        lab = f"{T:,.0f} K" + (" ($T_c$)" if abs(T - Tc) < 1 else "")
        ax.plot(x, G(x, T), color=c, lw=1.6, label=lab)
    xb = binodal(1000)
    xs = 0.5 * (1 - np.sqrt(1 - 2 * R * 1000 / W))
    Gb = G(xb, 1000)
    ax.plot([0.02, 0.98], [Gb, Gb], color=INK, lw=0.9, ls="--")
    ax.plot([xb, 1 - xb], [Gb, Gb], "o", color=INK, ms=4.5)
    ax.plot([xs, 1 - xs], [G(xs, 1000)] * 2, "D", color=COLORS[1], ms=4.5, mfc="white")
    ax.annotate(f"common tangent\nx = {xb:.3f}, {1 - xb:.3f}", xy=(1 - xb, Gb), xytext=(0.62, -2350),
                fontsize=7.8, ha="center", arrowprops=dict(arrowstyle="-", lw=0.6))
    ax.annotate(f"inflections\n{xs:.3f}, {1 - xs:.3f}", xy=(xs, G(xs, 1000)), xytext=(0.25, 330),
                fontsize=7.8, ha="center", color=COLORS[1],
                arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[1]))
    ax.axhline(0, color="0.7", lw=0.6)
    ax.set_xlim(0, 1)
    ax.set_ylim(-3200, 600)
    ax.set_xlabel("mole fraction x of B")
    ax.set_ylabel("ΔG$_{mix}$ (J/mol)")
    ax.legend(fontsize=7.8, loc="lower left", ncol=1)
    ax.set_title("(a) Ω = 20 kJ/mol", fontsize=10, loc="left")

    Ts = np.linspace(600, Tc - 0.01, 300)
    xbs = np.array([binodal(T) for T in Ts])
    xsp = 0.5 * (1 - np.sqrt(1 - 2 * R * Ts / W))
    bx.fill_betweenx(Ts, xsp, 1 - xsp, color=COLORS[3], alpha=0.15, lw=0)
    bx.fill_betweenx(Ts, xbs, xsp, color=COLORS[0], alpha=0.12, lw=0)
    bx.fill_betweenx(Ts, 1 - xsp, 1 - xbs, color=COLORS[0], alpha=0.12, lw=0)
    bx.plot(np.r_[xbs, 1 - xbs[::-1]], np.r_[Ts, Ts[::-1]], color=INK, lw=1.8, label="binodal")
    bx.plot(np.r_[xsp, 1 - xsp[::-1]], np.r_[Ts, Ts[::-1]], color=INK, lw=1.4, ls="--", label="spinodal")
    bx.plot([xb, 1 - xb], [1000, 1000], color=COLORS[1], lw=1.2)
    bx.plot([xb, 1 - xb], [1000, 1000], "o", color=COLORS[1], ms=4)
    bx.text(0.5, 1012, "tie-line at 1,000 K", ha="center", va="bottom", fontsize=7.8, color=COLORS[1])
    bx.plot(0.5, Tc, "o", color=INK, ms=4)
    bx.text(0.54, Tc + 8, f"$T_c$ = {Tc:,.0f} K", ha="left", va="bottom", fontsize=8.5)
    bx.text(0.5, 1262, "single phase", ha="center", fontsize=8.5)
    bx.text(0.5, 760, "spinodal\ndecomposition", ha="center", fontsize=8.3, color="#8A3F70")
    bx.text(0.10, 720, "nucleation\nand growth", ha="center", fontsize=7.8, color=COLORS[0],
            rotation=90, va="center")
    bx.text(0.90, 720, "nucleation\nand growth", ha="center", fontsize=7.8, color=COLORS[0],
            rotation=90, va="center")
    bx.set_xlim(0, 1)
    bx.set_ylim(600, 1300)
    bx.set_xlabel("mole fraction x of B")
    bx.set_ylabel("temperature (K)")
    bx.legend(fontsize=7.8, loc="lower center", ncol=2, bbox_to_anchor=(0.5, -0.01))
    bx.set_title("(b) miscibility gap", fontsize=10, loc="left")
    fig.tight_layout(w_pad=1.2)
    save(fig, "56", "fig-56-5-regular-solution")


# ---------------------------------------------------------------- Figure 56.6
def icme_chain():
    fig, ax = schematic(6.8, 4.8, xlim=(0, 17), ylim=(0, 12))
    heads = ["Process", "Microstructure", "Properties", "Performance"]
    hc = ["#E3EEF8", "#E6F2EC", "#F7EEDF", "#F3E6EF"]
    cw, gap, x0 = 3.75, 0.45, 0.3
    xs = [x0 + i * (cw + gap) for i in range(4)]
    # validation band (top)
    box(ax, 0.3, 10.9, 16.4, 0.85,
        "validation: experiments at each link (DSC, SEM, micropillar, creep tests)", fc="#FFF7D6",
        fontsize=8.3)
    for i, h in enumerate(heads):
        ax.text(xs[i] + cw / 2, 10.25, h, ha="center", va="center", fontsize=9.5, fontweight="bold")
        ax.plot([xs[i] + cw / 2] * 2, [10.55, 10.88], color="0.6", lw=0.8, ls=":")
    boxes = {
        "forge": (0, 7.6, "forging FEM\n(T, strain,\nstrain rate)"),
        "ht": (0, 4.9, "heat-treatment\nthermal model"),
        "calphad": (1, 4.9, "CALPHAD +\nprecipitation model:\nγ′ size and fraction"),
        "pf": (1, 7.6, "phase-field /\ngrain growth:\ngrain size"),
        "cp": (2, 4.9, "crystal plasticity +\nDDD-informed\nhardening:\nyield, flow"),
        "fat": (2, 7.6, "fatigue indicator\nfrom grain-scale\nhot spots"),
        "disc": (3, 6.25, "disc FEM:\ncreep, LCF life,\nburst margin"),
    }
    bh = 2.2
    pos = {}
    for k, (col, y, txt) in boxes.items():
        bhh = bh if k != "disc" else 2.6
        box(ax, xs[col], y, cw, bhh, txt, fc=hc[col], fontsize=7.9)
        pos[k] = (xs[col], y, cw, bhh)

    def right(k):
        x, y, w, h = pos[k]
        return x + w, y + h / 2

    def left(k):
        x, y, w, h = pos[k]
        return x, y + h / 2

    for a, b in [("forge", "calphad"), ("ht", "pf"), ("calphad", "cp"), ("pf", "fat"),
                 ("cp", "disc"), ("fat", "disc"), ("forge", "pf"), ("ht", "calphad"),
                 ("calphad", "fat"), ("pf", "cp")]:
        (x0_, y0_), (x1_, y1_) = right(a), left(b)
        ax.annotate("", xy=(x1_, y1_), xytext=(x0_, y0_),
                    arrowprops=dict(arrowstyle="-|>", lw=1.0, color=INK, mutation_scale=9,
                                    shrinkA=1, shrinkB=1))
    # design-optimization feedback (dotted) under the boxes
    xd, yd, wd, hd = pos["disc"]
    yb = 4.2
    ax.plot([xd + wd / 2, xd + wd / 2, xs[0] + cw / 2], [yd, yb, yb], color=COLORS[1], lw=1.3, ls=":")
    ax.annotate("", xy=(xs[0] + cw / 2, 4.9), xytext=(xs[0] + cw / 2, yb),
                arrowprops=dict(arrowstyle="-|>", lw=1.3, color=COLORS[1], ls=":", mutation_scale=10))
    ax.text((xs[0] + xs[3] + cw) / 2, yb - 0.12, "design optimization (alloy, process, geometry)",
            ha="center", va="top", fontsize=8.3, color=COLORS[1])
    # lower band: DFT -> potentials -> MD
    box(ax, xs[1] - 0.3, 0.6, xs[2] + cw - xs[1] + 0.6, 1.3,
        "DFT  →  interatomic potentials  →  MD inputs\n(formation energies, mobilities, CRSS, dislocation properties)",
        fc="#ECECEC", fontsize=8.2)
    for k in ("calphad", "cp"):
        x, y, w, h = pos[k]
        xa = x + w * (0.12 if k == "calphad" else 0.88)
        ax.annotate("", xy=(xa, y), xytext=(xa, 1.9),
                    arrowprops=dict(arrowstyle="-|>", lw=1.0, color="0.35", ls="--", mutation_scale=9))
    save(fig, "56", "fig-56-6-icme-chain")


if __name__ == "__main__":
    length_time_scales()
    kmc_residence_time()
    phase_field()
    cpfem_polycrystal()
    regular_solution()
    icme_chain()
