# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 6d729770 | **Time:** 352.18s | **Cost:** $1.52717
--------------------------------------------------------------------------------

# The Effect of Technical Intervention Parameters on the Spectral Radius of Learning Transfer Matrices in Cognitive Network Models

### Key Points
*   **Spectral Radius as a Stability Regulator:** In cognitive network models like Echo State Networks (ESN) and Fuzzy Cognitive Maps (FCM), the spectral radius ($\rho$) of the transfer (weight) matrix is the primary determinant of system stability, memory capacity, and convergence behavior. A spectral radius $\rho < 1$ generally ensures a stable equilibrium (Echo State Property), while $\rho > 1$ enables complex dynamics, long-term memory, or chaotic behavior.
*   **Interaction with Input Scaling:** In Reservoir Computing, technical interventions via **input scaling** parameters significantly alter the *effective* spectral radius. High input scaling drives neurons into saturation (the non-linear region of the activation function), effectively compressing the spectral radius and allowing the system to maintain stability even when the nominal weight matrix has $\rho > 1$.
*   **Expert Intervention in FCMs:** In Fuzzy Cognitive Maps, technical intervention often takes the form of hybrid learning algorithms where expert knowledge corrects data-driven weights. Research indicates that specific constraints on the learning rate and expert influence parameters are required to maintain the spectral radius below a critical threshold (often related to the Lipschitz constant of the activation function) to prevent unbounded oscillations.
*   **Topology and Connectivity:** The sparsity and topology of the network (e.g., small-world vs. random) are structural intervention parameters that indirectly manipulate the spectral radius. Adjusting connectivity density is a technical lever used to tune the system towards the "edge of chaos," where computational performance for complex tasks is often maximized.

---

## 1. Introduction

Cognitive network models, encompassing architectures such as Echo State Networks (ESN), Liquid State Machines (LSM), and Fuzzy Cognitive Maps (FCM), rely on the propagation of information through recurrently connected nodes. The mathematical backbone of this propagation is the **learning transfer matrix** (or simply the weight matrix), which dictates how the state of the network evolves over time. The **spectral radius** ($\rho$)—defined as the largest absolute value among the eigenvalues of this matrix—is the critical metric governing the dynamical regime of the network.

The query addresses the effect of **technical intervention parameters** on this spectral radius. In this context, "technical intervention" refers to the deliberate manipulation of hyperparameters (such as input scaling, leakage rates, and connection weights) or the imposition of structural constraints (such as sparsity or expert-guided corrections) during the design or training phases. These interventions are essential for navigating the **stability-plasticity dilemma**: the network must be stable enough to reliably represent information (fading memory) but plastic enough to react to inputs and retain history without decaying too quickly.

This report synthesizes research findings to explain how specific parameters influence the spectral radius and, consequently, the cognitive capabilities of the model. It distinguishes between two primary classes of models found in the literature: **Reservoir Computing (ESN)**, where the transfer matrix is often fixed and scaled globally, and **Fuzzy Cognitive Maps (FCM)**, where the matrix represents causal relationships and is subject to stability constraints during learning.

---

## 2. Spectral Radius in Reservoir Computing and Echo State Networks

Reservoir Computing (RC), particularly the Echo State Network (ESN), utilizes a large, fixed recurrent neural network (the reservoir) to project inputs into a high-dimensional space. The transfer matrix in this context is the reservoir weight matrix, $W_{res}$.

### 2.1 The Echo State Property and Spectral Radius Scaling
The fundamental theoretical requirement for an ESN is the **Echo State Property (ESP)**, which states that the effect of initial conditions should vanish over time, leaving the network state driven solely by the input history [cite: 1, 2].

*   **The Unitary Threshold:** A common heuristic for ensuring ESP is to scale the reservoir matrix $W_{res}$ such that its spectral radius $\rho(W_{res}) < 1$. If $\rho < 1$, the network is contractive, and information decays over time. If $\rho > 1$, the network can theoretically amplify disturbances, leading to unstable or chaotic dynamics [cite: 1, 2].
*   **Tuning for Timescales:** The spectral radius is a technical parameter used to tune the memory length of the network. A larger $\rho$ (closer to 1) implies longer time constants, meaning information persists in the network longer before decaying. This is crucial for tasks requiring long-term dependencies [cite: 2, 3]. Conversely, a smaller $\rho$ is suitable for tasks requiring rapid responses to immediate inputs.

### 2.2 The Interaction of Input Scaling and Spectral Radius
One of the most critical technical interventions in ESN design is **Input Scaling**. This parameter determines the magnitude of the input signal fed into the reservoir. Research highlights a complex, non-linear interaction between input scaling and the effective spectral radius.

*   **Non-linearity and Saturation:** The neurons in an ESN typically use a non-linear activation function, such as the hyperbolic tangent ($\tanh$). The $\tanh$ function is linear near zero but saturates (approaches -1 or 1) for large inputs.
*   **Dampening Effect:** When input scaling is increased, the total input to the neurons pushes them into the saturation region of the activation function. In this region, the derivative of the activation function is small (close to zero). This local reduction in gain effectively reduces the "local" spectral radius of the Jacobian of the system [cite: 1, 2].
*   **Violation of the $\rho < 1$ Rule:** Consequently, if the input scaling is large, the reservoir can maintain the Echo State Property even if the nominal spectral radius of the weight matrix is significantly larger than 1 (e.g., $\rho = 1.5$ or higher). The strong input forces the system into a stable regime despite the expansive nature of the recurrent weights [cite: 2, 4].
*   **Optimization:** Therefore, technical intervention requires joint optimization. If the input scaling is too small, the system operates linearly, and a $\rho > 1$ will cause instability. If input scaling is too large, the dynamics are truncated, and information is lost. Optimal performance is often found by balancing $\rho$ and input scaling to keep the system at the "edge of chaos" [cite: 1, 5].

### 2.3 Leakage Rate as an Intervention Parameter
The **leakage rate** ($\alpha$) is another parameter that modifies the effective time constant of the reservoir units. It determines how much of the previous state is retained versus how much is updated by the new input.

