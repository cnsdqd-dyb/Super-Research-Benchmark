# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 1cb26d50 | **Time:** 312.49s | **Cost:** $1.25125
--------------------------------------------------------------------------------

# Institutional Portfolio Rebalancing: Balancing Tracking Error and Execution Friction in Mean-Variance Frameworks

**Key Points**
*   **The Conflict:** Standard Mean-Variance Optimization (MVO) inherently amplifies execution friction because it assumes infinite liquidity and zero transaction costs. Without modification, MVO interprets small, noise-driven deviations in expected returns as arbitrage opportunities, leading to excessive turnover and high market impact costs.
*   **The Solution (No-Trade Regions):** Institutional algorithms successfully balance tracking error and cost by establishing "no-trade regions" or "buffer zones." Optimal policy dictates trading only when the portfolio drifts to the boundary of this region, rather than continuously rebalancing to the theoretical center.
*   **Market Impact Modeling:** Modern algorithms replace linear cost assumptions with quadratic or square-root market impact models. This penalizes large trades disproportionately, forcing the optimizer to "smooth" trading over time, thereby converting the optimization problem from a static allocation decision into a dynamic execution trajectory.
*   **Integrated Approaches:** Recent advancements, such as Integrated Prediction and Multi-period Optimization (IPMO), merge alpha signal generation with execution logic. This prevents the "optimizer's curse" where the theoretical alpha of a rebalance is negated by the realized cost of execution.

### Introduction
The management of institutional portfolios represents a continuous optimization problem constrained by two opposing forces: the imperative to minimize tracking error (TE) against a benchmark or strategic asset allocation, and the necessity to control transaction costs (TC). While Mean-Variance Optimization (MVO) serves as the theoretical bedrock for portfolio construction, its application in practice is fraught with challenges regarding execution friction. The central question facing quantitative finance is whether algorithmic rebalancing can effectively navigate the trade-off between TE and TC, or if the mathematical properties of MVO inevitably exacerbate market impact costs.

Research indicates that naive MVO amplifies execution friction by treating all deviations from the optimal weight as requiring correction, regardless of the cost-benefit analysis [cite: 1, 2]. However, sophisticated institutional algorithms mitigate this by incorporating transaction cost penalty terms directly into the objective function, effectively creating "no-trade regions" where inaction is the optimal policy [cite: 3]. Furthermore, the integration of market impact models—specifically those accounting for the non-linear, concave nature of price impact—allows algorithms to smooth trades over time, balancing the decay of alpha against the cost of liquidity consumption [cite: 4, 5].

## 1. The Theoretical Conflict: MVO and Execution Friction

### 1.1 The Markowitz Optimization Enigma
Harry Markowitz’s Modern Portfolio Theory (MPT) provides the mathematical framework for maximizing expected return for a given level of risk. However, the standard MVO model relies on the assumption of a frictionless market where assets can be traded instantaneously and without cost [cite: 1, 6]. In reality, institutional investors face significant transaction costs, which include explicit fees (commissions, taxes) and implicit costs (bid-ask spreads, market impact) [cite: 7, 8].

When applied blindly, MVO tends to amplify execution friction due to "error maximization." The optimizer acts as a "magnifying glass" for estimation errors in the covariance matrix and expected return vector. It frequently identifies assets with marginally higher estimated returns or lower estimated variances as superior, allocating aggressive weights to them [cite: 1, 9]. Since these marginal differences are often noise rather than signal, the optimizer demands high turnover to chase phantom efficiencies. In the presence of transaction costs, this "churning" destroys value, as the cost of executing the rebalance often exceeds the theoretical utility gain from the new weights [cite: 2, 10].

### 1.2 Market Impact as a Feedback Loop
For institutional investors, the primary component of transaction cost is not the commission, but the **market impact**—the adverse price movement induced by the trade itself. Market impact creates a feedback loop that standard MVO ignores: the act of rebalancing to capture alpha degrades the alpha it seeks to capture [cite: 11, 12].

If an algorithm attempts to rebalance a large portfolio instantly to minimize tracking error, it consumes available liquidity, pushing prices away from the decision price (slippage). This results in a "liquidity spiral" where the realized portfolio weights differ from the target weights immediately after execution due to the price shift, potentially triggering further rebalancing signals [cite: 4, 13].

## 2. Modeling Execution Friction: From Linear to Quadratic Costs

To balance tracking error and cost, algorithms must mathematically represent friction within the optimization problem. The complexity of this representation determines the algorithm's efficacy.

### 2.1 Linear vs. Quadratic Transaction Costs
The simplest cost models assume proportional (linear) transaction costs, where the cost is a fixed percentage of the traded value (e.g., bid-ask spread). However, institutional trading data suggests that market impact is non-linear.
*   **Linear Costs:** Modeled as $\sum c_i |w_{new} - w_{old}|$. This leads to a convex optimization problem but fails to capture the liquidity constraints of large orders [cite: 7, 14].
*   **Quadratic Costs:** Market impact is often modeled as quadratic in trade size (or square-root in price change, leading to power-law costs). Introducing quadratic transaction costs makes the optimization problem significantly more difficult because the budget constraint becomes non-linear [cite: 14, 15].

### 2.2 The Square-Root Law of Market Impact
Empirical microstructure research, such as the "square-root law," suggests that the price impact ($\Delta P$) of a trade of size $Q$ scales with the square root of the volume:
\[ \Delta P \propto \sigma \sqrt{\frac{Q}{V}} \]
where $\sigma$ is volatility and $V$ is daily volume [cite: 16, 17].
This implies that the cost per unit traded increases with trade size. Consequently, a rebalancing algorithm that ignores this concavity will underestimate the cost of large rebalances. Advanced algorithms approximate this using power-law functions with exponents between 1 and 2 (often 1.5 for the total cost of the trade) [cite: 5, 16, 18].

### 2.3 Quadratic Programming and Budget Constraints
When quadratic transaction costs are introduced, the standard Quadratic Programming (QP) solvers used for MVO face a "budget constraint" issue. The total wealth available for investment after rebalancing is endogenous; it depends on the transaction costs incurred by the rebalancing itself. This circular dependency (wealth depends on costs, costs depend on trades, trades depend on target weights, target weights depend on wealth) turns the problem into a Quadratically Constrained Quadratic Program (QCQP), which is NP-hard [cite: 14, 15].
To solve this, algorithms often use iterative approximations or Alternating Direction Method of Multipliers (ADMM) to decouple the weight optimization from the cost estimation [cite: 14, 19].

## 3. The Solution: No-Trade Regions and Buffer Zones

The most effective mechanism for balancing tracking error and cost is the implementation of **no-trade regions** (NTR).

### 3.1 Optimality of Inaction
Research consistently proves that in the presence of transaction costs, the optimal strategy is not to rebalance to the "ideal" Markowitz portfolio ($w^*$) continuously. Instead, there exists a region around $w^*$ where the utility loss from being sub-optimal (tracking error) is less than the cost of trading to correct it [cite: 3].
*   **Inside the Region:** If the current portfolio $w_0$ lies within the NTR, the optimal trade is zero.
*   **Outside the Region:** If $w_0$ drifts outside, the optimal trade is to rebalance to the *boundary* of the NTR, not all the way to $w^*$. Trading to the center incurs marginal costs that exceed marginal benefits [cite: 3, 18, 20].

### 3.2 Determinants of the No-Trade Region
The width of the no-trade band is dynamic and depends on:
1.  **Transaction Costs:** Higher costs widen the band [cite: 3].
2.  **Risk Aversion:** Higher risk aversion narrows the band (investors are less tolerant of tracking error) [cite: 18].
3.  **Volatility/Correlation:** Higher asset volatility typically widens the band to prevent "whipsaw" trading (rebalancing on noise) [cite: 21, 22].
4.  **Market Impact:** With market impact costs, the NTR shrinks over the investment horizon. Unlike proportional costs where trading might stop completely, market impact costs often imply continuous but small trading to "smooth" the execution [cite: 18].

### 3.3 Institutional Implementation: Drift-Based Rules
In practice, institutions implement NTRs via drift-based rebalancing rules rather than calendar-based rules.
*   **Calendar Rebalancing:** Rebalancing monthly or quarterly regardless of drift. This is inefficient; it trades when unnecessary (incurring costs) and fails to trade when risk spikes (incurring TE) [cite: 23, 24].
*   **Drift/Threshold Rebalancing:** Rebalancing only when asset weights deviate by a fixed percentage (e.g., $\pm 5\%$) from targets. This approximates the theoretical NTR and has been shown to improve Information Ratios by reducing unnecessary turnover [cite: 22, 24, 25].

## 4. Algorithmic Smoothing and Penalty Functions

To prevent MVO from amplifying friction, algorithms modify the objective function to explicitly penalize turnover.

