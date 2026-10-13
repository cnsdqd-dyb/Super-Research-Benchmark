# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** c071cdc1 | **Time:** 672.88s | **Cost:** $3.11375
--------------------------------------------------------------------------------

# Spectral Determinants of Social Rigidity: Laplacian Eigenvalues and the Thresholds of Structural Solidification in Stratification Networks

### Key Points
*   **Spectral Definition of Mobility:** In social network analysis, mobility is mathematically quantified by the **spectral gap**—the difference between the largest and second-largest eigenvalues of the transition (or Laplacian) matrix. A large gap indicates high fluidity and rapid mixing, while a gap approaching zero signals "structural solidification," where the network fractures into non-communicating strata.
*   **The Threshold of Solidification:** The **Fiedler value** (algebraic connectivity), which corresponds to the second smallest eigenvalue of the Laplacian, acts as the critical threshold. When this value drops below a specific critical point, the network undergoes a phase transition from a connected component to a segregated, stratified system, effectively "solidifying" social classes.
*   **Cheeger’s Inequality as a Delimiter:** The thresholds of solidification are rigorously delimited by **Cheeger’s Inequality**, which bounds the "bottleneck" (conductance) of the social network using Laplacian eigenvalues. This mathematical relationship defines the minimum difficulty required to move between social strata.
*   **Empirical Application:** Recent econometric methodologies, such as the **Spectral Gap Mobility Index**, utilize these eigenvalues to measure intergenerational mobility. These indices have demonstrated that structural solidification is not merely a metaphor but a quantifiable topological feature of social graphs, where low mobility corresponds to specific spectral signatures.
*   **Sociological Implications:** Structural solidification represents a "trapped" state where the mixing time of the social dynamic exceeds the relevant timescale of the system (e.g., a human lifespan). This results in persistent inequality and the emergence of distinct, self-reinforcing communities or "cliques" that resist external integration.

---

## 1. Introduction

The study of social stratification—the hierarchical arrangement of individuals into socioeconomic strata—has traditionally relied on statistical measures of income elasticity and occupational transition matrices. However, the integration of **spectral graph theory** into sociological analysis has provided a rigorous mathematical framework for understanding the topology of inequality. The central query of this report concerns how the **Laplacian eigenvalues** of mobility functions delimit the thresholds of **structural solidification** in these networks.

Structural solidification refers to the process by which a social system loses its fluidity, resulting in rigid class boundaries that prevent the diffusion of capital, information, and individuals between strata [cite: 1, 2]. In network terms, this is analogous to a graph partitioning problem where the network becomes highly modular, trapping random walkers (individuals) within local clusters (social classes) for extended periods.

The **Laplacian matrix** of a graph, a fundamental tool in spectral graph theory, encodes the connectivity and diffusion properties of the network. Its eigenvalues, particularly the **spectral gap** and the **algebraic connectivity** (Fiedler value), serve as precise metrics for the rate of convergence to a steady state [cite: 3, 4]. This report argues that these eigenvalues do not merely describe the network but actively delimit the thresholds of solidification: they define the critical values at which a cohesive society fractures into disparate, non-interacting components. By analyzing the spectral properties of mobility functions, we can mathematically identify the "tipping points" where social mobility effectively ceases and structural solidification becomes the dominant regime.

## 2. Theoretical Foundations: Graphs, Laplacians, and Mobility

To understand how eigenvalues delimit solidification, one must first establish the mathematical correspondence between social mobility and spectral graph theory.

### 2.1 The Social Stratification Network
A social stratification network can be modeled as a graph $G = (V, E)$, where $V$ represents social agents (or classes of agents) and $E$ represents the pathways of mobility or interaction between them. In intergenerational mobility studies, these nodes often represent income quantiles or occupational categories, and the edges are weighted by the probability of transition from one state to another [cite: 5, 6].

### 2.2 The Laplacian Matrix
The structural properties of this graph are encapsulated in the Laplacian matrix $L$. For a simple graph, the unnormalized Laplacian is defined as:
\[ L = D - A \]
where $D$ is the degree matrix (a diagonal matrix of node connections) and $A$ is the adjacency matrix [cite: 7, 8].

The eigenvalues of $L$, denoted as $0 = \lambda_1 \le \lambda_2 \le \dots \le \lambda_n$, provide deep insights into the network's structure.
*   **$\lambda_1 = 0$:** The smallest eigenvalue is always zero. The multiplicity of the zero eigenvalue indicates the number of connected components in the graph [cite: 8, 9].
*   **$\lambda_2$ (The Fiedler Value):** The second smallest eigenvalue is known as the **algebraic connectivity**. It is the most critical parameter for social stratification. If $\lambda_2 > 0$, the graph is connected; if $\lambda_2$ is close to 0, the graph is weakly connected and prone to severing into two pieces [cite: 10, 11].

### 2.3 Mobility Functions as Transition Operators
In the context of social dynamics, "mobility functions" are often represented by stochastic transition matrices $P$, related to the Laplacian. A mobility function $m(p_0)$ defines the distance or probability of movement between an initial social position $p_0$ and a future position [cite: 12].

The transition matrix $P$ is related to the normalized Laplacian $\mathcal{L}$ by:
\[ \mathcal{L} = I - D^{-1/2} A D^{-1/2} \]
The eigenvalues of the transition matrix ($1 = \mu_1 \ge \mu_2 \ge \dots \ge \mu_n$) are directly related to the Laplacian eigenvalues. Specifically, the **spectral gap** is defined as $1 - \mu_2$ (or $\lambda_2$ in the normalized Laplacian context) [cite: 13, 14]. This gap quantifies the "mixing rate" of the society—how quickly an individual's starting position becomes irrelevant to their current status.

## 3. Laplacian Eigenvalues as Delimiters of Solidification

The core mechanism by which eigenvalues delimit structural solidification is through the regulation of **diffusion** and **mixing times**. Solidification is mathematically equivalent to a divergence in the mixing time of the Markov chain representing social trajectories.

### 3.1 The Spectral Gap and the Mixing Time Threshold
The **mixing time** ($t_{mix}$) is the time required for a random walk on the graph to reach its stationary distribution (equilibrium). In a social context, this represents the number of generations or time steps required for equal opportunity to be realized, regardless of ancestral origin.

The mixing time is bounded by the spectral gap ($1 - \mu_2$ or $\lambda_2$):
\[ t_{mix} \approx \frac{1}{1 - \mu_2} = \frac{1}{\lambda_2} \]
[cite: 13, 15, 16].

*   **High Mobility Regime:** When the spectral gap is large (i.e., $\lambda_2$ is large), the mixing time is short. The network is an "expander graph," meaning there are no bottlenecks preventing movement between any two social strata.
*   **Solidification Threshold:** As $\lambda_2 \to 0$, the mixing time $t_{mix} \to \infty$. Structural solidification occurs when the mixing time exceeds the relevant timescale of the social system (e.g., if it takes 50 generations to regress to the mean, the society is effectively solidified for all practical purposes) [cite: 13].

Therefore, the eigenvalue $\lambda_2$ acts as the precise delimiter. There exists a critical threshold $\epsilon$ such that if $\lambda_2 < \epsilon$, the network is considered structurally solidified.

### 3.2 Cheeger’s Inequality: The Geometric Bound of Stratification
The relationship between the eigenvalue and the physical "bottlenecks" of society is rigorously defined by **Cheeger’s Inequality**. The Cheeger constant (or conductance), $\Phi(G)$, measures the difficulty of leaving a specific cluster of nodes (a social class). It is the ratio of edges leaving the set to the total volume of the set.

Cheeger's inequality states:
\[ \frac{\lambda_2}{2} \le \Phi(G) \le \sqrt{2\lambda_2} \]
[cite: 4, 15].

This inequality proves that the Laplacian eigenvalue $\lambda_2$ sandwiches the solidification threshold.
*   **Lower Bound:** If $\lambda_2$ is small, $\Phi(G)$ must be small. This means there *must* exist a cut in the network (a class divide) that is very hard to cross.
*   **Upper Bound:** If $\Phi(G)$ is small (high stratification), $\lambda_2$ must be small.

Thus, $\lambda_2$ is not just a proxy; it is a fundamental limit on how "solid" the social structure can be. A specific value of $\lambda_2$ guarantees that the social network cannot be more fluid than a certain bound, effectively delimiting the threshold of structural solidification.

## 4. The Spectral Gap Mobility Index (SGMI)

Recent econometric literature has formalized these concepts into the **Spectral Gap Mobility Index (SGMI)**, explicitly using eigenvalues to measure social fluidity.

### 4.1 Definition and Application
Attanasio et al. (2020, 2022) introduced the SGMI to analyze intergenerational mobility in socio-emotional and cognitive skills [cite: 14, 17, 18, 19]. The index is computed as the difference between the largest eigenvalue (which is always 1 for stochastic matrices) and the second-largest eigenvalue ($\mu_2$) of the transition matrix:
\[ SGMI = 1 - \mu_2 \]

*   **SGMI = 1:** Corresponds to a matrix with perfect mobility (an independent system where origin does not predict destination).
*   **SGMI = 0:** Corresponds to an identity matrix (perfect immobility/solidification), where every individual remains in their ancestral state [cite: 14, 18].

### 4.2 Empirical Findings on Solidification
Using the SGMI, researchers have identified that mobility is not uniform. The "discrepancy between one and the second largest [eigenvalue] could be seen as a departure from zero mobility" [cite: 14].
*   **Multi-generational Persistence:** The SGMI has revealed that structural solidification is often stronger than standard two-generation elasticity measures suggest. When analyzing three generations (grandmothers to grandchildren), the eigenvalues indicate a "memory" in the system that persists longer than expected, suggesting a form of "spectral solidification" where the decay of advantage is slower than the immediate transition matrix implies [cite: 19, 20].
*   **Life Cycle Dynamics:** The index also tracks how mobility functions change over the life cycle. Solidification is not static; the eigenvalues of the mobility function evolve as individuals age, often showing that "skill transmission becomes more persistent as parents age" [cite: 20].

