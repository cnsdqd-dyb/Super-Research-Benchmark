# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 87dc16a3 | **Time:** 1092.30s | **Cost:** $4.38141
--------------------------------------------------------------------------------

# The Influence of Social Network Rewiring Probability on the Spectral Clustering Structure of Collective Identity Vectors in Urbanization Models

### Key Points
*   **Rewiring as a Phase Transition Parameter:** The rewiring probability ($p$) in small-world network models (Watts-Strogatz) acts as a critical control parameter that dictates the transition of urban social structures from highly clustered, insular communities (low $p$) to integrated, random networks (high $p$). This transition fundamentally alters the spectral properties of the network's Laplacian matrix.
*   **Spectral Clustering and Identity Preservation:** At low rewiring probabilities, the spectral clustering structure exhibits distinct, block-diagonal features with near-zero eigenvalues, corresponding to strong, segregated collective identities (echo chambers). As rewiring increases, the "spectral gap" widens, facilitating global information diffusion but potentially eroding distinct local cultural or social identities.
*   **Urbanization and Deterritorialization:** In urbanization models, increasing rewiring probability simulates the "deterritorialization" of social ties—moving from geography-based village structures to interest-based or random urban interactions. This shift disrupts the stability of collective identity vectors, leading to either homogenized urban identities or fragmented, transient social alignments.
*   **Homophily vs. Randomness:** Research indicates that homophily-based networks (low rewiring) maintain high variance in collective identity (polarization), whereas high rewiring introduces "shortcuts" that can depolarize communities but may also reduce social cohesion and the resilience of local support systems.
*   **Algorithmic Sensitivity:** The efficacy of spectral clustering algorithms in detecting collective identity groups degrades as rewiring probability increases. The introduction of random links perturbs the eigenvectors of the graph Laplacian, making it computationally difficult to distinguish between genuine social communities and random noise in high-entropy urban environments.

---

## 1. Introduction

The intersection of network topology, spectral graph theory, and social dynamics offers a profound framework for understanding how urbanization reshapes human identity. The query at hand—*What is the influence of social network rewiring probability on the spectral clustering structure of collective identity vectors in urbanization models?*—requires a synthesis of mathematical modeling, sociopolitical theory, and computational simulation.

Urbanization is not merely a demographic shift; it is a structural transformation of social connectivity. Traditional rural structures are often modeled as regular lattices where connections are local, redundant, and highly clustered. Urban environments, characterized by mobility and digital connectivity, introduce "rewiring"—the breaking of local ties and the formation of long-range connections. This process is mathematically formalized in the Watts-Strogatz model, where a rewiring probability $p$ interpolates between order and randomness [cite: 1, 2].

Collective identity vectors represent the multidimensional attributes of social agents—their beliefs, cultural values, and affiliations. The "spectral clustering structure" refers to the geometric organization of these agents in the eigenspace of the social graph. When agents are strongly clustered, their identity vectors align within specific subspaces defined by the eigenvectors of the graph Laplacian.

This report argues that the rewiring probability serves as a proxy for the intensity of urbanization and modernization. It demonstrates that increasing rewiring probability fundamentally destabilizes the spectral structure of collective identities, transitioning the system from a state of high modularity and polarization (distinct identity clusters) to a state of low modularity and potential homogenization (spectral mixing). This transition has critical implications for social cohesion, political polarization, and the resilience of urban communities.

---

## 2. Theoretical Foundations

To fully address the influence of rewiring probability on spectral clustering, we must first establish the mathematical and theoretical underpinnings of the constituent models.

### 2.1 The Watts-Strogatz Model and Rewiring Probability ($p$)

The Watts-Strogatz (WS) model is the canonical framework for studying the transition from regular to random networks. It begins with a regular ring lattice where each node is connected to its $k$ nearest neighbors. The parameter $p$ ($0 \le p \le 1$) represents the probability that an edge is disconnected from its original target and reconnected to a randomly chosen node [cite: 2, 3].

*   **Regular Regime ($p \approx 0$):** The network is a regular lattice. It possesses a high clustering coefficient ($C$) but a long average path length ($L$). In the context of urbanization, this represents traditional, geography-bound village communities where social ties are dense, local, and overlapping [cite: 4].
*   **Small-World Regime ($0 < p < 1$):** As $p$ increases slightly, "shortcuts" are introduced. These shortcuts drastically reduce the average path length $L$ while leaving the clustering coefficient $C$ relatively high. This "small-world" property mimics real-world social networks where distinct communities exist but are linked by short chains of acquaintances [cite: 1, 5].
*   **Random Regime ($p \approx 1$):** As $p$ approaches 1, the network converges to an Erdős-Rényi (ER) random graph. The clustering coefficient drops significantly, and the degree distribution becomes Poissonian. This represents a "deterritorialized" urban environment where social connections are independent of spatial proximity [cite: 6, 7].

The rewiring probability is the independent variable in this analysis. It dictates the topological substrate upon which collective identity vectors evolve.

### 2.2 Spectral Graph Theory and Clustering Structure

Spectral clustering is a technique that partitions a graph based on the eigenvalues (spectrum) and eigenvectors of its Laplacian matrix, $L = D - A$, where $D$ is the degree matrix and $A$ is the adjacency matrix [cite: 8].

*   **The Spectrum:** The eigenvalues of $L$, denoted $0 = \lambda_1 \le \lambda_2 \le \dots \le \lambda_n$, reveal the connectivity of the graph. The multiplicity of the eigenvalue 0 indicates the number of connected components.
*   **The Fiedler Value ($\lambda_2$):** The second smallest eigenvalue, known as the algebraic connectivity or Fiedler value, measures how well-connected the graph is. A low $\lambda_2$ implies the graph is easily cut into two disconnected pieces (indicating strong community structure), while a high $\lambda_2$ implies the graph is a robust expander (random-like) [cite: 7, 8].
*   **Eigenvectors and Identity:** In spectral clustering, the eigenvectors corresponding to the smallest non-zero eigenvalues are used to embed nodes into a lower-dimensional space. Nodes that are tightly connected (forming a cluster) will be mapped to proximal points in this spectral space. If collective identity vectors are influenced by social influence, they will tend to align with these spectral clusters [cite: 9, 10].

### 2.3 Collective Identity Vectors

Collective identity is modeled as a vector associated with each node (agent). Let $v_i \in \mathbb{R}^d$ be the identity vector of agent $i$. The evolution of these vectors is often governed by homophily and social influence:
1.  **Homophily:** Agents are more likely to connect if $\|v_i - v_j\|$ is small [cite: 11].
2.  **Social Influence:** Connected agents tend to align their vectors over time, reducing $\|v_i - v_j\|$ [cite: 12, 13].

The "spectral clustering structure of collective identity vectors" therefore refers to the correlation between the topological clusters (defined by the graph spectrum) and the attribute clusters (defined by the identity vectors).

---

## 3. The Influence of Rewiring Probability on Spectral Structure

The core of the inquiry lies in how varying $p$ alters the spectral properties of the graph and, consequently, the organization of identity vectors.

### 3.1 Disruption of Block-Diagonal Structure (Low $p$)

At $p=0$, the adjacency matrix (and thus the Laplacian) of a ring lattice or a set of disconnected "factions" has a circulant or block-diagonal structure.
*   **Spectral Signature:** The spectrum contains multiple zero or near-zero eigenvalues. The eigenvectors are localized, meaning they have non-zero entries only for nodes within specific local neighborhoods [cite: 9, 14].
*   **Identity Implications:** In this regime, collective identity vectors are "frozen" in local clusters. Diffusion of information is slow. Distinct "factions" can maintain orthogonal identity vectors without interference. This models a segregated urban landscape or a collection of isolated rural villages [cite: 15, 16].
*   **Urbanization Context:** This corresponds to the "village corporatism" or "fractionalized" state described in sociological literature, where groups have almost no social ties between them [cite: 15, 17].

### 3.2 The Emergence of the Spectral Gap (Intermediate $p$)

