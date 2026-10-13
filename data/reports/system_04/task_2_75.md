# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** d71b1373 | **Time:** 516.56s | **Cost:** $2.36879
--------------------------------------------------------------------------------

# In Restorative Justice Games, How Do Eigenvectors of Punishment Matrices Determine the Stability of Social Harmony Gradients?

## Key Points
*   **Mathematical Intersection:** The stability of "social harmony" in game-theoretic models is typically determined by the **eigenvalues** of the system's Jacobian matrix (in continuous replicator dynamics) or the transition matrix (in stochastic processes), rather than the eigenvectors of the "punishment matrix" in isolation. However, the eigenvectors of the payoff or transition matrices define the **stationary distributions** (gradients) of strategies within the population.
*   **Role of Punishment Matrices:** Punishment matrices modify the payoff structures (e.g., transforming a Prisoner's Dilemma into a coordination game). In dynamic models, these matrices influence the **Jacobian**, where the real parts of the eigenvalues determine whether a "social harmony" equilibrium (cooperation) is asymptotically stable or unstable.
*   **Social Harmony Gradients:** In recent evolutionary models (e.g., Perceptual Rationality), "social harmony" is defined as a specific perceptual type (perceiving high benefit/low cost to cooperation). The "gradient" refers to the frequency distribution of these types across a population. Stability is achieved when the "social harmony" strategy resists invasion by "anti-harmony" or "free-riding" mutants, often requiring specific **enhancement factors** or structural network properties.
*   **Revenge and Dynamics:** Economic models of conflict and restorative justice utilize differential equations where the **eigenvalues** of the system explicitly dictate whether a cycle of revenge decays into peace (harmony) or escalates.

---

## 1. Introduction: The Mathematical Architecture of Restorative Justice

The application of Game Theory to **Restorative Justice (RJ)** represents a shift from static payoff analysis to dynamic, evolutionary modeling. Unlike traditional retributive justice, which is often modeled as a one-shot or repeated **Prisoner’s Dilemma** where the Nash Equilibrium is mutual defection, restorative justice games introduce mechanisms for repairing harm, signaling remorse, and reintegrating offenders [cite: 1, 2].

The user’s query regarding "eigenvectors of punishment matrices" and "social harmony gradients" touches upon the advanced linear algebra used to solve **dynamical systems** in evolutionary game theory. In these systems, the "punishment matrix" (often denoted as part of the payoff structure) alters the flow of strategy adoption in a population. The **eigenvectors** of the resulting dynamic matrices (such as the Jacobian of the replicator equation) define the "directions" of stability—indicating whether a population will converge toward a gradient of high social harmony or diverge into chaos or mutual defection [cite: 3, 4].

This report synthesizes research on evolutionary dynamics, conflict resolution models, and perceptual rationality to explain how these mathematical components interact to determine the stability of social cohesion.

---

## 2. Theoretical Framework: Punishment Matrices in Evolutionary Games

### 2.1 Defining the Punishment Matrix
In the context of game theory applied to crime and justice, the interaction is often modeled between three agents: the **Offender**, the **Victim**, and the **Community/Judiciary** [cite: 1, 2]. The "Punishment Matrix" ($P$) can be conceptualized as a modification to the standard Payoff Matrix ($M$).

In a standard **Prisoner's Dilemma (PD)**, the payoff matrix dictates that defection ($D$) dominates cooperation ($C$). However, in a **Restorative Justice Game**, the matrix is altered by "punishment" (sanctions) and "restoration" (reparations).
*   **Retributive Matrix:** Focuses on imposing cost $c_p$ on the defector.
*   **Restorative Matrix:** Focuses on a transfer of utility (reparation $r$) from offender to victim and a "reintegration" cost/benefit for the community.

Research indicates that "punishment matrices" in dynamic control problems (a subset of game theory dealing with time-consistency) utilize **eigenvectors** to determine optimal policies over time [cite: 5]. Specifically, in systems where agents must coordinate to avoid "terminal outcomes" (like the collapse of social order), the punishment matrix defines the probability of sanctions. The **square root of the eigenvalues** of these matrices can dictate the probability distributions of strategies in equilibrium [cite: 6].

### 2.2 Eigenvectors and Stationary Distributions
In evolutionary game theory, if we treat the game as a Markov process (where individuals switch strategies based on success), the **transition matrix** $T$ describes the probability of moving from one state (e.g., "Offender") to another (e.g., "Reintegrated Citizen").

*   **The Eigenvector Connection:** The **principal eigenvector** (associated with the eigenvalue of 1) of this transition matrix represents the **stationary distribution** of the population [cite: 7].
*   **Application:** If the "punishment matrix" is effectively integrated into the transition probabilities, its eigenvectors determine the long-term "gradient" of the population—i.e., what percentage of the population ends up in the "Social Harmony" state versus the "Criminal" state.

---

## 3. Stability Analysis: Eigenvalues of the Jacobian

The core of the user's query regarding "stability" is best addressed through **Dynamical Systems Theory**. When modeling conflict and restorative justice, economists and mathematicians use systems of differential equations to represent the evolution of "revenge" versus "peace" [cite: 3].

### 3.1 The Conflict Dynamics Model
Research into the economics of conflict (specifically regarding revenge and restorative justice) models the level of hostility as a time-dependent variable. The stability of the system—whether it settles into **social harmony** (zero conflict) or escalates—is determined by the **eigenvalues** of the system's coefficient matrix.

*   **The System:** Let $x(t)$ be the level of aggression. The rate of change $\dot{x}$ depends on past grievances and current punishments.
*   **Eigenvalue Analysis:** The solution to these differential equations often takes the form:
    \[ x(t) = c_1 e^{\lambda_1 t} \mathbf{v}_1 + c_2 e^{\lambda_2 t} \mathbf{v}_2 \]
    Here, $\lambda$ represents the **eigenvalues** and $\mathbf{v}$ represents the **eigenvectors** [cite: 3].
*   **Stability Condition:** For "social harmony" (where $x(t) \to 0$) to be a stable equilibrium, the real parts of all eigenvalues $\lambda$ must be **negative**. If the "punishment matrix" (which influences the coefficients of the system) produces positive eigenvalues, the conflict is unstable and will escalate, destroying social harmony.

### 3.2 Replicator Dynamics and the Jacobian
In **Evolutionary Game Theory (EGT)**, the evolution of strategies (e.g., Cooperate vs. Defect) is governed by the **Replicator Equation**. The stability of a fixed point (such as a population of pure cooperators, i.e., Social Harmony) is analyzed by calculating the **Jacobian Matrix** ($J$) of the system at that point [cite: 4].

*   **The Jacobian:** This matrix represents the gradient of the selection vectors.
*   **Stability of Harmony:** A state of social harmony is **Evolutionarily Stable (ESS)** if the eigenvalues of the Jacobian at that point have negative real parts.
*   **Impact of Punishment:** The parameters of the punishment matrix (e.g., severity of penalty $f$, probability of detection $m$) directly populate the Jacobian. Therefore, changing the punishment matrix shifts the eigenvalues.
    *   *Result:* If the punishment is too weak, the eigenvalues may be positive, rendering social harmony unstable (susceptible to invasion by defectors) [cite: 1, 4].

---

## 4. Social Harmony Gradients: Perceptual Rationality and Types

Recent breakthroughs in EGT, specifically the "Perceptual Rationality" framework, provide a precise definition of "Social Harmony" types and their gradients [cite: 8, 9].

### 4.1 Defining "Social Harmony" Types
In the **Perceptual Public Goods Game**, individuals are characterized by a vector $(c, b, s)$, where $c$ and $b$ are perceived costs/benefits and $s$ is **sociality** (susceptibility to social influence).
*   **The Social Harmony Type:** This is defined as a specific perceptual strategy, often denoted as $(0, 1, 1)$ or similar binary representations. These individuals perceive the cost of cooperation as zero and the benefit as maximal, and they are highly influenced by the group [cite: 8, 10].
*   **Behavior:** Social Harmony types do not withhold cooperation from "randomizing types" but will withhold it in groups dominated by "anti-harmony" perceptions [cite: 8].

### 4.2 The "Gradient" of Social Harmony
The "gradient" refers to the **distribution of sociality ($s$)** and perceptual types across the population.
*   **Stability of the Gradient:** The research shows that the stability of this gradient is non-monotonic. As the **enhancement factor** (efficiency of the public good) increases, the frequency of Social Harmony types increases, but only up to a point (approx $r \approx 2.7$) [cite: 8].
*   **Eigenvector Centrality:** In network-structured populations (lattices), the influence of a "Social Harmony" type can be measured by their **Eigenvector Centrality**. High centrality nodes that adopt restorative/cooperative strategies can stabilize the entire network toward harmony, acting as anchors against defectors [cite: 11, 12].

### 4.3 Punishment and the Gradient
In models combining **social reward and punishment**, the combination of mechanisms creates "inhomogeneities" (gradients) in social relations.
*   **Mechanism:** A pure punishment mechanism often fails to promote extensive cooperation. However, a **combination of reward and punishment** stabilizes the "Social Harmony" gradient by ensuring that cooperators (harmony types) can survive even when temptation to defect is high [cite: 12].
*   **Eigenvector Dynamics:** The "eigenvector" of the adjacency matrix in these social networks represents the **stationary distribution of influence**. If the punishment matrix targets high-eigenvector-centrality defectors effectively, the "Social Harmony gradient" becomes stable [cite: 11].

---

## 5. Synthesis: How Eigenvectors Determine Stability

To directly answer the query: **Eigenvectors of punishment matrices (or the system matrices influenced by punishment) determine the stability of social harmony gradients by defining the asymptotic behavior of the population's strategy distribution.**

### 5.1 The Mechanism of Determination
1.  **Construction of the Matrix:** The interaction is defined by a matrix $M$ which includes payoffs for cooperation and penalties for defection (the punishment component).
2.  **Dynamic Evolution:** The population evolves according to $\dot{\mathbf{x}} = \mathbf{x} \cdot (M\mathbf{x} - \bar{P})$, where $\mathbf{x}$ is the vector of strategy frequencies (the gradient).
3.  **Linearization (The Eigenvalue Step):** To check if a "Social Harmony" state (e.g., $\mathbf{x}^* = [cite: 13]^T$) is stable, we linearize this equation. The **Jacobian Matrix** $J$ is derived from $M$.
4.  **Eigenvector Direction:** The **eigenvectors** of $J$ associated with positive eigenvalues represent the "directions of instability"—the specific mutant strategies (e.g., "Vengeful Defector") that will grow and destroy social harmony. The **eigenvectors** associated with negative eigenvalues represent directions of stability, where deviations are corrected, preserving the harmony gradient [cite: 3, 4].

### 5.2 Case Study: Environmental Restorative Justice
In the tripartite evolutionary game of environmental crime (Judiciary, Offender, Victim), the stability of the "Restorative" equilibrium is analyzed.
*   **Findings:** Top-down RJ reforms often face resistance (instability) due to insufficient public participation. The **evolutionary stability** (determined by the eigenvalues of the replicator dynamics) requires a "moderate penal intensity" (punishment matrix parameter) to make the "intrinsic legal motivation" (harmony) stable [cite: 1, 2].
*   **Gradient:** The "gradient" here is the proportion of offenders accepting RJ versus traditional punishment. The eigenvectors of the game dynamics determine whether this proportion converges to 100% (stable harmony) or oscillates [cite: 4].

---

## 6. Conclusion

The stability of **social harmony gradients** in restorative justice games is mathematically governed by the spectral properties (eigenvalues and eigenvectors) of the dynamic matrices that describe the system.
*   **Eigenvalues** determine **stability**: Negative real parts ensure that the social harmony equilibrium is robust against invasion by non-cooperative strategies.
*   **Eigenvectors** determine **direction**: They describe the specific mix of strategies (the gradient) that comprises the stable state or the path the population takes to reach it.
*   **Punishment Matrices** act as the control parameters: By adjusting the severity and probability of punishment, the matrix entries change, shifting the eigenvalues. A properly tuned punishment matrix moves the eigenvalues into the negative half-plane, stabilizing the social harmony gradient [cite: 3, 4, 5].

In summary, while "eigenvectors of punishment matrices" is a highly technical phrasing, it accurately describes the linear algebraic mechanism by which evolutionary game theory predicts whether a society will settle into a stable state of restorative cooperation or fracture into conflict.

## 7. Detailed Literature Review and Source Analysis

### 7.1 Evolutionary Dynamics of Crime and Punishment
The application of **Evolutionary Game Theory (EGT)** to crime is well-documented. Source [cite: 4] explicitly studies the "dynamics and stability of the crime and punishment game." It uses **replicator dynamics** to show that a culture of "honest agents" (social harmony) is never stable without specific conditions. The stability is analyzed via the **Jacobian matrix**, where the **eigenvalues** determine the bifurcation points. When the penalty (punishment matrix) is high enough, the system tends toward an equilibrium of honest agents.

### 7.2 Perceptual Rationality and Harmony Types
Source [cite: 8, 9] introduces "Perceptual Rationality." This is critical for defining "Social Harmony" not just as an outcome, but as a **strategy type**.
*   **Type (0,1,1):** This type perceives the public good as having no cost and high benefit and is socially influenced.
*   **Stability:** The paper analyzes the "enhancement factor" (a payoff multiplier). The stability of the cooperation gradient is maintained by "social harmony types" who cooperate with "randomizing types" but defect against "anti-harmony" types. This conditional cooperation creates a stable gradient of sociality.

### 7.3 The Mathematics of Revenge and Reconciliation
Source [cite: 3] provides the most direct mathematical link. It models "revenge" in conflicts using differential equations. It explicitly states: *"By determining the eigenvalues and the eigenvectors of this system, it can be shown that the solution is..."* This confirms that in theoretical economics, the cessation of conflict (restoration) is a spectral problem. The "punishment" here is the act of revenge, and its matrix representation determines the system's oscillatory or decaying behavior (stability).

### 7.4 Social Network Analysis (SNA) and Harmony
Source [cite: 11] links **Eigenvector Centrality** to social harmony in architectural/spatial networks. While distinct from EGT, it reinforces the concept that "eigenvectors" measure the distribution of influence (gradients) in a system designed for social cohesion.

### 7.5 Survival-Imposed Defection Games
Source [cite: 14] introduces "Survival-Imposed Defection Games" (SIDGs). It shows that defection becomes the dominant strategy under **asymmetric punishment matrices**. This implies that for "Social Harmony" to be stable, the punishment matrix must possess specific symmetry or spectral properties that prevent the dominance of defection.

## References
*   **[cite: 8, 9]** Salahshour, M. (2025). *Perceptual rationality: an evolutionary game theory of perceptually rational decision-making*. Royal Society Open Science.
*   **[cite: 1, 2]** Zhang, X., & Zhang, J. (2025). *The application of restorative justice in China's environmental crime: an evolutionary game perspective*. Crime, Law and Social Change.
*   **[cite: 3]** *Revenge in Conflicts*. (2008). MPRA Paper.
*   **[cite: 4]** Quinteros, & Villena. (2022). *On the Dynamics and Stability of the Crime and Punishment Game*.
*   **[cite: 5]** *Time Inconsistency and Punishment Matrices in Control Theory*. (2021).
*   **[cite: 12]** *The combination of social reward and punishment is essential to social harmony*. (2022). Chaos.
*   **[cite: 11]** *Social network analysis (SNA) in architectural conceptual design*. (2025).
*   **[cite: 14]** Durrani, I. (2025). *PRISONER'S DILEMMA: Jail-Breaking via Game Theory*.

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIE8XZTA9SnEprDnfQnkdL0deTsftQSvkvy-TcG4sUoBX5pxd5j1T_wb1T4s2j014YEyq0ePFD-AOKdKGN7mCzsZb_5vxPkUU_HTU17Uus5QgZ6SQe7P-606t5GYUodAV-c15Et_psw8Dp89cSnTZvLLbTZe4hIWCS6AevjTzPcq-cvm4j_EnJe-3oSz9A6leE2lBpUbWx-QnwFJLQ6oGOs7EiL7yfCBBGJsXTcoSrd_cV3d7e0zpcj8z4OE-oTxKh7o93K_MoOTy9FN_BJ6w=)
2. [proquest.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCNxIwopnCSSWzyHGuBAU4mO3BTNpJ3ESmtbEcsMJDSyMPQAELSwcTgK1QSXXpu9kKHrSzdU1ZaKXMQKjhJ-Dg4igm1lXLhE2Ta-jtoo9FRgX8F-zMVUkWpClAlmAOacAqjDjWn72_wXIibyAb1pbMLT9Np0t-VEqGHoR0M1NS0ScyAmjwRYuyD9YUCu4HaLs3bC5pw6FEdGLUOQ==)
3. [uni-muenchen.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf4dqqDchrQPhLBTwO3r2eMDN9bY5f3mFIo2Hbvu43L0auK1t5j43kT7hs2NgBK93sDPWv32SajKdwyGRZRh-aYy7VguNojdU6nLMslegfeFQpU9v2PUj_z90xGeJqRMi573Irf4zHiTNZgruff_g=)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhZqdWFhu_V1dOcrhOfwRKszd6lAV98WM2Vgx9_CC4rA66zBdxB000yIUd1Jw75EC_LomqnaSvwnmNY-iOhjIjdTv62tcrnVLwm8P_coTec11fO6LXMK6SS_04PC_wUcWSHTvoxBB-7yLE_fvxK0b-GL35ZgjcJlB00OrB8mMeKXQPULbdSblF_kZeuD_BjtytFSCjuq5gkY4qWt64EeY9HL5sPqn1)
5. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3G0eqKP-CSRsaecZk9-Ac5zNcM9uYRVS7IjAaD_Xd8nwn0Wq2y4ip_p9P7H-XnZ3WAgQw6aiOJ4gzHwZTV_q-V753eUuR0n97HoGwlomdN0d9WU8f)
6. [dtic.mil](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHp0M-MfmKhDkXJq3FaYTUtKLHd7jEFp3pkeC0qXBxjqs33059GYeaqsReA4BsH5RDd7hr3KEPbKVNkw2O7CPVzGQKYpIyvOixDiCFGW4aKUHnmV1K-sDlZi_jD6fFXGR6yjlA=)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmjvLVPu7RKRnE9HmF-aH-LieqKA2cE4I8IjHS3QKY4KqMtiv7NYSrBg053V_qEIabvE81VK9TjiEKRQaiYAamomeY8xxnSbol5u1TdMe5-ZCRqt6agGngIodoygnxPd6GFtkwwfOMxrcgRH1-WSdmyolMi6tAf8CyvVVorPx9u39QWGvAeFA3oGr9C8PbfjGCkDaJqYgb3qyXfjzN_g3CmxUOQTQE5PAARdgTgSgddPqPrCAyy1zonQ==)
8. [royalsocietypublishing.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGphYPi05vBcAzndZLyFFXw7bk1GtdjJQUMqGVyvNJbFDRhB47A4nOt8Dz6eNtwTDqeqZgQmzCtb1-ER7hn9TcZ16MswgH1BALOqCsQaWQUJG2cWng7TEWZa0f485wcnnpA94rP_4bcQThnhUGOzxzwnRrFizeMXLepMMYL9hTuTLqZmc_G2VRVebvAPhfbNPN07uBFo-ojm-D6E1xZE8KnnlcqMZc3_Cs9zI4=)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZ6sq1n_aV70xv4qhnGWdYnKkdOCSnqKKNWyQXanObV95FnRta6bvLIaJzQ1vb4L2BKU5oZ6dhSkG5rDHExf3q3qsVLPFQMheDBD9sm3FUPrD7vlhNsxjHVxRzruhqPoGBaJNagnH5rXopLru10ifwsLAFNcrWc3oTumGXOMZwvizsYqS20n8eh0jEY2EhJOfPNHYEjCAHLQ1enI86AEbd9aoM7D1SJOb8D7EjxnpK2keCzZrS1tZphGw0tfNrKlKQxhMB)
10. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVOYUf_lHg7x5ab8lTvuiRuFKX99iqdcVP2Pj71_huVcFoeBrNrwwaF-GhbnCrUOp764yZgRMNramWeaxKcBz49Dog4I2kg88K5IRXe9X90jtwwHb4Usks)
11. [emerald.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdssBsLln_mbwwdgJWFhP_uiFnVEyiczydMn2ltABxu7Ej4_EztbnOeW--c5FASH88J4IdD6aV16fpABlBis5a8FIkwf49r4oCgJC52eoF9XqX6rn4wVjEWjDnhWCMSEaNf7HqydGKBaVbJF0kG9jPmclIz7jy4HUWvaXd4JqrKUsvLiXtDvbJlB9ZKSlk_MVcS85LVEFQMl3HXGSnTIQvgFnm5GA1Kl7MdpzA)
12. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4MWymDRbXEH0uK4_VGEgNWr6G0TwTdnmT9lsziR0kOkl9kc23WI5E7GRcesh-m7Eg23cfHCazkTuwbLNcAmLO2cGRLxbsdXxrCPVNUl47r_LBsl96oKZnXUIUkRcsN2DQW32ImZ7cp4qTE15GV5d2NBmGtdA3BQ0fdIZZPp-t_jSYQ8FXNlX8_P1mrkfLCodTiuP1brcNSJ9tkcpkYBLQ1Q==)
13. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE16mJut9Pqo9n4Hkd7_Ji4K3V5ni20eTj_3ZJtSEMEuqUSfm1XKLnKRPVjDzA_nQN9D7xCB4ECRzCtNndE1YCznXxQqnNbBCQybF6IS8LnlauMbfiMpBXkX0qiqMdRihGf7dtnxP4UiOFTS_7Y2Efg773G9v3kN-I3szkMtdXndDlW0YFFatI0JBH1L1dW4fdHlJSi5tBfArMc5hGwpVEk-4QrECSgzOEgwg==)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9rSBvMTqsre7BptrYyTP24mhgxqQWeKiCaN6V-laoCUC7_7oMZik4NX9WlE68p-oneO2iZVfG_4JpeNTnRx5U2E7n74GcZyiifJXQgGOfz3_Z0TuG40hNbqvVGFMAbJxFG-mm3y2sHCzoFXqAetMQc4DyiJTipH-4kNRtmMALnX3AgiCAtZHhzAqIwCOgg0yvar1l1clnhA==)