*   **Smoothing Dynamics:** A low leakage rate (close to 0) makes the neurons slow and integrative, effectively smoothing the dynamics. This can stabilize a network with a high spectral radius by slowing down the propagation of instabilities [cite: 5].
*   **Hyperparameter Interaction:** Recent studies on biologically instantiated networks found optimal performance with a specific combination of parameters: spectral radius $\rho = 0.9$, input scaling $\epsilon = 10^{-8}$, and leakage rate $\alpha = 1.0$ [cite: 5]. This suggests that when the spectral radius is high (near critical), the leakage rate and input scaling must be carefully adjusted to maximize memory capacity without crossing into chaotic regimes.

### 2.4 Intrinsic Plasticity and Spectral Radius
Advanced ESN implementations use **Intrinsic Plasticity (IP)**, a biological learning rule that adjusts the gain and bias of neurons to maximize information transmission (entropy).

*   **Effect on $\rho$:** Research indicates that applying IP learning rules tends to *increase* the spectral radius of the reservoir matrix [cite: 3]. This suggests that unsupervised adaptation mechanisms naturally push the network towards a more excitable, higher-radius state to maximize information processing capability.
*   **Compensation:** To counteract this increase and maintain stability, technical intervention is required to scale the effective spectral radius back down or adjust the bias inputs to reservoir nodes [cite: 3].

---

## 3. Fuzzy Cognitive Maps (FCM) and Stability Analysis

Fuzzy Cognitive Maps (FCMs) model complex systems as directed graphs where nodes are concepts and edges represent causal weights. Unlike ESNs, where the reservoir is often random, FCM weights are typically defined by experts or learned from data to represent specific causal truths.

### 3.1 Spectral Radius as a Stability Criterion
In FCMs, the state vector evolves iteratively. The stability of this inference process is paramount.

*   **Global Asymptotic Stability:** A fundamental result in FCM theory is that the system is globally asymptotically stable (converges to a unique fixed point regardless of the initial state) if the spectral radius of the weight matrix $W$ satisfies $\rho(W) < 1$ [cite: 6, 7].
*   **Multiple Attractors:** If $\rho(W) > 1$, the system may not converge to a unique point. Instead, it may exhibit multiple equilibria, limit cycles, or chaotic behavior. While often undesirable for simple decision-making, some researchers argue that $\rho > 1$ (e.g., $\rho = 3.25$) reflects the "dynamic diversity" of complex real-world systems, allowing for different outcomes based on different initial conditions (scenarios) [cite: 6, 7].

### 3.2 The Role of the Activation Function (Lipschitz Constant)
The stability condition is more accurately defined by the interaction between the weight matrix and the activation function used (usually sigmoid or tanh).

*   **Lipschitz Constraint:** A rigorous sufficient condition for stability is $\rho(W) < 1/L_f$, where $L_f$ is the Lipschitz constant of the activation function [cite: 8, 9].
*   **Technical Implication:** This provides a precise parameter for intervention. To stabilize an FCM, one can either reduce the weights (lowering $\rho(W)$) or choose an activation function with a smaller Lipschitz constant (making the curve flatter/less steep). This limits the "total causal feedback strength" within the system [cite: 8].

### 3.3 Expert Intervention and Hybrid Learning
Modern FCM approaches, such as the **Human-Centric Fuzzy Decision Support System (HCFDSS)**, integrate expert knowledge with data-driven learning. This involves a "technical intervention" where an expert adjusts the weights during the learning process.

*   **Intervention Parameters:** The learning update rule involves a learning rate ($\eta$) and an expert correction factor ($\alpha$).
*   **Stability Constraints:** To ensure that this intervention does not destabilize the learning process (i.e., cause the weights to diverge or oscillate), the parameters must satisfy specific constraints. Specifically, the sum of the learning rate and the expert influence factor must be bounded: $0 < \eta + \alpha < 1$ [cite: 8, 9].
*   **Effect on Spectral Radius:** This constraint ensures that the learning steps are controlled. The spectral radius condition ($\rho(W) < 1/L_f$) acts as a bound on the magnitude of the learned weights. The expert intervention helps guide the weights into a semantically meaningful region, while the spectral radius constraint prevents excessive amplification of inter-concept influences [cite: 8].

---

## 4. Structural and Topological Interventions

Beyond scalar parameters, technical interventions regarding the *structure* of the transfer matrix significantly impact the spectral radius.

### 4.1 Connectivity and Sparsity
The **connectivity** (percentage of non-zero weights) is a direct determinant of the spectral radius.

*   **Sparsity:** ESNs are typically sparsely connected (often < 1% connectivity). Increasing connectivity generally increases the spectral radius if the weights are not rescaled [cite: 1].
*   **Rescaling:** A standard technical intervention is to generate a random sparse matrix, compute its initial spectral radius, and then divide the entire matrix by this value to normalize $\rho$ to 1. It is then scaled by the desired target spectral radius [cite: 4]. This normalization step is crucial because the raw spectral radius grows with the square root of the network size ($N$) and the variance of the weights.

### 4.2 Network Topology (Small-World vs. Random)
The arrangement of connections (topology) influences memory and performance.

*   **Small-World Networks:** Research suggests that small-world topologies (characterized by high clustering and short path lengths) can perform well on synthetic data. The spectral radius of these structured matrices behaves differently than random matrices, often affecting the "criticality" of the network [cite: 10].
*   **Edge of Chaos:** The optimal performance for memory capacity is often found when the network is at the "edge of chaos," which corresponds to a spectral radius near 1 (critical state). Structural interventions that push the network toward this state (e.g., by adjusting rewiring probabilities in a Watts-Strogatz model) can optimize cognitive performance [cite: 5].

---

## 5. Applications in Cognitive Epidemic and Biological Models

The concept of spectral radius as a control parameter extends to other "cognitive" networks, such as those modeling disease spread or brain activity.

### 5.1 Epidemic Control as Spectral Radius Reduction
In cognitive epidemic models (where individuals change behavior based on infection risk), the **Basic Reproduction Number ($R_0$)** is mathematically equivalent to the spectral radius of the "next generation operator" (a transfer matrix of infection) [cite: 11, 12].

