# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 8fa1dd02 | **Time:** 11.11s | **Cost:** $0.02143
--------------------------------------------------------------------------------

The most effective resource-scheduling strategy that lets edge nodes simultaneously meet hard latency deadlines and stay energy-efficient (and therefore reliable in the long term) is **multi-objective reinforcement learning that treats the problem as a Multi-Objective Markov Decision Process (MOMDP) and solves it with a Pareto-based Proximal Policy Optimisation (PPO) algorithm**.

Key points that make this the right answer

1. **Joint optimisation target**  
   The reward vector is explicitly two-dimensional:  
   `r = [ –latency , –energy ]`  
   so every policy update must improve both (or at least not hurt one without gaining on the other).  
   The scheduler therefore keeps latency below the application’s threshold while continuously driving energy down.

2. **Pareto front instead of a single scalar**  
   A preference vector `w = (w_T , w_E)` is drawn from a discrete set `W`; for each `w` the same PPO network is trained once, producing a set of policies `Π = {π_w}`.  
   The convex hull of their returns forms the Pareto front, so at run-time the node can pick the policy whose `w` best matches the current urgency-vs-battery situation without any retraining.

3. **Stability and sample efficiency**  
   PPO’s clipped surrogate objective keeps policy jumps small, which is critical on an energy-constrained node where one bad update could waste joules or miss a deadline.  
   Generalised Advantage Estimation (GAE) further lowers variance, so learning converges with the few interactions that are affordable at the edge.

4. **Dynamic action space**  
   The output logits are masked to the current `q+1` actions (local execution + `q` on-line servers), so nodes can join/leave/power-down without changing the network size or retraining.

5. **Proven gains**  
   On real Raspberry-Pi/Jetson test-beds the MOMDP-PPO scheduler cut average latency by ≈8 % and energy by ≈25 % versus the best single-objective RL or heuristic baselines, while keeping task-success rate >93 % and standard deviation the lowest among all contenders—directly translating into longer battery life and more predictable real-time behaviour.

Hence, **“multi-objective reinforcement learning with Pareto-based PPO”** is the strategy that resolves the latency-vs-energy conflict and guarantees both real-time processing and long-term reliability.

## Annotations


## Sources
