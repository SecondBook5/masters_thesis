"""Four method schematics (fig1-panel-a..d) for the StageBridge defense deck (Act I).

These are CONCEPTUAL diagrams of the method -- no data values, no fabricated numbers.
Each panel matches the spoken script for its frame:

  a) "One measurement, two disjoint readings" -- a Visium spot deconvolved into
     receiver state z (773 named programs = 14 pathways + 759 TFs) and ecological
     context w (35 channels), with an anti-leakage strip between them.
  b) "Correspondence is estimated within ecological strata" -- source/target cells
     grouped into coarse strata; OT lines solved inside each stratum only, never
     crossing a boundary; context withheld from the cost.
  c) "The field is structured, context enters through a waist" -- the two-branch
     field: intrinsic branch (own state + tau) and context branch (w -> bounded
     14-d gate -> multiply pathway activities -> expand). The 14-channel waist is
     the stated limitation.
  d) "One start state, two integrations" -- one z0 integrated twice (full vs
     self-only), the endpoint gap = R_cond, a within-receiver residual.

Clean, presentation-scale, white background. Colors match the deck (key blue #19376e).
"""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import matplotlib.patheffects as pe
import numpy as np
import os

KEY  = "#19376e"   # deck 'key' blue
EPI  = "#b0392b"   # receiver / epithelial (warm)
CTX  = "#1f7a4d"   # context (green)
INK  = "#222222"
GREY = "#8a8a8a"
OUT  = "/home/booka/masters_thesis/presentation/figures"
os.makedirs(OUT, exist_ok=True)

def box(ax, x, y, w, h, text, color, fs=13, fc="white", tcolor=None, lw=2.2):
    b = FancyBboxPatch((x-w/2, y-h/2), w, h, boxstyle="round,pad=0.02,rounding_size=0.10",
                       linewidth=lw, edgecolor=color, facecolor=fc, zorder=3)
    ax.add_patch(b)
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, fontweight="bold",
            color=tcolor or color, zorder=4)

def arrow(ax, xy_from, xy_to, color=INK, lw=2.4, style="-|>", rad=0.0, ls="-"):
    a = FancyArrowPatch(xy_from, xy_to, connectionstyle=f"arc3,rad={rad}",
                        arrowstyle=style, mutation_scale=16, lw=lw, color=color,
                        linestyle=ls, zorder=2)
    ax.add_patch(a)