As $p$ increases (entering the small-world regime), long-range links are formed.
*   **Spectral Signature:** The degeneracy of the zero eigenvalue is broken (if components merge). The Fiedler value ($\lambda_2$) increases, creating a "spectral gap." This gap represents the speed of convergence for random walks and diffusion processes [cite: 7, 18].
*   **Identity Implications:** The introduction of shortcuts allows identity vectors to influence distant parts of the network. However, because $C$ remains high, local clusters persist. This creates a tension: global trends can spread (due to shortcuts), but local distinctiveness is maintained (due to clustering). This is the "sweet spot" for complex collective identities—allowing for a shared "urban identity" while preserving sub-cultural distinctiveness [cite: 1, 4].
*   **Research Finding:** Source 47 notes that the spectral radius ratio for node degree increases from 1 to 1.15 as rewiring probability increases from 0 to 0.5. This indicates a measurable shift in the network's structural variance, which directly impacts how identity vectors propagate [cite: 18].

### 3.3 Homogenization and the Semicircle Law (High $p$)

As $p \to 1$, the network becomes random.
*   **Spectral Signature:** The spectrum of the Laplacian approaches the Wigner Semicircle Law (characteristic of random matrices). The eigenvalues become tightly clustered around the mean, and the spectral gap becomes very large [cite: 8, 19].
*   **Identity Implications:** The distinct spectral clusters dissolve. The eigenvectors become delocalized (spread across the whole network). In terms of collective identity, this facilitates rapid global consensus or "mixing." It becomes difficult to sustain distinct, polarized identity vectors because the high connectivity averages out local fluctuations.
*   **Urbanization Context:** This represents the "deterritorialized" city where traditional social bonds are dissolved. While this reduces isolation, it can lead to a loss of "sense of belonging" and the erosion of specific cultural identities, leading to a homogenized "mass" identity [cite: 20, 21].

---

## 4. Urbanization Models: Simulating Identity Dynamics

Urbanization models use these network principles to simulate how cities grow and how social fabrics change. The research results highlight several specific dynamics.

### 4.1 Deterritorialization and the Loss of Local Clusters

Urbanization is described as a process of "deterritorialization," where the link between physical space and social connection is weakened [cite: 20].
*   **Model Representation:** In the model, this is represented by increasing $p$. As $p$ increases, the "geodesic distance" (social distance) between nodes becomes decoupled from their "Euclidean distance" (spatial distance).
*   **Impact on Identity:** Source 73 notes that urbanization triggers "distributional politics" and challenges the legitimacy of local identities. In the spectral domain, this is seen as the merging of previously orthogonal eigenvectors. The "identity vectors" of rural migrants (initially distinct) become projected onto the dominant eigenvectors of the urban network, forcing assimilation or hybridization [cite: 20].

### 4.2 Polarization and Echo Chambers

Contrary to the assumption that connectivity always breeds consensus, specific ranges of rewiring can exacerbate polarization.
*   **Homophily-Based Rewiring:** If rewiring is not random but based on homophily (connecting to similar others), the network creates "echo chambers." Source 60 and 67 explicitly state that homophily-based networks (which can be seen as a specific, non-random rewiring regime) produce greater national identity polarization compared to random networks [cite: 22].
*   **Spectral Clustering of Echo Chambers:** In these homophilous networks, the Laplacian matrix develops a near-block-diagonal structure *despite* long-range connections, because the connections are only between "like-minded" nodes. The spectral clustering algorithm will easily identify these polarized groups as distinct clusters [cite: 12, 13].
*   **Depolarization via Random Nudge:** Source 24 and 68 discuss using a "random dynamical nudge" (effectively increasing random rewiring) to depolarize echo chambers. This confirms that increasing the randomness of rewiring (higher $p$) degrades the spectral structure that supports polarized identities [cite: 12].

### 4.3 Sustainability and Resource Heterogeneity

Source 87 and 88 present a "social-ecological network model" where rewiring probability $\phi$ (a variant of $p$) interacts with resource distribution.
*   **Regimes of Collapse:** The research identifies distinct regimes. For low rewiring ($\phi < 0.8$) and slow interaction, sustainable regimes exist. However, high rewiring can lead to "non-sustainable or collapse regimes" depending on resource heterogeneity [cite: 23, 24].
*   **Interpretation:** This suggests that while high rewiring (urbanization) increases efficiency and information flow, it may reduce the resilience of the system. The "spectral clustering" of the network acts as a buffer; when that structure is destroyed by high $p$, the system becomes vulnerable to cascading failures or resource exhaustion, mirroring the ecological fragility of hyper-connected urban systems.

---

## 5. Algorithmic Implications: Spectral Clustering Stability

The query specifically asks about the "spectral clustering structure." This refers not just to the sociology, but to the mathematical stability of the clustering itself.

### 5.1 Perturbation of Eigenvectors

Spectral clustering relies on the stability of the eigenvectors of the Laplacian. According to the Davis-Kahan $\sin \Theta$ theorem, the stability of these eigenvectors depends on the "eigengap" (the distance between eigenvalues).
*   **Effect of Rewiring:** Increasing $p$ generally increases the eigengap between the first few eigenvalues (separating the connected component from the rest) but compresses the higher-order eigenvalues.
*   **Noise Sensitivity:** As $p$ increases, the "noise" (random connections) increases. If the rewiring is too high, the "community structure" (the signal) becomes indistinguishable from the random edges (the noise). The spectral clustering algorithm may fail to recover the "true" identity groups, or it may return clusters that are artifacts of randomness rather than genuine social structures [cite: 9, 10].

### 5.2 Fuzzy Similarity and Adaptive Clustering

To counter the loss of structure at high rewiring probabilities, advanced models use "fuzzy similarity matrices" or "adaptive k-nearest neighbor" graphs.
*   **Adaptive Methods:** Source 38 and 39 discuss "Joint Learning of Spectral Clustering Structure and Fuzzy Similarity Matrix." These methods attempt to learn a similarity matrix that preserves the block-diagonal structure even when the raw data (or network) is noisy or highly rewired [cite: 9, 14].
*   **Relevance to Urbanization:** In a highly urbanized (high $p$) environment, defining "collective identity" requires these adaptive methods. Simple adjacency-based spectral clustering fails because the "neighborhood" is no longer clearly defined by the network topology alone. One must infer the "latent" spectral structure that persists despite the random rewiring [cite: 10, 25].

---

## 6. Synthesis: The Spectral Topology of Urban Identity

We can now synthesize the findings into a coherent narrative regarding the influence of rewiring probability.

### 6.1 The Transition Curve

The influence of rewiring probability $p$ on the spectral clustering structure of collective identity vectors follows a non-linear trajectory:

1.  **The Segregated Phase ($p \to 0$):**
    *   **Topology:** Regular lattice / Caveman graph.
    *   **Spectral Structure:** High modularity. Multiple zero/near-zero eigenvalues. Eigenvectors are localized.
    *   **Identity:** Hyper-local, fragmented, stable. High diversity between clusters, zero diversity within clusters.
    *   **Urban Model:** Pre-industrial villages or highly segregated ghettos.

2.  **The Small-World Phase (Intermediate $p$):**
    *   **Topology:** High Clustering ($C$), Low Path Length ($L$).
    *   **Spectral Structure:** "Spectral gap" emerges. Eigenvalues separate, but cluster structure remains detectable in the lower eigenvectors.
    *   **Identity:** Coexistence of local distinctiveness and global awareness. Identity vectors can diffuse but are "pinned" by local clusters.
    *   **Urban Model:** The ideal "sustainable" city or "urban ecovillage" [cite: 26]. Communities interact but retain agency.

3.  **The Integrated/Homogenized Phase ($p \to 1$):**
    *   **Topology:** Random Graph. Low $C$, Low $L$.
    *   **Spectral Structure:** Loss of modularity. Spectrum follows Semicircle Law. Eigenvectors are delocalized.
    *   **Identity:** Rapid diffusion leading to global consensus (homogenization) or chaotic fluctuation (if noise is high). Loss of stable "collective" identities.
    *   **Urban Model:** The "deterritorialized" metropolis. Anonymity, transient ties, loss of traditional social capital [cite: 20, 21].

### 6.2 Vectors of Collective Identity

