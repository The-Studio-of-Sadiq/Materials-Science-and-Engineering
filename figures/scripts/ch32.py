"""Figures for Chapter 32 — Semiconductor Material Properties.

Run from the repository root:  python figures/scripts/ch32.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc
from scipy.optimize import brentq

kB = 8.617333e-5  # eV/K


def ni_si(T):
    """Intrinsic concentration of Si (cm^-3), Green's Nc, Nv with Varshni gap, calibrated to 1.0e10 at 300 K."""
    Eg = lambda t: 1.17 - 4.73e-4 * t ** 2 / (t + 636)
    pref = 1.0e10 / np.exp(-Eg(300) / (2 * kB * 300))
    return pref * (T / 300) ** 1.5 * np.exp(-Eg(T) / (2 * kB * T))


# ---------------------------------------------------------------- Figure 32.1
def dopant_levels():
    fig, ax = plt.subplots(figsize=(6.8, 5.0))
    Eg = 1.12
    W = 10.9
    ax.set_xlim(0, 14.0); ax.set_ylim(-0.22, 1.34); ax.axis("off")
    ax.add_patch(plt.Rectangle((0, Eg), W, 0.20, fc="#F3C08F", ec="none"))
    ax.add_patch(plt.Rectangle((0, -0.20), W, 0.20, fc="#9CC3E4", ec="none"))
    ax.plot([0, W], [Eg, Eg], color=INK, lw=1.2); ax.plot([0, W], [0, 0], color=INK, lw=1.2)
    ax.text(0.1, Eg + 0.10, "conduction band   $E_c$ = 1.12 eV", va="center", fontsize=9)
    ax.text(0.1, -0.10, "valence band   $E_v$ = 0", va="center", fontsize=9)
    Ei = 0.56
    ax.plot([0, W], [Ei, Ei], ls=":", color="0.4", lw=1.0)
    ax.text(0.1, Ei + 0.012, "$E_i$ (midgap)", fontsize=8.5, color="0.35", va="bottom")

    sh = COLORS[0]
    for i, (n, e) in enumerate([("Sb", 0.043), ("P", 0.045), ("As", 0.054)]):
        x = 0.4 + i * 1.0
        ax.plot([x, x + 0.7], [Eg - e] * 2, color=sh, lw=2.4)
        ax.text(x + 0.35, Eg - e - 0.02, f"{n}\n{e*1000:.0f}", ha="center", va="top", fontsize=8.5, color=sh)
    x = 3.5
    ax.plot([x, x + 0.7], [Eg - 0.026] * 2, color=sh, lw=1.4, ls="--")
    ax.text(x + 0.35, Eg - 0.046, "hydrogenic\nestimate\n26", ha="center", va="top", fontsize=8, color=sh)
    ax.text(0.4, Eg - 0.27, "shallow donors\n(meV below $E_c$)", fontsize=8.5, color=sh, va="top")
    for i, (n, e) in enumerate([("B", 0.045), ("Al", 0.069), ("Ga", 0.074), ("In", 0.157)]):
        x = 0.4 + i * 1.0
        ax.plot([x, x + 0.7], [e] * 2, color=sh, lw=2.4)
        ax.text(x + 0.35, e + 0.02, f"{n}\n{e*1000:.0f}", ha="center", va="bottom", fontsize=8.5, color=sh)
    ax.text(0.4, 0.33, "shallow acceptors\n(meV above $E_v$)", fontsize=8.5, color=sh, va="bottom")

    dp = COLORS[1]
    deep = [("Pt (A)", Eg - 0.23, "$E_c-0.23$"), ("divacancy", Eg - 0.42, "$E_c-0.42$"),
            ("Au (A)", Eg - 0.55, "$E_c-0.55$"), ("Fe$_i$ (D)", 0.38, "$E_v+0.38$"),
            ("Au (D)", 0.35, "$E_v+0.35$")]
    for i, (n, e, lab) in enumerate(deep):
        x = 5.0 + i * 1.2
        ax.plot([x, x + 0.8], [e, e], color=dp, lw=2.4)
        ax.text(x + 0.4, e + 0.015, f"{n}\n{lab}", ha="center", va="bottom", fontsize=8, color=dp)
    ax.text(5.0, 0.13, "deep levels (A = acceptor, D = donor)", fontsize=8.5, color=dp)

    ax.text(11.2, Eg - 0.04, "shallow levels:\nionized at 300 K,\nset $n$ and $p$", fontsize=8.5,
            color=sh, va="top")
    ax.text(11.2, Ei + 0.12, "deep levels:\nrecombination\ncentres, set the\nlifetime", fontsize=8.5,
            color=dp, va="top")
    ax.text(11.2, 0.22, "Si, 300 K;\ngap to scale", fontsize=8.5, color="0.35", va="top")
    save(fig, "32", "fig-32-1-dopant-levels")


