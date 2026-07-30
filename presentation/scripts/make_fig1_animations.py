"""Advanced ANIMATED method schematics (Act I) for the StageBridge defense.

These are CONCEPTUAL diagrams of the method -- no data values. Synthetic motion is used
to make the mechanism legible (this is deck material, not a paper figure; the data
results shown elsewhere -- forests, ladders, the real trajectory GIF -- stay real).

For each panel X in {a,b,c,d} this writes:
  figures/anim/panelX.gif        -- smooth looping animation (drop straight into PowerPoint/Keynote)
  figures/anim/panelX_flip_0..5  -- 6 motion-sample PNGs for the beamer overlay flip (any viewer)
  figures/anim/panelX_final.png  -- last frame (complete diagram; static fallback)

Motion design:
  a  spot deconvolves: epithelial dots stream up into receiver z, non-epithelial down into
     context w; anti-leakage strip snaps in -> disjoint by construction.
  b  cells settle into 3 ecological strata; OT lines grow source->target WITHIN each band,
     cascading band by band; context withheld from the cost.
  c  signal flows: intrinsic pulse z->field (wide); context pulse w->gate->14-d waist
     (constricts, glows)->expand to 773->field. The waist is the stated limitation.
  d  forward integration: z0 integrates twice, full (context on) and self-only pull apart
     as tau advances; the endpoint gap opens as R_cond.
"""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import matplotlib.patheffects as pe
import numpy as np
from PIL import Image
import os

KEY="#19376e"; EPI="#b0392b"; CTX="#1f7a4d"; INK="#222222"; GREY="#8a8a8a"
OUT="/home/booka/masters_thesis/presentation/figures/anim"
os.makedirs(OUT, exist_ok=True)

def ss(x):  # smoothstep 0..1
    x=float(np.clip(x,0,1)); return x*x*(3-2*x)
def fade(t,start,dur):  # eased 0..1 ramp over [start,start+dur]
    return ss((t-start)/dur) if dur>0 else (1.0 if t>=start else 0.0)

def _box(ax,x,y,w,h,text,color,fs=13,fc="white",a=1.0,lw=2.2):
    if a<=0: return
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle="round,pad=0.02,rounding_size=0.10",
                 lw=lw,edgecolor=color,facecolor=fc,zorder=3,alpha=a))
    ax.text(x,y,text,ha="center",va="center",fontsize=fs,fontweight="bold",color=color,zorder=4,alpha=a)
def _arrow(ax,a0,b0,color=INK,lw=2.4,style="-|>",rad=0.0,ls="-",alpha=1.0):
    if alpha<=0: return
    ax.add_patch(FancyArrowPatch(a0,b0,connectionstyle=f"arc3,rad={rad}",arrowstyle=style,
                 mutation_scale=16,lw=lw,color=color,linestyle=ls,zorder=2,alpha=alpha))
def _txt(ax,x,y,s,color,fs,a=1.0,**kw):
    if a<=0: return
    ax.text(x,y,s,color=color,fontsize=fs,alpha=a,zorder=5,**kw)

# ============================ PANEL A: deconvolution split ============================
_rng=np.random.default_rng(3)
_A_DOTS=[]
for _ in range(28):
    r,th=0.9*np.sqrt(_rng.random()),_rng.random()*2*np.pi
    home=(1.9+r*np.cos(th),4.0+r*np.sin(th))
    epi=_rng.random()<0.45
    col=EPI if epi else _rng.choice([CTX,GREY])
    dest=((6.9+_rng.random()*3.4, 5.45+_rng.random()*1.2) if epi
          else (6.9+_rng.random()*3.4, 1.35+_rng.random()*1.2))
    _A_DOTS.append((home,dest,col))
