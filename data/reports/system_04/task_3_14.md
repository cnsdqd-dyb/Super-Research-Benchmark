# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 6623f32b | **Time:** 362.70s | **Cost:** $1.68915
--------------------------------------------------------------------------------

# Edge Weight Optimization and Markov Equilibrium in Migration Networks

### Key Points
*   **Determinant of Equilibrium:** In migration networks modeled as Markov chains, edge weights (transition probabilities) are the fundamental mathematical determinants of the long-term regional population distribution (the Markov equilibrium or stationary distribution). Altering these weights is the primary mechanism for shifting the equilibrium state.
*   **Convergence Speed Optimization:** Edge weight optimization plays a critical role in determining the rate at which a population distribution stabilizes. This is mathematically formalized as the "Fastest Mixing Markov Chain" (FMMC) problem, where weights are optimized to minimize the Second Largest Eigenvalue Modulus (SLEM), thereby maximizing the mixing rate.
*   **Policy and Utility:** In human migration models, edge weights are often endogenous, resulting from individuals optimizing their personal utility (based on wages, amenities, and migration costs). "Optimization" in this context can also refer to policy interventions (e.g., taxes, incentives) designed to adjust these weights to achieve a socially optimal population distribution rather than a purely competitive equilibrium.
*   **Spectral Control:** The spectral properties of the transition matrix, specifically the spectral gap, dictate the system's resilience and speed of adaptation to disturbances. Optimizing edge weights modifies this spectrum, allowing planners to control both the final distribution and the system's dynamic responsiveness.

---

## 1. Introduction

The study of migration networks—whether describing the flow of human populations between cities, the movement of refugees across borders, or the biological dispersal of species—relies heavily on mathematical modeling to predict long-term outcomes. Among the most robust frameworks for this analysis is the Markov chain, which models migration as a stochastic process where the probability of moving from one region (node) to another is governed by transition probabilities (edge weights). The "Markov equilibrium state," or stationary distribution, represents the long-term population distribution where inflows and outflows for every region are balanced.

The query regarding the role of **edge weight optimization** in establishing this equilibrium touches upon the intersection of graph theory, linear algebra, and socio-economic modeling. Edge weights in migration networks are not merely static constants; they are dynamic variables that can be optimized—either by a central planner seeking stability or by individual agents seeking utility—to alter the system's trajectory.

This report provides an exhaustive analysis of how edge weight optimization influences the Markov equilibrium. It explores the mathematical mechanics of how weights determine the stationary distribution, the optimization of weights to maximize convergence speed (the Fastest Mixing Markov Chain problem), and the socio-economic implications of optimizing weights to achieve desirable population outcomes.

## 2. Theoretical Foundations: Migration as a Markov Process

To understand the role of edge weight optimization, one must first establish the mathematical framework of migration networks as Markov chains.

### 2.1 The Migration Network as a Graph
A migration network is defined as a directed graph $G = (V, E)$, where:
*   $V = \{1, 2, ..., n\}$ represents the set of regions or nodes (e.g., cities, rural areas, countries).
*   $E \subseteq V \times V$ represents the set of possible migration routes.
*   $W$ is a weight matrix where $w_{ij}$ represents the "weight" or strength of the connection from node $i$ to node $j$.

In the context of Markov chains, these weights are normalized to form a **transition probability matrix** $P$, where $P_{ij}$ is the probability that an individual in region $i$ migrates to region $j$ in a given time step [cite: 1]. The fundamental constraint for a valid Markov model is that the sum of outgoing probabilities from any node must equal unity:
\[ \sum_{j=1}^{n} P_{ij} = 1 \quad \forall i \in V \]

### 2.2 The Markov Equilibrium (Stationary Distribution)
The population distribution at time $t$ is given by a row vector $\pi^{(t)} = [\pi_1^{(t)}, \pi_2^{(t)}, ..., \pi_n^{(t)}]$, where $\pi_i^{(t)}$ is the proportion of the total population in region $i$. The evolution of the population is described by the recursive relation:
\[ \pi^{(t+1)} = \pi^{(t)} P \]

The **Markov equilibrium state**, or stationary distribution $\pi^*$, is reached when the population distribution remains invariant under the transition matrix:
\[ \pi^* = \pi^* P \]

Mathematically, $\pi^*$ is the left eigenvector of $P$ corresponding to the eigenvalue $\lambda = 1$. The Perron-Frobenius theorem guarantees the existence and uniqueness of this equilibrium for ergodic (irreducible and aperiodic) chains [cite: 2].

### 2.3 The Role of Edge Weights
The edge weights ($P_{ij}$) are the "knobs" of the system. They directly determine the values in the eigenvector $\pi^*$. Therefore, **edge weight optimization** is the process of adjusting these $P_{ij}$ values to achieve a specific objective, which generally falls into two categories:
1.  **Targeting a State:** Adjusting weights so that the resulting $\pi^*$ matches a desired population distribution (e.g., avoiding overpopulation in urban centers).
2.  **Targeting Speed:** Adjusting weights so that $\pi^{(t)}$ converges to $\pi^*$ as quickly as possible (maximizing the mixing rate).

## 3. Edge Weight Optimization for Convergence Speed: The Fastest Mixing Markov Chain (FMMC)

A critical aspect of migration network analysis is not just *where* the population will settle, but *how long* it takes to reach that equilibrium. In dynamic environments (e.g., refugee crises or rapid urbanization), a slow convergence rate can lead to prolonged instability. Edge weight optimization plays a central role in minimizing this transition time.

### 3.1 The Mixing Rate and SLEM
The speed at which a Markov chain converges to its stationary distribution is governed by the spectral properties of the transition matrix $P$. Specifically, the convergence rate is determined by the **Second Largest Eigenvalue Modulus (SLEM)**, denoted as $\mu(P)$ [cite: 3, 4, 5, 6].

Let the eigenvalues of $P$ be $1 = \lambda_1 \geq |\lambda_2| \geq ... \geq |\lambda_n|$. The deviation of the population distribution from equilibrium at time $t$ decays according to:
\[ ||\pi^{(t)} - \pi^*|| \leq C \mu(P)^t \]
where $\mu(P) = \max(|\lambda_2|, |\lambda_n|)$.

To achieve the fastest convergence (mixing), one must minimize $\mu(P)$. This is known as the **Fastest Mixing Markov Chain (FMMC)** problem [cite: 3, 5, 7, 8].

### 3.2 Optimization Formulation
The problem of optimizing edge weights to maximize convergence speed can be formulated as a convex optimization problem. Given a graph topology (which edges are allowed to have non-zero weights), the goal is to find the matrix $P$ that minimizes the SLEM:

\[ \text{minimize } \mu(P) \]
\[ \text{subject to: } \]
\[ P_{ij} \geq 0 \quad \forall (i,j) \in E \]
\[ P_{ij} = 0 \quad \forall (i,j) \notin E \]
\[ \sum_{j} P_{ij} = 1 \quad \forall i \]
\[ \pi^* P = \pi^* \quad (\text{if a specific equilibrium is constrained}) \]

Research by Boyd, Diaconis, and Xiao [cite: 5, 8] demonstrates that this problem can be cast as a **Semidefinite Program (SDP)**. This allows for the efficient computation of optimal edge weights that guarantee the fastest possible stabilization of the population distribution.

