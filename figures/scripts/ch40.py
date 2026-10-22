"""Figures for Chapter 40 — Materials for Energy.

Run from the repository root:  python figures/scripts/ch40.py
"""
import numpy as np
from matplotlib.patches import Ellipse, Rectangle, Circle, FancyBboxPatch
from matplotlib.lines import Line2D
from scipy.integrate import quad

from figstyle import new_fig, save, COLORS, INK, plt

C_BLUE, C_VERM, C_GREEN, C_PINK, C_ORANGE, C_SKY, C_YELLOW, C_BLACK = COLORS


# ---------------------------------------------------------------------------
# 32.1 Absorption coefficients of PV absorbers
# ---------------------------------------------------------------------------
def _inv(k):
    """Reciprocal mapping k/x that is safe at x = 0 (for secondary axes)."""
    def f(x):
        x = np.asarray(x, float)
        with np.errstate(divide="ignore"):
            return k / np.where(x == 0, 1e-30, x)
    return f


def _loginterp(E, table):
    from scipy.interpolate import PchipInterpolator
    e, a = np.array(table).T
    y = 10 ** PchipInterpolator(e, np.log10(a), extrapolate=False)(E)
    return y


def pv_absorption():
    E = np.linspace(1.0, 3.0, 800)
    # c-Si: Green (2008) tabulation, converted from wavelength to photon energy
    si_nm = [(1150, 0.3), (1120, 1.0), (1100, 3.5), (1050, 16.4), (1000, 64), (950, 157),
             (900, 306), (850, 535), (800, 850), (750, 1300), (700, 1900), (650, 2810),
             (600, 4140), (550, 6390), (500, 11100), (450, 25500), (410, 70000)]
    si = sorted((1239.84 / l, a) for l, a in si_nm)
    gaas = [(1.36, 3), (1.40, 1e2), (1.415, 2e3), (1.425, 7e3), (1.45, 9e3), (1.5, 1.1e4),
            (1.6, 1.4e4), (1.8, 2.0e4), (2.0, 3.0e4), (2.2, 4.0e4), (2.5, 6.5e4),
            (2.8, 1.5e5), (3.0, 4e5)]
    cdte = [(1.38, 5), (1.42, 5e1), (1.45, 3e2), (1.48, 2e3), (1.50, 5e3), (1.55, 1e4),
            (1.6, 1.6e4), (1.8, 3e4), (2.0, 5e4), (2.3, 7e4), (2.6, 9e4), (3.0, 1.5e5)]
    cigs = [(1.0, 3), (1.05, 1e2), (1.10, 1e3), (1.15, 7e3), (1.2, 1.5e4), (1.3, 3e4),
            (1.5, 5e4), (2.0, 8e4), (2.5, 1.1e5), (3.0, 1.5e5)]
    pvk = [(1.42, 3), (1.47, 6e1), (1.50, 1e3), (1.53, 6e3), (1.55, 1e4), (1.6, 1.5e4),
           (1.8, 2.5e4), (2.07, 5e4), (2.4, 1e5), (2.6, 1.5e5), (3.0, 2.2e5)]

    fig, ax = new_fig(6.6, 4.4)
    # faint AM1.5G-like photon flux (blackbody 5778 K shape with main H2O/O2 dips)
    axs = ax.twinx()
    phi = E ** 2 / (np.exp(E / (8.617e-5 * 5778)) - 1)
    for c, w, d in [(1.10, 0.03, 0.85), (1.32, 0.025, 0.7), (1.51, 0.015, 0.25),
                    (1.63, 0.005, 0.5), (1.72, 0.01, 0.2)]:
        phi *= 1 - d * np.exp(-0.5 * ((E - c) / w) ** 2)
    phi *= np.where(E > 2.9, np.exp(-(E - 2.9) / 0.15), 1)  # ozone / Rayleigh cut-off
    axs.fill_between(E, 0, phi / phi.max(), color="#F3D9A4", alpha=0.45, lw=0, zorder=0)
    axs.set_ylim(0, 2.4)
    axs.set_yticks([])
    axs.spines["right"].set_visible(False)
    axs.text(2.72, 0.3, "AM1.5G photon flux\n(shape only)", fontsize=7.5, color="#B07A20",
             ha="center")
    ax.set_zorder(axs.get_zorder() + 1)
    ax.patch.set_visible(False)

    curves = [("c-Si (indirect, 1.12 eV)", si, C_BLACK),
              ("GaAs (1.42 eV)", gaas, C_BLUE),
              ("CdTe (1.5 eV)", cdte, C_VERM),
              ("CIGS (≈1.15 eV)", cigs, C_GREEN),
              ("FAPbI$_3$ perovskite (1.55 eV)", pvk, C_PINK)]
    for lab, tab, c in curves:
        ax.semilogy(E, _loginterp(E, tab), color=c, lw=1.9, label=lab)

    # worked-example points
    pts = [(1239.84 / 900, 306, "Si, 900 nm: 75 µm", C_BLACK, (1.17, 1.6e3), "left"),
           (1239.84 / 800, 1e4, "CdTe, 800 nm: 2.3 µm", C_VERM, (1.62, 5.2e3), "left"),
           (1239.84 / 600, 5e4, "perovskite, 600 nm: 0.46 µm", C_PINK, (1.6, 3.2e5), "left")]
    for x, a, t, c, (tx, ty), ha in pts:
        ax.plot(x, a, "o", ms=6, mfc="white", mec=c, mew=1.6, zorder=5)
        ax.annotate(t, (x, a), (tx, ty), fontsize=7.8, color=c, ha=ha,
                    arrowprops=dict(arrowstyle="-", color=c, lw=0.8))

    ax.set_xlim(1.0, 3.0)
    ax.set_ylim(1e1, 1e6)
    ax.set_xlabel("Photon energy (eV)")
    ax.set_ylabel(r"Absorption coefficient $\alpha$ (cm$^{-1}$)")
    ax.legend(loc="upper left", fontsize=8, ncol=1)

    top = ax.secondary_xaxis("top", functions=(_inv(1239.84), _inv(1239.84)))
    top.set_ticks([1100, 900, 800, 700, 600, 500, 450, 410])
    top.set_xlabel("Wavelength (nm)")
    right = ax.secondary_yaxis("right", functions=(_inv(2.303e4), _inv(2.303e4)))
    right.set_ylabel("Thickness for 90 % absorption, 2.303/α (µm)")
    right.set_yticks([1000, 100, 10, 1, 0.1])
    right.set_yticklabels(["1000", "100", "10", "1", "0.1"])
    save(fig, "40", "fig-40-1-pv-absorption-coefficients")