*   **Intervention Effect:** Non-pharmaceutical interventions (NPIs) like quarantine, social distancing, or restricting movement are technical interventions designed specifically to reduce the entries of this transfer matrix.
*   **Threshold Dynamics:** The goal of these interventions is to drive the spectral radius $R_0 < 1$. If this is achieved, the disease-free equilibrium becomes globally asymptotically stable [cite: 12, 13]. This parallels the stability condition in ESNs and FCMs.

### 5.2 Seizure Dynamics and Brain Networks
In biological cognitive networks, the spectral radius serves as a biomarker for excitability.

*   **Seizure Prediction:** Research on epilepsy shows that the spectral radius of the functional connectivity matrix increases prior to seizures. It is higher for seizures that generalize (spread globally) compared to those that remain focal [cite: 14, 15].
*   **Intervention Implication:** This suggests that clinical interventions (e.g., stimulation or medication) aim to lower the spectral radius of the brain's connectivity matrix to prevent the hypersynchronization associated with seizures.

---

## 6. Conclusion

The spectral radius of the learning transfer matrix is the fulcrum upon which the dynamics of cognitive network models balance. It is not a static property but a dynamic variable heavily influenced by technical intervention parameters.

1.  **In Reservoir Computing:** The spectral radius defines the timescale and memory of the system. However, its effect is strictly coupled with **input scaling**. High input scaling saturates neurons, compressing the effective spectral radius and allowing for stability even when the nominal $\rho > 1$. This interaction is the primary lever for tuning ESNs to specific tasks.
2.  **In Fuzzy Cognitive Maps:** The spectral radius is a rigorous bound for stability. Technical interventions, such as **expert-guided weight updates**, must adhere to constraints involving the spectral radius and the Lipschitz constant of the activation function ($\rho < 1/L_f$) to guarantee convergence to a decision state.
3.  **General Principle:** Across all domains—from machine learning to epidemiology—technical interventions act as regulators of the spectral radius. Whether through scaling weights, adjusting activation gains, or imposing quarantine, the objective is invariably to manipulate the spectral radius to achieve a desired dynamical regime: either a stable fixed point (convergence) or a critical state at the edge of chaos (maximum computational capacity).

### Table 1: Summary of Technical Intervention Effects on Spectral Radius

| Model Type | Intervention Parameter | Effect on Spectral Radius / Dynamics | Goal / Outcome |
| :--- | :--- | :--- | :--- |
| **ESN / RC** | **Weight Scaling** | Directly sets nominal $\rho$. | Tune memory length ($\rho \approx 1$ for long memory). |
| **ESN / RC** | **Input Scaling** | Reduces *effective* $\rho$ via saturation. | Stabilize high-$\rho$ networks; induce non-linearity. |
| **ESN / RC** | **Leakage Rate** | Modifies effective time constant. | Smooth dynamics; stabilize critical networks. |
| **FCM** | **Expert Weight ($\alpha$)** | Modifies weight matrix structure. | Incorporate domain knowledge; must satisfy $\rho < 1/L_f$. |
| **FCM** | **Activation Function** | Changes Lipschitz constant ($L_f$). | Determines the critical threshold for $\rho$ for stability. |
| **Epidemic** | **Quarantine/Distancing** | Reduces transmission rates in matrix. | Drive $R_0$ (spectral radius) $< 1$ for disease extinction. |

## References
[cite: 1, 2] Jaeger, H. (2001/2007). The echo state approach to analysing and training recurrent neural networks; Scholarpedia.
[cite: 3] Steil, J. J. (2007). Online reservoir adaptation by intrinsic plasticity.
[cite: 5] Xiao, S. (2024). Generative AI for predicting the multimodal brain connectivity evolution over time.
[cite: 6, 7] Harmati, I. A. (2021). Global stability of fuzzy cognitive maps.
[cite: 8, 9] Zakaria, A. (2025). A Human-Centric Fuzzy Decision Support System for Medical Diagnosis.
[cite: 14, 15] Adhikari, M. H., et al. (2021). Brain network dynamics codify heterogeneity in seizure propagation.
[cite: 4] Mantas, L. (2009). Practical Guide to applying Echo State Networks.
[cite: 11, 12] Liu, G., & Wang, H. (2024). On cognitive epidemic models: spatial segregation versus nonpharmaceutical interventions.

