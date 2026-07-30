# Defense Prep — Narrative, Script, and Anticipated Questions

---

## Part 1 — Is the narrative strong enough?

Short answer: yes, structurally this is a strong shape for a defense, and you should
trust it. Longer answer below, including the one place I'd actively watch.

**What's working.** The five-act arc — paradox, then rigor, then biology, then the
boundary, then honest assessment — does the single hardest thing a defense talk has
to do: it doesn't bury the negative result, it *builds toward it* and frames it as the
sophistication of the design rather than a shortfall. Principal Findings in the thesis
says the three results "are best stated together because their tension is the
contribution," and the deck's structure enacts that same idea rather than just
asserting it. That's rare, and committees notice it. Most defenses either hide a null
result in a subordinate clause or apologize for it; yours spends an entire act on it
and calls it the central inferential result. That's the right call and it's already
built.

**The pivot from Act II to Act III is the moment that matters most**, and it's already
handled with real care — "A split verdict, and one half is a bound" and "Why one
interval is tight and the other is not" are exactly the right two slides to have back
to back, because they pre-empt the single most obvious objection (why do you trust the
equivalence claim more than the self-only claim, when both come from the same five
folds?) before anyone can raise it. Nail those two slides and you've defused the
sharpest likely challenge before Q&A even starts.

**The one place I'd actively watch: Act II's density.** Thirteen slides of biology is
a lot of ground, and the risk isn't any single slide — each one is well constructed —
it's that in the run of it, findings can start to land as a list ("here's finding
four... here's finding five...") rather than a story, especially under time pressure
where the instinct is to speed up and just deliver facts. The antidote is *stated
connective tissue*, out loud, between findings, not just moving to the next slide when
one is done. Two concrete anchor points already in the script that do this well and
that I'd lean on hardest:

