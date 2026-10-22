"""Figures for Chapter 33 — Semiconductor Material Families.

Run from the repository root:  python figures/scripts/ch33.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Ellipse

# ---------------------------------------------------------------- Figure 33.1
# binary: lattice constant (A), Gamma, X, L gaps (eV, 300 K, approximate)
BIN = {
    "GaAs": (5.653, 1.42, 1.90, 1.71), "AlAs": (5.661, 3.00, 2.16, 2.35), "InAs": (6.058, 0.35, 1.37, 1.08),
    "GaP": (5.451, 2.78, 2.26, 2.60), "AlP": (5.464, 3.60, 2.45, 3.30), "InP": (5.869, 1.34, 2.19, 1.93),
    "GaSb": (6.096, 0.73, 1.03, 0.76), "InSb": (6.479, 0.17, 1.63, 0.93), "AlSb": (6.136, 2.30, 1.60, 2.21),
}
# alloy: (A, B, bowing Gamma, X, L) — gap(x) = x*E_A + (1-x)*E_B - b x (1-x)
ALLOYS = [("AlAs", "GaAs", 0.37, 0.06, 0.06), ("GaAs", "InAs", 0.477, 1.4, 0.33), ("InP", "InAs", 0.10, 0.27, 0.27),
          ("GaAs", "GaP", 0.19, 0.24, 0.16), ("InP", "GaP", 0.65, 0.20, 1.03), ("GaSb", "InAs", 0.75, 0.6, 0.6),
          ("InSb", "InAs", 0.67, 0.6, 0.55)]
EV_UM = 1.23984


def bandgap_map():
    fig = plt.figure(figsize=(6.8, 4.6))
    ax = fig.add_axes([0.09, 0.11, 0.56, 0.80])
    ax2 = fig.add_axes([0.82, 0.11, 0.16, 0.80])
    for a0, lab, col in [(5.653, "GaAs / Ge substrate", COLORS[1]), (5.869, "InP substrate", COLORS[3])]:
        ax.axvspan(a0 - 0.008, a0 + 0.008, color=col, alpha=0.18, lw=0)
    ax.axvline(5.431, color="0.6", lw=0.8, ls=":")
    x = np.linspace(0, 1, 300)
    for A, B, bG, bX, bL in ALLOYS:
        aA, gA, xA, lA = BIN[A]; aB, gB, xB, lB = BIN[B]
        a = x * aA + (1 - x) * aB
        EG = x * gA + (1 - x) * gB - bG * x * (1 - x)
        EX = x * xA + (1 - x) * xB - bX * x * (1 - x)
        EL = x * lA + (1 - x) * lB - bL * x * (1 - x)
        E = np.minimum(EG, np.minimum(EX, EL))
        direct = EG <= np.minimum(EX, EL)
        Ed = np.where(direct, E, np.nan); Ei = np.where(~direct, E, np.nan)
        # make segments touch at the crossover
        idx = np.where(np.diff(direct.astype(int)) != 0)[0]
        for i in idx:
            Ei[i] = E[i]; Ei[i + 1] = E[i + 1]
        ax.plot(a, Ed, color=INK, lw=1.3)
        ax.plot(a, Ei, color=INK, lw=1.1, ls="--")
    pts = {"Si": (5.431, 1.12, False), "Ge": (5.658, 0.66, False)}
    for k, (a0, g, xg, lg) in BIN.items():
        pts[k] = (a0, min(g, xg, lg), g <= min(xg, lg))
    off = {"Si": (-6, 4, "right"), "Ge": (6, -10, "left"), "GaP": (-6, 4, "right"), "AlP": (6, 4, "left"),
           "AlAs": (6, 3, "left"), "GaAs": (-6, 4, "right"), "InP": (6, 3, "left"), "AlSb": (6, 2, "left"),
           "GaSb": (6, 2, "left"), "InAs": (-6, -10, "right"), "InSb": (-6, 4, "right")}
    for k, (a0, g, d) in pts.items():
        col = COLORS[0] if k in ("Si", "Ge") else COLORS[1] if k in ("GaAs", "AlAs") else INK
        ax.plot(a0, g, "o", ms=7, mfc=col if d else "white", mec=col, mew=1.5, zorder=5)
        dx, dy, ha = off[k]
        ax.annotate(k, (a0, g), xytext=(dx, dy), textcoords="offset points", fontsize=8.5, ha=ha, color=col)
    ax.text(5.661, 2.58, "AlGaAs,\nInGaP", fontsize=8, color=COLORS[1], ha="center", va="top")
    ax.text(5.875, 2.58, "In$_{0.53}$Ga$_{0.47}$As,\nInGaAsP\n(1.3, 1.55 µm)", fontsize=8, color=COLORS[3],
            ha="left", va="top")
    ax.set_xlim(5.4, 6.5); ax.set_ylim(0, 2.6)
    ax.set_xlabel("lattice constant (Å)"); ax.set_ylabel("band gap (eV)")
    sec = ax.secondary_yaxis("right", functions=(lambda e: EV_UM / np.clip(e, 1e-3, None),
                                                 lambda l: EV_UM / np.clip(l, 1e-3, None)))
    wl = [0.5, 0.6, 0.8, 1.0, 1.55, 3, 5]
    sec.set_yticks(wl); sec.set_yticklabels([str(w) for w in wl])
    sec.set_ylabel("wavelength (µm)")
    ax.spines["right"].set_visible(True)
    from matplotlib.lines import Line2D
    h = [Line2D([], [], marker="o", ls="", mfc="0.3", mec="0.3", label="direct"),
         Line2D([], [], marker="o", ls="", mfc="white", mec="0.3", label="indirect"),
         Line2D([], [], color=INK, label="alloy, direct"), Line2D([], [], color=INK, ls="--", label="alloy, indirect")]
    ax.legend(handles=h, loc="upper right", fontsize=7.5, frameon=True, framealpha=0.9, edgecolor="none")

    # nitrides panel
    nit = {"AlN": (3.112, 6.10), "GaN": (3.189, 3.40), "InN": (3.545, 0.70)}
    for (A, B, b) in [("AlN", "GaN", 0.8), ("GaN", "InN", 1.4), ("AlN", "InN", 3.0)]:
        aA, gA = nit[A]; aB, gB = nit[B]
        a = x * aA + (1 - x) * aB; g = x * gA + (1 - x) * gB - b * x * (1 - x)
        ax2.plot(a, g, color=INK, lw=1.2, ls="-" if b < 2 else ":")
    for k, (a0, g) in nit.items():
        ax2.plot(a0, g, "o", ms=7, color=COLORS[2], zorder=5)
        ax2.annotate(k, (a0, g), xytext=(6, 0), textcoords="offset points", fontsize=8.5, va="center")
    ax2.set_xlim(3.05, 3.65); ax2.set_ylim(0, 6.6)
    ax2.set_xticks([3.1, 3.3, 3.5])
    ax2.set_xlabel("a (Å)"); ax2.set_ylabel("band gap (eV)", labelpad=1)
    ax2.set_title("wurtzite\nnitrides", fontsize=9)
    save(fig, "33", "fig-33-1-bandgap-vs-lattice-constant")


# ---------------------------------------------------------------- Figure 33.2
def sic_polytypes():
    a = 3.08
    per = a * np.sqrt(3)          # lateral repeat in the [1-100] direction (projection along [11-20])
    off = {"A": 0.0, "B": per / 3, "C": 2 * per / 3}
    dz = 2.52                     # bilayer spacing (A)
    dsc = 0.63                    # Si above C within a bilayer
    poly = [("3C", "ABC", 2.36, 900, None), ("4H", "ABCB", 3.26, 950, 10.05), ("6H", "ABCACB", 3.02, 400, 15.12)]
    nb = 12
    fig, ax = plt.subplots(figsize=(6.8, 5.2))
    width = 1.6 * per
    gap = 12.5
    for j, (name, seq, eg, mu, c) in enumerate(poly):
        x0 = 4.0 + j * (width + gap)
        layers = [seq[i % len(seq)] for i in range(nb)]
        # site labels h/k
        sites = []
        for i in range(nb):
            prv = seq[(i - 1) % len(seq)]; nxt = seq[(i + 1) % len(seq)]
            sites.append("h" if prv == nxt else "k")
        if name == "6H":
            sites = [("k1" if sites[(i - 1) % nb] == "h" else "k2") if s == "k" else s for i, s in enumerate(sites)]
        atoms = []
        for i, L in enumerate(layers):
            zc = i * dz; zs = zc + dsc
            xs = [x0 + off[L] + m * per for m in range(-2, 4)]
            xs = [x for x in xs if x0 - 0.1 <= x <= x0 + width + 0.1]
            for x in xs:
                ax.plot([x, x], [zc, zs], color="0.35", lw=1.4, zorder=1)
                atoms.append((x, zs, "Si")); atoms.append((x, zc, "C"))
            if i + 1 < nb:
                Lu = layers[i + 1]
                xcu = [x0 + off[Lu] + m * per for m in range(-2, 4)]
                # the C atom of the upper bilayer sits directly above one of this layer's Si (shifted by per/3)
                for xc in [x for x in xcu if x0 - 0.1 <= x <= x0 + width + 0.1]:
                    cand = [xsl for xsl in xs if abs(abs(xc - xsl) - per / 3) < 0.05 or abs(abs(xc - xsl) - 2 * per / 3) < 0.05]
                    if cand:
                        xsl = min(cand, key=lambda q: abs(q - xc))
                        ax.plot([xc, xsl], [zc + dz, zs], color="0.35", lw=1.4, zorder=1)
            ax.text(x0 - 1.4, zc + dsc / 2, L, ha="right", va="center", fontsize=9, fontweight="bold")
            ax.text(x0 + width + 1.2, zc + dsc / 2, sites[i], ha="left", va="center", fontsize=8.5,
                    color=COLORS[1] if sites[i] == "h" else COLORS[0])
        for x, z, kind in atoms:
            if kind == "Si":
                ax.add_patch(Circle((x, z), 0.62, fc="#D9E6F2", ec=INK, lw=0.8, zorder=3))
            else:
                ax.add_patch(Circle((x, z), 0.36, fc="#333333", ec=INK, lw=0.6, zorder=4))
        rep = len(seq)
        top = rep * dz
        xb = x0 + width + 4.2
        ax.annotate("", xy=(xb, top - 0.0 + dsc / 2), xytext=(xb, dsc / 2),
                    arrowprops=dict(arrowstyle="|-|", lw=0.9, color=INK, mutation_scale=4, shrinkA=0, shrinkB=0))
        lab = f"c = {c:.2f} Å" if c else f"repeat {rep * dz:.2f} Å"
        ax.text(xb + 0.4, top / 2 + dsc / 2, lab, rotation=90, ha="left", va="center", fontsize=8)
        ax.text(x0 + width / 2, nb * dz + 1.9, f"{name}", ha="center", fontsize=11, fontweight="bold")
        ax.text(x0 + width / 2, nb * dz + 0.2, seq + "…", ha="center", fontsize=8.5, color="0.3")
        ax.text(x0 + width / 2, -2.2, f"$E_g$ = {eg:.2f} eV\n$\\mu_n$ ≈ {mu} cm$^2$/V s", ha="center",
                va="top", fontsize=8.5)
    ax.annotate("", xy=(0.3, 12), xytext=(0.3, 2), arrowprops=dict(arrowstyle="-|>", lw=1.3, color=INK))
    ax.text(-0.3, 7, "c axis [0001]", rotation=90, ha="right", va="center", fontsize=9)
    ax.add_patch(Circle((2.0, -8.6), 0.62, fc="#D9E6F2", ec=INK, lw=0.8))
    ax.text(3.0, -8.6, "Si", va="center", fontsize=8.5)
    ax.add_patch(Circle((5.5, -8.6), 0.36, fc="#333333", ec=INK, lw=0.6))
    ax.text(6.3, -8.6, "C", va="center", fontsize=8.5)
    ax.text(8.5, -8.6, "h = hexagonal site, k = cubic site;  view along [11$\\bar{2}$0]", va="center", fontsize=8.5)
    ax.set_xlim(-2.0, 4.0 + 3 * width + 2 * gap + 6.5)
    ax.set_ylim(-9.6, nb * dz + 3.6)
    ax.set_aspect("equal"); ax.axis("off")
    save(fig, "33", "fig-33-2-sic-polytypes")


# ---------------------------------------------------------------- Figure 33.3
def algan_gan():
    fig, ax = new_fig(6.4, 4.2)
    d = 20.0
    xb = np.linspace(0, d, 200)
    Ec0, Eci_b = 1.6, 0.05          # AlGaN surface and interface (barrier side) conduction band
    Ecb = Ec0 + (Eci_b - Ec0) * xb / d
    dEc = 0.40
    Ew = Eci_b - dEc                # bottom of the well on the GaN side (-0.35 eV)
    xg = np.linspace(d, 60, 600)
    V0, L = 0.95, (0.95 / 0.20)     # slope at interface ~0.2 eV/nm  (q ns / eps for ns = 1e13 cm^-2)
    Ecg = Ew + V0 * (1 - np.exp(-(xg - d) / L))
    ax.axvspan(0, d, color="#E9E1F3", lw=0)
    ax.plot(xb, Ecb, color=COLORS[0], lw=2)
    ax.plot([d, d], [Eci_b, Ew], color=COLORS[0], lw=2)
    ax.plot(xg, Ecg, color=COLORS[0], lw=2)
    ax.axhline(0, color=INK, ls="--", lw=1.0)
    ax.text(59, 0.04, "$E_F$", ha="right", va="bottom", fontsize=10)
    E0 = -0.10
    xr = d + -L * np.log(1 - (E0 - Ew) / V0)
    ax.plot([d, xr], [E0, E0], color=COLORS[2], lw=1.3)
    ax.annotate("$E_0$", xy=(xr, E0), xytext=(27.5, -0.12), color=COLORS[2], fontsize=9, va="center",
                arrowprops=dict(arrowstyle="-", lw=0.6, color=COLORS[2]))
    # Fang-Howard density with peak 2 nm from the interface
    z = np.linspace(0, 9, 300); b = 1.0
    psi2 = (b ** 3 / 2) * z ** 2 * np.exp(-b * z)
    ax.fill_between(d + z, E0, E0 - 0.9 * psi2 / psi2.max() * 0.5, color=COLORS[2], alpha=0.35, lw=0)
    ax.annotate("2DEG, $n_s\\approx10^{13}$ cm$^{-2}$\n$\\mu\\approx$ 1500–2000 cm$^2$/V s\npeak ≈ 2 nm from interface",
                xy=(d + 2.5, E0 - 0.3), xytext=(31, -0.31), fontsize=8.5, color=COLORS[2], va="center",
                arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[2]))
    ax.annotate("", xy=(d + 0.6, Eci_b), xytext=(d + 0.6, Ew),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, color=INK, mutation_scale=7, shrinkA=0, shrinkB=0))
    ax.text(18.4, -0.17, r"$\Delta E_c\approx0.4$ eV", fontsize=8.5, va="center", ha="right")
    # polarization charge at interface
    for yy in np.linspace(-0.3, 0.75, 6):
        ax.text(d - 0.55, yy, "+", color=COLORS[1], fontsize=11, ha="center", va="center", fontweight="bold")
    ax.annotate(r"$\sigma_{\mathrm{pol}}\approx+10^{13}\,q$ cm$^{-2}$", xy=(d - 0.6, 0.85), xytext=(12.5, 1.45),
                fontsize=8.5, color=COLORS[1], ha="center", arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[1]))
    # surface donors
    for yy in np.linspace(1.35, 1.75, 3):
        ax.plot([-1.6, -0.2], [yy, yy], color=COLORS[3], lw=1.6)
        ax.text(-2.1, yy, "+", color=COLORS[3], ha="center", va="center", fontsize=8)
    ax.text(0.5, 1.95, "ionized surface donors", fontsize=8.5, color=COLORS[3], ha="left")
    # polarization arrows
    for (x0, lab, yy) in [(4, r"$P_{\mathrm{sp}}$", -0.45), (4, r"$P_{\mathrm{pz}}$", -0.75)]:
        ax.annotate("", xy=(x0 + 7, yy), xytext=(x0, yy), arrowprops=dict(arrowstyle="-|>", lw=1.3, color="0.3"))
        ax.text(x0 + 3.5, yy + 0.05, lab, ha="center", va="bottom", fontsize=9)
    ax.annotate("", xy=(52, -0.82), xytext=(45, -0.82), arrowprops=dict(arrowstyle="-|>", lw=1.3, color="0.3"))
    ax.text(48.5, -0.77, r"$P_{\mathrm{sp}}$ (GaN)", ha="center", va="bottom", fontsize=9)
    ax.text(d / 2, 2.25, "Al$_{0.25}$Ga$_{0.75}$N barrier", ha="center", fontsize=9)
    ax.text(40, 2.25, "GaN channel / buffer", ha="center", fontsize=9)
    ax.text(10.5, 0.95, "$E_c$", color=COLORS[0], fontsize=10)
    ax.set_xlim(-3, 60); ax.set_ylim(-0.95, 2.45)
    ax.set_xlabel("depth from surface (nm)"); ax.set_ylabel("electron energy (eV, relative to $E_F$)")
    save(fig, "33", "fig-33-3-algan-gan-2deg")


# ---------------------------------------------------------------- Figure 33.4
def asi_dos():
    fig, ax = new_fig(6.4, 4.2)
    Ev, Ec = 0.5, 2.25
    E = np.linspace(0, 2.75, 3000)
    G0 = 2e21
    gv_ext = np.where(E <= Ev, G0 * np.sqrt(1 + (Ev - E) / 0.05), np.nan)
    gc_ext = np.where(E >= Ec, G0 * np.sqrt(1 + (E - Ec) / 0.05), np.nan)
    gv_t = np.where(E >= Ev, G0 * np.exp(-(E - Ev) / 0.045), np.nan)
    gc_t = np.where(E <= Ec, G0 * np.exp(-(Ec - E) / 0.025), np.nan)
    gauss = lambda Etot, mu, s: Etot / (s * np.sqrt(2 * np.pi)) * np.exp(-(E - mu) ** 2 / (2 * s ** 2))
    db = gauss(5e15, 1.25, 0.10) + gauss(5e15, 1.55, 0.10)
    db_u = gauss(5e18, 1.25, 0.15) + gauss(5e18, 1.55, 0.15)
    loc = np.nansum(np.vstack([np.nan_to_num(gv_t), np.nan_to_num(gc_t), db]), axis=0)
    loc = np.where((E > Ev) & (E < Ec), loc, np.nan)
    lo = 1e15
    ax.fill_between(E, lo, np.nan_to_num(gv_ext, nan=lo), where=E <= Ev, color=COLORS[0], alpha=0.30, lw=0)
    ax.fill_between(E, lo, np.nan_to_num(gc_ext, nan=lo), where=E >= Ec, color=COLORS[0], alpha=0.30, lw=0)
    ax.fill_between(E, lo, np.clip(np.nan_to_num(loc, nan=lo), lo, None), where=(E > Ev) & (E < Ec),
                    color=COLORS[1], alpha=0.25, lw=0)
    ax.semilogy(E, gv_ext, color=COLORS[0]); ax.semilogy(E, gc_ext, color=COLORS[0])
    ax.semilogy(E, loc, color=COLORS[1])
    ax.semilogy(E, np.where((E > 0.8) & (E < 2.0), db_u, np.nan), "--", color=COLORS[3], lw=1.4)
    for x in (Ev, Ec):
        ax.axvline(x, color=INK, ls="--", lw=0.9)
    ax.text(Ev - 0.03, 2e15, "$E_v$ (mobility\nedge)", ha="right", fontsize=8.5)
    ax.text(Ec + 0.03, 2e15, "$E_c$ (mobility\nedge)", ha="left", fontsize=8.5)
    ax.annotate("", xy=(Ev, 4e21), xytext=(Ec, 4e21),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.9, color=INK, mutation_scale=8, shrinkA=0, shrinkB=0))
    ax.text((Ev + Ec) / 2, 5e21, "mobility gap ≈ 1.75 eV", ha="center", va="bottom", fontsize=9)
    ax.text(0.54, 2e16, "valence tail\n$E_0$ = 45 meV", fontsize=8, color=COLORS[1])
    ax.text(2.07, 2e19, "conduction\ntail\n$E_0$ = 25 meV", fontsize=8.5, color=COLORS[1], ha="right")
    ax.text(1.40, 5e16, "dangling bonds\n(a-Si:H, $10^{16}$ cm$^{-3}$)", fontsize=8.5, color=COLORS[1], ha="center")
    ax.text(1.40, 6e18, "unhydrogenated a-Si\n($10^{19}$ cm$^{-3}$)", fontsize=8.5, color=COLORS[3], ha="center", va="top")
    ax.text(0.05, 6e18, "extended\nstates", fontsize=8.5, color=COLORS[0])
    ax.text(2.70, 6e18, "extended\nstates", fontsize=8.5, color=COLORS[0], ha="right")
    ax.text(1.40, 2.5e15, "localized states", fontsize=8.5, color=COLORS[1], ha="center")
    ax.set_xlim(0, 2.75); ax.set_ylim(1e15, 1e22)
    ax.set_xlabel("energy (eV)"); ax.set_ylabel(r"density of states (cm$^{-3}$ eV$^{-1}$)")
    # inset: crystalline Si
    ia = ax.inset_axes([0.33, 0.67, 0.22, 0.20])
    e = np.linspace(-0.6, 1.8, 400)
    g = np.where(e < 0, np.sqrt(np.clip(-e, 0, None)), np.where(e > 1.12, np.sqrt(np.clip(e - 1.12, 0, None)), 0))
    ia.fill_between(e, 0, g, color=COLORS[0], alpha=0.35, lw=0); ia.plot(e, g, color=COLORS[0], lw=1)
    ia.set_xticks([]); ia.set_yticks([]); ia.set_title("c-Si: sharp gap", fontsize=7.5, pad=2)
    ia.text(0.56, 0.35, "1.12 eV", ha="center", fontsize=7)
    save(fig, "33", "fig-33-4-asi-density-of-states")


# ---------------------------------------------------------------- Figure 33.5
MAT = {  # eps_r, mu (cm2/Vs), Ec (V/cm)
    "Si": (11.7, 1400, 3e5), "GaAs": (12.9, 8500, 4e5), "4H-SiC": (9.7, 950, 2.5e6),
    "GaN": (9.0, 1250, 3.3e6), r"$\beta$-Ga$_2$O$_3$": (10, 200, 8e6), "diamond": (5.7, 2000, 1e7),
}


def ron(V, eps, mu, Ec):
    return 4 * V ** 2 / (eps * 8.854e-14 * mu * Ec ** 3) * 1e3  # mOhm cm^2


def log_ellipse(ax, xc, yc, wx, wy, **kw):
    t = np.linspace(0, 2 * np.pi, 100)
    lx = np.log10(xc) + wx * np.cos(t); ly = np.log10(yc) + wy * np.sin(t)
    ax.add_patch(Polygon(np.c_[10 ** lx, 10 ** ly], closed=True, **kw))


def unipolar():
    fig, ax = new_fig(6.4, 4.4)
    V = np.logspace(2, np.log10(2e4), 200)
    cols = [COLORS[0], COLORS[5], COLORS[2], COLORS[1], COLORS[3], INK]
    for (name, p), c in zip(MAT.items(), cols):
        r = ron(V, *p)
        ax.loglog(V, r, color=c, lw=1.6)
        print(f"  {name}: {ron(1200, *p):.3g} mOhm cm2 at 1200 V")
        # label at the left/top edge inside the axes
        r_end = ron(2e4, *p)
        xt = np.sqrt(1e3 / ron(1, *p))
        ax.text(2.15e4, r_end, name, color=c, fontsize=8.5, va="center", clip_on=False) if r_end < 1e3 else ax.text(xt, 1.15e3, name, color=c, fontsize=8.5, ha="center", va="bottom", clip_on=False)
    log_ellipse(ax, 750, 14, 0.09, 0.17, fc=COLORS[0], alpha=0.25, ec=COLORS[0])
    ax.annotate("Si superjunction MOSFETs\n(beat the 1-D Si limit)", xy=(750, 14), xytext=(112, 150),
                fontsize=8, color=COLORS[0], arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[0]))
    log_ellipse(ax, 1460, 3.2, 0.36, 0.5, fc=COLORS[2], alpha=0.22, ec=COLORS[2])
    ax.text(900, 0.75, "SiC MOSFETs", fontsize=8, color=COLORS[2])
    log_ellipse(ax, 255, 1.6, 0.4, 0.5, fc=COLORS[1], alpha=0.22, ec=COLORS[1])
    ax.text(108, 0.33, "GaN HEMTs", fontsize=8, color=COLORS[1])
    for v in (650, 1200, 3300):
        ax.axvline(v, color="0.55", ls=":", lw=0.9)
        ax.text(v * 1.04, 5e2, f"{v} V", fontsize=8, color="0.35", rotation=90, va="top")
    ax.set_xlim(100, 2e4); ax.set_ylim(1e-3, 1e3)
    ax.set_xlabel("breakdown voltage $V_B$ (V)")
    ax.set_ylabel(r"specific on-resistance $R_{\mathrm{on,sp}}$ (m$\Omega$ cm$^2$)")
    ax.text(1.9e4, 1.4e-3, r"$R_{\mathrm{on,sp}}=4V_B^2/(\varepsilon\mu_n\mathcal{E}_c^3)$", fontsize=9,
            ha="right", va="bottom")
    save(fig, "33", "fig-33-5-unipolar-limits")


# ---------------------------------------------------------------- Figure 33.6
def fom_map():
    fig, ax = new_fig(6.4, 4.4)
    data = [  # name, BFOM, JFOM, kappa (W/mK), maturity
        ("Ge", 0.14, 0.2, 60, 0), ("Si", 1, 1, 148, 0), ("GaAs", 16, 1.3, 55, 0), ("InP", 19, 1.7, 68, 0),
        ("4H-SiC", 330, 17, 370, 1), ("GaN", 910, 28, 180, 1), (r"$\beta$-Ga$_2$O$_3$", 2300, 29, 20, 2),
        ("diamond", 26000, 90, 2000, 2)]
    mcol = [COLORS[0], COLORS[2], COLORS[1]]
    mlab = ["mature", "in production", "emerging"]
    lab_pos = {"Ge": (0.2, 0.2, "left"), "Si": (1.45, 0.92, "left"), "GaAs": (12, 1.3, "right"),
               "InP": (25, 1.85, "left"), "4H-SiC": (220, 17, "right"), "GaN": (1350, 25, "left"),
               r"$\beta$-Ga$_2$O$_3$": (2300, 42, "center"), "diamond": (26000, 48, "center")}
    for n, b, j, k, m in data:
        ax.scatter(b, j, s=k * 0.35, color=mcol[m], alpha=0.55, edgecolor=mcol[m], lw=1.0, zorder=3)
        x, y, ha = lab_pos[n]
        ax.text(x, y, n, fontsize=8.5, ha=ha, va="top" if n == "diamond" else "center")
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlim(0.1, 1e5); ax.set_ylim(0.1, 200)
    ax.set_xlabel("Baliga figure of merit, BFOM (relative to Si)")
    ax.set_ylabel("Johnson figure of merit, JFOM (relative to Si)")
    ax.annotate("", xy=(800, 0.14), xytext=(8, 0.14), arrowprops=dict(arrowstyle="-|>", lw=1.3, color="0.4"))
    ax.text(80, 0.155, "better for power switching", ha="center", va="bottom", fontsize=8.5, color="0.3")
    ax.annotate("", xy=(0.17, 40), xytext=(0.17, 2), arrowprops=dict(arrowstyle="-|>", lw=1.3, color="0.4"))
    ax.text(0.2, 9, "better for\nRF power", ha="left", va="center", fontsize=8.5, color="0.3")
    from matplotlib.lines import Line2D
    h = [Line2D([], [], marker="o", ls="", color=c, alpha=0.6, ms=8, label=l) for c, l in zip(mcol, mlab)]
    leg1 = ax.legend(handles=h, loc="upper left", fontsize=8, title="maturity", title_fontsize=8)
    ax.add_artist(leg1)
    hs = [ax.scatter([], [], s=k * 0.35, color="0.6", alpha=0.5, label=f"{k} W/m K") for k in (20, 200, 2000)]
    ax.legend(handles=hs, loc="lower right", fontsize=8, title="thermal conductivity", title_fontsize=8,
              labelspacing=1.3, borderpad=1.0)
    save(fig, "33", "fig-33-6-fom-map")


if __name__ == "__main__":
    bandgap_map()
    sic_polytypes()
    algan_gan()
    asi_dos()
    unipolar()
    fom_map()
