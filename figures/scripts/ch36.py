"""Figures for Chapter 36 — Optical Materials.

Run from the repository root:  python figures/scripts/ch36.py
"""
import numpy as np
from scipy.interpolate import PchipInterpolator
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch

from figstyle import new_fig, save, COLORS, INK


def wavelength_to_rgb(wl_nm):
    """Approximate sRGB colour of monochromatic light (380–780 nm)."""
    w = wl_nm
    if w < 380 or w > 780:
        return (0.5, 0.5, 0.5)
    if w < 440:
        r, g, b = -(w - 440) / 60, 0.0, 1.0
    elif w < 490:
        r, g, b = 0.0, (w - 440) / 50, 1.0
    elif w < 510:
        r, g, b = 0.0, 1.0, -(w - 510) / 20
    elif w < 580:
        r, g, b = (w - 510) / 70, 1.0, 0.0
    elif w < 645:
        r, g, b = 1.0, -(w - 645) / 65, 0.0
    else:
        r, g, b = 1.0, 0.0, 0.0
    f = 0.35 + 0.65 * (w - 380) / 40 if w < 420 else (0.35 + 0.65 * (780 - w) / 80 if w > 700 else 1.0)
    return (r * f + (1 - f), g * f + (1 - f), b * f + (1 - f))


def shade_visible(ax, lo=400, hi=700, scale=1.0, alpha=0.30, n=120):
    """Shade the visible band in spectral colours; x in units of nm/scale."""
    edges = np.linspace(lo, hi, n + 1)
    for a, b in zip(edges[:-1], edges[1:]):
        ax.axvspan(a / scale, b / scale, color=wavelength_to_rgb((a + b) / 2), alpha=alpha, lw=0, zorder=0)


# --------------------------------------------------------------------------- 28.1
def transmission_windows():
    # (name, lo, hi, family, extra-features)
    mats = [
        ("LiF", 0.11, 7, "fluoride"), ("MgF$_2$", 0.12, 7, "fluoride"), ("CaF$_2$", 0.13, 10, "fluoride"),
        ("fused silica", 0.16, 3.5, "glass"), ("BK7 glass", 0.33, 2.5, "glass"),
        ("sapphire", 0.17, 5.5, "oxide"), ("MgAl$_2$O$_4$ spinel", 0.2, 5.5, "oxide"),
        ("YAG", 0.21, 5.5, "oxide"), ("AlON", 0.22, 5, "oxide"),
        ("diamond", 0.23, 50, "covalent"), ("ZnS (multispectral)", 0.37, 12, "IR"),
        ("ZnSe", 0.5, 20, "IR"), ("As$_2$S$_3$ glass", 0.6, 11, "IR"), ("GaAs", 0.9, 15, "IR"),
        ("Si", 1.2, 7, "IR"), ("Ge", 2.0, 14, "IR"),
        ("PMMA", 0.38, 1.6, "polymer"), ("polycarbonate", 0.4, 1.6, "polymer"),
    ]
    fam_col = {"fluoride": COLORS[5], "glass": COLORS[0], "oxide": COLORS[2], "covalent": COLORS[3],
               "IR": COLORS[1], "polymer": COLORS[4]}
    fig, ax = new_fig(6.8, 5.0)
    shade_visible(ax, scale=1000, alpha=0.35)
    for lo, hi in ((3, 5), (8, 12)):
        ax.axvspan(lo, hi, color="#DDDDDD", alpha=0.6, lw=0, zorder=0)
    ax.text(3.9, len(mats) + 0.35, "atm.\n3–5 µm", ha="center", fontsize=7.5, color="#555555")
    ax.text(9.8, len(mats) + 0.35, "atm.\n8–12 µm", ha="center", fontsize=7.5, color="#555555")
    ax.text(0.53, len(mats) + 0.35, "visible", ha="center", fontsize=7.5, color="#555555")
    for i, (name, lo, hi, fam) in enumerate(mats):
        y = len(mats) - 1 - i
        hi_draw = min(hi, 30)
        ax.add_patch(Rectangle((lo, y - 0.32), hi_draw - lo, 0.64, fc=fam_col[fam], ec="none", alpha=0.85))
        if hi > 30:
            ax.annotate("", xy=(33, y), xytext=(29, y), annotation_clip=False,
                        arrowprops=dict(arrowstyle="-|>", color=fam_col[fam], lw=1.5))
            ax.text(29, y + 0.42, "to ~50 µm", fontsize=7, ha="right", va="bottom", color="#555555")
        ax.text(lo / 1.08, y, name, ha="right", va="center", fontsize=8)
        if name == "fused silica":     # OH absorption dip at 2.7 um
            ax.add_patch(Rectangle((2.6, y - 0.32), 0.2, 0.64, fc="white", ec="none", alpha=0.85))
            ax.text(2.7, y + 0.35, "OH", fontsize=6.5, ha="center", va="bottom")
        if name == "diamond":          # weak multiphonon band
            ax.add_patch(Rectangle((2.5, y - 0.32), 3.5, 0.64, fc="white", ec="none", alpha=0.45))
            ax.text(3.9, y, "multiphonon", fontsize=6.5, ha="center", va="center")
    ax.set_xscale("log")
    ax.set_xlim(0.03, 30)
    ax.set_ylim(-0.7, len(mats) + 1.8)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xticks([0.1, 0.2, 0.5, 1, 2, 5, 10, 20])
    ax.set_xticklabels(["0.1", "0.2", "0.5", "1", "2", "5", "10", "20"])
    ax.set_xlabel("Wavelength (µm)")
    # bound labels
    ax.annotate("short-λ edge: band gap\n(electronic absorption)", xy=(0.11, 17.3), xytext=(0.032, 19.25),
                fontsize=7.5, ha="left", va="center", arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK))
    ax.annotate("long-λ edge:\nmultiphonon\n(lattice)", xy=(10.2, 15.2), xytext=(21, 12.4), fontsize=7.5,
                ha="center", va="center", arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK))
    handles = [Rectangle((0, 0), 1, 1, fc=c, alpha=0.85) for c in fam_col.values()]
    ax.legend(handles, ["fluorides", "silicate glasses", "oxide crystals/ceramics", "diamond",
                        "IR materials", "polymers"], loc="upper center", fontsize=7.5, ncol=3,
              bbox_to_anchor=(0.5, -0.12))
    save(fig, "36", "fig-36-1-transmission-windows")


