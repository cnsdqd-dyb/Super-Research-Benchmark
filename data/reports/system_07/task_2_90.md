# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 354a64d5 | **Time:** 14.70s | **Cost:** $0.01191
--------------------------------------------------------------------------------

The “threshold” that decides how many warehouse nodes you should push down to the lower echelons of a hierarchical network is not a single magic number; it is the value at which the marginal cost of adding one more node is exactly offset by the marginal gain in the performance metric that the hierarchy is designed to optimise.  
Everything that shifts either the marginal-cost curve or the marginal-gain curve therefore shifts the threshold.  The literature and the case-specific models converge on six groups of drivers:

1. **Service-level target (β)**  
   - The model must guarantee that a prescribed % of demand is filled within a prescribed time window.  
   - The tighter the time window or the higher the fill-rate β, the more nodes have to be close to the customers, so the threshold number of forward/field warehouses rises.

2. **Risk-resilience target (Rmax)**  
   - A maximum acceptable aggregate risk (probability of disruption × impact) is treated as a hard constraint.  
   - Because risk is usually assumed proportional to the shipment volume on any lane, splitting the volume over more nodes reduces risk.  
   - A lower Rmax directly raises the optimal node count.

3. **Geographic demand-weighted distance (centroid dispersion)**  
   - Green-field “centre-of-gravity” runs give the theoretical minimum-distance solution.  
   - Each time the weighted distance saving produced by another node falls below the incremental fixed + variable cost of that node, the algorithm stops; the node count at that point is the threshold.

4. **Fixed cost versus variable cost ratio (F/c)**  
   - High real-estate, construction or maintenance cost (F) pushes the threshold down; high transport cost (c) or a low F/c ratio pushes it up.  
   - Sensitivity analysis on this ratio is the quickest way to see how the threshold reacts to local labour or land prices.

5. **Capacity and policy constraints**  
   - Maximum allowable capacity per node (e.g., military field warehouse, humanitarian ISF) forces the network to split volume once the limit is reached, mechanically raising the threshold.  
   - “No lateral transshipment” or “no flow between DPs” policies remove the pooling benefit of fewer nodes and therefore raise the threshold.

6. **Parametric weighting coming out of the AHP or pairwise-comparison stage**  
   - In military or disaster-relief models, qualitative factors ( concealment, distance to railhead, flood risk, enemy-threat index) are translated into weights through an analytic-hierarchy process.  
   - The composite weight has to exceed a cut-off value for a candidate site to be admitted; raising the cut-off lowers the node count, lowering it does the opposite.  Hence the “threshold” in the GIS layer is literally the minimum composite weight computed in the hierarchy.

Putting it together  
Optimal warehouse node distribution threshold = the smallest integer k such that  
ΔService(k) + ΔRisk(k) ≥ ΔCost(k)  
where the deltas are the marginal changes when the kth node is added.  All six drivers above shift one of the three delta terms and therefore move the breakeven k* to the left or to the right.

## Annotations


## Sources
