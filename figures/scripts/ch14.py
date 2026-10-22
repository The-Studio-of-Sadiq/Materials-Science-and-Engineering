"""Figures for Chapter 14 — Creep, Viscoelasticity and Fracture.

Run from the repository root:  python figures/scripts/ch14.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle
from matplotlib.colors import ListedColormap

from figstyle import new_fig, save, COLORS, INK, GRID


# ---------------------------------------------------------------------------
# 14.1 Larson–Miller master curves
# ---------------------------------------------------------------------------
def _lm_curve(P, P1, s1, P2, s2, bulge=0.10):
    """log-stress quadratic through (P1,s1),(P2,s2), concave down by `bulge` decades mid-way."""
    l1, l2 = np.log10(s1), np.log10(s2)
    lin = l1 + (l2 - l1) * (P - P1) / (P2 - P1)
    c = -bulge / ((P2 - P1) / 2) ** 2
    return 10 ** (lin + c * (P - P1) * (P - P2))


def larson_miller():
    fig, ax = new_fig(6.4, 4.3)
    curves = [("2.25Cr–1Mo", 17000, 300, 22500, 30, COLORS[0]),
              ("Grade 91 (9Cr–1Mo–V–Nb)", 18000, 350, 24000, 50, COLORS[1]),
              ("316 stainless", 18000, 300, 24500, 30, COLORS[2]),
              ("single-crystal Ni superalloy", 22000, 900, 29000, 100, COLORS[3])]
    lab_pos = {"2.25Cr–1Mo": (16150, 345, "left"),
               "Grade 91 (9Cr–1Mo–V–Nb)": (18000, 400, "left"),
               "316 stainless": (24650, 27, "left"),
               "single-crystal Ni superalloy": (23300, 420, "left")}
    for name, P1, s1, P2, s2, c in curves:
        P = np.linspace(P1, P2, 200)
        ax.plot(P, _lm_curve(P, P1, s1, P2, s2), color=c, lw=2.0)
        x, y, ha = lab_pos[name]
        ax.text(x, y, name, color=c, fontsize=8.5, ha=ha, va="center")
    # worked example on 2.25Cr-1Mo
    Pw = 923.15 * 23
    sw = _lm_curve(np.array([Pw]), 17000, 300, 22500, 30)[0]
    ax.plot([Pw, Pw], [10, sw], color=COLORS[0], lw=0.8, ls=":")
    ax.plot([16000, Pw], [sw, sw], color=COLORS[0], lw=0.8, ls=":")
    ax.plot(Pw, sw, "o", ms=7, mfc="white", mec=COLORS[0], mew=1.8, zorder=5)
    ax.annotate("rupture test 650 °C / 1000 h:\nLMP = 21 232\n≡ 600 °C / 2.08×10$^4$ h\n"
                "≡ 550 °C / 6.2×10$^5$ h", xy=(Pw, sw), xytext=(16300, 11.5), fontsize=8.5, va="bottom",
                color=INK, arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.8, mutation_scale=9))
    ax.set_yscale("log")
    ax.set_xlim(16000, 30000)
    ax.set_ylim(10, 1000)
    ax.set_yticks([10, 20, 50, 100, 200, 500, 1000])
    ax.set_yticklabels(["10", "20", "50", "100", "200", "500", "1000"])
    ax.set_xlabel("Larson–Miller parameter  LMP = $T\\,(20+\\log_{10}t_r)$   ($T$ in K, $t_r$ in h)")
    ax.set_ylabel("Rupture stress (MPa)")
    # top axis: rupture time at 565 C
    T565 = 838.15
    sec = ax.secondary_xaxis("top", functions=(lambda v: v, lambda v: v))
    tt = [1, 10, 100, 1e3, 1e4, 1e5, 1e6]
    sec.set_xticks([T565 * (20 + np.log10(t)) for t in tt])
    sec.set_xticklabels(["1", "10", "10$^2$", "10$^3$", "10$^4$", "10$^5$", "10$^6$"], fontsize=8.5)
    sec.set_xlabel("rupture time at 565 °C (h)", fontsize=9)
    ax.spines["top"].set_visible(True)
    save(fig, "14", "fig-14-1-larson-miller")


# ---------------------------------------------------------------------------
# 14.2 Deformation-mechanism map for nickel
# ---------------------------------------------------------------------------
NI = dict(Tm=1728.0, mu0=7.89e4, dmu=-0.64, b=2.49e-10, Om=1.09e-29, D0v=1.9e-4, Qv=284e3,
          dDb0=3.5e-15, Qb=115e3, acDc0=3.1e-23, Qc=170e3, n=4.6, A=3.0e6, tau_hat=2.5e-3, dF=2.0,
          gdot0=1e6, alpha=900.0)
kB, R = 1.380649e-23, 8.314


def _ni_rates(x, s, d):
    """x = T/Tm, s = sigma_s/mu (arrays). Returns dict of shear strain rates (1/s)."""
    p = NI
    T = x * p["Tm"]
    mu = p["mu0"] * 1e6 * (1 + p["dmu"] * (T - 300) / p["Tm"])  # Pa
    Dv = p["D0v"] * np.exp(-p["Qv"] / (R * T))
    dDb = p["dDb0"] * np.exp(-p["Qb"] / (R * T))
    acDc = p["acDc0"] * np.exp(-p["Qc"] / (R * T))
    sig = s * mu
    # diffusional flow (Frost & Ashby form)
    nh = 42 * sig * p["Om"] / (kB * T * d ** 2) * Dv
    cob = 42 * sig * p["Om"] / (kB * T * d ** 2) * np.pi * dDb / d
    # power-law creep with core diffusion and power-law breakdown
    Deff_l = Dv
    Deff_c = 10 * acDc / p["b"] ** 2 * s ** 2
    pre = p["A"] * mu * p["b"] / (kB * T) * (np.sinh(p["alpha"] * s) / p["alpha"]) ** p["n"]
    plc_l = pre * Deff_l
    plc_c = pre * Deff_c
    # obstacle-controlled glide
    dF = p["dF"] * mu * p["b"] ** 3
    arg = np.clip(1 - s / p["tau_hat"], 0, None)
    glide = p["gdot0"] * np.exp(-dF / (kB * T) * arg)
    return dict(glide=glide, plc_l=plc_l, plc_c=plc_c, nh=nh, coble=cob)


def _map(ax, d, small=False):
    x = np.linspace(0.005, 1.0, 500)
    ls = np.linspace(-6, -1, 500)
    X, LS = np.meshgrid(x, ls)
    S = 10 ** LS
    r = _ni_rates(X, S, d)
    plc = r["plc_l"] + r["plc_c"]
    stack = np.stack([r["glide"], plc, r["coble"], r["nh"]])
    dom = np.argmax(stack, axis=0).astype(float)
    tot = np.maximum(r["glide"], plc) + r["coble"] + r["nh"]
    dom[S > 0.05] = 4  # ideal strength
    fills = ["#F3D9C9", "#D6E6F4", "#DCEFD9", "#F6EBC6", "#E3E3E3"]
    ax.contourf(X, LS, dom, levels=[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5], colors=fills)
    ax.contour(X, LS, dom, levels=[0.5, 1.5, 2.5, 3.5], colors=INK, linewidths=1.3)
    # elastic region hatch
    ax.contourf(X, LS, np.log10(tot), levels=[-60, -10], colors="none", hatches=["....."])
    # core / lattice split
    if not small:
        ratio = r["plc_c"] / np.maximum(r["plc_l"], 1e-300)
        m = (dom == 1)
        rr = np.where(m, np.log10(ratio), np.nan)
        ax.contour(X, LS, rr, levels=[0], colors=INK, linewidths=0.9, linestyles="--")
    levels = [-10, -8, -6, -4, -2]
    cs = ax.contour(X, LS, np.log10(tot), levels=levels, colors=COLORS[0], linewidths=0.9)
    if not small:
        fmt = {lv: f"10$^{{{lv}}}$ s$^{{-1}}$" for lv in levels}
        # label each contour where it leaves the map (right edge, else bottom edge)
        def ltot(px, py):
            rr_ = _ni_rates(px, 10 ** py, d)
            return np.log10(np.maximum(rr_["glide"], rr_["plc_l"] + rr_["plc_c"]) + rr_["coble"] + rr_["nh"])
        yy = np.linspace(-5.95, -2.7, 600)
        lr = ltot(np.full_like(yy, 0.995), yy)
        xx = np.linspace(0.3, 0.995, 600)
        lb = ltot(xx, np.full_like(xx, -5.95))
        for lv in levels:
            if lr.min() < lv < lr.max():
                yv = np.interp(lv, lr, yy)
                ax.text(0.99, yv + 0.07, fmt[lv], fontsize=7, color=COLORS[0], ha="right", va="bottom",
                        bbox=dict(fc="white", ec="none", pad=0.5, alpha=0.8))
            else:
                xv = np.interp(lv, lb, xx)
                ax.text(xv + 0.01, -5.9, fmt[lv], fontsize=7, color=COLORS[0], ha="left", va="bottom",
                        rotation=0)
    ax.set_xlim(0, 1)
    ax.set_ylim(-6, -1)
    return dom


def deformation_map():
    fig = plt.figure(figsize=(6.8, 4.8))
    ax = fig.add_axes([0.10, 0.11, 0.56, 0.74])
    _map(ax, 100e-6)
    ax.set_xlabel("Homologous temperature $T/T_m$")
    ax.set_ylabel("Normalized shear stress $\\sigma_s/G$")
    ax.set_yticks([-6, -5, -4, -3, -2, -1])
    ax.set_yticklabels(["10$^{-6}$", "10$^{-5}$", "10$^{-4}$", "10$^{-3}$", "10$^{-2}$", "10$^{-1}$"])
    # field labels
    kw = dict(fontsize=8.5, ha="center", va="center", color=INK)
    ax.text(0.35, -1.15, "ideal strength", **kw)
    ax.text(0.17, -2.2, "dislocation glide\n(plasticity)", **kw)
    ax.text(0.44, -2.95, "power-law creep\n(core diffusion)", fontsize=8, ha="center", color=INK)
    ax.text(0.86, -2.95, "power-law\ncreep\n(lattice\ndiffusion)", fontsize=8, ha="center", va="center",
            color=INK)
    ax.text(0.66, -5.2, "Coble creep", **kw)
    ax.text(0.92, -5.5, "N–H\ncreep", **kw)
    ax.text(0.20, -4.6, "elastic\n($\\dot\\gamma<10^{-10}$ s$^{-1}$)", fontsize=8.5, ha="center",
            va="center", color=INK, bbox=dict(fc="white", ec="none", pad=1.5))
    # worked example point
    x0 = 1400 / NI["Tm"]
    Gt = NI["mu0"] * (1 + NI["dmu"] * (1400 - 300) / NI["Tm"])
    s0 = (10 / np.sqrt(3)) / Gt
    ax.plot(x0, np.log10(s0), "o", ms=7, mfc="white", mec=COLORS[1], mew=1.8, zorder=6)
    ax.annotate("worked example:\n1400 K, $\\sigma$ = 10 MPa", xy=(x0, np.log10(s0)), xytext=(0.47, -4.35),
                fontsize=8, color=COLORS[1], bbox=dict(fc="white", ec="none", pad=1),
                arrowprops=dict(arrowstyle="-", color=COLORS[1], lw=0.8))
    # turbine blade box (100-300 MPa at 850-1000 C)
    ax.add_patch(Rectangle((0.65, np.log10(1.1e-3)), 0.09, np.log10(3.3e-3) - np.log10(1.1e-3),
                           fc=COLORS[1], alpha=0.35, ec=COLORS[1], lw=1.2, zorder=5))
    ax.text(0.695, np.log10(3.3e-3) + 0.08, "turbine\nblade", fontsize=7.5, ha="center", va="bottom",
            color=COLORS[1], fontweight="bold", zorder=6)
    ax.set_title("Pure Ni, $d$ = 100 μm", fontsize=10, pad=34)
    # top axis in C
    sec = ax.secondary_xaxis("top", functions=(lambda v: v * NI["Tm"] - 273.15,
                                                lambda v: (v + 273.15) / NI["Tm"]))
    sec.set_xticks([-273, 0, 400, 800, 1200, 1455])
    sec.tick_params(labelsize=8)
    sec.set_xlabel("Temperature (°C)", fontsize=9)
    # right axis in MPa at RT modulus
    sec2 = ax.secondary_yaxis("right", functions=(lambda v: v + np.log10(79e3),
                                                   lambda v: v - np.log10(79e3)))
    mp = [0.1, 1, 10, 100, 1000]
    sec2.set_yticks(np.log10(mp))
    sec2.set_yticklabels(["0.1", "1", "10", "100", "1000"], fontsize=8)
    sec2.set_ylabel("Shear stress at $G$ = 79 GPa (MPa)", fontsize=9)
    ax.spines["top"].set_visible(True)
    ax.spines["right"].set_visible(True)
    # inset: d = 1 um
    axi = fig.add_axes([0.80, 0.50, 0.19, 0.30])
    _map(axi, 1e-6, small=True)
    axi.set_title("$d$ = 1 μm", fontsize=8.5)
    axi.tick_params(labelsize=7)
    axi.set_xticks([0, 0.5, 1])
    axi.set_yticks([-6, -4, -2])
    axi.set_yticklabels(["10$^{-6}$", "10$^{-4}$", "10$^{-2}$"])
    axi.set_xlabel("$T/T_m$", fontsize=7.5, labelpad=1)
    axi.text(0.62, -5.0, "Coble", fontsize=7.5, ha="center", color=INK)
    axi.text(0.35, -2.0, "glide", fontsize=7, ha="center", color=INK)
    for sp in ["top", "right"]:
        axi.spines[sp].set_visible(True)
    fig.text(0.80, 0.33, "Finer grains expand the\nCoble field: diffusional\nflow takes over up to\n"
             "much higher stresses.\n\nContours: total shear\nstrain rate.", fontsize=7.5, color=INK,
             va="top")
    save(fig, "14", "fig-14-2-deformation-map")


# ---------------------------------------------------------------------------
# 14.3 Viscoelastic models
# ---------------------------------------------------------------------------
def _spring(ax, x, y0, y1, w=0.18, n=6, color=INK):
    L = y1 - y0
    lead = 0.18 * L
    ys = np.linspace(y0 + lead, y1 - lead, 2 * n + 1)
    xs = np.r_[x, x + w * np.array([0] + [(-1) ** i for i in range(1, 2 * n)] + [0]), x]
    ys = np.r_[y0, ys, y1]
    ax.plot(xs, ys, color=color, lw=1.3)


def _dashpot(ax, x, y0, y1, w=0.22, color=INK):
    L = y1 - y0
    yc0, yc1 = y0 + 0.25 * L, y0 + 0.75 * L
    ax.plot([x, x], [y0, yc0], color=color, lw=1.3)
    ax.plot([x - w, x - w, x + w, x + w], [yc1, yc0, yc0, yc1], color=color, lw=1.3)
    yp = y0 + 0.55 * L
    ax.plot([x - 0.75 * w, x + 0.75 * w], [yp, yp], color=color, lw=2.0)
    ax.plot([x, x], [yp, y1], color=color, lw=1.3)


def _plate(ax, x0, x1, y):
    ax.plot([x0, x1], [y, y], color=INK, lw=2.2)


def viscoelastic_models():
    fig = plt.figure(figsize=(6.8, 5.4))
    titles = ["Maxwell", "Kelvin–Voigt", "Standard linear solid"]
    for i, t in enumerate(titles):
        a = fig.add_axes([0.06 + i * 0.32, 0.70, 0.26, 0.27])
        a.set_xlim(-1.4, 1.4)
        a.set_ylim(-0.2, 3.4)
        a.set_aspect("equal")
        a.axis("off")
        a.set_title(t, fontsize=9.5, color=COLORS[i], pad=2)
        if i == 0:
            _plate(a, -0.4, 0.4, 0.0)
            _spring(a, 0, 0.0, 1.5)
            _dashpot(a, 0, 1.5, 3.0)
            _plate(a, -0.4, 0.4, 3.0)
            a.text(0.35, 0.75, "$E$", fontsize=9)
            a.text(0.35, 2.25, "$\\eta$", fontsize=9)
        elif i == 1:
            _plate(a, -0.8, 0.8, 0.0)
            _plate(a, -0.8, 0.8, 3.0)
            _spring(a, -0.5, 0.0, 3.0)
            _dashpot(a, 0.5, 0.0, 3.0)
            a.text(-1.15, 1.5, "$E$", fontsize=9, va="center")
            a.text(0.85, 1.5, "$\\eta$", fontsize=9, va="center")
        else:
            _plate(a, -0.9, 0.9, 0.0)
            _plate(a, -0.9, 0.9, 3.0)
            _spring(a, -0.55, 0.0, 3.0)
            _spring(a, 0.55, 0.0, 1.5)
            _dashpot(a, 0.55, 1.5, 3.0)
            a.text(-1.25, 1.5, "$E_R$", fontsize=9, va="center")
            a.text(0.85, 0.75, "$E_U-E_R$", fontsize=8, va="center")
            a.text(0.85, 2.25, "$\\eta$", fontsize=9, va="center")
        a.annotate("", xy=(0, 3.35), xytext=(0, 3.0),
                   arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.0, mutation_scale=8))
        a.text(0.12, 3.25, "$\\sigma$", fontsize=8.5, va="center")

    # creep
    ax = fig.add_axes([0.08, 0.09, 0.40, 0.50])
    t = np.linspace(0, 6, 1200)
    t1 = 3.0
    on = t < t1
    # Maxwell (E, tau = eta/E): eps E/s0
    mx = np.where(on, 1 + t, t1)
    kv = np.where(on, 1 - np.exp(-t), (1 - np.exp(-t1)) * np.exp(-(t - t1)))
    EU, ER = 2.5, 1.0
    tc = EU / ER  # creep retardation time in units of the relaxation time
    sls_on = 1 / ER - (1 / ER - 1 / EU) * np.exp(-t / tc)
    e1 = 1 / ER - (1 / ER - 1 / EU) * np.exp(-t1 / tc)
    sls_off = (e1 - 1 / EU) * np.exp(-(t - t1) / tc)
    sls = np.where(on, sls_on, sls_off) * EU  # normalized by sigma0/EU
    ax.plot(t, mx, color=COLORS[0], label="Maxwell")
    ax.plot(t, kv, color=COLORS[1], label="Kelvin–Voigt")
    ax.plot(t, sls, color=COLORS[2], label="SLS ($E=E_U$)")
    ax.axvline(t1, color=GRID, lw=0.9, ls="--", zorder=0)
    ax.text(t1 + 0.08, 3.95, "load removed", fontsize=7.5, va="top", color=INK)
    ax.axhline(EU / ER, color=COLORS[2], lw=0.7, ls=":")
    ax.text(0.05, EU / ER + 0.06, "$\\sigma_0/E_R$", fontsize=8, color=COLORS[2])
    ax.text(4.5, 1.15, "SLS retardation\ntime $(E_U/E_R)\\tau$", fontsize=7.5, color=COLORS[2], ha="center")
    ax.text(5.95, 3.08, "permanent\nstrain", fontsize=7.5, ha="right", va="bottom", color=COLORS[0])
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 4.2)
    ax.set_xlabel("$t/\\tau$")
    ax.set_ylabel("$\\varepsilon E/\\sigma_0$")
    ax.set_title("Creep under constant $\\sigma_0$, removed at $t/\\tau=3$", fontsize=9)
    ax.legend(loc="center right", fontsize=8, bbox_to_anchor=(1.0, 0.55))

    # relaxation
    ax = fig.add_axes([0.58, 0.09, 0.40, 0.50])
    t = np.linspace(0, 5, 600)
    ax.plot(t, np.exp(-t), color=COLORS[0], label="Maxwell → 0")
    sls_r = (ER + (EU - ER) * np.exp(-t)) / EU
    ax.plot(t, sls_r, color=COLORS[2], label="SLS → $E_R/E_U$ = 0.4")
    ax.axhline(0.4, color=COLORS[2], lw=0.7, ls=":")
    ax.text(4.95, 0.62, "Kelvin–Voigt: cannot relax\n(instantaneous strain step\nwould need infinite force)",
            fontsize=7.5, ha="right", va="bottom", color=COLORS[1])
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel("$t/\\tau$")
    ax.set_ylabel("$\\sigma/(E_U\\varepsilon_0)$")
    ax.set_title("Stress relaxation at constant $\\varepsilon_0$", fontsize=9)
    ax.legend(loc="upper right", fontsize=8)
    ax.text(0.98, 0.22, "clip example: $E_U$ = 2.5 GPa,\n$E_R$ = 1.0 GPa; 25 → 10 MPa",
            transform=ax.transAxes, fontsize=7.5, ha="right", color=INK)
    save(fig, "14", "fig-14-3-viscoelastic-models")


# ---------------------------------------------------------------------------
# 14.4 Crack-tip field
# ---------------------------------------------------------------------------
def _mode_block(a, y0, kind):
    w, h = 2.4, 1.1
    x0 = 0.0
    a.add_patch(Rectangle((x0, y0), w, h, fc="#EEF3F8", ec=INK, lw=1.0))
    yc = y0 + h / 2
    if kind == "I":
        a.add_patch(Polygon([[x0, yc + 0.12], [x0 + 1.2, yc], [x0, yc - 0.12]], fc="white", ec=INK, lw=0.9))
        for yy, dy in [(y0 + h, 0.35), (y0, -0.35)]:
            a.annotate("", xy=(0.6, yy + dy), xytext=(0.6, yy),
                       arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.2, mutation_scale=8))
        lab = "Mode I\nopening"
    elif kind == "II":
        a.plot([x0, x0 + 1.2], [yc, yc], color=INK, lw=1.4)
        a.annotate("", xy=(0.15, yc + 0.28), xytext=(0.85, yc + 0.28),
                   arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.2, mutation_scale=8))
        a.annotate("", xy=(0.85, yc - 0.28), xytext=(0.15, yc - 0.28),
                   arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.2, mutation_scale=8))
        lab = "Mode II\nsliding"
    else:
        a.plot([x0, x0 + 1.2], [yc, yc], color=INK, lw=1.4)
        a.plot(0.55, yc + 0.28, "o", ms=7, mfc="white", mec=COLORS[1], mew=1.2)
        a.plot(0.55, yc + 0.28, "o", ms=2, color=COLORS[1])
        a.plot(0.55, yc - 0.28, "x", ms=6, color=COLORS[1], mew=1.3)
        a.add_patch(Circle((0.55, yc - 0.28), 0.12, fc="none", ec=COLORS[1], lw=1.0))
        lab = "Mode III\ntearing\n(out of plane)"
    a.plot(x0 + 1.2, yc, "o", ms=2.5, color=INK)
    a.text(w + 0.15, yc, lab, fontsize=7.5, va="center", ha="left")


def crack_tip_field():
    fig = plt.figure(figsize=(6.8, 3.4))
    a = fig.add_axes([0.0, 0.05, 0.20, 0.88])
    a.set_xlim(-0.1, 4.2)
    a.set_ylim(-0.4, 6.2)
    a.set_aspect("equal")
    a.axis("off")
    for y0, k in [(4.4, "I"), (2.2, "II"), (0.0, "III")]:
        _mode_block(a, y0, k)

    # centre: stress ahead of crack
    ax = fig.add_axes([0.30, 0.17, 0.33, 0.72])
    K, sy = 26.0, 500.0
    r = np.linspace(0.005, 2.0, 600)  # mm
    sel = K / np.sqrt(2 * np.pi * r * 1e-3)
    ax.plot(r, sel, color=INK, lw=1.3, ls="--", label="elastic $K/\\sqrt{2\\pi r}$")
    ry_ps = (K / sy) ** 2 / (2 * np.pi) * 1e3
    s_pe = np.sqrt(3) * sy
    ry_pe = (K / s_pe) ** 2 / (2 * np.pi) * 1e3
    ax.plot(np.r_[0, ry_ps, r[r > ry_ps]], np.r_[sy, sy, sel[r > ry_ps]], color=COLORS[0], lw=2,
            label="plane stress (cap $\\sigma_y$)")
    ax.plot(np.r_[0, ry_pe], [s_pe, s_pe], color=COLORS[1], lw=2, label="plane strain (cap ≈ $\\sqrt{3}\\sigma_y$)")
    ax.axvspan(0, ry_ps, color=COLORS[0], alpha=0.10, lw=0)
    ax.axvspan(0, ry_pe, color=COLORS[1], alpha=0.12, lw=0)
    ax.annotate(f"$r_p$ = {ry_ps:.2f} mm\n(plane stress)", xy=(ry_ps, sy), xytext=(0.75, 560),
                fontsize=7.5, color=COLORS[0], arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[0]))
    ax.annotate(f"$r_p$ = {ry_pe:.2f} mm\n(plane strain)", xy=(ry_pe, s_pe), xytext=(0.45, 930),
                fontsize=7.5, color=COLORS[1], arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[1]))
    ax.annotate("", xy=(2.0, 120), xytext=(0.9, 120),
                arrowprops=dict(arrowstyle="<|-|>", lw=0.8, color=INK, mutation_scale=7))
    ax.text(1.45, 140, "K-dominated zone", fontsize=7.5, ha="center", va="bottom")
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 1600)
    ax.set_xlabel("Distance ahead of tip $r$ (mm)")
    ax.set_ylabel("$\\sigma_{yy}$ (MPa)")
    ax.set_title("$K$ = 26 MPa m$^{1/2}$, $\\sigma_y$ = 500 MPa", fontsize=8.5)
    ax.legend(loc="upper right", fontsize=7, handlelength=1.6)

    # right: Kc vs thickness (Irwin)
    ax = fig.add_axes([0.73, 0.17, 0.26, 0.72])
    KIc = 26.0
    B = np.linspace(1.5, 30, 300)
    beta = (KIc / sy) ** 2 * 1e3 / B
    Kc = KIc * np.sqrt(1 + 1.4 * beta ** 2)
    ax.plot(B, Kc, color=COLORS[0], lw=2)
    ax.axhline(KIc, color=INK, lw=0.8, ls=":")
    Bc = 2.5 * (KIc / sy) ** 2 * 1e3
    ax.axvline(Bc, color=COLORS[1], lw=0.9, ls="--")
    ax.text(Bc + 0.8, 62, f"$B$ = {Bc:.1f} mm", fontsize=7.5, color=COLORS[1], va="top")
    ax.text(29.5, 29, "plane strain:\n$B\\geq2.5(K_{Ic}/\\sigma_y)^2$\n$K_{Ic}$ = 26 MPa m$^{1/2}$",
            fontsize=7.5, ha="right", va="bottom")
    ax.text(3, 52, "mixed / plane\nstress", fontsize=7.5, ha="left", va="center")
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 65)
    ax.set_xlabel("Thickness $B$ (mm)")
    ax.set_ylabel("Apparent $K_c$ (MPa m$^{1/2}$)")
    ax.set_title("7075-T651", fontsize=8.5)
    save(fig, "14", "fig-14-4-crack-tip-field")


# ---------------------------------------------------------------------------
# 14.5 Charpy transition
# ---------------------------------------------------------------------------
def _tanh_curve(T, LS, US, T_at, E_at, C):
    # E = LS + (US-LS)/2 (1+tanh((T-T0)/C)), with E(T_at) = E_at
    u = 2 * (E_at - LS) / (US - LS) - 1
    T0 = T_at - C * np.arctanh(u)
    return LS + (US - LS) / 2 * (1 + np.tanh((T - T0) / C)), T0


def charpy_transition():
    fig = plt.figure(figsize=(6.8, 4.0))
    ax = fig.add_axes([0.09, 0.13, 0.64, 0.80])
    T = np.linspace(-200, 100, 600)
    cm, _ = _tanh_curve(T, 5, 150, 0, 27, 25)
    fg, _ = _tanh_curve(T, 5, 200, -50, 27, 25)
    # T41 of fine-grained steel
    T41_fg = T[np.argmin(np.abs(fg - 41))]
    irr, _ = _tanh_curve(T, 5, 120, T41_fg + 80, 41, 28)
    ni9, _ = _tanh_curve(T, 10, 150, -210, 27, 28)
    ss = 250 - 25 * np.exp((-200 - T) / 120) * 0 - 0.08 * (100 - T) * 0.3
    ax.plot(T, ss, color=COLORS[3], label="304 austenitic (FCC, no transition)")
    ax.plot(T, ni9, color=COLORS[4], label="9 % Ni steel")
    ax.plot(T, fg, color=COLORS[2], label="fine-grained normalized C–Mn")
    ax.plot(T, cm, color=COLORS[0], label="plain C–Mn, coarse grain")
    ax.plot(T, irr, color=COLORS[1], ls="-.", label="fine-grained steel after irradiation")
    ax.axhline(27, color=INK, lw=0.8, ls="--")
    ax.text(97, 29, "27 J", fontsize=8, ha="right", va="bottom")
    ax.axhline(41, color=GRID, lw=0.8, ls=":")
    ax.text(97, 43, "41 J", fontsize=8, ha="right", va="bottom", color="#888888")
    T41_irr = T[np.argmin(np.abs(irr - 41))]
    ax.annotate("", xy=(T41_irr, 41), xytext=(T41_fg, 41),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=1.4, mutation_scale=10))
    ax.text((T41_fg + T41_irr) / 2, 47, "$\\Delta T_{41J}$ ≈ 80 °C\n(Ch 33)", fontsize=8,
            color=COLORS[1], ha="center", va="bottom")
    ax.annotate("", xy=(30, 120), xytext=(30, 200),
                arrowprops=dict(arrowstyle="-|>", color=COLORS[1], lw=0.9, mutation_scale=8))
    ax.text(33, 160, "upper shelf\nreduced", fontsize=7.5, color=COLORS[1], va="center")
    ax.axvline(-196, color=GRID, lw=0.8)
    ax.text(-194, 290, "−196 °C\n(LN$_2$)", fontsize=7.5, va="top")
    ax.set_xlim(-200, 100)
    ax.set_ylim(0, 300)
    ax.set_xlabel("Test temperature (°C)")
    ax.set_ylabel("Charpy V-notch energy (J)")
    ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1.0), fontsize=8)

    # fracture surface sketches
    rng = np.random.default_rng(5)
    a1 = fig.add_axes([0.755, 0.25, 0.10, 0.17])
    a1.set_xlim(0, 1); a1.set_ylim(0, 1); a1.set_aspect("equal"); a1.set_xticks([]); a1.set_yticks([])
    a1.set_facecolor("#D9D9D9")
    for _ in range(45):
        x, y = rng.random(2)
        r = 0.03 + 0.04 * rng.random()
        a1.add_patch(Circle((x, y), r, fc="#BDBDBD", ec="#6E6E6E", lw=0.6))
        a1.add_patch(Circle((x - 0.25 * r, y + 0.25 * r), 0.35 * r, fc="#F2F2F2", ec="none"))
    a1.set_title("fibrous\n(ductile, dimples)", fontsize=7, pad=2)
    a2 = fig.add_axes([0.885, 0.25, 0.10, 0.17])
    a2.set_xlim(0, 1); a2.set_ylim(0, 1); a2.set_aspect("equal"); a2.set_xticks([]); a2.set_yticks([])
    a2.set_facecolor("#9A9A9A")
    pts = rng.random((22, 2))
    from scipy.spatial import Voronoi
    vor = Voronoi(np.r_[pts, [[-1, -1], [-1, 2], [2, -1], [2, 2]]])
    for i, reg in enumerate(vor.point_region[:22]):
        verts = vor.regions[reg]
        if -1 in verts or len(verts) == 0:
            continue
        poly = np.clip(vor.vertices[verts], 0, 1)
        g = 0.55 + 0.4 * rng.random()
        a2.add_patch(Polygon(poly, fc=(g, g, g), ec="#555555", lw=0.6))
        cx, cy = pts[i]
        ang = rng.random() * np.pi
        for k in (-1, 0, 1):
            dx, dy = 0.05 * np.cos(ang), 0.05 * np.sin(ang)
            ox, oy = -0.02 * k * np.sin(ang), 0.02 * k * np.cos(ang)
            a2.plot([cx - dx + ox, cx + dx + ox], [cy - dy + oy, cy + dy + oy], color="#777777", lw=0.4)
    a2.set_title("crystalline\n(cleavage facets)", fontsize=7, pad=2)
    save(fig, "14", "fig-14-5-charpy-transition")


# ---------------------------------------------------------------------------
# 14.6 Paris law
# ---------------------------------------------------------------------------
def _dadn(dK, C, m, dKth, dKc, p=6.0, q=0.5):
    core = C * dK ** m
    thr = np.clip(1 - (dKth / dK) ** p, 1e-12, None)
    fin = np.clip(1 - dK / dKc, 1e-6, None) ** q
    return core * thr / fin


def paris_law():
    fig, ax = new_fig(6.4, 4.4)
    C, m = 6.9e-12, 3.0
    dK = np.logspace(0, 2, 800)
    st = (dK > 7.0) & (dK < 89.5)
    y = _dadn(dK[st], C, m, 7.0, 90.0)
    ax.plot(dK[st], y, color=COLORS[0], lw=2.0, label="ferritic steel, $R$ = 0.1")
    st7 = (dK > 3.0) & (dK < 29.8)
    y7 = _dadn(dK[st7], 1.6 * C, m, 3.0, 30.0)
    ax.plot(dK[st7], y7, color=COLORS[0], lw=1.6, ls="--", label="ferritic steel, $R$ = 0.7")
    al = (dK > 2.5) & (dK < 34.8)
    ya = _dadn(dK[al], 30 * C, m, 2.5, 35.0)
    ax.plot(dK[al], ya, color=COLORS[1], lw=2.0, label="Al 2024-T3, $R$ = 0.1")
    # Paris line for steel (thin)
    pl = (dK > 5) & (dK < 100)
    ax.plot(dK[pl], C * dK[pl] ** m, color=COLORS[0], lw=0.7, ls=":")
    # worked-example marks
    for k, lab in [(8.9, "8.9 MPa m$^{1/2}$: 4.8×10$^{-9}$ m/cycle\n(crane-hook example, on Paris line)"),
                   (10.0, None)]:
        ax.plot(k, C * k ** m, "o", ms=5.5, mfc="white", mec=COLORS[0], mew=1.5, zorder=5)
    ax.annotate("Paris line $C$ = 6.9×10$^{-12}$, $m$ = 3:\n8.9 MPa m$^{1/2}$ → 4.8×10$^{-9}$ m/cycle (worked example)\n"
                "10 MPa m$^{1/2}$ → 6.9×10$^{-9}$ m/cycle",
                xy=(8.9, C * 8.9 ** 3), xytext=(11.5, 4e-11), fontsize=7.5, va="bottom", color=COLORS[0],
                arrowprops=dict(arrowstyle="-", lw=0.7, color=COLORS[0]))
    # threshold markers
    for k, c, ls_ in [(7.0, COLORS[0], "-"), (3.0, COLORS[0], "--"), (2.5, COLORS[1], "-")]:
        ax.plot([k, k], [1e-11, 3e-11], color=c, lw=1.4, ls=ls_)
    ax.text(7.25, 1.6e-11, "$\\Delta K_{th}$ ≈ 7", fontsize=7.5, color=COLORS[0], va="center")
    ax.text(3.15, 2.2e-11, "≈ 3", fontsize=7.5, color=COLORS[0], ha="left")
    ax.text(2.5, 1.6e-11, "≈ 2.5 ", fontsize=7.5, color=COLORS[1], ha="right", va="center")
    # regime labels
    ax.text(1.6, 3e-6, "I\nthreshold", fontsize=9, ha="center", va="top", fontweight="bold", color=INK)
    ax.text(32, 2.5e-9, "II\nParis", fontsize=9, ha="center", va="top", fontweight="bold",
            color=INK)
    ax.text(75, 2.5e-9, "III\nfinal\nfracture", fontsize=9, ha="center", va="top", fontweight="bold",
            color=INK)
    ax.text(85, 1.1e-7, "$K_{max}\\to K_c$", fontsize=7.5, color=COLORS[0], ha="right")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1, 100)
    ax.set_ylim(1e-11, 1e-5)
    ax.set_xticks([1, 2, 5, 10, 20, 50, 100])
    ax.set_xticklabels(["1", "2", "5", "10", "20", "50", "100"])
    ax.set_xlabel("Stress-intensity range $\\Delta K$ (MPa m$^{1/2}$)")
    ax.set_ylabel("Crack growth rate $da/dN$ (m/cycle)")
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 0.84), fontsize=8)
    ax.text(1.05, 3e-10, "higher $R$: less\ncrack closure →\nlower threshold,\nfaster growth",
            fontsize=7, color=COLORS[0])
    save(fig, "14", "fig-14-6-paris-law")


if __name__ == "__main__":
    larson_miller()
    deformation_map()
    viscoelastic_models()
    crack_tip_field()
    charpy_transition()
    paris_law()
