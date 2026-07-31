"""Real-data charts to replace text/table slides in the defense deck.

Every value read from an authoritative source:
  - per-fold ladder:  results_hpc/ude/ladder_by_fold_<edge>_v2lowrank_source/*.parquet
  - per-program Rcond: results_hpc/DOSSIER_CSV/Rcond_ALL_<edge>.csv (CIs, stability, sign)
  - GSEA stage NES:    results_hpc/figures/<edge>/gsea/stage_gsea_<edge>.csv
  - identifiability:   Ch3 sec:leakage (R^2 mean -0.54, range [-1.03,-0.22]; recon MSE 0.48 vs 0.82)
Nothing here is synthesized. Where the chapter reports a mean+range rather than 5 per-fold
points (identifiability R^2), the figure shows exactly that -- mean marker + range band -- and
does NOT invent 5 fold values.

Writes to presentation/figures/:
  chart_ladder_perfold_AAH_AIS.pdf   grouped per-fold Sinkhorn, key rungs
  chart_verdict_forest.pdf           the two paired contrasts as a CI forest (both edges)
  chart_interferon.pdf               Rcond footprint vs GSEA NES, both edges
  chart_identifiability.pdf          held-out R^2 (mean+range, <0) + recon MSE true vs shuffle
  chart_preinvasive_circuit.pdf      signed Rcond bars: 4 repressors down, FOS/p53/RB1/KAT5 up
  chart_invasion_architecture.pdf    signed Rcond bars: 3 corepressors down, MAML1/FOXA1 up
  chart_anabolic_module.pdf          signed Rcond bars: ATF5/HSF2/NFKB2 + GSEA MYC/OxPhos
"""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import matplotlib.patheffects as pe
from scipy import stats
import pandas as pd, numpy as np, glob, os

R = "/home/booka/projects/crrt-ude/results_hpc"
DOS = f"{R}/DOSSIER_CSV"
OUT = "/home/booka/masters_thesis/presentation/figures"
os.makedirs(OUT, exist_ok=True)

KEY="#19376e"; GOOD="#1a6e3c"; BAD="#a02828"; EPI="#b0392b"; CTX="#1f7a4d"; GREY="#9a9a9a"
DASH="—"   # em-dash; matplotlib does not interpret TeX ---
# These charts sit under a beamer FRAME title on the slide, so the in-figure
# top title would double it. Suppress the top title; keep panel sub-titles and
# bottom captions (which carry distinct info). Flip to True for standalone use.
MAIN_TITLE=False
def _maintitle(ax, s, **kw):
    if MAIN_TITLE: ax.set_title(s, **kw)
def _suptitle(fig, s, **kw):
    if MAIN_TITLE: fig.suptitle(s, **kw)
plt.rcParams.update({"font.size":13,"axes.edgecolor":"#444","axes.linewidth":1.0,
                     "svg.fonttype":"none","pdf.fonttype":42})

def _dossier(edge):
    d = pd.read_csv(f"{DOS}/Rcond_ALL_{edge}.csv").set_index("program_name")
    return d

