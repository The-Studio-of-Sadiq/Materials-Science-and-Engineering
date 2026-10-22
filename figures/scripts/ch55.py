"""Figures for Chapter 55 — Density Functional Theory for Materials.

Run from the repository root:  python figures/scripts/ch55.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, schematic, box, arrow, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, FancyBboxPatch
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import brentq, curve_fit


def _diamond(ax, xc, yc, w, h, text, fc="#FFF4D6", fontsize=8.5):
    ax.add_patch(Polygon([[xc - w / 2, yc], [xc, yc + h / 2], [xc + w / 2, yc], [xc, yc - h / 2]],
                         closed=True, fc=fc, ec=INK, lw=1.0))
    ax.text(xc, yc, text, ha="center", va="center", fontsize=fontsize)


def _poly(ax, pts, text="", tx=None, ty=None, color=INK, ls="-", fontsize=8, ha="center", va="bottom"):
    xs, ys = zip(*pts)
    ax.plot(xs[:-1], ys[:-1], color=color, lw=1.1, ls=ls)
    ax.annotate("", xy=pts[-1], xytext=pts[-2],
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.1, ls=ls, shrinkA=0, shrinkB=0,
                                mutation_scale=10))
    if text:
        ax.text(tx, ty, text, ha=ha, va=va, fontsize=fontsize, color=color)


# ---------------------------------------------------------------- Figure 55.1
def kohn_sham_scf_loop():
    fig, ax = schematic(6.6, 5.0, xlim=(0, 13.2), ylim=(0, 10))
    xc, bw, bh = 6.3, 7.1, 0.78
    ax.add_patch(FancyBboxPatch((1.3, 3.85), 9.4, 4.95, boxstyle="round,pad=0.05,rounding_size=0.3",
                                fc="#EAF2FA", ec="none", zorder=0))
    ax.text(10.6, 3.95, "electronic\n(inner) loop", ha="right", va="bottom", fontsize=8.5,
            color=COLORS[0], style="italic")
    rows = {"n0": 9.45, "veff": 8.25, "ks": 7.05, "dens": 5.85, "conv": 4.55, "force": 3.15,
            "fconv": 1.85, "done": 0.45}
    box(ax, xc - bw / 2, rows["n0"] - bh / 2, bw, bh,
        "Initial density $n_0(\\mathbf{r})$ (sum of atomic densities)", fc="#F2F2F2", fontsize=8.2)
    box(ax, xc - bw / 2, rows["veff"] - bh / 2, bw, bh,
        "Build $V_{eff}=V_{ext}+V_H[n]+V_{xc}[n]$", fontsize=8.2)
    box(ax, xc - bw / 2, rows["ks"] - bh / 2, bw, bh,
        "Solve KS equations for $\\psi_i,\\ \\varepsilon_i$ at each k-point", fontsize=8.2)
    box(ax, xc - bw / 2, rows["dens"] - bh / 2, bw, bh,
        "New density $n(\\mathbf{r})=\\sum_i f_i\\,|\\psi_i|^2$", fontsize=8.2)
    _diamond(ax, xc, rows["conv"], 4.4, 1.2, "Converged?\n$\\Delta E<10^{-6}$ eV", fontsize=8.2)
    box(ax, xc - bw / 2, rows["force"] - bh / 2, bw, bh,
        "Energy, forces (Hellmann–Feynman), stress", fc="#E8F4EE", fontsize=8.2)
    _diamond(ax, xc, rows["fconv"], 4.4, 1.2, "Forces < 0.01 eV/Å?", fontsize=8.2)
    box(ax, xc - bw / 2, rows["done"] - bh / 2, bw, bh, "Relaxed structure and properties",
        fc="#DDEEDD", fontsize=8.2)
    # straight-down arrows
    for a, b in [("n0", "veff"), ("veff", "ks"), ("ks", "dens")]:
        arrow(ax, xc, rows[a] - bh / 2, xc, rows[b] + bh / 2)
    arrow(ax, xc, rows["dens"] - bh / 2, xc, rows["conv"] + 0.6)
    arrow(ax, xc, rows["conv"] - 0.6, xc, rows["force"] + bh / 2)
    ax.text(xc + 0.15, (rows["conv"] - 0.6 + rows["force"] + bh / 2) / 2, "yes", fontsize=8,
            va="center")
    arrow(ax, xc, rows["force"] - bh / 2, xc, rows["fconv"] + 0.6)
    arrow(ax, xc, rows["fconv"] - 0.6, xc, rows["done"] + bh / 2)
    ax.text(xc + 0.15, (rows["fconv"] - 0.6 + rows["done"] + bh / 2) / 2, "yes", fontsize=8,
            va="center")
    # inner loop: no -> mix -> back to Veff
    xl = 2.15
    _poly(ax, [(xc - 2.2, rows["conv"]), (xl, rows["conv"]), (xl, rows["veff"]),
               (xc - bw / 2, rows["veff"])], color=COLORS[0])
    ax.text(xl + 0.12, rows["conv"] + 0.12, "no", fontsize=8, color=COLORS[0], va="bottom")
    ax.text(xl - 0.15, (rows["conv"] + rows["veff"]) / 2, "mix densities\n(Pulay / Broyden)",
            fontsize=8, color=COLORS[0], rotation=90, ha="right", va="center")
    # outer loop: no -> move atoms -> back to start
    xr = 11.0
    _poly(ax, [(xc + 2.2, rows["fconv"]), (xr, rows["fconv"]), (xr, rows["n0"]),
               (xc + bw / 2, rows["n0"])], color=COLORS[1])
    ax.text(xc + 2.35, rows["fconv"] + 0.12, "no", fontsize=8, color=COLORS[1], va="bottom")
    ax.text(xr + 0.15, 3.0, "move atoms / cell", fontsize=8, color=COLORS[1], rotation=90,
            ha="left", va="center")
    ax.text(11.25, 6.3, "ionic\n(outer)\nloop", ha="left", va="center", fontsize=8.5,
            color=COLORS[1], style="italic")
    save(fig, "55", "fig-55-1-kohn-sham-scf-loop")


# ---------------------------------------------------------------- Figure 55.2
def jacobs_ladder():
    fig, ax = schematic(6.7, 4.9, xlim=(0, 13.6), ylim=(0, 9.8))
    xl, xr = 3.6, 5.0
    y0, dy = 1.3, 1.45
    ax.plot([xl, xl], [0.6, 8.9], color="#8B5A2B", lw=3)
    ax.plot([xr, xr], [0.6, 8.9], color="#8B5A2B", lw=3)
    rungs = [
        ("1", "LDA", "density $n$", "0.8"),
        ("2", "GGA: PBE, PBEsol", "+ gradient $\\nabla n$", "1"),
        ("3", "meta-GGA: SCAN, r$^2$SCAN", "+ kinetic-energy density $\\tau$", "2–5"),
        ("4", "hybrids: PBE0, HSE06", "+ exact exchange (occupied orbitals)", "10–100"),
        ("5", "RPA, double hybrids", "+ unoccupied orbitals", "100–1,000"),
    ]
    cols = ["#56B4E9", "#0072B2", "#009E73", "#E69F00", "#D55E00"]
    for i, (n, name, ingr, cost) in enumerate(rungs):
        y = y0 + i * dy
        ax.plot([xl, xr], [y, y], color="#8B5A2B", lw=3, solid_capstyle="round")
        ax.text((xl + xr) / 2, y + 0.15, n, ha="center", va="bottom", fontsize=9, fontweight="bold")
        ax.text(xr + 0.35, y + 0.17, name, ha="left", va="bottom", fontsize=9.2, color=cols[i],
                fontweight="bold")
        ax.text(xr + 0.35, y - 0.05, ingr, ha="left", va="top", fontsize=8.2, color="0.25")
        ax.text(12.2, y, "×" + cost, ha="center", va="center", fontsize=8.5)
    ax.text(4.3, 0.35, "Hartree world", ha="center", va="top", fontsize=9, style="italic")
    ax.text(4.3, 9.15, "heaven of chemical accuracy", ha="center", va="bottom", fontsize=9,
            style="italic")
    # cost arrow
    ax.annotate("", xy=(13.45, 8.0), xytext=(13.45, 1.0),
                arrowprops=dict(arrowstyle="-|>", lw=1.3, color=INK, mutation_scale=12))
    ax.text(12.2, 8.55, "cost rel.\nto PBE", ha="center", va="bottom", fontsize=8)
    # left side bar: +U and dispersion
    ax.add_patch(FancyBboxPatch((0.25, y0 - 0.35), 2.3, 2 * dy + 0.7,
                                boxstyle="round,pad=0.03,rounding_size=0.15", fc="#F3E6EF",
                                ec=COLORS[3], lw=1.0))
    ax.text(1.4, y0 + dy, "+U and\ndispersion\ncorrections:\nadd-ons at\nrungs 1–3",
            ha="center", va="center", fontsize=8.2, color="#7A3B64")
    for i in range(3):
        ax.plot([2.55, xl - 0.08], [y0 + i * dy, y0 + i * dy], color=COLORS[3], lw=0.8, ls=":")
    save(fig, "55", "fig-55-2-jacobs-ladder")


# ---------------------------------------------------------------- Figure 55.3
def _model_atom():
    """Na-like model atom: screened Coulomb potential, 3s state from a finite-difference solve."""
    Z, Zv, r0 = 11.0, 1.0, 0.40
    h = 0.002
    r = np.arange(1, 12000) * h
    V = -(Zv + (Z - Zv) * np.exp(-r / r0)) / r
    w, v = eigh_tridiagonal(1.0 / h ** 2 + V, -0.5 / h ** 2 * np.ones(r.size - 1),
                            select="i", select_range=(2, 2))
    E = w[0]
    u = v[:, 0] / np.sqrt(h)
    if u[np.argmax(np.abs(u))] < 0:
        u = -u
    return r, V, E, u


def _pseudize(r, V, E, u, rc, c2=1.2):
    """Smooth pseudization (Troullier-Martins form): u_ps = r exp(p(r)) with p even in r.

    p and its first three derivatives match the all-electron solution at rc, so u, V and dV/dr are continuous.
    The free coefficient c2 is chosen for a smooth, monotonic (repulsive-core) potential; norm
    conservation is not imposed in this illustration.
    """
    h = r[1] - r[0]
    i = np.searchsorted(r, rc)
    rc = r[i]
    du = (u[i + 1] - u[i - 1]) / (2 * h)
    dV = (V[i + 1] - V[i - 1]) / (2 * h)
    p0 = np.log(u[i] / rc)
    p1 = du / u[i] - 1 / rc
    p2 = 2 * (V[i] - E) - p1 ** 2 - 2 * p1 / rc
    p3 = 2 * dV - 2 * p1 * p2 - 2 * p2 / rc + 2 * p1 / rc ** 2
    pw = [0, 4, 6, 8]

    def dpow(n, k, x):
        coef = 1.0
        for j in range(k):
            coef *= (n - j)
        return coef * x ** (n - k) if n - k >= 0 and coef != 0 else 0.0 * x

    A = np.array([[dpow(n, k, rc) for n in pw] for k in range(4)])
    bvec = np.array([p0, p1, p2, p3]) - c2 * np.array([dpow(2, k, rc) for k in range(4)])
    cs = dict(zip(pw, np.linalg.solve(A, bvec)))
    cs[2] = c2
    x = r[: i + 1]
    pfun = lambda k: sum(cn * dpow(n, k, x) for n, cn in cs.items())
    ups = np.concatenate([x * np.exp(pfun(0)), u[i + 1:]])
    pp, ppp = pfun(1), pfun(2)
    Vin = E + 0.5 * (pp ** 2 + 2 * pp / x + ppp)
    Vps = np.concatenate([Vin, V[i + 1:]])
    return ups, Vps, rc


def pseudopotential():
    r, V, E, u = _model_atom()
    rc = 1.8
    ups, Vps, rc = _pseudize(r, V, E, u, rc)
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(6.4, 5.0), sharex=True,
                                 gridspec_kw=dict(height_ratios=[1, 1], hspace=0.12))
    ax.plot(r, u, color=COLORS[0], lw=1.8, label="all-electron $rR_{3s}(r)$ (two nodes)")
    ax.plot(r, ups, color=COLORS[1], lw=1.8, ls="--", label="pseudo-wavefunction (nodeless, smooth)")
    ax.axhline(0, color="0.7", lw=0.6)
    ax.axvline(rc, color="0.4", lw=0.9, ls=":")
    ax.text(rc + 0.04, 0.83, "$r_c$ = 1.8 bohr", fontsize=8.5, color="0.3")
    ax.set_ylabel("$rR(r)$ (bohr$^{-1/2}$)")
    ax.legend(loc="lower right", fontsize=8)
    ax.set_ylim(-0.75, 1.0)
    ax.axvspan(0, rc, color="0.93", zorder=0)
    ax.text(0.9, -0.62, "core region replaced", ha="center", fontsize=8.5, color="0.35")
    ax.set_title("(a) radial wavefunctions, Na-like 3s valence state", fontsize=10, loc="left")

    Zv = 1.0
    bx.plot(r, V, color=COLORS[0], lw=1.8, label="all-electron potential (→ $-Z/r$, $Z$ = 11)")
    bx.plot(r, Vps, color=COLORS[1], lw=1.8, ls="--", label="pseudopotential (finite at $r$ = 0)")
    bx.plot(r, -Zv / r, color="0.45", lw=1.0, ls=":", label="$-Z_v/r$, $Z_v$ = 1")
    bx.axvline(rc, color="0.4", lw=0.9, ls=":")
    bx.axvspan(0, rc, color="0.93", zorder=0)
    bx.axhline(E, color="0.6", lw=0.6, ls="-.")
    bx.text(3.95, E + 0.12, f"$\\varepsilon_{{3s}}$ = {E:.2f} Ha", fontsize=8, color="0.4", ha="right")
    bx.set_ylim(-6, 4.5)
    bx.set_xlim(0, 4)
    bx.set_xlabel("$r$ (bohr)")
    bx.set_ylabel("potential (Ha)")
    bx.legend(loc="lower right", fontsize=8)
    bx.set_title("(b) potentials", fontsize=10, loc="left")
    bx.text(2.0, 2.4, "plane-wave cutoff falls from\n~10$^4$ eV to ~300–500 eV", fontsize=8.5,
            color=INK, va="center")
    bx.text(0.06, 1.3, "smooth repulsive core\n(replaces orthogonality\nto the 1s, 2s core states)",
            fontsize=7.6, color=COLORS[1], va="center")
    save(fig, "55", "fig-55-3-pseudopotential")


# ---------------------------------------------------------------- Figure 55.4
def convergence_cutoff_kpoints():
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.8, 3.6))
    Ec = np.arange(150, 701, 25)

    def err(E, E1, slope, floor):     # log-linear decay to a noise floor
        return 10 ** (-slope * (E - E1)) + floor

    si = err(Ec, 300, 0.0145, 0.0)
    ox = err(Ec, 520, 0.0090, 0.0)
    ax.semilogy(Ec, si, "o-", color=COLORS[0], ms=3.5, label="Si")
    ax.semilogy(Ec, ox, "s-", color=COLORS[1], ms=3.5, label="O-containing oxide")
    ax.axhline(1, color="0.4", ls="--", lw=1.0)
    ax.text(420, 0.8, "typical target\n1 meV/atom", ha="center", va="top", fontsize=7.5, color="0.3")
    ax.set_xlim(150, 700)
    ax.set_ylim(0.01, 1000)
    ax.set_xlabel("plane-wave cutoff $E_{cut}$ (eV)")
    ax.set_ylabel("total-energy error ΔE (meV/atom)")
    ax.legend(loc="upper right", fontsize=8.5)
    ax.set_title("(a) cutoff", fontsize=10, loc="left")
    for x0, c in [(300, COLORS[0]), (520, COLORS[1])]:
        ax.plot([x0, x0], [0.01, 1], color=c, lw=0.7, ls=":")
        ax.text(x0 + 6, 0.013, f"{x0}", color=c, fontsize=7.5)

    n = np.arange(2, 25)
    si_k = 60 * np.exp(-1.2 * (n - 2))
    al_tab = {2: 150, 3: 60, 4: 20, 5: 28, 6: 6.5, 7: 9.5, 8: 3.0, 9: 4.2, 10: 1.6, 11: 2.3, 12: 1.0,
              13: 0.55, 14: 0.75, 15: 0.32, 16: 0.20, 17: 0.29, 18: 0.13, 19: 0.16, 20: 0.07,
              21: 0.095, 22: 0.05, 23: 0.06, 24: 0.035}
    al = np.array([al_tab[k] for k in n])
    m = si_k >= 0.01
    bx.semilogy(n[m], si_k[m], "o-", color=COLORS[0], ms=3.5, label="Si (semiconductor)")
    bx.semilogy(n, al, "s-", color=COLORS[2], ms=3.5, label="Al (metal, MP 0.1 eV)")
    bx.axhline(1, color="0.4", ls="--", lw=1.0)
    bx.set_xlim(1, 25)
    bx.set_ylim(0.01, 1000)
    bx.set_xticks([2, 4, 8, 12, 16, 20, 24])
    bx.set_xlabel("k-point mesh $n$ ($n\\times n\\times n$)")
    bx.set_ylabel("ΔE (meV/atom)")
    bx.legend(loc="upper right", fontsize=8.5)
    bx.set_title("(b) k-point sampling", fontsize=10, loc="left")
    bx.text(9.5, 0.025, "exponential\n(full bands)", color=COLORS[0], fontsize=7.8, ha="left")
    bx.text(15.5, 2.0, "oscillating,\nslow (Fermi\nsurface)", color=COLORS[2], fontsize=7.8)
    fig.tight_layout(w_pad=1.5)
    save(fig, "55", "fig-55-4-convergence-cutoff-kpoints")


# ---------------------------------------------------------------- Figure 55.5
def band_gap_parity():
    fig, ax = new_fig(5.4, 5.0)
    mats = ["Si", "GaAs", "ZnO", "C", "MgO", "NiO"]
    exp = [1.17, 1.52, 3.44, 5.48, 7.8, 4.0]
    pbe = [0.6, 0.5, 0.7, 4.1, 4.5, 0.7]
    hse = [1.2, 1.3, 2.5, 5.3, 6.5, 4.2]
    x = np.linspace(0, 8, 10)
    ax.fill_between(x, 0, 0.7 * x, color=COLORS[1], alpha=0.10, lw=0)
    ax.plot(x, x, color=INK, lw=1.0)
    ax.text(6.9, 7.2, "$y = x$", fontsize=9, rotation=45, ha="center", va="center")
    ax.plot(x, 0.7 * x, color=COLORS[1], lw=0.6, ls=":")
    ax.text(5.6, 1.15, "semi-local DFT\nunderestimates gaps\nby 30–100 %", fontsize=8.5,
            color=COLORS[1], ha="center")
    ax.plot(exp, pbe, "o", color=COLORS[1], ms=7, mec=INK, mew=0.5, label="PBE")
    ax.plot(exp, hse, "s", color=COLORS[0], ms=7, mec=INK, mew=0.5, label="HSE06")
    ax.plot([4.0], [3.0], "^", color=COLORS[2], ms=8, mec=INK, mew=0.5, label="PBE+U (NiO)")
    for m_, e, p, hh in zip(mats, exp, pbe, hse):
        ax.plot([e, e], [p, hh], color="0.75", lw=0.8, zorder=0)
        dx = 0.12
        ha = "left"
        if m_ in ("MgO", "Si", "ZnO"):
            dx, ha = -0.12, "right"
        ax.text(e + dx, hh + 0.12, m_, fontsize=8.5, ha=ha, va="bottom")
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)
    ax.set_aspect("equal")
    ax.set_xlabel("experimental band gap (eV)")
    ax.set_ylabel("calculated band gap (eV)")
    ax.legend(loc="upper left", fontsize=9)
    save(fig, "55", "fig-55-5-band-gap-parity")


# ---------------------------------------------------------------- Figure 55.6
def _bm(V, E0, V0, B, Bp):
    eta = (V0 / V) ** (2 / 3)
    return E0 + 9 * V0 * B / 16 * ((eta - 1) ** 3 * Bp + (eta - 1) ** 2 * (6 - 4 * eta))


def eos_copper():
    Vd = np.array([11.185, 11.567, 11.958, 12.358, 12.766])
    Ed = np.array([-3.6950, -3.7140, -3.7200, -3.7145, -3.6991])
    p, _ = curve_fit(_bm, Vd, Ed, p0=[-3.72, 11.96, 140 / 160.2, 5])
    E0, V0, B, Bp = p
    c = np.polyfit(Vd, Ed, 2)
    Vp = -c[1] / (2 * c[0])
    Vg = np.linspace(11.0, 13.0, 300)
    fig, ax = new_fig(6.2, 4.0)
    ax.plot(Vg, _bm(Vg, *p), color=COLORS[0], lw=1.8, label="Birch–Murnaghan fit")
    ax.plot(Vg, np.polyval(c, Vg), color=COLORS[1], lw=1.4, ls="--", label="parabola through all five points")
    ax.plot(Vd, Ed, "o", color=INK, ms=6, zorder=3, label="DFT (PBE) points")
    ax.axvline(11.81, color="0.4", ls=":", lw=1.0)
    ax.text(11.79, -3.6915, "experiment\n$V_0$ ≈ 11.81 Å$^3$\n($a$ = 3.615 Å)", ha="right", va="top",
            fontsize=8, color="0.3")
    ax.plot([V0, V0], [-3.725, E0], color=COLORS[0], lw=0.8, ls=":")
    ax.plot([Vp, Vp], [-3.725, np.polyval(c, Vp)], color=COLORS[1], lw=0.8, ls=":")
    ax.text(V0 - 0.02, -3.7245, f"{V0:.2f}", color=COLORS[0], fontsize=7.5, ha="right", va="bottom")
    ax.text(Vp + 0.02, -3.7245, f"{Vp:.2f}", color=COLORS[1], fontsize=7.5, ha="left", va="bottom")
    a0 = (4 * V0) ** (1 / 3)
    ax.text(12.25, -3.7228,
            f"BM fit: $V_0$ = {V0:.2f} Å$^3$, $a_0$ = {a0:.3f} Å\n$B$ = {B * 160.2:.0f} GPa, $B'$ = {Bp:.1f}",
            fontsize=8.5, color=COLORS[0], va="bottom")
    ax.set_xlim(11.0, 13.0)
    ax.set_ylim(-3.725, -3.690)
    ax.set_xlabel("volume per atom (Å$^3$)")
    ax.set_ylabel("energy (eV/atom)")
    ax.legend(loc="upper right", fontsize=8.3)
    save(fig, "55", "fig-55-6-eos-copper")


if __name__ == "__main__":
    kohn_sham_scf_loop()
    jacobs_ladder()
    pseudopotential()
    convergence_cutoff_kpoints()
    band_gap_parity()
    eos_copper()
