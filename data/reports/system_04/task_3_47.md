# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** c105ccc6 | **Time:** 336.89s | **Cost:** $1.41713
--------------------------------------------------------------------------------

# Spatial Clustering Characteristics and the Quality-Time Trade-off in Heuristic Path Planning

### Key Points
*   **Reduction of Search Space:** Spatial clustering significantly improves the time efficiency of heuristic path planning by abstracting complex environments into structured, weighted graphs. This reduces the number of redundant nodes algorithms like A* must evaluate, with specific implementations demonstrating runtime reductions of approximately 68% to 77% compared to traditional methods [cite: 1, 2].
*   **The Quality-Time Trade-off Curve:** There is a non-linear relationship between cluster granularity and solution quality. In dynamic scenarios like ride-sharing, an optimal cluster size (empirically found to be between 100 and 125 requests in specific high-density contexts) exists where computational latency is minimized without significantly degrading the matching rate (quality) [cite: 3].
*   **Algorithmic Synergy:** Integrating density-based clustering (e.g., DBSCAN) with heuristic search (e.g., A*, JPS) allows planners to account for obstacle distribution features, eliminating "blind" searching in large-scale maps. This synergy is particularly effective in environments with uneven obstacle densities, though it introduces a preprocessing overhead that must be balanced against search time savings [cite: 2].
*   **Total Execution Time Optimization:** In multi-point robotic manipulation, the objective function shifts from solely minimizing path length to minimizing the sum of planning and execution time. Spatial clustering facilitates this by generating locally optimal sequences quickly, preventing the planning phase from dominating the total operation time [cite: 4, 5].

---

## 1. Introduction

Heuristic path planning is a cornerstone of autonomous systems, governing the movement of entities ranging from mobile robots and autonomous vessels to digital packets and ride-sharing vehicles. The fundamental challenge in this domain is the **quality-time trade-off**: the tension between finding the optimal path (highest quality, lowest cost) and finding a solution within a feasible timeframe (computational efficiency). As environments scale in size and complexity, traditional heuristic searches such as A* or Dijkstra’s algorithm often suffer from exponential increases in search space, leading to unacceptable latencies.

Spatial clustering characteristics—the density, distribution, shape, and connectivity of spatial objects—play a pivotal role in mediating this trade-off. By grouping spatial data into meaningful clusters, algorithms can transition from processing raw, high-resolution grids to navigating abstract, topological representations. This report provides an exhaustive analysis of how spatial clustering modifies the performance landscape of heuristic path planning. It examines the theoretical underpinnings of clustering-enhanced search, analyzes empirical results across robotic and logistical domains, and details the specific mechanisms by which clustering alters the balance between solution optimality and computational speed.

## 2. Theoretical Foundations of Clustering in Path Planning

### 2.1 The Computational Bottleneck in Heuristic Search
Traditional heuristic algorithms operate by exploring a graph of nodes, estimating the cost to reach a goal state. In uniform grids or large-scale maps, the number of nodes can be vast. For instance, the A* algorithm, while complete and optimal, relies on a heuristic function that estimates the distance to the endpoint but typically ignores the *distributional features* of obstacles [cite: 2]. This leads to "blind" searching, where the algorithm explores a large number of redundant nodes in open spaces or gets trapped in local minima (concave obstacles) before finding a valid path.

### 2.2 Spatial Clustering as Dimensionality Reduction
Spatial clustering serves as a preprocessing or online abstraction layer that reduces the effective dimensionality of the search problem. By identifying regions of high object density (obstacles or demand points) and low density (free space), clustering algorithms transform the search space.
*   **DBSCAN (Density-Based Spatial Clustering of Applications with Noise):** This algorithm is particularly prevalent in path planning literature because it can discover clusters of arbitrary shapes and handle noise (outliers) without requiring a pre-specified number of clusters [cite: 6, 7].
*   **Hierarchical Clustering:** This approach builds a hierarchy of clusters, allowing path planning to occur at different resolutions—coarse planning at the global level and fine-grained planning within local clusters [cite: 8, 9].

### 2.3 Defining the Quality-Time Trade-off
In the context of this report, the "quality-time trade-off" is defined through two competing metrics:
1.  **Quality:** The optimality of the resulting path (shortest distance, lowest energy consumption, or highest shareability in ride-pooling) and the completeness of the solution (guarantee of finding a path if one exists).
2.  **Time:** The total latency, comprising **preprocessing time** (clustering and graph construction) and **search time** (pathfinding execution).

The integration of spatial clustering introduces a new variable: **Cluster Granularity**. Coarse clustering (large clusters) minimizes search time but risks oversimplifying the map, potentially blocking valid narrow passages (low quality). Fine clustering (small clusters) preserves map fidelity (high quality) but offers negligible computational savings.

## 3. Obstacle Clustering in Grid-Based Path Planning

### 3.1 Mechanism of Efficiency Improvement
Recent research has proposed integrating obstacle clustering analysis with graph search to address the inefficiencies of A* in large-scale maps. The core methodology involves using algorithms like DBSCAN to group obstacle grid nodes. Instead of treating every grid cell as a node, the planner identifies "effective edge points" or "central nodes" of these obstacle clusters to construct a weighted graph [cite: 1, 2].

This process fundamentally alters the search topology. By clustering obstacles, the algorithm can identify large navigable regions and connect them via a sparse graph. The search algorithm then propagates through this reduced graph rather than the dense grid.
*   **Reduction in Node Visits:** Simulation experiments indicate that the number of nodes calculated in the search process decreases significantly. For example, in environments with specific obstacle distributions, the proposed clustering-based algorithm required only **30.9 ms** to find a path, compared to **98.73 ms** for the standard A* algorithm [cite: 2].
*   **Runtime Statistics:** This represents a runtime that is approximately **31.3%** of the A* algorithm's time, illustrating a massive shift in the time variable of the trade-off equation [cite: 2].

### 3.2 Impact of Obstacle Distribution Characteristics
The effectiveness of clustering is heavily dependent on the spatial characteristics of the environment:
*   **Low Obstacle Density:** In large-scale maps with few, scattered obstacles, clustering algorithms perform exceptionally well. They quickly group the sparse obstacles, leaving vast "free space" nodes that can be traversed instantly in the abstract graph. The proposed algorithms demonstrate "excellent performance for large-scale maps with few obstacles" [cite: 1, 2].
*   **Complex/Maze-like Environments:** In partially closed spaces or mazes, the trade-off becomes more complex. While clustering still reduces node count, the overhead of the clustering process itself increases. Research notes that in maze-like maps, while the clustering-based search is faster than A* (runtime 22.7% of A*), it may be slower than highly optimized grid-search variants like Jump Point Search (JPS). In one comparison, the clustering approach was **4.2 times slower** than JPS due to the time consumed by map clustering in high-density node environments [cite: 2].

### 3.3 The Preprocessing Penalty
A critical component of the quality-time trade-off is the cost of generating the clusters. The time complexity of DBSCAN is generally $O(n \log n)$ with spatial indexing, but can degrade to $O(n^2)$ in worst-case scenarios [cite: 10]. If the environment is highly dynamic (obstacles moving frequently), the clustering must be recomputed, potentially negating the search time savings. Thus, spatial clustering is most beneficial when the **query-to-update ratio** is high—i.e., multiple paths are planned through a static or slowly changing environment [cite: 11].