def draw_a(ax,t):
    # spot
    ax.add_patch(Circle((1.9,4.0),1.05,facecolor="#eee6f0",edgecolor=KEY,lw=2.4,zorder=3))
    _txt(ax,1.9,5.55,"Visium spot",KEY,12,ha="center",fontweight="bold")
    _txt(ax,1.9,2.25,"multicellular",("#666"),9.5,ha="center",style="italic")
    _box(ax,4.55,4.0,1.5,0.95,"DestVI\ndeconv.",KEY,fs=11,a=fade(t,0.05,0.15))
    _arrow(ax,(3.0,4.0),(3.78,4.0),color=KEY,alpha=fade(t,0.05,0.15))
    trav=ss((t-0.2)/0.5)
    for home,dest,col in _A_DOTS:
        x=home[0]+(dest[0]-home[0])*trav; y=home[1]+(dest[1]-home[1])*trav
        ax.scatter(x,y,s=28,color=col,zorder=4,alpha=0.85-0.55*trav)
    az=fade(t,0.45,0.4)
    _box(ax,8.7,6.05,4.0,1.5,"receiver state  $z$\n773 named programs\n(14 pathways + 759 TFs)",EPI,fs=11.5,a=az)
    _box(ax,8.7,1.95,4.0,1.5,"ecological context  $w$\n35 channels\n(non-epithelial + neighborhood)",CTX,fs=11.5,a=az)
    astrip=fade(t,0.78,0.22)
    if astrip>0:
        ax.plot([6.7,10.7],[4.0,4.0],color="#444",lw=1.6,ls=(0,(5,3)),zorder=2,alpha=astrip)
        _txt(ax,8.7,4.30,"anti-leakage strip",("#444"),10.5,a=astrip,ha="center",fontweight="bold",style="italic",
             path_effects=[pe.withStroke(linewidth=3,foreground="white")])
        _txt(ax,8.7,3.66,"epithelial / whole-spot / stage / donor removed from $w$",("#666"),8.5,a=astrip,ha="center")
        _txt(ax,8.7,0.55,"the two representations are disjoint by construction",KEY,10.5,a=astrip,ha="center",va="center",fontweight="bold")

# ============================ PANEL B: OT within strata ============================
_STRATA=[("stratum 0",5.6,"#f2d9b8"),("stratum 1",3.7,"#d9c2e0"),("stratum 2",1.8,"#c2dce0")]
_rb=np.random.default_rng(7); _B={}
for nm,yc,col in _STRATA:
    _B[nm]=(1.4+_rb.random(5)*2.0, yc-0.5+_rb.random(5)*1.0, 8.6+_rb.random(5)*2.0, yc-0.5+_rb.random(5)*1.0, _rb.integers(0,5,5))
def draw_b(ax,t):
    ab=fade(t,0.0,0.18)
    _txt(ax,2.4,7.4,"source stage",INK,12,a=ab,ha="center",fontweight="bold")
    _txt(ax,9.6,7.4,"target stage",INK,12,a=ab,ha="center",fontweight="bold")
    for bi,(nm,yc,col) in enumerate(_STRATA):
        ax.add_patch(FancyBboxPatch((1.0,yc-0.72),2.8,1.44,boxstyle="round,pad=0.02,rounding_size=0.08",
                     facecolor=col,edgecolor="none",alpha=0.55*ab,zorder=1))
        ax.add_patch(FancyBboxPatch((8.2,yc-0.72),2.8,1.44,boxstyle="round,pad=0.02,rounding_size=0.08",
                     facecolor=col,edgecolor="none",alpha=0.55*ab,zorder=1))
        _txt(ax,0.85,yc,nm,("#555"),9.5,a=ab,ha="right",va="center",rotation=90)
        sx,sy,tx,ty,j=_B[nm]
        ax.scatter(sx,sy,s=45,color=EPI,zorder=4,edgecolor="white",lw=0.6,alpha=ab)
        ax.scatter(tx,ty,s=45,color=KEY,zorder=4,edgecolor="white",lw=0.6,alpha=ab)
        start=0.22+0.16*bi
        for i in range(5):
            p=ss((t-start)/0.28)
            if p<=0: continue
            ex=sx[i]+(tx[j[i]]-sx[i])*p; ey=sy[i]+(ty[j[i]]-sy[i])*p
            _arrow(ax,(sx[i],sy[i]),(ex,ey),color=GREY,lw=1.2,style="-",rad=0.05,alpha=0.9)
    _txt(ax,6.0,6.5,"context withheld from the cost",CTX,10,a=fade(t,0.15,0.2),ha="center",fontweight="bold",style="italic")
    _txt(ax,6.0,0.55,"OT solved inside each stratum, regulatory-distance cost only",KEY,10.5,a=fade(t,0.75,0.25),
         ha="center",fontweight="bold",path_effects=[pe.withStroke(linewidth=3,foreground="white")])

