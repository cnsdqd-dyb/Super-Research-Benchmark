# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 3b396c6e | **Time:** 671.38s | **Cost:** $2.56010
--------------------------------------------------------------------------------

# In Digital Interaction Hypergraphs, Does the Spectral Radius of Trust Matrices Delimit the Stability Boundary of Interaction Forms?

## Executive Summary

The stability of interaction forms within digital interaction hypergraphs is fundamentally governed by the spectral properties of the underlying structural matrices, including trust matrices. Research confirms that the spectral radius—and more broadly, the complete spectrum—of these matrices acts as a critical delimiter for the stability boundaries of dynamical processes such as synchronization, consensus, and trust propagation. However, in the context of hypergraphs, this relationship is more complex than in traditional pairwise graphs.

In digital interaction hypergraphs, where interactions involve groups of arbitrary size (higher-order interactions), the "trust matrix" generalizes to a set of adjacency tensors or generalized Laplacian matrices. The stability of interaction forms (the specific mathematical rules governing node influence) is determined by a **Master Stability Function (MSF)** framework extended to simplicial complexes and hypergraphs. Within this framework, the stability region is defined by the coupling functions (interaction forms), while the specific state of a system is placed within or outside this region based on the eigenvalues (spectra) of the hypergraph's structural operators.

Therefore, while the spectral radius of a trust matrix (or its higher-order equivalent) does not solely define the stability boundary, it provides the necessary structural coordinate that must fall within the stable region defined by the interaction form. For linear consensus dynamics, the spectral radius strictly delimits stability (e.g., $\rho < 1$ for error decay). For non-linear synchronization, the spectral radius often defines the critical coupling strength required to enter or exit a stable synchronized state.

**Key Points:**
*   **Generalization to Hypergraphs:** Digital interactions often involve multi-party relationships best modeled by hypergraphs or simplicial complexes rather than simple graphs. In these structures, trust and influence propagate through higher-order connections (e.g., three-body or $d$-body interactions) [cite: 1, 2].
*   **Spectral Determinants of Stability:** The stability of collective states (synchronization, consensus) is mathematically conditioned on the eigenvalues of generalized Laplacian matrices or adjacency tensors. The spectral radius represents the extreme mode of the network structure and typically sets the threshold for the onset of instability or the necessary coupling strength for stability [cite: 1].
*   **Role of Trust Matrices:** In dynamics like belief propagation or federated learning, the trust matrix functions as a transition or weight matrix. Its spectral radius directly dictates the convergence rate and the boundary between stable consensus and divergence [cite: 3, 4].
*   **Interaction Forms:** The functional form of the interaction (e.g., linear diffusive, Kuramoto sine-coupling) determines the shape of the stability region. The spectral properties of the hypergraph determine whether the system resides within that region [cite: 5, 6].

---

## 1. Introduction

The modeling of complex digital ecosystems—ranging from social networks and the Metaverse to the Internet of Things (IoT) and decentralized finance—has increasingly shifted from traditional graph theory to **hypergraph theory**. While graphs capture pairwise relationships (dyadic interactions), hypergraphs allow for the representation of **higher-order interactions** where an edge (hyperedge) can connect an arbitrary number of nodes simultaneously. This shift is crucial for accurately capturing phenomena such as group chats, conference calls, multi-party smart contracts, and collaborative teams [cite: 7, 8, 9].

Within these systems, **trust matrices** quantify the reliability, influence, or weight assigned to interactions between agents. The question of whether the **spectral radius** of these matrices delimits the **stability boundary** of interaction forms is central to understanding the robustness and safety of digital systems. Stability in this context refers to the ability of the system to maintain a coherent state (such as synchronization of data, consensus on a ledger, or stable trust propagation) in the face of perturbations.

This report provides an exhaustive analysis of the interplay between spectral theory, hypergraph topology, and dynamical stability. It synthesizes findings from control theory, network science, and digital trust modeling to establish how spectral radii serve as critical delimiters in the stability landscape of higher-order digital interactions.

---

## 2. Theoretical Foundations

### 2.1 Digital Interaction Hypergraphs
A **hypergraph** $H = (V, E)$ consists of a set of vertices $V$ and a set of hyperedges $E$, where each hyperedge $e \in E$ is a subset of $V$ with arbitrary cardinality $|e| \ge 2$. In digital interactions:
*   **Nodes ($V$):** Represent users, devices, sensors, or autonomous agents.
*   **Hyperedges ($E$):** Represent interactions such as a group message, a shared transaction, or a co-location event [cite: 7, 8].

Unlike simple graphs, hypergraphs can model **simplicial complexes**, which are hypergraphs closed under the inclusion of subsets (i.e., if a group interacts, all subgroups are also considered to interact). This distinction is vital because the mathematical tools for analyzing stability (e.g., Hodge Laplacians) are often developed for simplicial complexes [cite: 1, 2].

### 2.2 Trust Matrices in Digital Systems
A **trust matrix** $T$ (or $W$) typically represents the weighted relationships between agents.
*   **Entry $T_{ij}$:** Represents the degree of trust agent $i$ places in agent $j$, or the influence $j$ has on $i$.
*   **Properties:** These matrices are often row-stochastic (rows sum to 1) in consensus models, or they may be adjacency matrices in structural analysis.
*   **Higher-Order Trust:** In hypergraphs, trust may be defined not just between pairs, but towards groups (hyperedges). This leads to tensor representations of trust, $\mathcal{T}$, where an entry $\mathcal{T}_{ijk}$ might represent the joint trust in a collaborative triangle [cite: 2, 10].

### 2.3 Spectral Radius and Stability
The **spectral radius** $\rho(A)$ of a matrix $A$ is defined as the maximum absolute value of its eigenvalues: $\rho(A) = \max_i |\lambda_i|$.
In linear dynamical systems ($x_{t+1} = T x_t$), the condition $\rho(T) < 1$ is necessary and sufficient for asymptotic stability (convergence to zero). In continuous coupled systems ($\dot{x} = f(x) + \sigma \sum A_{ij} h(x_j)$), the eigenvalues of the coupling matrix $A$ (specifically the Laplacian $L$) determine stability via the Master Stability Function [cite: 1].

---

## 3. Stability Analysis in Hypergraph Dynamical Systems

The stability of interaction forms in hypergraphs is not governed by a single scalar value but by the spectra of operators that describe the geometry of interactions at different orders.

### 3.1 The Master Stability Function (MSF) for Simplicial Complexes
Recent research has generalized the Master Stability Function (MSF) to simplicial complexes and hypergraphs. This framework allows for the analysis of coupled dynamical systems with interactions at multiple orders (pairwise, three-body, etc.).

The dynamics of a node $i$ in a simplicial complex can be described as:
$$ \dot{\mathbf{x}}_i = \mathbf{f}(\mathbf{x}_i) + \sigma_1 \sum_{j=1}^N a_{ij}^{(1)} \mathbf{g}^{(1)}(\mathbf{x}_i, \mathbf{x}_j) + \sigma_2 \sum_{j,k=1}^N a_{ijk}^{(2)} \mathbf{g}^{(2)}(\mathbf{x}_i, \mathbf{x}_j, \mathbf{x}_k) + \dots $$
Here, $a_{ij}^{(1)}$ are entries of the standard adjacency matrix, and $a_{ijk}^{(2)}$ are entries of the adjacency tensor for 2-simplexes (triangles) [cite: 1, 2].