- Going into "Same configuration. Different organ. Different method." — say the
connection before you say the finding: *this is not just p53 and WNT both going up,
it's the exact same co-activation pattern already shown, with genetic manipulation,
in an unrelated organ.* The slide does this; just don't let it read as slide six of
thirteen.
- The KAT5 → MAML1 thread now sitting in your notes (from last night's edit) is a
genuine opportunity to make Act II feel like one argument instead of two separate
edges. Preinvasively: KAT5 gates the p53 checkpoint. At invasion: MAML1 gates the
same checkpoint. Say that explicitly when you reach MAML1 — "we saw this axis
already, on the other edge" — and two disconnected facts become one thread that
spans the whole act.

If you do only one thing with the time you have left, do that: rehearse Act II once
specifically listening for whether each finding *refers back* to the one before it.
Everything else in the deck is in good shape.

---

## Part 2 — The script

This is your actual presenter-note script, pulled directly from the deck and
lightly cleaned for reading, organized by act. It is not new content — it's what
you've already written and (presumably) rehearsed. I've added a short **[bridge]**
line between acts: not something to memorize, just the one-sentence connective
thought to have in mind so the transition doesn't feel like starting a new talk.

Three slides are marked **VERBATIM** below — these are the ones flagged earlier
in this process as high-risk to paraphrase badly under pressure. Everything else,
speak in your own words from the shape of it; these three, say close to as written.


## Act 0

### The paradox that defines premalignancy

A grossly normal adult pancreas contains hundreds of precancerous lesions.
Almost all of them carry oncogenic KRAS mutations. Almost none of them will
become cancer.

In the airway the picture is even sharper. Carcinoma in situ lesions that are
microscopically indistinguishable from one another have been followed
longitudinally --- and roughly half progress to invasive disease, while the other
half regress or simply persist.

So the driver mutations are present. The histology is identical. And the outcomes
diverge.

That is why histopathologic stage, which is indispensable for classification,
does not tell you which lesion within a stage is going to move. And it is why
molecular profiling of the epithelium alone has not closed the gap either.

### Two explanations

There are two broad explanations for that divergence.

One is cell-intrinsic: progression is set by the epithelial cell's own regulatory
state, and the tissue is essentially a bystander.

The other is tissue-held: comparable epithelial cells progress differently
because their surroundings differ. On this account the tissue is a participant,
not a setting.

These make different predictions about one measurable quantity --- the one on the
slide. Holding a cell's own regulatory state and its stage fixed, does its tissue
context change where it ends up?

Everything after this is the construction of that quantity and the attempt to
falsify it.

### The measurement will not cooperate

There is an obstacle, and it determines the entire design.

Profiling destroys the tissue. So every human precursor cohort is a
cross-sectional snapshot: each stage is represented by different cells, different
lesions, different patients. No cell is ever observed twice.

That means the question ``does this cell's neighbourhood change its trajectory''
is not directly observable at all. It has to be estimated, through a model of
correspondence between unpaired populations.

And once you are estimating rather than measuring, two failure modes open up.

First, a niche can be statistically enriched at a stage without altering the
trajectory of any cell in it. Enrichment and effect are different claims.

Second --- and this is the one that matters --- a model given neighbourhood
features will fit better than one denied them whether or not the identity
of the neighbourhood carries any information. More features, better fit.

So the design has to be built around falsification rather than fit.

### Three hypotheses, fixed before the data

Three hypotheses were specified before the cohorts were analysed.

The first is that a reproducible context residual exists at all --- that named
regulatory programs carry a context effect whose sign holds up across held-out
patients.

The second is that the information is receiver-local. Concretely: a model given
each cell's own local neighbourhood should beat a model given a specimen average,
should beat a model given no context, and --- critically --- should beat a model
given context whose receiver correspondence has been destroyed but whose
distribution is preserved. That last comparison is the one that separates real
ecological information from added flexibility.

The third is that the estimand transfers: applied unchanged to a different
precursor epithelium, it should return interpretable programs where the cohort
supports them and an empty set where it does not.

Each has a null. Each null was run. They do not resolve in the same direction,
and I would argue that is the contribution rather than a disappointment.


> **[bridge into Act I]** The paradox is stated; now build the thing that can actually test it.

## Act I

### One measurement, two disjoint readings

Here is how the two representations are built, and the important word is
disjoint.

A spatial transcriptomic spot is a multicellular measurement. Deconvolution
splits it in two.

From the epithelial side, I take the decoded epithelial expression and score it
against curated pathway and transcription-factor priors. That gives the receiver
state --- 773 named programs: fourteen signalling pathways and seven hundred
fifty-nine transcription factors. Not a latent space. Every coordinate has a
name, which is what makes the output interpretable later.

From the other side, I take non-epithelial composition together with spatial
neighbourhood features. That gives the ecological context, thirty-five channels.

And then an anti-leakage strip removes every epithelial, whole-spot, stage, and
donor channel from the context vector before anything is fitted. The two
representations do not share information by construction.

### Correspondence is estimated within

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

### The field is structured, and context enters through a waist

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
hundred fifty-nine transcription-factor coordinates are not gated directly ---
they move only insofar as they are driven through those fourteen, or through the
neural residual. So when I show you transcription-factor level results later,
those are downstream reflections of a low-dimensional gate, not independent
per-factor evidence. The pathway-level results sit directly in the gated block
and are the ones the architecture supports most strongly.

### One start state, two integrations

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

### My first design failed its own screen

Before any of this touched real data, I built a synthetic benchmark with known
ground truth and froze it --- four acceptance thresholds, fixed in advance.

Three candidate coupling designs went through it.

The progression-geometry coupling failed both tiers. The strict-state coupling
--- which was my first design, and the one I expected to use --- passed the first
tier and failed the second. Both were discarded.

The conditional-stratified coupling passed both, and it is what every result I am
about to show you is built on.

I want to be direct about why this slide is here. A falsification framework is
only worth anything if it was capable of rejecting the thing you wanted to be
true. Mine was, and it did. That is the evidence that the controls in this thesis
are not post-hoc.

### The context vector does not encode the receiver

One more thing has to be true before any of this is interpretable.

If the context vector secretly contained a copy of the cell's own state, then any
context effect would be self-referential --- I would be measuring the model
reading the cell back to itself. So I tested it rather than assuming it.

I fit a ridge regression from context to receiver state on training cells, and
evaluated it on held-out cells. The held-out R-squared is negative in every one
of the five folds, mean minus zero point five four. Context predicts receiver
state worse than simply predicting the mean.

I will be precise about one detail. True context does reduce reconstruction error
relative to a shuffled control --- zero point four eight against zero point eight
two. That is a real reduction, and it is expected, because tissue ecology and
epithelial state are genuinely correlated in biology. But neither recovers
receiver identity. The claim that matters is the negative R-squared.


> **[bridge into Act II]** The instrument is built and audited clean. Now: what does it find.

## Act II

### 29 of 773 programs are reproducibly niche-redirected

So: does a reproducible context residual exist? Yes.

Twenty-nine of the 773 programs on the preinvasive edge, and twenty-eight at the
invasion boundary, carry a context residual whose sign holds in every one of five
patient-held-out folds, with a donor-bootstrap interval excluding zero.

The leading programs also hold their sign in all ten leave-one-donor-out runs, so
no single patient is carrying the set.

That is hypothesis one, met.

### The preinvasive residual is a circuit, not a list

This is the slide where I think the method earns its keep, so I want to spend a
moment on it.

Read as a list, the stable set looks like a mixture. Read as a circuit, it
resolves.

Four of the programs that lose context weight are transcriptional
repressors. ETV3 and ETV6 are ETS-family repressors of immediate-early
genes. ZBTB18 represses mesenchymal programs. GLI3, in its processed form, is the
repressive output of Hedgehog signalling.

Four independent repressors move down. And FOS --- the immediate-early factor
they collectively restrain --- moves up.

So this is not ``AP-1 activity increases.'' It is de-repression: the brakes and
their output are observed moving in opposite directions within the same estimate.
That is a stronger statement, and it is only available because the readout is
signed, per-program, and named.

At the same time, the p53, RB1 and KAT5 checkpoint axis is context-elevated.
KAT5 is worth naming: it is the acetyltransferase that acts on p53. A cofactor and
its pathway both coming out stable across five folds is an internal consistency
check the estimand was not designed to pass.

The synthesis is loss of transcriptional repression under retained checkpoint
restraint --- which describes a contested lesion, not a half-transformed one.

### Same configuration. Different organ. Different method.

That configuration has been seen before, and not by me.

In mouse models of pancreatic carcinogenesis that capture spontaneous p53 loss,
oncogenic and tumour-suppressive programs are found co-activated in a
discrete progenitor-like population right at the benign-to-malignant transition
--- specifically the programs controlled by p53, CDKN2A, and SMAD4.

That is the same configuration I recover in human lung precursors, by a
completely different route. And the correspondence extends to the detail: SMAD4
is the suppressive arm that gives way in their system, and SMAD4 is the
suppressive arm that loses context weight in mine.

Two species. Two epithelia. Two unrelated inference strategies. Same result.

That kind of convergence is worth more than either observation alone, and it
suggests the contested state is a general property of the
precursor-to-invasion boundary rather than something specific to my cohort or my
estimator.

### The niche grades the contest

And the niche does not just add an effect --- it grades it.

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

### Interferon tone is lost before

This is the result I find most striking, and it inverts the intuition.

At the preinvasive step, two independent readouts agree. The context residual
shows JAK-STAT down and IRF9 --- a component of the complex that executes
canonical type-one interferon transcription --- stably down. And the
whole-transcriptome enrichment analysis, which knows nothing about my model,
shows both hallmark interferon responses down.

Those two readouts have different confounds. A stage contrast is
vulnerable to compositional change between stages. A context residual conditions
on cell state and niche stratum. When they agree across that difference, that is
the strongest form of internal support I have.

Then at invasion they diverge --- interferon comes back in the enrichment
analysis while the residual elevates a different STAT arm.

I want to be careful here rather than claim both halves. The invasive front has
documented compositional shifts, so a stage contrast is vulnerable exactly where
a conditioned residual is not. The divergence localises that confound to the
invasion edge. The preinvasive loss is the defensible half, and it is the half
that carries the implication.

### And in lesions with known outcomes, that loss predicts progression

And there is one cohort that can turn that into a statement about risk.

Bronchial premalignant lesions have been monitored longitudinally --- profiled
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

### Invasion is a change of architecture, not more drive

The invasion edge is not a stronger version of the preinvasive edge. Its stable
set has a different architecture, and the architecture is the finding.

Three corepressors lose context weight: HDAC1, CTBP1, and NAB2. Two factors that
open chromatin gain it: MAML1, which is the Notch coactivator that recruits p300,
and FOXA1, which is a pioneer factor.

MAML1 also promotes p53 acetylation after DNA damage --- same axis as KAT5,
preinvasively.

Five regulators, all operating at the level of transcriptional
coregulation rather than sequence-specific activation, all moving the same
way --- toward de-repression and accessibility.

The preinvasive edge removed specific repressors from a specific target module.
This edge shifts the global balance between repressive and activating
coregulation. That is a different kind of change.

And the whole-transcriptome result on the same edge agrees. Ciliary and axonemal
programs are up preinvasively and collapse at invasion --- sensory
perception of chemical stimulus is the single strongest enrichment on either
edge, at minus two point six one. So differentiated lineage identity is retained
preinvasively and dismantled at invasion, and the estimand names the coregulators
associated with the dismantling.

One more thing on this edge: the rotational fraction of the fitted field rises
from zero point four eight to zero point seven seven. The transition becomes
substantially less gradient-like.

### An anabolic-stress module, on the same edge

There is a second module at invasion where both readouts agree.

The context residual elevates ATF5, which is an integrated-stress-response
effector; HSF2, from the heat-shock family; and NFKB2, the non-canonical NF-kappa-B
subunit.

And the enrichment analysis on the same edge shows MYC targets up and oxidative
phosphorylation up --- both of which were down at the preinvasive step.

Put those together and they describe one state. High MYC output with restored
oxidative metabolism is a cell operating under elevated biosynthetic load. ATF5
and heat-shock activity are exactly the compensation arms that such a load
recruits. So anabolic demand and its stress-compensation machinery gain context
weight together, on the edge where metabolic programs reverse direction.

There is a cross-disease parallel that supports the timing rather than the
direction: proteomics of pancreatic precursors places mitochondrial remodelling
prominently in high-grade lesions before invasion. Different trajectory,
different tissue --- but both put metabolic reorganisation among the earlier
events.

### Only two programs are invariant across the boundary

Now compare the two edges directly.

Of all the programs stable on either edge, exactly two hold both stability and
sign across both: WNT and TRAIL. Everything else is edge-specific --- p53, EGFR,
FOS and the repressors preinvasively; VEGF, MAML1, FOXA1 and the corepressors at
invasion.

That reframes WNT. On its own, WNT in a cancer context is unsurprising. But this
is a specific claim: WNT context-redirection is the one regulatory effect that
does not change while the coregulator architecture, the metabolic
direction, the interferon tone, and the lineage identity all change around it.

That also makes it the more tractable interception target, because acting on an
invariant effect does not require knowing which side of the invasion boundary a
lesion is on --- and the whole diagnostic problem is that stage does not resolve
that.

I should add one caution about TRAIL. It is a death-receptor response footprint,
and sustained sub-lethal death-receptor signalling in apoptosis-resistant cells
is documented to produce non-apoptotic output instead of cell death. My estimand
cannot distinguish those two modes, so I am not going to tell you which one this
is.

### VEGF goes down

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

### The gate recovers the return arm of a known circuit

One more biological result, and this one connects to a circuit that has been
functionally validated by someone else.

I took roughly one point three million candidate signalling chains --- sender
population, ligand, receptor, downstream regulator, terminal program --- and
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
the return path --- macrophage and stromal signals coming back onto epithelial
receptors and terminating on AP-1. EGFR appears on both arms. The gate had no
knowledge of that circuit.

So: the epithelium builds a niche, and the niche redirects the epithelium that
built it.

### The estimand transfers without over-calling

Hypothesis three: does this transfer?

I applied the identical estimand, unchanged, to a graded pancreatic precursor
series --- a biologically different epithelium, dominated by fibroblast
remodelling rather than inflammatory macrophage proximity.

The stability filter returns zero programs. Directionally, the biology is
coherent --- NF-kappa-B up, EGFR up, which is the inflammatory-to-proliferative
shift the PanIN literature describes --- but nothing survives the reproducibility
criterion.

I want to be careful about how I describe that, because there is a tempting
overstatement available and I am not going to make it.

It would be convenient to call this correct-null calibration --- proof that the
estimator does not manufacture findings where there is no power. But with four
donors and no positive control at matched sample size, a true null and a simple
absence of power are not separable. I cannot distinguish them.

So what I claim is narrower: the estimand transfers, and it declines to
over-call. The experiment that would actually earn the calibration claim is to
inject a synthetic effect of known magnitude at four donors and show the filter
recovers it. That has not been run.


> **[bridge into Act III]** Two edges of real biology are on the table. Now the harder question: at what scale does any of it actually live.

## Act III

### The falsification ladder

Hypothesis two is the one that required the most machinery, so here is the design.

It is a ladder of models. Each rung removes exactly one thing and everything else
is held fixed, and each is scored by how well its predicted endpoints match the
observed target-stage population on held-out patients.

The reference is the full local-context model. Then: replace each cell's context
with its donor-and-stage average, which removes within-specimen variation.
Remove context entirely. Remove the ecological stratification from the coupling.
Remove each half of the structured decomposition.

And the one in bold, which is the important one --- shuffle the context. Permute
which cell gets which neighbourhood, matched on stage and state magnitude, so the
distribution of context is exactly preserved and only its identity is
destroyed. That is the comparison that separates ecological information from
added model flexibility, and it is the failure mode I flagged at the start.

Every comparison is paired within fold. Same folds, same donors, same populations
--- only the model changes. That is what makes the intervals on the next slide
mean something.

### A split verdict --- and one half is a bound  **[VERBATIM — say this one close to as written]**


And here is the answer, which comes in two halves that have to be kept separate.

Against shuffled context, the paired difference is plus zero point zero
eight, with a confidence interval from minus one point one to plus one point two
six. That interval excludes any receiver-local benefit above about one point three
Sinkhorn units --- which is under fifteen percent of the self-only gap. That is
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

### Why one interval is tight and the other is not

The obvious question is why I trust one of those intervals and not the other, so
let me answer it before it is asked.

Look at the fold-level numbers. The self-minus-local difference swings from plus
twenty-two down to minus one across folds --- a standard deviation of nine point
three. The local-minus-shuffle difference has a standard deviation of about one.

That difference is structural, not arbitrary.

The shuffle preserves the marginal structure of the context. So the shuffled model
and the local model are the same model receiving the same distribution of inputs
in a different order --- and their transport co-moves fold for fold. The paired
difference is therefore very tightly estimated.

Self-only is a structurally different field. It is missing a whole branch. Its
fold-level behaviour swings widely, and five folds simply cannot resolve an
eight-point-seven-six mean gap from zero against that variance.

So one interval is trustworthy and the other is honest, and the reason is the
design of the comparison rather than a choice about which result I prefer.

### At the invasion boundary, both comparisons are null

The invasion edge behaves the same way, more starkly.

Both intervals straddle zero. Local context is statistically indistinguishable
from shuffled context, and indistinguishable from no context at all. It improves
over self-only in one fold out of five.

There is a structural reason. This edge has zero shared donors --- no patient
contributes cells to both the source and the target stage. So the within-patient
contrast that a local ecological signal would need is simply not in the data.

I think the dissociation on this edge is worth naming explicitly, because it is
instructive. I have a coherent, reproducible stable signature here --- WNT
sustained, VEGF suppressed --- coexisting with no endpoint-predictive value for
local context whatsoever.

Those are answers to two different questions. One is about whether per-program
parameters reproduce. The other is about whether a distributional endpoint metric
improves. A small reproducible effect can do the first and fail the second. This
edge separates them about as sharply as they can be separated.

### Why: the ecology varies below our resolution

So why does it fail? This is the mechanism, and I think it is the most important
result in the thesis.

I decomposed the variance in the local composition features themselves --- the
raw ingredients of the context vector --- across three levels: between stage,
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
roughly ten thousand receivers --- a small systematic ordering is detectable
there. The variance decomposition is a statement about how much
progression-aligned signal reaches an endpoint metric. A small, reproducible
effect is exactly what fails to move a distributional distance while remaining
detectable per program. Same regime, two directions.

### An unrelated modality measured that scale

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

I want to be clear about what that changes. It means this is not ``I could not
resolve the effect.'' The scale at which the relevant ecology varies has been
independently measured, and it sits below the assay. That converts a limitation
into a measurement.

### Two readings, and the experiment that separates them

There are two readings of that, and I cannot separate them with the data I have.

Reading A is sub-resolution. The information is genuinely receiver-local, but it
varies below a hundred microns, so a higher-resolution assay would recover it.

Reading B is that the progression-relevant ecological variable is not a
neighbourhood property at all --- it is field-level. There is support for this:
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
then microenvironment is the wrong unit of analysis for progression risk --- and
a substantial amount of neighbourhood-scale niche analysis has been measuring
something other than what it intends to.


> **[bridge into Act IV]** The boundary is drawn and explained. Close by putting it against what was promised at the start.

## Act IV

### Scorecard  **[VERBATIM — say this one close to as written]**


So, against the three hypotheses I stated at the beginning.

Hypothesis one is met. A reproducible, program-resolved context residual exists,
and it holds across disjoint patient sets.

Hypothesis two is not met. And I want to give you both halves rather than the
summary: against shuffled context it is a bounded equivalence, which is a
quantitative result; against self-only it is underpowered, which is not.

Hypothesis three is met behaviourally --- the estimand transfers and declines to
over-call --- but not as a demonstration of calibration, for the reasons I gave.

And one thing I want to state plainly. My pre-registration specified an
alternative branch: if local context failed against shuffle but still beat
self-only, that would be the specimen-ecology outcome. That branch required the
self-only inequality to hold. It does not hold significantly. So the outcome I
actually got is weaker than the alternative I had prepared for, and I am
reporting the weaker one.

### Limitations

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
for that decomposition failed its threshold in one of five folds --- reported, not
hidden.

The co-expression and communication analyses read the same expression matrix, so
they are cross-method consistency, not independent validation.

And the retrained-shuffle null, which is the correct calibration test for the
stable program set, is specified and not yet run.

### What comes next

Five things, in the order I would do them.

First, the retrained-shuffle null. Weeks of compute, and it either confirms the
twenty-nine program set or it does not. It is the single largest outstanding item.

Second --- and this is the one I care most about --- the identical ladder at
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

### Contribution  **[VERBATIM — say this one close to as written]**


To summarise what I think this contributes.

A falsifiable estimand for niche effects on premalignant progression --- computed
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

---

## Part 3 — Anticipated defense questions

Organized by category, roughly in order of how likely each is to come up. For
each: the question, then a compressed answer built from what's actually in the
thesis — not new material, just the fastest path to the honest answer you already
have the evidence for. Where a question has a genuinely hard edge, I've said so
rather than smoothing it over.

### Identifiability and design choices

**Q: Why a conditional-stratified coupling instead of just conditioning the field
directly on neighborhood features?**
Because the coupling itself would then encode the ecological information whose
downstream contribution you're trying to estimate. If transport is optimized
directly on the same context features being evaluated, the correspondence can
absorb the effect upstream of the analysis — the context branch would get credit
for information the coupling already used to decide which cells correspond to
which. Coarse ecological stratification restricts correspondence to broadly
comparable settings while reserving the fine-grained context for the dynamical
model, specifically so this can't happen. This is Section 2.4 of Chapter 2 and
it's the single most load-bearing design decision in the thesis — know it cold.

**Q: Walk me through why your first design failed its own benchmark.**
The strict, state-neutral coupling passed Tier 1 (abstract latent-space recovery)
but failed Tier 2 (regulatory-space recovery) on the frozen synthetic benchmark —
recovery cosine, seed-direction agreement, null gain, and non-identifiable
correlation were fixed before either design was tested. That failure is what
motivated the conditional-stratified revision. The honest framing, if asked
whether this was really pre-registered: yes, in the sense that matters — the
acceptance bars were fixed before scoring, and the screen rejected your own
preferred first design. That's a stronger form of pre-registration than fixing
bars and then only testing the design you already believed in.

**Q: Only fourteen pathway dimensions for the context gate — isn't that an
arbitrary bottleneck that could be hiding real signal?**
It's a real limitation and you should say so plainly rather than defend it as
costless. The 759 transcription-factor coordinates aren't gated directly; they
move only through those fourteen channels or through the neural residual, which
is exactly why the thesis states pathway-level findings (WNT, p53, TRAIL, VEGF,
JAK-STAT) with more confidence than transcription-factor-level findings
throughout. The bottleneck doesn't determine *which* factors load or with what
sign — a rank-restricted map could produce any sign pattern — so the sign
structure of a finding is the informative part, and the grouping is the
descriptive part. This is explicitly in Limitations now, along with the
proposed remedy (a hierarchical Set Transformer that would learn the pooling
scale rather than assume it).

**Q: The neural-residual dominance ratio hit 1.008 in one of five folds. Doesn't
that mean the model is basically unstructured in that fold?**
In that one fold, yes — it crossed the prespecified 1.0 interpretability
threshold, which is why it's flagged and excluded from the "credible" count
rather than quietly averaged in. Four of five folds are credible, mean 0.965.
The honest reading is: the structured terms and the neural residual carry
comparable velocity magnitude across the fit, so per-program attribution is
bounded by that ceiling — not residual-free, but not residual-dominated either,
except in that one fold. Don't oversell this; it's a real, stated limit on how
far interpretation can be pushed.

### The falsification ladder and statistics

**Q: Local-over-self-only is P≈0.10 — wouldn't a stricter correction make this
disappear entirely?**
This comparison was never claimed as significant — say that plainly before
they finish the question. It's reported as directionally consistent (favored in
4 of 5 folds) but underpowered, with a wide CI (−2.83 to +20.35). The
well-powered claim in this thesis is a *different* comparison: local-over-shuffle,
which has a tight CI (−1.10 to +1.26) precisely because the shuffle preserves
marginal structure and co-moves with the local model fold-for-fold, while
self-only is a structurally different field whose fold-level differences swing
nine times as wide. That's not a stats trick — it's a structural fact about why
one comparison is precise and the other isn't, and it's worth having the two
standard deviations (≈1.0 vs ≈9.3) ready to cite directly.