# ---------------------------------------------------------------------------
# 32.2 Electrode potential vs capacity map
# ---------------------------------------------------------------------------
def electrode_map():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.6, 4.4), sharey=True,
                                 gridspec_kw=dict(width_ratios=[2.4, 1.2], wspace=0.06))
    for a in (a1, a2):
        a.axhspan(1.0, 4.3, color="#E6F0E6", zorder=0)
        a.axhspan(0, 1.0, color="#F6E3D6", zorder=0)
        a.set_ylim(-0.2, 5)
    a1.set_xlim(0, 400)
    a2.set_xlim(400, 4000)
    a2.spines["left"].set_visible(False)
    a2.tick_params(left=False)
    a1.text(8, 2.75, "carbonate electrolyte\nstable (≈1.0–4.3 V)", fontsize=7.8,
            color="#2E6B2E", va="top")
    a1.text(8, 0.92, "SEI forms (electrolyte reduced)", fontsize=7.8, color="#A0522D", va="top")
    a2.text(500, 4.85, "electrolyte oxidized" + chr(10) + "above ≈4.3 V", fontsize=7.8,
            color="#666666", va="top")

    # name, x, y, dx(practical range half-width), dy, vol change, colour, label offset
    cath = C_VERM
    an = C_BLUE
    items = [
        (a1, "LCO", 162, 3.9, 23, 0.12, "2–3 %", cath, (-25, 0.75)),
        (a1, "NMC811", 200, 3.75, 10, 0.18, "≈5 %", cath, (20, 0.22)),
        (a1, "LFP", 160, 3.45, 6, 0.06, "≈6.5 %", cath, (-62, -0.25)),
        (a1, "LMO", 110, 4.0, 10, 0.12, "≈7 %", cath, (-85, 0.0)),
        (a1, "graphite", 350, 0.1, 10, 0.1, "≈10 %", an, (-60, 0.55)),
        (a1, "LTO", 165, 1.55, 5, 0.05, "≈0.2 %", an, (14, 0.12)),
    ]
    for ax, name, x, y, dx, dy, dv, c, (ox, oy) in items:
        ax.add_patch(Ellipse((x, y), 2 * dx + 8, 2 * dy + 0.08, fc=c, alpha=0.22, ec=c, lw=1))
        ax.plot(x, y, "o", color=c, ms=5)
        if name == "LCO":
            ax.plot([x, x], [y + dy + 0.04, y + oy - 0.2], color=c, lw=0.7)
        ax.text(x + ox, y + oy, f"{name}\nΔV {dv}", fontsize=7.8, color=c, va="center")
    # silicon: practical 1000-3000 in composites, theoretical 3578
    a2.add_patch(Ellipse((2000, 0.4), 2000, 0.3, fc=an, alpha=0.18, ec=an, lw=1))
    a2.plot(3578, 0.4, "o", color=an, ms=5)
    a2.text(700, 1.3, "Si (Li$_{15}$Si$_4$, 3578)\npractical 1000–3000\nΔV ≈280 %", fontsize=7.8, color=an)
    a2.plot(3861, 0.0, "s", color=an, ms=5)
    a2.text(3950, 0.62, "Li metal 3861\n(no host)", fontsize=7.8, color=an, ha="right")
    # cell voltage arrow NMC811 - graphite
    xa = 255
    a1.plot([200, xa + 8], [3.75, 3.75], ls=":", color=INK, lw=0.8)
    a1.plot([350, xa - 8], [0.1, 0.1], ls=":", color=INK, lw=0.8)
    a1.annotate("", (xa, 0.1), (xa, 3.75),
                arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=1.2, mutation_scale=10))
    a1.text(xa + 6, 2.3, "cell voltage\nNMC811 | graphite\n≈3.65 V", fontsize=7.8, va="center")

    a1.set_ylabel("Potential vs Li/Li$^+$ (V)")
    fig.text(0.5, 0.0, "Specific capacity (mAh/g)   [linear scale; axis compressed above 400]",
             ha="center", fontsize=10)
    # break marks
    d = 0.015
    kw = dict(color=INK, clip_on=False, lw=1)
    a1.plot((1 - d, 1 + d), (-d, d), transform=a1.transAxes, **kw)
    a2.plot((-d * 2.6, d * 2.6), (-d, d), transform=a2.transAxes, **kw)
    legend = [Line2D([], [], marker="o", ls="", color=cath, label="cathodes"),
              Line2D([], [], marker="o", ls="", color=an, label="anodes")]
    a2.legend(handles=legend, loc="center right", bbox_to_anchor=(1.0, 0.56), fontsize=8)
    a2.set_xticks([1000, 2500, 4000])
    save(fig, "40", "fig-40-2-electrode-potential-capacity-map")


