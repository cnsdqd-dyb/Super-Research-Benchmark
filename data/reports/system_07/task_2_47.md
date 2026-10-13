# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 2b1b079c | **Time:** 18.29s | **Cost:** $0.02711
--------------------------------------------------------------------------------

Survival-analysis-based churn models **do** let you keep both “when” and “why” in the same equation, but the moment you start **paring-down covariates** (the usual step in a Cox model) you tilt the trade-off toward **speed and parsimony** and away from the very signals that matter for **long-term retention**.  
In other words, the algorithm *can* balance timeliness and complexity, yet the **standard covariate-selection routine for Cox models usually breaks that balance**.

Key points behind the tension

1. Timeliness vs. feature richness  
   - Survival models already deliver the “when” (hazard / survival curve), so marketing does not have to wait for a hard 30-/90-day label.  
   - To keep the scoring pipeline fast, analysts typically drop covariates with low Wald χ² or high VIF.  
   - The dropped variables are often **slow-burn predictors** (e.g., seasonal usage slope, support-thread depth, third-year price index) that only pay off for **long-horizon retention**.

2. Proportional-hazards straight-jacket  
   - Cox assumes the *relative* effect of a covariate is constant over tenure.  
   - If you force long-term variables into the model you frequently violate PH; the penalty is either (a) non-significant coefficients that get removed, or (b) time-split / time-interaction terms that explode the number of parameters and defeat the “simple, fast” goal.  
   - Hence **variable-selection routines tend to prune anything whose hazard ratio drifts**, even when that drift is *real* and **actionable for retention**.

3. Empirical evidence  
   - The Springer utility-dataset study (2025) shows that once contracts expire, CPH accuracy collapses (concordance drops 8-10 pts) because the pre-selected covariates were “before-end-of-contract” proxies.  
   - The Aalen additive model—no PH assumption, keeps the same covariates—recovers most of that lost signal, especially post-contract.  
   - Deep-time-to-event networks (DeepHit, Cox-Time) beat both Cox and Aalen on large data, but they keep **all** time-varying features; when the same nets are fed the *reduced* feature set chosen by the Cox step-wise routine, their edge shrinks to noise.

4. Business implication  
   - A lean Cox scorecard is perfect for **next-month** call-list generation.  
   - It **under-estimates late churn** (month 13-24), so retention campaigns thin out exactly when CLV is highest.  
   - Long-term programmes (loyalty tiers, annual price locks, seasonal upgrades) need the **slow variables** that were thrown away.

Practical work-arounds that keep the balance

- Fit **two linked models**: a sparse Cox for 0-6-month “hot” alerts, and a second model (Aalen, RSF, or DeepSurv) that keeps the full feature stack for 6-36-month CLV-based decisions.  
- Use **penalised Cox** (lasso or elastic-net) instead of step-wise deletion; it shrinks coefficients but rarely zeros out the weak long-term signals entirely.  
- Keep **time-varying covariates** as optional splines / tensors; accept a slightly heavier scoring pipeline in exchange for retaining the long-range slope information.  
- Validate with **time-dependent AUC / Brier curves** at 3, 6, 12, 24 months, not just a single concordance index; force the selection loop to defend cuts that hurt later horizons.

Bottom line  
The survival framework itself is not the culprit; **the way we usually select covariates inside a Cox model** is what sacrifices long-term retention insight for short-term scoring speed. If you treat covariate choice as a **multi-horizon optimisation** instead of a “make-it-simple” filter, survival analysis can deliver both timeliness and strategic depth.

## Annotations


## Sources