# ---------------------------------------------------------------- Figure 32.2
def doping_profiles():
    fig, ax = new_fig(6.4, 4.2)
    x = np.linspace(0, 2.0, 2001)
    NB = 1e16
    # (1) erfc, Ns = 1e20, xj = 0.5 um
    L1 = 0.5 / 2.7511
    N1 = 1e20 * erfc(x / L1)
    # (2) Gaussian drive-in, Ns = 1e18, xj = 1.2 um
    L2 = 1.2 / np.sqrt(np.log(1e18 / NB))
    N2 = 1e18 * np.exp(-(x / L2) ** 2)
    # (3) boron implant 1e15 cm^-2, Rp 0.16 um, dRp 0.05 um
    Rp, dR, dose = 0.16, 0.05, 1e15
    N3 = dose / (np.sqrt(2 * np.pi) * dR * 1e-4) * np.exp(-(x - Rp) ** 2 / (2 * dR ** 2))
    # (4) epitaxial n layer 1e16 on 1e19 substrate at 1.5 um (slightly graded by autodoping)
    N4 = 1e16 + 1e19 * 0.5 * erfc(-(x - 1.5) / 0.04)
    ax.axhline(NB, color="0.45", ls="--", lw=0.9)
    ax.text(1.98, NB * 0.75, r"background $10^{16}$ cm$^{-3}$", ha="right", va="top", fontsize=8.5, color="0.35")
    curves = [(N1, COLORS[0], "erfc (constant source), $N_s=10^{20}$"),
              (N2, COLORS[2], "Gaussian drive-in, $N_s=10^{18}$"),
              (N3, COLORS[1], r"B implant $10^{15}$ cm$^{-2}$, 50 keV"),
              (N4, COLORS[3], "epitaxial $10^{16}$ layer on $10^{19}$ substrate")]
    for N, c, lab in curves:
        ax.semilogy(x, np.clip(N, 1e10, None), color=c, label=lab)
    for xj, c in [(0.5, COLORS[0]), (1.2, COLORS[2]), (Rp + dR * np.sqrt(2 * np.log(7.5e19 / NB)), COLORS[1])]:
        ax.plot(xj, NB, "o", ms=5, color=c, zorder=5)
        off = {0.5: (0.80, 2.5e15), 1.2: (1.20, 1.5e15)}.get(round(xj, 2), (0.15, 1.5e15))
        ax.annotate(f"$x_j$ = {xj:.2f} µm", xy=(xj, NB), xytext=off,
                    fontsize=8, color=c, ha="center", arrowprops=dict(arrowstyle="-", lw=0.6, color=c))
    ax.annotate("", xy=(1.5, 3e17), xytext=(1.5, 3e16),
                arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[3]))
    ax.text(1.53, 1.2e17, "n/n$^+$ high–low step\n(no junction)", fontsize=8, color=COLORS[3], va="center")
    ax.text(Rp, 1.3e20, r"$R_p$ = 0.16 µm", fontsize=8, color=COLORS[1], ha="center")
    # built-in field in the graded region of the drive-in profile
    ax.annotate("", xy=(1.02, 2.5e18), xytext=(0.66, 2.5e18),
                arrowprops=dict(arrowstyle="-|>", lw=1.3, color=INK, mutation_scale=11))
    ax.text(0.84, 3.6e18, r"built-in field (graded region)   $\mathcal{E}=-\frac{k_BT}{q}\frac{1}{N}\frac{dN}{dx}$",
            ha="center", fontsize=8.5)
    ax.set_xlim(0, 2.0); ax.set_ylim(1e14, 1e21)
    ax.set_xlabel("depth $x$ (µm)"); ax.set_ylabel(r"dopant concentration (cm$^{-3}$)")
    ax.legend(loc="upper right", fontsize=8)
    save(fig, "32", "fig-32-2-doping-profiles")


