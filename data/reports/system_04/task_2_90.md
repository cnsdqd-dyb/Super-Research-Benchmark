# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 08b15a11 | **Time:** 328.61s | **Cost:** $1.51301
--------------------------------------------------------------------------------

# Determinants of Optimal Warehouse Node Distribution Thresholds in Hierarchical Configuration Models

### Key Points
*   **Dual Interpretation:** The determination of optimal thresholds depends on whether the "Hierarchical Configuration Model" is interpreted through the lens of **Supply Chain Management (SCM)** logistics optimization or **Network Science (Graph Theory)**. Both frameworks utilize distinct mathematical thresholds to ensure system stability and efficiency.
*   **Logistics Clustering Threshold ($N/k$):** In supply chain network design, a critical distribution threshold is defined by the ratio $N/k$, where $N$ is the total number of nodes and $k$ is the number of clusters. This threshold enforces equitable node distribution, triggering a reassignment of warehouse nodes if a cluster becomes overpopulated, thereby preventing resource imbalances [cite: 1].
*   **Risk and Diffusion Coefficients:** The optimal node distribution in dynamic e-commerce environments is determined by a specific function involving the **coefficient of supply chain risk-control ability ($k$)** and the **coefficient of diffusion and convergence ($r$)**. These parameters adjust the distribution threshold based on the system's volatility and the required speed of information/material flow [cite: 2, 3].
*   **Percolation Thresholds (Graph Theory):** In the theoretical Hierarchical Configuration Model (HCM), the distribution threshold is synonymous with the **percolation threshold**. This is the critical value (often denoted as $\nu_D > 1$) required for a "giant component" to emerge, ensuring global connectivity across the network. This threshold is determined by the inter-community degree distribution and the internal structure of the communities [cite: 4, 5].
*   **Operational Capacity Thresholds:** At the facility level, the optimal distribution is constrained by utilization thresholds, typically set at **85% of maximum capacity**. Exceeding this threshold degrades efficiency, necessitating the activation of new nodes or the redistribution of inventory to maintain service levels [cite: 6].

---

## 1. Introduction

The determination of the optimal warehouse node distribution threshold in hierarchical configuration models is a complex, multi-dimensional problem that bridges the gap between applied logistics strategy and theoretical network science. A "Hierarchical Configuration Model" (HCM) serves as a structural framework for organizing complex systems into tiered levels—such as central distribution centers (DCs), regional warehouses, and local forward deployment points. The "distribution threshold" within these models acts as a critical decision boundary: it is the quantitative limit that, when crossed, dictates a change in the network's topology, such as the opening of a new facility, the re-routing of flows, or the re-clustering of service areas.

This report provides an exhaustive analysis of the factors determining these thresholds. It addresses the query from two necessary perspectives found in the research literature:
1.  **The Supply Chain Optimization Perspective:** Where thresholds are decision variables used to minimize costs, maximize service levels, and balance workloads across a physical network of warehouses.
2.  **The Network Science Perspective:** Where HCM refers to a specific class of random graph models, and thresholds refer to critical points of connectivity (percolation) that determine whether the network functions as a cohesive whole.

By synthesizing these perspectives, we establish a comprehensive framework for understanding how optimal node distribution is calculated, maintained, and adapted in dynamic environments.

---

## 2. The Logistics Perspective: Optimization Thresholds in Supply Chain Networks

In the context of physical supply chains, hierarchical configuration models are used to design the layout of warehouse networks. The "optimal distribution threshold" here refers to the specific criteria used to allocate nodes (warehouses or customers) to specific clusters or hierarchy levels.

### 2.1 The $N/k$ Clustering Threshold for Balanced Distribution

One of the most definitive determinants of optimal node distribution found in recent algorithmic research is the **$N/k$ threshold**. This metric is employed in hierarchical clustering algorithms to ensure load balancing across the supply chain.

#### 2.1.1 Definition and Mechanism
The threshold is defined mathematically where $N$ represents the total number of nodes (e.g., customers or delivery points) and $k$ represents the pre-determined number of clusters (e.g., service regions or warehouse zones). The threshold value $T$ is calculated as:

\[ T = \frac{N}{k} \]

This threshold facilitates the equitable distribution of nodes across clusters. In algorithmic network design, specifically within the **Node Rating-Based and Grouping Raft cluster Practical Byzantine Fault Tolerance (NG-RPBFT)** algorithms and similar clustering heuristics, this threshold acts as a hard constraint for stability [cite: 1].

The mechanism for determining optimality using this threshold operates as follows:
1.  **Initial Assignment:** Nodes are assigned to the nearest central warehouse node based on distance or cost.
2.  **Threshold Verification:** The algorithm checks if the number of nodes in any specific cluster exceeds the threshold $N/k$.
3.  **Reallocation:** If the node count in a cluster $> N/k$, the system identifies "excess nodes." These are typically the nodes furthest from the cluster center or those with the lowest comprehensive rating.
4.  **Redistribution:** The excess nodes are forcibly reassigned to the cluster with the *second* minimum distance, provided that the new cluster has not yet reached the threshold [cite: 1].

#### 2.1.2 Determinants of the $N/k$ Threshold
The optimality of this specific threshold is determined by the need to avoid **skewed clustering outcomes**. Without this threshold, standard clustering algorithms (like K-means) might assign a disproportionate number of demand points to a single warehouse simply because of geographical density, leading to capacity overloads and service failures [cite: 1].

Research indicates that the default settings for these parameters often stabilize at $N=40$ and $k=4$ for pilot studies, but in large-scale industrial applications, $k$ is derived from the maximum service capacity of the warehouse facilities [cite: 1]. Therefore, the *physical capacity* of the warehouse nodes is the primary determinant of the denominator $k$, which in turn sets the distribution threshold.

### 2.2 The Risk-Control and Diffusion Coefficients

In dynamic e-commerce supply chains, the optimal node distribution is not static. It is governed by a dynamic function that accounts for environmental disturbances and risk. Research into Amazon's and other e-commerce supply chains has identified a specific **Optimized Node Distribution Function** [cite: 2, 3, 7, 8, 9, 10, 11, 12].

#### 2.2.1 The Node Distribution Function
The optimized node distribution is constructed using the following functional relationship:

\[ Y = \text{Function}(\bar{x}, k, r) \]

Where the determinants are:
*   **$\bar{x}$ (Average Trend):** This represents the average trend of measuring the optimization level of the supply chain. It is a baseline metric of performance.
*   **$k$ (Coefficient of Supply Chain Risk-Control Ability):** This is a critical determinant. A higher $k$ value implies a more robust network capable of withstanding disruptions. The threshold for node distribution shifts based on the enterprise's risk appetite. If $k$ is high, the model favors a more distributed, redundant network (more nodes) to mitigate risk.
*   **$r$ (Coefficient of Diffusion and Convergence):** This coefficient measures how quickly products or information diffuse through the network. It determines the "spread" of the warehouse nodes. A high diffusion coefficient suggests a network that must cover a wide geographic area rapidly, pushing the distribution threshold toward decentralization [cite: 2, 3].

#### 2.2.2 Determining the Optimal Values
The optimality of these coefficients is determined by the **maximum profit function** of the upstream supplier. The research explicitly links the node distribution threshold to profit maximization under constraints of information asymmetry. The profit function considers:
*   **Cost Bonus Coefficient:** The savings achieved through IoT integration.
*   **Output Matching Coefficient:** How well supply meets demand.
*   **Profit Loss from Information Asymmetry:** The cost of not knowing the exact state of the network [cite: 3, 8].

Therefore, the optimal distribution threshold is the point where the marginal cost of adding a node (diffusion) equals the marginal benefit of risk reduction ($k$) and profit maximization.

### 2.3 Service Level vs. Logistics Cost Trade-offs

The classical determination of warehouse node distribution thresholds is grounded in the trade-off between **Service Level** (usually measured by lead time) and **Logistics Costs** (transportation + inventory + warehousing) [cite: 13].

#### 2.3.1 The Cost-Service Threshold
In hierarchical models, the decision to add a layer to the hierarchy (e.g., adding a regional DC between the central warehouse and the customer) is triggered when the transportation cost savings from consolidation exceed the increase in inventory holding costs and fixed facility costs.

*   **Transportation Costs:** High outbound transport costs drive companies toward a **decentralized** structure (more nodes, lower threshold for opening a new node).
*   **Inventory Costs:** High inventory holding costs drive companies toward a **centralized** structure (fewer nodes, higher threshold for opening a new node) [cite: 13].

#### 2.3.2 The "Golden Rule" Threshold
A practical heuristic found in the literature for determining the optimal location count is the "Golden Rule" of warehouse location strategy: positioning facilities within a **one-day ground shipping distance of 80% of the customer base** [cite: 14]. Here, the threshold is explicitly defined as "80% coverage within 24 hours." This time-based threshold determines the spatial distribution of the nodes.

### 2.4 Capacity and Utilization Thresholds

Beyond the spatial distribution, the internal operational status of a warehouse acts as a threshold for network reconfiguration.

#### 2.4.1 The 85% Utilization Rule
Research indicates that the optimal warehouse space utilization rate is between **80% and 85%**.
*   **The Threshold:** 85% utilization.
*   **The Consequence:** Once inventory levels push utilization beyond 85%, efficiency drops drastically due to congestion (lack of maneuvering space for forklifts and staging).
*   **Network Implication:** Exceeding this threshold acts as a trigger to redistribute inventory to other nodes in the hierarchy or to acquire additional node capacity [cite: 6].

---

## 3. The Network Science Perspective: Thresholds in Hierarchical Configuration Models (HCM)

In the field of network science and graph theory, the "Hierarchical Configuration Model" (HCM) is a rigorous mathematical construct used to model complex networks with community structures (like social networks, the internet, or biological networks). The "distribution threshold" in this context refers to the **percolation threshold**—the critical point at which the network transitions from a collection of disconnected clusters to a connected giant component.

### 3.1 Defining the HCM in Graph Theory
The HCM is defined by two levels of structure:
1.  **Inter-community Level:** The graph behaves like a standard configuration model (random graph with a given degree sequence).
2.  **Intra-community Level:** Every vertex in the macroscopic configuration model is replaced by a "community" (a small, dense graph). These communities can have arbitrary shapes as long as they are connected [cite: 4, 5].

### 3.2 The Percolation Threshold (Connectivity)