## 5. Structural Solidification as a Phase Transition

The concept of "solidification" implies a dynamic change—a freezing of a previously fluid system. Spectral graph theory models this as a phase transition governed by the Laplacian spectrum.

### 5.1 The Fiedler Vector and Network Partitioning
The eigenvector corresponding to $\lambda_2$, known as the **Fiedler vector**, assigns a value to every node in the network. The signs and magnitudes of these values partition the network into two communities that are most weakly connected [cite: 5].
*   In a solidified society, the Fiedler vector will show a sharp dichotomy (e.g., positive values for the elite, negative for the underclass) with very few nodes having values near zero (the "middle class" or bridge nodes).
*   Newman (2006) utilized eigenspectrum decomposition of the modularity matrix (closely related to the Laplacian) to identify these optimal community structures [cite: 5]. The magnitude of the associated eigenvalue indicates the strength of this solidification. A high positive eigenvalue for the modularity matrix implies that the identified strata are robust and resistant to mixing.

### 5.2 Criticality and Instability
Research on pattern formation in spatial networks shows that the spatial structure affects system stability *only* via the Laplacian eigenvalues [cite: 3].
*   **$\kappa_{crit}$ (Critical Eigenvalue):** There exists a critical eigenvalue threshold. If the network's eigenvalues fall within a certain range, the "homogeneous state" (a classless or fully mixed society) becomes unstable, and the system spontaneously segregates into patterns (strata) [cite: 3].
*   **Rich-Get-Richer Dynamics:** This spectral instability drives mechanisms like preferential attachment, where hubs (elites) accumulate more connections (wealth/status), further suppressing $\lambda_2$ and driving the system toward solidification [cite: 21, 22].

### 5.3 The "Solidification Effect" in Urban Systems
Sociological studies define the "solidification effect" as the mutual reinforcement of social differentiation and spatial (housing) differentiation [cite: 23].
*   **Spectral Interpretation:** In graph terms, this is the coupling of two networks (social and spatial). The "supra-Laplacian" of this multilayer network governs the overall mobility.
*   **Thresholds:** If the algebraic connectivity of the coupled system drops below the synchronization threshold, the two layers (social status and location) become locked together. High-income groups solidify into specific spatial clusters, and low-income groups are trapped in others, with the eigenvalue $\lambda_2$ measuring the "permeability" of the boundaries between these spatial-social clusters [cite: 23, 24].

## 6. Mathematical Formalism: From Mobility Functions to Eigenvalues

To fully appreciate how eigenvalues delimit these thresholds, we must look at the mathematical properties of the mobility functions themselves.

### 6.1 Mobility Functions as Operators
A mobility function can be viewed as an operator $M$ acting on the distribution of social status $f(x)$.
\[ f_{t+1} = M f_t \]
If $M$ is linear (a matrix), the long-term behavior is dominated by the eigenspectrum.
\[ f_t = \pi + c_2 \lambda_2^t v_2 + c_3 \lambda_3^t v_3 + \dots \]
where $\pi$ is the steady-state distribution (perfect equality/mixing) and $\lambda_i$ are the eigenvalues sorted by magnitude (excluding $\lambda_1=1$) [cite: 6].

### 6.2 The Rate of Solidification
The term $\lambda_2^t$ governs the decay of inequality.
*   If $\lambda_2 \approx 1$ (small spectral gap), the term $\lambda_2^t$ decays very slowly. The initial distribution $f_0$ (historical inequality) persists for large $t$. This *is* structural solidification.
*   The threshold of solidification can be defined as the value of $\lambda_2$ for which the half-life of inequality $t_{1/2} = \frac{-\ln 2}{\ln \lambda_2}$ exceeds a sociologically acceptable timeframe (e.g., one generation) [cite: 13].

### 6.3 Power Laws and Mobility Functions
While some literature discusses mobility functions in the context of thin-film equations (using power laws $u^n$) [cite: 25, 26], the sociological parallel lies in the shape of the mobility curve. If the mobility function is non-linear (e.g., a "poverty trap" shape), the local linearization of the operator at the trap yields eigenvalues that indicate stability. A stable fixed point at the bottom of the distribution (a poverty trap) corresponds to a local Laplacian eigenvalue that prevents "flow" out of that state, effectively solidifying that segment of the population [cite: 3].

## 7. Comparative Analysis of Spectral Metrics in Stratification

Different spectral metrics highlight different aspects of solidification.

| Metric | Spectral Definition | Sociological Interpretation of Solidification | Source |
| :--- | :--- | :--- | :--- |
| **Algebraic Connectivity** | $\lambda_2$ of Laplacian ($L$) | The "width" of the bottleneck between social classes. Low value = narrow bottleneck (rigid stratification). | [cite: 5, 10, 11] |
| **Spectral Gap** | $1 - \mu_2$ of Transition Matrix ($P$) | The speed at which social background is "forgotten." Low gap = high inheritance of status. | [cite: 14, 17, 19] |
| **Mixing Time** | $\sim 1/\lambda_2$ | The number of generations required for a dynasty to regress to the mean. Infinite time = permanent caste system. | [cite: 13, 27] |
| **Modularity ($Q$)** | Eigenvalues of Modularity Matrix | The degree to which the network is divided into distinct, self-contained communities (classes). | [cite: 5] |
| **Relaxation Time** | Inverse of spectral gap | The persistence of wealth distributions against entropic mixing forces. | [cite: 13, 16] |

## 8. Discussion: The "Disorganized" vs. "Solidified" Institution

It is crucial to distinguish between "disorganization" and "solidification."
*   **Disorganization:** Sources [cite: 2, 28] discuss the "disorganized family" as a shift from rigid roles to negotiated ones. In spectral terms, this might look like a *decrease* in solidification (higher $\lambda_2$) as edges (relationships) become more fluid and less deterministic.
*   **Solidification:** Conversely, "structural solidification" [cite: 1, 2] implies the hardening of these roles or class boundaries. In the context of the "disorganized" institution, solidification may re-emerge not as formal rules, but as "expected moral responsibilities" that create strong, unbreakable bonds (high edge weights), locally reducing the spectral gap within the family unit while potentially disconnecting it from the broader social graph [cite: 2].

## 9. Conclusion

Laplacian eigenvalues of mobility functions serve as the fundamental mathematical delimiters of structural solidification in social stratification networks. They function as follows:
1.  **Quantification:** The **spectral gap** ($1-\lambda_2$) provides a scalar value representing the overall fluidity of the social structure.
2.  **Thresholding:** **Cheeger's Inequality** establishes that a low $\lambda_2$ necessitates the existence of a severe bottleneck (a "cut") in the society, mathematically proving the existence of distinct, solidified strata.
3.  **Dynamics:** The evolution of eigenvalues over time (as seen in the **Spectral Gap Mobility Index**) tracks the process of solidification, identifying when a society transitions from a mixing phase to a trapped, stratified phase.

Thus, structural solidification is not merely a qualitative sociological description but a spectral phenomenon where the Laplacian eigenvalues cross a critical threshold, causing the mixing time of social capital to diverge and trapping individuals within the eigenspaces of their origin.

## References
*   **[cite: 1]** Honneth, A. (2014). *Freedom's Right: The Social Foundations of Democratic Life*.
*   **[cite: 2, 28]** Smyth, L. (2015/2016). *The disorganized family: Institutions, practices and normativity*.
*   **[cite: 3]** *Laplacian eigenvalues and spatial network structure*. PNAS.
*   **[cite: 7]** *Laplacian eigenvalues of graphs*.
*   **[cite: 8]** *Unnormalized Laplacian and graph structure*.
*   **[cite: 29]** *Spectral graph theory in social networks*.
*   **[cite: 4]** *Spectral graph theory and Cheeger inequality*.
*   **[cite: 9]** *Graphs as Matrices: Laplacian definition*.
*   **[cite: 21, 22]** *Hierarchical mobility in temporal networks*.
*   **[cite: 10]** *Algebraic connectivity of graphs*.
*   **[cite: 5]** *Community detection and social mobility*.
*   **[cite: 6]** *Class Mobility Across Three Generations*.
*   **[cite: 20]** *PhD Thesis on Spectral Gap Mobility Index*.
*   **[cite: 13, 16]** *Measures of Physical Mixing Evaluate Economic Mobility*.
*   **[cite: 14, 17, 18, 19, 30, 31, 32, 33]** Attanasio et al. (2020/2022). *Intergenerational Mobility in Socio-emotional Skills* (Spectral Gap Mobility Index).
*   **[cite: 12]** *Economic Mobility and the Rise of the Latin American Middle Class*.
*   **[cite: 23]** *Solidification effect of social differentiation*.
*   **[cite: 27]** *Measurement of Mixing Time in Social Networks*.
*   **[cite: 15]** *Mixing times and spectral gaps*.
*   **[cite: 11]** *Phase transitions in social networks*.
*   **[cite: 24]** *Multilayer networks and algebraic connectivity*.
*   **[cite: 25, 26, 34]** *Mobility functions in stochastic thin-film equations*.