**Stability Condition:**
The stability of the synchronized state is determined by the variational equations, which decouple into independent modes diagonalized by the generalized Laplacian matrices.
*   The stability is governed by the **eigenvalues** of the Laplacian matrices associated with each interaction order ($L^{(1)}, L^{(2)}, \dots$).
*   The **Master Stability Function** relates these eigenvalues to the Lyapunov exponents of the dynamics.
*   **Conclusion:** The spectral radius (and the entire spectrum) of the generalized Laplacian matrices delimits the stability boundary. Specifically, for a given interaction form $\mathbf{g}^{(d)}$, there exists a region of stability $\mathcal{R}$ in the complex plane. The system is stable if and only if the relevant eigenvalues (scaled by coupling strengths $\sigma_d$) fall within $\mathcal{R}$ [cite: 1].

### 3.2 Generalized Laplacians and Adjacency Tensors
In hypergraphs, the "trust matrix" concept expands to **adjacency tensors**.
*   **Adjacency Tensor $\mathcal{A}^{(d)}$:** Describes interactions of order $d$.
*   **Generalized Laplacian:** Can be defined for each order. For example, the standard Laplacian $L^{(1)}$ captures diffusion over links. Higher-order Laplacians capture diffusion over triangles or tetrahedra.
*   **Spectral Radius Role:** The spectral radius of these operators determines the timescale of the fastest converging (or diverging) modes. In synchronization, a larger spectral radius of the Laplacian typically implies a stronger coupling effect, which can either stabilize (by pushing the system into the synchronization manifold) or destabilize (by pushing it into an instability region, e.g., in systems with limited stability intervals like the Rössler oscillator) [cite: 1].

### 3.3 Simultaneous Block Diagonalization
For systems with multiple types of interactions (e.g., a hypergraph with both pairwise and three-body trust links), stability analysis requires **Simultaneous Block Diagonalization (SBD)** of the matrices representing these interactions.
*   If the interaction matrices (trust matrices at different orders) commute, they share a common eigenvector basis.
*   If they do not commute, SBD is used to decouple the variational equation into lower-dimensional blocks.
*   **Significance:** The stability boundary is delimited not just by the spectral radius of a single matrix, but by the joint spectral properties of the set of matrices defining the hypergraph topology [cite: 11].

---

## 4. Trust Dynamics and Spectral Bounds

In digital ecosystems, "trust" is often a dynamic variable that evolves over time or a static weight that governs consensus.

### 4.1 Consensus and Belief Propagation
In models where agents update their beliefs or trust scores based on neighbors (e.g., DeGroot model, consensus algorithms), the system evolves as $\mathbf{x}(t+1) = W \mathbf{x}(t)$, where $W$ is the trust/weight matrix.
*   **Convergence:** Convergence to a consensus value requires that the spectral radius of the error transition matrix is less than 1 (or that the second largest eigenvalue modulus is $<1$ for the stochastic matrix itself).
*   **Hypergraph Consensus:** On hypergraphs, consensus dynamics involve non-linear averaging functions or higher-order Laplacians. Research indicates that the convergence rate is dictated by the **spectral radius of the hypergraph Laplacian** or the projected matrix derived from the hypergraph structure [cite: 12].
*   **Trust Matrices:** In federated learning, trust matrices weight the contributions of different nodes. The spectral radius of the trust matrix determines the stability of the learning process and the boundary between converging to a true model or diverging due to malicious inputs [cite: 3].

### 4.2 Trust Propagation in Social IoT
In the Social Internet of Things (SIoT), trust is computed using direct and indirect trust matrices.
*   **Direct Trust:** Based on direct interactions.
*   **Indirect Trust:** Propagated through the network.
*   **Stability:** The stability of the trust evaluation system—ensuring that trust scores do not oscillate wildly or diverge—depends on the damping factors and the spectral properties of the propagation matrix. If the spectral radius of the propagation influence matrix exceeds unity, trust values can amplify unboundedly (echo chamber effect). Algorithms typically normalize these matrices (e.g., row-stochastic) to ensure $\rho(W) = 1$ and stability [cite: 10, 13, 14].

### 4.3 Spectral Radius as a Stability Delimiter
Research explicitly links the spectral radius to stability boundaries in these contexts:
*   **Epidemic Spreading on Hypergraphs:** The epidemic threshold (a stability boundary for the disease-free equilibrium) is inversely proportional to the spectral radius of the hypergraph's adjacency tensor/matrix [cite: 15].
*   **Synchronization:** The "unbounded" or "bounded" nature of the stable region in the MSF means that the spectral radius (largest eigenvalue) determines if the system crosses the threshold into stability (for unbounded regions) or passes through it into instability (for bounded regions) [cite: 1].

---

## 5. Interaction Forms and Stability Boundaries

The "interaction form" refers to the mathematical function coupling the nodes (e.g., linear diffusive, sine coupling, non-linear chemical synapse). The spectral radius of the trust matrix interacts with this form to define stability.

### 5.1 Pairwise vs. Higher-Order Interactions
*   **Pairwise (Linear):** Stability is often monotonic with respect to the spectral radius (coupling strength $\times$ eigenvalue).
*   **Higher-Order (Non-linear):** Interaction forms in hypergraphs (e.g., $g^{(2)}(x_i, x_j, x_k)$) introduce non-linearities that can create **multistability** and **explosive transitions**.
    *   Research shows that higher-order interactions can induce abrupt desynchronization transitions, which are not observed in pairwise Kuramoto models. The stability boundary for these transitions is defined by the interplay between the coupling strength and the higher-order structural eigenvalues [cite: 5, 16].
    *   **Phase Reduction:** When reducing high-dimensional hypergraph dynamics to phase models (Kuramoto-like), higher-order terms emerge naturally. The stability of the synchronized state in these reduced models is analytically derived and depends on the critical values of coupling strengths, which are scaled by the hypergraph's structural properties (degrees/eigenvalues) [cite: 5, 17].

### 5.2 The Role of the Coupling Function
The Master Stability Function $\Lambda(\alpha)$ maps a complex parameter $\alpha$ (related to the eigenvalue) to a stability index (Lyapunov exponent).
*   **Stability Region:** The set of $\alpha$ for which $\Lambda(\alpha) < 0$.
*   **Delimiting the Boundary:** The spectral radius $\lambda_{max}$ of the trust/adjacency matrix determines the maximum effective coupling $\sigma \lambda_{max}$.
    *   If the stability region is **unbounded** (e.g., $(c, \infty)$), then stability requires $\sigma \lambda_{2} > c$. Here, the *second* largest eigenvalue (algebraic connectivity) is the delimiter for the *onset* of stability.
    *   If the stability region is **bounded** (e.g., $(c_1, c_2)$), then the spectral radius $\lambda_{max}$ acts as a delimiter for the *loss* of stability. If $\sigma \lambda_{max} > c_2$, the system becomes unstable (over-coupling instability) [cite: 1].

---

## 6. Applications in Digital Ecosystems

### 6.1 The Metaverse and Digital Twins
In the Metaverse, digital interactions form a complex hypergraph of users, assets, and environments. Trust matrices manage security and authentication.
*   **Stability:** Ensuring stable rendering and interaction requires that the update dynamics (governed by the network of interactions) remain stable. The spectral radius of the interaction matrix serves as a check for numerical stability and convergence of distributed simulations [cite: 18, 19].

