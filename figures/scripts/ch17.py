"""Figures for Chapter 17 — Ceramics and Glasses.

Run from the repository root:  python figures/scripts/ch17.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle
from matplotlib.collections import LineCollection
from scipy.spatial import Voronoi
from scipy.optimize import minimize, curve_fit
from scipy.special import erfinv

from figstyle import new_fig, save, COLORS, INK

RNG = np.random.default_rng(17)


# ---------------------------------------------------------------- 17.1
def _neck_outline(a, c, x, n=80):
    """Outline of two spheres (radius a, centres ±c) joined by a neck of radius x."""
    rho = (c ** 2 + x ** 2 - a ** 2) / (2 * (a - x))
    h = x + rho
    phi = np.arctan2(h, -c)                  # tangent angle on the right sphere
    psi = np.arctan2(h, c)                   # tangent angle on the fillet circle
    pts = []
    th = np.linspace(phi, -phi, n)           # right sphere, outer arc
    pts += list(zip(c + a * np.cos(th), a * np.sin(th)))
    th = np.linspace(psi, np.pi - psi, 20)   # bottom fillet
    pts += list(zip(rho * np.cos(th), -h + rho * np.sin(th)))
    th = np.linspace(-(np.pi - phi), -(np.pi + phi), n)              # left sphere
    pts += list(zip(-c + a * np.cos(th), a * np.sin(th)))
    th = np.linspace(np.pi + psi, 2 * np.pi - psi, 20)               # top fillet
    pts += list(zip(rho * np.cos(th), h + rho * np.sin(th)))
    return np.array(pts), rho, h


def _voronoi_graph(pts):
    vor = Voronoi(pts)
    edges = [tuple(r) for r in vor.ridge_vertices if -1 not in r]
    return vor, edges


def fig_sintering_stages():
    """Three stages of sintering, six transport paths, density–time curves."""
    fig = plt.figure(figsize=(6.8, 5.6))
    grain = "#D9CBB0"
    # ---------------- top row: stages
    w = 0.30
    titles = ["(a) initial stage", "(b) intermediate stage", "(c) final stage"]
    axs = [fig.add_axes([0.02 + i * 0.33, 0.62, w, 0.33]) for i in range(3)]
    for ax, t in zip(axs, titles):
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(t, fontsize=8.5, loc="left", pad=2)
    # (a)
    ax = axs[0]
    out, rho, h = _neck_outline(1.0, 0.98, 0.38)
    ax.add_patch(Polygon(out, closed=True, fc=grain, ec=INK, lw=1.0))
    ax.plot([0, 0], [-0.38, 0.38], color=INK, lw=0.7, ls="--")
    ax.annotate("", xy=(0.02, 0.38), xytext=(0.02, 0.0),
                arrowprops=dict(arrowstyle="-|>", lw=0.9, color=COLORS[1], mutation_scale=7))
    ax.text(0.10, 0.12, "$x$", fontsize=10, color=COLORS[1])
    ax.annotate("", xy=(0.98 + 0.707, 0.707), xytext=(0.98, 0.0),
                arrowprops=dict(arrowstyle="-|>", lw=0.9, color=COLORS[0], mutation_scale=7))
    ax.text(1.42, 0.22, "$a$", fontsize=10, color=COLORS[0])
    ax.text(0, -1.25, "neck radius $x$, particle radius $a$", fontsize=7.5, ha="center")
    ax.set_xlim(-2.1, 2.1)
    ax.set_ylim(-1.45, 1.15)
    # (b) and (c): Voronoi grains
    g = np.mgrid[0:7, 0:7].reshape(2, -1).T.astype(float)
    g[:, 0] += 0.5 * (g[:, 1] % 2)
    g[:, 1] *= 0.866
    g += RNG.normal(0, 0.10, g.shape)
    vor, edges = _voronoi_graph(g)
    V = vor.vertices
    for ax, stage in ((axs[1], "int"), (axs[2], "fin")):
        ax.set_facecolor("white")
        ax.add_patch(Polygon([[0.8, 0.6], [5.6, 0.6], [5.6, 4.6], [0.8, 4.6]], closed=True,
                             fc=grain, ec="none", zorder=0))
        segs = [V[list(e)] for e in edges]
        lc = LineCollection(segs, colors=INK, linewidths=0.8 if stage == "int" else 0.7)
        ax.add_collection(lc)
        inside = [(i, v) for i, v in enumerate(V) if 0.8 < v[0] < 5.6 and 0.6 < v[1] < 4.6]
        if stage == "int":
            # continuous channels: dark pores along every edge, wider at corners
            lc2 = LineCollection(segs, colors="#2B2B2B", linewidths=2.0)
            ax.add_collection(lc2)
            for i, v in enumerate(V):
                ax.add_patch(Circle(v, 0.10, fc="#2B2B2B", ec="none"))
            cap = "pore channels along grain\nedges, still connected"
        else:
            for i, v in inside:
                if RNG.random() < 0.55:
                    ax.add_patch(Circle(v, 0.09, fc="#2B2B2B", ec="none"))
            for p in ([2.35, 2.55], [4.05, 1.55], [3.0, 3.75]):
                ax.add_patch(Circle(p, 0.07, fc="#2B2B2B", ec="none"))
                ax.add_patch(Circle(p, 0.20, fc="none", ec=COLORS[1], lw=0.9))
            cap = "isolated pores at grain corners;\ncircled: trapped inside grains"
        ax.text(0.5, -0.03, cap, fontsize=7.2, ha="center", va="top", transform=ax.transAxes)
        ax.set_xlim(0.8, 5.6)
        ax.set_ylim(0.6, 4.6)
        ax.plot([0.8, 5.6, 5.6, 0.8, 0.8], [0.6, 0.6, 4.6, 4.6, 0.6], color=INK, lw=0.8,
                clip_on=False)

    # ---------------- bottom left: transport paths
    ax = fig.add_axes([0.0, 0.03, 0.50, 0.55])
    ax.set_aspect("equal")
    ax.axis("off")
    a, c, x = 1.0, 0.96, 0.45
    out, rho, h = _neck_outline(a, c, x)
    ax.add_patch(Polygon(out, closed=True, fc=grain, ec=INK, lw=1.0))
    ax.plot([0, 0], [-x, x], color=INK, lw=1.0)
    ax.annotate("grain boundary", xy=(0.0, 0.15), xytext=(-0.85, 0.15), fontsize=6.8,
                ha="center", va="center", arrowprops=dict(arrowstyle="-", lw=0.6))
    blue, red = COLORS[0], COLORS[1]

    def carrow(p0, p1, rad, col):
        ax.annotate("", xy=p1, xytext=p0,
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=1.2, mutation_scale=9,
                                    connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0))

    def tag(p, n, col):
        ax.add_patch(Circle(p, 0.11, fc="white", ec=col, lw=1.0, zorder=5))
        ax.text(p[0], p[1], str(n), fontsize=7.5, ha="center", va="center", color=col, zorder=6)
    nk = (0.0, x)          # top neck surface point
    nkb = (0.0, -x)
    # 1 surface diffusion (right sphere surface to neck, just outside)
    s1 = (c + a * np.cos(np.radians(105)), a * np.sin(np.radians(105)))
    carrow((s1[0] + 0.02, s1[1] + 0.07), (0.12, x + 0.08), 0.25, blue)
    tag((0.52, 1.17), 1, blue)
    # 2 lattice diffusion from surface (through right particle interior)
    s2 = (c + a * np.cos(np.radians(70)), a * np.sin(np.radians(70)) - 0.05)
    carrow(s2, (0.10, x - 0.06), -0.45, blue)
    tag((0.95, 0.45), 2, blue)
    # 3 evaporation–condensation (through the pore, from left particle)
    s3 = (-c + a * np.cos(np.radians(65)), a * np.sin(np.radians(65)) + 0.04)
    carrow(s3, (-0.1, x + 0.1), 0.45, blue)
    tag((-0.38, 1.12), 3, blue)
    # 4 grain-boundary diffusion (bottom neck)
    ax.plot([0, 0], [-0.02, -x + 0.06], color=red, lw=2.2, alpha=0.6)
    carrow((0.0, -0.20), (0.0, -x + 0.03), 0.0, red)
    tag((-0.17, -0.12), 4, red)
    # 5 lattice diffusion from the grain boundary (through the right grain)
    carrow((0.03, -0.06), (0.14, -x - 0.02), -1.1, red)
    tag((0.58, -0.12), 5, red)
    # 6 plastic / viscous flow (bulk of the left grain toward the neck)
    carrow((-0.75, -0.35), (-0.14, -x - 0.03), 0.25, red)
    tag((-0.85, -0.50), 6, red)
    ax.set_xlim(-2.05, 2.05)
    ax.set_ylim(-2.75, 1.45)
    ax.text(-2.0, 1.40, "(d) transport paths at a neck", fontsize=8.5, va="top")
    ax.text(-1.95, -1.12,
            "non-densifying (neck grows, no shrinkage):\n"
            "  1 surface diffusion   2 lattice diffusion from surface\n"
            "  3 evaporation–condensation", fontsize=7.2, va="top", color=blue)
    ax.text(-1.95, -1.90,
            "densifying (particle centres approach):\n"
            "  4 grain-boundary diffusion   5 lattice diffusion from g.b.\n"
            "  6 plastic / viscous flow", fontsize=7.2, va="top", color=red)

    # ---------------- bottom right: density vs time
    bx = fig.add_axes([0.60, 0.10, 0.38, 0.43])
    t = np.linspace(0, 4, 400)
    ss = 0.55 + 0.43 * (1 - np.exp(-(t / 1.1) ** 1.1))
    lp = (0.55 + 0.27 * (1 - np.exp(-t / 0.06)) + 0.14 * (1 - np.exp(-t / 0.45))
          + 0.032 * (1 - np.exp(-t / 1.5)))
    bx.plot(t, ss, color=COLORS[0], label="solid-state")
    bx.plot(t, lp, color=COLORS[1], label="liquid-phase")
    for yv, lab in ((0.65, "initial | intermediate"), (0.92, "intermediate | final")):
        bx.axhline(yv, color="0.6", ls=":", lw=0.9)
    bx.text(3.95, 0.635, "initial", fontsize=7, ha="right", va="top", color="0.35")
    bx.text(3.95, 0.66, "intermediate", fontsize=7, ha="right", va="bottom", color="0.35")
    bx.text(3.95, 0.905, "", fontsize=7)
    bx.text(3.95, 0.928, "final", fontsize=7, ha="right", va="bottom", color="0.35")
    bx.annotate("rearrangement", xy=(0.06, 0.76), xytext=(0.45, 0.60), fontsize=7,
                color=COLORS[1], arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[1]))
    bx.annotate("solution–\nprecipitation", xy=(0.6, 0.925), xytext=(1.35, 0.775), fontsize=7,
                color=COLORS[1], arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[1]))
    bx.annotate("solid skeleton", xy=(2.6, 0.983), xytext=(1.9, 1.005), fontsize=7,
                color=COLORS[1], va="bottom",
                arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[1]))
    bx.set_xlim(0, 4)
    bx.set_ylim(0.55, 1.03)
    bx.set_yticks([0.55, 0.65, 0.75, 0.85, 0.92, 1.0])
    bx.set_xlabel("Time at temperature (h)", fontsize=9)
    bx.set_ylabel("Relative density", fontsize=9)
    bx.tick_params(labelsize=8)
    bx.legend(loc="lower right", fontsize=7.5, bbox_to_anchor=(1.0, 0.28))
    bx.set_title("(e) densification", fontsize=8.5, loc="left")
    save(fig, "17", "fig-17-1-sintering-stages")


# ---------------------------------------------------------------- 17.2
def fig_weibull():
    """Weibull plot, m = 10 and 20, with volume scaling to 100× effective volume."""
    fig, ax = new_fig(6.4, 4.4)
    s0 = 400.0
    n = 25
    F = (np.arange(1, n + 1) - 0.5) / n
    yy = np.log(-np.log(1 - F))
    for m, c, lab in ((10, COLORS[0], "A: m = 10"), (20, COLORS[2], "B: m = 20")):
        sig = s0 * (-np.log(1 - F)) ** (1 / m) * np.exp(RNG.normal(0, 0.25 / m, n))
        sig = np.sort(sig)
        ax.plot(np.log(sig), yy, "o", color=c, ms=4, mfc="white", mew=1.1)
        xs = np.linspace(np.log(90), np.log(620), 50)
        ax.plot(xs, m * (xs - np.log(s0)), color=c, label=lab + " (test bars)")
    # component line, 100× effective volume
    sc = s0 * 100 ** (-1 / 10)
    xs = np.linspace(np.log(90), np.log(620), 50)
    ax.plot(xs, 10 * (xs - np.log(sc)), color=COLORS[0], ls="--",
            label="A, 100× effective\nvolume (σ × 0.631)")
    # worked-example points at Pf = 1e-4
    yp = np.log(-np.log(1 - 1e-4))
    ax.axhline(yp, color="0.5", ls=":", lw=0.9)
    ax.text(np.log(600), yp - 0.12, "$P_f = 10^{-4}$", fontsize=8, ha="right", va="top",
            color="0.3")
    for sv in (159, 100):
        ax.plot(np.log(sv), yp, "s", color=COLORS[1], ms=6, zorder=5)
        ax.text(np.log(sv) + 0.035, yp - 0.12, f"{sv} MPa", fontsize=8, color=COLORS[1],
                ha="left", va="top")
    ax.axhline(0, color="0.75", lw=0.7)
    ax.text(np.log(92), 0.12, "$P_f$ = 0.632 at $\\sigma_0$", fontsize=7.5, color="0.4")
    ax.set_xlim(np.log(90), np.log(620))
    ax.set_ylim(-10, 2.2)
    ax.set_xlabel("ln(σ / MPa)")
    ax.set_ylabel("ln ln[1/(1 − $P_f$)]")
    ax.legend(loc="lower right", fontsize=7.8, title="$\\sigma_0$ = 400 MPa", title_fontsize=7.8,
              bbox_to_anchor=(1.0, 0.11))
    # top axis in MPa
    top = ax.secondary_xaxis("top", functions=(np.exp, np.log))
    top.set_xticks([100, 150, 200, 300, 400, 600])
    top.set_xticklabels(["100", "150", "200", "300", "400", "600"])
    top.set_xlabel("Strength σ (MPa)")
    ax.spines["top"].set_visible(True)
    # right axis in Pf
    pf = np.array([1e-4, 0.001, 0.01, 0.1, 0.5, 0.9, 0.99])
    right = ax.secondary_yaxis("right", functions=(lambda y: y, lambda y: y))
    right.set_yticks(np.log(-np.log(1 - pf)))
    right.set_yticklabels(["0.0001", "0.001", "0.01", "0.1", "0.5", "0.9", "0.99"])
    right.set_ylabel("Failure probability $P_f$")
    ax.spines["right"].set_visible(True)
    save(fig, "17", "fig-17-2-weibull-plot")


# ---------------------------------------------------------------- 17.3
def fig_volume_temperature():
    """Specific volume vs temperature: crystallization, glass transition, fictive T."""
    fig, ax = new_fig(6.4, 4.3)
    Tm, Tgf, Tgs = 1.0, 0.74, 0.56
    bL, bG = 0.40, 0.11
    VL = lambda T: 1.20 + bL * (T - Tm)

    def glass(T, Tg, w=0.018):
        z = (Tg - T) / w
        sp = np.where(z > 30, z, np.log1p(np.exp(np.clip(z, None, 30))))
        return VL(T) + (bL - bG) * w * sp
    T = np.linspace(0.30, 1.30, 500)
    ax.axvspan(Tgf, Tm, color=COLORS[5], alpha=0.12, lw=0)
    ax.text(0.85, 0.94, "supercooled\nliquid", fontsize=8.5, ha="center", color="#1B5E86")
    TL = T[T >= Tm]
    ax.plot(TL, VL(TL), color=INK, lw=2.0)
    ax.text(1.20, VL(1.20) + 0.012, "liquid", fontsize=9, ha="right", va="bottom")
    Tsc = np.linspace(Tgs - 0.04, Tm, 100)
    ax.plot(Tsc, VL(Tsc), color=INK, lw=1.0, ls=(0, (4, 2)))
    # crystal
    Vc = lambda T: 1.00 + bG * 0.75 * (T - Tm)
    Tc = T[T <= Tm]
    ax.plot(Tc, Vc(Tc), color=COLORS[2], lw=2.0)
    ax.plot([Tm, Tm], [VL(Tm), 1.00], color=COLORS[2], lw=1.4, ls="-")
    ax.annotate("crystallization\nat $T_m$", xy=(Tm, 1.11), xytext=(1.06, 1.06), fontsize=8.5,
                color=COLORS[2], arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[2]))
    ax.text(0.33, Vc(0.33) - 0.008, "crystal", fontsize=9, color=COLORS[2], va="top")
    # glasses
    Ts = T[T <= Tm]
    for Tg, c, lab in ((Tgf, COLORS[1], "fast-cooled glass"), (Tgs, COLORS[0], "slow-cooled glass")):
        ax.plot(Ts[Ts <= Tg + 0.06], glass(Ts[Ts <= Tg + 0.06], Tg), color=c, lw=1.8)
        Tx = np.linspace(Tg, Tg + 0.13, 10)
        ax.plot(Tx, VL(Tg) + bG * (Tx - Tg), color=c, lw=0.9, ls="--")
        ax.plot(Tg, VL(Tg), "o", color=c, ms=4.5, zorder=5)
        up = Tg == Tgf
        yl = (glass(0.36, Tg) + (glass(0.36, Tgs) if up else Vc(0.36))) / 2
        ax.text(0.33, yl, lab, fontsize=8.5, color=c, va="center")
    ax.annotate("$T_{f,\\mathrm{fast}}$", xy=(Tgf, VL(Tgf)), xytext=(Tgf - 0.07, VL(Tgf) + 0.06),
                fontsize=9.5, color=COLORS[1], ha="center",
                arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[1]))
    ax.annotate("$T_{f,\\mathrm{slow}}$", xy=(Tgs, VL(Tgs)), xytext=(Tgs - 0.07, VL(Tgs) + 0.06),
                fontsize=9.5, color=COLORS[0], ha="center",
                arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[0]))
    ax.text(0.31, 1.315, "fictive temperature $T_f$: glass line (dashed)\n"
            "extrapolated to meet the liquid line;\nfaster cooling freezes in a higher $T_f$",
            fontsize=7.5, color="0.3", va="top")
    ax.set_xticks([Tgs, Tgf, Tm])
    ax.set_xticklabels(["$T_{g,\\mathrm{slow}}$", "$T_{g,\\mathrm{fast}}$", "$T_m$"])
    for xv in (Tgs, Tgf, Tm):
        ax.axvline(xv, color="0.8", lw=0.6, zorder=0)
    ax.set_yticks([])
    ax.set_xlim(0.30, 1.30)
    ax.set_ylim(0.91, 1.33)
    ax.set_xlabel("Temperature")
    ax.set_ylabel("Specific volume")
    # inset TTT (lower right, below the liquid line)
    ins = fig.add_axes([0.70, 0.20, 0.24, 0.30])
    Tn, tn = 0.75, 1.0
    TT = np.linspace(0.52, 0.995, 300)
    logt = np.log10(tn) + 1.6 * ((TT - Tn) / 0.12) ** 2 * np.where(TT > Tn, 1.0, 0.55)
    logt += 0.6 / (1.0 - TT + 0.02) - 0.6 / (1 - Tn + 0.02)
    tc = 10 ** logt
    ins.plot(tc, TT, color=INK, lw=1.4)
    rc = np.max((1.0 - TT) / tc)
    tl = np.logspace(-3, 3, 300)
    ins.plot(tl, 1.0 - rc * tl, color=COLORS[1], lw=1.2)
    ins.text(0.0016, 0.58, "$R_c$", color=COLORS[1], fontsize=8.5)
    ins.text(40, 0.80, "crystal", fontsize=7)
    ins.axhline(1.0, color="0.5", lw=0.7, ls=":")
    ins.text(0.0012, 1.005, "$T_m$", fontsize=7.5, va="bottom")
    ins.set_xscale("log")
    ins.set_xlim(1e-3, 1e3)
    ins.set_ylim(0.5, 1.08)
    ins.set_xticks([])
    ins.set_yticks([])
    ins.set_xlabel("log time", fontsize=7.5, labelpad=1)
    ins.set_ylabel("T", fontsize=7.5, labelpad=1)
    ins.set_title("TTT, crystallization", fontsize=7.5, pad=2)
    ins.spines["top"].set_visible(True)
    ins.spines["right"].set_visible(True)
    ax.text(0.31, 1.205, "critical cooling rate $R_c$ (tangent to the nose):\n"
            "SiO$_2$ ~ $10^{-4}$ K/s;  soda-lime ~ $10^{-2}$ K/s;\n"
            "metallic glasses $10^{2}$–$10^{6}$ K/s",
            fontsize=7.5, va="top", color="0.3")
    save(fig, "17", "fig-17-3-volume-temperature")


# ---------------------------------------------------------------- 17.4
def _relax(V, edges, b=1.0, w2=0.4, iters=400):
    """Relax a 3-connected network to equal bond length b and ~120° angles."""
    nb = {i: set() for i in range(len(V))}
    for i, j in edges:
        nb[i].add(j)
        nb[j].add(i)
    pairs2 = set()
    for i in nb:
        L = sorted(nb[i])
        for p in range(len(L)):
            for q in range(p + 1, len(L)):
                pairs2.add((L[p], L[q]))
    P1 = np.array(edges)
    P2 = np.array(sorted(pairs2))
    allp = np.vstack([P1, P2])
    L0 = np.r_[np.full(len(P1), b), np.full(len(P2), b * np.sqrt(3))]
    W = np.r_[np.ones(len(P1)), np.full(len(P2), w2)]

    def f(xf):
        X = xf.reshape(-1, 2)
        d = X[allp[:, 0]] - X[allp[:, 1]]
        L = np.hypot(d[:, 0], d[:, 1]) + 1e-12
        e = W * (L - L0) ** 2
        gcoef = (2 * W * (L - L0) / L)[:, None] * d
        g = np.zeros_like(X)
        np.add.at(g, allp[:, 0], gcoef)
        np.add.at(g, allp[:, 1], -gcoef)
        return e.sum(), g.ravel()
    r = minimize(f, V.ravel(), jac=True, method="L-BFGS-B", options=dict(maxiter=iters))
    return r.x.reshape(-1, 2)


def _network(jitter, seed, n=14):
    rng = np.random.default_rng(seed)
    g = np.mgrid[0:n, 0:n].reshape(2, -1).T.astype(float)
    g[:, 0] += 0.5 * (g[:, 1] % 2)
    g[:, 1] *= np.sqrt(3) / 2
    g = g * np.sqrt(3)          # lattice spacing √3 → honeycomb bond length 1
    g += rng.normal(0, jitter, g.shape)
    vor = Voronoi(g)
    V = vor.vertices.copy()
    ctr = g.mean(axis=0)
    keep = np.hypot(*(V - ctr).T) < 0.42 * n * np.sqrt(3)
    edges = [tuple(r) for r in vor.ridge_vertices
             if -1 not in r and keep[r[0]] and keep[r[1]]]
    rings = []
    for pi, reg in enumerate(vor.point_region):
        R = vor.regions[reg]
        if -1 in R or len(R) == 0 or not all(keep[R]):
            continue
        rings.append(R)
    if jitter > 0:
        V = _relax(V, edges)
    return V, edges, rings, ctr


def _draw_network(ax, V, edges, skip=()):
    for k, (i, j) in enumerate(edges):
        if k in skip:
            continue
        m = (V[i] + V[j]) / 2
        ax.plot([V[i, 0], V[j, 0]], [V[i, 1], V[j, 1]], color="0.45", lw=1.0, zorder=1)
        ax.add_patch(Circle(m, 0.16, fc="white", ec=INK, lw=0.9, zorder=3))
    used = set(i for e in edges for i in e)
    for i in used:
        ax.add_patch(Circle(V[i], 0.075, fc=INK, ec="none", zorder=4))


def fig_zachariasen():
    """2-D crystal, continuous random network and modified (Na) glass."""
    fig, axs = plt.subplots(1, 3, figsize=(6.8, 2.55))
    half = 3.7
    titles = ["(a) crystal", "(b) glass (random network)", "(c) modified glass (+ Na₂O)"]
    Vc, Ec, Rc, cc = _network(0.0, 1)
    Vg, Eg, Rg, cg = _network(0.45, 1)
    nets = [(Vc, Ec, Rc, cc), (Vg, Eg, Rg, cg), (Vg, Eg, Rg, cg)]
    for k, (ax, t, (V, E, R, c0)) in enumerate(zip(axs, titles, nets)):
        ax.set_aspect("equal")
        ax.set_xticks([])
        ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(True)
            s.set_linewidth(0.7)
        ax.set_title(t, fontsize=8.5, loc="left", pad=3)
        # centre the view on the network
        ax.set_xlim(c0[0] - half, c0[0] + half)
        ax.set_ylim(c0[1] - half, c0[1] + half)
        skip = []
        if k == 2:
            # choose bonds near the centre to break
            mids = np.array([(V[i] + V[j]) / 2 for i, j in E])
            dist = np.hypot(*(mids - c0).T)
            cand = np.argsort(dist)
            chosen = []
            for ci in cand:
                if dist[ci] > half - 0.8:
                    break
                if all(np.hypot(*(mids[ci] - mids[q])) > 2.4 for q in chosen):
                    chosen.append(ci)
                if len(chosen) == 4:
                    break
            skip = chosen
        _draw_network(ax, V, E, skip)
        if k == 1:
            # label ring sizes
            for Rr in R:
                cen = V[Rr].mean(axis=0)
                if np.max(np.abs(cen - c0)) < half - 0.7 and len(Rr) != 6:
                    ax.text(cen[0], cen[1], str(len(Rr)), fontsize=8, ha="center",
                            va="center", color=COLORS[1], fontweight="bold")
        if k == 2:
            for q, ci in enumerate(skip):
                i, j = E[ci]
                u = (V[j] - V[i]) / np.hypot(*(V[j] - V[i]))
                pvec = np.array([-u[1], u[0]])
                for (ii, sgn) in ((i, 1), (j, -1)):
                    rot = np.array([[np.cos(0.35), -np.sin(0.35)], [np.sin(0.35), np.cos(0.35)]])
                    d = sgn * u
                    d = rot @ d
                    ax.plot([V[ii, 0], V[ii, 0] + 0.42 * d[0]], [V[ii, 1], V[ii, 1] + 0.42 * d[1]],
                            color="0.45", lw=1.0, zorder=1)
                    ax.add_patch(Circle(V[ii] + 0.42 * d, 0.13, fc=COLORS[1], ec=INK, lw=0.7,
                                        zorder=3))
                m = (V[i] + V[j]) / 2
                for sg in (1, -1):
                    ax.add_patch(Circle(m + sg * 0.62 * pvec, 0.27, fc="white", ec=COLORS[0],
                                        lw=1.3, zorder=5))
                    ax.text(*(m + sg * 0.62 * pvec), "Na⁺", fontsize=5.2, ha="center",
                            va="center", color=COLORS[0], zorder=6)
    # legend under the panels
    from matplotlib.lines import Line2D
    fig.subplots_adjust(bottom=0.12, top=0.90, left=0.01, right=0.99, wspace=0.05)
    hd = [Line2D([], [], ls="", marker="o", ms=3.5, mfc=INK, mec=INK),
          Line2D([], [], ls="", marker="o", ms=7, mfc="white", mec=INK),
          Line2D([], [], ls="", marker="o", ms=6, mfc=COLORS[1], mec=INK),
          Line2D([], [], ls="", marker="o", ms=11, mfc="white", mec=COLORS[0], mew=1.3),
          Line2D([], [], ls="", marker="$5$", ms=7, color=COLORS[1])]
    fig.legend(hd, ["network cation (Si, B)", "bridging O", "non-bridging O (NBO)",
                    "Na⁺ modifier ion", "ring size ≠ 6"],
               loc="lower center", ncol=5, fontsize=7.5, handletextpad=0.3, columnspacing=1.2,
               bbox_to_anchor=(0.5, 0.0))
    save(fig, "17", "fig-17-4-zachariasen-network")


# ---------------------------------------------------------------- 17.5
def _vft(T, A, B, T0):
    return A + B / (T - T0)


def fig_viscosity():
    """log viscosity vs temperature for soda-lime, borosilicate and fused silica."""
    fig, ax = new_fig(6.4, 4.4)
    T = np.linspace(400, 1800, 800)
    # soda-lime: text VFT
    sl = _vft(T, -4.57, 6370, 160)
    # borosilicate: VFT fitted to the four reference points
    Tb = np.array([510, 560, 821, 1252.0])
    yb = np.array([13.5, 12.0, 6.6, 3.0])
    pb, _ = curve_fit(_vft, Tb, yb, p0=(-3, 6000, 200), maxfev=20000)
    bs = _vft(T, *pb)
    # fused silica: Arrhenius through annealing 1100 °C (12) and softening 1600 °C (6.6)
    T1, T2 = 1100 + 273.15, 1600 + 273.15
    Bs = (12 - 6.6) / (1 / T1 - 1 / T2)
    As = 12 - Bs / T1
    fs = As + Bs / (T + 273.15)
    # bands
    ax.axhspan(3, 6.6, color=COLORS[4], alpha=0.13, lw=0)
    ax.axhspan(12, 13.5, color=COLORS[2], alpha=0.15, lw=0)
    ax.text(1450, 4.8, "forming\n(pressing, blowing, float)", fontsize=7.5, ha="center",
            va="center", color="#8A5A00")
    ax.text(1450, 12.75, "annealing range", fontsize=7.5, ha="center", va="center",
            color="#00684A")
    for yv, lab in ((13.5, "strain 13.5"), (12, "annealing 12"), (6.6, "softening 6.6"),
                    (3, "working 3")):
        ax.axhline(yv, color="0.5", ls="--", lw=0.8)
        ax.text(1798, yv + 0.12, lab, fontsize=7, ha="right", va="bottom", color="0.3")
    m = (sl > -1) & (sl < 18.5) & (T > 160)
    ax.plot(T[m], sl[m], color=COLORS[0], lw=2, label="soda-lime")
    m = (bs < 18.5)
    ax.plot(T[m], bs[m], color=COLORS[3], lw=2, label="borosilicate")
    m = (fs < 18.5)
    ax.plot(T[m], fs[m], color=COLORS[1], lw=2, label="fused silica")
    # reference points
    for pts, c in (([511, 548, 726, 1005], COLORS[0]), (list(Tb), COLORS[3]),
                   ([1000, 1100, 1600], COLORS[1])):
        ys = {COLORS[0]: lambda x: _vft(np.array(x), -4.57, 6370, 160),
              COLORS[3]: lambda x: _vft(np.array(x), *pb),
              COLORS[1]: lambda x: As + Bs / (np.array(x) + 273.15)}[c](pts)
        ax.plot(pts, ys, "o", color=c, ms=4.5, mfc="white", mew=1.2, zorder=5)
    # tempering
    ax.plot([620, 650], _vft(np.array([620, 650]), -4.57, 6370, 160), color=INK, lw=5,
            alpha=0.35, solid_capstyle="butt")
    ax.annotate("tempering quench\nstart 620–650 °C", xy=(640, 8.8), xytext=(700, 10.4),
                fontsize=7.5, arrowprops=dict(arrowstyle="-", lw=0.7))
    # worked-example points
    for Tw, yw in ((500, 14.17), (450, 17.40)):
        ax.plot(Tw, yw, "D", color=COLORS[0], ms=5, zorder=6)
    ax.annotate("500 °C: 14.2 (τ ≈ 1.4 h)", xy=(500, 14.17), xytext=(560, 15.4), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", lw=0.7))
    ax.annotate("450 °C: 17.4 (τ ≈ 97 d)", xy=(450, 17.40), xytext=(510, 17.4), fontsize=7.5,
                va="center", arrowprops=dict(arrowstyle="-", lw=0.7))
    ax.set_xlim(400, 1800)
    ax.set_ylim(0, 18)
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("log$_{10}$ viscosity (Pa s)")
    ax.legend(loc="lower left", fontsize=8, bbox_to_anchor=(0.0, 0.0))
    print("borosilicate VFT fit A, B, T0 =", np.round(pb, 2),
          "resid", np.round(_vft(Tb, *pb) - yb, 2))
    print("fused silica Arrhenius A, B(K) =", round(As, 2), round(Bs))
    save(fig, "17", "fig-17-5-glass-viscosity")


# ---------------------------------------------------------------- 17.6
def fig_residual_stress():
    """Residual-stress profiles: thermally tempered sheet and ion-exchanged cover glass."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.8, 3.6))
    fig.subplots_adjust(wspace=0.35)
    z = np.linspace(0, 1, 400)
    s = 50 - 150 * (2 * z - 1) ** 2
    a1.fill_between(z, s, 0, where=s < 0, color=COLORS[0], alpha=0.18, lw=0)
    a1.fill_between(z, s, 0, where=s > 0, color=COLORS[1], alpha=0.18, lw=0)
    a1.plot(z, s, color=INK)
    a1.axhline(0, color="0.4", ls="--", lw=0.8)
    for zz in (0.211, 0.789):
        a1.plot(zz, 0, "o", color=INK, ms=4)
    a1.text(0.19, 4, "0.211", fontsize=7.5, ha="right")
    a1.text(0.81, 4, "0.789", fontsize=7.5, ha="left")
    a1.text(0.5, 53, "+50 MPa (mid-plane tension)", fontsize=7.5, ha="center", va="bottom")
    a1.text(0.03, -104, "−100 MPa", fontsize=7.5, va="top")
    a1.text(0.97, -104, "−100 MPa", fontsize=7.5, va="top", ha="right")
    a1.annotate("20 μm flaw inside\ncompressive layer\n(1.27 mm deep)", xy=(0.004, -98),
                xytext=(0.11, -60), fontsize=7.2,
                arrowprops=dict(arrowstyle="-|>", lw=0.8, mutation_scale=7))
    a1.plot([0, 0.0033], [-100, -100], color=COLORS[1], lw=4, solid_capstyle="butt")
    a1.set_xlim(0, 1)
    a1.set_ylim(-120, 65)
    a1.set_xlabel("Position through thickness, z/t")
    a1.set_ylabel("Residual stress (MPa), compression < 0")
    a1.set_title("(a) thermally tempered, 6 mm soda-lime", fontsize=8.5, loc="left")

    t, dol, cs = 700.0, 40.0, 700.0
    ct = cs * dol / (t - 2 * dol)
    d = np.linspace(0, t, 1401)
    prof = np.full_like(d, ct)
    m1 = d < dol
    prof[m1] = -cs * (1 - d[m1] / dol)
    m2 = d > t - dol
    prof[m2] = -cs * (1 - (t - d[m2]) / dol)
    # make the profile continuous at the layer edge (tension starts at DOL)
    a2.fill_between(d, prof, 0, where=prof < 0, color=COLORS[0], alpha=0.18, lw=0)
    a2.fill_between(d, prof, 0, where=prof > 0, color=COLORS[1], alpha=0.18, lw=0)
    a2.plot(d, prof, color=INK)
    a2.axhline(0, color="0.4", ls="--", lw=0.8)
    a2.text(350, ct + 12, f"central tension +{ct:.0f} MPa", fontsize=7.5, ha="center",
            va="bottom")
    a2.text(62, -620, "CS = −700 MPa", fontsize=7.5, va="center")
    a2.text(dol + 6, -60, "DOL 40 μm", fontsize=7.5, va="top")
    a2.annotate("20 μm flaw inside\ncompressive layer", xy=(22, -735), xytext=(300, -700),
                fontsize=7.2, arrowprops=dict(arrowstyle="-|>", lw=0.8, mutation_scale=7))
    a2.plot([0, 20], [-740, -740], color=COLORS[1], lw=5, solid_capstyle="butt", clip_on=False)
    a2.set_xlim(0, 700)
    a2.set_ylim(-750, 100)
    a2.set_xlabel("Depth from surface (μm)")
    a2.set_ylabel("Residual stress (MPa)")
    a2.set_title("(b) ion-exchanged, 0.7 mm cover glass", fontsize=8.5, loc="left")
    save(fig, "17", "fig-17-6-residual-stress-profiles")


if __name__ == "__main__":
    fig_sintering_stages()
    fig_weibull()
    fig_volume_temperature()
    fig_zachariasen()
    fig_viscosity()
    fig_residual_stress()
