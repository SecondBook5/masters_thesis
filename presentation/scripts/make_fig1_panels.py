"""Four method schematics (fig1-panel-a..d) for the StageBridge defense deck (Act I).

CONCEPTUAL diagrams of the method -- no data values, no fabricated numbers.

Each panel is drawn as an ORDERED LIST OF LAYERS. The script renders, for every panel:
  - fig1-panel-X.pdf/.png        : the full (all-layers) figure  [static fallback]
  - fig1-panel-X-step1..K.png    : cumulative builds (layer 1, 1-2, ..., 1-K)
The deck flips through the step images with beamer \\only<n> overlays, so each panel
builds up element-by-element as the speaker narrates -- robust in any PDF viewer.

Axes limits and figure size are fixed per panel so cumulative frames register exactly
(step frames are saved WITHOUT bbox_inches='tight' so the canvas never shifts).

Panels (match the spoken script):
  a) One measurement, two disjoint readings -- spot -> DestVI -> receiver z (773
     named programs) + context w (35 ch), anti-leakage strip between them.
  b) Correspondence within ecological strata -- source/target cells, coarse strata,
     OT solved inside each stratum only, context withheld from the cost.
  c) Structured field, context through a 14-d gated waist -- intrinsic branch +
     context branch (gate -> 14 -> x pathway activity -> expand to 773).
  d) One start state, two integrations -- z0 integrated full vs self-only,
     endpoint gap = R_cond, a within-receiver residual.
"""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import matplotlib.patheffects as pe
import numpy as np
import os

KEY  = "#19376e"; EPI = "#b0392b"; CTX = "#1f7a4d"; INK = "#222222"; GREY = "#8a8a8a"
OUT  = "/home/booka/masters_thesis/presentation/figures"
os.makedirs(OUT, exist_ok=True)

def _box(ax, x, y, w, h, text, color, fs=13, fc="white", tcolor=None, lw=2.2):
    ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h, boxstyle="round,pad=0.02,rounding_size=0.10",
                                linewidth=lw, edgecolor=color, facecolor=fc, zorder=3))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, fontweight="bold",
            color=tcolor or color, zorder=4)

def _arrow(ax, a, b, color=INK, lw=2.4, style="-|>", rad=0.0, ls="-"):
    ax.add_patch(FancyArrowPatch(a, b, connectionstyle=f"arc3,rad={rad}", arrowstyle=style,
                                 mutation_scale=16, lw=lw, color=color, linestyle=ls, zorder=2))

