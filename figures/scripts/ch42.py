"""Figures for Chapter 42 — Thermodynamics and Kinetics of Corrosion.

Run from the repository root:  python figures/scripts/ch42.py
"""
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.patches import Rectangle, Ellipse, Polygon, FancyBboxPatch

from figstyle import new_fig, save, COLORS, INK, plt

C_BLUE, C_VERM, C_GREEN, C_PINK, C_ORANGE, C_SKY, C_YELLOW, C_BLACK = COLORS
IMM, COR, PAS = "#D9D9D9", "#F8D3CC", "#D3E3F4"
REGION_CMAP = ListedColormap([IMM, COR, PAS])


def _water_lines(ax, x0, x1, labels=True):
    ph = np.array([x0, x1])
    ax.plot(ph, -0.0592 * ph, ls="--", color=C_BLUE, lw=1.1)
    ax.plot(ph, 1.229 - 0.0592 * ph, ls="--", color=C_BLUE, lw=1.1)
    if labels:
        ax.text(x1 - 0.2, -0.0592 * (x1 - 0.2) + 0.05, "(a)", color=C_BLUE, fontsize=8,
                ha="right", va="bottom")
        ax.text(x1 - 0.2, 1.229 - 0.0592 * (x1 - 0.2) + 0.05, "(b)", color=C_BLUE, fontsize=8,
                ha="right", va="bottom")


def _shade(ax, cls, extent):
    """cls: integer array 0 = immunity, 1 = corrosion, 2 = passivation."""
    ax.imshow(cls, origin="lower", extent=extent, aspect="auto", cmap=REGION_CMAP, vmin=0,
              vmax=2, interpolation="nearest", zorder=0)


