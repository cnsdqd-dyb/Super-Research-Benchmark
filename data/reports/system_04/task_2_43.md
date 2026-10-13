# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 6ee9f673 | **Time:** 365.86s | **Cost:** $1.16153
--------------------------------------------------------------------------------

# Graph Theory Algorithms in Financial Networks: Balancing Connectivity, Complexity, and Convergence

### Key Points
*   **The Connectivity-Complexity Trade-off:** Financial networks exhibit a "robust-yet-fragile" architecture. While increased connectivity (edges) improves risk diversification and liquidity provision under normal conditions, it creates channels for contagion during crises. Research indicates a "Price of Complexity," where intricate interdependencies increase the error margin in estimating systemic risk, potentially negating the benefits of diversification.
*   **PageRank Convergence and Sparsity:** Contrary to the premise that sparsity fundamentally limits convergence, sparse matrices actually enable the computational feasibility of PageRank on massive graphs by reducing memory requirements from $O(N^2)$ to $O(N)$. However, the *rate* of convergence is dictated by the spectral gap (the difference between the first and second eigenvalues), which is controlled by the damping factor ($\alpha$). As $\alpha$ approaches 1 (mimicking a system with no friction/decay), convergence slows drastically regardless of sparsity.
*   **Algorithmic Control:** Graph theory offers mechanisms to balance these forces. "Pinning control" algorithms allow regulators to stabilize vast chaotic networks by targeting a small fraction of influential nodes (identified via centrality metrics like PageRank or DebtRank). This suggests that while complexity cannot always be reduced, it can be managed through targeted intervention.

---

### Executive Summary
The application of graph theory to financial systems reveals a fundamental tension between the optimization of network flow (capital efficiency) and the control of systemic risk (complexity management). Financial institutions form complex networks where nodes represent entities (banks, firms) and edges represent financial exposures (loans, derivatives). Algorithms derived from graph theory, such as PageRank and its financial derivatives (e.g., DebtRank), are pivotal in identifying systemic importance. However, the user’s query touches upon two critical technical and theoretical constraints: the "robust-yet-fragile" nature of connectivity and the numerical stability of ranking algorithms in sparse environments.

Research suggests that graph theory algorithms can indeed balance connectivity and complexity, but this requires moving beyond simple topology optimization to dynamic control strategies. The "Price of Complexity" framework demonstrates that as networks become more interconnected and opaque, the computational error in risk estimation grows, often outpacing the benefits of risk sharing. Regarding PageRank, the convergence is not fundamentally limited by sparsity itself—sparsity is a computational prerequisite for large-scale graphs—but rather by the spectral properties of the transition matrix, specifically the damping factor which models the probability of random jumps (or in finance, exogenous liquidity shocks).

---

## 1. Introduction: The Graph Theoretic Foundation of Systemic Risk

Modern financial systems are quintessential complex networks. They are characterized by a web of direct exposures (interbank loans, derivatives) and indirect exposures (common asset holdings). Graph theory provides the mathematical formalism to model these systems, where $G = (V, E)$ represents the financial system, with $V$ being the set of institutions and $E$ the set of financial contracts [cite: 1, 2].

The analysis of these networks has shifted from static topological descriptions to dynamic algorithmic assessments. The central challenge in this field is the "connectivity vs. complexity" trade-off. High connectivity is often incentivized by market forces to maximize liquidity and risk sharing. However, this same connectivity creates "super-spreaders" of default risk. Algorithms must therefore not only quantify centrality (who is important) but also simulate dynamics (how distress propagates).

Furthermore, the computational efficiency of these algorithms is paramount. As financial networks grow in size and granularity, the numerical methods used to solve for equilibrium states (such as PageRank for centrality or Eisenberg-Noe for clearing vectors) face constraints related to matrix sparsity and convergence speeds.

## 2. The Connectivity Optimization vs. Complexity Control Trade-off

The question of whether algorithms can balance connectivity and complexity addresses the heart of macroprudential regulation. The literature identifies distinct phenomena that govern this balance.

### 2.1 The "Robust-Yet-Fragile" Paradigm
Financial networks display a property known as "robust-yet-fragile." In a highly connected system, small, idiosyncratic shocks are easily absorbed and dissipated across the network, making the system robust to standard volatility. However, this same connectivity acts as a conduit for contagion during major distress events.

*   **Risk Sharing vs. Contagion:** Increased connectivity allows counterparty losses to be dispersed among many creditors, lowering the probability of an initial default cascading. However, conditional on a cascade starting, high connectivity ensures it spreads wider and faster [cite: 3, 4].
*   **Threshold Effects:** Research indicates that a medium density of connections is often sufficient to induce this robust-yet-fragile state. Beyond a certain point, adding more connections yields diminishing returns for stability while increasing the potential for catastrophic systemic collapse [cite: 5].
*   **Algorithmic Implication:** Optimization algorithms cannot simply maximize connectivity. They must optimize for a topology that retains "firebreaks" or modularity to halt contagion, effectively curbing complexity to control systemic risk [cite: 6].

### 2.2 The Price of Complexity
A critical theoretical advancement is the concept of the "Price of Complexity," introduced by Battiston et al. This theory posits that complexity in financial networks—defined by the intricacy of interlaced contracts and derivatives—imposes a limit on the accuracy of risk estimation.

*   **Estimation Error:** As the network becomes more complex, the error in estimating the probability of systemic default increases. Small errors in the knowledge of the network structure or asset values can lead to disproportionately large errors in risk assessment [cite: 7, 8].
*   **Moral Hazard:** Complexity creates information asymmetries. If the impact of a default is difficult to compute due to network complexity, institutions may gamble on being "Too-Complex-To-Fail," expecting public bailouts because regulators cannot accurately gauge the fallout. This incentivizes further complexity, creating a destabilizing feedback loop [cite: 7, 9].
*   **Control Limitations:** The "Price of Complexity" suggests that there is a fundamental limit to balancing connectivity and control. If the network is too complex, algorithmic control becomes unreliable because the input parameters (probability of default, recovery rates) are subject to high uncertainty [cite: 8].

### 2.3 Topological Determinants of Stability
Graph theory algorithms analyze specific topologies to manage this trade-off.
*   **Core-Periphery Structures:** Real-world interbank markets often exhibit a core-periphery structure, where a tight core of large banks intermediates for a vast periphery of smaller banks. This structure is efficient for liquidity distribution but concentrates systemic risk in the core [cite: 5, 10].
*   **Scale-Free Networks:** Financial networks often follow power-law degree distributions (scale-free), meaning a few hubs have massive connectivity. While robust to random failures, these networks are highly vulnerable to targeted attacks or failures of the hubs [cite: 10, 11].
*   **Dissortativity:** Some interbank networks are disassortative (highly connected nodes link to poorly connected ones), which can dampen contagion compared to assortative networks where hubs link to hubs [cite: 12].

## 3. PageRank in Financial Networks: Convergence and Sparsity

PageRank, originally designed for the Web, has been adapted for finance to measure the "centrality" or systemic importance of institutions. The user asks if PageRank convergence is fundamentally limited by graph sparsity. The answer requires a nuanced understanding of numerical linear algebra.