**Q: The retrained-shuffle null is still outstanding. Why present the 29 stable
programs before that confirmatory experiment is done?**
Because the two questions are genuinely different. The 29 programs answer
"does a reproducible, sign-consistent context residual exist under
patient-held-out resampling" — and it does, that's established now. The
retrained-shuffle null would answer a stronger, separate question: does that
reproducible set exceed a shuffled-context baseline at the estimand level. Both
are named as distinct in Chapter 3's hypothesis assessment; the thesis is
explicit that the 29 programs are reproducible under resampling but not yet
shown to exceed a shuffled baseline, and that gap is stated as the primary
confirmatory experiment still to run, not glossed over.

**Q: Only two donors bridge AAH→AIS. Isn't your primary edge underpowered by
definition?**
Yes, and this is exactly why every real conclusion in the thesis is
patient-held-out and cross-fold, not a single fit. It's also the proximate
reason the receiver-local hypothesis couldn't be resolved — limited
within-patient contrast bounds how much local-vs-specimen separation the data
can support. This is named directly in Limitations. The donor-held-out AUC of
0.419 (below chance) for a self-only classifier crossing patients, against
0.833 within-donor on the earlier edge with eight shared donors, is the
concrete evidence that intrinsic state is genuinely stage-discriminative but
doesn't transfer across patients — which is the reason patient-held-out
evaluation is used everywhere, not a hedge.

