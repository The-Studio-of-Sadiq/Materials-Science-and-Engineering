"""Figures for Chapter 2 — Crystal Structures and Non-Crystalline Solids.

Run from the repository root:  python figures/scripts/ch02.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle, FancyArrowPatch, Arc, Wedge, Ellipse
from matplotlib.colors import to_rgb
from scipy.spatial import Voronoi, cKDTree

BLUE, VERM, GREEN, PINK, ORANGE, SKY = COLORS[:6]
GREY = "#9AA3AD"


# ====================================================================== helpers
def _light(c, f):
    r, g, b = to_rgb(c)
    return (r + (1 - r) * f, g + (1 - g) * f, b + (1 - b) * f)


class Scene:
    """Small orthographic 3D renderer on a 2D matplotlib axes (painter's algorithm)."""

    def __init__(self, ax, azim=25, elev=18):
        self.ax = ax
        p, t = np.radians(azim), np.radians(elev)
        self.d = np.array([np.cos(t) * np.cos(p), np.cos(t) * np.sin(p), np.sin(t)])
        self.e1 = np.array([-np.sin(p), np.cos(p), 0.0])
        self.e2 = np.cross(self.d, self.e1)
        self.items = []
        self.pts2 = []

    def P(self, p):
        p = np.asarray(p, float)
        xy = np.array([p @ self.e1, p @ self.e2])
        self.pts2.append(xy)
        return xy

    def Q(self, p):
        """Projection without registering the point for the axis limits."""
        p = np.asarray(p, float)
        return np.array([p @ self.e1, p @ self.e2])

    def depth(self, p):
        return float(np.asarray(p, float) @ self.d)

    def atom(self, p, r, color, lw=0.6, alpha=1.0, hollow=False, ls="-"):
        self.items.append((self.depth(p), "atom", (np.asarray(p, float), r, color, lw, alpha, hollow, ls)))
        xy = self.P(p)
        self.pts2.append(xy + r)
        self.pts2.append(xy - r)

    def line(self, p0, p1, color=INK, lw=1.0, ls="-", n=12, alpha=1.0, bias=0.0):
        p0, p1 = np.asarray(p0, float), np.asarray(p1, float)
        for k in range(n):
            a, b = p0 + (p1 - p0) * k / n, p0 + (p1 - p0) * (k + 1) / n
            self.items.append((self.depth((a + b) / 2) + bias, "line", (a, b, color, lw, ls, alpha)))
        self.P(p0); self.P(p1)

    def bond(self, p0, p1, color="0.55", lw=2.6):
        self.line(p0, p1, color=color, lw=lw, n=6)

    def poly(self, pts, fc, alpha=0.35, ec=None, lw=0.8, bias=0.0):
        pts = [np.asarray(p, float) for p in pts]
        dep = np.mean([self.depth(p) for p in pts]) + bias
        self.items.append((dep, "poly", (pts, fc, alpha, ec, lw)))
        for p in pts:
            self.P(p)

    def arrow(self, p0, p1, color=INK, lw=1.4, ms=11, bias=5.0):
        self.items.append((bias + max(self.depth(p0), self.depth(p1)), "arrow", (p0, p1, color, lw, ms)))
        self.P(p0); self.P(p1)

    def text(self, p, s, reg=True, **kw):
        self.items.append((1e6, "text", (p, s, kw)))
        if reg:
            self.P(p)

    def draw(self, pad=0.08):
        ax = self.ax
        self.items.sort(key=lambda t: t[0])
        z = 1
        for dep, kind, a in self.items:
            z += 0.001
            if kind == "atom":
                p, r, c, lw, al, hollow, ls = a
                xy = self.Q(p)
                if hollow:
                    ax.add_patch(Circle(xy, r, fc="none", ec=c, lw=lw, ls=ls, zorder=z))
                    continue
                ax.add_patch(Circle(xy, r, fc=c, ec="0.15", lw=lw, alpha=al, zorder=z))
                ax.add_patch(Circle(xy + np.array([-0.3, 0.3]) * r, 0.38 * r, fc=_light(c, 0.55),
                                    ec="none", alpha=0.8 * al, zorder=z + 0.0001))
            elif kind == "line":
                p0, p1, c, lw, ls, al = a
                q0, q1 = self.Q(p0), self.Q(p1)
                ax.plot([q0[0], q1[0]], [q0[1], q1[1]], color=c, lw=lw, ls=ls, alpha=al,
                        solid_capstyle="round", zorder=z)
            elif kind == "poly":
                pts, fc, al, ec, lw = a
                ax.add_patch(Polygon([self.Q(p) for p in pts], closed=True, fc=fc, alpha=al,
                                     ec=ec if ec else "none", lw=lw, zorder=z))
            elif kind == "arrow":
                p0, p1, c, lw, ms = a
                ax.annotate("", xy=self.Q(p1), xytext=self.Q(p0), zorder=z,
                            arrowprops=dict(arrowstyle="-|>", color=c, lw=lw, mutation_scale=ms,
                                            shrinkA=0, shrinkB=0))
            elif kind == "text":
                p, s, kw = a
                xy = self.Q(p)
                kw = dict(kw)
                kw.setdefault("ha", "center"); kw.setdefault("va", "center"); kw.setdefault("fontsize", 8.5)
                ax.text(xy[0], xy[1], s, zorder=1e3, **kw)
        P = np.array(self.pts2)
        lo, hi = P.min(0), P.max(0)
        ax.set_xlim(lo[0] - pad, hi[0] + pad)
        ax.set_ylim(lo[1] - pad, hi[1] + pad)
        ax.set_aspect("equal")
        ax.axis("off")


def cube_edges(sc, o=(0, 0, 0), L=(1, 1, 1), **kw):
    o = np.array(o, float)
    Lx, Ly, Lz = L
    V = [o + np.array([i * Lx, j * Ly, k * Lz]) for i in (0, 1) for j in (0, 1) for k in (0, 1)]
    for a in range(8):
        for b in range(a + 1, 8):
            d = V[b] - V[a]
            if np.count_nonzero(np.abs(d) > 1e-9) == 1:
                sc.line(V[a], V[b], **kw)


def corners():
    return [np.array([i, j, k], float) for i in (0, 1) for j in (0, 1) for k in (0, 1)]


def face_centres():
    out = []
    for ax_ in range(3):
        for v in (0, 1):
            p = np.full(3, 0.5); p[ax_] = v; out.append(p)
    return out


def in_cell(frac_list, tol=1e-6):
    """All lattice-translated copies of fractional positions that fall inside [0,1]^3."""
    out = []
    for f in frac_list:
        f = np.asarray(f, float) % 1.0
        for t in np.array(np.meshgrid([0, 1], [0, 1], [0, 1])).T.reshape(-1, 3):
            q = f + t
            if np.all(q < 1 + tol) and not any(np.allclose(q, o) for o in out):
                out.append(q)
    return out


FCC_T = [np.array(v, float) for v in [(0, 0, 0), (0, .5, .5), (.5, 0, .5), (.5, .5, 0)]]


def hexagon(a=1.0, z=0.0):
    return [np.array([a * np.cos(np.radians(60 * k)), a * np.sin(np.radians(60 * k)), z]) for k in range(6)]


def hex_prism(sc, a, c, **kw):
    hv = hexagon(a)
    for z in (0.0, c):
        for k in range(6):
            sc.line(hv[k] + [0, 0, z], hv[(k + 1) % 6] + [0, 0, z], **kw)
    for k in range(6):
        sc.line(hv[k], hv[k] + [0, 0, c], **kw)
    return hv


# ---------------------------------------------------------------- Figure 2.1
def metallic_structures():
    fig = plt.figure(figsize=(6.8, 4.9))
    gs = fig.add_gridspec(2, 6, height_ratios=[0.72, 1.0], hspace=0.18, wspace=0.05)
    top = [fig.add_subplot(gs[0, i]) for i in range(6)]
    C1, C2 = BLUE, ORANGE

    # BCC
    for k, hard in enumerate((True, False)):
        sc = Scene(top[k], azim=28, elev=17)
        cube_edges(sc, color=INK, lw=0.8)
        R = np.sqrt(3) / 4 if hard else 0.09
        if not hard:
            sc.line((0, 0, 0), (1, 1, 1), color=VERM, lw=1.2, ls="--", n=20)
        for p in corners():
            sc.atom(p, R, C1, alpha=1.0 if not hard else 0.95)
        sc.atom((0.5, 0.5, 0.5), R, C2)
        sc.draw(pad=0.03)
    # FCC
    for k, hard in enumerate((True, False)):
        sc = Scene(top[2 + k], azim=28, elev=17)
        cube_edges(sc, color=INK, lw=0.8)
        R = np.sqrt(2) / 4 if hard else 0.09
        if not hard:
            sc.poly([(1, 0, 0), (0, 1, 0), (0, 0, 1)], fc=GREEN, alpha=0.35, ec=GREEN, lw=1.0)
            sc.line((0, 0, 0), (1, 0, 1), color=VERM, lw=1.2, ls="--", n=20, bias=0.3)
        for p in corners():
            sc.atom(p, R, C1)
        for p in face_centres():
            sc.atom(p, R, C2)
        sc.draw(pad=0.03)
    # HCP
    a, c = 1.0, 1.633
    for k, hard in enumerate((True, False)):
        sc = Scene(top[4 + k], azim=20, elev=15)
        hv = hex_prism(sc, a, c, color=INK, lw=0.8)
        R = 0.5 if hard else 0.09
        for z in (0.0, c):
            for v in hv + [np.zeros(3)]:
                sc.atom(v + [0, 0, z], R, C1)
        for j in (0, 2, 4):
            cen = (hv[j] + hv[(j + 1) % 6]) / 3.0
            sc.atom(cen + [0, 0, c / 2], R, C2)
        if not hard:
            sc.text(hv[0] / 2 + hv[5] / 2 + np.array([0.15, -0.25, -0.05]), "$a$", fontsize=9)
            sc.text(hv[1] + np.array([0.12, 0.1, c / 2]), "$c$", fontsize=9)
        sc.draw(pad=0.03)
    heads = ["(a) BCC", "(b) FCC", "(c) HCP"]
    notes = ["$a=4R/\\sqrt{3}$\nCN 8, APF 0.68\nbody diagonal touches",
             "$a=2\\sqrt{2}R$\nCN 12, APF 0.74\n(111) plane shaded",
             "$c/a=1.633$ (ideal)\nCN 12, APF 0.74"]
    for i in range(3):
        top[2 * i].set_title(heads[i], fontsize=10, loc="left")
        top[2 * i].text(1.0, -0.12, notes[i], transform=top[2 * i].transAxes, ha="center", va="top",
                        fontsize=8.0)
    for i in range(3):
        top[2 * i].text(0.5, -0.01, "hard sphere", transform=top[2 * i].transAxes, fontsize=6.8, color="0.4",
                        ha="center", va="top")
        top[2 * i + 1].text(0.5, -0.01, "reduced sphere", transform=top[2 * i + 1].transAxes, fontsize=6.8,
                            color="0.4", ha="center", va="top")

    # ---- bottom row
    gsb = gs[1, :].subgridspec(1, 4, width_ratios=[1.15, 0.95, 1.0, 1.0], wspace=0.08)
    ax = fig.add_subplot(gsb[0])
    e1, e2 = np.array([1.0, 0.0]), np.array([0.5, np.sqrt(3) / 2])
    Rr = 0.5
    A = [i * e1 + j * e2 for i in range(-4, 8) for j in range(-1, 6)]
    A = [p for p in A if -0.05 <= p[0] <= 4.05 and -0.05 <= p[1] <= 3.5]
    for p in A:
        ax.add_patch(Circle(p, Rr, fc=_light(GREY, 0.35), ec="0.35", lw=0.5))
    Bo, Co = (e1 + e2) / 3.0, 2 * (e1 + e2) / 3.0
    for p in A:
        b = p + Bo; c_ = p + Co
        if b[0] < 4.0 and b[1] < 3.4:
            ax.plot(*b, "^", color=BLUE, ms=4.5)
        if c_[0] < 4.0 and c_[1] < 3.4:
            ax.plot(*c_, "v", color=VERM, ms=4.5)
    pA = min(A, key=lambda p: np.linalg.norm(p - np.array([1.0, 1.7])))
    ax.text(*pA, "A", ha="center", va="center", fontsize=10, weight="bold")
    ax.text(*(pA + Bo + np.array([0.0, 0.0])), "", fontsize=8)
    ax.annotate("B", xy=pA + Bo + e1, xytext=(4.5, 3.2), fontsize=10, weight="bold", color=BLUE,
                arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.7), annotation_clip=False)
    ax.annotate("C", xy=pA + Co + e1, xytext=(4.5, 2.4), fontsize=10, weight="bold", color=VERM,
                arrowprops=dict(arrowstyle="-", color=VERM, lw=0.7), annotation_clip=False)
    ax.set_xlim(-0.6, 5.0); ax.set_ylim(-0.7, 3.9); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("(d) close packing", fontsize=10, loc="left")
    ax.text(2.2, -0.75, "A = sphere centres;\nB (▲), C (▼) = the two sets\nof hollows", ha="center", va="top",
            fontsize=7.6)

    # stacking side views
    ax = fig.add_subplot(gsb[1])
    off = {"A": 0.0, "B": 1 / 3, "C": 2 / 3}
    col = {"A": GREY, "B": BLUE, "C": VERM}
    rr = 0.16
    dz = 0.36

    def stack(x0, seq):
        for k, L in enumerate(seq):
            for m in range(3):
                x = x0 + (m + off[L]) * 0.38
                ax.add_patch(Circle((x, k * dz), rr, fc=_light(col[L], 0.25), ec="0.25", lw=0.5))
            ax.text(x0 - 0.2, k * dz, L, ha="right", va="center", fontsize=8.5, weight="bold", color=col[L])

    stack(0.25, "ABCABC")
    stack(2.15, "ABABAB")
    ax.text(0.68, -0.4, "FCC\n…ABCABC…", ha="center", va="top", fontsize=8)
    ax.text(2.58, -0.4, "HCP\n…ABAB…", ha="center", va="top", fontsize=8)
    ax.set_xlim(-0.2, 3.3); ax.set_ylim(-1.15, 2.2); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("stacking", fontsize=9.5, loc="left")

    # (e) interstitial sites
    ax = fig.add_subplot(gsb[2])
    sc = Scene(ax, azim=28, elev=17)
    cube_edges(sc, color=INK, lw=0.8)
    lat = in_cell([t for t in FCC_T])
    for p in lat:
        sc.atom(p, 0.08, GREY)
    sc.atom((0.5, 0.5, 0.5), 0.06, VERM)
    # octahedron around body centre
    O = face_centres()
    for i in range(6):
        for j in range(i + 1, 6):
            if abs(np.linalg.norm(O[i] - O[j]) - np.sqrt(0.5)) < 1e-6:
                sc.line(O[i], O[j], color=VERM, lw=0.7, n=4, alpha=0.7)
    T = [np.array(v, float) for v in [(0, 0, 0), (0.5, 0.5, 0), (0.5, 0, 0.5), (0, 0.5, 0.5)]]
    for i in range(4):
        for j in range(i + 1, 4):
            sc.line(T[i], T[j], color=GREEN, lw=0.8, n=4)
    sc.atom((0.25, 0.25, 0.25), 0.033, GREEN)
    sc.draw(pad=0.03)
    ax.set_title("(e) FCC sites", fontsize=10, loc="left")
    ax.text(0.5, -0.02, "octahedral ½,½,½\n$r/R$ = 0.414", transform=ax.transAxes, ha="center", va="top", fontsize=7.4, color=VERM)
    ax.text(0.5, -0.2, "tetrahedral ¼,¼,¼\n$r/R$ = 0.225", transform=ax.transAxes, ha="center", va="top", fontsize=7.4, color="#007A5A")

    ax = fig.add_subplot(gsb[3])
    sc = Scene(ax, azim=28, elev=17)
    cube_edges(sc, color=INK, lw=0.8)
    for p in corners() + [np.array([0.5, 0.5, 0.5])]:
        sc.atom(p, 0.08, GREY)
    # octahedral site at face centre (1/2,1/2,0): flattened octahedron
    oc = np.array([0.5, 0.5, 0.0])
    sc.atom(oc, 0.0225, VERM)
    for v in [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]:
        sc.line(oc, v, color=VERM, lw=0.6, n=3, alpha=0.6)
    sc.line(oc, (0.5, 0.5, 0.5), color=VERM, lw=1.0, n=3)
    # tetrahedral site at (1/2,1/4,0)
    tc = np.array([0.5, 0.25, 0.0])
    sc.atom(tc, 0.042, GREEN)
    for v in [(0, 0, 0), (1, 0, 0), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5)]:
        if v[2] >= 0:
            sc.line(tc, v, color=GREEN, lw=0.8, n=3)
    sc.draw(pad=0.03)
    ax.set_title("BCC sites", fontsize=10, loc="left")
    ax.text(0.5, -0.02, "octahedral ½,½,0\n$r/R$ = 0.155", transform=ax.transAxes, ha="center", va="top", fontsize=7.4, color=VERM)
    ax.text(0.5, -0.2, "tetrahedral ½,¼,0\n$r/R$ = 0.291", transform=ax.transAxes, ha="center", va="top", fontsize=7.4, color="#007A5A")
    save(fig, "02", "fig-2-1-metallic-structures")


