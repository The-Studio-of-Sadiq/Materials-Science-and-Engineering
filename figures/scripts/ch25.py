"""Figures for Chapter 25 — Electrical Conduction in Materials.

Run from the repository root:  python figures/scripts/ch25.py
"""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, save, COLORS, INK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyArrowPatch
from scipy.integrate import quad


# ---------------------------------------------------------------- Figure 25.1
def resistivity_spectrum():
    fig, ax = new_fig(6.8, 4.6)
    ax.set_xscale("log")
    ax.set_xlim(1e-9, 1e18)
    # class bands
    bands = [(1e-9, 1e-5, "conductors", "#E8F0F8"),
             (1e-5, 1e6, "semiconductors", "#F3EEE2"),
             (1e6, 1e18, "insulators", "#EAF4EC")]
    rows = [
        ("Superconductors", None, None, COLORS[7]),
        ("Pure metals", 1.59e-8, 4.2e-7, COLORS[0]),
        ("Resistance alloys", 4e-7, 1.1e-6, COLORS[5]),
        ("Conductive oxides,\ngraphite", 1e-6, 1e-4, COLORS[3]),
        ("Conductive composites", 1e-6, 1e2, COLORS[4]),
        ("Semiconductors\n(Si, Ge, GaAs)", 1e-5, 1e6, COLORS[1]),
        ("ESD plastics", 1e4, 1e9, COLORS[6]),
        ("Glasses, ceramics", 1e9, 1e14, COLORS[2]),
        ("Polymers", 1e12, 1e17, "#6A5ACD"),
    ]
    n = len(rows)
    ax.set_ylim(-0.7, n + 0.2)
    for lo, hi, lab, c in bands:
        ax.axvspan(lo, hi, color=c, zorder=0)
        ax.text(np.sqrt(lo * hi), n - 0.15, lab, ha="center", va="center", fontsize=9.5,
                color=INK, style="italic")
    for i, (lab, lo, hi, c) in enumerate(rows):
        y = n - 1 - i - 0.3
        ax.text(1.5e-9 if lo is None or lo > 1e-3 else None or 1e-9, y, "", fontsize=1)
        if lo is None:
            ax.annotate("", xy=(1.05e-9, y), xytext=(1e-7, y),
                        arrowprops=dict(arrowstyle="-|>", color=c, lw=2))
            ax.text(1.2e-7, y, r"Superconductors: $\rho = 0$ below $T_c$", va="center", fontsize=8.5)
            continue
        if lab == "Pure metals":
            ax.plot([lo, hi], [y, y], color=c, lw=1, alpha=0.6)
            metals = [("Ag", 1.59e-8), ("Cu", 1.68e-8), ("Au", 2.44e-8), ("Al", 2.65e-8),
                      ("W", 5.6e-8), ("Fe", 9.7e-8), ("Ti", 4.2e-7)]
            lx = np.logspace(-8.85, -3.45, len(metals))
            for k, (m, r) in enumerate(metals):
                ax.plot(r, y, "o", color=c, ms=4.5, zorder=3)
                ax.plot([r, lx[k]], [y + 0.06, y + 0.36], color=c, lw=0.6)
                ax.text(lx[k], y + 0.38, m, ha="center", va="bottom", fontsize=8)
            ax.text(1.5e-6, y - 0.05, lab + "  (1.6×10$^{-8}$ to 4.2×10$^{-7}$)", va="center", fontsize=8.5)
            continue
        ax.barh(y, hi - lo, left=lo, height=0.42, color=c, alpha=0.85, edgecolor=INK, lw=0.6)
        if lab == "Semiconductors\n(Si, Ge, GaAs)":
            ax.text(np.sqrt(lo * hi), y, "doped  ←→  intrinsic", ha="center",
                    va="center", fontsize=7.5)
        if hi < 1e10:
            ax.text(hi * 2.2, y, lab, va="center", fontsize=8.5)
        else:
            ax.text(lo / 2.2, y, lab, va="center", ha="right", fontsize=8.5)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xticks([10.0 ** k for k in range(-9, 19, 3)])
    ax.set_xlabel(r"Resistivity at room temperature, $\rho$ ($\Omega\,$m)")
    save(fig, "25", "fig-25-1-resistivity-spectrum")