### 3.1 The Mechanics of PageRank and Sparsity
PageRank calculates the stationary distribution of a random walk on the graph. It solves the equation $r = M r$, where $M$ is the stochastic transition matrix.
*   **Sparsity as an Enabler:** Financial networks, like the Web, are sparse (most banks do not lend to most other banks). If $N$ is the number of nodes, a dense matrix requires $O(N^2)$ memory, which is infeasible for large $N$. Sparsity allows the matrix to be stored in $O(N + E)$ space (where $E$ is edges) using formats like Compressed Sparse Row (CSR) [cite: 13, 14].
*   **Computational Efficiency:** The primary algorithm for PageRank is the **Power Method**, which involves repeated Sparse Matrix-Vector Multiplications (SpMV). Sparsity makes SpMV efficient, reducing the complexity of each iteration. Therefore, sparsity *enables* rather than limits the computation [cite: 15, 16].

### 3.2 Convergence Limitations: The Spectral Gap
The convergence speed of PageRank is not determined by sparsity, but by the **spectral gap** of the transition matrix.
*   **The Damping Factor ($\alpha$):** The transition matrix $M$ is usually defined as $M = \alpha S + (1-\alpha)E$, where $S$ is the network structure and $E$ is a teleportation matrix (jumping to random nodes).
*   **Eigenvalue Dependence:** The convergence rate of the Power Method is determined by the ratio $|\lambda_2| / |\lambda_1|$, where $\lambda_1 = 1$ is the principal eigenvalue. In the standard PageRank formulation, the second eigenvalue $|\lambda_2|$ is exactly equal to the damping factor $\alpha$ [cite: 17, 18].
*   **The Trade-off:**
    *   **Low $\alpha$ (e.g., 0.85):** Fast convergence (fewer iterations). The random surfer "teleports" often, reducing the influence of the graph's specific topology (traps, cycles).
    *   **High $\alpha$ (e.g., 0.99):** Slow convergence. The surfer follows links for a long time. This captures the true long-range structure of the network but makes the computation expensive and sensitive to stability issues [cite: 18, 19].
*   **Sparsity's Role in Convergence:** While sparsity allows fast iterations, it does not dictate the *number* of iterations. However, in extremely sparse graphs (like trees or disconnected components) without a damping factor ($\alpha=1$), the Power Method may fail to converge due to cycles or reducibility (probability mass getting stuck in "sinks"). The damping factor is the mathematical "fix" for these sparsity-induced topological problems [cite: 20, 21].

### 3.3 Financial Interpretations of PageRank Convergence
In finance, the damping factor has an economic interpretation.
*   **Exogenous Liquidity:** The teleportation component $(1-\alpha)$ can be modeled as exogenous liquidity supplied by a central bank or external investors.
*   **Friction:** A high $\alpha$ implies a closed system where distress circulates almost indefinitely (high systemic risk). A lower $\alpha$ implies a system with "friction" or external bailouts that dampen shock transmission.
*   **DebtRank:** A modification called DebtRank is often used, which accounts for the specific balance sheet impact (leverage) rather than just connectivity. DebtRank does not assume a steady state (convergence) but measures the cumulative loss over time, avoiding some of the convergence debates of standard PageRank [cite: 22, 23].

## 4. Algorithmic Approaches to Complexity Control

Given the risks associated with complexity, researchers employ various algorithmic strategies to monitor and control financial networks.