# ---------------------------------------------------------------- Figure 2.2
def octa_faces(cen, d):
    v = [cen + d * np.array(e, float) for e in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]
    faces = []
    for sx in (0, 1):
        for sy in (2, 3):
            for sz in (4, 5):
                faces.append([v[sx], v[sy], v[sz]])
    return v, faces


def _legend(ax, items, title=None, y=-0.02):
    h = [plt.Line2D([], [], marker="o", ls="", color=c, ms=6, mec="0.2", mew=0.5) for c, _ in items]
    ax.legend(h, [l for _, l in items], loc="upper center", bbox_to_anchor=(0.5, y), ncol=len(items),
              fontsize=7.6, handletextpad=0.1, columnspacing=0.6, title=title, title_fontsize=7.6,
              borderaxespad=0.0)


def spinel_sites(u=0.2624):
    """MgAl2O4, Fd-3m origin choice 2: Mg 8a, Al 16d, O 32e (u,u,u). Fractional coordinates."""
    Fc = [np.array(v, float) for v in [(0, 0, 0), (0, .5, .5), (.5, 0, .5), (.5, .5, 0)]]
    a8 = [(1 / 8, 1 / 8, 1 / 8), (7 / 8, 3 / 8, 3 / 8)]
    d16 = [(.5, .5, .5), (.25, .75, 0), (.75, 0, .25), (0, .25, .75)]
    x = u
    e32 = [(x, x, x), (-x + .75, -x + .25, x + .5), (-x + .25, x + .5, -x + .75), (x + .5, -x + .75, -x + .25),
           (-x, -x, -x), (x + .25, x + .75, -x + .5), (x + .75, -x + .5, x + .25), (-x + .5, x + .25, x + .75)]

    def expand(lst):
        out = []
        for p in lst:
            for t in Fc:
                q = (np.array(p) + t) % 1.0
                if not any(np.allclose(q, o, atol=1e-6) for o in out):
                    out.append(q)
        return out

    return expand(a8), expand(d16), expand(e32)