# ---------------------------------------------------------------- Figure 25.2
THETA_CU = 343.0


def _bg(T, theta=THETA_CU):
    if T <= 0:
        return 0.0
    f = lambda x: x**5 / ((np.exp(x) - 1) * (1 - np.exp(-x)))
    return (T / theta) ** 5 * quad(f, 1e-8, theta / T, limit=200)[0]


def matthiessen():
    T = np.linspace(0.5, 400, 400)
    g = np.array([_bg(t) for t in T])
    K = (1.70 - 0.002) / _bg(293.0)
    rph = K * g
    r0, rimp, rdef = 0.002, 1.10, 0.05
    fig, ax = new_fig(6.4, 4.2)
    ax.plot(T, r0 + rph, color=COLORS[0], label="high-purity annealed Cu")
    ax.plot(T, r0 + rimp + rph, color=COLORS[1], label="Cu + 1 at.% Ni (annealed)")
    ax.plot(T, r0 + rimp + rdef + rph, color=COLORS[2], ls="--", label="Cu + 1 at.% Ni, cold-worked")
    ax.set_xlim(0, 400)
    ax.set_ylim(0, 5)
    ax.set_xlabel("Temperature, $T$ (K)")
    ax.set_ylabel(r"Resistivity, $\rho$ ($\mu\Omega\,$cm)")
    # arrows at 300 K
    x0 = 300
    rp300 = K * _bg(300.0)
    ax.annotate("", xy=(x0, r0 + rph[0] * 0 + rp300), xytext=(x0, 0),
                arrowprops=dict(arrowstyle="<|-|>", color=COLORS[0], lw=1.1, mutation_scale=9,
                                shrinkA=0, shrinkB=0))
    ax.text(x0 - 5, rp300 / 2, r"$\rho_{\rm ph}(T)$", ha="right", va="center", color=COLORS[0])
    ax.annotate("", xy=(x0 + 22, rp300 + rimp), xytext=(x0 + 22, rp300),
                arrowprops=dict(arrowstyle="<|-|>", color=COLORS[1], lw=1.1, mutation_scale=9,
                                shrinkA=0, shrinkB=0))
    ax.text(x0 + 27, rp300 + rimp / 2, r"$\rho_{\rm imp}\approx1.1$", va="center", color=COLORS[1])
    ax.annotate(r"$\rho_{\rm def}\approx0.05$" + "\n(cold work)", xy=(x0 + 22, rp300 + rimp + rdef / 2),
                xytext=(350, 4.3), fontsize=9, color=COLORS[2], ha="center",
                arrowprops=dict(arrowstyle="-", color=COLORS[2], lw=0.8))
    # Theta_D / 3
    ax.axvline(THETA_CU / 3, color="grey", ls=":", lw=1)
    ax.text(THETA_CU / 3 + 3, 2.75, r"$\Theta_D/3\approx115$ K", fontsize=8.5, color="grey", va="top")
    ax.text(THETA_CU / 3 - 4, 0.55, r"$\propto T^5$" + "\n(low $T$)", ha="right", fontsize=8.5, color=COLORS[0])
    ax.text(205, 1.0, r"$\propto T$", fontsize=9, color=COLORS[0])
    # residual
    ax.plot([4], [r0 + rimp], "o", color=COLORS[1], ms=4)
    ax.annotate("residual resistivity\n" + r"$\rho(4\,{\rm K})\approx1.1$ (alloy)," + "\n0.002 (pure Cu)",
                xy=(4, r0 + rimp), xytext=(20, 2.25), fontsize=8.5,
                arrowprops=dict(arrowstyle="-", color=INK, lw=0.7))
    ax.text(10, 4.85, r"RRR $=\dfrac{\rho(293\,{\rm K})}{\rho(4.2\,{\rm K})}$" + "\n" +
            r"pure Cu: $1.70/0.002\approx850$" + "\n" + r"Cu-1Ni: $2.8/1.1\approx2.5$",
            va="top", fontsize=8.5, bbox=dict(fc="white", ec="grey", lw=0.6, boxstyle="round,pad=0.35"))
    ax.legend(loc="upper left", bbox_to_anchor=(0.33, 0.83), fontsize=8.5)
    save(fig, "25", "fig-25-2-matthiessen-rho-vs-t")


