# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 877379ec | **Time:** 298.44s | **Cost:** $1.29757
--------------------------------------------------------------------------------

# The Effect of Network Flow Assignment Convergence on Model Complexity under Elastic Demand

### Key Points
*   **Elastic Demand Increases Computational Burden:** Unlike fixed-demand models, elastic demand introduces a feedback loop where traffic volumes depend on network costs, and costs depend on volumes. This interdependence significantly increases the complexity of achieving convergence, often requiring specialized algorithms or rigorous damping mechanisms like the Method of Successive Averages (MSA) to prevent oscillation.
*   **Algorithmic Trade-offs:** Traditional algorithms like Frank-Wolfe are often unstable or slow when applied to elastic demand problems. More robust methods, such as Evans’ algorithm or Gradient Projection, offer better convergence properties but may entail higher per-iteration computational costs.
*   **Topological vs. Algorithmic Complexity:** Techniques like Gartner’s Transformation reduce algorithmic complexity by converting the elastic demand problem into an equivalent fixed-demand problem on an augmented network. This trades algorithmic difficulty for increased topological complexity (adding dummy nodes and links).
*   **Convergence Criteria for Stability:** Research indicates that achieving stable link flows in elastic demand models requires stricter convergence criteria (e.g., a relative gap of $10^{-4}$) compared to aggregate metrics like total system travel time. Insufficient convergence can lead to erroneous policy conclusions, particularly in "build vs. no-build" scenarios.

---

## 1. Introduction

The Traffic Assignment Problem (TAP) is a cornerstone of transportation planning, serving as the mathematical framework for predicting how travel demand is distributed across a transportation network. In its simplest form, the Fixed Demand Traffic Assignment Problem (FD-TAP) assumes that the origin-destination (O-D) trip matrix is constant, regardless of the congestion levels in the network. However, this assumption often fails to capture the economic reality that travel demand is a derived demand, sensitive to the generalized cost of travel. Consequently, the Elastic Demand Traffic Assignment Problem (ED-TAP) was developed to model the interaction between supply (network capacity and performance) and demand (user willingness to travel).

The introduction of elastic demand fundamentally alters the mathematical structure of the assignment problem, transforming it from a simple resource allocation problem into a complex equilibrium problem involving feedback loops. This report provides an exhaustive analysis of how the requirement for convergence in network flow assignment impacts model complexity under elastic demand. It synthesizes theoretical formulations, algorithmic performance, and convergence stability requirements to determine the trade-offs inherent in modeling variable demand.

### 1.1 The Nature of Elastic Demand
In ED-TAP, the demand $q_{rs}$ between origin $r$ and destination $s$ is a function of the minimum travel cost $u_{rs}$. As congestion increases, travel costs rise, causing demand to decrease (and vice versa). This relationship is typically governed by a demand function $D(u_{rs})$ or its inverse, the disutility function $W(q_{rs})$. The equilibrium condition, known as Wardrop’s User Equilibrium (UE), is achieved when no traveler can reduce their travel cost by unilaterally changing routes, and the demand generated matches the cost of travel on the used paths [cite: 1].

The complexity arises because the demand function and the link performance functions (congestion) are coupled. Solving this requires finding a fixed point where the flow pattern generates costs that induce exactly that flow pattern.

---

## 2. Theoretical Formulations and Model Complexity

The mathematical formulation of ED-TAP dictates the complexity of the solution algorithms. The problem is generally formulated as a convex optimization program or a Variational Inequality (VI).

### 2.1 The Beckmann Transformation
The classic formulation by Beckmann, McGuire, and Winsten (1956) frames the user equilibrium as a minimization problem. For elastic demand, the objective function is modified to include the consumer surplus. The objective function $Z$ is minimized:

\[
\min Z(x, q) = \sum_{a} \int_{0}^{x_a} t_a(w) dw - \sum_{rs} \int_{0}^{q_{rs}} W_{rs}(w) dw
\]

Where:
*   $x_a$ is the flow on link $a$.
*   $t_a(x_a)$ is the link performance function (travel time).
*   $W_{rs}(q_{rs})$ is the inverse demand function for O-D pair $rs$.

This formulation integrates the supply side (first term) and the demand side (second term). While this provides a rigorous theoretical basis, it increases model complexity by requiring the algorithm to simultaneously update link flows and O-D demands [cite: 2, 3].

### 2.2 Gartner’s Transformation: Topological vs. Algorithmic Complexity
A pivotal method for managing the complexity of ED-TAP is **Gartner’s Transformation** (also known as the excess-demand formulation). This approach remodels the elastic demand problem as an equivalent fixed-demand assignment problem on an expanded network [cite: 4, 5].

**The Mechanism:**
1.  **Excess Demand:** For each O-D pair, a fixed "potential" demand $\bar{Q}_{rs}$ is defined (an upper bound on trips).
2.  **Augmented Network:** A "dummy" or "overflow" link is added for each O-D pair, connecting the origin directly to the destination (or via a super-node structure).
3.  **Cost Function:** The cost of this overflow link is defined by the inverse demand function. Flow that does not travel on the physical network "overflows" onto this dummy link.
4.  **Equivalence:** The problem becomes assigning the fixed potential demand $\bar{Q}_{rs}$ such that the cost on the physical network equals the cost on the overflow link (which represents the disutility of not traveling or traveling by an alternative mode).

**Effect on Complexity:**
*   **Algorithmic Reduction:** By converting ED-TAP to FD-TAP, practitioners can use standard, highly optimized fixed-demand algorithms (like Frank-Wolfe or Gradient Projection) without modification [cite: 5, 6]. This significantly lowers the barrier to implementation.
*   **Topological Increase:** The trade-off is an increase in the size of the network graph. For a network with many O-D pairs, the number of additional links can be substantial, potentially increasing memory requirements and the search space for shortest-path algorithms [cite: 7, 8]. However, since these links are direct O-D connections, they do not necessarily complicate the shortest path search within the physical network itself.

### 2.3 Variational Inequality (VI) Formulations
For more complex demand structures, such as asymmetric interactions (where demand for one pair depends on the cost of another) or multi-class models, the optimization formulation may not exist. In these cases, the problem is formulated as a Variational Inequality. The VI formulation allows for the rigorous analysis of existence and uniqueness of the equilibrium but generally requires more sophisticated solution algorithms (e.g., projection methods or diagonalization) than the simple convex minimization approaches, thereby increasing computational complexity [cite: 9, 10].

---

## 3. Algorithmic Convergence and Computational Effort

The choice of algorithm profoundly influences the speed and stability of convergence in elastic demand models. The interaction between flow updates and demand updates can lead to oscillatory behavior if not managed correctly.

### 3.1 The Frank-Wolfe (FW) Algorithm
The Frank-Wolfe algorithm (or Convex Combination algorithm) is the traditional workhorse for static traffic assignment. It operates by linearizing the objective function and finding a descent direction by solving all-or-nothing assignments.

**Performance in Elastic Demand:**
Research indicates that the standard Frank-Wolfe algorithm can be **unstable** or slow when applied to elastic demand problems [cite: 11, 12].
*   **Sensitivity:** The rate of convergence is often very sensitive to the values used for the upper bounds on trips (in the excess demand formulation) or the specific "tuning parameters" used to weigh the demand updates [cite: 11, 13].
*   **Zig-Zagging:** FW is known for "zig-zagging" near the optimum. In elastic demand, this is exacerbated because a small change in flow changes the cost, which immediately changes the demand, potentially causing the algorithm to overshoot the equilibrium repeatedly.
*   **Computational Cost:** While each iteration is relatively cheap (requiring shortest path searches), the total number of iterations required to reach a stable solution (e.g., a relative gap of $10^{-4}$) can be prohibitive [cite: 14].

### 3.2 Evans’ Algorithm
Evans’ algorithm is a partial linearization method specifically designed for the combined distribution and assignment problem (which is mathematically equivalent to ED-TAP). Unlike FW, which linearizes the entire objective function, Evans’ algorithm retains the nonlinearity of the demand function while linearizing the travel cost function.

