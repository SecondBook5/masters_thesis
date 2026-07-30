"""Cross-edge R_cond pathway comparison for the defense deck.

Slide claim: "Only two programs are invariant across the boundary" -- WNT and TRAIL are
the ONLY pathways STABLE with the same sign on BOTH the preinvasive (AAH->AIS) and the
invasion (AIS->invasive) edge. Every other pathway is stable on at most one edge.

Data: authoritative DOSSIER_CSV Rcond_ALL_{edge}.csv (verified). Slope-graph: each pathway
is a line from its AAH->AIS R_cond to its AIS->invasive R_cond. WNT and TRAIL highlighted;
all others greyed. Presentation-scale, white background.
"""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd, numpy as np

D = "/home/booka/projects/crrt-ude/results_hpc/DOSSIER_CSV"
a = pd.read_csv(f"{D}/Rcond_ALL_AAH_AIS.csv")
b = pd.read_csv(f"{D}/Rcond_ALL_AIS_invasive.csv")
ap = a[a["program_name"].str.startswith("pathway_")].set_index("program_name")
bp = b[b["program_name"].str.startswith("pathway_")].set_index("program_name")
j = ap[["Re_mean", "stability"]].join(bp[["Re_mean", "stability"]], lsuffix="_a", rsuffix="_b")
j.index = j.index.str.replace("pathway_", "", regex=False)

# invariant = STABLE + same sign on both edges
inv = (j.stability_a == "STABLE") & (j.stability_b == "STABLE") & (j.Re_mean_a * j.Re_mean_b > 0)
HL = {"WNT": "#1f7a4d", "Trail": "#d1701a"}   # highlight colors

fig, ax = plt.subplots(figsize=(8.2, 6.0))
fig.patch.set_facecolor("white"); ax.set_facecolor("white")
x0, x1 = 0, 1
ax.axhline(0, color="#bbb", lw=1.0, ls="--", zorder=1)

# grey background lines (non-invariant)
for name, r in j.iterrows():
    if inv.get(name, False): continue
    ax.plot([x0, x1], [r.Re_mean_a, r.Re_mean_b], color="#cccccc", lw=1.4, zorder=2)
    ax.scatter([x0, x1], [r.Re_mean_a, r.Re_mean_b], s=18, color="#cccccc", zorder=2)

# highlighted invariant lines on top
for name in j.index[inv]:
    r = j.loc[name]
    c = HL.get(name, "#333")
    ax.plot([x0, x1], [r.Re_mean_a, r.Re_mean_b], color=c, lw=3.2, zorder=4, solid_capstyle="round")
    ax.scatter([x0, x1], [r.Re_mean_a, r.Re_mean_b], s=70, color=c, zorder=5, edgecolor="white", linewidth=1.2)
    dy = 9 if name == "WNT" else -9   # split the near-overlapping WNT/Trail labels
    lbl = "TRAIL" if name == "Trail" else name
    ax.annotate(lbl, (x1, r.Re_mean_b), xytext=(10, dy), textcoords="offset points",
                va="center", ha="left", fontsize=13, fontweight="bold", color=c)

ax.set_xlim(-0.15, 1.35)
ax.set_xticks([x0, x1])
ax.set_xticklabels(["AAH$\\rightarrow$AIS\n(preinvasive)", "AIS$\\rightarrow$invasive\n(invasion)"], fontsize=12)
ax.set_ylabel(r"$R_{\mathrm{cond}}$ (context-conditioned transport)", fontsize=12)
ax.set_title("Only WNT and TRAIL are stable across both edges", fontsize=13.5, fontweight="bold")
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
ax.grid(axis="y", alpha=0.18)
plt.tight_layout()
OUT = "/home/booka/masters_thesis/presentation/figures/pres_cross_edge_rcond"
fig.savefig(OUT + ".pdf", bbox_inches="tight", facecolor="white")
fig.savefig(OUT + ".png", dpi=200, bbox_inches="tight", facecolor="white")
print("WROTE", OUT + ".pdf")
print("invariant pathways:", list(j.index[inv]))
print("WNT: %.3f -> %.3f | TRAIL: %.3f -> %.3f" %
      (j.loc["WNT","Re_mean_a"], j.loc["WNT","Re_mean_b"], j.loc["Trail","Re_mean_a"], j.loc["Trail","Re_mean_b"]))