# --------------------------------------------------------------------------- 28.2
def sellmeier(lam, B, C):
    l2 = lam**2
    return np.sqrt(1 + sum(b * l2 / (l2 - c) for b, c in zip(B, C)))


SILICA = ((0.6961663, 0.4079426, 0.8974794), (0.0684043**2, 0.1162414**2, 9.896161**2))


def sellmeier_dispersion():
    mats = [
        ("CaF$_2$", (0.5675888, 0.4710914, 3.8484723), (0.050263605**2, 0.1003909**2, 34.649040**2),
         0.2, 5.0, COLORS[5]),
        ("fused silica", *SILICA, 0.2, 3.7, COLORS[0]),
        ("N-BK7", (1.03961212, 0.231792344, 1.01046945), (0.00600069867, 0.0200179144, 103.560653),
         0.31, 2.5, COLORS[2]),
        ("sapphire ($n_o$)", (1.4313493, 0.65054713, 5.3414021), (0.0726631**2, 0.1193242**2, 18.028251**2),
         0.2, 5.0, COLORS[1]),
        ("YAG", (2.282, 3.27644), (0.01185, 282.734), 0.4, 5.0, COLORS[3]),
        ("diamond", (0.3306, 4.3356), (0.175**2, 0.106**2), 0.23, 5.0, INK),
    ]
    fig, ax = new_fig(6.6, 4.4)
    for name, B, C, lo, hi, c in mats:
        lam = np.logspace(np.log10(lo), np.log10(hi), 400)
        n = sellmeier(lam, B, C)
        ax.semilogx(lam, n, color=c, lw=1.8)
        nd = sellmeier(np.array([0.5893]), B, C)[0]
        if name == "fused silica":
            ax.text(0.205, 1.61, f"{name}, $n_d$ = {nd:.3f}", fontsize=7.8, color=c, va="center")
        elif name == "CaF$_2$":
            ax.text(0.95, 1.385, f"{name}, $n_d$ = {nd:.3f}", fontsize=7.8, color=c, va="center")
        else:
            ax.text(hi * 1.04, n[-1], f"{name}\n$n_d$ = {nd:.3f}", fontsize=7.8, color=c, va="center")
    ax.annotate("", xy=(0.215, 1.545), xytext=(0.23, 1.598), arrowprops=dict(arrowstyle="-", lw=0.6,
                                                                            color=COLORS[0]))
    for lam, lab in ((0.4861, "F"), (0.5893, "d"), (0.6563, "C")):
        ax.plot([lam, lam], [1.35, 1.375], color=INK, lw=1)
        ax.text(lam, 1.38, lab, ha="center", fontsize=8)
    ax.set_xlim(0.2, 5)
    ax.set_ylim(1.35, 2.5)
    ax.set_xticks([0.2, 0.3, 0.5, 1, 2, 5])
    ax.set_xticklabels(["0.2", "0.3", "0.5", "1", "2", "5"])
    ax.xaxis.set_minor_formatter(plt.NullFormatter())
    ax.set_xlabel("Wavelength (µm)")
    ax.set_ylabel("Refractive index $n$")
    ax.spines["right"].set_visible(False)
    # inset: material dispersion of fused silica
    ins = ax.inset_axes([0.47, 0.50, 0.30, 0.32])
    lam = np.linspace(0.95, 1.75, 800)
    n = sellmeier(lam, *SILICA)
    d2 = np.gradient(np.gradient(n, lam), lam)            # um^-2
    D = -(lam * 1e-6) / 2.998e8 * (d2 * 1e12) * 1e6     # s/m^2 -> ps/(nm km)
    ins.plot(lam, D, color=COLORS[0], lw=1.5)
    ins.axhline(0, color="#888888", lw=0.6)
    z = lam[np.argmin(abs(D))]
    d155 = np.interp(1.55, lam, D)
    ins.plot([z], [0], "o", ms=3, color=INK)
    ins.plot([1.55], [d155], "o", ms=3, color=INK)
    ins.text(z, 4, f"zero at {z:.2f} µm", fontsize=7, ha="center")
    ins.text(1.50, 24, f"+{d155:.0f} at 1.55 µm", fontsize=7, ha="right", va="bottom")
    ins.set_xlim(1.0, 1.7)
    ins.set_ylim(-40, 32)
    ins.tick_params(labelsize=7)
    ins.set_xlabel("λ (µm)", fontsize=7, labelpad=1)
    ins.set_ylabel("D (ps nm$^{-1}$ km$^{-1}$)", fontsize=7, labelpad=1)
    ins.set_title("fused silica material dispersion", fontsize=7, pad=2)
    save(fig, "36", "fig-36-2-sellmeier-dispersion")
    return z, d155


