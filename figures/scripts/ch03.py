"""Figures for Chapter 3 — Symmetry and Space Groups.

Run from the repository root:  python figures/scripts/ch03.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle, FancyArrowPatch, Arc, Wedge, Ellipse
from matplotlib.colors import to_rgb

BLUE, VERM, GREEN, PINK, ORANGE, SKY = COLORS[:6]
GREY = "#9AA3AD"
TAU = (1 + np.sqrt(5)) / 2


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
                p, r, c, lw, al, hollow, ls = a[:7]
                half = a[7] if len(a) > 7 else None
                xy = self.Q(p)
                if hollow:
                    ax.add_patch(Circle(xy, r, fc="none", ec=c, lw=lw, ls=ls, zorder=z))
                    continue
                ax.add_patch(Circle(xy, r, fc=c, ec="0.15", lw=lw, alpha=al, zorder=z))
                if half is not None:
                    ax.add_patch(Wedge(xy, r, 90, 270, fc=half, ec="0.15", lw=lw, zorder=z + 0.00005))
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



class Scene3(Scene):
    """Scene with an extra two-colour ('mixed occupancy') atom."""

    def split(self, p, r, c1, c2):
        self.items.append((self.depth(p), "atom", (np.asarray(p, float), r, c1, 0.6, 1.0, False, "-", c2)))
        xy = self.P(p)
        self.pts2.append(xy + r); self.pts2.append(xy - r)


def cube_edges(sc, o=(0, 0, 0), L=(1, 1, 1), **kw):
    o = np.array(o, float)
    Lx, Ly, Lz = L
    V = [o + np.array([i * Lx, j * Ly, k * Lz]) for i in (0, 1) for j in (0, 1) for k in (0, 1)]
    for a in range(8):
        for b in range(a + 1, 8):
            d = V[b] - V[a]
            if np.count_nonzero(np.abs(d) > 1e-9) == 1:
                sc.line(V[a], V[b], **kw)


def cell_edges(sc, A, B, C, o=(0, 0, 0), **kw):
    o = np.asarray(o, float)
    for i in (0, 1):
        for j in (0, 1):
            sc.line(o + i * A + j * B, o + i * A + j * B + C, **kw)
            sc.line(o + i * A + j * C, o + i * A + j * C + B, **kw)
            sc.line(o + i * B + j * C, o + i * B + j * C + A, **kw)


def in_cell(frac_list, tol=1e-6):
    out = []
    for f in frac_list:
        f = np.asarray(f, float) % 1.0
        for t in np.array(np.meshgrid([0, 1], [0, 1], [0, 1])).T.reshape(-1, 3):
            q = f + t
            if np.all(q < 1 + tol) and not any(np.allclose(q, o) for o in out):
                out.append(q)
    return out


FCC_T = [np.array(v, float) for v in [(0, 0, 0), (0, .5, .5), (.5, 0, .5), (.5, .5, 0)]]


# ---------------------------------------------------------------- Figure 3.1
def comma(ax, x, y, ang=0.0, mirror=False, filled=True, sign="+", s=1.0, color=BLUE, sign_off=(0.22, 0.12)):
    """Asymmetric comma motif (head + curved tail); mirror=True gives the enantiomorph."""
    t = np.linspace(0, 1, 25)
    cx = 0.06 - 0.22 * t ** 2
    cy = -0.05 - 0.30 * t
    w = 0.065 * (1 - t) + 0.006
    # tangent normals
    dx, dy = np.gradient(cx), np.gradient(cy)
    nn = np.hypot(dx, dy)
    nx, ny = -dy / nn, dx / nn
    left = np.c_[cx + w * nx, cy + w * ny]
    right = np.c_[cx - w * nx, cy - w * ny][::-1]
    th = np.linspace(0, 2 * np.pi, 40)
    head = np.c_[0.11 * np.cos(th), 0.11 * np.sin(th)]
    pts = [head, np.vstack([left, right])]
    R = np.array([[np.cos(ang), -np.sin(ang)], [np.sin(ang), np.cos(ang)]])
    for P in pts:
        Q = P.copy()
        if mirror:
            Q[:, 0] = -Q[:, 0]
        Q = (Q * s) @ R.T + [x, y]
        ax.add_patch(Polygon(Q, closed=True, fc=color if filled else "white", ec=color, lw=1.0, zorder=3))
    if sign:
        so = np.array(sign_off) * s
        if mirror:
            so[0] = -so[0]
        so = R @ so
        ax.text(x + so[0], y + so[1], sign, fontsize=9, ha="center", va="center", zorder=4,
                color=INK, weight="bold")


def symmetry_operations():
    fig, axs = plt.subplots(2, 3, figsize=(6.8, 4.9))
    axs = axs.ravel()
    for ax in axs:
        ax.set_aspect("equal"); ax.axis("off")

    def prim(ax):
        ax.add_patch(Circle((0, 0), 1.25, fc="none", ec="0.6", lw=0.8))
        ax.set_xlim(-1.55, 1.55); ax.set_ylim(-1.6, 1.5)

    # (a) 4-fold rotation
    ax = axs[0]; prim(ax)
    for k in range(4):
        a = np.radians(90 * k)
        comma(ax, 0.8 * np.cos(a + 0.5), 0.8 * np.sin(a + 0.5), ang=a)
    ax.add_patch(Rectangle((-0.09, -0.09), 0.18, 0.18, fc=INK, ec="none", zorder=4))
    ax.set_title("(a) rotation  4 / $C_4$", fontsize=9.5, loc="left")
    ax.text(0, -1.5, "rotate 90° four times", ha="center", fontsize=7.6, color="0.3")
    # (b) mirror
    ax = axs[1]; prim(ax)
    ax.plot([0, 0], [-1.25, 1.25], color=INK, lw=2.2)
    comma(ax, 0.6, 0.25)
    comma(ax, -0.6, 0.25, mirror=True, filled=False)
    ax.set_title("(b) mirror  $m$ / $\\sigma$", fontsize=9.5, loc="left")
    ax.text(0, -1.5, "filled ↔ open: mirror image", ha="center", fontsize=7.6, color="0.3")
    # (c) inversion
    ax = axs[2]; prim(ax)
    comma(ax, 0.6, 0.45, ang=0.3, sign="+")
    comma(ax, -0.6, -0.45, ang=0.3 + np.pi, mirror=True, filled=False, sign="−")
    ax.add_patch(Circle((0, 0), 0.07, fc="white", ec=INK, lw=1.2, zorder=4))
    ax.plot([0.6, -0.6], [0.45, -0.45], color="0.6", lw=0.7, ls=":")
    ax.set_title("(c) inversion  $\\bar1$ / $i$", fontsize=9.5, loc="left")
    ax.text(0, -1.5, "$x \\to -x$; +$z$ goes to −$z$", ha="center", fontsize=7.6, color="0.3")
    # (d) 4-bar
    ax = axs[3]; prim(ax)
    for k in range(4):
        a = np.radians(90 * k)
        odd = k % 2 == 1
        comma(ax, 0.8 * np.cos(a + 0.5), 0.8 * np.sin(a + 0.5), ang=a, mirror=odd, filled=not odd,
              sign="−" if odd else "+")
    ax.add_patch(Rectangle((-0.1, -0.1), 0.2, 0.2, fc="white", ec=INK, lw=1.2, zorder=4))
    ax.add_patch(Ellipse((0, 0), 0.16, 0.08, fc=INK, ec="none", zorder=5))
    ax.set_title("(d) rotoinversion  $\\bar4$ / $S_4$", fontsize=9.5, loc="left")
    ax.text(0, -1.5, "rotate 90°, then invert", ha="center", fontsize=7.6, color="0.3")

    # (e) screw 2_1 vs 2 (side view, c vertical)
    ax = axs[4]
    ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.6, 1.5)
    for x0, lab, screw in ((-0.75, "$2_1$", True), (0.85, "2", False)):
        ax.plot([x0, x0], [-1.15, 1.15], color=INK, lw=1.0, ls=(0, (6, 2)))
        ax.text(x0, 1.32, lab, ha="center", fontsize=10)
        for z in (-1.0, 0.0, 1.0) if screw else (-1.0, 1.0):
            comma(ax, x0 + 0.35, z - 0.0 + 0.1, ang=0.0, s=0.8, sign="")
            if screw:
                if z < 0.9:
                    comma(ax, x0 - 0.35, z + 0.5 + 0.1, mirror=True, s=0.8, sign="")
            else:
                comma(ax, x0 - 0.35, z + 0.1, mirror=True, s=0.8, sign="")
    ax.annotate("", xy=(-1.45, 0.0), xytext=(-1.45, -1.0),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, color=VERM, mutation_scale=7))
    ax.text(-1.5, -0.5, "$c$", color=VERM, ha="right", va="center", fontsize=9)
    ax.annotate("", xy=(-1.25, -0.4), xytext=(-1.25, -0.9),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, color="0.3", mutation_scale=6))
    ax.text(-1.2, -1.32, "180° + $c$/2", fontsize=7.4, color="0.3", ha="left")
    ax.text(0.85, -1.32, "180°, same height", fontsize=7.4, color="0.3", ha="center")
    ax.set_title("(e) screw $2_1$ vs. rotation 2", fontsize=9.5, loc="left")
    # (f) c-glide (side view; glide plane edge-on, c vertical)
    ax = axs[5]
    ax.set_xlim(-1.55, 1.55); ax.set_ylim(-1.6, 1.5)
    ax.plot([0, 0], [-1.2, 1.2], color=INK, lw=1.2, ls=(0, (4, 2, 1, 2)))
    for z in (-1.0, 0.0, 1.0):
        comma(ax, -0.55, z + 0.1, s=0.8, sign="")
    for z in (-0.5, 0.5):
        comma(ax, 0.55, z + 0.1, mirror=True, filled=False, s=0.8, sign="")
    ax.annotate("", xy=(1.2, 0.1), xytext=(1.2, -0.4), arrowprops=dict(arrowstyle="<|-|>", lw=0.8,
                                                                       color=VERM, mutation_scale=6))
    ax.text(1.27, -0.15, "$c$/2", color=VERM, fontsize=8.5, va="center")
    ax.set_title("(f) glide plane  $c$", fontsize=9.5, loc="left")
    ax.text(0, -1.5, "reflect, then translate $c$/2", ha="center", fontsize=7.6, color="0.3")
    fig.text(0.5, 0.01, "Plan views (a)–(d): + / − = above / below the page; filled and open commas are mirror "
             "images.\n(e), (f): side views, $c$ vertical; a rotation about $c$ looks like a left–right flip "
             "but keeps the hand.", ha="center", fontsize=7.4, color="0.3")
    fig.subplots_adjust(wspace=0.05, hspace=0.25, left=0.01, right=0.99, top=0.94, bottom=0.09)
    save(fig, "03", "fig-3-1-symmetry-operations")


# ---------------------------------------------------------------- Figure 3.2
def _poly(n, cen, R, rot=0.0):
    a = rot + 2 * np.pi * np.arange(n) / n
    return np.c_[cen[0] + R * np.cos(a), cen[1] + R * np.sin(a)]


def _tilings(axs):
    fc = "#DCE9F5"
    # triangles
    ax = axs[0]
    h = np.sqrt(3) / 2
    for i in range(-1, 4):
        for j in range(0, 3):
            x0 = i + 0.5 * (j % 2)
            ax.add_patch(Polygon([[x0, j * h], [x0 + 1, j * h], [x0 + 0.5, (j + 1) * h]], fc=fc, ec=BLUE, lw=0.7))
            ax.add_patch(Polygon([[x0 + 0.5, (j + 1) * h], [x0 + 1, j * h], [x0 + 1.5, (j + 1) * h]], fc=fc,
                                 ec=BLUE, lw=0.7))
    ax.set_xlim(0, 3); ax.set_ylim(0, 2.4); ax.set_title("$n$ = 3", fontsize=9)
    ax = axs[1]
    for i in range(3):
        for j in range(3):
            ax.add_patch(Rectangle((i * 0.85, j * 0.85), 0.85, 0.85, fc=fc, ec=BLUE, lw=0.7))
    ax.set_xlim(0, 2.55); ax.set_ylim(0, 2.55); ax.set_title("$n$ = 4", fontsize=9)
    ax = axs[2]
    r = 0.55
    for i in range(-1, 4):
        for j in range(-1, 4):
            c = np.array([i * 1.5 * r, j * np.sqrt(3) * r + (i % 2) * np.sqrt(3) / 2 * r])
            ax.add_patch(Polygon(_poly(6, c, r), fc=fc, ec=BLUE, lw=0.7))
    ax.set_xlim(0, 2.3); ax.set_ylim(0, 2.3); ax.set_title("$n$ = 6", fontsize=9)
    # pentagons: central + 5 edge-sharing neighbours -> 36 deg gaps
    ax = axs[3]
    R = 0.5
    cen = np.array([0.0, 0.0])
    P0 = _poly(5, cen, R, rot=np.pi / 2)
    ax.add_patch(Polygon(P0, fc=fc, ec=BLUE, lw=0.7))
    ap = R * np.cos(np.pi / 5)
    outs = []
    for k in range(5):
        p1, p2 = P0[k], P0[(k + 1) % 5]
        u = (p2 - p1) / np.linalg.norm(p2 - p1)
        refl = []
        for q in P0:
            d = q - p1
            par = (d @ u) * u
            refl.append(p1 + par - (d - par))
        Pk = np.array(refl)
        outs.append(Pk)
        ax.add_patch(Polygon(Pk, fc=fc, ec=BLUE, lw=0.7))
    for k in range(5):
        v = P0[k]
        # gap wedge at vertex v between neighbours: nearest vertices of adjacent outer pentagons
        pts = []
        for Pk in outs:
            d = np.linalg.norm(Pk - v, axis=1)
            near = np.argsort(d)
            if d[near[0]] < 1e-6:
                # the neighbour vertex along an edge leaving v that is not shared with P0
                for idx in near[1:3]:
                    q = Pk[idx]
                    if np.min(np.linalg.norm(P0 - q, axis=1)) > 1e-6:
                        pts.append(q)
        if len(pts) == 2:
            ax.add_patch(Polygon([v, pts[0], pts[1]], fc=VERM, alpha=0.55, ec=VERM, lw=0.6))
    ax.set_xlim(-1.45, 1.45); ax.set_ylim(-1.4, 1.5); ax.set_title("$n$ = 5: gaps", fontsize=9, color=VERM)
    # octagons
    ax = axs[4]
    s = 1.0
    Ro = s / (2 * np.sin(np.pi / 8))
    d = 2 * Ro * np.cos(np.pi / 8)
    for i in range(2):
        for j in range(2):
            ax.add_patch(Polygon(_poly(8, (i * d, j * d), Ro, rot=np.pi / 8), fc=fc, ec=BLUE, lw=0.7))
    c = np.array([d / 2, d / 2])
    ax.add_patch(Polygon(_poly(4, c, s / np.sqrt(2), rot=0), fc=VERM, alpha=0.55, ec=VERM, lw=0.6))
    ax.set_xlim(-1.0, d + 1.0); ax.set_ylim(-1.0, d + 1.0); ax.set_title("$n$ = 8: gaps", fontsize=9, color=VERM)
    for ax in axs:
        ax.set_aspect("equal"); ax.axis("off")


def lattice_panel(ax, A, B, C, centring, title, azim=28, elev=16, extra=None, outline=None):
    sc = Scene(ax, azim=azim, elev=elev)
    cell_edges(sc, A, B, C, color=INK, lw=0.8)
    r = 0.075
    for i in (0, 1):
        for j in (0, 1):
            for k in (0, 1):
                sc.atom(i * A + j * B + k * C, r, BLUE)
    for f in centring:
        for p in in_cell([f]):
            sc.atom(p[0] * A + p[1] * B + p[2] * C, r, ORANGE)
    if outline is not None:
        for p0, p1 in outline:
            sc.line(p0, p1, color=VERM, lw=1.1, n=4, bias=5)
    if extra:
        extra(sc)
    sc.draw(pad=0.05)
    ax.set_title(title, fontsize=7.8, loc="center", pad=2)


def restriction_bravais():
    fig = plt.figure(figsize=(6.8, 6.6))
    gs = fig.add_gridspec(4, 6, height_ratios=[0.62, 1, 1, 1], hspace=0.32, wspace=0.08)
    taxs = [fig.add_subplot(gs[0, k]) for k in range(5)]
    _tilings(taxs)
    tx = fig.add_subplot(gs[0, 5]); tx.axis("off")
    tx.text(0.0, 0.5, "trace $1+2\\cos(2\\pi/n)$\nmust be an integer:\n$n$ = 1, 2, 3, 4, 6", fontsize=8,
            va="center", ha="left")
    ex, ey, ez = np.eye(3)

    def vec(a, b, c, al, be, ga):
        al, be, ga = np.radians([al, be, ga])
        A = a * ex
        B = b * np.array([np.cos(ga), np.sin(ga), 0])
        cx = c * np.cos(be)
        cy = c * (np.cos(al) - np.cos(be) * np.cos(ga)) / np.sin(ga)
        cz = np.sqrt(c * c - cx * cx - cy * cy)
        return A, B, np.array([cx, cy, cz])

    P, Cc, I, F = [], [(.5, .5, 0)], [(.5, .5, .5)], [(.5, .5, 0), (.5, 0, .5), (0, .5, .5)]
    tri = vec(1.0, 0.8, 1.2, 75, 82, 68)
    mono = vec(1.0, 0.8, 1.2, 90, 72, 90)
    ortho = vec(1.0, 0.75, 1.25, 90, 90, 90)
    tet = vec(0.85, 0.85, 1.3, 90, 90, 90)
    hexv = vec(1.0, 1.0, 1.25, 90, 90, 120)
    cub = vec(1, 1, 1, 90, 90, 90)
    panels = [
        (gs[1, 0], tri, P, "triclinic P"), (gs[1, 1], mono, P, "monoclinic P"), (gs[1, 2], mono, Cc, "monoclinic C"),
        (gs[1, 3], tet, P, "tetragonal P"), (gs[1, 4], tet, I, "tetragonal I"),
        (gs[2, 0], ortho, P, "orthorhombic P"), (gs[2, 1], ortho, Cc, "orthorhombic C"),
        (gs[2, 2], ortho, I, "orthorhombic I"), (gs[2, 3], ortho, F, "orthorhombic F"),
        (gs[3, 2], cub, P, "cubic P"), (gs[3, 3], cub, I, "cubic I"), (gs[3, 4], cub, F, "cubic F"),
    ]
    for spec, (A, B, C), cen, title in panels:
        lattice_panel(fig.add_subplot(spec), A, B, C, cen, title)

    # hexagonal P: hexagonal prism of points, primitive cell outlined
    ax = fig.add_subplot(gs[2, 4])
    sc = Scene(ax, azim=20, elev=16)
    a, c = 0.8, 1.0
    hv = [np.array([a * np.cos(np.radians(60 * k)), a * np.sin(np.radians(60 * k)), 0]) for k in range(6)]
    for z in (0, c):
        for k in range(6):
            sc.line(hv[k] + [0, 0, z], hv[(k + 1) % 6] + [0, 0, z], color="0.55", lw=0.7)
    for k in range(6):
        sc.line(hv[k], hv[k] + [0, 0, c], color="0.55", lw=0.7)
    A1, A2, C3 = hv[0], hv[2], np.array([0, 0, c])
    cell_edges(sc, A1, A2, C3, color=VERM, lw=1.2)
    for z in (0, c):
        for v in hv + [np.zeros(3)]:
            sc.atom(v + [0, 0, z], 0.06, BLUE)
    sc.draw(pad=0.05)
    ax.set_title("hexagonal P", fontsize=8.6, pad=2)
    ax.text(0.5, -0.02, "primitive cell in red", transform=ax.transAxes, ha="center", va="top", fontsize=7,
            color=VERM)

    # rhombohedral R as rhombohedron
    ax = fig.add_subplot(gs[3, 0])
    A, B, C = vec(1, 1, 1, 70, 70, 70)
    lattice_panel(ax, A, B, C, [], "rhombohedral R")
    ax.text(0.5, -0.02, "a = b = c\nα = β = γ ≠ 90°", transform=ax.transAxes, ha="center", va="top",
            fontsize=7)
    # R in hexagonal setting
    ax = fig.add_subplot(gs[3, 1])
    A, B, C = vec(0.8, 0.8, 1.35, 90, 90, 120)
    lattice_panel(ax, A, B, C, [(2 / 3, 1 / 3, 1 / 3), (1 / 3, 2 / 3, 2 / 3)], "R (hexagonal setting)", azim=15)
    ax.text(0.5, -0.02, "extra points at\n⅔,⅓,⅓ and ⅓,⅔,⅔", transform=ax.transAxes, ha="center", va="top",
            fontsize=7)

    # inset: C-centred tetragonal = primitive tetragonal
    ax = fig.add_subplot(gs[1, 5])
    sc = Scene(ax, azim=28, elev=40)
    A, B, C = 1.0 * ex, 1.0 * ey, 0.7 * ez
    cell_edges(sc, A, B, C, color=INK, lw=0.8)
    A2, B2 = (A + B) / 2, (B - A) / 2
    cell_edges(sc, (A + B) / 2, (B - A) / 2, C, color=VERM, lw=1.2)
    for k in (0, 1):
        sc.atom(np.array([-.5, .5, 0]) + k * C, 0.06, ORANGE)
    for i in (0, 1):
        for j in (0, 1):
            for k in (0, 1):
                sc.atom(i * A + j * B + k * C, 0.06, BLUE)
    for k in (0, 1):
        sc.atom(np.array([.5, .5, 0]) + k * C, 0.06, ORANGE)
    sc.draw(pad=0.05)
    ax.set_title("inset", fontsize=8.6, pad=2)
    ax.text(0.5, -0.02, "C-centred tetragonal =\nprimitive tetragonal,\nedge $a/\\sqrt{2}$ (red)",
            transform=ax.transAxes, ha="center", va="top", fontsize=7, color=VERM)
    lx = fig.add_subplot(gs[2, 5]); lx.axis("off")
    lx.plot([0.1], [0.62], "o", color=BLUE, ms=7, mec="0.2"); lx.text(0.2, 0.62, "corner points", va="center",
                                                                    fontsize=7.6)
    lx.plot([0.1], [0.45], "o", color=ORANGE, ms=7, mec="0.2"); lx.text(0.2, 0.45, "centring points",
                                                                      va="center", fontsize=7.6)
    lx.set_xlim(0, 1); lx.set_ylim(0, 1)
    lx2 = fig.add_subplot(gs[3, 5]); lx2.axis("off")
    lx2.text(0.0, 0.55, "P primitive\nC one pair of\n   faces centred\nI body-centred\nF all faces centred",
             fontsize=7.4, va="center")
    save(fig, "03", "fig-3-2-restriction-bravais")


# ---------------------------------------------------------------- Figure 3.3
def spinel_sites(u=0.2624):
    """MgAl2O4 in Fd-3m, origin choice 2: Mg 8a, Al 16d, O 32e (u,u,u). Fractional coordinates."""
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


def _images(pts):
    out = []
    for p in pts:
        for t in np.array(np.meshgrid([-1, 0, 1], [-1, 0, 1], [-1, 0, 1])).T.reshape(-1, 3):
            out.append(p + t)
    return np.array(out)


def wyckoff_positions():
    fig = plt.figure(figsize=(6.8, 5.2))
    gs = fig.add_gridspec(2, 6, height_ratios=[1.15, 0.85], hspace=0.3, wspace=0.1)
    RED, BLU, GRN = "#D9473B", "#2B7BB9", "#3A9A5B"
    # (a) Fm-3m cell with sites
    ax = fig.add_subplot(gs[0, 0:2])
    sc = Scene(ax, azim=26, elev=18)
    cube_edges(sc, color=INK, lw=0.8)
    for p in in_cell(FCC_T):
        sc.atom(p, 0.06, RED)
    for p in in_cell([t + np.array([.5, .5, .5]) for t in FCC_T]):
        sc.atom(p, 0.06, BLU)
    for p in [np.array([i, j, k]) * 0.5 + 0.25 for i in (0, 1) for j in (0, 1) for k in (0, 1)]:
        sc.atom(p, 0.045, GRN)
    sc.atom((0.22, 0, 0), 0.04, "0.55")
    sc.text((0.22, -0.05, -0.12), "24e ($x$,0,0)", fontsize=7, color="0.35")
    sc.draw(pad=0.04)
    ax.set_title("(a) $Fm\\bar3m$ (No. 225)", fontsize=9.5, loc="left")
    tx = fig.add_subplot(gs[0, 2:4]); tx.axis("off")
    rows = [("site", "mult.", "site sym.", "coord."),
            ("4a", "4", "$m\\bar3m$", "0,0,0"), ("4b", "4", "$m\\bar3m$", "½,½,½"),
            ("8c", "8", "$\\bar43m$", "¼,¼,¼"), ("24d", "24", "$m.mm$", "0,¼,¼"),
            ("24e", "24", "$4m.m$", "$x$,0,0"), ("192l", "192", "1", "$x,y,z$")]
    cols = {"4a": RED, "4b": BLU, "8c": GRN, "24e": "0.45"}
    for i, r in enumerate(rows):
        y = 0.92 - i * 0.12
        for j, (cell, x) in enumerate(zip(r, (0.0, 0.2, 0.42, 0.78))):
            ax_c = cols.get(r[0], INK) if j == 0 else INK
            tx.text(x, y, cell, fontsize=7.8, color=ax_c, weight="bold" if i == 0 else "normal", va="center")
        if i == 0:
            tx.plot([0, 1.0], [y - 0.06, y - 0.06], color="0.5", lw=0.6)
    tx.text(0.0, 0.08, "+ F-centring translations\n(0,½,½), (½,0,½), (½,½,0)", fontsize=7.2, color="0.35", va="center")
    tx.set_xlim(0, 1.05); tx.set_ylim(0, 1)

    # (c) spinel one octant
    ax = fig.add_subplot(gs[0, 4:6])
    sc = Scene(ax, azim=26, elev=18)
    Mg8, Al16, O32 = spinel_sites()
    cube_edges(sc, L=(0.5, 0.5, 0.5), color=INK, lw=0.8)
    lo, hi = -1e-6, 0.5 + 1e-6
    inside = lambda p: np.all(p > lo) and np.all(p < hi)
    Oi = [p for p in _images(O32) if inside(p)]
    Mi = [p for p in _images(Mg8) if inside(p)]
    Ai = [p for p in _images(Al16) if inside(p)]
    allO = _images(O32)
    for m in Mi:
        nb = allO[np.linalg.norm(allO - m, axis=1) < 0.27]
        for i in range(4):
            for j in range(i + 1, 4):
                for k in range(j + 1, 4):
                    sc.poly([nb[i], nb[j], nb[k]], fc=ORANGE, alpha=0.45, ec="#8A5A00", lw=0.4)
    for a_ in Ai:
        nb = allO[np.linalg.norm(allO - a_, axis=1) < 0.27]
        for o in nb:
            sc.line(a_, o, color=BLUE, lw=1.0, n=3)
            if not inside(o):
                sc.atom(o, 0.016, _light(RED, 0.4))
    for p in Oi:
        sc.atom(p, 0.022, RED)
    for p in Mi:
        sc.atom(p, 0.026, "#7BB661")
    for p in Ai:
        sc.atom(p, 0.026, "#5A6B7D")
    sc.draw(pad=0.04)
    ax.set_title("(c) spinel MgAl$_2$O$_4$, $Fd\\bar3m$", fontsize=9.5, loc="left")
    ax.text(0.5, -0.02, "one-eighth of the cell; origin choice 2\nMg 8a (tetrahedral), Al 16d (octahedral),\n"
            "O 32e ($x,x,x$), $x$ ≈ 0.26\n8 + 16 + 32 = 56 atoms per cell", transform=ax.transAxes, ha="center",
            va="top", fontsize=7.2)
    h = [plt.Line2D([], [], marker="o", ls="", color=c, ms=6, mec="0.2") for c in ("#7BB661", "#5A6B7D", RED)]
    ax.legend(h, ["Mg", "Al", "O"], loc="upper right", fontsize=7, ncol=3, handletextpad=0.1, columnspacing=0.5,
              bbox_to_anchor=(1.02, 1.0))

    # (b) choose sites
    specs = [("NaCl = Na 4a + Cl 4b", [(FCC_T, RED, 0.08), ([t + .5 for t in FCC_T], BLU, 0.1)], 0),
             ("CaF$_2$ = Ca 4a + F 8c", [(FCC_T, RED, 0.08), (None, GRN, 0.06)], 1),
             ("Cu = Cu 4a", [(FCC_T, RED, 0.08)], 2)]
    for title, sets, k in specs:
        ax = fig.add_subplot(gs[1, 2 * k:2 * k + 2])
        sc = Scene(ax, azim=26, elev=18)
        cube_edges(sc, color="0.4", lw=0.7)
        for lst, col, r in sets:
            if lst is None:
                pts = [np.array([i, j, kk]) * 0.5 + 0.25 for i in (0, 1) for j in (0, 1) for kk in (0, 1)]
            else:
                pts = in_cell(lst)
            for p in pts:
                sc.atom(p, r, col)
        sc.draw(pad=0.04)
        ax.set_title(("(b) " if k == 0 else "") + title, fontsize=8.5, loc="left")
    save(fig, "03", "fig-3-3-wyckoff-positions")


# ---------------------------------------------------------------- Figure 3.4
def stereo(v):
    """Stereographic projection of unit vectors (upper hemisphere, z up) -> (x, y), R = 1."""
    v = np.asarray(v, float)
    v = v / np.linalg.norm(v, axis=-1, keepdims=True)
    return v[..., :2] / (1 + v[..., 2:3])


def _great_circle(n, npts=300):
    n = np.asarray(n, float); n /= np.linalg.norm(n)
    a = np.cross(n, [0, 0, 1.0])
    if np.linalg.norm(a) < 1e-9:
        a = np.array([1.0, 0, 0])
    a /= np.linalg.norm(a)
    b = np.cross(n, a)
    t = np.linspace(0, 2 * np.pi, npts)
    V = np.outer(np.cos(t), a) + np.outer(np.sin(t), b)
    V = V[V[:, 2] >= -1e-9]
    return V


def _slerp(p, q, n=40):
    p = np.asarray(p, float) / np.linalg.norm(p); q = np.asarray(q, float) / np.linalg.norm(q)
    om = np.arccos(np.clip(p @ q, -1, 1))
    t = np.linspace(0, 1, n)[:, None]
    return (np.sin((1 - t) * om) * p + np.sin(t * om) * q) / np.sin(om)


def _orient(hkl, uvw):
    """Rows: sample axes RD, TD, ND expressed in crystal coordinates."""
    nd = np.asarray(hkl, float); nd /= np.linalg.norm(nd)
    rd = np.asarray(uvw, float); rd /= np.linalg.norm(rd)
    td = np.cross(nd, rd)
    return np.array([rd, td, nd])


def _rand_rot(rng, sigma_deg, n):
    """Small random rotations (axis-angle, Gaussian angle)."""
    axes = rng.normal(size=(n, 3)); axes /= np.linalg.norm(axes, axis=1, keepdims=True)
    ang = np.radians(rng.normal(0, sigma_deg, n))
    K = np.zeros((n, 3, 3))
    K[:, 0, 1], K[:, 0, 2], K[:, 1, 2] = -axes[:, 2], axes[:, 1], -axes[:, 0]
    K = K - K.transpose(0, 2, 1)
    I = np.eye(3)[None]
    return I + np.sin(ang)[:, None, None] * K + (1 - np.cos(ang))[:, None, None] * (K @ K)


P111 = np.array([[1, 1, 1], [-1, 1, 1], [1, -1, 1], [1, 1, -1]], float) / np.sqrt(3)


def _pole_density(components, grid_xy, kappa=60.0, rng=None, n_per=120, random_frac=0.0):
    """MRD of {111} poles on stereographic grid points, from texture components.

    components: list of (G (3x3 rows RD,TD,ND in crystal coords), weight, spread_deg)."""
    rng = rng or np.random.default_rng(0)
    poles, wts = [], []
    for G, w, spread in components:
        R = _rand_rot(rng, spread, n_per)
        Gs = R @ G
        pc = np.einsum("nij,kj->nki", Gs, P111).reshape(-1, 3)
        # sample symmetry (orthorhombic): mirrors normal to RD and TD
        for sx in (1, -1):
            for sy in (1, -1):
                q = pc * [sx, sy, 1]
                poles.append(np.vstack([q, -q])); wts.append(np.full(2 * len(q), w))
    poles = np.vstack(poles); wts = np.concatenate(wts)
    wts = wts / wts.sum()
    x, y = grid_xy
    r2 = x ** 2 + y ** 2
    d = np.stack([2 * x / (1 + r2), 2 * y / (1 + r2), (1 - r2) / (1 + r2)], -1)
    D = d.reshape(-1, 3)
    f = np.empty(len(D))
    cst = kappa / (2 * np.pi * (1 - np.exp(-2 * kappa)))
    for i0 in range(0, len(D), 400):
        dot = D[i0:i0 + 400] @ poles.T
        f[i0:i0 + 400] = (cst * np.exp(kappa * (dot - 1)) * wts).sum(1)
    mrd = 4 * np.pi * f
    mrd = (1 - random_frac) * mrd + random_frac
    return mrd.reshape(x.shape)


def stereographic_pole_figures():
    fig = plt.figure(figsize=(6.8, 6.6))
    gs = fig.add_gridspec(2, 2, hspace=0.22, wspace=0.12)
    # (a) construction
    ax = fig.add_subplot(gs[0, 0]); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(Circle((0, 0), 1, fc="#F4F7FA", ec=INK, lw=1.0))
    ax.plot([-1.25, 1.25], [0, 0], color="0.4", lw=0.9)
    ax.text(-1.27, 0.03, "equatorial\n(projection) plane", fontsize=7.2, va="bottom", ha="left", color="0.35")
    phi = np.radians(50)
    Pp = np.array([np.sin(phi), np.cos(phi)])
    S = np.array([0, -1]); N = np.array([0, 1])
    Pq = np.array([np.tan(phi / 2), 0])
    ax.plot([0, Pp[0]], [0, Pp[1]], color=BLUE, lw=1.2)
    ax.plot([Pp[0], S[0]], [Pp[1], S[1]], color=VERM, lw=1.1, ls="--")
    ax.plot([0, 0], [-1, 1], color="0.6", lw=0.7, ls=":")
    for p, lab, off in ((N, "N", (0, 0.08)), (S, "S", (0, -0.12)), (Pp, "P (pole)", (0.08, 0.05)),
                        (Pq, "P′", (0.03, 0.08))):
        ax.plot(*p, "o", color=INK, ms=4)
        ax.text(p[0] + off[0], p[1] + off[1], lab, fontsize=8.5, ha="left" if lab not in "NS" else "center",
                va="center")
    ax.add_patch(Arc((0, 0), 0.5, 0.5, theta1=90 - np.degrees(phi), theta2=90, color=INK, lw=0.9))
    ax.text(0.1, 0.32, "φ", fontsize=10)
    ax.annotate("", xy=(Pq[0], -0.12), xytext=(0, -0.12), arrowprops=dict(arrowstyle="<|-|>", lw=0.8,
                                                                         mutation_scale=7, color=VERM))
    ax.text(Pq[0] / 2, -0.2, "$r = R\\tan(\\varphi/2)$", fontsize=8.5, color=VERM, ha="center", va="top")
    ax.text(-0.12, 0.0, "O", fontsize=8, ha="right", va="bottom")
    ax.text(-0.75, -0.95, "reference\nsphere, radius $R$", fontsize=7.2, color="0.35", ha="center")
    ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.25)
    ax.set_title("(a) construction", fontsize=9.5, loc="left")

    # (b) standard (001) projection
    ax = fig.add_subplot(gs[0, 1]); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(Circle((0, 0), 1, fc="white", ec=INK, lw=1.0))
    tri = np.vstack([_slerp([0, 0, 1], [0, 1, 1]), _slerp([0, 1, 1], [1, 1, 1]), _slerp([1, 1, 1], [0, 0, 1])])
    ax.add_patch(Polygon(stereo(tri), fc="#F6D9A8", ec="none", zorder=0))
    for n, col in [((1, 0, 0), BLUE), ((0, 1, 0), BLUE), ((1, 1, 0), GREEN), ((1, -1, 0), GREEN),
                   ((1, 0, 1), GREEN), ((-1, 0, 1), GREEN), ((0, 1, 1), GREEN), ((0, -1, 1), GREEN)]:
        V = _great_circle(n)
        xy = stereo(V)
        order = np.argsort(np.arctan2(*(V[:, :2].T[::-1])))
        ax.plot(*xy.T, ".", ms=0.6, color=col)
    import itertools
    fams = {"100": (BLUE, "s"), "110": (GREEN, "D"), "111": (VERM, "^"), "112": (PINK, "o"), "012": ("0.4", "o")}
    seen = set()
    for fam, (col, mk) in fams.items():
        base = [int(c) for c in fam]
        for perm in set(itertools.permutations(base)):
            for sg in itertools.product((1, -1), repeat=3):
                v = np.array(perm) * sg
                if v[2] < 0 or tuple(v) in seen or not v.any():
                    continue
                if v[2] == 0 and (v[0] < 0 or (v[0] == 0 and v[1] < 0)):
                    pass
                seen.add(tuple(v))
                xy = stereo(v)
                ax.plot(*xy, mk, color=col, ms=5 if fam in ("100", "110", "111") else 3.5, mec="0.2", mew=0.4,
                        zorder=5)
    lab = {(0, 0, 1): ("001", (0.05, -0.08)), (1, 0, 0): ("100", (0.06, -0.05)), (0, 1, 0): ("010", (0.0, 0.07)),
           (-1, 0, 0): ("$\\bar100$", (-0.1, -0.05)), (0, -1, 0): ("$0\\bar10$", (0.0, -0.08)),
           (0, 1, 1): ("011", (0.0, 0.07)), (1, 0, 1): ("101", (0.06, 0.05)), (1, 1, 1): ("111", (0.07, 0.04)),
           (1, 1, 0): ("110", (0.07, 0.05)), (1, 1, 2): ("112", (0.07, -0.02)), (0, 1, 2): ("012", (-0.09, 0.03))}
    for v, (t, off) in lab.items():
        xy = stereo(np.array(v, float))
        ax.text(xy[0] + off[0], xy[1] + off[1], t, fontsize=7.2, ha="center", va="center", zorder=6)
    ax.set_xlim(-1.15, 1.15); ax.set_ylim(-1.18, 1.15)
    ax.set_title("(b) standard (001) projection, cubic", fontsize=9.5, loc="left")
    ax.text(0, -1.17, "{100} ■ centre & rim;  {110} ◆ $r$=0.414$R$;  {111} ▲ 0.518$R$;  {112} 0.318$R$;  "
            "{012} 0.236$R$", fontsize=6.4, ha="center", va="top")

    # pole figures
    n = 151
    g = np.linspace(-1, 1, n)
    X, Y = np.meshgrid(g, g)
    mask = X ** 2 + Y ** 2 > 1
    # orientation matrices: in our plot x = TD, y = RD, centre = ND
    cube = [(_orient((0, 0, 1), (1, 0, 0)), 1.0, 7.0)]
    Z = _pole_density(cube, (Y, X), kappa=50, rng=np.random.default_rng(1), random_frac=0.10)
    comps = [(_orient((1, 1, 2), (-1, -1, 1)), 0.38, 5.0),   # copper {112}<111>
             (_orient((1, 2, 3), (6, 3, -4)), 0.40, 5.0),    # S {123}<634>
             (_orient((1, 1, 0), (-1, 1, 2)), 0.22, 5.0)]    # brass {110}<112>
    Z2 = _pole_density(comps, (Y, X), kappa=60, rng=np.random.default_rng(2), random_frac=0.0)
    fr = max(0.0, (Z2.max() - 8.0) / (Z2.max() - 1.0))   # random fraction giving a maximum of about 8 MRD
    Z2 = (1 - fr) * Z2 + fr
    levels = [1, 2, 4, 8, 16, 1000]
    cmap = plt.get_cmap("YlOrRd")
    for k, (ZZ, title) in enumerate(((Z, "(c) {111}: cube texture {001}⟨100⟩"),
                                      (Z2, "(d) {111}: cold-rolled Cu (β-fibre)"))):
        ax = fig.add_subplot(gs[1, k]); ax.set_aspect("equal"); ax.axis("off")
        ZZ = np.ma.array(ZZ, mask=mask)
        from matplotlib.colors import BoundaryNorm
        cs = ax.contourf(X, Y, ZZ, levels=levels, cmap=cmap, norm=BoundaryNorm(levels, cmap.N))
        ax.contour(X, Y, ZZ, levels=levels[:-1], colors="0.3", linewidths=0.4)
        ax.add_patch(Circle((0, 0), 1, fc="none", ec=INK, lw=1.0))
        ax.annotate("", xy=(0, 1.13), xytext=(0, 1.0), arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK))
        ax.text(0, 1.15, "RD", ha="center", va="bottom", fontsize=8)
        ax.annotate("", xy=(1.13, 0), xytext=(1.0, 0), arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK))
        ax.text(1.15, 0, "TD", ha="left", va="center", fontsize=8)
        ax.plot(0, 0, "+", color=INK, ms=6); ax.text(0.04, -0.06, "ND", fontsize=7)
        ax.set_xlim(-1.2, 1.3); ax.set_ylim(-1.15, 1.3)
        ax.set_title(title, fontsize=9.2, loc="left")
        ax.text(-1.18, -1.12, f"max {float(ZZ.max()):.0f} MRD", fontsize=7.4, color="0.3")
        if k == 0:
            for v in P111:
                for s_ in (1, -1):
                    w = v * s_
                    if w[2] > 0:
                        xy = stereo(w)
                        ax.plot(xy[0], xy[1], "x", color=INK, ms=4, mew=0.8)
            ax.text(1.18, -1.12, "peaks at $r$ = 0.518$R$\non the 45° diagonals", fontsize=7.2, ha="right",
                    color="0.3")
        else:
            marks = [((1, 1, 2), (-1, -1, 1), "o", "Cu {112}⟨111⟩"), ((1, 2, 3), (6, 3, -4), "s", "S {123}⟨634⟩"),
                     ((1, 1, 0), (-1, 1, 2), "D", "brass {110}⟨112⟩")]
            hs = []
            for hkl, uvw, mk, lab in marks:
                G = _orient(hkl, uvw)
                pc = (G @ P111.T).T
                for sx in (1, -1):
                    for sy in (1, -1):
                        for q in np.vstack([pc, -pc]) * [sx, sy, 1]:
                            if q[2] > 1e-9:
                                xy = stereo(q)
                                ax.plot(xy[1], xy[0], mk, mfc="none", mec=INK, ms=4.5, mew=0.8)
                hs.append(plt.Line2D([], [], marker=mk, ls="", mfc="none", mec=INK, ms=5))
            ax.legend(hs, [m[3] for m in marks], loc="lower right", bbox_to_anchor=(1.12, -0.13), fontsize=6.8,
                      handletextpad=0.2, borderaxespad=0)
    cax = fig.add_axes([0.93, 0.08, 0.015, 0.33])
    cb = fig.colorbar(cs, cax=cax, ticks=[1, 2, 4, 8, 16])
    cb.ax.set_yticklabels(["1", "2", "4", "8", "16"], fontsize=7)
    cb.set_label("MRD", fontsize=8)
    save(fig, "03", "fig-3-4-stereographic-pole-figures")


# ---------------------------------------------------------------- Figure 3.5
def _f_atom(Z, s):
    """Rough X-ray atomic scattering factor: Z at s = 0, falling with sin(theta)/lambda (1/Angstrom)."""
    return Z * (0.6 * np.exp(-11 * s ** 2) + 0.4 * np.exp(-0.9 * s ** 2) * 0 + 0.4 * np.exp(-1.2 * s ** 2))


def ordering_apb():
    fig = plt.figure(figsize=(6.8, 5.4))
    gs = fig.add_gridspec(2, 4, height_ratios=[1.0, 1.0], hspace=0.38, wspace=0.12)
    AU, CU, ZN = "#E0B040", "#C8743A", "#8A9AAA"
    # (a) FCC disordered and L1_2
    for k, ordered in enumerate((False, True)):
        ax = fig.add_subplot(gs[0, k])
        sc = Scene3(ax, azim=26, elev=18)
        cube_edges(sc, color=INK, lw=0.8)
        for p in in_cell([FCC_T[0]]):
            sc.atom(p, 0.1, AU) if ordered else sc.split(p, 0.1, CU, AU)
        for p in in_cell(FCC_T[1:]):
            sc.atom(p, 0.1, CU) if ordered else sc.split(p, 0.1, CU, AU)
        sc.draw(pad=0.03)
        ax.set_title("(a) disordered FCC" if not ordered else "L1$_2$ Cu$_3$Au", fontsize=9, loc="left")
        ax.text(0.5, -0.02, "random Cu/Au, $Fm\\bar3m$" if not ordered else "Au corners, Cu faces;\nsimple cubic, $Pm\\bar3m$",
                transform=ax.transAxes, ha="center", va="top", fontsize=7.4)
    # (b) BCC disordered and B2
    for k, ordered in enumerate((False, True)):
        ax = fig.add_subplot(gs[0, 2 + k])
        sc = Scene3(ax, azim=26, elev=18)
        cube_edges(sc, color=INK, lw=0.8)
        for p in [np.array([i, j, kk], float) for i in (0, 1) for j in (0, 1) for kk in (0, 1)]:
            sc.atom(p, 0.11, CU) if ordered else sc.split(p, 0.11, CU, ZN)
        c = np.array([.5, .5, .5])
        sc.atom(c, 0.11, ZN) if ordered else sc.split(c, 0.11, CU, ZN)
        sc.draw(pad=0.03)
        ax.set_title("(b) disordered BCC" if not ordered else "B2 CuZn", fontsize=9, loc="left")
        ax.text(0.5, -0.02, "random Cu/Zn, $Im\\bar3m$" if not ordered else "Cu corners, Zn centre;\nsimple cubic, $Pm\\bar3m$",
                transform=ax.transAxes, ha="center", va="top", fontsize=7.4)
    # (c) 2D antiphase boundary
    ax = fig.add_subplot(gs[1, 0:2]); ax.set_aspect("equal"); ax.axis("off")
    nx, ny = 10, 7
    xb = 4.5
    occ = {}
    for i in range(nx):
        for j in range(ny):
            par = (i + j) % 2
            if i > xb + (1 if j >= 4 else 0) - 0.5:
                par = 1 - par
            occ[(i, j)] = par
    for (i, j), par in occ.items():
        for di, dj in ((1, 0), (0, 1)):
            q = (i + di, j + dj)
            if q in occ:
                same = occ[q] == par
                ax.plot([i, q[0]], [j, q[1]], color=VERM if same else "0.75", lw=2.6 if same else 0.8, zorder=1)
    for (i, j), par in occ.items():
        ax.add_patch(Circle((i, j), 0.26, fc=AU if par == 0 else BLUE, ec="0.2", lw=0.5, zorder=2))
    # boundary trace
    bx = [xb + 0.0, xb, xb + 1, xb + 1]
    by = [-0.5, 3.5, 3.5, ny - 0.5]
    ax.plot([5.0 - 0.5, 5.0 - 0.5, 6.0 - 0.5, 6.0 - 0.5], [-0.5, 3.5, 3.5, ny - 0.5], color=VERM, lw=1.0, ls="--",
            zorder=0)
    ax.annotate("", xy=(6.5, -1.35), xytext=(5.5, -1.35), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.2,
                                                                          mutation_scale=9), annotation_clip=False)
    ax.text(6.65, -1.35, "domain shift ½⟨110⟩\nof the ordered cell", fontsize=7.2, va="center")
    ax.text(-0.5, ny - 0.05, "antiphase domain 1", fontsize=7.6, va="bottom")
    ax.text(nx - 0.5, ny - 0.05, "domain 2", fontsize=7.6, va="bottom", ha="right")
    ax.text(-0.5, -1.35, "APB: A–A and B–B\npairs (red); γ$_{APB}$ ≈\n0.1–0.3 J/m² (Ni$_3$Al)", fontsize=7.2,
            va="center", color=VERM)
    ax.set_xlim(-0.8, nx + 0.6); ax.set_ylim(-2.3, ny + 0.4)
    ax.set_title("(c) antiphase boundary, 2D AB", fontsize=9, loc="left")
    # (d) powder patterns
    ax = fig.add_subplot(gs[1, 2:4])
    a, lam = 3.75, 1.5406
    tt = np.linspace(20, 95, 3000)
    fAu, fCu = 79, 29
    for k, (S, lab, col) in enumerate(((0.0, "S = 0 (disordered)", BLUE), (1.0, "S = 1 (ordered)", VERM))):
        I = np.zeros_like(tt)
        peaks = []
        for h in range(0, 4):
            for kk in range(0, 4):
                for l in range(0, 4):
                    if (h, kk, l) == (0, 0, 0):
                        continue
                    N2 = h * h + kk * kk + l * l
                    d = a / np.sqrt(N2)
                    st = lam / (2 * d)
                    if st >= 1:
                        continue
                    th = np.degrees(np.arcsin(st))
                    if not 20 <= 2 * th <= 95:
                        continue
                    s = st / lam
                    fa, fc = _f_atom(fAu, s), _f_atom(fCu, s)
                    allsame = (h % 2 == kk % 2 == l % 2)
                    fav = 0.25 * fa + 0.75 * fc
                    if allsame:
                        F = 4 * fav
                    else:
                        F = S * (fa - fc)
                    peaks.append(((h, kk, l), 2 * th, F ** 2))
        # merge by 2theta (multiplicity from permutations of all-sign hkl)
        bucket = {}
        for hkl, t2, F2 in peaks:
            key = round(t2, 3)
            m = 0
            bucket.setdefault(key, [hkl, t2, F2, 0])
            bucket[key][3] += 1
        res = []
        for key, (hkl, t2, F2, cnt) in bucket.items():
            th = np.radians(t2 / 2)
            lp = (1 + np.cos(2 * th) ** 2) / (np.sin(th) ** 2 * np.cos(th))
            # count of +h+k+l permutations -> full multiplicity by sign factor
            mult = sum(1 for sh in (1, -1) for sk in (1, -1) for sl in (1, -1)
                       if len({(sh * hkl[0]), (sk * hkl[1]), (sl * hkl[2])}) >= 1) * 0 + cnt
            nz = sum(1 for v in hkl if v != 0)
            mult = cnt * 2 ** nz
            res.append((hkl, t2, F2 * mult * lp))
        Imax = max(r[2] for r in res if r[2] > 0) if S == 0 else Imax0
        if S == 0:
            Imax0 = Imax
        off = 1.25 * k
        for hkl, t2, inten in res:
            if inten <= 0:
                continue
            I += inten / Imax * np.exp(-(tt - t2) ** 2 / (2 * 0.12 ** 2))
            lab_hkl = "".join(str(v) for v in sorted(hkl, reverse=True))
            if inten / Imax > 0.005:
                ax.text(t2, off + min(inten / Imax, 1.0) + 0.04, lab_hkl, fontsize=6.3, ha="center", va="bottom",
                        rotation=90, color=col if (len(set(v % 2 for v in hkl)) > 1) else INK)
        ax.plot(tt, off + np.minimum(I, 1.0), color=col, lw=1.0)
        ax.text(60, off + 0.62, lab, fontsize=7.8, color=col)
    ax.set_xlim(20, 95); ax.set_ylim(-0.05, 2.75)
    ax.set_yticks([])
    ax.set_xlabel("2θ (degrees), Cu Kα")
    ax.set_ylabel("intensity (offset)")
    ax.set_title("(d) Cu$_3$Au, $a$ = 0.375 nm", fontsize=9, loc="left")
    ax.text(94, 2.62, "superlattice peaks (red labels):\n$|F|^2$ ratio = (50/166)$^2$ ≈ 9 %", fontsize=6.8,
            ha="right", va="top", color=VERM)
    save(fig, "03", "fig-3-5-ordering-apb")


# ---------------------------------------------------------------- Figure 3.6
def penrose(gamma=None, N=8):
    """Rhombus Penrose tiling by de Bruijn's pentagrid method. Returns list of (vertices(4x2), fat)."""
    e = np.array([[np.cos(2 * np.pi * j / 5), np.sin(2 * np.pi * j / 5)] for j in range(5)])
    if gamma is None:
        gamma = np.array([0.2, 0.15, -0.05, -0.1, -0.2])
        gamma = gamma - gamma.mean() + 0.0
    tiles = []
    for r in range(5):
        for s in range(r + 1, 5):
            for kr in range(-N, N + 1):
                for ks in range(-N, N + 1):
                    # intersection of grid lines x.e_r = kr - gamma_r and x.e_s = ks - gamma_s
                    M = np.array([e[r], e[s]])
                    z = np.linalg.solve(M, [kr - gamma[r], ks - gamma[s]])
                    K = np.ceil(e @ z + gamma).astype(int)
                    verts = []
                    for dr, ds in ((0, 0), (1, 0), (1, 1), (0, 1)):
                        KK = K.copy(); KK[r] = kr + dr; KK[s] = ks + ds
                        verts.append(KK @ e)
                    fat = (s - r) in (1, 4)
                    tiles.append((np.array(verts), fat))
    return tiles


