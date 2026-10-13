# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 6bbd4579 | **Time:** 12.51s | **Cost:** $0.01789
--------------------------------------------------------------------------------

Spatial clustering characteristics shape the **quality-time trade-off** in heuristic path planning in two opposite ways, depending on whether the planner is **cluster-aware** or **cluster-oblivious**.

1. **Cluster-oblivious heuristics** (standard GA, SA, A*, etc.)  
   - **Quality drops**: the search keeps jumping from one dense cluster to another, so the incumbent solution is repeatedly “fooled” by locally attractive but globally poor partial routes.  
   - **Time rises**: the same clusters are re-explored in every restart, the effective branching factor grows, and the algorithm needs more iterations to escape the resulting local optima.  
   → **Worse quality and longer time** as clustering increases.

2. **Cluster-aware heuristics** (two-level, ST-VNSGA, GRIA, HPD, DBSCAN+K-means, etc.)  
   - **Quality rises**: once clusters are extracted, the intra-cluster routing can be solved almost optimally by a cheap TSP solver, while the inter-cluster problem is a much smaller VRP; the global optimum is therefore approached from both sides.  
   - **Time falls**: the search space is collapsed from O(n²) edges to O(k²) inter-cluster edges (k ≪ n); low-level refinement is run only inside clusters, so each iteration is cheaper and fewer iterations are required.  
   → **Better quality in less time** as clustering increases.

Hence the **same spatial clustering** that hurts “plain” heuristics becomes a **free accelerator** for heuristics that explicitly exploit it. The break-even point is usually reached with only a few dozen customers per cluster; beyond that, cluster-aware methods dominate the quality-time frontier.

## Annotations


## Sources
