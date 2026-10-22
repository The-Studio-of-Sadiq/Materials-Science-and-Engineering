"""Figures for Chapter 41 — Materials for Extreme Environments.

Run from the repository root:  python figures/scripts/ch41.py
"""
import numpy as np
from matplotlib.patches import Rectangle, Circle, Polygon, FancyArrowPatch

from figstyle import new_fig, save, COLORS, INK, plt

C_BLUE, C_VERM, C_GREEN, C_PINK, C_ORANGE, C_SKY, C_YELLOW, C_BLACK = COLORS
SIGMA_SB = 5.670e-8


# ---------------------------------------------------------------------------
# 33.1 Larson-Miller master curves
# ---------------------------------------------------------------------------
def larson_miller():
    fig, ax = new_fig(6.6, 4.4)
    # name, (P1, s1), (P2, s2), colour, label position
    alloys = [
        ("Ti-6242", (16000, 500), (19500, 150), C_GREEN, (19650, 150), "left"),
        ("9Cr-1Mo (Gr. 91)", (18000, 300), (23000, 50), C_BLACK, None, "left"),
        ("316 stainless", (18000, 250), (24000, 40), C_SKY, (24150, 40), "left"),
        ("IN718 (wrought)", (20000, 700), (25000, 150), C_BLUE, (25150, 150), "left"),
        ("IN738 (cast, polycrystal)", (22000, 500), (27000, 100), C_PINK, (26900, 82), "left"),
        ("CMSX-4 (single crystal)", (24000, 600), (29500, 100), C_VERM, (24100, 730), "left"),
    ]
    for name, (p1, s1), (p2, s2), c, txy, ha in alloys:
        tx, ty = txy if txy else (None, None)
        P = np.linspace(p1, p2, 200)
        u = (P - p1) / (p2 - p1)
        logs = np.log10(s1) + u * (np.log10(s2) - np.log10(s1)) + 0.08 * 4 * u * (1 - u)
        ax.semilogy(P, 10 ** logs, color=c, lw=2)
        if tx is None:
            k = 175
            ax.annotate(name, (P[k], 10 ** logs[k]), (19000, 62), color=c, fontsize=8,
                        ha="center", arrowprops=dict(arrowstyle="-", lw=0.7, color=c))
        else:
            ax.text(tx, ty, name, color=c, fontsize=8, ha=ha, va="center")
    # worked example: LMP 29 279
    P = 29279
    u = (P - 24000) / 5500
    s = 10 ** (np.log10(600) + u * (np.log10(100) - np.log10(600)) + 0.32 * u * (1 - u))
    ax.axvline(P, color=C_VERM, ls=":", lw=1)
    ax.plot(P, s, "o", mfc="white", mec=C_VERM, mew=1.6, ms=7, zorder=5)
    ax.annotate("worked example:\n1000 h at 1273 K\nLMP = 29 279", (P, s), (29700, 420),
                fontsize=7.8, ha="left", arrowprops=dict(arrowstyle="-", lw=0.7, color=C_VERM))
    ax.annotate("", (28279, 26), (29279, 26),
                arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=1, mutation_scale=8))
    ax.text(28779, 28, "ΔLMP 1000\n≈ 42 °C at 10$^4$ h", fontsize=7.2, ha="center", va="bottom")
    ax.set_xlim(16000, 32000)
    ax.set_ylim(20, 1000)
    ax.set_xlabel(r"Larson–Miller parameter  $T\,(20+\log_{10} t_r)$   ($T$ in K, $t_r$ in h)")
    ax.set_ylabel("Stress (MPa)")
    ax.set_yticks([20, 50, 100, 200, 500, 1000])
    ax.set_yticklabels(["20", "50", "100", "200", "500", "1000"])
    ax.yaxis.set_minor_formatter(plt.NullFormatter())
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:,.0f}".replace(",", " ")))
    top = ax.secondary_xaxis("top", functions=(lambda P: P / 24 - 273.15,
                                               lambda T: (T + 273.15) * 24))
    top.set_xticks([400, 500, 600, 700, 800, 900, 1000])
    top.set_xlabel("Temperature for a 10 000 h rupture life (°C)")
    save(fig, "41", "fig-41-1-larson-miller-alloys")