# ---------------------------------------------------------------- Figure 25.3
def nordheim():
    x = np.linspace(0, 1, 801)
    # Cu-Ni: linear background + skewed Nordheim term, peak ~50 at 45 at.% Ni
    a, b = 1.12, 1.37
    shape = x**a * (1 - x) ** b
    shape /= shape.max()
    cuni = 1.7 * (1 - x) + 6.9 * x + 46.5 * shape
    # Cu-Au disordered
    cuau_d = 1.7 * (1 - x) + 2.2 * x + 52.0 * x * (1 - x) / 4 * 4 * 0.25
    cuau_d = 1.7 * (1 - x) + 2.2 * x + 51.0 * x * (1 - x)
    # ordered: dips at Cu3Au (0.25) and CuAu (0.50)
    dip = lambda x0, w, target: (cuau_d - target) * np.exp(-((x - x0) / w) ** 2)
    v25 = np.interp(0.25, x, cuau_d)
    cuau_o = cuau_d - dip(0.25, 0.035, 4.5) - dip(0.5, 0.03, 4.0)
    print("CuNi at 0.1:", np.interp(0.1, x, cuni), "peak", cuni.max(), x[cuni.argmax()],
          "CuAu peak", cuau_d.max(), "v25", v25)
    fig, ax = new_fig(6.4, 4.0)
    X = 100 * x
    ax.plot(X, cuni, color=COLORS[0], label="Cu–Ni (complete solid solution)")
    ax.plot(X, cuau_d, color=COLORS[1], ls="--", label="Cu–Au, quenched (disordered)")
    ax.plot(X, cuau_o, color=COLORS[1], label="Cu–Au, annealed (ordered)")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 55)
    ax.set_xlabel("Second element, Ni or Au (at.%)")
    ax.set_ylabel(r"Resistivity at room temperature ($\mu\Omega\,$cm)")
    ax.plot(10, np.interp(0.1, x, cuni), "o", color=COLORS[0], ms=4)
    ax.annotate("Cu–Ni 90/10\n(≈ 19)", xy=(10, np.interp(0.1, x, cuni)), xytext=(3, 30),
                fontsize=8.5, arrowprops=dict(arrowstyle="-", lw=0.7))
    ax.plot(45, np.interp(0.45, x, cuni), "o", color=COLORS[0], ms=4)
    ax.annotate("constantan\n(Cu–45Ni, ≈ 50)", xy=(45, np.interp(0.45, x, cuni)), xytext=(56, 50),
                fontsize=8.5, va="center", arrowprops=dict(arrowstyle="-", lw=0.7))
    ax.text(25, 4.5 - 1.5, r"Cu$_3$Au", ha="center", va="top", fontsize=8.5, color=COLORS[1])
    ax.text(50, 4.0 - 1.5, "CuAu", ha="center", va="top", fontsize=8.5, color=COLORS[1])
    ax.text(37.5, 2.0, "order\nremoves\nscattering", fontsize=8.5, color=COLORS[1], ha="center",
            va="bottom", linespacing=1.0)
    ax.text(97, np.interp(1, x, cuni) + 2, "Ni", ha="right", fontsize=8.5)
    ax.legend(loc="upper right", fontsize=8.5, bbox_to_anchor=(1.0, 0.82))
    ax.text(1.5, 51, r"$\rho\approx\rho_{\rm ph}+C\,x(1-x)$", fontsize=10, ha="left")
    save(fig, "25", "fig-25-3-nordheim-cu-ni-cu-au")