**Q: How do you know the local-vs-shuffle equivalence isn't just low power
dressed up as a finding?**
Because it's stated as an equivalence bound, not a bare failure to reject —
that distinction matters and is worth making explicitly if asked. The tight CI
means any local-context endpoint benefit above about 1.3 Sinkhorn units is
excluded by the data, which is a real, falsifiable statement, not an absence of
evidence. Contrast this with local-over-self-only, which genuinely is
underpowered (wide CI) and is reported as suggestive, not established — the
thesis treats these two differently on purpose because their precision is
different, and that distinction is the whole point of Section 3's falsification
ladder discussion.

### Biology

**Q: Could the KAT5/p53 co-stability just be two commonly-expressed, high-variance
programs coming out stable by chance?**
This is a fair challenge and the honest answer leans on independent
convergence rather than dismissing the concern. Stability here requires sign
consistency and a CI excluding zero in all five folds independently — a program
must clear that bar five times on disjoint patient sets, which is a stricter
bar than a single-pass FDR correction on pooled estimates. But the stronger
answer is that KAT5 and p53 aren't just two programs that happen to co-occur —
KAT5 is specifically the acetyltransferase that acts on p53 and is required for
the DNA-damage response p53 executes. A cofactor and the pathway it modifies
both emerging as stable is an internal consistency check the estimand wasn't
designed to pass and isn't guaranteed to pass under noise.