# ---------------------------------------------------------------------------
# 33.2 Thermal barrier coating system with temperature profile
# ---------------------------------------------------------------------------
def tbc_system():
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.8, 5.0), sharex=True,
                                 gridspec_kw=dict(height_ratios=[1, 1.35], hspace=0.08))
    # drawing positions (not to scale)
    xg0, xt0, xt1, xo1, xb1, xs1, xc1 = 0, 2.2, 5.6, 5.85, 6.9, 9.3, 11.0
    # --- temperature profile ---
    xs = [xg0, 1.4, xt0, xt1, xo1, xb1, xs1, 10.1, xc1]
    Ts = [1500, 1500, 1300, 1000, 995, 985, 900, 600, 600]
    a1.plot(xs, Ts, color=C_VERM, lw=2.2)
    for x0, x1, c in [(xg0, xt0, "#FCE4D6"), (xt0, xt1, "#FFF2CC"), (xt1, xo1, "#D9D9D9"),
                      (xo1, xb1, "#E2EFDA"), (xb1, xs1, "#DDEBF7"), (xs1, xc1, "#EAF4FB")]:
        a1.axvspan(x0, x1, color=c, lw=0, zorder=0)
    for x, T, t, dx, dy, ha, va in [(xt0, 1300, "≈1300 °C\nsurface", 0.12, 35, "left", "bottom"),
                                    (xt1, 1000, "≈1000 °C", -0.12, -40, "right", "top"),
                                    (xs1, 900, "≈900 °C\ninner wall", 0.12, 35, "left", "bottom")]:
        a1.plot(x, T, "o", color=C_VERM, ms=5)
        a1.text(x + dx, T + dy, t, fontsize=7.8, ha=ha, va=va)
    a1.text(0.15, 1520, "hot gas 1500 °C", fontsize=8, va="bottom")
    a1.text(10.9, 625, "cooling air\n600 °C", fontsize=8, ha="right", va="bottom")
    a1.plot([xt0, xt1], [1000, 1000], ls=":", color=INK, lw=0.8)
    a1.annotate("", (xt0 + 0.25, 1000), (xt0 + 0.25, 1300),
                arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=1, mutation_scale=8))
    a1.text(xt0 + 0.12, 780, "ΔT ≈ 300 K across topcoat\n(q = 1 MW/m², k ≈ 1 W/m K)",
            fontsize=7.2, va="center")
    a1.text(xc1 - 0.05, 1640, "layer widths not to scale", fontsize=7, style="italic",
            ha="right", va="top", color="#555555")
    a1.set_ylim(500, 1650)
    a1.set_ylabel("Temperature (°C)")
    a1.spines["bottom"].set_visible(False)
    a1.tick_params(bottom=False)

    # --- cross-section ---
    a2.set_ylim(0, 5)
    a2.set_xlim(xg0, xc1)
    a2.axis("off")
    rng = np.random.default_rng(7)
    a2.add_patch(Rectangle((xt0, 0.3), xt1 - xt0, 4.4, fc="#FFF2CC", ec=INK, lw=0.8))
    # columnar EB-PVD texture: column boundaries run normal to the surface
    xx = np.linspace(xt0, xt1, 80)
    for yy in np.arange(0.55, 4.6, 0.3):
        a2.plot(xx, yy + 0.03 * np.sin(xx * 3 + yy * 5), color="#C9A227", lw=0.7)
    a2.scatter(rng.uniform(xt0 + 0.1, xt1 - 0.1, 50), rng.uniform(0.4, 4.6, 50), s=3,
               color="#B8A05A", lw=0)
    # TGO (wavy, rumpled)
    yv = np.linspace(0.3, 4.7, 200)
    xw = xt1 + 0.05 * np.sin(yv * 9)
    a2.fill_betweenx(yv, xw, xw + 0.25, color="#8C8C8C", ec=INK, lw=0.5)
    a2.add_patch(Rectangle((xo1 + 0.05, 0.3), xb1 - xo1 - 0.05, 4.4, fc="#E2EFDA", ec=INK,
                           lw=0.8))
    a2.add_patch(Rectangle((xb1, 0.3), xs1 - xb1, 4.4, fc="#BDD7EE", ec=INK, lw=0.8))
    # film-cooling hole through wall and coating (inclined)
    hole = Polygon([[xs1, 1.0], [xs1, 1.45], [xt0, 3.0], [xt0, 2.55]], closed=True,
                   fc="white", ec=INK, lw=0.7)
    a2.add_patch(hole)
    a2.annotate("", (1.4, 2.95), (10.6, 0.94),
                arrowprops=dict(arrowstyle="-|>", color=C_SKY, lw=1.3, mutation_scale=10,
                                linestyle="--"))
    # CMAS at the hot surface
    a2.add_patch(Rectangle((xt0 - 0.12, 3.6), 0.12, 0.9, fc="#C55A11", ec="none"))
    for yy in (3.75, 4.05, 4.35):
        a2.plot([xt0, xt0 + 0.7], [yy, yy - 0.05], color="#C55A11", lw=1.4)
    # layer names
    a2.text((xg0 + xt0) / 2, 1.6, "hot gas", ha="center", va="center", fontsize=7.8)
    a2.text((xs1 + xc1) / 2, 2.2, "cooling\nair", ha="center", va="center", fontsize=7.8)
    a2.text((xt0 + xt1) / 2, 0.02, "7YSZ topcoat ≈300 µm\n(EB-PVD columns, porosity)",
            ha="center", va="top", fontsize=7.6)
    a2.text((xb1 + xs1) / 2, 0.02, "single-crystal\nsuperalloy wall, 1–2 mm", ha="center",
            va="top", fontsize=7.6)
    a2.text((xo1 + xb1) / 2, -0.75, "bond coat\nMCrAlY / PtAl\n50–100 µm", ha="center",
            va="top", fontsize=7.2)
    # callouts
    a2.annotate("CMAS melt\ninfiltrates\nthe columns", (xt0 - 0.12, 4.05), (0.1, 4.05),
                fontsize=7.2, va="center", arrowprops=dict(arrowstyle="-", lw=0.7))
    a2.annotate("TGO α-Al$_2$O$_3$\n1–10 µm: thickens,\nrumples → spallation",
                (xt1 + 0.15, 4.4), (xs1 + 0.08, 4.75), fontsize=6.8, va="top", ha="left",
                arrowprops=dict(arrowstyle="-", lw=0.7))
    a2.annotate("film-cooling\nhole", (xb1 + 1.6, 1.52), (xs1 + 0.08, 3.25), fontsize=6.8,
                va="top", arrowprops=dict(arrowstyle="-", lw=0.7))
    save(fig, "41", "fig-41-2-tbc-system-temperature-profile")


