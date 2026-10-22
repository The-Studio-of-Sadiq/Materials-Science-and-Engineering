"""Figures for Chapter 10 — Phase Transformations in Solids.

Run from the repository root:  python figures/scripts/ch10.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from matplotlib.collections import LineCollection
from scipy.interpolate import PchipInterpolator
from scipy.spatial import Voronoi
from scipy.optimize import brentq

BLUE, VERM, GREEN, PINK, ORANGE, SKY = COLORS[:6]
GREY = "#A7AEB6"


def _sig(x, x0, w):
    return 0.5 * (1 + np.tanh((x - x0) / w))


def _arr(ax, p0, p1, color=INK, lw=1.0, ms=9, style="-|>", **kw):
    ax.annotate("", xy=p1, xytext=p0, arrowprops=dict(arrowstyle=style, color=color, lw=lw,
                mutation_scale=ms, shrinkA=0, shrinkB=0, **kw))


# ---------------------------------------------------------------- Figure 10.1
def ageing_curves():
    fig, ax = new_fig(6.4, 3.9)
    t = np.logspace(-2, 3, 600)          # days
    L = np.log10(t)
    # 130 °C: GP-zone rise to ~90 HV, theta'' peak ~130 HV at 30-50 d, then theta' softening
    H130 = 45 + 45 * _sig(L, np.log10(0.12), 0.32) + 41 * _sig(L, np.log10(8), 0.33) \
        - 40 * _sig(L, np.log10(300), 0.38)
    # 190 °C: no GP plateau, peak ~115 HV at ~1 d, ~70 HV by 100 d
    H190 = 45 + 72 * _sig(L, np.log10(0.11), 0.42) - 47 * _sig(L, np.log10(9), 0.5)
    ax.plot(t, H130, color=BLUE, label="130 °C")
    ax.plot(t, H190, color=VERM, label="190 °C")
    ax.set_xscale("log")
    ax.set_xlim(0.01, 1000)
    ax.set_ylim(40, 152)
    ax.set_yticks(range(40, 141, 20))
    ax.set_xlabel("ageing time (days)")
    ax.set_ylabel("hardness (HV)")
    ax.set_xticks([0.01, 0.1, 1, 10, 100, 1000])
    ax.set_xticklabels(["0.01", "0.1", "1", "10", "100", "1000"])
    # labels along 130 °C curve
    ax.annotate("GP zones", xy=(1.0, np.interp(1.0, t, H130)), xytext=(1.6, 76),
                fontsize=8.5, color=BLUE, arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.7))
    i = np.argmax(H130)
    ax.annotate("θ″", xy=(t[i], H130[i]), xytext=(t[i] * 0.35, 134), fontsize=10, color=BLUE,
                ha="center", arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.7))
    ax.annotate("θ′", xy=(400, np.interp(400, t, H130)), xytext=(520, 124), fontsize=10, color=BLUE,
                arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.7))
    ax.text(0.012, 50, "130 °C", color=BLUE, fontsize=9, weight="bold")
    # labels along 190 °C curve
    j = np.argmax(H190)
    ax.annotate("θ″ + θ′", xy=(t[j], H190[j]), xytext=(0.12, 122), fontsize=9, color=VERM,
                ha="center", arrowprops=dict(arrowstyle="-", color=VERM, lw=0.7))
    ax.annotate("θ (over-aged)", xy=(100, np.interp(100, t, H190)), xytext=(40, 54), fontsize=9,
                color=VERM, ha="center", arrowprops=dict(arrowstyle="-", color=VERM, lw=0.7))
    ax.text(0.022, 74, "190 °C", color=VERM, fontsize=9, weight="bold")
    print(f"  130 °C peak {H130[i]:.0f} HV at {t[i]:.0f} d; 190 °C peak {H190[j]:.0f} HV at {t[j]:.2f} d, "
          f"{np.interp(100, t, H190):.0f} HV at 100 d")
    # regions for the 190 °C curve
    y = 145
    edges = [0.01, 0.3, 4.0, 1000]
    names = ["under-aged", "peak-aged", "over-aged"]
    for k in range(3):
        a, b = edges[k], edges[k + 1]
        _arr(ax, (a * 1.04, y), (b / 1.04, y), color=VERM, lw=0.8, ms=7, style="<|-|>")
        ax.text(np.sqrt(a * b), y + 1.5, names[k], ha="center", va="bottom", fontsize=8.5, color=VERM)
    for e in edges[1:3]:
        ax.axvline(e, color=VERM, lw=0.6, ls=":", ymax=0.93)
    ax.text(0.011, 135, "190 °C:", fontsize=8, color=VERM, va="bottom")
    save(fig, "10", "fig-10-1-al-cu-ageing-curves")


# ---------------------------------------------------------------- Figure 10.2
def spinodal_vs_nucleation():
    fig = plt.figure(figsize=(6.8, 4.4))
    gs = fig.add_gridspec(2, 2, width_ratios=[1.0, 1.05], wspace=0.28, hspace=0.55)
    ax = fig.add_subplot(gs[:, 0])
    W = np.log(0.85 / 0.15) / 0.7          # Omega/RT giving binodal at 0.15 / 0.85
    x = np.linspace(0.002, 0.998, 800)
    tilt = 0.04
    G = x * np.log(x) + (1 - x) * np.log(1 - x) + W * x * (1 - x) + tilt * x
    xb = np.array([0.15, 0.85])
    Gb = xb * np.log(xb) + (1 - xb) * np.log(1 - xb) + W * xb * (1 - xb) + tilt * xb
    xs = 0.5 + np.array([-1, 1]) * np.sqrt(0.25 - 1 / (2 * W))
    Gs = xs * np.log(xs) + (1 - xs) * np.log(1 - xs) + W * xs * (1 - xs) + tilt * xs
    m = (x > 0.03) & (x < 0.97)
    ymin, ymax = G[m].min() - 0.06, G[m].max() + 0.01
    ax.axvspan(xb[0], xs[0], color=ORANGE, alpha=0.18, lw=0)
    ax.axvspan(xs[1], xb[1], color=ORANGE, alpha=0.18, lw=0)
    ax.axvspan(xs[0], xs[1], color=SKY, alpha=0.18, lw=0)
    ax.plot(x, G, color=INK)
    xt = np.array([0.04, 0.96])
    ax.plot(xt, Gb[0] + (Gb[1] - Gb[0]) / 0.7 * (xt - 0.15), color=BLUE, lw=1.0, ls="--")
    ax.plot(xb, Gb, "o", color=BLUE, ms=6, zorder=5)
    ax.plot(xs, Gs, "s", color=VERM, ms=5.5, zorder=5)
    for xv in xb:
        ax.axvline(xv, color=BLUE, lw=0.8, ls="--")
    for xv in xs:
        ax.axvline(xv, color=VERM, lw=0.8, ls=":")
    ax.set_xlim(0, 1)
    ax.set_ylim(ymin, ymax)
    ax.set_xlabel("composition x")
    ax.set_ylabel("free energy G (arb. units)")
    ax.set_yticks([])
    tr = ax.get_xaxis_transform()
    slope = (Gb[1] - Gb[0]) / 0.7
    ax.text(0.5, Gb[0] + slope * 0.35 - 0.01, "common tangent", color=BLUE, fontsize=8, ha="center",
            va="top", rotation=0)
    ax.text(xb[0] - 0.005, 0.97, "binodal", color=BLUE, fontsize=8, rotation=90, ha="right", va="top",
            transform=tr)
    ax.text(xs[0] + 0.005, 0.97, "spinodal", color=VERM, fontsize=8, rotation=90, ha="left", va="top",
            transform=tr)
    ax.text(0.5, 0.05, "unstable:\nspinodal", ha="center", fontsize=8.5, color="#1F5F8B", transform=tr)
    for xm in ((xb[0] + xs[0]) / 2, (xb[1] + xs[1]) / 2):
        ax.text(xm, 0.03, "metastable: nucleation needed", ha="center", va="bottom", fontsize=7.5,
                rotation=90, color="#8A5A00", transform=tr)
    ax.set_title("(a) free energy at fixed T", fontsize=10, loc="left")

    # (b) spinodal: sinusoid growing in amplitude
    a1 = fig.add_subplot(gs[0, 1])
    z = np.linspace(0, 3, 600)
    c0 = 0.5
    shades = ["#9CC7E6", "#4C97CB", BLUE]
    for A, col, lab in zip([0.04, 0.13, 0.30], shades, ["t₁", "t₂", "t₃"]):
        a1.plot(z, c0 + A * np.cos(2 * np.pi * z), color=col, lw=1.5, label=lab)
    a1.axhline(c0, color=GREY, lw=0.7, ls=":")
    for zz in [0.5, 1.5]:     # uphill diffusion: from troughs (z=0.5k) to peaks
        _arr(a1, (zz - 0.05, 0.58), (zz - 0.30, 0.58), color=VERM, lw=1.0, ms=7)
        _arr(a1, (zz + 0.05, 0.58), (zz + 0.30, 0.58), color=VERM, lw=1.0, ms=7)
    a1.text(2.5, 0.92, "uphill diffusion", color=VERM, fontsize=7.5, ha="center")
    _arr(a1, (2.2, 0.88), (1.82, 0.62), color=VERM, lw=0.7, ms=6)
    a1.annotate("", xy=(2.0, 0.08), xytext=(1.0, 0.08),
                arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=0.8, mutation_scale=7))
    a1.text(1.5, 0.11, r"$\lambda_{\max}$", ha="center", fontsize=9)
    a1.set_xlim(0, 3); a1.set_ylim(0, 1)
    a1.set_xticks([]); a1.set_yticks([0, 0.5, 1])
    a1.set_ylabel("c")
    a1.set_xlabel("distance", labelpad=2)
    a1.legend(fontsize=7.5, loc="upper right", handlelength=1.2, ncol=3, bbox_to_anchor=(1.02, 1.18),
              columnspacing=0.8)
    a1.set_title("(b) spinodal (inside spinodal)", fontsize=10, loc="left", pad=14)

    # (c) nucleation and growth: equilibrium-composition particle growing, depleted zone
    a2 = fig.add_subplot(gs[1, 1])
    c0n, ca, cb = 0.24, 0.15, 0.85
    zz = np.linspace(-1.5, 1.5, 1200)
    for w, Ld, col, lab in zip([0.07, 0.17, 0.30], [0.12, 0.25, 0.42], ["#F2B58C", "#E5823F", VERM],
                              ["t₁", "t₂", "t₃"]):
        r = np.abs(zz)
        c = np.where(r < w, cb, c0n - (c0n - ca) * np.exp(-(r - w) / Ld))
        c = np.where(r < w, cb, c)
        a2.plot(zz, c, color=col, lw=1.5, label=lab)
    a2.axhline(c0n, color=GREY, lw=0.7, ls=":")
    a2.text(1.48, c0n + 0.03, r"$c_0$", fontsize=8.5, ha="right", color="0.35")
    a2.text(0.36, 0.80, r"particle at $c_\beta$", fontsize=8, color=VERM, ha="left")
    a2.annotate("depleted zone", xy=(0.45, 0.18), xytext=(0.75, 0.48), fontsize=8, color=INK,
                arrowprops=dict(arrowstyle="-", lw=0.7))
    a2.set_xlim(-1.5, 1.5); a2.set_ylim(0, 1)
    a2.set_xticks([]); a2.set_yticks([0, 0.5, 1])
    a2.set_ylabel("c")
    a2.set_xlabel("distance", labelpad=2)
    a2.set_title("(c) nucleation and growth\n     (between binodal and spinodal)", fontsize=10, loc="left")
    a2.legend(fontsize=7.5, loc="upper left", handlelength=1.2)
    save(fig, "10", "fig-10-2-spinodal-vs-nucleation")


# ---------------------------------------------------------------- Figure 10.3
def _proj(p, ang=np.radians(28), k=0.5):
    """Oblique projection: x right, z up, y receding at angle ang with scale k."""
    p = np.asarray(p, float)
    return np.array([p[..., 0] + k * p[..., 1] * np.cos(ang), p[..., 2] + k * p[..., 1] * np.sin(ang)]).T


def bain_correspondence():
    fig, ax = schematic(6.8, 3.7, xlim=(-0.08, 1.80), ylim=(-0.17, 0.66))
    ag = 0.3590
    a_m, c_m = 0.2856, 0.2959
    # two FCC cells along x
    cube_e = []
    for x0 in (0, ag):
        for s in [((0, 0, 0), (1, 0, 0)), ((0, 1, 0), (1, 1, 0)), ((0, 0, 1), (1, 0, 1)), ((0, 1, 1), (1, 1, 1)),
                  ((0, 0, 0), (0, 1, 0)), ((1, 0, 0), (1, 1, 0)), ((0, 0, 1), (0, 1, 1)), ((1, 0, 1), (1, 1, 1)),
                  ((0, 0, 0), (0, 0, 1)), ((1, 0, 0), (1, 0, 1)), ((0, 1, 0), (0, 1, 1)), ((1, 1, 0), (1, 1, 1))]:
            p0 = np.array(s[0]) * ag + [x0, 0, 0]
            p1 = np.array(s[1]) * ag + [x0, 0, 0]
            cube_e.append(_proj(np.array([p0, p1])))
    ax.add_collection(LineCollection(cube_e, colors="0.55", linewidths=0.8, zorder=1))
    atoms = set()
    for x0 in (0, 1):
        for c in [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0), (0, 0, 1), (1, 0, 1), (0, 1, 1), (1, 1, 1)]:
            atoms.add((c[0] + x0, c[1], c[2]))
        for f in [(0.5, 0.5, 0), (0.5, 0.5, 1), (0.5, 0, 0.5), (0.5, 1, 0.5), (0, 0.5, 0.5), (1, 0.5, 0.5)]:
            atoms.add((f[0] + x0, f[1], f[2]))
    atoms = sorted(atoms, key=lambda a: -a[1])   # back to front
    # BCT cell: base square corners (1,0,0),(1.5,.5,0),(1,1,0),(.5,.5,0); body centre (1,.5,.5)
    base = np.array([(1, 0, 0), (1.5, 0.5, 0), (1, 1, 0), (0.5, 0.5, 0)], float)
    bct_atoms = {tuple(p) for p in base} | {tuple(p + [0, 0, 1]) for p in base} | {(1, 0.5, 0.5)}
    for a in atoms:
        P = _proj(np.array(a) * ag)
        hl = tuple(float(v) for v in a) in bct_atoms
        ax.add_patch(Circle(P, 0.020 if hl else 0.016, fc=BLUE if hl else "#C9D3DD", ec=INK, lw=0.6,
                            zorder=4 if hl else 3))
    segs = []
    for i in range(4):
        for dz in (0, 1):
            segs.append(_proj(np.array([base[i] + [0, 0, dz], base[(i + 1) % 4] + [0, 0, dz]]) * ag))
        segs.append(_proj(np.array([base[i], base[i] + [0, 0, 1]]) * ag))
    ax.add_collection(LineCollection(segs, colors=VERM, linewidths=2.2, zorder=2))
    # dimension labels
    ax.text(0.47, -0.06, r"$a_\gamma/\sqrt{2}$ = 0.254 nm", fontsize=8, color=VERM, ha="left")
    p = _proj(np.array([(0.5, 0.5, 0.5)]) * ag)[0]
    ax.text(p[0] - 0.03, p[1] + 0.03, r"$a_\gamma$ = 0.359 nm", fontsize=8, color=VERM, ha="right")
    ax.text(-0.06, -0.15, "FCC austenite, two cells (grey);  BCT cell in bold:  c/a = √2 = 1.414",
            fontsize=8, ha="left")
    # strain arrows on the BCT cell
    top = _proj(np.array([1, 0.5, 1.0]) * ag)
    bot = _proj(np.array([1, 0.5, 0.0]) * ag)
    _arr(ax, top + [0, 0.10], top + [0, 0.025], color=GREEN, lw=1.6, ms=10)
    _arr(ax, bot - [0, 0.10], bot - [0, 0.025], color=GREEN, lw=1.6, ms=10)
    ax.text(top[0] + 0.015, top[1] + 0.075, "−17.6 % along [001]", color=GREEN, fontsize=8, ha="left")
    r1 = _proj(np.array([1.5, 0.5, 0.5]) * ag)
    _arr(ax, r1 + [0.01, 0], r1 + [0.10, 0], color=GREEN, lw=1.6, ms=10)
    ax.text(r1[0] + 0.02, r1[1] - 0.03, "+12.5 % along\n[110] and [1̄10]", color=GREEN, fontsize=8,
            ha="left", va="top", bbox=dict(fc="white", ec="none", alpha=0.85, pad=0.5))
    # axes triad
    o = np.array([-0.05, 0.47])
    for v, lab in [((1, 0, 0), "x"), ((0, 1, 0), "y"), ((0, 0, 1), "z [001]")]:
        d = _proj(np.array(v) * 0.07)
        _arr(ax, o, o + d, lw=0.8, ms=6)
        ax.text(*(o + d * 1.25), lab, fontsize=7.5, ha="center", va="center")

    # big arrow
    _arr(ax, (1.0, 0.33), (1.14, 0.33), lw=2.0, ms=14)
    ax.text(1.07, 0.37, "Bain\nstrain", ha="center", fontsize=8.5)

    # martensite cell (same scale, nm)
    off = np.array([1.31, 0.0, 0.0])
    corners = np.array([(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)], float)
    sc = np.array([a_m, a_m, c_m])
    msegs = []
    for i in range(4):
        for dz in (0, 1):
            msegs.append(_proj(np.array([(corners[i] + [0, 0, dz]) * sc + off,
                                         (corners[(i + 1) % 4] + [0, 0, dz]) * sc + off])))
        msegs.append(_proj(np.array([corners[i] * sc + off, (corners[i] + [0, 0, 1]) * sc + off])))
    ax.add_collection(LineCollection(msegs, colors=VERM, linewidths=2.2, zorder=2))
    fe = [tuple(c + [0, 0, dz]) for c in corners for dz in (0, 1)] + [(0.5, 0.5, 0.5)]
    csites = [tuple(c + [0, 0, 0.5]) for c in corners] + [(0.5, 0.5, 0), (0.5, 0.5, 1)]
    allp = [(p, "Fe") for p in fe] + [(p, "C") for p in csites]
    allp.sort(key=lambda q: -q[0][1])
    for p, kind in allp:
        P = _proj(np.array(p) * sc + off)
        if kind == "Fe":
            ax.add_patch(Circle(P, 0.020, fc=BLUE, ec=INK, lw=0.6, zorder=4))
        else:
            ax.add_patch(Circle(P, 0.009, fc=ORANGE, ec=INK, lw=0.5, zorder=5))
    p = _proj(np.array([0.5, 0, 0]) * sc + off)
    ax.text(p[0], p[1] - 0.045, "a = 0.286 nm", fontsize=8, color=VERM, ha="center")
    p = _proj(np.array([0, 0, 0.5]) * sc + off)
    ax.text(p[0] - 0.025, p[1], "c = 0.296 nm", fontsize=8, color=VERM, ha="right", va="center")
    ax.text(1.27, 0.47, "BCT martensite, c/a = 1.036\n(Fe–0.8 wt% C)", fontsize=8.5, ha="left")
    ax.add_patch(Circle((1.30, -0.13), 0.016, fc=BLUE, ec=INK, lw=0.6))
    ax.text(1.33, -0.13, "Fe", fontsize=8, va="center")
    ax.add_patch(Circle((1.41, -0.13), 0.009, fc=ORANGE, ec=INK, lw=0.5))
    ax.text(1.43, -0.13, "octahedral C sites\n(≈4 % filled at 0.8 % C)", fontsize=7.5, va="center")
    save(fig, "10", "fig-10-3-bain-correspondence")


# ---------------------------------------------------------------- Figure 10.4
def _grains(ax, x0, x1, y0, y1, n, seed, stretch=1.0, tangles=False, sub=False, new=0):
    r = np.random.default_rng(seed)
    S = np.c_[r.uniform(0, 1, n), r.uniform(0, 1, n)]
    V = Voronoi(np.vstack([S, [[-5, -5], [5, -5], [5, 5], [-5, 5]]]))
    W, H = x1 - x0, y1 - y0
    segs = []
    for rv in V.ridge_vertices:
        if -1 in rv:
            continue
        p = V.vertices[rv].copy()
        p[:, 1] = 0.5 + (p[:, 1] - 0.5) / stretch
        segs.append(np.c_[x0 + p[:, 0] * W, y0 + p[:, 1] * H])
    clip = Rectangle((x0, y0), W, H, transform=ax.transData)
    ax.add_patch(Rectangle((x0, y0), W, H, fc="#F4F0E8", ec=INK, lw=0.8))
    lc = LineCollection(segs, colors="0.3", linewidths=0.8)
    ax.add_collection(lc); lc.set_clip_path(clip)
    if tangles:
        for _ in range(55):
            cx, cy = x0 + r.uniform(0.04, 0.96) * W, y0 + r.uniform(0.08, 0.92) * H
            a = r.uniform(0, np.pi)
            ln, = ax.plot([cx - 0.03 * W * np.cos(a), cx + 0.03 * W * np.cos(a)],
                          [cy - 0.06 * H * np.sin(a), cy + 0.06 * H * np.sin(a)], color=VERM, lw=0.6)
            ln.set_clip_path(clip)
    if sub:
        for _ in range(30):
            cx, cy = x0 + r.uniform(0.04, 0.96) * W, y0 + r.uniform(0.1, 0.9) * H
            ln, = ax.plot([cx, cx], [cy - 0.07 * H, cy + 0.07 * H], color=VERM, lw=0.7)
            ln.set_clip_path(clip)
    if new:
        S2 = np.c_[r.uniform(0.05, 0.95, new), r.uniform(0.1, 0.9, new)]
        for sx, sy in S2:
            ax.add_patch(Circle((x0 + sx * W, y0 + sy * H), 0.09 * H, fc="white", ec=GREEN, lw=0.8,
                                zorder=3))


def annealing_stages():
    fig = plt.figure(figsize=(6.8, 5.0))
    gs = fig.add_gridspec(3, 1, height_ratios=[0.42, 1.0, 0.75], hspace=0.10)
    T = np.linspace(100, 700, 601)
    UTS = 600 - 30 * _sig(T, 220, 60) - 230 * _sig(T, 375, 32) - 12 * (T - 450).clip(0) / 250
    EL = 5 + 3 * _sig(T, 220, 60) + 42 * _sig(T, 375, 32) + 5 * (T - 450).clip(0) / 250
    # grain size: new grains ~10 µm at 400 °C, parabolic growth (Q ~ 150 kJ/mol) to ~70 µm at 700 °C
    Tk = T + 273.15
    d0, d700 = 10.0, 70.0
    Q, R = 150e3, 8.314
    K = lambda tk: np.exp(-Q / R * (1 / tk - 1 / 973.15))
    k_rel = (d700 ** 2 - d0 ** 2) / (K(973.15) - K(673.15))
    dg = np.sqrt(d0 ** 2 + k_rel * (K(Tk) - K(673.15)).clip(0))
    early = (T >= 355) & (T < 400)
    dg = np.where(T < 400, np.nan, dg)
    dg[early] = 3 + 7 * (T[early] - 355) / 45
    regions = [(100, 300, "recovery", "#E3EEF8"), (300, 450, "recrystallization", "#FFF1D6"),
               (450, 700, "grain growth", "#E2F3EC")]
    axs = fig.add_subplot(gs[0])
    axs.set_xlim(100, 700); axs.set_ylim(0, 1); axs.axis("off")
    _grains(axs, 125, 275, 0.05, 0.80, 22, seed=3, stretch=2.5, tangles=True)
    _grains(axs, 300, 450, 0.05, 0.80, 22, seed=3, stretch=2.5, sub=True, new=8)
    _grains(axs, 500, 650, 0.05, 0.80, 9, seed=6)
    for x, s in [(200, "deformed grains, tangles"), (375, "subgrains + new grains"), (575, "large equiaxed grains")]:
        axs.text(x, 0.84, s, ha="center", va="bottom", fontsize=8)

    ax1 = fig.add_subplot(gs[1])
    ax2 = fig.add_subplot(gs[2], sharex=ax1)
    for ax in (ax1, ax2):
        for a, b, name, col in regions:
            ax.axvspan(a, b, color=col, lw=0)
    for a, b, name, col in regions:
        ax1.text((a + b) / 2, 690, name, ha="center", va="top", fontsize=9, weight="bold", color="0.35")
    l1, = ax1.plot(T, UTS, color=BLUE, label="tensile strength")
    ax1.set_ylabel("tensile strength (MPa)", color=BLUE)
    ax1.set_ylim(300, 700)
    ax1b = ax1.twinx()
    ax1b.spines["right"].set_visible(True)
    l2, = ax1b.plot(T, EL, color=VERM, label="elongation")
    ax1b.set_ylabel("elongation (%)", color=VERM)
    ax1b.set_ylim(0, 60)
    ax1.legend(handles=[l1, l2], loc="center right", fontsize=8, bbox_to_anchor=(1.0, 0.55))
    plt.setp(ax1.get_xticklabels(), visible=False)

    ax2.plot(T, dg, color=GREEN, label="grain size")
    ax2.plot([100, 350], [25, 25], color=GREEN, ls=":", lw=1.4)
    ax2.text(110, 29, "original grains, cold-worked (unchanged)", fontsize=7.8, color="#006B4E")
    ax2.text(412, 13, "new grains ≈10 µm", fontsize=7.8, color="#006B4E", va="bottom")
    ax2.set_ylabel("grain size (µm)", color="#006B4E")
    ax2.set_ylim(0, 80)
    ax2.set_xlim(100, 700)
    ax2.set_xlabel("annealing temperature, 1 h (°C)")
    ax1.text(110, 480, "70 % cold-rolled\nCu–30Zn brass", fontsize=8.5, va="center")
    save(fig, "10", "fig-10-4-annealing-stages")


# ---------------------------------------------------------------- Figure 10.5
def _curve(pts):
    T, t = np.array(pts, float).T
    o = np.argsort(T)
    return PchipInterpolator(T[o], np.log10(t[o]))


def ttt_eutectoid():
    fig, ax = new_fig(6.6, 4.6)
    start = _curve([(722, 600), (715, 100), (700, 20), (650, 3), (600, 1.1), (540, 0.7), (500, 0.9),
                    (450, 2.5), (400, 8), (350, 25), (300, 60), (250, 160), (220, 280)])
    finish = _curve([(722, 3e4), (715, 6000), (700, 1000), (650, 50), (600, 12), (540, 6), (500, 8),
                     (450, 30), (400, 120), (350, 500), (300, 2000), (250, 6000), (220, 1.2e4)])
    Ts = np.linspace(220, 722, 500)
    ax.plot(10 ** start(Ts), Ts, color=INK, lw=1.8)
    ax.plot(10 ** finish(Ts), Ts, color=INK, lw=1.8, ls="--")
    ax.fill_betweenx(Ts, 10 ** start(Ts), 10 ** finish(Ts), color="#EEE6D8", lw=0)
    ax.axhline(727, color=INK, lw=0.9, ls="--")
    ax.text(1.3e5, 732, "A₁ = 727 °C", ha="right", va="bottom", fontsize=8.5)
    for Tm, lab in [(220, "Mₛ = 220 °C"), (160, "M₅₀ ≈ 160 °C"), (10, "M₉₀ ≈ 10 °C")]:
        ax.axhline(Tm, color=VERM, lw=1.0, ls="-" if Tm == 220 else ":", xmax=1.0)
        ax.text(1.3e5 if Tm > 10 else 2e2, Tm + 4, lab, ha="right", va="bottom", fontsize=8, color=VERM)
    # product regions (right of finish curve)
    for Tr, lab in [(688, "coarse pearlite"), (595, "fine pearlite"), (470, "upper bainite"),
                    (315, "lower bainite")]:
        ax.text(1.3e5, Tr, lab, ha="right", va="center", fontsize=8.5)
    for Tb in (650, 540, 400):
        ax.plot([10 ** finish(Tb) * 1.5, 1.4e5], [Tb, Tb], color=GREY, lw=0.6)
    ax.text(0.6, 765, "austenite (stable above A₁)", fontsize=8, va="center")
    ax.text(0.8, 640, "A", fontsize=10, weight="bold")
    ax.text(4.0, 470, "A + B", fontsize=8.5)
    ax.text(200, 650, "A + P", fontsize=8.5)
    ax.text(1.0, 360, "A (unstable)", fontsize=8)
    ax.text(0.5, 128, "A + M", fontsize=8.5, color=VERM)
    ax.text(1.5, 40, "M", fontsize=10, color=VERM, weight="bold")
    # cooling paths
    def quench(t0, T0, T1, tau, n=200, tend=None):
        tt = np.logspace(np.log10(t0), np.log10(tend), n)
        return tt, T1 + (T0 - T1) * np.exp(-(tt - t0) / tau)
    pc = [GREEN, BLUE, PINK, ORANGE]
    # (a) water quench
    tt, TT = quench(0.1, 800, 25, 0.12, tend=1.0)
    ax.plot(tt, TT, color=pc[0], lw=1.6)
    ax.text(0.2, 160, "(a)", color=pc[0], fontsize=9, weight="bold", ha="right")
    # (b) quench to 600, hold
    tt, TT = quench(0.1, 800, 600, 0.06, tend=4e3)
    tt = np.r_[tt, np.logspace(np.log10(4e3), np.log10(3e4), 40)]
    TT = np.r_[TT, 600 - (600 - 25) * (1 - np.exp(-(tt[-40:] - 4e3) / 3e3))]
    ax.plot(tt, TT, color=pc[1], lw=1.6)
    ax.text(1.2e3, 607, "(b)", color=pc[1], fontsize=9, weight="bold", va="bottom")
    # (c) quench to 300, hold (austempering)
    tt, TT = quench(0.1, 800, 300, 0.08, tend=1e4)
    ax.plot(tt, TT, color=pc[2], lw=1.6)
    ax.plot([1e4, 1e4 * 1.6, 3e4], [300, 200, 25], color=pc[2], lw=1.6)
    ax.text(8, 285, "(c)", color=pc[2], fontsize=9, weight="bold", va="top")
    # (d) martempering: quench to 240, equalize, slow cool through Ms
    tt, TT = quench(0.1, 800, 240, 0.09, tend=20)
    t2 = np.linspace(20, 900, 200)
    T2 = 240 - (240 - 25) * (t2 - 20) / 880
    ax.plot(np.r_[tt, t2], np.r_[TT, T2], color=pc[3], lw=1.6)
    ax.text(3, 245, "(d)", color=pc[3], fontsize=9, weight="bold", va="bottom")
    ax.set_xscale("log")
    ax.set_xlim(0.1, 1e5)
    ax.set_ylim(0, 800)
    ax.set_xlabel("time (s)")
    ax.set_ylabel("temperature (°C)")
    leg = ["(a) water quench → martensite", "(b) hold at 600 °C → fine pearlite (patenting)",
           "(c) hold at 300 °C → lower bainite (austempering)",
           "(d) equalize above Mₛ, cool slowly → martensite (martempering)"]
    from matplotlib.lines import Line2D
    h = [Line2D([], [], color=c, lw=1.6) for c in pc]
    h += [Line2D([], [], color=INK, lw=1.8), Line2D([], [], color=INK, lw=1.8, ls="--")]
    leg += ["transformation start (1 %)", "transformation finish (99 %)"]
    ax.legend(h, leg, fontsize=7.5, loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=2,
              handlelength=1.8, columnspacing=1.0)
    save(fig, "10", "fig-10-5-ttt-eutectoid")


# ---------------------------------------------------------------- Figure 10.6
def cct_4340():
    fig, ax = new_fig(6.6, 4.6)
    fp_s = _curve([(718, 6e4), (710, 8000), (700, 3000), (680, 1400), (650, 1000), (620, 1200),
                   (600, 1800), (580, 3000)])
    fp_f = _curve([(705, 9e4), (690, 3e4), (670, 1.3e4), (650, 9000), (620, 1.1e4), (600, 1.6e4),
                   (585, 2.5e4)])
    b_s = _curve([(560, 2000), (530, 400), (500, 130), (450, 65), (400, 60), (350, 80), (310, 120)])
    b_f = _curve([(530, 6e3), (500, 1500), (450, 500), (400, 320), (350, 380), (310, 550)])
    T1 = np.linspace(580, 718, 200)
    ax.plot(10 ** fp_s(T1), T1, color=INK, lw=1.8)
    T1f = np.linspace(585, 705, 200)
    ax.plot(10 ** fp_f(T1f), T1f, color=INK, lw=1.4, ls="--")
    T2 = np.linspace(310, 560, 200)
    ax.plot(10 ** b_s(T2), T2, color=INK, lw=1.8)
    T2f = np.linspace(310, 530, 200)
    ax.plot(10 ** b_f(T2f), T2f, color=INK, lw=1.4, ls="--")
    ax.axhline(775, color=INK, lw=0.9, ls="--")
    ax.axhline(720, color=INK, lw=0.9, ls="--")
    ax.text(9e4, 779, "Ac₃ ≈ 775 °C", fontsize=8, va="bottom", ha="right")
    ax.text(9e4, 724, "Ac₁ ≈ 720 °C", fontsize=8, va="bottom", ha="right")
    ax.axhline(305, color=VERM, lw=1.0)
    ax.axhline(240, color=VERM, lw=1.0, ls=":")
    ax.text(9e4, 309, "Mₛ = 305 °C", fontsize=8, color=VERM, ha="right", va="bottom")
    ax.text(9e4, 244, "M₅₀ ≈ 240 °C", fontsize=8, color=VERM, ha="right", va="bottom")
    ax.text(5e4, 590, "ferrite +\npearlite", fontsize=8.5, ha="center")
    ax.text(900, 440, "bainite", fontsize=8.5, ha="center")
    # Newtonian cooling curves from 850 °C
    t = np.logspace(0, 5, 800)
    cool = lambda tau: 25 + 825 * np.exp(-(t - 1) / tau)
    clip = lambda T: np.where(T < 40, np.nan, T)
    # critical curve tangent to the bainite start curve
    Tq = np.linspace(312, 555, 400)
    tau_c = np.min((10 ** b_s(Tq) - 1) / np.log(825 / (Tq - 25)))
    rate700 = (700 - 25) / tau_c
    print(f"  CCT: critical tau = {tau_c:.0f} s, cooling rate at 700 °C = {rate700:.1f} °C/s")
    curves = [(4.6, "1", GREEN), (1.25 * tau_c, "2", BLUE), (600, "3", PINK), (5e4, "4", ORANGE)]
    for tau, lab, col in curves:
        TT = cool(tau)
        ax.plot(t, clip(TT), color=col, lw=1.6)
    ax.plot(t, clip(cool(tau_c)), color=GREY, lw=1.3, ls="-.")
    TT = cool(tau_c)
    k = np.searchsorted(-TT, -650)
    ax.annotate(f"critical cooling curve\n(≈{rate700:.0f} °C/s at 700 °C)", xy=(t[k], TT[k]),
                xytext=(160, 815), fontsize=7.8, color="0.35",
                arrowprops=dict(arrowstyle="-", color="0.45", lw=0.7))
    # labels
    lab_txt = {"1": "① water-quenched 10 mm bar:\n    martensite, 57 HRC",
               "2": "② oil-quenched 50 mm bar, centre:\n    martensite + bainite, ≈50 HRC",
               "3": "③ air-cooled 50 mm bar:\n    bainite, ≈38 HRC",
               "4": "④ furnace-cooled:\n    ferrite + pearlite, ≈25 HRC"}
    for tau, lab, col in curves:
        TT = cool(tau)
        Tm = 160 if lab != "4" else 640
        if lab == "4":
            k = np.searchsorted(-TT, -560)
        else:
            k = np.searchsorted(-TT, -Tm)
        ax.text(t[k], TT[k], {"1": "①", "2": "②", "3": "③", "4": "④"}[lab], color=col, fontsize=11,
                ha="center", va="center", weight="bold",
                bbox=dict(fc="white", ec="none", pad=0.5))
    y = 0.02
    from matplotlib.lines import Line2D
    h = [Line2D([], [], color=c, lw=1.6) for _, _, c in curves]
    ax.legend(h, [lab_txt[l] for _, l, _ in curves], fontsize=7.5, loc="upper center",
              bbox_to_anchor=(0.5, -0.14), ncol=2, handlelength=1.6, columnspacing=1.0)
    ax.set_xscale("log")
    ax.set_xlim(1, 1e5)
    ax.set_ylim(0, 900)
    ax.set_xlabel("time (s)")
    ax.set_ylabel("temperature (°C)")
    save(fig, "10", "fig-10-6-cct-4340")


if __name__ == "__main__":
    ageing_curves()
    spinodal_vs_nucleation()
    bain_correspondence()
    annealing_stages()
    ttt_eutectoid()
    cct_4340()