def _periodic_neighbours(cen, pts, cut):
    """Neighbours of cen among periodic images of pts (fractional, cubic cell) within cut."""
    out = []
    for p in pts:
        for t in np.array(np.meshgrid([-1, 0, 1], [-1, 0, 1], [-1, 0, 1])).T.reshape(-1, 3):
            q = p + t
            if np.linalg.norm(q - cen) < cut:
                out.append(q)
    return out


def ionic_covalent_structures():
    fig, axs = plt.subplots(2, 4, figsize=(6.8, 5.2))
    axs = axs.ravel()
    MG, OX, CS, CL, CA, F_, GA, AS = "#7BB661", "#D9473B", "#8E6BB8", "#5BAE5B", "#E0B040", "#88C9E8", "#4C9BD6", "#B36B2E"

    # (a) rock salt MgO (Mg on 4b so the MgO6 octahedron sits at the body centre)
    ax = axs[0]
    sc = Scene(ax, azim=24, elev=17)
    cube_edges(sc, color="0.45", lw=0.7)
    Opos = in_cell(FCC_T)
    Mpos = in_cell([t + np.array([.5, 0, 0]) for t in FCC_T])
    v, faces = octa_faces(np.array([.5, .5, .5]), 0.5)
    for f in faces:
        sc.poly(f, fc=MG, alpha=0.18)
    for p in Opos:
        sc.atom(p, 0.085, OX)
    for p in Mpos:
        sc.atom(p, 0.06, MG)
    sc.draw(pad=0.02)
    ax.set_title("(a) rock salt MgO", fontsize=9, loc="left")
    _legend(ax, [(MG, "Mg"), (OX, "O")], "$a$ = 0.421 nm; MgO$_6$ octahedron")

    # (b) CsCl
    ax = axs[1]
    sc = Scene(ax, azim=24, elev=17)
    cube_edges(sc, color="0.45", lw=0.7)
    for p in corners():
        sc.bond(p, (0.5, 0.5, 0.5), color="0.7", lw=1.6)
        sc.atom(p, 0.11, CL)
    sc.atom((0.5, 0.5, 0.5), 0.13, CS)
    sc.draw(pad=0.02)
    ax.set_title("(b) CsCl", fontsize=9, loc="left")
    _legend(ax, [(CS, "Cs"), (CL, "Cl")], "$a$ = 0.412 nm; simple cubic\nlattice + 2-atom basis")

    # (c) fluorite
    ax = axs[2]
    sc = Scene(ax, azim=24, elev=17)
    cube_edges(sc, color="0.45", lw=0.7)
    Cap = in_cell(FCC_T)
    Fp = [np.array([i, j, k]) * 0.5 + 0.25 for i in (0, 1) for j in (0, 1) for k in (0, 1)]
    cube_edges(sc, o=(0.25, 0.25, 0.25), L=(0.5, 0.5, 0.5), color=SKY, lw=1.0)
    for f in Fp:
        for c_ in Cap:
            if abs(np.linalg.norm(f - c_) - np.sqrt(3) / 4) < 1e-6:
                sc.bond(f, c_, color="0.72", lw=1.4)
    for p in Cap:
        sc.atom(p, 0.075, CA)
    for p in Fp:
        sc.atom(p, 0.06, F_)
    sc.atom((0.5, 0.5, 0.5), 0.07, VERM, hollow=True, lw=1.2, ls="--")
    sc.draw(pad=0.02)
    ax.set_title("(c) fluorite CaF$_2$, UO$_2$", fontsize=9, loc="left")
    ax.annotate("empty\noctahedral\nhole", xy=sc.Q((0.5, 0.5, 0.5)), xytext=(1.08, 1.06), textcoords="axes fraction",
                fontsize=7, color=VERM, ha="right", va="top", arrowprops=dict(arrowstyle="-", color=VERM, lw=0.6))
    _legend(ax, [(CA, "Ca/U"), (F_, "F/O")], "$a$ = 0.547 nm (UO$_2$)")

    # (d) zincblende GaAs
    ax = axs[3]
    sc = Scene(ax, azim=24, elev=17)
    cube_edges(sc, color="0.45", lw=0.7)
    Gp = in_cell(FCC_T)
    Ap = [p for p in in_cell([t + 0.25 for t in FCC_T]) if np.all(p < 1 - 1e-6)]
    for g in Gp:
        for s in Ap:
            if abs(np.linalg.norm(g - s) - np.sqrt(3) / 4) < 1e-6:
                sc.bond(g, s, color="0.65", lw=1.8)
    tet = [np.array(v, float) for v in [(0, 0, 0), (.5, .5, 0), (.5, 0, .5), (0, .5, .5)]]
    for i in range(4):
        for j in range(i + 1, 4):
            for k in range(j + 1, 4):
                sc.poly([tet[i], tet[j], tet[k]], fc=ORANGE, alpha=0.12)
    for p in Gp:
        sc.atom(p, 0.06, GA)
    for p in Ap:
        sc.atom(p, 0.06, AS)
    sc.draw(pad=0.02)
    ax.set_title("(d) zincblende GaAs", fontsize=9, loc="left")
    _legend(ax, [(GA, "Ga"), (AS, "As")], "$a$ = 0.565 nm\nsame atom on both sites =\ndiamond cubic (Si, 0.543 nm)")

    # (e) wurtzite GaN
    ax = axs[4]
    sc = Scene(ax, azim=12, elev=13)
    a, c, u = 0.319, 0.519, 0.377
    a1 = np.array([a, 0, 0]); a2 = np.array([-a / 2, a * np.sqrt(3) / 2, 0]); c3 = np.array([0, 0, c])
    basis = [((1 / 3, 2 / 3, 0), "Ga"), ((2 / 3, 1 / 3, 0.5), "Ga"), ((1 / 3, 2 / 3, u), "N"),
             ((2 / 3, 1 / 3, 0.5 + u), "N")]
    hv = hexagon(a)

    def inside(p, tol=1e-6):
        if p[2] < -tol or p[2] > c + tol:
            return False
        for k in range(6):
            n = np.array([np.cos(np.radians(60 * k + 30)), np.sin(np.radians(60 * k + 30))])
            if p[:2] @ n > a * np.sqrt(3) / 2 + tol:
                return False
        return True

    atoms = []
    for i in range(-3, 4):
        for j in range(-3, 4):
            for k in (-1, 0, 1):
                for f, sp in basis:
                    pos = (i + f[0]) * a1 + (j + f[1]) * a2 + (k + f[2]) * c3
                    if inside(pos) and not any(np.allclose(pos, q) for q, _ in atoms):
                        atoms.append((pos, sp))
    hex_prism(sc, a, c, color="0.45", lw=0.7)
    for i, (p, s) in enumerate(atoms):
        for q, t in atoms[i + 1:]:
            if s != t and np.linalg.norm(p - q) < u * c * 1.08:
                sc.bond(p, q, color="0.65", lw=1.6)
    for p, s in atoms:
        sc.atom(p, 0.026 if s == "Ga" else 0.02, GA if s == "Ga" else "#5BAE5B")
    xa = a * 1.3
    sc.arrow((0, -xa, 0.0), (0, -xa, c + 0.08), color=VERM, lw=1.6, ms=10, bias=50)
    sc.text((0, -xa - 0.05, c * 0.5), "polar\n$c$ axis", color=VERM, fontsize=7.5, ha="right")
    sc.draw(pad=0.02)
    ax.set_title("(e) wurtzite GaN", fontsize=9, loc="left")
    _legend(ax, [(GA, "Ga"), ("#5BAE5B", "N")], "$a$ = 0.319, $c$ = 0.519 nm")

    # (f) perovskite BaTiO3
    ax = axs[5]
    sc = Scene(ax, azim=24, elev=17)
    cube_edges(sc, color="0.45", lw=0.7)
    v, faces = octa_faces(np.array([.5, .5, .5]), 0.5)
    for f in faces:
        sc.poly(f, fc=SKY, alpha=0.22)
    for p in corners():
        sc.atom(p, 0.12, "#7A9A3A")
    sc.atom((0.5, 0.5, 0.5), 0.065, "#9AA3AD")
    for o in face_centres():
        sc.atom(o, 0.07, OX)
    sc.draw(pad=0.02)
    ax.set_title("(f) perovskite BaTiO$_3$", fontsize=9, loc="left")
    _legend(ax, [("#7A9A3A", "Ba"), ("#9AA3AD", "Ti"), (OX, "O")], "$a$ ≈ 0.40 nm; TiO$_6$ oct.,\nBa 12-fold")

    # (g) spinel MgAl2O4: one MgO4 tetrahedron and four AlO6 octahedra sharing its corners
    ax = axs[6]
    sc = Scene(ax, azim=30, elev=20)
    Mg8, Al16, O32 = spinel_sites()
    cen = np.array([1 / 8, 1 / 8, 1 / 8])
    nb = _periodic_neighbours(cen, O32, 0.27)
    assert len(nb) == 4, len(nb)
    for i in range(4):
        for j in range(i + 1, 4):
            for k in range(j + 1, 4):
                sc.poly([nb[i], nb[j], nb[k]], fc=ORANGE, alpha=0.75, ec="#8A5A00", lw=0.6)
    sc.atom(cen, 0.02, MG)
    used = []
    for o in nb:
        cands = _periodic_neighbours(o, Al16, 0.27)
        cands.sort(key=lambda q: -np.linalg.norm(q - cen))
        al = cands[0]
        used.append(al)
        on = np.array(_periodic_neighbours(al, O32, 0.27))
        assert len(on) == 6
        for i in range(6):
            for j in range(i + 1, 6):
                for k in range(j + 1, 6):
                    tri = [on[i], on[j], on[k]]
                    ds = [np.linalg.norm(tri[m] - tri[n]) for m in range(3) for n in range(m + 1, 3)]
                    if max(ds) < 0.40:
                        sc.poly(tri, fc=BLUE, alpha=0.28, ec="#1F4E79", lw=0.4)
        sc.atom(al, 0.02, "#5A6B7D")
    for o in nb:
        sc.atom(o, 0.022, OX)
    sc.draw(pad=0.02)
    ax.set_title("(g) spinel MgAl$_2$O$_4$", fontsize=9, loc="left")
    h = [Rectangle((0, 0), 1, 1, fc=ORANGE, alpha=0.75), Rectangle((0, 0), 1, 1, fc=BLUE, alpha=0.4)]
    ax.legend(h, ["MgO$_4$", "AlO$_6$"], loc="upper center", bbox_to_anchor=(0.5, -0.02), ncol=2, fontsize=7.6,
              title="$a$ = 0.808 nm; AlO$_6$ share\ncorners (red O) with MgO$_4$",
              title_fontsize=7.4, handlelength=1.0, columnspacing=0.6, borderaxespad=0.0)
    # (h) corundum: one layer of AlO6 octahedra seen down c, 1/3 of sites empty (honeycomb)
    ax = axs[7]
    e1, e2 = np.array([1.0, 0.0]), np.array([0.5, np.sqrt(3) / 2])
    s3 = 1 / np.sqrt(3)
    Opts = [i * e1 + j * e2 for i in range(-6, 8) for j in range(-1, 7)]
    Opts = [p for p in Opts if -0.2 < p[0] < 5.3 and -0.2 < p[1] < 4.4]
    sites = [i * e1 + j * e2 + (e1 + e2) / 3 for i in range(-6, 8) for j in range(-1, 7)]
    sites = [p for p in sites if 0.2 < p[0] < 5.0 and 0.2 < p[1] < 4.2]
    for p in sites:
        i = round((p - (e1 + e2) / 3) @ np.array([1, -1 / np.sqrt(3)]))
        j = round((p - (e1 + e2) / 3)[1] / (np.sqrt(3) / 2))
        empty = (i - j) % 3 == 0
        # octahedron seen down its 3-fold axis: two opposite triangles (hexagon outline)
        up = [p + s3 * np.array([np.cos(np.radians(90 + 120 * k)), np.sin(np.radians(90 + 120 * k))]) for k in range(3)]
        dn = [p + s3 * np.array([np.cos(np.radians(-90 + 120 * k)), np.sin(np.radians(-90 + 120 * k))]) for k in range(3)]
        if empty:
            ax.plot(*p, "o", ms=4.5, mfc="white", mec="0.3", mew=0.8, zorder=3)
        else:
            ax.add_patch(Polygon(dn, closed=True, fc=_light(BLUE, 0.55), ec="#1F4E79", lw=0.5, zorder=1))
            ax.add_patch(Polygon(up, closed=True, fc=_light(BLUE, 0.25), ec="#1F4E79", lw=0.5, zorder=2))
            ax.plot(*p, "o", ms=3.2, color="#5A6B7D", zorder=3)
    ax.set_xlim(0.0, 5.2); ax.set_ylim(0.0, 4.3); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("(h) corundum α-Al$_2$O$_3$", fontsize=9, loc="left")
    hh = [Polygon([[0, 0], [1, 0], [.5, .8]], fc=_light(BLUE, 0.3), ec="#1F4E79"),
          plt.Line2D([], [], marker="o", ls="", mfc="white", mec="0.3", ms=5)]
    ax.legend(hh, ["AlO$_6$ (edge-sharing)", "empty site"], loc="upper center", bbox_to_anchor=(0.5, -0.02),
              ncol=1, fontsize=7.4, title="layer seen down $c$; ⅓ of\noctahedral sites empty", title_fontsize=7.4,
              handlelength=1.0, borderaxespad=0.0)
    fig.subplots_adjust(hspace=0.75, wspace=0.12, left=0.01, right=0.99, top=0.95, bottom=0.17)
    save(fig, "02", "fig-2-2-ionic-covalent-structures")