# ---------------------------------------------------------------- Figure 25.4
def holm():
    fig = plt.figure(figsize=(6.8, 3.9))
    axL = fig.add_axes([0.0, 0.0, 0.52, 1.0])
    axR = fig.add_axes([0.53, 0.12, 0.47, 0.88])
    for a in (axL, axR):
        a.set_aspect("equal")
        a.axis("off")
    # ---- left: rough contact
    axL.set_xlim(0, 10)
    axL.set_ylim(-0.6, 7.4)
    xs = np.linspace(0.5, 9.5, 600)
    rng = np.random.default_rng(3)
    base = 0.18 * np.sin(2.3 * xs) + 0.12 * np.sin(5.1 * xs + 1)
    spots = [2.0, 4.3, 6.4, 8.2]
    gap = 0.45
    upper = 3.5 + gap + base
    lower = 3.5 - gap - 0.15 * np.sin(1.9 * xs + 2) - 0.1 * np.sin(4.4 * xs)
    for s in spots:
        bump = np.exp(-((xs - s) / 0.28) ** 2)
        mid = 3.5 + 0.05 * np.sin(s)
        upper = upper - (upper - mid) * bump
        lower = lower + (mid - lower) * bump
    axL.fill_between(xs, upper, 6.4, color="#C9A27E", ec=INK, lw=0.8)
    axL.fill_between(xs, 0.6, lower, color="#B9B9C9", ec=INK, lw=0.8)
    # oxide film on non-contacting regions
    contact = np.zeros_like(xs, bool)
    for s in spots:
        contact |= np.abs(xs - s) < 0.17
    fu = np.where(contact, np.nan, upper)
    fl = np.where(contact, np.nan, lower)
    axL.plot(xs, fu - 0.04, color="#555555", lw=3.2, alpha=0.75, solid_capstyle="butt")
    axL.plot(xs, fl + 0.04, color="#555555", lw=3.2, alpha=0.75, solid_capstyle="butt")
    # current lines
    for s in spots:
        for dx in (-0.75, -0.38, 0, 0.38, 0.75):
            yy = np.linspace(0, 1, 50)
            xu = s + dx * (1 - np.exp(-((1 - yy) * 2.6))) * 0 + dx * (yy ** 1.6)
            axL.plot(xu, 3.5 + 2.7 * yy, color=COLORS[0], lw=0.8)
            axL.plot(xu, 3.5 - 2.7 * yy, color=COLORS[0], lw=0.8)
    axL.text(5, 6.65, "upper member", ha="center", fontsize=9)
    axL.text(5, 0.25, "lower member", ha="center", fontsize=9)
    # apparent area bracket
    axL.annotate("", xy=(0.5, 7.1), xytext=(9.5, 7.1),
                 arrowprops=dict(arrowstyle="|-|", color=INK, lw=0.9, mutation_scale=4))
    axL.text(5, 7.2, "apparent contact area", ha="center", va="bottom", fontsize=9)
    axL.annotate("a-spot", xy=(4.3, 3.5), xytext=(3.2, 2.0), fontsize=8.5, color=INK,
                 bbox=dict(fc="white", ec="none", pad=0.5),
                 arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.8, mutation_scale=8))
    axL.annotate("oxide / contaminant\nfilm", xy=(7.3, 3.5 + gap + 0.12), xytext=(6.6, 5.4),
                 fontsize=8.5, ha="center", bbox=dict(fc="white", ec="none", pad=0.5),
                 arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.8, mutation_scale=8))
    # ---- right: single a-spot, oblate spheroidal coordinates
    axR.set_xlim(-4.2, 4.2)
    axR.set_ylim(-3.3, 3.3)
    a = 1.0
    # boundary plane (insulating except |x|<a)
    axR.plot([-4, -a], [0, 0], color=INK, lw=2.5)
    axR.plot([a, 4], [0, 0], color=INK, lw=2.5)
    axR.fill_between([-4, -a], -0.06, 0.06, color="#888888")
    th = np.linspace(-np.pi / 2, np.pi / 2, 300)
    for mu in (0.35, 0.7, 1.05, 1.4):
        X = a * np.cosh(mu) * np.sin(th)
        Z = a * np.sinh(mu) * np.cos(th)
        for sgn in (1, -1):
            axR.plot(X, sgn * Z, color=COLORS[1], lw=0.9, ls="--")
    s = np.linspace(-3.0, 3.0, 300)
    for nu in (0.12, 0.35, 0.6, 0.85, 1.1, 1.35):
        # hyperbolae x = a sin(nu) cosh(u), z = a cos(nu) sinh(u)
        u = np.linspace(-2.0, 2.0, 300)
        X = a * np.sin(nu) * np.cosh(u)
        Z = a * np.cos(nu) * np.sinh(u)
        m = (np.abs(X) < 4.1) & (np.abs(Z) < 3.2)
        axR.plot(np.where(m, X, np.nan), Z, color=COLORS[0], lw=1.0)
        axR.plot(np.where(m, -X, np.nan), Z, color=COLORS[0], lw=1.0)
    axR.plot([0, 0], [-3.2, 3.2], color=COLORS[0], lw=1.0)
    axR.annotate("", xy=(a, -0.35), xytext=(0, -0.35),
                 arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=0.9, mutation_scale=8,
                                 shrinkA=0, shrinkB=0))
    axR.text(a / 2, -0.42, "$a$", ha="center", va="top", fontsize=10,
             bbox=dict(fc="white", ec="none", pad=0.3))
    axR.text(-4.1, 2.95, r"$\rho_1$", fontsize=10)
    axR.text(-4.1, -3.1, r"$\rho_2$", fontsize=10)
    axR.text(2.2, 0.15, "insulating\ninterface", fontsize=8, ha="center", va="bottom",
             bbox=dict(fc="white", ec="none", pad=0.4))
    axR.text(0, -3.55, "current lines (solid), equipotentials (dashed)", ha="center",
             fontsize=8, va="top")
    axR.text(2.75, 2.6, r"$R_c=\dfrac{\rho}{2a}$", fontsize=11, ha="center",
             bbox=dict(fc="white", ec="grey", lw=0.6, boxstyle="round,pad=0.3"))
    # ---- inset: equivalent circuit
    axC = fig.add_axes([0.53, 0.0, 0.47, 0.11])
    axC.set_xlim(0, 10)
    axC.set_ylim(0, 1)
    axC.axis("off")

    def resistor(x0, lab):
        xs_ = np.linspace(x0, x0 + 1.4, 13)
        ys_ = 0.5 + 0.18 * np.array([0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0])
        axC.plot(xs_, ys_, color=INK, lw=1)
        axC.text(x0 + 0.7, 0.85, lab, ha="center", va="bottom", fontsize=8.5)
    axC.plot([0.6, 1.5], [0.5, 0.5], color=INK, lw=1)
    resistor(1.5, r"$R_{\rm bulk}$")
    axC.plot([2.9, 4.0], [0.5, 0.5], color=INK, lw=1)
    resistor(4.0, r"$R_c$")
    axC.plot([5.4, 6.5], [0.5, 0.5], color=INK, lw=1)
    resistor(6.5, r"$R_{\rm film}$")
    axC.plot([7.9, 8.8], [0.5, 0.5], color=INK, lw=1)
    for xx in (0.6, 8.8):
        axC.plot(xx, 0.5, "o", color=INK, ms=3, mfc="white")
    save(fig, "25", "fig-25-4-holm-constriction")


