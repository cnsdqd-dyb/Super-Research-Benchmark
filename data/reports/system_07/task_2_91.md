# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** eb69885c | **Time:** 13.78s | **Cost:** $0.01493
--------------------------------------------------------------------------------

The strategy that guides marketing-node selection in word-of-mouth (WOM) propagation networks is called **Influence Maximization (IM)**.  
Its practical form is “seed-selection under a diffusion model”, and every mainstream WOM campaign today is governed by the following four-step IM pipeline:

1. **Pick a diffusion model that matches the campaign’s real-world constraints**  
   - Single-product, low-budget, quick reach → Independent Cascade (IC), SI, SIR  
   - Competing brands / multiple rumours → Competitive IC (CIM), TIC, Attic, Stackelberg leader–follower models  
   - Opinion-sensitive products (films, politics) → Opinion dynamics (ISR, POE, LIM)  
   - Community or trust-based items → Group-oriented models (TAM, PCL-DC, Trust Model)  
   - Long-term adoption forecasting → Marketing-oriented models (VMID, MAT, UAD)

2. **Encode business costs and node “price”**  
   - Distance-aware IM (DAIM) for bricks-and-mortar businesses: embed spatial cost so that seeds close to the store get higher weight.  
   - Arbitrary node cost: replace raw influence by “influence-per-dollar” so a slightly less influential but much cheaper blogger can enter the seed set.

3. **Optimise the seed set under the chosen model**  
   - Objective: maximise expected number of activated nodes (or revenue) subject to cardinality or budget constraint.  
   - Greedy hill-climbing with Monte-Carlo simulation gives the canonical (1 – 1/e) ≈ 63 % guarantee.  
   - Accelerated versions used in practice: CELF, CELF++, SIMPATH, TIM/TIM+, SKIM, Reverse-Reachable sketches, etc.  
   - For competitive settings the leader first fixes seeds; the follower solves a “best-response IM” that is still NP-hard but admits the same greedy approximation.

4. **Enrich the selection with side information**  
   - Network centrality heuristics (degree, eigenvector, betweenness, k-core, Rank-Degree) give fast but coarse seeds when real-time optimisation is impossible.  
   - Homophily and purchase-history similarity are added so that the seed audience resembles the firm’s core customers.  
   - Temporal and reinforcement effects (time-evolving graphs, social reinforcement thresholds) are folded in when the campaign must reach a target public before a deadline.

Hence, **IM under the right diffusion model plus cost-adjusted greedy optimisation** is the overarching strategy that tells a marketer exactly which customers should be the “first mouths” in a WOM campaign.

## Annotations


## Sources