# ---------------------------------------------------------------- Figure 2.3
def _honey(nx, ny):
    """Honeycomb vertices (bond length 1) with sublattice flag."""
    a = np.sqrt(3)
    a1 = np.array([a, 0.0]); a2 = np.array([a / 2, 1.5])
    P, S = [], []
    for i in range(-nx, nx + 1):
        for j in range(-ny, ny + 1):
            b = i * a1 + j * a2
            P.append(b); S.append(0)
            P.append(b + np.array([0, 1.0])); S.append(1)
    return np.array(P), np.array(S)


def _tets(ax, P, S, idx, framework=False, ox=0.0, oy=0.0, scale=1.0):
    """Draw corner-sharing SiO4 triangles (top view) for vertices idx of the honeycomb."""
    idx = list(idx)
    tree = cKDTree(P)
    sel = set(idx)
    for i in idx:
        nbr = [j for j in tree.query_ball_point(P[i], 1.05) if j != i]
        # corners at bond midpoints (bridging O sits exactly at a shared corner)
        corners_ = [(P[i] + P[j]) / 2 for j in nbr]
        tri = np.array([(c - P[i]) * 1.0 + P[i] for c in corners_])
        tri = (tri - [0, 0]) * scale + [ox, oy]
        fc = _light(BLUE, 0.45) if not framework else (_light(BLUE, 0.45) if S[i] == 0 else _light(BLUE, 0.1))
        ax.add_patch(Polygon(tri, closed=True, fc=fc, ec="#1F4E79", lw=0.8, zorder=1))
        cen = P[i] * scale + [ox, oy]
        ax.plot(*cen, "o", ms=2.2, color="#1F4E79", zorder=2)
        if not framework:
            ax.plot(*cen, "o", ms=4.4, mfc="none", mec=VERM, mew=0.9, zorder=3)
        for j, c in zip(nbr, corners_):
            cc = c * scale + [ox, oy]
            if j in sel:
                ax.plot(*cc, "o", ms=2.6, color="0.25", zorder=3)
            else:
                ax.plot(*cc, "o", ms=3.6 if not framework else 2.6, color=VERM if not framework else "0.25", zorder=3)


