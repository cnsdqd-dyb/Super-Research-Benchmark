# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 1b13b8b4 | **Time:** 352.34s | **Cost:** $1.55821
--------------------------------------------------------------------------------

# Network Flow Algorithms vs. Centrality Indicators in Liquidity Modeling: Accuracy, Complexity, and Market Illusions

### Key Points
*   **Network flow algorithms** (e.g., Ford-Fulkerson, Edmonds-Karp, and Tardos’s algorithm) provide a rigorous mechanism for modeling liquidity by accounting for capacity constraints and conservation laws, offering higher accuracy than topological metrics but often at the cost of computational intensity.
*   **Tardos’s algorithm** represents a critical breakthrough for financial modeling, offering a strongly polynomial-time solution for minimum-cost circulation problems, thereby balancing accuracy and complexity by ensuring runtime depends on the network size rather than the magnitude of financial values.
*   **Centrality indicators** (Betweenness, Eigenvector, Closeness) are computationally efficient heuristics but frequently exaggerate liquidity availability—creating a "liquidity illusion"—because they often assume geodesic (shortest-path) flows and ignore the capacity constraints inherent in segmented markets.
*   **Market segmentation** and core-periphery structures fundamentally alter liquidity dynamics; standard centrality measures may misidentify systemic risk by highlighting "hub" dealers who withdraw liquidity during stress, whereas "financial centrality" models suggest the true value lies in connecting to peripheral or "weak" agents to smooth consumption shocks.
*   **Generalized flow problems**, which account for friction (fees, exchange rates, losses), offer the most realistic modeling of economic processes but face NP-hard complexity barriers, necessitating approximation schemes for practical application in large-scale financial networks.

---

## 1. Introduction

The modeling of liquidity in financial networks sits at the intersection of graph theory, combinatorial optimization, and economic theory. As financial systems become increasingly interconnected and fragmented, the ability to accurately measure the capacity of a network to absorb shocks and facilitate asset transfer is paramount. The central tension in this field lies between the computational tractability of the models and their fidelity to the complex, often non-linear dynamics of real-world markets.

This report investigates two primary methodological approaches to this problem: **Network Flow Algorithms** and **Centrality Indicators**. Network flow algorithms, rooted in operations research, model the movement of assets subject to capacity constraints, offering a granular view of systemic throughput. Conversely, centrality indicators, derived from social network analysis, attempt to identify key nodes and structural vulnerabilities based on topological positioning.

The inquiry is driven by two critical questions: Can network flow algorithms achieve a balance between measurement accuracy and computational complexity? And do the weights assigned by centrality indicators contribute to "liquidity illusions"—the false perception of stability—particularly when markets undergo segmentation?

The evidence suggests that while network flow algorithms, particularly those leveraging strongly polynomial time solutions like **Tardos’s algorithm**, offer a superior theoretical framework for liquidity, they face significant implementation hurdles in generalized contexts. Meanwhile, centrality measures, while accessible, often rely on implicit assumptions about flow (e.g., shortest-path transmission) that fail during market stress, thereby masking the risks of liquidity evaporation in segmented markets.

---

## 2. Network Flow Algorithms in Liquidity Modeling

Network flow problems are a class of computational problems where the input is a flow network—a graph with numerical capacities on its edges—and the goal is to construct a flow that respects capacity constraints and conservation laws [cite: 1]. In the context of financial markets, these "flows" represent the transfer of capital, the clearing of obligations, or the routing of payments.

### 2.1 The Maximum Flow and Minimum-Cost Flow Problems

The fundamental construct in liquidity modeling is the **Maximum Flow Problem**, which seeks to determine the greatest possible flow from a source node (e.g., a liquidity provider or central bank) to a sink node (e.g., a distressed institution) [cite: 1, 2].

#### 2.1.1 Ford-Fulkerson and the Augmenting Path
The **Ford-Fulkerson algorithm** is a seminal method for solving the max-flow problem. It operates iteratively by identifying "augmenting paths"—paths from source to sink in the residual graph that can accommodate additional flow [cite: 3, 4].
*   **Mechanism:** The algorithm pushes the maximum possible flow along an augmenting path and updates the residual capacities. This repeats until no augmenting paths remain.
*   **Optimality:** The Max-Flow Min-Cut theorem establishes that the maximum flow is exactly equal to the capacity of the minimum cut (the bottleneck) of the network [cite: 1, 2].
*   **Limitations in Finance:** While conceptually robust, the Ford-Fulkerson algorithm is not strongly polynomial. Its runtime depends on the value of the maximum flow ($f^*$), leading to a complexity of $O(E \cdot f^*)$ [cite: 4, 5]. In financial contexts, where flow values (monetary amounts) can be astronomically large, this dependency renders the basic algorithm inefficient and potentially non-terminating if capacities are irrational numbers [cite: 6].

#### 2.1.2 Polynomial Time Improvements
To address the complexity issues of Ford-Fulkerson, the **Edmonds-Karp algorithm** implements the search for augmenting paths using Breadth-First Search (BFS), guaranteeing a polynomial time complexity of $O(VE^2)$ independent of the flow magnitude [cite: 4, 7]. This is crucial for liquidity modeling, as it ensures that the time to compute clearing vectors or stress-test results depends on the number of institutions (nodes) and contracts (edges), not the dollar value of the transactions.

### 2.2 Tardos’s Algorithm: Balancing Accuracy and Complexity

A pivotal development in balancing accuracy with complexity is **Tardos’s algorithm** for the minimum-cost circulation problem. In financial networks, flows often incur costs (e.g., transaction fees, interest rates, or opportunity costs). The minimum-cost flow problem seeks to satisfy demand at the lowest total cost [cite: 1, 3].

*   **Strongly Polynomial Time:** Éva Tardos developed the first strongly polynomial algorithm for minimum-cost flows. "Strongly polynomial" means the number of arithmetic operations depends only on the number of variables (nodes/edges) and is independent of the magnitude of the costs or capacities [cite: 8, 9].
*   **Significance for Liquidity:** This is a transformative property for economic modeling. It implies that liquidity models can handle networks with disparate scales of value (e.g., mixing retail payments with interbank settlements) without suffering exponential blowups in computation time [cite: 10, 11]. Tardos’s approach allows for high-accuracy modeling of cost-sensitive liquidity distribution without the prohibitive complexity usually associated with large-number arithmetic in linear programming [cite: 12, 13].

### 2.3 Generalized Flow Problems: Modeling Friction

While standard flow algorithms assume flow conservation (flow in = flow out), financial markets often involve friction: transaction fees, exchange rate slippage, or interest rate haircuts. These are modeled using **Generalized Flow Problems** (or flows with gains/losses), where the amount of flow entering an edge is multiplied by a gain factor $\gamma(e)$ before exiting [cite: 3, 14].

*   **Economic Realism:** This model perfectly captures phenomena like currency exchange (where 1 USD becomes 0.85 EUR) or "leakage" in supply chains [cite: 14].
*   **Complexity Barrier:** Unlike standard flows, generalized flow problems are significantly harder. While polynomial-time algorithms exist (e.g., interior point methods or generalized scaling algorithms by Goldberg, Plotkin, and Tardos), they are often not strongly polynomial [cite: 3].
*   **NP-Hardness:** In specific configurations, such as finding integer flows in generalized networks or optimizing under certain budget constraints, the problem becomes NP-hard [cite: 15, 16]. This forces modelers to rely on approximation schemes, introducing a trade-off: one can model the *physics* of liquidity friction accurately (generalized flow) but must accept approximate solutions, or model the *topology* accurately (standard flow) and ignore friction to retain exact solvability.

---

## 3. Centrality Indicators and the Liquidity Illusion

Centrality indicators are widely used to assess the systemic importance of financial institutions. However, their application to liquidity modeling is fraught with theoretical risks. Centrality measures typically assume specific modes of interaction—often based on shortest paths—that may not hold during liquidity crises.

### 3.1 The Taxonomy of Centrality

*   **Degree Centrality:** Measures the number of direct connections. In financial networks, this identifies "hubs" or market makers [cite: 17, 18].
*   **Betweenness Centrality:** Quantifies the frequency with which a node appears on the shortest path between two other nodes. This is often interpreted as a measure of a node's control over information or liquidity flow [cite: 17, 18].
*   **Eigenvector Centrality:** Assigns importance based on the importance of a node's neighbors. This is used to identify influential players in contagion models [cite: 17, 18].

### 3.2 The Shortest-Path Fallacy

A critical limitation of standard centrality measures (particularly Betweenness and Closeness) is their reliance on **geodesic paths** (shortest paths).
*   **Implicit Assumption:** These metrics assume that traffic (liquidity) flows optimally along the shortest route [cite: 19].
*   **Reality of Crisis:** In a liquidity crunch, the "shortest" path (e.g., a direct interbank loan) is often blocked due to counterparty risk or credit freezing. Liquidity must then traverse longer, suboptimal paths, or diffuse randomly through the network.
*   **Measurement Error:** Borgatti (2005) argues that applying centrality formulas designed for geodesic flow to processes that are diffusive or parallel results in the "wrong answer" [cite: 19, 20]. Consequently, Betweenness Centrality may identify a bank as a critical bridge when, in reality, liquidity could bypass it via alternative (albeit longer) routes, or conversely, fail to identify a bottleneck because the metric ignores capacity constraints on the edges [cite: 21].

### 3.3 Financial Centrality vs. Network Centrality

Recent research challenges the direct application of graph-theoretic centrality to finance. A distinct concept of **"Financial Centrality"** has emerged, defined as the ex-ante marginal social value of providing liquidity to an agent [cite: 22].