### 4.1 The Penalized Objective Function
The standard MVO objective function is:
\[ \max_w \mu^T w - \lambda w^T \Sigma w \]
To control friction, algorithms add a penalty term:
\[ \max_w \mu^T w - \lambda w^T \Sigma w - \text{Cost}(w - w_{old}) \]
*   **L1 Penalty (Lasso-like):** $\kappa \sum |w_i - w_{old,i}|$. This corresponds to proportional costs (bid-ask spread). It induces sparsity in trading, effectively creating a no-trade region where small alpha signals are ignored [cite: 7, 18].
*   **L2 Penalty (Ridge-like):** $\kappa \sum (w_i - w_{old,i})^2$. This corresponds to quadratic market impact. It discourages large, instantaneous trades and encourages breaking trades into smaller pieces over time [cite: 14, 26, 27].

### 4.2 Smoothing Trades
The inclusion of quadratic penalties leads to "smoothing." Instead of a binary decision (hold or rebalance fully), the algorithm dictates a partial adjustment. This aligns with the optimal execution literature (e.g., Almgren-Chriss), where large orders are split to minimize market impact [cite: 4, 28].
By penalizing the *change* in weights, the algorithm effectively regularizes the covariance matrix, shrinking the solution towards the current portfolio. This dampens the sensitivity of MVO to estimation errors, reducing the "amplification" of friction [cite: 26, 27].

### 4.3 Turnover Constraints
An alternative to penalty terms is adding explicit constraints, such as "Turnover $\le$ 20% per month." This forces the optimizer to budget its "trading allowance" for the highest-conviction trades, implicitly balancing TE minimization (using the allowed turnover to fix the worst drifts) with cost control (stopping once the limit is reached) [cite: 7, 29].

## 5. Integrated Prediction and Multi-Period Optimization (IPMO)

The most advanced solution to the MVO-friction conflict is the move from single-period optimization to multi-period, integrated frameworks.

### 5.1 The Flaw of Two-Stage Models
Traditional approaches use a two-stage process:
1.  **Prediction:** Machine learning models predict returns ($\mu$) and covariance ($\Sigma$).
2.  **Optimization:** MVO solves for weights based on these predictions.
This separation is problematic because the predictor does not "know" about the transaction costs. It might predict a small positive return that the optimizer chases, only to have the profit wiped out by the cost of the trade. The prediction error and optimization error compound [cite: 30, 31].

### 5.2 IPMO Frameworks
Integrated Prediction and Multi-period Optimization (IPMO) embeds the optimization layer *inside* the learning loop (end-to-end learning). The model learns to predict returns that result in good *net-of-cost* portfolio performance.
*   **Differentiable Optimization:** The optimization layer is made differentiable, allowing the neural network to update its weights based on the final realized utility (after costs) rather than just forecast accuracy [cite: 31, 32].
*   **Path Dependence:** IPMO accounts for the fact that a trade today affects the portfolio composition (and thus rebalancing needs) tomorrow. It optimizes a trajectory of trades rather than a single snapshot [cite: 30, 33].

### 5.3 Empirical Superiority
Studies show that IPMO frameworks consistently outperform two-stage MVO benchmarks. By "seeing" the transaction costs during the training phase, IPMO learns to ignore volatile, high-cost signals that standard MVO would aggressively trade. It naturally learns a "no-trade" behavior without needing hard-coded thresholds [cite: 31, 33, 34].

## 6. Tracking Error Rebalancing vs. Transaction Costs

### 6.1 The Trade-off Frontier
There is a convex frontier between Tracking Error and Transaction Costs.
*   **Zero TE:** Requires continuous rebalancing, incurring maximum costs.
*   **Zero Cost:** Requires never trading, leading to maximum TE drift (as asset betas change and weights drift) [cite: 35, 36].

### 6.2 Tracking Error Rebalancing (TER)
Instead of rebalancing to fix asset weights (e.g., "Sell Apple because it's 5% overweight"), institutional algorithms often use **Tracking Error Rebalancing**. The algorithm monitors the *predicted tracking error* of the current portfolio against the benchmark.
*   **Trigger:** Rebalance only when predicted TE exceeds a threshold (e.g., 50 bps).
*   **Action:** Execute the basket of trades that reduces TE below the threshold at the *minimum possible cost*. This often involves trading liquid proxies or derivatives (futures) rather than the illiquid underlying assets, significantly reducing friction [cite: 25, 35].

### 6.3 Synthetic Rebalancing
To further decouple TE from cost, institutions use "synthetic rebalancing" (overlay strategies). If the equity allocation drifts high, instead of selling physical stocks (high impact, tax consequences), the manager sells equity futures. This reduces the beta exposure (minimizing TE) with a fraction of the transaction cost of physical trading [cite: 3, 35].

## 7. Conclusion

Institutional portfolio rebalancing algorithms *can* balance tracking error minimization with cost control, but only if they abandon the naive assumptions of standard Mean-Variance Optimization.

**Does MVO amplify friction?**
Yes. In its raw form, MVO amplifies friction by treating liquidity as infinite and estimation errors as actionable signals. It lacks a mechanism to distinguish between a profitable arbitrage and a costly, noise-induced trade [cite: 1, 2].

**How is balance achieved?**
Balance is achieved through three layers of algorithmic sophistication:
1.  **Structural Constraints:** Implementing **no-trade regions** and drift bands that prevent trading on small deviations [cite: 3, 22].
2.  **Cost-Aware Objectives:** Incorporating **quadratic penalty terms** that model market impact, forcing the optimizer to smooth trades and account for the "square-root law" of liquidity [cite: 5, 16, 27].
3.  **Integrated Architectures:** Utilizing **IPMO** frameworks that jointly optimize prediction and execution, ensuring that the alpha sought is robust to the friction incurred [cite: 30, 31].

Ultimately, the "optimal" portfolio is not the one with the highest theoretical Sharpe ratio, but the one that maximizes the *net* information ratio after accounting for the path-dependent reality of market impact.

## References Table

| Source ID | Description | Key Insight |
| :--- | :--- | :--- |
| [cite: 7] | Quant StackExchange (2016) | Explains linear vs. quadratic cost constraints in MVO. |
| [cite: 3] | Dybvig et al. (2019) | Defines the "no-trade region" and optimal rebalancing to boundaries. |
| [cite: 1] | Diva Portal (2023) | Discusses "Markowitz optimization enigma" and sensitivity to errors. |
| [cite: 14] | Roncalli et al. (2020) | Quadratic costs make MVO non-linear; budget constraint issues. |
| [cite: 35] | Tracking Error Rebalancing | TE vs. Cost trade-off; synthetic rebalancing reduces costs. |
| [cite: 16] | Mosek Portfolio Cookbook | Models market impact using power cones (square-root law). |
| [cite: 25] | MIT Paper (2006) | Compares calendar vs. tolerance band rebalancing; dynamic programming. |
| [cite: 30] | Arxiv (2025) | Introduces IPMO: Integrated Prediction and Multi-period Optimization. |
| [cite: 4] | Arxiv (2017) | Market impact of correlated instruments; synchronizing execution. |
| [cite: 3] | Dybvig & Pezzo (2019) | Detailed analysis of non-trading regions with variable/fixed costs. |
| [cite: 5] | Arxiv (2026) | Square-root laws of market impact and endogenous market resistance. |
| [cite: 31] | Arxiv (2025) | IPMO outperforms two-stage MVO by accounting for turnover penalties. |
| [cite: 27] | Lancaster Univ (2020) | Quadratic transaction cost penalties act as covariance smoothing/regularization. |