**Q: The PAX8 finding — why not just treat it as noise and exclude it?**
Because a stable set containing only confirmatory hits would itself be more
suspicious, not less. PAX8 is reported honestly as an anomaly with an
unresolved interpretation — it's a Müllerian/thyroid/renal lineage factor with
no established role in lung lineage — and it is explicitly not used to support
any claim in the thesis. Reporting it is the more defensible choice
scientifically, even though it complicates the narrative.

**Q: VEGF going down at invasion contradicts textbook angiogenesis biology. How
do you know this isn't a modeling error?**
Two structural facts resolve this, and you should lead with them rather than
hedge. First, R_cond is a residual, not a level — a pathway can rise across a
transition in absolute terms while its context-attributable component is
negative; these are different quantities. Second, the receiver is epithelial,
while angiogenic VEGF signaling is transduced predominantly by endothelium — so
an epithelial VEGF-response redirection and tissue-level angiogenesis are not
the same measurement and need not move together. Independent profiling
(Chen 2025) finds that endothelial and stromal activity, not epithelial state,
distinguishes molecular subtypes within identical AAH/AIS histology — and your
own co-expression analysis agrees, with the vascular module enriched for
angiogenesis regulation on the same edge where the epithelial VEGF residual is
negative. This is a compartment-resolved statement a level-based analysis
couldn't make, which is the estimand doing its job, not failing.

