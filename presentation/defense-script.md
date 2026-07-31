# Defense speaker script

*Niche-Conditioned Regulatory Transport in Premalignant Epithelial Progression* — Abraham J. Book. Mentor: Chris Bradburne, PhD.

Generated from `defense.tex` presenter notes (`make_script.py`). One section per slide, in order. **[CUE: ...]** lines are stage directions / anticipated-question prompts, not spoken verbatim. Target ~150 words per slide, ~68 s each across ~40 main slides = 45 min.

---

## Slide 1. Title

Thank you all for being here. My name is Abraham Book, and this is work done with
Chris Bradburne.

I want to open with the question rather than the method, because the method only
exists to answer it.

A healthy pancreas contains hundreds of precancerous lesions, and almost none of
them will ever become cancer. I want to know what holds them back — and
specifically, whether what holds them back is inside the epithelial cell, or in
the tissue around it.

The answer I am going to give you is a bounded one. The tissue does carry
information about progression. And I can tell you the spatial scale at which that
information stops being recoverable from the data we currently have.

[CUE: that second sentence frames the negative as a finding, in the first minute]

## Slide 2. The paradox that defines premalignancy

A grossly normal adult pancreas contains hundreds of precancerous lesions.
Almost all of them carry oncogenic KRAS mutations. Almost none of them will
become cancer.

In the airway the picture is even sharper. Carcinoma in situ lesions that are
microscopically indistinguishable from one another have been followed
longitudinally — and roughly half progress to invasive disease, while the other
half regress or simply persist.

So the driver mutations are present. The histology is identical. And the outcomes
diverge.

That is why histopathologic stage, which is indispensable for classification,
does not tell you which lesion within a stage is going to move. And it is why
molecular profiling of the epithelium alone has not closed the gap either.

[CUE: Braxton 2024, Teixeira 2019 — say them, do not slide them]

[CUE: if asked why not just sequence the epithelium: Anderson 2026 separates LUAD
precursors within one histologic class, and the worst-outcome group differs as
much by immune context as by epithelial state]

## Slide 3. Two explanations

There are two broad explanations for that divergence.

One is cell-intrinsic: progression is set by the epithelial cell's own regulatory
state, and the tissue is essentially a bystander.

The other is tissue-held: comparable epithelial cells progress differently
because their surroundings differ. On this account the tissue is a participant,
not a setting.

These make different predictions about one measurable quantity — the one on the
slide. Holding a cell's own regulatory state and its stage fixed, does its tissue
context change where it ends up?

Everything after this is the construction of that quantity and the attempt to
falsify it.

[CUE: fifteen seconds — do not elaborate, the method is the next act]

## Slide 4. The premalignant niche: a candidate mechanism

Before the method, the biological hypothesis in one picture. A premalignant epithelial
lesion — AAH or AIS — sits inside a remodelling microenvironment: an IL1B-high
macrophage niche, activated fibroblasts, and an immune compartment that is spatially
organised rather than diffuse. The candidate mechanism is that signals from that niche
— routed through receptors on the epithelial cell — redirect its regulatory program
as it progresses, over and above what the cell's own state would do.

That is the “tissue-held” arrow made concrete. The rest of the talk asks whether that
arrow carries measurable, reproducible information, and at what spatial scale.

[CUE: this is the one slide where you tell the biology story — everything after is
measurement. Keep it to the niche -> receptor -> epithelial-program arrow.]

## Slide 5. The measurement will not cooperate

There is an obstacle, and it determines the entire design.

Profiling destroys the tissue. So every human precursor cohort is a
cross-sectional snapshot: each stage is represented by different cells, different
lesions, different patients. No cell is ever observed twice.

That means the question “does this cell's neighbourhood change its trajectory”
is not directly observable at all. It has to be estimated, through a model of
correspondence between unpaired populations.

And once you are estimating rather than measuring, two failure modes open up.

First, a niche can be statistically enriched at a stage without altering the
trajectory of any cell in it. Enrichment and effect are different claims.

Second — and this is the one that matters — a model given neighbourhood
features will fit better than one denied them whether or not the identity
of the neighbourhood carries any information. More features, better fit.

So the design has to be built around falsification rather than fit.

[CUE: this slide buys credit for the whole talk — when the negative arrives in
Act III they will already know falsification was designed in, not retrofitted]

[CUE: the second failure mode motivates the shuffle control; call back to it later]

## Slide 6. Three hypotheses, fixed before the data

Three hypotheses were specified before the cohorts were analysed.

The first is that a reproducible context residual exists at all — that named
regulatory programs carry a context effect whose sign holds up across held-out
patients.

The second is that the information is receiver-local. Concretely: a model given
each cell's own local neighbourhood should beat a model given a specimen average,
should beat a model given no context, and — critically — should beat a model
given context whose receiver correspondence has been destroyed but whose
distribution is preserved. That last comparison is the one that separates real
ecological information from added flexibility.

The third is that the estimand transfers: applied unchanged to a different
precursor epithelium, it should return interpretable programs where the cohort
supports them and an empty set where it does not.

Each has a null. Each null was run. They do not resolve in the same direction,
and I would argue that is the contribution rather than a disappointment.

[CUE: formalised Ch2 §2.7.4, assessed Ch3 §hypothesis-assessment]

