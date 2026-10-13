# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** a10c06a7 | **Time:** 356.00s | **Cost:** $1.04064
--------------------------------------------------------------------------------

# Convex Optimization in High-Dimensional Portfolio Allocation: Global Convergence, Local Extrema, and Duality Gap Dynamics

**Key Points**
*   **Convexity Guarantees Global Optimality:** In standard convex portfolio optimization (e.g., traditional Markowitz mean-variance), the distinction between local and global extrema is nonexistent; every local minimum is a global minimum. Therefore, solvers do not need to "balance" global convergence with local escape mechanisms in these contexts.
*   **Non-Convexity Requires Relaxation:** When realistic constraints (e.g., cardinality, buy-in thresholds) are added, the problem becomes non-convex (NP-hard). Algorithms handle this not by "escaping" local extrema in the heuristic sense, but by **relaxing** the problem into a convex form (e.g., $L_1$ relaxation) or using Successive Convexification (SCvx), which iteratively solves convex subproblems to approach a local (and under specific conditions, global) optimum.
*   **Duality Gap as an Efficiency Tool:** Duality gap estimation does not typically amplify complexity; rather, it serves as a critical **stopping criterion** that reduces computational cost by allowing solvers to terminate once a solution is within a guaranteed tolerance of the optimum.
*   **The Shapley-Folkman Effect in High Dimensions:** Contrary to the intuition that high dimensions increase complexity regarding the duality gap, the **Shapley-Folkman theorem** suggests that for separable non-convex problems, the relative duality gap **vanishes** as the number of assets increases. This implies that in high-dimensional allocation, the dual solution provides an increasingly accurate proxy for the primal global optimum.

## 1. Introduction

The application of convex optimization to portfolio allocation is a cornerstone of modern financial engineering. The user’s query posits a dichotomy: whether solvers balance global convergence with local extrema escape, or if duality gap estimation amplifies complexity in high-dimensional settings. This report argues that for purely convex formulations, the first premise is a category error because local optima are inherently global. However, for practical, non-convex portfolio problems (involving cardinality or sparsity constraints), solvers employ relaxation techniques that trade exact global guarantees for computational tractability. Furthermore, the report challenges the notion that duality gap estimation amplifies complexity; instead, theoretical frameworks like the Shapley-Folkman lemma demonstrate that in high-dimensional regimes, the duality gap diminishes, rendering dual-based approaches particularly effective.

## 2. Convex Optimization and the Nature of Convergence

To address whether solvers "balance" global convergence with local extrema escape, one must first distinguish between convex and non-convex portfolio formulations.

### 2.1. The Convexity Guarantee: Local is Global
The fundamental property of convex optimization is that the objective function is convex (bowl-shaped) and the feasible set is a convex set. In this landscape, any local minimum is guaranteed to be a global minimum [cite: 1, 2].
*   **Standard Mean-Variance:** The classic Markowitz optimization minimizes variance (a convex quadratic form $w^T \Sigma w$) subject to linear constraints (expected return, budget). This is a Quadratic Programming (QP) problem.
*   **Implication for Solvers:** For these problems, algorithms such as Interior Point Methods (IPM) or Active Set methods do not need mechanisms to "escape" local extrema because no suboptimal local traps exist [cite: 3, 4]. The solver follows a descent path (e.g., Newton steps) that converges directly to the global optimum with polynomial time complexity [cite: 5, 6].

### 2.2. Non-Convexity in Realistic Portfolios
The need to "balance" convergence with local escape arises only when the portfolio problem becomes non-convex. This occurs with:
*   **Cardinality Constraints:** Limiting the portfolio to a maximum of $K$ assets (using the $L_0$ "norm").
*   **Minimum Buy-In Thresholds:** Requiring that if an asset is bought, at least a certain amount must be purchased.
*   **Concave Transaction Costs:** Costs that decrease marginally with volume.

In these scenarios, the optimization landscape becomes rugged, possessing multiple local minima. Here, the user's query regarding "balancing global convergence with local extrema escape" becomes relevant. However, modern "convex optimization solvers" do not typically use heuristic escape mechanisms (like Simulated Annealing). Instead, they use **Convex Relaxation** or **Successive Convexification** [cite: 7, 8].

#### 2.2.1. Successive Convexification (SCvx)
SCvx algorithms address non-convex control and allocation problems by linearizing non-convex dynamics or constraints around a current solution, creating a convex subproblem. The solver iterates through these subproblems [cite: 5, 8].
*   **Mechanism:** The algorithm projects the non-convex problem onto a convex subset, solves it to optimality (global for the subproblem), and updates the linearization point.
*   **Convergence:** While SCvx guarantees convergence to a local optimum of the original non-convex problem, it does not inherently guarantee a global optimum unless specific conditions (like the Kurdyka-Łojasiewicz property) are met [cite: 5, 7]. Thus, the "balance" is between the computational speed of convex sub-solvers and the approximation quality of the non-convex solution.

#### 2.2.2. Difference of Convex (DC) Programming
Another approach for non-convex portfolios is decomposing the objective into the difference of two convex functions ($f(x) - g(x)$). Algorithms like the Boosted Difference of Convex Functions Algorithm (BDCA) exploit this structure to escape local extrema more effectively than standard gradient methods, often achieving linear convergence rates [cite: 9, 10].

## 3. Duality Gap Estimation: Complexity and Stopping Criteria

The second part of the query asks if duality gap estimation amplifies complexity. The literature suggests the opposite: the duality gap is a tool for *managing* and *reducing* effective computational complexity.