**Q: You lean on one outcome-linked cohort (Beane) for the interferon-timing
claim, and it's a different tissue — squamous airway, not LUAD. How much weight
can that comparison bear?**
Say the limit plainly before defending the point. It's the only human cohort
where premalignant lesions were profiled *and* followed to a known fate, which
is why it's cited despite the tissue mismatch — but the thesis is explicit that
the comparison must be made carefully across lesion types. The stronger,
tissue-matched support is the agreement between two independent readouts on the
*same* edge in your own data: JAK-STAT/IRF9 downregulation under R_cond and
independent GSEA showing interferon-γ/α suppression, agreeing at the
preinvasive step where they have different confounds, and diverging at
invasion in exactly the way a compositional confound would produce. That
internal agreement is doing more evidentiary work than the cross-tissue Beane
comparison, and it's worth saying so if pushed.

### Generalizability and scope

**Q: PanIN returned zero stable programs. How do you know that's the estimator
correctly declining to over-call, and not your method simply not working outside
LUAD?**
Honestly — you don't know that with certainty yet, and the thesis says so.
With four donors and no positive control at matched sample size, a true null
and simple absence of power are not separable from this cohort alone. What you
can say: zero stable programs at four donors is the expected behavior of a
patient-resampling filter that cannot manufacture cross-patient stability from
a cohort that small, and the directionally consistent programs it does return
(NFκB up, EGFR up) recover a biologically coherent inflammatory-to-proliferative
shift rather than noise. That's evidence of sane behavior, not proof of
calibration — and the thesis is careful not to claim more than that. This is
also the one place in your talk with an explicit stage direction not to say
"correct-null calibration" out loud — the deck already protects you here.