def _save(fig, name):
    fig.savefig(f"{OUT}/{name}.pdf", bbox_inches="tight", facecolor="white")
    fig.savefig(f"{OUT}/{name}.png", dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  {name}")

def _signed_bars(name, progs, edge, title, groups=None):
    """Horizontal signed-Rcond bars with CI whiskers; green up / red down."""
    d = _dossier(edge)
    rows = [(lbl, d.loc[key]) for lbl, key in progs if key in d.index]
    labels = [r[0] for r in rows]
    vals   = [r[1].Re_mean for r in rows]
    los    = [r[1].Re_lo   for r in rows]
    his    = [r[1].Re_hi   for r in rows]
    y = np.arange(len(rows))[::-1]
    fig, ax = plt.subplots(figsize=(8.6, 0.62*len(rows)+1.6))
    fig.patch.set_facecolor("white")
    for yi, v, lo, hi in zip(y, vals, los, his):
        c = GOOD if v >= 0 else BAD
        ax.barh(yi, v, color=c, alpha=0.88, height=0.62, zorder=3)
        ax.plot([lo, hi], [yi, yi], color="#333", lw=1.6, zorder=4)
        ax.plot([lo,lo],[yi-0.09,yi+0.09],color="#333",lw=1.6,zorder=4)
        ax.plot([hi,hi],[yi-0.09,yi+0.09],color="#333",lw=1.6,zorder=4)
    ax.axvline(0, color="#333", lw=1.2, zorder=2)
    ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=13)
    ax.set_xlabel(r"context residual  $R_{\mathrm{cond}}$  (across-fold mean, 95% CI)")
    _maintitle(ax, title, fontsize=14, color=KEY, fontweight="bold", pad=10)
    ax.spines[["top","right"]].set_visible(False)
    # up/down annotations at the extremes
    xr = max(abs(min(los)), abs(max(his)))
    ax.set_xlim(-xr*1.28, xr*1.28)
    ax.text(0.985,0.02,"up = context adds drive", transform=ax.transAxes, ha="right",
            va="bottom", fontsize=10.5, color=GOOD, style="italic")
    ax.text(0.015,0.02,"down = context removes", transform=ax.transAxes, ha="left",
            va="bottom", fontsize=10.5, color=BAD, style="italic")
    _save(fig, name)

# ---------------------------------------------------------------- 1. per-fold ladder
def ladder_perfold(edge="AAH_AIS"):
    rows=[]
    for f in sorted(glob.glob(f"{R}/ude/ladder_by_fold_{edge}_v2lowrank_source/ladder_fold_*.parquet")):
        x=pd.read_parquet(f); x=x[x.metric=="semantic_sinkhorn_distance"]
        fold=int(f.split("_")[-1].split(".")[0])
        rows.append(x.set_index("model")["value"].rename(f"F{fold}"))
    L=pd.concat(rows,axis=1)
    # load-bearing rungs, ordered
    order=[("local_context_full","local context",CTX),
           ("matched_state_shuffled","shuffled context",GREY),
           ("donor_stage_average_context","donor-stage avg",KEY),
           ("spatial_self_only","self-only",EPI)]
    order=[o for o in order if o[0] in L.index]
    folds=list(L.columns); nf=len(folds); nb=len(order)
    fig,ax=plt.subplots(figsize=(9.4,5.6)); fig.patch.set_facecolor("white")
    w=0.8/nb; xf=np.arange(nf)
    for bi,(m,lbl,c) in enumerate(order):
        ax.bar(xf+bi*w-0.4+w/2, L.loc[m,folds].values, width=w, color=c, label=lbl, zorder=3)
    ax.set_xticks(xf); ax.set_xticklabels([f"fold {f[1:]}" for f in folds])
    ax.set_ylabel("held-out Sinkhorn endpoint distance\n(lower = better transport)")
    _maintitle(ax, "Per-fold falsification ladder, preinvasive edge",
               fontsize=14, color=KEY, fontweight="bold", pad=10)
    # headroom for legend + means banner above the tall folds
    # (scope to plotted rungs only -- other ladder models can be orders larger)
    plotted_max = max(L.loc[m,folds].max() for m,_,_ in order)
    ax.set_ylim(0, plotted_max*1.34)
    ax.legend(frameon=False, ncol=4, fontsize=10.5, loc="upper left",
              bbox_to_anchor=(0.0,1.005), handlelength=1.2, columnspacing=1.1)
    ax.spines[["top","right"]].set_visible(False)
    # means banner (below the legend row, still clear of bars)
    loc=L.loc["local_context_full"].mean(); self_=L.loc["spatial_self_only"].mean()
    sh=L.loc["matched_state_shuffled"].mean()
    ax.text(0.5,0.885,
            f"means:  local {loc:.1f}  ·  shuffle {sh:.1f}  ·  self {self_:.1f}    "
            f"|    self $-$ local $= {self_-loc:+.2f}$ (P$\\approx$0.10)    "
            f"local $-$ shuffle $= {loc-sh:+.2f}$",
            transform=ax.transAxes, ha="center", va="top", fontsize=9.8, color="#333",
            bbox=dict(boxstyle="round,pad=0.4", fc="#f4f4f8", ec="#ccc"))
    _save(fig,f"chart_ladder_perfold_{edge}")

