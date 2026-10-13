# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 2/5 | **Run ID:** 9995c96a | **Time:** 5460.40s | **Cost:** $0.89478
--------------------------------------------------------------------------------

# To What Extent Does the Numerical Stability of Overlapping Generations Models Influence the Convergence Speed of Welfare Redistribution Algorithms?

### Key Points
*   **Critical Dependency:** The convergence speed of welfare redistribution algorithms is fundamentally constrained by the numerical stability of the underlying Overlapping Generations (OLG) equilibrium solver. Instability in the "inner loop" (equilibrium resolution) causes noise or divergence in the "outer loop" (welfare maximization), often necessitating robust but computationally expensive global optimization techniques over faster gradient-based methods.
*   **Explosive Dynamics and Saddle Paths:** OLG models, particularly those with non-separable preferences or complex intergenerational transfers, are prone to "explosive dynamics" or indeterminacy. This forces algorithms to rely on time-intensive manifold tracking or "shooting" methods to remain on the stable saddle path, significantly slowing convergence compared to standard convex optimization problems.
*   **The Curse of Dimensionality:** Welfare redistribution often requires modeling heterogeneous agents (by age, skill, wealth). As state variables increase, tensor-product grids become computationally intractable. Numerical stability is recovered via sparse grid techniques (e.g., Smolyak grids), which reduce complexity from exponential to polynomial, thereby enabling convergence where standard methods fail.
*   **Algorithmic Trade-offs:** There is a direct inverse relationship between the robustness of an algorithm to numerical instability and its convergence speed. Gradient-based methods (Newton-Raphson) offer quadratic convergence but fail under non-convexities common in welfare systems (e.g., means-tested benefit notches). Conversely, Global Life-Cycle Optimizers (GLO) ensure stability and global optimality but require thousands of iterations, slowing the process from seconds to minutes or hours.
*   **Theoretical Limits:** Recent research indicates that welfare maximization problems possess a "regret bound" of $T^{2/3}$, making them theoretically harder and slower to converge than standard multi-armed bandit problems ($T^{1/2}$). This suggests that even with perfect numerical stability, the structural complexity of welfare redistribution imposes an intrinsic limit on convergence speed.

---

## 1. Introduction

The intersection of computational macroeconomics and public finance relies heavily on Overlapping Generations (OLG) models to simulate the long-run effects of fiscal policy. Unlike representative agent models, OLG frameworks capture the lifecycle dynamics of birth, work, retirement, and death, making them indispensable for analyzing intergenerational welfare redistribution, social security reform, and taxation [cite: 1, 2]. However, the utility of these models is contingent upon the ability to solve them numerically. As these models grow in complexity—incorporating heterogeneous agents, stochastic shocks, and non-linear tax schedules—the numerical stability of the solution algorithms becomes a paramount concern.

The query addresses the relationship between **numerical stability** and the **convergence speed** of algorithms designed to optimize welfare redistribution. This is a bi-level optimization problem: the "inner loop" must solve for the general equilibrium of the economy given a policy, while the "outer loop" searches the policy space (e.g., tax rates, transfer thresholds) to maximize a Social Welfare Function (SWF) [cite: 3, 4].

Research indicates that numerical stability is not merely a technical convenience but a determinant factor in whether a welfare algorithm converges in finite time or diverges into "explosive" dynamic paths [cite: 5, 6]. Instabilities arising from non-convex budget sets (common in welfare systems) or saddle-path sensitivity force researchers to abandon fast, derivative-based algorithms in favor of slower, stochastic global optimizers [cite: 7]. Consequently, the extent of the influence is profound: numerical instability can transform a polynomial-time optimization problem into one that is computationally intractable without advanced sparse-grid or machine-learning interventions.

## 2. The Numerical Architecture of OLG Models

To understand how stability influences convergence, one must first understand the mathematical structure of the OLG framework and the specific sources of instability inherent to it.

### 2.1 The Auerbach-Kotlikoff Tradition
The standard tool for analyzing fiscal policy is the Auerbach-Kotlikoff (AK) model. In this framework, the economy is populated by cohorts of agents who live for a finite number of periods (e.g., 60 to 80 years) [cite: 1, 8]. Agents maximize lifetime utility subject to intertemporal budget constraints, while firms maximize profits. The equilibrium is defined as a set of prices (wages and interest rates) such that markets clear in every period.

Mathematically, this results in a massive system of non-linear equations. For a model with $A$ cohorts and $T$ transition periods, the system size can easily exceed $A \times T$ variables. Solving this requires finding a fixed point in the price vector or the capital stock path [cite: 9, 10]. The "numerical stability" of an OLG model refers to the ability of the algorithm to maintain the system on the stable manifold (the saddle path) that leads to a steady state, resisting the natural tendency of the dynamic system to diverge towards infinity or zero capital stock [cite: 11, 12].

### 2.2 Sources of Instability
Instability in OLG models arises from three primary sources, each affecting welfare algorithms differently:

1.  **Saddle-Path Instability:** OLG models are difference equations that typically possess a "saddle point" property. For a unique stable equilibrium to exist, the number of stable eigenvalues (inside the unit circle) must match the number of predetermined variables (state variables). If numerical errors push the solution off this manifold, the path exhibits "explosive dynamics," leading to solver failure [cite: 5, 6].
2.  **Non-Convexities in Budget Sets:** Welfare redistribution often involves means-tested transfers, progressive tax brackets, and social security caps. These create "kinks" and "notches" in the household budget constraint, rendering the decision problem non-differentiable and non-convex [cite: 7]. Standard gradient-based solvers (like Newton-Raphson) become unstable or get stuck in local optima when facing these discontinuities.
3.  **Non-Separable Preferences:** When models incorporate habit formation (where utility depends on past consumption) or intergenerational altruism, the dynamic system becomes higher-order. Research shows that non-separable preferences can induce endogenous cycles or explosive dynamics even in optimal planning solutions, complicating the convergence of any algorithm attempting to find a welfare maximum [cite: 13, 14].

## 3. Welfare Redistribution as a Bi-Level Optimization Problem

The search for an optimal welfare redistribution policy is computationally modeled as a Stackelberg game or a bi-level optimization problem [cite: 3, 15].

### 3.1 The Outer and Inner Loops
*   **The Outer Loop (Government):** The algorithm searches for a vector of policy parameters $\theta$ (e.g., tax rates $\tau$, benefit levels $b$) to maximize a Social Welfare Function $W(V_1, V_2, ..., V_N)$, where $V_i$ is the indirect utility of agent $i$.
*   **The Inner Loop (Equilibrium):** For a fixed $\theta$, the algorithm must solve the OLG equilibrium. This involves households maximizing utility given $\theta$ and prices clearing markets.

### 3.2 Transmission of Instability
The convergence speed of the outer loop is strictly limited by the stability of the inner loop. If the inner loop is numerically unstable, the mapping from policy $\theta$ to welfare $W$ becomes "noisy" or discontinuous.
*   **Gradient Corruption:** Many efficient optimization algorithms (e.g., BFGS, steepest ascent) rely on calculating the gradient $\nabla_\theta W$. If the inner OLG solver has low numerical precision or jumps between multiple equilibria due to instability, the calculated gradient will be erroneous [cite: 16].
*   **Fallback to Derivative-Free Methods:** When gradients are unreliable due to inner-loop instability, researchers must resort to derivative-free methods like the Global Life-Cycle Optimizer (GLO) or genetic algorithms [cite: 7, 17]. While robust, these methods converge significantly slower. For instance, GLO may require thousands of function evaluations compared to dozens for a gradient method, increasing computation time from seconds to hours [cite: 7].

## 4. Influence of Numerical Stability on Convergence Speed

The extent of the influence of numerical stability on convergence speed can be categorized into three regimes: the "Curse of Dimensionality," the handling of "Explosive Dynamics," and the theoretical "Regret Bounds."

