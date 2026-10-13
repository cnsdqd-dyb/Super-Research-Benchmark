# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** f0bf88e2 | **Time:** 787.12s | **Cost:** $0.77842
--------------------------------------------------------------------------------

# Resource Scheduling Strategies for Balancing Latency, Energy, and Reliability in Edge Computing

**Key Points**
*   **The Core Conflict:** Edge computing faces a fundamental trade-off where minimizing latency (via high-performance computing or rapid offloading) typically spikes energy consumption, while aggressive energy-saving measures (like dynamic voltage scaling or queuing) jeopardize real-time processing guarantees.
*   **The Dominant Strategy:** **Lyapunov Optimization (LO)** emerges as the primary theoretical framework for resolving this conflict. It transforms complex, long-term constraints (like battery life and queue stability) into manageable, real-time optimization problems.
*   **Mechanism of Action:** LO utilizes a **Drift-Plus-Penalty** algorithm, which dynamically balances a "penalty" (energy consumption) against "queue drift" (latency risk). A control parameter, often denoted as $V$, allows system architects to tune the precise trade-off between energy efficiency and delay minimization.
*   **Ensuring Reliability:** While traditional LO guarantees average stability, **Conformal Lyapunov Optimization (CLO)** has been developed to provide deterministic, worst-case reliability guarantees, essential for mission-critical applications.
*   **Hybrid Implementations:** To handle the computational complexity of these decisions in real-time, modern strategies combine Lyapunov theory with **Deep Reinforcement Learning (DRL)** (e.g., LyDROO, LyA3C) or meta-heuristics like **Particle Swarm Optimization (LPSO)**. These hybrids allow the system to learn optimal policies without perfect prior knowledge of network conditions.

## 1. Introduction

The proliferation of the Internet of Things (IoT) and the advent of 5G networks have necessitated a paradigm shift from centralized cloud computing to **Edge Computing**. By processing data closer to the source, edge computing significantly reduces transmission latency and bandwidth usage. However, this distributed architecture introduces a complex resource scheduling problem: how to allocate limited computational resources to stochastic task arrivals while balancing conflicting objectives [cite: 1, 2].

The primary conflict lies between **latency sensitivity** and **energy efficiency**. Real-time applications, such as autonomous driving, industrial automation, and augmented reality, require strict latency guarantees. Meeting these requirements often necessitates operating processors at high frequencies or offloading tasks to powerful, energy-hungry servers. Conversely, edge nodes (often battery-powered or energy-constrained) must maximize **long-term reliability** and operational lifespan by conserving energy, often at the cost of processing speed [cite: 3, 4].

This report details the resource scheduling strategies designed to resolve this conflict. The analysis identifies **Lyapunov Optimization** as the foundational mathematical strategy, supported by advanced integrations with Deep Reinforcement Learning (DRL) and meta-heuristic algorithms to ensure both real-time responsiveness and long-term system stability.

## 2. Theoretical Foundations of the Conflict

To understand the scheduling strategies, one must first formalize the conflict between latency, energy, and reliability within the edge computing environment.

### 2.1 The Latency Model
In edge computing, the total latency ($T_{total}$) for a task is typically modeled as the sum of computation latency and communication latency. For a task $s_i$ with data volume $d_i$ and computational requirement $c_i$ (in CPU cycles), executed on node $n_j$:

\[ T_i = T_i^{comp} + T_i^{comm} = \frac{c_i}{f_j} + \frac{d_i}{b_j} \]

Where $f_j$ is the CPU frequency of the node and $b_j$ is the available bandwidth [cite: 3]. Minimizing $T_i$ requires maximizing $f_j$ (increasing energy) or maximizing $b_j$ (requiring high transmission power). Furthermore, in multi-stage workflows modeled by Directed Acyclic Graphs (DAGs), dependencies between subtasks introduce waiting times that further complicate latency minimization [cite: 3].

### 2.2 The Energy Consumption Model
Energy efficiency is critical for the sustainability of edge nodes. The energy consumption model typically includes computation and communication components:

\[ E_i = E_i^{comp} + E_i^{comm} = \kappa_j f_j^2 c_i + P_{tx,j} \frac{d_i}{b_j} \]

Here, $\kappa_j$ is an effective switched capacitance coefficient. The term $f_j^2$ indicates that dynamic power consumption scales quadratically with CPU frequency [cite: 3]. This creates a direct conflict: increasing frequency $f_j$ to reduce computation latency ($T_i^{comp}$) results in a squared increase in energy consumption. Similarly, offloading tasks to save local energy incurs transmission energy costs ($P_{tx,j}$), which may be prohibitive if the channel quality is poor [cite: 4].

### 2.3 Reliability and Queue Stability
Long-term reliability in resource scheduling is often mathematically represented as **queue stability**. If tasks arrive faster than they are processed, queues grow infinitely, leading to buffer overflows and dropped tasks (system failure). A system is considered stable if the long-term average queue backlog is finite:

\[ \lim_{t \to \infty} \frac{1}{t} \sum_{\tau=0}^{t-1} \mathbb{E}[Q(\tau)] < \infty \]

where $Q(t)$ represents the queue backlog at time slot $t$ [cite: 4, 5]. Strategies that aggressively save energy by putting processors to sleep or reducing frequency risk destabilizing these queues, thereby violating reliability guarantees.

## 3. Lyapunov Optimization: The Core Strategy

The research overwhelmingly points to **Lyapunov Optimization (LO)** as the most effective strategy for resolving the latency-energy-reliability conflict [cite: 4, 6, 7, 8]. LO provides a framework to convert a long-term time-average optimization problem (e.g., "minimize average energy subject to average delay constraints") into a series of deterministic, per-time-slot optimization problems.

### 3.1 The Drift-Plus-Penalty Algorithm
The core mechanism of LO is the **Drift-Plus-Penalty** method. This approach defines a Lyapunov function $L(Q(t)) = \frac{1}{2} \sum Q_i(t)^2$, which represents a scalar measure of the aggregate queue congestion in the system. The "drift" $\Delta(Q(t))$ is the expected change in this function from one time slot to the next.

To balance stability (minimizing drift) with performance (minimizing energy), the algorithm minimizes an upper bound on the following expression at each time slot $t$:

\[ \text{Minimize: } \Delta(Q(t)) + V \cdot \mathbb{E}[\text{Penalty}(t) | Q(t)] \]

*   **$\Delta(Q(t))$ (Drift):** Pushes the system toward stability. If queues $Q(t)$ are large, minimizing the drift prioritizes clearing the backlog (reducing latency risk).
*   **$\text{Penalty}(t)$:** Represents the objective to be minimized, such as Energy Consumption ($E_{total}$).
*   **$V$ (Control Parameter):** A non-negative weight that determines the importance of the penalty relative to stability [cite: 4, 8, 9].

### 3.2 The Trade-off Parameter $V$
The parameter $V$ is the "tuning knob" that resolves the conflict between latency and energy:
*   **High $V$:** The system prioritizes energy efficiency (the Penalty). This allows queues to grow larger, increasing average latency but minimizing power usage.
*   **Low $V$:** The system prioritizes queue stability (Drift). This keeps queues short and latency low, but potentially consumes more energy to process tasks quickly [cite: 8, 10].

Research indicates that LO can achieve an energy consumption within $O(1/V)$ of the optimal value, while ensuring average queue sizes (and thus delay) are bounded by $O(V)$ [cite: 8]. This explicit theoretical bound allows system designers to guarantee long-term reliability while optimizing for energy.

### 3.3 Application in Edge Scenarios
In practical edge computing scenarios, LO is applied to decouple decisions across time frames.
*   **Dynamic Voltage and Frequency Scaling (DVFS):** LO determines the optimal CPU frequency $f(t)$ for each slot. If the virtual queue (representing delay constraints) is high, the algorithm selects a higher frequency despite the energy cost [cite: 4].
*   **Offloading Decisions:** LO guides whether to process locally or offload. If the local energy queue is critical, tasks are offloaded; if the transmission queue is backed up, tasks are processed locally [cite: 11].

## 4. Advanced Reliability: Conformal Lyapunov Optimization

While standard Lyapunov optimization guarantees *average* stability, mission-critical edge applications (e.g., industrial safety systems, autonomous vehicles) often require **deterministic** reliability guarantees. A significant advancement in this domain is **Conformal Lyapunov Optimization (CLO)**.

### 4.1 Limitations of Standard LO
Standard LO ensures that queues are asymptotically stable. However, it does not strictly guarantee that a queue will never exceed a specific threshold at any given instant, nor does it provide worst-case reliability for individual tasks [cite: 8].

### 4.2 The CLO Framework
CLO integrates the standard LO framework with **Online Conformal Risk Control (O-CRC)**. O-CRC is an adaptive mechanism that dynamically adjusts risk parameters based on observed data to control long-term risks.
*   **Mechanism:** CLO optimizes average long-term objectives while satisfying *deterministic* long-term reliability constraints (e.g., a strict limit on the false negative rate in edge inference tasks) [cite: 12, 13, 14].
*   **Outcome:** Simulation results in hierarchical edge inference architectures demonstrate that CLO can strictly control reliability constraints while minimizing the weighted sum of energy consumption and precision loss. This provides a formal worst-case guarantee that standard LO lacks [cite: 15].

## 5. Hybrid Strategies: Combining Lyapunov with AI

The optimization problems derived from the Lyapunov drift-plus-penalty method are often Mixed-Integer Non-Linear Programming (MINLP) problems, which are NP-hard and computationally expensive to solve in real-time [cite: 16]. To address this, researchers have developed hybrid strategies that combine the theoretical stability of LO with the learning capabilities of Deep Reinforcement Learning (DRL) and meta-heuristics.