# ============================ PANEL C: signal through gated waist ============================
def _along(pts,p):  # position at fraction p along polyline pts
    pts=np.array(pts,float); seg=np.linalg.norm(np.diff(pts,axis=0),axis=1); L=seg.sum()
    d=p*L; acc=0
    for k in range(len(seg)):
        if acc+seg[k]>=d:
            f=(d-acc)/seg[k] if seg[k]>0 else 0
            return pts[k]+(pts[k+1]-pts[k])*f
        acc+=seg[k]
    return pts[-1]
def draw_c(ax,t):
    a0=fade(t,0.0,0.22)
    _box(ax,1.5,6.2,2.2,1.0,"state $z$, $\\tau$",EPI,fs=12,a=a0)
    _box(ax,1.5,2.0,2.2,1.0,"context $w$",CTX,fs=12,a=a0)
    _box(ax,5.7,6.2,3.8,1.5,"intrinsic branch\nlow-rank $A$ + pathway map\n+ neural residual",EPI,fs=10.5,a=a0)
    _arrow(ax,(2.6,6.2),(3.72,6.2),color=EPI,alpha=a0)
    _box(ax,4.7,2.0,1.9,1.0,"bounded\ngate",CTX,fs=10.5,a=a0); _arrow(ax,(2.6,2.0),(3.75,2.0),color=CTX,alpha=a0)
    _arrow(ax,(5.65,2.0),(6.55,2.0),color=CTX,alpha=a0)
    _box(ax,9.9,2.0,3.0,1.1,"$\\times$ pathway activity\n$\\rightarrow$ expand to 773",CTX,fs=10.5,a=a0)
    _arrow(ax,(7.42,2.0),(8.4,2.0),color=CTX,alpha=a0)
    _box(ax,12.4,4.1,2.6,1.3,"$dz/d\\tau$\nfull field",KEY,fs=12,a=a0)
    _arrow(ax,(7.4,6.2),(11.3,4.55),color=EPI,rad=-0.12,alpha=a0)
    _arrow(ax,(11.4,2.0),(11.6,3.45),color=CTX,rad=0.15,alpha=a0)
    # waist -- pulses when context signal passes (~ context progress 0.5)
    cprog=ss((t-0.3)/0.6)
    wpulse=1.0+0.6*np.exp(-((cprog-0.5)/0.12)**2)
    ax.add_patch(Circle((7.0,2.0),0.42*wpulse,facecolor="white",edgecolor=CTX,lw=2.6,zorder=4,alpha=a0))
    _txt(ax,7.0,2.0,"14",CTX,12,a=a0,ha="center",va="center",fontweight="bold")
    _txt(ax,7.0,1.25,"14-d waist",CTX,9.5,a=a0,ha="center",fontweight="bold")
    # intrinsic pulse (fast, wide) along top path z-box -> field
    iprog=ss((t-0.3)/0.35)
    if 0<iprog<1:
        px,py=_along([(6.9,6.2),(11.3,4.55)],iprog)
        ax.scatter(px,py,s=180,color=EPI,zorder=6,alpha=0.85,edgecolor="white",lw=1.2)
    # context pulse through the bottleneck path
    if 0<cprog<1:
        px,py=_along([(2.6,2.0),(4.7,2.0),(7.0,2.0),(9.9,2.0),(11.55,3.4)],cprog)
        ax.scatter(px,py,s=160,color=CTX,zorder=6,alpha=0.9,edgecolor="white",lw=1.2)
    _txt(ax,7.0,0.35,"759 TF coordinates move only through the 14-channel gate or the residual",
         ("#a33"),9.5,a=fade(t,0.8,0.2),ha="center",style="italic",fontweight="bold")

