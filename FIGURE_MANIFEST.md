# CRRT-UDE Thesis + Defense Figure Manifest

Inventory of figures that physically exist, mapped to the blueprint's thesis
figure slots and a defense deck. **No figures were generated for this manifest** —
this is a truthful inventory of what is on disk as of 2026-07-27.

## Status legend
- **RENDERED** — a real data-derived file exists on disk and opens.
- **MISSING** — the slot has no file (data may exist elsewhere as a table or in the
  jobs tmp scratch, but nothing is placed as a thesis figure).
- **SCHEMATIC-NEEDED** — a concept/design diagram with no underlying data; must be
  drawn (TikZ/vector). Not a data figure, so cannot be "rendered" from a pipeline.
- **BROKEN** — file exists but is 0 bytes / unusable.
- **PLACEHOLDER** — JHU template default art (not a real figure).

## Source roots
- `THESIS/` = `/home/booka/JHU-Dissertation-Template/figures/`
- `TMP/` = `/home/booka/.claude/jobs/02e8a4e1/tmp/` (pipeline scratch; candidate assets
  not yet promoted into the thesis `figures/` tree)

## What the thesis actually references today
`drafts/results.tex` embeds 8 figures (lines 50, 57, 98, 124, 138, 149, 156, 165);
`08-chapter-3.tex` line 36 embeds `crrt_ude_schematic.pdf`. Everything else below is
either a candidate asset or a slot with no file.

---

## Thesis main-text figures (blueprint slots 1-13)

| # | Slot | Status | File path | One-line caption |
|---|------|--------|-----------|------------------|
| 1 | Receiver / context concept | **SCHEMATIC-NEEDED** | none (concept diagram; not yet drawn) | What a "receiver" cell and its spatial "context" are, and why a transition is modeled as niche-conditioned transport of the receiver's regulatory state. |
| 2 | LUAD + PanIN systems | **SCHEMATIC-NEEDED** | none (stage-ladder schematic; flagged as a GAP in prior catalog) | The two premalignant systems: the 5-stage LUAD ladder (Normal-AAH-AIS-MIA-LUAD) and the graded PanIN (low-to-high) transferability probe. |
| 3 | Study design | **SCHEMATIC-NEEDED** | none | Overall design: single-cell + spatial atlas -> receiver/context construction -> conditional OT estimand -> patient-held-out falsification. |
| 4 | Receiver / context construction | **SCHEMATIC-NEEDED** | none (partly subsumed by the architecture schematic, slot 5) | How the 773-dim regulatory receiver state (14 PROGENy + 759 CollecTRI) and the coarse niche context vector w (DestVI composition + Merchavit/BANKSY) are built. |
| 5 | StageBridge architecture + estimand | **RENDERED** | `THESIS/crrt_ude_schematic.pdf` (embedded, ch.3 l.36); vector twins `TMP/schematic_view-1.png`, `TMP/schematic_v2-1.png` | Context-gated regulatory transport as a UDE: v_self + v_context field decomposition, learned niche gate g(w), 3-stage OT-CFM training, R_cond / Helmholtz-Hodge readouts. |
| 6 | Conditional OT + falsification design | **SCHEMATIC-NEEDED** (design); data twin exists | schematic none; data ladder is `TMP/.../ude_result/ladder_bar.png` (AAH_AIS, AIS_invasive) | The three-candidate estimand screen against the frozen identifiability benchmark, plus the falsification-ladder logic (self-only vs local-context vs shuffles vs degenerate rungs). Numbers live as Table 2 in results. |
| 7 | Cohort / edge support | **MISSING** (as figure; Table 1 carries it) | none placed; candidate cohort embeddings `TMP/cc_test/cohort_umap_stage.png`, `cohort_umap_celltype.png`, `cohort_umap_donor.png` | Donor coverage and shared-donor support per progression edge; AIS->MIA invasion boundary has zero shared donors. Currently a table (`tab:edge_support`), no figure. |
| 8 | Held-out transport performance | **MISSING** (as dedicated figure) | none placed; candidates `TMP/.../ude_result/endpoint_metrics_by_fold.png`, `ladder_bar.png`, `transport_stability_normalized.png` | Five-fold patient-held-out endpoint fit and transport-stability geometry (D_N favors the pathway subspace). Not yet promoted into the thesis tree. |
| 9 | Stable regulatory programs | **RENDERED** | `THESIS/fig_stable_programs_forest.png` (results l.50); `THESIS/fig_rcond_regulon_network.png/.pdf` (results l.57) | The 29 stably niche-redirected programs on AAH->AIS (forest of held-out R_cond CIs) and the context-annotated CollecTRI regulon network (FOS up, IRF9 down). |
| 10 | Spatial localization | **RENDERED** | `THESIS/fig_niche_module_heatmap.png` (results l.124); candidate `TMP/biofigs/rcond_niche_gradient_{AAH_AIS,AIS_invasive}.png` | Niche-stratum x regulatory-module conditional transport heatmap; modules move only weakly across strata (coarse-ecology reading). |
| 11 | Local-vs-specimen ecology | **MISSING** (as main-text figure; Table 2 + defense fig exist) | none in main text; `THESIS/presentation/pres_ladder_AAH_AIS.png`, `pres_ladder_AIS_invasive.png`; `TMP/.../ladder_bar.png` | Falsification ladder: local context beats self-only on AAH->AIS but not its stratum-matched shuffle, and adds nothing at the invasion boundary. Currently Table 2. |
| 12 | PanIN transfer | **MISSING** (as main-text figure; defense fig rendered) | none in results.tex; `THESIS/presentation/pres_panin_null.png` (rendered) | PanIN low->high grade returns 0 STABLE programs (correct-null calibration) with coherent directional trends (NFkB up, EGFR up). Exists as a defense figure only. |
| 13 | Discussion synthesis | **SCHEMATIC-NEEDED** | none (synthesis diagram; not yet drawn) | Synthesis: sustained WNT across both edges, VEGF suppression specific to invasion, coarse-ecology gating, cross-disease null calibration. |