def silicate_units():
    fig = plt.figure(figsize=(6.8, 5.0))
    outer = fig.add_gridspec(1, 2, width_ratios=[2.15, 1.0], wspace=0.05)
    left = outer[0].subgridspec(3, 6, height_ratios=[0.8, 0.85, 1.35], hspace=0.45, wspace=0.15)
    P, S = _honey(8, 8)
    tree = cKDTree(P)
    o = int(np.argmin(np.linalg.norm(P - [0, 0], axis=1)))
    a = np.sqrt(3)
    j = [k for k in tree.query_ball_point(P[o], 1.05) if k != o][0]
    hexc = P[o] + np.array([a / 2, 0.5])
    ring = [i for i in range(len(P)) if abs(np.linalg.norm(P[i] - hexc) - 1.0) < 1e-6]
    ys = lambda lst: [i for i in range(len(P)) if any(abs(P[i, 1] - y) < 1e-6 for y in lst) and -3.6 < P[i, 0] < 3.6]
    chain = ys([0.0, -0.5])
    dbl = ys([0.0, -0.5, -1.5, -2.0])
    sheet = [i for i in range(len(P)) if np.linalg.norm(P[i] - hexc) < 2.9]
    panels = [("(a) isolated, $Q^0$", "Si:O = 1:4", [o], left[0, 0:2], False),
              ("(b) Si$_2$O$_7$, $Q^1$", "2:7", [o, j], left[0, 2:4], False),
              ("(c) 6-ring, $Q^2$", "1:3", ring, left[0, 4:6], False),
              ("(d) single chain, $Q^2$", "1:3", chain, left[1, 0:3], False),
              ("(e) double chain, $Q^2/Q^3$", "4:11", dbl, left[1, 3:6], False),
              ("(f) sheet, $Q^3$", "2:5", sheet, left[2, 0:3], False),
              ("(g) 3D framework, $Q^4$", "1:2", sheet, left[2, 3:6], True)]
    for title, ratio, idx, spec, fw in panels:
        ax = fig.add_subplot(spec)
        _tets(ax, P, S, idx, framework=fw)
        pts = P[idx]
        lo, hi = pts.min(0) - 0.9, pts.max(0) + 0.9
        if len(idx) <= 2:
            c = (lo + hi) / 2
            lo, hi = c - 1.6, c + 1.6
        ax.set_xlim(lo[0], hi[0]); ax.set_ylim(lo[1], hi[1])
        ax.set_aspect("equal", adjustable="datalim"); ax.axis("off")
        ax.set_title(title, fontsize=8.3, loc="left", pad=2)
        ax.text(0.0, -0.02, ("" if ratio.startswith("Si") else "Si:O = ") + ratio, transform=ax.transAxes,
                fontsize=7.8, color="0.3", va="top")
        if fw:
            ax.text(1.0, -0.13, "light/dark: apex up/down,\nshared with next sheet", transform=ax.transAxes,
                    fontsize=6.8, color="0.3", va="top", ha="right")
    h = [Polygon([[0, 0], [1, 0], [.5, .8]], fc=_light(BLUE, 0.45), ec="#1F4E79"),
         plt.Line2D([], [], marker="o", ls="", color="0.25", ms=4),
         plt.Line2D([], [], marker="o", ls="", color=VERM, ms=5),
         plt.Line2D([], [], marker="o", ls="", mfc="none", mec=VERM, ms=6)]
    fig.legend(h, ["SiO$_4$ tetrahedron (top view)", "bridging O", "non-bridging O",
                   "apical O above Si (non-bridging)"], loc="lower left", bbox_to_anchor=(0.02, -0.06),
               ncol=2, fontsize=7.4, handlelength=1.0, frameon=False)
    # (h) silica polymorphs
    ax = fig.add_subplot(outer[1])
    bands = [(0, 573, "α-quartz", "#CFE3F2"), (573, 867, "β-quartz", "#9CC6E6"), (867, 1470, "tridymite", "#BFE3D3"),
             (1470, 1713, "cristobalite", "#F6D9A8"), (1713, 1800, "liquid", "#F2B8A8")]
    for t0, t1, lab, c in bands:
        ax.add_patch(Rectangle((0, t0), 1, t1 - t0, fc=c, ec="0.3", lw=0.6))
        ax.text(0.5, (t0 + t1) / 2, lab, ha="center", va="center", fontsize=8.3)
    for T, lab, disp in [(573, "573 °C", True), (867, "867 °C", False), (1470, "1470 °C", False), (1713, "1713 °C", None)]:
        ax.text(-0.05, T, lab, ha="right", va="center", fontsize=7.6)
        if disp is True:
            ax.annotate("", xy=(1.18, T + 45), xytext=(1.18, T - 45),
                        arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=0.9, mutation_scale=7))
            ax.text(1.27, T, "displacive\n(fast)", fontsize=7, va="center")
        elif disp is False:
            ax.annotate("", xy=(1.18, T + 140), xytext=(1.18, T - 140),
                        arrowprops=dict(arrowstyle="<|-|>", color=VERM, lw=0.9, mutation_scale=7))
            ax.text(1.27, T, "reconstructive\n(sluggish)", fontsize=7, va="center", color=VERM)
    ax.set_xlim(-0.75, 2.4); ax.set_ylim(0, 1800)
    ax.axis("off")
    ax.text(-0.75, 1850, "(h) SiO$_2$ at 1 atm", fontsize=9, va="bottom")
    ax.annotate("", xy=(0.0, 1800), xytext=(0.0, 0), arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.8))
    ax.text(0.5, -60, "T increases upward\n(0–1800 °C)", fontsize=7, ha="center", va="top", color="0.35")
    dens = "density (g/cm³)\nquartz 2.65\ncristobalite 2.33\nfused silica 2.20\ncoesite 2.93 (HP)\nstishovite 4.29 (HP)"
    ax.text(1.27, 330, dens, fontsize=7, va="center", ha="left",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="0.6", lw=0.6))
    save(fig, "02", "fig-2-3-silicate-units")