The most significant "optimal" threshold in this theoretical context is the critical value that ensures the network is connected. This is vital for supply chains (to ensure goods can move from any supplier to any customer) and communication networks.

#### 3.2.1 Determinants of the Percolation Threshold
The percolation threshold in an HCM is determined by the **inter-community degree distribution** and the **internal structure of the communities**.

Research establishes that a giant component (a connected network spanning a significant fraction of the nodes) exists if and only if the size-biased mean of the inter-community degree distribution ($\nu_D$) satisfies the condition:

\[ \nu_D > 1 \]

This parameter $\nu_D$ is derived from the probability generating functions of the degree distributions. Specifically, if the communities are dense and follow a power-law degree distribution, the edges *between* communities must follow a power law with an exponent that is one higher than the exponent of the degree distribution to maintain connectivity [cite: 5].

#### 3.2.2 Critical Component Sizes
At the critical threshold (where the network is on the verge of connecting or fragmenting), the size of the components scales in a specific way. For a critical HCM on $N$ vertices, the ordered component sizes are of order $O(N^{2/3})$ [cite: 15]. This scaling law is a fundamental determinant of how "robust" the hierarchical structure is. If the node distribution (community sizes) does not adhere to these scaling laws, the network will fragment.

### 3.3 The Role of Community Size Distribution
The distribution of the *sizes* of the communities themselves acts as a threshold determinant.
*   If community sizes are too large relative to the inter-community links, the network becomes "trapped" in local clusters.
*   If community sizes are small and inter-links are high, the hierarchy dissolves into a random graph.
*   **Optimal Distribution:** The optimal distribution of community sizes is often power-law distributed, allowing for a "scale-free" topology that is robust against random node failures but vulnerable to targeted attacks on hubs [cite: 16, 17].

---

## 4. Mathematical Formulations of Distribution Thresholds

To provide a rigorous academic analysis, we must detail the mathematical formulations that govern these thresholds.

### 4.1 The Optimization Function for E-Commerce Nodes
As cited in multiple sources [cite: 2, 3, 7, 8, 9], the node distribution model in an IoT environment is governed by:

\[ f(x) = \text{Average Trend} + k \cdot (\text{Risk Control}) + r \cdot (\text{Diffusion}) \]

*   **Constraint:** The model assumes no shortage of product supplies upstream.
*   **Objective:** Maximize the profit function:
    \[ \Pi = \alpha \cdot (\text{Cost Bonus}) + \beta \cdot (\text{Output Matching}) - \gamma \cdot (\text{Info Asymmetry}) \]
    Where $\alpha, \beta, \gamma$ are coefficients determined by the IoT environment's efficiency.

The "threshold" for optimal distribution is the value of node density ($D$) that maximizes $\Pi$. If the risk coefficient $k$ increases (e.g., during a pandemic or supply shock), the optimal $D$ increases (more distributed nodes).

### 4.2 The Hierarchical Clustering Algorithm (NG-RPBFT)
The threshold logic for node assignment in the NG-RPBFT algorithm is explicitly procedural [cite: 1]:

```pseudo
IF Size(Group_i) > (Total_Nodes / k_Clusters) THEN
    Identify Excess_Node (Node with Max Distance from Center)
    Identify Target_Group (Group with 2nd Min Distance)
    Move Excess_Node to Target_Group
END IF
```

This algorithm proves that the "optimal" distribution is one that minimizes the variance in cluster sizes, subject to the constraint $N/k$.

---

## 5. Factors Influencing Threshold Determination

The determination of these thresholds is not arbitrary; it is influenced by specific exogenous and endogenous factors.

### 5.1 Demand Characteristics
*   **Demand Level:** High volume demand lowers the threshold for opening new nodes (economies of scale).
*   **Spatial Volatility:** Highly variable demand patterns require a lower distribution threshold (more decentralized nodes) to maintain service levels [cite: 13].

### 5.2 Product Characteristics
*   **Product Value:** High-value items typically have a higher threshold for decentralization (they are kept central to reduce inventory costs).
*   **Perishability:** Perishable goods (e.g., fresh agricultural products) require a "dynamic node layout model" where the threshold is determined by shelf-life constraints. Research shows that optimizing node layout for fresh products can reduce delivery costs by 20% and increase efficiency by 30% [cite: 18].

### 5.3 Infrastructure and Geography
*   **Accessibility:** The "center of gravity" approach determines optimal locations based on minimizing transport costs. However, this is constrained by the availability of land and labor. The threshold for placing a node is often the "impedance" or cost of transport in the last mile [cite: 19, 20].
*   **Traffic and Road Conditions:** In urban logistics, the threshold for node distribution is influenced by traffic peak hours and road safety. A node is only "optimal" if it falls within a specific time-distance threshold from the customer [cite: 21].

---

## 6. Algorithmic Approaches to Threshold Determination

Research highlights several computational methods used to find these thresholds.

### 6.1 Benders Decomposition
For large-scale adaptive network supply chain problems, **Benders decomposition** is used to separate the warehouse location problem (master problem) from the routing problem (subproblem). The threshold for convergence is determined by the gap between the upper and lower bounds of the solution [cite: 22].

### 6.2 Genetic Algorithms and Particle Swarm Optimization
Multi-objective optimization problems (balancing cost vs. service) are often solved using **Genetic Algorithms (GA)** or **Particle Swarm Optimization (PSO)**.
*   **GA:** Uses mutation and crossover to find the optimal node configuration. The "threshold" here is the fitness function value that triggers the termination of the algorithm [cite: 23, 24].
*   **PSO:** Used to solve 4-echelon network models. The threshold is the error rate or the number of iterations required to find a Pareto-optimal solution [cite: 23].

### 6.3 Hierarchical Neural Networks
In advanced applications (like solar radiation modeling or image recognition for inventory), **Deep Neural Networks (DNNs)** are used to identify spatial distribution thresholds. For example, a spatial dispersion threshold (e.g., 190 km) was identified as optimal for model portability in sensor networks [cite: 25]. While this is a specific application, the principle applies to "smart" warehouses using AI to determine distribution patterns.

---

## 7. Case Studies and Applications

### 7.1 E-Commerce (Amazon and General Platforms)
Research on Amazon's supply chain highlights the use of the **Node Distribution Model** involving risk-control coefficients. The complexity and dynamics of the e-commerce environment require that the threshold for node distribution be dynamic. The "optimal" threshold is constantly adjusted based on real-time data regarding "diffusion" (sales velocity) and "convergence" (inventory consolidation) [cite: 2].

### 7.2 Power Distribution Networks
While distinct from physical warehousing, power distribution networks also use hierarchical node models. Here, the threshold is often a **voltage deviation** limit or a **reliability index**. Research on IEEE 33-node systems shows that hierarchical distributed control strategies use thresholds to coordinate between local PV units and central substations. The "optimal" distribution is one that keeps voltage within 0.98–1.02 p.u. [cite: 26, 27].

### 7.3 Wireless Sensor Networks (WSN)
In WSNs, hierarchical clustering is used to save energy. The threshold is an **energy level** or a **sensed value** (e.g., temperature > 80°F). If a node's value exceeds this threshold, it transmits data to the cluster head. This "hard" threshold determines the distribution of active nodes in the network [cite: 28, 29].

---

## 8. Conclusion

The determination of the optimal warehouse node distribution threshold in hierarchical configuration models is governed by the interplay of **algorithmic constraints**, **economic trade-offs**, and **network topology**.

1.  **Algorithmic Determinant:** The ratio **$N/k$** serves as the fundamental clustering threshold to ensure balanced resource allocation [cite: 1].
2.  **Economic Determinant:** The **Risk-Control ($k$)** and **Diffusion ($r$)** coefficients determine the density of the network required to maximize profit under uncertainty [cite: 3].
3.  **Topological Determinant:** The **Percolation Threshold ($\nu_D > 1$)** determines the connectivity of the hierarchical graph, ensuring that the local communities (warehouses) form a cohesive global supply chain [cite: 4].
4.  **Operational Determinant:** The **85% Capacity Rule** and **Service Level (Time)** constraints act as practical boundaries that trigger network expansion or reconfiguration [cite: 6, 14].

Optimal distribution is achieved when the network topology satisfies the percolation threshold for connectivity, the clustering threshold for load balancing, and the economic thresholds for cost-efficiency and risk mitigation.

## References
[cite: 13] Factors determining distribution structure decisions in logistics: a literature review and research agenda.
[cite: 23] Determining an optimal warehouse location, capacity and product allocation in a multi-product multi-period distribution network: a case study.
[cite: 19] The concept of a warehouse and its functions at the enterprise. Types of warehouses and their classification.
[cite: 20] Hierarchical modelling of Last Mile logistic distribution system.
[cite: 2] Research on Supply Chain Optimization at Amazon.
[cite: 1] Node Rating-Based and Grouping Raft cluster Practical Byzantine Fault Tolerance (NG-RPBFT).
[cite: 18] Optimization Algorithm of Network Node Layout.
[cite: 28] Hierarchical or cluster based routing protocol for wireless sensor network.
[cite: 21] Choosing a Warehouse Location: 7 Critical Criteria to Consider.
[cite: 14] Warehouse Location Selection Guide.
[cite: 6] Space Utilization in the Warehouse.
[cite: 30] Distribution threshold supply chain network design.
[cite: 25] Identification of a spatial distribution threshold for the development of a solar radiation model using deep neural networks.
[cite: 4] Hierarchical Configuration Model.
[cite: 5] Hierarchical configuration model (arXiv).
[cite: 16] Power-law relations in random networks with communities.
[cite: 26] Hierarchical distributed and local voltage control strategy for PV clusters.
[cite: 29] The comparative study of hierarchical or cluster based routing protocol for wireless sensor network.
[cite: 27] DG hierarchical planning model.
[cite: 3] Optimization and Simulation for E-Commerce Supply Chain in the Internet of Things Environment.
[cite: 7] Applications and Challenges of Warehouse Optimization Technology in E-commerce Platforms.
[cite: 8] E-Commerce Model Based on the Internet of Things.
[cite: 2] Research on Supply Chain Optimization at Amazon.
[cite: 22] Combining Benders decomposition and parallelisation to solve large-scale adaptive network supply chain management problems.
[cite: 1] Node Rating-Based and Grouping Raft cluster Practical Byzantine Fault Tolerance (NG-RPBFT).
[cite: 31] Mitigating environmental and density risk in supply chains.
[cite: 4] Hierarchical Configuration Model (ResearchGate).
[cite: 5] Hierarchical configuration model (arXiv).
[cite: 15] The probability of unusually large components in the near-critical Erdős-Rényi graph.

