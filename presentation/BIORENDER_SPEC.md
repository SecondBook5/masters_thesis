# BioRender figure spec — "The premalignant niche: a candidate mechanism"

Export as `presentation/figures/biorender_mechanism.pdf` (or `.png`, 300 dpi).
The deck auto-detects it (fail-soft placeholder until then). Slide sits right after
"Two explanations" in Act 0 — it is the ONE biology-story slide before the method.

## Purpose
Make the "tissue-held" hypothesis concrete in one picture: a premalignant epithelial
cell's regulatory program is redirected by signals from its remodelling
microenvironment — niche → receptor → epithelial program.

## Layout (left → right = progression; keep it a single clean horizontal scene)

1. **Tissue context (left/surround), the niche:**
   - An **IL1B-high macrophage** (label "IL1B⁺ macrophage") releasing ligand dots.
   - **Activated fibroblast / CAF** nearby (label "CAF").
   - A few **immune cells (T/NK)** clustered — show them as a *focal cluster*, not scattered, to signal "spatially organized, not diffuse."
   - Optional faint alveolar/lung-tissue backdrop.

2. **The epithelial receiver (center), the progressing cell:**
   - An **epithelial cell** at an AAH/AIS precursor stage (label "AAH/AIS epithelial receiver").
   - On its surface draw **receptors** catching the niche ligands — label the two the
     analysis actually recovered: **IL1R1** and **EGFR** (also LRP1 if room).
   - Inside the cell, a small **regulatory-program module** (a gene/TF node cluster) —
     label representative recovered programs: **NF-κB, WNT, p53, FOS↑ ; interferon/IRF9↓**.

3. **The redirection arrow (the hypothesis):**
   - A bold arrow from niche-ligand → receptor → the intracellular program module,
     labeled **"context redirects the regulatory program"**.
   - A second, thinner arrow along the bottom: the cell's **own intrinsic trajectory**
     (AAH → AIS), so the figure shows *intrinsic path* + *niche redirection on top of it*.

## Labels / text (minimal, legible from back of room)
- Title is on the slide already — do NOT repeat it in the art.
- Key callouts: "IL1B⁺ macrophage niche", "CAF", "spatially focal immune", "IL1R1 / EGFR",
  "epithelial regulatory program", "niche → receptor → program".
- Keep to ≤ 7 text labels total.

## Palette (match the deck)
- epithelial / receiver: warm red  `#b0392b`
- niche / context (macrophage, CAF, immune): green `#1f7a4d`
- emphasis arrows / key term: deep blue `#19376e`
- white background, no drop-shadows-heavy style; clean flat vector.

## Aspect
~4:3 landscape, fills ~0.78 text-height on the slide. Leave breathing room; do not crowd.

## Scientific accuracy (do not overstate)
- This is a **candidate mechanism / hypothesis**, not a proven circuit. The recovered
  programs (NF-κB, WNT, p53, FOS up; IRF9 down) and receptors (IL1R1, EGFR) are the
  real ones from the R_cond analysis — safe to label. Do NOT draw a definitive causal
  pathway (no "→ cancer"); the arrow is "redirects the regulatory program."
- IL1B–IL1R1 macrophage axis and EGFR are grounded in the biology (Peng/Kadara,
  Cardoso 2026 amphiregulin–fibroblast–EGFR). Fine to depict.