## 4. Clustering in Dynamic Ride-Sharing and Logistics

In dynamic ride-sharing (DRS) and logistics, the "path" involves connecting multiple dynamic requests. Here, spatial clustering is used to decompose large-scale matching problems into smaller, tractable sub-problems.

### 4.1 Cluster Size and the "Sweet Spot"
The size of the spatial cluster is a determinant factor in the system's performance.
*   **Small Clusters:** If the space is divided into very small clusters, the computational time for matching within each cluster is negligible. However, the **quality** of the solution drops drastically because the system fails to identify matches between requests that are spatially close but separated by arbitrary cluster boundaries (the "boundary effect").
*   **Large Clusters:** Large clusters maximize the potential for high-quality matches (high shareability) but lead to exponential increases in computation time, potentially violating real-time constraints (e.g., a user waiting 30 seconds for a match).

Research utilizing hierarchical and k-means clustering for ride-sharing requests has quantified this trade-off. In simulations involving thousands of requests, an optimal cluster size was identified to be between **100 and 125 requests** [cite: 3].
*   **Empirical Evidence:** At 6 AM and 7 AM (lower density), cluster sizes of 100 and 125 balanced the Within-Cluster Sum of Squares (WSS) and Between-Cluster Sum of Squares (BSS). At peak times (8 AM, 9 AM), the optimal size shifted slightly to 125–150 [cite: 3, 12].
*   **Performance Impact:** Using this optimized clustering, algorithms could provide high-quality solutions in less than 2 minutes for large-scale problems that would otherwise take 216 minutes, reducing computation time by over 99% while maintaining solution quality within ~3.6% of the global optimum [cite: 3].

### 4.2 Spatial vs. Temporal vs. Shareability Clustering
The "characteristic" of the clustering is not limited to Euclidean distance.
*   **Spatial Clustering:** Groups requests based on origin/destination coordinates. While computationally fast, it often yields poor objective function values (lower quality) because it ignores time windows [cite: 3].
*   **Space-Time Clustering:** Incorporates temporal constraints. This improves quality but increases dimensionality.
*   **Shareability Clustering:** A more advanced heuristic that clusters requests based on a "shareability function" (likelihood of being paired). Research indicates that spatial clustering alone performs poorly compared to shareability-based clustering (objective function 4.04% worse), suggesting that for high-quality path planning in logistics, simple geographic clustering is insufficient [cite: 3].

## 5. Multi-Point Robotic Manipulation and TSP Variants

In robotic manufacturing (e.g., drilling, welding), the robot must visit many points. This is a Traveling Salesperson Problem (TSP) variant where the "path" is the sequence of operations.

### 5.1 Total Execution Time as the Metric
In online planning, the metric for success is **Total Execution Time = Planning Time + Movement Time**. Traditional optimal solvers (finding the absolute shortest path) may take minutes to run, which is unacceptable if the robot's movement only takes seconds.
*   **Clustering Strategy:** Algorithms use spatial clustering (e.g., k-NN or recursive bisection) to group waypoints. The solver optimizes the sequence *within* clusters and then connects the clusters [cite: 4, 5].
*   **Trade-off Results:** A greedy clustering-based algorithm demonstrated a **21.1% improvement** in total execution time compared to a base case. While the resulting physical path might be slightly longer than the theoretical optimum (lower quality in terms of distance), the drastic reduction in planning time (from minutes to fractions of a second) results in a superior *overall* system performance [cite: 4].
*   **Locally Optimal Sequences:** By accepting locally optimal sequences within clusters, the system balances the quality of the solution with the computational time. The algorithm runs in $O(N)$ time, making it scalable for real-time applications [cite: 4].

## 6. Maritime Path Planning and Trajectory Optimization

The maritime domain presents unique spatial characteristics due to unrestricted open waters combined with highly constrained port environments.

### 6.1 AIS Data and Density-Based Clustering
Path planning for autonomous ships utilizes Automatic Identification System (AIS) data to learn from historical traffic patterns.
*   **Methodology:** Algorithms employ DBSCAN to cluster trajectory endpoints and turning points. This filters out noise and identifies "high-density routes" that represent safe, navigable channels [cite: 13, 14].
*   **Performance Metrics:** An integrated model using DBSCAN and Siamese Neural Networks (SNN) for ship route planning demonstrated significant trade-off advantages:
    *   **Planning Time:** Reduced by **67.8%** (8.11s vs. 25.24s for genetic algorithms).
    *   **Quality:** Trajectory fitting improved by **21%** (cosine similarity 0.86 vs. 0.71).
    *   **Operational Efficiency:** Voyage deviation reduced by 36.8% and fuel consumption by 20.8% [cite: 13].
*   **Interpretation:** Here, spatial clustering improves *both* quality and time. By extracting the "wisdom of the crowd" from historical data via clustering, the heuristic search is guided toward high-probability navigable areas, avoiding the extensive exploration of invalid sea space.

## 7. Algorithmic Complexity and Scalability Analysis

The influence of spatial clustering on the quality-time trade-off is fundamentally rooted in algorithmic complexity.

### 7.1 Complexity Classes
*   **Grid Search (A*):** Complexity is roughly proportional to the number of grid cells $N$. In high-resolution maps, $N$ is massive.
*   **Clustering (DBSCAN):** Complexity is $O(N \log N)$ with indexing.
*   **Clustered Search:** Complexity becomes $O(N \log N) + O(C^2)$ or $O(C \log C)$, where $C$ is the number of clusters and $C \ll N$.

### 7.2 The Cross-Over Point
There exists a cross-over point where the cost of clustering exceeds the savings in search time.
*   **Small Maps/Low Complexity:** For simple maps, A* or JPS are sufficiently fast. Adding clustering introduces unnecessary overhead (calculating densities, centroids), degrading the time metric without improving quality [cite: 2].
*   **Large Maps/High Complexity:** As map scale increases, the $O(N)$ growth of A* outpaces the clustering overhead. The "impact of map scale on the time cost" is reduced, making clustering essential for scalability [cite: 1, 2].

### 7.3 Hierarchical and Multi-Resolution Approaches
To further optimize the trade-off, hierarchical methods (HDBSCAN, Hierarchical Reinforcement Learning) are employed. These methods create a pyramid of abstractions.
*   **Benefit:** They allow for "Anytime Planning"—the algorithm can quickly return a coarse path (low quality, fast time) and refine it if more computation time is available [cite: 15].
*   **Narrow Passages:** In sampling-based planning (e.g., RRT), density-based spatial clustering helps identify "narrow passages" (areas of low sampling probability but high importance). By clustering samples in these regions, the planner can bias its search to ensure connectivity, addressing a major quality failure mode of randomized planners [cite: 16].

## 8. Broader Context: Spatial Heterogeneity and Resource Allocation

While this report focuses on path planning, the principles of spatial clustering characteristics affecting trade-offs extend to static resource planning, reinforcing the theoretical validity of the findings.
*   **Spatial Autocorrelation:** In urban planning, high-quality resources (e.g., sports facilities, arable land) tend to cluster (High-High clusters). Ignoring this spatial heterogeneity leads to inefficient resource allocation (low quality) [cite: 17, 18].
*   **Trade-off Synergy:** Just as path planners must balance distance vs. time, ecosystem service planning uses bivariate local spatial autocorrelation (LISA) to identify regions where services (e.g., food production vs. soil retention) trade off or synergize. This spatial understanding allows for differentiated management strategies, analogous to how a robot might switch between "highway" navigation (sparse graph) and "cluttered" navigation (dense grid) based on local cluster characteristics [cite: 19, 20].