### Corroboration figures embedded in Results (independent-modality section, slot-9 support)

| Slot | Status | File path | One-line caption |
|------|--------|-----------|------------------|
| hdWGCNA module UMAP (AAH->AIS) | **RENDERED** | `THESIS/grn/module_umap_pub_AAH_AIS.png` (results l.138) | Co-expression module architecture (SM1-SM7) on the topological-overlap embedding, hub genes ringed; recovers lineage identities independent of the estimand. |
| hdWGCNA module UMAP (AIS->invasive) | **RENDERED** | `THESIS/grn/module_umap_pub_AIS_invasive.png` (not yet cited) | Invasion-edge co-expression module architecture (SM5 shifts to macrophage/monocyte). |
| GO-BP module enrichment (AAH->AIS) | **RENDERED** | `THESIS/grn/module_enrichment_AAH_AIS.png` (results l.149) | fgsea GO-BP enrichment of hdWGCNA modules; vascular SM4 enriched for cell-migration / TGFb / MAPK. |
| SCENIC RSS vs R_cond (AAH->AIS) | **RENDERED** | `THESIS/scenic/scenic_rss_vs_rcond_AAH_AIS.png` (results l.156) | Regulon stage-specificity vs model context effect; upper-right = AIS-specific + context-up (FOS, ETS2, NFkB), lower-right = IRF9. |
| SCENIC RSS vs R_cond (AIS->invasive) | **RENDERED** | `THESIS/scenic/scenic_rss_vs_rcond_AIS_invasive.png` (not yet cited) | Invasion-edge specificity-vs-context scatter. |
| SCENIC per-cell clustermap (AAH->AIS) | **RENDERED** | `THESIS/scenic/scenic_cell_clustermap_AAH_AIS.png` (results l.165) | Per-cell AUCell regulon-activity clustermap; NFkB/STAT/IRF-high inflammatory block, annotated by stage/donor/cell type. |
| SCENIC per-cell clustermap (AIS->invasive) | **RENDERED** | `THESIS/scenic/scenic_cell_clustermap_AIS_invasive.png` (not yet cited) | Invasion-edge per-cell regulon-activity clustermap. |
| SCENIC regulon UMAP (AAH->AIS) | **RENDERED** | `THESIS/scenic/scenic_regulon_umap_AAH_AIS.png` (4.4 MB; not yet cited) | Regulon-activity UMAP, AAH->AIS. |
| SCENIC regulon UMAP (AIS->invasive) | **BROKEN** | `THESIS/scenic/scenic_regulon_umap_AIS_invasive.png` (0 bytes) | File is empty; regenerate or drop. Non-empty copy exists at `TMP/check_figures/AIS_invasive/scenic/scenic_regulon_umap.png`. |
| hdWGCNA hub-gene networks | **RENDERED** (PDF only) | `THESIS/grn/hub_gene_network_AAH_AIS.pdf`, `hub_gene_network_AIS_invasive.pdf` (not cited) | Per-edge hub-gene co-expression networks; supplementary. |
| Waddington progression landscape | **RENDERED** | `THESIS/fig_waddington_landscape.png/.pdf` (results l.98); also `.gif`, `.html` interactive | -log-density potential over AAH+AIS epithelial clouds with integrated regulatory trajectories overlaid. |

---

## Thesis appendix figures

The appendices (`drafts/appendices.tex`) are currently **table-only** (ablation ladder,
baselines, CRRT-UDE hyperparameters, D_rho / D_N diagnostics, software). No
`\includegraphics` calls exist in the appendix. The following rendered diagnostic
assets exist in `TMP/` and are the natural candidates if any appendix figure is added.