# --------------------------------------------------------------------------- 28.3
def metal_reflectance():
    # Representative normal-incidence reflectance of fresh evaporated films (handbook-level values)
    data = {
        "Ag": ([200, 250, 300, 316, 330, 350, 380, 400, 450, 500, 600, 700, 1000, 2000],
               [23, 27, 17, 5, 30, 75, 88, 92, 95.5, 97, 98, 98.5, 99, 99]),
        "Al": ([200, 300, 400, 500, 600, 700, 780, 830, 900, 1000, 1500, 2000],
               [92, 92.2, 92.3, 91.8, 90.8, 89, 87, 86.4, 88.5, 93.5, 96.5, 97]),
        "Au": ([200, 300, 400, 450, 500, 525, 550, 575, 600, 650, 700, 800, 1000, 2000],
               [22, 37, 38.5, 38.3, 47.5, 64, 81, 88.5, 92, 95, 96.5, 97.5, 98, 98.5]),
        "Cu": ([200, 300, 400, 450, 500, 550, 570, 585, 600, 650, 700, 800, 1000, 2000],
               [33, 34, 46, 50.5, 55, 60, 69, 84, 91, 95, 96.5, 97.5, 98, 98.5]),
    }
    cols = {"Ag": "#7F7F7F", "Al": COLORS[0], "Au": "#C99A00", "Cu": "#B5651D"}
    fig, ax = new_fig(6.4, 4.0)
    shade_visible(ax, alpha=0.30)
    lam = np.linspace(200, 2000, 1000)
    for k, (x, y) in data.items():
        R = PchipInterpolator(np.log(x), y)(np.log(lam))
        ax.plot(lam, R, color=cols[k], lw=2)
    ax.text(1960, 99.6, "Ag", color=cols["Ag"], fontsize=9, ha="right", va="bottom")
    ax.text(1200, 92.0, "Al", color=cols["Al"], fontsize=9, va="top")
    ax.text(470, 30, "Au", color=cols["Au"], fontsize=9)
    ax.text(222, 39, "Cu", color=cols["Cu"], fontsize=9)
    ax.text(290, 9, "Ag plasma\nedge ≈ 320 nm", fontsize=7.5, ha="center")
    ax.annotate("Al interband\ndip at 830 nm", xy=(830, 86.4), xytext=(1050, 72), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", lw=0.6))
    ax.annotate("Cu d-band edge\n≈ 2.1 eV (590 nm)", xy=(585, 85), xytext=(700, 50), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", lw=0.6, color=cols["Cu"]), color=cols["Cu"])
    ax.annotate("Au d-band edge\n≈ 2.4 eV (520 nm)", xy=(522, 62), xytext=(700, 30), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", lw=0.6, color="#A07800"), color="#A07800")
    ax.set_xscale("log")
    ax.set_xlim(200, 2000)
    ax.set_xticks([200, 300, 400, 500, 700, 1000, 1500, 2000])
    ax.set_xticklabels(["200", "300", "400", "500", "700", "1000", "1500", "2000"])
    ax.xaxis.set_minor_formatter(plt.NullFormatter())
    ax.set_ylim(0, 102)
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Normal-incidence reflectance (%)")
    save(fig, "36", "fig-36-3-metal-reflectance")


# --------------------------------------------------------------------------- 28.4
def _mie_qsca(m, x, nmax=None):
    """Scattering efficiency of a sphere (Bohren & Huffman), real relative index m."""
    nmax = nmax or int(x + 4 * x ** (1 / 3) + 2)
    mx = m * x
    nmx = int(max(nmax, abs(mx)) + 16)
    D = np.zeros(nmx + 1)
    for n in range(nmx, 0, -1):
        D[n - 1] = n / mx - 1 / (D[n] + n / mx)
    psi0, psi1 = np.cos(x), np.sin(x)
    chi0, chi1 = -np.sin(x), np.cos(x)
    xi1 = psi1 - 1j * chi1
    q = 0.0
    for n in range(1, nmax + 1):
        psi = (2 * n - 1) / x * psi1 - psi0
        chi = (2 * n - 1) / x * chi1 - chi0
        xi = psi - 1j * chi
        a = ((D[n] / m + n / x) * psi - psi1) / ((D[n] / m + n / x) * xi - xi1)
        b = ((D[n] * m + n / x) * psi - psi1) / ((D[n] * m + n / x) * xi - xi1)
        q += (2 * n + 1) * (abs(a) ** 2 + abs(b) ** 2)
        psi0, psi1, chi0, chi1, xi1 = psi1, psi, chi1, chi, xi
    return 2 / x**2 * q


def transparent_ceramic():
    lam0, d, dn = 640e-9, 0.8e-3, 0.008
    D = np.logspace(-1, 2, 400) * 1e-6          # grain diameter (m)
    R = ((1.76 - 1) / 2.76) ** 2
    Rs = 2 * R / (1 + R)
    T_al = (1 - Rs) * np.exp(-3 * np.pi**2 * dn**2 * (D / 2) * d / lam0**2)
    Rsp = ((1.72 - 1) / 2.72) ** 2
    Rs_sp = 2 * Rsp / (1 + Rsp)
    # porosity 0.05 % of 0.2-um pores in spinel (Mie)
    rp, phi, nm = 0.1e-6, 5e-4, 1.72
    Q = _mie_qsca(1 / nm, 2 * np.pi * rp * nm / lam0)
    Nv = phi / (4 / 3 * np.pi * rp**3)
    T_por = (1 - Rs_sp) * np.exp(-Nv * Q * np.pi * rp**2 * d)

    fig, ax = new_fig(6.4, 4.0)
    ax.axhspan(100 * (1 - Rs_sp) - 2, 100 * (1 - Rs_sp), color=COLORS[2], alpha=0.25, lw=0)
    ax.text(0.12, 100 * (1 - Rs_sp) - 2.5, f"MgAl$_2$O$_4$ spinel, dense (cubic): ≈{100*(1-Rs_sp):.0f} %, any grain size",
            fontsize=8, color="#1B7A5A", va="top")
    ax.axhline(100 * (1 - Rs), color=COLORS[0], ls="--", lw=1)
    ax.text(99, 100 * (1 - Rs) + 0.8, f"1 − $R_s$ = {100*(1-Rs):.0f} % (alumina)", fontsize=8, ha="right",
            va="bottom", color=COLORS[0])
    ax.plot(D * 1e6, 100 * T_al, color=COLORS[0], lw=2.2)
    ax.text(0.5, 38, "Al$_2$O$_3$ (birefringent, Δn = 0.008)\nApetz–Bruls", fontsize=8, color=COLORS[0])
    ax.axhline(100 * T_por, color=COLORS[2], lw=1.8, ls="-.")
    ax.text(12, 100 * T_por + 1.2, f"spinel with 0.05 % porosity, 0.2 µm pores: ≈{100*T_por:.0f} %", fontsize=8,
            color="#1B7A5A", ha="center", va="bottom")
    for g, v in ((0.3, 49), (1.0, 13.5), (2.0, 2.1)):
        ax.plot(g, v, "o", ms=4, color=INK, zorder=5)
        ax.text(g * 1.12, v + 1.5, f"{v:g} %", fontsize=8)
    # icons: text seen through discs
    for (xc, lab, blur, sub) in ((0.17, "ABC", False, "0.3 µm grains: clear"),
                                 (0.80, "ABC", True, "20 µm grains: translucent")):
        ia = ax.inset_axes([xc - 0.06, 0.035, 0.12, 0.17])
        ia.set_xlim(0, 1)
        ia.set_ylim(0, 1)
        ia.axis("off")
        ia.add_patch(plt.Circle((0.5, 0.5), 0.48, fc="#F2F2F2" if blur else "white", ec=INK, lw=0.8))
        if blur:
            rng = np.random.default_rng(1)
            for _ in range(14):
                dx, dy = rng.normal(0, 0.035, 2)
                ia.text(0.5 + dx, 0.5 + dy, lab, ha="center", va="center", fontsize=9, color="#000000",
                        alpha=0.06, fontweight="bold")
        else:
            ia.text(0.5, 0.5, lab, ha="center", va="center", fontsize=9, fontweight="bold")
        ax.text(xc, 0.215, sub, transform=ax.transAxes, ha="center", va="bottom", fontsize=7)
    ax.set_xscale("log")
    ax.set_xlim(0.1, 100)
    ax.set_ylim(0, 92)
    ax.set_xticks([0.1, 0.3, 1, 3, 10, 30, 100])
    ax.set_xticklabels(["0.1", "0.3", "1", "3", "10", "30", "100"])
    ax.set_xlabel("Mean grain size (µm)")
    ax.set_ylabel("Real in-line transmission (%)\n640 nm, 0.8 mm thick")
    save(fig, "36", "fig-36-4-transparent-ceramic-grain-size")
    return T_por, Q


# --------------------------------------------------------------------------- 28.5
def white_led():
    fig = plt.figure(figsize=(6.8, 3.9))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.0, 1.2], wspace=0.28)
    a = fig.add_subplot(gs[0])
    a.set_xlim(0, 10)
    a.set_ylim(0, 10)
    a.set_aspect("equal")
    a.axis("off")
    # chip cross-section (mesa structure, not to scale)
    a.add_patch(Rectangle((0.5, 0.6), 5.0, 1.6, fc="#D9E4EC", ec=INK, lw=0.6))     # substrate
    a.add_patch(Rectangle((0.5, 2.2), 5.0, 0.9, fc="#9DB4C8", ec=INK, lw=0.6))     # n-GaN
    a.add_patch(Rectangle((1.7, 3.1), 3.8, 0.4, fc="#5E7FA3", ec=INK, lw=0.6))     # MQW
    a.add_patch(Rectangle((1.7, 3.5), 3.8, 0.5, fc="#C8A2C8", ec=INK, lw=0.6))     # p-GaN
    a.add_patch(Rectangle((0.7, 3.1), 0.7, 0.25, fc="#B8860B", ec=INK, lw=0.6))    # n contact
    a.add_patch(Rectangle((4.4, 4.0), 0.8, 0.25, fc="#B8860B", ec=INK, lw=0.6))    # p contact
    for y, lab in ((1.4, "sapphire / patterned\nsubstrate"), (2.65, "n-GaN"), (3.3, "InGaN/GaN MQWs"),
                   (3.8, "p-GaN")):
        a.plot([5.5, 5.8], [y, y], color=INK, lw=0.5)
        a.text(5.9, y, lab, fontsize=7, va="center")
    a.text(1.05, 3.4, "n", fontsize=6.5, ha="center", va="bottom")
    a.text(4.8, 4.27, "p", fontsize=6.5, ha="center", va="bottom")
    a.add_patch(FancyBboxPatch((0.9, 4.0), 4.9, 2.6, boxstyle="round,pad=0,rounding_size=0.6",
                               fc="#FFF3B0", ec=INK, lw=0.6, zorder=0))
    rng = np.random.default_rng(3)
    a.scatter(rng.uniform(1.2, 5.5, 45), rng.uniform(4.45, 6.35, 45), s=6, color="#E0B000", zorder=2)
    a.plot([5.8, 6.1], [5.6, 5.6], color=INK, lw=0.5)
    a.text(6.2, 5.6, "YAG:Ce phosphor\nin silicone", fontsize=7, va="center")
    # photons: some blue escapes, some is absorbed and re-emitted as yellow
    for x0 in (1.9, 2.9):
        a.annotate("", xy=(x0 - 0.3, 9.0), xytext=(x0, 3.3),
                   arrowprops=dict(arrowstyle="-|>", color="#2E5BFF", lw=1.3))
    a.plot([3.9, 4.1], [3.3, 5.3], color="#2E5BFF", lw=1.3)
    a.plot(4.1, 5.3, "*", color="#E0A800", ms=9, zorder=3)
    for xe in (3.4, 5.0):
        a.annotate("", xy=(xe, 9.0), xytext=(4.1, 5.3),
                   arrowprops=dict(arrowstyle="-|>", color="#E0A800", lw=1.5))
    a.text(1.0, 9.15, "blue\n450 nm", fontsize=7.5, color="#2E5BFF", ha="left", va="bottom")
    a.text(4.3, 9.15, "yellow\n(converted)", fontsize=7.5, color="#B08000", ha="left", va="bottom")

    b = fig.add_subplot(gs[1])
    lam = np.linspace(380, 780, 800)

    def gauss(c, fwhm):
        return np.exp(-4 * np.log(2) * (lam - c) ** 2 / fwhm**2)
    yag0 = 0.60 * gauss(555, 110)
    blue = gauss(450, 20)
    norm = (blue + yag0).max()
    blue, yag = blue / norm, yag0 / norm
    red = 0.36 * gauss(630, 90)
    V = 1.019 * np.exp(-285.4 * (lam / 1000 - 0.559) ** 2)
    shade_visible(b, 380, 780, alpha=0.18)
    b.plot(lam, V, color="#777777", lw=1.0)
    b.fill_between(lam, 0, yag, color="#F0C000", alpha=0.25, lw=0)
    b.plot(lam, blue + yag, color=INK, lw=2, label="cool white: blue + YAG:Ce")
    b.plot(lam, blue + yag + red, color=COLORS[1], lw=1.5, ls="--", label="warm white: + red nitride")
    b.text(392, 1.12, "InGaN chip, 450 nm\n(FWHM ≈ 20 nm)", fontsize=7.5, ha="left", va="center")
    b.text(560, 0.13, "YAG:Ce, 555 nm\n(FWHM ≈ 110 nm)", fontsize=7.5, ha="center", va="center")
    b.text(728, 0.30, "red nitride\nphosphor\n≈ 630 nm", fontsize=7.5, ha="center", color=COLORS[1])
    b.text(604, 0.70, r"eye sensitivity $V(\lambda)$", fontsize=7.5, color="#666666", ha="left")
    b.set_xlim(380, 780)
    b.set_ylim(0, 1.24)
    b.set_xlabel("Wavelength (nm)")
    b.set_ylabel("Relative spectral power")
    b.legend(loc="upper right", fontsize=7.0, bbox_to_anchor=(1.03, 1.03))
    save(fig, "36", "fig-36-5-white-led-spectrum")


# --------------------------------------------------------------------------- 28.6
def fibre_attenuation():
    lam = np.linspace(0.7, 1.8, 1000)
    ray = 0.85 / lam**4
    ir = 7.81e11 * np.exp(-48.48 / lam)
    x = 0.04
    uv = 154.2 * x / (46.6 * x + 60) * 1e-2 * np.exp(4.63 / lam)
    base = ray + ir + uv + 0.005
    oh = 1.0 * np.exp(-0.5 * ((lam - 1.383) / 0.012) ** 2) + 0.08 * np.exp(-0.5 * ((lam - 1.24) / 0.012) ** 2) \
        + 0.03 * np.exp(-0.5 * ((lam - 0.945) / 0.010) ** 2)
    lwp = 0.02 * np.exp(-0.5 * ((lam - 1.383) / 0.012) ** 2)
    fig, ax = new_fig(6.4, 4.0)
    for lo, hi, lab in ((1.26, 1.36, "O"), (1.53, 1.565, "C"), (1.565, 1.625, "L")):
        ax.axvspan(lo, hi, color="#E3EFE3" if lab != "L" else "#EAE3F0", lw=0)
        ax.text((lo + hi) / 2, 7.5, lab, ha="center", fontsize=9)
    ax.semilogy(lam, base + oh, color="#999999", lw=1.4, ls="--", label="older fibre (OH peak)")
    ax.semilogy(lam, base + lwp, color=INK, lw=2.2, label="standard SMF, low water peak")
    ax.semilogy(lam, ray, color=COLORS[0], lw=1.2, ls=":", label=r"Rayleigh, $0.85/\lambda^4$")
    ax.semilogy(lam, ir, color=COLORS[1], lw=1.2, ls=":", label="IR absorption (Si–O)")
    ax.semilogy(lam, uv, color=COLORS[3], lw=1.2, ls=":", label="UV absorption tail")
    ax.plot(1.56, 0.14, "*", ms=11, color=COLORS[2])
    ax.annotate("record 0.14 dB/km at 1.56 µm\n(pure-silica-core fibre)", xy=(1.55, 0.14), xytext=(1.02, 0.135),
                fontsize=7.5, color="#1B7A5A", va="center",
                arrowprops=dict(arrowstyle="-", lw=0.7, color="#1B7A5A"))
    for l0 in (0.85, 1.31, 1.55):
        v = np.interp(l0, lam, base + lwp)
        ax.plot(l0, v, "o", ms=4, color=INK)
        ax.text(l0 + 0.015, v * 1.15, f"{v:.2f}", fontsize=8, va="bottom")
    ax.text(1.383, 1.15, "OH 1.38 µm", fontsize=7.5, ha="center", color="#777777")
    ax.set_xlim(0.7, 1.8)
    ax.set_ylim(0.1, 10)
    ax.set_yticks([0.1, 0.2, 0.5, 1, 2, 5, 10])
    ax.set_yticklabels(["0.1", "0.2", "0.5", "1", "2", "5", "10"])
    ax.yaxis.set_minor_formatter(plt.NullFormatter())
    ax.set_xlabel("Wavelength (µm)")
    ax.set_ylabel("Attenuation (dB/km)")
    ax.legend(loc="upper right", fontsize=7.5, bbox_to_anchor=(1.0, 0.93))
    save(fig, "36", "fig-36-6-fibre-attenuation")


if __name__ == "__main__":
    transmission_windows()
    z, d = sellmeier_dispersion()
    metal_reflectance()
    tp, q = transparent_ceramic()
    white_led()
    fibre_attenuation()
    print(f"silica zero-dispersion {z:.3f} um, D(1.55) = {d:.1f}; spinel porous T = {tp:.2f}, Qsca = {q:.2f}")