## 9. Conclusion

Spatial clustering characteristics fundamentally alter the quality-time trade-off in heuristic path planning by restructuring the search space. The impact is multifaceted:

1.  **Efficiency Gains:** In static obstacle environments, clustering reduces node redundancy, offering runtime reductions of over 30% compared to standard A*, provided the environment is sufficiently large to justify the preprocessing cost.
2.  **Parameter Sensitivity:** In dynamic matching problems (ride-sharing), the cluster size is a critical control parameter. A size range of 100–125 requests has been identified as a Pareto-optimal region for specific high-density scenarios, balancing computational latency with matching probability.
3.  **Total System Optimization:** For multi-point tasks, clustering shifts the focus from "shortest path" to "shortest time to completion," enabling real-time responsiveness in manufacturing and robotics.
4.  **Data-Driven Heuristics:** In maritime and complex navigation, clustering historical data (AIS) generates high-fidelity heuristics that improve both safety (quality) and planning speed simultaneously.

Future research in this domain is moving toward **adaptive clustering**, where the algorithm dynamically adjusts cluster sizes and shapes in real-time based on the observed density of obstacles or requests, ensuring the system remains at the optimal point of the quality-time curve regardless of environmental fluctuations.

---

### References
*   **[cite: 1]** Path Planning Algorithm Based on Obstacle Clustering Analysis and Graph Search (Source 1)
*   **[cite: 2]** Path Planning Algorithm Based on Obstacle Clustering Analysis and Graph Search (Source 2)
*   **[cite: 17]** A research on spatial configuration characteristics... (Source 10)
*   **[cite: 19]** Scale effects and time variation of trade-offs... (Source 11)
*   **[cite: 18]** Spatial autocorrelation of farmland quality... (Source 12)
*   **[cite: 20]** Quantification of ecosystem service trade-offs... (Source 15)
*   **[cite: 3]** Space-time clustering-based method to optimize shareability... (Source 16)
*   **[cite: 11]** Increasing the Efficiency of Lazy Theta*... (Source 19)
*   **[cite: 4]** Greedy Clustering-Based Algorithm for Improving Multi-point Robotic Manipulation Sequencing (Source 20)
*   **[cite: 16]** Using density-based spatial clustering... (Source 23)
*   **[cite: 3]** Space-time clustering-based method to optimize shareability... (Source 26)
*   **[cite: 6]** Clustering Spatial Data in the Presence of Obstacles (Source 27)
*   **[cite: 2]** Path Planning Algorithm Based on Obstacle Clustering... (Source 28)
*   **[cite: 8]** Space-Time Hierarchical Clustering... (Source 31)
*   **[cite: 9]** Spatial clustering algorithms comparison (Source 32)
*   **[cite: 10]** Clustering algorithms in Maritime ITS (Source 34)
*   **[cite: 20]** Quantification of ecosystem service trade-offs... (Source 37)
*   **[cite: 7]** A density-based spatial clustering approach... (Source 40)
*   **[cite: 2]** Path Planning Algorithm Based on Obstacle Clustering... (Source 52)
*   **[cite: 13]** AIS Data and DBSCAN-Based Ship Route Planning Model (Source 53)
*   **[cite: 5]** Greedy Clustering-Based Algorithm... (Source 58)
*   **[cite: 4]** Greedy Clustering-Based Algorithm... (Source 59)
*   **[cite: 15]** A Novel Clustering-Based Algorithm... (Source 61)
*   **[cite: 14]** Global Path Planning for Autonomous Ship Navigation... (Source 63)
*   **[cite: 3]** Space-time clustering-based method... (Source 71)
*   **[cite: 12]** Space-time clustering-based method... (Source 72)
*   **[cite: 2]** Path Planning Algorithm Based on Obstacle Clustering... (Source 81)

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHG_AkScy3JDY0TWV2fE93Fqdp7xTWOARsMj2ANEBPSnDMHdPxjTwp0v1OO_oXoCfRw5hBd7hYLaPuX0aSYeqc57KAT7fPMqJGRLhZjvC-Rx5nH6hL3MStDqHJLo_Nwlcqn9_kohYcdi9IHxWvnS8mVlFba2OlNzKaTh7xfIrmXyZ4SOb2RE3Vo2UBiAfl5sjAVYqVJ5C4yQGQriqSK-vdUjOCmJ0umrqZxjCWd09U3Of2wWuFwV8g2)
2. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_4WoAXd4leVOwQmCPPgsahV_9dahtwFqJFEzsfH84ViRwFesOTtYU2pJpo4PkKWu77BonZ8GIlxuQQZycH68r9ZggQ67EIOneWKxdVKVATUJQxu9nEuwYewbDPW5)
3. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRCR-zD6tftOf21IFLnaLhkPO_DBxZtZGkx1XlzzY3JHlQel2FPlSEiziY46JjBHJt53kBxfr4xGcX_CzMGfrqhZC3tXg-Mo3cW5Bt9igwjXVYUtFzyamVMvlmzdkakFcDioyQbUYdwXxs1-JwfpQVpH8sKOFqHUW_UV7HBiQe)
4. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGY2isWaD6nqZi--wIGM7-RT4yvWV8BapMCjSW88yeqBnWyobLb5OfYkhnsk3X71mS4n1ukkMmczJK01YPg3T5ifG3P3-K48TtwAvqqw6syrx0Wu7fj5g==)
5. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-mUko0UD8IHgzTpbnqVcBk6tN41IOtT-FQp28qNnk7LL7_TGejqhcW4zhJKis9VD5Q4IWNddgA7KicCNLDIxFarlH1Q7fSar21IqV4iFAIec0j86gIA==)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFe3Xis26pyJbGbCR4UOU_9-b80S2hAZB8wM5TxPM_gGgzYBfOqN0-kj5PFillKS9iTbWyHaokJ397RrT6Tl1MtmUVM1uSiyfnc9kGRCP2BI9Hu1_nhpXlkQepp6Jt9R75L9IZnl0MAeoi6JYy81jfpkhs4LQ09-8I02MuYqJeVUZVif_tw9T8Ckg2prhgTNzVAEOmOTOGTVkEV4IS)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5YR2UvbsDF0VZAO59-YWchBER4uX4HnS5arJm8VCA329wTqxbBcYWhFtLmB2bdcJeMGJ84gSnavazy1NqH10TeMLgpyl_6NV2deS-XudDwAyueaRaH6NEYD5T60Dt9pUsXQkCiMO-l3jKI-EaS_nmKtog9N8SX4Q4crmVTVQoSy09CfFmBd24ERG-zHSn3KdhdUkhcqofDuAYKG-xFKqRxWNNMXU7gkWr4bI5kKEp4hrmeSPU76NdYwFMSzzjAuKUFGzm2je2sxw70GfllvHOe8c2io87jbaZ1UYL99lvlA==)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtF9nBSupLhAKTV6bvvU7YvVSEZ4reTGSX-GMPAn-qnI5x4CAyBHG_BUmhra9qNKuPwTwyj8Nbq9lADmmJdh1dU4ApxMFYd-PBHgww0GQMQ8WwdVXXENACs1NAyQWf-TCdS5LloGnKqoknYCc4HWzpMlRTvDo4Q8-lJ3naS7cc7X8jYhe-UG23v7u4Oy7gpjXQjgwC_JnOuUhlcOAzzdr-fTUJCxbfmfjfBXNEe2v4BEqPBYNYu_9CH6U31Bsx3jkAtA==)
9. [warse.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsliUjcd9TlLmoIOrnmkhkn0WYQGoJEWt73NUPlOuDJ5604IaGL9mNL6_o4inC97yYsZpvYz9GAdxYemUuItQDrJyOtwh3tmSnxTvRqdaR5moUjzAWehshYYJywCi6fLwfbYOLIWNjwL-vTDNXP4i5v7qh)
10. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLeVA0Rsh2YHAGKQxhXdtJkyVxuAj1jw8fX-J_p5BMt26cedHTeLBVQ-GVfp6uQdGI1Aeaw1670Z8QyNKWiNm__EAgXTi8otrsMzOraXs0pTFlf9AV-ohScGT9etBG)
11. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6_iLuzUFnhQw0ImEvNRftlu-X1j6cKH65k7zima6KdqS-KfVktrtbRqgBjBI7eyykWs99gqdmn8AxWbeiVcmobwEc7pZ_X7p4viH_g3ydF6K2vUWG7sjcU-Et0sM=)
12. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMnRZxueAQ6f1aMnycqUwA319lvrIjCYAJtIncecPYOMgg4W2r2lK-CFDFts_Rd1to_w3-dXAhHdCIqDTJ_Ul1cQk8bg2sjaf_gLvkbLCFAH933iX5VpLWFZgD99sWQUU-HXUEx9Bc)
13. [informatica.si](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5Jrbe-90JEoqSek4TBNV7t3SQfoLd8vzc2B1HPg4hn6YIEEk-vcSrD2sBGWWXmophXf0M7_T0he0dis3LUfI0t5WHGpMvTJLrwMus9c_zITCogJymS9Dc1vGNsTCpNnVQ4gzGHlO8QEVm98v7ROmgO48EhRTqcj9RjqT00A==)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVxpWz1WrcW-cGWo2WO05uaUHXHvh4x0RXKm8Ka0vbJsz3YeSDfOhlKWQ6I_6UAYztMSw35X9iZ4MCoRzKyETotqVcyqZYUHm7WUhbMGgfdG1iI3cXEnTNaJPBo4t9MNB_2FsW-uoVC3iDxcDSFWfzcGmZyzDnyAkxr8npLTpWmTRxMNow4oDVmapmGi3CsK3nro5aKpi5bueO3BcH3qe6JT9rXgR-Ebx3yF0vMGKXlTVjk4rPXvUPkjBk9qmR_2BYRToGOJz9I4mYBiRUM4cOx5K_09mK6_M9ZLYC)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHB_0gYToHpOTCz1zC4RX8q_I12k01EUFwbyo56NRktKZ8qQBNMMhM9mBJENOVehtfs1SlRF1CDyLA5KnKXyTEufbnovcH2S1s4720f7-ghJWZNKizkhajcRMaAGrhw2rLDW7YCLTxCjzI5mffzBXrsR49YJUzyaowcJx2a5JIv6hGjKiLHDPmUjE-iRT3YF4RNkQzBwIbVMcLMAUs8VtlJNkpd3Yqiq4OmjwM-vaKUC68gRgNObi3Iqt8wavrqBVZc8a5hWN6ma6d0aGN1O6U=)
16. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHU8SZCPezplue3E_6eyDjl4Xxr_TyKMSiyxReIs0Wt7mKsdcuFOzt1y4HnXnRkT21UofLlTlHfuxTfa0d6YzT10zBpZdqlP72J-hkLC2zVFIxWDH8IenfhJg==)
17. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKkcmDlsWucZ7han8vdSt9NyiohmHypolqIejrkrjw5LUk8-Gxur-51Dde1vzJ4sh5HFJyUd14Iq5xRGk3MLQfVxvhUPZw-lZYyKhii-XW6rsyviKZX8ELWU_I_ecj814zRFCSnH9TGFiYoQ48rI8HCrJx0L1eNDrBofZEbWbF)
18. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJBHGUOdgnTwq8Wb1MxSW_4ui0ltE6ht_rXoPhUpvo2AgUbm9PNYcNBOcIwUlWxL5DOen-G98Zqgh1kEWF9Tg-UfxjK6Y7w9YF61xEI6CrEfE9TDVFYhmEe34Jm14GLA0BJ5Cxa2Ht5SrhDimg-IAnPXTPlAXBfJL-ZJq55ZU6P-WBJjrbp3wvWpquoQ4reMNZV27T51uXjWc=)
19. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFayWGDloIEhpHdCrFiH1djddAp5BNf3cFPuqSvQbRJBQNunBDQRf_JIZILPAIFSc_exFgkT7HuWoDW9-uV3fWoEnWmEW65Yn7J9DRPbsRDGafHTM1sd9qMhpl9he7Z)
20. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtWAWSkuyB03oKukiCBYl_bA2kbbpNtB9Dsfs5L0W80JVPVP_F8j27QbKOnfG2QPSoiH7fUe7xHV1wmWv5tJ0Ku13eV9GXivwXdA7ZVVI2CORqYAT7spjlK_g0sSWAJyJ4-hyDVEhjjZE9aZK9z7esqnim0jBTGFg=)