### 3.1. Definition and Role
The duality gap is the difference between the primal objective value ($P^*$) and the dual objective value ($D^*$).
*   **Weak Duality:** $D^* \leq P^*$ (for minimization). The gap is always non-negative [cite: 11, 12].
*   **Strong Duality:** For convex problems satisfying Slater's condition, the gap is zero ($P^* = D^*$) [cite: 13, 14].

### 3.2. The Gap as a Stopping Criterion
In high-dimensional allocation, finding the *exact* analytical solution is often computationally prohibitive. Solvers use the duality gap as a rigorous stopping criterion [cite: 15, 16].
*   **Efficiency:** Instead of iterating until machine precision is reached, a solver terminates when the duality gap falls below a threshold $\epsilon$ (e.g., $10^{-4}$). This guarantees the solution is within $\epsilon$ of the true global optimum.
*   **Complexity Reduction:** By providing a certificate of near-optimality, duality gap estimation prevents "over-solving," thereby reducing the number of iterations required in high-dimensional spaces [cite: 6].

### 3.3. Duality Gap in Non-Convex Regimes
For non-convex problems (e.g., cardinality constrained), the duality gap is generally non-zero (Weak Duality). However, the size of this gap is informative.
*   **Gap Safe Screening:** Duality gaps allow for "screening" techniques where features (assets) that cannot possibly be part of the optimal solution are discarded early. This effectively reduces the dimensionality of the problem, *lowering* complexity rather than amplifying it [cite: 17].

## 4. High-Dimensional Allocation and the Shapley-Folkman Theorem

A critical theoretical insight regarding high-dimensional portfolios contradicts the fear of amplified complexity. This is the **Shapley-Folkman Theorem**.

### 4.1. The "Blessing of Dimensionality"
The Shapley-Folkman lemma states that the Minkowski sum of a large number of non-convex sets becomes approximately convex.
*   **Application to Portfolios:** If a portfolio optimization problem is **separable** (the objective is a sum of functions for each asset, $f(w) = \sum f_i(w_i)$), the non-convexity "averages out" as the number of assets $N$ increases [cite: 18, 19].
*   **Vanishing Duality Gap:** The duality gap for separable non-convex problems is bounded by a value that depends on the non-convexity of individual terms and the number of constraints $m$. Crucially, as the number of assets $N \to \infty$ (while constraints $m$ remain fixed), the *relative* duality gap approaches zero [cite: 18, 20].

### 4.2. Implications for High-Dimensional Allocation
In a high-dimensional portfolio ($N \gg m$):
1.  **Dual Reliability:** The solution to the convex dual problem becomes an increasingly accurate proxy for the primal non-convex global optimum.
2.  **Algorithmic Strategy:** Instead of struggling with the combinatorial complexity of the primal non-convex problem, one can solve the convex dual problem efficiently. The Shapley-Folkman theorem guarantees that the resulting solution is nearly feasible and nearly optimal for the primal problem [cite: 19, 21].
3.  **Conclusion:** Far from amplifying complexity, duality gap estimation in high dimensions facilitates the use of efficient dual-based algorithms that provide near-global solutions to otherwise NP-hard problems.

## 5. Complexity in High-Dimensional Settings: Ill-Conditioning

While the duality gap itself does not amplify complexity, high-dimensional portfolios face the challenge of **ill-conditioning**.

### 5.1. Covariance Matrix Singularity
When the number of assets $N$ exceeds the number of historical observations $T$, the sample covariance matrix $\Sigma$ becomes singular or ill-conditioned [cite: 22, 23].
*   **Impact:** This makes the quadratic term $w^T \Sigma w$ flat in certain directions, leading to unstable solutions and numerical difficulties for solvers.
*   **Duality Gap Behavior:** Research indicates that the condition number of the Newton system in interior point methods may plateau at small duality gaps, suggesting that while numerical precision is hard, the duality gap metric remains robust [cite: 23].

### 5.2. Regularization and Sparsity
To combat ill-conditioning, high-dimensional algorithms employ regularization (e.g., $L_1$ Lasso, $L_2$ Ridge).
*   **Sparse Portfolios:** $L_1$ regularization induces sparsity (selecting fewer assets). This effectively reduces the dimensionality of the active set.
*   **Complexity:** The complexity of solving these regularized problems is often dominated by matrix operations ($O(N^3)$). However, coordinate descent and proximal gradient methods (like FISTA) can solve these efficiently, using the duality gap to monitor convergence [cite: 7, 16].

## 6. Detailed Analysis of Solver Mechanisms

### 6.1. Interior Point Methods (IPM)
IPMs are the standard for convex portfolio problems (e.g., Second-Order Cone Programming - SOCP).
*   **Mechanism:** They traverse the interior of the feasible region using a barrier function.
*   **Duality Gap:** The gap is explicitly minimized as part of the "central path" trajectory. The complexity is polynomial, typically $O(\sqrt{N} \log(1/\epsilon))$ iterations [cite: 6].
*   **Balance:** There is no balancing of local/global; the path leads uniquely to the global optimum.

### 6.2. Proximal Gradient Algorithms (PGA)
For non-smooth convex problems (e.g., Lasso portfolios), PGAs are preferred.
*   **Mechanism:** They alternate between a gradient descent step and a proximal projection (e.g., soft thresholding).
*   **Global Convergence:** For convex objectives, they converge globally. For non-convex (e.g., $L_0$ constraints), they converge to a critical point. Recent research (2024) utilizes the Kurdyka-Łojasiewicz (KL) property to prove that these algorithms can achieve globally optimal $m$-sparse Sharpe ratios under specific conditions, effectively bridging the gap between local and global search [cite: 7].

## 7. Conclusion

