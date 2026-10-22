"""Figures for Chapter 52 — Materials Characterization: The Laboratory Toolkit. Run from the repository root: python figures/scripts/ch52.py"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle, Polygon, Ellipse, FancyBboxPatch  # noqa: E402

BLUE, VERM, GREEN, PINK, ORANGE, SKY = COLORS[:6]


# ---------------------------------------------------------------- Figure 52.1
def technique_map():
    """Log-log map drawn in log10 coordinates so that ellipses stay ellipses."""
    fig, ax = new_fig(6.8, 5.0)
    probe_col = {"photons": ORANGE, "electrons": BLUE, "ions": VERM}
    # name, (lat lo, hi) m, (depth lo, hi) m, probe, detection limit, label position (log x, log y), ha
    T = [
        ("TEM/STEM", (1e-10, 1e-9), (1e-8, 1e-7), "electrons", "single columns", (-9.5, -6.6), "center"),
        ("AES", (1e-8, 5e-8), (2e-9, 5e-9), "electrons", "~0.1 at.%", (-7.65, -8.5), "center"),
        ("EBSD", (2e-8, 1e-7), (1e-8, 5e-8), "electrons", "phase/orientation", (-7.35, -7.0), "center"),
        ("optical\nmicroscopy", (2.5e-7, 1e-6), (1e-8, 1e-7), "photons", "surface", (-6.4, -8.35), "center"),
        ("SEM-EDS", (3e-7, 3e-6), (3e-7, 3e-6), "electrons", "~0.1 wt%", (-7.3, -5.85), "center"),
        ("Raman", (5e-7, 2e-6), (1e-7, 1e-3), "photons", "depth set by\ntransparency", (-5.0, -3.6), "center"),
        ("FTIR-ATR", (1e-5, 5e-5), (5e-7, 2e-6), "photons", "~0.1–1 wt%", (-4.65, -5.25), "center"),
        ("XPS", (1e-5, 1e-3), (3e-9, 1e-8), "photons", "~0.1 at.%", (-4.0, -8.15), "center"),
        ("lab XRD", (1e-4, 1e-2), (1e-6, 1e-4), "photons", "~1 wt% phase", (-3.0, -5.0), "center"),
    ]
    for name, (x0, x1), (y0, y1), pr, dl, (lx, ly), ha in T:
        cx, cy = (np.log10(x0) + np.log10(x1)) / 2, (np.log10(y0) + np.log10(y1)) / 2
        w = max(np.log10(x1) - np.log10(x0), 0.35) + 0.15
        h = max(np.log10(y1) - np.log10(y0), 0.35) + 0.15
        c = probe_col[pr]
        ax.add_patch(Ellipse((cx, cy), w, h, fc=c, alpha=0.22, ec=c, lw=1.3))
        ax.text(lx, ly, f"{name}\n[{dl}]", ha=ha, va="center", fontsize=7.6, color=INK,
                linespacing=1.05)
    # SIMS: static to dynamic (sputter depth profiling)
    cx, cy = (-7 + -4) / 2, (-9 + -5) / 2
    ax.add_patch(Ellipse((cx, cy), 3.4, 4.3, fc="none", ec=VERM, lw=1.5, ls="--"))
    ax.add_patch(Ellipse((cx, cy), 3.4, 4.3, fc=VERM, alpha=0.06, ec="none"))
    ax.text(-5.45, -7.55, "static/dynamic SIMS\n[ppm–ppb]\n(depth by sputtering)", ha="center",
            va="center", fontsize=7.6, color=VERM)
    # bulk bar
    ax.add_patch(Rectangle((-2.45, -3.9), 0.4, 1.85, fc="0.55", ec=INK, lw=0.8, alpha=0.6))
    ax.text(-2.55, -2.95, "thermal analysis,\nmechanical tests:\nwhole specimen", ha="right", va="center",
            fontsize=7.6)
    # leader lines for crowded labels
    leaders = [((-7.65, -8.3), (-7.65, -8.55)), ]
    ax.set_xlim(-10, -2)
    ax.set_ylim(-9, -2)
    xt = np.arange(-10, -1)
    xl = ["0.1 nm", "1 nm", "10 nm", "100 nm", "1 µm", "10 µm", "100 µm", "1 mm", "10 mm"]
    ax.set_xticks(xt)
    ax.set_xticklabels(xl, fontsize=8.5)
    yt = np.arange(-9, -1)
    yl = ["1 nm", "10 nm", "100 nm", "1 µm", "10 µm", "100 µm", "1 mm", "10 mm"]
    ax.set_yticks(yt)
    ax.set_yticklabels(yl, fontsize=8.5)
    ax.set_xlabel("lateral resolution")
    ax.set_ylabel("information depth")
    ax.grid(True, color="#EEEEEE", lw=0.6)
    ax.set_axisbelow(True)
    from matplotlib.lines import Line2D
    hs = [Line2D([], [], marker="o", ls="", ms=9, mfc=c, mec=c, alpha=0.5) for c in probe_col.values()]
    ax.legend(hs, [f"{k} in" for k in probe_col], loc="upper left", fontsize=8, title="probe",
              title_fontsize=8, frameon=True, framealpha=0.9, edgecolor="0.8")
    ax.text(-2.05, -8.9, "[ ] = typical detection limit", ha="right", va="bottom", fontsize=7.5, color="0.35")
    save(fig, "52", "fig-52-1-technique-map")


# ---------------------------------------------------------------- Figure 52.2
def _teardrop(R, p, q, neck=0.02):
    u = np.linspace(0, 1, 200)
    w = u ** p * (1 - u) ** q
    w = w / w.max() * 0.5 * R * 1.0
    w = np.maximum(w, neck)
    return u * R, w


def interaction_volumes():
    fig, ax = schematic(6.8, 4.3, xlim=(-0.6, 11.2), ylim=(-5.4, 1.4))
    specs = [("Al", 4.2, 0.62, 0.45, 2.35, "#9CC3E4"), ("Fe", 1.6, 0.48, 0.5, 6.4, "#F2B48F"),
             ("W", 0.85, 0.32, 0.55, 8.9, "#A9D8B8")]
    for name, R, p, q, xc, col in specs:
        depth, w = _teardrop(R, p, q)
        xs = np.concatenate([xc - w, (xc + w)[::-1]])
        ys = np.concatenate([-depth, (-depth)[::-1]])
        ax.add_patch(Polygon(np.column_stack([xs, ys]), closed=True, fc=col, ec=INK, lw=0.9, alpha=0.55))
        # BSE zone: upper 30 %
        m = depth <= 0.3 * R
        xs2 = np.concatenate([xc - w[m], (xc + w[m])[::-1]])
        ys2 = np.concatenate([-depth[m], (-depth[m])[::-1]])
        ax.add_patch(Polygon(np.column_stack([xs2, ys2]), closed=True, fc=col, ec=INK, lw=0.6, alpha=0.9,
                             hatch="////"))
        # surface
        ax.plot([xc - 1.15 * max(R / 2, 0.55), xc + 1.15 * max(R / 2, 0.55)], [0, 0], color=INK, lw=1.3)
        # SE skin
        wse = w[np.searchsorted(depth, 0.02)] + 0.06
        ax.plot([xc - wse, xc + wse], [0.0, 0.0], color=VERM, lw=3.5, solid_capstyle="butt")
        # beam
        ax.annotate("", xy=(xc, 0.02), xytext=(xc, 1.05), arrowprops=dict(arrowstyle="-|>", lw=1.4, color=INK))
        ax.text(xc + 0.08, 1.05, "20 keV", fontsize=7.5, ha="left", va="top")
        ax.text(xc, -R - 0.15, f"{name}: R = {R} µm", ha="center", va="top", fontsize=9, weight="bold")
        # depth dimension
        xd = xc + 0.5 * R + 0.25
        ax.annotate("", xy=(xd, -R), xytext=(xd, 0), arrowprops=dict(arrowstyle="<|-|>", lw=0.7,
                                                                     mutation_scale=7))
    # labels on Al
    xc, R = 2.35, 4.2
    ax.annotate("secondary electrons:\ntop 1–10 nm (not to scale)", xy=(xc - 0.3, 0.0), xytext=(-0.45, 0.85),
                fontsize=7.5, color=VERM, ha="left", va="center",
                arrowprops=dict(arrowstyle="-", lw=0.7, color=VERM))
    ax.annotate("backscattered\nelectrons\n(upper ~30 %)", xy=(xc - 0.6, -0.8), xytext=(-0.5, -1.6),
                fontsize=7.5, ha="left", va="center", arrowprops=dict(arrowstyle="-", lw=0.7))
    ax.annotate("characteristic\nX-rays (EDS):\nwhole volume", xy=(xc - 0.9, -2.6), xytext=(-0.5, -3.5),
                fontsize=7.5, ha="left", va="center", arrowprops=dict(arrowstyle="-", lw=0.7))
    # scale bar
    ax.plot([9.6, 10.6], [-4.4, -4.4], color=INK, lw=2.5, solid_capstyle="butt")
    ax.text(10.1, -4.5, "1 µm", ha="center", va="top", fontsize=8.5)
    # table
    tx, ty = 4.9, -3.4
    ax.add_patch(Rectangle((tx - 0.3, ty - 1.25), 3.5, 1.45, fc="white", ec="0.5", lw=0.7))
    ax.text(tx + 1.45, ty, "Kanaya–Okayama R (µm)", ha="center", va="center", fontsize=7.5, weight="bold")
    rows = [("", "20 keV", "5 keV"), ("Al", "4.2", "0.42"), ("Fe", "1.6", "0.16"), ("W", "0.85", "0.08")]
    for k, (a, b, c) in enumerate(rows):
        yy = ty - 0.3 - 0.25 * k
        ax.text(tx + 0.35, yy, a, fontsize=7.5, ha="center", va="center")
        ax.text(tx + 1.35, yy, b, fontsize=7.5, ha="center", va="center")
        ax.text(tx + 2.35, yy, c, fontsize=7.5, ha="center", va="center")
    ax.text(5.3, -5.2, "EDS spatial resolution ≈ R, not the beam diameter", ha="center", va="center",
            fontsize=9, style="italic", bbox=dict(fc="#FFF4D6", ec="0.6", lw=0.6, boxstyle="round,pad=0.3"))
    save(fig, "52", "fig-52-2-interaction-volumes")


# ---------------------------------------------------------------- Figure 52.3
def _ipf_color(b):
    """b: barycentric weights (w001, w101, w111) -> RGB (red, green, blue)."""
    c = np.asarray(b, float)
    c = c / c.max(axis=-1, keepdims=True)
    return np.clip(c, 0, 1)


def _rand_ipf(rng, n):
    w = rng.dirichlet([1.0, 1.0, 1.0], size=n)
    return _ipf_color(w ** 0.8)


def ebsd_map():
    rng = np.random.default_rng(11)
    nx, ny = 400, 300                     # 0.5 um pixels -> 200 x 150 um
    px = 0.5
    xs = (np.arange(nx) + 0.5) * px
    ys = (np.arange(ny) + 0.5) * px
    X, Y = np.meshgrid(xs, ys)
    # columnar ferrite grains (weld metal), elongated vertically
    ns = 13
    seeds = np.column_stack([rng.uniform(0, 200, ns), rng.uniform(0, 150, ns)])
    sx, sy = 1.0, 0.45  # anisotropic metric -> grains elongated along y
    d = ((X[..., None] - seeds[:, 0]) * sx) ** 2 + ((Y[..., None] - seeds[:, 1]) * sy) ** 2
    order = np.argsort(d, axis=-1)
    lab = order[..., 0]
    d1 = np.sqrt(np.take_along_axis(d, order[..., :1], -1)[..., 0])
    d2 = np.sqrt(np.take_along_axis(d, order[..., 1:2], -1)[..., 0])
    bdist = (d2 - d1) / 2
    lab2 = order[..., 1]
    fcol = _rand_ipf(rng, ns)
    img = fcol[lab]

    # grain-boundary austenite
    gamma = bdist < 1.75
    gam_id = np.minimum(lab, lab2) * 100 + np.maximum(lab, lab2)
    # Widmanstatten plates growing from boundaries
    nplates = 70
    plate = np.zeros_like(gamma)
    bpix = np.argwhere((bdist < 1.0))
    picks = bpix[rng.choice(len(bpix), nplates, replace=False)]
    plate_id = np.full(gamma.shape, -1)
    for k, (iy, ix) in enumerate(picks):
        x0, y0 = xs[ix], ys[iy]
        g = lab[iy, ix]
        ang = rng.choice([0.6, 2.5]) + rng.normal(0, 0.12) + (0 if g % 2 else 0.5)
        L = rng.uniform(12, 30)
        wdt = rng.uniform(1.2, 2.2)
        ux, uy = np.cos(ang), np.sin(ang)
        # direction pointing into grain g
        cx, cy = seeds[g]
        if (cx - x0) * ux + (cy - y0) * uy < 0:
            ux, uy = -ux, -uy
        rx, ry = X - x0, Y - y0
        along = rx * ux + ry * uy
        perp = np.abs(-rx * uy + ry * ux)
        m = (along > 0) & (along < L) & (perp < wdt / 2 * (1 - 0.6 * along / L)) & (lab == g)
        plate |= m
        plate_id[m] = 10000 + k
    gamma_all = gamma | plate
    frac = gamma_all.mean()
    # austenite orientation colours: per boundary segment / plate
    ids = np.where(plate, plate_id, gam_id)
    uniq = np.unique(ids[gamma_all])
    gc = _rand_ipf(rng, len(uniq))
    lut = {u: gc[i] for i, u in enumerate(uniq)}
    for u in uniq:
        img[(ids == u) & gamma_all] = lut[u]

    fig = plt.figure(figsize=(6.8, 4.1))
    gs = fig.add_gridspec(2, 2, width_ratios=[1.55, 1.0], height_ratios=[0.42, 1.0], wspace=0.28, hspace=0.55)
    ax = fig.add_subplot(gs[:, 0])
    ax.imshow(img, extent=(0, 200, 150, 0), interpolation="nearest")
    # ferrite boundaries
    edge = np.zeros_like(lab, bool)
    edge[:, 1:] |= lab[:, 1:] != lab[:, :-1]
    edge[1:, :] |= lab[1:, :] != lab[:-1, :]
    ax.contour(X, Y, gamma_all.astype(float), levels=[0.5], colors="k", linewidths=0.7)
    ax.set_xlim(0, 200)
    ax.set_ylim(150, 0)
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(True)
    # scale bar
    ax.add_patch(Rectangle((135, 138), 50, 4, fc="white", ec="k", lw=0.6))
    ax.text(160, 135, "50 µm", ha="center", va="bottom", fontsize=8, color="white", weight="bold",
            bbox=dict(fc="k", ec="none", alpha=0.45, pad=1))
    # line profile (60 um)
    best = None
    for iy in range(20, 280, 4):
        for ix in range(10, 270, 4):
            row = lab[iy, ix:ix + 121]
            gr = gamma_all[iy, ix:ix + 121]
            if row.size < 121:
                continue
            if (row[:86] == row[0]).all() and (row[92:] == row[-1]).all() and row[0] != row[-1] \
                    and not gr[:84].any() and not gr[95:].any():
                best = (xs[ix], ys[iy])
                break
        if best:
            break
    lx0, ly0 = best if best else (60.0, 40.0)
    ax.annotate("", xy=(lx0 + 60, ly0), xytext=(lx0, ly0),
                arrowprops=dict(arrowstyle="-|>", color="white", lw=2.6, mutation_scale=11))
    ax.annotate("", xy=(lx0 + 60, ly0), xytext=(lx0, ly0),
                arrowprops=dict(arrowstyle="-|>", color="k", lw=1.2, mutation_scale=9))
    ax.text(lx0, ly0 - 4, "A", fontsize=9, weight="bold", color="k", ha="center",
            bbox=dict(fc="white", ec="none", pad=0.5, alpha=0.8))
    ax.text(lx0 + 60, ly0 - 4, "B", fontsize=9, weight="bold", color="k", ha="center",
            bbox=dict(fc="white", ec="none", pad=0.5, alpha=0.8))
    ax.set_title("IPF-Z map, duplex weld metal (black outline = austenite)", fontsize=8.5, pad=3)
    ax.set_xlabel("≈ 200 × 150 µm", fontsize=8)

    # IPF key triangle
    ins = ax.inset_axes([0.0, -0.36, 0.26, 0.28])
    ins.set_xlim(-0.08, 1.08)
    ins.set_ylim(-0.12, 0.98)
    ins.set_aspect("equal")
    ins.axis("off")
    P0, P1, P2 = np.array([0, 0]), np.array([1, 0]), np.array([0.85, 0.8])
    n = 120
    uu, vv = np.meshgrid(np.linspace(0, 1, n), np.linspace(0, 1, n))
    tri = np.zeros((n, n, 4))
    for i in range(n):
        for j in range(n):
            a_, b_ = uu[i, j], vv[i, j]
            if a_ + b_ <= 1:
                c0 = 1 - a_ - b_
                tri[i, j, :3] = _ipf_color(np.array([c0, a_, b_]) ** 0.8)
                tri[i, j, 3] = 1
    # map barycentric to cartesian by rendering as scatter (simple and robust)
    w0 = 1 - uu - vv
    msk = w0 >= 0
    pts = (w0[msk, None] * P0 + uu[msk, None] * P1 + vv[msk, None] * P2)
    ins.scatter(pts[:, 0], pts[:, 1], c=tri[msk][:, :3], s=1.2, marker="s", lw=0)
    ins.plot([0, 1, 0.85, 0], [0, 0, 0.8, 0], color=INK, lw=0.7)
    ins.text(-0.04, -0.03, "001", ha="right", va="top", fontsize=7)
    ins.text(1.04, -0.03, "101", ha="left", va="top", fontsize=7)
    ins.text(0.85, 0.84, "111", ha="center", va="bottom", fontsize=7)

    # phase fraction bar
    a1 = fig.add_subplot(gs[0, 1])
    a1.barh([0], [75], color="#C9C9C9", ec=INK, lw=0.7, height=0.6)
    a1.barh([0], [25], left=[75], color="#F1F1F1", ec=INK, lw=0.7, height=0.6, hatch="///")
    a1.text(37.5, 0, "ferrite (BCC) 75 %", ha="center", va="center", fontsize=8)
    a1.text(87.5, 0, "γ 25 %", ha="center", va="center", fontsize=8)
    a1.set_xlim(0, 100)
    a1.set_ylim(-0.5, 0.5)
    a1.set_yticks([])
    a1.set_xticks([0, 50, 100])
    a1.tick_params(labelsize=7.5)
    a1.set_xlabel("area fraction (%)", fontsize=8, labelpad=1)
    a1.set_title("phase map", fontsize=8.5, pad=2)
    a1.spines["left"].set_visible(False)

    # misorientation profile
    a2 = fig.add_subplot(gs[1, 1])
    dd = np.linspace(0, 60, 241)
    xb = 44.0
    mis = np.where(dd < xb, 3.0 * (dd / xb) ** 1.6, 45.5 + 0.4 * np.sin(dd))
    mis = mis + np.random.default_rng(2).normal(0, 0.12, dd.size) * (dd < xb)
    mis = np.maximum(mis, 0)
    a2.plot(dd, mis, color=BLUE, lw=1.4)
    a2.axhline(15, color=INK, ls="--", lw=0.8)
    a2.text(1, 14, "high-angle boundary threshold (15°)", fontsize=7, va="top")
    a2.set_xlim(0, 60)
    a2.set_ylim(0, 52)
    a2.set_xlabel("distance A → B (µm)", fontsize=8.5)
    a2.set_ylabel("point-to-origin\nmisorientation (°)", fontsize=8.5)
    a2.tick_params(labelsize=7.5)
    a2.annotate("45° step:\ngrain boundary", xy=(xb + 0.3, 30), xytext=(47, 24), fontsize=7, ha="left",
                arrowprops=dict(arrowstyle="-|>", lw=0.7))
    # zoom inset
    z = a2.inset_axes([0.14, 0.42, 0.42, 0.2])
    z.plot(dd[dd < xb], mis[dd < xb], color=BLUE, lw=1.1)
    z.set_xlim(0, xb)
    z.set_ylim(0, 3.6)
    z.set_yticks([0, 3])
    z.tick_params(labelsize=6.5, pad=1)
    z.set_title("zoom: rise to ~3° (plastic strain / KAM)", fontsize=6.3, pad=2, loc="left")
    save(fig, "52", "fig-52-3-ebsd-map")
    return frac


# ---------------------------------------------------------------- Figure 52.4
def _pv(x, x0, fwhm, eta=0.5):
    g = np.exp(-4 * np.log(2) * ((x - x0) / fwhm) ** 2)
    l = 1 / (1 + 4 * ((x - x0) / fwhm) ** 2)
    return eta * l + (1 - eta) * g


def _two_theta(lam, a, hkl):
    d = a / np.sqrt(sum(i * i for i in hkl))
    return 2 * np.degrees(np.arcsin(lam / (2 * d)))


def xrd_duplex():
    fig, ax = new_fig(6.8, 4.0)
    lam = 0.178897
    tt = np.linspace(45, 130, 4000)
    alpha = [((1, 1, 0), 100), ((2, 0, 0), 14), ((2, 1, 1), 30), ((2, 2, 0), 13)]
    gam = [((1, 1, 1), 82), ((2, 0, 0), 38), ((2, 2, 0), 20), ((3, 1, 1), 26)]
    bg = 4 + 2.0 * np.exp(-(tt - 45) / 40)
    y = bg.copy()
    peaks = []
    for hkl, I in alpha:
        p = _two_theta(lam, 0.2866, hkl)
        y += I * _pv(tt, p, 0.25 + 0.003 * (p - 45))
        peaks.append(("α", hkl, p, I, BLUE))
    for hkl, I in gam:
        p = _two_theta(lam, 0.3595, hkl)
        y += I * _pv(tt, p, 0.25 + 0.003 * (p - 45))
        peaks.append(("γ", hkl, p, I, VERM))
    y += np.random.default_rng(1).normal(0, 0.35, tt.size)
    ax.plot(tt, y, color=INK, lw=0.9)
    for ph, hkl, p, I, c in peaks:
        lab = f"{ph}({''.join(map(str, hkl))})"
        top = I + 5 + bg[np.searchsorted(tt, p)]
        dx = 0
        ha = "center"
        if ph == "γ" and hkl == (1, 1, 1):
            dx, ha = -0.5, "right"
        if ph == "α" and hkl == (1, 1, 0):
            dx, ha = 0.5, "left"
        ax.text(p + dx, top, f"{lab}\n{p:.2f}°", color=c, fontsize=7.5, ha=ha, va="bottom", linespacing=1.0)
    ax.set_xlim(45, 130)
    ax.set_ylim(0, 128)
    ax.set_xlabel(r"2$\theta$ (°), Co K$\alpha_1$, $\lambda$ = 0.178897 nm")
    ax.set_ylabel("intensity (arb. units)")
    ax.text(63, 112, "α ferrite (BCC), a = 0.2866 nm", color=BLUE, fontsize=8.5)
    ax.text(63, 103, "γ austenite (FCC), a = 0.3595 nm", color=VERM, fontsize=8.5)
    ax.text(63, 95, "phase balance ≈ 50/50", color="0.3", fontsize=8)

    ins = ax.inset_axes([0.67, 0.55, 0.32, 0.37])
    lc = 0.15406
    t2 = np.linspace(40, 100, 2000)
    y2 = 30 + 0.0 * t2
    for hkl, I in alpha:
        p = _two_theta(lc, 0.2866, hkl)
        if p < 100:
            y2 += I * 0.6 * _pv(t2, p, 0.3)
    for hkl, I in gam:
        p = _two_theta(lc, 0.3595, hkl)
        if p < 100:
            y2 += I * 0.6 * _pv(t2, p, 0.3)
    y2 += np.random.default_rng(3).normal(0, 1.6, t2.size)
    ins.plot(t2, y2, color="0.35", lw=0.7)
    ins.axhline(4, color=BLUE, ls=":", lw=0.8)
    ins.set_xlim(40, 100)
    ins.set_ylim(0, 100)
    ins.set_yticks([])
    ins.tick_params(labelsize=6.5, pad=1)
    ins.set_xlabel(r"2$\theta$ (°), Cu K$\alpha$", fontsize=6.5, labelpad=1)
    ins.set_title("same specimen, Cu Kα", fontsize=7, pad=2)
    ins.annotate("Fe fluorescence\n(Cu Kα 8.05 keV >\nFe K edge 7.11 keV)", xy=(62, 31), xytext=(62, 62),
                 fontsize=6, ha="center", va="bottom", arrowprops=dict(arrowstyle="-|>", lw=0.6))
    ins.text(99, 6, "background level with Co Kα", fontsize=5.8, color=BLUE, ha="right", va="bottom")
    save(fig, "52", "fig-52-4-xrd-duplex")


# ---------------------------------------------------------------- Figure 52.5
def dsc_pet():
    fig, ax = new_fig(6.6, 4.0)
    T = np.linspace(30, 290, 3000)
    rate = 10 / 60  # K/s
    base0 = -0.35 - 0.0006 * (T - 30)
    # glass transition: Cp step down (endo down) with relaxation overshoot
    Tg, wg = 78, 2.5
    step = -0.06 / (1 + np.exp(-(T - Tg) / wg))
    over = -0.035 * np.exp(-0.5 * ((T - (Tg + 3.5)) / 1.8) ** 2)
    base = base0 + step
    # cold crystallisation exotherm (up), 25 J/g
    s_cc = 6.0
    h_cc = 25 * rate / (s_cc * np.sqrt(2 * np.pi))
    cc = h_cc * np.exp(-0.5 * ((T - 130) / s_cc) ** 2)
    # melting endotherm (down), 45 J/g, skewed to low T
    from scipy.stats import skewnorm
    melt_shape = skewnorm.pdf(T, -3, loc=256, scale=9.5)
    melt = -45 * rate * melt_shape
    q = base + over + cc + melt
    ax.plot(T, q, color=INK, lw=1.6)
    ax.plot(T, base, color="0.45", ls="--", lw=0.9)
    ax.fill_between(T, base, base + cc, where=cc > 1e-4, color=VERM, alpha=0.3, lw=0)
    ax.fill_between(T, base + melt, base, where=melt < -1e-4, color=BLUE, alpha=0.3, lw=0)
    # check areas
    a_cc = np.trapezoid(cc, T) / rate
    a_m = -np.trapezoid(melt, T) / rate
    ax.text(130, base[np.searchsorted(T, 130)] + h_cc + 0.02, f"cold crystallization\nΔH$_{{cc}}$ = {a_cc:.0f} J/g",
            ha="center", va="bottom", fontsize=8.5, color=VERM)
    tm = T[np.argmin(melt)]
    ax.text(tm - 14, q.min() + 0.01, f"melting\nΔH$_m$ = {a_m:.0f} J/g", ha="right", va="bottom",
            fontsize=8.5, color=BLUE)
    yg = base[np.searchsorted(T, Tg)]
    ax.plot(Tg, yg, "o", color=GREEN, ms=5, zorder=5)
    ax.annotate(r"$T_g$ ≈ 78 °C (midpoint)", xy=(Tg, yg), xytext=(36, -0.6), fontsize=8.5, color=GREEN,
                ha="left", arrowprops=dict(arrowstyle="-|>", lw=0.7, color=GREEN))
    ax.annotate("enthalpy-relaxation\novershoot", xy=(Tg + 3.5, base[np.searchsorted(T, Tg + 3.5)] - 0.035),
                xytext=(98, -0.74), fontsize=7.5, ha="left",
                arrowprops=dict(arrowstyle="-|>", lw=0.6))
    ax.text(168, -0.1, "$X_c$ = (45 − 25)/140 = 14 % as received", fontsize=9,
            bbox=dict(fc="#FFF4D6", ec="0.6", lw=0.6, boxstyle="round,pad=0.35"))
    ax.set_xlim(30, 290)
    ax.set_ylim(-1.15, 0.05)
    ax.set_xlabel("temperature (°C), heating at 10 K/min")
    ax.set_ylabel("heat flow (W/g)   endo ↓  exo ↑")
    ax.text(287, -0.545, "baseline", fontsize=7.5, color="0.4", ha="right", va="bottom")
    save(fig, "52", "fig-52-5-dsc-pet")
    return a_cc, a_m


# ---------------------------------------------------------------- Figure 52.6
def uncertainty_budget():
    fig = plt.figure(figsize=(6.8, 4.3))
    gs = fig.add_gridspec(2, 1, height_ratios=[3.3, 1.0], hspace=0.55)
    ax = fig.add_subplot(gs[0])
    comps = [("specimen scatter (Type A)", 6 / np.sqrt(5)),
             ("load cell, class 1 (Type B)", 400 * 0.01 / np.sqrt(3)),
             ("0.2 % offset determination (Type B)", 400 * 0.005),
             ("diameter (Type B)", 400 * 2 * 0.01 / np.sqrt(3) / 10)]
    u = np.array([c[1] for c in comps])
    uc = np.sqrt((u ** 2).sum())
    U = 2 * uc
    share = u ** 2 / uc ** 2 * 100
    labels = [c[0] for c in comps] + ["combined $u_c$", "expanded $U$ ($k$ = 2)"]
    vals = list(u) + [uc, U]
    ypos = np.arange(len(vals))[::-1]
    cols = [SKY] * 4 + [BLUE, "white"]
    ecs = [INK] * 4 + [INK, BLUE]
    for yy, v, c, e in zip(ypos, vals, cols, ecs):
        ax.barh(yy, v, color=c, ec=e, lw=1.4 if c == "white" else 0.7, height=0.62)
        ax.text(v + 0.1, yy, f"{v:.2f} MPa", va="center", ha="left", fontsize=8)
    for yy, sh in zip(ypos[:4], share):
        ax.text(10.6, yy, f"{sh:.1f} %", va="center", ha="right", fontsize=8, color="0.3")
    ax.text(10.6, ypos[0] + 0.62, "share of\nvariance", va="bottom", ha="right", fontsize=7.5, color="0.3")
    ax.set_yticks(ypos)
    ax.set_yticklabels(labels, fontsize=8.5)
    ax.set_xlim(0, 10.7)
    ax.set_ylim(-0.6, len(vals) - 0.2)
    ax.set_xlabel("standard uncertainty (MPa)")
    ax.axhline(1.5, color="0.7", lw=0.6)
    ax.set_title(r"$R_{p0.2}$ = 400 MPa, five Ø10 mm specimens", fontsize=9, pad=4)

    a2 = fig.add_subplot(gs[1])
    a2.set_xlim(385, 415)
    a2.set_ylim(-1, 1.4)
    a2.set_yticks([])
    a2.spines["left"].set_visible(False)
    a2.axhline(0, color=INK, lw=0.8)
    a2.add_patch(Rectangle((400 - U, -0.25), 2 * U, 0.5, fc=BLUE, alpha=0.25, ec=BLUE))
    a2.plot([400, 400], [-0.45, 0.45], color=BLUE, lw=1.6, ls="--")
    a2.axvline(390, color=VERM, lw=1.5)
    a2.text(389.7, 0.75, "specification\nminimum 390 MPa", color=VERM, fontsize=7.5, va="center", ha="right")
    a2.text(400, 0.62, f"result 400 ± {U:.0f} MPa ($k$ = 2)", ha="center", va="bottom", fontsize=8.5, color=BLUE)
    a2.text(400 - U, -0.35, f"{400 - U:.0f}", ha="center", va="top", fontsize=7.5)
    a2.text(400 + U, -0.35, f"{400 + U:.0f}", ha="center", va="top", fontsize=7.5)
    a2.set_xticks([385, 390, 395, 400, 405, 410, 415])
    a2.tick_params(labelsize=8)
    a2.set_xlabel("yield strength (MPa)", fontsize=8.5)
    save(fig, "52", "fig-52-6-uncertainty-budget")
    return u, uc, U, share


if __name__ == "__main__":
    technique_map()
    interaction_volumes()
    f = ebsd_map()
    print("austenite fraction in map:", round(float(f), 3))
    print("DSC areas:", dsc_pet())
    xrd_duplex()
    print(uncertainty_budget())