# ---------------------------------------------------------------------------
# 34.1 Corrosion cell and Evans drop
# ---------------------------------------------------------------------------
def corrosion_cell():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.8, 3.4),
                                 gridspec_kw=dict(width_ratios=[1, 1.05], wspace=0.08))
    for a in (a1, a2):
        a.set_aspect("equal")
        a.axis("off")
    # (a) generic cell
    a1.set_xlim(0, 10)
    a1.set_ylim(-0.4, 7.4)
    a1.add_patch(Rectangle((0.5, 3.0), 9, 2.4, fc="#DCEBF7", ec="none"))
    a1.text(5, 5.3, "electrolyte (water + ions)", ha="center", va="top", fontsize=7.8,
            color="#1F4E79")
    a1.add_patch(Rectangle((0.5, 1.4), 9, 1.6, fc="#BFBFBF", ec=INK, lw=0.9))
    a1.text(5, 1.7, "metal: metallic path", ha="center", va="center", fontsize=7.8)
    a1.add_patch(Rectangle((1.0, 2.75), 2.6, 0.25, fc=C_VERM, ec="none"))
    a1.add_patch(Rectangle((6.4, 2.75), 2.6, 0.25, fc=C_BLUE, ec="none"))
    a1.text(2.3, 6.1, "ANODE\nFe → Fe$^{2+}$ + 2e$^-$", ha="center", fontsize=7.8, color=C_VERM)
    a1.text(7.7, 6.1, "CATHODE\nO$_2$ + 2H$_2$O + 4e$^-$\n→ 4OH$^-$", ha="center", fontsize=7.8,
            color=C_BLUE)
    a1.annotate("", (2.3, 4.2), (2.3, 3.05),
                arrowprops=dict(arrowstyle="-|>", color=C_VERM, lw=1.3, mutation_scale=9))
    a1.text(2.45, 3.6, "Fe$^{2+}$", fontsize=7.5, color=C_VERM)
    a1.annotate("", (7.7, 3.05), (7.7, 4.2),
                arrowprops=dict(arrowstyle="-|>", color=C_BLUE, lw=1.3, mutation_scale=9))
    a1.text(7.85, 3.6, "O$_2$", fontsize=7.5, color=C_BLUE)
    # electrons through metal
    a1.annotate("", (6.6, 2.3), (3.4, 2.3),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.6, mutation_scale=11))
    a1.text(5, 2.42, "e$^-$ flow", ha="center", va="bottom", fontsize=7.8)
    # ionic current through electrolyte
    a1.annotate("", (6.4, 4.4), (3.6, 4.4),
                arrowprops=dict(arrowstyle="-|>", color=C_GREEN, lw=1.4, mutation_scale=10))
    a1.text(5, 3.75, "ionic current", ha="center", fontsize=7.5, color=C_GREEN)
    a1.text(5, 0.6, "Remove any one of the four\nelements and corrosion stops",
            ha="center", va="center", fontsize=7.5, style="italic")
    a1.set_title("(a) the corrosion cell", fontsize=9.5)

    # (b) Evans drop (cross-section)
    a2.set_xlim(-4.2, 4.2)
    a2.set_ylim(-1.6, 4.4)
    a2.add_patch(Rectangle((-4.0, -1.0), 8.0, 1.0, fc="#BFBFBF", ec=INK, lw=0.9))
    a2.text(-2.6, -0.5, "steel", ha="center", va="center", fontsize=8)
    th = np.linspace(0, np.pi, 200)
    R = 3.0
    xd = R * np.cos(th)
    yd = 1.7 * np.sin(th)
    a2.fill_between(xd, 0, yd, color="#E8F3FB", ec=INK, lw=0.9)
    # zones on the steel surface (indicator colours)
    a2.add_patch(Rectangle((-0.9, 0.0), 1.8, 0.16, fc="#2E75B6", ec="none"))
    for s in (-1, 1):
        a2.add_patch(Rectangle((s * 0.9 if s > 0 else -1.6, 0.0), 0.7, 0.2, fc="#8B4513",
                               ec="none"))
        a2.add_patch(Rectangle((s * 1.6 if s > 0 else -2.95, 0.0), 1.35, 0.16, fc="#F48FB1",
                               ec="none"))
    # O2 diffusion arrows through the thin edges
    for x0 in (-2.6, -2.1, 2.1, 2.6):
        y0 = 1.7 * np.sqrt(max(0, 1 - (x0 / R) ** 2)) + 0.55
        a2.annotate("", (x0 * 0.98, 0.3), (x0 * 1.08, y0),
                    arrowprops=dict(arrowstyle="-|>", color=C_BLUE, lw=1.1, mutation_scale=8))
    a2.text(-3.3, 2.5, "O$_2$ from air", color=C_BLUE, fontsize=7.8, ha="center")
    a2.text(0, 1.15, "low O$_2$", ha="center", fontsize=7.8)
    a2.annotate("", (2.2, -0.35), (0.0, -0.35),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.0, mutation_scale=7))
    a2.text(1.1, -0.42, "e$^-$ in steel", fontsize=7, ha="center", va="top")
    # labels below
    a2.annotate("anodic centre: Fe → Fe$^{2+}$\n(blue with ferricyanide)", (0, 0.0), (-1.2, 3.75),
                fontsize=7.3, ha="center", color="#1F4E79",
                arrowprops=dict(arrowstyle="-", lw=0.6, color="#1F4E79"))
    a2.annotate("cathodic ring: O$_2$ → OH$^-$\n(pink with phenolphthalein)", (2.3, 0.12),
                (2.4, 3.0), fontsize=7.3, ha="center", color="#AD1457",
                arrowprops=dict(arrowstyle="-", lw=0.6, color="#AD1457"))
    a2.annotate("rust ring Fe(OH)$_3$", (-1.25, 0.15), (-4.1, -1.45), fontsize=7.3, va="center",
                color="#8B4513", ha="left", arrowprops=dict(arrowstyle="-", lw=0.6,
                                                            color="#8B4513"))
    a2.plot([-3.0, 3.0], [-1.15, -1.15], color=INK, lw=0.8)
    a2.text(1.9, -1.45, "drop ≈5 mm across", fontsize=7.3, ha="center", va="center")
    a2.set_title("(b) differential aeration under a drop", fontsize=9.5)
    save(fig, "42", "fig-42-1-corrosion-cell-drop")


# ---------------------------------------------------------------------------
# 34.2 Pourbaix diagram of iron
# ---------------------------------------------------------------------------
def _fe_class(pH, E):
    """Return species index: 0 Fe, 1 Fe2+, 2 Fe3+, 3 HFeO2-, 4 Fe3O4, 5 Fe2O3."""
    out = np.full(pH.shape, 5)
    low = np.where(pH < 9.03, -0.624, np.where(pH < 13.6, -0.085 - 0.0592 * pH,
                                               0.3155 - 0.0887 * pH))
    fe2_top = np.where(pH < 1.76, 0.771, np.where(pH < 7.26, 1.083 - 0.1775 * pH,
                                                  1.512 - 0.2366 * pH))
    m3o4_top = 0.221 - 0.0592 * pH
    out[(pH < 1.76) & (E >= 0.771)] = 2
    out[(pH < 9.03) & (E < fe2_top)] = 1
    out[(pH >= 7.26) & (E < m3o4_top) & ~((pH < 9.03) & (E < fe2_top))] = 4
    out[(pH >= 13.6) & (E < -1.287 + 0.0296 * pH)] = 3
    out[E < low] = 0
    return out