# ---------------------------------------------------------------------------
# 32.3 Arrhenius plot of ionic conductors
# ---------------------------------------------------------------------------
def ionic_arrhenius():
    kB = 8.617e-5

    def arr(s_ref, T_ref_C, Ea, TC):
        T = TC + 273.15
        Tr = T_ref_C + 273.15
        return s_ref * (Tr / T) * np.exp(-Ea / kB * (1 / T - 1 / Tr))

    fig, ax = new_fig(6.6, 4.4)
    lines = [
        ("LiPF$_6$ in EC–DMC (liquid)", 1e-2, 25, 0.15, (-3, 60), C_BLACK, "--"),
        ("LGPS (sulfide)", 1.2e-2, 25, 0.25, (-3, 150), C_ORANGE, "-"),
        ("Li$_6$PS$_5$Cl (argyrodite)", 3e-3, 25, 0.30, (-3, 150), C_YELLOW, "-"),
        ("LLZO (garnet)", 5e-4, 25, 0.35, (-3, 300), C_GREEN, "-"),
        ("LATP (NASICON)", 3e-4, 25, 0.38, (-3, 300), C_SKY, "-"),
        ("Na-β″-alumina", 0.3, 300, 0.30, (25, 350), C_PINK, "-"),
        ("Nafion (humidified)", 0.1, 80, 0.12, (20, 100), C_BLUE, "-."),
        ("8YSZ", 0.1, 1000, 0.90, (500, 1000), C_VERM, "-"),
        ("GDC", 0.025, 600, 0.70, (400, 800), "#8B4513", "-"),
    ]
    for lab, s, Tr, Ea, (t0, t1), c, ls in lines:
        TC = np.linspace(t0, t1, 200)
        ax.plot(1000 / (TC + 273.15), np.log10(arr(s, Tr, Ea, TC)), color=c, ls=ls, label=lab)
    # PEO–LiTFSI, VTF form fitted to 1e-5 at 25 C and 1e-3 at 80 C
    T0, B = 200.0, 1278.6
    A = 1e-5 * np.sqrt(298.15) * np.exp(B / (298.15 - T0))
    TC = np.linspace(15, 100, 200)
    T = TC + 273.15
    ax.plot(1000 / T, np.log10(A / np.sqrt(T) * np.exp(-B / (T - T0))), color="#7F7F7F",
            ls=(0, (5, 1.5, 1, 1.5)), label="PEO–LiTFSI (polymer)")

    ax.axhline(-3, color=INK, ls=":", lw=1)
    ax.text(1.55, -2.93, "solid-electrolyte target 10$^{-3}$ S/cm", fontsize=7.8)
    # worked example points (YSZ)
    for TC_, s_ in [(1000, 0.1), (700, 0.0104)]:
        ax.plot(1000 / (TC_ + 273.15), np.log10(s_), "o", mfc="white", mec=C_VERM, mew=1.5)
    ax.annotate("8YSZ, 700 °C:\n0.010 S/cm", (1000 / 973.15, np.log10(0.0104)), (0.74, -3.3),
                fontsize=7.5, color=C_VERM, va="top",
                arrowprops=dict(arrowstyle="-", color=C_VERM, lw=0.7))
    ax.set_xlim(0.7, 3.7)
    ax.set_ylim(-7, 0)
    ax.set_xlabel("1000/T (K$^{-1}$)")
    ax.set_ylabel(r"log$_{10}$ $\sigma$ (S/cm)")
    top = ax.secondary_xaxis("top", functions=(lambda x: x, lambda x: x))
    tc = np.array([1000, 700, 500, 300, 100, 25])
    top.set_xticks(1000 / (tc + 273.15), labels=[str(t) for t in tc])
    top.set_xlabel("Temperature (°C)")
    ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5), fontsize=8)
    save(fig, "40", "fig-40-3-ionic-conductivity-arrhenius")