### 6.2 Blockchain and Consensus
Blockchain networks rely on consensus algorithms (e.g., PBFT, PoS) which can be modeled as belief propagation on a hypergraph (validators voting on blocks).
*   **Trust Matrices:** Validators assign trust weights to peers.
*   **Stability Boundary:** The system is stable (reaches consensus) if the trust matrix allows for the rapid decay of disagreement. This is guaranteed if the spectral radius of the non-consensus modes is strictly less than 1. Malicious actors attempting to destabilize the network effectively try to manipulate the trust matrix to push this spectral radius towards or above 1 [cite: 3, 12].

### 6.3 Recommender Systems
Graph Neural Networks (GNNs) and hypergraph learning are used in recommender systems (e.g., TrustMF, TrustGraph-Rec).
*   **Stability:** In the context of learning algorithms (e.g., GCNs), the spectral radius of the normalized Laplacian determines the numerical stability of the propagation layers (preventing exploding gradients). Trust matrices are used to calibrate these propagations. A spectral radius $>1$ in the propagation step would lead to numerical instability [cite: 20, 21, 22].

---

## 7. Discussion: Does Spectral Radius Delimit the Boundary?

Based on the synthesized research, the answer is **Yes**, but it acts as a **structural coordinate** rather than the sole determinant.

1.  **Necessary Condition:** For a wide class of interaction forms (especially those satisfying the MSF conditions), the stability of the synchronized or consensus state requires that the eigenvalues of the trust/interaction matrix (scaled by coupling strength) lie within a specific region. The spectral radius, being the extremal eigenvalue, defines the outer limit of the system's structural influence.
2.  **Interaction Form Dependency:** The *shape* and *existence* of the stability boundary are determined by the interaction form (the function $\mathbf{g}$). The spectral radius determines *where* the specific network instance sits relative to that boundary.
3.  **Hypergraph Complexity:** In hypergraphs, "spectral radius" refers to the spectra of a family of operators (generalized Laplacians). Stability might be delimited by the spectral radius of the 1-mode Laplacian, the 2-mode Laplacian, or a combination, depending on which interaction orders are active and dominant [cite: 1].
4.  **Dynamic Trust:** If the trust matrix itself evolves (adaptive networks), the spectral radius becomes a time-dependent parameter. Stability then requires that the spectral radius remains within the stable region over time, or that its excursion outside is brief enough not to break the basin of attraction [cite: 3, 23].

---

## 8. Conclusion

In digital interaction hypergraphs, the spectral radius of trust matrices (and their higher-order generalizations) plays a definitive role in delimiting the stability boundary of interaction forms. It serves as the critical link between the **topology** of the digital ecosystem (who trusts whom, and in what groups) and the **dynamics** of the interactions (how influence propagates).

*   **For Synchronization:** The spectral radius of the generalized Laplacian determines if the coupling is strong enough to synchronize the hypergraph or too strong, leading to instability.
*   **For Consensus/Trust Propagation:** The spectral radius of the trust transition matrix strictly delimits the boundary between convergence (stability) and divergence (instability).
*   **For Higher-Order Dynamics:** The stability boundaries are multidimensional, defined by the joint spectra of tensors representing different interaction orders.

Thus, analyzing the spectral radius is a fundamental step in certifying the stability of any complex digital interaction system, from secure blockchain consensus to robust social networking in the Metaverse.

---

## References