# ============================ PANEL D: forward integration ============================
def draw_d(ax,t):
    _txt(ax,6.0,7.5,"one fit, one intrinsic field, context held fixed along both paths",KEY,10.5,
         a=fade(t,0.0,0.15),ha="center",fontweight="bold")
    # tau axis
    ax.annotate("",xy=(11.0,0.9),xytext=(1.2,0.9),arrowprops=dict(arrowstyle="-|>",color="#999",lw=1.6))
    _txt(ax,11.0,0.55,r"$\tau$",("#666"),12,ha="center")
    _txt(ax,1.3,0.55,"0",("#666"),10,ha="center"); _txt(ax,10.6,0.55,"1",("#666"),10,ha="center")
    ax.scatter([1.5],[4.0],s=160,color=INK,zorder=5)
    _txt(ax,1.5,3.35,"$z_0$\nobserved",INK,11,ha="center",va="top",fontweight="bold")
    taumax=ss(min(1,t/0.82))
    if taumax>0.001:
        tau=np.linspace(0,taumax,max(3,int(120*taumax)))
        xs=1.5+tau*8.4
        yf=4.0+1.9*tau+0.5*np.sin(tau*2.2); ys=4.0+0.85*tau-0.15*np.sin(tau*2.0)
        ax.plot(xs,yf,color=CTX,lw=3.2,zorder=4)
        ax.plot(xs,ys,color=EPI,lw=3.2,ls=(0,(5,2)),zorder=4)
        # moving integration heads
        ax.scatter([xs[-1]],[yf[-1]],s=120,color=CTX,zorder=6,edgecolor="white",lw=1.4)
        ax.scatter([xs[-1]],[ys[-1]],s=120,color=EPI,zorder=6,edgecolor="white",lw=1.4)
        # progress tick on tau axis
        ax.plot([xs[-1],xs[-1]],[0.78,1.02],color="#bbb",lw=1.2)
    aend=fade(t,0.8,0.2)
    if aend>0:
        xf=1.5+8.4; yf1=4.0+1.9+0.5*np.sin(2.2); ys1=4.0+0.85-0.15*np.sin(2.0)
        _txt(ax,xf+0.15,yf1,"full\n(context on)",CTX,10.5,a=aend,ha="left",va="center",fontweight="bold")
        _txt(ax,xf+0.15,ys1,"self-only\n(context off)",EPI,10.5,a=aend,ha="left",va="center",fontweight="bold")
        _arrow(ax,(xf,ys1),(xf,yf1),color=KEY,lw=2.4,style="<->",alpha=aend)
        _txt(ax,xf-0.25,(yf1+ys1)/2,r"$R_{\mathrm{cond}}$",KEY,15,a=aend,ha="right",va="center",fontweight="bold",
             path_effects=[pe.withStroke(linewidth=3,foreground="white")])
        _txt(ax,6.0,0.15,"within-receiver residual, not a level; computed out of fold",("#666"),9.5,a=aend,ha="center",style="italic")

def render(name,figsize,xlim,ylim,draw_fn,nframes=44,fps=18,flip_k=6,hold=6):
    frames=[]
    seq=list(range(nframes))+[nframes-1]*hold   # hold on final frame before loop
    for i in seq:
        t=i/(nframes-1)
        fig,ax=plt.subplots(figsize=figsize,dpi=115); ax.set_xlim(*xlim); ax.set_ylim(*ylim)
        ax.axis("off"); fig.patch.set_facecolor("white")
        draw_fn(ax,t); fig.canvas.draw()
        frames.append(Image.fromarray(np.asarray(fig.canvas.buffer_rgba())).convert("RGB"))
        plt.close(fig)
    dur=int(1000/fps)
    frames[0].save(f"{OUT}/{name}.gif",save_all=True,append_images=frames[1:],duration=dur,loop=0,optimize=True)
    for slot in range(flip_k):
        idx=round(slot*(nframes-1)/(flip_k-1)); frames[idx].save(f"{OUT}/{name}_flip_{slot}.png")
    frames[nframes-1].save(f"{OUT}/{name}_final.png")
    print(f"{name}.gif ({len(frames)} frames) + {flip_k} flip + final")

render("panela",(8.6,5.6),(0,12),(0,8),draw_a)
render("panelb",(8.6,5.6),(0,12),(0,8),draw_b)
render("panelc",(10.2,5.4),(0,14),(0,8),draw_c)
render("paneld",(9.4,5.4),(0,12),(0,8),draw_d)
print("DONE: 4 animated panels")