*   **Contrarian Findings:** Unlike Eigenvector centrality, which suggests a node is important if connected to other important nodes, Financial Centrality suggests that an agent is most valuable if they bridge to "weak" agents or those with correlated shocks [cite: 22].
*   **The "Weak" Link:** In risk-sharing networks, the most "central" player for liquidity provision is the one who can absorb shocks from the periphery. Standard centrality weights, which reward clustering with the core, may therefore exaggerate the stability of the network by focusing on the strong-to-strong links (the "rich club") while ignoring the fragility of the periphery [cite: 22].

---

## 4. Market Segmentation and Liquidity Illusions

**Liquidity illusion** refers to the phenomenon where market participants systematically underestimate the cost of liquidation or overestimate the availability of buyers, particularly during stress events [cite: 23, 24]. This illusion is exacerbated by market segmentation and the structural limitations of centrality metrics.

### 4.1 The Mechanics of Illusion

*   **The "Liquidity Tax":** In normal times, large trades have minimal price impact. During stress, liquidity vanishes, and the "liquidity tax" (price impact) explodes. For example, during the 2008 crisis, the price impact of trading Treasuries spiked 5x [cite: 25].
*   **Dependence on Conventions:** Liquidity often relies on social conventions and market-maker confidence. When these conventions break down (e.g., trust evaporates), the "illusion" of a connected market shatters, revealing a set of disconnected segments [cite: 26, 27].

### 4.2 Segmentation and Core-Periphery Structures

Financial markets often exhibit a **core-periphery structure**, where a small number of dealers (the core) intermediate trades for the periphery [cite: 28, 29].
*   **Centrality Misinterpretation:** In this structure, core dealers have massive Degree and Betweenness Centrality. A naive analysis would suggest these nodes are robust sources of liquidity.
*   **Strategic Withdrawal:** However, research indicates that during volatility, these central dealers often withdraw from the market to protect their balance sheets, causing liquidity to evaporate precisely where centrality metrics predicted it would be highest [cite: 29, 30].
*   **Segmentation Effects:** As the core retreats, the market segments. "Global" liquidity becomes "local" liquidity. Centrality measures calculated on the pre-crisis (connected) graph become obsolete and misleading, as they weight paths that no longer exist [cite: 17, 31].

### 4.3 Exaggerating the Illusion

Centrality indicator weights exaggerate liquidity illusions by:
1.  **Ignoring Capacity:** They treat edges as binary or simple weighted links, ignoring the fact that a "connection" may have zero remaining capacity during a run [cite: 21].
2.  **Assuming Stationarity:** They are often static measures applied to dynamic systems. A high centrality score implies a permanent structural role, masking the transient nature of market-making commitment [cite: 17, 30].
3.  **Overvaluing the Core:** By emphasizing the interconnectedness of the core (Eigenvector centrality), they reinforce the belief that the core is a stronghold, whereas systemic risk models (like Eisenberg-Noe) show that interconnectedness can amplify contagion rather than dampen it [cite: 16].

---

## 5. Comparative Analysis: Algorithms vs. Indicators

The choice between network flow algorithms and centrality indicators represents a trade-off between **structural fidelity** and **computational cost**.

| Feature | Network Flow Algorithms | Centrality Indicators |
| :--- | :--- | :--- |
| **Primary Output** | Feasible flow volume, bottlenecks (Min-Cut) | Node ranking, structural importance |
| **Constraint Handling** | Explicit (Capacity, Conservation, Cost) | Implicit or Ignored |
| **Computational Complexity** | High (Polynomial to NP-Hard) | Low to Moderate (Polynomial) |
| **Accuracy in Stress** | High (Models constraints/losses) | Low (Assumes static topology) |
| **Liquidity Definition** | Throughput (Volume/Time) | Connectivity (Path existence) |
| **Risk of Illusion** | Low (Detects capacity limits) | High (Assumes infinite capacity/shortest path) |

### 5.1 Balancing Accuracy and Complexity

Network flow algorithms *can* balance accuracy and complexity, but only through careful algorithm selection.
*   **Tardos’s Algorithm** is the gold standard for this balance in linear/cost-based models, removing the dependency on financial magnitudes [cite: 8].
*   **Approximation Schemes:** For NP-hard generalized flow problems (e.g., calculating optimal intervention in a network with default costs), Fully Polynomial Time Approximation Schemes (FPTAS) or heuristic approaches based on flow decomposition are necessary to maintain tractability [cite: 16, 32].

### 5.2 The Failure of Centrality in Segmentation

Centrality indicators fail to balance this trade-off in the context of segmentation. While they are computationally cheap, their "accuracy" regarding liquidity is fundamentally compromised because they measure *potential* connectivity rather than *realizable* flow.
*   **Case in Point:** In the EU trade network, centrality measures remained stable between 2007 and 2011, failing to capture the massive structural shifts and liquidity drying up in the Eurozone investment network [cite: 17]. This empirical failure demonstrates that centrality weights can mask the reality of market fragmentation.

---

## 6. Applications and Case Studies

### 6.1 The Lightning Network (Payment Channels)
The Bitcoin Lightning Network provides a contemporary example of these principles in action. It is a network of payment channels where liquidity is strictly defined by channel capacity.
*   **Flow vs. Centrality:** Routing payments is a **Minimum Cost Flow** problem. Early attempts to use shortest-path algorithms (akin to Betweenness Centrality) failed because they ignored the probability of liquidity depletion in intermediate channels [cite: 33].
*   **Optimization:** Advanced implementations now use min-cost flow formulations (often separable and convex) to optimize reliability and fees. This confirms that in systems where capacity is hard-constrained, flow algorithms are indispensable, and centrality heuristics are insufficient [cite: 33, 34].

### 6.2 Interbank Markets and Systemic Risk
In interbank markets, the **Eisenberg-Noe model** is the standard for clearing obligations. This is fundamentally a network flow problem (specifically, a fixed-point problem related to flow conservation).
*   **Complexity:** Computing best responses in these networks to maximize equity can be NP-hard, highlighting the extreme complexity of accurate liquidity modeling [cite: 16].
*   **Intervention:** Central banks acting as "market makers of last resort" essentially solve a max-flow problem: injecting liquidity at specific nodes to prevent the min-cut (systemic failure) from reaching zero [cite: 24, 35].

---

## 7. Conclusion

The modeling of liquidity requires a rigorous distinction between the *topology* of connections and the *physics* of flow. **Network flow algorithms**, particularly those leveraging strongly polynomial advancements like **Tardos’s algorithm**, offer a robust framework that balances measurement accuracy with computational complexity. They explicitly account for the capacity constraints and frictional losses that define real-world liquidity, preventing the mathematical "illusions" that arise from simpler models.

In contrast, **centrality indicators**, while valuable for identifying static structural features, frequently **exaggerate liquidity illusions** during market segmentation. By weighting nodes based on geodesic paths and infinite-capacity assumptions, they project an image of connectivity that often disintegrates under stress. The "central" dealer in a graph often becomes the "bottleneck" in a crisis.

Therefore, for accurate liquidity modeling—especially for stress testing and systemic risk analysis—reliance must shift from topological centrality heuristics to capacity-constrained flow dynamics. While this increases computational demands, the existence of polynomial-time algorithms for many flow classes proves that this cost is manageable and necessary to pierce the veil of liquidity illusion.

### References
*   **[cite: 3]** Goldberg, A. V., Tardos, E., & Tarjan, R. E. (1989). Network Flow Algorithms.
*   **[cite: 2]** MindMapAI. (2025). Flow Networks & Max Flow Algorithms Explained.
*   **[cite: 10]** Megiddo, N. (1989). Flow.
*   **[cite: 4]** GeeksforGeeks. (2025). Ford-Fulkerson Algorithm for Maximum Flow Problem.
*   **[cite: 22]** Elliott, M., Golub, B., & Jackson, M. O. (2014). Financial Centrality and the Value of Key Players.
*   **[cite: 28]** Li, D., & Schürhoff, N. (2019). Dealer Networks.
*   **[cite: 17]** Qureshi, A. (2016). Centrality Measures for Trade and Investment Networks.
*   **[cite: 19]** Borgatti, S. P. (2005). Centrality and network flow.
*   **[cite: 25]** Illumination. (2025). The Liquidity Illusion.
*   **[cite: 23]** Nesvetailova, A. (2010). The Crisis of Invented Money: Liquidity Illusion and the Global Credit Meltdown.
*   **[cite: 24]** BIS. (2015). Market robustness and liquidity illusion.
*   **[cite: 35]** Gazda, V., et al. (2015). Formal Model for Single Liquidity Source.
*   **[cite: 19]** Borgatti, S. P. (2004). Centrality and network flow.
*   **[cite: 36]** Bellavitis, C., et al. (2022). How Efficient is Decentralized Finance (DeFi)?
*   **[cite: 22]** Elliott, M., et al. (2014). Liquidity, Financial Centrality, and the Value of Key Players.
*   **[cite: 1]** Wikipedia. (2025). Network flow problem.
*   **[cite: 37]** Wikipedia. (2025). Ford-Fulkerson algorithm.
*   **[cite: 14]** Wayne, K. (2002). Generalized Maximum Flow Algorithms.
*   **[cite: 29]** Zhang, S. (2016). A Model of OTC Market Segmentation.
*   **[cite: 33]** Pickhardt, R., & Richter, S. (2021). Optimally Reliable & Cheap Payment Flows on the Lightning Network.
*   **[cite: 15]** Kichikawa, Y., et al. (2019). Liquidity in Financial Networks.
*   **[cite: 16]** Bertschinger, N., et al. (2020). Nash Equilibrium, Financial Network, Systemic Risk.
*   **[cite: 8]** Végh, L. A. (2013). Strongly polynomial algorithm for generalized flow maximization.
*   **[cite: 12]** Dadush, D., et al. (2020). Tardos's algorithm.