The answer to the user's query is nuanced but clear based on current research:

1.  **No Balance Needed for Convex Cases:** For standard convex portfolio optimization, solvers do not balance global convergence with local extrema escape because local extrema do not exist. Global convergence is mathematically guaranteed.
2.  **Relaxation for Non-Convexity:** In non-convex high-dimensional allocation (e.g., sparse portfolios), solvers use relaxation (convexification) to approximate global solutions. They do not typically use heuristic "escape" mechanisms but rather rely on the properties of the relaxed landscape (like the KL property) to ensure convergence to optimality.
3.  **Duality Gap Reduces Complexity:** Duality gap estimation does **not** amplify complexity. It serves as a vital stopping criterion that prevents unnecessary iterations.
4.  **High-Dimensional Advantage:** Theoretical results (Shapley-Folkman) indicate that in high-dimensional separable problems, the duality gap naturally diminishes. This allows dual-based solvers to find near-global optima for non-convex problems efficiently, effectively turning the "curse of dimensionality" into a computational advantage for validity checking.

Therefore, the duality gap is a mechanism of **efficiency and verification**, not a source of amplified complexity, while the "balancing" of global/local convergence is a specific characteristic of **non-convex relaxation algorithms** rather than general convex solvers.

## References

*   **[cite: 7]** *Li, X. et al.* (2024). "Sparse Sharpe Ratio Maximization." arXiv:2410.21100.
*   **[cite: 18]** *Dubois-Taine, B. & d'Aspremont, A.* (2025). "Shapley-Folkman and Duality Gap." arXiv:2406.18282.
*   **[cite: 1]** *Deepchecks.* "Convex Optimization Glossary."
*   **[cite: 3]** *Beck, A.* "Introduction to Nonlinear Optimization." Lecture Slides.
*   **[cite: 5]** *Mao, Y. et al.* (2017). "Successive Convexification." arXiv:1701.00558.
*   **[cite: 17]** *Du, J. et al.* (2022). "High-Dimensional Portfolio Selection." Journal of the American Statistical Association.
*   **[cite: 6]** *Cornuejols, G.* "Optimization Algorithms." Portfolio Optimization Book Slides.
*   **[cite: 22]** *Kjellberg, M.* (2023). "Portfolio Optimization with Ill-Conditioned Covariance." DIVA Portal.
*   **[cite: 23]** *Zheng, X. et al.* (2024). "Ill-Conditioned Null-Space Basis." arXiv:2211.12489.
*   **[cite: 15]** *Taylor & Francis.* "Duality Gap in Engineering."
*   **[cite: 16]** *Sun, D. et al.* (2023). "Efficient Algorithm for Exclusive Lasso." PolyU.
*   **[cite: 8]** *Mao, Y.* (2017). "Successive Convexification for Non-Convex Control." arXiv:1701.00558.
*   **[cite: 19]** *Bi, Y. & Tang, A.* (2020). "Refined Shapley-Folkman Lemma." SIAM Journal on Optimization.
*   **[cite: 18]** *Dubois-Taine, B.* (2025). "Two-Stage Approach for Nonconvex Optimization." arXiv:2406.18282.