### 4.1 The Curse of Dimensionality and Sparse Grids
In welfare analysis, accurate redistribution requires modeling heterogeneity (rich vs. poor, lucky vs. unlucky). As the number of state variables (wealth, productivity, age) increases, the computational cost grows exponentially—the "curse of dimensionality" [cite: 18, 19].

*   **Tensor Product Instability:** Standard tensor-product grids become computationally infeasible and numerically unstable as dimensions rise. The interpolation errors in high-dimensional space can prevent the equilibrium conditions from closing, causing the welfare algorithm to loop indefinitely.
*   **Smolyak Grids:** To restore stability and speed, researchers employ Smolyak (sparse) grids. This technique reduces the number of grid points from $N^d$ (exponential) to a polynomial growth, maintaining numerical accuracy without the massive computational overhead [cite: 18].
*   **Impact on Speed:** By stabilizing the interpolation in high dimensions, Smolyak methods allow the welfare algorithm to converge. Research indicates that for high-dimensional models (e.g., >20 state variables), Smolyak methods are the *only* viable path to convergence, effectively reducing the "time to solution" from infinity (non-convergence) to a feasible timeframe [cite: 20, 21].

### 4.2 Managing Explosive Dynamics
OLG models are prone to "explosive dynamics" where the economy diverges from the steady state if the initial conditions are not perfectly placed on the saddle path [cite: 6, 22].

*   **Shooting Methods vs. Relaxation:** Traditional "shooting" methods (guessing initial values and iterating forward) are highly sensitive to numerical instability. A small error in the guess leads to rapid divergence (instability), forcing the algorithm to restart frequently with smaller steps. This results in slow linear convergence.
*   **Global Stability Approaches:** To counter this, modern algorithms use "relaxation" methods (solving the entire transition path simultaneously as a system of equations) or projection methods. While these are more stable, they involve inverting massive Jacobians. The stability of the Jacobian (its condition number) directly dictates the speed of the linear solver (e.g., GMRES or BiCGSTAB). An ill-conditioned (unstable) Jacobian requires effective preconditioning, otherwise, the convergence speed degrades significantly [cite: 19, 23].

### 4.3 Theoretical Limits: Regret Bounds
Recent theoretical work in algorithmic welfare maximization suggests that numerical stability issues impose a hard limit on learning rates.
*   **Regret Analysis:** In the context of learning the optimal welfare policy (bandit problems), the "regret" (the difference between optimal and realized welfare) typically scales with $T^{1/2}$ for standard problems. However, for welfare maximization involving complex feedback loops (like OLG), the regret bound is often worse, scaling with $T^{2/3}$ [cite: 24, 25].
*   **Implication:** This implies that welfare redistribution is structurally "harder" than standard optimization. Even with a stable solver, the convergence rate is sub-linear. If numerical instability introduces noise into the feedback signal (the "reward"), the regret bound degrades further, potentially preventing convergence to the global optimum entirely [cite: 26].

## 5. Algorithmic Solutions and Performance Trade-offs

The research highlights several specific algorithmic approaches used to mitigate instability, each with a distinct impact on convergence speed.

### 5.1 Global Life-Cycle Optimizer (GLO)
The GLO is specifically designed to handle the numerical instabilities caused by the non-differentiable tax and benefit schedules inherent in welfare redistribution [cite: 7, 27].
*   **Mechanism:** It uses a stochastic pattern-search algorithm that does not rely on gradients. It is robust to "earnings flipping" and "bunching" at kink points, which cause standard solvers to crash.
*   **Speed Impact:** The trade-off is speed. While a Newton-based solver might converge in fewer than 50 iterations, GLO often requires over 5,000 iterations to meet convergence criteria [cite: 7]. However, because it avoids getting stuck in local optima (a form of stability failure), it is often the only way to find the true global welfare maximum in complex fiscal environments.

### 5.2 GPU Acceleration and Parallelization
To offset the slow convergence caused by the need for robust, stable algorithms, researchers have turned to hardware acceleration.
*   **Parallelization:** OLG models with heterogeneous agents are "embarrassingly parallel" in the household step. Solving for 400,000 different household types can be distributed across GPU cores.
*   **Performance:** Research shows that using NVIDIA Tesla GPUs can reduce the solution time for the household block to approximately 30 seconds per iteration [cite: 28]. This hardware stability allows for the use of more computationally intensive (but numerically stable) algorithms without incurring prohibitive time costs.

### 5.3 Damped Fixed-Point Iteration
A common technique to induce stability in the equilibrium transition path is "damping." Instead of updating the capital stock fully to the new implied value ($K_{new}$), the algorithm updates to a weighted average: $K_{next} = \lambda K_{new} + (1-\lambda) K_{old}$.
*   **Influence:** While damping prevents explosive oscillations (increasing stability), it linearly reduces convergence speed. A high damping factor (close to 1) is often required for unstable OLG models, which can increase the number of iterations required by an order of magnitude [cite: 9, 23].

## 6. Case Studies in Welfare Redistribution

### 6.1 Social Security and Pension Reform
In models analyzing the transition from Pay-As-You-Go to funded pension systems, the transition path is long (decades). Small numerical instabilities in the early years of the simulation propagate and amplify over the transition [cite: 29].
*   **Result:** Algorithms must employ "time-stacking" (solving for all periods simultaneously) to ensure the terminal condition (steady state) anchors the path. This stabilizes the solution but requires solving a system of equations that is $T$ times larger, impacting memory and speed [cite: 1, 19].

### 6.2 Means-Tested Transfers
Welfare programs often have high effective marginal tax rates at withdrawal points (poverty traps). This creates non-convex budget sets.
*   **Instability:** Standard Euler-equation based solvers fail here because the first-order conditions are not sufficient (or defined) at the kinks.
*   **Solution:** Discrete Value Function Iteration (VFI) or GLO must be used. VFI is numerically stable (contraction mapping) but suffers severely from the curse of dimensionality. GLO provides a middle ground but still represents a significant slowdown compared to smooth models [cite: 7].

## 7. Conclusion

The numerical stability of Overlapping Generations models exerts a **dominant and constraining influence** on the convergence speed of welfare redistribution algorithms. This influence manifests through three primary mechanisms:

1.  **Algorithmic Selection:** Instability forces the abandonment of fast, gradient-based algorithms (quadratic convergence) in favor of robust, derivative-free, or global optimization methods (linear or sub-linear convergence). This substitution alone can increase computation time by orders of magnitude [cite: 7].
2.  **Damping Requirements:** To contain explosive dynamics and maintain saddle-path stability, solvers often require heavy damping or complex manifold tracking. This artificially slows the iterative process to prevent divergence [cite: 6, 9].
3.  **Dimensionality Constraints:** The need for stability in high-dimensional heterogeneous agent models necessitates the use of sparse grid techniques (Smolyak). While these techniques enable convergence where tensor grids fail, they introduce their own computational overhead compared to simple low-dimensional approximations [cite: 18].

In summary, numerical stability is the "bottleneck" of computational welfare analysis. The speed of finding an optimal redistribution policy is not primarily limited by hardware speed, but by the mathematical necessity of navigating a precarious dynamic landscape without falling into explosive paths or local optima. As models become more realistic (and thus more unstable), the reliance on computationally intensive global optimizers like GLO and hardware acceleration (GPUs) will likely increase, cementing the trade-off between stability and speed.

## References