# ---------------------------------------------------------------------------
# 33.3 Displacement cascade
# ---------------------------------------------------------------------------
def displacement_cascade():
    N = 32
    a = 0.25  # nm, projected spacing (schematic)
    rng = np.random.default_rng(11)
    gx, gy = np.meshgrid(np.arange(N), np.arange(N))
    gx = gx.ravel() * a
    gy = gy.ravel() * a
    c = np.array([(N - 1) * a / 2 + 0.3, (N - 1) * a / 2])
    r = np.hypot(gx - c[0], gy - c[1])

    fig, axs = plt.subplots(1, 3, figsize=(6.8, 3.3))
    for ax in axs:
        ax.set_aspect("equal")
        ax.set_xlim(-0.3, N * a)
        ax.set_ylim(-0.6, N * a)
        ax.axis("off")
    ms = 2.6
    # (a) t = 0
    ax = axs[0]
    ax.plot(gx, gy, "o", ms=ms, color="#7F7F7F", mew=0)
    pka = np.array([c[0] - 2.2, c[1] + 0.4])
    ax.annotate("", pka, (pka[0] - 2.3, pka[1] + 2.6),
                arrowprops=dict(arrowstyle="-|>", color=C_BLUE, lw=1.5, ls="--",
                                mutation_scale=10))
    ax.text(pka[0] - 2.3, pka[1] + 2.75, "1 MeV n", color=C_BLUE, fontsize=8, ha="center")
    ax.plot(*pka, "o", ms=6, color=C_VERM, zorder=5)
    ax.annotate("", (pka[0] + 1.9, pka[1] - 0.5), pka,
                arrowprops=dict(arrowstyle="-|>", color=C_VERM, lw=1.8, mutation_scale=11))
    ax.text(pka[0] + 0.3, pka[1] - 1.25, "PKA, ≈35 keV", color=C_VERM, fontsize=8,
            bbox=dict(fc="white", ec="none", pad=0.8))
    ax.set_title("(a) t = 0: knock-on", fontsize=9)

    # (b) t ~ 0.5 ps: thermal spike
    ax = axs[1]
    core = r < 2.5
    jit = np.where(core, 0.09, 0.0)
    ax.add_patch(Circle(c, 2.5, fc="#FCE4D6", ec=C_VERM, lw=0.8, ls="--", zorder=0))
    ax.plot(gx + rng.normal(0, 1, gx.size) * jit, gy + rng.normal(0, 1, gy.size) * jit, "o",
            ms=ms, color="#7F7F7F", mew=0)

    def branch(p, ang, L, depth):
        if depth == 0 or L < 0.25:
            return
        q = p + L * np.array([np.cos(ang), np.sin(ang)])
        ax.plot([p[0], q[0]], [p[1], q[1]], color=C_VERM, lw=1.3 * (0.6 + 0.2 * depth))
        ax.plot(*q, "o", ms=3.2, color=C_VERM)
        for d in (-1, 1):
            branch(q, ang + d * rng.uniform(0.4, 1.0), L * rng.uniform(0.5, 0.75), depth - 1)

    branch(pka, np.arctan2(-0.5, 1.9), 1.3, 5)
    ax.text(c[0], -0.45, "≈250 displacements (NRT);\nmolten-like core ≈5 nm",
            fontsize=7.5, ha="center", va="top")
    ax.set_title("(b) t ≈ 0.5 ps: thermal spike", fontsize=9)

    # (c) t ~ 10 ps: surviving defects
    ax = axs[2]
    order = np.argsort(r + rng.uniform(0, 1.2, r.size))
    vac = order[:80]
    keep = np.ones(gx.size, bool)
    keep[vac] = False
    ax.plot(gx[keep], gy[keep], "o", ms=ms, color="#7F7F7F", mew=0)
    ax.plot(gx[vac], gy[vac], "s", ms=3.6, mfc="white", mec=C_BLUE, mew=0.9)
    # self-interstitials at periphery (off-lattice sites), some as small loops
    ang = rng.uniform(0, 2 * np.pi, 40)
    rad = rng.uniform(3.0, 3.8, 40)
    ix = c[0] + rad * np.cos(ang) + a / 2
    iy = c[1] + rad * np.sin(ang) + a / 2
    ax.plot(ix, iy, "o", ms=3.4, color=C_VERM, zorder=5)
    for t in (0.4, 1.9, 3.3, 4.8):
        p = c + 3.4 * np.array([np.cos(t), np.sin(t)])
        d = 0.35 * np.array([-np.sin(t), np.cos(t)])
        ax.plot([p[0] - d[0], p[0] + d[0]], [p[1] - d[1], p[1] + d[1]], color=C_VERM, lw=2.6,
                solid_capstyle="butt", zorder=6)
    ax.text(c[0], -0.45, "≈80 Frenkel pairs survive:\n□ vacancies at centre, ● SIAs and\n"
            "▬ small loops at the edge", fontsize=7.2, ha="center", va="top")
    ax.set_title("(c) t ≈ 10 ps: quenched", fontsize=9)
    # scale bar
    ax = axs[0]
    ax.plot([0.2, 0.2 + 2.0], [-0.35, -0.35], color=INK, lw=2.5, solid_capstyle="butt")
    ax.text(1.2, -0.5, "2 nm", ha="center", va="top", fontsize=8)
    # timeline
    tl = fig.add_axes([0.08, 0.05, 0.86, 0.06])
    tl.axis("off")
    tl.set_xlim(0, 1)
    tl.set_ylim(0, 1)
    tl.annotate("", (1, 0.6), (0, 0.6),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.1, mutation_scale=10))
    for x, t in [(0.12, "0"), (0.3, "0.1 ps\nballistic"), (0.5, "0.5 ps\nthermal spike"),
                 (0.85, "10 ps\nquench; defects then diffuse")]:
        tl.plot(x, 0.6, "|", color=INK, ms=8)
        tl.text(x, 0.35, t, ha="center", va="top", fontsize=7.2)
    save(fig, "41", "fig-41-3-displacement-cascade")


