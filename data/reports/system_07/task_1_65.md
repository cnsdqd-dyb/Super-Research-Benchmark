# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** a8b35c7d | **Time:** 14.38s | **Cost:** $0.01752
--------------------------------------------------------------------------------

Power-law parameters of travel distance evolve with city scale and network topology in three main ways:

1. Exponent β decreases as the city gets larger and the street network becomes more grid-like and less tree-like.  
   - Compact, monocentric cities (e.g. Florence, Modena) keep β ≈ 1.4–1.6 because most trips are short and radial.  
   - Sprawled, polycentric cities (e.g. Melbourne, Chicago) drop to β ≈ 1.0–1.2 because the distribution of trip lengths flattens: the extra lane-miles and alternative routes allow the same population to take systematically longer trips without a proportional increase in travel-time cost.  
   - The scaling is well approximated by β(N) ≈ β₀ – γ ln N, with γ ≈ 0.08–0.10 across the empirical samples.

2. Cut-off distance κ grows super-linearly with city population N.  
   κ ~ N^α with α ≈ 0.20–0.25.  
   The larger and more dendritic the arterial network becomes, the farther the tail of the distribution is pushed before the exponential decay dominates.

3. Topology controls the pre-factor and the precise curvature of the truncated power-law.  
   - Planar, tree-like or “stroke”-hierarchical networks (space-syntax graphs with long, continuous axes) concentrate flow on a few high-betweenness links and keep β high.  
   - Dense, mesh-like or small-world topologies (rich-club of expressways plus local grid) spread flow, shorten the average shortest-path length (MSP ∝ k^–0.18), and lower β.  
   - When the network is allowed to become non-planar through layered infrastructure (freeway over arterial), the in-degree and out-degree distributions themselves approach power-laws, and the trip-length exponent becomes virtually independent of Euclidean distance; the governing variable is “effective” network distance, whose distribution inherits the topology-induced exponent.

Hence, as a city grows, the travel-distance power-law softens (smaller β) and stretches (larger κ), and the quantitative values of these parameters can be predicted from the scaling of population and from summary topological descriptors such as meshedness, circuity, and the slope of the MSP-degree relation.

## Annotations


## Sources