**Sources:**
1. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFF48KwNBFJpXFnBx7XJUVN45bA-EA8caV8B9aRVGzJNIy2PytauJaVPf2kHFOkER8DkpjP5ZJlPL-7MFaQtfUZ8k6wF0X0JejiTEBrjNeInubLU0_rBFaXQ3pSj5QPra9YDSpTVvXvqw==)
2. [mindmapai.app](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDuUKms-DLYWxTiyn4sGs5iuNI2MQUDDcyZHui93mR2VCEWFG2zj9TO7CEghYNsLTGnCgSxPkDtOCMvc58L5cJ_gtGQvWKbtwqkl0dANwPbVu8uNGjJTChm-obWeY9fX_Fi_vRyaSm8ap4tRBF_p6d9kAq1e0VIF3lqMijsp8=)
3. [cornell.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1Zf7Ht9xIIryctp_6wgCbUFGsqg0KjKrkKQm0Ngzceeo-GhpwwqTemy4idsZuB-9q9vxo_bCbMGB172RSFSdhRIH2E-td__OZ_TN59osWDmMEFWAf2tYnneV-ohFMX8zXye6HCjtATtaQuSJVDVCouw==)
4. [geeksforgeeks.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIBsO7pKmmRul-tjeeoQBQvdXloSAkExhq7o0dxq4soYXyKFFQSaFmFy3nCeETIsBgTyf0hrf7P05Qtt-zmyrMl6TSuKAsmwZM3w6ua6pWlfeKnRmYNLSoUOhTLYfuWp015HwIH6pcPrdAf-osVdY8mPgJBte0EdUzgNZrzpjO1JPw4IRIGH9fOdw=)
5. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwSkbq6jhsclXmacutAXTpRsSBK6PUajE0EWwgI-fH7P1mO9GvOaDrbsnrvHq3hveXnhiZzz5pT0zmNGHH23m4psk1q9RPE5-6eU-NBvDvRopMEo49x4fKcuVsBy6EC0u4)
6. [nyu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIburDx6UIB63uxMse1uvZAD4mbg4DupA0Ouq1qGRvkqwlKRXHCHJrATbTRZz36QIx56ibtrs7STOc9-InGHE512h_1rEiEaUnipyH6i_Irt-oUDpJ2PNYFWxM4QjTcTeEpwCuhW1VV8uj_maGuQ==)
7. [bankseta.org.za](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAlOPMBGLps__j94GkGqOYJ87Qu5ZW3JB39uiyL2mUJtOvRoS_fpkWiBx_UteugD97zEKKJ3rJSCUTWkSfkYfhBXEZ-DpR6fNmo-qditV2wIoyfPgotgB8ne8CIJugYAtLK_fvaNzjSRmSfL1u2GsMJc9uoi8cOmiU1WRBvWbpZSthNsdfDyGef9VaPGwXGKxieGRWHpXEaZMzvT2DFmUbNUFAzCz5EURThRNoCpHp5GI1fcHKLqpKRk8=)
8. [laszlovegh.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBdNrJaHJFglKTw1qKBVMMggXERIRbQDVIzHqs9KnXrugakl7vlZ9kFhSMbNuG7d5UUx8vcE0lePjqlg5tR5u8PR_4THAjb2lhe9T0y7VQUwiajgkfdnQ6xnOK6lCdFOu9fnONLZtEJZw1-jfVIq2Dc6Nn94YIHQ==)
9. [ubc.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsjvTKHdWSoDd7Z8ScXEIMGNqRfLAUjPiH3CCEr3cwtTQD323SZJ_UCn_XgkX7rG69WKMNkbnGeiRk-ff7pRBa6AjdjJTeuu0SgSUIFg9eXkktkuU56tuBb_ndoyGzG9sXehg-ZZHtlbWYX6l33Sk6mZeTCezylHMxPCJ7tQBECAskQvU=)
10. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYXDpxIrFP7LlwVPxh9oD-fy_PJaqlwmaWQtIOaZ2TnlOk2m4eDRIiVFFyYazByFenJyn7eYydSUJatjQO-O5HgdvAu6Uk3qks9u4HRqj926AUKJjaUbWqXVxV1Rj-j-M_MBBSxrg=)
11. [dtic.mil](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELcZs0wTwVzGUa4C_uVPE_v0GcCzieBfKeqH5sogpBnNu_7hwp8eYHr7o7uz2MxsBcnRb8DJaFl7CWHlO9tQDcgGc0QpfEvWDWQqZMtfqSzP4Ap_oyzs16zNadg8dlXQjEmw==)
12. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH943_7DD18XDVQe7OW0UKLui8tVqx_CAQHS4W_rAnLjqUJBsXGACPMX9yIKBQmYZqY5jcBc1xXg71iVApOD5cnFsCxgcxbB9IHJWJWCV0_JrWHV9ic-g==)
13. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWtL7v7abAGCyD8LECMObIaDbafUPqONzp5ikRMX-3OwF3ZQCzQ7SJrek5g34K5mVy7SGudOJGdjGg4QWYp125SpxU1ly31b4yCMefH5C0ww154q7INAvcMozSfxIUnUGdHIsuE-u5pMBVm12T1xxIRDM3WcQMRqIcOeBGz83SKvCG_Mqy9fUaEiE=)
14. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdMtqCSAsaAriMCJqY9VJsmgp0ovhK9FEveBkqbrK2QIhOo-xiQfqEtsbVsGaPw2tUKgA6Fvt7QL7jNENAHigbS8iAghesP1bun386v2hs5mEXph02MFKoo2C4-BdnuzxcBbL-rvypzHAS1Vpm6PEapp603UAf3hTBiLgetNuC6mI=)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBpqr8xgOct-Zp3IJpG2c2LflFXVW5J78mEQcC4mBeWf0c7DcLc0VwKTuHQePw0J1S2xg6V2eY41rmN8U0qLmLUunxkCu1psqt80XYV8NTHVBQZRNpMuf2ufjNCBKVlo287xmZLTrjHDklYHualTfFgl7tA-7r4sQfo22_nTkANt02vfW4uDt0)
16. [dagstuhl.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyl0IOU6BFEeWY8wUoJC6xIb7Uig3Ox8E0zaYguIhjigLc7fqVQCgkaIae5tMwix21nSUpXIUJbh1e_T1SvnSyO_-sIMOvDN8L-ZaYq8sE_5F7ZS4soHtk_6xykZtwue1mJhlaSeuV63QWNscQxHTHdeCur0v7FvwdFrqCLTTkD0ylsrLpPbievOzT2Lg9kRNSQGHaXy667SUclbk0Rzsm8o5g)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEBWNkIbORFN86k08G2P0XcJljqB4x_ACZgpcmlKMUWD3kCq-cIIccEYH41rGhGn8ZFg4JpP5S3e6oZdD44YGWqQNMaNJblCJrV0uoIYTKzQEdCPlNUXIAPtgtSdwHIIcThkdZYkxmSkC9ndR3Xh538IBw8zOOpPhpujCEapJVRERorWN_sSb9CI02jpOAA_NfmhpmYkwyNKx6yHzqvg==)
18. [cambridge-intelligence.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHU9MZkoK-D6bHXJzrFjUg_T-qxgmEOEfCJ4RAxuhEw1ffn3cFccNNvKQQHVhuKtx_A-47J1U2cRDJxTDeF2M2OUktmGvvj3IdYu11UKAemOzCGWvR46WoB4nkTWb0gJV85katLWF2c-FUlrT76OTmQL3f6bFKDheZeIeQQ7l3_)
19. [analytictech.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOcBIvgSlroyg60IhSsBVgWSNOTBqW0gNs1OdiK2q99WjI1vlpnN1BGSsURiJetubF6mo7rIFt9nrkqUST4MeUpZIxgKQvv3x6VRTQfGwZv9Ox1Ch71mOCOSF1VlAisIgeDhpv6PUP6y20Ur0WHQ==)
20. [uky.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGR93P5M3EnJJdz8hCAQRbC2xFHo4jgiVdoY_eRhFFjh3Honb8RUm8D98kRh6IfgKnLvYS4J9fbu6Cuj3exq1XLPgcWonGkqUruUZ4NIe-v35roqZWjL96-NozAwknIhknLsvmKXRuNsxGHvJQ3z5_PlZWNihFpDbLQ-T4=)
21. [quora.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQmXThGjhvebniD_h18Oar1EXQ_6z-Qtb_Z95j7V922lueWjsfFj3eMOiF1L_U6cqgAJCvBhyLnlb5HQA93G5u0ru4IZIw2tjZ3cbU_gpzDf768_VU3sJXdtFnh9TcW9cJfSy0ZpVCA8TvpD6xuLwJMmJ3UVCPD0sxEXjSfYYVryk=)
22. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDfHCOKW3ie3uvgzdsqbWZepYLFweK4NUqKG61X10NChrVgZwch7Zz-KV7WVriwyJ6IWIdmSohJsAPUPSEKjdRPmCOz-FY8T50y6qo5hkTGhQ0pKcje-dkZ50=)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE18jNjmlfl_rnnyT7d5mQI2K3SPnoHhCd7mNqlQRRZ6eXXAjQLegAYOK6xBi-ZX-Gw4JvyKa7WdBXrF5y5V1r6WdyhiFND3WxzarWu4uMOY58F1MFrtPJj7MRdPznuRvjVp82Hzl67q5chwBCS9w-ygQnjLzCW5hHUWWiSZz9B_PJEhgTDKDWcGoph7UG_tPFrqpFfTg5aFfqkYENFROW6uB4KaxX4HZU7_Kqu9P8TYHUdX9uEVLA=)
24. [bis.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5StiaNqkgV88QcPFwI3gcI-t5utdb5Fq8ErSC20S_bvWTr_HXK0War6zdG9B6cvkxR-v1c1uUcPDQ-O9GqHvrOIGvxkShFZHyDpMpMuhRS1Kpjpwbl59p4DoQoGXhGfa02iE=)
25. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPHP0ZEOF5C7zivUuKgOE1o2GhdQZqCXw_3oInXZF06HmGl6lisOpJUeDzbhIapCt4Ao8kCGdo6gCPL1-q9qI0bg6-FyCqMSK_FYFV6k9iPCW4y6ohCiV8A7059LhDgmUgFE1FjwyQSpzDHVasIeN557U-J6_wI4SFbdHdOeIEryCxot6cyPG6XUKMKjtcCERF2NKTziYZa4KlFRS6m902RO0LukMa3lnxNFSfuXlgm-pTCg==)
26. [columbia.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGplICzu0y4PwZde6qsZyuQvrXeAAcF9JATq_o6AehRTtdClg5fXrQebJZIkbY1lpQExrwrmG_Wm2m2ORVYghhjx2Xt6AkMCPdUGL_oEYjcaAIvJl9Kc9p8gHKnHvD0knKx8iQ9nRhuc0YF617AB2Yve5FghaKCbECsUaOT0WptnRNsb4u8WBr1GuSEhk2mn2M5b-bkdT_Fhrn8Pj1XzHe7WHWTX03Wt4w=)
27. [cambridge.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESLVEhqqgzk8aAmBTJiQOgJdhnqrm36VbzboQ9pWA3krPewM0AgQL8w2_ywy0ecDs8rpcxodKC2eYXOOPLXwm9LN_CY-9PgUOigeiZIAuZk0byvSWMr-yOJnpb_1Q6Orlxvq8diwAHpIv8F6lTQQwqf3i9OQqgHMVNmrUiWOqf8-cLPrKv9gBIhUUo-O-KrY6MTcKpZOj0Nqvy2fGPCN2MkYeDvi9Ro_XaOdh5e65yfrsIDWIZvuV3CqOwMLkqzfSwcpq3okAsl9ZjJcmttEyng95ziKhXDxkznWCS8p2zIt1sI6EbfYOGfVfuOqkC-EHaShJk3YhVDM0mXN4O6MxCuEiIoQ==)
28. [cuhk.edu.hk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUEs1iWAFVFFUs8MrJ5HlNur_eHPd5Fj3HrMDEKKcIijh8T9pqvPZ3GeLfwibVXF-1VsYno9-DjDhjGcDA1ONwknJdNHCDNIHZEPUM_jdMhTq6LD-vLqBz3-Vk2TTM4bloM8V5c1zbIRVUduO3q1ymcL6d39g2nzHdJ3ou0OQ=)
29. [nyu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjuqqSGoT4cPjMk88b2BvJDYVCCFwR7AM5bQiOm6IrDyj9QxHsfhIl11HnBhua2qdm49gK-OecCTL9ve2sopMbdLiPAcMSI5gviKDAJXAJquXLUH_Nk7evvBUQ6mSu9UQyqm32UOgHATe0E_H16zwbHFFf8LEyyBLAVEZOj7dRV7hdOOYIX7IeGQ==)
30. [icmagroup.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEItsFjlXg5n8NOVlLjGOyTqE0QfYfTooGjeAsipE4YA3QEeUe-cQUHZv4-3h4C3RNw29kVCzlXv_m6wnoHM9mhju3Yt4VjJ16Yh_anoJh-OeHTt_RDKmhdTxEC9ALHqBrlqPMAAqXnmz1Wo_K9JHNi9FRH7fgWdvkve6v_w4j--XZpumzL1xnxWC8rqE5RZ-A63eECHGZKWkx5lvvptGU7MkH87QkFa_wFa1hM9OEq7rm6m_iJMspYuxUykVhdc3o2WDXTYA4NDkC7FCdX8CjmAfH9fxfWPH4z0J4ilQ==)
31. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbmOt5Fp-c6qIAMiTdT-L3BZ2jeI3XEQmOEnSQhGjGtECOAxUsYPX4OGo9KXOCCDv6RN7F1q0vobaGmYB2fkGn8-llbbrrUIy9YPHFqD6fTfFHsS6YLlXbzWFJ_vKlbGoBjyzNspIThfqpUxhFv0MdlXOJlQVCw8LTdAuIF1WladXVg5Ev26ZYlrQJgjPh79-hB36gNjnJ6ZdOYEFBOHA5V0jSuCsdvOl8q8dT7uqCmlwMpk8PKsodNoefHjDLxEET37iLVt4P-O3_v1j0tb8MtZqFH1JE2S9HTSYBjiPEMXM=)
32. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxW2RIW6AUPDHyuxzjmrM0DHNlispPZWYsIcF8_YPpIraKgqXYzqp0-PjfC6GlAw5X6b9dzFBtpnpQFe8uEOMawKJh9wv62NLZoLhTgzzFHgOKWELeGWn9jcWyEoRBrhIq)
33. [cointhinktank.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx95VMNLcQ9uROlNiV7BAOtN2nBgSyXGN_2sWOt3RZkoNDoBSahTXVjHtiku4H60sDtq5CIy7htE0LB4gTsxY40HoRdnt-QaElTH_Ue2OM-ycAb-VvdLcTysvhn2eTdOQWTgjICsXaKWOViwRFeEG0Py5dB1JhIHEPZ6N6m21VGPKCbeNGDhXFrZlTvD8Q5rBRLLHEDJC_jvHt6nwKAnGpZ9kCbOdswfNF9TPU-QiSv3fH_3eDl8A=)
34. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7cmQQwQbBA1A8RaxQSvkLNIoSA3OF46-DCiRG6bhGbCUGebOvD1qdd1RSflMslS6L2f9lx6Be2T43WxIpKQlCfEaPrHabpJ63D_IXlEGQJ2j7DRl4P4_0sg==)
35. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGq187CnuSoghUDTKrvjRqTe8onS6c5GcNlWOK_FvUCqNVkmzffNCDEVGN7wNZ4hKllKbZOJFda_4vhZqkpf3tfA6xCQaM7sim4M2CIzMyy2U3-lbnWaFwtuy_mWTk=)
36. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEESKUgRyKJugeTGYKEt9Tk9vyyG1zeZIRAVhQIMJ8oIxT-zMDlDwQHuf-gP2Nk-5Y61X2tTNBKJKzojbnZmzDlUHvT-52j9T2wv3h0GkdcwymiJDtDh4TwjwDZL3eswH16MswqCE1HQdXYMm4iqZWde6HTsMza_gXrQic5w1Gy4BVNpWg1R7KYb7GGwZG-BH6WJSs_)
37. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHG-ZhsYGDhlFmQ7bHWVtyg0xzFPNAw8vRdI-XMwX8K-mgYjoKleapq0nKuAyp61eRRut7vQctVr2y-WHOoSPBpTDB_1vYOqLJaRr61DjexbLZptt8zx4mPHZK7Y1fnStf7TRY8_NxVY0UG-F_ot8cZHXzhTg==)


