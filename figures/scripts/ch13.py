"""Figures for Chapter 13 — Plasticity and Strengthening Mechanisms.

Run from the repository root:  python figures/scripts/ch13.py
"""
import numpy as np
from matplotlib.patches import Ellipse, Polygon, Circle, FancyArrowPatch, Rectangle
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

from figstyle import new_fig, save, COLORS, INK, GRID
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# 13.1 Schmid geometry
# ---------------------------------------------------------------------------
def schmid_geometry():
    fig = plt.figure(figsize=(6.8, 3.9))
    axL = fig.add_axes([0.0, 0.02, 0.42, 0.96])
    axR = fig.add_axes([0.53, 0.14, 0.45, 0.78])

    ax = axL
    ax.set_xlim(-2.6, 2.9)
    ax.set_ylim(-3.6, 3.6)
    ax.set_aspect("equal")
    ax.axis("off")
    R, H = 1.0, 2.4
    ery = 0.28  # ellipse half-height of end faces (perspective)
    # cylinder body
    ax.plot([-R, -R], [-H, H], color=INK, lw=1.3)
    ax.plot([R, R], [-H, H], color=INK, lw=1.3)
    ax.add_patch(Ellipse((0, H), 2 * R, 2 * ery, fc="#E8EEF5", ec=INK, lw=1.3))
    th = np.linspace(np.pi, 2 * np.pi, 60)
    ax.plot(R * np.cos(th), -H + ery * np.sin(th), color=INK, lw=1.3)
    th2 = np.linspace(0, np.pi, 60)
    ax.plot(R * np.cos(th2), -H + ery * np.sin(th2), color=INK, lw=0.8, ls=(0, (3, 2)))
    # A0 label at top face
    ax.text(0, H, "$A_0$", ha="center", va="center", fontsize=10, color=INK)
    # inclined slip plane: ellipse through the cylinder, tilted
    phi = np.deg2rad(50)  # angle between plane normal and axis
    tilt = np.tan(phi)  # height change across the diameter
    t = np.linspace(0, 2 * np.pi, 200)
    xs = R * np.cos(t)
    ys = 0.0 + 0.62 * np.cos(t) + ery * 1.25 * np.sin(t)
    ax.add_patch(Polygon(np.c_[xs, ys], closed=True, fc=COLORS[0], alpha=0.25, ec=COLORS[0], lw=1.3))
    ax.text(-1.05, 0.95, "slip plane\narea $A_0/\\cos\\phi$", ha="right", va="center", fontsize=8.5,
            color=COLORS[0])
    ax.plot([-1.02, -0.55], [0.75, -0.2], color=COLORS[0], lw=0.8)
    # force arrows
    ax.annotate("", xy=(0, H + 1.05), xytext=(0, H + 0.3),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.6, mutation_scale=14))
    ax.annotate("", xy=(0, -H - 1.05), xytext=(0, -H - 0.35),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.6, mutation_scale=14))
    ax.text(0.15, H + 0.85, "$F$", fontsize=11, color=INK, va="center")
    ax.text(0.15, -H - 0.85, "$F$", fontsize=11, color=INK, va="center")
    # tensile axis (dash-dot)
    ax.plot([0, 0], [-0.1, 2.1], color=INK, lw=0.8, ls="-.")
    # normal vector n: from centre, angle phi from vertical axis
    # plane drawn with rise 0.62 across x in [-1,1] => normal tilted to the left
    nphi = np.arctan(0.62)  # perpendicular to the drawn plane
    L = 1.9
    n_end = (-L * np.sin(nphi), L * np.cos(nphi))
    ax.annotate("", xy=n_end, xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.6, mutation_scale=12))
    ax.text(n_end[0] - 0.05, n_end[1] + 0.12, "$\\mathbf{n}$", color=COLORS[1], fontsize=11,
            ha="center", va="bottom")
    # slip direction d in the plane (down-slope direction to right)
    lam = np.pi / 2 - np.arctan(0.62)  # steepest line in the plane
    d_end = (1.55 * np.sin(lam), 1.55 * np.cos(lam))
    ax.annotate("", xy=d_end, xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[2], lw=1.6, mutation_scale=12))
    ax.text(d_end[0] + 0.08, d_end[1] + 0.05, "$\\mathbf{d}$", color=COLORS[2], fontsize=11,
            ha="left", va="bottom")
    # angle arcs
    a1 = np.linspace(np.pi / 2, np.pi / 2 + nphi, 30)
    ax.plot(0.75 * np.cos(a1), 0.75 * np.sin(a1), color=COLORS[1], lw=1.0)
    ax.text(-0.27, 0.93, "$\\phi$", color=COLORS[1], fontsize=11, ha="center")
    a2 = np.linspace(np.pi / 2 - lam, np.pi / 2, 30)
    ax.plot(0.95 * np.cos(a2), 0.95 * np.sin(a2), color=COLORS[2], lw=1.0)
    ax.text(0.60, 1.08, "$\\lambda$", color=COLORS[2], fontsize=11, ha="center")
    ax.text(1.25, -1.45, "$\\tau_R=\\dfrac{F\\cos\\lambda}{A_0/\\cos\\phi}$\n$\\;\\;=\\sigma\\cos\\phi\\cos\\lambda$",
            fontsize=9.5, color=INK, ha="left", va="center")
    ax.text(-2.55, 3.45, "(a)", fontsize=10, fontweight="bold", color=INK, va="top")

    # ---- right: yield stress vs Schmid factor for Mg basal slip
    ax = axR
    tau_c = 0.5
    m = np.linspace(0.009, 0.5, 400)
    ax.axhspan(40, 50, color=COLORS[3], alpha=0.18, lw=0)
    ax.axhline(40, color=COLORS[3], lw=0.9, ls="--")
    ax.axhline(50, color=COLORS[3], lw=0.9, ls="--")
    ax.text(0.49, 58, "prismatic/pyramidal slip\nor twinning takes over", ha="right", va="bottom",
            fontsize=8.5, color=COLORS[3])
    ax.plot(m, tau_c / m, color=COLORS[0], lw=1.8, label="$\\sigma_y=\\tau_c/m$, $\\tau_c=0.5$ MPa")
    rng = np.random.default_rng(13)
    md = np.array([0.03, 0.05, 0.07, 0.1, 0.13, 0.17, 0.22, 0.27, 0.32, 0.37, 0.42, 0.46, 0.49])
    sd = tau_c / md * np.exp(rng.normal(0, 0.09, md.size))
    ax.plot(md, sd, "o", ms=4.5, mfc="white", mec=COLORS[0], mew=1.2, label="single-crystal tests (schematic)")
    ax.plot([0.5], [1.0], "s", color=COLORS[1], ms=6, zorder=5)
    ax.annotate("$m=0.5$: $\\sigma_y=1.0$ MPa", xy=(0.5, 1.0), xytext=(0.30, 0.62),
                fontsize=8.5, color=COLORS[1], arrowprops=dict(arrowstyle="-", color=COLORS[1], lw=0.8))
    ax.plot([0.087], [5.75], "s", color=COLORS[1], ms=6, zorder=5)
    ax.annotate("$m=0.087$ ($c$-axis 5° off):\n$\\sigma_y\\approx5.8$ MPa", xy=(0.087, 5.75),
                xytext=(0.15, 9.5), fontsize=8.5, color=COLORS[1],
                arrowprops=dict(arrowstyle="-", color=COLORS[1], lw=0.8))
    ax.set_yscale("log")
    ax.set_xlim(0, 0.5)
    ax.set_ylim(0.5, 100)
    ax.set_yticks([0.5, 1, 2, 5, 10, 20, 50, 100])
    ax.set_yticklabels(["0.5", "1", "2", "5", "10", "20", "50", "100"])
    ax.set_xlabel("Schmid factor $m=\\cos\\phi\\cos\\lambda$")
    ax.set_ylabel("Tensile yield stress (MPa)")
    ax.set_title("Mg single crystals, basal slip", fontsize=10)
    ax.legend(loc="upper right", fontsize=8, bbox_to_anchor=(1.0, 0.80))
    ax.text(-0.17, 1.08, "(b)", transform=ax.transAxes, fontsize=10, fontweight="bold", color=INK)
    save(fig, "13", "fig-13-1-schmid-geometry")


