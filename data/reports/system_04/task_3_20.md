# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 8da4f959 | **Time:** 448.37s | **Cost:** $2.06047
--------------------------------------------------------------------------------

# How the Random Walk Matrix of Migration Flows Impacts the Spectral Clustering Stability of Traditional Cultural Networks

### Key Points
*   **Mathematical Mechanism:** The random walk matrix ($P = D^{-1}A$) derived from migration flows serves as the diffusion operator in spectral clustering. The stability of the resulting clusters is mathematically determined by the **spectral gap** (the difference between the primary eigenvalues, specifically related to $\lambda_2$). A larger spectral gap generally indicates faster mixing and weaker cluster definition, while a smaller spectral gap (in the context of the normalized Laplacian) indicates strong, metastable communities.
*   **Impact of Migration Motives:** The impact on stability is bifurcated by the underlying drivers of migration. **Economic migration**, often diffusive and bridging, tends to increase the spectral gap, promoting cultural convergence and destabilizing traditional cluster boundaries. Conversely, **cultural homophily** (migration to culturally similar nodes) reinforces the block-diagonal structure of the matrix, deepening the "cuts" between communities and enhancing the stability of traditional cultural networks.
*   **System Fragility:** Recent econometric physics research identifies "system fragility" as the inverse of the spectral gap ($F = 1/\lambda_2$). In this framework, traditional cultural networks that are highly insular (low spectral gap) are structurally "fragile" in the sense that they are slow to equilibrate and prone to distinct phase separations, whereas highly connected migration networks are more robust but less culturally distinct.
*   **Algorithmic Stability:** Standard spectral clustering can be unstable under the "noise" of short-term migration fluctuations. Advanced methods, such as **Evolutionary Spectral Clustering** and **Parametrized Random Walk Diffusion**, smooth these transitions over time, allowing for the identification of stable cultural cores despite transient population flows.

---

## 1. Introduction

The intersection of network theory, migration studies, and cultural dynamics offers a rigorous framework for understanding how population movements reshape societal structures. At the heart of this analysis lies the **random walk matrix**, a mathematical construct that defines the probability of transition between nodes in a network. In the context of migration, this matrix encapsulates the flows of individuals between geographic or social locations. **Spectral clustering**, a powerful algorithmic technique that partitions graphs based on the eigenvalues of their associated matrices, relies heavily on the properties of this random walk to identify community structures.

The query addresses a complex dynamic: how the specific probabilistic structure of migration flows (encoded in the random walk matrix) influences the mathematical stability of detecting and maintaining **traditional cultural networks**. These networks, often characterized by kinship, lineage, and historical inertia, are subject to the dispersive or cohesive forces of migration.

This report synthesizes advanced spectral graph theory, the "Compositional Model" of migration economics, and recent findings in sociophysics to provide an exhaustive analysis of this interaction. It explores how the **spectral gap** serves as the critical mediator between migration flows and cultural stability, determining whether traditional networks dissolve into a global monoculture or crystallize into distinct, polarized clusters.

## 2. The Random Walk Matrix in Migration Modeling

To understand the impact on stability, one must first define how migration is mathematically formalized within the spectral framework.

### 2.1 Constructing the Transition Matrix
In a migration network $G = (V, E)$, the nodes $V$ represent locations (countries, regions, or cultural units) and the edges $E$ represent migration flows. The adjacency matrix $A$ captures the raw volume of flow, where $A_{ij}$ is the number of migrants moving from node $i$ to node $j$.

The **random walk matrix** (or transition matrix), denoted as $P$, is derived by row-normalizing the adjacency matrix using the degree matrix $D$ (where $D_{ii} = \sum_j A_{ij}$). Formally:
\[ P = D^{-1}A \]
The entry $P_{ij}$ represents the probability that a random walker (a migrant) starting at location $i$ will move to location $j$ in one time step [cite: 1, 2].

In traditional cultural networks, this matrix is rarely symmetric. Migration flows are often directed and unbalanced due to economic disparities or conflict. However, spectral clustering theory typically requires a symmetric matrix (or a reversible Markov chain) to guarantee real eigenvalues. This necessitates transformations, such as analyzing the **random walk Laplacian** or symmetrizing the matrix (e.g., considering $A + A^T$ or $M|M + MM|$ for digraphs) [cite: 3].

### 2.2 The Diffusion Geometry of Migration
The random walk matrix defines a **diffusion geometry** over the network. The probability distribution of a random walker at time $t$, denoted as $p_t$, evolves according to $p_t = p_0 P^t$ [cite: 1].
*   **Short-term flows ($t$ is small):** Capture local migration patterns and immediate neighbors.
*   **Long-term flows ($t \to \infty$):** Converge to the stationary distribution $\pi$, provided the graph is connected and non-bipartite.

In the context of cultural networks, the "diffusion distance" defined by this random walk is a more accurate metric of cultural proximity than simple geographic distance. Two regions are "close" if there is a high probability of a migrant transitioning between them, either directly or through a dense network of intermediaries [cite: 4, 5].

## 3. Spectral Clustering and Stability Theory

Spectral clustering partitions the network by utilizing the eigenvectors of matrices derived from $P$, typically the Laplacian $L$. The stability of these partitions is governed by the spectrum (eigenvalues) of the matrix.

### 3.1 The Spectral Gap and Clusterability
The performance and stability of spectral clustering are theoretically bounded by the **spectral gap**. For the normalized random walk Laplacian $L_{rw} = I - P$, the eigenvalues are $0 = \lambda_1 \le \lambda_2 \le \dots \le \lambda_n$.
*   **$\lambda_1 = 0$:** Corresponds to the stationary distribution (equilibrium).
*   **$\lambda_2$ (The Fiedler Value):** This is the critical value. It determines the **algebraic connectivity** of the graph.

A **large spectral gap** (a large difference between $\lambda_k$ and $\lambda_{k+1}$, or a $\lambda_2$ far from 0 in the unnormalized case) implies that the random walk mixes quickly; the graph is highly connected (an "expander graph"). Conversely, a **small $\lambda_2$** indicates that the random walk gets "trapped" in sub-regions for long periods before escaping. These "traps" correspond to stable clusters or communities [cite: 6, 7, 8].