def render(name, figsize, xlim, ylim, layers):
    """Render full figure + cumulative step frames from an ordered list of layer fns."""
    def _fresh():
        fig, ax = plt.subplots(figsize=figsize); ax.set_xlim(*xlim); ax.set_ylim(*ylim)
        ax.axis("off"); fig.patch.set_facecolor("white"); return fig, ax
    fig, ax = _fresh()
    for L in layers: L(ax)
    fig.savefig(f"{OUT}/{name}.pdf", bbox_inches="tight", facecolor="white")
    fig.savefig(f"{OUT}/{name}.png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    # cumulative steps -- fixed bbox (NO bbox_inches='tight') so frames register exactly
    for k in range(1, len(layers) + 1):
        fig, ax = _fresh()
        for L in layers[:k]: L(ax)
        fig.savefig(f"{OUT}/{name}-step{k}.png", dpi=170, facecolor="white")
        plt.close(fig)
    print(f"{name}: full + {len(layers)} steps")

# ============================ PANEL A ============================
def _a_layers():
    rng = np.random.default_rng(3)
    dots = [(0.9*np.sqrt(rng.random()), rng.random()*2*np.pi, rng.choice([EPI,CTX,GREY,GREY])) for _ in range(26)]
    def spot(ax):
        ax.add_patch(Circle((1.9,4.0),1.05,facecolor="#eee6f0",edgecolor=KEY,lw=2.4,zorder=3))
        for r,th,c in dots: ax.scatter(1.9+r*np.cos(th),4.0+r*np.sin(th),s=26,color=c,zorder=4,alpha=0.85)
        ax.text(1.9,5.55,"Visium spot",ha="center",fontsize=12,fontweight="bold",color=KEY)
        ax.text(1.9,2.25,"multicellular",ha="center",fontsize=9.5,color="#666",style="italic")
    def deconv(ax):
        _box(ax,4.55,4.0,1.5,0.95,"DestVI\ndeconv.",KEY,fs=11); _arrow(ax,(3.0,4.0),(3.78,4.0),color=KEY)
    def zbox(ax):
        _arrow(ax,(5.32,4.4),(6.5,6.0),color=EPI,rad=0.12)
        _box(ax,8.7,6.05,4.0,1.5,"receiver state  $z$\n773 named programs\n(14 pathways + 759 TFs)",EPI,fs=11.5)
    def wbox(ax):
        _arrow(ax,(5.32,3.6),(6.5,2.0),color=CTX,rad=-0.12)
        _box(ax,8.7,1.95,4.0,1.5,"ecological context  $w$\n35 channels\n(non-epithelial + neighborhood)",CTX,fs=11.5)
    def strip(ax):
        ax.plot([6.7,10.7],[4.0,4.0],color="#444",lw=1.6,ls=(0,(5,3)),zorder=2)
        ax.text(8.7,4.30,"anti-leakage strip",ha="center",fontsize=10.5,color="#444",fontweight="bold",
                style="italic",path_effects=[pe.withStroke(linewidth=3,foreground="white")])
        ax.text(8.7,3.66,"epithelial / whole-spot / stage / donor removed from $w$",ha="center",fontsize=8.5,color="#666")
        ax.text(8.7,0.55,"the two representations are disjoint by construction",ha="center",va="center",
                fontsize=10.5,color=KEY,fontweight="bold")
    return [spot, deconv, zbox, wbox, strip]

# ============================ PANEL B ============================
def _b_layers():
    strata=[("stratum 0",5.6,"#f2d9b8"),("stratum 1",3.7,"#d9c2e0"),("stratum 2",1.8,"#c2dce0")]
    rng=np.random.default_rng(7)
    pts={}
    for nm,yc,col in strata:
        pts[nm]=(1.4+rng.random(5)*2.0, yc-0.5+rng.random(5)*1.0, 8.6+rng.random(5)*2.0, yc-0.5+rng.random(5)*1.0,
                 rng.integers(0,5,5))
    def cells(ax):
        ax.text(2.4,7.4,"source stage",ha="center",fontsize=12,fontweight="bold",color=INK)
        ax.text(9.6,7.4,"target stage",ha="center",fontsize=12,fontweight="bold",color=INK)
        for nm,yc,col in strata:
            sx,sy,tx,ty,_=pts[nm]
            ax.scatter(sx,sy,s=45,color=EPI,zorder=4,edgecolor="white",lw=0.6)
            ax.scatter(tx,ty,s=45,color=KEY,zorder=4,edgecolor="white",lw=0.6)
    def bands(ax):
        for nm,yc,col in strata:
            ax.add_patch(FancyBboxPatch((1.0,yc-0.72),2.8,1.44,boxstyle="round,pad=0.02,rounding_size=0.08",
                         facecolor=col,edgecolor="none",alpha=0.55,zorder=1))
            ax.add_patch(FancyBboxPatch((8.2,yc-0.72),2.8,1.44,boxstyle="round,pad=0.02,rounding_size=0.08",
                         facecolor=col,edgecolor="none",alpha=0.55,zorder=1))
            ax.text(0.85,yc,nm,ha="right",va="center",fontsize=9.5,color="#555",rotation=90)
    def otlines(ax):
        for nm,yc,col in strata:
            sx,sy,tx,ty,j=pts[nm]
            for i in range(5): _arrow(ax,(sx[i],sy[i]),(tx[j[i]],ty[j[i]]),color=GREY,lw=1.1,style="-",rad=0.05)
    def caps(ax):
        ax.text(6.0,6.5,"context withheld from the cost",ha="center",fontsize=10,color=CTX,fontweight="bold",style="italic")
        ax.text(6.0,0.55,"OT solved inside each stratum, regulatory-distance cost only",ha="center",fontsize=10.5,
                color=KEY,fontweight="bold",path_effects=[pe.withStroke(linewidth=3,foreground="white")])
    return [cells, bands, otlines, caps]

# ============================ PANEL C ============================
def _c_layers():
    def inputs(ax):
        _box(ax,1.5,6.2,2.2,1.0,"state $z$, $\\tau$",EPI,fs=12)
        _box(ax,1.5,2.0,2.2,1.0,"context $w$",CTX,fs=12)
    def intrinsic(ax):
        _box(ax,5.7,6.2,3.8,1.5,"intrinsic branch\nlow-rank $A$ + pathway map\n+ neural residual",EPI,fs=10.5)
        _arrow(ax,(2.6,6.2),(3.72,6.2),color=EPI)
    def context(ax):
        _box(ax,4.7,2.0,1.9,1.0,"bounded\ngate",CTX,fs=10.5); _arrow(ax,(2.6,2.0),(3.75,2.0),color=CTX)
        ax.add_patch(Circle((7.0,2.0),0.42,facecolor="white",edgecolor=CTX,lw=2.6,zorder=4))
        ax.text(7.0,2.0,"14",ha="center",va="center",fontsize=12,fontweight="bold",color=CTX,zorder=5)
        _arrow(ax,(5.65,2.0),(6.55,2.0),color=CTX); ax.text(7.0,1.25,"14-d waist",ha="center",fontsize=9.5,color=CTX,fontweight="bold")
        _box(ax,9.9,2.0,3.0,1.1,"$\\times$ pathway activity\n$\\rightarrow$ expand to 773",CTX,fs=10.5)
        _arrow(ax,(7.42,2.0),(8.4,2.0),color=CTX)
    def field(ax):
        _box(ax,12.4,4.1,2.6,1.3,"$dz/d\\tau$\nfull field",KEY,fs=12)
        _arrow(ax,(7.4,6.2),(11.3,4.55),color=EPI,rad=-0.12); _arrow(ax,(11.4,2.0),(11.6,3.45),color=CTX,rad=0.15)
    def limit(ax):
        ax.text(7.0,0.35,"759 TF coordinates move only through the 14-channel gate or the residual",
                ha="center",fontsize=9.5,color="#a33",style="italic",fontweight="bold")
    return [inputs, intrinsic, context, field, limit]

# ============================ PANEL D ============================
def _d_layers():
    t=np.linspace(0,1,100); xs=1.5+t*8.4
    yf=4.0+1.9*t+0.5*np.sin(t*2.2); ys=4.0+0.85*t-0.15*np.sin(t*2.0)
    def start(ax):
        ax.scatter([1.5],[4.0],s=160,color=INK,zorder=5)
        ax.text(1.5,3.35,"$z_0$\nobserved",ha="center",va="top",fontsize=11,fontweight="bold",color=INK)
        ax.annotate("",xy=(11.0,0.9),xytext=(1.2,0.9),arrowprops=dict(arrowstyle="-|>",color="#999",lw=1.6))
        ax.text(11.0,0.55,r"$\tau$",ha="center",fontsize=12,color="#666")
        ax.text(1.3,0.55,"0",ha="center",fontsize=10,color="#666"); ax.text(10.6,0.55,"1",ha="center",fontsize=10,color="#666")
        ax.text(6.0,7.5,"one fit, one intrinsic field, context held fixed along both paths",ha="center",fontsize=10.5,color=KEY,fontweight="bold")
    def full(ax):
        ax.plot(xs,yf,color=CTX,lw=3.2,zorder=4)
        ax.scatter([xs[-1]],[yf[-1]],s=110,color=CTX,zorder=5,edgecolor="white",lw=1.2)
        ax.text(xs[-1]+0.15,yf[-1],"full\n(context on)",ha="left",va="center",fontsize=10.5,color=CTX,fontweight="bold")
    def selfonly(ax):
        ax.plot(xs,ys,color=EPI,lw=3.2,ls=(0,(5,2)),zorder=4)
        ax.scatter([xs[-1]],[ys[-1]],s=110,color=EPI,zorder=5,edgecolor="white",lw=1.2)
        ax.text(xs[-1]+0.15,ys[-1],"self-only\n(context off)",ha="left",va="center",fontsize=10.5,color=EPI,fontweight="bold")
    def gap(ax):
        ax.annotate("",xy=(xs[-1],yf[-1]),xytext=(xs[-1],ys[-1]),arrowprops=dict(arrowstyle="<->",color=KEY,lw=2.4))
        ax.text(xs[-1]-0.25,(yf[-1]+ys[-1])/2,r"$R_{\mathrm{cond}}$",ha="right",va="center",fontsize=15,fontweight="bold",
                color=KEY,path_effects=[pe.withStroke(linewidth=3,foreground="white")])
        ax.text(6.0,0.15,"within-receiver residual, not a level; computed out of fold",ha="center",fontsize=9.5,color="#666",style="italic")
    return [start, full, selfonly, gap]

render("fig1-panel-a", (8.6,5.6), (0,12), (0,8), _a_layers())
render("fig1-panel-b", (8.6,5.6), (0,12), (0,8), _b_layers())
render("fig1-panel-c", (10.2,5.4), (0,14), (0,8), _c_layers())
render("fig1-panel-d", (9.4,5.4), (0,12), (0,8), _d_layers())
print("DONE: 4 panels, full + cumulative steps")
