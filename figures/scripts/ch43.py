"""Figures for Chapter 43 — Forms of Corrosion and Protection.

Run from the repository root:  python figures/scripts/ch43.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, Wedge, FancyArrowPatch, Ellipse
from scipy.special import erfc

METAL = "#B9BEC4"
WATER = "#DDEFFA"
ACID = "#F4A582"
FILM = "#1F5FBF"


# ---------------------------------------------------------------- Figure 43.1
def galvanic_series():
    rows = [  # (label, low, high)  V vs SCE
        ("Magnesium alloys", -1.63, -1.60),
        ("Zinc", -1.03, -0.98),
        ("Aluminium alloys", -1.00, -0.76),
        ("Carbon steel, cast iron", -0.72, -0.60),
        ("Austenitic stainless, active (crevice)", -0.58, -0.46),
        ("Copper, brass, bronze", -0.36, -0.24),
        ("90/10 copper–nickel", -0.28, -0.21),
        ("Nickel–aluminium bronze", -0.22, -0.15),
        ("Austenitic stainless, passive", -0.10, -0.05),
        ("Titanium, Ni–Cr–Mo alloys", -0.05, 0.06),
        ("Graphite, platinum", 0.20, 0.25),
    ]
    fig, ax = plt.subplots(figsize=(6.8, 4.4))
    n = len(rows)
    cmap = plt.get_cmap("coolwarm_r")
    for k, (lab, lo, hi) in enumerate(rows):
        y = n - 1 - k
        mid = (lo + hi) / 2
        col = cmap(0.08 + 0.84 * (mid + 1.7) / 2.0)
        hatch = "////" if "active" in lab else None
        ax.barh(y, hi - lo, left=lo, height=0.62, color="white" if hatch else col,
                edgecolor=INK if hatch else "none", hatch=hatch, lw=0.8)
        if hatch:
            ax.barh(y, hi - lo, left=lo, height=0.62, color="none", edgecolor=COLORS[1], hatch="////", lw=0)
    ax.set_yticks(range(n))
    ax.set_yticklabels([r[0] for r in rows][::-1], fontsize=8.5)
    ax.set_xlim(-1.7, 0.3)
    ax.set_ylim(-2.0, n - 0.4)
    ax.set_xlabel("Corrosion potential in flowing seawater (V vs SCE)")
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.axvline(0, color="#999999", lw=0.6, ls=":")
    # double-entry note for stainless
    ys_a = n - 1 - 4
    ys_p = n - 1 - 8
    ax.annotate("", xy=(-0.075, ys_p - 0.35), xytext=(-0.52, ys_a + 0.35),
                arrowprops=dict(arrowstyle="<|-|>", color=COLORS[3], lw=1.0, ls="--",
                                connectionstyle="arc3,rad=-0.25"))
    ax.text(0.04, ys_a + 0.6, "same alloy:\nfilm broken (crevice)\nvs film intact", fontsize=7.5,
            color=COLORS[3], ha="left", va="center")
    # bracket steel -> copper
    y_st = n - 1 - 3
    y_cu = n - 1 - 5
    yb = y_st + 0.75
    xs, xc = -0.66, -0.30
    ax.plot([xs, xs, xc, xc], [y_st + 0.38, yb, yb, y_cu + 0.38], color=INK, lw=1.0)
    ax.text(xc + 0.04, yb + 0.05, "ΔE ≈ 0.35 V: steel corrodes", fontsize=8.5,
            ha="left", va="center", color=INK)
    # active / noble arrow along the bottom
    ax.annotate("", xy=(-1.65, -1.35), xytext=(-0.75, -1.35),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.4))
    ax.annotate("", xy=(0.25, -1.35), xytext=(-0.65, -1.35),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.4))
    ax.text(-1.2, -1.15, "more active (anodic)", color=COLORS[1], fontsize=8.5, ha="center", va="bottom")
    ax.text(-0.2, -1.15, "more noble (cathodic)", color=COLORS[0], fontsize=8.5, ha="center", va="bottom")
    save(fig, "43", "fig-43-1-galvanic-series")


# ---------------------------------------------------------------- Figure 43.2
def pit_crevice():
    fig, axs = plt.subplots(1, 2, figsize=(6.8, 3.2))
    fig.subplots_adjust(left=0.01, right=0.99, top=0.95, bottom=0.08, wspace=0.05)
    for ax in axs:
        ax.set_xlim(0, 10); ax.set_ylim(0, 8); ax.set_aspect("equal"); ax.axis("off")
    S = 3.6  # metal surface level

    # ---------- (a) pit
    ax = axs[0]
    ax.add_patch(Rectangle((0, 0), 10, S, fc=METAL, ec="none"))
    ax.add_patch(Rectangle((0, S), 10, 7.4 - S, fc=WATER, ec="none"))
    th = np.linspace(np.pi, 2 * np.pi, 80)
    cx, rx, ry = 5.0, 2.0, 2.6
    ax.add_patch(Polygon(np.c_[cx + rx * np.cos(th), S + ry * np.sin(th)], closed=True,
                         fc=ACID, ec="#B2442A", lw=1.2))
    ax.plot([0, cx - rx], [S, S], color=FILM, lw=2.2)
    ax.plot([cx + rx, 10], [S, S], color=FILM, lw=2.2)
    for xx in np.arange(cx - rx - 0.1, cx + rx + 0.15, 0.33):
        ax.add_patch(Circle((xx, S + 0.12), 0.15, fc="#8C5A2B", ec="none"))
    ax.text(cx + rx + 0.25, S + 0.3, "porous cap", fontsize=7, ha="left", va="bottom", color="#6B3F16")
    ax.text(cx, S - 0.55, r"M $\rightarrow$ M$^{n+}$ + $n$e$^-$", fontsize=7, ha="center", va="center")
    ax.text(cx, S - 1.1, r"M$^{n+}$ + H$_2$O $\rightarrow$ MOH + H$^+$", fontsize=6.6, ha="center", va="center")
    ax.text(cx, S - 1.7, "pH 1–2, high Cl$^-$", fontsize=7.2, ha="center", va="center",
            color="#8B1A1A", weight="bold")
    for dx in (-0.7, 0.7):
        ax.annotate("", xy=(cx + dx * 0.5, S - 0.1), xytext=(cx + dx, S + 1.25),
                    arrowprops=dict(arrowstyle="-|>", color=COLORS[2], lw=1.1))
    ax.text(cx, S + 1.4, "Cl$^-$ migrates in", fontsize=7.5, ha="center", va="bottom", color=COLORS[2])
    for xx in (1.2, 9.0):
        ax.text(xx, 5.75, "O$_2$+2H$_2$O+4e$^-$\n$\\rightarrow$ 4OH$^-$", fontsize=6.6, ha="center",
                va="bottom", color=COLORS[0])
        ax.annotate("", xy=(xx, S + 0.05), xytext=(xx, 5.65), arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.0))
    ax.text(1.3, 4.3, "cathode", fontsize=6.8, ha="left", va="center", color=COLORS[0], alpha=0)
    ax.annotate("", xy=(1.4, S - 0.3), xytext=(cx - 1.5, S - 2.2),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.0, connectionstyle="arc3,rad=-0.3"))
    ax.annotate("", xy=(8.6, S - 0.3), xytext=(cx + 1.5, S - 2.2),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.0, connectionstyle="arc3,rad=0.3"))
    ax.text(1.75, 1.75, "e$^-$", fontsize=8.5, ha="center")
    ax.text(8.25, 1.75, "e$^-$", fontsize=8.5, ha="center")
    ax.text(0.2, 0.25, "stainless steel", fontsize=7.5)
    ax.text(0.2, 7.0, "aerated NaCl", fontsize=7.5)
    ax.text(5.0, 7.75, "(a) pit: small anode, large passive cathode", fontsize=8.3, ha="center", weight="bold")

    # ---------- (b) crevice
    ax = axs[1]
    ax.add_patch(Rectangle((0, 0), 10, S, fc=METAL, ec="none"))
    ax.add_patch(Rectangle((0, S), 10, 7.4 - S, fc=WATER, ec="none"))
    gap = 0.45
    ax.add_patch(Rectangle((3.4, S + gap), 6.6, 1.3, fc="#5E5E5E", ec="none"))
    ax.text(6.7, S + gap + 0.65, "gasket / washer", color="white", fontsize=7.5, ha="center", va="center")
    xs = np.linspace(3.4, 10, 60)
    for x0, x1 in zip(xs[:-1], xs[1:]):
        f = np.clip((x0 - 3.4) / 3.8, 0, 1)
        c = np.array([0xDD, 0xEF, 0xFA]) / 255 * (1 - f) + np.array([0xF4, 0xA5, 0x82]) / 255 * f
        ax.add_patch(Rectangle((x0, S), x1 - x0 + 0.01, gap, fc=c, ec="none"))
    ax.plot([0, 6.4], [S, S], color=FILM, lw=2.2)
    ax.plot([6.4, 10], [S, S], color="#B2442A", lw=1.2, ls=(0, (2, 1.5)))
    ax.add_patch(Polygon([[6.6, S], [7.2, S - 0.25], [8.4, S - 0.32], [9.4, S - 0.25], [10, S - 0.18], [10, S]],
                         fc=ACID, ec="#B2442A", lw=0.8))
    ax.annotate("", xy=(7.0, S + gap / 2), xytext=(3.6, S + gap / 2),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[2], lw=1.0, mutation_scale=8))
    for x, t in [(4.3, "1"), (5.8, "2"), (7.8, "3")]:
        ax.add_patch(Circle((x, S - 0.75), 0.3, fc="white", ec=INK, lw=0.8))
        ax.text(x, S - 0.75, t, fontsize=7.5, ha="center", va="center")
    ax.text(0.2, 2.0, "1  O$_2$ depleted inside\n2  Cl$^-$ migrates in\n3  pH falls, film breaks down",
            fontsize=7, va="top", linespacing=1.45)
    ax.text(9.8, 0.25, "stainless steel", fontsize=7.5, ha="right")
    ax.text(1.3, 5.75, "O$_2$+2H$_2$O+4e$^-$\n$\\rightarrow$ 4OH$^-$", fontsize=6.6, ha="center", va="bottom",
            color=COLORS[0])
    ax.annotate("", xy=(0.6, S + 0.05), xytext=(0.9, 5.65), arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.0))
    ax.text(0.2, 7.0, "cathode at the mouth", fontsize=7.5, color=COLORS[0])
    ax.annotate("", xy=(1.0, S - 0.35), xytext=(7.5, S - 1.35),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.0, connectionstyle="arc3,rad=-0.15"))
    ax.text(6.4, S - 1.9, "e$^-$", fontsize=8.5, ha="center", va="center")
    ax.text(3.2, S + 0.9, "gap 1–50 µm\n(drawn enlarged)", fontsize=6.6, ha="right", va="bottom")
    ax.plot([3.25, 3.45], [S + 0.95, S + 0.3], color=INK, lw=0.5)
    ax.annotate("", xy=(3.4, 5.95), xytext=(10, 5.95),
                arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=0.7, mutation_scale=6))
    ax.text(6.7, 6.05, "several mm deep", fontsize=7, ha="center", va="bottom")
    ax.text(5.0, 7.75, "(b) crevice: differential aeration", fontsize=8.3, ha="center", weight="bold")

    fig.text(0.5, 0.03, "blue line: passive film     orange-red: acidified chloride solution (anode)     "
             "green: Cl$^-$ migration", fontsize=7, ha="center", color=INK)
    save(fig, "43", "fig-43-2-pit-crevice-cells")


# ---------------------------------------------------------------- Figure 43.3
def sensitization():
    fig, ax = plt.subplots(figsize=(6.6, 3.9))
    x = np.linspace(-300, 300, 1201)
    w = 60.0
    cr = 18 - 9 * erfc(np.abs(x) / w)
    ax.fill_between(x, 0, 12, where=cr < 12, color=COLORS[1], alpha=0.18, lw=0)
    ax.plot(x, cr, color=COLORS[0], lw=2)
    ax.axhline(12, color=INK, ls="--", lw=1)
    ax.axhline(18, color="#999999", ls=":", lw=0.8)
    ax.text(-295, 12.3, "passivity threshold ≈ 12 % Cr", fontsize=8, va="bottom")
    ax.text(-295, 18.3, "bulk 18 % Cr", fontsize=8, va="bottom", color="#666666")
    ax.annotate("depleted zone\ncorrodes", xy=(0, 6), xytext=(-110, 4.0), fontsize=8, ha="right", va="center",
                color=COLORS[1], arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=0.9))
    ax.annotate("≈ 9 % at boundary", xy=(0, 9), xytext=(-45, 9.6), fontsize=8, ha="right",
                arrowprops=dict(arrowstyle="-", color=INK, lw=0.7))
    ax.axvline(0, color="#6B3F16", lw=1.0)
    ax.plot([0], [0.6], marker="D", ms=8, color="#6B3F16")
    ax.text(8, 1.9, "Cr$_{23}$C$_6$ on\ngrain boundary", fontsize=7.5, va="center", color="#6B3F16")
    ax.set_xlim(-300, 300)
    ax.set_ylim(0, 20)
    ax.set_xlabel("Distance from grain boundary (nm)")
    ax.set_ylabel("Chromium (wt %)")
    ax.text(-200, 15.8, "grain (passive)", fontsize=8, ha="center", color="#555555")
    ax.text(200, 15.8, "grain (passive)", fontsize=8, ha="center", color="#555555")

    # inset: TTS C-curves
    ins = fig.add_axes([0.71, 0.27, 0.25, 0.27])
    T = np.linspace(400, 900, 300)
    for tn, W, lab, c, xl in [(0.3, 134, "0.06 % C", COLORS[1], 0.45), (30, 120, "0.02 % C (L)", COLORS[0], 40)]:
        lt = np.log10(tn) + ((T - 700) / W) ** 2
        m = lt <= 3
        ins.plot(10 ** lt[m], T[m], color=c, lw=1.5)
        ins.text(xl, 700, lab, fontsize=6.3, ha="left", va="center", color=c)
    ins.set_xscale("log")
    ins.set_xlim(0.1, 1000)
    ins.set_ylim(400, 900)
    ins.set_xlabel("time (h)", fontsize=7, labelpad=1)
    ins.set_ylabel("T (°C)", fontsize=7, labelpad=1)
    ins.tick_params(labelsize=6.5)
    ins.set_title("sensitization C-curves", fontsize=7, pad=2)
    ins.spines["top"].set_visible(True); ins.spines["right"].set_visible(True)
    save(fig, "43", "fig-43-3-sensitization-profile")


# ---------------------------------------------------------------- Figure 43.4
def scc_velocity():
    fig, ax = new_fig(6.4, 3.9)
    KIc = 29.0

    def curve(K, Kth, vII):
        vI = 1e-12 * np.exp((K - Kth) / (0.35 if Kth < 10 else 0.15))          # steep stage I
        v = 1 / (1 / vI + 1 / vII)
        vIII = 1e-5 * np.exp((K - KIc) / 0.15)          # stage III
        return v + vIII

    for Kth, vII, lab, c in [(7, 1e-8, "7xxx-T651 (peak aged)", COLORS[1]),
                             (25, 1e-10, "7xxx-T73 (over-aged)", COLORS[0])]:
        K = np.linspace(Kth, KIc, 600)
        v = curve(K, Kth, vII)
        m = v <= 1e-5
        ax.semilogy(K[m], v[m], color=c, lw=2, label=lab)
        ax.axvline(Kth, color=c, ls="--", lw=1)
        ax.text(Kth - 0.25, 2.5e-12, f"$K_{{\\rm ISCC}}$ = {Kth}", color=c, fontsize=8, rotation=90, va="bottom", ha="right")
    ax.axvline(KIc, color=INK, ls=":", lw=1)
    ax.text(KIc + 0.3, 2.5e-12, "$K_{\\rm Ic}$ = 29", fontsize=8, rotation=90, va="bottom")
    ax.set_xlim(0, 35)
    ax.set_ylim(1e-12, 1e-5)
    ax.set_xlabel(r"Stress intensity $K$ (MPa$\sqrt{\rm m}$)")
    ax.set_ylabel("Crack velocity d$a$/d$t$ (m/s)")
    ax.text(8.6, 3e-10, "I", fontsize=11, weight="bold", color=COLORS[1])
    ax.text(17, 2e-8, "II  plateau (transport / reaction limited)", fontsize=8.5, color=COLORS[1], ha="center")
    ax.text(27.3, 1e-6, "III", fontsize=11, weight="bold", ha="center")
    ax.text(29.5, 1.0e-10, "T73 plateau\n≈ 10$^{-10}$ m/s", fontsize=7.5, color=COLORS[0], ha="left", va="center")
    ax.text(3.5, 1e-6, "no SCC growth\nbelow $K_{\\rm ISCC}$", fontsize=8, ha="center", color="#555555")
    ax.legend(loc="lower center", bbox_to_anchor=(0.47, 0.02), fontsize=8)
    ax.set_title("7xxx aluminium in 3.5 % NaCl", fontsize=9)
    save(fig, "43", "fig-43-4-scc-velocity-k")


# ---------------------------------------------------------------- Figure 43.5
def cathodic_protection():
    fig = plt.figure(figsize=(6.8, 4.2))
    ax = fig.add_axes([0.10, 0.12, 0.50, 0.82])
    E = np.linspace(-1.2, -0.4, 600)
    Ecorr, iL, ba = -0.65, 0.1, 0.06
    ia = iL * 10 ** ((E - Ecorr) / ba)
    i_o2 = 1 / (1 / (iL * 10 ** ((-0.45 - E) / 0.10) * 0.1) + 1 / iL)
    i_h2 = 0.1 * 10 ** ((-1.05 - E) / 0.12)
    ic = i_o2 + i_h2
    ax.axhspan(-1.2, -1.05, color=COLORS[1], alpha=0.12, lw=0)
    ax.semilogx(ia, E, color=COLORS[1], lw=2, label="Fe → Fe$^{2+}$ (anodic)")
    ax.semilogx(i_o2, E, color=COLORS[0], lw=1.3, ls="--")
    ax.semilogx(ic, E, color=COLORS[0], lw=2, label="O$_2$ + H$_2$ reduction (cathodic)")
    ax.set_xlim(1e-3, 10)
    ax.set_ylim(-1.2, -0.4)
    ax.set_xlabel("Current density |$i$| (A/m$^2$)")
    ax.set_ylabel("Potential (V vs Ag/AgCl)")
    ax.axhline(Ecorr, color="#888888", lw=0.7, ls=":")
    ax.axhline(-0.80, color=COLORS[2], lw=1.0, ls="--")
    ax.plot([iL], [Ecorr], "o", color=INK, ms=5)
    ax.text(1.3e-3, Ecorr + 0.012, "$E_{\\rm corr}$ ≈ −0.65 V", fontsize=8, va="bottom")
    ax.text(0.15, -0.80 + 0.01, "protection potential −0.80 V", fontsize=8, va="bottom", color=COLORS[2])
    ax.annotate("", xy=(0.012, -0.80), xytext=(0.012, Ecorr),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[2], lw=1.2))
    ax.text(0.0135, -0.755, "polarize\n−150 mV", fontsize=7, color=COLORS[2], ha="left", va="center")
    # applied current ~ iL at -0.80
    ax.plot([iL], [-0.80], "s", color=COLORS[2], ms=5)
    ax.annotate("applied current ≈ $i_{\\rm L}$\n(Fe dissolution ~300× slower)", xy=(iL, -0.80),
                xytext=(0.17, -0.92), fontsize=7.5, va="center",
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.8))
    ax.text(0.12, -0.50, "$i_{\\rm L}$ = 0.1 A/m$^2$\n(O$_2$ diffusion)", fontsize=7.5, color=COLORS[0])
    ax.text(0.3, -1.08, "H$_2$ evolution", fontsize=7.5, color=COLORS[0], ha="left")
    ax.text(1.2e-3, -1.18, "overprotection: H embrittlement,\ncoating disbondment", fontsize=7.5,
            color=COLORS[1], va="bottom")
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 0.92), fontsize=7.3)
    ax.set_title("(a) Evans diagram, steel in seawater", fontsize=9)

    # ---- (b) sacrificial anodes on monopile
    s1 = fig.add_axes([0.63, 0.53, 0.36, 0.43])
    s1.set_xlim(0, 10); s1.set_ylim(0, 10); s1.axis("off")
    s1.add_patch(Rectangle((0, 7.5), 10, 1.0, fc="white", ec="none"))
    s1.add_patch(Rectangle((0, 2.0), 10, 6.0, fc=WATER, ec="none"))
    s1.add_patch(Rectangle((0, 0), 10, 2.0, fc="#D9C79B", ec="none"))
    s1.plot([0, 10], [8, 8], color=COLORS[0], lw=0.8)
    s1.add_patch(Rectangle((4.0, 0), 2.0, 9.8, fc=METAL, ec=INK, lw=0.8))
    for yy in (4.0, 6.2):
        for side in (-1, 1):
            x0 = 5 + side * 1.0
            xa = 5 + side * 2.2
            s1.plot([x0, xa], [yy + 0.6, yy + 0.6], color=INK, lw=0.8)
            s1.plot([x0, xa], [yy - 0.6, yy - 0.6], color=INK, lw=0.8)
            s1.add_patch(Rectangle((xa - 0.3, yy - 0.9), 0.6, 1.8, fc="#E6E6E6", ec=INK, lw=0.7))
    s1.text(9.8, 2.35, "Al–Zn–In anodes", fontsize=7, ha="right")
    s1.text(1.6, 0.8, "seabed", fontsize=7, ha="center")
    s1.text(1.3, 7.0, "monopile", fontsize=7, ha="center")
    s1.text(5, 10.2, "(b) sacrificial anodes", fontsize=8.5, ha="center", weight="bold")

    # ---- (c) ICCP pipeline
    s2 = fig.add_axes([0.63, 0.04, 0.36, 0.43])
    s2.set_xlim(0, 10); s2.set_ylim(0, 10); s2.axis("off")
    s2.add_patch(Rectangle((0, 0), 10, 7.0, fc="#E8DCC0", ec="none"))
    s2.plot([0, 10], [7.0, 7.0], color="#6B5B3E", lw=1)
    s2.add_patch(Rectangle((0.5, 1.6), 9.0, 1.0, fc=METAL, ec=INK, lw=0.8))
    s2.text(5, 2.1, "buried coated pipeline", fontsize=7, ha="center", va="center")
    s2.add_patch(Rectangle((3.6, 7.4), 2.4, 1.6, fc="white", ec=INK, lw=0.8))
    s2.text(4.8, 8.2, "rectifier", fontsize=7, ha="center", va="center")
    # anode bed
    for xx in (8.0, 8.6, 9.2):
        s2.add_patch(Rectangle((xx - 0.15, 4.2), 0.3, 1.4, fc="#444444", ec="none"))
    s2.text(8.6, 5.9, "anode bed", fontsize=7, ha="center", va="bottom")
    s2.plot([6.0, 8.6, 8.6], [8.6, 8.6, 5.6], color=COLORS[1], lw=1)
    s2.text(6.3, 8.7, "+", color=COLORS[1], fontsize=9, va="bottom")
    s2.plot([3.6, 1.5, 1.5], [8.6, 8.6, 2.6], color=COLORS[0], lw=1)
    s2.text(3.2, 8.7, "−", color=COLORS[0], fontsize=10, va="bottom")
    for xx in (3.5, 5.5, 7.3):
        s2.annotate("", xy=(xx - 0.6, 2.75), xytext=(xx + 0.4, 4.3),
                    arrowprops=dict(arrowstyle="-|>", color=COLORS[2], lw=0.9))
    s2.text(4.5, 4.4, "current through soil", fontsize=6.8, color=COLORS[2], ha="center", va="bottom")
    s2.text(5, 10.2, "(c) impressed current", fontsize=8.5, ha="center", weight="bold")
    save(fig, "43", "fig-43-5-cathodic-protection")


# ---------------------------------------------------------------- Figure 43.6
def eis_randles():
    Rs, Rct, C = 10.0, 2000.0, 50e-6
    f = np.logspace(-2, 5, 600)
    w = 2 * np.pi * f
    Z = Rs + Rct / (1 + 1j * w * Rct * C)
    n = 0.85
    w0 = 1 / (Rct * C)
    Q = 1 / (Rct * w0 ** n)
    Zc = Rs + Rct / (1 + (1j * w) ** n * Rct * Q)
    fig = plt.figure(figsize=(6.8, 3.6))
    ax = fig.add_axes([0.08, 0.15, 0.44, 0.75])
    ax.plot(Z.real, -Z.imag, color=COLORS[0], lw=2, label="Randles, ideal $C_{\\rm dl}$")
    ax.plot(Zc.real, -Zc.imag, color=COLORS[1], lw=1.5, ls="--", label="CPE, $n$ = 0.85")
    ax.set_aspect("equal")
    ax.set_xlim(0, 2200); ax.set_ylim(0, 1100)
    ax.set_xlabel("Re $Z$ (Ω cm$^2$)")
    ax.set_ylabel("−Im $Z$ (Ω cm$^2$)")
    fa = 1 / (2 * np.pi * Rct * C)
    ax.plot([Rs + Rct / 2], [Rct / 2], "o", color=COLORS[0], ms=4)
    ax.text(Rs + Rct / 2, Rct / 2 + 40, "f = 1.6 Hz", fontsize=8, ha="center", va="bottom")
    ax.annotate("$R_s$ = 10", xy=(Rs, 0), xytext=(260, 150), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
    ax.annotate("$R_s+R_{ct}$ = 2010", xy=(2010, 0), xytext=(1600, 330), fontsize=7.5, ha="center",
                arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
    ax.annotate("", xy=(Rs, 30), xytext=(Rs + Rct, 30), arrowprops=dict(arrowstyle="<|-|>", lw=0.7, color=INK))
    ax.text(1010, 45, "$R_{ct}$ ≈ $R_p$", fontsize=7.5, ha="center", va="bottom")
    ax.text(1700, 1000, "← high f   low f →", fontsize=6.8, ha="center", color="#666666", alpha=0)
    ax.legend(loc="upper right", bbox_to_anchor=(1.02, 1.12), fontsize=7, ncol=1)
    # circuit inset (upper left)
    ci = fig.add_axes([0.075, 0.71, 0.13, 0.17])
    ci.set_xlim(0, 10); ci.set_ylim(0, 6); ci.axis("off")
    ci.plot([0, 1], [3, 3], color=INK, lw=0.8)
    ci.add_patch(Rectangle((1, 2.5), 2.2, 1.0, fc="white", ec=INK, lw=0.8))
    ci.text(2.1, 3.0, "$R_s$", fontsize=6.5, ha="center", va="center")
    ci.plot([3.2, 4.2], [3, 3], color=INK, lw=0.8)
    ci.plot([4.2, 4.2], [1.2, 4.8], color=INK, lw=0.8)
    ci.plot([8.4, 8.4], [1.2, 4.8], color=INK, lw=0.8)
    ci.plot([4.2, 5.2], [4.8, 4.8], color=INK, lw=0.8); ci.plot([7.4, 8.4], [4.8, 4.8], color=INK, lw=0.8)
    ci.add_patch(Rectangle((5.2, 4.3), 2.2, 1.0, fc="white", ec=INK, lw=0.8))
    ci.text(6.3, 4.8, "$R_{ct}$", fontsize=6.5, ha="center", va="center")
    ci.plot([4.2, 6.0], [1.2, 1.2], color=INK, lw=0.8); ci.plot([6.6, 8.4], [1.2, 1.2], color=INK, lw=0.8)
    ci.plot([6.0, 6.0], [0.5, 1.9], color=INK, lw=1.0); ci.plot([6.6, 6.6], [0.5, 1.9], color=INK, lw=1.0)
    ci.text(6.3, -0.35, "$C_{\\rm dl}$", fontsize=6.5, ha="center", va="center")
    ci.plot([8.4, 9.6], [3, 3], color=INK, lw=0.8)

    # Bode
    bx = fig.add_axes([0.64, 0.15, 0.27, 0.75])
    bx.loglog(f, np.abs(Z), color=COLORS[0], lw=2)
    bx.set_xlabel("Frequency (Hz)")
    bx.set_ylabel("|$Z$| (Ω cm$^2$)", color=COLORS[0])
    bx.set_xlim(1e-2, 1e5); bx.set_ylim(5, 5000)
    bx.set_xticks([1e-2, 1, 1e2, 1e4])
    bp = bx.twinx()
    bp.spines["right"].set_visible(True)
    phase = -np.degrees(np.angle(Z))
    bp.semilogx(f, phase, color=COLORS[1], lw=1.8)
    bp.set_ylabel("−phase angle (°)", color=COLORS[1])
    bp.set_ylim(0, 90)
    k = np.argmax(phase)
    bp.plot(f[k], phase[k], "o", color=COLORS[1], ms=4)
    bp.text(f[k] * 1.6, phase[k] + 1, f"peak {phase[k]:.0f}° at {f[k]:.0f} Hz", fontsize=7, color=COLORS[1], va="bottom")
    bx.axvline(fa, color="#888888", ls=":", lw=0.8)
    bx.text(fa * 0.8, 4000, "1.6 Hz", fontsize=6.5, ha="right", va="center", color="#555555")
    bx.text(3e-2, 1250, "$R_s+R_{ct}$", fontsize=7, color=COLORS[0], va="top")
    bx.text(1.5e3, 13, "$R_s$", fontsize=7, color=COLORS[0])
    save(fig, "43", "fig-43-6-eis-randles")


if __name__ == "__main__":
    galvanic_series()
    pit_crevice()
    sensitization()
    scc_velocity()
    cathodic_protection()
    eis_randles()