### 3.2 Defining Stability in Cultural Networks
"Stability" in this context has two interpretations, both impacted by the random walk matrix:
1.  **Algorithmic Stability:** The robustness of the clustering result to perturbations (noise) in the migration data. If a few migrants change their destination, does the spectral clustering algorithm drastically alter the cultural boundaries? Research indicates that spectral clustering is stable provided the **eigengap** is sufficiently large relative to the perturbation [cite: 1, 9, 10].
2.  **Structural/Community Stability:** The persistence of the cultural communities themselves over time. Do the migration flows erode the distinction between cultures (merging clusters), or do they reinforce the boundaries (deepening the gap)? This is measured by the **metastability** of the random walk [cite: 4].

## 4. Impact of Migration Flows on Network Topology

The structure of the random walk matrix $P$ is determined by human decision-making. The "Compositional Model" of migration provides the behavioral logic that dictates whether $P$ promotes stability or instability.

### 4.1 The Compositional Model: Homophily vs. Economics
Migration decisions are driven by a mix of economic incentives and cultural preferences.
*   **Cultural Homophily (The "Cultural" Component):** Migrants prefer destinations with similar cultural norms, language, or kinship networks. This is the "compositional" effect where migrants carry values and sort themselves into compatible clusters [cite: 11].
    *   *Impact on Matrix:* This concentrates probability mass $P_{ij}$ within existing cultural blocks. It makes the matrix **block-diagonal**.
    *   *Impact on Stability:* This **decreases $\lambda_2$** (making it closer to 0), thereby **increasing the stability** of the clusters. The random walk stays within the "traditional cultural network," reinforcing the separation between groups. This leads to **cultural divergence** between clusters [cite: 12].

*   **Economic Maximization (The "Diffusion" Component):** Migrants move to where wages or safety are highest, regardless of cultural fit.
    *   *Impact on Matrix:* This introduces "bridge" edges between previously disconnected cultural blocks. It adds off-diagonal probability mass.
    *   *Impact on Stability:* This **increases $\lambda_2$** (widening the gap from 0), facilitating faster mixing. This **decreases the stability** of the traditional cultural boundaries, leading to **cultural convergence** or "universal mixing" [cite: 13, 14].

### 4.2 Asymmetry and Directed Flows
Migration is rarely symmetric. A flow from the Global South to the Global North, or from rural to urban areas, creates a directed graph.
*   **Irreducibility Issues:** In directed graphs, the random walk may not be irreducible (it may get stuck in "sink" nodes). This challenges standard spectral clustering [cite: 15].
*   **Hermitian Clustering:** To handle this, recent approaches use Hermitian matrix representations or symmetrized versions ($M|M + MM|$) to extract stable clusters from directed flows. These methods show that directed flows often reveal a hierarchical structure that undirected approximations miss [cite: 3].

## 5. The Mechanism of Stability: Spectral Gap and Fragility

Recent theoretical work, particularly by Kikuchi (2024-2025), establishes a direct physical link between the spectral properties of the migration/diffusion operator and the "fragility" of the socio-economic system.

### 5.1 Fragility as the Inverse of the Spectral Gap
Kikuchi defines **system fragility ($F$)** as the inverse of the spectral gap:
\[ F = \frac{1}{\lambda_2} \]
(Note: In the context of the diffusion operator $L = -\nu \nabla^2$, $\lambda_2$ represents the decay rate of the slowest mode) [cite: 16, 17].

*   **High Fragility (Small Gap):** A system with distinct, isolated cultural clusters (traditional networks) has a small $\lambda_2$. It is "fragile" because it equilibrates very slowly. Shocks or information do not propagate globally; they remain localized. However, the *clusters themselves* are stable and distinct.
*   **Low Fragility (Large Gap):** A system with high migration integration has a large $\lambda_2$. It equilibrates quickly (short half-life of shocks). The system is robust to cascading failures in some contexts, but the *traditional cultural distinctions* are unstable and prone to dissolving [cite: 7, 18].

### 5.2 Entropy and Early Warning Signals
The spectral gap also determines the rate of **entropy production** in the network. A declining spectral gap (increasing fragility) serves as an early warning signal of a phase transition—potentially a crisis or a radical restructuring of the network. In the context of cultural networks, a rapid change in migration flows that alters $\lambda_2$ can signal the impending collapse or consolidation of traditional cultural identities [cite: 16, 17].

## 6. Traditional Cultural Networks: Resistance and Adaptation

Traditional cultural networks, such as the *cieng* systems in South Sudan or indigenous networks in the Americas, rely on lineage and historical ties that are inherently resistant to random mixing.

### 6.1 The Role of "Bad Paths" and Noise
In spectral clustering, "good paths" are those that traverse high-probability transitions within a cluster. "Bad paths" traverse low-probability edges between clusters.
*   **Migration as Noise:** Unregulated or forced migration (e.g., refugee flows) introduces "noise" into the matrix—random connections that do not reflect deep cultural ties.
*   **Random Walk Smoothing:** Algorithms that utilize random walks (e.g., running the walk for $t$ steps) effectively filter out this noise. The random walk tends to settle into the "metastable" states (the true cultural cores) while transient migration flows wash out. This makes the spectral clustering of traditional networks **stable** against short-term migration fluctuations, provided the core lineage structures remain intact [cite: 4, 9, 19].

### 6.2 Assimilation vs. Separation
The "Compositional Model" predicts that if migration flows are driven by cultural selection (homophily), the spectral clustering will reveal **divergence**. The "home" and "host" countries move further apart in the spectral embedding, creating sharper cluster boundaries. This preserves the stability of the traditional network by reinforcing its isolation. Conversely, if assimilation occurs (diffusion of values), the random walk matrix becomes more uniform, $\lambda_2$ increases, and the spectral clustering becomes less stable (the distinction between clusters vanishes) [cite: 11].

## 7. Algorithmic Perspectives on Stability

How do we computationally ensure stability when analyzing these networks?

### 7.1 Evolutionary Spectral Clustering
For dynamic networks where migration flows change over time (temporal networks), standard spectral clustering on a snapshot-by-snapshot basis is unstable. **Evolutionary Spectral Clustering** introduces a temporal smoothness framework. It penalizes deviations from the previous timestep's clustering, effectively "smoothing" the eigenvectors over time. This allows the algorithm to track the "drift" of cultural communities without reacting to every minor fluctuation in migration flow [cite: 19, 20].

### 7.2 Parametrized Random Walk Diffusion
For directed and sparse migration networks, standard random walks may fail to cover the graph. **Parametrized Random Walk Diffusion Kernel Clustering (P-RWDKC)** and **Reluctant Backtracking** operators are used to enhance stability. These methods adjust the random walk to ensure it explores the local topology (the traditional network) thoroughly before exiting to the global network, thereby improving the detection of density-based cultural clusters [cite: 15, 21].