### 3.3 Implications for Migration Networks
In the context of migration, solving the FMMC problem has profound implications:
*   **Crisis Management:** In refugee scenarios, optimizing the "weights" (capacity and flow rates of transit routes) can ensure that refugees are distributed to safe havens (equilibrium states) as quickly as possible, minimizing the time spent in transient, unstable states [cite: 9].
*   **Urban Planning:** Planners can adjust transportation connectivity (edge weights) to ensure that a region reaches a balanced population distribution quickly after a disturbance (e.g., a new housing development or industry opening) [cite: 1].
*   **Robustness:** A network with optimized mixing rates is more robust to perturbations. If a sudden migration shock occurs, a system with optimized edge weights will return to equilibrium faster than a non-optimized one [cite: 6].

## 4. Endogenous Edge Weight Optimization: Economic Equilibrium Models

While the FMMC approach views edge weights as parameters to be tuned by a central planner, economic migration models view edge weights as the outcome of **individual optimization** by migrants. In this view, the "optimization" is performed by the agents themselves, and the Markov equilibrium is the aggregate result of these individual choices.

### 4.1 Utility Maximization and Transition Probabilities
Pan and Nagurney [cite: 2] developed a network equilibrium framework where migration flows are determined by utility functions. An individual in location $i$ will move to location $j$ if the utility of living in $j$ (minus migration costs) exceeds the utility of staying in $i$.

The transition probability $P_{ij}$ is not fixed but is a function of the population distribution and flow:
\[ P_{ij} = f(U_j, C_{ij}, \pi) \]
where:
*   $U_j$ is the utility of location $j$ (often a decreasing function of population density due to congestion).
*   $C_{ij}$ is the transaction cost of moving from $i$ to $j$.

### 4.2 The Variational Inequality Formulation
The equilibrium state in this context is defined by a **Variational Inequality (VI)** problem. The population distribution $\pi^*$ is an equilibrium if no individual has an incentive to unilaterally change their location. This is a more complex form of Markov equilibrium where the transition matrix $P(\pi)$ is itself dependent on the state vector $\pi$ [cite: 2].

### 4.3 Social vs. Individual Optimization
A critical distinction arises between the **user-optimized equilibrium** (where every migrant maximizes their own utility) and the **system-optimized equilibrium** (which maximizes total social welfare).
*   **User-Optimized:** Migrants ignore the negative externalities they impose (e.g., congestion). This leads to a Nash equilibrium that may be inefficient.
*   **System-Optimized:** A central planner would "optimize edge weights" (flows) to maximize total societal utility.
*   **Policy Intervention:** Ferrari and Garaud [cite: 10] discuss how incentives (taxes, subsidies) can be used to alter the perceived costs $C_{ij}$. By optimizing these costs, the planner effectively optimizes the edge weights of the Markov chain to shift the equilibrium from the user-optimized state to the socially optimal state.

## 5. Establishing the Equilibrium State: The Inverse Problem

Beyond speed and utility, edge weight optimization is used to solve the **inverse eigenvalue problem**: determining the weights required to sustain a specific, target population distribution.

### 5.1 Designing for Stability
Suppose a government wants to maintain a population ratio of 70% urban and 30% rural ($\pi^* = [0.7, 0.3]$). The problem is to find a transition matrix $P$ such that:
\[ [0.7, 0.3] P = [0.7, 0.3] \]
There are infinite matrices $P$ that satisfy this. Edge weight optimization allows the selection of the "best" $P$ among these candidates—for example, the one that minimizes total migration cost or maximizes network entropy [cite: 11].

### 5.2 Entropy Maximization
In the absence of detailed constraints, the Principle of Maximum Entropy is often used to estimate edge weights. This approach constructs the transition matrix that is consistent with the known constraints (e.g., average travel distance) while making the fewest assumptions about the unknown micro-behaviors. This results in a "most likely" equilibrium state [cite: 11].

### 5.3 Controlling Mobility via Edge Weights
Research on pandemic mobility networks [cite: 12] highlights a form of subtractive optimization: **reducing** edge weights to restrict flow. By selectively lowering the weights of edges with high centrality (betweenness), authorities can fragment the network or alter the equilibrium distribution to prevent the spread of contagion (or in a migration context, to prevent overcrowding). This is an optimization problem where the objective is to minimize the spectral radius or connectivity of the graph.

## 6. Case Studies and Applications

### 6.1 Urban-Rural Population Migration
Shen and He [cite: 1] utilize Markov chains to predict the saturation point of urbanization in China.
*   **Context:** Rapid industrialization drives rural-to-urban migration.
*   **Edge Weights:** Calculated from historical data (e.g., 1% urban-to-rural, 4% rural-to-urban).
*   **Equilibrium:** The model predicts a future saturation state where the flows balance.
*   **Optimization Role:** The study implies that "human factors" (policy, disasters) act as perturbations to these weights. Optimizing urban planning policy (changing the weights) can shift this saturation point to a more sustainable level, preventing "over-urbanization."

### 6.2 Refugee Crisis Modeling
Unwin [cite: 9] applies Markov chains to the Burundi refugee crisis.
*   **Context:** Refugees move between camps and cities based on safety and distance.
*   **Edge Weights:** Derived from distance thresholds and local properties.
*   **Optimization:** The study compares Markov models to agent-based models. Optimizing the edge weights (e.g., by placing aid stations or transport links) allows humanitarian organizations to predict and influence the final distribution of refugees, ensuring resources are allocated where the equilibrium will form.

### 6.3 Biogeography-Based Optimization (BBO)
While an algorithmic analogy, BBO [cite: 13] provides a theoretical testbed for migration logic.
*   **Mechanism:** Solutions "migrate" features between each other based on fitness.
*   **Edge Weights:** Migration rates are optimized (e.g., sinusoidal vs. linear models) to improve the algorithm's convergence to the global optimum.
*   **Relevance:** This confirms that the *functional form* of the edge weights (how they change with population/fitness) is a critical factor in determining whether the system reaches a high-quality equilibrium.

## 7. Computational Methods for Weight Optimization

The actual process of finding optimal edge weights involves sophisticated computational techniques.

### 7.1 Semidefinite Programming (SDP)
As mentioned regarding FMMC, SDP is the gold standard for optimizing spectral properties [cite: 3, 5].
*   **Primal Problem:** Minimize the spectral norm of the deviation matrix.
*   **Dual Problem:** Maximizing the nuclear norm of a related matrix.
*   **Application:** For a migration network of $N$ cities, an SDP solver can determine the exact transition probabilities between every pair of cities that would result in the fastest stabilization of the population.

### 7.2 Metropolis-Hastings and Heuristics
For very large networks where SDP is computationally expensive, heuristics are used:
*   **Metropolis-Hastings:** Assigns weights based on node degrees to ensure a specific stationary distribution (usually uniform). This is a standard method for "designing" a chain with a known equilibrium [cite: 5].
*   **Maximum-Degree Heuristic:** Assigns weights inversely proportional to the maximum degree in the network.
*   **Subgradient Methods:** For large-scale optimization of the SLEM [cite: 5].

### 7.3 Distributed Optimization
In decentralized migration networks (where no central planner exists), distributed algorithms can adjust weights locally. Agents (or local governments) adjust their incoming/outgoing flow restrictions based on local information, iteratively converging toward a global optimum [cite: 6, 14].

## 8. Detailed Analysis of Key Research Contributions

