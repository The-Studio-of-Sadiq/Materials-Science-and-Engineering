"""Figures for Chapter 9 — Nucleation, Growth and Solidification.

Run from the repository root:  python figures/scripts/ch09.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle, Arc, Wedge, FancyArrowPatch
from matplotlib.gridspec import GridSpec
from scipy.spatial import Voronoi

RNG = np.random.default_rng(9)
GAMMA, DHV, TM = 0.177, 1.88e9, 1358.0


# ---------------------------------------------------------------- Figure 9.1
def nucleation_barrier():
    fig, ax = new_fig(6.4, 4.0)
    r = np.linspace(0, 6e-9, 600)
    rn = r * 1e9
    S = 4 * np.pi * r**2 * GAMMA / 1e-18
    ax.axhline(0, color="0.6", lw=0.7)
    for dT, c, ann in [(100, COLORS[0], (3.3, 6.2)), (236, COLORS[1], (1.6, 2.6))]:
        Gv = DHV * dT / TM
        V = -(4 / 3) * np.pi * r**3 * Gv / 1e-18
        tot = S + V
        rs = 2 * GAMMA / Gv
        Gs = 16 * np.pi * GAMMA**3 / (3 * Gv**2) / 1e-18
        if dT == 100:
            ax.plot(rn, S, "--", color="0.45", lw=1.2)
            ax.plot(rn, V, "--", color=c, lw=1.2, alpha=0.8)
            ax.text(2.2, 8.0, r"surface $+4\pi r^2\gamma_{SL}$", fontsize=8.5, color="0.35", ha="left")
            ax.text(2.7, -7.6, "volume " r"$-\frac{4}{3}\pi r^3\Delta G_v$" "\n" r"($\Delta T$ = 100 K)", fontsize=8.5,
                    color=c, ha="left", va="center")
        ax.plot(rn, tot, color=c, lw=2.2, label=rf"total, $\Delta T$ = {dT} K")
        ax.plot([rs * 1e9] * 2, [-10, Gs], ":", color=c, lw=1)
        ax.plot(rs * 1e9, Gs, "o", color=c, ms=5, zorder=5)
        ax.annotate(rf"$r^*$ = {rs*1e9:.2f} nm" "\n" rf"$\Delta G^*$ = {Gs:.2f}×10$^{{-18}}$ J",
                    xy=(rs * 1e9, Gs), xytext=ann, fontsize=8, color=c,
                    arrowprops=dict(arrowstyle="-", color=c, lw=0.7))
        print(f"dT={dT}: r*={rs*1e9:.3f} nm  dG*={Gs:.3f}e-18 J")
    ax.text(1.0, -2.2, "embryos shrink\n($r<r^*$)", fontsize=8.5, ha="center", va="top")
    ax.text(4.5, 2.0, "nuclei grow ($r>r^*$)", fontsize=8.5, ha="center")
    ax.annotate("", xy=(0.6, -1.0), xytext=(1.7, -1.0), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1,
                                                                         mutation_scale=9))
    ax.annotate("", xy=(5.4, 1.2), xytext=(3.6, 1.2), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1,
                                                                       mutation_scale=9))
    ax.set_xlim(0, 6); ax.set_ylim(-10, 10)
    ax.set_xlabel("Cluster radius $r$ (nm)")
    ax.set_ylabel(r"$\Delta G$ ($10^{-18}$ J)")
    ax.legend(fontsize=8.5, loc="center right", bbox_to_anchor=(1.0, 0.42))
    ax.text(0.08, 9.7, "Cu:\n" r"$\gamma_{SL}$ = 0.177 J/m²" "\n" r"$\Delta H_v$ = 1.88×10$^9$ J/m³" "\n"
            r"$T_m$ = 1358 K", fontsize=7.5, color="0.3", va="top")
    save(fig, "09", "fig-9-1-nucleation-barrier")


# ---------------------------------------------------------------- Figure 9.2
def heterogeneous_nucleation():
    fig = plt.figure(figsize=(6.8, 3.4))
    a = fig.add_axes([0.01, 0.08, 0.40, 0.84])
    a.set_xlim(-1.6, 1.6); a.set_ylim(-0.45, 1.15); a.set_aspect("equal"); a.axis("off")
    a.add_patch(Rectangle((-1.6, -0.45), 3.2, 0.45, fc="0.82", ec="none"))
    a.plot([-1.6, 1.6], [0, 0], color=INK, lw=1)
    th = np.radians(60); Rr = 1.0
    zc = -Rr * np.cos(th)
    phi = np.linspace(np.pi / 2 - th, np.pi / 2 + th, 100)
    xs, ys = Rr * np.cos(phi), zc + Rr * np.sin(phi)
    a.add_patch(Polygon(np.c_[xs, ys], fc="#9CC3E4", ec=INK, lw=1.1))
    # radius of curvature
    a.plot([0, 0.55], [zc, zc + np.sqrt(1 - 0.55**2)], color="0.3", lw=0.8, ls="--")
    a.plot(0, zc, "o", color="0.3", ms=2.5)
    a.text(0.32, 0.12, "$r$", fontsize=9, color="0.3")
    xe = Rr * np.sin(th)
    # contact angle arc at right triple line (inside solid, between substrate and cap tangent)
    a.add_patch(Arc((xe, 0), 0.55, 0.55, theta1=180 - 60, theta2=180, color=INK, lw=1))
    a.text(xe - 0.42, 0.07, r"$\theta$", fontsize=10)
    # tension vectors at right triple line
    def vec(dx, dy, lab, off, c):
        a.add_patch(FancyArrowPatch((xe, 0), (xe + dx, dy), arrowstyle="-|>", mutation_scale=10, color=c, lw=1.4))
        a.text(xe + dx + off[0], dy + off[1], lab, fontsize=8.5, color=c)
    vec(0.6, 0, r"$\gamma_{LS'}$", (0.02, 0.06), COLORS[1])
    vec(-0.6, 0, r"$\gamma_{SS'}$", (-0.42, -0.2), COLORS[2])
    vec(-0.6 * np.cos(th), 0.6 * np.sin(th), r"$\gamma_{SL}$", (-0.32, 0.03), COLORS[0])
    a.text(-0.05, 0.22, "S", fontsize=11, ha="center")
    a.text(-1.2, 0.7, "L", fontsize=11)
    a.text(-0.95, -0.25, "substrate S′", fontsize=8.5, ha="center")
    a.text(-1.55, 1.12, r"(a) spherical cap: $\gamma_{LS'}=\gamma_{SS'}+\gamma_{SL}\cos\theta$", fontsize=8.5,
           va="top")
    b = fig.add_axes([0.53, 0.17, 0.38, 0.72])
    t = np.linspace(0.5, 180, 500)
    f = lambda d: (2 + np.cos(np.radians(d))) * (1 - np.cos(np.radians(d)))**2 / 4
    b.axvspan(0, 30, color=COLORS[2], alpha=0.15, lw=0)
    b.text(2, 2.2e-5, "potent nucleants\n(TiB$_2$/Al$_3$Ti in Al,\nAgI for ice)", fontsize=7, color="#006B4E",
           va="bottom")
    b.semilogy(t, f(t), color=COLORS[0])
    for d, lab in [(20, "0.0027"), (30, "0.013"), (90, "0.5")]:
        b.plot(d, f(d), "o", color=COLORS[1], ms=4.5, zorder=5)
        b.text(d + 4, f(d) * 0.55, f"θ = {d}°: f = {lab}", fontsize=7.5, va="top")
    b.set_xlim(0, 180); b.set_ylim(1e-5, 1.5)
    b.set_xticks([0, 30, 60, 90, 120, 150, 180])
    b.set_xlabel(r"Contact angle $\theta$ (°)")
    b.set_ylabel(r"$f(\theta)=\Delta G^*_{het}/\Delta G^*_{hom}$")
    sec = b.secondary_yaxis("right", functions=(np.sqrt, np.square))
    sec.set_ylabel(r"$\sqrt{f}$  (relative undercooling)", fontsize=9)
    b.spines["right"].set_visible(True)
    b.text(95, 2e-3, r"$f=\frac{(2+\cos\theta)(1-\cos\theta)^2}{4}$", fontsize=9)
    b.set_title("(b) barrier-reduction factor", loc="left", fontsize=9.5)
    save(fig, "09", "fig-9-2-heterogeneous-nucleation")


# ---------------------------------------------------------------- Figure 9.3
def _ttt_model(T, Te=1000.0):
    dT = np.maximum(Te - T, 1e-6)
    Q, A, B = 9000.0, 3.0e7, 8.0
    I = np.exp(-A / (dT**2 * T)) * np.exp(-Q / T)
    v = np.exp(-Q / T) * (1 - np.exp(-B * dT / T))
    return I, v


def jmak_ttt():
    fig = plt.figure(figsize=(6.8, 3.6))
    gs = GridSpec(1, 3, figure=fig, width_ratios=[3.0, 0.9, 2.6], wspace=0.08)
    a = fig.add_subplot(gs[0])
    t = np.logspace(-1, 3, 400)
    for n, c in [(1, COLORS[0]), (1.72, COLORS[1]), (4, COLORS[2])]:
        k = np.log(2) / 30**n
        a.semilogx(t, 1 - np.exp(-k * t**n), color=c, label=f"n = {n:g}")
    a.plot([10, 60], [0.10, 0.90], "o", color=COLORS[1], ms=5, mec=INK, mew=0.6, zorder=5)
    a.text(11, 0.07, "10 min, 10 %", fontsize=7.5, va="top")
    a.text(55, 0.93, "60 min, 90 %", fontsize=7.5, ha="right", va="bottom")
    a.axhline(0.5, color="0.7", lw=0.7, ls=":"); a.axvline(30, color="0.7", lw=0.7, ls=":")
    a.text(32, 0.47, "$t_{50}$ = 30 min", fontsize=7.5, va="top")
    a.set_xlim(0.1, 1000); a.set_ylim(0, 1.05)
    a.set_xlabel("Time (min)"); a.set_ylabel("Fraction transformed $f$")
    a.legend(fontsize=8, loc="upper left")
    a.set_title(r"(a) JMAK: $f=1-\exp(-kt^n)$", loc="left", fontsize=9.5)
    # rates
    Te = 1000.0
    T = np.linspace(560, 999, 600)
    I, v = _ttt_model(T, Te)
    b = fig.add_subplot(gs[1])
    b.plot(I / I.max(), T, color=COLORS[3], label="$I$")
    b.plot(v / v.max(), T, color=COLORS[4], label="$v$")
    b.set_ylim(560, 1010); b.set_xlim(0, 1.15)
    b.set_xticks([]); b.set_yticks([Te]); b.set_yticklabels(["$T_e$"])
    b.axhline(Te, color="0.5", lw=0.8, ls="--")
    b.text(0.66, 575, "nucleation\nrate $I$", fontsize=7, color=COLORS[3], ha="center", va="bottom")
    b.text(0.60, T[v.argmax()] + 12, "growth\nrate $v$", fontsize=7, color=COLORS[4], ha="center", va="bottom")
    b.set_xlabel("rate", fontsize=8.5)
    b.set_ylabel("Temperature →", fontsize=9)
    b.set_title("(b)", loc="left", fontsize=9.5)
    c = fig.add_subplot(gs[2], sharey=b)
    c.tick_params(labelleft=False)
    tf = lambda f: (-np.log(1 - f) * 3 / (np.pi * I * v**3)) ** 0.25
    t1, t99 = tf(0.01), tf(0.99)
    norm = t1.min()
    t1, t99 = t1 / norm, t99 / norm
    c.semilogx(t1, T, color=COLORS[0], label="1 %")
    c.semilogx(t99, T, color=COLORS[1], label="99 %")
    i = t1.argmin()
    c.plot(t1[i], T[i], "o", color=INK, ms=4)
    c.text(t1[i] * 0.75, T[i], "nose", fontsize=8, ha="right", va="center")
    # critical cooling path: T = Te - Rc t tangent to the 1 % curve
    Rc = np.max((Te - T) / t1)
    tt = np.logspace(-2, 3, 400)
    c.semilogx(tt, Te - Rc * 1.05 * tt, "--", color=INK, lw=1.1)
    c.annotate("critical\ncooling rate", xy=(1.6, 800), xytext=(0.012, 700), fontsize=7.5, ha="left",
               arrowprops=dict(arrowstyle="-", color=INK, lw=0.6))
    c.axhline(Te, color="0.5", lw=0.8, ls="--")
    c.set_xlim(1e-2, 1e3)
    c.set_xlabel("log time (a.u.)")
    c.legend(fontsize=8, loc="center right", title="transformed", title_fontsize=7.5)
    c.text(30, 975, "slow: small\ndriving force", fontsize=7, va="top")
    c.text(0.012, 590, "slow: low\nmobility", fontsize=7)
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.14, top=0.9)
    save(fig, "09", "fig-9-3-jmak-ttt")


# ---------------------------------------------------------------- Figure 9.4
def _interface(ax, x0, kind, rng):
    """Draw a solid (bottom) / liquid (top) interface sketch in a 2-unit-wide box at x0."""
    w, h = 2.0, 2.2
    ax.add_patch(Rectangle((x0, 0), w, h, fc="white", ec="0.5", lw=0.8))
    xs = np.linspace(x0, x0 + w, 300)
    if kind == "planar":
        y = np.full_like(xs, 1.0)
        ax.fill_between(xs, 0, y, color="#9CC3E4", lw=0)
        ax.plot(xs, y, color=INK, lw=1)
    elif kind == "cellular":
        y = 1.0 + 0.25 * np.abs(np.cos(np.pi * (xs - x0) / 0.4)) ** 0.5
        ax.fill_between(xs, 0, y, color="#9CC3E4", lw=0)
        ax.plot(xs, y, color=INK, lw=1)
    elif kind == "columnar":
        ax.fill_between(xs, 0, 0.6, color="#9CC3E4", lw=0)
        for cx in np.arange(x0 + 0.25, x0 + w, 0.5):
            ax.add_patch(Polygon([[cx - 0.05, 0.6], [cx, 1.75], [cx + 0.05, 0.6]], fc="#9CC3E4", ec=INK, lw=0.7))
            for yy in np.arange(0.75, 1.6, 0.17):
                L = 0.17 * (1.75 - yy) / 1.0
                ax.plot([cx - L, cx + L], [yy, yy], color=INK, lw=0.7)
        ax.plot([x0, x0 + w], [0.6, 0.6], color=INK, lw=0.8)
    else:  # equiaxed
        for (ex, ey) in [(0.45, 0.6), (1.4, 0.55), (0.9, 1.5), (1.6, 1.6), (0.3, 1.65)]:
            cx, cy = x0 + ex, ey
            rot = rng.uniform(0, np.pi / 2)
            for k in range(4):
                ang = rot + k * np.pi / 2
                L = 0.28
                ax.plot([cx, cx + L * np.cos(ang)], [cy, cy + L * np.sin(ang)], color=INK, lw=1.4)
                for s in (0.1, 0.18):
                    bx, by = cx + s * np.cos(ang), cy + s * np.sin(ang)
                    l2 = 0.07
                    ax.plot([bx - l2 * np.sin(ang), bx + l2 * np.sin(ang)],
                            [by + l2 * np.cos(ang), by - l2 * np.cos(ang)], color=INK, lw=0.7)
    lab = {"planar": "planar", "cellular": "cellular", "columnar": "columnar\ndendritic",
           "equiaxed": "equiaxed\ndendritic"}[kind]
    ax.text(x0 + w / 2, -0.15, lab, ha="center", va="top", fontsize=8.5)


def constitutional_supercooling():
    fig = plt.figure(figsize=(6.8, 4.6))
    k, C0, m, Tm, DL = 0.17, 4.5, 3.4, 660.0, 3e-9
    xp = np.linspace(0, 4, 300)   # x' in units of D_L/V
    CL = C0 * (1 + (1 - k) / k * np.exp(-xp))
    TL = Tm - m * CL
    a = fig.add_axes([0.09, 0.56, 0.38, 0.38])
    a.plot(xp, CL, color=COLORS[0])
    a.axhline(C0, color="0.6", lw=0.8, ls="--")
    a.text(3.95, C0 + 0.6, "$C_0$ = 4.5", fontsize=8, ha="right", va="bottom")
    a.text(0.08, C0 / k, "$C_0/k$ = 26.5", fontsize=8, va="center", ha="left")
    a.annotate("", xy=(1, 2), xytext=(0, 2), arrowprops=dict(arrowstyle="<|-|>", lw=0.8, color=INK,
                                                             mutation_scale=7))
    a.text(0.5, 2.6, "$D_L/V$", fontsize=8, ha="center", va="bottom")
    a.set_xlim(0, 4); a.set_ylim(0, 30)
    a.set_xlabel("Distance ahead of interface $x'$ (units of $D_L/V$)", fontsize=8.5)
    a.set_ylabel("$C_L$ (wt% Cu)")
    a.set_title("(a) solute pile-up", loc="left", fontsize=9.5)
    b = fig.add_axes([0.59, 0.56, 0.38, 0.38])
    b.plot(xp, TL, color=COLORS[1], lw=2, label="local liquidus $T_L(x')$")
    T0 = TL[0]
    slope0 = m * C0 * (1 - k) / k        # dT_L/dx' at interface (K per D_L/V)
    steep = T0 + 1.3 * slope0 * xp
    shallow = T0 + 0.25 * slope0 * xp
    b.plot(xp, steep, color=INK, lw=1.2, label="steep $G$: stable")
    b.plot(xp, shallow, "--", color=INK, lw=1.2, label="shallow $G$")
    b.fill_between(xp, shallow, TL, where=TL > shallow, color=COLORS[5], alpha=0.35, lw=0)
    b.text(2.1, 618, "constitutionally\nsupercooled", fontsize=7.5, ha="center", color="#1F6F9F")
    b.axhline(Tm - m * C0, color="0.6", lw=0.8, ls=":")
    b.text(3.95, Tm - m * C0 + 1.5, "liquidus of $C_0$ (645 °C)", fontsize=7, ha="right", va="bottom")
    b.text(3.95, T0 + 1, "solidus of $C_0$ (570 °C)", fontsize=7, ha="right", va="bottom")
    b.axhline(T0, color="0.6", lw=0.8, ls=":")
    b.set_xlim(0, 4); b.set_ylim(565, 660)
    b.set_xlabel("$x'$ (units of $D_L/V$)", fontsize=8.5)
    b.set_ylabel("Temperature (°C)")
    b.legend(fontsize=7, loc="lower right", bbox_to_anchor=(1.0, 0.07))
    b.set_title("(b) liquidus vs actual temperature", loc="left", fontsize=9.5)
    # morphologies
    c = fig.add_axes([0.02, 0.02, 0.96, 0.34])
    c.set_xlim(0, 13); c.set_ylim(-1.4, 3.6); c.set_aspect("equal"); c.axis("off")
    rng = np.random.default_rng(2)
    for i, kind in enumerate(["planar", "cellular", "columnar", "equiaxed"]):
        _interface(c, 0.5 + 2.6 * i, kind, rng)
    c.annotate("", xy=(10.8, 2.75), xytext=(0.5, 2.75), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.2,
                                                                       mutation_scale=10))
    c.text(5.6, 2.85, "decreasing $G/V$ (more constitutional supercooling)", fontsize=8.5, ha="center",
           va="bottom")
    c.text(10.9, 1.9, "Al–4.5Cu:\n$\\Delta T_0$ = 75 K\ncritical $G/V$ =\n2.5×10$^{10}$ K s/m²\n\n"
           "$GV$ ↑ → finer\nspacing", fontsize=7.5, va="top")
    save(fig, "09", "fig-9-4-constitutional-supercooling")


# ---------------------------------------------------------------- Figure 9.5
def scheil_vs_lever():
    fig, ax = new_fig(6.4, 4.2)
    k, C0, CE = 0.17, 4.5, 33.2
    fe = 1 - (CE / C0) ** (1 / (k - 1))
    fs = np.linspace(0, fe, 400)
    CSs = k * C0 * (1 - fs) ** (k - 1)
    CLs = C0 * (1 - fs) ** (k - 1)
    f2 = np.linspace(0, 1, 400)
    CLe = C0 / (1 - f2 * (1 - k))
    CSe = k * CLe
    ax.axvspan(fe, 1, color=COLORS[6], alpha=0.35, lw=0)
    ax.text((fe + 1) / 2, 20, "non-equilibrium\neutectic (Scheil)\n9 %", fontsize=7.5, ha="center",
            rotation=90, va="center")
    ax.axhline(CE, color="0.4", ls="--", lw=1)
    ax.text(0.02, CE + 0.4, "eutectic 33.2 wt% Cu (548 °C)", fontsize=8, va="bottom")
    ax.plot(fs, CLs, color=COLORS[1], lw=2, label="$C_L$, Scheil")
    ax.plot(fs, CSs, color=COLORS[0], lw=2, label="$C_S$, Scheil")
    ax.plot(f2, CLe, "--", color=COLORS[1], lw=1.4, label="$C_L$, lever rule")
    ax.plot(f2, CSe, "--", color=COLORS[0], lw=1.4, label="$C_S$, lever rule")
    for f, cs in [(0, 0.77), (0.5, 1.36), (0.9, 5.2)]:
        ax.plot(f, k * C0 * (1 - f) ** (k - 1), "o", color=COLORS[0], ms=4.5, zorder=5)
        ax.text(f - 0.012 if f > 0.8 else f + 0.012, k * C0 * (1 - f) ** (k - 1) + 0.5, f"{cs}", fontsize=7.5,
                color=COLORS[0], va="bottom", ha="right" if f > 0.8 else "left")
    ax.plot(1, 4.5, "s", color=COLORS[0], ms=4.5, zorder=5)
    ax.annotate("4.5 at $f_s$ = 1", xy=(0.995, 4.4), xytext=(0.80, 1.2), fontsize=7.5, color=COLORS[0],
                arrowprops=dict(arrowstyle="-", color=COLORS[0], lw=0.6))
    ax.plot(fe, CE, "o", color=COLORS[1], ms=5, zorder=5)
    ax.text(fe - 0.01, CE - 0.8, "$f_s$ = 0.91", fontsize=7.5, ha="right", va="top", color=COLORS[1])
    ax.set_xlim(0, 1); ax.set_ylim(0, 35)
    ax.set_xlabel("Fraction solid $f_s$"); ax.set_ylabel("Cu (wt%)")
    ax.legend(fontsize=8, loc="center left", bbox_to_anchor=(0.0, 0.62))
    # inset: cored dendrite
    ins = ax.inset_axes([0.36, 0.30, 0.30, 0.42])
    n = 260
    X, Y = np.meshgrid(np.linspace(-1, 1, n), np.linspace(-1, 1, n))
    d = np.full_like(X, 9.0)
    def seg(x0, y0, x1, y1):
        dx, dy = x1 - x0, y1 - y0
        t = np.clip(((X - x0) * dx + (Y - y0) * dy) / (dx * dx + dy * dy), 0, 1)
        return np.hypot(X - (x0 + t * dx), Y - (y0 + t * dy))
    for ang in np.arange(4) * np.pi / 2 + 0.3:
        d = np.minimum(d, seg(0, 0, 0.95 * np.cos(ang), 0.95 * np.sin(ang)))
        for s in np.arange(0.18, 0.9, 0.16):
            bx, by = s * np.cos(ang), s * np.sin(ang)
            L = 0.24 * (1 - 0.7 * s)
            for sg in (1, -1):
                d = np.minimum(d, seg(bx, by, bx + sg * L * np.cos(ang + np.pi / 2), by + sg * L * np.sin(ang + np.pi / 2)))
    conc = np.clip(d / 0.12, 0, 1)
    ins.imshow(conc, extent=(-1, 1, -1, 1), cmap="YlOrBr", vmin=-0.1, vmax=1.15, origin="lower")
    ins.set_xticks([]); ins.set_yticks([])
    ins.set_title("cored dendrite: Cu-rich\ninterdendritic regions (dark)", fontsize=7)
    save(fig, "09", "fig-9-5-scheil-vs-lever")


# ---------------------------------------------------------------- Figure 9.6
def _voronoi_segments(seeds):
    vor = Voronoi(seeds)
    segs = []
    for rv in vor.ridge_vertices:
        if -1 in rv:
            continue
        segs.append(vor.vertices[rv])
    return segs


def casting_macrostructure():
    fig = plt.figure(figsize=(6.8, 5.0))
    ax = fig.add_axes([0.02, 0.33, 0.96, 0.64])
    ax.set_xlim(-75, 75); ax.set_ylim(-56, 60); ax.set_aspect("equal"); ax.axis("off")
    R0, Rch, Req = 50.0, 47.5, 13.0
    from matplotlib.collections import LineCollection
    # left half: no refiner
    ax.add_patch(Wedge((0, 0), R0, 90, 270, fc="#E9EEF3", ec="none"))
    rng = np.random.default_rng(5)
    # chill zone (drawn thicker than 1 mm for visibility)
    for ang in np.linspace(90, 270, 70):
        a = np.radians(ang)
        ax.plot([Rch * np.cos(a), R0 * np.cos(a)], [Rch * np.sin(a), R0 * np.sin(a)], color="0.45", lw=0.4)
    # columnar grains: radial wedges with jittered boundaries
    angs = np.sort(rng.uniform(92, 268, 44))
    for ang in angs:
        a1 = np.radians(ang)
        ra = np.linspace(Req, Rch, 20)
        jit = np.radians(rng.normal(0, 1.2)) * (1 - (ra - Req) / (Rch - Req))
        ax.plot(ra * np.cos(a1 + jit), ra * np.sin(a1 + jit), color="0.25", lw=0.7)
    # equiaxed centre
    seeds = rng.uniform(-Req, Req, (60, 2))
    seeds = seeds[(seeds[:, 0] < 0) & (np.hypot(*seeds.T) < Req)]
    segs = _voronoi_segments(np.vstack([seeds, rng.uniform(-30, 30, (40, 2))]))
    clip_c = Wedge((0, 0), Req, 90, 270, transform=ax.transData)
    lc = LineCollection(segs, colors="0.25", linewidths=0.6)
    ax.add_collection(lc); lc.set_clip_path(clip_c)
    ax.add_patch(Wedge((0, 0), Req, 90, 270, fc="none", ec="0.25", lw=0.6, ls=":"))
    # hot tear between columnar grains
    a = np.radians(angs[8]); ra = np.linspace(20, 34, 10)
    ax.plot(ra * np.cos(a), ra * np.sin(a), color=COLORS[1], lw=2.2)
    ax.annotate("hot tears between\ncolumnar grains", xy=(27 * np.cos(a), 27 * np.sin(a)), xytext=(-74, -45),
                fontsize=7.5, color=COLORS[1], arrowprops=dict(arrowstyle="-", color=COLORS[1], lw=0.7))
    ax.annotate("chill zone (~1 mm,\nfine grains)", xy=(-49 * np.cos(np.radians(40)), 49 * np.sin(np.radians(40))),
                xytext=(-74, 38), fontsize=7.5, arrowprops=dict(arrowstyle="-", color=INK, lw=0.7))
    ax.annotate("columnar zone\n(tens of mm)", xy=(-30, 8), xytext=(-74, 22), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", color=INK, lw=0.7))
    ax.annotate("equiaxed zone", xy=(-6, -4), xytext=(-74, -2), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", color=INK, lw=0.7))
    ax.annotate("", xy=(-38 * np.cos(np.radians(25)), -38 * np.sin(np.radians(25))),
                xytext=(-48 * np.cos(np.radians(25)), -48 * np.sin(np.radians(25))),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.2, mutation_scale=9))
    ax.text(-74, -26, "⟨100⟩ ∥ heat flow", fontsize=7.5, color=COLORS[0])
    # right half: refined
    ax.add_patch(Wedge((0, 0), R0, -90, 90, fc="#EEF5EC", ec="none"))
    pts = []
    while len(pts) < 900:
        p = rng.uniform(-2, R0 + 2, 2) * [1, 1]
        p[1] = rng.uniform(-R0 - 2, R0 + 2)
        if np.hypot(*p) < R0 + 2:
            pts.append(p)
    segs = _voronoi_segments(np.array(pts))
    clip_r = Wedge((0, 0), R0, -90, 90, transform=ax.transData)
    lc2 = LineCollection(segs, colors="0.35", linewidths=0.35)
    ax.add_collection(lc2); lc2.set_clip_path(clip_r)
    ax.add_patch(Circle((0, 0), R0, fc="none", ec=INK, lw=1.2))
    ax.plot([0, 0], [-R0, R0], color=INK, lw=1.2)
    ax.text(-25, 53, "no refiner", fontsize=9.5, ha="center")
    ax.text(25, 53, "with Al–5Ti–1B", fontsize=9.5, ha="center")
    ax.annotate("fine equiaxed grains\n~150 µm (schematic)", xy=(35, -20), xytext=(52, -45), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", color=INK, lw=0.7))
    ax.annotate("", xy=(-R0, -54), xytext=(R0, -54), arrowprops=dict(arrowstyle="<|-|>", color="0.4", lw=0.8,
                                                                     mutation_scale=7))
    ax.text(0, -55, "≈100 mm", fontsize=7.5, ha="center", va="top", color="0.4",
            bbox=dict(fc="white", ec="none", pad=0.5))
    # cooling-rate bar
    b = fig.add_axes([0.08, 0.10, 0.86, 0.08])
    b.set_xscale("log"); b.set_xlim(0.1, 1e6); b.set_ylim(0, 1)
    b.set_yticks([])
    for s in ["left", "right", "top"]:
        b.spines[s].set_visible(False)
    procs = [(0.3, 3, "sand\ncasting", COLORS[4]), (3, 30, "permanent\nmould", COLORS[2]),
             (30, 300, "pressure\ndie casting", COLORS[0]), (1e3, 1e6, "atomization, additive manufacturing (sub-µm cells)", COLORS[3])]
    for lo, hi, lab, c in procs:
        b.add_patch(Rectangle((lo, 0.1), hi - lo, 0.8, fc=c, alpha=0.35, ec=c))
        b.text(np.sqrt(lo * hi), 0.5, lab, ha="center", va="center", fontsize=7.3)
    b.set_xlabel("Cooling rate (K/s)", fontsize=9)
    top = b.secondary_xaxis("top", functions=(lambda r: 50 * np.asarray(r) ** (-1 / 3),
                                              lambda l: (50 / np.asarray(l)) ** 3))
    top.set_ticks([100, 50, 20, 10, 5, 2, 1, 0.5])
    top.set_xticklabels(["100", "50", "20", "10", "5", "2", "1", "0.5"])
    top.set_xlabel(r"secondary dendrite arm spacing $\lambda_2$ (µm), $\lambda_2\approx50\,\dot T^{-1/3}$",
                   fontsize=8.5)
    top.tick_params(labelsize=8)
    save(fig, "09", "fig-9-6-casting-macrostructure")


if __name__ == "__main__":
    nucleation_barrier()
    heterogeneous_nucleation()
    jmak_ttt()
    constitutional_supercooling()
    scheil_vs_lever()
    casting_macrostructure()