**Q: Couldn't the receiver-local-vs-specimen-scale result just mean your
neighborhood featurization (BANKSY) is inadequate, not that the biology is
genuinely specimen-scale?**
This is the sharpest version of the scale question and deserves a direct,
two-part answer. First, an outside measurement with no relationship to this
analysis — cellular-resolution histology of over a thousand pancreatic
precancers — independently finds perilesional inflammation varying over tens of
microns, below Visium's ~55μm/100μm-pitch resolution. That's not a
featurization choice; it's a hardware/assay resolution limit. Second, the
variance decomposition shows 85–96% of composition-feature variance is
receiver-local and stage-invariant *in the raw context data itself*, before any
BANKSY step — so a better neighborhood encoder wouldn't add information the
platform never captured. The honest caveat, which is now explicitly in
Limitations: this doesn't rule out that a *learned*, hierarchical aggregation
could recover signal at a scale your current fixed featurization can't reach —
which is exactly why the Set Transformer extension is proposed as a second,
purely computational route to the same question, alongside the higher-resolution
assay.

### Big picture

**Q: What is the one experiment that would most change your confidence in
these findings?**
The retrained-shuffle null, without hesitation. Retraining the full pipeline on
stratum-permuted context and recounting stable programs is the direct test of
whether the 29 programs exceed a shuffled-context baseline at the estimand
level — it's the confirmatory experiment the thesis names explicitly as
outstanding, and it's the one result that could most directly strengthen (or
complicate) the central positive claim.