**Sources:**
1. [deepchecks.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAW9YDxDQedKLdTtjboVLKAvSw6tiKKvBPbP1wrWGVFQ22AB6bW_MUcKiF_jshZA_o4yT8nZy2E52SWtZb8sNRKKFbF3JOUljfCyk18_OA61hIIua86o7KK2QCxovQ1cUJDrA8JK82eP8SQuGg8Q==)
2. [futhark-lang.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb7vCcPJP3VdVLeecV5gNM__hQFRqnihwkCipxaJ2SHJJXD6B3qpbGHiMtqqS67D0l6Epts57q-yjIY1RvebByLzGqrK6111XCBKqI8Pftcg0I0fpGCmzGEeTWkjCIcRrKg_3OMSOK53Gg3wgeuJVzwbzknYI=)
3. [tau.ac.il](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7qgp_FKmG679g-BLTDKVd6BE3yZJnM7Tz_dMlFa-g_v_axbXTye927jMvX8_T3a5_GHF9VRlppQBxFEB-DKzPhKUdGHEn7Uurok2lwP3og-AJ6IeStPWnmbhN4FhirpoMQcsSkLGd-sJoPcci1z4xtm9FjDYqhgd4kA==)
4. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcpxl11gVFP3WvlgjIOng3RAXn5ef2pz6FNyjcTXanjBuYSZfCnVRj8d7sUy-eIm4SvVrELEP7gRQ2TvmFhjpvWcP_Q8n52tOFDj2aowduAr4KKYWJ8hs22_jxrSaSdU19a6moS7AV-tptrt13etBnFiGS1FkWzJIr)
5. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgh-XFCRjR6kwkMcIdEoPIhJcrwCOrhD9rZlcXRO7CI914Wl5ZXPUVHW8lIznVotS3hwbnQG9hS6evJileOHZbkY9kpWJXDFXlD8nvhWjkcPuBMihXOA==)
6. [portfoliooptimizationbook.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpRGuOJDKBFur7wLJJCGB-VGZDPe5ab26S4vz3rubFg49MYFScLY4wVM3kOXcVhXqgXiN6ILFeU0usbYrwuHm-PmUZ0VwmnjwBKjasp_J1-v3Q5lrQ1lJietPGyrQ-lhxKSmrFvFg2EP8BOu0y2Wwxi_jrPOeC9e7Loy39ElB5bfEzBvkj)
7. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFomO7mqD-fjlmYmQL7k514PFd-vOqwDV9BUxHJ1f1YWIG4oLtFKlhyMFTn6Z3PmeKoBB663eyqVazLuJfcscpzxu4xR55tDK0FhXQbouKy0KABXxCGKg==)
8. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6WpNJmi8qfDXrECAvp1WhpwMpa6u_azsPP-U6LHPOtdVxwJMElY9do3WcJxbCYd-Fwzbyh40ad17ssOo0Y1waephlI4LbvEoVpb0-r2-yxcw3in_WZg==)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEx8NKe0VYhcpbwDjrWwslMo6iqkjOE8-azIk1GAHoKj7lJLr1mOaQrcSpo8yRsFn7qQCilbNW-nyUy5RAj5VoB3hW5KF5Pmh7kxiNos37rUlGBUnVNDbEzz9jhLvv2WdT0rasww5XbqYbSzK4qy6Tz0-EUGDUCLwjyJ5YwOklyZZRyY4cSPfG7AwL114dLNCjbMeiQLhPdR0IsgRwKNV5tJz4rvELYkTETBMnBX-beu-o9F08Lbj8mJu7CVQgz90nnstLI1K8hc6Yn8b0v3IDzJXVa)
10. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlIUBzXs1hAWjFrjI_WQgMzOhC-FhaHkaDMPU9LQw0uMF6qYJv65AHsvbuja-0Ej4k6-Ep97shizrrrZ0oo5z63koScztodQYe7C5SFZHc30y3UR4NRA==)
11. [ens.fr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiSHLKEmDT1tE4g_HIK_XdWmMBUOu_4sjp9f37OgqXE3iPStg7nEeVUVsA_aV4LJxQgTmdDxiJQmfSWug_GNKEseZh0Hnh7SLvO1RrMssrtrgkDmx0R0xEwqdJ947ujWxk6mfpYDRhrArsYV9FSLsoX_W_1Z6cZW0=)
12. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8Nu6IivmiX0IniT7dEXLmhu-U0NTw80ohqvG1ICwJK79piU0Qu8DF06SDHWrd55hQVM7Yv6U5IVUuCSNG44hfDKz_zyYFFzULcVnyzF5-W3UkEYKvNx_qEdWSipr0-PH1D5__EZQWexZZ)
13. [cornell.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE23AHApa_U751M6AV_CdQYurFm1BZbyIIExGXbuZD3aj_9_dnbcus7-cwwe4zKiBylnDHW7c3x452YAgLKwfgjaKzw70m2CSkzuyfQmIKCzUsl5E_db4v9WFzpv_rrIotDS-ozej6SiRQbXMYGIrcvkEI=)
14. [iitb.ac.in](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjnAtAauHVmEPTMSbwHCdAQF31U9sulvP1UHvcIYOhR0YwpZhorcahTfDGSb2eEl_KpBble_tQKA6Kh5DtSrKrneFwBUOgDXsOi1wE9EAo3uqmg35e295Vmw7laSq1MYxsAwTGYho80MPrXNnAjvR8jr1ZudQlgeTQnNGOFN1611Ef5K7PV2a6lmavt2FCkmtsi9QmWKRdP6aSa_K-8JZ8dhkA-zskfepquDs06xSY)
15. [taylorandfrancis.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSXbXIBr5XDbWTysSCj_1FGEWoylRoXlkUJIEk871EioKgzJq0xovi-D2-_S_9eRNJgG58mhZ9KsxQ8NjJNpjtFkSxy7pwXDWUuRJV5oKJlNDDCYu-W4lvwxQRvspAOFR2TIrX8rAUJj081x_jXGGiRqPjUwmwwsKwsbgGF1Pm7J2yxX5h_DDqghLIT-fojcklGik7ww==)
16. [polyu.edu.hk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKBFAcSTOqz88Mwa6IQU1WIYq-RTx3ZcXQsGMyhIA8UhxYtYVwllYR-UGYSuYTzILvV-LZEM6goK2ry5pDuDk5wqAofa5xmziVCfb1XyR7bJlWb3UY6gInwYUxfREaJ9V9RfzJAHkoCG0UcZ348tD41-8IPPDk_DyEA9mfGajZ3DJx8YqdgcF_Im7aFjdJRRrmlycUzTn5S1IReC1k5brfUvfhqmHb7zYayP_hyAVFfIz_nPnZLnkxQL_ZIQw=)
17. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdcy8s9Cd0HwPBmSNRzh7OI7qX9KARxXNtnlf3Umqd74MIaNUiBctvdTepMVuF3qpLG_IFTpBUNMoqL5VCnI8cvVJCUIa7ArLHThVEKmodz6Bya4L_dF7dwr-DKxSIkjEMotzZVZiyUxEzSfRNHzgPnD4ZaaTKv80=)
18. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1iy6iELp2e7tJuSpq3aSpRIcgHv2947zN19giHlWfYDxueUgeiNa-w4bkcpseRg49ao6OjlR7ox4nkwVMNXqhos80D_97UWTpSYEBM1RNHNTDfJfuVQ==)
19. [cornell.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-Ug_C_EQv7KQ8VkCF8gRplFpyZ7BB0SLoaccdzFK6ip5ej9S4u6bRj0B9NSA8B13xfCCujXkncaN28lCqf2W8jiYcjIgM62i59myqhX8Q2S55hDwVd_PULQ-9qFww5v1K1zZhnbduYzt8cziusg==)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmlr3g3ezkJ97APPQi_EdCUQ4fo2Z-RIfdK2DQGu1BnaFjD6mvxmlnJtpiXfAg1TybYzcggo-gLFx88Sbmzpy5WE4-54A1Gh4uO3G1vv_xnmUQE2U0jabW3vT8CgcF-KaKroLPXNtRZpkSAB9xvfxbYpHd3WEz1wXz0eAxbSZ24VK83tGZsCC7GQhAgbqoW1Ea7EkqVYEgSXPKqI5iOqiMaaebPNoLr7NDfQITXR9Ps-Skqybk1HMA0gydRY5VhPoUc3PzL14ZbEbZ2gHa3yenlx1EJdlQl3ZMfT3fhk0gbJzV)
21. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCus1n_LUkrKZA86ohYhu1_Cll7K1mPil_CZmgIFWMg4yvg3H61AOu60zNizK8JFmeNDVFENtVPyzx3f6M6v9CSN2j_cBNudzK0X8F55BxokTwX6lOTZowuOPh-84YGv1T6pnSgEmpe9ZRUq1QWgLP9XWO)
22. [diva-portal.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGClJ_TQtOY2jI6pyxMNNYC40ZqbXA22C9KFF60BYDUIw8hR69Y4hN3o7RskyFp7FLVEGM4NBp-H94BcW4VyP87kjSsBwX47dW-EvrHAef8bkJbyponOVYLOjMq9SyQG9R_CVYAc79TFcfX51_tI7J2yiE1_vUcjKY=)
23. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfQs1ma6DfniFrFzDnqThKzOFaD2RlNIMiTVQA_STZxwbHX2u67zEGuqxI0CmAQm6lgvCe30D4nSifgYmqCZdqh8uuOcIlLkH0n5bbqlcErmPOEx2ojg==)