# ---------------------------------------------------------------------------
# 33.4 Void swelling vs dose
# ---------------------------------------------------------------------------
def _soft(x, w):
    return w * np.logaddexp(0, x / w)


def void_swelling():
    fig, ax = new_fig(6.4, 4.0)
    d = np.linspace(0, 200, 800)
    curves = [
        ("annealed 316 SS", 1.0 * _soft(d - 18, 4), C_VERM, "-"),
        ("20 % CW 316 / D9 (Ti-modified)", 1.0 * _soft(d - 52, 6), C_ORANGE, "-"),
        ("HT-9 / 9–12Cr F/M steel", 0.8 * (d / 200) ** 1.6, C_BLUE, "-"),
        ("ODS ferritic", 0.2 * (d / 200) ** 1.6, C_GREEN, "--"),
    ]
    for lab, s, c, ls in curves:
        ax.plot(d, np.minimum(s, 60), color=c, ls=ls, lw=2.2, label=lab)
    ax.set_xlim(0, 200)
    ax.set_ylim(0, 50)
    ax.set_xlabel("Dose (dpa)")
    ax.set_ylabel("Volumetric swelling (%)")
    ax.text(18, 46, "≈1 %/dpa\n(curve clipped)", color=C_VERM, fontsize=7.8, ha="left")
    ax.text(110, 47, "≈1 %/dpa", color=C_ORANGE, fontsize=7.8)
    ax.annotate("incubation\n10–20 dpa", (17, 0.5), (3, 9), fontsize=7.6, color=C_VERM,
                arrowprops=dict(arrowstyle="-", lw=0.7, color=C_VERM))
    ax.annotate("incubation\n40–60 dpa", (52, 0.5), (76, 4), fontsize=7.6, color=C_ORANGE,
                arrowprops=dict(arrowstyle="-", lw=0.7, color=C_ORANGE))
    ax.text(198, 2.0, "F/M: <1 % at 200 dpa;  ODS: lowest", ha="right", fontsize=7.8,
            color=C_BLUE)
    ax.legend(loc="center right", bbox_to_anchor=(1.0, 0.18), fontsize=7.8)
    ax.text(2, -7.8, "Fast-reactor irradiation, ≈400–550 °C; representative trends.",
            fontsize=7, style="italic", color="#555555")
    # inset: swelling vs temperature
    ins = ax.inset_axes([0.62, 0.48, 0.35, 0.36])
    T = np.linspace(300, 700, 300)
    ins.plot(T, 10 * np.exp(-0.5 * ((T - 480) / 55) ** 2), color=C_VERM, lw=1.8)
    ins.set_xlim(300, 700)
    ins.set_ylim(0, 12)
    ins.set_xlabel("Irradiation T (°C)", fontsize=7.5, labelpad=1)
    ins.set_ylabel("Swelling (%)", fontsize=7.5, labelpad=1)
    ins.tick_params(labelsize=7)
    ins.set_title("316 SS, fixed dose", fontsize=7.5, pad=2)
    ins.text(560, 8.5, "peak ≈450–500 °C\n(≈0.4 $T_m$)", fontsize=6.8, ha="left")
    ins.patch.set_facecolor("white")
    save(fig, "41", "fig-41-4-void-swelling-dose")


