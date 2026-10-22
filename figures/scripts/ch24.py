"""Figures for Chapter 24 — Thermal Properties.

Run from the repository root:  python figures/scripts/ch24.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Ellipse, Polygon
from scipy.integrate import quad
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq

from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK

R_GAS = 8.314


def debye(t):
    """C_v/3R for reduced temperature t = T/theta_D."""
    if t <= 0:
        return 0.0
    x = 1.0 / t
    val = quad(lambda u: u ** 4 * np.exp(-u) / (-np.expm1(-u)) ** 2 if u > 1e-8 else u * u, 0, min(x, 200), limit=200)[0]
    return 3 * t ** 3 * val


def einstein(t, ratio=0.806):
    """C_v/3R for T/theta_D = t with theta_E = ratio * theta_D."""
    if t <= 0:
        return 0.0
    x = ratio / t
    if x > 300:
        return 0.0
    return x * x * np.exp(x) / np.expm1(x) ** 2


# ---------------------------------------------------------------- 24.1
def debye_einstein_heat_capacity():
    fig, ax = new_fig(6.4, 4.2)
    t = np.linspace(0.002, 1.5, 500)
    cd = np.array([debye(v) for v in t])
    ce = np.array([einstein(v) for v in t])
    ax.axhline(1.0, color="0.5", lw=0.9, ls=":")
    ax.text(1.49, 1.012, "Dulong–Petit 3R", ha="right", va="bottom", fontsize=8, color="0.35")
    ax.plot(t, cd, color=COLORS[0], label="Debye")
    ax.plot(t, ce, color=COLORS[1], ls="--", label=r"Einstein, $\theta_E=0.806\,\theta_D$")
    pts = [("Cu", 300 / 343, COLORS[2]), ("Si", 300 / 645, COLORS[3]), ("diamond", 300 / 2230, COLORS[4])]
    for lab, x, c in pts:
        y = debye(x)
        ax.plot(x, y, "o", color=c, ms=7, zorder=5, mec="white")
    ax.annotate("Cu, 300 K\n(0.875, 0.938)", xy=(300 / 343, debye(300 / 343)), xytext=(1.0, 0.74), fontsize=7.8,
                arrowprops=dict(arrowstyle="-", lw=0.6, color="0.4"))
    ax.annotate("Si, 300 K\n(0.465, 0.802)", xy=(300 / 645, debye(300 / 645)), xytext=(0.5, 0.6), fontsize=7.8,
                arrowprops=dict(arrowstyle="-", lw=0.6, color="0.4"))
    xd = 300 / 2230
    ax.plot(xd, 0.245, "o", mfc="white", mec=COLORS[4], mew=1.6, ms=7, zorder=5)
    ax.annotate("diamond, 300 K: Debye 0.166\n(open: measured 0.245)", xy=(xd, 0.2), xytext=(0.2, 0.1), fontsize=7.8,
                arrowprops=dict(arrowstyle="-", lw=0.6, color="0.4"))
    ax.plot(0.146, debye(0.146), "s", color=COLORS[0], ms=4)
    ax.annotate("Cu at 50 K: 0.200", xy=(0.146, debye(0.146)), xytext=(0.2, 0.33), fontsize=7.5, color=COLORS[0],
                arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[0]))
    ax.set_xlim(0, 1.5)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel(r"reduced temperature $T/\theta_D$")
    ax.set_ylabel(r"$C_v/3R$")
    ax.legend(loc="upper left", fontsize=8.5, bbox_to_anchor=(0.02, 0.97))

    # inset: copper at low temperature
    ins = fig.add_axes([0.62, 0.25, 0.27, 0.3])
    T = np.logspace(0, np.log10(50), 200)
    gam = 0.695e-3
    lat = np.array([3 * R_GAS * debye(x / 343) for x in T])
    t3 = 12 * np.pi ** 4 / 5 * R_GAS * (T / 343) ** 3
    ins.loglog(T, lat + gam * T, color=INK, lw=1.4, label="total")
    ins.loglog(T, t3, color=COLORS[0], lw=1.0, ls="--")
    ins.loglog(T, gam * T, color=COLORS[1], lw=1.0, ls="--")
    tx = (gam / (12 * np.pi ** 4 / 5 * R_GAS / 343 ** 3)) ** 0.5
    ins.plot(tx, gam * tx, "o", color=INK, ms=3.5)
    ins.text(1.6, 5e-2, r"lattice $\propto T^3$", color=COLORS[0], fontsize=7)
    ins.text(12, 1.6e-3, r"electronic $\gamma T$", color=COLORS[1], fontsize=7, va="top")
    ins.text(tx * 1.15, gam * tx * 0.45, f"{tx:.1f} K", fontsize=6.8, va="top")
    ins.set_xlim(1, 50)
    ins.set_ylim(1e-4, 10)
    ins.set_xlabel("T (K)", fontsize=7, labelpad=1)
    ins.set_ylabel(r"$C$ (J mol$^{-1}$K$^{-1}$)", fontsize=7, labelpad=1)
    ins.tick_params(labelsize=6.5)
    ins.set_title("Cu, 1–50 K", fontsize=7.5, pad=2)
    save(fig, "24", "fig-24-1-debye-einstein-heat-capacity")


# ---------------------------------------------------------------- 24.2
def anharmonic_potential():
    fig, (ax, axb) = plt.subplots(1, 2, figsize=(6.8, 4.0), gridspec_kw=dict(width_ratios=[1.45, 1], wspace=0.42))
    a = 4.0
    r = np.linspace(0.8, 1.6, 600)
    U = (1 - np.exp(-a * (r - 1))) ** 2 - 1
    Uh = -1 + a * a * (r - 1) ** 2
    ax.plot(r, U, color=COLORS[0], lw=2, label="Morse-type")
    ax.plot(r, Uh, color="0.45", ls="--", lw=1.2, label="harmonic")
    ax.axvline(1.0, color="0.75", lw=0.7, ls=":")
    levels = [(-0.85, "$T_1$"), (-0.6, "$T_2$"), (-0.35, "$T_3$")]
    mids = []
    for E, lab in levels:
        f = lambda x: (1 - np.exp(-a * (x - 1))) ** 2 - 1 - E
        r1 = brentq(f, 0.7, 1.0)
        r2 = brentq(f, 1.0, 3.0)
        ax.plot([r1, r2], [E, E], color=COLORS[1], lw=1.2)
        m = (r1 + r2) / 2
        mids.append((m, E))
        ax.plot(m, E, "o", color=COLORS[1], ms=5, zorder=5)
        ax.text(r2 + 0.012, E, lab, ha="left", va="center", fontsize=8.5, color=COLORS[1])
        # harmonic turning points: symmetric about r0
        dh = np.sqrt((E + 1) / a ** 2)
        ax.plot(1.0, E, "s", mfc="white", mec="0.45", ms=4, zorder=4)
    mids = np.array(mids)
    ax.plot(mids[:, 0], mids[:, 1], color=COLORS[1], lw=1.0)
    ax.annotate("mean separation\nincreases:\nthermal expansion", xy=(mids[-1, 0], mids[-1, 1]), xytext=(1.32, -0.88),
                fontsize=7.8, color=COLORS[1], arrowprops=dict(arrowstyle="-|>", lw=0.7, mutation_scale=7, color=COLORS[1]))
    ax.annotate("harmonic: midpoints stay\nat $r_0$ (no expansion)", xy=(1.0, -0.6), xytext=(0.82, 0.27), fontsize=7.6,
                color="0.35", arrowprops=dict(arrowstyle="-|>", lw=0.7, mutation_scale=7, color="0.45"))
    ax.set_xlim(0.8, 1.6)
    ax.set_ylim(-1.05, 0.55)
    ax.set_xlabel(r"interatomic separation $r/r_0$")
    ax.set_ylabel("potential energy $U$ (arb. units)")
    ax.legend(loc="upper right", fontsize=7.6)
    ax.set_yticks([-1, -0.5, 0, 0.5])

    data = [("PE", 150), ("PMMA", 70), ("Pb", 29), ("Al", 23), ("Cu", 16.5), ("steel", 12), ("Al$_2$O$_3$", 8),
            ("W", 4.5), ("SiC", 4.0), ("Invar", 1.2), ("diamond", 1.0), ("fused silica", 0.5)]
    cols = {"PE": COLORS[3], "PMMA": COLORS[3], "Pb": COLORS[0], "Al": COLORS[0], "Cu": COLORS[0], "steel": COLORS[0],
            "Invar": COLORS[0], "W": COLORS[0]}
    names = [d[0] for d in data][::-1]
    vals = [d[1] for d in data][::-1]
    cc = [cols.get(n, COLORS[2]) for n in names]
    axb.barh(range(len(vals)), vals, color=cc, height=0.65)
    axb.set_xscale("log")
    axb.set_xlim(0.3, 400)
    axb.set_yticks(range(len(vals)))
    axb.set_yticklabels(names, fontsize=7.8)
    for i, v in enumerate(vals):
        axb.text(v * 1.12, i, f"{v:g}", va="center", fontsize=7)
    axb.set_xlabel(r"$\alpha$ (ppm/K)")
    axb.set_xticks([1, 10, 100])
    axb.set_xticklabels(["1", "10", "100"])
    axb.set_title("linear expansion, ~300 K", fontsize=8.5)
    axb.text(0.98, 0.02, "metals", color=COLORS[0], fontsize=7, transform=axb.transAxes, ha="right", va="bottom")
    axb.text(0.98, 0.09, "ceramics, glass, C", color=COLORS[2], fontsize=7, transform=axb.transAxes, ha="right", va="bottom")
    axb.text(0.98, 0.16, "polymers", color=COLORS[3], fontsize=7, transform=axb.transAxes, ha="right", va="bottom")
    save(fig, "24", "fig-24-2-anharmonic-potential")


# ---------------------------------------------------------------- 24.3
def conductivity_vs_temperature():
    fig, ax = new_fig(6.8, 5.0)
    C_CER, C_MET, C_ALL, C_AMO, C_INS = COLORS[0], COLORS[1], COLORS[3], COLORS[2], "#7F7F7F"
    curves = [
        ("diamond", [(250, 2800), (300, 2200), (400, 1650), (500, 1300), (600, 1080), (800, 800), (1000, 650)], C_CER, "-"),
        ("Cu", [(200, 413), (300, 401), (400, 393), (600, 379), (800, 366), (1000, 352), (1200, 339)], C_MET, "-"),
        ("Al", [(200, 237), (300, 237), (400, 240), (600, 231), (800, 218), (933, 210)], C_MET, "--"),
        ("AlN", [(300, 175), (400, 140), (600, 100), (800, 80), (1000, 68), (1200, 60)], C_CER, "--"),
        ("SiC (sintered)", [(300, 120), (400, 100), (600, 75), (800, 62), (1000, 55), (1200, 50)], C_CER, "-."),
        ("carbon steel", [(300, 50), (400, 48), (600, 42), (800, 36), (1000, 30), (1200, 28)], C_ALL, "-"),
        ("Al$_2$O$_3$", [(250, 46), (300, 35), (400, 26), (600, 16), (800, 12), (1000, 9), (1300, 7)], C_CER, ":"),
        ("304 stainless", [(250, 15), (300, 16), (400, 16.6), (600, 19.8), (800, 22.6), (1000, 25.4), (1200, 28)], C_ALL, "--"),
        ("Ti-6Al-4V", [(250, 6.4), (300, 6.7), (400, 7.6), (600, 10), (800, 13), (900, 15), (1000, 17)], C_ALL, ":"),
        ("dense YSZ", [(300, 2.5), (600, 2.35), (900, 2.25), (1300, 2.2)], C_AMO, "-."),
        ("concrete", [(250, 1.75), (300, 1.7), (400, 1.6), (500, 1.5)], C_AMO, ":"),
        ("fused silica", [(250, 1.3), (300, 1.4), (400, 1.5), (600, 1.7), (800, 1.9), (1000, 2.0), (1200, 2.1)], C_AMO, "-"),
        ("plasma-sprayed YSZ", [(300, 1.0), (700, 0.95), (1000, 0.95), (1300, 1.0)], C_AMO, "--"),
        ("HDPE", [(250, 0.5), (300, 0.45), (350, 0.42), (400, 0.38)], C_AMO, "-"),
        ("mineral wool", [(250, 0.032), (300, 0.035), (500, 0.055), (700, 0.09), (900, 0.15)], C_INS, "-"),
    ]
    label_pos = {
        "diamond": (1010, 650, "left"), "Cu": (1210, 339, "left"), "Al": (945, 205, "left"),
        "AlN": (1210, 66, "left"), "SiC (sintered)": (1210, 46, "left"), "carbon steel": (1210, 34, "left"),
        "Al$_2$O$_3$": (1310, 6.6, "left"), "304 stainless": (1210, 23, "left"), "Ti-6Al-4V": (1010, 16, "left"),
        "dense YSZ": (1310, 2.65, "left"), "concrete": (330, 1.2, "left"), "fused silica": (1210, 1.85, "left"),
        "plasma-sprayed YSZ": (1310, 0.95, "left"), "HDPE": (410, 0.37, "left"), "mineral wool": (910, 0.15, "left"),
    }
    for name, pts, col, ls in curves:
        T, k = np.array(pts).T
        f = PchipInterpolator(T, np.log10(k))
        tt = np.linspace(T[0], T[-1], 200)
        ax.plot(tt, 10 ** f(tt), color=col, ls=ls, lw=1.6)
        x, y, ha = label_pos[name]
        ax.text(x, y, name, fontsize=7.2, color=col, ha=ha, va="center")
    ax.set_yscale("log")
    ax.set_xlim(200, 1700)
    ax.set_ylim(0.02, 3000)
    ax.set_xticks([200, 400, 600, 800, 1000, 1200])
    ax.spines["bottom"].set_bounds(200, 1300)
    ax.set_xlabel("temperature (K)")
    ax.set_ylabel("thermal conductivity $k$ (W m$^{-1}$ K$^{-1}$)")
    ax.set_yticks([0.1, 1, 10, 100, 1000])
    ax.set_yticklabels(["0.1", "1", "10", "100", "1000"])
    ax.text(560, 1600, "Umklapp: $k\\propto1/T$", fontsize=8, color=C_CER, ha="left")
    ax.text(470, 470, "electrons: nearly flat", fontsize=8, color=C_MET)
    ax.text(650, 5.0, "solute scattering: rising", fontsize=8, color=C_ALL, ha="center", va="center")
    ax.text(700, 0.48, "disorder-limited\n(glasses, polymers, porous YSZ)", fontsize=8, color=C_AMO, ha="center")
    ax.text(560, 0.045, "radiation adds $\\propto T^3$", fontsize=7.8, color=C_INS, ha="left")
    for lab, c in (("crystalline ceramics", C_CER), ("pure metals", C_MET), ("alloys", C_ALL),
                   ("amorphous / disordered", C_AMO), ("insulation", C_INS)):
        ax.plot([], [], color=c, lw=2, label=lab)
    ax.legend(loc="lower right", fontsize=7.5, bbox_to_anchor=(1.0, 0.02))
    save(fig, "24", "fig-24-3-conductivity-vs-temperature")


# ---------------------------------------------------------------- 24.4
def _slab_surface_stress(Bi, tau):
    """Normalized surface stress (T_mean - T_surface)/dT for a plate quenched from both faces."""
    lam = []
    for n in range(60):
        lo, hi = n * np.pi + 1e-9, n * np.pi + np.pi / 2 - 1e-9
        lam.append(brentq(lambda x: x * np.tan(x) - Bi, lo, hi))
    lam = np.array(lam)
    C = 4 * np.sin(lam) / (2 * lam + np.sin(2 * lam))
    tau = np.atleast_1d(tau)[:, None]
    th_s = np.sum(C * np.exp(-lam ** 2 * tau) * np.cos(lam), axis=1)
    th_m = np.sum(C * np.exp(-lam ** 2 * tau) * np.sin(lam) / lam, axis=1)
    return th_m - th_s


def thermal_shock_ranking():
    fig = plt.figure(figsize=(6.8, 5.0))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.25, 1], hspace=0.55, wspace=0.55)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[1, 0])
    ax4 = fig.add_subplot(gs[1, 1])
    Rv = [("soda-lime glass", 62), ("alumina", 90), ("borosilicate", 189), ("SiC", 212), ("3Y-TZP", 325),
          ("Si$_3$N$_4$", 589), ("fused silica", 1050)]
    Rp = [("soda-lime glass", 62), ("borosilicate", 208), ("3Y-TZP", 810), ("fused silica", 1470), ("alumina", 2700),
          ("Si$_3$N$_4$", 14700), ("SiC", 25400)]
    cmap = {"soda-lime glass": COLORS[3], "borosilicate": COLORS[3], "fused silica": COLORS[3]}
    for ax, data, xl, lim, title in ((ax1, Rv, r"$R=\Delta T_c$ (K)", (30, 3000), "fast quench: $R$"),
                                     (ax2, Rp, r"$R'=Rk$ (W/m)", (30, 30000), "slow heat transfer: $R'$")):
        names = [d[0] for d in data]
        vals = [d[1] for d in data]
        ax.barh(range(len(vals)), vals, color=[cmap.get(n, COLORS[0]) for n in names], height=0.62, left=lim[0] * 0 + 1e-9)
        ax.set_xscale("log")
        ax.set_xlim(*lim)
        ax.set_yticks(range(len(vals)))
        ax.set_yticklabels(names, fontsize=7.8)
        for i, v in enumerate(vals):
            ax.text(v * 1.1, i, f"{v:,}", va="center", fontsize=7)
        ax.set_xlabel(xl, fontsize=9)
        ax.set_title(title, fontsize=9)
        ax.tick_params(axis="x", labelsize=7.5)
    ax1.text(0.98, 0.02, "glasses", color=COLORS[3], fontsize=7, transform=ax1.transAxes, ha="right")
    ax1.text(0.98, 0.10, "technical ceramics", color=COLORS[0], fontsize=7, transform=ax1.transAxes, ha="right")

    tau = np.concatenate([np.linspace(1e-4, 0.02, 200), np.linspace(0.02, 1.5, 400)])
    ax3.axhline(0, color="0.6", lw=0.5)
    for Bi, c, lab in ((0.5, COLORS[2], "Bi = 0.5"), (2.0, COLORS[1], "Bi = 2"), (1e4, COLORS[0], "Bi → ∞")):
        sstar = _slab_surface_stress(Bi, tau)
        tt = tau
        if Bi > 100:   # instantaneous surface change: stress is 1 at t = 0
            tt, sstar = np.concatenate([[0.0], tau]), np.concatenate([[1.0], sstar])
        i = np.argmax(sstar)
        ax3.plot(tt, sstar, color=c, lw=1.5, label=f"{lab}: peak {sstar[i]:.2f}")
        ax3.plot(tt[i], sstar[i], "o", color=c, ms=3.5)
    ax3.set_xlim(0, 1.5)
    ax3.legend(loc="upper right", fontsize=7.2)
    ax3.set_ylim(0, 1.15)
    ax3.set_xlabel(r"time $at/L^2$", fontsize=8.5)
    ax3.set_ylabel("surface stress\n" r"$\div\,E\alpha\Delta T/(1-\nu)$", fontsize=8)
    ax3.tick_params(labelsize=7.5)
    ax3.set_title("quenched plate (half-thickness $L$)", fontsize=8.5)

    ax4.axis("off")
    ax4.text(0.5, 0.62, "rapid quench (high Bi)\n→ $R$ governs\n\nslow heat transfer (low Bi)\n→ $R'$ governs",
             ha="center", va="center", fontsize=8.5,
             bbox=dict(fc="#EEF3F8", ec=INK, lw=0.8, boxstyle="round,pad=0.5"))
    ax4.text(0.5, 0.05, "Manson: peak ≈ 1/(1.5 + 3.25/Bi − 0.5 e$^{-16/\\mathrm{Bi}}$)", ha="center", fontsize=7.2,
             color="0.35")
    save(fig, "24", "fig-24-4-thermal-shock-ranking")


# ---------------------------------------------------------------- 24.5
def tbc_temperature_profile():
    fig, (axl, axr) = plt.subplots(1, 2, figsize=(6.8, 4.6), sharey=True, gridspec_kw=dict(width_ratios=[1, 1.15], wspace=0.08))
    # depth coordinate (mm), positive downward; plotted with inverted y
    d_ysz, d_tgo, d_bc, d_wall = 0.25, 0.004, 0.10, 1.5
    z0 = 0.0
    z1 = z0 + d_ysz
    z2 = z1 + d_tgo
    z3 = z2 + d_bc
    z4 = z3 + d_wall
    zg, zc = -0.45, z4 + 0.45
    rng = np.random.default_rng(2)
    axl.set_xlim(0, 1)
    axl.add_patch(Rectangle((0, zg), 1, -zg, fc="#FDE3D2", ec="none"))
    axl.add_patch(Rectangle((0, z0), 1, d_ysz, fc="#F2F2F2", ec=INK, lw=0.8))
    for x in np.arange(0.05, 1.0, 0.08):            # columnar / vertical cracks
        axl.plot([x + rng.normal(0, 0.005), x], [z0 + 0.005, z1 - 0.01], color="0.55", lw=0.6)
    for _ in range(45):                              # pores
        axl.add_patch(Ellipse((rng.uniform(0.02, 0.98), rng.uniform(z0 + 0.03, z1 - 0.03)), 0.03, 0.012, fc="0.75", ec="none"))
    axl.add_patch(Rectangle((0, z1), 1, 0.012, fc="#333333", ec="none"))   # TGO (drawn thicker than scale)
    axl.add_patch(Rectangle((0, z2 + 0.008), 1, d_bc - 0.008, fc="#C9D3DC", ec=INK, lw=0.8))
    axl.add_patch(Rectangle((0, z3), 1, d_wall, fc="#9AA5B1", ec=INK, lw=0.8))
    axl.add_patch(Rectangle((0, z4), 1, zc - z4, fc="#D6EAF8", ec="none"))
    axl.text(0.5, zg / 2, "hot gas ~1,500 °C", ha="center", va="center", fontsize=8.5)
    axl.text(0.5, (z0 + z1) / 2, "YSZ top coat 250 μm", ha="center", va="center", fontsize=8,
             bbox=dict(fc="white", ec="none", pad=0.6, alpha=0.85))
    axl.annotate("TGO α-Al$_2$O$_3$, 3–5 μm", xy=(0.93, z1 + 0.006), xytext=(0.62, z1 + 0.25), fontsize=7.4,
                 arrowprops=dict(arrowstyle="-", lw=0.6), ha="center",
                 bbox=dict(fc="white", ec="none", pad=0.3, alpha=0.9))
    axl.text(0.5, (z2 + z3) / 2 + 0.005, "bond coat 100 μm (MCrAlY / Pt-aluminide)", ha="center", va="center", fontsize=6.9)
    axl.text(0.5, (z3 + z4) / 2, "superalloy wall\n1.5 mm", ha="center", va="center", fontsize=8.5)
    axl.text(0.5, (z4 + zc) / 2, "cooling air ~650 °C", ha="center", va="center", fontsize=8.5)
    axl.set_ylim(zc, zg)
    axl.set_ylabel("depth from coating surface (mm)")
    axl.set_xticks([])
    axl.spines["bottom"].set_visible(False)

    q = 0.8e6
    T_s, T_gas, T_cool = 1250.0, 1500.0, 650.0
    T1 = T_s - q * d_ysz * 1e-3 / 1.0
    T2 = T1
    T3 = T2 - q * d_bc * 1e-3 / 10.0
    T4 = T3 - q * d_wall * 1e-3 / 25.0
    zgz = np.linspace(zg, z0, 60)
    Tg = T_s + (T_gas - T_s) * (1 - np.exp((zgz - z0) / 0.08))
    zcz = np.linspace(z4, zc, 60)
    Tc = T_cool + (T4 - T_cool) * np.exp(-(zcz - z4) / 0.08)
    axr.plot(Tg, zgz, color=COLORS[1], lw=1.6, ls="--")
    axr.plot([T_s, T1, T2, T3, T4], [z0, z1, z2, z3, z4], color=COLORS[1], lw=2.2)
    axr.plot(Tc, zcz, color=COLORS[0], lw=1.6, ls="--")
    for zz in (z0, z1, z3, z4):
        axr.axhline(zz, color="0.85", lw=0.6, zorder=0)
    axr.plot(T_s, z0, "o", color=COLORS[1], ms=4)
    axr.text(T_s + 15, z0 + 0.03, "1,250 °C", fontsize=7.4, va="top")
    axr.plot(T1, z1, "o", color=COLORS[1], ms=4)
    axr.text(T1 - 15, z1, "1,050 °C", fontsize=7.4, va="center", ha="right")
    axr.plot(T3, z3, "o", color=COLORS[1], ms=4)
    axr.text(T3 + 15, z3 + 0.03, "1,042 °C", fontsize=7.4, va="top")
    axr.plot(T4, z4, "o", color=COLORS[1], ms=4)
    axr.text(T4 + 15, z4 - 0.02, "≈ 994 °C", fontsize=7.4, va="bottom")
    axr.annotate("", xy=(T1, -0.07), xytext=(T_s, -0.07), arrowprops=dict(arrowstyle="<|-|>", lw=0.8, mutation_scale=6))
    axr.text((T1 + T_s) / 2, -0.09, "200 K", ha="center", va="bottom", fontsize=7.6, fontweight="bold")
    axr.text(800, (z3 + z4) / 2, "48 K across\n1.5 mm of metal", fontsize=7.6, ha="center", va="center", color=COLORS[1])
    axr.text(1330, zg + 0.12, "gas-side film", fontsize=7.4, color=COLORS[1], va="center")
    axr.text(700, zc - 0.12, "coolant-side film", fontsize=7.4, color=COLORS[0], va="center")
    axr.text(1520, 0.95, "q = 0.8 MW/m²", fontsize=8.5, ha="right",
             bbox=dict(fc="#EEF3F8", ec=INK, lw=0.6, boxstyle="round,pad=0.3"))
    axr.text(1520, 1.42, "200 K across 0.25 mm of YSZ,\n8 K across the bond coat,\nversus 48 K across 1.5 mm of metal", fontsize=7.4,
             ha="right", va="center", color="0.25")
    axr.set_xlim(600, 1550)
    axr.set_xlabel("temperature (°C)")
    axr.tick_params(axis="y", left=False)
    axr.spines["left"].set_visible(False)
    save(fig, "24", "fig-24-5-tbc-temperature-profile")
    return T1, T3, T4


# ---------------------------------------------------------------- 24.6
def k_vs_cte_map():
    fig, ax = new_fig(6.8, 5.0)
    ax.set_yscale("log")
    ax.axvspan(2.5, 7.0, color=COLORS[2], alpha=0.10, lw=0)
    ax.text(4.75, 1.08, "Si, SiC, GaN, GaAs dies\nand ceramic substrates", ha="center", va="bottom", fontsize=7.5, color="#00704f")
    # guide lines of constant alpha/k
    xs = np.linspace(0.3, 25.5, 200)
    for ratio, lab in ((0.01, "α/k = 0.01"), (0.1, "0.1"), (1.0, "1 (ppm/K)/(W/m K)")):
        ax.plot(xs, xs / ratio, color="0.7", lw=0.7, ls="--", zorder=0)
    ax.text(11.0, 11.0 / 0.01 * 1.25, "α/k = 0.01", fontsize=6.8, color="0.5", rotation=0, ha="center")
    ax.text(21.5, 21.5 / 0.1 * 1.2, "0.1", fontsize=6.8, color="0.5", ha="center")
    ax.text(21.5, 21.5 / 1.0 * 1.15, "α/k = 1 (ppm/K)/(W/m K)", fontsize=6.8, color="0.5", ha="center")
    ax.annotate("better\n(low α/k)", xy=(10.6, 140), xytext=(13.2, 45), fontsize=7.6, color=COLORS[0], ha="center",
                arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.2, mutation_scale=10))

    # (label, a_lo, a_hi, k_lo, k_hi, colour, label position (x, y) or None, ha)
    C_M, C_C, C_S, C_X, C_P = COLORS[1], COLORS[0], COLORS[3], COLORS[4], COLORS[2]
    items = [
        ("diamond", 0.8, 1.2, 1000, 2200, C_C, (1.5, 1450), "left"),
        ("CVD diamond/Cu", 6, 7, 500, 700, C_X, (7.5, 590), "left"),
        ("Cu", 16.5, 17.5, 380, 401, C_M, (18.1, 390), "left"),
        ("Al", 22.6, 23.4, 230, 240, C_M, (23.0, 315), "center"),
        ("Al-6061", 23.2, 24.0, 160, 172, C_M, (23.6, 120), "center"),
        ("AlSiC 63 % / Cu–W 10–20 % Cu", 7, 8, 170, 200, C_X, (8.6, 178), "left"),
        (None, 6, 8, 180, 200, C_X, None, "left"),
        ("Cu–Mo–Cu", 6, 8, 200, 300, C_X, (8.6, 340), "left"),
        ("BeO", 7.3, 7.7, 250, 280, C_C, (8.6, 255), "left"),
        ("Kovar", 5.3, 5.7, 16, 18, C_M, (6.15, 17), "left"),
        ("Invar", 1.0, 1.4, 9.5, 10.5, C_M, (1.85, 10), "left"),
        ("AlN", 4.4, 4.8, 140, 180, C_C, (4.05, 150), "right"),
        ("SiC", 4.0, 4.4, 80, 150, C_C, (4.8, 95), "left"),
        ("Si$_3$N$_4$", 2.8, 3.2, 60, 90, C_C, (2.45, 72), "right"),
        ("Al$_2$O$_3$", 7, 8, 25, 35, C_C, (8.6, 30), "left"),
        ("Si", 2.5, 2.7, 145, 155, C_S, (2.2, 150), "right"),
        ("GaN", 5.5, 5.7, 180, 220, C_S, (5.0, 250), "right"),
        ("stainless steel", 16.5, 17.5, 15, 17, C_M, (18.1, 16), "left"),
        ("Ti-6Al-4V", 8.8, 9.2, 6.5, 7.5, C_M, (9.65, 7), "left"),
        ("pyrolytic graphite, in-plane", -1.2, -0.8, 1500, 1700, C_C, (-1.75, 640), "left"),
        ("pyrolytic graphite,\nthrough-plane", 24.5, 25.5, 5, 10, C_C, (24.2, 7), "right"),
    ]
    for lab, a0, a1, k0, k1, c, pos, ha in items:
        ax.fill([a0, a1, a1, a0], [k0, k0, k1, k1], color=c, alpha=0.45, lw=1.0, ec=c)
        if k1 / k0 < 1.08:
            ax.plot((a0 + a1) / 2, np.sqrt(k0 * k1), "o", color=c, ms=5)
        if lab:
            ax.text(pos[0], pos[1], lab, fontsize=7.2, ha=ha, va="center")
    ax.plot([-1.0, -1.0], [1500, 760], color="0.5", lw=0.6)
    ax.annotate("epoxy (α ≈ 60, k ≈ 0.2)\noff scale", xy=(25.8, 1.0), xytext=(20.5, 1.7), fontsize=7.2, ha="center",
                arrowprops=dict(arrowstyle="-|>", lw=0.9, mutation_scale=8))
    for lab, c in (("metals and alloys", C_M), ("ceramics and carbon", C_C), ("semiconductors", C_S),
                   ("metal-matrix composites", C_X)):
        ax.fill([], [], color=c, alpha=0.6, label=lab)
    ax.legend(loc="upper right", fontsize=7.4, frameon=True, framealpha=0.95, edgecolor="0.8")
    ax.set_xlim(-2, 26)
    ax.set_ylim(1, 2500)
    ax.set_yticks([1, 10, 100, 1000])
    ax.set_yticklabels(["1", "10", "100", "1000"])
    ax.set_xlabel("coefficient of thermal expansion α (ppm/K)")
    ax.set_ylabel("thermal conductivity $k$ (W m$^{-1}$ K$^{-1}$)")
    save(fig, "24", "fig-24-6-k-vs-cte-map")


if __name__ == "__main__":
    debye_einstein_heat_capacity()
    anharmonic_potential()
    conductivity_vs_temperature()
    thermal_shock_ranking()
    T1, T3, T4 = tbc_temperature_profile()
    print(f"  TBC interfaces: {T1:.0f}, {T3:.0f}, {T4:.0f} °C")
    k_vs_cte_map()