# ---------------------------------------------------------------------------
# 13.2 Single-crystal stages
# ---------------------------------------------------------------------------
def _integrate(tau0, thI, gI, thII, tauIII, tausat, gmax=0.8, n=8000):
    g = np.linspace(0, gmax, n)
    tau = np.empty_like(g)
    tau[0] = tau0
    for i in range(1, n):
        gg = g[i - 1]
        w = 1 / (1 + np.exp(-(gg - gI) / 0.008)) if gI > 0 else 1.0
        th = thI + (thII - thI) * w
        t = tau[i - 1]
        if t > tauIII:
            th *= max(0.0, 1 - (t - tauIII) / (tausat - tauIII))
        tau[i] = t + th * (g[i] - gg)
    return g, tau


def single_crystal_stages():
    G = 48e3
    fig, ax = new_fig(6.4, 4.2)
    # Cu [123]: tune saturation so tau(0.8) ~ 85 MPa
    g1, t1 = _integrate(0.6, G / 3000, 0.10, G / 200, 50.0, 88.6)
    g2, t2 = _integrate(0.6, G / 200, 0.0, G / 200, 50.0, 92.0)
    g3, t3 = _integrate(0.6, 26e3 / 3000, 0.04, 26e3 / 200, 12.0, 25.5)
    ax.plot(g2, t2, color=COLORS[1], label="Cu [001] / [111] (multiple slip)")
    ax.plot(g1, t1, color=COLORS[0], lw=2.2, label="Cu [123] (single slip)")
    ax.plot(g3, t3, color=COLORS[2], label="Al [123] (high SFE)")
    ax.set_xlim(0, 0.8)
    ax.set_ylim(0, 100)
    ax.set_xlabel("Resolved shear strain $\\gamma$")
    ax.set_ylabel("Resolved shear stress $\\tau$ (MPa)")
    ax.legend(loc="upper left", fontsize=8.5)
    # stage boundaries on Cu [123]
    gII = g1[np.argmin(np.abs(t1 - 50))]
    ax.axvline(0.10, color=GRID, lw=0.9, ls="--", zorder=0)
    ax.axvline(gII, color=GRID, lw=0.9, ls="--", zorder=0)
    ax.text(0.05, 60, "I", ha="center", fontsize=12, color=COLORS[0], fontweight="bold")
    ax.text((0.10 + gII) / 2, 60, "II", ha="center", fontsize=12, color=COLORS[0], fontweight="bold")
    ax.text(0.42, 58, "III", ha="center", fontsize=12, color=COLORS[0], fontweight="bold")
    # theta_II annotation
    ga, gb = 0.17, 0.25
    ta, tb = np.interp(ga, g1, t1), np.interp(gb, g1, t1)
    ax.plot([ga, gb, gb], [ta, ta, tb], color=INK, lw=0.9)
    ax.text(gb + 0.01, (ta + tb) / 2, "$\\theta_{II}\\approx G/200$\n$\\approx240$ MPa", fontsize=8.5,
            va="center", color=INK)
    ax.plot(gII, 50, "o", ms=4, color=INK, zorder=5)
    ax.text(gII + 0.012, 47, "stage III begins\n$\\tau_{III}\\approx50$ MPa", fontsize=8.5,
            color=INK, va="top", ha="left")
    ax.annotate("Al: dynamic recovery from\n$\\tau\\approx12$ MPa, saturates ~25 MPa",
                xy=(0.55, np.interp(0.55, g3, t3)), xytext=(0.47, 8), fontsize=8.5, color=COLORS[2],
                arrowprops=dict(arrowstyle="-", lw=0.8, color=COLORS[2]))
    # inset: stage I detail
    axi = fig.add_axes([0.66, 0.40, 0.27, 0.22])
    axi.plot(g1, t1, color=COLORS[0], lw=1.8)
    axi.plot(g2, t2, color=COLORS[1], lw=1.4)
    axi.set_xlim(0, 0.14)
    axi.set_ylim(0, 8)
    axi.tick_params(labelsize=7.5)
    axi.set_xticks([0, 0.05, 0.1])
    axi.set_title("stage I (easy glide)", fontsize=8)
    axi.annotate("$\\theta_I\\approx G/3000$\n$\\approx16$ MPa", xy=(0.06, np.interp(0.06, g1, t1)),
                 xytext=(0.012, 4.6), fontsize=7.5, color=COLORS[0],
                 arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[0]))
    axi.text(0.135, 0.3, "$\\tau_0\\approx0.6$ MPa", fontsize=7.5, ha="right", color=INK)
    save(fig, "13", "fig-13-2-single-crystal-stages")


