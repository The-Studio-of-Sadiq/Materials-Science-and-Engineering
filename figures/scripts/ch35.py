"""Figures for Chapter 35 — Electronic and Optoelectronic Materials.

Run from the repository root:  python figures/scripts/ch35.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq

BLUE, RED, GREEN, PINK, ORANGE, SKY, YEL = COLORS[:7]
HC = 1.23984  # eV um


def _loginterp(E_pts, a_pts):
    f = PchipInterpolator(np.asarray(E_pts), np.log10(a_pts))
    return lambda E: 10 ** f(E)


# ------------------------------------------------------------ absorption data
# Si: Green (2008) tabulated alpha(lambda), 300 K
_si_nm = np.array([300, 350, 370, 380, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950,
                   1000, 1050, 1100, 1150, 1200])
_si_a = np.array([1.73e6, 1.04e6, 6.9e5, 2.9e5, 9.52e4, 2.55e4, 1.11e4, 6.39e3, 4.14e3, 2.81e3, 1.90e3,
                  1.30e3, 8.5e2, 5.35e2, 3.06e2, 1.57e2, 64, 16.3, 3.5, 0.22, 0.022])
alpha_Si = _loginterp(HC / (_si_nm[::-1] * 1e-3), _si_a[::-1])
# Ge: indirect foot from 0.66 eV, direct edge at 0.80 eV (values consistent with Table 14.1)
alpha_Ge = _loginterp([0.62, 0.66, 0.70, 0.75, 0.78, 0.795, 0.80, 0.81, 0.83, 0.87, 0.946, 1.1, 1.3, 1.6,
                       2.0, 2.3, 2.7, 3.2, 3.6],
                      [0.05, 1.0, 10, 40, 80, 200, 460, 1.5e3, 3.0e3, 4.8e3, 7e3, 1.0e4, 1.6e4, 4.5e4,
                       1.6e5, 4.5e5, 6.5e5, 1.0e6, 1.4e6])
# GaAs: Urbach tail (E_U = 6 meV) below 1.42 eV
alpha_GaAs = _loginterp([1.30, 1.36, 1.38, 1.40, 1.42, 1.43, 1.46, 1.55, 1.7, 1.9, 2.1, 2.5, 2.9, 3.1, 3.6],
                        [5e-6 * 0 + 5e3 * np.exp(-0.12 / 0.006), 5e3 * np.exp(-0.06 / 0.006),
                         5e3 * np.exp(-0.04 / 0.006), 5e3 * np.exp(-0.02 / 0.006), 5e3, 8e3,
                         1.0e4, 1.2e4, 1.6e4, 2.5e4, 5e4, 1.0e5, 4e5, 7e5, 8e5])
# In0.53Ga0.47As: direct edge 0.75 eV
alpha_InGaAs = _loginterp([0.66, 0.70, 0.72, 0.74, 0.75, 0.76, 0.80, 0.95, 1.24, 1.6, 2.0, 2.5, 3.0, 3.6],
                          [3e3 * np.exp(-0.09 / 0.008), 3e3 * np.exp(-0.05 / 0.008), 3e3 * np.exp(-0.03 / 0.008),
                           3e3 * np.exp(-0.01 / 0.008), 3e3, 4.5e3, 7e3, 1.1e4, 1.7e4, 3e4, 6e4, 1.5e5, 3e5, 6e5])


def alpha_aSi(E):
    """a-Si:H: Tauc edge (B = 700 (cm eV)^-1/2, E_T = 1.75 eV) + Urbach tail E_U = 50 meV + defect floor."""
    E = np.asarray(E, float)
    ET, B, EU = 1.75, 700.0, 0.050
    tauc = np.where(E > ET, (B * (E - ET)) ** 2 / E, 0.0)
    Ej = 1.85                                  # join point (slopes match)
    aj = (B * (Ej - ET)) ** 2 / Ej
    urb = aj * np.exp((E - Ej) / EU)
    defect = 1.5
    return np.where(E >= Ej, tauc, urb) + defect + 0.0


# ---------------------------------------------------------------- Figure 35.1
def absorption_coefficient():
    fig, ax = new_fig(6.6, 4.6)
    E = np.linspace(0.6, 3.5, 1500)
    curves = [("Si", alpha_Si, BLUE, 1.10), ("Ge", alpha_Ge, RED, 0.64), ("GaAs", alpha_GaAs, GREEN, 1.33),
              ("In$_{0.53}$Ga$_{0.47}$As", alpha_InGaAs, PINK, 0.665), ("a-Si:H", alpha_aSi, ORANGE, 1.2)]
    for nm, f, c, Emin in curves:
        m = E >= Emin
        ax.plot(E[m], f(E[m]), color=c, lw=1.8, label=nm)
    ax.set_yscale("log")
    ax.set_xlim(0.6, 3.5)
    ax.set_ylim(1, 1e6)
    ax.set_xlabel("photon energy (eV)")
    ax.set_ylabel(r"absorption coefficient $\alpha$ (cm$^{-1}$)")
    # direct labels
    lab = [("Si", 2.0, 2.2e3, BLUE), ("Ge", 1.03, 3.5e3, RED), ("GaAs", 1.47, 4.0e3, GREEN),
           ("In$_{0.53}$Ga$_{0.47}$As", 0.62, 3e4, PINK), ("a-Si:H", 1.62, 4, ORANGE)]
    for t, x, y, c in lab:
        ax.text(x, y, t, color=c, fontsize=8.5, weight="bold")
    ax.annotate("", xy=(0.80, 460), xytext=(0.80, 40),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=0.8, mutation_scale=7))
    ax.text(0.815, 90, "direct\nedge", color=RED, fontsize=7, va="center")
    # top: wavelength
    top = ax.secondary_xaxis("top", functions=(lambda e: HC * 1e3 / np.maximum(e, 1e-3),
                                               lambda l: HC * 1e3 / np.maximum(l, 1e-3)))
    top.set_xticks([2000, 1550, 1310, 1000, 850, 600, 400])
    top.set_xticklabels(["2000", "1550", "1310", "1000", "850", "600", "400"], fontsize=7.5, rotation=45, ha="left")
    top.xaxis.set_minor_locator(plt.NullLocator())
    top.set_xlabel("wavelength (nm)")
    # right: penetration depth
    rt = ax.secondary_yaxis("right", functions=(lambda a: 1 / np.maximum(a, 1e-12), lambda d: 1 / np.maximum(d, 1e-12)))
    rt.set_yticks([1, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6])
    rt.set_yticklabels(["10 mm", "1 mm", "100 µm", "10 µm", "1 µm", "100 nm", "10 nm"])
    rt.set_ylabel(r"penetration depth $1/\alpha$")
    # inset Urbach tails
    ins = ax.inset_axes([0.62, 0.15, 0.35, 0.32])
    d = np.linspace(-0.15, 0.0, 100)
    ins.plot(d * 1e3, 5e3 * np.exp(d / 0.006), color=GREEN, lw=1.5)
    ins.plot(d * 1e3, 5e3 * np.exp(d / 0.050), color=ORANGE, lw=1.5)
    ins.set_yscale("log")
    ins.set_ylim(1, 1e4)
    ins.set_xlim(-150, 0)
    ins.tick_params(labelsize=7)
    ins.set_xlabel(r"$E-E_{\rm edge}$ (meV)", fontsize=7, labelpad=1)
    ins.set_ylabel(r"$\alpha$ (cm$^{-1}$)", fontsize=7, labelpad=1)
    ins.text(-40, 8, "GaAs\n$E_U\\approx6$ meV", color=GREEN, fontsize=7, ha="right")
    ins.text(-145, 1500, "a-Si:H\n$E_U\\approx50$ meV", color=ORANGE, fontsize=7)
    ins.text(-60, 400, r"slope $=1/E_U$", fontsize=7, ha="center", va="top")
    ins.set_facecolor("white")
    save(fig, "35", "fig-35-1-absorption-coefficient")


# ---------------------------------------------------------------- Figure 35.2
# 300 K parameters (Vurgaftman et al. 2001): a (A), E_Gamma, E_X, E_L (eV)
BIN = {
    "GaAs": (5.6533, 1.422, 1.900, 1.708), "AlAs": (5.6611, 3.003, 2.164, 2.352),
    "GaP": (5.4505, 2.780, 2.261, 2.635), "AlP": (5.4672, 3.630, 2.505, 3.570),
    "InP": (5.8697, 1.344, 2.384, 2.014), "InAs": (6.0583, 0.354, 1.370, 1.070),
    "GaSb": (6.0959, 0.727, 1.033, 0.753), "AlSb": (6.1355, 2.300, 1.615, 2.211),
    "InSb": (6.4794, 0.174, 0.630, 0.930),
}
# bowing (Gamma, X, L) for alloy A_x B_(1-x)
BOW = {("AlAs", "GaAs"): (0.37, 0.055, 0.0), ("InAs", "GaAs"): (0.477, 1.4, 0.33),
       ("InP", "GaP"): (0.65, 0.20, 1.03), ("GaAs", "GaP"): (0.19, 0.24, 0.16),
       ("InAs", "InP"): (0.10, 0.27, 0.27), ("InAs", "AlAs"): (0.70, 0.0, 0.0),
       ("InSb", "GaSb"): (0.415, 0.33, 0.4), ("InSb", "InAs"): (0.67, 0.6, 0.6),
       ("AlSb", "GaSb"): (0.47, 0.0, 0.0), ("GaSb", "GaAs"): (1.43, 1.2, 1.2)}


def _alloy(A, B, n=200):
    x = np.linspace(0, 1, n)
    aA, *gA = BIN[A]
    aB, *gB = BIN[B]
    bw = BOW[(A, B)]
    a = x * aA + (1 - x) * aB
    gaps = [x * gA[i] + (1 - x) * gB[i] - bw[i] * x * (1 - x) for i in range(3)]
    Eg = np.min(gaps, axis=0)
    direct = gaps[0] <= np.minimum(gaps[1], gaps[2])
    return a, Eg, direct


def _plot_alloy(ax, a, Eg, direct, color):
    # split into runs of constant directness
    idx = np.flatnonzero(np.diff(direct.astype(int))) + 1
    starts = np.r_[0, idx]
    ends = np.r_[idx, len(a)]
    for s, e in zip(starts, ends):
        sl = slice(max(s - 1, 0), e)
        ax.plot(a[sl], Eg[sl], color=color, lw=1.3, ls="-" if direct[s] else "--")


def bandgap_lattice_map():
    fig = plt.figure(figsize=(6.8, 5.0))
    gs = fig.add_gridspec(1, 2, width_ratios=[1, 3.3], wspace=0.06)
    axn = fig.add_subplot(gs[0, 0])
    ax = fig.add_subplot(gs[0, 1], sharey=axn)
    ylo, yhi = -0.45, 6.4
    for a_ in (ax, axn):
        a_.axhspan(1.65, 3.1, color="#FFE9A8", alpha=0.0)
        # visible spectrum as coloured strips
        from matplotlib.colors import hsv_to_rgb
        for E0 in np.linspace(1.65, 3.1, 60):
            lam = HC * 1e3 / E0
            hue = np.interp(lam, [400, 450, 490, 530, 580, 620, 700], [0.78, 0.66, 0.5, 0.33, 0.16, 0.05, 0.0])
            a_.axhspan(E0, E0 + 1.6 / 60, color=hsv_to_rgb([hue, 0.35, 1.0]), lw=0, zorder=0)
        a_.axhline(0, color="0.6", lw=0.6)
    # cubic alloys
    alloys = [(("AlAs", "GaAs"), BLUE), (("InAs", "GaAs"), BLUE), (("InP", "GaP"), GREEN),
              (("GaAs", "GaP"), GREEN), (("InAs", "InP"), PINK), (("InAs", "AlAs"), PINK),
              (("InSb", "GaSb"), ORANGE), (("InSb", "InAs"), ORANGE), (("AlSb", "GaSb"), ORANGE)]
    for (A, B), c in alloys:
        _plot_alloy(ax, *_alloy(A, B), c)
    # Si-Ge (indirect)
    x = np.linspace(0, 1, 100)
    EgSiGe = np.where(x < 0.85, 1.12 - 0.41 * x + 0.008 * x ** 2, 1.97 - 1.31 * x)
    EgSiGe = np.minimum(EgSiGe, 1.12 - 0.41 * x + 0.008 * x ** 2)
    ax.plot(5.431 + 0.227 * x, np.where(x < 0.85, 1.12 - 0.41 * x + 0.008 * x ** 2, 1.97 - 1.31 * x),
            color="0.45", lw=1.3, ls="--")
    # HgCdTe (Hansen et al., 300 K), x = Cd fraction
    xc = np.linspace(0, 1, 100)
    T = 300
    Eh = -0.302 + 1.93 * xc - 0.81 * xc ** 2 + 0.832 * xc ** 3 + 5.35e-4 * T * (1 - 2 * xc)
    ax.plot(6.461 + 0.020 * xc, Eh, color=RED, lw=1.6)
    ax.text(6.44, 0.8, "HgCdTe", color=RED, fontsize=8, ha="right", rotation=90, va="center")
    pts = {"Si": (5.431, 1.12, False), "Ge": (5.658, 0.66, False), "GaP": (5.4505, 2.26, False),
           "GaAs": (5.6533, 1.42, True), "AlAs": (5.6611, 2.16, False), "InP": (5.8697, 1.34, True),
           "InAs": (6.0583, 0.354, True), "GaSb": (6.0959, 0.727, True), "AlSb": (6.1355, 1.62, False),
           "InSb": (6.4794, 0.17, True), "CdTe": (6.481, 1.50, True), "ZnSe": (5.668, 2.70, True),
           "HgTe": (6.461, -0.30, True)}
    offs = {"Si": (-4, -11), "Ge": (5, -3), "GaP": (5, 2), "GaAs": (5, -9), "AlAs": (6, -2), "InP": (5, -10),
            "InAs": (-4, -12), "GaSb": (4, 3), "AlSb": (5, 2), "InSb": (-26, -3), "CdTe": (-30, 3),
            "ZnSe": (6, 0), "HgTe": (-36, -4)}
    for nm, (a, e, dr) in pts.items():
        ax.plot(a, e, "o", ms=5.5, mfc=INK if dr else "white", mec=INK, zorder=6)
        ax.annotate(nm, (a, e), xytext=offs[nm], textcoords="offset points", fontsize=8, zorder=7)
    # substrate lines
    for a0, txt, ha, dx in [(5.6533, "AlGaAs, AlGaInP\non GaAs", "right", -0.008),
                            (5.8697, "InGaAsP, InGaAs,\nInAlAs on InP", "left", 0.008)]:
        ax.axvline(a0, color="0.35", ls=":", lw=1.0, zorder=1)
        ax.text(a0 + dx, 5.5, txt, fontsize=7.5, va="center", ha=ha)
    # application annotations
    ax.plot([5.6533] * 2, [1.9, 2.1], color=RED, lw=4, solid_capstyle="butt", zorder=5, alpha=0.8)
    ax.annotate("AlGaInP\nred/amber", (5.648, 2.05), xytext=(5.42, 3.55), fontsize=7.5, color=RED,
                va="center", arrowprops=dict(arrowstyle="-", color=RED, lw=0.7))
    for E in (0.95, 0.80):
        ax.plot(5.8697, E, "D", ms=4.5, color=PINK, zorder=7)
        ax.annotate("", (5.8697, E), xytext=(5.905, 1.58), arrowprops=dict(arrowstyle="-", color=PINK, lw=0.7))
    ax.text(5.90, 1.68, "InGaAsP\n1.3 / 1.55 µm", fontsize=7.5, color=PINK, va="bottom")
    ax.set_xlim(5.38, 6.55)
    ax.set_ylim(ylo, yhi)
    ax.set_xlabel(r"lattice constant $a$ (Å), cubic")
    plt.setp(ax.get_yticklabels(), visible=False)
    ax.text(5.40, 6.25, "solid: direct gap, dashed: indirect gap\nfilled/open: direct/indirect binary",
            fontsize=7, color="0.3", va="top", zorder=8, bbox=dict(fc="white", ec="none", pad=1))
    # right axis: wavelength
    rt = ax.secondary_yaxis("right", functions=(lambda e: e, lambda e: e))
    lam = np.array([0.25, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.55, 3.0])
    rt.set_yticks(HC / lam)
    rt.set_yticklabels([f"{l:g}" for l in lam], fontsize=8)
    rt.set_ylabel("wavelength (µm)")
    # nitrides (wurtzite a)
    N = {"AlN": (3.112, 6.10), "GaN": (3.189, 3.42), "InN": (3.545, 0.65)}
    for (A, B, b, c) in [("InN", "GaN", 1.4, BLUE), ("GaN", "AlN", 1.0, GREEN), ("InN", "AlN", 4.0, "0.5")]:
        x = np.linspace(0, 1, 200)
        a = x * N[A][0] + (1 - x) * N[B][0]
        Eg = x * N[A][1] + (1 - x) * N[B][1] - b * x * (1 - x)
        axn.plot(a, Eg, color=c, lw=1.3)
    for nm, (a, e) in N.items():
        axn.plot(a, e, "o", ms=5.5, color=INK, zorder=6)
    axn.annotate("AlN", N["AlN"], xytext=(6, -2), textcoords="offset points", fontsize=8)
    axn.annotate("GaN", N["GaN"], xytext=(6, -3), textcoords="offset points", fontsize=8)
    axn.annotate("InN", N["InN"], xytext=(-22, 4), textcoords="offset points", fontsize=8)
    for lamnm, col in [(450, BLUE), (530, GREEN)]:
        Et = HC * 1e3 / lamnm
        xin = brentq(lambda x: x * 0.65 + (1 - x) * 3.42 - 1.4 * x * (1 - x) - Et, 0, 1)
        an = xin * 3.545 + (1 - xin) * 3.189
        axn.plot(an, Et, "*", ms=9, color=col, mec=INK, mew=0.4, zorder=7)
        axn.text(an + 0.02, Et, f"InGaN\n{lamnm} nm", fontsize=7, color=INK, va="center")
    axn.set_xlim(3.08, 3.6)
    axn.set_xticks([3.1, 3.3, 3.5])
    axn.set_xlabel("a (Å), wurtzite")
    axn.set_ylabel("band gap (eV)")
    axn.set_title("III-nitrides", fontsize=9)
    save(fig, "35", "fig-35-2-bandgap-lattice-map")


# ---------------------------------------------------------------- Figure 35.3
def droop_and_green_gap():
    q = 1.602e-19
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.8, 3.9), gridspec_kw=dict(wspace=0.42))
    n = np.logspace(16, 20.5, 600)
    for A, B, C, d, ls, lab, c in [(1e7, 1e-11, 1e-30, 3e-7, "-", "ABC, d = 3 nm", BLUE),
                                   (1e7, 1e-11, 0.0, 3e-7, "--", "C = 0 (no Auger)", "0.5"),
                                   (1e7, 1e-11, 1e-30, 9e-7, "--", "d = 9 nm", GREEN)]:
        R = A * n + B * n ** 2 + C * n ** 3
        J = q * d * R
        eta = B * n ** 2 / R
        a1.plot(J, 100 * eta, ls=ls, color=c, label=lab, lw=1.8 if ls == "-" else 1.4)
    # mark worked-example points
    for nn, ytxt in ((np.sqrt(1e37), 30), (1e19, 22), (3e19, 14)):
        R = 1e7 * nn + 1e-11 * nn ** 2 + 1e-30 * nn ** 3
        J, eta = q * 3e-7 * R, 1e-11 * nn ** 2 / R
        a1.plot(J, 100 * eta, "o", color=BLUE, ms=5, zorder=5)
        txt = f"{100 * eta:.0f}% at {J:.2g} A/cm²" if J < 10 else f"{100 * eta:.0f}% at {J:.0f} A/cm²" if J < 1000 else f"{100 * eta:.0f}% at {J / 1e3:.1f} kA/cm²"
        a1.annotate(txt, (J, 100 * eta), xytext=(1.6, ytxt), fontsize=7.5, color=BLUE, va="center",
                    arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.6, alpha=0.7))
    a1.set_xscale("log")
    a1.set_xlim(0.1, 1000 * 2)
    a1.set_ylim(0, 100)
    a1.set_yticks(range(0, 101, 20))
    a1.set_xlabel(r"current density $J$ (A/cm$^2$)")
    a1.set_ylabel("internal quantum efficiency (%)")
    a1.legend(loc="upper left", fontsize=7.5)
    a1.set_title("efficiency droop (ABC model)", fontsize=9.5)
    # right: green gap
    lam = np.linspace(380, 660, 400)
    lI = np.array([380, 405, 430, 450, 470, 500, 530, 555, 580])
    eI = np.array([50, 72, 78.5, 80, 75, 55, 35, 18, 8])
    lP = np.array([565, 570, 580, 590, 605, 625, 645, 660])
    eP = np.array([2.0, 3.5, 8, 15, 35, 55, 50, 45])
    fI = PchipInterpolator(lI, eI)
    fP = PchipInterpolator(lP, eP)
    a2.axvspan(530, 590, color="0.85", lw=0)
    a2.text(560, 86, "green\ngap", ha="center", va="top", fontsize=8.5)
    xI = np.linspace(380, 580, 200)
    xP = np.linspace(565, 660, 200)
    a2.plot(xI, fI(xI), color=BLUE, lw=1.9)
    a2.plot(xP, fP(xP), color=RED, lw=1.9)
    a2.text(415, 83, "InGaN", color=BLUE, fontsize=9, weight="bold")
    a2.text(625, 64, "AlGaInP", color=RED, fontsize=9, weight="bold", ha="center")
    V = 1.019 * np.exp(-285.4 * (lam / 1e3 - 0.559) ** 2)
    a2.plot(lam, 85 * V, color=INK, ls=":", lw=1.3)
    a2.text(385, 40, "eye sensitivity\n" + r"$V(\lambda)$, scaled", fontsize=7.5, ha="left")
    a2.set_xlim(380, 660)
    a2.set_ylim(0, 90)
    a2.set_xlabel("emission wavelength (nm)")
    a2.set_ylabel("peak external quantum efficiency (%)")
    a2.set_title("the green gap", fontsize=9.5)
    save(fig, "35", "fig-35-3-droop-and-green-gap")


# ---------------------------------------------------------------- Figure 35.4
def detector_materials():
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.6, 5.6), gridspec_kw=dict(height_ratios=[1.25, 1], hspace=0.38))
    bars = [("AlGaN", 0.2, 0.28, None, PINK), ("Si", 0.3, 1.1, None, BLUE), ("Ge", 0.8, 1.6, None, RED),
            ("InGaAs", 0.9, 1.7, 2.6, GREEN), ("PbS", 1.0, 3.0, None, "0.45"), ("InSb", 1.0, 5.4, None, ORANGE),
            ("HgCdTe MWIR", 3.0, 5.0, None, SKY), ("HgCdTe LWIR", 8.0, 12.0, None, SKY),
            ("T2SL (InAs/GaSb)", 3.0, 15.0, None, PINK), ("microbolometer (thermal)", 8.0, 14.0, None, "0.6")]
    for lo, hi in [(0.4, 2.5), (3, 5), (8, 14)]:
        a1.axvspan(lo, hi, color="#CFE3F3", alpha=0.6, lw=0, zorder=0)
    a1.text(1.0, -0.95, "atmospheric windows (shaded)", fontsize=7.5, color="#2b6a9a", ha="center", va="center")
    for i, (nm, lo, hi, ext, c) in enumerate(bars):
        y = len(bars) - 1 - i
        hatch = "////" if "thermal" in nm else None
        a1.add_patch(Rectangle((lo, y - 0.32), hi - lo, 0.64, fc=c if not hatch else "white",
                               ec=c if not hatch else INK, hatch=hatch, lw=0.8, alpha=0.9))
        if ext:
            a1.add_patch(Rectangle((hi, y - 0.32), ext - hi, 0.64, fc="none", ec=c, ls="--", lw=1.0))
        xt = (ext or hi) * 1.08
        if hi > 9:
            a1.text(lo / 1.08, y, nm, va="center", ha="right", fontsize=8)
        else:
            a1.text(xt, y, nm + (" (dashed: extended)" if ext else ""), va="center", ha="left", fontsize=8)
    a1.set_xscale("log")
    a1.set_xlim(0.2, 20)
    a1.set_ylim(-1.3, len(bars) - 0.4)
    a1.set_yticks([])
    a1.spines["left"].set_visible(False)
    a1.set_xticks([0.2, 0.3, 0.5, 1, 2, 3, 5, 10, 20])
    a1.set_xticklabels(["0.2", "0.3", "0.5", "1", "2", "3", "5", "10", "20"])
    a1.xaxis.set_minor_formatter(plt.NullFormatter())
    a1.set_xlabel("wavelength (µm)")
    # responsivity
    lam = np.linspace(0.3, 1.8, 600)
    a2.plot(lam, lam / HC, color=INK, ls="--", lw=1.2)
    a2.text(1.2, 1.2 / HC + 0.07, r"ideal $\eta=1$: $\mathcal{R}=\lambda/1.24$", fontsize=8, rotation=0, ha="right")
    # Si: 100 um collection depth, 90% internal, blue loss from surface recombination
    ls = lam[(lam > 0.32) & (lam < 1.15)]
    aSi = alpha_Si(HC / ls)
    eta = 0.9 * (1 - np.exp(-aSi * 100e-4)) * (1 - np.exp(-(ls - 0.30) / 0.12))
    a2.plot(ls, eta * ls / HC, color=BLUE, lw=1.8)
    # Ge (bulk photodiode, empirical shape)
    lg = lam[(lam > 0.6) & (lam < 1.8)]
    eta = 0.68 / (1 + np.exp((lg - 1.585) / 0.025)) * (1 - np.exp(-(lg - 0.55) / 0.25))
    a2.plot(lg, eta * lg / HC, color=RED, lw=1.8)
    # InGaAs with InP cap (absorbs below 0.92 um)
    li = lam[(lam > 0.85) & (lam < 1.8)]
    eta = 0.81 / (1 + np.exp((li - 1.66) / 0.018)) / (1 + np.exp(-(li - 0.93) / 0.02))
    a2.plot(li, eta * li / HC, color=GREEN, lw=1.8)
    a2.text(0.75, 0.40, "Si", color=BLUE, fontsize=9, weight="bold")
    a2.text(1.25, 0.44, "Ge", color=RED, fontsize=9, weight="bold")
    a2.text(1.64, 1.08, "InGaAs", color=GREEN, fontsize=9, weight="bold")
    a2.set_xlim(0.3, 1.8)
    a2.set_ylim(0, 1.5)
    a2.set_xlabel("wavelength (µm)")
    a2.set_ylabel(r"responsivity $\mathcal{R}$ (A/W)")
    save(fig, "35", "fig-35-4-detector-materials")


# ---------------------------------------------------------------- Figure 35.5
def _am15g():
    """Approximate AM1.5G photon spectrum: 5778 K blackbody at 1 AU attenuated by Rayleigh, aerosol,
    ozone and Gaussian H2O/O2/CO2 bands (AM 1.5), renormalised to 1000 W/m^2."""
    h, c, k = 6.62607e-34, 2.99792e8, 1.380649e-23
    lam = np.linspace(0.28, 4.0, 8000)                     # um
    L = lam * 1e-6
    Bb = 2 * h * c ** 2 / L ** 5 / np.expm1(h * c / (L * k * 5778))
    Bb *= 6.8e-5                                          # solid angle of the Sun
    m = 1.5
    tau = 0.8 * 0.008735 * lam ** -4.08 + 0.09 * lam ** -1.3
    tau += 3.0 * np.exp(-((lam - 0.26) / 0.03) ** 2) + 0.03 * np.exp(-((lam - 0.6) / 0.08) ** 2)
    bands = [(0.69, 0.006, 0.4), (0.72, 0.012, 0.25), (0.76, 0.004, 1.0), (0.82, 0.015, 0.25),
             (0.955, 0.025, 1.8), (1.13, 0.03, 0.8), (1.38, 0.06, 5.0), (1.87, 0.07, 6.0),
             (2.0, 0.02, 0.6), (2.7, 0.15, 6.0), (3.2, 0.1, 1.0)]
    for c0, w, dpt in bands:
        tau += dpt * np.exp(-((lam - c0) / w) ** 2)
    S = Bb * np.exp(-m * tau)                             # W m^-2 m^-1
    S *= 1000 / np.trapezoid(S, L)
    E = HC / lam                                          # eV
    phi = S * L / (h * c)                                 # photons m^-2 s^-1 per m
    # convert to per eV
    phiE = phi * (L / E)                                  # dL/dE = L/E
    o = np.argsort(E)
    return E[o], phiE[o]


def _sq(E, phiE):
    q, kT = 1.602e-19, 0.025852
    h, c = 6.62607e-34, 2.99792e8
    Eg_list = np.linspace(0.5, 3.0, 401)
    eff = []
    for Eg in Eg_list:
        m = E >= Eg
        Jsc = q * np.trapezoid(phiE[m], E[m])
        Ee = np.linspace(Eg, Eg + 1.5, 600)
        J0 = q * 2 * np.pi / (h ** 3 * c ** 2) * np.trapezoid((Ee * q) ** 2 / np.expm1(Ee / kT), Ee * q)
        V = np.linspace(0, Eg, 4000)
        P = V * (Jsc - J0 * np.expm1(V / kT))
        eff.append(P.max() / 1000)
    return Eg_list, np.array(eff)


def shockley_queisser():
    E, phiE = _am15g()
    Eg, eff = _sq(E, phiE)
    eff = eff * 0.337 / eff.max()   # pin the peak to the published AM1.5G value (approximate spectrum)
    fig, ax = new_fig(6.6, 4.6)
    ax.plot(Eg, 100 * eff, color=INK, lw=1.9)
    i = np.argmax(eff)
    ax.annotate(f"SQ limit (AM1.5G): {100 * eff[i]:.1f}% at {Eg[i]:.2f} eV", (Eg[i], 100 * eff[i]),
                xytext=(0.53, 35.6), fontsize=8, va="center", arrowprops=dict(arrowstyle="-", lw=0.7))
    # (name, Eg, record %, loss, colour, label position)
    cells = [("c-Si", 1.12, 27, "Auger + weak absorption", BLUE, (0.53, 14.0)),
             ("CIGS", 1.15, 23.5, "interface/bulk recombination", GREEN, (0.53, 10.5)),
             ("GaAs", 1.42, 29, "non-radiative (ERE < 1)", RED, (0.53, 7.0)),
             ("CdTe", 1.50, 23, r"$V_{oc}$ deficit: defects, GBs", ORANGE, (0.53, 3.5)),
             ("perovskite", 1.55, 26.5, "interface non-radiative", PINK, (1.90, 10.5)),
             ("CZTS", 1.50, 14, r"cation disorder, large $E_U$", "0.35", (1.90, 7.0)),
             ("a-Si:H", 1.75, 10, r"Urbach tail, low $\mu\tau$", SKY, (1.90, 3.5))]
    f = lambda e: 100 * np.interp(e, Eg, eff)
    for nm, e, ef, loss, c, (tx, ty) in cells:
        ax.annotate("", xy=(e, f(e) - 0.3), xytext=(e, ef + 0.4),
                    arrowprops=dict(arrowstyle="-|>", color=c, lw=1.0, mutation_scale=8))
        ax.plot([e, tx + (0.33 if tx < 1 else -0.01)], [ef, ty], color=c, lw=0.5, alpha=0.6, zorder=1)
        ax.plot(e, ef, "o", ms=6.5, color=c, mec=INK, mew=0.4, zorder=5)
        ax.text(tx, ty, f"{nm} ({ef:g}%)\n" + loss, fontsize=7, ha="left", va="center", color=INK,
                bbox=dict(fc="white", ec=c, lw=0.6, pad=1.5), zorder=6)
    ax.set_xlim(0.5, 3.0)
    ax.set_ylim(0, 37)
    ax.set_xlabel(r"band gap $E_g$ (eV)")
    ax.set_ylabel("efficiency (%)")
    # inset: energy breakdown at Eg = 1.34
    Eg0 = 1.34
    q = 1.602e-19
    Pin = np.trapezoid(phiE * E * q, E)
    m = E >= Eg0
    below = np.trapezoid((phiE * E * q)[~m], E[~m]) / Pin
    therm = np.trapezoid((phiE * (E - Eg0) * q)[m], E[m]) / Pin
    out = 100 * np.interp(Eg0, Eg, eff) / 100
    emis = 1 - below - therm - out
    ins = ax.inset_axes([0.70, 0.56, 0.28, 0.33])
    parts = [("output", out, GREEN), ("thermalization", therm, ORANGE), ("below-gap\ntransmission", below, BLUE),
             ("emission +\n$V_{oc}<E_g$", emis, "0.6")]
    bottom = 0
    for nm, v, c in parts:
        ins.bar(0, 100 * v, bottom=bottom, color=c, width=0.6, ec="white")
        ins.text(0.38, bottom + 50 * v, f"{nm} {100 * v:.0f}%", va="center", fontsize=6.5)
        bottom += 100 * v
    ins.set_xlim(-0.35, 2.4)
    ins.set_ylim(0, 100)
    ins.set_xticks([])
    ins.tick_params(labelsize=6.5)
    ins.set_title(r"where sunlight goes, $E_g=1.34$ eV", fontsize=7, pad=9)
    ins.set_ylabel("% of incident", fontsize=6.5, labelpad=1)
    save(fig, "35", "fig-35-5-shockley-queisser")


# ---------------------------------------------------------------- Figure 35.6
def silica_fibre_loss():
    lam = np.linspace(0.8, 1.8, 1000)
    ray = 0.8 / lam ** 4
    ir = 6e11 * np.exp(-48 / lam)
    uv = 1e-3 * np.exp(4.6 / lam) * 0.05
    imp = 0.02
    oh = 1.6 * np.exp(-((lam - 1.383) / 0.012) ** 2) + 0.08 * np.exp(-((lam - 1.24) / 0.02) ** 2) \
        + 0.05 * np.exp(-((lam - 0.945) / 0.015) ** 2)
    base = ray + ir + uv + imp
    fig, ax = new_fig(6.4, 4.2)
    ax.plot(lam, ray, color=BLUE, ls="--", lw=1.3)
    ax.plot(lam, ir, color=RED, ls="--", lw=1.3)
    ax.plot(lam, base + oh, color=INK, lw=1.9, label="standard fibre (OH peak at 1383 nm)")
    ax.plot(lam, base, color=GREEN, ls=":", lw=2.0, label="low-water-peak fibre")
    ax.set_yscale("log")
    ax.set_xlim(0.8, 1.8)
    ax.set_ylim(0.1, 10)
    ax.set_yticks([0.1, 0.2, 0.5, 1, 2, 5, 10])
    ax.set_yticklabels(["0.1", "0.2", "0.5", "1", "2", "5", "10"])
    ax.yaxis.set_minor_formatter(plt.NullFormatter())
    ax.set_xlabel("wavelength (µm)")
    ax.set_ylabel("attenuation (dB/km)")
    ax.text(0.86, 0.62, r"Rayleigh $0.8/\lambda^4$", color=BLUE, fontsize=8, rotation=-22)
    ax.text(1.70, 0.13, "IR absorption\n(Si–O vibrations)", color=RED, fontsize=8, ha="left", va="center")
    i = np.argmin(base)
    ax.annotate(f"minimum ≈ {base[i]:.2f} dB/km\nnear {lam[i] * 1e3:.0f} nm", (lam[i], base[i]),
                xytext=(1.0, 0.15), fontsize=8, arrowprops=dict(arrowstyle="-", lw=0.7))
    ax.annotate("OH overtone\n1383 nm", (1.383, 1.75), xytext=(1.43, 1.6), fontsize=8,
                arrowprops=dict(arrowstyle="-", lw=0.7))
    for lam0, v in [(0.85, 0.8 / 0.85 ** 4), (1.31, 0.8 / 1.31 ** 4), (1.55, 0.8 / 1.55 ** 4)]:
        ax.plot(lam0, v, "o", ms=3.5, color=BLUE)
    ax.legend(loc="upper left", fontsize=7.5)
    # telecom bands along top
    bands = [("O", 1.26, 1.36), ("E", 1.36, 1.46), ("S", 1.46, 1.53), ("C", 1.53, 1.565), ("L", 1.565, 1.625)]
    cols = ["#E8EEF5", "#F5ECE3", "#E8F3EE", "#F8E1D2", "#EFE6F2"]
    for (nm, lo, hi), c in zip(bands, cols):
        ax.axvspan(lo, hi, ymin=0.0, ymax=1.0, color=c, lw=0, zorder=0)
        ax.text((lo + hi) / 2, 8.3, nm, ha="center", fontsize=8.5, weight="bold")
    ax.annotate("", xy=(1.565, 5.6), xytext=(1.53, 5.6),
                arrowprops=dict(arrowstyle="<|-|>", color=RED, lw=1.0, mutation_scale=7, shrinkA=0, shrinkB=0))
    ax.text(1.635, 5.6, "EDFA gain", ha="left", va="center", fontsize=7.5, color=RED)
    save(fig, "35", "fig-35-6-silica-fibre-loss")


if __name__ == "__main__":
    absorption_coefficient()
    bandgap_lattice_map()
    droop_and_green_gap()
    detector_materials()
    shockley_queisser()
    silica_fibre_loss()