# ============================ PANEL A ============================
# Visium spot -> deconvolution -> z (receiver) + w (context), anti-leakage strip
def panel_a():
    fig, ax = plt.subplots(figsize=(8.6, 5.6)); ax.set_xlim(0, 12); ax.set_ylim(0, 8)
    ax.axis("off"); fig.patch.set_facecolor("white")
    # spot
    sp = Circle((1.9, 4.0), 1.05, facecolor="#eee6f0", edgecolor=KEY, lw=2.4, zorder=3)
    ax.add_patch(sp)
    # multicellular dots inside
    rng = np.random.default_rng(3)
    for _ in range(26):
        r, th = 0.9*np.sqrt(rng.random()), rng.random()*2*np.pi
        col = rng.choice([EPI, CTX, GREY, GREY])
        ax.scatter(1.9+r*np.cos(th), 4.0+r*np.sin(th), s=26, color=col, zorder=4, alpha=0.85)
    ax.text(1.9, 5.55, "Visium spot", ha="center", fontsize=12, fontweight="bold", color=KEY)
    ax.text(1.9, 2.25, "multicellular", ha="center", fontsize=9.5, color="#666", style="italic")
    # deconvolution
    box(ax, 4.55, 4.0, 1.5, 0.95, "DestVI\ndeconv.", KEY, fs=11)
    arrow(ax, (3.0, 4.0), (3.78, 4.0), color=KEY)
    # two disjoint outputs
    arrow(ax, (5.32, 4.4), (6.5, 6.0), color=EPI, rad=0.12)
    arrow(ax, (5.32, 3.6), (6.5, 2.0), color=CTX, rad=-0.12)
    box(ax, 8.7, 6.05, 4.0, 1.5,
        "receiver state  $z$\n773 named programs\n(14 pathways + 759 TFs)", EPI, fs=11.5)
    box(ax, 8.7, 1.95, 4.0, 1.5,
        "ecological context  $w$\n35 channels\n(non-epithelial + neighborhood)", CTX, fs=11.5)
    # anti-leakage strip between them
    ax.plot([6.7, 10.7], [4.0, 4.0], color="#444", lw=1.6, ls=(0,(5,3)), zorder=2)
    ax.text(8.7, 4.30, "anti-leakage strip", ha="center", fontsize=10.5, color="#444",
            fontweight="bold", style="italic",
            path_effects=[pe.withStroke(linewidth=3, foreground="white")])
    ax.text(8.7, 3.66, "epithelial / whole-spot / stage / donor removed from $w$",
            ha="center", fontsize=8.5, color="#666")
    ax.text(8.7, 0.55, "the two representations are disjoint by construction", ha="center",
            va="center", fontsize=10.5, color=KEY, fontweight="bold")
    fig.savefig(f"{OUT}/fig1-panel-a.pdf", bbox_inches="tight", facecolor="white")
    fig.savefig(f"{OUT}/fig1-panel-a.png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)

# ============================ PANEL B ============================
# Stratified OT: source/target populations, coarse strata, OT within stratum only
def panel_b():
    fig, ax = plt.subplots(figsize=(8.6, 5.6)); ax.set_xlim(0, 12); ax.set_ylim(0, 8)
    ax.axis("off"); fig.patch.set_facecolor("white")
    ax.text(2.4, 7.4, "source stage", ha="center", fontsize=12, fontweight="bold", color=INK)
    ax.text(9.6, 7.4, "target stage", ha="center", fontsize=12, fontweight="bold", color=INK)
    strata = [("stratum 0", 5.6, "#f2d9b8"), ("stratum 1", 3.7, "#d9c2e0"), ("stratum 2", 1.8, "#c2dce0")]
    rng = np.random.default_rng(7)
    for name, yc, col in strata:
        # stratum bands
        ax.add_patch(FancyBboxPatch((1.0, yc-0.72), 2.8, 1.44, boxstyle="round,pad=0.02,rounding_size=0.08",
                                    facecolor=col, edgecolor="none", alpha=0.55, zorder=1))
        ax.add_patch(FancyBboxPatch((8.2, yc-0.72), 2.8, 1.44, boxstyle="round,pad=0.02,rounding_size=0.08",
                                    facecolor=col, edgecolor="none", alpha=0.55, zorder=1))
        ax.text(0.85, yc, name, ha="right", va="center", fontsize=9.5, color="#555", rotation=90)
        # cells
        srcx = 1.4 + rng.random(5)*2.0; srcy = yc-0.5 + rng.random(5)*1.0
        tgtx = 8.6 + rng.random(5)*2.0; tgty = yc-0.5 + rng.random(5)*1.0
        ax.scatter(srcx, srcy, s=45, color=EPI, zorder=4, edgecolor="white", lw=0.6)
        ax.scatter(tgtx, tgty, s=45, color=KEY, zorder=4, edgecolor="white", lw=0.6)
        # OT lines WITHIN this stratum only
        for i in range(5):
            j = rng.integers(0, 5)
            arrow(ax, (srcx[i], srcy[i]), (tgtx[j], tgty[j]), color=GREY, lw=1.1, style="-", rad=0.05)
    # emphasise: no line crosses a boundary; context withheld
    ax.text(6.0, 0.55, "OT solved inside each stratum, regulatory-distance cost only",
            ha="center", fontsize=10.5, color=KEY, fontweight="bold",
            path_effects=[pe.withStroke(linewidth=3, foreground="white")])
    ax.text(6.0, 6.5, "context withheld from the cost", ha="center", fontsize=10,
            color=CTX, fontweight="bold", style="italic")
    fig.savefig(f"{OUT}/fig1-panel-b.pdf", bbox_inches="tight", facecolor="white")
    fig.savefig(f"{OUT}/fig1-panel-b.png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)

# ============================ PANEL C ============================
# Two-branch field; context enters through a 14-d gated waist
def panel_c():
    fig, ax = plt.subplots(figsize=(10.2, 5.4)); ax.set_xlim(0, 14); ax.set_ylim(0, 8)
    ax.axis("off"); fig.patch.set_facecolor("white")
    # inputs
    box(ax, 1.5, 6.2, 2.2, 1.0, "state $z$, $\\tau$", EPI, fs=12)
    box(ax, 1.5, 2.0, 2.2, 1.0, "context $w$", CTX, fs=12)
    # intrinsic branch
    box(ax, 5.7, 6.2, 3.8, 1.5, "intrinsic branch\nlow-rank $A$ + pathway map\n+ neural residual", EPI, fs=10.5)
    arrow(ax, (2.6, 6.2), (3.72, 6.2), color=EPI)
    # context branch through a WAIST
    box(ax, 4.7, 2.0, 1.9, 1.0, "bounded\ngate", CTX, fs=10.5)
    arrow(ax, (2.6, 2.0), (3.75, 2.0), color=CTX)
    # the waist: 14 channels
    ax.add_patch(Circle((7.0, 2.0), 0.42, facecolor="white", edgecolor=CTX, lw=2.6, zorder=4))
    ax.text(7.0, 2.0, "14", ha="center", va="center", fontsize=12, fontweight="bold", color=CTX, zorder=5)
    arrow(ax, (5.65, 2.0), (6.55, 2.0), color=CTX)
    ax.text(7.0, 1.25, "14-d waist", ha="center", fontsize=9.5, color=CTX, fontweight="bold")
    # multiply against pathway activities, expand
    box(ax, 9.9, 2.0, 3.0, 1.1, "$\\times$ pathway activity\n$\\rightarrow$ expand to 773", CTX, fs=10.5)
    arrow(ax, (7.42, 2.0), (8.4, 2.0), color=CTX)
    # sum into field
    box(ax, 12.4, 4.1, 2.6, 1.3, "$dz/d\\tau$\nfull field", KEY, fs=12)
    arrow(ax, (7.4, 6.2), (11.3, 4.55), color=EPI, rad=-0.12)
    arrow(ax, (11.4, 2.0), (11.6, 3.45), color=CTX, rad=0.15)
    # limitation caption
    ax.text(7.0, 0.35, "759 TF coordinates move only through the 14-channel gate or the residual",
            ha="center", fontsize=9.5, color="#a33", style="italic", fontweight="bold")
    fig.savefig(f"{OUT}/fig1-panel-c.pdf", bbox_inches="tight", facecolor="white")
    fig.savefig(f"{OUT}/fig1-panel-c.png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)

# ============================ PANEL D ============================
# One z0, two integrations (full vs self-only), endpoint gap = R_cond
def panel_d():
    fig, ax = plt.subplots(figsize=(9.4, 5.4)); ax.set_xlim(0, 12); ax.set_ylim(0, 8)
    ax.axis("off"); fig.patch.set_facecolor("white")
    # start state
    ax.scatter([1.5], [4.0], s=160, color=INK, zorder=5)
    ax.text(1.5, 3.35, "$z_0$\nobserved", ha="center", va="top", fontsize=11, fontweight="bold", color=INK)
    # tau axis
    ax.annotate("", xy=(11.0, 0.9), xytext=(1.2, 0.9), arrowprops=dict(arrowstyle="-|>", color="#999", lw=1.6))
    ax.text(11.0, 0.55, r"$\tau$", ha="center", fontsize=12, color="#666")
    ax.text(1.3, 0.55, "0", ha="center", fontsize=10, color="#666"); ax.text(10.6, 0.55, "1", ha="center", fontsize=10, color="#666")
    t = np.linspace(0, 1, 100); xs = 1.5 + t*8.4
    # full trajectory (context on) -- curves up
    yf = 4.0 + 1.9*t + 0.5*np.sin(t*2.2)
    ax.plot(xs, yf, color=CTX, lw=3.2, zorder=4)
    ax.scatter([xs[-1]], [yf[-1]], s=110, color=CTX, zorder=5, edgecolor="white", lw=1.2)
    ax.text(xs[-1]+0.15, yf[-1], "full\n(context on)", ha="left", va="center", fontsize=10.5, color=CTX, fontweight="bold")
    # self-only trajectory (context off) -- flatter
    ys = 4.0 + 0.85*t - 0.15*np.sin(t*2.0)
    ax.plot(xs, ys, color=EPI, lw=3.2, ls=(0,(5,2)), zorder=4)
    ax.scatter([xs[-1]], [ys[-1]], s=110, color=EPI, zorder=5, edgecolor="white", lw=1.2)
    ax.text(xs[-1]+0.15, ys[-1], "self-only\n(context off)", ha="left", va="center", fontsize=10.5, color=EPI, fontweight="bold")
    # the gap = R_cond
    ax.annotate("", xy=(xs[-1], yf[-1]), xytext=(xs[-1], ys[-1]),
                arrowprops=dict(arrowstyle="<->", color=KEY, lw=2.4))
    ax.text(xs[-1]-0.25, (yf[-1]+ys[-1])/2, r"$R_{\mathrm{cond}}$", ha="right", va="center",
            fontsize=15, fontweight="bold", color=KEY,
            path_effects=[pe.withStroke(linewidth=3, foreground="white")])
    ax.text(6.0, 7.5, "one fit, one intrinsic field, context held fixed along both paths",
            ha="center", fontsize=10.5, color=KEY, fontweight="bold")
    ax.text(6.0, 0.15, "within-receiver residual, not a level; computed out of fold",
            ha="center", fontsize=9.5, color="#666", style="italic")
    fig.savefig(f"{OUT}/fig1-panel-d.pdf", bbox_inches="tight", facecolor="white")
    fig.savefig(f"{OUT}/fig1-panel-d.png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)

panel_a(); panel_b(); panel_c(); panel_d()
print("WROTE fig1-panel-a..d in", OUT)
