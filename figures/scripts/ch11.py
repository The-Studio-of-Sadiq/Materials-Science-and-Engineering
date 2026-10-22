"""Figures for Chapter 11 — Elasticity and Mechanical Testing.

Run from the repository root:  python figures/scripts/ch11.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle, Arc, Wedge
from matplotlib.lines import Line2D

BLUE, VERM, GREEN, PINK, ORANGE, SKY = COLORS[:6]
GREY = "#A7AEB6"


def _arr(ax, p0, p1, color=INK, lw=1.0, ms=9, style="-|>", **kw):
    ax.annotate("", xy=p1, xytext=p0, arrowprops=dict(arrowstyle=style, color=color, lw=lw,
                mutation_scale=ms, shrinkA=0, shrinkB=0, **kw))


# ---------------------------------------------------------------- Figure 11.1
def _iso(p):
    """Isometric-style projection; x towards lower left, y to the right, z up."""
    p = np.asarray(p, float)
    x, y, z = p[..., 0], p[..., 1], p[..., 2]
    c30 = np.cos(np.radians(30))
    return np.stack([(y - x) * c30, z - 0.5 * (x + y)], axis=-1)


def stress_tensor_mohr():
    fig = plt.figure(figsize=(6.8, 3.6))
    ax = fig.add_axes([0.0, 0.0, 0.46, 1.0])
    ax.set_aspect("equal"); ax.axis("off")
    # unit cube [0,1]^3, visible faces x=1, y=1, z=1
    faces = {"x": [(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 0, 1)],
             "y": [(0, 1, 0), (1, 1, 0), (1, 1, 1), (0, 1, 1)],
             "z": [(0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)]}
    shade = {"x": "#DCE8F3", "y": "#EAF1F8", "z": "#F5F8FB"}
    for k, f in faces.items():
        ax.add_patch(Polygon(_iso(np.array(f)), closed=True, fc=shade[k], ec=INK, lw=1.0))
    L = 0.42
    cols = {"n": VERM, "s": BLUE}
    # each visible face: centre, normal direction, two in-plane directions
    specs = [("x", (1, 0.5, 0.5), 0, [1, 2]), ("y", (0.5, 1, 0.5), 1, [0, 2]), ("z", (0.5, 0.5, 1), 2, [0, 1])]
    names = "xyz"
    for face, c, ni, sh in specs:
        c = np.array(c, float)
        e = np.eye(3)
        P0 = _iso(c)
        P1 = _iso(c + L * e[ni])
        _arr(ax, P0, P1, color=VERM, lw=1.4, ms=10)
        d = P1 - P0
        ax.text(*(P1 + 0.18 * d / np.linalg.norm(d)), rf"$\sigma_{{{names[ni]}{names[ni]}}}$", color=VERM,
                fontsize=10, ha="center", va="center")
        offs = {("x", 1): (0.0, -0.13), ("y", 0): (0.0, -0.13), ("x", 2): (-0.14, 0.0), ("y", 2): (0.14, 0.0),
                ("z", 0): (-0.06, 0.12), ("z", 1): (0.06, 0.12)}
        for j in sh:
            Q1 = _iso(c + 0.27 * e[j])
            _arr(ax, P0, Q1, color=BLUE, lw=1.1, ms=8)
            ax.text(*(Q1 + np.array(offs[(face, j)])),
                    rf"$\tau_{{{names[ni]}{names[j]}}}$", color=BLUE, fontsize=9.5, ha="center", va="center")
    # axes triad (from back-bottom corner region, offset)
    o = np.array([-1.25, -1.2])
    for v, lab in [((1, 0, 0), "x"), ((0, 1, 0), "y"), ((0, 0, 1), "z")]:
        d = _iso(np.array(v) * 0.35)
        _arr(ax, o, o + d, lw=0.9, ms=7)
        ax.text(*(o + d * 1.3), lab, fontsize=9, ha="center", va="center")
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.5, 1.75)
    ax.text(-1.55, 1.65, "(a) stress components on a cubic element", fontsize=9.5, va="top")

    # (b) Mohr circle
    bx = fig.add_axes([0.56, 0.16, 0.42, 0.72])
    sxx, syy, txy = 120.0, 20.0, 40.0
    C = (sxx + syy) / 2
    R = np.hypot((sxx - syy) / 2, txy)
    s1, s2 = C + R, C - R
    th = np.linspace(0, 2 * np.pi, 400)
    bx.plot(C + R * np.cos(th), R * np.sin(th), color=INK, lw=1.5)
    bx.axhline(0, color=INK, lw=0.7)
    bx.axvline(0, color=INK, lw=0.7)
    # stress points: X = (sxx, -txy) and Y = (syy, +txy) (shear plotted positive downward convention avoided:
    # plot X at (sxx, txy), Y at (syy, -txy))
    X, Y = (sxx, txy), (syy, -txy)
    bx.plot([X[0], Y[0]], [X[1], Y[1]], color=GREY, lw=1.0)
    bx.plot(*X, "o", color=BLUE, ms=5); bx.plot(*Y, "o", color=BLUE, ms=5)
    bx.text(X[0] + 4, X[1] + 4, "x face\n(120, 40)", fontsize=7.5, color=BLUE, va="bottom")
    bx.text(Y[0] - 4, Y[1] - 4, "y face\n(20, −40)", fontsize=7.5, color=BLUE, ha="right", va="top")
    bx.plot([s1, s2], [0, 0], "s", color=VERM, ms=5)
    bx.text(s1 - 3, 4, f"σ₁ = {s1:.0f}", fontsize=8.5, color=VERM, ha="right", va="bottom")
    bx.text(s2 + 3, 4, f"σ₂ = {s2:.0f}", fontsize=8.5, color=VERM, ha="left", va="bottom")
    bx.plot(C, 0, "+", color=INK, ms=7)
    bx.text(C, -7, f"C = {C:.0f}", fontsize=8, ha="center", va="top")
    bx.plot([C, C], [0, R], color=GREEN, lw=1.0, ls="--")
    bx.plot(C, R, "o", color=GREEN, ms=4.5)
    bx.text(C + 3, R + 3, f"τmax = R = {R:.0f}", fontsize=8.5, color=GREEN, va="bottom")
    ang = np.degrees(np.arctan2(txy, (sxx - syy) / 2))
    bx.add_patch(Arc((C, 0), 44, 44, theta1=0, theta2=ang, color=PINK, lw=1.3))
    bx.text(C + 22, -5, f"2θp = {ang:.1f}°", fontsize=8, color=PINK, ha="left", va="top")
    bx.set_xlim(-50, 150)
    bx.set_ylim(-75, 80)
    bx.set_aspect("equal")
    bx.set_xlabel("normal stress σ (MPa)")
    bx.set_ylabel("shear stress τ (MPa)")
    bx.set_title("(b) Mohr circle: σxx = 120, σyy = 20, τxy = 40 MPa", fontsize=9, loc="left")
    print(f"  Mohr: C={C}, R={R:.2f}, s1={s1:.1f}, s2={s2:.1f}, 2thp={ang:.2f}")
    save(fig, "11", "fig-11-1-stress-tensor-mohr")


# ---------------------------------------------------------------- Figure 11.2
CUBIC = {  # C11, C12, C44 (GPa)
    "Cu": (168.4, 121.4, 75.4),
    "Fe": (231.4, 134.7, 116.4),
    "Al": (108.2, 61.3, 28.5),
    "W": (522.4, 204.4, 160.6),
}


def _compliance(C11, C12, C44):
    d = (C11 - C12) * (C11 + 2 * C12)
    return (C11 + C12) / d, -C12 / d, 1 / C44


def _E_dir(n, S11, S12, S44):
    l1, l2, l3 = n
    J = l1 ** 2 * l2 ** 2 + l2 ** 2 * l3 ** 2 + l3 ** 2 * l1 ** 2
    return 1 / (S11 - 2 * (S11 - S12 - 0.5 * S44) * J)


def _hill_E(C11, C12, C44):
    S11, S12, S44 = _compliance(C11, C12, C44)
    K = (C11 + 2 * C12) / 3
    GV = (C11 - C12 + 3 * C44) / 5
    GR = 5 / (4 * (S11 - S12) + 3 * S44)
    G = (GV + GR) / 2
    return 9 * K * G / (3 * K + G)


def directional_modulus():
    fig = plt.figure(figsize=(6.6, 4.4))
    ax = fig.add_axes([0.02, 0.0, 0.70, 0.98], projection="polar")
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_thetamin(0); ax.set_thetamax(180)
    th = np.linspace(0, np.pi, 721)
    n = np.stack([np.sin(th) / np.sqrt(2), np.sin(th) / np.sqrt(2), np.cos(th)], axis=1)
    col = {"Cu": VERM, "Fe": BLUE, "Al": GREEN, "W": PINK}
    for m, (C11, C12, C44) in CUBIC.items():
        S = _compliance(C11, C12, C44)
        E = _E_dir(n.T, *S)
        ax.plot(th, E, color=col[m], lw=1.8, label=m)
        e100 = _E_dir((0, 0, 1), *S); e111 = _E_dir(np.ones(3) / np.sqrt(3), *S)
        e110 = _E_dir((1 / np.sqrt(2), 1 / np.sqrt(2), 0), *S)
        print(f"  {m}: E100={e100:.1f} E111={e111:.1f} E110={e110:.1f} Hill={_hill_E(C11, C12, C44):.0f} "
              f"A={2 * C44 / (C11 - C12):.2f}")
    for m in ("Cu", "Fe"):
        EH = _hill_E(*CUBIC[m])
        ax.plot(th, np.full_like(th, EH), color=col[m], lw=1.0, ls="--")
    for ang, lab in [(0, "[001]"), (np.degrees(np.arccos(1 / np.sqrt(3))), "[111]"), (90, "[110]"),
                     (180 - np.degrees(np.arccos(1 / np.sqrt(3))), "[11̄1̄] → [111̄]"), (180, "[001̄]")]:
        a = np.radians(ang)
        ax.plot([a, a], [0, 450], color="0.55", lw=0.7, ls=":")
    for ang, lab in [(0, "[001]  0°"), (54.74, "[111]  54.7°"), (90, "[110]  90°"),
                     (125.26, r"$[11\bar{1}]$"), (180, r"$[00\bar{1}]$")]:
        ax.text(np.radians(ang), 490, lab, fontsize=8.5, ha="center", va="center")
    ax.set_rlim(0, 450)
    ax.set_rticks([100, 200, 300, 400])
    ax.set_rlabel_position(170)
    ax.tick_params(axis="y", labelsize=8)
    ax.set_xticks(np.radians([0, 30, 60, 90, 120, 150, 180]))
    ax.set_xticklabels([])
    ax.grid(color="#E4E4E4", lw=0.6)
    ax.text(np.radians(172), 300, "E (GPa)", fontsize=8.5, ha="left", va="center", rotation=0)
    h = [Line2D([], [], color=col[m], lw=1.8) for m in CUBIC]
    lab = ["Cu (A = 3.2)", "Fe (A = 2.4)", "Al (A = 1.2)", "W (A = 1.0)"]
    h += [Line2D([], [], color=VERM, lw=1.0, ls="--"), Line2D([], [], color=BLUE, lw=1.0, ls="--")]
    lab += ["Cu polycrystal (Hill) 127 GPa", "Fe polycrystal (Hill) 211 GPa"]
    fig.legend(h, lab, loc="center left", bbox_to_anchor=(0.62, 0.55), fontsize=8.5, title="single crystals",
               title_fontsize=8.5)
    fig.text(0.63, 0.20, "directions in the (11̄0) plane;\nangle measured from [001]", fontsize=8,
             color="0.3")
    save(fig, "11", "fig-11-2-directional-modulus")


# ---------------------------------------------------------------- Figure 11.3
def modulus_by_class():
    groups = [
        ("Elastomers", PINK, [("natural rubber", 0.001, 0.005), ("silicone", 0.001, 0.01)]),
        ("Foams", ORANGE, [("PU foam", 0.001, 0.1)]),
        ("Polymers", BLUE, [("HDPE", 0.8, 1.2), ("PMMA", 2.4, 3.3), ("epoxy", 2.5, 3.5), ("PEEK", 3.6, 4.0)]),
        ("Natural", GREEN, [("wood ⊥ grain", 0.5, 0.8), ("wood ∥ grain", 10, 13), ("cortical bone", 15, 20)]),
        ("Concrete, glass", "#8C6D46", [("concrete", 25, 40), ("silica glass", 70, 74)]),
        ("Metals", "#555555", [("Mg", 45, 45), ("Al", 70, 70), ("Ti", 115, 115), ("Cu", 125, 125),
                               ("steel", 205, 205), ("W", 411, 411)]),
        ("Ceramics", VERM, [("Si₃N₄", 310, 310), ("Al₂O₃", 380, 380), ("SiC", 420, 420), ("WC", 600, 600)]),
        ("Composites", SKY, [("GFRP", 20, 45), ("CFRP (UD, axial)", 130, 180)]),
        ("Diamond", INK, [("diamond", 1050, 1050)]),
    ]
    fig, ax = new_fig(6.8, 5.0)
    y = 0
    yt, yl = [], []
    gpos = []
    for gname, c, items in groups:
        y0 = y
        for name, lo, hi in items:
            if hi / lo > 1.02:
                ax.plot([lo, hi], [y, y], color=c, lw=6, solid_capstyle="butt")
            else:
                ax.plot([lo], [y], marker="D", color=c, ms=6)
            yt.append(y); yl.append(name)
            y -= 1
        gpos.append((gname, c, y0, y + 1))
        y -= 0.6
    ax.set_xscale("log")
    ax.set_xlim(1e-4, 2e3)
    ax.set_ylim(y + 0.3, 4.3)
    ax.set_yticks(yt)
    ax.set_yticklabels(yl, fontsize=7.8)
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    for gname, c, ya, yb in gpos:
        los = [lo for gn, cc, it in groups if gn == gname for _, lo, _ in it]
        his = [hi for gn, cc, it in groups if gn == gname for _, _, hi in it]
        if max(his) < 15:
            ax.text(max(his) * 1.8, (ya + yb) / 2, gname, color=c, fontsize=8.5, weight="bold", va="center",
                    ha="left")
        else:
            ax.text(min(los) / 1.8, (ya + yb) / 2, gname, color=c, fontsize=8.5, weight="bold", va="center",
                    ha="right")
    ax.set_xlabel("Young's modulus E (GPa)")
    ax.grid(axis="x", color="#EEEEEE", lw=0.6)
    ax.set_axisbelow(True)
    # bond-type brackets along the top
    brackets = [("entropic", 1e-3, 1e-2, 3.4, PINK), ("van der Waals / H-bond", 0.5, 13, 3.4, BLUE),
                ("metallic", 45, 411, 3.4, "#555555"), ("ionic–covalent", 30, 600, 2.05, VERM),
                ("covalent", 200, 1050, 0.7, INK)]
    for lab, a, b, yy, c in brackets:
        ax.plot([a, b], [yy, yy], color=c, lw=1.2)
        ax.plot([a, a], [yy, yy - 0.25], color=c, lw=1.2)
        ax.plot([b, b], [yy, yy - 0.25], color=c, lw=1.2)
        if lab in ("ionic–covalent", "covalent"):
            ax.text(a / 1.15, yy, lab, color=c, fontsize=8, ha="right", va="center")
        else:
            ax.text(np.sqrt(a * b), yy + 0.12, lab, color=c, fontsize=8, ha="center", va="bottom")
    save(fig, "11", "fig-11-3-modulus-by-class")


# ---------------------------------------------------------------- Figure 11.4
def tensile_true_engineering():
    E = 205e3
    K, n = 1050.0, 0.20
    sy = 412.0
    A0 = np.pi * 12.5 ** 2 / 4
    # engineering curve up to UTS from the Hollomon law with a yield plateau at 412 MPa
    e = np.linspace(0, 0.221, 2000)
    eT = np.log1p(e)
    hol = K * np.clip(eT, 1e-9, None) ** n / (1 + e)
    flow = np.maximum(sy, hol)
    p = 18
    s_up = (np.maximum(E * e, 1e-9) ** -p + flow ** -p) ** (-1 / p)
    s_up[0] = 0
    uts = K * n ** n / np.exp(n)
    print(f"  UTS from Hollomon = {uts:.0f} MPa at e = {np.exp(n) - 1:.3f}; fracture eng stress = {60000 / A0:.0f}")
    e2 = np.linspace(0.221, 0.30, 200)
    s2 = uts - (uts - 60000 / A0) * ((e2 - 0.221) / 0.079) ** 1.8
    fig, ax = new_fig(6.6, 4.6)
    ax.plot(np.r_[e, e2], np.r_[s_up, s2], color=BLUE, label="engineering σ vs e")
    ax.plot(0.30, 60000 / A0, "x", color=BLUE, ms=8, mew=2)
    # true curve
    eTs = np.linspace(0, 0.20, 1500)
    sT = (np.maximum(E * eTs, 1e-9) ** -p + np.maximum(sy, K * np.clip(eTs, 1e-9, None) ** n) ** -p) ** (-1 / p)
    sT[0] = 0
    ax.plot(eTs, sT, color=VERM, label="true σ_T vs ε_T  (σ_T = 1050 ε_T^0.20)")
    eTd = np.linspace(0.20, 0.795, 200)
    sTd = K * eTd ** n + (1083 - K * 0.795 ** n) * ((eTd - 0.2) / 0.595) ** 2
    ax.plot(eTd, sTd, color=VERM, ls="--")
    ax.plot(0.795, 1083, "x", color=VERM, ms=9, mew=2)
    ax.annotate("true fracture stress\n(uncorrected) 1083 MPa", xy=(0.795, 1083), xytext=(0.50, 1150),
                fontsize=8, color=VERM, ha="center", va="center",
                arrowprops=dict(arrowstyle="-", color=VERM, lw=0.7))
    # Considère
    eC = np.linspace(0.13, 0.42, 200)
    ax.plot(eC, n * K * eC ** (n - 1), color=GREEN, lw=1.3, ls="-.", label="dσ_T/dε_T")
    sN = K * n ** n
    ax.plot(n, sN, "o", color=GREEN, ms=6, zorder=5)
    ax.annotate(f"necking (Considère):\nε_T = n = 0.20, σ_T = {sN:.0f} MPa", xy=(n, sN), xytext=(0.33, 1010),
                fontsize=8, color="#006B4E", arrowprops=dict(arrowstyle="-", color=GREEN, lw=0.7))
    ax.plot(0.221, uts, "o", color=BLUE, ms=5)
    ax.annotate(f"UTS {uts:.0f} MPa at e = 0.221\n(end of uniform elongation)", xy=(0.221, uts),
                xytext=(0.36, 560), fontsize=8, color=BLUE, arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.7))
    ax.annotate("fracture, e = 0.30\n490 MPa", xy=(0.30, 60000 / A0), xytext=(0.31, 250), fontsize=8, color=BLUE,
                arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.7))
    ax.axvspan(0.221, 0.30, color=BLUE, alpha=0.06, lw=0)
    ax.text(0.26, 120, "necking", fontsize=8, color=BLUE, ha="center", rotation=90)
    ax.set_xlim(0, 0.8)
    ax.set_ylim(0, 1200)
    ax.set_xlabel("strain (engineering e, or true ε_T)")
    ax.set_ylabel("stress (MPa)")
    ax.text(0.12, 540, "engineering", color=BLUE, fontsize=8.5, ha="left", va="top")
    ax.annotate(r"true: $\sigma_T = 1050\,\varepsilon_T^{0.20}$", xy=(0.18, 744), xytext=(0.31, 700),
                fontsize=8.5, color=VERM, va="center", arrowprops=dict(arrowstyle="-", color=VERM, lw=0.7))
    ax.text(0.43, 425, r"$d\sigma_T/d\varepsilon_T$", color="#006B4E", fontsize=9, ha="left", va="center")
    # inset: 0.2 % offset
    ins = ax.inset_axes([0.65, 0.13, 0.33, 0.24])
    ei = np.linspace(0, 0.01, 400)
    si = (np.maximum(E * ei, 1e-9) ** -p + np.maximum(sy, K * np.log1p(ei).clip(1e-9) ** n / (1 + ei)) ** -p) ** (-1 / p)
    ins.plot(ei * 100, si, color=BLUE, lw=1.4)
    ins.plot(np.array([0.002, 0.0045]) * 100, E * (np.array([0.002, 0.0045]) - 0.002), color=GREY, lw=1.0, ls="--")
    ins.plot(0.4, 412, "o", color=INK, ms=3.5)
    ins.text(0.48, 330, "R$_{p0.2}$ = 412 MPa", fontsize=7.2)
    ins.annotate("", xy=(0.0, 60), xytext=(0.2, 60),
                 arrowprops=dict(arrowstyle="<|-|>", lw=0.6, mutation_scale=6))
    ins.text(0.1, 80, "0.2 %", fontsize=6.8, ha="center")
    ins.set_xlim(0, 1.0); ins.set_ylim(0, 500)
    ins.set_xlabel("e (%)", fontsize=7, labelpad=1)
    ins.set_ylabel("σ (MPa)", fontsize=7, labelpad=1)
    ins.tick_params(labelsize=6.5)
    ins.set_facecolor("white")
    save(fig, "11", "fig-11-4-tensile-true-engineering")


# ---------------------------------------------------------------- Figure 11.5
def indentation():
    fig = plt.figure(figsize=(6.8, 3.9))
    a = fig.add_axes([0.0, 0.0, 0.42, 1.0])
    a.set_xlim(0, 4.2); a.set_ylim(0, 4.4); a.set_aspect("equal"); a.axis("off")
    # Brinell (side view)
    cx, sy = 1.0, 3.0
    a.add_patch(Rectangle((0.05, sy - 0.75), 1.9, 0.75, fc="#E6E2DA", ec="none"))
    R = 0.55
    dep = 0.18
    hw = np.sqrt(R ** 2 - (R - dep) ** 2)
    a.plot([0.05, cx - hw], [sy, sy], color=INK, lw=1.0)
    a.plot([cx + hw, 1.95], [sy, sy], color=INK, lw=1.0)
    a.add_patch(Circle((cx, sy - dep + R), R, fc="#C9D3DD", ec=INK, lw=1.0, zorder=3))
    _arr(a, (cx - R, sy - dep + R + 0.0), (cx + R, sy - dep + R), lw=0.7, ms=6, style="<|-|>")
    a.text(cx, sy - dep + R + 0.06, "D", ha="center", va="bottom", fontsize=9)
    _arr(a, (cx - hw, sy - 0.35), (cx + hw, sy - 0.35), lw=0.7, ms=6, style="<|-|>")
    a.text(cx, sy - 0.62, "d", ha="center", fontsize=9)
    a.text(1.0, 4.35, "Brinell ball (side)", ha="center", va="top", fontsize=8.5)
    # Vickers plan view
    vx, vy = 3.15, 3.0
    s = 0.6
    a.add_patch(Polygon([(vx, vy + s), (vx + s, vy), (vx, vy - s), (vx - s, vy)], fc="#DCE8F3", ec=INK, lw=1.0))
    a.plot([vx, vx], [vy - s, vy + s], color=INK, lw=0.6)
    a.plot([vx - s, vx + s], [vy, vy], color=INK, lw=0.6)
    _arr(a, (vx - s, vy - s - 0.15), (vx + s, vy - s - 0.15), lw=0.7, ms=6, style="<|-|>")
    a.text(vx, vy - s - 0.42, "d₁", ha="center", fontsize=9)
    _arr(a, (vx + s + 0.15, vy - s), (vx + s + 0.15, vy + s), lw=0.7, ms=6, style="<|-|>")
    a.text(vx + s + 0.22, vy, "d₂", ha="left", va="center", fontsize=9)
    a.text(vx, 4.35, "Vickers (plan)", ha="center", va="top", fontsize=8.5)
    # Vickers side profile with 136°
    px, py = 2.95, 1.25
    hh = 0.32
    half = hh * np.tan(np.radians(68))
    a.add_patch(Polygon([(px - half, py + hh + 0.25), (px + half, py + hh + 0.25), (px + half, py + hh),
                         (px, py), (px - half, py + hh)], fc="#C9D3DD", ec=INK, lw=1.0))
    a.add_patch(Arc((px, py), 0.55, 0.55, theta1=22, theta2=158, color=VERM, lw=1.0))
    a.text(px, py + 0.33, "136°", ha="center", fontsize=8, color=VERM)
    a.text(px, py - 0.12, "Vickers pyramid (side)", ha="center", va="top", fontsize=8.5)
    # Berkovich plan view
    bx_, by_ = 1.0, 1.15
    r = 0.62
    pts = [(bx_ + r * np.cos(np.radians(t)), by_ + r * np.sin(np.radians(t))) for t in (90, 210, 330)]
    a.add_patch(Polygon(pts, fc="#E2F3EC", ec=INK, lw=1.0))
    for p in pts:
        a.plot([bx_, p[0]], [by_, p[1]], color=INK, lw=0.6)
    a.text(bx_, by_ - 0.55, "Berkovich (plan)\n3-sided pyramid", ha="center", va="top", fontsize=8.5)

    # P-h curve
    b = fig.add_axes([0.53, 0.15, 0.45, 0.76])
    Pmax, hmax, hf = 10.0, 280.0, 150.0
    hload = 274.0
    h1 = np.linspace(0, hload, 300)
    P1 = Pmax * (h1 / hload) ** 2
    m = 1.5
    alpha = Pmax / (hmax - hf) ** m
    h2 = np.linspace(hmax, hf, 300)
    P2 = alpha * (h2 - hf) ** m
    S = m * Pmax / (hmax - hf)
    hc = hmax - 0.75 * Pmax / S
    hr = hmax - Pmax / S
    b.fill(np.r_[h1, hmax, h2], np.r_[P1, Pmax, P2], color=ORANGE, alpha=0.18, lw=0)
    b.plot(h1, P1, color=BLUE, label="loading")
    b.plot([hload, hmax], [Pmax, Pmax], color=INK, lw=1.6)
    b.plot(h2, P2, color=VERM, label="unloading")
    ht = np.linspace(hr, hmax + 10, 10)
    b.plot(ht, Pmax + S * (ht - hmax), color=GREEN, lw=1.1, ls="--")
    b.text(286, 6.5, "S = dP/dh", color="#006B4E", fontsize=8.5, ha="left")
    b.text(hmax - 4, Pmax + 0.25, "hold", fontsize=7.5, ha="center", va="bottom")
    b.text(200, 3.6, "plastic\nwork", fontsize=8.5, ha="center", color="#8A5A00")
    for hv, lab in [(hf, "h$_f$"), (hc, "h$_c$"), (hmax, "h$_{max}$")]:
        b.plot([hv, hv], [0, 0.45], color=INK, lw=1.0)
        b.text(hv, 0.55, lab, ha="center", va="bottom", fontsize=8.5)
    b.text(hr, -0.05, "", fontsize=1)
    b.set_xlim(0, 345); b.set_ylim(0, 11.5)
    b.set_xlabel("displacement h (nm)")
    b.set_ylabel("load P (mN)")
    b.legend(loc="upper left", fontsize=8)
    b.text(5, 8.2, f"P$_{{max}}$ = 10 mN\nh$_c$ = h$_{{max}}$ − 0.75 P$_{{max}}$/S ≈ {hc:.0f} nm", fontsize=7.8,
           va="top")
    print(f"  indentation: S={S:.4f} mN/nm, hc={hc:.0f} nm, hr={hr:.0f}")
    save(fig, "11", "fig-11-5-indentation")


# ---------------------------------------------------------------- Figure 11.6
def _tanh(T, LS, US, T0, C):
    return LS + (US - LS) / 2 * (1 + np.tanh((T - T0) / C))


def charpy_transition():
    fig = plt.figure(figsize=(6.8, 4.0))
    ax = fig.add_axes([0.09, 0.13, 0.64, 0.82])
    T = np.linspace(-196, 100, 600)
    # S355J0: LS 5, US 200, midpoint 10 °C, 27 J at -10 °C
    C1 = (-10 - 10) / np.arctanh(2 * (27 - 5) / 195 - 1)
    E1 = _tanh(T, 5, 200, 10, C1)
    # Ni low-temperature steel: US 250, 27 J at -70 °C (midpoint -45 °C)
    C2 = (-70 + 45) / np.arctanh(2 * (27 - 5) / 245 - 1)
    E2 = _tanh(T, 5, 250, -45, C2)
    E3 = 200 - 50 * ((100 - T) / 296) ** 1.5
    E4 = 30 + 10 * ((100 - T) / 296)
    ax.plot(T, E2, color=BLUE, label="fine-grained Ni low-temperature steel")
    ax.plot(T, E1, color=VERM, label="structural steel S355J0")
    ax.plot(T, E3, color=GREEN, label="austenitic stainless 304")
    ax.plot(T, E4, color=PINK, label="aluminium 5083-O")
    ax.axhline(27, color=INK, lw=0.9, ls="--")
    ax.text(98, 24, "27 J: typical spec. level", fontsize=7.5, va="top", ha="right")
    for TT, EE, col in [(-10, 27, VERM), (-70, 27, BLUE)]:
        ax.plot(TT, EE, "o", color=col, ms=5, zorder=5)
    ax.text(-23, 14, "T$_{27J}$ ≈ −10 °C", fontsize=7.5, color=VERM, ha="right")
    ax.text(-80, 14, "T$_{27J}$ ≈ −70 °C", fontsize=7.5, color=BLUE, ha="right")
    ax.set_xlim(-196, 100)
    ax.set_ylim(0, 300)
    ax.set_xlabel("test temperature (°C)")
    ax.set_ylabel("Charpy V-notch energy (J)")
    ax.legend(loc="upper left", fontsize=7.8, bbox_to_anchor=(0.0, 1.02))
    ax.text(70, 208, "upper shelf", fontsize=7.8, color=VERM, ha="center", va="bottom")
    ax.text(-188, 8, "lower shelf", fontsize=7.5, color=VERM, ha="left", va="bottom")
    # fracture-surface insets
    rng = np.random.default_rng(4)
    i1 = fig.add_axes([0.78, 0.56, 0.20, 0.30])
    i1.set_xlim(0, 1); i1.set_ylim(0, 1); i1.set_aspect("equal"); i1.set_xticks([]); i1.set_yticks([])
    i1.set_facecolor("#E9E4DA")
    for _ in range(70):
        x, y = rng.uniform(0, 1, 2)
        r = rng.uniform(0.025, 0.06)
        i1.add_patch(Circle((x, y), r, fc="#D2CABB", ec="0.35", lw=0.6))
        i1.add_patch(Circle((x + 0.25 * r, y - 0.25 * r), 0.25 * r, fc="0.35", ec="none"))
    i1.set_title("fibrous (ductile):\ndimples", fontsize=8, pad=3)
    i2 = fig.add_axes([0.78, 0.13, 0.20, 0.30])
    i2.set_xlim(0, 1); i2.set_ylim(0, 1); i2.set_aspect("equal"); i2.set_xticks([]); i2.set_yticks([])
    from scipy.spatial import Voronoi
    seeds = rng.uniform(-0.3, 1.3, (30, 2))
    V = Voronoi(seeds)
    for k, reg_i in enumerate(V.point_region):
        reg = V.regions[reg_i]
        if -1 in reg or not reg:
            continue
        poly = V.vertices[reg]
        g = rng.uniform(0.70, 0.95)
        i2.add_patch(Polygon(poly, fc=(g, g, g * 1.02 if g < 0.98 else g), ec="0.3", lw=0.7))
        cx, cy = seeds[k]
        ang = rng.uniform(0, np.pi)
        for j in range(3):
            o = (j - 1) * 0.04
            i2.plot([cx - 0.06 * np.cos(ang) + o * np.sin(ang), cx + 0.06 * np.cos(ang) + o * np.sin(ang)],
                    [cy - 0.06 * np.sin(ang) - o * np.cos(ang), cy + 0.06 * np.sin(ang) - o * np.cos(ang)],
                    color="0.45", lw=0.5)
    i2.set_title("cleavage (brittle):\nflat facets, river lines", fontsize=8, pad=3)
    # connectors
    save(fig, "11", "fig-11-6-charpy-transition")


if __name__ == "__main__":
    stress_tensor_mohr()
    directional_modulus()
    modulus_by_class()
    tensile_true_engineering()
    indentation()
    charpy_transition()
