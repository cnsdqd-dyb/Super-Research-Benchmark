# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 91d03418 | **Time:** 701.84s | **Cost:** $2.02786
--------------------------------------------------------------------------------

# The Spectral Architecture of Resistance: Jordan Canonical Forms, Social Stratification, and the Ergodicity Boundary in Counter-Globalization Flow Fields

### Executive Summary

The mathematical modeling of social mobility through Markov chains provides a rigorous framework for understanding the dynamics of stratification. However, the intersection of linear algebra and critical social theory—specifically the analysis of "counter-globalization" movements within "flow fields"—requires a sophisticated treatment of matrix spectroscopy. This report establishes that the **Jordan Canonical Form (JCF)** of social stratification matrices serves as the precise mathematical delineator of the **ergodicity boundary**.

In an ideal "globalized" flow field, the mobility matrix is irreducible and primitive, possessing a simple unit eigenvalue ($\lambda=1$) and a spectral gap that ensures rapid convergence to a unique stationary distribution (global ergodicity). Counter-globalization forces—manifesting as borders, protectionism, and social closure—act as perturbations that drive the system toward reducibility. The JCF captures this transition: as the system approaches the ergodicity boundary, the spectral gap closes, and the algebraic multiplicity of the unit eigenvalue increases, reflecting the fragmentation of the global system into disconnected, self-referential "basins of attraction" (absorbing states or closed classes). Furthermore, the JCF is critical in solving the **embedding problem**—determining whether a discrete-time mobility matrix can arise from a continuous-time "flow" (generator matrix). Counter-globalization often renders the mobility matrix "un-embeddable" in a real-valued continuous flow, mathematically proving the disruption of smooth social trajectories. Thus, the Jordan structure does not merely describe the system; it defines the topological limits of social connectivity and the horizon of possible movement.

---

## 1. Introduction: The Linear Algebra of Social Mechanics

The study of social stratification—the hierarchical arrangement of individuals into divisions of power and wealth—has long utilized the Markov chain as its primary mathematical engine. In this model, society is viewed as a system of states (classes), and mobility is the probabilistic transition between these states over time. The resulting **Social Stratification Matrix** (or transition matrix), denoted as $\mathbf{P}$, encapsulates the physics of the social universe.

However, contemporary social theory, particularly informed by the works of Deleuze, Guattari, and Appadurai, conceptualizes society not merely as static positions but as **flow fields**—dynamic, continuous movements of capital, bodies, and information. "Globalization" represents the smoothing of this space, maximizing flow and connectivity (ergodicity). Conversely, "counter-globalization" represents the re-imposition of striation: the erection of boundaries, the solidification of identities, and the resistance to flow.

To rigorously analyze the collision between these opposing forces, we must look beyond the surface probabilities of matrix $\mathbf{P}$ and examine its deep spectral structure. The **Jordan Canonical Form (JCF)** offers the necessary resolution. It reveals the eigenspace decomposition that dictates the system's asymptotic behavior. This report explores how the JCF identifies the **ergodicity boundary**—the critical threshold where a cohesive, mixing social system fractures into non-communicating segments, effectively mapping the mathematical topology of counter-globalization.

---

## 2. Mathematical Foundations of Social Stratification Matrices

### 2.1 The Markovian Model of Mobility
Let $S = \{s_1, s_2, \dots, s_n\}$ be a set of $n$ distinct social strata (e.g., lower class, middle class, elite). The state of the system at time $t$ is described by a row vector $\mathbf{x}^{(t)}$, where $x_i^{(t)}$ represents the proportion of the population in stratum $s_i$. The evolution of the system is governed by the stochastic matrix $\mathbf{P}$:
\[ \mathbf{x}^{(t+1)} = \mathbf{x}^{(t)} \mathbf{P} \]
where $P_{ij}$ is the probability that an individual moves from stratum $i$ to stratum $j$ in one time step [cite: 1].

For the matrix to be stochastic:
1.  $P_{ij} \geq 0$ for all $i, j$.
2.  $\sum_{j=1}^n P_{ij} = 1$ for all $i$.