# ---------------------------------------------------------------- Figure 32.3
def ct_mobility(N, mumax, mumin, Nref, alpha):
    return mumin + (mumax - mumin) / (1 + (N / Nref) ** alpha)


def mobility():
    fig, ax = new_fig(6.4, 4.2)
    N = np.logspace(13, 21, 400)
    si_n = (1414, 68.5, 9.2e16, 0.711)
    ax.loglog(N, ct_mobility(N, *si_n), color=COLORS[0], label="Si electrons")
    ax.loglog(N, ct_mobility(N, 470.5, 44.9, 2.23e17, 0.719), color=COLORS[1], label="Si holes")
    ax.loglog(N, ct_mobility(N, 8500, 800, 1e17, 0.5), "--", color=COLORS[2], label="GaAs electrons")
    ax.loglog(N, ct_mobility(N, 950, 40, 2e17, 0.76), ":", color=COLORS[3], lw=2.2,
              label="4H-SiC electrons (in-plane)")
    Nt = [1e14, 1e15, 1e16, 1e17, 1e18, 1e19, 1e20]
    ax.plot(Nt, ct_mobility(np.array(Nt), *si_n), "o", ms=3.5, color=COLORS[0])
    ax.plot(Nt, ct_mobility(np.array(Nt), 470.5, 44.9, 2.23e17, 0.719), "o", ms=3.5, color=COLORS[1])
    # parameter markers for Si electrons
    ax.axhline(1414, xmax=0.30, color=COLORS[0], lw=0.8, ls="-.")
    ax.text(1.3e13, 1414 * 1.30, r"$\mu_{\max}$ = 1414", fontsize=8.5, color=COLORS[0])
    ax.axhline(68.5, xmin=0.75, color=COLORS[0], lw=0.8, ls="-.")
    ax.annotate(r"$\mu_{\min}$ = 68.5", xy=(5e20, 68.5), xytext=(2e20, 27), fontsize=8.5, color=COLORS[0],
                ha="center", arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[0]))
    mid = (1414 + 68.5) / 2
    ax.annotate(r"$N_{\mathrm{ref}}=9.2\times10^{16}$" "\n" r"($\mu=(\mu_{\max}+\mu_{\min})/2$)",
                xy=(9.2e16, mid), xytext=(1.3e13, 150), fontsize=8.5, color=COLORS[0], va="center",
                arrowprops=dict(arrowstyle="-|>", lw=0.8, color=COLORS[0], mutation_scale=9, relpos=(1.0, 0.5)))
    ax.plot(9.2e16, mid, "s", ms=5, mfc="white", mec=COLORS[0])
    ax.text(3e13, 14, "lattice-limited\n(phonon scattering)", fontsize=8.5, color="0.35")
    ax.text(5e20, 14, "impurity-limited\n(ionized-impurity scattering)", fontsize=8.5, color="0.35", ha="right")
    ax.set_xlim(1e13, 1e21); ax.set_ylim(10, 1e4)
    ax.set_xlabel(r"total ionized impurity concentration (cm$^{-3}$)")
    ax.set_ylabel(r"mobility (cm$^2$ V$^{-1}$ s$^{-1}$)")
    ax.legend(loc="upper right", fontsize=8)
    save(fig, "32", "fig-32-3-mobility-vs-doping")