### 5.1 Lyapunov-Guided Deep Reinforcement Learning (LyDROO)
**LyDROO** is a prominent framework that addresses the computational complexity of LO.
*   **Decoupling:** It uses Lyapunov optimization to decouple the multi-stage stochastic problem into deterministic per-frame subproblems.
*   **Deep Learning:** Instead of using a heavy solver for the per-frame problem, it employs a Deep Neural Network (DNN) to approximate the optimal offloading actions.
*   **Performance:** LyDROO achieves optimal computation performance while stabilizing all queues. It significantly reduces computation time compared to traditional optimization solvers, making it suitable for fast-fading edge environments [cite: 16, 17, 18].

### 5.2 Lyapunov-Guided Actor-Critic (LyA3C)
For environments with continuous action spaces (e.g., continuous power control or frequency scaling), **LyA3C** combines Lyapunov optimization with the Asynchronous Advantage Actor-Critic (A3C) algorithm.
*   **Method:** The problem is modeled as a Markov Decision Process (MDP) guided by Lyapunov drift. The A3C algorithm learns the policy that minimizes the drift-plus-penalty.
*   **Results:** Experiments show LyA3C improves the long-term network computation rate by 2.8% to 5.7% compared to standard DRL baselines (like A2C or TD3) while ensuring queue stability [cite: 19].

### 5.3 Lyapunov-Based Particle Swarm Optimization (LPSO)
For scenarios where training a neural network is not feasible or where a heuristic search is preferred, **LPSO** is utilized.
*   **Integration:** The Lyapunov framework defines the objective function (Drift + Penalty) for each time slot. Particle Swarm Optimization (PSO) is then used to search for the optimal resource allocation vector within that slot.
*   **Benefits:** LPSO avoids local optima better than greedy algorithms and balances transmission power, computing resources, and energy consumption. It has been shown to reduce delay by approximately 25-31% and energy consumption by 9-33% compared to other bio-inspired algorithms [cite: 20, 21, 22].

## 6. Domain-Specific Implementations

The application of these strategies varies based on the specific constraints of the edge environment.

### 6.1 Vehicular Edge Computing (VEC)
In VEC, high mobility causes rapid fluctuations in channel quality and network topology.
*   **Reliability Challenges:** Link failures and handover interruptions.
*   **Strategy:** Multi-agent Proximal Policy Optimization (MAPPO) combined with Lyapunov optimization (Ly-MAPPO) is used. Graph Convolutional Networks (GCN) extract inter-dependencies between subtasks in complex vehicular applications. This approach maximizes data processing rates while adhering to long-term constraints imposed by the variable number of vehicles [cite: 23].
*   **Energy-Latency Trade-off:** Joint optimization of offloading and resource allocation (JOTE) based on Lyapunov optimization minimizes time-average expected delay while stabilizing system operation under mobility constraints [cite: 24].

### 6.2 UAV-Aided Edge Networks
UAVs act as flying edge servers but have severe battery constraints and rely on wireless backhaul.
*   **Strategy:** Energy-efficient task offloading is formulated as an integer programming problem solved via Lyapunov optimization. The algorithm must account for the energy cost of hovering and transmission.
*   **Reliability:** The strategy explicitly handles disturbances caused by UAV communication link failures, ensuring that the offloading decisions remain robust to network instability [cite: 25].

### 6.3 Industrial IoT (IIoT)
IIoT requires strict adherence to process control cycles.
*   **Strategy:** Lyapunov-guided DRL is employed to manage the "end-edge" computation offloading. The focus is on maximizing the network computation rate while strictly balancing CPU frequency and transmission power to maintain data queue stability, which acts as a proxy for operational reliability [cite: 19].

## 7. Comparative Analysis of Strategies

The following table summarizes the strengths and weaknesses of the primary strategies identified in the research:

| Strategy | Core Mechanism | Latency Management | Energy Efficiency | Reliability Guarantee | Best Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Standard Lyapunov (LO)** | Drift-Plus-Penalty | Controlled via queue drift minimization | Tunable via parameter $V$ | Asymptotic Queue Stability | General Edge/Fog scenarios with stochastic arrivals [cite: 4, 8] |
| **Conformal Lyapunov (CLO)** | LO + Online Conformal Risk Control | Implicit in risk control | Optimized alongside risk | **Deterministic / Worst-Case** | Mission-critical inference (e.g., medical, safety) [cite: 12, 14] |
| **LyDROO / LyA3C** | LO + Deep Reinforcement Learning | Learned policy minimizes drift | Learned policy minimizes penalty | Stability via LO guidance | Complex, dynamic environments (fast fading channels) [cite: 16, 19] |
| **LPSO** | LO + Particle Swarm Optimization | Search minimizes slot drift | Search minimizes slot penalty | Stability via LO objective | Scenarios requiring global optimization without training overhead [cite: 21, 22] |
| **Score-Based / Ranking** | Heuristic Scoring | Selection based on node capability | Selection based on resource availability | Best-effort (No formal guarantee) | Simple implementations, Video Streaming [cite: 1, 26] |

## 8. Emerging Trends: Federated Learning and Edge Intelligence

Recent research applies these scheduling strategies to **Federated Learning (FL)** at the edge. FL involves training models across distributed devices, which consumes significant energy and bandwidth.
*   **Adaptive Resource Allocation:** Lyapunov stochastic optimization is used to dynamically optimize radio parameters (transmit power, bits) and computation resources (CPU cycles) for FL.
*   **Objective:** The goal is to strike the best trade-off between the power consumption of the devices, the latency of the training rounds, and the learning performance (accuracy).
*   **Outcome:** These strategies allow for energy-efficient, low-latency adaptive learning that guarantees the convergence of the model (a form of algorithmic reliability) [cite: 7, 27].

## 9. Conclusion

To resolve the conflict between latency sensitivity and energy efficiency while guaranteeing reliability in edge computing, the **Lyapunov Optimization (LO)** framework stands out as the definitive strategy. By transforming long-term stability constraints into instantaneous "drift" minimization problems, LO allows edge nodes to dynamically trade off energy consumption (penalty) against latency risk (queue backlog) using the control parameter $V$.

For modern, complex edge environments, this theoretical foundation is best implemented through **hybrid architectures**. **LyDROO** and **LyA3C** leverage Deep Reinforcement Learning to solve the per-slot optimization problems efficiently in real-time, adapting to unknown channel statistics. For applications requiring strict safety guarantees, **Conformal Lyapunov Optimization (CLO)** provides the necessary deterministic reliability that standard stochastic methods lack. Ultimately, the choice of strategy depends on the specific "reliability" definition required: asymptotic queue stability (Standard LO) or worst-case performance guarantees (CLO).

## References

[cite: 1] Scoca, A., Aral, A., Brandic, I., De Nicola, R., & Uriarte, R. B. (2018). Scheduling Latency-Sensitive Applications in Edge Computing.
[cite: 26] Scoca, A., Aral, A., Brandic, I., De Nicola, R., & Uriarte, R. B. (2018). Scheduling Latency-Sensitive Applications in Edge Computing.
[cite: 2] Electronics 2023, 12, 2599.
[cite: 20] Electronics 2023, 12, 1511.
[cite: 3] MDPI, Electronics 2025, 14, 79.
[cite: 6] arXiv:2103.16985.
[cite: 7] TechRxiv, Lyapunov-based Optimization of Edge Resources for Energy-Efficient Adaptive Federated Learning.
[cite: 19] Applied Sciences 2024, 14, 11160.
[cite: 25] IEEE Xplore, 2024 International Conference on Computing, Networking and Communications (ICNC).
[cite: 21] PMC, Delay-Sensitive Tasks in IoT.
[cite: 21] PMC, Delay-Sensitive Multi-Period Computation Offloading.
[cite: 28] arXiv:2506.04291.
[cite: 4] Merluzzi, M., et al. Network Energy Efficient Mobile Edge Computing with Reliability Guarantees.
[cite: 11] MDPI, Sensors 2020, 20, 122.
[cite: 5] Oulu Repo, Power-delay tradeoff in MEC.
[cite: 12] Binucci, F., et al. (2025). Resource Management for Multiuser Opportunistic Edge-Inference by Conformal Lyapunov Optimization.
[cite: 13] arXiv:2503.00486.
[cite: 15] ResearchGate, Conformal Lyapunov Optimization.
[cite: 29] IEEE Transactions on Network and Service Management, Vol 21, No 6, Dec 2024.
[cite: 8] ResearchGate, Lyapunov Drift-Plus-Penalty Optimization for Queues With Finite Capacity.
[cite: 9] arXiv:2506.04291.
[cite: 10] IEEE Xplore, Lyapunov's theory utilized to decouple coupling relationship.
[cite: 16] IEEE Transactions on Wireless Communications, 2021.
[cite: 17] SciSpace, Lyapunov-Guided Deep Reinforcement Learning.
[cite: 19] Applied Sciences 2024, 14, 11160.
[cite: 30] arXiv:2010.01370.
[cite: 18] GitHub, revenol/LyDROO.
[cite: 14] arXiv:2503.00486v5.
[cite: 23] ResearchGate, Lyapunov Optimization based Mobile Edge Computing for Internet of Vehicles Systems.
[cite: 15] ResearchGate, Conformal Lyapunov Optimization.
[cite: 31] MDPI, Sensors 2024, 24, 1165.
[cite: 32] Iris Unito, Modified PSO.
[cite: 33] Journal of Cloud Computing, 2021.
[cite: 27] MDPI, Sensors 2026, 26, 619.
[cite: 22] MDPI, Sensors 2022, 22, 3527.
[cite: 24] ResearchGate, Energy-latency tradeoff for task offloading.

