"""Figures for Chapter 53 — Large-Facility and Nanoscale Characterization. Run from the repository root: python figures/scripts/ch53.py"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle, Polygon, Ellipse, FancyBboxPatch, Circle, Wedge  # noqa: E402
from scipy.special import kv  # noqa: E402
from scipy.integrate import quad  # noqa: E402

BLUE, VERM, GREEN, PINK, ORANGE, SKY = COLORS[:6]


# ---------------------------------------------------------------- Figure 53.1
def _G1(y):
    """Synchrotron universal function y * int_y^inf K_5/3."""
    out = []
    for yy in np.atleast_1d(y):
        val, _ = quad(lambda t: kv(5 / 3, t), yy, max(60, 40 * yy), limit=200)
        out.append(yy * val)
    return np.array(out)


def source_brilliance():
    fig, ax = new_fig(6.8, 4.6)
    E = np.logspace(-1, np.log10(200), 500)

    # laboratory sources: bremsstrahlung band and characteristic lines
    Eb = E[(E > 2) & (E < 60)]
    ax.fill_between(Eb, 1e7, 1e8, color="0.6", alpha=0.45, lw=0)
    for e0, top, lab in [(8.05, 1e10, "Cu Kα"), (17.5, 1e9, "Mo Kα")]:
        ax.plot([e0, e0], [1e8, top], color="0.3", lw=1.6)
        ax.text(e0 * 1.07, top, lab, fontsize=7.5, va="center", color="0.25")
    ax.text(3.0, 3.2e7, "lab tubes", fontsize=8, color="0.2", ha="center", va="center")

    # bending magnet, Ec = 19 keV
    g = _G1(E / 19.0)
    bm = 1e16 * g / g.max()
    ax.plot(E, bm, color=GREEN, lw=2)
    ax.text(0.13, 2.5e16, "bending magnet (3rd gen.)", fontsize=8, color=GREEN, va="bottom")
    yc = 1e16 * _G1([1.0])[0] / g.max()
    ax.plot(19, yc, "o", color=GREEN, ms=5)
    ax.annotate(r"$E_c$ ≈ 19 keV", xy=(19, yc), xytext=(40, 1.2e14),
                fontsize=7.5, color=GREEN, arrowprops=dict(arrowstyle="-", lw=0.6, color=GREEN))

    # wiggler, Ec ~ 33 keV
    gw = _G1(E / 33.0)
    wg = 1e18 * gw / gw.max()
    ax.plot(E, wg, color=ORANGE, lw=2)
    ax.text(45, 2.2e18, "wiggler", fontsize=8, color="#A86F00", va="bottom")

    # undulators: tuning envelopes; 3rd gen. also shows the harmonic comb at one gap
    bump = np.exp(-0.5 * ((np.log10(E) - 0.85) / 0.55) ** 2)
    u3 = 10 ** (19 + 2 * bump) / (1 + (E / 30) ** 4)
    u4 = 10 ** (21 + 1.5 * bump) / (1 + (E / 35) ** 4)
    ax.fill_between(E, 1e21, np.maximum(u4, 1e21), color=PINK, alpha=0.15, lw=0)
    ax.plot(E, u4, color=PINK, lw=2)
    ax.plot(E, u3, color=BLUE, lw=1.0, ls="--")
    E1 = 2.4
    comb = np.zeros_like(E)
    for n in range(1, 14, 2):
        en = n * E1
        comb = np.maximum(comb, np.exp(-0.5 * ((E - en) / (0.02 * en)) ** 2))
    y3 = u3 * (0.02 + 0.98 * comb)
    m3 = (E > 1.5) & (E < 34)
    ax.plot(E[m3], y3[m3], color=BLUE, lw=1.2)
    ax.text(0.13, 1.1e19, "3rd-gen. undulator\n(comb; dashed = envelope)", fontsize=8,
            color=BLUE, va="top")
    ax.text(0.13, 2.6e21, "4th-gen. (MBA) undulator", fontsize=8, color=PINK, va="bottom")

    # energy-use bands
    for (a, b, lab) in [(0.1, 2, "soft X-ray:\nXPS, C/N/O edges"),
                        (5, 9, "3d-metal K edges 5–9 keV"),
                        (60, 150, "high-energy\ndiffraction\nin steel\n60–150 keV")]:
        ax.axvspan(a, b, color="#E9E2F3", alpha=0.6, lw=0, zorder=0)
        ax.text(np.sqrt(a * b), 4e23, lab, ha="center", va="top", fontsize=7, color="#5B3F87")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.1, 200)
    ax.set_ylim(1e6, 1e24)
    ax.set_yticks([1e6, 1e9, 1e12, 1e15, 1e18, 1e21, 1e24])
    ax.set_xticks([0.1, 1, 10, 100])
    ax.set_xticklabels(["0.1", "1", "10", "100"])
    ax.set_xlabel("photon energy (keV)")
    ax.set_ylabel("brilliance (photons s$^{-1}$ mm$^{-2}$\nmrad$^{-2}$ per 0.1 % BW)")
    save(fig, "53", "fig-53-1-source-brilliance")


# ---------------------------------------------------------------- Figure 53.2
E0 = 8333.0


def _chi(k):
    """Model Ni EXAFS: Ni-O (6 at apparent 1.5 A) and Ni-M (6 at apparent 2.5 A)."""
    k = np.asarray(k, float)
    fO = 0.9 * np.exp(-((k - 4.0) / 5.0) ** 2)
    fM = 1.0 * np.exp(-((k - 8.0) / 5.5) ** 2)
    chi = (6 * fO / (k * 2.05 ** 2) * np.exp(-2 * k ** 2 * 0.0045) * np.sin(2 * k * 1.50 + 0.3)
           + 6 * fM / (k * 2.85 ** 2) * np.exp(-2 * k ** 2 * 0.005) * np.sin(2 * k * 2.50 + 0.9))
    return 0.25 * chi


def _mu(E, shift=0.0):
    e0 = E0 + shift
    x = E - e0
    edge = 0.5 + np.arctan(x / 2.0) / np.pi
    white = 0.55 * np.exp(-0.5 * ((x - 8.0) / 4.5) ** 2) * (x > -10)
    post = -0.12 * np.exp(-0.5 * ((x - 30) / 8) ** 2)
    pre = 0.03 * np.exp(-0.5 * ((x + 8.5) / 1.0) ** 2)
    k = 0.5123 * np.sqrt(np.clip(x, 0, None))
    damp = np.clip((k - 2.0) / 1.5, 0, 1)
    ex = np.where(k > 0.5, _chi(np.maximum(k, 0.5)) * damp, 0)
    return edge * (1 + ex) + edge * (white + post) + pre


def xanes_exafs():
    fig = plt.figure(figsize=(6.8, 5.2))
    gs = fig.add_gridspec(2, 3, height_ratios=[1.35, 1.0], hspace=0.62, wspace=0.42)
    ax = fig.add_subplot(gs[0, :])
    E = np.linspace(8250, 8950, 3000)
    ax.axvspan(E0 - 20, E0 + 50, color=ORANGE, alpha=0.15, lw=0)
    ax.axvspan(E0 + 50, 8950, color=SKY, alpha=0.10, lw=0)
    ax.plot(E, _mu(E, 0.0), color=GREEN, lw=1.3, label="Ni$^{2+}$ (discharged)")
    ax.plot(E, _mu(E, 2.5), color=VERM, lw=1.3, ls="--", label="Ni$^{4+}$ (charged)")
    ax.text(E0 + 15, 1.72, "XANES", ha="center", fontsize=9, weight="bold", color="#A86F00")
    ax.text(8700, 1.72, "EXAFS", ha="center", fontsize=9, weight="bold", color=BLUE)
    ax.axvline(E0, color="0.5", lw=0.7, ls=":")
    ax.annotate("$E_0$ = 8333 eV", xy=(E0, 0.2), xytext=(E0 + 60, 0.2), fontsize=8, va="center",
                arrowprops=dict(arrowstyle="-|>", lw=0.7))
    ax.set_xlim(8250, 8950)
    ax.set_ylim(-0.05, 1.85)
    ax.set_xlabel("photon energy (eV)")
    ax.set_ylabel(r"normalized $\mu(E)$")
    ax.legend(loc="lower right", fontsize=8)
    top = ax.secondary_xaxis("top", functions=(lambda e: 0.5123 * np.sqrt(np.clip(e - E0, 0, None)),
                                               lambda k: E0 + (np.asarray(k) / 0.5123) ** 2))
    top.set_xticks([3, 6, 9, 12.5])
    top.set_xticklabels(["3", "6", "9", "12.5"])
    top.set_xlabel(r"$k$ = 0.5123$\sqrt{E-E_0}$ (Å$^{-1}$)", fontsize=9)
    ax.spines["top"].set_visible(True)

    # XANES zoom
    a0 = fig.add_subplot(gs[1, 0])
    Ez = np.linspace(8315, 8365, 600)
    a0.plot(Ez, _mu(Ez, 0.0), color=GREEN, lw=1.3)
    a0.plot(Ez, _mu(Ez, 2.5), color=VERM, lw=1.3, ls="--")
    a0.annotate("", xy=(E0 + 2.5, 0.5), xytext=(E0, 0.5),
                arrowprops=dict(arrowstyle="-|>", lw=0.9, mutation_scale=8))
    a0.text(E0 - 1, 0.62, "+2.5 eV", fontsize=7, ha="right")
    a0.set_xlim(8315, 8365)
    a0.set_xticks([8320, 8340, 8360])
    a0.tick_params(labelsize=7)
    a0.set_xlabel("E (eV)", fontsize=8)
    a0.set_ylabel(r"$\mu(E)$", fontsize=8)
    a0.set_title("edge shift", fontsize=8.5, pad=3)

    # k^2 chi
    a1 = fig.add_subplot(gs[1, 1])
    k = np.linspace(3, 12.5, 600)
    a1.plot(k, k ** 2 * _chi(k), color=BLUE, lw=1.2)
    a1.axhline(0, color="0.6", lw=0.6)
    a1.set_xlim(3, 12.5)
    a1.tick_params(labelsize=7)
    a1.set_xlabel(r"$k$ (Å$^{-1}$)", fontsize=8)
    a1.set_ylabel(r"$k^2\chi(k)$ (Å$^{-2}$)", fontsize=8)
    a1.set_title("EXAFS", fontsize=8.5, pad=3)

    # Fourier transform
    a2 = fig.add_subplot(gs[1, 2])
    kk = np.linspace(3, 12.5, 2048)
    win = np.sin(np.pi * (kk - 3) / 9.5) ** 0.3
    y = kk ** 2 * _chi(kk) * win
    R = np.linspace(0, 6, 600)
    dk = kk[1] - kk[0]
    ft = np.abs((y[None, :] * np.exp(2j * kk[None, :] * R[:, None])).sum(axis=1) * dk) / np.sqrt(np.pi)
    a2.plot(R, ft, color=BLUE, lw=1.3)
    a2.set_xlim(0, 6)
    a2.set_ylim(0, ft.max() * 1.3)
    i1 = np.argmax(ft * (R < 2))
    i2 = np.argmax(ft * (R > 2))
    a2.text(R[i1], ft[i1] * 1.04, "Ni–O", ha="center", va="bottom", fontsize=7.5)
    a2.text(R[i2], ft[i2] * 1.04, "Ni–M", ha="center", va="bottom", fontsize=7.5)
    a2.tick_params(labelsize=7)
    a2.set_xlabel(r"$R$ (Å), no phase correction", fontsize=8)
    a2.set_ylabel(r"$|\chi(R)|$", fontsize=8)
    a2.set_yticks([])
    a2.set_title("Fourier transform", fontsize=8.5, pad=3)
    save(fig, "53", "fig-53-2-xanes-exafs")
    return R[i1], R[i2]


# ---------------------------------------------------------------- Figure 53.3
def _sphere_I(q, R):
    x = np.outer(q, R)
    F = 3 * (np.sin(x) - x * np.cos(x)) / x ** 3
    return F ** 2


def _poly_I(q, Rm, s):
    R = np.linspace(Rm * (1 - 4 * s), Rm * (1 + 4 * s), 401)
    w = np.exp(-0.5 * ((R - Rm) / (s * Rm)) ** 2)
    V2 = R ** 6
    I = (_sphere_I(q, R) * (w * V2)).sum(axis=1) / (w * V2).sum()
    rg2 = 0.6 * (w * R ** 8).sum() / (w * R ** 6).sum()
    return I, np.sqrt(rg2)


def saxs_guinier_porod():
    s = 0.15
    # find mean radius whose Guinier Rg is 3.0 nm
    from scipy.optimize import brentq
    Rm = brentq(lambda r: _poly_I(np.array([1.0]), r, s)[1] - 3.0, 2.0, 4.0)
    q = np.logspace(np.log10(0.05), np.log10(5), 600)
    I, rg = _poly_I(q, Rm, s)
    I = 1e4 * I
    fig, ax = new_fig(6.6, 4.3)
    ax.loglog(q, I, color=BLUE, lw=2)
    qp = np.logspace(0, np.log10(5), 20)
    Ap = np.exp(np.mean(np.log(I[q > 1.5] * q[q > 1.5] ** 4)))
    ax.loglog(qp, 2.2 * Ap * qp ** -4, color=INK, ls="--", lw=1)
    ax.text(1.25, 2.2 * Ap * 1.25 ** -4 * 1.9, "slope −4 (Porod)", fontsize=8.5, rotation=-41,
            rotation_mode="anchor", ha="left")
    ql = 1.3 / rg
    ax.axvline(ql, color=VERM, ls="--", lw=1)
    ax.text(ql / 1.06, 1.2e3, f"Guinier limit\n$q$ = 1.3/$R_g$ = {ql:.2f} nm$^{{-1}}$", fontsize=8, color=VERM,
            va="top", ha="right")
    ax.text(0.055, 1.6e4 / 1.35, "Guinier plateau", fontsize=8.5, va="top")
    ax.set_xlim(0.05, 5)
    ax.set_ylim(1e-2, 1e4 * 1.5)
    ax.set_xlabel(r"$q$ (nm$^{-1}$)")
    ax.set_ylabel(r"$I(q)$ (arb. units)")
    ax.text(4.8, 1.0e4, f"spheres, ~15 % size dispersion\n$R_g$ = 3.0 nm → R = √(5/3) $R_g$ = 3.9 nm\n"
            f"(mean radius {Rm:.1f} nm)", fontsize=7.5, va="top", ha="right", color="0.3")
    top = ax.secondary_xaxis("top", functions=(lambda x: 2 * np.pi / np.clip(x, 1e-6, None),
                                               lambda d: 2 * np.pi / np.clip(d, 1e-6, None)))
    top.set_xticks([100, 30, 10, 3, 2])
    top.set_xticklabels(["100", "30", "10", "3", "2"])
    top.set_xlabel(r"real-space size $2\pi/q$ (nm)")
    ax.spines["top"].set_visible(True)
    # Guinier inset
    ins = ax.inset_axes([0.1, 0.1, 0.36, 0.38])
    q2 = np.linspace(0.005, 0.2, 25)
    Ig, _ = _poly_I(np.sqrt(q2), Rm, s)
    Ig = 1e4 * Ig
    m = q2 <= 0.1
    sl, ic = np.polyfit(q2[m], np.log(Ig[m]), 1)
    ins.plot(q2, np.log(Ig), "o", color=BLUE, ms=3)
    xx = np.linspace(0, 0.2, 10)
    ins.plot(xx, ic + sl * xx, color=INK, lw=1)
    ins.axvline(ql ** 2, color=VERM, lw=0.7, ls=":")
    ins.set_xlim(0, 0.2)
    ins.tick_params(labelsize=6.5)
    ins.set_xlabel(r"$q^2$ (nm$^{-2}$)", fontsize=7, labelpad=1)
    ins.set_ylabel(r"ln $I$", fontsize=7, labelpad=1)
    ins.text(0.195, ic - 0.05, f"slope = {sl:.1f} nm$^2$\n$R_g$ = 3.0 nm", fontsize=7, ha="right", va="top")
    ins.set_title("Guinier plot", fontsize=7, pad=2)
    save(fig, "53", "fig-53-3-saxs-guinier-porod")
    return Rm, rg, sl


# ---------------------------------------------------------------- Figure 53.4
def xray_neutron_contrast():
    els = [("H", 1, -3.74), ("Li", 3, -1.90), ("C", 6, 6.65), ("O", 8, 5.80), ("Al", 13, 3.45),
           ("Ti", 22, -3.44), ("V", 23, -0.38), ("Mn", 25, -3.73), ("Fe", 26, 9.45), ("Co", 27, 2.49),
           ("Ni", 28, 10.3), ("Cu", 29, 7.72), ("Zr", 40, 7.16), ("Pb", 82, 9.41)]
    fig = plt.figure(figsize=(6.8, 5.0))
    gs = fig.add_gridspec(2, 1, height_ratios=[1.25, 1.0], hspace=0.12)
    ax = fig.add_subplot(gs[0])
    a2 = fig.add_subplot(gs[1], sharex=ax)
    Z = np.linspace(1, 82, 200)
    for a in (ax, a2):
        a.axhline(0, color=INK, lw=1.2)
    ax.plot(Z, 2.818 * Z, color=VERM, lw=2, label="X-rays: $f(0)$ = 2.82 $Z$ fm")
    for nm, z, b in els:
        ax.plot([z, z], [0, b], color=BLUE, lw=1.2)
        ax.plot(z, b, "o", color=BLUE, ms=4)
    ax.plot([], [], "o-", color=BLUE, ms=4, lw=1.2, label="neutrons: coherent $b$")
    ax.set_ylim(-5, 120)
    ax.set_ylabel("scattering amplitude (fm)")
    for nm, z, xyt in [("H", 1, (2.0, 42)), ("Fe", 26, (31, 52))]:
        ax.annotate(f"{nm}: {2.818 * z:.1f}", xy=(z, 2.818 * z), xytext=xyt, fontsize=7.5,
                    color=VERM, arrowprops=dict(arrowstyle="-", lw=0.6, color=VERM))
    ax.annotate("Pb: 231 (off scale)", xy=(42.5, 119), xytext=(52, 104), fontsize=7.5, color=VERM,
                arrowprops=dict(arrowstyle="-|>", lw=0.8, color=VERM))
    ax.legend(loc="upper left", fontsize=8)
    ax.text(81, 30, "same data, neutron scale expanded below ↓", fontsize=7.5, ha="right", color="0.35")
    plt.setp(ax.get_xticklabels(), visible=False)

    a2.axhspan(-5, 0, color=VERM, alpha=0.08, lw=0)
    for nm, z, b in els:
        a2.plot([z, z], [0, b], color=BLUE, lw=1.4)
        a2.plot(z, b, "o", color=BLUE, ms=5)
        off = 0.5 if b >= 0 else -0.5
        dx = {"Mn": -0.9, "Fe": -0.4, "Co": 0.3, "Ni": 0.7, "Cu": 1.2, "Ti": -0.6, "V": 0.6}.get(nm, 0)
        a2.text(z + dx, b + off, nm, ha="center", va="bottom" if b >= 0 else "top", fontsize=7.5)
    a2.plot(1, 6.67, "D", color=GREEN, ms=6, zorder=5)
    a2.text(2.2, 6.67, "D", color=GREEN, fontsize=8, va="center")
    a2.set_ylim(-5.5, 12.5)
    a2.set_ylabel("neutron $b$ (fm)")
    a2.set_xlim(0, 84)
    a2.set_xlabel("atomic number $Z$")
    a2.text(83, -4.6, "negative $b$ (shaded)", fontsize=7.5, color=VERM, va="center", ha="right")
    a2.text(5.0, -2.5, "H and D:\nopposite sign →\ncontrast variation", fontsize=7.5,
            bbox=dict(fc="white", ec="0.6", lw=0.6, boxstyle="round,pad=0.3"), ha="left", va="center")
    a2.annotate("V ≈ 0: sample cans", xy=(23, -0.38), xytext=(33, -3.6), fontsize=8,
                bbox=dict(fc="white", ec="0.6", lw=0.6, boxstyle="round,pad=0.3"), va="center",
                arrowprops=dict(arrowstyle="-", lw=0.6))
    save(fig, "53", "fig-53-4-xray-neutron-contrast")


# ---------------------------------------------------------------- Figure 53.5
def apt_reconstruction():
    rng = np.random.default_rng(5)
    fig = plt.figure(figsize=(6.8, 4.4))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.25, 0.8, 1.15], wspace=0.35)

    # (a) instrument principle
    a = fig.add_subplot(gs[0])
    a.set_xlim(0, 10)
    a.set_ylim(0, 10)
    a.axis("off")
    a.set_title("(a) principle", fontsize=9, pad=2)
    # needle tip on the left, pointing right
    xs = np.linspace(0, 1.6, 50)
    tip = [(0.2, 4.2), (1.7, 4.85)]
    th = np.linspace(-np.pi / 2, np.pi / 2, 30)
    apex = [(1.7 + 0.18 * np.cos(t), 5.0 + 0.18 * np.sin(t)) for t in th]
    poly = [(0.2, 4.2), (1.7, 4.82)] + apex + [(1.7, 5.18), (0.2, 5.8)]
    a.add_patch(Polygon(poly, closed=True, fc="0.7", ec=INK, lw=0.9))
    a.text(0.8, 3.75, "needle specimen\napex R ≈ 50 nm\n20–80 K", fontsize=7, ha="center", va="top")
    a.text(0.8, 6.15, "V ≈ 8 kV\n+ pulses", fontsize=7, ha="center", va="bottom")
    # detector
    a.add_patch(Rectangle((8.6, 1.8), 0.45, 6.4, fc="#BFD9EE", ec=INK, lw=0.9))
    a.text(8.82, 8.4, "position-\nsensitive\ndetector", fontsize=7, ha="center", va="bottom")
    # trajectories
    for yd, c in [(2.4, "0.55"), (3.6, "0.55"), (5.0, VERM), (6.4, "0.55"), (7.6, "0.55")]:
        t = np.linspace(0, 1, 50)
        x = 1.9 + (8.6 - 1.9) * t
        y = 5.0 + (yd - 5.0) * (1 - (1 - t) ** 2.5)
        a.plot(x, y, color=c, lw=1.2 if c == VERM else 0.7)
    a.plot(1.9, 5.0, "o", color=VERM, ms=4)
    a.text(4.6, 5.25, r"$^{56}$Fe$^{2+}$", fontsize=7.5, color=VERM)
    a.annotate("", xy=(8.5, 1.2), xytext=(1.9, 1.2), arrowprops=dict(arrowstyle="<|-|>", lw=0.7,
                                                                     mutation_scale=8))
    a.text(5.2, 1.0, "L ≈ 0.1 m", fontsize=7, ha="center", va="top")
    for k, txt in enumerate(["time of flight → m/n", "hit position → x, y", "sequence → z"]):
        a.text(0.0, -0.6 - 0.75 * k, txt, fontsize=7.5, ha="left", va="top")
    a.set_ylim(-2.6, 10)

    # (b) reconstruction box 50 x 50 x 200 nm (oblique projection)
    b = fig.add_subplot(gs[1])
    b.set_aspect("equal")
    b.axis("off")
    b.set_title("(b) reconstruction\n(Fe omitted)", fontsize=9, pad=2)
    W, H, D = 50.0, 200.0, 50.0
    ox, oy = 0.35 * D, 0.25 * D

    def proj(x, y, z):  # x width, y height, z depth
        return x + ox * z / D, y + oy * z / D
    for p0, p1 in [((0, 0, 0), (W, 0, 0)), ((0, 0, 0), (0, H, 0)), ((W, 0, 0), (W, H, 0)),
                   ((0, H, 0), (W, H, 0)), ((0, 0, D), (W, 0, D)), ((0, 0, D), (0, H, D)),
                   ((W, 0, D), (W, H, D)), ((0, H, D), (W, H, D)), ((0, 0, 0), (0, 0, D)),
                   ((W, 0, 0), (W, 0, D)), ((0, H, 0), (0, H, D)), ((W, H, 0), (W, H, D))]:
        (x0, y0), (x1, y1) = proj(*p0), proj(*p1)
        b.plot([x0, x1], [y0, y1], color="0.4", lw=0.7)
    species = [("Cu", ORANGE, 0.30, 0.0005), ("Ni", GREEN, 0.20, 0.007), ("Mn", PINK, 0.10, 0.014),
               ("Si", "0.55", 0.08, 0.005)]
    ncl = 20
    cen = np.column_stack([rng.uniform(4, W - 4, ncl), rng.uniform(5, H - 5, ncl), rng.uniform(4, D - 4, ncl)])
    rad = rng.uniform(1.0, 2.0, ncl)
    pts = {sp[0]: [] for sp in species}
    for c, r in zip(cen, rad):
        nat = int(84.9 * 4 / 3 * np.pi * r ** 3)
        for nm, col, frac, _ in species:
            n = rng.binomial(nat, frac * 0.5)  # 50 % detection efficiency
            v = rng.normal(size=(n, 3))
            v = v / np.linalg.norm(v, axis=1)[:, None] * (r * rng.uniform(0, 1, n) ** (1 / 3))[:, None]
            pts[nm].append(c + v)
    for nm, col, frac, mat in species:
        nmat = int(rng.poisson(84.9 * W * H * D * mat * 0.5 * 0.0015))  # thinned display of matrix solute
        pts[nm].append(np.column_stack([rng.uniform(0, W, nmat), rng.uniform(0, H, nmat), rng.uniform(0, D, nmat)]))
    allp, allc, alls = [], [], []
    for nm, col, frac, _ in species:
        for kk, P in enumerate(pts[nm]):
            allp.append(P)
            allc += [col] * len(P)
            alls += [1.4 if kk < ncl else 0.5] * len(P)
    P = np.vstack(allp)
    perm = rng.permutation(len(P))
    X, Y = proj(P[perm, 0], P[perm, 1], P[perm, 2])
    b.scatter(X, Y, s=np.array(alls)[perm], c=np.array(allc, dtype=object)[perm].tolist(), lw=0, alpha=0.95)
    b.plot([W + ox + 4, W + ox + 4], [10, 30], color=INK, lw=2)
    b.text(W + ox + 6, 20, "20 nm", fontsize=7, va="center", rotation=90)
    b.text(W / 2 + ox / 2, -6, "50 × 50 × 200 nm", fontsize=7, ha="center", va="top")
    for k, (nm, col, _, _) in enumerate(species):
        b.plot(-4 + 19 * k, -24, "o", color=col, ms=4)
        b.text(-0.5 + 19 * k, -24, nm, fontsize=7, va="center")
    b.set_xlim(-6, W + ox + 12)
    b.set_ylim(-30, H + oy + 4)

    # (c) proximity histogram
    c = fig.add_subplot(gs[2])
    d = np.linspace(-2, 2, 200)
    sig = 1 / (1 + np.exp(-d / 0.35))
    conc = {"Cu": 0.05 + (30 - 0.05) * sig, "Ni": 0.7 + (20 - 0.7) * sig,
            "Mn": 1.4 + (10 - 1.4) * sig, "Si": 0.5 + (8 - 0.5) * sig}
    fe = 100 - sum(conc.values())
    cols = {"Cu": ORANGE, "Ni": GREEN, "Mn": PINK, "Si": "0.45"}
    c.semilogy(d, fe, color=INK, lw=1.6, label="Fe (balance)")
    for nm in ["Cu", "Ni", "Mn", "Si"]:
        c.semilogy(d, conc[nm], color=cols[nm], lw=1.6, label=nm)
    dd = np.linspace(-1.9, 1.9, 13)
    for nm in ["Cu", "Ni", "Mn", "Si"]:
        s_ = 1 / (1 + np.exp(-dd / 0.35))
        base = {"Cu": (0.05, 30), "Ni": (0.7, 20), "Mn": (1.4, 10), "Si": (0.5, 8)}[nm]
        val = base[0] + (base[1] - base[0]) * s_
        c.semilogy(dd, val * np.exp(np.random.default_rng(3).normal(0, 0.06, dd.size)), "o",
                   color=cols[nm], ms=2.5)
    c.axvline(0, color="0.5", lw=0.7, ls=":")
    c.set_xlim(-2, 2)
    c.set_ylim(0.02, 150)
    c.set_xlabel("distance from interface (nm)", fontsize=8.5)
    c.set_ylabel("concentration (at.%)", fontsize=8.5)
    c.tick_params(labelsize=7.5)
    c.text(-1.9, 0.03, "matrix", fontsize=7.5, color="0.35")
    c.text(1.9, 55, "cluster core", fontsize=7.5, color="0.35", ha="right")
    c.legend(fontsize=7, loc="lower right", handlelength=1.4)
    c.set_title("(c) proximity histogram", fontsize=9, pad=2)
    save(fig, "53", "fig-53-5-apt-reconstruction")


# ---------------------------------------------------------------- Figure 53.6
def _gauss_img(n, extent, cols):
    """cols: list of (x, y, amplitude, sigma) in pm; returns image n x n over extent (pm)."""
    x = np.linspace(0, extent, n)
    X, Y = np.meshgrid(x, x)
    img = np.zeros_like(X)
    for (cx, cy, a, s) in cols:
        img += a * np.exp(-((X - cx) ** 2 + (Y - cy) ** 2) / (2 * s ** 2))
    return img


def stem_detectors():
    fig = plt.figure(figsize=(6.8, 5.6))
    gs = fig.add_gridspec(3, 3, width_ratios=[1.35, 0.8, 0.8], height_ratios=[1, 1, 1], wspace=0.15, hspace=0.55)

    # ray diagram
    a = fig.add_subplot(gs[:, 0])
    a.set_xlim(-5, 5)
    a.set_ylim(-15.5, 10.5)
    a.set_aspect("equal")
    a.axis("off")
    # source
    a.add_patch(Polygon([(-0.4, 10.2), (0.4, 10.2), (0, 9.5)], closed=True, fc="0.3", ec=INK))
    a.text(0.6, 9.9, "electron source\n(300 kV)", fontsize=7, va="center")
    # corrector
    a.add_patch(FancyBboxPatch((-1.6, 6.6), 3.2, 1.6, boxstyle="round,pad=0.05", fc="#E8DDF2", ec=INK, lw=0.8))
    for xx in np.linspace(-1.3, 1.3, 6):
        a.add_patch(Rectangle((xx - 0.12, 6.75), 0.24, 1.3, fc="#B497D6", ec="none"))
    a.text(1.75, 7.4, "Cs corrector\n(hexapole/\noctupole)", fontsize=7, va="center")
    # beam
    a.plot([-0.3, -0.3], [9.5, 4.4], color=BLUE, lw=0.8)
    a.plot([0.3, 0.3], [9.5, 4.4], color=BLUE, lw=0.8)
    # probe-forming lens
    a.add_patch(Ellipse((0, 4.2), 3.6, 0.5, fc="#CFE3F3", ec=INK, lw=0.8))
    a.text(1.95, 4.2, "probe-forming\nlens", fontsize=7, va="center")
    a.fill([-1.2, 1.2, 0], [4.0, 4.0, 1.0], color=BLUE, alpha=0.25, lw=0)
    a.plot([-1.2, 0], [4.0, 1.0], color=BLUE, lw=0.8)
    a.plot([1.2, 0], [4.0, 1.0], color=BLUE, lw=0.8)
    a.text(-1.3, 2.7, "α = 30 mrad", fontsize=7, ha="right", va="center")
    # specimen with columns
    a.add_patch(Rectangle((-2.2, 0.75), 4.4, 0.5, fc="#F4E3C3", ec=INK, lw=0.7))
    for xx in np.linspace(-2.0, 2.0, 11):
        a.plot([xx, xx], [0.8, 1.2], color="0.45", lw=0.8)
    a.text(2.3, 1.0, "thin crystal\nprobe ≈ 40 pm", fontsize=7, va="center")
    # scattered cones (exaggerated angles): ABF, ADF, HAADF
    yd = -3.0
    ang = {"ABF": (11, 22), "ADF": (40, 80), "HAADF": (80, 200)}
    scale = 0.038  # drawing units per mrad at detector plane
    cols = {"ABF": GREEN, "ADF": ORANGE, "HAADF": VERM}
    for nm, (t0, t1) in ang.items():
        r0, r1 = t0 * scale * 1.0, min(t1, 120) * scale
        for sgn in (-1, 1):
            a.fill([0, sgn * r0, sgn * r1], [1.0 - 0.25, yd, yd], color=cols[nm], alpha=0.18, lw=0)
            a.add_patch(Rectangle((sgn * r0 if sgn > 0 else -r1, yd - 0.3), r1 - r0, 0.3, fc=cols[nm],
                                  ec=INK, lw=0.6))
    # BF / EELS pass-through
    rbf = 30 * scale
    a.fill([0, -rbf, rbf], [0.75, yd, yd], color=BLUE, alpha=0.2, lw=0)
    a.text(0, yd - 0.75, "HAADF > 80 · ADF 40–80 · ABF 11–22 mrad", fontsize=6.6, ha="center", va="top")
    a.text(-4.95, yd - 0.15, "HAADF", fontsize=6.5, color=VERM, ha="left", va="bottom")
    a.text(-3.25, yd + 0.45, "ADF", fontsize=6.5, color="#A86F00", ha="left", va="bottom")
    a.text(-0.85, yd + 0.45, "ABF", fontsize=6.5, color=GREEN, ha="center", va="bottom")
    # EELS spectrometer: prism
    a.plot([0, 0], [yd - 1.6, -6.2], color=BLUE, lw=0.9)
    a.add_patch(Wedge((0, -7.4), 1.3, 90, 180, fc="#D9D9D9", ec=INK, lw=0.8))
    a.text(0.3, -6.6, "magnetic prism", fontsize=7, va="center")
    for de, c in [(0, BLUE), (0.25, SKY), (0.5, PINK)]:
        t = np.linspace(0, 1, 30)
        a.plot(-(1.3 + 1.5 * de) * (1 - np.cos(t * np.pi / 2)), -6.2 - (1.2 + de * 0.4) * np.sin(t * np.pi / 2) - 2.2 * t ** 2,
               color=c, lw=0.9)
    a.text(-2.6, -10.5, "EELS", fontsize=8, weight="bold", ha="center")
    # EELS spectrum sketch
    ax_s = a.inset_axes([0.05, 0.0, 0.9, 0.17])
    e = np.linspace(-10, 700, 2000)
    zl = 1.0 * np.exp(-0.5 * (e / 1.5) ** 2)
    pl = 0.12 * np.exp(-0.5 * ((e - 22) / 7) ** 2)
    bg = 0.03 * (np.clip(e, 5, None) / 30) ** -2.2 * (e > 5)
    edge = 0.01 * (e > 532) * np.exp(-(e - 532) / 300) * (1 + 0.4 * np.exp(-((e - 540) / 6) ** 2))
    spec = zl + pl + bg + edge
    ax_s.semilogy(e, spec, color=INK, lw=0.9)
    ax_s.set_ylim(2e-4, 2)
    ax_s.set_xlim(-10, 700)
    ax_s.set_yticks([])
    ax_s.set_xticks([0, 200, 400, 600])
    ax_s.tick_params(labelsize=6, pad=1)
    ax_s.set_xlabel("energy loss (eV)", fontsize=6.5, labelpad=1)
    ax_s.text(8, 0.6, "zero loss", fontsize=6, ha="left")
    ax_s.text(32, 0.06, "plasmon", fontsize=6, ha="left")
    ax_s.annotate("O K 532 eV", xy=(535, 0.012), xytext=(400, 0.15), fontsize=6,
                  arrowprops=dict(arrowstyle="-", lw=0.5))
    ax_s.spines["left"].set_visible(False)
    ax_s.yaxis.set_minor_locator(plt.NullLocator())
    ax_s.tick_params(axis="y", which="both", left=False)

    # top view of detectors
    t = fig.add_subplot(gs[0, 1])
    t.set_aspect("equal")
    t.axis("off")
    t.set_xlim(-1.15, 1.15)
    t.set_ylim(-1.15, 1.15)
    R = 1.1 / 120
    for nm, (t0, t1) in [("HAADF", (80, 120)), ("ADF", (40, 80)), ("ABF", (11, 22))]:
        t.add_patch(Wedge((0, 0), t1 * R, 0, 360, width=(t1 - t0) * R, fc=cols[nm], ec=INK, lw=0.5, alpha=0.75))
    t.add_patch(Circle((0, 0), 30 * R, fc="none", ec=BLUE, lw=0.8, ls="--"))
    t.text(0, -1.18, "hole → EELS; dashed = BF disc", fontsize=5.8, ha="center", va="top")
    for nm, rr_, c_ in [("HAADF", 100, INK), ("ADF", 60, INK)]:
        t.text(0, -rr_ * R, nm, fontsize=5.5, ha="center", va="center", color=c_)
    t.annotate("ABF", xy=(-16.5 * R * 0.7, 16.5 * R * 0.7), xytext=(-0.95, 0.95), fontsize=5.5,
               ha="center", va="center", arrowprops=dict(arrowstyle="-", lw=0.5))
    t.set_title("detector plane\n(top view)", fontsize=7.5, pad=1)

    # 4D-STEM pixelated detector
    p = fig.add_subplot(gs[0, 2])
    nn = 64
    yy, xx = np.mgrid[0:nn, 0:nn] - nn / 2 + 0.5
    rr = np.hypot(xx, yy)
    cbed = (rr < 12).astype(float)
    for gx, gy in [(26, 0), (-26, 0), (0, 26), (0, -26)]:
        cbed += 0.35 * (np.hypot(xx - gx, yy - gy) < 12)
    cbed += 0.05 * np.random.default_rng(2).random((nn, nn))
    p.imshow(cbed, cmap="gray_r", interpolation="nearest")
    p.set_xticks([])
    p.set_yticks([])
    p.set_title("4D-STEM camera:\nCBED at each (x, y)\n→ (x, y, $k_x$, $k_y$)", fontsize=7, pad=2)

    # HAADF / ABF images
    def si110():
        a_ = 543.1
        cols_ = []
        for i in range(-2, 4):
            for j in range(-2, 4):
                for (bx, by) in [(0, 0), (a_ / np.sqrt(2) / 2, a_ / 2)]:
                    cx = i * a_ / np.sqrt(2) + bx
                    cy = j * a_ + by
                    for dz in (-68, 68):
                        cols_.append((cx + 60, cy + dz + 120, 1.0, 26))
        return _gauss_img(220, 800, cols_)

    def sto(abf=False):
        a_ = 390.5
        cols_ = []
        for i in range(-1, 4):
            for j in range(-1, 4):
                x0, y0 = i * a_ + 100, j * a_ + 100
                zf = (lambda Z: Z ** 1.7) if not abf else (lambda Z: Z ** 0.6)
                cols_.append((x0, y0, zf(38), 30))                    # Sr
                cols_.append((x0 + a_ / 2, y0 + a_ / 2, zf(22) + zf(8), 30))  # Ti-O
                cols_.append((x0 + a_ / 2, y0, zf(8), 30))            # O
                cols_.append((x0, y0 + a_ / 2, zf(8), 30))            # O
        img = _gauss_img(220, 800, cols_)
        return -img if abf else img

    panels = [(gs[1, 1], si110(), "Si ⟨110⟩ HAADF:\ndumbbells 136 pm"),
              (gs[1, 2], sto(), "SrTiO$_3$ ⟨100⟩ HAADF:\nSr bright, Ti–O weaker"),
              (gs[2, 1], sto(abf=True), "SrTiO$_3$ ⟨100⟩ ABF:\nO columns visible")]
    for spec_, img, title in panels:
        q = fig.add_subplot(spec_)
        q.imshow(img, cmap="gray", origin="lower", extent=(0, 800, 0, 800))
        q.set_xticks([])
        q.set_yticks([])
        q.set_title(title, fontsize=7, pad=2)
        bc = "k" if "ABF" in title else "white"
        q.plot([560, 760], [50, 50], color=bc, lw=2.5)
        q.text(660, 75, "200 pm", color=bc, fontsize=6, ha="center", va="bottom")
    # STO legend panel
    lg = fig.add_subplot(gs[2, 2])
    lg.axis("off")
    lg.text(0.0, 0.85, "HAADF: intensity ∝ $Z^{1.6–2}$\n(O, Z = 8, invisible)", fontsize=7, va="top")
    lg.text(0.0, 0.45, "ABF: inverted contrast,\nlight columns (O, Li, H)\nshow as dark dots", fontsize=7, va="top")
    lg.text(0.0, 0.0, "images simulated as Gaussian\ncolumns (schematic)", fontsize=6.3, va="top", color="0.4")
    save(fig, "53", "fig-53-6-stem-detectors")


if __name__ == "__main__":
    source_brilliance()
    print("FT peaks (apparent R):", xanes_exafs())
    print("SAXS Rm, Rg, slope:", saxs_guinier_porod())
    xray_neutron_contrast()
    apt_reconstruction()
    stem_detectors()