The "vectors" themselves—representing the content of identity—are subjected to forces defined by this spectral topology.
*   **Projection:** The identity vectors are effectively projected onto the eigenspace of the network.
*   **Smoothing:** The Laplacian acts as a diffusion operator. High rewiring increases the "smoothing" of these vectors across the graph.
*   **Resistance:** "Factions" or "fractionalization" (Source 20) act as barriers to this smoothing. If the rewiring is biased (homophily), the spectral smoothing is confined within the faction, reinforcing the identity vector's magnitude and direction (polarization) rather than diluting it [cite: 15, 22].

---

## 7. Conclusion

The rewiring probability $p$ is the master switch in urbanization models that controls the tension between **local cohesion** and **global integration**. Its influence on the spectral clustering structure is decisive:

1.  **Structural Dissolution:** Increasing $p$ degrades the block-diagonal spectral structure that supports distinct collective identities.
2.  **Diffusion Acceleration:** Increasing $p$ widens the spectral gap, accelerating the diffusion of identity vectors and promoting homogenization.
3.  **Algorithmic Obfuscation:** High $p$ introduces topological noise that makes the algorithmic detection of "true" collective identities via spectral methods more difficult, necessitating fuzzy or adaptive approaches.

In the context of urbanization, this suggests that the "modernization" of social networks (increasing $p$) inherently challenges the preservation of distinct collective identities. Unless counter-mechanisms like homophily or active "factionalization" are present, the spectral logic of the rewired network drives the system toward entropy and identity dilution. The "politics of deterritorialization" [cite: 20, 21] is thus mathematically visible in the collapsing eigenspectrum of the urban social graph.

### References
[cite: 27] Quantification of network structural dissimilarities.
[cite: 20] Urbanization of the local state.
[cite: 15, 16] Fractionalization and small-world networks.
[cite: 6, 7] Random graphs and Watts-Strogatz models.
[cite: 12] Depolarization of echo chambers by random dynamical nudge.
[cite: 9, 14] Joint Learning of Spectral Clustering Structure.
[cite: 18] Spectral radius ratio and rewiring probability.
[cite: 13, 22] Social identity bias and communication network / National identity polarisation.
[cite: 1, 2] Watts-Strogatz model properties.
[cite: 4] The Non-Random Brain (WS model diagram).
[cite: 11] Diversity and Community Can Coexist (Rewiring and homophily).
[cite: 26] A Model of Sustainable Living Collective Identity.
[cite: 23, 24] Sustainable use of renewable resources in social-ecological networks.
[cite: 17] Postcolonial Vietnam (Village corporatism).