## Annotations
Annotation(end_index=3881, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFF48KwNBFJpXFnBx7XJUVN45bA-EA8caV8B9aRVGzJNIy2PytauJaVPf2kHFOkER8DkpjP5ZJlPL-7MFaQtfUZ8k6wF0X0JejiTEBrjNeInubLU0_rBFaXQ3pSj5QPra9YDSpTVvXvqw==', start_index=3872)
Annotation(end_index=4341, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFF48KwNBFJpXFnBx7XJUVN45bA-EA8caV8B9aRVGzJNIy2PytauJaVPf2kHFOkER8DkpjP5ZJlPL-7MFaQtfUZ8k6wF0X0JejiTEBrjNeInubLU0_rBFaXQ3pSj5QPra9YDSpTVvXvqw==', start_index=4329)
Annotation(end_index=4341, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDuUKms-DLYWxTiyn4sGs5iuNI2MQUDDcyZHui93mR2VCEWFG2zj9TO7CEghYNsLTGnCgSxPkDtOCMvc58L5cJ_gtGQvWKbtwqkl0dANwPbVu8uNGjJTChm-obWeY9fX_Fi_vRyaSm8ap4tRBF_p6d9kAq1e0VIF3lqMijsp8=', start_index=4329)
Annotation(end_index=4638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIBsO7pKmmRul-tjeeoQBQvdXloSAkExhq7o0dxq4soYXyKFFQSaFmFy3nCeETIsBgTyf0hrf7P05Qtt-zmyrMl6TSuKAsmwZM3w6ua6pWlfeKnRmYNLSoUOhTLYfuWp015HwIH6pcPrdAf-osVdY8mPgJBte0EdUzgNZrzpjO1JPw4IRIGH9fOdw=', start_index=4626)
Annotation(end_index=4638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1Zf7Ht9xIIryctp_6wgCbUFGsqg0KjKrkKQm0Ngzceeo-GhpwwqTemy4idsZuB-9q9vxo_bCbMGB172RSFSdhRIH2E-td__OZ_TN59osWDmMEFWAf2tYnneV-ohFMX8zXye6HCjtATtaQuSJVDVCouw==', start_index=4626)
Annotation(end_index=4994, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFF48KwNBFJpXFnBx7XJUVN45bA-EA8caV8B9aRVGzJNIy2PytauJaVPf2kHFOkER8DkpjP5ZJlPL-7MFaQtfUZ8k6wF0X0JejiTEBrjNeInubLU0_rBFaXQ3pSj5QPra9YDSpTVvXvqw==', start_index=4982)
Annotation(end_index=4994, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDuUKms-DLYWxTiyn4sGs5iuNI2MQUDDcyZHui93mR2VCEWFG2zj9TO7CEghYNsLTGnCgSxPkDtOCMvc58L5cJ_gtGQvWKbtwqkl0dANwPbVu8uNGjJTChm-obWeY9fX_Fi_vRyaSm8ap4tRBF_p6d9kAq1e0VIF3lqMijsp8=', start_index=4982)
Annotation(end_index=5230, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIBsO7pKmmRul-tjeeoQBQvdXloSAkExhq7o0dxq4soYXyKFFQSaFmFy3nCeETIsBgTyf0hrf7P05Qtt-zmyrMl6TSuKAsmwZM3w6ua6pWlfeKnRmYNLSoUOhTLYfuWp015HwIH6pcPrdAf-osVdY8mPgJBte0EdUzgNZrzpjO1JPw4IRIGH9fOdw=', start_index=5218)
Annotation(end_index=5230, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwSkbq6jhsclXmacutAXTpRsSBK6PUajE0EWwgI-fH7P1mO9GvOaDrbsnrvHq3hveXnhiZzz5pT0zmNGHH23m4psk1q9RPE5-6eU-NBvDvRopMEo49x4fKcuVsBy6EC0u4', start_index=5218)
Annotation(end_index=5455, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIburDx6UIB63uxMse1uvZAD4mbg4DupA0Ouq1qGRvkqwlKRXHCHJrATbTRZz36QIx56ibtrs7STOc9-InGHE512h_1rEiEaUnipyH6i_Irt-oUDpJ2PNYFWxM4QjTcTeEpwCuhW1VV8uj_maGuQ==', start_index=5446)
Annotation(end_index=5759, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIBsO7pKmmRul-tjeeoQBQvdXloSAkExhq7o0dxq4soYXyKFFQSaFmFy3nCeETIsBgTyf0hrf7P05Qtt-zmyrMl6TSuKAsmwZM3w6ua6pWlfeKnRmYNLSoUOhTLYfuWp015HwIH6pcPrdAf-osVdY8mPgJBte0EdUzgNZrzpjO1JPw4IRIGH9fOdw=', start_index=5747)
Annotation(end_index=5759, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAlOPMBGLps__j94GkGqOYJ87Qu5ZW3JB39uiyL2mUJtOvRoS_fpkWiBx_UteugD97zEKKJ3rJSCUTWkSfkYfhBXEZ-DpR6fNmo-qditV2wIoyfPgotgB8ne8CIJugYAtLK_fvaNzjSRmSfL1u2GsMJc9uoi8cOmiU1WRBvWbpZSthNsdfDyGef9VaPGwXGKxieGRWHpXEaZMzvT2DFmUbNUFAzCz5EURThRNoCpHp5GI1fcHKLqpKRk8=', start_index=5747)
Annotation(end_index=6389, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFF48KwNBFJpXFnBx7XJUVN45bA-EA8caV8B9aRVGzJNIy2PytauJaVPf2kHFOkER8DkpjP5ZJlPL-7MFaQtfUZ8k6wF0X0JejiTEBrjNeInubLU0_rBFaXQ3pSj5QPra9YDSpTVvXvqw==', start_index=6377)
Annotation(end_index=6389, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1Zf7Ht9xIIryctp_6wgCbUFGsqg0KjKrkKQm0Ngzceeo-GhpwwqTemy4idsZuB-9q9vxo_bCbMGB172RSFSdhRIH2E-td__OZ_TN59osWDmMEFWAf2tYnneV-ohFMX8zXye6HCjtATtaQuSJVDVCouw==', start_index=6377)
Annotation(end_index=6705, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBdNrJaHJFglKTw1qKBVMMggXERIRbQDVIzHqs9KnXrugakl7vlZ9kFhSMbNuG7d5UUx8vcE0lePjqlg5tR5u8PR_4THAjb2lhe9T0y7VQUwiajgkfdnQ6xnOK6lCdFOu9fnONLZtEJZw1-jfVIq2Dc6Nn94YIHQ==', start_index=6693)
Annotation(end_index=6705, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsjvTKHdWSoDd7Z8ScXEIMGNqRfLAUjPiH3CCEr3cwtTQD323SZJ_UCn_XgkX7rG69WKMNkbnGeiRk-ff7pRBa6AjdjJTeuu0SgSUIFg9eXkktkuU56tuBb_ndoyGzG9sXehg-ZZHtlbWYX6l33Sk6mZeTCezylHMxPCJ7tQBECAskQvU=', start_index=6693)
Annotation(end_index=7014, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELcZs0wTwVzGUa4C_uVPE_v0GcCzieBfKeqH5sogpBnNu_7hwp8eYHr7o7uz2MxsBcnRb8DJaFl7CWHlO9tQDcgGc0QpfEvWDWQqZMtfqSzP4Ap_oyzs16zNadg8dlXQjEmw==', start_index=7000)
Annotation(end_index=7014, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYXDpxIrFP7LlwVPxh9oD-fy_PJaqlwmaWQtIOaZ2TnlOk2m4eDRIiVFFyYazByFenJyn7eYydSUJatjQO-O5HgdvAu6Uk3qks9u4HRqj926AUKJjaUbWqXVxV1Rj-j-M_MBBSxrg=', start_index=7000)
Annotation(end_index=7230, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWtL7v7abAGCyD8LECMObIaDbafUPqONzp5ikRMX-3OwF3ZQCzQ7SJrek5g34K5mVy7SGudOJGdjGg4QWYp125SpxU1ly31b4yCMefH5C0ww154q7INAvcMozSfxIUnUGdHIsuE-u5pMBVm12T1xxIRDM3WcQMRqIcOeBGz83SKvCG_Mqy9fUaEiE=', start_index=7216)
Annotation(end_index=7230, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH943_7DD18XDVQe7OW0UKLui8tVqx_CAQHS4W_rAnLjqUJBsXGACPMX9yIKBQmYZqY5jcBc1xXg71iVApOD5cnFsCxgcxbB9IHJWJWCV0_JrWHV9ic-g==', start_index=7216)
Annotation(end_index=7673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1Zf7Ht9xIIryctp_6wgCbUFGsqg0KjKrkKQm0Ngzceeo-GhpwwqTemy4idsZuB-9q9vxo_bCbMGB172RSFSdhRIH2E-td__OZ_TN59osWDmMEFWAf2tYnneV-ohFMX8zXye6HCjtATtaQuSJVDVCouw==', start_index=7660)
Annotation(end_index=7673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdMtqCSAsaAriMCJqY9VJsmgp0ovhK9FEveBkqbrK2QIhOo-xiQfqEtsbVsGaPw2tUKgA6Fvt7QL7jNENAHigbS8iAghesP1bun386v2hs5mEXph02MFKoo2C4-BdnuzxcBbL-rvypzHAS1Vpm6PEapp603UAf3hTBiLgetNuC6mI=', start_index=7660)
Annotation(end_index=7836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdMtqCSAsaAriMCJqY9VJsmgp0ovhK9FEveBkqbrK2QIhOo-xiQfqEtsbVsGaPw2tUKgA6Fvt7QL7jNENAHigbS8iAghesP1bun386v2hs5mEXph02MFKoo2C4-BdnuzxcBbL-rvypzHAS1Vpm6PEapp603UAf3hTBiLgetNuC6mI=', start_index=7826)
Annotation(end_index=8127, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1Zf7Ht9xIIryctp_6wgCbUFGsqg0KjKrkKQm0Ngzceeo-GhpwwqTemy4idsZuB-9q9vxo_bCbMGB172RSFSdhRIH2E-td__OZ_TN59osWDmMEFWAf2tYnneV-ohFMX8zXye6HCjtATtaQuSJVDVCouw==', start_index=8118)
Annotation(end_index=8322, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyl0IOU6BFEeWY8wUoJC6xIb7Uig3Ox8E0zaYguIhjigLc7fqVQCgkaIae5tMwix21nSUpXIUJbh1e_T1SvnSyO_-sIMOvDN8L-ZaYq8sE_5F7ZS4soHtk_6xykZtwue1mJhlaSeuV63QWNscQxHTHdeCur0v7FvwdFrqCLTTkD0ylsrLpPbievOzT2Lg9kRNSQGHaXy667SUclbk0Rzsm8o5g', start_index=8308)
Annotation(end_index=8322, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBpqr8xgOct-Zp3IJpG2c2LflFXVW5J78mEQcC4mBeWf0c7DcLc0VwKTuHQePw0J1S2xg6V2eY41rmN8U0qLmLUunxkCu1psqt80XYV8NTHVBQZRNpMuf2ufjNCBKVlo287xmZLTrjHDklYHualTfFgl7tA-7r4sQfo22_nTkANt02vfW4uDt0', start_index=8308)
Annotation(end_index=9196, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEBWNkIbORFN86k08G2P0XcJljqB4x_ACZgpcmlKMUWD3kCq-cIIccEYH41rGhGn8ZFg4JpP5S3e6oZdD44YGWqQNMaNJblCJrV0uoIYTKzQEdCPlNUXIAPtgtSdwHIIcThkdZYkxmSkC9ndR3Xh538IBw8zOOpPhpujCEapJVRERorWN_sSb9CI02jpOAA_NfmhpmYkwyNKx6yHzqvg==', start_index=9182)
Annotation(end_index=9196, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHU9MZkoK-D6bHXJzrFjUg_T-qxgmEOEfCJ4RAxuhEw1ffn3cFccNNvKQQHVhuKtx_A-47J1U2cRDJxTDeF2M2OUktmGvvj3IdYu11UKAemOzCGWvR46WoB4nkTWb0gJV85katLWF2c-FUlrT76OTmQL3f6bFKDheZeIeQQ7l3_', start_index=9182)
Annotation(end_index=9435, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEBWNkIbORFN86k08G2P0XcJljqB4x_ACZgpcmlKMUWD3kCq-cIIccEYH41rGhGn8ZFg4JpP5S3e6oZdD44YGWqQNMaNJblCJrV0uoIYTKzQEdCPlNUXIAPtgtSdwHIIcThkdZYkxmSkC9ndR3Xh538IBw8zOOpPhpujCEapJVRERorWN_sSb9CI02jpOAA_NfmhpmYkwyNKx6yHzqvg==', start_index=9421)
Annotation(end_index=9435, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHU9MZkoK-D6bHXJzrFjUg_T-qxgmEOEfCJ4RAxuhEw1ffn3cFccNNvKQQHVhuKtx_A-47J1U2cRDJxTDeF2M2OUktmGvvj3IdYu11UKAemOzCGWvR46WoB4nkTWb0gJV85katLWF2c-FUlrT76OTmQL3f6bFKDheZeIeQQ7l3_', start_index=9421)
Annotation(end_index=9614, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEBWNkIbORFN86k08G2P0XcJljqB4x_ACZgpcmlKMUWD3kCq-cIIccEYH41rGhGn8ZFg4JpP5S3e6oZdD44YGWqQNMaNJblCJrV0uoIYTKzQEdCPlNUXIAPtgtSdwHIIcThkdZYkxmSkC9ndR3Xh538IBw8zOOpPhpujCEapJVRERorWN_sSb9CI02jpOAA_NfmhpmYkwyNKx6yHzqvg==', start_index=9600)
Annotation(end_index=9614, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHU9MZkoK-D6bHXJzrFjUg_T-qxgmEOEfCJ4RAxuhEw1ffn3cFccNNvKQQHVhuKtx_A-47J1U2cRDJxTDeF2M2OUktmGvvj3IdYu11UKAemOzCGWvR46WoB4nkTWb0gJV85katLWF2c-FUlrT76OTmQL3f6bFKDheZeIeQQ7l3_', start_index=9600)
Annotation(end_index=9931, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOcBIvgSlroyg60IhSsBVgWSNOTBqW0gNs1OdiK2q99WjI1vlpnN1BGSsURiJetubF6mo7rIFt9nrkqUST4MeUpZIxgKQvv3x6VRTQfGwZv9Ox1Ch71mOCOSF1VlAisIgeDhpv6PUP6y20Ur0WHQ==', start_index=9921)
Annotation(end_index=10392, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOcBIvgSlroyg60IhSsBVgWSNOTBqW0gNs1OdiK2q99WjI1vlpnN1BGSsURiJetubF6mo7rIFt9nrkqUST4MeUpZIxgKQvv3x6VRTQfGwZv9Ox1Ch71mOCOSF1VlAisIgeDhpv6PUP6y20Ur0WHQ==', start_index=10378)
Annotation(end_index=10392, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGR93P5M3EnJJdz8hCAQRbC2xFHo4jgiVdoY_eRhFFjh3Honb8RUm8D98kRh6IfgKnLvYS4J9fbu6Cuj3exq1XLPgcWonGkqUruUZ4NIe-v35roqZWjL96-NozAwknIhknLsvmKXRuNsxGHvJQ3z5_PlZWNihFpDbLQ-T4=', start_index=10378)
Annotation(end_index=10672, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQmXThGjhvebniD_h18Oar1EXQ_6z-Qtb_Z95j7V922lueWjsfFj3eMOiF1L_U6cqgAJCvBhyLnlb5HQA93G5u0ru4IZIw2tjZ3cbU_gpzDf768_VU3sJXdtFnh9TcW9cJfSy0ZpVCA8TvpD6xuLwJMmJ3UVCPD0sxEXjSfYYVryk=', start_index=10662)
Annotation(end_index=10972, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDfHCOKW3ie3uvgzdsqbWZepYLFweK4NUqKG61X10NChrVgZwch7Zz-KV7WVriwyJ6IWIdmSohJsAPUPSEKjdRPmCOz-FY8T50y6qo5hkTGhQ0pKcje-dkZ50=', start_index=10962)
Annotation(end_index=11244, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDfHCOKW3ie3uvgzdsqbWZepYLFweK4NUqKG61X10NChrVgZwch7Zz-KV7WVriwyJ6IWIdmSohJsAPUPSEKjdRPmCOz-FY8T50y6qo5hkTGhQ0pKcje-dkZ50=', start_index=11234)
Annotation(end_index=11638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDfHCOKW3ie3uvgzdsqbWZepYLFweK4NUqKG61X10NChrVgZwch7Zz-KV7WVriwyJ6IWIdmSohJsAPUPSEKjdRPmCOz-FY8T50y6qo5hkTGhQ0pKcje-dkZ50=', start_index=11628)
Annotation(end_index=11916, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE18jNjmlfl_rnnyT7d5mQI2K3SPnoHhCd7mNqlQRRZ6eXXAjQLegAYOK6xBi-ZX-Gw4JvyKa7WdBXrF5y5V1r6WdyhiFND3WxzarWu4uMOY58F1MFrtPJj7MRdPznuRvjVp82Hzl67q5chwBCS9w-ygQnjLzCW5hHUWWiSZz9B_PJEhgTDKDWcGoph7UG_tPFrqpFfTg5aFfqkYENFROW6uB4KaxX4HZU7_Kqu9P8TYHUdX9uEVLA=', start_index=11902)
Annotation(end_index=11916, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5StiaNqkgV88QcPFwI3gcI-t5utdb5Fq8ErSC20S_bvWTr_HXK0War6zdG9B6cvkxR-v1c1uUcPDQ-O9GqHvrOIGvxkShFZHyDpMpMuhRS1Kpjpwbl59p4DoQoGXhGfa02iE=', start_index=11902)
Annotation(end_index=12326, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPHP0ZEOF5C7zivUuKgOE1o2GhdQZqCXw_3oInXZF06HmGl6lisOpJUeDzbhIapCt4Ao8kCGdo6gCPL1-q9qI0bg6-FyCqMSK_FYFV6k9iPCW4y6ohCiV8A7059LhDgmUgFE1FjwyQSpzDHVasIeN557U-J6_wI4SFbdHdOeIEryCxot6cyPG6XUKMKjtcCERF2NKTziYZa4KlFRS6m902RO0LukMa3lnxNFSfuXlgm-pTCg==', start_index=12316)
Annotation(end_index=12599, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESLVEhqqgzk8aAmBTJiQOgJdhnqrm36VbzboQ9pWA3krPewM0AgQL8w2_ywy0ecDs8rpcxodKC2eYXOOPLXwm9LN_CY-9PgUOigeiZIAuZk0byvSWMr-yOJnpb_1Q6Orlxvq8diwAHpIv8F6lTQQwqf3i9OQqgHMVNmrUiWOqf8-cLPrKv9gBIhUUo-O-KrY6MTcKpZOj0Nqvy2fGPCN2MkYeDvi9Ro_XaOdh5e65yfrsIDWIZvuV3CqOwMLkqzfSwcpq3okAsl9ZjJcmttEyng95ziKhXDxkznWCS8p2zIt1sI6EbfYOGfVfuOqkC-EHaShJk3YhVDM0mXN4O6MxCuEiIoQ==', start_index=12585)
Annotation(end_index=12599, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGplICzu0y4PwZde6qsZyuQvrXeAAcF9JATq_o6AehRTtdClg5fXrQebJZIkbY1lpQExrwrmG_Wm2m2ORVYghhjx2Xt6AkMCPdUGL_oEYjcaAIvJl9Kc9p8gHKnHvD0knKx8iQ9nRhuc0YF617AB2Yve5FghaKCbECsUaOT0WptnRNsb4u8WBr1GuSEhk2mn2M5b-bkdT_Fhrn8Pj1XzHe7WHWTX03Wt4w=', start_index=12585)
Annotation(end_index=12813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUEs1iWAFVFFUs8MrJ5HlNur_eHPd5Fj3HrMDEKKcIijh8T9pqvPZ3GeLfwibVXF-1VsYno9-DjDhjGcDA1ONwknJdNHCDNIHZEPUM_jdMhTq6LD-vLqBz3-Vk2TTM4bloM8V5c1zbIRVUduO3q1ymcL6d39g2nzHdJ3ou0OQ=', start_index=12799)
Annotation(end_index=12813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjuqqSGoT4cPjMk88b2BvJDYVCCFwR7AM5bQiOm6IrDyj9QxHsfhIl11HnBhua2qdm49gK-OecCTL9ve2sopMbdLiPAcMSI5gviKDAJXAJquXLUH_Nk7evvBUQ6mSu9UQyqm32UOgHATe0E_H16zwbHFFf8LEyyBLAVEZOj7dRV7hdOOYIX7IeGQ==', start_index=12799)
Annotation(end_index=13287, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEItsFjlXg5n8NOVlLjGOyTqE0QfYfTooGjeAsipE4YA3QEeUe-cQUHZv4-3h4C3RNw29kVCzlXv_m6wnoHM9mhju3Yt4VjJ16Yh_anoJh-OeHTt_RDKmhdTxEC9ALHqBrlqPMAAqXnmz1Wo_K9JHNi9FRH7fgWdvkve6v_w4j--XZpumzL1xnxWC8rqE5RZ-A63eECHGZKWkx5lvvptGU7MkH87QkFa_wFa1hM9OEq7rm6m_iJMspYuxUykVhdc3o2WDXTYA4NDkC7FCdX8CjmAfH9fxfWPH4z0J4ilQ==', start_index=13273)
Annotation(end_index=13287, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjuqqSGoT4cPjMk88b2BvJDYVCCFwR7AM5bQiOm6IrDyj9QxHsfhIl11HnBhua2qdm49gK-OecCTL9ve2sopMbdLiPAcMSI5gviKDAJXAJquXLUH_Nk7evvBUQ6mSu9UQyqm32UOgHATe0E_H16zwbHFFf8LEyyBLAVEZOj7dRV7hdOOYIX7IeGQ==', start_index=13273)
Annotation(end_index=13563, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbmOt5Fp-c6qIAMiTdT-L3BZ2jeI3XEQmOEnSQhGjGtECOAxUsYPX4OGo9KXOCCDv6RN7F1q0vobaGmYB2fkGn8-llbbrrUIy9YPHFqD6fTfFHsS6YLlXbzWFJ_vKlbGoBjyzNspIThfqpUxhFv0MdlXOJlQVCw8LTdAuIF1WladXVg5Ev26ZYlrQJgjPh79-hB36gNjnJ6ZdOYEFBOHA5V0jSuCsdvOl8q8dT7uqCmlwMpk8PKsodNoefHjDLxEET37iLVt4P-O3_v1j0tb8MtZqFH1JE2S9HTSYBjiPEMXM=', start_index=13549)
Annotation(end_index=13563, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEBWNkIbORFN86k08G2P0XcJljqB4x_ACZgpcmlKMUWD3kCq-cIIccEYH41rGhGn8ZFg4JpP5S3e6oZdD44YGWqQNMaNJblCJrV0uoIYTKzQEdCPlNUXIAPtgtSdwHIIcThkdZYkxmSkC9ndR3Xh538IBw8zOOpPhpujCEapJVRERorWN_sSb9CI02jpOAA_NfmhpmYkwyNKx6yHzqvg==', start_index=13549)
Annotation(end_index=13839, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQmXThGjhvebniD_h18Oar1EXQ_6z-Qtb_Z95j7V922lueWjsfFj3eMOiF1L_U6cqgAJCvBhyLnlb5HQA93G5u0ru4IZIw2tjZ3cbU_gpzDf768_VU3sJXdtFnh9TcW9cJfSy0ZpVCA8TvpD6xuLwJMmJ3UVCPD0sxEXjSfYYVryk=', start_index=13829)
Annotation(end_index=14063, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEItsFjlXg5n8NOVlLjGOyTqE0QfYfTooGjeAsipE4YA3QEeUe-cQUHZv4-3h4C3RNw29kVCzlXv_m6wnoHM9mhju3Yt4VjJ16Yh_anoJh-OeHTt_RDKmhdTxEC9ALHqBrlqPMAAqXnmz1Wo_K9JHNi9FRH7fgWdvkve6v_w4j--XZpumzL1xnxWC8rqE5RZ-A63eECHGZKWkx5lvvptGU7MkH87QkFa_wFa1hM9OEq7rm6m_iJMspYuxUykVhdc3o2WDXTYA4NDkC7FCdX8CjmAfH9fxfWPH4z0J4ilQ==', start_index=14049)
Annotation(end_index=14063, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEBWNkIbORFN86k08G2P0XcJljqB4x_ACZgpcmlKMUWD3kCq-cIIccEYH41rGhGn8ZFg4JpP5S3e6oZdD44YGWqQNMaNJblCJrV0uoIYTKzQEdCPlNUXIAPtgtSdwHIIcThkdZYkxmSkC9ndR3Xh538IBw8zOOpPhpujCEapJVRERorWN_sSb9CI02jpOAA_NfmhpmYkwyNKx6yHzqvg==', start_index=14049)
Annotation(end_index=14361, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyl0IOU6BFEeWY8wUoJC6xIb7Uig3Ox8E0zaYguIhjigLc7fqVQCgkaIae5tMwix21nSUpXIUJbh1e_T1SvnSyO_-sIMOvDN8L-ZaYq8sE_5F7ZS4soHtk_6xykZtwue1mJhlaSeuV63QWNscQxHTHdeCur0v7FvwdFrqCLTTkD0ylsrLpPbievOzT2Lg9kRNSQGHaXy667SUclbk0Rzsm8o5g', start_index=14351)
Annotation(end_index=15550, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBdNrJaHJFglKTw1qKBVMMggXERIRbQDVIzHqs9KnXrugakl7vlZ9kFhSMbNuG7d5UUx8vcE0lePjqlg5tR5u8PR_4THAjb2lhe9T0y7VQUwiajgkfdnQ6xnOK6lCdFOu9fnONLZtEJZw1-jfVIq2Dc6Nn94YIHQ==', start_index=15541)
Annotation(end_index=15852, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyl0IOU6BFEeWY8wUoJC6xIb7Uig3Ox8E0zaYguIhjigLc7fqVQCgkaIae5tMwix21nSUpXIUJbh1e_T1SvnSyO_-sIMOvDN8L-ZaYq8sE_5F7ZS4soHtk_6xykZtwue1mJhlaSeuV63QWNscQxHTHdeCur0v7FvwdFrqCLTTkD0ylsrLpPbievOzT2Lg9kRNSQGHaXy667SUclbk0Rzsm8o5g', start_index=15838)
Annotation(end_index=15852, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxW2RIW6AUPDHyuxzjmrM0DHNlispPZWYsIcF8_YPpIraKgqXYzqp0-PjfC6GlAw5X6b9dzFBtpnpQFe8uEOMawKJh9wv62NLZoLhTgzzFHgOKWELeGWn9jcWyEoRBrhIq', start_index=15838)
Annotation(end_index=16397, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEBWNkIbORFN86k08G2P0XcJljqB4x_ACZgpcmlKMUWD3kCq-cIIccEYH41rGhGn8ZFg4JpP5S3e6oZdD44YGWqQNMaNJblCJrV0uoIYTKzQEdCPlNUXIAPtgtSdwHIIcThkdZYkxmSkC9ndR3Xh538IBw8zOOpPhpujCEapJVRERorWN_sSb9CI02jpOAA_NfmhpmYkwyNKx6yHzqvg==', start_index=16387)
Annotation(end_index=17047, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx95VMNLcQ9uROlNiV7BAOtN2nBgSyXGN_2sWOt3RZkoNDoBSahTXVjHtiku4H60sDtq5CIy7htE0LB4gTsxY40HoRdnt-QaElTH_Ue2OM-ycAb-VvdLcTysvhn2eTdOQWTgjICsXaKWOViwRFeEG0Py5dB1JhIHEPZ6N6m21VGPKCbeNGDhXFrZlTvD8Q5rBRLLHEDJC_jvHt6nwKAnGpZ9kCbOdswfNF9TPU-QiSv3fH_3eDl8A=', start_index=17037)
Annotation(end_index=17352, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7cmQQwQbBA1A8RaxQSvkLNIoSA3OF46-DCiRG6bhGbCUGebOvD1qdd1RSflMslS6L2f9lx6Be2T43WxIpKQlCfEaPrHabpJ63D_IXlEGQJ2j7DRl4P4_0sg==', start_index=17338)
Annotation(end_index=17352, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx95VMNLcQ9uROlNiV7BAOtN2nBgSyXGN_2sWOt3RZkoNDoBSahTXVjHtiku4H60sDtq5CIy7htE0LB4gTsxY40HoRdnt-QaElTH_Ue2OM-ycAb-VvdLcTysvhn2eTdOQWTgjICsXaKWOViwRFeEG0Py5dB1JhIHEPZ6N6m21VGPKCbeNGDhXFrZlTvD8Q5rBRLLHEDJC_jvHt6nwKAnGpZ9kCbOdswfNF9TPU-QiSv3fH_3eDl8A=', start_index=17338)
Annotation(end_index=17779, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyl0IOU6BFEeWY8wUoJC6xIb7Uig3Ox8E0zaYguIhjigLc7fqVQCgkaIae5tMwix21nSUpXIUJbh1e_T1SvnSyO_-sIMOvDN8L-ZaYq8sE_5F7ZS4soHtk_6xykZtwue1mJhlaSeuV63QWNscQxHTHdeCur0v7FvwdFrqCLTTkD0ylsrLpPbievOzT2Lg9kRNSQGHaXy667SUclbk0Rzsm8o5g', start_index=17769)
Annotation(end_index=18009, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5StiaNqkgV88QcPFwI3gcI-t5utdb5Fq8ErSC20S_bvWTr_HXK0War6zdG9B6cvkxR-v1c1uUcPDQ-O9GqHvrOIGvxkShFZHyDpMpMuhRS1Kpjpwbl59p4DoQoGXhGfa02iE=', start_index=17995)
Annotation(end_index=18009, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGq187CnuSoghUDTKrvjRqTe8onS6c5GcNlWOK_FvUCqNVkmzffNCDEVGN7wNZ4hKllKbZOJFda_4vhZqkpf3tfA6xCQaM7sim4M2CIzMyy2U3-lbnWaFwtuy_mWTk=', start_index=17995)
Annotation(end_index=19394, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1Zf7Ht9xIIryctp_6wgCbUFGsqg0KjKrkKQm0Ngzceeo-GhpwwqTemy4idsZuB-9q9vxo_bCbMGB172RSFSdhRIH2E-td__OZ_TN59osWDmMEFWAf2tYnneV-ohFMX8zXye6HCjtATtaQuSJVDVCouw==', start_index=19385)
Annotation(end_index=19490, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDuUKms-DLYWxTiyn4sGs5iuNI2MQUDDcyZHui93mR2VCEWFG2zj9TO7CEghYNsLTGnCgSxPkDtOCMvc58L5cJ_gtGQvWKbtwqkl0dANwPbVu8uNGjJTChm-obWeY9fX_Fi_vRyaSm8ap4tRBF_p6d9kAq1e0VIF3lqMijsp8=', start_index=19481)
Annotation(end_index=19575, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYXDpxIrFP7LlwVPxh9oD-fy_PJaqlwmaWQtIOaZ2TnlOk2m4eDRIiVFFyYazByFenJyn7eYydSUJatjQO-O5HgdvAu6Uk3qks9u4HRqj926AUKJjaUbWqXVxV1Rj-j-M_MBBSxrg=', start_index=19565)
Annotation(end_index=19619, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIBsO7pKmmRul-tjeeoQBQvdXloSAkExhq7o0dxq4soYXyKFFQSaFmFy3nCeETIsBgTyf0hrf7P05Qtt-zmyrMl6TSuKAsmwZM3w6ua6pWlfeKnRmYNLSoUOhTLYfuWp015HwIH6pcPrdAf-osVdY8mPgJBte0EdUzgNZrzpjO1JPw4IRIGH9fOdw=', start_index=19610)
Annotation(end_index=19712, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDfHCOKW3ie3uvgzdsqbWZepYLFweK4NUqKG61X10NChrVgZwch7Zz-KV7WVriwyJ6IWIdmSohJsAPUPSEKjdRPmCOz-FY8T50y6qo5hkTGhQ0pKcje-dkZ50=', start_index=19702)
Annotation(end_index=19831, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUEs1iWAFVFFUs8MrJ5HlNur_eHPd5Fj3HrMDEKKcIijh8T9pqvPZ3GeLfwibVXF-1VsYno9-DjDhjGcDA1ONwknJdNHCDNIHZEPUM_jdMhTq6LD-vLqBz3-Vk2TTM4bloM8V5c1zbIRVUduO3q1ymcL6d39g2nzHdJ3ou0OQ=', start_index=19821)
Annotation(end_index=19900, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEBWNkIbORFN86k08G2P0XcJljqB4x_ACZgpcmlKMUWD3kCq-cIIccEYH41rGhGn8ZFg4JpP5S3e6oZdD44YGWqQNMaNJblCJrV0uoIYTKzQEdCPlNUXIAPtgtSdwHIIcThkdZYkxmSkC9ndR3Xh538IBw8zOOpPhpujCEapJVRERorWN_sSb9CI02jpOAA_NfmhpmYkwyNKx6yHzqvg==', start_index=19890)
Annotation(end_index=19994, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOcBIvgSlroyg60IhSsBVgWSNOTBqW0gNs1OdiK2q99WjI1vlpnN1BGSsURiJetubF6mo7rIFt9nrkqUST4MeUpZIxgKQvv3x6VRTQfGwZv9Ox1Ch71mOCOSF1VlAisIgeDhpv6PUP6y20Ur0WHQ==', start_index=19984)
Annotation(end_index=20066, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPHP0ZEOF5C7zivUuKgOE1o2GhdQZqCXw_3oInXZF06HmGl6lisOpJUeDzbhIapCt4Ao8kCGdo6gCPL1-q9qI0bg6-FyCqMSK_FYFV6k9iPCW4y6ohCiV8A7059LhDgmUgFE1FjwyQSpzDHVasIeN557U-J6_wI4SFbdHdOeIEryCxot6cyPG6XUKMKjtcCERF2NKTziYZa4KlFRS6m902RO0LukMa3lnxNFSfuXlgm-pTCg==', start_index=20056)
Annotation(end_index=20131, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE18jNjmlfl_rnnyT7d5mQI2K3SPnoHhCd7mNqlQRRZ6eXXAjQLegAYOK6xBi-ZX-Gw4JvyKa7WdBXrF5y5V1r6WdyhiFND3WxzarWu4uMOY58F1MFrtPJj7MRdPznuRvjVp82Hzl67q5chwBCS9w-ygQnjLzCW5hHUWWiSZz9B_PJEhgTDKDWcGoph7UG_tPFrqpFfTg5aFfqkYENFROW6uB4KaxX4HZU7_Kqu9P8TYHUdX9uEVLA=', start_index=20121)
Annotation(end_index=20256, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5StiaNqkgV88QcPFwI3gcI-t5utdb5Fq8ErSC20S_bvWTr_HXK0War6zdG9B6cvkxR-v1c1uUcPDQ-O9GqHvrOIGvxkShFZHyDpMpMuhRS1Kpjpwbl59p4DoQoGXhGfa02iE=', start_index=20246)
Annotation(end_index=20330, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGq187CnuSoghUDTKrvjRqTe8onS6c5GcNlWOK_FvUCqNVkmzffNCDEVGN7wNZ4hKllKbZOJFda_4vhZqkpf3tfA6xCQaM7sim4M2CIzMyy2U3-lbnWaFwtuy_mWTk=', start_index=20320)
Annotation(end_index=20417, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOcBIvgSlroyg60IhSsBVgWSNOTBqW0gNs1OdiK2q99WjI1vlpnN1BGSsURiJetubF6mo7rIFt9nrkqUST4MeUpZIxgKQvv3x6VRTQfGwZv9Ox1Ch71mOCOSF1VlAisIgeDhpv6PUP6y20Ur0WHQ==', start_index=20407)
Annotation(end_index=20489, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEESKUgRyKJugeTGYKEt9Tk9vyyG1zeZIRAVhQIMJ8oIxT-zMDlDwQHuf-gP2Nk-5Y61X2tTNBKJKzojbnZmzDlUHvT-52j9T2wv3h0GkdcwymiJDtDh4TwjwDZL3eswH16MswqCE1HQdXYMm4iqZWde6HTsMza_gXrQic5w1Gy4BVNpWg1R7KYb7GGwZG-BH6WJSs_', start_index=20479)
Annotation(end_index=20586, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDfHCOKW3ie3uvgzdsqbWZepYLFweK4NUqKG61X10NChrVgZwch7Zz-KV7WVriwyJ6IWIdmSohJsAPUPSEKjdRPmCOz-FY8T50y6qo5hkTGhQ0pKcje-dkZ50=', start_index=20576)
Annotation(end_index=20695, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFF48KwNBFJpXFnBx7XJUVN45bA-EA8caV8B9aRVGzJNIy2PytauJaVPf2kHFOkER8DkpjP5ZJlPL-7MFaQtfUZ8k6wF0X0JejiTEBrjNeInubLU0_rBFaXQ3pSj5QPra9YDSpTVvXvqw==', start_index=20686)
Annotation(end_index=20755, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHG-ZhsYGDhlFmQ7bHWVtyg0xzFPNAw8vRdI-XMwX8K-mgYjoKleapq0nKuAyp61eRRut7vQctVr2y-WHOoSPBpTDB_1vYOqLJaRr61DjexbLZptt8zx4mPHZK7Y1fnStf7TRY8_NxVY0UG-F_ot8cZHXzhTg==', start_index=20745)
Annotation(end_index=20819, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdMtqCSAsaAriMCJqY9VJsmgp0ovhK9FEveBkqbrK2QIhOo-xiQfqEtsbVsGaPw2tUKgA6Fvt7QL7jNENAHigbS8iAghesP1bun386v2hs5mEXph02MFKoo2C4-BdnuzxcBbL-rvypzHAS1Vpm6PEapp603UAf3hTBiLgetNuC6mI=', start_index=20809)
Annotation(end_index=20893, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjuqqSGoT4cPjMk88b2BvJDYVCCFwR7AM5bQiOm6IrDyj9QxHsfhIl11HnBhua2qdm49gK-OecCTL9ve2sopMbdLiPAcMSI5gviKDAJXAJquXLUH_Nk7evvBUQ6mSu9UQyqm32UOgHATe0E_H16zwbHFFf8LEyyBLAVEZOj7dRV7hdOOYIX7IeGQ==', start_index=20883)
Annotation(end_index=20966, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx95VMNLcQ9uROlNiV7BAOtN2nBgSyXGN_2sWOt3RZkoNDoBSahTXVjHtiku4H60sDtq5CIy7htE0LB4gTsxY40HoRdnt-QaElTH_Ue2OM-ycAb-VvdLcTysvhn2eTdOQWTgjICsXaKWOViwRFeEG0Py5dB1JhIHEPZ6N6m21VGPKCbeNGDhXFrZlTvD8Q5rBRLLHEDJC_jvHt6nwKAnGpZ9kCbOdswfNF9TPU-QiSv3fH_3eDl8A=', start_index=20956)
Annotation(end_index=21089, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBpqr8xgOct-Zp3IJpG2c2LflFXVW5J78mEQcC4mBeWf0c7DcLc0VwKTuHQePw0J1S2xg6V2eY41rmN8U0qLmLUunxkCu1psqt80XYV8NTHVBQZRNpMuf2ufjNCBKVlo287xmZLTrjHDklYHualTfFgl7tA-7r4sQfo22_nTkANt02vfW4uDt0', start_index=21079)
Annotation(end_index=21171, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyl0IOU6BFEeWY8wUoJC6xIb7Uig3Ox8E0zaYguIhjigLc7fqVQCgkaIae5tMwix21nSUpXIUJbh1e_T1SvnSyO_-sIMOvDN8L-ZaYq8sE_5F7ZS4soHtk_6xykZtwue1mJhlaSeuV63QWNscQxHTHdeCur0v7FvwdFrqCLTTkD0ylsrLpPbievOzT2Lg9kRNSQGHaXy667SUclbk0Rzsm8o5g', start_index=21161)
Annotation(end_index=21274, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBdNrJaHJFglKTw1qKBVMMggXERIRbQDVIzHqs9KnXrugakl7vlZ9kFhSMbNuG7d5UUx8vcE0lePjqlg5tR5u8PR_4THAjb2lhe9T0y7VQUwiajgkfdnQ6xnOK6lCdFOu9fnONLZtEJZw1-jfVIq2Dc6Nn94YIHQ==', start_index=21265)
Annotation(end_index=21379, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH943_7DD18XDVQe7OW0UKLui8tVqx_CAQHS4W_rAnLjqUJBsXGACPMX9yIKBQmYZqY5jcBc1xXg71iVApOD5cnFsCxgcxbB9IHJWJWCV0_JrWHV9ic-g==', start_index=21369)

## Sources
