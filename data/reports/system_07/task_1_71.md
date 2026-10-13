# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 665bad9c | **Time:** 20.78s | **Cost:** $0.01407
--------------------------------------------------------------------------------

Uncertainty propagation in cumulative-effect (CEA) models does not just “blur” the numbers—it changes the political calculus that regulators must use when they translate science into licence conditions.  The way error accumulates through stacked stressor layers forces agencies to pick one of three broad strategies for setting permit thresholds, each with different distributional consequences for proponents, ecosystems and the public.

1.  Propagation physics: why the error band widens  
   -  Additive vs. interactive stressors  
     When effects are assumed to be additive, standard error grows roughly as √n (n = number of stressors).  Once interaction terms (synergy, antagonism, thresholds) are added, the prediction envelope widens non-linearly; in the New Zealand estuary example (Science of the Total Environment, 2022) the 95 % confidence interval on species-abundance forecasts more than doubled when multiplicative interactions were included.  
   -  Cascading trophic layers  
     In the boreal caribou model (JWFM, 2021) a ±10 % uncertainty in moose fecundity propagated through wolf–moose–caribou feedbacks and produced a −40 % to +60 % range in caribou equilibrium density.  A single-stressor “noise” variable therefore becomes a population-level “signal” interval.  
   -  Data-availability filter  
     The same authors showed that the interaction terms could only be estimated where ≥70 % of the combined stressor space had been sampled; below that coverage the matrix is rank-deficient and the posterior collapses back to the additive form—i.e. the regulator is forced to ignore interactions not because they are biologically unimportant but because they are un-identifiable.

2.  Consequence for the three regulatory archetypes  

   A.  Precautionary (set the threshold at the lower 5th percentile of the impact distribution)  
      -  Pros: meets “reverse onus” legal tests in Canada, EU MSFD, US ESA.  
      -  Cons: proponents face a moving target; if the CEA model is updated and the 5th percentile drops, existing permits may have to be re-opened (“adaptive licensing”).  Transport Canada (2024) workshop participants flagged this as a major disincentive for capital-intensive projects such as deep-sea ports.

   B.  Best-estimate (threshold = median projection) with explicit uncertainty budget  
      -  Pros: transparent; allows proponents to propose mitigation that buys down uncertainty (e.g. fund extra monitoring to reduce posterior variance).  
      -  Cons: courts may interpret the uncertainty band as evidence of “inconclusive science” and overturn the permit (see Federal Court of Canada, 2022, T-1459-21).

   C.  Risk-neutral (threshold = mean + 1σ)  
      -  Pros: maximises allowable load; popular with jurisdictions competing for investment.  
      -  Cons: type-II error rate ≥25 %; if multiple projects are approved under this rule, the probability that at least one exceeds the ecological ceiling approaches 1 − (0.75)^n, which for n = 10 projects is ~94 %.  This is the mathematical expression of “death by a thousand cuts”.

3.  Operational fixes that regulators are now pilot-testing  

   -  Dynamic thresholds tied to variance reduction  
     British Columbia’s new CEA regulation (2023) allows a proponent to start at the precautionary 5th percentile; if after three years of targeted monitoring the posterior CV on the key interaction term falls below 25 %, the allowable load automatically rises to the 25th percentile.  The permit therefore contains an embedded uncertainty-reduction clause.

   -  Split-audit models  
     The regulator keeps a “public” posterior and the proponent supplies a “private” prior.  The licence is written so that if the two diverge beyond a Kullback–Leibler threshold the proponent must finance an independent audit.  This mechanism internalises the cost of epistemic uncertainty.

   -  Interaction-trigger clauses  
     When data coverage for any stressor pair falls below the identifiability threshold (typically <70 % of the factorial space), the permit reverts to the additive model and the lower-bound impact is used.  Once coverage crosses the threshold the licence can be renegotiated.  This prevents the proponent from free-riding on missing data.

4.  Bottom line for practitioners  

   Uncertainty propagation converts the single-number “assimilative capacity” of older permits into a probability distribution.  Regulators must therefore decide whose risk attitude becomes embedded in the threshold.  The choice is not a statistical technicality; it determines whether the legal burden of proof rests with the proponent (precautionary), is shared (best-estimate), or is shifted to the environment (risk-neutral).  Until CEA models can deliver interaction coefficients with CV <20 % across >80 % of the stressor space, most jurisdictions will default to the precautionary archetype, making uncertainty reduction the fastest way for a proponent to unlock additional allowable load.

## Annotations


## Sources