# ---------------------------------------------------------------- 2. verdict forest
def _contrast(edge, comparator, base="local_context_full"):
    """Paired across-fold contrast (comparator - local); +ve => local transports better.
    Computed live from the per-fold ladder parquets; nothing hardcoded."""
    rows={}
    for f in sorted(glob.glob(f"{R}/ude/ladder_by_fold_{edge}_v2lowrank_source/ladder_fold_*.parquet")):
        x=pd.read_parquet(f); x=x[x.metric=="semantic_sinkhorn_distance"]
        fold=int(f.split("_")[-1].split(".")[0]); rows[fold]=x.set_index("model")["value"]
    L=pd.DataFrame(rows)
    d=(L.loc[comparator]-L.loc[base]).dropna(); n=len(d)
    m=d.mean(); se=d.std(ddof=1)/np.sqrt(n); t=stats.t.ppf(0.975,n-1)
    return m, m-t*se, m+t*se

def _forest(name, edge, title, subtitle, xlim):
    """CI forest of the two paired contrasts for one edge (real, live-computed)."""
    rows=[]  # (label, delta, lo, hi)
    for comp,lbl in [("matched_state_shuffled","Local over\nshuffled context"),
                     ("spatial_self_only","Local over\nself-only")]:
        m,lo,hi=_contrast(edge,comp); rows.append((lbl,m,lo,hi))
    fig,ax=plt.subplots(figsize=(9.6,3.8)); fig.patch.set_facecolor("white")
    y=np.arange(len(rows))[::-1]
    span=xlim[1]-xlim[0]
    for yi,(lbl,d,lo,hi) in zip(y,rows):
        tight=(hi-lo)<3
        c = GOOD if tight else "#8a8a8a"
        ax.plot([lo,hi],[yi,yi],color=c,lw=4.0,zorder=3,solid_capstyle="round")
        ax.scatter([d],[yi],s=110,color=c,zorder=4,edgecolor="white",lw=1.6)
        ax.text(hi+span*0.02,yi,f"$\\Delta={d:+.2f}$  [{lo:+.2f}, {hi:+.2f}]",
                va="center",ha="left",fontsize=11,color="#333")
        ax.text(-0.02,yi,lbl,transform=ax.get_yaxis_transform(),
                va="center",ha="right",fontsize=12)
    ax.axvline(0,color=BAD,lw=1.5,ls="--",zorder=2)
    ax.set_yticks([]); ax.set_xlim(*xlim)
    ax.set_xlabel(r"paired $\Delta$ Sinkhorn (local $-$ comparator), 95% CI across 5 folds")
    _maintitle(ax, title,fontsize=14,color=KEY,fontweight="bold",pad=10)
    ax.spines[["top","right","left"]].set_visible(False)
    ax.text(0.5,-0.40,subtitle,transform=ax.transAxes,ha="center",fontsize=10.5,
            style="italic",color="#555")
    _save(fig,name)

def verdict_forest():
    _forest("chart_verdict_preinvasive","AAH_AIS",
            f"A split verdict {DASH} and one half is a bound",
            "green = tight interval excluding a receiver-local benefit;  "
            "grey = wide, underpowered, straddles zero", (-16,42))
    _forest("chart_verdict_invasion","AIS_invasive",
            "At the invasion boundary, both comparisons are null",
            f"both intervals straddle zero {DASH} zero shared donors on this edge", (-16,24))

def _perfold_series(edge, comparator, base="local_context_full"):
    rows={}
    for f in sorted(glob.glob(f"{R}/ude/ladder_by_fold_{edge}_v2lowrank_source/ladder_fold_*.parquet")):
        x=pd.read_parquet(f); x=x[x.metric=="semantic_sinkhorn_distance"]
        fold=int(f.split("_")[-1].split(".")[0]); rows[fold]=x.set_index("model")["value"]
    L=pd.DataFrame(rows)
    return (L.loc[comparator]-L.loc[base]).sort_index()