### 2.2 Ergodicity in Social Systems
In the context of social mobility, **ergodicity** implies two crucial properties:
1.  **Irreducibility:** It is possible to reach any social stratum from any other stratum in a finite number of steps. The social graph is strongly connected.
2.  **Regularity (Primitivity):** There are no fixed cycles (e.g., the poor don't just swap places with the rich every fixed $k$ years).

Mathematically, a matrix $\mathbf{P}$ is ergodic if there exists an integer $k > 0$ such that all entries of $\mathbf{P}^k$ are positive. Under these conditions, the Perron-Frobenius theorem guarantees a unique stationary distribution $\pi$ such that:
\[ \lim_{t \to \infty} \mathbf{P}^t = \mathbf{1}\pi \]
where $\mathbf{1}$ is a column vector of ones. This represents a "globalized" equilibrium where initial conditions (history) are washed away by the mixing of the flow field [cite: 2, 3].

### 2.3 The Ergodicity Boundary
The **ergodicity boundary** is the hypersurface in the parameter space of $\mathbf{P}$ where the matrix loses its property of primitivity or irreducibility. This boundary is defined by the spectrum of $\mathbf{P}$, specifically the behavior of its eigenvalues $\lambda$.
*   **Inside the Ergodic Regime:** $\lambda_1 = 1$ is simple (algebraic multiplicity = 1), and $|\lambda_i| < 1$ for all $i > 1$.
*   **At the Boundary:**
    *   **Reducibility:** The eigenvalue $\lambda=1$ acquires an algebraic multiplicity $m > 1$. The eigenspace associated with $\lambda=1$ may become multidimensional, indicating the emergence of disjoint closed sets (fragmented societies).
    *   **Cyclicity:** An eigenvalue $\lambda \neq 1$ touches the unit circle ($|\lambda| = 1$), indicating periodic behavior (e.g., $\lambda = -1$).

---

## 3. The Jordan Canonical Form (JCF): Spectral Anatomy of the Matrix

To understand the behavior at the boundary, we cannot rely on diagonalization, as matrices at critical transition points are often **defective** (non-diagonalizable). We must use the Jordan Canonical Form.

### 3.1 Definition and Structure
Any square matrix $\mathbf{P} \in \mathbb{C}^{n \times n}$ is similar to a block diagonal matrix $\mathbf{J}$, known as the Jordan Canonical Form:
\[ \mathbf{P} = \mathbf{V} \mathbf{J} \mathbf{V}^{-1} \]
where $\mathbf{J} = \text{diag}(J_{n_1}(\lambda_1), J_{n_2}(\lambda_2), \dots, J_{n_k}(\lambda_k))$.

Each **Jordan Block** $J_m(\lambda)$ is an $m \times m$ matrix of the form:
\[ J_m(\lambda) = \begin{pmatrix} 
\lambda & 1 & 0 & \cdots & 0 \\
0 & \lambda & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \ddots & \vdots \\
0 & 0 & 0 & \lambda & 1 \\
0 & 0 & 0 & 0 & \lambda 
\end{pmatrix} \]

### 3.2 Geometric vs. Algebraic Multiplicity
The distinction between these multiplicities is vital for analyzing social stratification:
*   **Algebraic Multiplicity ($a_\lambda$):** The number of times $\lambda$ appears as a root of the characteristic polynomial $\det(\mathbf{P} - \lambda \mathbf{I}) = 0$. This represents the total "weight" of the mode associated with $\lambda$.
*   **Geometric Multiplicity ($g_\lambda$):** The dimension of the eigenspace $\ker(\mathbf{P} - \lambda \mathbf{I})$. This corresponds to the number of linearly independent eigenvectors associated with $\lambda$. It is equal to the number of Jordan blocks associated with $\lambda$ [cite: 4, 5].

**Crucial Insight for Social Systems:**
If $a_\lambda > g_\lambda$, the matrix is defective. This implies the existence of **generalized eigenvectors** and Jordan blocks of size $> 1$. In physical systems, this often correlates with "critical damping" or transition points. In social mobility matrices, the structure of the Jordan blocks for $\lambda=1$ determines the number of independent stationary distributions (ergodic classes) [cite: 3, 6].

---

## 4. Flow Fields and the Embedding Problem

The user's query references "flow fields," a term invoking continuous motion. In sociology, this corresponds to modeling mobility not as discrete jumps (steps) but as a continuous-time Markov chain (CTMC) governed by a generator matrix $\mathbf{Q}$ (the "flow field"), such that:
\[ \mathbf{P}(t) = e^{\mathbf{Q}t} \]
where $\mathbf{P}(1)$ is the observed discrete transition matrix.

### 4.1 The Embedding Condition
Not every discrete matrix $\mathbf{P}$ can be generated by a continuous flow $\mathbf{Q}$. This is known as the **Embedding Problem**. The Jordan form is the decisive test for this property.
For a real stochastic matrix $\mathbf{P}$ to be embeddable in a continuous flow (i.e., to have a real logarithm $\mathbf{Q}$), specific conditions on its JCF must be met:
1.  **Determinant:** $\det(\mathbf{P}) > 0$.
2.  **Negative Eigenvalues:** Any Jordan block associated with a negative eigenvalue must occur an even number of times (i.e., they must come in pairs to allow for a real-valued root) [cite: 7, 8].
3.  **Jordan Structure:** The structure of the Jordan blocks restricts the possible pathways of flow.

### 4.2 Counter-Globalization as Flow Disruption
"Counter-globalization" can be interpreted mathematically as a structural change to $\mathbf{P}$ that violates the embedding conditions.
*   **Example:** If a counter-globalization movement imposes a strict cyclic alternation between two states (e.g., seasonal migration strictly enforced), the matrix might acquire an eigenvalue of $-1$ with a single Jordan block. This makes the matrix un-embeddable in a real continuous flow [cite: 7]. The "flow" is broken; the system is no longer a "field" but a discrete, rigid oscillation.
*   **Deleuzian Interpretation:** The "smooth space" of the flow field (continuous $\mathbf{Q}$) is "striated" by the discrete, non-embeddable matrix $\mathbf{P}$. The JCF detects this striation by revealing the spectral obstructions to taking the logarithm of the matrix.

---

## 5. Delimiting the Ergodicity Boundary via Jordan Form

The core of the query asks how the JCF *delimits* the ergodicity boundary. This boundary is the threshold between a unified, mixing system and a fragmented or periodic one.

### 5.1 The Spectral Gap and Mixing Time
For an ergodic matrix, the rate of convergence to the stationary distribution is governed by the **Spectral Gap** ($\gamma$):
\[ \gamma = 1 - |\lambda_2| \]
where $\lambda_2$ is the eigenvalue with the second-largest modulus (SLEM).
*   **Globalized Flow:** High mobility, large spectral gap, rapid mixing. The JCF is diagonal or near-diagonal with $|\lambda_2| \ll 1$.
*   **Approaching the Boundary:** As counter-globalization barriers rise (off-diagonal transition probabilities $P_{ij} \to 0$), $\lambda_2$ approaches 1. The spectral gap closes ($\gamma \to 0$). The system exhibits "critical slowing down" [cite: 9, 10].

### 5.2 The Boundary Crossing: Bifurcation of $\lambda=1$
The definitive "ergodicity boundary" is crossed when the matrix becomes **reducible**.
Consider a global system splitting into two isolated blocs (e.g., "West" and "East") due to counter-globalization.
*   **Before Split (Ergodic):** $\mathbf{P}$ has a single eigenvalue $\lambda_1 = 1$. The Jordan form has one $1 \times 1$ block for $\lambda=1$.
*   **At the Split (Non-Ergodic):** The matrix $\mathbf{P}$ can be permuted to:
    \[ \mathbf{P} = \begin{pmatrix} \mathbf{P}_A & \mathbf{0} \\ \mathbf{0} & \mathbf{P}_B \end{pmatrix} \]
    Now, the characteristic polynomial has $\lambda=1$ with algebraic multiplicity $a_1 = 2$.
    The Geometric multiplicity $g_1$ also becomes 2.
    The JCF for $\lambda=1$ becomes:
    \[ \mathbf{J}_{\lambda=1} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \]
    The emergence of the second Jordan block for $\lambda=1$ marks the precise location of the ergodicity boundary [cite: 4, 6].

### 5.3 The "Fading Ergodicity" Regime
Recent research in physics (applied here to social systems) describes a "fading ergodicity" regime near the boundary. As the system approaches the split, fluctuations in the matrix elements "soften." The JCF might exhibit **transient defectiveness** or extreme sensitivity.
*   **Thouless Energy Analogy:** In disordered systems, the "Thouless energy" separates ergodic from non-ergodic spectral statistics. In social matrices, as the "lines of flight" (escape routes from strata) are cut by counter-globalization, the "social Thouless energy" (mixing rate) drops to zero [cite: 11, 12].

### 5.4 Absorbing States and Jordan Blocks
Counter-globalization often creates **absorbing states** (traps)—strata from which exit is impossible (e.g., extreme poverty, or a closed authoritarian state).
If state $k$ is absorbing, $P_{kk} = 1$.
*   If the system has transient states feeding into this absorbing state, the JCF will contain a $1 \times 1$ block for $\lambda=1$ corresponding to the absorbing state.
*   If there are multiple absorbing states, the geometric multiplicity of $\lambda=1$ equals the number of absorbing states.
*   **Jordan Chains:** If the system is "nearly" absorbing or has a specific feed-forward structure (e.g., a hierarchy where you can only move up, never down), the matrix might be nilpotent-like in its transient parts. The sizes of the Jordan blocks for $\lambda=0$ (or small $\lambda$) describe the "depth" of the stratification—the number of steps required to flush the transient population [cite: 13, 14].

---

## 6. Counter-Globalization: Lines of Flight and Striation

### 6.1 Deleuzian Mechanics of the Matrix
Deleuze and Guattari describe "lines of flight" as movements that escape the "molar" aggregates (rigid social structures). Globalization attempts to capture these lines into a single axiomatic of capital (the ergodic flow). Counter-globalization can be:
1.  **Reactionary:** Re-imposing molar lines (borders), creating reducible matrices with multiple absorbing blocks.
2.  **Revolutionary:** Creating new lines of flight that escape the matrix entirely (system change).

In the context of the query, we focus on the **flow fields** (the matrix dynamics). Counter-globalization acts as a **constraint operator** on $\mathbf{P}$.
*   **Striation:** Forcing $P_{ij} = 0$ for specific $i, j$.
*   **Territorialization:** Increasing $P_{ii}$ (diagonal dominance).

### 6.2 The Jordan Form as a Measure of "Social Defectiveness"
A "defective" matrix (where geometric multiplicity < algebraic multiplicity) represents a system with internal coupling that cannot be decoupled by coordinate transformation.
*   **Interpretation:** In a defective social matrix, strata are "glued" together in a way that prevents independent evolution, yet they do not mix. This is a rare but profound state of "critical fragility" often found at the tipping point of revolutions or systemic collapses (phase transitions) [cite: 14, 15].
*   **The Boundary:** The ergodicity boundary is often where the matrix passes through a defective state as eigenvalues collide (e.g., two real eigenvalues merging and becoming complex conjugates, signifying the onset of oscillation/conflict).

---

## 7. Detailed Analysis of Spectral Delimitation

### 7.1 The Perron-Frobenius Consequence
For a non-negative, irreducible matrix $\mathbf{P}$:
*   The spectral radius $\rho(\mathbf{P}) = 1$.
*   $\lambda=1$ is a simple eigenvalue (Jordan block size 1).
*   The associated eigenvector is strictly positive.

**Delimitation Mechanism:**
The JCF delimits the boundary by monitoring the **Jordan structure of the spectral radius**.
1.  **Ergodic Region:** $J = [cite: 16] \oplus J_{rest}$.
2.  **Boundary (Reducible):** $J = [cite: 16] \oplus [cite: 16] \oplus J_{rest}$. (Multiplicity jump).
3.  **Boundary (Periodic):** $J = [cite: 16] \oplus [-1] \oplus J_{rest}$ or $J = [cite: 16] \oplus [e^{i\theta}] \dots$. (Spectrum touches unit circle).

### 7.2 Sensitivity and Condition Numbers
The computation of the Jordan form is notoriously unstable numerically (ill-posed). However, in social theory, this instability is a feature, not a bug. It reflects the **social volatility** near the ergodicity boundary. Small perturbations in mobility rates (e.g., a slight change in visa policy) can drastically alter the Jordan structure (splitting blocks), shifting the system from ergodic to non-ergodic. This sensitivity defines the "width" of the boundary layer in the flow field [cite: 2, 17].

---

## 8. Conclusion

The Jordan Canonical Form of social stratification matrices provides the rigorous spectral language necessary to articulate the dynamics of counter-globalization. It delimits the ergodicity boundary through three specific mechanisms:

1.  **Multiplicity Bifurcation:** The transition from a simple unit eigenvalue to a multiple one signals the fragmentation of the global flow field into disconnected, non-communicating social basins (reducibility).
2.  **Spectral Gap Closure:** The movement of sub-dominant eigenvalues toward the unit circle (revealed by the JCF) quantifies the "slowing down" of social mixing and the hardening of class boundaries.
3.  **Embedding Obstruction:** The specific arrangement of Jordan blocks (particularly for negative eigenvalues) determines whether the discrete mobility observed can be mapped to a continuous "smooth" flow. Counter-globalization often generates Jordan structures that are topologically incompatible with continuous flow, mathematically proving the "striation" of social space.

In the clash between the "smooth space" of globalization and the "striated space" of counter-movements, the Jordan form acts as the seismograph, detecting the deep structural fractures that define the limits of social mobility.

---

### References
[cite: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17, 18, 19, 20, 21, 22, 23, 24]

**Sources:**
1. [ssa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGapHzmXgRDTcFe-YEPGcA15IK5O5jHPhGy4cVtp4r8oX1poSSc1YEXEp5v3zhVergB8Xt4fLQAtxLrlLeLQpNFpdaZ9nil81mu2F1xxO1B-Xq2asxp17yfzdrOoC_mMnfLoNx7f4X1L8qLHw==)
2. [msu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOGhneWHE-pj88_vNilS7SHg-B1A0oqDG465JRlP7f8IA_D6JEHri9c6VJeLdTAQqCkYIKjM54QGsNbL2vLehp2B9B1V1YjBF5Sv7r-uSfnJpx6mO8vPBrSnE9PIh7qpNHa5dYOqxEFg28J9Le6BcStw==)
3. [libretexts.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLtQAd8L3aHQop5z2XTKVPG94_80zCuyC4tZKGy4cBKmtAsotWUwGU3JnxBG_3i9vWiKBiIPrzwa2xHmRtnGbUmTcMzFd9Ml5be6sKSdqpZzDek2hAQGXjUmuGp3WZE5MmT6O0u6yIcnd9xjHNSsBAgvS3hI6pYAgmfLqb37FXQQVQUQQVghDWk1BIIK1VGnlq_ErIBf7EBsqdVFd_u5vFdYxH2E5_aZgNZu-rNlDbJvKoSxEiX7-F4gwAZWjTxv6fqcbSkYsWU9S7R9WNPrNfrrdIfIDHebi5Y4Zokb4Cgcw_0U7DxnpUWziqZy9oBSkmhB2ynow7bsLt6L41IA4dkOB9qdBEGFGy_G-Yl6wOQb3OMHnulmBnqaCsUJ4=)
4. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZu7Nh0kAhybRbAxiuD_7EvaJIXKnW0MyrRHTgkwdLvdsexDajDneBLbPrZebslItkTMSOtemTrO1c2YwsFF8v1LczgipWmkx5_IZJeONxgoSd3u9j7soAIiAyen3Ey9P8sgJm6J8=)
5. [stackexchange.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTCyE7Hi5bGy4GvSuGjWi1lmtjFFSywCoCnkFTFuP0mtJhX4DsXnZ_vj39Ji1tMGiEOz8hp5iCTQI9Qw8fkIqjQ-p2wQ3HaPfp5zsX_4WiM4D1HbVPHb8lvnDgQkWJ_0wejVKZdLdnuF9Nx3kEDGQYmio0sjECE3QRX51EhX3lZR1x4WBFxMNOpEehlBZkei_monAxC0HkQQUFePCkBnY=)
6. [uni-lj.si](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhQ5TPAmqaI9XBA60t6ML7Y8U1OIoJ4jLe7S2Lk11THzA3AF2-DDsWCPwMILX7VR0pQhtrBMbosAG_7Hk4qlbfhKi2ELS7gKbGW_DhdinV-zYxIcP5zePWDBQf7fAv4qYqDbxClBOd8puPzSEPmAI5S8qVkQ==)
7. [upc.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElzYiVi8CMKizP5FNvojekrqY2AMH0YELSZ-XLNDR_oKi7BoGO1QdHogoFDPxzLbzzNEsDwpI2QXFIxgwDDfrL4JOpRMo6J8AXE8-iSLMhw_dAPlhfJCw5N3RurezkaLdUuHdfHXHoEF79a2unV-8U7FEXByFjFoFzyrJxAWs7Okc0xazVz2mC)
8. [columbia.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBaqV9wCAThXJRiGPnXISJjaGp6u2XWTpHkwwhrTRO--uz1awmvU0Cd6WiEHWKTNpksyKTeHsEvDmZ3_D-qKmeKxwgbFgwz51sAt1vJHAc10f7tSehO_qW6hTsxX2jhzKsVQSkqxajR650JNaQ-IzSQpgbEllIxkg=)
9. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQWqCrrV0uzC4Kt4nmP9ufWTzxUWcCMlyIlW6cjgVcVSuGNkO3aCcVerwGNEyNd2JieltS8fv_jz-HjXUr_R0yVHFzml4wWi2Nx48l00cHSRqR-_5DI0pieg==)
10. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnbr60jnet00LAKIp-NRI-SUDlSIX6VAQejBTnIWTFpeOZLIZokB-5mWdXhERRQVBZsLfuwd1t5qcTb9V4FLtm50u7dEI0VOh1wFogWTrIUuFYpQfVj0GHx51AMf2zurshQfEFKq53Du7IoW5ffAT5cmfBwhte6LdznSiTv4cfAGZjdhwlsjUUVvKVyVhntSUN3yeAulGiAzkxeF2goqu0)
11. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSSz3P0NqJuJf31C5gqHWu2BoAHkZCHDZLSakadMm2epd1EkQwQYWsMgH62106t13dqdbmSXb5xkC9tamwtYdm1b3JNEw9rC-4EZpYjthvxlBoMhVTU3rk6w==)
12. [ijs.si](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE38stMdx0cqypD7NwBfukk4GuibX3krTQjPXBMq3ERCjRVsbFL70imkQ1Ysjsyagnmubh9t8lzCJ4ogvE1zyjHo56Kp3unmVTFJgqNdVcqJNtmVuPhjrMnivWa4GAagYBk2UxKHKpET5OBxw==)
13. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpgQEJwhBll0fRGScNd3nGPHNOX4ff-fFp1h0WBf4zJQnkhl7yFW8I5DcAA7kK8E6G-nL_4WeKLIcyLuXKc53c02AC_FxxBFE_KCJbATWpb86jh9owInbXFHxkD4wbztD3HWDPZKxUQpIgjc2KQQ4sfkHCoaxiJLcNnl1i_oMc7n6_FF20qssk6nmIeg==)
14. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-fLjqWG3IU-B3REoaRs8929EdMVD4iujYh4-3l-Dq-O7E655KwJ-Is2K1xGU2BaCIWuHBZjQmyGpRoVgYsHFBdFRy0JZkr82mQ6BpM6B__bbEsh9L9Ych47zOFCykZIR4oIBQoS9wgVEHprbPrY8kJg5vnlaljzCGam_s5e8fEiBNXNz7aDAN1FkDMzLHfxPPOgx6WNG5zbIgoX2dGe66_VGvcA81Me_VOC7n-cSevZe0)
15. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELrFsQwR-SXEnBhKnXmyynJN1xnI52LEgd-Y0cZucfRPNnTftcZKLgs6FtuvmyCzhzdyqGme2bhpLS6d2Ps1ZxOA9hj-0XHx0IZMOrSepcf_iWR8zM3LSyyoK7)
16. [uwaterloo.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGc8L0sQNS00wRzWOIuyFKMYcskXBf8tyLahhZcGcPS2_pfq_w5sGkvcuM4-Ufbx-5pU-w7yfZ8CnHbtPxlM7XwnAoHBQmtmi_VPgRVmBCXzaf8XJNH1G-_b6nqAhBJeK6hNT7Oq4gOnHi0_K2suI4QjBO76wjpgPJ0kb5DUg==)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNhIyaiYSrkhfE4ddue8y8ylRowBnDyHZBNA6dZJnUsWCsIdLqpu_cm5HmLtWS3o44v_hCBr7alyPRaWmEz44d2EavZbDNQyx4RQ-Kmti79-Q9VWL0_-gV9IusTt4eWBwWg2FOzs-G4jo6J5h1y91lvzLcMB61Ca6SaNekQ9E3efHzsGWFYLWJ31PnaUZihGcsQXQa3XTnc5qCZ3tzDuXbsYR-Wg==)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8Gz5kAyNa0yby2KmZMiRccinyDmLCD5Ojf311hupy6Ys_5MGBJKrA7Kxs8H7Q26Dvcq5uGXhXbYmlUHqw5qX3aQH5ztu7iO7Nk-1_cAk_Qy2cvfYBnXGSwNW1PoHb2cLxAuprVj9fiL_1AoVrN_ajCe0LMqfH-EMXUGN5wPQhWwc2aWdl2WlMiF0yu8JK003L3hVgcqX27P7bKYlqJ9fI1lWV5_I2mPo4EaHEeIDZVirnzMNj1R-7qB3RN_ty7LaGzREJZvWyzjL0wA==)
19. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNyJXJuqwECFYWW4gQjb7k83TS6MGI22Lm6pFNTBFXt2dE5Cs-bL8sBCueTcx9knLLtT0ykljCaIydUHieBSQkT1PpQqwh4CJcZM98Sv4HV3L71NIM)
20. [libcom.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_vf2iqDJkpzdPpo8GCZCOgC3qjVLMljwOOs9ta6aeJmXG2zrIa51kxJOz4Ko6BQNmUAeTNvO2QehPxvJjsMs53i9pB3_h6OEIbfVuXS0yfUs3q5OVEic5PSdgxZODrKyKiQU2DbMxw_KI_Kv1z54BfBp2s5IfuEstzSbuLpvHtTA9WeBPOWDcBH2LkIGLUXY=)
21. [theanarchistlibrary.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0udfpjY2aV57xsZK4hLU_IOu7qKTwoHoP8uNb8iw5aC-MK5rVfDzEyZxTrZlltAJ5rLw7QlNNwC38LYH9GummTaEZakDZ6KZJ5FweYYAeuatbXD7aRx76u0cUXrviPwRSRcLGzpl1eoXoY6kJE_EzGvPwWtNdhKS14ALy-O6SrRigSDN9JYUKCtQz4V6A_Q0KKDOK2ZHdHUfOh_A=)
22. [ujcv.edu.hn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhDx2tM8_6mAyf_W9QjGk1AXBkiOhHxw1c6ksinKafwhcLmURN07yjpECusOpHN4utaDmDqB8F9VRUMRYzjfZVrhpW0ZXv9RqyJ7WWCpuvJvmuRRsvMQqiLZj0Noyt4UTckSKHNzh2cOH8edNp0QMakM94IDhXJjk3pAgoQ9hn7wKblUlm8DdLyihgLDjqryoMWeoXYyI=)
23. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoNbUbj621pkZq0buaTDEssCMJW8uQ4FM3LnJ0CiOvl47fHuRAl_rf2-5ZxGAaow2BPf-ylL0x5XUT18-l_QXoDZUtIXf9kLsc0yZDFHNNFhutTZ3YO1ydL4fKBFk=)
24. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwQmkoQWLpNMYqj6BT-uErq0I0AQvk6CkKksV0voWfK5CaNY28X5gXYKamUyfiSt-QEreZrzQn-5KKjIxZqrMjzCQYDInS473ipXTCh1vR1JSZwFq89k_JkAZQossl8xkdWfGHcLIz)