**Sources:**
1. [rug.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlkIrJeXRUYF7YuW4jl6Qrtco4GEoX7sU3bOvYj6WI9r0dztm10mjRIZRPfeURhMg2PwySGUq1VtFXwa0I7UuknKeRDPZkK2GywIq-5X8y32IkECrV0FeDIj_BeIdjxhZHaNmw_u2N9fmszXx4VA==)
2. [scholarpedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkWTJ0RtsJRWeRUDIKoKDVTzCMi3M9UT05ChQSIkR1jWWl9kLZQ86xJJwTW-LYrkPOMsqNERPJMu-v28UWCohA4njQRdPiFAi2Qj9-u9xtaySudhfALgBPSGMC38NjsvWqMsxYuR827ZIE1P0=)
3. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFM1N7ZpRRmW-ADpvBawevduTOkT8NS_EjiIm5l_aQGkjQNqIwmYwN4EjZVlW6UkgJRVLSVmhfcvxzYwK1-s-P2roup7UTUzPTZKqTdnObqVUy9hEXuZvgkkbkwCRleLswEYFxVdUd3)
4. [rug.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTSOhb-07e8xXpehgvfhiLvNWPS6hVq14pFvvellO0vE7vqp5a0Qxpw5QNrw6twWLLsTSJOZQYkLzhIht9XkXs7ZB4KW4ZE3mPkhkMXm6_gMy_lPUJbv3nmLa36DR5fyCFnD37NMgXBaeT)
5. [imperial.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpEbp4ikaAYQ6WlO2DQc41Quk-TMGsgN9IqivoZHNi0uZIH-Iu1LMGJwSNJR3hB2zx0YeR1fweTC0sfKz1r7X961WAoFicBKlJJlAB4XVn05y4D3Cp4yc3FMSIiQj0DlB592cNqxQVqncNWQfrQBjn3gUq4fpICbVFQarri47mJr950uahtOiHM3TsFDjhrqMVOoUllk7NFLyTrzhkWzR93RhzqGLtEY9le3UImZykHfY5wr1nXddUd3FMemQWWV1VIouTEtTor2uKv6Heplql0wqplcm2TbhZkPbaXqmLZviiNOnsy3DK_s1Fs5RN-Z5aEnKleAqs2TibCj_XtskqHY3VJlOGhmThF0VKNUPCbQuU0Y8A_Kk5j0i_9s0=)
6. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFRdSklKyEwjA9YvbcYJgT-TNkNVqwT0WS_RAN6csgDNQhBIk_653wILBMA6jJFTagE4X96LhqnIsu84QrHQKfQW8tQtQtPtWJWfyGRzbwkfJJnhsVlrwvqjyTuFWGW1CVbz7Z7VS8NA==)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFus3aFniFsSZZ33M-2fHG_91EGo3vDrJRqGYjT74KdImQdl1ZT0DxHtdpmo9BkRFTOkFYgLaE_zzr66G6qXV79U9jo9PsgX7Mg24QdR_htjadltU2QgT5BIl7ka0f1lPSnizqhMkhPh-dqHrJFCg4CaVVT6rVZ-G6q0O6DgYnncIO4DknSJzwRFCk4CiWWAbXB)
8. [researchsquare.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVSW5GLaBE0A_GxBd6BJMfNMyKDuu06TWpUc6Dl5B7uCiilBOuQWnAZRdrFAaqie0-_Ma531p3a-F4kxIO7XqODSWmW4CotQrPe1r54lufMNX3BiQTwMkF6sGxHaWi2-QTVF8b-QzuSgFmCZkjojKH4BQ1MLwMb8AP0jLpGcNrjmNZGi0pocJ6jFQlbL6iNwKaPWW4ighfDFBFb3ZHvYE=)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDXSj7_uN3ruQXJHhxpgd00GdAOUdhWskVZVaXokwNId_vbPOXiq860E8BKkaD6Hwd7wxE610SG8vc1b7kmKdzaiSKltjGMskojo2qW9jNUEVpPu6kY4irfSqOe8V0K0Nu8URy-s_YE5WpkeozcZJyWwZWJm7Gt6Ekae1D_IYY7E4mZYTGV-cbbIg77FyNdIZAfQBXSjL0_l3wSiYMqA==)
10. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxKkLhQ_fAx2yNpFh2LUejKUyh9mA4ADSS-ThrBtHpPziu-6_2gWLoKUyMG-g6I1vtDzc1-Jb7_tzqRWNvOMYIM47TeyqcK5ffiHosYRBbAsGpUquuDp0Zug==)
11. [ualberta.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLjLwNki6K48ItivLv0_BA7nDce0Pph-LZ1B6Cd7JZi2jUztfNFc8_r80aK57v_rWOZz2XYdd8CvWLgMWPi5b988dAgWOEX1zsQgrqWvWU7Ew9r831WINxs_6somQavOyXcnFhQGGOKpLpK6dd)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFujXRlezxqece9nrvN8vC-CSesMmXQyT6iO2y8xdWPGrdWbnjpqeWhFWZqelO-V_s-yoko-YPZMentami5U0vusRS7p-Z028yl9yelz1hgWo8rzXNFwVJs6l6SWsdFkF3MtLpxsMU2HZFqQnWPssQ8tAUiEmdAO2aa2fp646Q6TAnPV2LzCiph3OSt73SNWaPb7nKEdFL2P7Z_xwf9m_XRJqAC3njMI6DPQupIVqcad_rZQip1_lgbc_FHN4NXymgIEB7ks4Ii8Ai9)
13. [siam.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAVWvxOcPeYXZvhqdgYxTuarn5Ba5zZmDRh24BTm8o3YlwwKVtKvNlJT7auaMQldU30-3L8bZ-j-78mh---6XSUK62WkWIfJCSrpQhjNORGFp4kPILpBMngE8Dgm1CYh1hNEY=)
14. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe2y_wS0KuOAQE77V4wQQHbSNkf02DxiLXLjQFrap6p84y-z5W2-buLaz2-C1e5Gi4Cdegb5iuc7BJ1THqe9Rbvt9grCmP6Ug2qaf-Z17oBliTAFiOSEzATTgNTXQeWJK2PmaM59JY-rBQQFFI942n5LO4Ag==)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrP2VWH3bHQRllFhNFSOcWF361-Xu4SW-pIERH3zOF9UWOg6pA2lt-ZnjKFFdGtVNcqOTz9-ZKtonoVkgrWDeyOEfo081HIgIQJCGDdQY5DwEC-Vz1X_QrWlMgq_p9Bu9dsSoXcd-FyJXMFPSGXQtEnwt3lI0uBr5IKUNAZNRElv1svrPXYqbe4JyDq8FBzkgUQ1LnZKi2FMW2z2QevnGFiRY49PjsjDK5u8Q=)


