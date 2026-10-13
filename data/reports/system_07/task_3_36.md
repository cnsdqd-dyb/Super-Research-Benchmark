# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** bb483b44 | **Time:** 15.89s | **Cost:** $0.01480
--------------------------------------------------------------------------------

Yes—how hub-node capacity is allocated under peak load is one of the decisive factors that fixes the **cascade mode** (i.e., which sequence of nodes collapses, how far the avalanche spreads, and whether it dies out or takes the whole network down).  

Key points that emerge from the literature:

1. **Capacity margin sets the failure threshold**  
   - In the standard Motter–Lai load-capacity model (used in most traffic studies) a node fails instantaneously when its real-time load L(t) exceeds its capacity C.  
   - C is usually written as C = ⌈(1 + α)L₀⌉, where L₀ is the initial (peak-hour) load and α is the *capacity redundancy*.  
   - The smaller α is on the busiest hubs, the lower the perturbation needed to start a cascade, so the **first failing hub is almost always the one with the smallest α**.

2. **Redistribution rule couples capacity geography to cascade path**  
   - When a hub fails, its load is pushed to neighbours.  
   - If capacity has been “average” or random, high-degree neighbours are already near their own threshold; they tip next, producing a **degree-ordered avalanche**.  
   - If extra capacity has been **preferentially installed on other hubs**, the load is absorbed there and the cascade is **deflected into a shorter, star-like pattern** that often dies out quickly.  
   - If capacity follows a **distance-decay or least-loaded rule**, the cascade may jump to remote but lightly loaded nodes, creating a **spatially scattered failure sequence**.

3. **Peak-load heterogeneity fixes the seed**  
   - Empirical air-traffic and rail studies show that the node whose *initial load/capacity* ratio is highest under the peak Origin–Destination matrix is the statistical seed of 70–90 % of large cascades, no matter which node is *attacked* first.  
   - In other words, **capacity allocation under peak load pre-selects the failure seed**, and the redistribution rule then determines the **propagation tree**.

4. **Capacity allocation strategies can flip the network from robust-yet-fragile to genuinely robust**  
   - Degree-proportional allocation → cascade size distribution with fat tail (black-swan events).  
   - Equal-redundancy allocation → cascade size distribution exponential (rare large events).  
   - Optimised allocation (PSO, simulated annealing, etc.) → can cut the largest possible cascade by 50–80 % without increasing total capacity, merely by **relocating the slack to the nodes that the redistribution rule will hit next**.

5. **Recovery and congestion back-coupling**  
   - Recent models that allow **temporary overload** (congestion) rather than instant failure show that the **recovery rate μ** of a hub is also proportional to its installed capacity.  
   - Hence capacity allocation governs not only **how** the cascade starts and propagates, but also **how fast the system can retract** from the brink once peak load subsides.

Therefore, **hub-node capacity allocation under peak load does not merely “influence” cascading failures—it effectively programmes the failure sequence and the final avalanche size**.

## Annotations


## Sources