**Advantages:**
*   **Robustness:** Computational studies consistently show that Evans’ algorithm is more robust than Frank-Wolfe for elastic demand problems [cite: 12, 13].
*   **Convergence Speed:** It converges consistently faster (in terms of iteration count) because it solves a sub-problem that explicitly balances demand and flow at each step, rather than just shifting flow [cite: 15, 16].
*   **Correctness:** It produces a solution where link volumes are consistent with travel times *and* the trip table is consistent with path costs, solving the elastic demand problem exactly rather than approximately [cite: 15].

### 3.3 Gradient Projection (GP) and Path-Based Algorithms
Path-based algorithms, such as Gradient Projection, operate directly on path flows rather than link flows.
*   **Efficiency:** GP algorithms have been shown to outperform classical Evans’ algorithms and FW algorithms, particularly in bi-modal or complex elastic demand contexts [cite: 17].
*   **Mechanism:** By keeping track of path flows, GP can shift flow more precisely between efficient paths and the "excess demand" path. This avoids the smearing effect of link-based algorithms and allows for faster convergence to high-precision solutions [cite: 17].
*   **Symmetric Interactions:** Recent research suggests that if link interactions are symmetric and monotone, GP algorithms converge significantly faster, even if the underlying interactions are slightly asymmetric [cite: 18].

---

## 4. The Feedback Loop: Internal vs. External Equilibrium

A critical aspect of model complexity in elastic demand is the architecture of the solution procedure. This is often described as the distinction between solving a single integrated mathematical program (Internal Equilibrium) versus iterating between separate software modules (External Equilibrium).

### 4.1 The Method of Repeated Approximations (MRA)
In many practical transport models (e.g., the "Four-Step Model"), demand and assignment are separate modules. The simplest way to solve for elastic demand is the **Method of Repeated Approximations (MRA)**, also known as naive feedback.
1.  Calculate Demand based on current costs.
2.  Assign Demand to the network to get new flows and costs.
3.  Feed new costs back to the Demand model.
4.  Repeat.

**Instability and Failure:**
Research explicitly highlights that MRA is prone to instability. Because the demand function and supply function often have slopes that do not satisfy contraction mapping conditions, MRA may exhibit cyclic unstable patterns or fail to converge entirely [cite: 19, 20]. The "contraction region"—the set of conditions under which MRA converges—shrinks as the sensitivity of demand to cost increases [cite: 19].

### 4.2 The Method of Successive Averages (MSA)
To remedy the instability of MRA, the **Method of Successive Averages (MSA)** is employed. Instead of replacing the old demand/flow with the new calculation, MSA takes a weighted average of the current and previous states (e.g., $x_{k+1} = (1/k)x_{new} + ((k-1)/k)x_{old}$).

**Complexity Implications:**
*   **Guaranteed Convergence:** MSA is proven to converge under fairly weak regularity conditions (Robbins and Monro, 1951), making it a reliable "fix" for the instability of MRA [cite: 19, 21].
*   **Slow Convergence:** The trade-off is speed. MSA has a sublinear convergence rate ($O(1/k)$). While it prevents oscillation, it may require a vast number of iterations to reach a tight convergence gap, significantly increasing the computational runtime of the model [cite: 19, 22].
*   **Damping Noise:** In large-scale models (like the Danish National Transport Model), MSA is essential not just for equilibrium but for damping random noise inherent in simulation-based assignment or stochastic demand models [cite: 20].

---

## 5. Convergence Criteria and Stability Requirements

The definition of "convergence" significantly impacts model complexity. How much convergence is enough? The answer depends on the application, but elastic demand generally raises the bar.

### 5.1 Relative Gap and Link Flow Stability
The **Relative Gap (RG)** is the standard metric for measuring convergence (the difference between the current total system cost and the cost if all users were on the shortest paths).
*   **The $10^{-4}$ Standard:** Research by Boyce, Bar-Gera, and others indicates that a relative gap of $0.01\%$ ($10^{-4}$) is required to ensure that link flows are stable [cite: 14].
*   **Aggregate vs. Disaggregate Stability:** Aggregate metrics like Total System Travel Time (TSTT) or Vehicle Miles Traveled (VMT) stabilize relatively early (around RG $10^{-3}$ or $10^{-4}$). However, individual link flows—which are crucial for environmental analysis or toll revenue estimation—stabilize later (RG $10^{-5}$). Path flows stabilize last (RG $10^{-6}$) [cite: 23, 24].

### 5.2 The Cost of Stability in Elastic Models
In elastic demand models, the "trip table" is not fixed. Therefore, "stability" implies that both the routing *and* the total number of trips must stabilize.
*   **Fluctuations:** If the convergence criteria are too loose (e.g., RG $10^{-2}$), the demand model may react to "noise" in the travel times rather than true congestion signals. This leads to "counter-intuitive differences" between scenarios (e.g., a road improvement leading to less traffic due to iteration noise) [cite: 14, 25].
*   **Computational Burden:** Achieving RG $10^{-4}$ with elastic demand using standard algorithms (like FW) can take orders of magnitude more time than fixed demand assignments. This necessitates the use of advanced algorithms like Origin-Based Assignment (OBA) or Gradient Projection to achieve high convergence with reasonable computing effort [cite: 14].

---

## 6. Advanced Model Complexities

### 6.1 Bi-Criteria Assignment and Heterogeneity
When users trade off between time and cost (e.g., toll roads), the problem becomes a **Bi-Criteria Traffic Assignment**. If the Value of Time (VOT) is continuously distributed, this effectively creates an infinite number of user classes.
*   **Complexity:** This explodes the model complexity. Standard algorithms cannot handle infinite classes.
*   **Solution:** Algorithms like the Two-Stage Gradient Projection (TSGP) decompose the problem into "demand equilibration" (adjusting total demand based on expected generalized time) and "boundary equilibration" (adjusting flows between efficient paths). This structure allows for high-quality solutions but requires sophisticated mathematical reformulation [cite: 1, 3].

### 6.2 Dynamic Traffic Assignment (DTA)
Moving from static to dynamic assignment with elastic demand introduces the highest level of complexity.
*   **Non-Monotonicity:** In DTA, path delay operators are not necessarily monotonic (more flow does not always mean more delay in a predictable way due to queue spillback). This violates the standard assumptions required for convex optimization convergence [cite: 9].
*   **Existence of Equilibrium:** The existence of a dynamic equilibrium is not always guaranteed, and computation requires fixed-point algorithms that are robust to non-monotonicity. The "external loop" between DTA and demand models is particularly fragile and computationally expensive [cite: 9, 18].

---

## 7. Conclusion

The effect of network flow assignment convergence on model complexity under elastic demand is characterized by a fundamental trade-off between **realism** and **computational stability**.

1.  **Instability is the Default:** Without specific interventions, the feedback loop between cost and demand creates unstable, oscillating models (MRA failure).
2.  **Complexity is Conserved:** To solve this instability, complexity must be introduced elsewhere:
    *   **Topological Complexity:** Via Gartner’s transformation (augmenting the network).
    *   **Algorithmic Complexity:** Via Evans’ algorithm or Gradient Projection (more complex iteration steps).
    *   **Computational Complexity:** Via MSA (requiring many more iterations to converge).
3.  **High Convergence is Mandatory:** Unlike fixed demand models where "good enough" convergence might suffice for aggregate planning, elastic demand models require tight convergence (Relative Gap $< 10^{-4}$) to ensure that the demand response is reacting to the equilibrium state rather than algorithmic noise.

For academic and practical applications, this implies that simply "turning on" elastic demand in a standard assignment software without adjusting the solution algorithm (e.g., switching from FW to Evans or GP) or the convergence criteria will likely result in invalid, unstable model outputs.

## References