### 8.1 Pan & Nagurney: Network Equilibrium
The work of Pan and Nagurney [cite: 2] is pivotal because it bridges the gap between static Markov models and dynamic economic theory.
*   **Contribution:** They proved that if utility functions are monotone (e.g., utility decreases as population increases), a unique equilibrium population distribution exists.
*   **Edge Weight Dynamics:** They explicitly model the transition matrix $P$ as time-varying ($P^{(t)}$). The "optimization" is the iterative process of solving the variational inequality at each step.
*   **Significance:** This confirms that edge weights are the transmission mechanism for economic forces. If wages rise in City A (utility increases), the edge weights pointing to A increase, and the Markov equilibrium shifts toward A.

### 8.2 Boyd, Diaconis, & Xiao: Fastest Mixing
This work [cite: 5, 8] provides the rigorous mathematical proof that edge weights determine convergence speed.
*   **Contribution:** They showed that the mixing rate is determined by the spectral gap ($1 - \mu(P)$).
*   **Optimization:** They provided the convex optimization framework to find the "best" weights.
*   **Significance:** In migration policy, this implies that simply having open borders (edges exists) is not enough for stability; the *capacity* (weights) of those borders must be tuned to prevent oscillation and ensure rapid settling.

### 8.3 Ferrari & Garaud: Social Utility
Building on Pan & Nagurney, Ferrari and Garaud [cite: 10] introduce the conflict between individual and social optimality.
*   **Contribution:** They demonstrate that the "natural" Markov equilibrium (result of selfish edge weight optimization) is often suboptimal.
*   **Optimization:** They propose using incentives to modify the flow functions (edge weights).
*   **Significance:** This justifies government intervention in migration networks. By optimizing the cost parameters (a component of edge weights), the government can align the Markov equilibrium with the social optimum.

## 9. Conclusion

In migration networks, edge weight optimization is the decisive factor in establishing the Markov equilibrium state. Its role is threefold:

1.  **Defining the State:** The specific values of edge weights (transition probabilities) mathematically define the stationary distribution vector. Changing weights is the only way to permanently shift the long-term population distribution.
2.  **Controlling Convergence:** Optimization of edge weights (specifically minimizing the Second Largest Eigenvalue Modulus) determines the speed at which the population reaches equilibrium. This is crucial for minimizing instability during transition periods.
3.  **Aligning Incentives:** From an economic perspective, optimizing edge weights (via costs and utilities) allows for the alignment of individual migration choices with socially optimal outcomes, preventing overcrowding and resource depletion.

Whether viewed through the lens of spectral graph theory (FMMC), economic equilibrium (Variational Inequalities), or urban planning, the optimization of edge weights is the primary lever for understanding and controlling the dynamics of regional population distribution.

---

## 10. Extended Discussion: Mathematical Derivations and Advanced Concepts

### 10.1 The Perron-Frobenius Theorem in Migration
The existence of a stable regional population distribution relies on the transition matrix $P$ being **stochastic** (rows sum to 1) and **irreducible** (every region is reachable from every other region).
*   **Irreducibility:** If the network is reducible (e.g., a sink node exists from which no one leaves), the population will eventually accumulate entirely in the sink. Edge weight optimization often involves ensuring irreducibility (adding small non-zero weights to all edges) to prevent total depopulation of rural areas [cite: 2].
*   **Aperiodicity:** If the network is periodic (e.g., bipartite migration where populations swap every year), convergence does not occur. Optimizing weights (adding self-loops, $P_{ii} > 0$) breaks periodicity and ensures convergence [cite: 5].

### 10.2 Spectral Gap and Resilience
The **spectral gap** $\gamma = 1 - \mu(P)$ is a measure of the network's connectivity and resilience.
*   **Large Gap:** Fast convergence, high resilience. The population distribution recovers quickly after a shock (e.g., a natural disaster displacing people).
*   **Small Gap:** Slow convergence. The system has "memory" and disturbances linger for a long time.
*   **Optimization:** Planners aiming for a resilient migration network should optimize edge weights to maximize this spectral gap. This often involves strengthening "weak ties" or bottleneck edges in the migration graph [cite: 6].

### 10.3 The Inverse Frobenius-Perron Problem
The problem of finding a matrix $P$ such that $\pi P = \pi$ for a given $\pi$ is known as the Inverse Frobenius-Perron problem.
*   **Constraint:** The topology of the migration network (which $P_{ij}$ can be non-zero) is usually fixed by geography.
*   **Solution:** Edge weight optimization algorithms use gradient descent or genetic algorithms to adjust the non-zero $P_{ij}$ values until the error $||\pi P - \pi||$ is minimized. This allows researchers to "reverse engineer" the migration rates that must have existed to produce a current population distribution [cite: 11].

### 10.4 Entropy Rate and Migration
The **entropy rate** of the Markov chain, $H(P) = - \sum_i \pi_i \sum_j P_{ij} \log P_{ij}$, measures the randomness or unpredictability of migration paths.
*   **Optimization:** Maximizing entropy (subject to constraints) produces the "most neutral" model of migration.
*   **Minimizing Entropy:** Corresponds to highly deterministic migration (e.g., forced migration or strict border controls).
*   **Equilibrium:** High-entropy networks tend to have more uniform equilibrium distributions, while low-entropy networks can support highly skewed distributions (e.g., extreme urbanization) [cite: 11].

## 11. Future Directions in Research

The intersection of edge weight optimization and migration networks is evolving with new data sources and computational powers.
*   **Real-Time Optimization:** With mobile phone data, edge weights can be estimated and optimized in real-time (e.g., during a disaster evacuation) to direct population flows dynamically [cite: 15, 16].
*   **Machine Learning Integration:** Neural networks are being used to predict non-linear edge weights based on complex socio-economic features, allowing for more accurate equilibrium predictions than traditional gravity models [cite: 17, 18].
*   **Multi-Layer Networks:** Modern migration happens on multiple layers (physical, economic, social). Optimizing weights on one layer (e.g., digital connectivity) can influence physical migration weights, requiring multi-layer Markov models [cite: 19].

## 12. Comprehensive Literature Review

### 12.1 Classical Markov Migration Models
*   **Rogers (1966):** Established the matrix algebra of interregional population growth.
*   **Shen & He (2022) [cite: 1]:** Applied Markov chains to modern Chinese urbanization, demonstrating the predictive power of the equilibrium state.
*   **Unwin (2019) [cite: 9]:** Demonstrated the superiority of Markov chains over agent-based models for refugee flows due to computational efficiency and analytical tractability.

### 12.2 Optimization and Control
*   **Boyd et al. (2004) [cite: 5]:** The seminal work on FMMC. While abstract, it provides the solver for the "speed of convergence" problem in migration.
*   **Pan & Nagurney (1994) [cite: 2]:** The foundational text for "Network Equilibrium" in migration, linking utility theory to Markov stability.

### 12.3 Network Science Perspectives
*   **Tong et al. (2012) [cite: 12]:** Discussed edge weight manipulation for controlling diffusion (epidemics/migration) on graphs.
*   **Ferrari & Garaud (2015) [cite: 10]:** Provided the explicit link between social utility maximization and the resulting Markov flows.

## 13. Summary of Findings

The role of edge weight optimization in establishing the Markov equilibrium of regional population distribution is fundamental and multifaceted. It is the mechanism by which:
1.  **The Target is Set:** Weights define the eigenvector $\pi^*$.
2.  **The Speed is Set:** Weights define the eigenvalue spectrum and mixing rate.
3.  **The System is Tuned:** Policy makers and individuals optimize weights (costs/utilities) to align the system with desired economic or social outcomes.