def pourbaix_iron():
    fig, ax = new_fig(6.4, 4.8)
    x0, x1, y0, y1 = -2, 16, -1.8, 2.0
    pH, E = np.meshgrid(np.linspace(x0, x1, 900), np.linspace(y0, y1, 900))
    sp = _fe_class(pH, E)
    reg = np.select([sp == 0, np.isin(sp, (1, 2, 3))], [0, 1], 2)
    _shade(ax, reg, (x0, x1, y0, y1))
    k = dict(color=INK, lw=1.4)
    ax.plot([x0, 9.03], [-0.624, -0.624], **k)
    p = np.array([9.03, 13.6]); ax.plot(p, -0.085 - 0.0592 * p, **k)
    p = np.array([13.6, 16]); ax.plot(p, 0.3155 - 0.0887 * p, **k)
    p = np.array([13.6, 16]); ax.plot(p, -1.287 + 0.0296 * p, **k)
    p = np.array([1.76, 7.26]); ax.plot(p, 1.083 - 0.1775 * p, **k)
    p = np.array([7.26, 9.03]); ax.plot(p, 1.512 - 0.2366 * p, **k)
    p = np.array([7.26, 16]); ax.plot(p, 0.221 - 0.0592 * p, **k)
    ax.plot([x0, 1.76], [0.771, 0.771], **k)
    ax.plot([1.76, 1.76], [0.771, y1], **k)
    _water_lines(ax, x0, x1)
    lab = dict(ha="center", va="center", fontsize=10, fontweight="bold")
    ax.text(5, -1.2, "Fe\n(immunity)", **lab)
    ax.text(2.6, -0.4, "Fe$^{2+}$\n(corrosion)", **lab)
    ax.text(-0.2, 1.45, "Fe$^{3+}$", **lab)
    ax.text(9.3, 0.2, "Fe$_2$O$_3$\n(passivation)", **lab)
    ax.text(11.3, -0.78, "Fe$_3$O$_4$", ha="center", va="center", fontsize=9,
            fontweight="bold")
    ax.annotate("HFeO$_2^-$", (15.3, -0.9), (15.0, -1.55), fontsize=8, ha="center",
                arrowprops=dict(arrowstyle="-", lw=0.7))
    # steel in concrete
    ax.plot([12.5, 13.5], [-0.2, -0.2], color=C_GREEN, lw=4, solid_capstyle="butt")
    ax.annotate("steel in concrete\n(pH 12.5–13.5)", (13.0, -0.2), (14.0, 0.05), fontsize=7.8,
                ha="center", color="#00704F", arrowprops=dict(arrowstyle="-", lw=0.7,
                                                              color="#00704F"))
    ax.text(-1.8, -0.624 + 0.03, "−0.624 V", fontsize=7.5, va="bottom")
    ax.text(8.6, -0.624, "pH 9.1", fontsize=7, va="top", ha="left")
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
    ax.set_xlabel("pH")
    ax.set_ylabel("E (V vs SHE)")
    handles = [Rectangle((0, 0), 1, 1, fc=c) for c in (IMM, COR, PAS)]
    ax.legend(handles + [plt.Line2D([], [], ls="--", color=C_BLUE)],
              ["immunity", "corrosion", "passivation", "water lines (a) H$_2$, (b) O$_2$"],
              loc="upper right", fontsize=7.8, frameon=True, framealpha=0.9)
    ax.text(x0 + 0.2, y0 + 0.08, "25 °C, dissolved-ion activity 10$^{-6}$", fontsize=7.3,
            style="italic")
    save(fig, "42", "fig-42-2-pourbaix-iron")