# ---------------------------------------------------------------------------
# 13.3 Yield surfaces
# ---------------------------------------------------------------------------
def yield_surfaces():
    fig, ax = new_fig(5.6, 5.4)
    t = np.linspace(0, 2 * np.pi, 400)
    # von Mises ellipse: principal axes along (1,1) and (1,-1)
    a = np.sqrt(2)  # semi-axis along (1,1)/sqrt2 : s^2 * (1 - 1 + 1)... computed below
    # parametrize: s1 = u+v, s2 = u-v ; s1^2 - s1 s2 + s2^2 = u^2 + 3 v^2 = 1
    u = np.cos(t)
    v = np.sin(t) / np.sqrt(3)
    s1, s2 = (u + v), (u - v)
    ax.plot(s1, s2, color=COLORS[0], lw=2.0, label="von Mises")
    hx = [1, 1, 0, -1, -1, 0, 1]
    hy = [0, 1, 1, 0, -1, -1, 0]
    ax.plot(hx, hy, color=COLORS[1], lw=1.8, ls="--", label="Tresca")
    ax.axhline(0, color=INK, lw=0.7)
    ax.axvline(0, color=INK, lw=0.7)
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    ax.set_aspect("equal")
    ax.set_xlabel("$\\sigma_1/\\sigma_y$")
    ax.set_ylabel("$\\sigma_2/\\sigma_y$")
    ax.spines["top"].set_visible(True)
    ax.spines["right"].set_visible(True)

    def ray(x, y, c=INK):
        ax.plot([0, x], [0, y], color=c, lw=0.8, ls=":")

    # uniaxial
    ray(1.0, 0)
    ax.plot(1, 0, "o", color=INK, ms=5, zorder=5)
    ax.text(1.04, -0.07, "uniaxial\ntension", fontsize=8.5, va="top", ha="left")
    # equibiaxial
    ray(1, 1)
    ax.plot(1, 1, "o", color=INK, ms=5, zorder=5)
    ax.text(1.38, 1.38, "equibiaxial\ntension\n(balloon, sheet\nstretching)", fontsize=7.5, ha="right",
            va="top")
    # pure shear
    ray(0.577, -0.577)
    ax.plot(0.577, -0.577, "o", color=COLORS[0], ms=5, zorder=5)
    ax.plot(0.5, -0.5, "o", color=COLORS[1], ms=5, zorder=5)
    ax.annotate("pure shear $\\sigma_1=-\\sigma_2$ (torsion):\nVM 0.577, Tresca 0.5\n"
                "→ 15 % difference", xy=(0.577, -0.577), xytext=(0.22, -1.08), fontsize=8.5,
                va="top", ha="left", arrowprops=dict(arrowstyle="-", lw=0.7, color=INK))
    # pressure vessel
    ray(1.155, 0.577)
    ax.plot(1.155, 0.577, "o", color=COLORS[0], ms=5, zorder=5)
    ax.plot(1.0, 0.5, "o", color=COLORS[1], ms=5, zorder=5)
    ax.annotate("thin-walled pressure\nvessel $\\sigma_\\theta=2\\sigma_z$\n(1.155, 0.577)", xy=(1.155, 0.577),
                xytext=(0.06, 0.93), fontsize=8, va="top", ha="left",
                arrowprops=dict(arrowstyle="-", lw=0.7, color=INK))
    ax.legend(loc="lower right", bbox_to_anchor=(1.0, 0.2), fontsize=9)
    # inset: 3-D view of the cylinder about the hydrostatic axis
    axi = fig.add_axes([0.13, 0.72, 0.17, 0.17])
    axi.set_xlim(-1.2, 1.2)
    axi.set_ylim(-1.2, 1.3)
    axi.set_aspect("equal")
    axi.axis("off")
    # isometric-like axes
    for ang, lab in [(-150, "$\\sigma_1$"), (-30, "$\\sigma_2$"), (90, "$\\sigma_3$")]:
        r = np.deg2rad(ang)
        axi.annotate("", xy=(0.95 * np.cos(r), 0.95 * np.sin(r)), xytext=(0, 0),
                     arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.8, mutation_scale=7))
        axi.text(1.12 * np.cos(r), 1.12 * np.sin(r), lab, fontsize=8, ha="center", va="center")
    axi.add_patch(Circle((0, 0), 0.55, fc=COLORS[0], alpha=0.15, ec=COLORS[0], lw=1.0))
    axi.plot(0, 0, "o", ms=6, mfc="white", mec=INK)
    axi.plot(0, 0, "o", ms=1.8, color=INK)
    ax.text(-1.36, 0.70, "hydrostatic axis\n$\\sigma_1=\\sigma_2=\\sigma_3$\n(⊙ out of page)", fontsize=7.5,
            ha="left", va="top")
    save(fig, "13", "fig-13-3-yield-surfaces")


