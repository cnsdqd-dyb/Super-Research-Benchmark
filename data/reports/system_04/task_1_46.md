# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** adaefbd8 | **Time:** 5320.03s | **Cost:** $1.13755
--------------------------------------------------------------------------------

# By what process does the responsibility assignment matrix in AI systems achieve dynamic equilibrium via Markov decision processes?

### Key Points
*   **Dual Interpretation of "RACI" in AI:** The query touches upon two distinct but converging concepts: the traditional **Responsibility Assignment Matrix (RACI)** used in project governance, and a specific, novel technical framework titled **RACI (Resource-Aware Cooperative Inference)**. The latter explicitly uses Markov Decision Processes (MDPs) to achieve dynamic equilibrium in edge computing.
*   **The Technical Process (RACI Framework):** In the context of distributed AI (specifically Deep Neural Network inference), the "RACI" framework achieves dynamic equilibrium by modeling the system as a **Constrained Markov Decision Process (CMDP)**. The process involves agents observing system states (bandwidth, device capability), taking actions (partitioning models, assigning "responsibilities" for computation), and receiving rewards (latency, accuracy).
*   **Dynamic Equilibrium via RL:** The system reaches dynamic equilibrium through **Deep Reinforcement Learning (DRL)** algorithms, such as **LSTM-TD3** or **PPO**. These algorithms allow the system to continuously adjust task assignments in response to stochastic environmental changes (e.g., network fluctuations), balancing the trade-offs between inference speed, accuracy, and energy consumption.
*   **Role Assignment in Multi-Agent Systems (MAS):** Beyond the specific RACI framework, general AI systems use MDPs to automate the "Responsibility Assignment Matrix" by treating role allocation as a sequential decision problem. Agents dynamically switch roles (e.g., from "worker" to "manager") based on reward signals to maximize collective utility, stabilizing the system into a Nash equilibrium or a cooperative optimum.
*   **Organizational Governance:** In human-centric AI project management, the Responsibility Assignment Matrix is evolving from a static artifact into a dynamic tool. While less mathematical than the technical framework, modern governance uses "dynamic equilibrium" concepts to balance agile adaptability with rigid safety protocols, ensuring clear accountability (the "A" in RACI) amidst the volatility of AI development.

---

## 1. Introduction

The intersection of **Responsibility Assignment Matrices (RAM)**, **Artificial Intelligence (AI)**, and **Markov Decision Processes (MDP)** represents a sophisticated frontier in both computational systems engineering and organizational theory. The user's query identifies a complex mechanism where the static concept of "assigning responsibility" is transformed into a dynamic, mathematically optimized process.

Research indicates this transformation occurs through two primary pathways. First, and most literally, recent literature (2024-2025) has introduced a technical framework explicitly named **RACI (Resource-Aware Cooperative Inference)**. This framework utilizes MDPs to dynamically assign computational responsibilities across heterogeneous edge devices, achieving an equilibrium between resource usage and performance [cite: 1, 2].

Second, in the broader field of **Multi-Agent Systems (MAS)**, the abstract concept of a Responsibility Assignment Matrix is operationalized as a **Role Assignment Matrix**. Here, MDPs serve as the governing logic that allows autonomous agents to dynamically discover and adopt roles, ensuring the system maintains equilibrium (stability and efficiency) despite environmental stochasticity [cite: 3, 4, 5].

This report provides an exhaustive analysis of these processes, detailing the mathematical formulations, the algorithmic drivers (such as Reinforcement Learning), and the systemic implications of automating responsibility assignment in AI.

---

## 2. Theoretical Foundations

To understand the process by which a Responsibility Assignment Matrix achieves dynamic equilibrium via MDPs, one must first deconstruct the constituent theories and how they are synthesized in modern AI architectures.

### 2.1 The Responsibility Assignment Matrix (RAM/RACI)
Traditionally, a RAM is a linear responsibility chart used in project management to define the participation of various roles in completing tasks. The most common variant is **RACI** (Responsible, Accountable, Consulted, Informed) [cite: 6, 7].
*   **Responsible (R):** The entity that performs the work.
*   **Accountable (A):** The entity ultimately answerable for the work (final decision authority).
*   **Consulted (C):** Subject matter experts who provide input.
*   **Informed (I):** Stakeholders notified of outcomes.

In **static systems**, this matrix is defined once. In **AI systems**, particularly autonomous ones, "responsibility" refers to the execution of specific computational sub-tasks (inference, data processing, actuation). Because the environment (network latency, data arrival rates) is volatile, a static assignment fails. The matrix must therefore become a **dynamic variable**, updated in real-time [cite: 8, 9].

### 2.2 Markov Decision Processes (MDP)
The MDP is the mathematical engine used to automate this dynamic assignment. An MDP is defined by the tuple $\langle S, A, P, R, \gamma \rangle$:
*   **State ($S$):** The current status of the AI system (e.g., "Device A is overloaded," "Bandwidth is low").
*   **Action ($A$):** The decision to assign a specific responsibility (task) to a specific agent (node).
*   **Transition Probability ($P$):** The likelihood that assigning Task $X$ to Agent $Y$ will lead to a new system state $S'$.
*   **Reward ($R$):** A scalar feedback signal indicating the success of the assignment (e.g., "Low Latency = +10", "High Energy Cost = -5").
*   **Discount Factor ($\gamma$):** The weight given to future rewards versus immediate ones [cite: 10, 11, 12].

### 2.3 Dynamic Equilibrium in AI
In cybernetics and systems theory, **dynamic equilibrium** refers to a state where a system maintains stability and function despite continuous external fluctuations [cite: 8, 13]. In the context of AI and MDPs, this is achieved when the **Policy ($\pi$)**—the rule mapping states to actions—converges to an optimum. The system continuously adjusts its "Responsibility Matrix" (actions) to counteract disturbances (state changes), thereby maintaining a steady flow of value (reward maximization) [cite: 8, 14].

---

## 3. The Technical Process: The RACI Framework
**Source Synthesis:** [cite: 1, 2, 15]

The most direct answer to the query lies in the **RACI (Resource-Aware Cooperative Inference)** framework. This specific AI architecture was developed to solve the problem of running complex Deep Neural Networks (DNNs) on resource-constrained edge devices (like IoT sensors or mobile phones).

### 3.1 The Problem: Static vs. Dynamic Assignment
Running a massive AI model on a single weak device causes high latency. Splitting the model across multiple devices (Cooperative Inference) is the solution. However, a static assignment of model layers to devices fails because:
1.  **Heterogeneity:** Devices have different computing powers.
2.  **Stochasticity:** Wireless bandwidth varies unpredictably.
3.  **Complexity:** DNN layers have different computational requirements.

### 3.2 The Process of Achieving Equilibrium
The RACI framework achieves dynamic equilibrium by treating the "assignment of model layers to devices" as a sequential decision problem solved via MDPs.

#### Step 1: State Space Construction ($S$)
The system continuously observes the environment. The state space is a high-dimensional vector representing:
*   **Network Conditions:** Current bandwidth between devices.
*   **Device Status:** Available computational power (FLOPS), memory usage, and battery level.
*   **Task Characteristics:** The specific requirements of the DNN layers (e.g., convolution depth, data size) [cite: 2, 15].

#### Step 2: Action Space Definition ($A$)
The "Responsibility Assignment" is the action. The agent must decide:
*   **Model Partitioning:** Where to cut the neural network (e.g., after Layer 5).
*   **Workload Allocation:** Which device is **Responsible (R)** for computing the first partition, and which is **Responsible** for the second.
*   **Offloading Decisions:** Whether to process locally or transmit data to a neighbor [cite: 1, 15].

#### Step 3: The Reward Function ($R$)
To drive the system toward equilibrium, the reward function is crafted to balance conflicting objectives. The reward $r_t$ is typically defined as a weighted sum of:
*   **Negative Latency:** Minimizing the time to result.
*   **Accuracy:** Maintaining high inference precision.
*   **Energy Efficiency:** Penalizing excessive battery drain.
*   **Formula:** $R = \alpha \cdot (-Latency) + \beta \cdot Accuracy - \gamma \cdot Energy$ [cite: 1, 16].

#### Step 4: The Learning Algorithm (Deep Reinforcement Learning)
Because the state space is too large for exact calculation, the system uses **Deep Reinforcement Learning (DRL)**.
*   **Multi-Agent Cooperation:** The framework often employs a multi-agent approach where a **Model Agent** (deciding partitions) and a **Workload Agent** (deciding assignments) co-train.
*   **Algorithms:**
    *   **PPO (Proximal Policy Optimization):** Used for its stability in continuous action spaces [cite: 14, 17].
    *   **LSTM-TD3:** A specialized algorithm combining **Long Short-Term Memory (LSTM)** networks with **Twin Delayed DDPG (TD3)**. The LSTM component predicts future network states (handling the "dynamic" aspect), while TD3 optimizes the assignment policy [cite: 18, 19, 20].

#### Step 5: Achieving Dynamic Equilibrium
The "equilibrium" is reached when the DRL agents converge on a policy that can instantly adapt to perturbations.
*   *Scenario:* If bandwidth suddenly drops (perturbation), the LSTM predicts a high latency cost for offloading. The Policy ($\pi$) immediately shifts the "Responsibility" of the next layer computation back to the local device (Action).
*   *Result:* The system maintains its performance targets (latency/accuracy) despite the environmental change. This self-correction *is* the dynamic equilibrium [cite: 1, 15].