# ---------------------------------------------------------------------------
# 34.3 Pourbaix diagrams of Al, Cu, Zn, Ti
# ---------------------------------------------------------------------------
def pourbaix_four():
    x0, x1, y0, y1 = 0, 14, -2.4, 1.6
    pH, E = np.meshgrid(np.linspace(x0, x1, 700), np.linspace(y0, y1, 700))
    fig, axs = plt.subplots(2, 2, figsize=(6.8, 5.6), sharex=True, sharey=True)
    k = dict(color=INK, lw=1.3)
    lab = dict(ha="center", va="center", fontsize=8.5, fontweight="bold")

    # Al
    ax = axs[0, 0]
    imm = np.where(pH < 3.9, -1.778, np.where(pH < 8.6, -1.55 - 0.0591 * pH,
                                               -1.380 - 0.0788 * pH))
    reg = np.where(E < imm, 0, np.where((pH < 3.9) | (pH > 8.6), 1, 2))
    _shade(ax, reg, (x0, x1, y0, y1))
    ax.plot([0, 3.9], [-1.778] * 2, **k)
    p = np.array([3.9, 8.6]); ax.plot(p, -1.55 - 0.0591 * p, **k)
    p = np.array([8.6, 14]); ax.plot(p, -1.380 - 0.0788 * p, **k)
    ax.plot([3.9, 3.9], [-1.778, y1], **k)
    ax.plot([8.6, 8.6], [-2.058, y1], **k)
    ax.text(1.9, 0.3, "Al$^{3+}$", **lab)
    ax.text(6.25, 0.3, "Al$_2$O$_3$·3H$_2$O", fontsize=7.5, fontweight="bold", ha="center")
    ax.text(11.3, -1.3, "AlO$_2^-$", **lab)
    ax.text(5, -2.15, "Al (immunity)", **lab)
    ax.set_title("(a) aluminium", fontsize=9.5)

    # Cu
    ax = axs[0, 1]
    imm = np.where(pH < 5.26, 0.162, 0.471 - 0.0591 * pH)
    c2o_top = np.where(pH < 6.95, -0.152 + 0.0591 * pH,
                       np.where(pH < 12.83, 0.669 - 0.0591 * pH, 1.428 - 0.1182 * pH))
    reg = np.full(pH.shape, 2)
    reg[(pH < 6.95) & (E >= c2o_top)] = 1
    reg[(pH < 5.26)] = 1
    reg[(pH >= 12.83) & (E >= 1.428 - 0.1182 * pH)] = 1
    reg[E < imm] = 0
    _shade(ax, reg, (x0, x1, y0, y1))
    ax.plot([0, 5.26], [0.162] * 2, **k)
    p = np.array([5.26, 14]); ax.plot(p, 0.471 - 0.0591 * p, **k)
    p = np.array([5.26, 6.95]); ax.plot(p, -0.152 + 0.0591 * p, **k)
    p = np.array([6.95, 12.83]); ax.plot(p, 0.669 - 0.0591 * p, **k)
    p = np.array([12.83, 14]); ax.plot(p, 1.428 - 0.1182 * p, **k)
    ax.plot([6.95, 6.95], [0.259, y1], **k)
    ax.plot([12.83, 12.83], [-0.089, y1], **k)
    ax.text(2.6, 0.8, "Cu$^{2+}$", **lab)
    ax.text(9.8, 0.8, "CuO", **lab)
    ax.text(9.5, 0.03, "Cu$_2$O", fontsize=6.5, fontweight="bold", ha="center", va="center", rotation=-6)
    ax.text(13.45, 0.8, "HCuO$_2^-$", fontsize=6.5, fontweight="bold", ha="center",
            rotation=90)
    ax.text(5, -1.2, "Cu (immunity)", **lab)
    ax.text(0.3, 0.2, "0.16 V", fontsize=7, va="bottom")
    ax.set_title("(b) copper", fontsize=9.5)

    # Zn
    ax = axs[1, 0]
    imm = np.where(pH < 8.5, -0.94, np.where(pH < 10.68, -0.439 - 0.0591 * pH,
                                             np.where(pH < 13.17, -0.123 - 0.0886 * pH,
                                                      0.264 - 0.1182 * pH)))
    reg = np.where(E < imm, 0, np.where((pH < 8.5) | (pH > 10.68), 1, 2))
    _shade(ax, reg, (x0, x1, y0, y1))
    ax.plot([0, 8.5], [-0.94] * 2, **k)
    p = np.array([8.5, 10.68]); ax.plot(p, -0.439 - 0.0591 * p, **k)
    p = np.array([10.68, 13.17]); ax.plot(p, -0.123 - 0.0886 * p, **k)
    p = np.array([13.17, 14]); ax.plot(p, 0.264 - 0.1182 * p, **k)
    ax.plot([8.5, 8.5], [-0.94, y1], **k)
    ax.plot([10.68, 10.68], [-1.07, y1], **k)
    ax.plot([13.17, 13.17], [-1.29, y1], **k, ls=":")
    ax.text(4.2, 0.3, "Zn$^{2+}$", **lab)
    ax.text(9.6, 0.95, "ZnO /\nZn(OH)$_2$", fontsize=6.8, fontweight="bold", ha="center")
    ax.text(11.9, -0.6, "HZnO$_2^-$", fontsize=7, fontweight="bold", ha="center", rotation=90)
    ax.text(13.6, -0.6, "ZnO$_2^{2-}$", fontsize=7, fontweight="bold", ha="center",
            rotation=90)
    ax.text(4.5, -1.7, "Zn (immunity)", **lab)
    ax.set_title("(c) zinc", fontsize=9.5)

    # Ti (simplified)
    ax = axs[1, 1]
    imm = -1.81 - 0.0279 * pH
    cor_poly = np.array([[0, -1.81], [0, -0.31], [2.0, -0.78], [2.7, -1.885]])
    from matplotlib.path import Path
    inside = Path(cor_poly).contains_points(np.c_[pH.ravel(), E.ravel()]).reshape(pH.shape)
    reg = np.where(E < imm, 0, np.where(inside, 1, 2))
    _shade(ax, reg, (x0, x1, y0, y1))
    p = np.array([0, 14]); ax.plot(p, -1.81 - 0.0279 * p, **k)
    ax.plot(cor_poly[1:, 0], cor_poly[1:, 1], **k)
    ax.text(0.15, -1.25, "Ti$^{2+}$\nTi$^{3+}$", fontsize=7, fontweight="bold")
    ax.text(8, 0.3, "TiO$_2$ (passivation)", **lab)
    ax.text(7, -2.25, "Ti (immunity)", **lab)
    ax.set_title("(d) titanium (simplified)", fontsize=9.5)

    for ax in axs.ravel():
        _water_lines(ax, x0, x1, labels=False)
        ax.set_xlim(x0, x1)
        ax.set_ylim(y0, y1)
    for ax in axs[1]:
        ax.set_xlabel("pH")
    for ax in axs[:, 0]:
        ax.set_ylabel("E (V vs SHE)")
    handles = [Rectangle((0, 0), 1, 1, fc=c) for c in (IMM, COR, PAS)]
    fig.legend(handles + [plt.Line2D([], [], ls="--", color=C_BLUE)],
               ["immunity", "corrosion", "passivation", "water stability lines"],
               loc="lower center", ncol=4, fontsize=8, bbox_to_anchor=(0.5, -0.03))
    fig.subplots_adjust(hspace=0.22, wspace=0.08, bottom=0.12)
    save(fig, "42", "fig-42-3-pourbaix-al-cu-zn-ti")