# ---------------------------------------------------------------------------
# 13.4 Hall–Petch
# ---------------------------------------------------------------------------
def hall_petch():
    fig, ax = new_fig(6.4, 4.3)
    mats = [("Low-carbon steel", 70, 0.74, COLORS[0]),
            ("CP α-Ti", 80, 0.40, COLORS[1]),
            ("AZ31 Mg", 80, 0.25, COLORS[2]),
            ("Cu", 25, 0.11, COLORS[3]),
            ("Al", 15, 0.05, COLORS[4])]
    x = np.linspace(0, 25, 200)  # d^-1/2 in mm^-1/2
    for name, s0, ky, c in mats:
        ky_mm = ky * np.sqrt(1000)  # MPa mm^1/2
        y = s0 + ky_mm * x
        ax.plot(x, y, color=c, lw=1.9)
        yl = s0 + ky_mm * 25
        lab = f"{name} ({ky:g})"
        if yl > 690:
            xl = (690 - s0) / ky_mm
            ax.text(xl - 0.4, 690, f"{name}  ($k_y$ = {ky:g} MPa m$^{{1/2}}$)", color=c, fontsize=8.5,
                    ha="right", va="top")
        else:
            ax.text(25.3, yl, lab, color=c, fontsize=8.5, va="center", ha="left")
    ax.text(17.5, 140, "labels: $k_y$ in MPa m$^{1/2}$", fontsize=8.5, color=INK, ha="center")
    # worked example points
    for d_um, s in [(30, 205), (5, 401)]:
        xx = 1 / np.sqrt(d_um / 1000)
        ax.plot(xx, s, "o", color=COLORS[0], ms=6, mfc="white", mew=1.6, zorder=5)
        ax.annotate(f"$d$ = {d_um} μm: {s} MPa", xy=(xx, s), xytext=((0.6, 262) if d_um == 30 else (xx + 1.2, s - 72)),
                    fontsize=8.5, color=COLORS[0],
                    arrowprops=dict(arrowstyle="-", color=COLORS[0], lw=0.8))
    ax.set_xlim(0, 25)
    ax.set_ylim(0, 700)
    ax.set_xlabel("$d^{-1/2}$ (mm$^{-1/2}$)")
    ax.set_ylabel("Yield strength $\\sigma_y$ (MPa)")
    sec = ax.secondary_xaxis("top", functions=(lambda v: v, lambda v: v))
    dvals = [1000, 100, 10, 5, 2]
    sec.set_xticks([1 / np.sqrt(d / 1000) for d in dvals])
    sec.set_xticklabels(["1 mm", "100 μm", "10 μm", "5 μm", "2 μm"], fontsize=8.5)
    sec.set_xlabel("grain size $d$", fontsize=9)
    ax.spines["top"].set_visible(True)
    # inset: nanocrystalline deviation (Cu)
    axi = fig.add_axes([0.20, 0.50, 0.27, 0.25])
    xx = np.linspace(0, 330, 400)  # mm^-1/2
    ky_mm = 0.11 * np.sqrt(1000)
    hp = 25 + ky_mm * xx
    d_nm = (1 / xx[1:]) ** 2 * 1e6
    # measured-like: follows HP down to ~100 nm (x=100), bends over, peaks ~15 nm (x=258), then falls
    real = np.r_[25, 25 + ky_mm * xx[1:] / (1 + (xx[1:] / 165) ** 4) ** 0.25]
    real = np.where(xx > 258, np.interp(258, xx, real) - 2.2 * (xx - 258), real)
    axi.plot(xx, hp, color=COLORS[3], lw=1.1, ls="--")
    axi.plot(xx, real, color=COLORS[3], lw=1.8)
    axi.axvline(100, color=GRID, lw=0.8)
    axi.axvline(258, color=GRID, lw=0.8)
    axi.text(105, 1180, "100 nm", fontsize=6.8, ha="left", va="top")
    axi.text(253, 1180, "15 nm", fontsize=6.8, ha="right", va="top")
    axi.set_yticks([0, 500, 1000])
    axi.set_xlim(0, 330)
    axi.set_ylim(0, 1200)
    axi.tick_params(labelsize=7)
    axi.set_xlabel("$d^{-1/2}$ (mm$^{-1/2}$)", fontsize=7.5, labelpad=1)
    axi.set_ylabel("$\\sigma_y$ (MPa)", fontsize=7.5, labelpad=1)
    axi.set_title("Cu, nanocrystalline range", fontsize=7.5, pad=10)
    axi.text(232, 25, "deviation below ~100 nm;\ninverse Hall–Petch\nbelow ~15 nm (Ch 30)",
             fontsize=6.8, ha="center", va="bottom", color=INK)
    axi.add_patch(Rectangle((0, 0), 25, 1200, fc=COLORS[0], alpha=0.12, lw=0))
    save(fig, "13", "fig-13-4-hall-petch")