---

## 4. The General Process: Role Assignment in Multi-Agent Systems (MAS)
**Source Synthesis:** [cite: 3, 4, 5, 21]

Beyond the specific "RACI Framework," the broader field of Multi-Agent Systems (MAS) utilizes MDPs to automate the concept of a Responsibility Assignment Matrix (often called a **Role Assignment Matrix** or **T-Matrix**).

### 4.1 The Role Assignment Matrix (RAM)
In MAS, a Role Assignment Matrix $T$ is defined as an $m \times n$ matrix where $T_{ij} = 1$ if Agent $i$ is assigned to Role $j$, and 0 otherwise [cite: 4, 5].
*   **Roles:** Abstract definitions of responsibilities (e.g., "Scout," "Attacker," "Defender" in a robot soccer team; or "Data Collector," "Processor" in a sensor network).
*   **Agents:** The autonomous entities.

### 4.2 The Dynamic Role Discovery Process
Static role assignment is insufficient for dynamic environments. The process of achieving equilibrium involves **Dynamic Role Discovery** via MDPs.

#### Process Flow:
1.  **Decomposition:** The global goal (e.g., "Win the game" or "Maximize throughput") is decomposed into sub-tasks associated with roles [cite: 3].
2.  **Observation:** Agents observe the global state $S$ (e.g., enemy positions, server loads).
3.  **MDP Policy Execution:** Each agent utilizes a policy $\pi(a|s)$ to select a role. This is a "meta-action."
    *   *Example:* An agent observes it is close to the ball (State). Its policy dictates it should switch its Role from "Defender" to "Attacker" (Action).
4.  **Matrix Update:** The global Role Assignment Matrix changes. This reconfigures the responsibilities of the entire swarm.
5.  **Equilibrium Selection:**
    *   In **Game Theoretic** terms, the system seeks a **Nash Equilibrium** where no agent can improve the collective reward by unilaterally changing its role [cite: 22].
    *   **Regularization:** To prevent chaos (agents constantly switching roles, preventing equilibrium), regularizers are added to the MDP reward function to penalize frequent role changes. This forces the system into a *stable* dynamic equilibrium rather than an oscillating one [cite: 3].

### 4.3 E-CARGO Model
The **E-CARGO** (Environments, Classes, Agents, Roles, Groups, and Objects) model is a formal methodology used here. It treats the Role Assignment Matrix as an optimization variable.
*   **Mechanism:** The system solves a linear programming problem or uses RL to maximize the "Group Efficacy" defined by the matrix.
*   **Dynamic Adjustment:** As agents' capabilities (e.g., battery, sensor health) degrade (State transition), the MDP re-solves the assignment matrix to maintain the highest possible efficacy (Equilibrium) [cite: 4, 5].

---

## 5. Algorithmic Enablers: How the Math Works
The "process" is fundamentally algorithmic. The following mechanisms are cited as the drivers of this dynamic equilibrium.

### 5.1 LSTM-TD3 (Long Short-Term Memory + Twin Delayed DDPG)
This is a critical algorithm for achieving equilibrium in environments with time-dependent dynamics (like network traffic).
*   **LSTM Component:** It acts as the "predictor." It analyzes the sequence of past states to predict future conditions (e.g., "Traffic will spike in 5ms"). This allows the Responsibility Matrix to be updated *proactively* rather than *reactively* [cite: 18, 19, 20].
*   **TD3 Component:** It acts as the "optimizer." It is an Actor-Critic method.
    *   **Actor:** Proposes the specific offloading/assignment configuration (The Matrix).
    *   **Critic:** Evaluates the potential long-term reward of that configuration.
    *   **Twin Delayed:** Uses two critics to prevent overestimating the value of an action, ensuring the equilibrium reached is robust and not a local optimum [cite: 18].

### 5.2 Constrained MDPs (CMDP)
Standard MDPs maximize reward. However, AI systems often have hard constraints (e.g., "Latency must be < 100ms").
*   **Process:** The problem is formulated as a CMDP.
*   **Lagrangian Relaxation:** The constraints are converted into penalty terms in the reward function.
*   **Equilibrium:** The system oscillates between satisfying the constraint and maximizing the reward until it finds a saddle point (equilibrium) where the constraints are met with optimal performance [cite: 1, 16].

---

## 6. Organizational Governance: The Human-AI Interface
**Source Synthesis:** [cite: 8, 9, 21, 23, 24]

While the technical frameworks automate responsibility assignment *within* the software, the user's query also touches upon how these matrices govern the *human-AI* relationship.

### 6.1 Dynamic Governance
In traditional management, a RACI matrix is a static document. In AI projects, the "dynamic equilibrium" refers to the organization's ability to adapt its governance structure to the volatility of AI behavior.
*   **The Process:** Management Control Systems (MCS) monitor environmental factors (regulations, model drift).
*   **Adaptation:** When the environment changes (e.g., a new bias is detected), the "Responsibility" for oversight might dynamically shift from the "Developer" to the "Ethics Committee."
*   **AI as a Stakeholder:** Advanced governance models now include the AI agent itself in the RACI matrix (e.g., AI is "Responsible" for execution, Human is "Accountable" for the outcome) [cite: 21, 25].

### 6.2 Algorithmic Management
Emerging research suggests using the same MDP logic to assign tasks to *humans* in a mixed human-AI team.
*   **Mechanism:** The AI monitors the "State" of human workers (fatigue, workload).
*   **Action:** It updates the Responsibility Assignment Matrix to re-route tasks to underutilized humans or automated agents.
*   **Equilibrium:** The system balances human well-being with process efficiency [cite: 21].

---

## 7. Conclusion

The Responsibility Assignment Matrix in AI systems achieves dynamic equilibrium via Markov Decision Processes through a cycle of **State Observation**, **Policy-Driven Assignment**, and **Reward-Based Adaptation**.

1.  **Formalization:** The abstract concept of "responsibility" is quantified as a discrete action within an MDP (e.g., assigning a tensor operation to a GPU, or a role to an agent).
2.  **Optimization:** Deep Reinforcement Learning algorithms (specifically **LSTM-TD3** and **PPO**) explore the vast space of possible assignment matrices.
3.  **Stabilization:** By incorporating predictive elements (LSTM) and stability mechanisms (Twin Critics, Regularizers), the system converges to a policy that maintains optimal performance (Equilibrium) despite stochastic disruptions.

This process transforms the RAM from a static project management artifact into a living, breathing algorithmic engine that powers the efficiency and adaptability of modern AI systems, particularly in edge computing and multi-agent environments.

---

## 8. References

