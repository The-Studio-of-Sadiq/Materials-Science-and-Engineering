"""Figures for Chapter 30 — Superconducting Materials.

Run from the repository root:  python figures/scripts/ch30.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, RegularPolygon, Polygon, FancyBboxPatch, Ellipse
from matplotlib.collections import PatchCollection
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

PHI0 = 2.068e-15


# ---------------------------------------------------------------- Figure 30.1
def _field_lines_uniform(ax, R, expel, ys):
    """Field lines (vertical, upward) around a sphere of radius R at origin.
    expel=True: potential-flow lines of a perfect diamagnet (B=0 inside)."""
    for y0 in ys:  # y0 here is the horizontal offset of the line far away
        if not expel:
            ax.plot([y0, y0], [-2.0, 2.0], color=COLORS[0], lw=1.0)
            ax.annotate("", xy=(y0, 1.25), xytext=(y0, 1.0),
                        arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.0, mutation_scale=8))
        else:
            # stream function of uniform field past a perfect diamagnetic sphere (axisymmetric,
            # drawn in the meridian plane): psi = 0.5 * B0 * s^2 (1 - R^3/r^3)
            psi0 = 0.5 * y0**2
            zz = np.linspace(-2.0, 2.0, 400)
            ss = []
            for z in zz:
                # solve 0.5 s^2 (1 - R^3/(s^2+z^2)^1.5) = psi0 for s > 0
                lo, hi = 1e-6, 4.0
                for _ in range(60):
                    mid = 0.5 * (lo + hi)
                    r = np.hypot(mid, z)
                    val = 0.5 * mid**2 * (1 - (R / r)**3) if r > R else -1
                    if val < psi0:
                        lo = mid
                    else:
                        hi = mid
                ss.append(0.5 * (lo + hi))
            ss = np.array(ss) * np.sign(y0)
            ax.plot(ss, zz, color=COLORS[0], lw=1.0)
            k = np.argmin(abs(zz - 1.15))
            ax.annotate("", xy=(ss[k + 8], zz[k + 8]), xytext=(ss[k], zz[k]),
                        arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.0, mutation_scale=8))


def _trapped_dipole(ax, R):
    """Uniform field inside the sphere, dipole field outside (trapped flux, external field off)."""
    for x0 in (-0.52, -0.40, 0.0, 0.40, 0.52):
        ax.plot([x0, x0], [-np.sqrt(R**2 - x0**2), np.sqrt(R**2 - x0**2)], color=COLORS[0], lw=1.0)
    ax.plot([0, 0], [R, 1.75], color=COLORS[0], lw=1.0)
    ax.plot([0, 0], [-1.75, -R], color=COLORS[0], lw=1.0)
    ax.annotate("", xy=(0, 0.25), xytext=(0, 0.0),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.0, mutation_scale=8))
    # dipole field lines r = C sin^2(theta), theta measured from vertical axis
    th = np.linspace(0.02, np.pi - 0.02, 300)
    for C in (R**3 / 0.52**2, R**3 / 0.40**2):
        r = C * np.sin(th)**2
        m = r >= R * 0.999
        for sgn in (1, -1):
            x = sgn * r * np.sin(th)
            z = r * np.cos(th)
            x = np.where(m, x, np.nan)
            ax.plot(x, z, color=COLORS[0], lw=1.0)
        # arrow pointing downward on the outside (return flux)
        i = 150
        ax.annotate("", xy=(r[i + 6] * np.sin(th[i + 6]), r[i + 6] * np.cos(th[i + 6])),
                    xytext=(r[i] * np.sin(th[i]), r[i] * np.cos(th[i])),
                    arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.0, mutation_scale=8))


def perfect_conductor_vs_meissner():
    fig, axes = plt.subplots(2, 3, figsize=(6.6, 4.9))
    R = 0.62
    xs = [-1.4, -1.0, -0.6, -0.2, 0.2, 0.6, 1.0, 1.4]
    titles = [r"(a) $T>T_c$, $B_{\rm ext}$ on", r"(b) cooled to $T<T_c$, $B_{\rm ext}$ on",
              r"(c) $T<T_c$, $B_{\rm ext}$ off"]
    for row in range(2):
        for col in range(3):
            ax = axes[row, col]
            ax.set_xlim(-1.75, 1.75)
            ax.set_ylim(-1.75, 1.75)
            ax.set_aspect("equal")
            ax.axis("off")
            sc = (row == 1 and col > 0) or (row == 0 and col > 0)
            fc = "#D6E6F5" if col > 0 else "#EEEEEE"
            ax.add_patch(Circle((0, 0), R, fc=fc, ec=INK, lw=1.2, zorder=3 if (row == 1 and col > 0) else 0,
                                alpha=1.0))
            if col == 0:
                _field_lines_uniform(ax, R, False, xs)
            elif col == 1:
                _field_lines_uniform(ax, R, row == 1, xs)
                if row == 0:
                    ax.add_patch(Circle((0, 0), R, fc="none", ec=INK, lw=1.2, zorder=4))
            else:
                if row == 0:
                    _trapped_dipole(ax, R)
                    ax.add_patch(Circle((0, 0), R, fc="none", ec=INK, lw=1.2, zorder=4))
                else:
                    ax.text(0, -1.25, r"$B=0$ inside and outside", ha="center", fontsize=8.5)
            if row == 0:
                ax.set_title(titles[col], fontsize=9)
            if (row == 1 and col == 1):
                ax.text(0, 0, r"$B=0$", ha="center", va="center", fontsize=9, zorder=5)
    fig.text(0.01, 0.73, "perfect\nconductor\n" + r"($\rho\to0$)", fontsize=9.5, ha="left", va="center",
             fontweight="bold")
    fig.text(0.01, 0.28, "super-\nconductor\n(Meissner)", fontsize=9.5, ha="left", va="center",
             fontweight="bold")
    fig.text(0.56, 0.515, "field frozen in: final state depends on history", fontsize=8.5,
             ha="center", style="italic", color="0.3")
    fig.text(0.56, 0.035, "field expelled: final state independent of history", fontsize=8.5,
             ha="center", style="italic", color="0.3")
    fig.subplots_adjust(left=0.14, right=0.99, top=0.93, bottom=0.07, wspace=0.05, hspace=0.25)
    save(fig, "30", "fig-30-1-perfect-conductor-vs-meissner")


# ---------------------------------------------------------------- Figure 30.2
def lambda_xi_interface():
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 3.4))
    cases = [("Type I, $\\xi\\gg\\lambda$\n" + r"Al-like: $\lambda=16$ nm, $\xi=1600$ nm, $\kappa\approx0.01$",
              16.0, 1600.0, 5000.0),
             ("Type II, $\\lambda\\gg\\xi$\n" + r"Nb–Ti-like: $\lambda=270$ nm, $\xi=5$ nm, $\kappa\approx50$",
              270.0, 5.0, 1000.0)]
    for ax, (title, lam, xi, xmax) in zip(axes, cases):
        x = np.linspace(-0.12 * xmax, xmax, 4000)
        B = np.where(x < 0, 1.0, np.exp(-np.clip(x, 0, None) / lam))
        ns = np.where(x < 0, 0.0, np.tanh(np.clip(x, 0, None) / (np.sqrt(2) * xi))**2)
        ax.axvspan(-0.12 * xmax, 0, color="0.9")
        ax.plot(x, B, color=COLORS[0], lw=1.8, label=r"$B(x)/B_0$")
        ax.plot(x, ns, color=COLORS[1], lw=1.8, ls="--", label=r"$n_s(x)/n_s(\infty)$")
        ax.set_xlim(-0.12 * xmax, xmax)
        ax.set_ylim(0, 1.12)
        ax.set_xlabel("distance into superconductor $x$ (nm)")
        ax.set_title(title, fontsize=9)
        ax.text(-0.06 * xmax, 0.5, "normal", rotation=90, ha="center", va="center", fontsize=8.5)
        # markers
        y_l, y_x = 1 / np.e, np.tanh(1 / np.sqrt(2))**2
        ax.plot([lam], [y_l], "o", color=COLORS[0], ms=4)
        ax.plot([xi], [y_x], "o", color=COLORS[1], ms=4)
        ax.axvline(lam, color=COLORS[0], lw=0.7, ls=":")
        ax.axvline(xi, color=COLORS[1], lw=0.7, ls=":")
    axes[0].set_ylabel("normalized value")
    # labels for lengths (placed by hand to avoid clutter)
    axes[0].annotate(r"$\lambda$", xy=(16, 1 / np.e), xytext=(450, 0.12), fontsize=10, color=COLORS[0],
                     arrowprops=dict(arrowstyle="-", color=COLORS[0], lw=0.7))
    axes[0].text(1720, 0.25, r"$\xi$", fontsize=10, color=COLORS[1])
    axes[1].annotate(r"$\xi$", xy=(5, np.tanh(1 / np.sqrt(2))**2), xytext=(90, 0.55), fontsize=10,
                     color=COLORS[1], arrowprops=dict(arrowstyle="-", color=COLORS[1], lw=0.7))
    axes[1].text(285, 0.42, r"$\lambda$", fontsize=10, color=COLORS[0])
    axes[0].legend(loc="center right", fontsize=8.5, bbox_to_anchor=(1.0, 0.72))
    fig.tight_layout()
    save(fig, "30", "fig-30-2-lambda-xi-interface")


# ---------------------------------------------------------------- Figure 30.3
def jc_nbti(B, T):
    """Bottura-type scaling for Nb-Ti (non-Cu), A/mm^2; calibrated to 3000 A/mm^2 at 4.2 K, 5 T."""
    Tc0, Bc20 = 9.2, 14.5
    t = np.clip(T / Tc0, 0, 1)
    Bc2 = Bc20 * (1 - t**1.7)
    b = np.clip(B / np.maximum(Bc2, 1e-9), 0, 1)
    raw = np.where((b > 0) & (b < 1), (1 / np.maximum(B, 1e-9)) * b**0.63 * (1 - b)**1.0 * (1 - t**1.7)**2.3, 0)
    return raw


def jc_nb3sn(B, T):
    """Godeke-type scaling for Nb3Sn (non-Cu), A/mm^2; calibrated to 2800 A/mm^2 at 4.2 K, 12 T."""
    Tc0, Bc20 = 18.0, 30.0
    t = np.clip(T / Tc0, 0, 1)
    Bc2 = Bc20 * (1 - t**1.52)
    b = np.clip(B / np.maximum(Bc2, 1e-9), 0, 1)
    raw = np.where((b > 0) & (b < 1),
                   (1 / np.maximum(B, 1e-9)) * (1 - t**1.52) * (1 - t**2) * b**0.5 * (1 - b)**2, 0)
    return raw


C_NBTI = 3000.0 / jc_nbti(np.array(5.0), np.array(4.2))
C_NB3SN = 2800.0 / jc_nb3sn(np.array(12.0), np.array(4.2))


def critical_surface():
    fig = plt.figure(figsize=(6.8, 3.9))
    ax = fig.add_axes([-0.06, -0.02, 0.62, 1.0], projection="3d")
    JMAX = 1.0e4
    for f, C, Tc, Bc, ex, col, name in ((jc_nb3sn, C_NB3SN, 18.0, 30.0, 1.52, COLORS[1], r"Nb$_3$Sn"),
                                       (jc_nbti, C_NBTI, 9.2, 14.5, 1.7, COLORS[0], "Nb–Ti")):
        T = np.linspace(0, Tc * 0.999, 50)
        s = np.linspace(0.04, 0.999, 60)
        TT, SS = np.meshgrid(T, s)
        BB = SS * Bc * (1 - (TT / Tc)**ex)
        BB = np.maximum(BB, 0.6)
        J = np.minimum(C * f(BB, TT), JMAX)
        ax.plot_surface(TT, BB, J / 1e3, color=col, alpha=0.55, linewidth=0, antialiased=True,
                        rstride=1, cstride=1)
        tt = np.linspace(0, Tc, 100)
        ax.plot(tt, Bc * (1 - (tt / Tc)**ex), 0, color=col, lw=1.5)
        ax.plot([], [], color=col, lw=6, alpha=0.6, label=name)
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 30)
    ax.set_zlim(0, 10)
    ax.set_xticks([0, 5, 10, 15, 20])
    ax.set_yticks([0, 10, 20, 30])
    ax.set_xlabel("$T$ (K)", labelpad=-3)
    ax.set_ylabel("$B$ (T)", labelpad=-3)
    ax.set_zlabel(r"$J_c$ ($10^3$ A mm$^{-2}$)", labelpad=-4)
    ax.tick_params(pad=-2, labelsize=8)
    ax.view_init(elev=22, azim=-128)
    ax.legend(loc="upper left", bbox_to_anchor=(0.12, 0.88), fontsize=8.5)
    fig.text(0.03, 0.93, "(a) critical surfaces (non-Cu $J_c$, capped at $10^4$)", fontsize=9.5)

    # (b) 2D projection at 4.2 K, linear axes so the load line is straight
    a2 = fig.add_axes([0.66, 0.14, 0.33, 0.72])
    B = np.linspace(0.3, 32, 600)
    a2.plot(B, C_NBTI * jc_nbti(B, 4.2), color=COLORS[0], label="Nb–Ti")
    a2.plot(B, C_NB3SN * jc_nb3sn(B, 4.2), color=COLORS[1], label=r"Nb$_3$Sn")
    # HTS at 4.2 K (engineering current density, approximate empirical fits)
    a2.plot(B, 2400 * (B + 2.0)**-0.32, color=COLORS[2], label="Bi-2212 ($J_e$)")
    a2.plot(B, 5200 * (B + 1.0)**-0.45, color=COLORS[3], label=r"REBCO $B\parallel c$ ($J_e$)")
    j8 = C_NBTI * jc_nbti(np.array(8.0), 4.2)
    Bl = np.linspace(0, 10.5, 50)
    a2.plot(Bl, j8 / 8.0 * Bl, color=INK, ls="--", lw=1.2)
    a2.plot([8.0], [j8], "o", color=INK, ms=4)
    a2.text(1.6, 620, "load line", fontsize=8, rotation=50)
    a2.annotate("quench\n≈8 T", xy=(8.0, j8), xytext=(19.5, 2500), fontsize=8,
                arrowprops=dict(arrowstyle="-", lw=0.7, color=INK))
    a2.set_xlim(0, 32)
    a2.set_ylim(0, 5000)
    a2.set_xlabel("$B$ (T)")
    a2.set_ylabel(r"$J_c$ at 4.2 K (A mm$^{-2}$)")
    a2.set_title("(b) projection at 4.2 K", fontsize=9.5)
    a2.legend(fontsize=7.3, loc="upper right")
    save(fig, "30", "fig-30-3-critical-surface")


# ---------------------------------------------------------------- Figure 30.4
def type_i_type_ii():
    fig = plt.figure(figsize=(6.8, 4.6))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.1, 1], width_ratios=[1.15, 1], hspace=0.42, wspace=0.32)
    # (a) magnetization
    ax = fig.add_subplot(gs[0, 0])
    Bc, Bc1, Bc2 = 1.0, 0.35, 3.0
    H = np.linspace(0, 3.3, 1000)
    MI = np.where(H < Bc, H, 0)
    ax.plot(H[H < Bc], MI[H < Bc], color=COLORS[0], lw=1.8, label="Type I")
    ax.plot([Bc, Bc], [Bc, 0], color=COLORS[0], lw=1.8)
    Mrev = np.where(H < Bc1, H, Bc1 * np.log(Bc2 / np.maximum(H, Bc1)) / np.log(Bc2 / Bc1))
    Mrev = np.where(H > Bc2, 0, Mrev)
    ax.plot(H, Mrev, color=COLORS[1], lw=1.6, ls="--", label="Type II, reversible")
    # pinned: Bean-like loop of width 2w(H) about the reversible curve (Kim-type field dependence)
    w = 0.32 / (1 + H / 0.5) * (1 - np.clip(H / Bc2, 0, 1))
    Mup = np.minimum(H, Mrev + w)
    Mdn = Mrev - w
    ax.plot(H, Mup, color=COLORS[2], lw=1.6, label="Type II, pinned")
    ax.plot(H, Mdn, color=COLORS[2], lw=1.6)
    ax.annotate("", xy=(1.6, Mup[np.searchsorted(H, 1.6)]), xytext=(1.3, Mup[np.searchsorted(H, 1.3)]),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[2], mutation_scale=9))
    ax.annotate("", xy=(1.3, Mdn[np.searchsorted(H, 1.3)]), xytext=(1.6, Mdn[np.searchsorted(H, 1.6)]),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[2], mutation_scale=9))
    ax.axhline(0, color="0.5", lw=0.6)
    ax.set_xticks([Bc1, Bc, Bc2])
    ax.set_xticklabels([r"$B_{c1}$", r"$B_c$", r"$B_{c2}$"])
    ax.set_yticks([0])
    ax.set_xlim(0, 3.3)
    ax.set_ylim(-0.4, 1.12)
    ax.set_xlabel(r"applied field $\mu_0H$")
    ax.set_ylabel(r"$-\mu_0M$")
    ax.legend(fontsize=7.5, loc="upper right")
    ax.set_title("(a) magnetization", fontsize=9.5)

    # (b) phase diagram (cuprate-like, normalized)
    bx = fig.add_subplot(gs[0, 1])
    t = np.linspace(0, 1, 300)
    bc2 = 1 - t**2
    birr = 0.55 * (1 - t)**1.5
    bc1 = 0.06 * (1 - t**2)
    bx.fill_between(t, 0, bc1, color="#CFE3F3")
    bx.fill_between(t, bc1, birr, color="#D9EFD9")
    bx.fill_between(t, birr, bc2, color="#FBE3CF")
    bx.fill_between(t, bc2, 1.15, color="0.93")
    bx.plot(t, bc2, color=INK, lw=1.4)
    bx.plot(t, birr, color=COLORS[2], lw=1.4, ls="--")
    bx.plot(t, bc1, color=COLORS[0], lw=1.4)
    bx.text(0.62, 0.95, "normal", fontsize=8.5)
    bx.text(0.47, 0.50, "vortex liquid", fontsize=8.5)
    bx.text(0.03, 0.24, "vortex solid\n(pinned)", fontsize=8.5)
    bx.text(0.03, 0.075, "Meissner", fontsize=7.5, color=COLORS[0])
    bx.text(0.08, 1.0, r"$B_{c2}(T)$", fontsize=8.5)
    bx.annotate(r"$B_{irr}(T)$", xy=(0.25, 0.55 * 0.75**1.5), xytext=(0.22, 0.53), fontsize=8.5,
                color=COLORS[2], arrowprops=dict(arrowstyle="-", color=COLORS[2], lw=0.7))
    bx.annotate("$B_{c1}(T)$\n(exaggerated)", xy=(0.52, 0.06 * (1 - 0.52**2)), xytext=(0.58, 0.27),
                fontsize=7.5, color=COLORS[0], arrowprops=dict(arrowstyle="-", color=COLORS[0], lw=0.7))
    bx.set_xlim(0, 1.05)
    bx.set_ylim(0, 1.15)
    bx.set_xlabel(r"$T/T_c$")
    bx.set_ylabel(r"$B/B_{c2}(0)$")
    bx.set_title("(b) Type II phase diagram (cuprate)", fontsize=9.5)

    # (c) vortex lattice
    cx = fig.add_subplot(gs[1, :])
    cx.set_aspect("equal")
    cx.axis("off")
    a0 = 1.0
    xi_r, lam_r = 0.09, 0.42
    pts = []
    for j in range(-1, 4):
        for i in range(-2, 10):
            x = i * a0 + (j % 2) * a0 / 2
            y = j * a0 * np.sqrt(3) / 2
            pts.append((x, y))
    xs = np.linspace(-0.5, 8.5, 500)
    ys = np.linspace(-0.4, 2.2, 200)
    X, Y = np.meshgrid(xs, ys)
    Bmap = np.zeros_like(X)
    from scipy.special import k0
    for (x, y) in pts:
        r = np.hypot(X - x, Y - y)
        Bmap += k0(np.sqrt(r**2 + xi_r**2) / lam_r)
    cx.imshow(Bmap, extent=(xs[0], xs[-1], ys[0], ys[-1]), origin="lower", cmap="Blues", alpha=0.75,
              vmin=Bmap.min(), vmax=Bmap.max() * 1.05)
    for (x, y) in pts:
        if -0.3 < x < 8.3 and -0.2 < y < 2.0:
            cx.add_patch(Circle((x, y), xi_r, fc="#08306B", ec="none"))
            # circulating current arrows (one ring per vortex)
            th = np.linspace(0.3, 2 * np.pi - 0.3, 60)
            cx.plot(x + 0.28 * np.cos(th), y + 0.28 * np.sin(th), color=COLORS[1], lw=0.7)
            cx.annotate("", xy=(x + 0.28 * np.cos(-0.3), y + 0.28 * np.sin(-0.3)),
                        xytext=(x + 0.28 * np.cos(-0.45), y + 0.28 * np.sin(-0.45)),
                        arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=0.7, mutation_scale=6))
    cx.set_xlim(-0.5, 11.3)
    cx.set_ylim(-0.4, 2.2)
    # a0 marker
    y0 = 0.0
    cx.annotate("", xy=(2.0, -0.28), xytext=(3.0, -0.28),
                arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=0.9, mutation_scale=8))
    cx.text(2.5, -0.27, r"$a_0$", ha="center", va="bottom", fontsize=9, color=INK)
    # legend text
    cx.text(8.8, 1.75, "vortex core, radius $\\approx\\xi$\n(normal, dark)", fontsize=8, va="center")
    cx.text(8.8, 1.0, "screening currents\n(orange) and field\n(blue shading)\nextend to $\\approx\\lambda$", fontsize=8,
            va="center")
    cx.text(8.8, 0.15, r"$a_0\approx1.075\sqrt{\Phi_0/B}$" + "\n(22 nm at 5 T)", fontsize=8, va="center")
    cx.set_title("(c) triangular vortex lattice in the mixed state (plan view)", fontsize=9.5)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.95, bottom=0.03)
    save(fig, "30", "fig-30-4-type-i-type-ii")


# ---------------------------------------------------------------- Figure 30.5
def bean_profile_up(x, H, a=1.0, Jc=1.0):
    return np.maximum(H - Jc * (a - np.abs(x)), 0)


def bean_model():
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.8, 3.4), gridspec_kw=dict(width_ratios=[1.1, 1]))
    a, Jc = 1.0, 1.0
    Hs = Jc * a
    x = np.linspace(-a, a, 801)
    cols = [COLORS[5], COLORS[0], "#08306B"]
    for H, c in zip((0.5, 1.0, 2.0), cols):
        ax.plot(x, bean_profile_up(x, H * Hs), color=c, lw=1.6, label=(r"$H=H^*$" if H == 1.0 else rf"$H={H:g}H^*$") + " (up)")
    # reverse sweep: 2H* -> H*
    Hd = 1.0 * Hs
    up = bean_profile_up(x, 2.0 * Hs)
    rev = np.minimum(up, Hd + Jc * (a - np.abs(x)))
    ax.plot(x, rev, color=COLORS[1], lw=1.8, ls="--", label=r"$2H^*\to H^*$ (down)")
    # shading of current regions for the reverse profile
    d = (2.0 * Hs - Hd) / (2 * Jc)
    # current sign J = -dH/dx in each region of the down-sweep profile
    for (x0, x1, sgn) in ((-a, -a + d, -1), (-a + d, 0, +1), (0, a - d, -1), (a - d, a, +1)):
        col = COLORS[1] if sgn < 0 else COLORS[0]
        ax.add_patch(Rectangle((x0, 0), x1 - x0, 0.14, fc=col, alpha=0.35, ec="none"))
        ax.text((x0 + x1) / 2, 0.07, r"$-J_c$" if sgn < 0 else r"$+J_c$", ha="center", va="center", fontsize=7.5)
    ax.text(-1.03, 0.07, "$J$ (down):", ha="right", va="center", fontsize=7)
    ax.text(-0.62, 0.62, r"slope $J_c$", fontsize=8, rotation=-38)
    ax.axvline(-a, color=INK, lw=1)
    ax.axvline(a, color=INK, lw=1)
    ax.set_xlim(-1.62, 1.35)
    ax.set_ylim(0, 2.35)
    ax.set_xticks([-1, -0.5, 0, 0.5, 1])
    ax.set_xticklabels(["$-a$", "", "0", "", "$a$"])
    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(["0", "$H^*$", "$2H^*$"])
    ax.set_xlabel("position in slab $x$")
    ax.set_ylabel("local field $H(x)$")
    ax.legend(fontsize=7.2, loc="upper center", ncol=2, bbox_to_anchor=(0.5, 1.17), handlelength=1.6,
              columnspacing=0.8)
    ax.text(-1.59, 2.2, "(a)", fontsize=10, fontweight="bold")

    # (b) M-H loop of a slab, H in units of H*, M in units of Jc a
    def M_of_history(Hpath):
        # simulate Bean slab numerically via profile memory
        prof = np.zeros_like(x)
        out = []
        for H in Hpath:
            prof = np.minimum(np.maximum(prof, H - Jc * (a - np.abs(x))), H + Jc * (a - np.abs(x)))
            out.append(prof.mean() - H)
        return np.array(out)
    Hm = 4.0
    up1 = np.linspace(0, Hm, 400)
    dn = np.linspace(Hm, -Hm, 800)
    up2 = np.linspace(-Hm, Hm, 800)
    path = np.concatenate([up1, dn, up2])
    M = M_of_history(path)
    n1, n2 = len(up1), len(up1) + len(dn)
    bx.fill_between(up2, M[n2:], np.interp(up2, dn[::-1], M[n1:n2][::-1]), color="#FBE3CF")
    bx.plot(up1, M[:n1], color=COLORS[0], lw=1.6, ls="--", label="virgin curve")
    bx.plot(dn, M[n1:n2], color=COLORS[1], lw=1.6, label="decreasing $H$")
    bx.plot(up2, M[n2:], color=COLORS[2], lw=1.6, label="increasing $H$")
    bx.axhline(0, color="0.5", lw=0.6)
    bx.axvline(0, color="0.5", lw=0.6)
    bx.axhline(-0.5, color="0.6", lw=0.6, ls=":")
    bx.axhline(0.5, color="0.6", lw=0.6, ls=":")
    bx.set_yticks([-0.5, 0, 0.5])
    bx.set_yticklabels([r"$-J_ca/2$", "0", r"$+J_ca/2$"])
    bx.set_xticks([-4, -1, 0, 1, 4])
    bx.set_xticklabels([r"$-H_m$", r"$-H^*$", "0", r"$H^*$", r"$H_m$"])
    bx.set_xlabel("applied field $H$")
    bx.set_ylabel("magnetization $M$")
    bx.set_ylim(-1.12, 0.95)
    bx.text(0.2, 0.1, "loop area = hysteresis\nloss per cycle\n" + r"$Q_h\approx2B_mJ_ca$", fontsize=7.8,
            ha="center", va="bottom")
    bx.legend(fontsize=7.2, loc="lower center", ncol=2, columnspacing=0.8, handlelength=1.6)
    bx.text(-4.3, 0.84, "(b)", fontsize=10, fontweight="bold")
    fig.tight_layout()
    save(fig, "30", "fig-30-5-bean-model")


# ---------------------------------------------------------------- Figure 30.6
def _hex_points(rings, pitch):
    pts = [(0.0, 0.0)]
    for k in range(1, rings + 1):
        for side in range(6):
            a0 = np.pi / 3 * side
            a1 = np.pi / 3 * (side + 1)
            p0 = np.array([np.cos(a0), np.sin(a0)]) * k * pitch
            p1 = np.array([np.cos(a1), np.sin(a1)]) * k * pitch
            for s in range(k):
                p = p0 + (p1 - p0) * s / k
                pts.append(tuple(p))
    return np.array(pts)


def _scalebar(ax, x, y, length, label, color="white"):
    ax.plot([x, x + length], [y, y], color=color, lw=3, solid_capstyle="butt")
    ax.text(x + length / 2, y + 0.025 * (ax.get_ylim()[1] - ax.get_ylim()[0]), label, color=color,
            ha="center", va="bottom", fontsize=8)


def conductor_cross_sections():
    fig = plt.figure(figsize=(6.8, 5.6))
    CU, NBTI, BRONZE, AG = "#D98C4A", "#5A6E8C", "#C9A65A", "#C8CCD2"
    BG = "#2B2B2B"

    # (a) Nb-Ti strand, 0.8 mm diameter, units of um
    ax = fig.add_axes([0.0, 0.5, 0.5, 0.46])
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_xlim(-480, 480); ax.set_ylim(-440, 440)
    ax.add_patch(Rectangle((-480, -440), 960, 880, fc=BG, ec="none"))
    ax.add_patch(Circle((0, 0), 400, fc=CU, ec="none"))
    bundle_centres = _hex_points(3, 88)
    patches = []
    fil = _hex_points(4, 9.0)  # 61 filaments per bundle, 6 um dia on 9 um pitch
    for (bx_, by_) in bundle_centres:
        patches.append(RegularPolygon((bx_, by_), 6, radius=48, orientation=np.pi / 6))
    ax.add_collection(PatchCollection(patches, fc="#E2A36A", ec="#B06A30", lw=0.4))
    circs = [Circle((bx_ + fx, by_ + fy), 3.0) for (bx_, by_) in bundle_centres for (fx, fy) in fil]
    ax.add_collection(PatchCollection(circs, fc=NBTI, ec="none"))
    ax.text(0, -372, "Cu stabilizer", color="white", ha="center", va="center", fontsize=7.5)
    ax.text(-470, 405, f"{len(bundle_centres) * len(fil)} Nb–Ti filaments", color="white", fontsize=7.5)
    _scalebar(ax, -460, -420, 200, "200 µm")
    # zoom inset
    ins = fig.add_axes([0.335, 0.80, 0.155, 0.155])
    ins.set_aspect("equal"); ins.set_xticks([]); ins.set_yticks([])
    for s in ins.spines.values():
        s.set_visible(True); s.set_color("white"); s.set_linewidth(1.2)
    ins.set_xlim(-28, 28); ins.set_ylim(-28, 28)
    ins.add_patch(Rectangle((-28, -28), 56, 56, fc="#E2A36A"))
    for (fx, fy) in _hex_points(4, 9.0):
        ins.add_patch(Circle((fx, fy), 3.0, fc=NBTI, ec="none"))
    ins.plot([-24, -4], [-24, -24], color="white", lw=2.5)
    ins.text(-14, -22, "20 µm", color="white", ha="center", va="bottom", fontsize=7)
    ax.set_title("(a) Nb–Ti strand, Ø 0.8 mm, 6 µm filaments", fontsize=8.8, loc="left")

    # (b) Nb3Sn RRP
    bx = fig.add_axes([0.5, 0.5, 0.5, 0.46])
    bx.set_aspect("equal"); bx.axis("off")
    bx.set_xlim(-480, 480); bx.set_ylim(-440, 440)
    bx.add_patch(Rectangle((-480, -440), 960, 880, fc=BG, ec="none"))
    bx.add_patch(Circle((0, 0), 425, fc=CU, ec="none"))
    bx.add_patch(Circle((0, 0), 335, fc="#7A6A9A", ec="none"))   # Ta/Nb barrier
    bx.add_patch(Circle((0, 0), 322, fc="#E2A36A", ec="none"))   # inner Cu
    sub = [p for p in _hex_points(6, 53) if np.hypot(*p) < 290 and np.hypot(*p) > 1]
    for (sx, sy) in sub:
        bx.add_patch(RegularPolygon((sx, sy), 6, radius=27, orientation=np.pi / 6, fc="#8E8E6A", ec="#E2A36A", lw=0.6))
        bx.add_patch(Circle((sx, sy), 14, fc="#3A3A3A", ec="none"))  # void / Cu-Sn core
    bx.text(0, 0, f"{len(sub)} sub-elements", color="white", ha="center", va="center", fontsize=7,
            bbox=dict(fc=BG, ec="none", pad=1, alpha=0.75))
    _scalebar(bx, -460, -420, 200, "200 µm")
    # zoom of one sub-element
    ins = fig.add_axes([0.84, 0.79, 0.16, 0.16])
    ins.set_aspect("equal"); ins.set_xticks([]); ins.set_yticks([])
    for s in ins.spines.values():
        s.set_visible(True); s.set_color("white"); s.set_linewidth(1.2)
    ins.set_xlim(-34, 34); ins.set_ylim(-34, 34)
    ins.add_patch(Rectangle((-34, -34), 68, 68, fc="#E2A36A"))
    ins.add_patch(RegularPolygon((0, 0), 6, radius=29, orientation=np.pi / 6, fc="#8E8E6A", ec="#E2A36A"))
    ins.add_patch(Circle((0, 0), 15, fc="#3A3A3A"))
    ins.text(0, 0, "void /\nCu–Sn", color="white", ha="center", va="center", fontsize=5.5)
    ins.text(0, -24, r"Nb$_3$Sn", color="white", ha="center", va="center", fontsize=6)
    ins.text(0, 30.5, "≈50 µm", color=INK, ha="center", va="center", fontsize=6)
    bx.text(-470, 395, "Cu stabilizer", color="white", fontsize=7.5)
    bx.annotate("Ta/Nb barrier", xy=(237, -237), xytext=(150, -425), color="white", fontsize=7.5,
                arrowprops=dict(arrowstyle="-", color="white", lw=0.7))
    bx.set_title(r"(b) Nb$_3$Sn RRP wire, Ø 0.85 mm", fontsize=8.8, loc="left")

    # (c) Bi-2223 tape, 4 mm x 0.25 mm  (units: um), drawn at true aspect ratio
    cx = fig.add_axes([0.03, 0.30, 0.94, 0.15])
    cx.set_aspect("equal"); cx.axis("off")
    cx.set_xlim(-2150, 2150); cx.set_ylim(-260, 260)
    cx.add_patch(Rectangle((-2150, -260), 4300, 520, fc=BG, ec="none"))
    cx.add_patch(Rectangle((-2000, 105), 4000, 20, fc="#9AA3AD", ec="none"))     # steel laminations
    cx.add_patch(Rectangle((-2000, -125), 4000, 20, fc="#9AA3AD", ec="none"))
    cx.add_patch(Rectangle((-2000, -105), 4000, 210, fc=AG, ec="none"))          # Ag matrix
    rng = np.random.default_rng(3)
    nfil = 0
    for row, yy in enumerate(np.linspace(-75, 75, 7)):
        ncol = 13 if row % 2 == 0 else 12
        xs = np.linspace(-1800, 1800, ncol) + (0 if row % 2 == 0 else 0)
        for xx in xs:
            w = 120 + rng.normal(0, 12)
            cx.add_patch(Ellipse((xx + rng.normal(0, 15), yy + rng.normal(0, 2)), w, 13, fc="#3E4B8C", ec="none"))
            nfil += 1
    cx.text(-2120, 150, "steel laminations (top and bottom)", color="white", fontsize=7.5, va="bottom")
    cx.text(2120, 150, f"Ag matrix with {nfil} flattened Bi-2223 filaments", color="white", fontsize=7.5,
            va="bottom", ha="right")
    _scalebar(cx, -2120, -240, 500, "0.5 mm")
    cx.set_title("(c) Ag-sheathed Bi-2223 tape, 4 mm × 0.25 mm (true aspect ratio)", fontsize=8.8, loc="left")

    # (d) REBCO coated conductor, layered, not to scale
    dx = fig.add_axes([0.03, 0.0, 0.94, 0.26])
    dx.axis("off")
    dx.set_xlim(0, 10); dx.set_ylim(-0.2, 3.9)
    layers = [("Cu stabilizer, 20 µm", 0.55, CU),
              ("Ag cap, 2 µm", 0.18, AG),
              ("REBCO, 1.5 µm (BaZrO$_3$ nanorods)", 0.45, "#2E5E8C"),
              ("buffer stack ≈0.2 µm: LaMnO$_3$ / MgO / IBAD-MgO /\nY$_2$O$_3$ / Al$_2$O$_3$", 0.30, "#9B7FB8"),
              ("Hastelloy C-276 substrate, 50 µm", 1.1, "#8A9099"),
              ("Ag, 2 µm", 0.15, AG),
              ("Cu stabilizer, 20 µm", 0.55, CU)]
    y = 0.45
    x0, x1 = 0.3, 5.2
    label_y = [0.62, 1.05, 1.7, 2.33, 2.88, 3.24, 3.62]  # bottom to top, spread to avoid overlap
    for (name, hgt, col), ly in zip(reversed(layers), label_y):
        dx.add_patch(Rectangle((x0, y), x1 - x0, hgt, fc=col, ec="white", lw=0.5))
        if "REBCO" in name:
            for xr in np.arange(x0 + 0.08, x1, 0.13):
                dx.plot([xr, xr], [y + 0.05, y + hgt - 0.05], color="#BFD7EE", lw=0.6)
        dx.annotate(name, xy=(x1, y + hgt / 2), xytext=(5.6, ly), fontsize=7.3, va="center",
                    arrowprops=dict(arrowstyle="-", lw=0.5, color="0.4", shrinkA=1, shrinkB=0))
        y += hgt
    # buffer labels compressed into one; width arrow
    dx.annotate("", xy=(x0, 0.22), xytext=(x1, 0.22),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, color=INK, mutation_scale=8))
    dx.text((x0 + x1) / 2, -0.12, "width 4 mm (layer thicknesses not to scale; total ≈0.1 mm)", ha="center",
            fontsize=7.3)
    dx.set_title("(d) REBCO coated conductor (schematic cross-section)", fontsize=8.8, loc="left", y=0.98)
    save(fig, "30", "fig-30-6-conductor-cross-sections")


if __name__ == "__main__":
    perfect_conductor_vs_meissner()
    lambda_xi_interface()
    critical_surface()
    type_i_type_ii()
    bean_model()
    conductor_cross_sections()