**Sources:**
1. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8juMmzvxcRW3zKctE-KYBUZoetMobjcXci-S-GT65c4N3XiVXIx0LxO2xSWrrKEpl4uzB59HH947fjhVU5mMHkPUZYy-LYfxxyZbF7S47RR_BYH0uPziTVX2b)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENuwyL49y67qnXpq0LYZz4RkKKACCjQ3v182f0cSHsnbtcwJbH8Pabui7l4w9C2RQcY6Y5ezgjR8y637b5U4QCXo7FJmrbzIl9Uy3umS6Isrse6afQrFfyVc_S5aLrfNhCWe95L-G_JoU5nIJ6acjjkLy2LHU1tYxsj38mg6hGBfGmBpRNse60r59mUhtNA8Et2Zb-Jgoo)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEQ-N7_YdRmurYzzL_xTomfZmj0W-qFUKh0yY6U9j6SlAAInKBjlAgxWQ47zLplNi92Lt2GXYjWxjZq4zN52BM-BQOpu7sD7N1_SdtH5aA-Ww_o2iYTmgxpagfNl9ZUAbnJK3Z1nEpCtr9VNZIcy_x2L0OhZSo48iRCwY5QaV-Sb0QW8Ah26ZqWA8JmXAI5bGitegIEOpr-Qn-7eD0br48S5dPYH58b3Wl5Knob6DO1LA5uszMXw1Zbx58THTMSDXdVhMzsCg=)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5TNO7IURzvQiyIDbMRCTkpkqKaD65Y6hTDPFSwtkTi6B9tiu3rCFvLhW9sxihMct5vFN7jvO0-Hj2HeK8T-KMgC_69HYn0dcafbUDYUhohiltU95ohbZyoyvuPqvDu557pnU0hkwyhs_XO3sgcabKWZpTHIVUgWKCAzr4iihIrgDAlciTUJBV)
5. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHZ5BQKnyjDbmR3sLWOBuHkfBy95KGpDW4aB2tRUyw0wzlCdZPxsHhVWjItnrUZLGEwCW6vcM5YvTSxRc1iK1gVGBOXRc6WzBzc5DW0EpR3WFMyh38)
6. [netsuite.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlRPxy8TzotLJBvK4ZAK3Tb7VZYj7huXu4mPt10cJnoay__WkJIfr7cjckBTkJV0OYoVKWZ0Ob7OpFufen00VIw-Ln-cmsN5a3bI5DI2eRwY7R3l6d7AkBzV4F9vdschvD_JinrEZ64dkhy2sVjCvGu9SHvaJcw7DZm7m_JPORuLP4M5exphsClc9ZnKJyXiuGY7kAP7XiPEWyZxKL)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGx-snX3H6pN35CNawEyabnTshulcZttI8w5FCrFoFEDMjPWnwxRma9cGLZJDx3cbA-tcjHnmmLFh0LC5hmQhpOkm2chHPaEq9gh7RjcNdeJMk3G87G_dGKqmqk0qir5hkdVsbSQqOVS-gfxFgCBBUaobzyYZznOeaaLdjIfNzlPXqiG3d01TvCJEb1ZgLiQ9ocyaP6kWYqDDW8sR99IhmrGjflgRv-DR53fSGvadYNbdOs2Zcb_7AlfaDtKu8oCqXcYKxO4KIrWaQUBk0VWODNIWMmfqCirgBxCJhauZjJ)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHafGlQxh6Bv0FEMkbMuISEA6zelvnz6cG-yg9nGu9wiAv2uJJk5CixBt_JI8mQuZym4pMJ4v6Cfa3Im7iBIqa6fl6Y07d3enruwQAVQ1ZSLoUrSoJhBiYsJzsoK7btvJd1VDb0j0R1YgeMi_6kkK8hKO8kT3MJm9kz-pzV2t9ThQzPNArIY-wUMbDsBUJAibRvlPgF-ZDE_Q==)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzkY7mce72ZmcBtMb7cXRCIB-KJ2npeDqWDrwNUEoJ_4mKkqtldtyf2AYUEOm6o_7ESFXQ5qqU42biQF4UFN1YuN9iZ8Y1PiZ4Co2IR4mz1yHx3P2nNNSseMd6cbMOIQX8o2KTy32cXWTSTkC9tvRH2sdmz1Ho1imAEZzCzgWDgZmtXHrgKQmDJpJwJAzx2XAvQpaarl9zQo6nai5_1ssIc7SdNTulxOjlKPzQR-g6fPuLj5OIqVNdaJAuMKSA5yKWjp09TWG9j_VqPgdWGR0ts5YD)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxp8fDWRAQHytQT9xZQsqXIqcYqnDqX2kaIM-7Vp3RttP99CtMJtiCNHkiUh2FPOknLZ-n16nWx8s7cmtyhQnRol84SpIrV_0WfKvOJDLbl0f3dpmqrEhoQk3-EXjog5St700LGKAlx229OQSCgmmixljoyOCicMGa0tLwR-3VyukhOpwd2TLWxpIFsj1wCl7O1miqZamggdD19yn8iSbM1P5WKE-dki9Stai00glEgpKkXb8r0N8=)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOQ_uQf8HecsdEBKtYrSa7QP83Tp8wHycTZ_gcw0s72wRipvAqeCc4elIkgXycDkGf9WYDxC3GkDEgm_B2CJCcbmKrhDByF0Bd1U3h9nzAmHz234NdE2l1qMU9yegUo3YIaDf46KglSQSR-oflEiTKF7Ffr4FfF59XFn8QWMxfHsQs-5zNK8N8Gk6pp9CTsViuRmRVCl63w3NAdaO3hLV2taYw9K2q_nDN4cSyxriuYYsrlK1l9drshnwOmrudI1drNnAvaAx-JtrYAzHqBU52136wLmBN9dlJck4=)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-XBvJdd_CqYdzxiywQAajEyznK83LUoIvfYYGXrEAcoxyoojLpqs-LH3e0dDJ_jmoNsPjOXdoPRz8lVC0R1g8yRrhsuzHM7MGk53X1Mpxok9CgvtcFcILce4rZPLXjaOD1TgCGoW9avQkq3A5VLRS3124hKS3UGrF13ZjfHvfeZhWO2oeLPU0pPSQs0c8b6PEe0XDe6RfkSQB3CbhED0rJp8RbqGdYufHm3XnwbLrRcfn9kTQwr371No6qNmZsxdAshCXAd9so1DL-r6UzWW75c8=)
13. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECwjl1ey3JiDsba-5at3r1e7mjpLUz8CGTOb6IJw70WZ2geKSm9pyBtldj4W6Cdlqr02JFUNGfN98Yt7b8-_It6r7Pbr2QTMnr3-KdSNApafJNa-jHn1EEFVqWJ1bwUjqAuL2uS-KSt122ysRzobVrkllYi3vpIvFuD_v24TJ1QQf4FXy5ZBjnG7TERBj1yS0lvWk9vuKYVviAN2rbdPfYjwYqDKM9KC1Jd7K21ul8gbb4CmBzIrfUUUPqaa6LOtgB34imwQKVANhPCxyRWOm4pHg=)
14. [deliberatedirections.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTbZdjvTqxpk9MWL-S0TQWQJAC3yVLQidPg1qxhqvfb-n4v_HpHzPiNpQIyU9BuN_l4O2-xKdm0uL8zc74lbBvNeUTBA47bEEwq1Uk1lM6V7DLZAlzfXP4Zx0RFJWYB4RsG8RPni-hDmwY7x6DM1FU2a3TVm8H4QtJ)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyQeKy4u9jQJ8A_etzCfW6C7ZJ7GCYkmAopmtd8vcO6-LcH3cylpIBPjdVeSiue74KDPjNxsNaFwJOsUo_oujd7s3UTSyNwMrNHhhpCj3z5nPIjewU9imwrTs9S7ZzzBlJRjg3zA-ics6t1LZf7sw1ya3UxcdOJDhT578m0NAbLpuxsiEeklXVl5ypipg7DPkgw6elTbaNjG_QlCDj3zNCaa7DdLIgZROUBjlOcf6sdlHcIq1Nkd0YBx-K8OOFQA==)
16. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhcKb1HMjivSV-UuqHFNDb1MpPw4acfvW_fLqhAo7lSa7NXFQN0OMJMqBUnWIJvIn8p-8PnA6SgCJNjbuEB4Bj5LlM2HE1LDz8P1PuTE30X6MAOuy7LRJre-yHy6IGD8izMbz7Q6I8aOjQRzUo7dwJkE6ePbA1Uythj1HiiRqkde5rHg==)
17. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH17RDsFcUh5gzw0LAnuCDjNgohBCxvXRRM9zxIwitWR04Hho-_5-tJnW7IEbp7ilSlp53RhHxXetLiuRCH5ESzGzd5Xj3VrpBkG-s_JDmDKxuAyzNR)
18. [worldscientific.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgMLpOVGZ7QWWO2oOZ5CPHxpzpsOTlDgBt6uLXDzbZcdg5d989DjQdjP5KU09ZMRrLs2CfwPQNjamM7Gp3lVDvikr2vRaqT-jBw_iUqkomRu2S_7VCvKPMe6dsBQiizNLAIjoA6RpGN8xuaHTNEiUU6NNcChoCSJ8iobgBH3rZj-fMW-8=)
19. [bsu.by](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8FOu8WFWTptIX0aMxICl2dYip-_BmBLoPbDP88fyxwAa11cwIucg0rX2nKY2zRJoYXWSkqn0X1-EZtFRZjBtqmqVqP-mbxBBw2tpY9R7XEMDHu4pXpnjydm4_VbWxVmm-ApqXsDGg6VnN-UuENOC9wQ==)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFT1HgKdUCpA70AX988gaTMXzc12hfhdF3mqmlC5Hidmsy-zxqUyq5Owlv-XGVxkyAWxvU-HAoMZaN4w8SJzhRHb5m7M1UXB9k3NwKXofYg2L5FwegMGa_FWg_Gu6U0SBbZLDB0F_MXZr9ZK1kbJdGyQxaMo5AsU-rdh6mtN5x9hC4t5Y7XDFFJ7bwPP9CAawfwMsWqc1IhoAz1T3jQ2evZkvbBDfQnsds=)
21. [cyzerg.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeZTstPmz-MjrXNqOFQkikCd4srP6nYtiV1hx-yTFtfpuqqpTTjiimEBviikomIjE5fKHUX3xTavKpO1klyN7r8FPnH7SKHn6PU8hy-xf_EklSLcZLAJqLa5b34cIqw4BuKNgnBv3uHk5IZ5SfclqsRVZEVM-mpuULQREbz70DPqhfr8vjdzILE5eH)
22. [ketmarket.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEelF5srdLYprRfM0x2TkS0QuAcA_4i-EAaHq654lpm2kb4xdsZuBxvYXOkfiB2tg7HdxxPfSjClzlnh2Bcoo5qAxZY_sWLSXuM6u4swS8nzC3s5pfPLc-1xigoMrbftFHBbRCEDEJ2nYsP6bxB-XkjThgwZ7vdEAvXTd74bMHCWTMy2c2WtzTKvaPgXRXLt_Ij865cllhfDEImWrRaTmx1zvy_KvEjjPe5MYe8E6LhsZFVozR7RT7R1BIATDMi2vBPHEw90_3_ZsSwJl0Jru4dlzllSA==)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyDgfaFpPHvKyIiAcG6nOoLRmk5OASPgLOLtpctSMlQABnFBJD0gEt1pRgoXjHaxsLMwA-7lAG5Tl7ec5NkxN3L8M6mF1nkV-01K5PAor3RCK-wUlgFUuL-7VaUNAzxALnA6inWmJuI87EBRiIQI4WS6PpnnEOFfpxFWDgO_Yayu8cPZ3iRAx4Gf6YspDYZ1WsXCK9zo9K4odaOGiDcIiF4jSIIf7B6NIZcjH7invl3qAupCeQBsaTBTuD2rHYv05g4KRt2GXOv0fSzepzH6dq4sEk4D2Cmv2aqWGlcj0OGs_b0krfm-eNjmDi9vzY4BgKErEB)
24. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFY35KkZQbaiNW9iKJOqdekVnZfP9tu1RsAiswknJhWebNts_9C2OozBcM3So5O8zTOCjMnUxjefn3_ik8pF9SCPxd2hqhnlDLyNoLm4zLgyrGXuBB61rw2gGM7eCozs-v1JbZIBFXmaBteOGdVqw6zbpX)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERG4XWAhl1viZmnCZGZe40UEOJLTTOU7XENHqKyFcoZCnNA0YzRet9YyYBwOb7qZ5TOr2Ej-68r_Z_kGCsPvoKllKrQ-Tem4Vdaq7p01CA9I86c9Lk0lL-B_dNR_bd5shgFSlCqLhdKHLfX4lFU8cuLzNk-8eMw7XKFK3oMvnjFBJ1RmRurKcohUa1tJg3TTD4WABgw7uIVLx0Q1vlPOMHKUu1NDJ90fYmXWmGRdoXAFBE6N3B5E63r3RMHDDrpoE8sQW0HZWqAr7ucTuIJ_SFwx-MLokNrErfWdkhUnRWDB8YBevP)
26. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaeaVEUZOjEFcddep5fcXBtd-Eyl6eqCUGU7uSrIplevcUb64rd1CO1lUC0n3TFuelFmD-fH0ES0OqzZWTcsqIhQPMXNRFBVohpiitO5e9yVUSBvVVZ3njppi4s5U=)
27. [myu-group.co.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECG84Lib719XhJkrEigK3jjzyCPgP2FX5h87cSoz5P7XP64HRaOfk_Gc0pV2yBLomV8PBAOhyvvA6YKavI2v8lCNHzgwUSdSOWvSQ7KUVDWQd_frkbRp8enDIn6AhFfGamWIF_5d0=)
28. [gvpress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGST7Ftnp0woaGkcXvW55H9xf7wypMH2EB08Pf6N5mzYMUuI-GLWJk_FvoSd-RELqr01PHo1XGSfkxFwcVwFCPKloQqb5u7mgd0QHsiiL1DIu51-eHHWvxl3EFucDJazLNeebT3FA=)
29. [ijert.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAANVLuvVY9IMIMvOPlw9uRY7VEseigHXgK-KlATvFjBTIXUPK6gs6krVyAv3JfiwrAFE8M309aPaHRyyAPP0qeCi62Nis7scoulVOgPCXbrT9l0kH5BQDd04wJGlyLQH1yVjvUM-RKjDg9UThhJhw4bQ895OfIJSeOUzC0iDLeY21hldmruV4b2cZEvoEQhhRDhlAMHCishr2cyartUM8iYwLBxrcKU1OEFisP1E=)
30. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjoebZ4Bh0Ul1EbK0kJWKInyGsGHrXQRxd495Vm-edGtuLRFa16y4xOVsW-EcS7voAJLQyr1L2cMLG_wEfAuVqzHtmaNqb0JN47MP08xIU2cpkpnsisgB3gvA2)
31. [emerald.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0vNp_DZQi3DikCCt2wAN8zUjBStQMzEYjzKBwyJaQlpYxZHtU0C0kICRP6TBp098a2B2uCbmpBqicNEuj3SbE0S7Zm0JGoUzhrhflHfMGRkfZoI3Tpi9BEL47wz1z9si92OgTzy7zwikzzG2A_9BtHFEgZ_uejzL-Ilu0WPukMUzN7tOWB8VkF-63XVz4Z9DCbV-HDvGEjYw=)


