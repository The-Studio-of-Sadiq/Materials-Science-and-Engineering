"""Figures for Chapter 18 — Cement, Concrete and Construction Materials.

Run from the repository root:  python figures/scripts/ch18.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle, Ellipse, Wedge, FancyBboxPatch
from matplotlib.collections import LineCollection
from scipy.special import erf, erfinv
from scipy.integrate import cumulative_trapezoid

from figstyle import new_fig, save, COLORS, INK

RNG = np.random.default_rng(18)


# ---------------------------------------------------------------- 18.1
def heat_flow(t):
    """Model heat-flow curve of a CEM I paste at 20 °C (mW/g); t in hours."""
    t = np.asarray(t, float)
    init = 25.0 * np.exp(-t / 0.06)                                   # wetting, C3A, ettringite
    base = 0.30 * np.ones_like(t)                                    # dormant level
    main = 1.85 * np.exp(-(np.log(np.maximum(t, 1e-6) / 9.5) / 0.50) ** 2)   # C3S
    sh = 0.75 * np.exp(-((t - 15.5) / 2.6) ** 2)                      # renewed C3A
    tail = 0.50 * (1 / (1 + np.exp(-(t - 7.0) / 1.2))) * (48.0 / np.maximum(t, 1)) ** 0.6
    base = base * (1 / (1 + np.exp((t - 6.0) / 1.0)))
    return init + base + main + sh + tail


def fig_hydration():
    fig, ax = new_fig(6.4, 4.0)
    t = np.linspace(0.0, 48, 4801)
    q = heat_flow(t)
    Q = cumulative_trapezoid(q * 3.6, t, initial=0)                  # mW/g × h → J/g
    ax.plot(t, q, color=COLORS[0])
    ax.set_xlim(0, 48)
    ax.set_ylim(0, 4)
    ax.set_xlabel("Time after mixing (h)")
    ax.set_ylabel("Heat flow (mW per g cement)", color=COLORS[0])
    ax.tick_params(axis="y", colors=COLORS[0])
    ax2 = ax.twinx()
    ax2.spines["right"].set_visible(True)
    ax2.plot(t, Q, color=COLORS[1], ls="--")
    ax2.set_ylim(0, 300)
    ax2.set_ylabel("Cumulative heat (J/g)", color=COLORS[1])
    ax2.tick_params(axis="y", colors=COLORS[1])
    ax2.text(46, Q[-1] + 8, f"≈ {Q[-1]:.0f} J/g at 48 h", fontsize=8, color=COLORS[1], ha="right",
             va="bottom")
    # annotations
    ax.annotate("initial peak (off scale):\nwetting, C₃A, ettringite",
                xy=(0.12, 3.6), xytext=(1.0, 3.5), fontsize=7.8, va="center",
                arrowprops=dict(arrowstyle="-|>", lw=0.8, mutation_scale=7))
    ax.annotate("main peak:\nC₃S hydration\n(C–S–H + CH)", xy=(9.5, heat_flow(9.5)),
                xytext=(14.0, 3.12), fontsize=7.8, va="center",
                arrowprops=dict(arrowstyle="-", lw=0.7))
    ax.annotate("shoulder: renewed C₃A\nreaction (sulfate depletion)", xy=(15.5, heat_flow(15.5)),
                xytext=(22, 2.7), fontsize=7.8, va="center",
                arrowprops=dict(arrowstyle="-", lw=0.7))
    ax.annotate("dormant ≈ 0.3 mW/g", xy=(2.0, heat_flow(2.0)), xytext=(3.0, 0.15),
                fontsize=7.5, arrowprops=dict(arrowstyle="-", lw=0.6))
    # stage boundaries
    for xb in (0.5, 3.0, 10.0):
        ax.axvline(xb, color="0.7", ls=":", lw=0.9)
    for x0, x1, lab in ((0, 0.5, "I"), (0.5, 3.0, "II"), (3.0, 10.0, "III"), (10.0, 48, "IV")):
        ax.text((x0 + x1) / 2 if lab != "IV" else 30, 3.82, lab, ha="center", fontsize=9,
                fontweight="bold", color="0.35")
    ax.text(47.5, 0.22, "I initial · II induction · III acceleration · IV deceleration",
            fontsize=7, ha="right", color="0.35")
    for ts, lab, tx in ((4.0, "initial set", (0.8, 1.25)), (6.0, "final set", (1.4, 2.2))):
        ax.annotate(lab, xy=(ts, heat_flow(ts)), xytext=tx, fontsize=7.5, ha="left",
                    arrowprops=dict(arrowstyle="-|>", lw=0.8, mutation_scale=7, color=COLORS[2]),
                    color=COLORS[2])
    print(f"18.1: peak {q[(t > 5)].max():.2f} mW/g at {t[t > 5][q[t > 5].argmax()]:.1f} h; "
          f"q(48) = {q[-1]:.2f}; Q(48) = {Q[-1]:.0f} J/g")
    save(fig, "18", "fig-18-1-hydration-calorimetry")


# ---------------------------------------------------------------- 18.2
def fig_strength_wc():
    fig, ax = new_fig(6.4, 4.0)
    wc = np.linspace(0.30, 0.80, 300)
    f28 = 117 / 13 ** wc
    age = {3: COLORS[4], 7: COLORS[2], 28: COLORS[0], 90: COLORS[3]}
    for d, c in age.items():
        k = np.exp(0.25 * (1 - np.sqrt(28 / d)))
        good = wc >= 0.35
        ax.plot(wc[good], k * f28[good], color=c, lw=2.2 if d == 28 else 1.5,
                label=f"{d} d (× {k:.2f})" if d != 28 else r"28 d: $f_c = 117/13^{\,w/c}$")
        # compaction-limited branch
        w2 = np.linspace(0.30, 0.35, 30)
        drop = k * 117 / 13 ** 0.35 * (1 - 3.5 * (0.35 - w2) ** 1.3)
        ax.plot(w2, drop, color=c, lw=1.4 if d == 28 else 1.0, ls="--")
    aci = np.array([(0.42, 40), (0.47, 35), (0.54, 30), (0.61, 25), (0.69, 20)])
    ax.plot(aci[:, 0], aci[:, 1], "o", mfc="white", mec=INK, ms=6, mew=1.2,
            label="ACI 211.1 table (28 d)", zorder=5)
    ax.plot(0.43, 38.3, "*", color=COLORS[1], ms=12, zorder=6)
    ax.annotate("worked example:\nw/c = 0.43, $f_{cr}$ = 38.3 MPa", xy=(0.43, 38.3),
                xytext=(0.50, 47), fontsize=8, color=COLORS[1],
                arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[1]))
    ax.annotate("incomplete compaction\n(no superplasticizer)", xy=(0.322, 46), xytext=(0.305, 8),
                fontsize=7.8, arrowprops=dict(arrowstyle="-", lw=0.7))
    ax.set_xlim(0.30, 0.80)
    ax.set_ylim(0, 60)
    ax.set_xlabel("Water–cement ratio, w/c")
    ax.set_ylabel("Cylinder compressive strength (MPa)")
    ax.legend(fontsize=8, loc="upper right", title="age", title_fontsize=8)
    save(fig, "18", "fig-18-2-strength-wc-ratio")


# ---------------------------------------------------------------- 18.3
def fig_chloride():
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.8, 3.7), gridspec_kw=dict(width_ratios=[1.5, 1]))
    fig.subplots_adjust(wspace=0.32)
    Cs, D = 3.0, 1.0e-12
    yr = 3.156e7
    x = np.linspace(0, 100, 400)
    for ty, c in ((10, COLORS[0]), (25, COLORS[2]), (50, COLORS[1])):
        C = Cs * (1 - erf(x * 1e-3 / (2 * np.sqrt(D * ty * yr))))
        ax.plot(x, C, color=c, label=f"{ty} years")
        chk = {xx: Cs * (1 - erf(xx * 1e-3 / (2 * np.sqrt(D * ty * yr)))) for xx in (10, 20, 40, 60, 80)}
        print(f"18.3 {ty} y:", {k: round(v, 2) for k, v in chk.items()})
    ax.axhline(0.4, color=INK, ls="--", lw=1.0)
    ax.text(99, 0.45, "critical chloride content 0.4 %", fontsize=7.8, ha="right", va="bottom")
    for xc in (40, 60):
        ax.axvline(xc, color="0.45", ls=":", lw=1.1)
        ax.text(xc + 1, 2.85, f"{xc} mm\ncover", fontsize=7.5, va="top", color="0.3")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 3.0)
    ax.set_xlabel("Depth from surface (mm)")
    ax.set_ylabel("Chloride (% by mass of cement)")
    ax.legend(fontsize=8, loc="upper right", bbox_to_anchor=(1.0, 0.82),
              title="$C_s$ = 3.0 %, $D$ = 1.0×10$^{-12}$ m²/s", title_fontsize=7.2)
    ax.set_title("(a) chloride profiles", fontsize=9, loc="left")
    z = erfinv(1 - 0.4 / 3.0)
    cov = np.linspace(20, 80, 200)
    for Dv, c, lab in ((1e-12, COLORS[0], "$D$ = 1×10$^{-12}$ (CEM I)"),
                       (2e-13, COLORS[2], "$D$ = 2×10$^{-13}$ (slag)")):
        ti = (cov * 1e-3 / (2 * z)) ** 2 / Dv / yr
        bx.plot(cov, ti, color=c, label=lab)
        for xc in (40, 60):
            tv = (xc * 1e-3 / (2 * z)) ** 2 / Dv / yr
            bx.plot(xc, tv, "o", color=c, ms=4.5)
            bx.text(xc - 1.5, tv * 1.18, f"{tv:.0f} y", fontsize=7.5, ha="right", color=c)
    print(f"18.3 z = {z:.3f}")
    bx.set_yscale("log")
    bx.set_ylim(1, 200)
    bx.set_xlim(20, 80)
    bx.set_xlabel("Cover (mm)")
    bx.set_ylabel("Time to initiation (years)")
    bx.legend(fontsize=7.2, loc="lower right")
    bx.set_title("(b) time to corrosion initiation", fontsize=9, loc="left")
    save(fig, "18", "fig-18-3-chloride-profiles")


# ---------------------------------------------------------------- 18.4
def _stress_block(ax, top, bot, title, scale=25.0):
    """Linear stress block over depth 0 (top) .. 600 (bottom); compression (<0) drawn left."""
    H = 600.0
    ax.set_xlim(-scale, scale)
    ax.set_ylim(H + 60, -90)
    ax.axis("off")
    ax.plot([0, 0], [0, H], color=INK, lw=1.0)
    ax.plot([-scale * 0.15, scale * 0.15], [0, 0], color=INK, lw=0.6)
    ax.plot([-scale * 0.15, scale * 0.15], [H, H], color=INK, lw=0.6)
    y = np.linspace(0, H, 100)
    s = top + (bot - top) * y / H
    ax.fill_betweenx(y, 0, s, where=s <= 0, color=COLORS[0], alpha=0.35, lw=0)
    ax.fill_betweenx(y, 0, s, where=s >= 0, color=COLORS[1], alpha=0.35, lw=0)
    ax.plot(s, y, color=INK, lw=1.0)
    for val, yy in ((top, 0), (bot, H)):
        if abs(val) < 1e-9:
            txt = "0"
        else:
            txt = f"{val:+.1f}".replace("-", "−")
        ha = "right" if val < 0 else "left"
        ax.text(val + (-1.2 if val < 0 else 1.2) if val != 0 else 1.2, yy + (-28 if yy == 0 else 40),
                txt, fontsize=8, ha=ha if val != 0 else "left", va="center")
    ax.text(0, -78, title, fontsize=7.8, ha="center", va="bottom")


def fig_prestress():
    fig = plt.figure(figsize=(6.8, 5.0))
    # ---- elevation
    ax = fig.add_axes([0.04, 0.66, 0.92, 0.32])
    ax.set_xlim(-0.8, 10.8)
    ax.set_ylim(-1.75, 0.85)
    ax.axis("off")
    L, h = 10.0, 0.6
    sc = 1.0                                # vertical exaggeration of depth (m → plot units)
    ax.add_patch(Rectangle((0, -h * sc), L, h * sc, fc="#E4E4E4", ec=INK, lw=1.0))
    xs = np.linspace(0, L, 100)
    e = 0.2 * (1 - ((xs - L / 2) / (L / 2)) ** 2)     # eccentricity below centroid
    ax.plot(xs, -h * sc / 2 - e * sc, color=COLORS[1], lw=1.8)
    ax.plot([0, L], [-h * sc / 2, -h * sc / 2], color="0.5", lw=0.7, ls="-.")
    ax.text(L + 0.1, -h / 2, "centroid", fontsize=7.5, va="center")
    ax.annotate("", xy=(L / 2, -h / 2 - 0.2), xytext=(L / 2, -h / 2),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, mutation_scale=6))
    ax.text(L / 2 + 0.1, -h / 2 - 0.07, "e = 200 mm", fontsize=7.5, va="center",
            bbox=dict(fc="#E4E4E4", ec="none", pad=0.2))
    ax.annotate("parabolic draped tendon, P = 1.25 MN", xy=(2.0, -0.44), xytext=(0.8, -0.95),
                fontsize=7.5, color=COLORS[1], arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[1]))
    # supports
    for xx, roller in ((0, False), (L, True)):
        ax.add_patch(Polygon([[xx, -h], [xx - 0.25, -h - 0.35], [xx + 0.25, -h - 0.35]],
                             closed=True, fc="white", ec=INK, lw=0.9))
        if roller:
            for dx in (-0.12, 0.12):
                ax.add_patch(Circle((xx + dx, -h - 0.43), 0.07, fc="white", ec=INK, lw=0.8))
    # load
    for xx in np.linspace(0, L, 21):
        ax.annotate("", xy=(xx, 0.02), xytext=(xx, 0.45),
                    arrowprops=dict(arrowstyle="-|>", lw=0.8, mutation_scale=6, color=COLORS[0]))
    ax.plot([0, L], [0.45, 0.45], color=COLORS[0], lw=0.8)
    ax.text(L / 2, 0.55, "w = 30 kN/m (service, incl. self-weight)", fontsize=8, ha="center",
            color=COLORS[0])
    ax.annotate("", xy=(0, -1.2), xytext=(L, -1.2),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, mutation_scale=7))
    ax.text(L / 2, -1.3, "L = 10 m;  section 300 × 600 mm;  M = 375 kN m;  Z = 0.018 m³",
            fontsize=8, ha="center", va="top")
    ax.plot([L / 2, L / 2], [0.0, -h], color="0.3", lw=0.8, ls="--")
    ax.text(L / 2 + 0.08, -0.72, "midspan", fontsize=7, color="0.3")

    # ---- stress blocks
    w, y0, hh = 0.135, 0.06, 0.50
    xs0 = [0.03, 0.215, 0.40, 0.585]
    specs = [(-20.8, 20.8, "(a) load M/Z"), (-6.9, -6.9, "(b) P/A"),
             (13.9, -13.9, "(c) Pe/Z"), (-13.9, 0.0, "(d) sum")]
    for x0, (tp, bt, tl) in zip(xs0, specs):
        a = fig.add_axes([x0, y0, w, hh])
        _stress_block(a, tp, bt, tl)
    for xop, sym in ((0.195, "+"), (0.38, "+"), (0.565, "=")):
        fig.text(xop + 0.005, y0 + hh * 0.45, sym, fontsize=14, ha="center", va="center")
    fig.text(0.03, y0 - 0.025, "stresses in MPa at midspan; tension +, compression − (drawn left)",
             fontsize=7.5, va="top")
    # ---- (e) cracked reinforced section
    e_ax = fig.add_axes([0.765, y0, 0.22, hh])
    e_ax.set_xlim(-1.4, 2.2)
    e_ax.set_ylim(6.6, -0.9)
    e_ax.set_aspect("equal")
    e_ax.axis("off")
    e_ax.add_patch(Rectangle((-0.75, 0), 1.5, 6.0, fc="#E4E4E4", ec=INK, lw=1.0))
    e_ax.add_patch(Rectangle((-0.75, 0), 1.5, 1.6, fc=COLORS[0], alpha=0.35, ec="none",
                             hatch="///"))
    e_ax.plot([-0.95, 0.95], [2.0, 2.0], color=INK, ls="--", lw=0.9)
    e_ax.text(0.98, 2.0, "N.A.", fontsize=7, va="center")
    for xc in (-0.3, 0.2):
        e_ax.plot([xc, xc + 0.08, xc - 0.05, xc + 0.04], [6.0, 4.6, 3.4, 2.3], color=INK, lw=0.9)
    for xb in (-0.45, 0, 0.45):
        e_ax.add_patch(Circle((xb, 5.3), 0.14, fc=INK))
    e_ax.annotate("", xy=(1.9, 0.75), xytext=(1.1, 0.75),
                  arrowprops=dict(arrowstyle="<|-", lw=1.2, color=COLORS[0], mutation_scale=9))
    e_ax.text(1.5, 0.45, "C", fontsize=9, ha="center", color=COLORS[0])
    e_ax.annotate("", xy=(1.9, 5.3), xytext=(1.1, 5.3),
                  arrowprops=dict(arrowstyle="-|>", lw=1.2, color=COLORS[1], mutation_scale=9))
    e_ax.text(1.5, 5.0, "T", fontsize=9, ha="center", color=COLORS[1])
    e_ax.text(0.0, 6.4, "cracks; steel\ncarries tension", fontsize=6.8, ha="center", va="top")
    e_ax.text(-1.3, -0.85, "(e) cracked RC section", fontsize=7.8, va="bottom")
    e_ax.text(0, 0.8, "compr.\nblock", fontsize=6.5, ha="center", va="center")
    save(fig, "18", "fig-18-4-prestress-stresses")


# ---------------------------------------------------------------- 18.5
def fig_wood():
    fig = plt.figure(figsize=(6.8, 5.2))
    # (a) log cross-section
    ax = fig.add_axes([0.0, 0.50, 0.48, 0.47])
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-1.35, 1.6)
    ax.set_ylim(-1.3, 1.3)
    ax.add_patch(Circle((0, 0), 1.0, fc="#6E4B2A", ec=INK, lw=0.8))          # bark
    ax.add_patch(Circle((0, 0), 0.92, fc="#E9D3A6", ec="#3C6E2E", lw=1.6))   # sapwood + cambium
    ax.add_patch(Circle((0, 0), 0.62, fc="#C99A5B", ec="none"))              # heartwood
    for r in np.linspace(0.08, 0.90, 11):
        ax.add_patch(Circle((0, 0), r, fc="none", ec="#8A6332", lw=0.7))
    ax.add_patch(Circle((0, 0), 0.04, fc="#4A3018", ec="none"))
    # cut wedge with axes
    ax.add_patch(Wedge((0, 0), 0.92, -25, 25, fc="none", ec=COLORS[0], lw=1.6))
    ax.annotate("", xy=(1.42, 0.0), xytext=(0.30, 0.0),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.3, mutation_scale=9))
    ax.text(1.45, 0.02, "R", fontsize=10, color=COLORS[0], va="center", fontweight="bold")
    ax.annotate("", xy=(0.70, 0.62), xytext=(0.70, 0.0),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.3, mutation_scale=9))
    ax.text(0.73, 0.62, "T", fontsize=10, color=COLORS[0], fontweight="bold")
    ax.add_patch(Circle((1.12, -0.55), 0.08, fc="white", ec=COLORS[0], lw=1.3))
    ax.add_patch(Circle((1.12, -0.55), 0.025, fc=COLORS[0], ec="none"))
    ax.text(1.24, -0.55, "L (along\ntrunk, out\nof page)", fontsize=7.2, color=COLORS[0],
            va="center")
    lab = [("pith", (0.0, 0.0), (-1.05, 1.08)), ("heartwood", (-0.4, 0.2), (-1.33, 0.70)),
           ("sapwood", (-0.75, -0.2), (-1.33, -0.45)), ("cambium", (-0.65, -0.65), (-1.30, -0.95)),
           ("bark", (-0.30, -0.95), (-0.35, -1.25)), ("annual ring", (0.0, 0.49), (0.6, 1.15))]
    for t, xy, xt in lab:
        ax.annotate(t, xy=xy, xytext=xt, fontsize=7.5, va="center",
                    arrowprops=dict(arrowstyle="-", lw=0.6))
    ax.text(-1.33, 1.28, "(a) trunk cross-section", fontsize=8.5, va="top")
    ax.text(1.58, -1.12, "$E_L:E_R:E_T$ ≈ 20 : 1.6 : 1\n(spruce 11 : 0.8 : 0.5 GPa)",
            fontsize=7.5, ha="right", va="center",
            bbox=dict(fc="white", ec=COLORS[0], lw=0.8, pad=2))

    # (b) softwood cube (oblique projection)
    bx = fig.add_axes([0.50, 0.50, 0.49, 0.47])
    bx.set_aspect("equal")
    bx.axis("off")
    bx.set_xlim(-0.3, 6.6)
    bx.set_ylim(-0.9, 5.85)
    W, Hc, D = 4.0, 3.2, 1.6          # front width (R), height (T), depth (L, oblique)
    ox, oy = 0.55, 0.45                # oblique unit vector for depth
    # front face cells: rows along T (y), columns along R (x) with earlywood → latewood
    xr = [0.0]
    widths = [0.42, 0.42, 0.41, 0.40, 0.38, 0.33, 0.26, 0.20, 0.16]   # earlywood → latewood
    walls = [0.03, 0.03, 0.03, 0.035, 0.04, 0.055, 0.07, 0.075, 0.075]
    i = 0
    while xr[-1] < W - 1e-6:
        wv = widths[i % len(widths)]
        xr.append(min(xr[-1] + wv, W))
        i += 1
    nrow = 8
    hrow = Hc / nrow
    bx.add_patch(Rectangle((0, 0), W, Hc, fc="#B88A4E", ec=INK, lw=1.0, zorder=1))
    ray_row = 5
    for j in range(len(xr) - 1):
        k = j % len(widths)
        wt = walls[k]
        for r in range(nrow):
            x0, x1 = xr[j], xr[j + 1]
            y0 = r * hrow
            if r == ray_row:
                # ray cells: elongated radially, small
                bx.add_patch(Rectangle((x0 + 0.02, y0 + 0.12), x1 - x0 - 0.04, hrow - 0.24,
                                       fc="#F5E8CC", ec="none", zorder=2))
                continue
            bx.add_patch(Rectangle((x0 + wt, y0 + wt), x1 - x0 - 2 * wt, hrow - 2 * wt,
                                   fc="#F5E8CC", ec="none", zorder=2))
    bx.plot([0, W], [ray_row * hrow, ray_row * hrow], color="#7A5530", lw=0.6, zorder=3)
    bx.plot([0, W], [(ray_row + 1) * hrow, (ray_row + 1) * hrow], color="#7A5530", lw=0.6, zorder=3)
    # top face (radial plane R–L)
    top = [[0, Hc], [W, Hc], [W + ox * D, Hc + oy * D], [ox * D, Hc + oy * D]]
    bx.add_patch(Polygon(top, closed=True, fc="#E7CFA0", ec=INK, lw=1.0, zorder=1))
    for xv in xr[1:-1]:
        bx.plot([xv, xv + ox * D], [Hc, Hc + oy * D], color="#8A6332", lw=0.6, zorder=2)
    # bordered pits on radial walls (top face)
    for xv in xr[1:6]:
        for s in (0.35, 0.75):
            bx.add_patch(Ellipse((xv + ox * D * s, Hc + oy * D * s), 0.16, 0.10, fc="white",
                                 ec="#5B3F20", lw=0.6, zorder=3))
            bx.add_patch(Ellipse((xv + ox * D * s, Hc + oy * D * s), 0.05, 0.035, fc="#5B3F20",
                                 ec="none", zorder=4))
    # right face (tangential plane T–L)
    rf = [[W, 0], [W + ox * D, oy * D], [W + ox * D, Hc + oy * D], [W, Hc]]
    bx.add_patch(Polygon(rf, closed=True, fc="#D8B985", ec=INK, lw=1.0, zorder=1))
    for r in range(1, nrow):
        bx.plot([W, W + ox * D], [r * hrow, r * hrow + oy * D], color="#8A6332", lw=0.6, zorder=2)
    # ray seen on the tangential face as a spindle
    cx, cy = W + ox * D * 0.5, ray_row * hrow + hrow / 2 + oy * D * 0.5
    bx.add_patch(Ellipse((cx, cy), 0.18, 0.55, angle=-50, fc="#F5E8CC", ec="#5B3F20", lw=0.7,
                         zorder=3))
    # labels
    bx.annotate("earlywood\n(thin walls)", xy=(0.4, 0.6), xytext=(0.0, -0.75), fontsize=7.2,
                arrowprops=dict(arrowstyle="-", lw=0.6))
    bx.annotate("latewood\n(thick walls)", xy=(3.45, 0.6), xytext=(2.3, -0.75), fontsize=7.2,
                arrowprops=dict(arrowstyle="-", lw=0.6))
    bx.annotate("ray (runs radially)", xy=(2.2, ray_row * hrow + hrow / 2), xytext=(4.4, -0.55),
                fontsize=7.2, arrowprops=dict(arrowstyle="-", lw=0.6))
    bx.annotate("bordered pits", xy=(xr[2] + ox * D * 0.75, Hc + oy * D * 0.75),
                xytext=(0.2, 4.95), fontsize=7.2, arrowprops=dict(arrowstyle="-", lw=0.6))
    bx.annotate("tracheid ≈ 30 μm", xy=(xr[1] + 0.2, 2.6), xytext=(4.95, 4.2), fontsize=7.2,
                arrowprops=dict(arrowstyle="-", lw=0.6))
    # axes
    bx.annotate("", xy=(5.75, 0.5), xytext=(5.0, 0.5),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.1, mutation_scale=8))
    bx.text(5.8, 0.5, "R", color=COLORS[0], fontsize=9, va="center", fontweight="bold")
    bx.annotate("", xy=(5.0, 1.25), xytext=(5.0, 0.5),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.1, mutation_scale=8))
    bx.text(5.0, 1.32, "T", color=COLORS[0], fontsize=9, ha="center", fontweight="bold")
    bx.annotate("", xy=(5.0 + 0.55, 0.5 + 0.45), xytext=(5.0, 0.5),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[0], lw=1.1, mutation_scale=8))
    bx.text(5.62, 1.0, "L", color=COLORS[0], fontsize=9, fontweight="bold")
    bx.text(-0.25, 5.85, "(b) softwood block, ≈ 1 mm", fontsize=8.5, va="top")

    # (c) cell-wall layers, stepped cut-away; lines show microfibril direction
    cx_ = fig.add_axes([0.02, 0.02, 0.50, 0.45])
    cx_.set_xlim(-0.6, 10)
    cx_.set_ylim(-0.4, 7.2)
    cx_.set_aspect("equal")
    cx_.axis("off")
    layers = [("middle lamella", 0.0, None, "#C9B48A", 1.0),
              ("primary wall (random)", 0.0, "rand", "#E3D3B0", 1.0),
              ("S1: 60–80° to axis", 70.0, None, "#EBDDBE", 1.0),
              ("S2: 5–30° (microfibril angle), thick", 15.0, None, "#F2E6CC", 2.2),
              ("S3: 60–90°", 75.0, None, "#EBDDBE", 0.9)]
    x = 0.4
    top_y = 6.6
    step = 0.85
    for k, (lab, ang, kind, col, wdt) in enumerate(layers):
        ybot = k * step
        rect = Rectangle((x, ybot), wdt, top_y - ybot, fc=col, ec=INK, lw=0.8)
        cx_.add_patch(rect)
        if kind == "rand":
            segs = []
            for _ in range(30):
                p = np.array([x + RNG.uniform(0, wdt), RNG.uniform(ybot, top_y)])
                a = RNG.uniform(0, np.pi)
                d = 0.35 * np.array([np.cos(a), np.sin(a)])
                segs.append([p - d, p + d])
            lc = LineCollection(segs, colors="#6B5B45", linewidths=0.6)
            cx_.add_collection(lc)
            lc.set_clip_path(rect)
        elif ang > 0:
            th = np.radians(ang)
            dvec = np.array([np.sin(th), np.cos(th)])          # angle from the cell axis
            nvec = np.array([dvec[1], -dvec[0]])
            spacing = 0.17 if ang < 30 else 0.24
            c0 = np.array([x + wdt / 2, (ybot + top_y) / 2])
            segs = [[c0 + s_ * nvec - 9 * dvec, c0 + s_ * nvec + 9 * dvec]
                    for s_ in np.arange(-9, 9, spacing)]
            lc = LineCollection(segs, colors="#6B5B45", linewidths=0.6)
            cx_.add_collection(lc)
            lc.set_clip_path(rect)
        cx_.text(x + wdt + 0.15, ybot + step / 2, lab, fontsize=6.9, va="center", ha="left")
        x += wdt
    cx_.add_patch(Rectangle((x, 4.6), 1.0, top_y - 4.6, fc="white", ec=INK, lw=0.8, ls="--"))
    cx_.text(x + 0.5, (4.6 + top_y) / 2, "lumen", fontsize=7, ha="center", rotation=90,
             va="center")
    cx_.annotate("", xy=(0.0, 6.4), xytext=(0.0, 3.4),
                 arrowprops=dict(arrowstyle="-|>", lw=1.0, color=COLORS[0], mutation_scale=8))
    cx_.text(-0.1, 3.3, "cell\naxis\n(L)", fontsize=6.8, color=COLORS[0], ha="center", va="top")
    cx_.text(-0.55, 7.2, "(c) tracheid wall layers (cut away; lines = microfibrils)",
             fontsize=8.5, va="top")

    # (d) microfibril cross-section
    dx = fig.add_axes([0.55, 0.03, 0.43, 0.43])
    dx.set_aspect("equal")
    dx.axis("off")
    dx.set_xlim(-0.5, 13)
    dx.set_ylim(-1.3, 13.2)
    dx.add_patch(Rectangle((0, 0), 12, 10, fc="#B78A55", ec=INK, lw=0.8))    # lignin matrix
    for _ in range(140):
        p = RNG.uniform([0.2, 0.2], [11.8, 9.8])
        dx.add_patch(Circle(p, RNG.uniform(0.05, 0.12), fc="#8F6638", ec="none"))
    centres = [(3, 3), (3, 7.2), (7.4, 2.6), (7.6, 7.0)]
    for (cxm, cym) in centres:
        dx.add_patch(Circle((cxm, cym), 2.15, fc="#D9C29A", ec="none"))     # hemicellulose
        th = np.linspace(0, 2 * np.pi, 120)
        rr = 2.15 + 0.12 * np.sin(9 * th)
        dx.plot(cxm + rr * np.cos(th), cym + rr * np.sin(th), color="#9C7B47", lw=0.8)
        s = 1.5
        dx.add_patch(Rectangle((cxm - s, cym - s), 2 * s, 2 * s, fc="#F7F1E3", ec=INK, lw=0.8))
        for gx in np.linspace(cxm - s + 0.3, cxm + s - 0.3, 6):
            for gy in np.linspace(cym - s + 0.3, cym + s - 0.3, 6):
                dx.add_patch(Circle((gx, gy), 0.11, fc="#5A4A30", ec="none"))
    dx.annotate("", xy=(1.5, -0.5), xytext=(4.5, -0.5),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, mutation_scale=6))
    dx.text(3.0, -0.65, "≈ 3 nm", fontsize=7.5, ha="center", va="top")
    dx.annotate("crystalline cellulose\n(chains end-on)", xy=(7.6, 7.6), xytext=(8.0, 10.6),
                fontsize=7, ha="center", va="bottom", arrowprops=dict(arrowstyle="-", lw=0.6))
    dx.annotate("hemicellulose", xy=(9.6, 3.4), xytext=(12.9, -0.4), fontsize=7, ha="right",
                va="top", arrowprops=dict(arrowstyle="-", lw=0.6))
    dx.annotate("lignin", xy=(5.3, 5.0), xytext=(1.0, 10.6), fontsize=7, va="bottom",
                arrowprops=dict(arrowstyle="-", lw=0.6))
    dx.text(-0.4, 13.2, "(d) microfibrils in matrix (cross-section)", fontsize=8.5, va="top")
    save(fig, "18", "fig-18-5-wood-hierarchy")


# ---------------------------------------------------------------- 18.6
def fig_binder_carbon():
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.8, 4.2), gridspec_kw=dict(width_ratios=[1, 1.15]))
    fig.subplots_adjust(wspace=0.95, left=0.22)
    binders = [("CEM I (95 % clinker)", 0.95, 0.83), ("CEM II/A-LL (85 %)", 0.85, 0.74),
               ("LC3-50", 0.50, 0.51), ("CEM III/A (50 % GGBS)", 0.50, 0.47),
               ("CEM III/B (75 % GGBS)", 0.25, 0.27)]
    y = np.arange(len(binders) + 1)[::-1]
    for yy, (lab, cf, tot) in zip(y, binders):
        proc = 0.51 * cf
        ax.barh(yy, proc, color=COLORS[1], height=0.6)
        ax.barh(yy, tot - proc, left=proc, color=COLORS[5], height=0.6)
        ax.text(tot + 0.02, yy, f"{tot:.2f}", va="center", fontsize=7.8)
    ax.barh(y[-1], 0.20, left=0.15, color="0.6", height=0.6, hatch="//", ec="white")
    ax.text(0.37, y[-1], "0.15–0.35", va="center", fontsize=7.8)
    ax.set_yticks(y)
    ax.set_yticklabels([b[0] for b in binders] + ["alkali-activated slag"], fontsize=7.8)
    ax.set_xlim(0, 1.0)
    ax.set_xlabel("t CO₂ per t binder")
    ax.set_title("(a) binders", fontsize=9, loc="left")
    from matplotlib.patches import Patch
    ax.legend([Patch(color=COLORS[1]), Patch(color=COLORS[5]), Patch(fc="0.6", hatch="//", ec="white")],
              ["process (calcination)", "fuel + electricity (+ SCM)", "range (activator-dependent)"],
              fontsize=7, loc="upper center", bbox_to_anchor=(0.35, -0.16), ncol=1)
    mats = [("aggregate", 0.004, 0.006, "0.6"),
            ("asphalt mix", 0.05, 0.08, "0.6"),
            ("concrete, 50 % GGBS", 0.08, 0.10, COLORS[2]),
            ("concrete C30, CEM I", 0.13, 0.16, COLORS[2]),
            ("fired brick", 0.20, 0.25, COLORS[1]),
            ("glulam / CLT (fossil only)", 0.30, 0.50, COLORS[4]),
            ("rebar, EAF", 0.5, 1.0, COLORS[0]),
            ("rebar, BOF", 1.8, 2.2, COLORS[0]),
            ("steel sections, EAF", 0.6, 1.2, COLORS[0]),
            ("steel sections, BOF", 1.8, 2.5, COLORS[0]),
            ("float glass", 1.0, 1.4, COLORS[5]),
            ("aluminium, recycled", 0.5, 1.0, COLORS[3]),
            ("aluminium, primary", 8.0, 16.0, COLORS[3])]
    yb = np.arange(len(mats))[::-1]
    for yy, (lab, lo, hi, c) in zip(yb, mats):
        bx.barh(yy, hi - lo, left=lo, color=c, height=0.62)
        txt = f"{lo:g}–{hi:g}" if lab != "aggregate" else "≈ 0.005"
        bx.text(hi * 1.12, yy, txt, va="center", fontsize=7)
    bx.set_xscale("log")
    bx.set_xlim(0.003, 30)
    bx.set_yticks(yb)
    bx.set_yticklabels([m[0] for m in mats], fontsize=7.8)
    bx.set_xlabel("kg CO₂e per kg (cradle to gate)")
    bx.set_title("(b) construction materials", fontsize=9, loc="left")
    save(fig, "18", "fig-18-6-binder-carbon")


if __name__ == "__main__":
    fig_hydration()
    fig_strength_wc()
    fig_chloride()
    fig_prestress()
    fig_wood()
    fig_binder_carbon()