# ---------------------------------------------------------------------------
# 13.5 Cutting vs Orowan
# ---------------------------------------------------------------------------
def _orowan(r_nm, f=0.03, G=26e9, b=0.286e-9, nu=0.33, M=3.06):
    r = r_nm * 1e-9
    L = r * np.sqrt(2 * np.pi / (3 * f))
    rb = np.sqrt(2 / 3) * r
    lam = L - 2 * rb
    dtau = 0.4 * G * b / (np.pi * np.sqrt(1 - nu) * lam) * np.log(2 * rb / b)
    return M * dtau / 1e6


def cutting_orowan():
    fig, ax = new_fig(6.4, 4.3)
    r = np.linspace(0.5, 40, 800)
    oro = _orowan(r)
    rc = 7.0
    C = _orowan(rc) / np.sqrt(0.03 * rc)
    cut = C * np.sqrt(0.03 * r)
    env = np.minimum(oro, cut)
    ax.plot(r, cut, color=COLORS[2], lw=1.3, ls="--", label="cutting, $\\Delta\\sigma\\propto\\sqrt{fr}$")
    ax.plot(r[r > 1.6], oro[r > 1.6], color=COLORS[1], lw=1.3, ls="--",
            label="Orowan bypass (Ashby–Orowan)")
    ax.plot(r, env, color=INK, lw=2.6, label="flow-stress increment (lower of the two)")
    for rr in [5, 10, 20]:
        ax.plot(rr, _orowan(rr), "o", color=COLORS[1], ms=5, zorder=5)
        ax.text(rr + 0.6, _orowan(rr) + 6, f"{_orowan(rr):.0f}", color=COLORS[1], fontsize=8.5)
    ax.plot(rc, _orowan(rc), "o", color=INK, ms=6, zorder=6)
    ax.annotate(f"peak aged\n$r_c\\approx7$ nm, {_orowan(rc):.0f} MPa", xy=(rc, _orowan(rc)),
                xytext=(9.0, 262), fontsize=8, arrowprops=dict(arrowstyle="-", lw=0.8))
    ax.text(3.0, 262, "underaged\n(cutting)", fontsize=8.5, ha="center", color=COLORS[2])
    ax.text(30, 55, "overaged (Orowan)", fontsize=8.5, ha="center", color=COLORS[1])
    ax.set_xlim(0, 40)
    ax.set_ylim(0, 500)
    ax.set_xlabel("Precipitate radius $r$ (nm)")
    ax.set_ylabel("$\\Delta\\sigma=M\\Delta\\tau$ (MPa)")
    ax.legend(loc="upper right", fontsize=8, bbox_to_anchor=(1.0, 1.0))
    ax.text(0.99, 0.72, "Al alloy: $G$ = 26 GPa, $b$ = 0.286 nm,\n$M$ = 3.06, $f$ = 0.03",
            transform=ax.transAxes, ha="right", fontsize=8, color=INK)
    # top axis: ageing time at 175 C, LSW r^3 ~ t, r = 7 nm at 8 h (schematic)
    sec = ax.secondary_xaxis("top", functions=(lambda v: v, lambda v: v))
    tt = [1, 10, 100]
    sec.set_xticks([7 * (t / 8) ** (1 / 3) for t in tt])
    sec.set_xticklabels(["1 h", "10 h", "100 h"], fontsize=8.5)
    sec.set_xlabel("approximate ageing time at 175 °C ($r^3\\propto t$)", fontsize=9)
    ax.spines["top"].set_visible(True)

    # insets
    def inset_cut(a):
        a.set_xlim(0, 10)
        a.set_ylim(0, 6)
        a.set_aspect("equal")
        a.axis("off")
        a.add_patch(Rectangle((0, 0), 10, 6, fc="white", ec=INK, lw=0.8))
        for cx in [2.0, 5.0, 8.0]:
            # sheared particle: two halves offset
            a.add_patch(Polygon([[cx - 0.8, 3.0], [cx + 0.8, 3.0], [cx + 0.8, 3.9], [cx - 0.8, 3.9]],
                                fc=COLORS[2], alpha=0.5, ec=COLORS[2]))
            a.add_patch(Polygon([[cx - 0.5, 2.1], [cx + 1.1, 2.1], [cx + 1.1, 3.0], [cx - 0.5, 3.0]],
                                fc=COLORS[2], alpha=0.5, ec=COLORS[2]))
        a.plot([0, 10], [3.0, 3.0], color=GRID, lw=0.6, ls=":")
        a.plot([0.3, 9.7], [1.0, 1.0], color=INK, lw=1.6)
        a.text(5, 6.3, "(a) cutting: sheared particles,\nledges of height $b$", fontsize=7, ha="center",
               va="bottom")

    def inset_orowan(a):
        a.set_xlim(0, 10)
        a.set_ylim(0, 6)
        a.set_aspect("equal")
        a.axis("off")
        a.add_patch(Rectangle((0, 0), 10, 6, fc="white", ec=INK, lw=0.8))
        xs = [2.0, 5.0, 8.0]
        for cx in xs:
            a.add_patch(Circle((cx, 3.0), 0.6, fc=COLORS[1], alpha=0.5, ec=COLORS[1]))
            a.add_patch(Circle((cx, 3.0), 0.85, fc="none", ec=INK, lw=1.0))  # Orowan loop
        # bowed dislocation line below particles
        x = np.linspace(0.3, 9.7, 300)
        y = 2.05 - 0.0 * x
        for cx in xs:
            y = np.where(np.abs(x - cx) < 0.6, 2.05, y)
        # bulge between particles
        bul = np.zeros_like(x)
        for a0, a1 in [(0.3, 1.4), (2.6, 4.4), (5.6, 7.4), (8.6, 9.7)]:
            mask = (x > a0) & (x < a1)
            bul[mask] = -1.1 * np.sin(np.pi * (x[mask] - a0) / (a1 - a0))
        a.plot(x, 2.05 + bul, color=INK, lw=1.6)
        a.text(5, 6.3, "(b) Orowan bypass: bowing,\nloops left round particles", fontsize=7,
               ha="center", va="bottom")

    a1 = fig.add_axes([0.50, 0.40, 0.19, 0.15])
    inset_cut(a1)
    a2 = fig.add_axes([0.73, 0.40, 0.19, 0.15])
    inset_orowan(a2)
    save(fig, "13", "fig-13-5-cutting-orowan")


