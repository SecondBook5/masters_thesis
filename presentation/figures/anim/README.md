# Defense animation assets

Drop these GIFs straight into PowerPoint / Keynote (Insert -> Video/Picture -> the .gif;
they autoplay and loop). Each also has `_flip_0..5.png` motion samples (used by the beamer
overlay flip in `defense.tex`) and a `_final.png` static end-frame.

## Method schematics (Act I) -- CONCEPTUAL, synthetic motion for clarity (no data)

| GIF | Slide | What it shows |
|-----|-------|---------------|
| `panela.gif` | "One measurement, two disjoint readings" | Spot deconvolves: epithelial dots stream up into receiver state `z` (773 programs), non-epithelial down into context `w` (35 ch); anti-leakage strip snaps in. |
| `panelb.gif` | "Correspondence within ecological strata" | Cells settle into 3 strata; OT lines grow source->target *within* each band, cascading; context withheld from the cost. |
| `panelc.gif` | "The field is structured, context enters through a waist" | Intrinsic pulse (red) flows z->field; context pulse (green) flows w->gate->**14-d waist**->expand to 773->field. The waist is the stated limitation. |
| `paneld.gif` | "One start state, two integrations" | `z0` integrates forward twice; full (context on) and self-only (context off) pull apart; endpoint gap opens as `R_cond`. |

## Result animation -- REAL model output (NOT synthetic)

| GIF | Slide | What it shows |
|-----|-------|---------------|
| `traj_real_AAH_AIS.gif` | "Watching the transport" | Integrated AAH receivers (red) flowing over tau=0..1 to land on the held-out real AIS distribution (grey) in regulatory PC space. Genuine fitted-model transport. |

## Integrity note
Panels a-d are conceptual method diagrams; their motion is synthetic and illustrative
(deck material, not paper figures). The trajectory GIF is real model output. No data
*result* is synthesized.

## Regenerate
```
python presentation/scripts/make_fig1_animations.py   # panels a-d (gif + flip + final)
python presentation/scripts/make_fig1_panels.py        # static step-builds for beamer
# traj_real_AAH_AIS.gif is copied from results_hpc/figures/AAH_AIS/ude_result/trajectory.gif
```