| Slot | Status | File path | One-line caption |
|------|--------|-----------|------------------|
| Ablation ladder | **MISSING** (table only) | none; table `tab:app-ablations` | StageBridge ablation deltas; no-gate is most load-bearing (+11.3%). Table, no figure. |
| Baseline comparison | **MISSING** (table only) | none; table `tab:app-baselines` | Set/graph baselines >1 order of magnitude worse. Table, no figure. |
| CRRT-UDE hyperparameters | **MISSING** (table only) | none; table `tab:app-crrt-hyperparams` | Model/coupling/training settings. Table, no figure. |
| Regulatory-drift credibility (D_rho) | **MISSING** (prose only) | candidate `TMP/.../ude_dynamics/flux_index_self_vs_full.png`, `helmholtz_decomposition_{self,full}.png` | Per-fold D_rho structured-vs-residual regime; reported inline, no figure placed. |
| Transport-stability geometry (D_N) | **MISSING** (prose only) | candidate `TMP/.../ude_result/transport_stability_{raw,normalized}.png` | D_N per candidate regulatory geometry; reported inline, no figure placed. |
| DestVI mapping / training QC | **RENDERED** (in TMP) | `TMP/destvi_real/destvi_mapping.png`, `destvi_training_curves.png` | DestVI composition-deconvolution QC; supplementary candidate. |
| CNV burden / CNV-vs-R_cond | **RENDERED** (in TMP) | `TMP/cnv_real/cnv_burden_by_stage.png`, `TMP/bio/figs/cnv_vs_rcond.png` | inferCNV burden by stage and vs R_cond; supplementary candidate. |
| Velocity streams / potential landscape | **RENDERED** (in TMP) | `TMP/.../ude_dynamics/velocity_streamplot.png`, `velocity_stream_grid.png`, `potential_landscape.png` | Learned regulatory velocity fields and potential landscape; supplementary candidates. |
| Cell-cell communication (PanIN) | **RENDERED** (in TMP) | `TMP/panin_comm/figures/circos_{low_grade,high_grade,differential}.png`, `sankey_gated_chains.png`, `full_chain_*.png` | R_cond-gated LIANA communication circos + gated-chain sankey; supports the communication section. NOTE: full-cohort LUAD comm run COMPLETED (comm/{edge}/summary.json); sec:comm numbers verified and in main text; gated_chain_AAH_AIS.pdf placed. |
| Trajectory montage / self-vs-full | **RENDERED** (in TMP) | `TMP/anim/trajectory_montage.png`, `self_vs_full_trajectory.png` | Integrated trajectory montage; self-only vs full-context transport comparison. |
| Leakage ROC | **RENDERED** (in TMP) | `TMP/roc_test/leakage_roc.png` | Context-leakage control ROC; credibility supplement. |
| Cohort embeddings (UMAP/PHATE/PAGA) | **RENDERED** (in TMP) | `TMP/cc_test/cohort_umap_{stage,celltype,donor,leiden}.png`, `cohort_paga_umap_overlay.png`, DPT roots | Cohort structure embeddings; candidates for a cohort supplementary panel (feeds main slot 7). |

---

## Defense deck (~18 slides, CRRT-UDE narrative)

**IMPORTANT:** the pre-existing `DEFENSE_FIGURE_MAPPING.md` in the StageBridge repo
describes the OLD StageBridge v1 "invasion switch" narrative (volcano/DE, master
regulators, MMP paradox) and its figure paths point to `StageBridge/` and
`StageBridge_V1/` — it does **not** match the current CRRT-UDE thesis. The deck below
is mapped to the CRRT-UDE thesis using assets that actually exist. Slides marked
SCHEMATIC-NEEDED reuse the thesis concept slots.

