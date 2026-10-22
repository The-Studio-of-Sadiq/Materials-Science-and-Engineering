"""Figures for Chapter 19 — Polymer Synthesis and Molecular Structure.

Run from the repository root:  python figures/scripts/ch19.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon

from figstyle import new_fig, schematic, save, COLORS, INK

A_COL = "#1F4E79"   # dark bead (A)
B_COL = "#BFD7EA"   # light bead (B)


# ---------------------------------------------------------------- 19.1
def step_vs_chain():
    fig, ax = new_fig(6.4, 3.9)
    p = np.linspace(0.0, 0.9995, 4000)
    ax.semilogy(p, 1 / (1 - p), color=COLORS[0], label="step growth,  $X_n = 1/(1-p)$")
    pr = np.linspace(0.01, 0.95, 200)
    ax.semilogy(pr, 1500 * (1 - 0.12 * pr), color=COLORS[1],
                label="free-radical chain growth (high polymer at once)")
    pl = np.linspace(0.001, 1.0, 400)
    ax.semilogy(pl, 1000 * pl, color=COLORS[2], ls="--",
                label=r"living anionic,  $X_n = p\,[M]_0/[I]_0$,  $[M]_0/[I]_0=1000$")
    ax.plot([0.99], [100], "o", color=COLORS[0], ms=5)
    ax.annotate("$p = 0.99 \\Rightarrow X_n = 100$", xy=(0.99, 100), xytext=(0.62, 230),
                fontsize=9, arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.8))
    ax.plot([0.9], [10], "o", color=COLORS[0], ms=4)
    ax.annotate("$p = 0.9$: only $X_n = 10$", xy=(0.9, 10), xytext=(0.5, 4),
                fontsize=9, arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.8))
    ax.plot([0.999], [1000], "o", color=COLORS[0], ms=4)
    ax.annotate("$p = 0.999 \\Rightarrow X_n = 1000$", xy=(0.999, 1000), xytext=(0.55, 3200),
                fontsize=9, arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.8))
    ax.set_xlim(0, 1.0)
    ax.set_ylim(1, 1e4)
    ax.set_xlabel("monomer conversion (extent of reaction) $p$")
    ax.set_ylabel("number-average degree of\npolymerization $X_n$")
    ax.legend(loc="center", fontsize=8.5, bbox_to_anchor=(0.45, 0.40))
    save(fig, "19", "fig-19-1-step-vs-chain-growth")


# ---------------------------------------------------------------- 19.2
def carothers():
    fig, ax = new_fig(6.4, 4.0)
    p = np.linspace(0.90, 0.99995, 3000)
    styles = [(1.000, COLORS[0], "-"), (0.999, COLORS[1], "-"),
              (0.99, COLORS[2], "-"), (0.98, COLORS[3], "-")]
    ax.axhspan(100, 250, color="#E8E8E8", zorder=0)
    ax.text(0.902, 135, "engineering polyamides and polyesters,  $X_n \\approx 100$–$250$",
            fontsize=8.5, va="center", color="#444444")
    for r, c, ls in styles:
        Xn = (1 + r) / (1 + r - 2 * r * p)
        ax.semilogy(p, Xn, color=c, ls=ls, label=f"$r$ = {r:.3f}")
        if r < 1:
            lim = (1 + r) / (1 - r)
            ax.axhline(lim, color=c, lw=0.7, ls=":")
            below = r == 0.98
            ax.text(0.9025 if r != 0.999 else 0.94, lim * (0.95 if below else 1.04),
                    f"plateau $(1+r)/(1-r)$ = {lim:.0f}", color=c,
                    fontsize=8, va="top" if below else "bottom")
    ax.plot([0.99], [100], "o", color=COLORS[0], ms=5, zorder=5)
    ax.annotate("$r=1$: $X_n=100$", xy=(0.99, 100), xytext=(0.955, 330), fontsize=8.5,
                arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK))
    ax.plot([0.99], [66.8], "s", color=COLORS[2], ms=5, zorder=5)
    ax.annotate("$r=0.99$: $X_n=66.8$", xy=(0.99, 66.8), xytext=(0.925, 40), fontsize=8.5,
                arrowprops=dict(arrowstyle="-|>", lw=0.8, color=INK))
    ax.set_xlim(0.90, 1.0)
    ax.set_ylim(10, 1e4)
    ax.set_xlabel("extent of reaction $p$")
    ax.set_ylabel("number-average degree of polymerization $X_n$")
    ax.legend(loc="center left", fontsize=8.5, bbox_to_anchor=(0.0, 0.62))
    m0 = 113.16
    sec = ax.secondary_yaxis("right", functions=(lambda x: x * m0, lambda y: y / m0))
    sec.set_ylabel("$M_n$ of nylon-6,6 (g/mol)")
    ax.spines["right"].set_visible(True)
    save(fig, "19", "fig-19-2-carothers")


# ---------------------------------------------------------------- 19.3
def _lognormal_w(logM, Mn, D):
    """Weight distribution dw/dlogM of a log-normal number distribution (peak-normalized)."""
    s2 = np.log(D)
    mu_w = np.log(Mn) + 0.5 * s2          # mean of ln M in the weight distribution
    x = logM * np.log(10)
    w = np.exp(-(x - mu_w) ** 2 / (2 * s2))
    return w / w.max()


def mw_distribution():
    fig, ax = new_fig(6.4, 4.6)
    logM = np.linspace(3, 7, 1200)
    w1 = _lognormal_w(logM, 5e4, 2.0)
    w2 = _lognormal_w(logM, 1e5, 1.05)
    # bimodal PE100: two broad components peaking near 2e4 and 4e5 g/mol
    def comp(peak, sig):
        return np.exp(-(logM - np.log10(peak)) ** 2 / (2 * sig ** 2))
    w3 = 0.95 * comp(2e4, 0.33) + 0.75 * comp(4e5, 0.38)
    w3 /= w3.max()
    ax.fill_between(logM, w1, color=COLORS[0], alpha=0.12)
    ax.plot(logM, w1, color=COLORS[0], label="log-normal, $M_n$ = 50 000, $M_w$ = 100 000 g/mol, Đ = 2.0")
    ax.plot(logM, w2, color=COLORS[1], ls="--", label="anionic PS standard, $M_n$ = 100 000, Đ = 1.05")
    ax.plot(logM, w3, color=COLORS[2], ls=":", lw=2.2, label="bimodal PE100 pipe resin")
    avgs = [("$M_n$", 5.0e4, "5.0", 1.08, "right"), ("$M_v$", 9.0e4, "9.0", 1.24, "right"),
            ("$M_w$", 1.0e5, "1.0", 1.24, "left"), ("$M_z$", 2.0e5, "2.0", 1.08, "left")]
    for lab, M, mant, yt, ha in avgs:
        x = np.log10(M)
        ax.plot([x, x], [0, yt + 0.07], color=INK, lw=0.8)
        extra = " ($a$ = 0.7)" if lab == "$M_v$" else ""
        dx = -0.03 if ha == "right" else 0.03
        ax.text(x + dx, yt, f"{lab} = {mant}×10$^{4 if M < 1e5 else 5}${extra}", ha=ha, va="bottom", fontsize=8)
    ax.text(6.98, 1.45, "$M_n$ ↔ toughness\n$M_w$ ↔ melt viscosity\n$M_z$ ↔ melt elasticity",
            fontsize=8.5, va="top", ha="right", bbox=dict(fc="white", ec="#BBBBBB", lw=0.6))
    ax.set_xlim(3, 7)
    ax.set_ylim(0, 1.5)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xlabel("$\\log_{10}(M$ / g mol$^{-1})$")
    ax.set_ylabel("$dw/d\\log M$ (normalized to peak)")
    ax.legend(loc="upper center", fontsize=8, bbox_to_anchor=(0.5, -0.16), ncol=1)
    save(fig, "19", "fig-19-3-mw-distribution")


# ---------------------------------------------------------------- 19.4
def _beads(ax, pts, colors, r=0.075):
    pts = np.asarray(pts)
    ax.plot(pts[:, 0], pts[:, 1], color="#555555", lw=0.8, zorder=1)
    for (x, y), c in zip(pts, colors):
        ax.add_patch(Circle((x, y), r, fc=c, ec=INK, lw=0.5, zorder=2))


def _serpentine(x0, y0, n, per_row=10, dx=0.17, dy=0.24):
    pts = []
    for i in range(n):
        row, k = divmod(i, per_row)
        xx = x0 + (k if row % 2 == 0 else per_row - 1 - k) * dx
        pts.append((xx, y0 - row * dy))
    return pts


def copolymer_architectures():
    fig, ax = schematic(6.8, 4.6, xlim=(0, 12.6), ylim=(0.4, 9.3))
    ax.text(0.05, 9.05, "(a) Sequence (A dark, B light)", fontsize=10, weight="bold", va="center")
    ax.text(0.05, 5.6, "(b) Chain topology", fontsize=10, weight="bold", va="center")
    rng = np.random.default_rng(7)
    cw = 2.1
    x0s = [0.15 + i * cw for i in range(6)]
    ytop = 8.3
    A, B = A_COL, B_COL
    seqs = {
        0: [A] * 30,
        1: [A if v else B for v in rng.random(30) < 0.55],
        2: [A, B] * 15,
        3: [A] * 20 + [B] * 20,
        4: [A] * 10 + [B] * 20 + [A] * 10,
    }
    names = ["homopolymer", "random", "alternating", "diblock", "triblock ABA", "graft"]
    examples = ["PS, PE", "SBR", "SMA", "PS-b-PMMA", "SBS", "HIPS, ABS"]
    for i in range(5):
        pts = _serpentine(x0s[i] + 0.12, ytop, len(seqs[i]))
        _beads(ax, pts, seqs[i])
    # graft: A backbone with three B side chains
    gx0 = x0s[5] + 0.12
    back = [(gx0 + k * 0.17, ytop) for k in range(11)]
    _beads(ax, back, [A] * 11)
    for k in (2, 5, 8):
        bx, by = back[k]
        side = [(bx, by)] + [(bx + 0.06 * j, by - 0.2 * j) for j in range(1, 5)]
        ax.plot([p[0] for p in side], [p[1] for p in side], color="#555555", lw=0.8, zorder=1)
        for (x, y) in side[1:]:
            ax.add_patch(Circle((x, y), 0.075, fc=B, ec=INK, lw=0.5, zorder=2))
    for i in range(6):
        cx = x0s[i] + 0.12 + 9 * 0.17 / 2
        ax.text(cx, 6.75, names[i], ha="center", fontsize=8.5, weight="bold")
        ax.text(cx, 6.35, examples[i], ha="center", fontsize=8, color="#444444")

    # ---- topology row
    ybase = 3.7
    cw2 = 2.5
    xs = [0.2 + i * cw2 for i in range(5)]
    lc = INK

    def wiggle(x0, x1, y, amp=0.08, nw=5, n=120):
        t = np.linspace(0, 1, n)
        return x0 + (x1 - x0) * t, y + amp * np.sin(2 * np.pi * nw * t)

    # linear
    X, Y = wiggle(xs[0] + 0.1, xs[0] + 2.1, ybase + 0.4)
    ax.plot(X, Y, color=lc, lw=1.6)
    # short-chain branched
    X, Y = wiggle(xs[1] + 0.1, xs[1] + 2.1, ybase + 0.4)
    ax.plot(X, Y, color=lc, lw=1.6)
    for k, xb in enumerate(np.linspace(xs[1] + 0.3, xs[1] + 1.9, 7)):
        yb = ybase + 0.4 + 0.08 * np.sin(2 * np.pi * 5 * (xb - xs[1] - 0.1) / 2.0)
        s = 1 if k % 2 == 0 else -1
        ax.plot([xb, xb + 0.08], [yb, yb + s * 0.25], color=COLORS[1], lw=1.4)
    # long-chain branched (branches of branches)
    xL = xs[2]
    main = np.array([[xL + 0.1, ybase + 0.2], [xL + 0.6, ybase + 0.45], [xL + 1.1, ybase + 0.3],
                     [xL + 1.6, ybase + 0.5], [xL + 2.1, ybase + 0.35]])
    ax.plot(main[:, 0], main[:, 1], color=lc, lw=1.6)
    br = [[(xL + 0.6, ybase + 0.45), (xL + 0.7, ybase + 1.0), (xL + 0.5, ybase + 1.45)],
          [(xL + 0.7, ybase + 1.0), (xL + 1.05, ybase + 1.3)],
          [(xL + 1.1, ybase + 0.3), (xL + 1.25, ybase - 0.3), (xL + 1.0, ybase - 0.75)],
          [(xL + 1.25, ybase - 0.3), (xL + 1.6, ybase - 0.45)],
          [(xL + 1.6, ybase + 0.5), (xL + 1.85, ybase + 1.1)]]
    for b in br:
        b = np.array(b)
        ax.plot(b[:, 0], b[:, 1], color=COLORS[1], lw=1.4)
    # star
    cx, cy = xs[3] + 1.1, ybase + 0.35
    for k in range(6):
        ang = np.pi / 2 + k * np.pi / 3
        t = np.linspace(0, 1, 40)
        rr = 0.95 * t
        wob = 0.08 * np.sin(2 * np.pi * 2.5 * t)
        xx = cx + rr * np.cos(ang) - wob * np.sin(ang)
        yy = cy + rr * np.sin(ang) + wob * np.cos(ang)
        ax.plot(xx, yy, color=lc, lw=1.5)
    ax.add_patch(Circle((cx, cy), 0.07, fc=COLORS[1], ec=INK, lw=0.6, zorder=3))
    # network
    nx0 = xs[4] + 0.15
    rngn = np.random.default_rng(3)
    nodes = np.array([[nx0 + 0.3 + 0.7 * i + rngn.normal(0, 0.06),
                       ybase - 0.5 + 0.6 * j + rngn.normal(0, 0.06)] for j in range(3) for i in range(3)])
    edges = [(0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (7, 8), (0, 3), (3, 6), (1, 4), (4, 7), (2, 5), (5, 8)]
    for a, b in edges:
        p0, p1 = nodes[a], nodes[b]
        t = np.linspace(0, 1, 30)
        d = p1 - p0
        nrm = np.array([-d[1], d[0]]) / np.hypot(*d)
        pts = p0[None, :] + t[:, None] * d[None, :] + 0.06 * np.sin(np.pi * 2 * t)[:, None] * nrm[None, :]
        ax.plot(pts[:, 0], pts[:, 1], color=lc, lw=1.3)
    for n in nodes:
        ax.add_patch(Circle(n, 0.07, fc=COLORS[1], ec=INK, lw=0.6, zorder=3))
    # dangling end
    de = nodes[2]
    ax.plot([de[0], de[0] + 0.25, de[0] + 0.45], [de[1], de[1] - 0.25, de[1] - 0.15], color=COLORS[0], lw=1.5)
    ax.text(de[0] + 0.25, de[1] - 0.5, "dangling\nend", fontsize=7, ha="center", va="top", color=COLORS[0])
    # loop
    lp = nodes[6]
    th = np.linspace(0, 2 * np.pi, 60)
    ax.plot(lp[0] - 0.2 + 0.2 * np.cos(th), lp[1] + 0.2 + 0.2 * np.sin(th), color=COLORS[0], lw=1.4)
    ax.text(lp[0] - 0.42, lp[1] + 0.48, "loop", fontsize=7, ha="center", color=COLORS[0])
    ax.text(nodes[4][0] + 0.2, nodes[4][1] + 0.1, "junction", fontsize=7, ha="center", va="bottom",
            color="#444444")
    tnames = ["linear", "short-chain\nbranched", "long-chain\nbranched", "star", "crosslinked\nnetwork"]
    tex = ["HDPE", "LLDPE", "LDPE", "oil viscosity\nmodifiers", "cured epoxy,\nrubber"]
    for i in range(5):
        cx = xs[i] + 1.1
        ax.text(cx, 2.05, tnames[i], ha="center", va="top", fontsize=8.5, weight="bold")
        ax.text(cx, 1.3, tex[i], ha="center", va="top", fontsize=8, color="#444444")
    save(fig, "19", "fig-19-4-copolymer-architectures")


# ---------------------------------------------------------------- 19.5
def _wedge(ax, x0, y0, x1, y1, w=0.09):
    d = np.array([x1 - x0, y1 - y0])
    n = np.array([-d[1], d[0]]) / np.hypot(*d)
    poly = [(x0, y0), (x1 + n[0] * w, y1 + n[1] * w), (x1 - n[0] * w, y1 - n[1] * w)]
    ax.add_patch(Polygon(poly, closed=True, fc=INK, ec=INK, lw=0.5))


def _dash(ax, x0, y0, x1, y1, w=0.09, n=6):
    d = np.array([x1 - x0, y1 - y0])
    nn = np.array([-d[1], d[0]]) / np.hypot(*d)
    for t in np.linspace(0.15, 1.0, n):
        cx, cy = x0 + t * d[0], y0 + t * d[1]
        hw = w * t
        ax.plot([cx - nn[0] * hw, cx + nn[0] * hw], [cy - nn[1] * hw, cy + nn[1] * hw], color=INK, lw=1.0)


def tacticity():
    fig, ax = schematic(6.8, 4.4, xlim=(0, 15.6), ylim=(-0.1, 9.2))
    dx, dy = 0.55, 0.32
    rows = [
        ("isotactic", "WWWWW", "meso dyads ($m$), $mmmm$ > 95 %\ncrystalline, $T_m$ ≈ 165 °C"),
        ("syndiotactic", "WDWDW", "racemo dyads ($r$)\ncrystalline, $T_m$ ≈ 130–150 °C"),
        ("atactic", "WDDWW", "random $m$/$r$ sequence\namorphous, $T_g$ ≈ −10 °C, adhesive"),
    ]
    ys = [7.3, 4.4, 1.5]
    for (name, pat, lab), y0 in zip(rows, ys):
        xs = 0.6 + np.arange(10) * dx
        yc = np.where(np.arange(10) % 2 == 0, y0, y0 + dy * 2)
        # chain ends
        ax.plot([xs[0] - dx * 0.8, xs[0]], [y0 + dy * 2, y0], color=INK, lw=1.6)
        ax.plot(xs, yc, color=INK, lw=1.6, marker="o", ms=3.5, mfc=INK)
        ax.plot([xs[-1], xs[-1] + dx * 0.8], [yc[-1], y0], color=INK, lw=1.6)
        # stereocentres: odd-index (top-apex) carbons carry CH3
        for k, s in zip(range(1, 10, 2), pat):
            x1, y1 = xs[k], yc[k]
            if s == "W":
                _wedge(ax, x1, y1, x1, y1 + 0.85)
            else:
                _dash(ax, x1, y1, x1, y1 + 0.85)
            ax.text(x1, y1 + 0.95, "CH$_3$", ha="center", va="bottom", fontsize=7.5)
        ax.text(6.5, y0 + 0.95, name, fontsize=10, weight="bold", va="bottom")
        ax.text(6.5, y0 + 0.85, lab, fontsize=8.8, va="top")
    # legend for wedge/dash
    _wedge(ax, 0.3, 0.25, 0.75, 0.25, w=0.07)
    ax.text(0.85, 0.25, "toward viewer", fontsize=7.5, va="center")
    _dash(ax, 3.3, 0.25, 3.75, 0.25, w=0.07)
    ax.text(3.85, 0.25, "away from viewer (backbone in page plane)", fontsize=7.5, va="center")

    # inset: 3_1 helix viewed along chain axis
    cx, cy, R = 14.3, 7.0, 0.55
    ang = np.pi / 2 + np.arange(3) * 2 * np.pi / 3
    pts = np.c_[cx + R * np.cos(ang), cy + R * np.sin(ang)]
    ax.add_patch(Polygon(pts, closed=True, fill=False, ec=INK, lw=1.4))
    for a, (x, y) in zip(ang, pts):
        ax.add_patch(Circle((x, y), 0.08, fc=INK, ec=INK))
        x2, y2 = cx + (R + 0.55) * np.cos(a), cy + (R + 0.55) * np.sin(a)
        ax.plot([x, x2], [y, y2], color=COLORS[1], lw=1.4)
        ax.add_patch(Circle((x2, y2), 0.15, fc=COLORS[1], ec=INK, lw=0.6))
    ax.add_patch(Circle((cx, cy), 0.06, fc="none", ec=INK, lw=0.8))
    ax.text(cx, cy - 1.55, "iPP $3_1$ helix\n(view along\nchain axis;\nCH$_3$ outward)",
            ha="center", va="top", fontsize=7.5)
    save(fig, "19", "fig-19-5-tacticity")


# ---------------------------------------------------------------- 19.6
def polymer_pyramid():
    fig, ax = new_fig(6.6, 5.0)
    T0, Tapex, W = 40.0, 300.0, 5.0

    def hw(T):
        return W * (Tapex - T) / (Tapex - T0)

    tiers = [(T0, 100, "#DCEAF5"), (100, 150, "#FBE3CF"), (150, Tapex, "#F6D0D0")]
    for a, b, c in tiers:
        poly = [(-hw(a), a), (hw(a), a), (hw(b), b), (-hw(b), b)]
        ax.add_patch(Polygon(poly, closed=True, fc=c, ec="none"))
    ax.add_patch(Polygon([(-W, T0), (W, T0), (0, Tapex)], closed=True, fill=False, ec=INK, lw=1.2))
    for b in (100, 150):
        ax.plot([-hw(b), hw(b)], [b, b], color=INK, lw=0.9)
    ax.plot([0, 0], [T0, Tapex], color=INK, lw=0.9, ls="--")
    ax.text(-2.4, 44, "AMORPHOUS", ha="center", va="bottom", fontsize=8.5, weight="bold", color="#333")
    ax.text(2.4, 44, "SEMICRYSTALLINE", ha="center", va="bottom", fontsize=8.5, weight="bold", color="#333")

    # tier labels outside the triangle on the left
    ax.text(-5.3, 72, "COMMODITY\n≤ 60–100 °C\n1–2 USD/kg", ha="right", va="center", fontsize=8.5)
    ax.text(-5.3, 125, "ENGINEERING\n100–150 °C\n2–6 USD/kg", ha="right", va="center", fontsize=8.5)
    ax.text(-5.3, 215, "HIGH-\nPERFORMANCE\n150–260 °C\n10–100 USD/kg", ha="right", va="center",
            fontsize=8.5)

    # (name, continuous-use T in °C, x offset from centre line); values from the Sec. 19.7 table
    # where listed, otherwise typical handbook values (marked *)
    amorph = [("PVC", 55, -1.3), ("PS", 65, -1.3), ("PMMA", 78, -2.5), ("ABS*", 80, -1.0),
              ("PPO*", 105, -1.2), ("PC", 120, -1.2), ("PSU*", 150, -1.0),
              ("PEI", 175, -1.6), ("PES*", 180, -0.6), ("PAI*", 250, -0.45)]
    semi = [("PE (HDPE)", 70, 1.3), ("PP", 90, 0.9), ("PA6*", 90, 1.9), ("POM", 95, 2.6),
            ("PA66", 100, 1.2), ("PET", 110, 1.2), ("PBT*", 120, 1.2), ("PPS", 210, 0.6),
            ("LCP*", 230, 0.3), ("PEEK", 250, 0.25), ("PTFE", 260, 0.1)]
    for name, T, x in amorph:
        ax.plot(x, T, "o", ms=3.5, color=COLORS[0])
        ax.text(x - 0.12, T, name, ha="right", va="center", fontsize=8)
    for name, T, x in semi:
        ax.plot(x, T, "o", ms=3.5, color=COLORS[1])
        ax.text(x + 0.12, T, name, ha="left", va="center", fontsize=8)
    ax.text(0, 30, "* typical handbook value (not in the Section 19.7 table)", ha="center",
            fontsize=7.5, color="#555555")

    ax.set_xlim(-8.6, 5.6)
    ax.set_ylim(25, 300)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(True)
    ax.set_xticks([])
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    ax.set_yticks([50, 100, 150, 200, 250])
    ax.spines["right"].set_bounds(50, 260)
    ax.set_ylabel("approximate continuous-use temperature (°C)")
    save(fig, "19", "fig-19-6-polymer-pyramid")


if __name__ == "__main__":
    step_vs_chain()
    carothers()
    mw_distribution()
    copolymer_architectures()
    tacticity()
    polymer_pyramid()
