"""Figures for Chapter 34 — Semiconductor Interfaces and Thin Films.

Run from the repository root:  python figures/scripts/ch34.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle
from matplotlib.collections import PolyCollection
from scipy.optimize import brentq
from scipy.spatial import Voronoi

BLUE, RED, GREEN, PINK, ORANGE = COLORS[0], COLORS[1], COLORS[2], COLORS[3], COLORS[4]


def _varrow(ax, x, y0, y1, text, side="right", color=INK, fs=8.5, dx=0.08):
    ax.annotate("", xy=(x, y1), xytext=(x, y0),
                arrowprops=dict(arrowstyle="<|-|>", color=color, lw=0.9, shrinkA=0, shrinkB=0,
                                mutation_scale=8))
    ha = "left" if side == "right" else "right"
    ax.text(x + (dx if side == "right" else -dx), (y0 + y1) / 2, text, ha=ha, va="center",
            fontsize=fs, color=color)


# ---------------------------------------------------------------- Figure 34.1
def band_alignment_types():
    fig = plt.figure(figsize=(6.8, 4.6))
    gs = fig.add_gridspec(3, 2, width_ratios=[2.25, 1.0], wspace=0.05, hspace=0.25)
    ax = fig.add_subplot(gs[:, 0])
    chiA, EgA, chiB, EgB = 4.1, 1.2, 3.6, 2.2
    # ---- isolated semiconductors (vacuum level at 0)
    xa0, xa1, xb0, xb1 = 0.2, 1.7, 2.3, 3.8
    ax.plot([xa0, xb1], [0, 0], color=INK, lw=1.2)
    ax.text((xa0 + xb1) / 2, 0.12, r"common vacuum level $E_{\rm vac}$", ha="center", va="bottom", fontsize=8.5)
    for (x0, x1, chi, Eg, c, nm, EFoff) in [(xa0, xa1, chiA, EgA, BLUE, "A\n(narrow gap)", -0.12),
                                             (xb0, xb1, chiB, EgB, RED, "B\n(wide gap)", None)]:
        Ec, Ev = -chi, -chi - Eg
        ax.plot([x0, x1], [Ec, Ec], color=c, lw=2)
        ax.plot([x0, x1], [Ev, Ev], color=c, lw=2)
        ax.text(x0, Ec + 0.1, r"$E_c$", color=c, fontsize=8.5, va="bottom")
        ax.text(x0, Ev - 0.1, r"$E_v$", color=c, fontsize=8.5, va="top")
        ax.text((x0 + x1) / 2, -6.35, nm, ha="center", va="top", fontsize=8.5, color=c)
    _varrow(ax, xa1 - 0.25, 0, -chiA, r"$\chi_A$", side="left")
    _varrow(ax, xa1 - 0.25, -chiA, -chiA - EgA, r"$E_{g,A}$", side="left")
    _varrow(ax, xb1 - 0.25, 0, -chiB, r"$\chi_B$", side="left")
    _varrow(ax, xb1 - 0.25, -chiB, -chiB - EgB, r"$E_{g,B}$", side="left")
    # Fermi levels: A n-type, B p-type
    ax.plot([xa0, xa1], [-chiA - 0.12] * 2, color=INK, ls="--", lw=0.9)
    ax.plot([xb0, xb1], [-chiB - EgB + 0.12] * 2, color=INK, ls="--", lw=0.9)
    ax.text(xa0 + 0.05, -chiA - 0.18, r"$E_F$ (n)", fontsize=7.5, va="top")
    ax.text(xb0 + 0.05, -chiB - EgB + 0.18, r"$E_F$ (p)", fontsize=7.5, va="bottom")
    ax.text(2.0, 1.75, "isolated", ha="center", fontsize=9.5, weight="bold")
    # ---- joined junction
    EF = -chiA - 0.12           # A far side keeps its isolated position
    PhiA, PhiB = chiA + 0.12, chiB + EgB - 0.12
    Vbi = PhiB - PhiA
    vacL = EF + PhiA
    W = 1.8
    x0j, xi, x1j = 4.6, 7.25, 9.9
    x = np.linspace(x0j, x1j, 600)
    s = x - xi
    vac = np.where(s < -W, vacL,
          np.where(s < 0, vacL + Vbi / 2 * ((s + W) / W) ** 2,
          np.where(s < W, vacL + Vbi - Vbi / 2 * (1 - s / W) ** 2, vacL + Vbi)))
    left = s < 0
    ax.plot(x, vac, color=INK, lw=1.2)
    ax.plot(x[left], vac[left] - chiA, color=BLUE, lw=2)
    ax.plot(x[left], vac[left] - chiA - EgA, color=BLUE, lw=2)
    ax.plot(x[~left], vac[~left] - chiB, color=RED, lw=2)
    ax.plot(x[~left], vac[~left] - chiB - EgB, color=RED, lw=2)
    vi = vacL + Vbi / 2
    ax.plot([xi, xi], [vi - chiA, vi - chiB], color=INK, lw=1.2)
    ax.plot([xi, xi], [vi - chiA - EgA, vi - chiB - EgB], color=INK, lw=1.2)
    ax.plot([x0j, x1j], [EF, EF], color=INK, ls="--", lw=0.9)
    ax.text(x0j + 0.05, EF - 0.08, r"$E_F$", fontsize=8.5, va="top")
    _varrow(ax, xi + 0.35, vi - chiA, vi - chiB, r"$\Delta E_c=\chi_A-\chi_B$", fs=8)
    ax.annotate("", xy=(xi + 0.25, vi - chiB - EgB), xytext=(xi + 0.25, vi - chiA - EgA),
                arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=0.9, shrinkA=0, shrinkB=0, mutation_scale=8))
    ax.text(xi + 0.4, vi - chiB - EgB - 0.12, r"$\Delta E_v=\Delta E_g-\Delta E_c$", fontsize=8, va="top")
    ax.text(x0j + 0.05, vacL + 0.1, r"$E_{\rm vac}$", fontsize=8, va="bottom")
    ax.text(x0j + 0.05, vacL - chiA + 0.1, r"$E_c$", fontsize=8.5, color=BLUE, va="bottom")
    ax.text(x0j + 0.05, vacL - chiA - EgA - 0.1, r"$E_v$", fontsize=8.5, color=BLUE, va="top")
    ax.text(x1j - 0.05, vacL + Vbi - chiB + 0.1, r"$E_c$", fontsize=8.5, color=RED, va="bottom", ha="right")
    ax.text(x1j - 0.05, vacL + Vbi - chiB - EgB - 0.1, r"$E_v$", fontsize=8.5, color=RED, va="top", ha="right")
    ax.text((x0j + xi) / 2 - 0.4, -6.45, "n-A", ha="center", fontsize=8.5, color=BLUE)
    ax.text((xi + x1j) / 2 + 0.4, -6.45, "p-B", ha="center", fontsize=8.5, color=RED)
    ax.text((x0j + x1j) / 2, 1.75, "in contact", ha="center", fontsize=9.5, weight="bold")
    ax.axvline(xi, color="0.75", lw=0.6, ls=":", ymax=0.88)
    ax.set_xlim(0, 10)
    ax.set_ylim(-7.0, 2.1)
    ax.axis("off")

    # ---- three alignment types
    types = [
        ("Type I (straddling)", "GaAs/AlGaAs", (0.0, 1.4), (0.3, -0.3)),
        ("Type II (staggered)", "Si/strained SiGe, GaAsSb/InP", (0.5, 1.2), (-0.2, -0.6)),
        ("Type III (broken gap)", "InAs/GaSb", (-0.4, 0.0), (0.6, -0.15)),
    ]
    # each tuple: (Ev_A, Ec_A) narrow, (Ec_B, Ev_B) wide relative
    specs = [
        dict(A=(0.0, 1.0), B=(-0.45, 1.5)),
        dict(A=(0.35, 1.25), B=(-0.35, 0.85)),
        dict(A=(-0.9, -0.55), B=(-0.25, 0.45)),
    ]
    for k, ((title, ex, _, _), sp) in enumerate(zip(types, specs)):
        a = fig.add_subplot(gs[k, 1])
        a.set_xlim(0, 4)
        a.set_ylim(-1.35, 2.15)
        a.axis("off")
        EvA, EcA = sp["A"]
        EvB, EcB = sp["B"]
        a.plot([0.3, 2.0], [EcA, EcA], color=BLUE, lw=2)
        a.plot([0.3, 2.0], [EvA, EvA], color=BLUE, lw=2)
        a.plot([2.0, 3.7], [EcB, EcB], color=RED, lw=2)
        a.plot([2.0, 3.7], [EvB, EvB], color=RED, lw=2)
        a.plot([2.0, 2.0], [min(EvA, EvB, EcA, EcB), max(EvA, EvB, EcA, EcB)], color="0.6", lw=0.6, ls=":")
        # electron at lowest Ec, hole at highest Ev
        if EcA < EcB:
            ex_, ey = 1.15, EcA
        else:
            ex_, ey = 2.85, EcB
        if EvA > EvB:
            hx, hy = 1.15, EvA
        else:
            hx, hy = 2.85, EvB
        a.add_patch(Circle((ex_, ey + 0.13), 0.1, fc=INK, ec=INK))
        a.add_patch(Circle((hx, hy - 0.13), 0.1, fc="white", ec=INK, lw=1))
        a.text(0.1, 2.05, title, fontsize=8.5, weight="bold", va="top")
        a.text(0.1, 1.68, ex, fontsize=7.5, va="top", color="0.25")
        a.set_aspect("auto")
    fig.text(0.70, 0.035, "blue: narrow gap,  red: wide gap\n" + r"$\bullet$ electron   $\circ$ hole",
             fontsize=7.5, color="0.25", ha="left")
    save(fig, "34", "fig-34-1-band-alignment-types")


# ---------------------------------------------------------------- Figure 34.2
def _mb(f, b=0.384, nu=0.28):
    pref = b * (1 - nu * 0.25) / (8 * np.pi * abs(f) * (1 + nu) * 0.5)
    g = lambda h: h - pref * (np.log(h / b) + 1)
    return brentq(g, b * 1.0001 * np.e ** 0, 1e7) if pref > 0 else np.nan


def _mb_solve(f, b=0.384, nu=0.28):
    pref = (1 - nu * 0.25) / (8 * np.pi * abs(f) * (1 + nu) * 0.5)
    y = 30.0
    for _ in range(200):
        y = pref * (np.log(y) + 1)
    return y * b


def _pb_solve(f, b=0.4, nu=0.28, a=0.5431):
    k = (1 - nu) / (1 + nu) * b ** 2 / (16 * np.pi * np.sqrt(2) * a) / f ** 2
    h = 1e4
    with np.errstate(all="ignore"):
        for _ in range(300):
            h = k * np.log(h / b)
    return h if np.isfinite(h) and h > b else np.nan


def critical_thickness():
    fSiGe = (5.658 - 5.431) / 5.431
    f = np.logspace(-3, np.log10(0.05), 300)
    hmb = np.array([_mb_solve(v) for v in f])
    hpb = np.array([_pb_solve(v) for v in f])
    hpb = np.where(np.isfinite(hpb) & (f < 0.035), hpb, np.nan)
    fig, ax = new_fig(6.4, 4.4)
    lo, hi = 1, 1e4
    ax.fill_between(f, lo, hmb, color=GREEN, alpha=0.12, lw=0)
    ax.fill_between(f, hmb, np.minimum(np.where(np.isnan(hpb), hmb, hpb), hi), color=ORANGE, alpha=0.15, lw=0)
    ax.fill_between(f, np.minimum(np.where(np.isnan(hpb), hmb, hpb), hi), hi, color=RED, alpha=0.10, lw=0)
    ax.plot(f, hmb, color=INK, lw=1.9, label="Matthews–Blakeslee (equilibrium, 60° dislocations)")
    ax.plot(f, hpb, color=INK, lw=1.4, ls="--", label="People–Bean (metastable limit, low-T growth)")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1e-3, 0.05)
    ax.set_ylim(lo, hi)
    ax.set_xlabel(r"lattice mismatch $|f|$")
    ax.set_ylabel(r"critical thickness $h_c$ (nm)")
    ax.set_yticks([1, 10, 100, 1000, 10000])
    ax.set_yticklabels(["1 nm", "10 nm", "100 nm", "1 µm", "10 µm"])
    ax.set_xticks([1e-3, 2e-3, 5e-3, 1e-2, 2e-2, 5e-2])
    ax.set_xticklabels(["0.001", "0.002", "0.005", "0.01", "0.02", "0.05"])
    ax.xaxis.set_minor_formatter(plt.NullFormatter())
    sec = ax.secondary_xaxis("top", functions=(lambda v: v / fSiGe, lambda x: x * fSiGe))
    sec.set_xticks([0.025, 0.05, 0.1, 0.2, 0.5, 1.0])
    sec.set_xticklabels(["0.025", "0.05", "0.1", "0.2", "0.5", "1.0"])
    sec.xaxis.set_minor_formatter(plt.NullFormatter())
    sec.set_xlabel(r"Ge fraction $x$ in Si$_{1-x}$Ge$_x$ on Si(001)")
    ax.text(1.25e-3, 2.0, "stable\n(coherent)", fontsize=9, color="#1b6b50")
    ax.text(0.0105, 300, "metastable\n(kinetically limited)", fontsize=9, color="#8a5a00", ha="left")
    ax.text(0.012, 3500, "relaxed (misfit dislocations)", fontsize=9, color="#9c3a10", ha="left")
    # worked-example points
    for xg, mk in [(0.1, "o"), (0.2, "o"), (0.3, "o")]:
        fv = xg * fSiGe
        ax.plot(fv, _mb_solve(fv), mk, color=BLUE, ms=6, zorder=5)
    fv = 0.2 * fSiGe
    ax.annotate(r"Si$_{0.8}$Ge$_{0.2}$: $h_c\approx$" + f"{_mb_solve(fv):.1f} nm", xy=(fv, _mb_solve(fv)),
                xytext=(1.6e-3, 5.0), fontsize=8.5, color=BLUE,
                arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.8))
    fv = 0.1 * fSiGe
    ax.annotate(f"x = 0.1: {_mb_solve(fv):.0f} nm", xy=(fv, _mb_solve(fv)), xytext=(1.25e-3, 60),
                fontsize=8, color=BLUE, arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.8))
    fv = 0.3 * fSiGe
    ax.annotate(f"x = 0.3: {_mb_solve(fv):.0f} nm", xy=(fv, _mb_solve(fv)), xytext=(0.0048, 1.6),
                fontsize=8, color=BLUE, arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.8))
    # InGaAs on GaAs (b = a_GaAs/sqrt2 = 0.400 nm, nu = 0.31)
    fI = 0.0143
    hI = _mb_solve(fI, b=0.400, nu=0.31)
    ax.plot(fI, hI, "s", color=RED, ms=6, zorder=5)
    ax.annotate(r"In$_{0.2}$Ga$_{0.8}$As/GaAs" + f"\n$h_c\\approx${hI:.0f} nm", xy=(fI, hI), xytext=(0.0165, 1.15),
                fontsize=8.5, color=RED, arrowprops=dict(arrowstyle="-", color=RED, lw=0.8))
    # direct line labels, rotated to the on-screen slope
    fig.canvas.draw()
    for fx, curve, txt, off in [(1.5e-3, _mb_solve, "Matthews–Blakeslee (equilibrium, 60° dislocations)", 1.35),
                                (2.6e-3, _pb_solve, "People–Bean (metastable limit, low-T growth)", 0.62)]:
        p1 = ax.transData.transform((fx, curve(fx)))
        p2 = ax.transData.transform((fx * 1.3, curve(fx * 1.3)))
        ang = np.degrees(np.arctan2(p2[1] - p1[1], p2[0] - p1[0]))
        ax.text(fx, curve(fx) * off, txt, rotation=ang, rotation_mode="anchor", fontsize=8,
                ha="left", va="bottom" if off > 1 else "top", color=INK)
    save(fig, "34", "fig-34-2-critical-thickness")


# ---------------------------------------------------------------- Figure 34.3
def algan_gan_2deg():
    fig, (at, ab) = plt.subplots(2, 1, figsize=(6.4, 5.2), sharex=False,
                                 gridspec_kw=dict(height_ratios=[1.0, 2.3], hspace=0.12))
    d = 25.0
    XL = (-10, 100)
    # ---- layer stack
    at.set_xlim(*XL)
    at.set_ylim(0, 1)
    at.axis("off")
    at.add_patch(Rectangle((0, 0.02), d, 0.96, fc="#F3D9C6", ec=INK, lw=0.8))
    at.add_patch(Rectangle((d, 0.02), 100 - d, 0.96, fc="#DCE7F2", ec=INK, lw=0.8))
    at.text(d / 2, 0.93, "Al$_{0.3}$Ga$_{0.7}$N\nbarrier, 25 nm", ha="center", va="top", fontsize=8)
    at.text(65, 0.93, "GaN channel / buffer (Ga-face)", ha="center", va="top", fontsize=8)
    at.annotate("", xy=(22, 0.52), xytext=(4, 0.52),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.2, mutation_scale=12))
    at.text(13, 0.56, r"$P_{sp}+P_{pz}$", ha="center", va="bottom", fontsize=8.5, color=RED)
    at.annotate("", xy=(58, 0.52), xytext=(48, 0.52),
                arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.2, mutation_scale=12))
    at.text(53, 0.56, r"$P_{sp}$", ha="center", va="bottom", fontsize=8.5, color=BLUE)
    at.text(79, 0.52, "(arrows point toward substrate)", fontsize=7, color="0.35", ha="center", va="center")
    for yy in np.linspace(0.08, 0.32, 4):
        at.text(d - 1.3, yy, "+", color=RED, fontsize=9, ha="center", va="center", weight="bold")
        at.text(1.3, yy, "−", color=BLUE, fontsize=10, ha="center", va="center", weight="bold")
        at.text(-1.6, yy, "+", color=GREEN, fontsize=9, ha="center", va="center", weight="bold")
    at.text(d - 3.0, 0.20, r"$+\sigma_{\rm pol}$", fontsize=8, color=RED, va="center", ha="right")
    at.text(3.0, 0.20, r"$-\sigma_{\rm pol}$", fontsize=8, color=BLUE, va="center", ha="left")
    at.text(-3.0, 0.20, "surface\ndonors", fontsize=7, color=GREEN, ha="right", va="center")
    at.scatter(np.linspace(d + 2, d + 10, 6), [0.14] * 6, s=14, color=INK, zorder=5)
    at.text(d + 11.5, 0.14, r"2DEG ($-qn_s$)", fontsize=7.5, va="center")
    # ---- conduction band
    qPhiB, dEc = 1.23, 0.42
    Ec_int_gan, E0 = -0.40, -0.12
    Ec_int_bar = Ec_int_gan + dEc
    z1 = np.linspace(0, d, 100)
    Ec1 = qPhiB + (Ec_int_bar - qPhiB) * z1 / d
    z2 = np.linspace(d, 100, 4000)
    u = z2 - d
    F2deg = 1.602e-19 * 1e17 / (8.854e-12 * 9.5) * 1e-9         # V/nm, field of the 2DEG sheet
    zav = 2.6
    bb = 3 / zav
    Q = 1 - (1 + bb * u + (bb * u) ** 2 / 2) * np.exp(-bb * u)
    integ = np.cumsum(1 - Q) * (u[1] - u[0])
    Ec2 = Ec_int_gan + F2deg * integ + 0.008 * u
    for a in (ab,):
        a.plot(z1, Ec1, color=RED, lw=2)
        a.plot(z2, Ec2, color=BLUE, lw=2)
        a.plot([d, d], [Ec_int_bar, Ec_int_gan], color=INK, lw=2)
        a.axhline(0, color=INK, ls="--", lw=0.9)
    ab.text(99, 0.03, r"$E_F$", ha="right", va="bottom", fontsize=9)
    ab.annotate("", xy=(-2.5, qPhiB), xytext=(-2.5, 0),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.9, mutation_scale=8, color=INK, shrinkA=0, shrinkB=0))
    ab.text(1.5, 0.30, r"$q\Phi_B\approx1.2$ eV", fontsize=8.5)
    ab.annotate("", xy=(23.3, Ec_int_bar), xytext=(23.3, Ec_int_gan),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.9, mutation_scale=8, color=INK, shrinkA=0, shrinkB=0))
    ab.text(22, -0.25, r"$\Delta E_c\approx0.4$ eV", fontsize=8.5, ha="right", va="top")
    ab.text(9, 1.0, "linear slope: field\n" + r"set by $\sigma_{\rm pol}-qn_s$", fontsize=7.5, color=RED)
    ab.text(70, 0.72, "GaN conduction band", fontsize=8, color=BLUE)
    ab.set_ylim(-0.62, 1.45)
    ab.set_xlim(*XL)
    ab.set_xlabel("depth below surface (nm)")
    ab.set_ylabel(r"$E_c-E_F$ (eV)")
    ab.spines["left"].set_bounds(-0.6, 1.4)
    ab.spines["bottom"].set_bounds(0, 100)
    ab.set_xticks([0, 25, 50, 75, 100])
    # zoom on the triangular well
    ins = ab.inset_axes([0.56, 0.12, 0.33, 0.40])
    ins.plot(z2, Ec2, color=BLUE, lw=1.8)
    ins.plot([d, d], [Ec_int_bar, Ec_int_gan], color=INK, lw=1.8)
    ins.plot(z1, Ec1, color=RED, lw=1.8)
    ins.axhline(0, color=INK, ls="--", lw=0.8)
    zE0 = z2[Ec2 <= E0].max()
    ins.plot([d, zE0], [E0, E0], color=GREEN, lw=1.3)
    ins.text(zE0 + 0.3, E0, r"$E_0$", color=GREEN, fontsize=8, va="center")
    psi2 = (bb ** 3 / 2) * u ** 2 * np.exp(-bb * u)
    m = u < 12
    ins.fill_between(z2[m], -0.48, -0.48 + 0.2 * psi2[m] / psi2.max(), color=BLUE, alpha=0.3, lw=0)
    ins.text(d + 4.5, -0.40, r"$n(z)$, $n_s\approx1\times10^{13}$ cm$^{-2}$", fontsize=7, color=BLUE, va="center")
    ins.set_xlim(22, 36)
    ins.set_ylim(-0.49, 0.3)
    ins.set_xticks([25, 30, 35])
    ins.set_yticks([-0.2, 0, 0.2])
    ins.tick_params(labelsize=7)
    for sp in ins.spines.values():
        sp.set_visible(True)
        sp.set_color("0.5")
    ab.indicate_inset_zoom(ins, edgecolor="0.5", lw=0.6)
    save(fig, "34", "fig-34-3-algan-gan-2deg")


# ---------------------------------------------------------------- Figure 34.4
def _grain_sketch(ax, zone, rng):
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.2, 8.8)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(Rectangle((0, -1.0), 10, 1.0, fc="0.75", ec=INK, lw=0.6))
    ax.text(5, -0.5, "substrate", ha="center", va="center", fontsize=6.5)
    fc = "#E7EEF6"
    if zone == "1":
        xs = np.linspace(0.6, 9.4, 6)
        for x0 in xs:
            wb, wt = 0.35, 1.45
            hgt = 6.2 + rng.uniform(-0.6, 0.6)
            th = np.linspace(0, np.pi, 30)
            top = [(x0 + wt / 2 * np.cos(t), hgt + 0.55 * np.sin(t)) for t in th]
            pts = [(x0 - wb / 2, 0), (x0 + wb / 2, 0), (x0 + wt / 2, hgt)] + top[1:-1] + [(x0 - wt / 2, hgt)]
            ax.add_patch(Polygon(pts, closed=True, fc=fc, ec=INK, lw=0.7))
    elif zone == "T":
        x = 0
        while x < 10:
            w = rng.uniform(0.35, 0.6)
            ax.add_patch(Rectangle((x, 0), min(w, 10 - x), 6.6, fc=fc, ec=INK, lw=0.5))
            x += w
    elif zone == "2":
        edges = np.array([0, 2.4, 4.6, 7.3, 10])
        for x0, x1 in zip(edges[:-1], edges[1:]):
            xm = (x0 + x1) / 2
            pts = [(x0, 0), (x1, 0), (x1, 6.3), (xm, 7.3), (x0, 6.3)]
            ax.add_patch(Polygon(pts, closed=True, fc=fc, ec=INK, lw=0.8))
    else:
        pts = np.column_stack([rng.uniform(-2, 12, 60), rng.uniform(-2, 9, 60)])
        vor = Voronoi(pts)
        from matplotlib.path import Path as MPath
        ax.add_patch(Rectangle((0, 0), 10, 6.6, fc=fc, ec=INK, lw=0.8))
        clip = Rectangle((0, 0), 10, 6.6, transform=ax.transData)
        for (p, q) in vor.ridge_vertices:
            if p >= 0 and q >= 0:
                v = vor.vertices[[p, q]]
                ln, = ax.plot(v[:, 0], v[:, 1], color=INK, lw=0.7)
                ln.set_clip_path(clip)


def structure_zone_model():
    fig = plt.figure(figsize=(6.8, 5.0))
    gs = fig.add_gridspec(2, 4, height_ratios=[1.0, 1.55], hspace=0.12, wspace=0.08)
    rng = np.random.default_rng(3)
    names = [("1", "Zone 1\ntapered columns, voids"), ("T", "Zone T\ndense fibrous"),
             ("2", "Zone 2\ncolumnar, faceted"), ("3", "Zone 3\nequiaxed, recrystallized")]
    for k, (z, lab) in enumerate(names):
        a = fig.add_subplot(gs[0, k])
        _grain_sketch(a, z, rng)
        a.set_title(lab, fontsize=8.5, pad=2)
    ax = fig.add_subplot(gs[1, :3])
    p = np.logspace(-1, np.log10(4), 100)
    s = np.log10(p / 0.1) / np.log10(40)
    b1 = 0.15 + 0.17 * s
    bT = 0.35 + 0.05 * s
    b2 = 0.50 + 0.05 * s
    ax.fill_betweenx(p, 0.1, b1, color=RED, alpha=0.13, lw=0)
    ax.fill_betweenx(p, b1, bT, color=ORANGE, alpha=0.18, lw=0)
    ax.fill_betweenx(p, bT, b2, color=GREEN, alpha=0.15, lw=0)
    ax.fill_betweenx(p, b2, 0.9, color=BLUE, alpha=0.12, lw=0)
    for bnd in (b1, bT, b2):
        ax.plot(bnd, p, color=INK, lw=0.8)
    ax.set_yscale("log")
    ax.set_xlim(0.1, 0.9)
    ax.set_ylim(0.1, 4)
    ax.set_yticks([0.1, 0.3, 1, 4])
    ax.set_yticklabels(["0.1", "0.3", "1", "4"])
    ax.set_xlabel(r"homologous substrate temperature $T_s/T_m$")
    ax.set_ylabel("sputter-gas pressure (Pa)")
    for xx, yy, t in [(0.18, 1.6, "1"), (0.27, 0.15, "T"), (0.46, 1.6, "2"), (0.72, 1.3, "3")]:
        ax.text(xx, yy, "Zone " + t, ha="center", fontsize=9, weight="bold")
    for nm, val, yy, ha in [("W", 0.18, 0.55, "left"), ("TiN", 0.21, 0.36, "left"),
                            ("Cu", 0.50, 0.45, "left"), ("Al", 0.72, 0.45, "left")]:
        ax.plot([val, val], [0.1, yy], color=INK, lw=0.9, ls=":")
        ax.plot(val, 0.1, marker="v", color=INK, ms=6, clip_on=False, zorder=5)
        ax.text(val + (0.006 if ha == "left" else -0.006), yy, f"{nm} ({val:.2f})", ha=ha, fontsize=8,
                va="center", bbox=dict(fc="white", ec="none", pad=0.6, alpha=0.85))
    ax.yaxis.set_minor_formatter(plt.NullFormatter())
    ax.text(0.6, 2.6, "▼ films deposited\n    at $T_s=400$ °C", fontsize=7.5, ha="left", color="0.25")
    # inset: bamboo vs polycrystalline line (top view)
    ai = fig.add_subplot(gs[1, 3])
    ai.set_xlim(0, 10)
    ai.set_ylim(0, 10)
    ai.axis("off")
    # bamboo line
    y0, h = 6.1, 1.2
    ai.add_patch(Rectangle((0.3, y0), 9.4, h, fc="#F3D9C6", ec=INK, lw=0.8))
    for xb in [1.9, 3.6, 5.0, 6.9, 8.4]:
        ai.plot([xb, xb + rng.uniform(-0.3, 0.3)], [y0, y0 + h], color=INK, lw=0.8)
    ai.text(5, y0 + h + 0.35, "bamboo line\n(boundaries cross width)", ha="center", va="bottom", fontsize=7)
    # polycrystalline line
    y1, h1 = 1.4, 2.4
    ai.add_patch(Rectangle((0.3, y1), 9.4, h1, fc="#F3D9C6", ec=INK, lw=0.8))
    pts = np.column_stack([rng.uniform(0, 10, 40), rng.uniform(y1 - 1, y1 + h1 + 1, 40)])
    vor = Voronoi(pts)
    clip = Rectangle((0.3, y1), 9.4, h1, transform=ai.transData)
    for (pp, qq) in vor.ridge_vertices:
        if pp >= 0 and qq >= 0:
            v = vor.vertices[[pp, qq]]
            ln, = ai.plot(v[:, 0], v[:, 1], color=INK, lw=0.6)
            ln.set_clip_path(clip)
    ai.text(5, y1 + h1 + 0.35, "polycrystalline line\n(boundaries along line)", ha="center", va="bottom", fontsize=7)
    ai.annotate("", xy=(9.7, 0.6), xytext=(0.3, 0.6), arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK))
    ai.text(5, 0.25, "current", ha="center", va="top", fontsize=7)
    save(fig, "34", "fig-34-4-structure-zone-model")


# ---------------------------------------------------------------- Figure 34.5
def barrier_vs_workfunction():
    phim = np.array([4.28, 4.33, 4.55, 5.15, 5.10, 5.65])
    metals = ["Al", "Ti", "W", "Ni", "Au", "Pt"]
    data = {   # Table 13.4; CNL-predicted pinning level E_g - phi_CNL (Tersoff/Robertson CNLs)
        "n-Si": (np.array([0.72, 0.55, 0.67, 0.64, 0.80, 0.875]), BLUE, "o", 0.76, -0.012, 0.70),
        "n-GaAs": (np.array([0.80, 0.83, 0.80, 0.84, 0.90, 0.86]), RED, "s", 0.92, 0.0, 0.95),
        "n-GaN": (np.array([0.60, 0.55, 0.70, 1.00, 1.00, 1.10]), GREEN, "^", 1.03, 0.012, 1.25),
    }
    fig, ax = new_fig(6.4, 4.4)
    x = np.linspace(4.0, 5.8, 50)
    ax.plot(x, x - 4.05, color=INK, ls="--", lw=1.2)
    ax.text(5.52, 1.66, "Schottky–Mott limit, Si\n" + r"$\phi_{Bn}=\phi_m-\chi_{\rm Si}$  ($S=1$)",
            fontsize=8, ha="right", va="center")
    for name, (phiB, c, mk, cnl, jit, ylab) in data.items():
        S, c0 = np.polyfit(phim, phiB, 1)
        ax.plot(phim + jit, phiB, mk, color=c, ms=6, mec="white", mew=0.5, zorder=5)
        ax.plot(x, S * x + c0, color=c, lw=1.5)
        ax.axhline(cnl, color=c, ls=":", lw=1.0)
        ax.text(5.82, ylab, f"{name}\n$S\\approx{S:.2f}$", color=c, fontsize=8, va="center", ha="left")
    for m, pm in zip(metals, phim):
        ax.text(pm, 0.03, m, ha="center", fontsize=8, color="0.3")
        ax.plot([pm, pm], [0.12, 0.4], color="0.8", lw=0.6)
    ax.text(4.02, 1.06, "dotted: CNL-predicted pinning levels", fontsize=7.5, color="0.35", va="bottom")
    ax.set_xlim(4.0, 5.8)
    ax.set_ylim(0, 1.8)
    ax.set_xlabel(r"metal work function $\phi_m$ (eV)")
    ax.set_ylabel(r"electron barrier height $\phi_{Bn}$ (eV)")
    # inset: MIGS band diagram
    ins = ax.inset_axes([0.025, 0.63, 0.36, 0.36])
    ins.set_xlim(0, 10)
    ins.set_ylim(0, 6)
    ins.set_xticks([])
    ins.set_yticks([])
    for sp in ins.spines.values():
        sp.set_visible(True)
        sp.set_color("0.5")
        sp.set_linewidth(0.6)
    EF, Ec0, Eci, Eg = 2.8, 3.15, 4.6, 2.0
    ins.add_patch(Rectangle((0, 0.6), 3, EF - 0.6, fc="0.82", ec="none"))
    ins.text(1.5, 1.7, "metal", ha="center", fontsize=7)
    xs = np.linspace(3, 10, 200)
    Ec = Ec0 + (Eci - Ec0) * np.clip(1 - (xs - 3) / 4.5, 0, 1) ** 2
    ins.plot(xs, Ec, color=BLUE, lw=1.4)
    ins.plot(xs, Ec - Eg, color=BLUE, lw=1.4)
    ins.plot([0, 10], [EF, EF], color=INK, ls="--", lw=0.8)
    ins.text(9.9, EF - 0.1, r"$E_F$", fontsize=7, ha="right", va="top")
    for k in range(12):
        x0 = 3 + k * 0.12
        ins.add_patch(Rectangle((x0, Eci - Eg + 0.05), 0.12, Eg - 0.1, fc=PINK, ec="none",
                                alpha=0.55 * np.exp(-k / 3.5)))
    ins.text(4.7, 3.25, "MIGS", color=PINK, fontsize=7.5, weight="bold", va="center")
    ins.annotate("", xy=(3.25, Eci), xytext=(3.25, EF),
                 arrowprops=dict(arrowstyle="<|-|>", lw=0.7, mutation_scale=6, color=INK, shrinkA=0, shrinkB=0))
    ins.text(3.45, 5.3, r"$\phi_{Bn}$", fontsize=7.5, va="center")
    ins.text(2.65, 0.25, "−", fontsize=9, ha="center", va="center")
    ins.text(3.35, 0.25, "+", fontsize=9, ha="center", va="center")
    ins.text(4.0, 0.25, "interface dipole", fontsize=6.5, va="center")
    save(fig, "34", "fig-34-5-barrier-vs-workfunction")


# ---------------------------------------------------------------- Figure 34.6
def highk_band_offsets():
    names = ["SiO$_2$", "Al$_2$O$_3$", "Si$_3$N$_4$", "HfO$_2$", "ZrO$_2$", "La$_2$O$_3$",
             "Ta$_2$O$_5$", "TiO$_2$", "SrTiO$_3$"]
    k = np.array([3.9, 9, 7, 22, 25, 30, 24, 60, 200])
    Eg = np.array([8.9, 8.8, 5.3, 5.8, 5.8, 6.0, 4.4, 3.2, 3.2])
    cbo = np.array([3.1, 2.8, 2.4, 1.5, 1.4, 2.3, 0.35, 0.0, 0.0])
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.8, 4.0), gridspec_kw=dict(width_ratios=[1, 1.25], wspace=0.32))
    kk = np.logspace(np.log10(3), np.log10(300), 100)
    a1.plot(kk, 18 / np.sqrt(kk), color="0.55", ls="--", lw=1)
    a1.text(140, 18 / np.sqrt(140) + 0.35, r"$E_g\propto k^{-1/2}$", color="0.4", fontsize=8, ha="center", va="bottom")
    good = cbo >= 1.0
    a1.scatter(k[good], Eg[good], color=BLUE, s=28, zorder=5, label=r"CB offset $\geq$ 1 eV")
    a1.scatter(k[~good], Eg[~good], color=RED, s=28, marker="s", zorder=5, label=r"CB offset $<$ 1 eV")
    offs = {"SiO$_2$": (4, 3), "Al$_2$O$_3$": (5, 3), "Si$_3$N$_4$": (-4, -10), "HfO$_2$": (-30, 5),
            "ZrO$_2$": (4, -10), "La$_2$O$_3$": (5, 3), "Ta$_2$O$_5$": (-8, -11), "TiO$_2$": (-12, 6),
            "SrTiO$_3$": (-30, 6)}
    for n, kv, e in zip(names, k, Eg):
        dx, dy = offs[n]
        a1.annotate(n, (kv, e), xytext=(dx, dy), textcoords="offset points", fontsize=7.5)
    a1.set_xscale("log")
    a1.set_xlim(3, 300)
    a1.set_ylim(0, 10)
    a1.set_xticks([3, 10, 30, 100, 300])
    a1.set_xticklabels(["3", "10", "30", "100", "300"])
    a1.set_xlabel("dielectric constant $k$")
    a1.set_ylabel("band gap $E_g$ (eV)")
    a1.legend(loc="lower left", fontsize=7.5)
    # right: band offsets
    EgSi = 1.12
    xpos = np.arange(len(names))
    a2.axhspan(EgSi, EgSi + 1.0, color=GREEN, alpha=0.15, lw=0)
    a2.text(4, -5.25, "shaded: minimum 1 eV barrier for low leakage", fontsize=7.5, color="#1b6b50",
            ha="center", va="center")
    a2.axhline(EgSi, color=INK, lw=0.9)
    a2.axhline(0, color=INK, lw=0.9)
    tw = a2.twinx()
    tw.set_ylim(-5.6, 5.0)
    tw.set_yticks([0, EgSi])
    tw.set_yticklabels([r"$E_v$(Si)", r"$E_c$(Si)"], fontsize=8)
    tw.spines["right"].set_visible(True)
    for i, (e, c) in enumerate(zip(Eg, cbo)):
        top = EgSi + c
        bot = top - e
        col = BLUE if c >= 1.0 else RED
        a2.add_patch(Rectangle((i - 0.32, bot), 0.64, e, fc=col, alpha=0.25, ec=col, lw=1))
        a2.text(i, top + 0.12, f"{c:g}", ha="center", va="bottom", fontsize=7.5, color=col)
    a2.set_xticks(xpos)
    a2.set_xticklabels(names, rotation=55, ha="right", fontsize=7.5)
    a2.set_xlim(-0.6, len(names) - 0.4)
    a2.set_ylim(-5.6, 5.0)
    a2.set_ylabel("energy relative to Si $E_v$ (eV)")
    a2.text(4, 4.65, "numbers: CB offset to Si (eV)", ha="center", fontsize=7.5, color="0.3")
    save(fig, "34", "fig-34-6-highk-band-offsets")


if __name__ == "__main__":
    for xg in (0.1, 0.2, 0.3):
        print(f"MB h_c(x={xg}) = {_mb_solve(xg * 0.0418):.1f} nm, PB = {_pb_solve(xg * 0.0418):.0f} nm")
    print("InGaAs h_c =", _mb_solve(0.0143, b=0.400, nu=0.31), _mb_solve(0.0143))
    band_alignment_types()
    critical_thickness()
    algan_gan_2deg()
    structure_zone_model()
    barrier_vs_workfunction()
    highk_band_offsets()