## Annotations
Annotation(end_index=2231, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCNxIwopnCSSWzyHGuBAU4mO3BTNpJ3ESmtbEcsMJDSyMPQAELSwcTgK1QSXXpu9kKHrSzdU1ZaKXMQKjhJ-Dg4igm1lXLhE2Ta-jtoo9FRgX8F-zMVUkWpClAlmAOacAqjDjWn72_wXIibyAb1pbMLT9Np0t-VEqGHoR0M1NS0ScyAmjwRYuyD9YUCu4HaLs3bC5pw6FEdGLUOQ==', start_index=2219)
Annotation(end_index=2231, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIE8XZTA9SnEprDnfQnkdL0deTsftQSvkvy-TcG4sUoBX5pxd5j1T_wb1T4s2j014YEyq0ePFD-AOKdKGN7mCzsZb_5vxPkUU_HTU17Uus5QgZ6SQe7P-606t5GYUodAV-c15Et_psw8Dp89cSnTZvLLbTZe4hIWCS6AevjTzPcq-cvm4j_EnJe-3oSz9A6leE2lBpUbWx-QnwFJLQ6oGOs7EiL7yfCBBGJsXTcoSrd_cV3d7e0zpcj8z4OE-oTxKh7o93K_MoOTy9FN_BJ6w=', start_index=2219)
Annotation(end_index=2867, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf4dqqDchrQPhLBTwO3r2eMDN9bY5f3mFIo2Hbvu43L0auK1t5j43kT7hs2NgBK93sDPWv32SajKdwyGRZRh-aYy7VguNojdU6nLMslegfeFQpU9v2PUj_z90xGeJqRMi573Irf4zHiTNZgruff_g=', start_index=2855)
Annotation(end_index=2867, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhZqdWFhu_V1dOcrhOfwRKszd6lAV98WM2Vgx9_CC4rA66zBdxB000yIUd1Jw75EC_LomqnaSvwnmNY-iOhjIjdTv62tcrnVLwm8P_coTec11fO6LXMK6SS_04PC_wUcWSHTvoxBB-7yLE_fvxK0b-GL35ZgjcJlB00OrB8mMeKXQPULbdSblF_kZeuD_BjtytFSCjuq5gkY4qWt64EeY9HL5sPqn1', start_index=2855)
Annotation(end_index=3395, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCNxIwopnCSSWzyHGuBAU4mO3BTNpJ3ESmtbEcsMJDSyMPQAELSwcTgK1QSXXpu9kKHrSzdU1ZaKXMQKjhJ-Dg4igm1lXLhE2Ta-jtoo9FRgX8F-zMVUkWpClAlmAOacAqjDjWn72_wXIibyAb1pbMLT9Np0t-VEqGHoR0M1NS0ScyAmjwRYuyD9YUCu4HaLs3bC5pw6FEdGLUOQ==', start_index=3383)
Annotation(end_index=3395, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIE8XZTA9SnEprDnfQnkdL0deTsftQSvkvy-TcG4sUoBX5pxd5j1T_wb1T4s2j014YEyq0ePFD-AOKdKGN7mCzsZb_5vxPkUU_HTU17Uus5QgZ6SQe7P-606t5GYUodAV-c15Et_psw8Dp89cSnTZvLLbTZe4hIWCS6AevjTzPcq-cvm4j_EnJe-3oSz9A6leE2lBpUbWx-QnwFJLQ6oGOs7EiL7yfCBBGJsXTcoSrd_cV3d7e0zpcj8z4OE-oTxKh7o93K_MoOTy9FN_BJ6w=', start_index=3383)
Annotation(end_index=4189, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3G0eqKP-CSRsaecZk9-Ac5zNcM9uYRVS7IjAaD_Xd8nwn0Wq2y4ip_p9P7H-XnZ3WAgQw6aiOJ4gzHwZTV_q-V753eUuR0n97HoGwlomdN0d9WU8f', start_index=4180)
Annotation(end_index=4508, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHp0M-MfmKhDkXJq3FaYTUtKLHd7jEFp3pkeC0qXBxjqs33059GYeaqsReA4BsH5RDd7hr3KEPbKVNkw2O7CPVzGQKYpIyvOixDiCFGW4aKUHnmV1K-sDlZi_jD6fFXGR6yjlA=', start_index=4499)
Annotation(end_index=5031, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmjvLVPu7RKRnE9HmF-aH-LieqKA2cE4I8IjHS3QKY4KqMtiv7NYSrBg053V_qEIabvE81VK9TjiEKRQaiYAamomeY8xxnSbol5u1TdMe5-ZCRqt6agGngIodoygnxPd6GFtkwwfOMxrcgRH1-WSdmyolMi6tAf8CyvVVorPx9u39QWGvAeFA3oGr9C8PbfjGCkDaJqYgb3qyXfjzN_g3CmxUOQTQE5PAARdgTgSgddPqPrCAyy1zonQ==', start_index=5022)
Annotation(end_index=5669, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf4dqqDchrQPhLBTwO3r2eMDN9bY5f3mFIo2Hbvu43L0auK1t5j43kT7hs2NgBK93sDPWv32SajKdwyGRZRh-aYy7VguNojdU6nLMslegfeFQpU9v2PUj_z90xGeJqRMi573Irf4zHiTNZgruff_g=', start_index=5660)
Annotation(end_index=6473, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf4dqqDchrQPhLBTwO3r2eMDN9bY5f3mFIo2Hbvu43L0auK1t5j43kT7hs2NgBK93sDPWv32SajKdwyGRZRh-aYy7VguNojdU6nLMslegfeFQpU9v2PUj_z90xGeJqRMi573Irf4zHiTNZgruff_g=', start_index=6464)
Annotation(end_index=7195, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhZqdWFhu_V1dOcrhOfwRKszd6lAV98WM2Vgx9_CC4rA66zBdxB000yIUd1Jw75EC_LomqnaSvwnmNY-iOhjIjdTv62tcrnVLwm8P_coTec11fO6LXMK6SS_04PC_wUcWSHTvoxBB-7yLE_fvxK0b-GL35ZgjcJlB00OrB8mMeKXQPULbdSblF_kZeuD_BjtytFSCjuq5gkY4qWt64EeY9HL5sPqn1', start_index=7186)
Annotation(end_index=7845, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIE8XZTA9SnEprDnfQnkdL0deTsftQSvkvy-TcG4sUoBX5pxd5j1T_wb1T4s2j014YEyq0ePFD-AOKdKGN7mCzsZb_5vxPkUU_HTU17Uus5QgZ6SQe7P-606t5GYUodAV-c15Et_psw8Dp89cSnTZvLLbTZe4hIWCS6AevjTzPcq-cvm4j_EnJe-3oSz9A6leE2lBpUbWx-QnwFJLQ6oGOs7EiL7yfCBBGJsXTcoSrd_cV3d7e0zpcj8z4OE-oTxKh7o93K_MoOTy9FN_BJ6w=', start_index=7833)
Annotation(end_index=7845, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhZqdWFhu_V1dOcrhOfwRKszd6lAV98WM2Vgx9_CC4rA66zBdxB000yIUd1Jw75EC_LomqnaSvwnmNY-iOhjIjdTv62tcrnVLwm8P_coTec11fO6LXMK6SS_04PC_wUcWSHTvoxBB-7yLE_fvxK0b-GL35ZgjcJlB00OrB8mMeKXQPULbdSblF_kZeuD_BjtytFSCjuq5gkY4qWt64EeY9HL5sPqn1', start_index=7833)
Annotation(end_index=8088, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGphYPi05vBcAzndZLyFFXw7bk1GtdjJQUMqGVyvNJbFDRhB47A4nOt8Dz6eNtwTDqeqZgQmzCtb1-ER7hn9TcZ16MswgH1BALOqCsQaWQUJG2cWng7TEWZa0f485wcnnpA94rP_4bcQThnhUGOzxzwnRrFizeMXLepMMYL9hTuTLqZmc_G2VRVebvAPhfbNPN07uBFo-ojm-D6E1xZE8KnnlcqMZc3_Cs9zI4=', start_index=8076)
Annotation(end_index=8088, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZ6sq1n_aV70xv4qhnGWdYnKkdOCSnqKKNWyQXanObV95FnRta6bvLIaJzQ1vb4L2BKU5oZ6dhSkG5rDHExf3q3qsVLPFQMheDBD9sm3FUPrD7vlhNsxjHVxRzruhqPoGBaJNagnH5rXopLru10ifwsLAFNcrWc3oTumGXOMZwvizsYqS20n8eh0jEY2EhJOfPNHYEjCAHLQ1enI86AEbd9aoM7D1SJOb8D7EjxnpK2keCzZrS1tZphGw0tfNrKlKQxhMB', start_index=8076)
Annotation(end_index=8629, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGphYPi05vBcAzndZLyFFXw7bk1GtdjJQUMqGVyvNJbFDRhB47A4nOt8Dz6eNtwTDqeqZgQmzCtb1-ER7hn9TcZ16MswgH1BALOqCsQaWQUJG2cWng7TEWZa0f485wcnnpA94rP_4bcQThnhUGOzxzwnRrFizeMXLepMMYL9hTuTLqZmc_G2VRVebvAPhfbNPN07uBFo-ojm-D6E1xZE8KnnlcqMZc3_Cs9zI4=', start_index=8616)
Annotation(end_index=8629, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVOYUf_lHg7x5ab8lTvuiRuFKX99iqdcVP2Pj71_huVcFoeBrNrwwaF-GhbnCrUOp764yZgRMNramWeaxKcBz49Dog4I2kg88K5IRXe9X90jtwwHb4Usks', start_index=8616)
Annotation(end_index=8803, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGphYPi05vBcAzndZLyFFXw7bk1GtdjJQUMqGVyvNJbFDRhB47A4nOt8Dz6eNtwTDqeqZgQmzCtb1-ER7hn9TcZ16MswgH1BALOqCsQaWQUJG2cWng7TEWZa0f485wcnnpA94rP_4bcQThnhUGOzxzwnRrFizeMXLepMMYL9hTuTLqZmc_G2VRVebvAPhfbNPN07uBFo-ojm-D6E1xZE8KnnlcqMZc3_Cs9zI4=', start_index=8794)
Annotation(end_index=9243, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGphYPi05vBcAzndZLyFFXw7bk1GtdjJQUMqGVyvNJbFDRhB47A4nOt8Dz6eNtwTDqeqZgQmzCtb1-ER7hn9TcZ16MswgH1BALOqCsQaWQUJG2cWng7TEWZa0f485wcnnpA94rP_4bcQThnhUGOzxzwnRrFizeMXLepMMYL9hTuTLqZmc_G2VRVebvAPhfbNPN07uBFo-ojm-D6E1xZE8KnnlcqMZc3_Cs9zI4=', start_index=9234)
Annotation(end_index=9584, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdssBsLln_mbwwdgJWFhP_uiFnVEyiczydMn2ltABxu7Ej4_EztbnOeW--c5FASH88J4IdD6aV16fpABlBis5a8FIkwf49r4oCgJC52eoF9XqX6rn4wVjEWjDnhWCMSEaNf7HqydGKBaVbJF0kG9jPmclIz7jy4HUWvaXd4JqrKUsvLiXtDvbJlB9ZKSlk_MVcS85LVEFQMl3HXGSnTIQvgFnm5GA1Kl7MdpzA', start_index=9570)
Annotation(end_index=9584, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4MWymDRbXEH0uK4_VGEgNWr6G0TwTdnmT9lsziR0kOkl9kc23WI5E7GRcesh-m7Eg23cfHCazkTuwbLNcAmLO2cGRLxbsdXxrCPVNUl47r_LBsl96oKZnXUIUkRcsN2DQW32ImZ7cp4qTE15GV5d2NBmGtdA3BQ0fdIZZPp-t_jSYQ8FXNlX8_P1mrkfLCodTiuP1brcNSJ9tkcpkYBLQ1Q==', start_index=9570)
Annotation(end_index=10058, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4MWymDRbXEH0uK4_VGEgNWr6G0TwTdnmT9lsziR0kOkl9kc23WI5E7GRcesh-m7Eg23cfHCazkTuwbLNcAmLO2cGRLxbsdXxrCPVNUl47r_LBsl96oKZnXUIUkRcsN2DQW32ImZ7cp4qTE15GV5d2NBmGtdA3BQ0fdIZZPp-t_jSYQ8FXNlX8_P1mrkfLCodTiuP1brcNSJ9tkcpkYBLQ1Q==', start_index=10048)
Annotation(end_index=10353, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdssBsLln_mbwwdgJWFhP_uiFnVEyiczydMn2ltABxu7Ej4_EztbnOeW--c5FASH88J4IdD6aV16fpABlBis5a8FIkwf49r4oCgJC52eoF9XqX6rn4wVjEWjDnhWCMSEaNf7HqydGKBaVbJF0kG9jPmclIz7jy4HUWvaXd4JqrKUsvLiXtDvbJlB9ZKSlk_MVcS85LVEFQMl3HXGSnTIQvgFnm5GA1Kl7MdpzA', start_index=10343)
Annotation(end_index=11195, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE16mJut9Pqo9n4Hkd7_Ji4K3V5ni20eTj_3ZJtSEMEuqUSfm1XKLnKRPVjDzA_nQN9D7xCB4ECRzCtNndE1YCznXxQqnNbBCQybF6IS8LnlauMbfiMpBXkX0qiqMdRihGf7dtnxP4UiOFTS_7Y2Efg773G9v3kN-I3szkMtdXndDlW0YFFatI0JBH1L1dW4fdHlJSi5tBfArMc5hGwpVEk-4QrECSgzOEgwg==', start_index=11185)
Annotation(end_index=11699, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf4dqqDchrQPhLBTwO3r2eMDN9bY5f3mFIo2Hbvu43L0auK1t5j43kT7hs2NgBK93sDPWv32SajKdwyGRZRh-aYy7VguNojdU6nLMslegfeFQpU9v2PUj_z90xGeJqRMi573Irf4zHiTNZgruff_g=', start_index=11687)
Annotation(end_index=11699, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhZqdWFhu_V1dOcrhOfwRKszd6lAV98WM2Vgx9_CC4rA66zBdxB000yIUd1Jw75EC_LomqnaSvwnmNY-iOhjIjdTv62tcrnVLwm8P_coTec11fO6LXMK6SS_04PC_wUcWSHTvoxBB-7yLE_fvxK0b-GL35ZgjcJlB00OrB8mMeKXQPULbdSblF_kZeuD_BjtytFSCjuq5gkY4qWt64EeY9HL5sPqn1', start_index=11687)
Annotation(end_index=12250, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCNxIwopnCSSWzyHGuBAU4mO3BTNpJ3ESmtbEcsMJDSyMPQAELSwcTgK1QSXXpu9kKHrSzdU1ZaKXMQKjhJ-Dg4igm1lXLhE2Ta-jtoo9FRgX8F-zMVUkWpClAlmAOacAqjDjWn72_wXIibyAb1pbMLT9Np0t-VEqGHoR0M1NS0ScyAmjwRYuyD9YUCu4HaLs3bC5pw6FEdGLUOQ==', start_index=12238)
Annotation(end_index=12250, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIE8XZTA9SnEprDnfQnkdL0deTsftQSvkvy-TcG4sUoBX5pxd5j1T_wb1T4s2j014YEyq0ePFD-AOKdKGN7mCzsZb_5vxPkUU_HTU17Uus5QgZ6SQe7P-606t5GYUodAV-c15Et_psw8Dp89cSnTZvLLbTZe4hIWCS6AevjTzPcq-cvm4j_EnJe-3oSz9A6leE2lBpUbWx-QnwFJLQ6oGOs7EiL7yfCBBGJsXTcoSrd_cV3d7e0zpcj8z4OE-oTxKh7o93K_MoOTy9FN_BJ6w=', start_index=12238)
Annotation(end_index=12495, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhZqdWFhu_V1dOcrhOfwRKszd6lAV98WM2Vgx9_CC4rA66zBdxB000yIUd1Jw75EC_LomqnaSvwnmNY-iOhjIjdTv62tcrnVLwm8P_coTec11fO6LXMK6SS_04PC_wUcWSHTvoxBB-7yLE_fvxK0b-GL35ZgjcJlB00OrB8mMeKXQPULbdSblF_kZeuD_BjtytFSCjuq5gkY4qWt64EeY9HL5sPqn1', start_index=12486)
Annotation(end_index=13392, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3G0eqKP-CSRsaecZk9-Ac5zNcM9uYRVS7IjAaD_Xd8nwn0Wq2y4ip_p9P7H-XnZ3WAgQw6aiOJ4gzHwZTV_q-V753eUuR0n97HoGwlomdN0d9WU8f', start_index=13377)
Annotation(end_index=13392, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf4dqqDchrQPhLBTwO3r2eMDN9bY5f3mFIo2Hbvu43L0auK1t5j43kT7hs2NgBK93sDPWv32SajKdwyGRZRh-aYy7VguNojdU6nLMslegfeFQpU9v2PUj_z90xGeJqRMi573Irf4zHiTNZgruff_g=', start_index=13377)
Annotation(end_index=13392, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhZqdWFhu_V1dOcrhOfwRKszd6lAV98WM2Vgx9_CC4rA66zBdxB000yIUd1Jw75EC_LomqnaSvwnmNY-iOhjIjdTv62tcrnVLwm8P_coTec11fO6LXMK6SS_04PC_wUcWSHTvoxBB-7yLE_fvxK0b-GL35ZgjcJlB00OrB8mMeKXQPULbdSblF_kZeuD_BjtytFSCjuq5gkY4qWt64EeY9HL5sPqn1', start_index=13377)
Annotation(end_index=13893, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhZqdWFhu_V1dOcrhOfwRKszd6lAV98WM2Vgx9_CC4rA66zBdxB000yIUd1Jw75EC_LomqnaSvwnmNY-iOhjIjdTv62tcrnVLwm8P_coTec11fO6LXMK6SS_04PC_wUcWSHTvoxBB-7yLE_fvxK0b-GL35ZgjcJlB00OrB8mMeKXQPULbdSblF_kZeuD_BjtytFSCjuq5gkY4qWt64EeY9HL5sPqn1', start_index=13884)
Annotation(end_index=14406, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGphYPi05vBcAzndZLyFFXw7bk1GtdjJQUMqGVyvNJbFDRhB47A4nOt8Dz6eNtwTDqeqZgQmzCtb1-ER7hn9TcZ16MswgH1BALOqCsQaWQUJG2cWng7TEWZa0f485wcnnpA94rP_4bcQThnhUGOzxzwnRrFizeMXLepMMYL9hTuTLqZmc_G2VRVebvAPhfbNPN07uBFo-ojm-D6E1xZE8KnnlcqMZc3_Cs9zI4=', start_index=14394)
Annotation(end_index=14406, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZ6sq1n_aV70xv4qhnGWdYnKkdOCSnqKKNWyQXanObV95FnRta6bvLIaJzQ1vb4L2BKU5oZ6dhSkG5rDHExf3q3qsVLPFQMheDBD9sm3FUPrD7vlhNsxjHVxRzruhqPoGBaJNagnH5rXopLru10ifwsLAFNcrWc3oTumGXOMZwvizsYqS20n8eh0jEY2EhJOfPNHYEjCAHLQ1enI86AEbd9aoM7D1SJOb8D7EjxnpK2keCzZrS1tZphGw0tfNrKlKQxhMB', start_index=14394)
Annotation(end_index=15052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf4dqqDchrQPhLBTwO3r2eMDN9bY5f3mFIo2Hbvu43L0auK1t5j43kT7hs2NgBK93sDPWv32SajKdwyGRZRh-aYy7VguNojdU6nLMslegfeFQpU9v2PUj_z90xGeJqRMi573Irf4zHiTNZgruff_g=', start_index=15043)
Annotation(end_index=15615, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdssBsLln_mbwwdgJWFhP_uiFnVEyiczydMn2ltABxu7Ej4_EztbnOeW--c5FASH88J4IdD6aV16fpABlBis5a8FIkwf49r4oCgJC52eoF9XqX6rn4wVjEWjDnhWCMSEaNf7HqydGKBaVbJF0kG9jPmclIz7jy4HUWvaXd4JqrKUsvLiXtDvbJlB9ZKSlk_MVcS85LVEFQMl3HXGSnTIQvgFnm5GA1Kl7MdpzA', start_index=15605)
Annotation(end_index=15924, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9rSBvMTqsre7BptrYyTP24mhgxqQWeKiCaN6V-laoCUC7_7oMZik4NX9WlE68p-oneO2iZVfG_4JpeNTnRx5U2E7n74GcZyiifJXQgGOfz3_Z0TuG40hNbqvVGFMAbJxFG-mm3y2sHCzoFXqAetMQc4DyiJTipH-4kNRtmMALnX3AgiCAtZHhzAqIwCOgg0yvar1l1clnhA==', start_index=15914)
Annotation(end_index=16279, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGphYPi05vBcAzndZLyFFXw7bk1GtdjJQUMqGVyvNJbFDRhB47A4nOt8Dz6eNtwTDqeqZgQmzCtb1-ER7hn9TcZ16MswgH1BALOqCsQaWQUJG2cWng7TEWZa0f485wcnnpA94rP_4bcQThnhUGOzxzwnRrFizeMXLepMMYL9hTuTLqZmc_G2VRVebvAPhfbNPN07uBFo-ojm-D6E1xZE8KnnlcqMZc3_Cs9zI4=', start_index=16267)
Annotation(end_index=16279, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZ6sq1n_aV70xv4qhnGWdYnKkdOCSnqKKNWyQXanObV95FnRta6bvLIaJzQ1vb4L2BKU5oZ6dhSkG5rDHExf3q3qsVLPFQMheDBD9sm3FUPrD7vlhNsxjHVxRzruhqPoGBaJNagnH5rXopLru10ifwsLAFNcrWc3oTumGXOMZwvizsYqS20n8eh0jEY2EhJOfPNHYEjCAHLQ1enI86AEbd9aoM7D1SJOb8D7EjxnpK2keCzZrS1tZphGw0tfNrKlKQxhMB', start_index=16267)
Annotation(end_index=16447, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCNxIwopnCSSWzyHGuBAU4mO3BTNpJ3ESmtbEcsMJDSyMPQAELSwcTgK1QSXXpu9kKHrSzdU1ZaKXMQKjhJ-Dg4igm1lXLhE2Ta-jtoo9FRgX8F-zMVUkWpClAlmAOacAqjDjWn72_wXIibyAb1pbMLT9Np0t-VEqGHoR0M1NS0ScyAmjwRYuyD9YUCu4HaLs3bC5pw6FEdGLUOQ==', start_index=16435)
Annotation(end_index=16447, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIE8XZTA9SnEprDnfQnkdL0deTsftQSvkvy-TcG4sUoBX5pxd5j1T_wb1T4s2j014YEyq0ePFD-AOKdKGN7mCzsZb_5vxPkUU_HTU17Uus5QgZ6SQe7P-606t5GYUodAV-c15Et_psw8Dp89cSnTZvLLbTZe4hIWCS6AevjTzPcq-cvm4j_EnJe-3oSz9A6leE2lBpUbWx-QnwFJLQ6oGOs7EiL7yfCBBGJsXTcoSrd_cV3d7e0zpcj8z4OE-oTxKh7o93K_MoOTy9FN_BJ6w=', start_index=16435)
Annotation(end_index=16633, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf4dqqDchrQPhLBTwO3r2eMDN9bY5f3mFIo2Hbvu43L0auK1t5j43kT7hs2NgBK93sDPWv32SajKdwyGRZRh-aYy7VguNojdU6nLMslegfeFQpU9v2PUj_z90xGeJqRMi573Irf4zHiTNZgruff_g=', start_index=16624)
Annotation(end_index=16695, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhZqdWFhu_V1dOcrhOfwRKszd6lAV98WM2Vgx9_CC4rA66zBdxB000yIUd1Jw75EC_LomqnaSvwnmNY-iOhjIjdTv62tcrnVLwm8P_coTec11fO6LXMK6SS_04PC_wUcWSHTvoxBB-7yLE_fvxK0b-GL35ZgjcJlB00OrB8mMeKXQPULbdSblF_kZeuD_BjtytFSCjuq5gkY4qWt64EeY9HL5sPqn1', start_index=16686)
Annotation(end_index=16809, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3G0eqKP-CSRsaecZk9-Ac5zNcM9uYRVS7IjAaD_Xd8nwn0Wq2y4ip_p9P7H-XnZ3WAgQw6aiOJ4gzHwZTV_q-V753eUuR0n97HoGwlomdN0d9WU8f', start_index=16800)
Annotation(end_index=16900, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4MWymDRbXEH0uK4_VGEgNWr6G0TwTdnmT9lsziR0kOkl9kc23WI5E7GRcesh-m7Eg23cfHCazkTuwbLNcAmLO2cGRLxbsdXxrCPVNUl47r_LBsl96oKZnXUIUkRcsN2DQW32ImZ7cp4qTE15GV5d2NBmGtdA3BQ0fdIZZPp-t_jSYQ8FXNlX8_P1mrkfLCodTiuP1brcNSJ9tkcpkYBLQ1Q==', start_index=16890)
Annotation(end_index=17016, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdssBsLln_mbwwdgJWFhP_uiFnVEyiczydMn2ltABxu7Ej4_EztbnOeW--c5FASH88J4IdD6aV16fpABlBis5a8FIkwf49r4oCgJC52eoF9XqX6rn4wVjEWjDnhWCMSEaNf7HqydGKBaVbJF0kG9jPmclIz7jy4HUWvaXd4JqrKUsvLiXtDvbJlB9ZKSlk_MVcS85LVEFQMl3HXGSnTIQvgFnm5GA1Kl7MdpzA', start_index=17006)
Annotation(end_index=17111, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9rSBvMTqsre7BptrYyTP24mhgxqQWeKiCaN6V-laoCUC7_7oMZik4NX9WlE68p-oneO2iZVfG_4JpeNTnRx5U2E7n74GcZyiifJXQgGOfz3_Z0TuG40hNbqvVGFMAbJxFG-mm3y2sHCzoFXqAetMQc4DyiJTipH-4kNRtmMALnX3AgiCAtZHhzAqIwCOgg0yvar1l1clnhA==', start_index=17101)

## Sources
