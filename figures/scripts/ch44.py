"""Figures for Chapter 44 — Degradation and Failure Analysis.

Run from the repository root:  python figures/scripts/ch44.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (Rectangle, Polygon, Circle, Ellipse, Wedge, FancyBboxPatch,
                                FancyArrowPatch, PathPatch)
from matplotlib.path import Path
from scipy.spatial import Voronoi

R_GAS = 8.314


# ---------------------------------------------------------------- Figure 44.1
def tuutti():
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.8, 3.6), gridspec_kw=dict(width_ratios=[1, 1.05]))
    fig.subplots_adjust(wspace=0.32, left=0.09, right=0.98, bottom=0.14, top=0.90)
    t = np.linspace(0, 100, 400)
    for k, c in [(4, COLORS[1]), (2, COLORS[0])]:
        ax.plot(t, k * np.sqrt(t), color=c, lw=2)
    ax.text(70, 4 * np.sqrt(70) + 1.5, "$k$ = 4 mm/yr$^{1/2}$", color=COLORS[1], fontsize=8, ha="right")
    ax.text(97, 2 * np.sqrt(97) - 3.6, "$k$ = 2", color=COLORS[0], fontsize=8, ha="right")
    for c_ in (20, 30):
        ax.axhline(c_, color="#777777", ls="--", lw=0.9)
        ax.text(99, c_ + 0.6, f"cover {c_} mm", fontsize=7.5, ha="right", va="bottom", color="#555555")
    for tt, cc, lab in [(25, 20, "25 y"), (56.25, 30, "56 y")]:
        ax.plot([tt], [cc], "o", color=COLORS[1], ms=5)
        ax.plot([tt, tt], [0, cc], color=COLORS[1], lw=0.7, ls=":")
        ax.text(tt + 1.5, 1.2, lab, fontsize=8, color=COLORS[1])
    ax.text(85, 31.6, "$k$ = 2, 30 mm:\n225 y →", fontsize=7.5, color=COLORS[0], ha="left", va="bottom",
            alpha=0)
    ax.text(99, 28.9, "$k$ = 2 reaches 30 mm\nonly at 225 y (off scale) →", fontsize=7.5, color=COLORS[0], ha="right", va="top")
    ax.set_xlim(0, 100); ax.set_ylim(0, 50)
    ax.set_xlabel("Time (years)")
    ax.set_ylabel("Carbonation depth $x = k\\sqrt{t}$ (mm)")
    ax.set_title("(a) carbonation front", fontsize=9)

    # (b) Tuutti schematic
    ti = 4.0
    tt = np.linspace(0, 10, 300)
    d = 0.18 * np.clip(tt - ti, 0, None) ** 1.35
    bx.axvspan(0, ti, color=COLORS[0], alpha=0.10, lw=0)
    bx.axvspan(ti, 10, color=COLORS[1], alpha=0.08, lw=0)
    bx.plot(tt, d, color=INK, lw=2)
    for y, lab in [(0.35, "cracking"), (0.85, "spalling"), (1.55, "collapse risk")]:
        bx.plot([ti, 10], [y, y], color="#888888", ls="--", lw=0.8)
        bx.text(ti + 0.12, y + 0.03, lab, fontsize=7.5, va="bottom", color="#444444")
    bx.axvline(ti, color=INK, lw=0.8, ls=":")
    bx.text(ti - 0.1, 1.98, "depassivation", fontsize=7.5, ha="right", va="top")
    bx.text(ti / 2, 1.2, "initiation", fontsize=9, ha="center", weight="bold", color=COLORS[0])
    bx.text(ti / 2, 1.08, "agents: CO$_2$, Cl$^-$\npenetrate the cover", fontsize=7.3, ha="center",
            va="top", color=COLORS[0])
    bx.text(6.6, 1.75, "propagation", fontsize=9, ha="center", weight="bold", color=COLORS[1])
    bx.text(7.6, 0.98 + 0.0, "", fontsize=7)
    bx.text(9.9, 0.06, "rate set by O$_2$, H$_2$O,\ntemperature", fontsize=7.3, ha="right",
            va="bottom", color=COLORS[1])
    bx.set_xlim(0, 10); bx.set_ylim(0, 2.05)
    bx.set_xticks([]); bx.set_yticks([])
    bx.set_xlabel("Time")
    bx.set_ylabel("Damage (corrosion, cracking)")
    bx.set_title("(b) Tuutti two-stage model", fontsize=9)
    save(fig, "44", "fig-44-1-tuutti-concrete-life")


# ---------------------------------------------------------------- Figure 44.2
def arrhenius_aging():
    TC = np.array([150.0, 135.0, 120.0])
    L = np.array([300.0, 1000.0, 3500.0])
    T = TC + 273.15
    slope, icpt = np.polyfit(1 / T, np.log(L), 1)
    fig, ax = new_fig(6.4, 4.0)
    xs = lambda Tk: 1000.0 / Tk
    # shaded extrapolation band
    ax.axvspan(xs(T[-1]), 3.0, color="#999999", alpha=0.12, lw=0)
    ax.text(2.78, 2.0e2, "extrapolation:\nmechanism must not change", fontsize=8, ha="center", color="#444444")
    # fit within data
    Td = np.linspace(T[0], T[-1], 50)
    ax.semilogy(xs(Td), np.exp(icpt + slope / Td), color=COLORS[0], lw=2,
                label=f"fit $E_a$ = {slope * R_GAS / 1000:.0f} kJ/mol")
    Te = np.linspace(T[-1], 333.15, 80)
    ax.semilogy(xs(Te), np.exp(icpt + slope / Te), color=COLORS[0], lw=1.6, ls="--")
    # Ea = 80 kJ/mol from 150 C point
    T80 = np.linspace(T[0], 333.15, 80)
    L80 = 300 * np.exp(80e3 / R_GAS * (1 / T80 - 1 / T[0]))
    ax.semilogy(xs(T80), L80, color=COLORS[1], lw=1.6, ls="--", label="if $E_a$ = 80 kJ/mol at low T")
    ax.semilogy(xs(T), L, "o", color=INK, ms=6, zorder=5, label="oven-aging data")
    # 70 C results
    T70 = 343.15
    L70 = 300 * np.exp(slope * (1 / T70 - 1 / T[0]))
    L70b = 300 * np.exp(80e3 / R_GAS * (1 / T70 - 1 / T[0]))
    ax.plot([xs(T70)], [L70], "s", color=COLORS[0], ms=6)
    ax.plot([xs(T70)], [L70b], "s", color=COLORS[1], ms=6)
    ax.text(xs(T70) - 0.012, L70 * 1.25, f"70 °C: {L70:.1e} h\n(≈ 62 years)".replace("e+05", "×10$^5$"),
            fontsize=7.5, ha="right", va="bottom", color=COLORS[0])
    ax.annotate(f"70 °C if $E_a$ = 80 kJ/mol:\n{L70b:.1e} h (≈ 7 years)".replace("e+04", "×10$^4$"),
                xy=(xs(T70), L70b), xytext=(2.56, 1.3e5), fontsize=7.5, ha="left", va="bottom",
                color=COLORS[1], arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=0.8))
    ax.axhline(2e4, color=COLORS[2], lw=1, ls="-.")
    ax.text(2.31, 2.25e4, "20 000 h: thermal-index reference", fontsize=7.5, color=COLORS[2], va="bottom")
    for x, l, tc in zip(xs(T), L, TC):
        ax.text(x + 0.008, l / 1.5, f"{tc:.0f} °C", fontsize=7, va="top")
    ax.set_xlim(2.3, 3.0)
    ax.set_ylim(1e2, 1e7)
    ax.set_xlabel("1000/$T$ (K$^{-1}$)")
    ax.set_ylabel("Time to 50 % retained elongation (h)")
    ax.legend(loc="upper left", fontsize=7.8)
    top = ax.secondary_xaxis("top", functions=(lambda x: x, lambda x: x))
    tick_c = [160, 150, 135, 120, 100, 90, 70, 60]
    top.set_xticks([1000 / (c + 273.15) for c in tick_c])
    top.set_xticklabels([str(c) for c in tick_c], fontsize=8)
    top.set_xlabel("Temperature (°C)", fontsize=9)
    save(fig, "44", "fig-44-2-arrhenius-polymer-aging")


# ---------------------------------------------------------------- Figure 44.3
def bathtub():
    t = np.linspace(0.002, 1.2, 800)
    h1 = 0.25 * t ** -0.5                # beta = 0.5
    h2 = np.full_like(t, 0.5)            # beta = 1
    eta = 1.15
    h3 = 4 / eta * (t / eta) ** 3        # beta = 4
    h = h1 + h2 + h3
    fig, ax = new_fig(6.4, 3.9)
    ax.axvspan(0, 0.15, color=COLORS[0], alpha=0.10, lw=0)
    ax.axvspan(0.15, 0.75, color=COLORS[2], alpha=0.08, lw=0)
    ax.axvspan(0.75, 1.2, color=COLORS[1], alpha=0.10, lw=0)
    ax.plot(t, h1, ls="--", color=COLORS[0], lw=1.3, label="infant mortality, β = 0.5")
    ax.plot(t, h2, ls="--", color=COLORS[2], lw=1.3, label="random, β = 1")
    ax.plot(t, h3, ls="--", color=COLORS[1], lw=1.3, label="wear-out, β = 4")
    ax.plot(t, h, color=INK, lw=2.4, label="total hazard (bathtub)")
    ax.axvline(1.0, color=INK, ls=":", lw=1)
    ax.text(1.01, 4.6, "design\nlife", fontsize=8, va="top")
    ax.set_xlim(0, 1.2); ax.set_ylim(0, 5)
    ax.set_xlabel("Time (fraction of design life)")
    ax.set_ylabel("Hazard rate $h(t)$ (arb. units)")
    ax.text(0.17, 3.1, "early failures: burn-in,\nproof test, process control", fontsize=7.8,
            ha="left", va="center", color=COLORS[0])
    ax.text(0.45, 2.0, "random failures:\ndesign margin", fontsize=8, ha="center", color="#00704F")
    ax.text(0.86, 3.9, "wear-out:\npreventive\nreplacement", fontsize=8, ha="center", va="center",
            color=COLORS[1])
    ax.legend(loc="upper center", bbox_to_anchor=(0.45, 1.0), fontsize=7.5, ncol=2)
    save(fig, "44", "fig-44-3-bathtub-curve")


# ---------------------------------------------------------------- Figure 44.4
def weibull_seals():
    t = np.array([410, 620, 780, 900, 1020, 1130, 1260, 1400, 1590, 1900.0])
    n = len(t)
    F = (np.arange(1, n + 1) - 0.3) / (n + 0.4)
    y = np.log(-np.log(1 - F))
    b, a = np.polyfit(np.log(t), y, 1)
    eta = np.exp(-a / b)
    b10 = eta * (-np.log(0.9)) ** (1 / b)
    fig, ax = new_fig(6.4, 4.0)
    tt = np.logspace(np.log10(200), np.log10(3000), 100)
    ax.semilogx(tt, b * np.log(tt / eta), color=COLORS[0], lw=1.8,
                label=f"fit: β = {b:.2f}, η = {eta:.0f} h")
    ax.semilogx(t, y, "o", color=COLORS[1], ms=6, zorder=5, label="seal failures (median ranks)")
    y10 = np.log(-np.log(0.9))
    y63 = 0.0
    for yy, xx, lab in [(y10, b10, f"B10 = {b10:.0f} h"), (y63, eta, f"η = {eta:.0f} h")]:
        ax.plot([200, xx], [yy, yy], color="#777777", ls="--", lw=0.9)
        ax.plot([xx, xx], [-3, yy], color="#777777", ls="--", lw=0.9)
        ax.text(xx * 1.03, -2.85, lab, fontsize=8, ha="left", va="bottom")
    ax.set_xlim(200, 3000); ax.set_ylim(-3, 1.5)
    ax.set_xticks([200, 300, 500, 1000, 2000, 3000])
    ax.set_xticklabels(["200", "300", "500", "1000", "2000", "3000"])
    ax.xaxis.set_minor_formatter(plt.NullFormatter())
    ax.set_xlabel("Time to failure (h)")
    ax.set_ylabel("ln[−ln(1 − F)]")
    ax.legend(loc="upper left", fontsize=8)
    ax.text(2050, -1.2, "β = 2.42:\nwear-out", fontsize=9, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=INK, lw=0.8))
    rx = ax.twinx()
    rx.spines["right"].set_visible(True)
    rx.set_ylim(-3, 1.5)
    Fs = [0.05, 0.10, 0.20, 0.50, 0.632, 0.90, 0.95]
    rx.set_yticks([np.log(-np.log(1 - f)) for f in Fs])
    rx.set_yticklabels(["5 %", "10 %", "20 %", "50 %", "63.2 %", "90 %", "95 %"], fontsize=8)
    rx.set_ylabel("Cumulative failures F")
    save(fig, "44", "fig-44-4-weibull-seals")


# ---------------------------------------------------------------- Figure 44.5
def fa_workflow():
    fig, ax = plt.subplots(figsize=(6.8, 5.9))
    fig.subplots_adjust(left=0.005, right=0.995, top=0.995, bottom=0.005)
    ax.set_xlim(0, 13.6); ax.set_ylim(0, 11.8); ax.axis("off")
    G, O, B = "#D6EFD8", "#FBE0C8", "#DCE8F6"
    H, gap = 1.75, 0.45
    left = [
        ("1  Background", "service history, loads, environment,\ndrawings, material certificates,\nsimilar failures", B),
        ("2  Preserve and document", "photographs, chain of custody,\nprotect fracture surfaces", G),
        ("3  Non-destructive examination", "visual, stereo microscope, dye penetrant,\nmagnetic particle, ultrasonic,\neddy current, X-ray CT", G),
        ("4  Fractography", "macro: origin, beach marks, chevrons,\nshear lips;  SEM: dimples, cleavage,\nstriations, intergranular facets", G),
        ("5  Metallography and testing", "sections, hardness, chemistry (OES, EDS),\ntensile and Charpy;\nFTIR/DSC for polymers", O),
    ]
    right = [
        ("6  Mechanism identified", "fatigue, overload, SCC, creep,\nwear, aging ...", B),
        ("7  Root cause", "5-why, fishbone,\nfault tree", B),
        ("8  Verify", "stress analysis,\nreproduce the failure", B),
        ("9  Corrective action", "design, material, process,\ninspection; 8D report,\nFMEA update", B),
    ]

    def draw(col_x, W, items, y_top):
        pos = []
        for k, (title, body, fc) in enumerate(items):
            y = y_top - k * (H + gap) - H
            ax.add_patch(FancyBboxPatch((col_x, y), W, H, boxstyle="round,pad=0.02,rounding_size=0.15",
                                        fc=fc, ec=INK, lw=0.9))
            ax.text(col_x + 0.18, y + H - 0.17, title, fontsize=8.4, weight="bold", va="top")
            ax.text(col_x + 0.18, y + H - 0.58, body, fontsize=7.1, va="top", linespacing=1.2)
            pos.append(y)
        for y0, y1 in zip(pos[:-1], pos[1:]):
            ax.annotate("", xy=(col_x + W / 2, y1 + H), xytext=(col_x + W / 2, y0),
                        arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.1))
        return pos

    xl, WL = 0.1, 6.1
    xr, WR = 7.05, 4.6
    pl = draw(xl, WL, left, 11.7)
    pr = draw(xr, WR, right, 11.7)
    # connector 5 -> 6: right, up the gutter, right
    xm = (xl + WL + xr) / 2
    y5 = pl[-1] + H / 2
    y6 = pr[0] + H / 2
    ax.plot([xl + WL, xm, xm], [y5, y5, y6], color=INK, lw=1.1)
    ax.annotate("", xy=(xr, y6), xytext=(xm, y6), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.1))
    # side input to 7
    sx, sw = xr + WR + 0.3, 13.55 - (xr + WR + 0.3)
    sy = pr[1]
    ax.add_patch(FancyBboxPatch((sx, sy + 0.05), sw, H - 0.1, boxstyle="round,pad=0.02,rounding_size=0.12",
                                fc="white", ec=INK, lw=0.8, ls="--"))
    ax.text(sx + sw / 2, sy + H / 2, "compare\nwith sound\nparts and\ndesign\nassumptions", fontsize=6.6,
            ha="center", va="center", linespacing=1.1)
    ax.annotate("", xy=(xr + WR, sy + H / 2), xytext=(sx, sy + H / 2),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.9))
    # feedback 9 -> design and specifications
    by = pr[-1] - 1.55
    ax.add_patch(FancyBboxPatch((xr + 0.3, by), WR - 0.6, 0.85, boxstyle="round,pad=0.02,rounding_size=0.12",
                                fc="white", ec=COLORS[0], lw=0.9, ls="--"))
    ax.text(xr + WR / 2, by + 0.425, "design and specifications", fontsize=7.8, ha="center", va="center",
            color=COLORS[0])
    ax.annotate("", xy=(xr + WR / 2, by + 0.85), xytext=(xr + WR / 2, pr[-1]),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.1, ls="--"))
    ax.text(xr + WR / 2 + 0.15, pr[-1] - 0.35, "feedback", fontsize=7, color=COLORS[0], va="center")
    # legend
    lx, ly = 7.2, 0.25
    for k, (fc, lab) in enumerate([(G, "non-destructive"), (O, "destructive"), (B, "reasoning")]):
        yy = ly + (2 - k) * 0.42
        ax.add_patch(Rectangle((lx + 2.6, yy), 0.4, 0.3, fc=fc, ec=INK, lw=0.7))
        ax.text(lx + 3.1, yy + 0.15, lab, fontsize=7.5, va="center")
    save(fig, "44", "fig-44-5-failure-analysis-workflow")


# ---------------------------------------------------------------- Figure 44.6
def _scalebar(ax, x, y, L, lab, color="white"):
    ax.plot([x, x + L], [y, y], color=color, lw=2.5, solid_capstyle="butt")
    ax.text(x + L / 2, y + 0.03 * (ax.get_ylim()[1] - ax.get_ylim()[0]), lab, color=color, fontsize=7,
            ha="center", va="bottom", weight="bold",
            bbox=dict(fc="#333333" if color == "white" else "white", ec="none", pad=0.8, alpha=0.75))


def _panel(ax, title):
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(True); s.set_color(INK); s.set_linewidth(0.8)
    ax.set_title(title, fontsize=8.3, pad=3)


def fractography():
    rng = np.random.default_rng(36)
    fig, axs = plt.subplots(2, 3, figsize=(6.8, 4.0))
    fig.subplots_adjust(left=0.01, right=0.99, top=0.94, bottom=0.01, wspace=0.05, hspace=0.12)
    SEM_BG = "#6E6E6E"

    # (a) fatigued shaft cross-section
    ax = axs[0, 0]
    ax.set_xlim(-1.53, 1.53); ax.set_ylim(-1.15, 1.15); ax.set_aspect("equal")
    ax.set_facecolor("#EFEFEF")
    ax.add_patch(Circle((0, 0), 1.0, fc="#B8B2A6", ec=INK, lw=1))
    # keyway at top
    ax.add_patch(Rectangle((-0.15, 0.82), 0.3, 0.25, fc="#EFEFEF", ec=INK, lw=1))
    origin = np.array([0.15, 0.82])
    for r in np.linspace(0.2, 1.35, 9):
        th = np.linspace(-np.pi, 0, 200)
        xx = origin[0] + r * 1.05 * np.cos(th)
        yy = origin[1] + r * 0.9 * np.sin(th)
        m = xx ** 2 + yy ** 2 < 0.985
        ax.plot(np.where(m, xx, np.nan), np.where(m, yy, np.nan), color="#6B6458", lw=0.8)
    # final overload zone (rough) near bottom
    th = np.linspace(-np.pi * 0.85, -np.pi * 0.15, 60)
    fz = np.c_[np.cos(th) * 0.99, np.sin(th) * 0.99]
    fz = np.vstack([fz, [[0.55, -0.55], [-0.55, -0.55]]])
    ax.add_patch(Polygon(fz, fc="#8E877B", ec="none"))
    for _ in range(80):
        p = rng.uniform(-0.8, 0.8, 2)
        if p[1] < -0.6 and p @ p < 0.95:
            ax.plot(p[0], p[1], ".", color="#5A5348", ms=2)
    ax.plot(*origin, marker="v", color=COLORS[1], ms=7)
    ax.annotate("origin at\nkeyway", xy=origin, xytext=(1.03, 0.9), fontsize=6.5, color=COLORS[1],
                arrowprops=dict(arrowstyle="-", color=COLORS[1], lw=0.7), va="center")
    ax.text(-1.45, 0.75, "beach\nmarks", fontsize=6.5, ha="left", va="center")
    ax.text(0, -0.8, "final overload", fontsize=6.5, ha="center", color="white")
    _scalebar(ax, -1.45, -1.05, 0.5, "10 mm", color=INK)
    _panel(ax, "(a) fatigue, macro")

    # (b) striations
    ax = axs[0, 1]
    ax.set_xlim(0, 4); ax.set_ylim(0, 3); ax.set_aspect("equal")
    ax.set_facecolor(SEM_BG)
    xg = np.linspace(-0.2, 4.2, 300)
    for k, y0 in enumerate(np.arange(-0.6, 3.6, 0.25)):
        yy = y0 + 0.35 * np.sin(xg * 0.9 + 0.3) + 0.06 * np.sin(xg * 4 + k)
        ax.plot(xg, yy, color="#D9D9D9", lw=1.1)
        ax.plot(xg, yy - 0.05, color="#4A4A4A", lw=0.7)
    ax.annotate("", xy=(3.6, 2.55), xytext=(3.6, 1.6), arrowprops=dict(arrowstyle="-|>", color="#FFD27F", lw=1.2))
    ax.text(3.45, 2.1, "growth", fontsize=6.5, color="#FFD27F", rotation=90, ha="right", va="center")
    ax.text(0.15, 2.75, "spacing ≈ 0.5 µm\n(one per cycle)", fontsize=6.5, color="white", va="top",
            bbox=dict(fc=SEM_BG, ec="none", pad=1))
    _scalebar(ax, 0.2, 0.2, 1.0, "2 µm")      # 0.25 units = 0.5 um -> 2 um = 1.0
    _panel(ax, "(b) fatigue striations, SEM")

    # (c) dimples
    ax = axs[0, 2]
    ax.set_xlim(0, 4); ax.set_ylim(0, 3); ax.set_aspect("equal")
    ax.set_facecolor("#5C5C5C")
    pts = rng.uniform(-0.5, 4.5, (70, 2))
    vor = Voronoi(pts)
    for i, reg_idx in enumerate(vor.point_region):
        reg = vor.regions[reg_idx]
        if -1 in reg or len(reg) == 0:
            continue
        poly = vor.vertices[reg]
        c = poly.mean(axis=0)
        poly_s = c + 0.88 * (poly - c)
        ax.add_patch(Polygon(poly, fc="#E2E2E2", ec="none"))
        ax.add_patch(Polygon(poly_s, fc="#7A7A7A", ec="none"))
        ax.add_patch(Polygon(c + 0.55 * (poly - c), fc="#4F4F4F", ec="none"))
        if rng.random() < 0.55:
            ax.add_patch(Circle(c, 0.06, fc="#F5F5F5", ec="#222222", lw=0.4))
    ax.text(0.1, 2.85, "inclusion at\ndimple bottom", fontsize=6.3, color="white", va="top",
            bbox=dict(fc="#3A3A3A", ec="none", pad=1, alpha=0.8))
    _scalebar(ax, 2.6, 0.2, 1.0, "10 µm")
    _panel(ax, "(c) ductile dimples, SEM")

    # (d) cleavage with river pattern
    ax = axs[1, 0]
    ax.set_xlim(0, 4); ax.set_ylim(0, 3); ax.set_aspect("equal")
    ax.set_facecolor("#7C7C7C")
    facets = [[[0, 0], [2.1, 0], [1.7, 1.6], [0, 1.9]], [[2.1, 0], [4, 0], [4, 1.4], [1.7, 1.6]],
              [[0, 1.9], [1.7, 1.6], [2.2, 3], [0, 3]], [[1.7, 1.6], [4, 1.4], [4, 3], [2.2, 3]]]
    shades = ["#C9C9C9", "#A9A9A9", "#B6B6B6", "#D8D8D8"]
    for f, s in zip(facets, shades):
        ax.add_patch(Polygon(f, fc=s, ec="#333333", lw=1.0))
    # river lines converging downstream (towards +x within the left-lower facet)
    for k in range(9):
        y0 = 0.1 + k * 0.2
        xs_ = np.linspace(0.05, 1.8, 50)
        yy = y0 + (0.85 - y0) * (xs_ / 1.8) ** 1.6
        ax.plot(xs_, yy, color="#555555", lw=0.7)
    for k in range(6):
        y0 = 2.0 + k * 0.17
        xs_ = np.linspace(0.05, 2.0, 40)
        yy = y0 + (2.45 - y0) * (xs_ / 2.0) ** 1.5
        ax.plot(xs_, yy, color="#666666", lw=0.6)
    ax.annotate("", xy=(3.7, 0.7), xytext=(2.5, 0.7), arrowprops=dict(arrowstyle="-|>", color="#FFD27F", lw=1.3))
    ax.text(3.1, 0.82, "propagation", fontsize=6.3, color="#3A2A00", ha="center", va="bottom")
    ax.text(3.0, 2.4, "flat facets", fontsize=6.3, ha="center", color="#222222")
    _scalebar(ax, 0.2, 0.2, 0.9, "20 µm", color="white")
    _panel(ax, "(d) cleavage, river pattern")

    # (e) intergranular
    ax = axs[1, 1]
    ax.set_xlim(0, 4); ax.set_ylim(0, 3); ax.set_aspect("equal")
    ax.set_facecolor("#555555")
    pts = rng.uniform(-0.8, 4.8, (16, 2))
    vor = Voronoi(pts)
    for reg_idx in vor.point_region:
        reg = vor.regions[reg_idx]
        if -1 in reg or len(reg) == 0:
            continue
        poly = vor.vertices[reg]
        c = poly.mean(axis=0)
        n = len(poly)
        for j in range(n):
            p1, p2 = poly[j], poly[(j + 1) % n]
            # facet shading by edge orientation: pseudo-3D grain faces
            ang = np.arctan2(p2[1] - p1[1], p2[0] - p1[0])
            g = 0.55 + 0.35 * np.cos(ang - 0.8)
            ax.add_patch(Polygon([c, p1, p2], fc=(g, g, g), ec="#2E2E2E", lw=0.3))
        ax.plot(*np.r_[poly, poly[:1]].T, color="#1E1E1E", lw=1.0)
    ax.text(0.1, 2.85, "smooth grain faces", fontsize=6.3, color="white", va="top",
            bbox=dict(fc="#333333", ec="none", pad=1, alpha=0.85))
    _scalebar(ax, 2.7, 0.2, 0.9, "20 µm")
    _panel(ax, "(e) intergranular, SEM")

    # (f) glass mirror-mist-hackle
    ax = axs[1, 2]
    ax.set_xlim(-2, 2); ax.set_ylim(-0.3, 2.7); ax.set_aspect("equal")
    ax.set_facecolor("#DCE9EE")
    ax.add_patch(Wedge((0, 0), 2.6, 0, 180, fc="#C2D6DE", ec="none"))
    for k in range(70):
        a = np.pi * (k + 0.5) / 70
        r0 = 1.05
        x0, y0 = r0 * np.cos(a), r0 * np.sin(a)
        x1, y1 = 2.6 * np.cos(a + rng.normal(0, 0.02)), 2.6 * np.sin(a + rng.normal(0, 0.02))
        ax.plot([x0, x1], [y0, y1], color="#6F8A94", lw=0.6)
    ax.add_patch(Wedge((0, 0), 1.05, 0, 180, width=0.3, fc="#B3C9D1", ec="none"))
    for _ in range(200):
        r = rng.uniform(0.76, 1.04); a = rng.uniform(0.02, np.pi - 0.02)
        ax.plot(r * np.cos(a), r * np.sin(a), ".", color="#8AA3AC", ms=1.2)
    ax.add_patch(Wedge((0, 0), 0.75, 0, 180, fc="#EEF6F9", ec="#7A9AA5", lw=0.6))
    ax.plot([-2, 2], [0, 0], color=INK, lw=1.2)
    ax.plot(0, 0.02, marker="^", color=COLORS[1], ms=6)
    ax.annotate("", xy=(0.75 * np.cos(0.6), 0.75 * np.sin(0.6)), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.9))
    ax.text(0.42, 0.12, "$r_m$", fontsize=8)
    ax.text(-0.25, 0.45, "mirror", fontsize=6.5, ha="center")
    ax.annotate("mist", xy=(-0.85, 0.32), xytext=(-1.7, 0.75), fontsize=6.5, ha="center", arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
    ax.text(-1.4, 2.2, "hackle", fontsize=6.5, ha="center")
    ax.text(0.35, -0.2, "origin (tensile surface)", fontsize=6.3, va="center", ha="left", alpha=0)
    _scalebar(ax, 0.9, 2.35, 0.75, "0.5 mm", color=INK)
    _panel(ax, "(f) glass: mirror, mist, hackle")
    save(fig, "44", "fig-44-6-fractography-features")


if __name__ == "__main__":
    tuutti()
    arrhenius_aging()
    bathtub()
    weibull_seals()
    fa_workflow()
    fractography()
