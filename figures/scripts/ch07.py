"""Figures for Chapter 7 — Phase Diagrams.

Run from the repository root:  python figures/scripts/ch07.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle, RegularPolygon
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq

R = 8.314
RNG = np.random.default_rng(11)
FIELD = ["#EAF2FA", "#FBEDE3", "#E6F4EE", "#F6EAF2", "#FDF3DC", "#EEEEEE"]


# ---------------------------------------------------------------- Figure 7.1
def _water(ax):
    Tc, pc = 647.096, 22.064e6
    a = [-7.85951783, 1.84408259, -11.7866497, 22.6807411, -15.9618719, 1.80122502]
    T = np.linspace(273.16, Tc, 400)
    tau = 1 - T / Tc
    lnp = (Tc / T) * (a[0] * tau + a[1] * tau**1.5 + a[2] * tau**3 + a[3] * tau**3.5
                      + a[4] * tau**4 + a[5] * tau**7.5)
    p_vap = pc * np.exp(lnp)
    Tt, pt = 273.16, 611.657
    Ts = np.linspace(223.15, Tt, 200)
    th = Ts / Tt
    p_sub = pt * np.exp((-21.2144006 * th**0.00333333 + 27.3203819 * th**1.20666667
                         - 6.1059813 * th**1.70333333) / th)
    # ice Ih melting (IAPWS 2011), 273.16 K -> 251.165 K / 208.566 MPa
    Tm = np.linspace(251.165, Tt, 200)
    th = Tm / Tt
    p_m = pt * (1 + 0.119539337e7 * (1 - th**3) + 0.808183159e5 * (1 - th**25.75)
                + 0.33382686e4 * (1 - th**103.75))
    # high-pressure ices III, V, VI melting curves (IAPWS)
    T3 = np.linspace(251.165, 256.164, 50); p3 = 208.566e6 * (1 - 0.299948 * (1 - (T3 / 251.165)**60))
    T5 = np.linspace(256.164, 273.31, 50); p5 = 350.1e6 * (1 - 1.18721 * (1 - (T5 / 256.164)**8))
    T6 = np.linspace(273.31, 300.5, 50); p6 = 632.4e6 * (1 - 1.07476 * (1 - (T6 / 273.31)**4.6))
    C = lambda t: t - 273.15
    ax.set_yscale("log")
    ax.plot(C(T), p_vap, color=COLORS[0])
    ax.plot(C(Ts), p_sub, color=COLORS[0])
    ax.plot(C(Tm), p_m, color=COLORS[1])
    hpT = np.r_[T3, T5, T6]; hpp = np.r_[p3, p5, p6]
    ax.plot(C(hpT), hpp, color=COLORS[1], lw=1.2)
    ax.fill_betweenx(np.r_[hpp, 1e9], -60, C(np.r_[hpT, hpT[-1]]), color="0.88", lw=0)
    ax.annotate("ice III, V, VI", xy=(-38, 6e8), xytext=(40, 4e8), fontsize=7, color="0.3", va="center",
                arrowprops=dict(arrowstyle="-", color="0.5", lw=0.7))
    ax.plot(C(Tt), pt, "o", color=INK, ms=4)
    ax.plot(C(Tc), pc, "o", color=INK, ms=4)
    ax.annotate("triple point\n0.01 °C, 611.657 Pa", xy=(0.01, pt), xytext=(40, 25),
                fontsize=7, va="center", arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
    ax.annotate("critical point\n373.9 °C, 22.06 MPa", xy=(C(Tc), pc), xytext=(300, 1.5e3),
                fontsize=7, ha="center", arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
    ax.annotate("melting line\n$dp/dT\\approx-13.5$ MPa/K", xy=(-1, 1.0e6), xytext=(15, 7e6), va="center",
                fontsize=7, color=COLORS[1], arrowprops=dict(arrowstyle="-", color=COLORS[1], lw=0.7))
    ax.text(-38, 3e4, "ice Ih", fontsize=9)
    ax.text(200, 4e7, "liquid", fontsize=9)
    ax.text(270, 20, "vapour", fontsize=9)
    ax.set_xlim(-50, 400); ax.set_ylim(1, 1e9)
    ax.set_yticks([1, 1e3, 1e6, 1e9]); ax.set_yticklabels(["1 Pa", "1 kPa", "1 MPa", "1 GPa"])
    ax.set_xlabel("Temperature (°C)"); ax.set_ylabel("Pressure")
    ax.set_title("(a) H$_2$O", loc="left")


def _iron(ax):
    ax.set_xlim(0, 1800); ax.set_ylim(0, 20)
    # alpha/gamma: 912 °C at 0 to triple point 490 °C, 11 GPa
    P = np.linspace(0, 11, 50)
    T_ag = 912 - 30 * P - 0.76 * P**2
    ax.plot(T_ag, P, color=INK)
    # alpha/epsilon: triple point to ~13 GPa at 25 °C
    ax.plot([490, 300, 25, 0], [11, 11.9, 13.0, 13.1], color=INK)
    # gamma/epsilon
    P2 = np.linspace(11, 20, 20); ax.plot(490 + 34 * (P2 - 11), P2, color=INK)
    # gamma/delta and delta/L meeting at ~5.2 GPa, 1700 °C
    P3 = np.linspace(0, 5.2, 30)
    ax.plot(1394 + 58.5 * P3, P3, color=INK)
    ax.plot(1538 + 31.2 * P3, P3, color=INK)
    P4 = np.linspace(5.2, 8.6, 20); ax.plot(1700 + 29 * (P4 - 5.2), P4, color=INK)
    ax.fill_betweenx(P3, 1394 + 58.5 * P3, 1538 + 31.2 * P3, color=FIELD[3], lw=0)
    ax.text(330, 4.5, "α (BCC)", fontsize=9)
    ax.text(1000, 9, "γ (FCC)", fontsize=9)
    ax.text(110, 16, "ε (HCP)", fontsize=9)
    ax.text(1690, 12, "L", fontsize=10)
    ax.annotate("δ (BCC)", xy=(1500, 1.2), xytext=(1150, 2.6), fontsize=8,
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
    for t, lab in [(912, "912"), (1394, "1394"), (1538, "1538")]:
        ax.plot(t, 0, "|", color=INK, ms=6)
    ax.text(880, 0.35, "912", fontsize=7, ha="right")
    ax.text(1390, 0.35, "1394", fontsize=7, ha="right")
    ax.text(1545, 0.35, "1538", fontsize=7, ha="left")
    ax.annotate("≈13 GPa", xy=(25, 13.0), xytext=(230, 14.0), fontsize=7,
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
    ax.set_xlabel("Temperature (°C)"); ax.set_ylabel("Pressure (GPa)")
    ax.set_title("(b) Fe", loc="left")


def _carbon(ax):
    ax.set_xlim(0, 5000); ax.set_ylim(0, 20)
    T = np.linspace(0, 4500, 300)
    P = 1.7 + 0.00244 * T * np.tanh(T / 400)
    ax.plot(T, P, color=INK)
    Tt, Pt = 4500, P[-1]
    # graphite melting (approximate) and diamond melting
    gm_T = [4650, 4800, 4780, Tt]; gm_P = [0, 4, 8, Pt]
    ax.plot(PchipInterpolator(gm_P, gm_T)(np.linspace(0, Pt, 50)), np.linspace(0, Pt, 50), color=INK)
    ax.plot([Tt, 4700, 4900], [Pt, 16, 20], color=INK)
    ax.add_patch(Rectangle((1600, 5), 300, 1, fc=COLORS[4], ec=INK, lw=0.8, alpha=0.8, zorder=3))
    ax.annotate("HPHT synthesis\n5–6 GPa, 1600–1900 K,\nmetal solvent", xy=(1750, 6.0),
                xytext=(200, 11.0), fontsize=7, arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
    ax.annotate("CVD diamond: metastable,\nlow pressure", xy=(1400, 0.15), xytext=(1550, 1.2),
                fontsize=7, arrowprops=dict(arrowstyle="-|>", color=COLORS[2], lw=0.9, mutation_scale=8),
                color=COLORS[2])
    ax.plot([800, 1400], [0.05, 0.05], color=COLORS[2], lw=4, solid_capstyle="butt")
    ax.text(2600, 15, "diamond", fontsize=9)
    ax.text(3000, 4.0, "graphite", fontsize=9)
    ax.text(4910, 9, "L", fontsize=9, ha="center")
    ax.annotate("≈1.7 GPa at 0 K", xy=(0, 1.7), xytext=(200, 7.4), fontsize=7,
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
    ax.set_xlabel("Temperature (K)"); ax.set_ylabel("Pressure (GPa)")
    ax.set_title("(c) C", loc="left")


def _silica(ax_bar, ax_in):
    phases = [(0, 573, "α-quartz", FIELD[0]), (573, 870, "β-quartz", FIELD[2]),
              (870, 1470, "tridymite", FIELD[1]), (1470, 1713, "cristo-\nbalite", FIELD[3]),
              (1713, 1800, "L", "#FFFFFF")]
    for a, b, lab, c in phases:
        ax_bar.add_patch(Rectangle((a, 0), b - a, 1, fc=c, ec=INK, lw=0.8))
        ax_bar.text((a + b) / 2, 0.5, lab, ha="center", va="center", fontsize=7)
    ax_bar.set_xlim(0, 1800); ax_bar.set_ylim(0, 1)
    ax_bar.set_yticks([])
    for s in ["left", "right", "top"]:
        ax_bar.spines[s].set_visible(False)
    ax_bar.set_xticks([0, 573, 870, 1470, 1713])
    ax_bar.tick_params(axis="x", labelsize=7)
    ax_bar.set_xlabel("Temperature at 1 atm (°C)", fontsize=9)
    # P–T inset
    T = np.linspace(0, 1800, 100)
    ax_in.set_xlim(0, 1800); ax_in.set_ylim(0, 12)
    ax_in.plot(T, 2.0 + 0.0009 * T, color=INK, lw=1.2)
    ax_in.plot(T, 6.1 + 0.0026 * (T + 273.15), color=INK, lw=1.2)
    Pq = np.linspace(0, 2.0 + 0.0009 * 950, 30)
    ax_in.plot(573 + 260 * Pq, Pq, color=INK, lw=0.9, ls="--")
    ax_in.text(150, 0.9, "α-qz", fontsize=7)
    ax_in.text(1100, 0.9, "β-qz", fontsize=7)
    ax_in.text(400, 4.0, "coesite", fontsize=7.5)
    ax_in.text(250, 10.2, "stishovite", fontsize=7.5)
    ax_in.set_ylabel("P (GPa)", fontsize=8)
    ax_in.set_yticks([0, 4, 8, 12])
    ax_in.tick_params(labelsize=7)
    ax_in.set_xticklabels([])
    ax_in.set_title("(d) SiO$_2$", loc="left")


def unary_diagrams():
    fig = plt.figure(figsize=(6.8, 5.0))
    gs = GridSpec(2, 2, figure=fig, hspace=0.45, wspace=0.32)
    _water(fig.add_subplot(gs[0, 0]))
    _iron(fig.add_subplot(gs[0, 1]))
    _carbon(fig.add_subplot(gs[1, 0]))
    sub = GridSpecFromSubplotSpec(2, 1, subplot_spec=gs[1, 1], height_ratios=[3, 1], hspace=0.08)
    ax_in = fig.add_subplot(sub[0]); ax_bar = fig.add_subplot(sub[1])
    _silica(ax_bar, ax_in)
    save(fig, "07", "fig-7-1-unary-diagrams")


# ---------------------------------------------------------------- Figure 7.2
def _ideal_cu_ni(T):
    a = np.exp(13260 / R * (1 / T - 1 / 1358.0))
    b = np.exp(17480 / R * (1 / T - 1 / 1728.0))
    xL = (1 - a) / (b - a)
    return xL, b * xL


def _wt_ni(x):
    return 100 * x * 58.69 / (x * 58.69 + (1 - x) * 63.55)


def cu_ni_isomorphous():
    fig, ax = new_fig(6.4, 4.4)
    x = np.linspace(0, 1, 400)
    TL = 1085 + 370 * x + x * (1 - x) * (200 - 24 * (2 * x - 1))
    TS = 1085 + 370 * x + x * (1 - x) * (-100 + 60 * (2 * x - 1))
    w = 100 * x
    ax.fill_between(w, TL, 1500, color=FIELD[1], lw=0)
    ax.fill_between(w, TS, TL, color=FIELD[4], lw=0)
    ax.fill_between(w, 1000, TS, color=FIELD[0], lw=0)
    ax.plot(w, TL, color=COLORS[1], label="measured")
    ax.plot(w, TS, color=COLORS[0])
    T = np.linspace(1358.2, 1727.8, 400)
    xL, xS = _ideal_cu_ni(T)
    ax.plot(np.r_[0, _wt_ni(xL), 100], np.r_[1085, T - 273.15, 1455], "--", color=COLORS[1], lw=1.3,
            label="ideal solution")
    ax.plot(np.r_[0, _wt_ni(xS), 100], np.r_[1085, T - 273.15, 1455], "--", color=COLORS[0], lw=1.3)
    ax.text(30, 1440, "L", fontsize=13)
    ax.text(78, 1150, "α", fontsize=13)
    ax.text(62, 1372, "L + α", fontsize=10, rotation=22)
    ax.text(36, 1300, "liquidus", color=COLORS[1], fontsize=8, rotation=31)
    ax.text(52, 1222, "solidus", color=COLORS[0], fontsize=8, rotation=29)
    ax.text(1, 1040, "1085 °C (Cu)", fontsize=8)
    ax.text(99, 1463, "1455 °C (Ni)", fontsize=8, ha="right")
    # tie line at 1205 °C
    CL, Ca, C0, Tt = 26.9, 33.2, 30.0, 1205
    ax.plot([CL, Ca], [Tt, Tt], color=INK, lw=1.2)
    ax.axvline(30, ymax=(1205 - 1000) / 500, color=COLORS[2], lw=1, ls=":")
    ax.annotate("70/30 cupronickel", xy=(30, 1000), xytext=(33, 1022), fontsize=8, color=COLORS[2],
                arrowprops=dict(arrowstyle="-|>", color=COLORS[2], lw=0.8, mutation_scale=8))
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 0.88), fontsize=8, handlelength=2.2)
    ax.set_xlim(0, 100); ax.set_ylim(1000, 1500)
    ax.set_xlabel("Composition (wt% Ni)"); ax.set_ylabel("Temperature (°C)")
    # zoom inset of the tie line
    ins = ax.inset_axes([0.60, 0.06, 0.38, 0.38])
    ins.fill_between(w, TL, 1500, color=FIELD[1], lw=0)
    ins.fill_between(w, TS, TL, color=FIELD[4], lw=0)
    ins.fill_between(w, 1000, TS, color=FIELD[0], lw=0)
    ins.plot(w, TL, color=COLORS[1]); ins.plot(w, TS, color=COLORS[0])
    ins.plot(np.r_[_wt_ni(xL)], T - 273.15, "--", color=COLORS[1], lw=1.2)
    ins.plot(np.r_[_wt_ni(xS)], T - 273.15, "--", color=COLORS[0], lw=1.2)
    ins.plot([CL, Ca], [Tt, Tt], color=INK, lw=1.3)
    ins.plot([CL, Ca], [Tt, Tt], "o", color=INK, ms=3.5)
    ins.plot([C0], [Tt], "s", color=COLORS[2], ms=4.5)
    ins.text(26.6, 1207, r"$C_L$", fontsize=8, ha="right", va="bottom")
    ins.text(33.5, 1203, r"$C_\alpha$", fontsize=8, ha="left", va="top")
    ins.text((CL + C0) / 2, Tt - 1.5, "R", fontsize=8.5, ha="center", va="top", fontweight="bold")
    ins.text((C0 + Ca) / 2, Tt - 1.5, "S", fontsize=8.5, ha="center", va="top", fontweight="bold")
    ins.text(C0, Tt + 2, r"$C_0$", fontsize=7.5, ha="center", va="bottom", color=COLORS[2])
    ins.plot([C0, C0], [1193, 1217], "^", color=INK, ms=3.5)
    ins.text(C0 + 0.4, 1218, "1217 °C", fontsize=6.5, color=COLORS[1], va="bottom")
    ins.text(C0 + 0.4, 1191, "1193 °C", fontsize=6.5, color=COLORS[0], va="top")
    ax.text(62, 1262, "Ideal-solution tie line at 1205 °C:\n" r"$C_L$ = 26.9, $C_\alpha$ = 33.2 wt% Ni",
            fontsize=7.5, va="center")
    ins.set_xlim(22, 38); ins.set_ylim(1180, 1230)
    ins.tick_params(labelsize=6.5)
    ins.set_facecolor("white")
    for s in ["top", "right"]:
        ins.spines[s].set_visible(True)
    ax.indicate_inset_zoom(ins, edgecolor="0.5")
    ax.text(2, 1300, r"$W_\alpha=\dfrac{R}{R+S}=0.49$", fontsize=8.5, ha="left", va="center")
    save(fig, "07", "fig-7-2-cu-ni-isomorphous")


# ---------------------------------------------------------------- Figure 7.3
def _seg_dist(X, Y, x0, y0, x1, y1):
    dx, dy = x1 - x0, y1 - y0
    t = np.clip(((X - x0) * dx + (Y - y0) * dy) / (dx * dx + dy * dy + 1e-12), 0, 1)
    return np.hypot(X - (x0 + t * dx), Y - (y0 + t * dy))


def _eutectic_texture(n, rng, density, length, width):
    """Light Al background with dark Si flakes; returns float image (1 = light)."""
    X, Y = np.meshgrid(np.linspace(0, 1, n), np.linspace(0, 1, n))
    img = np.full((n, n), 0.66)
    # colonies with locally aligned flakes
    for _ in range(density):
        cx, cy = rng.uniform(-0.05, 1.05, 2)
        ang = rng.uniform(0, np.pi)
        L = length * rng.uniform(0.6, 1.3)
        x0, y0 = cx - L / 2 * np.cos(ang), cy - L / 2 * np.sin(ang)
        x1, y1 = cx + L / 2 * np.cos(ang), cy + L / 2 * np.sin(ang)
        # restrict computation to a bounding box for speed
        i0 = max(int((min(y0, y1) - 0.03) * n), 0); i1 = min(int((max(y0, y1) + 0.03) * n) + 1, n)
        j0 = max(int((min(x0, x1) - 0.03) * n), 0); j1 = min(int((max(x0, x1) + 0.03) * n) + 1, n)
        if i0 >= i1 or j0 >= j1:
            continue
        d = _seg_dist(X[i0:i1, j0:j1], Y[i0:i1, j0:j1], x0, y0, x1, y1)
        img[i0:i1, j0:j1] = np.where(d < width, 0.18, img[i0:i1, j0:j1])
    return img


def _dendrite_mask(n, rng, centres, arm, w_primary, w_sec, sec_len, sec_sp):
    X, Y = np.meshgrid(np.linspace(0, 1, n), np.linspace(0, 1, n))
    m = np.zeros((n, n), bool)
    for cx, cy in centres:
        rot = rng.uniform(0, np.pi / 2)
        for k in range(4):
            a = rot + k * np.pi / 2
            L = arm * rng.uniform(0.75, 1.1)
            ex, ey = cx + L * np.cos(a), cy + L * np.sin(a)
            m |= _seg_dist(X, Y, cx, cy, ex, ey) < w_primary
            for s in np.arange(sec_sp, L, sec_sp):
                bx, by = cx + s * np.cos(a), cy + s * np.sin(a)
                sl = sec_len * (1 - 0.6 * s / L)
                for sg in (+1, -1):
                    m |= _seg_dist(X, Y, bx, by, bx + sg * sl * np.cos(a + np.pi / 2),
                                   by + sg * sl * np.sin(a + np.pi / 2)) < w_sec
    return m


def _circle_image(ax, img, xc, yc, r, label, cmap="gray"):
    im = ax.imshow(img, extent=(xc - r, xc + r, yc - r, yc + r), cmap=cmap, vmin=0, vmax=1,
                   origin="lower", interpolation="bilinear", zorder=2)
    c = Circle((xc, yc), r, transform=ax.transData, fc="none", ec=INK, lw=1.2, zorder=4)
    ax.add_patch(c)
    im.set_clip_path(c)
    ax.text(xc, yc - r - 0.12, label, ha="center", va="top", fontsize=8)
    return c


def al_si_eutectic():
    fig = plt.figure(figsize=(6.8, 5.0))
    gs = GridSpec(2, 2, figure=fig, width_ratios=[6, 1], height_ratios=[2.7, 1.9], wspace=0.06, hspace=0.30)
    ax = fig.add_subplot(gs[0, 0]); axr = fig.add_subplot(gs[0, 1], sharey=ax)
    Te, Ce, Ca = 577, 12.6, 1.65
    liq_w = [12.6, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100]
    liq_T = [577, 625, 710, 790, 855, 960, 1040, 1110, 1180, 1250, 1330, 1414]
    liq = PchipInterpolator(liq_w, liq_T)
    for a in (ax, axr):
        wv = np.linspace(Ce, 100, 500)
        a.fill_between(wv, Te, liq(wv), color=FIELD[2], lw=0)
        a.fill_between([0, 100], 400, Te, color=FIELD[5], lw=0)
        a.plot(wv, liq(wv), color=COLORS[1])
        a.plot([Ca, 100], [Te, Te], color=INK, lw=1.4)
        a.axvline(100, color=INK, lw=1.4)
    wl = np.linspace(0, Ce, 100)
    ax.fill_between(wl, 660 - 83 * wl / Ce, 900, color=FIELD[1], lw=0)
    ax.fill_between(np.linspace(Ce, 30, 100), liq(np.linspace(Ce, 30, 100)), 900, color=FIELD[1], lw=0)
    ax.fill_between([0, Ca, Ce], [660, Te, Te], [660, 660 - 83 * Ca / Ce, Te], color=FIELD[0], lw=0)
    ax.plot(wl, 660 - 83 * wl / Ce, color=COLORS[1])
    ax.plot([0, Ca], [660, Te], color=COLORS[0])
    Ts = np.linspace(400, Te, 50)
    sol = Ca * np.exp(-5600 * (1 / (Ts + 273.15) - 1 / (Te + 273.15)))
    ax.plot(sol, Ts, color=COLORS[0])
    ax.fill_betweenx(np.r_[Ts, 660], 0, np.r_[sol, 0], color=FIELD[0], lw=0)
    ax.fill_betweenx(np.linspace(Te, 660, 20), 0, Ca * (660 - np.linspace(Te, 660, 20)) / 83, color=FIELD[0], lw=0)
    ax.plot(Ce, Te, "o", color=INK, ms=4)
    ax.text(Ce + 0.4, Te - 8, "12.6 wt%, 577 °C", fontsize=7.5, ha="left", va="top")
    ax.text(Ca + 0.25, Te - 6, "1.65", fontsize=7, va="top")
    ax.text(0.4, 666, "660 °C (Al)", fontsize=7.5, va="bottom")
    ax.text(6, 800, "L", fontsize=13)
    ax.annotate("α", xy=(0.45, 520), xytext=(2.6, 480), fontsize=11, va="center",
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
    ax.text(3.6, 586, "L + α", fontsize=8, va="bottom")
    ax.text(22.5, 660, "L + Si", fontsize=9)
    ax.text(18, 450, "α + Si", fontsize=10)
    for c, lab in [(7, "A356\n7 Si"), (12.6, "A413\n12.6 Si"), (18, "A390\n18 Si")]:
        ax.axvline(c, color=COLORS[2], ls="--", lw=1)
        ax.text(c + 0.3, 880, lab, color=COLORS[2], fontsize=7.5, va="top")
    ax.set_xlim(0, 30); axr.set_xlim(95, 100.0)
    ax.set_ylim(400, 900)
    ax.set_xlabel("Composition (wt% Si)", x=0.58)
    ax.set_ylabel("Temperature (°C)")
    ax.spines["right"].set_visible(False)
    axr.spines["left"].set_visible(False); axr.tick_params(left=False, labelleft=False)
    axr.set_xticks([100])
    axr.text(97.5, 860, "Si melts\n1414 °C ↑", fontsize=7, ha="center", va="top")
    axr.text(97.5, 690, "L+Si", fontsize=7.5, ha="center")
    axr.text(97.5, 470, "α+Si", fontsize=7.5, ha="center")
    # break marks
    d = 0.015
    kw = dict(color=INK, clip_on=False, lw=1)
    ax.plot((1 - d / 2, 1 + d / 2), (-d * 2, d * 2), transform=ax.transAxes, **kw)
    axr.plot((-d * 3, d * 3), (-d * 2, d * 2), transform=axr.transAxes, **kw)

    # micrograph insets
    axm = fig.add_subplot(gs[1, :])
    axm.set_xlim(0, 9); axm.set_ylim(-0.55, 2.0); axm.set_aspect("equal"); axm.axis("off")
    n = 360
    rng = np.random.default_rng(3)
    # A356: primary alpha dendrites ~51 %
    eut = _eutectic_texture(n, rng, 1400, 0.05, 0.0030)
    cent = [(0.22, 0.25), (0.72, 0.22), (0.25, 0.75), (0.75, 0.74), (0.5, 0.5), (0.02, 0.5),
            (0.98, 0.5), (0.5, 0.0), (0.5, 1.0)]
    m = _dendrite_mask(n, rng, cent, 0.27, 0.024, 0.0135, 0.07, 0.05)
    img = np.where(m, 0.97, eut)
    print(f"A356 inset primary alpha area fraction = {m.mean():.2f}")
    _circle_image(axm, img, 1.3, 1.0, 0.95, "A356 (7 % Si): ~51 % primary\nα-Al dendrites + eutectic")
    # eutectic
    eut2 = _eutectic_texture(n, np.random.default_rng(5), 1400, 0.06, 0.0030)
    _circle_image(axm, eut2, 4.5, 1.0, 0.95, "A413 (12.6 % Si): fine\nAl + Si eutectic plates")
    # A390: blocky primary Si
    eut3 = _eutectic_texture(n, np.random.default_rng(8), 1400, 0.06, 0.0030)
    _circle_image(axm, eut3, 7.7, 1.0, 0.95, "A390 (18 % Si): ~6 % blocky\nprimary Si + eutectic")
    clip = Circle((7.7, 1.0), 0.95, transform=axm.transData)
    blocks = [(7.35, 1.45, 0.13, 5, 10), (8.1, 1.25, 0.11, 6, 30),
              (7.55, 0.55, 0.12, 4, 20), (8.15, 0.6, 0.09, 5, 0), (7.75, 1.0, 0.08, 6, 15)]
    blocks = [(bx, by, 1.12 * s, nv, rot) for bx, by, s, nv, rot in blocks]
    for (bx, by, s, nv, rot) in blocks:
        p = RegularPolygon((bx, by), nv, radius=s, orientation=np.radians(rot), fc="0.18", ec="0.05",
                           lw=0.6, zorder=3)
        axm.add_patch(p); p.set_clip_path(clip)
    area = sum(nv / 2 * s**2 * np.sin(2 * np.pi / nv) for _, _, s, nv, _ in blocks) / (np.pi * 0.95**2)
    print(f"A390 inset primary Si area fraction = {area:.3f}")
    save(fig, "07", "fig-7-3-al-si-eutectic")


# ---------------------------------------------------------------- Figure 7.4
def _fe_c_lines(ax, lw=1.4):
    c = INK
    L = PchipInterpolator([0, 0.53, 2.0, 4.30], [1538, 1495, 1385, 1147])
    x = np.linspace(0, 4.30, 200); ax.plot(x, L(x), color=c, lw=lw)
    ax.plot([4.30, 6.70], [1147, 1227], color=c, lw=lw)
    ax.plot([0, 0.09], [1538, 1495], color=c, lw=lw)
    ax.plot([0, 0.09], [1394, 1495], color=c, lw=lw)
    ax.plot([0, 0.17], [1394, 1495], color=c, lw=lw)
    ax.plot([0.09, 0.53], [1495, 1495], color=c, lw=lw)
    S = PchipInterpolator([0.17, 1.0, 2.14], [1495, 1380, 1147])
    x = np.linspace(0.17, 2.14, 100); ax.plot(x, S(x), color=c, lw=lw)
    ax.plot([2.14, 6.70], [1147, 1147], color=c, lw=lw)
    A3 = PchipInterpolator([0, 0.4, 0.76], [912, 795, 727])
    x = np.linspace(0, 0.76, 100); ax.plot(x, A3(x), color=COLORS[0], lw=lw)
    Acm = PchipInterpolator([0.76, 1.4, 2.14], [727, 945, 1147])
    x = np.linspace(0.76, 2.14, 100); ax.plot(x, Acm(x), color=COLORS[1], lw=lw)
    ax.plot([0, 0.022], [912, 727], color=c, lw=lw)
    ax.plot([0.022, 6.70], [727, 727], color=COLORS[2], lw=lw)
    ax.plot([0.022, 0.006], [727, 400], color=c, lw=lw * 0.8)
    ax.plot([6.70, 6.70], [400, 1227], color=c, lw=lw)
    return A3, Acm


def fe_fe3c_diagram():
    fig, ax = new_fig(6.8, 4.9)
    A3, Acm = _fe_c_lines(ax)
    ax.set_xlim(0, 6.70); ax.set_ylim(400, 1600)
    ax.set_xlabel("Composition (wt% C)"); ax.set_ylabel("Temperature (°C)")
    # graphite (stable) lines, dotted
    ax.plot([2.08, 6.70], [1153, 1153], ":", color=COLORS[3], lw=1.4)
    ax.plot([0.02, 6.70], [738, 738], ":", color=COLORS[3], lw=1.4)
    ax.text(6.62, 1157, "Fe–graphite eutectic 1153 °C", fontsize=7, color=COLORS[3], ha="right", va="bottom")
    ax.text(6.62, 742, "Fe–graphite eutectoid 738 °C", fontsize=7, color=COLORS[3], ha="right", va="bottom")
    # field labels
    ax.text(2.6, 1450, "L", fontsize=13)
    ax.text(0.75, 1150, "γ\n(austenite)", fontsize=10, ha="center")
    ax.text(2.4, 1300, "L + γ", fontsize=9)
    ax.text(5.0, 1240, "L + Fe$_3$C", fontsize=9)
    ax.text(3.9, 950, "γ + Fe$_3$C", fontsize=10)
    ax.text(5.75, 600, "α + Fe$_3$C", fontsize=10, ha="center")
    ax.text(0.17, 735, "α+γ", fontsize=8, va="bottom")
    ax.annotate("α (ferrite)", xy=(0.012, 660), xytext=(1.45, 610), fontsize=8.5, va="center",
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
    ax.text(6.56, 640, "Fe$_3$C", fontsize=8.5, ha="right", rotation=90)
    # key points
    for (xp, yp, lab, dx, dy, ha) in [(4.30, 1147, "eutectic\n4.30 wt%, 1147 °C", 0.0, -95, "center"),
                                      (0.76, 727, "eutectoid\n0.76 wt%, 727 °C", 0.15, -95, "left"),
                                      (2.14, 1147, "2.14", 0.08, -60, "left")]:
        ax.plot(xp, yp, "o", color=INK, ms=4, zorder=5)
        ax.text(xp + dx, yp + dy, lab, fontsize=7.5, ha=ha, va="bottom")
    ax.text(0.05, 722, "0.022", fontsize=7, va="top")
    ax.text(0.03, 916, "912 °C", fontsize=7.5, va="bottom")
    ax.text(5.5, 718, "A$_1$ 727 °C", fontsize=8, color=COLORS[2], va="top")
    ax.text(0.30, 845, "A$_3$", fontsize=9, color=COLORS[0])
    ax.text(1.40, 1000, "A$_{cm}$", fontsize=9, color=COLORS[1], ha="right")
    # steel grades
    for c, lab in [(0.40, "AISI 1040"), (1.0, "AISI 52100\nbearing steel")]:
        ax.axvline(c, ymax=(700 - 400) / 1200, color=COLORS[4], ls="--", lw=1.1)
        ax.text(c + 0.05, 405, lab, fontsize=7, color="#9A6A00", va="bottom", rotation=90)
    # brackets
    yb = 1578
    for a_, b_, lab in [(0, 2.14, "steels"), (2.14, 6.70, "cast irons")]:
        ax.annotate("", xy=(a_, yb), xytext=(b_, yb), annotation_clip=False,
                    arrowprops=dict(arrowstyle="<->", color=INK, lw=0.9, shrinkA=0, shrinkB=0))
        ax.text((a_ + b_) / 2, yb - 6, lab, ha="center", va="top", fontsize=8.5)
    top = ax.secondary_xaxis("top", functions=(lambda c: c / 6.70 * 100, lambda f: f * 6.70 / 100))
    top.set_xlabel("wt% Fe$_3$C", fontsize=9)
    top.set_xticks([0, 20, 40, 60, 80, 100])
    # inset: peritectic corner
    ins = ax.inset_axes([0.42, 0.075, 0.30, 0.18])
    _fe_c_lines(ins, lw=1.1)
    ins.set_xlim(0, 0.65); ins.set_ylim(1380, 1568)
    ins.tick_params(labelsize=6.5)
    ins.set_facecolor("white")
    for s in ["top", "right"]:
        ins.spines[s].set_visible(True)
    ins.plot([0.09, 0.17, 0.53], [1495] * 3, "o", color=INK, ms=3)
    ins.text(0.09, 1500, "0.09", fontsize=6.5, ha="center", va="bottom")
    ins.text(0.17, 1484, "0.17", fontsize=6.5, ha="center", va="top")
    ins.text(0.53, 1500, "0.53", fontsize=6.5, ha="center", va="bottom")
    ins.text(0.36, 1488, "peritectic\n1495 °C", fontsize=6.5, ha="center", va="top")
    ins.text(0.012, 1450, "δ", fontsize=8)
    ins.text(0.30, 1530, "L", fontsize=8)
    ins.text(0.40, 1405, "L + γ", fontsize=7)
    ins.text(0.07, 1395, "γ", fontsize=8)
    ins.text(0.065, 1430, "δ+γ", fontsize=6)
    ax.add_patch(Rectangle((0, 1380), 0.65, 170, fc="none", ec="0.5", lw=0.8))
    ax.text(0.68, 1385, "(inset)", fontsize=6.5, color="0.4", va="bottom")
    ins.text(0.015, 1541, "1538 °C", fontsize=6.5, va="bottom")
    save(fig, "07", "fig-7-4-fe-fe3c-diagram")


# ---------------------------------------------------------------- Figure 7.5
def zro2_y2o3():
    fig, ax = new_fig(6.4, 4.6)
    ax.set_xlim(0, 12); ax.set_ylim(0, 2800)
    Teo = 565
    # boundaries (schematic after Scott 1975; mol% Y2O3)
    xmt, Tmt = np.array([0, 0.4, 0.8, 1.0]), np.array([1170, 950, 700, Teo])     # m/(m+t)
    xtm, Ttm = np.array([0, 0.8, 1.6, 2.3]), np.array([1170, 1000, 780, Teo])    # t/(m+t)
    xt = np.array([0, 1.0, 1.8, 2.4, 2.65, 2.6, 2.3])                              # t/(t+c)
    Tt = np.array([2370, 2150, 1900, 1600, 1250, 900, Teo])
    xc = np.array([0, 1.2, 2.6, 4.2, 5.8, 7.0, 8.0])                               # c/(t+c)
    Tc = np.array([2370, 2200, 1950, 1600, 1200, 850, Teo])
    xmc, Tmc = np.array([8.0, 8.3, 8.6]), np.array([Teo, 300, 0])                  # c/(m+c)
    poly = lambda x, y, c: ax.add_patch(Polygon(np.c_[x, y], fc=c, ec="none", zorder=0))
    poly(np.r_[0, 1.0, xmt[::-1]], np.r_[0, 0, Tmt[::-1]], FIELD[0])                       # m
    poly(np.r_[xmt, xtm[::-1]], np.r_[Tmt, Ttm[::-1]], FIELD[3])                           # m+t
    poly(np.r_[xtm, xt[::-1]], np.r_[Ttm, Tt[::-1]], FIELD[2])                             # t
    poly(np.r_[xt, xc[::-1]], np.r_[Tt, Tc[::-1]], FIELD[4])                               # t+c
    poly(np.r_[xc, xmc[1:], 12, 12, 0], np.r_[Tc, Tmc[1:], 0, 2725, 2710], FIELD[1])       # c
    poly(np.r_[1.0, xmc[::-1], 1.0], np.r_[0, Tmc[::-1], Teo], FIELD[5])                   # m+c
    # lines
    ax.plot(xtm, Ttm, color=INK)
    ax.plot(xmt, Tmt, color=INK)
    ax.plot([1.0, 1.0], [0, Teo], color=INK)
    ax.plot(xt, Tt, color=INK)
    ax.plot(xc, Tc, color=INK)
    ax.plot(xmc, Tmc, color=INK)
    ax.plot([1.0, 8.0], [Teo, Teo], color=INK)
    ax.plot([0, 12], [2710, 2745], color=INK)
    ax.plot([0, 12], [2710, 2725], color=INK, lw=1)
    ax.text(0.2, 2754, "L", fontsize=10, va="bottom")
    # labels
    ax.text(0.3, 250, "m", fontsize=12)
    ax.text(6.4, 120, "m + c", fontsize=11)
    ax.text(1.95, 1200, "t", fontsize=12)
    ax.text(5.3, 850, "t + c", fontsize=11)
    ax.text(9.5, 1500, "c (cubic, fluorite)", fontsize=10, ha="center")
    ax.text(0.45, 830, "m+t", fontsize=7.5, rotation=-62)
    ax.text(5.0, Teo + 20, "eutectoid ≈565 °C", fontsize=7, va="bottom")
    ax.text(0.1, 1190, "1170", fontsize=7, va="bottom")
    ax.text(0.1, 2390, "2370", fontsize=7, va="bottom")
    ax.text(1.5, 2690, "≈2710 °C", fontsize=7, va="top")
    # compositions
    def vline(x, txt, y, c):
        ax.axvline(x, color=c, ls="--", lw=1.2, ymax=0.93)
        ax.text(x + 0.12, y, txt, fontsize=7.3, color=c, va="bottom", rotation=90)
    ax.axvspan(4.0, 4.5, ymax=0.93, color=COLORS[4], alpha=0.35, lw=0)
    vline(3.0, "3Y-TZP: crowns, hip heads\n(metastable t)", 700, COLORS[0])
    ax.text(4.55, 1650, "7–8 wt% YSZ: thermal-\nbarrier coatings (t′)", fontsize=7.3, color="#9A6A00",
            rotation=90, va="bottom")
    vline(8.0, "8YSZ: SOFC electrolytes,\noxygen sensors (cubic)", 1700, COLORS[2])
    ax.annotate("t→m under crack-tip stress:\ntransformation toughening", xy=(3.0, 60), xytext=(3.3, 400), va="center",
                fontsize=7.3, color=COLORS[0],
                arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=0.9, mutation_scale=9))
    ax.plot(3.0, 60, "o", color=COLORS[0], ms=5)
    ax.set_xlabel("Composition (mol% Y$_2$O$_3$)"); ax.set_ylabel("Temperature (°C)")
    save(fig, "07", "fig-7-5-zro2-y2o3")


# ---------------------------------------------------------------- Figure 7.6
SQ3 = np.sqrt(3) / 2
CORNERS = np.array([[0.5, SQ3], [0.0, 0.0], [1.0, 0.0]])  # A top, B left, C right


def bary(a, b, c):
    return a * CORNERS[0] + b * CORNERS[1] + c * CORNERS[2]


def _perm(p, k):
    p = np.asarray(p, float)
    return np.roll(p, k)


def _triangle(ax, labels=("A", "B", "C")):
    ax.add_patch(Polygon(CORNERS, closed=True, fc="none", ec=INK, lw=1.2, zorder=5))
    ax.text(0.5, SQ3 + 0.03, labels[0], ha="center", va="bottom", fontsize=10)
    ax.text(-0.03, -0.03, labels[1], ha="right", va="top", fontsize=10)
    ax.text(1.03, -0.03, labels[2], ha="left", va="top", fontsize=10)
    ax.set_xlim(-0.1, 1.1); ax.set_ylim(-0.2, 1.0); ax.set_aspect("equal"); ax.axis("off")


def _bezier(p0, p1, p2, n=40):
    t = np.linspace(0, 1, n)[:, None]
    return (1 - t) ** 2 * p0 + 2 * (1 - t) * t * p1 + t**2 * p2


def ternary_gibbs():
    fig, axs = plt.subplots(1, 3, figsize=(6.8, 2.9))
    # (a) Gibbs triangle
    ax = axs[0]
    _triangle(ax)
    for f in np.arange(0.1, 1.0, 0.1):
        for k in range(3):
            p = np.zeros(3); q = np.zeros(3)
            p[k] = f; q[k] = f
            p[(k + 1) % 3] = 1 - f; q[(k + 2) % 3] = 1 - f
            P1, P2 = bary(*p), bary(*q)
            ax.plot([P1[0], P2[0]], [P1[1], P2[1]], color="0.85", lw=0.6, zorder=1)
    P = bary(0.5, 0.3, 0.2)
    # read-off lines: constant A to edge AB, constant B to edge BC, constant C to edge CA
    for target, col, lab in [(bary(0.5, 0.5, 0.0), COLORS[0], "A = 50 %"),
                             (bary(0.0, 0.3, 0.7), COLORS[1], "B = 30 %"),
                             (bary(0.8, 0.0, 0.2), COLORS[2], "C = 20 %")]:
        ax.plot([P[0], target[0]], [P[1], target[1]], "--", color=col, lw=1.2, zorder=3)
        ax.plot(*target, "o", color=col, ms=3, zorder=6)
    ax.text(*(bary(0.5, 0.5, 0.0) + [-0.04, 0.0]), "50 % A", color=COLORS[0], fontsize=7.5, ha="right", va="center")
    ax.text(*(bary(0.0, 0.3, 0.7) + [0, -0.03]), "30 % B", color=COLORS[1], fontsize=7.5, ha="center", va="top")
    ax.text(*(bary(0.8, 0.0, 0.2) + [0.04, 0.0]), "20 % C", color=COLORS[2], fontsize=7.5, ha="left", va="center")
    ax.plot(*P, "o", color=INK, ms=5, zorder=7)
    ax.text(P[0] - 0.02, P[1] - 0.04, "P", fontsize=9, zorder=7, ha="right", va="top")
    ax.set_title("(a) Gibbs triangle", loc="left", fontsize=9.5)

    # (b) isothermal section
    ax = axs[1]
    _triangle(ax)
    # use symmetric construction by cyclic permutation of a template for corner A
    def corner_pts(k):
        # returns dict of barycentric points for corner phase k (0=A/alpha,1=B/beta,2=C/gamma)
        e_next = _perm([0.84, 0.16, 0.0], k)     # solvus on edge toward next corner
        e_prev = _perm([0.84, 0.0, 0.16], k)
        t_next = _perm([0.76, 0.17, 0.07], k)    # alpha vertex of tie triangle with next phase
        t_prev = _perm([0.76, 0.07, 0.17], k)
        return e_next, t_next, t_prev, e_prev
    # liquid vertices: L_k is the liquid corner of tie triangle (phase k, phase k+1)
    Lk = [np.array([0.40, 0.40, 0.20]), np.array([0.20, 0.40, 0.40]), np.array([0.40, 0.20, 0.40])]
    phase = ["α", "β", "γ"]
    cols = [FIELD[0], FIELD[1], FIELD[2]]
    xy = lambda p: bary(*p)
    for k in range(3):
        e_n, t_n, t_p, e_p = corner_pts(k)
        # single-phase corner region
        corner = CORNERS[k]
        arc = _bezier(xy(t_n), xy(_perm([0.70, 0.15, 0.15], k)), xy(t_p))
        poly = np.vstack([corner, xy(e_n), xy(t_n), arc, xy(t_p), xy(e_p)])
        ax.add_patch(Polygon(poly, fc=cols[k], ec=INK, lw=0.9, zorder=2))
    # liquid region: curved triangle through Lk, bulging toward the corners' two-phase fields
    Lc = []
    for k in range(3):
        a_, b_ = Lk[(k - 1) % 3], Lk[k]     # liquid side facing corner k lies between L_{k-1} and L_k
        mid = (a_ + b_) / 2; mid = mid + 0.05 * (np.eye(3)[k] - mid)
        Lc.append(_bezier(xy(a_), xy(mid), xy(b_)))
    ax.add_patch(Polygon(np.vstack(Lc), fc="white", ec=INK, lw=0.9, zorder=2))
    for k in range(3):
        e_n, t_n, t_p, e_p = corner_pts(k)
        kn = (k + 1) % 3
        e_n2, t_n2, t_p2, e_p2 = corner_pts(kn)
        # tie triangle k + kn + L_k
        tri = np.vstack([xy(t_n), xy(t_p2), xy(Lk[k])])
        ax.add_patch(Polygon(tri, fc="#E4E4E4", ec=INK, lw=0.9, zorder=2))
        # two-phase solid field along edge: tie lines between e_n..t_n and e_p2..t_p2
        for s in np.linspace(0.15, 0.85, 5):
            p1 = xy(e_n + s * (t_n - e_n)); p2 = xy(e_p2 + s * (t_p2 - e_p2))
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color="0.55", lw=0.6, zorder=1)
        # solid + L fanning tie lines: from arc on corner k to liquid side
        arc = _bezier(xy(t_n), xy(_perm([0.70, 0.15, 0.15], k)), xy(t_p))
        liq = Lc[k][::-1]  # from L_k to L_{k-1}
        for s in np.linspace(0.1, 0.9, 7):
            i = int(s * (len(arc) - 1))
            ax.plot([arc[i, 0], liq[i, 0]], [arc[i, 1], liq[i, 1]], color="0.55", lw=0.6, zorder=1)
    # labels
    for k, lab in enumerate(phase):
        ax.text(*(CORNERS[k] + (CORNERS[k] - [0.5, SQ3 / 3]) * -0.13), lab, ha="center", va="center", fontsize=9, zorder=6)
    ax.text(0.5, SQ3 / 3, "L", ha="center", va="center", fontsize=10, zorder=6)
    ax.text(*xy([0.60, 0.20, 0.20]), "α+L", ha="center", va="center", fontsize=6.5, zorder=6,
            bbox=dict(fc="white", ec="none", pad=0.5))
    ax.text(*xy([0.50, 0.465, 0.035]), "α+β", ha="center", va="center", fontsize=6.5, zorder=6, rotation=60,
            bbox=dict(fc="white", ec="none", pad=0.5))
    # centre of gravity point in tie triangle alpha-beta-L (k=0)
    e_n, t_n, t_p, e_p = corner_pts(0); _, _, t_p2, _ = corner_pts(1)
    V = [xy(t_n), xy(t_p2), xy(Lk[0])]
    w = np.array([0.35, 0.35, 0.30]); X = w[0] * V[0] + w[1] * V[1] + w[2] * V[2]
    for i in range(3):
        o1, o2 = V[(i + 1) % 3], V[(i + 2) % 3]
        # intersection of line Vi->X with side o1-o2
        d = X - V[i]; e = o2 - o1
        M = np.array([[d[0], -e[0]], [d[1], -e[1]]]); s, _ = np.linalg.solve(M, o1 - V[i])
        Q = V[i] + s * d
        ax.plot([V[i][0], Q[0]], [V[i][1], Q[1]], ":", color=COLORS[1], lw=0.9, zorder=4)
    ax.plot(*X, "o", color=COLORS[1], ms=3.5, zorder=7)
    ax.annotate("α+β+L tie triangle:\ncentre of gravity", xy=X, xytext=(-0.14, 0.78), fontsize=6.5, color=COLORS[1],
                arrowprops=dict(arrowstyle="-", color=COLORS[1], lw=0.6), zorder=7)
    ax.set_title("(b) isothermal section", loc="left", fontsize=9.5)

    # (c) liquidus projection
    ax = axs[2]
    Tm = np.array([1000.0, 900.0, 800.0])
    S = np.array([[0, 700, 480], [600, 0, 650], [430, 560, 0]])   # S[i, j]: slope of surface i toward j
    def surf(p):
        lin = Tm - S @ p
        return lin - 120 * (1 - p) ** 2
    _triangle(ax)
    n = 160
    pts, vals, own = [], [], []
    for i in range(n + 1):
        for j in range(n + 1 - i):
            a, b = i / n, j / n; c = 1 - a - b
            p = np.array([a, b, c])
            T = surf(p)
            pts.append(bary(a, b, c)); vals.append(T.max()); own.append(T.argmax())
    pts = np.array(pts); vals = np.array(vals); own = np.array(own)
    import matplotlib.tri as mtri
    tri = mtri.Triangulation(pts[:, 0], pts[:, 1])
    cs = ax.tricontour(tri, vals, levels=np.arange(350, 1000, 50), colors="0.55", linewidths=0.6)
    ax.clabel(cs, levels=[500, 700, 900], fontsize=5.5, fmt="%d °C", inline_spacing=1)
    # valleys: where two surfaces are equal and both maximal
    def valley(i, j):
        out = []
        for s in np.linspace(0, 1, 300):
            k = 3 - i - j
            # composition with x_k = s, solve along the line for T_i = T_j
            def g(u):
                p = np.zeros(3); p[k] = s; p[i] = u * (1 - s); p[j] = (1 - u) * (1 - s)
                Ts = surf(p); return Ts[i] - Ts[j]
            try:
                u = brentq(g, 0, 1)
            except ValueError:
                continue
            p = np.zeros(3); p[k] = s; p[i] = u * (1 - s); p[j] = (1 - u) * (1 - s)
            Ts = surf(p)
            if Ts[k] > Ts[i] + 1e-9:
                break
            out.append((p, Ts[i]))
        return out
    Es = []
    names = {(0, 1): "e$_1$", (1, 2): "e$_2$", (2, 0): "e$_3$"}
    for (i, j) in [(0, 1), (1, 2), (2, 0)]:
        v = valley(i, j)
        xyv = np.array([bary(*p) for p, _ in v])
        ax.plot(xyv[:, 0], xyv[:, 1], color=COLORS[1], lw=1.6, zorder=4)
        mid = len(xyv) // 2
        ax.annotate("", xy=xyv[mid + 4], xytext=xyv[mid - 4],
                    arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.2, mutation_scale=10), zorder=5)
        e = xyv[0]
        ax.plot(*e, "o", color=COLORS[1], ms=3.5, zorder=6)
        off = e - np.array([0.5, SQ3 / 3]); off = off / np.linalg.norm(off) * 0.08
        ax.text(*(e + off), names[(i, j)], fontsize=8, ha="center", va="center", color=COLORS[1])
        Es.append((xyv[-1], v[-1][1]))
    E = np.mean([e for e, _ in Es], axis=0)
    ax.plot(*E, "s", color=COLORS[1], ms=5, zorder=6)
    ax.text(E[0] + 0.04, E[1] - 0.02, "E", fontsize=9, color=COLORS[1], zorder=6, va="top")
    print(f"ternary eutectic T approx {np.mean([t for _, t in Es]):.0f} °C")
    ax.text(0.5, -0.15, "e.g. Sn–Ag–Cu: E ≈ 217 °C near Sn–3.5Ag–0.9Cu", fontsize=6.5, ha="center", va="top")
    ax.text(1.08, 0.80, "isotherms\nevery 50 °C", fontsize=6.5, color="0.4", ha="right", va="top")
    ax.set_title("(c) liquidus projection", loc="left", fontsize=9.5)
    fig.tight_layout(w_pad=0.4)
    save(fig, "07", "fig-7-6-ternary-gibbs-triangle")


if __name__ == "__main__":
    unary_diagrams()
    cu_ni_isomorphous()
    al_si_eutectic()
    fe_fe3c_diagram()
    zro2_y2o3()
    ternary_gibbs()