**Sources:**
1. [mathoverflow.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRdVj-GcEPPqEec7mx0pcJ_pf1-qzZaj1044QUSU8z3QBV-rb6gD3DOgembSLB7vTxlZW1r5nzoNbAJXz17o0eW-YBvkAfbgA6tChYWLLGXiP79T7RATvLTTB64t5DNuwkx7kzppHJLkwrpODYhf8T92nOAW0BwM4D6Q==)
2. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWM1NYYbbReWa-m_N6bo-8_UnZRFCZdeZUqnUDCj3gOJMh4Ngiyhy70eqdmjNJOap_M9bxBTaKhJTbYUNwdKfzBf_z82WjfBtPZrw6Wa8-BiQSq0B5DtjiM-rD_51bY2kuBn4KAbseV4X6lkIn36md)
3. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0UipPSM_iuyUyuNe8IUeO3hy8fscBziw6BltwC6AAf1Ibh3qqJF8m-fWZ_YNAc_w9d-H8qTuZvNv0oQU6x8giVFZInOXrUyO-q_o8MFwOcZIymWqE6L4JcJt72JCDIaA7Uqe3MhotK0neajT0n0M=)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOEoiJhOFRzAr8OCPP3nodYEfNByQi1uhbhDo1849u8EtmYriPp8xEscXI9q21Xbke1M87xSPEkznJ48XD-ipizrUzThot24oDXCEEmsxrvu3c8zSt4BI-yVjP5lZbEtggK_BECyzhr00nhZGLndVkR7CmaMOANFxkupR7lUALv7InPoR4tTXxQAdoEcDpTE4mWBo47KOhVgooBNJg1ACszVJXID-k-I03YzKDrByjiC__vhuhYk-d5g_iPXvC)
5. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFad_Rag0fPmm01m2js61wr8ac7Ft4IbV97E51wcH3kiWxfJiVt1dWkiD5qe44S4XAKc8G3BZ0HFApL2GkeTSoB39tiBI2r9NyaLQK8Jjk0lmYdzGUsryPTNLYNutEu_3vpwG7myUMSHIIg37YazrSTu_csGg==)
6. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgPVTxG4boWNSBuIm1T8QcTWh56tiEDAf4nH8i6wixlMNti2xdVucWzXC-f4QcSCAIM0WRGzz3sYF0unja7Ck4xIN5QKR4sfQQP4QSdjN8Ajl2o0-V2w==)
7. [su.se](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcqyPhULn7Majt7DSeCizBmMdop5bH88v17-KEp3bBPSscMyeatE2tHAG8LV-9YEIpFvfOQl2gIKlFJSFu3-Ult2K-WLxMNNEurDLiimQzqsehQOfST99k0FlOLXktvyTn99aw1-zNWISJQV_If0V5zun4byCAutng4mtQyIQy5uhBFfHcn9pYnVhPKfpvNxjpSfEeQTxggCZ_trrYuZsnh-XplFgXJw==)
8. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGF-xmaKv8O4p8mpvuxwzPWg2KKwVrjHajA6F-AStmVnbfxL1_rj_MNk-WkC50iX0VbU5J33aY-n07_oI_6dEPf2RSVonS1EYt6mbQFt9-DcUFDwsBw)
9. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjiBjtrOXvFygSLiZBHHAp1sokMQg1dBPUd_THb3exFYVzS73y2I6sPPZDmnAb8hPPhqtRt5pYgBx83_aC6mlwL_gZ1lL6fq1KJmrT2LaEF5gBvnqUoiNWATg-6D5BWQ==)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZG-Z9Mvbez__5kaDfMYextG4o4waEMwVOac-FsjrvMZP11cgt4V2RV8owRe8ZFLT51K5mQudWT1CV78MVnJu8gUMM9ADDScevvOGXG4wdYiVGGz8aKBZzx4QBqGebeI0fDxcdIT-lSHN--WsD-vOBR9Y5xXN-6l_HTTi3DMyIGl1dhaA0w7_MV1ClhZWmilAX_MxLxBi6088=)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFejLkl4KQx56_FS73CkCCJYDUs4R2kInCAHlMl1f78uVWsyg6et1MPIEuNWVFyHS7rJqoc-BujWd5A9xk7sfKmYWwRImiSkvgALLSiU24LjdFzT49GbrxZorDQb4a2QFazh-3dbkJqE9h5_W991IfySwThUfFtNomkxgq35wLZIvKQvCUX5Sw6dxN8wQ==)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHligmWUzZkhNAkdSzHwatEUUky82EG20-_Ty64N2fJNF8HZA5NB8nwA51vPGHe0q3-SqNtbtVQ2aG-mSzSCCJ2nDXtz61L7kMbaoJy2imsupUIGaDzufrrV74uqmtJDWRpLMFOKFHZUPFd-S_o5zxtQws2LHqFMU0XdpCbMqF9xoWYji2bOkg1VBQgFcy6ysOy_zQ_6GcCsKqEFuwde7-twNQ=)
13. [royalsocietypublishing.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6L2cbHXcRK9ZnkKFj_DLvbbfykCVFuj9tFL23UERFtpJSLDq3IDKMEcvdDQFABcAEciHGgcXiw2Y1hfCH7hP0DDk33ccq8nU6Vp476KhBRRzA5b47DJ3J6lOMOhdNCIOULLA5FmHXaagAsKpSBIWsvm1xJlh9TCE9isYl447AOSheqnYA4aYJ-qhhw_xspD7AluP5PB7Ecjod5g1UvlXUB8SUfKlSXpMjiw==)
14. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEe7XeZx_uSn5_3DVMzIaQaI2cbJVjuc7t3Sn66MjWsUqLhpYvRrFwZW025mmOngRlAhISiTq2l68mIBqWwVBx95wbXURu3YBVclbngK3JGFeTOHMswNfzDdfLKSIILAV6d66j_FVgYQg==)
15. [northwestern.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_agvl39r-0oQoBgGGIeRlhyvhYIMdXkUcdUoUTerxDvgdXV_nAJqyZUfaGDEw_WlKSh_oaUjXRFjAqk-5LPEAExGVN7qZh-e7yTgdEoM3s67de2Idim-6K66FZdqRTDbg-Dl-z914Em2_8Hf_jNArsuSiJ1bhT3uL7QNwoJE=)
16. [bancaditalia.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYQiOxoiVwpRjT5wyvn-vXjehkYKpgNQxVk9cX8KdpOmRvQKQmWeONCTitGj34OWHkyguGGqJz723adulOyglMvp1CHh8IgmyFrwNsIAsI2YjBFJYQTE2_wo5EM9yLwCZ25o5R-OCZsXko4Ge4umV3DAqoyBYUhVbMGxebQyr9VqcdB7suKLM2wlZ7brOU0Stx)
17. [dokumen.pub](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeo-TPnuwX1OYhvGxr2DhavWTF2HwO6cU3LTHoiZe1NBOgRlF-Tt4ZEVTrrBPha80MM6WwMIb005ywqYi04JBGIZU8Ct_IUveP5zVQ_wKdmCiu2XeMQXqIaog26TegrMsl98lsCPvWzWdwCM4r1UiT2qySINUsjxzvlOg9u__BCIAaqEPXHSloaS1b0xFhvrL7Dphs)
18. [airccj.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdkxP6ek8WA_thpsRTBUasI1CA9eiNMy2Bgm0EbFCKJzScvweO6gajTFdLbiBCmGGXr4r2xm0h5mPAhBWQZOkj_pgp7ZpMOYhmoTO5e_Q8SLKa00GgZetxOcr42Gzpu6Q=)
19. [upenn.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2tZxtBuzk_FxAQ02mxnHRu6KGvU7-ucHbqUBubu6e3D1KAfInQW1TgJQvfKcriijF5lb0DPZFbeHMmddBhw7z7mxwTIksRfLCYghIEUzk3bin9G09xhSquMX_5ZiW2OnoDvypnI0v0Mcj9GorvQe9MjaaCW8-KJvpUFQoAlLtsUOZ)
20. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9dEHbKC9bRvy5b9oznmJWArOVcLu53jengKge2LtgApT9kEwsDuc-ntkoARcDr0TieSPasXWm8pTmSopqWqd2nass2Eq-bzDQ4_b7oAW_EDck-DQp4FemuHUy5HysOut7ZWchVBjn48cbEw==)
21. [dokumen.pub](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoHX7tuxbEcjNws55P8FCY5O5crjtDFlW5NxHJb9LDpEsa3VOscjknwEeUswVt0ZkZp59a1h7u74MdKrU1evyuzZDqBXkDeMS6IJmRfFPmylKQ9hwG6AMzZ4ji36nv-eioFcJRn4Gc4WrlSANnRXPuIgc9DvWRZ0S86S3yXYrenRgVsQKYUSH-jRgZbpuQKcwK4Mqy0wvLdpTzLMdUUWaVqsdOiJ1lSjQprfNmcSspjQ==)
22. [gla.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFITZkznSBJIske4ZWKpXJRbXskSI8Tljitwr7okJkf2qNMDCDbQfWtwfUNSiuaLEPFUEuf-gWaap7PZOWCFn7gwE7xQFchn-LrK1iuCLXwCQiIA38Dg7Bfu64MZFa8bu1-20tRJM1cTqiVnEVJaXA0)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHF9FVCiwGo1K01JjS7-EQRKgR1WW3X4JzT8owhhXYzZ55oXWjFxGnJCeCBf-cA0AnbUvhNNvHyt1-FMJF9n6eTjHaIq5RwSjfsbzGEmK3LINGEMmTsJhzyoxB5Hdtq9AlMzj7cDDJ7ifm_W49_q0D9ZGKCRlSOvMr9bcrSRm5F0kxFSjkcODkWFav_iKBypgZuSklXFYvB-dkUMIKUuaj9fSxDqixKGpH2zx5QCP7m1xp84K_EJV6NzK8taIdR0cUf6fJcgXxueQ9s0Olx3sTtRiA2QARDWnAuBwHxS_CUoIUyd7a_inqN)
24. [pik-potsdam.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8BTZx5vN6T-tDa-rvX2v-VH7F_PU3vNRKiG1W-SCgRQow2rsuA4Ilyser_Z-wLB_gO-nYwC2tSI0z4hG0h3kVXJUyTqq65faFkCMx2vMTdWacKDd4vkckeFXo6HjpD8oOaTfHRwwBOv4pov-oHR3AP1dUjdtG-GUDTB-J4BiRr-5snUpCFIcnejj6tl4mt5PG)
25. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbCaz4LSHn9R5zcEBWp_0mruto26Pz6VSgRFUGHNLwnWLtfdJB9BCnJaxzX8FF8Uk1uGan0gvP2yh7-ADelA3c9-YFapzrhkByIKtGTYyOZadXV2iBYeiXviMrGVMs1HWWF3VUzdU7ow==)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc3gUuZGnG8pMhGjbWJg73RxmQ9GeJQaCsExyRSrHSCd-eWwSOIYEBdPLReKF__hNxitAJ2NX-n04i-h2TpGJjeTMvNzQYtvt-tB-q9bRih3PjfJYC_1fB4NPz2vkl8KPYOmCPsD3dA00GUms9ILTPO1VR-9wsjXUiKBMG4y2dAaiASqJ6m8dQ9ICcQ9TxZjIsxZj3knXtA6WmTeMcavCZiqk52A4mxxRJBIErQvgw38k=)
27. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHUzL2wBH5ex88kovtgAb1R7fTyF3JKuAZY9FVg0EPkprHBQVrLUHdX4dP-rqudnq_o2kJVIczb3yTc7jCna1v_S5nDqdhGkS4tyH1qLKN5GcDIiqJyg2kpInynmB-GCWR05S4tf18-s5t0BeSraUrJAhrZi_YMvSyzl3cygM8zDJA-z9TzrjITxwgxwylOS7Sy2zIJ-2QTM9lTiZX)