## Annotations
Annotation(end_index=877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8juMmzvxcRW3zKctE-KYBUZoetMobjcXci-S-GT65c4N3XiVXIx0LxO2xSWrrKEpl4uzB59HH947fjhVU5mMHkPUZYy-LYfxxyZbF7S47RR_BYH0uPziTVX2b', start_index=868)
Annotation(end_index=1303, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENuwyL49y67qnXpq0LYZz4RkKKACCjQ3v182f0cSHsnbtcwJbH8Pabui7l4w9C2RQcY6Y5ezgjR8y637b5U4QCXo7FJmrbzIl9Uy3umS6Isrse6afQrFfyVc_S5aLrfNhCWe95L-G_JoU5nIJ6acjjkLy2LHU1tYxsj38mg6hGBfGmBpRNse60r59mUhtNA8Et2Zb-Jgoo', start_index=1291)
Annotation(end_index=1303, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEQ-N7_YdRmurYzzL_xTomfZmj0W-qFUKh0yY6U9j6SlAAInKBjlAgxWQ47zLplNi92Lt2GXYjWxjZq4zN52BM-BQOpu7sD7N1_SdtH5aA-Ww_o2iYTmgxpagfNl9ZUAbnJK3Z1nEpCtr9VNZIcy_x2L0OhZSo48iRCwY5QaV-Sb0QW8Ah26ZqWA8JmXAI5bGitegIEOpr-Qn-7eD0br48S5dPYH58b3Wl5Knob6DO1LA5uszMXw1Zbx58THTMSDXdVhMzsCg=', start_index=1291)
Annotation(end_index=1769, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5TNO7IURzvQiyIDbMRCTkpkqKaD65Y6hTDPFSwtkTi6B9tiu3rCFvLhW9sxihMct5vFN7jvO0-Hj2HeK8T-KMgC_69HYn0dcafbUDYUhohiltU95ohbZyoyvuPqvDu557pnU0hkwyhs_XO3sgcabKWZpTHIVUgWKCAzr4iihIrgDAlciTUJBV', start_index=1757)
Annotation(end_index=1769, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHZ5BQKnyjDbmR3sLWOBuHkfBy95KGpDW4aB2tRUyw0wzlCdZPxsHhVWjItnrUZLGEwCW6vcM5YvTSxRc1iK1gVGBOXRc6WzBzc5DW0EpR3WFMyh38', start_index=1757)
Annotation(end_index=2107, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlRPxy8TzotLJBvK4ZAK3Tb7VZYj7huXu4mPt10cJnoay__WkJIfr7cjckBTkJV0OYoVKWZ0Ob7OpFufen00VIw-Ln-cmsN5a3bI5DI2eRwY7R3l6d7AkBzV4F9vdschvD_JinrEZ64dkhy2sVjCvGu9SHvaJcw7DZm7m_JPORuLP4M5exphsClc9ZnKJyXiuGY7kAP7XiPEWyZxKL', start_index=2098)
Annotation(end_index=5058, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8juMmzvxcRW3zKctE-KYBUZoetMobjcXci-S-GT65c4N3XiVXIx0LxO2xSWrrKEpl4uzB59HH947fjhVU5mMHkPUZYy-LYfxxyZbF7S47RR_BYH0uPziTVX2b', start_index=5049)
Annotation(end_index=5784, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8juMmzvxcRW3zKctE-KYBUZoetMobjcXci-S-GT65c4N3XiVXIx0LxO2xSWrrKEpl4uzB59HH947fjhVU5mMHkPUZYy-LYfxxyZbF7S47RR_BYH0uPziTVX2b', start_index=5775)
Annotation(end_index=6191, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8juMmzvxcRW3zKctE-KYBUZoetMobjcXci-S-GT65c4N3XiVXIx0LxO2xSWrrKEpl4uzB59HH947fjhVU5mMHkPUZYy-LYfxxyZbF7S47RR_BYH0uPziTVX2b', start_index=6182)
Annotation(end_index=6445, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8juMmzvxcRW3zKctE-KYBUZoetMobjcXci-S-GT65c4N3XiVXIx0LxO2xSWrrKEpl4uzB59HH947fjhVU5mMHkPUZYy-LYfxxyZbF7S47RR_BYH0uPziTVX2b', start_index=6436)
Annotation(end_index=6989, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-XBvJdd_CqYdzxiywQAajEyznK83LUoIvfYYGXrEAcoxyoojLpqs-LH3e0dDJ_jmoNsPjOXdoPRz8lVC0R1g8yRrhsuzHM7MGk53X1Mpxok9CgvtcFcILce4rZPLXjaOD1TgCGoW9avQkq3A5VLRS3124hKS3UGrF13ZjfHvfeZhWO2oeLPU0pPSQs0c8b6PEe0XDe6RfkSQB3CbhED0rJp8RbqGdYufHm3XnwbLrRcfn9kTQwr371No6qNmZsxdAshCXAd9so1DL-r6UzWW75c8=', start_index=6956)
Annotation(end_index=6989, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENuwyL49y67qnXpq0LYZz4RkKKACCjQ3v182f0cSHsnbtcwJbH8Pabui7l4w9C2RQcY6Y5ezgjR8y637b5U4QCXo7FJmrbzIl9Uy3umS6Isrse6afQrFfyVc_S5aLrfNhCWe95L-G_JoU5nIJ6acjjkLy2LHU1tYxsj38mg6hGBfGmBpRNse60r59mUhtNA8Et2Zb-Jgoo', start_index=6956)
Annotation(end_index=6989, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOQ_uQf8HecsdEBKtYrSa7QP83Tp8wHycTZ_gcw0s72wRipvAqeCc4elIkgXycDkGf9WYDxC3GkDEgm_B2CJCcbmKrhDByF0Bd1U3h9nzAmHz234NdE2l1qMU9yegUo3YIaDf46KglSQSR-oflEiTKF7Ffr4FfF59XFn8QWMxfHsQs-5zNK8N8Gk6pp9CTsViuRmRVCl63w3NAdaO3hLV2taYw9K2q_nDN4cSyxriuYYsrlK1l9drshnwOmrudI1drNnAvaAx-JtrYAzHqBU52136wLmBN9dlJck4=', start_index=6956)
Annotation(end_index=6989, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGx-snX3H6pN35CNawEyabnTshulcZttI8w5FCrFoFEDMjPWnwxRma9cGLZJDx3cbA-tcjHnmmLFh0LC5hmQhpOkm2chHPaEq9gh7RjcNdeJMk3G87G_dGKqmqk0qir5hkdVsbSQqOVS-gfxFgCBBUaobzyYZznOeaaLdjIfNzlPXqiG3d01TvCJEb1ZgLiQ9ocyaP6kWYqDDW8sR99IhmrGjflgRv-DR53fSGvadYNbdOs2Zcb_7AlfaDtKu8oCqXcYKxO4KIrWaQUBk0VWODNIWMmfqCirgBxCJhauZjJ', start_index=6956)
Annotation(end_index=6989, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxp8fDWRAQHytQT9xZQsqXIqcYqnDqX2kaIM-7Vp3RttP99CtMJtiCNHkiUh2FPOknLZ-n16nWx8s7cmtyhQnRol84SpIrV_0WfKvOJDLbl0f3dpmqrEhoQk3-EXjog5St700LGKAlx229OQSCgmmixljoyOCicMGa0tLwR-3VyukhOpwd2TLWxpIFsj1wCl7O1miqZamggdD19yn8iSbM1P5WKE-dki9Stai00glEgpKkXb8r0N8=', start_index=6956)
Annotation(end_index=6989, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzkY7mce72ZmcBtMb7cXRCIB-KJ2npeDqWDrwNUEoJ_4mKkqtldtyf2AYUEOm6o_7ESFXQ5qqU42biQF4UFN1YuN9iZ8Y1PiZ4Co2IR4mz1yHx3P2nNNSseMd6cbMOIQX8o2KTy32cXWTSTkC9tvRH2sdmz1Ho1imAEZzCzgWDgZmtXHrgKQmDJpJwJAzx2XAvQpaarl9zQo6nai5_1ssIc7SdNTulxOjlKPzQR-g6fPuLj5OIqVNdaJAuMKSA5yKWjp09TWG9j_VqPgdWGR0ts5YD', start_index=6956)
Annotation(end_index=6989, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEQ-N7_YdRmurYzzL_xTomfZmj0W-qFUKh0yY6U9j6SlAAInKBjlAgxWQ47zLplNi92Lt2GXYjWxjZq4zN52BM-BQOpu7sD7N1_SdtH5aA-Ww_o2iYTmgxpagfNl9ZUAbnJK3Z1nEpCtr9VNZIcy_x2L0OhZSo48iRCwY5QaV-Sb0QW8Ah26ZqWA8JmXAI5bGitegIEOpr-Qn-7eD0br48S5dPYH58b3Wl5Knob6DO1LA5uszMXw1Zbx58THTMSDXdVhMzsCg=', start_index=6956)
Annotation(end_index=6989, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHafGlQxh6Bv0FEMkbMuISEA6zelvnz6cG-yg9nGu9wiAv2uJJk5CixBt_JI8mQuZym4pMJ4v6Cfa3Im7iBIqa6fl6Y07d3enruwQAVQ1ZSLoUrSoJhBiYsJzsoK7btvJd1VDb0j0R1YgeMi_6kkK8hKO8kT3MJm9kz-pzV2t9ThQzPNArIY-wUMbDsBUJAibRvlPgF-ZDE_Q==', start_index=6956)
Annotation(end_index=8096, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENuwyL49y67qnXpq0LYZz4RkKKACCjQ3v182f0cSHsnbtcwJbH8Pabui7l4w9C2RQcY6Y5ezgjR8y637b5U4QCXo7FJmrbzIl9Uy3umS6Isrse6afQrFfyVc_S5aLrfNhCWe95L-G_JoU5nIJ6acjjkLy2LHU1tYxsj38mg6hGBfGmBpRNse60r59mUhtNA8Et2Zb-Jgoo', start_index=8084)
Annotation(end_index=8096, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEQ-N7_YdRmurYzzL_xTomfZmj0W-qFUKh0yY6U9j6SlAAInKBjlAgxWQ47zLplNi92Lt2GXYjWxjZq4zN52BM-BQOpu7sD7N1_SdtH5aA-Ww_o2iYTmgxpagfNl9ZUAbnJK3Z1nEpCtr9VNZIcy_x2L0OhZSo48iRCwY5QaV-Sb0QW8Ah26ZqWA8JmXAI5bGitegIEOpr-Qn-7eD0br48S5dPYH58b3Wl5Knob6DO1LA5uszMXw1Zbx58THTMSDXdVhMzsCg=', start_index=8084)
Annotation(end_index=8673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEQ-N7_YdRmurYzzL_xTomfZmj0W-qFUKh0yY6U9j6SlAAInKBjlAgxWQ47zLplNi92Lt2GXYjWxjZq4zN52BM-BQOpu7sD7N1_SdtH5aA-Ww_o2iYTmgxpagfNl9ZUAbnJK3Z1nEpCtr9VNZIcy_x2L0OhZSo48iRCwY5QaV-Sb0QW8Ah26ZqWA8JmXAI5bGitegIEOpr-Qn-7eD0br48S5dPYH58b3Wl5Knob6DO1LA5uszMXw1Zbx58THTMSDXdVhMzsCg=', start_index=8661)
Annotation(end_index=8673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHafGlQxh6Bv0FEMkbMuISEA6zelvnz6cG-yg9nGu9wiAv2uJJk5CixBt_JI8mQuZym4pMJ4v6Cfa3Im7iBIqa6fl6Y07d3enruwQAVQ1ZSLoUrSoJhBiYsJzsoK7btvJd1VDb0j0R1YgeMi_6kkK8hKO8kT3MJm9kz-pzV2t9ThQzPNArIY-wUMbDsBUJAibRvlPgF-ZDE_Q==', start_index=8661)
Annotation(end_index=9153, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECwjl1ey3JiDsba-5at3r1e7mjpLUz8CGTOb6IJw70WZ2geKSm9pyBtldj4W6Cdlqr02JFUNGfN98Yt7b8-_It6r7Pbr2QTMnr3-KdSNApafJNa-jHn1EEFVqWJ1bwUjqAuL2uS-KSt122ysRzobVrkllYi3vpIvFuD_v24TJ1QQf4FXy5ZBjnG7TERBj1yS0lvWk9vuKYVviAN2rbdPfYjwYqDKM9KC1Jd7K21ul8gbb4CmBzIrfUUUPqaa6LOtgB34imwQKVANhPCxyRWOm4pHg=', start_index=9143)
Annotation(end_index=9819, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECwjl1ey3JiDsba-5at3r1e7mjpLUz8CGTOb6IJw70WZ2geKSm9pyBtldj4W6Cdlqr02JFUNGfN98Yt7b8-_It6r7Pbr2QTMnr3-KdSNApafJNa-jHn1EEFVqWJ1bwUjqAuL2uS-KSt122ysRzobVrkllYi3vpIvFuD_v24TJ1QQf4FXy5ZBjnG7TERBj1yS0lvWk9vuKYVviAN2rbdPfYjwYqDKM9KC1Jd7K21ul8gbb4CmBzIrfUUUPqaa6LOtgB34imwQKVANhPCxyRWOm4pHg=', start_index=9809)
Annotation(end_index=10110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTbZdjvTqxpk9MWL-S0TQWQJAC3yVLQidPg1qxhqvfb-n4v_HpHzPiNpQIyU9BuN_l4O2-xKdm0uL8zc74lbBvNeUTBA47bEEwq1Uk1lM6V7DLZAlzfXP4Zx0RFJWYB4RsG8RPni-hDmwY7x6DM1FU2a3TVm8H4QtJ', start_index=10100)
Annotation(end_index=10970, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlRPxy8TzotLJBvK4ZAK3Tb7VZYj7huXu4mPt10cJnoay__WkJIfr7cjckBTkJV0OYoVKWZ0Ob7OpFufen00VIw-Ln-cmsN5a3bI5DI2eRwY7R3l6d7AkBzV4F9vdschvD_JinrEZ64dkhy2sVjCvGu9SHvaJcw7DZm7m_JPORuLP4M5exphsClc9ZnKJyXiuGY7kAP7XiPEWyZxKL', start_index=10961)
Annotation(end_index=11978, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5TNO7IURzvQiyIDbMRCTkpkqKaD65Y6hTDPFSwtkTi6B9tiu3rCFvLhW9sxihMct5vFN7jvO0-Hj2HeK8T-KMgC_69HYn0dcafbUDYUhohiltU95ohbZyoyvuPqvDu557pnU0hkwyhs_XO3sgcabKWZpTHIVUgWKCAzr4iihIrgDAlciTUJBV', start_index=11966)
Annotation(end_index=11978, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHZ5BQKnyjDbmR3sLWOBuHkfBy95KGpDW4aB2tRUyw0wzlCdZPxsHhVWjItnrUZLGEwCW6vcM5YvTSxRc1iK1gVGBOXRc6WzBzc5DW0EpR3WFMyh38', start_index=11966)
Annotation(end_index=13098, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHZ5BQKnyjDbmR3sLWOBuHkfBy95KGpDW4aB2tRUyw0wzlCdZPxsHhVWjItnrUZLGEwCW6vcM5YvTSxRc1iK1gVGBOXRc6WzBzc5DW0EpR3WFMyh38', start_index=13089)
Annotation(end_index=13382, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyQeKy4u9jQJ8A_etzCfW6C7ZJ7GCYkmAopmtd8vcO6-LcH3cylpIBPjdVeSiue74KDPjNxsNaFwJOsUo_oujd7s3UTSyNwMrNHhhpCj3z5nPIjewU9imwrTs9S7ZzzBlJRjg3zA-ics6t1LZf7sw1ya3UxcdOJDhT578m0NAbLpuxsiEeklXVl5ypipg7DPkgw6elTbaNjG_QlCDj3zNCaa7DdLIgZROUBjlOcf6sdlHcIq1Nkd0YBx-K8OOFQA==', start_index=13372)
Annotation(end_index=14203, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH17RDsFcUh5gzw0LAnuCDjNgohBCxvXRRM9zxIwitWR04Hho-_5-tJnW7IEbp7ilSlp53RhHxXetLiuRCH5ESzGzd5Xj3VrpBkG-s_JDmDKxuAyzNR', start_index=14189)
Annotation(end_index=14203, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhcKb1HMjivSV-UuqHFNDb1MpPw4acfvW_fLqhAo7lSa7NXFQN0OMJMqBUnWIJvIn8p-8PnA6SgCJNjbuEB4Bj5LlM2HE1LDz8P1PuTE30X6MAOuy7LRJre-yHy6IGD8izMbz7Q6I8aOjQRzUo7dwJkE6ePbA1Uythj1HiiRqkde5rHg==', start_index=14189)
Annotation(end_index=14493, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENuwyL49y67qnXpq0LYZz4RkKKACCjQ3v182f0cSHsnbtcwJbH8Pabui7l4w9C2RQcY6Y5ezgjR8y637b5U4QCXo7FJmrbzIl9Uy3umS6Isrse6afQrFfyVc_S5aLrfNhCWe95L-G_JoU5nIJ6acjjkLy2LHU1tYxsj38mg6hGBfGmBpRNse60r59mUhtNA8Et2Zb-Jgoo', start_index=14472)
Annotation(end_index=14493, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGx-snX3H6pN35CNawEyabnTshulcZttI8w5FCrFoFEDMjPWnwxRma9cGLZJDx3cbA-tcjHnmmLFh0LC5hmQhpOkm2chHPaEq9gh7RjcNdeJMk3G87G_dGKqmqk0qir5hkdVsbSQqOVS-gfxFgCBBUaobzyYZznOeaaLdjIfNzlPXqiG3d01TvCJEb1ZgLiQ9ocyaP6kWYqDDW8sR99IhmrGjflgRv-DR53fSGvadYNbdOs2Zcb_7AlfaDtKu8oCqXcYKxO4KIrWaQUBk0VWODNIWMmfqCirgBxCJhauZjJ', start_index=14472)
Annotation(end_index=14493, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzkY7mce72ZmcBtMb7cXRCIB-KJ2npeDqWDrwNUEoJ_4mKkqtldtyf2AYUEOm6o_7ESFXQ5qqU42biQF4UFN1YuN9iZ8Y1PiZ4Co2IR4mz1yHx3P2nNNSseMd6cbMOIQX8o2KTy32cXWTSTkC9tvRH2sdmz1Ho1imAEZzCzgWDgZmtXHrgKQmDJpJwJAzx2XAvQpaarl9zQo6nai5_1ssIc7SdNTulxOjlKPzQR-g6fPuLj5OIqVNdaJAuMKSA5yKWjp09TWG9j_VqPgdWGR0ts5YD', start_index=14472)
Annotation(end_index=14493, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEQ-N7_YdRmurYzzL_xTomfZmj0W-qFUKh0yY6U9j6SlAAInKBjlAgxWQ47zLplNi92Lt2GXYjWxjZq4zN52BM-BQOpu7sD7N1_SdtH5aA-Ww_o2iYTmgxpagfNl9ZUAbnJK3Z1nEpCtr9VNZIcy_x2L0OhZSo48iRCwY5QaV-Sb0QW8Ah26ZqWA8JmXAI5bGitegIEOpr-Qn-7eD0br48S5dPYH58b3Wl5Knob6DO1LA5uszMXw1Zbx58THTMSDXdVhMzsCg=', start_index=14472)
Annotation(end_index=14493, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHafGlQxh6Bv0FEMkbMuISEA6zelvnz6cG-yg9nGu9wiAv2uJJk5CixBt_JI8mQuZym4pMJ4v6Cfa3Im7iBIqa6fl6Y07d3enruwQAVQ1ZSLoUrSoJhBiYsJzsoK7btvJd1VDb0j0R1YgeMi_6kkK8hKO8kT3MJm9kz-pzV2t9ThQzPNArIY-wUMbDsBUJAibRvlPgF-ZDE_Q==', start_index=14472)
Annotation(end_index=15403, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8juMmzvxcRW3zKctE-KYBUZoetMobjcXci-S-GT65c4N3XiVXIx0LxO2xSWrrKEpl4uzB59HH947fjhVU5mMHkPUZYy-LYfxxyZbF7S47RR_BYH0uPziTVX2b', start_index=15394)
Annotation(end_index=16251, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECwjl1ey3JiDsba-5at3r1e7mjpLUz8CGTOb6IJw70WZ2geKSm9pyBtldj4W6Cdlqr02JFUNGfN98Yt7b8-_It6r7Pbr2QTMnr3-KdSNApafJNa-jHn1EEFVqWJ1bwUjqAuL2uS-KSt122ysRzobVrkllYi3vpIvFuD_v24TJ1QQf4FXy5ZBjnG7TERBj1yS0lvWk9vuKYVviAN2rbdPfYjwYqDKM9KC1Jd7K21ul8gbb4CmBzIrfUUUPqaa6LOtgB34imwQKVANhPCxyRWOm4pHg=', start_index=16241)
Annotation(end_index=16743, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgMLpOVGZ7QWWO2oOZ5CPHxpzpsOTlDgBt6uLXDzbZcdg5d989DjQdjP5KU09ZMRrLs2CfwPQNjamM7Gp3lVDvikr2vRaqT-jBw_iUqkomRu2S_7VCvKPMe6dsBQiizNLAIjoA6RpGN8xuaHTNEiUU6NNcChoCSJ8iobgBH3rZj-fMW-8=', start_index=16733)
Annotation(end_index=17083, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8FOu8WFWTptIX0aMxICl2dYip-_BmBLoPbDP88fyxwAa11cwIucg0rX2nKY2zRJoYXWSkqn0X1-EZtFRZjBtqmqVqP-mbxBBw2tpY9R7XEMDHu4pXpnjydm4_VbWxVmm-ApqXsDGg6VnN-UuENOC9wQ==', start_index=17069)
Annotation(end_index=17083, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFT1HgKdUCpA70AX988gaTMXzc12hfhdF3mqmlC5Hidmsy-zxqUyq5Owlv-XGVxkyAWxvU-HAoMZaN4w8SJzhRHb5m7M1UXB9k3NwKXofYg2L5FwegMGa_FWg_Gu6U0SBbZLDB0F_MXZr9ZK1kbJdGyQxaMo5AsU-rdh6mtN5x9hC4t5Y7XDFFJ7bwPP9CAawfwMsWqc1IhoAz1T3jQ2evZkvbBDfQnsds=', start_index=17069)
Annotation(end_index=17338, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeZTstPmz-MjrXNqOFQkikCd4srP6nYtiV1hx-yTFtfpuqqpTTjiimEBviikomIjE5fKHUX3xTavKpO1klyN7r8FPnH7SKHn6PU8hy-xf_EklSLcZLAJqLa5b34cIqw4BuKNgnBv3uHk5IZ5SfclqsRVZEVM-mpuULQREbz70DPqhfr8vjdzILE5eH', start_index=17328)
Annotation(end_index=17820, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEelF5srdLYprRfM0x2TkS0QuAcA_4i-EAaHq654lpm2kb4xdsZuBxvYXOkfiB2tg7HdxxPfSjClzlnh2Bcoo5qAxZY_sWLSXuM6u4swS8nzC3s5pfPLc-1xigoMrbftFHBbRCEDEJ2nYsP6bxB-XkjThgwZ7vdEAvXTd74bMHCWTMy2c2WtzTKvaPgXRXLt_Ij865cllhfDEImWrRaTmx1zvy_KvEjjPe5MYe8E6LhsZFVozR7RT7R1BIATDMi2vBPHEw90_3_ZsSwJl0Jru4dlzllSA==', start_index=17810)
Annotation(end_index=18234, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFY35KkZQbaiNW9iKJOqdekVnZfP9tu1RsAiswknJhWebNts_9C2OozBcM3So5O8zTOCjMnUxjefn3_ik8pF9SCPxd2hqhnlDLyNoLm4zLgyrGXuBB61rw2gGM7eCozs-v1JbZIBFXmaBteOGdVqw6zbpX', start_index=18220)
Annotation(end_index=18234, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyDgfaFpPHvKyIiAcG6nOoLRmk5OASPgLOLtpctSMlQABnFBJD0gEt1pRgoXjHaxsLMwA-7lAG5Tl7ec5NkxN3L8M6mF1nkV-01K5PAor3RCK-wUlgFUuL-7VaUNAzxALnA6inWmJuI87EBRiIQI4WS6PpnnEOFfpxFWDgO_Yayu8cPZ3iRAx4Gf6YspDYZ1WsXCK9zo9K4odaOGiDcIiF4jSIIf7B6NIZcjH7invl3qAupCeQBsaTBTuD2rHYv05g4KRt2GXOv0fSzepzH6dq4sEk4D2Cmv2aqWGlcj0OGs_b0krfm-eNjmDi9vzY4BgKErEB', start_index=18220)
Annotation(end_index=18402, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyDgfaFpPHvKyIiAcG6nOoLRmk5OASPgLOLtpctSMlQABnFBJD0gEt1pRgoXjHaxsLMwA-7lAG5Tl7ec5NkxN3L8M6mF1nkV-01K5PAor3RCK-wUlgFUuL-7VaUNAzxALnA6inWmJuI87EBRiIQI4WS6PpnnEOFfpxFWDgO_Yayu8cPZ3iRAx4Gf6YspDYZ1WsXCK9zo9K4odaOGiDcIiF4jSIIf7B6NIZcjH7invl3qAupCeQBsaTBTuD2rHYv05g4KRt2GXOv0fSzepzH6dq4sEk4D2Cmv2aqWGlcj0OGs_b0krfm-eNjmDi9vzY4BgKErEB', start_index=18392)
Annotation(end_index=18757, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERG4XWAhl1viZmnCZGZe40UEOJLTTOU7XENHqKyFcoZCnNA0YzRet9YyYBwOb7qZ5TOr2Ej-68r_Z_kGCsPvoKllKrQ-Tem4Vdaq7p01CA9I86c9Lk0lL-B_dNR_bd5shgFSlCqLhdKHLfX4lFU8cuLzNk-8eMw7XKFK3oMvnjFBJ1RmRurKcohUa1tJg3TTD4WABgw7uIVLx0Q1vlPOMHKUu1NDJ90fYmXWmGRdoXAFBE6N3B5E63r3RMHDDrpoE8sQW0HZWqAr7ucTuIJ_SFwx-MLokNrErfWdkhUnRWDB8YBevP', start_index=18747)
Annotation(end_index=19386, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENuwyL49y67qnXpq0LYZz4RkKKACCjQ3v182f0cSHsnbtcwJbH8Pabui7l4w9C2RQcY6Y5ezgjR8y637b5U4QCXo7FJmrbzIl9Uy3umS6Isrse6afQrFfyVc_S5aLrfNhCWe95L-G_JoU5nIJ6acjjkLy2LHU1tYxsj38mg6hGBfGmBpRNse60r59mUhtNA8Et2Zb-Jgoo', start_index=19377)
Annotation(end_index=19873, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECG84Lib719XhJkrEigK3jjzyCPgP2FX5h87cSoz5P7XP64HRaOfk_Gc0pV2yBLomV8PBAOhyvvA6YKavI2v8lCNHzgwUSdSOWvSQ7KUVDWQd_frkbRp8enDIn6AhFfGamWIF_5d0=', start_index=19859)
Annotation(end_index=19873, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaeaVEUZOjEFcddep5fcXBtd-Eyl6eqCUGU7uSrIplevcUb64rd1CO1lUC0n3TFuelFmD-fH0ES0OqzZWTcsqIhQPMXNRFBVohpiitO5e9yVUSBvVVZ3njppi4s5U=', start_index=19859)
Annotation(end_index=20236, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAANVLuvVY9IMIMvOPlw9uRY7VEseigHXgK-KlATvFjBTIXUPK6gs6krVyAv3JfiwrAFE8M309aPaHRyyAPP0qeCi62Nis7scoulVOgPCXbrT9l0kH5BQDd04wJGlyLQH1yVjvUM-RKjDg9UThhJhw4bQ895OfIJSeOUzC0iDLeY21hldmruV4b2cZEvoEQhhRDhlAMHCishr2cyartUM8iYwLBxrcKU1OEFisP1E=', start_index=20222)
Annotation(end_index=20236, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGST7Ftnp0woaGkcXvW55H9xf7wypMH2EB08Pf6N5mzYMUuI-GLWJk_FvoSd-RELqr01PHo1XGSfkxFwcVwFCPKloQqb5u7mgd0QHsiiL1DIu51-eHHWvxl3EFucDJazLNeebT3FA=', start_index=20222)
Annotation(end_index=20631, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8juMmzvxcRW3zKctE-KYBUZoetMobjcXci-S-GT65c4N3XiVXIx0LxO2xSWrrKEpl4uzB59HH947fjhVU5mMHkPUZYy-LYfxxyZbF7S47RR_BYH0uPziTVX2b', start_index=20622)
Annotation(end_index=20819, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEQ-N7_YdRmurYzzL_xTomfZmj0W-qFUKh0yY6U9j6SlAAInKBjlAgxWQ47zLplNi92Lt2GXYjWxjZq4zN52BM-BQOpu7sD7N1_SdtH5aA-Ww_o2iYTmgxpagfNl9ZUAbnJK3Z1nEpCtr9VNZIcy_x2L0OhZSo48iRCwY5QaV-Sb0QW8Ah26ZqWA8JmXAI5bGitegIEOpr-Qn-7eD0br48S5dPYH58b3Wl5Knob6DO1LA5uszMXw1Zbx58THTMSDXdVhMzsCg=', start_index=20810)
Annotation(end_index=21047, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5TNO7IURzvQiyIDbMRCTkpkqKaD65Y6hTDPFSwtkTi6B9tiu3rCFvLhW9sxihMct5vFN7jvO0-Hj2HeK8T-KMgC_69HYn0dcafbUDYUhohiltU95ohbZyoyvuPqvDu557pnU0hkwyhs_XO3sgcabKWZpTHIVUgWKCAzr4iihIrgDAlciTUJBV', start_index=21038)
Annotation(end_index=21240, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlRPxy8TzotLJBvK4ZAK3Tb7VZYj7huXu4mPt10cJnoay__WkJIfr7cjckBTkJV0OYoVKWZ0Ob7OpFufen00VIw-Ln-cmsN5a3bI5DI2eRwY7R3l6d7AkBzV4F9vdschvD_JinrEZ64dkhy2sVjCvGu9SHvaJcw7DZm7m_JPORuLP4M5exphsClc9ZnKJyXiuGY7kAP7XiPEWyZxKL', start_index=21227)
Annotation(end_index=21240, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTbZdjvTqxpk9MWL-S0TQWQJAC3yVLQidPg1qxhqvfb-n4v_HpHzPiNpQIyU9BuN_l4O2-xKdm0uL8zc74lbBvNeUTBA47bEEwq1Uk1lM6V7DLZAlzfXP4Zx0RFJWYB4RsG8RPni-hDmwY7x6DM1FU2a3TVm8H4QtJ', start_index=21227)
Annotation(end_index=21495, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECwjl1ey3JiDsba-5at3r1e7mjpLUz8CGTOb6IJw70WZ2geKSm9pyBtldj4W6Cdlqr02JFUNGfN98Yt7b8-_It6r7Pbr2QTMnr3-KdSNApafJNa-jHn1EEFVqWJ1bwUjqAuL2uS-KSt122ysRzobVrkllYi3vpIvFuD_v24TJ1QQf4FXy5ZBjnG7TERBj1yS0lvWk9vuKYVviAN2rbdPfYjwYqDKM9KC1Jd7K21ul8gbb4CmBzIrfUUUPqaa6LOtgB34imwQKVANhPCxyRWOm4pHg=', start_index=21485)
Annotation(end_index=21614, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyDgfaFpPHvKyIiAcG6nOoLRmk5OASPgLOLtpctSMlQABnFBJD0gEt1pRgoXjHaxsLMwA-7lAG5Tl7ec5NkxN3L8M6mF1nkV-01K5PAor3RCK-wUlgFUuL-7VaUNAzxALnA6inWmJuI87EBRiIQI4WS6PpnnEOFfpxFWDgO_Yayu8cPZ3iRAx4Gf6YspDYZ1WsXCK9zo9K4odaOGiDcIiF4jSIIf7B6NIZcjH7invl3qAupCeQBsaTBTuD2rHYv05g4KRt2GXOv0fSzepzH6dq4sEk4D2Cmv2aqWGlcj0OGs_b0krfm-eNjmDi9vzY4BgKErEB', start_index=21604)
Annotation(end_index=21768, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8FOu8WFWTptIX0aMxICl2dYip-_BmBLoPbDP88fyxwAa11cwIucg0rX2nKY2zRJoYXWSkqn0X1-EZtFRZjBtqmqVqP-mbxBBw2tpY9R7XEMDHu4pXpnjydm4_VbWxVmm-ApqXsDGg6VnN-UuENOC9wQ==', start_index=21758)
Annotation(end_index=21889, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFT1HgKdUCpA70AX988gaTMXzc12hfhdF3mqmlC5Hidmsy-zxqUyq5Owlv-XGVxkyAWxvU-HAoMZaN4w8SJzhRHb5m7M1UXB9k3NwKXofYg2L5FwegMGa_FWg_Gu6U0SBbZLDB0F_MXZr9ZK1kbJdGyQxaMo5AsU-rdh6mtN5x9hC4t5Y7XDFFJ7bwPP9CAawfwMsWqc1IhoAz1T3jQ2evZkvbBDfQnsds=', start_index=21879)
Annotation(end_index=21965, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENuwyL49y67qnXpq0LYZz4RkKKACCjQ3v182f0cSHsnbtcwJbH8Pabui7l4w9C2RQcY6Y5ezgjR8y637b5U4QCXo7FJmrbzIl9Uy3umS6Isrse6afQrFfyVc_S5aLrfNhCWe95L-G_JoU5nIJ6acjjkLy2LHU1tYxsj38mg6hGBfGmBpRNse60r59mUhtNA8Et2Zb-Jgoo', start_index=21956)
Annotation(end_index=22024, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8juMmzvxcRW3zKctE-KYBUZoetMobjcXci-S-GT65c4N3XiVXIx0LxO2xSWrrKEpl4uzB59HH947fjhVU5mMHkPUZYy-LYfxxyZbF7S47RR_BYH0uPziTVX2b', start_index=22015)
Annotation(end_index=22127, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgMLpOVGZ7QWWO2oOZ5CPHxpzpsOTlDgBt6uLXDzbZcdg5d989DjQdjP5KU09ZMRrLs2CfwPQNjamM7Gp3lVDvikr2vRaqT-jBw_iUqkomRu2S_7VCvKPMe6dsBQiizNLAIjoA6RpGN8xuaHTNEiUU6NNcChoCSJ8iobgBH3rZj-fMW-8=', start_index=22117)
Annotation(end_index=22185, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGST7Ftnp0woaGkcXvW55H9xf7wypMH2EB08Pf6N5mzYMUuI-GLWJk_FvoSd-RELqr01PHo1XGSfkxFwcVwFCPKloQqb5u7mgd0QHsiiL1DIu51-eHHWvxl3EFucDJazLNeebT3FA=', start_index=22175)
Annotation(end_index=22272, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeZTstPmz-MjrXNqOFQkikCd4srP6nYtiV1hx-yTFtfpuqqpTTjiimEBviikomIjE5fKHUX3xTavKpO1klyN7r8FPnH7SKHn6PU8hy-xf_EklSLcZLAJqLa5b34cIqw4BuKNgnBv3uHk5IZ5SfclqsRVZEVM-mpuULQREbz70DPqhfr8vjdzILE5eH', start_index=22262)
Annotation(end_index=22347, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTbZdjvTqxpk9MWL-S0TQWQJAC3yVLQidPg1qxhqvfb-n4v_HpHzPiNpQIyU9BuN_l4O2-xKdm0uL8zc74lbBvNeUTBA47bEEwq1Uk1lM6V7DLZAlzfXP4Zx0RFJWYB4RsG8RPni-hDmwY7x6DM1FU2a3TVm8H4QtJ', start_index=22337)
Annotation(end_index=22393, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlRPxy8TzotLJBvK4ZAK3Tb7VZYj7huXu4mPt10cJnoay__WkJIfr7cjckBTkJV0OYoVKWZ0Ob7OpFufen00VIw-Ln-cmsN5a3bI5DI2eRwY7R3l6d7AkBzV4F9vdschvD_JinrEZ64dkhy2sVjCvGu9SHvaJcw7DZm7m_JPORuLP4M5exphsClc9ZnKJyXiuGY7kAP7XiPEWyZxKL', start_index=22384)
Annotation(end_index=22440, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjoebZ4Bh0Ul1EbK0kJWKInyGsGHrXQRxd495Vm-edGtuLRFa16y4xOVsW-EcS7voAJLQyr1L2cMLG_wEfAuVqzHtmaNqb0JN47MP08xIU2cpkpnsisgB3gvA2', start_index=22430)
Annotation(end_index=22503, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERG4XWAhl1viZmnCZGZe40UEOJLTTOU7XENHqKyFcoZCnNA0YzRet9YyYBwOb7qZ5TOr2Ej-68r_Z_kGCsPvoKllKrQ-Tem4Vdaq7p01CA9I86c9Lk0lL-B_dNR_bd5shgFSlCqLhdKHLfX4lFU8cuLzNk-8eMw7XKFK3oMvnjFBJ1RmRurKcohUa1tJg3TTD4WABgw7uIVLx0Q1vlPOMHKUu1NDJ90fYmXWmGRdoXAFBE6N3B5E63r3RMHDDrpoE8sQW0HZWqAr7ucTuIJ_SFwx-MLokNrErfWdkhUnRWDB8YBevP', start_index=22493)
Annotation(end_index=22639, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5TNO7IURzvQiyIDbMRCTkpkqKaD65Y6hTDPFSwtkTi6B9tiu3rCFvLhW9sxihMct5vFN7jvO0-Hj2HeK8T-KMgC_69HYn0dcafbUDYUhohiltU95ohbZyoyvuPqvDu557pnU0hkwyhs_XO3sgcabKWZpTHIVUgWKCAzr4iihIrgDAlciTUJBV', start_index=22630)
Annotation(end_index=22683, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHZ5BQKnyjDbmR3sLWOBuHkfBy95KGpDW4aB2tRUyw0wzlCdZPxsHhVWjItnrUZLGEwCW6vcM5YvTSxRc1iK1gVGBOXRc6WzBzc5DW0EpR3WFMyh38', start_index=22674)
Annotation(end_index=22736, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhcKb1HMjivSV-UuqHFNDb1MpPw4acfvW_fLqhAo7lSa7NXFQN0OMJMqBUnWIJvIn8p-8PnA6SgCJNjbuEB4Bj5LlM2HE1LDz8P1PuTE30X6MAOuy7LRJre-yHy6IGD8izMbz7Q6I8aOjQRzUo7dwJkE6ePbA1Uythj1HiiRqkde5rHg==', start_index=22726)
Annotation(end_index=22804, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaeaVEUZOjEFcddep5fcXBtd-Eyl6eqCUGU7uSrIplevcUb64rd1CO1lUC0n3TFuelFmD-fH0ES0OqzZWTcsqIhQPMXNRFBVohpiitO5e9yVUSBvVVZ3njppi4s5U=', start_index=22794)
Annotation(end_index=22892, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAANVLuvVY9IMIMvOPlw9uRY7VEseigHXgK-KlATvFjBTIXUPK6gs6krVyAv3JfiwrAFE8M309aPaHRyyAPP0qeCi62Nis7scoulVOgPCXbrT9l0kH5BQDd04wJGlyLQH1yVjvUM-RKjDg9UThhJhw4bQ895OfIJSeOUzC0iDLeY21hldmruV4b2cZEvoEQhhRDhlAMHCishr2cyartUM8iYwLBxrcKU1OEFisP1E=', start_index=22882)
Annotation(end_index=23004, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECG84Lib719XhJkrEigK3jjzyCPgP2FX5h87cSoz5P7XP64HRaOfk_Gc0pV2yBLomV8PBAOhyvvA6YKavI2v8lCNHzgwUSdSOWvSQ7KUVDWQd_frkbRp8enDIn6AhFfGamWIF_5d0=', start_index=22994)
Annotation(end_index=23046, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEQ-N7_YdRmurYzzL_xTomfZmj0W-qFUKh0yY6U9j6SlAAInKBjlAgxWQ47zLplNi92Lt2GXYjWxjZq4zN52BM-BQOpu7sD7N1_SdtH5aA-Ww_o2iYTmgxpagfNl9ZUAbnJK3Z1nEpCtr9VNZIcy_x2L0OhZSo48iRCwY5QaV-Sb0QW8Ah26ZqWA8JmXAI5bGitegIEOpr-Qn-7eD0br48S5dPYH58b3Wl5Knob6DO1LA5uszMXw1Zbx58THTMSDXdVhMzsCg=', start_index=23037)
Annotation(end_index=23151, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGx-snX3H6pN35CNawEyabnTshulcZttI8w5FCrFoFEDMjPWnwxRma9cGLZJDx3cbA-tcjHnmmLFh0LC5hmQhpOkm2chHPaEq9gh7RjcNdeJMk3G87G_dGKqmqk0qir5hkdVsbSQqOVS-gfxFgCBBUaobzyYZznOeaaLdjIfNzlPXqiG3d01TvCJEb1ZgLiQ9ocyaP6kWYqDDW8sR99IhmrGjflgRv-DR53fSGvadYNbdOs2Zcb_7AlfaDtKu8oCqXcYKxO4KIrWaQUBk0VWODNIWMmfqCirgBxCJhauZjJ', start_index=23142)
Annotation(end_index=23251, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHafGlQxh6Bv0FEMkbMuISEA6zelvnz6cG-yg9nGu9wiAv2uJJk5CixBt_JI8mQuZym4pMJ4v6Cfa3Im7iBIqa6fl6Y07d3enruwQAVQ1ZSLoUrSoJhBiYsJzsoK7btvJd1VDb0j0R1YgeMi_6kkK8hKO8kT3MJm9kz-pzV2t9ThQzPNArIY-wUMbDsBUJAibRvlPgF-ZDE_Q==', start_index=23242)
Annotation(end_index=23311, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENuwyL49y67qnXpq0LYZz4RkKKACCjQ3v182f0cSHsnbtcwJbH8Pabui7l4w9C2RQcY6Y5ezgjR8y637b5U4QCXo7FJmrbzIl9Uy3umS6Isrse6afQrFfyVc_S5aLrfNhCWe95L-G_JoU5nIJ6acjjkLy2LHU1tYxsj38mg6hGBfGmBpRNse60r59mUhtNA8Et2Zb-Jgoo', start_index=23302)
Annotation(end_index=23371, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEelF5srdLYprRfM0x2TkS0QuAcA_4i-EAaHq654lpm2kb4xdsZuBxvYXOkfiB2tg7HdxxPfSjClzlnh2Bcoo5qAxZY_sWLSXuM6u4swS8nzC3s5pfPLc-1xigoMrbftFHBbRCEDEJ2nYsP6bxB-XkjThgwZ7vdEAvXTd74bMHCWTMy2c2WtzTKvaPgXRXLt_Ij865cllhfDEImWrRaTmx1zvy_KvEjjPe5MYe8E6LhsZFVozR7RT7R1BIATDMi2vBPHEw90_3_ZsSwJl0Jru4dlzllSA==', start_index=23361)
Annotation(end_index=23505, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8juMmzvxcRW3zKctE-KYBUZoetMobjcXci-S-GT65c4N3XiVXIx0LxO2xSWrrKEpl4uzB59HH947fjhVU5mMHkPUZYy-LYfxxyZbF7S47RR_BYH0uPziTVX2b', start_index=23496)
Annotation(end_index=23608, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0vNp_DZQi3DikCCt2wAN8zUjBStQMzEYjzKBwyJaQlpYxZHtU0C0kICRP6TBp098a2B2uCbmpBqicNEuj3SbE0S7Zm0JGoUzhrhflHfMGRkfZoI3Tpi9BEL47wz1z9si92OgTzy7zwikzzG2A_9BtHFEgZ_uejzL-Ilu0WPukMUzN7tOWB8VkF-63XVz4Z9DCbV-HDvGEjYw=', start_index=23598)
Annotation(end_index=23678, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5TNO7IURzvQiyIDbMRCTkpkqKaD65Y6hTDPFSwtkTi6B9tiu3rCFvLhW9sxihMct5vFN7jvO0-Hj2HeK8T-KMgC_69HYn0dcafbUDYUhohiltU95ohbZyoyvuPqvDu557pnU0hkwyhs_XO3sgcabKWZpTHIVUgWKCAzr4iihIrgDAlciTUJBV', start_index=23669)
Annotation(end_index=23737, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHZ5BQKnyjDbmR3sLWOBuHkfBy95KGpDW4aB2tRUyw0wzlCdZPxsHhVWjItnrUZLGEwCW6vcM5YvTSxRc1iK1gVGBOXRc6WzBzc5DW0EpR3WFMyh38', start_index=23728)
Annotation(end_index=23790, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyQeKy4u9jQJ8A_etzCfW6C7ZJ7GCYkmAopmtd8vcO6-LcH3cylpIBPjdVeSiue74KDPjNxsNaFwJOsUo_oujd7s3UTSyNwMrNHhhpCj3z5nPIjewU9imwrTs9S7ZzzBlJRjg3zA-ics6t1LZf7sw1ya3UxcdOJDhT578m0NAbLpuxsiEeklXVl5ypipg7DPkgw6elTbaNjG_QlCDj3zNCaa7DdLIgZROUBjlOcf6sdlHcIq1Nkd0YBx-K8OOFQA==', start_index=23780)

## Sources