# ---------------------------------------------------------------- Figure 25.5
def _fs(t, lam, p=0.0):
    """Fuchs-Sondheimer rho/rho0 for film thickness t, mean free path lam."""
    k = t / lam
    f = lambda u: (1 / u**3 - 1 / u**5) * (1 - np.exp(-k * u)) / (1 - p * np.exp(-k * u))
    I = quad(f, 1, np.inf, limit=200)[0]
    return 1 / (1 - 3 / (2 * k) * (1 - p) * I)


def _ms(d, lam, R):
    al = lam / d * R / (1 - R)
    return 1 / (3 * (1 / 3 - al / 2 + al**2 - al**3 * np.log(1 + 1 / al)))


def _film(t, rho0, lam, R=0.3, p=0.0):
    return rho0 * (1 + (_fs(t, lam, p) - 1) + (_ms(t, lam, R) - 1))


def _line(W, rho0, lam, tb, p, R):
    """Effective resistivity of a line of width W, height 2W, with a non-conducting
    barrier of thickness tb on sides and bottom; grain size = conductor width."""
    Wc = W - 2 * tb
    if Wc < 1.0:
        return np.nan
    return _film(Wc, rho0, lam, R, p) * (2 * W * W) / (Wc * (2 * W - tb))


def size_effect():
    w = np.logspace(np.log10(5), 3, 300)
    cu_film = np.array([_film(t, 1.68, 39.0) for t in w])
    cu_line = np.array([_line(W, 1.68, 39.0, 2.0, 0.3, 0.25) for W in w])
    co_line = np.array([_line(W, 6.2, 11.8, 0.0, 0.0, 0.2) for W in w])
    ru_line = np.array([_line(W, 7.1, 6.7, 0.0, 0.0, 0.2) for W in w])
    for name, arr in (("cu_film", cu_film), ("cu_line", cu_line), ("co", co_line), ("ru", ru_line)):
        print(name, [round(float(np.interp(v, w, arr)), 2) for v in (10, 15, 20, 30, 100, 1000)])
    fig, ax = new_fig(6.4, 4.0)
    ax.set_xscale("log")
    ax.axhline(1.68, color=COLORS[0], ls="--", lw=1.2)
    ax.text(600, 1.4, "Cu bulk (1.7)", color=COLORS[0], fontsize=8.5, ha="center", va="top")
    ax.plot(w, cu_film, color=COLORS[0], label=r"Cu film, FS + MS ($p=0$, $R=0.3$, $d=t$)")
    ax.plot(w, cu_line, color=COLORS[0], ls="-.", label="Cu line incl. 2 nm TaN barrier (effective)")
    ax.plot(w, co_line, color=COLORS[3], label="Co line (no barrier)")
    ax.plot(w, ru_line, color=COLORS[1], label="Ru line (no barrier)")
    ax.axvline(39, color="grey", ls=":", lw=1)
    ax.text(41, 9.7, r"$\lambda_{\rm Cu}=39$ nm", color="grey", fontsize=8.5, va="top")
    ax.set_xlim(5, 1000)
    ax.set_ylim(0, 10)
    ax.set_xlabel("Line width or film thickness (nm)")
    ax.set_ylabel(r"Resistivity ($\mu\Omega\,$cm)")
    ax.legend(loc="center right", fontsize=8, bbox_to_anchor=(1.0, 0.43))
    ax.set_xticks([5, 10, 20, 50, 100, 200, 500, 1000])
    ax.set_xticklabels(["5", "10", "20", "50", "100", "200", "500", "1000"])
    save(fig, "25", "fig-25-5-thin-film-size-effect")