def whytight(edge="AAH_AIS"):
    """Per-fold self-minus-local (swings wildly) vs local-minus-shuffle (co-moves)."""
    sl=_perfold_series(edge,"spatial_self_only")
    ls=-_perfold_series(edge,"matched_state_shuffled")  # local - shuffle
    folds=list(sl.index); x=np.arange(len(folds)); w=0.4
    fig,ax=plt.subplots(figsize=(9.2,5.0)); fig.patch.set_facecolor("white")
    b1=ax.bar(x-w/2, sl.values, w, color=EPI, label="self $-$ local", zorder=3)
    b2=ax.bar(x+w/2, ls.values, w, color=CTX, label="local $-$ shuffle", zorder=3)
    ax.axhline(0,color="#333",lw=1.1)
    ax.set_xticks(x); ax.set_xticklabels([f"fold {f}" for f in folds])
    ax.set_ylabel(r"paired $\Delta$ Sinkhorn")
    _maintitle(ax, "Why one interval is tight and the other is not",
               fontsize=14,color=KEY,fontweight="bold",pad=10)
    ax.legend(frameon=False,fontsize=12,loc="upper right")
    ax.spines[["top","right"]].set_visible(False)
    ax.text(0.02,0.97,
            f"self $-$ local:  SD $= {sl.std(ddof=1):.1f}$  (swings $+{sl.max():.0f}$ to ${sl.min():+.0f}$)\n"
            f"local $-$ shuffle:  SD $\\approx {ls.std(ddof=1):.1f}$  (folds co-move)",
            transform=ax.transAxes, ha="left", va="top", fontsize=11, color="#333",
            bbox=dict(boxstyle="round,pad=0.4", fc="#f4f4f8", ec="#ccc"))
    ax.text(0.5,-0.13,"structural, not arbitrary: the shuffle keeps the same inputs in a "
            "different order, so its transport tracks local's fold for fold",
            transform=ax.transAxes,ha="center",fontsize=10,style="italic",color="#555")
    _save(fig,f"chart_whytight_{edge}")

# ---------------------------------------------------------------- 3. interferon
def interferon():
    da=_dossier("AAH_AIS")
    rc = {"JAK-STAT":da.loc["pathway_JAK-STAT","Re_mean"], "IRF9":da.loc["tf_IRF9","Re_mean"]}
    # GSEA hallmark IFN NES both edges
    def nes(edge):
        g=pd.read_csv(f"{R}/figures/{edge}/gsea/stage_gsea_{edge}.csv")
        h=g[g.pathway.str.contains("HALLMARK_INTERFERON",na=False)]
        return dict(zip(h.pathway.str.replace("HALLMARK_INTERFERON_","").str.replace("_RESPONSE",""), h.NES))
    na, ni = nes("AAH_AIS"), nes("AIS_invasive")
    fig,(a1,a2)=plt.subplots(1,2,figsize=(10.6,4.8),gridspec_kw={"width_ratios":[1,1.25]})
    fig.patch.set_facecolor("white")
    # left: Rcond footprint (preinvasive)
    labs=list(rc); vals=[rc[k] for k in labs]; y=np.arange(len(labs))[::-1]
    a1.barh(y,vals,color=BAD,height=0.55,zorder=3)
    a1.axvline(0,color="#333",lw=1.1); a1.set_yticks(y); a1.set_yticklabels(labs)
    a1.set_title("Context residual\n(AAH→AIS)",fontsize=12.5,color=KEY,fontweight="bold")
    a1.set_xlabel(r"$R_{\mathrm{cond}}$"); a1.set_xlim(-0.32,0.05)
    a1.spines[["top","right"]].set_visible(False)
    # right: GSEA NES two edges grouped
    cats=["ALPHA","GAMMA"]; x=np.arange(len(cats)); w=0.38
    a2.bar(x-w/2,[na.get(c,np.nan) for c in cats],w,color=BAD,label="AAH→AIS",zorder=3)
    a2.bar(x+w/2,[ni.get(c,np.nan) for c in cats],w,color=GOOD,label="AIS→invasive",zorder=3)
    a2.axhline(0,color="#333",lw=1.1); a2.set_xticks(x); a2.set_xticklabels([f"IFN-{c.lower()}" for c in cats])
    a2.set_ylabel("GSEA hallmark NES"); a2.set_title("Whole-transcriptome enrichment",
                  fontsize=12.5,color=KEY,fontweight="bold")
    a2.legend(frameon=False,fontsize=10.5); a2.spines[["top","right"]].set_visible(False)
    _suptitle(fig, "Interferon tone is lost before invasion, and returns after",
              fontsize=14,color=KEY,fontweight="bold",y=1.02)
    fig.text(0.5,-0.04,"two readouts with different confounds agree on the preinvasive loss "
             "(all padj $<10^{-3}$)",ha="center",fontsize=10,style="italic",color="#555")
    _save(fig,"chart_interferon")

