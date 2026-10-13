# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** e5ce83ea | **Time:** 23.55s | **Cost:** $0.02250
--------------------------------------------------------------------------------

The **optimal budget allocation ratio** in multi-channel marketing is not a fixed number—it is the output of a constrained optimization problem whose objective is **maximizing the expected business outcome** (sales, profit, CLV, conversions, etc.) subject to

1. a finite total budget,  
2. channel-level diminishing-returns curves,  
3. cross-channel synergy / cannibalization effects,  
4. tactical guardrails (minimum/maximum spend per channel, legal, brand-safety, staffing), and  
5. time dynamics (seasonality, ad-stock, carry-over, attribution lag).

What “determines” the ratio is therefore the set of **estimable parameters** that enter this optimization:

--------------------------------------------------------------------
1. **Marginal Return curves**  
   Empirically estimated response functions for every channel  
   (usually concave: log, power, or s-shaped).  
   → Dictate how much extra return the next €1 will generate.

2. **Saturation point**  
   The spend level where marginal ROAS drops below the blended cost-of-capital or the next-best channel’s marginal ROAS.  
   → Once a channel hits saturation, additional dollars are optimally re-allocated.

3. **Cross-elasticities / synergy matrix**  
   Quantified interaction terms (e.g., display lifts search CTR, email lifts conversion rate on retargeting).  
   → A negative cross-elasticity (cannibalization) lowers the optimal share; a positive one raises it.

4. **Attribution weights or Shapley/MTA values**  
   Give credit to touch-points that lie higher in the funnel but are essential for final conversions.  
   → Channels that look “expensive” on last-click may still receive more money once true incremental contribution is modelled.

5. **Customer-level heterogeneity**  
   CLV or profit pool by segment × channel cost to reach that segment.  
   → Channels that attract high-CLV customers receive a higher share even if CPA is higher.

6. **Risk-adjusted perspective**  
   Bayesian or stochastic optimisation incorporates parameter uncertainty; a risk-averse planner will underspend in high-variance channels even if mean ROAS is attractive.

7. **Constraints**  
   - Budget ceiling (hard)  
   - Minimum spend to “stay on air” (TV GRP threshold, Google Impression-Share target)  
   - Inventory limits (e.g., TikTok CPM spikes once spend > $X)  
   - Legal/margin constraints (no more than 20 % promo sales)

--------------------------------------------------------------------
Practical recipe used by MMM & budget-opt engines

1. Estimate channel-level response functions with Marketing-Mix-Model or Bayesian hierarchical regression.  
2. Feed the functions into a non-linear optimiser (Sequential Quadratic Programming, Genetic Algorithm, or Reinforcement-Learning policy such as PGPE) with the above constraints.  
3. Output: spend vector {S*1, S*2, …, S*k} that maximises  
   Objective = Σᵢ Salesᵢ(Sᵢ) + Σᵢⱼ Γᵢⱼ Sᵢ Sⱼ – λ·Risk  
   under Σᵢ Sᵢ ≤ B, Sᵢ ≥ Lᵢ, Sᵢ ≤ Uᵢ.  
4. Re-run weekly/monthly as new data updates the curves.

--------------------------------------------------------------------
Heuristic shortcuts (when full optimisation is not possible)

- **70-20-10 rule**  
  70 % to proven ROI channels, 20 % to promising but unproven, 10 % to pure experiments.  
  Works as a governance rule, not as a true optimum.

- **Funnel mapping**  
  40 % top-funnel (video, display), 35 % mid (paid social, email), 25 % bottom (search, shopping, retargeting).  
  Useful starting point, but still needs marginal ROAS check.

- **Equalised marginal ROAS**  
  Shift dollars until marginal ROAS of every active channel is equal (respecting constraints).  
  This is the first-order condition of the optimisation above and is easy to implement in spreadsheets.

--------------------------------------------------------------------
Bottom line

The **optimal ratio is determined by the shape of the empirical response and interaction functions**, not by industry benchmarks.  
Build the curves → let the optimiser tell you the percentages → keep 10-15 % of the budget fluid so you can re-optimise every 2-3 weeks as new data arrives.

## Annotations


## Sources