## 8. Case Studies and Empirical Evidence

### 8.1 US Migration and Regional Clusters
Studies on US county-to-county migration networks demonstrate that spectral clustering can identify "hubs" and stable regions. When network effects are included (migration flows), the spatial decay of influence is slower, and "hot spots" of amplification emerge. The spectral gap in these networks has been shown to correlate with economic stability; a rising spectral gap (faster mixing) indicated improving structural isolation and resilience in some periods, while consolidation in others increased fragility [cite: 5, 16, 18].

### 8.2 Refugee Flows and Dynamic Communities
In the analysis of international refugee networks, evolutionary spectral clustering was found to provide stable results despite the chaotic nature of displacement. The method could distinguish between short-term noise (temporary displacement) and long-term cluster drifts (permanent resettlement patterns), effectively mapping the reorganization of cultural communities under stress [cite: 19].

### 8.3 European Banking and Contagion
While financial rather than purely cultural, the European banking network provides a proxy for how "migration" (of capital/exposure) impacts stability. Research using the Navier-Stokes framework and spectral analysis showed that consolidation (merging of nodes) reduced the spectral gap $\lambda_2$ from 0.32 to 0.11, increasing system fragility by a factor of three. This mirrors the risk in cultural networks: as distinct local networks merge into a globalized whole, the system may become more robust to local shocks but more fragile to systemic collapse [cite: 16, 17].

## 9. Conclusion

The random walk matrix of migration flows acts as the fundamental operator determining the structural integrity of traditional cultural networks. Its impact on spectral clustering stability is governed by the **spectral gap ($\lambda_2$)**.

1.  **Homophilous Migration** (Cultural Selection) reinforces the block-diagonal structure of the matrix, **lowering the spectral gap**. This increases the **stability of the clusters** (making them easier to detect and more distinct) but increases the **fragility of the global system** (slowing down equilibration and information exchange).
2.  **Economic/Diffusive Migration** introduces cross-cluster edges, **increasing the spectral gap**. This reduces the distinctness of traditional networks, leading to **instability in clustering** (merging of communities) but potentially creating a more robust, rapidly mixing global system.

Therefore, the "stability" of a traditional cultural network under migration is not a binary state but a dynamic tension defined by the eigenvalues of its migration flow matrix. The preservation of traditional cultural identities in the face of migration mathematically requires migration flows that maintain a low spectral gap—flows that are either limited in volume or highly selective in their directionality.

## References

*   **[cite: 9]** Zhang, X., et al. (2025). *An improved spectral clustering algorithm based on random walk*. ResearchGate.
*   **[cite: 6]** *Fluctuations of random walks on graphs and their relation to spectral clustering*. arXiv:2204.06087.
*   **[cite: 15]** *Parametrized Random Walk Diffusion Kernel Clustering*. arXiv:2210.00310.
*   **[cite: 4]** *Random walk-based method for identifying phases in temporal networks*. PMC12238632.
*   **[cite: 22]** *Graph spectral embedding using the random walk Laplacian*. arXiv:2105.00987.
*   **[cite: 23]** *The role of migrants networks in explaining aggregate migration flows*. International Journal of Manpower.
*   **[cite: 11]** *A compositional model of migration and cultural change*. IZA Discussion Papers.
*   **[cite: 20]** *Persistent communities by eigenvector smoothing (PisCES)*. PNAS.
*   **[cite: 3]** *Spectral Clustering of Signed and Directed Graphs*. NeurIPS Proceedings.
*   **[cite: 1]** Macgregor, P., & Sun, H. (2022). *On Learning the Structure of Clusters in Graphs*. arXiv.
*   **[cite: 2]** *Extracting Spatial Information*. UCLA Math.
*   **[cite: 5]** *Diffusion Maps*. Oxford Statistics.
*   **[cite: 10]** *Improved analysis of spectral algorithm for clustering*. Optimization Letters.
*   **[cite: 7, 16]** Kikuchi, T. (2025). *Dynamic Spatial Treatment Effects and Network Fragility*. MPRA.
*   **[cite: 19]** *Dynamic Communities in Directed Networks: A Case Study of International Refugee*. ResearchGate.
*   **[cite: 21]** *Spectral community detection in sparse networks*. ResearchGate.
*   **[cite: 18]** *Network Fragility and Structural Evolution*. MPRA.
*   **[cite: 17]** *System Fragility and the Spectral Gap*. MPRA.

