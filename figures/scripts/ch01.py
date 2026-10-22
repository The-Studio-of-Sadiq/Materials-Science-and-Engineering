"""Figures for Chapter 1 — The Materials Discipline.

Run from the repository root:  python figures/scripts/ch01.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Polygon, Circle, Ellipse
from scipy.spatial import ConvexHull

BLUE, VERM, GREEN, PINK, ORANGE, SKY = COLORS[:6]
BROWN = "#8B5A2B"
RED = "#C0392B"
PURPLE = "#7B4FA0"
L10 = np.log10


# ---------------------------------------------------------------- Figure 1.1
def materials_ages():
    fig, ax = new_fig(6.8, 5.0)
    ticks = np.array([-10000, -5000, 0, 1000, 1500, 1800, 1900, 1950, 2000, 2025], float)
    tlab = ["10 000\nBCE", "5000\nBCE", "0", "1000", "1500", "1800", "1900", "1950", "2000", "2025"]

    def X(year):
        return np.interp(year, ticks, np.arange(len(ticks)))

    knots = np.array([-10000, -5000, -3000, -1200, 0, 1000, 1500, 1800, 1850, 1900, 1950, 1960,
                      1980, 2000, 2025], float)
    raw = {
        "natural materials": ([75, 62, 50, 42, 40, 40, 38, 33, 28, 22, 15, 14, 14, 15, 16], BROWN),
        "ceramics and glass": ([25, 35, 38, 35, 32, 30, 30, 30, 28, 25, 20, 18, 18, 19, 19], RED),
        "metals": ([0, 3, 12, 23, 28, 30, 32, 37, 44, 52, 58, 58, 47, 40, 35], BLUE),
        "polymers and elastomers": ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0.6, 6, 9, 14, 17, 18], GREEN),
        "composites": ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.4, 1.2, 4.5, 7, 9], PURPLE),
        "semiconductors": ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2, 0.8, 1.5, 2.0, 2.5], ORANGE),
    }
    yrs = np.concatenate([np.linspace(-10000, 1800, 300), np.linspace(1800, 2025, 400)])
    vals = np.array([np.interp(yrs, knots, v) for v, _ in raw.values()])
    vals = 100 * vals / vals.sum(0)
    x = X(yrs)
    base = np.zeros_like(x)
    centers = {}
    for (name, (_, col)), v in zip(raw.items(), vals):
        ax.fill_between(x, base, base + v, color=col, alpha=0.55, lw=0)
        ax.plot(x, base + v, color=col, lw=0.8)
        centers[name] = (base, base + v)
        base = base + v
    # class labels placed inside their bands
    PEL = "polymers,\nelastomers"
    lab_at = {"natural materials": (1.5, None), "ceramics and glass": (1.9, None), "metals": (4.0, None),
              PEL: (8.4, None), "composites": (8.55, None)}
    centers[PEL] = centers["polymers and elastomers"]
    raw[PEL] = raw["polymers and elastomers"]
    for name, (xx, _) in lab_at.items():
        lo, hi = centers[name]
        yy = (np.interp(xx, x, lo) + np.interp(xx, x, hi)) / 2
        col = raw[name][1]
        fs = 8.5 if name not in ("composites", PEL) else 7.5
        ax.text(xx, yy, name, ha="center", va="center", fontsize=fs, color="white" if name != "composites" else INK,
                weight="bold")
    lo, hi = centers["semiconductors"]
    ax.annotate("semi-\nconductors", xy=(8.9, (np.interp(8.9, x, lo) + np.interp(8.9, x, hi)) / 2),
                xytext=(9.12, 96), fontsize=7.5, color="#9A6A00", ha="left", va="center",
                arrowprops=dict(arrowstyle="-", color="#9A6A00", lw=0.7), annotation_clip=False)
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 100)
    ax.set_xticks(np.arange(len(ticks)))
    ax.set_xticklabels(tlab, fontsize=8)
    ax.set_ylabel("relative importance (%)")
    ax.set_xlabel("year (piecewise scale)")
    for k in range(1, len(ticks) - 1):
        ax.axvline(k, color="white", lw=0.5, alpha=0.6)
    # milestones
    ms = [(-3300, "bronze 3300 BCE"), (-1200, "iron 1200 BCE"), (1824, "Portland cement 1824"),
          (1856, "Bessemer 1856"), (1886, "Hall–Héroult 1886"), (1906.5, "age hardening 1906, Bakelite 1907"),
          (1947, "transistor 1947"), (1965, "carbon fibre 1960s"), (1982, "single-crystal blades 1980s"),
          (2004, "graphene 2004")]
    for yr, lab in ms:
        xx = X(yr)
        ax.plot([xx, xx], [100, 100.0], color=INK)
        ax.plot([xx, xx], [96, 100], color=INK, lw=0.8)
        ax.text(xx, 101, lab, rotation=90, ha="center", va="bottom", fontsize=7.3, color=INK,
                linespacing=1.0)
    save(fig, "01", "fig-1-1-materials-ages")


# ---------------------------------------------------------------- Figure 1.2
def tetrahedron():
    fig, ax = schematic(6.8, 5.2, xlim=(0, 13.6), ylim=(0, 10.4))
    V = {"Processing": np.array([1.9, 2.7]), "Structure": np.array([7.0, 2.0]),
         "Properties": np.array([8.0, 4.7]), "Performance": np.array([4.9, 8.4])}
    C = np.mean(list(V.values()), axis=0)
    ax.plot(*zip(V["Processing"], V["Properties"]), color="0.6", lw=1.0, ls=(0, (3, 2)))
    ax.plot(*zip(V["Structure"], V["Performance"]), color="0.45", lw=1.2)
    ax.add_patch(Polygon([V["Processing"], V["Structure"], V["Performance"]], fc="#EEF3F8", ec="none",
                         alpha=0.8, zorder=0))
    ax.add_patch(Polygon([V["Structure"], V["Properties"], V["Performance"]], fc="#DDE6F0", ec="none",
                         alpha=0.8, zorder=0))

    def edge(a, b, dashed=False, color=INK, rad=0.0):
        p0, p1 = V[a], V[b]
        d = (p1 - p0) / np.linalg.norm(p1 - p0)
        ax.add_patch(FancyArrowPatch(p0 + 0.45 * d, p1 - 0.45 * d, arrowstyle="-|>", mutation_scale=14,
                                     color=color, lw=1.8, ls="--" if dashed else "-",
                                     connectionstyle=f"arc3,rad={rad}", zorder=3))

    edge("Processing", "Structure")
    edge("Structure", "Properties")
    edge("Properties", "Performance")
    edge("Performance", "Processing", dashed=True, color=VERM, rad=0.25)
    ax.text(1.75, 6.1, "redesign", color=VERM, fontsize=9.5, style="italic", ha="center", rotation=60)
    for k, p in V.items():
        ax.plot(*zip(C, p), color="#B08A00", lw=0.9, ls=(0, (1.5, 1.5)), zorder=1)
    ax.add_patch(Circle(C, 0.55, fc="#FFE9A8", ec="#B08A00", lw=1.0, zorder=4))
    ax.add_patch(Circle(C + np.array([-0.18, 0.18]), 0.2, fc="white", ec="none", alpha=0.6, zorder=4))
    ax.text(C[0], C[1] - 0.7, "Characterization", ha="center", va="top", fontsize=8.5, weight="bold",
            color="#7A5E00", zorder=5)
    for k, p in V.items():
        ax.add_patch(Circle(p, 0.3, fc=INK, ec="none", zorder=4))
    lab = {"Processing": (0.1, 1.95), "Structure": (5.3, 1.25), "Properties": (8.7, 5.0),
           "Performance": (5.5, 9.25)}
    notes = {"Processing": "investment casting with grain\nselector; solution + ageing",
             "Structure": "single crystal, [001] along axis;\n65–70 vol % cuboidal γ′ ≈ 0.5 µm",
             "Properties": "creep rupture ~1000 h\nat ~1050 °C, 140 MPa",
             "Performance": "blade life > 20 000 h\nat turbine entry 1900 K"}
    for k, (lx, ly) in lab.items():
        ax.text(lx, ly, k, ha="left", va="center", fontsize=10.5, weight="bold", color=INK)
        ax.text(lx, ly - 0.38, notes[k], ha="left", va="top", fontsize=8, color="#444444", style="italic",
                linespacing=1.15)
    ax.text(0.1, 10.3, "Example: single-crystal\nturbine blade", fontsize=8.5, color="#444444", va="top")

    # inset: concrete beam tetrahedron
    bx0, by0, bw, bh = 9.0, 5.75, 4.5, 4.55
    ax.add_patch(Rectangle((bx0, by0), bw, bh, fc="white", ec="0.6", lw=0.8, zorder=0))
    ax.text(bx0 + 0.15, by0 + bh - 0.12, "Inset: concrete beam", fontsize=8, weight="bold", va="top")
    W = {"Pc": np.array([9.7, 7.1]), "St": np.array([11.9, 6.75]), "Pr": np.array([12.8, 8.0]),
         "Pf": np.array([10.9, 9.1])}
    ax.plot(*zip(W["Pc"], W["Pr"]), color="0.65", lw=0.8, ls=(0, (2, 2)))
    ax.plot(*zip(W["St"], W["Pf"]), color="0.55", lw=0.9)
    for a, b, col, ls in [("Pc", "St", INK, "-"), ("St", "Pr", INK, "-"), ("Pr", "Pf", INK, "-"),
                          ("Pf", "Pc", VERM, "--")]:
        p0, p1 = W[a], W[b]
        d = (p1 - p0) / np.linalg.norm(p1 - p0)
        ax.add_patch(FancyArrowPatch(p0 + 0.15 * d, p1 - 0.15 * d, arrowstyle="-|>", mutation_scale=9,
                                     color=col, lw=1.1, ls=ls))
    for p in W.values():
        ax.add_patch(Circle(p, 0.1, fc=INK, ec="none", zorder=4))
    fs = 7.0
    ax.text(9.15, 6.75, "mix design,\ncuring", fontsize=fs, ha="left", va="top")
    ax.text(13.4, 6.45, "C–S–H, porosity,\naggregate", fontsize=fs, ha="right", va="top")
    ax.text(13.4, 8.25, "40 MPa; low\nchloride diffusivity", fontsize=fs, ha="right", va="bottom")
    ax.text(11.1, 9.2, "100-year design life", fontsize=fs, ha="left", va="bottom")
    save(fig, "01", "fig-1-2-tetrahedron")


# ---------------------------------------------------------------- Figure 1.3
def length_time_scales():
    fig, ax = new_fig(6.8, 5.0)
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlim(1e-11, 1e2); ax.set_ylim(1e-15, 1e10)
    regions = [
        ("electronic structure / DFT", (1e-11, 1e-9), (1e-15, 1e-12), BLUE, (1.2e-11, 2.2e-15), "left", "bottom"),
        ("molecular\ndynamics", (1e-10, 1e-7), (1e-14, 1e-8), GREEN, (8e-8, 1.4e-14), "right", "bottom"),
        ("kinetic Monte Carlo,\ndislocation dynamics,\nphase field", (1e-8, 1e-4), (1e-9, 1e2), PINK,
         (8e-5, 1.5e-9), "right", "bottom"),
        ("crystal plasticity /\ncontinuum FEM", (1e-5, 1e2), (1e-3, 1e10), ORANGE, (8e1, 1.6e-3), "right", "bottom"),
    ]
    for lab, (x0, x1), (y0, y1), col, (tx, ty), ha, va in regions:
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fc=col, alpha=0.13, ec=col, lw=1.0))
        ax.text(tx, ty, lab, ha=ha, va=va, fontsize=8, color=col if col != ORANGE else "#9A6A00",
                weight="bold", linespacing=1.05)
    pts = [
        (2.5e-10, 1e-13, "atomic vibration\n10$^{-13}$ s at 0.25 nm", (2e-10, 2e-11), "left"),
        (1e-9, 3600, "C in ferrite, 20 °C:\n1 nm in 1 h", (1.5e-11, 1.5e5), "left"),
        (3.3e-7, 1200, "bake hardening:\n0.33 µm in 20 min, 180 °C", (1.4e-9, 4e-1), "left"),
        (3.4e-4, 14400, "carburizing: 0.34 mm\nin 4 h, 925 °C", (1.5e-6, 2e6), "left"),
    ]
    for x, y, lab, (tx, ty), ha in pts:
        ax.plot(x, y, "o", color=INK, ms=5, zorder=5)
        ax.annotate(lab, xy=(x, y), xytext=(tx, ty), fontsize=7.6, ha=ha, va="center",
                    arrowprops=dict(arrowstyle="-", color="0.35", lw=0.7))
    # precipitation ageing: 10–50 nm, 1–10 h
    ax.add_patch(Rectangle((1e-8, 3600), 4e-8, 32400, fc=INK, alpha=0.6, ec=INK))
    ax.annotate("precipitation ageing:\n10–50 nm, hours", xy=(3e-8, 2e4), xytext=(1.5e-11, 4e8), fontsize=7.6,
                ha="left", va="center", arrowprops=dict(arrowstyle="-", color="0.35", lw=0.7))
    # creep design life of power plant pipe: 1e5 h = 3.6e8 s, wall 30 mm to diameter ~0.5 m
    ax.plot([3e-2, 0.5], [3.6e8, 3.6e8], color=INK, lw=3.5, solid_capstyle="butt")
    ax.text(0.12, 1.5e8, "creep design life 10$^5$ h\n(power-plant pipe)", ha="center", va="top",
            fontsize=7.6)
    ax.plot([1, 100], [3.15e9, 3.15e9], color=INK, lw=3.5, solid_capstyle="butt")
    ax.text(0.7, 3.15e9, "concrete design life 100 years, 1–100 m", ha="right", va="center", fontsize=7.6)
    ax.set_xlabel("length (m)")
    ax.set_ylabel("time (s)")
    ax.set_xticks([10.0 ** k for k in range(-11, 3)])
    ax.set_xticklabels([f"$10^{{{k}}}$" if k % 2 == 1 else "" for k in range(-11, 3)])
    ax.set_yticks([10.0 ** k for k in range(-15, 11, 3)])
    # right-hand time labels
    ax2 = ax.twinx()
    ax2.set_yscale("log"); ax2.set_ylim(ax.get_ylim())
    tl = [(1e-15, "fs"), (1e-12, "ps"), (1e-9, "ns"), (1e-6, "µs"), (1e-3, "ms"), (1, "s"), (3600, "hour"),
          (3.156e7, "year"), (3.156e9, "century")]
    ax2.set_yticks([t for t, _ in tl]); ax2.set_yticklabels([s for _, s in tl], fontsize=8)
    ax2.minorticks_off()
    ax2.spines["right"].set_visible(True)
    ax.grid(True, which="major", lw=0.4, color="#E6E6E6")
    ax.set_axisbelow(True)
    save(fig, "01", "fig-1-3-length-time-scales")


# ---------------------------------------------------------------- Figure 1.4
def morse(x, U0, a):
    """Morse potential in reduced separation x = r/r0; a in units of 1/r0."""
    e = np.exp(-a * (x - 1))
    return U0 * ((1 - e) ** 2 - 1)


def morse_force(x, U0, a):
    e = np.exp(-a * (x - 1))
    return -2 * U0 * a * e * (1 - e)


def bond_energy_curves():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.8, 3.9))
    x = np.linspace(0.7, 2.5, 800)
    bonds = [("strong bond (e.g. W, SiC)\n$U_0$ ≈ 8 eV", 8.0, 5.0, BLUE),
             ("weak bond (e.g. Al, polymer\ninterchain), $U_0$ ≈ 1–3 eV", 2.0, 3.0, VERM)]
    for lab, U0, a, col in bonds:
        a1.plot(x, morse(x, U0, a), color=col)
        mids = []
        for f in (0.3, 0.6):
            s = np.sqrt(f)
            xl = 1 - np.log(1 + s) / a
            xr = 1 - np.log(1 - s) / a
            E = -U0 + f * U0
            a1.plot([xl, xr], [E, E], color=col, lw=0.9)
            mids.append(((xl + xr) / 2, E))
            a1.plot((xl + xr) / 2, E, "o", color=col, ms=4.5, zorder=5)
        a1.plot([1, mids[0][0], mids[1][0]], [-U0, mids[0][1], mids[1][1]], color=col, lw=0.8, ls=":")
    a1.axhline(0, color="0.5", lw=0.6)
    a1.axvline(1, color="0.6", lw=0.6, ls="--")
    a1.text(1.01, 1.2, "$r_0$", fontsize=9, color="0.3")
    a1.text(1.5, -7.6, bonds[0][0], color=BLUE, fontsize=7.8, va="center")
    a1.text(1.62, -2.75, bonds[1][0], color=VERM, fontsize=7.8, va="center")
    a1.annotate("mean spacing grows\n→ thermal expansion", xy=(1.23, -0.85), xytext=(1.5, 1.35), fontsize=7.8,
                ha="left", va="center", arrowprops=dict(arrowstyle="-", color="0.35", lw=0.7))
    a1.set_xlim(0.7, 2.5); a1.set_ylim(-9, 3)
    a1.set_xlabel("separation $r/r_0$")
    a1.set_ylabel("potential energy $U$ (eV)")
    a1.set_title("(a) bond energy", fontsize=10, loc="left")

    for lab, U0, a, col in bonds:
        F = morse_force(x, U0, a)
        a2.plot(x, F, color=col)
        xm = 1 + np.log(2) / a
        Fm = morse_force(xm, U0, a)
        a2.plot(xm, Fm, "o", color=col, ms=4.5)
    # tangents at r0 (both bonds); the steeper one is the stiffer bond
    for U0, a in ((8.0, 5.0), (2.0, 3.0)):
        S0 = 2 * U0 * a * a
        h = 9.0 / S0 * 2.2
        xt = np.array([1 - h, 1 + h])
        a2.plot(xt, -S0 * (xt - 1), color=INK, lw=1.0, ls="--", zorder=6)
    a2.annotate("slope at $r_0$: $S_0=d^2U/dr^2$\n→ $E\\approx S_0/r_0$", xy=(1.1, -2.0 * 2 * 9 * 0.1),
                xytext=(1.3, 12), fontsize=7.8, ha="left", va="center",
                arrowprops=dict(arrowstyle="-", color="0.35", lw=0.7))
    xm = 1 + np.log(2) / 5.0
    a2.annotate("ideal strength\n(force extremum)", xy=(xm, morse_force(xm, 8, 5)), xytext=(1.5, -20.5),
                fontsize=7.8, ha="left", va="center", arrowprops=dict(arrowstyle="-", color="0.35", lw=0.7))
    xm2 = 1 + np.log(2) / 3.0
    a2.annotate("", xy=(xm2, morse_force(xm2, 2, 3)), xytext=(1.6, -18.8),
                arrowprops=dict(arrowstyle="-", color="0.35", lw=0.7))
    a2.axhline(0, color="0.5", lw=0.6)
    a2.axvline(1, color="0.6", lw=0.6, ls="--")
    a2.text(1.08, 22, "repulsive, $F>0$", fontsize=7.8, color="0.35")
    a2.text(2.45, -6, "attractive (restoring), $F<0$", fontsize=7.8, color="0.35", ha="right")
    a2.set_xlim(0.7, 2.5); a2.set_ylim(-25, 25)
    a2.set_xlabel("separation $r/r_0$")
    a2.set_ylabel("force $F=-dU/dr$ (eV per $r_0$)")
    a2.set_title("(b) force", fontsize=10, loc="left")
    fig.tight_layout()
    save(fig, "01", "fig-1-4-bond-energy-curves")


# ---------------------------------------------------------------- Figure 1.5
def _log_ticks(ax, axis, lo, hi):
    ticks = list(range(lo, hi + 1))
    labels = [f"{10.0 ** t:g}" for t in ticks]
    minor = [L10(m * 10.0 ** t) for t in range(lo - 1, hi + 1) for m in range(2, 10)]
    if axis == "x":
        ax.set_xticks(ticks); ax.set_xticklabels(labels); ax.set_xticks(minor, minor=True)
    else:
        ax.set_yticks(ticks); ax.set_yticklabels(labels); ax.set_yticks(minor, minor=True)


def _hull(ax, pts, color, pad=0.08, alpha=0.16):
    pts = np.asarray(pts)
    ang = np.linspace(0, 2 * np.pi, 24, endpoint=False)
    cloud = np.vstack([pts + pad * np.c_[np.cos(a) * np.ones(len(pts)), np.sin(a) * np.ones(len(pts))]
                       for a in ang])
    h = ConvexHull(cloud)
    poly = cloud[h.vertices]
    ax.add_patch(Polygon(poly, closed=True, fc=color, alpha=alpha, lw=0))
    ax.add_patch(Polygon(poly, closed=True, fc="none", ec=color, lw=1.0))


def _ell(ax, rr, ee, color, alpha=0.16):
    xc, yc = (L10(rr[0]) + L10(rr[1])) / 2, (L10(ee[0]) + L10(ee[1])) / 2
    w, h = L10(rr[1]) - L10(rr[0]) + 0.1, L10(ee[1]) - L10(ee[0]) + 0.12
    ax.add_patch(Ellipse((xc, yc), w, h, fc=color, alpha=alpha, ec="none"))
    ax.add_patch(Ellipse((xc, yc), w, h, fc="none", ec=color, lw=1.0))


def modulus_density_chart():
    fig, ax = new_fig(6.8, 5.2)
    TEAL = "#2A7FB0"
    GREY = "#6E6E6E"
    _ell(ax, (0.02, 0.5), (1e-3, 1), ORANGE)
    _ell(ax, (0.9, 1.3), (1e-3, 0.1), PINK)
    _ell(ax, (0.9, 2.2), (0.2, 4), BLUE)
    _ell(ax, (2.2, 2.6), (60, 90), SKY)
    _ell(ax, (1.9, 2.7), (20, 70), GREY)
    # natural materials: hull around wood along/across grain, bamboo, bone, cork
    nat = {"wood ∥": [(0.35, 8), (0.8, 25), (0.5, 13)], "wood ⊥": [(0.35, 0.3), (0.8, 2)],
           "bamboo": [(0.6, 15), (0.8, 20)], "bone": [(1.9, 15), (2.0, 30)], "cork": [(0.1, 0.005), (0.24, 0.05)]}
    natp = np.array([[L10(r), L10(e)] for v in nat.values() for r, e in v])
    _hull(ax, natp, BROWN, pad=0.1)
    comp = np.array([[L10(r), L10(e)] for r, e in [(1.5, 50), (1.6, 220), (1.55, 60), (1.8, 15), (2.0, 40),
                                                     (1.9, 25), (1.5, 15)]])
    _hull(ax, comp, "#333333", pad=0.06, alpha=0.12)
    metals = {"Mg": (1.8, 45), "Al": (2.7, 70), "Ti": (4.4, 114), "steel": (7.85, 210), "Cu": (8.9, 120),
              "W": (19.3, 410)}
    cer = {"alumina": (3.9, 370), "SiC": (3.15, 410), "Si$_3$N$_4$": (3.2, 310), "diamond": (3.5, 1050)}
    _hull(ax, np.array([[L10(r), L10(e)] for r, e in metals.values()]), VERM, pad=0.07)
    _hull(ax, np.array([[L10(r), L10(e)] for r, e in cer.values()]), GREEN, pad=0.06)
    for n, (r, e) in metals.items():
        if n in ("steel", "Al", "Ti", "Mg"):
            continue
        ax.plot(L10(r), L10(e), "o", color=VERM, ms=3.5)
        ax.text(L10(r) + 0.04, L10(e) - 0.08, n, fontsize=7.3, ha="left", va="center", color="#8A3A00")
    for n, (r, e) in cer.items():
        ax.plot(L10(r), L10(e), "s", color=GREEN, ms=3.5)
    ax.text(L10(3.9) + 0.04, L10(370) - 0.02, "alumina", fontsize=7.0, ha="left", va="center", color="#00704f")
    ax.text(L10(3.15) - 0.04, L10(410) + 0.09, "SiC", fontsize=7.0, ha="right", va="center", color="#00704f")
    ax.text(L10(3.2) - 0.04, L10(310) - 0.03, "Si$_3$N$_4$", fontsize=7.0, ha="right", va="center", color="#00704f")
    ax.text(L10(3.5) + 0.05, L10(1050), "diamond", fontsize=7.0, ha="left", va="center", color="#00704f")
    # class labels
    lab = [("foams", 0.1, 0.03, "#9A6A00"), ("polymers", 1.4, 0.9, BLUE),
           ("natural\nmaterials", 0.3, 0.25, BROWN), ("composites", 0.95, 300, "#333333"),
           ("metals", 12, 35, VERM), ("technical\nceramics", 10, 1100, "#00704f"),
           ("concrete,\nstone", 2.8, 7, GREY)]
    for t, r, e, c in lab:
        ax.text(L10(r), L10(e), t, ha="center", va="center", fontsize=8, color=c, weight="bold", linespacing=1.0)
    ax.text(L10(1.08), L10(0.01), "elastomers", ha="center", va="center", fontsize=8, color=PINK, weight="bold",
            rotation=90)
    ax.text(L10(2.4), L10(100), "glasses", ha="center", va="bottom", fontsize=7.5, color=TEAL, weight="bold")
    # worked-example points
    wex = [("steel", 7.85, 210, (0.06, 0.1, "left")), ("Al alloy", 2.7, 70, (0.07, -0.09, "left")),
           ("Ti-6Al-4V", 4.43, 114, (0.0, 0.13, "center")), ("Mg alloy", 1.8, 45, (-0.06, -0.08, "right")),
           ("GFRP", 1.9, 25, (0.05, -0.1, "left")), ("CFRP q-i", 1.55, 60, (-0.06, 0.08, "right")),
           ("Douglas fir ∥", 0.50, 13, (0.05, -0.13, "left"))]
    for n, r, e, (dx, dy, ha) in wex:
        ax.plot(L10(r), L10(e), "*", color=INK, ms=8, mec="white", mew=0.4, zorder=6)
        ax.text(L10(r) + dx, L10(e) + dy, n, fontsize=7.3, ha=ha, va="center", zorder=6)
    ax.set_xlim(L10(0.01), L10(30)); ax.set_ylim(-4, L10(2000))
    _log_ticks(ax, "x", -2, 1)
    _log_ticks(ax, "y", -4, 3)
    ax.set_xlim(L10(0.01), L10(30)); ax.set_ylim(-4, L10(2000))
    # guide lines: a fan through a common point in the empty upper-left corner
    ax0, ay0 = L10(0.012), L10(0.6)
    xs = np.array([L10(0.01), L10(30)])
    fig.canvas.draw()
    for n, txt, xa, dy in ((1, r"$E/\rho$ (tie)", L10(0.03), 0.08), (2, r"$E^{1/2}/\rho$ (beam)", L10(0.05), 0.08),
                           (3, r"$E^{1/3}/\rho$ (panel)", L10(0.0205), 0.08)):
        ax.plot(xs, ay0 + n * (xs - ax0), ls="--", color="0.45", lw=0.9, zorder=2)
        p0 = ax.transData.transform((xa, ay0 + n * (xa - ax0)))
        p1 = ax.transData.transform((xa + 0.1, ay0 + n * (xa + 0.1 - ax0)))
        ang = np.degrees(np.arctan2(p1[1] - p0[1], p1[0] - p0[0]))
        ax.text(xa, ay0 + n * (xa - ax0) + dy, txt, fontsize=7.6, color="0.25", rotation=ang,
                rotation_mode="anchor", ha="left", va="bottom")
    xb = L10(0.2)
    yb = ay0 + 1 * (xb - ax0)
    ax.annotate("", xy=(xb - 0.32, yb + 0.55), xytext=(xb + 0.05, yb - 0.1),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.4, mutation_scale=12), zorder=7)
    ax.text(xb - 0.17, yb + 0.62, "search\nregion", fontsize=8.5, ha="left", va="bottom", weight="bold")
    ax.set_xlabel(r"density $\rho$ (g/cm$^3$)")
    ax.set_ylabel("Young's modulus $E$ (GPa)")
    save(fig, "01", "fig-1-5-modulus-density-chart")


# ---------------------------------------------------------------- Figure 1.6
def criticality_map():
    fig, ax = new_fig(6.4, 4.4)
    ax.add_patch(Rectangle((2.8, 1.0), 10 - 2.8, 4.0, fc=VERM, alpha=0.10, ec="none"))
    ax.plot([2.8, 2.8, 10], [5, 1.0, 1.0], color=VERM, lw=1.0, ls="--")
    ax.text(9.9, 4.93, "critical", color=VERM, fontsize=10, weight="bold", ha="right", va="top")
    pts = [("heavy rare earths", 6, 4.5, (0.15, 0.0, "left")), ("light rare earths", 5, 3.8, (0.0, -0.22, "center")),
           ("gallium", 4, 3.9, (-0.15, 0.0, "right")), ("magnesium", 7, 4.0, (0.15, 0.0, "left")),
           ("niobium", 6, 3.9, (0.15, -0.12, "left")), ("tungsten", 8, 1.3, (0.15, 0.0, "left")),
           ("cobalt", 6.5, 2.5, (0.15, 0.0, "left")), ("platinum-group metals", 6, 2.4, (-0.15, -0.05, "right")),
           ("lithium", 4, 1.9, (0.15, 0.0, "left")), ("natural graphite", 3, 1.8, (-0.12, -0.15, "left")),
           ("silicon metal", 5, 1.2, (-0.15, 0.0, "right")), ("titanium", 5, 1.3, (0.12, 0.1, "left")),
           ("bauxite", 5.5, 1.0, (0.15, -0.08, "left")), ("copper", 5.5, 0.3, (0.15, 0.0, "left")),
           ("nickel", 5, 0.5, (-0.15, 0.0, "right")), ("iron ore", 6.5, 0.6, (0.15, 0.0, "left")),
           ("limestone", 3, 0.2, (0.15, 0.0, "left"))]
    for n, x, y, (dx, dy, ha) in pts:
        crit = x > 2.8 and y >= 1.0
        ax.plot(x, y, "o", color=VERM if crit else BLUE, ms=5.5, zorder=5)
        ax.text(x + dx, y + dy, n, fontsize=7.8, ha=ha, va="center")
    ax.annotate("by-product metal\n(of alumina refining)", xy=(4, 3.9), xytext=(1.35, 3.0), fontsize=7.6,
                color="0.25", ha="center", arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
    ax.annotate("single-country supply", xy=(5.9, 4.5), xytext=(3.3, 4.75), fontsize=7.6, color="0.25",
                ha="left", va="center", arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
    for xy in [(5.95, 3.92), (5.03, 3.86)]:
        ax.annotate("", xy=xy, xytext=(5.0, 4.68), arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5)
    ax.set_xlabel("economic importance")
    ax.set_ylabel("supply risk")
    ax.text(0.1, 1.75, "indicative positions;\nschematic, in the style\nof EU criticality\nassessments",
            fontsize=7.3, color="0.4", va="top", ha="left")
    save(fig, "01", "fig-1-6-criticality-map")


if __name__ == "__main__":
    materials_ages()
    tetrahedron()
    length_time_scales()
    bond_energy_curves()
    modulus_density_chart()
    criticality_map()