*   **[cite: 2]** Zetina, C. (2018). *Profit Oriented Network Design with Elastic Demand*.
*   **[cite: 1, 3]** Xu, Z., et al. (2023/2024). *Elastic-demand bi-criteria traffic assignment under the continuously distributed value of time*.
*   **[cite: 19, 20, 21]** Rich, J., & Nielsen, O. A. (2010/2015). *System Convergence in Transport Modelling*.
*   **[cite: 14]** Boyce, D., Ralevic-Dekic, B., & Bar-Gera, H. (2004). *Convergence of traffic assignments: how much is enough?*
*   **[cite: 23, 24]** *Convergence behavior for traffic assignment characterization metrics*.
*   **[cite: 9]** Friesz, T. L., et al. (2021). *Convergence of a scheme for elastic flow...*
*   **[cite: 18]** Patil, P. N. (2023). *A fresh look at symmetric traffic assignment and algorithm convergence*.
*   **[cite: 11, 12, 13]** *Computational Experience on Advanced Algorithms... / Different algorithms for solving elastic demand...*
*   **[cite: 17]** Chen, A. *Solving Combined Modal Split and Traffic Assignment...*
*   **[cite: 6]** *The Traffic Assignment Toolboxes of Scilab*.
*   **[cite: 7]** *An Excess-Demand Dynamic Traffic Assignment Approach...*
*   **[cite: 4, 5]** Gartner, N. H. (1980). *Optimal Traffic Assignment with Elastic Demands: A Review*.
*   **[cite: 8, 10]** Codina, E. *A Method to approximate the Steepest Descent direction...*
*   **[cite: 15]** Horowitz, A. J. (1989). *Convergence Properties of Some Iterative Traffic Assignment Algorithms*.

**Sources:**
1. [polyu.edu.hk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGErBUFrxtXeu7tXSzSDJGrnMUO8DbiI18vE2BeCNSJtowMiNlmiDNS21qIq2Ijojc9ZHpKUp9cZ_ahZWtVgtGMKjgvbI3z0Qf-_RzEjvARTo94jh1NdRZLPZEPq8femU0jPU56Vz4krjZ-m0808fYTf_e4kAl-pSQnT57qgQdY4Eiji6cxYhUmsa5xhiA1mBo7BtriWg==)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4CVs6y3l-jMRYuLfIaclv1VNzPgTQaev3nY_IPCGpYtoimMyMk0ELgjrEV8Ui1ZisK5iG8ooZBvTnMv_JPNCBr0U4HHDqf7Se4pr8ZPNqFocKk4Exx9_vjaYnb2y1NmOrNyn53jIf2Q3AeFk2If_D5hW-Ue8Mmtvo2G_7Y0vn5ler0wqw_MFo03hzCKZ35YaUTPUD66JsUO5XfAthJWPWOAAxQ1tK0-M3C_NTk6DSnsS3MtVfYj8_IYj0sY8i2gZ1s72z32ltlPMmd3RbI2sEoO8lUnqOKPabro5vw_j-F3bnN-TFkWTDmSRI7OWyiakmmNIW0eFTpVnzGVwK9QcaJjZLJs3DFkg=)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaVqtwxLB2xEGYsCq56bD4BK_HZiJVd6AM7FmaG574t6O6wS0EsfgOof-jKyimkB23Jm_ipr232SQ9w3RIlgJJXNkAvrIArG8d_FXlN6fFTqBAh6v70I-cpboB1tZMY3KN2OxiPnJLm_gcCgJxfZMERI42UcBOTBVVn0x1k6SwTL8QzPKJfdceDiBYEshUFb_u-QMvc4x4ZQ7ayH_sd_JovPJmy7ghRHAr_lLa9yBGdnb40CYSE4LlkvXnS9xhKpZYW830t1Y8m8pljMpkZH1QftYIMP9RgtzcMcd04rFe4Cjz0ZKm44oJfdAqrX6lwoYc_zfkixVHwZxnmlrNY5LIoNdykHjdPd63x-nDAltbTU8=)
4. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiurr9TJ2TXj0M09TGle2Xs8Y6Ib-i4euqUfeqBJlsNUieAZXw6KQmadVC9Up-GAU0tneRj7BZ6FGITA9qyna-6PBZ-uTmy2Q7Q4UjEY57afnBVj6ivau6OpU3r923jF7A-T6_ODWqgL71i9oDlSFFdP0=)
5. [informs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9Krv733tmFuAPQsU60kPrdQ8WSNVhdQrST3ccf-FMBIXsHL5Mikho9FxnC3JGtOPEDTYPuZ1ywMv3vkN-s7RlIL_7YXNZRPcpjG0LyOCSBVNEqEnkVyAXIxvFR65SBZyj-XKYXLHDtHvLf51kaQ107qE=)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoh_yVvB8OZ_Kkv7lM2ab3cuqOqQhY8-dxWUgmjRGrHjksKNE_AivtgaxtCRjbHEdxT4egh8gAISBoPGGmF0NM6Gzz0nuwyYR7SvmJA79J0gPa11wJwfEym8qBQTisXbvnFIjaL9fwNjsIBLFTamd5DCsJAesRm3sDYXGR4rw5dn-DFI8gnmJVByXqCZS0KIh6GV0=)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGefq_wccGoFVCx5tuvZrxccWgT6hdP5mz4mQSgV281pQKnRlj2rckQrpycAKLtJLrFlEazpdVOil7DzfPWK955mNtiEJ0s_Ww4v_5RiegKzdvO_C3Ga_g32P4NSmAADaCBfhpKau3kLNdfRDIOPW4SKmYzOi3zRW7vdkGndldCEUoYlHD_-TZFaHBbgEh8Syjas7Z0rxDyiQA03qsC4pmQsiiX-KzpCEZdJKT23JxImyt0A75Rcw5ISwIhnLU22R9J2mkUz8_kFQjFy-ae)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1YoA4v4Wd4pXZO0mzMLAGT0LvsuW79oBMbDTf9YlqFDIiI_gmMyo25gGgywq4mdTAVRVhh4qSQnOmDShPMQDNqjOrgKzg1_ZW-qYaQeQtLLf0Kn5aE8kIqYf00o_NXHNEZneO-hupwqluOSs4zzqLQuIYliBI3dPKV2D1t4HyLsEcMVFRCYMyLoDC5Yn-bT19GPdwNZuezmo2txNMDxYCHME-hfcGnibtZtm1RieEXRz8LJuq30vlE9tkDFuovtxBs4dK)
9. [nsf.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIqK9WcMoDnqu9nUu6wfi3A2wPXlk3uQgkSFmD-CRxJPGiLZIkFGbglKijwz3QumkVWLVfijrNQ7I-vcA4aUOa_hc7y0AF05cgQg7SAFwyvT5ecvSN8-ae5SLcoX5V_Pg=)
10. [upc.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRIB68u8WQEXRh9DUWohIf4o_UnOxDQRmctu5D69Rg7SY3ievrdBE5WDxEec4t-Nf3W4bRKujlLB1ZmvsnJEIcluOWIvnomkB2o_UNYtueY7ps5ov98pLinYnuxwEnfykkiDgOuxsBWJAVO0gdJLLQltm186Rxj2IRKi-e4EiLg6SjUGmBNHZD)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEi9Syn8c2CTBr8FZ3V6qtakgYnBXAQ0Nz37pVF93BzDXJDMLsVLkL9kQN68jjyxBlxq09vYxUVhkjff9APhWyMCEzxmyyZMgTRVvtNuMUYxtOsm624cxtzgQKuqqEGliuee9LJYuUdAYJJggD_s8CgyKqf7789h9Q9PK_ZXZtT-PQ5VxRokWbnY1kOzqkLNPJvyS0kh3khAwDkTFwIFHgMu6KcKiHw2PvsA_HKeqzO9PbQ3btDtbF0)
12. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMCq59RlksyyqrINu5P3r71Z0S0jEMwM4tVxeyTUaW6py5mVKOn6IMb9hR21j5uXmBGTzh1cW8QjVM7KfJBwl3ViUTOxBq8FzI0mI4hQZQnTb-8Oj6GBgFgnp_2KGmidppHZZCfgHKtcWKxaUwdBpvqQs=)
13. [informs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4CL8jd4NbwPTfZov_s_2Dd7__0EAWYB3F9R7iBpRZ2PSCdBvi2QEBozqOZLZc9jDw4YsBZH2p-m41goSRdpj3lo_ogCHax5-f5lMuW1MTb0Pji-aNjNraBSImFohk62U41vmFvyiyVDs3rgmLqQ==)
14. [northwestern.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5ggiMPx2XABjCWwL378Id14YQ8UQD5XQ8cOvhXM_4QKWt0QI7AZdsv66saEtVJImzmGYkYBU4xWmx07y9gbA4y35pTN-pVNuBm7yOWr7XNBAD5i1PmH2MTGrBJk6p9smp1eO7RoZ0SyUY_wAWZ8BuXgg=)
15. [trb.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHL7JZaX22s0UNf3WCWMZgVs7XmNl6dCyuTJW6vA1vj7aSnyrnMh5pFRblEr_-2Y6zHXE1734HVUMMRhS0WSd0vsnUrVj_hD9sj64BTDPQFPIVbX2mnXa61d70VMxcz8BYK9UfNpciaZ3NqJdNmCBoIqvd0TY34)
16. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX88virA45K-jyGPwakxLjdjB34MH3RpdzPqfsdUqpLnFFAcHgv4htXInjLAjgdQ5hjJeTZQk7ZQy7mzuhXw7K_-xKWdpXtp6y6KaPVN9-pv4-fRUdmuYN7sgNBiW7b-DQfJHp0CRbtX7Wm7Nu9TQu7rg=)
17. [polyu.edu.hk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMY0QX40JTQjoCHbG8yi4SLLTQ0MAn8r5AgoF4HYYyQ8QvEcq-f7OAiNvVcjf5v2v1hfeJSBG6IiJ6hRtkoXoG-nnsYepne0NT9WPFcawh9fpZAAI3EvSrC6xzwSXeEMf9rDlNuhNflB9EeZmjD8EgKLAE1jYPhuScntRIi0lgjDHczShj_e6Jy1J6)
18. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWhUyXfSpO-EWRWqj1EsJMw4qPPd06ql4TVnKw479MmNrQaojwt-2ZM_uznrzRkjp5aUInsWoyaSw3_kbpdOoXHXrsLM22TJPxQu9RLMA_kxujtoqDcA==)
19. [dtu.dk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEu9nmDcuv7KBkdpaE71D6-IpfUnuzzxsH-OXTdyQ1TsT6aSqLg8igcLFGt5Prq7wTtYv5cRUrAaABCHv6YWfFQm9MlbOwQMQlQAt2kxbZRB3leQurmLqVylBZO3eOkfbOqwQ2Yqwju0BlQTOhy47VnGzpzGIy3tdxJ8QJujeYJmlVUJAK1zQhaJTxfQ-GpacnHT_Q=)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuvXKxtrl2VTHaf6NDKlwbeCMwFpQ0yI4lXQQJlc2ZnrJaZHXvkZ0T5JHSCsCCoyrqyPvMLS1iN8UyOZcrm8LN85Ar9UEtif3ekspLj7KKaH5MtvoLDMXO_nwwX8lMAV9zYJfOBM782l_cn1RqhJweXD5gZWbd-uo2G0blZ6O2j_QpPIUsxEINiWQQqm0jyHSHUXv0JiSFhH1NYKXTvioHcZVh5aAbukZUZ01k7TL0Wboa8WBP4pI4dSumMlQ=)
21. [dtu.dk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFb1AiGYIW0skQ6Nihdlg51Y6XozTuWgvHIGgCkj4NiTUcqZ2p9KbWEcaoVLjnDhgIUz6EkzvN_8Ig5IR_JKtNGdAnW8qfKGxVoh4LGb81S5yZZtj9CRkIms7wKLfZ433EBf3gTHNZEuSRXjpoxhx2XRdfKxg==)
22. [uniroma1.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEd7e7gh4Jm4MoC7WuqjqQ_dMVpxulIV9g-qel6gk5VtUuoQuWMdnxsi235x8yqqSfccAPbCqj-4euoWYqqMHvlDBuWtSVxGs9pNGolFNldhuUaGSZmK-o_6wXe4Kjq2_uosMCr1T4XULpyCNnRzY2b2V6mAquo5w5vxRc-8fiXJoGxTXuu2cs0wJ1xw1uWojYNnpwAD6Mg6OI=)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpmOpyWhQGfsS_jsEW_IyYzVenwHoSESmY4e8Zp67IQfgYgbL2Mfgct34aB3mOpPUlhN3DdzQV_h-t1y5OudMd0Zg4jS1CpkviiB8T4KvDHWEtnrSk8xp2etQmGd81SIQ-YqB2cYPZoU3SssT-2eeG1cI8O-QkTcIXSEelMGAJIL2QZ2RYvJnAwf-MKAlzD_xWvtUyWeGmPRvhOqyQVgheK4oV5fTg47Xjflsllw==)
24. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEznW5EqBS45w1ANX1NloDIiO2pDQWq7ViLCHev3GUsNabiS0Jw9AqSvZRRHIBwYyr-qsoTWQxKWPM4DhZnvRj2rsphkzCcjGBDeVqFZEsOp6mtmwzzF7tRfZFB9tGHPDt0FcxDfRPT6M7FjnuD2CZfzckY46MuRQ==)
25. [rand.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFthrKwsr8jgPZ4vQqHW1R-N3ckdU-iVGfK6UhQdvRi1uwnaxlpzqUEO2jm31FMqdnqb0-5mYtwUPaEgQflqKedbjuIhzq-H_M0HWB6EpEKt55sk6ugyQaQsu-TdCPszk3H7ICmp5j1rTVQBlLRfpgUoBA2GlMxr81G4MQCE-ebG9etgA==)