## Annotations
Annotation(end_index=3149, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWM1NYYbbReWa-m_N6bo-8_UnZRFCZdeZUqnUDCj3gOJMh4Ngiyhy70eqdmjNJOap_M9bxBTaKhJTbYUNwdKfzBf_z82WjfBtPZrw6Wa8-BiQSq0B5DtjiM-rD_51bY2kuBn4KAbseV4X6lkIn36md', start_index=3137)
Annotation(end_index=3149, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRdVj-GcEPPqEec7mx0pcJ_pf1-qzZaj1044QUSU8z3QBV-rb6gD3DOgembSLB7vTxlZW1r5nzoNbAJXz17o0eW-YBvkAfbgA6tChYWLLGXiP79T7RATvLTTB64t5DNuwkx7kzppHJLkwrpODYhf8T92nOAW0BwM4D6Q==', start_index=3137)
Annotation(end_index=4786, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0UipPSM_iuyUyuNe8IUeO3hy8fscBziw6BltwC6AAf1Ibh3qqJF8m-fWZ_YNAc_w9d-H8qTuZvNv0oQU6x8giVFZInOXrUyO-q_o8MFwOcZIymWqE6L4JcJt72JCDIaA7Uqe3MhotK0neajT0n0M=', start_index=4774)
Annotation(end_index=4786, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWM1NYYbbReWa-m_N6bo-8_UnZRFCZdeZUqnUDCj3gOJMh4Ngiyhy70eqdmjNJOap_M9bxBTaKhJTbYUNwdKfzBf_z82WjfBtPZrw6Wa8-BiQSq0B5DtjiM-rD_51bY2kuBn4KAbseV4X6lkIn36md', start_index=4774)
Annotation(end_index=5108, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOEoiJhOFRzAr8OCPP3nodYEfNByQi1uhbhDo1849u8EtmYriPp8xEscXI9q21Xbke1M87xSPEkznJ48XD-ipizrUzThot24oDXCEEmsxrvu3c8zSt4BI-yVjP5lZbEtggK_BECyzhr00nhZGLndVkR7CmaMOANFxkupR7lUALv7InPoR4tTXxQAdoEcDpTE4mWBo47KOhVgooBNJg1ACszVJXID-k-I03YzKDrByjiC__vhuhYk-d5g_iPXvC', start_index=5099)
Annotation(end_index=5487, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFad_Rag0fPmm01m2js61wr8ac7Ft4IbV97E51wcH3kiWxfJiVt1dWkiD5qe44S4XAKc8G3BZ0HFApL2GkeTSoB39tiBI2r9NyaLQK8Jjk0lmYdzGUsryPTNLYNutEu_3vpwG7myUMSHIIg37YazrSTu_csGg==', start_index=5475)
Annotation(end_index=5487, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRdVj-GcEPPqEec7mx0pcJ_pf1-qzZaj1044QUSU8z3QBV-rb6gD3DOgembSLB7vTxlZW1r5nzoNbAJXz17o0eW-YBvkAfbgA6tChYWLLGXiP79T7RATvLTTB64t5DNuwkx7kzppHJLkwrpODYhf8T92nOAW0BwM4D6Q==', start_index=5475)
Annotation(end_index=5836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgPVTxG4boWNSBuIm1T8QcTWh56tiEDAf4nH8i6wixlMNti2xdVucWzXC-f4QcSCAIM0WRGzz3sYF0unja7Ck4xIN5QKR4sfQQP4QSdjN8Ajl2o0-V2w==', start_index=5824)
Annotation(end_index=5836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcqyPhULn7Majt7DSeCizBmMdop5bH88v17-KEp3bBPSscMyeatE2tHAG8LV-9YEIpFvfOQl2gIKlFJSFu3-Ult2K-WLxMNNEurDLiimQzqsehQOfST99k0FlOLXktvyTn99aw1-zNWISJQV_If0V5zun4byCAutng4mtQyIQy5uhBFfHcn9pYnVhPKfpvNxjpSfEeQTxggCZ_trrYuZsnh-XplFgXJw==', start_index=5824)
Annotation(end_index=6274, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGF-xmaKv8O4p8mpvuxwzPWg2KKwVrjHajA6F-AStmVnbfxL1_rj_MNk-WkC50iX0VbU5J33aY-n07_oI_6dEPf2RSVonS1EYt6mbQFt9-DcUFDwsBw', start_index=6265)
Annotation(end_index=6886, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcqyPhULn7Majt7DSeCizBmMdop5bH88v17-KEp3bBPSscMyeatE2tHAG8LV-9YEIpFvfOQl2gIKlFJSFu3-Ult2K-WLxMNNEurDLiimQzqsehQOfST99k0FlOLXktvyTn99aw1-zNWISJQV_If0V5zun4byCAutng4mtQyIQy5uhBFfHcn9pYnVhPKfpvNxjpSfEeQTxggCZ_trrYuZsnh-XplFgXJw==', start_index=6874)
Annotation(end_index=6886, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGF-xmaKv8O4p8mpvuxwzPWg2KKwVrjHajA6F-AStmVnbfxL1_rj_MNk-WkC50iX0VbU5J33aY-n07_oI_6dEPf2RSVonS1EYt6mbQFt9-DcUFDwsBw', start_index=6874)
Annotation(end_index=7315, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZG-Z9Mvbez__5kaDfMYextG4o4waEMwVOac-FsjrvMZP11cgt4V2RV8owRe8ZFLT51K5mQudWT1CV78MVnJu8gUMM9ADDScevvOGXG4wdYiVGGz8aKBZzx4QBqGebeI0fDxcdIT-lSHN--WsD-vOBR9Y5xXN-6l_HTTi3DMyIGl1dhaA0w7_MV1ClhZWmilAX_MxLxBi6088=', start_index=7302)
Annotation(end_index=7315, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjiBjtrOXvFygSLiZBHHAp1sokMQg1dBPUd_THb3exFYVzS73y2I6sPPZDmnAb8hPPhqtRt5pYgBx83_aC6mlwL_gZ1lL6fq1KJmrT2LaEF5gBvnqUoiNWATg-6D5BWQ==', start_index=7302)
Annotation(end_index=7672, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFejLkl4KQx56_FS73CkCCJYDUs4R2kInCAHlMl1f78uVWsyg6et1MPIEuNWVFyHS7rJqoc-BujWd5A9xk7sfKmYWwRImiSkvgALLSiU24LjdFzT49GbrxZorDQb4a2QFazh-3dbkJqE9h5_W991IfySwThUfFtNomkxgq35wLZIvKQvCUX5Sw6dxN8wQ==', start_index=7662)
Annotation(end_index=7795, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6L2cbHXcRK9ZnkKFj_DLvbbfykCVFuj9tFL23UERFtpJSLDq3IDKMEcvdDQFABcAEciHGgcXiw2Y1hfCH7hP0DDk33ccq8nU6Vp476KhBRRzA5b47DJ3J6lOMOhdNCIOULLA5FmHXaagAsKpSBIWsvm1xJlh9TCE9isYl447AOSheqnYA4aYJ-qhhw_xspD7AluP5PB7Ecjod5g1UvlXUB8SUfKlSXpMjiw==', start_index=7781)
Annotation(end_index=7795, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHligmWUzZkhNAkdSzHwatEUUky82EG20-_Ty64N2fJNF8HZA5NB8nwA51vPGHe0q3-SqNtbtVQ2aG-mSzSCCJ2nDXtz61L7kMbaoJy2imsupUIGaDzufrrV74uqmtJDWRpLMFOKFHZUPFd-S_o5zxtQws2LHqFMU0XdpCbMqF9xoWYji2bOkg1VBQgFcy6ysOy_zQ_6GcCsKqEFuwde7-twNQ=', start_index=7781)
Annotation(end_index=8685, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEe7XeZx_uSn5_3DVMzIaQaI2cbJVjuc7t3Sn66MjWsUqLhpYvRrFwZW025mmOngRlAhISiTq2l68mIBqWwVBx95wbXURu3YBVclbngK3JGFeTOHMswNfzDdfLKSIILAV6d66j_FVgYQg==', start_index=8672)
Annotation(end_index=8685, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjiBjtrOXvFygSLiZBHHAp1sokMQg1dBPUd_THb3exFYVzS73y2I6sPPZDmnAb8hPPhqtRt5pYgBx83_aC6mlwL_gZ1lL6fq1KJmrT2LaEF5gBvnqUoiNWATg-6D5BWQ==', start_index=8672)
Annotation(end_index=9009, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYQiOxoiVwpRjT5wyvn-vXjehkYKpgNQxVk9cX8KdpOmRvQKQmWeONCTitGj34OWHkyguGGqJz723adulOyglMvp1CHh8IgmyFrwNsIAsI2YjBFJYQTE2_wo5EM9yLwCZ25o5R-OCZsXko4Ge4umV3DAqoyBYUhVbMGxebQyr9VqcdB7suKLM2wlZ7brOU0Stx', start_index=8995)
Annotation(end_index=9009, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_agvl39r-0oQoBgGGIeRlhyvhYIMdXkUcdUoUTerxDvgdXV_nAJqyZUfaGDEw_WlKSh_oaUjXRFjAqk-5LPEAExGVN7qZh-e7yTgdEoM3s67de2Idim-6K66FZdqRTDbg-Dl-z914Em2_8Hf_jNArsuSiJ1bhT3uL7QNwoJE=', start_index=8995)
Annotation(end_index=9218, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_agvl39r-0oQoBgGGIeRlhyvhYIMdXkUcdUoUTerxDvgdXV_nAJqyZUfaGDEw_WlKSh_oaUjXRFjAqk-5LPEAExGVN7qZh-e7yTgdEoM3s67de2Idim-6K66FZdqRTDbg-Dl-z914Em2_8Hf_jNArsuSiJ1bhT3uL7QNwoJE=', start_index=9204)
Annotation(end_index=9218, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeo-TPnuwX1OYhvGxr2DhavWTF2HwO6cU3LTHoiZe1NBOgRlF-Tt4ZEVTrrBPha80MM6WwMIb005ywqYi04JBGIZU8Ct_IUveP5zVQ_wKdmCiu2XeMQXqIaog26TegrMsl98lsCPvWzWdwCM4r1UiT2qySINUsjxzvlOg9u__BCIAaqEPXHSloaS1b0xFhvrL7Dphs', start_index=9204)
Annotation(end_index=9632, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcqyPhULn7Majt7DSeCizBmMdop5bH88v17-KEp3bBPSscMyeatE2tHAG8LV-9YEIpFvfOQl2gIKlFJSFu3-Ult2K-WLxMNNEurDLiimQzqsehQOfST99k0FlOLXktvyTn99aw1-zNWISJQV_If0V5zun4byCAutng4mtQyIQy5uhBFfHcn9pYnVhPKfpvNxjpSfEeQTxggCZ_trrYuZsnh-XplFgXJw==', start_index=9619)
Annotation(end_index=9632, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdkxP6ek8WA_thpsRTBUasI1CA9eiNMy2Bgm0EbFCKJzScvweO6gajTFdLbiBCmGGXr4r2xm0h5mPAhBWQZOkj_pgp7ZpMOYhmoTO5e_Q8SLKa00GgZetxOcr42Gzpu6Q=', start_index=9619)
Annotation(end_index=10109, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOEoiJhOFRzAr8OCPP3nodYEfNByQi1uhbhDo1849u8EtmYriPp8xEscXI9q21Xbke1M87xSPEkznJ48XD-ipizrUzThot24oDXCEEmsxrvu3c8zSt4BI-yVjP5lZbEtggK_BECyzhr00nhZGLndVkR7CmaMOANFxkupR7lUALv7InPoR4tTXxQAdoEcDpTE4mWBo47KOhVgooBNJg1ACszVJXID-k-I03YzKDrByjiC__vhuhYk-d5g_iPXvC', start_index=10097)
Annotation(end_index=10109, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRdVj-GcEPPqEec7mx0pcJ_pf1-qzZaj1044QUSU8z3QBV-rb6gD3DOgembSLB7vTxlZW1r5nzoNbAJXz17o0eW-YBvkAfbgA6tChYWLLGXiP79T7RATvLTTB64t5DNuwkx7kzppHJLkwrpODYhf8T92nOAW0BwM4D6Q==', start_index=10097)
Annotation(end_index=10410, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdkxP6ek8WA_thpsRTBUasI1CA9eiNMy2Bgm0EbFCKJzScvweO6gajTFdLbiBCmGGXr4r2xm0h5mPAhBWQZOkj_pgp7ZpMOYhmoTO5e_Q8SLKa00GgZetxOcr42Gzpu6Q=', start_index=10400)
Annotation(end_index=10756, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2tZxtBuzk_FxAQ02mxnHRu6KGvU7-ucHbqUBubu6e3D1KAfInQW1TgJQvfKcriijF5lb0DPZFbeHMmddBhw7z7mxwTIksRfLCYghIEUzk3bin9G09xhSquMX_5ZiW2OnoDvypnI0v0Mcj9GorvQe9MjaaCW8-KJvpUFQoAlLtsUOZ', start_index=10743)
Annotation(end_index=10756, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGF-xmaKv8O4p8mpvuxwzPWg2KKwVrjHajA6F-AStmVnbfxL1_rj_MNk-WkC50iX0VbU5J33aY-n07_oI_6dEPf2RSVonS1EYt6mbQFt9-DcUFDwsBw', start_index=10743)
Annotation(end_index=11420, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9dEHbKC9bRvy5b9oznmJWArOVcLu53jengKge2LtgApT9kEwsDuc-ntkoARcDr0TieSPasXWm8pTmSopqWqd2nass2Eq-bzDQ4_b7oAW_EDck-DQp4FemuHUy5HysOut7ZWchVBjn48cbEw==', start_index=11406)
Annotation(end_index=11420, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoHX7tuxbEcjNws55P8FCY5O5crjtDFlW5NxHJb9LDpEsa3VOscjknwEeUswVt0ZkZp59a1h7u74MdKrU1evyuzZDqBXkDeMS6IJmRfFPmylKQ9hwG6AMzZ4ji36nv-eioFcJRn4Gc4WrlSANnRXPuIgc9DvWRZ0S86S3yXYrenRgVsQKYUSH-jRgZbpuQKcwK4Mqy0wvLdpTzLMdUUWaVqsdOiJ1lSjQprfNmcSspjQ==', start_index=11406)
Annotation(end_index=11861, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9dEHbKC9bRvy5b9oznmJWArOVcLu53jengKge2LtgApT9kEwsDuc-ntkoARcDr0TieSPasXWm8pTmSopqWqd2nass2Eq-bzDQ4_b7oAW_EDck-DQp4FemuHUy5HysOut7ZWchVBjn48cbEw==', start_index=11851)
Annotation(end_index=12509, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9dEHbKC9bRvy5b9oznmJWArOVcLu53jengKge2LtgApT9kEwsDuc-ntkoARcDr0TieSPasXWm8pTmSopqWqd2nass2Eq-bzDQ4_b7oAW_EDck-DQp4FemuHUy5HysOut7ZWchVBjn48cbEw==', start_index=12499)
Annotation(end_index=13042, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFITZkznSBJIske4ZWKpXJRbXskSI8Tljitwr7okJkf2qNMDCDbQfWtwfUNSiuaLEPFUEuf-gWaap7PZOWCFn7gwE7xQFchn-LrK1iuCLXwCQiIA38Dg7Bfu64MZFa8bu1-20tRJM1cTqiVnEVJaXA0', start_index=13032)
Annotation(end_index=13392, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6L2cbHXcRK9ZnkKFj_DLvbbfykCVFuj9tFL23UERFtpJSLDq3IDKMEcvdDQFABcAEciHGgcXiw2Y1hfCH7hP0DDk33ccq8nU6Vp476KhBRRzA5b47DJ3J6lOMOhdNCIOULLA5FmHXaagAsKpSBIWsvm1xJlh9TCE9isYl447AOSheqnYA4aYJ-qhhw_xspD7AluP5PB7Ecjod5g1UvlXUB8SUfKlSXpMjiw==', start_index=13378)
Annotation(end_index=13392, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHligmWUzZkhNAkdSzHwatEUUky82EG20-_Ty64N2fJNF8HZA5NB8nwA51vPGHe0q3-SqNtbtVQ2aG-mSzSCCJ2nDXtz61L7kMbaoJy2imsupUIGaDzufrrV74uqmtJDWRpLMFOKFHZUPFd-S_o5zxtQws2LHqFMU0XdpCbMqF9xoWYji2bOkg1VBQgFcy6ysOy_zQ_6GcCsKqEFuwde7-twNQ=', start_index=13378)
Annotation(end_index=13710, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHligmWUzZkhNAkdSzHwatEUUky82EG20-_Ty64N2fJNF8HZA5NB8nwA51vPGHe0q3-SqNtbtVQ2aG-mSzSCCJ2nDXtz61L7kMbaoJy2imsupUIGaDzufrrV74uqmtJDWRpLMFOKFHZUPFd-S_o5zxtQws2LHqFMU0XdpCbMqF9xoWYji2bOkg1VBQgFcy6ysOy_zQ_6GcCsKqEFuwde7-twNQ=', start_index=13700)
Annotation(end_index=14191, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8BTZx5vN6T-tDa-rvX2v-VH7F_PU3vNRKiG1W-SCgRQow2rsuA4Ilyser_Z-wLB_gO-nYwC2tSI0z4hG0h3kVXJUyTqq65faFkCMx2vMTdWacKDd4vkckeFXo6HjpD8oOaTfHRwwBOv4pov-oHR3AP1dUjdtG-GUDTB-J4BiRr-5snUpCFIcnejj6tl4mt5PG', start_index=14177)
Annotation(end_index=14191, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHF9FVCiwGo1K01JjS7-EQRKgR1WW3X4JzT8owhhXYzZ55oXWjFxGnJCeCBf-cA0AnbUvhNNvHyt1-FMJF9n6eTjHaIq5RwSjfsbzGEmK3LINGEMmTsJhzyoxB5Hdtq9AlMzj7cDDJ7ifm_W49_q0D9ZGKCRlSOvMr9bcrSRm5F0kxFSjkcODkWFav_iKBypgZuSklXFYvB-dkUMIKUuaj9fSxDqixKGpH2zx5QCP7m1xp84K_EJV6NzK8taIdR0cUf6fJcgXxueQ9s0Olx3sTtRiA2QARDWnAuBwHxS_CUoIUyd7a_inqN', start_index=14177)
Annotation(end_index=15734, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZG-Z9Mvbez__5kaDfMYextG4o4waEMwVOac-FsjrvMZP11cgt4V2RV8owRe8ZFLT51K5mQudWT1CV78MVnJu8gUMM9ADDScevvOGXG4wdYiVGGz8aKBZzx4QBqGebeI0fDxcdIT-lSHN--WsD-vOBR9Y5xXN-6l_HTTi3DMyIGl1dhaA0w7_MV1ClhZWmilAX_MxLxBi6088=', start_index=15721)
Annotation(end_index=15734, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjiBjtrOXvFygSLiZBHHAp1sokMQg1dBPUd_THb3exFYVzS73y2I6sPPZDmnAb8hPPhqtRt5pYgBx83_aC6mlwL_gZ1lL6fq1KJmrT2LaEF5gBvnqUoiNWATg-6D5BWQ==', start_index=15721)
Annotation(end_index=16242, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEe7XeZx_uSn5_3DVMzIaQaI2cbJVjuc7t3Sn66MjWsUqLhpYvRrFwZW025mmOngRlAhISiTq2l68mIBqWwVBx95wbXURu3YBVclbngK3JGFeTOHMswNfzDdfLKSIILAV6d66j_FVgYQg==', start_index=16229)
Annotation(end_index=16242, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjiBjtrOXvFygSLiZBHHAp1sokMQg1dBPUd_THb3exFYVzS73y2I6sPPZDmnAb8hPPhqtRt5pYgBx83_aC6mlwL_gZ1lL6fq1KJmrT2LaEF5gBvnqUoiNWATg-6D5BWQ==', start_index=16229)
Annotation(end_index=16628, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZG-Z9Mvbez__5kaDfMYextG4o4waEMwVOac-FsjrvMZP11cgt4V2RV8owRe8ZFLT51K5mQudWT1CV78MVnJu8gUMM9ADDScevvOGXG4wdYiVGGz8aKBZzx4QBqGebeI0fDxcdIT-lSHN--WsD-vOBR9Y5xXN-6l_HTTi3DMyIGl1dhaA0w7_MV1ClhZWmilAX_MxLxBi6088=', start_index=16614)
Annotation(end_index=16628, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbCaz4LSHn9R5zcEBWp_0mruto26Pz6VSgRFUGHNLwnWLtfdJB9BCnJaxzX8FF8Uk1uGan0gvP2yh7-ADelA3c9-YFapzrhkByIKtGTYyOZadXV2iBYeiXviMrGVMs1HWWF3VUzdU7ow==', start_index=16614)
Annotation(end_index=17886, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc3gUuZGnG8pMhGjbWJg73RxmQ9GeJQaCsExyRSrHSCd-eWwSOIYEBdPLReKF__hNxitAJ2NX-n04i-h2TpGJjeTMvNzQYtvt-tB-q9bRih3PjfJYC_1fB4NPz2vkl8KPYOmCPsD3dA00GUms9ILTPO1VR-9wsjXUiKBMG4y2dAaiASqJ6m8dQ9ICcQ9TxZjIsxZj3knXtA6WmTeMcavCZiqk52A4mxxRJBIErQvgw38k=', start_index=17876)
Annotation(end_index=18455, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9dEHbKC9bRvy5b9oznmJWArOVcLu53jengKge2LtgApT9kEwsDuc-ntkoARcDr0TieSPasXWm8pTmSopqWqd2nass2Eq-bzDQ4_b7oAW_EDck-DQp4FemuHUy5HysOut7ZWchVBjn48cbEw==', start_index=18441)
Annotation(end_index=18455, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoHX7tuxbEcjNws55P8FCY5O5crjtDFlW5NxHJb9LDpEsa3VOscjknwEeUswVt0ZkZp59a1h7u74MdKrU1evyuzZDqBXkDeMS6IJmRfFPmylKQ9hwG6AMzZ4ji36nv-eioFcJRn4Gc4WrlSANnRXPuIgc9DvWRZ0S86S3yXYrenRgVsQKYUSH-jRgZbpuQKcwK4Mqy0wvLdpTzLMdUUWaVqsdOiJ1lSjQprfNmcSspjQ==', start_index=18441)
Annotation(end_index=19170, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFITZkznSBJIske4ZWKpXJRbXskSI8Tljitwr7okJkf2qNMDCDbQfWtwfUNSiuaLEPFUEuf-gWaap7PZOWCFn7gwE7xQFchn-LrK1iuCLXwCQiIA38Dg7Bfu64MZFa8bu1-20tRJM1cTqiVnEVJaXA0', start_index=19156)
Annotation(end_index=19170, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_agvl39r-0oQoBgGGIeRlhyvhYIMdXkUcdUoUTerxDvgdXV_nAJqyZUfaGDEw_WlKSh_oaUjXRFjAqk-5LPEAExGVN7qZh-e7yTgdEoM3s67de2Idim-6K66FZdqRTDbg-Dl-z914Em2_8Hf_jNArsuSiJ1bhT3uL7QNwoJE=', start_index=19156)
Annotation(end_index=20341, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9dEHbKC9bRvy5b9oznmJWArOVcLu53jengKge2LtgApT9kEwsDuc-ntkoARcDr0TieSPasXWm8pTmSopqWqd2nass2Eq-bzDQ4_b7oAW_EDck-DQp4FemuHUy5HysOut7ZWchVBjn48cbEw==', start_index=20327)
Annotation(end_index=20341, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoHX7tuxbEcjNws55P8FCY5O5crjtDFlW5NxHJb9LDpEsa3VOscjknwEeUswVt0ZkZp59a1h7u74MdKrU1evyuzZDqBXkDeMS6IJmRfFPmylKQ9hwG6AMzZ4ji36nv-eioFcJRn4Gc4WrlSANnRXPuIgc9DvWRZ0S86S3yXYrenRgVsQKYUSH-jRgZbpuQKcwK4Mqy0wvLdpTzLMdUUWaVqsdOiJ1lSjQprfNmcSspjQ==', start_index=20327)
Annotation(end_index=20458, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHUzL2wBH5ex88kovtgAb1R7fTyF3JKuAZY9FVg0EPkprHBQVrLUHdX4dP-rqudnq_o2kJVIczb3yTc7jCna1v_S5nDqdhGkS4tyH1qLKN5GcDIiqJyg2kpInynmB-GCWR05S4tf18-s5t0BeSraUrJAhrZi_YMvSyzl3cygM8zDJA-z9TzrjITxwgxwylOS7Sy2zIJ-2QTM9lTiZX', start_index=20448)
Annotation(end_index=20523, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9dEHbKC9bRvy5b9oznmJWArOVcLu53jengKge2LtgApT9kEwsDuc-ntkoARcDr0TieSPasXWm8pTmSopqWqd2nass2Eq-bzDQ4_b7oAW_EDck-DQp4FemuHUy5HysOut7ZWchVBjn48cbEw==', start_index=20513)
Annotation(end_index=20571, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYQiOxoiVwpRjT5wyvn-vXjehkYKpgNQxVk9cX8KdpOmRvQKQmWeONCTitGj34OWHkyguGGqJz723adulOyglMvp1CHh8IgmyFrwNsIAsI2YjBFJYQTE2_wo5EM9yLwCZ25o5R-OCZsXko4Ge4umV3DAqoyBYUhVbMGxebQyr9VqcdB7suKLM2wlZ7brOU0Stx', start_index=20557)
Annotation(end_index=20571, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_agvl39r-0oQoBgGGIeRlhyvhYIMdXkUcdUoUTerxDvgdXV_nAJqyZUfaGDEw_WlKSh_oaUjXRFjAqk-5LPEAExGVN7qZh-e7yTgdEoM3s67de2Idim-6K66FZdqRTDbg-Dl-z914Em2_8Hf_jNArsuSiJ1bhT3uL7QNwoJE=', start_index=20557)
Annotation(end_index=20628, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgPVTxG4boWNSBuIm1T8QcTWh56tiEDAf4nH8i6wixlMNti2xdVucWzXC-f4QcSCAIM0WRGzz3sYF0unja7Ck4xIN5QKR4sfQQP4QSdjN8Ajl2o0-V2w==', start_index=20616)
Annotation(end_index=20628, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcqyPhULn7Majt7DSeCizBmMdop5bH88v17-KEp3bBPSscMyeatE2tHAG8LV-9YEIpFvfOQl2gIKlFJSFu3-Ult2K-WLxMNNEurDLiimQzqsehQOfST99k0FlOLXktvyTn99aw1-zNWISJQV_If0V5zun4byCAutng4mtQyIQy5uhBFfHcn9pYnVhPKfpvNxjpSfEeQTxggCZ_trrYuZsnh-XplFgXJw==', start_index=20616)
Annotation(end_index=20680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHligmWUzZkhNAkdSzHwatEUUky82EG20-_Ty64N2fJNF8HZA5NB8nwA51vPGHe0q3-SqNtbtVQ2aG-mSzSCCJ2nDXtz61L7kMbaoJy2imsupUIGaDzufrrV74uqmtJDWRpLMFOKFHZUPFd-S_o5zxtQws2LHqFMU0XdpCbMqF9xoWYji2bOkg1VBQgFcy6ysOy_zQ_6GcCsKqEFuwde7-twNQ=', start_index=20670)
Annotation(end_index=20753, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEe7XeZx_uSn5_3DVMzIaQaI2cbJVjuc7t3Sn66MjWsUqLhpYvRrFwZW025mmOngRlAhISiTq2l68mIBqWwVBx95wbXURu3YBVclbngK3JGFeTOHMswNfzDdfLKSIILAV6d66j_FVgYQg==', start_index=20740)
Annotation(end_index=20753, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjiBjtrOXvFygSLiZBHHAp1sokMQg1dBPUd_THb3exFYVzS73y2I6sPPZDmnAb8hPPhqtRt5pYgBx83_aC6mlwL_gZ1lL6fq1KJmrT2LaEF5gBvnqUoiNWATg-6D5BWQ==', start_index=20740)
Annotation(end_index=20813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdkxP6ek8WA_thpsRTBUasI1CA9eiNMy2Bgm0EbFCKJzScvweO6gajTFdLbiBCmGGXr4r2xm0h5mPAhBWQZOkj_pgp7ZpMOYhmoTO5e_Q8SLKa00GgZetxOcr42Gzpu6Q=', start_index=20803)
Annotation(end_index=20876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6L2cbHXcRK9ZnkKFj_DLvbbfykCVFuj9tFL23UERFtpJSLDq3IDKMEcvdDQFABcAEciHGgcXiw2Y1hfCH7hP0DDk33ccq8nU6Vp476KhBRRzA5b47DJ3J6lOMOhdNCIOULLA5FmHXaagAsKpSBIWsvm1xJlh9TCE9isYl447AOSheqnYA4aYJ-qhhw_xspD7AluP5PB7Ecjod5g1UvlXUB8SUfKlSXpMjiw==', start_index=20862)
Annotation(end_index=20876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFITZkznSBJIske4ZWKpXJRbXskSI8Tljitwr7okJkf2qNMDCDbQfWtwfUNSiuaLEPFUEuf-gWaap7PZOWCFn7gwE7xQFchn-LrK1iuCLXwCQiIA38Dg7Bfu64MZFa8bu1-20tRJM1cTqiVnEVJaXA0', start_index=20862)
Annotation(end_index=20970, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWM1NYYbbReWa-m_N6bo-8_UnZRFCZdeZUqnUDCj3gOJMh4Ngiyhy70eqdmjNJOap_M9bxBTaKhJTbYUNwdKfzBf_z82WjfBtPZrw6Wa8-BiQSq0B5DtjiM-rD_51bY2kuBn4KAbseV4X6lkIn36md', start_index=20958)
Annotation(end_index=20970, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRdVj-GcEPPqEec7mx0pcJ_pf1-qzZaj1044QUSU8z3QBV-rb6gD3DOgembSLB7vTxlZW1r5nzoNbAJXz17o0eW-YBvkAfbgA6tChYWLLGXiP79T7RATvLTTB64t5DNuwkx7kzppHJLkwrpODYhf8T92nOAW0BwM4D6Q==', start_index=20958)
Annotation(end_index=21013, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOEoiJhOFRzAr8OCPP3nodYEfNByQi1uhbhDo1849u8EtmYriPp8xEscXI9q21Xbke1M87xSPEkznJ48XD-ipizrUzThot24oDXCEEmsxrvu3c8zSt4BI-yVjP5lZbEtggK_BECyzhr00nhZGLndVkR7CmaMOANFxkupR7lUALv7InPoR4tTXxQAdoEcDpTE4mWBo47KOhVgooBNJg1ACszVJXID-k-I03YzKDrByjiC__vhuhYk-d5g_iPXvC', start_index=21004)
Annotation(end_index=21065, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFejLkl4KQx56_FS73CkCCJYDUs4R2kInCAHlMl1f78uVWsyg6et1MPIEuNWVFyHS7rJqoc-BujWd5A9xk7sfKmYWwRImiSkvgALLSiU24LjdFzT49GbrxZorDQb4a2QFazh-3dbkJqE9h5_W991IfySwThUfFtNomkxgq35wLZIvKQvCUX5Sw6dxN8wQ==', start_index=21055)
Annotation(end_index=21138, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc3gUuZGnG8pMhGjbWJg73RxmQ9GeJQaCsExyRSrHSCd-eWwSOIYEBdPLReKF__hNxitAJ2NX-n04i-h2TpGJjeTMvNzQYtvt-tB-q9bRih3PjfJYC_1fB4NPz2vkl8KPYOmCPsD3dA00GUms9ILTPO1VR-9wsjXUiKBMG4y2dAaiASqJ6m8dQ9ICcQ9TxZjIsxZj3knXtA6WmTeMcavCZiqk52A4mxxRJBIErQvgw38k=', start_index=21128)
Annotation(end_index=21204, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8BTZx5vN6T-tDa-rvX2v-VH7F_PU3vNRKiG1W-SCgRQow2rsuA4Ilyser_Z-wLB_gO-nYwC2tSI0z4hG0h3kVXJUyTqq65faFkCMx2vMTdWacKDd4vkckeFXo6HjpD8oOaTfHRwwBOv4pov-oHR3AP1dUjdtG-GUDTB-J4BiRr-5snUpCFIcnejj6tl4mt5PG', start_index=21190)
Annotation(end_index=21204, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHF9FVCiwGo1K01JjS7-EQRKgR1WW3X4JzT8owhhXYzZ55oXWjFxGnJCeCBf-cA0AnbUvhNNvHyt1-FMJF9n6eTjHaIq5RwSjfsbzGEmK3LINGEMmTsJhzyoxB5Hdtq9AlMzj7cDDJ7ifm_W49_q0D9ZGKCRlSOvMr9bcrSRm5F0kxFSjkcODkWFav_iKBypgZuSklXFYvB-dkUMIKUuaj9fSxDqixKGpH2zx5QCP7m1xp84K_EJV6NzK8taIdR0cUf6fJcgXxueQ9s0Olx3sTtRiA2QARDWnAuBwHxS_CUoIUyd7a_inqN', start_index=21190)
Annotation(end_index=21285, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeo-TPnuwX1OYhvGxr2DhavWTF2HwO6cU3LTHoiZe1NBOgRlF-Tt4ZEVTrrBPha80MM6WwMIb005ywqYi04JBGIZU8Ct_IUveP5zVQ_wKdmCiu2XeMQXqIaog26TegrMsl98lsCPvWzWdwCM4r1UiT2qySINUsjxzvlOg9u__BCIAaqEPXHSloaS1b0xFhvrL7Dphs', start_index=21275)

## Sources