# ---------------------------------------------------------------- Figure 32.4
def lifetime():
    fig, ax = new_fig(6.4, 4.3)
    N = np.logspace(14, 20, 400)
    tsrh, B, Cn = 1e-3, 1e-14, 2.8e-31
    trad = 1 / (B * N); taug = 1 / (Cn * N ** 2)
    ttot = 1 / (1 / tsrh + 1 / trad + 1 / taug)
    Nx = np.sqrt(1 / (tsrh * Cn))
    ax.axvspan(1e14, Nx, color=COLORS[5], alpha=0.10, lw=0)
    ax.axvspan(Nx, 1e20, color=COLORS[1], alpha=0.07, lw=0)
    ax.text(3e14, 2e-10 * 1.4, "SRH-limited\n(purity)", fontsize=9, color="0.3", va="bottom")
    ax.text(8e19, 0.25, "Auger-limited\n(intrinsic)", fontsize=9, color="0.3", va="top", ha="right")
    ax.loglog(N, np.full_like(N, tsrh), color=COLORS[0], lw=1.3)
    ax.loglog(N, np.full_like(N, 1e-5), "--", color=COLORS[0], lw=1.0)
    ax.loglog(N, trad, color=COLORS[2], lw=1.3)
    ax.loglog(N, taug, color=COLORS[1], lw=1.3)
    ax.loglog(N, ttot, color=INK, lw=2.8)
    ax.loglog(N, 1 / (2e-10 * N), ":", color=COLORS[3], lw=1.8)
    ax.text(1.3e14, 1.4e-3, r"$\tau_{\mathrm{SRH}}$ = 1 ms (clean float-zone)", fontsize=8.5, color=COLORS[0])
    ax.text(1.0e15, 1.4e-5, r"$\tau_{\mathrm{SRH}}$ = 10 µs (contaminated)", fontsize=8.5, color=COLORS[0])
    ax.text(2.5e14, 0.08, r"radiative $1/BN$, $B=10^{-14}$", fontsize=8.5, color=COLORS[2], rotation=-22, rotation_mode="anchor")
    ax.text(3e16, 0.12, "Auger " r"$1/C_nN^2$" "\n" r"$C_n=2.8\times10^{-31}$", fontsize=8.5, color=COLORS[1])
    ax.text(1.0e16, 1.5e-4, "total", fontsize=9, color=INK, fontweight="bold", va="top")
    ax.text(1.0e16, 2.5e-8, r"GaAs radiative, $B=2\times10^{-10}$", fontsize=8.5, color=COLORS[3], rotation=-22)
    for n, t, lab in [(1e17, ttot[np.argmin(abs(N - 1e17))], "0.21 ms"), (1e18, None, "3.4 µs"),
                      (1e19, None, "36 ns")]:
        t = 1 / (1 / tsrh + B * n + Cn * n ** 2)
        ax.plot(n, t, "o", ms=4, color=INK)
        ax.text(n * 1.3, t * 1.3, lab, fontsize=8, va="bottom")
    ax.plot(Nx, tsrh / 2, "s", ms=4, mfc="white", mec=COLORS[1])
    ax.set_xlim(1e14, 1e20); ax.set_ylim(1e-10, 1)
    ax.set_xlabel(r"doping $N_D$ (cm$^{-3}$)"); ax.set_ylabel(r"minority-carrier lifetime $\tau$ (s)")
    sec = ax.secondary_yaxis("right")
    sec.set_yticks([1e-9, 1e-6, 1e-3]); sec.set_yticklabels(["1 ns", "1 µs", "1 ms"])
    save(fig, "32", "fig-32-4-lifetime-vs-doping")


# ---------------------------------------------------------------- Figure 32.5
def n_of_T(ND, T, Ed=0.045, gD=2):
    Nc = 2.86e19 * (T / 300) ** 1.5
    n1 = Nc / gD * np.exp(-Ed / (kB * T))
    ni = ni_si(T)
    f = lambda ln: np.exp(ln) - ND / (1 + np.exp(ln) / n1) - ni ** 2 / np.exp(ln)
    return np.exp(brentq(f, np.log(1e-30 + 1e-5), np.log(1e22)))