**Sources:**
1. [diva-portal.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESUzNYLRtGbAzxSD2stNPCp7ZmHNf0a23wtt2WBq6nne0qPrxQS45UsLbgk5ziGkJWOnQGIXIdIMIvfJEN5FAUuQww54dknDtSNJ4CAsT_iNiHCqNln90aYq5-Oo1T3n5CUT0aBigwK5SHaXKYlgn7FFvMSYG4Yw==)
2. [stackexchange.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIiP_6pBv-LzOuBbjaERzfUzxPBJJDmuxj_DkjDz3jKqFIUgpxRMwXr-VZudRgz0-NXwI0QIm4efZtJrYPPUTi_FKZOEX6_kEIYqg4CbgeATgR3XB4KSDTV4pPkGvvKPWFOnh0vSTWAc1ZtUexvPnAGaO28DQDuDJqg217FtqQOWK8akCnY_a_JofJvVXvdIUeH0_0qSbO4cIouvsFniF5JA_br7hMDIqKeZpbSVDNGdOvgA==)
3. [wustl.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbuv0srXEeU9zGAVEGJLODgHTzvLXs9fd2fHNA7oNxA_eTLb9_3B6n5BRbpKdw1jVvpR7JrAvhpdZ2d6g67ZL83Y0rnJYpvrfjiCd9eq5KPLTOjqGgZuCwn9G8nyQfGf-5wvD0-vYNDKgH39dS)
4. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkDjA3pgpJKKbOL_eJIOahJLk4ZQ88v_Ah4bjFG61etVjylJWXwxaF4qSLnj41mgxGmuUfqsqEtFn23wMiUnTZmZibsK6HBQPMxvhRJEh9d9r-5JKj)
5. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_Coa79Glk7mK4mhFeF3odjpZM53Sxmas3jV6xrvKbM6fhDGu1E5MO_kLpB3ubvHOJClIKXewXvFebKtYYot9Yz9TESxbXfSDEk9i4GxDkHxTeObpS)
6. [smartasset.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbEs0rX8kBZLGvf6S0_moGg3MntaBmYqY9a-0kRLSvW8GYWs9Po2xAZwEU80-xY38JL4S2u-NjARU0f-9xuHsnpAVwCSVSqvNWvDKBcOXKGlfL3sB9KiiegTuKRoFRH0kggIo3QsqrtM2nuCxiTb2O2p75VdNUq-M=)
7. [stackexchange.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkz_5VlQKVwi-Cs31lFyaobc2wKZIeDeMkzlhG3y8S0sWcNLFOnkkp0N3NEeWrnOsObydLA3IfXnRjdRdkmtS7ib0OnmDQxpV3gbvfBspZuI66LZVx8TUXDqktWQk4DzfoMR3zFFfa5udreFt2dgBx6CiphhGzXSoed5zyZk_xH142g0dKvrIL8icrDlvN5bdmpXnAtrAFRA==)
8. [analystprep.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcDMbbwMsV3Q6yReKWqbgNl79eEisEeNyJ8z77JC8si20-H17Wy4IcBmrg7kONypGm1xbWIqDPj_6XcQQgnnr2jOBLhLQ1o7nXM8GeHNVmNxZxPEOQY9NPTCO7UbQSwXIGZvPlDHUs-myOjSjw)
9. [diva-portal.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJR1Wr0CcQLc69maZxqhstr3BuWhFkURLf-E3Pz6EyMbWpNqIUhSYzoP49Yx_uB5fMDtzc3UauUOHhjo1ysZ5u58BFHDpRpN2sw2LgU-Sp2EMrWmXOHoT09KP_j8TO45V-yaSHkf5SV0hSpYPIF8YfoyS2PDcnhQ==)
10. [lu.se](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8JERI9Gj-UWxTpr00XXTnBFH51bqUEGbTlzBV5meX90ycNGD-_B0V2uDYkwiRTyBK4gz_lod7kIzy2HUHBE2vaM0myNuXMnN7joS3_Tqx5d-5Q609LydZwNgP4gfkViK_8RTFXgXEHW7nRVAJRN3WESi-S4usWZ33)
11. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL-4_OZCj2aBs5P67rD35IkOJVzfQ1IThHiIxhJbjPIAlUfy5pDaCOgooP5l6gYRbvKgju9_vqDh9bAmW9kJ4_cx1L-D7CUZEx0soAuP2xFlSp5CTtkwv4n9VBs2jubb4IIoNsnsoBgGGHCA4FRyKnWMZp2DqH)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5l4WukQ3U5_nq4W3AfPx3tRm-PnTft0RQvLwBLAL6pcqo7wJgVJ6SLrVLmjD1WHeX6CwoEgaRxu9SkUrJgegML81ybjwpU4ew4a1SFRXp67g7qMBVLfQ-K71aJt9w8a8ujl36DjVJ8Wk173ryiPPzP_MYydHzMKcqxIqdYC2xCs4aHcD8KOY9JujQWJGPfrqUYd5K1S02XE-yhAWzLEErojY8yzuweX6O)
13. [columbia.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwYu-77UIaSrExhDShBvDuDXqIV1H6qRrKpNaRqEYEA2ICSZsTRklQuKeRtC3hxme2hHefhfwfZb44ZRRD5pYHem6VNfxeSgemVjJjZZsSV5nX2fEaPLBI5FWkyE84tOGwphPJMhzuG3mWbQJz31XwR-noearW1Nsb)
14. [thierry-roncalli.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRwhn50kdKIc_LN-DRaTqTXxgl9IE5ZkLBpCFMukjtFTCrijCLug4X1eRKP-jwVzr1vwMGcDumXWdqiksj0yd3rrqWNBXXttMTgpJCX5JSC8HYP3C24f5QjnGN4hd80AulyG3-Sjc8Tv0f0CIUmOW6VfYMN4ShdwSYrTDBPg==)
15. [amundi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIOoSGGKqSJk5Bfz2bwC-qpw5_Gh1QoME4G58qnCsq_fJ8VgkUwq1NeHBomzGF4z8n2thvwD0x5f-83fB4_0Lh1xcGcoYNAmmKrJ6WZTZ-uQJOUA_LtvPg_1IuVCMaPNEsFYvEoHLDYhRLvLwkMzICGGsYBSI0-XOKRpNapUICWAW5vtQh8g40Vdx3DwLny0rUOu0=)
16. [mosek.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE61KTGAWLK73A-RvY3AqbMZYPlZW9_SErQ7Io7VQA0mB9sJ742B3Sa9Ci4haLocNZGYL8t-BTjmgStV-ln0lur44Eo4sbC3i7B2AME1g6WB6g7ouwSeS6dZPl_Gmy_qvtS0kQKF5JivuuQDna4r0o=)
17. [imperial.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFimFbe2JfZqY5r_jUDg93ON0EbHRvjDOB7dd4L0Tex3TfuPFphTP1SMkctN_-6lPL-hTrTxuEKlhNDOjmK_VTAOUIYbWEYxMYjdpEtMXPTpk2CnMUKqMXZqgkoXUvu_zoE4zRbv5qyNCCVrukFxwHbW3Ob74i0CfPX8_YZ0u2uIeOPAcOo1eXjX0cXSWuuAvl38TuuIsR6DR10lduvjQhGQmjdqCSHAl4nRc3KRQ7rUXhiHb6EtuC2U7fwp1jd9n0Guui9IQius2_D-Cqc6GGpaSo2eHQ=)
18. [optimization-online.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc-R2vUrHT3NPOb-GJjRItcnXGIIgIlz8cVwFM6e_cUUXCurF7RkY_cPk2lzKRWj0oxV3t0dEjUZn67PftQuyPSzpEFaxJ_X_RKYaes8zaRVd5AQE8yJP1Sil6jCjUStcDncFgDANDGPH6-HCOWrQ_-tZSs84Akl0=)
19. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjJCunLeHyn-Iu1jwhOjHy2SQwIq_7xaSYo0K4OqesyHL0iSg_dgBQO0gKEoKEPxnoC5Dtj5CqaFO4BHS8MUWKeSq3F9yVlB1yl75VOOg_CCqLAmES)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfonH-mSI7BInhrbm6wiChKeXbf4JOlCiSa4vg0yze8H0SeZGmn7L-pZgSIYVXSHbIvTEfaQAEUWtX8auk0n-qwQA562bttdg9F8xn8qWfzBfvxIe-y5YnKlW0wRS5iaIS5WSx0iKDt-8tTZ4h4wAkGoejTe8n1WSFr8VqU1nBdl430fVhbOJxBX4RRu8zA3FuK7-iiMgTqyV6eXVop1-0)
21. [pm-research.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8RnpyZbVL6qlOQRlCUXyPsjTVO8A7cHqGYE4qYhVgtaHrM_kkxFyYrBcKEwiH3FMC7PhcyrbKAox2xM6qnS29fu9ECGXfGa0RKW1Ca8RfOgiJvgeKkam68L7bnPgIAfmSGxrIYr_jVPWSew==)
22. [nbim.no](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_MZjPEa-A7TqUdb_MRQMdxOOJ9_JpjUUs2HAw_tdQwGHPSskoT1Vgx9YMyvgEw_k35WaUp2_1GpLPDcF7mBwDpiy0mQXbvbDCNhwA8cW_-1Oivbj-m1LUl5VdQAD9iX9RVAQ70PTaBkXKdEmEzY6M4QyYW3zSrVhCYLsuz0mLoRX1i4itV1YA21pccnW_UNPi7Nk-VfMkVzw8qXgpiqux_Bt2xYJ_I7zZa7TR33BEozVs_5k0fWp_Rf1xQkin8bAMYpM=)
23. [investopedia.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHa1iOmqH-zpxOfRfMoazR9dIyUTd3YzrF06CamlojRG6UNYZm6w0jrZge2UHOLbcvOBb3qflKvJBE6VdbuI6wJnbbDMS0xGRRUSy46dPdvg2k41AZB4RdW82GhnWrlxvaD2jXPP_maqiymRJmMi7a_viaToR3g2dw95ZwJR6Jw)
24. [morganstanley.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFa_05tgOYgLwkPDphQVbqbnTqVkqepO7w1AYh1fXZTGz0fsT_z-eUTlw5S9OXqoD-Zw3fRshQti9IPN99G2DmSVyTeNgd7x9agRVxmE-zqE8d8HKUKu_g7HzOZPT4YqyDVBUWHIiDiF0nrITnQ4yZnpN4kiznBm_PRgKAsUophejXQJzjspKAvm9k7TJDV6fotSysLk7xzRAPOT8LAHvrpISiSui3_WUESg9CxzJtNx-64HZGPuw==)
25. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMQQA-IWdO1dpDL8n4OLFqtoo9M9gsyuw1FqSdmtwFsrEVffkKSyuQExFt7dfz78crl-QRzkbzXKRjZwmvBdLtrcmUPQ4PEGya2QnVNBEhgE0NaBdzt_a_HIE36_8wVv_nZsBVwshDnwB_vkqWrbbHe6rUP7SJX4OjwyeBa7MK)
26. [kth.se](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFD32tROahv_1OOCvEalDtxeeqTCCLbJUwWNbqMWb07cGPMXifbFurxYt4Ya17kIPZipOgxXyeIVxmuJV8MFrYubE-Ih3Gr07Fl3fRccCTG8YbWUv5CtdgwX0BiXLrmimztnljauO9jbqSMbiYf-zs5DcrBTtMpatwh0nFXSg==)
27. [lancs.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzu5_sZfTm8fGizEJRNFWgWK7fs3-LwGnnSd7wqc8r5Ra39bSU0qNvdqIOhc6jvOWnoR9tZlL6J3jg5n3zER3skXGU39lvXtYVpM6w-Rum_fWkd3JimDLfEHZSRzw37rle5w3bNPiGG8nAY1DF9R_cBvhoL8r95PfriiFN8CQOog==)
28. [applied-financial-mathematics.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4ESaDD253iP3KVzhD40FBeaSg0eZ9iC9Ec7DMm6BD3FnCCO0xUWtFEp2TQeinCZx_W-fVXTfAqKWA0WSjh2gnMYaAb-tlkpJNmuFC8GcsR2XfojQOEVSBK_peZbnFCCVwfUNJm1yRw7QjVtadPbqpPE2Z4GTj-k8ORKh6a1iMVmU1-VzpQsgchtdJicsll4s2bWxi2iCkVYpCw9-qBNATWzkUPz9BFeaAGxvNfXiP1zkcafcFm4v6kHIIG1T6J3H6nevLYIJy1Gz9iO8=)
29. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdgpEqv743clJG4K0Gdi0Gb6KijWWuBfEdXz7rKf2sJGe7IZfJ8HedXytWtcp0IMb48kh4YaGhggvjy424vnWSV6InznfpYgxGayvZD8NIDoIvEvFFGU2N-ek=)
30. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOn3rpWUuGk1VyZVxVSCdl_VWRjGxBrmke4azBR1qsq3hNp_9hisGb4G7HWQK4KHWzPj493MgQUXMclf5niTMe8E-dJKmLh9zCe0ZLcsD1IFvbo9DM)
31. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1_aoJToZ0JqVEEoDLZlBkSnEl6IWfROIZTnSnBJukyjBfCKpDyFcBLCMlogEULNgk7dYw73AXnooXzetCJnUNmzv67MhbiXhMXfYRxk1fZOB1XQ-2rky3)
32. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhak0D4Qf0YRlV2mE58r-XMCsPnZv-7QYdN4RV9c9s2gzfyV_U5OcvpsivlcHRXaLHZ0Iug_7HIlJIdxf7C1QuVlefmBueRfEsH1aztQlwV45bozxqJM-8)
33. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2CkANG2oZr3LQmFLw-8TFPL2m3vJaxFa1qGQ9swttLqL0UCc8hFij9w4Jd7rjvUzfHn1sfQffxyrp5qKsmTZpv1X-s0cRqZROdB0b8EU8niUn_q6p)
34. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBF2UTEuGSWs8m2tZzk_VJmPuclEL9IpiUyf3Jn_Cf0JvFI9G3GtiAr9Vb-yHQQhzck6IveCOgOQlJCuH0iuTQpnS9ztfmETw2n9X0zy8vIajUMQySvExThoUHXTdNGnDq9UYhGMK5q84EiWpu5FnycV1SzA_q7SLu5jqSNukct_9O)
35. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzZWvrwp7mApkk_C6i57rfa9L1TaJPRdxTvpAyPf9B5blk8NC_CDFMhAlNEecakX6QAfeSSUsqE6kNCWFF4zCnrSazJ2x3oLawbeSCjBtWU8LqjmARZzzUg0AOHdqEG1-dNUf6_sRwS1HGreDut8xTbZg7v7ziSg8Tri1fdBw6atif)
36. [investopedia.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFONvmMOl7A6eznmvE3AoLPcbII3imWkBB2ZnxmL75bih0L6EBGsdIoBjxkJHa0Y15XKA_2x1QMtzVD9x2rOJ7YD9ejql0Ht-J3jzT0MNLT-UmOnaaMWLF9xCDAXLj3wIAYRW0h8qTE2_qKaQ==)