[CUE: if asked whether this was really pre-registered — the identifiability
screen rejected my own first design. That is slide 10.]

## Act I — The estimand is identifiable, and it is not circular

*(section divider slide — no script; pause, then advance)*

## Slide 7. One measurement, two disjoint readings

Here is how the two representations are built, and the important word is
disjoint.

A spatial transcriptomic spot is a multicellular measurement. Deconvolution
splits it in two.

From the epithelial side, I take the decoded epithelial expression and score it
against curated pathway and transcription-factor priors. That gives the receiver
state — 773 named programs: fourteen signalling pathways and seven hundred
fifty-nine transcription factors. Not a latent space. Every coordinate has a
name, which is what makes the output interpretable later.

From the other side, I take non-epithelial composition together with spatial
neighbourhood features. That gives the ecological context, thirty-five channels.

And then an anti-leakage strip removes every epithelial, whole-spot, stage, and
donor channel from the context vector before anything is fitted. The two
representations do not share information by construction.

[CUE: be ready for “what exactly is a receiver?” — a Visium spot,
epithelially decoded. The single-nucleus data is the deconvolution reference and
the co-expression substrate, not a transport receiver. Know this cold.]

## Slide 8. Correspondence is estimated within ecological strata

Now I need to relate source-stage cells to target-stage cells, and they are
different cells from different patients.

Optimal transport gives a principled way to do that: treat the two populations as
distributions and find the assignment of probability mass that minimises total
cost.

But there is a trap. If I compute that coupling using context, then the coupling
itself encodes the ecological differences I am trying to attribute to context.
The effect gets absorbed into the correspondence used to estimate it, and the
result is meaningless.

So the coupling is stratified. Broad composition defines coarse ecological
strata, and transport is solved independently inside each one, using
regulatory-state distance only. In the figure, the transport lines never cross a
stratum boundary. Context is withheld from the cost entirely.

There is also a support gate: a stratum only enters if it holds at least ten
receivers and at least two donors on both sides. So no correspondence is ever
driven by an ecology seen in one stage or one patient.

[CUE: this design decision is the one most likely to be challenged — give the
reason out loud, do not wait for the question]

## Slide 9. The field is structured, and context enters through a waist

This is the model. It is a differential equation on regulatory state, and it has
two branches.

The intrinsic branch depends only on the cell's own state and its position along
the stage edge. It has a rank-restricted linear operator, an explicit
pathway-to-velocity mapping, and a neural residual.

The context branch takes the ecological vector, passes it through a bounded gate
to produce one modulation score per pathway, multiplies that against the
receiver's own pathway activities, and expands the result back into the full
regulatory space.

And now the limitation, which I want to state before anyone asks me.

Context enters that structured field through only fourteen channels. The seven
hundred fifty-nine transcription-factor coordinates are not gated directly —
they move only insofar as they are driven through those fourteen, or through the
neural residual. So when I show you transcription-factor level results later,
those are downstream reflections of a low-dimensional gate, not independent
per-factor evidence. The pathway-level results sit directly in the gated block
and are the ones the architecture supports most strongly.

[CUE: anyone who reads the field equation finds this. Saying it first is worth
more than being asked. Backup B2 has the full version.]

## Slide 10. One start state, two integrations

And this is the estimand.

Take a cell in its observed regulatory state. Integrate the fitted field forward
twice. Once with the context branch active. Once with it switched off. Same
starting point, same fitted intrinsic dynamics, context held fixed along both
paths.

The difference between the two endpoints is the conditional context residual.

Two things about that construction matter.

First, it is a within-receiver contrast, not a comparison between two
separately fitted models. Both trajectories come out of one fit and share one
intrinsic field. The gap is attributable to context rather than to two different
models disagreeing.

Second, it is a residual, not a level. It tells you how the surrounding
tissue redirects a cell relative to where its own state would have taken it. It
makes no claim about absolute abundance of anything. I will come back to that
distinction, because it resolves a result that otherwise looks wrong.

Everything I report is computed out of fold, on held-out patients only.

[CUE: say “out of fold, held-out patients” once here and you never defend it again]

[CUE: plant “residual, not a level” — you spend it twice: on VEGF, and on
anyone who says a finding contradicts known biology]

## Slide 11. The fitted field, both branches, over the real manifold

That was the schematic. This is the fitted field itself, drawn as streamlines over
the real receiver manifold. Left is the self-only branch — the cell's own dynamics.
Right is the full, niche-gated field. Blue are the AAH receivers at tau=0; grey is
the real AIS target.

Two things to see. The flow is directed — it carries AAH cells toward the AIS
region rather than relaxing to a point. And the two panels are nearly identical: the
niche-gated field redirects transport only modestly. That is not a failure — it is the
first visual statement of the result I will quantify later, that the context effect is
real but small, and that its recoverable scale is the question of this thesis.

[CUE: do not over-claim the difference between the panels — the whole point is that it is subtle]

## Slide 12. Watching the transport: integrated AAH lands on real AIS

This is the fitted transport running on the primary edge, in the regulatory
principal-component plane. Grey is the real AIS distribution — the target we never
show the model. Red is the integrated AAH receivers, moving from their observed state
at tau=0 toward tau=1.

