"""Figures for Chapter 8 — Diffusion in Solids.

Run from the repository root:  python figures/scripts/ch08.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
from scipy.special import erfc, erfinv

R = 8.314
HOST = "#BBBBBB"


# ---------------------------------------------------------------- Figure 8.1
def fick_solutions():
    fig, (a, b) = plt.subplots(1, 2, figsize=(6.6, 3.4), sharex=True)
    xi = np.linspace(0, 4, 400)          # x / L, L = 2 sqrt(D t1)
    times = [(1, "$t_1$"), (4, "$4t_1$"), (16, "$16t_1$")]
    for (m, lab), c in zip(times, COLORS[:3]):
        g = np.exp(-xi**2 / m) / np.sqrt(m)
        a.plot(xi, g, color=c, label=f"t = {lab}")
        a.fill_between(xi, 0, g, color=c, alpha=0.12, lw=0)
        e = erfc(xi / np.sqrt(m))
        b.plot(xi, e, color=c, label=f"t = {lab}")
        xq = erfinv(0.75) * np.sqrt(m)
        b.plot([xq, xq], [0, 0.25], ":", color=c, lw=1)
        b.plot(xq, 0.25, "o", color=c, ms=4)
        b.text(xq + 0.04, 0.02, f"{xq:.2f}", color=c, fontsize=7.5, ha="left", va="bottom")
    a.set_xlim(0, 4); a.set_ylim(0, 1.05)
    a.set_xlabel(r"Depth $x/L$,  $L=2\sqrt{Dt_1}$")
    a.set_ylabel(r"$C\,/\,(Q/\sqrt{\pi D t_1})$")
    a.legend(fontsize=8, loc="upper right")
    a.text(1.35, 0.60, "constant dose $Q$:\nequal areas", fontsize=8)
    a.text(2.1, 0.36, "amplitude halves,\nwidth doubles\nfor each 4× in t", fontsize=7.5, color="0.3")
    a.set_title("(a) thin-film source (Gaussian)", loc="left", fontsize=10)
    b.axhline(0.25, color="0.4", ls="--", lw=1)
    b.text(2.0, 0.62, r"$x\propto\sqrt{Dt}$:" + "\n4× time → 2× depth", fontsize=8.5)
    b.set_ylim(0, 1.05)
    b.set_xlabel(r"Depth $x/L$,  $L=2\sqrt{Dt_1}$")
    b.set_ylabel(r"$(C-C_0)\,/\,(C_s-C_0)$")
    b.legend(fontsize=8, loc="upper right")
    b.set_title("(b) constant surface concentration (erfc)", loc="left", fontsize=10)
    fig.tight_layout(w_pad=1.5)
    save(fig, "08", "fig-8-1-fick-solutions")


# ---------------------------------------------------------------- Figure 8.2
def _lattice(ax, skip=(), nx=5, ny=4, r=0.36):
    for i in range(nx):
        for j in range(ny):
            if (i, j) in skip:
                continue
            ax.add_patch(Circle((i, j), r, fc=HOST, ec="0.45", lw=0.6))
    ax.set_xlim(-0.6, nx - 0.4); ax.set_ylim(-0.75, ny - 0.4); ax.set_aspect("equal"); ax.axis("off")


def _arr(ax, p0, p1, color, ls="-", rad=0.0, lw=1.4):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=11, color=color, lw=lw,
                                 linestyle=ls, connectionstyle=f"arc3,rad={rad}", zorder=6))


def diffusion_mechanisms():
    fig = plt.figure(figsize=(6.8, 3.7))
    axs = [fig.add_axes([0.01 + 0.33 * k, 0.33, 0.31, 0.64]) for k in range(3)]
    # (a) vacancy
    ax = axs[0]
    _lattice(ax, skip=[(2, 1)])
    ax.add_patch(Circle((2, 1), 0.36, fc="white", ec="0.45", lw=0.8, ls="--"))
    ax.add_patch(Circle((1, 1), 0.36, fc=COLORS[0], ec=INK, lw=0.8, zorder=5))
    _arr(ax, (1.25, 1.18), (1.78, 1.18), COLORS[0], rad=-0.4)
    ax.text(1.5, 1.62, "atom →", fontsize=7.5, ha="center", color=COLORS[0], zorder=7,
            bbox=dict(fc="white", ec="none", pad=0.3))
    _arr(ax, (1.78, 0.80), (1.25, 0.80), "0.3", ls="--", rad=-0.4)
    ax.text(1.5, 0.30, "vacancy ←", fontsize=7.5, ha="center", color="0.3", zorder=7,
            bbox=dict(fc="white", ec="none", pad=0.3))
    ax.text(2.0, -0.62, r"(a) vacancy: $Q=H_f+H_m$", fontsize=9, ha="center")
    # (b) interstitial
    ax = axs[1]
    _lattice(ax)
    for (x, y) in [(0.5, 2.5), (3.5, 0.5), (3.5, 2.5)]:
        ax.add_patch(Circle((x, y), 0.13, fc=COLORS[1], ec=INK, lw=0.5, zorder=5))
    ax.add_patch(Circle((1.5, 1.5), 0.13, fc=COLORS[1], ec=INK, lw=0.8, zorder=5))
    ax.add_patch(Circle((2.5, 1.5), 0.13, fc="white", ec=COLORS[1], lw=0.8, ls="--", zorder=5))
    _arr(ax, (1.65, 1.5), (2.35, 1.5), COLORS[1])
    ax.text(2.0, -0.62, r"(b) interstitial: $Q=H_m$", fontsize=9, ha="center")
    # (c) interstitialcy
    ax = axs[2]
    _lattice(ax, skip=[(2, 2)])
    ax.add_patch(Circle((2, 2), 0.36, fc="#8FB8D8", ec=INK, lw=0.8, zorder=4))
    ax.add_patch(Circle((1.5, 1.5), 0.30, fc=COLORS[0], ec=INK, lw=0.8, zorder=5))
    _arr(ax, (1.68, 1.68), (1.86, 1.86), COLORS[0], lw=1.6)
    _arr(ax, (2.18, 2.18), (2.42, 2.42), "#3A6F99", lw=1.6)
    ax.add_patch(Circle((2.5, 2.5), 0.30, fc="none", ec="#3A6F99", lw=0.9, ls="--", zorder=5))
    ax.text(0.95, 3.25, "self-interstitial\npushes lattice atom", fontsize=7, ha="left", va="bottom")
    ax.text(2.0, -0.62, "(c) interstitialcy", fontsize=9, ha="center")
    # energy strip
    e = fig.add_axes([0.10, 0.08, 0.84, 0.20])
    s = np.linspace(0, 3, 600)
    E = 0.5 * (1 - np.cos(2 * np.pi * s))
    e.plot(s, E, color=INK)
    e.set_xlim(0, 3); e.set_ylim(-0.25, 1.35)
    e.set_xticks([]); e.set_yticks([])
    e.set_xlabel("reaction coordinate (position along jump path)", fontsize=8.5)
    e.set_ylabel("energy", fontsize=8.5)
    e.annotate("", xy=(1.5, 1.0), xytext=(1.5, 0.0),
               arrowprops=dict(arrowstyle="<|-|>", color=COLORS[1], lw=1, mutation_scale=8))
    e.text(1.54, 0.45, "$H_m$", fontsize=9, color=COLORS[1])
    e.text(1.5, 1.05, "saddle point", fontsize=7.5, ha="center", va="bottom")
    e.annotate("", xy=(2.0, -0.12), xytext=(1.0, -0.12),
               arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=0.9, mutation_scale=8))
    e.text(1.5, -0.10, r"jump distance $\lambda$", fontsize=7.5, ha="center", va="bottom")
    for xs in [1, 2]:
        e.plot(xs, 0, "o", color=COLORS[0], ms=4)
    save(fig, "08", "fig-8-2-diffusion-mechanisms")


# ---------------------------------------------------------------- Figure 8.3
DATA = [  # label, D0, Q (kJ/mol), Tmin °C, Tmax °C, colour, style
    ("H in α-Fe", 7e-8, 6, 20, 912, COLORS[5], "-"),
    ("C in α-Fe", 1.1e-6, 87, 20, 912, COLORS[0], "-"),
    ("C in γ-Fe", 2.3e-5, 148, 900, 1400, COLORS[0], "-"),
    ("Fe in α-Fe", 2.8e-4, 251, 400, 912, COLORS[1], "--"),
    ("Fe in γ-Fe", 5.0e-5, 284, 912, 1394, COLORS[1], "--"),
    ("Cu in Cu", 7.8e-5, 211, 300, 1085, COLORS[4], "--"),
    ("Al in Al", 2.3e-4, 144, 200, 660, COLORS[2], "--"),
    ("Cu in Al", 6.5e-5, 136, 200, 660, COLORS[3], "--"),
    ("B in Si", 7.6e-5, 334, 800, 1200, "0.25", ":"),
    ("P in Si", 3.9e-4, 353, 800, 1200, "0.55", ":"),
]


def arrhenius_plot():
    fig, ax = new_fig(6.4, 4.6)
    ax.axhspan(-13, -12, color=COLORS[6], alpha=0.35, lw=0)
    ax.text(3.45, -13.15, r"solid metals near $T_m$: $D\approx10^{-13}$–$10^{-12}$ m²/s (band)", fontsize=7.5,
            ha="right", va="top")
    for lab, D0, Q, t0, t1, c, ls in DATA:
        T = np.linspace(t0, t1, 100) + 273.15
        y = np.log10(D0) - Q * 1e3 / (2.303 * R * T)
        ax.plot(1000 / T, y, color=c, ls=ls, lw=1.8, label=lab)
    # slope triangle on C in alpha-Fe
    D0, Q = 1.1e-6, 87
    x1, x2 = 1.6, 2.2
    f = lambda x: np.log10(D0) - Q * 1e3 / (2.303 * R) * x / 1000
    ax.plot([x1, x2, x2], [f(x1), f(x1), f(x2)], color="0.35", lw=0.9)
    ax.text(x2 + 0.04, (f(x1) + f(x2)) / 2 - 0.3, "slope = $-Q/(2.303R)$", fontsize=7.5, va="center", color="0.25")
    # melting-point markers
    for lab, Tm in [("Cu in Cu", 1085), ("Al in Al", 660)]:
        d = [r for r in DATA if r[0] == lab][0]
        T = Tm + 273.15
        ax.plot(1000 / T, np.log10(d[1]) - d[2] * 1e3 / (2.303 * R * T), "o", color=d[5], ms=5, mec=INK, mew=0.6)
    ax.plot(0.66, -23.2, "o", color="white", ms=5, mec=INK, mew=0.6)
    ax.text(0.70, -23.2, "= melting point (Cu, Al)", fontsize=7, va="center", color="0.3")
    ax.legend(ncol=2, fontsize=7.3, loc="upper right", bbox_to_anchor=(1.0, 0.985), frameon=True,
              framealpha=1, edgecolor="none", handlelength=2.4, columnspacing=1.0, labelspacing=0.3)
    ax.set_xlim(0.6, 3.5); ax.set_ylim(-24, -8)
    ax.set_xlabel("$1000/T$ (K$^{-1}$)")
    ax.set_ylabel(r"$\log_{10} D$ (m$^2$/s)")
    top = ax.secondary_xaxis("top", functions=(lambda x: 1000 / np.maximum(x, 1e-6) - 273.15,
                                               lambda t: 1000 / (np.asarray(t) + 273.15)))
    top.set_ticks([1200, 800, 600, 400, 200, 100, 25])
    top.set_xlabel("Temperature (°C)", fontsize=9)
    top.tick_params(labelsize=8)
    save(fig, "08", "fig-8-3-arrhenius-plot")


# ---------------------------------------------------------------- Figure 8.4
def kirkendall_effect():
    fig = plt.figure(figsize=(6.4, 4.8))
    top = fig.add_axes([0.06, 0.66, 0.9, 0.30])
    top.set_xlim(-5, 5); top.set_ylim(-0.6, 2.4); top.axis("off")
    top.add_patch(Rectangle((-4.5, 0), 4.5, 1.8, fc="#E8A97A", ec=INK, lw=1))
    top.add_patch(Rectangle((0, 0), 4.5, 1.8, fc="#F2D98A", ec=INK, lw=1))
    top.text(-2.25, 0.9, "Cu", ha="center", va="center", fontsize=11)
    top.text(2.25, 0.9, "α-brass (Cu–30Zn)", ha="center", va="center", fontsize=10)
    for y in np.linspace(0.2, 1.6, 6):
        top.add_patch(Circle((0, y), 0.07, fc=INK, ec=INK, transform=top.transData, zorder=5))
    top.text(0, -0.12, "Mo marker wires, x = 0", ha="center", va="top", fontsize=8)
    top.text(-4.9, 2.2, "(a) before annealing", fontsize=9.5, ha="left", va="top")
    ax = fig.add_axes([0.11, 0.10, 0.84, 0.46])
    x = np.linspace(-150, 150, 400)       # µm
    dx = 20.0
    c = 30 * 0.5 * erfc(-(x - 0) / 60)    # wt% Zn
    ax.axvspan(-150, 0, color="#E8A97A", alpha=0.25, lw=0)
    ax.axvspan(0, 150, color="#F2D98A", alpha=0.35, lw=0)
    ax.plot(x, c, color=COLORS[0], lw=2)
    ax.text(-140, 33, "Zn profile after\n785 °C anneal", fontsize=8, color=COLORS[0], va="top")
    ax.axvline(0, color="0.5", ls=":", lw=1)
    ax.axvline(dx, color=INK, ls="--", lw=1)
    for y in np.linspace(3, 25, 6):
        ax.plot(dx, y, "o", color=INK, ms=4)
        ax.plot(0, y, "o", mfc="white", mec="0.5", ms=4)
    ax.annotate("", xy=(dx, 27.5), xytext=(0, 27.5), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1,
                                                                     mutation_scale=8))
    ax.text(dx / 2, 28.3, "Δx", ha="center", va="bottom", fontsize=9)
    ax.text(-3, 27.5, "original\ninterface", fontsize=7, ha="right", va="center", color="0.4")
    ax.text(dx + 3, 30.5, "markers", fontsize=7.5, ha="left", va="center")
    rng = np.random.default_rng(4)
    for _ in range(9):
        vx, vy = dx + rng.uniform(12, 55), rng.uniform(4, 24)
        ax.plot(vx, vy, "o", mfc="white", mec=INK, ms=rng.uniform(3, 5.5), mew=0.8, zorder=4)
    ax.text(95, 6, "Kirkendall\nvoids", fontsize=8, ha="center", va="center")
    # fluxes
    ax.annotate("", xy=(-90, 17), xytext=(10, 17), arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=2.2,
                                                                   mutation_scale=13))
    ax.text(-40, 18.2, r"$J_{Zn}$ (fast)", color=COLORS[1], fontsize=9, ha="center", va="bottom")
    ax.annotate("", xy=(-10, 11), xytext=(-45, 11), arrowprops=dict(arrowstyle="-|>", color=COLORS[2], lw=2.2,
                                                                     mutation_scale=13))
    ax.text(-28, 9.8, r"$J_{Cu}$ (slow)", color=COLORS[2], fontsize=9, ha="center", va="top")
    ax.annotate("", xy=(70, 33), xytext=(25, 33), arrowprops=dict(arrowstyle="-|>", color=COLORS[3], lw=1.8,
                                                                  mutation_scale=12))
    ax.text(73, 33, r"$J_v$ (net vacancy flux)", color=COLORS[3], fontsize=8, va="center")
    ax.set_xlim(-150, 150); ax.set_ylim(0, 37)
    ax.set_xlabel("Position x (µm)")
    ax.set_ylabel("Zn (wt%)")
    fig.text(0.02, 0.585, "(b) after annealing at 785 °C", fontsize=9.5, ha="left", va="center")
    save(fig, "08", "fig-8-4-kirkendall-effect")


# ---------------------------------------------------------------- Figure 8.5
def harrison_regimes():
    fig = plt.figure(figsize=(6.8, 4.9))
    W, H = 3.0, 2.4
    X, Y = np.meshgrid(np.linspace(0, W, 360), np.linspace(0, H, 300))
    gbx = [0.5, 1.5, 2.5]
    dist = np.min([np.abs(X - g) for g in gbx], axis=0)
    fields = {}
    # A: overlapping fields -> nearly flat front with shallow bumps
    LA = 0.75
    fields["A"] = erfc(Y / (2 * LA)) * (1 + 0.08 * np.exp(-dist / 0.25))
    # B: lattice part + wedges along boundaries
    Ll = 0.12
    cgb = np.exp(-(Y / 1.1) ** 1.2)
    width = Ll * 1.6 * (1 - 0.55 * Y / H) + 0.01
    fields["B"] = np.maximum(erfc(Y / (2 * Ll)), cgb * np.exp(-dist / width))
    # C: boundary-only
    fields["C"] = np.where(dist < 0.025, np.exp(-(Y / 1.3) ** 1.2), 0.0)
    crit = {"A": r"$\sqrt{D_l t}>d$", "B": r"$\delta<\sqrt{D_l t}<d$", "C": r"$\sqrt{D_l t}<\delta$"}
    desc = {"A": "high T, long t, fine grains", "B": "intermediate T (most common)", "C": "low T"}
    for k, key in enumerate("ABC"):
        ax = fig.add_axes([0.04 + 0.325 * k, 0.53, 0.29, 0.40])
        ax.imshow(np.clip(fields[key], 0, 1), extent=(0, W, H, 0), cmap="Blues", vmin=0, vmax=1.05,
                  aspect="auto", interpolation="bilinear")
        for g in gbx:
            ax.plot([g, g], [0, H], color=INK, lw=0.9)
        ax.add_patch(Rectangle((0, -0.16), W, 0.16, fc=COLORS[1], ec="none", clip_on=False))
        ax.set_xlim(0, W); ax.set_ylim(H, -0.16)
        ax.text(W / 2, -0.08, "tracer source", color="white", fontsize=7, ha="center", va="center")
        ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(True); s.set_color("0.4")
        ax.set_title(f"Type {key}", fontsize=10, pad=3)
        if k == 0:
            ax.set_ylabel("depth ↓", fontsize=8.5)
            ax.annotate("", xy=(0.5, 2.2), xytext=(1.5, 2.2),
                        arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=0.8, mutation_scale=7))
            ax.text(1.0, 2.15, "d", ha="center", va="bottom", fontsize=9,
                    bbox=dict(fc="white", ec="none", pad=0.5))
        if k == 2:
            ax.annotate("grain boundary\n(width δ)", xy=(1.5, 1.6), xytext=(1.7, 2.0), fontsize=6.5,
                        arrowprops=dict(arrowstyle="-", color=INK, lw=0.6),
                        bbox=dict(fc="white", ec="none", pad=0.5))
        fig.text(0.04 + 0.325 * k + 0.145, 0.475, crit[key] + "\n" + desc[key], ha="center", va="top",
                 fontsize=8.5)
    # penetration profiles
    u = np.linspace(0, 1, 300)          # depth^(6/5), arbitrary units
    profs = {
        "A": np.log10(erfc(u / 0.35) + 1e-9),
        "B": np.log10(erfc(u / 0.08) + 10**(-1.6 - 2.6 * u)),
        "C": -1.9 - 2.2 * u,
    }
    for k, key in enumerate("ABC"):
        ax = fig.add_axes([0.06 + 0.325 * k, 0.07, 0.26, 0.27])
        ax.plot(u, profs[key], color=COLORS[0], lw=1.8)
        ax.set_ylim(-5, 0.2); ax.set_xlim(0, 1)
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_xlabel(r"depth$^{6/5}$", fontsize=8)
        if k == 0:
            ax.set_ylabel(r"$\log\,\bar C$", fontsize=9)
        if key == "B":
            ax.annotate(r"slope $\rightarrow s\delta D_{gb}$", xy=(0.6, -1.6 - 2.6 * 0.6), xytext=(0.42, -1.2),
                        fontsize=7.5, arrowprops=dict(arrowstyle="-", color=INK, lw=0.6))
            ax.text(0.09, -0.6, "lattice", fontsize=7, ha="left")
        if key == "A":
            ax.text(0.05, -3.6, "single erfc-like\nprofile, $D_{eff}$", fontsize=7.5)
        if key == "C":
            ax.text(0.35, -1.2, "boundary-only\ntail, $D_{gb}$", fontsize=7.5)
    save(fig, "08", "fig-8-5-harrison-regimes")


# ---------------------------------------------------------------- Figure 8.6
def carburizing_profiles():
    fig, ax = new_fig(6.4, 3.9)
    Cs, C0 = 1.0, 0.20
    D950 = 2.3e-5 * np.exp(-148000 / (R * 1223.15))
    D925 = 2.3e-5 * np.exp(-148000 / (R * 1198.15))
    x = np.linspace(0, 2.5e-3, 400)
    z = erfinv(0.75)
    for (th, c) in [(2.4, COLORS[0]), (9.5, COLORS[1]), (20, COLORS[2])]:
        t = th * 3600
        C = C0 + (Cs - C0) * erfc(x / (2 * np.sqrt(D950 * t)))
        ax.plot(x * 1e3, C, color=c, label=f"{th:g} h at 950 °C")
        xc = 2 * z * np.sqrt(D950 * t) * 1e3
        print(f"950 °C, {th} h: depth to 0.40 % C = {xc:.2f} mm")
    t = 9.5 * 3600
    C = C0 + (Cs - C0) * erfc(x / (2 * np.sqrt(D925 * t)))
    ax.plot(x * 1e3, C, ":", color=COLORS[1], lw=2, label="9.5 h at 925 °C (furnace 25 °C cold)")
    x925 = 2 * z * np.sqrt(D925 * t) * 1e3
    x950 = 2 * z * np.sqrt(D950 * t) * 1e3
    print(f"D950={D950:.3e}, D925={D925:.3e}, x950={x950:.3f} mm, x925={x925:.3f} mm")
    ax.axhline(0.40, color="0.4", ls="--", lw=1)
    ax.text(2.48, 0.415, "case-depth criterion 0.40 wt% C", fontsize=8, ha="right", va="bottom", color="0.3")
    ax.plot([x950], [0.40], "o", color=COLORS[1], ms=5, zorder=5)
    ax.plot([x925], [0.40], "o", mfc="white", mec=COLORS[1], ms=5, mew=1.3, zorder=5)
    ax.vlines([x925, x950], 0.1, 0.40, colors=COLORS[1], lw=0.8, linestyles=[":", "-"])
    ax.text(x950 + 0.03, 0.13, f"{x950:.2f} mm", fontsize=8, color=COLORS[1])
    ax.text(x925 - 0.03, 0.13, f"{x925:.2f} mm", fontsize=8, color=COLORS[1], ha="right")
    ax.axhline(C0, color="0.7", lw=0.8)
    ax.text(2.48, 0.185, "core 0.20 wt% C", fontsize=7.5, ha="right", va="top", color="0.4")
    ax.set_xlim(0, 2.5); ax.set_ylim(0.1, 1.1)
    ax.set_xlabel("Depth below surface (mm)")
    ax.set_ylabel("Carbon (wt%)")
    ax.legend(fontsize=8, loc="upper right")
    ax.text(1.5, 0.74, r"$C_s$ = 1.0, $C_0$ = 0.20 wt% C" "\n" r"$D_{950}$ = 1.10×10$^{-11}$ m²/s" "\n"
            r"$D_{925}$ = 8.1×10$^{-12}$ m²/s",
            fontsize=7.5, va="top")
    save(fig, "08", "fig-8-6-carburizing-profiles")


if __name__ == "__main__":
    fick_solutions()
    diffusion_mechanisms()
    arrhenius_plot()
    kirkendall_effect()
    harrison_regimes()
    carburizing_profiles()