def n_vs_T():
    fig, ax = new_fig(6.4, 4.2)
    x = np.linspace(1, 20, 800)
    T = 1000 / x
    ax.semilogy(x, ni_si(T), "--", color="0.4", lw=1.2)
    for ND, c in [(1e14, COLORS[2]), (1e15, COLORS[1]), (1e16, COLORS[0])]:
        n = np.array([n_of_T(ND, t) for t in T])
        ax.semilogy(x, n, color=c)
        ax.text(6.2, ND * 1.25, rf"$N_D=10^{{{int(np.log10(ND))}}}$", fontsize=8.5, color=c, va="bottom")
        if ND == 1e15:
            Tdep = brentq(lambda t: n_of_T(ND, t) / ND - 1.10, 350, 900)
            print(f"  ND=1e15: n = 1.1 ND at {Tdep:.0f} K")
        if ND == 1e16:
            print(f"  ND=1e16: n/ND at 77 K = {n_of_T(ND, 77.0)/ND:.2f}")
    n77 = n_of_T(1e16, 77.0)
    ax.plot(1000 / 77, n77, "o", ms=4, color=COLORS[0])
    ax.text(1000 / 77 + 0.3, n77 * 0.55, f"{n77/1e16*100:.0f} % ionized at 77 K", fontsize=8,
            color=COLORS[0], va="top")
    for Tm, lab in [(300, "300 K"), (77, "77 K")]:
        ax.axvline(1000 / Tm, color="0.55", ls=":", lw=0.9)
    ax.text(1.4, 2e17, r"$n_i(T)$", fontsize=9, color="0.35")
    ax.text(1.25, 1e12, "intrinsic", fontsize=9, color="0.3", ha="center", rotation=90)
    ax.text(5.5, 3e11, "extrinsic (saturation)\n$n\\approx N_D$", fontsize=9, color="0.3", ha="center")
    ax.text(16.0, 3e11, "freeze-out\nslope $-E_d/2k_B$", fontsize=9, color="0.3", ha="center")
    ax.set_xlim(1, 20); ax.set_ylim(1e10, 1e18)
    ax.set_xlabel(r"$1000/T$ (K$^{-1}$)"); ax.set_ylabel(r"electron concentration $n$ (cm$^{-3}$)")
    top = ax.secondary_xaxis("top", functions=(lambda v: v, lambda v: v))
    Ts = np.array([500, 300, 200, 100, 77, 50])
    top.set_xticks(1000 / Ts); top.set_xticklabels([str(t) for t in Ts])
    top.set_xlabel("temperature (K)")
    save(fig, "32", "fig-32-5-n-vs-temperature")


# ---------------------------------------------------------------- Figure 32.6
def v_ct(E, mu, vs, beta):
    return mu * E / (1 + (mu * E / vs) ** beta) ** (1 / beta)


def v_ted(E, mu, vp, b, vs, E0, n):
    """Transferred-electron form: Caughey-Thomas Gamma-valley velocity blended to the satellite-valley vsat."""
    r = (E / E0) ** n
    return (v_ct(E, mu, vp, b) + vs * r) / (1 + r)


def velocity_field():
    fig, ax = new_fig(6.4, 4.2)
    E = np.logspace(2, 6, 1500)
    cur = {
        "Si electrons": (v_ct(E, 1400, 1.0e7, 2), COLORS[0], "-"),
        "Si holes": (v_ct(E, 450, 8e6, 1), COLORS[0], "--"),
        "GaAs": (v_ted(E, 8500, 1e9, 2, 1.0e7, 3.6e3, 4), COLORS[1], "-"),
        "InP": (v_ted(E, 5000, 3.5e7, 2, 1.0e7, 1.6e4, 3), COLORS[3], "-"),
        "4H-SiC": (v_ct(E, 950, 2.0e7, 1.5), COLORS[2], "-"),
        "GaN": (v_ted(E, 1000, 3.4e7, 1.0, 1.7e7, 3.2e5, 3), COLORS[4], "-"),
    }
    for name, (v, c, ls) in cur.items():
        ax.plot(E, v / 1e7, color=c, ls=ls, label=name)
        i = np.argmax(v)
        print(f"  {name}: peak {v[i]:.3g} cm/s at {E[i]/1e3:.3g} kV/cm; v(1e6) = {v[-1]:.3g}")
    vg = cur["GaAs"][0]
    ip = np.argmax(vg)
    ax.axvspan(E[ip], 2e4, color=COLORS[1], alpha=0.12, lw=0)
    ax.text(np.sqrt(E[ip] * 2e4), 3.05, "GaAs\nNDM", ha="center", fontsize=8.5, color=COLORS[1], va="top")
    ax.set_xscale("log"); ax.set_xlim(1e2, 1e6); ax.set_ylim(0, 3.2)
    ax.set_xlabel(r"electric field $\mathcal{E}$ (V/cm)")
    ax.set_ylabel(r"drift velocity ($10^7$ cm/s)")
    ax.legend(loc="upper left", fontsize=8.5)
    save(fig, "32", "fig-32-6-velocity-field")


if __name__ == "__main__":
    dopant_levels()
    doping_profiles()
    mobility()
    lifetime()
    n_vs_T()
    velocity_field()