# ---------------------------------------------------------------- Figure 25.6
def _perc(phi, phic, w, s0, sm, t=2.0):
    d = w * np.logaddexp(0, (phi - phic) / w)
    return sm + s0 * d**t


def percolation():
    fig = plt.figure(figsize=(6.4, 5.2))
    ax = fig.add_axes([0.12, 0.36, 0.84, 0.6])
    phi = np.linspace(0, 0.5, 3000)
    ag = _perc(phi, 0.16, 0.0015, 5e6, 1e-13)
    cnt = _perc(phi, 0.005, 0.0003, 1e5, 1e-13)
    ax.axhspan(1e-7, 1e-2, color="#E9F2E4")
    ax.axhspan(1e4, 1e6, color="#F6ECDD")
    ax.text(0.495, 3e-5, "ESD / antistatic range", ha="right", va="center", fontsize=8.5, color="#3E7A2E")
    ax.text(0.01, 1.5e5, "conductive adhesive range", ha="left", va="center", fontsize=8.5, color="#9A6214")
    ax.semilogy(phi, ag, color=COLORS[0], label="Ag spheres in epoxy")
    ax.semilogy(phi, cnt, color=COLORS[1], label="CNTs in epoxy")
    ax.axvline(0.16, color=COLORS[0], ls=":", lw=1)
    ax.text(0.163, 1e-12, r"$\phi_c\approx0.16$", color=COLORS[0], fontsize=9)
    ax.annotate(r"$\phi_c\approx0.005$", xy=(0.006, 1e-9), xytext=(0.04, 1e-10), fontsize=9,
                color=COLORS[1], arrowprops=dict(arrowstyle="-", color=COLORS[1], lw=0.8))
    ax.text(0.33, 3e2, r"$\sigma\approx\sigma_0(\phi-\phi_c)^2$", fontsize=10, color=COLORS[0])
    ax.text(0.02, 3e-14 * 10, "epoxy matrix", fontsize=8.5, color="grey")
    ax.set_xlim(0, 0.5)
    ax.set_ylim(1e-14, 1e6)
    ax.set_yticks([10.0 ** k for k in range(-14, 7, 2)])
    ax.set_xlabel(r"Filler volume fraction, $\phi$")
    ax.set_ylabel(r"Conductivity, $\sigma$ (S/m)")
    ax.legend(loc="lower right", bbox_to_anchor=(1.0, 0.1), fontsize=8.5)
    # insets
    rng = np.random.default_rng(7)
    titles = [(r"$\phi<\phi_c$: isolated particles", 0.09),
              (r"$\phi\approx\phi_c$: first spanning cluster", 0.16),
              (r"$\phi>\phi_c$: dense network", 0.30)]
    for k, (tt, f) in enumerate(titles):
        a = fig.add_axes([0.06 + 0.315 * k, 0.015, 0.25, 0.22])
        a.set_xlim(0, 1)
        a.set_ylim(0, 1)
        a.set_aspect("equal")
        a.set_xticks([])
        a.set_yticks([])
        a.add_patch(Rectangle((0, 0), 1, 1, fc="#F4EFE2", ec=INK, lw=0.8))
        r = 0.045
        nP = int(f / (np.pi * r**2))
        pts = []
        tries = 0
        while len(pts) < nP and tries < 20000:
            tries += 1
            p = rng.uniform(r, 1 - r, 2)
            if all(np.hypot(*(p - q)) > 2 * r * 0.92 for q in pts):
                pts.append(p)
        pts = np.array(pts)
        if k == 1:
            # build an explicit spanning chain left to right
            chain = np.column_stack([np.linspace(r, 1 - r, 12),
                                     0.5 + 0.18 * np.sin(np.linspace(0, 6, 12))])
            keep = [p for p in pts if np.min(np.hypot(*(chain - p).T)) > 2 * r]
            pts = np.vstack([chain, np.array(keep)[:len(keep) - 6]])
        for p in pts:
            a.add_patch(Circle(p, r, fc="#9A9A9A", ec=INK, lw=0.4))
        if k == 1:
            for p in pts[:12]:
                a.add_patch(Circle(p, r, fc=COLORS[0], ec=INK, lw=0.4))
        a.set_title(tt, fontsize=8, pad=3)
        a.annotate("", xy=(f, 2e-14 if False else 1e-14), xycoords=ax.transData,
                   xytext=(0.5, 1.0), textcoords=a.transAxes) if False else None
    save(fig, "25", "fig-25-6-percolation")


