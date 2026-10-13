# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** cb0cad05 | **Time:** 14.55s | **Cost:** $0.01546
--------------------------------------------------------------------------------

Convex solvers used in portfolio engines are **not designed to “balance” global and local behaviour** – they simply **do not need to**.  
For any problem that is kept convex (mean-variance, risk-parity, CVaR, volatility-budget, etc.) every local minimum is already the global one, so the algorithm cannot be trapped in a sub-optimal extremum.  Interior-point, ADMM or first-order solvers therefore put all of their effort into **shrinking the duality gap as fast as possible**; there is no “escape” phase.

The moment the model is made non-convex – e.g. by adding cardinality constraints, 3rd/4th-moment terms, VaR computed from discrete scenarios, or market-impact that is not diagonal – the guarantee disappears.  The codes that are still shipped under the label “convex” then switch to a **heuristic outer loop** (DCA, SCO, LMWU, B&B, …).  These loops do try to hop out of local minima, but they are no longer “convex solvers”; they are **global-optimisation heuristics** wrapped around convex sub-problems.  Their ability to reach the global solution is probabilistic or enumerative, and the price is a complexity that grows **exponentially with the number of non-convex degrees of freedom**, not with the raw dimension n.

High dimension (n ≈ 10³–10⁴) hurts **only when the convexity assumption is violated**.  In the pure convex case the duality gap is estimated in O(n³) (or O(n²) if the covariance matrix is factorised) and the iteration count of a primal-dual interior method is almost insensitive to n (20–80 iterations no matter how large n is).  Screening / safe-elimination rules can push the **per-iteration cost down to the number of active assets**, so the solver time grows sub-linearly in practice.

Hence:

- **Convex formulation** → no local-minima issue, duality-gap estimation is cheap and dimension-friendly.  
- **Non-convex features** → you are no longer using “convex optimisation”; you are using a meta-heuristic whose worst-case complexity explodes with the number of combinatorial or DC components, not with the portfolio size itself.

So the duality-gap machinery does **not** amplify complexity in high-dimensional allocation **as long as the problem remains convex**; it is the abandonment of convexity that creates both the local-extrema problem and the exponential blow-up.

## Annotations


## Sources