# ---------------------------------------------------------------- Figure 2.4
def miller_indices():
    fig = plt.figure(figsize=(6.8, 6.4))
    gs = fig.add_gridspec(3, 12, height_ratios=[1.0, 1.05, 1.05], hspace=0.28, wspace=0.2)
    AZ, EL = 35, 20

    def axes_xyz(sc, L=1.0):
        o = np.zeros(3)
        for v, lab in [((L * 1.3, 0, 0), "$x$"), ((0, L * 1.3, 0), "$y$"), ((0, 0, L * 1.3), "$z$")]:
            sc.arrow(o, v, color="0.45", lw=0.8, ms=7, bias=-50)
            sc.text(np.array(v) * 1.12, lab, fontsize=8.5, color="0.3")

    planes = [("(100)", [(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 0, 1)], ((1, .5, .5), (1.7, .5, .5)), "[100]"),
              ("(110)", [(1, 0, 0), (0, 1, 0), (0, 1, 1), (1, 0, 1)], ((.5, .5, .5), (1.05, 1.05, .5)), "[110]"),
              ("(111)", [(1, 0, 0), (0, 1, 0), (0, 0, 1)], ((1 / 3, 1 / 3, 1 / 3), (.8, .8, .8)), "[111]")]
    for i, (name, pts, (n0, n1), dl) in enumerate(planes):
        ax = fig.add_subplot(gs[0, 3 * i:3 * i + 3])
        sc = Scene(ax, AZ, EL)
        cube_edges(sc, color=INK, lw=0.8)
        axes_xyz(sc)
        sc.poly(pts, fc=BLUE, alpha=0.35, ec=BLUE, lw=1.0)
        sc.arrow(n0, n1, color=VERM, lw=1.5, ms=9, bias=10)
        sc.text(np.array(n1) + np.array([0.0, 0.0, 0.15]), dl, color=VERM, fontsize=8.5)
        sc.draw(pad=0.05)
        ax.set_title(f"({'abc'[i]}) {name}", fontsize=9.5, loc="left")
    ax = fig.add_subplot(gs[0, 9:12])
    sc = Scene(ax, AZ, EL)
    cube_edges(sc, L=(1, 2, 1), color="0.6", lw=0.6, ls=":")
    cube_edges(sc, color=INK, lw=0.8)
    axes_xyz(sc)
    sc.poly([(1, 0, 0), (0, 2, 0), (0, 2, 1), (1, 0, 1)], fc=GREEN, alpha=0.35, ec=GREEN, lw=1.0)
    sc.text((1.0, 0.25, -0.2), "1", fontsize=8.5, color="#006B4E")
    sc.text((0, 2.15, -0.12), "2", fontsize=8.5, color="#006B4E")
    sc.draw(pad=0.05)
    ax.set_title("(d) (210)", fontsize=9.5, loc="left")
    ax.text(0.5, -0.02, "intercepts 1, 2, ∞\n→ 1, ½, 0 → (210)", transform=ax.transAxes, ha="center", va="top",
            fontsize=7.4)

    # middle row
    ax = fig.add_subplot(gs[1, 0:4])
    sc = Scene(ax, AZ, EL)
    cube_edges(sc, color=INK, lw=0.8)
    tri = [np.array(v, float) for v in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]
    sc.poly(tri, fc=GREEN, alpha=0.3, ec=GREEN, lw=1.0)
    for p in in_cell(FCC_T):
        if abs(p.sum() - 1) < 1e-6:
            sc.atom(p, 0.06, ORANGE)
    for (p0, p1, lab, off) in [((1, 0, 0), (0, 1, 0), r"$[\bar110]$", (0.05, 0.05, -0.17)),
                               ((0, 1, 0), (0, 0, 1), r"$[0\bar11]$", (-0.05, 0.12, 0.12)),
                               ((0, 0, 1), (1, 0, 0), r"$[10\bar1]$", (0.15, -0.1, 0.05))]:
        sc.arrow(p0, (np.array(p0) + 0.86 * (np.array(p1) - np.array(p0))), color=VERM, lw=1.4, ms=9, bias=20)
        sc.text((np.array(p0) + np.array(p1)) / 2 + np.array(off), lab, color=VERM, fontsize=8)
    sc.draw(pad=0.05)
    ax.set_title("(e) FCC (111), three ⟨110⟩", fontsize=9, loc="left")

    ax = fig.add_subplot(gs[1, 4:8])
    sc = Scene(ax, AZ, EL)
    cube_edges(sc, color=INK, lw=0.8)
    rect = [np.array(v, float) for v in [(1, 0, 0), (0, 1, 0), (0, 1, 1), (1, 0, 1)]]
    sc.poly(rect, fc=GREEN, alpha=0.3, ec=GREEN, lw=1.0)
    for p in rect + [np.array([.5, .5, .5])]:
        sc.atom(p, 0.06, ORANGE)
    sc.arrow((1, 0, 0), (0.07, 0.93, 0.93), color=VERM, lw=1.4, ms=9, bias=20)
    sc.arrow((0, 1, 0), (0.93, 0.07, 0.93), color=VERM, lw=1.4, ms=9, bias=20)
    sc.text((0.25, 0.75, 0.95), r"$[\bar111]$", color=VERM, fontsize=8)
    sc.text((0.85, 0.15, 1.05), r"$[1\bar11]$", color=VERM, fontsize=8)
    sc.draw(pad=0.05)
    ax.set_title("(f) BCC (110), two ⟨111⟩", fontsize=9, loc="left")

    ax = fig.add_subplot(gs[1, 8:12])
    sc = Scene(ax, AZ, EL)
    cube_edges(sc, color=INK, lw=0.8)
    o = np.zeros(3)
    sc.arrow(o, (1, 0, 0), color=BLUE, lw=1.6, ms=10, bias=10)
    sc.arrow(o, (1, 1, 1), color=VERM, lw=1.6, ms=10, bias=10)
    sc.text((1.0, -0.12, -0.12), "[100]", color=BLUE, fontsize=8.5)
    sc.text((1.0, 1.0, 1.15), "[111]", color=VERM, fontsize=8.5)
    u1 = np.array([1, 0, 0.0]); u2 = np.array([1, 1, 1.0]) / np.sqrt(3)
    w = u2 - (u2 @ u1) * u1; w /= np.linalg.norm(w)
    arc = [0.42 * (np.cos(t) * u1 + np.sin(t) * w) for t in np.linspace(0, np.arccos(u2 @ u1), 24)]
    for k in range(len(arc) - 1):
        sc.line(arc[k], arc[k + 1], color=INK, lw=1.0, n=1, bias=20)
    sc.text(0.62 * (u1 + u2) / np.linalg.norm(u1 + u2) + np.array([0.25, -0.2, -0.05]), "54.74°", fontsize=8)
    sc.draw(pad=0.05)
    ax.set_title("(g) angle [100]–[111]", fontsize=9, loc="left")

    # bottom row: hexagonal
    a, c = 1.0, 1.6
    hv = hexagon(a)
    specs = [("(h) basal (0001), axes", [h + [0, 0, c / 2] for h in hv], BLUE),
             ("(i) prism $(1\\bar100)$, $(11\\bar20)$", None, None),
             ("(j) pyramidal $(10\\bar11)$", [hv[0], hv[1], hv[2] + [0, 0, c], hv[5] + [0, 0, c]], "0.45")]
    for i, (title, pts, col) in enumerate(specs):
        ax = fig.add_subplot(gs[2, 4 * i:4 * i + 4])
        sc = Scene(ax, azim=(15 if i == 1 else -35), elev=18)
        hex_prism(sc, a, c, color=INK, lw=0.8)
        if i == 1:
            sc.poly([hv[0], hv[5], hv[5] + [0, 0, c], hv[0] + [0, 0, c]], fc=GREEN, alpha=0.4, ec=GREEN, lw=1.0)
            sc.poly([hv[0], hv[2], hv[2] + [0, 0, c], hv[0] + [0, 0, c]], fc=ORANGE, alpha=0.4, ec=ORANGE, lw=1.0)
            sc.text(hv[5] * 1.05 + np.array([0.35, 0, c * 0.5]), "$(1\\bar100)$", color="#006B4E", fontsize=8,
                    ha="left")
            sc.text((hv[0] + hv[2]) / 2 + np.array([-0.1, 0.0, c + 0.2]), "$(11\\bar20)$", color="#9A6A00",
                    fontsize=8)
        else:
            sc.poly(pts, fc=col, alpha=0.4, ec=col, lw=1.0)
        o = np.zeros(3)
        if i == 0:
            for k, lab in [(0, "$a_1$"), (2, "$a_2$"), (4, "$a_3$")]:
                sc.arrow(o, hv[k] * 0.98, color="0.25", lw=1.0, ms=8, bias=30)
                sc.text(hv[k] * 1.25, lab, fontsize=8.5, color="0.2")
            sc.arrow(o, (0, 0, c * 1.25), color=VERM, lw=1.3, ms=9, bias=40)
            sc.text((0.0, 0.25, c * 1.2), "$c$ = [0001]", fontsize=8.5, color=VERM, ha="left")
        if i == 2:
            sc.arrow(o, hv[0] * 1.0, color=VERM, lw=1.5, ms=9, bias=40)
            sc.text(hv[0] * 1.0 + np.array([0.25, -0.25, -0.15]), "$[2\\bar1\\bar10]$", fontsize=8.5, color=VERM)
        sc.draw(pad=0.1)
        ax.set_title(title, fontsize=9, loc="left")
    fig.text(0.5, 0.015, "Miller–Bravais $(hkil)$ with $i=-(h+k)$; $[2\\bar1\\bar10]$ is the $a_1$ axis, "
             "a close-packed ⟨11$\\bar2$0⟩ direction", ha="center", fontsize=8)
    save(fig, "02", "fig-2-4-miller-indices")


# ---------------------------------------------------------------- Figure 2.5
def honeycomb(nx, ny, d=1.0):
    a = d * np.sqrt(3)
    a1 = np.array([a, 0]); a2 = np.array([a / 2, a * np.sqrt(3) / 2])
    pts = []
    for i in range(-nx, nx):
        for j in range(-ny, ny):
            base = i * a1 + j * a2
            pts.append(base); pts.append(base + np.array([0, d]))
    return np.array(pts)


def bonds_of(P, d, tol=0.12):
    t = cKDTree(P)
    pairs = t.query_pairs(d * (1 + tol))
    return [(i, j) for i, j in pairs if np.linalg.norm(P[i] - P[j]) > d * (1 - tol)]


def crn(n_seed=420, box_=12.0, iters=40, rng=None):
    """Continuous random network: Lloyd-relaxed Voronoi edges (3-coordinated), spring-relaxed."""
    rng = rng or np.random.default_rng(3)
    S = rng.uniform(-box_, box_, (n_seed, 2))
    for _ in range(iters):
        vor = Voronoi(np.vstack([S, S + [2 * box_, 0], S - [2 * box_, 0], S + [0, 2 * box_], S - [0, 2 * box_]]))
        newS = []
        for k in range(len(S)):
            reg = vor.regions[vor.point_region[k]]
            if -1 in reg or len(reg) == 0:
                newS.append(S[k]); continue
            newS.append(vor.vertices[reg].mean(0))
        S = (np.array(newS) + box_) % (2 * box_) - box_
    vor = Voronoi(np.vstack([S + [i * 2 * box_, j * 2 * box_] for i in (-1, 0, 1) for j in (-1, 0, 1)]))
    V = vor.vertices
    E = [tuple(r) for r in vor.ridge_vertices if -1 not in r]
    keep = np.all(np.abs(V) < 10.0, axis=1)
    idx = -np.ones(len(V), int); idx[keep] = np.arange(keep.sum())
    V = V[keep].copy()
    E = np.array([(idx[i], idx[j]) for i, j in E if keep[i] and keep[j]])
    deg = np.bincount(E.ravel(), minlength=len(V))
    nbrs = [[] for _ in range(len(V))]
    for i, j in E:
        nbrs[i].append(j); nbrs[j].append(i)
    A2 = np.array([(a, b) for n in nbrs for k, a in enumerate(n) for b in n[k + 1:]])
    L0 = np.median(np.linalg.norm(V[E[:, 0]] - V[E[:, 1]], axis=1))
    free = deg == 3
    for _ in range(600):
        F = np.zeros_like(V)
        for pairs, target, w in ((E, L0, 1.0), (A2, np.sqrt(3) * L0, 0.3)):
            dv = V[pairs[:, 1]] - V[pairs[:, 0]]
            ln = np.linalg.norm(dv, axis=1)[:, None]
            f = w * (ln - target) * dv / ln
            np.add.at(F, pairs[:, 0], f); np.add.at(F, pairs[:, 1], -f)
        V[free] += 0.1 * F[free]
    return V, [tuple(e) for e in E]


def _ring_sizes(V, E, W):
    """Count ring sizes of a planar 3-coordinated network via Voronoi-free face walk."""
    nbrs = {}
    for i, j in E:
        nbrs.setdefault(i, []).append(j); nbrs.setdefault(j, []).append(i)
    rings = []
    seen = set()
    for i, j in E:
        for (u, v) in ((i, j), (j, i)):
            if (u, v) in seen:
                continue
            path = [u]; a, b = u, v
            ok = True
            for _ in range(12):
                seen.add((a, b)); path.append(b)
                if b == u:
                    break
                nb = nbrs.get(b, [])
                if len(nb) < 2:
                    ok = False; break
                d0 = V[a] - V[b]
                ang = [(np.arctan2(*(V[n] - V[b])[::-1]) - np.arctan2(*d0[::-1])) % (2 * np.pi) for n in nb]
                cand = [(t, n) for t, n in zip(ang, nb) if n != a]
                t, n = min(cand)
                a, b = b, n
            else:
                ok = False
            if ok and path[-1] == u and 4 <= len(path) - 1 <= 9:
                cen = V[path[:-1]].mean(0)
                if np.all(np.abs(cen) < W - 1):
                    rings.append((len(path) - 1, path[:-1]))
    return rings


