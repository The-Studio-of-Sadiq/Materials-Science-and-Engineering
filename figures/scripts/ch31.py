"""Figures for Chapter 31 — Solid-State Foundations for Materials Engineering.

Run from the repository root:  python figures/scripts/ch31.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator, CubicSpline

kB = 8.617333e-5  # eV/K


# ---------------------------------------------------------------- Figure 31.1
def level_splitting():
    fig = plt.figure(figsize=(6.8, 4.3))
    ax = fig.add_axes([0.09, 0.12, 0.62, 0.84])
    Es, Ep = -10.0, -3.5          # schematic atomic 3s, 3p energies (eV)
    rm, rg, r0 = 0.36, 0.30, 0.235
    r = np.linspace(0.20, 1.0, 800)
    # half-width growth: zero at large spacing, 3.25 eV at the merge point
    w = 3.25 * np.exp((rm - r) / 0.2)
    w = w * np.clip((0.62 - r) / (0.62 - rm), 0, None) ** 0.8
    w[r < rm] = 3.25 * np.exp((rm - r[r < rm]) / 0.2)
    L1, L2, U1, U2 = Es - w, Es + w, Ep - w, Ep + w
    Emid = -4.6
    Eg = np.clip(1.12 * (rg - r) / (rg - r0), 0, None)
    Ev, Ec = Emid - Eg / 2, Emid + Eg / 2

    cv, cc, cm = "#9CC3E4", "#F3C08F", "#C9C9C9"
    sep = r >= rm
    ax.fill_between(r[sep], L1[sep], L2[sep], color=cv, lw=0)
    ax.fill_between(r[sep], U1[sep], U2[sep], color=cc, lw=0)
    mer = (r <= rm) & (r >= rg)
    ax.fill_between(r[mer], L1[mer], U2[mer], color=cm, lw=0)
    sp = r <= rg
    ax.fill_between(r[sp], L1[sp], Ev[sp], color=cv, lw=0)
    ax.fill_between(r[sp], Ec[sp], U2[sp], color=cc, lw=0)
    for y in (L1, U2):
        ax.plot(r, y, color=INK, lw=1.0)
    ax.plot(r[sep], L2[sep], color=INK, lw=1.0)
    ax.plot(r[sep], U1[sep], color=INK, lw=1.0)
    ax.plot(r[sp], Ev[sp], color=INK, lw=1.0)
    ax.plot(r[sp], Ec[sp], color=INK, lw=1.0)

    ax.axvline(r0, color=INK, ls="--", lw=0.9)
    ax.text(r0 + 0.008, 4.3, r"$r_0=0.235$ nm" "\n(Si–Si bond)", fontsize=8.5, va="top")
    i0 = np.argmin(abs(r - r0))
    ax.annotate("", xy=(r0 - 0.012, Ev[i0]), xytext=(r0 - 0.012, Ec[i0]),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.9, color=INK, mutation_scale=7, shrinkA=0, shrinkB=0))
    ax.annotate(r"$E_g=1.12$ eV", xy=(r0 - 0.012, Emid), xytext=(0.285, -6.6), fontsize=9,
                arrowprops=dict(arrowstyle="-", lw=0.7, color=INK))
    bb = dict(fc="white", ec="none", alpha=0.75, pad=1.0)
    ax.text(0.207, -1.6, "conduction band\n4N states, empty", fontsize=8.5, ha="left", bbox=bb)
    ax.text(0.207, -13.9, "valence band\n4N states,\nfilled (4N e$^-$)", fontsize=8.5, ha="left", bbox=bb)
    ax.annotate("bands overlap\nand hybridize", xy=(0.33, 0.0), xytext=(0.40, 2.4), fontsize=8.5,
                color="0.3", arrowprops=dict(arrowstyle="-", lw=0.7, color="0.4"))
    ax.text(0.97, Ep + 0.35, r"$3p$: 6N states, 2N e$^-$", fontsize=8.5, ha="right", va="bottom")
    ax.text(0.97, Es + 0.35, r"$3s$: 2N states, 2N e$^-$", fontsize=8.5, ha="right", va="bottom")
    ax.set_xlim(0.20, 1.0)
    ax.set_ylim(-17.5, 5)
    ax.set_xlabel("interatomic spacing $r$ (nm)")
    ax.set_ylabel("electron energy (eV, schematic)")

    # inset: two-atom bonding / antibonding
    ia = fig.add_axes([0.75, 0.30, 0.24, 0.50])
    ia.set_xlim(0, 4); ia.set_ylim(-3.2, 3.2); ia.axis("off")
    ia.hlines(0, 0.2, 1.0, color=INK, lw=2); ia.hlines(0, 3.0, 3.8, color=INK, lw=2)
    ia.hlines(1.8, 1.6, 2.4, color=COLORS[1], lw=2); ia.hlines(-1.8, 1.6, 2.4, color=COLORS[0], lw=2)
    for xa, xb in [(1.0, 1.6), (3.0, 2.4)]:
        ia.plot([xa, xb], [0, 1.8], ls=":", color="0.4", lw=0.9)
        ia.plot([xa, xb], [0, -1.8], ls=":", color="0.4", lw=0.9)
    ia.text(0.6, -0.35, "atom 1", ha="center", va="top", fontsize=8)
    ia.text(3.4, -0.35, "atom 2", ha="center", va="top", fontsize=8)
    ia.text(2.0, 2.05, "antibonding", ha="center", fontsize=8, color=COLORS[1])
    ia.text(2.0, -2.05, "bonding", ha="center", va="top", fontsize=8, color=COLORS[0])
    ia.plot([1.85, 2.15], [-1.8, -1.8], "o", ms=3, color=INK)
    ia.text(2.0, 3.0, "two atoms (H$_2$-like)", ha="center", fontsize=8.5, va="top")
    ia.add_patch(plt.Rectangle((0.02, -3.1), 3.96, 6.25, fill=False, ec="0.6", lw=0.7))
    save(fig, "31", "fig-31-1-level-splitting-to-bands")


# ---------------------------------------------------------------- Figure 31.2
def tb_nfe():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.8, 3.9), gridspec_kw=dict(width_ratios=[1, 1.35], wspace=0.28))
    # (a) tight binding, eps0 = 0, energies in units of t, k in units of pi/a
    k = np.linspace(-1, 1, 400)
    E = -2 * np.cos(np.pi * k)
    a1.plot(k, E, color=COLORS[0])
    a1.plot(k, -2 + (np.pi * k) ** 2, "--", color=COLORS[1], lw=1.2)
    for y, lab in [(-2, r"$\varepsilon_0-2t$"), (0, r"$\varepsilon_0$"), (2, r"$\varepsilon_0+2t$")]:
        a1.axhline(y, color="0.6", lw=0.7, ls=":")
    a1.set_yticks([-2, 0, 2]); a1.set_yticklabels([r"$\varepsilon_0-2t$", r"$\varepsilon_0$", r"$\varepsilon_0+2t$"])
    a1.annotate("", xy=(-0.93, -2), xytext=(-0.93, 2),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.9, color=INK, mutation_scale=8, shrinkA=0, shrinkB=0))
    a1.text(-0.88, 0.25, "$4t$", ha="left", fontsize=10)
    a1.text(0.40, -1.65, "parabola:\n" r"$m^*=\hbar^2/2ta^2$", ha="left", fontsize=8.5, color=COLORS[1])
    a1.set_xlim(-1, 1); a1.set_ylim(-2.6, 2.9)
    a1.set_xticks([-1, 0, 1]); a1.set_xticklabels([r"$-\pi/a$", "0", r"$\pi/a$"])
    a1.set_xlabel("wavevector $k$"); a1.set_ylabel("energy $E(k)$")
    a1.set_title(r"(a) tight binding: $\varepsilon_0-2t\cos ka$", fontsize=10)

    # (b) nearly free electron, units: E in hbar^2(pi/a)^2/2m, k in pi/a
    U = {1: 0.20, 2: 0.10}
    Gs = np.arange(-4, 5) * 2  # reciprocal vectors in units of pi/a
    kk = np.linspace(-2, 2, 1601)
    bands = []
    for kv in kk:
        q = ((kv + 1) % 2) - 1   # reduced k in [-1,1)
        H = np.diag((q + Gs) ** 2.0)
        for i in range(len(Gs)):
            for j in range(len(Gs)):
                m = abs(Gs[i] - Gs[j]) // 2
                if m in U:
                    H[i, j] = U[m]
        bands.append(np.linalg.eigvalsh(H))
    bands = np.array(bands)
    n = np.floor(np.abs(kk)).astype(int)
    n[n > 1] = 1
    Eext = bands[np.arange(len(kk)), n]
    for sgn in (-1, 1):
        for zone in (0, 1):
            ak = np.abs(kk)
            m = ((ak < 1) if zone == 0 else (ak > 1)) & (np.sign(kk) * sgn >= 0)
            a2.plot(kk[m], Eext[m], color=COLORS[0])
    a2.plot(kk, kk ** 2, "--", color="0.5", lw=1.0)
    for x in (-2, -1, 1, 2):
        a2.axvline(x, color="0.6", ls=":", lw=0.8)
    # gap annotations
    for kz, lab, xo in [(1, r"$2|U_1|$", 0.12), (2, r"$2|U_2|$", -0.12)]:
        i = np.argmin(abs(kk - kz))
        lo, hi = bands[i, kz - 1], bands[i, kz]
        a2.axhspan(lo, hi, color=COLORS[4], alpha=0.25, lw=0)
        a2.text(kz + xo, (lo + hi) / 2, lab, ha="left" if xo > 0 else "right", va="center", fontsize=9)
    a2.text(-1.12, 2.5, "free electron\n" r"$\hbar^2k^2/2m_0$", fontsize=8.5, color="0.4", ha="left", va="top")
    a2.set_xlim(-2.05, 2.05); a2.set_ylim(0, 4.6)
    a2.set_xticks([-2, -1, 0, 1, 2]); a2.set_xticklabels([r"$-2\pi/a$", r"$-\pi/a$", "0", r"$\pi/a$", r"$2\pi/a$"])
    a2.set_yticks([]); a2.set_xlabel("wavevector $k$"); a2.set_ylabel("energy $E(k)$")
    a2.set_title("(b) nearly free electrons", fontsize=10)
    # inset: standing waves at k = pi/a
    ia = a2.inset_axes([0.30, 0.58, 0.40, 0.36])
    x = np.linspace(0, 3, 400)
    ia.plot(x, np.cos(np.pi * x) ** 2, color=COLORS[2], lw=1.2)
    ia.plot(x, np.sin(np.pi * x) ** 2, color=COLORS[3], lw=1.2)
    ia.plot([0, 1, 2, 3], [-0.18] * 4, "o", ms=5, color="0.35")
    ia.text(3.08, 1.0, r"$\cos^2$", fontsize=8, color=COLORS[2], va="center")
    ia.text(3.08, 0.45, r"$\sin^2$", fontsize=8, color=COLORS[3], va="center")
    ia.text(1.5, -0.42, "ion cores", fontsize=7.5, ha="center", va="top", color="0.35")
    ia.set_xlim(-0.15, 3.7); ia.set_ylim(-0.6, 1.15); ia.axis("off")
    save(fig, "31", "fig-31-2-tight-binding-and-nfe-bands")


# ---------------------------------------------------------------- Figure 31.3
def _sat(s, Eend, sig, E0=0.0):
    """Band from E0 at Gamma to Eend at the zone edge, parabolic near Gamma, flat at the edge."""
    return E0 + (Eend - E0) * (1 - np.exp(-(s / sig) ** 2)) / (1 - np.exp(-1 / sig ** 2))


def _band(ax, sL, sX, fL, fX, **kw):
    ax.plot(-0.866 * sL, fL, **kw)
    ax.plot(sX, fX, **kw)


def si_gaas():
    fig, axs = plt.subplots(1, 2, figsize=(6.8, 4.2), sharey=True, gridspec_kw=dict(wspace=0.12))
    s = np.linspace(0, 1, 300)
    vb = dict(color=COLORS[0], lw=1.6)
    cb = dict(color=COLORS[1], lw=1.6)

    def valence(ax, EL, EX, so):
        _band(ax, s, s, _sat(s, EL, 0.55), _sat(s, EX, 0.6), **vb)      # heavy hole
        _band(ax, s, s, _sat(s, EL, 0.30), _sat(s, EX, 0.33), **vb)     # light hole
        _band(ax, s, s, _sat(s, -7.0, 0.5, -so), _sat(s, -7.5, 0.55, -so), **vb)  # split-off / third band

    def nonpar(sk, a, m, Eg):  # E(1+E/Eg) = hbar^2 k^2/2m*, k = sk * 2pi/a
        kA = sk * 2 * np.pi / a
        x = 3.81 * kA ** 2 / m
        return (-1 + np.sqrt(1 + 4 * x / Eg)) * Eg / 2

    # ---- Si
    ax = axs[0]
    valence(ax, -1.2, -2.9, 0.044)
    cbX = CubicSpline([0, 0.2, 0.45, 0.7, 0.85, 1.0], [3.4, 3.2, 2.35, 1.40, 1.12, 1.2],
                      bc_type=((1, 0.0), "not-a-knot"))(s)
    cbL = CubicSpline([0, 0.5, 1.0], [3.4, 2.55, 2.0], bc_type=((1, 0.0), (1, 0.0)))(s)
    _band(ax, s, s, cbL, cbX, **cb)
    cb2X = PchipInterpolator([0, 0.6, 1.0], [3.4, 3.9, 4.5])(s)
    _band(ax, s, s, PchipInterpolator([0, 1], [3.4, 4.3])(s), cb2X, color=COLORS[1], lw=1.0, alpha=0.6)
    ax.annotate("", xy=(0.85, 1.12), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", ls="--", color=COLORS[2], lw=1.2, mutation_scale=10))
    ax.text(0.27, 0.62, "indirect\n+ phonon", fontsize=8.5, color=COLORS[2], ha="center")
    ax.text(0.86, 0.72, "$E_g=1.12$ eV\n(0.85 to X)", fontsize=8, ha="center", va="top")
    ax.plot(0.85, 1.12, "o", ms=4, color=COLORS[1])
    ax.text(-0.84, 1.88, "L 2.0 eV", fontsize=8, va="top")
    ax.text(0.04, 3.48, r"$\Gamma$ 3.4 eV (direct)", fontsize=8, va="bottom")
    ax.text(-0.04, 0.12, "hh, lh", fontsize=8, ha="right")
    ax.text(-0.06, -0.35, "so (−44 meV)", fontsize=8, ha="right")
    ax.set_title("Si (indirect gap)", fontsize=10)

    # ---- GaAs
    ax = axs[1]
    valence(ax, -1.1, -2.9, 0.34)
    a = 5.653
    knots_L = [0, 0.03, 0.06, 0.09, 0.30, 0.65, 1.0]
    vals_L = [1.42] + [1.42 + nonpar(x * 0.866, a, 0.067, 1.42) for x in knots_L[1:4]] + [2.25, 2.0, 1.71]
    cbL = CubicSpline(knots_L, vals_L, bc_type=((1, 0.0), (1, 0.0)))(s)
    knots_X = [0, 0.03, 0.06, 0.09, 0.40, 0.75, 1.0]
    vals_X = [1.42] + [1.42 + nonpar(x, a, 0.067, 1.42) for x in knots_X[1:4]] + [2.45, 2.1, 1.90]
    cbX = CubicSpline(knots_X, vals_X, bc_type=((1, 0.0), (1, 0.0)))(s)
    _band(ax, s, s, cbL, cbX, **cb)
    _band(ax, s, s, PchipInterpolator([0, 1], [4.6, 3.3])(s), PchipInterpolator([0, 1], [4.6, 2.6])(s),
          color=COLORS[1], lw=1.0, alpha=0.6)
    ax.annotate("", xy=(0, 1.42), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[2], lw=1.4, mutation_scale=10, shrinkA=0, shrinkB=0))
    ax.text(0.04, 0.45, "direct\n$E_g=1.42$ eV", fontsize=8.5, color=COLORS[2])
    ax.annotate(r"$m^*=0.067\,m_0$", xy=(-0.02, 1.48), xytext=(-0.08, 0.72), fontsize=8, ha="right",
                arrowprops=dict(arrowstyle="-", lw=0.6, color="0.4"))
    ax.text(-0.84, 1.60, "L 1.71 eV\n(+0.29 eV)", fontsize=8, va="top")
    ax.text(0.98, 1.62, "X 1.90 eV", fontsize=8, ha="right", va="top")
    ax.text(-0.06, -0.62, "so (−0.34 eV)", fontsize=8, ha="right")
    ax.set_title("GaAs (direct gap)", fontsize=10)

    for ax in axs:
        ax.axhline(0, color="0.6", lw=0.6, ls=":")
        for x in (-0.866, 0, 1):
            ax.axvline(x, color="0.75", lw=0.7)
        ax.set_xlim(-0.866, 1); ax.set_ylim(-3, 4)
        ax.set_xticks([-0.866, 0, 1]); ax.set_xticklabels(["L", r"$\Gamma$", "X"])
        ax.set_xlabel("wavevector")
    axs[0].set_ylabel("energy (eV, zero at valence-band maximum)")
    save(fig, "31", "fig-31-3-si-gaas-band-structures")


# ---------------------------------------------------------------- Figure 31.4
def dos_fermi():
    T = 300; kT = kB * T
    Nc, Nv, Eg = 2.86e19, 3.10e19, 1.12
    E = np.linspace(-0.3, 1.4, 4000)
    gc = np.where(E > Eg, 2 / np.sqrt(np.pi) * Nc * np.sqrt(np.clip(E - Eg, 0, None)) / kT ** 1.5, 0)
    gv = np.where(E < 0, 2 / np.sqrt(np.pi) * Nv * np.sqrt(np.clip(-E, 0, None)) / kT ** 1.5, 0)
    EF_i = Eg / 2 + 0.75 * kT * np.log(Nv / Nc)
    EF_n = Eg - 0.20
    f = lambda EF: 1 / (1 + np.exp((E - EF) / kT))

    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(6.8, 4.2), sharey=True,
                                     gridspec_kw=dict(width_ratios=[1, 1, 1.3], wspace=0.10))
    a1.plot(gc / 1e21, E, color=COLORS[1]); a1.plot(gv / 1e21, E, color=COLORS[0])
    a1.set_xlim(0, 3.2); a1.set_xlabel(r"$g(E)$ ($10^{21}$ cm$^{-3}$eV$^{-1}$)")
    a1.text(1.6, 1.30, r"$g_c(E)$", color=COLORS[1], fontsize=9)
    a1.text(1.6, -0.22, r"$g_v(E)$", color=COLORS[0], fontsize=9)
    a1.text(0.15, 0.56, "no states\nin the gap", fontsize=8.5, va="center", color="0.35")
    a1.set_ylabel("energy (eV)")
    a1.set_title("density of states", fontsize=10)

    a2.plot(f(EF_i), E, color=INK, label="intrinsic ($E_F$ midgap)")
    a2.plot(f(EF_n), E, "--", color=COLORS[3], label=r"n-type ($E_F=E_c-0.2$ eV)")
    a2.set_xlim(-0.03, 1.08); a2.set_xticks([0, 0.5, 1]); a2.set_xlabel("$f(E)$")
    a2.legend(["intrinsic\n($E_F$ midgap)", "n-type\n($E_F=E_c-0.2$ eV)"], loc="upper right",
              fontsize=7.5, handlelength=1.6)
    a2.set_title("Fermi–Dirac, 300 K", fontsize=10)
    # kT scale bar
    a2.plot([0.08, 0.08], [0.15, 0.15 + kT], color=INK, lw=3, solid_capstyle="butt")
    a2.text(0.13, 0.15 + kT / 2, "$k_BT$ = 25.9 meV", fontsize=7.5, ha="left", va="center")

    lo = 1e2
    for EF, col, ls, lab in [(EF_i, INK, "-", "intrinsic"), (EF_n, COLORS[3], "--", "n-type")]:
        ne = np.clip(gc * f(EF), lo, None); nh = np.clip(gv * (1 - f(EF)), lo, None)
        a3.plot(ne, E, ls=ls, color=col, lw=1.3)
        a3.plot(nh, E, ls=ls, color=col, lw=1.3, label=lab)
    neN = np.clip(gc * f(EF_n), lo, None); nhN = np.clip(gv * (1 - f(EF_n)), lo, None)
    a3.fill_betweenx(E, lo, neN, where=E > Eg, color=COLORS[1], alpha=0.30, lw=0)
    a3.fill_betweenx(E, lo, nhN, where=E < 0, color=COLORS[0], alpha=0.30, lw=0)
    a3.set_xscale("log"); a3.set_xlim(1e3, 1e19)
    a3.set_xticks([1e4, 1e8, 1e12, 1e16])
    a3.set_xlabel(r"carriers per eV (cm$^{-3}$eV$^{-1}$)")
    a3.text(3e3, 1.07, "electrons $g_cf$ (above $E_c$)", fontsize=8, color=COLORS[1], va="center")
    a3.text(3e3, 0.05, "holes $g_v(1-f)$ (below $E_v$)", fontsize=8, color=COLORS[0], va="center")
    a3.text(2e14, 1.20, r"n-type:" "\n" r"$n\approx10^{16}$", fontsize=7.5, color=COLORS[3], ha="center")
    a3.text(3e3, 0.20, r"n-type: $p\approx10^{4}$ cm$^{-3}$", fontsize=7.5, color=COLORS[3])
    a3.text(3e3, 0.80, r"intrinsic: $n=p=n_i$", fontsize=7.5, color=INK)
    a3.text(3e3, 0.70, "peaks lie $k_BT/2$\ninside each band", fontsize=7.5, color="0.35", va="top")
    a3.legend(loc="center", fontsize=7.5, bbox_to_anchor=(0.5, 0.40))
    a3.set_title("carrier distributions", fontsize=10)

    for ax in (a1, a2, a3):
        ax.axhspan(0, Eg, color="0.94", lw=0, zorder=0)
        ax.axhline(Eg, color="0.5", lw=0.7); ax.axhline(0, color="0.5", lw=0.7)
        ax.axhline(EF_i, color=INK, lw=0.6, ls=":")
        ax.axhline(EF_n, color=COLORS[3], lw=0.6, ls=":")
    a1.text(3.15, Eg + 0.02, "$E_c$", ha="right", va="bottom", fontsize=9)
    a1.text(3.15, 0.02, "$E_v$", ha="right", va="bottom", fontsize=9)
    a1.text(3.15, EF_i + 0.02, "$E_{F}$ (i)", ha="right", va="bottom", fontsize=8)
    a1.text(3.15, EF_n - 0.02, "$E_{F}$ (n)", ha="right", va="top", fontsize=8, color=COLORS[3])
    a1.set_ylim(-0.3, 1.4)
    save(fig, "31", "fig-31-4-dos-fermi-carriers")


# ---------------------------------------------------------------- Figure 31.5
NI_MAT = {
    # name: (Nc300, Nv300, Eg(T) function, calibrate to n_i(300) or None, colour)
    "Ge": (1.04e19, 6.0e18, lambda T: 0.7437 - 4.774e-4 * T ** 2 / (T + 235), None),
    "Si": (2.86e19, 3.10e19, lambda T: 1.17 - 4.73e-4 * T ** 2 / (T + 636), 1.0e10),
    "GaAs": (4.4e17, 9.0e18, lambda T: 1.519 - 5.405e-4 * T ** 2 / (T + 204), None),
    "4H-SiC": (1.7e19, 2.5e19, lambda T: 3.26 - 6.5e-4 * (T ** 2 / (T + 1300) - 300 ** 2 / 1600), None),
    "GaN": (2.2e18, 4.6e19, lambda T: 3.39 - 7.7e-4 * (T ** 2 / (T + 600) - 300 ** 2 / 900), None),
}


def ni(name, T):
    Nc, Nv, Eg, cal = NI_MAT[name]
    v = np.sqrt(Nc * Nv) * (T / 300) ** 1.5 * np.exp(-Eg(T) / (2 * kB * T))
    if cal:
        v = v * cal / (np.sqrt(Nc * Nv) * np.exp(-Eg(300) / (2 * kB * 300)))
    return v


def ni_vs_T():
    from scipy.optimize import brentq
    fig, ax = new_fig(6.4, 4.2)
    x = np.linspace(0.45, 4.1, 600)
    T = 1000 / x
    for i, name in enumerate(NI_MAT):
        ax.semilogy(x, ni(name, T), color=COLORS[i], label=name)
        T15 = brentq(lambda t: np.log(ni(name, t) / 1e15), 200, 3000)
        print(f"  {name}: n_i(300)={ni(name, 300):.2g}, n_i=1e15 at {T15:.0f} K")
    ax.axvspan(1000 / 448.15, 1000 / 398.15, color=COLORS[4], alpha=0.25, lw=0)
    ax.text(1000 / 423, 3e-9, "125–175 °C\njunction\nlimits", ha="center", fontsize=8, color="0.25")
    for y in (1e14, 1e15):
        ax.axhline(y, color="0.45", ls="--", lw=0.8)
    ax.text(4.05, 1.6e15, "typical drift-layer doping", ha="right", fontsize=8, color="0.3")
    ax.set_ylim(1e-10, 1e18); ax.set_xlim(0.45, 4.1)
    ax.set_xlabel(r"$1000/T$ (K$^{-1}$)"); ax.set_ylabel(r"intrinsic concentration $n_i$ (cm$^{-3}$)")
    # direct labels
    for name, xl, fac, va in [("Ge", 3.6, 1 / 40, "top"), ("Si", 3.6, 1 / 40, "top"), ("GaAs", 3.6, 1 / 40, "top"),
                              ("4H-SiC", 2.9, 100, "bottom"), ("GaN", 2.9, 1 / 100, "top")]:
        y = ni(name, 1000 / xl)
        ax.text(xl, y * fac, name, fontsize=9, color=COLORS[list(NI_MAT).index(name)],
                ha="left" if name in ("4H-SiC", "GaN") else "center", va=va)
    ax.set_yticks([10.0 ** k for k in range(-10, 19, 4)])
    top = ax.secondary_xaxis("top", functions=(lambda v: v, lambda v: v))
    tc = np.array([-25, 25, 125, 300, 600, 1000])
    top.set_xticks(1000 / (tc + 273.15)); top.set_xticklabels([f"{c}" for c in tc])
    top.set_xlabel("temperature (°C)")
    save(fig, "31", "fig-31-5-ni-vs-temperature")


# ---------------------------------------------------------------- Figure 31.6
ABS = {
    "Si": [(1.06, 0.12), (1.10, 1.1), (1.127, 3.5), (1.17, 14), (1.24, 64), (1.38, 306), (1.55, 850),
           (1.77, 1.9e3), (2.07, 4.1e3), (2.48, 1.1e4), (2.76, 2.6e4), (3.10, 9.5e4), (3.26, 1.6e5),
           (3.35, 6.0e5), (3.42, 1.05e6), (3.50, 1.15e6)],
    "Ge": [(0.62, 0.15), (0.66, 0.8), (0.70, 12), (0.74, 60), (0.78, 200), (0.795, 400), (0.80, 1.6e3),
           (0.81, 5.0e3), (0.85, 7.5e3), (0.90, 9.5e3), (1.0, 1.3e4), (1.24, 2.0e4), (1.5, 4.5e4),
           (1.8, 9e4), (2.1, 3e5), (2.5, 5e5), (3.0, 7e5), (3.5, 1.0e6)],
    "GaAs": [(1.36, 1.0), (1.39, 15), (1.41, 300), (1.42, 3e3), (1.43, 6.5e3), (1.47, 1.0e4), (1.55, 1.2e4),
             (1.8, 2.3e4), (2.1, 4e4), (2.5, 8e4), (2.9, 4e5), (3.2, 7e5), (3.5, 8e5)],
    "InP": [(1.28, 1.0), (1.31, 15), (1.33, 300), (1.34, 3e3), (1.36, 9e3), (1.40, 1.4e4), (1.55, 2.0e4),
            (1.8, 3.2e4), (2.2, 6e4), (2.6, 1.2e5), (3.1, 5e5), (3.5, 7e5)],
}


def absorption():
    fig, ax = new_fig(6.4, 4.3)
    cols = {"Si": COLORS[0], "Ge": COLORS[2], "GaAs": COLORS[1], "InP": COLORS[3]}
    for name, tab in ABS.items():
        e, a = np.array(tab).T
        ee = np.linspace(e[0], e[-1], 800)
        aa = 10 ** PchipInterpolator(e, np.log10(a))(ee)
        ls = "-" if name in ("GaAs", "InP") else "-"
        ax.semilogy(ee, aa, color=cols[name], ls=ls, lw=1.7)
    lab = {"Si": (1.62, 260, "Si (indirect)"), "Ge": (0.63, 1.2e5, "Ge (indirect,\ndirect at 0.80 eV)"),
           "GaAs": (1.55, 3.2e3, "GaAs\n(direct)"), "InP": (1.31, 1.5e3, "InP (direct)")}
    for name, (x, y, t) in lab.items():
        ax.text(x, y, t, color=cols[name], fontsize=8.5, ha="left" if name != "InP" else "right")
    for nm, txt in [(1550, "1550"), (1310, "1310"), (850, "850 nm")]:
        ev = 1239.84 / nm
        ax.axvline(ev, color="0.55", ls=":", lw=0.9)
        ax.text(ev + 0.015, 2.0, txt, fontsize=8, color="0.35", rotation=90, va="bottom")
    ax.set_xlim(0.6, 3.5); ax.set_ylim(1, 1e7)
    ax.set_xlabel("photon energy (eV)"); ax.set_ylabel(r"absorption coefficient $\alpha$ (cm$^{-1}$)")
    top = ax.secondary_xaxis("top", functions=(lambda e: e, lambda e: e))
    wl = np.array([2000, 1000, 800, 600, 500, 400])
    top.set_xticks(1239.84 / wl); top.set_xticklabels([str(w) for w in wl])
    top.set_xlabel("wavelength (nm)")
    right = ax.secondary_yaxis("right", functions=(lambda a: 1 / np.clip(a, 1e-30, None),
                                                   lambda d: 1 / np.clip(d, 1e-30, None)))
    depth = [1, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7]
    right.set_yticks(depth)
    right.set_yticklabels(["10 mm", "1 mm", "100 µm", "10 µm", "1 µm", "100 nm", "10 nm", "1 nm"])
    right.set_ylabel(r"absorption depth $1/\alpha$")
    ax.spines["right"].set_visible(True)
    save(fig, "31", "fig-31-6-absorption-coefficient")


if __name__ == "__main__":
    level_splitting()
    tb_nfe()
    si_gaas()
    dos_fermi()
    ni_vs_T()
    absorption()