*   **[cite: 1]** Fiskalrat Austria. (2021). *WP7-FISK_OLG_Model_2021.pdf*.
*   **[cite: 8]** Heer, B., & Maussner, A. (2020). *Social Security in Dynamic General Equilibrium*.
*   **[cite: 2]** Kotlikoff, L. J. (1998). *The A-K Model: Its Past, Present, and Future*. NBER Working Paper.
*   **[cite: 19]** Ozbilgin, M. (2023). *OLG Solution Method*.
*   **[cite: 9]** QuantEcon. (2025). *Overlapping Generations Model*.
*   **[cite: 23]** Ludwig, A. (2015). *Efficient solution of OLG models*.
*   **[cite: 11]** Acemoglu, D. (2011). *Lecture Notes on OLG Stability*.
*   **[cite: 10]** Acemoglu, D. (2011). *Economic Growth Lecture 8*.
*   **[cite: 5]** Marini, G. (2022). *Dynamics and stability in an olg model with non-separable preferences*.
*   **[cite: 13]** Marini, G. (2022). *Dynamics and stability in an OLG model*. RIEDS.
*   **[cite: 24]** Kasy, M. (2024). *Adaptive Maximization of Social Welfare*.
*   **[cite: 16]** Chen, T., et al. (2024). *Convergence of the outer loop iteration*.
*   **[cite: 25]** Kasy, M. (2025). *Adaptive Maximization of Social Welfare*.
*   **[cite: 7]** Brumm, J., et al. (2024). *The Global Life-Cycle Optimizer*. NBER.
*   **[cite: 18]** Judd, K., et al. (2014). *Smolyak Method for Solving Dynamic Economic Models*.
*   **[cite: 3]** Hosseini, et al. (2022). *Bi-level optimization for OLG and Demand Response*.
*   **[cite: 6]** Marini, G. (2015). *Explosive dynamics in OLG models*.
*   **[cite: 19]** Ozbilgin, M. (2020). *Solution methods for OLG models*.
*   **[cite: 28]** Jin, Y. (2020). *Stochastic OLG Models and Transition Path using GPU*.
*   **[cite: 7]** Brumm, J., et al. (2024). *The Global Life-Cycle Optimizer*.