def crystal_glass_rdf():
    fig = plt.figure(figsize=(6.8, 5.6))
    gs = fig.add_gridspec(2, 3, height_ratios=[1.15, 1.0], hspace=0.38, wspace=0.18)
    W = 6.5
    d = 1.0

    def frame(ax, title):
        ax.set_xlim(-W, W); ax.set_ylim(-W, W); ax.set_aspect("equal"); ax.axis("off")
        ax.add_patch(Rectangle((-W, -W), 2 * W, 2 * W, fc="none", ec="0.5", lw=0.8))
        ax.set_title(title, fontsize=9.5, loc="left")

    def draw_net(ax, P, E, col="0.35", ms=2.4):
        for i, j in E:
            if np.any(np.abs(P[i]) > W) or np.any(np.abs(P[j]) > W):
                continue
            ax.plot([P[i, 0], P[j, 0]], [P[i, 1], P[j, 1]], color="0.6", lw=0.8, zorder=1)
        m = np.all(np.abs(P) <= W, axis=1)
        ax.plot(P[m, 0], P[m, 1], "o", ms=ms, color=col, zorder=2)

    ax = fig.add_subplot(gs[0, 0])
    P = honeycomb(10, 10, d)
    draw_net(ax, P, bonds_of(P, d), col=BLUE)
    frame(ax, "(a) crystal")

    ax = fig.add_subplot(gs[0, 1])
    rng = np.random.default_rng(7)
    seeds = np.array([[-3.4, 3.2], [3.6, 3.8], [-3.6, -3.4], [3.4, -3.1]])
    angles = np.radians([0, 23, 41, 12])
    base = honeycomb(12, 12, d)
    allP, owner = [], []
    for g, (s, th) in enumerate(zip(seeds, angles)):
        R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
        Q = base @ R.T + s
        dist = np.linalg.norm(Q[:, None, :] - seeds[None, :, :], axis=2)
        srt = np.sort(dist, axis=1)
        keep = (np.argmin(dist, axis=1) == g) & ((srt[:, 1] - srt[:, 0]) > 0.45)
        allP.append(Q[keep]); owner += [g] * keep.sum()
    P = np.vstack(allP); owner = np.array(owner)
    E = [(i, j) for i, j in bonds_of(P, d, 0.1) if owner[i] == owner[j]]
    gb = []
    for _ in range(5000):
        q = rng.uniform(-W, W, 2)
        sd = np.sort(np.linalg.norm(seeds - q, axis=1))
        if sd[1] - sd[0] < 0.6 and np.min(np.linalg.norm(P - q, axis=1)) > 0.8 and \
                (len(gb) == 0 or np.min(np.linalg.norm(np.array(gb) - q, axis=1)) > 0.85):
            gb.append(q)
    gb = np.array(gb)
    draw_net(ax, P, E, col=BLUE)
    ax.plot(gb[:, 0], gb[:, 1], "o", ms=2.4, color=VERM, zorder=2)
    frame(ax, "(b) polycrystal")
    ax.annotate("grain boundary\n~0.5 nm", xy=(0.15, -5.2), xytext=(0.0, -W - 0.4), ha="center", va="top",
                fontsize=7.6, color=VERM, arrowprops=dict(arrowstyle="-", color=VERM, lw=0.7),
                annotation_clip=False)

    ax = fig.add_subplot(gs[0, 2])
    V, E = crn()
    L = np.array([np.linalg.norm(V[i] - V[j]) for i, j in E])
    V = V * (d / np.median(L))
    draw_net(ax, V, E, col=GREEN)
    rings = _ring_sizes(V, E, W)
    colr = {5: "#F2B8A8", 6: "#E6EEF5", 7: "#BFD8EE"}
    shown = {5: 0, 7: 0}
    for n, path in rings:
        if n in (5, 7) and shown[n] < 3:
            ax.add_patch(Polygon(V[path], closed=True, fc=colr[n], ec="none", zorder=0))
            cen = V[path].mean(0)
            ax.text(*cen, str(n), fontsize=7, ha="center", va="center", zorder=3)
            shown[n] += 1
    frame(ax, "(c) glass (random network)")
    ax.text(0, -W - 0.4, "3 neighbours each; rings of\n5 (red), 6 and 7 (blue) members", ha="center",
            va="top", fontsize=7.6)

    # g(r)
    big = honeycomb(14, 14, d)
    c0 = big[np.argmin(np.linalg.norm(big, axis=1))]
    r_sh = np.linalg.norm(big - c0, axis=1)
    r_sh = r_sh[(r_sh > 0.5) & (r_sh < 7)]
    rho = 2 / (np.sqrt(3) * d * np.sqrt(3) * d * np.sqrt(3) / 2)
    r = np.linspace(0.01, 5, 2500)

    def g_of(sig_fn):
        g = np.zeros_like(r)
        for rs in r_sh:
            s = sig_fn(rs)
            g += np.exp(-(r - rs) ** 2 / (2 * s * s)) / (np.sqrt(2 * np.pi) * s)
        return g / (2 * np.pi * r * rho)

    g_cr = g_of(lambda rs: 0.03)
    g_am = g_of(lambda rs: 0.045 if rs < 1.05 else 0.06 + 0.17 * (rs - 1.0))
    ax = fig.add_subplot(gs[1, 0:2])
    ax.plot(r, g_cr, color=BLUE, lw=0.9, label="crystal (sharp shells)")
    ax.plot(r, g_am, color=GREEN, lw=1.8, label="glass")
    ax.axhline(1, color="0.5", lw=0.7, ls=":")
    ax.set_xlim(0, 5); ax.set_ylim(0, 9)
    ax.set_xlabel(r"$r/d_{\mathrm{nn}}$"); ax.set_ylabel(r"$g(r)$")
    ax.legend(loc="upper right", fontsize=8)
    ax.annotate("glass: short-range\norder only",
                xy=(2.25, 0.85), xytext=(2.05, 3.0), fontsize=7.8, color="#006B4E", zorder=5,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.9),
                arrowprops=dict(arrowstyle="-", color="#006B4E", lw=0.7))
    ax.set_title("(d) pair distribution functions", fontsize=9.5, loc="left")

    # V-T
    ax = fig.add_subplot(gs[1, 2])
    Tm = 0.75
    T = np.linspace(0.05, 1.0, 600)
    aL, aS = 0.45, 0.15
    VL = lambda t: 1.0 + aL * (t - Tm)
    VC = lambda t: 1.0 - 0.17 + aS * (t - Tm)

    def glass(t, Tg, w=0.02):
        s = 0.5 * (1 + np.tanh((t - Tg) / w))
        slope = aS + (aL - aS) * s
        idx = np.argsort(t)[::-1]
        out = np.empty_like(t); v = VL(t[idx[0]]); prev = t[idx[0]]
        for k in idx:
            v += slope[k] * (t[k] - prev); prev = t[k]; out[k] = v
        return out

    tl = T[T >= Tm]
    ax.plot(tl, VL(tl), color=INK)
    tc = T[T <= Tm]
    ax.plot(tc, VC(tc), color=BLUE)
    ax.plot([Tm, Tm], [VC(Tm), VL(Tm)], color=BLUE, ls=":")
    for Tg, col, lab, xl in [(0.52, VERM, "glass (fast)", 0.07), (0.38, ORANGE, "glass (slow)", 0.17)]:
        g = glass(tc, Tg)
        ax.plot(tc, g, color=col)
        ax.text(xl, np.interp(xl, tc, g) + (0.025 if Tg > 0.5 else -0.015), lab, fontsize=7.4, color=col,
                va="bottom" if Tg > 0.5 else "top")
    ax.text(0.84, VL(0.84) + 0.04, "liquid", ha="center", va="bottom", fontsize=7.8)
    ax.text(0.6, VL(0.6) + 0.02, "supercooled\nliquid", ha="right", va="bottom", fontsize=7.6)
    ax.text(0.5, VC(0.5) - 0.02, "crystal", fontsize=7.8, color=BLUE, va="top")
    ax.set_ylim(0.6, 1.14); ax.set_xlim(0.05, 1.0)
    ax.set_xticks([0.38, 0.52, Tm])
    ax.set_xticklabels([r"$T_g^{\,s}$", r"$T_g^{\,f}$", r"$T_m$"], fontsize=8.5)
    ax.set_yticks([])
    ax.set_xlabel("temperature")
    ax.set_ylabel("specific volume")
    ax.set_title("(e) glass transition", fontsize=9.5, loc="left")
    save(fig, "02", "fig-2-5-crystal-glass-rdf")