*   **[cite: 8]** *Responsibility Assignment Matrix in AI systems dynamic equilibrium.* (Source 1)
*   **[cite: 6]** *Responsibility Assignment Matrix.* (Source 2)
*   **[cite: 14]** *Distributed multi-agent scheduling architecture (DMASA).* (Source 11)
*   **[cite: 3]** *Dynamic role discovery and assignment in multi-agent task decomposition.* (Source 13)
*   **[cite: 22]** *Equilibrium Selection for Multi-agent Reinforcement Learning.* (Source 14)
*   **[cite: 10]** *Planning with Markov Decision Processes: An AI Perspective.* (Source 17)
*   **[cite: 11]** *Optimal MDP Decision Trees.* (Source 20)
*   **[cite: 23]** *An Operational Taxonomy of AI Alignment Approaches.* (Source 21)
*   **[cite: 12]** *Multi-Agent Reinforcement Learning for Traffic Signal Control.* (Source 22)
*   **[cite: 1]** *RACI: A Resource-Aware Cooperative Inference Framework on Heterogeneous Edge Devices.* (Source 25)
*   **[cite: 13]** *Dynamic equilibrium and equifinality in open systems.* (Source 31)
*   **[cite: 8]** *Management Control Systems (MCS) and RAM.* (Source 33)
*   **[cite: 9]** *How to Create a Responsibility Assignment Matrix (RAM) in 2025.* (Source 35)
*   **[cite: 7]** *RACI Matrix: Responsibility Assignment Matrix Guide.* (Source 36)
*   **[cite: 4]** *Role-Based Collaboration and E-CARGO.* (Source 45)
*   **[cite: 5]** *An Efficient Outpatient Scheduling Approach (Group Role Assignment).* (Source 49)
*   **[cite: 21]** *AI Responsibility tool: RACI Matrix and Multi-Agent Systems.* (Source 56)
*   **[cite: 1]** *RACI: A Resource-Aware Cooperative Inference Framework.* (Source 64)
*   **[cite: 16]** *DeepEdge: A Deep Reinforcement Learning based Task Orchestrator.* (Source 79)
*   **[cite: 2]** *RACI: A Resource-Aware Cooperative Inference Framework (IEEE).* (Source 82)
*   **[cite: 15]** *RACI Framework Analysis (IEEE PDF).* (Source 83)
*   **[cite: 5]** *E-CARGO and Role Assignment Matrix.* (Source 87)
*   **[cite: 17]** *Solving non-permutation flow-shop scheduling problem via DRL.* (Source 89)
*   **[cite: 18]** *Learning-based deep neural network inference task offloading (LSTM-TD3).* (Source 90)
*   **[cite: 19]** *Trajectory Prediction and Decision Optimization (LSTM-TD3).* (Source 91)
*   **[cite: 20]** *Integrated LSTM-TD3 Framework for UAV-Assisted VEC.* (Source 92)

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNygc_KBTx7eoURg05Q8SmQPRnIx_3zkCcQ8BJOiXhfs_HkRh3Wxy-HZtg_8wT55lyyZNWDFrAOBVbJnclKwUBfrQUafbqHghh3PVowj97CXFBjwuoKZXuQgxb4q4RhazdVPaiOh_GKeN3PEvN2iKyZJj2JhgIngqnp73cAjONMJBpEzEr4mpTbs6m_p6ZtO6klP5GBVk6uUyEXEO2biZsQu83XknJ8SDkjefe95R13fG7ervTNcWtaUlcjiw=)
2. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFXQG2aL-19by9ZTWEULStW9PkWu-s1y4sWY2eC4gLGOII0BVJCW7MFzqGhdZD6oWwua9o1tAQFMBdFY6ILQZF_DsgwMazrxBjVIXsROVSI_Y0RFG9frzTc6DLZYV8WNDoXPAW)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN7FN9EvLddbn1m-f9yUgzlVWEylvPKU3xnPzh2TPyr-DNq4cVAxCauaWGs4-J8Ggkqi8lOmSh2ZpmSHClziUZNhd7m-KoeieI4Xx3zdglAVAoDuENY7tsUgv366F5fAQGwg__AP1VDoIJ0--VM5RL1ovjrPJZqt6gL0FZjZBqiGGx9hB5zYSmSkujtZMqmbBugZtBTN7kxiEVHTLVZo6y8lH9cs3fLTqYAMYPBd63UQ==)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC5iDBwlEbo-WxdAZEwzKdDsnGtHuEXSHmjt4wksyekbrnWpyCdZGlP7PRxJSSxj8RbUlZeZM3oubTHmyf5eBUi4ARAJUNapvVJspDVgyIsr012ncZDDTNa1V986Uh4Bn3t40-A5J_es_SmY6HUkyG6t1HINzXhjohGV1CjHT_rjyLC-2e2r8swkzi0OrixtuHPFgG4qWaObNK6D2OecgJu5Swfn9kONayL8MeL2GtV51fU5zxLPMPkZkUCc_wAuBPfw3DNDYOPcn7ao-U0P1duR0csVo_IsuqvGfOb81cjJUTXCVGefulj9P2Anmq3cOad201kkhRe5hUHSmlEf1uf7Wls7r822VsZ2Np4-44xEjpCr5lr8ZK_NjxeJU9yA==)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjVobRew9Ho68B-kl9eUGRu_ScxuDFgECwVkGy1-r8fnBQ3H-DbT6XCmKdM9XZn6azB16VAKOZ-My-EFkDIX9HjBrAkqIdobIWtu9mQ9ydKLbcvcznZZO1wvF-XDZDxIpVV65O8a8UZ10FxNO_JXtk8P2BR4vGg2vVmd59K3l0zHMtEdGGjelB1hrJg8gNXuYaSejW)
6. [theintactone.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDLvU1dcJJnSu3oMuTrMoXoZgx5hCJG3aKreR3lPmUyi7LR_rjhcdUEAc8lVTNDzAjopdFk5gWtWADTt_vBXnRi4KZi1PCGiAXYumYp_jg-96oLmxrzPkd3DNIEu87nRWR-LMRROw9_EFBFdXF5jWHkCm3uigfcx0-KXM=)
7. [project-management.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyz-0bZGzhw8mw3GsVaBwP1RzXGq72SpfsQ21W5hkMuqO8Wu7p72doASEjsfAK61b4v0A-MTMpRubzA8QWyUVMaJS93eIbYHJXECO6Z7j99sretmLfNipqDGJZ9REXCdS6wpzDwmjwhRuskRvpx3rLLMOZQBlXqBNgRrCTs0-QkCFashzhe-4vaEF6iuUqkNY=)
8. [tum.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXSGX1AVfI9a1-qTO0kyep1kKxxtWPzZkpAwD9FnqfQY_0LSJReDuxJUcarwKr9zxZgTnOnnnxjP1bxTIJSu-MeGTsWr-q0Ub6pv62DervGQQb_WA2_V9yrt9hO8MV-Mm9HRuRY-0NyQ==)
9. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE73FZX5KIS1uHaH4krPYcc6vjlyevl8Z1tyhNI71lYBiYygMNTKI4_4P9Z3rZlFGQ6mi9OI-jwBxLYqS99vqIMPY11i5mR39q_3yX1GaplV0wiLNkgSEDvJBmkRlMGM0mrjeEDlfjNl_hq-0Q6JNMBRXv9g9fAL8ceQ_TZ-SZm1EUnsZHo9ycMFi8CROx6q1loOU0b3jKUUiijq3rAJgVpZozphVM=)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWownjXCxYF9c_F4CNyq-ciqmHKfTN_7Yzc9b7bOqgsGm540HW4Z0_nExcsQ6zpCgqJ70IH-pNFo4yYJe2kBM4MGJSO48wd9mr2iQF9uZ8Cev0td4eU9Ltju2Xaw4eQ-guUOinxVxlK8f7hMLxfXIEBJbiiykGQe8pdA_HWzpnWitGexmIppesKqumLlkBj-bMh6rszZeXgth5xVD1cdi6JTY=)
11. [ijcai.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDRvIMN67p9xEKv2ZRqfx1_OFF2dwqah5s0BWvhjNNR7QGyF64WIVXn7DKZb7yCa7WhMb9oa9wM3p1IxeM9iBbhjeCNXIOKIRI83gzsaxo8fWMLWoJ6uFGgwJqlXmWZ-Fn-fxneA==)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNd0PqVG7uvW3uBPurb_HTF10Bimzr8EtRhpzCUw9uf63bWlfnAq_mer_XtRTeU7d9sZA51Tf3Aff45gSvkvQRFxXF76Et9_85Z2Ykye2l1vlUnd3Wf3v0MiPIrmgsBRHspNq_SVpPwLkU-AdVkQYRHtLlsNKgfPNJDNKB-eQyxZCCKSCSr7wiNK5Hx2EAeTPgWZF_cNeBNZqe9_qO67g_XQdpBK5a3NB-N2H9Sk_npKfxOdQitjmRVlef4oMC)
13. [wiley.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3P7NpwYatf7OmRMwUCdgaLMXYOn2pWe5SR0YR8PxTv2J5ZlXngmGTbRxL_cOfN1u4zmGH-8msexbvJq5xz3AU9XtsGld6Q1sCNroizpRb4n7YHzTSS4pVqyvxkGaS1zbc0QFCESpD2N2JZgcaoP8eeFJIbz4uS23XdbXBlg==)
14. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfDkf2WUwdwugaY6LWmjpp_x-eujaY0AhL-WlD5u1n2burbwg8giiKXzvgaMkppKjKyDdVuEi9zi5Tv-Ehsy7-pf7huIhtOodWl0Vbjr-l2ROy5GEYRiq57-u5u3Jr)
15. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2FD_2uSIv7V73bZbj5NpUFPBAUM-BT8uwy8KCRyGNEcg0P8a4K0zkubVueg3eCcwnuwcz-nyGrQlJhlqsYLqwket84PVS9wTlN4ws7TOJ_hEQnWFf9eQxta-8KY4tuaoUMKROerjtSquzwIzNVCa8F8yzdF0=)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJIPJaqGEAT4ml_chsCLiqKrF2LsXIKlQZaZueI2YxvCYt2Y5bpVc2avoYvYkU9NjGVDJMN9O6RPJqbhMFvbYemyle45at5E9zVQtfH6nYzLBsp03bJLGI6mV47JwJM6Huu3yhEOWj-gX_29HU7sjEQJBfS0EEa0gg5RZwa-sDqjVPVbsPwPBnOcrp4EioZM7bDfvAjXL-FIjD9tVoFImpQeb_UtVPpib9Lob8A2NDKBl1B-5g8fSc2NoD)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGJArz7Hy_43aZXY1isJafKo1UBTSVXHZhcheqhrNq70LrX0GU8FhO8TdlndVUWDxqc0N6K7ZyXfRQrLnTr-mA_yPM8EYVP1MKsQjGdo2Njr57YLryE4IlGdJ3R4rPi8nZLgd6847LRDJ9WEJoMh9IGDH0do2aqHWy2VHGrkLEKNcOHCdT2nm55HwN_rRCqkzgWzOmNqE8YEu8coeSE3fxzNm1m_G9XU2ozsWefCodGyvCt075UqKTTaCavWKoJH9qdsHF_gNepPJs0MzKhB4=)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc8R5uBiTQEon3jIGiV2aFdMlWnMSIiB0KGS1biYvmgxTSdGJ3T5nIrXfrAbVoO5KTQKoiF4lfKOOpQCLiU0VjwqOe-j__wGWS25d9DDCu1PTgpCVHtVIZEC6p3tfSz--XL96ncTBhDINqrlid_h-7JaJaifEbHgf_ZjHaDnv3QTugJ0tDNSBVkOot5HRfWHREMV-MVkC82WHYJM4l-7I4UDfZnt8gDWShGX0HYwGRtD1dVY8aVHdy_lSxpyFqbF4nz5UyCMWs_AmFizaU60q3JisddbGhY7wmhOY0FUiW5s-rfSs=)
19. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhW80AOkGyno52hiRqBE9qbmaRuz4nNtRJ5lfHQCCK_sP3n24_RsTv9_wbSzssRW9Q61yOtVfCB1Yto7M9rZlI0GaTHrJBvWn-zeoT3FMyuluiInFXW1Fk5QYKVvg=)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-mhO9k8XOvWM651-vpqZaPU3AeSC6FiZ3eLCfv4s1kcb1yrZOez4jdC4VBosqzNbr6bPIbvNFtYYqKCzjOr3mCa3obMTByA-FfTjbqr1bvc646jzUDPo7llusr6f1MhMSQjoZzW0onl8A7xzf8sfOnBLVFy9g0tpMP5J6bAy4IbN2RB2VlSFWyRrOziYjFhULQdjJXQELk0KAx5K14o7Wnv6tuOI57g74MmSLJpZ0NxVpaJdjHeM1t3V81zEMum9c5kXNRS5LKMddpq--y724fbv5b-hpUTI=)
21. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFt-oAfirJrFq9g1RE12OJ8VdiJ7qsaF357zc1p42BljdRMzm-wigDtv_WPOkj7hLQUrUah0fPYnNiUe2-D-CU0UjhjyvL3NGWWvzfnYhoGXEbSKuZd4uPy3A==)
22. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHugd-rq_p0yn1DwCqzjeuiuQgr4-7qOO5t3-n4Z4cidnvJYfyoHSwl1nWe2MNCNvQKp7V0ae047Nx_BFRhnWUaNY4WgB9aswRar1DHv5M1lLEqeMq1nQ==)
23. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhQxJr6QUVyRsr7ELmjuYTeD_Lvx_VSTPUhr_ygCa4sTsSUyRnIotD1vbc00-qRcDCeo-Vc7X-syBqMVa0uDGKdLDSgNxjUrrh91_X_9TBHmGu9YbsrhEriGQqU58ni75seINIFomnwmZ7suvOY1uXA4fNWIwpwSz5_Ng56ORAgP6rbL63-E0poUMIDMs2CY1of_DNAw==)
24. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa_epLGL90gw_MZvcbm7wPBBnabPZTwQpjuiA_8wpPLLqxHgt_yl1FDXDBvqCcwi8esyli1R4tGWz8HnG3Plktva-U8-FMykhYZ4cQuEC-9HMuNmCRDA==)
25. [thinkpol.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsSV5qvestnUXoJuUy3wTSMNI7w1S9d8BOWj4iukwSyfVLuNI9SVq0mDClYjgA6xwhzZ5do7vp93faqj4YVl5R32y3cLzLKo5Elq2Bm7cnRXOSVn28Tf677qu1gbj4SRTd8wPIjzKiA_gDRkQYwNzZgNBQkQLT2uwXLqA=)