# ---------------------------------------------------------------------------
# 13.6 Strength contributions
# ---------------------------------------------------------------------------
def strength_contributions():
    mech = ["Lattice friction", "Solid solution", "Grain size (Hall–Petch)", "Precipitates",
            "Dislocations"]
    cols = ["#9E9E9E", COLORS[4], COLORS[0], COLORS[1], COLORS[2]]
    alloys = [("Annealed Cu\n($d$ = 30 μm)", [15, 0, 20, 0, 10]),
              ("Cold-rolled Cu\n(hard temper)", [15, 0, 20, 0, 250]),
              ("X70 HSLA\npipeline steel", [50, 70, 302, 80, 40]),
              ("7075-T6\naluminium", [10, 30, 20, 420, 20])]
    fig, ax = new_fig(6.6, 3.9)
    ys = np.arange(len(alloys))[::-1]
    for (name, vals), y in zip(alloys, ys):
        left = 0
        for v, c, mname in zip(vals, cols, mech):
            if v > 0:
                ax.barh(y, v, left=left, color=c, height=0.55, ec="white", lw=0.8)
                if v >= 40:
                    ax.text(left + v / 2, y, f"{v}", ha="center", va="center", fontsize=8,
                            color="white" if c != COLORS[4] else INK)
            left += v
        xt = {542: 566, 500: 510}.get(left, left + 6)
        ax.text(xt, y, f"{left}", va="center", fontsize=8.5, color=INK, fontweight="bold")
    # X70 band & quadrature marker
    yx = ys[2]
    ax.add_patch(Rectangle((485, yx - 0.42), 75, 0.84, fc="none", ec=INK, lw=0.9, ls="--", hatch="////",
                           alpha=0.6))
    ax.plot([511, 511], [yx - 0.36, yx + 0.36], color=INK, lw=2.0)
    ax.text(511, yx + 0.40, "511 (quadrature)", ha="center", va="bottom", fontsize=7.5)
    ax.text(522, yx - 0.40, "measured 485–560", ha="center", va="top", fontsize=7.5)
    y7 = ys[3]
    ax.add_patch(Rectangle((460, y7 - 0.42), 45, 0.84, fc="none", ec=INK, lw=0.9, ls="--", hatch="////",
                           alpha=0.6))
    ax.text(482, y7 - 0.40, "measured 460–505", ha="center", va="top", fontsize=7.5)
    ax.set_yticks(ys)
    ax.set_yticklabels([a[0] for a in alloys], fontsize=9)
    ax.set_xlim(0, 600)
    ax.set_ylim(-0.75, 3.6)
    ax.set_xlabel("Yield strength (MPa) — linear sum of contributions")
    handles = [Rectangle((0, 0), 1, 1, color=c) for c in cols]
    ax.legend(handles, mech, loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=3, fontsize=8.5)
    save(fig, "13", "fig-13-6-strength-contributions")


if __name__ == "__main__":
    schmid_geometry()
    single_crystal_stages()
    yield_surfaces()
    hall_petch()
    cutting_orowan()
    strength_contributions()
