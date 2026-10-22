"""Figures for Chapter 15 — Physical Metallurgy of Steels and Cast Irons.

Run from the repository root:  python figures/scripts/ch15.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Ellipse
from scipy.interpolate import PchipInterpolator

from figstyle import new_fig, save, COLORS, INK, GRID


# ---------------------------------------------------------------------------
# Fe–Fe3C diagram helpers
# ---------------------------------------------------------------------------
def _quad(p0, p1, p2, x):
    (x0, y0), (x1, y1), (x2, y2) = p0, p1, p2
    c = np.polyfit([x0, x1, x2], [y0, y1, y2], 2)
    return np.polyval(c, x)


def _A3(x):
    return _quad((0, 912), (0.4, 795), (0.76, 727), x)


def _Acm(x):
    return _quad((0.76, 727), (1.2, 865), (2.14, 1147), x)


def _draw_fec(ax, lw=1.4):
    k = dict(color=INK, lw=lw)
    ax.plot([0, 0.53], [1538, 1495], **k)                  # delta liquidus
    ax.plot([0.53, 4.30], [1495, 1147], **k)               # gamma liquidus
    ax.plot([4.30, 6.70], [1147, 1227], **k)               # Fe3C liquidus
    ax.plot([0, 0.09], [1538, 1495], **k)                  # delta solidus
    ax.plot([0.09, 0.0], [1495, 1394], **k)                # delta / delta+gamma
    ax.plot([0.17, 0.0], [1495, 1394], **k)                # delta+gamma / gamma
    ax.plot([0.17, 2.14], [1495, 1147], **k)               # gamma solidus
    ax.plot([0.09, 0.53], [1495, 1495], **k)               # peritectic
    ax.plot([2.14, 6.70], [1147, 1147], **k)               # eutectic
    ax.plot([0.022, 6.70], [727, 727], **k)                # eutectoid
    xa = np.linspace(0, 0.76, 60)
    ax.plot(xa, _A3(xa), **k)                              # A3
    ax.plot([0, 0.022], [912, 727], **k)                   # alpha / alpha+gamma
    xs = np.linspace(0.76, 2.14, 60)
    ax.plot(xs, _Acm(xs), **k)                             # Acm
    ys = np.linspace(727, 400, 30)
    ax.plot(0.022 * ((ys - 300) / 427) ** 2, ys, **k)      # alpha solvus
    ax.plot([6.70, 6.70], [400, 1227], **k)                # Fe3C


def fe_fe3c_diagram():
    fig = plt.figure(figsize=(6.8, 4.8))
    ax = fig.add_axes([0.09, 0.11, 0.53, 0.74])
    # composition bands
    ax.add_patch(Rectangle((0, 400), 2.14, 1200, fc=COLORS[0], alpha=0.06, lw=0))
    ax.add_patch(Rectangle((2.14, 400), 4.5 - 2.14, 1200, fc=COLORS[1], alpha=0.06, lw=0))
    ax.text(1.6, 425, "steels", ha="center", va="center", fontsize=8.5, color=COLORS[0])
    ax.text(3.32, 425, "cast irons", ha="center", va="center", fontsize=8.5, color=COLORS[1])
    _draw_fec(ax)
    kw = dict(fontsize=9, ha="center", va="center", color=INK)
    ax.text(3.6, 1420, "L", **kw)
    ax.text(1.05, 1090, "γ\n(austenite)", **kw)
    ax.text(2.55, 1260, "L + γ", **kw)
    ax.text(5.6, 1250, "L + Fe$_3$C", **kw)
    ax.text(4.0, 950, "γ + Fe$_3$C", **kw)
    ax.text(3.8, 560, "α + Fe$_3$C", **kw)
    # small fields with leaders
    sk = dict(fontsize=8, arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
    ax.annotate("δ", xy=(0.03, 1450), xytext=(0.5, 1590), **sk)
    ax.annotate("L + δ", xy=(0.25, 1508), xytext=(0.8, 1525), **sk)
    ax.annotate("δ + γ", xy=(0.06, 1430), xytext=(0.3, 1310), **sk)
    ax.annotate("α + γ", xy=(0.3, 760), xytext=(1.0, 800), **sk)
    ax.annotate("α", xy=(0.008, 600), xytext=(0.9, 520), **sk)
    # invariant points
    for x, y, lab, dx, dy in [(0.17, 1495, "1495 °C, 0.17 %", 0.35, 1450),
                              (4.30, 1147, "eutectic 1147 °C, 4.30 %", 3.2, 1060),
                              (0.76, 727, "eutectoid 727 °C, 0.76 %", 1.25, 655)]:
        ax.plot(x, y, "o", ms=4, color=INK, zorder=5)
    ax.text(2.25, 1110, "eutectic 1147 °C\n(γ 2.14 %, L 4.30 %)", fontsize=7.5, ha="left", va="top")
    ax.text(0.95, 690, "eutectoid 727 °C (α 0.022 %, γ 0.76 %)", fontsize=7.5, ha="left", va="top")
    ax.text(1.25, 1640, "peritectic 1495 °C\n(δ 0.09, γ 0.17, L 0.53 %)", fontsize=7.5, ha="left",
            va="top")
    # critical line labels
    ax.text(5.9, 735, "$A_1$", fontsize=9, color=COLORS[1], va="bottom")
    ax.text(0.56, 845, "$A_3$", fontsize=9, color=COLORS[1])
    ax.text(1.55, 925, "$A_{cm}$", fontsize=9, color=COLORS[1])
    ax.axvline(0.45, color=COLORS[2], lw=1.0, ls="--", ymax=(1000 - 400) / 1250)
    ax.text(0.5, 408, "0.45 %", fontsize=7.5, color=COLORS[2], rotation=90, va="bottom")
    ax.set_xlim(0, 6.9)
    ax.set_ylim(400, 1650)
    ax.set_xlabel("Carbon (wt%)")
    ax.set_ylabel("Temperature (°C)")
    sec = ax.secondary_xaxis("top", functions=(lambda v: v / 6.70, lambda v: v * 6.70))
    sec.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    sec.tick_params(labelsize=8)
    sec.set_xlabel("weight fraction Fe$_3$C", fontsize=9)
    ax.spines["top"].set_visible(True)
    ax.add_patch(Rectangle((0, 600), 1.4, 400, fc="none", ec=COLORS[2], lw=0.9, ls=":"))

    # ---- zoom with heat-treatment windows
    az = fig.add_axes([0.72, 0.11, 0.27, 0.74])
    x1 = np.linspace(0, 0.76, 80)
    x2 = np.linspace(0.76, 1.4, 80)
    def band(x, lo, hi, c, lab=None):
        az.fill_between(x, lo, hi, color=c, alpha=0.45, lw=0, label=lab)
    band(x1, _A3(x1) + 50, _A3(x1) + 80, COLORS[0], "normalizing")
    band(x2, _Acm(x2) + 50, np.minimum(_Acm(x2) + 80, 1000), COLORS[0])
    band(x1, _A3(x1) + 30, _A3(x1) + 50, COLORS[1], "full anneal / harden")
    band(x2, 727 + 30, 727 + 50, COLORS[1])
    band(np.linspace(0.25, 1.4, 10), 690, 720, COLORS[2], "spheroidize")
    az.plot(x1, _A3(x1), color=INK, lw=1.3)
    az.plot(x2, _Acm(x2), color=INK, lw=1.3)
    az.plot([0, 0.022], [912, 727], color=INK, lw=1.3)
    az.plot([0.022, 1.4], [727, 727], color=INK, lw=1.3)
    az.axvline(0.45, color=COLORS[2], lw=1.0, ls="--")
    az.text(0.43, 745, "1045", fontsize=7, color=COLORS[2], rotation=90, ha="right", va="bottom")
    az.text(0.1, 735, "$A_1$", fontsize=8)
    az.text(0.08, 885, "$A_3$", fontsize=8)
    az.text(1.0, 790, "$A_{cm}$", fontsize=8)
    az.text(0.12, 668, "α + P", fontsize=8, color=INK)
    az.text(1.05, 668, "P + Fe$_3$C", fontsize=8, color=INK, ha="center")
    az.set_xlim(0, 1.4)
    az.set_ylim(600, 1000)
    az.set_xlabel("Carbon (wt%)", fontsize=9)
    az.tick_params(labelsize=8)
    az.set_title("heat-treatment windows", fontsize=9)
    az.legend(loc="lower center", bbox_to_anchor=(0.55, 0.0), fontsize=7, handlelength=1.2)
    for sp in ["top", "right"]:
        az.spines[sp].set_visible(True)
    save(fig, "15", "fig-15-1-fe-fe3c-diagram")


# ---------------------------------------------------------------------------
# 15.2 Properties versus carbon
# ---------------------------------------------------------------------------
HRC_HV = [(20, 238), (30, 302), (40, 392), (50, 513), (55, 595), (60, 697), (65, 832)]


def properties_vs_carbon():
    fig = plt.figure(figsize=(6.8, 3.9))
    ax = fig.add_axes([0.09, 0.14, 0.43, 0.76])
    x = np.linspace(0.05, 1.2, 300)
    mart = PchipInterpolator([0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0, 1.2],
                             [360, 400, 490, 575, 650, 730, 800, 845, 865, 875, 875])(x)
    norm = PchipInterpolator([0.05, 0.08, 0.2, 0.45, 0.8, 0.95, 1.2],
                             [95, 102, 137, 205, 300, 302, 305])(x)
    sph = PchipInterpolator([0.05, 0.2, 0.45, 0.8, 1.2], [80, 110, 150, 180, 200])(x)
    temp = PchipInterpolator([0.05, 0.2, 0.45, 0.8, 1.2], [190, 220, 270, 310, 330])(x)
    ax.plot(x, mart, color=COLORS[1], lw=2, label="as-quenched martensite")
    ax.plot(x, temp, color=COLORS[3], lw=2, label="quenched + tempered 600 °C")
    ax.plot(x, norm, color=COLORS[0], lw=2, label="normalized ferrite–pearlite")
    ax.plot(x, sph, color=COLORS[2], lw=2, label="spheroidized")
    ax.annotate("retained austenite\nlimits hardness", xy=(1.0, 875), xytext=(0.62, 935),
                fontsize=7.5, arrowprops=dict(arrowstyle="-", lw=0.7), va="bottom")
    ax.set_xlim(0, 1.2)
    ax.set_ylim(0, 1000)
    ax.set_xlabel("Carbon (wt%)")
    ax.set_ylabel("Hardness (HV)")
    ax.legend(loc="center right", fontsize=7.5, bbox_to_anchor=(1.0, 0.52))
    sec = ax.secondary_yaxis("right", functions=(lambda v: v, lambda v: v))
    sec.set_yticks([hv for _, hv in HRC_HV])
    sec.set_yticklabels([str(h) for h, _ in HRC_HV], fontsize=8)
    sec.set_ylabel("≈ HRC", fontsize=9, labelpad=2)
    ax.spines["right"].set_visible(True)

    # Table 15.1 panel
    ax2 = fig.add_axes([0.71, 0.14, 0.22, 0.76])
    C = np.array([0.08, 0.20, 0.45, 0.80, 0.95])
    uts = np.array([320, 450, 670, 1025, 1010])
    uts_e = np.array([20, 10, 20, 25, 10])
    ys = np.array([200, 345, 420, 540, 525])
    el = np.array([40, 35, 22.5, 11, 9.5])
    ax2.errorbar(C, uts, yerr=uts_e, fmt="o-", color=COLORS[1], ms=4, lw=1.5, capsize=2, label="UTS")
    ax2.plot(C, ys, "s-", color=COLORS[0], ms=4, lw=1.5, label="yield")
    ax2.set_xlim(0, 1.0)
    ax2.set_ylim(0, 1200)
    ax2.set_xlabel("Carbon (wt%)")
    ax2.set_ylabel("Strength (MPa)")
    ax3 = ax2.twinx()
    ax3.plot(C, el, "^--", color=COLORS[2], ms=4, lw=1.5, label="elongation")
    ax3.set_ylim(0, 50)
    ax3.set_ylabel("Elongation (%)", color=COLORS[2])
    ax3.tick_params(axis="y", colors=COLORS[2])
    ax3.spines["right"].set_visible(True)
    ax3.spines["right"].set_color(COLORS[2])
    h1, l1 = ax2.get_legend_handles_labels()
    h2, l2 = ax3.get_legend_handles_labels()
    ax2.legend(h1 + h2, l1 + l2, loc="upper center", fontsize=7, bbox_to_anchor=(0.5, 1.0))
    ax2.set_title("normalized (Table 15.1)", fontsize=9)
    save(fig, "15", "fig-15-2-properties-vs-carbon")


# ---------------------------------------------------------------------------
# 15.3 CCT diagrams
# ---------------------------------------------------------------------------
def _c_curve(Tu, Tn, tn, Tl, k_up=0.55, k_dn=0.5, n=200):
    """Return (t, T) of a C-shaped start/finish curve between Tl and Tu (asymptote at Tu)."""
    T_up = np.linspace(Tn, Tu - 3, n)
    lt_up = np.log10(tn) + k_up * ((T_up - Tn) / (Tu - T_up)) ** 0.8
    T_dn = np.linspace(Tl, Tn, n)
    lt_dn = np.log10(tn) + k_dn * ((Tn - T_dn) / (Tn - Tl)) ** 2
    T = np.r_[T_dn, T_up]
    return 10 ** np.r_[lt_dn, lt_up], T


def _cool_surface(t):
    return 60 + 790 * np.exp(-(t / 7.5) ** 0.42)


def _cool_centre(t):
    return 60 + 790 * np.exp(-t / 71.0)


def cct_diagrams():
    fig, axs = plt.subplots(1, 2, figsize=(6.8, 3.9), sharey=True)
    fig.subplots_adjust(wspace=0.08, left=0.09, right=0.98, bottom=0.14, top=0.90)
    t = np.logspace(-1, 5, 600)
    specs = {
        "1045": dict(Ac3=780, Ac1=725, Ms=326,
                     curves=[("F", (780, 650, 1.0, 610), COLORS[2]),
                             ("P start", (725, 575, 2.0, 530), COLORS[1]),
                             ("P finish", (725, 575, 9.0, 530), COLORS[1]),
                             ("B", (530, 450, 3.0, 326), COLORS[0])],
                     labels=[(4.0, 690, "F"), (200, 650, "P"), (12, 420, "B")],
                     ends=["martensite +\nsome bainite", "ferrite + pearlite\n(~20 HRC)"]),
        "4140": dict(Ac3=790, Ac1=730, Ms=330,
                     curves=[("F+P start", (790, 650, 100, 560), COLORS[1]),
                             ("F+P finish", (730, 650, 1000, 580), COLORS[1]),
                             ("B start", (550, 470, 10, 330), COLORS[0]),
                             ("B finish", (550, 470, 150, 330), COLORS[0])],
                     labels=[(400, 690, "F + P"), (35, 440, "B")],
                     ends=["martensite", "martensite + bainite\n(~45 HRC)"]),
    }
    for ax, (steel, sp) in zip(axs, specs.items()):
        for name, (Tu, Tn, tn, Tl), c in sp["curves"]:
            tc, Tc = _c_curve(Tu, Tn, tn, Tl)
            ls = "--" if "finish" in name else "-"
            ax.plot(tc, Tc, color=c, lw=1.6, ls=ls)
        for x, y, lab in sp["labels"]:
            ax.text(x, y, lab, fontsize=9, fontweight="bold", ha="center", va="center", color=INK)
        ax.axhline(sp["Ac3"], color=GRID, lw=0.9, ls="-")
        ax.axhline(sp["Ac1"], color=GRID, lw=0.9, ls="-")
        ax.text(1.2e5, sp["Ac3"] + 4, "$Ac_3$", fontsize=7.5, ha="right", va="bottom")
        ax.text(1.2e5, sp["Ac1"] - 4, "$Ac_1$", fontsize=7.5, ha="right", va="top")
        Ms = sp["Ms"]
        for T_, lab in [(Ms, f"$M_s$ = {Ms} °C"), (Ms - 63, "$M_{50}$"), (Ms - 209, "$M_{90}$")]:
            ax.axhline(T_, color=INK, lw=0.9, ls="--")
            ax.text(1.2e5, T_ + 4, lab, fontsize=7.5, ha="right", va="bottom")
        ax.plot(t, _cool_surface(t), color=COLORS[3], lw=1.6)
        ax.plot(t, _cool_centre(t), color=COLORS[4], lw=1.6)
        ax.text(0.12, 655, "surface,\noil", fontsize=7, color=COLORS[3])
        # end-of-curve microstructure labels
        ax.annotate(sp["ends"][0], xy=(12, _cool_surface(12)), xytext=(0.15, 140), fontsize=7.5,
                    color=COLORS[3], arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[3]))
        ax.annotate(sp["ends"][1], xy=(140, _cool_centre(140)), xytext=(400, 380), fontsize=7.5,
                    color=COLORS[4], ha="left", arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[4]))
        ax.set_xscale("log")
        ax.set_xlim(0.1, 1e5)
        ax.set_ylim(100, 900)
        ax.set_xlabel("Time (s)")
        ax.set_title(f"AISI {steel}", fontsize=10)
    axs[0].set_ylabel("Temperature (°C)")
    for a in axs:
        a.annotate("centre of 50 mm bar, oil", xy=(12, _cool_centre(12)), xytext=(60, 850), fontsize=7,
                   color=COLORS[4], ha="left", va="center",
                   arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[4]))
    axs[0].set_xticks([0.1, 1, 10, 100, 1e3, 1e4])
    axs[1].set_xticks([1, 10, 100, 1e3, 1e4, 1e5])
    save(fig, "15", "fig-15-3-cct-diagrams")


# ---------------------------------------------------------------------------
# 15.4 Jominy curves
# ---------------------------------------------------------------------------
def jominy_curves():
    fig, ax = new_fig(6.4, 4.0)
    x = np.linspace(0, 50, 400)
    data = {
        "1040": ([0, 1.5, 3, 4.5, 6, 9, 13, 20, 30, 50], [55, 54, 45, 36, 30, 26, 24, 22, 21, 20], COLORS[0],
                 "$D_I$ ≈ 22 mm"),
        "4140": ([0, 5, 10, 15, 20, 30, 40, 50], [56, 55, 53, 49, 45, 40, 38, 36.5], COLORS[1],
                 "$D_I$ ≈ 120 mm"),
        "4340": ([0, 10, 20, 30, 40, 50], [55, 54, 53, 52, 51, 50], COLORS[2], "$D_I$ ≈ 170 mm"),
    }
    for name, (xs, hs, c, di) in data.items():
        h = PchipInterpolator(xs, hs)(x)
        ax.plot(x, h, color=c, lw=2.2)
    ax.text(25, 23.2, "1040   ($D_I$ ≈ 22 mm)", color=COLORS[0], fontsize=9, ha="center")
    ax.text(23, 46.5, "4140   ($D_I$ ≈ 120 mm)", color=COLORS[1], fontsize=9, ha="left")
    ax.text(25, 54.5, "4340   ($D_I$ ≈ 170 mm)", color=COLORS[2], fontsize=9, ha="center")
    ax.axhline(43, color=INK, lw=0.9, ls="--")
    ax.text(49.5, 43.5, "50 % martensite, 0.4 % C (≈ 43 HRC)", fontsize=8, ha="right", va="bottom")
    ax.set_xlim(0, 50)
    ax.set_ylim(20, 60)
    ax.set_xlabel("Distance from quenched end (mm)")
    ax.set_ylabel("Hardness (HRC)")
    sec = ax.secondary_xaxis("top", functions=(lambda v: v, lambda v: v))
    sec.set_xticks([1.5, 5, 10, 20, 30, 50])
    sec.set_xticklabels(["300", "70", "30", "10", "5", "3"], fontsize=8.5)
    sec.set_xlabel("Cooling rate at 700 °C (°C/s)", fontsize=9)
    ax.spines["top"].set_visible(True)
    save(fig, "15", "fig-15-4-jominy-curves")


# ---------------------------------------------------------------------------
# 15.5 Schaeffler diagram
# ---------------------------------------------------------------------------
ISO = {0: (18.0, 1.9), 5: (19.5, 1.85), 10: (20.6, 1.8), 20: (22.6, 1.7), 40: (27.5, 1.5),
       80: (32.5, 1.1), 100: (35.5, 0.9)}


def _iso_x(p, y):
    x12, s = ISO[p]
    return x12 + (y - 12) / s


def schaeffler():
    fig, ax = new_fig(6.6, 5.0)
    yJ1 = 9.8
    J1 = (_iso_x(0, yJ1), yJ1)
    J3 = (_iso_x(100, 5.0), 5.0)
    J2 = (12.5, 6.0)
    def on13(x):
        return J1[1] + (x - J1[0]) * (J3[1] - J1[1]) / (J3[0] - J1[0])
    J4 = (20.5, on13(20.5))
    top0 = (_iso_x(0, 32), 32)
    y100_40 = 12 + (40 - 35.5) * 0.9
    fields = {
        "A": [(0, 19), J1, top0, (0, 32)],
        "A + M": [(0, 19), J1, J2, (0, 10)],
        "M": [(0, 10), J2, (14, 0), (0, 0)],
        "A+M+F": [J1, J4, J2],
        "M + F": [J2, J4, J3, (19.5, 0), (14, 0)],
        "F": [J3, (40, y100_40), (40, 0), (19.5, 0)],
        "A + F": [J1, top0, (40, 32), (40, y100_40), J3],
    }
    fc = {"A": "#E7EEF8", "A + M": "#EFE7F3", "M": "#F7E3DA", "A+M+F": "#F2F2F2", "M + F": "#F6EFD9",
          "F": "#E4F1E4", "A + F": "#FFFFFF"}
    for k, pts in fields.items():
        ax.add_patch(Polygon(pts, closed=True, fc=fc[k], ec=INK, lw=1.3, zorder=1))
    # zones (hatched)
    zones = [
        ([(0, 19), J1, top0, (0, 32)], COLORS[1], "\\\\\\", "hot cracking\n(fully austenitic)", (6, 27)),
        ([(_iso_x(40, on13(_iso_x(40, 7.0))), on13(_iso_x(40, 7.0))), (_iso_x(40, 32), 32), (40, 32),
          (40, y100_40), J3], COLORS[3], "///", "sigma\nembrittlement\n(high ferrite)", (37.2, 23.5)),
        ([(0, 10), J2, (14, 0), (0, 0)], COLORS[0], "...", "martensite cracking", (6.5, 4.0)),
        ([J3, (40, y100_40), (40, 0), (19.5, 0)], COLORS[2], "xx", "grain growth\n(ferritic)", (32, 3.2)),
    ]
    for pts, c, h, lab, (lx, ly) in zones:
        ax.add_patch(Polygon(pts, closed=True, fc="none", ec=c, hatch=h, lw=0, alpha=0.45, zorder=2))
        ax.text(lx, ly, lab, fontsize=7.5, color=c, ha="center", va="center", fontweight="bold",
                zorder=6, bbox=dict(fc="white", ec="none", pad=0.8, alpha=0.85))
    # iso-ferrite lines
    for p in [5, 10, 20, 40, 80]:
        # intersection with J1-J3 line
        xs = np.linspace(J1[0], J3[0], 2000)
        diff = _iso_x(p, on13(xs)) - xs
        x0 = xs[np.argmin(np.abs(diff))]
        y0 = on13(x0)
        y1 = 32.0
        x1 = _iso_x(p, y1)
        if x1 > 40:
            x1, y1 = 40, 12 + (40 - ISO[p][0]) * ISO[p][1]
        ax.plot([x0, x1], [y0, y1], color=INK, lw=0.8, ls="--", zorder=3)
        yl = {5: 29.0, 10: 27.0, 20: 20.0}.get(p, y1 - 0.4)
        xl = min(_iso_x(p, yl), 39.6)
        ax.text(xl, yl, f"{p} %", fontsize=7, ha="center", va="center", zorder=4,
                bbox=dict(fc="white", ec="none", pad=0.3))
    ax.text(_iso_x(0, 31.0), 31.0, "0 %", fontsize=7, ha="center", va="center", zorder=4,
            bbox=dict(fc="white", ec="none", pad=0.3))
    ax.text(39.8, y100_40 + 0.3, "100 %", fontsize=7, ha="right", va="bottom", zorder=4)
    # field labels
    fl = dict(fontsize=11, fontweight="bold", ha="center", va="center", color=INK, zorder=5)
    ax.text(10, 22, "A", **fl)
    ax.text(5, 13.5, "A + M", **fl)
    ax.text(5, 6.5, "M", **fl)
    ax.text(26, 18, "A + F", **fl)
    ax.text(18.2, 2.5, "M + F", fontsize=9, fontweight="bold", ha="center", color=INK, zorder=5)
    ax.text(31, 8.5, "F", **fl)
    ax.annotate("A + M + F", xy=(16.3, 8.3), xytext=(9.0, 8.6), fontsize=7.5, zorder=6,
                arrowprops=dict(arrowstyle="-", lw=0.6))
    # grades
    grades = [("304", 19.25, 11.25, (-2.6, 0.5)), ("316L", 19.9, 12.4, (0.6, 1.4)),
              ("2205", 25.9, 6.9, (0.6, -1.5)), ("430", 17, 1.0, (0.6, 0.6)),
              ("410", 12.5, 3.0, (0.5, -1.3)), ("mild steel", 1.0, 1.5, (0.7, -1.0)),
              ("309 filler", 24.0, 14.0, (0.6, 0.6))]
    for name, x, y, (dx, dy) in grades:
        ax.plot(x, y, "o", ms=5.5, color=COLORS[1] if name != "309 filler" else COLORS[0], zorder=7,
                mec="white", mew=0.6)
        ax.text(x + dx, y + dy, name, fontsize=8, zorder=7, color=INK)
    # dissimilar weld construction
    mix = ((19.25 + 1.0) / 2, (11.25 + 1.5) / 2)
    ax.plot([1.0, 19.25], [1.5, 11.25], color=COLORS[0], lw=1.0, zorder=6)
    ax.plot([mix[0], 24.0], [mix[1], 14.0], color=COLORS[0], lw=1.0, zorder=6)
    weld = (0.7 * 24.0 + 0.3 * mix[0], 0.7 * 14.0 + 0.3 * mix[1])
    ax.plot(*mix, "s", ms=4.5, color=COLORS[0], zorder=7)
    ax.plot(*weld, "D", ms=6, color=COLORS[0], zorder=7, mec="white", mew=0.6)
    ax.annotate("weld: 309 + 30 % dilution\n(50/50 304 + mild steel)\n→ A + F, ~5–8 % ferrite",
                xy=weld, xytext=(21.5, 23.5), fontsize=7.5, color=COLORS[0], zorder=8,
                bbox=dict(fc="white", ec="none", pad=0.8, alpha=0.9),
                arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[0]))
    ax.set_xlim(0, 40)
    ax.set_ylim(0, 32)
    ax.set_xlabel("Cr$_{eq}$ = Cr + Mo + 1.5 Si + 0.5 Nb (wt%)")
    ax.set_ylabel("Ni$_{eq}$ = Ni + 30 C + 0.5 Mn (wt%)")
    ax.spines["top"].set_visible(True)
    ax.spines["right"].set_visible(True)
    save(fig, "15", "fig-15-5-schaeffler")


# ---------------------------------------------------------------------------
# 15.6 AHSS banana
# ---------------------------------------------------------------------------
def ahss_banana():
    fig, ax = new_fig(6.6, 4.4)
    grades = [
        ("IF", (280, 350), (40, 50), "conv"), ("Mild", (300, 400), (32, 42), "conv"),
        ("BH", (350, 450), (30, 38), "conv"), ("HSLA", (450, 650), (18, 28), "conv"),
        ("DP", (500, 1200), (10, 30), "g1"), ("TRIP", (600, 1000), (22, 35), "g1"),
        ("CP", (800, 1100), (10, 18), "g1"), ("MS", (1000, 1700), (3, 8), "g1"),
        ("PHS 22MnB5", (1300, 1600), (5, 8), "g1"),
        ("Q&P, medium-Mn\n(3rd gen)", (980, 1500), (15, 30), "g3"),
        ("TWIP", (900, 1100), (45, 65), "g2"), ("301 stainless", (700, 1300), (30, 60), "g2"),
    ]
    col = {"conv": "#9E9E9E", "g1": COLORS[0], "g3": COLORS[2], "g2": COLORS[1]}
    for name, (u0, u1), (e0, e1), g in grades:
        ax.add_patch(Ellipse(((u0 + u1) / 2, (e0 + e1) / 2), u1 - u0, e1 - e0, fc=col[g], alpha=0.28,
                             ec=col[g], lw=1.2))
    lab = {"IF": (315, 45), "Mild": (350, 37), "BH": (400, 33.5), "HSLA": (550, 23), "DP": (720, 14),
           "TRIP": (800, 28.5), "CP": (950, 14), "MS": (1350, 5.5), "PHS 22MnB5": (1455, 9.6),
           "Q&P, medium-Mn\n(3rd gen)": (1240, 22.5), "TWIP": (1000, 55), "301 stainless": (1100, 40)}
    for name, (x, y) in lab.items():
        ax.text(x, y, name, fontsize=7.5, ha="center", va="center", color=INK)
    # banana band for conventional + 1st generation
    u = np.linspace(250, 1750, 300)
    hi = np.polyval(np.polyfit(np.log([250, 450, 700, 1000, 1300, 1750]), [56, 42, 35, 25, 14, 9.5], 2),
                    np.log(u))
    lo = np.polyval(np.polyfit(np.log([250, 500, 700, 1000, 1300, 1750]), [33, 15, 8.5, 4.5, 2.6, 2.0], 2),
                    np.log(u))
    ax.plot(u, hi, color=INK, lw=1.0, ls="--")
    ax.plot(u, lo, color=INK, lw=1.0, ls="--")
    ax.text(1990, 15.5, "banana: conventional +\n1st-generation AHSS\n(DP, TRIP, CP, MS, PHS)", fontsize=8,
            ha="right", va="center", color=COLORS[0])
    ax.text(1530, 30, "3rd generation", fontsize=9, color=COLORS[2], fontweight="bold")
    ax.text(1350, 62, "2nd generation (high Mn,\naustenitic)", fontsize=9, color=COLORS[1],
            fontweight="bold", va="center")
    ax.text(215, 61, "conventional\n(grey)", fontsize=8, color="#777777")
    ax.set_xlim(200, 2000)
    ax.set_ylim(0, 70)
    ax.set_xlabel("Tensile strength (MPa)")
    ax.set_ylabel("Total elongation (%)")
    save(fig, "15", "fig-15-6-ahss-banana")


if __name__ == "__main__":
    fe_fe3c_diagram()
    properties_vs_carbon()
    cct_diagrams()
    jominy_curves()
    schaeffler()
    ahss_banana()
