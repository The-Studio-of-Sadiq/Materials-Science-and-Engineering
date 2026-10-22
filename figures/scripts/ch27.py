"""Figures for Chapter 27 — Functional Dielectric Materials.

Run from the repository root:  python figures/scripts/ch27.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, Ellipse
from scipy.interpolate import PchipInterpolator


# ---------------------------------------------------------------- Figure 27.1
def symmetry_classes():
    fig, ax = schematic(6.6, 4.6, xlim=(0, 11), ylim=(0, 7.6))
    levels = [
        ((0.05, 0.05, 10.9, 7.5), "#EEF1F6", "All dielectrics: 32 point groups (plus amorphous solids)",
         "electrostriction ($S\\propto E^2$) present in all"),
        ((3.2, 0.25, 7.55, 6.2), "#DCE8F4", "Non-centrosymmetric: 21 point groups", ""),
        ((3.4, 0.45, 7.15, 5.15), "#C6E2D2", "Piezoelectric: 20 point groups", "quartz, GaAs, AlN"),
        ((3.6, 0.65, 6.75, 3.95), "#F6DDB8", "Pyroelectric (polar): 10 point groups",
         "ZnO, AlN, LiTaO$_3$, tourmaline"),
        ((3.8, 0.85, 6.35, 2.55), "#F2C1BE", "Ferroelectric: polar and switchable",
         "BaTiO$_3$, PZT, LiNbO$_3$, PVDF, HfO$_2$:Si"),
    ]
    for (x, y, w, h), c, title, ex in levels:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.25",
                                    fc=c, ec=INK, lw=0.9))
        ax.text(x + 0.2, y + h - 0.2, title, ha="left", va="top", fontsize=9.5, weight="bold")
        if ex:
            ax.text(x + 0.2, y + h - 0.62, ex, ha="left", va="top", fontsize=8.5, style="italic")
    # centrosymmetric examples outside the non-centrosymmetric box
    ax.text(1.65, 3.6, "Centrosymmetric\n(11 point groups,\nnot piezoelectric)", ha="center",
            va="center", fontsize=8.5, weight="bold")
    ax.text(1.65, 2.25, "NaCl, Si,\nalumina,\nglass", ha="center", va="center", fontsize=8.5,
            style="italic")
    ax.text(1.65, 0.35, "(class 432 is non-\ncentrosymmetric but\nnot piezoelectric)", ha="center",
            va="bottom", fontsize=7.5, color="#444444")
    save(fig, "27", "fig-27-1-symmetry-classes")


# ---------------------------------------------------------------- Figure 27.2
def _proj(p):
    x, y, z = p
    return np.array([x + 0.42 * y, z + 0.30 * y])


def _cell(ax, ox, c=1.0, ti_dz=0.0, o_dz=0.0, scale=2.2):
    P = lambda x, y, z: np.array([ox, 0.0]) + scale * _proj((x, y, z))
    # edges
    corners = [(i, j, k) for i in (0, 1) for j in (0, 1) for k in (0, 1)]
    for a in corners:
        for b in corners:
            if sum(abs(np.array(a) - np.array(b))) == 1 and a < b:
                pa, pb = P(a[0], a[1], a[2] * c), P(b[0], b[1], b[2] * c)
                back = (a[1] == 1 and b[1] == 1) or (a[0] == 0 and b[0] == 0 and a[1] + b[1] > 0 and a[2] + b[2] == 0)
                ax.plot([pa[0], pb[0]], [pa[1], pb[1]], color="#555555", lw=0.9, ls="-", zorder=1)
    # octahedron
    Os = {"b": (0.5, 0.5, 0.0), "t": (0.5, 0.5, 1.0), "l": (0.0, 0.5, 0.5), "r": (1.0, 0.5, 0.5),
          "f": (0.5, 0.0, 0.5), "k": (0.5, 1.0, 0.5)}
    Op = {k: P(v[0], v[1], (v[2] * c) + (o_dz if k in "lrfk" else 0.0) + (0 if k in "lrfk" else (
        o_dz * 0.5 if k == "t" else o_dz * 0.5))) for k, v in Os.items()}
    for apex in "bt":
        for e1, e2 in (("l", "f"), ("f", "r"), ("r", "k"), ("k", "l")):
            ax.add_patch(Polygon([Op[apex], Op[e1], Op[e2]], closed=True, fc="#E8A0A0", ec="#B05050",
                                 lw=0.6, alpha=0.28, zorder=2))
    atoms = []
    for (i, j, k) in corners:
        atoms.append(((i, j, k * c), 0.22, "#4F9A6A", "Ba"))
    for k_, v in Os.items():
        z = v[2] * c + o_dz * (1 if k_ in "lrfk" else 0.5)
        atoms.append(((v[0], v[1], z), 0.14, "#D9534F", "O"))
    atoms.append(((0.5, 0.5, 0.5 * c + ti_dz), 0.11, "#3B6FB6", "Ti"))
    atoms.sort(key=lambda a: -a[0][1])  # back (large y) first
    for pos, r, col, name in atoms:
        q = P(*pos)
        ax.add_patch(Circle(q, r, fc=col, ec=INK, lw=0.6, zorder=3 + (1 - pos[1]) * 2))
    return P


def batio3():
    fig = plt.figure(figsize=(6.6, 5.0))
    ax = fig.add_axes([0.0, 0.3, 1.0, 0.7])
    ax.set_xlim(-0.6, 9.4)
    ax.set_ylim(-1.45, 4.1)
    ax.set_aspect("equal")
    ax.axis("off")
    P1 = _cell(ax, 0.3, c=1.0)
    P2 = _cell(ax, 5.3, c=1.10, ti_dz=0.09, o_dz=-0.04)
    ax.text(P1(0.7, 0.5, 0)[0], -0.85, "cubic, $T>T_C$ (paraelectric)\n$a=0.401$ nm",
            ha="center", va="center", fontsize=9)
    ax.text(P2(0.7, 0.5, 0)[0], -0.85, "tetragonal, $T<T_C$ (ferroelectric)\n$c/a\\approx1.01$ (exaggerated)",
            ha="center", va="center", fontsize=9)
    # a dimension
    pa, pb = P1(0, 0, 0), P1(1, 0, 0)
    ax.annotate("", xy=(pb[0], pb[1] - 0.18), xytext=(pa[0], pa[1] - 0.18),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, mutation_scale=7, shrinkA=0, shrinkB=0))
    ax.text((pa[0] + pb[0]) / 2, pa[1] - 0.22, "$a$", ha="center", va="top", fontsize=9)
    # Ti displacement & Ps arrow
    tc = P2(0.5, 0.5, 0.55 + 0.09)
    ax.annotate("", xy=(tc[0], tc[1] + 0.45), xytext=(tc[0], tc[1] + 0.12),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.6, mutation_scale=10,
                                shrinkA=0, shrinkB=0), zorder=10)
    pl = P2(0, 0, 0)
    ax.annotate("Ti shift ≈ 0.01 nm\n(exaggerated)", xy=(tc[0] - 0.05, tc[1] + 0.3),
                xytext=(pl[0] - 0.55, P2(0, 0, 1.25)[1] + 0.25), fontsize=7.5, color=COLORS[0],
                ha="center", va="bottom", zorder=12,
                arrowprops=dict(arrowstyle="-", color=COLORS[0], lw=0.6))
    right = P2(1, 0, 0.5)[0] + 1.25
    ax.annotate("", xy=(right, P2(1, 0, 0.95)[1] + 0.3), xytext=(right, P2(1, 0, 0.1)[1] + 0.3),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=2.4, mutation_scale=14))
    ax.text(right + 0.12, P2(1, 0, 0.55)[1] + 0.3, "$P_s$\n‖ $c$", color=COLORS[1], fontsize=10, va="center")
    pc0, pc1 = P2(0, 0, 0), P2(0, 0, 1.10)
    ax.annotate("", xy=(pc1[0] - 0.4, pc1[1]), xytext=(pc0[0] - 0.4, pc0[1]),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, mutation_scale=7, shrinkA=0, shrinkB=0))
    ax.text(pc0[0] - 0.5, P2(0, 0, 0.55)[1], "$c$", fontsize=10, ha="right", va="center")
    ax.text(P2(0.7, 0.5, 0)[0], -1.22, "O octahedron shifts opposite to Ti", fontsize=8, ha="center",
            color="#B05050")
    # legend of atoms
    for i, (lab, col, r) in enumerate((("Ba$^{2+}$", "#4F9A6A", 0.17), ("O$^{2-}$", "#D9534F", 0.12),
                                       ("Ti$^{4+}$", "#3B6FB6", 0.08))):
        ax.add_patch(Circle((-0.3 + 1.25 * i, 3.85), r, fc=col, ec=INK, lw=0.6))
        ax.text(-0.05 + 1.25 * i, 3.85, lab, va="center", fontsize=9)
    # phase sequence
    axp = fig.add_axes([0.07, 0.07, 0.88, 0.13])
    axp.set_xlim(-150, 200)
    axp.set_ylim(0, 1)
    for s in ("left", "right", "top"):
        axp.spines[s].set_visible(False)
    axp.set_yticks([])
    phases = [(-150, -90, "rhombohedral", "$P\\parallel[111]$", "#E6E0F2"),
              (-90, 5, "orthorhombic", "$P\\parallel[110]$", "#E1EEF7"),
              (5, 125, "tetragonal", "$P\\parallel[001]$", "#E6F2E1"),
              (125, 200, "cubic", "$P=0$", "#F7EBDD")]
    for lo, hi, n, p, col in phases:
        axp.axvspan(lo, hi, color=col)
        axp.text((lo + hi) / 2, 0.68, n, ha="center", va="center", fontsize=9)
        axp.text((lo + hi) / 2, 0.28, p, ha="center", va="center", fontsize=9)
    for t in (-90, 5, 125):
        axp.axvline(t, color=INK, lw=0.8)
    axp.set_xticks([-150, -90, 5, 125, 200])
    axp.set_xlabel("Temperature (°C)")
    axp.text(125, 1.05, "$T_C$", ha="center", va="bottom", fontsize=9)
    save(fig, "27", "fig-27-2-batio3-perovskite")


# ---------------------------------------------------------------- Figure 27.3
def _bto_eps(T):
    Tc, C = 125.0, 1.7e5
    T0 = Tc - C / 1.0e4
    above = C / np.maximum(T - T0, 1e-3)
    base = 1300 + 6.0 * (T + 150)
    below = (base + 2600 / (1 + ((T - 5) / 9) ** 2) + 1500 / (1 + ((T + 90) / 11) ** 2)
             + (1.0e4 - 2400) * np.exp(-(Tc - T) / 5.0))
    return np.where(T >= Tc, above, below)


def pe_and_eps():
    fig = plt.figure(figsize=(6.8, 5.4))
    E = np.linspace(-3, 3, 400)
    tops = []
    w = 0.19
    for k in range(4):
        tops.append(fig.add_axes([0.07 + k * 0.24, 0.62, w, 0.30]))
    titles = ["(a) linear dielectric", "(b) ferroelectric\n(PZT-like)", "(c) relaxor (PMN)",
              "(d) paraelectric"]
    for a, t in zip(tops, titles):
        a.axhline(0, color="#999999", lw=0.6)
        a.axvline(0, color="#999999", lw=0.6)
        a.set_xlim(-3.2, 3.2)
        a.set_ylim(-0.48, 0.48)
        a.set_xticks([-3, 0, 3])
        a.set_title(t, fontsize=9, pad=4)
        a.tick_params(labelsize=8)
        a.set_xlabel("$E$ (kV/mm)", fontsize=8.5, labelpad=1)
    for a in tops[1:]:
        a.set_yticklabels([])
    tops[0].set_ylabel("$P$ (C/m$^2$)", fontsize=9)
    tops[0].plot(E, 0.04 * E, color=COLORS[0])
    Ps, Ec, d = 0.35, 1.0, 0.78
    up = Ps * np.tanh((E - Ec) / d) + 0.01 * E
    dn = Ps * np.tanh((E + Ec) / d) + 0.01 * E
    tops[1].plot(E, up, color=COLORS[1])
    tops[1].plot(E, dn, color=COLORS[1])
    pr = Ps * np.tanh(Ec / d)
    tops[1].plot([0], [pr], "o", color=INK, ms=3)
    tops[1].text(0.2, 0.17, r"$P_r\approx0.3$", fontsize=8, va="bottom")
    tops[1].plot([Ec], [0], "o", color=INK, ms=3)
    tops[1].text(Ec + 0.1, -0.1, "$E_c\\approx1$", fontsize=8, va="top")
    tops[2].plot(E, 0.3 * np.tanh((E - 0.08) / 1.0), color=COLORS[3])
    tops[2].plot(E, 0.3 * np.tanh((E + 0.08) / 1.0), color=COLORS[3])
    Eb = np.linspace(-3, 3, 300)
    tops[3].plot(Eb, 0.25 * np.tanh(Eb / 1.6), color=COLORS[2])
    e0 = 1.6; p0 = 0.25 * np.tanh(e0 / 1.6); sl = 0.25 / 1.6 / np.cosh(e0 / 1.6) ** 2
    tops[3].plot([e0 - 0.9, e0 + 0.9], [p0 - 0.9 * sl, p0 + 0.9 * sl], color=INK, lw=0.8)
    tops[3].plot(e0, p0, "o", color=INK, ms=3)
    tops[3].text(e0 - 0.2, p0 + 0.09, "bias point:\nlower slope", fontsize=7.5, ha="center")
    tops[3].text(0.3, -0.35, "no loop", fontsize=8)
    # bottom: eps-T
    ax = fig.add_axes([0.09, 0.08, 0.86, 0.40])
    T = np.linspace(-150, 200, 1400)
    eps = _bto_eps(T)
    ax.plot(T, eps, color=COLORS[1], label="BaTiO$_3$ ceramic (undoped)")
    Tx = np.linspace(-150, 200, 500)
    x7 = 3000 * (1 - 0.10 * ((Tx - 25) / 80) ** 2 + 0.07 * np.exp(-((Tx - 120) / 18) ** 2))
    x7 = np.where(Tx > 125, x7 * np.exp(-(Tx - 125) / 60), x7)
    x7 = np.where(Tx < -55, x7 * np.exp((Tx + 55) / 90), x7)
    ax.plot(Tx, x7, color=COLORS[0], ls="--", label='doped core–shell "X7R" ceramic')
    ax.add_patch(Rectangle((-55, 2550), 180, 900, fc="none", ec=COLORS[0], lw=0.8, ls=":"))
    ax.text(-2, 2420, "X7R window: ±15 %, −55 to 125 °C", fontsize=8, color=COLORS[0], va="top")
    for t, lab in ((-90, "R–O"), (5, "O–T"), (125, "$T_C$ (T–C)")):
        ax.axvline(t, color="#BBBBBB", lw=0.6, ls=":")
        ax.text(t, 10400, lab, ha="center", va="bottom", fontsize=8)
    Ta = np.linspace(140, 195, 10)
    ax.annotate("Curie–Weiss\n$\\varepsilon_r\\approx C/(T-T_0)$", xy=(150, float(_bto_eps(np.array([150.0]))[0])),
                xytext=(160, 7000), fontsize=8.5, arrowprops=dict(arrowstyle="-", lw=0.6))
    ax.set_xlim(-150, 200)
    ax.set_ylim(0, 11000)
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel(r"$\varepsilon_r$", fontsize=12)
    ax.legend(loc="upper left", fontsize=8.5, bbox_to_anchor=(0.0, 0.93))
    save(fig, "27", "fig-27-3-pe-loops-and-epsilon-t")


# ---------------------------------------------------------------- Figure 27.4
def mlcc():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.8, 3.8))
    curves = {
        "C0G": (np.array([-55, 125]), np.array([0, 0]), COLORS[2]),
        "X7R": (np.array([-55, -30, 0, 25, 60, 90, 110, 125]),
                np.array([-11, -6, -2, 0, -1.5, -1, 3, 5]), COLORS[0]),
        "X5R": (np.array([-55, -25, 0, 25, 50, 85]), np.array([-13, -6, -2, 0, -4, -12]), COLORS[3]),
        "Y5V": (np.array([-30, -15, 0, 10, 18, 25, 45, 65, 85]),
                np.array([-62, -30, 10, 20, 14, 0, -38, -64, -80]), COLORS[1]),
    }
    for n, (tx, ty, c) in curves.items():
        T = np.linspace(tx[0], tx[-1], 300)
        y = PchipInterpolator(tx, ty)(T) if len(tx) > 2 else np.zeros_like(T)
        a1.plot(T, y, color=c, label=n)
    boxes = [(-55, 125, -15, 15, COLORS[0]), (-55, 85, -15.8, 15.8, COLORS[3]), (-30, 85, -82, 22, COLORS[1])]
    for t0, t1, y0, y1, c in boxes:
        a1.add_patch(Rectangle((t0, y0), t1 - t0, y1 - y0, fc="none", ec=c, ls="--", lw=0.9))
    a1.text(122, 16.5, "X7R ±15 %", color=COLORS[0], fontsize=7.5, ha="right", va="bottom")
    a1.text(-28, -79, "Y5V +22/−82 %", color=COLORS[1], fontsize=7.5, ha="left", va="bottom")
    a1.set_xlim(-60, 130)
    a1.set_ylim(-90, 25)
    a1.set_xlabel("Temperature (°C)")
    a1.set_ylabel("Capacitance change (%)")
    a1.legend(loc="lower right", fontsize=8, handlelength=1.2, bbox_to_anchor=(1.04, 0.0))
    a1.axhline(0, color="#BBBBBB", lw=0.5)
    v = np.linspace(0, 100, 200)
    a2.plot(v, 0 * v, color=COLORS[2], label="C0G")
    a2.plot(v, -30 * (v / 100) ** 1.6, color=COLORS[0], label="X7R, 1206 (thick layers)")
    a2.plot(v, -70 * (1 - np.exp(-v / 45)) / (1 - np.exp(-100 / 45)), color=COLORS[3],
            label="X5R, 0402 (thin layers)")
    a2.plot(v, -80 * (1 - np.exp(-v / 25)) / (1 - np.exp(-4)), color=COLORS[1], label="Y5V")
    a2.set_xlim(0, 100)
    a2.set_ylim(-90, 5)
    a2.set_xlabel("d.c. bias (% of rated voltage)")
    a2.set_ylabel("Capacitance change (%)")
    for xt, yt, t, c in ((55, 2, "C0G", COLORS[2]), (52, -37, "X7R, 1206\n(thick layers)", COLORS[0]),
                         (52, -50, "X5R, 0402 (thin layers)", COLORS[3]), (45, -86, "Y5V", COLORS[1])):
        a2.text(xt, yt, t, color=c, fontsize=8.5, va="bottom" if yt > -80 else "center")
    for a, t in ((a1, "(a) temperature"), (a2, "(b) d.c. bias, 25 °C")):
        a.set_title(t, fontsize=10)
    fig.tight_layout()
    save(fig, "27", "fig-27-4-mlcc-dc-bias-temperature")


# ---------------------------------------------------------------- Figure 27.5
def microwave_map():
    data = [  # name, eps, Qf, tau_f near zero?, label offset (dx factor, dy factor), ha
        ("Al$_2$O$_3$", 10, 4.0e5, False, (1.0, 1.55), "center"),
        ("forsterite", 7, 2.0e5, False, (1.0, 0.62), "center"),
        ("BMT", 24, 3.0e5, True, (0.92, 1.0), "right"),
        ("BZT", 30, 1.7e5, True, (1.12, 1.0), "left"),
        ("MCT", 21, 5.5e4, True, (0.89, 1.0), "right"),
        ("(Zr,Sn)TiO$_4$", 38, 4.5e4, True, (0.97, 1.45), "center"),
        ("Ba$_2$Ti$_9$O$_{20}$", 40, 3.5e4, True, (1.08, 0.78), "left"),
        ("CT–NA", 44, 4.5e4, True, (1.1, 1.18), "left"),
        ("Ba–Nd–Ti", 85, 8e3, True, (1.0, 0.68), "center"),
        ("TiO$_2$\n($\\tau_f=+450$)", 100, 4.5e4, False, (1.0, 1.5), "center"),
    ]
    fig, ax = new_fig(6.4, 4.4)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.add_patch(Rectangle((20, 3e4), 26, 2.7e5, fc="#E5F0E0", ec="#7FB070", lw=0.8, zorder=0))
    ax.text(21, 3.3e5, "base-station\nfilter materials", fontsize=8, color="#3E7A2E", va="bottom")
    ax.plot([10, 10], [3e5, 5e5], color=COLORS[0], lw=5, alpha=0.35, solid_capstyle="round")
    for n, e, q, zero, (fx, fy), ha in data:
        ax.plot(e, q, "o", ms=7, color=COLORS[0], mfc=COLORS[0] if zero else "white", mew=1.4, zorder=4)
        ax.text(e * fx, q * fy, n, fontsize=8.5, ha=ha, va="center")
    ee = np.logspace(np.log10(6), np.log10(140), 50)
    ax.plot(ee, 5e5 * (10 / ee) ** 1.6, color="#888888", ls="--", lw=1.2)
    ax.text(70, 5e5 * (10 / 70) ** 1.6 * 1.25, "trend", color="#777777", fontsize=8.5, rotation=-28)
    ax.plot([], [], "o", color=COLORS[0], label=r"$\tau_f\approx0$")
    ax.plot([], [], "o", color=COLORS[0], mfc="white", mew=1.4, label=r"large $|\tau_f|$")
    ax.legend(loc="lower left", fontsize=8.5)
    ax.set_xlim(5, 150)
    ax.set_ylim(1e3, 1e6)
    ax.set_xticks([5, 10, 20, 50, 100, 150])
    ax.set_xticklabels(["5", "10", "20", "50", "100", "150"])
    ax.set_xlabel(r"Relative permittivity, $\varepsilon_r$")
    ax.set_ylabel(r"$Q\times f$ (GHz)")
    save(fig, "27", "fig-27-5-microwave-dielectrics-qf-map")


# ---------------------------------------------------------------- Figure 27.6
def mach_zehnder():
    fig = plt.figure(figsize=(6.8, 5.0))
    at = fig.add_axes([0.02, 0.50, 0.96, 0.48])
    at.set_xlim(0, 12)
    at.set_ylim(-0.3, 4.6)
    at.set_aspect("equal")
    at.axis("off")
    at.add_patch(Rectangle((0, 0), 12, 4.2, fc="#EEF0F6", ec=INK, lw=0.8))
    yc, dy = 2.1, 0.62
    wg = dict(color="#C0392B", lw=2.0)
    xs = np.linspace(1.6, 3.0, 50)
    s = (1 - np.cos(np.pi * (xs - 1.6) / 1.4)) / 2
    at.plot([0, 1.6], [yc, yc], **wg)
    at.plot(xs, yc + dy * s, **wg)
    at.plot(xs, yc - dy * s, **wg)
    at.plot([3.0, 9.0], [yc + dy, yc + dy], **wg)
    at.plot([3.0, 9.0], [yc - dy, yc - dy], **wg)
    xs2 = np.linspace(9.0, 10.4, 50)
    s2 = (1 + np.cos(np.pi * (xs2 - 9.0) / 1.4)) / 2
    at.plot(xs2, yc + dy * s2, **wg)
    at.plot(xs2, yc - dy * s2, **wg)
    at.plot([10.4, 12], [yc, yc], **wg)
    # electrodes G S G
    ek = dict(fc="#E3B23C", ec=INK, lw=0.7, alpha=0.95)
    at.add_patch(Rectangle((3.2, yc + dy + 0.18), 5.6, 0.9, **ek))
    at.add_patch(Rectangle((3.2, yc - 0.44), 5.6, 0.88, **ek))
    at.add_patch(Rectangle((3.2, yc - dy - 1.08), 5.6, 0.9, **ek))
    at.text(6.0, yc + dy + 0.63, "G", ha="center", va="center", fontsize=9, weight="bold")
    at.text(6.0, yc, "S (signal, travelling wave)", ha="center", va="center", fontsize=8.5)
    at.text(6.0, yc - dy - 0.63, "G", ha="center", va="center", fontsize=9, weight="bold")
    at.add_patch(Rectangle((2.6, yc - 0.22), 0.6, 0.44, fc="#E3B23C", ec=INK, lw=0.6))
    at.text(0.15, yc + 0.18, "light in", fontsize=8.5, va="bottom")
    at.text(11.85, yc + 0.18, "out", fontsize=8.5, va="bottom", ha="right")
    at.text(1.75, yc - 0.95, "Y-junction", fontsize=8, ha="center")
    at.text(10.25, yc - 0.95, "Y-junction", fontsize=8, ha="center")
    at.annotate("", xy=(8.8, 4.38), xytext=(3.2, 4.38),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0))
    at.text(6.0, 4.42, "$L\\approx20$ mm", ha="center", va="bottom", fontsize=9)
    at.text(11.9, 0.12, "x-cut LiNbO$_3$, TE mode uses $r_{33}$", ha="right", va="bottom", fontsize=8.5)
    # in an x-cut wafer z (c) lies in the plane, perpendicular to the waveguides
    at.annotate("", xy=(0.5, 1.45), xytext=(0.5, 0.35),
                arrowprops=dict(arrowstyle="-|>", lw=1.0, mutation_scale=8))
    at.text(0.65, 0.9, "$z$ ($c$)", ha="left", va="center", fontsize=8.5)
    at.text(0.15, 3.95, "top view", ha="left", va="top", fontsize=8.5, style="italic")
    # cross-section
    ac = fig.add_axes([0.02, 0.02, 0.56, 0.44])
    ac.set_xlim(0, 8)
    ac.set_ylim(-0.4, 4.4)
    ac.set_aspect("equal")
    ac.axis("off")
    ac.add_patch(Rectangle((0, 0), 8, 1.2, fc="#D8D8D8", ec=INK, lw=0.7))
    ac.text(7.9, 0.6, "Si", ha="right", va="center", fontsize=8.5)
    ac.add_patch(Rectangle((0, 1.2), 8, 0.9, fc="#F3F3F3", ec=INK, lw=0.7))
    ac.text(7.9, 1.65, "SiO$_2$", ha="right", va="center", fontsize=8.5)
    ac.add_patch(Rectangle((0, 2.1), 8, 0.6, fc="#DDE6F5", ec=INK, lw=0.7))
    ac.text(7.9, 2.4, "thin-film LiNbO$_3$", ha="right", va="center", fontsize=8)
    # rib waveguides
    for xw in (2.6, 5.4):
        ac.add_patch(Rectangle((xw - 0.35, 2.7), 0.7, 0.25, fc="#DDE6F5", ec=INK, lw=0.7))
        ac.add_patch(Ellipse((xw, 2.65), 0.75, 0.42, fc="#C0392B", alpha=0.55, ec="none", zorder=4))
    # electrodes
    for x0, w, lab in ((0.3, 1.5, "G"), (3.35, 1.3, "S"), (6.2, 1.5, "G")):
        ac.add_patch(Rectangle((x0, 2.7), w, 0.35, fc="#E3B23C", ec=INK, lw=0.7))
        ac.text(x0 + w / 2, 3.1, lab, ha="center", va="bottom", fontsize=9, weight="bold")
    # field lines S -> G (horizontal through waveguides)
    for h in (0.04, 0.15, 0.28):
        for sgn in (-1, 1):
            xa = 4.0 + sgn * 0.65
            xb = 4.0 + sgn * 2.2
            xx = np.linspace(xa, xb, 40)
            yy = 2.86 - h * np.sin(np.pi * (xx - xa) / (xb - xa))
            ac.plot(xx, yy, color=COLORS[0], lw=0.9, zorder=5)
            i = 21
            ac.annotate("", xy=(xx[i + 1], yy[i + 1]), xytext=(xx[i], yy[i]),
                        arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=0.9, mutation_scale=7), zorder=5)
    ac.annotate("", xy=(1.8, 3.75), xytext=(3.35, 3.75),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, mutation_scale=7, shrinkA=0, shrinkB=0))
    ac.text(2.575, 3.82, "gap $d$", ha="center", va="bottom", fontsize=8.5)
    ac.annotate("", xy=(1.3, 4.25), xytext=(0.2, 4.25),
                arrowprops=dict(arrowstyle="-|>", lw=1.0, mutation_scale=8))
    ac.text(1.4, 4.25, "$z$ ($c$ axis)", va="center", fontsize=8.5)
    ac.text(4.0, -0.3, "cross-section: optical modes (red) and field $E\\approx V/d$ along $z$",
            ha="center", va="center", fontsize=8)
    # inset transfer curve
    ai = fig.add_axes([0.66, 0.09, 0.31, 0.30])
    Vpi = 5.1
    V = np.linspace(-12, 12, 400)
    ai.plot(V, np.cos(np.pi * V / (2 * Vpi)) ** 2, color=COLORS[1])
    ai.axvline(Vpi, color="grey", ls=":", lw=0.9)
    ai.annotate("", xy=(Vpi, 0.5), xytext=(0, 0.5),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, mutation_scale=7, shrinkA=0, shrinkB=0))
    ai.text(Vpi / 2, 0.55, "$V_\\pi\\approx5$ V", ha="center", va="bottom", fontsize=8,
            bbox=dict(fc="white", ec="none", pad=0.5))
    ai.set_xlim(-12, 12)
    ai.set_ylim(0, 1.12)
    ai.set_xlabel("$V$ (V)", fontsize=9)
    ai.set_ylabel("$I_{\\rm out}/I_{\\rm in}$", fontsize=9)
    ai.tick_params(labelsize=8)
    save(fig, "27", "fig-27-6-linbo3-mach-zehnder")


if __name__ == "__main__":
    symmetry_classes()
    batio3()
    pe_and_eps()
    mlcc()
    microwave_map()
    mach_zehnder()