### 4.1 Network Reconstruction Algorithms
A major hurdle in financial network analysis is data opacity. Regulators often know the total assets and liabilities of banks but not the bilateral links.
*   **Maximum Entropy:** Algorithms like Maximum Entropy Estimation (MEE) reconstruct the most probable network structure given the aggregate constraints. These methods tend to create fully connected (dense) networks, which may underestimate systemic risk by diluting concentration [cite: 10, 24].
*   **Stochastic Reconstruction:** More advanced algorithms (e.g., Lux's algorithm) generate stochastic networks that match stylized facts (sparsity, power-law distributions) better than MEE. These are crucial for stress testing "what-if" scenarios [cite: 11, 25].

### 4.2 Pinning Control for Stability
To manage the "robust-yet-fragile" nature, control theory offers **Pinning Control**.
*   **Mechanism:** Instead of regulating every institution (which is costly and complex), pinning control identifies a minimal set of "driver nodes" or "pinned nodes." By applying feedback control (e.g., capital requirements, liquidity injections) to just this subset, the entire network can be steered toward a stable equilibrium [cite: 2, 26].
*   **Selection Algorithms:** The selection of pinned nodes is non-trivial. It relies on centrality measures (PageRank, Betweenness) to find nodes that have the highest influence on the network's dynamics. This bridges the gap between connectivity optimization and complexity control [cite: 27].

### 4.3 Machine Learning and Nonlinear Dynamics
Recent approaches integrate Machine Learning (ML) with graph theory.
*   **XGBoost and Random Forests:** These are used to predict systemic risk contributions based on both node-level financial variables and topological features. Research shows that topological features (centrality) are dominant drivers of systemic impact during high-stress periods [cite: 22, 28].
*   **Continuum Limits:** For very large directed graphs, PageRank and similar processes can be modeled using partial differential equations (PDEs) in the continuum limit. This allows for the analysis of stability and regularity in massive financial networks where discrete matrix operations become cumbersome [cite: 29].

## 5. Computational Challenges: The Sparsity Bottleneck

While sparsity enables storage, it introduces the **SpMV Bottleneck** in high-performance computing.
*   **Irregular Memory Access:** Sparse matrix-vector multiplication involves irregular memory access patterns, which are inefficient on modern CPUs/GPUs compared to dense matrix operations. This is the main computational bottleneck for calculating PageRank on billion-node graphs [cite: 14, 16].
*   **Optimization Techniques:**
    *   **Loop Fusion & Reordering:** Compilers can optimize SpMV by reordering the matrix (e.g., reducing bandwidth) to improve cache locality [cite: 30, 31].
    *   **Approximation:** Algorithms like "FusEd-PageRank" or local approximation methods estimate PageRank without traversing the entire graph. However, local approximation is theoretically difficult on graphs with high in-degree nodes (common in finance), suggesting that global computation is often necessary [cite: 30, 32].
    *   **Gaussian Elimination Failure:** Direct solvers like Gaussian elimination are generally avoided because they induce "fill-in"—creating non-zero elements in the matrix during computation—which destroys sparsity and causes memory overflow [cite: 13].

## 6. Conclusion

Graph theory algorithms in financial networks operate within a constrained optimization space defined by the "robust-yet-fragile" dichotomy.
1.  **Balancing Connectivity and Complexity:** Algorithms *can* assist in balancing these forces, but not by simply maximizing connectivity. Instead, they must be used to design topologies that allow for risk sharing while implementing "pinning controls" on central nodes to prevent contagion. The "Price of Complexity" imposes a theoretical limit: as networks grow more complex, the ability of any algorithm to accurately estimate risk diminishes, necessitating structural simplification or higher capital buffers.
2.  **PageRank and Sparsity:** PageRank convergence is **not** fundamentally limited by sparsity. Sparsity is the feature that makes PageRank computationally viable. The limitation lies in the **spectral gap** (controlled by the damping factor). In financial contexts, a damping factor close to 1 (representing a highly liquid, frictionless market) causes slow convergence and sensitivity to errors, reflecting the economic reality that highly interconnected, frictionless markets are prone to prolonged instability.

Ultimately, the effective management of financial networks requires a hybrid approach: using graph algorithms to reconstruct and monitor the topology, employing spectral methods (like PageRank/DebtRank) to identify systemic cores, and applying control theory (pinning) to impose stability constraints on the most complex components of the system.

---

## 7. Detailed Analysis of Research Findings

### 7.1 The "Price of Complexity" in Depth
Battiston et al. [cite: 7, 8] provide a rigorous quantification of why complexity control is difficult. They define a financial network $G$ and a leverage matrix $\Lambda$. The value of interbank assets depends on the survival of counterparties.
*   **The Equation:** The equity of bank $i$ is $E_i = A_i^{ext} + \sum_j \Lambda_{ij} E_j - L_i$. This creates a system of coupled equations.
*   **The Result:** As the number of paths in the network increases (complexity), the sensitivity of the solution (the equity values) to small perturbations in the parameters (asset values) grows.
*   **Implication:** Regulators might observe a network and calculate that it is stable. However, if the "Price of Complexity" is high, a 1% error in estimating a bank's external assets could flip the algorithmic output from "Stable" to "Systemic Collapse." This proves that connectivity optimization without complexity limits is dangerous.

### 7.2 Pinning Control Mathematics
The dynamics of a financial network under control can be described as:
$$ \dot{X}_i = F(X_i) + c \sum_{j=1}^N a_{ij} H(X_j - X_i) - g_i (X_i - X_r) $$
Where:
*   $F(X_i)$ is the intrinsic dynamics of bank $i$.
*   The summation term represents the coupling (contagion/influence) from other banks.
*   $g_i$ is the **pinning control gain**. If node $i$ is pinned, $g_i > 0$; otherwise $g_i = 0$.
*   $X_r$ is the reference state (stability).
Research [cite: 2, 27] shows that selecting the nodes with the highest PageRank or Degree Centrality to be "pinned" (high $g_i$) is the most efficient way to force the synchronization of the network to a stable state $X_r$.

### 7.3 PageRank Convergence Rates
The error in PageRank at iteration $k$ is approximately proportional to $\alpha^k$ [cite: 33].
*   If $\alpha = 0.85$, error drops quickly.
*   If $\alpha = 0.99$, error persists for hundreds of iterations.
*   **Financial Context:** In a stress scenario, trust evaporates, and the effective "damping factor" (willingness to lend) might drop, fragmenting the network. Conversely, in a boom, $\alpha$ is high, connectivity is high, and the system is computationally and economically slow to resolve imbalances (slow convergence).

### 7.4 Algorithmic Scalability on Supercomputers
Recent work on the Fugaku supercomputer [cite: 14] demonstrates that PageRank can scale to graphs with billions of nodes using distributed computing.
*   **Weak Scaling:** The algorithm maintains efficiency as the graph size grows, provided the number of processors grows.
*   **Communication Overhead:** The limit is not the computation but the communication of the rank vector $r$ between nodes.
*   **Sparsity Formats:** Using CSR (Compressed Sparse Row) or ELL formats is crucial. The "fill-in" phenomenon of Gaussian elimination [cite: 13] is strictly avoided in favor of iterative power methods.

## 8. Synthesis of Conflicting Views
*   **View A (Optimization):** Higher connectivity is better because it dilutes idiosyncratic risk. Algorithms should optimize for maximum flow and risk sharing [cite: 3].
*   **View B (Control):** Higher connectivity creates "too-connected-to-fail" entities and contagion channels. Complexity must be penalized or capped [cite: 7].
*   **Resolution:** The "Robust-Yet-Fragile" model reconciles these. Connectivity is good up to a point (phase transition), after which it becomes detrimental. Algorithms must detect this phase transition. Pinning control allows for high connectivity *if* the central nodes are heavily regulated (pinned).

## 9. Conclusion on the User's Specific Query
*   **Can algorithms balance connectivity and complexity?** Yes, but it requires a shift from purely descriptive metrics (like simple centrality) to **control-theoretic** approaches (Pinning Control) and **probabilistic** approaches (Price of Complexity) that explicitly account for error propagation and contagion dynamics.
*   **Is PageRank convergence limited by sparsity?** No. Sparsity is a facilitator. Convergence is limited by the **damping factor** (spectral gap) and the presence of specific topological structures (like reducible components) that require teleportation to resolve. In financial terms, this means that without "teleportation" (external liquidity/bailouts), a purely internal interbank market might not reach a stable equilibrium during a crisis.

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkH0YpLeRUwJ9DZRBjId_6YSkAct5owqxosPvGbFWrbTZt7h6PTiaoqLgnG_O_mDPLKbgcCA7OpdMPNqBNU6F-yEFdePxb0JoSjunkYCWEs_O1-dJ62gSBIUTBn0h7prOPO7pUJ-b0ZbDh-kTufgDLhMePnUo80XOrkGsmAGYK9oTSIQ==)
2. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE31RJgzoqX10T1_0UN5CQnQKGbOWVyfIheFCEVxLnGw4qyOG8cJiQYhWOMnCbXruOQ1oyZubP2jtVtI7EWwRHcy1ld50TqZmUYBSy6Vvx-mZ9iZ-HZuxckSHVJLiS7FQ==)
3. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6_cXwtyhyXfj6IboU0p7TVU_2e8fhtZe5pyozvYHYL4DcP4leuHR7MB_6JWqFGokgWuEf_mKVMoZmzmY6-dTouk8lefO07LPJYVhCd0dFKIINS6Wk7qKOU2l1V8V95cK1oiHhY2Q6O7xFvA==)
4. [bankofengland.co.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxdbcB3iXCNBk2D_2xDxLCyMxW9M6qebV5RjleyPY4qDlR1fuuTlTDrgrPj9DxuaTqqHns-JrxWVH9BZhughBHNwQ9fUzx3tESPVvvJLO0U7t8RTObpiozaSp0zDmT_MtcnXbwN8Dl77fsZUY_8TAt9DxipRsBKWhQgWuZm_ZYzXsqIf8EkaOYxj7IxIQqperk0-U7axEsNad_LPbK9A==)
5. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUqwN5bUX0lVkJCtVJ6-G5d2Oh2qXrredXTCnRs4vwcnJN-uqsCVqhL0vkIJ5s3mj6BrADB5QtIpFjWJQKBoGfnCZxzAkg8Zj3dVlIPRJN-1pMhDMwikCnRit0Zy28CZtUyz9riT-Z)
6. [simudyne.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo65hHdIdW1bMRgGDY0TgI5qm0p2eM4byzW_gs1PoyVLi2He1LEqLVVUxZr20tGdncjlYT4Sfkgk9GIOLSfFBY8G5hbokBAS_oZxmsjsxx5GiyGsvIZZK5kwaLPWGZitHW79Gm6rjBl-DCIkDC3SI9PNbezDiutYLgwaDY8XfrKqvGL1hZ7_lTnw7p3Q==)
7. [pnas.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbAhtE5Tq8t5s3T84IH5wkV7kvPJciE3g8mdKSDILFC3C5ggm1gVPr8mEqRifNr6WGsivf7Z3sd32JQUbHxANVS4IDbpsnczFyXOsEs-9A2kXy-7x7G2qJ_c2d81nS2njJxXgqOzM=)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHOPJwuFnpVBJJn6uLkqrPVCOrmjV97NOTdpXLEsT8S4jAvPyIyQE7XYqAA0iaB-CSnFpkf3ovu9AuiyDkOt9j_2xbFrTA5xiZAnqQZJLibVp80XB3qu0Ti7CNJwDSdA==)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFt7U3obkzYBhLNdJBF7TV7YYJF_6jXQ5e2swZxJQwfQI0q-42ojQTd2oLWNUxMAFTFgl0HmvnTG9-BgRbtP8vT4k4v4j4HyIJtcX7mdSt8iWe-JNs5oxdWV77N3jfmSNM00L_mZ23w)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQQ6B3ra1UDyQUNEDFJziL6cYhtvYXUmLuRogZvT--R-yov8Cd3hpKSVXKvZnFj4N6qzqOPXxTlS4nY0Cl5e9kbVzCphK_Teeuuvu5ohKcb3V_3R-IxeEvC0H9iw6iCav2OXlDpaJjmohClWeawlDKWTo1t-tRim3wXSTO_C22evv8yYBQ1CmK7rMXk8rav8eFkRk=)
11. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbXSLTUAp2TD3n24UtmMaPu47ndOXNQqqKnMm_jn8x8mCVdhBJPCTUJ2YKoEtkMiTWEDmAz9ZMHY8qEX0Q3m2Jxm5sWeikil-ypNiKagYPnPj-UgOZ7AtjNfsdZQYt)
12. [bbvaresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIVYm18WLJopBuiYw8FLNs2HWTw2bJ8rYNQ2N3IvPCwC5oNZumvvg_rCEXJQFfWZAGlat2kA38rKYlo3DzlsP22HpNZWi39I4szRDPsEYPAGtpahpm7GBdt9QY38bRVLXUtuGH8b2lV5SZKlK7-tn22_SYvKLWx-F4s9iuhBs2aK9WWje4DU6HADtQ60BkYzB61iDEkozKNPRosJC84tP68-iKm__nmggScIztgDZdfd-bhx9N)
13. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWmtexSOcZ3ft6BEKiHv0zaZzeRA6FSGitsoT-Mdc7CQQjXuUV75wfQlDoD2Q7IG3iYWYwWvgJzVRJ_DEPKaBLm7P-PiP5MwxOBamgJ9FTFZ7B5KL5J9gr2P8B2fXfaKfCXFUChf9JmdiZVeNhuvDVi4MZRcAucn3FVYnhT70I10jg_ZFt)
14. [iccs-meeting.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGX3_Dybyg18fyxeEspoaQpevDdK1vBbWALmc447CjeRZjwllmZg1xXlYZOKPTp-fUI8QM6kRTbBIO3n939OysXQtoPxXrLHgVUcjWe1ylFmhxYybW5h-ivzjW9YCVrlIUlGYkIaUNzLXqAMKVaPHRWBcAjKNKSk1Y=)
15. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTnQ0OEGyhfam2GI2lZqYibFgo5iERn1qkm3lA4ToyOBovhiZqggr6b1XU6KmnJIHF007cZM8nyYdQ1mm98cDeqM_QyuoxUXMu06Ip4yaYMs2R6S2q8rtjdxTdBhLOer4oAudpEATeiNFqjh3YhdMBWgV5cM5OBKD71i8=)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwzXCSfx2z_vBWsm_x353swOmg4z7kBXIEN7U3HrQy0uXE-J_LSfS2oKv05W_PS5VcQKy6j7RkykIPln5HtL4-QnJG1UV1Zo8iaWutauZWuLKaZgYPmNjSEJg7xyOfVIU56HcxU0umgXMEL1zDmfgMVR3fdKkh_ZiH8WhyEIxXyMwUzf4ISgmXJP8ghV5sgJcQupVfODe_npKR-mF0khcjsLx_MgEmX26UrHz44d2JN3Iae7CZTLm69gFNorWDcw==)
17. [stackexchange.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXSeFjwbQaS_8_GZiI8kW6EPCR8_sHVy-9pp617hxVM3juOFfmwL6ZKzMTQIW2jiByJ8ZWd_GNYw52AF1IQoGvfjnFv0nd6dC2O2FnFYosOMybSHhtcyKfZaoi1M4GF2_65MyhX9p-XAqJ82yG05PVVRPTcEAsAFug0zHsyVPKKxZAEZc5R9uC-EFhML4KcWq2sWJrexvWrWnXHer7ETC2CPg3yxvEHksyswBeEjH_0aH27K4=)
18. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJhp0M3KyogbXaBhT4P7oqxPjjj822U5Hd5NNXYhql1UGqlkPlL0cElhnfDT8CtPrpSuCVk2N4VLV7gsLzJyBVC2iC-LNJ8QfGqWOZ06Z1kcT7SE6BQw==)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYQCOrF4Gh3eq7m3WEWAJcwxVtMRVtVdj0-eDNVEa9macB5AlWkoONdR7rcUptHxbEcrnQkjD9fwXHAtB9Q5sI2EqZzoN2W5kXKH0etIJ-2kEBR8M_fajQdmXhVP0CTp6E_GXvKzHtH6G6A7PCn7KIRxc-TXK7Wae6O341Dyhe6oTCZa5jyjBP0JfxQ-dYiK4I9tf2kA==)
20. [stackexchange.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUUhkLmmP7QVSZO83iuShsaeXTjAR4VnlKwulKvNBNMLblEurfd-q5EXaHxtTPe7I5MRZy5JRuUXR5gqyPH3SFL83aaS6FzJw_8MSFNIurnqyiRKUqFKm0fVQ6jlUDuoQddXrV6XVIXzkYWsz__9muonLArL09lGQ1K7Vxih316cQJQCkpxsn6BFYYcQ==)
21. [quora.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4FqxWfSXEJMqd14xfuqHjqVaV4t31IlirUBgwFKB7EDSoXA9lNR_IsD4k5_LVnitfWbVXRWu0ZuM5NdnGKZaNJeiwsapy69TkECDTRN_hcktm4Fgl-l9-0KMRL-dJ5c2sNWWL2E4=)
22. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8oiE1Mz_Gu5cobejpsoLudW5MXpQmkVF97e8nxui_NObTkzYYBwaWnODMAIJZ7mjcMYwLLHbzJle6FOktapdVDRtIzNlBdm4PP09lBmGLx3wb-Zdied72OfyGVfjKrZhpEfuC15n053q9eI3-snBn70zpFAKVRZo40shiOg==)
23. [cam.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHn5p-nVjqskBbootM1ZO-Iq5IJMYpQNroyZU4c96XKZkZeZS4XYhbxroAiB4ViUlMtLGiyaFtB1XPRtBdBMiGl8pjVVW1IJaNYjjMtc2lJBd9ajm8GZMadBlvVWq3xnOfg60skLFkG8EgGLkjYzNhKoE9pxaez1R-7Y64XKWc5OBle6rhg)
24. [amazonaws.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNbT7TzdjmQwBtE867rCxRtpqL-hMUsIXUfaNKLh1bOUjHa22dq4D-r_KLDCEvL7fCiFJzrErA0-s5z4QE3NrR9tFzREvyeYMMAFRFWKjesfRDwQyCMNntmihOZkQeUhq9ZPA2NIFNsncD1PHYbOWpbxxK-r8N0xuYrqEmcHoSl_b9pnXCH3xDezbtyJeUWFNy9ZWAxuto6V8bzCK1P1Ls8x4BDDIjkAukOGyIkkxRy0X-_GEG03auyKoZNl6mZlRyxYBD3Q==)
25. [financialresearch.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXyGLdGn6vxIr-hscWklcd0qOZhBU4sVmvI_KlHPHm0lACztbsthj55JTFMY7CJ3gXtzRuxVJAP1pJlce96Rp8wGLmoIohcx66PzAkCAMHdiyF6SU1N81LQ8vE8QSzVND9zWRcpWsThNNR3cOVk4RM5WkVZXapVT-eR-XZKow=)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaBBxj1p-BYw-sQQ83G2fdR2wgM6cM6qoSvIiJRYL6-pjmahF-K2dpr_ekkmWT27j8C9reBkPFY2lKHOC3u_GmnNzNBW9ILfqjywHd9xhM2HQi6Op26tD8ThjD01U5ipyBopjAZIvE0U9yoRSjEYGgxfX1nck62ev35a2me2TqlS-m1jSj3eQE28eFzns2aORDZvfvwgAyS9eqvND61OdWVDBEzc5czSvIeIEpfcR68mcM)
27. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFFTUhq3cCysfFOK9_DbFQsQqqTRxUwFmDzXgWkvi5u4ozP3c8w_qc5zFsgq-UTm0JpPtomCCtcE6BX9DU3z8XpVg7QKUw4iF8HkxK6UbRQYk_ABhulFY7GjxeW247lOSMrP4iQwM6IanWwVkHEktLz0u60Q==)
28. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHH8sfa-FBdnnCU7bymuN64WF78v678tGrhE-gWYD51Tv6w2HK2IZN6hwjpcKYEA77cesl1k_HeE4rXEnky-dmn5asupXQVdltt6OBioee51y2N3hGOy59q8Vg_9qdKZmQ-E-BLq6pkOCVLfSKsRfMGJfw-E3LREMQW_QB5zd_2DqHeVpL2u8-xvGm27LkXacgkbB9tg7GgqnphShvKRmUJ)
29. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFaie2TiOP-cERgboLrBcX_K9ITNjCvkfOAn7fHlzmybS70VJHbZNW7RNyZETIO9grdTLxVc5hk0r_mFbE6leJDrUkhKyqfkTnDLV4lmsBmJrglGHfWw==)
30. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHp89asgPB3W-anNRDr-AM-idHoz9HjT32_rEIHZeB2JNuZHGPfqngwRuvqPfU0IiElxytddnltEYZZvYr4TgEhLqwSPDDkLc8JAz30GkldzDbVbXHZeA==)
31. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTGo1_CHbRDFDfrbMX-bfa_4FQmQ1J-F2Ml_BylCIre9QfLQXF8Onx12hcJS0jeikIJARqHI8FUi-73Iz122PHvu83lnIN_9CserH2ET5PZL0nV_aPU89GbWflbvbienhHYmR1A9ijJpJXaeX1M6KbWrfvtUyXNJI4-_z8nFqw4OpmCPsOrH3PHbP-IyyCNC3-2YsVgPx8_D0K1nkmbqSEjYiLrmxMQAhyXCJ3m5U4nUlho2opVXTxL4n_lgK2SkRRj-5VfXi7NZaDS1_JjoSCq96MUURgrjPMu7Xv1WkpNdo47uywE3J5-kORHJGeSMjycEZSScCi3O7MmY2nVdy94sY1tzqB09ycvPRmHG93kiBcwS7240l8zoclQoVSe2Mit6s4z1FD8thjEXFBQ5ebR_1w)
32. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJD2pqsr4AmlV-VLuHmgQjgRSWYx6-1MuJwS6hLtbbkLN3iip_Ot1xAB-ivI0_57s3sc4wAthupcWt5UBq4yneEb0BNFmMLgEDEuPdX4Ka3fMdCu6iZU1r5BiDhLRAil2g-HybAlYb2g==)
33. [unimi.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqnKaHU7gYGr7qLeHCjbUnb7ZMpkA1oGnwtHmL9x8VOTR-zm676VM7OHaMEiOmhfVeVqamhum2FBpxe2orLBAwOl90Vn0sRZdlr7GAlXG__iiGe7Lbes52EqVWu5C7TQvmU9yYhqx5q-qmLEm2v5oBrg==)