# ---------------------------------------------------------------------------
# 34.4 Evans diagrams for iron
# ---------------------------------------------------------------------------
def evans_iron():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.8, 4.0), sharey=True,
                                 gridspec_kw=dict(wspace=0.08))
    li = np.linspace(-10, -1, 400)
    Ea = -0.624 + 0.060 * (li + 8)
    for ax in (a1, a2):
        m = li >= -8
        ax.plot(li[m], Ea[m], color=C_VERM, lw=2, label="Fe → Fe$^{2+}$ (b$_a$ = 60 mV/dec)")
        ax.axhline(-0.624, color=C_VERM, ls=":", lw=1)
        ax.plot(-8, -0.624, "o", color=C_VERM, ms=4)
        ax.text(-9.9, -0.615, "E$_{eq}$(Fe/Fe$^{2+}$) = −0.624", fontsize=7, color=C_VERM,
                va="bottom")
        ax.set_xlim(-10, -1)
        ax.set_ylim(-0.8, 0.2)
        ax.set_xlabel(r"log$_{10}$ |i| (A/cm$^2$)")
    # (a) deaerated pH 1
    Ec = -0.059 - 0.120 * (li + 6)
    m = li >= -6
    a1.plot(li[m], Ec[m], color=C_BLUE, lw=2, label="2H$^+$ → H$_2$ (b$_c$ = 120 mV/dec)")
    a1.axhline(-0.059, color=C_BLUE, ls=":", lw=1)
    a1.plot(-6, -0.059, "o", color=C_BLUE, ms=4)
    a1.text(-9.9, -0.05, "E$_{eq}$(H$^+$/H$_2$) = −0.059", fontsize=7, color=C_BLUE,
            va="bottom")
    lc, Ecorr = -3.53, -0.356
    a1.plot(lc, Ecorr, "o", mfc="white", mec=INK, mew=1.6, ms=7, zorder=5)
    a1.plot([-10, lc], [Ecorr, Ecorr], color=INK, lw=0.7, ls="--")
    a1.plot([lc, lc], [-0.8, Ecorr], color=INK, lw=0.7, ls="--")
    a1.text(-9.9, Ecorr + 0.01, "E$_{corr}$ = −0.356 V", fontsize=7.8, va="bottom")
    a1.text(lc - 0.1, -0.78, "i$_{corr}$ = 3.0×10$^{-4}$\n≈ 3.5 mm/yr", fontsize=7.5,
            ha="right", va="bottom")
    a1.set_ylabel("E (V vs SHE)")
    a1.set_title("(a) deaerated acid, pH 1", fontsize=9.5)
    a1.legend(loc="upper right", fontsize=6.8, bbox_to_anchor=(1.0, 1.0))
    # (b) aerated neutral
    i0, Eeq, b = 1e-12, 0.815, 0.12
    E = np.linspace(-0.8, 0.2, 500)
    iact = i0 * 10 ** ((Eeq - E) / b)
    for iL, ls, lab in [(3.9e-5, "-", "still (δ 0.05 cm)"),
                        (3.9e-4, "--", "stirred (δ 0.005 cm)")]:
        itot = 1 / (1 / iact + 1 / iL)
        a2.plot(np.log10(itot), E, color=C_BLUE, lw=2, ls=ls, label="O$_2$, " + lab)
        Ex = -0.624 + 0.060 * (np.log10(iL) + 8)
        a2.plot(np.log10(iL), Ex, "o", mfc="white", mec=INK, mew=1.6, ms=7, zorder=5)
    a2.annotate("i$_L$ = 39 µA/cm²\nE$_{corr}$ ≈ −0.41 V\n≈0.45 mm/yr",
                (np.log10(3.9e-5), -0.409), (-6.2, -0.3), fontsize=7.2, ha="right",
                va="center", arrowprops=dict(arrowstyle="-", lw=0.7))
    a2.text(np.log10(3.9e-4) + 0.15, -0.37, "i$_L$ = 390 µA/cm²\nE$_{corr}$ ≈ −0.35 V",
            fontsize=7.2, ha="left", va="top")
    a2.text(-1.1, 0.17, "E$_{eq}$(O$_2$/H$_2$O) = +0.82 V\nat pH 7 (off scale ↑)", fontsize=7, ha="right",
            color=C_BLUE, va="top")
    a2.set_title("(b) aerated neutral water", fontsize=9.5)
    hh, ll = a2.get_legend_handles_labels()
    a2.legend(hh[1:], ll[1:], loc="lower left", fontsize=6.6, bbox_to_anchor=(0.0, 0.0))
    save(fig, "42", "fig-42-4-evans-diagram-iron")