**Sources:**
1. [fiskalrat.at](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpuRGfKP9mKIlEnB8Zi-qOyIyhzXZZgytIEMVl1IjeXDkfQak1NzHm3QPy3NoX7H1dWFr9sFwIarpI0vLqKhsSOG7eaaT7xOMay-VjHBFSnfaSPwvgzjoicoENPF7_vxiinkw5zg5asO8nC-SUpkZebW0adYl4RVtJmqjVo64ejML19JMWoDtEUg-C7NP2sBSQWwELTz2u)
2. [nber.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMPsO1ImZhCOGeETT_2VoC5um8ktT3pP3PRcruF4fAncftvMri3XEPdHA1jCt16Wg7j7z-qwbLcRQY4QnwD73O3aUlRJvkMDgH-Pq4BY6nOoP_T4ic4rv_KLvvDJEKDset-V45Nw-lGxrAkfnyGC2YrJf0qJST)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtfT2iGSNfSoxxkQ2MyM2-hrUjYJ5EjcD_vqnNtQaFPMv-VZsQSdao2s4NDtviGtJQKk-ye9SolODuoXke29RmIA1OtAqqXo_dxF8DiQZViF-qC_wf5ay63ii7j1E6vZ77VXs6FGQqC8l7wzH7As0s2klghJpQp4t9EsRsdf4s2qLt8_RMDhG04EMcXTrCo5oSkOP7XikWiZ4xYS6UqJhVuZs_cG-t2gQVnjuo4AOmhjQ9OjXqbKcGIZrudrTbJTYHLqvyiLNTvFEAueZ8SA==)
4. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLVnld5zN5g_tI0cs4Zs-nijtS4NTnLMcZsky9Dm52Mcgmj03Xdu7UiV3fvZxF3UVDsTocAyoen6oMiQ6jLlhD9jJwz7Y7VNPnuRaDwiKd7qOmX4jYRc8BDQ==)
5. [uniroma1.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnyBN3lhgxvvY2OvaBw67hFc-JzyrwaUmTtxasxQFI1SOnFwK_7HH4VV3rIwGQDdmvkUJx0VA0J5lUK4zOC_4rW8LdSLL845Yc_c3U7JtTSg-XQl3VWolCOS6GjmKO-sLnuao=)
6. [uniroma1.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKA-TrEZHZQZ0XEs46aKSgz17DBYaIn0zr4qrvvk0W3TfFbqhtiF83xAF5eCtH55a9V1xNB6XlTq4yJt7C2fUbzkJxclmX0MEGtm8J6Dsb-pN8_2f8goLHcx0Gf1NEFndSmLSN1A3I7xKERiuVylvZRlcWCIMRGWyDAOlm8RmSJks-5ag6kBRq6K5tTO7Ba9dCpQdnIZgzciHNjOLv)
7. [kotlikoff.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcyfatAisrdOB9cerd0a7lw5abrR0uJ-790QmpwK78gWAv3C1FF9IkjOjA0cImaE2u7zkctqmeJfGqIS88iFEWZHUe7vH6VSOm2a4WnXbayPwvcPHs99Flzpa6RX4XJDHwMj3wtc3L63iOyhRQ0whSXlY6-rCIfbVGH2cHpFQRfI4V6Vo1vZyxJZc=)
8. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEs0d6BLXMxE3hJm3d81BjU8LzWpCRce_m4jT2Hmu4D32_uTbqOJJ72j4TEb-81qTqLFCHU3MI_OD5cHDtM5o5n52kN1vS81NAVj0as-4fzbw65HuQ_GHeWUmxpyTM6aqwt)
9. [quantecon.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGF5yMSEaxzHvh_gNuQEySMcbTzrWGm0mAYZjmIGSZLRYBrLUI7HSX3l1g-61sjpHb6ZmGqUC5jYwcf__bGvIzWWw1vhQlhSAA4um46w73_R3IS2TVIq1_oKOg=)
10. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE25IuAuiHm9uRIbb5ZuQdshETp2GokmJO7jnepXMBbZAm77tkqlfeZ-0peQrh_sy-RoJlhp6nSQnmPvJkufnMQrCy7ry0mMYdLrhp4Pb33L-a9VEsGt67w-6wy6530NLBnSmys7p7p9tg8X-U6Ym5iLdexRHH7GRb-DHnrMlUUlpsXNyWULZCobvWK84VJi3ISxObSSm8GytdVc91mLnZa6yQ=)
11. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEKab7PLI_TKtae_adlsy0MSCIfZNs5cTYIDnGJPdxzK4A062n0-a_E2_wxfmb0PPzfJTnIaaGaMy8urGp9EkYFw1exP2dB_V6Mykq6uLOge9CCQjyFsieLwNLmvOifa9nsJ6vqp19I6VOaC0=)
12. [berkeley.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGel3z968OTrXJl3mIjn_D9ji5Yss6IlYzH48PMRyX8xeXaLhOFC7cdAPOXr66cwmMJLtzDECITir4_DD-tsqjCd4E6A1fbDvchl9a9V4Sk1lrcCJNDdopTCkmN296WbGUhNb5ztARVbVXCTQ==)
13. [sieds.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKakzxUWoVeDV6CztTfIGFPb0bgnOTk7IvKFl7h_SBGSrJD9e3bw7aro3oi0ERkA5N_D3UbxJZefE5uAFuHCDQMnXyAdtreEN5igEGcsJ-Ivv-zjFjnp3fID-yB_dHj5K5Jj3ZwXshSCvoQNZOf0ZxwOZj7oQ=)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqwxf8MyX9t8pr9G3WmHOnLdtXuVkCsc0Ao2ddb6pVV45kt2Qg9XYzceJUEzFOQIICIqqGigwEm1zGVnrYih8iEeO0eK1q46-YPULfLl3NtG-2b4LarVM8sJPXoBqG3j6n6pCXPns5FzSRN5E2ttFJA-x8j8rO4-GvJQAvZpP9zD0SG7lQUSS1hQWBtKnMtEXvP0TYG8oCC74Uwv05h8_iJDzC6SdFbIRljSpX0OI=)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6cpYf8LNUOVHdV4FMyV6g0EAs9idRc1shNZ-VmEIsKr_Hgt1fFbZxmU2WWjHwMe0p5FIYeW2-WGWEwMxsbbDUDuPlY8vQAZRfI8JPU9yndRxBgo6VuhTMyQopDloHzcidbp0H6tIIolxj0Q9bAjLYgEFjwwqPL8b74neGAHntATA63rw9zB445skUqo30fTFf8VTQ7MAshuhKMwBdJfzYVgEOfenaWXmoHfMyGe9hBV_CNUE=)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFufSltDxVsgqKfkOzpmErEQ59vpVjTTMbd1rEjBBPND-qlfTkiTArCAUmxkOo_iCzgholNVjy1z5McSAACyypYpen1ZqC28zFIMWriFZMipIoPV8_LuC7G6M_fedly6TuVAmoZLo9wMOROBfxutGXYNvyeYV3V_T3j51ECAzZUMNoQI-kQ-GkYf9kFR1WRROk=)
17. [unimelb.edu.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNPCIJ8bj9KLMlerjgPNnBne7H600i3kKyCg1te_YZLn1fef1wt8xDplWAZ2XBGHyc_jhjIsLVM2pBZu-FknZxUIYOso1dv7P0DoRftkt32xtQqKWkcCVi5u4GiC6G1CHR9NueCl0MeulI3t5O_DbzPk1AhMFHpJhtxQ==)
18. [uchicago.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2Q4v_8hABLQa8Yq5_Y5glel9csA4aQsAo9hoC9ZekvW8L1U8Tc79IH1OGHS1NWGZv4vkIQQI5Jq3W4kcVX6e_6RZtYLzV1tUt0OTIzscdDaMvxCEC1LUkdj3FvAfY5Jmbda6RRQGmtk33AqgSFBnnVFMDsfaGZqpgLA==)
19. [muratozbilgin.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFw5DjRoVYWNwBnkAHUsVRFfUBdwuUb3Wia4byqYKOukWvuXi3c14xdq5kJH51M8rd7hFV1zlCK94GrEJ5a8NtvjS-T4WtiMfXXcTJIyM_3KmWj2DZdZR71BAud9DW1Cs8OGWE4vl3J)
20. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHu2jUoBteSb2PKqX0p0_S4j8Al_ZZ_jwqcw9P5PTVDbmv1M6OVldY3k2gVgPVG5domB5D7rKq7HjRzLUWOo5TrwZWXIdzM0vcXsrY_y0jHrxBDvRif4SOsLypCbmrLPNJf07dBIWy_YaOsuA==)
21. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF00J-qisVMU67LhRWxETYRZx3LsZzu8sxLjgEqqdIQSp6u_i5Ith4RDedRtvUBXnPabvGLB9EOZpFcxb7p9IDGm81Me7297_ik4Hex5sMYCbfR2KIG2E6ltRbaXnutv3Du9KYYZYagTIsOPI6C-90s0g==)
22. [rieds-journal.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnkIojGwezDOfyR9cnR5fdu6jDvIib1JczmG9IkJCnALXs4zZ80I_3MqGtUOFXY6CsRKd74OIlEW5bIOUNywCHAg2FF1CDxHGjcKGs93ujNhAp3HnDtH-TOf30g1Mrrm8OrECfUsPSVShb4RmoVWJFX2vGrlC_)
23. [econstor.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwkxFtK1gTPk486CDeJBIAjh7YRtN4EwHZ4tImbIxpSMvn37MfHxfoMPKrHNJGaOmDZJklsDwRO6MFvW7gdK-muiJ1FWc3_0nPYCIhSH9SZ2FCOpJlNGyPRDlG7iMRowAzgrWNKcEM4qKkVIHPh7SU58ZHXQ==)
24. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqKDmTg1gadzlbMuHpe8JRde8lQ2xZT8fap4zLTDR19vAkQJeM55Ow5MFV8FTB1-2ZlbMGvRbMgISb-rGZrUxEmjMtHd1qBGRqiAXLnke-YvH_ExnQ7nCptQhtLz1XlyyQHq6gUE3iud1np3lCF3AoWyQUZstyCceJmTR0nw==)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVHbzXg4RRN359Hscj7AjhCGNPulUuHuoqMmEXlv7BvbHSWzP53o0xj_IS4f8nHxg5GziIj1Qs76N0aYHREBy4HjPFozH-148JxJqYCcqEpvnjTee32VWSrU4GE3pCD9HNn6ycSFmtPtisBV1BB08M_fE6-KMRxaHD43Om_gpC-VxVxmRJwCBM5QrVyvdyjpg=)
26. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELqNI4A1trdZhjAaObdUOalrQsKXtwPqw8x7IaD4EQMqZVsT3Te3GQZOXyI4mnBHA4dOzcZOWLO5hPgMx0L_pWAg9ji_SbKwnoeCp_1vMGHyNw_lYrnX3KQa8=)
27. [kotlikoff.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC2g3sDNaDrSjHbPlLBf3hYA-prCF6qAjwwRwFqT-nunAHCOIc9EvV0QnlvpMOM_sjjldIqa4gnZR8_h3QyGGPx0bw8k_KqY4KbHyDE5Ir_iT72QVpu7vT6IIpNneEsENbQHZteSYLsI2SdM-J0zgVmwteqLBWz0Tp)
28. [upenn.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOqT_7s3t5vTBHqqTsuKQPP6BouQfwZlpF5tGLA0UvXdOypG7pvjfVu57M19vClPRTgzPZQwgfHmq32sVtw9shnemO6o3djrWZBsP3O9DPPKTLtEX9cE_Mh6IKtWS7TzznkFmTALgBQ2_3CjqNwcKGuIIFX2z0GECIisiBXvr6M3WfHKkuJctnXma3)
29. [uni-muenchen.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkkEX147smfsEP-1LAdYjPVmJIPtZTC5GgaYNkQJJnohnNc0iuWFcxLUs-jIwmRW7jvzq6eQLYQErvHcw8oZk9k1ZbphYL7Vk4OA1CMkVzvq3O3Kh9zQ8JXoTBHZWoohiQWXENMbasizAVZqWVLX8Rb6VRRg==)


