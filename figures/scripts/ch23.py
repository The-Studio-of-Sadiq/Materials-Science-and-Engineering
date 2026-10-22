"""Figures for Chapter 23 — Laminate Theory, Failure and Composite Manufacturing.

Run from the repository root:  python figures/scripts/ch23.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle, Ellipse, FancyArrowPatch, Arc
import matplotlib.transforms as mtransforms

from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK

# ---------------------------------------------------------------- CLT core (T300/epoxy, Table 22.3)
E1, E2, G12, NU12 = 181e3, 10.3e3, 7.17e3, 0.28      # MPa
A1, A2 = 0.02e-6, 22.5e-6                             # 1/K
XT, XC, YT, YC, S = 1500.0, 1500.0, 40.0, 246.0, 68.0  # MPa
TPLY = 0.125                                          # mm

PLY_C = "#F3E9C6"
FIB = "#8A7A50"


def _Q(e1=E1, e2=E2, g=G12, n=NU12):
    n21 = n * e2 / e1
    d = 1 - n * n21
    return np.array([[e1 / d, n * e2 / d, 0], [n * e2 / d, e2 / d, 0], [0, 0, g]])


def _T(th):
    c, s = np.cos(np.radians(th)), np.sin(np.radians(th))
    return np.array([[c * c, s * s, 2 * s * c], [s * s, c * c, -2 * s * c], [-s * c, s * c, c * c - s * s]])


_R = np.diag([1.0, 1.0, 2.0])


def _Qbar(th, Q=None):
    Q = _Q() if Q is None else Q
    return np.linalg.inv(_T(th)) @ Q @ _R @ _T(th) @ np.linalg.inv(_R)


def _alpha(th):
    c, s = np.cos(np.radians(th)), np.sin(np.radians(th))
    return np.array([A1 * c * c + A2 * s * s, A1 * s * s + A2 * c * c, 2 * (A1 - A2) * s * c])


def _abd(angles, t=TPLY):
    n = len(angles)
    h = n * t
    z = np.linspace(-h / 2, h / 2, n + 1)
    A, B, D = np.zeros((3, 3)), np.zeros((3, 3)), np.zeros((3, 3))
    for k, th in enumerate(angles):
        q = _Qbar(th)
        A += q * (z[k + 1] - z[k])
        B += q * (z[k + 1] ** 2 - z[k] ** 2) / 2
        D += q * (z[k + 1] ** 3 - z[k] ** 3) / 3
    return A, B, D, z


def _fibre_lines(ax, poly_pts, ang_deg, spacing, color=FIB, lw=0.5, zorder=3, project=None):
    """Fill a polygon (already drawn) with parallel lines at ang_deg (in the plate plane)."""
    patch = Polygon(np.array(poly_pts), closed=True, fc="none", ec="none")
    ax.add_patch(patch)
    cen = np.mean(np.array(poly_pts), axis=0)
    th = np.radians(ang_deg)
    d, nrm = np.array([np.cos(th), np.sin(th)]), np.array([-np.sin(th), np.cos(th)])
    for s in np.arange(-6, 6, spacing):
        p0, p1 = s * nrm - 8 * d, s * nrm + 8 * d
        if project is not None:
            p0, p1 = project(p0), project(p1)
        p0, p1 = p0 + (cen if project is None else 0), p1 + (cen if project is None else 0)
        ln, = ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=color, lw=lw, zorder=zorder)
        ln.set_clip_path(patch)


# ---------------------------------------------------------------- 23.1
def laminate_geometry():
    fig = plt.figure(figsize=(6.8, 5.8))
    gs = fig.add_gridspec(2, 3, height_ratios=[1.55, 1], width_ratios=[1.6, 0.75, 0.9], hspace=0.3, wspace=0.32)
    axs = fig.add_subplot(gs[0, 0])
    axe = fig.add_subplot(gs[0, 1])
    axq = fig.add_subplot(gs[0, 2], sharey=axe)
    axb = fig.add_subplot(gs[1, :])

    angles = [0, 45, -45, 90, 90, -45, 45, 0]
    n = len(angles)
    # --- exploded stack (oblique projection of each ply)
    axs.set_aspect("equal")
    axs.axis("off")
    W, Dp, t, g = 2.4, 1.0, 0.08, 0.46
    k_ob, a_ob = 0.9, np.radians(40)

    def P(x, z):
        return np.array([x + k_ob * z * np.cos(a_ob), k_ob * z * np.sin(a_ob)])

    ytop = 0.0
    ys = []
    for k, th in enumerate(angles):
        y = ytop - k * (t + g)
        ys.append(y)
    for k in range(n - 1, -1, -1):   # draw bottom ply first
        y = ys[k]
        top = [P(0, 0) + [0, y], P(W, 0) + [0, y], P(W, Dp) + [0, y], P(0, Dp) + [0, y]]
        front = [P(0, 0) + [0, y - t], P(W, 0) + [0, y - t], P(W, 0) + [0, y], P(0, 0) + [0, y]]
        side = [P(W, 0) + [0, y - t], P(W, Dp) + [0, y - t], P(W, Dp) + [0, y], P(W, 0) + [0, y]]
        zb = 2 + (n - k) * 3
        pt = Polygon(np.array(top), closed=True, fc=PLY_C, ec=INK, lw=0.7, zorder=zb)
        axs.add_patch(pt)
        axs.add_patch(Polygon(np.array(front), closed=True, fc="#E6D9AE", ec=INK, lw=0.7, zorder=zb))
        axs.add_patch(Polygon(np.array(side), closed=True, fc="#DCCD9A", ec=INK, lw=0.7, zorder=zb))
        th = np.radians(angles[k])
        d = np.array([np.cos(th), np.sin(th)])
        nv = np.array([-np.sin(th), np.cos(th)])
        for s in np.arange(-2.5, 2.5, 0.2):
            b = np.array([W / 2, Dp / 2]) + s * nv
            p0, p1 = P(*(b - 3 * d)) + [0, y], P(*(b + 3 * d)) + [0, y]
            ln, = axs.plot([p0[0], p1[0]], [p0[1], p1[1]], color=FIB, lw=0.45, zorder=zb + 1)
            ln.set_clip_path(pt)
        lab = f"{angles[k]:+d}°".replace("-", "−") if angles[k] not in (0, 90) else f"{angles[k]}°"
        axs.text(-0.1, y - t / 2, lab, ha="right", va="center", fontsize=7.6)
        axs.text(-1.05, y - t / 2, f"{k + 1}", ha="center", va="center", fontsize=7, color="0.45")
    axs.text(-1.05, ys[0] + 0.32, "ply", ha="center", fontsize=7, color="0.45")
    # interface coordinates (right of the stack)
    xr = P(W, Dp)[0] + 0.15
    for k in range(n + 1):
        y = ys[0] if k == 0 else ys[k - 1] - t
        if k in (0, 4, 8):
            lab = {0: r"$z_0=-h/2$", 4: r"$z_4=0$", 8: r"$z_8=+h/2$"}[k]
        else:
            lab = f"$z_{k}$"
        # interface sits midway in the gap for display
        yy = (ys[k - 1] - t + ys[k]) / 2 if 0 < k < n else (ys[0] + 0.0 if k == 0 else ys[-1] - t)
        axs.text(xr + 0.05, yy, lab, fontsize=7.3, va="center")
    ymid = (ys[3] - t + ys[4]) / 2
    axs.plot([-0.1, xr], [ymid, ymid], ls="--", color=COLORS[0], lw=0.9, zorder=50)
    axs.text(1.2, ymid + 0.03, "mid-plane", color=COLORS[0], fontsize=7.3, va="bottom", zorder=51,
             bbox=dict(fc="white", ec="none", pad=0.3, alpha=0.8))
    axs.annotate("", xy=(-1.35, ys[-1] - 0.3), xytext=(-1.35, ys[0] + 0.25),
                 arrowprops=dict(arrowstyle="-|>", lw=1.1, color=INK, mutation_scale=9))
    axs.text(-1.42, ys[-1] - 0.25, "$z$", fontsize=10, ha="right", va="center")
    axs.set_xlim(-1.6, xr + 1.2)
    axs.set_ylim(ys[-1] - 0.5, ys[0] + P(W, Dp)[1] + 0.1)
    axs.set_title("[0/±45/90]$_s$, plies 0.125 mm", fontsize=9)

    # --- strain and stress through thickness: CLT under N_x and M_x
    A, B, D, z = _abd(angles)
    ABD = np.block([[A, B], [B, D]])
    Nx, Mx = 300.0, 20.0   # N/mm and N mm/mm
    sol = np.linalg.solve(ABD, [Nx, 0, 0, Mx, 0, 0])
    e0, kap = sol[:3], sol[3:]
    zz = np.linspace(z[0], z[-1], 200)
    ex = e0[0] + zz * kap[0]
    axe.plot(ex * 100, zz, color=COLORS[0], lw=1.8)
    axe.axvline(0, color="0.6", lw=0.6)
    for zi in z:
        axe.axhline(zi, color="0.85", lw=0.5, zorder=0)
        axq.axhline(zi, color="0.85", lw=0.5, zorder=0)
    axe.axhline(0, color=COLORS[0], ls="--", lw=0.8)
    axe.set_xlabel(r"strain $\varepsilon_x$ (%)", fontsize=8.5)
    axe.set_ylabel("$z$ (mm)", fontsize=8.5)
    axe.set_ylim(z[-1] + 0.03, z[0] - 0.03)   # z down
    axe.set_xlim(0, max(ex) * 100 * 1.25)
    axe.set_title("linear strain", fontsize=9)
    axe.tick_params(labelsize=7.5)
    for k, th in enumerate(angles):
        zs = np.linspace(z[k], z[k + 1], 20)
        eps = np.vstack([e0[0] + zs * kap[0], e0[1] + zs * kap[1], e0[2] + zs * kap[2]])
        sig = (_Qbar(th) @ eps)[0]
        col = {0: COLORS[1], 45: COLORS[2], -45: COLORS[2], 90: COLORS[3]}[th]
        axq.fill_betweenx(zs, 0, sig, color=col, alpha=0.35, lw=0)
        axq.plot(sig, zs, color=col, lw=1.6)
    axq.axvline(0, color="0.6", lw=0.6)
    axq.axhline(0, color=COLORS[0], ls="--", lw=0.8)
    axq.set_xlabel(r"stress $\sigma_x$ (MPa)", fontsize=8.5)
    axq.set_title("stress jumps at interfaces", fontsize=9)
    axq.tick_params(labelsize=7.5)
    plt.setp(axq.get_yticklabels(), visible=False)
    axq.set_xlim(-40, 1250)
    smax = 1240
    axq.text(smax * 0.98, (z[0] + z[1]) / 2, "0°", fontsize=7.5, color=COLORS[1], ha="right", va="center")
    axq.text(smax * 0.98, (z[1] + z[2]) / 2, "±45°", fontsize=7.5, color=COLORS[2], ha="right", va="center")
    axq.text(smax * 0.98, (z[3] + z[4]) / 2, "90°", fontsize=7.5, color=COLORS[3], ha="right", va="center")
    axq.text(smax * 0.98, (z[7] + z[8]) / 2, "0°", fontsize=7.5, color=COLORS[1], ha="right", va="center")
    axe.text(0.97, 0.03, f"$N_x$ = {Nx:.0f} N/mm\n$M_x$ = {Mx:.0f} N mm/mm", transform=axe.transAxes,
             fontsize=7, ha="right", va="bottom", color="0.3")

    # --- bottom: plate element with force and moment resultants
    axb.set_aspect("equal")
    axb.axis("off")
    axb.set_xlim(0, 18.6)
    axb.set_ylim(-0.4, 5.4)

    def element(cx, cy, s):
        axb.add_patch(Rectangle((cx - s, cy - s), 2 * s, 2 * s, fc="#F5F5F5", ec=INK, lw=1.0))

    s = 1.32
    c1 = np.array([3.2, 2.6])
    element(*c1, s)
    kw_n = dict(arrowstyle="-|>", color=COLORS[0], lw=1.6, mutation_scale=11)
    kw_s = dict(arrowstyle="-|>", color=COLORS[3], lw=1.4, mutation_scale=10)
    for sg in (1, -1):
        axb.annotate("", xy=c1 + [sg * (s + 1.0), 0], xytext=c1 + [sg * s, 0], arrowprops=kw_n)
        axb.annotate("", xy=c1 + [0, sg * (s + 0.9)], xytext=c1 + [0, sg * s], arrowprops=kw_n)
        axb.annotate("", xy=c1 + [sg * (s + 0.15), sg * 0.75], xytext=c1 + [sg * (s + 0.15), -sg * 0.75], arrowprops=kw_s)
        axb.annotate("", xy=c1 + [sg * 0.75, sg * (s + 0.15)], xytext=c1 + [-sg * 0.75, sg * (s + 0.15)], arrowprops=kw_s)
    axb.text(*(c1 + [s + 1.15, 0]), "$N_x$", fontsize=10, color=COLORS[0], va="center")
    axb.text(*(c1 + [0.12, s + 0.95]), "$N_y$", fontsize=10, color=COLORS[0], va="center")
    axb.text(*(c1 + [s + 0.3, 0.95]), "$N_{xy}$", fontsize=9.5, color=COLORS[3], va="center")
    axb.text(*c1, "forces\n(N/mm)", ha="center", va="center", fontsize=8)

    c2 = np.array([10.4, 2.6])
    element(*c2, s)
    kw_m = dict(arrowstyle="-|>", color=COLORS[1], lw=1.5, mutation_scale=10)
    kw_t = dict(arrowstyle="-|>", color=COLORS[2], lw=1.5, mutation_scale=10)

    def dbl(p0, p1, kw):  # double-headed moment vector: arrow with a second head
        axb.annotate("", xy=p1, xytext=p0, arrowprops=kw)
        p_mid = p0 + 0.82 * (np.array(p1) - np.array(p0))
        axb.annotate("", xy=p_mid, xytext=p0, arrowprops=kw)

    # bending moments M_x act on x-faces, vector along y (right-hand rule)
    for sg in (1, -1):
        p = c2 + [sg * (s + 0.35), 0]
        dbl(p - [0, sg * 0.8], p + [0, sg * 0.8], kw_m)
        p = c2 + [0, sg * (s + 0.35)]
        dbl(p + [sg * 0.8, 0], p - [sg * 0.8, 0], kw_m)
    # twisting moments M_xy: vectors normal to the faces
    for sg in (1, -1):
        p = c2 + [sg * (s + 0.55), -0.95]
        dbl(p - [sg * 0.0, 0], p + [sg * 0.85, 0], kw_t)
    axb.text(*(c2 + [s + 0.55, 1.0]), "$M_x$", fontsize=10, color=COLORS[1], va="center")
    axb.text(*(c2 + [0.9, s + 0.75]), "$M_y$", fontsize=10, color=COLORS[1], va="center")
    axb.text(*(c2 + [s + 1.55, -0.95]), "$M_{xy}$", fontsize=9.5, color=COLORS[2], va="center")
    axb.text(*c2, "moments\n(N mm/mm)", ha="center", va="center", fontsize=8)
    axb.text(16.3, 2.6, r"$\begin{pmatrix}\mathbf{N}\\ \mathbf{M}\end{pmatrix}$" if False else
             "N = [A] ε⁰ + [B] κ\nM = [B] ε⁰ + [D] κ", ha="center", va="center", fontsize=9,
             bbox=dict(fc="#EEF3F8", ec=INK, lw=0.8, boxstyle="round,pad=0.4"))
    axb.text(7.0, -0.3, "resultants per unit width of the plate; double-headed arrows are moment vectors (right-hand rule)", fontsize=7.2, ha="center", color="0.35")
    # axes
    axb.annotate("", xy=(0.9, 0.2), xytext=(0.2, 0.2), arrowprops=dict(arrowstyle="-|>", lw=1.0, mutation_scale=8))
    axb.annotate("", xy=(0.2, 0.9), xytext=(0.2, 0.2), arrowprops=dict(arrowstyle="-|>", lw=1.0, mutation_scale=8))
    axb.text(0.95, 0.2, "$x$", fontsize=9, va="center")
    axb.text(0.2, 1.0, "$y$", fontsize=9, ha="center")
    save(fig, "23", "fig-23-1-laminate-geometry")


# ---------------------------------------------------------------- 23.2
def laminate_coupling():
    fig, axs = plt.subplots(1, 3, figsize=(6.8, 3.4), gridspec_kw=dict(wspace=0.05))
    for ax in axs:
        ax.set_aspect("equal")
        ax.axis("off")

    # (a) unbalanced [30]_4 under N_x: compute shear/extension ratio from CLT
    ax = axs[0]
    A, B, D, z = _abd([30, 30, 30, 30])
    a = np.linalg.inv(A)
    eps = a @ [1.0, 0, 0]
    ratio_g, ratio_y = eps[2] / eps[0], eps[1] / eps[0]
    ex_vis = 0.10
    F = np.array([[1 + ex_vis, ex_vis * ratio_g], [0, 1 + ex_vis * ratio_y]])
    w, h = 1.6, 1.0
    sq = np.array([[-w, -h], [w, -h], [w, h], [-w, h]])
    ax.add_patch(Polygon(sq, closed=True, fill=False, ec="0.45", ls="--", lw=1.0, zorder=4))
    dfm = sq @ F.T
    pd = Polygon(dfm, closed=True, fc=PLY_C, ec=COLORS[1], lw=1.4, zorder=2)
    ax.add_patch(pd)
    th = np.radians(30)
    d, nv = np.array([np.cos(th), np.sin(th)]), np.array([-np.sin(th), np.cos(th)])
    for s_ in np.arange(-3, 3, 0.2):
        pts = np.array([s_ * nv - 4 * d, s_ * nv + 4 * d]) @ F.T
        ln, = ax.plot(pts[:, 0], pts[:, 1], color=FIB, lw=0.5, zorder=3)
        ln.set_clip_path(pd)
    for yy in (-0.6, 0, 0.6):
        for sg in (1, -1):
            x_edge = (np.array([sg * w, yy]) @ F.T)[0]
            ax.annotate("", xy=(x_edge + sg * 0.55, yy), xytext=(x_edge + sg * 0.05, yy),
                        arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.2, mutation_scale=9), zorder=5)
    ax.text(2.45, 0.85, "$N_x$", color=COLORS[0], fontsize=10)
    ax.set_xlim(-2.6, 2.7)
    ax.set_ylim(-2.6, 2.4)
    ax.text(0, 1.55, "(a) unbalanced [30]$_4$", ha="center", fontsize=9, fontweight="bold")
    ax.text(0, -1.55, r"$A_{16}\neq0$: extension–shear", ha="center", fontsize=8.5, color=COLORS[1])
    ax.text(0, -2.05, f"γ$_{{xy}}$/ε$_x$ = {ratio_g:.2f} (CLT)".replace("-", "−"), ha="center", fontsize=7.6, color="0.35")
    ax.text(0, -2.5, "dashed: unloaded; shear exaggerated", ha="center", fontsize=7, color="0.35")

    # (b) thermal warping of unsymmetric [0/90]_T vs flat [0/90]_s
    ax = axs[1]
    A, B, D, z = _abd([0, 90])
    ABD = np.block([[A, B], [B, D]])
    NT, MT = np.zeros(3), np.zeros(3)
    for k, th in enumerate([0, 90]):
        q = _Qbar(th)
        NT += q @ _alpha(th) * (z[k + 1] - z[k])
        MT += q @ _alpha(th) * (z[k + 1] ** 2 - z[k] ** 2) / 2
    sol = np.linalg.solve(ABD, np.concatenate([NT, MT]) * -150.0)
    R = 1 / abs(sol[4])
    # cylindrical panel 100 mm x 100 mm bent about x (curvature in y): oblique 3D sketch
    Lp = 100.0
    yy = np.linspace(-Lp / 2, Lp / 2, 41)
    wdef = R - np.sqrt(R ** 2 - yy ** 2)  # rises at the edges
    sc = 1 / 45.0
    kx, ang = 0.55, np.radians(28)

    def P3(x, y, zv):
        return np.array([sc * (x + kx * y * np.cos(ang)), sc * (zv + kx * y * np.sin(ang)) + 0.0])

    xx = yy.copy()                       # curvature drawn along the horizontal direction
    front = np.array([P3(x, -Lp / 2, w_) for x, w_ in zip(xx, wdef)])
    back = np.array([P3(x, Lp / 2, w_) for x, w_ in zip(xx, wdef)])
    off = np.array([-0.3, 0.2])
    ax.add_patch(Polygon(np.concatenate([front, back[::-1]]) + off, closed=True, fc="#DCE6F0", ec=COLORS[0], lw=1.2))
    for x, w_ in zip(xx[::5], wdef[::5]):
        line = np.array([P3(x, -Lp / 2, w_), P3(x, Lp / 2, w_)]) + off
        ax.plot(line[:, 0], line[:, 1], color=COLORS[0], lw=0.5, alpha=0.7)
    ax.plot(front[:, 0] + off[0], front[:, 1] + off[1], color=COLORS[0], lw=1.6)
    ax.text(0.0, 1.2, "snaps to a cylinder (bistable)", ha="center", fontsize=7, color="0.35")
    ax.text(0.0, 2.3, "(b) unsymmetric [0/90]$_T$", ha="center", fontsize=9, fontweight="bold")
    ax.text(0.0, 1.95, f"cooled 150 K from cure: R ≈ {R:.0f} mm", ha="center", fontsize=7.6)
    ax.text(0.0, 1.62, "(h = 0.25 mm, 100 mm panel)", ha="center", fontsize=7.2, color="0.35")
    ax.text(0.0, -0.5, r"$B\neq0$: thermal warping", ha="center", fontsize=8.5, color=COLORS[0])
    # flat symmetric plate
    off2 = np.array([0.0, -1.55])
    flat = np.array([P3(-Lp / 2, -Lp / 2, 0), P3(Lp / 2, -Lp / 2, 0), P3(Lp / 2, Lp / 2, 0), P3(-Lp / 2, Lp / 2, 0)]) + off2
    ax.add_patch(Polygon(flat, closed=True, fc="#E8EFE3", ec=COLORS[2], lw=1.2))
    ax.text(0.0, -2.2, "[0/90]$_s$ flat:", ha="center", fontsize=8, color=COLORS[2])
    ax.text(0.0, -2.55, r"symmetric, $B=0$", ha="center", fontsize=8.5, color=COLORS[2])
    ax.set_xlim(-2.6, 2.6)
    ax.set_ylim(-2.6, 2.4)

    # (c) bend-twist coupling of a cantilever strip
    ax = axs[2]
    L, b = 3.6, 0.55
    xs = np.linspace(0, L, 40)
    wv = -0.45 * (xs / L) ** 2 * (3 - xs / L) / 2       # cantilever deflection shape (scaled)
    phi = np.radians(40) * (xs / L)                        # twist grows along the span
    kx2, ang2 = 0.6, np.radians(30)

    def P2(x, yv, zv):
        return np.array([x + kx2 * yv * np.cos(ang2), zv + kx2 * yv * np.sin(ang2)])

    lead = np.array([P2(x, b * np.cos(p), w_ + b * np.sin(p)) for x, w_, p in zip(xs, wv, phi)])
    trail = np.array([P2(x, -b * np.cos(p), w_ - b * np.sin(p)) for x, w_, p in zip(xs, wv, phi)])
    x0 = -1.7
    lead[:, 0] += x0
    trail[:, 0] += x0
    ax.add_patch(Polygon(np.concatenate([lead, trail[::-1]]), closed=True, fc="#F1E3EC", ec=COLORS[3], lw=1.2))
    for i in range(0, 40, 6):
        ax.plot([lead[i, 0], trail[i, 0]], [lead[i, 1], trail[i, 1]], color=COLORS[3], lw=0.5)
    # undeformed outline
    lead0 = np.array([P2(x, b, 0) for x in xs]) + [x0, 0]
    trail0 = np.array([P2(x, -b, 0) for x in xs]) + [x0, 0]
    ax.add_patch(Polygon(np.concatenate([lead0, trail0[::-1]]), closed=True, fill=False, ec="0.5", ls="--", lw=0.9))
    # clamp
    cl = np.array([P2(0, -b - 0.2, -0.5), P2(0, b + 0.2, -0.5), P2(0, b + 0.2, 0.5), P2(0, -b - 0.2, 0.5)]) + [x0, 0]
    ax.add_patch(Polygon(cl, closed=True, fc="0.75", ec=INK, lw=0.8, hatch="////"))
    tip = (lead[-1] + trail[-1]) / 2
    ax.annotate("", xy=tip, xytext=tip + [0, 0.9], arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.4, mutation_scale=10))
    ax.text(tip[0] + 0.12, tip[1] + 0.6, "$P$", fontsize=10)
    ax.annotate("tip twist", xy=lead[-1], xytext=(lead[-1][0] - 1.3, lead[-1][1] + 0.75), fontsize=7.8, ha="center",
                arrowprops=dict(arrowstyle="-", lw=0.6, color="0.35"))
    ax.text(0.0, 1.55, "(c) [+30/−30/+30/−30]", ha="center", fontsize=9, fontweight="bold")
    ax.text(0.0, -1.55, r"$D_{16}\neq0$: bend–twist coupling", ha="center", fontsize=8.5, color=COLORS[3])
    ax.text(0.0, -2.05, "(aeroelastic tailoring)", ha="center", fontsize=8, color=COLORS[3])
    ax.set_xlim(-2.6, 2.6)
    ax.set_ylim(-2.6, 2.4)
    save(fig, "23", "fig-23-2-laminate-coupling")
    return R


# ---------------------------------------------------------------- 23.3
def _th_radius(u, v):
    """Tsai–Hill failure radius along direction (u, v) in the sigma1–sigma2 plane (tau12 = 0)."""
    X = XT if u >= 0 else XC
    Y = YT if v >= 0 else YC
    return 1 / np.sqrt(u * u / X ** 2 - u * v / X ** 2 + v * v / Y ** 2)


def _tw_radius(u, v, t=0.0):
    F1, F2 = 1 / XT - 1 / XC, 1 / YT - 1 / YC
    F11, F22, F66 = 1 / (XT * XC), 1 / (YT * YC), 1 / S ** 2
    F12 = -0.5 * np.sqrt(F11 * F22)
    a = F11 * u * u + F22 * v * v + F66 * t * t + 2 * F12 * u * v
    b = F1 * u + F2 * v
    return (-b + np.sqrt(b * b + 4 * a)) / (2 * a)


def _ms_radius(u, v, t=0.0):
    r = []
    if u > 0:
        r.append(XT / u)
    if u < 0:
        r.append(XC / -u)
    if v > 0:
        r.append(YT / v)
    if v < 0:
        r.append(YC / -v)
    if t != 0:
        r.append(S / abs(t))
    return min(r)


def failure_envelopes():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(6.8, 3.9), gridspec_kw=dict(width_ratios=[1.15, 1], wspace=0.32))
    phi = np.linspace(0, 2 * np.pi, 2001)
    # directions in normalized space so all regions are sampled
    U, V = 1500 * np.cos(phi), 246 * np.sin(phi)
    nrm = np.hypot(U, V)
    u, v = U / nrm, V / nrm
    rth = np.array([_th_radius(a, b) for a, b in zip(u, v)])
    rtw = np.array([_tw_radius(a, b) for a, b in zip(u, v)])
    ax.add_patch(Rectangle((-XC, -YC), XC + XT, YC + YT, fill=False, ec=COLORS[0], lw=1.6, label="maximum stress"))
    ax.plot(rth * u, rth * v, color=COLORS[1], lw=1.6, ls="--", label="Tsai–Hill")
    ax.plot(rtw * u, rtw * v, color=COLORS[2], lw=1.6, label="Tsai–Wu")
    ax.axhline(0, color="0.6", lw=0.6)
    ax.axvline(0, color="0.6", lw=0.6)
    ax.set_xlim(-1800, 1800)
    ax.set_ylim(-300, 100)
    ax.set_xlabel(r"$\sigma_1$ (MPa)")
    ax.set_ylabel(r"$\sigma_2$ (MPa)")
    ax.set_xticks([-1500, -750, 0, 750, 1500])
    ax.legend(loc="lower center", fontsize=7.6, bbox_to_anchor=(0.5, 0.25))
    ax.text(1450, 75, "T/T", fontsize=7.5, ha="right", color="0.35")
    ax.text(-1450, 75, "C/T", fontsize=7.5, ha="left", color="0.35")
    ax.text(1450, -290, "T/C", fontsize=7.5, ha="right", color="0.35")
    ax.text(-1450, -290, "C/C", fontsize=7.5, ha="left", color="0.35")
    ax.text(30, 46, "$Y_t$ = 40", fontsize=7.3, color=COLORS[0], va="bottom")
    ax.text(30, -252, "$Y_c$ = 246", fontsize=7.3, color=COLORS[0], va="top")
    ax.text(1510, -150, "$X_t$\n1500", fontsize=7.3, color=COLORS[0], ha="left", va="center")
    ax.text(-1510, -150, "$X_c$\n1500", fontsize=7.3, color=COLORS[0], ha="right", va="center")
    ax.set_title(r"T300/epoxy ply, $\tau_{12}=0$ (note scales)", fontsize=9)

    # right: off-axis uniaxial strength
    th = np.linspace(0.01, 90, 900)
    c, s = np.cos(np.radians(th)), np.sin(np.radians(th))
    th_s = np.array([_th_radius(cc * cc, ss * ss) if False else
                     1 / np.sqrt((cc * cc) ** 2 / XT ** 2 - cc * cc * ss * ss / XT ** 2 + (ss * ss) ** 2 / YT ** 2 + (ss * cc) ** 2 / S ** 2)
                     for cc, ss in zip(c, s)])
    ms_s = np.array([_ms_radius(cc * cc, ss * ss, -ss * cc) for cc, ss in zip(c, s)])
    tw_s = np.array([_tw_radius(cc * cc, ss * ss, -ss * cc) for cc, ss in zip(c, s)])
    t1 = np.degrees(np.arctan(S / XT))
    t2 = np.degrees(np.arctan(YT / S))
    ax2.axvspan(0, t1, color=COLORS[0], alpha=0.10, lw=0)
    ax2.axvspan(t1, t2, color=COLORS[4], alpha=0.12, lw=0)
    ax2.axvspan(t2, 90, color=COLORS[3], alpha=0.10, lw=0)
    ax2.annotate(f"fibre (< {t1:.1f}°)", xy=(t1 / 2, 22), xytext=(4.5, 22), fontsize=7.2, va="center", arrowprops=dict(arrowstyle="-", lw=0.5, color="0.4"))
    ax2.text((t1 + t2) / 2, 13, "shear", fontsize=7.5, ha="center", va="bottom")
    ax2.text((t2 + 90) / 2, 13, "transverse", fontsize=7.5, ha="center", va="bottom")
    ax2.text((t2 + 90) / 2, 1100, "max-stress mode:", fontsize=7, ha="center", color="0.35")
    ax2.plot(th, ms_s, color=COLORS[0], lw=1.6, label="maximum stress")
    ax2.plot(th, th_s, color=COLORS[1], lw=1.6, ls="--", label="Tsai–Hill")
    ax2.plot(th, tw_s, color=COLORS[2], lw=1.2, alpha=0.8, label="Tsai–Wu")
    for tt, v in ((0, 1500), (5, 690), (10, 370), (15, 245), (30, 112), (45, 69), (60, 50.5), (90, 40)):
        ax2.plot(tt, v, "o", color=COLORS[1], ms=3.2, zorder=5)
    ax2.annotate("15°: 245 MPa", xy=(15, 245), xytext=(30, 300), fontsize=7.5,
                 arrowprops=dict(arrowstyle="-", lw=0.6, color="0.4"))
    ax2.set_yscale("log")
    ax2.set_ylim(10, 2000)
    ax2.set_xlim(0, 90)
    ax2.set_xticks([0, 15, 30, 45, 60, 75, 90])
    ax2.set_xlabel(r"load angle $\theta$ (°)")
    ax2.set_ylabel("uniaxial strength (MPa)")
    ax2.legend(loc="upper right", fontsize=7.4, bbox_to_anchor=(1.0, 0.86))
    ax2.set_yticks([10, 20, 50, 100, 200, 500, 1000, 2000])
    ax2.set_yticklabels(["10", "20", "50", "100", "200", "500", "1000", "2000"])
    ax2.set_title("off-axis strength", fontsize=9)
    save(fig, "23", "fig-23-3-failure-envelopes")
    return t1, t2


# ---------------------------------------------------------------- 23.4
def progressive_failure():
    fig, ax = new_fig(6.4, 4.0)
    E0, E1d = 96.0e3, 91.0e3
    fpf_r, fpf_0, ult_strain = 76.0, 374.0, 0.0083
    e_fpf_r = fpf_r / E0
    e_fpf_0 = fpf_0 / E0
    s_ult_r = fpf_r + E1d * (ult_strain - e_fpf_r)
    s_ult_0 = fpf_0 + E1d * (ult_strain - e_fpf_0)
    e = np.array([0, e_fpf_r, ult_strain])
    sres = np.array([0, fpf_r, s_ult_r])
    ax.plot(e * 100, sres, color=COLORS[0], lw=2.0, label="with cure residual stress (ΔT = −150 K)")
    ax.plot(np.array([e_fpf_0, ult_strain]) * 100, [fpf_0, s_ult_0], color=COLORS[1], lw=1.4, ls="--",
            label="hypothetical stress-free laminate")
    ax.plot(e_fpf_r * 100, fpf_r, "o", color=COLORS[0], ms=7, zorder=5)
    ax.plot(e_fpf_0 * 100, fpf_0, "o", mfc="white", mec=COLORS[1], mew=1.6, ms=7, zorder=5)
    ax.plot(ult_strain * 100, s_ult_r, "X", color=INK, ms=9, zorder=5)
    ax.annotate("first-ply failure\n76 MPa, ε ≈ 0.08 %\n(90° plies crack)", xy=(e_fpf_r * 100, fpf_r),
                xytext=(0.07, 260), fontsize=7.8, arrowprops=dict(arrowstyle="-|>", lw=0.8, mutation_scale=8))
    ax.annotate("FPF without residual\nstress: 374 MPa, ε ≈ 0.39 %", xy=(e_fpf_0 * 100, fpf_0),
                xytext=(0.45, 200), fontsize=7.8, color=COLORS[1],
                arrowprops=dict(arrowstyle="-|>", lw=0.8, mutation_scale=8, color=COLORS[1]))
    ax.annotate("last-ply failure: 0° fibres break\n≈ 760 MPa at ε ≈ 0.83 %", xy=(ult_strain * 100, s_ult_r),
                xytext=(0.7, 470), fontsize=7.8, ha="center", va="top",
                arrowprops=dict(arrowstyle="-|>", lw=0.8, mutation_scale=8))
    ax.text(0.17, 135, "slope 96 GPa", fontsize=7.8, rotation=0, color=COLORS[0])
    ax.text(0.88, 300, "slope ≈ 91 GPa\n(90° plies discounted)", fontsize=7.8, color=COLORS[0], ha="right")
    ax.set_xlim(0, 0.9)
    ax.set_ylim(0, 850)
    ax.set_xlabel(r"laminate strain $\varepsilon_x$ (%)")
    ax.set_ylabel("average laminate stress (MPa)")
    ax.legend(loc="lower right", fontsize=7.6, bbox_to_anchor=(1.0, 0.02))
    ax.set_title("T300/epoxy [0/90]$_s$ in tension", fontsize=9.5)

    # inset: edge view with crack multiplication
    ins = fig.add_axes([0.13, 0.5, 0.36, 0.3])
    ins.set_xlim(0, 10)
    ins.set_ylim(0, 10.2)
    ins.axis("off")
    rows = [(7.0, 3, "low load"), (3.8, 7, "higher load"), (0.6, 14, "saturation")]
    for y0, ncr, lab in rows:
        ins.add_patch(Rectangle((0, y0), 7.2, 0.5, fc="#C9D9EA", ec=INK, lw=0.5))
        ins.add_patch(Rectangle((0, y0 + 0.5), 7.2, 1.0, fc="#E8CFE0", ec=INK, lw=0.5))
        ins.add_patch(Rectangle((0, y0 + 1.5), 7.2, 0.5, fc="#C9D9EA", ec=INK, lw=0.5))
        for xc in np.linspace(0, 7.2, ncr + 2)[1:-1]:
            ins.plot([xc, xc], [y0 + 0.5, y0 + 1.5], color=COLORS[1], lw=1.0)
        ins.text(7.5, y0 + 1.0, lab, fontsize=6.8, va="center")
    ins.text(0, 9.5, "edge view, 0°/90°/0°: transverse cracks multiply\nin the 90° plies up to matrix crack saturation", fontsize=6.6, va="bottom")
    save(fig, "23", "fig-23-4-progressive-failure")


# ---------------------------------------------------------------- 23.5
def free_edge_and_impact():
    fig = plt.figure(figsize=(6.8, 5.2))
    gs = fig.add_gridspec(3, 2, height_ratios=[0.75, 1.2, 1.2], width_ratios=[1, 1.2], hspace=0.55, wspace=0.18)
    axk = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[1, 0])
    ax2 = fig.add_subplot(gs[2, 0], sharex=ax1)
    axi = fig.add_subplot(gs[:, 1])

    # coupon cross-section sketch
    axk.axis("off")
    axk.set_xlim(-1.25, 1.35)
    axk.set_ylim(-0.75, 0.75)
    cols = ["#C9D9EA", "#F1D7B5", "#F1D7B5", "#C9D9EA"]
    labs = ["+45", "−45", "−45", "+45"]
    hpl = 0.18
    for i in range(4):
        y = 0.36 - (i + 1) * hpl
        axk.add_patch(Rectangle((-1, y), 2, hpl, fc=cols[i], ec=INK, lw=0.6))
        axk.text(1.04, y + hpl / 2, labs[i], fontsize=6.8, va="center")
    for sg in (1, -1):
        axk.add_patch(Rectangle((sg * 1.0 - (0.12 if sg > 0 else 0), -0.36), 0.12, 0.72, fc=COLORS[1], alpha=0.3, lw=0))
    axk.annotate("", xy=(1.0, -0.52), xytext=(0.35, -0.52), arrowprops=dict(arrowstyle="-|>", lw=0.8, mutation_scale=7))
    axk.text(1.05, -0.52, "$y$", fontsize=8, ha="left", va="center")
    axk.text(0, 0.45, "[±45]$_s$ coupon in tension (cross-section)", fontsize=7.6, ha="center", va="bottom")
    axk.text(-1.0, -0.52, "edge boundary layers ≈ h", fontsize=6.8, color=COLORS[1], va="center")

    yb = np.linspace(0, 1, 600)
    u = 1 - yb
    delta = 0.08
    txy = 1 - np.exp(-u / delta)
    txz = 0.9 * np.exp(-u / (0.45 * delta)) / np.sqrt(np.maximum(u, 0.004) / 0.004) ** 0.25
    ax1.plot(yb, txy, color=COLORS[0], label=r"in-plane $\tau_{xy}$ (ply)")
    ax1.plot(yb, txz, color=COLORS[1], label=r"interlaminar $\tau_{xz}$ (+45/−45)")
    ax1.axvspan(1 - 2.5 * delta, 1, color="0.92", lw=0, zorder=0)
    ax1.set_ylim(0, 1.25)
    ax1.set_ylabel("stress / CLT\n$\\tau_{xy}$", fontsize=8)
    ax1.legend(loc="center left", fontsize=7, bbox_to_anchor=(0.0, 0.55))
    ax1.tick_params(labelsize=7.5)
    plt.setp(ax1.get_xticklabels(), visible=False)
    ax1.text(0.97, 1.15, "singular\nat edge", fontsize=6.8, ha="right", va="top", color=COLORS[1])

    sz = np.exp(-u / delta) * (1 - u / delta)
    ax2.plot(yb, sz, color=COLORS[1], label="[±30/90]$_s$: tensile at edge")
    ax2.plot(yb, -sz, color=COLORS[2], ls="--", label="[90/±30]$_s$: compressive")
    ax2.axhline(0, color="0.6", lw=0.6)
    ax2.axvspan(1 - 2.5 * delta, 1, color="0.92", lw=0, zorder=0)
    ax2.set_ylim(-1.2, 1.3)
    ax2.set_xlim(0, 1)
    ax2.set_xlabel("$y/b$ (centre → free edge)", fontsize=8.5)
    ax2.set_ylabel(r"mid-plane $\sigma_z$" "\n(arb. units)", fontsize=8)
    ax2.legend(loc="lower left", fontsize=6.9)
    ax2.text(0.78, 0.95, "delamination-\nprone", fontsize=7, color=COLORS[1], ha="right", va="center")
    ax2.tick_params(labelsize=7.5)

    # impact cross-section
    axi.set_aspect("equal")
    axi.axis("off")
    axi.set_xlim(-34, 34)
    axi.set_ylim(-47.5, 34)
    hh = 5.0
    sc = 3.0     # vertical exaggeration
    H = hh * sc
    top = 0.0
    nint = 9
    axi.add_patch(Rectangle((-32, top - H), 64, H, fc=PLY_C, ec=INK, lw=1.0))
    for i in range(1, nint + 1):
        y = top - i * H / (nint + 1)
        axi.plot([-32, 32], [y, y], color="0.7", lw=0.4)
    # dent
    xd = np.linspace(-4, 4, 50)
    axi.fill_between(xd, top, top - 0.3 * sc * (1 - (xd / 4) ** 2), color="white", zorder=3)
    axi.plot(xd, top - 0.3 * sc * (1 - (xd / 4) ** 2), color=INK, lw=0.9, zorder=4)
    # impactor
    axi.add_patch(Circle((0, top + 6.2 - 0.3 * sc + 0.01), 6.2, fc="0.8", ec=INK, lw=0.8, zorder=2))
    axi.annotate("", xy=(0, top + 13.5), xytext=(0, top + 20), arrowprops=dict(arrowstyle="-|>", lw=1.3, mutation_scale=10))
    axi.text(1.2, top + 17.5, "impactor\n(e.g. 30 J)", fontsize=7.3, va="center")
    axi.annotate("dent ≈ 0.3 mm:\n“barely visible”", xy=(-3.5, top - 0.3), xytext=(-33, top + 15), fontsize=7.3, va="center", arrowprops=dict(arrowstyle="-|>", lw=0.7, mutation_scale=7))
    # delaminations: widening cone, alternating offsets
    rng = np.random.default_rng(5)
    prev = None
    for i in range(1, nint + 1):
        y = top - i * H / (nint + 1)
        half = 2.5 + 2.6 * i
        shift = (1.5 if i % 2 else -1.5)
        xa, xb = -half + shift, half + shift
        axi.plot([xa, xb], [y, y], color=COLORS[1], lw=2.2, solid_capstyle="butt", zorder=5)
        if prev is not None:
            # matrix cracks linking delamination tips at ~45 degrees
            for (xp, sgn) in ((prev[0], -1), (prev[1], 1)):
                axi.plot([xp, xp + sgn * (H / (nint + 1)) * 1.0], [y + H / (nint + 1), y], color=INK, lw=0.8, zorder=6)
        prev = (xa, xb)
    # back-face splitting
    xs = np.linspace(-6, 6, 9)
    yy = top - H - np.abs(rng.normal(0, 0.9, len(xs))) - 0.3
    axi.plot(xs, yy, color=INK, lw=1.0)
    axi.text(0, top - H - 3.2, "back-face fibre splitting", fontsize=7.3, ha="center", va="top")
    axi.text(0, top - H - 7.6, "4–6 mm thick (thickness exaggerated ×3)", fontsize=6.8, ha="center", va="top", color="0.35")
    axi.annotate("delaminations widen\ntoward the back face", xy=(-18, top - 8 * H / 10), xytext=(-33, top + 5.5),
                 fontsize=7.3, arrowprops=dict(arrowstyle="-|>", lw=0.7, mutation_scale=7, color=COLORS[1]), color=COLORS[1])
    axi.annotate("matrix cracks\nlink them", xy=(9.5, top - 2.5 * H / 10), xytext=(13, top + 6), fontsize=7.3,
                 arrowprops=dict(arrowstyle="-|>", lw=0.7, mutation_scale=7))
    axi.text(0, top + 28, "low-velocity impact on a\nquasi-isotropic laminate", ha="center", fontsize=8.5, va="center")

    # C-scan inset (plan view)
    cy = -37.5
    axi.add_patch(Rectangle((-22, cy - 9), 44, 18, fc="#F7F7F7", ec="0.5", lw=0.6))
    for i, (ang, sz_) in enumerate(((90, 7), (45, 9), (0, 11), (-45, 13), (90, 15), (45, 16.5), (0, 18))):
        e = Ellipse((0, cy), sz_ * 1.0 * 1.0, sz_ * 0.36, angle=ang, fc=COLORS[1], alpha=0.12, ec=COLORS[1], lw=0.6)
        axi.add_patch(e)
    axi.add_patch(Circle((0, cy), 1.2, fc=INK, ec="none"))
    axi.annotate("", xy=(-15, cy - 7.5), xytext=(15, cy - 7.5), arrowprops=dict(arrowstyle="<|-|>", lw=0.7, mutation_scale=6))
    axi.text(0, cy - 7.0, "≈ 25–40 mm", fontsize=6.8, ha="center", va="bottom")
    axi.text(-21.5, cy + 8.3, "C-scan (plan view)", fontsize=7, va="top")
    axi.text(14, cy + 4, "dent", fontsize=6.8)
    axi.plot([1.3, 13.6], [cy + 0.3, cy + 4.3], color="0.4", lw=0.5)
    save(fig, "23", "fig-23-5-free-edge-and-impact")


# ---------------------------------------------------------------- 23.6
def sandwich_failure_modes():
    fig = plt.figure(figsize=(6.8, 5.6))
    gs = fig.add_gridspec(2, 1, height_ratios=[1.0, 1.15], hspace=0.08)
    axb = fig.add_subplot(gs[0])
    axbar = fig.add_axes([0.86, 0.62, 0.12, 0.25])
    gbot = gs[1].subgridspec(2, 3, hspace=0.5, wspace=0.12)

    # beam (thickness not to scale) with through-thickness stress profiles --------
    axb.set_aspect("equal")
    axb.axis("off")
    Lb, tf, c = 9.0, 0.3, 2.3
    H = 2 * tf + c
    axb.set_xlim(-0.3, 17.6)
    axb.set_ylim(-1.5, 4.85)
    axb.add_patch(Rectangle((0, 0), Lb, tf, fc="#5F6B7A", ec=INK, lw=0.8))
    axb.add_patch(Rectangle((0, tf + c), Lb, tf, fc="#5F6B7A", ec=INK, lw=0.8))
    axb.add_patch(Rectangle((0, tf), Lb, c, fc="#F6E7B0", ec=INK, lw=0.8))
    for x in np.arange(0.2, Lb, 0.4):
        axb.plot([x, x], [tf, tf + c], color="#B8A266", lw=0.5)
    for xs in (0.5, Lb - 0.5):
        axb.add_patch(Polygon([[xs, 0], [xs - 0.3, -0.5], [xs + 0.3, -0.5]], closed=True, fc="0.75", ec=INK, lw=0.8))
    axb.annotate("", xy=(Lb / 2, H + 0.02), xytext=(Lb / 2, H + 0.95),
                 arrowprops=dict(arrowstyle="-|>", lw=1.6, mutation_scale=12))
    axb.text(Lb / 2 + 0.15, H + 0.75, "$P$", fontsize=11)
    axb.annotate("", xy=(0.5, -0.8), xytext=(Lb - 0.5, -0.8), arrowprops=dict(arrowstyle="<|-|>", lw=0.8, mutation_scale=7))
    axb.text(Lb / 2, -1.2, "span $L$", fontsize=8.5, ha="center")
    axb.text(Lb / 2 + 0.7, H + 0.1, "CFRP faces $t_f$ = 1 mm", fontsize=7.6, va="bottom")
    axb.text(Lb / 2, tf + c / 2, "honeycomb core $c$ = 20 mm", fontsize=7.8, ha="center", va="center",
             bbox=dict(fc="#F6E7B0", ec="none", pad=0.6))
    axb.text(Lb / 2, 4.5, r"$D\approx E_f t_f d^2/2$,   $S\approx G_c d^2/c$   ($d=c+t_f$)", fontsize=8.5, ha="center")

    zz = np.linspace(0, H, 400)
    zm = H / 2
    infc = (zz >= tf) & (zz <= tf + c)
    sig = np.where(infc, 0.4 / 70.0, 1.0) * (zm - zz) / zm
    sig /= np.max(np.abs(sig))
    tau = np.where(zz < tf, zz / tf, np.where(zz > tf + c, (H - zz) / tf, 1.0)) * 0.92
    tau = np.where(infc, 0.92 + 0.06 * (1 - ((zz - zm) / (c / 2)) ** 2), tau)
    for x0, prof, col, lab in ((10.9, sig, COLORS[0], "bending\nstress σ"),
                               (12.9, tau, COLORS[1], "shear\nstress τ")):
        axb.plot([x0, x0], [-0.05, H + 0.05], color="0.4", lw=0.8)
        for zline in (tf, tf + c):
            axb.plot([x0 - 0.9, x0 + 0.9], [zline, zline], color="0.85", lw=0.5)
        axb.fill_betweenx(zz, x0, x0 + 0.8 * prof, color=col, alpha=0.35, lw=0)
        axb.plot(x0 + 0.8 * prof, zz, color=col, lw=1.4)
        axb.text(x0, -0.3, lab, fontsize=7.2, ha="center", va="top", color=col)
    axb.text(10.9 + 0.88, tf / 2, "T", fontsize=7, va="center", color=COLORS[0])
    axb.text(10.9 - 1.0, H - tf / 2, "C", fontsize=7, va="center", color=COLORS[0])

    # equal-mass stiffness bar inset ----------------------------------------------
    D_sand, D_solid = 1.54e7, 1.06e5
    axbar.bar([0, 1], [D_sand, D_solid], color=[COLORS[2], "0.6"], width=0.6)
    axbar.set_yscale("log")
    axbar.set_ylim(1e4, 1e8)
    axbar.set_xticks([0, 1])
    axbar.set_xticklabels(["sand-\nwich", "solid\n2.63 mm"], fontsize=7)
    axbar.tick_params(axis="y", labelsize=7)
    axbar.set_ylabel("bending stiffness D\n(N mm per mm)", fontsize=7.2)
    axbar.text(0, D_sand * 1.5, "146×", ha="center", fontsize=8.5, fontweight="bold", color=COLORS[2])
    axbar.set_title("equal mass\n4.2 kg/m²", fontsize=7.6)

    # failure-mode sketches -----------------------------------------------------
    titles = ["face fracture (tension face)", "face wrinkling", "intracell dimpling",
              "core shear failure", "core indentation", "face–core debond"]
    for i in range(6):
        a_ = fig.add_subplot(gbot[i // 3, i % 3])
        a_.set_aspect("equal")
        a_.axis("off")
        a_.set_xlim(-0.2, 6.2)
        a_.set_ylim(-0.75, 2.3)
        a_.set_title(f"({chr(97 + i)}) {titles[i]}", fontsize=7.8, pad=2)
        ft, cc = 0.18, 1.3
        top_y = ft + cc
        x = np.linspace(0, 6, 400)
        bottom_face = np.zeros_like(x)
        top_face = np.zeros_like(x) + top_y
        if i == 1:
            top_face = top_y - 0.12 * np.maximum(0, np.sin(2 * np.pi * (x - 1.5) / 0.6)) * ((x > 1.5) & (x < 4.5))
            top_face += 0.1 * np.minimum(0, np.sin(2 * np.pi * (x - 1.5) / 0.6)) * ((x > 1.5) & (x < 4.5)) * 1.0
        if i == 2:
            cell = 0.5
            dip = 0.09 * np.abs(np.sin(np.pi * x / cell)) * ((x > 1.5) & (x < 4.5))
            top_face = top_face - dip
        if i == 4:
            top_face = top_y - 0.35 * np.exp(-((x - 3) / 0.5) ** 2)
        # core
        core = Polygon(np.concatenate([np.column_stack([x, bottom_face + ft]), np.column_stack([x[::-1], top_face[::-1]])]),
                       closed=True, fc="#F6E7B0", ec="none")
        a_.add_patch(core)
        for xc in np.arange(0.25, 6, 0.5):
            j = np.argmin(abs(x - xc))
            yt = top_face[j]
            if i == 4 and abs(xc - 3) < 0.8:
                # crushed walls
                a_.plot([xc, xc + 0.08, xc - 0.06, xc], [ft, ft + 0.45, ft + 0.7, yt], color="#B8A266", lw=0.6)
            else:
                a_.plot([xc, xc], [ft, yt], color="#B8A266", lw=0.6)
        # faces
        a_.fill_between(x, bottom_face, bottom_face + ft, color="#5F6B7A", lw=0)
        if i == 5:
            # debond: gap between top face and core in the middle
            gap = 0.16 * np.exp(-((x - 3) / 1.0) ** 2) * (np.abs(x - 3) < 1.6)
            a_.fill_between(x, top_face + gap, top_face + gap + ft, color="#5F6B7A", lw=0)
            a_.fill_between(x, top_face, top_face + gap, color="white", lw=0)
            a_.annotate("debond", xy=(3, top_y + 0.08), xytext=(4.4, 2.05), fontsize=6.8,
                        arrowprops=dict(arrowstyle="-", lw=0.5, color="0.35"))
        else:
            a_.fill_between(x, top_face, top_face + ft, color="#5F6B7A", lw=0)
        if i == 0:
            a_.add_patch(Rectangle((2.93, -0.01), 0.14, ft + 0.02, fc="white", ec="none"))
            a_.plot([2.93, 2.98, 2.95, 3.0], [0, 0.06, 0.12, ft], color=COLORS[1], lw=1.2)
            for sg in (1, -1):
                a_.annotate("", xy=(3 + sg * 2.0, -0.35), xytext=(3 + sg * 0.6, -0.35),
                            arrowprops=dict(arrowstyle="-|>", lw=0.8, mutation_scale=6, color=COLORS[0]))
            a_.text(3, -0.45, "tension", fontsize=6.6, ha="center", va="top", color=COLORS[0])
        if i in (1, 2):
            for sg in (1, -1):
                a_.annotate("", xy=(3 + sg * 1.15, top_y + ft + 0.35), xytext=(3 + sg * 2.7, top_y + ft + 0.35),
                            arrowprops=dict(arrowstyle="-|>", lw=0.8, mutation_scale=6, color=COLORS[0]))
            a_.text(3, top_y + ft + 0.35, "compression", fontsize=6.6, ha="center", va="center", color=COLORS[0])
        if i == 3:
            for x0 in (1.3, 2.3, 3.3, 4.3):
                a_.plot([x0, x0 + 0.7], [ft + 0.15, top_y - 0.15], color=COLORS[1], lw=1.2)
            for sg, yy in ((1, -0.35), (-1, top_y + ft + 0.3)):
                a_.annotate("", xy=(3 + sg * 1.8, yy), xytext=(3 - sg * 1.8, yy),
                            arrowprops=dict(arrowstyle="-|>", lw=0.8, mutation_scale=6, color=COLORS[3]))
            a_.text(3, -0.45, "45° cracks in core", fontsize=6.6, ha="center", va="top", color=COLORS[1])
        if i == 4:
            a_.annotate("", xy=(3, top_y + ft - 0.33), xytext=(3, top_y + ft + 0.55),
                        arrowprops=dict(arrowstyle="-|>", lw=1.2, mutation_scale=8))
            a_.text(3.15, top_y + ft + 0.4, "local load", fontsize=6.6, va="center")
    save(fig, "23", "fig-23-6-sandwich-failure-modes")


if __name__ == "__main__":
    laminate_geometry()
    R = laminate_coupling()
    print(f"  [0/90]_T curvature radius: {R:.1f} mm")
    t1, t2 = failure_envelopes()
    print(f"  max-stress mode boundaries: fibre/shear {t1:.1f} deg, shear/transverse {t2:.1f} deg")
    progressive_failure()
    free_edge_and_impact()
    sandwich_failure_modes()
