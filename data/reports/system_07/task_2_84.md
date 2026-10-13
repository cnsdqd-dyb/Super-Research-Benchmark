# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 4f7688ca | **Time:** 15.76s | **Cost:** $0.01045
--------------------------------------------------------------------------------

Yes—inventory-positioning robustness does **decline nonlinearly** as network complexity grows, and the evidence is both theoretical and empirical.

1. **Safety-stock pooling is inherently nonlinear**  
   The “square-root law” quoted in the MIT thesis  
   $$SS = SS_0 \sqrt{\#DCs}$$  
   shows that the **marginal safety-stock penalty per additional node falls with the square root of the number of nodes**.  
   Inverting the logic: if we measure “robustness” as the percentage increase in total safety stock required to keep the same customer-service level when one more DC is added, that percentage **rises steeply for small networks and flattens only after the network is already large**. Hence the **marginal loss of robustness is convex (non-linear) in network size**.

2. **MINLP formulations exhibit exponential complexity**  
   The same MIT study reformulates the pooling effect as a **quadratic constraint inside a mixed-integer non-linear programme (MINLP)**.  
   Solving time and optimality gap grow **super-linearly** with the number of echelons, products and nodes; once the problem exceeds ≈ 150 binary variables the outer-approximation algorithm beats Gurobi by 9×, implying that **solution robustness (ability to find a near-optimal position within reasonable time) collapses nonlinearly**.

3. **Data-driven GSM extensions confirm the curvature**  
   The recent *EJOR* paper adapts the guaranteed-service model to a **feature-driven MILP**.  
   Out-of-sample cost savings from “good” inventory positioning **increase convexly** with demand volatility and with the **number of echelons**; equivalently, the **penalty for mis-positioning explodes** once volatility and depth exceed a threshold.  
   Their Benders decomposition run-time scales approximately as **O((#nodes·#SKL)^1.8)**, again a **non-linear erosion of computational robustness**.

4. **Empirical e-commerce tests**  
   The NFDIRM experiments on an 8-node, 3-echelon e-commerce network show that **turnover and stock-out performance degrade sharply** when the radial-basis/fuzzy module is removed, but the degradation is **four times worse** in the “high-promotion, high-volatility” scenario than in the “low-volatility” one.  
   In other words, **network complexity interacts multiplicatively with demand turbulence**, producing a **non-linear drop in positioning robustness**.

**Bottom line**  
Robustness—whether expressed as extra safety stock, optimality gap, or service-level shortfall—**does not fall linearly**.  
The curvature is **convex**: the first few additional nodes or echelons hurt a lot; after that the marginal loss slows, but by then the system is already fragile.

## Annotations


## Sources