# ---------------------------------------------------------------- Figure 2.6
def polymer_crystallinity():
    fig = plt.figure(figsize=(6.8, 3.0))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.05, 1.2, 0.95], wspace=0.12)
    # (a) PE unit cell down c
    ax = fig.add_subplot(gs[0])
    A, B = 0.741, 0.494
    ax.add_patch(Rectangle((0, 0), A, B, fc="#F4F7FA", ec=INK, lw=1.0))
    L = 0.085  # half projected length of zigzag (C atoms at +-0.04 nm across)

    def chain(x, y, ang):
        u = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
        p1, p2 = np.array([x, y]) + 0.0635 * u, np.array([x, y]) - 0.0635 * u
        ax.plot(*zip(p1, p2), color="0.3", lw=2.0, zorder=2)
        for p in (p1, p2):
            ax.add_patch(Circle(p, 0.025, fc="0.25", ec="none", zorder=3))
            nrm = np.array([-u[1], u[0]])
            for s in (1, -1):
                h = p + 0.045 * (s * nrm) + 0.03 * (u if p is p1 else -u)
                ax.plot(*zip(p, h), color="0.6", lw=0.8, zorder=1)
                ax.add_patch(Circle(h, 0.012, fc="white", ec="0.5", lw=0.5, zorder=2))

    for (x, y) in [(0, 0), (A, 0), (0, B), (A, B)]:
        chain(x, y, 42)
    chain(A / 2, B / 2, -42)
    ax.annotate("", xy=(A, -0.07), xytext=(0, -0.07), arrowprops=dict(arrowstyle="<|-|>", lw=0.8, color=INK,
                                                                      mutation_scale=7))
    ax.text(A / 2, -0.09, "$a$ = 0.741 nm", ha="center", va="top", fontsize=8)
    ax.annotate("", xy=(-0.08, B), xytext=(-0.08, 0), arrowprops=dict(arrowstyle="<|-|>", lw=0.8, color=INK,
                                                                      mutation_scale=7))
    ax.text(-0.14, B / 2, "$b$ = 0.494 nm", ha="right", va="center", fontsize=8, rotation=90)
    ax.text(A + 0.1, B / 2, "zigzag\nplanes\n≈ ±42°\nto $a$", fontsize=7, ha="left", va="center", color="0.3")
    # side view of a chain
    y0 = -0.42
    cz = 0.2547
    xs = np.arange(0, 6) * cz / 2
    ys = y0 + np.where(np.arange(6) % 2 == 0, 0.0, 0.042 * 2)
    ax.plot(xs + 0.1, ys, color="0.3", lw=1.8)
    for x, y in zip(xs + 0.1, ys):
        ax.add_patch(Circle((x, y), 0.022, fc="0.25", ec="none", zorder=3))
    ax.annotate("", xy=(0.1 + cz, y0 - 0.06), xytext=(0.1, y0 - 0.06),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, color=VERM, mutation_scale=7))
    ax.text(0.1 + cz / 2, y0 - 0.08, "$c$ = 0.2547 nm", color=VERM, ha="center", va="top", fontsize=8)
    ax.text(0.85, y0 + 0.04, "side view\n(chain axis $c$ →)", fontsize=7, va="center", color="0.3")
    ax.set_xlim(-0.3, 1.2); ax.set_ylim(-0.62, 0.62)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("(a) unit cell, down $c$", fontsize=9.5, loc="left")

    # (b) lamellae
    ax = fig.add_subplot(gs[1])
    rng = np.random.default_rng(4)
    lam = [(0.0, 1.5), (2.5, 4.0), (5.0, 6.5)]   # crystal layers (y ranges) in units of ~10 nm
    for y0_, y1_ in lam:
        ax.add_patch(Rectangle((0, y0_), 6, y1_ - y0_, fc="#DCE9F5", ec="none"))
        for x in np.arange(0.25, 6, 0.3):
            ax.plot([x, x], [y0_, y1_], color=BLUE, lw=0.9)
        # folds (loops) at surfaces
        for x in np.arange(0.25, 5.8, 0.6):
            for yy, s in ((y1_, 1), (y0_, -1)):
                th = np.linspace(0, np.pi, 20)
                ax.plot(x + 0.15 - 0.15 * np.cos(th), yy + s * 0.12 * np.sin(th), color=BLUE, lw=0.9)
    # amorphous chains between lamellae
    for yA, yB in ((1.5, 2.5), (4.0, 5.0)):
        for k in range(7):
            x = rng.uniform(0.3, 5.7)
            t = np.linspace(0, 1, 40)
            px = x + 0.35 * np.sin(6 * t + rng.uniform(0, 6)) + rng.normal(0, 0.03, 40).cumsum() * 0.3
            py = yA + 0.15 + (yB - yA - 0.3) * (0.5 + 0.45 * np.sin(5 * t + rng.uniform(0, 6)))
            ax.plot(np.clip(px, 0.05, 5.95), py, color="0.55", lw=0.7)
    # tie molecule
    t = np.linspace(0, 1, 60)
    ax.plot(3.25 + 0.3 * np.sin(9 * t), 1.5 + t * 1.0, color=VERM, lw=1.6)
    ax.annotate("tie molecule", xy=(3.5, 2.0), xytext=(6.2, 2.15), fontsize=7.6, color=VERM, va="center",
                arrowprops=dict(arrowstyle="-", color=VERM, lw=0.7), annotation_clip=False)
    # cilium
    ax.plot(1.15 + 0.15 * np.sin(np.linspace(0, 8, 30)), np.linspace(4.0, 4.65, 30), color=GREEN, lw=1.6)
    ax.annotate("cilium", xy=(1.3, 4.6), xytext=(6.2, 4.6), fontsize=7.6, color="#006B4E", va="center",
                arrowprops=dict(arrowstyle="-", color="#006B4E", lw=0.7), annotation_clip=False)
    ax.annotate("loop (fold)", xy=(4.4, 6.6), xytext=(6.2, 6.6), fontsize=7.6, color=BLUE, va="center",
                arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.7), annotation_clip=False)
    ax.annotate("", xy=(-0.15, 4.0), xytext=(-0.15, 2.5), arrowprops=dict(arrowstyle="<|-|>", lw=0.8,
                                                                          mutation_scale=7))
    ax.text(-0.35, 3.25, "lamella\n10–20 nm", ha="right", va="center", fontsize=7.6)
    ax.annotate("", xy=(-0.15, 5.0), xytext=(-0.15, 4.0), arrowprops=dict(arrowstyle="<|-|>", lw=0.8,
                                                                          mutation_scale=7, color="0.45"))
    ax.text(-0.35, 4.6, "amorphous\n5–10 nm", ha="right", va="center", fontsize=7.6, color="0.35")
    ax.set_xlim(-2.4, 7.6); ax.set_ylim(-0.3, 7.0); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("(b) chain-folded lamellae", fontsize=9.5, loc="left")

    # (c) spherulite
    ax = fig.add_subplot(gs[2])
    rng = np.random.default_rng(11)
    R = 1.0
    for k in range(70):
        th = 2 * np.pi * k / 70 + rng.normal(0, 0.02)
        r = np.linspace(0.05, R * rng.uniform(0.9, 1.0), 30)
        wob = 0.05 * np.sin(r * 12 + k)
        ax.plot((r) * np.cos(th + wob * 0.3), (r) * np.sin(th + wob * 0.3), color=BLUE, lw=0.7)
        if k % 3 == 0:
            r0 = rng.uniform(0.35, 0.6)
            r2 = np.linspace(r0, R * 0.95, 15)
            ax.plot(r2 * np.cos(th + 0.04 + (r2 - r0) * 0.08), r2 * np.sin(th + 0.04 + (r2 - r0) * 0.08),
                    color=BLUE, lw=0.5)
    ax.add_patch(Circle((0, 0), 0.06, fc=VERM, ec="none", zorder=4))
    ax.annotate("nucleus", xy=(0.04, -0.04), xytext=(0.75, -1.3), fontsize=7.6, color=VERM,
                arrowprops=dict(arrowstyle="-", color=VERM, lw=0.7))
    ax.text(0, 1.12, "radiating lamellar fibrils", ha="center", fontsize=7.6)
    # Maltese cross inset
    ins = ax.inset_axes([-0.02, -0.02, 0.33, 0.33])
    ins.add_patch(Circle((0, 0), 1, fc="#F5E6A8", ec="0.4", lw=0.6))
    for a0 in (0, 90, 180, 270):
        ins.add_patch(Wedge((0, 0), 1, a0 - 12, a0 + 12, fc="0.1", ec="none"))
    ins.set_xlim(-1.1, 1.1); ins.set_ylim(-1.1, 1.1); ins.set_aspect("equal"); ins.axis("off")
    ins.text(0, -1.2, "crossed polars:\nMaltese cross", ha="center", va="top", fontsize=6.6)
    ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.45, 1.3); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("(c) spherulite, 1–100 µm", fontsize=9.5, loc="left")
    fig.text(0.5, -0.02, "scale:  (a) ~1 nm     →     (b) ~10–100 nm     →     (c) ~10 µm", ha="center", fontsize=8,
             color="0.3")
    save(fig, "02", "fig-2-6-polymer-crystallinity")


if __name__ == "__main__":
    metallic_structures()
    ionic_covalent_structures()
    silicate_units()
    miller_indices()
    crystal_glass_rdf()
    polymer_crystallinity()