# ---------------------------------------------------------------------------
# 33.5 Cryogenic Charpy energies
# ---------------------------------------------------------------------------
def cryogenic_charpy():
    fig, ax = new_fig(6.6, 4.2)
    T = np.linspace(-273, 50, 600)
    cs = 10 + 140 * 0.5 * (1 + np.tanh((T + 10) / 8))
    ni9 = 100 + 50 * (T + 196) / 216
    ni9_lo = T < -196
    s304 = 200 - 15 * (1 - (T + 273) / 323)
    al = 45 + 5 * (1 - (T + 273) / 323)
    ax.plot(T, cs, color=C_BLACK, lw=2.2, label="plain C–Mn structural steel (BCC)")
    ax.plot(T[~ni9_lo], ni9[~ni9_lo], color=C_BLUE, lw=2.2, label="9 % Ni steel (Q&T)")
    ax.plot(T[ni9_lo], ni9[ni9_lo], color=C_BLUE, lw=1.6, ls="--")
    ax.plot(T, s304, color=C_GREEN, lw=2.2, label="304L austenitic stainless (FCC)")
    ax.plot(T, al, color=C_ORANGE, lw=2.2, ls="-.", label="5083-O aluminium (FCC)")
    ax.axhline(34, color="#C00000", ls="--", lw=1)
    ax.text(-120, 28, "34 J acceptance level", color="#C00000", fontsize=7.8, va="top")
    for Tv, lab in [(-162, "LNG −162 °C"), (-196, "LN$_2$ −196 °C"), (-253, "LH$_2$ −253 °C"),
                    (-269, "LHe −269 °C")]:
        ax.axvline(Tv, color="#888888", ls=":", lw=1)
        ax.text(Tv + 1.5, 246, lab, rotation=90, fontsize=7.5, va="top", ha="left",
                color="#555555")
    ax.text(-70, 76, "ductile–brittle\ntransition", fontsize=7.8, ha="center")
    ax.text(-238, 60, "no transition;\nlow but constant\nenergy, ductile", fontsize=7, color=C_ORANGE,
            ha="center")
    ax.set_xlim(-275, 50)
    ax.set_ylim(0, 250)
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Charpy V-notch absorbed energy (J)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), fontsize=7.8, ncol=2)
    save(fig, "41", "fig-41-5-cryogenic-charpy")


