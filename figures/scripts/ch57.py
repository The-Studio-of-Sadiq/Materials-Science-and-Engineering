"""Figures for Chapter 57 — Materials Informatics.

Run from the repository root:  python figures/scripts/ch57.py
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, box, arrow, save, COLORS, INK  # noqa: E402,F401
import numpy as np  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon, FancyArrowPatch  # noqa: E402
from scipy.stats import norm  # noqa: E402

BLUE, VERM, GREEN, PINK, ORANGE, SKY = COLORS[:6]


# ---------------------------------------------------------------- Figure 57.1
def database_workflow_convex_hull():
    fig = plt.figure(figsize=(6.8, 4.3))
    axL = fig.add_axes([0.0, 0.0, 0.47, 1.0])
    axR = fig.add_axes([0.58, 0.13, 0.40, 0.80])

    # --- left: workflow
    axL.set_xlim(0, 10)
    axL.set_ylim(0, 10)
    axL.axis("off")
    steps = [
        "Structure source\n(ICSD, prototype substitution)",
        "Standardized DFT relaxation\n(fixed functional, cutoff, k-mesh)",
        "Property calculations\n(energy, bands, elastic, dielectric)",
        "Corrections and validation",
        "Database with provenance\n(API query)",
    ]
    x0, w, h = 0.3, 7.0, 1.35
    ys = [8.35, 6.45, 4.55, 2.65, 0.75]
    fcs = ["#EEF3F8", "#EEF3F8", "#EEF3F8", "#EEF3F8", "#DCEBF7"]
    for yy, t, fc in zip(ys, steps, fcs):
        box(axL, x0, yy, w, h, t, fc=fc, fontsize=8.3)
    for a, b in zip(ys[:-1], ys[1:]):
        arrow(axL, x0 + w / 2, a, x0 + w / 2, b + h)
    # feedback loop on the right
    xr = 8.6
    axL.plot([x0 + w, xr], [ys[4] + h / 2] * 2, color=GREEN, lw=1.2)
    axL.plot([xr, xr], [ys[4] + h / 2, ys[0] + h / 2], color=GREEN, lw=1.2)
    axL.annotate("", xy=(x0 + w, ys[0] + h / 2), xytext=(xr, ys[0] + h / 2),
                 arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.2, mutation_scale=10))
    axL.text(xr + 0.25, 4.9, "ML models trained on the database", rotation=90, ha="left", va="center",
             fontsize=8, color=GREEN)
    axL.text(xr - 0.12, ys[0] + h / 2 - 0.15, "new\ncandidates", ha="right", va="top",
             fontsize=7.3, color=GREEN)

    # --- right: convex hull
    ax = axR
    xA, xAB, xB = 0.0, 0.5, 1.0
    eAB = -0.50
    ax.axhline(0, color="0.6", lw=0.7, zorder=0)
    ax.plot([xA, xAB, xB], [0, eAB, 0], "-", color=INK, lw=1.6, zorder=2, label="original hull")
    ax.plot([xA, xAB, xB], [0, eAB, 0], "o", color=INK, ms=7, zorder=4)
    # AB2 above the hull, AB3 below it (new stable phase) and the rebuilt hull
    x2, e2 = 2 / 3, -0.30
    x3, e3 = 0.75, -0.27
    hull2 = eAB + (x2 - 0.5) / 0.5 * (0 - eAB)
    hull2n = eAB + (x2 - 0.5) / 0.25 * (e3 - eAB)
    ax.plot([xAB, x3, xB], [eAB, e3, 0], ":", color=VERM, lw=1.8, zorder=3, label="rebuilt hull (with AB$_3$)")
    ax.plot(x2, e2, "o", mfc="white", mec=BLUE, mew=1.5, ms=6, zorder=5)
    ax.plot(x3, e3, "*", color=VERM, ms=10, zorder=6)
    ax.text(x2 - 0.03, e2, r"AB$_2$", ha="right", va="center", fontsize=8.5, color=BLUE)
    ax.text(x3 + 0.04, e3 - 0.01, r"AB$_3$", ha="left", va="top", fontsize=8.5, color=VERM)
    # zoom inset
    ins = ax.inset_axes([0.25, 0.55, 0.52, 0.38])
    ins.plot([xAB, xB], [eAB, 0], "-", color=INK, lw=1.4)
    ins.plot([xAB, x3, xB], [eAB, e3, 0], ":", color=VERM, lw=1.8)
    ins.plot(x2, e2, "o", mfc="white", mec=BLUE, mew=1.5, ms=6, zorder=5)
    ins.plot(x3, e3, "*", color=VERM, ms=10, zorder=6)
    ins.annotate("", xy=(x2 - 0.004, hull2 + 0.001), xytext=(x2 - 0.004, e2 - 0.003),
                 arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.0, ls="--", mutation_scale=7, shrinkA=0, shrinkB=0))
    ins.annotate("", xy=(x2 + 0.006, hull2n + 0.001), xytext=(x2 + 0.006, e2 - 0.003),
                 arrowprops=dict(arrowstyle="-|>", color=VERM, lw=1.0, mutation_scale=7, shrinkA=0, shrinkB=0))
    ins.text(x2 - 0.012, (e2 + hull2) / 2, "33", ha="right", va="center", fontsize=7.5, color=BLUE)
    ins.text(x2 - 0.012, hull2n + 0.002, "47", ha="right", va="center", fontsize=7.5, color=VERM)
    ins.plot([x3, x3], [e3, -0.25], color=VERM, lw=0.9)
    ins.plot([x3 - 0.005, x3 + 0.005], [-0.25, -0.25], color=VERM, lw=0.9)
    ins.text(x3 + 0.008, e3 - 0.004, "AB$_3$: 20 below\nold hull", ha="left", va="top", fontsize=6.6,
             color=VERM)
    ins.text(x2 - 0.008, e2 + 0.005, r"AB$_2$", ha="right", va="bottom", fontsize=7, color=BLUE)
    ins.set_xlim(0.60, 0.81)
    ins.set_ylim(-0.365, -0.24)
    ins.set_xticks([])
    ins.set_yticks([])
    for sp in ins.spines.values():
        sp.set_visible(True)
        sp.set_color("0.5")
    ins.set_title(r"zoom: $E_{\rm hull}$ of AB$_2$ (meV/atom)", fontsize=7.0, pad=2)
    ax.indicate_inset_zoom(ins, edgecolor="0.5", lw=0.7)
    ax.text(xA + 0.02, 0.02, "A", ha="left", va="bottom", fontsize=9)
    ax.text(xB - 0.02, 0.02, "B", ha="right", va="bottom", fontsize=9)
    ax.text(xAB, eAB - 0.03, "AB", ha="center", va="top", fontsize=9)
    ax.set_xlim(-0.03, 1.03)
    ax.set_ylim(-0.6, 0.1)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xticklabels(["0\n(A)", "0.25", "0.5", "0.75", "1\n(B)"])
    ax.set_xlabel(r"composition $x_{\rm B}$")
    ax.set_ylabel(r"formation energy $\Delta E_f$ (eV/atom)")
    ax.legend(loc="lower left", fontsize=7.5, handlelength=2.2, bbox_to_anchor=(0.0, 0.0))
    save(fig, "57", "fig-57-1-database-workflow-convex-hull")


# ---------------------------------------------------------------- Figure 57.2
def parity_and_learning_curve():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.8, 3.5), gridspec_kw=dict(wspace=0.38))
    ref = np.array([0.00, 0.45, 1.12, 1.80, 2.35, 3.10, 4.05, 5.60])
    pred = np.array([0.12, 0.30, 1.30, 1.62, 2.61, 2.88, 3.70, 4.95])
    err = pred - ref
    mae = np.mean(np.abs(err))
    r2 = 1 - np.sum(err ** 2) / np.sum((ref - ref.mean()) ** 2)
    xx = np.array([0, 6])
    a1.fill_between(xx, xx - mae, xx + mae, color=BLUE, alpha=0.10, lw=0)
    a1.plot(xx, xx + mae, "--", color=BLUE, lw=0.9)
    a1.plot(xx, xx - mae, "--", color=BLUE, lw=0.9)
    a1.plot(xx, xx, "-", color=INK, lw=1.2)
    a1.plot(ref, pred, "o", color=VERM, ms=6, mec="white", mew=0.6, zorder=4)
    a1.text(0.9, 1.75, f"MAE = {mae:.2f} eV", rotation=45, rotation_mode="anchor", fontsize=8, color=BLUE,
            ha="left", va="bottom", transform_rotates_text=True)
    a1.text(0.15, 5.75, f"$R^2$ = {r2:.2f}\nbias = {err.mean():+.2f} eV".replace("-", "−"), fontsize=8.3,
            va="top")
    a1.annotate("under-predicted:\nsparse data", xy=(4.05, 3.62), xytext=(3.7, 1.15), fontsize=8,
                color=VERM, ha="center", arrowprops=dict(arrowstyle="-|>", color=VERM, lw=0.9))
    a1.annotate("", xy=(5.52, 4.85), xytext=(4.25, 1.55),
                arrowprops=dict(arrowstyle="-|>", color=VERM, lw=0.9))
    a1.set_xlim(0, 6)
    a1.set_ylim(0, 6)
    a1.set_aspect("equal")
    a1.set_xlabel("reference (HSE) band gap (eV)")
    a1.set_ylabel("predicted band gap (eV)")

    N = np.logspace(2, 6, 200)
    # power laws through 0.30 eV/atom at N = 1e3, combined in quadrature with a noise floor
    rf = np.sqrt((0.30 * (N / 1e3) ** -0.2) ** 2 + 0.035 ** 2)
    gnn = np.sqrt((0.30 * (N / 1e3) ** -0.4) ** 2 + 0.015 ** 2)
    a2.loglog(N, rf, color=ORANGE, lw=2, label="composition features\n+ random forest (slope −0.2)")
    a2.loglog(N, gnn, color=BLUE, lw=2, label="graph neural network\n(slope −0.4)")
    a2.axhline(0.1, ls="--", color="0.4", lw=1)
    a2.text(1.2e2, 0.108, "typical DFT vs experiment\ndiscrepancy", fontsize=7.6, color="0.3", va="bottom")
    a2.plot([1e3], [0.30], "o", color=INK, ms=4)
    a2.text(1.1e3, 0.33, "0.30 at 10³", fontsize=7.5, va="bottom")
    a2.text(9e5, rf[-1] * 0.86, f"≈{rf[-1]:.2f}", fontsize=7.5, color=ORANGE, ha="right", va="top")
    a2.text(9e5, gnn[-1] * 0.85, f"≈{gnn[-1]:.3f}", fontsize=7.5, color=BLUE, ha="right", va="top")
    a2.set_xlim(1e2, 1e6)
    a2.set_ylim(0.01, 1)
    a2.set_xlabel("training-set size N")
    a2.set_ylabel("test MAE, formation energy (eV/atom)")
    a2.legend(loc="lower left", fontsize=7.3, handlelength=1.6)
    save(fig, "57", "fig-57-2-parity-and-learning-curve")
    print(f"   parity: MAE={mae:.3f}, R2={r2:.3f}, bias={err.mean():.3f}; RF(1e6)={rf[-1]:.3f}, GNN(1e6)={gnn[-1]:.3f}")


# ---------------------------------------------------------------- Figure 57.3
def screening_funnel():
    fig = plt.figure(figsize=(6.8, 4.6))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 17.4)
    ax.set_ylim(0, 11.5)
    ax.axis("off")
    stages = [
        ("Enumerate", "ICSD + prototype substitution", "cost: —", "100 000"),
        ("Composition rules", "no toxic/scarce elements, charge balance, Li fraction", "cost: ~0", "40 000"),
        ("ML stability", r"universal MLIP relax + GNN $E_{\rm hull}$ < 50 meV/atom", "cost: ~0.1 s", "3 000"),
        ("DFT stability + electrochemical window", "grand-potential phase diagram", "cost: ~200 core-h", "300"),
        ("MLIP/AIMD Li diffusion", "300–900 K, Nernst–Einstein conductivity", r"cost: ~10$^4$ core-h", "30"),
        ("Synthesis and impedance testing", "a handful of survivors", "cost: weeks", "5"),
    ]
    cx, wtop, wbot = 6.0, 5.6, 1.4
    ytop, hb, gap = 10.9, 1.55, 0.18
    shades = ["#DCEBF7", "#C6DDF0", "#AECFEA", "#8FBCE0", "#6AA5D4", "#3F86C2"]
    n = len(stages)
    total = n * hb + (n - 1) * gap
    wid = lambda y: wbot + (wtop - wbot) * (y - (ytop - total)) / total
    band_y = []
    for i, (name, method, cost, num) in enumerate(stages):
        yt = ytop - i * (hb + gap)
        yb = yt - hb
        wt, wb = wid(yt), wid(yb)
        ax.add_patch(Polygon([(cx - wt / 2, yt), (cx + wt / 2, yt), (cx + wb / 2, yb), (cx - wb / 2, yb)],
                             closed=True, fc=shades[i], ec=INK, lw=0.9))
        ax.text(cx, (yt + yb) / 2, num, ha="center", va="center", fontsize=10, fontweight="bold",
                color=INK if i < 4 else "white")
        tx = 9.15
        ax.plot([cx + (wt + wb) / 4 + 0.1, tx - 0.1], [(yt + yb) / 2] * 2, color="0.6", lw=0.6)
        ax.text(tx, (yt + yb) / 2 + 0.28, f"{i + 1}. {name}", ha="left", va="center", fontsize=8.4,
                fontweight="bold")
        ax.text(tx, (yt + yb) / 2 - 0.12, method, ha="left", va="center", fontsize=7.3)
        ax.text(tx, (yt + yb) / 2 - 0.50, cost, ha="left", va="center", fontsize=7.3, color=VERM)
        band_y.append((yt + yb) / 2)
    ax.text(cx, ytop + 0.35, "candidates surviving", ha="center", va="bottom", fontsize=8.3, color="0.3")
    # right-hand arrow
    xa = 17.15
    ax.annotate("", xy=(xa, ytop - total + 0.1), xytext=(xa, ytop - 0.1),
                arrowprops=dict(arrowstyle="-|>", color=VERM, lw=1.6, mutation_scale=14))
    ax.text(xa - 0.2, ytop - total / 2, "accuracy and cost per candidate increase", rotation=90, ha="right",
            va="center", fontsize=8.2, color=VERM)

    # Gaussian inset beside the ML stage
    yml = band_y[2]
    fx0, fy0 = 0.035, (yml - 1.45) / 11.5
    ins = fig.add_axes([fx0, fy0, 0.175, 2.2 / 11.5])
    ins.patch.set_alpha(0)
    sig = 0.05
    e = np.linspace(-0.16, 0.16, 300)
    pdf = norm.pdf(e, 0, sig)
    ins.plot(e, pdf, color=INK, lw=1.2)
    keep = e <= 0.05
    ins.fill_between(e[keep], pdf[keep], color=GREEN, alpha=0.35, lw=0)
    ins.axvline(0.05, color=VERM, lw=1.1, ls="--")
    ins.text(-0.005, 2.6, "84 %", fontsize=7.5, color="#004D36", ha="center")
    ins.text(0.058, 8.2, "t", fontsize=8, color=VERM, ha="left", style="italic")
    ins.set_yticks([])
    ins.set_xticks([-0.1, 0, 0.1])
    ins.tick_params(labelsize=6.5)
    ins.set_xlabel(r"predicted $E_{\rm hull}$ (eV/atom)" + "\nfor a truly stable phase", fontsize=6.5,
                   labelpad=1)
    ins.spines["left"].set_visible(False)
    ins.set_ylim(0, 9.5)
    ax.text(1.95, yml + 1.05, r"$\sigma\approx0.05$ eV/atom:" + "\nthreshold t set to keep\n84 % of truly\nstable phases",
            ha="center", va="bottom", fontsize=7.3)
    save(fig, "57", "fig-57-3-screening-funnel")


# ---------------------------------------------------------------- Figure 57.4
def active_learning_loop():
    fig = plt.figure(figsize=(6.8, 4.4))
    gs = fig.add_gridspec(2, 2, width_ratios=[1.0, 1.0], height_ratios=[3.0, 1.1], wspace=0.08, hspace=0.08,
                          left=0.09, right=0.995, top=0.97, bottom=0.11)
    ax = fig.add_subplot(gs[0, 0])
    axe = fig.add_subplot(gs[1, 0], sharex=ax)
    axs = fig.add_subplot(gs[:, 1])

    x = np.linspace(0, 1, 801)
    true = lambda t: 0.80 * np.exp(-((t - 0.55) / 0.25) ** 2) + 0.68 * np.exp(-((t - 0.79) / 0.08) ** 2)
    xs = np.array([0.05, 0.25, 0.40, 0.55, 0.62])
    ys = true(xs)
    # GP with squared-exponential kernel; prior mean = broad, cheap (DFT-like) trend
    sf, ell = 0.25, 0.10
    prior = lambda t: 0.25 + 0.45 * np.exp(-((t - 0.70) / 0.30) ** 2)
    k = lambda p, q: sf ** 2 * np.exp(-(p[:, None] - q[None, :]) ** 2 / (2 * ell ** 2))
    K = k(xs, xs) + 1e-6 * np.eye(len(xs))
    Ks = k(x, xs)
    mu = prior(x) + Ks @ np.linalg.solve(K, ys - prior(xs))
    var = sf ** 2 - np.einsum("ij,ji->i", Ks, np.linalg.solve(K, Ks.T))
    s = np.sqrt(np.maximum(var, 1e-12))
    fstar = ys.max()
    z = (mu - fstar) / s
    ei = (mu - fstar) * norm.cdf(z) + s * norm.pdf(z)
    xnext = x[np.argmax(ei)]

    ax.fill_between(x, mu - 2 * s, mu + 2 * s, color=BLUE, alpha=0.15, lw=0, label=r"GP $\pm2\sigma$")
    ax.plot(x, true(x), "--", color="0.55", lw=0.9, label="true (hidden)")
    ax.plot(x, mu, color=BLUE, lw=1.8, label=r"GP mean $\mu$")
    ax.plot(xs, ys, "o", color="k", ms=5.5, zorder=5, label="measured")
    ax.axhline(fstar, ls=":", color=VERM, lw=1.1)
    ax.text(0.01, fstar + 0.015, r"$f^*$ = 0.80", fontsize=7.6, color=VERM, va="bottom")
    ax.set_ylim(0, 1.3)
    ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2])
    ax.set_xlim(0, 1)
    ax.set_ylabel("normalized figure of merit")
    ax.legend(loc="upper left", fontsize=7.0, ncol=2, handlelength=1.6, borderaxespad=0.2, columnspacing=0.8)
    plt.setp(ax.get_xticklabels(), visible=False)

    axe.fill_between(x, ei / ei.max(), color=GREEN, alpha=0.3, lw=0)
    axe.plot(x, ei / ei.max(), color=GREEN, lw=1.5)
    axe.annotate("next\nexperiment", xy=(xnext, 1.0), xytext=(xnext - 0.30, 0.62), fontsize=7.6,
                 ha="center", va="center", arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.9))
    axe.axvline(xnext, color=GREEN, lw=0.8, ls=":")
    ax.axvline(xnext, color=GREEN, lw=0.8, ls=":")
    axe.set_ylim(0, 1.25)
    axe.set_yticks([0, 1])
    axe.set_ylabel("EI\n(scaled)", fontsize=8.5)
    axe.set_xlabel("composition variable x")

    # right: autonomous-lab loop
    axs.set_xlim(0, 10)
    axs.set_ylim(0, 10.6)
    axs.axis("off")
    bw, bh = 4.6, 1.75
    pos = {"plan": (2.7, 7.7), "synth": (5.2, 4.95), "char": (2.7, 2.2), "anal": (0.2, 4.95)}
    txt = {"plan": "Plan\n(acquisition function)",
           "synth": "Synthesize\n(robotic dispensing,\nfurnace/sputter/\nflow reactor)",
           "char": "Characterize\n(XRD, spectroscopy,\nconductivity)",
           "anal": "Analyse and\nupdate model\n(phase ID,\nGP refit)"}
    sizes = {"plan": (bw, 1.4), "synth": (4.6, 2.1), "char": (bw, 1.6), "anal": (4.0, 2.1)}
    fcs = {"plan": "#E3F1EA", "synth": "#EEF3F8", "char": "#EEF3F8", "anal": "#FBEBDD"}
    for kk, (px, py) in pos.items():
        w, h = sizes[kk]
        box(axs, px, py, w, h, txt[kk], fc=fcs[kk], fontsize=7.8)

    def curved(p0, p1, rad):
        axs.add_patch(FancyArrowPatch(p0, p1, connectionstyle=f"arc3,rad={rad}", arrowstyle="-|>",
                                      mutation_scale=11, color=INK, lw=1.2))
    curved((7.3, 7.9), (8.4, 7.1), -0.35)     # plan -> synth
    curved((8.0, 4.9), (6.9, 3.85), -0.35)    # synth -> char
    curved((2.6, 2.6), (1.6, 4.9), -0.35)     # char -> anal
    curved((1.6, 7.1), (2.6, 8.2), -0.35)     # anal -> plan
    # side input / output
    box(axs, 0.0, 9.55, 6.7, 0.95, "prior knowledge: databases, DFT,\nliterature-mined recipes", fc="white",
        fontsize=7.3, ls="--")
    axs.annotate("", xy=(5.0, 9.13), xytext=(5.0, 9.55),
                 arrowprops=dict(arrowstyle="-|>", color="0.35", lw=1.0, ls="--", mutation_scale=9))
    box(axs, 0.0, 0.25, 4.3, 0.95, "human review of claims", fc="white", fontsize=7.3, ls="--")
    axs.annotate("", xy=(0.7, 1.22), xytext=(0.7, 4.95),
                 arrowprops=dict(arrowstyle="-|>", color="0.35", lw=1.0, ls="--", mutation_scale=9))
    save(fig, "57", "fig-57-4-active-learning-loop")
    print(f"   EI peak at x = {xnext:.3f}")


if __name__ == "__main__":
    database_workflow_convex_hull()
    parity_and_learning_curve()
    screening_funnel()
    active_learning_loop()