Watch where they land. The red cloud settles into the body of the grey distribution.
That endpoint agreement — integrated source onto held-out real target — is what the
Sinkhorn endpoint metric scores, out of fold.

[CUE: if presenting from Adobe, slide 1 auto-plays the video; otherwise step 2–9 flips
through the real frames. Either way it is the SAME model output, not a cartoon.]

[CUE: one sentence only — “the model was never shown the grey.” Then move on.]

## Slide 13. My first design failed its own screen

Before any of this touched real data, I built a synthetic benchmark with known
ground truth and froze it — four acceptance thresholds, fixed in advance.

Three candidate coupling designs went through it.

The progression-geometry coupling failed both tiers. The strict-state coupling
— which was my first design, and the one I expected to use — passed the first
tier and failed the second. Both were discarded.

The conditional-stratified coupling passed both, and it is what every result I am
about to show you is built on.

I want to be direct about why this slide is here. A falsification framework is
only worth anything if it was capable of rejecting the thing you wanted to be
true. Mine was, and it did. That is the evidence that the controls in this thesis
are not post-hoc.

[CUE: do not skip this slide — it pre-empts “how do we know the controls
weren't chosen after the fact” entirely]

[CUE: say the words: my pre-registered screen killed my first design and I
changed it]

## Slide 14. The context vector does not encode the receiver

One more thing has to be true before any of this is interpretable.

If the context vector secretly contained a copy of the cell's own state, then any
context effect would be self-referential — I would be measuring the model
reading the cell back to itself. So I tested it rather than assuming it.

I fit a ridge regression from context to receiver state on training cells, and
evaluated it on held-out cells. The held-out R-squared is negative in every one
of the five folds, mean minus zero point five four. Context predicts receiver
state worse than simply predicting the mean.

I will be precise about one detail. True context does reduce reconstruction error
relative to a shuffled control — zero point four eight against zero point eight
two. That is a real reduction, and it is expected, because tissue ecology and
epithelial state are genuinely correlated in biology. But neither recovers
receiver identity. The claim that matters is the negative R-squared.

[CUE: do not call 0.48 vs 0.82 “marginal” — it is a 41% reduction, and
overstating a control is how you lose it]

## Act II — What the estimand finds

*(section divider slide — no script; pause, then advance)*

## Slide 15. 29 of 773 programs are reproducibly niche-redirected

So: does a reproducible context residual exist? Yes.

Twenty-nine of the 773 programs on the preinvasive edge, and twenty-eight at the
invasion boundary, carry a context residual whose sign holds in every one of five
patient-held-out folds, with a donor-bootstrap interval excluding zero.

The leading programs also hold their sign in all ten leave-one-donor-out runs, so
no single patient is carrying the set.

That is hypothesis one, met.

[CUE: expect: “29 out of 773 is 3.8% — isn't that just your false positive
rate?” It is a fair question and you should say so.]

[CUE: short answer: the criterion is not one test. It is a confidence interval
excluding zero AND sign-consistency across five disjoint patient folds. Under
independence that compounds well below one percent. But the folds are correlated,
so I do not claim an exact null rate — and the retrained-shuffle null, which is
the correct test, is specified and not yet run. Backup B1. Do not bluff this.]

## Slide 16. The preinvasive residual is a circuit, not a list

This is the slide where I think the method earns its keep, so I want to spend a
moment on it.

Read as a list, the stable set looks like a mixture. Read as a circuit, it
resolves.

Four of the programs that lose context weight are transcriptional
repressors. ETV3 and ETV6 are ETS-family repressors of immediate-early
genes. ZBTB18 represses mesenchymal programs. GLI3, in its processed form, is the
repressive output of Hedgehog signalling.

Four independent repressors move down. And FOS — the immediate-early factor
they collectively restrain — moves up.

So this is not “AP-1 activity increases.” It is de-repression: the brakes and
their output are observed moving in opposite directions within the same estimate.
That is a stronger statement, and it is only available because the readout is
signed, per-program, and named.

[CUE: advance]
And it is not a cherry-picked handful. Plotted over all three
hundred SCENIC regulons against their stage specificity, FOS is the single most
context-elevated program and IRF9, ETV6 and SMAD4 sit at the context-removed
extreme — the darkened points are the ones stable across all five folds, so the
circuit I just described is the tail of a genome-wide distribution, not a list I
selected.

At the same time, the p53, RB1 and KAT5 checkpoint axis is context-elevated.
KAT5 is worth naming: it is the acetyltransferase that acts on p53. A cofactor and
its pathway both coming out stable across five folds is an internal consistency
check the estimand was not designed to pass.

The synthesis is loss of transcriptional repression under retained checkpoint
restraint — which describes a contested lesion, not a half-transformed one.

[CUE: expect “p53 up with WNT up is contradictory” — these are transcriptional
response footprints, not mutation status. TP53 mutation is a later event. An
elevated p53 footprint in a precursor is what oncogene-induced stress with intact
machinery looks like.]

## Slide 17. Same configuration. Different organ. Different method.

That configuration has been seen before, and not by me.

In mouse models of pancreatic carcinogenesis that capture spontaneous p53 loss,
oncogenic and tumour-suppressive programs are found co-activated in a
discrete progenitor-like population right at the benign-to-malignant transition
— specifically the programs controlled by p53, CDKN2A, and SMAD4.

That is the same configuration I recover in human lung precursors, by a
completely different route. And the correspondence extends to the detail: SMAD4
is the suppressive arm that gives way in their system, and SMAD4 is the
suppressive arm that loses context weight in mine.

Two species. Two epithelia. Two unrelated inference strategies. Same result.

That kind of convergence is worth more than either observation alone, and it
suggests the contested state is a general property of the
precursor-to-invasion boundary rather than something specific to my cohort or my
estimator.

[CUE: your strongest single slide — do not rush it]

[CUE: Reyes also supplies causal direction: p53 suppression enables progenitor
expansion, EMT reprogramming, and immune-privileged niche formation. That sets up
the next slide.]

## Slide 18. The niche grades the contest

And the niche does not just add an effect — it grades it.

Within a single histologic class, I stratified receivers by how CAF- and
immune-dense their surroundings are, and looked at how the residuals order across
those strata.

Moving toward the inflamed, stroma-rich end: p53 restraint falls, from
plus zero point three six three to plus zero point two four zero. WNT rises. TRAIL
rises. All three significant against a within-donor permutation null at about five
times ten to the minus four.

So the same lesion class shows less restraint and more drive where the tissue is
more inflamed. That is the direction a permissive microenvironment would predict,
and it is the direction the pancreatic model I just showed you predicts causally.

It is graded rather than switch-like, and the magnitudes are modest. I would not
describe this as a niche licensing progression. I would describe it as the niche
tilting a balance.

[CUE: state the permutation null before anyone asks — the strata also define the
transport coupling, and that is a fair circularity concern. Permuting within
donor preserves each donor's residual distribution and stratum counts.]

## Slide 19. Interferon tone is lost before invasion

This is the result I find most striking, and it inverts the intuition.

At the preinvasive step, two independent readouts agree. The context residual
shows JAK-STAT down and IRF9 — a component of the complex that executes
canonical type-one interferon transcription — stably down. And the
whole-transcriptome enrichment analysis, which knows nothing about my model,
shows both hallmark interferon responses down.

Those two readouts have different confounds. A stage contrast is
vulnerable to compositional change between stages. A context residual conditions
on cell state and niche stratum. When they agree across that difference, that is
the strongest form of internal support I have.

Then at invasion they diverge — interferon comes back in the enrichment
analysis while the residual elevates a different STAT arm.

I want to be careful here rather than claim both halves. The invasive front has
documented compositional shifts, so a stage contrast is vulnerable exactly where
a conditioned residual is not. The divergence localises that confound to the
invasion edge. The preinvasive loss is the defensible half, and it is the half
that carries the implication.

[CUE: own the divergence out loud — volunteering it is what makes the
preinvasive claim credible]

## Slide 20. And in lesions with known outcomes, that loss predicts progression

And there is one cohort that can turn that into a statement about risk.

Bronchial premalignant lesions have been monitored longitudinally — profiled
molecularly, and then followed until you know which ones progressed. It is, as
far as I know, the only human premalignancy cohort where both halves exist.

In that cohort, the progressive and persistent lesions show decreased interferon
signalling and decreased antigen presentation, with immunofluorescence confirming
depletion of immune cells. The regressive lesions retain interferon tone.

Those are squamous airway precursors, not adenocarcinoma, so the comparison
crosses lesion types and I want to say that plainly rather than let it slide.

But the claim it licenses is specific: loss of interferon tone in a premalignant
lesion is associated with progression rather than regression. And my analysis
places that loss at the preinvasive step.

There is a supporting observation from my own primary cohort: the
proinflammatory macrophage niches most associated with precursor epithelium are
more frequent in precursors and become less frequent in established
cancer.

If that is right, the window in which immune-directed interception is most likely
to matter closes before the transition that current staging emphasises.

[CUE: deliver as an implication, not a claim]

[CUE: if pressed: Peng shows targeting inflammation in the precancerous phase
reduces progenitor burden; Than 2026 shows interception beats treatment on
survival in mouse PDAC]

## Slide 21. Invasion is a change of architecture, not more drive

The invasion edge is not a stronger version of the preinvasive edge. Its stable
set has a different architecture, and the architecture is the finding.

Three corepressors lose context weight: HDAC1, CTBP1, and NAB2. Two factors that
open chromatin gain it: MAML1, which is the Notch coactivator that recruits p300,
and FOXA1, which is a pioneer factor.

MAML1 also promotes p53 acetylation after DNA damage — same axis as KAT5,
preinvasively.

Five regulators, all operating at the level of transcriptional
coregulation rather than sequence-specific activation, all moving the same
way — toward de-repression and accessibility.

The preinvasive edge removed specific repressors from a specific target module.
This edge shifts the global balance between repressive and activating
coregulation. That is a different kind of change.

[CUE: advance]
You can see that architecture directly. An independent co-expression
analysis on this edge resolves into seven modules, each anchored on a lineage hub
— fibroblast collagen, endothelial, myeloid, T-cell, and a ciliary module.

[CUE: advance]
And when I score those modules for functional enrichment, the
whole-transcriptome result agrees with the coregulator story. Ciliary and axonemal
programs are up preinvasively and collapse at invasion — sensory
perception of chemical stimulus is the single strongest enrichment on either
edge, at minus two point six one. So differentiated lineage identity is retained
preinvasively and dismantled at invasion, and the estimand names the coregulators
associated with the dismantling.

One more thing on this edge: the rotational fraction of the fitted field rises
from zero point four eight to zero point seven seven. The transition becomes
substantially less gradient-like.

[CUE: external concordance if wanted: Zhao 2025 (TP53-mutant cells lose alveolar
identity, high-entropy programs), Haga 2023 (hypomethylation begins at later
AIS), Chan 2026 (ablating a high-plasticity state abrogates the transition)]

## Slide 22. An anabolic-stress module, on the same edge

There is a second module at invasion where both readouts agree.

The context residual elevates ATF5, which is an integrated-stress-response
effector; HSF2, from the heat-shock family; and NFKB2, the non-canonical NF-kappa-B
subunit.

And the enrichment analysis on the same edge shows MYC targets up and oxidative
phosphorylation up — both of which were down at the preinvasive step.

Put those together and they describe one state. High MYC output with restored
oxidative metabolism is a cell operating under elevated biosynthetic load. ATF5
and heat-shock activity are exactly the compensation arms that such a load
recruits. So anabolic demand and its stress-compensation machinery gain context
weight together, on the edge where metabolic programs reverse direction.

There is a cross-disease parallel that supports the timing rather than the
direction: proteomics of pancreatic precursors places mitochondrial remodelling
prominently in high-grade lesions before invasion. Different trajectory,
different tissue — but both put metabolic reorganisation among the earlier
events.

[CUE: keep this one brisk, it is a supporting module not a headline]

## Slide 23. Only two programs are invariant across the boundary

Now compare the two edges directly.

Of all the programs stable on either edge, exactly two hold both stability and
sign across both: WNT and TRAIL. Everything else is edge-specific — p53, EGFR,
FOS and the repressors preinvasively; VEGF, MAML1, FOXA1 and the corepressors at
invasion.

That reframes WNT. On its own, WNT in a cancer context is unsurprising. But this
is a specific claim: WNT context-redirection is the one regulatory effect that
does not change while the coregulator architecture, the metabolic
direction, the interferon tone, and the lineage identity all change around it.

That also makes it the more tractable interception target, because acting on an
invariant effect does not require knowing which side of the invasion boundary a
lesion is on — and the whole diagnostic problem is that stage does not resolve
that.

I should add one caution about TRAIL. It is a death-receptor response footprint,
and sustained sub-lethal death-receptor signalling in apoptosis-resistant cells
is documented to produce non-apoptotic output instead of cell death. My estimand
cannot distinguish those two modes, so I am not going to tell you which one this
is.

[CUE: the TRAIL caveat is unprompted honesty that costs you nothing and buys a lot]

## Slide 24. VEGF goes down at invasion — and that is consistent

I want to raise a result that looks wrong, before anyone raises it for me.

VEGF is the largest-magnitude stable pathway at the invasion boundary, and it is
redirected downward. Invasion is canonically accompanied by angiogenesis.
So on the face of it, the model has the sign backwards.

It does not, for two reasons.

First: this is a residual, not a level. It says the surrounding tissue redirects a
cell's VEGF response relative to where its own state would have taken it.
It makes no claim about whether absolute VEGF signalling is higher or lower at
invasion. A pathway can rise across a transition while its context-attributable
component is negative.

Second: the receiver here is epithelial, and the score measures VEGF
response in the cells being scored. Angiogenic VEGF signalling is
transduced predominantly by endothelium. Epithelial VEGF response and tissue-level
angiogenesis are simply different quantities.

And my own data supports that separation. In the same cohort, the vascular
co-expression module is enriched for migration and angiogenesis, and the stromal
matrix module gains significance specifically at invasion. The tissue-level
vascular program is active while the epithelial residual is negative. That is a
compartment-resolved statement, and it is the kind of thing only a
receiver-centred residual can make.

[CUE: independent support: Chen 2025 finds endothelial and stromal activity, not
epithelial state, distinguishes subtypes within identical AAH/AIS histology]

## Slide 25. Progression is a directed flow, not a relaxation

A geometric read of the same fitted field, because it says something the coefficients
do not.

[build 1 — the landscape] First, the cell-potential landscape. The fitted field defines
a scalar potential over the manifold; cells sit in it like a Waddington surface. But a
potential alone would mean progression is pure downhill relaxation — and it is not.

[build 2 — Helmholtz] Decompose the field into a gradient part (equilibrium, the
landscape) and a rotational part (non-equilibrium flux). On the preinvasive edge the
non-equilibrium fraction is 0.53; at invasion it rises to 0.76. The invasion transition
is the most strongly non-gradient — a directed, cycle-like flow, not relaxation to a
fixed point. And adding context changes this fraction by at most 0.01 — the
non-equilibrium character is a property of the intrinsic progression field.

[CUE: this is the systems-biology beat — “landscape AND flux,” the Wang framework.
Say the two numbers: 0.53 preinvasive, 0.76 invasion.]

[CUE: do NOT claim thermodynamics — it is the geometry of the FITTED field, descriptive]

## Slide 26. The gate recovers the return arm of a known circuit

One more biological result, and this one connects to a circuit that has been
functionally validated by someone else.

I took roughly one point three million candidate signalling chains — sender
population, ligand, receptor, downstream regulator, terminal program — and
gated them on the context residual. Two programs survive.

The ligands that come through are macrophage- and stromal-derived: APOE, PSAP,
A2M, routed through LRP1 and EGFR onto an AP-1 program. Three of those ligands
share a receptor. A filter returning noise would not reconstitute a
shared-receptor ligand family from a million candidates.

Now the connection. In mouse lung, KRAS-mutant alveolar cells secrete
amphiregulin, activate EGFR on adjacent fibroblasts, drive a fibrotic program,
and those fibroblasts in turn reprogram alveolar macrophages and reinforce
epithelial plasticity. Blocking that axis abrogates tumour initiation entirely.

That circuit runs from epithelium to stroma. What my gate found is
the return path — macrophage and stromal signals coming back onto epithelial
receptors and terminating on AP-1. EGFR appears on both arms. The gate had no
knowledge of that circuit.

So: the epithelium builds a niche, and the niche redirects the epithelium that
built it.

[CUE: frame honestly — the gate is a filter, selective by construction. The
question is whether what survives is coherent. It is.]

[CUE: these are nominations for organoid perturbation, not established channels]

## Slide 27. The estimand transfers without over-calling

Hypothesis three: does this transfer?

I applied the identical estimand, unchanged, to a graded pancreatic precursor
series — a biologically different epithelium, dominated by fibroblast
remodelling rather than inflammatory macrophage proximity.

The stability filter returns zero programs. Directionally, the biology is
coherent — NF-kappa-B up, EGFR up, which is the inflammatory-to-proliferative
shift the PanIN literature describes — but nothing survives the reproducibility
criterion.

I want to be careful about how I describe that, because there is a tempting
overstatement available and I am not going to make it.

It would be convenient to call this correct-null calibration — proof that the
estimator does not manufacture findings where there is no power. But with four
donors and no positive control at matched sample size, a true null and a simple
absence of power are not separable. I cannot distinguish them.

So what I claim is narrower: the estimand transfers, and it declines to
over-call. The experiment that would actually earn the calibration claim is to
inject a synthetic effect of known magnitude at four donors and show the filter
recovers it. That has not been run.

[CUE: this is a trap slide — do NOT say “correct-null calibration” out loud]

## Act III — At what spatial scale does this hold?

*(section divider slide — no script; pause, then advance)*

## Slide 28. The falsification ladder

Hypothesis two is the one that required the most machinery, so here is the design.

It is a ladder of models. Each rung removes exactly one thing and everything else
is held fixed, and each is scored by how well its predicted endpoints match the
observed target-stage population on held-out patients.

The reference is the full local-context model. Then: replace each cell's context
with its donor-and-stage average, which removes within-specimen variation.
Remove context entirely. Remove the ecological stratification from the coupling.
Remove each half of the structured decomposition.

And the one in bold, which is the important one — shuffle the context. Permute
which cell gets which neighbourhood, matched on stage and state magnitude, so the
distribution of context is exactly preserved and only its identity is
destroyed. That is the comparison that separates ecological information from
added model flexibility, and it is the failure mode I flagged at the start.

Every comparison is paired within fold. Same folds, same donors, same populations
— only the model changes. That is what makes the intervals on the next slide
mean something.

[CUE: the full ladder is twelve rungs; this is the load-bearing subset.
Appendix C.10 has all of them per fold.]

## Slide 29. A split verdict — and one half is a bound

And here is the answer, which comes in two halves that have to be kept separate.

Against shuffled context, the paired difference is plus zero point zero
eight, with a confidence interval from minus one point one to plus one point two
six. That interval excludes any receiver-local benefit above about one point three
Sinkhorn units — which is under fifteen percent of the self-only gap. That is
an equivalence result. Not a failure to find a difference: a bound on how
large any difference could be.

Against self-only, the paired difference is plus eight point seven six, but
the interval runs from minus two point eight three to plus twenty point three
five. Four of five folds favour local context, and the paired test gives P around
zero point one zero. So that comparison is directionally consistent and
underpowered. I am not claiming it.

Which means hypothesis two is not met, and the outcome is actually weaker than the
pre-registered alternative branch, which required the self-only inequality to
hold. It does not hold significantly. I am reporting the weaker outcome.

[CUE: REHEARSE THIS SLIDE VERBATIM. The trap under pressure is reverting to
“improves substantially” when your own interval includes zero. Never say it.]

## Slide 30. Why one interval is tight and the other is not

The obvious question is why I trust one of those intervals and not the other, so
let me answer it before it is asked.

Look at the fold-level numbers. The self-minus-local difference swings from plus
twenty-two down to minus one across folds — a standard deviation of nine point
three. The local-minus-shuffle difference has a standard deviation of about one.

That difference is structural, not arbitrary.

The shuffle preserves the marginal structure of the context. So the shuffled model
and the local model are the same model receiving the same distribution of inputs
in a different order — and their transport co-moves fold for fold. The paired
difference is therefore very tightly estimated.

Self-only is a structurally different field. It is missing a whole branch. Its
fold-level behaviour swings widely, and five folds simply cannot resolve an
eight-point-seven-six mean gap from zero against that variance.

So one interval is trustworthy and the other is honest, and the reason is the
design of the comparison rather than a choice about which result I prefer.

[CUE: publishing the per-fold table in Appendix C.10 is what makes the interval
checkable by anyone. Say that.]

## Slide 31. At the invasion boundary, both comparisons are null

The invasion edge behaves the same way, more starkly.

Both intervals straddle zero. Local context is statistically indistinguishable
from shuffled context, and indistinguishable from no context at all. It improves
over self-only in one fold out of five.

There is a structural reason. This edge has zero shared donors — no patient
contributes cells to both the source and the target stage. So the within-patient
contrast that a local ecological signal would need is simply not in the data.

I think the dissociation on this edge is worth naming explicitly, because it is
instructive. I have a coherent, reproducible stable signature here — WNT
sustained, VEGF suppressed — coexisting with no endpoint-predictive value for
local context whatsoever.

Those are answers to two different questions. One is about whether per-program
parameters reproduce. The other is about whether a distributional endpoint metric
improves. A small reproducible effect can do the first and fail the second. This
edge separates them about as sharply as they can be separated.

[CUE: do not present this as a second failure — present it as the same finding
with the confound removed]

## Slide 32. Why: the ecology varies below our resolution

So why does it fail? This is the mechanism, and I think it is the most important
result in the thesis.

I decomposed the variance in the local composition features themselves — the
raw ingredients of the context vector — across three levels: between stage,
between patient, and receiver-to-receiver within patient.

Between-stage variance is under one percent. Between-patient is eight to fifteen.
And eighty-five to ninety-six percent of the variance is receiver-local and
stage-invariant.

Which means a cell-resolved context feature, at this resolution, is
overwhelmingly carrying variation that has nothing to do with the stage contrast.
It is not that there is no ecological signal. It is that the signal is embedded in
a large amount of stage-orthogonal local variation, and a distributional endpoint
metric cannot pull it out.

That also reconciles this with the gradient result I showed earlier, which looked
like a contradiction. The gradient is a statement about parameter structure across
roughly ten thousand receivers — a small systematic ordering is detectable
there. The variance decomposition is a statement about how much
progression-aligned signal reaches an endpoint metric. A small, reproducible
effect is exactly what fails to move a distributional distance while remaining
detectable per program. Same regime, two directions.

[CUE: do not rush this slide — it is the mechanism for the negative and the
reason the negative is a finding]

## Slide 33. An unrelated modality measured that scale

And here is the part I find most persuasive, because it does not come from me.

Three-dimensional, cellular-resolution histology of more than a thousand human
pancreatic precancers has mapped inflammation around individual lesions directly.
What that work found is that immune hot spots and cold spots interchange over
tens of microns.

Our spatial transcriptomic spots are fifty-five microns across, on hundred-micron
centres.

So an imaging modality with no relationship to this analysis, using a completely
different measurement, found the ecological variation operating at or below the
resolution at which my context vector was constructed. My variance decomposition
infers the same fact statistically, from transcriptomic data.

I want to be clear about what that changes. It means this is not “I could not
resolve the effect.” The scale at which the relevant ecology varies has been
independently measured, and it sits below the assay. That converts a limitation
into a measurement.

[CUE: strongest defensive move in the deck — land it slowly]

[CUE: it is also the basis for a collaboration: her imaging measured the length
scale, my estimator measured its consequence for inference]

## Slide 34. Two readings, and the experiment that separates them

There are two readings of that, and I cannot separate them with the data I have.

Reading A is sub-resolution. The information is genuinely receiver-local, but it
varies below a hundred microns, so a higher-resolution assay would recover it.

Reading B is that the progression-relevant ecological variable is not a
neighbourhood property at all — it is field-level. There is support for this:
spatial mapping in donor pancreata finds the PanIN epithelium lying on a continuum
with cancer while the microenvironment is drastically distinct and evolves
asynchronously, and the absence of stromal reprogramming has been proposed as the
reason most PanINs never progress. If that is the gating variable, it is a
property of the specimen, and a receiver-local feature is measuring the wrong
object however well it is resolved.

One experiment separates them: run this identical ladder on single-cell
resolution spatial data. Reading A predicts recovery. Reading B predicts
continued equivalence.

And I want to say what is at stake in that, because it is not small. If B holds,
then microenvironment is the wrong unit of analysis for progression risk — and
a substantial amount of neighbourhood-scale niche analysis has been measuring
something other than what it intends to.

[CUE: that last claim is the systems-level result and the reason this work belongs
in a systems journal. It is testable and consequential. Land it confidently —
it is not a hedge.]

## Act IV — How the hypotheses resolve

*(section divider slide — no script; pause, then advance)*

## Slide 35. Scorecard

So, against the three hypotheses I stated at the beginning.

Hypothesis one is met. A reproducible, program-resolved context residual exists,
and it holds across disjoint patient sets.

Hypothesis two is not met. And I want to give you both halves rather than the
summary: against shuffled context it is a bounded equivalence, which is a
quantitative result; against self-only it is underpowered, which is not.

Hypothesis three is met behaviourally — the estimand transfers and declines to
over-call — but not as a demonstration of calibration, for the reasons I gave.

And one thing I want to state plainly. My pre-registration specified an
alternative branch: if local context failed against shuffle but still beat
self-only, that would be the specimen-ecology outcome. That branch required the
self-only inequality to hold. It does not hold significantly. So the outcome I
actually got is weaker than the alternative I had prepared for, and I am
reporting the weaker one.

[CUE: that last paragraph is the most credibility-generating thing you will say.
Do not cut it and do not rush it.]

[CUE: if someone says “so H2 failed” — agree, then add that failing against
shuffle with a bound excluding anything above 1.3 units is more informative than
a failed test]

## Slide 36. Limitations

Seven limitations, and these are all stated in the thesis rather than discovered
in the writing of this talk.

The data are cross-sectional, so the couplings are model-defined alignments, not
lineage maps, and the progression coordinate carries no clock time.

Two shared donors on the primary edge and zero at invasion. This is the binding
constraint on everything, and no amount of statistical care fixes it.

Receivers are decoded spots, and the ecology varies at or below that scale.

Context is read at the source stage and held fixed, so co-evolution of the niche
with the cell is outside the model.

Context enters through fourteen channels, so factor-level residuals are
downstream reflections of a low-dimensional gate. And the credibility diagnostic
for that decomposition failed its threshold in one of five folds — reported, not
hidden.

The co-expression and communication analyses read the same expression matrix, so
they are cross-method consistency, not independent validation.

And the retrained-shuffle null, which is the correct calibration test for the
stable program set, is specified and not yet run.

[CUE: brisk and without apology — seven real limitations stated crisply reads as
command; hedging each reads as uncertainty]

## Slide 37. What comes next

Five things, in the order I would do them.

First, the retrained-shuffle null. Weeks of compute, and it either confirms the
twenty-nine program set or it does not. It is the single largest outstanding item.

Second — and this is the one I care most about — the identical ladder at
single-cell spatial resolution. That decides between the two readings I showed
you, and both outcomes are results. Recovery would mean I have measured the
resolution threshold at which ecological information becomes visible. Continued
equivalence would mean receiver-local niche identity does not carry progression
information at any resolution.

Third, if it turns out to be field-scale, then estimate a specimen-level term
explicitly rather than a receiver-local one.

Fourth, replace the learned context gate with actual receptor occupancy under
known ligand-receptor structure. That makes the model a genuine universal
differential equation rather than a structured approximation, and it makes the
communication chains a fitted term with an estimated affinity rather than a
post-hoc filter.

Fifth, perturb the axis the gate nominated, in organoid co-culture.

[CUE: point two is the one to sound most invested in — it is the paper]

## Slide 38. Contribution

To summarise what I think this contributes.

A falsifiable estimand for niche effects on premalignant progression — computed
out of fold, on held-out patients, read out on named biological programs rather
than latent dimensions.

An identifiability screen that was capable of rejecting my own preferred design,
and did.

Reproducible, signed, named biology on two stage edges, which resolves into
interpretable circuitry rather than a ranked list: de-repression under retained
checkpoint restraint before invasion, a coregulator switch at invasion, and
interferon loss preceding the invasive transition.

And a quantitative bound on receiver-local ecological information, together with
the specific experiment that decides why the recovery stops where it does.

The method works. The biology is reproducible. And the boundary is measured
rather than guessed.

[CUE: closing line, out loud:]

[CUE: “The result I am most confident in is the one that limits my own claim —
and I can tell you exactly which experiment resolves it.”]

[CUE: then STOP. Do not add anything.]

## Slide 39. Acknowledgments

*(no script — visual/table slide, or backup)*

## Slide 40. Backup

Likely order: B1 null rate, B2 the 14-channel gate, B3 per-fold ladder,
B4 decomposition credibility, B5 the below-chance AUC, B6 baselines,
B7 metric mechanics, B8 PanIN power, B9 provenance, B10 evidential tiers,
B11 spatial autocorrelation, B12 the selection screen.

## Slide 41. B1 — Is 29/773 just the false-positive rate?

Do not bluff. “The right test isn't run, here is what I can bound, here is
what it costs” is a strong answer. Improvising a null rate is not.

## Slide 42. B2 — The context channel is 14-dimensional

If you get this question you are being examined by someone who read the
field equation carefully. Answering it precisely is worth more than any result on
the main slides.

## Slide 43. B3 — Per-fold ladder, preinvasive edge

*(no script — visual/table slide, or backup)*

## Slide 44. B4 — Decomposition credibility per fold

*(no script — visual/table slide, or backup)*

## Slide 45. B5 — Why is the held-out AUC below chance?

Lead with “that is the confound signature,” not “it is at chance.”

## Slide 46. B6 — Baselines and ablations

*(no script — visual/table slide, or backup)*

## Slide 47. B7 — Endpoint metric mechanics

*(no script — visual/table slide, or backup)*

## Slide 48. B8 — PanIN power

*(no script — visual/table slide, or backup)*

## Slide 49. B9 — Provenance

*(no script — visual/table slide, or backup)*

## Slide 50. B10 — Secondary analyses and their evidential status

Claiming independence for the third tier is the easiest way to lose
credibility you have already earned.

## Slide 51. B11 — The ecology is spatially structured

*(no script — visual/table slide, or backup)*

## Slide 52. B12 — The estimand selection screen

*(no script — visual/table slide, or backup)*