# ---------------------------------------------------------------------------
# 33.6 Radiative equilibrium temperature and TPS materials
# ---------------------------------------------------------------------------
def radiative_tps():
    fig, ax = new_fig(6.6, 4.4)
    q = np.logspace(-2, 1, 400)  # MW/m^2
    ax.axvspan(3, 10, color="#EADCF0", lw=0, zorder=0)
    ax.text(5.5, 1150, "ablators:\nno temperature limit\n(sacrificial)", ha="center", va="top",
            fontsize=7.6, color="#6A3D7A")
    bands = [(1300, "Ni superalloy / Inconel ≈1300 K", "#9DC3E6"),
             (1530, "silica tiles ≈1530 K", "#A9D18E"),
             (1920, "RCC, C/SiC ≈1920 K", "#7F7F7F"),
             (2300, "ZrB$_2$–SiC UHTC ≈2300 K", "#C55A11")]
    for Tb, lab, c in bands:
        ax.axhline(Tb, color=c, lw=2.2, alpha=0.9, zorder=1)
        ax.text(0.0105, Tb + 25, lab, fontsize=7.6, va="bottom", color=INK)
    ax.axhspan(2070, 2300, color="#F4B183", alpha=0.35, lw=0, zorder=0)
    ax.text(0.0105, 2160, "borosilicate glass evaporates above ≈2070 K", fontsize=6.8,
            va="center", color="#8C3A06", style="italic")
    for eps, ls, c in [(0.85, "-", C_VERM), (0.5, "--", C_BLUE)]:
        T = (q * 1e6 / (eps * SIGMA_SB)) ** 0.25
        ax.semilogx(q, T, ls=ls, color=c, lw=2.2, label=f"ε = {eps}", zorder=3)
    for qq, TT in [(1, 2130), (2, 2540)]:
        ax.plot(qq, TT, "o", mfc="white", mec=C_VERM, mew=1.6, ms=6.5, zorder=5)
        ax.text(qq * 1.1, TT - 50, f"{qq} MW/m², {TT} K", fontsize=7.4, ha="left",
                va="top", color=C_VERM)
    notes = [(0.25, 1505, "Shuttle acreage\n(tiles)", (0.06, 1700)),
             (0.65, 1910, "Shuttle nose cap\n(RCC)", (0.16, 2600)),
             (3.0, 2820, "sharp hypersonic\nleading edge", (0.75, 3150)),
             (5.0, 3376, "lunar-return\ncapsule", (5.5, 1650))]
    for qq, TT, t, xy in notes:
        ax.annotate(t, (qq, TT), xy, fontsize=7.4, ha="center",
                    arrowprops=dict(arrowstyle="-|>", lw=0.8, mutation_scale=8))
    ax.set_xlim(0.01, 10)
    ax.set_ylim(500, 3500)
    ax.set_xlabel("Heat flux q (MW/m²)")
    ax.set_ylabel("Radiative-equilibrium surface temperature (K)")
    ax.set_xticks([0.01, 0.1, 1, 10])
    ax.set_xticklabels(["0.01", "0.1", "1", "10"])
    ax.legend(loc="upper left", fontsize=8, title=r"$T=(q/\varepsilon\sigma)^{1/4}$",
              title_fontsize=8)
    save(fig, "41", "fig-41-6-radiative-equilibrium-tps")


if __name__ == "__main__":
    larson_miller()
    tbc_system()
    displacement_cascade()
    void_swelling()
    cryogenic_charpy()
    radiative_tps()
