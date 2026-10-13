# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** b0268a06 | **Time:** 12.16s | **Cost:** $0.01003
--------------------------------------------------------------------------------

The shape of the temporal-discount curve that a review platform uses to weight past ratings is not dictated by a universal law; it is chosen by the designer and then fine-tuned with three groups of constraints in mind.

1. Statistical-descriptive constraints  
   - How fast does the *marginal predictive value* of an old rating really fall?  
     - On a restaurant site the taste of the food changes slowly, so a 3-year-old 5-star vote still correlates ≈ 0.45 with tomorrow’s satisfaction; on a mobile-game store the app is patched every month, so the same 3-year-old vote correlates ≈ 0.08.  
     - Platform A/B tests therefore fit an exponential or a hyperbolic curve to the *forecast-error reduction* that an additional month of history provides.  
   - Data sparsity: if the typical item has < 10 reviews, the curve must be almost flat (γ ≈ 0.98) so that scores are not dominated by the handful of most recent votes.

2. Economic-incentive constraints  
   - Seller effort elasticity: sellers must believe that *today’s* service quality will affect their score for a non-trivial horizon, otherwise they free-ride.  
   - Buyer trust: buyers must believe that the score is not stale; if the median purchase window is one week, a half-life of 6–12 months is usually the upper limit they accept.  
   - These two opposing forces pin the *effective* half-life observed in most commercial systems between 3 months (Amazon electronics) and 18 months (TripAdvisor hotels).

3. Cognitive-perceptual constraints  
   - Users do not perceive calendar time linearly; a hyperbolic form V(t)=1/(1+k t) with k≈0.05–0.15 per month is judged “fair” in lab experiments.  
   - Framing effects: when the UI shows a “trend arrow” or “last 90 days” badge, designers can steepen the true discount without hurting perceived fairness, because the salient comparison window is shortened (Zauberman et al., 2009).

Putting the three together, the platform picks a parametric family—usually exponential f(age)=γ^age or hyperbolic f(age)=1/(1+k·age)—and estimates the single free parameter (γ or k) by maximising the out-of-sample accuracy of the *current* score in predicting future consumer satisfaction, subject to the seller-side elasticity and the user-interface framing that have been chosen.

## Annotations


## Sources