**Q: Suppose that null comes back negative — the 29 programs don't beat
shuffle at the estimand level. What would that mean for your thesis?**
It would sharpen the boundary rather than erase the finding. The programs would
still be reproducible under patient-held-out and leave-one-donor-out
resampling — that result doesn't depend on the shuffle null. What would change
is the interpretation of *why* they're reproducible: not necessarily because
context carries receiver-specific information, but possibly because the
marginal ecological distribution itself is progression-associated at the
specimen scale, which is actually consistent with, not contradictory to, the
specimen-scale finding already reported in Chapter 3. It would make the
thesis's own central claim — that the informative signal is specimen-scale —
even more load-bearing, not less.

**Q: What would you do differently if starting over?**
Three concrete things, all now in Future Directions rather than raised for the
first time here: represent the regulatory state non-Euclideanly (a
hyperspherical embedding is the natural first candidate, since it preserves
angular co-activation structure while bounding the transport space); replace
the deterministic field with a stochastic branching process, since the
motivating epidemiology — hundreds of precursors, rare progression — describes
a branching outcome that a single velocity field can only approximate the
average tendency of, not represent directly; and replace the fixed,
hand-specified context aggregation with a hierarchical Set Transformer that
learns the pooling scale rather than assumes it, which bears directly on the
central open question of the thesis.

**Q: The hyperspherical/branching-process/Set-Transformer ideas — why weren't
these built now instead of proposed as future work?**
Because each is a substantial independent modeling effort, and stacking any of
them onto an already-complex structured UDE without first establishing that the
current, simpler construction is identifiable and falsifiable would have made
the core contribution harder to trust, not easier. The identifiability
discipline — a frozen benchmark that rejected your own first design — is
itself a large part of the thesis's contribution; adding degrees of freedom
before that discipline was in place would have worked against it. These are
named as the next steps precisely because they follow from what the current,
simpler model was able to establish cleanly.

---

## One last thing

You already have all of this. Nothing above is new — it's what's already in the
thesis and the deck, organized so you can hold the whole shape of it in your head
tonight instead of the individual slides. Read Part 2 once for flow, not for
memorization; know Part 3's structural answers cold, since those are the ones
that get asked in some form at almost every defense. Good luck tomorrow.
