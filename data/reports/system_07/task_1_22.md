# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 038494dc | **Time:** 13.15s | **Cost:** $0.02211
--------------------------------------------------------------------------------

The short answer is: **both happen, but in different places in the literature.**  

1. **Behavioral-game-theoretic models of trading** (e.g., level-k, cognitive-hierarchy, quantal-response equilibrium) are explicitly designed to **keep a clean rational equilibrium concept and then add a bias-correction term** – typically a stochastic or bounded-rationality term that nests the Nash/rational expectation case as λ→0.  
   - The “bias” is therefore a **perturbation parameter** that can be estimated and, if desired, **subtracted out** to recover the rational benchmark.  
   - These models are used mainly to explain **price formation, strategic bidding, or market micro-structure anomalies** while still allowing welfare and comparative-static calculations relative to the rational equilibrium.

2. **Prospect-theory parameterizations** (α, β, λ, plus probability-weighting parameters) are **not bias corrections**; they are **positive descriptors** of the utility surface itself.  
   - Raising the loss-aversion coefficient λ **amplifies** the kink at the reference point and **increases** the implied willingness to pay to avoid a given loss.  
   - In portfolio-choice or asset-pricing applications this **widens the equity-premium prediction, deepens the disposition effect, and magnifies the gap from the frictionless CRRA/expected-utility optimum**; it does **not** converge back to that optimum as λ→1 (λ=1 already implies no loss aversion, but the value function is still kinked and probability-weighted).

So, **within behavioral game theory the rational equilibrium is preserved and biases are treated as corrective noise**, whereas **within prospect-theory implementations the loss-aversion parameter is a primitive that inherently enlarges departures from the rational benchmark rather than correcting toward it.**

## Annotations


## Sources
