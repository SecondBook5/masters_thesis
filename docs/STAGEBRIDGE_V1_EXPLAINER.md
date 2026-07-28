# StageBridge V1 — reference explainer

Reference for explaining StageBridge V1 (the prior formulation) when drafting the thesis
V1-motivation. Facts here are code-verified (see memory `stagebridge_v1_facts.md`); the plain-language
framing below is the author's. Use it to write Ch1 §1.7 and the Discussion's method-development context.

## StageBridge V1 in one sentence

StageBridge V1 combined an atlas-derived epithelial state with a receiver-centered Set Transformer
representation of the local niche and used optimal-transport conditional flow matching to learn a
gated, context-conditioned progression field.

## The question V1 asked

Can we predict premalignant epithelial progression better when we include information about the cell's
local tissue neighborhood? It treated progression as movement from an earlier disease-stage population
to a later one (Normal -> Preinvasive, or AAH -> AIS). Because sequencing destroys the tissue, the same
cell cannot be observed at both stages, so V1 inferred plausible transitions between different
populations of cells.

## The pieces

1. **Focal receiver.** Every prediction centered on one epithelial observation (the "receiver"), carrying
   both its own molecular state and information about its surrounding niche (immune, macrophage,
   fibroblast, other epithelial states, spatial distances). Biological premise: two receivers with
   similar internal states might move differently if surrounded by different tissue.
2. **Latent state space.** V1 represented epithelial state in a lower-dimensional learned latent built
   from reference atlases (healthy-lung HLCA + lung-cancer LuCA), organizing cells so normal and
   malignant states separate and precursors sit between. Movement through this space = change in state.
   Not directly interpretable as named pathways/TFs.
3. **Niche as a set.** Each neighborhood had a variable number of cells, treated as an order-independent
   set N_i = {n_i1, ..., n_ik} and processed by a Set Transformer (SAB/ISAB/PMA).
4. **Receiver-centered attention.** The model weighted neighbors by relevance to the focal receiver
   (alpha_ij depends on receiver state, neighbor state, distance, stage), then summarized the niche as
   h_i = sum_j alpha_ij n_ij (real architecture more complex; this is the intuition).
5. **Intrinsic + context-conditioned drift, gated.** Two velocities — v_latent (from the cell's own
   state) and v_context (from the niche) — blended by a learned per-cell gate:
   v_i = (1 - g_i) v_latent + g_i v_context,  0 <= g_i <= 1. Hence "niche-conditioned transition model."
6. **Optimal transport pairings.** With no tracked pairs, entropic Sinkhorn OT proposed plausible
   source->target correspondences by minimizing a state-difference cost c_ij = ||x_i - y_j||^2 — a
   probabilistic "plausible target," not a claim that cell i became cell j.
7. **Conditional flow matching.** Trained the field to predict the direction connecting OT-paired states:
   x_tau = (1-tau)x_0 + tau x_1, target u = x_1 - x_0, learn v_theta(x_tau, h, tau) ~ x_1 - x_0. Related
   to neural ODEs (dx/dtau = v_theta).
8. **Output.** One context-conditioned field per receiver, integrated to a predicted trajectory
   x_i(0) -> x_i(1); applicable across a population to generate a predicted later-stage distribution.

## What V1 tested

receiver + niche vs receiver alone, plus reduced architectures (no niche, no gate, simpler pooling,
simpler graph/set encoders). Existing V1 results suggested progression was highly learnable, the gating
architecture mattered, and niche information provided a smaller incremental improvement — evidence that
context contained useful predictive information. (Note for the thesis: V1 has NO reproducible held-out
transition number; the val-loss ablations are preliminary. Do not quote held-out accuracy or the
"96.4%" poster figure. See memory `stagebridge_v1_facts.md`.)

## The crucial limitation (why V2 was necessary)

V1 combined receiver and niche in ONE model and produced only one final prediction v_combined(x,h,tau).
It did not yield a clean pair — "what the cell does by itself" vs "what context adds." So a correct
prediction could not be attributed to state vs neighborhood vs patient vs specimen ecology vs stage. A
no-niche ablation could show context was useful but could not establish that a receiver's own immediate
neighborhood produced a specific biological change. It also worked in a broad latent space, so movement
was not directly interpretable as named pathway/TF changes.

## Transition to V2 (CRRT-UDE)

V2 changed the scientific objective, not just the implementation:
- V1: Does context improve prediction?
- V2: What does context add BEYOND epithelial state, and is that information actually receiver-local?

V2 explicitly separates v_self from v_context, integrates the same start twice (self-only vs
self+context), and takes the difference as the context residual R_cond; replaces the latent atlas
embedding with an interpretable regulatory (pathway + TF) space; and directly compares receiver-local
vs donor/stage-average vs shuffled vs self-only context.

## Analogy (boat)

V1: give the model the boat's direction, engine, wind, current, shoreline; it predicts where the boat
goes. If adding weather helps, environment was useful — but you can't say how much came from engine vs
wind vs current vs location. V2: predict the boat's path from the boat alone, then again with
environment; the difference estimates the environment-associated contribution — then test whether you
need the exact wind around that boat or only the bay's average weather.