| # | Slide | Status | File path | One-line caption |
|---|-------|--------|-----------|------------------|
| 1 | Title | **SCHEMATIC-NEEDED** | none | Niche-conditioned regulatory transport in premalignant progression. |
| 2 | The question | **SCHEMATIC-NEEDED** | none (reuse main slot 1) | Which epithelial states + niches mark progression-prone precursors, from one biopsy. |
| 3 | Two systems (LUAD + PanIN) | **SCHEMATIC-NEEDED** | none (reuse main slot 2) | 5-stage LUAD ladder + graded PanIN transferability probe. |
| 4 | Study design | **SCHEMATIC-NEEDED** | none (reuse main slot 3) | Atlas -> receiver/context -> conditional OT -> patient-held-out falsification. |
| 5 | Receiver + context | **SCHEMATIC-NEEDED** | none (reuse main slot 4) | 773-dim regulatory receiver state; coarse niche context vector w. |
| 6 | CRRT-UDE architecture | **RENDERED** | `THESIS/crrt_ude_schematic.pdf` / `TMP/schematic_view-1.png` | Context-gated UDE: v_self + v_context, learned gate, 3-stage OT-CFM, R_cond. |
| 7 | Estimand selection | **SCHEMATIC-NEEDED** | none (Table 1 in text; reuse main slot 6) | Conditional-stratified coupling is the only estimand clearing the frozen benchmark. |
| 8 | Cohort / edge support | **RENDERED** (candidate) | `TMP/cc_test/cohort_umap_stage.png` (+ table) | Shared-donor support per edge; invasion boundary has zero shared donors. |
| 9 | Stable programs (forest) | **RENDERED** | `THESIS/fig_stable_programs_forest.png` | 29 stably niche-redirected programs on AAH->AIS; p53/WNT/Trail/FOS up, IRF9/SMAD4 down. |
| 10 | Regulon network | **RENDERED** | `THESIS/fig_rcond_regulon_network.png` | Context-annotated CollecTRI regulon network; FOS up, IRF9 down. |
| 11 | Held-out reproducibility | **RENDERED** | `THESIS/presentation/pres_reproducibility.png` | Leave-one-donor-out reproducibility of R_cond on AAH->AIS (sign-consistency). |
| 12 | Falsification ladder (preinvasive) | **RENDERED** | `THESIS/presentation/pres_ladder_AAH_AIS.png` | Local context beats self-only (4/5 folds); degenerate rungs collapse; ties its shuffle. |
| 13 | Falsification ladder (invasion) | **RENDERED** | `THESIS/presentation/pres_ladder_AIS_invasive.png` | At invasion, local context adds no endpoint-predictive value over self-only. |
| 14 | Cross-edge R_cond | **RENDERED** | `THESIS/presentation/pres_cross_edge_rcond.png` | WNT sustained on both edges; VEGF suppression specific to the invasion boundary. |
| 15 | Spatial localization | **RENDERED** | `THESIS/fig_niche_module_heatmap.png` | Niche-stratum x module transport; coarse-ecology gating, not niche-identity-specific. |
| 16 | Progression landscape | **RENDERED** | `THESIS/fig_waddington_landscape.png` (or `.gif` live) | -log-density potential with integrated regulatory trajectories over AAH+AIS clouds. |
| 17 | Independent corroboration | **RENDERED** | `THESIS/grn/module_umap_pub_AAH_AIS.png` + `THESIS/scenic/scenic_rss_vs_rcond_AAH_AIS.png` | hdWGCNA + pySCENIC independently recover FOS/RB1/JAK-STAT signature. |
| 18 | PanIN transfer / null calibration | **RENDERED** | `THESIS/presentation/pres_panin_null.png` | 0 STABLE programs (correct null) with coherent directional trends (NFkB/EGFR up). |
| 19 | Communication (optional) | **RENDERED** (candidate) | `TMP/panin_comm/figures/sankey_gated_chains.png` / `circos_differential.png` | R_cond-gated ligand-receptor-TF chains (Macro/Fibro -> LRP1/EGFR -> FOS/RB1). |
| 20 | Synthesis / conclusions | **SCHEMATIC-NEEDED** | none (reuse main slot 13) | Coarse-ecology niche gating; sustained WNT; invasion-specific VEGF loss; honest nulls. |

---

## Counts

**Thesis main-text (13 blueprint slots):**
- RENDERED: 3 slots (5 architecture, 9 stable programs, 10 spatial localization)
- MISSING (data exists as table/defense-fig/TMP, not placed as main figure): 4 slots (7, 8, 11, 12)
- SCHEMATIC-NEEDED (concept/design, no data): 6 slots (1, 2, 3, 4, 6-schematic, 13)

**Results-embedded corroboration figures (11 files):** 9 RENDERED, 1 BROKEN
(`scenic_regulon_umap_AIS_invasive.png`, 0 bytes), 1 (`fig_waddington`) RENDERED.

**Thesis figures/ tree overall:** 20 non-empty image files RENDERED + 1 BROKEN
+ 1 PLACEHOLDER (`chap4.pdf`, JHU default duck-grid art, not a real figure).

**Appendix:** 0 figures placed (all tables); ~12 rendered diagnostic assets available in TMP as candidates.

**Defense deck (20 slides):** RENDERED assets for 13 slides
(6,8,9,10,11,12,13,14,15,16,17,18,19), SCHEMATIC-NEEDED for 7 (1,2,3,4,5,7,20).

**Bottom line:** 20 RENDERED image files on disk in the thesis tree (8 already wired
into the manuscript); 1 BROKEN (0-byte SCENIC invasion UMAP); 1 PLACEHOLDER to
replace; and roughly 7 concept/design schematics that must still be drawn (they carry
no data, so they cannot be "rendered" from the pipeline).