Without edge weight optimization, migration models would be static descriptors. With optimization, they become powerful tools for planning, policy analysis, and crisis management, allowing us not just to predict where people will go, but to design networks that ensure they arrive there safely, efficiently, and sustainably.

## 14. References
*   [cite: 1] Shen, S., & He, Y. (2022). *Markov chain equilibrium regional population distribution migration*. Atlantis Press.
*   [cite: 9] Unwin, H. J. T. (2019). *The application of Markov chains to modelling refugee crises*. arXiv.
*   [cite: 20] *India migration Markov chain analysis*. IJCRT.
*   [cite: 12] *Reducing edge weights in mobility networks*.
*   [cite: 2] Pan, J., & Nagurney, A. (1994). *Using Markov Chains to Model Human Migration in a Network Equilibrium Framework*. Mathematical and Computer Modelling.
*   [cite: 10] Ferrari, C., & Garaud, P. (2015). *Exploring Equilibrium of A Markov Chain Model of Migration and Social Utility*.
*   [cite: 3] *Fastest Mixing Markov Chain (FMMC) problem*. arXiv.
*   [cite: 19] *Edge weight indicators in urban agglomeration networks*. MDPI.
*   [cite: 18] *Dynamic Population Distribution Aware Human Trajectory Generation*.
*   [cite: 2] Pan, J., & Nagurney, A. *Multi-stage network equilibrium model of human migration*.
*   [cite: 11] *Population entropy and phase transitions*. PMC.
*   [cite: 8] Boyd, S., Diaconis, P., & Xiao, L. (2004). *Fastest Mixing Markov Chain on a Graph*. SIAM Review.
*   [cite: 1] Shen, S., & He, Y. *Prediction of Population Migration Changes*.
*   [cite: 5] Boyd, S., et al. *Fastest mixing Markov chain on a graph*.
*   [cite: 2] Pan, J., & Nagurney, A. *Network Equilibrium Models*.
*   [cite: 10] Ferrari, C., & Garaud, P. *Markov Chain Model of Migration and Social Utility*.
*   [cite: 6] *Convergence rate and second largest eigenvalue modulus*.
*   [cite: 14] *Decentralized Control of Connectivity*.

**Sources:**
1. [atlantis-press.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcgQWcCTwEOJJ8YEioE5w8BW0XkO-N4_ksJrZQv7wO0lVyb_cPUAcEYORo7FCHwTpskiKrLPVUBXE6pMcCWQHfww62bSL1cM9IvGelBezN2hiK68bDTT1qoK3KRtKs0wF5NtMOiXBXcyPL)
2. [umass.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgeVeTVHo2RiW1WMv3IY75fbAWnT0G9OJ99KGlafmHd6pr2aJyeCR4U3RW7eOsi_FAggZN3F92tHM08WtBhOOXrakTD3px8fkHNXCTeaRH34N0yI7nzlz-UyPEpQowy0yTuFGnr6iV9uLFL7E=)
3. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJRz7N79ZjsEJZBbcOtPulgLS-mzX4Ve0n290pmrjTjb-GXyO_N8-rtDAx8SGcWxif2ixa8qQaWYH8UarwWislYrnBDPmuhKGv687Xd6ydLCmhR9b8fA==)
4. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFefR2iqD1-d_kxFEMnRzlOYpmya71fK4uPsTZWRaQdjwGmKDfgTVIJB261OMHNHBuv5_tWd59S_wb4aJCAg3qkstv6Vrd-sOdyf3yqREKJd6iuflLq)
5. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWk_UciGUA92ZujZPT2svl94pxa5Yl2PbxIEcdG9BwC7tmXmdELavmr_rJfEMsoWbAOi8g5Gi6GrZTztXrO8b3k4bMM9TIZzSUMZuAEl9FdVCycpGrwhzGhqiXRLKlSuO7q-bFDqUmYw==)
6. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVU9M4cLN6c0mnMwYZxTP-c0wBaPGWebIVh1x9oh5M53o6--qCZSgFkynX1rt3WjDp3ekS4M2Y8J7FEZJ6SgVS1NuoZJfr3EKUeMAWyTmUGP-lDnwjKQ==)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4MHt29drlYJaFrR5vfB5c9DTYIG-HrU85TOJ2qO0wvpW1ABiGSUN6IcNadRs0yJe0_lEJAcywoCOQtyoeHYhFZaai_IRVcl40UkYGdDtcUbxlrDCGdxd4NGI7LAUrpvnkIgGxED3qwRhesVUEUZZRal3dJ7O5iUyhpGa_6pFbA5taKouxFTdcPOqNZMKV_jJdTSx4QmtMQCS8959nQT-M)
8. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDqzx9LhOTts99v5ccHmrKH4BZG-wWpGIxpzR65HgSJG3bcapII0MlC3uzBK8OgD2WQPiAUQD55QmYjeBfrHGcc59mlsrciDoJbRZaAx_nqNar_17q7ux3Awbf9KhbExVITuYRMrjr4cjptkC0)
9. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9WZXgxrhB0q7KU4dSqcIzR3xrB8m8fQp_darRgD7xrLJ1mQ47er8aKCtO52UCSb5QbX0fswbo3W_5PEw9seQI7PS8l1nhMRgjo6xc1QsLMrCi7DdKDg==)
10. [amazonaws.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHSx2F7VfiMQq3pMTiLwr3W4w3BQ94VgKV6FKOn0dQEVU_7SseyyrC_SAGLfjRqqkrf-1r9MvoY5wRlTriEBUp4hpR5_fzeY5zVLHvBy4suWEZKe85Uli6JDAojKANttqRcoHE0t3_SnxIAxuBFZegZ3y37m5CwMj2OJ1bcSfHVGFVVe47urRppQqqTXGarg==)
11. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmyqI_Wak6IPpgPI5-W8xuAHF_4n87dJJydT_zOcR_arycalMUEcLD05OzFLpFzmhIV7wh0OMZCLs5qtWbMUAD_hPZbiBfw-WlfGUpPMm4K_sf0vcYvLgM6kAaiF2ft233Oy0ZpjRK5Q==)
12. [hongyangzhang.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFp6TtLpLemmVRJAim5IFABDHLkiEua4OoGDqgWt3JFqyUNrKBHxMPdMehLg2CE_fQWRXPNkE4ZpEGxolRwM7ejHddHwfxqXSfPq6SiE-kem0zzXky_9-KJ1QYlwbw4dnCAmMQOuLtTb-Ke_w==)
13. [core.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkN4WGycAHroTYlKABPniTJxjUu7yUMW46X5xRFrNp9acPVkG_5ZXER16Q_dkE0YEb8ahyZiWp9uKK4tjA494K85dku2SPPJJaDTFfpWztRVdQgsTgfAAfwGixTobpe3gCjuE=)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIiiC0gniSdrR4YLcl_MtGtREvLRrbKmUQNJwKShN6nlF5MrIyhypfS2bcZgw3Sx62zzGSZwY2ctbl1r7Cg0P3V2kD9tay-2UdLN9RQHe9KnuxFcu34QWuK6PsnNp9U_WuZ41pQAoWc3t_3CS_OrViRckxX9SWHHbzFRsLxsvuVNaKpAoJ5UwyQH1Q2nAWdYzZ91J4kATw5vHEg9xOu2Wb7MTZya-K)
15. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIBochxvYp7gIE_2HBZMl9Io6RixWvSPs-ocCpp_T0ROKWu_uBIWRYfEtjzFlpEA8itdlImiY9F8bx--h-6H0nrul-_Sl2sedpsrI7KCBvqSn0RBiLhfYtIBPmVg==)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH45XN1WbA3nRXsxBHbGgURNa0UUUmOkcmZeSXV0Lea_eDAkURypd5juq9kx-KCg2FtzQko2vDtSyycY9iQgzCS30IE8MPv8ElEuK3D4yU_Hd4YCJ-m1BhM2NgCBcWhAZxOxwTbdbHcCQ2fVQ_Mhe1r0FlWmDuxU8q21y7QMNQJdpBEG0P_aD3L9hmns-6Zor7IRW2SSdoeFGQPE3EIuQ==)
17. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMObtdKXlAI4fhRMn7WIkN7h_vreMJV_W6ijgwOG7IPdFCA1qT0fUDp3JQjVs1Zu15JYboAwcMPeonGpwDIQ0rEPHO6LPDaO9eBGWjDI00qgOn_VvjduE36xmsTg4=)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECA6oFRuWdEwZrEfeFsJaBcjDS_A3eBGtmbYX_uifLSTLwEu_Ue7q-qqEQmYeZAPaE4IX-i4UsEfKRAUc6RHI9JzqTojN95asgt2q40vRcztjHk3SGe-s7fRI6LH-UvQebmlROUp0jD4ohn9RFdVODbtxTzicIU3IFR3fi3qoQBdX401fGRB7M-_jeDRfo9eUJnz7uq2Z6lqQMSbAub7oFprYzld3s8gjDFxwoudQPcTezZP-zdMfilWlum8Watgs=)
19. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLEPda_8Y8Asnkg5a7dy2iJLulNU_XywRwC1bUNDHx-8j7P1TAxSUKNKxq_ETfj8_SelDeiyvojH9Dsdo6eomq2qtcXaBZU1f6Or_QAxBbCL2Kq9BYJW3dPsky7v1gGBo=)
20. [ijcrt.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvMYUvgMsvISgzs880pw_w3PKwGok6P7ULNhW-IUP1Lf2UH2YMHebuO6iDIWfKqeMA26MNrRYznZTJgjb-aqATpsTswMxr8ispMKceAiAcdGXlTBL3Q2nR8kL7ZUFhTw==)