## Annotations
Annotation(end_index=2805, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpuRGfKP9mKIlEnB8Zi-qOyIyhzXZZgytIEMVl1IjeXDkfQak1NzHm3QPy3NoX7H1dWFr9sFwIarpI0vLqKhsSOG7eaaT7xOMay-VjHBFSnfaSPwvgzjoicoENPF7_vxiinkw5zg5asO8nC-SUpkZebW0adYl4RVtJmqjVo64ejML19JMWoDtEUg-C7NP2sBSQWwELTz2u', start_index=2793)
Annotation(end_index=2805, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMPsO1ImZhCOGeETT_2VoC5um8ktT3pP3PRcruF4fAncftvMri3XEPdHA1jCt16Wg7j7z-qwbLcRQY4QnwD73O3aUlRJvkMDgH-Pq4BY6nOoP_T4ic4rv_KLvvDJEKDset-V45Nw-lGxrAkfnyGC2YrJf0qJST', start_index=2793)
Annotation(end_index=3536, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLVnld5zN5g_tI0cs4Zs-nijtS4NTnLMcZsky9Dm52Mcgmj03Xdu7UiV3fvZxF3UVDsTocAyoen6oMiQ6jLlhD9jJwz7Y7VNPnuRaDwiKd7qOmX4jYRc8BDQ==', start_index=3524)
Annotation(end_index=3536, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtfT2iGSNfSoxxkQ2MyM2-hrUjYJ5EjcD_vqnNtQaFPMv-VZsQSdao2s4NDtviGtJQKk-ye9SolODuoXke29RmIA1OtAqqXo_dxF8DiQZViF-qC_wf5ay63ii7j1E6vZ77VXs6FGQqC8l7wzH7As0s2klghJpQp4t9EsRsdf4s2qLt8_RMDhG04EMcXTrCo5oSkOP7XikWiZ4xYS6UqJhVuZs_cG-t2gQVnjuo4AOmhjQ9OjXqbKcGIZrudrTbJTYHLqvyiLNTvFEAueZ8SA==', start_index=3524)
Annotation(end_index=3757, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKA-TrEZHZQZ0XEs46aKSgz17DBYaIn0zr4qrvvk0W3TfFbqhtiF83xAF5eCtH55a9V1xNB6XlTq4yJt7C2fUbzkJxclmX0MEGtm8J6Dsb-pN8_2f8goLHcx0Gf1NEFndSmLSN1A3I7xKERiuVylvZRlcWCIMRGWyDAOlm8RmSJks-5ag6kBRq6K5tTO7Ba9dCpQdnIZgzciHNjOLv', start_index=3745)
Annotation(end_index=3757, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnyBN3lhgxvvY2OvaBw67hFc-JzyrwaUmTtxasxQFI1SOnFwK_7HH4VV3rIwGQDdmvkUJx0VA0J5lUK4zOC_4rW8LdSLL845Yc_c3U7JtTSg-XQl3VWolCOS6GjmKO-sLnuao=', start_index=3745)
Annotation(end_index=3985, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcyfatAisrdOB9cerd0a7lw5abrR0uJ-790QmpwK78gWAv3C1FF9IkjOjA0cImaE2u7zkctqmeJfGqIS88iFEWZHUe7vH6VSOm2a4WnXbayPwvcPHs99Flzpa6RX4XJDHwMj3wtc3L63iOyhRQ0whSXlY6-rCIfbVGH2cHpFQRfI4V6Vo1vZyxJZc=', start_index=3976)
Annotation(end_index=4723, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpuRGfKP9mKIlEnB8Zi-qOyIyhzXZZgytIEMVl1IjeXDkfQak1NzHm3QPy3NoX7H1dWFr9sFwIarpI0vLqKhsSOG7eaaT7xOMay-VjHBFSnfaSPwvgzjoicoENPF7_vxiinkw5zg5asO8nC-SUpkZebW0adYl4RVtJmqjVo64ejML19JMWoDtEUg-C7NP2sBSQWwELTz2u', start_index=4711)
Annotation(end_index=4723, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEs0d6BLXMxE3hJm3d81BjU8LzWpCRce_m4jT2Hmu4D32_uTbqOJJ72j4TEb-81qTqLFCHU3MI_OD5cHDtM5o5n52kN1vS81NAVj0as-4fzbw65HuQ_GHeWUmxpyTM6aqwt', start_index=4711)
Annotation(end_index=5240, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE25IuAuiHm9uRIbb5ZuQdshETp2GokmJO7jnepXMBbZAm77tkqlfeZ-0peQrh_sy-RoJlhp6nSQnmPvJkufnMQrCy7ry0mMYdLrhp4Pb33L-a9VEsGt67w-6wy6530NLBnSmys7p7p9tg8X-U6Ym5iLdexRHH7GRb-DHnrMlUUlpsXNyWULZCobvWK84VJi3ISxObSSm8GytdVc91mLnZa6yQ=', start_index=5227)
Annotation(end_index=5240, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGF5yMSEaxzHvh_gNuQEySMcbTzrWGm0mAYZjmIGSZLRYBrLUI7HSX3l1g-61sjpHb6ZmGqUC5jYwcf__bGvIzWWw1vhQlhSAA4um46w73_R3IS2TVIq1_oKOg=', start_index=5227)
Annotation(end_index=5534, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEKab7PLI_TKtae_adlsy0MSCIfZNs5cTYIDnGJPdxzK4A062n0-a_E2_wxfmb0PPzfJTnIaaGaMy8urGp9EkYFw1exP2dB_V6Mykq6uLOge9CCQjyFsieLwNLmvOifa9nsJ6vqp19I6VOaC0=', start_index=5520)
Annotation(end_index=5534, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGel3z968OTrXJl3mIjn_D9ji5Yss6IlYzH48PMRyX8xeXaLhOFC7cdAPOXr66cwmMJLtzDECITir4_DD-tsqjCd4E6A1fbDvchl9a9V4Sk1lrcCJNDdopTCkmN296WbGUhNb5ztARVbVXCTQ==', start_index=5520)
Annotation(end_index=6099, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKA-TrEZHZQZ0XEs46aKSgz17DBYaIn0zr4qrvvk0W3TfFbqhtiF83xAF5eCtH55a9V1xNB6XlTq4yJt7C2fUbzkJxclmX0MEGtm8J6Dsb-pN8_2f8goLHcx0Gf1NEFndSmLSN1A3I7xKERiuVylvZRlcWCIMRGWyDAOlm8RmSJks-5ag6kBRq6K5tTO7Ba9dCpQdnIZgzciHNjOLv', start_index=6087)
Annotation(end_index=6099, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnyBN3lhgxvvY2OvaBw67hFc-JzyrwaUmTtxasxQFI1SOnFwK_7HH4VV3rIwGQDdmvkUJx0VA0J5lUK4zOC_4rW8LdSLL845Yc_c3U7JtTSg-XQl3VWolCOS6GjmKO-sLnuao=', start_index=6087)
Annotation(end_index=6400, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcyfatAisrdOB9cerd0a7lw5abrR0uJ-790QmpwK78gWAv3C1FF9IkjOjA0cImaE2u7zkctqmeJfGqIS88iFEWZHUe7vH6VSOm2a4WnXbayPwvcPHs99Flzpa6RX4XJDHwMj3wtc3L63iOyhRQ0whSXlY6-rCIfbVGH2cHpFQRfI4V6Vo1vZyxJZc=', start_index=6391)
Annotation(end_index=6957, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqwxf8MyX9t8pr9G3WmHOnLdtXuVkCsc0Ao2ddb6pVV45kt2Qg9XYzceJUEzFOQIICIqqGigwEm1zGVnrYih8iEeO0eK1q46-YPULfLl3NtG-2b4LarVM8sJPXoBqG3j6n6pCXPns5FzSRN5E2ttFJA-x8j8rO4-GvJQAvZpP9zD0SG7lQUSS1hQWBtKnMtEXvP0TYG8oCC74Uwv05h8_iJDzC6SdFbIRljSpX0OI=', start_index=6943)
Annotation(end_index=6957, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKakzxUWoVeDV6CztTfIGFPb0bgnOTk7IvKFl7h_SBGSrJD9e3bw7aro3oi0ERkA5N_D3UbxJZefE5uAFuHCDQMnXyAdtreEN5igEGcsJ-Ivv-zjFjnp3fID-yB_dHj5K5Jj3ZwXshSCvoQNZOf0ZxwOZj7oQ=', start_index=6943)
Annotation(end_index=7178, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtfT2iGSNfSoxxkQ2MyM2-hrUjYJ5EjcD_vqnNtQaFPMv-VZsQSdao2s4NDtviGtJQKk-ye9SolODuoXke29RmIA1OtAqqXo_dxF8DiQZViF-qC_wf5ay63ii7j1E6vZ77VXs6FGQqC8l7wzH7As0s2klghJpQp4t9EsRsdf4s2qLt8_RMDhG04EMcXTrCo5oSkOP7XikWiZ4xYS6UqJhVuZs_cG-t2gQVnjuo4AOmhjQ9OjXqbKcGIZrudrTbJTYHLqvyiLNTvFEAueZ8SA==', start_index=7165)
Annotation(end_index=7178, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6cpYf8LNUOVHdV4FMyV6g0EAs9idRc1shNZ-VmEIsKr_Hgt1fFbZxmU2WWjHwMe0p5FIYeW2-WGWEwMxsbbDUDuPlY8vQAZRfI8JPU9yndRxBgo6VuhTMyQopDloHzcidbp0H6tIIolxj0Q9bAjLYgEFjwwqPL8b74neGAHntATA63rw9zB445skUqo30fTFf8VTQ7MAshuhKMwBdJfzYVgEOfenaWXmoHfMyGe9hBV_CNUE=', start_index=7165)
Annotation(end_index=8239, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFufSltDxVsgqKfkOzpmErEQ59vpVjTTMbd1rEjBBPND-qlfTkiTArCAUmxkOo_iCzgholNVjy1z5McSAACyypYpen1ZqC28zFIMWriFZMipIoPV8_LuC7G6M_fedly6TuVAmoZLo9wMOROBfxutGXYNvyeYV3V_T3j51ECAzZUMNoQI-kQ-GkYf9kFR1WRROk=', start_index=8229)
Annotation(end_index=8476, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNPCIJ8bj9KLMlerjgPNnBne7H600i3kKyCg1te_YZLn1fef1wt8xDplWAZ2XBGHyc_jhjIsLVM2pBZu-FknZxUIYOso1dv7P0DoRftkt32xtQqKWkcCVi5u4GiC6G1CHR9NueCl0MeulI3t5O_DbzPk1AhMFHpJhtxQ==', start_index=8463)
Annotation(end_index=8476, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcyfatAisrdOB9cerd0a7lw5abrR0uJ-790QmpwK78gWAv3C1FF9IkjOjA0cImaE2u7zkctqmeJfGqIS88iFEWZHUe7vH6VSOm2a4WnXbayPwvcPHs99Flzpa6RX4XJDHwMj3wtc3L63iOyhRQ0whSXlY6-rCIfbVGH2cHpFQRfI4V6Vo1vZyxJZc=', start_index=8463)
Annotation(end_index=8702, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcyfatAisrdOB9cerd0a7lw5abrR0uJ-790QmpwK78gWAv3C1FF9IkjOjA0cImaE2u7zkctqmeJfGqIS88iFEWZHUe7vH6VSOm2a4WnXbayPwvcPHs99Flzpa6RX4XJDHwMj3wtc3L63iOyhRQ0whSXlY6-rCIfbVGH2cHpFQRfI4V6Vo1vZyxJZc=', start_index=8693)
Annotation(end_index=9311, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFw5DjRoVYWNwBnkAHUsVRFfUBdwuUb3Wia4byqYKOukWvuXi3c14xdq5kJH51M8rd7hFV1zlCK94GrEJ5a8NtvjS-T4WtiMfXXcTJIyM_3KmWj2DZdZR71BAud9DW1Cs8OGWE4vl3J', start_index=9297)
Annotation(end_index=9311, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2Q4v_8hABLQa8Yq5_Y5glel9csA4aQsAo9hoC9ZekvW8L1U8Tc79IH1OGHS1NWGZv4vkIQQI5Jq3W4kcVX6e_6RZtYLzV1tUt0OTIzscdDaMvxCEC1LUkdj3FvAfY5Jmbda6RRQGmtk33AqgSFBnnVFMDsfaGZqpgLA==', start_index=9297)
Annotation(end_index=9895, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2Q4v_8hABLQa8Yq5_Y5glel9csA4aQsAo9hoC9ZekvW8L1U8Tc79IH1OGHS1NWGZv4vkIQQI5Jq3W4kcVX6e_6RZtYLzV1tUt0OTIzscdDaMvxCEC1LUkdj3FvAfY5Jmbda6RRQGmtk33AqgSFBnnVFMDsfaGZqpgLA==', start_index=9885)
Annotation(end_index=10286, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF00J-qisVMU67LhRWxETYRZx3LsZzu8sxLjgEqqdIQSp6u_i5Ith4RDedRtvUBXnPabvGLB9EOZpFcxb7p9IDGm81Me7297_ik4Hex5sMYCbfR2KIG2E6ltRbaXnutv3Du9KYYZYagTIsOPI6C-90s0g==', start_index=10272)
Annotation(end_index=10286, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHu2jUoBteSb2PKqX0p0_S4j8Al_ZZ_jwqcw9P5PTVDbmv1M6OVldY3k2gVgPVG5domB5D7rKq7HjRzLUWOo5TrwZWXIdzM0vcXsrY_y0jHrxBDvRif4SOsLypCbmrLPNJf07dBIWy_YaOsuA==', start_index=10272)
Annotation(end_index=10502, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnkIojGwezDOfyR9cnR5fdu6jDvIib1JczmG9IkJCnALXs4zZ80I_3MqGtUOFXY6CsRKd74OIlEW5bIOUNywCHAg2FF1CDxHGjcKGs93ujNhAp3HnDtH-TOf30g1Mrrm8OrECfUsPSVShb4RmoVWJFX2vGrlC_', start_index=10489)
Annotation(end_index=10502, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKA-TrEZHZQZ0XEs46aKSgz17DBYaIn0zr4qrvvk0W3TfFbqhtiF83xAF5eCtH55a9V1xNB6XlTq4yJt7C2fUbzkJxclmX0MEGtm8J6Dsb-pN8_2f8goLHcx0Gf1NEFndSmLSN1A3I7xKERiuVylvZRlcWCIMRGWyDAOlm8RmSJks-5ag6kBRq6K5tTO7Ba9dCpQdnIZgzciHNjOLv', start_index=10489)
Annotation(end_index=11387, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFw5DjRoVYWNwBnkAHUsVRFfUBdwuUb3Wia4byqYKOukWvuXi3c14xdq5kJH51M8rd7hFV1zlCK94GrEJ5a8NtvjS-T4WtiMfXXcTJIyM_3KmWj2DZdZR71BAud9DW1Cs8OGWE4vl3J', start_index=11373)
Annotation(end_index=11387, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwkxFtK1gTPk486CDeJBIAjh7YRtN4EwHZ4tImbIxpSMvn37MfHxfoMPKrHNJGaOmDZJklsDwRO6MFvW7gdK-muiJ1FWc3_0nPYCIhSH9SZ2FCOpJlNGyPRDlG7iMRowAzgrWNKcEM4qKkVIHPh7SU58ZHXQ==', start_index=11373)
Annotation(end_index=11941, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVHbzXg4RRN359Hscj7AjhCGNPulUuHuoqMmEXlv7BvbHSWzP53o0xj_IS4f8nHxg5GziIj1Qs76N0aYHREBy4HjPFozH-148JxJqYCcqEpvnjTee32VWSrU4GE3pCD9HNn6ycSFmtPtisBV1BB08M_fE6-KMRxaHD43Om_gpC-VxVxmRJwCBM5QrVyvdyjpg=', start_index=11927)
Annotation(end_index=11941, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqKDmTg1gadzlbMuHpe8JRde8lQ2xZT8fap4zLTDR19vAkQJeM55Ow5MFV8FTB1-2ZlbMGvRbMgISb-rGZrUxEmjMtHd1qBGRqiAXLnke-YvH_ExnQ7nCptQhtLz1XlyyQHq6gUE3iud1np3lCF3AoWyQUZstyCceJmTR0nw==', start_index=11927)
Annotation(end_index=12315, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELqNI4A1trdZhjAaObdUOalrQsKXtwPqw8x7IaD4EQMqZVsT3Te3GQZOXyI4mnBHA4dOzcZOWLO5hPgMx0L_pWAg9ji_SbKwnoeCp_1vMGHyNw_lYrnX3KQa8=', start_index=12305)
Annotation(end_index=12739, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC2g3sDNaDrSjHbPlLBf3hYA-prCF6qAjwwRwFqT-nunAHCOIc9EvV0QnlvpMOM_sjjldIqa4gnZR8_h3QyGGPx0bw8k_KqY4KbHyDE5Ir_iT72QVpu7vT6IIpNneEsENbQHZteSYLsI2SdM-J0zgVmwteqLBWz0Tp', start_index=12726)
Annotation(end_index=12739, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcyfatAisrdOB9cerd0a7lw5abrR0uJ-790QmpwK78gWAv3C1FF9IkjOjA0cImaE2u7zkctqmeJfGqIS88iFEWZHUe7vH6VSOm2a4WnXbayPwvcPHs99Flzpa6RX4XJDHwMj3wtc3L63iOyhRQ0whSXlY6-rCIfbVGH2cHpFQRfI4V6Vo1vZyxJZc=', start_index=12726)
Annotation(end_index=13142, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcyfatAisrdOB9cerd0a7lw5abrR0uJ-790QmpwK78gWAv3C1FF9IkjOjA0cImaE2u7zkctqmeJfGqIS88iFEWZHUe7vH6VSOm2a4WnXbayPwvcPHs99Flzpa6RX4XJDHwMj3wtc3L63iOyhRQ0whSXlY6-rCIfbVGH2cHpFQRfI4V6Vo1vZyxJZc=', start_index=13133)
Annotation(end_index=13874, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOqT_7s3t5vTBHqqTsuKQPP6BouQfwZlpF5tGLA0UvXdOypG7pvjfVu57M19vClPRTgzPZQwgfHmq32sVtw9shnemO6o3djrWZBsP3O9DPPKTLtEX9cE_Mh6IKtWS7TzznkFmTALgBQ2_3CjqNwcKGuIIFX2z0GECIisiBXvr6M3WfHKkuJctnXma3', start_index=13864)
Annotation(end_index=14633, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGF5yMSEaxzHvh_gNuQEySMcbTzrWGm0mAYZjmIGSZLRYBrLUI7HSX3l1g-61sjpHb6ZmGqUC5jYwcf__bGvIzWWw1vhQlhSAA4um46w73_R3IS2TVIq1_oKOg=', start_index=14620)
Annotation(end_index=14633, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwkxFtK1gTPk486CDeJBIAjh7YRtN4EwHZ4tImbIxpSMvn37MfHxfoMPKrHNJGaOmDZJklsDwRO6MFvW7gdK-muiJ1FWc3_0nPYCIhSH9SZ2FCOpJlNGyPRDlG7iMRowAzgrWNKcEM4qKkVIHPh7SU58ZHXQ==', start_index=14620)
Annotation(end_index=14964, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkkEX147smfsEP-1LAdYjPVmJIPtZTC5GgaYNkQJJnohnNc0iuWFcxLUs-jIwmRW7jvzq6eQLYQErvHcw8oZk9k1ZbphYL7Vk4OA1CMkVzvq3O3Kh9zQ8JXoTBHZWoohiQWXENMbasizAVZqWVLX8Rb6VRRg==', start_index=14954)
Annotation(end_index=15266, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpuRGfKP9mKIlEnB8Zi-qOyIyhzXZZgytIEMVl1IjeXDkfQak1NzHm3QPy3NoX7H1dWFr9sFwIarpI0vLqKhsSOG7eaaT7xOMay-VjHBFSnfaSPwvgzjoicoENPF7_vxiinkw5zg5asO8nC-SUpkZebW0adYl4RVtJmqjVo64ejML19JMWoDtEUg-C7NP2sBSQWwELTz2u', start_index=15253)
Annotation(end_index=15266, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFw5DjRoVYWNwBnkAHUsVRFfUBdwuUb3Wia4byqYKOukWvuXi3c14xdq5kJH51M8rd7hFV1zlCK94GrEJ5a8NtvjS-T4WtiMfXXcTJIyM_3KmWj2DZdZR71BAud9DW1Cs8OGWE4vl3J', start_index=15253)
Annotation(end_index=15877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcyfatAisrdOB9cerd0a7lw5abrR0uJ-790QmpwK78gWAv3C1FF9IkjOjA0cImaE2u7zkctqmeJfGqIS88iFEWZHUe7vH6VSOm2a4WnXbayPwvcPHs99Flzpa6RX4XJDHwMj3wtc3L63iOyhRQ0whSXlY6-rCIfbVGH2cHpFQRfI4V6Vo1vZyxJZc=', start_index=15868)
Annotation(end_index=16443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcyfatAisrdOB9cerd0a7lw5abrR0uJ-790QmpwK78gWAv3C1FF9IkjOjA0cImaE2u7zkctqmeJfGqIS88iFEWZHUe7vH6VSOm2a4WnXbayPwvcPHs99Flzpa6RX4XJDHwMj3wtc3L63iOyhRQ0whSXlY6-rCIfbVGH2cHpFQRfI4V6Vo1vZyxJZc=', start_index=16434)
Annotation(end_index=16687, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGF5yMSEaxzHvh_gNuQEySMcbTzrWGm0mAYZjmIGSZLRYBrLUI7HSX3l1g-61sjpHb6ZmGqUC5jYwcf__bGvIzWWw1vhQlhSAA4um46w73_R3IS2TVIq1_oKOg=', start_index=16675)
Annotation(end_index=16687, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKA-TrEZHZQZ0XEs46aKSgz17DBYaIn0zr4qrvvk0W3TfFbqhtiF83xAF5eCtH55a9V1xNB6XlTq4yJt7C2fUbzkJxclmX0MEGtm8J6Dsb-pN8_2f8goLHcx0Gf1NEFndSmLSN1A3I7xKERiuVylvZRlcWCIMRGWyDAOlm8RmSJks-5ag6kBRq6K5tTO7Ba9dCpQdnIZgzciHNjOLv', start_index=16675)
Annotation(end_index=17028, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2Q4v_8hABLQa8Yq5_Y5glel9csA4aQsAo9hoC9ZekvW8L1U8Tc79IH1OGHS1NWGZv4vkIQQI5Jq3W4kcVX6e_6RZtYLzV1tUt0OTIzscdDaMvxCEC1LUkdj3FvAfY5Jmbda6RRQGmtk33AqgSFBnnVFMDsfaGZqpgLA==', start_index=17018)
Annotation(end_index=17615, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpuRGfKP9mKIlEnB8Zi-qOyIyhzXZZgytIEMVl1IjeXDkfQak1NzHm3QPy3NoX7H1dWFr9sFwIarpI0vLqKhsSOG7eaaT7xOMay-VjHBFSnfaSPwvgzjoicoENPF7_vxiinkw5zg5asO8nC-SUpkZebW0adYl4RVtJmqjVo64ejML19JMWoDtEUg-C7NP2sBSQWwELTz2u', start_index=17606)
Annotation(end_index=17691, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEs0d6BLXMxE3hJm3d81BjU8LzWpCRce_m4jT2Hmu4D32_uTbqOJJ72j4TEb-81qTqLFCHU3MI_OD5cHDtM5o5n52kN1vS81NAVj0as-4fzbw65HuQ_GHeWUmxpyTM6aqwt', start_index=17682)
Annotation(end_index=17792, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMPsO1ImZhCOGeETT_2VoC5um8ktT3pP3PRcruF4fAncftvMri3XEPdHA1jCt16Wg7j7z-qwbLcRQY4QnwD73O3aUlRJvkMDgH-Pq4BY6nOoP_T4ic4rv_KLvvDJEKDset-V45Nw-lGxrAkfnyGC2YrJf0qJST', start_index=17783)
Annotation(end_index=17904, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFw5DjRoVYWNwBnkAHUsVRFfUBdwuUb3Wia4byqYKOukWvuXi3c14xdq5kJH51M8rd7hFV1zlCK94GrEJ5a8NtvjS-T4WtiMfXXcTJIyM_3KmWj2DZdZR71BAud9DW1Cs8OGWE4vl3J', start_index=17894)
Annotation(end_index=17966, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGF5yMSEaxzHvh_gNuQEySMcbTzrWGm0mAYZjmIGSZLRYBrLUI7HSX3l1g-61sjpHb6ZmGqUC5jYwcf__bGvIzWWw1vhQlhSAA4um46w73_R3IS2TVIq1_oKOg=', start_index=17957)
Annotation(end_index=18037, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwkxFtK1gTPk486CDeJBIAjh7YRtN4EwHZ4tImbIxpSMvn37MfHxfoMPKrHNJGaOmDZJklsDwRO6MFvW7gdK-muiJ1FWc3_0nPYCIhSH9SZ2FCOpJlNGyPRDlG7iMRowAzgrWNKcEM4qKkVIHPh7SU58ZHXQ==', start_index=18027)
Annotation(end_index=18111, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEKab7PLI_TKtae_adlsy0MSCIfZNs5cTYIDnGJPdxzK4A062n0-a_E2_wxfmb0PPzfJTnIaaGaMy8urGp9EkYFw1exP2dB_V6Mykq6uLOge9CCQjyFsieLwNLmvOifa9nsJ6vqp19I6VOaC0=', start_index=18101)
Annotation(end_index=18185, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE25IuAuiHm9uRIbb5ZuQdshETp2GokmJO7jnepXMBbZAm77tkqlfeZ-0peQrh_sy-RoJlhp6nSQnmPvJkufnMQrCy7ry0mMYdLrhp4Pb33L-a9VEsGt67w-6wy6530NLBnSmys7p7p9tg8X-U6Ym5iLdexRHH7GRb-DHnrMlUUlpsXNyWULZCobvWK84VJi3ISxObSSm8GytdVc91mLnZa6yQ=', start_index=18175)
Annotation(end_index=18253, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnyBN3lhgxvvY2OvaBw67hFc-JzyrwaUmTtxasxQFI1SOnFwK_7HH4VV3rIwGQDdmvkUJx0VA0J5lUK4zOC_4rW8LdSLL845Yc_c3U7JtTSg-XQl3VWolCOS6GjmKO-sLnuao=', start_index=18244)
Annotation(end_index=18364, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKakzxUWoVeDV6CztTfIGFPb0bgnOTk7IvKFl7h_SBGSrJD9e3bw7aro3oi0ERkA5N_D3UbxJZefE5uAFuHCDQMnXyAdtreEN5igEGcsJ-Ivv-zjFjnp3fID-yB_dHj5K5Jj3ZwXshSCvoQNZOf0ZxwOZj7oQ=', start_index=18354)
Annotation(end_index=18451, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqKDmTg1gadzlbMuHpe8JRde8lQ2xZT8fap4zLTDR19vAkQJeM55Ow5MFV8FTB1-2ZlbMGvRbMgISb-rGZrUxEmjMtHd1qBGRqiAXLnke-YvH_ExnQ7nCptQhtLz1XlyyQHq6gUE3iud1np3lCF3AoWyQUZstyCceJmTR0nw==', start_index=18441)
Annotation(end_index=18530, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFufSltDxVsgqKfkOzpmErEQ59vpVjTTMbd1rEjBBPND-qlfTkiTArCAUmxkOo_iCzgholNVjy1z5McSAACyypYpen1ZqC28zFIMWriFZMipIoPV8_LuC7G6M_fedly6TuVAmoZLo9wMOROBfxutGXYNvyeYV3V_T3j51ECAzZUMNoQI-kQ-GkYf9kFR1WRROk=', start_index=18520)
Annotation(end_index=18617, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVHbzXg4RRN359Hscj7AjhCGNPulUuHuoqMmEXlv7BvbHSWzP53o0xj_IS4f8nHxg5GziIj1Qs76N0aYHREBy4HjPFozH-148JxJqYCcqEpvnjTee32VWSrU4GE3pCD9HNn6ycSFmtPtisBV1BB08M_fE6-KMRxaHD43Om_gpC-VxVxmRJwCBM5QrVyvdyjpg=', start_index=18607)
Annotation(end_index=18695, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcyfatAisrdOB9cerd0a7lw5abrR0uJ-790QmpwK78gWAv3C1FF9IkjOjA0cImaE2u7zkctqmeJfGqIS88iFEWZHUe7vH6VSOm2a4WnXbayPwvcPHs99Flzpa6RX4XJDHwMj3wtc3L63iOyhRQ0whSXlY6-rCIfbVGH2cHpFQRfI4V6Vo1vZyxJZc=', start_index=18686)
Annotation(end_index=18781, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2Q4v_8hABLQa8Yq5_Y5glel9csA4aQsAo9hoC9ZekvW8L1U8Tc79IH1OGHS1NWGZv4vkIQQI5Jq3W4kcVX6e_6RZtYLzV1tUt0OTIzscdDaMvxCEC1LUkdj3FvAfY5Jmbda6RRQGmtk33AqgSFBnnVFMDsfaGZqpgLA==', start_index=18771)
Annotation(end_index=18878, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtfT2iGSNfSoxxkQ2MyM2-hrUjYJ5EjcD_vqnNtQaFPMv-VZsQSdao2s4NDtviGtJQKk-ye9SolODuoXke29RmIA1OtAqqXo_dxF8DiQZViF-qC_wf5ay63ii7j1E6vZ77VXs6FGQqC8l7wzH7As0s2klghJpQp4t9EsRsdf4s2qLt8_RMDhG04EMcXTrCo5oSkOP7XikWiZ4xYS6UqJhVuZs_cG-t2gQVnjuo4AOmhjQ9OjXqbKcGIZrudrTbJTYHLqvyiLNTvFEAueZ8SA==', start_index=18869)
Annotation(end_index=18974, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKA-TrEZHZQZ0XEs46aKSgz17DBYaIn0zr4qrvvk0W3TfFbqhtiF83xAF5eCtH55a9V1xNB6XlTq4yJt7C2fUbzkJxclmX0MEGtm8J6Dsb-pN8_2f8goLHcx0Gf1NEFndSmLSN1A3I7xKERiuVylvZRlcWCIMRGWyDAOlm8RmSJks-5ag6kBRq6K5tTO7Ba9dCpQdnIZgzciHNjOLv', start_index=18965)
Annotation(end_index=19048, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFw5DjRoVYWNwBnkAHUsVRFfUBdwuUb3Wia4byqYKOukWvuXi3c14xdq5kJH51M8rd7hFV1zlCK94GrEJ5a8NtvjS-T4WtiMfXXcTJIyM_3KmWj2DZdZR71BAud9DW1Cs8OGWE4vl3J', start_index=19038)
Annotation(end_index=19123, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOqT_7s3t5vTBHqqTsuKQPP6BouQfwZlpF5tGLA0UvXdOypG7pvjfVu57M19vClPRTgzPZQwgfHmq32sVtw9shnemO6o3djrWZBsP3O9DPPKTLtEX9cE_Mh6IKtWS7TzznkFmTALgBQ2_3CjqNwcKGuIIFX2z0GECIisiBXvr6M3WfHKkuJctnXma3', start_index=19113)
Annotation(end_index=19212, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcyfatAisrdOB9cerd0a7lw5abrR0uJ-790QmpwK78gWAv3C1FF9IkjOjA0cImaE2u7zkctqmeJfGqIS88iFEWZHUe7vH6VSOm2a4WnXbayPwvcPHs99Flzpa6RX4XJDHwMj3wtc3L63iOyhRQ0whSXlY6-rCIfbVGH2cHpFQRfI4V6Vo1vZyxJZc=', start_index=19203)

## Sources