# ---------------------------------------------------------------------------
# 32.4 PEMFC and SOFC cross-sections
# ---------------------------------------------------------------------------
def _channels(ax, x0, w, y0, h, fc, n=4, top=True, gas="", gc=INK):
    ax.add_patch(Rectangle((x0, y0), w, h, fc=fc, ec=INK, lw=0.8))
    cw = w / (2 * n)
    for k in range(n):
        cx = x0 + cw * (2 * k + 0.5)
        cy = y0 if top else y0 + h * 0.45
        ax.add_patch(Rectangle((cx, cy), cw, h * 0.55, fc="white", ec=INK, lw=0.6))
        ax.plot(cx + cw / 2, cy + h * 0.27, marker="o", ms=3.2, mfc="white", mec=gc, mew=1)
        ax.plot(cx + cw / 2, cy + h * 0.27, marker=".", ms=2.5, color=gc)


def fuel_cell_sections():
    fig, ax = plt.subplots(figsize=(6.8, 5.0))
    ax.set_xlim(0, 14.0)
    ax.set_ylim(-0.3, 10.0)
    ax.set_aspect("equal")
    ax.axis("off")
    rng = np.random.default_rng(3)
    W = 2.0

    def stack(x0, layers):
        y = 9.0
        pos = {}
        for h, fc, lab in layers:
            y -= h
            if fc is not None:
                ax.add_patch(Rectangle((x0, y), W, h, fc=fc, ec=INK, lw=0.8))
            pos[lab] = (y, h)
        return pos

    def labels(x0, pos, texts):
        for k, t in texts.items():
            y, h = pos[k]
            ax.plot([x0 + W, x0 + W + 0.15], [y + h / 2] * 2, color=INK, lw=0.6)
            ax.text(x0 + W + 0.2, y + h / 2, t, fontsize=7, va="center")

    # ---- (a) PEMFC ----
    x0 = 1.0
    p = stack(x0, [(1.0, None, "plateA"), (0.9, "#4D4D4D", "gdlA"), (0.6, "#2B2B2B", "clA"),
                   (0.7, "#D8E8F5", "mem"), (0.6, "#2B2B2B", "clC"), (0.9, "#4D4D4D", "gdlC"),
                   (1.0, None, "plateC")])
    _channels(ax, x0, W, p["plateA"][0], 1.0, "#A8A8A8", n=3, top=False, gc=C_BLUE)
    _channels(ax, x0, W, p["plateC"][0], 1.0, "#A8A8A8", n=3, top=True, gc=C_VERM)
    for key in ("gdlA", "gdlC"):
        y, h = p[key]
        for _ in range(12):
            xa = x0 + rng.uniform(0.2, W - 0.2)
            ya = y + rng.uniform(0.15, h - 0.15)
            ang = rng.uniform(-0.4, 0.4)
            ax.plot([xa - 0.3, xa + 0.3], [ya - 0.3 * ang, ya + 0.3 * ang], color="#BBBBBB",
                    lw=0.7)
    ym, hm = p["mem"]
    for xx in np.linspace(x0 + 0.3, x0 + W - 0.3, 4):
        ax.annotate("", (xx, ym + 0.08), (xx, ym + hm - 0.08),
                    arrowprops=dict(arrowstyle="-|>", color=C_VERM, lw=1.1, mutation_scale=8))
    ax.text(x0 - 0.12, ym + hm / 2, "H$^+$", fontsize=8.5, color=C_VERM, ha="right", va="center")
    labels(x0, p, {
        "plateA": "bipolar plate: graphite or\ncoated steel; H$_2$ channels",
        "gdlA": "gas-diffusion layer,\ncarbon paper ≈200 µm",
        "clA": "anode catalyst layer\nPt/C + ionomer, 5–10 µm",
        "mem": "PFSA membrane 15–25 µm",
        "clC": "cathode catalyst layer\nPt/C + ionomer",
        "gdlC": "gas-diffusion layer ≈200 µm",
        "plateC": "bipolar plate; air (O$_2$) in,\nwater out",
    })
    ax.text(x0 - 0.12, p["plateA"][0] + 0.7, "H$_2$ in", color=C_BLUE, fontsize=8, ha="right",
            va="center")
    ax.text(x0 - 0.12, p["plateC"][0] + 0.3, "air in\nH$_2$O out", color=C_VERM, fontsize=7.5,
            ha="right", va="center")
    ax.text(3.4, 9.6, "(a) PEM fuel cell, 80 °C", fontsize=9.5, ha="center", fontweight="bold")
    # catalyst-layer zoom below the stack
    zx, zy, zr = 2.0, 1.25, 0.95
    ax.add_patch(Circle((zx, zy), zr, fc="white", ec=INK, lw=0.9, zorder=4))
    for (cx, cy) in [(-0.4, 0.3), (0.3, 0.38), (-0.05, -0.35), (0.5, -0.3), (-0.55, -0.35)]:
        ax.add_patch(Circle((zx + cx, zy + cy), 0.28, fc="#3A3A3A", ec="#7DB3D9", lw=2.0, zorder=5))
        for a in np.linspace(0, 2 * np.pi, 7, endpoint=False):
            ax.add_patch(Circle((zx + cx + 0.25 * np.cos(a + cx), zy + cy + 0.25 * np.sin(a + cx)),
                                0.045, fc="#E0C060", ec="none", zorder=6))
    ax.plot([zx, x0 + 0.5], [zy + zr, p["clC"][0] + 0.05], color=INK, lw=0.6, ls=":")
    ax.text(zx + zr + 0.25, zy, "catalyst-layer zoom:\n30 nm carbon (dark)\n3 nm Pt (gold)\n"
            "ionomer film (blue)", fontsize=6.8, va="center")

    # ---- (b) SOFC ----
    x1 = 8.1
    q = stack(x1, [(0.9, None, "icA"), (1.8, "#9DB98F", "sup"), (0.5, "#7FA36E", "afl"),
                   (0.55, "#F1E4B0", "el"), (0.45, "#E8C8A0", "gdc"), (0.8, "#4E5B8C", "cat"),
                   (0.9, None, "icC")])
    _channels(ax, x1, W, q["icA"][0], 0.9, "#B0B8C0", n=3, top=False, gc=C_BLUE)
    _channels(ax, x1, W, q["icC"][0], 0.9, "#B0B8C0", n=3, top=True, gc=C_VERM)
    for key, col, n in (("sup", "#EEF5EA", 55), ("cat", "#B9C1E0", 18)):
        y, h = q[key]
        ax.scatter(x1 + rng.uniform(0.08, W - 0.08, n), y + rng.uniform(0.08, h - 0.08, n), s=7,
                   color=col, zorder=3, lw=0)
    ye, he = q["el"]
    for xx in np.linspace(x1 + 0.3, x1 + W - 0.3, 4):
        ax.annotate("", (xx, ye + he - 0.05), (xx, ye + 0.05),
                    arrowprops=dict(arrowstyle="-|>", color=C_BLUE, lw=1.1, mutation_scale=8))
    ax.text(x1 - 0.12, ye + he / 2, "O$^{2-}$", fontsize=8.5, color=C_BLUE, ha="right",
            va="center")
    labels(x1, q, {
        "icA": "Fe–22Cr interconnect, α 11.5;\nfuel (H$_2$) channels",
        "sup": "porous Ni–YSZ support,\n300–500 µm, α ≈12.5",
        "afl": "Ni–YSZ functional layer ≈10 µm",
        "el": "dense 8YSZ electrolyte 10 µm, α 10.5",
        "gdc": "GDC barrier ≈2 µm",
        "cat": "porous LSCF cathode\n≈30 µm, α ≈15",
        "icC": "interconnect; air channels",
    })
    ax.text(x1 - 0.12, q["icA"][0] + 0.6, "H$_2$ in", color=C_BLUE, fontsize=8, ha="right",
            va="center")
    ax.text(x1 - 0.12, q["icC"][0] + 0.3, "air in", color=C_VERM, fontsize=7.5, ha="right",
            va="center")
    ax.text(10.5, 9.6, "(b) anode-supported SOFC, 700 °C", fontsize=9.5, ha="center",
            fontweight="bold")
    # TPB zoom
    tx, ty, tr = 9.1, 1.25, 0.95
    ax.add_patch(Circle((tx, ty), tr, fc="#F8F8F8", ec=INK, lw=0.9, zorder=4))
    ax.add_patch(Circle((tx - 0.38, ty + 0.2), 0.5, fc="#9AA5A0", ec=INK, lw=0.6, zorder=5))
    ax.add_patch(Circle((tx + 0.4, ty + 0.16), 0.48, fc="#F1E4B0", ec=INK, lw=0.6, zorder=5))
    ax.add_patch(Circle((tx + 0.02, ty - 0.52), 0.4, fc="#F1E4B0", ec=INK, lw=0.6, zorder=5))
    ax.plot(tx + 0.0, ty + 0.36, "*", color=C_VERM, ms=9, zorder=7)
    ax.text(tx - 0.42, ty + 0.12, "Ni", fontsize=7, ha="center", va="center", zorder=6)
    ax.text(tx + 0.45, ty + 0.1, "YSZ", fontsize=7, ha="center", va="center", zorder=6)
    ax.text(tx - 0.05, ty + 0.75, "pore", fontsize=6.5, ha="center", va="center", zorder=6)
    ax.plot([tx, x1 + 0.5], [ty + tr, q["afl"][0] + 0.05], color=INK, lw=0.6, ls=":")
    ax.text(tx + tr + 0.25, ty, "functional-layer zoom:\ntriple-phase boundary ★\n"
            "where Ni, YSZ and pore\nmeet", fontsize=6.8, va="center")
    ax.text(7.0, -0.2, "Not to scale.  α = thermal expansion coefficient (ppm/K).", fontsize=7.5,
            style="italic", ha="center")
    save(fig, "40", "fig-40-4-pemfc-sofc-cross-sections")