**Sources:**
1. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHr0OpgnDJFh_PULDQAquVBjHL1xXnVPd-8YdHWHKmCZVhSDou0Jv7fggNju9RDfs4bw2J6jwKeQCBR3HMEWaHIrhvS_tV7DOVQit6ULWk7ypZgXa47)
2. [ucla.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5jDe2PfnhhyWnOIkPnDkmxmh7bsyn_F_pKi54Eq-JFbI2CROlrJKP0oj5YY_TL0tdJqWSE54_hyYKmSjMvI_j6n_Zul2kubAi8qvjpfofNc0wEjUJQXbb78k5qA733XcOHRLeN2bq0Rh4KrnTV-VsZxpdfI34hIs=)
3. [neurips.cc](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVxYVI0kNkqMYYd2EWY_kMUAxkp7vur8kkuI_FtvyOKmu18UZCCnxkARgZvPNzNp6sUyU_Lt6uq2xfsrh_bdgcpOBU7Ff-5WAKiHtvi5cymkEBzzCMsyiXvHSfGKzHaKAdTlziyBIor1pOB-avSuMWagiNWW7MWWlgVO_-4csnQkRTPXJxr-1VxNd3D2Oxx9-BCKg0NpKt0sAd)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyw1Q-S_ZlclD-dHXr01r_bS1EP7olN36fl4AkQwIDKkNiu3cz7lForzaBkH9gQoAqTouJMsIiSnHl1xDzRwoGqATr7fQO_J5WXG0WRSWSqpOAu9AYDlXLHOMfHtveY5_RV6S3hqOt)
5. [ox.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDz6QOVCur2kZE5eM9jWz398GlBUhZC7vtDUBK6a3wr0ZDqmFNpPQ09MCE__PE-SJQ_QZ68-kxehPjqxsGwSt70bjtEGhMfHQYuG_lWgwja0tLGuzQjw03px_4FCp1nxifXWImlfw8pVRBn1eVlSA=)
6. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmn63FYB_4DSFSBZlpshl29lLPMRLU5VQ3ZRjsT_5s07-CM2O_USDqkAOFkgepd29NnrftpfQyqmUA5xF09SU_zSY8tz41wSmxUdH9GTJdpdnpVX6P)
7. [uni-muenchen.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqKgCkVcidsD5avgiJLrLQnkEVY7aAiuYNhYQ9dhjg6ugAnZBuPFqvC52hzAS_LRjXG2pZX5OyYtAUTL2TEmx5ktcVNuM_T7Amwfni4x1c19SehnTYM-qNeqZSTWxqBaO4GCXzgsQzB3E3zRLLk3zY3xxr)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkz-SVQxST16Tmq6SjveEi-5KSknN5-k7NW1bzjd1v8ZP7-f_5j-4fFqF_7job96htlJcB1LFjqtHbzZB90R4wG1VY_J-b6kkLr24-xrmgSrLUzQgHRftRWbU8h76fDKAD8LHPyMw=)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmf2bJwpLpvSOySYpY-iQkWKFJ060F2pR5QF8zxYdsowbKZ7dyjxmo3g8PCTGs9HtciMuDuHuVG3dgQhZ6NG0xl9m5_GbtRTbpGBMAmGKfOMYr0pT9IBaVXbxaERVQwY97faBcrDNqfdkLmesEC9e0nvhlGmoIV9QnQ1jDuhaXkrifB9vL2BAHchgOL5InX-jTp74apTdxDrvz3dOQ8rgqsv-PE3aV)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfIVHBuKYZXnl--iwbL94JVgJrRHBNyHDjnfod4NDJMMKFma1LMeNJOymsuYtM5SnE8PCK86PzxnN8M6erP2i4MdZ6Mf88nt-dChgnaNh7-UT78BY0R3Y-cVPE2obTuxvvaEseD8nWvhkJMW3TZQ7X_2GUGUo55cdqZEuhqpWSepC3vs4gmWwovAFivtDoKbMaC35bXjijGGvohJNCJg==)
11. [iza.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQED7kSgF10M4T2Pw3hni0fwFSFN3mEk-9zY0iEjeNcCmlD1-gwelGxbHVjPM1hCO_d0T6fiNMwDLwzTV_FBlNwI1iMhBQufYUj-88y8zvdM6kv3CDol)
12. [cepii.fr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKTl4ZObnDO6TNRJg_Wy1P-jQgulonlP5vogfmQGhigOx3rhI7KaSxeRksZmv1XCDYOZATaJzIWXyWjGUn8OedI4HlQwd7cUOKN7vf1qRN7bB42h2B-_BA7HeOwPOgk4J4mncKBsfn)
13. [aeaweb.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuj-u7-DgjsSaauFpt4DvDXXkS-ytayIORBeAoldoNxrxJrdCjiSmcHRI3ejV6hamvhyF1EMaen5yr2DcV4R1Qk_8ZPf7T94w6qqewntjEeYcaWp4IVb1SzDa9g6QcLvEbAQn9Z6wEuHQ2wZrB3KY6RS0=)
14. [cornell.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHllb8T1njEmviUdZOeEIAyaIqVbDFT8YNxaKDlAXCKZcZVrPzQovSh1K1TUoFhoIxPed640TKUzTtcbnNKcTlg1WQl9nMyKFLoACoAHMdSt2LeUvBewoJGi3nNLmo1KXCT3bMsSFR8nQ=)
15. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdl6yS_doLXLX0Ks65U7-vlcVCP26G5DQ1zweVG3-ghphGxJOodSez6NGN7Q-JSerXfQmh-UgK3blU6t_slZPYSkRglp17_FfWg0A5N5w5TaXaA-81)
16. [uni-muenchen.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFde8vkA6HhH1flXyDkUrp8Axh5UMFozE1p84nM9WgK97cVH9iNrnElmgHCn3_8_Lzcn54DHPdCOYTpbNQ_gzR6xNQrOFQicYDnMJK9ycP8sPu_7Q2PT1NT1wMI2v3_UuCSfBqm3rMQjH8aTXKW02S7Q5Ma)
17. [uni-muenchen.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3JtleuDrzfO1lFtm-PP0Gq5awFdrj50Rvn-RfwcApJkNnkqAdPxUq7KBsbLaprd-0s_mfa7FXKS2Fds2C3x1DR7uxeCMlq8gNfr25LtAkNR00zzyscaFe4ftTUtXXxgTpjyllzZsTXbuzzPuM1krlfGKY)
18. [uni-muenchen.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKeGBzxolUZRMMj_TNMv6WGGOx_3Xi9QC9vRgXl7c-oggmazOohfeWyA4DGrs1lXTx2xo5iQ7RQG7erJRIGw_Iiorn5HRCQqSi54mtRJ3uzlfGUG1S3gmjL5MtS_zQAghW6VIX0vBmtuw66ISZTzMhI8mF)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1eGZq7ENnTSuiWI0BVXTWadURnGFhTJjKtYuihzkMfhMgD7qSNruD6mdm60TNWN36Uvh4yPx3pwGd9AZu3zxwabkNWzvWB3qTQ3nQ5c2EDTgqJzA5IM54PTEj5vZhwTm4MUglSEhBMA7QvFaGmqs_DPTm0GINuzT9JbWdiw-qykLo4DnXC7wlaSQxd4eV-bd5LPsVZiQUzXNsNI3Vr5v00d4IL44d9ruKPBSDjV1G1LQ4ES7M0HQ=)
20. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEupyvsmOwrOMT5lPp7OcG9u1WvrI7O_TRTpyaaclg9DBwLMC6Tr6U6D8tqipHldJLonpsNVtZ_EFVCOjaCL2bJbvkU0qOH4x2U3ww1L1sdUAJwY_P33GQ1WNe1TYMS)
21. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXV2K_234FJS93pS-m_u8OfOB1c5ss6GtCevNEFbEYCGGBpWARHQybPNRfv6RW1Rx94sfDH4P8G8tgwlKM3Mtna6ZGQEWRheosOMarpIQfPyE2ZQSdAswcwbNdJ_BCQQuw0AtB3mlx0mDAa3Yq3jreuin9pTtHLXK2Rzhhi7w7vbp11zLwS8DaBZ78P9bYA4CVK0W_uKA=)
22. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEELGR3geKKl3cASAManL6f_adL3EmY6BFvfrAdzclLRfLpDTs_48ulA8lfioXr6y_YiSu2-tA8oeex3S3l5gE3vwd0_imldNRs3LSi66LBHYqOYOk3)
23. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGg9BDtTE3Tys5oZVNLErbx5Z_R89QBNOZwCo6h4BQQ8pNQY003QovJCVgnm14dRCwnJnVixeyPbThfB3qIQUd25fq3w7X4KxtB9U7lKj1HNiCjs7pdydUeNqtQ9aMcbIpy5ueeYW9qbHeWCREvsVif1Pj4)