*   **[cite: 1, 24, 25]** Gambuzza, L. V., et al. "Stability of synchronization in simplicial complexes." *Nature Communications*, 2021. (Establishes the MSF for hypergraphs and the role of generalized Laplacian eigenvalues).
*   **[cite: 2]** Millán, A. P., et al. "Explosive synchronization in simplicial complexes." *Physical Review Letters*, 2020. (Discusses higher-order interactions and adjacency tensors).
*   **[cite: 3]** "Trust-based Consensus in Federated Learning." (Discusses spectral radius of trust matrices in consensus stability).
*   **[cite: 4]** "Models for the Diffusion of Beliefs in Social Networks." (Links spectral radius to convergence rate of belief/trust).
*   **[cite: 12]** "Consensus on Hypergraphs." (Extends consensus dynamics and spectral conditions to hypergraphs).
*   **[cite: 11]** "Unified treatment of synchronization patterns in generalized networks." (Simultaneous block diagonalization for stability analysis).
*   **[cite: 5, 17]** "Theory of phase reduction from hypergraphs to simplicial complexes." (Derives stability boundaries for phase models on hypergraphs).
*   **[cite: 21, 22]** "TrustMF: A Social Recommendation Approach." (Trust matrices in recommender systems).
*   **[cite: 7, 8]** "Spatial Interaction Hypergraphs." (Context of digital/spatial interactions).
*   **[cite: 16]** "Stability of synchronization in simplicial complexes" (IEEE JAS reference).
*   **[cite: 15]** "Approximation algorithms for reducing the spectral radius to control epidemic spread." (Spectral radius as stability threshold for spreading processes).

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElty-jt_xjwTSsrdpACYkOgzDp30NkNrcKAejJwwxiI1d0grHZEwpCZNWB_vau4LlWjSQkA3TPMA0YuZG84vsvLjgYVHhS-gwl90PWvqLmzy1RAvJ7xNEcd6RG098lhGqwgvnfkWrgzVI7fygI4-_wWXYCUg6IflLQQYcTZWYB_te_rwX5P2SwscrNJslm_cbndFogFom7KQCYdO0=)
2. [cnr.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbsOpkoDfuZ9DJfxBtrBpzVNaaF7mHYrjH5RNjVmZjVN0HE3WYFZFGEzxMLg-9eGrwVvJ1TPidsRPZ7n7pw9urnAqSLD7ZHMPVmIT13DgQf4AWL3DnfaU89NZ0nK1XG5HZHh7xltVJ-YOiwA6QnSRlTjmXEdLXKg==)
3. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHh2pRl5Hgsb9EeTdoRjkKgp2HU9HagFi0sCfQ8ngSPtWH_KFrtEOPoBgjoysd-GoLK47dlsuNS90RoIPeDWfRL9E_AZUKMoXm5Cz2IkV95IRhEiNZw)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgMon1cgsmoiwKKkqF7E84DIWEG5bo0ujhkWIGU5i3jFRfZE9TKefwMhrqVEUXlXhyYamiTiza9QO_Q2XTuFyl3TWxQj1UJL5i65mAazJ5NHmZFFbv62UI2FBY6QpovfDg79n0ZJxS_RY0HOK_KRy4Ky-ieD8pZ-TlI3mVzmnTcb7kPB4zVvJgGhz0pVx3kBVE41EBlUtJBJ7M1xsecsEAStD8-8933qtI9g==)
5. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHELe289tCD-SKLjnqusRcUXfDMs7mr8xNEIDMgb6NvqaCoBzJnQR9av2OJ9Rkrx0qOpeSqrr7ifrGUAnD8iLHyY0L3Jg_-qFP0tDFgnE0AF7_4Y6zJ)
6. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdVs2oxmxaXwCR697oB1_iqibznBbKg8uSGoV7aHcGl3tChUWTgwAi4tIUv-b40llNXRBGWwA-rnRY-Ib48OYw7R193nhEDLBP9Sq8SeJEKU4RzGvchkzsZewHnWrgT5jsdhp34t9ApZrNfbr-69wXVIIdPVr2YvlpxmHsjd06DRNzG5KWWHB-te4xI22mC4jFten5xVn5PARi0Q==)
7. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnSkYIlRBRC4COhRMuZPudUJhpLQKvfFObqFzUOzKRVndluoyBwuttqeXiIKtI4EtR6XbgVMcpppxaQqnUDEikSeCwW2s4FRPfr2qTKURIV3styRKXY4A40WFZPrVSXLHpqi1IoJExxjw5edR2877AJc1ak9AW1A==)
8. [polyu.edu.hk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTo4ZIFaE_PpGVCJ_fgOUv7zmT6hIY1c1RAJfXqkAtHD7Hx3e_pKa_cDmRSLL6laNoQT4PKRZ3z2XJIGiiZn1qQ1y-OuVQVuFOcuO2WjZNQCSyls-GR6kRoa6xMvJJlw-uEYeLCEvGQQQbDmF1Q2GuU72G_RVRY8qc0dssa1iWVMZa_SQn2Y7P6Huqy5Fu)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGO4F9LDtieRg16z539lu6sSr1_GrKJAJvfeCVQ_jLd2UhW-wLjII7a7h5Ofwng9KLLCQb4F0V1r4-KJntzB1Nqew3jc_uU6n65vA7shaAfWPn9yaxa2y9GYcj422lnJnWtA-ScKz0yjr6wkwTSO8aA4CSy0_AuiYR0UUjYOPKu1s9o5b2joQuc-uVZags-eYps2KZbvc8YJ98-f50P7yTNHnI6bpBlgqOI0PJ6359Td8lgYIPb7QLw0yK3)
10. [thescipub.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4XYdt6oV4StLYYRDj1mhFnk5BteZbXMcqJNjQBAoZqpDpdT8ti43JNM1bsYxgp1AXVyakVUztIFFi-5waCz-Dpvmk7h4FtNVnj_lZq1hQMFjqQIBTGyiDzF8v2w63r--cS9sizQ==)
11. [qmul.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcoDjcC0APbnaJSG0eoyV_ZC6W0NP3cVDbDHycsZwgG2GD5dG1N10jNXPh8kUP0NxgC3JPuM9IGMcw2EssWdIJXfrBydcREKqOZFkrK2k-OdBebAUIojkYI058aL-nfMn_k7lQ2O6aj8yOGbZDNez2RlXHE2_zGzI91OSZ7xllpDsmkyiJuGPzXO7i1gV7FxCqxi4uDAmXk8l8q1DMuudZhBaujpVJGMSMeRowvPkRuzSRurHB2Pn4)
12. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiiKnvS20uLRYOv9qgzlndNbpeoDgyZPf9JHEJXaP_ksPL7TvqfKmWEakJM5SnkvXUfHDritt662rNbJs7vwks_RiXZZymUtP5rEXypr3eyiS6Pw8t)
13. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRmVEDdnCtN128sDvQrMVSSBitRoN6zRA-XsznZFlBwb9PizI0p8nZ1urnanhNfB_euAosT1BRcF9dumpcrfUal6W3xMXtRqByGzsJFs9AfnSBzMjgpuHCFW5PzU77RgAq9CgSTLqbejLOhlY4Mt8_L5c=)
14. [dokumen.pub](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEow2xnxMJCiCTm8erwKxtCNquTgYgNihyuXhbS2zzu-gdzFdQ9gN2MVmGOZxszNloiDtu7BYL_eJLtg8xKwZT06qPNYn94ChGKfbUCSDWIUuyvbUF1SvcVY6xj8_yDCUMA71CiriIWR9MDd-RFZO7-q_J1OhcN_I9VRICrvbLjdNnyktd6_JjKmRnX33Qog8uS97tvWUV4rNiPRYbUxXpiELWEO2PVOGQZj4iS787g8YQy7rTiBG0ZP-UrXybNZRAsf_wRZQ-L23R8jJwPAojh)
15. [esaim-m2an.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIL1_XZs8SSfKEhxP9ocjI3hWl_mGxvoEDDXvNIFlo1DiPzoMTatAL4iWnLJH_Y8bQyHMQeiMLuvsZSA-OHncmdd6A2iOFZMXU2DTSmrMB_hcbtzcmUMEC4CA_0X4AA6oAhqaIm4ri95g2ybkW6YZ8RUOQzaHZmcM=)
16. [ieee-jas.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQVN8w8EgXv625ZVcZakOSCifl5cKE7Jq_4Kdr8fNQWBHifoTYbln7OK-Ig2Spo64S77TfU228XqlejxTwcTB7KE78yFtfJf8zmG7vGgwYZkO_apOLbZVTjTdpOa0DJIUmVQL9pueZOId2DvifjKQ2QQ==)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPRxMrUaGXEm9J3ZVfWeX0HBsfPnzj1vcgLGRZihdgbkOHrRx4pRwnFBG7ShL6tTWnrohjQKYHG_dQnBmcecqSMYvR-Cp2Q_uoxz4UjebVpaMSsfCX-LxrBvhxxV_luAP0UFz342cNUQ4Ef2YnBijtxEFOl2MVNORLKpw_R0kBSwydj97X1uweL9-ej8r7ZvvP-TELzNHRLX2KpyiQgSsVIAGet5pfljMbwZM4TRRU6_GGHGDvjgnkVJ86BY8mUeW68KjSaqWjlyriNPhye-prhuxOrg9f5AaYBo0=)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5J-M7KOy49leTemIPOEHgjm2s-Bx1p85Cf3Xc0S2UTP-4aiKAbiM4tEznqNW2HyqCSb5N3yCbDkV_EINdubPL9quJEX3kpiPOO3t3eGAnh3nRAyWWuUPhHop9XpL-B8rx3llxiTcuaQpFJAxIaNT0JNA6xbLru36ACvHCe8NWlPSN1GaVCVfrIPi2AVI0BGTfrcRPi16bDdqrl3GGfnZdTw==)
19. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoUlbM3DORFbiQVZHt03cNzh6AA10X-jNmRfv06YUeYLKaSvZxYL_uknAlYZDNP-MOgv8Tei-Zj5KI97tF-LKHsmRZj-BUl10EMxbJC_iVX1O4oc42oB6UilvrCTRprsa7h1TC0REgJSzPy1I2PlpqLP8P)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzbzazwSk11YNV6r7eu3Ey3mUqj3d91k_i7HwJ-hGEY-iGPBHwCrg9FJ2wIGzLZFZrH5758E2V7YfQM1p0kv2sKtlaEQkZws_MTTWhFJQRbf1gE1-xaXcir3LewdRTF-Dw6f-XGYxYB9eUuMSoNwSvazdyy9UhnR_G65gLxr7b3V4Uw6DU0cYJlSIgPBxrEyZw8kKJ8yV5h2WCzgEF1PvncC-Ja6Oot1_mnii63d8ob_AJ_NqwpwKbABnC_34fVgoM-mKe41UbqNjqOdpf)
21. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE60MWlVjVuoKzyAyEOCGQi99DSl5PrT3gw9nwdZv1M2Cv9XZSmWhn_EkObCvzr0EU5fnWufP7w-mAVhrA0bgS_zjfDFX_dhp9eJWQjDyeelqju2OZjoOghBIrZsPY=)
22. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbTlQ1TuLY-AG6fCBFXkXS5mbCR_vcKoWZ_6e_vI_qEfgV4oQjiHX50-WeGXk1hgzlN6U9HaEF8Hhw-mZtaJve_2OP2am7Hu6k-osvCRa-yG2AgEyb)
23. [scl.rs](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEipFS-Uxt7ugN9eQozBTxRRiTuIERPpT1PzDziNdaJGuc37n56EEvxU3yT5ya9_Oo-h2LSFfuDN489rEwSa6CruEFs2KiDNy4CC8ZujrJajeXUsmHkrQ1YzX6tPYWN2uu4I_rXDU67qMUBBrIBHA==)
24. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiD0PhPjGY7aqR7Wv3nhn6VPmz6SWS6PMEvYxzAGABFrLPJf2t5qdQb13xeksfR2D5T5164nV6PKv4IErWwezty0im7FZzdhnt4QKKW35ZMu5YVL7lhDZ1RToZfvTtwfn4iEabBTXu8K-LAAD3Ihl0CfIm7HQuQsoiXPusdLmr3mPxZiD5ZQBiZt6Se7hvCWl4)
25. [unamur.be](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgJy3tNCHnWnRbl9tp00HN08_4J0yW0wvzq95gaCXOrAgdJnWFJzuJH19lwO6ijNLYJS_w1UiBU2C8EH6lxE77H5Qhd1EkdbTm4Fv-C2ELUbe-0eu8V5FoJimn02g7QjYSgW9jmDSxhora0dBC1TdQIImd5LEIaERKYtUDJ5LAhwUl212JAcoddvg2e6PzYaiXOMlTyPdsyYy2dg==)


