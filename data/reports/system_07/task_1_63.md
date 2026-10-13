# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 7097836b | **Time:** 27.25s | **Cost:** $0.01878
--------------------------------------------------------------------------------

Non-linear density-velocity relations are the mathematical “origin” of the phase-transition that the MFD is supposed to reproduce.  
Everything that happens to the MFD in the neighbourhood of the critical density ρc can be traced back to the shape of the v(ρ) curve and, in particular, to the way its first and second derivatives behave.

1.  **Loss of convexity of the flux–density relation**  
    q(ρ)=ρ v(ρ).  
    If v(ρ) is strictly concave (v′<0, v″≤0) the product ρ v(ρ) is convex and the LWR model is hyperbolic with a single maximum (capacity).  
    As soon as v(ρ) ceases to be concave – which is always the case in real data once drivers start over-reacting at ≈ 25–35 veh/km/lane – q(ρ) becomes non-convex.  
    Non-convexity creates a interval [ρ1,ρ2] in which q″(ρ) changes sign; inside this interval the fundamental diagram is no longer a single-valued function but a “fold” that can be crossed only by a discontinuity (shock).  
    ⇒ the MFD predicted by any first- or second-order model that keeps the non-concave v(ρ) necessarily exhibits:

    *   a sudden drop of speed and flow instead of a smooth parabolic top,  
    *   a density interval in which three different flows are mathematically admissible for the same density (the classic “inverse-λ” or “Z” shape).

2.  **Location and sharpness of the transition**  
    The critical density ρc is the abscissa where the chord that connects the two branches of the folded q(ρ) is tangent to the curve (Maxwell-like construction).  
    Because v(ρ) is nonlinear, a small change in a microscopic parameter (desired time-headway, reaction time τ, aggressiveness a in OV-models, road-condition parameter α in kinetic models) moves the inflection point of v(ρ) and therefore shifts ρc by several veh/km/lane.  
    ⇒ the MFD prediction is extremely sensitive to the exact curvature of v(ρ) near ρc; calibration errors of only a few percent in the nonlinear part of v(ρ) move the predicted capacity point by 10–15 %.

3.  **Metastable branch and hysteresis**  
    The non-concave v(ρ) produces a decreasing branch of q(ρ) that is linearly stable but nonlinearly unstable.  
    Numerical simulations (Delitala–Tosin, OV, PTM) show that this branch acts as a “metastable” region:  
    –   if the initial condition is on the upper part of the branch the system can stay there for O(10² T) before nucleation of a jam collapses the flow;  
    –   once the system has jumped to the congested branch it will not jump back at the same density because the reverse shock sits at a lower ρ.  
    ⇒ the MFD measured in simulation or in the field displays a hysteresis loop whose width is proportional to the size of the interval where v″(ρ)>0.

4.  **Variance peak and capacity scatter**  
    The second consequence of the nonlinear v(ρ) is that the equilibrium speed variance  
    Θ(ρ)=⟨(v−⟨v⟩)²⟩  
    is proportional to −ρ v′(ρ).  
    Exactly at the density where v′(ρ) changes curvature, Θ(ρ) attains its maximum.  
    ⇒ every macroscopic model that keeps the nonlinear v(ρ) predicts a sharp peak of velocity variance at ρc; the larger the nonlinearity, the larger the peak.  
    Because the stochastic MFD is obtained by ensemble-averaging q over many realisations, the large Θ(ρc) translates into a large standard deviation of the flow at capacity, i.e. the well-known “capacity-drop” distribution observed in empirical MFDs.

5.  **Prediction error near ρc**  
    *   If a macroscopic model is calibrated on free-flow data only (ρ<ρc) and uses a linear or exponential v(ρ) that is still concave at ρc, it will overestimate the capacity and predict a smooth quadratic MFD.  
    *   Conversely, if the model uses a v(ρ) that is too steep in the neighbourhood of ρc (e.g. a high-order polynomial fitted to congested data) it will underestimate capacity and predict a premature collapse.  
    *   The only way to obtain the correct location and the correct discontinuity is to keep the non-concave shape of v(ρ) that comes out of car-following or kinetic equations; replacing it by a convenient “fundamental-diagram” function (Greenshields, Daganzo-Newell, etc.) removes the mathematical mechanism that creates the phase transition and therefore mis-locates ρc and erases the hysteresis loop.

**Bottom line**  
The nonlinear density-velocity characteristic is not just a refinement: it is the term that destroys the convexity of the flux–density relation and thereby creates the fold that the MFD must exhibit at the free-flow → congested transition.  
Any macroscopic model that linearises or smooths v(ρ) around ρc will necessarily

*   shift the predicted critical density,  
*   remove the metastable branch,  
*   suppress the hysteresis and the capacity scatter,  
*   under- or over-estimate network capacity.

Accurate MFD prediction near phase transition therefore requires that the *exact* non-concave, inflection-carrying v(ρ) delivered by microscopic calibration is retained in the macroscopic equation.

## Annotations


## Sources