# ---------------------------------------------------------------------------
# 32.5 Thermoelectric trade-off (single parabolic band, acoustic-phonon scattering)
# ---------------------------------------------------------------------------
def _F(j, eta):
    f = lambda x: x ** j / (1 + np.exp(np.clip(x - eta, -700, 700)))
    up = max(eta, 0) + 60
    return quad(f, 0, up, limit=200)[0]


def thermoelectric():
    kB, e, h, me = 1.380649e-23, 1.602e-19, 6.626e-34, 9.109e-31
    T, mstar, mu0, kL = 300.0, 1.5, 135e-4, 0.55  # mu0 in m^2/Vs, kL in W/mK
    Nc = 2 * (2 * np.pi * mstar * me * kB * T / h ** 2) ** 1.5  # m^-3
    etas = np.linspace(-8, 90, 500)
    n, S, sig, L = [], [], [], []
    for eta in etas:
        F0, F1, F2, Fh = _F(0, eta), _F(1, eta), _F(2, eta), _F(0.5, eta)
        nn = Nc * (2 / np.sqrt(np.pi)) * Fh
        mu = mu0 * F0 / ((2 / np.sqrt(np.pi)) * Fh)
        n.append(nn)
        S.append(kB / e * (2 * F1 / F0 - eta))
        sig.append(nn * e * mu)
        L.append((kB / e) ** 2 * (3 * F0 * F2 - 4 * F1 ** 2) / F0 ** 2)
    n, S, sig, L = map(np.array, (n, S, sig, L))
    ncm = n * 1e-6
    ke = L * sig * T
    PF = S ** 2 * sig
    ZT = PF * T / (ke + kL)
    m = (ncm >= 1e17) & (ncm <= 1e22)

    fig = plt.figure(figsize=(6.8, 5.0))
    gs = fig.add_gridspec(2, 2, width_ratios=[2.25, 1], height_ratios=[1, 1], hspace=0.12,
                          wspace=0.55)
    a1 = fig.add_subplot(gs[0, 0])
    a2 = fig.add_subplot(gs[1, 0], sharex=a1)
    a1.loglog(ncm[m], S[m] * 1e6, color=C_BLUE, label="Seebeck S")
    a1.set_ylabel("S (µV/K)", color=C_BLUE)
    a1.set_ylim(2, 2000)
    a1b = a1.twinx()
    a1b.spines["right"].set_visible(True)
    a1b.loglog(ncm[m], sig[m], color=C_VERM)
    a1b.set_ylabel(r"$\sigma$ (S/m)", color=C_VERM)
    a1b.set_ylim(1e1, 1e8)
    a1.text(2e17, 700, "S", color=C_BLUE, fontsize=10)
    a1.text(3e21, 15, r"$\sigma$", color=C_VERM, fontsize=11)
    for x0, x1, lab in [(1e17, 1e18, "insulators"), (1e18, 1e21, "semiconductors"),
                        (1e21, 1e22, "metals")]:
        a1.text(np.sqrt(x0 * x1), 1300, lab, ha="center", fontsize=8, color="#555555")
    for a in (a1, a2):
        a.axvline(1e18, color="#BBBBBB", lw=0.8, ls=":")
        a.axvline(1e21, color="#BBBBBB", lw=0.8, ls=":")
        a.axvspan(1e19, 1e20, color="#F3E7C4", alpha=0.6, lw=0)
    plt.setp(a1.get_xticklabels(), visible=False)

    a2.loglog(ncm[m], ke[m], color=C_GREEN, label=r"$\kappa_e$ (W m$^{-1}$K$^{-1}$)")
    a2.axhline(kL, color=C_GREEN, ls="--", lw=1.3, label=r"$\kappa_L$ (constant)")
    a2.loglog(ncm[m], PF[m] * 1e3, color=C_ORANGE,
              label=r"$S^2\sigma$ (mW m$^{-1}$K$^{-2}$)")
    a2.set_ylim(1e-3, 30)
    a2.set_xlim(1e17, 1e22)
    a2.set_ylabel(r"$\kappa$ (W m$^{-1}$K$^{-1}$)," + "\n" + r"$S^2\sigma$ (mW m$^{-1}$K$^{-2}$)",
                  fontsize=8.5)
    a2.set_xlabel(r"Carrier concentration $n$ (cm$^{-3}$)")
    a2b = a2.twinx()
    a2b.spines["right"].set_visible(True)
    a2b.semilogx(ncm[m], ZT[m], color=C_BLACK, lw=2.2, label="ZT")
    a2b.set_ylim(0, 1.6)
    a2b.set_ylabel("ZT (linear)")
    i = np.argmax(np.where(m, ZT, 0))
    a2b.annotate(f"ZT$_{{max}}$ ≈ {ZT[i]:.1f}\nat n ≈ 10$^{{{np.log10(ncm[i]):.1f}}}$ cm$^{{-3}}$",
                 (ncm[i], ZT[i]), (2.5e17, 1.25), fontsize=8,
                 arrowprops=dict(arrowstyle="-", lw=0.7))
    a2.text(2.5e21, 4, r"$\kappa_e$", color=C_GREEN, fontsize=10)
    a2.text(1.3e17, 0.33, r"$\kappa_L$ (constant)", color=C_GREEN, fontsize=8)
    a2.text(1.5e21, 0.9, r"$S^2\sigma$", color=C_ORANGE, fontsize=10)
    a2b.text(10 ** 20.05, 0.62, "ZT", fontsize=10, fontweight="bold")

    # module inset
    a3 = fig.add_subplot(gs[:, 1])
    a3.set_xlim(0, 4)
    a3.set_ylim(-0.8, 8.0)
    a3.set_aspect("equal")
    a3.axis("off")
    a3.add_patch(Rectangle((0.2, 5.6), 3.6, 0.5, fc="#F4B183", ec=INK, lw=0.8))
    a3.text(2, 5.85, "hot plate  T$_h$", ha="center", va="center", fontsize=7.5)
    a3.add_patch(Rectangle((0.2, 1.0), 3.6, 0.5, fc="#9DC3E6", ec=INK, lw=0.8))
    a3.text(2, 1.25, "cold plate  T$_c$", ha="center", va="center", fontsize=7.5)
    a3.add_patch(Rectangle((0.5, 5.35), 3.0, 0.25, fc="#C0C0C0", ec=INK, lw=0.6))
    a3.add_patch(Rectangle((0.5, 1.5), 1.1, 0.25, fc="#C0C0C0", ec=INK, lw=0.6))
    a3.add_patch(Rectangle((2.4, 1.5), 1.1, 0.25, fc="#C0C0C0", ec=INK, lw=0.6))
    a3.add_patch(Rectangle((0.7, 1.75), 0.75, 3.6, fc="#F8CBAD", ec=INK, lw=0.8))
    a3.add_patch(Rectangle((2.55, 1.75), 0.75, 3.6, fc="#BDD7EE", ec=INK, lw=0.8))
    a3.text(1.075, 3.55, "p", ha="center", va="center", fontsize=11, fontweight="bold")
    a3.text(2.925, 3.55, "n", ha="center", va="center", fontsize=11, fontweight="bold")
    # current loop: up n, across top, down p, out through load
    I = dict(arrowstyle="-|>", color=C_VERM, lw=1.3, mutation_scale=9)
    a3.annotate("", (2.925, 4.6), (2.925, 2.5), arrowprops=I)
    a3.annotate("", (1.075, 2.5), (1.075, 4.6), arrowprops=I)
    a3.plot([1.05, 1.05, 1.6], [1.5, 0.3, 0.3], color=C_VERM, lw=1.1)
    a3.plot([2.4, 2.95, 2.95], [0.3, 0.3, 1.5], color=C_VERM, lw=1.1)
    a3.add_patch(Rectangle((1.6, 0.1), 0.8, 0.4, fc="white", ec=INK, lw=0.8))
    a3.text(2.0, 0.3, "load", ha="center", va="center", fontsize=7)
    a3.annotate("", (2.95, 1.0), (2.95, 0.35), arrowprops=I)
    a3.text(2.0, -0.25, "current I", color=C_VERM, ha="center", fontsize=7.5)
    # heat flow
    for xx in (0.35, 3.65):
        a3.annotate("", (xx, 1.8), (xx, 5.3),
                    arrowprops=dict(arrowstyle="-|>", color="#C55A11", lw=2.0, mutation_scale=12))
    a3.text(2.0, 6.55, "heat in", ha="center", fontsize=7.5, color="#C55A11")
    a3.annotate("", (2.0, 6.15), (2.0, 6.5),
                arrowprops=dict(arrowstyle="-|>", color="#C55A11", lw=1.5, mutation_scale=9))
    a3.text(2.0, 7.6, "Module: legs electrically\nin series, thermally in parallel",
            ha="center", va="center", fontsize=7.2)
    save(fig, "40", "fig-40-5-thermoelectric-tradeoff")