# ---------------------------------------------------------------------------
# 34.5 Active–passive polarization curve
# ---------------------------------------------------------------------------
def active_passive():
    fig, ax = new_fig(6.6, 4.6)
    E = np.linspace(-0.6, 1.4, 2000)
    ia = 2e-5 * 10 ** ((E + 0.4) / 0.1) / (1 + np.exp((E + 0.215) / 0.009))
    ia += 1e-6 / (1 + np.exp(-(E + 0.2) / 0.012)) + 1e-6 * 10 ** ((E - 1.0) / 0.06)
    ic = 1.4e-8 * 10 ** (-(E + 0.02) / 0.12)
    net = np.abs(ia - ic)
    ax.semilogx(net, E, color=C_BLACK, lw=2,
                label="stainless steel, 0.5 M H$_2$SO$_4$ (no Cl$^-$)")
    # curve 2: neutral NaCl, passive from Ecorr to E_pit, then pitting
    E2 = np.linspace(-0.1, 0.30, 200)
    i2 = 7e-7 * 10 ** ((E2 + 0.1) / 2.5)
    E2b = np.linspace(0.30, 0.42, 100)
    i2b = 10 ** (np.log10(i2[-1]) + (E2b - 0.30) / 0.12 * 4.3)
    ax.semilogx(np.r_[i2, i2b], np.r_[E2, E2b], color=C_VERM, lw=2,
                label="same steel (316L), neutral NaCl")
    Er = np.linspace(0.42, 0.0, 200)
    ir = 10 ** (np.interp(Er, [0.0, 0.03, 0.42], [-6.0, -3.6, -1.7]))
    ax.semilogx(ir, Er, color=C_VERM, lw=1.6, ls="--", label="reverse scan in NaCl (hysteresis)")
    ax.annotate("", (10 ** -2.95, 0.235), (10 ** -2.35, 0.32),
                arrowprops=dict(arrowstyle="-|>", color=C_VERM, lw=1.2, mutation_scale=10))
    ax.annotate("", (10 ** -2.2, 0.40), (10 ** -3.2, 0.37),
                arrowprops=dict(arrowstyle="-|>", color=C_VERM, lw=1.2, mutation_scale=10))
    # cathodic lines
    Ew = np.linspace(-0.12, -0.45, 300)
    iw = 1e-6 * 10 ** ((-0.12 - Ew) / 0.08)
    ax.semilogx(iw, Ew, color=C_GREEN, lw=1.5)
    ax.text(10 ** -6.25, -0.12, "weak oxidant", color=C_GREEN, fontsize=7.6, ha="right",
            va="center")
    ian = np.interp(Ew, E, ia)
    k = np.argmin(np.abs(np.log10(ian) - np.log10(iw)))
    ax.plot(iw[k], Ew[k], "o", color=C_GREEN, ms=6, zorder=5)
    ax.text(iw[k] * 1.4, Ew[k] - 0.03, "corrodes", color=C_GREEN, fontsize=7.8, va="top")
    Es = np.linspace(0.8, 0.1, 50)
    ax.semilogx(1e-7 * 10 ** ((0.8 - Es) / 0.12), Es, color=C_BLUE, lw=1.5)
    ax.text(10 ** -7.1, 0.82, "strong oxidant", color=C_BLUE, fontsize=7.6, ha="right")
    ax.plot(1e-6, 0.68, "o", color=C_BLUE, ms=6, zorder=5)
    ax.text(10 ** -5.9, 0.68, "passive", color=C_BLUE, fontsize=7.8, va="center")
    # annotations
    ip = np.argmax(np.where(E < 0, ia, 0))
    ax.annotate("E$_{pp}$, i$_{crit}$ ≈ 10$^{-3}$", (ia[ip], E[ip]), (10 ** -2.5, -0.05),
                fontsize=7.8, arrowprops=dict(arrowstyle="-", lw=0.7))
    ax.text(10 ** -5.95, 0.5, "i$_{pass}$ ≈ 10$^{-6}$", fontsize=7.8)
    ax.text(10 ** -5.8, 1.15, "transpassive", fontsize=7.8)
    ax.text(10 ** -6.75, -0.43, "E$_{corr}$", fontsize=7.8, va="center")
    ax.annotate("E$_{pit}$ ≈ +0.3 V", (10 ** -6.0, 0.30), (10 ** -7.9, 0.30), fontsize=7.8,
                va="center", color=C_VERM, arrowprops=dict(arrowstyle="-", lw=0.7,
                                                           color=C_VERM))
    ax.annotate("E$_{rp}$ ≈ 0 V", (10 ** -6.0, 0.0), (10 ** -7.9, 0.06), fontsize=7.8,
                va="center", color=C_VERM, arrowprops=dict(arrowstyle="-", lw=0.7,
                                                           color=C_VERM))
    ax.set_xlim(1e-8, 1e-1)
    ax.set_ylim(-0.6, 1.4)
    ax.set_xlabel("Current density i (A/cm²)")
    ax.set_ylabel("E (V vs SHE)")
    ax.legend(loc="upper center", fontsize=7.4, bbox_to_anchor=(0.5, -0.15), ncol=2)
    save(fig, "42", "fig-42-5-active-passive-curve")


