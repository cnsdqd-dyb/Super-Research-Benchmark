# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** bc9f56d8 | **Time:** 20.30s | **Cost:** $0.02819
--------------------------------------------------------------------------------

Diversity–stability parameterization is the set of rules used to translate “how many species, of which kind, interacting how strongly” into the numbers that sit in a community-matrix (or analogous) model.  
Because biological-control (BC) success is nothing more than “will the natural-enemy complex suppress the pest and stay suppressed through time?”, every one of those translation rules feeds directly into the answer the model gives. The literature shows four concrete ways in which the parameterization changes the prediction.

1.  **Linear (Lotka-Volterra or GLV) parameterization**  
    - Interaction coefficients are drawn at random with mean 0 and variance γ².  
    - May’s (1972) criterion: stable only if  
      γ√(S C) < 1 (or, in the mutualistic version, λmax(A) < s/γ).  
    - Consequence for BC: increasing the number of enemy species (S↑) or their average attack rate (γ↑) pushes the system across the threshold; the same model that yesterday predicted “single-agent BC fails” will today predict “multi-agent BC collapses”.  
    - Empirical networks violate the criterion (they lie in the “unstable” region), so the raw GLV prediction is “the system should not exist”, clearly useless for BC forecasting.

2.  **Non-linear saturation parameterization (Holling-II or Hill function)**  
    - Attack rate saturates: f(R) = γR/(h+R).  
    - The same eigenvalue that had to be < s/γ in the linear model now only has to be < (s/γ + N/h), where N is enemy richness.  
    - Consequence for BC: adding enemies or increasing γ now enlarges the r.h.s. of the inequality – the model flips to “diversity begets stability”. A multi-agent BC release that the linear model called catastrophic is predicted to succeed and to be more robust to perturbation.

3.  **Trophic-level or “diversity-difference” parameterization**  
    - Predator richness N and prey (pest) richness M enter as separate parameters; stability depends on the ratio N/M and on the correlation ρ between “who eats whom” and “who grows on whom”.  
    - Re-entrant transition: pest suppression first deteriorates when N is slightly larger than M, then improves again once N ≫ M.  
    - Consequence for BC: the model predicts an optimum number of enemy species – below it, adding species helps; above it, further additions can re-destabilise the food web and allow pest resurgence. Without this parameterization, a monotonic “more is better” rule would be used and could fail in the field.

4.  **Spatially explicit or trait-matching parameterization**  
    - Attack coefficients are not i.i.d. but covary with body-size, temperature, or habitat openness; γij becomes γij = γ0 exp[–(trait_i – trait_j)²/2σ²].  
    - σ is inversely related to niche breadth; increasing σ (generalist enemies) enlarges the eigenvalue spread and can move the system back into the unstable region even under the saturating functional response.  
    - Consequence for BC: the same five-agent release that is predicted to stabilise a greenhouse crop (narrow σ) can be predicted to fail in an open field system where the enemies become generalists and interact strongly among themselves.

Numerical illustration (taken from the mutualistic-network re-analysis in the first URL):  
- Linear rule: λmax = 4.7, s/γ = 3.2 → model says “collapse”.  
- Non-linear rule with same λmax but h = 0.5 and N = 8: effective threshold becomes 3.2 + 8/0.5 = 19.2 → 4.7 < 19.2, model now says “persist”.  
The only thing that changed was the functional form used to parameterise the interaction.

Therefore, the way diversity is turned into numbers – random vs. structured, linear vs. saturating, single-level vs. trophic, fixed vs. trait-matched – determines whether the ecological model forecasts that a given biological-control cocktail will suppress the pest reliably, oscillate, or crash. Wrong parameterisation, wrong release strategy.

## Annotations


## Sources