# ---------------------------------------------------------------------------
# 32.6 Material intensity vs world production
# ---------------------------------------------------------------------------
def material_intensity():
    rows = [
        ("Te — 100 GW/yr CdTe", 3300 / 600, "≈33 t Te/GW (2 µm CdTe, 19 %)"),
        ("Ir — 100 GW/yr PEM electrolysers", 40 / 7.5, "0.4 g Ir/kW"),
        ("Li — 4 TWh/yr Li-ion", 400 / 225, "0.1 kg Li/kWh"),
        ("Ir — same, tenfold lower loading", 4 / 7.5, "0.04 g Ir/kW"),
        ("Dy — 100 GW/yr wind (NdFeB)", 1000 / 2000, "≈10 kg Dy/MW"),
        ("Li — 1 TWh/yr Li-ion", 100 / 225, "0.1 kg Li/kWh"),
        ("Co — 1 TWh/yr, all NMC811", 83 / 225, "≈83 g Co/kWh"),
        ("Ag — 500 GW/yr c-Si PV", 5000 / 25000, "10 mg Ag/W"),
    ]
    rows = rows[::-1]
    fig, ax = new_fig(6.6, 4.0)
    y = np.arange(len(rows))
    vals = np.array([r[1] for r in rows])
    cols = [C_VERM if v > 1 else C_BLUE for v in vals]
    ax.barh(y, vals, left=0.01, color=cols, height=0.62, alpha=0.85)
    ax.set_xscale("log")
    ax.set_xlim(0.01, 10)
    ax.axvline(1, color="#C00000", lw=1.6)
    ax.text(1.07, -0.75, "1 = all current world production", color="#C00000", fontsize=7.8,
            va="center")
    ax.set_yticks(y)
    ax.set_yticklabels([r[0] for r in rows], fontsize=8.3)
    for yi, (lab, v, note) in zip(y, rows):
        ax.text(v / 1.07, yi, note, ha="right", va="center", fontsize=7.4, color="white")
        ax.text(v * 1.08, yi, f"×{v:.2g}", ha="left", va="center", fontsize=7.8)
    ax.set_xlabel("Fraction of current world primary production needed each year")
    ax.set_xticks([0.01, 0.1, 1, 10])
    ax.set_xticklabels(["0.01", "0.1", "1", "10"])
    fig.text(0.5, -0.1, "Order-of-magnitude illustration. Bar labels give the assumed material "
             "intensity.\nWorld production (mid-2020s): Li ≈225 kt, Co ≈225 kt, Te ≈600 t, "
             "Ir ≈7.5 t, Ag ≈25 kt, Dy ≈2 kt per year.", fontsize=7, style="italic",
             color="#555555", ha="center")
    ax.set_ylim(-1.1, len(rows) - 0.5)
    save(fig, "40", "fig-40-6-material-intensity-supply")


if __name__ == "__main__":
    pv_absorption()
    electrode_map()
    ionic_arrhenius()
    fuel_cell_sections()
    thermoelectric()
    material_intensity()
