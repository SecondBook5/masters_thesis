# StageBridge
## Niche-Conditioned Regulatory Transport in Premalignant Epithelial Progression: A Reproducible Context-Residual Estimand and the Spatial Scale of Its Recovery

**M.S. in Bioinformatics thesis, Johns Hopkins University — Krieger School of Arts and Sciences, Advanced Academic Programs. August 2026.**
Author: Abraham J. Book. Advisor: Dr. Chris Bradburne, PhD (Associate Professor, Department of Genetic Medicine, Johns Hopkins University).

<!-- Graphical abstract: PNG rendered from crrt_ude_schematic.pdf for inline GitHub display -->
<p align='center'><img src='crrt_ude_schematic.png' alt='StageBridge model overview.' width='100%'></p>

> **Note:** the abstract below is a working draft and will be replaced with the final thesis abstract.

Premalignant epithelial lesions progress within tissue ecosystems whose inflammatory and stromal
composition changes across the precursor sequence, yet whether the local microenvironment alters an
epithelial cell's progression-aligned regulatory state beyond its own intrinsic state---and at what
spatial scale---has been difficult to isolate, because cross-sectional profiling captures snapshots
rather than trajectories and confounds cell state with tissue context. This thesis develops
StageBridge, a biologically structured universal differential equation that separates an intrinsic
regulatory-progression field from a niche-gated context field and defines a per-program, conditional
context residual, R_cond, as the additional regulatory displacement attributable to local ecology
within ecologically comparable cells. The transport coupling underlying the estimand was selected
against a frozen synthetic identifiability benchmark, which falsified an initial state-neutral coupling
and motivated the conditional-stratified formulation used throughout. Applied to a patient-held-out
lung adenocarcinoma precursor cohort spanning atypical adenomatous hyperplasia (AAH), adenocarcinoma
in situ (AIS), and invasive disease, StageBridge recovered a small, reproducible set of
context-associated regulatory programs---twenty-nine on the preinvasive AAH-to-AIS edge and
twenty-eight at the AIS-to-invasive boundary---forming a coordinated WNT, p53, TRAIL, and AP-1 axis
with coupled interferon and TGF-beta-effector suppression, sign-consistent across all folds and donors
and concordant with co-expression analysis. A pre-registered falsification ladder then showed that this
contextual information did not resolve at the single-cell-neighborhood scale: cell-resolved niche did
not outperform specimen-level ecology or a matched shuffle, and a variance decomposition attributed
the result to niche-composition variance that, though overwhelmingly cell-local, is stage-invariant at
the available resolution. A pancreatic precursor series returned a correctly calibrated null. StageBridge
therefore supports a reproducible, interpretable context-associated component of premalignant epithelial
progression while defining the unresolved spatial scale of that association, contributing a prespecified
estimand with a characterized recovery boundary rather than an unqualified positive claim.

### Overview of contents

| Chapter | Contents |
|---|---|
| 1. Introduction | Premalignancy as a tissue-level process; the lung and pancreatic precursor systems; single-cell and spatial profiling; optimal transport and neural differential equations; the unresolved context-residual estimand; objective and three pre-specified hypotheses. |
| 2. StageBridge: Materials and Methods | The structured context-residual UDE (intrinsic + niche-gated fields); the receiver and context representations; conditional-stratified optimal transport; the context residual R_cond; the frozen identifiability screen that selected the coupling; three-stage OT-CFM training; the falsification ladder. |
| 3. Results | Cohort and edge support; estimand selection; the reproducible per-program context residuals; the bounded local-vs-specimen falsification and its ecological explanation; the invasion edge; a stage-GSEA metabolic/interferon reversal; the correctly calibrated PanIN null; regulatory-network and cell--cell-communication corroboration; sensitivity analyses; hypothesis assessment. |
| 4. Discussion and Conclusions | Principal findings; the spatial-scale result as the central inferential contribution; methodological contribution; limitations; future directions; conclusion. |
| Appendices A--C | Entropic OT and Sinkhorn; derivation of the training objective and estimand; extended implementation and supplementary results. |

The model, pipeline, and analysis code are maintained in a companion repository (CRRT-UDE); this
repository contains the written thesis and its figures.

### Building

Built on the Johns Hopkins University dissertation template (see License). Compile with the JHU
template's standard toolchain (`latexmk` with the provided `latexmkrc`, or Overleaf import). The main
file is `00-main.tex`; chapters are `06-chapter-1.tex` (Introduction), `07-chapter-2.tex` (Methods),
`08-chapter-3.tex` (Results), and `09-chapter-4.tex` (Discussion and Conclusions). Template usage
notes are preserved in `TEMPLATE_README.md`.

### License

The thesis document is built on the [JHU Dissertation Template](https://github.com/bibekananda-datta/JHU-Dissertation-Template)
by Bibekananda Datta, used under the [MIT License](LICENSE) (see `LICENSE`, which retains the original
copyright notice as the license requires). The template meets the Johns Hopkins University Sheridan
Library formatting requirements. Thesis content, figures, and results are the author's own work.

### Contact

AJ Book --- `ajbook12@gmail.com`
