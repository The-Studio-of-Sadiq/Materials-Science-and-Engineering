"""Figures for Chapter 12 — Dislocation Theory.

Run from the repository root:  python figures/scripts/ch12.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle, FancyBboxPatch
from matplotlib.colors import TwoSlopeNorm
from scipy.interpolate import splprep, splev

BLUE, VERM, GREEN, PINK, ORANGE, SKY = COLORS[:6]
GREY = "#A7AEB6"
LGREY = "#C8CDD3"


def _arr(ax, p0, p1, color=INK, lw=1.0, ms=9, style="-|>", **kw):
    ax.annotate("", xy=p1, xytext=p0, arrowprops=dict(arrowstyle=style, color=color, lw=lw,
                mutation_scale=ms, shrinkA=0, shrinkB=0, **kw))


def _perp(ax, x, y, s=0.32, color=VERM, lw=2.0):
    """Edge-dislocation symbol (extra half-plane up)."""
    ax.plot([x - s, x + s], [y, y], color=color, lw=lw, solid_capstyle="butt", zorder=6)
    ax.plot([x, x], [y, y + 1.1 * s], color=color, lw=lw, solid_capstyle="butt", zorder=6)


# ---------------------------------------------------------------- Figure 12.1
def frenkel_and_slip():
    fig = plt.figure(figsize=(6.8, 4.6))
    # (a) rigid shear: two rows of atoms
    a = fig.add_axes([0.0, 0.56, 0.40, 0.40])
    a.set_aspect("equal"); a.axis("off")
    xs = np.arange(6)
    shift = 0.3
    for x in xs:
        a.add_patch(Circle((x, 0), 0.32, fc="#C9D3DD", ec=INK, lw=0.8))
        a.add_patch(Circle((x + shift, 1.0), 0.32, fc=SKY, ec=INK, lw=0.8))
    a.plot([-0.6, 5.9], [0.5, 0.5], color=GREY, lw=0.8, ls="--")
    _arr(a, (2.0, 1.55), (2.0 + shift, 1.55), lw=0.9, ms=7)
    a.text(2.15, 1.65, "x", fontsize=9, ha="center", va="bottom")
    _arr(a, (3, -0.55), (4, -0.55), lw=0.8, ms=6, style="<|-|>")
    a.text(3.5, -0.62, "b", fontsize=9, ha="center", va="top")
    _arr(a, (-0.7, 0), (-0.7, 1.0), lw=0.8, ms=6, style="<|-|>")
    a.text(-0.8, 0.5, "d", fontsize=9, ha="right", va="center")
    _arr(a, (4.3, 1.55), (5.6, 1.55), color=VERM, lw=1.3, ms=9)
    a.text(4.95, 1.65, "τ", color=VERM, fontsize=10, ha="center", va="bottom")
    a.set_xlim(-1.1, 6.2); a.set_ylim(-1.0, 2.1)
    a.set_title("(a) rigid shear of a perfect crystal", fontsize=9.5, loc="left")

    p = fig.add_axes([0.50, 0.60, 0.47, 0.33])
    u = np.linspace(0, 1, 400)
    p.plot(u, np.sin(2 * np.pi * u), color=BLUE)
    p.axhline(0, color=INK, lw=0.6)
    p.plot([0, 0.16], [0, 2 * np.pi * 0.16], color=VERM, lw=1.0, ls="--")
    p.annotate("initial slope: τ = G x/d", xy=(0.09, 0.56), xytext=(0.13, -0.55), color=VERM, fontsize=8, arrowprops=dict(arrowstyle="-", color=VERM, lw=0.7))
    p.plot(0.25, 1, "o", color=BLUE, ms=5)
    p.text(0.30, 1.0, r"$\tau_{\max}=\dfrac{Gb}{2\pi d}\approx\dfrac{G}{2\pi}$", fontsize=9, va="center")
    p.text(0.52, 0.45, "theoretical shear strength\n≈ 7–9 GPa for Cu", fontsize=8, va="center")
    p.set_xlim(0, 1); p.set_ylim(-1.25, 1.45)
    p.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    p.set_yticks([-1, 0, 1]); p.set_yticklabels([r"$-\tau_{\max}$", "0", r"$\tau_{\max}$"])
    p.set_xlabel("displacement x / b", labelpad=1)
    p.set_ylabel("shear stress τ")

    # (b) edge dislocation crossing an 8 x 6 block
    nx, ny = 8, 6
    b_ = 1.0
    frames = [(1.5, "dislocation enters"), (4.0, "glides under low stress"), (8.6, "exits: step of b")]
    for k, (xd, lab) in enumerate(frames):
        ax = fig.add_axes([0.0 + k * 0.245, 0.02, 0.235, 0.42])
        ax.set_aspect("equal"); ax.axis("off")
        X = np.arange(nx, dtype=float)
        for j in range(ny):
            y = j - 2.5          # rows at -2.5..2.5, slip plane at y = 0
            if y > 0:
                w = 1.5 + 0.6 * (y - 0.5)
                ux = (b_ / 2) * (1 - (0.5 * (1 + np.tanh((X - xd) / w))) * 2) * 0 \
                    + b_ * (1 - 0.5 * (1 + np.tanh((X - xd) / w))) - b_ / 2
                ux = ux + b_ / 2
                xx = X + ux
            else:
                xx = X.copy()
            for xi in xx:
                ax.add_patch(Circle((xi, y), 0.22, fc=SKY if y > 0 else "#C9D3DD", ec=INK, lw=0.6))
            # bonds along the row
            ax.plot(xx, np.full_like(xx, y), color="0.6", lw=0.5, zorder=0)
        # vertical lattice lines
        for i in range(nx):
            top = []
            for j in range(ny):
                y = j - 2.5
                if y > 0:
                    w = 1.5 + 0.6 * (y - 0.5)
                    top.append((i + b_ * (1 - 0.5 * (1 + np.tanh((i - xd) / w))), y))
                else:
                    top.append((i, y))
            t = np.array(top)
            ax.plot(t[:3, 0], t[:3, 1], color="0.6", lw=0.5, zorder=0)
            ax.plot(t[3:, 0], t[3:, 1], color="0.6", lw=0.5, zorder=0)
        if -0.4 < xd < nx - 0.2:
            _perp(ax, xd, 0.0, s=0.35)
        ax.plot([-0.9, nx + 0.4], [0, 0], color=GREY, lw=0.6, ls=":")
        _arr(ax, (1.5, 3.25), (5.0, 3.25), color=VERM, lw=1.2, ms=8)
        _arr(ax, (5.5, -3.25), (2.0, -3.25), color=VERM, lw=1.2, ms=8)
        ax.text(5.3, 3.3, "τ", color=VERM, fontsize=9, va="center", ha="left")
        ax.set_xlim(-1.0, nx + 0.6); ax.set_ylim(-4.6, 3.8)
        ax.text((nx - 1) / 2, -4.3, f"({k + 1}) {lab}", fontsize=8, ha="center", va="center")
        if k == 2:
            ax.plot([nx - 1, nx - 1], [-0.3, 0.3], color=INK, lw=0.6)
            ax.plot([nx, nx], [0.3, 0.9], color=INK, lw=0.6)
            _arr(ax, (nx - 1, 0.0), (nx, 0.0), lw=0.8, ms=6, style="<|-|>")
            ax.text(nx + 0.25, -0.05, "b", fontsize=9, ha="left", va="center")
    fig.text(0.01, 0.43, "(b) slip by glide of an edge dislocation", fontsize=9.5)
    # carpet inset
    c = fig.add_axes([0.745, 0.08, 0.25, 0.30])
    c.set_aspect("equal"); c.axis("off")
    xx = np.linspace(0, 6, 300)
    ruck = 0.55 * np.exp(-((xx - 2.4) / 0.35) ** 2)
    c.fill_between(xx, 0, 0.12 + ruck, color="#D9A066", lw=0)
    c.plot(xx, 0.12 + ruck, color="#8A5A2B", lw=1.0)
    c.plot([-0.2, 6.4], [0, 0], color=INK, lw=1.2)
    _arr(c, (2.4, 1.15), (3.6, 1.15), color=VERM, lw=1.2, ms=8)
    c.text(3.0, 1.25, "push the ruck", fontsize=7.5, color=VERM, ha="center", va="bottom")
    c.text(3.0, -0.25, "a ruck moves a carpet\nwith little force", fontsize=8, ha="center", va="top")
    c.set_xlim(-0.3, 6.5); c.set_ylim(-1.3, 1.9)
    save(fig, "12", "fig-12-1-frenkel-and-slip")


# ---------------------------------------------------------------- Figure 12.2
def edge_stress_field():
    nu = 0.3
    n = 401
    x = np.linspace(-5, 5, n)
    X, Y = np.meshgrid(x, x)
    r2 = X ** 2 + Y ** 2
    with np.errstate(divide="ignore", invalid="ignore"):
        sxx = -Y * (3 * X ** 2 + Y ** 2) / r2 ** 2
        sxy = X * (X ** 2 - Y ** 2) / r2 ** 2
        sm = -2 / 3 * (1 + nu) * Y / r2
    core = r2 < 0.5 ** 2
    fields = [(sxx, r"(a) $\sigma_{xx}/D$"), (sxy, r"(b) $\sigma_{xy}/D$"), (sm, r"(c) $\sigma_m/D$ (hydrostatic)")]
    fig, axs = plt.subplots(1, 3, figsize=(6.8, 2.9))
    lev = np.linspace(-0.5, 0.5, 21)
    norm = TwoSlopeNorm(vmin=-0.5, vcenter=0, vmax=0.5)
    for ax, (F, title) in zip(axs, fields):
        G = np.clip(np.where(core, np.nan, F), -0.5, 0.5)
        cf = ax.contourf(X, Y, G, levels=lev, cmap="RdBu_r", norm=norm, extend="both")
        ax.contour(X, Y, np.where(core, np.nan, F), levels=[0], colors="0.3", linewidths=0.5)
        ax.add_patch(Circle((0, 0), 0.5, fc="white", ec="0.4", lw=0.5))
        _perp(ax, 0, 0, s=0.38, color=INK, lw=1.8)
        ax.axhline(0, color=INK, lw=0.7, ls="--")
        ax.set_aspect("equal")
        ax.set_xlim(-5, 5); ax.set_ylim(-5, 5)
        ax.set_xticks([-5, 0, 5]); ax.set_yticks([-5, 0, 5])
        ax.tick_params(labelsize=8)
        ax.set_xlabel("x (nm)", fontsize=8.5, labelpad=1)
        ax.set_title(title, fontsize=9, loc="left")
        for s in ("top", "right"):
            ax.spines[s].set_visible(True)
    axs[0].set_ylabel("y (nm)", fontsize=8.5)
    _arr(axs[0], (2.5, -4.2), (4.3, -4.2), lw=1.0, ms=7)
    axs[0].text(3.4, -3.9, "b", fontsize=9, ha="center", va="bottom")
    axs[2].text(0, 3.4, "small solutes /\nvacancies attracted", fontsize=7, ha="center", va="center",
                bbox=dict(fc="white", ec="none", alpha=0.8, pad=0.6))
    axs[2].text(0, -3.4, "large solutes\nattracted here", fontsize=7, ha="center", va="center",
                bbox=dict(fc="white", ec="none", alpha=0.8, pad=0.6))
    cax = fig.add_axes([0.25, 0.04, 0.5, 0.035])
    cb = fig.colorbar(cf, cax=cax, orientation="horizontal", ticks=[-0.5, -0.25, 0, 0.25, 0.5])
    cb.ax.tick_params(labelsize=8)
    cb.set_label(r"stress / $D$  (nm$^{-1}$),   $D = Gb/[2\pi(1-\nu)]$;  blue = compressive, red = tensile",
                 fontsize=8)
    fig.subplots_adjust(left=0.07, right=0.99, top=0.90, bottom=0.30, wspace=0.28)
    save(fig, "12", "fig-12-2-edge-stress-field")


# ---------------------------------------------------------------- Figure 12.3
def taylor_hardening():
    fig, ax = new_fig(6.4, 4.0)
    alpha, M = 0.3, 3.06
    sr = np.linspace(0, 1.2e8, 300)
    mats = [("Cu", 48e9, 0.2556e-9, VERM, "-"), ("Al", 26e9, 0.286e-9, BLUE, "--"),
            ("Ni", 76e9, 0.249e-9, GREEN, "--")]
    ax.axvspan(1e7, np.sqrt(1e15), color="#EEE6D8", lw=0)
    ax.text(2.08e7, 1150, "cold-worked\nsheet and wire", fontsize=8,
            ha="center", va="top", color="#7A5A2A")
    for name, G, b, c, ls in mats:
        s = M * alpha * G * b * sr / 1e6
        ax.plot(sr, s, color=c, ls=ls, label=f"{name}: G = {G / 1e9:.0f} GPa, b = {b * 1e9:.3f} nm")
    sCu = lambda q: M * alpha * 48e9 * 0.2556e-9 * q / 1e6
    print(f"  Taylor Cu: {sCu(np.sqrt(1e15)):.0f} MPa at 1e15, {sCu(1e8):.0f} at 1e16")
    rng = np.random.default_rng(3)
    q = rng.uniform(0.5e7, 1.05e8, 24)
    pts = sCu(q) * rng.normal(1.0, 0.09, q.size)
    ax.plot(q, pts, "o", mfc="none", mec=INK, ms=5, mew=0.8, label="TEM and XRD measurements (schematic)")
    ax.plot(np.sqrt(1e15), sCu(np.sqrt(1e15)), "s", color=VERM, ms=5)
    ax.annotate("356 MPa", xy=(np.sqrt(1e15), sCu(np.sqrt(1e15))), xytext=(1.1e7, 470), fontsize=8,
                color=VERM, arrowprops=dict(arrowstyle="-", color=VERM, lw=0.7))
    ax.plot(1e8, sCu(1e8), "s", color=VERM, ms=5)
    ax.annotate("1126 MPa", xy=(1e8, sCu(1e8)), xytext=(1.03e8, 950), fontsize=8, color=VERM,
                arrowprops=dict(arrowstyle="-", color=VERM, lw=0.7))
    ax.set_xlim(0, 1.2e8); ax.set_ylim(0, 1200)
    ax.set_xlabel(r"$\sqrt{\rho}$ ($10^{7}$ m$^{-1}$)")
    ax.set_ylabel("tensile flow stress σ = MαGb√ρ (MPa)")
    ax.legend(loc="lower right", fontsize=7.8, title=r"$\alpha$ = 0.3, M = 3.06", title_fontsize=8)
    ax.set_xticks(np.arange(0, 1.21e8, 0.2e8))
    ax.set_xticklabels([f"{v:.0f}" for v in np.arange(0, 12.1, 2)])
    top = ax.secondary_xaxis("top")
    top.set_xticks([1e6, 1e7, np.sqrt(1e15), 1e8])
    top.set_xticklabels([r"$10^{12}$", r"$10^{14}$", r"$10^{15}$", r"$10^{16}$"], fontsize=8.5)
    top.set_xlabel(r"dislocation density ρ (m$^{-2}$)", fontsize=9)
    ax.spines["top"].set_visible(True)
    save(fig, "12", "fig-12-3-taylor-hardening")


# ---------------------------------------------------------------- Figure 12.4
def _smooth(P, n=300, closed=False):
    P = np.asarray(P, float)
    if closed:
        P = np.vstack([P, P[:1]])
    tck, _ = splprep([P[:, 0], P[:, 1]], s=0, per=1 if closed else 0)
    u = np.linspace(0, 1, n)
    x, y = splev(u, tck)
    return np.array(x), np.array(y)


def frank_read_source():
    fig, axs = plt.subplots(1, 5, figsize=(6.8, 2.75))
    A, B = np.array([-1.0, 0.0]), np.array([1.0, 0.0])
    line_c = BLUE

    def arc(R, up=True, n=200):
        h = np.sqrt(max(R ** 2 - 1, 0))
        yc = -h if up else h
        t0 = np.arctan2(0 - yc, -1)
        t1 = np.arctan2(0 - yc, 1)
        if t0 < t1:
            t0 += 2 * np.pi
        t = np.linspace(t1, t0, n)
        return np.cos(t) * R, yc + np.sin(t) * R

    # stage-4 shape (left half from A, then mirrored)
    Lh = [(-1, 0), (-0.85, -0.45), (-0.45, -0.85), (-0.13, -1.12), (-0.35, -1.38), (-1.05, -1.5),
          (-1.7, -1.05), (-1.98, -0.15), (-1.8, 0.8), (-1.05, 1.5), (0, 1.75)]
    Rh = [(-x, y) for x, y in Lh[::-1]][1:]
    st4 = _smooth(Lh + Rh, 400)
    loop = _smooth([(0, 2.2), (1.55, 1.75), (2.3, 0.4), (2.0, -1.2), (0.9, -1.95), (0, -2.0), (-0.9, -1.95),
                    (-2.0, -1.2), (-2.3, 0.4), (-1.55, 1.75)], 400, closed=True)
    history = []
    for k, ax in enumerate(axs):
        ax.set_aspect("equal"); ax.axis("off")
        ax.set_xlim(-2.5, 2.5); ax.set_ylim(-2.3, 2.6)
        for hx, hy in history:
            ax.plot(hx, hy, color=LGREY, lw=1.0)
        if k == 0:
            cur = ([-1, 1], [0, 0])
            ax.plot(*cur, color=line_c, lw=2)
            _arr(ax, (0, -0.7), (0, -0.05), color=VERM, lw=1.2, ms=8)
            ax.text(0.12, -0.6, "τ", color=VERM, fontsize=9)
            _arr(ax, (1.4, -1.2), (1.4, -0.4), color=INK, lw=1.0, ms=7)
            ax.text(1.55, -0.85, "b", fontsize=9, va="center")
            _arr(ax, (-1, -1.5), (1, -1.5), lw=0.7, ms=6, style="<|-|>")
            ax.text(0, -1.75, "L", fontsize=9, ha="center", va="top")
            cap = "(1) pinned\nsegment AB"
        elif k == 1:
            cur = arc(1.9)
            ax.plot(*cur, color=line_c, lw=2)
            ax.text(0, 0.6, "R > L/2", fontsize=8, ha="center")
            cap = "(2) bows out"
        elif k == 2:
            cur = arc(1.0)
            ax.plot(*cur, color=line_c, lw=2)
            ax.text(0, -0.55, "R = L/2", fontsize=8, ha="center")
            cap = "(3) semicircle:\nmax stress τ ≈ Gb/L"
        elif k == 3:
            cur = st4
            ax.plot(*cur, color=line_c, lw=2)
            ax.plot(0, -1.22, "x", color=VERM, ms=6, mew=1.5)
            ax.text(0, -1.62, "P", color=VERM, fontsize=9, ha="center", va="top")
            _arr(ax, (-0.75, -1.85), (-0.2, -1.35), color=VERM, lw=0.8, ms=6)
            _arr(ax, (0.75, -1.85), (0.2, -1.35), color=VERM, lw=0.8, ms=6)
            ax.text(0, 1.95, "edge", fontsize=7.5, ha="center", va="bottom")
            ax.text(-2.05, 0.3, "screw", fontsize=7.5, ha="right", va="center", rotation=90)
            ax.text(2.05, 0.3, "screw", fontsize=7.5, ha="left", va="center", rotation=90)
            cap = "(4) unstable: wraps\nround A, B; meets at P"
        else:
            ax.plot(*loop, color=line_c, lw=2)
            ax.plot([-1, 1], [0, 0], color=line_c, lw=2)
            for t in np.linspace(0, 2 * np.pi, 8, endpoint=False):
                p0 = np.array([2.35 * np.cos(t) * 0.97, 0.1 + 2.2 * np.sin(t)])
            cur = None
            cap = "(5) loop released;\nAB regenerated:\ncycle repeats"
        for P, lab, dx in [(A, "A", -0.32), (B, "B", 0.32)]:
            ax.plot(*P, "o", color=INK, ms=5, zorder=5)
            if k in (0, 1, 2, 4):
                ax.text(P[0] + dx, P[1] - 0.05, lab, fontsize=8.5, ha="center", va="top")
        ax.text(0, -2.35, cap, fontsize=7.6, ha="center", va="top")
        if cur is not None and k < 3:
            history.append(cur)
    fig.subplots_adjust(left=0.0, right=1.0, top=0.98, bottom=0.25, wspace=0.05)
    save(fig, "12", "fig-12-4-frank-read-source")


# ---------------------------------------------------------------- Figure 12.5
def partials_stacking_fault():
    fig = plt.figure(figsize=(6.8, 4.2))
    a = fig.add_axes([0.0, 0.0, 0.45, 0.93])
    a.set_aspect("equal"); a.axis("off")
    e1 = np.array([1.0, 0.0]); e2 = np.array([0.5, np.sqrt(3) / 2])
    for i in range(-2, 7):
        for j in range(-1, 5):
            p = i * e1 + j * e2
            if -0.5 < p[0] < 5.5 and -0.3 < p[1] < 3.7:
                a.add_patch(Circle(p, 0.40, fc="#C9D3DD", ec="0.45", lw=0.7))
                a.text(*p, "A", fontsize=6.5, ha="center", va="center", color="0.35")
    Bsite = lambda i, j: i * e1 + j * e2 + (e1 + e2) / 3
    Csite = lambda i, j: i * e1 + j * e2 + 2 * (e1 + e2) / 3
    for i in range(-2, 7):
        for j in range(-1, 5):
            for f, col, mk in [(Bsite, BLUE, "^"), (Csite, VERM, "v")]:
                p = f(i, j)
                if -0.4 < p[0] < 5.4 and -0.1 < p[1] < 3.5:
                    a.plot(*p, mk, ms=4, color=col)
    B0 = Bsite(1, 1); B1 = Bsite(2, 1); Cm = Csite(1, 1)
    a.text(B0[0] - 0.12, B0[1] - 0.08, "B", color=BLUE, fontsize=10, ha="right", va="top", weight="bold")
    a.text(B1[0] + 0.12, B1[1] - 0.08, "B", color=BLUE, fontsize=10, ha="left", va="top", weight="bold")
    a.text(Cm[0], Cm[1] + 0.12, "C", color=VERM, fontsize=10, ha="center", va="bottom", weight="bold")
    _arr(a, B0, B1, color=INK, lw=2.0, ms=11)
    _arr(a, B0, Cm, color=GREEN, lw=1.8, ms=10)
    _arr(a, Cm, B1, color=GREEN, lw=1.8, ms=10)
    a.text((B0[0] + B1[0]) / 2, B0[1] - 0.22, r"$\mathbf{b}=\frac{a}{2}[\bar{1}01]$", fontsize=9.5,
           ha="center", va="top", bbox=dict(fc="white", ec="none", alpha=0.9, pad=0.6))
    a.text(B0[0] - 0.05, Cm[1] + 0.55, r"$\frac{a}{6}[\bar{2}11]$", fontsize=9, ha="right", va="center",
           color="#006B4E", bbox=dict(fc="white", ec="none", alpha=0.9, pad=0.5))
    a.text(B1[0] + 0.05, Cm[1] + 0.55, r"$\frac{a}{6}[\bar{1}\bar{1}2]$", fontsize=9, ha="left", va="center",
           color="#006B4E", bbox=dict(fc="white", ec="none", alpha=0.9, pad=0.5))
    a.text(-0.5, -0.75, r"Frank's rule: $b^2=a^2/2\;>\;2\times a^2/6=a^2/3$", fontsize=9, ha="left")
    a.plot(-0.3, -1.35, "^", ms=5, color=BLUE)
    a.text(-0.1, -1.35, "B sites", fontsize=8, va="center")
    a.plot(1.5, -1.35, "v", ms=5, color=VERM)
    a.text(1.7, -1.35, "C sites (valley route)", fontsize=8, va="center")
    a.set_xlim(-0.6, 5.6); a.set_ylim(-1.7, 4.2)
    a.text(-0.55, 4.15, "(a) plan view of a (111) A layer", fontsize=9.5, va="top")

    # (b) cross-section
    s = fig.add_axes([0.48, 0.0, 0.52, 0.93])
    s.axis("off")
    seq = "ABCABCAB"
    off = {"A": 0.0, "B": 1 / 3, "C": 2 / 3}
    nxp = 13
    x1, x2 = 3.6, 8.6       # partial positions (in atom spacings)
    dy = 0.62
    s.add_patch(Rectangle((x1, 3.5 * dy), x2 - x1, 4.5 * dy, fc="#FFE3B0", ec="none", zorder=0))
    shift_map = {"A": "B", "B": "C", "C": "A"}
    for j, L in enumerate(seq):
        y = j * dy
        for i in range(nxp):
            xbase = i + off[L]
            if j >= 4:
                f = 0.5 * (np.tanh((xbase - x1) / 0.5) - np.tanh((xbase - x2) / 0.5))
                xx = xbase + f / 3
            else:
                xx = xbase
            s.add_patch(Circle((xx, y), 0.21, fc=SKY if j >= 4 else "#C9D3DD", ec="0.35", lw=0.5))
    s.plot([-0.4, nxp], [3.5 * dy, 3.5 * dy], color=INK, lw=0.7, ls="--")
    for xp, lab in [(x1, "partial 1"), (x2, "partial 2")]:
        _perp(s, xp, 3.5 * dy, s=0.3, color=VERM, lw=1.8)
        s.text(xp, -0.45, lab, fontsize=7.8, ha="center", va="top", color=VERM)
    _arr(s, (x1, 8 * dy - 0.25), (x2, 8 * dy - 0.25), lw=0.8, ms=7, style="<|-|>")
    s.text((x1 + x2) / 2, 8 * dy - 0.18, "d  (faulted ribbon, shaded)", fontsize=8, ha="center", va="bottom")
    s.text(-1.0, 8 * dy - 0.2, "outside", fontsize=7.5, ha="center", va="bottom")
    s.text(nxp + 0.6, 8 * dy - 0.2, "inside", fontsize=7.5, ha="center", va="bottom", color="#8A5A00")
    for j, L in enumerate(seq):
        s.text(-1.0, j * dy, L, fontsize=9, ha="center", va="center")
        Lf = shift_map[L] if j >= 4 else L
        s.text(nxp + 0.6, j * dy, Lf, fontsize=9, ha="center", va="center", weight="bold", color="#8A5A00")
    s.text(-1.0, -0.45, "ABCABCAB", fontsize=7.2, ha="center", va="top")
    s.text(nxp + 0.6, -0.45, "ABCACABC", fontsize=7.2, ha="center", va="top", color="#8A5A00")
    s.set_xlim(-1.8, nxp + 1.4); s.set_ylim(-4.1, 8 * dy + 1.3)
    s.set_aspect("equal")
    s.text(-1.7, 8 * dy + 1.25, "(b) cross-section: two Shockley partials", fontsize=9.5, va="top")
    # width table
    rows = [("Al", "0.7"), ("Ni", "2"), ("Cu", "3.7"), ("austenitic stainless", "13")]
    tx, ty = 2.0, -1.35
    s.add_patch(FancyBboxPatch((tx - 0.3, ty - 2.55), 8.4, 2.85, boxstyle="round,pad=0.05", fc="white",
                               ec="0.6", lw=0.6))
    s.text(tx, ty, "equilibrium width d", fontsize=8, weight="bold", va="center")
    for k, (m, d) in enumerate(rows):
        col, row = 0, k
        xx = tx + col * 4.8
        yy = ty - 0.55 - row * 0.55
        s.text(xx, yy, m, fontsize=8, va="center")
        s.text(xx + 7.8, yy, f"≈ {d} nm", fontsize=8, ha="right", va="center")
    save(fig, "12", "fig-12-5-partials-stacking-fault")


# ---------------------------------------------------------------- Figure 12.6
def crss_temperature():
    fig, ax = new_fig(6.4, 4.2)
    t = np.linspace(0, 0.5, 400)
    # BCC: thermally activated Peierls component (Kocks form p = 1/2, q = 3/2) + athermal plateau
    Tk = 0.18
    tstar = 4.9e-3 * np.clip(1 - np.sqrt(t / Tk), 0, None) ** 1.5
    bcc = 1.0e-4 * (1 - 0.3 * t) + tstar
    fcc = 1.5e-5 * (1 - 0.6 * t)
    mg_b = 3.0e-5 * (1 - 0.3 * t)
    mg_ca = 5e-3 * np.exp(-t / 0.5 * np.log(5e-3 / 3e-4))
    al2o3 = 1e-2 * np.exp(-t / 0.5 * np.log(10))
    ax.fill_between(t, 1e-4 * (1 - 0.6 * t), 1e-3 * (1 - 0.6 * t), color="#EEE6D8", lw=0,
                    label="NaCl, MgO (ceramic band)")
    ax.plot(t, bcc, color=BLUE, label="BCC (Fe, Nb, W)")
    ax.plot(t, fcc, color=VERM, label="FCC (Cu, Al)")
    ax.plot(t, mg_b, color=GREEN, label="HCP Mg, basal ⟨a⟩")
    ax.plot(t, mg_ca, color=GREEN, ls="--", label="HCP Mg, prismatic / pyramidal ⟨c+a⟩")
    ax.plot(t, al2o3, color=INK, ls=":", lw=2.0, label="Al₂O₃ basal slip")
    tfe = 293 / 1811
    bfe = 1.0e-4 * (1 - 0.3 * tfe) + 4.9e-3 * max(1 - np.sqrt(tfe / Tk), 0) ** 1.5
    ax.plot(tfe, bfe, "o", color=BLUE, ms=6, mfc="white", mew=1.5, zorder=5)
    ax.annotate("Fe at room temperature (T/Tm ≈ 0.16)", xy=(tfe, bfe), xytext=(0.21, 4.8e-5), fontsize=7.8,
                color=BLUE, va="center", arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.7))
    ax.text(0.006, 2.4e-4, "Peierls-controlled\n(thermally activated)", fontsize=8, color=BLUE, ha="left",
            va="center")
    ax.text(0.30, 1.25e-4, "athermal plateaus (forest, solutes)", fontsize=8, color="0.3", ha="left",
            va="bottom")
    ax.axvspan(0.15, 0.20, color=BLUE, alpha=0.07, lw=0)
    ax.text(0.175, 1.4e-2, "knee", fontsize=7.5, color=BLUE, ha="center", va="center")
    ax.set_yscale("log")
    ax.set_xlim(0, 0.5); ax.set_ylim(1e-6, 2e-2)
    ax.set_xlabel("homologous temperature T / Tm")
    ax.set_ylabel("critical resolved shear stress τc / G")
    ax.legend(loc="lower right", fontsize=7.4, ncol=2, columnspacing=1.0, handlelength=1.8)
    save(fig, "12", "fig-12-6-crss-temperature")


if __name__ == "__main__":
    frenkel_and_slip()
    edge_stress_field()
    taylor_hardening()
    frank_read_source()
    partials_stacking_fault()
    crss_temperature()