## Annotations
Annotation(end_index=2244, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElty-jt_xjwTSsrdpACYkOgzDp30NkNrcKAejJwwxiI1d0grHZEwpCZNWB_vau4LlWjSQkA3TPMA0YuZG84vsvLjgYVHhS-gwl90PWvqLmzy1RAvJ7xNEcd6RG098lhGqwgvnfkWrgzVI7fygI4-_wWXYCUg6IflLQQYcTZWYB_te_rwX5P2SwscrNJslm_cbndFogFom7KQCYdO0=', start_index=2232)
Annotation(end_index=2244, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbsOpkoDfuZ9DJfxBtrBpzVNaaF7mHYrjH5RNjVmZjVN0HE3WYFZFGEzxMLg-9eGrwVvJ1TPidsRPZ7n7pw9urnAqSLD7ZHMPVmIT13DgQf4AWL3DnfaU89NZ0nK1XG5HZHh7xltVJ-YOiwA6QnSRlTjmXEdLXKg==', start_index=2232)
Annotation(end_index=2652, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElty-jt_xjwTSsrdpACYkOgzDp30NkNrcKAejJwwxiI1d0grHZEwpCZNWB_vau4LlWjSQkA3TPMA0YuZG84vsvLjgYVHhS-gwl90PWvqLmzy1RAvJ7xNEcd6RG098lhGqwgvnfkWrgzVI7fygI4-_wWXYCUg6IflLQQYcTZWYB_te_rwX5P2SwscrNJslm_cbndFogFom7KQCYdO0=', start_index=2643)
Annotation(end_index=2934, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgMon1cgsmoiwKKkqF7E84DIWEG5bo0ujhkWIGU5i3jFRfZE9TKefwMhrqVEUXlXhyYamiTiza9QO_Q2XTuFyl3TWxQj1UJL5i65mAazJ5NHmZFFbv62UI2FBY6QpovfDg79n0ZJxS_RY0HOK_KRy4Ky-ieD8pZ-TlI3mVzmnTcb7kPB4zVvJgGhz0pVx3kBVE41EBlUtJBJ7M1xsecsEAStD8-8933qtI9g==', start_index=2922)
Annotation(end_index=2934, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHh2pRl5Hgsb9EeTdoRjkKgp2HU9HagFi0sCfQ8ngSPtWH_KFrtEOPoBgjoysd-GoLK47dlsuNS90RoIPeDWfRL9E_AZUKMoXm5Cz2IkV95IRhEiNZw', start_index=2922)
Annotation(end_index=3207, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdVs2oxmxaXwCR697oB1_iqibznBbKg8uSGoV7aHcGl3tChUWTgwAi4tIUv-b40llNXRBGWwA-rnRY-Ib48OYw7R193nhEDLBP9Sq8SeJEKU4RzGvchkzsZewHnWrgT5jsdhp34t9ApZrNfbr-69wXVIIdPVr2YvlpxmHsjd06DRNzG5KWWHB-te4xI22mC4jFten5xVn5PARi0Q==', start_index=3195)
Annotation(end_index=3207, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHELe289tCD-SKLjnqusRcUXfDMs7mr8xNEIDMgb6NvqaCoBzJnQR9av2OJ9Rkrx0qOpeSqrr7ifrGUAnD8iLHyY0L3Jg_-qFP0tDFgnE0AF7_4Y6zJ', start_index=3195)
Annotation(end_index=3856, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnSkYIlRBRC4COhRMuZPudUJhpLQKvfFObqFzUOzKRVndluoyBwuttqeXiIKtI4EtR6XbgVMcpppxaQqnUDEikSeCwW2s4FRPfr2qTKURIV3styRKXY4A40WFZPrVSXLHpqi1IoJExxjw5edR2877AJc1ak9AW1A==', start_index=3841)
Annotation(end_index=3856, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGO4F9LDtieRg16z539lu6sSr1_GrKJAJvfeCVQ_jLd2UhW-wLjII7a7h5Ofwng9KLLCQb4F0V1r4-KJntzB1Nqew3jc_uU6n65vA7shaAfWPn9yaxa2y9GYcj422lnJnWtA-ScKz0yjr6wkwTSO8aA4CSy0_AuiYR0UUjYOPKu1s9o5b2joQuc-uVZags-eYps2KZbvc8YJ98-f50P7yTNHnI6bpBlgqOI0PJ6359Td8lgYIPb7QLw0yK3', start_index=3841)
Annotation(end_index=3856, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTo4ZIFaE_PpGVCJ_fgOUv7zmT6hIY1c1RAJfXqkAtHD7Hx3e_pKa_cDmRSLL6laNoQT4PKRZ3z2XJIGiiZn1qQ1y-OuVQVuFOcuO2WjZNQCSyls-GR6kRoa6xMvJJlw-uEYeLCEvGQQQbDmF1Q2GuU72G_RVRY8qc0dssa1iWVMZa_SQn2Y7P6Huqy5Fu', start_index=3841)
Annotation(end_index=5234, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnSkYIlRBRC4COhRMuZPudUJhpLQKvfFObqFzUOzKRVndluoyBwuttqeXiIKtI4EtR6XbgVMcpppxaQqnUDEikSeCwW2s4FRPfr2qTKURIV3styRKXY4A40WFZPrVSXLHpqi1IoJExxjw5edR2877AJc1ak9AW1A==', start_index=5222)
Annotation(end_index=5234, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTo4ZIFaE_PpGVCJ_fgOUv7zmT6hIY1c1RAJfXqkAtHD7Hx3e_pKa_cDmRSLL6laNoQT4PKRZ3z2XJIGiiZn1qQ1y-OuVQVuFOcuO2WjZNQCSyls-GR6kRoa6xMvJJlw-uEYeLCEvGQQQbDmF1Q2GuU72G_RVRY8qc0dssa1iWVMZa_SQn2Y7P6Huqy5Fu', start_index=5222)
Annotation(end_index=5607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElty-jt_xjwTSsrdpACYkOgzDp30NkNrcKAejJwwxiI1d0grHZEwpCZNWB_vau4LlWjSQkA3TPMA0YuZG84vsvLjgYVHhS-gwl90PWvqLmzy1RAvJ7xNEcd6RG098lhGqwgvnfkWrgzVI7fygI4-_wWXYCUg6IflLQQYcTZWYB_te_rwX5P2SwscrNJslm_cbndFogFom7KQCYdO0=', start_index=5595)
Annotation(end_index=5607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbsOpkoDfuZ9DJfxBtrBpzVNaaF7mHYrjH5RNjVmZjVN0HE3WYFZFGEzxMLg-9eGrwVvJ1TPidsRPZ7n7pw9urnAqSLD7ZHMPVmIT13DgQf4AWL3DnfaU89NZ0nK1XG5HZHh7xltVJ-YOiwA6QnSRlTjmXEdLXKg==', start_index=5595)
Annotation(end_index=6314, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4XYdt6oV4StLYYRDj1mhFnk5BteZbXMcqJNjQBAoZqpDpdT8ti43JNM1bsYxgp1AXVyakVUztIFFi-5waCz-Dpvmk7h4FtNVnj_lZq1hQMFjqQIBTGyiDzF8v2w63r--cS9sizQ==', start_index=6301)
Annotation(end_index=6314, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbsOpkoDfuZ9DJfxBtrBpzVNaaF7mHYrjH5RNjVmZjVN0HE3WYFZFGEzxMLg-9eGrwVvJ1TPidsRPZ7n7pw9urnAqSLD7ZHMPVmIT13DgQf4AWL3DnfaU89NZ0nK1XG5HZHh7xltVJ-YOiwA6QnSRlTjmXEdLXKg==', start_index=6301)
Annotation(end_index=6868, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElty-jt_xjwTSsrdpACYkOgzDp30NkNrcKAejJwwxiI1d0grHZEwpCZNWB_vau4LlWjSQkA3TPMA0YuZG84vsvLjgYVHhS-gwl90PWvqLmzy1RAvJ7xNEcd6RG098lhGqwgvnfkWrgzVI7fygI4-_wWXYCUg6IflLQQYcTZWYB_te_rwX5P2SwscrNJslm_cbndFogFom7KQCYdO0=', start_index=6859)
Annotation(end_index=7912, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElty-jt_xjwTSsrdpACYkOgzDp30NkNrcKAejJwwxiI1d0grHZEwpCZNWB_vau4LlWjSQkA3TPMA0YuZG84vsvLjgYVHhS-gwl90PWvqLmzy1RAvJ7xNEcd6RG098lhGqwgvnfkWrgzVI7fygI4-_wWXYCUg6IflLQQYcTZWYB_te_rwX5P2SwscrNJslm_cbndFogFom7KQCYdO0=', start_index=7900)
Annotation(end_index=7912, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbsOpkoDfuZ9DJfxBtrBpzVNaaF7mHYrjH5RNjVmZjVN0HE3WYFZFGEzxMLg-9eGrwVvJ1TPidsRPZ7n7pw9urnAqSLD7ZHMPVmIT13DgQf4AWL3DnfaU89NZ0nK1XG5HZHh7xltVJ-YOiwA6QnSRlTjmXEdLXKg==', start_index=7900)
Annotation(end_index=8777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElty-jt_xjwTSsrdpACYkOgzDp30NkNrcKAejJwwxiI1d0grHZEwpCZNWB_vau4LlWjSQkA3TPMA0YuZG84vsvLjgYVHhS-gwl90PWvqLmzy1RAvJ7xNEcd6RG098lhGqwgvnfkWrgzVI7fygI4-_wWXYCUg6IflLQQYcTZWYB_te_rwX5P2SwscrNJslm_cbndFogFom7KQCYdO0=', start_index=8768)
Annotation(end_index=9686, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElty-jt_xjwTSsrdpACYkOgzDp30NkNrcKAejJwwxiI1d0grHZEwpCZNWB_vau4LlWjSQkA3TPMA0YuZG84vsvLjgYVHhS-gwl90PWvqLmzy1RAvJ7xNEcd6RG098lhGqwgvnfkWrgzVI7fygI4-_wWXYCUg6IflLQQYcTZWYB_te_rwX5P2SwscrNJslm_cbndFogFom7KQCYdO0=', start_index=9677)
Annotation(end_index=10408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcoDjcC0APbnaJSG0eoyV_ZC6W0NP3cVDbDHycsZwgG2GD5dG1N10jNXPh8kUP0NxgC3JPuM9IGMcw2EssWdIJXfrBydcREKqOZFkrK2k-OdBebAUIojkYI058aL-nfMn_k7lQ2O6aj8yOGbZDNez2RlXHE2_zGzI91OSZ7xllpDsmkyiJuGPzXO7i1gV7FxCqxi4uDAmXk8l8q1DMuudZhBaujpVJGMSMeRowvPkRuzSRurHB2Pn4', start_index=10398)
Annotation(end_index=11386, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiiKnvS20uLRYOv9qgzlndNbpeoDgyZPf9JHEJXaP_ksPL7TvqfKmWEakJM5SnkvXUfHDritt662rNbJs7vwks_RiXZZymUtP5rEXypr3eyiS6Pw8t', start_index=11376)
Annotation(end_index=11682, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHh2pRl5Hgsb9EeTdoRjkKgp2HU9HagFi0sCfQ8ngSPtWH_KFrtEOPoBgjoysd-GoLK47dlsuNS90RoIPeDWfRL9E_AZUKMoXm5Cz2IkV95IRhEiNZw', start_index=11673)
Annotation(end_index=12409, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEow2xnxMJCiCTm8erwKxtCNquTgYgNihyuXhbS2zzu-gdzFdQ9gN2MVmGOZxszNloiDtu7BYL_eJLtg8xKwZT06qPNYn94ChGKfbUCSDWIUuyvbUF1SvcVY6xj8_yDCUMA71CiriIWR9MDd-RFZO7-q_J1OhcN_I9VRICrvbLjdNnyktd6_JjKmRnX33Qog8uS97tvWUV4rNiPRYbUxXpiELWEO2PVOGQZj4iS787g8YQy7rTiBG0ZP-UrXybNZRAsf_wRZQ-L23R8jJwPAojh', start_index=12391)
Annotation(end_index=12409, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4XYdt6oV4StLYYRDj1mhFnk5BteZbXMcqJNjQBAoZqpDpdT8ti43JNM1bsYxgp1AXVyakVUztIFFi-5waCz-Dpvmk7h4FtNVnj_lZq1hQMFjqQIBTGyiDzF8v2w63r--cS9sizQ==', start_index=12391)
Annotation(end_index=12409, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRmVEDdnCtN128sDvQrMVSSBitRoN6zRA-XsznZFlBwb9PizI0p8nZ1urnanhNfB_euAosT1BRcF9dumpcrfUal6W3xMXtRqByGzsJFs9AfnSBzMjgpuHCFW5PzU77RgAq9CgSTLqbejLOhlY4Mt8_L5c=', start_index=12391)
Annotation(end_index=12775, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIL1_XZs8SSfKEhxP9ocjI3hWl_mGxvoEDDXvNIFlo1DiPzoMTatAL4iWnLJH_Y8bQyHMQeiMLuvsZSA-OHncmdd6A2iOFZMXU2DTSmrMB_hcbtzcmUMEC4CA_0X4AA6oAhqaIm4ri95g2ybkW6YZ8RUOQzaHZmcM=', start_index=12765)
Annotation(end_index=13077, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElty-jt_xjwTSsrdpACYkOgzDp30NkNrcKAejJwwxiI1d0grHZEwpCZNWB_vau4LlWjSQkA3TPMA0YuZG84vsvLjgYVHhS-gwl90PWvqLmzy1RAvJ7xNEcd6RG098lhGqwgvnfkWrgzVI7fygI4-_wWXYCUg6IflLQQYcTZWYB_te_rwX5P2SwscrNJslm_cbndFogFom7KQCYdO0=', start_index=13068)
Annotation(end_index=14058, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQVN8w8EgXv625ZVcZakOSCifl5cKE7Jq_4Kdr8fNQWBHifoTYbln7OK-Ig2Spo64S77TfU228XqlejxTwcTB7KE78yFtfJf8zmG7vGgwYZkO_apOLbZVTjTdpOa0DJIUmVQL9pueZOId2DvifjKQ2QQ==', start_index=14045)
Annotation(end_index=14058, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHELe289tCD-SKLjnqusRcUXfDMs7mr8xNEIDMgb6NvqaCoBzJnQR9av2OJ9Rkrx0qOpeSqrr7ifrGUAnD8iLHyY0L3Jg_-qFP0tDFgnE0AF7_4Y6zJ', start_index=14045)
Annotation(end_index=14450, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPRxMrUaGXEm9J3ZVfWeX0HBsfPnzj1vcgLGRZihdgbkOHrRx4pRwnFBG7ShL6tTWnrohjQKYHG_dQnBmcecqSMYvR-Cp2Q_uoxz4UjebVpaMSsfCX-LxrBvhxxV_luAP0UFz342cNUQ4Ef2YnBijtxEFOl2MVNORLKpw_R0kBSwydj97X1uweL9-ej8r7ZvvP-TELzNHRLX2KpyiQgSsVIAGet5pfljMbwZM4TRRU6_GGHGDvjgnkVJ86BY8mUeW68KjSaqWjlyriNPhye-prhuxOrg9f5AaYBo0=', start_index=14437)
Annotation(end_index=14450, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHELe289tCD-SKLjnqusRcUXfDMs7mr8xNEIDMgb6NvqaCoBzJnQR9av2OJ9Rkrx0qOpeSqrr7ifrGUAnD8iLHyY0L3Jg_-qFP0tDFgnE0AF7_4Y6zJ', start_index=14437)
Annotation(end_index=15380, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElty-jt_xjwTSsrdpACYkOgzDp30NkNrcKAejJwwxiI1d0grHZEwpCZNWB_vau4LlWjSQkA3TPMA0YuZG84vsvLjgYVHhS-gwl90PWvqLmzy1RAvJ7xNEcd6RG098lhGqwgvnfkWrgzVI7fygI4-_wWXYCUg6IflLQQYcTZWYB_te_rwX5P2SwscrNJslm_cbndFogFom7KQCYdO0=', start_index=15371)
Annotation(end_index=15919, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoUlbM3DORFbiQVZHt03cNzh6AA10X-jNmRfv06YUeYLKaSvZxYL_uknAlYZDNP-MOgv8Tei-Zj5KI97tF-LKHsmRZj-BUl10EMxbJC_iVX1O4oc42oB6UilvrCTRprsa7h1TC0REgJSzPy1I2PlpqLP8P', start_index=15905)
Annotation(end_index=15919, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5J-M7KOy49leTemIPOEHgjm2s-Bx1p85Cf3Xc0S2UTP-4aiKAbiM4tEznqNW2HyqCSb5N3yCbDkV_EINdubPL9quJEX3kpiPOO3t3eGAnh3nRAyWWuUPhHop9XpL-B8rx3llxiTcuaQpFJAxIaNT0JNA6xbLru36ACvHCe8NWlPSN1GaVCVfrIPi2AVI0BGTfrcRPi16bDdqrl3GGfnZdTw==', start_index=15905)
Annotation(end_index=16568, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHh2pRl5Hgsb9EeTdoRjkKgp2HU9HagFi0sCfQ8ngSPtWH_KFrtEOPoBgjoysd-GoLK47dlsuNS90RoIPeDWfRL9E_AZUKMoXm5Cz2IkV95IRhEiNZw', start_index=16555)
Annotation(end_index=16568, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiiKnvS20uLRYOv9qgzlndNbpeoDgyZPf9JHEJXaP_ksPL7TvqfKmWEakJM5SnkvXUfHDritt662rNbJs7vwks_RiXZZymUtP5rEXypr3eyiS6Pw8t', start_index=16555)
Annotation(end_index=17089, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE60MWlVjVuoKzyAyEOCGQi99DSl5PrT3gw9nwdZv1M2Cv9XZSmWhn_EkObCvzr0EU5fnWufP7w-mAVhrA0bgS_zjfDFX_dhp9eJWQjDyeelqju2OZjoOghBIrZsPY=', start_index=17071)
Annotation(end_index=17089, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzbzazwSk11YNV6r7eu3Ey3mUqj3d91k_i7HwJ-hGEY-iGPBHwCrg9FJ2wIGzLZFZrH5758E2V7YfQM1p0kv2sKtlaEQkZws_MTTWhFJQRbf1gE1-xaXcir3LewdRTF-Dw6f-XGYxYB9eUuMSoNwSvazdyy9UhnR_G65gLxr7b3V4Uw6DU0cYJlSIgPBxrEyZw8kKJ8yV5h2WCzgEF1PvncC-Ja6Oot1_mnii63d8ob_AJ_NqwpwKbABnC_34fVgoM-mKe41UbqNjqOdpf', start_index=17071)
Annotation(end_index=17089, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbTlQ1TuLY-AG6fCBFXkXS5mbCR_vcKoWZ_6e_vI_qEfgV4oQjiHX50-WeGXk1hgzlN6U9HaEF8Hhw-mZtaJve_2OP2am7Hu6k-osvCRa-yG2AgEyb', start_index=17071)
Annotation(end_index=18287, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElty-jt_xjwTSsrdpACYkOgzDp30NkNrcKAejJwwxiI1d0grHZEwpCZNWB_vau4LlWjSQkA3TPMA0YuZG84vsvLjgYVHhS-gwl90PWvqLmzy1RAvJ7xNEcd6RG098lhGqwgvnfkWrgzVI7fygI4-_wWXYCUg6IflLQQYcTZWYB_te_rwX5P2SwscrNJslm_cbndFogFom7KQCYdO0=', start_index=18278)
Annotation(end_index=18613, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEipFS-Uxt7ugN9eQozBTxRRiTuIERPpT1PzDziNdaJGuc37n56EEvxU3yT5ya9_Oo-h2LSFfuDN489rEwSa6CruEFs2KiDNy4CC8ZujrJajeXUsmHkrQ1YzX6tPYWN2uu4I_rXDU67qMUBBrIBHA==', start_index=18600)
Annotation(end_index=18613, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHh2pRl5Hgsb9EeTdoRjkKgp2HU9HagFi0sCfQ8ngSPtWH_KFrtEOPoBgjoysd-GoLK47dlsuNS90RoIPeDWfRL9E_AZUKMoXm5Cz2IkV95IRhEiNZw', start_index=18600)
Annotation(end_index=19820, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElty-jt_xjwTSsrdpACYkOgzDp30NkNrcKAejJwwxiI1d0grHZEwpCZNWB_vau4LlWjSQkA3TPMA0YuZG84vsvLjgYVHhS-gwl90PWvqLmzy1RAvJ7xNEcd6RG098lhGqwgvnfkWrgzVI7fygI4-_wWXYCUg6IflLQQYcTZWYB_te_rwX5P2SwscrNJslm_cbndFogFom7KQCYdO0=', start_index=19803)
Annotation(end_index=19820, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiD0PhPjGY7aqR7Wv3nhn6VPmz6SWS6PMEvYxzAGABFrLPJf2t5qdQb13xeksfR2D5T5164nV6PKv4IErWwezty0im7FZzdhnt4QKKW35ZMu5YVL7lhDZ1RToZfvTtwfn4iEabBTXu8K-LAAD3Ihl0CfIm7HQuQsoiXPusdLmr3mPxZiD5ZQBiZt6Se7hvCWl4', start_index=19803)
Annotation(end_index=19820, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgJy3tNCHnWnRbl9tp00HN08_4J0yW0wvzq95gaCXOrAgdJnWFJzuJH19lwO6ijNLYJS_w1UiBU2C8EH6lxE77H5Qhd1EkdbTm4Fv-C2ELUbe-0eu8V5FoJimn02g7QjYSgW9jmDSxhora0dBC1TdQIImd5LEIaERKYtUDJ5LAhwUl212JAcoddvg2e6PzYaiXOMlTyPdsyYy2dg==', start_index=19803)
Annotation(end_index=20038, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbsOpkoDfuZ9DJfxBtrBpzVNaaF7mHYrjH5RNjVmZjVN0HE3WYFZFGEzxMLg-9eGrwVvJ1TPidsRPZ7n7pw9urnAqSLD7ZHMPVmIT13DgQf4AWL3DnfaU89NZ0nK1XG5HZHh7xltVJ-YOiwA6QnSRlTjmXEdLXKg==', start_index=20029)
Annotation(end_index=20226, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHh2pRl5Hgsb9EeTdoRjkKgp2HU9HagFi0sCfQ8ngSPtWH_KFrtEOPoBgjoysd-GoLK47dlsuNS90RoIPeDWfRL9E_AZUKMoXm5Cz2IkV95IRhEiNZw', start_index=20217)
Annotation(end_index=20361, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgMon1cgsmoiwKKkqF7E84DIWEG5bo0ujhkWIGU5i3jFRfZE9TKefwMhrqVEUXlXhyYamiTiza9QO_Q2XTuFyl3TWxQj1UJL5i65mAazJ5NHmZFFbv62UI2FBY6QpovfDg79n0ZJxS_RY0HOK_KRy4Ky-ieD8pZ-TlI3mVzmnTcb7kPB4zVvJgGhz0pVx3kBVE41EBlUtJBJ7M1xsecsEAStD8-8933qtI9g==', start_index=20352)
Annotation(end_index=20499, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiiKnvS20uLRYOv9qgzlndNbpeoDgyZPf9JHEJXaP_ksPL7TvqfKmWEakJM5SnkvXUfHDritt662rNbJs7vwks_RiXZZymUtP5rEXypr3eyiS6Pw8t', start_index=20489)
Annotation(end_index=20615, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcoDjcC0APbnaJSG0eoyV_ZC6W0NP3cVDbDHycsZwgG2GD5dG1N10jNXPh8kUP0NxgC3JPuM9IGMcw2EssWdIJXfrBydcREKqOZFkrK2k-OdBebAUIojkYI058aL-nfMn_k7lQ2O6aj8yOGbZDNez2RlXHE2_zGzI91OSZ7xllpDsmkyiJuGPzXO7i1gV7FxCqxi4uDAmXk8l8q1DMuudZhBaujpVJGMSMeRowvPkRuzSRurHB2Pn4', start_index=20605)
Annotation(end_index=20771, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPRxMrUaGXEm9J3ZVfWeX0HBsfPnzj1vcgLGRZihdgbkOHrRx4pRwnFBG7ShL6tTWnrohjQKYHG_dQnBmcecqSMYvR-Cp2Q_uoxz4UjebVpaMSsfCX-LxrBvhxxV_luAP0UFz342cNUQ4Ef2YnBijtxEFOl2MVNORLKpw_R0kBSwydj97X1uweL9-ej8r7ZvvP-TELzNHRLX2KpyiQgSsVIAGet5pfljMbwZM4TRRU6_GGHGDvjgnkVJ86BY8mUeW68KjSaqWjlyriNPhye-prhuxOrg9f5AaYBo0=', start_index=20758)
Annotation(end_index=20771, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHELe289tCD-SKLjnqusRcUXfDMs7mr8xNEIDMgb6NvqaCoBzJnQR9av2OJ9Rkrx0qOpeSqrr7ifrGUAnD8iLHyY0L3Jg_-qFP0tDFgnE0AF7_4Y6zJ', start_index=20758)
Annotation(end_index=20928, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE60MWlVjVuoKzyAyEOCGQi99DSl5PrT3gw9nwdZv1M2Cv9XZSmWhn_EkObCvzr0EU5fnWufP7w-mAVhrA0bgS_zjfDFX_dhp9eJWQjDyeelqju2OZjoOghBIrZsPY=', start_index=20914)
Annotation(end_index=20928, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbTlQ1TuLY-AG6fCBFXkXS5mbCR_vcKoWZ_6e_vI_qEfgV4oQjiHX50-WeGXk1hgzlN6U9HaEF8Hhw-mZtaJve_2OP2am7Hu6k-osvCRa-yG2AgEyb', start_index=20914)
Annotation(end_index=21035, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnSkYIlRBRC4COhRMuZPudUJhpLQKvfFObqFzUOzKRVndluoyBwuttqeXiIKtI4EtR6XbgVMcpppxaQqnUDEikSeCwW2s4FRPfr2qTKURIV3styRKXY4A40WFZPrVSXLHpqi1IoJExxjw5edR2877AJc1ak9AW1A==', start_index=21023)
Annotation(end_index=21035, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTo4ZIFaE_PpGVCJ_fgOUv7zmT6hIY1c1RAJfXqkAtHD7Hx3e_pKa_cDmRSLL6laNoQT4PKRZ3z2XJIGiiZn1qQ1y-OuVQVuFOcuO2WjZNQCSyls-GR6kRoa6xMvJJlw-uEYeLCEvGQQQbDmF1Q2GuU72G_RVRY8qc0dssa1iWVMZa_SQn2Y7P6Huqy5Fu', start_index=21023)
Annotation(end_index=21132, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQVN8w8EgXv625ZVcZakOSCifl5cKE7Jq_4Kdr8fNQWBHifoTYbln7OK-Ig2Spo64S77TfU228XqlejxTwcTB7KE78yFtfJf8zmG7vGgwYZkO_apOLbZVTjTdpOa0DJIUmVQL9pueZOId2DvifjKQ2QQ==', start_index=21122)
Annotation(end_index=21228, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIL1_XZs8SSfKEhxP9ocjI3hWl_mGxvoEDDXvNIFlo1DiPzoMTatAL4iWnLJH_Y8bQyHMQeiMLuvsZSA-OHncmdd6A2iOFZMXU2DTSmrMB_hcbtzcmUMEC4CA_0X4AA6oAhqaIm4ri95g2ybkW6YZ8RUOQzaHZmcM=', start_index=21218)

## Sources