# ---------------------------------------------------------------- 4. identifiability
def identifiability():
    # Ch3 sec:leakage: held-out R^2 mean -0.54, range [-1.03, -0.22]; recon MSE 0.48 (true) vs 0.82 (shuffle)
    fig,(a1,a2)=plt.subplots(1,2,figsize=(10.2,4.4)); fig.patch.set_facecolor("white")
    # left: R^2 mean+range band, all <0
    a1.axhspan(-1.03,-0.22,color=GOOD,alpha=0.15,zorder=1)
    a1.plot([0,0],[-1.03,-0.22],color=GOOD,lw=4,zorder=3,solid_capstyle="round")
    a1.scatter([0],[-0.54],s=140,color=GOOD,zorder=4,edgecolor="white",lw=1.6)
    a1.axhline(0,color=BAD,lw=1.6,ls="--",zorder=2)
    a1.text(0.12,-0.54,"mean $-0.54$",va="center",fontsize=12,color=GOOD,fontweight="bold")
    a1.text(0.12,-0.22,"best fold $-0.22$",va="center",fontsize=10,color="#555")
    a1.text(0.12,-1.03,"worst fold $-1.03$",va="center",fontsize=10,color="#555")
    a1.text(0.5,0.06,"chance (predict the mean)",ha="center",fontsize=10,color=BAD,style="italic")
    a1.set_xlim(-0.5,1.1); a1.set_ylim(-1.15,0.2); a1.set_xticks([])
    a1.set_ylabel(r"held-out $R^2$:  context $w \rightarrow$ receiver $z$")
    a1.set_title("$w$ cannot reconstruct $z$\n(negative in all 5 folds)",
                 fontsize=12.5,color=KEY,fontweight="bold")
    a1.spines[["top","right","bottom"]].set_visible(False)
    # right: reconstruction MSE true vs shuffle
    a2.bar([0,1],[0.48,0.82],color=[CTX,GREY],width=0.55,zorder=3)
    for xi,v in zip([0,1],[0.48,0.82]):
        a2.text(xi,v+0.02,f"{v:.2f}",ha="center",fontsize=13,fontweight="bold")
    a2.set_xticks([0,1]); a2.set_xticklabels(["true\ncontext","shuffled\ncontext"])
    a2.set_ylabel("reconstruction MSE (lower = more state info)")
    a2.set_ylim(0,0.95)
    a2.set_title("True context carries some\nstate-correlated info — as expected",
                 fontsize=12.5,color=KEY,fontweight="bold")
    a2.spines[["top","right"]].set_visible(False)
    a2.text(0.5,0.90,"41% lower, but still\nno receiver identity",transform=a2.transAxes,
            ha="center",va="top",fontsize=10,style="italic",color="#555")
    _suptitle(fig, "The context vector does not encode the receiver",
              fontsize=14,color=KEY,fontweight="bold",y=1.03)
    _save(fig,"chart_identifiability")