def quasicrystal_modulated():
    fig = plt.figure(figsize=(6.8, 6.2))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.15, 1.0], hspace=0.3, wspace=0.15)
    tiles = penrose(N=7)
    cen_all = np.array([t[0].mean(0) for t in tiles])
    # (a) patch of ~150 tiles
    ax = fig.add_subplot(gs[0, 0]); ax.set_aspect("equal"); ax.axis("off")
    Rp = 5.6
    sel = [t for t, c in zip(tiles, cen_all) if np.linalg.norm(c) < Rp]
    nfat = sum(1 for _, f in sel if f); nthin = len(sel) - nfat
    for v, fat in sel:
        ax.add_patch(Polygon(v, fc="#A9CCEA" if fat else "#2F5F8A", ec="white", lw=0.5))
    # highlight a local fivefold star: vertex with 5 fat tiles meeting at 72 deg
    from collections import defaultdict
    vt = defaultdict(list)
    for idx, (v, fat) in enumerate(sel):
        for p in v:
            vt[tuple(np.round(p, 5))].append((idx, fat))
    best = None
    for p, lst in vt.items():
        if len(lst) == 5 and all(f for _, f in lst):
            if best is None or np.linalg.norm(p) < np.linalg.norm(best[0]):
                best = (np.array(p), lst)
    if best is not None:
        for idx, _ in best[1]:
            ax.add_patch(Polygon(sel[idx][0], fc="none", ec=VERM, lw=1.4, zorder=3))
    ax.set_xlim(-Rp - 0.3, Rp + 0.3); ax.set_ylim(-Rp - 0.3, Rp + 0.3)
    ax.set_title(f"(a) Penrose tiling ({len(sel)} tiles)", fontsize=9.5, loc="left")
    ax.text(0, -Rp - 0.45, f"fat (72°/108°) : thin (36°/144°) = {nfat}:{nthin} = {nfat / nthin:.2f}"
            " → τ = 1.618 for a large patch\nred: local fivefold star", ha="center", va="top", fontsize=7.0)

    # (b) diffraction of the vertex set (large patch), computed on the Fourier module
    ax = fig.add_subplot(gs[0, 1]); ax.set_aspect("equal")
    big = [t for t, c in zip(tiles, cen_all) if np.linalg.norm(c) < 7.5]
    V = np.unique(np.round(np.vstack([t[0] for t in big]), 6), axis=0)
    V = V[np.linalg.norm(V, axis=1) < 7.5]
    e = np.array([[np.cos(2 * np.pi * j / 5), np.sin(2 * np.pi * j / 5)] for j in range(5)])
    import itertools
    ks = set()
    for n in itertools.product(range(-2, 3), repeat=4):
        k = np.array(n) @ e[:4]
        if np.linalg.norm(k) < 3.2:
            ks.add(tuple(np.round(k, 6)))
    ks = np.array(sorted(ks))
    wts = np.exp(-(np.linalg.norm(V, axis=1) / 6.0) ** 2)
    amp = np.abs((np.exp(2j * np.pi * (ks @ V.T)) * wts).sum(1)) / wts.sum()
    I = amp ** 2
    I[np.linalg.norm(ks, axis=1) < 1e-9] = 0
    keep = I > 0.02 * I.max()
    ax.set_facecolor("black")
    ax.scatter(ks[keep, 0], ks[keep, 1], s=60 * np.sqrt(I[keep] / I.max()), c="white", lw=0)
    ax.scatter([0], [0], s=60, c="white", marker="o")
    ax.set_xlim(-3.1, 3.1); ax.set_ylim(-3.1, 3.1)
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(True)
    ax.set_title("(b) calculated diffraction (tenfold)", fontsize=9.5, loc="left")
    kr = np.sort(np.linalg.norm(ks[keep], axis=1))
    # mark two rings whose radii differ by tau
    strong = ks[keep][np.argsort(-I[keep])][:30]
    rs = np.unique(np.round(np.linalg.norm(strong, axis=1), 3))
    rs = rs[rs > 0.1]
    r1 = rs[0]
    for rr in (r1, r1 * TAU):
        ax.add_patch(Circle((0, 0), rr, fc="none", ec=VERM, lw=0.8, ls="--"))
    ax.text(0, -3.0, f"dashed rings: radii in ratio τ", color=VERM, fontsize=7.4, ha="center", va="bottom",
            bbox=dict(fc="black", ec="none", pad=1))

    # (c) Fibonacci chain and strip projection
    ax = fig.add_subplot(gs[1, 0]); ax.set_aspect("equal"); ax.axis("off")
    word = "L"
    for _ in range(7):
        word = "".join("LS" if ch == "L" else "L" for ch in word)
    # strip projection: square lattice, line slope 1/tau, window = projection of unit square
    th = np.arctan(1 / TAU)
    u = np.array([np.cos(th), np.sin(th)]); w = np.array([-np.sin(th), np.cos(th)])
    W = abs(w[0]) + abs(w[1])
    pts = np.array([(i, j) for i in range(-1, 9) for j in range(-1, 6)], float)
    inside = (pts @ w >= -1e-9) & (pts @ w < W - 1e-9)
    ax.plot(pts[:, 0], pts[:, 1], "o", ms=2.5, color="0.7")
    ax.plot(pts[inside, 0], pts[inside, 1], "o", ms=4, color=BLUE)
    L = 9.5
    ax.plot([0, L * u[0]], [0, L * u[1]], color=VERM, lw=1.3)
    ax.plot([w[0] * W, w[0] * W + L * u[0]], [w[1] * W, w[1] * W + L * u[1]], color="0.5", lw=0.7, ls="--")
    ax.add_patch(Polygon([[0, 0], [L * u[0], L * u[1]], [w[0] * W + L * u[0], w[1] * W + L * u[1]],
                          [w[0] * W, w[1] * W]], fc=_light(VERM, 0.85), ec="none", zorder=0))
    sp = pts[inside]
    sp = sp[np.argsort(sp @ u)]
    proj = (sp @ u)
    for p, t in zip(sp, proj):
        if 0 <= t <= L:
            q = t * u
            ax.plot([p[0], q[0]], [p[1], q[1]], color=BLUE, lw=0.5, alpha=0.6)
            ax.plot(*q, "o", ms=3.5, color=VERM, zorder=4)
    seq = ""
    for a_, b_ in zip(sp[:-1], sp[1:]):
        if 0 <= a_ @ u and b_ @ u <= L:
            d = b_ - a_
            seq += "L" if abs(d[0] - 1) < 1e-9 and abs(d[1]) < 1e-9 else "S"
    ax.set_xlim(-1.2, 9.3); ax.set_ylim(-2.4, 7.6)
    ax.set_title("(c) Fibonacci chain", fontsize=9.5, loc="left")
    ax.text(-1.0, 7.4, "L → LS,  S → L:\n" + " ".join(word[:21]) + " …", fontsize=7.4, va="top",
            family="DejaVu Sans Mono")
    ax.text(4.5, -1.3, "cut through a square lattice at slope 1/τ:\nprojected points form the same L/S sequence",
            fontsize=7.2, ha="center", va="top", color="0.3")
    ax.text(L * u[0] + 0.1, L * u[1] - 0.2, "slope\n1/τ", fontsize=7.2, color=VERM, va="top")

    # (d) incommensurately modulated chain and its diffraction
    sub = gs[1, 1].subgridspec(2, 1, height_ratios=[0.8, 1.0], hspace=0.6)
    ax = fig.add_subplot(sub[0])
    q = 1 / 3.7
    n = np.arange(0, 19)
    amp_ = 0.12
    xs = n + amp_ * np.sin(2 * np.pi * q * n)
    ax.plot(n, np.zeros_like(n), "|", color="0.6", ms=8)
    ax.plot(xs, np.zeros_like(xs), "o", color=BLUE, ms=6, zorder=3)
    for xi, ni in zip(xs, n):
        ax.annotate("", xy=(xi, 0.25), xytext=(ni, 0.25), arrowprops=dict(arrowstyle="-|>", lw=0.6, color=VERM,
                                                                          mutation_scale=5))
    tt = np.linspace(0, 18, 400)
    ax.plot(tt, 0.55 + 0.25 * np.sin(2 * np.pi * q * tt), color=VERM, lw=0.9)
    ax.text(18.3, 0.55, "displacement wave,\nλ = 3.7$a$ (incommensurate)", fontsize=7, va="center", color=VERM)
    ax.set_xlim(-0.5, 18.5); ax.set_ylim(-0.4, 0.95)
    ax.axis("off")
    ax.set_title("(d) modulated chain and its diffraction", fontsize=9.5, loc="left")
    ax = fig.add_subplot(sub[1])
    h = np.linspace(-0.2, 3.2, 3000)
    Ntot = 600
    xs_all = np.arange(Ntot) + amp_ * np.sin(2 * np.pi * q * np.arange(Ntot))
    F = np.exp(2j * np.pi * np.outer(h, xs_all)).sum(1)
    Ih = np.abs(F) ** 2 / Ntot ** 2
    ax.plot(h, Ih, color=INK, lw=0.8)
    for hh in range(0, 4):
        for m, col in ((1, VERM), (2, ORANGE)):
            for sgn in (1, -1):
                pos = hh + sgn * m * q
                if -0.2 < pos < 3.2:
                    ax.plot(pos, 1.08, "v", color=col, ms=3.5, clip_on=False)
    ax.set_yscale("symlog", linthresh=1e-3)
    ax.set_ylim(0, 1.15)
    ax.set_xlim(-0.2, 3.2)
    ax.set_xlabel("$h$ (units of $a^*$)")
    ax.set_ylabel("$I$ (log)")
    ax.set_yticks([])
    ax.text(1.0, 1.04, "main peaks at integer $h$; satellites (▼) at $h \\pm q$ (red),\n$h \\pm 2q$ (orange); $q$ = 0.27 $a^*$",
            fontsize=6.8, ha="right", va="bottom", transform=ax.transAxes)
    save(fig, "03", "fig-3-6-quasicrystal-modulated")


if __name__ == "__main__":
    symmetry_operations()
    restriction_bravais()
    wyckoff_positions()
    stereographic_pole_figures()
    ordering_apb()
    quasicrystal_modulated()