**Sources:**
1. [dokumen.pub](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEelRx2XmQmV-HCgTHyJg8jd9Jl92NFVUQGPxcVCBxp5_WmdHg7YrGDvJZjCVZ7tJaxVQdjxJeZTW_nFJ92KHbwBycZVATFIS-jUFpH9NhpjzNep3CRt1Zflp0RaUZQCYX9R8EZS_RE2dye2xNlDqrfYmGx2ace42tAERb9sFHhoILeum8e9SP5NB6xDEjUwNCBxm-A8UT4A378QY3kGgAwjxw_vWBKyE7prnhTANPWCUBjodeDgMUj818831Jgt_ZJMcSqy_NLQVMOI5LvnEkkhbo=)
2. [qub.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0lwlcbQUFeQKBsg1K1XiI9tFKgF1brU8Qo9WGSrJU0uuGkwGyeFQMpDxMWS7W4dYOrzyHEpUvYiykloyv_SABswfGMyb2044rl_DdOuAzsvas9WAVJTFJpVduRMEglpWqtksvFmtUTgzlcKF9bnqLO1vAKrvLp0S2hZRnWORiL05gxfppFpEMKDjcW5KOOEbh1G1_eYMHMla-i6XYJLLBRmJAF_rMjMgTtimQhg==)
3. [pnas.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHI1rBOPmEgz8j4cONMECbcUJOArVfF1ubzLL9bjJrCM0YDLm2Pj6q5LHnRNfIGJvi-XSuHhbOO_HCYrPaX75xHcHY4i5TO-jqFAWJrrqBFwD7fTd1jCptOBZal6XzIFFC9LNpMYRg=)
4. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-uEgPRQlZRe4-XjNAJ6VJUdxfhVC-yWCq0hvgWal5V58gZXi17SglX0yCdejlrmjJVXE2BBs0ASfT2dDZvltVL-v4eAtTBG_EvgoLh6ZCCa3utWGrolfqen3i-U4EEq3QLQ2W4QtoDm8=)
5. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiwGAAuNbl4ueeAINU_G7VAZ-9pULMnjumLUvyI6NPfhQdsDgjdchcbKGdDtpRdjr7JDdxqDUjr5JTuqjG-XLyw9GvUC7cX3ry_qHj7q0Ty-Yx_I5dIbcdXjmUxxWLAeZAgqnPsEOSXNIydQBsEuc8TeNrNrz4V7LKAYU4uRb63TUYTfbuuXBiTF1KHJddwnsDuO8=)
6. [upenn.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG86aumjWeJ6ocDQYVUrqsYxK9pJAOeccJitwEF-0VIgX7aRm42n3SIzr7NHhnp4LYhEAx0IQ6rKY8n3svszER_vJ6bF95NlDnwBDg2OgCbBZq0JYFSy2q7kqRQ8QxLP6ycRUlh4ckkwcDPuCxGTJIo0HykkkgaMWhC2BbXA-HUiF4FLjaVMeL7D5a6Ud0rOb7k-JfBmb1lRWoY)
7. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_aAMuGEXIL8X1Z4fU2r-Pn6R0AXLCWtg2hKqiM6LmRUreUHse6jZk5nElDsn7cL-IXTi6FSYWYpg8QO3bWh-zUPoF3s3NSCa1pJTYUe7ifeNVHSTl)
8. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpCrn_pL98cOqDZeQE8QF_ZpaKP5aOll2r5ELGs4tGBstvWRAsW56QwuJ5A7ZBFXLruQyuiU87ZY-Ssdnro8Oro7lbJFFyzMm145dDrvOLjmUKsGmBIW-w3qWWrWK2NbSvHRVPMnl0YMud47gQ6J1ck11dYg==)
9. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEatlUiwxKD21_8w1qDlVp3xIWg7AH7_Tkkj28q0sA2WnCv6OTGGSJ8jqt5kC8RbuEAWLyPJmsx74o6xSL39tjOMhKnNRirkCjmnj8Nb0uVbvhq17XuNmPNhZFpZLOnkDMMoZDM)
10. [pageplace.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg1oNlpjV4Vemzcr-sLS1MReDpIWguV_Hjr1STcnpE5FUnrHmjWJn-oybwRrYGGzmYc9KOHQiEfv_N8t3Ax9Xw9HZ-DeDnkzJb8of0CyrqTpl_2EJQwo_KtpGOlFJkwbySuNVMb2Vj_9om_F7Fp9WKa1Wmx-5Hq5tfccGH4MNftb8Ee1_93-FhfmQAoWmNdQo4SRHAv3fuFY0=)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCDMeSOlE2pTNj7f6NLGKxzA7SRmR7wJXprVBx9K3VAg_k5e921ae8M6eSgUpVUmpNUKJvzVBC9mVWH0nDobxXyWB3Zg2dpyU3PuUfU_0-D__FHe2YH7TAy7MiEzwjmkvSJGgECGEc8-HT0jyF3psTttWMY9k7Ajd9G5QLGRwY7ohzaeIpIGmIESIOG5JDZbKHUjaPU-AF5GnO6buLXP9IbT_T_iQguuLsZ6Cyfw==)
12. [worldbank.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMmEjUpsJuDdMxRzd9ZN012c4o-ioewN7RRq7PkpzpM_C7QU7MXOTWHgdx23AWELxzOXEIcKQDo58G5q4ho7YNExEkAg1-5YO9yJ4iFc9UEZdfWszGszoGnaj4HsHRz5UpBPYOZmMfQ1Ly5jFMnkSnJnvPGfl07pzxK3GEKHlOUEHCONQXmx_zCDh1t117mIzapxav5wAERxIEL5MEBKZshWanDqaBsFn8oM71Qv8ZhzAuOj7nfdTAUUbmSDRDxA==)
13. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjnxWV4icHGbiBc0A4qv1ChpN9Ukkl7tV3JkbwTguB6MLSbYN5umvyPhdl2wpuF0lMOlPeS5lJhXAjwwiOHu0aiHrqRq_eKAcqPJP11X77erbsSRVbuOdqkE7FS6Jzun9Jq9_tZgNEiBJETRuuTvk9azX22JoelCOiQSV2E04RrdQgzkYz4eIqMdwzwPkgfTNfyWJWecx6MxczzyxuQ2sMwHDTH5BJVPJpNR1yZYKzMpZpIdA056Qd9RE3l1UX)
14. [nber.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVyuAfIUjJrGXPVu1ZAi-X9zg4nHJeTa2ShgNxA1kLICX3u1QUuA3afkw9wBI5nJhg_V1_lrTs1zqGr5xUORbkcvnAcJS1QKmMrnlRDW41kczQKGL0ecU6_6D0K5MCncT9GOec7n0NqX-I6JiGVlFRhZHa-fv82Yk=)
15. [ubc.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSWoKWdmn2IzP3awl_VL7lGz4B2heLBSk3J7dwTp_qTTR5VsESiJXUpU2nNmsW1e535gFL5WmiuMRmlTrsdFJv7rQXTjZ273AaWzgn4i86liWRKCa22qwV95qzxMe8cePnXgfNbqHHuRSXUxs=)
16. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-P6o5tyhzmnTa0a4uABr5cN0TGUAGqa2r5PLfpRCsp4utS-DeSeEoAXHhndPUfu8nIeJ7KFbGilWNxasvb_wUQXRYGl_ap46deGtyMLcIjrie8e1muw==)
17. [scribd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEi4tRBl5uhbvG-ateNStKOwIL8cUK_n9TKbziBreFRp8zAu4qD4pccVw9Mv0bzpxtGQeRgwxL0OzSk-lINqjjS1In935AkZduiTuSUD_T-zrki887-tc5gARSBsokSW7ltlPgwimGhG1UUguRjrZyxqtlfM0JYeUwb67mvPcfc)
18. [ucl.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGomjvh7n1c9SMj3n94dw3FDCalbhXub1DOJlK7-hl7i3iIwEh5ubBVBa-mSAhbiQKKgGOT-3HRzZol3P8SvWXDMG_qspdccHgzCgxWxTp4AVfCtGutolBtxAXxqGtrZmT-Ar8e4rEBBPP_F_tMqKo5H9kUhKg=)
19. [ifs.org.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmA2fpb_9jekwegle7aZqWWrqblzLZ66ycy69bnQgQ-WL91WQ1Cx_AbiZphsomxYOuiigKhP7XTURzQ_WWrfs5LIBAblU_mbBYarpWFGUM21pj2X2Ab_e3I9RV30VN1cMBmL3QK_HLaUPVZq23loi75cT78VyEYnqvcIERuJ8HDdXll1CN2NQ-99wPJHplkjZJjYrxPQjEJJhjFYCPW74YxQSsDwXB)
20. [ucl.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPhUnfCr6v4e-YtZT1Yx4kRhDYX_RRYWDCl3Zr-9oeb1pGidGB3g643VhA6TRT-DYtmTEW0D22FOhfSHgYivqgBROXlM-bcvZgnrLkBrk6OOx5fBNQ-2ggxd1pLeQjlTf8wB7yKD9vnC8M1FFg_sNg7JLPP2FzfB4=)
21. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAKX0TDQ6rvKbzhNLRE3VelZx5f8x6YxG3YtSCmQ8ote-zgDQMF3WhuzKanmesaIdZcLUfv2tmWg9NSH4oRE8h8zlOt5d9ld2zBf9ARc8Hiyo8s9hxQA==)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0mW5z28La6jr0OTKINcz5hAnYYQQOVKPUysZVB82d7Q4bZWmfo813bod9KaneudiKPvPzHPdFgzkNs7NGMZXwMgwh3XIexyH5O-7y1C82MsvO6PyvstJPORu-rR_bJLfbp9xNv4Pbyk6R1b3zg7fPXeQoUi6BgAI9RN5MtjCCREvp9_7TCS2wTvYxSJbFdGPvBYSTI0AK)
23. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHozuszwYJ9uV7BSvElL2f7GvaPeEfRSYvY18o37bA5DvA3N7WsRqokPRwqVcgkN3wQpGVfZONbpJKmylxTIjiwUbDK5Vy_DWG44merdT_5YVuAKQQ5OMH3Hd5pPCjKPQ==)
24. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGetdi2uZLpOscK3z_gwy0HiyKqMePrpalCJAkN89IqlbZJrACGqc64VfSPOASMsDxB6iitO4D4RxOVGueN5MIv1gelMDkuL6a9_33fRHOjy3zObyLdsWOpWw==)
25. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuNx916jAGBEs2RlWA5goncR19kKEkdHAOBBIecaNlMnU_7wkU2B_DocBNfRO6i9xsOiiqEjDj5eIwuWPGMi2YkKinHKuxkXoEPbS-mAel8RgUujseqqMeiw==)
26. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBONUPK8cQ4WYnm4nZ-I5q-WPryQs_Ijw46PQ-8d1Tzvscz4j8civMvfQAOnn3Yk1ymCFl4Liz_sbNU9ikXeMao_qlBS8damTeukT9Y1pKE9i2SIEd0Q==)
27. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEzNSpuLA3DKzCEwBsGG13i_vFpJddGPEE_Cf5gcbq-iXgiS_lmXUW0uUYksQ-C11kgI4jHYVZP5TzeUn-0qLSn2RmClTOFcZp01ymjq__KHPic0iCZAOmLhaF_2YWSbDYen2tHnTnn_3FpHKKDdCSGgjQHZIKObfOhVLV7DI-oAa0zdRdmVZDWgaH2M-pf8DPqGYCSLh86w==)
28. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEHHFmnQ67rZznWVmjpQYWzk7ydN0Th3zb_bOOn9Dv7AG6kUkBLibuFIgnGKyVBVf41j0QfssmJo8q-e0KfW9S1CLkGk4eHif6zSsVYPPllZYQY-ZFR2g4AfzWzp_F3RqsuKEsCqexkQ4XyV0sa2ogyX7dcjpHHEmdlT0FD964lmHC7hoUxgx5yk9X103Uq8dSanrLAHVSZuokGj_Aaj7j3OR05B9Ykg==)
29. [ijercse.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0Utu_A3vWtRo4VQE-PgMkPMut-PGeCzBvuiAK2eroo8EHUM2XyQ1cXBODQGYqTHSL_UK-xmtlzZIrwzzIesntqHNekIjDb2A30jNAZST2m5huQfGTvxTlk086oXCJtgRLiLUvo75URm1OsrQa_b4=)
30. [nber.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmDLU_ZEmgFQ49YNdTENRg2AIJJogoxE2K4DRL0KdpsLmJWtbZKCuc2KRQFJP9e9zgpyEm9I0eTkQOx-hVOEr6BvIUPPVnEUbWbViZdIq0B3J4j-Fy7kKurTBKkg-FS52Dzy2OfKtE3G_j6PK4Sw9qLy61ggjHwp-muXe0NSYVvul7qay80Jk=)
31. [ifs.org.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQjUac4B4K21NjBJj3ykybA_VxiebNJDGp9S1QI_oWhMkMXSgKg4LyzoIUztUWUU94sk6WWYXb4yrcpD5vGHMkAA_3yeIwC6vmRMCMuCOxmrBr2yg_r1z6-A2Asao8HaNmTHwRwIXksiyA8W8-3mrw_i5k45hOM2AqBkMiiYMe8Rch-V6-w4kq5_0fJgCjQdku673GMdEIZwbV8_L2hM0OIAjrVFzbhXsEbA==)
32. [uchicago.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEogC6vCsCIpC7HrcbuRA7-C4a6TQIn-m2OgUJMyPX7zoMOX5wygNr5jP4uCWszgFMDs0wvvOLKKpWVTL8v17Le1-b02mOfqrw6Lf_fEfWf-HlUmZlcRN-lsg0-eAqhTmedwyylkGcjlFL7vyoDt9VlZ5NgsUMDJg1jFt0gWuvm7P0LaPBanL2XOf3XFOEK0P5UcGFF97YA3gxOxuJZQbCpKMZnLvfrQB7__UklNMIBUsswbbjLKkgBkN_H)
33. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEclhx_BxEtHQA8XxytNdMGAhLEWNU0yrAogmbZxh9HhdIbPAPxFecJ-Pn39Djg6j9DufRUCME9d6eGyZVr7uCRRHcPGa8bYt_-vnLw-5Yd_C8MlawbekWJkW8WspJX)
34. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0yDee5nAADBuongKsIFsrb6Rpwa3Se2c2POVHKane9YjlcXlw9bIekSosQUFhnXOliOjFh2r2AGjdY-ts2c8dE2CdIZ2RqqZBxFRHpKoYqNgcdItu8g==)