## Annotations
Annotation(end_index=4261, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGapHzmXgRDTcFe-YEPGcA15IK5O5jHPhGy4cVtp4r8oX1poSSc1YEXEp5v3zhVergB8Xt4fLQAtxLrlLeLQpNFpdaZ9nil81mu2F1xxO1B-Xq2asxp17yfzdrOoC_mMnfLoNx7f4X1L8qLHw==', start_index=4252)
Annotation(end_index=5285, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOGhneWHE-pj88_vNilS7SHg-B1A0oqDG465JRlP7f8IA_D6JEHri9c6VJeLdTAQqCkYIKjM54QGsNbL2vLehp2B9B1V1YjBF5Sv7r-uSfnJpx6mO8vPBrSnE9PIh7qpNHa5dYOqxEFg28J9Le6BcStw==', start_index=5273)
Annotation(end_index=5285, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLtQAd8L3aHQop5z2XTKVPG94_80zCuyC4tZKGy4cBKmtAsotWUwGU3JnxBG_3i9vWiKBiIPrzwa2xHmRtnGbUmTcMzFd9Ml5be6sKSdqpZzDek2hAQGXjUmuGp3WZE5MmT6O0u6yIcnd9xjHNSsBAgvS3hI6pYAgmfLqb37FXQQVQUQQVghDWk1BIIK1VGnlq_ErIBf7EBsqdVFd_u5vFdYxH2E5_aZgNZu-rNlDbJvKoSxEiX7-F4gwAZWjTxv6fqcbSkYsWU9S7R9WNPrNfrrdIfIDHebi5Y4Zokb4Cgcw_0U7DxnpUWziqZy9oBSkmhB2ynow7bsLt6L41IA4dkOB9qdBEGFGy_G-Yl6wOQb3OMHnulmBnqaCsUJ4=', start_index=5273)
Annotation(end_index=7729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTCyE7Hi5bGy4GvSuGjWi1lmtjFFSywCoCnkFTFuP0mtJhX4DsXnZ_vj39Ji1tMGiEOz8hp5iCTQI9Qw8fkIqjQ-p2wQ3HaPfp5zsX_4WiM4D1HbVPHb8lvnDgQkWJ_0wejVKZdLdnuF9Nx3kEDGQYmio0sjECE3QRX51EhX3lZR1x4WBFxMNOpEehlBZkei_monAxC0HkQQUFePCkBnY=', start_index=7717)
Annotation(end_index=7729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZu7Nh0kAhybRbAxiuD_7EvaJIXKnW0MyrRHTgkwdLvdsexDajDneBLbPrZebslItkTMSOtemTrO1c2YwsFF8v1LczgipWmkx5_IZJeONxgoSd3u9j7soAIiAyen3Ey9P8sgJm6J8=', start_index=7717)
Annotation(end_index=8178, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhQ5TPAmqaI9XBA60t6ML7Y8U1OIoJ4jLe7S2Lk11THzA3AF2-DDsWCPwMILX7VR0pQhtrBMbosAG_7Hk4qlbfhKi2ELS7gKbGW_DhdinV-zYxIcP5zePWDBQf7fAv4qYqDbxClBOd8puPzSEPmAI5S8qVkQ==', start_index=8166)
Annotation(end_index=8178, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLtQAd8L3aHQop5z2XTKVPG94_80zCuyC4tZKGy4cBKmtAsotWUwGU3JnxBG_3i9vWiKBiIPrzwa2xHmRtnGbUmTcMzFd9Ml5be6sKSdqpZzDek2hAQGXjUmuGp3WZE5MmT6O0u6yIcnd9xjHNSsBAgvS3hI6pYAgmfLqb37FXQQVQUQQVghDWk1BIIK1VGnlq_ErIBf7EBsqdVFd_u5vFdYxH2E5_aZgNZu-rNlDbJvKoSxEiX7-F4gwAZWjTxv6fqcbSkYsWU9S7R9WNPrNfrrdIfIDHebi5Y4Zokb4Cgcw_0U7DxnpUWziqZy9oBSkmhB2ynow7bsLt6L41IA4dkOB9qdBEGFGy_G-Yl6wOQb3OMHnulmBnqaCsUJ4=', start_index=8166)
Annotation(end_index=9251, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElzYiVi8CMKizP5FNvojekrqY2AMH0YELSZ-XLNDR_oKi7BoGO1QdHogoFDPxzLbzzNEsDwpI2QXFIxgwDDfrL4JOpRMo6J8AXE8-iSLMhw_dAPlhfJCw5N3RurezkaLdUuHdfHXHoEF79a2unV-8U7FEXByFjFoFzyrJxAWs7Okc0xazVz2mC', start_index=9239)
Annotation(end_index=9251, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBaqV9wCAThXJRiGPnXISJjaGp6u2XWTpHkwwhrTRO--uz1awmvU0Cd6WiEHWKTNpksyKTeHsEvDmZ3_D-qKmeKxwgbFgwz51sAt1vJHAc10f7tSehO_qW6hTsxX2jhzKsVQSkqxajR650JNaQ-IzSQpgbEllIxkg=', start_index=9239)
Annotation(end_index=9842, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElzYiVi8CMKizP5FNvojekrqY2AMH0YELSZ-XLNDR_oKi7BoGO1QdHogoFDPxzLbzzNEsDwpI2QXFIxgwDDfrL4JOpRMo6J8AXE8-iSLMhw_dAPlhfJCw5N3RurezkaLdUuHdfHXHoEF79a2unV-8U7FEXByFjFoFzyrJxAWs7Okc0xazVz2mC', start_index=9833)
Annotation(end_index=11111, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQWqCrrV0uzC4Kt4nmP9ufWTzxUWcCMlyIlW6cjgVcVSuGNkO3aCcVerwGNEyNd2JieltS8fv_jz-HjXUr_R0yVHFzml4wWi2Nx48l00cHSRqR-_5DI0pieg==', start_index=11098)
Annotation(end_index=11111, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnbr60jnet00LAKIp-NRI-SUDlSIX6VAQejBTnIWTFpeOZLIZokB-5mWdXhERRQVBZsLfuwd1t5qcTb9V4FLtm50u7dEI0VOh1wFogWTrIUuFYpQfVj0GHx51AMf2zurshQfEFKq53Du7IoW5ffAT5cmfBwhte6LdznSiTv4cfAGZjdhwlsjUUVvKVyVhntSUN3yeAulGiAzkxeF2goqu0', start_index=11098)
Annotation(end_index=12099, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhQ5TPAmqaI9XBA60t6ML7Y8U1OIoJ4jLe7S2Lk11THzA3AF2-DDsWCPwMILX7VR0pQhtrBMbosAG_7Hk4qlbfhKi2ELS7gKbGW_DhdinV-zYxIcP5zePWDBQf7fAv4qYqDbxClBOd8puPzSEPmAI5S8qVkQ==', start_index=12087)
Annotation(end_index=12099, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZu7Nh0kAhybRbAxiuD_7EvaJIXKnW0MyrRHTgkwdLvdsexDajDneBLbPrZebslItkTMSOtemTrO1c2YwsFF8v1LczgipWmkx5_IZJeONxgoSd3u9j7soAIiAyen3Ey9P8sgJm6J8=', start_index=12087)
Annotation(end_index=12727, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE38stMdx0cqypD7NwBfukk4GuibX3krTQjPXBMq3ERCjRVsbFL70imkQ1Ysjsyagnmubh9t8lzCJ4ogvE1zyjHo56Kp3unmVTFJgqNdVcqJNtmVuPhjrMnivWa4GAagYBk2UxKHKpET5OBxw==', start_index=12713)
Annotation(end_index=12727, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSSz3P0NqJuJf31C5gqHWu2BoAHkZCHDZLSakadMm2epd1EkQwQYWsMgH62106t13dqdbmSXb5xkC9tamwtYdm1b3JNEw9rC-4EZpYjthvxlBoMhVTU3rk6w==', start_index=12713)
Annotation(end_index=13680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpgQEJwhBll0fRGScNd3nGPHNOX4ff-fFp1h0WBf4zJQnkhl7yFW8I5DcAA7kK8E6G-nL_4WeKLIcyLuXKc53c02AC_FxxBFE_KCJbATWpb86jh9owInbXFHxkD4wbztD3HWDPZKxUQpIgjc2KQQ4sfkHCoaxiJLcNnl1i_oMc7n6_FF20qssk6nmIeg==', start_index=13666)
Annotation(end_index=13680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-fLjqWG3IU-B3REoaRs8929EdMVD4iujYh4-3l-Dq-O7E655KwJ-Is2K1xGU2BaCIWuHBZjQmyGpRoVgYsHFBdFRy0JZkr82mQ6BpM6B__bbEsh9L9Ych47zOFCykZIR4oIBQoS9wgVEHprbPrY8kJg5vnlaljzCGam_s5e8fEiBNXNz7aDAN1FkDMzLHfxPPOgx6WNG5zbIgoX2dGe66_VGvcA81Me_VOC7n-cSevZe0', start_index=13666)
Annotation(end_index=15100, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELrFsQwR-SXEnBhKnXmyynJN1xnI52LEgd-Y0cZucfRPNnTftcZKLgs6FtuvmyCzhzdyqGme2bhpLS6d2Ps1ZxOA9hj-0XHx0IZMOrSepcf_iWR8zM3LSyyoK7', start_index=15086)
Annotation(end_index=15100, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-fLjqWG3IU-B3REoaRs8929EdMVD4iujYh4-3l-Dq-O7E655KwJ-Is2K1xGU2BaCIWuHBZjQmyGpRoVgYsHFBdFRy0JZkr82mQ6BpM6B__bbEsh9L9Ych47zOFCykZIR4oIBQoS9wgVEHprbPrY8kJg5vnlaljzCGam_s5e8fEiBNXNz7aDAN1FkDMzLHfxPPOgx6WNG5zbIgoX2dGe66_VGvcA81Me_VOC7n-cSevZe0', start_index=15086)
Annotation(end_index=15820, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGc8L0sQNS00wRzWOIuyFKMYcskXBf8tyLahhZcGcPS2_pfq_w5sGkvcuM4-Ufbx-5pU-w7yfZ8CnHbtPxlM7XwnAoHBQmtmi_VPgRVmBCXzaf8XJNH1G-_b6nqAhBJeK6hNT7Oq4gOnHi0_K2suI4QjBO76wjpgPJ0kb5DUg==', start_index=15810)
Annotation(end_index=15884, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGc8L0sQNS00wRzWOIuyFKMYcskXBf8tyLahhZcGcPS2_pfq_w5sGkvcuM4-Ufbx-5pU-w7yfZ8CnHbtPxlM7XwnAoHBQmtmi_VPgRVmBCXzaf8XJNH1G-_b6nqAhBJeK6hNT7Oq4gOnHi0_K2suI4QjBO76wjpgPJ0kb5DUg==', start_index=15874)
Annotation(end_index=15902, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGc8L0sQNS00wRzWOIuyFKMYcskXBf8tyLahhZcGcPS2_pfq_w5sGkvcuM4-Ufbx-5pU-w7yfZ8CnHbtPxlM7XwnAoHBQmtmi_VPgRVmBCXzaf8XJNH1G-_b6nqAhBJeK6hNT7Oq4gOnHi0_K2suI4QjBO76wjpgPJ0kb5DUg==', start_index=15892)
Annotation(end_index=15986, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGc8L0sQNS00wRzWOIuyFKMYcskXBf8tyLahhZcGcPS2_pfq_w5sGkvcuM4-Ufbx-5pU-w7yfZ8CnHbtPxlM7XwnAoHBQmtmi_VPgRVmBCXzaf8XJNH1G-_b6nqAhBJeK6hNT7Oq4gOnHi0_K2suI4QjBO76wjpgPJ0kb5DUg==', start_index=15976)
Annotation(end_index=16034, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGc8L0sQNS00wRzWOIuyFKMYcskXBf8tyLahhZcGcPS2_pfq_w5sGkvcuM4-Ufbx-5pU-w7yfZ8CnHbtPxlM7XwnAoHBQmtmi_VPgRVmBCXzaf8XJNH1G-_b6nqAhBJeK6hNT7Oq4gOnHi0_K2suI4QjBO76wjpgPJ0kb5DUg==', start_index=16024)
Annotation(end_index=16639, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOGhneWHE-pj88_vNilS7SHg-B1A0oqDG465JRlP7f8IA_D6JEHri9c6VJeLdTAQqCkYIKjM54QGsNbL2vLehp2B9B1V1YjBF5Sv7r-uSfnJpx6mO8vPBrSnE9PIh7qpNHa5dYOqxEFg28J9Le6BcStw==', start_index=16626)
Annotation(end_index=16639, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNhIyaiYSrkhfE4ddue8y8ylRowBnDyHZBNA6dZJnUsWCsIdLqpu_cm5HmLtWS3o44v_hCBr7alyPRaWmEz44d2EavZbDNQyx4RQ-Kmti79-Q9VWL0_-gV9IusTt4eWBwWg2FOzs-G4jo6J5h1y91lvzLcMB61Ca6SaNekQ9E3efHzsGWFYLWJ31PnaUZihGcsQXQa3XTnc5qCZ3tzDuXbsYR-Wg==', start_index=16626)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE38stMdx0cqypD7NwBfukk4GuibX3krTQjPXBMq3ERCjRVsbFL70imkQ1Ysjsyagnmubh9t8lzCJ4ogvE1zyjHo56Kp3unmVTFJgqNdVcqJNtmVuPhjrMnivWa4GAagYBk2UxKHKpET5OBxw==', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQWqCrrV0uzC4Kt4nmP9ufWTzxUWcCMlyIlW6cjgVcVSuGNkO3aCcVerwGNEyNd2JieltS8fv_jz-HjXUr_R0yVHFzml4wWi2Nx48l00cHSRqR-_5DI0pieg==', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElzYiVi8CMKizP5FNvojekrqY2AMH0YELSZ-XLNDR_oKi7BoGO1QdHogoFDPxzLbzzNEsDwpI2QXFIxgwDDfrL4JOpRMo6J8AXE8-iSLMhw_dAPlhfJCw5N3RurezkaLdUuHdfHXHoEF79a2unV-8U7FEXByFjFoFzyrJxAWs7Okc0xazVz2mC', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpgQEJwhBll0fRGScNd3nGPHNOX4ff-fFp1h0WBf4zJQnkhl7yFW8I5DcAA7kK8E6G-nL_4WeKLIcyLuXKc53c02AC_FxxBFE_KCJbATWpb86jh9owInbXFHxkD4wbztD3HWDPZKxUQpIgjc2KQQ4sfkHCoaxiJLcNnl1i_oMc7n6_FF20qssk6nmIeg==', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-fLjqWG3IU-B3REoaRs8929EdMVD4iujYh4-3l-Dq-O7E655KwJ-Is2K1xGU2BaCIWuHBZjQmyGpRoVgYsHFBdFRy0JZkr82mQ6BpM6B__bbEsh9L9Ych47zOFCykZIR4oIBQoS9wgVEHprbPrY8kJg5vnlaljzCGam_s5e8fEiBNXNz7aDAN1FkDMzLHfxPPOgx6WNG5zbIgoX2dGe66_VGvcA81Me_VOC7n-cSevZe0', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8Gz5kAyNa0yby2KmZMiRccinyDmLCD5Ojf311hupy6Ys_5MGBJKrA7Kxs8H7Q26Dvcq5uGXhXbYmlUHqw5qX3aQH5ztu7iO7Nk-1_cAk_Qy2cvfYBnXGSwNW1PoHb2cLxAuprVj9fiL_1AoVrN_ajCe0LMqfH-EMXUGN5wPQhWwc2aWdl2WlMiF0yu8JK003L3hVgcqX27P7bKYlqJ9fI1lWV5_I2mPo4EaHEeIDZVirnzMNj1R-7qB3RN_ty7LaGzREJZvWyzjL0wA==', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOGhneWHE-pj88_vNilS7SHg-B1A0oqDG465JRlP7f8IA_D6JEHri9c6VJeLdTAQqCkYIKjM54QGsNbL2vLehp2B9B1V1YjBF5Sv7r-uSfnJpx6mO8vPBrSnE9PIh7qpNHa5dYOqxEFg28J9Le6BcStw==', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTCyE7Hi5bGy4GvSuGjWi1lmtjFFSywCoCnkFTFuP0mtJhX4DsXnZ_vj39Ji1tMGiEOz8hp5iCTQI9Qw8fkIqjQ-p2wQ3HaPfp5zsX_4WiM4D1HbVPHb8lvnDgQkWJ_0wejVKZdLdnuF9Nx3kEDGQYmio0sjECE3QRX51EhX3lZR1x4WBFxMNOpEehlBZkei_monAxC0HkQQUFePCkBnY=', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhQ5TPAmqaI9XBA60t6ML7Y8U1OIoJ4jLe7S2Lk11THzA3AF2-DDsWCPwMILX7VR0pQhtrBMbosAG_7Hk4qlbfhKi2ELS7gKbGW_DhdinV-zYxIcP5zePWDBQf7fAv4qYqDbxClBOd8puPzSEPmAI5S8qVkQ==', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnbr60jnet00LAKIp-NRI-SUDlSIX6VAQejBTnIWTFpeOZLIZokB-5mWdXhERRQVBZsLfuwd1t5qcTb9V4FLtm50u7dEI0VOh1wFogWTrIUuFYpQfVj0GHx51AMf2zurshQfEFKq53Du7IoW5ffAT5cmfBwhte6LdznSiTv4cfAGZjdhwlsjUUVvKVyVhntSUN3yeAulGiAzkxeF2goqu0', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0udfpjY2aV57xsZK4hLU_IOu7qKTwoHoP8uNb8iw5aC-MK5rVfDzEyZxTrZlltAJ5rLw7QlNNwC38LYH9GummTaEZakDZ6KZJ5FweYYAeuatbXD7aRx76u0cUXrviPwRSRcLGzpl1eoXoY6kJE_EzGvPwWtNdhKS14ALy-O6SrRigSDN9JYUKCtQz4V6A_Q0KKDOK2ZHdHUfOh_A=', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBaqV9wCAThXJRiGPnXISJjaGp6u2XWTpHkwwhrTRO--uz1awmvU0Cd6WiEHWKTNpksyKTeHsEvDmZ3_D-qKmeKxwgbFgwz51sAt1vJHAc10f7tSehO_qW6hTsxX2jhzKsVQSkqxajR650JNaQ-IzSQpgbEllIxkg=', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLtQAd8L3aHQop5z2XTKVPG94_80zCuyC4tZKGy4cBKmtAsotWUwGU3JnxBG_3i9vWiKBiIPrzwa2xHmRtnGbUmTcMzFd9Ml5be6sKSdqpZzDek2hAQGXjUmuGp3WZE5MmT6O0u6yIcnd9xjHNSsBAgvS3hI6pYAgmfLqb37FXQQVQUQQVghDWk1BIIK1VGnlq_ErIBf7EBsqdVFd_u5vFdYxH2E5_aZgNZu-rNlDbJvKoSxEiX7-F4gwAZWjTxv6fqcbSkYsWU9S7R9WNPrNfrrdIfIDHebi5Y4Zokb4Cgcw_0U7DxnpUWziqZy9oBSkmhB2ynow7bsLt6L41IA4dkOB9qdBEGFGy_G-Yl6wOQb3OMHnulmBnqaCsUJ4=', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNyJXJuqwECFYWW4gQjb7k83TS6MGI22Lm6pFNTBFXt2dE5Cs-bL8sBCueTcx9knLLtT0ykljCaIydUHieBSQkT1PpQqwh4CJcZM98Sv4HV3L71NIM', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGapHzmXgRDTcFe-YEPGcA15IK5O5jHPhGy4cVtp4r8oX1poSSc1YEXEp5v3zhVergB8Xt4fLQAtxLrlLeLQpNFpdaZ9nil81mu2F1xxO1B-Xq2asxp17yfzdrOoC_mMnfLoNx7f4X1L8qLHw==', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwQmkoQWLpNMYqj6BT-uErq0I0AQvk6CkKksV0voWfK5CaNY28X5gXYKamUyfiSt-QEreZrzQn-5KKjIxZqrMjzCQYDInS473ipXTCh1vR1JSZwFq89k_JkAZQossl8xkdWfGHcLIz', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNhIyaiYSrkhfE4ddue8y8ylRowBnDyHZBNA6dZJnUsWCsIdLqpu_cm5HmLtWS3o44v_hCBr7alyPRaWmEz44d2EavZbDNQyx4RQ-Kmti79-Q9VWL0_-gV9IusTt4eWBwWg2FOzs-G4jo6J5h1y91lvzLcMB61Ca6SaNekQ9E3efHzsGWFYLWJ31PnaUZihGcsQXQa3XTnc5qCZ3tzDuXbsYR-Wg==', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSSz3P0NqJuJf31C5gqHWu2BoAHkZCHDZLSakadMm2epd1EkQwQYWsMgH62106t13dqdbmSXb5xkC9tamwtYdm1b3JNEw9rC-4EZpYjthvxlBoMhVTU3rk6w==', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZu7Nh0kAhybRbAxiuD_7EvaJIXKnW0MyrRHTgkwdLvdsexDajDneBLbPrZebslItkTMSOtemTrO1c2YwsFF8v1LczgipWmkx5_IZJeONxgoSd3u9j7soAIiAyen3Ey9P8sgJm6J8=', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_vf2iqDJkpzdPpo8GCZCOgC3qjVLMljwOOs9ta6aeJmXG2zrIa51kxJOz4Ko6BQNmUAeTNvO2QehPxvJjsMs53i9pB3_h6OEIbfVuXS0yfUs3q5OVEic5PSdgxZODrKyKiQU2DbMxw_KI_Kv1z54BfBp2s5IfuEstzSbuLpvHtTA9WeBPOWDcBH2LkIGLUXY=', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhDx2tM8_6mAyf_W9QjGk1AXBkiOhHxw1c6ksinKafwhcLmURN07yjpECusOpHN4utaDmDqB8F9VRUMRYzjfZVrhpW0ZXv9RqyJ7WWCpuvJvmuRRsvMQqiLZj0Noyt4UTckSKHNzh2cOH8edNp0QMakM94IDhXJjk3pAgoQ9hn7wKblUlm8DdLyihgLDjqryoMWeoXYyI=', start_index=17945)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoNbUbj621pkZq0buaTDEssCMJW8uQ4FM3LnJ0CiOvl47fHuRAl_rf2-5ZxGAaow2BPf-ylL0x5XUT18-l_QXoDZUtIXf9kLsc0yZDFHNNFhutTZ3YO1ydL4fKBFk=', start_index=17945)

## Sources