## Annotations
Annotation(end_index=517, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_4WoAXd4leVOwQmCPPgsahV_9dahtwFqJFEzsfH84ViRwFesOTtYU2pJpo4PkKWu77BonZ8GIlxuQQZycH68r9ZggQ67EIOneWKxdVKVATUJQxu9nEuwYewbDPW5', start_index=505)
Annotation(end_index=517, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHG_AkScy3JDY0TWV2fE93Fqdp7xTWOARsMj2ANEBPSnDMHdPxjTwp0v1OO_oXoCfRw5hBd7hYLaPuX0aSYeqc57KAT7fPMqJGRLhZjvC-Rx5nH6hL3MStDqHJLo_Nwlcqn9_kohYcdi9IHxWvnS8mVlFba2OlNzKaTh7xfIrmXyZ4SOb2RE3Vo2UBiAfl5sjAVYqVJ5C4yQGQriqSK-vdUjOCmJ0umrqZxjCWd09U3Of2wWuFwV8g2', start_index=505)
Annotation(end_index=916, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRCR-zD6tftOf21IFLnaLhkPO_DBxZtZGkx1XlzzY3JHlQel2FPlSEiziY46JjBHJt53kBxfr4xGcX_CzMGfrqhZC3tXg-Mo3cW5Bt9igwjXVYUtFzyamVMvlmzdkakFcDioyQbUYdwXxs1-JwfpQVpH8sKOFqHUW_UV7HBiQe', start_index=907)
Annotation(end_index=1343, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_4WoAXd4leVOwQmCPPgsahV_9dahtwFqJFEzsfH84ViRwFesOTtYU2pJpo4PkKWu77BonZ8GIlxuQQZycH68r9ZggQ67EIOneWKxdVKVATUJQxu9nEuwYewbDPW5', start_index=1334)
Annotation(end_index=1712, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGY2isWaD6nqZi--wIGM7-RT4yvWV8BapMCjSW88yeqBnWyobLb5OfYkhnsk3X71mS4n1ukkMmczJK01YPg3T5ifG3P3-K48TtwAvqqw6syrx0Wu7fj5g==', start_index=1700)
Annotation(end_index=1712, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-mUko0UD8IHgzTpbnqVcBk6tN41IOtT-FQp28qNnk7LL7_TGejqhcW4zhJKis9VD5Q4IWNddgA7KicCNLDIxFarlH1Q7fSar21IqV4iFAIec0j86gIA==', start_index=1700)
Annotation(end_index=3619, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_4WoAXd4leVOwQmCPPgsahV_9dahtwFqJFEzsfH84ViRwFesOTtYU2pJpo4PkKWu77BonZ8GIlxuQQZycH68r9ZggQ67EIOneWKxdVKVATUJQxu9nEuwYewbDPW5', start_index=3610)
Annotation(end_index=4455, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFe3Xis26pyJbGbCR4UOU_9-b80S2hAZB8wM5TxPM_gGgzYBfOqN0-kj5PFillKS9iTbWyHaokJ397RrT6Tl1MtmUVM1uSiyfnc9kGRCP2BI9Hu1_nhpXlkQepp6Jt9R75L9IZnl0MAeoi6JYy81jfpkhs4LQ09-8I02MuYqJeVUZVif_tw9T8Ckg2prhgTNzVAEOmOTOGTVkEV4IS', start_index=4443)
Annotation(end_index=4455, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5YR2UvbsDF0VZAO59-YWchBER4uX4HnS5arJm8VCA329wTqxbBcYWhFtLmB2bdcJeMGJ84gSnavazy1NqH10TeMLgpyl_6NV2deS-XudDwAyueaRaH6NEYD5T60Dt9pUsXQkCiMO-l3jKI-EaS_nmKtog9N8SX4Q4crmVTVQoSy09CfFmBd24ERG-zHSn3KdhdUkhcqofDuAYKG-xFKqRxWNNMXU7gkWr4bI5kKEp4hrmeSPU76NdYwFMSzzjAuKUFGzm2je2sxw70GfllvHOe8c2io87jbaZ1UYL99lvlA==', start_index=4443)
Annotation(end_index=4691, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtF9nBSupLhAKTV6bvvU7YvVSEZ4reTGSX-GMPAn-qnI5x4CAyBHG_BUmhra9qNKuPwTwyj8Nbq9lADmmJdh1dU4ApxMFYd-PBHgww0GQMQ8WwdVXXENACs1NAyQWf-TCdS5LloGnKqoknYCc4HWzpMlRTvDo4Q8-lJ3naS7cc7X8jYhe-UG23v7u4Oy7gpjXQjgwC_JnOuUhlcOAzzdr-fTUJCxbfmfjfBXNEe2v4BEqPBYNYu_9CH6U31Bsx3jkAtA==', start_index=4679)
Annotation(end_index=4691, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsliUjcd9TlLmoIOrnmkhkn0WYQGoJEWt73NUPlOuDJ5604IaGL9mNL6_o4inC97yYsZpvYz9GAdxYemUuItQDrJyOtwh3tmSnxTvRqdaR5moUjzAWehshYYJywCi6fLwfbYOLIWNjwL-vTDNXP4i5v7qh', start_index=4679)
Annotation(end_index=6085, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_4WoAXd4leVOwQmCPPgsahV_9dahtwFqJFEzsfH84ViRwFesOTtYU2pJpo4PkKWu77BonZ8GIlxuQQZycH68r9ZggQ67EIOneWKxdVKVATUJQxu9nEuwYewbDPW5', start_index=6073)
Annotation(end_index=6085, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHG_AkScy3JDY0TWV2fE93Fqdp7xTWOARsMj2ANEBPSnDMHdPxjTwp0v1OO_oXoCfRw5hBd7hYLaPuX0aSYeqc57KAT7fPMqJGRLhZjvC-Rx5nH6hL3MStDqHJLo_Nwlcqn9_kohYcdi9IHxWvnS8mVlFba2OlNzKaTh7xfIrmXyZ4SOb2RE3Vo2UBiAfl5sjAVYqVJ5C4yQGQriqSK-vdUjOCmJ0umrqZxjCWd09U3Of2wWuFwV8g2', start_index=6073)
Annotation(end_index=6710, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_4WoAXd4leVOwQmCPPgsahV_9dahtwFqJFEzsfH84ViRwFesOTtYU2pJpo4PkKWu77BonZ8GIlxuQQZycH68r9ZggQ67EIOneWKxdVKVATUJQxu9nEuwYewbDPW5', start_index=6701)
Annotation(end_index=6911, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_4WoAXd4leVOwQmCPPgsahV_9dahtwFqJFEzsfH84ViRwFesOTtYU2pJpo4PkKWu77BonZ8GIlxuQQZycH68r9ZggQ67EIOneWKxdVKVATUJQxu9nEuwYewbDPW5', start_index=6902)
Annotation(end_index=7445, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_4WoAXd4leVOwQmCPPgsahV_9dahtwFqJFEzsfH84ViRwFesOTtYU2pJpo4PkKWu77BonZ8GIlxuQQZycH68r9ZggQ67EIOneWKxdVKVATUJQxu9nEuwYewbDPW5', start_index=7433)
Annotation(end_index=7445, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHG_AkScy3JDY0TWV2fE93Fqdp7xTWOARsMj2ANEBPSnDMHdPxjTwp0v1OO_oXoCfRw5hBd7hYLaPuX0aSYeqc57KAT7fPMqJGRLhZjvC-Rx5nH6hL3MStDqHJLo_Nwlcqn9_kohYcdi9IHxWvnS8mVlFba2OlNzKaTh7xfIrmXyZ4SOb2RE3Vo2UBiAfl5sjAVYqVJ5C4yQGQriqSK-vdUjOCmJ0umrqZxjCWd09U3Of2wWuFwV8g2', start_index=7433)
Annotation(end_index=8027, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_4WoAXd4leVOwQmCPPgsahV_9dahtwFqJFEzsfH84ViRwFesOTtYU2pJpo4PkKWu77BonZ8GIlxuQQZycH68r9ZggQ67EIOneWKxdVKVATUJQxu9nEuwYewbDPW5', start_index=8018)
Annotation(end_index=8297, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLeVA0Rsh2YHAGKQxhXdtJkyVxuAj1jw8fX-J_p5BMt26cedHTeLBVQ-GVfp6uQdGI1Aeaw1670Z8QyNKWiNm__EAgXTi8otrsMzOraXs0pTFlf9AV-ohScGT9etBG', start_index=8287)
Annotation(end_index=8628, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6_iLuzUFnhQw0ImEvNRftlu-X1j6cKH65k7zima6KdqS-KfVktrtbRqgBjBI7eyykWs99gqdmn8AxWbeiVcmobwEc7pZ_X7p4viH_g3ydF6K2vUWG7sjcU-Et0sM=', start_index=8618)
Annotation(end_index=9895, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRCR-zD6tftOf21IFLnaLhkPO_DBxZtZGkx1XlzzY3JHlQel2FPlSEiziY46JjBHJt53kBxfr4xGcX_CzMGfrqhZC3tXg-Mo3cW5Bt9igwjXVYUtFzyamVMvlmzdkakFcDioyQbUYdwXxs1-JwfpQVpH8sKOFqHUW_UV7HBiQe', start_index=9886)
Annotation(end_index=10167, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRCR-zD6tftOf21IFLnaLhkPO_DBxZtZGkx1XlzzY3JHlQel2FPlSEiziY46JjBHJt53kBxfr4xGcX_CzMGfrqhZC3tXg-Mo3cW5Bt9igwjXVYUtFzyamVMvlmzdkakFcDioyQbUYdwXxs1-JwfpQVpH8sKOFqHUW_UV7HBiQe', start_index=10154)
Annotation(end_index=10167, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMnRZxueAQ6f1aMnycqUwA319lvrIjCYAJtIncecPYOMgg4W2r2lK-CFDFts_Rd1to_w3-dXAhHdCIqDTJ_Ul1cQk8bg2sjaf_gLvkbLCFAH933iX5VpLWFZgD99sWQUU-HXUEx9Bc', start_index=10154)
Annotation(end_index=10482, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRCR-zD6tftOf21IFLnaLhkPO_DBxZtZGkx1XlzzY3JHlQel2FPlSEiziY46JjBHJt53kBxfr4xGcX_CzMGfrqhZC3tXg-Mo3cW5Bt9igwjXVYUtFzyamVMvlmzdkakFcDioyQbUYdwXxs1-JwfpQVpH8sKOFqHUW_UV7HBiQe', start_index=10473)
Annotation(end_index=10836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRCR-zD6tftOf21IFLnaLhkPO_DBxZtZGkx1XlzzY3JHlQel2FPlSEiziY46JjBHJt53kBxfr4xGcX_CzMGfrqhZC3tXg-Mo3cW5Bt9igwjXVYUtFzyamVMvlmzdkakFcDioyQbUYdwXxs1-JwfpQVpH8sKOFqHUW_UV7HBiQe', start_index=10827)
Annotation(end_index=11359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRCR-zD6tftOf21IFLnaLhkPO_DBxZtZGkx1XlzzY3JHlQel2FPlSEiziY46JjBHJt53kBxfr4xGcX_CzMGfrqhZC3tXg-Mo3cW5Bt9igwjXVYUtFzyamVMvlmzdkakFcDioyQbUYdwXxs1-JwfpQVpH8sKOFqHUW_UV7HBiQe', start_index=11350)
Annotation(end_index=12125, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGY2isWaD6nqZi--wIGM7-RT4yvWV8BapMCjSW88yeqBnWyobLb5OfYkhnsk3X71mS4n1ukkMmczJK01YPg3T5ifG3P3-K48TtwAvqqw6syrx0Wu7fj5g==', start_index=12113)
Annotation(end_index=12125, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-mUko0UD8IHgzTpbnqVcBk6tN41IOtT-FQp28qNnk7LL7_TGejqhcW4zhJKis9VD5Q4IWNddgA7KicCNLDIxFarlH1Q7fSar21IqV4iFAIec0j86gIA==', start_index=12113)
Annotation(end_index=12541, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGY2isWaD6nqZi--wIGM7-RT4yvWV8BapMCjSW88yeqBnWyobLb5OfYkhnsk3X71mS4n1ukkMmczJK01YPg3T5ifG3P3-K48TtwAvqqw6syrx0Wu7fj5g==', start_index=12532)
Annotation(end_index=12801, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGY2isWaD6nqZi--wIGM7-RT4yvWV8BapMCjSW88yeqBnWyobLb5OfYkhnsk3X71mS4n1ukkMmczJK01YPg3T5ifG3P3-K48TtwAvqqw6syrx0Wu7fj5g==', start_index=12792)
Annotation(end_index=13395, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5Jrbe-90JEoqSek4TBNV7t3SQfoLd8vzc2B1HPg4hn6YIEEk-vcSrD2sBGWWXmophXf0M7_T0he0dis3LUfI0t5WHGpMvTJLrwMus9c_zITCogJymS9Dc1vGNsTCpNnVQ4gzGHlO8QEVm98v7ROmgO48EhRTqcj9RjqT00A==', start_index=13381)
Annotation(end_index=13395, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVxpWz1WrcW-cGWo2WO05uaUHXHvh4x0RXKm8Ka0vbJsz3YeSDfOhlKWQ6I_6UAYztMSw35X9iZ4MCoRzKyETotqVcyqZYUHm7WUhbMGgfdG1iI3cXEnTNaJPBo4t9MNB_2FsW-uoVC3iDxcDSFWfzcGmZyzDnyAkxr8npLTpWmTRxMNow4oDVmapmGi3CsK3nro5aKpi5bueO3BcH3qe6JT9rXgR-Ebx3yF0vMGKXlTVjk4rPXvUPkjBk9qmR_2BYRToGOJz9I4mYBiRUM4cOx5K_09mK6_M9ZLYC', start_index=13381)
Annotation(end_index=13860, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5Jrbe-90JEoqSek4TBNV7t3SQfoLd8vzc2B1HPg4hn6YIEEk-vcSrD2sBGWWXmophXf0M7_T0he0dis3LUfI0t5WHGpMvTJLrwMus9c_zITCogJymS9Dc1vGNsTCpNnVQ4gzGHlO8QEVm98v7ROmgO48EhRTqcj9RjqT00A==', start_index=13850)
Annotation(end_index=15055, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_4WoAXd4leVOwQmCPPgsahV_9dahtwFqJFEzsfH84ViRwFesOTtYU2pJpo4PkKWu77BonZ8GIlxuQQZycH68r9ZggQ67EIOneWKxdVKVATUJQxu9nEuwYewbDPW5', start_index=15046)
Annotation(end_index=15286, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_4WoAXd4leVOwQmCPPgsahV_9dahtwFqJFEzsfH84ViRwFesOTtYU2pJpo4PkKWu77BonZ8GIlxuQQZycH68r9ZggQ67EIOneWKxdVKVATUJQxu9nEuwYewbDPW5', start_index=15274)
Annotation(end_index=15286, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHG_AkScy3JDY0TWV2fE93Fqdp7xTWOARsMj2ANEBPSnDMHdPxjTwp0v1OO_oXoCfRw5hBd7hYLaPuX0aSYeqc57KAT7fPMqJGRLhZjvC-Rx5nH6hL3MStDqHJLo_Nwlcqn9_kohYcdi9IHxWvnS8mVlFba2OlNzKaTh7xfIrmXyZ4SOb2RE3Vo2UBiAfl5sjAVYqVJ5C4yQGQriqSK-vdUjOCmJ0umrqZxjCWd09U3Of2wWuFwV8g2', start_index=15274)
Annotation(end_index=15694, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHB_0gYToHpOTCz1zC4RX8q_I12k01EUFwbyo56NRktKZ8qQBNMMhM9mBJENOVehtfs1SlRF1CDyLA5KnKXyTEufbnovcH2S1s4720f7-ghJWZNKizkhajcRMaAGrhw2rLDW7YCLTxCjzI5mffzBXrsR49YJUzyaowcJx2a5JIv6hGjKiLHDPmUjE-iRT3YF4RNkQzBwIbVMcLMAUs8VtlJNkpd3Yqiq4OmjwM-vaKUC68gRgNObi3Iqt8wavrqBVZc8a5hWN6ma6d0aGN1O6U=', start_index=15684)
Annotation(end_index=16053, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHU8SZCPezplue3E_6eyDjl4Xxr_TyKMSiyxReIs0Wt7mKsdcuFOzt1y4HnXnRkT21UofLlTlHfuxTfa0d6YzT10zBpZdqlP72J-hkLC2zVFIxWDH8IenfhJg==', start_index=16043)
Annotation(end_index=16591, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJBHGUOdgnTwq8Wb1MxSW_4ui0ltE6ht_rXoPhUpvo2AgUbm9PNYcNBOcIwUlWxL5DOen-G98Zqgh1kEWF9Tg-UfxjK6Y7w9YF61xEI6CrEfE9TDVFYhmEe34Jm14GLA0BJ5Cxa2Ht5SrhDimg-IAnPXTPlAXBfJL-ZJq55ZU6P-WBJjrbp3wvWpquoQ4reMNZV27T51uXjWc=', start_index=16577)
Annotation(end_index=16591, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKkcmDlsWucZ7han8vdSt9NyiohmHypolqIejrkrjw5LUk8-Gxur-51Dde1vzJ4sh5HFJyUd14Iq5xRGk3MLQfVxvhUPZw-lZYyKhii-XW6rsyviKZX8ELWU_I_ecj814zRFCSnH9TGFiYoQ48rI8HCrJx0L1eNDrBofZEbWbF', start_index=16577)
Annotation(end_index=17106, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtWAWSkuyB03oKukiCBYl_bA2kbbpNtB9Dsfs5L0W80JVPVP_F8j27QbKOnfG2QPSoiH7fUe7xHV1wmWv5tJ0Ku13eV9GXivwXdA7ZVVI2CORqYAT7spjlK_g0sSWAJyJ4-hyDVEhjjZE9aZK9z7esqnim0jBTGFg=', start_index=17092)
Annotation(end_index=17106, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFayWGDloIEhpHdCrFiH1djddAp5BNf3cFPuqSvQbRJBQNunBDQRf_JIZILPAIFSc_exFgkT7HuWoDW9-uV3fWoEnWmEW65Yn7J9DRPbsRDGafHTM1sd9qMhpl9he7Z', start_index=17092)
Annotation(end_index=18619, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHG_AkScy3JDY0TWV2fE93Fqdp7xTWOARsMj2ANEBPSnDMHdPxjTwp0v1OO_oXoCfRw5hBd7hYLaPuX0aSYeqc57KAT7fPMqJGRLhZjvC-Rx5nH6hL3MStDqHJLo_Nwlcqn9_kohYcdi9IHxWvnS8mVlFba2OlNzKaTh7xfIrmXyZ4SOb2RE3Vo2UBiAfl5sjAVYqVJ5C4yQGQriqSK-vdUjOCmJ0umrqZxjCWd09U3Of2wWuFwV8g2', start_index=18610)
Annotation(end_index=18727, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_4WoAXd4leVOwQmCPPgsahV_9dahtwFqJFEzsfH84ViRwFesOTtYU2pJpo4PkKWu77BonZ8GIlxuQQZycH68r9ZggQ67EIOneWKxdVKVATUJQxu9nEuwYewbDPW5', start_index=18718)
Annotation(end_index=18836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKkcmDlsWucZ7han8vdSt9NyiohmHypolqIejrkrjw5LUk8-Gxur-51Dde1vzJ4sh5HFJyUd14Iq5xRGk3MLQfVxvhUPZw-lZYyKhii-XW6rsyviKZX8ELWU_I_ecj814zRFCSnH9TGFiYoQ48rI8HCrJx0L1eNDrBofZEbWbF', start_index=18826)
Annotation(end_index=18922, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFayWGDloIEhpHdCrFiH1djddAp5BNf3cFPuqSvQbRJBQNunBDQRf_JIZILPAIFSc_exFgkT7HuWoDW9-uV3fWoEnWmEW65Yn7J9DRPbsRDGafHTM1sd9qMhpl9he7Z', start_index=18912)
Annotation(end_index=19003, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJBHGUOdgnTwq8Wb1MxSW_4ui0ltE6ht_rXoPhUpvo2AgUbm9PNYcNBOcIwUlWxL5DOen-G98Zqgh1kEWF9Tg-UfxjK6Y7w9YF61xEI6CrEfE9TDVFYhmEe34Jm14GLA0BJ5Cxa2Ht5SrhDimg-IAnPXTPlAXBfJL-ZJq55ZU6P-WBJjrbp3wvWpquoQ4reMNZV27T51uXjWc=', start_index=18993)
Annotation(end_index=19081, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtWAWSkuyB03oKukiCBYl_bA2kbbpNtB9Dsfs5L0W80JVPVP_F8j27QbKOnfG2QPSoiH7fUe7xHV1wmWv5tJ0Ku13eV9GXivwXdA7ZVVI2CORqYAT7spjlK_g0sSWAJyJ4-hyDVEhjjZE9aZK9z7esqnim0jBTGFg=', start_index=19071)
Annotation(end_index=19161, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRCR-zD6tftOf21IFLnaLhkPO_DBxZtZGkx1XlzzY3JHlQel2FPlSEiziY46JjBHJt53kBxfr4xGcX_CzMGfrqhZC3tXg-Mo3cW5Bt9igwjXVYUtFzyamVMvlmzdkakFcDioyQbUYdwXxs1-JwfpQVpH8sKOFqHUW_UV7HBiQe', start_index=19152)
Annotation(end_index=19255, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6_iLuzUFnhQw0ImEvNRftlu-X1j6cKH65k7zima6KdqS-KfVktrtbRqgBjBI7eyykWs99gqdmn8AxWbeiVcmobwEc7pZ_X7p4viH_g3ydF6K2vUWG7sjcU-Et0sM=', start_index=19245)
Annotation(end_index=19329, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGY2isWaD6nqZi--wIGM7-RT4yvWV8BapMCjSW88yeqBnWyobLb5OfYkhnsk3X71mS4n1ukkMmczJK01YPg3T5ifG3P3-K48TtwAvqqw6syrx0Wu7fj5g==', start_index=19320)
Annotation(end_index=19452, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHU8SZCPezplue3E_6eyDjl4Xxr_TyKMSiyxReIs0Wt7mKsdcuFOzt1y4HnXnRkT21UofLlTlHfuxTfa0d6YzT10zBpZdqlP72J-hkLC2zVFIxWDH8IenfhJg==', start_index=19442)
Annotation(end_index=19524, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRCR-zD6tftOf21IFLnaLhkPO_DBxZtZGkx1XlzzY3JHlQel2FPlSEiziY46JjBHJt53kBxfr4xGcX_CzMGfrqhZC3tXg-Mo3cW5Bt9igwjXVYUtFzyamVMvlmzdkakFcDioyQbUYdwXxs1-JwfpQVpH8sKOFqHUW_UV7HBiQe', start_index=19515)
Annotation(end_index=19617, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFe3Xis26pyJbGbCR4UOU_9-b80S2hAZB8wM5TxPM_gGgzYBfOqN0-kj5PFillKS9iTbWyHaokJ397RrT6Tl1MtmUVM1uSiyfnc9kGRCP2BI9Hu1_nhpXlkQepp6Jt9R75L9IZnl0MAeoi6JYy81jfpkhs4LQ09-8I02MuYqJeVUZVif_tw9T8Ckg2prhgTNzVAEOmOTOGTVkEV4IS', start_index=19608)
Annotation(end_index=19700, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_4WoAXd4leVOwQmCPPgsahV_9dahtwFqJFEzsfH84ViRwFesOTtYU2pJpo4PkKWu77BonZ8GIlxuQQZycH68r9ZggQ67EIOneWKxdVKVATUJQxu9nEuwYewbDPW5', start_index=19691)
Annotation(end_index=19786, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtF9nBSupLhAKTV6bvvU7YvVSEZ4reTGSX-GMPAn-qnI5x4CAyBHG_BUmhra9qNKuPwTwyj8Nbq9lADmmJdh1dU4ApxMFYd-PBHgww0GQMQ8WwdVXXENACs1NAyQWf-TCdS5LloGnKqoknYCc4HWzpMlRTvDo4Q8-lJ3naS7cc7X8jYhe-UG23v7u4Oy7gpjXQjgwC_JnOuUhlcOAzzdr-fTUJCxbfmfjfBXNEe2v4BEqPBYNYu_9CH6U31Bsx3jkAtA==', start_index=19777)
Annotation(end_index=19854, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsliUjcd9TlLmoIOrnmkhkn0WYQGoJEWt73NUPlOuDJ5604IaGL9mNL6_o4inC97yYsZpvYz9GAdxYemUuItQDrJyOtwh3tmSnxTvRqdaR5moUjzAWehshYYJywCi6fLwfbYOLIWNjwL-vTDNXP4i5v7qh', start_index=19845)
Annotation(end_index=19926, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLeVA0Rsh2YHAGKQxhXdtJkyVxuAj1jw8fX-J_p5BMt26cedHTeLBVQ-GVfp6uQdGI1Aeaw1670Z8QyNKWiNm__EAgXTi8otrsMzOraXs0pTFlf9AV-ohScGT9etBG', start_index=19916)
Annotation(end_index=19995, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtWAWSkuyB03oKukiCBYl_bA2kbbpNtB9Dsfs5L0W80JVPVP_F8j27QbKOnfG2QPSoiH7fUe7xHV1wmWv5tJ0Ku13eV9GXivwXdA7ZVVI2CORqYAT7spjlK_g0sSWAJyJ4-hyDVEhjjZE9aZK9z7esqnim0jBTGFg=', start_index=19985)
Annotation(end_index=20075, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5YR2UvbsDF0VZAO59-YWchBER4uX4HnS5arJm8VCA329wTqxbBcYWhFtLmB2bdcJeMGJ84gSnavazy1NqH10TeMLgpyl_6NV2deS-XudDwAyueaRaH6NEYD5T60Dt9pUsXQkCiMO-l3jKI-EaS_nmKtog9N8SX4Q4crmVTVQoSy09CfFmBd24ERG-zHSn3KdhdUkhcqofDuAYKG-xFKqRxWNNMXU7gkWr4bI5kKEp4hrmeSPU76NdYwFMSzzjAuKUFGzm2je2sxw70GfllvHOe8c2io87jbaZ1UYL99lvlA==', start_index=20066)
Annotation(end_index=20152, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_4WoAXd4leVOwQmCPPgsahV_9dahtwFqJFEzsfH84ViRwFesOTtYU2pJpo4PkKWu77BonZ8GIlxuQQZycH68r9ZggQ67EIOneWKxdVKVATUJQxu9nEuwYewbDPW5', start_index=20143)
Annotation(end_index=20239, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5Jrbe-90JEoqSek4TBNV7t3SQfoLd8vzc2B1HPg4hn6YIEEk-vcSrD2sBGWWXmophXf0M7_T0he0dis3LUfI0t5WHGpMvTJLrwMus9c_zITCogJymS9Dc1vGNsTCpNnVQ4gzGHlO8QEVm98v7ROmgO48EhRTqcj9RjqT00A==', start_index=20229)
Annotation(end_index=20321, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-mUko0UD8IHgzTpbnqVcBk6tN41IOtT-FQp28qNnk7LL7_TGejqhcW4zhJKis9VD5Q4IWNddgA7KicCNLDIxFarlH1Q7fSar21IqV4iFAIec0j86gIA==', start_index=20312)
Annotation(end_index=20388, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGY2isWaD6nqZi--wIGM7-RT4yvWV8BapMCjSW88yeqBnWyobLb5OfYkhnsk3X71mS4n1ukkMmczJK01YPg3T5ifG3P3-K48TtwAvqqw6syrx0Wu7fj5g==', start_index=20379)
Annotation(end_index=20456, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHB_0gYToHpOTCz1zC4RX8q_I12k01EUFwbyo56NRktKZ8qQBNMMhM9mBJENOVehtfs1SlRF1CDyLA5KnKXyTEufbnovcH2S1s4720f7-ghJWZNKizkhajcRMaAGrhw2rLDW7YCLTxCjzI5mffzBXrsR49YJUzyaowcJx2a5JIv6hGjKiLHDPmUjE-iRT3YF4RNkQzBwIbVMcLMAUs8VtlJNkpd3Yqiq4OmjwM-vaKUC68gRgNObi3Iqt8wavrqBVZc8a5hWN6ma6d0aGN1O6U=', start_index=20446)
Annotation(end_index=20525, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVxpWz1WrcW-cGWo2WO05uaUHXHvh4x0RXKm8Ka0vbJsz3YeSDfOhlKWQ6I_6UAYztMSw35X9iZ4MCoRzKyETotqVcyqZYUHm7WUhbMGgfdG1iI3cXEnTNaJPBo4t9MNB_2FsW-uoVC3iDxcDSFWfzcGmZyzDnyAkxr8npLTpWmTRxMNow4oDVmapmGi3CsK3nro5aKpi5bueO3BcH3qe6JT9rXgR-Ebx3yF0vMGKXlTVjk4rPXvUPkjBk9qmR_2BYRToGOJz9I4mYBiRUM4cOx5K_09mK6_M9ZLYC', start_index=20515)
Annotation(end_index=20610, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRCR-zD6tftOf21IFLnaLhkPO_DBxZtZGkx1XlzzY3JHlQel2FPlSEiziY46JjBHJt53kBxfr4xGcX_CzMGfrqhZC3tXg-Mo3cW5Bt9igwjXVYUtFzyamVMvlmzdkakFcDioyQbUYdwXxs1-JwfpQVpH8sKOFqHUW_UV7HBiQe', start_index=20601)
Annotation(end_index=20679, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMnRZxueAQ6f1aMnycqUwA319lvrIjCYAJtIncecPYOMgg4W2r2lK-CFDFts_Rd1to_w3-dXAhHdCIqDTJ_Ul1cQk8bg2sjaf_gLvkbLCFAH933iX5VpLWFZgD99sWQUU-HXUEx9Bc', start_index=20669)
Annotation(end_index=20747, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_4WoAXd4leVOwQmCPPgsahV_9dahtwFqJFEzsfH84ViRwFesOTtYU2pJpo4PkKWu77BonZ8GIlxuQQZycH68r9ZggQ67EIOneWKxdVKVATUJQxu9nEuwYewbDPW5', start_index=20738)

## Sources
