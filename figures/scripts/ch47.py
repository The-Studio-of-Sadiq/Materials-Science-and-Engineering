"""Figures for Chapter 47 — Joining: Welding, Brazing and Adhesive Bonding.

Run from the repository root:  python figures/scripts/ch47.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Ellipse, Circle, FancyArrowPatch
from scipy.interpolate import PchipInterpolator

from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK

BLUE, ORANGE, GREEN, PINK, YELLOW, SKY = COLORS[:6]
FZ = "#7A3B1E"     # fusion zone
HAZ = "#F2B880"    # heat-affected zone
STEEL = "#D9DEE4"  # base metal


def _clean(ax):
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)


# ---------------------------------------------------------------- 39.1
def _bowl(cx, w, d, n=60, top=0.0):
    """Half-ellipse weld bowl below y = top, width w and depth d."""
    t = np.linspace(0, np.pi, n)
    return np.column_stack([cx + 0.5 * w * np.cos(t), top - d * np.sin(t)])


def fig_power_density_weld_shape():
    fig = plt.figure(figsize=(6.8, 4.4))
    # --- power-density scale
    at = fig.add_axes([0.06, 0.73, 0.90, 0.24])
    bands = [("oxy-fuel", 6, 7, ORANGE, 3), ("arc (SMAW, GMAW, GTAW, SAW)", 7, 9, BLUE, 2),
             ("plasma", 9, 10, PINK, 1), ("laser", 10, 12, GREEN, 2), ("electron beam", 10, 12, "#555555", 1)]
    for lab, lo, hi, c, row in bands:
        at.add_patch(Rectangle((lo, row - 0.32), hi - lo, 0.64, fc=c, alpha=0.30, ec=c, lw=1.0))
        at.text((lo + hi) / 2, row, lab, ha="center", va="center", fontsize=8.5)
    at.axvline(10, ls="--", color=INK, lw=1.0)
    at.text(10.05, 3.15, "keyhole threshold ≈ 10$^{10}$ W/m²", fontsize=8.3, va="center")
    at.set_xlim(6, 12)
    at.set_ylim(0.5, 3.6)
    at.set_yticks([])
    at.spines["left"].set_visible(False)
    at.set_xticks(range(6, 13))
    at.set_xticklabels([f"10$^{{{k}}}$" for k in range(6, 13)])
    at.set_xlabel("power density at the work surface (W/m²)", labelpad=2)

    # --- weld cross-sections at the same scale (mm)
    ax = fig.add_axes([0.01, 0.0, 0.98, 0.62])
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-5, 140)
    ax.set_ylim(-42, 6)

    def plate(x0, x1, t):
        r = Rectangle((x0, -t), x1 - x0, t, fc=STEEL, ec="none")
        ax.add_patch(r)
        outlines.append((x0, x1, t))
        return r

    secs = []
    outlines = []
    # (1) oxy-fuel: wide shallow bowl, very wide HAZ
    r = plate(0, 42, 10)
    h = ax.add_patch(Polygon(_bowl(21, 15 + 2 * 11, 6 + 6.5), fc=HAZ, ec="none"))
    h.set_clip_path(r)
    ax.add_patch(Polygon(_bowl(21, 15, 6), fc=FZ, ec="none"))
    secs.append((21, "oxy-fuel", "D/W ≈ 0.4\nHAZ ≈ 10 mm"))
    # (2) GMAW: 10 mm wide, 4 mm deep, HAZ ~3 mm, small reinforcement
    r = plate(48, 76, 10)
    h = ax.add_patch(Polygon(_bowl(62, 10 + 6, 4 + 3), fc=HAZ, ec="none"))
    h.set_clip_path(r)
    ax.add_patch(Polygon(_bowl(62, 10, 4), fc=FZ, ec="none"))
    t = np.linspace(0, np.pi, 40)
    ax.add_patch(Polygon(np.column_stack([62 + 5 * np.cos(t), 1.0 * np.sin(t)]), fc=FZ, ec="none"))
    secs.append((62, "arc (GMAW)", "D/W ≈ 0.4\nHAZ ≈ 3 mm"))
    # (3) laser keyhole: 2 mm wide x 10 mm deep, full penetration
    r = plate(82, 102, 10)
    lw_top, lw_bot = 2.4, 1.4
    hz = 0.6
    ax.add_patch(Polygon([[92 - lw_top / 2 - hz, 0], [92 + lw_top / 2 + hz, 0], [92 + lw_bot / 2 + hz, -10],
                          [92 - lw_bot / 2 - hz, -10]], fc=HAZ, ec="none"))
    ax.add_patch(Polygon([[92 - lw_top / 2, 0], [92 + lw_top / 2, 0], [92 + lw_bot / 2, -10],
                          [92 - lw_bot / 2, -10]], fc=FZ, ec="none"))
    secs.append((92, "laser (keyhole)", "D/W ≈ 5\nnarrow HAZ"))
    # (4) electron beam, 30 mm section
    r = plate(108, 128, 30)
    hz = 0.4
    ax.add_patch(Polygon([[118 - 0.6 - hz, 0], [118 + 0.6 + hz, 0], [118 + 0.4 + hz, -30], [118 - 0.4 - hz, -30]],
                         fc=HAZ, ec="none"))
    ax.add_patch(Polygon([[118 - 0.6, 0], [118 + 0.6, 0], [118 + 0.4, -30], [118 - 0.4, -30]], fc=FZ, ec="none"))
    secs.append((118, "electron beam", "D/W ≈ 30\n(30 mm section)"))
    for x0, x1, t_ in outlines:
        ax.add_patch(Rectangle((x0, -t_), x1 - x0, t_, fc="none", ec=INK, lw=0.9, zorder=5))
    for cx, name, note in secs:
        ax.text(cx, 3.2, name, ha="center", va="bottom", fontsize=9, fontweight="bold")
    for cx, name, note in secs[:3]:
        ax.text(cx, -12, note, ha="center", va="top", fontsize=8.5)
    ax.text(129.5, -15, secs[3][2], ha="left", va="center", fontsize=8.5)
    # plate-thickness dimension and legend
    ax.annotate("", xy=(-1.2, 0), xytext=(-1.2, -10), arrowprops=dict(arrowstyle="<|-|>", lw=0.8, color=INK,
                                                                       mutation_scale=7))
    ax.text(-1.9, -5, "10 mm", rotation=90, fontsize=7.8, va="center", ha="right")
    ax.add_patch(Rectangle((2, -30), 4, 2.6, fc=FZ, ec="none"))
    ax.text(7, -28.7, "fusion zone", fontsize=8.5, va="center")
    ax.add_patch(Rectangle((2, -35), 4, 2.6, fc=HAZ, ec="none"))
    ax.text(7, -33.7, "heat-affected zone", fontsize=8.5, va="center")
    ax.add_patch(Rectangle((2, -40), 4, 2.6, fc=STEEL, ec=INK, lw=0.6))
    ax.text(7, -38.7, "base metal (steel); all sections to the same scale", fontsize=8.5, va="center")
    save(fig, "47", "fig-47-1-power-density-weld-shape")


# ---------------------------------------------------------------- 39.2
def t85(H, T0, F3=1.0):
    return (6700 - 5 * T0) * H * (1 / (500 - T0) - 1 / (800 - T0)) * F3


def fig_t85_heat_input():
    fig, ax = new_fig(6.4, 4.2)
    H = np.linspace(0.5, 3.0, 200)
    ax.axhspan(0, 5, color="#F8D9D2", zorder=0)
    ax.axhspan(25, 40, color="#DDEBF7", zorder=0)
    ax.text(2.97, 2.5, "martensitic HAZ, cold-cracking risk (typical C–Mn steel)", fontsize=8.3,
            va="center", ha="right", color="#9A3324")
    ax.text(0.55, 37.5, "coarse-grained HAZ, toughness loss in TMCP steels", fontsize=8.3, va="center",
            color="#1F4E79")
    for T0, c in [(20, BLUE), (100, ORANGE), (150, GREEN)]:
        ax.plot(H, t85(H, T0), color=c, lw=2.0, label=f"butt weld, $T_0$ = {T0} °C")
        ax.plot(1.12, t85(1.12, T0), "o", color=c, ms=5, zorder=5)
    ax.plot(H, t85(H, 20, 0.67), color=BLUE, lw=1.6, ls="--", label="fillet weld ($F_3$ = 0.67), $T_0$ = 20 °C")
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 0.74), fontsize=8.3)
    ax.axvline(1.12, color="#888888", lw=0.8, ls=":")
    ax.annotate("worked example, 1.12 kJ/mm:\n5.9, 7.4 and 8.8 s", xy=(1.12, 8.8), xytext=(1.25, 17),
                fontsize=8.3, arrowprops=dict(arrowstyle="-", color="#555555", lw=0.7))
    ax.set_xlim(0.5, 3.0)
    ax.set_ylim(0, 40)
    ax.set_xlabel("heat input $H$ (kJ/mm)")
    ax.set_ylabel("cooling time $t_{8/5}$ (s)")
    ax.set_title("butt weld, thick plate (3-D heat flow), $F_3$ = 1 unless noted", fontsize=9, loc="left")
    # HAZ hardness trend (schematic): 400 HV at 3 s to 200 HV at 30 s, linear in log t
    def t2hv(t):
        return 400 - 200 * np.log10(np.clip(t, 1e-3, None) / 3.0)

    def hv2t(hv):
        return 3.0 * 10 ** ((400 - hv) / 200)
    sec = ax.secondary_yaxis("right", functions=(t2hv, hv2t))
    sec.set_yticks([400, 350, 300, 250, 200])
    sec.set_ylabel("approx. CGHAZ hardness (HV, schematic)")
    ax.spines["right"].set_visible(True)
    save(fig, "47", "fig-47-2-t85-heat-input")


# ---------------------------------------------------------------- 39.3
def _a3(c):
    # A3 of Fe-C: 912 at 0, 860 at 0.15, 727 at 0.77 (quadratic through these)
    a, b = np.polyfit([0, 0.15, 0.77], [912, 860, 727], 2)[:2]
    return np.polyval(np.polyfit([0, 0.15, 0.77], [912, 860, 727], 2), c)


def fig_haz_regions_fe_c():
    T0 = 20.0
    Tf = 1495.0                                   # peak temperature at the fusion line
    a = (1 / (500 - T0) - 1 / (Tf - T0)) / 6.0    # 2-D peak-temperature law: 500 °C at 6 mm

    def Tp(y):
        return T0 + 1 / (1 / (Tf - T0) + a * y)

    def y_of(T):
        return (1 / (T - T0) - 1 / (Tf - T0)) / a
    A1, A3 = 727.0, 860.0
    zones = [("partially melted", 1495, 1525, "#B5651D"), ("coarse-grained HAZ", 1100, 1495, "#E8833A"),
             ("fine-grained HAZ", A3, 1100, "#F3B26B"), ("intercritical HAZ", A1, A3, "#F7D9A8"),
             ("subcritical HAZ (tempered)", 600, A1, "#FBEBD3")]

    fig = plt.figure(figsize=(6.8, 5.6))
    ad = fig.add_axes([0.09, 0.40, 0.38, 0.57])
    # --- Fe-Fe3C steel corner
    c = np.linspace(0, 1.0, 200)
    ad.plot([0, 0.53], [1538, 1495], color=INK, lw=1.3)                     # liquidus (delta)
    ad.plot([0.53, 1.0], [1495, 1495 - (1495 - 1148) * 0.47 / 3.77], color=INK, lw=1.3)  # liquidus (gamma)
    ad.plot([0, 0.09], [1538, 1495], color=INK, lw=1.0)                     # delta solidus
    ad.plot([0, 0.09], [1394, 1495], color=INK, lw=1.0)
    ad.plot([0, 0.17], [1394, 1495], color=INK, lw=1.0)
    ad.plot([0.09, 0.53], [1495, 1495], color=INK, lw=1.0)                  # peritectic
    ad.plot([0.17, 1.0], [1495, 1495 - (1495 - 1148) * 0.83 / 1.94], color=INK, lw=1.3)  # gamma solidus
    cc = np.linspace(0, 0.77, 100)
    ad.plot(cc, _a3(cc), color=INK, lw=1.3)
    ce = np.linspace(0.77, 1.0, 30)
    ad.plot(ce, 727 + (800 - 727) * ((ce - 0.77) / 0.23) ** 1.0, color=INK, lw=1.3)   # Acm
    ad.plot([0.022, 1.0], [727, 727], color=INK, lw=1.3)
    ad.plot([0.022, 0.0], [727, 912], color=INK, lw=0.8)
    ad.axvline(0.15, color=BLUE, lw=1.4)
    ad.text(0.16, 625, "0.15 % C", color=BLUE, fontsize=8.5)
    for (x, y, s) in [(0.9, 1540, "L"), (0.55, 1200, "γ (austenite)"),
                      (0.30, 1520, "L + δ"), (0.72, 1450, "L + γ"), (0.085, 770, "α+γ"),
                      (0.55, 650, "α + Fe$_3$C"), (0.91, 752, "γ+Fe$_3$C")]:
        ad.text(x, y, s, fontsize=7.8 if len(s) < 5 else 8.3, ha="center", va="center")
    ad.text(0.74, 718, "$A_1$ 727 °C", fontsize=8, ha="right", va="top")
    ad.annotate("$A_3$ ≈ 860 °C", xy=(0.15, 860), xytext=(0.30, 905), fontsize=8,
                arrowprops=dict(arrowstyle="-", color="#555555", lw=0.6))
    ad.annotate("liquidus", xy=(0.35, 1510), xytext=(0.62, 1585), fontsize=7.8,
                arrowprops=dict(arrowstyle="-", color="#555555", lw=0.6))
    ad.annotate("solidus", xy=(0.45, 1430), xytext=(0.62, 1385), fontsize=7.8,
                arrowprops=dict(arrowstyle="-", color="#555555", lw=0.6))
    ad.set_xlim(0, 1.0)
    ad.set_ylim(600, 1600)
    ad.set_xlabel("carbon (wt%)")
    ad.set_ylabel("temperature / peak temperature (°C)")
    ad.set_title("Fe–Fe$_3$C, steel corner", fontsize=9.5)

    # --- right panel: peak-temperature levels and the half weld section
    aw = fig.add_axes([0.49, 0.40, 0.50, 0.57], sharey=ad)
    aw.axis("off")
    for name, lo, hi, col in zones:
        aw.axhspan(lo, min(hi, 1525), xmin=0.0, xmax=0.36, color=col, ec="none")
        ad.axhspan(lo, min(hi, 1525), color=col, alpha=0.22, zorder=0)
        aw.text(0.02, (lo + min(hi, 1525)) / 2, name, fontsize=8, va="center", transform=aw.get_yaxis_transform())
        aw.axhline(lo, xmin=0, xmax=0.36, color="#888888", lw=0.6, ls="--")
    aw.text(0.02, 1560, "molten (fusion zone)", fontsize=8, va="center", transform=aw.get_yaxis_transform())
    for T in [A1, A3, 1100, 1495]:
        ad.axhline(T, color="#888888", lw=0.6, ls="--", zorder=0.5)
    # half weld section drawn in an inset with mm coordinates
    sw = fig.add_axes([0.70, 0.43, 0.29, 0.50])
    sw.set_aspect("equal")
    sw.axis("off")
    sw.set_xlim(-0.3, 9.5)
    sw.set_ylim(-9.5, 1.6)
    sw.set_title("half cross-section", fontsize=9, pad=2)
    plate = Rectangle((0, -9), 9.3, 9, fc=STEEL, ec=INK, lw=0.9)
    sw.add_patch(plate)
    W0, D0 = 4.0, 4.5   # fusion-zone half width / depth
    def ring(T):
        dy = y_of(T) if T < Tf else 0.0
        t = np.linspace(0, np.pi / 2, 50)
        return np.vstack([[0, 0], np.column_stack([(W0 + dy) * np.cos(t), -(D0 + dy * 0.9) * np.sin(t)])])
    for name, lo, hi, col in zones[::-1]:
        p = sw.add_patch(Polygon(ring(lo), fc=col, ec="none"))
        p.set_clip_path(plate)
    pm = sw.add_patch(Polygon(ring(Tf - 1), fc="#B5651D", ec="none"))
    t = np.linspace(0, np.pi / 2, 50)
    fz = np.vstack([[0, 0], np.column_stack([W0 * np.cos(t), -D0 * np.sin(t)])])
    sw.add_patch(Polygon(fz, fc="#8C4A2F", ec=INK, lw=0.8))
    # columnar grains growing epitaxially from the fusion boundary toward the centreline
    for th in np.linspace(0.08, np.pi / 2 - 0.05, 9):
        x0, y0 = W0 * np.cos(th), -D0 * np.sin(th)
        xs = np.linspace(x0, x0 * 0.12, 8)
        ys = y0 * np.linspace(1, 0.35, 8) ** 0.8
        sw.plot(xs, ys, color="#E9C7B0", lw=0.7)
    sw.plot([0, 0], [0, -9], color=INK, lw=0.8, ls="-.")
    sw.text(0.1, 0.25, "weld ℄", fontsize=7.5, va="bottom")
    sw.text(2.0, -2.0, "FZ", color="white", fontsize=8, ha="center")
    sw.text(8.9, -8.6, "base\nmetal", fontsize=7.5, ha="right", va="bottom")

    # --- bottom: peak temperature vs distance from fusion line
    ab = fig.add_axes([0.09, 0.07, 0.88, 0.24])
    y = np.linspace(0, 6, 300)
    for name, lo, hi, col in zones:
        ylo = y_of(min(hi, Tf)) if hi < Tf else 0
        yhi = y_of(lo) if lo > 500 else 6
        ab.axvspan(ylo, min(yhi, 6), color=col, alpha=0.8, ec="none")
    ab.axvspan(y_of(600), 6, color="white")
    ab.plot(y, Tp(y), color=INK, lw=2.0)
    for T in [A1, A3, 1100]:
        ab.axhline(T, color="#888888", lw=0.6, ls="--")
    labs = [("CG", 0.5), ("FG", (y_of(1100) + y_of(A3)) / 2), ("IC", (y_of(A3) + y_of(A1)) / 2),
            ("SC", (y_of(A1) + y_of(600)) / 2)]
    for s, xpos in labs:
        ab.text(xpos, 1420, s, ha="center", fontsize=8.5)
    ab.text(5.9, 1400, "unaffected\n(< 600 °C)", ha="right", fontsize=8, va="top")
    ab.set_xlim(0, 6)
    ab.set_ylim(450, 1550)
    ab.set_xlabel("distance from fusion line (mm)")
    ab.set_ylabel("peak temp. (°C)")
    save(fig, "47", "fig-47-3-haz-regions-fe-c")


# ---------------------------------------------------------------- 39.4
def fig_graville_diagram():
    fig, ax = new_fig(6.4, 4.4)
    ce = np.linspace(0.2, 0.9, 200)
    # boundary I/II at C = 0.10; boundary II/III sloping from (0.47, 0.10) to (0.37, 0.50)
    x_top, x_bot = 0.37, 0.47
    ax.fill_between([0.2, 0.6], 0, 0.10, color="#DDEFD9")
    ax.fill_between([0.6, 0.9], 0, 0.10, color="#F8D9D2")
    ax.fill([0.2, x_bot, x_top, 0.2], [0.10, 0.10, 0.5, 0.5], color="#FFF0C4")
    ax.fill([x_bot, 0.9, 0.9, x_top], [0.10, 0.10, 0.5, 0.5], color="#F8D9D2")
    ax.plot([0.2, 0.6], [0.10, 0.10], color=INK, lw=1.2)
    ax.plot([x_bot, x_top], [0.10, 0.5], color=INK, lw=1.2)
    ax.plot([0.6, 0.6], [0, 0.10], color=INK, lw=1.2)
    ax.text(0.30, 0.04, "Zone I\neasily weldable, low risk", fontsize=8.8, ha="center", va="center")
    ax.text(0.27, 0.36, "Zone II\ncontrol cooling rate /\nheat input", fontsize=8.8, ha="center", va="center")
    ax.text(0.78, 0.30, "Zone III\npreheat, low hydrogen,\nPWHT required", fontsize=8.8, ha="center", va="center")
    pts = [("X70 TMCP", 0.38, 0.08, (-62, -4)), ("S355", 0.44, 0.18, (-36, -2)), ("S690 Q&T", 0.55, 0.16, (6, -12)),
           ("AISI 4140", 0.78, 0.40, (7, 2)), ("1045", 0.60, 0.45, (7, 2))]
    for lab, x, y, off in pts:
        ax.plot(x, y, "o", color=INK, ms=5.5, zorder=5)
        ax.annotate(lab, xy=(x, y), xytext=off, textcoords="offset points", fontsize=8.5)
    ax.set_xlim(0.2, 0.9)
    ax.set_ylim(0, 0.5)
    ax.set_xlabel("carbon equivalent CE$_{\\mathrm{IIW}}$")
    ax.set_ylabel("carbon (wt%)")
    save(fig, "47", "fig-47-4-graville-diagram")


# ---------------------------------------------------------------- 39.5
def fig_friction_stir_zones():
    fig = plt.figure(figsize=(6.8, 5.6))
    # --- upper left: oblique sketch of the tool and plates
    a3 = fig.add_axes([0.0, 0.55, 0.46, 0.45])
    a3.set_aspect("equal")
    a3.axis("off")
    a3.set_xlim(-30, 80)
    a3.set_ylim(-26, 36)
    k = np.array([0.5, 0.32])     # oblique projection of the y (across) direction

    def P(x, y, z):
        return np.array([x + k[0] * y, z + k[1] * y])
    L, Wp, tp = 60, 24, 6
    for y0, y1, col in [(-Wp, 0, "#DCE3EA"), (0, Wp, "#E9EEF3")]:
        top = [P(0, y0, 0), P(L, y0, 0), P(L, y1, 0), P(0, y1, 0)]
        a3.add_patch(Polygon(top, fc=col, ec=INK, lw=0.8))
        if y0 == -Wp:
            front = [P(0, y0, 0), P(L, y0, 0), P(L, y0, -tp), P(0, y0, -tp)]
            a3.add_patch(Polygon(front, fc="#B9C3CE", ec=INK, lw=0.8))
        side = [P(L, y0, 0), P(L, y1, 0), P(L, y1, -tp), P(L, y0, -tp)]
        a3.add_patch(Polygon(side, fc="#C9D1DA", ec=INK, lw=0.8))
    # weld track behind the tool with onion rings
    xt = 40
    tr = [P(2, -4.5, 0), P(xt, -4.5, 0), P(xt, 4.5, 0), P(2, 4.5, 0)]
    a3.add_patch(Polygon(tr, fc="#C7B8A6", ec="none"))
    for xx in np.arange(4, xt - 9, 2.4):
        t = np.linspace(-np.pi / 2, np.pi / 2, 30)
        pts = np.array([P(xx + 2.5 * np.cos(tt), 4.5 * np.sin(tt), 0) for tt in t])
        a3.plot(pts[:, 0], pts[:, 1], color="#7D6A55", lw=0.6)
    # pin inside the plate (hidden, dashed)
    pin = np.array([P(xt - 3, 0, 0), P(xt - 3, 0, -5.5), P(xt + 3, 0, -5.5), P(xt + 3, 0, 0)])
    a3.plot(pin[:, 0], pin[:, 1], color=INK, lw=0.8, ls="--")
    for zz in np.arange(-5, 0, 1.0):
        p0, p1 = P(xt - 3, 0, zz), P(xt + 3, 0, zz + 0.5)
        a3.plot([p0[0], p1[0]], [p0[1], p1[1]], color="#777777", lw=0.5, ls="--")

    def cyl(xc, r, z0, z1, fc):
        t = np.linspace(0, 2 * np.pi, 80)
        bot = np.array([P(xc + r * np.cos(tt), r * np.sin(tt), z0) for tt in t])
        topc = np.array([P(xc + r * np.cos(tt), r * np.sin(tt), z1) for tt in t])
        a3.add_patch(Polygon(bot, fc=fc, ec=INK, lw=0.7))
        lft, rgt = P(xc - r, 0, z0), P(xc + r, 0, z0)
        body = np.array([lft, P(xc - r, 0, z1), P(xc + r, 0, z1), rgt])
        a3.add_patch(Polygon(body, fc=fc, ec="none"))
        a3.plot([lft[0], lft[0]], [lft[1], lft[1] + z1 - z0], color=INK, lw=0.7)
        a3.plot([rgt[0], rgt[0]], [rgt[1], rgt[1] + z1 - z0], color=INK, lw=0.7)
        a3.add_patch(Polygon(topc, fc="#E5E5E5", ec=INK, lw=0.7))
    cyl(xt, 9, 0, 12, "#A9B2BB")
    cyl(xt, 5, 12, 26, "#8E98A2")
    # rotation arrow and travel arrow
    t = np.linspace(-0.2 * np.pi, 0.95 * np.pi, 40)
    rot = np.array([P(xt + 8 * np.cos(tt), 8 * np.sin(tt), 20) for tt in t])
    a3.plot(rot[:, 0], rot[:, 1], color=ORANGE, lw=1.3)
    a3.annotate("", xy=rot[-1], xytext=rot[-4], arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.3))
    a3.text(xt + 10, 27, "rotation", color=ORANGE, fontsize=8)
    t0, t1 = P(xt + 11, 0, 0.5), P(L + 6, 0, 0.5)
    a3.annotate("", xy=t1, xytext=t0, arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.6))
    a3.text((t0[0] + t1[0]) / 2, t0[1] + 2, "travel", color=BLUE, fontsize=8, ha="center", va="bottom")
    a3.text(*P(-1, -Wp + 4, 0), "AS", fontsize=9, fontweight="bold", va="center", ha="right")
    a3.text(*P(-1, Wp - 4, 0), "RS", fontsize=9, fontweight="bold", va="center", ha="right")
    a3.text(*P(14, -9.5, 0.4), "onion rings", fontsize=7.5, color="#5A4A38", ha="center", va="top")
    a3.annotate("shoulder Ø18 mm", xy=P(xt - 9, 0, 7), xytext=(5, 20), fontsize=7.8, ha="center",
                arrowprops=dict(arrowstyle="-", color="#555555", lw=0.6))
    a3.annotate("threaded pin Ø6 mm\n(inside the joint)", xy=P(xt + 2, 0, -4), xytext=(48, -21), fontsize=7.6,
                ha="center", va="center", arrowprops=dict(arrowstyle="-", color="#555555", lw=0.6))
    a3.text(-2, -21, "two clamped\n6 mm plates", fontsize=7.6, ha="center", va="center")

    # --- upper right: transverse section, same x-scale as the hardness plot
    asec = fig.add_axes([0.49, 0.62, 0.50, 0.38])
    asec.set_xlim(-30, 30)
    asec.set_ylim(-7.5, 6.5)
    asec.set_aspect("equal")
    asec.axis("off")
    asec.add_patch(Rectangle((-30, -6), 60, 6, fc="#E6EBF0", ec=INK, lw=0.8))

    def basin(top, bot, ymin=-5.6):
        return np.array([[-top, 0], [top, 0], [bot, ymin], [-bot, ymin]])
    asec.add_patch(Polygon(basin(17, 13, -6), fc="#F6DDBA", ec="none"))      # HAZ
    asec.add_patch(Polygon(basin(10.2, 5.8, -5.8), fc="#E9B77E", ec="none"))  # TMAZ
    nug = basin(8.8, 3.6, -5.6)
    asec.add_patch(Polygon(nug, fc="#C98D58", ec="none"))                    # stir zone
    for r in [0.9, 0.7, 0.5, 0.3]:
        asec.add_patch(Ellipse((0.8, -3.3), 9 * r, 4.2 * r, fc="none", ec="#7A4E28", lw=0.5))
    # bent elongated grains in the TMAZ
    for s in [-1, 1]:
        for yy in np.linspace(-5.2, -0.6, 6):
            xx = s * (9.6 + 0.1 * yy)
            asec.plot([xx, xx - s * 1.2], [yy, yy + 0.5], color="#7A4E28", lw=0.5)
    asec.add_patch(Rectangle((-30, -6), 60, 6, fc="none", ec=INK, lw=0.8))
    for x, yv, s in [(0, 0.5, "SZ"), (10, 0.5, "TMAZ"), (-10, 0.5, "TMAZ"), (15.5, 2.6, "HAZ"),
                     (-15.5, 2.6, "HAZ"), (24, 0.5, "BM"), (-24, 0.5, "BM")]:
        asec.text(x, yv, s, fontsize=7.8, ha="center", va="bottom")
        if yv > 1:
            asec.plot([x, x * 0.92], [yv, 0.2], color="#777777", lw=0.5)
    asec.text(0, -6.5, "stir zone: recrystallized 2–10 µm grains;  TMAZ: bent, elongated grains",
              fontsize=7.5, ha="center", va="top")
    asec.text(29, 4.6, "AS →", fontsize=8.5, ha="right", fontweight="bold")
    asec.text(-29, 4.6, "← RS", fontsize=8.5, ha="left", fontweight="bold")

    # --- lower: hardness profile
    ah = fig.add_axes([0.10, 0.08, 0.86, 0.45])
    xp = np.array([0, 3, 5, 7, 8.5, 10, 11.5, 13, 16, 20, 25, 30])
    hp = np.array([76, 75, 73, 69, 66, 65, 67, 73, 86, 98, 104, 105])
    f = PchipInterpolator(xp, hp)
    x = np.linspace(-30, 30, 601)
    H_fsw = f(np.abs(x)) - 1.5 * np.exp(-((x - 10) / 2.5) ** 2)   # slightly deeper on the AS
    xg = np.array([0, 3.5, 5, 6, 8, 11, 14, 18, 22, 26, 30])
    hg = np.array([55, 55, 60, 68, 64, 57, 55, 62, 80, 96, 103])
    g = PchipInterpolator(xg, hg)
    H_gm = g(np.abs(x))
    ah.axhline(105, color="#999999", lw=0.8, ls=":")
    ah.plot(x, H_fsw, color=BLUE, lw=2.0, label="friction stir weld, 6061-T6")
    ah.plot(x, H_gm, color=ORANGE, lw=1.8, ls="--", label="GMAW, 4043 filler, same alloy")
    ah.text(-29.5, 106, "base metal ≈ 105 HV", fontsize=8, va="bottom")
    ah.annotate("HAZ minimum ≈ 65 HV", xy=(10, 64), xytext=(15, 50), fontsize=8, color=BLUE,
                arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.7))
    ah.annotate("stir zone 70–80 HV", xy=(0, 76), xytext=(-4, 92), fontsize=8, color=BLUE, ha="center",
                arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.7))
    ah.annotate("fusion zone ≈ 55 HV", xy=(-1, 55), xytext=(0, 44), fontsize=8, color=ORANGE, ha="center",
                arrowprops=dict(arrowstyle="-", color=ORANGE, lw=0.7))
    ah.annotate("GMAW HAZ min ≈ 55 HV", xy=(-14, 55), xytext=(-29.5, 44), fontsize=8,
                color=ORANGE, arrowprops=dict(arrowstyle="-", color=ORANGE, lw=0.7))
    ah.set_xlim(-30, 30)
    ah.set_ylim(40, 125)
    ah.set_xlabel("distance from weld centre (mm)    (RS ←  → AS)")
    ah.set_ylabel("hardness (HV)")
    ah.legend(loc="upper center", fontsize=8, ncol=2)
    save(fig, "47", "fig-47-5-friction-stir-zones")


# ---------------------------------------------------------------- 39.6
def fig_lap_joint_shear_lag():
    E, t, G, eta, b, tau = 70e3, 2.0, 1.0e3, 0.2, 25.0, 30.0   # MPa, mm
    w = np.sqrt(2 * G / (E * t * eta))                          # 1/mm
    fig = plt.figure(figsize=(6.8, 5.2))
    a1 = fig.add_axes([0.08, 0.40, 0.56, 0.54])
    xi = np.linspace(-0.5, 0.5, 400)
    for L, c in [(12.5, GREEN), (25.0, BLUE), (50.0, ORANGE)]:
        k = w * L / 2
        r = k * np.cosh(w * L * xi) / np.sinh(k)
        a1.plot(xi, r, color=c, lw=2.0,
                label=f"L = {L:g} mm, $\\omega L/2$ = {k:.2f}, peak {k / np.tanh(k):.2f}")
    a1.legend(loc="upper center", fontsize=8)
    a1.axhline(1, ls="--", color="#666666", lw=1.0)
    a1.text(-0.15, 1.25, "uniform (rigid adherends)", fontsize=8, color="#555555")
    a1.set_xlim(-0.5, 0.5)
    a1.set_ylim(0, 7)
    a1.set_xlabel("position along overlap $x/L$")
    a1.set_ylabel("$\\tau / \\tau_{\\mathrm{avg}}$")
    a1.set_title("Volkersen: Al 2 mm, epoxy $G$ = 1 GPa, 0.2 mm;  $1/\\omega$ = 3.7 mm", fontsize=8.5, loc="left")

    a2 = fig.add_axes([0.80, 0.40, 0.18, 0.50])
    Lr = np.linspace(5, 60, 200)
    F = tau * b * (2 / w) * np.tanh(w * Lr / 2) / 1e3
    a2.plot(Lr, F, color=BLUE, lw=2.0)
    a2.plot(Lr, tau * b * Lr / 1e3, color="#666666", ls="--", lw=1.2)
    for L in [12.5, 25, 50]:
        a2.plot(L, tau * b * (2 / w) * np.tanh(w * L / 2) / 1e3, "o", color=BLUE, ms=4)
    a2.set_xlim(5, 60)
    a2.set_ylim(0, 20)
    a2.set_xlabel("overlap $L$ (mm)")
    a2.set_ylabel("elastic-limit load (kN)")
    a2.text(58, 6.3, "Volkersen\n→ 5.6 kN", fontsize=7.8, color=BLUE, ha="right", va="bottom")
    a2.text(24, 12.5, "average\nstress", fontsize=7.8, color="#555555", ha="left")
    a2.set_title("$\\tau_{\\mathrm{allow}}$ = 30 MPa,\nwidth 25 mm", fontsize=8.5)

    # --- bottom strip: joint configurations
    ab = fig.add_axes([0.01, 0.0, 0.98, 0.29])
    ab.set_aspect("equal")
    ab.axis("off")
    ab.set_xlim(0, 100)
    ab.set_ylim(-3.5, 15.5)
    ad, gl = "#B8C4D0", "#E39B3B"

    def poly(pts, fc=ad):
        ab.add_patch(Polygon(pts, fc=fc, ec=INK, lw=0.6))
    names = ["single lap", "tapered lap", "double lap", "stepped lap", "scarf"]
    xs = [1, 21, 41, 61, 81]
    y = 3.6
    # single lap
    x = xs[0]
    poly([[x, y], [x + 11, y], [x + 11, y + 1.2], [x, y + 1.2]])
    poly([[x + 5, y + 1.2], [x + 11, y + 1.2], [x + 11, y + 1.55], [x + 5, y + 1.55]], gl)
    poly([[x + 5, y + 1.55], [x + 16, y + 1.55], [x + 16, y + 2.75], [x + 5, y + 2.75]])
    # tapered lap (adherend ends thinned on their outer faces)
    x = xs[1]
    poly([[x, y], [x + 5, y], [x + 11, y + 0.9], [x + 11, y + 1.2], [x, y + 1.2]])
    poly([[x + 5, y + 1.2], [x + 11, y + 1.2], [x + 11, y + 1.55], [x + 5, y + 1.55]], gl)
    poly([[x + 5, y + 1.55], [x + 16, y + 1.55], [x + 16, y + 2.75], [x + 11, y + 2.75], [x + 5, y + 1.85]])
    # double lap
    x = xs[2]
    poly([[x + 5, y], [x + 16, y], [x + 16, y + 1.2], [x + 5, y + 1.2]])
    poly([[x + 5, y + 1.2], [x + 10, y + 1.2], [x + 10, y + 1.55], [x + 5, y + 1.55]], gl)
    poly([[x, y + 1.55], [x + 10, y + 1.55], [x + 10, y + 2.75], [x, y + 2.75]])
    poly([[x + 5, y + 2.75], [x + 10, y + 2.75], [x + 10, y + 3.1], [x + 5, y + 3.1]], gl)
    poly([[x + 5, y + 3.1], [x + 16, y + 3.1], [x + 16, y + 4.3], [x + 5, y + 4.3]])
    # stepped lap
    x = xs[3]
    poly([[x, y], [x + 11, y], [x + 11, y + 0.8], [x + 9, y + 0.8], [x + 9, y + 1.6], [x + 7, y + 1.6],
          [x + 7, y + 2.4], [x, y + 2.4]])
    poly([[x + 7, y + 1.6], [x + 9, y + 1.6], [x + 9, y + 0.8], [x + 11, y + 0.8], [x + 11, y], [x + 18, y],
          [x + 18, y + 2.4], [x + 7, y + 2.4]])
    ab.plot([x + 7, x + 7, x + 9, x + 9, x + 11, x + 11], [y + 2.4, y + 1.6, y + 1.6, y + 0.8, y + 0.8, y],
            color=gl, lw=2.0)
    # scarf
    x = xs[4]
    poly([[x, y], [x + 11, y], [x + 7, y + 2.4], [x, y + 2.4]])
    poly([[x + 11, y], [x + 18, y], [x + 18, y + 2.4], [x + 7, y + 2.4]])
    ab.plot([x + 11, x + 7], [y, y + 2.4], color=gl, lw=2.0)
    for xx, n in zip(xs, names):
        ab.text(xx + 8.5, y - 0.5, n, ha="center", va="top", fontsize=8.3)
    ab.add_patch(FancyArrowPatch((2, -0.9), (98, -0.9), arrowstyle="-|>", mutation_scale=12, color=GREEN, lw=1.6))
    ab.text(50, -1.5, "increasing joint efficiency (more gradual load transfer, less peel)", ha="center", va="top",
            fontsize=8.3, color=GREEN)
    # peel icon (to avoid)
    xi_, yi_ = 2, 9.6
    poly([[xi_, yi_], [xi_ + 12, yi_], [xi_ + 12, yi_ + 0.9], [xi_, yi_ + 0.9]])
    poly([[xi_, yi_ + 0.9], [xi_ + 6, yi_ + 0.9], [xi_ + 6, yi_ + 1.2], [xi_, yi_ + 1.2]], gl)
    poly([[xi_, yi_ + 1.2], [xi_ + 6, yi_ + 1.2], [xi_ + 10, yi_ + 3.0], [xi_ + 9.6, yi_ + 3.8], [xi_ + 5.7, yi_ + 2.1],
          [xi_, yi_ + 2.1]])
    ab.annotate("", xy=(xi_ + 10.6, yi_ + 5.6), xytext=(xi_ + 9.8, yi_ + 3.5),
                arrowprops=dict(arrowstyle="-|>", color=PINK, lw=1.4))
    ab.text(xi_ + 14, yi_ + 1.8, "avoid peel and cleavage: load concentrated on a line at the bond edge",
            fontsize=8.3, color=PINK, va="center")
    save(fig, "47", "fig-47-6-lap-joint-shear-lag")


if __name__ == "__main__":
    fig_power_density_weld_shape()
    fig_t85_heat_input()
    fig_haz_regions_fe_c()
    fig_graville_diagram()
    fig_friction_stir_zones()
    fig_lap_joint_shear_lag()