## Annotations
Annotation(end_index=3155, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAW9YDxDQedKLdTtjboVLKAvSw6tiKKvBPbP1wrWGVFQ22AB6bW_MUcKiF_jshZA_o4yT8nZy2E52SWtZb8sNRKKFbF3JOUljfCyk18_OA61hIIua86o7KK2QCxovQ1cUJDrA8JK82eP8SQuGg8Q==', start_index=3143)
Annotation(end_index=3155, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb7vCcPJP3VdVLeecV5gNM__hQFRqnihwkCipxaJ2SHJJXD6B3qpbGHiMtqqS67D0l6Epts57q-yjIY1RvebByLzGqrK6111XCBKqI8Pftcg0I0fpGCmzGEeTWkjCIcRrKg_3OMSOK53Gg3wgeuJVzwbzknYI=', start_index=3143)
Annotation(end_index=3611, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcpxl11gVFP3WvlgjIOng3RAXn5ef2pz6FNyjcTXanjBuYSZfCnVRj8d7sUy-eIm4SvVrELEP7gRQ2TvmFhjpvWcP_Q8n52tOFDj2aowduAr4KKYWJ8hs22_jxrSaSdU19a6moS7AV-tptrt13etBnFiGS1FkWzJIr', start_index=3599)
Annotation(end_index=3611, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7qgp_FKmG679g-BLTDKVd6BE3yZJnM7Tz_dMlFa-g_v_axbXTye927jMvX8_T3a5_GHF9VRlppQBxFEB-DKzPhKUdGHEn7Uurok2lwP3og-AJ6IeStPWnmbhN4FhirpoMQcsSkLGd-sJoPcci1z4xtm9FjDYqhgd4kA==', start_index=3599)
Annotation(end_index=3758, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgh-XFCRjR6kwkMcIdEoPIhJcrwCOrhD9rZlcXRO7CI914Wl5ZXPUVHW8lIznVotS3hwbnQG9hS6evJileOHZbkY9kpWJXDFXlD8nvhWjkcPuBMihXOA==', start_index=3746)
Annotation(end_index=3758, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpRGuOJDKBFur7wLJJCGB-VGZDPe5ab26S4vz3rubFg49MYFScLY4wVM3kOXcVhXqgXiN6ILFeU0usbYrwuHm-PmUZ0VwmnjwBKjasp_J1-v3Q5lrQ1lJietPGyrQ-lhxKSmrFvFg2EP8BOu0y2Wwxi_jrPOeC9e7Loy39ElB5bfEzBvkj', start_index=3746)
Annotation(end_index=4658, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6WpNJmi8qfDXrECAvp1WhpwMpa6u_azsPP-U6LHPOtdVxwJMElY9do3WcJxbCYd-Fwzbyh40ad17ssOo0Y1waephlI4LbvEoVpb0-r2-yxcw3in_WZg==', start_index=4646)
Annotation(end_index=4658, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFomO7mqD-fjlmYmQL7k514PFd-vOqwDV9BUxHJ1f1YWIG4oLtFKlhyMFTn6Z3PmeKoBB663eyqVazLuJfcscpzxu4xR55tDK0FhXQbouKy0KABXxCGKg==', start_index=4646)
Annotation(end_index=4939, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6WpNJmi8qfDXrECAvp1WhpwMpa6u_azsPP-U6LHPOtdVxwJMElY9do3WcJxbCYd-Fwzbyh40ad17ssOo0Y1waephlI4LbvEoVpb0-r2-yxcw3in_WZg==', start_index=4927)
Annotation(end_index=4939, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgh-XFCRjR6kwkMcIdEoPIhJcrwCOrhD9rZlcXRO7CI914Wl5ZXPUVHW8lIznVotS3hwbnQG9hS6evJileOHZbkY9kpWJXDFXlD8nvhWjkcPuBMihXOA==', start_index=4927)
Annotation(end_index=5366, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgh-XFCRjR6kwkMcIdEoPIhJcrwCOrhD9rZlcXRO7CI914Wl5ZXPUVHW8lIznVotS3hwbnQG9hS6evJileOHZbkY9kpWJXDFXlD8nvhWjkcPuBMihXOA==', start_index=5354)
Annotation(end_index=5366, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFomO7mqD-fjlmYmQL7k514PFd-vOqwDV9BUxHJ1f1YWIG4oLtFKlhyMFTn6Z3PmeKoBB663eyqVazLuJfcscpzxu4xR55tDK0FhXQbouKy0KABXxCGKg==', start_index=5354)
Annotation(end_index=5913, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEx8NKe0VYhcpbwDjrWwslMo6iqkjOE8-azIk1GAHoKj7lJLr1mOaQrcSpo8yRsFn7qQCilbNW-nyUy5RAj5VoB3hW5KF5Pmh7kxiNos37rUlGBUnVNDbEzz9jhLvv2WdT0rasww5XbqYbSzK4qy6Tz0-EUGDUCLwjyJ5YwOklyZZRyY4cSPfG7AwL114dLNCjbMeiQLhPdR0IsgRwKNV5tJz4rvELYkTETBMnBX-beu-o9F08Lbj8mJu7CVQgz90nnstLI1K8hc6Yn8b0v3IDzJXVa', start_index=5900)
Annotation(end_index=5913, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlIUBzXs1hAWjFrjI_WQgMzOhC-FhaHkaDMPU9LQw0uMF6qYJv65AHsvbuja-0Ej4k6-Ep97shizrrrZ0oo5z63koScztodQYe7C5SFZHc30y3UR4NRA==', start_index=5900)
Annotation(end_index=6439, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8Nu6IivmiX0IniT7dEXLmhu-U0NTw80ohqvG1ICwJK79piU0Qu8DF06SDHWrd55hQVM7Yv6U5IVUuCSNG44hfDKz_zyYFFzULcVnyzF5-W3UkEYKvNx_qEdWSipr0-PH1D5__EZQWexZZ', start_index=6425)
Annotation(end_index=6439, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiSHLKEmDT1tE4g_HIK_XdWmMBUOu_4sjp9f37OgqXE3iPStg7nEeVUVsA_aV4LJxQgTmdDxiJQmfSWug_GNKEseZh0Hnh7SLvO1RrMssrtrgkDmx0R0xEwqdJ947ujWxk6mfpYDRhrArsYV9FSLsoX_W_1Z6cZW0=', start_index=6425)
Annotation(end_index=6560, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE23AHApa_U751M6AV_CdQYurFm1BZbyIIExGXbuZD3aj_9_dnbcus7-cwwe4zKiBylnDHW7c3x452YAgLKwfgjaKzw70m2CSkzuyfQmIKCzUsl5E_db4v9WFzpv_rrIotDS-ozej6SiRQbXMYGIrcvkEI=', start_index=6546)
Annotation(end_index=6560, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjnAtAauHVmEPTMSbwHCdAQF31U9sulvP1UHvcIYOhR0YwpZhorcahTfDGSb2eEl_KpBble_tQKA6Kh5DtSrKrneFwBUOgDXsOi1wE9EAo3uqmg35e295Vmw7laSq1MYxsAwTGYho80MPrXNnAjvR8jr1ZudQlgeTQnNGOFN1611Ef5K7PV2a6lmavt2FCkmtsi9QmWKRdP6aSa_K-8JZ8dhkA-zskfepquDs06xSY', start_index=6546)
Annotation(end_index=6789, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSXbXIBr5XDbWTysSCj_1FGEWoylRoXlkUJIEk871EioKgzJq0xovi-D2-_S_9eRNJgG58mhZ9KsxQ8NjJNpjtFkSxy7pwXDWUuRJV5oKJlNDDCYu-W4lvwxQRvspAOFR2TIrX8rAUJj081x_jXGGiRqPjUwmwwsKwsbgGF1Pm7J2yxX5h_DDqghLIT-fojcklGik7ww==', start_index=6775)
Annotation(end_index=6789, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKBFAcSTOqz88Mwa6IQU1WIYq-RTx3ZcXQsGMyhIA8UhxYtYVwllYR-UGYSuYTzILvV-LZEM6goK2ry5pDuDk5wqAofa5xmziVCfb1XyR7bJlWb3UY6gInwYUxfREaJ9V9RfzJAHkoCG0UcZ348tD41-8IPPDk_DyEA9mfGajZ3DJx8YqdgcF_Im7aFjdJRRrmlycUzTn5S1IReC1k5brfUvfhqmHb7zYayP_hyAVFfIz_nPnZLnkxQL_ZIQw=', start_index=6775)
Annotation(end_index=7253, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpRGuOJDKBFur7wLJJCGB-VGZDPe5ab26S4vz3rubFg49MYFScLY4wVM3kOXcVhXqgXiN6ILFeU0usbYrwuHm-PmUZ0VwmnjwBKjasp_J1-v3Q5lrQ1lJietPGyrQ-lhxKSmrFvFg2EP8BOu0y2Wwxi_jrPOeC9e7Loy39ElB5bfEzBvkj', start_index=7244)
Annotation(end_index=7746, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdcy8s9Cd0HwPBmSNRzh7OI7qX9KARxXNtnlf3Umqd74MIaNUiBctvdTepMVuF3qpLG_IFTpBUNMoqL5VCnI8cvVJCUIa7ArLHThVEKmodz6Bya4L_dF7dwr-DKxSIkjEMotzZVZiyUxEzSfRNHzgPnD4ZaaTKv80=', start_index=7736)
Annotation(end_index=8389, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-Ug_C_EQv7KQ8VkCF8gRplFpyZ7BB0SLoaccdzFK6ip5ej9S4u6bRj0B9NSA8B13xfCCujXkncaN28lCqf2W8jiYcjIgM62i59myqhX8Q2S55hDwVd_PULQ-9qFww5v1K1zZhnbduYzt8cziusg==', start_index=8375)
Annotation(end_index=8389, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1iy6iELp2e7tJuSpq3aSpRIcgHv2947zN19giHlWfYDxueUgeiNa-w4bkcpseRg49ao6OjlR7ox4nkwVMNXqhos80D_97UWTpSYEBM1RNHNTDfJfuVQ==', start_index=8375)
Annotation(end_index=8728, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmlr3g3ezkJ97APPQi_EdCUQ4fo2Z-RIfdK2DQGu1BnaFjD6mvxmlnJtpiXfAg1TybYzcggo-gLFx88Sbmzpy5WE4-54A1Gh4uO3G1vv_xnmUQE2U0jabW3vT8CgcF-KaKroLPXNtRZpkSAB9xvfxbYpHd3WEz1wXz0eAxbSZ24VK83tGZsCC7GQhAgbqoW1Ea7EkqVYEgSXPKqI5iOqiMaaebPNoLr7NDfQITXR9Ps-Skqybk1HMA0gydRY5VhPoUc3PzL14ZbEbZ2gHa3yenlx1EJdlQl3ZMfT3fhk0gbJzV', start_index=8714)
Annotation(end_index=8728, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1iy6iELp2e7tJuSpq3aSpRIcgHv2947zN19giHlWfYDxueUgeiNa-w4bkcpseRg49ao6OjlR7ox4nkwVMNXqhos80D_97UWTpSYEBM1RNHNTDfJfuVQ==', start_index=8714)
Annotation(end_index=9290, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-Ug_C_EQv7KQ8VkCF8gRplFpyZ7BB0SLoaccdzFK6ip5ej9S4u6bRj0B9NSA8B13xfCCujXkncaN28lCqf2W8jiYcjIgM62i59myqhX8Q2S55hDwVd_PULQ-9qFww5v1K1zZhnbduYzt8cziusg==', start_index=9276)
Annotation(end_index=9290, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCus1n_LUkrKZA86ohYhu1_Cll7K1mPil_CZmgIFWMg4yvg3H61AOu60zNizK8JFmeNDVFENtVPyzx3f6M6v9CSN2j_cBNudzK0X8F55BxokTwX6lOTZowuOPh-84YGv1T6pnSgEmpe9ZRUq1QWgLP9XWO', start_index=9276)
Annotation(end_index=9912, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGClJ_TQtOY2jI6pyxMNNYC40ZqbXA22C9KFF60BYDUIw8hR69Y4hN3o7RskyFp7FLVEGM4NBp-H94BcW4VyP87kjSsBwX47dW-EvrHAef8bkJbyponOVYLOjMq9SyQG9R_CVYAc79TFcfX51_tI7J2yiE1_vUcjKY=', start_index=9898)
Annotation(end_index=9912, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfQs1ma6DfniFrFzDnqThKzOFaD2RlNIMiTVQA_STZxwbHX2u67zEGuqxI0CmAQm6lgvCe30D4nSifgYmqCZdqh8uuOcIlLkH0n5bbqlcErmPOEx2ojg==', start_index=9898)
Annotation(end_index=10329, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfQs1ma6DfniFrFzDnqThKzOFaD2RlNIMiTVQA_STZxwbHX2u67zEGuqxI0CmAQm6lgvCe30D4nSifgYmqCZdqh8uuOcIlLkH0n5bbqlcErmPOEx2ojg==', start_index=10319)
Annotation(end_index=10918, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFomO7mqD-fjlmYmQL7k514PFd-vOqwDV9BUxHJ1f1YWIG4oLtFKlhyMFTn6Z3PmeKoBB663eyqVazLuJfcscpzxu4xR55tDK0FhXQbouKy0KABXxCGKg==', start_index=10905)
Annotation(end_index=10918, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKBFAcSTOqz88Mwa6IQU1WIYq-RTx3ZcXQsGMyhIA8UhxYtYVwllYR-UGYSuYTzILvV-LZEM6goK2ry5pDuDk5wqAofa5xmziVCfb1XyR7bJlWb3UY6gInwYUxfREaJ9V9RfzJAHkoCG0UcZ348tD41-8IPPDk_DyEA9mfGajZ3DJx8YqdgcF_Im7aFjdJRRrmlycUzTn5S1IReC1k5brfUvfhqmHb7zYayP_hyAVFfIz_nPnZLnkxQL_ZIQw=', start_index=10905)
Annotation(end_index=11384, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpRGuOJDKBFur7wLJJCGB-VGZDPe5ab26S4vz3rubFg49MYFScLY4wVM3kOXcVhXqgXiN6ILFeU0usbYrwuHm-PmUZ0VwmnjwBKjasp_J1-v3Q5lrQ1lJietPGyrQ-lhxKSmrFvFg2EP8BOu0y2Wwxi_jrPOeC9e7Loy39ElB5bfEzBvkj', start_index=11375)
Annotation(end_index=12135, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFomO7mqD-fjlmYmQL7k514PFd-vOqwDV9BUxHJ1f1YWIG4oLtFKlhyMFTn6Z3PmeKoBB663eyqVazLuJfcscpzxu4xR55tDK0FhXQbouKy0KABXxCGKg==', start_index=12126)
Annotation(end_index=13675, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFomO7mqD-fjlmYmQL7k514PFd-vOqwDV9BUxHJ1f1YWIG4oLtFKlhyMFTn6Z3PmeKoBB663eyqVazLuJfcscpzxu4xR55tDK0FhXQbouKy0KABXxCGKg==', start_index=13666)
Annotation(end_index=13772, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1iy6iELp2e7tJuSpq3aSpRIcgHv2947zN19giHlWfYDxueUgeiNa-w4bkcpseRg49ao6OjlR7ox4nkwVMNXqhos80D_97UWTpSYEBM1RNHNTDfJfuVQ==', start_index=13762)
Annotation(end_index=13888, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAW9YDxDQedKLdTtjboVLKAvSw6tiKKvBPbP1wrWGVFQ22AB6bW_MUcKiF_jshZA_o4yT8nZy2E52SWtZb8sNRKKFbF3JOUljfCyk18_OA61hIIua86o7KK2QCxovQ1cUJDrA8JK82eP8SQuGg8Q==', start_index=13879)
Annotation(end_index=13952, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7qgp_FKmG679g-BLTDKVd6BE3yZJnM7Tz_dMlFa-g_v_axbXTye927jMvX8_T3a5_GHF9VRlppQBxFEB-DKzPhKUdGHEn7Uurok2lwP3og-AJ6IeStPWnmbhN4FhirpoMQcsSkLGd-sJoPcci1z4xtm9FjDYqhgd4kA==', start_index=13943)
Annotation(end_index=14039, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgh-XFCRjR6kwkMcIdEoPIhJcrwCOrhD9rZlcXRO7CI914Wl5ZXPUVHW8lIznVotS3hwbnQG9hS6evJileOHZbkY9kpWJXDFXlD8nvhWjkcPuBMihXOA==', start_index=14030)
Annotation(end_index=14131, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdcy8s9Cd0HwPBmSNRzh7OI7qX9KARxXNtnlf3Umqd74MIaNUiBctvdTepMVuF3qpLG_IFTpBUNMoqL5VCnI8cvVJCUIa7ArLHThVEKmodz6Bya4L_dF7dwr-DKxSIkjEMotzZVZiyUxEzSfRNHzgPnD4ZaaTKv80=', start_index=14121)
Annotation(end_index=14262, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpRGuOJDKBFur7wLJJCGB-VGZDPe5ab26S4vz3rubFg49MYFScLY4wVM3kOXcVhXqgXiN6ILFeU0usbYrwuHm-PmUZ0VwmnjwBKjasp_J1-v3Q5lrQ1lJietPGyrQ-lhxKSmrFvFg2EP8BOu0y2Wwxi_jrPOeC9e7Loy39ElB5bfEzBvkj', start_index=14253)
Annotation(end_index=14361, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGClJ_TQtOY2jI6pyxMNNYC40ZqbXA22C9KFF60BYDUIw8hR69Y4hN3o7RskyFp7FLVEGM4NBp-H94BcW4VyP87kjSsBwX47dW-EvrHAef8bkJbyponOVYLOjMq9SyQG9R_CVYAc79TFcfX51_tI7J2yiE1_vUcjKY=', start_index=14351)
Annotation(end_index=14475, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfQs1ma6DfniFrFzDnqThKzOFaD2RlNIMiTVQA_STZxwbHX2u67zEGuqxI0CmAQm6lgvCe30D4nSifgYmqCZdqh8uuOcIlLkH0n5bbqlcErmPOEx2ojg==', start_index=14465)
Annotation(end_index=14575, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSXbXIBr5XDbWTysSCj_1FGEWoylRoXlkUJIEk871EioKgzJq0xovi-D2-_S_9eRNJgG58mhZ9KsxQ8NjJNpjtFkSxy7pwXDWUuRJV5oKJlNDDCYu-W4lvwxQRvspAOFR2TIrX8rAUJj081x_jXGGiRqPjUwmwwsKwsbgGF1Pm7J2yxX5h_DDqghLIT-fojcklGik7ww==', start_index=14565)
Annotation(end_index=14644, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKBFAcSTOqz88Mwa6IQU1WIYq-RTx3ZcXQsGMyhIA8UhxYtYVwllYR-UGYSuYTzILvV-LZEM6goK2ry5pDuDk5wqAofa5xmziVCfb1XyR7bJlWb3UY6gInwYUxfREaJ9V9RfzJAHkoCG0UcZ348tD41-8IPPDk_DyEA9mfGajZ3DJx8YqdgcF_Im7aFjdJRRrmlycUzTn5S1IReC1k5brfUvfhqmHb7zYayP_hyAVFfIz_nPnZLnkxQL_ZIQw=', start_index=14634)
Annotation(end_index=14737, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6WpNJmi8qfDXrECAvp1WhpwMpa6u_azsPP-U6LHPOtdVxwJMElY9do3WcJxbCYd-Fwzbyh40ad17ssOo0Y1waephlI4LbvEoVpb0-r2-yxcw3in_WZg==', start_index=14728)
Annotation(end_index=14845, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-Ug_C_EQv7KQ8VkCF8gRplFpyZ7BB0SLoaccdzFK6ip5ej9S4u6bRj0B9NSA8B13xfCCujXkncaN28lCqf2W8jiYcjIgM62i59myqhX8Q2S55hDwVd_PULQ-9qFww5v1K1zZhnbduYzt8cziusg==', start_index=14835)
Annotation(end_index=14955, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1iy6iELp2e7tJuSpq3aSpRIcgHv2947zN19giHlWfYDxueUgeiNa-w4bkcpseRg49ao6OjlR7ox4nkwVMNXqhos80D_97UWTpSYEBM1RNHNTDfJfuVQ==', start_index=14945)

## Sources