## Annotations
Annotation(end_index=3948, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcgQWcCTwEOJJ8YEioE5w8BW0XkO-N4_ksJrZQv7wO0lVyb_cPUAcEYORo7FCHwTpskiKrLPVUBXE6pMcCWQHfww62bSL1cM9IvGelBezN2hiK68bDTT1qoK3KRtKs0wF5NtMOiXBXcyPL', start_index=3939)
Annotation(end_index=4926, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgeVeTVHo2RiW1WMv3IY75fbAWnT0G9OJ99KGlafmHd6pr2aJyeCR4U3RW7eOsi_FAggZN3F92tHM08WtBhOOXrakTD3px8fkHNXCTeaRH34N0yI7nzlz-UyPEpQowy0yTuFGnr6iV9uLFL7E=', start_index=4917)
Annotation(end_index=6325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJRz7N79ZjsEJZBbcOtPulgLS-mzX4Ve0n290pmrjTjb-GXyO_N8-rtDAx8SGcWxif2ixa8qQaWYH8UarwWislYrnBDPmuhKGv687Xd6ydLCmhR9b8fA==', start_index=6307)
Annotation(end_index=6325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWk_UciGUA92ZujZPT2svl94pxa5Yl2PbxIEcdG9BwC7tmXmdELavmr_rJfEMsoWbAOi8g5Gi6GrZTztXrO8b3k4bMM9TIZzSUMZuAEl9FdVCycpGrwhzGhqiXRLKlSuO7q-bFDqUmYw==', start_index=6307)
Annotation(end_index=6325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFefR2iqD1-d_kxFEMnRzlOYpmya71fK4uPsTZWRaQdjwGmKDfgTVIJB261OMHNHBuv5_tWd59S_wb4aJCAg3qkstv6Vrd-sOdyf3yqREKJd6iuflLq', start_index=6307)
Annotation(end_index=6325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVU9M4cLN6c0mnMwYZxTP-c0wBaPGWebIVh1x9oh5M53o6--qCZSgFkynX1rt3WjDp3ekS4M2Y8J7FEZJ6SgVS1NuoZJfr3EKUeMAWyTmUGP-lDnwjKQ==', start_index=6307)
Annotation(end_index=6766, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4MHt29drlYJaFrR5vfB5c9DTYIG-HrU85TOJ2qO0wvpW1ABiGSUN6IcNadRs0yJe0_lEJAcywoCOQtyoeHYhFZaai_IRVcl40UkYGdDtcUbxlrDCGdxd4NGI7LAUrpvnkIgGxED3qwRhesVUEUZZRal3dJ7O5iUyhpGa_6pFbA5taKouxFTdcPOqNZMKV_jJdTSx4QmtMQCS8959nQT-M', start_index=6748)
Annotation(end_index=6766, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJRz7N79ZjsEJZBbcOtPulgLS-mzX4Ve0n290pmrjTjb-GXyO_N8-rtDAx8SGcWxif2ixa8qQaWYH8UarwWislYrnBDPmuhKGv687Xd6ydLCmhR9b8fA==', start_index=6748)
Annotation(end_index=6766, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWk_UciGUA92ZujZPT2svl94pxa5Yl2PbxIEcdG9BwC7tmXmdELavmr_rJfEMsoWbAOi8g5Gi6GrZTztXrO8b3k4bMM9TIZzSUMZuAEl9FdVCycpGrwhzGhqiXRLKlSuO7q-bFDqUmYw==', start_index=6748)
Annotation(end_index=6766, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDqzx9LhOTts99v5ccHmrKH4BZG-wWpGIxpzR65HgSJG3bcapII0MlC3uzBK8OgD2WQPiAUQD55QmYjeBfrHGcc59mlsrciDoJbRZaAx_nqNar_17q7ux3Awbf9KhbExVITuYRMrjr4cjptkC0', start_index=6748)
Annotation(end_index=7377, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWk_UciGUA92ZujZPT2svl94pxa5Yl2PbxIEcdG9BwC7tmXmdELavmr_rJfEMsoWbAOi8g5Gi6GrZTztXrO8b3k4bMM9TIZzSUMZuAEl9FdVCycpGrwhzGhqiXRLKlSuO7q-bFDqUmYw==', start_index=7365)
Annotation(end_index=7377, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDqzx9LhOTts99v5ccHmrKH4BZG-wWpGIxpzR65HgSJG3bcapII0MlC3uzBK8OgD2WQPiAUQD55QmYjeBfrHGcc59mlsrciDoJbRZaAx_nqNar_17q7ux3Awbf9KhbExVITuYRMrjr4cjptkC0', start_index=7365)
Annotation(end_index=8016, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9WZXgxrhB0q7KU4dSqcIzR3xrB8m8fQp_darRgD7xrLJ1mQ47er8aKCtO52UCSb5QbX0fswbo3W_5PEw9seQI7PS8l1nhMRgjo6xc1QsLMrCi7DdKDg==', start_index=8007)
Annotation(end_index=8263, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcgQWcCTwEOJJ8YEioE5w8BW0XkO-N4_ksJrZQv7wO0lVyb_cPUAcEYORo7FCHwTpskiKrLPVUBXE6pMcCWQHfww62bSL1cM9IvGelBezN2hiK68bDTT1qoK3KRtKs0wF5NtMOiXBXcyPL', start_index=8254)
Annotation(end_index=8497, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVU9M4cLN6c0mnMwYZxTP-c0wBaPGWebIVh1x9oh5M53o6--qCZSgFkynX1rt3WjDp3ekS4M2Y8J7FEZJ6SgVS1NuoZJfr3EKUeMAWyTmUGP-lDnwjKQ==', start_index=8488)
Annotation(end_index=9003, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgeVeTVHo2RiW1WMv3IY75fbAWnT0G9OJ99KGlafmHd6pr2aJyeCR4U3RW7eOsi_FAggZN3F92tHM08WtBhOOXrakTD3px8fkHNXCTeaRH34N0yI7nzlz-UyPEpQowy0yTuFGnr6iV9uLFL7E=', start_index=8994)
Annotation(end_index=9995, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgeVeTVHo2RiW1WMv3IY75fbAWnT0G9OJ99KGlafmHd6pr2aJyeCR4U3RW7eOsi_FAggZN3F92tHM08WtBhOOXrakTD3px8fkHNXCTeaRH34N0yI7nzlz-UyPEpQowy0yTuFGnr6iV9uLFL7E=', start_index=9986)
Annotation(end_index=10578, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHSx2F7VfiMQq3pMTiLwr3W4w3BQ94VgKV6FKOn0dQEVU_7SseyyrC_SAGLfjRqqkrf-1r9MvoY5wRlTriEBUp4hpR5_fzeY5zVLHvBy4suWEZKe85Uli6JDAojKANttqRcoHE0t3_SnxIAxuBFZegZ3y37m5CwMj2OJ1bcSfHVGFVVe47urRppQqqTXGarg==', start_index=10568)
Annotation(end_index=11580, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmyqI_Wak6IPpgPI5-W8xuAHF_4n87dJJydT_zOcR_arycalMUEcLD05OzFLpFzmhIV7wh0OMZCLs5qtWbMUAD_hPZbiBfw-WlfGUpPMm4K_sf0vcYvLgM6kAaiF2ft233Oy0ZpjRK5Q==', start_index=11570)
Annotation(end_index=11981, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmyqI_Wak6IPpgPI5-W8xuAHF_4n87dJJydT_zOcR_arycalMUEcLD05OzFLpFzmhIV7wh0OMZCLs5qtWbMUAD_hPZbiBfw-WlfGUpPMm4K_sf0vcYvLgM6kAaiF2ft233Oy0ZpjRK5Q==', start_index=11971)
Annotation(end_index=12079, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFp6TtLpLemmVRJAim5IFABDHLkiEua4OoGDqgWt3JFqyUNrKBHxMPdMehLg2CE_fQWRXPNkE4ZpEGxolRwM7ejHddHwfxqXSfPq6SiE-kem0zzXky_9-KJ1QYlwbw4dnCAmMQOuLtTb-Ke_w==', start_index=12069)
Annotation(end_index=12633, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcgQWcCTwEOJJ8YEioE5w8BW0XkO-N4_ksJrZQv7wO0lVyb_cPUAcEYORo7FCHwTpskiKrLPVUBXE6pMcCWQHfww62bSL1cM9IvGelBezN2hiK68bDTT1qoK3KRtKs0wF5NtMOiXBXcyPL', start_index=12624)
Annotation(end_index=13301, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9WZXgxrhB0q7KU4dSqcIzR3xrB8m8fQp_darRgD7xrLJ1mQ47er8aKCtO52UCSb5QbX0fswbo3W_5PEw9seQI7PS8l1nhMRgjo6xc1QsLMrCi7DdKDg==', start_index=13292)
Annotation(end_index=13927, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkN4WGycAHroTYlKABPniTJxjUu7yUMW46X5xRFrNp9acPVkG_5ZXER16Q_dkE0YEb8ahyZiWp9uKK4tjA494K85dku2SPPJJaDTFfpWztRVdQgsTgfAAfwGixTobpe3gCjuE=', start_index=13917)
Annotation(end_index=14724, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJRz7N79ZjsEJZBbcOtPulgLS-mzX4Ve0n290pmrjTjb-GXyO_N8-rtDAx8SGcWxif2ixa8qQaWYH8UarwWislYrnBDPmuhKGv687Xd6ydLCmhR9b8fA==', start_index=14712)
Annotation(end_index=14724, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWk_UciGUA92ZujZPT2svl94pxa5Yl2PbxIEcdG9BwC7tmXmdELavmr_rJfEMsoWbAOi8g5Gi6GrZTztXrO8b3k4bMM9TIZzSUMZuAEl9FdVCycpGrwhzGhqiXRLKlSuO7q-bFDqUmYw==', start_index=14712)
Annotation(end_index=15435, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWk_UciGUA92ZujZPT2svl94pxa5Yl2PbxIEcdG9BwC7tmXmdELavmr_rJfEMsoWbAOi8g5Gi6GrZTztXrO8b3k4bMM9TIZzSUMZuAEl9FdVCycpGrwhzGhqiXRLKlSuO7q-bFDqUmYw==', start_index=15426)
Annotation(end_index=15627, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWk_UciGUA92ZujZPT2svl94pxa5Yl2PbxIEcdG9BwC7tmXmdELavmr_rJfEMsoWbAOi8g5Gi6GrZTztXrO8b3k4bMM9TIZzSUMZuAEl9FdVCycpGrwhzGhqiXRLKlSuO7q-bFDqUmYw==', start_index=15618)
Annotation(end_index=15952, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIiiC0gniSdrR4YLcl_MtGtREvLRrbKmUQNJwKShN6nlF5MrIyhypfS2bcZgw3Sx62zzGSZwY2ctbl1r7Cg0P3V2kD9tay-2UdLN9RQHe9KnuxFcu34QWuK6PsnNp9U_WuZ41pQAoWc3t_3CS_OrViRckxX9SWHHbzFRsLxsvuVNaKpAoJ5UwyQH1Q2nAWdYzZ91J4kATw5vHEg9xOu2Wb7MTZya-K', start_index=15939)
Annotation(end_index=15952, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVU9M4cLN6c0mnMwYZxTP-c0wBaPGWebIVh1x9oh5M53o6--qCZSgFkynX1rt3WjDp3ekS4M2Y8J7FEZJ6SgVS1NuoZJfr3EKUeMAWyTmUGP-lDnwjKQ==', start_index=15939)
Annotation(end_index=16092, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgeVeTVHo2RiW1WMv3IY75fbAWnT0G9OJ99KGlafmHd6pr2aJyeCR4U3RW7eOsi_FAggZN3F92tHM08WtBhOOXrakTD3px8fkHNXCTeaRH34N0yI7nzlz-UyPEpQowy0yTuFGnr6iV9uLFL7E=', start_index=16083)
Annotation(end_index=16875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWk_UciGUA92ZujZPT2svl94pxa5Yl2PbxIEcdG9BwC7tmXmdELavmr_rJfEMsoWbAOi8g5Gi6GrZTztXrO8b3k4bMM9TIZzSUMZuAEl9FdVCycpGrwhzGhqiXRLKlSuO7q-bFDqUmYw==', start_index=16863)
Annotation(end_index=16875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDqzx9LhOTts99v5ccHmrKH4BZG-wWpGIxpzR65HgSJG3bcapII0MlC3uzBK8OgD2WQPiAUQD55QmYjeBfrHGcc59mlsrciDoJbRZaAx_nqNar_17q7ux3Awbf9KhbExVITuYRMrjr4cjptkC0', start_index=16863)
Annotation(end_index=17504, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHSx2F7VfiMQq3pMTiLwr3W4w3BQ94VgKV6FKOn0dQEVU_7SseyyrC_SAGLfjRqqkrf-1r9MvoY5wRlTriEBUp4hpR5_fzeY5zVLHvBy4suWEZKe85Uli6JDAojKANttqRcoHE0t3_SnxIAxuBFZegZ3y37m5CwMj2OJ1bcSfHVGFVVe47urRppQqqTXGarg==', start_index=17494)
Annotation(end_index=19884, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgeVeTVHo2RiW1WMv3IY75fbAWnT0G9OJ99KGlafmHd6pr2aJyeCR4U3RW7eOsi_FAggZN3F92tHM08WtBhOOXrakTD3px8fkHNXCTeaRH34N0yI7nzlz-UyPEpQowy0yTuFGnr6iV9uLFL7E=', start_index=19875)
Annotation(end_index=20131, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWk_UciGUA92ZujZPT2svl94pxa5Yl2PbxIEcdG9BwC7tmXmdELavmr_rJfEMsoWbAOi8g5Gi6GrZTztXrO8b3k4bMM9TIZzSUMZuAEl9FdVCycpGrwhzGhqiXRLKlSuO7q-bFDqUmYw==', start_index=20122)
Annotation(end_index=20764, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVU9M4cLN6c0mnMwYZxTP-c0wBaPGWebIVh1x9oh5M53o6--qCZSgFkynX1rt3WjDp3ekS4M2Y8J7FEZJ6SgVS1NuoZJfr3EKUeMAWyTmUGP-lDnwjKQ==', start_index=20755)
Annotation(end_index=21391, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmyqI_Wak6IPpgPI5-W8xuAHF_4n87dJJydT_zOcR_arycalMUEcLD05OzFLpFzmhIV7wh0OMZCLs5qtWbMUAD_hPZbiBfw-WlfGUpPMm4K_sf0vcYvLgM6kAaiF2ft233Oy0ZpjRK5Q==', start_index=21381)
Annotation(end_index=22029, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmyqI_Wak6IPpgPI5-W8xuAHF_4n87dJJydT_zOcR_arycalMUEcLD05OzFLpFzmhIV7wh0OMZCLs5qtWbMUAD_hPZbiBfw-WlfGUpPMm4K_sf0vcYvLgM6kAaiF2ft233Oy0ZpjRK5Q==', start_index=22019)
Annotation(end_index=22401, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH45XN1WbA3nRXsxBHbGgURNa0UUUmOkcmZeSXV0Lea_eDAkURypd5juq9kx-KCg2FtzQko2vDtSyycY9iQgzCS30IE8MPv8ElEuK3D4yU_Hd4YCJ-m1BhM2NgCBcWhAZxOxwTbdbHcCQ2fVQ_Mhe1r0FlWmDuxU8q21y7QMNQJdpBEG0P_aD3L9hmns-6Zor7IRW2SSdoeFGQPE3EIuQ==', start_index=22387)
Annotation(end_index=22401, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIBochxvYp7gIE_2HBZMl9Io6RixWvSPs-ocCpp_T0ROKWu_uBIWRYfEtjzFlpEA8itdlImiY9F8bx--h-6H0nrul-_Sl2sedpsrI7KCBvqSn0RBiLhfYtIBPmVg==', start_index=22387)
Annotation(end_index=22646, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECA6oFRuWdEwZrEfeFsJaBcjDS_A3eBGtmbYX_uifLSTLwEu_Ue7q-qqEQmYeZAPaE4IX-i4UsEfKRAUc6RHI9JzqTojN95asgt2q40vRcztjHk3SGe-s7fRI6LH-UvQebmlROUp0jD4ohn9RFdVODbtxTzicIU3IFR3fi3qoQBdX401fGRB7M-_jeDRfo9eUJnz7uq2Z6lqQMSbAub7oFprYzld3s8gjDFxwoudQPcTezZP-zdMfilWlum8Watgs=', start_index=22632)
Annotation(end_index=22646, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMObtdKXlAI4fhRMn7WIkN7h_vreMJV_W6ijgwOG7IPdFCA1qT0fUDp3JQjVs1Zu15JYboAwcMPeonGpwDIQ0rEPHO6LPDaO9eBGWjDI00qgOn_VvjduE36xmsTg4=', start_index=22632)
Annotation(end_index=22901, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLEPda_8Y8Asnkg5a7dy2iJLulNU_XywRwC1bUNDHx-8j7P1TAxSUKNKxq_ETfj8_SelDeiyvojH9Dsdo6eomq2qtcXaBZU1f6Or_QAxBbCL2Kq9BYJW3dPsky7v1gGBo=', start_index=22891)
Annotation(end_index=23109, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcgQWcCTwEOJJ8YEioE5w8BW0XkO-N4_ksJrZQv7wO0lVyb_cPUAcEYORo7FCHwTpskiKrLPVUBXE6pMcCWQHfww62bSL1cM9IvGelBezN2hiK68bDTT1qoK3KRtKs0wF5NtMOiXBXcyPL', start_index=23100)
Annotation(end_index=23256, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9WZXgxrhB0q7KU4dSqcIzR3xrB8m8fQp_darRgD7xrLJ1mQ47er8aKCtO52UCSb5QbX0fswbo3W_5PEw9seQI7PS8l1nhMRgjo6xc1QsLMrCi7DdKDg==', start_index=23247)
Annotation(end_index=23478, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWk_UciGUA92ZujZPT2svl94pxa5Yl2PbxIEcdG9BwC7tmXmdELavmr_rJfEMsoWbAOi8g5Gi6GrZTztXrO8b3k4bMM9TIZzSUMZuAEl9FdVCycpGrwhzGhqiXRLKlSuO7q-bFDqUmYw==', start_index=23469)
Annotation(end_index=23637, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgeVeTVHo2RiW1WMv3IY75fbAWnT0G9OJ99KGlafmHd6pr2aJyeCR4U3RW7eOsi_FAggZN3F92tHM08WtBhOOXrakTD3px8fkHNXCTeaRH34N0yI7nzlz-UyPEpQowy0yTuFGnr6iV9uLFL7E=', start_index=23628)
Annotation(end_index=23821, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFp6TtLpLemmVRJAim5IFABDHLkiEua4OoGDqgWt3JFqyUNrKBHxMPdMehLg2CE_fQWRXPNkE4ZpEGxolRwM7ejHddHwfxqXSfPq6SiE-kem0zzXky_9-KJ1QYlwbw4dnCAmMQOuLtTb-Ke_w==', start_index=23811)
Annotation(end_index=23959, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHSx2F7VfiMQq3pMTiLwr3W4w3BQ94VgKV6FKOn0dQEVU_7SseyyrC_SAGLfjRqqkrf-1r9MvoY5wRlTriEBUp4hpR5_fzeY5zVLHvBy4suWEZKe85Uli6JDAojKANttqRcoHE0t3_SnxIAxuBFZegZ3y37m5CwMj2OJ1bcSfHVGFVVe47urRppQqqTXGarg==', start_index=23949)
Annotation(end_index=24925, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcgQWcCTwEOJJ8YEioE5w8BW0XkO-N4_ksJrZQv7wO0lVyb_cPUAcEYORo7FCHwTpskiKrLPVUBXE6pMcCWQHfww62bSL1cM9IvGelBezN2hiK68bDTT1qoK3KRtKs0wF5NtMOiXBXcyPL', start_index=24916)
Annotation(end_index=25053, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9WZXgxrhB0q7KU4dSqcIzR3xrB8m8fQp_darRgD7xrLJ1mQ47er8aKCtO52UCSb5QbX0fswbo3W_5PEw9seQI7PS8l1nhMRgjo6xc1QsLMrCi7DdKDg==', start_index=25044)
Annotation(end_index=25163, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvMYUvgMsvISgzs880pw_w3PKwGok6P7ULNhW-IUP1Lf2UH2YMHebuO6iDIWfKqeMA26MNrRYznZTJgjb-aqATpsTswMxr8ispMKceAiAcdGXlTBL3Q2nR8kL7ZUFhTw==', start_index=25153)
Annotation(end_index=25226, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFp6TtLpLemmVRJAim5IFABDHLkiEua4OoGDqgWt3JFqyUNrKBHxMPdMehLg2CE_fQWRXPNkE4ZpEGxolRwM7ejHddHwfxqXSfPq6SiE-kem0zzXky_9-KJ1QYlwbw4dnCAmMQOuLtTb-Ke_w==', start_index=25216)
Annotation(end_index=25286, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgeVeTVHo2RiW1WMv3IY75fbAWnT0G9OJ99KGlafmHd6pr2aJyeCR4U3RW7eOsi_FAggZN3F92tHM08WtBhOOXrakTD3px8fkHNXCTeaRH34N0yI7nzlz-UyPEpQowy0yTuFGnr6iV9uLFL7E=', start_index=25277)
Annotation(end_index=25453, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHSx2F7VfiMQq3pMTiLwr3W4w3BQ94VgKV6FKOn0dQEVU_7SseyyrC_SAGLfjRqqkrf-1r9MvoY5wRlTriEBUp4hpR5_fzeY5zVLHvBy4suWEZKe85Uli6JDAojKANttqRcoHE0t3_SnxIAxuBFZegZ3y37m5CwMj2OJ1bcSfHVGFVVe47urRppQqqTXGarg==', start_index=25443)
Annotation(end_index=25582, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJRz7N79ZjsEJZBbcOtPulgLS-mzX4Ve0n290pmrjTjb-GXyO_N8-rtDAx8SGcWxif2ixa8qQaWYH8UarwWislYrnBDPmuhKGv687Xd6ydLCmhR9b8fA==', start_index=25573)
Annotation(end_index=25650, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLEPda_8Y8Asnkg5a7dy2iJLulNU_XywRwC1bUNDHx-8j7P1TAxSUKNKxq_ETfj8_SelDeiyvojH9Dsdo6eomq2qtcXaBZU1f6Or_QAxBbCL2Kq9BYJW3dPsky7v1gGBo=', start_index=25640)
Annotation(end_index=25729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECA6oFRuWdEwZrEfeFsJaBcjDS_A3eBGtmbYX_uifLSTLwEu_Ue7q-qqEQmYeZAPaE4IX-i4UsEfKRAUc6RHI9JzqTojN95asgt2q40vRcztjHk3SGe-s7fRI6LH-UvQebmlROUp0jD4ohn9RFdVODbtxTzicIU3IFR3fi3qoQBdX401fGRB7M-_jeDRfo9eUJnz7uq2Z6lqQMSbAub7oFprYzld3s8gjDFxwoudQPcTezZP-zdMfilWlum8Watgs=', start_index=25719)
Annotation(end_index=25812, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgeVeTVHo2RiW1WMv3IY75fbAWnT0G9OJ99KGlafmHd6pr2aJyeCR4U3RW7eOsi_FAggZN3F92tHM08WtBhOOXrakTD3px8fkHNXCTeaRH34N0yI7nzlz-UyPEpQowy0yTuFGnr6iV9uLFL7E=', start_index=25803)
Annotation(end_index=25911, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmyqI_Wak6IPpgPI5-W8xuAHF_4n87dJJydT_zOcR_arycalMUEcLD05OzFLpFzmhIV7wh0OMZCLs5qtWbMUAD_hPZbiBfw-WlfGUpPMm4K_sf0vcYvLgM6kAaiF2ft233Oy0ZpjRK5Q==', start_index=25901)
Annotation(end_index=25974, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDqzx9LhOTts99v5ccHmrKH4BZG-wWpGIxpzR65HgSJG3bcapII0MlC3uzBK8OgD2WQPiAUQD55QmYjeBfrHGcc59mlsrciDoJbRZaAx_nqNar_17q7ux3Awbf9KhbExVITuYRMrjr4cjptkC0', start_index=25965)
Annotation(end_index=26086, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcgQWcCTwEOJJ8YEioE5w8BW0XkO-N4_ksJrZQv7wO0lVyb_cPUAcEYORo7FCHwTpskiKrLPVUBXE6pMcCWQHfww62bSL1cM9IvGelBezN2hiK68bDTT1qoK3KRtKs0wF5NtMOiXBXcyPL', start_index=26077)
Annotation(end_index=26165, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWk_UciGUA92ZujZPT2svl94pxa5Yl2PbxIEcdG9BwC7tmXmdELavmr_rJfEMsoWbAOi8g5Gi6GrZTztXrO8b3k4bMM9TIZzSUMZuAEl9FdVCycpGrwhzGhqiXRLKlSuO7q-bFDqUmYw==', start_index=26156)
Annotation(end_index=26238, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgeVeTVHo2RiW1WMv3IY75fbAWnT0G9OJ99KGlafmHd6pr2aJyeCR4U3RW7eOsi_FAggZN3F92tHM08WtBhOOXrakTD3px8fkHNXCTeaRH34N0yI7nzlz-UyPEpQowy0yTuFGnr6iV9uLFL7E=', start_index=26229)
Annotation(end_index=26307, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHSx2F7VfiMQq3pMTiLwr3W4w3BQ94VgKV6FKOn0dQEVU_7SseyyrC_SAGLfjRqqkrf-1r9MvoY5wRlTriEBUp4hpR5_fzeY5zVLHvBy4suWEZKe85Uli6JDAojKANttqRcoHE0t3_SnxIAxuBFZegZ3y37m5CwMj2OJ1bcSfHVGFVVe47urRppQqqTXGarg==', start_index=26297)
Annotation(end_index=26401, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVU9M4cLN6c0mnMwYZxTP-c0wBaPGWebIVh1x9oh5M53o6--qCZSgFkynX1rt3WjDp3ekS4M2Y8J7FEZJ6SgVS1NuoZJfr3EKUeMAWyTmUGP-lDnwjKQ==', start_index=26392)
Annotation(end_index=26474, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIiiC0gniSdrR4YLcl_MtGtREvLRrbKmUQNJwKShN6nlF5MrIyhypfS2bcZgw3Sx62zzGSZwY2ctbl1r7Cg0P3V2kD9tay-2UdLN9RQHe9KnuxFcu34QWuK6PsnNp9U_WuZ41pQAoWc3t_3CS_OrViRckxX9SWHHbzFRsLxsvuVNaKpAoJ5UwyQH1Q2nAWdYzZ91J4kATw5vHEg9xOu2Wb7MTZya-K', start_index=26464)

## Sources
