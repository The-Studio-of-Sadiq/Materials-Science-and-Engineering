"""Figures for Chapter 50 — Electronic Materials Manufacturing.

Run from the repository root:  python figures/scripts/ch50.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle, FancyArrowPatch, Arc, Ellipse
from scipy.special import erfc, erfcinv

SI = "#B9C4CF"
MELT = "#F2A65A"
OXIDE = "#CFE8F5"


def curved(ax, p0, p1, rad, color=INK, lw=1.0, style="-|>", ms=9):
    ax.add_patch(FancyArrowPatch(p0, p1, connectionstyle=f"arc3,rad={rad}", arrowstyle=style,
                                 color=color, lw=lw, mutation_scale=ms))


# ---------------------------------------------------------------- Figure 50.1
def cz_fz():
    fig, ax = schematic(6.8, 5.2, xlim=(0, 17), ylim=(0, 13))
    # ---- (a) Czochralski
    ax.text(0.2, 12.95, "(a) Czochralski", fontsize=10, va="top")
    cx = 5.0
    # heaters
    for sx in (-1, 1):
        for k in range(4):
            ax.add_patch(Rectangle((cx + sx * 3.55 - 0.2, 1.0 + k * 0.9), 0.4, 0.6, fc="#C0392B", ec="none"))
    ax.text(cx + 3.55, 4.75, "heaters", fontsize=7.5, ha="center")
    # susceptor and crucible
    ax.add_patch(Polygon([[cx - 3.1, 4.6], [cx - 3.1, 1.0], [cx + 3.1, 1.0], [cx + 3.1, 4.6],
                          [cx + 2.8, 4.6], [cx + 2.8, 1.3], [cx - 2.8, 1.3], [cx - 2.8, 4.6]],
                         fc="0.35", ec=INK, lw=0.6))
    ax.add_patch(Polygon([[cx - 2.8, 4.6], [cx - 2.8, 1.3], [cx + 2.8, 1.3], [cx + 2.8, 4.6],
                          [cx + 2.6, 4.6], [cx + 2.6, 1.5], [cx - 2.6, 1.5], [cx - 2.6, 4.6]],
                         fc="#EAF4FB", ec=INK, lw=0.6))
    ax.add_patch(Rectangle((cx - 2.6, 1.5), 5.2, 2.3, fc=MELT, ec="none"))
    ax.text(cx + 1.6, 2.0, "Si melt\n1414 °C", fontsize=7.5, ha="center")
    ax.annotate("graphite\nsusceptor", xy=(cx - 3.05, 1.6), xytext=(0.1, 0.35), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", lw=0.6, color="0.3"))
    ax.annotate("quartz\ncrucible", xy=(cx - 2.7, 4.3), xytext=(0.1, 4.4), fontsize=7.5, va="center",
                arrowprops=dict(arrowstyle="-", lw=0.6, color="0.3"))
    # convection loops
    for sx in (-1, 1):
        ax.add_patch(Ellipse((cx + sx * 1.6, 2.65), 1.5, 1.4, fc="none", ec="#A0522D", lw=0.8, ls="--"))
        curved(ax, (cx + sx * 0.9, 2.9), (cx + sx * 0.95, 2.4), 0.6 * sx, color="#A0522D", lw=0.8, ms=7)
    # crystal: body, shoulder, neck, seed
    body = [[cx - 1.4, 3.8], [cx + 1.4, 3.8], [cx + 1.4, 8.0], [cx + 0.15, 9.0], [cx + 0.1, 10.1],
            [cx + 0.2, 10.1], [cx + 0.2, 10.8], [cx - 0.2, 10.8], [cx - 0.2, 10.1], [cx - 0.1, 10.1],
            [cx - 0.15, 9.0], [cx - 1.4, 8.0]]
    ax.add_patch(Polygon(body, fc=SI, ec=INK, lw=0.8))
    th = np.linspace(0, np.pi, 30)
    ax.plot(cx + 1.4 * np.cos(th), 3.8 + 0.18 * np.sin(th), color=INK, lw=0.8)
    ax.plot([cx, cx], [10.8, 12.2], color=INK, lw=1.2)
    ax.text(cx + 0.35, 10.45, "seed", fontsize=7.5, va="center")
    ax.text(cx + 0.35, 9.55, "Dash neck", fontsize=7.5, va="center")
    ax.text(cx + 0.9, 8.55, "shoulder", fontsize=7.5, va="center")
    ax.text(cx, 6.0, "single-\ncrystal\nbody", fontsize=7.5, ha="center", va="center")
    # rotations
    curved(ax, (cx - 0.6, 11.6), (cx + 0.6, 11.6), 0.5, lw=1.0)
    ax.text(cx + 0.8, 11.75, "pull v,\nrotate", fontsize=7.5, va="center")
    ax.annotate("", xy=(cx - 0.5, 12.7), xytext=(cx - 0.5, 11.9),
                arrowprops=dict(arrowstyle="-|>", lw=1.0, color=INK, mutation_scale=9))
    curved(ax, (cx + 0.8, 0.75), (cx - 0.8, 0.75), 0.4, lw=1.0)
    ax.text(cx + 1.0, 0.3, "crucible counter-rotation", fontsize=7.5, ha="left", va="center")
    # SiO evaporation and argon
    for x in (cx - 2.1, cx + 2.1):
        ax.annotate("", xy=(x, 5.0), xytext=(x, 3.95),
                    arrowprops=dict(arrowstyle="-|>", lw=0.8, color=COLORS[3], mutation_scale=7))
    ax.text(cx + 2.1, 5.05, "SiO", fontsize=7.5, color=COLORS[3], ha="center", va="bottom")
    for sgn in (-1, 1):
        ax.annotate("", xy=(cx + sgn * 1.95, 5.5), xytext=(cx + sgn * 1.7, 8.0),
                    arrowprops=dict(arrowstyle="-|>", lw=0.8, color=COLORS[5], mutation_scale=7))
    ax.text(cx + 1.75, 8.1, "Ar", fontsize=7.5, color=COLORS[0], ha="center", va="bottom")
    ax.annotate("interface:\npull rate v,\ngradient G", xy=(cx - 1.3, 3.85), xytext=(0.1, 6.0), fontsize=7.5,
                va="center", arrowprops=dict(arrowstyle="-", lw=0.6, color="0.3"))
    ax.text(0.1, 7.6, "O from crucible\n5–10×10$^{17}$ cm$^{-3}$", fontsize=7.5, color=COLORS[3], va="center")
    # inset: Scheil segregation
    ins = ax.inset_axes([0.9, 9.0, 2.5, 2.6], transform=ax.transData)
    fs = np.linspace(0, 0.95, 200)
    for k, lab, c in [(0.8, "B, k = 0.8", COLORS[0]), (0.35, "P, k = 0.35", COLORS[1])]:
        ins.plot(fs, (1 - fs) ** (k - 1), color=c, lw=1.4, label=lab)
    ins.set_xlim(0, 1); ins.set_ylim(0, 5)
    ins.set_xticks([0, 0.5, 1])
    ins.set_xlabel("fraction solidified $f_s$", fontsize=7, labelpad=1)
    ins.set_ylabel(r"$C_s/kC_0$", fontsize=7, labelpad=1)
    ins.tick_params(labelsize=6.5)
    ins.legend(fontsize=6.5, loc="upper left", handlelength=1.2)

    # ---- (b) float zone
    fx = 14.0
    ax.text(10.2, 12.95, "(b) Float zone", fontsize=10, va="top")
    ax.add_patch(Rectangle((fx - 1.0, 7.4), 2.0, 4.2, fc="#9AA5B1", ec=INK, lw=0.8, hatch="..."))
    ax.text(fx - 1.2, 8.6, "poly-Si\nfeed rod", fontsize=7.5, ha="right", va="center")
    zone = [[fx - 1.0, 7.4], [fx + 1.0, 7.4], [fx + 1.15, 6.6], [fx + 1.0, 5.8], [fx - 1.0, 5.8], [fx - 1.15, 6.6]]
    ax.add_patch(Polygon(zone, fc=MELT, ec=INK, lw=0.8))
    ax.text(fx, 6.6, "molten\nzone", fontsize=7, ha="center", va="center")
    for y in (6.3, 6.9):
        ax.add_patch(Ellipse((fx, y), 3.4, 0.45, fc="none", ec="#B87333", lw=2.2))
    ax.text(fx + 1.8, 5.7, "RF coil", fontsize=7.5, ha="left", color="#8B4513")
    ax.add_patch(Polygon([[fx - 1.0, 5.8], [fx + 1.0, 5.8], [fx + 1.0, 2.6], [fx + 0.15, 1.8], [fx + 0.15, 1.1],
                          [fx - 0.15, 1.1], [fx - 0.15, 1.8], [fx - 1.0, 2.6]], fc=SI, ec=INK, lw=0.8))
    ax.text(fx - 1.2, 4.1, "single-\ncrystal rod", fontsize=7.5, ha="right", va="center")
    ax.text(fx + 0.3, 1.3, "seed", fontsize=7.5, va="center")
    ax.annotate("", xy=(fx + 1.75, 9.0), xytext=(fx + 1.75, 7.6),
                arrowprops=dict(arrowstyle="-|>", lw=1.2, color=INK, mutation_scale=10))
    ax.text(fx + 1.9, 8.3, "zone\ntravel", fontsize=7.5, va="center")
    ax.text(10.2, 11.6, "no crucible:\nO < 10$^{16}$ cm$^{-3}$\nresistivity\n> 1 kΩ·cm", fontsize=7.5,
            va="top", color=COLORS[3])
    ax.plot([9.8, 9.8], [0.2, 12.6], color="0.75", lw=0.8)
    save(fig, "50", "fig-50-1-czochralski-float-zone")


# ---------------------------------------------------------------- Figure 50.2
DG = {  # (A um, B um^2/h, tau h)
    ("dry", 800): (0.370, 0.0011, 9.0), ("dry", 920): (0.235, 0.0049, 1.4),
    ("dry", 1000): (0.165, 0.0117, 0.37), ("dry", 1100): (0.090, 0.027, 0.076),
    ("dry", 1200): (0.040, 0.045, 0.027),
    ("wet", 920): (0.50, 0.203, 0.0), ("wet", 1000): (0.226, 0.287, 0.0),
    ("wet", 1100): (0.11, 0.510, 0.0), ("wet", 1200): (0.05, 0.720, 0.0),
}


def dg_x(t, A, B, tau):
    return A / 2 * (np.sqrt(1 + (t + tau) / (A**2 / (4 * B))) - 1)


def deal_grove():
    fig, ax = new_fig(6.4, 4.4)
    t = np.logspace(-2, 2, 300)
    # 900 °C dry by Arrhenius interpolation between 800 and 920 °C in 1/T
    T1, T2 = 800 + 273.15, 920 + 273.15
    w = (1 / (900 + 273.15) - 1 / T1) / (1 / T2 - 1 / T1)
    A1, B1, ta1 = DG[("dry", 800)]; A2, B2, ta2 = DG[("dry", 920)]
    B900 = np.exp(np.log(B1) + w * (np.log(B2) - np.log(B1)))
    BA900 = np.exp(np.log(B1 / A1) + w * (np.log(B2 / A2) - np.log(B1 / A1)))
    tau900 = np.exp(np.log(ta1) + w * (np.log(ta2) - np.log(ta1)))
    dry = [(900, (B900 / BA900, B900, tau900))] + [(T, DG[("dry", T)]) for T in (1000, 1100, 1200)]
    wet = [(T, DG[("wet", T)]) for T in (920, 1000, 1100)]
    blues = ["#9ecae1", "#6baed6", "#2171b5", "#08306b"]
    reds = ["#fdae6b", "#e6550d", "#a63603"]
    for (T, (A, B, tau)), c in zip(dry, blues):
        x = dg_x(t, A, B, tau)
        ax.plot(t, x, color=c, lw=1.6)
        ax.text(100 * 1.08, x[-1], f"dry {T}" + (" (interp.)" if T == 900 else ""), color=c, fontsize=7.5,
                va="center")
    for (T, (A, B, tau)), c in zip(wet, reds):
        x = dg_x(t, A, B, tau)
        ax.plot(t, x, color=c, lw=1.6)
        ax.text(100 * 1.08, x[-1], f"wet {T}", color=c, fontsize=7.5, va="center")
    A, B, _ = DG[("wet", 1000)]
    ax.plot(t, B / A * t, "--", color="0.35", lw=1, label=r"linear limit $x=(B/A)t$ (slope 1), wet 1000 °C")
    ax.plot(t, np.sqrt(B * t), ":", color="0.35", lw=1.3, label=r"parabolic limit $x=\sqrt{Bt}$ (slope 1/2), wet 1000 °C")
    tc = A**2 / (4 * B)
    ax.plot([tc], [B / A * tc], "o", ms=4, mfc="white", mec="0.35")
    ax.annotate(r"$t=A^2/4B\approx2.7$ min", xy=(tc, B / A * tc), xytext=(0.011, 0.25), fontsize=8,
                arrowprops=dict(arrowstyle="-", lw=0.6, color="0.35"))
    ax.legend(loc="upper left", fontsize=7.5, bbox_to_anchor=(0.0, 0.93))
    ax.annotate("0.435 µm, 1 h wet", xy=(1, 0.435), xytext=(2.5, 0.23), fontsize=8,
                arrowprops=dict(arrowstyle="-", lw=0.6))
    ax.annotate("0.103 µm, 2 h dry", xy=(2, 0.103), xytext=(0.45, 0.0145), fontsize=8,
                arrowprops=dict(arrowstyle="-", lw=0.6))
    ax.plot([1, 2], [dg_x(1, *DG[("wet", 1000)]), dg_x(2, *DG[("dry", 1000)])], "o", color=INK, ms=4)
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlim(0.01, 100); ax.set_ylim(0.01, 5)
    ax.set_xticks([0.01, 0.1, 1, 10, 100]); ax.set_xticklabels(["0.01", "0.1", "1", "10", "100"])
    ax.set_yticks([0.01, 0.1, 1]); ax.set_yticklabels(["0.01", "0.1", "1"])
    ax.set_xlabel("Oxidation time (h)")
    ax.set_ylabel("Oxide thickness x (µm)")
    ax.text(0.011, 4.2, "(111) Si, Deal–Grove constants", fontsize=8, va="top")
    # inset cross-section
    ins = ax.inset_axes([0.70, 0.03, 0.29, 0.28])
    ins.set_xlim(0, 4); ins.set_ylim(0, 4); ins.axis("off")
    ins.add_patch(Rectangle((0, 0), 4, 1.6, fc=SI, ec="none"))
    ins.add_patch(Rectangle((0, 1.6), 4, 1.6, fc=OXIDE, ec=INK, lw=0.6))
    ins.plot([0, 4], [2.3, 2.3], color=INK, lw=0.8, ls="--")
    ins.text(0.05, 2.38, "original\nsurface", fontsize=6, va="bottom")
    ins.annotate("", xy=(3.75, 3.2), xytext=(3.75, 1.6), arrowprops=dict(arrowstyle="<|-|>", lw=0.7, mutation_scale=6))
    ins.text(3.6, 2.7, "x", fontsize=8, ha="right")
    ins.annotate("", xy=(3.25, 2.3), xytext=(3.25, 1.6), arrowprops=dict(arrowstyle="<|-|>", lw=0.7, mutation_scale=6))
    ins.text(3.1, 1.75, "0.44x", fontsize=6.5, ha="right")
    for xx, y0, y1, lab in [(1.6, 3.95, 3.3, "$F_1$"), (1.6, 3.1, 1.85, "$F_2$"), (2.3, 1.75, 1.45, "$F_3$")]:
        ins.annotate("", xy=(xx, y1), xytext=(xx, y0),
                     arrowprops=dict(arrowstyle="-|>", lw=0.8, color=COLORS[1], mutation_scale=6))
        ins.text(xx + 0.08, (y0 + y1) / 2, lab, fontsize=7, color=COLORS[1], va="center")
    ins.text(2.0, 0.6, "Si", fontsize=7, ha="center")
    ins.text(2.6, 3.4, "gas", fontsize=7, ha="center")
    ins.text(2.5, 2.75, "SiO$_2$", fontsize=7, ha="center")
    save(fig, "50", "fig-50-2-deal-grove-oxide-growth")


# ---------------------------------------------------------------- Figure 50.3
def erfc_gauss():
    fig, ax = new_fig(6.4, 4.0)
    NB = 1e16
    Cs = 2e20
    s1 = 5.23e-6  # cm, sqrt(Dt) predep
    Q = 2 / np.sqrt(np.pi) * Cs * s1
    s2 = 3.30e-5
    x = np.linspace(0, 2.5e-4, 1000)
    C1 = Cs * erfc(x / (2 * s1))
    C2 = Q / (np.sqrt(np.pi) * s2) * np.exp(-x**2 / (4 * s2**2))
    xj1 = 2 * s1 * erfcinv(NB / Cs)
    xj2 = 2 * s2 * np.sqrt(np.log(Q / (NB * np.sqrt(np.pi) * s2)))
    print(f"Q={Q:.3g}, C0={Q/(np.sqrt(np.pi)*s2):.3g}, xj1={xj1*1e4:.3f} um, xj2={xj2*1e4:.3f} um")
    ax.semilogy(x * 1e4, C1, color=COLORS[0], label=r"predeposition (erfc), $C_s=2\times10^{20}$, $\sqrt{Dt}$ = 52 nm")
    ax.semilogy(x * 1e4, C2, color=COLORS[1],
                label=r"after drive-in (Gaussian), $Q=1.18\times10^{15}$ cm$^{-2}$, $\sqrt{Dt}$ = 0.33 µm")
    ax.axhline(NB, color="0.4", ls="--", lw=1)
    ax.text(2.45, NB * 1.3, r"background $N_B=10^{16}$ cm$^{-3}$", fontsize=8, ha="right", va="bottom")
    for xj, c in [(xj1, COLORS[0]), (xj2, COLORS[1])]:
        ax.vlines(xj * 1e4, 1e15, 3e17, color=c, ls=":", lw=1.2)
        ax.text(xj * 1e4 + 0.03, 2e15, rf"$x_j$ = {xj*1e4:.2f} µm", color=c, fontsize=8, va="center")
    ax.plot(0, Q / (np.sqrt(np.pi) * s2), "o", color=COLORS[1], ms=4, clip_on=False)
    ax.annotate(r"$C(0)=2.0\times10^{19}$", xy=(0.0, 2.0e19), xytext=(0.35, 4e19), color=COLORS[1],
                fontsize=8, va="bottom", arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[1]))
    ax.set_xlim(0, 2.5); ax.set_ylim(1e15, 1e21)
    ax.set_xlabel("Depth x (µm)")
    ax.set_ylabel("Boron concentration (cm$^{-3}$)")
    ax.legend(loc="upper right", fontsize=7.5, bbox_to_anchor=(1.0, 1.08))
    ins = ax.inset_axes([0.60, 0.42, 0.37, 0.38])
    u = np.linspace(0, 3, 200)
    ins.plot(u, erfc(u), color=COLORS[0], label="erfc(u)")
    ins.plot(u, np.exp(-u**2), color=COLORS[1], label=r"exp($-u^2$)")
    ins.set_xlim(0, 3); ins.set_ylim(0, 1.05)
    ins.set_xlabel(r"$u=x/2\sqrt{Dt}$", fontsize=7.5, labelpad=1)
    ins.set_ylabel(r"$C/C_{\rm surface}$", fontsize=7.5, labelpad=1)
    ins.tick_params(labelsize=7)
    ins.legend(fontsize=7, loc="upper right")
    save(fig, "50", "fig-50-3-erfc-gaussian-profiles")


# ---------------------------------------------------------------- Figure 50.4
def implant():
    fig, ax = new_fig(6.4, 4.2)
    x = np.linspace(0, 250, 1000)
    Rp, dRp, Phi = 58.0, 21.0, 5e15
    Np = Phi / (np.sqrt(2 * np.pi) * dRp * 1e-7)
    N = Np * np.exp(-(x - Rp) ** 2 / (2 * dRp**2))
    # channelling tail: a small exponential component (~0.1 % of the dose) added to the Gaussian
    tail = 2e19 * np.exp(-x / 28.0)
    Nreal = N + tail
    # 1050 °C spike anneal: slight broadening; electrically active level capped at solubility
    sig = np.sqrt(dRp**2 + 8.0**2)
    Nann = Phi / (np.sqrt(2 * np.pi) * sig * 1e-7) * np.exp(-(x - Rp) ** 2 / (2 * sig**2)) + 1.2 * tail
    Nact = np.minimum(Nann, 3e20)
    xj = Rp + dRp * np.sqrt(2 * np.log(Np / 1e17))
    print(f"Np={Np:.3g}, xj={xj:.1f} nm")
    ax.axvspan(0, 100, color="#DDDDDD", alpha=0.6, lw=0)
    ax.axvspan(100, 112, color=COLORS[3], alpha=0.25, lw=0)
    ax.text(50, 5e21, "amorphous layer", ha="center", fontsize=8)
    ax.annotate("end-of-range defects\n(dislocation loops)", xy=(106, 1.2e19), xytext=(150, 1.2e19),
                fontsize=7.5, color="#7a3d66", va="center",
                arrowprops=dict(arrowstyle="-", lw=0.6, color="#7a3d66"))
    ax.semilogy(x, N, color=COLORS[0], label="as implanted (Gaussian)")
    ax.semilogy(x, Nreal, "--", color=COLORS[0], lw=1.3, label="real profile, channelling tail")
    ax.semilogy(x, Nact, color=COLORS[1], label="active As after 1050 °C spike")
    ax.axhline(3e20, color=COLORS[1], ls=":", lw=1)
    ax.text(248, 3.6e20, "solubility ≈ 3×10$^{20}$", fontsize=7.5, ha="right", color=COLORS[1])
    ax.axhline(1e17, color="0.4", ls=":", lw=1)
    ax.text(248, 1.2e17, r"$N_B=10^{17}$", fontsize=7.5, ha="right")
    ax.plot(xj, 1e17, "o", color=COLORS[0], ms=4)
    ax.annotate(rf"$x_j\approx$ {xj:.0f} nm", xy=(xj, 1e17), xytext=(196, 5.5e16), fontsize=8,
                arrowprops=dict(arrowstyle="-", lw=0.6))
    ax.annotate(r"peak $9.5\times10^{20}$ at $R_p$ = 58 nm", xy=(Rp, Np), xytext=(68, 2.2e21), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", lw=0.6))
    ax.set_xlim(0, 250); ax.set_ylim(1e16, 1e22)
    ax.set_xlabel("Depth (nm)")
    ax.set_ylabel("As concentration (cm$^{-3}$)")
    ax.legend(loc="center right", fontsize=7.5, bbox_to_anchor=(1.0, 0.62))
    axr = ax.twinx(); axr.spines["right"].set_visible(True)
    dmg = 4.5 * np.exp(-(x - 0.75 * Rp) ** 2 / (2 * 32.9**2))
    axr.plot(x, dmg, color=COLORS[2], lw=1.4, ls="-.")
    axr.axhline(1.0, xmax=0.6, color=COLORS[2], ls=(0, (1, 2)), lw=1)
    axr.text(3, 1.12, "amorphisation threshold", color=COLORS[2], fontsize=7.5)
    axr.text(8, 4.6, "displaced Si atoms\n(right axis)", color=COLORS[2], fontsize=7.5)
    axr.set_ylim(0, 9)
    axr.set_ylabel(r"Displaced-atom density ($10^{22}$ cm$^{-3}$)", color=COLORS[2])
    save(fig, "50", "fig-50-4-implant-profile-damage")


# ---------------------------------------------------------------- Figure 50.5
def _mask(ax, x0, x1, y, h=0.35):
    ax.add_patch(Rectangle((x0, y), x1 - x0, h, fc="white", ec=INK, lw=0.8, hatch="////"))


def etch_profiles():
    fig, axs = plt.subplots(1, 4, figsize=(6.8, 3.7))
    for a in axs:
        a.set_xlim(0, 4); a.set_ylim(-0.3, 5.6); a.set_aspect("equal"); a.axis("off")

    def foot(a, text):
        a.text(2, -0.45, text, fontsize=7, ha="center", va="top")

    # (a) isotropic wet etch of SiO2 on Si
    a = axs[0]
    a.add_patch(Rectangle((0, 0), 4, 1.2, fc=SI, ec="none"))
    d = 1.4
    top = 1.2 + 2.0
    arcR = np.c_[2.5 + d * np.cos(np.linspace(0, -np.pi / 2, 30)), top + d * np.sin(np.linspace(0, -np.pi / 2, 30))]
    arcL = np.c_[1.5 + d * np.cos(np.linspace(-np.pi / 2, -np.pi, 30)), top + d * np.sin(np.linspace(-np.pi / 2, -np.pi, 30))]
    ox = np.vstack([[0, 1.2], [4, 1.2], [4, top], [2.5 + d, top], arcR, arcL, [0, top]])
    a.add_patch(Polygon(ox, fc=OXIDE, ec=INK, lw=0.8))
    _mask(a, 0, 1.5, top); _mask(a, 2.5, 4, top)
    a.annotate("", xy=(1.5 - d, top - 0.15), xytext=(1.5, top - 0.15),
               arrowprops=dict(arrowstyle="<|-|>", lw=0.6, mutation_scale=6))
    a.text(0.8, top + 0.5, "undercut = depth", fontsize=6.5, ha="center", va="bottom")
    a.text(2, 0.5, "Si", fontsize=7.5, ha="center")
    a.text(3.5, 1.45, "SiO$_2$", fontsize=7, ha="center")
    foot(a, "A = 0\nS(oxide:Si) ≈ 30–100")
    a.set_title("(a) Wet HF, SiO$_2$:\nisotropic", fontsize=8)
    # (b) KOH on (100) Si
    a = axs[1]
    dd = 1.6
    wb = 0.5
    wt = wb + 2 * dd / np.tan(np.radians(54.74))
    xc = 2.0
    st = 3.0
    si = [[0, 0], [4, 0], [4, st], [xc + wt / 2, st], [xc + wb / 2, st - dd], [xc - wb / 2, st - dd],
          [xc - wt / 2, st], [0, st]]
    a.add_patch(Polygon(si, fc=SI, ec=INK, lw=0.8))
    _mask(a, 0, xc - wt / 2, st); _mask(a, xc + wt / 2, 4, st)
    a.add_patch(Arc((xc + wb / 2, st - dd), 0.8, 0.8, theta1=0, theta2=54.74, lw=0.8))
    a.text(xc + wb / 2 + 0.5, st - dd + 0.12, "54.7°", fontsize=6.5)
    a.annotate("", xy=(xc - wt / 2, st + 0.55), xytext=(xc + wt / 2, st + 0.55),
               arrowprops=dict(arrowstyle="<|-|>", lw=0.6, mutation_scale=6))
    a.text(xc, st + 0.65, r"$W_{top}$", fontsize=7, ha="center", va="bottom")
    a.text(xc, st - dd - 0.1, r"$W_{bottom}$", fontsize=7, ha="center", va="top")
    a.annotate("", xy=(xc, st), xytext=(xc, st - dd), arrowprops=dict(arrowstyle="<|-|>", lw=0.6, mutation_scale=6))
    a.text(xc + 0.1, st - dd / 2, "d", fontsize=7.5, va="center")
    a.annotate("{111}", xy=(xc + wb / 2 + 0.6 * dd / np.tan(np.radians(54.74)), st - 0.4 * dd),
               xytext=(3.45, 2.75), fontsize=7, ha="center", va="center",
               arrowprops=dict(arrowstyle="-", lw=0.5))
    a.text(0.6, 3.75, "SiN$_x$ mask", fontsize=6.5, ha="center")
    foot(a, "A ≈ 1 along {111}\nS(Si:SiN) > 1000")
    a.set_title("(b) KOH, (100) Si:\ncrystallographic", fontsize=8)
    # (c) RIE of SiO2
    a = axs[2]
    a.add_patch(Rectangle((0, 0), 4, 1.2, fc=SI, ec="none"))
    top = 3.2
    a.add_patch(Polygon([[0, 1.2], [4, 1.2], [4, top], [2.5, top], [2.45, 1.2], [1.55, 1.2], [1.5, top], [0, top]],
                        fc=OXIDE, ec=INK, lw=0.8))
    for xs in ([1.5, 1.55], [2.5, 2.45]):
        a.plot(xs, [top, 1.25], color="#6B4C9A", lw=2.2)
    _mask(a, 0, 1.5, top); _mask(a, 2.5, 4, top)
    for xi in (1.75, 2.0, 2.25):
        a.annotate("", xy=(xi, 1.5), xytext=(xi, 4.6), arrowprops=dict(arrowstyle="-|>", lw=0.9, color=COLORS[1], mutation_scale=7))
    a.text(2.0, 4.7, "ions", fontsize=7, color=COLORS[1], ha="center", va="bottom")
    rng = np.random.default_rng(2)
    for p in [(0.4, 4.1), (0.9, 4.7), (0.6, 5.1), (3.2, 4.1), (3.6, 4.7), (3.0, 5.0)]:
        ang = rng.uniform(0, 2 * np.pi)
        p = np.array(p)
        a.annotate("", xy=p + 0.35 * np.array([np.cos(ang), np.sin(ang)]), xytext=p,
                   arrowprops=dict(arrowstyle="-|>", lw=0.7, color=COLORS[2], mutation_scale=6))
    a.text(0.7, 3.6, "radicals", fontsize=7, color=COLORS[2], ha="center")
    a.text(3.3, 3.6, "radicals", fontsize=7, color=COLORS[2], ha="center")
    a.annotate("sidewall\npolymer", xy=(2.48, 2.0), xytext=(3.25, 1.95), fontsize=6.5, color="#4B2C7A",
               ha="center", va="center", arrowprops=dict(arrowstyle="-", lw=0.5, color="#4B2C7A"))
    foot(a, "A ≈ 0.9–0.98\nS(oxide:resist) ≈ 3–10")
    a.set_title("(c) RIE, SiO$_2$:\nion-assisted", fontsize=8)
    # (d) Bosch DRIE
    a = axs[3]
    w = 0.22
    xc = 2.0
    ytop, ybot = 5.0, 0.2
    n = 18
    ys = np.linspace(ytop, ybot, n + 1)
    right = []
    for i in range(n):
        yy = np.linspace(ys[i], ys[i + 1], 8)
        bulge = 0.06 * np.sin(np.linspace(0, np.pi, 8))
        right += list(np.c_[xc + w + bulge, yy])
    right = np.array(right)
    left = np.c_[2 * xc - right[:, 0], right[:, 1]]
    si = np.vstack([[0, -0.3], [4, -0.3], [4, ytop], right, left[::-1], [0, ytop]])
    a.add_patch(Polygon(si, fc=SI, ec=INK, lw=0.6))
    _mask(a, 0, xc - w, ytop, 0.3); _mask(a, xc + w, 4, ytop, 0.3)
    a.text(2.45, 3.6, "cycles:\netch (SF$_6$)\npassivate (C$_4$F$_8$)", fontsize=6.5, va="center")
    a.text(1.55, 1.2, "AR\n> 20:1", fontsize=7, ha="right", va="center")
    a.text(1, -1.0, "", fontsize=1)
    a.text(2, -0.45, "A ≈ 0.99\nS(Si:resist) 50–100", fontsize=7, ha="center", va="top")
    a.set_title("(d) Bosch DRIE, Si:\nscalloped walls", fontsize=8)
    fig.tight_layout(w_pad=0.3)
    save(fig, "50", "fig-50-5-etch-profiles")


# ---------------------------------------------------------------- Figure 50.6
def damascene():
    fig, ax = schematic(6.8, 5.0, xlim=(0, 13.6), ylim=(0, 10))
    W = 9.0
    CU, BAR, CAP, LOWK = "#D9822B", "#2F4F4F", "#5E8C61", "#F3EEDC"
    # substrate, n+ region
    ax.add_patch(Rectangle((0, 0), W, 1.4, fc=SI, ec="none"))
    ax.add_patch(Rectangle((2.0, 0.6), 3.0, 0.8, fc="#9FB7D0", ec="none"))
    ax.text(2.3, 0.85, "n$^+$", fontsize=8, ha="center")
    ax.text(0.3, 0.5, "Si substrate", fontsize=8)
    # pre-metal dielectric, then NiSi and W plug
    ax.add_patch(Rectangle((0, 1.4), W, 2.0, fc="#E5EEF5", ec=INK, lw=0.5))
    ax.add_patch(Rectangle((2.4, 1.24), 2.2, 0.18, fc="#7D5BA6", ec="none"))
    ax.text(4.75, 1.2, "NiSi", fontsize=7.5, color="#4B2C7A", va="center")
    ax.text(0.3, 2.4, "pre-metal\ndielectric", fontsize=7.5, va="center")
    ax.add_patch(Rectangle((3.15, 1.42), 0.7, 1.98, fc=BAR, ec="none"))
    ax.add_patch(Rectangle((3.25, 1.52), 0.5, 1.88, fc="#A9A9A9", ec="none"))
    ax.text(3.5, 2.5, "W", fontsize=8, ha="center", va="center")
    ax.text(4.05, 2.5, "W contact plug,\nTi/TiN liner", fontsize=7.3, va="center")

    def cu_line(x0, x1, yb, yt, dish=0.0):
        b = 0.12
        ax.add_patch(Rectangle((x0, yb), x1 - x0, yt - yb, fc=BAR, ec="none"))
        ax.add_patch(Rectangle((x0 + b, yb + b), x1 - x0 - 2 * b, yt - yb - b, fc=CU, ec="none"))
        if dish:
            xs = np.linspace(x0 + b, x1 - b, 40)
            dep = yt - dish * np.sin(np.pi * (xs - xs[0]) / (xs[-1] - xs[0]))
            ax.add_patch(Polygon(np.vstack([np.c_[xs, dep], [[x1 - b, yt], [x0 + b, yt]]]), fc=CAP, ec="none"))
    # M1 level
    y1 = 3.4
    ax.add_patch(Rectangle((0, y1), W, 1.6, fc=LOWK, ec=INK, lw=0.5))
    ax.text(0.3, y1 + 0.8, "low-k SiCOH\n(k ≈ 2.7)", fontsize=7.5, va="center")
    cu_line(2.5, 4.5, y1, y1 + 1.6)
    cu_line(5.6, 8.6, y1, y1 + 1.6, dish=0.15)
    ax.text(3.5, y1 + 0.75, "Cu M1", fontsize=8, ha="center", va="center")
    ax.text(7.1, y1 + 0.7, "wide Cu line", fontsize=7.5, ha="center", va="center")
    ax.add_patch(Rectangle((0, y1 + 1.6), W, 0.2, fc=CAP, ec="none"))
    # M2 level (via + trench, one fill)
    y2 = y1 + 1.8
    ax.add_patch(Rectangle((0, y2), W, 3.2, fc=LOWK, ec=INK, lw=0.5))
    ax.add_patch(Rectangle((0, y2 + 1.5), W, 0.18, fc="#E6B85C", ec="none"))
    b = 0.12
    via = [[3.1, y2 - 0.2], [3.9, y2 - 0.2], [3.9, y2 + 1.7], [6.5, y2 + 1.7], [6.5, y2 + 3.2],
           [1.5, y2 + 3.2], [1.5, y2 + 1.7], [3.1, y2 + 1.7]]
    ax.add_patch(Polygon(via, fc=BAR, ec="none"))
    inner = [[3.1 + b, y2 - 0.2 + b], [3.9 - b, y2 - 0.2 + b], [3.9 - b, y2 + 1.7 + b], [6.5 - b, y2 + 1.7 + b],
             [6.5 - b, y2 + 3.2], [1.5 + b, y2 + 3.2], [1.5 + b, y2 + 1.7 + b], [3.1 + b, y2 + 1.7 + b]]
    ax.add_patch(Polygon(inner, fc=CU, ec="none"))
    ax.add_patch(Rectangle((0, y2 + 3.2), W, 0.2, fc=CAP, ec="none"))
    ax.text(3.2, y2 + 2.45, "Cu M2 trench", fontsize=8, ha="center", va="center")
    ax.text(3.5, y2 + 0.7, "via", fontsize=8, ha="center", va="center")
    ax.text(0.3, y2 + 0.75, "low-k", fontsize=7.5, va="center")
    # labels on right
    lx = 9.3

    def lab(y, text, xy, color=INK):
        ax.annotate(text, xy=xy, xytext=(lx, y), fontsize=7.3, va="center", color=color,
                    arrowprops=dict(arrowstyle="-", lw=0.5, color="0.4"))
    lab(9.65, "SiCN cap (Cu diffusion barrier)", (8.6, y2 + 3.3))
    lab(8.85, "dual damascene: via + trench\nin one Cu fill, continuous barrier", (5.6, y2 + 2.9))
    lab(7.85, "TaN/Ta barrier 2–5 nm\n(drawn exaggerated) + Cu seed", (6.44, y2 + 2.3))
    lab(6.95, "etch-stop layer", (7.6, y2 + 1.6))
    lab(6.15, "electromigration fastest\nalong Cu/cap interface", (8.4, y1 + 1.62), COLORS[1])
    lab(5.2, "CMP dishing on wide line", (7.1, y1 + 1.5))
    # inset: resistivity vs width
    ins = ax.inset_axes([10.3, 0.9, 3.2, 2.9], transform=ax.transData)
    w = np.linspace(10, 200, 300)
    lam, p, Rg, rho0 = 39.0, 0.3, 0.25, 1.72
    h = 2 * w
    core = rho0 * (1 + 0.375 * (1 - p) * lam * (1 / w + 1 / h) + 1.5 * Rg / (1 - Rg) * lam / w)
    tb = 2.0
    eff = core * (w * h) / ((w - 2 * tb) * (h - tb))
    ins.plot(w, eff, color=COLORS[1], lw=1.3, label="with 2 nm barrier")
    ins.plot(w, core, color=COLORS[0], lw=1.3, label="scattering only")
    ins.axhline(1.72, color="0.5", ls=":", lw=0.8)
    ins.text(198, 1.3, "bulk 1.7", fontsize=6, ha="right", va="top", color="0.4")
    ins.set_xlim(10, 200); ins.set_ylim(0, 15)
    ins.set_xlabel("line width (nm)", fontsize=6.5, labelpad=1)
    ins.set_ylabel(r"$\rho_{\rm eff}$ (µΩ·cm)", fontsize=6.5, labelpad=1)
    ins.tick_params(labelsize=6)
    ins.legend(fontsize=5.8, loc="upper right", handlelength=1.0)
    ins.set_title("barrier + scattering raise\nresistance as width shrinks", fontsize=6.8)
    print("rho at 10/20/100 nm:", [round(float(np.interp(v, w, core)), 2) for v in (10, 20, 100)],
          [round(float(np.interp(v, w, eff)), 2) for v in (10, 20, 100)])
    save(fig, "50", "fig-50-6-dual-damascene-cross-section")


if __name__ == "__main__":
    cz_fz()
    deal_grove()
    erfc_gauss()
    implant()
    etch_profiles()
    damascene()
