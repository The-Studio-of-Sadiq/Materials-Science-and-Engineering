"""Figures for Chapter 59 — Sustainability, Lifecycle and the Circular Economy.

Run from the repository root:  python figures/scripts/ch59.py
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figstyle import new_fig, box, arrow, save, COLORS, INK  # noqa: E402,F401
import numpy as np  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon, Patch, Rectangle  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

BLUE, VERM, GREEN, PINK, ORANGE, SKY = COLORS[:6]


# ---------------------------------------------------------------- Figure 59.1
def global_material_production():
    fig, ax = new_fig(6.8, 4.4)
    rows = [  # name, Mt/yr, CO2 share text, group colour
        ("concrete", 27000, "(via cement)", "#8C8C8C"),
        ("cement", 4100, "~7–8 %", "#8C8C8C"),
        ("wood (industrial roundwood, as mass)", 1000, "", "#8B5A2B"),
        ("crude steel", 1900, "~7–9 %", VERM),
        ("paper and board", 400, "~1 %", "#8B5A2B"),
        ("plastics", 400, "~4 % (incl. chemicals)", BLUE),
        ("glass", 150, "<1 %", SKY),
        ("aluminium (primary)", 70, "~2 %", VERM),
        ("copper (refined)", 25, "", VERM),
        ("titanium metal", 0.3, "", VERM),
        ("rare-earth oxides", 0.3, "", PINK),
    ]
    y = np.arange(len(rows))[::-1]
    for yy, (name, v, co2, col) in zip(y, rows):
        ax.barh(yy, v - 0.1, left=0.1, height=0.66, color=col, alpha=0.8, edgecolor="none")
        lab = f"{v:,.0f}".replace(",", " ") if v >= 1 else f"{v:g}"
        if v > 1e4:
            ax.text(v * 0.85, yy, lab, va="center", ha="right", fontsize=7.8, color="white")
        else:
            ax.text(v * 1.15, yy, lab, va="center", ha="left", fontsize=7.8)
    ax.set_yticks(y)
    ax.set_yticklabels([r[0] for r in rows], fontsize=8.3)
    ax.set_xscale("log")
    ax.set_xlim(0.1, 5e4)
    ax.set_ylim(-0.6, len(rows) - 0.4)
    ax.set_xticks([0.1, 1, 10, 100, 1e3, 1e4])
    ax.set_xticklabels(["0.1", "1", "10", "100", "1 000", "10 000"])
    ax.set_xlabel("production (Mt/yr)")
    ax.tick_params(axis="y", length=0)
    # right-hand column: share of global CO2
    tr = ax.get_yaxis_transform()
    ax.text(1.03, len(rows) - 0.45, "share of\nglobal CO$_2$", transform=tr, ha="left", va="bottom", fontsize=8,
            fontweight="bold")
    for yy, (name, v, co2, col) in zip(y, rows):
        if co2:
            ax.text(1.03, yy, co2, transform=tr, ha="left", va="center", fontsize=7.8,
                    color="0.4" if co2.startswith("(") else INK)
    fig.text(0.5, -0.01, "About one quarter of global energy- and process-related CO$_2$ comes from making materials.",
             ha="center", va="top", fontsize=8.3, style="italic")
    save(fig, "59", "fig-59-1-global-material-production")


# ---------------------------------------------------------------- Figure 59.2
def _sband(ax, x0, yb0, x1, yb1, w, color, alpha=0.75):
    """Smooth band from a vertical interval [yb0, yb0+w] at x0 to [yb1, yb1+w] at x1."""
    t = np.linspace(0, 1, 60)
    s = t * t * (3 - 2 * t)
    x = x0 + (x1 - x0) * t
    yb = yb0 + (yb1 - yb0) * s
    pts = np.r_[np.c_[x, yb], np.c_[x[::-1], (yb + w)[::-1]]]
    ax.add_patch(Polygon(pts, closed=True, fc=color, ec="none", alpha=alpha))


def _rib(ax, pts, w, color, alpha=0.75, arrow_end=False):
    """Ribbon of width w along an orthogonal polyline (centre line)."""
    pts = np.asarray(pts, float)
    n = len(pts)
    dirs = [(pts[i + 1] - pts[i]) / np.linalg.norm(pts[i + 1] - pts[i]) for i in range(n - 1)]
    nrm = [np.array([-d[1], d[0]]) for d in dirs]
    left, right = [], []
    for i in range(n):
        if i == 0:
            o = nrm[0]
        elif i == n - 1:
            o = nrm[-1]
        else:
            o = nrm[i - 1] + nrm[i]
        left.append(pts[i] + o * w / 2)
        right.append(pts[i] - o * w / 2)
    poly = left + right[::-1]
    if arrow_end:
        d = dirs[-1]
        tip = pts[-1] + d * w * 0.6
        poly = left + [left[-1] + nrm[-1] * w * 0.15, tip, right[-1] - nrm[-1] * w * 0.15] + right[::-1]
    ax.add_patch(Polygon(poly, closed=True, fc=color, ec="none", alpha=alpha))


def steel_sankey():
    fig = plt.figure(figsize=(6.8, 4.7))
    ax = fig.add_axes([0.005, 0.005, 0.99, 0.99])
    ax.set_xlim(0, 22.4)
    ax.set_ylim(-0.6, 14.4)
    ax.axis("off")
    k = 1 / 250.0  # data units per Mt/yr
    ORE, SCR, BOF, EAF, PROD, GREY = "#A0522D", GREEN, "#4A6FA5", "#2E9C7A", "#7FB3DA", "#9A9A9A"
    top = 13.0
    w_ore, w_eol, w_man = 1400 * k, 350 * k, 300 * k
    w_cr, w_loss = 1900 * k, 150 * k
    xs0, xs1 = 4.3, 4.7      # steelmaking node
    xf0, xf1 = 9.0, 9.4      # fabrication node
    # inputs
    y_ore = top - w_ore
    _rib(ax, [(0.2, y_ore + w_ore / 2), (xs0, y_ore + w_ore / 2)], w_ore, ORE)
    y_eol_in = y_ore - w_eol
    y_man_in = y_eol_in - w_man
    # steelmaking node
    ax.add_patch(Rectangle((xs0, y_man_in), xs1 - xs0, top - y_man_in, fc="0.25", ec="none"))
    # crude steel split BF-BOF / EAF, then losses
    w_bof, w_eaf = 0.70 * w_cr, 0.30 * w_cr
    _rib(ax, [(xs1, top - w_bof / 2), (xf0, top - w_bof / 2)], w_bof, BOF)
    _rib(ax, [(xs1, top - w_bof - w_eaf / 2), (xf0, top - w_bof - w_eaf / 2)], w_eaf, EAF)
    y_loss = top - w_cr - w_loss
    _rib(ax, [(xs1, y_loss + w_loss / 2), (5.7, y_loss + w_loss / 2)], w_loss, GREY, arrow_end=True)
    ax.text(6.25, y_loss + w_loss / 2, "yield losses ~150", fontsize=7, va="center", ha="left", color="0.3")
    # fabrication node
    ax.add_patch(Rectangle((xf0, top - w_cr), xf1 - xf0, w_cr, fc="0.25", ec="none"))
    w_prod = 1600 * k
    # manufacturing scrap loop (inner)
    ym = top - w_prod - w_man / 2
    _rib(ax, [(xf1, ym), (10.2, ym), (10.2, 3.2), (2.4, 3.2), (2.4, y_man_in + w_man / 2),
              (xs0, y_man_in + w_man / 2)], w_man, SCR, alpha=0.55)
    # end-of-life collected scrap loop (outer)
    xb0, xb1 = 14.2, 17.8   # stock box
    y_eol_out = 6.0
    w_lost = 150 * k
    _rib(ax, [(xb1, y_eol_out + w_eol / 2), (19.5, y_eol_out + w_eol / 2), (19.5, 1.3), (0.9, 1.3),
              (0.9, y_eol_in + w_eol / 2), (xs0, y_eol_in + w_eol / 2)], w_eol, SCR, alpha=0.8)
    _rib(ax, [(xb1, y_eol_out + w_eol + w_lost / 2), (21.4, y_eol_out + w_eol + w_lost / 2)], w_lost, GREY,
         arrow_end=True)
    # products: straight, then fan out by sector into the stock box
    sectors = [("construction", 0.52), ("mech. equipment", 0.16), ("automotive", 0.12),
               ("metal products", 0.10), ("other transport", 0.05), ("appliances, elec.", 0.05)]
    _rib(ax, [(xf1, top - w_prod / 2), (11.0, top - w_prod / 2)], w_prod, PROD)
    ys = top
    ye = top
    gap = 0.3
    for name, f in sectors:
        w = f * w_prod
        _sband(ax, 11.0, ys - w, 12.6, ye - w, w, PROD)
        _rib(ax, [(12.6, ye - w / 2), (xb0, ye - w / 2)], w, PROD)
        ax.text(xb0 + 0.15, ye - w / 2, f"{name} {f * 100:.0f} %", fontsize=6.6, va="center", ha="left")
        ys -= w
        ye -= w + gap
    # stock box
    ax.add_patch(Rectangle((xb0, 2.4), xb1 - xb0, top + 0.3 - 2.4, fc="#F1F1F1", ec=INK, lw=1.0, zorder=0))
    ax.text((xb0 + xb1) / 2, 3.9, "In-use stock\n~35 000 Mt\n(growing\n~1 000 Mt/yr)", ha="center",
            va="center", fontsize=7.6, fontweight="bold")
    # labels
    ax.text(1.9, y_ore + w_ore / 2, "iron ore →\npig iron / DRI\n~1 400", ha="center", va="center", fontsize=7.8,
            color="white", fontweight="bold")
    ax.text(3.35, y_eol_in + w_eol / 2, "EoL\n~350", ha="center", va="center", fontsize=6.6, color="white")
    ax.text(3.65, y_man_in + w_man / 2, "new\n~300", ha="center", va="center", fontsize=6.6, color="white")
    ax.text(6.85, top - w_bof / 2 + 0.45, "crude steel ~1 900", ha="center", va="center", fontsize=8,
            color="white", fontweight="bold")
    ax.text(6.85, top - w_bof / 2 - 0.45, "BF–BOF ~70 %", ha="center", va="center", fontsize=7.6, color="white")
    ax.text(6.85, top - w_bof - w_eaf / 2, "EAF ~30 %", ha="center", va="center", fontsize=7.6, color="white")
    ax.text(10.2, top - w_prod / 2, "products\n~1 600", ha="center", va="center", fontsize=7.6, color=INK)
    ax.text(6.3, 3.2, "home and new (manufacturing) scrap ~300", ha="center", va="center", fontsize=7.2,
            color="white", fontweight="bold")
    ax.text(10.2, 1.3, "end-of-life scrap collected ~350 (scrap input total ~650)", ha="center", va="center",
            fontsize=7.2, color="white", fontweight="bold")
    ax.text(xs0 + 0.2, top + 0.15, "steel-\nmaking", ha="center", va="bottom", fontsize=7.2)
    ax.text(xf0 + 0.2, top + 0.15, "fabri-\ncation", ha="center", va="bottom", fontsize=7.2)
    ax.text(21.4, y_eol_out + w_eol + w_lost + 0.2, "end of life ~500;\nlost / landfilled /\nunrecovered ~150", ha="right",
            va="bottom", fontsize=7.0, color="0.3")
    ax.text(20.1, 11.2, "stock lag:\nproducts last\n15–60 years", ha="center", va="center", fontsize=7.6,
            style="italic", color="0.25")
    ax.text(0.2, -0.35, "Flows in Mt/yr, approximate, early 2020s; band widths proportional to flow "
            "(the stock is not to scale).", fontsize=7, color="0.35", va="center")
    save(fig, "59", "fig-59-2-steel-sankey")


# ---------------------------------------------------------------- Figure 59.3
def beam_embodied_carbon():
    fig, ax = new_fig(6.6, 4.2)
    mats = [  # name, solid, shaped, phi label
        ("primary steel (BF–BOF)", 1.00, 0.158, "φ = 40"),
        ("EAF steel (scrap)", 0.27, 0.043, "φ = 40"),
        ("concrete C30/37", 0.055, 0.024, "φ = 10, +40 % rebar"),
        ("glulam (fossil C only)", 0.047, 0.021, "φ = 5"),
        ("primary aluminium", 4.4, 0.80, "φ = 30"),
        ("recycled aluminium", 0.22, 0.040, "φ = 30"),
        ("CFRP", 4.2, 0.84, "φ = 25"),
    ]
    y = np.arange(len(mats))[::-1] * 1.0
    h = 0.36
    for yy, (n, so, sh, ph) in zip(y, mats):
        ax.barh(yy + h / 2, so - 0.01, left=0.01, height=h, color="0.55", edgecolor="none")
        ax.barh(yy - h / 2, sh - 0.01, left=0.01, height=h, color=GREEN, edgecolor="none")
        ax.text(so * 1.1, yy + h / 2, f"{so:g}", va="center", fontsize=7.4)
        lab = (f"{sh:.3f}" if sh < 0.2 else f"{sh:.2f}") + f"  ({ph})"
        if sh > 0.5:
            ax.text(sh * 0.9, yy - h / 2, lab, va="center", ha="right", fontsize=7.0, color="white")
        else:
            ax.text(sh * 1.1, yy - h / 2, lab, va="center", fontsize=7.0, color="#006B4E")
    ax.axvline(1, ls="--", color=INK, lw=1)
    ax.set_xscale("log")
    ax.set_xlim(0.01, 10)
    ax.set_yticks(y)
    ax.set_yticklabels([m[0] for m in mats], fontsize=8.2)
    ax.tick_params(axis="y", length=0)
    ax.set_ylim(-0.75, len(mats) + 0.45)
    ax.set_xticks([0.01, 0.1, 1, 10])
    ax.set_xticklabels(["0.01", "0.1", "1", "10"])
    ax.set_xlabel("embodied carbon relative to primary-steel solid beam")
    ax.legend(handles=[Patch(color="0.55", label=r"solid section ($\rho H_c/E^{1/2}$)"),
                       Patch(color=GREEN, label=r"practical shaped section ($\div\sqrt{\phi}$)")],
              loc="upper right", fontsize=7.6)
    fig.text(0.5, -0.01, "Shape narrows the gap between metals and timber or concrete; primary aluminium and CFRP "
             "swap places.", ha="center", va="top", fontsize=8, style="italic")
    save(fig, "59", "fig-59-3-beam-embodied-carbon")


# ---------------------------------------------------------------- Figure 59.4
def life_phase_breakdown():
    fig, ax = new_fig(6.8, 4.3)
    cols = {"mat": "#1F4E79", "man": "#4F81BD", "mm": "#2F679C", "tr": "#A9C8E8", "use": ORANGE,
            "eol": "0.65"}
    rows = [
        ("Petrol passenger car,\n200 000 km", [("mat", 15), ("man", 5), ("use", 80)], 0),
        ("Battery-electric car,\nlow-carbon grid", [("mat", 55), ("man", 10), ("use", 35)], 0),
        ("Commercial aircraft,\n25 years", [("mm", 0.7), ("use", 99.3)], 0),
        ("Office building, 60 years,\nefficient", [("mat", 45), ("man", 5), ("use", 45), ("eol", 5)], 0),
        ("Onshore wind turbine,\n20–25 years", [("mat", 75), ("man", 15), ("tr", 5), ("use", 5)], -10),
        ("Smartphone, 3 years", [("mm", 75), ("tr", 3), ("use", 20), ("eol", 2)], 0),
        ("Hip implant, 20 years", [("mm", 90), ("tr", 5), ("eol", 5)], 0),
    ]
    y = np.arange(len(rows))[::-1]
    for yy, (name, segs, credit) in zip(y, rows):
        left = 0
        for key, v in segs:
            hatch = "////" if key == "mm" else None
            ax.barh(yy, v, left=left, height=0.62, color=cols[key], edgecolor="white" if hatch else "none",
                    hatch=hatch, lw=0)
            if v >= 8:
                tc = "white" if key in ("mat", "mm", "man") else INK
                ax.text(left + v / 2, yy, f"{v:g} %", ha="center", va="center", fontsize=7.4, color=tc,
                        bbox=dict(fc=cols[key], ec="none", pad=0.5) if key == "mm" else None)
            left += v
        if credit:
            ax.barh(yy, credit, left=0, height=0.62, color="white", edgecolor="0.45", hatch="xxx", lw=0.6)
            ax.text(credit - 0.8, yy, f"recycling\ncredit {credit:g} %".replace("-", "−"), ha="right",
                    va="center", fontsize=6.8, color="0.3")
    # small-value annotations
    ax.annotate("materials + manufacture < 1 %", xy=(0.4, y[2] + 0.31), xytext=(3, y[2] + 0.55), fontsize=7,
                va="center", color="0.25", arrowprops=dict(arrowstyle="-", color="0.4", lw=0.7))
    ax.text(101, y[6], "(no use-phase energy)", fontsize=7, va="center", ha="left", color="0.3")
    ax.axvline(0, color=INK, lw=0.8)
    ax.set_yticks(y)
    ax.set_yticklabels([r[0] for r in rows], fontsize=8)
    ax.tick_params(axis="y", length=0)
    ax.set_xlim(-30, 100)
    ax.spines["left"].set_visible(False)
    ax.set_xticks([0, 20, 40, 60, 80, 100])
    ax.set_xlabel("share of lifecycle carbon (%)")
    ax.set_ylim(-0.6, len(rows) - 0.2)
    handles = [Patch(color=cols["mat"], label="material production"),
               Patch(fc=cols["mm"], ec="white", hatch="////", label="materials + manufacture"),
               Patch(color=cols["man"], label="manufacture / construction"),
               Patch(color=cols["tr"], label="transport"),
               Patch(color=cols["use"], label="use"),
               Patch(color=cols["eol"], label="end of life")]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=3, fontsize=7.4,
              handlelength=1.4, columnspacing=1.0)
    fig.text(0.02, 0.97, "The dominant phase sets the design strategy.", fontsize=8.2, style="italic", va="top")
    save(fig, "59", "fig-59-4-life-phase-breakdown")


# ---------------------------------------------------------------- Figure 59.5
def criticality_matrix():
    fig, ax = new_fig(6.6, 4.6)
    fam = {"energy": BLUE, "digital": PINK, "structural": VERM}
    pts = [  # name, EI, SR, family, label offset (pt), ha
        ("heavy rare earths", 4.0, 5.5, "energy", (8, 0), "left"),
        ("light rare earths", 4.0, 4.0, "energy", (8, 0), "left"),
        ("magnesium", 7.0, 4.0, "structural", (8, 0), "left"),
        ("gallium", 3.4, 1.8, "digital", (-8, 6), "right"),
        ("germanium", 3.5, 3.9, "digital", (-8, -4), "right"),
        ("niobium", 6.0, 4.4, "structural", (8, 0), "left"),
        ("tungsten", 8.0, 1.2, "structural", (0, 9), "center"),
        ("cobalt", 6.0, 2.5, "energy", (8, 0), "left"),
        ("natural graphite", 3.6, 1.8, "energy", (-4, -11), "right"),
        ("lithium", 4.0, 1.9, "energy", (8, 0), "left"),
        ("iron ore", 6.5, 0.5, "structural", (6, -6), "left"),
        ("aluminium / bauxite", 5.5, 0.6, "structural", (4, 10), "center"),
        ("copper", 5.0, 0.3, "energy", (8, -2), "left"),
        ("nickel", 5.0, 0.5, "energy", (-8, 3), "right"),
        ("zinc", 4.5, 0.3, "structural", (-8, -2), "right"),
    ]
    ax.add_patch(Rectangle((2.8, 1.0), 10, 10, fc=VERM, alpha=0.08, ec="none"))
    ax.axvline(2.8, ls="--", color="0.35", lw=1)
    ax.axhline(1.0, ls="--", color="0.35", lw=1)
    ax.text(8.4, 5.85, "critical", fontsize=11, color=VERM, ha="right", va="top", fontweight="bold")
    ax.text(2.75, 5.85, "economic importance\nthreshold 2.8", fontsize=7.2, ha="right", va="top", color="0.35")
    ax.text(0.1, 1.05, "supply-risk threshold 1.0", fontsize=7.2, ha="left", va="bottom", color="0.35")
    for n, ei, sr, f, off, ha in pts:
        crit = ei >= 2.8 and sr >= 1.0
        ax.plot(ei, sr, "o", ms=7, color=fam[f], mfc=fam[f] if crit else "white", mew=1.4, zorder=4)
        ax.annotate(n, (ei, sr), xytext=off, textcoords="offset points", ha=ha, va="center", fontsize=7.5)
    # platinum-group metals: a range of supply risk
    ax.plot([5.5, 5.5], [2.5, 3.0], color=fam["energy"], lw=3, solid_capstyle="round", zorder=4)
    ax.plot(5.5, 2.75, "o", ms=7, color=fam["energy"], zorder=5)
    ax.annotate("platinum-group metals", (5.5, 2.75), xytext=(-8, 0), textcoords="offset points", ha="right",
                va="center", fontsize=7.5)
    ax.set_xlim(0, 8.5)
    ax.set_ylim(0, 6)
    ax.set_xlabel("economic importance (scaled)")
    ax.set_ylabel("supply risk")
    handles = [Line2D([], [], marker="o", ls="", color=c, ms=7, label=k) for k, c in fam.items()]
    handles.append(Line2D([], [], marker="o", ls="", color="0.4", mfc="white", ms=7, mew=1.4,
                          label="non-critical (open)"))
    ax.legend(handles=handles, loc="upper left", fontsize=7.4, title="main end use", title_fontsize=7.6,
              bbox_to_anchor=(0.0, 0.88))
    fig.text(0.99, -0.01, "Illustrative of EU-type assessments; positions vary between assessments and years.",
             ha="right", va="top", fontsize=7.4, style="italic", color="0.3")
    save(fig, "59", "fig-59-5-criticality-matrix")


# ---------------------------------------------------------------- Figure 59.6
def recycled_content_limits():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.8, 3.6), gridspec_kw=dict(wspace=0.32))
    x = np.linspace(0, 1, 200)
    for cs, col in ((0.25, BLUE), (0.30, VERM)):
        a1.plot(x, 0.01 + (cs - 0.01) * x, color=col, lw=1.8, label=f"scrap {cs:.2f} % Cu")
    a1.legend(loc="upper left", fontsize=7.6, handlelength=1.6)
    for lim, lab in ((0.10, "deep-drawing sheet 0.10 %"), (0.20, "structural sections 0.20 %")):
        a1.axhline(lim, ls="--", color="0.4", lw=1)
        if lim < 0.15:
            a1.text(0.98, lim - 0.006, lab, fontsize=7.4, color="0.25", va="top", ha="right")
        else:
            a1.text(0.02, lim + 0.005, lab, fontsize=7.4, color="0.25", va="bottom", ha="left")
    a1.annotate("rebar 0.40 % (off scale)", xy=(0.78, 0.345), xytext=(0.78, 0.31), fontsize=7.4, ha="center",
                va="top", color="0.25", arrowprops=dict(arrowstyle="-|>", color="0.4", lw=0.9))
    for cs, col in ((0.25, BLUE), (0.30, VERM)):
        xi = 0.09 / (cs - 0.01)
        a1.plot([xi, xi], [0, 0.10], ":", color=col, lw=1.1)
        a1.plot(xi, 0.10, "o", color=col, ms=5, zorder=5)
        a1.text(xi + (0.012 if cs == 0.25 else -0.012), 0.012, f"x = {xi:.3g}" if cs == 0.25 else f"x = {xi:.2f}",
                color=col, fontsize=7.4, ha="left" if cs == 0.25 else "right", va="bottom")
    a1.set_xlim(0, 1)
    a1.set_ylim(0, 0.35)
    a1.set_xlabel("scrap fraction in charge, x")
    a1.set_ylabel("Cu content of melt (wt %)")

    g = np.linspace(0, 0.05, 200)
    for L, c, col, lab in ((15, 0.70, ORANGE, "L = 15 yr, $c$ = 0.70\n(packaging, consumer Al)"),
                           (40, 0.85, BLUE, "L = 40 yr, $c$ = 0.85\n(steel in buildings)")):
        a2.plot(g * 100, c / (1 + g) ** L, color=col, lw=1.8)
        gm = np.array([0, 0.01, 0.02, 0.03, 0.05]) if L == 40 else np.array([0, 0.02, 0.05])
        a2.plot(gm * 100, c / (1 + gm) ** L, "o", color=col, ms=4)
        for gg in gm:
            v = c / (1 + gg) ** L
            a2.text(gg * 100 + 0.08, v + 0.015, f"{v:.2f}", fontsize=6.8, color=col, va="bottom")
    a2.text(2.45, 0.66, "L = 15 yr, $c$ = 0.70\n(packaging, consumer Al)", color=ORANGE, fontsize=7.2)
    a2.text(0.15, 0.13, "L = 40 yr, $c$ = 0.85\n(steel in buildings,\ninfrastructure)", color=BLUE, fontsize=7.2)
    a2.text(4.95, 0.97, "growth, not collection,\nlimits recycled content", ha="right", va="top", fontsize=7.6,
            style="italic")
    a2.set_xlim(0, 5)
    a2.set_ylim(0, 1)
    a2.set_xlabel("annual demand growth rate g (%/yr)")
    a2.set_ylabel(r"max. recycled share $S/D=c/(1+g)^L$")
    save(fig, "59", "fig-59-6-recycled-content-limits")


if __name__ == "__main__":
    global_material_production()
    steel_sankey()
    beam_embodied_carbon()
    life_phase_breakdown()
    criticality_matrix()
    recycled_content_limits()