## Annotations
Annotation(end_index=3490, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGErBUFrxtXeu7tXSzSDJGrnMUO8DbiI18vE2BeCNSJtowMiNlmiDNS21qIq2Ijojc9ZHpKUp9cZ_ahZWtVgtGMKjgvbI3z0Qf-_RzEjvARTo94jh1NdRZLPZEPq8femU0jPU56Vz4krjZ-m0808fYTf_e4kAl-pSQnT57qgQdY4Eiji6cxYhUmsa5xhiA1mBo7BtriWg==', start_index=3481)
Annotation(end_index=4805, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4CVs6y3l-jMRYuLfIaclv1VNzPgTQaev3nY_IPCGpYtoimMyMk0ELgjrEV8Ui1ZisK5iG8ooZBvTnMv_JPNCBr0U4HHDqf7Se4pr8ZPNqFocKk4Exx9_vjaYnb2y1NmOrNyn53jIf2Q3AeFk2If_D5hW-Ue8Mmtvo2G_7Y0vn5ler0wqw_MFo03hzCKZ35YaUTPUD66JsUO5XfAthJWPWOAAxQ1tK0-M3C_NTk6DSnsS3MtVfYj8_IYj0sY8i2gZ1s72z32ltlPMmd3RbI2sEoO8lUnqOKPabro5vw_j-F3bnN-TFkWTDmSRI7OWyiakmmNIW0eFTpVnzGVwK9QcaJjZLJs3DFkg=', start_index=4793)
Annotation(end_index=4805, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaVqtwxLB2xEGYsCq56bD4BK_HZiJVd6AM7FmaG574t6O6wS0EsfgOof-jKyimkB23Jm_ipr232SQ9w3RIlgJJXNkAvrIArG8d_FXlN6fFTqBAh6v70I-cpboB1tZMY3KN2OxiPnJLm_gcCgJxfZMERI42UcBOTBVVn0x1k6SwTL8QzPKJfdceDiBYEshUFb_u-QMvc4x4ZQ7ayH_sd_JovPJmy7ghRHAr_lLa9yBGdnb40CYSE4LlkvXnS9xhKpZYW830t1Y8m8pljMpkZH1QftYIMP9RgtzcMcd04rFe4Cjz0ZKm44oJfdAqrX6lwoYc_zfkixVHwZxnmlrNY5LIoNdykHjdPd63x-nDAltbTU8=', start_index=4793)
Annotation(end_index=5153, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9Krv733tmFuAPQsU60kPrdQ8WSNVhdQrST3ccf-FMBIXsHL5Mikho9FxnC3JGtOPEDTYPuZ1ywMv3vkN-s7RlIL_7YXNZRPcpjG0LyOCSBVNEqEnkVyAXIxvFR65SBZyj-XKYXLHDtHvLf51kaQ107qE=', start_index=5141)
Annotation(end_index=5153, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiurr9TJ2TXj0M09TGle2Xs8Y6Ib-i4euqUfeqBJlsNUieAZXw6KQmadVC9Up-GAU0tneRj7BZ6FGITA9qyna-6PBZ-uTmy2Q7Q4UjEY57afnBVj6ivau6OpU3r923jF7A-T6_ODWqgL71i9oDlSFFdP0=', start_index=5141)
Annotation(end_index=6144, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9Krv733tmFuAPQsU60kPrdQ8WSNVhdQrST3ccf-FMBIXsHL5Mikho9FxnC3JGtOPEDTYPuZ1ywMv3vkN-s7RlIL_7YXNZRPcpjG0LyOCSBVNEqEnkVyAXIxvFR65SBZyj-XKYXLHDtHvLf51kaQ107qE=', start_index=6132)
Annotation(end_index=6144, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoh_yVvB8OZ_Kkv7lM2ab3cuqOqQhY8-dxWUgmjRGrHjksKNE_AivtgaxtCRjbHEdxT4egh8gAISBoPGGmF0NM6Gzz0nuwyYR7SvmJA79J0gPa11wJwfEym8qBQTisXbvnFIjaL9fwNjsIBLFTamd5DCsJAesRm3sDYXGR4rw5dn-DFI8gnmJVByXqCZS0KIh6GV0=', start_index=6132)
Annotation(end_index=6487, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1YoA4v4Wd4pXZO0mzMLAGT0LvsuW79oBMbDTf9YlqFDIiI_gmMyo25gGgywq4mdTAVRVhh4qSQnOmDShPMQDNqjOrgKzg1_ZW-qYaQeQtLLf0Kn5aE8kIqYf00o_NXHNEZneO-hupwqluOSs4zzqLQuIYliBI3dPKV2D1t4HyLsEcMVFRCYMyLoDC5Yn-bT19GPdwNZuezmo2txNMDxYCHME-hfcGnibtZtm1RieEXRz8LJuq30vlE9tkDFuovtxBs4dK', start_index=6475)
Annotation(end_index=6487, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGefq_wccGoFVCx5tuvZrxccWgT6hdP5mz4mQSgV281pQKnRlj2rckQrpycAKLtJLrFlEazpdVOil7DzfPWK955mNtiEJ0s_Ww4v_5RiegKzdvO_C3Ga_g32P4NSmAADaCBfhpKau3kLNdfRDIOPW4SKmYzOi3zRW7vdkGndldCEUoYlHD_-TZFaHBbgEh8Syjas7Z0rxDyiQA03qsC4pmQsiiX-KzpCEZdJKT23JxImyt0A75Rcw5ISwIhnLU22R9J2mkUz8_kFQjFy-ae', start_index=6475)
Annotation(end_index=7267, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRIB68u8WQEXRh9DUWohIf4o_UnOxDQRmctu5D69Rg7SY3ievrdBE5WDxEec4t-Nf3W4bRKujlLB1ZmvsnJEIcluOWIvnomkB2o_UNYtueY7ps5ov98pLinYnuxwEnfykkiDgOuxsBWJAVO0gdJLLQltm186Rxj2IRKi-e4EiLg6SjUGmBNHZD', start_index=7254)
Annotation(end_index=7267, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIqK9WcMoDnqu9nUu6wfi3A2wPXlk3uQgkSFmD-CRxJPGiLZIkFGbglKijwz3QumkVWLVfijrNQ7I-vcA4aUOa_hc7y0AF05cgQg7SAFwyvT5ecvSN8-ae5SLcoX5V_Pg=', start_index=7254)
Annotation(end_index=8015, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEi9Syn8c2CTBr8FZ3V6qtakgYnBXAQ0Nz37pVF93BzDXJDMLsVLkL9kQN68jjyxBlxq09vYxUVhkjff9APhWyMCEzxmyyZMgTRVvtNuMUYxtOsm624cxtzgQKuqqEGliuee9LJYuUdAYJJggD_s8CgyKqf7789h9Q9PK_ZXZtT-PQ5VxRokWbnY1kOzqkLNPJvyS0kh3khAwDkTFwIFHgMu6KcKiHw2PvsA_HKeqzO9PbQ3btDtbF0', start_index=8001)
Annotation(end_index=8015, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMCq59RlksyyqrINu5P3r71Z0S0jEMwM4tVxeyTUaW6py5mVKOn6IMb9hR21j5uXmBGTzh1cW8QjVM7KfJBwl3ViUTOxBq8FzI0mI4hQZQnTb-8Oj6GBgFgnp_2KGmidppHZZCfgHKtcWKxaUwdBpvqQs=', start_index=8001)
Annotation(end_index=8253, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEi9Syn8c2CTBr8FZ3V6qtakgYnBXAQ0Nz37pVF93BzDXJDMLsVLkL9kQN68jjyxBlxq09vYxUVhkjff9APhWyMCEzxmyyZMgTRVvtNuMUYxtOsm624cxtzgQKuqqEGliuee9LJYuUdAYJJggD_s8CgyKqf7789h9Q9PK_ZXZtT-PQ5VxRokWbnY1kOzqkLNPJvyS0kh3khAwDkTFwIFHgMu6KcKiHw2PvsA_HKeqzO9PbQ3btDtbF0', start_index=8239)
Annotation(end_index=8253, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4CL8jd4NbwPTfZov_s_2Dd7__0EAWYB3F9R7iBpRZ2PSCdBvi2QEBozqOZLZc9jDw4YsBZH2p-m41goSRdpj3lo_ogCHax5-f5lMuW1MTb0Pji-aNjNraBSImFohk62U41vmFvyiyVDs3rgmLqQ==', start_index=8239)
Annotation(end_index=8762, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5ggiMPx2XABjCWwL378Id14YQ8UQD5XQ8cOvhXM_4QKWt0QI7AZdsv66saEtVJImzmGYkYBU4xWmx07y9gbA4y35pTN-pVNuBm7yOWr7XNBAD5i1PmH2MTGrBJk6p9smp1eO7RoZ0SyUY_wAWZ8BuXgg=', start_index=8752)
Annotation(end_index=9313, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMCq59RlksyyqrINu5P3r71Z0S0jEMwM4tVxeyTUaW6py5mVKOn6IMb9hR21j5uXmBGTzh1cW8QjVM7KfJBwl3ViUTOxBq8FzI0mI4hQZQnTb-8Oj6GBgFgnp_2KGmidppHZZCfgHKtcWKxaUwdBpvqQs=', start_index=9299)
Annotation(end_index=9313, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4CL8jd4NbwPTfZov_s_2Dd7__0EAWYB3F9R7iBpRZ2PSCdBvi2QEBozqOZLZc9jDw4YsBZH2p-m41goSRdpj3lo_ogCHax5-f5lMuW1MTb0Pji-aNjNraBSImFohk62U41vmFvyiyVDs3rgmLqQ==', start_index=9299)
Annotation(end_index=9537, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX88virA45K-jyGPwakxLjdjB34MH3RpdzPqfsdUqpLnFFAcHgv4htXInjLAjgdQ5hjJeTZQk7ZQy7mzuhXw7K_-xKWdpXtp6y6KaPVN9-pv4-fRUdmuYN7sgNBiW7b-DQfJHp0CRbtX7Wm7Nu9TQu7rg=', start_index=9523)
Annotation(end_index=9537, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHL7JZaX22s0UNf3WCWMZgVs7XmNl6dCyuTJW6vA1vj7aSnyrnMh5pFRblEr_-2Y6zHXE1734HVUMMRhS0WSd0vsnUrVj_hD9sj64BTDPQFPIVbX2mnXa61d70VMxcz8BYK9UfNpciaZ3NqJdNmCBoIqvd0TY34', start_index=9523)
Annotation(end_index=9766, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHL7JZaX22s0UNf3WCWMZgVs7XmNl6dCyuTJW6vA1vj7aSnyrnMh5pFRblEr_-2Y6zHXE1734HVUMMRhS0WSd0vsnUrVj_hD9sj64BTDPQFPIVbX2mnXa61d70VMxcz8BYK9UfNpciaZ3NqJdNmCBoIqvd0TY34', start_index=9756)
Annotation(end_index=10118, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMY0QX40JTQjoCHbG8yi4SLLTQ0MAn8r5AgoF4HYYyQ8QvEcq-f7OAiNvVcjf5v2v1hfeJSBG6IiJ6hRtkoXoG-nnsYepne0NT9WPFcawh9fpZAAI3EvSrC6xzwSXeEMf9rDlNuhNflB9EeZmjD8EgKLAE1jYPhuScntRIi0lgjDHczShj_e6Jy1J6', start_index=10108)
Annotation(end_index=10387, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMY0QX40JTQjoCHbG8yi4SLLTQ0MAn8r5AgoF4HYYyQ8QvEcq-f7OAiNvVcjf5v2v1hfeJSBG6IiJ6hRtkoXoG-nnsYepne0NT9WPFcawh9fpZAAI3EvSrC6xzwSXeEMf9rDlNuhNflB9EeZmjD8EgKLAE1jYPhuScntRIi0lgjDHczShj_e6Jy1J6', start_index=10377)
Annotation(end_index=10615, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWhUyXfSpO-EWRWqj1EsJMw4qPPd06ql4TVnKw479MmNrQaojwt-2ZM_uznrzRkjp5aUInsWoyaSw3_kbpdOoXHXrsLM22TJPxQu9RLMA_kxujtoqDcA==', start_index=10605)
Annotation(end_index=11734, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEu9nmDcuv7KBkdpaE71D6-IpfUnuzzxsH-OXTdyQ1TsT6aSqLg8igcLFGt5Prq7wTtYv5cRUrAaABCHv6YWfFQm9MlbOwQMQlQAt2kxbZRB3leQurmLqVylBZO3eOkfbOqwQ2Yqwju0BlQTOhy47VnGzpzGIy3tdxJ8QJujeYJmlVUJAK1zQhaJTxfQ-GpacnHT_Q=', start_index=11720)
Annotation(end_index=11734, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuvXKxtrl2VTHaf6NDKlwbeCMwFpQ0yI4lXQQJlc2ZnrJaZHXvkZ0T5JHSCsCCoyrqyPvMLS1iN8UyOZcrm8LN85Ar9UEtif3ekspLj7KKaH5MtvoLDMXO_nwwX8lMAV9zYJfOBM782l_cn1RqhJweXD5gZWbd-uo2G0blZ6O2j_QpPIUsxEINiWQQqm0jyHSHUXv0JiSFhH1NYKXTvioHcZVh5aAbukZUZ01k7TL0Wboa8WBP4pI4dSumMlQ=', start_index=11720)
Annotation(end_index=11878, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEu9nmDcuv7KBkdpaE71D6-IpfUnuzzxsH-OXTdyQ1TsT6aSqLg8igcLFGt5Prq7wTtYv5cRUrAaABCHv6YWfFQm9MlbOwQMQlQAt2kxbZRB3leQurmLqVylBZO3eOkfbOqwQ2Yqwju0BlQTOhy47VnGzpzGIy3tdxJ8QJujeYJmlVUJAK1zQhaJTxfQ-GpacnHT_Q=', start_index=11868)
Annotation(end_index=12427, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEu9nmDcuv7KBkdpaE71D6-IpfUnuzzxsH-OXTdyQ1TsT6aSqLg8igcLFGt5Prq7wTtYv5cRUrAaABCHv6YWfFQm9MlbOwQMQlQAt2kxbZRB3leQurmLqVylBZO3eOkfbOqwQ2Yqwju0BlQTOhy47VnGzpzGIy3tdxJ8QJujeYJmlVUJAK1zQhaJTxfQ-GpacnHT_Q=', start_index=12413)
Annotation(end_index=12427, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFb1AiGYIW0skQ6Nihdlg51Y6XozTuWgvHIGgCkj4NiTUcqZ2p9KbWEcaoVLjnDhgIUz6EkzvN_8Ig5IR_JKtNGdAnW8qfKGxVoh4LGb81S5yZZtj9CRkIms7wKLfZ433EBf3gTHNZEuSRXjpoxhx2XRdfKxg==', start_index=12413)
Annotation(end_index=12714, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEd7e7gh4Jm4MoC7WuqjqQ_dMVpxulIV9g-qel6gk5VtUuoQuWMdnxsi235x8yqqSfccAPbCqj-4euoWYqqMHvlDBuWtSVxGs9pNGolFNldhuUaGSZmK-o_6wXe4Kjq2_uosMCr1T4XULpyCNnRzY2b2V6mAquo5w5vxRc-8fiXJoGxTXuu2cs0wJ1xw1uWojYNnpwAD6Mg6OI=', start_index=12700)
Annotation(end_index=12714, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEu9nmDcuv7KBkdpaE71D6-IpfUnuzzxsH-OXTdyQ1TsT6aSqLg8igcLFGt5Prq7wTtYv5cRUrAaABCHv6YWfFQm9MlbOwQMQlQAt2kxbZRB3leQurmLqVylBZO3eOkfbOqwQ2Yqwju0BlQTOhy47VnGzpzGIy3tdxJ8QJujeYJmlVUJAK1zQhaJTxfQ-GpacnHT_Q=', start_index=12700)
Annotation(end_index=12954, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuvXKxtrl2VTHaf6NDKlwbeCMwFpQ0yI4lXQQJlc2ZnrJaZHXvkZ0T5JHSCsCCoyrqyPvMLS1iN8UyOZcrm8LN85Ar9UEtif3ekspLj7KKaH5MtvoLDMXO_nwwX8lMAV9zYJfOBM782l_cn1RqhJweXD5gZWbd-uo2G0blZ6O2j_QpPIUsxEINiWQQqm0jyHSHUXv0JiSFhH1NYKXTvioHcZVh5aAbukZUZ01k7TL0Wboa8WBP4pI4dSumMlQ=', start_index=12944)
Annotation(end_index=13620, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5ggiMPx2XABjCWwL378Id14YQ8UQD5XQ8cOvhXM_4QKWt0QI7AZdsv66saEtVJImzmGYkYBU4xWmx07y9gbA4y35pTN-pVNuBm7yOWr7XNBAD5i1PmH2MTGrBJk6p9smp1eO7RoZ0SyUY_wAWZ8BuXgg=', start_index=13610)
Annotation(end_index=14012, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEznW5EqBS45w1ANX1NloDIiO2pDQWq7ViLCHev3GUsNabiS0Jw9AqSvZRRHIBwYyr-qsoTWQxKWPM4DhZnvRj2rsphkzCcjGBDeVqFZEsOp6mtmwzzF7tRfZFB9tGHPDt0FcxDfRPT6M7FjnuD2CZfzckY46MuRQ==', start_index=13998)
Annotation(end_index=14012, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpmOpyWhQGfsS_jsEW_IyYzVenwHoSESmY4e8Zp67IQfgYgbL2Mfgct34aB3mOpPUlhN3DdzQV_h-t1y5OudMd0Zg4jS1CpkviiB8T4KvDHWEtnrSk8xp2etQmGd81SIQ-YqB2cYPZoU3SssT-2eeG1cI8O-QkTcIXSEelMGAJIL2QZ2RYvJnAwf-MKAlzD_xWvtUyWeGmPRvhOqyQVgheK4oV5fTg47Xjflsllw==', start_index=13998)
Annotation(end_index=14554, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5ggiMPx2XABjCWwL378Id14YQ8UQD5XQ8cOvhXM_4QKWt0QI7AZdsv66saEtVJImzmGYkYBU4xWmx07y9gbA4y35pTN-pVNuBm7yOWr7XNBAD5i1PmH2MTGrBJk6p9smp1eO7RoZ0SyUY_wAWZ8BuXgg=', start_index=14540)
Annotation(end_index=14554, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFthrKwsr8jgPZ4vQqHW1R-N3ckdU-iVGfK6UhQdvRi1uwnaxlpzqUEO2jm31FMqdnqb0-5mYtwUPaEgQflqKedbjuIhzq-H_M0HWB6EpEKt55sk6ugyQaQsu-TdCPszk3H7ICmp5j1rTVQBlLRfpgUoBA2GlMxr81G4MQCE-ebG9etgA==', start_index=14540)
Annotation(end_index=14913, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5ggiMPx2XABjCWwL378Id14YQ8UQD5XQ8cOvhXM_4QKWt0QI7AZdsv66saEtVJImzmGYkYBU4xWmx07y9gbA4y35pTN-pVNuBm7yOWr7XNBAD5i1PmH2MTGrBJk6p9smp1eO7RoZ0SyUY_wAWZ8BuXgg=', start_index=14903)
Annotation(end_index=15723, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGErBUFrxtXeu7tXSzSDJGrnMUO8DbiI18vE2BeCNSJtowMiNlmiDNS21qIq2Ijojc9ZHpKUp9cZ_ahZWtVgtGMKjgvbI3z0Qf-_RzEjvARTo94jh1NdRZLPZEPq8femU0jPU56Vz4krjZ-m0808fYTf_e4kAl-pSQnT57qgQdY4Eiji6cxYhUmsa5xhiA1mBo7BtriWg==', start_index=15711)
Annotation(end_index=15723, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaVqtwxLB2xEGYsCq56bD4BK_HZiJVd6AM7FmaG574t6O6wS0EsfgOof-jKyimkB23Jm_ipr232SQ9w3RIlgJJXNkAvrIArG8d_FXlN6fFTqBAh6v70I-cpboB1tZMY3KN2OxiPnJLm_gcCgJxfZMERI42UcBOTBVVn0x1k6SwTL8QzPKJfdceDiBYEshUFb_u-QMvc4x4ZQ7ayH_sd_JovPJmy7ghRHAr_lLa9yBGdnb40CYSE4LlkvXnS9xhKpZYW830t1Y8m8pljMpkZH1QftYIMP9RgtzcMcd04rFe4Cjz0ZKm44oJfdAqrX6lwoYc_zfkixVHwZxnmlrNY5LIoNdykHjdPd63x-nDAltbTU8=', start_index=15711)
Annotation(end_index=16139, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIqK9WcMoDnqu9nUu6wfi3A2wPXlk3uQgkSFmD-CRxJPGiLZIkFGbglKijwz3QumkVWLVfijrNQ7I-vcA4aUOa_hc7y0AF05cgQg7SAFwyvT5ecvSN8-ae5SLcoX5V_Pg=', start_index=16130)
Annotation(end_index=16442, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWhUyXfSpO-EWRWqj1EsJMw4qPPd06ql4TVnKw479MmNrQaojwt-2ZM_uznrzRkjp5aUInsWoyaSw3_kbpdOoXHXrsLM22TJPxQu9RLMA_kxujtoqDcA==', start_index=16429)
Annotation(end_index=16442, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIqK9WcMoDnqu9nUu6wfi3A2wPXlk3uQgkSFmD-CRxJPGiLZIkFGbglKijwz3QumkVWLVfijrNQ7I-vcA4aUOa_hc7y0AF05cgQg7SAFwyvT5ecvSN8-ae5SLcoX5V_Pg=', start_index=16429)
Annotation(end_index=17858, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4CVs6y3l-jMRYuLfIaclv1VNzPgTQaev3nY_IPCGpYtoimMyMk0ELgjrEV8Ui1ZisK5iG8ooZBvTnMv_JPNCBr0U4HHDqf7Se4pr8ZPNqFocKk4Exx9_vjaYnb2y1NmOrNyn53jIf2Q3AeFk2If_D5hW-Ue8Mmtvo2G_7Y0vn5ler0wqw_MFo03hzCKZ35YaUTPUD66JsUO5XfAthJWPWOAAxQ1tK0-M3C_NTk6DSnsS3MtVfYj8_IYj0sY8i2gZ1s72z32ltlPMmd3RbI2sEoO8lUnqOKPabro5vw_j-F3bnN-TFkWTDmSRI7OWyiakmmNIW0eFTpVnzGVwK9QcaJjZLJs3DFkg=', start_index=17849)
Annotation(end_index=17952, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGErBUFrxtXeu7tXSzSDJGrnMUO8DbiI18vE2BeCNSJtowMiNlmiDNS21qIq2Ijojc9ZHpKUp9cZ_ahZWtVgtGMKjgvbI3z0Qf-_RzEjvARTo94jh1NdRZLPZEPq8femU0jPU56Vz4krjZ-m0808fYTf_e4kAl-pSQnT57qgQdY4Eiji6cxYhUmsa5xhiA1mBo7BtriWg==', start_index=17940)
Annotation(end_index=17952, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaVqtwxLB2xEGYsCq56bD4BK_HZiJVd6AM7FmaG574t6O6wS0EsfgOof-jKyimkB23Jm_ipr232SQ9w3RIlgJJXNkAvrIArG8d_FXlN6fFTqBAh6v70I-cpboB1tZMY3KN2OxiPnJLm_gcCgJxfZMERI42UcBOTBVVn0x1k6SwTL8QzPKJfdceDiBYEshUFb_u-QMvc4x4ZQ7ayH_sd_JovPJmy7ghRHAr_lLa9yBGdnb40CYSE4LlkvXnS9xhKpZYW830t1Y8m8pljMpkZH1QftYIMP9RgtzcMcd04rFe4Cjz0ZKm44oJfdAqrX6lwoYc_zfkixVHwZxnmlrNY5LIoNdykHjdPd63x-nDAltbTU8=', start_index=17940)
Annotation(end_index=18105, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEu9nmDcuv7KBkdpaE71D6-IpfUnuzzxsH-OXTdyQ1TsT6aSqLg8igcLFGt5Prq7wTtYv5cRUrAaABCHv6YWfFQm9MlbOwQMQlQAt2kxbZRB3leQurmLqVylBZO3eOkfbOqwQ2Yqwju0BlQTOhy47VnGzpzGIy3tdxJ8QJujeYJmlVUJAK1zQhaJTxfQ-GpacnHT_Q=', start_index=18087)
Annotation(end_index=18105, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuvXKxtrl2VTHaf6NDKlwbeCMwFpQ0yI4lXQQJlc2ZnrJaZHXvkZ0T5JHSCsCCoyrqyPvMLS1iN8UyOZcrm8LN85Ar9UEtif3ekspLj7KKaH5MtvoLDMXO_nwwX8lMAV9zYJfOBM782l_cn1RqhJweXD5gZWbd-uo2G0blZ6O2j_QpPIUsxEINiWQQqm0jyHSHUXv0JiSFhH1NYKXTvioHcZVh5aAbukZUZ01k7TL0Wboa8WBP4pI4dSumMlQ=', start_index=18087)
Annotation(end_index=18105, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFb1AiGYIW0skQ6Nihdlg51Y6XozTuWgvHIGgCkj4NiTUcqZ2p9KbWEcaoVLjnDhgIUz6EkzvN_8Ig5IR_JKtNGdAnW8qfKGxVoh4LGb81S5yZZtj9CRkIms7wKLfZ433EBf3gTHNZEuSRXjpoxhx2XRdfKxg==', start_index=18087)
Annotation(end_index=18209, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5ggiMPx2XABjCWwL378Id14YQ8UQD5XQ8cOvhXM_4QKWt0QI7AZdsv66saEtVJImzmGYkYBU4xWmx07y9gbA4y35pTN-pVNuBm7yOWr7XNBAD5i1PmH2MTGrBJk6p9smp1eO7RoZ0SyUY_wAWZ8BuXgg=', start_index=18199)
Annotation(end_index=18343, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEznW5EqBS45w1ANX1NloDIiO2pDQWq7ViLCHev3GUsNabiS0Jw9AqSvZRRHIBwYyr-qsoTWQxKWPM4DhZnvRj2rsphkzCcjGBDeVqFZEsOp6mtmwzzF7tRfZFB9tGHPDt0FcxDfRPT6M7FjnuD2CZfzckY46MuRQ==', start_index=18329)
Annotation(end_index=18343, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpmOpyWhQGfsS_jsEW_IyYzVenwHoSESmY4e8Zp67IQfgYgbL2Mfgct34aB3mOpPUlhN3DdzQV_h-t1y5OudMd0Zg4jS1CpkviiB8T4KvDHWEtnrSk8xp2etQmGd81SIQ-YqB2cYPZoU3SssT-2eeG1cI8O-QkTcIXSEelMGAJIL2QZ2RYvJnAwf-MKAlzD_xWvtUyWeGmPRvhOqyQVgheK4oV5fTg47Xjflsllw==', start_index=18329)
Annotation(end_index=18433, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIqK9WcMoDnqu9nUu6wfi3A2wPXlk3uQgkSFmD-CRxJPGiLZIkFGbglKijwz3QumkVWLVfijrNQ7I-vcA4aUOa_hc7y0AF05cgQg7SAFwyvT5ecvSN8-ae5SLcoX5V_Pg=', start_index=18424)
Annotation(end_index=18528, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWhUyXfSpO-EWRWqj1EsJMw4qPPd06ql4TVnKw479MmNrQaojwt-2ZM_uznrzRkjp5aUInsWoyaSw3_kbpdOoXHXrsLM22TJPxQu9RLMA_kxujtoqDcA==', start_index=18518)
Annotation(end_index=18650, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEi9Syn8c2CTBr8FZ3V6qtakgYnBXAQ0Nz37pVF93BzDXJDMLsVLkL9kQN68jjyxBlxq09vYxUVhkjff9APhWyMCEzxmyyZMgTRVvtNuMUYxtOsm624cxtzgQKuqqEGliuee9LJYuUdAYJJggD_s8CgyKqf7789h9Q9PK_ZXZtT-PQ5VxRokWbnY1kOzqkLNPJvyS0kh3khAwDkTFwIFHgMu6KcKiHw2PvsA_HKeqzO9PbQ3btDtbF0', start_index=18632)
Annotation(end_index=18650, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMCq59RlksyyqrINu5P3r71Z0S0jEMwM4tVxeyTUaW6py5mVKOn6IMb9hR21j5uXmBGTzh1cW8QjVM7KfJBwl3ViUTOxBq8FzI0mI4hQZQnTb-8Oj6GBgFgnp_2KGmidppHZZCfgHKtcWKxaUwdBpvqQs=', start_index=18632)
Annotation(end_index=18650, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4CL8jd4NbwPTfZov_s_2Dd7__0EAWYB3F9R7iBpRZ2PSCdBvi2QEBozqOZLZc9jDw4YsBZH2p-m41goSRdpj3lo_ogCHax5-f5lMuW1MTb0Pji-aNjNraBSImFohk62U41vmFvyiyVDs3rgmLqQ==', start_index=18632)
Annotation(end_index=18775, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMY0QX40JTQjoCHbG8yi4SLLTQ0MAn8r5AgoF4HYYyQ8QvEcq-f7OAiNvVcjf5v2v1hfeJSBG6IiJ6hRtkoXoG-nnsYepne0NT9WPFcawh9fpZAAI3EvSrC6xzwSXeEMf9rDlNuhNflB9EeZmjD8EgKLAE1jYPhuScntRIi0lgjDHczShj_e6Jy1J6', start_index=18765)
Annotation(end_index=18859, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoh_yVvB8OZ_Kkv7lM2ab3cuqOqQhY8-dxWUgmjRGrHjksKNE_AivtgaxtCRjbHEdxT4egh8gAISBoPGGmF0NM6Gzz0nuwyYR7SvmJA79J0gPa11wJwfEym8qBQTisXbvnFIjaL9fwNjsIBLFTamd5DCsJAesRm3sDYXGR4rw5dn-DFI8gnmJVByXqCZS0KIh6GV0=', start_index=18850)
Annotation(end_index=18923, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGefq_wccGoFVCx5tuvZrxccWgT6hdP5mz4mQSgV281pQKnRlj2rckQrpycAKLtJLrFlEazpdVOil7DzfPWK955mNtiEJ0s_Ww4v_5RiegKzdvO_C3Ga_g32P4NSmAADaCBfhpKau3kLNdfRDIOPW4SKmYzOi3zRW7vdkGndldCEUoYlHD_-TZFaHBbgEh8Syjas7Z0rxDyiQA03qsC4pmQsiiX-KzpCEZdJKT23JxImyt0A75Rcw5ISwIhnLU22R9J2mkUz8_kFQjFy-ae', start_index=18914)
Annotation(end_index=19002, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9Krv733tmFuAPQsU60kPrdQ8WSNVhdQrST3ccf-FMBIXsHL5Mikho9FxnC3JGtOPEDTYPuZ1ywMv3vkN-s7RlIL_7YXNZRPcpjG0LyOCSBVNEqEnkVyAXIxvFR65SBZyj-XKYXLHDtHvLf51kaQ107qE=', start_index=18990)
Annotation(end_index=19002, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiurr9TJ2TXj0M09TGle2Xs8Y6Ib-i4euqUfeqBJlsNUieAZXw6KQmadVC9Up-GAU0tneRj7BZ6FGITA9qyna-6PBZ-uTmy2Q7Q4UjEY57afnBVj6ivau6OpU3r923jF7A-T6_ODWqgL71i9oDlSFFdP0=', start_index=18990)
Annotation(end_index=19108, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRIB68u8WQEXRh9DUWohIf4o_UnOxDQRmctu5D69Rg7SY3ievrdBE5WDxEec4t-Nf3W4bRKujlLB1ZmvsnJEIcluOWIvnomkB2o_UNYtueY7ps5ov98pLinYnuxwEnfykkiDgOuxsBWJAVO0gdJLLQltm186Rxj2IRKi-e4EiLg6SjUGmBNHZD', start_index=19095)
Annotation(end_index=19108, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1YoA4v4Wd4pXZO0mzMLAGT0LvsuW79oBMbDTf9YlqFDIiI_gmMyo25gGgywq4mdTAVRVhh4qSQnOmDShPMQDNqjOrgKzg1_ZW-qYaQeQtLLf0Kn5aE8kIqYf00o_NXHNEZneO-hupwqluOSs4zzqLQuIYliBI3dPKV2D1t4HyLsEcMVFRCYMyLoDC5Yn-bT19GPdwNZuezmo2txNMDxYCHME-hfcGnibtZtm1RieEXRz8LJuq30vlE9tkDFuovtxBs4dK', start_index=19095)
Annotation(end_index=19198, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHL7JZaX22s0UNf3WCWMZgVs7XmNl6dCyuTJW6vA1vj7aSnyrnMh5pFRblEr_-2Y6zHXE1734HVUMMRhS0WSd0vsnUrVj_hD9sj64BTDPQFPIVbX2mnXa61d70VMxcz8BYK9UfNpciaZ3NqJdNmCBoIqvd0TY34', start_index=19188)

## Sources
