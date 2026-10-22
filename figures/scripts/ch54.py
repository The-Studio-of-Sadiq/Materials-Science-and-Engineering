"""Figures for Chapter 54 — In-situ, Operando and Specialized Characterization.

Run from the repository root:  python figures/scripts/ch54.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon, FancyBboxPatch

SI = "#B8B8B8"
SIN = "#7A8FA6"
HEAT = "#E69F00"
FLUID = "#9BCBEB"
METAL = "#C9A227"


def _beam(ax, x, y0, y1):
    ax.annotate("", xy=(x, y1), xytext=(x, y0),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=2.0, mutation_scale=13))
    ax.text(x + 0.12, y0 - 0.05, "e$^-$", color=COLORS[0], fontsize=9, va="top")


# ---------------------------------------------------------------- Figure 54.1
def insitu_holder_types():
    fig, axs = plt.subplots(1, 4, figsize=(6.8, 3.3))
    for ax in axs:
        ax.set_xlim(0, 4)
        ax.set_ylim(-0.4, 5)
        ax.set_aspect("equal")
        ax.axis("off")

    # (a) MEMS heating chip
    ax = axs[0]
    ax.set_title("(a) MEMS heating", fontsize=9.5)
    ax.add_patch(Rectangle((0.1, 1.9), 0.9, 0.6, fc=SI, ec=INK, lw=0.8))
    ax.add_patch(Rectangle((3.0, 1.9), 0.9, 0.6, fc=SI, ec=INK, lw=0.8))
    ax.add_patch(Rectangle((0.1, 2.5), 3.8, 0.08, fc=SIN, ec=INK, lw=0.6))
    for x in [1.15, 1.45, 2.35, 2.65]:
        ax.add_patch(Rectangle((x, 2.58), 0.2, 0.09, fc=HEAT, ec="none"))
    for x in [1.75, 2.05]:     # windows with particles
        ax.add_patch(Circle((x + 0.1, 2.67), 0.07, fc=COLORS[2], ec="none"))
    ax.text(2.0, 2.2, "specimen on\nwindows", ha="center", va="center", fontsize=6.8, color=COLORS[2])
    _beam(ax, 2.0, 4.1, 2.75)
    ax.text(0.55, 1.75, "Si frame", ha="center", va="top", fontsize=7.5)
    ax.annotate("SiN membrane", xy=(3.4, 2.56), xytext=(3.95, 3.25), fontsize=7.5, ha="right",
                arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
    ax.annotate("spiral heater", xy=(1.25, 2.66), xytext=(0.05, 3.25), fontsize=7.5,
                color="#B07800", arrowprops=dict(arrowstyle="-", lw=0.6, color="#B07800"))
    ax.text(2.0, 1.15, "up to ~1,300 °C\n~10$^6$ °C/s", ha="center", va="top", fontsize=8,
            color=INK, fontweight="bold")

    # (b) straining (push-to-pull)
    ax = axs[1]
    ax.set_title("(b) straining", fontsize=9.5)
    ax.add_patch(Rectangle((0.1, 2.0), 1.6, 0.5, fc=SI, ec=INK, lw=0.8))
    ax.add_patch(Rectangle((2.3, 2.0), 1.6, 0.5, fc=SI, ec=INK, lw=0.8))
    # dog-bone specimen bridging the gap
    db = Polygon([[1.25, 2.5], [1.25, 2.75], [1.6, 2.75], [1.75, 2.62], [2.25, 2.62], [2.4, 2.75],
                  [2.75, 2.75], [2.75, 2.5]], closed=True, fc="#7FB8A4", ec=INK, lw=0.7)
    ax.add_patch(db)
    ax.annotate("", xy=(3.85, 1.65), xytext=(2.6, 1.65),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.6, mutation_scale=11))
    ax.text(3.2, 1.55, "actuator", ha="center", va="top", fontsize=7.5, color=COLORS[1])
    ax.text(0.75, 1.55, "fixed", ha="center", va="top", fontsize=7.5, color="0.4")
    _beam(ax, 2.0, 4.1, 2.8)
    ax.annotate("dog-bone\nspecimen", xy=(2.55, 2.72), xytext=(3.95, 3.4), fontsize=7.5, ha="right",
                arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
    ax.text(2.0, 1.15, "tension,\n~nm displacement\ncontrol", ha="center", va="top", fontsize=8,
            fontweight="bold")

    # (c) biasing chip
    ax = axs[2]
    ax.set_title("(c) biasing", fontsize=9.5)
    ax.add_patch(Rectangle((0.1, 2.0), 3.8, 0.5, fc=SI, ec=INK, lw=0.8))
    ax.add_patch(Rectangle((1.75, 2.0), 0.5, 0.5, fc="white", ec=INK, lw=0.8))   # window
    ax.add_patch(Rectangle((0.5, 2.5), 1.3, 0.12, fc=METAL, ec=INK, lw=0.6))
    ax.add_patch(Rectangle((2.2, 2.5), 1.3, 0.12, fc=METAL, ec=INK, lw=0.6))
    ax.add_patch(Rectangle((1.5, 2.62), 1.0, 0.16, fc="#7FB8A4", ec=INK, lw=0.6))  # lamella
    # circuit, routed below the chip
    ax.plot([0.55, 0.25, 0.25, 1.72], [2.56, 2.56, 1.45, 1.45], color=INK, lw=0.9)
    ax.plot([3.45, 3.75, 3.75, 2.28], [2.56, 2.56, 1.45, 1.45], color=INK, lw=0.9)
    ax.add_patch(Circle((2.0, 1.45), 0.28, fc="white", ec=INK, lw=0.9, zorder=3))
    ax.text(2.0, 1.45, "V", ha="center", va="center", fontsize=8.5, zorder=4)
    ax.text(1.55, 1.55, "+", fontsize=8, ha="center", va="bottom")
    ax.text(2.45, 1.55, "−", fontsize=8, ha="center", va="bottom")
    _beam(ax, 2.0, 4.1, 2.9)
    ax.annotate("lamella", xy=(2.4, 2.75), xytext=(3.95, 3.4), fontsize=7.5, ha="right",
                arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
    ax.annotate("electrodes", xy=(0.9, 2.6), xytext=(0.05, 3.4), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
    ax.text(2.0, 1.15, "field, current,\nelectromigration", ha="center", va="top", fontsize=8,
            fontweight="bold")

    # (d) closed gas / liquid cell
    ax = axs[3]
    ax.set_title("(d) gas / liquid cell", fontsize=9.5)
    ax.add_patch(Rectangle((0.4, 2.0), 3.2, 0.5, fc=FLUID, ec="none"))
    for y in (1.65, 2.5):
        ax.add_patch(Rectangle((0.4, y), 1.3, 0.35, fc=SI, ec=INK, lw=0.8))
        ax.add_patch(Rectangle((2.3, y), 1.3, 0.35, fc=SI, ec=INK, lw=0.8))
    ax.add_patch(Rectangle((1.7, 2.5), 0.6, 0.05, fc=SIN, ec=INK, lw=0.5))
    ax.add_patch(Rectangle((1.7, 1.95), 0.6, 0.05, fc=SIN, ec=INK, lw=0.5))
    ax.plot([0.4, 3.6], [2.0, 2.0], color=INK, lw=0.6)
    ax.plot([0.4, 3.6], [2.5, 2.5], color=INK, lw=0.6)
    for x0, x1, lab in [(0.4, 0.0, "in"), (3.6, 4.0, "out")]:
        ax.add_patch(Rectangle((min(x0, x1), 2.12), 0.4, 0.26, fc=FLUID, ec=INK, lw=0.6))
    ax.annotate("", xy=(0.45, 2.25), xytext=(-0.05, 2.25),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.0, mutation_scale=8))
    ax.annotate("", xy=(4.1, 2.25), xytext=(3.6, 2.25),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.0, mutation_scale=8))
    ax.text(0.15, 2.5, "inlet", ha="center", va="bottom", fontsize=7)
    ax.text(3.85, 2.5, "outlet", ha="center", va="bottom", fontsize=7)
    _beam(ax, 2.0, 4.1, 2.95)
    ax.annotate("SiN windows\n20–50 nm", xy=(2.25, 2.53), xytext=(3.95, 3.15), fontsize=7.5,
                ha="right", arrowprops=dict(arrowstyle="-", lw=0.6, color=INK))
    ax.text(2.0, 1.15, "≤1 bar gas or\nliquid flow", ha="center", va="top", fontsize=8,
            fontweight="bold")
    fig.subplots_adjust(wspace=0.08, left=0.01, right=0.99)
    save(fig, "54", "fig-54-1-insitu-holder-types")


# ---------------------------------------------------------------- Figure 54.2
def micropillar_size_effect():
    fig = plt.figure(figsize=(6.8, 3.6))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.25, 1], wspace=0.33)
    ax = fig.add_subplot(gs[0])
    rng = np.random.default_rng(4)
    E_app = 60e3   # apparent loading modulus (MPa) including machine/base compliance
    cases = [(5, 150, COLORS[0]), (2, 260, COLORS[2]), (1, 390, COLORS[4]), (0.5, 600, COLORS[1])]
    for D, s0, c in cases:
        if D == 5:
            eps_y = 0.8 * s0 / E_app
            e = np.linspace(0, 0.072, 400)
            s = np.where(e < eps_y, E_app * e,
                         0.8 * s0 + (s0 * 1.03 - 0.8 * s0) * (1 - np.exp(-(e - eps_y) / 0.012)))
            ax.plot(e, s, color=c)
        else:
            es, ss = [0.0], [0.0]
            sig = 0.9 * s0
            e = sig / E_app
            es.append(e); ss.append(sig)
            while e < 0.072:
                burst = rng.uniform(0.004, 0.012) * (1.6 if D == 0.5 else 1.0)
                e = min(e + burst, 0.072)
                es.append(e); ss.append(sig)       # flat strain burst
                if e >= 0.072:
                    break
                drop = rng.uniform(0.0, 0.04) * s0
                ss.append(sig - drop); es.append(e)   # small unload at burst end
                new = min(sig - drop + rng.uniform(0.02, 0.09) * s0, 1.12 * s0)
                new = max(new, sig - 0.02 * s0)
                e += (new - (sig - drop)) / E_app
                sig = new
                es.append(e); ss.append(sig)
            ax.plot(es, ss, color=c, lw=1.5)
        ax.text(0.040, s0 * 1.13 + 14, f"D = {D:g} μm", color=c, fontsize=8.5, ha="center")
    ax.set_xlim(0, 0.10)
    ax.set_ylim(0, 700)
    ax.set_xlabel("engineering strain")
    ax.set_ylabel("engineering stress (MPa)")
    ax.set_title("(a) single-crystal Ni pillars", fontsize=10, loc="left")
    ax.text(0.048, 70, "flat steps = strain bursts\n(dislocation avalanches)", fontsize=7.5,
            color="0.35", ha="center")
    # inset sketch: tapered pillar with slip steps
    ins = ax.inset_axes([0.76, 0.27, 0.23, 0.48])
    ins.set_xlim(0, 2); ins.set_ylim(0, 3); ins.axis("off"); ins.set_aspect("equal")
    ins.add_patch(Rectangle((0.0, 0.0), 2.0, 0.35, fc="#C8C8C8", ec=INK, lw=0.6))
    left = lambda y: 0.55 - 0.07 * (y - 0.35)
    right = lambda y: 1.45 + 0.07 * (y - 0.35)
    ys = [0.35, 1.0, 1.05, 1.6, 1.65, 2.3]
    off = [0, 0, 0.12, 0.12, 0.22, 0.22]
    pts_l = [(left(y) + o, y) for y, o in zip(ys, off)]
    pts_r = [(right(y) + o, y) for y, o in zip(ys, off)][::-1]
    ins.add_patch(Polygon(pts_l + pts_r, closed=True, fc="#9CC3DE", ec=INK, lw=0.7))
    ins.add_patch(Rectangle((0.35, 2.3), 1.55, 0.25, fc="0.35", ec=INK, lw=0.6))
    ins.annotate("", xy=(1.12, 2.58), xytext=(1.12, 2.98),
                 arrowprops=dict(arrowstyle="-|>", lw=0.9, color=INK, mutation_scale=7))
    ins.text(1.0, -0.12, "taper +\nslip steps", ha="center", va="top", fontsize=7)

    # (b) size effect
    bx = fig.add_subplot(gs[1])
    D = np.array([5, 2, 1, 0.5, 0.2])
    s = 150 * (D / 5) ** -0.6
    Dl = np.logspace(np.log10(0.1), 1, 50)
    bx.loglog(Dl, 150 * (Dl / 5) ** -0.6, color=COLORS[0], lw=1.2, ls="-", alpha=0.6)
    bx.loglog(D, s, "o", color=COLORS[1], ms=6, mec=INK, mew=0.6, zorder=3)
    bx.axhline(50, color="0.4", ls="--", lw=1.2)
    bx.text(0.13, 55, "bulk single crystal (~50 MPa)", fontsize=8, color="0.3", va="bottom")
    bx.text(1.5, 520, "slope −0.6\n$\\sigma = 150\\,(D/5\\,\\mu$m$)^{-0.6}$", fontsize=8.5,
            color=COLORS[0])
    for d, v in zip(D, s):
        bx.annotate(f"{v:.0f}", xy=(d, v), xytext=(5, -9), textcoords="offset points",
                    fontsize=7.5, color="0.3")
    bx.set_xlim(0.1, 10)
    bx.set_ylim(30, 2000)
    bx.set_xlabel("pillar diameter D (μm)")
    bx.set_ylabel("flow stress at 5 % strain (MPa)")
    bx.set_title("(b) power-law size effect", fontsize=10, loc="left")
    save(fig, "54", "fig-54-2-micropillar-size-effect")


# ---------------------------------------------------------------- Figure 54.3
def operando_xrd_graphite():
    t = np.linspace(0, 5, 301)          # h
    x = t / 5                           # Li fraction in Li_xC6
    d = np.linspace(3.30, 3.75, 451)
    w = 0.011
    I = np.zeros((t.size, d.size))
    x_s2 = 0.50
    x_s1 = 0.55                          # LiC6 appears: last ~45 % of capacity

    def peak(d0, a=1.0):
        return a * np.exp(-0.5 * ((d - d0) / w) ** 2)

    for i, xi in enumerate(x):
        if xi < 0.05:                    # dilute stage 1L, continuous expansion
            I[i] = peak(3.354 + (3.40 - 3.354) * xi / 0.05)
        elif xi < 0.25:                  # stages 4 -> 3 -> 2L, apparent d 3.40 -> 3.515
            I[i] = peak(3.40 + 0.115 * ((xi - 0.05) / 0.20) ** 0.8)
        elif xi < x_s2:                  # 2L -> 2 (LiC12)
            I[i] = peak(3.515 + 0.015 * (xi - 0.25) / 0.25)
        elif xi < x_s1:
            I[i] = peak(3.530)
        else:                            # two-phase LiC12 + LiC6
            f = (xi - x_s1) / (1 - x_s1)
            I[i] = peak(3.530, 1 - f) + peak(3.700, f)
    I += 0.02
    fig = plt.figure(figsize=(6.6, 4.2))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.6, 1], wspace=0.06)
    ax = fig.add_subplot(gs[0])
    ax.pcolormesh(d, t, I, cmap="magma", shading="auto", vmin=0, vmax=1.05, rasterized=True)
    ax.set_xlim(3.30, 3.75)
    ax.set_ylim(0, 5)
    ax.set_xlabel("interlayer spacing d(00l) (Å)")
    ax.set_ylabel("time at C/5 (h)")
    ax.set_title("(a) operando XRD intensity", fontsize=10, loc="left")
    lab = dict(fontsize=8, color="white", ha="center")
    ax.text(3.36, 0.5, "graphite\n3.35 Å", **lab, va="bottom")
    ax.text(3.44, 0.95, "dilute\nstages", **lab, va="bottom")
    ax.text(3.585, 1.85, "LiC$_{12}$\n(stage 2)\n3.53 Å", **lab, va="center")
    ax.text(3.65, 4.35, "LiC$_6$\n(stage 1)\n3.70 Å", **lab, va="center")
    ax.text(3.31, 3.15, "one pattern every\n5 min = 1.7 % SOC", fontsize=8, color="white",
            ha="left", va="center")
    ax.axhline(5 * x_s1, color="white", lw=0.6, ls=":")
    ax.set_xticks([3.30, 3.40, 3.50, 3.60, 3.70])

    vx = fig.add_subplot(gs[1], sharey=ax)
    knots_x = [0, 0.015, 0.05, 0.20, 0.235, 0.25, 0.48, 0.52, 0.55, 0.96, 0.99, 1.0]
    knots_v = [0.30, 0.235, 0.212, 0.200, 0.15, 0.125, 0.118, 0.095, 0.088, 0.082, 0.05, 0.01]
    V = np.interp(x, knots_x, knots_v)
    vx.plot(V, t, color=COLORS[0], lw=1.8)
    vx.set_xlim(0, 0.3)
    vx.set_xlabel("voltage vs Li/Li$^+$ (V)")
    vx.set_title("(b) voltage", fontsize=10, loc="left")
    plt.setp(vx.get_yticklabels(), visible=False)
    for v, tt, txt in [(0.21, 0.6, "~0.21 V"), (0.12, 1.85, "~0.12 V"), (0.085, 3.8, "~0.085 V")]:
        vx.text(v + 0.012, tt, txt, fontsize=8, color=COLORS[0], va="center")
    vx.axhline(5 * x_s1, color="0.6", lw=0.6, ls=":")
    vx.set_xticks([0, 0.1, 0.2, 0.3])
    save(fig, "54", "fig-54-3-operando-xrd-graphite")


# ---------------------------------------------------------------- Figure 54.4
def positron_lifetime_spectrum():
    dt = 0.01                                   # ns bins
    t = np.arange(0, 2.0 + dt, dt)
    t0 = 0.25
    sig = 0.200 / 2.3548
    tt = np.arange(-1.0, 3.0, 0.001)

    def comp(tau, I, N=4.0e6):
        decay = np.where(tt >= 0, I / tau * np.exp(-np.clip(tt, 0, None) / tau), 0.0)
        kt = np.arange(-0.5, 0.5 + 1e-9, 0.001)
        g = np.exp(-0.5 * (kt / sig) ** 2)
        g /= g.sum()
        conv = np.convolve(decay, g, mode="same")
        return N * dt * np.interp(t - t0, tt, conv)

    bg = 10.0
    ann = comp(0.110, 1.0) + bg
    c1 = comp(0.088, 0.60)
    c2 = comp(0.175, 0.40)
    irr = c1 + c2 + bg
    rng = np.random.default_rng(1)
    fig, ax = new_fig(6.4, 4.0)
    ax.semilogy(t, rng.poisson(ann).clip(0.8), ".", color=COLORS[0], ms=2.2, alpha=0.5)
    ax.semilogy(t, rng.poisson(irr).clip(0.8), ".", color=COLORS[1], ms=2.2, alpha=0.5)
    ax.semilogy(t, ann, color=COLORS[0], lw=1.6, label="annealed Fe: single τ = 110 ps")
    ax.semilogy(t, irr, color=COLORS[1], lw=1.8, label="irradiated Fe: sum of components")
    ax.semilogy(t, c1, color=COLORS[1], lw=1.1, ls="--", label="  τ$_1$ = 88 ps (60 %), reduced bulk")
    ax.semilogy(t, c2, color=COLORS[1], lw=1.1, ls=(0, (1.5, 1.5)),
                label="  τ$_2$ = 175 ps (40 %), monovacancy")
    ax.axhline(bg, color="0.6", lw=0.8, ls=":")
    ax.text(1.98, 8, "background ~10 counts", fontsize=7.5, color="0.45", ha="right", va="top")
    ax.set_xlim(0, 2.0)
    ax.set_ylim(1, 1e6)
    ax.set_xlabel("time after start signal (ns)")
    ax.set_ylabel("counts per 10 ps channel")
    ax.legend(loc="lower left", fontsize=7.8, handlelength=2.4, borderaxespad=0.3)
    ax.text(0.03, 3e5, "resolution\nFWHM ≈ 200 ps", fontsize=7.5, color="0.35", va="center")
    # inset: lattice with trapped positron and well
    ins = ax.inset_axes([0.60, 0.62, 0.20, 0.36])
    ins.set_xlim(-0.5, 4.5); ins.set_ylim(-0.5, 4.5); ins.set_aspect("equal"); ins.axis("off")
    for i in range(5):
        for j in range(5):
            if (i, j) == (2, 2):
                ins.add_patch(Circle((i, j), 0.33, fc="white", ec="0.5", lw=0.7, ls="--"))
                ins.add_patch(Circle((i, j), 0.17, fc="#D62728", ec="none"))
            else:
                ins.add_patch(Circle((i, j), 0.33, fc="#B8C4D0", ec=INK, lw=0.4))
    ins.set_title("e$^+$ at vacancy", fontsize=7.5, pad=1)
    ins2 = ax.inset_axes([0.82, 0.62, 0.17, 0.36])
    xx = np.linspace(-3, 3, 200)
    U = -1.0 * np.exp(-(xx / 0.8) ** 2)
    ins2.plot(xx, U, color=INK, lw=1.0)
    ins2.plot(0, -0.85, "o", color="#D62728", ms=4)
    ins2.annotate("", xy=(2.2, -1.0), xytext=(2.2, 0.0),
                  arrowprops=dict(arrowstyle="<|-|>", lw=0.7, mutation_scale=6, color=INK))
    ins2.text(2.0, -0.5, "~1 eV", fontsize=7, ha="right", va="center")
    ins2.set_ylim(-1.3, 0.25); ins2.axis("off")
    ins2.set_title("potential well", fontsize=7.5, pad=1)
    save(fig, "54", "fig-54-4-positron-lifetime-spectrum")


# ---------------------------------------------------------------- Figure 54.5
ALPHA_FE = np.array([-5.312, -3.076, -0.840, 0.840, 3.076, 5.312])   # mm/s for 33.0 T
REL = np.array([3, 2, 1, 1, 2, 3], float)


def _lor(v, v0, G):
    return (G / 2) ** 2 / ((v - v0) ** 2 + (G / 2) ** 2)


def _sextet(v, B, delta=0.0, eps=0.0, G=0.30, area=1.0):
    pos = delta + ALPHA_FE * B / 33.0 + eps * np.array([1, -1, -1, -1, -1, 1])
    a = REL / REL.sum()
    return area * sum(ai * _lor(v, p, G) / (np.pi * G / 2) for ai, p in zip(a, pos))


def mossbauer_steel_rust():
    v = np.linspace(-10, 10, 2001)
    fig, axs = plt.subplots(2, 1, figsize=(6.4, 5.0), sharex=True)
    # (a) Q&T steel: martensite/ferrite sextet + austenite singlet (8 % area)
    G = 0.34
    sext = _sextet(v, 33.0, 0.0, G=0.38, area=0.92) * 0.8 + _sextet(v, 30.5, 0.02, G=0.7, area=0.92) * 0.2
    sing = 0.08 * _lor(v, -0.09, 0.32) / (np.pi * 0.32 / 2)
    k = 0.085 / max((sext + sing).max(), 1e-9)
    T = 1 - k * (sext + sing)
    ax = axs[0]
    ax.plot(v, T, color=INK, lw=1.4)
    ax.fill_between(v, 1, 1 - k * sing, color=COLORS[1], alpha=0.5, lw=0)
    ax.plot(v, 1 - k * sext, color=COLORS[0], lw=0.9, ls="--")
    ax.set_ylim(0.90, 1.005)
    ax.set_ylabel("transmission")
    ax.set_title("(a) quenched and tempered steel", fontsize=10, loc="left")
    ax.annotate("retained austenite\nsinglet, δ ≈ −0.09 mm/s\n(~8 % of area)", xy=(-0.12, 0.975),
                xytext=(-3.0, 0.905), fontsize=8, color=COLORS[1], ha="center",
                arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[1]))
    ax.text(6.3, 0.935, "ferrite / martensite\nsextet, $B_{hf}$ ≈ 33 T", fontsize=8, color=COLORS[0])
    ax.text(5.75, 0.915, "outer lines\nat ±5.3 mm/s", fontsize=7.5, color="0.35", va="center")
    # (b) rust layer: broad goethite sextet + Fe3+ doublet
    Bs = np.linspace(26, 39, 27)
    wB = np.exp(-0.5 * ((Bs - 34.5) / 2.6) ** 2)
    wB /= wB.sum()
    goe = sum(wi * _sextet(v, B, 0.37, -0.13, G=0.4, area=0.6) for wi, B in zip(wB, Bs))
    dbl = 0.4 * (0.5 * _lor(v, 0.37 - 0.3, 0.4) + 0.5 * _lor(v, 0.37 + 0.3, 0.4)) / (np.pi * 0.2)
    k2 = 0.08 / (goe + dbl).max()
    bx = axs[1]
    bx.plot(v, 1 - k2 * (goe + dbl), color=INK, lw=1.4)
    bx.plot(v, 1 - k2 * goe, color=COLORS[2], lw=0.9, ls="--")
    bx.fill_between(v, 1, 1 - k2 * dbl, color=COLORS[3], alpha=0.45, lw=0)
    bx.set_ylim(0.90, 1.005)
    bx.set_ylabel("transmission")
    bx.set_title("(b) rust layer on weathering steel", fontsize=10, loc="left")
    bx.text(4.4, 0.925, "goethite: broadened sextet,\n$B_{hf}$ ≤ 38 T (reduced and\ndistributed by small particles)",
            fontsize=8, color=COLORS[2])
    bx.annotate("Fe$^{3+}$ doublet, δ ≈ 0.37,\nΔ$E_Q$ ≈ 0.6 mm/s\n(superparamagnetic /\nlepidocrocite)",
                xy=(0.75, 0.94), xytext=(-3.6, 0.903), fontsize=8, color=COLORS[3], ha="center",
                arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[3]))
    bx.set_xlim(-10, 10)
    bx.set_xticks(np.arange(-10, 11, 2))
    bx.set_xlabel("source velocity (mm/s)")
    fig.tight_layout()
    save(fig, "54", "fig-54-5-mossbauer-steel-rust")


# ---------------------------------------------------------------- Figure 54.6
def correlative_workflow():
    fig, ax = schematic(6.8, 4.0, xlim=(0, 17), ylim=(0, 10))
    steps = [
        ("1  Lab X-ray\nCT of\ncomponent", "voxel 10 μm\nfield ~cm", "locate crack\nor defect"),
        ("2  Nano-CT of\nextracted\nregion", "voxel 0.5 μm\nfield ~mm", "3D context"),
        ("3  SEM / EBSD\n/ EDS of\nsection", "pixel 50 nm\nfield ~100 μm", "grain\norientation,\nphases"),
        ("4  FIB lift-out,\nTEM /\n4D-STEM", "0.1–1 nm\nfield ~μm", "dislocations,\ninterfaces"),
        ("5  Atom-\nprobe\ntomography", "~0.3 nm\nfield ~100 nm", "solute\nsegregation"),
    ]
    fcs = ["#E3EEF8", "#E6F2EC", "#F7EEDF", "#F3E6EF", "#ECECEC"]
    bw, gap, x0 = 2.9, 0.55, 0.15
    links = ["fiducial\nmarks", "registra-\ntion", "site-specific\nlift-out", "inert-gas /\ncryo transfer"]
    for i, (title, scale, q) in enumerate(steps):
        x = x0 + i * (bw + gap)
        box(ax, x, 2.6, bw, 4.9, "", fc=fcs[i])
        ax.text(x + bw / 2, 7.3, title, ha="center", va="top", fontsize=7.6, fontweight="bold")
        ax.text(x + bw / 2, 4.75, scale, ha="center", va="center", fontsize=8, color="0.25")
        ax.text(x + bw / 2, 3.35, "“" + q + "”", ha="center", va="center", fontsize=7.5,
                color=COLORS[0], style="italic")
        if i < 4:
            xa = x + bw + 0.04
            arrow(ax, xa, 4.75, xa + gap - 0.08, 4.75)
            ax.text(xa + gap / 2 - 0.02, 2.45, links[i], ha="center", va="top", fontsize=6.6,
                    color="0.3", rotation=0)
    # shared data model band on top
    box(ax, 0.15, 8.5, 16.7, 1.0, "shared data model and coordinate system",
        fc="#FFF7D6", fontsize=8.5)
    for i in range(5):
        xc = x0 + i * (bw + gap) + bw / 2
        ax.plot([xc, xc], [7.55, 8.48], color="0.5", lw=0.8, ls=":")
    # bottom bar
    ax.annotate("", xy=(16.85, 0.55), xytext=(0.15, 0.55),
                arrowprops=dict(arrowstyle="-|>", lw=2.2, color=COLORS[1], mutation_scale=15))
    ax.text(8.5, 0.75, "increasing resolution, decreasing volume examined (cm$^3$ → (100 nm)$^3$ ≈ 10$^{15}$ ×)",
            ha="center", va="bottom", fontsize=8.3, color=COLORS[1])
    save(fig, "54", "fig-54-6-correlative-workflow")


if __name__ == "__main__":
    insitu_holder_types()
    micropillar_size_effect()
    operando_xrd_graphite()
    positron_lifetime_spectrum()
    mossbauer_steel_rust()
    correlative_workflow()