**Sources:**
1. [tuwien.ac.at](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxLqfV9SDUCCO4fZyVmUk1mncy9OpQnJfdmNrbNTwA2Ix7R3VkijEY5IZrhlpe3FKNjZ1GtDSmhdQ51csybqdzGceqxpTg8YV6jvHW-Lo0tsCkCFVdAbgHb5sfkvgaat_K06nL6CezxqhYCf7Je4SZLUjKS0T_gCy1ecofmhw6-PoZU6ntMuiy_b-pl42pKw5V5nEQxxlia12m7OmWOPTMAv2z8s7TD6g2-loCNWJIuVV4SBF0Q3rhtED5mbLkqN3H4SdHyCAoLQBMr2vopi5vrEU0luRGSCeJK0JqSJViYwLQMhhc8w==)
2. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbE9IQO2Uyhhi8Bi5t2zo_LMYomaNJZ22gpvjRkkNF5faa-c84OfiWZbn0Hn17PkYNZX2LtFEE3hQ2ksi8tIP0_WOt859N779fGr9SjCsr-LEQX36Y0GyljuL8SOx_HA==)
3. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEEB07SCNM0wt4WMK4w7qM535fmMezofHikMD-FZEN8RJ8aBtJWj9vburtahCfViebNqzpIm2Xwyl-QDTiIwUj64phkroc3B4bteVufdllFQHmSZDUROGbJpyVZg==)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_aNvmVkntbkaTwHbYP_FmJGC734MMQSbEk-iLxnyT-Eh1u2KpG_eV78Tvbxq8NEzagcW74IYabYwCZpijxyKFiCsHWSGXW6oAToqngsMjO51O6JzLN5-I4jzIAwKlPF7UcsiitctKH_lZORFRRp7VDFmbpAMZveL3SSSUAB0ft98ZockPz_0orOkoT-6_JbY7LlcSGNZHN4Q3Qtoml5R1jdbfLMq8YPQv7cr1XWA9QJY_4Q==)
5. [oulu.fi](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBVMNfqCL_x2EHnhAIrT1s0dFe_DP1QtN_wTcDt-QNri0Q1sjGbNANFjgQdZ6Cjs0cue8fxQCpM8KdpWlh9iOAtjNC0JhyjF__yBtRFlZVaPDv_Y20XwuA7F3FZLbHJzj1gGWmlzEWydGXijalLEtPRrJtrH-qjO0kmWg_ryCSVuYhzjlYyXm6HIu2c-edoR4Ww5EqbXpHNEtwxuc=)
6. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcTpPsSib24dcz3quyNSU7xEmHuJBGVR2iXClZFUPZaKpdyuoFQ3vKced7T7-FhRooNhwL6kYRVM4vs9qGjXXuyWSXuHYXT-_7TNYqkRIx2H0ny5ZVZQ==)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGK0s6z54nqSpKHGL8UrwDBlmLxLFzKUSQz9_jvD0WTeceYDwhYJT9Kvs2BMlDwJe5o2G_ptFqqTxERlRB8qT-zg9VJUqQf9mu74jBsJpvUraR_9_qGUUti_KoHWJHrfBHgoF2-45f46TaStC2T7KiJmTa64M5k5iwtUWVqeGV-gLPQLDaeC7v1whFm4WahRPkue19qWJtgdR8g8zuJ_pHvvtVqkPUHjKpvxiFPBeX6riKYUuBe013p4TaKWpyseRDjE4JgAbFuUg==)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSJmj2ToHyxcxmorZCiHMZu1aA9AvHeUVAgcy3l5PWsRtHgbQCNOlLMC3Ueu00Ul7GbILdGLba9nluaqrx2afEQni_bvqeEdqzSPX4ah3XriJOtMK1n8ZuTqeg9JVm1Q0jsGapXUrB6FOM4egMuN3RLEDGMUOWjB51bcCIT33PIb6BdxM8VkAvYv4CB8A_-zkS67cSTYRowoA0JyDFSjzN9xoaHRuX3vTUMb4N4NSJtWs=)
9. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyu-MsdRMwFlZQMR3xK-pe50Vey7Pt-7HBkryVh7IYxJWm8BKX-ZMpmGaVRndOg_IdhOVFC7GMwJrCyT9Jhom5HecZrgmYbgkzFVT8OI1nbWq7N_KvCA==)
10. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_Zb6M8IyGyUpDI2Z88wVpo5PiqmuLTPpukwG94oFw5pm-KQC3ShzqcbtdnKAdKKtwNSyfVCV1CU0whLPU9tkS5em332wX_mwX20br2BSAUOPZV-Rg5dEnSpMRIcB0EQw_RTUzPHnI3Mg_VbHPCELOKAtt)
11. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFm60LkeEU_kRf4jXowgYcDb0XmtItrFcCITaSXFEnCecVpckCRxIJyNwH1BlzV7LxGAqnTJuHSUk_ojrtgBowxTxHbp95Fl2vn9WnR_XVTXk3RYI_AW_Prec81HM=)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7ELRTSMttl4_HjDzCqrbct6om0cDm7nlmRClI2GnzLMM2TQzWJW3hhTWIII8Dfu16ztcYR8JNPERoyhM9l3-mdaOBK9t9P9ot6dX5WLZDxQSh1gjsiw7ukHfPE_D-33NLgvyMaeVH6-k4BPBRCbSUmu3D5o8AIo6V91aLQnvTHsokyVELRzELg1wF4mv4lIW6hia2Be593tO78255DJhka50X8UZxXKBP50AWdYD1BC0aRiWoLGlgSql8DZqgf9Qh14CIuA==)
13. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIu8A9eDBTX5ZJc7s0ChB6eXrddwIk49Ugii4gL0Vctri4uvs-JbZm1-rKtLWdXe_lTLSddssgT6O7m15oCzmDemfsva1vGCByTQSJcl5HR8rN7BfaXw==)
14. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHevl5k-05aVJyTLFQQLwTekeJAkhvpXlnzDkL_j2sC0a7LP2v8t2-Dy97_xak9gv7H3rSfPuFtiSO5DQAUobY6ktmzKJvbE1oViIrenVz1fjTQZ0y4c3jGnQ==)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0QY6I4reNMv9VNMDjdhR5yuVFiVztC_53EGSce0bouJImSeeGyec5z5viqNQveZK0-awvTfArlaNCNP3u9QH18fg2KsyYLwyV-czYUYJo14UdTLz1VN1y2FM1B65yoqtDlcXvxJBPnl_VeNsmL7knoARY76RXYhfPyDRWZPIV_jk7Uk42YlcbP5HgOY7vP7XDIy93t_6H5TFUFwEiId-KUQH3_NwmEI8REbsmnypN1SG7J10It6VSx1A0vB7jx4q99yj2KiePEuVlV_5-kzCvBA==)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqbS24wD9X4dY6neGSC10B8KkSWdHwBm-Tr9w7oJPa0A0lfXOrd_e-MMg7PVrA7y52grICA09onduvOZAnKLgX7c_jSF5htPNmOckEY6Veb0IuEiWIJc0TTSAeDs0ujjv6aNLg0bDpi_1FKNq-t8ULVZY4EFU5u1CTEirc5w2ketmyJ1okYzkOWDShq6_kwO_LHGc2XmhMIleKARNNBqnBTiwpCU-sIFg1c-0B70YVBPX5_Tl1-9jXgSqfFQ9dztRW0PbmGzLeu__hcYofb4QNR6fLTIW8MyilfPk7UUK-HA==)
17. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqZvp6W3m4YL369BS07Lhnd8gUfVX_aAsy-n60aeF3E_whYYXakXqdYr4Xm-0mknLm-ZEdj0HrU8z0M-A2cELMhqguAxDgq1BUGIm2GBOsvG0s5XtNwrqqHsG51J5b6GxkPYJtgIe9N5Cfiihg63Mn7BKJRTx6l_U5rrmy2puSmKkqsGcq2zVy3sBTvOExc49RDBM=)
18. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZ-NnLNyUrc27y95cxQWL0T6NOaTJLBKqrVxdx6CHBrbGQOWWZEKhDhBK8URYY-ZOBzc1uSrzO64LXiFxRE9Z9VOCB8aIsc8oD2VEPZrNYjMEbvM-B1y8=)
19. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsWs-ZbVp6ufEQUzeL-4jM2svwMZOd4h86NXs-jTadgn2Z-48bWinE2NERV0DO3fGz-X4FqeOCpKohJfmtAb1xnl4T0BfuzOnooZJ7mzr8je6rWKbwjiIUtocHJPgnw_Y=)
20. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkfghdCTkXUjoFVY8gsB0npILuPtU_CB7f1bNy5BYzewirgomeb4e5AeCz5U97oc_TiwS5Oz8TwVFnhPjOuR_ZuHJ7joEf5w4Mu1I-GHb7a5ZsTzUwXxe-mfAwfYzp)
21. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHokidy5AnwIWkhWv3EZpL469s7SttvFkl-RU4PWs2qWuKBy5ZXVF2CnInT-khi_IEOskEAgampi8ZcJJN3rsmoQQUWMBreY1cazXtNT3ZO_ki5wJqVqh4g2-0Q1LGhXrutWWNZG6Kn)
22. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4fWmsAKkiO54TsI65_-kHlPoSoAlq8AIbZYXOAUL8VxA316E3q7sOyyRMKDcaBxYnUkl6cvj3qrrFnRWZ9Jd_fZxZHRORYfCCsF441RtJebom_Vq0XMnUp6PrjpvS)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6GPGwt55k-r2C2Ic8i55oBNSFVE3evzjIvgmmNYnAN2wUus8swUcYfgdaj5MIPz_TvUtlo71ffqTjqOI7k-70SfEINZER9NFfHFZ3IcqLkmBht4HwXmI-1nyTjeA9YMVO13db6cErjipr-lvjgG2UWXU8WDPwKjDMU-JngYZ35bx0uXIrsbord44Zve3QlOVWDaIWK6VA0HgKX8UgWvLZ6DfX_09tAf7l2GicrvHx3K2BVcjGbHxS8t3G2Q==)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELNzIzFoAAA5eWgoNuuyaCdcK1bkGJxVGVxhn1QSTjAAXOzjFnMni_0DdcYPOOPCZ0e8gMWlfuYF5gsccYS9oh20gHM-XbM0_mfXC11oxFPDhpntK-UuqI4nogXdfA_WDK7eaUcIBT_iD_Dnk6wmzTw30UQF675msLv_p_z42c_zuojk3bh9-0MGvs3MMdmK_TJzIHmenTqTzUHv5zQhRruTSsLzw8JRo3NnOWiqeCREWNUer05mCLqUms4sayatjITWmIWkHxE1o=)
25. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpfee8-ZEjqNrdj25FL2SJcCi2TgAcl2IDA-UceQ8USKAZJsVnKsJsRMj8lJBLH1Q4WHn_1VORv-vrAHdNwz2nd2U-yExB2gEZBTvifHmi7xx41sKYpifkcHs2sig-uKqE7zgI)
26. [scitepress.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcEdwYc-Hs5hIJ_N86doOWKIpzEk37rfzjtVkTMwXj0MmvLrKSR26qgWWL0Sjz20RGJgEiUoe1LSR5GoUuxEjFG9simCj9HaB3kz-BFWponGFq_3yiv9xFEr1eQK5zoaFRBeq7SoX7SqdNteg=)
27. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNkQ_nxA-QkEyeDaBv3cZ0gCET8e7t5EC1G6W_FmWp43ao-2bYk3niJEAqUh638boHeterGRRS8_zfsHVIX3yG5CGlXxRQ8QA_PJLmHjxEi78bSfwuJF3qQNm-YoQ=)
28. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpp6ofZIpNHVFQy3fsjmGfpu-m1h4dzus3TpVaEB3-QwTURb_zpjCnvA3ytY4bYfAJATZT1fucqGhMkEDESGqlxdWS0XxKzHH8gsxElb7KhT5ge_RplerELg==)
29. [scribd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCaJwcSFjez0CaEft_zJte87bccSb_RkLVJOTxdPIFxOSo5lbHfMgKr8LoZq7AhoNVOru4zQqBOCY0nXk3Pkrt35tkPTssqngBZyUjchtkZsgVneTD4XFoo7WS1uhx6qiIUEk=)
30. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaldcXOu4Mm4BezJv71IGgmfO-gKA5PzjC1z32ZI-VLVZr73FK0uZwQA0pGVSq412udG8xPhcerfOPQN6byqLu8ISKafZrrdOJiQ3vXdhGgnUNdQr5nQ==)
31. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHM5ebRiXgPEx8THpfiqhUOsDbUN9VsgLKKZmKnROsUV-lwhZjWQI7R-bf_Ub12ZwgD9meU6JPHAfbuGRwO14AfGNndgX5Oby9K3Hg5k9u90h9yDr-EAiN91_FCPBr)
32. [unito.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXYsFzjUj8aB6nnzeX9O3kcFZ8IEAQmrQcoxy-wNFgJsVU3BrLPRoRhykiPpDbcW4NQ3GdTbdMmBRDMt2z5n9EZ3XE9dSBQXtNdiwzz5bj_4QjWvjBPWIpexWSLp9DLuj1KivGpXsxttSr0J9CZ0-zbcu9Gzj1f5E4Qv5vhYAToiOpfmiRgUT1MLy59OXDvA==)
33. [slogix.in](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLAudLrQ3B28eeBL_8G08jJft6Fu8_VptiNORfLYqyIfVoEZRU0L3EdXpAolAikjM9JEIHqlZAj5fiRLBcSOPWMBG2r_jvBzZhDWT9oKMfkuRwCbsW6Lllrxycwom7hYKXycB5A4oOHPNo--sC283m1jY2FwU9-6-FxgUzBd210gBwMqjUbf1oOTAe-3ZmB6qYrNh95lwV-NqYi-wxZA_5baJ8nas0sUII5UJlpvnYdcsZ1HjKXbM9Lavm9M1qHPyXtkGdCSzjc5K85y9wLtZPDLP5mnyv)