## Annotations
Annotation(end_index=3499, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE31RJgzoqX10T1_0UN5CQnQKGbOWVyfIheFCEVxLnGw4qyOG8cJiQYhWOMnCbXruOQ1oyZubP2jtVtI7EWwRHcy1ld50TqZmUYBSy6Vvx-mZ9iZ-HZuxckSHVJLiS7FQ==', start_index=3487)
Annotation(end_index=3499, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkH0YpLeRUwJ9DZRBjId_6YSkAct5owqxosPvGbFWrbTZt7h6PTiaoqLgnG_O_mDPLKbgcCA7OpdMPNqBNU6F-yEFdePxb0JoSjunkYCWEs_O1-dJ62gSBIUTBn0h7prOPO7pUJ-b0ZbDh-kTufgDLhMePnUo80XOrkGsmAGYK9oTSIQ==', start_index=3487)
Annotation(end_index=5259, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6_cXwtyhyXfj6IboU0p7TVU_2e8fhtZe5pyozvYHYL4DcP4leuHR7MB_6JWqFGokgWuEf_mKVMoZmzmY6-dTouk8lefO07LPJYVhCd0dFKIINS6Wk7qKOU2l1V8V95cK1oiHhY2Q6O7xFvA==', start_index=5247)
Annotation(end_index=5259, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxdbcB3iXCNBk2D_2xDxLCyMxW9M6qebV5RjleyPY4qDlR1fuuTlTDrgrPj9DxuaTqqHns-JrxWVH9BZhughBHNwQ9fUzx3tESPVvvJLO0U7t8RTObpiozaSp0zDmT_MtcnXbwN8Dl77fsZUY_8TAt9DxipRsBKWhQgWuZm_ZYzXsqIf8EkaOYxj7IxIQqperk0-U7axEsNad_LPbK9A==', start_index=5247)
Annotation(end_index=5569, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUqwN5bUX0lVkJCtVJ6-G5d2Oh2qXrredXTCnRs4vwcnJN-uqsCVqhL0vkIJ5s3mj6BrADB5QtIpFjWJQKBoGfnCZxzAkg8Zj3dVlIPRJN-1pMhDMwikCnRit0Zy28CZtUyz9riT-Z', start_index=5560)
Annotation(end_index=5823, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo65hHdIdW1bMRgGDY0TgI5qm0p2eM4byzW_gs1PoyVLi2He1LEqLVVUxZr20tGdncjlYT4Sfkgk9GIOLSfFBY8G5hbokBAS_oZxmsjsxx5GiyGsvIZZK5kwaLPWGZitHW79Gm6rjBl-DCIkDC3SI9PNbezDiutYLgwaDY8XfrKqvGL1hZ7_lTnw7p3Q==', start_index=5814)
Annotation(end_index=6428, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbAhtE5Tq8t5s3T84IH5wkV7kvPJciE3g8mdKSDILFC3C5ggm1gVPr8mEqRifNr6WGsivf7Z3sd32JQUbHxANVS4IDbpsnczFyXOsEs-9A2kXy-7x7G2qJ_c2d81nS2njJxXgqOzM=', start_index=6416)
Annotation(end_index=6428, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHOPJwuFnpVBJJn6uLkqrPVCOrmjV97NOTdpXLEsT8S4jAvPyIyQE7XYqAA0iaB-CSnFpkf3ovu9AuiyDkOt9j_2xbFrTA5xiZAnqQZJLibVp80XB3qu0Ti7CNJwDSdA==', start_index=6416)
Annotation(end_index=6801, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbAhtE5Tq8t5s3T84IH5wkV7kvPJciE3g8mdKSDILFC3C5ggm1gVPr8mEqRifNr6WGsivf7Z3sd32JQUbHxANVS4IDbpsnczFyXOsEs-9A2kXy-7x7G2qJ_c2d81nS2njJxXgqOzM=', start_index=6789)
Annotation(end_index=6801, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFt7U3obkzYBhLNdJBF7TV7YYJF_6jXQ5e2swZxJQwfQI0q-42ojQTd2oLWNUxMAFTFgl0HmvnTG9-BgRbtP8vT4k4v4j4HyIJtcX7mdSt8iWe-JNs5oxdWV77N3jfmSNM00L_mZ23w', start_index=6789)
Annotation(end_index=7121, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHOPJwuFnpVBJJn6uLkqrPVCOrmjV97NOTdpXLEsT8S4jAvPyIyQE7XYqAA0iaB-CSnFpkf3ovu9AuiyDkOt9j_2xbFrTA5xiZAnqQZJLibVp80XB3qu0Ti7CNJwDSdA==', start_index=7112)
Annotation(end_index=7552, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQQ6B3ra1UDyQUNEDFJziL6cYhtvYXUmLuRogZvT--R-yov8Cd3hpKSVXKvZnFj4N6qzqOPXxTlS4nY0Cl5e9kbVzCphK_Teeuuvu5ohKcb3V_3R-IxeEvC0H9iw6iCav2OXlDpaJjmohClWeawlDKWTo1t-tRim3wXSTO_C22evv8yYBQ1CmK7rMXk8rav8eFkRk=', start_index=7539)
Annotation(end_index=7552, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUqwN5bUX0lVkJCtVJ6-G5d2Oh2qXrredXTCnRs4vwcnJN-uqsCVqhL0vkIJ5s3mj6BrADB5QtIpFjWJQKBoGfnCZxzAkg8Zj3dVlIPRJN-1pMhDMwikCnRit0Zy28CZtUyz9riT-Z', start_index=7539)
Annotation(end_index=7834, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbXSLTUAp2TD3n24UtmMaPu47ndOXNQqqKnMm_jn8x8mCVdhBJPCTUJ2YKoEtkMiTWEDmAz9ZMHY8qEX0Q3m2Jxm5sWeikil-ypNiKagYPnPj-UgOZ7AtjNfsdZQYt', start_index=7820)
Annotation(end_index=7834, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQQ6B3ra1UDyQUNEDFJziL6cYhtvYXUmLuRogZvT--R-yov8Cd3hpKSVXKvZnFj4N6qzqOPXxTlS4nY0Cl5e9kbVzCphK_Teeuuvu5ohKcb3V_3R-IxeEvC0H9iw6iCav2OXlDpaJjmohClWeawlDKWTo1t-tRim3wXSTO_C22evv8yYBQ1CmK7rMXk8rav8eFkRk=', start_index=7820)
Annotation(end_index=8053, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIVYm18WLJopBuiYw8FLNs2HWTw2bJ8rYNQ2N3IvPCwC5oNZumvvg_rCEXJQFfWZAGlat2kA38rKYlo3DzlsP22HpNZWi39I4szRDPsEYPAGtpahpm7GBdt9QY38bRVLXUtuGH8b2lV5SZKlK7-tn22_SYvKLWx-F4s9iuhBs2aK9WWje4DU6HADtQ60BkYzB61iDEkozKNPRosJC84tP68-iKm__nmggScIztgDZdfd-bhx9N', start_index=8043)
Annotation(end_index=8995, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGX3_Dybyg18fyxeEspoaQpevDdK1vBbWALmc447CjeRZjwllmZg1xXlYZOKPTp-fUI8QM6kRTbBIO3n939OysXQtoPxXrLHgVUcjWe1ylFmhxYybW5h-ivzjW9YCVrlIUlGYkIaUNzLXqAMKVaPHRWBcAjKNKSk1Y=', start_index=8981)
Annotation(end_index=8995, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWmtexSOcZ3ft6BEKiHv0zaZzeRA6FSGitsoT-Mdc7CQQjXuUV75wfQlDoD2Q7IG3iYWYwWvgJzVRJ_DEPKaBLm7P-PiP5MwxOBamgJ9FTFZ7B5KL5J9gr2P8B2fXfaKfCXFUChf9JmdiZVeNhuvDVi4MZRcAucn3FVYnhT70I10jg_ZFt', start_index=8981)
Annotation(end_index=9313, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwzXCSfx2z_vBWsm_x353swOmg4z7kBXIEN7U3HrQy0uXE-J_LSfS2oKv05W_PS5VcQKy6j7RkykIPln5HtL4-QnJG1UV1Zo8iaWutauZWuLKaZgYPmNjSEJg7xyOfVIU56HcxU0umgXMEL1zDmfgMVR3fdKkh_ZiH8WhyEIxXyMwUzf4ISgmXJP8ghV5sgJcQupVfODe_npKR-mF0khcjsLx_MgEmX26UrHz44d2JN3Iae7CZTLm69gFNorWDcw==', start_index=9299)
Annotation(end_index=9313, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTnQ0OEGyhfam2GI2lZqYibFgo5iERn1qkm3lA4ToyOBovhiZqggr6b1XU6KmnJIHF007cZM8nyYdQ1mm98cDeqM_QyuoxUXMu06Ip4yaYMs2R6S2q8rtjdxTdBhLOer4oAudpEATeiNFqjh3YhdMBWgV5cM5OBKD71i8=', start_index=9299)
Annotation(end_index=10013, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJhp0M3KyogbXaBhT4P7oqxPjjj822U5Hd5NNXYhql1UGqlkPlL0cElhnfDT8CtPrpSuCVk2N4VLV7gsLzJyBVC2iC-LNJ8QfGqWOZ06Z1kcT7SE6BQw==', start_index=9999)
Annotation(end_index=10013, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXSeFjwbQaS_8_GZiI8kW6EPCR8_sHVy-9pp617hxVM3juOFfmwL6ZKzMTQIW2jiByJ8ZWd_GNYw52AF1IQoGvfjnFv0nd6dC2O2FnFYosOMybSHhtcyKfZaoi1M4GF2_65MyhX9p-XAqJ82yG05PVVRPTcEAsAFug0zHsyVPKKxZAEZc5R9uC-EFhML4KcWq2sWJrexvWrWnXHer7ETC2CPg3yxvEHksyswBeEjH_0aH27K4=', start_index=9999)
Annotation(end_index=10467, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJhp0M3KyogbXaBhT4P7oqxPjjj822U5Hd5NNXYhql1UGqlkPlL0cElhnfDT8CtPrpSuCVk2N4VLV7gsLzJyBVC2iC-LNJ8QfGqWOZ06Z1kcT7SE6BQw==', start_index=10453)
Annotation(end_index=10467, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYQCOrF4Gh3eq7m3WEWAJcwxVtMRVtVdj0-eDNVEa9macB5AlWkoONdR7rcUptHxbEcrnQkjD9fwXHAtB9Q5sI2EqZzoN2W5kXKH0etIJ-2kEBR8M_fajQdmXhVP0CTp6E_GXvKzHtH6G6A7PCn7KIRxc-TXK7Wae6O341Dyhe6oTCZa5jyjBP0JfxQ-dYiK4I9tf2kA==', start_index=10453)
Annotation(end_index=10931, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4FqxWfSXEJMqd14xfuqHjqVaV4t31IlirUBgwFKB7EDSoXA9lNR_IsD4k5_LVnitfWbVXRWu0ZuM5NdnGKZaNJeiwsapy69TkECDTRN_hcktm4Fgl-l9-0KMRL-dJ5c2sNWWL2E4=', start_index=10917)
Annotation(end_index=10931, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUUhkLmmP7QVSZO83iuShsaeXTjAR4VnlKwulKvNBNMLblEurfd-q5EXaHxtTPe7I5MRZy5JRuUXR5gqyPH3SFL83aaS6FzJw_8MSFNIurnqyiRKUqFKm0fVQ6jlUDuoQddXrV6XVIXzkYWsz__9muonLArL09lGQ1K7Vxih316cQJQCkpxsn6BFYYcQ==', start_index=10917)
Annotation(end_index=11775, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8oiE1Mz_Gu5cobejpsoLudW5MXpQmkVF97e8nxui_NObTkzYYBwaWnODMAIJZ7mjcMYwLLHbzJle6FOktapdVDRtIzNlBdm4PP09lBmGLx3wb-Zdied72OfyGVfjKrZhpEfuC15n053q9eI3-snBn70zpFAKVRZo40shiOg==', start_index=11761)
Annotation(end_index=11775, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHn5p-nVjqskBbootM1ZO-Iq5IJMYpQNroyZU4c96XKZkZeZS4XYhbxroAiB4ViUlMtLGiyaFtB1XPRtBdBMiGl8pjVVW1IJaNYjjMtc2lJBd9ajm8GZMadBlvVWq3xnOfg60skLFkG8EgGLkjYzNhKoE9pxaez1R-7Y64XKWc5OBle6rhg', start_index=11761)
Annotation(end_index=12461, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNbT7TzdjmQwBtE867rCxRtpqL-hMUsIXUfaNKLh1bOUjHa22dq4D-r_KLDCEvL7fCiFJzrErA0-s5z4QE3NrR9tFzREvyeYMMAFRFWKjesfRDwQyCMNntmihOZkQeUhq9ZPA2NIFNsncD1PHYbOWpbxxK-r8N0xuYrqEmcHoSl_b9pnXCH3xDezbtyJeUWFNy9ZWAxuto6V8bzCK1P1Ls8x4BDDIjkAukOGyIkkxRy0X-_GEG03auyKoZNl6mZlRyxYBD3Q==', start_index=12447)
Annotation(end_index=12461, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQQ6B3ra1UDyQUNEDFJziL6cYhtvYXUmLuRogZvT--R-yov8Cd3hpKSVXKvZnFj4N6qzqOPXxTlS4nY0Cl5e9kbVzCphK_Teeuuvu5ohKcb3V_3R-IxeEvC0H9iw6iCav2OXlDpaJjmohClWeawlDKWTo1t-tRim3wXSTO_C22evv8yYBQ1CmK7rMXk8rav8eFkRk=', start_index=12447)
Annotation(end_index=12726, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbXSLTUAp2TD3n24UtmMaPu47ndOXNQqqKnMm_jn8x8mCVdhBJPCTUJ2YKoEtkMiTWEDmAz9ZMHY8qEX0Q3m2Jxm5sWeikil-ypNiKagYPnPj-UgOZ7AtjNfsdZQYt', start_index=12712)
Annotation(end_index=12726, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXyGLdGn6vxIr-hscWklcd0qOZhBU4sVmvI_KlHPHm0lACztbsthj55JTFMY7CJ3gXtzRuxVJAP1pJlce96Rp8wGLmoIohcx66PzAkCAMHdiyF6SU1N81LQ8vE8QSzVND9zWRcpWsThNNR3cOVk4RM5WkVZXapVT-eR-XZKow=', start_index=12712)
Annotation(end_index=13197, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE31RJgzoqX10T1_0UN5CQnQKGbOWVyfIheFCEVxLnGw4qyOG8cJiQYhWOMnCbXruOQ1oyZubP2jtVtI7EWwRHcy1ld50TqZmUYBSy6Vvx-mZ9iZ-HZuxckSHVJLiS7FQ==', start_index=13184)
Annotation(end_index=13197, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaBBxj1p-BYw-sQQ83G2fdR2wgM6cM6qoSvIiJRYL6-pjmahF-K2dpr_ekkmWT27j8C9reBkPFY2lKHOC3u_GmnNzNBW9ILfqjywHd9xhM2HQi6Op26tD8ThjD01U5ipyBopjAZIvE0U9yoRSjEYGgxfX1nck62ev35a2me2TqlS-m1jSj3eQE28eFzns2aORDZvfvwgAyS9eqvND61OdWVDBEzc5czSvIeIEpfcR68mcM', start_index=13184)
Annotation(end_index=13493, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFFTUhq3cCysfFOK9_DbFQsQqqTRxUwFmDzXgWkvi5u4ozP3c8w_qc5zFsgq-UTm0JpPtomCCtcE6BX9DU3z8XpVg7QKUw4iF8HkxK6UbRQYk_ABhulFY7GjxeW247lOSMrP4iQwM6IanWwVkHEktLz0u60Q==', start_index=13483)
Annotation(end_index=13909, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8oiE1Mz_Gu5cobejpsoLudW5MXpQmkVF97e8nxui_NObTkzYYBwaWnODMAIJZ7mjcMYwLLHbzJle6FOktapdVDRtIzNlBdm4PP09lBmGLx3wb-Zdied72OfyGVfjKrZhpEfuC15n053q9eI3-snBn70zpFAKVRZo40shiOg==', start_index=13895)
Annotation(end_index=13909, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHH8sfa-FBdnnCU7bymuN64WF78v678tGrhE-gWYD51Tv6w2HK2IZN6hwjpcKYEA77cesl1k_HeE4rXEnky-dmn5asupXQVdltt6OBioee51y2N3hGOy59q8Vg_9qdKZmQ-E-BLq6pkOCVLfSKsRfMGJfw-E3LREMQW_QB5zd_2DqHeVpL2u8-xvGm27LkXacgkbB9tg7GgqnphShvKRmUJ', start_index=13895)
Annotation(end_index=14231, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFaie2TiOP-cERgboLrBcX_K9ITNjCvkfOAn7fHlzmybS70VJHbZNW7RNyZETIO9grdTLxVc5hk0r_mFbE6leJDrUkhKyqfkTnDLV4lmsBmJrglGHfWw==', start_index=14221)
Annotation(end_index=14687, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwzXCSfx2z_vBWsm_x353swOmg4z7kBXIEN7U3HrQy0uXE-J_LSfS2oKv05W_PS5VcQKy6j7RkykIPln5HtL4-QnJG1UV1Zo8iaWutauZWuLKaZgYPmNjSEJg7xyOfVIU56HcxU0umgXMEL1zDmfgMVR3fdKkh_ZiH8WhyEIxXyMwUzf4ISgmXJP8ghV5sgJcQupVfODe_npKR-mF0khcjsLx_MgEmX26UrHz44d2JN3Iae7CZTLm69gFNorWDcw==', start_index=14673)
Annotation(end_index=14687, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGX3_Dybyg18fyxeEspoaQpevDdK1vBbWALmc447CjeRZjwllmZg1xXlYZOKPTp-fUI8QM6kRTbBIO3n939OysXQtoPxXrLHgVUcjWe1ylFmhxYybW5h-ivzjW9YCVrlIUlGYkIaUNzLXqAMKVaPHRWBcAjKNKSk1Y=', start_index=14673)
Annotation(end_index=14880, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTGo1_CHbRDFDfrbMX-bfa_4FQmQ1J-F2Ml_BylCIre9QfLQXF8Onx12hcJS0jeikIJARqHI8FUi-73Iz122PHvu83lnIN_9CserH2ET5PZL0nV_aPU89GbWflbvbienhHYmR1A9ijJpJXaeX1M6KbWrfvtUyXNJI4-_z8nFqw4OpmCPsOrH3PHbP-IyyCNC3-2YsVgPx8_D0K1nkmbqSEjYiLrmxMQAhyXCJ3m5U4nUlho2opVXTxL4n_lgK2SkRRj-5VfXi7NZaDS1_JjoSCq96MUURgrjPMu7Xv1WkpNdo47uywE3J5-kORHJGeSMjycEZSScCi3O7MmY2nVdy94sY1tzqB09ycvPRmHG93kiBcwS7240l8zoclQoVSe2Mit6s4z1FD8thjEXFBQ5ebR_1w', start_index=14866)
Annotation(end_index=14880, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHp89asgPB3W-anNRDr-AM-idHoz9HjT32_rEIHZeB2JNuZHGPfqngwRuvqPfU0IiElxytddnltEYZZvYr4TgEhLqwSPDDkLc8JAz30GkldzDbVbXHZeA==', start_index=14866)
Annotation(end_index=15209, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJD2pqsr4AmlV-VLuHmgQjgRSWYx6-1MuJwS6hLtbbkLN3iip_Ot1xAB-ivI0_57s3sc4wAthupcWt5UBq4yneEb0BNFmMLgEDEuPdX4Ka3fMdCu6iZU1r5BiDhLRAil2g-HybAlYb2g==', start_index=15195)
Annotation(end_index=15209, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHp89asgPB3W-anNRDr-AM-idHoz9HjT32_rEIHZeB2JNuZHGPfqngwRuvqPfU0IiElxytddnltEYZZvYr4TgEhLqwSPDDkLc8JAz30GkldzDbVbXHZeA==', start_index=15195)
Annotation(end_index=15471, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWmtexSOcZ3ft6BEKiHv0zaZzeRA6FSGitsoT-Mdc7CQQjXuUV75wfQlDoD2Q7IG3iYWYwWvgJzVRJ_DEPKaBLm7P-PiP5MwxOBamgJ9FTFZ7B5KL5J9gr2P8B2fXfaKfCXFUChf9JmdiZVeNhuvDVi4MZRcAucn3FVYnhT70I10jg_ZFt', start_index=15461)
Annotation(end_index=17138, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbAhtE5Tq8t5s3T84IH5wkV7kvPJciE3g8mdKSDILFC3C5ggm1gVPr8mEqRifNr6WGsivf7Z3sd32JQUbHxANVS4IDbpsnczFyXOsEs-9A2kXy-7x7G2qJ_c2d81nS2njJxXgqOzM=', start_index=17126)
Annotation(end_index=17138, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHOPJwuFnpVBJJn6uLkqrPVCOrmjV97NOTdpXLEsT8S4jAvPyIyQE7XYqAA0iaB-CSnFpkf3ovu9AuiyDkOt9j_2xbFrTA5xiZAnqQZJLibVp80XB3qu0Ti7CNJwDSdA==', start_index=17126)
Annotation(end_index=18536, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE31RJgzoqX10T1_0UN5CQnQKGbOWVyfIheFCEVxLnGw4qyOG8cJiQYhWOMnCbXruOQ1oyZubP2jtVtI7EWwRHcy1ld50TqZmUYBSy6Vvx-mZ9iZ-HZuxckSHVJLiS7FQ==', start_index=18523)
Annotation(end_index=18536, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFFTUhq3cCysfFOK9_DbFQsQqqTRxUwFmDzXgWkvi5u4ozP3c8w_qc5zFsgq-UTm0JpPtomCCtcE6BX9DU3z8XpVg7QKUw4iF8HkxK6UbRQYk_ABhulFY7GjxeW247lOSMrP4iQwM6IanWwVkHEktLz0u60Q==', start_index=18523)
Annotation(end_index=18867, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqnKaHU7gYGr7qLeHCjbUnb7ZMpkA1oGnwtHmL9x8VOTR-zm676VM7OHaMEiOmhfVeVqamhum2FBpxe2orLBAwOl90Vn0sRZdlr7GAlXG__iiGe7Lbes52EqVWu5C7TQvmU9yYhqx5q-qmLEm2v5oBrg==', start_index=18857)
Annotation(end_index=19404, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGX3_Dybyg18fyxeEspoaQpevDdK1vBbWALmc447CjeRZjwllmZg1xXlYZOKPTp-fUI8QM6kRTbBIO3n939OysXQtoPxXrLHgVUcjWe1ylFmhxYybW5h-ivzjW9YCVrlIUlGYkIaUNzLXqAMKVaPHRWBcAjKNKSk1Y=', start_index=19394)
Annotation(end_index=19898, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWmtexSOcZ3ft6BEKiHv0zaZzeRA6FSGitsoT-Mdc7CQQjXuUV75wfQlDoD2Q7IG3iYWYwWvgJzVRJ_DEPKaBLm7P-PiP5MwxOBamgJ9FTFZ7B5KL5J9gr2P8B2fXfaKfCXFUChf9JmdiZVeNhuvDVi4MZRcAucn3FVYnhT70I10jg_ZFt', start_index=19888)
Annotation(end_index=20164, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6_cXwtyhyXfj6IboU0p7TVU_2e8fhtZe5pyozvYHYL4DcP4leuHR7MB_6JWqFGokgWuEf_mKVMoZmzmY6-dTouk8lefO07LPJYVhCd0dFKIINS6Wk7qKOU2l1V8V95cK1oiHhY2Q6O7xFvA==', start_index=20155)
Annotation(end_index=20325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbAhtE5Tq8t5s3T84IH5wkV7kvPJciE3g8mdKSDILFC3C5ggm1gVPr8mEqRifNr6WGsivf7Z3sd32JQUbHxANVS4IDbpsnczFyXOsEs-9A2kXy-7x7G2qJ_c2d81nS2njJxXgqOzM=', start_index=20316)

## Sources
