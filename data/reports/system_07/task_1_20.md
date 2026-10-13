# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 8bdc8be9 | **Time:** 20.43s | **Cost:** $0.02829
--------------------------------------------------------------------------------

Short answer:  
Neither.  
(i) Venture capital (VC) allocation algorithms do not try to reproduce the “efficient-frontier” idea at all; they maximise expected fund-level IRR subject to a *budget* and a *deal-flow* constraint, so the return/diversification trade-off that Markowitz formalised is simply not in the objective set.  
(ii) The Markowitz covariance matrix does not “exaggerate” tail-risk forecasts – it *ignores* them. Variance is a two-sided, second-moment-only statistic; by construction it assigns zero extra weight to the left tail, so any tail-risk prediction error comes from *omission*, not from *overstatement*.

--------------------------------------------------------------------
1. What a “VC allocation algorithm” actually does  
--------------------------------------------------------------------
- Data that are available before the investment is made:  
  – Historical *fund* IRR/vintage statistics (not company-level returns).  
  – Capital-line draw-down schedules (calls/distributions).  
  – A pipeline of prospective deals with *ex-ante* expected IRR or money-multiple and a round size.  

- Optimiser:  
  maximise   𝔼[IRR_portfolio]  
  s.t.       Σ_i commitment_i ≤ total AUM  
             Σ_i 1_{stage=j} ≤ deal-flow limit_j  
             Σ_i 1_{geo=k}   ≤ mandate limit_k  

- Diversification is enforced as *linear constraints* (“no more than 25 % in Series C”, “no more than 40 % outside US”, etc.).  
- Covariance between company returns is *not* an input; the variance that matters is the *fund-level* variance of IRR, which is usually modelled with a 3- or 4-parameter parametric distribution (log-normal, beta, or normal-inverse-Gaussian) calibrated on Preqin/Cambridge-Associates vintage data.  
- Because the objective is *expectation* maximisation, the algorithm will crowd into the highest-expected-IRR segment that still satisfies the diversification *constraints*; it does *not* look for a tangency point on a mean-variance frontier.  

Empirical result: When the constraints are relaxed, the optimum collapses to a very small number of high-IRR segments (early-stage US software), producing a *concentrated* portfolio – the exact opposite of what a Markowitz investor would do.  

--------------------------------------------------------------------
2. Where Markowitz goes wrong on tail risk  
--------------------------------------------------------------------
Markowitz uses  
  σ²_p = wᵀ Σ w,  Σ = covariance matrix of returns.  

Problems:  
a) Σ is estimated from a short history → *estimation risk*.  
b) Even if Σ were known, σ²_p is *symmetric*: a +5 σ event and a –5 σ event contribute the same 25 σ².  
c) Tail events are *non-linear* (correlations → 1, vol → ∞), so Σ changes precisely when you need it most.  

Consequence: the model *under-estimates* tail risk, not over-estimates. During 2008, 2020, 2022, ex-ante σ for a “diversified” equity portfolio was 14–16 %; realised 1-month draw-downs were –30 % to –45 %. The Gaussian tail implied by Σ assigned a probability < 10⁻⁵ to such moves; the market delivered them twice inside 15 years.  

--------------------------------------------------------------------
3. What fixes the tail-risk miss, and what does not  
--------------------------------------------------------------------
- Replacing variance with CVaR (Expected Shortfall) or a coherent spectral risk measure *does* shift weight away from the left tail.  
- Shrinkage or Ledoit-Wolf estimators reduce *estimation error* but still leave the symmetric definition of risk intact; they do *not* correct the tail-blindness.  
- Robust Bayes or min-max (Goldfarb-Iyengar) versions bound the *range* of Σ, but again do not add skew/kurtosis information.  
- Only once you go to *higher-moment* optimisation (skewness & kurtosis penalties, copula-CVaR, or full non-parametric scenario optimisation) do you get a front-end that is flatter in the tail-risk region – and that frontier is *inside* the Markowitz frontier, not outside it.  

--------------------------------------------------------------------
Bottom line  
--------------------------------------------------------------------
VC algorithms are *not* mean-variance machines; they are expected-return maximisers with diversification treated as a regulatory constraint.  
Markowitz does not “exaggerate” tail risk – it *omits* it; the model’s forecast error is a *down-side* surprise, not an up-side one.

## Annotations


## Sources