## Annotations
Annotation(end_index=2347, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIiP_6pBv-LzOuBbjaERzfUzxPBJJDmuxj_DkjDz3jKqFIUgpxRMwXr-VZudRgz0-NXwI0QIm4efZtJrYPPUTi_FKZOEX6_kEIYqg4CbgeATgR3XB4KSDTV4pPkGvvKPWFOnh0vSTWAc1ZtUexvPnAGaO28DQDuDJqg217FtqQOWK8akCnY_a_JofJvVXvdIUeH0_0qSbO4cIouvsFniF5JA_br7hMDIqKeZpbSVDNGdOvgA==', start_index=2335)
Annotation(end_index=2347, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESUzNYLRtGbAzxSD2stNPCp7ZmHNf0a23wtt2WBq6nne0qPrxQS45UsLbgk5ziGkJWOnQGIXIdIMIvfJEN5FAUuQww54dknDtSNJ4CAsT_iNiHCqNln90aYq5-Oo1T3n5CUT0aBigwK5SHaXKYlgn7FFvMSYG4Yw==', start_index=2335)
Annotation(end_index=2583, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbuv0srXEeU9zGAVEGJLODgHTzvLXs9fd2fHNA7oNxA_eTLb9_3B6n5BRbpKdw1jVvpR7JrAvhpdZ2d6g67ZL83Y0rnJYpvrfjiCd9eq5KPLTOjqGgZuCwn9G8nyQfGf-5wvD0-vYNDKgH39dS', start_index=2574)
Annotation(end_index=2852, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkDjA3pgpJKKbOL_eJIOahJLk4ZQ88v_Ah4bjFG61etVjylJWXwxaF4qSLnj41mgxGmuUfqsqEtFn23wMiUnTZmZibsK6HBQPMxvhRJEh9d9r-5JKj', start_index=2840)
Annotation(end_index=2852, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_Coa79Glk7mK4mhFeF3odjpZM53Sxmas3jV6xrvKbM6fhDGu1E5MO_kLpB3ubvHOJClIKXewXvFebKtYYot9Yz9TESxbXfSDEk9i4GxDkHxTeObpS', start_index=2840)
Annotation(end_index=3255, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESUzNYLRtGbAzxSD2stNPCp7ZmHNf0a23wtt2WBq6nne0qPrxQS45UsLbgk5ziGkJWOnQGIXIdIMIvfJEN5FAUuQww54dknDtSNJ4CAsT_iNiHCqNln90aYq5-Oo1T3n5CUT0aBigwK5SHaXKYlgn7FFvMSYG4Yw==', start_index=3243)
Annotation(end_index=3255, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbEs0rX8kBZLGvf6S0_moGg3MntaBmYqY9a-0kRLSvW8GYWs9Po2xAZwEU80-xY38JL4S2u-NjARU0f-9xuHsnpAVwCSVSqvNWvDKBcOXKGlfL3sB9KiiegTuKRoFRH0kggIo3QsqrtM2nuCxiTb2O2p75VdNUq-M=', start_index=3243)
Annotation(end_index=3442, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcDMbbwMsV3Q6yReKWqbgNl79eEisEeNyJ8z77JC8si20-H17Wy4IcBmrg7kONypGm1xbWIqDPj_6XcQQgnnr2jOBLhLQ1o7nXM8GeHNVmNxZxPEOQY9NPTCO7UbQSwXIGZvPlDHUs-myOjSjw', start_index=3430)
Annotation(end_index=3442, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkz_5VlQKVwi-Cs31lFyaobc2wKZIeDeMkzlhG3y8S0sWcNLFOnkkp0N3NEeWrnOsObydLA3IfXnRjdRdkmtS7ib0OnmDQxpV3gbvfBspZuI66LZVx8TUXDqktWQk4DzfoMR3zFFfa5udreFt2dgBx6CiphhGzXSoed5zyZk_xH142g0dKvrIL8icrDlvN5bdmpXnAtrAFRA==', start_index=3430)
Annotation(end_index=3819, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESUzNYLRtGbAzxSD2stNPCp7ZmHNf0a23wtt2WBq6nne0qPrxQS45UsLbgk5ziGkJWOnQGIXIdIMIvfJEN5FAUuQww54dknDtSNJ4CAsT_iNiHCqNln90aYq5-Oo1T3n5CUT0aBigwK5SHaXKYlgn7FFvMSYG4Yw==', start_index=3807)
Annotation(end_index=3819, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJR1Wr0CcQLc69maZxqhstr3BuWhFkURLf-E3Pz6EyMbWpNqIUhSYzoP49Yx_uB5fMDtzc3UauUOHhjo1ysZ5u58BFHDpRpN2sw2LgU-Sp2EMrWmXOHoT09KP_j8TO45V-yaSHkf5SV0hSpYPIF8YfoyS2PDcnhQ==', start_index=3807)
Annotation(end_index=4143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIiP_6pBv-LzOuBbjaERzfUzxPBJJDmuxj_DkjDz3jKqFIUgpxRMwXr-VZudRgz0-NXwI0QIm4efZtJrYPPUTi_FKZOEX6_kEIYqg4CbgeATgR3XB4KSDTV4pPkGvvKPWFOnh0vSTWAc1ZtUexvPnAGaO28DQDuDJqg217FtqQOWK8akCnY_a_JofJvVXvdIUeH0_0qSbO4cIouvsFniF5JA_br7hMDIqKeZpbSVDNGdOvgA==', start_index=4130)
Annotation(end_index=4143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8JERI9Gj-UWxTpr00XXTnBFH51bqUEGbTlzBV5meX90ycNGD-_B0V2uDYkwiRTyBK4gz_lod7kIzy2HUHBE2vaM0myNuXMnN7joS3_Tqx5d-5Q609LydZwNgP4gfkViK_8RTFXgXEHW7nRVAJRN3WESi-S4usWZ33', start_index=4130)
Annotation(end_index=4523, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5l4WukQ3U5_nq4W3AfPx3tRm-PnTft0RQvLwBLAL6pcqo7wJgVJ6SLrVLmjD1WHeX6CwoEgaRxu9SkUrJgegML81ybjwpU4ew4a1SFRXp67g7qMBVLfQ-K71aJt9w8a8ujl36DjVJ8Wk173ryiPPzP_MYydHzMKcqxIqdYC2xCs4aHcD8KOY9JujQWJGPfrqUYd5K1S02XE-yhAWzLEErojY8yzuweX6O', start_index=4509)
Annotation(end_index=4523, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL-4_OZCj2aBs5P67rD35IkOJVzfQ1IThHiIxhJbjPIAlUfy5pDaCOgooP5l6gYRbvKgju9_vqDh9bAmW9kJ4_cx1L-D7CUZEx0soAuP2xFlSp5CTtkwv4n9VBs2jubb4IIoNsnsoBgGGHCA4FRyKnWMZp2DqH', start_index=4509)
Annotation(end_index=4930, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwYu-77UIaSrExhDShBvDuDXqIV1H6qRrKpNaRqEYEA2ICSZsTRklQuKeRtC3hxme2hHefhfwfZb44ZRRD5pYHem6VNfxeSgemVjJjZZsSV5nX2fEaPLBI5FWkyE84tOGwphPJMhzuG3mWbQJz31XwR-noearW1Nsb', start_index=4917)
Annotation(end_index=4930, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkDjA3pgpJKKbOL_eJIOahJLk4ZQ88v_Ah4bjFG61etVjylJWXwxaF4qSLnj41mgxGmuUfqsqEtFn23wMiUnTZmZibsK6HBQPMxvhRJEh9d9r-5JKj', start_index=4917)
Annotation(end_index=5660, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkz_5VlQKVwi-Cs31lFyaobc2wKZIeDeMkzlhG3y8S0sWcNLFOnkkp0N3NEeWrnOsObydLA3IfXnRjdRdkmtS7ib0OnmDQxpV3gbvfBspZuI66LZVx8TUXDqktWQk4DzfoMR3zFFfa5udreFt2dgBx6CiphhGzXSoed5zyZk_xH142g0dKvrIL8icrDlvN5bdmpXnAtrAFRA==', start_index=5647)
Annotation(end_index=5660, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRwhn50kdKIc_LN-DRaTqTXxgl9IE5ZkLBpCFMukjtFTCrijCLug4X1eRKP-jwVzr1vwMGcDumXWdqiksj0yd3rrqWNBXXttMTgpJCX5JSC8HYP3C24f5QjnGN4hd80AulyG3-Sjc8Tv0f0CIUmOW6VfYMN4ShdwSYrTDBPg==', start_index=5647)
Annotation(end_index=5970, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIOoSGGKqSJk5Bfz2bwC-qpw5_Gh1QoME4G58qnCsq_fJ8VgkUwq1NeHBomzGF4z8n2thvwD0x5f-83fB4_0Lh1xcGcoYNAmmKrJ6WZTZ-uQJOUA_LtvPg_1IuVCMaPNEsFYvEoHLDYhRLvLwkMzICGGsYBSI0-XOKRpNapUICWAW5vtQh8g40Vdx3DwLny0rUOu0=', start_index=5956)
Annotation(end_index=5970, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRwhn50kdKIc_LN-DRaTqTXxgl9IE5ZkLBpCFMukjtFTCrijCLug4X1eRKP-jwVzr1vwMGcDumXWdqiksj0yd3rrqWNBXXttMTgpJCX5JSC8HYP3C24f5QjnGN4hd80AulyG3-Sjc8Tv0f0CIUmOW6VfYMN4ShdwSYrTDBPg==', start_index=5956)
Annotation(end_index=6310, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE61KTGAWLK73A-RvY3AqbMZYPlZW9_SErQ7Io7VQA0mB9sJ742B3Sa9Ci4haLocNZGYL8t-BTjmgStV-ln0lur44Eo4sbC3i7B2AME1g6WB6g7ouwSeS6dZPl_Gmy_qvtS0kQKF5JivuuQDna4r0o=', start_index=6296)
Annotation(end_index=6310, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFimFbe2JfZqY5r_jUDg93ON0EbHRvjDOB7dd4L0Tex3TfuPFphTP1SMkctN_-6lPL-hTrTxuEKlhNDOjmK_VTAOUIYbWEYxMYjdpEtMXPTpk2CnMUKqMXZqgkoXUvu_zoE4zRbv5qyNCCVrukFxwHbW3Ob74i0CfPX8_YZ0u2uIeOPAcOo1eXjX0cXSWuuAvl38TuuIsR6DR10lduvjQhGQmjdqCSHAl4nRc3KRQ7rUXhiHb6EtuC2U7fwp1jd9n0Guui9IQius2_D-Cqc6GGpaSo2eHQ=', start_index=6296)
Annotation(end_index=6652, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE61KTGAWLK73A-RvY3AqbMZYPlZW9_SErQ7Io7VQA0mB9sJ742B3Sa9Ci4haLocNZGYL8t-BTjmgStV-ln0lur44Eo4sbC3i7B2AME1g6WB6g7ouwSeS6dZPl_Gmy_qvtS0kQKF5JivuuQDna4r0o=', start_index=6635)
Annotation(end_index=6652, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc-R2vUrHT3NPOb-GJjRItcnXGIIgIlz8cVwFM6e_cUUXCurF7RkY_cPk2lzKRWj0oxV3t0dEjUZn67PftQuyPSzpEFaxJ_X_RKYaes8zaRVd5AQE8yJP1Sil6jCjUStcDncFgDANDGPH6-HCOWrQ_-tZSs84Akl0=', start_index=6635)
Annotation(end_index=6652, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_Coa79Glk7mK4mhFeF3odjpZM53Sxmas3jV6xrvKbM6fhDGu1E5MO_kLpB3ubvHOJClIKXewXvFebKtYYot9Yz9TESxbXfSDEk9i4GxDkHxTeObpS', start_index=6635)
Annotation(end_index=7248, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIOoSGGKqSJk5Bfz2bwC-qpw5_Gh1QoME4G58qnCsq_fJ8VgkUwq1NeHBomzGF4z8n2thvwD0x5f-83fB4_0Lh1xcGcoYNAmmKrJ6WZTZ-uQJOUA_LtvPg_1IuVCMaPNEsFYvEoHLDYhRLvLwkMzICGGsYBSI0-XOKRpNapUICWAW5vtQh8g40Vdx3DwLny0rUOu0=', start_index=7234)
Annotation(end_index=7248, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRwhn50kdKIc_LN-DRaTqTXxgl9IE5ZkLBpCFMukjtFTCrijCLug4X1eRKP-jwVzr1vwMGcDumXWdqiksj0yd3rrqWNBXXttMTgpJCX5JSC8HYP3C24f5QjnGN4hd80AulyG3-Sjc8Tv0f0CIUmOW6VfYMN4ShdwSYrTDBPg==', start_index=7234)
Annotation(end_index=7440, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjJCunLeHyn-Iu1jwhOjHy2SQwIq_7xaSYo0K4OqesyHL0iSg_dgBQO0gKEoKEPxnoC5Dtj5CqaFO4BHS8MUWKeSq3F9yVlB1yl75VOOg_CCqLAmES', start_index=7426)
Annotation(end_index=7440, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRwhn50kdKIc_LN-DRaTqTXxgl9IE5ZkLBpCFMukjtFTCrijCLug4X1eRKP-jwVzr1vwMGcDumXWdqiksj0yd3rrqWNBXXttMTgpJCX5JSC8HYP3C24f5QjnGN4hd80AulyG3-Sjc8Tv0f0CIUmOW6VfYMN4ShdwSYrTDBPg==', start_index=7426)
Annotation(end_index=7983, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbuv0srXEeU9zGAVEGJLODgHTzvLXs9fd2fHNA7oNxA_eTLb9_3B6n5BRbpKdw1jVvpR7JrAvhpdZ2d6g67ZL83Y0rnJYpvrfjiCd9eq5KPLTOjqGgZuCwn9G8nyQfGf-5wvD0-vYNDKgH39dS', start_index=7974)
Annotation(end_index=8325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbuv0srXEeU9zGAVEGJLODgHTzvLXs9fd2fHNA7oNxA_eTLb9_3B6n5BRbpKdw1jVvpR7JrAvhpdZ2d6g67ZL83Y0rnJYpvrfjiCd9eq5KPLTOjqGgZuCwn9G8nyQfGf-5wvD0-vYNDKgH39dS', start_index=8308)
Annotation(end_index=8325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc-R2vUrHT3NPOb-GJjRItcnXGIIgIlz8cVwFM6e_cUUXCurF7RkY_cPk2lzKRWj0oxV3t0dEjUZn67PftQuyPSzpEFaxJ_X_RKYaes8zaRVd5AQE8yJP1Sil6jCjUStcDncFgDANDGPH6-HCOWrQ_-tZSs84Akl0=', start_index=8308)
Annotation(end_index=8325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfonH-mSI7BInhrbm6wiChKeXbf4JOlCiSa4vg0yze8H0SeZGmn7L-pZgSIYVXSHbIvTEfaQAEUWtX8auk0n-qwQA562bttdg9F8xn8qWfzBfvxIe-y5YnKlW0wRS5iaIS5WSx0iKDt-8tTZ4h4wAkGoejTe8n1WSFr8VqU1nBdl430fVhbOJxBX4RRu8zA3FuK7-iiMgTqyV6eXVop1-0', start_index=8308)
Annotation(end_index=8494, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbuv0srXEeU9zGAVEGJLODgHTzvLXs9fd2fHNA7oNxA_eTLb9_3B6n5BRbpKdw1jVvpR7JrAvhpdZ2d6g67ZL83Y0rnJYpvrfjiCd9eq5KPLTOjqGgZuCwn9G8nyQfGf-5wvD0-vYNDKgH39dS', start_index=8485)
Annotation(end_index=8615, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc-R2vUrHT3NPOb-GJjRItcnXGIIgIlz8cVwFM6e_cUUXCurF7RkY_cPk2lzKRWj0oxV3t0dEjUZn67PftQuyPSzpEFaxJ_X_RKYaes8zaRVd5AQE8yJP1Sil6jCjUStcDncFgDANDGPH6-HCOWrQ_-tZSs84Akl0=', start_index=8605)
Annotation(end_index=8765, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_MZjPEa-A7TqUdb_MRQMdxOOJ9_JpjUUs2HAw_tdQwGHPSskoT1Vgx9YMyvgEw_k35WaUp2_1GpLPDcF7mBwDpiy0mQXbvbDCNhwA8cW_-1Oivbj-m1LUl5VdQAD9iX9RVAQ70PTaBkXKdEmEzY6M4QyYW3zSrVhCYLsuz0mLoRX1i4itV1YA21pccnW_UNPi7Nk-VfMkVzw8qXgpiqux_Bt2xYJ_I7zZa7TR33BEozVs_5k0fWp_Rf1xQkin8bAMYpM=', start_index=8751)
Annotation(end_index=8765, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8RnpyZbVL6qlOQRlCUXyPsjTVO8A7cHqGYE4qYhVgtaHrM_kkxFyYrBcKEwiH3FMC7PhcyrbKAox2xM6qnS29fu9ECGXfGa0RKW1Ca8RfOgiJvgeKkam68L7bnPgIAfmSGxrIYr_jVPWSew==', start_index=8751)
Annotation(end_index=9021, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc-R2vUrHT3NPOb-GJjRItcnXGIIgIlz8cVwFM6e_cUUXCurF7RkY_cPk2lzKRWj0oxV3t0dEjUZn67PftQuyPSzpEFaxJ_X_RKYaes8zaRVd5AQE8yJP1Sil6jCjUStcDncFgDANDGPH6-HCOWrQ_-tZSs84Akl0=', start_index=9011)
Annotation(end_index=9404, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFa_05tgOYgLwkPDphQVbqbnTqVkqepO7w1AYh1fXZTGz0fsT_z-eUTlw5S9OXqoD-Zw3fRshQti9IPN99G2DmSVyTeNgd7x9agRVxmE-zqE8d8HKUKu_g7HzOZPT4YqyDVBUWHIiDiF0nrITnQ4yZnpN4kiznBm_PRgKAsUophejXQJzjspKAvm9k7TJDV6fotSysLk7xzRAPOT8LAHvrpISiSui3_WUESg9CxzJtNx-64HZGPuw==', start_index=9390)
Annotation(end_index=9404, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHa1iOmqH-zpxOfRfMoazR9dIyUTd3YzrF06CamlojRG6UNYZm6w0jrZge2UHOLbcvOBb3qflKvJBE6VdbuI6wJnbbDMS0xGRRUSy46dPdvg2k41AZB4RdW82GhnWrlxvaD2jXPP_maqiymRJmMi7a_viaToR3g2dw95ZwJR6Jw', start_index=9390)
Annotation(end_index=9679, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_MZjPEa-A7TqUdb_MRQMdxOOJ9_JpjUUs2HAw_tdQwGHPSskoT1Vgx9YMyvgEw_k35WaUp2_1GpLPDcF7mBwDpiy0mQXbvbDCNhwA8cW_-1Oivbj-m1LUl5VdQAD9iX9RVAQ70PTaBkXKdEmEzY6M4QyYW3zSrVhCYLsuz0mLoRX1i4itV1YA21pccnW_UNPi7Nk-VfMkVzw8qXgpiqux_Bt2xYJ_I7zZa7TR33BEozVs_5k0fWp_Rf1xQkin8bAMYpM=', start_index=9661)
Annotation(end_index=9679, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFa_05tgOYgLwkPDphQVbqbnTqVkqepO7w1AYh1fXZTGz0fsT_z-eUTlw5S9OXqoD-Zw3fRshQti9IPN99G2DmSVyTeNgd7x9agRVxmE-zqE8d8HKUKu_g7HzOZPT4YqyDVBUWHIiDiF0nrITnQ4yZnpN4kiznBm_PRgKAsUophejXQJzjspKAvm9k7TJDV6fotSysLk7xzRAPOT8LAHvrpISiSui3_WUESg9CxzJtNx-64HZGPuw==', start_index=9661)
Annotation(end_index=9679, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMQQA-IWdO1dpDL8n4OLFqtoo9M9gsyuw1FqSdmtwFsrEVffkKSyuQExFt7dfz78crl-QRzkbzXKRjZwmvBdLtrcmUPQ4PEGya2QnVNBEhgE0NaBdzt_a_HIE36_8wVv_nZsBVwshDnwB_vkqWrbbHe6rUP7SJX4OjwyeBa7MK', start_index=9661)
Annotation(end_index=10342, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc-R2vUrHT3NPOb-GJjRItcnXGIIgIlz8cVwFM6e_cUUXCurF7RkY_cPk2lzKRWj0oxV3t0dEjUZn67PftQuyPSzpEFaxJ_X_RKYaes8zaRVd5AQE8yJP1Sil6jCjUStcDncFgDANDGPH6-HCOWrQ_-tZSs84Akl0=', start_index=10329)
Annotation(end_index=10342, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkz_5VlQKVwi-Cs31lFyaobc2wKZIeDeMkzlhG3y8S0sWcNLFOnkkp0N3NEeWrnOsObydLA3IfXnRjdRdkmtS7ib0OnmDQxpV3gbvfBspZuI66LZVx8TUXDqktWQk4DzfoMR3zFFfa5udreFt2dgBx6CiphhGzXSoed5zyZk_xH142g0dKvrIL8icrDlvN5bdmpXnAtrAFRA==', start_index=10329)
Annotation(end_index=10579, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFD32tROahv_1OOCvEalDtxeeqTCCLbJUwWNbqMWb07cGPMXifbFurxYt4Ya17kIPZipOgxXyeIVxmuJV8MFrYubE-Ih3Gr07Fl3fRccCTG8YbWUv5CtdgwX0BiXLrmimztnljauO9jbqSMbiYf-zs5DcrBTtMpatwh0nFXSg==', start_index=10561)
Annotation(end_index=10579, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRwhn50kdKIc_LN-DRaTqTXxgl9IE5ZkLBpCFMukjtFTCrijCLug4X1eRKP-jwVzr1vwMGcDumXWdqiksj0yd3rrqWNBXXttMTgpJCX5JSC8HYP3C24f5QjnGN4hd80AulyG3-Sjc8Tv0f0CIUmOW6VfYMN4ShdwSYrTDBPg==', start_index=10561)
Annotation(end_index=10579, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzu5_sZfTm8fGizEJRNFWgWK7fs3-LwGnnSd7wqc8r5Ra39bSU0qNvdqIOhc6jvOWnoR9tZlL6J3jg5n3zER3skXGU39lvXtYVpM6w-Rum_fWkd3JimDLfEHZSRzw37rle5w3bNPiGG8nAY1DF9R_cBvhoL8r95PfriiFN8CQOog==', start_index=10561)
Annotation(end_index=10909, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4ESaDD253iP3KVzhD40FBeaSg0eZ9iC9Ec7DMm6BD3FnCCO0xUWtFEp2TQeinCZx_W-fVXTfAqKWA0WSjh2gnMYaAb-tlkpJNmuFC8GcsR2XfojQOEVSBK_peZbnFCCVwfUNJm1yRw7QjVtadPbqpPE2Z4GTj-k8ORKh6a1iMVmU1-VzpQsgchtdJicsll4s2bWxi2iCkVYpCw9-qBNATWzkUPz9BFeaAGxvNfXiP1zkcafcFm4v6kHIIG1T6J3H6nevLYIJy1Gz9iO8=', start_index=10896)
Annotation(end_index=10909, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkDjA3pgpJKKbOL_eJIOahJLk4ZQ88v_Ah4bjFG61etVjylJWXwxaF4qSLnj41mgxGmuUfqsqEtFn23wMiUnTZmZibsK6HBQPMxvhRJEh9d9r-5JKj', start_index=10896)
Annotation(end_index=11178, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFD32tROahv_1OOCvEalDtxeeqTCCLbJUwWNbqMWb07cGPMXifbFurxYt4Ya17kIPZipOgxXyeIVxmuJV8MFrYubE-Ih3Gr07Fl3fRccCTG8YbWUv5CtdgwX0BiXLrmimztnljauO9jbqSMbiYf-zs5DcrBTtMpatwh0nFXSg==', start_index=11164)
Annotation(end_index=11178, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzu5_sZfTm8fGizEJRNFWgWK7fs3-LwGnnSd7wqc8r5Ra39bSU0qNvdqIOhc6jvOWnoR9tZlL6J3jg5n3zER3skXGU39lvXtYVpM6w-Rum_fWkd3JimDLfEHZSRzw37rle5w3bNPiGG8nAY1DF9R_cBvhoL8r95PfriiFN8CQOog==', start_index=11164)
Annotation(end_index=11567, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdgpEqv743clJG4K0Gdi0Gb6KijWWuBfEdXz7rKf2sJGe7IZfJ8HedXytWtcp0IMb48kh4YaGhggvjy424vnWSV6InznfpYgxGayvZD8NIDoIvEvFFGU2N-ek=', start_index=11554)
Annotation(end_index=11567, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkz_5VlQKVwi-Cs31lFyaobc2wKZIeDeMkzlhG3y8S0sWcNLFOnkkp0N3NEeWrnOsObydLA3IfXnRjdRdkmtS7ib0OnmDQxpV3gbvfBspZuI66LZVx8TUXDqktWQk4DzfoMR3zFFfa5udreFt2dgBx6CiphhGzXSoed5zyZk_xH142g0dKvrIL8icrDlvN5bdmpXnAtrAFRA==', start_index=11554)
Annotation(end_index=12323, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOn3rpWUuGk1VyZVxVSCdl_VWRjGxBrmke4azBR1qsq3hNp_9hisGb4G7HWQK4KHWzPj493MgQUXMclf5niTMe8E-dJKmLh9zCe0ZLcsD1IFvbo9DM', start_index=12309)
Annotation(end_index=12323, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1_aoJToZ0JqVEEoDLZlBkSnEl6IWfROIZTnSnBJukyjBfCKpDyFcBLCMlogEULNgk7dYw73AXnooXzetCJnUNmzv67MhbiXhMXfYRxk1fZOB1XQ-2rky3', start_index=12309)
Annotation(end_index=12815, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhak0D4Qf0YRlV2mE58r-XMCsPnZv-7QYdN4RV9c9s2gzfyV_U5OcvpsivlcHRXaLHZ0Iug_7HIlJIdxf7C1QuVlefmBueRfEsH1aztQlwV45bozxqJM-8', start_index=12801)
Annotation(end_index=12815, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1_aoJToZ0JqVEEoDLZlBkSnEl6IWfROIZTnSnBJukyjBfCKpDyFcBLCMlogEULNgk7dYw73AXnooXzetCJnUNmzv67MhbiXhMXfYRxk1fZOB1XQ-2rky3', start_index=12801)
Annotation(end_index=13041, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2CkANG2oZr3LQmFLw-8TFPL2m3vJaxFa1qGQ9swttLqL0UCc8hFij9w4Jd7rjvUzfHn1sfQffxyrp5qKsmTZpv1X-s0cRqZROdB0b8EU8niUn_q6p', start_index=13027)
Annotation(end_index=13041, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOn3rpWUuGk1VyZVxVSCdl_VWRjGxBrmke4azBR1qsq3hNp_9hisGb4G7HWQK4KHWzPj493MgQUXMclf5niTMe8E-dJKmLh9zCe0ZLcsD1IFvbo9DM', start_index=13027)
Annotation(end_index=13411, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2CkANG2oZr3LQmFLw-8TFPL2m3vJaxFa1qGQ9swttLqL0UCc8hFij9w4Jd7rjvUzfHn1sfQffxyrp5qKsmTZpv1X-s0cRqZROdB0b8EU8niUn_q6p', start_index=13393)
Annotation(end_index=13411, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBF2UTEuGSWs8m2tZzk_VJmPuclEL9IpiUyf3Jn_Cf0JvFI9G3GtiAr9Vb-yHQQhzck6IveCOgOQlJCuH0iuTQpnS9ztfmETw2n9X0zy8vIajUMQySvExThoUHXTdNGnDq9UYhGMK5q84EiWpu5FnycV1SzA_q7SLu5jqSNukct_9O', start_index=13393)
Annotation(end_index=13411, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1_aoJToZ0JqVEEoDLZlBkSnEl6IWfROIZTnSnBJukyjBfCKpDyFcBLCMlogEULNgk7dYw73AXnooXzetCJnUNmzv67MhbiXhMXfYRxk1fZOB1XQ-2rky3', start_index=13393)
Annotation(end_index=13776, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFONvmMOl7A6eznmvE3AoLPcbII3imWkBB2ZnxmL75bih0L6EBGsdIoBjxkJHa0Y15XKA_2x1QMtzVD9x2rOJ7YD9ejql0Ht-J3jzT0MNLT-UmOnaaMWLF9xCDAXLj3wIAYRW0h8qTE2_qKaQ==', start_index=13762)
Annotation(end_index=13776, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzZWvrwp7mApkk_C6i57rfa9L1TaJPRdxTvpAyPf9B5blk8NC_CDFMhAlNEecakX6QAfeSSUsqE6kNCWFF4zCnrSazJ2x3oLawbeSCjBtWU8LqjmARZzzUg0AOHdqEG1-dNUf6_sRwS1HGreDut8xTbZg7v7ziSg8Tri1fdBw6atif', start_index=13762)
Annotation(end_index=14439, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzZWvrwp7mApkk_C6i57rfa9L1TaJPRdxTvpAyPf9B5blk8NC_CDFMhAlNEecakX6QAfeSSUsqE6kNCWFF4zCnrSazJ2x3oLawbeSCjBtWU8LqjmARZzzUg0AOHdqEG1-dNUf6_sRwS1HGreDut8xTbZg7v7ziSg8Tri1fdBw6atif', start_index=14425)
Annotation(end_index=14439, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMQQA-IWdO1dpDL8n4OLFqtoo9M9gsyuw1FqSdmtwFsrEVffkKSyuQExFt7dfz78crl-QRzkbzXKRjZwmvBdLtrcmUPQ4PEGya2QnVNBEhgE0NaBdzt_a_HIE36_8wVv_nZsBVwshDnwB_vkqWrbbHe6rUP7SJX4OjwyeBa7MK', start_index=14425)
Annotation(end_index=14829, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbuv0srXEeU9zGAVEGJLODgHTzvLXs9fd2fHNA7oNxA_eTLb9_3B6n5BRbpKdw1jVvpR7JrAvhpdZ2d6g67ZL83Y0rnJYpvrfjiCd9eq5KPLTOjqGgZuCwn9G8nyQfGf-5wvD0-vYNDKgH39dS', start_index=14816)
Annotation(end_index=14829, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzZWvrwp7mApkk_C6i57rfa9L1TaJPRdxTvpAyPf9B5blk8NC_CDFMhAlNEecakX6QAfeSSUsqE6kNCWFF4zCnrSazJ2x3oLawbeSCjBtWU8LqjmARZzzUg0AOHdqEG1-dNUf6_sRwS1HGreDut8xTbZg7v7ziSg8Tri1fdBw6atif', start_index=14816)
Annotation(end_index=15314, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIiP_6pBv-LzOuBbjaERzfUzxPBJJDmuxj_DkjDz3jKqFIUgpxRMwXr-VZudRgz0-NXwI0QIm4efZtJrYPPUTi_FKZOEX6_kEIYqg4CbgeATgR3XB4KSDTV4pPkGvvKPWFOnh0vSTWAc1ZtUexvPnAGaO28DQDuDJqg217FtqQOWK8akCnY_a_JofJvVXvdIUeH0_0qSbO4cIouvsFniF5JA_br7hMDIqKeZpbSVDNGdOvgA==', start_index=15302)
Annotation(end_index=15314, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESUzNYLRtGbAzxSD2stNPCp7ZmHNf0a23wtt2WBq6nne0qPrxQS45UsLbgk5ziGkJWOnQGIXIdIMIvfJEN5FAUuQww54dknDtSNJ4CAsT_iNiHCqNln90aYq5-Oo1T3n5CUT0aBigwK5SHaXKYlgn7FFvMSYG4Yw==', start_index=15302)
Annotation(end_index=15554, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_MZjPEa-A7TqUdb_MRQMdxOOJ9_JpjUUs2HAw_tdQwGHPSskoT1Vgx9YMyvgEw_k35WaUp2_1GpLPDcF7mBwDpiy0mQXbvbDCNhwA8cW_-1Oivbj-m1LUl5VdQAD9iX9RVAQ70PTaBkXKdEmEzY6M4QyYW3zSrVhCYLsuz0mLoRX1i4itV1YA21pccnW_UNPi7Nk-VfMkVzw8qXgpiqux_Bt2xYJ_I7zZa7TR33BEozVs_5k0fWp_Rf1xQkin8bAMYpM=', start_index=15541)
Annotation(end_index=15554, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbuv0srXEeU9zGAVEGJLODgHTzvLXs9fd2fHNA7oNxA_eTLb9_3B6n5BRbpKdw1jVvpR7JrAvhpdZ2d6g67ZL83Y0rnJYpvrfjiCd9eq5KPLTOjqGgZuCwn9G8nyQfGf-5wvD0-vYNDKgH39dS', start_index=15541)
Annotation(end_index=15762, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE61KTGAWLK73A-RvY3AqbMZYPlZW9_SErQ7Io7VQA0mB9sJ742B3Sa9Ci4haLocNZGYL8t-BTjmgStV-ln0lur44Eo4sbC3i7B2AME1g6WB6g7ouwSeS6dZPl_Gmy_qvtS0kQKF5JivuuQDna4r0o=', start_index=15745)
Annotation(end_index=15762, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_Coa79Glk7mK4mhFeF3odjpZM53Sxmas3jV6xrvKbM6fhDGu1E5MO_kLpB3ubvHOJClIKXewXvFebKtYYot9Yz9TESxbXfSDEk9i4GxDkHxTeObpS', start_index=15745)
Annotation(end_index=15762, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzu5_sZfTm8fGizEJRNFWgWK7fs3-LwGnnSd7wqc8r5Ra39bSU0qNvdqIOhc6jvOWnoR9tZlL6J3jg5n3zER3skXGU39lvXtYVpM6w-Rum_fWkd3JimDLfEHZSRzw37rle5w3bNPiGG8nAY1DF9R_cBvhoL8r95PfriiFN8CQOog==', start_index=15745)
Annotation(end_index=15956, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOn3rpWUuGk1VyZVxVSCdl_VWRjGxBrmke4azBR1qsq3hNp_9hisGb4G7HWQK4KHWzPj493MgQUXMclf5niTMe8E-dJKmLh9zCe0ZLcsD1IFvbo9DM', start_index=15942)
Annotation(end_index=15956, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1_aoJToZ0JqVEEoDLZlBkSnEl6IWfROIZTnSnBJukyjBfCKpDyFcBLCMlogEULNgk7dYw73AXnooXzetCJnUNmzv67MhbiXhMXfYRxk1fZOB1XQ-2rky3', start_index=15942)
Annotation(end_index=16272, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkz_5VlQKVwi-Cs31lFyaobc2wKZIeDeMkzlhG3y8S0sWcNLFOnkkp0N3NEeWrnOsObydLA3IfXnRjdRdkmtS7ib0OnmDQxpV3gbvfBspZuI66LZVx8TUXDqktWQk4DzfoMR3zFFfa5udreFt2dgBx6CiphhGzXSoed5zyZk_xH142g0dKvrIL8icrDlvN5bdmpXnAtrAFRA==', start_index=16263)
Annotation(end_index=16372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbuv0srXEeU9zGAVEGJLODgHTzvLXs9fd2fHNA7oNxA_eTLb9_3B6n5BRbpKdw1jVvpR7JrAvhpdZ2d6g67ZL83Y0rnJYpvrfjiCd9eq5KPLTOjqGgZuCwn9G8nyQfGf-5wvD0-vYNDKgH39dS', start_index=16363)
Annotation(end_index=16480, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESUzNYLRtGbAzxSD2stNPCp7ZmHNf0a23wtt2WBq6nne0qPrxQS45UsLbgk5ziGkJWOnQGIXIdIMIvfJEN5FAUuQww54dknDtSNJ4CAsT_iNiHCqNln90aYq5-Oo1T3n5CUT0aBigwK5SHaXKYlgn7FFvMSYG4Yw==', start_index=16471)
Annotation(end_index=16587, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRwhn50kdKIc_LN-DRaTqTXxgl9IE5ZkLBpCFMukjtFTCrijCLug4X1eRKP-jwVzr1vwMGcDumXWdqiksj0yd3rrqWNBXXttMTgpJCX5JSC8HYP3C24f5QjnGN4hd80AulyG3-Sjc8Tv0f0CIUmOW6VfYMN4ShdwSYrTDBPg==', start_index=16577)
Annotation(end_index=16692, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzZWvrwp7mApkk_C6i57rfa9L1TaJPRdxTvpAyPf9B5blk8NC_CDFMhAlNEecakX6QAfeSSUsqE6kNCWFF4zCnrSazJ2x3oLawbeSCjBtWU8LqjmARZzzUg0AOHdqEG1-dNUf6_sRwS1HGreDut8xTbZg7v7ziSg8Tri1fdBw6atif', start_index=16682)
Annotation(end_index=16798, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE61KTGAWLK73A-RvY3AqbMZYPlZW9_SErQ7Io7VQA0mB9sJ742B3Sa9Ci4haLocNZGYL8t-BTjmgStV-ln0lur44Eo4sbC3i7B2AME1g6WB6g7ouwSeS6dZPl_Gmy_qvtS0kQKF5JivuuQDna4r0o=', start_index=16788)
Annotation(end_index=16900, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMQQA-IWdO1dpDL8n4OLFqtoo9M9gsyuw1FqSdmtwFsrEVffkKSyuQExFt7dfz78crl-QRzkbzXKRjZwmvBdLtrcmUPQ4PEGya2QnVNBEhgE0NaBdzt_a_HIE36_8wVv_nZsBVwshDnwB_vkqWrbbHe6rUP7SJX4OjwyeBa7MK', start_index=16890)
Annotation(end_index=17007, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOn3rpWUuGk1VyZVxVSCdl_VWRjGxBrmke4azBR1qsq3hNp_9hisGb4G7HWQK4KHWzPj493MgQUXMclf5niTMe8E-dJKmLh9zCe0ZLcsD1IFvbo9DM', start_index=16997)
Annotation(end_index=17108, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkDjA3pgpJKKbOL_eJIOahJLk4ZQ88v_Ah4bjFG61etVjylJWXwxaF4qSLnj41mgxGmuUfqsqEtFn23wMiUnTZmZibsK6HBQPMxvhRJEh9d9r-5JKj', start_index=17099)
Annotation(end_index=17205, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbuv0srXEeU9zGAVEGJLODgHTzvLXs9fd2fHNA7oNxA_eTLb9_3B6n5BRbpKdw1jVvpR7JrAvhpdZ2d6g67ZL83Y0rnJYpvrfjiCd9eq5KPLTOjqGgZuCwn9G8nyQfGf-5wvD0-vYNDKgH39dS', start_index=17196)
Annotation(end_index=17313, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_Coa79Glk7mK4mhFeF3odjpZM53Sxmas3jV6xrvKbM6fhDGu1E5MO_kLpB3ubvHOJClIKXewXvFebKtYYot9Yz9TESxbXfSDEk9i4GxDkHxTeObpS', start_index=17304)
Annotation(end_index=17413, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1_aoJToZ0JqVEEoDLZlBkSnEl6IWfROIZTnSnBJukyjBfCKpDyFcBLCMlogEULNgk7dYw73AXnooXzetCJnUNmzv67MhbiXhMXfYRxk1fZOB1XQ-2rky3', start_index=17403)
Annotation(end_index=17514, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzu5_sZfTm8fGizEJRNFWgWK7fs3-LwGnnSd7wqc8r5Ra39bSU0qNvdqIOhc6jvOWnoR9tZlL6J3jg5n3zER3skXGU39lvXtYVpM6w-Rum_fWkd3JimDLfEHZSRzw37rle5w3bNPiGG8nAY1DF9R_cBvhoL8r95PfriiFN8CQOog==', start_index=17504)

## Sources