## Annotations
Annotation(end_index=2184, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbE9IQO2Uyhhi8Bi5t2zo_LMYomaNJZ22gpvjRkkNF5faa-c84OfiWZbn0Hn17PkYNZX2LtFEE3hQ2ksi8tIP0_WOt859N779fGr9SjCsr-LEQX36Y0GyljuL8SOx_HA==', start_index=2172)
Annotation(end_index=2184, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxLqfV9SDUCCO4fZyVmUk1mncy9OpQnJfdmNrbNTwA2Ix7R3VkijEY5IZrhlpe3FKNjZ1GtDSmhdQ51csybqdzGceqxpTg8YV6jvHW-Lo0tsCkCFVdAbgHb5sfkvgaat_K06nL6CezxqhYCf7Je4SZLUjKS0T_gCy1ecofmhw6-PoZU6ntMuiy_b-pl42pKw5V5nEQxxlia12m7OmWOPTMAv2z8s7TD6g2-loCNWJIuVV4SBF0Q3rhtED5mbLkqN3H4SdHyCAoLQBMr2vopi5vrEU0luRGSCeJK0JqSJViYwLQMhhc8w==', start_index=2172)
Annotation(end_index=2754, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_aNvmVkntbkaTwHbYP_FmJGC734MMQSbEk-iLxnyT-Eh1u2KpG_eV78Tvbxq8NEzagcW74IYabYwCZpijxyKFiCsHWSGXW6oAToqngsMjO51O6JzLN5-I4jzIAwKlPF7UcsiitctKH_lZORFRRp7VDFmbpAMZveL3SSSUAB0ft98ZockPz_0orOkoT-6_JbY7LlcSGNZHN4Q3Qtoml5R1jdbfLMq8YPQv7cr1XWA9QJY_4Q==', start_index=2742)
Annotation(end_index=2754, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEEB07SCNM0wt4WMK4w7qM535fmMezofHikMD-FZEN8RJ8aBtJWj9vburtahCfViebNqzpIm2Xwyl-QDTiIwUj64phkroc3B4bteVufdllFQHmSZDUROGbJpyVZg==', start_index=2742)
Annotation(end_index=3776, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEEB07SCNM0wt4WMK4w7qM535fmMezofHikMD-FZEN8RJ8aBtJWj9vburtahCfViebNqzpIm2Xwyl-QDTiIwUj64phkroc3B4bteVufdllFQHmSZDUROGbJpyVZg==', start_index=3767)
Annotation(end_index=4087, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEEB07SCNM0wt4WMK4w7qM535fmMezofHikMD-FZEN8RJ8aBtJWj9vburtahCfViebNqzpIm2Xwyl-QDTiIwUj64phkroc3B4bteVufdllFQHmSZDUROGbJpyVZg==', start_index=4078)
Annotation(end_index=4545, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEEB07SCNM0wt4WMK4w7qM535fmMezofHikMD-FZEN8RJ8aBtJWj9vburtahCfViebNqzpIm2Xwyl-QDTiIwUj64phkroc3B4bteVufdllFQHmSZDUROGbJpyVZg==', start_index=4536)
Annotation(end_index=4865, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_aNvmVkntbkaTwHbYP_FmJGC734MMQSbEk-iLxnyT-Eh1u2KpG_eV78Tvbxq8NEzagcW74IYabYwCZpijxyKFiCsHWSGXW6oAToqngsMjO51O6JzLN5-I4jzIAwKlPF7UcsiitctKH_lZORFRRp7VDFmbpAMZveL3SSSUAB0ft98ZockPz_0orOkoT-6_JbY7LlcSGNZHN4Q3Qtoml5R1jdbfLMq8YPQv7cr1XWA9QJY_4Q==', start_index=4856)
Annotation(end_index=5389, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_aNvmVkntbkaTwHbYP_FmJGC734MMQSbEk-iLxnyT-Eh1u2KpG_eV78Tvbxq8NEzagcW74IYabYwCZpijxyKFiCsHWSGXW6oAToqngsMjO51O6JzLN5-I4jzIAwKlPF7UcsiitctKH_lZORFRRp7VDFmbpAMZveL3SSSUAB0ft98ZockPz_0orOkoT-6_JbY7LlcSGNZHN4Q3Qtoml5R1jdbfLMq8YPQv7cr1XWA9QJY_4Q==', start_index=5377)
Annotation(end_index=5389, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBVMNfqCL_x2EHnhAIrT1s0dFe_DP1QtN_wTcDt-QNri0Q1sjGbNANFjgQdZ6Cjs0cue8fxQCpM8KdpWlh9iOAtjNC0JhyjF__yBtRFlZVaPDv_Y20XwuA7F3FZLbHJzj1gGWmlzEWydGXijalLEtPRrJtrH-qjO0kmWg_ryCSVuYhzjlYyXm6HIu2c-edoR4Ww5EqbXpHNEtwxuc=', start_index=5377)
Annotation(end_index=5781, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_aNvmVkntbkaTwHbYP_FmJGC734MMQSbEk-iLxnyT-Eh1u2KpG_eV78Tvbxq8NEzagcW74IYabYwCZpijxyKFiCsHWSGXW6oAToqngsMjO51O6JzLN5-I4jzIAwKlPF7UcsiitctKH_lZORFRRp7VDFmbpAMZveL3SSSUAB0ft98ZockPz_0orOkoT-6_JbY7LlcSGNZHN4Q3Qtoml5R1jdbfLMq8YPQv7cr1XWA9QJY_4Q==', start_index=5763)
Annotation(end_index=5781, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSJmj2ToHyxcxmorZCiHMZu1aA9AvHeUVAgcy3l5PWsRtHgbQCNOlLMC3Ueu00Ul7GbILdGLba9nluaqrx2afEQni_bvqeEdqzSPX4ah3XriJOtMK1n8ZuTqeg9JVm1Q0jsGapXUrB6FOM4egMuN3RLEDGMUOWjB51bcCIT33PIb6BdxM8VkAvYv4CB8A_-zkS67cSTYRowoA0JyDFSjzN9xoaHRuX3vTUMb4N4NSJtWs=', start_index=5763)
Annotation(end_index=5781, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcTpPsSib24dcz3quyNSU7xEmHuJBGVR2iXClZFUPZaKpdyuoFQ3vKced7T7-FhRooNhwL6kYRVM4vs9qGjXXuyWSXuHYXT-_7TNYqkRIx2H0ny5ZVZQ==', start_index=5763)
Annotation(end_index=5781, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGK0s6z54nqSpKHGL8UrwDBlmLxLFzKUSQz9_jvD0WTeceYDwhYJT9Kvs2BMlDwJe5o2G_ptFqqTxERlRB8qT-zg9VJUqQf9mu74jBsJpvUraR_9_qGUUti_KoHWJHrfBHgoF2-45f46TaStC2T7KiJmTa64M5k5iwtUWVqeGV-gLPQLDaeC7v1whFm4WahRPkue19qWJtgdR8g8zuJ_pHvvtVqkPUHjKpvxiFPBeX6riKYUuBe013p4TaKWpyseRDjE4JgAbFuUg==', start_index=5763)
Annotation(end_index=7053, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_aNvmVkntbkaTwHbYP_FmJGC734MMQSbEk-iLxnyT-Eh1u2KpG_eV78Tvbxq8NEzagcW74IYabYwCZpijxyKFiCsHWSGXW6oAToqngsMjO51O6JzLN5-I4jzIAwKlPF7UcsiitctKH_lZORFRRp7VDFmbpAMZveL3SSSUAB0ft98ZockPz_0orOkoT-6_JbY7LlcSGNZHN4Q3Qtoml5R1jdbfLMq8YPQv7cr1XWA9QJY_4Q==', start_index=7038)
Annotation(end_index=7053, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSJmj2ToHyxcxmorZCiHMZu1aA9AvHeUVAgcy3l5PWsRtHgbQCNOlLMC3Ueu00Ul7GbILdGLba9nluaqrx2afEQni_bvqeEdqzSPX4ah3XriJOtMK1n8ZuTqeg9JVm1Q0jsGapXUrB6FOM4egMuN3RLEDGMUOWjB51bcCIT33PIb6BdxM8VkAvYv4CB8A_-zkS67cSTYRowoA0JyDFSjzN9xoaHRuX3vTUMb4N4NSJtWs=', start_index=7038)
Annotation(end_index=7053, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyu-MsdRMwFlZQMR3xK-pe50Vey7Pt-7HBkryVh7IYxJWm8BKX-ZMpmGaVRndOg_IdhOVFC7GMwJrCyT9Jhom5HecZrgmYbgkzFVT8OI1nbWq7N_KvCA==', start_index=7038)
Annotation(end_index=7531, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSJmj2ToHyxcxmorZCiHMZu1aA9AvHeUVAgcy3l5PWsRtHgbQCNOlLMC3Ueu00Ul7GbILdGLba9nluaqrx2afEQni_bvqeEdqzSPX4ah3XriJOtMK1n8ZuTqeg9JVm1Q0jsGapXUrB6FOM4egMuN3RLEDGMUOWjB51bcCIT33PIb6BdxM8VkAvYv4CB8A_-zkS67cSTYRowoA0JyDFSjzN9xoaHRuX3vTUMb4N4NSJtWs=', start_index=7518)
Annotation(end_index=7531, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_Zb6M8IyGyUpDI2Z88wVpo5PiqmuLTPpukwG94oFw5pm-KQC3ShzqcbtdnKAdKKtwNSyfVCV1CU0whLPU9tkS5em332wX_mwX20br2BSAUOPZV-Rg5dEnSpMRIcB0EQw_RTUzPHnI3Mg_VbHPCELOKAtt', start_index=7518)
Annotation(end_index=7716, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSJmj2ToHyxcxmorZCiHMZu1aA9AvHeUVAgcy3l5PWsRtHgbQCNOlLMC3Ueu00Ul7GbILdGLba9nluaqrx2afEQni_bvqeEdqzSPX4ah3XriJOtMK1n8ZuTqeg9JVm1Q0jsGapXUrB6FOM4egMuN3RLEDGMUOWjB51bcCIT33PIb6BdxM8VkAvYv4CB8A_-zkS67cSTYRowoA0JyDFSjzN9xoaHRuX3vTUMb4N4NSJtWs=', start_index=7707)
Annotation(end_index=8225, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_aNvmVkntbkaTwHbYP_FmJGC734MMQSbEk-iLxnyT-Eh1u2KpG_eV78Tvbxq8NEzagcW74IYabYwCZpijxyKFiCsHWSGXW6oAToqngsMjO51O6JzLN5-I4jzIAwKlPF7UcsiitctKH_lZORFRRp7VDFmbpAMZveL3SSSUAB0ft98ZockPz_0orOkoT-6_JbY7LlcSGNZHN4Q3Qtoml5R1jdbfLMq8YPQv7cr1XWA9QJY_4Q==', start_index=8216)
Annotation(end_index=8444, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFm60LkeEU_kRf4jXowgYcDb0XmtItrFcCITaSXFEnCecVpckCRxIJyNwH1BlzV7LxGAqnTJuHSUk_ojrtgBowxTxHbp95Fl2vn9WnR_XVTXk3RYI_AW_Prec81HM=', start_index=8434)
Annotation(end_index=9092, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSJmj2ToHyxcxmorZCiHMZu1aA9AvHeUVAgcy3l5PWsRtHgbQCNOlLMC3Ueu00Ul7GbILdGLba9nluaqrx2afEQni_bvqeEdqzSPX4ah3XriJOtMK1n8ZuTqeg9JVm1Q0jsGapXUrB6FOM4egMuN3RLEDGMUOWjB51bcCIT33PIb6BdxM8VkAvYv4CB8A_-zkS67cSTYRowoA0JyDFSjzN9xoaHRuX3vTUMb4N4NSJtWs=', start_index=9083)
Annotation(end_index=9554, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7ELRTSMttl4_HjDzCqrbct6om0cDm7nlmRClI2GnzLMM2TQzWJW3hhTWIII8Dfu16ztcYR8JNPERoyhM9l3-mdaOBK9t9P9ot6dX5WLZDxQSh1gjsiw7ukHfPE_D-33NLgvyMaeVH6-k4BPBRCbSUmu3D5o8AIo6V91aLQnvTHsokyVELRzELg1wF4mv4lIW6hia2Be593tO78255DJhka50X8UZxXKBP50AWdYD1BC0aRiWoLGlgSql8DZqgf9Qh14CIuA==', start_index=9536)
Annotation(end_index=9554, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIu8A9eDBTX5ZJc7s0ChB6eXrddwIk49Ugii4gL0Vctri4uvs-JbZm1-rKtLWdXe_lTLSddssgT6O7m15oCzmDemfsva1vGCByTQSJcl5HR8rN7BfaXw==', start_index=9536)
Annotation(end_index=9554, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHevl5k-05aVJyTLFQQLwTekeJAkhvpXlnzDkL_j2sC0a7LP2v8t2-Dy97_xak9gv7H3rSfPuFtiSO5DQAUobY6ktmzKJvbE1oViIrenVz1fjTQZ0y4c3jGnQ==', start_index=9536)
Annotation(end_index=9856, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0QY6I4reNMv9VNMDjdhR5yuVFiVztC_53EGSce0bouJImSeeGyec5z5viqNQveZK0-awvTfArlaNCNP3u9QH18fg2KsyYLwyV-czYUYJo14UdTLz1VN1y2FM1B65yoqtDlcXvxJBPnl_VeNsmL7knoARY76RXYhfPyDRWZPIV_jk7Uk42YlcbP5HgOY7vP7XDIy93t_6H5TFUFwEiId-KUQH3_NwmEI8REbsmnypN1SG7J10It6VSx1A0vB7jx4q99yj2KiePEuVlV_5-kzCvBA==', start_index=9846)
Annotation(end_index=10135, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqbS24wD9X4dY6neGSC10B8KkSWdHwBm-Tr9w7oJPa0A0lfXOrd_e-MMg7PVrA7y52grICA09onduvOZAnKLgX7c_jSF5htPNmOckEY6Veb0IuEiWIJc0TTSAeDs0ujjv6aNLg0bDpi_1FKNq-t8ULVZY4EFU5u1CTEirc5w2ketmyJ1okYzkOWDShq6_kwO_LHGc2XmhMIleKARNNBqnBTiwpCU-sIFg1c-0B70YVBPX5_Tl1-9jXgSqfFQ9dztRW0PbmGzLeu__hcYofb4QNR6fLTIW8MyilfPk7UUK-HA==', start_index=10125)
Annotation(end_index=11047, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqbS24wD9X4dY6neGSC10B8KkSWdHwBm-Tr9w7oJPa0A0lfXOrd_e-MMg7PVrA7y52grICA09onduvOZAnKLgX7c_jSF5htPNmOckEY6Veb0IuEiWIJc0TTSAeDs0ujjv6aNLg0bDpi_1FKNq-t8ULVZY4EFU5u1CTEirc5w2ketmyJ1okYzkOWDShq6_kwO_LHGc2XmhMIleKARNNBqnBTiwpCU-sIFg1c-0B70YVBPX5_Tl1-9jXgSqfFQ9dztRW0PbmGzLeu__hcYofb4QNR6fLTIW8MyilfPk7UUK-HA==', start_index=11029)
Annotation(end_index=11047, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZ-NnLNyUrc27y95cxQWL0T6NOaTJLBKqrVxdx6CHBrbGQOWWZEKhDhBK8URYY-ZOBzc1uSrzO64LXiFxRE9Z9VOCB8aIsc8oD2VEPZrNYjMEbvM-B1y8=', start_index=11029)
Annotation(end_index=11047, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqZvp6W3m4YL369BS07Lhnd8gUfVX_aAsy-n60aeF3E_whYYXakXqdYr4Xm-0mknLm-ZEdj0HrU8z0M-A2cELMhqguAxDgq1BUGIm2GBOsvG0s5XtNwrqqHsG51J5b6GxkPYJtgIe9N5Cfiihg63Mn7BKJRTx6l_U5rrmy2puSmKkqsGcq2zVy3sBTvOExc49RDBM=', start_index=11029)
Annotation(end_index=11673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsWs-ZbVp6ufEQUzeL-4jM2svwMZOd4h86NXs-jTadgn2Z-48bWinE2NERV0DO3fGz-X4FqeOCpKohJfmtAb1xnl4T0BfuzOnooZJ7mzr8je6rWKbwjiIUtocHJPgnw_Y=', start_index=11663)
Annotation(end_index=12392, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkfghdCTkXUjoFVY8gsB0npILuPtU_CB7f1bNy5BYzewirgomeb4e5AeCz5U97oc_TiwS5Oz8TwVFnhPjOuR_ZuHJ7joEf5w4Mu1I-GHb7a5ZsTzUwXxe-mfAwfYzp', start_index=12374)
Annotation(end_index=12392, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4fWmsAKkiO54TsI65_-kHlPoSoAlq8AIbZYXOAUL8VxA316E3q7sOyyRMKDcaBxYnUkl6cvj3qrrFnRWZ9Jd_fZxZHRORYfCCsF441RtJebom_Vq0XMnUp6PrjpvS', start_index=12374)
Annotation(end_index=12392, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHokidy5AnwIWkhWv3EZpL469s7SttvFkl-RU4PWs2qWuKBy5ZXVF2CnInT-khi_IEOskEAgampi8ZcJJN3rsmoQQUWMBreY1cazXtNT3ZO_ki5wJqVqh4g2-0Q1LGhXrutWWNZG6Kn', start_index=12374)
Annotation(end_index=13115, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6GPGwt55k-r2C2Ic8i55oBNSFVE3evzjIvgmmNYnAN2wUus8swUcYfgdaj5MIPz_TvUtlo71ffqTjqOI7k-70SfEINZER9NFfHFZ3IcqLkmBht4HwXmI-1nyTjeA9YMVO13db6cErjipr-lvjgG2UWXU8WDPwKjDMU-JngYZ35bx0uXIrsbord44Zve3QlOVWDaIWK6VA0HgKX8UgWvLZ6DfX_09tAf7l2GicrvHx3K2BVcjGbHxS8t3G2Q==', start_index=13105)
Annotation(end_index=13356, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELNzIzFoAAA5eWgoNuuyaCdcK1bkGJxVGVxhn1QSTjAAXOzjFnMni_0DdcYPOOPCZ0e8gMWlfuYF5gsccYS9oh20gHM-XbM0_mfXC11oxFPDhpntK-UuqI4nogXdfA_WDK7eaUcIBT_iD_Dnk6wmzTw30UQF675msLv_p_z42c_zuojk3bh9-0MGvs3MMdmK_TJzIHmenTqTzUHv5zQhRruTSsLzw8JRo3NnOWiqeCREWNUer05mCLqUms4sayatjITWmIWkHxE1o=', start_index=13346)
Annotation(end_index=13895, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpfee8-ZEjqNrdj25FL2SJcCi2TgAcl2IDA-UceQ8USKAZJsVnKsJsRMj8lJBLH1Q4WHn_1VORv-vrAHdNwz2nd2U-yExB2gEZBTvifHmi7xx41sKYpifkcHs2sig-uKqE7zgI', start_index=13885)
Annotation(end_index=14297, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsWs-ZbVp6ufEQUzeL-4jM2svwMZOd4h86NXs-jTadgn2Z-48bWinE2NERV0DO3fGz-X4FqeOCpKohJfmtAb1xnl4T0BfuzOnooZJ7mzr8je6rWKbwjiIUtocHJPgnw_Y=', start_index=14287)
Annotation(end_index=14827, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_aNvmVkntbkaTwHbYP_FmJGC734MMQSbEk-iLxnyT-Eh1u2KpG_eV78Tvbxq8NEzagcW74IYabYwCZpijxyKFiCsHWSGXW6oAToqngsMjO51O6JzLN5-I4jzIAwKlPF7UcsiitctKH_lZORFRRp7VDFmbpAMZveL3SSSUAB0ft98ZockPz_0orOkoT-6_JbY7LlcSGNZHN4Q3Qtoml5R1jdbfLMq8YPQv7cr1XWA9QJY_4Q==', start_index=14815)
Annotation(end_index=14827, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSJmj2ToHyxcxmorZCiHMZu1aA9AvHeUVAgcy3l5PWsRtHgbQCNOlLMC3Ueu00Ul7GbILdGLba9nluaqrx2afEQni_bvqeEdqzSPX4ah3XriJOtMK1n8ZuTqeg9JVm1Q0jsGapXUrB6FOM4egMuN3RLEDGMUOWjB51bcCIT33PIb6BdxM8VkAvYv4CB8A_-zkS67cSTYRowoA0JyDFSjzN9xoaHRuX3vTUMb4N4NSJtWs=', start_index=14815)
Annotation(end_index=15052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7ELRTSMttl4_HjDzCqrbct6om0cDm7nlmRClI2GnzLMM2TQzWJW3hhTWIII8Dfu16ztcYR8JNPERoyhM9l3-mdaOBK9t9P9ot6dX5WLZDxQSh1gjsiw7ukHfPE_D-33NLgvyMaeVH6-k4BPBRCbSUmu3D5o8AIo6V91aLQnvTHsokyVELRzELg1wF4mv4lIW6hia2Be593tO78255DJhka50X8UZxXKBP50AWdYD1BC0aRiWoLGlgSql8DZqgf9Qh14CIuA==', start_index=15038)
Annotation(end_index=15052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHevl5k-05aVJyTLFQQLwTekeJAkhvpXlnzDkL_j2sC0a7LP2v8t2-Dy97_xak9gv7H3rSfPuFtiSO5DQAUobY6ktmzKJvbE1oViIrenVz1fjTQZ0y4c3jGnQ==', start_index=15038)
Annotation(end_index=15276, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqbS24wD9X4dY6neGSC10B8KkSWdHwBm-Tr9w7oJPa0A0lfXOrd_e-MMg7PVrA7y52grICA09onduvOZAnKLgX7c_jSF5htPNmOckEY6Veb0IuEiWIJc0TTSAeDs0ujjv6aNLg0bDpi_1FKNq-t8ULVZY4EFU5u1CTEirc5w2ketmyJ1okYzkOWDShq6_kwO_LHGc2XmhMIleKARNNBqnBTiwpCU-sIFg1c-0B70YVBPX5_Tl1-9jXgSqfFQ9dztRW0PbmGzLeu__hcYofb4QNR6fLTIW8MyilfPk7UUK-HA==', start_index=15262)
Annotation(end_index=15276, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsWs-ZbVp6ufEQUzeL-4jM2svwMZOd4h86NXs-jTadgn2Z-48bWinE2NERV0DO3fGz-X4FqeOCpKohJfmtAb1xnl4T0BfuzOnooZJ7mzr8je6rWKbwjiIUtocHJPgnw_Y=', start_index=15262)
Annotation(end_index=15498, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4fWmsAKkiO54TsI65_-kHlPoSoAlq8AIbZYXOAUL8VxA316E3q7sOyyRMKDcaBxYnUkl6cvj3qrrFnRWZ9Jd_fZxZHRORYfCCsF441RtJebom_Vq0XMnUp6PrjpvS', start_index=15484)
Annotation(end_index=15498, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHokidy5AnwIWkhWv3EZpL469s7SttvFkl-RU4PWs2qWuKBy5ZXVF2CnInT-khi_IEOskEAgampi8ZcJJN3rsmoQQUWMBreY1cazXtNT3ZO_ki5wJqVqh4g2-0Q1LGhXrutWWNZG6Kn', start_index=15484)
Annotation(end_index=15720, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxLqfV9SDUCCO4fZyVmUk1mncy9OpQnJfdmNrbNTwA2Ix7R3VkijEY5IZrhlpe3FKNjZ1GtDSmhdQ51csybqdzGceqxpTg8YV6jvHW-Lo0tsCkCFVdAbgHb5sfkvgaat_K06nL6CezxqhYCf7Je4SZLUjKS0T_gCy1ecofmhw6-PoZU6ntMuiy_b-pl42pKw5V5nEQxxlia12m7OmWOPTMAv2z8s7TD6g2-loCNWJIuVV4SBF0Q3rhtED5mbLkqN3H4SdHyCAoLQBMr2vopi5vrEU0luRGSCeJK0JqSJViYwLQMhhc8w==', start_index=15707)
Annotation(end_index=15720, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcEdwYc-Hs5hIJ_N86doOWKIpzEk37rfzjtVkTMwXj0MmvLrKSR26qgWWL0Sjz20RGJgEiUoe1LSR5GoUuxEjFG9simCj9HaB3kz-BFWponGFq_3yiv9xFEr1eQK5zoaFRBeq7SoX7SqdNteg=', start_index=15707)
Annotation(end_index=16549, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGK0s6z54nqSpKHGL8UrwDBlmLxLFzKUSQz9_jvD0WTeceYDwhYJT9Kvs2BMlDwJe5o2G_ptFqqTxERlRB8qT-zg9VJUqQf9mu74jBsJpvUraR_9_qGUUti_KoHWJHrfBHgoF2-45f46TaStC2T7KiJmTa64M5k5iwtUWVqeGV-gLPQLDaeC7v1whFm4WahRPkue19qWJtgdR8g8zuJ_pHvvtVqkPUHjKpvxiFPBeX6riKYUuBe013p4TaKWpyseRDjE4JgAbFuUg==', start_index=16536)
Annotation(end_index=16549, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNkQ_nxA-QkEyeDaBv3cZ0gCET8e7t5EC1G6W_FmWp43ao-2bYk3niJEAqUh638boHeterGRRS8_zfsHVIX3yG5CGlXxRQ8QA_PJLmHjxEi78bSfwuJF3qQNm-YoQ=', start_index=16536)
Annotation(end_index=17702, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxLqfV9SDUCCO4fZyVmUk1mncy9OpQnJfdmNrbNTwA2Ix7R3VkijEY5IZrhlpe3FKNjZ1GtDSmhdQ51csybqdzGceqxpTg8YV6jvHW-Lo0tsCkCFVdAbgHb5sfkvgaat_K06nL6CezxqhYCf7Je4SZLUjKS0T_gCy1ecofmhw6-PoZU6ntMuiy_b-pl42pKw5V5nEQxxlia12m7OmWOPTMAv2z8s7TD6g2-loCNWJIuVV4SBF0Q3rhtED5mbLkqN3H4SdHyCAoLQBMr2vopi5vrEU0luRGSCeJK0JqSJViYwLQMhhc8w==', start_index=17693)
Annotation(end_index=17848, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcEdwYc-Hs5hIJ_N86doOWKIpzEk37rfzjtVkTMwXj0MmvLrKSR26qgWWL0Sjz20RGJgEiUoe1LSR5GoUuxEjFG9simCj9HaB3kz-BFWponGFq_3yiv9xFEr1eQK5zoaFRBeq7SoX7SqdNteg=', start_index=17838)
Annotation(end_index=17993, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbE9IQO2Uyhhi8Bi5t2zo_LMYomaNJZ22gpvjRkkNF5faa-c84OfiWZbn0Hn17PkYNZX2LtFEE3hQ2ksi8tIP0_WOt859N779fGr9SjCsr-LEQX36Y0GyljuL8SOx_HA==', start_index=17984)
Annotation(end_index=18032, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkfghdCTkXUjoFVY8gsB0npILuPtU_CB7f1bNy5BYzewirgomeb4e5AeCz5U97oc_TiwS5Oz8TwVFnhPjOuR_ZuHJ7joEf5w4Mu1I-GHb7a5ZsTzUwXxe-mfAwfYzp', start_index=18022)
Annotation(end_index=18070, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEEB07SCNM0wt4WMK4w7qM535fmMezofHikMD-FZEN8RJ8aBtJWj9vburtahCfViebNqzpIm2Xwyl-QDTiIwUj64phkroc3B4bteVufdllFQHmSZDUROGbJpyVZg==', start_index=18061)
Annotation(end_index=18112, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcTpPsSib24dcz3quyNSU7xEmHuJBGVR2iXClZFUPZaKpdyuoFQ3vKced7T7-FhRooNhwL6kYRVM4vs9qGjXXuyWSXuHYXT-_7TNYqkRIx2H0ny5ZVZQ==', start_index=18103)
Annotation(end_index=18140, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGK0s6z54nqSpKHGL8UrwDBlmLxLFzKUSQz9_jvD0WTeceYDwhYJT9Kvs2BMlDwJe5o2G_ptFqqTxERlRB8qT-zg9VJUqQf9mu74jBsJpvUraR_9_qGUUti_KoHWJHrfBHgoF2-45f46TaStC2T7KiJmTa64M5k5iwtUWVqeGV-gLPQLDaeC7v1whFm4WahRPkue19qWJtgdR8g8zuJ_pHvvtVqkPUHjKpvxiFPBeX6riKYUuBe013p4TaKWpyseRDjE4JgAbFuUg==', start_index=18131)
Annotation(end_index=18257, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsWs-ZbVp6ufEQUzeL-4jM2svwMZOd4h86NXs-jTadgn2Z-48bWinE2NERV0DO3fGz-X4FqeOCpKohJfmtAb1xnl4T0BfuzOnooZJ7mzr8je6rWKbwjiIUtocHJPgnw_Y=', start_index=18247)
Annotation(end_index=18302, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpfee8-ZEjqNrdj25FL2SJcCi2TgAcl2IDA-UceQ8USKAZJsVnKsJsRMj8lJBLH1Q4WHn_1VORv-vrAHdNwz2nd2U-yExB2gEZBTvifHmi7xx41sKYpifkcHs2sig-uKqE7zgI', start_index=18292)
Annotation(end_index=18408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHokidy5AnwIWkhWv3EZpL469s7SttvFkl-RU4PWs2qWuKBy5ZXVF2CnInT-khi_IEOskEAgampi8ZcJJN3rsmoQQUWMBreY1cazXtNT3ZO_ki5wJqVqh4g2-0Q1LGhXrutWWNZG6Kn', start_index=18398)
Annotation(end_index=18454, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHokidy5AnwIWkhWv3EZpL469s7SttvFkl-RU4PWs2qWuKBy5ZXVF2CnInT-khi_IEOskEAgampi8ZcJJN3rsmoQQUWMBreY1cazXtNT3ZO_ki5wJqVqh4g2-0Q1LGhXrutWWNZG6Kn', start_index=18444)
Annotation(end_index=18523, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpp6ofZIpNHVFQy3fsjmGfpu-m1h4dzus3TpVaEB3-QwTURb_zpjCnvA3ytY4bYfAJATZT1fucqGhMkEDESGqlxdWS0XxKzHH8gsxElb7KhT5ge_RplerELg==', start_index=18513)
Annotation(end_index=18551, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_aNvmVkntbkaTwHbYP_FmJGC734MMQSbEk-iLxnyT-Eh1u2KpG_eV78Tvbxq8NEzagcW74IYabYwCZpijxyKFiCsHWSGXW6oAToqngsMjO51O6JzLN5-I4jzIAwKlPF7UcsiitctKH_lZORFRRp7VDFmbpAMZveL3SSSUAB0ft98ZockPz_0orOkoT-6_JbY7LlcSGNZHN4Q3Qtoml5R1jdbfLMq8YPQv7cr1XWA9QJY_4Q==', start_index=18542)
Annotation(end_index=18659, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFm60LkeEU_kRf4jXowgYcDb0XmtItrFcCITaSXFEnCecVpckCRxIJyNwH1BlzV7LxGAqnTJuHSUk_ojrtgBowxTxHbp95Fl2vn9WnR_XVTXk3RYI_AW_Prec81HM=', start_index=18649)
Annotation(end_index=18698, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBVMNfqCL_x2EHnhAIrT1s0dFe_DP1QtN_wTcDt-QNri0Q1sjGbNANFjgQdZ6Cjs0cue8fxQCpM8KdpWlh9iOAtjNC0JhyjF__yBtRFlZVaPDv_Y20XwuA7F3FZLbHJzj1gGWmlzEWydGXijalLEtPRrJtrH-qjO0kmWg_ryCSVuYhzjlYyXm6HIu2c-edoR4Ww5EqbXpHNEtwxuc=', start_index=18689)
Annotation(end_index=18749, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7ELRTSMttl4_HjDzCqrbct6om0cDm7nlmRClI2GnzLMM2TQzWJW3hhTWIII8Dfu16ztcYR8JNPERoyhM9l3-mdaOBK9t9P9ot6dX5WLZDxQSh1gjsiw7ukHfPE_D-33NLgvyMaeVH6-k4BPBRCbSUmu3D5o8AIo6V91aLQnvTHsokyVELRzELg1wF4mv4lIW6hia2Be593tO78255DJhka50X8UZxXKBP50AWdYD1BC0aRiWoLGlgSql8DZqgf9Qh14CIuA==', start_index=18739)
Annotation(end_index=18887, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIu8A9eDBTX5ZJc7s0ChB6eXrddwIk49Ugii4gL0Vctri4uvs-JbZm1-rKtLWdXe_lTLSddssgT6O7m15oCzmDemfsva1vGCByTQSJcl5HR8rN7BfaXw==', start_index=18877)
Annotation(end_index=18916, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0QY6I4reNMv9VNMDjdhR5yuVFiVztC_53EGSce0bouJImSeeGyec5z5viqNQveZK0-awvTfArlaNCNP3u9QH18fg2KsyYLwyV-czYUYJo14UdTLz1VN1y2FM1B65yoqtDlcXvxJBPnl_VeNsmL7knoARY76RXYhfPyDRWZPIV_jk7Uk42YlcbP5HgOY7vP7XDIy93t_6H5TFUFwEiId-KUQH3_NwmEI8REbsmnypN1SG7J10It6VSx1A0vB7jx4q99yj2KiePEuVlV_5-kzCvBA==', start_index=18906)
Annotation(end_index=18974, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCaJwcSFjez0CaEft_zJte87bccSb_RkLVJOTxdPIFxOSo5lbHfMgKr8LoZq7AhoNVOru4zQqBOCY0nXk3Pkrt35tkPTssqngBZyUjchtkZsgVneTD4XFoo7WS1uhx6qiIUEk=', start_index=18964)
Annotation(end_index=19061, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSJmj2ToHyxcxmorZCiHMZu1aA9AvHeUVAgcy3l5PWsRtHgbQCNOlLMC3Ueu00Ul7GbILdGLba9nluaqrx2afEQni_bvqeEdqzSPX4ah3XriJOtMK1n8ZuTqeg9JVm1Q0jsGapXUrB6FOM4egMuN3RLEDGMUOWjB51bcCIT33PIb6BdxM8VkAvYv4CB8A_-zkS67cSTYRowoA0JyDFSjzN9xoaHRuX3vTUMb4N4NSJtWs=', start_index=19052)
Annotation(end_index=19159, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyu-MsdRMwFlZQMR3xK-pe50Vey7Pt-7HBkryVh7IYxJWm8BKX-ZMpmGaVRndOg_IdhOVFC7GMwJrCyT9Jhom5HecZrgmYbgkzFVT8OI1nbWq7N_KvCA==', start_index=19150)
Annotation(end_index=19188, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_Zb6M8IyGyUpDI2Z88wVpo5PiqmuLTPpukwG94oFw5pm-KQC3ShzqcbtdnKAdKKtwNSyfVCV1CU0whLPU9tkS5em332wX_mwX20br2BSAUOPZV-Rg5dEnSpMRIcB0EQw_RTUzPHnI3Mg_VbHPCELOKAtt', start_index=19178)
Annotation(end_index=19274, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqbS24wD9X4dY6neGSC10B8KkSWdHwBm-Tr9w7oJPa0A0lfXOrd_e-MMg7PVrA7y52grICA09onduvOZAnKLgX7c_jSF5htPNmOckEY6Veb0IuEiWIJc0TTSAeDs0ujjv6aNLg0bDpi_1FKNq-t8ULVZY4EFU5u1CTEirc5w2ketmyJ1okYzkOWDShq6_kwO_LHGc2XmhMIleKARNNBqnBTiwpCU-sIFg1c-0B70YVBPX5_Tl1-9jXgSqfFQ9dztRW0PbmGzLeu__hcYofb4QNR6fLTIW8MyilfPk7UUK-HA==', start_index=19264)
Annotation(end_index=19337, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqZvp6W3m4YL369BS07Lhnd8gUfVX_aAsy-n60aeF3E_whYYXakXqdYr4Xm-0mknLm-ZEdj0HrU8z0M-A2cELMhqguAxDgq1BUGIm2GBOsvG0s5XtNwrqqHsG51J5b6GxkPYJtgIe9N5Cfiihg63Mn7BKJRTx6l_U5rrmy2puSmKkqsGcq2zVy3sBTvOExc49RDBM=', start_index=19327)
Annotation(end_index=19403, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsWs-ZbVp6ufEQUzeL-4jM2svwMZOd4h86NXs-jTadgn2Z-48bWinE2NERV0DO3fGz-X4FqeOCpKohJfmtAb1xnl4T0BfuzOnooZJ7mzr8je6rWKbwjiIUtocHJPgnw_Y=', start_index=19393)
Annotation(end_index=19448, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaldcXOu4Mm4BezJv71IGgmfO-gKA5PzjC1z32ZI-VLVZr73FK0uZwQA0pGVSq412udG8xPhcerfOPQN6byqLu8ISKafZrrdOJiQ3vXdhGgnUNdQr5nQ==', start_index=19438)
Annotation(end_index=19477, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZ-NnLNyUrc27y95cxQWL0T6NOaTJLBKqrVxdx6CHBrbGQOWWZEKhDhBK8URYY-ZOBzc1uSrzO64LXiFxRE9Z9VOCB8aIsc8oD2VEPZrNYjMEbvM-B1y8=', start_index=19467)
Annotation(end_index=19512, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHevl5k-05aVJyTLFQQLwTekeJAkhvpXlnzDkL_j2sC0a7LP2v8t2-Dy97_xak9gv7H3rSfPuFtiSO5DQAUobY6ktmzKJvbE1oViIrenVz1fjTQZ0y4c3jGnQ==', start_index=19502)
Annotation(end_index=19543, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6GPGwt55k-r2C2Ic8i55oBNSFVE3evzjIvgmmNYnAN2wUus8swUcYfgdaj5MIPz_TvUtlo71ffqTjqOI7k-70SfEINZER9NFfHFZ3IcqLkmBht4HwXmI-1nyTjeA9YMVO13db6cErjipr-lvjgG2UWXU8WDPwKjDMU-JngYZ35bx0uXIrsbord44Zve3QlOVWDaIWK6VA0HgKX8UgWvLZ6DfX_09tAf7l2GicrvHx3K2BVcjGbHxS8t3G2Q==', start_index=19533)
Annotation(end_index=19652, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0QY6I4reNMv9VNMDjdhR5yuVFiVztC_53EGSce0bouJImSeeGyec5z5viqNQveZK0-awvTfArlaNCNP3u9QH18fg2KsyYLwyV-czYUYJo14UdTLz1VN1y2FM1B65yoqtDlcXvxJBPnl_VeNsmL7knoARY76RXYhfPyDRWZPIV_jk7Uk42YlcbP5HgOY7vP7XDIy93t_6H5TFUFwEiId-KUQH3_NwmEI8REbsmnypN1SG7J10It6VSx1A0vB7jx4q99yj2KiePEuVlV_5-kzCvBA==', start_index=19642)
Annotation(end_index=19710, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHM5ebRiXgPEx8THpfiqhUOsDbUN9VsgLKKZmKnROsUV-lwhZjWQI7R-bf_Ub12ZwgD9meU6JPHAfbuGRwO14AfGNndgX5Oby9K3Hg5k9u90h9yDr-EAiN91_FCPBr', start_index=19700)
Annotation(end_index=19751, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXYsFzjUj8aB6nnzeX9O3kcFZ8IEAQmrQcoxy-wNFgJsVU3BrLPRoRhykiPpDbcW4NQ3GdTbdMmBRDMt2z5n9EZ3XE9dSBQXtNdiwzz5bj_4QjWvjBPWIpexWSLp9DLuj1KivGpXsxttSr0J9CZ0-zbcu9Gzj1f5E4Qv5vhYAToiOpfmiRgUT1MLy59OXDvA==', start_index=19741)
Annotation(end_index=19788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLAudLrQ3B28eeBL_8G08jJft6Fu8_VptiNORfLYqyIfVoEZRU0L3EdXpAolAikjM9JEIHqlZAj5fiRLBcSOPWMBG2r_jvBzZhDWT9oKMfkuRwCbsW6Lllrxycwom7hYKXycB5A4oOHPNo--sC283m1jY2FwU9-6-FxgUzBd210gBwMqjUbf1oOTAe-3ZmB6qYrNh95lwV-NqYi-wxZA_5baJ8nas0sUII5UJlpvnYdcsZ1HjKXbM9Lavm9M1qHPyXtkGdCSzjc5K85y9wLtZPDLP5mnyv', start_index=19778)
Annotation(end_index=19833, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNkQ_nxA-QkEyeDaBv3cZ0gCET8e7t5EC1G6W_FmWp43ao-2bYk3niJEAqUh638boHeterGRRS8_zfsHVIX3yG5CGlXxRQ8QA_PJLmHjxEi78bSfwuJF3qQNm-YoQ=', start_index=19823)
Annotation(end_index=19873, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4fWmsAKkiO54TsI65_-kHlPoSoAlq8AIbZYXOAUL8VxA316E3q7sOyyRMKDcaBxYnUkl6cvj3qrrFnRWZ9Jd_fZxZHRORYfCCsF441RtJebom_Vq0XMnUp6PrjpvS', start_index=19863)
Annotation(end_index=19914, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELNzIzFoAAA5eWgoNuuyaCdcK1bkGJxVGVxhn1QSTjAAXOzjFnMni_0DdcYPOOPCZ0e8gMWlfuYF5gsccYS9oh20gHM-XbM0_mfXC11oxFPDhpntK-UuqI4nogXdfA_WDK7eaUcIBT_iD_Dnk6wmzTw30UQF675msLv_p_z42c_zuojk3bh9-0MGvs3MMdmK_TJzIHmenTqTzUHv5zQhRruTSsLzw8JRo3NnOWiqeCREWNUer05mCLqUms4sayatjITWmIWkHxE1o=', start_index=19904)

## Sources