## Annotations
Annotation(end_index=4240, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkWTJ0RtsJRWeRUDIKoKDVTzCMi3M9UT05ChQSIkR1jWWl9kLZQ86xJJwTW-LYrkPOMsqNERPJMu-v28UWCohA4njQRdPiFAi2Qj9-u9xtaySudhfALgBPSGMC38NjsvWqMsxYuR827ZIE1P0=', start_index=4228)
Annotation(end_index=4240, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlkIrJeXRUYF7YuW4jl6Qrtco4GEoX7sU3bOvYj6WI9r0dztm10mjRIZRPfeURhMg2PwySGUq1VtFXwa0I7UuknKeRDPZkK2GywIq-5X8y32IkECrV0FeDIj_BeIdjxhZHaNmw_u2N9fmszXx4VA==', start_index=4228)
Annotation(end_index=4600, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkWTJ0RtsJRWeRUDIKoKDVTzCMi3M9UT05ChQSIkR1jWWl9kLZQ86xJJwTW-LYrkPOMsqNERPJMu-v28UWCohA4njQRdPiFAi2Qj9-u9xtaySudhfALgBPSGMC38NjsvWqMsxYuR827ZIE1P0=', start_index=4588)
Annotation(end_index=4600, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlkIrJeXRUYF7YuW4jl6Qrtco4GEoX7sU3bOvYj6WI9r0dztm10mjRIZRPfeURhMg2PwySGUq1VtFXwa0I7UuknKeRDPZkK2GywIq-5X8y32IkECrV0FeDIj_BeIdjxhZHaNmw_u2N9fmszXx4VA==', start_index=4588)
Annotation(end_index=4925, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkWTJ0RtsJRWeRUDIKoKDVTzCMi3M9UT05ChQSIkR1jWWl9kLZQ86xJJwTW-LYrkPOMsqNERPJMu-v28UWCohA4njQRdPiFAi2Qj9-u9xtaySudhfALgBPSGMC38NjsvWqMsxYuR827ZIE1P0=', start_index=4913)
Annotation(end_index=4925, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFM1N7ZpRRmW-ADpvBawevduTOkT8NS_EjiIm5l_aQGkjQNqIwmYwN4EjZVlW6UkgJRVLSVmhfcvxzYwK1-s-P2roup7UTUzPTZKqTdnObqVUy9hEXuZvgkkbkwCRleLswEYFxVdUd3', start_index=4913)
Annotation(end_index=5972, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkWTJ0RtsJRWeRUDIKoKDVTzCMi3M9UT05ChQSIkR1jWWl9kLZQ86xJJwTW-LYrkPOMsqNERPJMu-v28UWCohA4njQRdPiFAi2Qj9-u9xtaySudhfALgBPSGMC38NjsvWqMsxYuR827ZIE1P0=', start_index=5960)
Annotation(end_index=5972, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlkIrJeXRUYF7YuW4jl6Qrtco4GEoX7sU3bOvYj6WI9r0dztm10mjRIZRPfeURhMg2PwySGUq1VtFXwa0I7UuknKeRDPZkK2GywIq-5X8y32IkECrV0FeDIj_BeIdjxhZHaNmw_u2N9fmszXx4VA==', start_index=5960)
Annotation(end_index=6354, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkWTJ0RtsJRWeRUDIKoKDVTzCMi3M9UT05ChQSIkR1jWWl9kLZQ86xJJwTW-LYrkPOMsqNERPJMu-v28UWCohA4njQRdPiFAi2Qj9-u9xtaySudhfALgBPSGMC38NjsvWqMsxYuR827ZIE1P0=', start_index=6342)
Annotation(end_index=6354, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTSOhb-07e8xXpehgvfhiLvNWPS6hVq14pFvvellO0vE7vqp5a0Qxpw5QNrw6twWLLsTSJOZQYkLzhIht9XkXs7ZB4KW4ZE3mPkhkMXm6_gMy_lPUJbv3nmLa36DR5fyCFnD37NMgXBaeT', start_index=6342)
Annotation(end_index=6758, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpEbp4ikaAYQ6WlO2DQc41Quk-TMGsgN9IqivoZHNi0uZIH-Iu1LMGJwSNJR3hB2zx0YeR1fweTC0sfKz1r7X961WAoFicBKlJJlAB4XVn05y4D3Cp4yc3FMSIiQj0DlB592cNqxQVqncNWQfrQBjn3gUq4fpICbVFQarri47mJr950uahtOiHM3TsFDjhrqMVOoUllk7NFLyTrzhkWzR93RhzqGLtEY9le3UImZykHfY5wr1nXddUd3FMemQWWV1VIouTEtTor2uKv6Heplql0wqplcm2TbhZkPbaXqmLZviiNOnsy3DK_s1Fs5RN-Z5aEnKleAqs2TibCj_XtskqHY3VJlOGhmThF0VKNUPCbQuU0Y8A_Kk5j0i_9s0=', start_index=6746)
Annotation(end_index=6758, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlkIrJeXRUYF7YuW4jl6Qrtco4GEoX7sU3bOvYj6WI9r0dztm10mjRIZRPfeURhMg2PwySGUq1VtFXwa0I7UuknKeRDPZkK2GywIq-5X8y32IkECrV0FeDIj_BeIdjxhZHaNmw_u2N9fmszXx4VA==', start_index=6746)
Annotation(end_index=7284, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpEbp4ikaAYQ6WlO2DQc41Quk-TMGsgN9IqivoZHNi0uZIH-Iu1LMGJwSNJR3hB2zx0YeR1fweTC0sfKz1r7X961WAoFicBKlJJlAB4XVn05y4D3Cp4yc3FMSIiQj0DlB592cNqxQVqncNWQfrQBjn3gUq4fpICbVFQarri47mJr950uahtOiHM3TsFDjhrqMVOoUllk7NFLyTrzhkWzR93RhzqGLtEY9le3UImZykHfY5wr1nXddUd3FMemQWWV1VIouTEtTor2uKv6Heplql0wqplcm2TbhZkPbaXqmLZviiNOnsy3DK_s1Fs5RN-Z5aEnKleAqs2TibCj_XtskqHY3VJlOGhmThF0VKNUPCbQuU0Y8A_Kk5j0i_9s0=', start_index=7275)
Annotation(end_index=7551, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpEbp4ikaAYQ6WlO2DQc41Quk-TMGsgN9IqivoZHNi0uZIH-Iu1LMGJwSNJR3hB2zx0YeR1fweTC0sfKz1r7X961WAoFicBKlJJlAB4XVn05y4D3Cp4yc3FMSIiQj0DlB592cNqxQVqncNWQfrQBjn3gUq4fpICbVFQarri47mJr950uahtOiHM3TsFDjhrqMVOoUllk7NFLyTrzhkWzR93RhzqGLtEY9le3UImZykHfY5wr1nXddUd3FMemQWWV1VIouTEtTor2uKv6Heplql0wqplcm2TbhZkPbaXqmLZviiNOnsy3DK_s1Fs5RN-Z5aEnKleAqs2TibCj_XtskqHY3VJlOGhmThF0VKNUPCbQuU0Y8A_Kk5j0i_9s0=', start_index=7542)
Annotation(end_index=8133, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFM1N7ZpRRmW-ADpvBawevduTOkT8NS_EjiIm5l_aQGkjQNqIwmYwN4EjZVlW6UkgJRVLSVmhfcvxzYwK1-s-P2roup7UTUzPTZKqTdnObqVUy9hEXuZvgkkbkwCRleLswEYFxVdUd3', start_index=8124)
Annotation(end_index=8521, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFM1N7ZpRRmW-ADpvBawevduTOkT8NS_EjiIm5l_aQGkjQNqIwmYwN4EjZVlW6UkgJRVLSVmhfcvxzYwK1-s-P2roup7UTUzPTZKqTdnObqVUy9hEXuZvgkkbkwCRleLswEYFxVdUd3', start_index=8512)
Annotation(end_index=9298, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFRdSklKyEwjA9YvbcYJgT-TNkNVqwT0WS_RAN6csgDNQhBIk_653wILBMA6jJFTagE4X96LhqnIsu84QrHQKfQW8tQtQtPtWJWfyGRzbwkfJJnhsVlrwvqjyTuFWGW1CVbz7Z7VS8NA==', start_index=9286)
Annotation(end_index=9298, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFus3aFniFsSZZ33M-2fHG_91EGo3vDrJRqGYjT74KdImQdl1ZT0DxHtdpmo9BkRFTOkFYgLaE_zzr66G6qXV79U9jo9PsgX7Mg24QdR_htjadltU2QgT5BIl7ka0f1lPSnizqhMkhPh-dqHrJFCg4CaVVT6rVZ-G6q0O6DgYnncIO4DknSJzwRFCk4CiWWAbXB', start_index=9286)
Annotation(end_index=9745, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFRdSklKyEwjA9YvbcYJgT-TNkNVqwT0WS_RAN6csgDNQhBIk_653wILBMA6jJFTagE4X96LhqnIsu84QrHQKfQW8tQtQtPtWJWfyGRzbwkfJJnhsVlrwvqjyTuFWGW1CVbz7Z7VS8NA==', start_index=9733)
Annotation(end_index=9745, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFus3aFniFsSZZ33M-2fHG_91EGo3vDrJRqGYjT74KdImQdl1ZT0DxHtdpmo9BkRFTOkFYgLaE_zzr66G6qXV79U9jo9PsgX7Mg24QdR_htjadltU2QgT5BIl7ka0f1lPSnizqhMkhPh-dqHrJFCg4CaVVT6rVZ-G6q0O6DgYnncIO4DknSJzwRFCk4CiWWAbXB', start_index=9733)
Annotation(end_index=10145, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDXSj7_uN3ruQXJHhxpgd00GdAOUdhWskVZVaXokwNId_vbPOXiq860E8BKkaD6Hwd7wxE610SG8vc1b7kmKdzaiSKltjGMskojo2qW9jNUEVpPu6kY4irfSqOe8V0K0Nu8URy-s_YE5WpkeozcZJyWwZWJm7Gt6Ekae1D_IYY7E4mZYTGV-cbbIg77FyNdIZAfQBXSjL0_l3wSiYMqA==', start_index=10133)
Annotation(end_index=10145, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVSW5GLaBE0A_GxBd6BJMfNMyKDuu06TWpUc6Dl5B7uCiilBOuQWnAZRdrFAaqie0-_Ma531p3a-F4kxIO7XqODSWmW4CotQrPe1r54lufMNX3BiQTwMkF6sGxHaWi2-QTVF8b-QzuSgFmCZkjojKH4BQ1MLwMb8AP0jLpGcNrjmNZGi0pocJ6jFQlbL6iNwKaPWW4ighfDFBFb3ZHvYE=', start_index=10133)
Annotation(end_index=10488, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVSW5GLaBE0A_GxBd6BJMfNMyKDuu06TWpUc6Dl5B7uCiilBOuQWnAZRdrFAaqie0-_Ma531p3a-F4kxIO7XqODSWmW4CotQrPe1r54lufMNX3BiQTwMkF6sGxHaWi2-QTVF8b-QzuSgFmCZkjojKH4BQ1MLwMb8AP0jLpGcNrjmNZGi0pocJ6jFQlbL6iNwKaPWW4ighfDFBFb3ZHvYE=', start_index=10479)
Annotation(end_index=11264, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDXSj7_uN3ruQXJHhxpgd00GdAOUdhWskVZVaXokwNId_vbPOXiq860E8BKkaD6Hwd7wxE610SG8vc1b7kmKdzaiSKltjGMskojo2qW9jNUEVpPu6kY4irfSqOe8V0K0Nu8URy-s_YE5WpkeozcZJyWwZWJm7Gt6Ekae1D_IYY7E4mZYTGV-cbbIg77FyNdIZAfQBXSjL0_l3wSiYMqA==', start_index=11252)
Annotation(end_index=11264, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVSW5GLaBE0A_GxBd6BJMfNMyKDuu06TWpUc6Dl5B7uCiilBOuQWnAZRdrFAaqie0-_Ma531p3a-F4kxIO7XqODSWmW4CotQrPe1r54lufMNX3BiQTwMkF6sGxHaWi2-QTVF8b-QzuSgFmCZkjojKH4BQ1MLwMb8AP0jLpGcNrjmNZGi0pocJ6jFQlbL6iNwKaPWW4ighfDFBFb3ZHvYE=', start_index=11252)
Annotation(end_index=11666, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVSW5GLaBE0A_GxBd6BJMfNMyKDuu06TWpUc6Dl5B7uCiilBOuQWnAZRdrFAaqie0-_Ma531p3a-F4kxIO7XqODSWmW4CotQrPe1r54lufMNX3BiQTwMkF6sGxHaWi2-QTVF8b-QzuSgFmCZkjojKH4BQ1MLwMb8AP0jLpGcNrjmNZGi0pocJ6jFQlbL6iNwKaPWW4ighfDFBFb3ZHvYE=', start_index=11657)
Annotation(end_index=12189, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlkIrJeXRUYF7YuW4jl6Qrtco4GEoX7sU3bOvYj6WI9r0dztm10mjRIZRPfeURhMg2PwySGUq1VtFXwa0I7UuknKeRDPZkK2GywIq-5X8y32IkECrV0FeDIj_BeIdjxhZHaNmw_u2N9fmszXx4VA==', start_index=12180)
Annotation(end_index=12459, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTSOhb-07e8xXpehgvfhiLvNWPS6hVq14pFvvellO0vE7vqp5a0Qxpw5QNrw6twWLLsTSJOZQYkLzhIht9XkXs7ZB4KW4ZE3mPkhkMXm6_gMy_lPUJbv3nmLa36DR5fyCFnD37NMgXBaeT', start_index=12450)
Annotation(end_index=13063, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxKkLhQ_fAx2yNpFh2LUejKUyh9mA4ADSS-ThrBtHpPziu-6_2gWLoKUyMG-g6I1vtDzc1-Jb7_tzqRWNvOMYIM47TeyqcK5ffiHosYRBbAsGpUquuDp0Zug==', start_index=13053)
Annotation(end_index=13434, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpEbp4ikaAYQ6WlO2DQc41Quk-TMGsgN9IqivoZHNi0uZIH-Iu1LMGJwSNJR3hB2zx0YeR1fweTC0sfKz1r7X961WAoFicBKlJJlAB4XVn05y4D3Cp4yc3FMSIiQj0DlB592cNqxQVqncNWQfrQBjn3gUq4fpICbVFQarri47mJr950uahtOiHM3TsFDjhrqMVOoUllk7NFLyTrzhkWzR93RhzqGLtEY9le3UImZykHfY5wr1nXddUd3FMemQWWV1VIouTEtTor2uKv6Heplql0wqplcm2TbhZkPbaXqmLZviiNOnsy3DK_s1Fs5RN-Z5aEnKleAqs2TibCj_XtskqHY3VJlOGhmThF0VKNUPCbQuU0Y8A_Kk5j0i_9s0=', start_index=13425)
Annotation(end_index=13976, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFujXRlezxqece9nrvN8vC-CSesMmXQyT6iO2y8xdWPGrdWbnjpqeWhFWZqelO-V_s-yoko-YPZMentami5U0vusRS7p-Z028yl9yelz1hgWo8rzXNFwVJs6l6SWsdFkF3MtLpxsMU2HZFqQnWPssQ8tAUiEmdAO2aa2fp646Q6TAnPV2LzCiph3OSt73SNWaPb7nKEdFL2P7Z_xwf9m_XRJqAC3njMI6DPQupIVqcad_rZQip1_lgbc_FHN4NXymgIEB7ks4Ii8Ai9', start_index=13962)
Annotation(end_index=13976, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLjLwNki6K48ItivLv0_BA7nDce0Pph-LZ1B6Cd7JZi2jUztfNFc8_r80aK57v_rWOZz2XYdd8CvWLgMWPi5b988dAgWOEX1zsQgrqWvWU7Ew9r831WINxs_6somQavOyXcnFhQGGOKpLpK6dd', start_index=13962)
Annotation(end_index=14411, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAVWvxOcPeYXZvhqdgYxTuarn5Ba5zZmDRh24BTm8o3YlwwKVtKvNlJT7auaMQldU30-3L8bZ-j-78mh---6XSUK62WkWIfJCSrpQhjNORGFp4kPILpBMngE8Dgm1CYh1hNEY=', start_index=14397)
Annotation(end_index=14411, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFujXRlezxqece9nrvN8vC-CSesMmXQyT6iO2y8xdWPGrdWbnjpqeWhFWZqelO-V_s-yoko-YPZMentami5U0vusRS7p-Z028yl9yelz1hgWo8rzXNFwVJs6l6SWsdFkF3MtLpxsMU2HZFqQnWPssQ8tAUiEmdAO2aa2fp646Q6TAnPV2LzCiph3OSt73SNWaPb7nKEdFL2P7Z_xwf9m_XRJqAC3njMI6DPQupIVqcad_rZQip1_lgbc_FHN4NXymgIEB7ks4Ii8Ai9', start_index=14397)
Annotation(end_index=14867, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrP2VWH3bHQRllFhNFSOcWF361-Xu4SW-pIERH3zOF9UWOg6pA2lt-ZnjKFFdGtVNcqOTz9-ZKtonoVkgrWDeyOEfo081HIgIQJCGDdQY5DwEC-Vz1X_QrWlMgq_p9Bu9dsSoXcd-FyJXMFPSGXQtEnwt3lI0uBr5IKUNAZNRElv1svrPXYqbe4JyDq8FBzkgUQ1LnZKi2FMW2z2QevnGFiRY49PjsjDK5u8Q=', start_index=14853)
Annotation(end_index=14867, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe2y_wS0KuOAQE77V4wQQHbSNkf02DxiLXLjQFrap6p84y-z5W2-buLaz2-C1e5Gi4Cdegb5iuc7BJ1THqe9Rbvt9grCmP6Ug2qaf-Z17oBliTAFiOSEzATTgNTXQeWJK2PmaM59JY-rBQQFFI942n5LO4Ag==', start_index=14853)
Annotation(end_index=17573, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkWTJ0RtsJRWeRUDIKoKDVTzCMi3M9UT05ChQSIkR1jWWl9kLZQ86xJJwTW-LYrkPOMsqNERPJMu-v28UWCohA4njQRdPiFAi2Qj9-u9xtaySudhfALgBPSGMC38NjsvWqMsxYuR827ZIE1P0=', start_index=17561)
Annotation(end_index=17573, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlkIrJeXRUYF7YuW4jl6Qrtco4GEoX7sU3bOvYj6WI9r0dztm10mjRIZRPfeURhMg2PwySGUq1VtFXwa0I7UuknKeRDPZkK2GywIq-5X8y32IkECrV0FeDIj_BeIdjxhZHaNmw_u2N9fmszXx4VA==', start_index=17561)
Annotation(end_index=17698, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFM1N7ZpRRmW-ADpvBawevduTOkT8NS_EjiIm5l_aQGkjQNqIwmYwN4EjZVlW6UkgJRVLSVmhfcvxzYwK1-s-P2roup7UTUzPTZKqTdnObqVUy9hEXuZvgkkbkwCRleLswEYFxVdUd3', start_index=17689)
Annotation(end_index=17782, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpEbp4ikaAYQ6WlO2DQc41Quk-TMGsgN9IqivoZHNi0uZIH-Iu1LMGJwSNJR3hB2zx0YeR1fweTC0sfKz1r7X961WAoFicBKlJJlAB4XVn05y4D3Cp4yc3FMSIiQj0DlB592cNqxQVqncNWQfrQBjn3gUq4fpICbVFQarri47mJr950uahtOiHM3TsFDjhrqMVOoUllk7NFLyTrzhkWzR93RhzqGLtEY9le3UImZykHfY5wr1nXddUd3FMemQWWV1VIouTEtTor2uKv6Heplql0wqplcm2TbhZkPbaXqmLZviiNOnsy3DK_s1Fs5RN-Z5aEnKleAqs2TibCj_XtskqHY3VJlOGhmThF0VKNUPCbQuU0Y8A_Kk5j0i_9s0=', start_index=17773)
Annotation(end_index=17896, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFRdSklKyEwjA9YvbcYJgT-TNkNVqwT0WS_RAN6csgDNQhBIk_653wILBMA6jJFTagE4X96LhqnIsu84QrHQKfQW8tQtQtPtWJWfyGRzbwkfJJnhsVlrwvqjyTuFWGW1CVbz7Z7VS8NA==', start_index=17884)
Annotation(end_index=17896, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFus3aFniFsSZZ33M-2fHG_91EGo3vDrJRqGYjT74KdImQdl1ZT0DxHtdpmo9BkRFTOkFYgLaE_zzr66G6qXV79U9jo9PsgX7Mg24QdR_htjadltU2QgT5BIl7ka0f1lPSnizqhMkhPh-dqHrJFCg4CaVVT6rVZ-G6q0O6DgYnncIO4DknSJzwRFCk4CiWWAbXB', start_index=17884)
Annotation(end_index=17974, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDXSj7_uN3ruQXJHhxpgd00GdAOUdhWskVZVaXokwNId_vbPOXiq860E8BKkaD6Hwd7wxE610SG8vc1b7kmKdzaiSKltjGMskojo2qW9jNUEVpPu6kY4irfSqOe8V0K0Nu8URy-s_YE5WpkeozcZJyWwZWJm7Gt6Ekae1D_IYY7E4mZYTGV-cbbIg77FyNdIZAfQBXSjL0_l3wSiYMqA==', start_index=17962)
Annotation(end_index=17974, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVSW5GLaBE0A_GxBd6BJMfNMyKDuu06TWpUc6Dl5B7uCiilBOuQWnAZRdrFAaqie0-_Ma531p3a-F4kxIO7XqODSWmW4CotQrPe1r54lufMNX3BiQTwMkF6sGxHaWi2-QTVF8b-QzuSgFmCZkjojKH4BQ1MLwMb8AP0jLpGcNrjmNZGi0pocJ6jFQlbL6iNwKaPWW4ighfDFBFb3ZHvYE=', start_index=17962)
Annotation(end_index=18078, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrP2VWH3bHQRllFhNFSOcWF361-Xu4SW-pIERH3zOF9UWOg6pA2lt-ZnjKFFdGtVNcqOTz9-ZKtonoVkgrWDeyOEfo081HIgIQJCGDdQY5DwEC-Vz1X_QrWlMgq_p9Bu9dsSoXcd-FyJXMFPSGXQtEnwt3lI0uBr5IKUNAZNRElv1svrPXYqbe4JyDq8FBzkgUQ1LnZKi2FMW2z2QevnGFiRY49PjsjDK5u8Q=', start_index=18064)
Annotation(end_index=18078, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe2y_wS0KuOAQE77V4wQQHbSNkf02DxiLXLjQFrap6p84y-z5W2-buLaz2-C1e5Gi4Cdegb5iuc7BJ1THqe9Rbvt9grCmP6Ug2qaf-Z17oBliTAFiOSEzATTgNTXQeWJK2PmaM59JY-rBQQFFI942n5LO4Ag==', start_index=18064)
Annotation(end_index=18188, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTSOhb-07e8xXpehgvfhiLvNWPS6hVq14pFvvellO0vE7vqp5a0Qxpw5QNrw6twWLLsTSJOZQYkLzhIht9XkXs7ZB4KW4ZE3mPkhkMXm6_gMy_lPUJbv3nmLa36DR5fyCFnD37NMgXBaeT', start_index=18179)
Annotation(end_index=18271, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFujXRlezxqece9nrvN8vC-CSesMmXQyT6iO2y8xdWPGrdWbnjpqeWhFWZqelO-V_s-yoko-YPZMentami5U0vusRS7p-Z028yl9yelz1hgWo8rzXNFwVJs6l6SWsdFkF3MtLpxsMU2HZFqQnWPssQ8tAUiEmdAO2aa2fp646Q6TAnPV2LzCiph3OSt73SNWaPb7nKEdFL2P7Z_xwf9m_XRJqAC3njMI6DPQupIVqcad_rZQip1_lgbc_FHN4NXymgIEB7ks4Ii8Ai9', start_index=18257)
Annotation(end_index=18271, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLjLwNki6K48ItivLv0_BA7nDce0Pph-LZ1B6Cd7JZi2jUztfNFc8_r80aK57v_rWOZz2XYdd8CvWLgMWPi5b988dAgWOEX1zsQgrqWvWU7Ew9r831WINxs_6somQavOyXcnFhQGGOKpLpK6dd', start_index=18257)

## Sources