# ---------------------------------------------------------------------------
# 34.6 Oxidation kinetics and PBR
# ---------------------------------------------------------------------------
def oxidation_kinetics():
    fig = plt.figure(figsize=(6.8, 4.6))
    gs = fig.add_gridspec(2, 2, width_ratios=[1.75, 1], hspace=0.55, wspace=0.32)
    ax = fig.add_subplot(gs[:, 0])
    t = np.logspace(0, 8, 400)
    ax.set_xlim(1, 1e8)
    ax.set_ylim(1e-2, 1e4)
    ax.set_xscale("log")
    ax.set_yscale("log")
    fig.canvas.draw()
    p0 = ax.transData.transform((1, 1))
    p1 = ax.transData.transform((1e4, 100))
    ang = np.degrees(np.arctan2(p1[1] - p0[1], p1[0] - p0[0]))
    for kp, lab, c, tx in [(1e-7, "FeO on Fe, 1000 °C, k$_p$ = 10$^{-7}$ cm²/s", C_VERM, 2.0),
                           (1e-12, "Cr$_2$O$_3$, 1000 °C, 10$^{-12}$", C_GREEN, 6.0),
                           (1e-14, "α-Al$_2$O$_3$, 1100 °C, 10$^{-14}$", C_BLUE, 400.0)]:
        x = np.sqrt(kp * t) * 1e4  # µm
        ax.loglog(t, x, color=c, lw=2)
        ax.text(tx, np.sqrt(kp * tx) * 1e4 * 2.0, lab, color=c, fontsize=7.2,
                rotation=ang, rotation_mode="anchor", ha="left", va="bottom")
    tb = 3000 * 3600
    xb = np.sqrt(1e-12 * tb) * 1e4
    tt = np.logspace(np.log10(tb), 8, 100)
    ax.loglog(tt, xb + 2e-9 * (tt - tb) * 1e4, color=C_GREEN, ls="--", lw=1.6)
    ax.text(2.2e7, 300, "breakaway\n(linear)", color=C_GREEN, fontsize=7.5, ha="right")
    for tp, xp, lab in [(3600, 190, "190 µm, 1 h"), (3.6e5, 6, "6 µm, 100 h"),
                        (3.6e7, 6, "6 µm, 10 000 h")]:
        ax.plot(tp, xp, "o", mfc="white", mec=INK, mew=1.4, ms=6, zorder=5)
        if tp < 1e5:
            ax.text(tp * 1.6, xp / 1.6, lab, fontsize=7.2, va="top")
        else:
            txy = (2e4, 25) if tp < 1e7 else (1.5e6, 0.3)
            ax.annotate(lab, (tp, xp), txy, fontsize=7.2, ha="center", va="center",
                        arrowprops=dict(arrowstyle="-", lw=0.7, shrinkB=4))
    ax.text(9e7, 0.013, "all lines: parabolic,\nslope ½", fontsize=7, ha="right",
            style="italic", color="#555555")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Scale thickness (µm)")
    ax.set_yticks([0.01, 0.1, 1, 10, 100, 1000, 10000])
    ax.set_yticklabels(["0.01", "0.1", "1", "10", "100", "1 mm", "10 mm"])
    top = ax.secondary_xaxis("top", functions=(lambda s: s / 3600, lambda h: h * 3600))
    top.set_xticks([1e-3, 1e-1, 10, 1e4])
    top.set_xticklabels(["0.001", "0.1", "10", "10 000"])
    top.set_xlabel("Time (h)")
    ax.set_title("(a)", loc="left", fontsize=9.5)
    # (b) rate laws schematic
    b = fig.add_subplot(gs[0, 1])
    tl = np.linspace(0, 10, 200)
    b.plot(tl, 0.8 * tl, color=C_VERM, label="linear")
    b.plot(tl, 2.6 * np.sqrt(tl), color=C_GREEN, label="parabolic")
    b.plot(tl, 1.6 * np.log10(3 * tl + 1), color=C_BLUE, label="logarithmic")
    tb2 = 5
    bk = np.where(tl < tb2, 2.0 * np.sqrt(tl), 2.0 * np.sqrt(tb2) + 1.3 * (tl - tb2))
    b.plot(tl, bk, color=C_BLACK, ls="--", label="breakaway")
    b.set_xlim(0, 10)
    b.set_ylim(0, 10)
    b.set_xticks([])
    b.set_yticks([])
    b.set_xlabel("time", fontsize=8)
    b.set_ylabel("thickness", fontsize=8)
    b.legend(fontsize=6.5, loc="upper left", handlelength=1.5)
    b.set_title("(b) rate laws", loc="left", fontsize=9)

    # (c) PBR bars
    c = fig.add_subplot(gs[1, 1])
    names = ["Mg", "Al", "Ni", "Fe", "Cr", "Nb", "W"]
    vals = [0.81, 1.28, 1.70, 1.76, 2.01, 2.67, 3.40]
    c.axvspan(1, 2, color="#E2EFDA", lw=0)
    cols = [C_VERM if (v < 1 or v > 2.05) else C_GREEN for v in vals]
    c.barh(range(len(names))[::-1], vals, color=cols, height=0.65)
    c.set_yticks(range(len(names))[::-1])
    c.set_yticklabels(names, fontsize=7.5)
    for i, v in zip(range(len(names))[::-1], vals):
        c.text(v + 0.05, i, f"{v:.2f}", va="center", fontsize=6.8)
    c.set_xlim(0, 4.1)
    c.set_xlabel("Pilling–Bedworth ratio", fontsize=8)
    c.tick_params(labelsize=7)
    c.text(1.5, 7.0, "protective 1–2", fontsize=6.8, ha="center", color="#2E6B2E")
    c.set_ylim(-0.6, 7.6)
    c.set_title("(c)", loc="left", fontsize=9)
    save(fig, "42", "fig-42-6-oxidation-kinetics-pbr")


if __name__ == "__main__":
    corrosion_cell()
    pourbaix_iron()
    pourbaix_four()
    evans_iron()
    active_passive()
    oxidation_kinetics()
