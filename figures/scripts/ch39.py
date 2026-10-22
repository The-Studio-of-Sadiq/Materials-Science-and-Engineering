"""Figures for Chapter 39 — Biomaterials.

Run from the repository root:  python figures/scripts/ch39.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, Ellipse, FancyBboxPatch, Wedge, PathPatch
from matplotlib.path import Path
from matplotlib.lines import Line2D
from scipy.interpolate import splprep, splev

BONE = "#EADBB8"
BONE_D = "#D6C08E"
TI = "#9DB0C0"
COCR = "#C8CDD3"
PE = "#F4F1E6"
CER = "#F7F2D8"


# ---------------------------------------------------------------- Figure 39.1
def host_response_timeline():
    fig = plt.figure(figsize=(6.8, 5.2))
    ax = fig.add_axes([0.035, 0.36, 0.60, 0.56])
    ax.set_xscale("log")
    YEAR = 3.156e7
    ax.set_xlim(1, YEAR)
    ax.set_ylim(-0.4, 5.3)
    ticks = [1, 60, 3600, 86400, 604800, 2.63e6, YEAR]
    ax.set_xticks(ticks)
    ax.set_xticklabels(["1 s", "1 min", "1 h", "1 day", "1 wk", "1 mo", "1 yr"], fontsize=8)
    ax.xaxis.set_minor_locator(plt.NullLocator())
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    for t in ticks:
        ax.axvline(t, color="0.88", lw=0.6, zorder=0)
    ax.set_xlabel("time after implantation (log scale)")
    bands = [  # label, start, end, colour, fade-to (or None)
        ("protein adsorption,\nVroman exchange", 1, 3600, "#7FA7D1", None),
        ("platelet adhesion,\ncoagulation", 60, 3.6e4, "#D98C8C", None),
        ("acute inflammation\n(neutrophils)", 3600, 2.6e5, "#E8B04B", None),
        ("chronic inflammation:\nmacrophages, giant cells", 2.6e5, 3.6e6, "#A98BC6", YEAR),
        ("fibrous capsule\n50–200 µm", 1.2e6, YEAR, "#7DBE9A", None),
    ]
    for k, (lab, a, b, c, fade) in enumerate(bands):
        y = 4.6 - k * 1.05
        ax.add_patch(FancyBboxPatch((a, y - 0.32), b - a, 0.64, boxstyle="round,pad=0,rounding_size=0.15",
                                    fc=c, ec="none", alpha=0.85, mutation_aspect=0.05))
        if fade:
            xs = np.logspace(np.log10(b), np.log10(fade), 30)
            for x0, x1, al in zip(xs[:-1], xs[1:], np.linspace(0.6, 0.05, 29)):
                ax.add_patch(Rectangle((x0, y - 0.32), x1 - x0, 0.64, fc=c, ec="none", alpha=al))
        if k >= 3:
            ax.text(a / 1.5, y, lab, ha="right", va="center", fontsize=7.8)
        else:
            ax.text(b * 1.4, y, lab, ha="left", va="center", fontsize=7.8)
    ax.set_title("(a) common sequence of the host response", fontsize=9.5, loc="left")

    # (b) end points
    bx = fig.add_axes([0.66, 0.36, 0.33, 0.56])
    bx.set_xlim(0, 4); bx.set_ylim(-0.3, 6.6); bx.set_aspect("equal"); bx.axis("off")
    bx.set_title("(b) two end points", fontsize=9.5, loc="left")
    # soft tissue: implant + giant cells + collagen capsule
    y0 = 3.75
    bx.add_patch(Rectangle((0.1, y0), 1.1, 2.2, fc=TI, ec=INK, lw=0.8))
    bx.text(0.65, y0 + 1.1, "implant", rotation=90, ha="center", va="center", fontsize=7.5)
    bx.text(0.05, y0 + 2.3, "soft tissue: fibrous encapsulation", fontsize=7.8, va="bottom", color="#7A2E49")
    rng = np.random.default_rng(4)
    for yy in np.linspace(y0 + 0.25, y0 + 1.95, 4):
        bx.add_patch(Ellipse((1.38, yy), 0.32, 0.42, fc="#C9B3E0", ec=INK, lw=0.5))
        for d in (-0.08, 0.06):
            bx.plot(1.38 + d * 0.6, yy + d, "o", ms=1.6, color="#4B2A6E")
    for xx in np.linspace(1.65, 2.25, 6):
        t = np.linspace(y0, y0 + 2.2, 60)
        bx.plot(xx + 0.04 * np.sin(t * 9 + xx * 5), t, color="#C0577A", lw=0.9)
    bx.add_patch(Rectangle((2.35, y0), 1.5, 2.2, fc="#F6DADF", ec="none"))
    bx.text(3.1, y0 + 1.1, "soft\ntissue", ha="center", va="center", fontsize=7.3)
    bx.text(1.75, y0 - 0.1, "giant cells + collagen capsule (50–200 µm)", ha="center", va="top", fontsize=7.0)
    # bone: osseointegration
    y1 = 0.2
    bx.add_patch(Rectangle((0.1, y1), 1.1, 2.2, fc=TI, ec=INK, lw=0.8))
    bx.text(0.65, y1 + 1.1, "implant", rotation=90, ha="center", va="center", fontsize=7.5)
    bx.add_patch(Rectangle((1.2, y1), 2.65, 2.2, fc=BONE, ec="none"))
    for k in range(30):
        cx_, cy_ = 1.5 + rng.random() * 2.2, y1 + 0.2 + rng.random() * 1.8
        bx.add_patch(Ellipse((cx_, cy_), 0.25, 0.16, angle=rng.random() * 180, fc="#F8F1E0", ec=BONE_D, lw=0.5))
    bx.plot([1.2, 1.2], [y1, y1 + 2.2], color=INK, lw=1.2)
    bx.text(2.6, y1 + 1.1, "bone", ha="center", va="center", fontsize=7.5,
            bbox=dict(fc=BONE, ec="none", pad=0.5))
    bx.text(0.05, y1 + 2.3, "bone: osseointegration (direct contact),\nneeds micromotion < ~50–150 µm",
            fontsize=7.6, va="bottom", color="#6B5A2A")

    # (c) particle size scale
    cx = fig.add_axes([0.06, 0.07, 0.90, 0.13])
    cx.set_xscale("log")
    cx.set_xlim(0.01, 1e4)
    cx.set_ylim(0, 1)
    cx.set_yticks([])
    for sp in ("left", "right", "top"):
        cx.spines[sp].set_visible(False)
    cx.set_xticks([0.01, 0.1, 1, 10, 100, 1000, 1e4])
    cx.set_xticklabels(["10 nm", "0.1 µm", "1 µm", "10 µm", "100 µm", "1 mm", "10 mm"], fontsize=8)
    cx.xaxis.set_minor_locator(plt.NullLocator())
    cx.axvspan(0.1, 10, color="#F3C9A6", lw=0)
    cx.axvspan(10, 1e4, color="#E3DAF0", lw=0)
    cx.text(1, 0.5, "phagocytosed by macrophages\n(0.1–10 µm): wear debris → cytokines\n→ osteoclasts → osteolysis"
,
            ha="center", va="center", fontsize=7.3)
    cx.text(300, 0.5, "too large to engulf (> 10 µm): macrophages\nfuse into foreign-body giant cells\non the implant surface",
            ha="center", va="center", fontsize=7.3)

    cx.text(0.03, 0.5, "ions,\nnano-\nparticles", ha="center", va="center", fontsize=7)
    cx.set_title("(c) particle or object size and the cellular response", fontsize=9.5, loc="left")
    save(fig, "39", "fig-39-1-host-response-timeline")


# ---------------------------------------------------------------- Figure 39.2
def modulus_comparison():
    fig, ax = new_fig(6.8, 4.9)
    rows = [  # name, lo, hi, group colour
        ("cancellous bone", 0.1, 2, BONE_D),
        ("cortical bone", 15, 20, "#B8892E"),
        ("UHMWPE", 0.5, 1, COLORS[5]),
        ("PMMA bone cement", 2, 3, COLORS[5]),
        ("PEEK", 3.5, 3.7, COLORS[5]),
        ("CF-PEEK", 15, 20, COLORS[5]),
        ("porous tantalum", 1.5, 3, COLORS[3]),
        ("porous Ti lattice", 1, 20, COLORS[3]),
        ("Mg alloys", 44, 46, COLORS[0]),
        ("NiTi (austenite)", 40, 75, COLORS[0]),
        ("β-Ti alloys", 55, 85, COLORS[0]),
        ("Ti-6Al-4V", 110, 114, COLORS[0]),
        ("316L stainless", 190, 196, COLORS[0]),
        ("CoCrMo", 210, 230, COLORS[0]),
        ("3Y-TZP zirconia", 200, 210, COLORS[1]),
        ("alumina", 380, 400, COLORS[1]),
    ]
    n = len(rows)
    ax.axvspan(15, 20, color="#E9D3A6", alpha=0.6, lw=0, zorder=0)
    ax.text(17.3, n - 0.3, "cortical\nbone", ha="center", va="bottom", fontsize=7.5, color="#7A5A12")
    for k, (name, lo, hi, c) in enumerate(rows):
        y = n - 1 - k
        ax.barh(y, hi - lo, left=lo, height=0.62, color=c, ec=INK, lw=0.5, zorder=3)
    ax.set_yticks([n - 1 - k for k in range(n)])
    ax.set_yticklabels([r[0] for r in rows], fontsize=8.3)
    ax.set_xscale("log")
    ax.set_xlim(0.05, 500)
    ax.set_ylim(-0.6, n + 0.6)
    ax.set_xticks([0.1, 1, 10, 100])
    ax.set_xticklabels(["0.1", "1", "10", "100"])
    ax.set_xlabel("Young's modulus (GPa, log scale)")
    ax.tick_params(axis="y", length=0)
    shares = {"CF-PEEK": "73 %", "β-Ti alloys": "45 %", "Ti-6Al-4V": "31 %", "CoCrMo": "19 %"}
    for k, (name, lo, hi, c) in enumerate(rows):
        if name in shares:
            y = n - 1 - k
            ax.text(hi * 1.25, y, f"bone carries {shares[name]}", va="center", fontsize=7.8, color="#7A2E2E")
    ax.text(0.06, 1.0, "load share to bone in the\nworked example (stem 154 mm²,\nbone 439 mm², $E_b$ = 17 GPa)",
            fontsize=7.5, color="#7A2E2E", va="center")
    handles = [Line2D([], [], lw=6, color=c, label=l) for c, l in
               ((BONE_D, "bone"), (COLORS[5], "polymers, composite"), (COLORS[3], "porous metals"),
                (COLORS[0], "dense metals"), (COLORS[1], "ceramics"))]
    ax.legend(handles=handles, loc="upper right", fontsize=7.5, frameon=True, framealpha=0.95, edgecolor="none")
    save(fig, "39", "fig-39-2-modulus-comparison")


# ---------------------------------------------------------------- Figure 39.3
TOT = 94.0  # SiO2 + CaO + Na2O at constant 6 wt% P2O5


def _tern(s, c):
    """(SiO2, CaO) wt% -> plot xy; Na2O = TOT - s - c. CaO at left, Na2O at right, SiO2 at top."""
    n = TOT - s - c
    return np.array([(n + 0.5 * s) / TOT, s / TOT * np.sqrt(3) / 2])


def _smooth_region(ax, pts, **kw):
    P = np.array([_tern(s, c) for s, c in pts])
    P = np.vstack([P, P[:1]])
    tck, _ = splprep([P[:, 0], P[:, 1]], s=0, per=True)
    x, y = splev(np.linspace(0, 1, 300), tck)
    ax.fill(x, y, **kw)
    return x, y


def bioactive_glass_diagram():
    fig, ax = plt.subplots(figsize=(6.8, 5.2))
    ax.set_aspect("equal"); ax.axis("off")
    h = np.sqrt(3) / 2
    ax.set_xlim(-0.12, 1.36); ax.set_ylim(-0.12, h + 0.08)
    # region B: SiO2 > 60
    B = [_tern(60, 0), _tern(60, 34), _tern(TOT, 0)]
    ax.add_patch(Polygon([_tern(60, 34), _tern(TOT, 0), _tern(60, 0)], fc="#DCE6F0", ec="none"))
    # region D: CaO-rich, not glass forming
    D = [_tern(0, TOT), _tern(50, 44), _tern(42, 40), _tern(30, 38), _tern(0, 52)]
    ax.add_patch(Polygon(D, fc="#EDE3D3", ec="none"))
    # region C: SiO2 < 35 (rest of the low-silica field)
    C = [_tern(0, 52), _tern(30, 38), _tern(35, 30), _tern(35, 0), _tern(0, 0)]
    ax.add_patch(Polygon(C, fc="#F6DADA", ec="none"))
    # region A and inner E
    A = [(40, 30), (45, 32), (52, 27), (55.5, 22), (55, 17), (50, 15), (43, 20.5), (39.5, 26)]
    _smooth_region(ax, A, fc="#BFE3C6", ec="#2E7D46", lw=1.2)
    E = [(42, 26), (45, 28.2), (49, 25.5), (50, 22), (47, 20.5), (43, 22)]
    _smooth_region(ax, E, fc="#5BB475", ec="#1F5E32", lw=1.0, alpha=0.9)
    # grid
    for v in range(10, 91, 10):
        for (a1, a2) in (((v, 0), (v, TOT - v)), ((0, v), (TOT - v, v)), ((0, TOT - v - 0), (TOT - v, 0))):
            pass
    for v in np.arange(10, 91, 10):
        # constant SiO2
        p, q = _tern(v, 0), _tern(v, TOT - v)
        ax.plot([p[0], q[0]], [p[1], q[1]], color="0.82", lw=0.5, zorder=1)
        # constant CaO
        p, q = _tern(0, v), _tern(TOT - v, v)
        ax.plot([p[0], q[0]], [p[1], q[1]], color="0.82", lw=0.5, zorder=1)
        # constant Na2O
        n_ = v
        p, q = _tern(0, TOT - n_), _tern(TOT - n_, 0)
        ax.plot([p[0], q[0]], [p[1], q[1]], color="0.82", lw=0.5, zorder=1)
        # tick labels
        pl = _tern(v, TOT - v); ax.text(pl[0] - 0.015, pl[1], f"{v}", ha="right", va="center", fontsize=7, color="0.35")
        pc = _tern(0, v); ax.text(pc[0], pc[1] - 0.025, f"{v}", ha="center", va="top", fontsize=7, color="0.35")
        pn = _tern(v, 0) if False else _tern(TOT - n_, 0)
        ax.text(pn[0] + 0.015, pn[1], f"{n_}", ha="left", va="center", fontsize=7, color="0.35")
    tri = np.array([_tern(0, TOT), _tern(0, 0), _tern(TOT, 0), _tern(0, TOT)])
    ax.plot(tri[:, 0], tri[:, 1], color=INK, lw=1.2, zorder=4)
    ax.text(0.5, h + 0.03, "SiO$_2$", ha="center", va="bottom", fontsize=10)
    ax.text(-0.03, -0.04, "CaO", ha="right", va="top", fontsize=10)
    ax.text(1.03, -0.04, "Na$_2$O", ha="left", va="top", fontsize=10)
    ax.text(0.5, -0.085, "wt% (SiO$_2$ + CaO + Na$_2$O = 94; P$_2$O$_5$ fixed at 6 wt%)", ha="center",
            va="top", fontsize=8, color="0.3")
    # labels
    def lab(s, c, t, **kw):
        p = _tern(s, c); ax.text(p[0], p[1], t, ha="center", va="center", **kw)
    lab(66, 13.5, "B  bioinert\n(encapsulated)", fontsize=8.5)
    lab(17, 22, "C  resorbs\ntoo fast", fontsize=8.5)
    lab(14, 64, "D  not\nglass-forming", fontsize=8.5)
    p = _tern(54.5, 25); ax.annotate("A  bioactive:\nbonds to bone", xy=p, xytext=(0.93, 0.52), fontsize=8.5,
                                     color="#1F5E32", arrowprops=dict(arrowstyle="-", lw=0.7, color="#1F5E32"))
    p = _tern(48.5, 22.5); ax.annotate("E  also bonds to\nsoft tissue", xy=p, xytext=(0.93, 0.36), fontsize=8.5,
                                     color="#1F5E32", arrowprops=dict(arrowstyle="-", lw=0.7, color="#1F5E32"))
    p = _tern(45, 24.5)
    ax.plot(*p, "*", ms=11, color=COLORS[1], mec=INK, mew=0.5, zorder=6)
    ax.annotate("45S5 Bioglass\n(45 SiO$_2$, 24.5 CaO,\n24.5 Na$_2$O)", xy=p, xytext=(-0.11, 0.60), fontsize=8,

                arrowprops=dict(arrowstyle="-", lw=0.7), zorder=6)
    s_, c_, n_ = 72 * TOT / 95, 9 * TOT / 95, 14 * TOT / 95
    p = _tern(s_, c_)
    ax.plot(*p, "s", ms=6, color=COLORS[0], mec=INK, mew=0.5, zorder=6)
    ax.annotate("window glass\n(~72 SiO$_2$, 9 CaO, 14 Na$_2$O)", xy=p, xytext=(0.80, 0.72), fontsize=8,

                arrowprops=dict(arrowstyle="-", lw=0.7), zorder=6)
    save(fig, "39", "fig-39-3-bioactive-glass-diagram")


# ---------------------------------------------------------------- Figure 39.4
def polyester_degradation():
    fig = plt.figure(figsize=(6.8, 3.9))
    ax = fig.add_axes([0.08, 0.14, 0.40, 0.57])
    t = np.logspace(0, np.log10(260), 400)  # weeks
    data = [("PGA", 2, COLORS[3]), ("PLGA 50:50", 3, COLORS[1]), ("PDLLA", 8, COLORS[4]),
            ("PLLA", 25, COLORS[0]), ("PCL", 52, COLORS[2])]
    for name, th, c in data:
        y = np.exp(-np.log(2) * t / th)
        lab = f"{name}, $t_{{1/2}}$ = {th} wk" if name != "PCL" else "PCL, $t_{1/2}$ ≈ 1 yr"
        ax.semilogx(t, y, color=c, lw=1.9, label=lab)
        ax.plot(th, 0.5, "o", color=c, ms=4)
    ax.legend(fontsize=7.2, loc="lower left", bbox_to_anchor=(-0.02, 1.0), ncol=2, columnspacing=0.8,
              handlelength=1.5)

    ax.axhline(0.5, color="0.7", lw=0.6, ls=":")
    ax.set_xlim(1, 260)
    ax.set_ylim(0, 1.05)
    ax.set_xticks([1, 4, 13, 52, 104, 260])
    ax.set_xticklabels(["1 wk", "1 mo", "3 mo", "1 yr", "2 yr", "5 yr"], fontsize=8)
    ax.xaxis.set_minor_locator(plt.NullLocator())
    ax.set_xlabel("time in vivo (log scale)")
    ax.set_ylabel(r"$M_n/M_{n0}$")

    bx = fig.add_axes([0.58, 0.14, 0.40, 0.76])
    tm = np.linspace(0, 60, 600)  # months
    k = np.log(2) / 25 * 4.345     # per month
    Mn = 150 * np.exp(-k * tm)
    strength = 1 / (1 + np.exp((tm - 12) / 1.9))
    mass = np.where(tm < 24, 1.0, np.where(tm > 48, 0.0, 0.5 * (1 + np.cos(np.pi * (tm - 24) / 24))))
    bx.axvspan(0, 9, color="#DDEBDD", lw=0)
    bx.axvspan(17, 48, color="#F6E3D3", lw=0)
    bx.text(4.5, 1.08, "device holds\nload", ha="center", va="bottom", fontsize=7.5, color="#2E6B2E")
    bx.text(32.5, 1.08, "device present but weak", ha="center", va="bottom", fontsize=7.5, color="#8A4A10")
    bx.plot(tm, Mn / 150, color=COLORS[0], lw=2, label="$M_n$ (150 kg/mol at $t$ = 0)")
    bx.plot(tm, strength, color=COLORS[1], lw=2, label="strength")
    bx.plot(tm, mass, color=INK, lw=2, label="mass")
    t20 = np.log(150 / 20) / k
    bx.axhline(20 / 150, color=COLORS[0], ls=":", lw=0.9)
    bx.plot(t20, 20 / 150, "o", color=COLORS[0], ms=5)
    bx.annotate(f"$M_n$ = 20 kg/mol\nat {t20:.0f} months", xy=(t20, 20 / 150), xytext=(24, 0.32), fontsize=7.8,
                color=COLORS[0], arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[0]))
    bx.set_xlim(0, 60)
    bx.set_ylim(0, 1.25)
    bx.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    bx.set_xlabel("time (months)")
    bx.set_ylabel("fraction of initial value")
    bx.legend(fontsize=7.5, loc="center right", bbox_to_anchor=(1.0, 0.62))
    bx.set_title("(b) PLLA interference screw", fontsize=9, loc="left", y=1.0, pad=14)
    fig.text(0.08, 0.95, "(a) molar-mass loss, first-order hydrolysis", fontsize=9)

    save(fig, "39", "fig-39-4-polyester-degradation")


# ---------------------------------------------------------------- Figure 39.5
def _label(ax, xy, txt, xyt, ha="left", c=INK, fs=7.2):
    ax.annotate(txt, xy=xy, xytext=xyt, fontsize=fs, ha=ha, va="center", color=c,
                arrowprops=dict(arrowstyle="-", lw=0.6, color="0.3", shrinkA=1, shrinkB=0))


def hip_knee_materials():
    fig = plt.figure(figsize=(6.8, 5.4))
    ax = fig.add_axes([0.0, 0.0, 0.60, 0.95])
    ax.set_xlim(-6.6, 4.4); ax.set_ylim(-8.6, 4.4); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("(a) total hip replacement (cementless, coronal section)", fontsize=9, loc="left")
    hc = np.array([0.75, 0.65])
    rim1 = hc + 1.62 * np.array([np.cos(np.radians(-45)), np.sin(np.radians(-45))])
    rim2 = hc + 1.62 * np.array([np.cos(np.radians(135)), np.sin(np.radians(135))])
    # pelvis
    ax.add_patch(Polygon([(-1.5, 4.3), (3.6, 4.3), (3.6, 0.0), (3.0, -0.9), (2.3, -0.9), tuple(rim1),
                          tuple(rim2), (-0.9, 2.2), (-1.5, 2.5)], fc=BONE, ec=BONE_D, lw=1.0, zorder=1))
    ax.text(1.8, 3.5, "pelvis", fontsize=8, color="#6B5A2A")
    # femur and canal
    ax.add_patch(Polygon([(-2.1, -8.5), (-2.1, -3.2), (-2.4, -1.6), (-2.8, -0.3), (-2.4, 0.3), (-1.7, 0.0),
                          (-1.0, -0.45), (-0.2, -0.85), (0.4, -1.6), (0.6, -2.6), (0.5, -3.4), (0.5, -8.5)],
                         fc=BONE, ec=BONE_D, lw=1.0, zorder=1))
    ax.add_patch(Polygon([(-1.45, -8.5), (-1.45, -3.4), (-1.75, -2.0), (-1.65, -0.95), (-0.9, -0.62),
                          (-0.25, -1.05), (0.15, -2.2), (-0.15, -3.4), (-0.15, -8.5)],
                         fc="#F7EFE0", ec=BONE_D, lw=0.6, zorder=1))
    # stress-shielding zone: proximal medial cortex (calcar)
    ax.add_patch(Polygon([(-0.25, -1.05), (-0.2, -0.85), (0.4, -1.6), (0.6, -2.6), (0.5, -3.6), (-0.15, -3.6),
                          (-0.15, -3.4), (0.15, -2.2)], fc="#F2B8B8", ec="none", alpha=0.85, zorder=2))
    # cemented alternative: PMMA mantle outline (dashed)
    ax.plot([-1.55, -1.55, -1.1], [-3.0, -7.6, -8.15], color=COLORS[1], ls="--", lw=1.0, zorder=5)
    ax.plot([-0.05, -0.05, -0.5], [-3.0, -7.6, -8.15], color=COLORS[1], ls="--", lw=1.0, zorder=5)
    # stem
    stem = [(-1.12, -7.9), (-1.3, -3.2), (-1.5, -1.9), (-1.42, -1.0), (-0.9, -0.82), (-0.3, -1.25),
            (-0.08, -2.2), (-0.32, -3.2), (-0.48, -7.9), (-0.8, -8.15)]
    ax.add_patch(Polygon(stem, fc=TI, ec=INK, lw=0.8, zorder=4))
    ax.add_patch(Polygon([(-1.3, -3.2), (-1.5, -1.9), (-1.42, -1.0), (-0.9, -0.82), (-0.3, -1.25),
                          (-0.08, -2.2), (-0.32, -3.2)], fc="none", ec="0.35", hatch="xxxx", lw=0, zorder=5))
    # neck towards the head centre, taper inside head
    d = (hc - np.array([-0.75, -0.95])); d = d / np.linalg.norm(d); nrm = np.array([-d[1], d[0]])
    base = np.array([-0.75, -0.95])
    neck = [base + 0.28 * nrm, base - 0.28 * nrm, hc - 0.55 * d - 0.2 * nrm, hc - 0.55 * d + 0.2 * nrm]
    ax.add_patch(Polygon(neck, fc=TI, ec=INK, lw=0.8, zorder=4))
    # liner and shell (cup opens inferolaterally)
    ax.add_patch(Wedge(hc, 1.6, -45, 135, width=0.32, fc=TI, ec=INK, lw=0.7, hatch="....", zorder=3))
    ax.add_patch(Wedge(hc, 1.28, -45, 135, width=0.32, fc=PE, ec=INK, lw=0.7, zorder=3))
    for ang in (55, 95):
        a = np.radians(ang)
        p0 = hc + 1.6 * np.array([np.cos(a), np.sin(a)])
        p1 = hc + 2.5 * np.array([np.cos(a), np.sin(a)])
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color="0.25", lw=2.2, zorder=2)
    ax.add_patch(Circle(hc, 0.95, fc=COCR, ec=INK, lw=0.9, zorder=6))
    tp = [hc - 0.55 * d - 0.2 * nrm, hc - 0.55 * d + 0.2 * nrm, hc + 0.1 * d + 0.14 * nrm,
          hc + 0.1 * d - 0.14 * nrm]
    ax.add_patch(Polygon(tp, fc="#7E8E9C", ec=INK, lw=0.6, zorder=7))
    tc = hc - 0.9 * d
    ax.plot(*tc, "o", ms=8, mfc="none", mec=COLORS[1], mew=1.5, zorder=8)
    # osteolysis zones from wear particles
    for (x, y) in (tuple(rim2 + np.array([-0.25, 0.1])), tuple(rim1 + np.array([0.15, -0.2])), (-1.7, -1.6),
                   (0.05, -1.3)):
        ax.add_patch(Ellipse((x, y), 0.45, 0.3, fc="#B05C5C", ec="none", alpha=0.65, zorder=6))
    L = -6.5
    _label(ax, hc + 1.45 * np.array([np.cos(np.radians(120)), np.sin(np.radians(120))]),
           "shell: porous Ti / AM lattice\n+ screws (bone ingrowth)", (L, 3.7))
    _label(ax, hc + 1.12 * np.array([np.cos(np.radians(150)), np.sin(np.radians(150))]) + np.array([0.0, 0.0]),
           "liner: HXLPE or ceramic\n(low wear)", (L, 2.6))
    _label(ax, hc + np.array([-0.5, 0.55]), "head: CoCr or ZTA, 28–36 mm\n(hard, low wear)", (L, 1.5))
    _label(ax, tuple(rim2 + np.array([-0.25, 0.1])), "osteolysis: 0.1–1 µm PE\nparticles → aseptic loosening",
           (L, 0.5), c="#8B2E2E")
    _label(ax, (-1.4, -2.2), "proximal porous / HA\ncoating (fixation)", (L, -2.0))
    _label(ax, (-1.2, -5.2), "stem: Ti-6Al-4V\n(low modulus, fatigue)", (L, -4.6))
    _label(ax, (-1.55, -6.6), "cemented option:\nPMMA mantle (dashed)", (L, -6.4), c=COLORS[1])
    R = 1.5
    _label(ax, tuple(tc), "12/14 taper:\ntaper corrosion\n(fretting)", (R, -1.5), c=COLORS[1])
    _label(ax, (0.35, -2.9), "stress-shielding\nzone: proximal\nbone resorbs", (R, -3.8), c="#B03030")
    ax.text(0.7, -7.6, "femur", fontsize=8, color="#6B5A2A", ha="left")

    # (b) knee
    bx = fig.add_axes([0.61, 0.0, 0.39, 0.95])
    bx.set_xlim(-3.4, 3.6); bx.set_ylim(-8.6, 4.4); bx.set_aspect("equal"); bx.axis("off")
    bx.set_title("(b) total knee replacement (sagittal)", fontsize=9, loc="left")
    # femur
    bx.add_patch(Polygon([(-1.0, 4.3), (1.0, 4.3), (1.2, 1.6), (1.5, 0.6), (1.2, -0.1), (0.0, -0.45), (-1.1, -0.2),
                          (-1.5, 0.6), (-1.2, 1.6)], fc=BONE, ec=BONE_D, lw=1.0))
    # femoral component (CoCr) as thick curved shell
    th = np.linspace(np.radians(200), np.radians(380), 60)
    cx0, cy0, r1, r2 = 0.0, 0.55, 1.35, 1.65
    outer = np.c_[cx0 + r2 * np.cos(th), cy0 + 1.0 * r2 * np.sin(th)]
    inner = np.c_[cx0 + r1 * np.cos(th[::-1]), cy0 + 1.0 * r1 * np.sin(th[::-1])]
    bx.add_patch(Polygon(np.vstack([outer, inner]), fc=COCR, ec=INK, lw=0.8, zorder=3))
    # patella and button
    bx.add_patch(Ellipse((2.25, 1.3), 0.8, 1.6, fc=BONE, ec=BONE_D, lw=1.0))
    bx.add_patch(Ellipse((1.78, 1.2), 0.32, 0.9, fc=PE, ec=INK, lw=0.7, zorder=4))
    # tibial insert, tray, stem, tibia
    bx.add_patch(Polygon([(-1.6, -1.15), (-1.0, -0.95), (0.0, -1.2), (1.0, -0.95), (1.6, -1.15), (1.6, -1.75),
                          (-1.6, -1.75)], fc=PE, ec=INK, lw=0.8, zorder=3))
    bx.add_patch(Rectangle((-1.7, -2.05), 3.4, 0.3, fc=TI, ec=INK, lw=0.8, zorder=3))
    bx.add_patch(Polygon([(-0.3, -2.05), (0.3, -2.05), (0.2, -4.6), (-0.2, -4.6)], fc=TI, ec=INK, lw=0.8, zorder=3))
    bx.add_patch(Polygon([(-1.8, -2.05), (1.8, -2.05), (1.4, -3.4), (1.0, -8.5), (-1.0, -8.5), (-1.4, -3.4)],
                         fc=BONE, ec=BONE_D, lw=1.0, zorder=1))
    bx.text(0.35, -6.5, "tibia", fontsize=8, color="#6B5A2A")
    bx.text(-0.35, 3.3, "femur", fontsize=8, color="#6B5A2A")
    # wear sites
    for x in (-0.55, 0.55):
        bx.add_patch(Ellipse((x, -1.22), 0.5, 0.18, fc="#C0392B", ec="none", alpha=0.7, zorder=5))
    LL, RR = -3.35, 2.0
    _label(bx, (-1.45, 0.4), "femoral component:\ncast CoCr", (LL, 2.6))
    _label(bx, (-1.3, -1.45), "tibial insert:\nUHMWPE / HXLPE", (LL, -0.6))
    _label(bx, (-1.5, -1.9), "tibial tray:\nTi or CoCr", (LL, -2.6))
    _label(bx, (1.78, 1.6), "patella button:\nPE", (RR, 3.2))
    _label(bx, (0.55, -1.25), "wear sites:\ndelamination,\npitting (fatigue,\noxidised PE)", (RR, -1.4),
           c="#8B2E2E")
    save(fig, "39", "fig-39-5-hip-knee-materials")


# ---------------------------------------------------------------- Figure 39.6
def drug_release_profiles():
    fig, ax = new_fig(6.6, 4.7)
    t = np.linspace(0, 90, 900)  # days
    ax.plot(t, t / 90, color=COLORS[2], lw=2, label="reservoir (membrane): zero order")
    C0, Cs, ell = 200.0, 1.0, 10e-6
    for D, c, lab in ((1e-15, COLORS[0], r"matrix (Higuchi), $D=10^{-15}$ m$^2$/s"),
                      (1e-14, COLORS[5], r"matrix (Higuchi), $D=10^{-14}$ m$^2$/s")):
        f = np.sqrt(D * (2 * C0 - Cs) * Cs * t * 86400) / (C0 * ell)
        m = f <= 0.6
        m2 = (f > 0.6) & (f <= 1.0)
        ax.plot(t[m], f[m], color=c, lw=2, label=lab)
        ax.plot(t[m2], f[m2], color=c, lw=1.6, ls="--")
    for d, v in ((1, 0.09), (7, 0.25), (28, 0.49)):
        ax.plot(d, v, "o", color=COLORS[0], ms=4.5, zorder=5)
        ax.annotate(f"{v * 100:.0f} %", xy=(d, v), xytext=(d + 2.5, v - 0.06), fontsize=7.8, color=COLORS[0])
    ax.annotate("50 % at ≈3 days", xy=(2.9, 0.5), xytext=(13, 0.80), fontsize=7.8, color=COLORS[5],
                arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[5]))
    burst = 0.15 * (1 - np.exp(-t / 0.3))
    ero = 0.8 / (1 + np.exp(-(t - 40) / 6.0))
    ax.plot(t, burst + ero, color=COLORS[1], lw=2, label="PLGA microspheres: burst, lag, erosion")
    ax.text(3, 0.115, "burst", fontsize=7.5, color=COLORS[1], va="top")
    ax.text(21, 0.12, "lag", fontsize=7.5, color=COLORS[1])
    ax.text(47.5, 0.70, "erosion", fontsize=7.5, color=COLORS[1], ha="right")
    ax.text(62, 0.565, "dashed: beyond the\nHiguchi validity (>60 %)", fontsize=7, color="0.35")
    ax.set_xlim(0, 90)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel("time (days)")
    ax.set_ylabel("cumulative fraction released")
    ax.legend(fontsize=7.5, loc="lower left", bbox_to_anchor=(0.0, 1.01), ncol=2, columnspacing=1.0,
              handlelength=1.8)
    # inset: plasma concentration and therapeutic window
    ins = fig.add_axes([0.61, 0.21, 0.32, 0.22])

    tt = np.linspace(0, 4, 2000)
    conc = np.zeros_like(tt)
    for t0 in np.arange(0, 4, 1.0):
        conc += np.where(tt >= t0, 2.6 * np.exp(-(tt - t0) / 0.28) * (1 - np.exp(-(tt - t0) / 0.03)), 0)
    ins.axhspan(0.8, 1.6, color="#DDEBDD", lw=0)
    ins.text(2.5, 0.84, "therapeutic window", fontsize=6.5, ha="center", va="bottom", color="#2E6B2E")
    ins.plot(tt, conc, color=COLORS[1], lw=1.1, label="repeated bolus")
    ins.plot(tt, np.where(tt < 0.15, tt / 0.15 * 1.15, 1.15), color=COLORS[2], lw=1.6, label="controlled")
    ins.text(0.62, 2.3, "toxic", fontsize=6.5, color="0.4")
    ins.text(0.62, 0.15, "ineffective", fontsize=6.5, color="0.4")
    ins.set_xlim(0, 4); ins.set_ylim(0, 2.8)
    ins.set_xticks([0, 1, 2, 3, 4]); ins.set_yticks([])
    ins.tick_params(labelsize=6.5)
    ins.set_xlabel("time (days)", fontsize=7, labelpad=1)
    ins.set_ylabel("plasma conc.", fontsize=7, labelpad=1)
    ins.legend(fontsize=6.3, loc="upper right", frameon=True, framealpha=0.9, edgecolor="none")
    save(fig, "39", "fig-39-6-drug-release-profiles")


if __name__ == "__main__":
    host_response_timeline()
    modulus_comparison()
    bioactive_glass_diagram()
    polyester_degradation()
    hip_knee_materials()
    drug_release_profiles()