## Annotations
Annotation(end_index=4427, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5jDe2PfnhhyWnOIkPnDkmxmh7bsyn_F_pKi54Eq-JFbI2CROlrJKP0oj5YY_TL0tdJqWSE54_hyYKmSjMvI_j6n_Zul2kubAi8qvjpfofNc0wEjUJQXbb78k5qA733XcOHRLeN2bq0Rh4KrnTV-VsZxpdfI34hIs=', start_index=4415)
Annotation(end_index=4427, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHr0OpgnDJFh_PULDQAquVBjHL1xXnVPd-8YdHWHKmCZVhSDou0Jv7fggNju9RDfs4bw2J6jwKeQCBR3HMEWaHIrhvS_tV7DOVQit6ULWk7ypZgXa47', start_index=4415)
Annotation(end_index=4901, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVxYVI0kNkqMYYd2EWY_kMUAxkp7vur8kkuI_FtvyOKmu18UZCCnxkARgZvPNzNp6sUyU_Lt6uq2xfsrh_bdgcpOBU7Ff-5WAKiHtvi5cymkEBzzCMsyiXvHSfGKzHaKAdTlziyBIor1pOB-avSuMWagiNWW7MWWlgVO_-4csnQkRTPXJxr-1VxNd3D2Oxx9-BCKg0NpKt0sAd', start_index=4892)
Annotation(end_index=5147, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHr0OpgnDJFh_PULDQAquVBjHL1xXnVPd-8YdHWHKmCZVhSDou0Jv7fggNju9RDfs4bw2J6jwKeQCBR3HMEWaHIrhvS_tV7DOVQit6ULWk7ypZgXa47', start_index=5138)
Annotation(end_index=5729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyw1Q-S_ZlclD-dHXr01r_bS1EP7olN36fl4AkQwIDKkNiu3cz7lForzaBkH9gQoAqTouJMsIiSnHl1xDzRwoGqATr7fQO_J5WXG0WRSWSqpOAu9AYDlXLHOMfHtveY5_RV6S3hqOt', start_index=5717)
Annotation(end_index=5729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDz6QOVCur2kZE5eM9jWz398GlBUhZC7vtDUBK6a3wr0ZDqmFNpPQ09MCE__PE-SJQ_QZ68-kxehPjqxsGwSt70bjtEGhMfHQYuG_lWgwja0tLGuzQjw03px_4FCp1nxifXWImlfw8pVRBn1eVlSA=', start_index=5717)
Annotation(end_index=6940, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkz-SVQxST16Tmq6SjveEi-5KSknN5-k7NW1bzjd1v8ZP7-f_5j-4fFqF_7job96htlJcB1LFjqtHbzZB90R4wG1VY_J-b6kkLr24-xrmgSrLUzQgHRftRWbU8h76fDKAD8LHPyMw=', start_index=6925)
Annotation(end_index=6940, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmn63FYB_4DSFSBZlpshl29lLPMRLU5VQ3ZRjsT_5s07-CM2O_USDqkAOFkgepd29NnrftpfQyqmUA5xF09SU_zSY8tz41wSmxUdH9GTJdpdnpVX6P', start_index=6925)
Annotation(end_index=6940, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqKgCkVcidsD5avgiJLrLQnkEVY7aAiuYNhYQ9dhjg6ugAnZBuPFqvC52hzAS_LRjXG2pZX5OyYtAUTL2TEmx5ktcVNuM_T7Amwfni4x1c19SehnTYM-qNeqZSTWxqBaO4GCXzgsQzB3E3zRLLk3zY3xxr', start_index=6925)
Annotation(end_index=7477, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmf2bJwpLpvSOySYpY-iQkWKFJ060F2pR5QF8zxYdsowbKZ7dyjxmo3g8PCTGs9HtciMuDuHuVG3dgQhZ6NG0xl9m5_GbtRTbpGBMAmGKfOMYr0pT9IBaVXbxaERVQwY97faBcrDNqfdkLmesEC9e0nvhlGmoIV9QnQ1jDuhaXkrifB9vL2BAHchgOL5InX-jTp74apTdxDrvz3dOQ8rgqsv-PE3aV', start_index=7461)
Annotation(end_index=7477, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfIVHBuKYZXnl--iwbL94JVgJrRHBNyHDjnfod4NDJMMKFma1LMeNJOymsuYtM5SnE8PCK86PzxnN8M6erP2i4MdZ6Mf88nt-dChgnaNh7-UT78BY0R3Y-cVPE2obTuxvvaEseD8nWvhkJMW3TZQ7X_2GUGUo55cdqZEuhqpWSepC3vs4gmWwovAFivtDoKbMaC35bXjijGGvohJNCJg==', start_index=7461)
Annotation(end_index=7477, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHr0OpgnDJFh_PULDQAquVBjHL1xXnVPd-8YdHWHKmCZVhSDou0Jv7fggNju9RDfs4bw2J6jwKeQCBR3HMEWaHIrhvS_tV7DOVQit6ULWk7ypZgXa47', start_index=7461)
Annotation(end_index=7794, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyw1Q-S_ZlclD-dHXr01r_bS1EP7olN36fl4AkQwIDKkNiu3cz7lForzaBkH9gQoAqTouJMsIiSnHl1xDzRwoGqATr7fQO_J5WXG0WRSWSqpOAu9AYDlXLHOMfHtveY5_RV6S3hqOt', start_index=7785)
Annotation(end_index=8473, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQED7kSgF10M4T2Pw3hni0fwFSFN3mEk-9zY0iEjeNcCmlD1-gwelGxbHVjPM1hCO_d0T6fiNMwDLwzTV_FBlNwI1iMhBQufYUj-88y8zvdM6kv3CDol', start_index=8463)
Annotation(end_index=8934, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKTl4ZObnDO6TNRJg_Wy1P-jQgulonlP5vogfmQGhigOx3rhI7KaSxeRksZmv1XCDYOZATaJzIWXyWjGUn8OedI4HlQwd7cUOKN7vf1qRN7bB42h2B-_BA7HeOwPOgk4J4mncKBsfn', start_index=8924)
Annotation(end_index=9485, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHllb8T1njEmviUdZOeEIAyaIqVbDFT8YNxaKDlAXCKZcZVrPzQovSh1K1TUoFhoIxPed640TKUzTtcbnNKcTlg1WQl9nMyKFLoACoAHMdSt2LeUvBewoJGi3nNLmo1KXCT3bMsSFR8nQ=', start_index=9471)
Annotation(end_index=9485, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuj-u7-DgjsSaauFpt4DvDXXkS-ytayIORBeAoldoNxrxJrdCjiSmcHRI3ejV6hamvhyF1EMaen5yr2DcV4R1Qk_8ZPf7T94w6qqewntjEeYcaWp4IVb1SzDa9g6QcLvEbAQn9Z6wEuHQ2wZrB3KY6RS0=', start_index=9471)
Annotation(end_index=9843, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdl6yS_doLXLX0Ks65U7-vlcVCP26G5DQ1zweVG3-ghphGxJOodSez6NGN7Q-JSerXfQmh-UgK3blU6t_slZPYSkRglp17_FfWg0A5N5w5TaXaA-81', start_index=9833)
Annotation(end_index=10154, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVxYVI0kNkqMYYd2EWY_kMUAxkp7vur8kkuI_FtvyOKmu18UZCCnxkARgZvPNzNp6sUyU_Lt6uq2xfsrh_bdgcpOBU7Ff-5WAKiHtvi5cymkEBzzCMsyiXvHSfGKzHaKAdTlziyBIor1pOB-avSuMWagiNWW7MWWlgVO_-4csnQkRTPXJxr-1VxNd3D2Oxx9-BCKg0NpKt0sAd', start_index=10145)
Annotation(end_index=10739, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3JtleuDrzfO1lFtm-PP0Gq5awFdrj50Rvn-RfwcApJkNnkqAdPxUq7KBsbLaprd-0s_mfa7FXKS2Fds2C3x1DR7uxeCMlq8gNfr25LtAkNR00zzyscaFe4ftTUtXXxgTpjyllzZsTXbuzzPuM1krlfGKY', start_index=10725)
Annotation(end_index=10739, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFde8vkA6HhH1flXyDkUrp8Axh5UMFozE1p84nM9WgK97cVH9iNrnElmgHCn3_8_Lzcn54DHPdCOYTpbNQ_gzR6xNQrOFQicYDnMJK9ycP8sPu_7Q2PT1NT1wMI2v3_UuCSfBqm3rMQjH8aTXKW02S7Q5Ma', start_index=10725)
Annotation(end_index=11371, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKeGBzxolUZRMMj_TNMv6WGGOx_3Xi9QC9vRgXl7c-oggmazOohfeWyA4DGrs1lXTx2xo5iQ7RQG7erJRIGw_Iiorn5HRCQqSi54mtRJ3uzlfGUG1S3gmjL5MtS_zQAghW6VIX0vBmtuw66ISZTzMhI8mF', start_index=11358)
Annotation(end_index=11371, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqKgCkVcidsD5avgiJLrLQnkEVY7aAiuYNhYQ9dhjg6ugAnZBuPFqvC52hzAS_LRjXG2pZX5OyYtAUTL2TEmx5ktcVNuM_T7Amwfni4x1c19SehnTYM-qNeqZSTWxqBaO4GCXzgsQzB3E3zRLLk3zY3xxr', start_index=11358)
Annotation(end_index=11865, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3JtleuDrzfO1lFtm-PP0Gq5awFdrj50Rvn-RfwcApJkNnkqAdPxUq7KBsbLaprd-0s_mfa7FXKS2Fds2C3x1DR7uxeCMlq8gNfr25LtAkNR00zzyscaFe4ftTUtXXxgTpjyllzZsTXbuzzPuM1krlfGKY', start_index=11851)
Annotation(end_index=11865, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFde8vkA6HhH1flXyDkUrp8Axh5UMFozE1p84nM9WgK97cVH9iNrnElmgHCn3_8_Lzcn54DHPdCOYTpbNQ_gzR6xNQrOFQicYDnMJK9ycP8sPu_7Q2PT1NT1wMI2v3_UuCSfBqm3rMQjH8aTXKW02S7Q5Ma', start_index=11851)
Annotation(end_index=12971, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyw1Q-S_ZlclD-dHXr01r_bS1EP7olN36fl4AkQwIDKkNiu3cz7lForzaBkH9gQoAqTouJMsIiSnHl1xDzRwoGqATr7fQO_J5WXG0WRSWSqpOAu9AYDlXLHOMfHtveY5_RV6S3hqOt', start_index=12955)
Annotation(end_index=12971, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmf2bJwpLpvSOySYpY-iQkWKFJ060F2pR5QF8zxYdsowbKZ7dyjxmo3g8PCTGs9HtciMuDuHuVG3dgQhZ6NG0xl9m5_GbtRTbpGBMAmGKfOMYr0pT9IBaVXbxaERVQwY97faBcrDNqfdkLmesEC9e0nvhlGmoIV9QnQ1jDuhaXkrifB9vL2BAHchgOL5InX-jTp74apTdxDrvz3dOQ8rgqsv-PE3aV', start_index=12955)
Annotation(end_index=12971, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1eGZq7ENnTSuiWI0BVXTWadURnGFhTJjKtYuihzkMfhMgD7qSNruD6mdm60TNWN36Uvh4yPx3pwGd9AZu3zxwabkNWzvWB3qTQ3nQ5c2EDTgqJzA5IM54PTEj5vZhwTm4MUglSEhBMA7QvFaGmqs_DPTm0GINuzT9JbWdiw-qykLo4DnXC7wlaSQxd4eV-bd5LPsVZiQUzXNsNI3Vr5v00d4IL44d9ruKPBSDjV1G1LQ4ES7M0HQ=', start_index=12955)
Annotation(end_index=13596, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQED7kSgF10M4T2Pw3hni0fwFSFN3mEk-9zY0iEjeNcCmlD1-gwelGxbHVjPM1hCO_d0T6fiNMwDLwzTV_FBlNwI1iMhBQufYUj-88y8zvdM6kv3CDol', start_index=13586)
Annotation(end_index=14260, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEupyvsmOwrOMT5lPp7OcG9u1WvrI7O_TRTpyaaclg9DBwLMC6Tr6U6D8tqipHldJLonpsNVtZ_EFVCOjaCL2bJbvkU0qOH4x2U3ww1L1sdUAJwY_P33GQ1WNe1TYMS', start_index=14246)
Annotation(end_index=14260, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1eGZq7ENnTSuiWI0BVXTWadURnGFhTJjKtYuihzkMfhMgD7qSNruD6mdm60TNWN36Uvh4yPx3pwGd9AZu3zxwabkNWzvWB3qTQ3nQ5c2EDTgqJzA5IM54PTEj5vZhwTm4MUglSEhBMA7QvFaGmqs_DPTm0GINuzT9JbWdiw-qykLo4DnXC7wlaSQxd4eV-bd5LPsVZiQUzXNsNI3Vr5v00d4IL44d9ruKPBSDjV1G1LQ4ES7M0HQ=', start_index=14246)
Annotation(end_index=14774, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXV2K_234FJS93pS-m_u8OfOB1c5ss6GtCevNEFbEYCGGBpWARHQybPNRfv6RW1Rx94sfDH4P8G8tgwlKM3Mtna6ZGQEWRheosOMarpIQfPyE2ZQSdAswcwbNdJ_BCQQuw0AtB3mlx0mDAa3Yq3jreuin9pTtHLXK2Rzhhi7w7vbp11zLwS8DaBZ78P9bYA4CVK0W_uKA=', start_index=14760)
Annotation(end_index=14774, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdl6yS_doLXLX0Ks65U7-vlcVCP26G5DQ1zweVG3-ghphGxJOodSez6NGN7Q-JSerXfQmh-UgK3blU6t_slZPYSkRglp17_FfWg0A5N5w5TaXaA-81', start_index=14760)
Annotation(end_index=15392, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKeGBzxolUZRMMj_TNMv6WGGOx_3Xi9QC9vRgXl7c-oggmazOohfeWyA4DGrs1lXTx2xo5iQ7RQG7erJRIGw_Iiorn5HRCQqSi54mtRJ3uzlfGUG1S3gmjL5MtS_zQAghW6VIX0vBmtuw66ISZTzMhI8mF', start_index=15375)
Annotation(end_index=15392, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFde8vkA6HhH1flXyDkUrp8Axh5UMFozE1p84nM9WgK97cVH9iNrnElmgHCn3_8_Lzcn54DHPdCOYTpbNQ_gzR6xNQrOFQicYDnMJK9ycP8sPu_7Q2PT1NT1wMI2v3_UuCSfBqm3rMQjH8aTXKW02S7Q5Ma', start_index=15375)
Annotation(end_index=15392, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDz6QOVCur2kZE5eM9jWz398GlBUhZC7vtDUBK6a3wr0ZDqmFNpPQ09MCE__PE-SJQ_QZ68-kxehPjqxsGwSt70bjtEGhMfHQYuG_lWgwja0tLGuzQjw03px_4FCp1nxifXWImlfw8pVRBn1eVlSA=', start_index=15375)
Annotation(end_index=15834, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1eGZq7ENnTSuiWI0BVXTWadURnGFhTJjKtYuihzkMfhMgD7qSNruD6mdm60TNWN36Uvh4yPx3pwGd9AZu3zxwabkNWzvWB3qTQ3nQ5c2EDTgqJzA5IM54PTEj5vZhwTm4MUglSEhBMA7QvFaGmqs_DPTm0GINuzT9JbWdiw-qykLo4DnXC7wlaSQxd4eV-bd5LPsVZiQUzXNsNI3Vr5v00d4IL44d9ruKPBSDjV1G1LQ4ES7M0HQ=', start_index=15824)
Annotation(end_index=16448, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3JtleuDrzfO1lFtm-PP0Gq5awFdrj50Rvn-RfwcApJkNnkqAdPxUq7KBsbLaprd-0s_mfa7FXKS2Fds2C3x1DR7uxeCMlq8gNfr25LtAkNR00zzyscaFe4ftTUtXXxgTpjyllzZsTXbuzzPuM1krlfGKY', start_index=16434)
Annotation(end_index=16448, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFde8vkA6HhH1flXyDkUrp8Axh5UMFozE1p84nM9WgK97cVH9iNrnElmgHCn3_8_Lzcn54DHPdCOYTpbNQ_gzR6xNQrOFQicYDnMJK9ycP8sPu_7Q2PT1NT1wMI2v3_UuCSfBqm3rMQjH8aTXKW02S7Q5Ma', start_index=16434)
Annotation(end_index=17794, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmf2bJwpLpvSOySYpY-iQkWKFJ060F2pR5QF8zxYdsowbKZ7dyjxmo3g8PCTGs9HtciMuDuHuVG3dgQhZ6NG0xl9m5_GbtRTbpGBMAmGKfOMYr0pT9IBaVXbxaERVQwY97faBcrDNqfdkLmesEC9e0nvhlGmoIV9QnQ1jDuhaXkrifB9vL2BAHchgOL5InX-jTp74apTdxDrvz3dOQ8rgqsv-PE3aV', start_index=17785)
Annotation(end_index=17918, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmn63FYB_4DSFSBZlpshl29lLPMRLU5VQ3ZRjsT_5s07-CM2O_USDqkAOFkgepd29NnrftpfQyqmUA5xF09SU_zSY8tz41wSmxUdH9GTJdpdnpVX6P', start_index=17909)
Annotation(end_index=18039, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdl6yS_doLXLX0Ks65U7-vlcVCP26G5DQ1zweVG3-ghphGxJOodSez6NGN7Q-JSerXfQmh-UgK3blU6t_slZPYSkRglp17_FfWg0A5N5w5TaXaA-81', start_index=18029)
Annotation(end_index=18131, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyw1Q-S_ZlclD-dHXr01r_bS1EP7olN36fl4AkQwIDKkNiu3cz7lForzaBkH9gQoAqTouJMsIiSnHl1xDzRwoGqATr7fQO_J5WXG0WRSWSqpOAu9AYDlXLHOMfHtveY5_RV6S3hqOt', start_index=18122)
Annotation(end_index=18235, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEELGR3geKKl3cASAManL6f_adL3EmY6BFvfrAdzclLRfLpDTs_48ulA8lfioXr6y_YiSu2-tA8oeex3S3l5gE3vwd0_imldNRs3LSi66LBHYqOYOk3', start_index=18225)
Annotation(end_index=18332, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGg9BDtTE3Tys5oZVNLErbx5Z_R89QBNOZwCo6h4BQQ8pNQY003QovJCVgnm14dRCwnJnVixeyPbThfB3qIQUd25fq3w7X4KxtB9U7lKj1HNiCjs7pdydUeNqtQ9aMcbIpy5ueeYW9qbHeWCREvsVif1Pj4', start_index=18322)
Annotation(end_index=18459, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQED7kSgF10M4T2Pw3hni0fwFSFN3mEk-9zY0iEjeNcCmlD1-gwelGxbHVjPM1hCO_d0T6fiNMwDLwzTV_FBlNwI1iMhBQufYUj-88y8zvdM6kv3CDol', start_index=18449)
Annotation(end_index=18559, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEupyvsmOwrOMT5lPp7OcG9u1WvrI7O_TRTpyaaclg9DBwLMC6Tr6U6D8tqipHldJLonpsNVtZ_EFVCOjaCL2bJbvkU0qOH4x2U3ww1L1sdUAJwY_P33GQ1WNe1TYMS', start_index=18549)
Annotation(end_index=18643, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVxYVI0kNkqMYYd2EWY_kMUAxkp7vur8kkuI_FtvyOKmu18UZCCnxkARgZvPNzNp6sUyU_Lt6uq2xfsrh_bdgcpOBU7Ff-5WAKiHtvi5cymkEBzzCMsyiXvHSfGKzHaKAdTlziyBIor1pOB-avSuMWagiNWW7MWWlgVO_-4csnQkRTPXJxr-1VxNd3D2Oxx9-BCKg0NpKt0sAd', start_index=18634)
Annotation(end_index=18735, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHr0OpgnDJFh_PULDQAquVBjHL1xXnVPd-8YdHWHKmCZVhSDou0Jv7fggNju9RDfs4bw2J6jwKeQCBR3HMEWaHIrhvS_tV7DOVQit6ULWk7ypZgXa47', start_index=18726)
Annotation(end_index=18844, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5jDe2PfnhhyWnOIkPnDkmxmh7bsyn_F_pKi54Eq-JFbI2CROlrJKP0oj5YY_TL0tdJqWSE54_hyYKmSjMvI_j6n_Zul2kubAi8qvjpfofNc0wEjUJQXbb78k5qA733XcOHRLeN2bq0Rh4KrnTV-VsZxpdfI34hIs=', start_index=18835)
Annotation(end_index=18907, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDz6QOVCur2kZE5eM9jWz398GlBUhZC7vtDUBK6a3wr0ZDqmFNpPQ09MCE__PE-SJQ_QZ68-kxehPjqxsGwSt70bjtEGhMfHQYuG_lWgwja0tLGuzQjw03px_4FCp1nxifXWImlfw8pVRBn1eVlSA=', start_index=18898)
Annotation(end_index=18963, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfIVHBuKYZXnl--iwbL94JVgJrRHBNyHDjnfod4NDJMMKFma1LMeNJOymsuYtM5SnE8PCK86PzxnN8M6erP2i4MdZ6Mf88nt-dChgnaNh7-UT78BY0R3Y-cVPE2obTuxvvaEseD8nWvhkJMW3TZQ7X_2GUGUo55cdqZEuhqpWSepC3vs4gmWwovAFivtDoKbMaC35bXjijGGvohJNCJg==', start_index=18953)
Annotation(end_index=19065, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFde8vkA6HhH1flXyDkUrp8Axh5UMFozE1p84nM9WgK97cVH9iNrnElmgHCn3_8_Lzcn54DHPdCOYTpbNQ_gzR6xNQrOFQicYDnMJK9ycP8sPu_7Q2PT1NT1wMI2v3_UuCSfBqm3rMQjH8aTXKW02S7Q5Ma', start_index=19052)
Annotation(end_index=19065, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqKgCkVcidsD5avgiJLrLQnkEVY7aAiuYNhYQ9dhjg6ugAnZBuPFqvC52hzAS_LRjXG2pZX5OyYtAUTL2TEmx5ktcVNuM_T7Amwfni4x1c19SehnTYM-qNeqZSTWxqBaO4GCXzgsQzB3E3zRLLk3zY3xxr', start_index=19052)
Annotation(end_index=19169, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1eGZq7ENnTSuiWI0BVXTWadURnGFhTJjKtYuihzkMfhMgD7qSNruD6mdm60TNWN36Uvh4yPx3pwGd9AZu3zxwabkNWzvWB3qTQ3nQ5c2EDTgqJzA5IM54PTEj5vZhwTm4MUglSEhBMA7QvFaGmqs_DPTm0GINuzT9JbWdiw-qykLo4DnXC7wlaSQxd4eV-bd5LPsVZiQUzXNsNI3Vr5v00d4IL44d9ruKPBSDjV1G1LQ4ES7M0HQ=', start_index=19159)
Annotation(end_index=19285, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXV2K_234FJS93pS-m_u8OfOB1c5ss6GtCevNEFbEYCGGBpWARHQybPNRfv6RW1Rx94sfDH4P8G8tgwlKM3Mtna6ZGQEWRheosOMarpIQfPyE2ZQSdAswcwbNdJ_BCQQuw0AtB3mlx0mDAa3Yq3jreuin9pTtHLXK2Rzhhi7w7vbp11zLwS8DaBZ78P9bYA4CVK0W_uKA=', start_index=19275)
Annotation(end_index=19369, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKeGBzxolUZRMMj_TNMv6WGGOx_3Xi9QC9vRgXl7c-oggmazOohfeWyA4DGrs1lXTx2xo5iQ7RQG7erJRIGw_Iiorn5HRCQqSi54mtRJ3uzlfGUG1S3gmjL5MtS_zQAghW6VIX0vBmtuw66ISZTzMhI8mF', start_index=19359)
Annotation(end_index=19440, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3JtleuDrzfO1lFtm-PP0Gq5awFdrj50Rvn-RfwcApJkNnkqAdPxUq7KBsbLaprd-0s_mfa7FXKS2Fds2C3x1DR7uxeCMlq8gNfr25LtAkNR00zzyscaFe4ftTUtXXxgTpjyllzZsTXbuzzPuM1krlfGKY', start_index=19430)

## Sources