KB = 8.617e-5  # eV/K


def ionic_arrhenius():
    fig, ax = new_fig(6.6, 4.4)

    def line(s_ref, T_ref_C, Ea, T_lo_C, T_hi_C, **kw):
        Tc = np.linspace(T_lo_C, T_hi_C, 50)
        T = Tc + 273.15
        Tr = T_ref_C + 273.15
        s = s_ref * np.exp(-Ea / KB * (1 / T - 1 / Tr))
        ax.plot(1000 / T, np.log10(s), **kw)
        return 1000 / T, np.log10(s)

    # target region / liquid reference
    ax.axhspan(-2, 0.6, color=COLORS[2], alpha=0.08, lw=0)
    ax.axhline(-2, color=COLORS[2], ls="--", lw=1.1)
    ax.text(1.62, -2.1, r"liquid Li-ion electrolyte $\approx10^{-2}$ S/cm", ha="left", va="top", fontsize=8,
            color=COLORS[2])
    ax.text(3.58, 0.32, r"target: $\sigma > 10^{-2}$ S/cm", ha="right", va="center", fontsize=8,
            color=COLORS[2])

    line(0.03, 800, 0.95, 350, 1000, color=COLORS[0])
    ax.text(1.62, -4.85, "8YSZ (0.95 eV)", fontsize=8, color=COLORS[0], ha="left", va="center")
    line(0.025, 600, 0.70, 300, 800, color=COLORS[5])
    ax.text(1.77, -3.8, "Gd-doped CeO$_2$ (0.70 eV)", fontsize=8, color="#2E86C1", ha="left", va="center")
    line(0.3, 300, 0.30, 25, 400, color=COLORS[1])
    ax.text(1.45, -0.05, "Na $\\beta''$-alumina\n(0.30 eV)", fontsize=8, color=COLORS[1], ha="right",
            va="center")
    line(5e-4, 25, 0.35, 25, 200, color=COLORS[3])
    ax.text(3.37, -3.65, "LLZO\ngarnet\n(0.35 eV)", fontsize=8, color=COLORS[3], ha="left", va="center")
    line(1e-2, 25, 0.25, 25, 200, color=COLORS[4])
    ax.text(2.13, -0.30, "Li$_{10}$GeP$_2$S$_{12}$ (0.25 eV)", fontsize=8, color="#A06A00", ha="left",
            va="bottom")
    # AgI: beta below 147 C, alpha above with jump
    xb, yb = line(1e-6, 25, 0.45, 25, 147, color=INK, lw=1.4)
    xa, ya = line(1.3, 147, 0.05, 147, 350, color=INK, lw=2.4)
    ax.plot([xb[-1], xa[0]], [yb[-1], ya[0]], color=INK, lw=1.0, ls=":")
    ax.text(2.34, -3.0, "AgI: β→α\njump at 147 °C", fontsize=8, ha="right", va="center")
    ax.text(1.95, 0.27, r"$\alpha$-AgI (superionic)", fontsize=8, ha="center", va="bottom")
    ax.text(2.95, -5.6, r"$\beta$-AgI", fontsize=8, ha="center")
    # Nafion
    line(0.1, 80, 0.10, 20, 90, color="#777777", lw=3.2, solid_capstyle="round")
    ax.text(3.44, -1.2, "Nafion", fontsize=8, color="#555555", ha="left", va="center")

    ax.set_xlim(0.75, 3.6)
    ax.set_ylim(-8, 0.6)
    ax.set_xlabel(r"$1000/T$ (K$^{-1}$)")
    ax.set_ylabel(r"$\log_{10}\,\sigma$ ($\sigma$ in S/cm)")
    top = ax.secondary_xaxis("top", functions=(lambda x: x, lambda x: x))
    tc = np.array([800, 600, 400, 300, 200, 100, 25])
    top.set_xticks(1000 / (tc + 273.15))
    top.set_xticklabels([str(t) for t in tc])
    top.set_xlabel("Temperature (°C)")
    ax.spines["top"].set_visible(True)
    save(fig, "25", "fig-25-7-ionic-conductivity-arrhenius")


# --------------------------------------------------------------------------- 25.3


if __name__ == "__main__":
    resistivity_spectrum()
    matthiessen()
    nordheim()
    holm()
    size_effect()
    percolation()
    ionic_arrhenius()
