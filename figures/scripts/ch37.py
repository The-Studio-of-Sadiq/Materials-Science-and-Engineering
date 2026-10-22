"""Figures for Chapter 37 — Smart and Soft Materials.

Run from the repository root:  python figures/scripts/ch37.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, Ellipse, FancyArrowPatch, Wedge
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D
from scipy.integrate import quad
from scipy.optimize import brentq


# ---------------------------------------------------------------- Figure 37.1
def actuator_map():
    fig, ax = new_fig(6.6, 4.8)
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlim(1e-4, 1); ax.set_ylim(0.01, 1000)
    # constant work-density lines  w = sigma*eps/4
    e = np.logspace(-4, 0, 50)
    for W, lab, ep in ((1e3, r"$10^3$", 1.5e-3), (1e4, r"$10^4$", 3e-3), (1e5, r"$10^5$", 0.02),
                       (1e6, r"$10^6$", 0.15), (1e7, r"$10^7$ J/m$^3$", 0.5)):
        s = 4 * W / e / 1e6
        ax.plot(e, s, ls="--", color="0.6", lw=0.8, zorder=1)
        ax.text(ep, 4 * W / ep / 1e6 * 1.12, lab, fontsize=7.5, color="0.4", rotation=-36, ha="center",
                va="bottom", zorder=1)
    ax.text(1.3e-4, 0.016, r"dashed: $w=\sigma_{\rm bl}\,\varepsilon_{\max}/4$", fontsize=7.8, color="0.35")

    fams = [  # name, eps range, sigma range (MPa), colour, bandwidth, label position (x, y), ha
        ("NiTi SMA", (0.02, 0.08), (100, 600), COLORS[1], "0.1–10 Hz", (0.09, 250), "left"),
        ("Ni–Mn–Ga\nMSM", (0.03, 0.1), (1, 3), COLORS[3], "≤1 kHz", (0.027, 2.3), "right"),
        ("Terfenol-D", (1e-3, 2e-3), (50, 100), COLORS[2], "~10 kHz", (2.2e-3, 105), "left"),
        ("PZT stack", (1e-3, 1.5e-3), (30, 50), COLORS[0], "10–100 kHz", (8.8e-4, 38), "right"),
        ("dielectric\nelastomers", (0.1, 1.0), (0.1, 3), COLORS[4], "10 Hz–1 kHz", (0.32, 7.0), "center"),
        ("IPMC /\nconducting\npolymers", (0.005, 0.03), (0.1, 1), COLORS[5], "0.1–10 Hz", (4.4e-3, 0.32), "right"),
        ("skeletal\nmuscle", (0.2, 0.4), (0.1, 0.35), "#8C564B", "~10 Hz", (0.28, 0.05), "center"),
    ]
    for name, (e0, e1), (s0, s1), c, bw, (lx, ly), ha in fams:
        cx, cy = np.sqrt(e0 * e1), np.sqrt(s0 * s1)
        rx = max(np.log10(e1 / e0) / 2, 0.08)
        ry = max(np.log10(s1 / s0) / 2, 0.08)
        t = np.linspace(0, 2 * np.pi, 200)
        xs = 10**(np.log10(cx) + rx * np.cos(t))
        ys = 10**(np.log10(cy) + ry * np.sin(t))
        ax.fill(xs, ys, color=c, alpha=0.35, lw=0, zorder=2)
        ax.plot(xs, ys, color=c, lw=1.2, zorder=3)
        ax.text(lx, ly, f"{name}\n({bw})", fontsize=7.8, ha=ha, va="center", color=INK, zorder=5,
                linespacing=1.05)
    # thermal expansion of steel (Delta T = 100 K)
    ax.plot(1.2e-3, 250, "s", ms=6, color="0.3", zorder=4)
    ax.text(1.0e-3, 290, "thermal expansion,\nsteel ΔT=100 K (slow)", fontsize=7.8, ha="right", va="bottom")
    ax.set_xlabel(r"free strain $\varepsilon_{\max}$")
    ax.set_ylabel(r"blocking stress $\sigma_{\rm bl}$ (MPa)")
    ax.set_xticks([1e-4, 1e-3, 1e-2, 1e-1, 1])
    ax.set_xticklabels(["0.01 %", "0.1 %", "1 %", "10 %", "100 %"])
    ax.set_yticks([0.01, 0.1, 1, 10, 100, 1000])
    ax.set_yticklabels(["0.01", "0.1", "1", "10", "100", "1000"])
    save(fig, "37", "fig-37-1-actuator-map")


# ---------------------------------------------------------------- Figure 37.2
def _lattice_sketch(ax, kind):
    """Small crystal sketch drawn in its own axes (unit cells of size 1)."""
    ax.set_aspect("equal"); ax.axis("off")
    if kind == "aus":
        for i in range(3):
            for j in range(3):
                ax.add_patch(Rectangle((i, j), 1, 1, fc="#DCE9F5", ec=INK, lw=0.6))
        ax.set_xlim(-0.6, 3.6); ax.set_ylim(-0.3, 3.3)
        return
    sh, hgt = 0.45, 0.8
    for j in range(4):
        sign = 1 if (kind == "detw" or j % 2 == 0) else -1
        xoff = j * sh if kind == "detw" else (0 if j % 2 == 0 else sh)
        for i in range(3):
            xb = i + xoff
            ax.add_patch(Polygon([(xb, j * hgt), (xb + 1, j * hgt), (xb + 1 + sign * sh, (j + 1) * hgt),
                                  (xb + sign * sh, (j + 1) * hgt)],
                                 fc="#F6DCC8" if kind == "tw" else "#F2C7A5", ec=INK, lw=0.6))
    ax.set_xlim(-0.6, 5.0 if kind == "detw" else 3.9); ax.set_ylim(-0.3, 3.5)


def sma_cycle_superelastic():
    from mpl_toolkits.mplot3d import proj3d
    fig = plt.figure(figsize=(6.8, 5.0))
    ax = fig.add_axes([0.0, 0.02, 0.56, 0.86], projection="3d")
    ax.set_axis_off()
    Thot, Tc = 70.0, -10.0
    Mf, Ms, As, Af = 10, 25, 35, 50
    T1 = np.linspace(Thot, Tc, 30)
    seg1 = np.c_[np.zeros_like(T1), T1, np.zeros_like(T1)]
    e2 = np.r_[np.linspace(0, 0.4, 6), np.linspace(0.4, 6.0, 30)]
    s2 = np.where(e2 <= 0.4, e2 / 0.4 * 140, 140 + (e2 - 0.4) / 5.6 * 20)
    seg2 = np.c_[e2, np.full_like(e2, Tc), s2]
    seg3 = np.c_[np.linspace(6.0, 5.5, 8), np.full(8, Tc), np.linspace(160, 0, 8)]
    T4 = np.linspace(Tc, Thot, 60)
    rec = np.clip((T4 - As) / (Af - As), 0, 1)
    seg4 = np.c_[5.5 * (1 - rec), T4, np.zeros_like(T4)]
    ax.set_xlim(0, 7); ax.set_ylim(Tc, Thot + 10); ax.set_zlim(0, 170)
    ax.set_box_aspect((1.0, 1.0, 0.75))
    ax.view_init(elev=20, azim=-62)
    # own axes
    O = (0, Tc, 0)
    for end, lab in (((7.3, Tc, 0), "strain (%)"), ((0, Thot + 14, 0), "temperature"), ((0, Tc, 180), "stress")):
        ax.plot([O[0], end[0]], [O[1], end[1]], [O[2], end[2]], color="0.4", lw=1.0)
    for e_ in (2, 4, 6):
        ax.plot([e_, e_], [Tc, Tc - 3], [0, 0], color="0.4", lw=0.8)
    for s_ in (100, 150):
        ax.plot([0, -0.2], [Tc, Tc], [s_, s_], color="0.4", lw=0.8)
    # floor guides for transformation temperatures
    for Tm in (Mf, Ms, As, Af):
        ax.plot([0, 6.2], [Tm, Tm], [0, 0], color="0.75", lw=0.6, ls=":")
    cols = [COLORS[0], COLORS[1], COLORS[1], COLORS[2]]
    for seg, c in zip((seg1, seg2, seg3, seg4), cols):
        ax.plot(seg[:, 0], seg[:, 1], seg[:, 2], color=c, lw=2.2)
    for p in (seg1[0], seg1[-1], seg2[-1], seg3[-1]):
        ax.scatter(*p, color=INK, s=12, depthshade=False)
    fig.canvas.draw()

    def fxy(p):
        x2, y2, _ = proj3d.proj_transform(p[0], p[1], p[2], ax.get_proj())
        return fig.transFigure.inverted().transform(ax.transData.transform((x2, y2)))

    for seg, c in zip((seg1, seg2, seg3, seg4), cols):
        m = len(seg) // 2 if seg is not seg4 else 40
        fig.add_artist(FancyArrowPatch(fxy(seg[m - 1]), fxy(seg[m + 1]), transform=fig.transFigure,
                                       arrowstyle="-|>", mutation_scale=13, color=c, lw=0.1))
    def ftext(p, txt, dx=0, dy=0, **kw):
        xy = fxy(p)
        fig.text(xy[0] + dx, xy[1] + dy, txt, **kw)
    ftext((7.3, Tc, 0), "strain (%)", 0.035, -0.02, fontsize=8, ha="center", color="0.25")
    ftext((0, Thot + 14, 0), "temperature", 0.005, 0.0, fontsize=8, ha="left", color="0.25")
    ftext((0, Tc, 180), "stress (MPa)", 0.0, 0.012, fontsize=8, ha="center", color="0.25")
    for e_ in (2, 4, 6):
        ftext((e_, Tc - 4, 0), str(e_), 0, -0.02, fontsize=7, ha="center", color="0.3")
    for s_ in (100, 150):
        ftext((-0.25, Tc, s_), f"{s_}", -0.005, 0, fontsize=7, ha="right", va="center", color="0.3")
    for Tm, lab in ((Mf, "$M_f$"), (Ms, "$M_s$"), (As, "$A_s$"), (Af, "$A_f$")):
        ftext((6.25, Tm, 0), lab, 0.003, 0, fontsize=7.5, ha="left", va="center", color="0.3")
    ftext(seg1[22], "1 cool:\nno shape change", 0.0, -0.034, fontsize=7.8, color=COLORS[0], ha="left",
          va="center")
    ftext(seg2[22], "2 load: detwinning,\n~150 MPa plateau", 0.0, 0.03, fontsize=7.8, color=COLORS[1],
          ha="center", va="bottom")
    ftext(seg3[-1], "3 unload:\n5.5 % retained", -0.01, -0.02, fontsize=7.8, color=COLORS[1], ha="right",
          va="top")
    fig.text(0.47, 0.375, "4 heat: strain\nrecovers between\n$A_s$ and $A_f$", fontsize=7.8, color=COLORS[2],
             ha="left", va="top")

    def sketch(p, kind, label, dx, dy, w=0.085):
        xy = fxy(p)
        a_ = fig.add_axes([xy[0] + dx, xy[1] + dy, w, w * 0.9])
        _lattice_sketch(a_, kind)
        fig.text(xy[0] + dx + w / 2, xy[1] + dy + w * 0.93, label, fontsize=7, ha="center", va="bottom")
    sketch(seg1[0], "aus", "austenite (cubic)", -0.045, 0.025)
    sketch(seg1[-1], "tw", "twinned martensite", -0.10, -0.16)
    sketch(seg2[-1], "detw", "detwinned", -0.03, 0.04, w=0.10)
    fig.text(0.01, 0.955, "(a) one-way shape-memory effect", fontsize=9.5)

    # (b) superelastic curves
    bx = fig.add_axes([0.62, 0.42, 0.36, 0.50])
    EA, EM = 50e3, 30e3
    for T, c in ((20, COLORS[0]), (37, COLORS[2]), (60, COLORS[1])):
        sU = 6.5 * (T + 20)
        sL = sU - 200
        e_s = sU / EA * 100
        e_p = e_s + 6.0
        s_end = sU + 25
        e_max = e_p + 0.4
        s_max = s_end + EM * 0.004
        eL_end = e_max - (s_max - sL - 20) / EM * 100
        bx.plot([0, e_s, e_p, e_max], [0, sU, s_end, s_max], color=c, lw=1.8)
        bx.plot([e_max, eL_end, sL / EA * 100 + 0.5, sL / EA * 100, 0], [s_max, sL + 20, sL, sL, 0],
                color=c, lw=1.2)
        bx.text(e_s + 0.25, sU + 14, f"{T} °C: {sU:.0f} MPa", color=c, fontsize=7.8, ha="left", va="bottom")
    bx.set_xlim(0, 8); bx.set_ylim(0, 700)
    bx.set_xlabel("strain (%)", fontsize=9)
    bx.set_ylabel("stress (MPa)", fontsize=9)
    bx.tick_params(labelsize=8)
    bx.set_title("(b) superelastic NiTi", fontsize=9.5, loc="left")
    bx.text(7.9, 15, "lower plateaus\n≈200 MPa below", fontsize=7, ha="right", va="bottom", color="0.3")

    cx = fig.add_axes([0.62, 0.08, 0.36, 0.22])
    Tl = np.linspace(-20, 80, 50)
    cx.plot(Tl, 6.5 * (Tl + 20), color=INK, lw=1.4)
    cx.axvspan(80, 100, color="#F3C9C9", lw=0)
    cx.text(90, 330, "slip:\nno super-\nelasticity", fontsize=6.8, ha="center", va="center", color="#8B1A1A")
    for T, c in ((20, COLORS[0]), (37, COLORS[2]), (60, COLORS[1])):
        cx.plot(T, 6.5 * (T + 20), "o", color=c, ms=4)
    cx.text(0, 420, "slope 6.5 MPa/K", fontsize=7.5)
    cx.text(-18, 40, "$M_s$ = −20 °C", fontsize=7.2)
    cx.text(78, 40, "$M_d$", fontsize=7.5, ha="right")
    cx.set_xlim(-30, 100); cx.set_ylim(0, 750)
    cx.set_xticks([-20, 0, 20, 37, 60, 80]); cx.set_yticks([0, 300, 600])
    cx.tick_params(labelsize=7.5)
    cx.set_xlabel("temperature (°C)", fontsize=8.5)
    cx.set_ylabel("plateau (MPa)", fontsize=8, labelpad=2)
    save(fig, "37", "fig-37-2-sma-cycle-superelastic")


# ---------------------------------------------------------------- Figure 37.3
def dlvo_potential():
    kT = 1.380649e-23 * 298.15
    e0, er, R, A, psi = 8.854e-12, 78.5, 50e-9, 1e-20, 0.030
    h = np.linspace(0.05, 20, 4000) * 1e-9
    VA = -A * R / (12 * h) / kT
    fig, ax = new_fig(6.6, 4.3)
    ax.axhline(0, color="0.5", lw=0.6)
    cols = [COLORS[0], COLORS[2], COLORS[1]]
    for c_, col, lab in ((1e-3, cols[0], "1 mM"), (1e-2, cols[1], "10 mM"), (1e-1, cols[2], "100 mM")):
        kap = np.sqrt(c_) / 0.304e-9
        VR = 2 * np.pi * e0 * er * R * psi**2 * np.log(1 + np.exp(-kap * h)) / kT
        V = VA + VR
        ax.plot(h * 1e9, V, color=col, lw=2, label=f"NaCl {lab} (Debye length {0.304 / np.sqrt(c_):.2g} nm)")
        m = h > 0.3e-9
        i = np.argmax(V[m])
        hb, Vb = h[m][i] * 1e9, V[m][i]
        ax.plot(hb, Vb, "o", color=col, ms=5, zorder=5)
        pos = {1e-3: (3.6, 25.8), 1e-2: (2.7, 11.6), 1e-1: (3.2, -6.0)}[c_]

        pre = "barrier " if c_ == 1e-3 else ""
        ax.annotate(f"{pre}{Vb:.2g} $k_BT$ at {hb:.2g} nm", xy=(hb, Vb), xytext=pos, fontsize=8,
                    color=col, arrowprops=dict(arrowstyle="-", lw=0.6, color=col))
        if c_ == 1e-3:
            ax.plot(h * 1e9, VR, color="0.55", ls="--", lw=1.2, label="double-layer repulsion alone (1 mM)")
    ax.plot(h * 1e9, VA, color=INK, ls="--", lw=1.2, label="van der Waals attraction alone")
    ax.axhline(15, color="0.3", ls=":", lw=1)
    ax.text(19.8, 14.5, "approx. stability threshold (15 $k_BT$)", fontsize=8, ha="right", va="top",
            color="0.3")

    ax.annotate("primary minimum\n(coagulation)", xy=(0.25, -19), xytext=(1.6, -16.5), fontsize=8,
                arrowprops=dict(arrowstyle="-|>", lw=0.8, mutation_scale=9))

    ax.set_xlim(0, 20)
    ax.set_ylim(-20, 30)
    ax.set_xlabel("surface separation $h$ (nm)")
    ax.set_ylabel("interaction energy $V/k_BT$")
    ax.legend(fontsize=7.5, loc="lower right", frameon=True, framealpha=0.95, edgecolor="none")
    ins = ax.inset_axes([0.66, 0.79, 0.26, 0.15])
    I = np.logspace(-4, 0, 50)
    ins.loglog(I, 0.304 / np.sqrt(I), color=INK, lw=1.3)
    for Iv, lab in ((1e-3, "1 mM"), (1e-2, "10 mM"), (1e-1, "100 mM")):
        ins.plot(Iv, 0.304 / np.sqrt(Iv), "o", ms=3.5, color="0.4")
    ins.plot(0.7, 0.304 / np.sqrt(0.7), "s", ms=4.5, color=COLORS[0])
    ins.annotate("sea water\n0.36 nm", xy=(0.7, 0.36), xytext=(0.01, 0.3), fontsize=6.5,

                 arrowprops=dict(arrowstyle="-", lw=0.5))
    ins.set_title("Debye length vs ionic strength (M)", fontsize=7, pad=2)

    ins.set_ylabel(r"$\kappa^{-1}$ (nm)", fontsize=7, labelpad=1)
    ins.tick_params(labelsize=6.5)
    ins.set_xlim(1e-4, 1); ins.set_ylim(0.2, 40)
    save(fig, "37", "fig-37-3-dlvo-potential")


# ---------------------------------------------------------------- Figure 37.4
def hydrogel_swelling():
    fig = plt.figure(figsize=(6.8, 4.6))
    a = fig.add_axes([0.09, 0.56, 0.38, 0.36])
    T = np.linspace(15, 50, 400)
    logQ = np.log10(2.0) + (np.log10(17) - np.log10(2.0)) / (1 + np.exp((T - 32) / 0.55))
    logQ += np.where(T < 32, -0.0045 * (T - 15), 0) * 1.0
    a.semilogy(T, 10**logQ, color=COLORS[0], lw=2)
    a.axvline(32, color="0.4", ls="--", lw=0.9)
    a.text(32.6, 300, "LCST\n32 °C", fontsize=8, va="top")
    a.text(17, 26, "swollen, hydrated", fontsize=7.8, color=COLORS[0])
    a.text(36, 2.8, "collapsed", fontsize=7.8, color=COLORS[0])
    a.set_xlim(15, 50); a.set_ylim(1, 1000)
    a.set_xlabel("temperature (°C)")
    a.set_ylabel("swelling ratio $Q$\n(swollen/dry mass)")
    a.set_title("(a) PNIPAM gel", fontsize=9.5, loc="left")

    b = fig.add_axes([0.59, 0.56, 0.38, 0.36])
    c = np.logspace(-4, 0, 300)
    Qs, Q0, c0, n = 12.0, 300.0, 0.0197, 0.886
    Q = Qs + (Q0 - Qs) / (1 + (c / c0)**n)
    b.loglog(c, Q, color=COLORS[1], lw=2)
    b.axvline(0.15, color="0.4", ls="--", lw=0.9)
    b.text(0.13, 520, "0.15 M\nsaline / urine", fontsize=7.5, ha="right", va="top")
    qq = Qs + (Q0 - Qs) / (1 + (0.15 / c0)**n)
    b.plot(0.15, qq, "o", color=COLORS[1], ms=5)
    b.annotate("≈50", xy=(0.15, qq), xytext=(0.25, 90), fontsize=8,
               arrowprops=dict(arrowstyle="-", lw=0.6))
    b.plot(1, 20, "o", color=COLORS[1], ms=5, clip_on=False)
    b.text(0.75, 13, "≈20", fontsize=8, ha="right")
    b.text(1.3e-4, 330, "pure water ≈300", fontsize=8, va="bottom")
    b.set_xlim(1e-4, 1); b.set_ylim(1, 1000)
    b.set_xlabel("NaCl concentration (M)")
    b.set_ylabel("swelling ratio $Q$")
    b.set_title("(b) sodium polyacrylate superabsorbent", fontsize=9.5, loc="left")

    # (c) network schematic (drawing units = nm)
    cx = fig.add_axes([0.02, 0.0, 0.96, 0.41])
    cx.set_aspect("equal"); cx.axis("off")
    cx.set_xlim(-2, 62); cx.set_ylim(-3, 25)
    rng = np.random.default_rng(3)
    xi = 7.0
    nodes = {}
    for i in range(6):
        for j in range(4):
            nodes[(i, j)] = np.array([1.5 + i * xi + rng.normal(0, 0.9), 1.0 + j * xi + rng.normal(0, 0.9)])
    segs = []
    for (i, j), p in nodes.items():
        for di, dj in ((1, 0), (0, 1)):
            q = nodes.get((i + di, j + dj))
            if q is not None:
                # slightly wavy strand
                t = np.linspace(0, 1, 20)
                mid = (p + q) / 2 + rng.normal(0, 0.7, 2)
                curve = ((1 - t)**2)[:, None] * p + (2 * t * (1 - t))[:, None] * mid + (t**2)[:, None] * q
                cx.plot(curve[:, 0], curve[:, 1], color="0.35", lw=1.2, zorder=1)
    for p in nodes.values():
        cx.plot(*p, "o", color=COLORS[0], ms=5.5, zorder=3)
    p, q = nodes[(1, 1)], nodes[(2, 1)]
    cx.annotate("", xy=(q[0], q[1] - 1.2), xytext=(p[0], p[1] - 1.2),
                arrowprops=dict(arrowstyle="<|-|>", lw=1.0, color=COLORS[1], mutation_scale=8))
    cx.text((p[0] + q[0]) / 2, p[1] - 2.0, r"mesh size $\xi\approx7$ nm", fontsize=8, ha="center", va="top",
            color=COLORS[1], bbox=dict(fc="white", ec="none", pad=0.5, alpha=0.85))
    # solutes to scale (diameters in nm): one glucose and one insulin inside the mesh
    gl = (nodes[(3, 2)] + nodes[(4, 3)]) / 2
    cx.add_patch(Circle(gl, 0.5, fc=COLORS[2], ec=INK, lw=0.5, zorder=4))
    ins_ = (nodes[(1, 2)] + nodes[(2, 3)]) / 2
    cx.add_patch(Circle(ins_, 1.5, fc=COLORS[4], ec=INK, lw=0.5, zorder=4))
    # key, same scale
    for xc, r, fc, lab in ((42.5, 0.5,
 COLORS[2], "glucose\n1 nm\nfree"),
                           (47.5, 1.5, COLORS[4], "insulin\n3 nm\nhindered"),
                           (56.0, 6.0, "#E7B7D2", "IgG antibody\n12 nm\nexcluded")):
        cx.add_patch(Circle((xc, 13.0), r, fc=fc, ec=INK, lw=0.6, zorder=4))
        if r < 1:
            cx.text(xc, 14.5, lab, fontsize=7.6, ha="center", va="bottom")
        else:
            cx.text(xc, 13.0 - r - 0.8, lab, fontsize=7.6, ha="center", va="top")
    cx.text(50.0, 22.5, "solutes (same scale)", fontsize=8, ha="center")
    cx.plot([40.5, 45.5], [-1.5, -1.5], color=INK, lw=2)
    cx.text(43, -2.0, "5 nm", fontsize=7.5, ha="center", va="top")
    fig.text(0.015, 0.455, "(c) network drawn to scale (dots = crosslinks)", fontsize=9.5, va="top")
    cx.set_ylim(-4, 23.5)
    save(fig, "37", "fig-37-4-hydrogel-swelling")


# ---------------------------------------------------------------- Figure 37.5
def _rod(ax, x, y, ang, L=0.34, w=0.075, fc="#7FA7D1", z=3):
    ax.add_patch(Ellipse((x, y), L, w, angle=ang, fc=fc, ec=INK, lw=0.5, zorder=z))


def _maier_saupe(t):
    def F(S, a):
        num = quad(lambda x: 0.5 * (3 * x * x - 1) * np.exp(a * S * 0.5 * (3 * x * x - 1)), 0, 1)[0]
        den = quad(lambda x: np.exp(a * S * 0.5 * (3 * x * x - 1)), 0, 1)[0]
        return num / den - S
    return brentq(F, 0.42, 0.995, args=(4.5415 / t,))


def liquid_crystal_phases():
    fig = plt.figure(figsize=(6.8, 5.6))
    ax = fig.add_axes([0.0, 0.60, 1.0, 0.38])
    ax.set_xlim(0, 16.0); ax.set_ylim(-1.15, 3.35); ax.set_aspect("equal"); ax.axis("off")
    rng = np.random.default_rng(7)
    names = ["crystal", "smectic C", "smectic A", "nematic", "isotropic liquid"]
    subs = ["positional +\norientational order", "tilted layers", "layers, director\nnormal to layers",
            "director $\\mathbf{n}$, no layers", "no order"]
    bw, gap = 2.75, 0.45
    for k in range(5):
        x0 = 0.25 + k * (bw + gap)
        ax.add_patch(Rectangle((x0, 0.35), bw, 2.35, fc="white", ec=INK, lw=0.9))
        ax.text(x0 + bw / 2, 2.95, names[k], ha="center", fontsize=8.8, fontweight="bold")
        ax.text(x0 + bw / 2, 0.22, subs[k], ha="center", va="top", fontsize=7.3)
        if k == 0:
            for i in range(6):
                for j in range(5):
                    _rod(ax, x0 + 0.33 + i * 0.42, 0.6 + j * 0.45, 90, L=0.36)
        elif k in (1, 2):
            tilt = 60 if k == 1 else 90
            for j in range(3):
                yl = 0.75 + j * 0.78
                ax.plot([x0 + 0.05, x0 + bw - 0.05], [yl - 0.32, yl - 0.32], color="0.75", lw=0.6, ls=":")
                for i in range(7):
                    _rod(ax, x0 + 0.27 + i * 0.37 + rng.normal(0, 0.03), yl + rng.normal(0, 0.02),
                         tilt + rng.normal(0, 6), L=0.5)
            if k == 1:
                ax.annotate("", xy=(x0 + bw - 0.15, 2.62), xytext=(x0 + bw - 0.45, 2.1),
                            arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.2, mutation_scale=9))
        elif k == 3:
            for _ in range(26):
                xx, yy = x0 + 0.25 + rng.random() * (bw - 0.5), 0.6 + rng.random() * 1.85
                _rod(ax, xx, yy, 90 + rng.normal(0, 14), L=0.5)
            ax.annotate("", xy=(x0 + bw - 0.2, 2.6), xytext=(x0 + bw - 0.2, 1.9),
                        arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.4, mutation_scale=10), zorder=6)
            ax.text(x0 + bw - 0.32, 2.3, r"$\mathbf{n}$", color=COLORS[1], ha="right", fontsize=10, zorder=6)
        else:
            for _ in range(24):
                xx, yy = x0 + 0.25 + rng.random() * (bw - 0.5), 0.6 + rng.random() * 1.85
                _rod(ax, xx, yy, rng.random() * 180, L=0.5)
    ax.annotate("", xy=(15.9, -0.98), xytext=(0.3, -0.98),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.2, mutation_scale=11))
    ax.text(8.1, -0.98, "temperature increasing", ha="center", va="center", fontsize=8,
            bbox=dict(fc="white", ec="none", pad=0.4))
    fig.text(0.005, 0.975, "(a)", fontsize=10, fontweight="bold")

    # cholesteric inset
    ci = fig.add_axes([0.005, 0.03, 0.15, 0.45])
    ci.set_xlim(-1, 1); ci.set_ylim(-0.35, 4.4); ci.axis("off")
    for j, z in enumerate(np.linspace(0, 3.6, 13)):
        phi = 2 * np.pi * z / 3.6 * 1.0
        Lp = 0.75 * abs(np.cos(phi)) + 0.08
        ci.add_patch(Ellipse((0, z), 2 * Lp * 0.9, 0.12, fc="#B9A2D6", ec=INK, lw=0.5))
    ci.plot([0, 0], [-0.2, 3.8], color="0.5", lw=0.6, ls=":")
    ci.annotate("", xy=(0.95, 3.6), xytext=(0.95, 0.0),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.9, color=COLORS[3], mutation_scale=8))
    ci.text(0.98, 1.8, "$p$", color=COLORS[3], fontsize=10, va="center")
    ci.text(0, 4.35, "cholesteric\nhelix", ha="center", va="top", fontsize=8)

    # (b) order parameter
    bx = fig.add_axes([0.25, 0.10, 0.30, 0.40])
    t = np.linspace(0.8, 1.0, 40)
    S = np.array([_maier_saupe(v) for v in t])
    bx.plot(t, S, color=COLORS[0], lw=2, label="Maier–Saupe theory")
    bx.plot([1.0, 1.0], [0, S[-1]], color=COLORS[0], lw=1.2, ls="--")
    bx.plot([1.0, 1.05], [0, 0], color=COLORS[0], lw=2)
    dT = np.array([0.5, 1, 2, 4, 6, 8, 10, 12])
    S5 = np.array([0.31, 0.35, 0.39, 0.43, 0.46, 0.49, 0.51, 0.53])
    bx.plot((308.15 - dT) / 308.15, S5, "o", color=COLORS[1], ms=4.5, mfc="white", mew=1.2,
            label="5CB ($T_{NI}$ = 35 °C)")
    bx.annotate(f"$S$ = {S[-1]:.2f}", xy=(1.0, S[-1]), xytext=(0.93, 0.25), fontsize=8,
                arrowprops=dict(arrowstyle="-", lw=0.6))
    bx.set_xlim(0.8, 1.05); bx.set_ylim(0, 0.8)
    bx.set_xlabel(r"$T/T_{NI}$")
    bx.set_ylabel("order parameter $S$")
    bx.legend(fontsize=7.3, loc="upper right")
    bx.set_title("(b)", fontsize=10, fontweight="bold", loc="left")

    # (c) twisted-nematic cell
    cx = fig.add_axes([0.58, 0.02, 0.42, 0.52])
    cx.set_xlim(0, 8.4); cx.set_ylim(-0.6, 6.2); cx.set_aspect("equal"); cx.axis("off")
    for k, (state, x0) in enumerate((("off: bright", 0.3), ("on: dark", 4.5))):
        # polarizers (top & bottom), glass plates
        cx.add_patch(Rectangle((x0, 4.7), 3.4, 0.22, fc="#D8D8D8", ec=INK, lw=0.6))
        cx.add_patch(Rectangle((x0, 0.9), 3.4, 0.22, fc="#D8D8D8", ec=INK, lw=0.6))
        for yy in (4.45, 1.15):
            cx.add_patch(Rectangle((x0, yy), 3.4, 0.22 if yy > 2 else 0.22, fc="#E7F1FA", ec=INK, lw=0.5))
        # polarizer axis marks
        for j in range(5):
            cx.plot([x0 + 0.4 + j * 0.65, x0 + 0.4 + j * 0.65], [4.72, 4.90], color="0.3", lw=0.6)
            cx.plot([x0 + 0.25 + j * 0.65, x0 + 0.55 + j * 0.65], [1.01, 1.01], color="0.3", lw=0.6)
        # LC rods
        nl = 6
        for i in range(nl):
            yy = 1.55 + i * 0.52
            ang_t = 90 * i / (nl - 1)
            for j in range(4):
                xx = x0 + 0.55 + j * 0.78
                if k == 0:
                    Lr = 0.12 + 0.48 * abs(np.cos(np.radians(ang_t)))
                    _rod(cx, xx, yy, 0, L=Lr, w=0.13)
                else:
                    tilt = 90 if 0 < i < nl - 1 else 20
                    _rod(cx, xx, yy, tilt, L=0.42, w=0.12)
        # light
        cx.annotate("", xy=(x0 + 1.7, 6.0), xytext=(x0 + 1.7, 5.05),
                    arrowprops=dict(arrowstyle="-|>", lw=2.2, color="#E5B800" if k == 0 else "0.6",
                                    mutation_scale=12))
        if k == 1:
            cx.text(x0 + 1.95, 5.55, "blocked", fontsize=7.5, va="center")
            cx.plot([x0 - 0.1, x0 - 0.1], [1.2, 4.55], color=COLORS[1], lw=1.0)
            cx.text(x0 - 0.18, 2.9, "V", fontsize=8, color=COLORS[1], ha="right")
        cx.annotate("", xy=(x0 + 1.7, 0.85), xytext=(x0 + 1.7, -0.25),
                    arrowprops=dict(arrowstyle="-|>", lw=2.2, color="#E5B800", mutation_scale=12))
        cx.text(x0 + 1.7, 6.2, state, ha="center", va="bottom", fontsize=8.5, fontweight="bold")
    cx.text(0.3, -0.45, "backlight", fontsize=7.5, va="center")
    cx.text(2.15, 0.25, "90° twist rotates\npolarization", fontsize=7, ha="left", va="center", color="0.25")
    cx.text(6.35, 0.25, "field aligns\nmolecules", fontsize=7, ha="left", va="center", color="0.25")

    cx.text(8.35, 4.81, "analyser", fontsize=7, ha="right", va="center", rotation=0, alpha=0)
    fig.text(0.585, 0.53, "(c) twisted-nematic cell, crossed polarizers", fontsize=9)
    save(fig, "37", "fig-37-5-liquid-crystal-phases")


# ---------------------------------------------------------------- Figure 37.6
def _amph(ax, base, direction, L=0.5, head=0.11, two=False, col=COLORS[0]):
    """Amphiphile with head at `base` and tail(s) pointing along unit vector `direction`."""
    d = np.asarray(direction, float); d /= np.linalg.norm(d)
    nrm = np.array([-d[1], d[0]])
    offs = (-0.035, 0.035) if two else (0.0,)
    for o in offs:
        p0 = np.asarray(base) + d * head * 0.9 + nrm * o
        t = np.linspace(0, 1, 12)
        pts = p0[None, :] + t[:, None] * d[None, :] * L + nrm[None, :] * 0.025 * np.sin(t * 14)[:, None]
        ax.plot(pts[:, 0], pts[:, 1], color="0.35", lw=0.9, zorder=2)
    ax.add_patch(Circle(base, head, fc=col, ec=INK, lw=0.4, zorder=3))


def packing_parameter():
    fig = plt.figure(figsize=(6.8, 5.0))
    ax = fig.add_axes([0.0, 0.17, 1.0, 0.80])
    ax.set_xlim(0, 15); ax.set_ylim(0, 8.8); ax.set_aspect("equal"); ax.axis("off")
    xs = [1.5, 4.5, 7.5, 10.5, 13.5]
    tops = [(1.2, 0.0), (1.0, 0.45), (0.95, 0.65), (0.75, 0.75), (0.35, 1.05)]  # (top width, bottom width)
    shape_names = ["cone", "truncated cone", "truncated cone", "cylinder", "inverted cone"]
    Pr = ["$P<1/3$", "$1/3<P<1/2$", "$1/2<P<1$", "$P\\approx1$", "$P>1$"]
    agg = ["spherical micelle", "cylindrical micelle", "vesicle /\nflexible bilayer", "planar bilayer",
           "inverted micelle"]
    yb, yt = 5.6, 7.6
    for x, (wt, wb), sn, pr in zip(xs, tops, shape_names, Pr):
        ax.add_patch(Polygon([(x - wt / 2, yt), (x + wt / 2, yt), (x + wb / 2, yb), (x - wb / 2, yb)],
                             fc="#F4EBD9", ec="0.4", lw=0.9, ls="--", zorder=1))
        ax.add_patch(Circle((x, yt), 0.2, fc=COLORS[0], ec=INK, lw=0.5, zorder=3))
        for o in (-0.07, 0.07):
            t = np.linspace(0, 1, 15)
            ax.plot(x + o + 0.04 * np.sin(t * 12), yt - 0.2 - t * 1.7, color="0.35", lw=1.0, zorder=2)
        ax.text(x, 8.05, sn, ha="center", fontsize=8.3)
        ax.text(x, 5.3, pr, ha="center", va="top", fontsize=8.5, color=COLORS[1])
    # annotate a0, v, lc on the cylinder
    x = xs[3]
    ax.annotate("", xy=(x - 0.375, yt + 0.32), xytext=(x + 0.375, yt + 0.32),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, mutation_scale=7))
    ax.text(x + 0.55, yt + 0.2, "$a_0$", fontsize=9, va="center")
    ax.annotate("", xy=(x + 0.55, yt - 0.2), xytext=(x + 0.55, yb),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, mutation_scale=7))
    ax.text(x + 0.65, (yt + yb) / 2, "$l_c$", fontsize=9, va="center")
    ax.text(x - 0.5, (yt + yb) / 2 - 0.3, "$v$", fontsize=9, ha="right", va="center")
    ax.text(0.05, 6.6, "head", fontsize=7.5, color=COLORS[0])
    ax.annotate("", xy=(xs[0] - 0.22, yt), xytext=(0.6, 6.75),
                arrowprops=dict(arrowstyle="-", lw=0.5, color=COLORS[0]))
    ax.text(0.05, 5.9, "tail(s)", fontsize=7.5, color="0.35")
    for k in range(4):
        ax.annotate("", xy=(xs[k] + 1.15, 6.6), xytext=(xs[k] + 1.85, 6.6),
                    arrowprops=dict(arrowstyle="-", lw=0.0, color="white"))
    # aggregates
    yc = 2.7
    # spherical micelle
    c = np.array([xs[0], yc])
    for a in np.linspace(0, 2 * np.pi, 16, endpoint=False):
        u = np.array([np.cos(a), np.sin(a)])
        _amph(ax, c + 1.0 * u, -u, L=0.75)
    # cylindrical micelle (side view, cut-away)
    c = np.array([xs[1], yc])
    for yy in np.linspace(-0.75, 0.75, 6):
        _amph(ax, c + np.array([-0.62, yy]), (1, 0), L=0.48)
        _amph(ax, c + np.array([0.62, yy]), (-1, 0), L=0.48)
    for a in np.linspace(np.pi * 0.15, np.pi * 0.85, 4):
        u = np.array([np.cos(a), np.sin(a)])
        _amph(ax, c + np.array([0, 0.85]) + 0.62 * u, -u, L=0.45)
        _amph(ax, c + np.array([0, -0.85]) - 0.62 * u, u, L=0.45)
    # vesicle
    c = np.array([xs[2], yc])
    for a in np.linspace(0, 2 * np.pi, 22, endpoint=False):
        u = np.array([np.cos(a), np.sin(a)])
        _amph(ax, c + 1.32 * u, -u, L=0.3, head=0.09, two=True)

    for a in np.linspace(0, 2 * np.pi, 15, endpoint=False):
        u = np.array([np.cos(a), np.sin(a)])
        _amph(ax, c + 0.5 * u, u, L=0.3, head=0.09, two=True)
    ax.text(c[0], c[1], "water", fontsize=6.5, ha="center", va="center", color="0.4")
    # planar bilayer
    c = np.array([xs[3], yc])
    for xx in np.linspace(-1.05, 1.05, 9):
        _amph(ax, c + np.array([xx, 0.62]), (0, -1), L=0.47, two=True)
        _amph(ax, c + np.array([xx, -0.62]), (0, 1), L=0.47, two=True)
    # inverted micelle
    c = np.array([xs[4], yc])
    for a in np.linspace(0, 2 * np.pi, 9, endpoint=False):
        u = np.array([np.cos(a), np.sin(a)])
        _amph(ax, c + 0.32 * u, u, L=0.75, two=True)
    ax.text(c[0], c[1], "water", fontsize=5.5, ha="center", va="center", color="white", zorder=5)
    ax.text(c[0] + 1.25, c[1] - 1.25, "oil", fontsize=7.5, color="0.4", ha="center")
    for x, a in zip(xs, agg):
        ax.text(x, 0.75, a, ha="center", va="top", fontsize=8.3)
        ax.annotate("", xy=(x, 4.35), xytext=(x, 5.0),
                    arrowprops=dict(arrowstyle="-|>", lw=1.0, color="0.5", mutation_scale=9))

    # P axis
    px = fig.add_axes([0.08, 0.09, 0.86, 0.06])
    px.set_xlim(0, 1.5); px.set_ylim(0, 1)
    px.set_yticks([])
    for sp in ("left", "right", "top"):
        px.spines[sp].set_visible(False)
    bounds = [0, 1 / 3, 0.5, 1.0, 1.5]
    fills = ["#DCE9F5", "#E3F1E6", "#FFF1D6", "#F6E0EC"]
    for (a_, b_), fc in zip(zip(bounds[:-1], bounds[1:]), fills):
        px.axvspan(a_, b_, color=fc, lw=0)
    px.axvline(1.0, color=COLORS[1], lw=1.2, ls="--")
    for v in (0.30, 0.42, 0.65):
        px.plot([v, v], [0, 1], color=INK, lw=1.4)
    px.text(0.30, 1.1, "SDS in water (0.30)", fontsize=7.3, ha="right", va="bottom")
    px.text(0.42, 1.1, "SDS + salt (0.42)", fontsize=7.3, ha="left", va="bottom")
    px.text(0.67, 0.5, "two-tailed C$_{16}$\nphospholipid (0.65)", fontsize=7.3, ha="left", va="center")
    px.set_xticks([0, 1 / 3, 0.5, 1.0, 1.5])
    px.set_xticklabels(["0", "1/3", "1/2", "1", "1.5"])
    px.set_xlabel(r"packing parameter $P=v/(a_0\,l_c)$", fontsize=9)
    save(fig, "37", "fig-37-6-packing-parameter")


if __name__ == "__main__":
    actuator_map()
    sma_cycle_superelastic()
    dlvo_potential()
    hydrogel_swelling()
    liquid_crystal_phases()
    packing_parameter()
