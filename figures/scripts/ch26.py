"""Figures for Chapter 26 — Dielectric and Insulating Materials.

Run from the repository root:  python figures/scripts/ch26.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch, Ellipse

kB = 8.617333e-5  # eV/K


# ---------------------------------------------------------------- Figure 26.1
def _arrow(ax, x0, y0, x1, y1, color=INK, lw=1.2, ms=9):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=ms,
                                shrinkA=0, shrinkB=0))


def _water(ax, x, y, ang, s=0.32):
    """Bent H2O molecule; dipole points along angle ang (from H side to O... drawn as p)."""
    ux, uy = np.cos(ang), np.sin(ang)
    # O at front (negative end), H atoms behind at +-52 deg
    ox, oy = x - 0.15 * ux, y - 0.15 * uy
    for d in (+0.91, -0.91):
        hx = ox + s * np.cos(ang + np.pi + d) * -1
        hy = oy + s * np.sin(ang + np.pi + d) * -1
    hs = []
    for d in (+0.91, -0.91):
        a = ang + d
        hs.append((ox + s * np.cos(a), oy + s * np.sin(a)))
    for hx, hy in hs:
        ax.plot([ox, hx], [oy, hy], color=INK, lw=1)
        ax.add_patch(Circle((hx, hy), 0.09, fc="white", ec=INK, lw=0.8, zorder=3))
    ax.add_patch(Circle((ox, oy), 0.15, fc="#E06666", ec=INK, lw=0.8, zorder=3))
    _arrow(ax, ox - 0.05 * ux, oy - 0.05 * uy, ox + 0.62 * ux, oy + 0.62 * uy, color=COLORS[0], lw=1.0, ms=7)


def polarization_mechanisms():
    fig, ax = schematic(6.8, 4.4, xlim=(0, 16.4), ylim=(-0.6, 10))
    titles = ["(a) Electronic", "(b) Ionic", "(c) Orientational", "(d) Interfacial\n(space charge)"]
    freqs = [r"up to $\sim10^{15}$ Hz", r"up to $\sim10^{13}$ Hz",
             r"$10^{3}$–$10^{11}$ Hz" + "\n(material dependent)", r"below $\sim10^{3}$ Hz"]
    rng = np.random.default_rng(4)
    for k in range(4):
        x0 = 0.4 + 4.0 * k
        cx = x0 + 1.8
        ax.text(cx, 9.75, titles[k], ha="center", va="top", fontsize=9.5, weight="bold")
        for row, yc in ((0, 6.6), (1, 2.6)):
            ax.add_patch(FancyBboxPatch((x0, yc - 1.7), 3.6, 3.4,
                                        boxstyle="round,pad=0.02,rounding_size=0.15",
                                        fc="#FAFAFA", ec="#AAAAAA", lw=0.8))
            on = row == 1
            if k == 0:
                sh = -0.32 if on else 0.0
                ax.add_patch(Circle((cx + sh, yc), 1.0, fc="#BFD7EE", ec=COLORS[0], lw=0.8, alpha=0.9))
                ax.add_patch(Circle((cx, yc), 0.12, fc=COLORS[1], ec=INK, lw=0.6, zorder=4))
                ax.text(cx + 0.18, yc + 0.18, "+", fontsize=8, color=COLORS[1])
                if on:
                    _arrow(ax, cx - 0.32, yc - 1.25, cx + 0.05, yc - 1.25, color=COLORS[0], ms=7)
                    ax.text(cx + 0.2, yc - 1.25, "$p$", va="center", fontsize=9, color=COLORS[0])
            elif k == 1:
                xs = cx + np.array([-1.32, -0.44, 0.44, 1.32])
                for i, xx in enumerate(xs):
                    cat = i % 2 == 0
                    d = (0.14 if cat else -0.14) if on else 0.0
                    r = 0.2 if cat else 0.3
                    ax.add_patch(Circle((xx + d, yc), r, fc="#F2C38F" if cat else "#9DC9A5",
                                        ec=INK, lw=0.7, zorder=3))
                    ax.text(xx + d, yc - 0.02, "+" if cat else "−", ha="center", va="center",
                            fontsize=9, zorder=4)
                ax.plot([xs[0] - 0.4, xs[-1] + 0.4], [yc, yc], color="#888888", lw=0.8, zorder=1)
                if on:
                    ax.text(cx, yc - 0.75, "unequal bond lengths", ha="center", fontsize=7.5)
                    ax.text(cx, yc + 0.6, "cations →   ← anions", ha="center", fontsize=7.5)
                else:
                    ax.text(cx, yc - 0.75, "Na$^+$ (small), Cl$^-$ (large)", ha="center", fontsize=7.5)
            elif k == 2:
                pos = [(-1.0, 0.75), (0.6, 0.85), (-0.3, -0.05), (1.05, -0.2), (-1.05, -0.9), (0.35, -1.0)]
                rand = rng.uniform(0, 2 * np.pi, len(pos))
                for (dx, dy), a in zip(pos, rand):
                    ang = (0.45 * np.sin(a)) if on else a
                    _water(ax, cx + dx - 0.15, yc + dy, ang)
            else:
                # two grains separated by a boundary; mobile charges
                ax.add_patch(Rectangle((cx - 0.12, yc - 1.55), 0.24, 3.1, fc="#888888", ec="none"))
                for gx in (cx - 0.95, cx + 0.95):
                    if not on:
                        q = 0
                        for iy, py in enumerate(np.linspace(yc - 1.1, yc + 1.1, 4)):
                            for px in (gx - 0.4, gx + 0.4):
                                plus = (q + iy) % 2 == 0
                                q += 1
                                ax.text(px + rng.uniform(-0.12, 0.12), py + rng.uniform(-0.1, 0.1),
                                        "+" if plus else "−", ha="center", va="center",
                                        fontsize=10 if plus else 11, color=COLORS[1] if plus else COLORS[0])
                    else:
                        for yy in np.linspace(yc - 1.1, yc + 1.1, 4):
                            ax.text(gx + 0.62, yy, "+", ha="center", va="center", fontsize=10, color=COLORS[1])
                            ax.text(gx - 0.62, yy, "−", ha="center", va="center", fontsize=11, color=COLORS[0])
                if not on:
                    ax.text(cx, yc + 1.85, "grain | boundary | grain", ha="center", va="bottom", fontsize=7)
        # field arrow and frequency
        _arrow(ax, x0 + 0.6, 0.55, x0 + 3.0, 0.55, color=INK, lw=1.4)
        ax.text(x0 + 3.1, 0.55, "$E$", va="center", fontsize=9)
        ax.text(cx, 0.15, freqs[k], ha="center", va="top", fontsize=8, color=COLORS[2])
    ax.text(0.15, 6.6, "$E=0$", rotation=90, ha="center", va="center", fontsize=9)
    ax.text(0.15, 2.6, "$E$ applied", rotation=90, ha="center", va="center", fontsize=9)
    save(fig, "26", "fig-26-1-polarization-mechanisms")


# ---------------------------------------------------------------- Figure 26.2
def dielectric_spectrum():
    f = np.logspace(-2, 16, 6000)
    w = 2 * np.pi * f

    def lorentz(d, f0, g):
        return d * f0**2 / (f0**2 - f**2 - 1j * f * g)

    def cole(d, fp, al):
        tau = 1 / (2 * np.pi * fp)
        return d / (1 + (-1j * w * tau) ** (1 - al))

    eps = (1 + lorentz(1.25, 1.2e15, 0.45e15) + lorentz(3.0, 1.0e13, 0.45e13)
           + cole(5.0, 1e8, 0.15) + cole(5.0, 3.0, 0.25))
    e1, e2 = eps.real, eps.imag
    fig = plt.figure(figsize=(6.6, 5.4))
    axb = fig.add_axes([0.11, 0.88, 0.86, 0.07])
    ax1 = fig.add_axes([0.11, 0.50, 0.86, 0.36])
    ax2 = fig.add_axes([0.11, 0.09, 0.86, 0.36], sharex=ax1)
    for a in (ax1, ax2, axb):
        a.set_xscale("log")
        a.set_xlim(1e-2, 1e16)
    ax1.plot(f, e1, color=COLORS[0])
    ax1.set_ylim(-3, 17.5)
    ax1.axhline(0, color="grey", lw=0.5)
    ax1.set_ylabel(r"$\varepsilon'$", fontsize=13)
    ax2.plot(f, e2, color=COLORS[1])
    ax2.set_yscale("log")
    ax2.set_ylim(1e-2, 50)
    ax2.set_ylabel(r"$\varepsilon''$", fontsize=13)
    ax2.set_xlabel("Frequency, $f$ (Hz)")
    ax2.set_xticks([10.0 ** k for k in range(-2, 17, 2)])
    plt.setp(ax1.get_xticklabels(), visible=False)
    # step labels
    labs = [(0.4, 11.0, "interfacial"), (1.5e7, 6.0, "orientational"),
            (1e13, 7.8, "ionic\n(resonance)"), (1.2e15, 5.0, "electronic\n(resonance)")]
    for x, y, t in labs:
        ax1.text(x, y, t, ha="center", va="bottom", fontsize=8.5)
    ax1.annotate(r"$n^2=\varepsilon_\infty\approx2.25$" + "\n(visible)", xy=(5.5e14, 2.4),
                 xytext=(1e10, 2.0), fontsize=8.5, va="center",
                 arrowprops=dict(arrowstyle="-", color=INK, lw=0.7))
    ax2.text(3.0, 4.0, "relaxation", ha="center", fontsize=8.5)
    ax2.text(1e8, 4.0, "relaxation", ha="center", fontsize=8.5)
    ax2.text(1e13, 13 * 1.6, "resonance", ha="center", fontsize=8.5)
    ax2.text(1.2e15, 7.0 * 1.6, "resonance", ha="center", fontsize=8.5)
    # bands strip
    axb.set_ylim(0, 1)
    axb.axis("off")
    bands = [(20, 2e4, "audio", "#EFE3C8"), (2e4, 1e9, "RF", "#DCE9D5"),
             (1e9, 1e11, "μwave", "#D5E3F0"), (3e11, 4e14, "infrared", "#F2D7D5"),
             (4e14, 7.9e14, "", "#C9E6C1"), (7.9e14, 1e16, "UV", "#E2D5EF")]
    for lo, hi, t, c in bands:
        axb.axvspan(lo, hi, 0.05, 0.95, color=c)
        if t:
            axb.text(np.sqrt(lo * hi), 0.5, t, ha="center", va="center", fontsize=8)
    axb.text(np.sqrt(4e14 * 7.9e14), 1.15, "visible", ha="center", va="bottom", fontsize=8)
    axb.plot([5.5e14, 5.5e14], [0.95, 1.12], color=INK, lw=0.6)
    axb.axvline(55, 0.05, 0.95, color=INK, lw=1.5)
    axb.text(55, 1.15, "power 50/60 Hz", ha="center", va="bottom", fontsize=8)
    for a in (ax1, ax2):
        a.axvline(55, color="grey", lw=0.6, ls=":")
    save(fig, "26", "fig-26-2-dielectric-spectrum")


# ---------------------------------------------------------------- Figure 26.3
def debye():
    es, ei = 80.0, 5.0
    d = es - ei
    x = np.linspace(-3, 3, 600)
    wt = 10.0**x
    deb = ei + d / (1 + 1j * wt)
    al = 0.35
    cc = ei + d / (1 + (1j * wt) ** (1 - al))
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.8, 3.6), gridspec_kw=dict(width_ratios=[1.1, 1]))
    ax1.plot(x, deb.real, color=COLORS[0], label=r"$\varepsilon'$ (Debye)")
    ax1.plot(x, -deb.imag, color=COLORS[1], label=r"$\varepsilon''$ (Debye)")
    ax1.plot(x, -cc.imag, color=COLORS[1], ls="--", lw=1.4,
             label=r"$\varepsilon''$, distribution of" + "\nrelaxation times (polymer)")
    ax1.axhline(es, color="grey", lw=0.6, ls=":")
    ax1.axhline(ei, color="grey", lw=0.6, ls=":")
    ax1.text(-2.9, es + 1.5, r"$\varepsilon_s=80$", ha="left", va="bottom", fontsize=8.5, color="grey")
    ax1.text(-2.9, ei + 1.5, r"$\varepsilon_\infty=5$", ha="left", va="bottom", fontsize=8.5, color="grey")
    ax1.plot(0, d / 2, "o", color=COLORS[1], ms=4)
    ax1.annotate(r"peak $\Delta\varepsilon/2=37.5$" + "\nat $\\omega\\tau=1$" + "\n(water: 19 GHz)",
                 xy=(0, d / 2), xytext=(0.55, 47), fontsize=8,
                 arrowprops=dict(arrowstyle="-", lw=0.7))
    xo = np.log10(2.45 / 19.2)
    ax1.axvline(xo, color=COLORS[2], lw=1, ls="-.")
    ax1.text(xo - 0.08, 22, "microwave\noven\n2.45 GHz", color=COLORS[2], fontsize=8, ha="right")
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(0, 90)
    ax1.set_xlabel(r"$\log_{10}(\omega\tau)$")
    ax1.set_ylabel(r"$\varepsilon'$, $\varepsilon''$")
    ax1.legend(loc="upper right", fontsize=7.5, bbox_to_anchor=(1.03, 0.97), handlelength=1.6)
    # Cole-Cole
    xx = np.linspace(-6, 6, 1500)
    w2 = 10.0**xx
    deb2 = ei + d / (1 + 1j * w2)
    cc2 = ei + d / (1 + (1j * w2) ** (1 - al))
    ax2.plot(deb2.real, -deb2.imag, color=COLORS[1], label="Debye semicircle")
    ax2.plot(cc2.real, -cc2.imag, color=COLORS[1], ls="--", lw=1.4, label="depressed arc\n(distributed)")
    ax2.plot([ei, es], [0, 0], color=INK, lw=0.6)
    ax2.plot([(es + ei) / 2], [d / 2], "o", color=COLORS[1], ms=4)
    po = ei + d / (1 + 1j * (2.45 / 19.2))
    ax2.plot(po.real, -po.imag, "s", color=COLORS[2], ms=5)
    ax2.annotate("2.45 GHz", xy=(po.real, -po.imag), xytext=(po.real - 6, -po.imag + 8),
                 fontsize=8, color=COLORS[2], ha="center")
    ax2.annotate("", xy=(20, 30.5), xytext=(60, 37.5),
                 arrowprops=dict(arrowstyle="-|>", color=INK, lw=1, connectionstyle="arc3,rad=0.25",
                                 mutation_scale=9))
    ax2.text(38, 42.5, r"increasing $\omega$", fontsize=8.5, ha="center")
    ax2.text(ei, -2.5, r"$\varepsilon_\infty$", ha="center", va="top", fontsize=9)
    ax2.text(es, -2.5, r"$\varepsilon_s$", ha="center", va="top", fontsize=9)
    ax2.set_xlim(0, 88)
    ax2.set_ylim(-8, 50)
    ax2.set_aspect("equal")
    ax2.set_xlabel(r"$\varepsilon'$")
    ax2.set_ylabel(r"$\varepsilon''$")
    ax2.legend(loc="upper right", fontsize=7.5, bbox_to_anchor=(1.05, 1.18))
    fig.tight_layout()
    save(fig, "26", "fig-26-3-debye-cole-cole")


# ---------------------------------------------------------------- Figure 26.4
def _paschen(x, A, B, K):
    den = np.log(A * x) - K
    v = np.where(den > 0.02, B * x / np.where(den > 0.02, den, 1), np.nan)
    return np.where(v < 2e6, v, np.nan)


def paschen():
    gases = [("SF$_6$", 14.4, 975.0, 1.0, COLORS[3]),
             ("air", 15.0, 365.0, 1.53, COLORS[0]),
             ("N$_2$", 10.0, 310.0, 1.2, COLORS[2]),
             ("He", 3.0, 34.0, 1.48, COLORS[4])]
    x = np.logspace(-1, 3, 4000)
    fig, ax = new_fig(6.4, 4.4)
    ax.set_xscale("log")
    ax.set_yscale("log")
    air = gases[1]
    pdmin = np.e * np.exp(air[3]) / air[1]
    ax.axvspan(0.1, pdmin, color="#EEEEEE")
    ax.text(0.105, 4e5, "left branch:\nvacuum and\nlow-pressure\ninsulation", fontsize=8, va="top")
    for name, A, B, K, c in gases:
        v = _paschen(x, A, B, K)
        ax.plot(x, v, color=c, lw=2.0 if name == "air" else 1.5, ls="--" if name == "N$_2$" else "-")
        i = np.nanargmin(v)
        print(name, "min", round(np.nanmin(v)), "at", round(x[i], 2), "V(760)", round(float(_paschen(760., A, B, K))))
    # direct labels
    ax.text(30, 1.0e5 * 0.95, "SF$_6$", color=COLORS[3], fontsize=9.5)
    ax.text(300, 5.5e4, "air", color=COLORS[0], fontsize=9.5)
    ax.text(330, 9.0e3, "N$_2$", color=COLORS[2], fontsize=9.5)
    ax.text(300, 1.6e3, "He", color=COLORS[4], fontsize=9.5)
    ax.annotate("air minimum\n≈ 330 V (meas.)", xy=(pdmin, 305), xytext=(0.115, 125), fontsize=8,
                arrowprops=dict(arrowstyle="-", lw=0.7))
    A, B, K = air[1], air[2], air[3]
    pts = [(76.0, "1 mm, 1 atm\n5.0 kV (meas. 4.5)", (6, 1.4e4), "o"),
           (760.0, "1 cm, 1 atm\n35 kV (meas. 31)", (55, 2.4e5), "o"),
           (40.7, "1 mm, 5000 m\n3.0 kV", (120, 1.7e2), "^"),
           (407.0, "1 cm, 5000 m\n21 kV", (120, 4.3e2), "^"),
           (7.6, "0.1 mm void,\n1 atm: 0.9 kV", (0.9, 3.0e3), "s")]
    for pd, lab, xyt, m in pts:
        v = float(_paschen(pd, A, B, K))
        ax.plot(pd, v, m, color=COLORS[1], ms=5.5, zorder=4)
        ax.annotate(lab, xy=(pd, v), xytext=xyt, fontsize=7.5,
                    arrowprops=dict(arrowstyle="-", lw=0.6, color="#555555"))
    ax.set_xlim(0.1, 1000)
    ax.set_ylim(100, 1e6)
    ax.set_xlabel(r"$pd$ (Torr cm)")
    ax.set_ylabel("Breakdown voltage, $V_b$ (V)")
    sec = ax.secondary_xaxis("top", functions=(lambda t: t * 1.3332, lambda t: t / 1.3332))
    sec.set_xlabel(r"$pd$ (Pa m)", fontsize=9)
    ax.spines["top"].set_visible(True)
    save(fig, "26", "fig-26-4-paschen-curve")


# ---------------------------------------------------------------- Figure 26.5
def _tree(ax, x, y, ang, length, depth, rng, color, lw):
    if depth == 0 or length < 0.04:
        return
    n = 4
    pts = [(x, y)]
    a = ang
    for _ in range(n):
        a += rng.normal(0, 0.25)
        x, y = x + length / n * np.cos(a), y + length / n * np.sin(a)
        pts.append((x, y))
    p = np.array(pts)
    ax.plot(p[:, 0], p[:, 1], color=color, lw=lw, solid_capstyle="round")
    nb = 2 if rng.random() < 0.75 else 3
    for _ in range(nb):
        _tree(ax, x, y, a + rng.uniform(-0.8, 0.8), length * rng.uniform(0.6, 0.8), depth - 1, rng,
              color, max(lw * 0.75, 0.4))


def breakdown_mechanisms():
    fig = plt.figure(figsize=(6.8, 5.6))
    ax = fig.add_axes([0.11, 0.47, 0.86, 0.45])
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1e-8, 1e9)
    ax.set_ylim(1, 1000)
    regions = [(1e-8, 1e-6, 500, 1000, "intrinsic /\nelectronic", COLORS[3]),
               (1e-5, 1e-1, 100, 450, "electro-\nmechanical", COLORS[5]),
               (1.0, 3e4, 20, 300, "thermal\n(depends on\ncooling)", COLORS[1]),
               (3.6e3, 1e9, 5, 50, "partial-discharge erosion,\nelectrical treeing", COLORS[0]),
               (3e7, 1e9, 1, 5, "water\ntreeing", COLORS[2])]
    for t0, t1, e0, e1, lab, c in regions:
        ax.add_patch(Rectangle((t0, e0), t1 - t0, e1 - e0, fc=c, alpha=0.28, ec=c, lw=1.2))
        if lab.startswith("intrinsic"):
            ax.text(1e-7, 450, lab, ha="center", va="top", fontsize=8.5)
        else:
            ax.text(np.sqrt(t0 * t1), np.sqrt(e0 * e1), lab, ha="center", va="center", fontsize=8.5)
    ax.set_xlabel("Time to breakdown (s)")
    ax.set_ylabel("Breakdown field (kV/mm)")
    ax.set_xticks([10.0 ** k for k in range(-8, 10, 2)])
    top = ax.twiny()
    top.set_xscale("log")
    top.set_xlim(ax.get_xlim())
    top.set_xticks([1e-6, 1, 3600, 86400, 3.156e7, 9.5e8])
    top.set_xticklabels(["1 μs", "1 s", "1 h", "1 d", "1 yr", "30 yr"], fontsize=8.5)
    top.minorticks_off()
    top.spines["top"].set_visible(True)
    # lower panel sketches
    rng = np.random.default_rng(11)
    for k in range(2):
        a = fig.add_axes([0.06 + 0.48 * k, 0.0, 0.42, 0.36])
        a.set_xlim(0, 4)
        a.set_ylim(-0.35, 3.2)
        a.set_aspect("equal")
        a.axis("off")
        a.add_patch(Rectangle((0, 0.25), 4, 2.4, fc="#F3EEDC", ec=INK, lw=0.8))
        if k == 0:
            a.add_patch(Rectangle((0, 0), 4, 0.25, fc="#999999", ec=INK, lw=0.8))
            a.text(2, 0.12, "plane electrode", ha="center", va="center", fontsize=7.5, color="white")
            a.add_patch(Polygon([(1.88, 3.1), (2.12, 3.1), (2.12, 2.55), (2.0, 1.95), (1.88, 2.55)],
                                fc="#777777", ec=INK, lw=0.8, zorder=4))
            a.text(2.2, 2.9, "needle", fontsize=7.5)
            for ang in np.linspace(-np.pi / 2 - 0.9, -np.pi / 2 + 0.9, 5):
                _tree(a, 2.0, 1.97, ang, 0.32, 4, rng, "#3A2A1A", 1.3)
            a.text(2.0, -0.12, "electrical tree: branched hollow channels", ha="center", va="top", fontsize=8)
        else:
            a.add_patch(Rectangle((0, 2.4), 4, 0.25, fc="#333333", ec=INK, lw=0.8))
            a.text(0.05, 2.85, "conductor screen (semicon)", ha="left", va="center", fontsize=7.5)
            a.add_patch(Rectangle((0, 0.0), 4, 0.25, fc="#333333", ec=INK, lw=0.8))
            a.text(2, 0.12, "insulation screen", ha="center", va="center", fontsize=7.5, color="white")
            a.add_patch(Polygon([(1.85, 2.4), (2.15, 2.4), (2.05, 2.22), (1.95, 2.2)], fc="#8B4513",
                                ec=INK, lw=0.6, zorder=4))
            n = 900
            r = 1.25 * np.sqrt(rng.uniform(0, 1, n)) ** 1.2
            th = rng.uniform(np.pi * 1.08, np.pi * 1.92, n)
            px, py = 2.0 + 1.05 * r * np.cos(th), 2.25 + r * np.sin(th) * 1.15
            m = py > 0.35
            a.scatter(px[m], py[m], s=2.5, color=COLORS[0], alpha=0.55, lw=0)
            a.annotate("contaminant", xy=(2.08, 2.3), xytext=(2.85, 2.85), fontsize=7.5, va="center",
                       arrowprops=dict(arrowstyle="-", lw=0.6))
            a.text(2.0, -0.12, "vented water tree: diffuse bush of water-filled voids",
                   ha="center", va="top", fontsize=8)
        a.text(0.05, 1.45, "insulation", fontsize=7.5, rotation=90, va="center", color="#666666")
    save(fig, "26", "fig-26-5-solid-breakdown-mechanisms")


# ---------------------------------------------------------------- Figure 26.6
def arrhenius_aging():
    fig, ax = new_fig(6.4, 4.2)
    inv = np.linspace(2.0, 2.9, 200)          # 1000/T in 1/kK
    T = 1000 / inv
    systems = [("class B (130 °C)", 130, 0.90, COLORS[0]),
               ("class F (155 °C)", 155, 1.00, COLORS[2]),
               ("class H (180 °C)", 180, 1.10, COLORS[1])]
    for lab, Tc, Ea, c in systems:
        T0 = Tc + 273.15
        life = 2e4 * np.exp(Ea / kB * (1 / T - 1 / T0))
        if Tc == 180:
            m = inv <= 2.16
            ax.plot(inv[m], life[m], color=c, label=f"{lab}, $E_a$ = {Ea:.2f} eV")
            ax.plot(inv[~m], life[~m], color=c, ls="--")
        else:
            ax.plot(inv, life, color=c, label=f"{lab}, $E_a$ = {Ea:.2f} eV")
        ax.plot(1000 / T0, 2e4, "o", color=c, ms=5, mfc="white", zorder=4)
    # accelerated test points on class H
    Ea, T0 = 1.10, 453.15
    tests = np.array([195, 210, 225]) + 273.15
    lt = 2e4 * np.exp(Ea / kB * (1 / tests - 1 / T0)) * np.array([1.12, 0.9, 1.08])
    ax.plot(1000 / tests, lt, "D", color=COLORS[1], ms=5.5, zorder=5, label="accelerated ageing tests (class H)")
    ax.axhline(2e4, color="grey", ls="--", lw=1)
    ax.text(2.895, 1.6e4, "20 000 h: reference life\nfor thermal index", fontsize=8.5, color="grey",
            ha="right", va="top")
    ax.text(2.235, 9e3, "extrapolated\nfrom tests", fontsize=8, color=COLORS[1], va="center")

    # 10 K halving rule: local slope triangle on class B near 120-130 C
    Ea, T0 = 0.90, 403.15
    Ta, Tb = 393.15, 403.15
    la = 2e4 * np.exp(Ea / kB * (1 / Ta - 1 / T0))
    lb = 2e4
    xa, xb = 1000 / Ta, 1000 / Tb
    ax.plot([xb, xa], [lb, lb], color=INK, lw=0.8)
    ax.plot([xa, xa], [lb, la], color=INK, lw=0.8)
    ax.annotate("10 K hotter → life ≈ halved\n(local slope, Montsinger rule)", xy=(xa, np.sqrt(la * lb)),
                xytext=(2.6, 1.2e5), fontsize=8, ha="center",
                arrowprops=dict(arrowstyle="-", lw=0.7))
    ax.set_yscale("log")
    ax.set_xlim(2.0, 2.9)
    ax.set_ylim(100, 1e6)
    ax.set_xlabel(r"$1000/T$ (K$^{-1}$)")
    ax.set_ylabel("Life (h)")
    ax.legend(loc="lower right", fontsize=8)
    top = ax.secondary_xaxis("top", functions=(lambda v: 1000 / np.maximum(v, 1e-3) - 273.15,
                                                 lambda c: 1000 / (np.asarray(c) + 273.15)))
    top.set_xticks([80, 100, 120, 140, 160, 180, 200, 220])
    top.set_xlabel("Temperature (°C)", fontsize=9)
    ax.spines["top"].set_visible(True)
    save(fig, "26", "fig-26-6-arrhenius-aging")


if __name__ == "__main__":
    polarization_mechanisms()
    dielectric_spectrum()
    debye()
    paschen()
    breakdown_mechanisms()
    arrhenius_aging()