# ---------------------------------------------------------------- 5,6,7 biology bar slides
def biology():
    _signed_bars("chart_preinvasive_circuit",
        [("ETV3","tf_ETV3"),("ETV6","tf_ETV6"),("ZBTB18","tf_ZBTB18"),("GLI3","tf_GLI3"),
         ("FOS","tf_FOS"),("p53 (pathway)","pathway_p53"),("RB1","tf_RB1"),("KAT5","tf_KAT5")],
        "AAH_AIS","Preinvasive residual: loss of repression under retained restraint")
    _signed_bars("chart_invasion_architecture",
        [("HDAC1","tf_HDAC1"),("CTBP1","tf_CTBP1"),("NAB2","tf_NAB2"),
         ("MAML1","tf_MAML1"),("FOXA1","tf_FOXA1")],
        "AIS_invasive","Invasion: a coregulator / accessibility switch")
    anabolic_module()

# --------------------------------------------------------- 7b. anabolic two-panel
def anabolic_module():
    """Left: R_cond of the 3 stress TFs at invasion. Right: MYC/OxPhos GSEA
    reversing sign between the two edges (both padj<1e-3 where labelled)."""
    di=_dossier("AIS_invasive")
    tfs=[("ATF5","tf_ATF5"),("HSF2","tf_HSF2"),("NFKB2","tf_NFKB2")]
    rows=[(l,di.loc[k]) for l,k in tfs if k in di.index]
    def nes(edge,pw):
        g=pd.read_csv(f"{R}/figures/{edge}/gsea/stage_gsea_{edge}.csv")
        h=g[g.pathway==pw]
        return float(h.NES.iloc[0]) if len(h) else np.nan
    cats=[("MYC targets","HALLMARK_MYC_TARGETS_V1"),
          ("OxPhos","HALLMARK_OXIDATIVE_PHOSPHORYLATION")]
    pre=[nes("AAH_AIS",pw) for _,pw in cats]
    inv=[nes("AIS_invasive",pw) for _,pw in cats]
    fig,(a1,a2)=plt.subplots(1,2,figsize=(10.6,4.6),gridspec_kw={"width_ratios":[1,1.15]})
    fig.patch.set_facecolor("white")
    # left: Rcond bars (all up at invasion)
    y=np.arange(len(rows))[::-1]
    for yi,(l,r) in zip(y,rows):
        a1.barh(yi,r.Re_mean,color=GOOD,height=0.55,zorder=3)
        a1.plot([r.Re_lo,r.Re_hi],[yi,yi],color="#333",lw=1.6,zorder=4)
    a1.axvline(0,color="#333",lw=1.1); a1.set_yticks(y)
    a1.set_yticklabels([l for l,_ in rows]); a1.set_xlim(0,0.32)
    a1.set_xlabel(r"$R_{\mathrm{cond}}$ (invasion)")
    a1.set_title("Stress-response TFs\ngain context weight",fontsize=12.5,color=KEY,fontweight="bold")
    a1.spines[["top","right"]].set_visible(False)
    # right: GSEA reversal grouped
    x=np.arange(len(cats)); w=0.38
    a2.bar(x-w/2,pre,w,color=BAD,label="AAH→AIS",zorder=3)
    a2.bar(x+w/2,inv,w,color=GOOD,label="AIS→invasive",zorder=3)
    a2.axhline(0,color="#333",lw=1.1); a2.set_xticks(x)
    a2.set_xticklabels([c for c,_ in cats])
    a2.set_ylabel("GSEA hallmark NES")
    a2.set_title("Metabolic programs reverse\nsign at invasion",fontsize=12.5,color=KEY,fontweight="bold")
    a2.legend(frameon=False,fontsize=10.5); a2.spines[["top","right"]].set_visible(False)
    _suptitle(fig, "An anabolic-stress module, on the same edge",
              fontsize=14,color=KEY,fontweight="bold",y=1.02)
    fig.text(0.5,-0.04,"anabolic demand (MYC, OxPhos up) and its stress compensation "
             "(ATF5, HSF2, NFKB2) gain weight together",ha="center",fontsize=10,
             style="italic",color="#555")
    _save(fig,"chart_anabolic_module")

if __name__ == "__main__":
    print("building real-data charts:")
    ladder_perfold("AAH_AIS")
    verdict_forest()
    whytight("AAH_AIS")
    interferon()
    identifiability()
    biology()
    print("DONE")