## Annotations
Annotation(end_index=2850, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0lwlcbQUFeQKBsg1K1XiI9tFKgF1brU8Qo9WGSrJU0uuGkwGyeFQMpDxMWS7W4dYOrzyHEpUvYiykloyv_SABswfGMyb2044rl_DdOuAzsvas9WAVJTFJpVduRMEglpWqtksvFmtUTgzlcKF9bnqLO1vAKrvLp0S2hZRnWORiL05gxfppFpEMKDjcW5KOOEbh1G1_eYMHMla-i6XYJLLBRmJAF_rMjMgTtimQhg==', start_index=2838)
Annotation(end_index=2850, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEelRx2XmQmV-HCgTHyJg8jd9Jl92NFVUQGPxcVCBxp5_WmdHg7YrGDvJZjCVZ7tJaxVQdjxJeZTW_nFJ92KHbwBycZVATFIS-jUFpH9NhpjzNep3CRt1Zflp0RaUZQCYX9R8EZS_RE2dye2xNlDqrfYmGx2ace42tAERb9sFHhoILeum8e9SP5NB6xDEjUwNCBxm-A8UT4A378QY3kGgAwjxw_vWBKyE7prnhTANPWCUBjodeDgMUj818831Jgt_ZJMcSqy_NLQVMOI5LvnEkkhbo=', start_index=2838)
Annotation(end_index=3396, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-uEgPRQlZRe4-XjNAJ6VJUdxfhVC-yWCq0hvgWal5V58gZXi17SglX0yCdejlrmjJVXE2BBs0ASfT2dDZvltVL-v4eAtTBG_EvgoLh6ZCCa3utWGrolfqen3i-U4EEq3QLQ2W4QtoDm8=', start_index=3384)
Annotation(end_index=3396, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHI1rBOPmEgz8j4cONMECbcUJOArVfF1ubzLL9bjJrCM0YDLm2Pj6q5LHnRNfIGJvi-XSuHhbOO_HCYrPaX75xHcHY4i5TO-jqFAWJrrqBFwD7fTd1jCptOBZal6XzIFFC9LNpMYRg=', start_index=3384)
Annotation(end_index=4540, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiwGAAuNbl4ueeAINU_G7VAZ-9pULMnjumLUvyI6NPfhQdsDgjdchcbKGdDtpRdjr7JDdxqDUjr5JTuqjG-XLyw9GvUC7cX3ry_qHj7q0Ty-Yx_I5dIbcdXjmUxxWLAeZAgqnPsEOSXNIydQBsEuc8TeNrNrz4V7LKAYU4uRb63TUYTfbuuXBiTF1KHJddwnsDuO8=', start_index=4528)
Annotation(end_index=4540, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG86aumjWeJ6ocDQYVUrqsYxK9pJAOeccJitwEF-0VIgX7aRm42n3SIzr7NHhnp4LYhEAx0IQ6rKY8n3svszER_vJ6bF95NlDnwBDg2OgCbBZq0JYFSy2q7kqRQ8QxLP6ycRUlh4ckkwcDPuCxGTJIo0HykkkgaMWhC2BbXA-HUiF4FLjaVMeL7D5a6Ud0rOb7k-JfBmb1lRWoY', start_index=4528)
Annotation(end_index=4851, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpCrn_pL98cOqDZeQE8QF_ZpaKP5aOll2r5ELGs4tGBstvWRAsW56QwuJ5A7ZBFXLruQyuiU87ZY-Ssdnro8Oro7lbJFFyzMm145dDrvOLjmUKsGmBIW-w3qWWrWK2NbSvHRVPMnl0YMud47gQ6J1ck11dYg==', start_index=4839)
Annotation(end_index=4851, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_aAMuGEXIL8X1Z4fU2r-Pn6R0AXLCWtg2hKqiM6LmRUreUHse6jZk5nElDsn7cL-IXTi6FSYWYpg8QO3bWh-zUPoF3s3NSCa1pJTYUe7ifeNVHSTl', start_index=4839)
Annotation(end_index=5171, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEatlUiwxKD21_8w1qDlVp3xIWg7AH7_Tkkj28q0sA2WnCv6OTGGSJ8jqt5kC8RbuEAWLyPJmsx74o6xSL39tjOMhKnNRirkCjmnj8Nb0uVbvhq17XuNmPNhZFpZLOnkDMMoZDM', start_index=5159)
Annotation(end_index=5171, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpCrn_pL98cOqDZeQE8QF_ZpaKP5aOll2r5ELGs4tGBstvWRAsW56QwuJ5A7ZBFXLruQyuiU87ZY-Ssdnro8Oro7lbJFFyzMm145dDrvOLjmUKsGmBIW-w3qWWrWK2NbSvHRVPMnl0YMud47gQ6J1ck11dYg==', start_index=5159)
Annotation(end_index=5506, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCDMeSOlE2pTNj7f6NLGKxzA7SRmR7wJXprVBx9K3VAg_k5e921ae8M6eSgUpVUmpNUKJvzVBC9mVWH0nDobxXyWB3Zg2dpyU3PuUfU_0-D__FHe2YH7TAy7MiEzwjmkvSJGgECGEc8-HT0jyF3psTttWMY9k7Ajd9G5QLGRwY7ohzaeIpIGmIESIOG5JDZbKHUjaPU-AF5GnO6buLXP9IbT_T_iQguuLsZ6Cyfw==', start_index=5492)
Annotation(end_index=5506, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg1oNlpjV4Vemzcr-sLS1MReDpIWguV_Hjr1STcnpE5FUnrHmjWJn-oybwRrYGGzmYc9KOHQiEfv_N8t3Ax9Xw9HZ-DeDnkzJb8of0CyrqTpl_2EJQwo_KtpGOlFJkwbySuNVMb2Vj_9om_F7Fp9WKa1Wmx-5Hq5tfccGH4MNftb8Ee1_93-FhfmQAoWmNdQo4SRHAv3fuFY0=', start_index=5492)
Annotation(end_index=5853, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMmEjUpsJuDdMxRzd9ZN012c4o-ioewN7RRq7PkpzpM_C7QU7MXOTWHgdx23AWELxzOXEIcKQDo58G5q4ho7YNExEkAg1-5YO9yJ4iFc9UEZdfWszGszoGnaj4HsHRz5UpBPYOZmMfQ1Ly5jFMnkSnJnvPGfl07pzxK3GEKHlOUEHCONQXmx_zCDh1t117mIzapxav5wAERxIEL5MEBKZshWanDqaBsFn8oM71Qv8ZhzAuOj7nfdTAUUbmSDRDxA==', start_index=5843)
Annotation(end_index=6247, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjnxWV4icHGbiBc0A4qv1ChpN9Ukkl7tV3JkbwTguB6MLSbYN5umvyPhdl2wpuF0lMOlPeS5lJhXAjwwiOHu0aiHrqRq_eKAcqPJP11X77erbsSRVbuOdqkE7FS6Jzun9Jq9_tZgNEiBJETRuuTvk9azX22JoelCOiQSV2E04RrdQgzkYz4eIqMdwzwPkgfTNfyWJWecx6MxczzyxuQ2sMwHDTH5BJVPJpNR1yZYKzMpZpIdA056Qd9RE3l1UX', start_index=6233)
Annotation(end_index=6247, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVyuAfIUjJrGXPVu1ZAi-X9zg4nHJeTa2ShgNxA1kLICX3u1QUuA3afkw9wBI5nJhg_V1_lrTs1zqGr5xUORbkcvnAcJS1QKmMrnlRDW41kczQKGL0ecU6_6D0K5MCncT9GOec7n0NqX-I6JiGVlFRhZHa-fv82Yk=', start_index=6233)
Annotation(end_index=7236, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjnxWV4icHGbiBc0A4qv1ChpN9Ukkl7tV3JkbwTguB6MLSbYN5umvyPhdl2wpuF0lMOlPeS5lJhXAjwwiOHu0aiHrqRq_eKAcqPJP11X77erbsSRVbuOdqkE7FS6Jzun9Jq9_tZgNEiBJETRuuTvk9azX22JoelCOiQSV2E04RrdQgzkYz4eIqMdwzwPkgfTNfyWJWecx6MxczzyxuQ2sMwHDTH5BJVPJpNR1yZYKzMpZpIdA056Qd9RE3l1UX', start_index=7218)
Annotation(end_index=7236, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-P6o5tyhzmnTa0a4uABr5cN0TGUAGqa2r5PLfpRCsp4utS-DeSeEoAXHhndPUfu8nIeJ7KFbGilWNxasvb_wUQXRYGl_ap46deGtyMLcIjrie8e1muw==', start_index=7218)
Annotation(end_index=7236, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSWoKWdmn2IzP3awl_VL7lGz4B2heLBSk3J7dwTp_qTTR5VsESiJXUpU2nNmsW1e535gFL5WmiuMRmlTrsdFJv7rQXTjZ273AaWzgn4i86liWRKCa22qwV95qzxMe8cePnXgfNbqHHuRSXUxs=', start_index=7218)
Annotation(end_index=7810, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjnxWV4icHGbiBc0A4qv1ChpN9Ukkl7tV3JkbwTguB6MLSbYN5umvyPhdl2wpuF0lMOlPeS5lJhXAjwwiOHu0aiHrqRq_eKAcqPJP11X77erbsSRVbuOdqkE7FS6Jzun9Jq9_tZgNEiBJETRuuTvk9azX22JoelCOiQSV2E04RrdQgzkYz4eIqMdwzwPkgfTNfyWJWecx6MxczzyxuQ2sMwHDTH5BJVPJpNR1yZYKzMpZpIdA056Qd9RE3l1UX', start_index=7800)
Annotation(end_index=8528, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-uEgPRQlZRe4-XjNAJ6VJUdxfhVC-yWCq0hvgWal5V58gZXi17SglX0yCdejlrmjJVXE2BBs0ASfT2dDZvltVL-v4eAtTBG_EvgoLh6ZCCa3utWGrolfqen3i-U4EEq3QLQ2W4QtoDm8=', start_index=8515)
Annotation(end_index=8528, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSWoKWdmn2IzP3awl_VL7lGz4B2heLBSk3J7dwTp_qTTR5VsESiJXUpU2nNmsW1e535gFL5WmiuMRmlTrsdFJv7rQXTjZ273AaWzgn4i86liWRKCa22qwV95qzxMe8cePnXgfNbqHHuRSXUxs=', start_index=8515)
Annotation(end_index=9583, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEi4tRBl5uhbvG-ateNStKOwIL8cUK_n9TKbziBreFRp8zAu4qD4pccVw9Mv0bzpxtGQeRgwxL0OzSk-lINqjjS1In935AkZduiTuSUD_T-zrki887-tc5gARSBsokSW7ltlPgwimGhG1UUguRjrZyxqtlfM0JYeUwb67mvPcfc', start_index=9561)
Annotation(end_index=9583, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGomjvh7n1c9SMj3n94dw3FDCalbhXub1DOJlK7-hl7i3iIwEh5ubBVBa-mSAhbiQKKgGOT-3HRzZol3P8SvWXDMG_qspdccHgzCgxWxTp4AVfCtGutolBtxAXxqGtrZmT-Ar8e4rEBBPP_F_tMqKo5H9kUhKg=', start_index=9561)
Annotation(end_index=9583, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVyuAfIUjJrGXPVu1ZAi-X9zg4nHJeTa2ShgNxA1kLICX3u1QUuA3afkw9wBI5nJhg_V1_lrTs1zqGr5xUORbkcvnAcJS1QKmMrnlRDW41kczQKGL0ecU6_6D0K5MCncT9GOec7n0NqX-I6JiGVlFRhZHa-fv82Yk=', start_index=9561)
Annotation(end_index=9583, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmA2fpb_9jekwegle7aZqWWrqblzLZ66ycy69bnQgQ-WL91WQ1Cx_AbiZphsomxYOuiigKhP7XTURzQ_WWrfs5LIBAblU_mbBYarpWFGUM21pj2X2Ab_e3I9RV30VN1cMBmL3QK_HLaUPVZq23loi75cT78VyEYnqvcIERuJ8HDdXll1CN2NQ-99wPJHplkjZJjYrxPQjEJJhjFYCPW74YxQSsDwXB', start_index=9561)
Annotation(end_index=10084, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGomjvh7n1c9SMj3n94dw3FDCalbhXub1DOJlK7-hl7i3iIwEh5ubBVBa-mSAhbiQKKgGOT-3HRzZol3P8SvWXDMG_qspdccHgzCgxWxTp4AVfCtGutolBtxAXxqGtrZmT-Ar8e4rEBBPP_F_tMqKo5H9kUhKg=', start_index=10070)
Annotation(end_index=10084, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVyuAfIUjJrGXPVu1ZAi-X9zg4nHJeTa2ShgNxA1kLICX3u1QUuA3afkw9wBI5nJhg_V1_lrTs1zqGr5xUORbkcvnAcJS1QKmMrnlRDW41kczQKGL0ecU6_6D0K5MCncT9GOec7n0NqX-I6JiGVlFRhZHa-fv82Yk=', start_index=10070)
Annotation(end_index=10330, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVyuAfIUjJrGXPVu1ZAi-X9zg4nHJeTa2ShgNxA1kLICX3u1QUuA3afkw9wBI5nJhg_V1_lrTs1zqGr5xUORbkcvnAcJS1QKmMrnlRDW41kczQKGL0ecU6_6D0K5MCncT9GOec7n0NqX-I6JiGVlFRhZHa-fv82Yk=', start_index=10320)
Annotation(end_index=10798, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPhUnfCr6v4e-YtZT1Yx4kRhDYX_RRYWDCl3Zr-9oeb1pGidGB3g643VhA6TRT-DYtmTEW0D22FOhfSHgYivqgBROXlM-bcvZgnrLkBrk6OOx5fBNQ-2ggxd1pLeQjlTf8wB7yKD9vnC8M1FFg_sNg7JLPP2FzfB4=', start_index=10784)
Annotation(end_index=10798, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmA2fpb_9jekwegle7aZqWWrqblzLZ66ycy69bnQgQ-WL91WQ1Cx_AbiZphsomxYOuiigKhP7XTURzQ_WWrfs5LIBAblU_mbBYarpWFGUM21pj2X2Ab_e3I9RV30VN1cMBmL3QK_HLaUPVZq23loi75cT78VyEYnqvcIERuJ8HDdXll1CN2NQ-99wPJHplkjZJjYrxPQjEJJhjFYCPW74YxQSsDwXB', start_index=10784)
Annotation(end_index=11089, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPhUnfCr6v4e-YtZT1Yx4kRhDYX_RRYWDCl3Zr-9oeb1pGidGB3g643VhA6TRT-DYtmTEW0D22FOhfSHgYivqgBROXlM-bcvZgnrLkBrk6OOx5fBNQ-2ggxd1pLeQjlTf8wB7yKD9vnC8M1FFg_sNg7JLPP2FzfB4=', start_index=11079)
Annotation(end_index=11641, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiwGAAuNbl4ueeAINU_G7VAZ-9pULMnjumLUvyI6NPfhQdsDgjdchcbKGdDtpRdjr7JDdxqDUjr5JTuqjG-XLyw9GvUC7cX3ry_qHj7q0Ty-Yx_I5dIbcdXjmUxxWLAeZAgqnPsEOSXNIydQBsEuc8TeNrNrz4V7LKAYU4uRb63TUYTfbuuXBiTF1KHJddwnsDuO8=', start_index=11632)
Annotation(end_index=12039, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiwGAAuNbl4ueeAINU_G7VAZ-9pULMnjumLUvyI6NPfhQdsDgjdchcbKGdDtpRdjr7JDdxqDUjr5JTuqjG-XLyw9GvUC7cX3ry_qHj7q0Ty-Yx_I5dIbcdXjmUxxWLAeZAgqnPsEOSXNIydQBsEuc8TeNrNrz4V7LKAYU4uRb63TUYTfbuuXBiTF1KHJddwnsDuO8=', start_index=12030)
Annotation(end_index=12446, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHI1rBOPmEgz8j4cONMECbcUJOArVfF1ubzLL9bjJrCM0YDLm2Pj6q5LHnRNfIGJvi-XSuHhbOO_HCYrPaX75xHcHY4i5TO-jqFAWJrrqBFwD7fTd1jCptOBZal6XzIFFC9LNpMYRg=', start_index=12437)
Annotation(end_index=12750, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHI1rBOPmEgz8j4cONMECbcUJOArVfF1ubzLL9bjJrCM0YDLm2Pj6q5LHnRNfIGJvi-XSuHhbOO_HCYrPaX75xHcHY4i5TO-jqFAWJrrqBFwD7fTd1jCptOBZal6XzIFFC9LNpMYRg=', start_index=12741)
Annotation(end_index=13016, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0mW5z28La6jr0OTKINcz5hAnYYQQOVKPUysZVB82d7Q4bZWmfo813bod9KaneudiKPvPzHPdFgzkNs7NGMZXwMgwh3XIexyH5O-7y1C82MsvO6PyvstJPORu-rR_bJLfbp9xNv4Pbyk6R1b3zg7fPXeQoUi6BgAI9RN5MtjCCREvp9_7TCS2wTvYxSJbFdGPvBYSTI0AK', start_index=13002)
Annotation(end_index=13016, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAKX0TDQ6rvKbzhNLRE3VelZx5f8x6YxG3YtSCmQ8ote-zgDQMF3WhuzKanmesaIdZcLUfv2tmWg9NSH4oRE8h8zlOt5d9ld2zBf9ARc8Hiyo8s9hxQA==', start_index=13002)
Annotation(end_index=13230, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHozuszwYJ9uV7BSvElL2f7GvaPeEfRSYvY18o37bA5DvA3N7WsRqokPRwqVcgkN3wQpGVfZONbpJKmylxTIjiwUbDK5Vy_DWG44merdT_5YVuAKQQ5OMH3Hd5pPCjKPQ==', start_index=13220)
Annotation(end_index=13838, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGetdi2uZLpOscK3z_gwy0HiyKqMePrpalCJAkN89IqlbZJrACGqc64VfSPOASMsDxB6iitO4D4RxOVGueN5MIv1gelMDkuL6a9_33fRHOjy3zObyLdsWOpWw==', start_index=13824)
Annotation(end_index=13838, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHozuszwYJ9uV7BSvElL2f7GvaPeEfRSYvY18o37bA5DvA3N7WsRqokPRwqVcgkN3wQpGVfZONbpJKmylxTIjiwUbDK5Vy_DWG44merdT_5YVuAKQQ5OMH3Hd5pPCjKPQ==', start_index=13824)
Annotation(end_index=14540, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG86aumjWeJ6ocDQYVUrqsYxK9pJAOeccJitwEF-0VIgX7aRm42n3SIzr7NHhnp4LYhEAx0IQ6rKY8n3svszER_vJ6bF95NlDnwBDg2OgCbBZq0JYFSy2q7kqRQ8QxLP6ycRUlh4ckkwcDPuCxGTJIo0HykkkgaMWhC2BbXA-HUiF4FLjaVMeL7D5a6Ud0rOb7k-JfBmb1lRWoY', start_index=14531)
Annotation(end_index=15081, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjnxWV4icHGbiBc0A4qv1ChpN9Ukkl7tV3JkbwTguB6MLSbYN5umvyPhdl2wpuF0lMOlPeS5lJhXAjwwiOHu0aiHrqRq_eKAcqPJP11X77erbsSRVbuOdqkE7FS6Jzun9Jq9_tZgNEiBJETRuuTvk9azX22JoelCOiQSV2E04RrdQgzkYz4eIqMdwzwPkgfTNfyWJWecx6MxczzyxuQ2sMwHDTH5BJVPJpNR1yZYKzMpZpIdA056Qd9RE3l1UX', start_index=15071)
Annotation(end_index=15254, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuNx916jAGBEs2RlWA5goncR19kKEkdHAOBBIecaNlMnU_7wkU2B_DocBNfRO6i9xsOiiqEjDj5eIwuWPGMi2YkKinHKuxkXoEPbS-mAel8RgUujseqqMeiw==', start_index=15240)
Annotation(end_index=15254, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBONUPK8cQ4WYnm4nZ-I5q-WPryQs_Ijw46PQ-8d1Tzvscz4j8civMvfQAOnn3Yk1ymCFl4Liz_sbNU9ikXeMao_qlBS8damTeukT9Y1pKE9i2SIEd0Q==', start_index=15240)
Annotation(end_index=15710, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHI1rBOPmEgz8j4cONMECbcUJOArVfF1ubzLL9bjJrCM0YDLm2Pj6q5LHnRNfIGJvi-XSuHhbOO_HCYrPaX75xHcHY4i5TO-jqFAWJrrqBFwD7fTd1jCptOBZal6XzIFFC9LNpMYRg=', start_index=15701)
Annotation(end_index=16165, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCDMeSOlE2pTNj7f6NLGKxzA7SRmR7wJXprVBx9K3VAg_k5e921ae8M6eSgUpVUmpNUKJvzVBC9mVWH0nDobxXyWB3Zg2dpyU3PuUfU_0-D__FHe2YH7TAy7MiEzwjmkvSJGgECGEc8-HT0jyF3psTttWMY9k7Ajd9G5QLGRwY7ohzaeIpIGmIESIOG5JDZbKHUjaPU-AF5GnO6buLXP9IbT_T_iQguuLsZ6Cyfw==', start_index=16148)
Annotation(end_index=16165, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg1oNlpjV4Vemzcr-sLS1MReDpIWguV_Hjr1STcnpE5FUnrHmjWJn-oybwRrYGGzmYc9KOHQiEfv_N8t3Ax9Xw9HZ-DeDnkzJb8of0CyrqTpl_2EJQwo_KtpGOlFJkwbySuNVMb2Vj_9om_F7Fp9WKa1Wmx-5Hq5tfccGH4MNftb8Ee1_93-FhfmQAoWmNdQo4SRHAv3fuFY0=', start_index=16148)
Annotation(end_index=16165, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiwGAAuNbl4ueeAINU_G7VAZ-9pULMnjumLUvyI6NPfhQdsDgjdchcbKGdDtpRdjr7JDdxqDUjr5JTuqjG-XLyw9GvUC7cX3ry_qHj7q0Ty-Yx_I5dIbcdXjmUxxWLAeZAgqnPsEOSXNIydQBsEuc8TeNrNrz4V7LKAYU4uRb63TUYTfbuuXBiTF1KHJddwnsDuO8=', start_index=16148)
Annotation(end_index=16341, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEi4tRBl5uhbvG-ateNStKOwIL8cUK_n9TKbziBreFRp8zAu4qD4pccVw9Mv0bzpxtGQeRgwxL0OzSk-lINqjjS1In935AkZduiTuSUD_T-zrki887-tc5gARSBsokSW7ltlPgwimGhG1UUguRjrZyxqtlfM0JYeUwb67mvPcfc', start_index=16323)
Annotation(end_index=16341, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVyuAfIUjJrGXPVu1ZAi-X9zg4nHJeTa2ShgNxA1kLICX3u1QUuA3afkw9wBI5nJhg_V1_lrTs1zqGr5xUORbkcvnAcJS1QKmMrnlRDW41kczQKGL0ecU6_6D0K5MCncT9GOec7n0NqX-I6JiGVlFRhZHa-fv82Yk=', start_index=16323)
Annotation(end_index=16341, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmA2fpb_9jekwegle7aZqWWrqblzLZ66ycy69bnQgQ-WL91WQ1Cx_AbiZphsomxYOuiigKhP7XTURzQ_WWrfs5LIBAblU_mbBYarpWFGUM21pj2X2Ab_e3I9RV30VN1cMBmL3QK_HLaUPVZq23loi75cT78VyEYnqvcIERuJ8HDdXll1CN2NQ-99wPJHplkjZJjYrxPQjEJJhjFYCPW74YxQSsDwXB', start_index=16323)
Annotation(end_index=16514, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjnxWV4icHGbiBc0A4qv1ChpN9Ukkl7tV3JkbwTguB6MLSbYN5umvyPhdl2wpuF0lMOlPeS5lJhXAjwwiOHu0aiHrqRq_eKAcqPJP11X77erbsSRVbuOdqkE7FS6Jzun9Jq9_tZgNEiBJETRuuTvk9azX22JoelCOiQSV2E04RrdQgzkYz4eIqMdwzwPkgfTNfyWJWecx6MxczzyxuQ2sMwHDTH5BJVPJpNR1yZYKzMpZpIdA056Qd9RE3l1UX', start_index=16500)
Annotation(end_index=16514, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEzNSpuLA3DKzCEwBsGG13i_vFpJddGPEE_Cf5gcbq-iXgiS_lmXUW0uUYksQ-C11kgI4jHYVZP5TzeUn-0qLSn2RmClTOFcZp01ymjq__KHPic0iCZAOmLhaF_2YWSbDYen2tHnTnn_3FpHKKDdCSGgjQHZIKObfOhVLV7DI-oAa0zdRdmVZDWgaH2M-pf8DPqGYCSLh86w==', start_index=16500)
Annotation(end_index=16684, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiwGAAuNbl4ueeAINU_G7VAZ-9pULMnjumLUvyI6NPfhQdsDgjdchcbKGdDtpRdjr7JDdxqDUjr5JTuqjG-XLyw9GvUC7cX3ry_qHj7q0Ty-Yx_I5dIbcdXjmUxxWLAeZAgqnPsEOSXNIydQBsEuc8TeNrNrz4V7LKAYU4uRb63TUYTfbuuXBiTF1KHJddwnsDuO8=', start_index=16675)
Annotation(end_index=16825, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjnxWV4icHGbiBc0A4qv1ChpN9Ukkl7tV3JkbwTguB6MLSbYN5umvyPhdl2wpuF0lMOlPeS5lJhXAjwwiOHu0aiHrqRq_eKAcqPJP11X77erbsSRVbuOdqkE7FS6Jzun9Jq9_tZgNEiBJETRuuTvk9azX22JoelCOiQSV2E04RrdQgzkYz4eIqMdwzwPkgfTNfyWJWecx6MxczzyxuQ2sMwHDTH5BJVPJpNR1yZYKzMpZpIdA056Qd9RE3l1UX', start_index=16811)
Annotation(end_index=16825, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-P6o5tyhzmnTa0a4uABr5cN0TGUAGqa2r5PLfpRCsp4utS-DeSeEoAXHhndPUfu8nIeJ7KFbGilWNxasvb_wUQXRYGl_ap46deGtyMLcIjrie8e1muw==', start_index=16811)
Annotation(end_index=17019, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0lwlcbQUFeQKBsg1K1XiI9tFKgF1brU8Qo9WGSrJU0uuGkwGyeFQMpDxMWS7W4dYOrzyHEpUvYiykloyv_SABswfGMyb2044rl_DdOuAzsvas9WAVJTFJpVduRMEglpWqtksvFmtUTgzlcKF9bnqLO1vAKrvLp0S2hZRnWORiL05gxfppFpEMKDjcW5KOOEbh1G1_eYMHMla-i6XYJLLBRmJAF_rMjMgTtimQhg==', start_index=17006)
Annotation(end_index=17019, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEHHFmnQ67rZznWVmjpQYWzk7ydN0Th3zb_bOOn9Dv7AG6kUkBLibuFIgnGKyVBVf41j0QfssmJo8q-e0KfW9S1CLkGk4eHif6zSsVYPPllZYQY-ZFR2g4AfzWzp_F3RqsuKEsCqexkQ4XyV0sa2ogyX7dcjpHHEmdlT0FD964lmHC7hoUxgx5yk9X103Uq8dSanrLAHVSZuokGj_Aaj7j3OR05B9Ykg==', start_index=17006)
Annotation(end_index=17337, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0lwlcbQUFeQKBsg1K1XiI9tFKgF1brU8Qo9WGSrJU0uuGkwGyeFQMpDxMWS7W4dYOrzyHEpUvYiykloyv_SABswfGMyb2044rl_DdOuAzsvas9WAVJTFJpVduRMEglpWqtksvFmtUTgzlcKF9bnqLO1vAKrvLp0S2hZRnWORiL05gxfppFpEMKDjcW5KOOEbh1G1_eYMHMla-i6XYJLLBRmJAF_rMjMgTtimQhg==', start_index=17325)
Annotation(end_index=17337, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEelRx2XmQmV-HCgTHyJg8jd9Jl92NFVUQGPxcVCBxp5_WmdHg7YrGDvJZjCVZ7tJaxVQdjxJeZTW_nFJ92KHbwBycZVATFIS-jUFpH9NhpjzNep3CRt1Zflp0RaUZQCYX9R8EZS_RE2dye2xNlDqrfYmGx2ace42tAERb9sFHhoILeum8e9SP5NB6xDEjUwNCBxm-A8UT4A378QY3kGgAwjxw_vWBKyE7prnhTANPWCUBjodeDgMUj818831Jgt_ZJMcSqy_NLQVMOI5LvnEkkhbo=', start_index=17325)
Annotation(end_index=17727, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0lwlcbQUFeQKBsg1K1XiI9tFKgF1brU8Qo9WGSrJU0uuGkwGyeFQMpDxMWS7W4dYOrzyHEpUvYiykloyv_SABswfGMyb2044rl_DdOuAzsvas9WAVJTFJpVduRMEglpWqtksvFmtUTgzlcKF9bnqLO1vAKrvLp0S2hZRnWORiL05gxfppFpEMKDjcW5KOOEbh1G1_eYMHMla-i6XYJLLBRmJAF_rMjMgTtimQhg==', start_index=17718)
Annotation(end_index=18857, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEelRx2XmQmV-HCgTHyJg8jd9Jl92NFVUQGPxcVCBxp5_WmdHg7YrGDvJZjCVZ7tJaxVQdjxJeZTW_nFJ92KHbwBycZVATFIS-jUFpH9NhpjzNep3CRt1Zflp0RaUZQCYX9R8EZS_RE2dye2xNlDqrfYmGx2ace42tAERb9sFHhoILeum8e9SP5NB6xDEjUwNCBxm-A8UT4A378QY3kGgAwjxw_vWBKyE7prnhTANPWCUBjodeDgMUj818831Jgt_ZJMcSqy_NLQVMOI5LvnEkkhbo=', start_index=18848)
Annotation(end_index=18961, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0lwlcbQUFeQKBsg1K1XiI9tFKgF1brU8Qo9WGSrJU0uuGkwGyeFQMpDxMWS7W4dYOrzyHEpUvYiykloyv_SABswfGMyb2044rl_DdOuAzsvas9WAVJTFJpVduRMEglpWqtksvFmtUTgzlcKF9bnqLO1vAKrvLp0S2hZRnWORiL05gxfppFpEMKDjcW5KOOEbh1G1_eYMHMla-i6XYJLLBRmJAF_rMjMgTtimQhg==', start_index=18948)
Annotation(end_index=18961, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEHHFmnQ67rZznWVmjpQYWzk7ydN0Th3zb_bOOn9Dv7AG6kUkBLibuFIgnGKyVBVf41j0QfssmJo8q-e0KfW9S1CLkGk4eHif6zSsVYPPllZYQY-ZFR2g4AfzWzp_F3RqsuKEsCqexkQ4XyV0sa2ogyX7dcjpHHEmdlT0FD964lmHC7hoUxgx5yk9X103Uq8dSanrLAHVSZuokGj_Aaj7j3OR05B9Ykg==', start_index=18948)
Annotation(end_index=19070, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHI1rBOPmEgz8j4cONMECbcUJOArVfF1ubzLL9bjJrCM0YDLm2Pj6q5LHnRNfIGJvi-XSuHhbOO_HCYrPaX75xHcHY4i5TO-jqFAWJrrqBFwD7fTd1jCptOBZal6XzIFFC9LNpMYRg=', start_index=19061)
Annotation(end_index=19149, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_aAMuGEXIL8X1Z4fU2r-Pn6R0AXLCWtg2hKqiM6LmRUreUHse6jZk5nElDsn7cL-IXTi6FSYWYpg8QO3bWh-zUPoF3s3NSCa1pJTYUe7ifeNVHSTl', start_index=19140)
Annotation(end_index=19202, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpCrn_pL98cOqDZeQE8QF_ZpaKP5aOll2r5ELGs4tGBstvWRAsW56QwuJ5A7ZBFXLruQyuiU87ZY-Ssdnro8Oro7lbJFFyzMm145dDrvOLjmUKsGmBIW-w3qWWrWK2NbSvHRVPMnl0YMud47gQ6J1ck11dYg==', start_index=19193)
Annotation(end_index=19267, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0Utu_A3vWtRo4VQE-PgMkPMut-PGeCzBvuiAK2eroo8EHUM2XyQ1cXBODQGYqTHSL_UK-xmtlzZIrwzzIesntqHNekIjDb2A30jNAZST2m5huQfGTvxTlk086oXCJtgRLiLUvo75URm1OsrQa_b4=', start_index=19257)
Annotation(end_index=19329, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-uEgPRQlZRe4-XjNAJ6VJUdxfhVC-yWCq0hvgWal5V58gZXi17SglX0yCdejlrmjJVXE2BBs0ASfT2dDZvltVL-v4eAtTBG_EvgoLh6ZCCa3utWGrolfqen3i-U4EEq3QLQ2W4QtoDm8=', start_index=19320)
Annotation(end_index=19395, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEatlUiwxKD21_8w1qDlVp3xIWg7AH7_Tkkj28q0sA2WnCv6OTGGSJ8jqt5kC8RbuEAWLyPJmsx74o6xSL39tjOMhKnNRirkCjmnj8Nb0uVbvhq17XuNmPNhZFpZLOnkDMMoZDM', start_index=19386)
Annotation(end_index=19462, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0mW5z28La6jr0OTKINcz5hAnYYQQOVKPUysZVB82d7Q4bZWmfo813bod9KaneudiKPvPzHPdFgzkNs7NGMZXwMgwh3XIexyH5O-7y1C82MsvO6PyvstJPORu-rR_bJLfbp9xNv4Pbyk6R1b3zg7fPXeQoUi6BgAI9RN5MtjCCREvp9_7TCS2wTvYxSJbFdGPvBYSTI0AK', start_index=19448)
Annotation(end_index=19462, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAKX0TDQ6rvKbzhNLRE3VelZx5f8x6YxG3YtSCmQ8ote-zgDQMF3WhuzKanmesaIdZcLUfv2tmWg9NSH4oRE8h8zlOt5d9ld2zBf9ARc8Hiyo8s9hxQA==', start_index=19448)
Annotation(end_index=19527, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg1oNlpjV4Vemzcr-sLS1MReDpIWguV_Hjr1STcnpE5FUnrHmjWJn-oybwRrYGGzmYc9KOHQiEfv_N8t3Ax9Xw9HZ-DeDnkzJb8of0CyrqTpl_2EJQwo_KtpGOlFJkwbySuNVMb2Vj_9om_F7Fp9WKa1Wmx-5Hq5tfccGH4MNftb8Ee1_93-FhfmQAoWmNdQo4SRHAv3fuFY0=', start_index=19517)
Annotation(end_index=19581, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiwGAAuNbl4ueeAINU_G7VAZ-9pULMnjumLUvyI6NPfhQdsDgjdchcbKGdDtpRdjr7JDdxqDUjr5JTuqjG-XLyw9GvUC7cX3ry_qHj7q0Ty-Yx_I5dIbcdXjmUxxWLAeZAgqnPsEOSXNIydQBsEuc8TeNrNrz4V7LKAYU4uRb63TUYTfbuuXBiTF1KHJddwnsDuO8=', start_index=19572)
Annotation(end_index=19642, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG86aumjWeJ6ocDQYVUrqsYxK9pJAOeccJitwEF-0VIgX7aRm42n3SIzr7NHhnp4LYhEAx0IQ6rKY8n3svszER_vJ6bF95NlDnwBDg2OgCbBZq0JYFSy2q7kqRQ8QxLP6ycRUlh4ckkwcDPuCxGTJIo0HykkkgaMWhC2BbXA-HUiF4FLjaVMeL7D5a6Ud0rOb7k-JfBmb1lRWoY', start_index=19633)
Annotation(end_index=19704, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPhUnfCr6v4e-YtZT1Yx4kRhDYX_RRYWDCl3Zr-9oeb1pGidGB3g643VhA6TRT-DYtmTEW0D22FOhfSHgYivqgBROXlM-bcvZgnrLkBrk6OOx5fBNQ-2ggxd1pLeQjlTf8wB7yKD9vnC8M1FFg_sNg7JLPP2FzfB4=', start_index=19694)
Annotation(end_index=19772, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjnxWV4icHGbiBc0A4qv1ChpN9Ukkl7tV3JkbwTguB6MLSbYN5umvyPhdl2wpuF0lMOlPeS5lJhXAjwwiOHu0aiHrqRq_eKAcqPJP11X77erbsSRVbuOdqkE7FS6Jzun9Jq9_tZgNEiBJETRuuTvk9azX22JoelCOiQSV2E04RrdQgzkYz4eIqMdwzwPkgfTNfyWJWecx6MxczzyxuQ2sMwHDTH5BJVPJpNR1yZYKzMpZpIdA056Qd9RE3l1UX', start_index=19758)
Annotation(end_index=19772, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-P6o5tyhzmnTa0a4uABr5cN0TGUAGqa2r5PLfpRCsp4utS-DeSeEoAXHhndPUfu8nIeJ7KFbGilWNxasvb_wUQXRYGl_ap46deGtyMLcIjrie8e1muw==', start_index=19758)
Annotation(end_index=19877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEclhx_BxEtHQA8XxytNdMGAhLEWNU0yrAogmbZxh9HhdIbPAPxFecJ-Pn39Djg6j9DufRUCME9d6eGyZVr7uCRRHcPGa8bYt_-vnLw-5Yd_C8MlawbekWJkW8WspJX', start_index=19839)
Annotation(end_index=19877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEi4tRBl5uhbvG-ateNStKOwIL8cUK_n9TKbziBreFRp8zAu4qD4pccVw9Mv0bzpxtGQeRgwxL0OzSk-lINqjjS1In935AkZduiTuSUD_T-zrki887-tc5gARSBsokSW7ltlPgwimGhG1UUguRjrZyxqtlfM0JYeUwb67mvPcfc', start_index=19839)
Annotation(end_index=19877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEogC6vCsCIpC7HrcbuRA7-C4a6TQIn-m2OgUJMyPX7zoMOX5wygNr5jP4uCWszgFMDs0wvvOLKKpWVTL8v17Le1-b02mOfqrw6Lf_fEfWf-HlUmZlcRN-lsg0-eAqhTmedwyylkGcjlFL7vyoDt9VlZ5NgsUMDJg1jFt0gWuvm7P0LaPBanL2XOf3XFOEK0P5UcGFF97YA3gxOxuJZQbCpKMZnLvfrQB7__UklNMIBUsswbbjLKkgBkN_H', start_index=19839)
Annotation(end_index=19877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGomjvh7n1c9SMj3n94dw3FDCalbhXub1DOJlK7-hl7i3iIwEh5ubBVBa-mSAhbiQKKgGOT-3HRzZol3P8SvWXDMG_qspdccHgzCgxWxTp4AVfCtGutolBtxAXxqGtrZmT-Ar8e4rEBBPP_F_tMqKo5H9kUhKg=', start_index=19839)
Annotation(end_index=19877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQjUac4B4K21NjBJj3ykybA_VxiebNJDGp9S1QI_oWhMkMXSgKg4LyzoIUztUWUU94sk6WWYXb4yrcpD5vGHMkAA_3yeIwC6vmRMCMuCOxmrBr2yg_r1z6-A2Asao8HaNmTHwRwIXksiyA8W8-3mrw_i5k45hOM2AqBkMiiYMe8Rch-V6-w4kq5_0fJgCjQdku673GMdEIZwbV8_L2hM0OIAjrVFzbhXsEbA==', start_index=19839)
Annotation(end_index=19877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVyuAfIUjJrGXPVu1ZAi-X9zg4nHJeTa2ShgNxA1kLICX3u1QUuA3afkw9wBI5nJhg_V1_lrTs1zqGr5xUORbkcvnAcJS1QKmMrnlRDW41kczQKGL0ecU6_6D0K5MCncT9GOec7n0NqX-I6JiGVlFRhZHa-fv82Yk=', start_index=19839)
Annotation(end_index=19877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmA2fpb_9jekwegle7aZqWWrqblzLZ66ycy69bnQgQ-WL91WQ1Cx_AbiZphsomxYOuiigKhP7XTURzQ_WWrfs5LIBAblU_mbBYarpWFGUM21pj2X2Ab_e3I9RV30VN1cMBmL3QK_HLaUPVZq23loi75cT78VyEYnqvcIERuJ8HDdXll1CN2NQ-99wPJHplkjZJjYrxPQjEJJhjFYCPW74YxQSsDwXB', start_index=19839)
Annotation(end_index=19877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmDLU_ZEmgFQ49YNdTENRg2AIJJogoxE2K4DRL0KdpsLmJWtbZKCuc2KRQFJP9e9zgpyEm9I0eTkQOx-hVOEr6BvIUPPVnEUbWbViZdIq0B3J4j-Fy7kKurTBKkg-FS52Dzy2OfKtE3G_j6PK4Sw9qLy61ggjHwp-muXe0NSYVvul7qay80Jk=', start_index=19839)
Annotation(end_index=20012, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMmEjUpsJuDdMxRzd9ZN012c4o-ioewN7RRq7PkpzpM_C7QU7MXOTWHgdx23AWELxzOXEIcKQDo58G5q4ho7YNExEkAg1-5YO9yJ4iFc9UEZdfWszGszoGnaj4HsHRz5UpBPYOZmMfQ1Ly5jFMnkSnJnvPGfl07pzxK3GEKHlOUEHCONQXmx_zCDh1t117mIzapxav5wAERxIEL5MEBKZshWanDqaBsFn8oM71Qv8ZhzAuOj7nfdTAUUbmSDRDxA==', start_index=20002)
Annotation(end_index=20100, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHozuszwYJ9uV7BSvElL2f7GvaPeEfRSYvY18o37bA5DvA3N7WsRqokPRwqVcgkN3wQpGVfZONbpJKmylxTIjiwUbDK5Vy_DWG44merdT_5YVuAKQQ5OMH3Hd5pPCjKPQ==', start_index=20090)
Annotation(end_index=20170, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEzNSpuLA3DKzCEwBsGG13i_vFpJddGPEE_Cf5gcbq-iXgiS_lmXUW0uUYksQ-C11kgI4jHYVZP5TzeUn-0qLSn2RmClTOFcZp01ymjq__KHPic0iCZAOmLhaF_2YWSbDYen2tHnTnn_3FpHKKDdCSGgjQHZIKObfOhVLV7DI-oAa0zdRdmVZDWgaH2M-pf8DPqGYCSLh86w==', start_index=20160)
Annotation(end_index=20238, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSWoKWdmn2IzP3awl_VL7lGz4B2heLBSk3J7dwTp_qTTR5VsESiJXUpU2nNmsW1e535gFL5WmiuMRmlTrsdFJv7rQXTjZ273AaWzgn4i86liWRKCa22qwV95qzxMe8cePnXgfNbqHHuRSXUxs=', start_index=20228)
Annotation(end_index=20291, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCDMeSOlE2pTNj7f6NLGKxzA7SRmR7wJXprVBx9K3VAg_k5e921ae8M6eSgUpVUmpNUKJvzVBC9mVWH0nDobxXyWB3Zg2dpyU3PuUfU_0-D__FHe2YH7TAy7MiEzwjmkvSJGgECGEc8-HT0jyF3psTttWMY9k7Ajd9G5QLGRwY7ohzaeIpIGmIESIOG5JDZbKHUjaPU-AF5GnO6buLXP9IbT_T_iQguuLsZ6Cyfw==', start_index=20281)
Annotation(end_index=20350, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGetdi2uZLpOscK3z_gwy0HiyKqMePrpalCJAkN89IqlbZJrACGqc64VfSPOASMsDxB6iitO4D4RxOVGueN5MIv1gelMDkuL6a9_33fRHOjy3zObyLdsWOpWw==', start_index=20340)
Annotation(end_index=20427, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0yDee5nAADBuongKsIFsrb6Rpwa3Se2c2POVHKane9YjlcXlw9bIekSosQUFhnXOliOjFh2r2AGjdY-ts2c8dE2CdIZ2RqqZBxFRHpKoYqNgcdItu8g==', start_index=20409)
Annotation(end_index=20427, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuNx916jAGBEs2RlWA5goncR19kKEkdHAOBBIecaNlMnU_7wkU2B_DocBNfRO6i9xsOiiqEjDj5eIwuWPGMi2YkKinHKuxkXoEPbS-mAel8RgUujseqqMeiw==', start_index=20409)
Annotation(end_index=20427, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBONUPK8cQ4WYnm4nZ-I5q-WPryQs_Ijw46PQ-8d1Tzvscz4j8civMvfQAOnn3Yk1ymCFl4Liz_sbNU9ikXeMao_qlBS8damTeukT9Y1pKE9i2SIEd0Q==', start_index=20409)

## Sources
