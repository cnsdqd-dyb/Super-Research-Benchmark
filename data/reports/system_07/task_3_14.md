# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** e848955e | **Time:** 15.55s | **Cost:** $0.00918
--------------------------------------------------------------------------------

In migration networks, **edge-weight optimization** is the process of adjusting the **transition probabilities** (i.e., the weights on directed edges between regions) so that the **Markov chain converges to a desired equilibrium distribution** of population across regions.

### Key Role in Establishing Markov Equilibrium:

1. **Defines the Transition Matrix**  
   Edge weights directly determine the **entries of the Markov transition matrix** \( P = [p_{ij}] \), where \( p_{ij} \) is the probability of moving from region \( i \) to region \( j \). These probabilities must satisfy \( \sum_j p_{ij} = 1 \) for each \( i \).

2. **Shapes the Stationary Distribution**  
   The **stationary distribution** \( \pi \) of the Markov chain satisfies:  
   \[
   \pi = \pi P
   \]  
   This \( \pi \) represents the **long-term regional population distribution**. By **optimizing edge weights**, we can **steer** \( \pi \) toward a target distribution—such as one that balances population density, economic opportunity, or resource availability.

3. **Enforces Constraints and Objectives**  
   Optimization can incorporate:
   - **Capacity constraints** (e.g., maximum population per region)
   - **Policy goals** (e.g., reduce overcrowding in urban centers)
   - **Cost minimization** (e.g., reduce total migration distance or cost)

4. **Ensures Convergence and Stability**  
   Properly optimized weights ensure the Markov chain is:
   - **Irreducible** (all regions are reachable)
   - **Aperiodic** (no cyclic trapping)
   - **Positive recurrent** (equilibrium exists and is unique)

---

### Summary:
Edge-weight optimization **calibrates the migration flow structure** so that the **Markov process converges to a stable, policy-aligned equilibrium** of regional population distribution. It is not just a technical step—it is the **mechanism by which demographic outcomes are engineered** in migration network models.

## Annotations


## Sources