## Annotations
Annotation(end_index=3137, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFXQG2aL-19by9ZTWEULStW9PkWu-s1y4sWY2eC4gLGOII0BVJCW7MFzqGhdZD6oWwua9o1tAQFMBdFY6ILQZF_DsgwMazrxBjVIXsROVSI_Y0RFG9frzTc6DLZYV8WNDoXPAW', start_index=3125)
Annotation(end_index=3137, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNygc_KBTx7eoURg05Q8SmQPRnIx_3zkCcQ8BJOiXhfs_HkRh3Wxy-HZtg_8wT55lyyZNWDFrAOBVbJnclKwUBfrQUafbqHghh3PVowj97CXFBjwuoKZXuQgxb4q4RhazdVPaiOh_GKeN3PEvN2iKyZJj2JhgIngqnp73cAjONMJBpEzEr4mpTbs6m_p6ZtO6klP5GBVk6uUyEXEO2biZsQu83XknJ8SDkjefe95R13fG7ervTNcWtaUlcjiw=', start_index=3125)
Annotation(end_index=3545, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC5iDBwlEbo-WxdAZEwzKdDsnGtHuEXSHmjt4wksyekbrnWpyCdZGlP7PRxJSSxj8RbUlZeZM3oubTHmyf5eBUi4ARAJUNapvVJspDVgyIsr012ncZDDTNa1V986Uh4Bn3t40-A5J_es_SmY6HUkyG6t1HINzXhjohGV1CjHT_rjyLC-2e2r8swkzi0OrixtuHPFgG4qWaObNK6D2OecgJu5Swfn9kONayL8MeL2GtV51fU5zxLPMPkZkUCc_wAuBPfw3DNDYOPcn7ao-U0P1duR0csVo_IsuqvGfOb81cjJUTXCVGefulj9P2Anmq3cOad201kkhRe5hUHSmlEf1uf7Wls7r822VsZ2Np4-44xEjpCr5lr8ZK_NjxeJU9yA==', start_index=3530)
Annotation(end_index=3545, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN7FN9EvLddbn1m-f9yUgzlVWEylvPKU3xnPzh2TPyr-DNq4cVAxCauaWGs4-J8Ggkqi8lOmSh2ZpmSHClziUZNhd7m-KoeieI4Xx3zdglAVAoDuENY7tsUgv366F5fAQGwg__AP1VDoIJ0--VM5RL1ovjrPJZqt6gL0FZjZBqiGGx9hB5zYSmSkujtZMqmbBugZtBTN7kxiEVHTLVZo6y8lH9cs3fLTqYAMYPBd63UQ==', start_index=3530)
Annotation(end_index=3545, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjVobRew9Ho68B-kl9eUGRu_ScxuDFgECwVkGy1-r8fnBQ3H-DbT6XCmKdM9XZn6azB16VAKOZ-My-EFkDIX9HjBrAkqIdobIWtu9mQ9ydKLbcvcznZZO1wvF-XDZDxIpVV65O8a8UZ10FxNO_JXtk8P2BR4vGg2vVmd59K3l0zHMtEdGGjelB1hrJg8gNXuYaSejW', start_index=3530)
Annotation(end_index=4343, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDLvU1dcJJnSu3oMuTrMoXoZgx5hCJG3aKreR3lPmUyi7LR_rjhcdUEAc8lVTNDzAjopdFk5gWtWADTt_vBXnRi4KZi1PCGiAXYumYp_jg-96oLmxrzPkd3DNIEu87nRWR-LMRROw9_EFBFdXF5jWHkCm3uigfcx0-KXM=', start_index=4331)
Annotation(end_index=4343, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyz-0bZGzhw8mw3GsVaBwP1RzXGq72SpfsQ21W5hkMuqO8Wu7p72doASEjsfAK61b4v0A-MTMpRubzA8QWyUVMaJS93eIbYHJXECO6Z7j99sretmLfNipqDGJZ9REXCdS6wpzDwmjwhRuskRvpx3rLLMOZQBlXqBNgRrCTs0-QkCFashzhe-4vaEF6iuUqkNY=', start_index=4331)
Annotation(end_index=5038, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE73FZX5KIS1uHaH4krPYcc6vjlyevl8Z1tyhNI71lYBiYygMNTKI4_4P9Z3rZlFGQ6mi9OI-jwBxLYqS99vqIMPY11i5mR39q_3yX1GaplV0wiLNkgSEDvJBmkRlMGM0mrjeEDlfjNl_hq-0Q6JNMBRXv9g9fAL8ceQ_TZ-SZm1EUnsZHo9ycMFi8CROx6q1loOU0b3jKUUiijq3rAJgVpZozphVM=', start_index=5026)
Annotation(end_index=5038, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXSGX1AVfI9a1-qTO0kyep1kKxxtWPzZkpAwD9FnqfQY_0LSJReDuxJUcarwKr9zxZgTnOnnnxjP1bxTIJSu-MeGTsWr-q0Ub6pv62DervGQQb_WA2_V9yrt9hO8MV-Mm9HRuRY-0NyQ==', start_index=5026)
Annotation(end_index=5825, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDRvIMN67p9xEKv2ZRqfx1_OFF2dwqah5s0BWvhjNNR7QGyF64WIVXn7DKZb7yCa7WhMb9oa9wM3p1IxeM9iBbhjeCNXIOKIRI83gzsaxo8fWMLWoJ6uFGgwJqlXmWZ-Fn-fxneA==', start_index=5807)
Annotation(end_index=5825, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWownjXCxYF9c_F4CNyq-ciqmHKfTN_7Yzc9b7bOqgsGm540HW4Z0_nExcsQ6zpCgqJ70IH-pNFo4yYJe2kBM4MGJSO48wd9mr2iQF9uZ8Cev0td4eU9Ltju2Xaw4eQ-guUOinxVxlK8f7hMLxfXIEBJbiiykGQe8pdA_HWzpnWitGexmIppesKqumLlkBj-bMh6rszZeXgth5xVD1cdi6JTY=', start_index=5807)
Annotation(end_index=5825, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNd0PqVG7uvW3uBPurb_HTF10Bimzr8EtRhpzCUw9uf63bWlfnAq_mer_XtRTeU7d9sZA51Tf3Aff45gSvkvQRFxXF76Et9_85Z2Ykye2l1vlUnd3Wf3v0MiPIrmgsBRHspNq_SVpPwLkU-AdVkQYRHtLlsNKgfPNJDNKB-eQyxZCCKSCSr7wiNK5Hx2EAeTPgWZF_cNeBNZqe9_qO67g_XQdpBK5a3NB-N2H9Sk_npKfxOdQitjmRVlef4oMC', start_index=5807)
Annotation(end_index=6041, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3P7NpwYatf7OmRMwUCdgaLMXYOn2pWe5SR0YR8PxTv2J5ZlXngmGTbRxL_cOfN1u4zmGH-8msexbvJq5xz3AU9XtsGld6Q1sCNroizpRb4n7YHzTSS4pVqyvxkGaS1zbc0QFCESpD2N2JZgcaoP8eeFJIbz4uS23XdbXBlg==', start_index=6028)
Annotation(end_index=6041, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXSGX1AVfI9a1-qTO0kyep1kKxxtWPzZkpAwD9FnqfQY_0LSJReDuxJUcarwKr9zxZgTnOnnnxjP1bxTIJSu-MeGTsWr-q0Ub6pv62DervGQQb_WA2_V9yrt9hO8MV-Mm9HRuRY-0NyQ==', start_index=6028)
Annotation(end_index=6375, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXSGX1AVfI9a1-qTO0kyep1kKxxtWPzZkpAwD9FnqfQY_0LSJReDuxJUcarwKr9zxZgTnOnnnxjP1bxTIJSu-MeGTsWr-q0Ub6pv62DervGQQb_WA2_V9yrt9hO8MV-Mm9HRuRY-0NyQ==', start_index=6362)
Annotation(end_index=6375, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfDkf2WUwdwugaY6LWmjpp_x-eujaY0AhL-WlD5u1n2burbwg8giiKXzvgaMkppKjKyDdVuEi9zi5Tv-Ehsy7-pf7huIhtOodWl0Vbjr-l2ROy5GEYRiq57-u5u3Jr', start_index=6362)
Annotation(end_index=6469, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFXQG2aL-19by9ZTWEULStW9PkWu-s1y4sWY2eC4gLGOII0BVJCW7MFzqGhdZD6oWwua9o1tAQFMBdFY6ILQZF_DsgwMazrxBjVIXsROVSI_Y0RFG9frzTc6DLZYV8WNDoXPAW', start_index=6453)
Annotation(end_index=6469, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNygc_KBTx7eoURg05Q8SmQPRnIx_3zkCcQ8BJOiXhfs_HkRh3Wxy-HZtg_8wT55lyyZNWDFrAOBVbJnclKwUBfrQUafbqHghh3PVowj97CXFBjwuoKZXuQgxb4q4RhazdVPaiOh_GKeN3PEvN2iKyZJj2JhgIngqnp73cAjONMJBpEzEr4mpTbs6m_p6ZtO6klP5GBVk6uUyEXEO2biZsQu83XknJ8SDkjefe95R13fG7ervTNcWtaUlcjiw=', start_index=6453)
Annotation(end_index=6469, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2FD_2uSIv7V73bZbj5NpUFPBAUM-BT8uwy8KCRyGNEcg0P8a4K0zkubVueg3eCcwnuwcz-nyGrQlJhlqsYLqwket84PVS9wTlN4ws7TOJ_hEQnWFf9eQxta-8KY4tuaoUMKROerjtSquzwIzNVCa8F8yzdF0=', start_index=6453)
Annotation(end_index=7882, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFXQG2aL-19by9ZTWEULStW9PkWu-s1y4sWY2eC4gLGOII0BVJCW7MFzqGhdZD6oWwua9o1tAQFMBdFY6ILQZF_DsgwMazrxBjVIXsROVSI_Y0RFG9frzTc6DLZYV8WNDoXPAW', start_index=7869)
Annotation(end_index=7882, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2FD_2uSIv7V73bZbj5NpUFPBAUM-BT8uwy8KCRyGNEcg0P8a4K0zkubVueg3eCcwnuwcz-nyGrQlJhlqsYLqwket84PVS9wTlN4ws7TOJ_hEQnWFf9eQxta-8KY4tuaoUMKROerjtSquzwIzNVCa8F8yzdF0=', start_index=7869)
Annotation(end_index=8327, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNygc_KBTx7eoURg05Q8SmQPRnIx_3zkCcQ8BJOiXhfs_HkRh3Wxy-HZtg_8wT55lyyZNWDFrAOBVbJnclKwUBfrQUafbqHghh3PVowj97CXFBjwuoKZXuQgxb4q4RhazdVPaiOh_GKeN3PEvN2iKyZJj2JhgIngqnp73cAjONMJBpEzEr4mpTbs6m_p6ZtO6klP5GBVk6uUyEXEO2biZsQu83XknJ8SDkjefe95R13fG7ervTNcWtaUlcjiw=', start_index=8314)
Annotation(end_index=8327, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2FD_2uSIv7V73bZbj5NpUFPBAUM-BT8uwy8KCRyGNEcg0P8a4K0zkubVueg3eCcwnuwcz-nyGrQlJhlqsYLqwket84PVS9wTlN4ws7TOJ_hEQnWFf9eQxta-8KY4tuaoUMKROerjtSquzwIzNVCa8F8yzdF0=', start_index=8314)
Annotation(end_index=8816, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJIPJaqGEAT4ml_chsCLiqKrF2LsXIKlQZaZueI2YxvCYt2Y5bpVc2avoYvYkU9NjGVDJMN9O6RPJqbhMFvbYemyle45at5E9zVQtfH6nYzLBsp03bJLGI6mV47JwJM6Huu3yhEOWj-gX_29HU7sjEQJBfS0EEa0gg5RZwa-sDqjVPVbsPwPBnOcrp4EioZM7bDfvAjXL-FIjD9tVoFImpQeb_UtVPpib9Lob8A2NDKBl1B-5g8fSc2NoD', start_index=8803)
Annotation(end_index=8816, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNygc_KBTx7eoURg05Q8SmQPRnIx_3zkCcQ8BJOiXhfs_HkRh3Wxy-HZtg_8wT55lyyZNWDFrAOBVbJnclKwUBfrQUafbqHghh3PVowj97CXFBjwuoKZXuQgxb4q4RhazdVPaiOh_GKeN3PEvN2iKyZJj2JhgIngqnp73cAjONMJBpEzEr4mpTbs6m_p6ZtO6klP5GBVk6uUyEXEO2biZsQu83XknJ8SDkjefe95R13fG7ervTNcWtaUlcjiw=', start_index=8803)
Annotation(end_index=9321, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfDkf2WUwdwugaY6LWmjpp_x-eujaY0AhL-WlD5u1n2burbwg8giiKXzvgaMkppKjKyDdVuEi9zi5Tv-Ehsy7-pf7huIhtOodWl0Vbjr-l2ROy5GEYRiq57-u5u3Jr', start_index=9307)
Annotation(end_index=9321, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGJArz7Hy_43aZXY1isJafKo1UBTSVXHZhcheqhrNq70LrX0GU8FhO8TdlndVUWDxqc0N6K7ZyXfRQrLnTr-mA_yPM8EYVP1MKsQjGdo2Njr57YLryE4IlGdJ3R4rPi8nZLgd6847LRDJ9WEJoMh9IGDH0do2aqHWy2VHGrkLEKNcOHCdT2nm55HwN_rRCqkzgWzOmNqE8YEu8coeSE3fxzNm1m_G9XU2ozsWefCodGyvCt075UqKTTaCavWKoJH9qdsHF_gNepPJs0MzKhB4=', start_index=9307)
Annotation(end_index=9599, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-mhO9k8XOvWM651-vpqZaPU3AeSC6FiZ3eLCfv4s1kcb1yrZOez4jdC4VBosqzNbr6bPIbvNFtYYqKCzjOr3mCa3obMTByA-FfTjbqr1bvc646jzUDPo7llusr6f1MhMSQjoZzW0onl8A7xzf8sfOnBLVFy9g0tpMP5J6bAy4IbN2RB2VlSFWyRrOziYjFhULQdjJXQELk0KAx5K14o7Wnv6tuOI57g74MmSLJpZ0NxVpaJdjHeM1t3V81zEMum9c5kXNRS5LKMddpq--y724fbv5b-hpUTI=', start_index=9581)
Annotation(end_index=9599, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc8R5uBiTQEon3jIGiV2aFdMlWnMSIiB0KGS1biYvmgxTSdGJ3T5nIrXfrAbVoO5KTQKoiF4lfKOOpQCLiU0VjwqOe-j__wGWS25d9DDCu1PTgpCVHtVIZEC6p3tfSz--XL96ncTBhDINqrlid_h-7JaJaifEbHgf_ZjHaDnv3QTugJ0tDNSBVkOot5HRfWHREMV-MVkC82WHYJM4l-7I4UDfZnt8gDWShGX0HYwGRtD1dVY8aVHdy_lSxpyFqbF4nz5UyCMWs_AmFizaU60q3JisddbGhY7wmhOY0FUiW5s-rfSs=', start_index=9581)
Annotation(end_index=9599, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhW80AOkGyno52hiRqBE9qbmaRuz4nNtRJ5lfHQCCK_sP3n24_RsTv9_wbSzssRW9Q61yOtVfCB1Yto7M9rZlI0GaTHrJBvWn-zeoT3FMyuluiInFXW1Fk5QYKVvg=', start_index=9581)
Annotation(end_index=10171, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNygc_KBTx7eoURg05Q8SmQPRnIx_3zkCcQ8BJOiXhfs_HkRh3Wxy-HZtg_8wT55lyyZNWDFrAOBVbJnclKwUBfrQUafbqHghh3PVowj97CXFBjwuoKZXuQgxb4q4RhazdVPaiOh_GKeN3PEvN2iKyZJj2JhgIngqnp73cAjONMJBpEzEr4mpTbs6m_p6ZtO6klP5GBVk6uUyEXEO2biZsQu83XknJ8SDkjefe95R13fG7ervTNcWtaUlcjiw=', start_index=10158)
Annotation(end_index=10171, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2FD_2uSIv7V73bZbj5NpUFPBAUM-BT8uwy8KCRyGNEcg0P8a4K0zkubVueg3eCcwnuwcz-nyGrQlJhlqsYLqwket84PVS9wTlN4ws7TOJ_hEQnWFf9eQxta-8KY4tuaoUMKROerjtSquzwIzNVCa8F8yzdF0=', start_index=10158)
Annotation(end_index=10292, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC5iDBwlEbo-WxdAZEwzKdDsnGtHuEXSHmjt4wksyekbrnWpyCdZGlP7PRxJSSxj8RbUlZeZM3oubTHmyf5eBUi4ARAJUNapvVJspDVgyIsr012ncZDDTNa1V986Uh4Bn3t40-A5J_es_SmY6HUkyG6t1HINzXhjohGV1CjHT_rjyLC-2e2r8swkzi0OrixtuHPFgG4qWaObNK6D2OecgJu5Swfn9kONayL8MeL2GtV51fU5zxLPMPkZkUCc_wAuBPfw3DNDYOPcn7ao-U0P1duR0csVo_IsuqvGfOb81cjJUTXCVGefulj9P2Anmq3cOad201kkhRe5hUHSmlEf1uf7Wls7r822VsZ2Np4-44xEjpCr5lr8ZK_NjxeJU9yA==', start_index=10273)
Annotation(end_index=10292, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN7FN9EvLddbn1m-f9yUgzlVWEylvPKU3xnPzh2TPyr-DNq4cVAxCauaWGs4-J8Ggkqi8lOmSh2ZpmSHClziUZNhd7m-KoeieI4Xx3zdglAVAoDuENY7tsUgv366F5fAQGwg__AP1VDoIJ0--VM5RL1ovjrPJZqt6gL0FZjZBqiGGx9hB5zYSmSkujtZMqmbBugZtBTN7kxiEVHTLVZo6y8lH9cs3fLTqYAMYPBd63UQ==', start_index=10273)
Annotation(end_index=10292, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjVobRew9Ho68B-kl9eUGRu_ScxuDFgECwVkGy1-r8fnBQ3H-DbT6XCmKdM9XZn6azB16VAKOZ-My-EFkDIX9HjBrAkqIdobIWtu9mQ9ydKLbcvcznZZO1wvF-XDZDxIpVV65O8a8UZ10FxNO_JXtk8P2BR4vGg2vVmd59K3l0zHMtEdGGjelB1hrJg8gNXuYaSejW', start_index=10273)
Annotation(end_index=10292, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFt-oAfirJrFq9g1RE12OJ8VdiJ7qsaF357zc1p42BljdRMzm-wigDtv_WPOkj7hLQUrUah0fPYnNiUe2-D-CU0UjhjyvL3NGWWvzfnYhoGXEbSKuZd4uPy3A==', start_index=10273)
Annotation(end_index=10717, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC5iDBwlEbo-WxdAZEwzKdDsnGtHuEXSHmjt4wksyekbrnWpyCdZGlP7PRxJSSxj8RbUlZeZM3oubTHmyf5eBUi4ARAJUNapvVJspDVgyIsr012ncZDDTNa1V986Uh4Bn3t40-A5J_es_SmY6HUkyG6t1HINzXhjohGV1CjHT_rjyLC-2e2r8swkzi0OrixtuHPFgG4qWaObNK6D2OecgJu5Swfn9kONayL8MeL2GtV51fU5zxLPMPkZkUCc_wAuBPfw3DNDYOPcn7ao-U0P1duR0csVo_IsuqvGfOb81cjJUTXCVGefulj9P2Anmq3cOad201kkhRe5hUHSmlEf1uf7Wls7r822VsZ2Np4-44xEjpCr5lr8ZK_NjxeJU9yA==', start_index=10705)
Annotation(end_index=10717, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjVobRew9Ho68B-kl9eUGRu_ScxuDFgECwVkGy1-r8fnBQ3H-DbT6XCmKdM9XZn6azB16VAKOZ-My-EFkDIX9HjBrAkqIdobIWtu9mQ9ydKLbcvcznZZO1wvF-XDZDxIpVV65O8a8UZ10FxNO_JXtk8P2BR4vGg2vVmd59K3l0zHMtEdGGjelB1hrJg8gNXuYaSejW', start_index=10705)
Annotation(end_index=11293, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN7FN9EvLddbn1m-f9yUgzlVWEylvPKU3xnPzh2TPyr-DNq4cVAxCauaWGs4-J8Ggkqi8lOmSh2ZpmSHClziUZNhd7m-KoeieI4Xx3zdglAVAoDuENY7tsUgv366F5fAQGwg__AP1VDoIJ0--VM5RL1ovjrPJZqt6gL0FZjZBqiGGx9hB5zYSmSkujtZMqmbBugZtBTN7kxiEVHTLVZo6y8lH9cs3fLTqYAMYPBd63UQ==', start_index=11284)
Annotation(end_index=11987, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHugd-rq_p0yn1DwCqzjeuiuQgr4-7qOO5t3-n4Z4cidnvJYfyoHSwl1nWe2MNCNvQKp7V0ae047Nx_BFRhnWUaNY4WgB9aswRar1DHv5M1lLEqeMq1nQ==', start_index=11977)
Annotation(end_index=12279, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN7FN9EvLddbn1m-f9yUgzlVWEylvPKU3xnPzh2TPyr-DNq4cVAxCauaWGs4-J8Ggkqi8lOmSh2ZpmSHClziUZNhd7m-KoeieI4Xx3zdglAVAoDuENY7tsUgv366F5fAQGwg__AP1VDoIJ0--VM5RL1ovjrPJZqt6gL0FZjZBqiGGx9hB5zYSmSkujtZMqmbBugZtBTN7kxiEVHTLVZo6y8lH9cs3fLTqYAMYPBd63UQ==', start_index=12270)
Annotation(end_index=12839, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC5iDBwlEbo-WxdAZEwzKdDsnGtHuEXSHmjt4wksyekbrnWpyCdZGlP7PRxJSSxj8RbUlZeZM3oubTHmyf5eBUi4ARAJUNapvVJspDVgyIsr012ncZDDTNa1V986Uh4Bn3t40-A5J_es_SmY6HUkyG6t1HINzXhjohGV1CjHT_rjyLC-2e2r8swkzi0OrixtuHPFgG4qWaObNK6D2OecgJu5Swfn9kONayL8MeL2GtV51fU5zxLPMPkZkUCc_wAuBPfw3DNDYOPcn7ao-U0P1duR0csVo_IsuqvGfOb81cjJUTXCVGefulj9P2Anmq3cOad201kkhRe5hUHSmlEf1uf7Wls7r822VsZ2Np4-44xEjpCr5lr8ZK_NjxeJU9yA==', start_index=12827)
Annotation(end_index=12839, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjVobRew9Ho68B-kl9eUGRu_ScxuDFgECwVkGy1-r8fnBQ3H-DbT6XCmKdM9XZn6azB16VAKOZ-My-EFkDIX9HjBrAkqIdobIWtu9mQ9ydKLbcvcznZZO1wvF-XDZDxIpVV65O8a8UZ10FxNO_JXtk8P2BR4vGg2vVmd59K3l0zHMtEdGGjelB1hrJg8gNXuYaSejW', start_index=12827)
Annotation(end_index=13471, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-mhO9k8XOvWM651-vpqZaPU3AeSC6FiZ3eLCfv4s1kcb1yrZOez4jdC4VBosqzNbr6bPIbvNFtYYqKCzjOr3mCa3obMTByA-FfTjbqr1bvc646jzUDPo7llusr6f1MhMSQjoZzW0onl8A7xzf8sfOnBLVFy9g0tpMP5J6bAy4IbN2RB2VlSFWyRrOziYjFhULQdjJXQELk0KAx5K14o7Wnv6tuOI57g74MmSLJpZ0NxVpaJdjHeM1t3V81zEMum9c5kXNRS5LKMddpq--y724fbv5b-hpUTI=', start_index=13453)
Annotation(end_index=13471, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc8R5uBiTQEon3jIGiV2aFdMlWnMSIiB0KGS1biYvmgxTSdGJ3T5nIrXfrAbVoO5KTQKoiF4lfKOOpQCLiU0VjwqOe-j__wGWS25d9DDCu1PTgpCVHtVIZEC6p3tfSz--XL96ncTBhDINqrlid_h-7JaJaifEbHgf_ZjHaDnv3QTugJ0tDNSBVkOot5HRfWHREMV-MVkC82WHYJM4l-7I4UDfZnt8gDWShGX0HYwGRtD1dVY8aVHdy_lSxpyFqbF4nz5UyCMWs_AmFizaU60q3JisddbGhY7wmhOY0FUiW5s-rfSs=', start_index=13453)
Annotation(end_index=13471, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhW80AOkGyno52hiRqBE9qbmaRuz4nNtRJ5lfHQCCK_sP3n24_RsTv9_wbSzssRW9Q61yOtVfCB1Yto7M9rZlI0GaTHrJBvWn-zeoT3FMyuluiInFXW1Fk5QYKVvg=', start_index=13453)
Annotation(end_index=13899, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc8R5uBiTQEon3jIGiV2aFdMlWnMSIiB0KGS1biYvmgxTSdGJ3T5nIrXfrAbVoO5KTQKoiF4lfKOOpQCLiU0VjwqOe-j__wGWS25d9DDCu1PTgpCVHtVIZEC6p3tfSz--XL96ncTBhDINqrlid_h-7JaJaifEbHgf_ZjHaDnv3QTugJ0tDNSBVkOot5HRfWHREMV-MVkC82WHYJM4l-7I4UDfZnt8gDWShGX0HYwGRtD1dVY8aVHdy_lSxpyFqbF4nz5UyCMWs_AmFizaU60q3JisddbGhY7wmhOY0FUiW5s-rfSs=', start_index=13889)
Annotation(end_index=14421, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJIPJaqGEAT4ml_chsCLiqKrF2LsXIKlQZaZueI2YxvCYt2Y5bpVc2avoYvYkU9NjGVDJMN9O6RPJqbhMFvbYemyle45at5E9zVQtfH6nYzLBsp03bJLGI6mV47JwJM6Huu3yhEOWj-gX_29HU7sjEQJBfS0EEa0gg5RZwa-sDqjVPVbsPwPBnOcrp4EioZM7bDfvAjXL-FIjD9tVoFImpQeb_UtVPpib9Lob8A2NDKBl1B-5g8fSc2NoD', start_index=14408)
Annotation(end_index=14421, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNygc_KBTx7eoURg05Q8SmQPRnIx_3zkCcQ8BJOiXhfs_HkRh3Wxy-HZtg_8wT55lyyZNWDFrAOBVbJnclKwUBfrQUafbqHghh3PVowj97CXFBjwuoKZXuQgxb4q4RhazdVPaiOh_GKeN3PEvN2iKyZJj2JhgIngqnp73cAjONMJBpEzEr4mpTbs6m_p6ZtO6klP5GBVk6uUyEXEO2biZsQu83XknJ8SDkjefe95R13fG7ervTNcWtaUlcjiw=', start_index=14408)
Annotation(end_index=14531, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE73FZX5KIS1uHaH4krPYcc6vjlyevl8Z1tyhNI71lYBiYygMNTKI4_4P9Z3rZlFGQ6mi9OI-jwBxLYqS99vqIMPY11i5mR39q_3yX1GaplV0wiLNkgSEDvJBmkRlMGM0mrjeEDlfjNl_hq-0Q6JNMBRXv9g9fAL8ceQ_TZ-SZm1EUnsZHo9ycMFi8CROx6q1loOU0b3jKUUiijq3rAJgVpZozphVM=', start_index=14507)
Annotation(end_index=14531, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa_epLGL90gw_MZvcbm7wPBBnabPZTwQpjuiA_8wpPLLqxHgt_yl1FDXDBvqCcwi8esyli1R4tGWz8HnG3Plktva-U8-FMykhYZ4cQuEC-9HMuNmCRDA==', start_index=14507)
Annotation(end_index=14531, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFt-oAfirJrFq9g1RE12OJ8VdiJ7qsaF357zc1p42BljdRMzm-wigDtv_WPOkj7hLQUrUah0fPYnNiUe2-D-CU0UjhjyvL3NGWWvzfnYhoGXEbSKuZd4uPy3A==', start_index=14507)
Annotation(end_index=14531, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXSGX1AVfI9a1-qTO0kyep1kKxxtWPzZkpAwD9FnqfQY_0LSJReDuxJUcarwKr9zxZgTnOnnnxjP1bxTIJSu-MeGTsWr-q0Ub6pv62DervGQQb_WA2_V9yrt9hO8MV-Mm9HRuRY-0NyQ==', start_index=14507)
Annotation(end_index=14531, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhQxJr6QUVyRsr7ELmjuYTeD_Lvx_VSTPUhr_ygCa4sTsSUyRnIotD1vbc00-qRcDCeo-Vc7X-syBqMVa0uDGKdLDSgNxjUrrh91_X_9TBHmGu9YbsrhEriGQqU58ni75seINIFomnwmZ7suvOY1uXA4fNWIwpwSz5_Ng56ORAgP6rbL63-E0poUMIDMs2CY1of_DNAw==', start_index=14507)
Annotation(end_index=15453, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFt-oAfirJrFq9g1RE12OJ8VdiJ7qsaF357zc1p42BljdRMzm-wigDtv_WPOkj7hLQUrUah0fPYnNiUe2-D-CU0UjhjyvL3NGWWvzfnYhoGXEbSKuZd4uPy3A==', start_index=15439)
Annotation(end_index=15453, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsSV5qvestnUXoJuUy3wTSMNI7w1S9d8BOWj4iukwSyfVLuNI9SVq0mDClYjgA6xwhzZ5do7vp93faqj4YVl5R32y3cLzLKo5Elq2Bm7cnRXOSVn28Tf677qu1gbj4SRTd8wPIjzKiA_gDRkQYwNzZgNBQkQLT2uwXLqA=', start_index=15439)
Annotation(end_index=15897, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFt-oAfirJrFq9g1RE12OJ8VdiJ7qsaF357zc1p42BljdRMzm-wigDtv_WPOkj7hLQUrUah0fPYnNiUe2-D-CU0UjhjyvL3NGWWvzfnYhoGXEbSKuZd4uPy3A==', start_index=15887)
Annotation(end_index=17000, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXSGX1AVfI9a1-qTO0kyep1kKxxtWPzZkpAwD9FnqfQY_0LSJReDuxJUcarwKr9zxZgTnOnnnxjP1bxTIJSu-MeGTsWr-q0Ub6pv62DervGQQb_WA2_V9yrt9hO8MV-Mm9HRuRY-0NyQ==', start_index=16991)
Annotation(end_index=17099, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDLvU1dcJJnSu3oMuTrMoXoZgx5hCJG3aKreR3lPmUyi7LR_rjhcdUEAc8lVTNDzAjopdFk5gWtWADTt_vBXnRi4KZi1PCGiAXYumYp_jg-96oLmxrzPkd3DNIEu87nRWR-LMRROw9_EFBFdXF5jWHkCm3uigfcx0-KXM=', start_index=17090)
Annotation(end_index=17165, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfDkf2WUwdwugaY6LWmjpp_x-eujaY0AhL-WlD5u1n2burbwg8giiKXzvgaMkppKjKyDdVuEi9zi5Tv-Ehsy7-pf7huIhtOodWl0Vbjr-l2ROy5GEYRiq57-u5u3Jr', start_index=17155)
Annotation(end_index=17254, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN7FN9EvLddbn1m-f9yUgzlVWEylvPKU3xnPzh2TPyr-DNq4cVAxCauaWGs4-J8Ggkqi8lOmSh2ZpmSHClziUZNhd7m-KoeieI4Xx3zdglAVAoDuENY7tsUgv366F5fAQGwg__AP1VDoIJ0--VM5RL1ovjrPJZqt6gL0FZjZBqiGGx9hB5zYSmSkujtZMqmbBugZtBTN7kxiEVHTLVZo6y8lH9cs3fLTqYAMYPBd63UQ==', start_index=17245)
Annotation(end_index=17360, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHugd-rq_p0yn1DwCqzjeuiuQgr4-7qOO5t3-n4Z4cidnvJYfyoHSwl1nWe2MNCNvQKp7V0ae047Nx_BFRhnWUaNY4WgB9aswRar1DHv5M1lLEqeMq1nQ==', start_index=17350)
Annotation(end_index=17455, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWownjXCxYF9c_F4CNyq-ciqmHKfTN_7Yzc9b7bOqgsGm540HW4Z0_nExcsQ6zpCgqJ70IH-pNFo4yYJe2kBM4MGJSO48wd9mr2iQF9uZ8Cev0td4eU9Ltju2Xaw4eQ-guUOinxVxlK8f7hMLxfXIEBJbiiykGQe8pdA_HWzpnWitGexmIppesKqumLlkBj-bMh6rszZeXgth5xVD1cdi6JTY=', start_index=17445)
Annotation(end_index=17548, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDRvIMN67p9xEKv2ZRqfx1_OFF2dwqah5s0BWvhjNNR7QGyF64WIVXn7DKZb7yCa7WhMb9oa9wM3p1IxeM9iBbhjeCNXIOKIRI83gzsaxo8fWMLWoJ6uFGgwJqlXmWZ-Fn-fxneA==', start_index=17538)
Annotation(end_index=17609, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhQxJr6QUVyRsr7ELmjuYTeD_Lvx_VSTPUhr_ygCa4sTsSUyRnIotD1vbc00-qRcDCeo-Vc7X-syBqMVa0uDGKdLDSgNxjUrrh91_X_9TBHmGu9YbsrhEriGQqU58ni75seINIFomnwmZ7suvOY1uXA4fNWIwpwSz5_Ng56ORAgP6rbL63-E0poUMIDMs2CY1of_DNAw==', start_index=17599)
Annotation(end_index=17694, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNd0PqVG7uvW3uBPurb_HTF10Bimzr8EtRhpzCUw9uf63bWlfnAq_mer_XtRTeU7d9sZA51Tf3Aff45gSvkvQRFxXF76Et9_85Z2Ykye2l1vlUnd3Wf3v0MiPIrmgsBRHspNq_SVpPwLkU-AdVkQYRHtLlsNKgfPNJDNKB-eQyxZCCKSCSr7wiNK5Hx2EAeTPgWZF_cNeBNZqe9_qO67g_XQdpBK5a3NB-N2H9Sk_npKfxOdQitjmRVlef4oMC', start_index=17684)
Annotation(end_index=17789, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNygc_KBTx7eoURg05Q8SmQPRnIx_3zkCcQ8BJOiXhfs_HkRh3Wxy-HZtg_8wT55lyyZNWDFrAOBVbJnclKwUBfrQUafbqHghh3PVowj97CXFBjwuoKZXuQgxb4q4RhazdVPaiOh_GKeN3PEvN2iKyZJj2JhgIngqnp73cAjONMJBpEzEr4mpTbs6m_p6ZtO6klP5GBVk6uUyEXEO2biZsQu83XknJ8SDkjefe95R13fG7ervTNcWtaUlcjiw=', start_index=17780)
Annotation(end_index=17908, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3P7NpwYatf7OmRMwUCdgaLMXYOn2pWe5SR0YR8PxTv2J5ZlXngmGTbRxL_cOfN1u4zmGH-8msexbvJq5xz3AU9XtsGld6Q1sCNroizpRb4n7YHzTSS4pVqyvxkGaS1zbc0QFCESpD2N2JZgcaoP8eeFJIbz4uS23XdbXBlg==', start_index=17898)
Annotation(end_index=17994, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXSGX1AVfI9a1-qTO0kyep1kKxxtWPzZkpAwD9FnqfQY_0LSJReDuxJUcarwKr9zxZgTnOnnnxjP1bxTIJSu-MeGTsWr-q0Ub6pv62DervGQQb_WA2_V9yrt9hO8MV-Mm9HRuRY-0NyQ==', start_index=17985)
Annotation(end_index=18068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE73FZX5KIS1uHaH4krPYcc6vjlyevl8Z1tyhNI71lYBiYygMNTKI4_4P9Z3rZlFGQ6mi9OI-jwBxLYqS99vqIMPY11i5mR39q_3yX1GaplV0wiLNkgSEDvJBmkRlMGM0mrjeEDlfjNl_hq-0Q6JNMBRXv9g9fAL8ceQ_TZ-SZm1EUnsZHo9ycMFi8CROx6q1loOU0b3jKUUiijq3rAJgVpZozphVM=', start_index=18059)
Annotation(end_index=18164, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyz-0bZGzhw8mw3GsVaBwP1RzXGq72SpfsQ21W5hkMuqO8Wu7p72doASEjsfAK61b4v0A-MTMpRubzA8QWyUVMaJS93eIbYHJXECO6Z7j99sretmLfNipqDGJZ9REXCdS6wpzDwmjwhRuskRvpx3rLLMOZQBlXqBNgRrCTs0-QkCFashzhe-4vaEF6iuUqkNY=', start_index=18155)
Annotation(end_index=18249, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC5iDBwlEbo-WxdAZEwzKdDsnGtHuEXSHmjt4wksyekbrnWpyCdZGlP7PRxJSSxj8RbUlZeZM3oubTHmyf5eBUi4ARAJUNapvVJspDVgyIsr012ncZDDTNa1V986Uh4Bn3t40-A5J_es_SmY6HUkyG6t1HINzXhjohGV1CjHT_rjyLC-2e2r8swkzi0OrixtuHPFgG4qWaObNK6D2OecgJu5Swfn9kONayL8MeL2GtV51fU5zxLPMPkZkUCc_wAuBPfw3DNDYOPcn7ao-U0P1duR0csVo_IsuqvGfOb81cjJUTXCVGefulj9P2Anmq3cOad201kkhRe5hUHSmlEf1uf7Wls7r822VsZ2Np4-44xEjpCr5lr8ZK_NjxeJU9yA==', start_index=18240)
Annotation(end_index=18319, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjVobRew9Ho68B-kl9eUGRu_ScxuDFgECwVkGy1-r8fnBQ3H-DbT6XCmKdM9XZn6azB16VAKOZ-My-EFkDIX9HjBrAkqIdobIWtu9mQ9ydKLbcvcznZZO1wvF-XDZDxIpVV65O8a8UZ10FxNO_JXtk8P2BR4vGg2vVmd59K3l0zHMtEdGGjelB1hrJg8gNXuYaSejW', start_index=18310)
Annotation(end_index=18421, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFt-oAfirJrFq9g1RE12OJ8VdiJ7qsaF357zc1p42BljdRMzm-wigDtv_WPOkj7hLQUrUah0fPYnNiUe2-D-CU0UjhjyvL3NGWWvzfnYhoGXEbSKuZd4uPy3A==', start_index=18411)
Annotation(end_index=18514, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNygc_KBTx7eoURg05Q8SmQPRnIx_3zkCcQ8BJOiXhfs_HkRh3Wxy-HZtg_8wT55lyyZNWDFrAOBVbJnclKwUBfrQUafbqHghh3PVowj97CXFBjwuoKZXuQgxb4q4RhazdVPaiOh_GKeN3PEvN2iKyZJj2JhgIngqnp73cAjONMJBpEzEr4mpTbs6m_p6ZtO6klP5GBVk6uUyEXEO2biZsQu83XknJ8SDkjefe95R13fG7ervTNcWtaUlcjiw=', start_index=18505)
Annotation(end_index=18603, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJIPJaqGEAT4ml_chsCLiqKrF2LsXIKlQZaZueI2YxvCYt2Y5bpVc2avoYvYkU9NjGVDJMN9O6RPJqbhMFvbYemyle45at5E9zVQtfH6nYzLBsp03bJLGI6mV47JwJM6Huu3yhEOWj-gX_29HU7sjEQJBfS0EEa0gg5RZwa-sDqjVPVbsPwPBnOcrp4EioZM7bDfvAjXL-FIjD9tVoFImpQeb_UtVPpib9Lob8A2NDKBl1B-5g8fSc2NoD', start_index=18593)
Annotation(end_index=18700, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFXQG2aL-19by9ZTWEULStW9PkWu-s1y4sWY2eC4gLGOII0BVJCW7MFzqGhdZD6oWwua9o1tAQFMBdFY6ILQZF_DsgwMazrxBjVIXsROVSI_Y0RFG9frzTc6DLZYV8WNDoXPAW', start_index=18691)
Annotation(end_index=18796, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2FD_2uSIv7V73bZbj5NpUFPBAUM-BT8uwy8KCRyGNEcg0P8a4K0zkubVueg3eCcwnuwcz-nyGrQlJhlqsYLqwket84PVS9wTlN4ws7TOJ_hEQnWFf9eQxta-8KY4tuaoUMKROerjtSquzwIzNVCa8F8yzdF0=', start_index=18786)
Annotation(end_index=18864, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjVobRew9Ho68B-kl9eUGRu_ScxuDFgECwVkGy1-r8fnBQ3H-DbT6XCmKdM9XZn6azB16VAKOZ-My-EFkDIX9HjBrAkqIdobIWtu9mQ9ydKLbcvcznZZO1wvF-XDZDxIpVV65O8a8UZ10FxNO_JXtk8P2BR4vGg2vVmd59K3l0zHMtEdGGjelB1hrJg8gNXuYaSejW', start_index=18855)
Annotation(end_index=18933, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGJArz7Hy_43aZXY1isJafKo1UBTSVXHZhcheqhrNq70LrX0GU8FhO8TdlndVUWDxqc0N6K7ZyXfRQrLnTr-mA_yPM8EYVP1MKsQjGdo2Njr57YLryE4IlGdJ3R4rPi8nZLgd6847LRDJ9WEJoMh9IGDH0do2aqHWy2VHGrkLEKNcOHCdT2nm55HwN_rRCqkzgWzOmNqE8YEu8coeSE3fxzNm1m_G9XU2ozsWefCodGyvCt075UqKTTaCavWKoJH9qdsHF_gNepPJs0MzKhB4=', start_index=18923)
Annotation(end_index=19028, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc8R5uBiTQEon3jIGiV2aFdMlWnMSIiB0KGS1biYvmgxTSdGJ3T5nIrXfrAbVoO5KTQKoiF4lfKOOpQCLiU0VjwqOe-j__wGWS25d9DDCu1PTgpCVHtVIZEC6p3tfSz--XL96ncTBhDINqrlid_h-7JaJaifEbHgf_ZjHaDnv3QTugJ0tDNSBVkOot5HRfWHREMV-MVkC82WHYJM4l-7I4UDfZnt8gDWShGX0HYwGRtD1dVY8aVHdy_lSxpyFqbF4nz5UyCMWs_AmFizaU60q3JisddbGhY7wmhOY0FUiW5s-rfSs=', start_index=19018)
Annotation(end_index=19134, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhW80AOkGyno52hiRqBE9qbmaRuz4nNtRJ5lfHQCCK_sP3n24_RsTv9_wbSzssRW9Q61yOtVfCB1Yto7M9rZlI0GaTHrJBvWn-zeoT3FMyuluiInFXW1Fk5QYKVvg=', start_index=19124)
Annotation(end_index=19227, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-mhO9k8XOvWM651-vpqZaPU3AeSC6FiZ3eLCfv4s1kcb1yrZOez4jdC4VBosqzNbr6bPIbvNFtYYqKCzjOr3mCa3obMTByA-FfTjbqr1bvc646jzUDPo7llusr6f1MhMSQjoZzW0onl8A7xzf8sfOnBLVFy9g0tpMP5J6bAy4IbN2RB2VlSFWyRrOziYjFhULQdjJXQELk0KAx5K14o7Wnv6tuOI57g74MmSLJpZ0NxVpaJdjHeM1t3V81zEMum9c5kXNRS5LKMddpq--y724fbv5b-hpUTI=', start_index=19217)

## Sources
