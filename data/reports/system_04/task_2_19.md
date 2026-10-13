# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 99568e3b | **Time:** 240.28s | **Cost:** $0.85259
--------------------------------------------------------------------------------

# Computation Offloading Strategies in IoT Edge Nodes: Optimizing the Energy-Latency Trade-off

### Key Points
*   **The Optimal Strategy is Hybrid:** Research indicates that **Lyapunov-guided Deep Reinforcement Learning (DRL)** frameworks, such as **LyDROO** and **LyA3C**, yield the best comprehensive performance. These strategies outperform traditional heuristic, pure convex optimization, and standalone DRL methods by effectively balancing real-time latency minimization with long-term energy constraints and queue stability [cite: 1, 2, 3, 4].
*   **Hardware-Software Co-design is Critical:** The decision to offload is increasingly influenced by advancements in local Neural Processing Units (NPUs), such as the **Arm Ethos-U85**. These processors enable "always-on" local AI with sub-threshold voltage operation, significantly raising the threshold for when offloading is energetically favorable compared to local execution [cite: 5, 6, 7].
*   **Stability vs. Agility:** While DRL provides agility in unknown dynamic environments (varying channel states), it often lacks stability. Lyapunov optimization provides the necessary theoretical control guarantees for battery and task queues, transforming complex stochastic problems into solvable deterministic sub-problems per time slot [cite: 8, 9, 10].
*   **Context-Awareness:** The "best" strategy shifts based on task dependencies (DAGs) and energy sources. For energy-harvesting IoT nodes, strategies must incorporate virtual energy queues to prevent battery depletion, a capability intrinsic to Lyapunov-based approaches but difficult for pure game-theoretic models [cite: 9, 11].

---

## 1. Introduction

The proliferation of the Internet of Things (IoT) has transitioned computing paradigms from centralized cloud architectures to decentralized Mobile Edge Computing (MEC). In this ecosystem, IoT edge nodes—ranging from industrial sensors to smart wearables—face a fundamental resource conflict: the demand for complex, real-time computation (e.g., video analytics, deep learning inference) versus the constraints of limited battery capacity and thermal envelopes.

Computation offloading—the transfer of computational tasks from a resource-constrained device to a resource-rich edge server—is the primary mechanism to resolve this conflict. However, offloading is not a panacea; it introduces transmission energy costs and network latency. Therefore, the central optimization problem is determining the **offloading decision** (local vs. remote), **resource allocation** (transmit power, bandwidth), and **scheduling** that minimizes a weighted cost function of latency and energy consumption.

This report provides an exhaustive analysis of computation offloading strategies. It synthesizes recent research to demonstrate that hybrid algorithms combining **Lyapunov optimization** with **Deep Reinforcement Learning (DRL)** currently offer the most robust solution for maximizing comprehensive performance. Furthermore, it analyzes the impact of next-generation hardware on these software decisions.

---

## 2. The IoT Edge Dilemma: Latency vs. Energy

The comprehensive performance of an IoT node is typically modeled as a utility function or a cost minimization problem. The system aims to minimize the weighted sum of execution delay and energy consumption.

### 2.1 The Cost Model
The total cost ($C$) for a task $k$ is generally formulated as:
\[ C_k = w_t T_k + w_e E_k \]
Where:
*   $T_k$ is the total time (processing + transmission + waiting).
*   $E_k$ is the total energy consumed.
*   $w_t$ and $w_e$ are weighting factors representing the application's preference for speed versus battery conservation [cite: 12, 13].

### 2.2 Local Execution Constraints
Local execution avoids transmission delays but incurs high processing energy and potential queuing delays if the local CPU is overwhelmed. The energy consumption is proportional to $f^3$ (where $f$ is the CPU frequency), meaning high-speed local processing drains batteries non-linearly [cite: 14].

### 2.3 Offloading Constraints
Offloading reduces local processing load but introduces:
1.  **Transmission Energy:** Dependent on the distance to the base station and channel interference.
2.  **Transmission Delay:** A function of available bandwidth and channel state information (CSI).
3.  **Edge Server Latency:** While edge servers are powerful, they are not infinite; queuing delays at the server can negate the benefits of offloading [cite: 12, 15].

---

## 3. Hardware Evolution: The Shift Toward Local Processing

Before analyzing software strategies, it is crucial to acknowledge that the "best" strategy is hardware-dependent. Recent advancements in edge AI hardware have shifted the equilibrium point of the offloading decision.

### 3.1 Next-Generation NPUs
The introduction of specialized Neural Processing Units (NPUs) like the **Arm Ethos-U85** and **Ambiq Atomiq SoC** has dramatically improved local efficiency.
*   **Performance:** The Ethos-U85 delivers up to 4 TOPS (Tera Operations Per Second) and supports transformer networks locally, a task previously reserved for cloud/edge servers [cite: 6, 7].
*   **Efficiency:** These chips utilize sub-threshold and near-threshold voltage operations, improving power efficiency by approximately 20% compared to predecessors. This allows for "always-on" AI classification directly on sensors (e.g., IMUs) without waking the main application processor [cite: 5].

### 3.2 Impact on Offloading Strategy
With hardware capable of 200 GOPS (Giga Operations Per Second) at microwatt power levels, the energy cost of *transmission* often exceeds the energy cost of *local computation* for small to medium inference tasks. Consequently, the optimal offloading strategy for modern nodes is increasingly **conservative**, offloading only the most computationally intensive or data-heavy tasks that exceed the local NPU's memory capacity [cite: 5, 16].

---

## 4. Theoretical Frameworks for Offloading Strategies

To solve the optimization problem described in Section 2, researchers employ three primary theoretical frameworks.

### 4.1 Lyapunov Optimization
Lyapunov optimization is a control-theoretic approach used to stabilize dynamic systems. In IoT offloading, it is used to manage **queues** (task buffers and battery energy levels).
*   **Mechanism:** It constructs a "Lyapunov drift-plus-penalty" function. This technique transforms a long-term stochastic optimization problem (e.g., "maximize battery life over a year") into a series of deterministic per-time-slot problems.
*   **Advantage:** It guarantees system stability (e.g., the task queue will not grow infinitely, and the battery will not deplete) without requiring knowledge of future events [cite: 8, 9, 14].
*   **Limitation:** While it ensures stability, solving the per-slot problem can still be computationally intensive if the solution space is non-convex (Mixed-Integer Non-Linear Programming, MINLP) [cite: 1, 3].

### 4.2 Deep Reinforcement Learning (DRL)
DRL agents (e.g., Deep Q-Networks, Actor-Critic) learn optimal policies by interacting with the environment.
*   **Mechanism:** The IoT device observes the state (channel quality, battery level, task queue) and takes an action (offload vs. local). It receives a reward (negative cost) and updates its neural network.
*   **Advantage:** DRL excels in dynamic environments where channel models are complex or unknown. It can learn subtle patterns that heuristic algorithms miss [cite: 12, 17, 18].
*   **Limitation:** Pure DRL suffers from the "curse of dimensionality," slow convergence, and a lack of safety guarantees. A DRL agent might make a decision that violates a hard constraint (e.g., draining the battery below a critical threshold) during the exploration phase [cite: 1, 2].

### 4.3 Game Theory
Game theory models the offloading process as a competition or cooperation between multiple IoT devices and edge servers.
*   **Mechanism:** Devices compete for limited bandwidth or server processing slots. The solution seeks a **Nash Equilibrium**, where no device can improve its utility by unilaterally changing its strategy.
*   **Advantage:** Essential for multi-user interference scenarios and pricing models in commercial MEC [cite: 17, 19].
*   **Limitation:** Often assumes rational actors and static environments, which may not hold in highly volatile wireless channels.

---

## 5. The Superior Strategy: Lyapunov-Guided DRL

Research consistently identifies the integration of Lyapunov optimization with Deep Reinforcement Learning as the strategy yielding the best comprehensive performance. This hybrid approach mitigates the instability of DRL and the computational complexity of pure optimization methods.

### 5.1 LyDROO: Lyapunov-Guided Deep Reinforcement Learning for Online Offloading
**LyDROO** represents the state-of-the-art in minimizing computation cost while ensuring queue stability.

*   **How it Works:**
    1.  **Lyapunov Decoupling:** The algorithm uses Lyapunov optimization to decouple the long-term constraints (e.g., average power consumption) from the immediate objective. This transforms the complex, multi-stage stochastic problem into a deterministic problem for the current time slot [cite: 3, 10].
    2.  **DRL for Sub-problems:** The per-slot problem is typically a non-convex MINLP (Mixed-Integer Non-Linear Programming). Instead of using a slow numerical solver, LyDROO uses a Deep Neural Network (DNN) to generate offloading actions.
    3.  **Label Generation:** The optimal solution for the *current* simplified slot (generated by a traditional solver on a small scale) is used to train the DNN. This allows the DNN to "imitate" the optimal solver but run much faster during inference [cite: 20, 21].

*   **Performance Metrics:**
    *   **Accuracy:** LyDROO achieves computation performance greater than 99% of the optimal offline solution (which requires perfect future knowledge).
    *   **Speed:** It reduces CPU execution latency by orders of magnitude compared to traditional optimization solvers, making it feasible for real-time IoT implementation [cite: 3, 22].
    *   **Stability:** Unlike pure DRL, LyDROO guarantees that data queues remain stable and average power constraints are met [cite: 10].

### 5.2 LyA3C: Lyapunov-Guided Asynchronous Advantage Actor-Critic
Building on the concepts of LyDROO, **LyA3C** utilizes the A3C (Asynchronous Advantage Actor-Critic) algorithm to further enhance learning efficiency in multi-terminal environments.

*   **Architecture:** It employs a parallel training mechanism where multiple "worker" agents interact with the environment and update a global network asynchronously.
*   **Performance:**
    *   **Convergence:** LyA3C converges more stably than standard A2C or Deep Deterministic Policy Gradient (DDPG) methods.
    *   **Throughput:** Experiments demonstrate that LyA3C improves the long-term network computation rate by **2.8% to 5.7%** compared to A2C and TD3-based algorithms, respectively [cite: 1, 4].
    *   **Application:** It is particularly effective in industrial IoT (IIoT) scenarios where tasks are delay-sensitive and arrive dynamically [cite: 4].

### 5.3 DAEE: Delay-Aware Energy-Efficient Algorithm
Another derivative of the Lyapunov approach is the **DAEE** algorithm.
*   **Mechanism:** It constructs a "virtual queue" representing the task deadline constraints. It adaptively offloads more tasks when the network quality is high and delays transmission when connectivity is poor, provided the deadline is not violated.
*   **Trade-off:** DAEE theoretically proves an $[O(1/V), O(V)]$ trade-off between energy consumption and queue backlog (delay), where $V$ is a control parameter. This allows system designers to tune the system explicitly for "Power Saving" or "Ultra-Low Latency" modes [cite: 8, 23, 24].

---

## 6. Comparative Analysis of Strategies

The following table synthesizes the performance characteristics of the primary offloading strategies found in the research.

| Strategy | Real-Time Response | Energy Efficiency | Stability (Queue/Battery) | Computational Overhead | Best Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Local Execution (NPU)** | High (for supported tasks) | High (with Ethos-U85) | N/A | Low | Privacy-sensitive, small-model inference [cite: 6]. |
| **Binary Offloading (Heuristic)** | Low to Medium | Medium | Low | Very Low | Simple sensors, static environments [cite: 25]. |
| **Pure Lyapunov Optimization** | Medium | High | **Very High** | High (Solver dependent) | Delay-tolerant apps requiring strict battery guarantees [cite: 14]. |
| **Pure DRL (DQN/DDPG)** | High | Medium | Low (Variance) | Medium | Highly dynamic channels, unknown models [cite: 12, 26]. |
| **LyDROO / LyA3C (Hybrid)** | **Very High** | **Very High** | **High** | Low (Inference) | **Complex IoT Edge nodes requiring optimal trade-offs** [cite: 3, 4]. |
| **Game Theory (Nash)** | Medium | Medium | Medium | High | Multi-user interference scenarios [cite: 19]. |

### 6.1 Why Pure DRL Falls Short
While DRL (e.g., DQN) can outperform heuristic methods by 30-50% in terms of energy/latency reduction [cite: 26, 27], it struggles with **hard constraints**. A pure DRL agent learns by trial and error; in an IoT context, an "error" could mean depleting the battery below the level required to send a distress signal. Lyapunov-guided methods enforce these constraints mathematically, preventing the DRL agent from exploring "unsafe" actions [cite: 1, 2].

### 6.2 The Role of Federated Learning
To further reduce the energy cost of the *offloading decision itself*, **Federated Learning (FL)** is employed. Instead of sending raw training data to a central server to train the DRL agent (which consumes bandwidth), IoT devices train local models and share only model updates.
*   **LyFOTO:** A Lyapunov-guided Federated DRL algorithm. It balances system throughput and battery energy while preserving privacy. It is shown to outperform benchmark algorithms in maximizing throughput while adhering to energy thresholds [cite: 24].

---

## 7. Advanced Scenarios and Considerations

### 7.1 Sequential Task Dependencies (DAGs)
Real-world applications (e.g., AR/VR, facial recognition) are not single atomic tasks but Directed Acyclic Graphs (DAGs) of dependent sub-tasks.
*   **Challenge:** Offloading a sub-task requires transferring its input data. If the predecessor task was local and the successor is remote, high transmission costs occur.
*   **Strategy:** Algorithms must consider the **critical path** of the DAG.
*   **Solution:** The **MCE-GA** (Multi-population Cooperative Elite Genetic Algorithm) and specific DRL-based DAG schedulers are used to partition these graphs. MCE-GA has shown overhead reductions of up to 72.4% compared to baselines by optimizing the partition point of the DAG [cite: 28, 29].

### 7.2 Energy Harvesting (EH)
For IoT nodes powered by solar or RF harvesting, the offloading strategy must account for energy arrival stochasticity.
*   **Virtual Energy Queues:** Lyapunov optimization is uniquely suited here. It models the battery as a queue with stochastic arrivals (harvested energy) and departures (consumed energy). The algorithm ensures the "energy queue" never hits zero.
*   **Performance:** Lyapunov-based online algorithms for EH systems can find optimal trade-offs without a priori knowledge of energy arrival rates, making them realistic for solar-powered sensors [cite: 9, 11].

### 7.3 Multi-Access and Cooperative Edge
In dense IoT deployments, a node might have choices: offload to Edge Server A, Edge Server B, or the Cloud.
*   **Cooperative Computing:** Tasks can be split, with parts processed locally, parts at the edge, and parts in the cloud.
*   **Result:** Research indicates that **DRCOM** (Deep Reinforcement Learning for Computation Offloading) and similar cooperative strategies can increase computation rates by 142% compared to local-only execution by effectively utilizing the entire vertical hierarchy (End-Edge-Cloud) [cite: 30, 31].

---

## 8. Conclusion

To achieve the best comprehensive performance in IoT edge nodes, weighing real-time response against battery life, the research conclusively points toward **Lyapunov-guided Deep Reinforcement Learning (DRL)** strategies, specifically frameworks like **LyDROO** and **LyA3C**.

These hybrid strategies succeed because they:
1.  **Decouple Complexity:** Use Lyapunov optimization to handle long-term stability (battery life, queue limits) and transform the problem into manageable short-term decisions.
2.  **Adapt Intelligently:** Use DRL to navigate the complex, non-linear trade-offs of channel interference and server availability in real-time, without needing computationally expensive iterative solvers on the device.
3.  **Guarantee Stability:** Unlike pure AI approaches, they mathematically ensure that critical constraints (like not running out of battery) are respected.

However, the implementation of these software strategies must be contextualized by the hardware. With the advent of **sub-threshold NPUs (e.g., Arm Ethos-U85)**, the "zero-offload" (local execution) strategy is becoming increasingly viable for standard inference tasks. Therefore, the ultimate strategy is a **Lyapunov-guided DRL agent running on a high-efficiency NPU**, capable of dynamically deciding when the task complexity truly warrants the energy cost of wireless transmission.

### References
[cite: 5, 6, 7] Hardware advancements (Arm Ethos-U85, Ambiq).
[cite: 12, 13, 15] Cost models and QoS metrics.
[cite: 8, 9, 14, 23, 24] Lyapunov optimization and DAEE.
[cite: 1, 4] LyA3C and DRL comparisons.
[cite: 2, 3, 10, 20, 21, 22] LyDROO framework and performance.
[cite: 28, 29] DAG and dependent task offloading.
[cite: 17, 19] Game theory and multi-user scenarios.
[cite: 9, 11] Energy harvesting considerations.
[cite: 26, 27] DRL performance improvements over heuristics.

**Sources:**
1. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd-TAfdCZtoSyVp9Q2jo2G2Je5yNfuOnWjZ_tIzJgXAKbF5aX5DyazzCh4H5yteGyHv8vqoJw0igdR8cgcD-1EcnSDtn8gnyIh-0KY0XQfHMUe091mjHiELll9AUovPQA=)
2. [atlantis-press.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEO1VopscMgUJsC7lArwbOsbPTJjRnitLu7_es3uHVgij_8iq-F8yDt9keyPWEUNxnN-RlBHO3kqTmSlBVqKBX2Srb57UL0cGO67YgahSd836XO2vpO_R2I-g6MPLAq_lE-z_jE1-5emxng)
3. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxot0fEUVSFibdNKOP89x-S3CjshZlDSY-zjudO1xuh0VIv07Hao0rz35sBnvdyiEfMoTEPuTBF1fezN5tzDD6MSTY0_vZWjGUE5xmpmqpK5C9qS3K_Q==)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqrCnkClfyw75rgUPAY-_LmKtCFor2W912UJAIeqYFTESe1JDPCNyxHwox9BD-XBbSl-H9yP9kk-bS7EATPVIcgKuwQBwPEmhfw4UbWqjs61oJzzuNzSaADNAS7zqCH-wukS2ZeNyajRgcvsM9VyN90FuBF0gtO_AJVgPWy0R5SxfHv_9K0HqnzAfS_t3opW9pM3tWMR8GeaM-DZSBw874BsgR2dPB59SsaWBJgJnJqrK_oc78PWWd67VE_Lb7sepPF788lymjn05V)
5. [edn.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHy3uR9ZpcEcNZgyW82ApfnIBnmtNyUnt8e9KQv-pVU65CHbPGSklEY5zTGYhyEBAhi1_iMLkYmDeubnf9iT6NrAB5kzAoLaPzGMSD_LzpqVMI8ihT5U9rvlZ6O5c4i5r7YV6o7IMFheYtBq6gGngRRSfPVuET5A==)
6. [arm.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy7z8jZFlTDR3VdV4zMSUMt2o4zLJ18fXfi0HHO-rllEPcBHf0EMqK2YYY8ILIGYSRxq--nB1fk9cgkJDeoYZpCwIeaY5gcBjq5rO2ysobkwm68MztCI2BkS3HMHc=)
7. [allaboutcircuits.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFARZWoUOrOOm2h9NZH0lihu7xYvLel6LqN0Od812qLV4KyQrEFMjQB28v89Ysam06RDar0k3G1qWvKRbfIsviRInH1KjN0hLsyW82zKf-3iOWA7WW2rmaIrnol3RYeIlUJ3HnwjcVSZEcAXQubwg3YOXMZw3B9F8zS-BD4akmpOlaoACA1pkFABvhSyrIExl1uEhhhdLnKO4I=)
8. [tju.edu.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_aE7dOIeWJ1yuIuW7h_O-LwWSZz1Bv2dmMNoyF3ORAzJWNw3gJ8sOFbtrjYJW6MfknoU75qVwwoah8D1zfz86c_aFRtim_FqpEvfgZBzFlFY9DwF_-5SMJrwnrGiLOE6W_jJmEnw_paQtSoS8xw==)
9. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE143Llm2yxCGR1X0z8Bn6zfygbY7po8CPcdf5Dybd0eHJzdqQDnc6VXEkj-MOoaeCScLXrF-5YvIh9zLC5buiCfRJ3rsCh6dyDe0QHa9RkZoDdnHS0ICMw9FCZmeke)
10. [bisuzhi.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyAGTY3Qd2EtpN5cerM_cIRW52GzWNJALmHul6l0oNhqA6NFxdHy8GtheCEJFLTIEDb6XWnMmvS7-M-c86CL2MPLS8fMzcQ1-hFwWb0HMOZ_XXMVU7ZCylXirUnsx3iww=)
11. [uwaterloo.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEn9WyPwLN-xwcIIH4ZXYqTubEJFLzYrwAUX4m-cjYThifro0Vs6RQQVwCKhBDIQJ1w__SHxgD5koVnkXkzLGM2G7xWZnn0p0DkGXrCuXfhd6gaH4iqYuX3o9Ew-xBoPccR7WeUouXrQCKyh3cZoRqF2IlztljsLHpZSY5K2A5wxZqbE7i9KFvB3I5WqmHXY6JnJdsFkhOOTEJh5ohyOvjZdkJMjrkPjOzKBI0nw47FLqMrVRnCMb2e0X6Bgd-bUn_9sz-FcNd4aw==)
12. [preprints.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoI2EDGvJpNb0CLWR74CoLcjR0z-jrhIn7vAwBa_0QOZYEdjWye0xIx4zLERS2L4tbD0pv4CYRaMroDQ8uG5wlS6NDZdhKMJkYqM1c5F5_PQkH1Jw8U6Yjxeg3SewpvCzlGDg0F_s=)
13. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIzdMdYBlatgveUzoq1kWxjz9jxh7drGTuisQNJsZ9OQx7YtSSy5kSzzLj2bSmDTwrXYBltvIu4d9HhJbxPuIn4FVGhbZ4hZ4SHI1_oDfd9uO7Uqhy0eW7YlctDvmA-rBF7I4Nz98H5tXKeEx2un5ca4hc)
14. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKAsSMJ2w5gEyAAQDfWS2LYVg-OHZiqU87tfPia_4lMye79qvuijD67dzUSYbLNtQG9miVCU2g92qOioy8lH3jEmbsm2arjAHNs-HnYKC-VP2nohY8yg==)
15. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGA1Mlid9tRgnzDeK7AG5QFzWgoQXPsfhCd1jo-kERV_WiIAMVK3UUCgrkk1fmJ-ewNK0aphp9jeRvYAoCF--iP2CqFDUL0zF8hZ2PzYv2pVavGBVYtcA9dl-uIxuZKtZSY)
16. [digica.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEV67cHnyOuZsBoVAz4_U4eDevFaosZjlHkalzRG6CFlzimwuKJuZL0aj6O9cgE3vXf69cZfprTRV7lfhsG-QNnoFixIJmR46OjE0xNp1Tt71i9XkVYpTjTza82tm0egU2WX-b5d_9mt2-OQgThj1DFvbFWEzjiEJpOtKzYOHgJLlXrWuRCaHSfSMsLD9z0OYQ-9vJbtRs=)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmIAY-l_bT6bYbo0MLzp0Fwxi4jXIGjfRZVVAuwzlGdB47MyU0r5NwixEhD0cM-bsBnAtVlItiZ_5KgPVKDW5KW2l_qGOZwW6039fibq7JMT30pBxh-J2X_hg97b1KpnjYLNCypYqULfbiyBWjtRyo-omI6PpMJ2crW6Gxp6TGx2g8ACyATdaHgLMEpIAYhKQV1-gRV9oQOgSAu9K_SethXs3NKXxANBkbcGLNw6bLgY9LzlYXBWXytvXipsnQ5NY3kyi0p1UXmljWdVGhsKvwS_E=)
18. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjmIPbj9wUKDv6dER7LPRpNKgW3J_QjWAbTJCQpejF8yHuQM_bUHC0sBHvqjRhO4h1aaFmZzirJZvnbYKmLpvWLFZvAGPInj3jHmtMdKnaqWht3HfhIQ==)
19. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXdphMTX-KDKM9QNyzwRjbi7r8R_MRE4DdBIhP7IFNdT3w_F69lyh0zEUR4LkoHbzjTvGwD_Iw8akoFtu3iP_c8I1kX5sPM6YgjmwEjn4Mhyi27tfTSPCjUKaULuo1fg==)
20. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNG28UCWjuiToZHlWQmQe6HTrnTNw_g2tAxS1ynRH6O62Jg3WM8_QNKabkhhpcWgX8j8X91vZrwNa6-x-KfaxI10Fig7RYwzsPDap3dnBPSheu23AtLw==)
21. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOOrTz50RBozCGadoMSwNtVqrlYdt4pzFnagx3WxtSJNXBC5nNCg1LG9TJC4EadAR9UX964TwuHjsOpG3rfSt0WeXi7P7uN8Sr57df9PtBChVZQCFjk7mzaL303q9DTVdOnlXOMU15dtMKj28Aj5iAA7-6g5rjDX6Etfb5J0K8iAv3DQBoefk0affckmXD8CGaEAIwb3Ezse1T0LS9dpFM4puFhQ-XNRM2Z8X3cpPhUrqAYYgmyVNH9hBu5XbCTpmWYkVL4AKMe_Z7LzjSWOc6bIoCRUC9yVGnM2yy2XbpDA==)
22. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmT0ben8F7SNs8WUIVBb8FO0pH9IUQju1HVM3VGsmuXDu6fX5pvGA_TUERL9BTvJvYimgQQyITff5Z6WZ662EP2K7tfPy-qwK16O_46CAvJw16kwrAFcQ=)
23. [kennesaw.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFumrPhUL5u4Dg0i2tPGFX2VjI8whaNw_JRpVe3zSa4MDhLNPIOjxkh69lcMOxoYN368TK2pRLdKvk1hl7b2CZ23IhAYCDIgR8fjsPSnn1PZWe3fK5yHKBwKpLb2j7HYfdu2jGPMWqV)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiYkbjlfkfEWItPkjdwxRq_T9PPma8iCX0ySHxsjg7T6My0jeCf6iauaok6xMeawf5iCuU__iqiMnfPGM9wH6-N7nXIWeAL9z9OSacV8JIYkxEuPqM9F_vryE1_2JZGCDzlIGFonEmRAuPQrnbOYg12oLqXnGroOEw3CzrwwZmePe9f4cbZQSRXZ8utyEvOU1ZtA-I_UW3aBgRsYDl9wBT3YIIBJghLK4A8wRa1YcZ_CILUAk=)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEL_zIXEdG6n97lWEZjIN8ccRseQ3-4jazH6PXhHZbqnbkqmt1HlsXus3ylFbdMw5DL-PffVVswE53Iex4s3FB1I6_hfREo6bNik4GnBT4CaCv0NV5FoGHyF70HS9w6CQGj0PatDiv83Odn0ooB4Jf54eVuMxkBfNat7oPZoJlPf_gNgCJoulXwaAH0oGehsEAZZEjA44nFJ0KcJ9Iu)
26. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeHOeTtxmQNPbZ1PkNo0jjy12XUObtxtibJif45zT2JoJDkVUlyVgVhC9eapBA4awbWInTt3SNyGcZaL1nhIQuPon4CVgzH-tCoMR-1EABWDylUI_IYJsM1RByuqwsdg==)
27. [preprints.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGB2qO62_gSAX2jZzi2pKdVX-Nrnb2dYcJaah7m9CCZN2VbGnrSnC44hHpGAh4KzPDZq0Z-oiT4p1WfcCN3blxpiK_zg1bX7wTMy7VQoXmc22ou5ziav1eHgl4NX-3wVuuJmq1T5mM=)
28. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbddZL0CNhC4tS0bWSZze4-17sMYKezM-7Sz3HDpShQm7_qDDSgqOPABMSDqWPt-FKJPAODUwAuTvEKelGQ0ae7h-LGki8fpUZLkZJNa-18bTpGWYBSP14ZF82e3o=)
29. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElRbFQiF29gUknVtp_Z-86Lel06biGgK127hfijqfE8QBONS9xF6wb9qtAljhhJOqRrm4Jbya7PYUvkgdNBA8FgVs_g66nzmzBL-cOhU4ATuKVoMYLrwQSejJfCSq_SPHfK5GjvcqZU6kW9yuJVi9UlHQQlsj1pgf3yQwRKPA4jU3VkWg5Rw0JPwH_ja-bK25pamk479XyD3W0myaXjjAhnibxo3-AiQxZk1Gqjy8pbErM2thFLE6tsjg1fhStJkQ8nrWYS89sEHWezQBy5OjVlNl5KkA=)
30. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfSRZUB-pyD1VChFGx1sZY0uBRDg8TUvBXI9HpQ4Hm4rS76maZuU2Ruk29gEss3VcJkFPFvRKSbQ82V4NJt0rcG0T_RAdAE7C3O2AZJi48x23J4fA-v6SflQKXGw==)
31. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-u1npSYElmVuV-I6ux4GET1IRf95refH8J7fzrloQT5JIAV8KKOk0btj8_gc1aJuV4uEiu2xitgSMrwdktYXsMpsAyCi9W4wX_NLr4aa-wO7g0p9UkjpenXL0UuA=)


## Annotations
Annotation(end_index=549, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEO1VopscMgUJsC7lArwbOsbPTJjRnitLu7_es3uHVgij_8iq-F8yDt9keyPWEUNxnN-RlBHO3kqTmSlBVqKBX2Srb57UL0cGO67YgahSd836XO2vpO_R2I-g6MPLAq_lE-z_jE1-5emxng', start_index=531)
Annotation(end_index=549, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqrCnkClfyw75rgUPAY-_LmKtCFor2W912UJAIeqYFTESe1JDPCNyxHwox9BD-XBbSl-H9yP9kk-bS7EATPVIcgKuwQBwPEmhfw4UbWqjs61oJzzuNzSaADNAS7zqCH-wukS2ZeNyajRgcvsM9VyN90FuBF0gtO_AJVgPWy0R5SxfHv_9K0HqnzAfS_t3opW9pM3tWMR8GeaM-DZSBw874BsgR2dPB59SsaWBJgJnJqrK_oc78PWWd67VE_Lb7sepPF788lymjn05V', start_index=531)
Annotation(end_index=549, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd-TAfdCZtoSyVp9Q2jo2G2Je5yNfuOnWjZ_tIzJgXAKbF5aX5DyazzCh4H5yteGyHv8vqoJw0igdR8cgcD-1EcnSDtn8gnyIh-0KY0XQfHMUe091mjHiELll9AUovPQA=', start_index=531)
Annotation(end_index=549, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxot0fEUVSFibdNKOP89x-S3CjshZlDSY-zjudO1xuh0VIv07Hao0rz35sBnvdyiEfMoTEPuTBF1fezN5tzDD6MSTY0_vZWjGUE5xmpmqpK5C9qS3K_Q==', start_index=531)
Annotation(end_index=948, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHy3uR9ZpcEcNZgyW82ApfnIBnmtNyUnt8e9KQv-pVU65CHbPGSklEY5zTGYhyEBAhi1_iMLkYmDeubnf9iT6NrAB5kzAoLaPzGMSD_LzpqVMI8ihT5U9rvlZ6O5c4i5r7YV6o7IMFheYtBq6gGngRRSfPVuET5A==', start_index=933)
Annotation(end_index=948, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFARZWoUOrOOm2h9NZH0lihu7xYvLel6LqN0Od812qLV4KyQrEFMjQB28v89Ysam06RDar0k3G1qWvKRbfIsviRInH1KjN0hLsyW82zKf-3iOWA7WW2rmaIrnol3RYeIlUJ3HnwjcVSZEcAXQubwg3YOXMZw3B9F8zS-BD4akmpOlaoACA1pkFABvhSyrIExl1uEhhhdLnKO4I=', start_index=933)
Annotation(end_index=948, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy7z8jZFlTDR3VdV4zMSUMt2o4zLJ18fXfi0HHO-rllEPcBHf0EMqK2YYY8ILIGYSRxq--nB1fk9cgkJDeoYZpCwIeaY5gcBjq5rO2ysobkwm68MztCI2BkS3HMHc=', start_index=933)
Annotation(end_index=1309, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE143Llm2yxCGR1X0z8Bn6zfygbY7po8CPcdf5Dybd0eHJzdqQDnc6VXEkj-MOoaeCScLXrF-5YvIh9zLC5buiCfRJ3rsCh6dyDe0QHa9RkZoDdnHS0ICMw9FCZmeke', start_index=1293)
Annotation(end_index=1309, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyAGTY3Qd2EtpN5cerM_cIRW52GzWNJALmHul6l0oNhqA6NFxdHy8GtheCEJFLTIEDb6XWnMmvS7-M-c86CL2MPLS8fMzcQ1-hFwWb0HMOZ_XXMVU7ZCylXirUnsx3iww=', start_index=1293)
Annotation(end_index=1309, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_aE7dOIeWJ1yuIuW7h_O-LwWSZz1Bv2dmMNoyF3ORAzJWNw3gJ8sOFbtrjYJW6MfknoU75qVwwoah8D1zfz86c_aFRtim_FqpEvfgZBzFlFY9DwF_-5SMJrwnrGiLOE6W_jJmEnw_paQtSoS8xw==', start_index=1293)
Annotation(end_index=1642, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE143Llm2yxCGR1X0z8Bn6zfygbY7po8CPcdf5Dybd0eHJzdqQDnc6VXEkj-MOoaeCScLXrF-5YvIh9zLC5buiCfRJ3rsCh6dyDe0QHa9RkZoDdnHS0ICMw9FCZmeke', start_index=1629)
Annotation(end_index=1642, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEn9WyPwLN-xwcIIH4ZXYqTubEJFLzYrwAUX4m-cjYThifro0Vs6RQQVwCKhBDIQJ1w__SHxgD5koVnkXkzLGM2G7xWZnn0p0DkGXrCuXfhd6gaH4iqYuX3o9Ew-xBoPccR7WeUouXrQCKyh3cZoRqF2IlztljsLHpZSY5K2A5wxZqbE7i9KFvB3I5WqmHXY6JnJdsFkhOOTEJh5ohyOvjZdkJMjrkPjOzKBI0nw47FLqMrVRnCMb2e0X6Bgd-bUn_9sz-FcNd4aw==', start_index=1629)
Annotation(end_index=3707, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIzdMdYBlatgveUzoq1kWxjz9jxh7drGTuisQNJsZ9OQx7YtSSy5kSzzLj2bSmDTwrXYBltvIu4d9HhJbxPuIn4FVGhbZ4hZ4SHI1_oDfd9uO7Uqhy0eW7YlctDvmA-rBF7I4Nz98H5tXKeEx2un5ca4hc', start_index=3693)
Annotation(end_index=3707, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoI2EDGvJpNb0CLWR74CoLcjR0z-jrhIn7vAwBa_0QOZYEdjWye0xIx4zLERS2L4tbD0pv4CYRaMroDQ8uG5wlS6NDZdhKMJkYqM1c5F5_PQkH1Jw8U6Yjxeg3SewpvCzlGDg0F_s=', start_index=3693)
Annotation(end_index=4043, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKAsSMJ2w5gEyAAQDfWS2LYVg-OHZiqU87tfPia_4lMye79qvuijD67dzUSYbLNtQG9miVCU2g92qOioy8lH3jEmbsm2arjAHNs-HnYKC-VP2nohY8yg==', start_index=4033)
Annotation(end_index=4500, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGA1Mlid9tRgnzDeK7AG5QFzWgoQXPsfhCd1jo-kERV_WiIAMVK3UUCgrkk1fmJ-ewNK0aphp9jeRvYAoCF--iP2CqFDUL0zF8hZ2PzYv2pVavGBVYtcA9dl-uIxuZKtZSY', start_index=4486)
Annotation(end_index=4500, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoI2EDGvJpNb0CLWR74CoLcjR0z-jrhIn7vAwBa_0QOZYEdjWye0xIx4zLERS2L4tbD0pv4CYRaMroDQ8uG5wlS6NDZdhKMJkYqM1c5F5_PQkH1Jw8U6Yjxeg3SewpvCzlGDg0F_s=', start_index=4486)
Annotation(end_index=5167, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFARZWoUOrOOm2h9NZH0lihu7xYvLel6LqN0Od812qLV4KyQrEFMjQB28v89Ysam06RDar0k3G1qWvKRbfIsviRInH1KjN0hLsyW82zKf-3iOWA7WW2rmaIrnol3RYeIlUJ3HnwjcVSZEcAXQubwg3YOXMZw3B9F8zS-BD4akmpOlaoACA1pkFABvhSyrIExl1uEhhhdLnKO4I=', start_index=5155)
Annotation(end_index=5167, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy7z8jZFlTDR3VdV4zMSUMt2o4zLJ18fXfi0HHO-rllEPcBHf0EMqK2YYY8ILIGYSRxq--nB1fk9cgkJDeoYZpCwIeaY5gcBjq5rO2ysobkwm68MztCI2BkS3HMHc=', start_index=5155)
Annotation(end_index=5470, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHy3uR9ZpcEcNZgyW82ApfnIBnmtNyUnt8e9KQv-pVU65CHbPGSklEY5zTGYhyEBAhi1_iMLkYmDeubnf9iT6NrAB5kzAoLaPzGMSD_LzpqVMI8ihT5U9rvlZ6O5c4i5r7YV6o7IMFheYtBq6gGngRRSfPVuET5A==', start_index=5461)
Annotation(end_index=5950, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHy3uR9ZpcEcNZgyW82ApfnIBnmtNyUnt8e9KQv-pVU65CHbPGSklEY5zTGYhyEBAhi1_iMLkYmDeubnf9iT6NrAB5kzAoLaPzGMSD_LzpqVMI8ihT5U9rvlZ6O5c4i5r7YV6o7IMFheYtBq6gGngRRSfPVuET5A==', start_index=5937)
Annotation(end_index=5950, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEV67cHnyOuZsBoVAz4_U4eDevFaosZjlHkalzRG6CFlzimwuKJuZL0aj6O9cgE3vXf69cZfprTRV7lfhsG-QNnoFixIJmR46OjE0xNp1Tt71i9XkVYpTjTza82tm0egU2WX-b5d_9mt2-OQgThj1DFvbFWEzjiEJpOtKzYOHgJLlXrWuRCaHSfSMsLD9z0OYQ-9vJbtRs=', start_index=5937)
Annotation(end_index=6779, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE143Llm2yxCGR1X0z8Bn6zfygbY7po8CPcdf5Dybd0eHJzdqQDnc6VXEkj-MOoaeCScLXrF-5YvIh9zLC5buiCfRJ3rsCh6dyDe0QHa9RkZoDdnHS0ICMw9FCZmeke', start_index=6763)
Annotation(end_index=6779, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKAsSMJ2w5gEyAAQDfWS2LYVg-OHZiqU87tfPia_4lMye79qvuijD67dzUSYbLNtQG9miVCU2g92qOioy8lH3jEmbsm2arjAHNs-HnYKC-VP2nohY8yg==', start_index=6763)
Annotation(end_index=6779, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_aE7dOIeWJ1yuIuW7h_O-LwWSZz1Bv2dmMNoyF3ORAzJWNw3gJ8sOFbtrjYJW6MfknoU75qVwwoah8D1zfz86c_aFRtim_FqpEvfgZBzFlFY9DwF_-5SMJrwnrGiLOE6W_jJmEnw_paQtSoS8xw==', start_index=6763)
Annotation(end_index=6991, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd-TAfdCZtoSyVp9Q2jo2G2Je5yNfuOnWjZ_tIzJgXAKbF5aX5DyazzCh4H5yteGyHv8vqoJw0igdR8cgcD-1EcnSDtn8gnyIh-0KY0XQfHMUe091mjHiELll9AUovPQA=', start_index=6979)
Annotation(end_index=6991, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxot0fEUVSFibdNKOP89x-S3CjshZlDSY-zjudO1xuh0VIv07Hao0rz35sBnvdyiEfMoTEPuTBF1fezN5tzDD6MSTY0_vZWjGUE5xmpmqpK5C9qS3K_Q==', start_index=6979)
Annotation(end_index=7530, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjmIPbj9wUKDv6dER7LPRpNKgW3J_QjWAbTJCQpejF8yHuQM_bUHC0sBHvqjRhO4h1aaFmZzirJZvnbYKmLpvWLFZvAGPInj3jHmtMdKnaqWht3HfhIQ==', start_index=7512)
Annotation(end_index=7530, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmIAY-l_bT6bYbo0MLzp0Fwxi4jXIGjfRZVVAuwzlGdB47MyU0r5NwixEhD0cM-bsBnAtVlItiZ_5KgPVKDW5KW2l_qGOZwW6039fibq7JMT30pBxh-J2X_hg97b1KpnjYLNCypYqULfbiyBWjtRyo-omI6PpMJ2crW6Gxp6TGx2g8ACyATdaHgLMEpIAYhKQV1-gRV9oQOgSAu9K_SethXs3NKXxANBkbcGLNw6bLgY9LzlYXBWXytvXipsnQ5NY3kyi0p1UXmljWdVGhsKvwS_E=', start_index=7512)
Annotation(end_index=7530, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoI2EDGvJpNb0CLWR74CoLcjR0z-jrhIn7vAwBa_0QOZYEdjWye0xIx4zLERS2L4tbD0pv4CYRaMroDQ8uG5wlS6NDZdhKMJkYqM1c5F5_PQkH1Jw8U6Yjxeg3SewpvCzlGDg0F_s=', start_index=7512)
Annotation(end_index=7819, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEO1VopscMgUJsC7lArwbOsbPTJjRnitLu7_es3uHVgij_8iq-F8yDt9keyPWEUNxnN-RlBHO3kqTmSlBVqKBX2Srb57UL0cGO67YgahSd836XO2vpO_R2I-g6MPLAq_lE-z_jE1-5emxng', start_index=7807)
Annotation(end_index=7819, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd-TAfdCZtoSyVp9Q2jo2G2Je5yNfuOnWjZ_tIzJgXAKbF5aX5DyazzCh4H5yteGyHv8vqoJw0igdR8cgcD-1EcnSDtn8gnyIh-0KY0XQfHMUe091mjHiELll9AUovPQA=', start_index=7807)
Annotation(end_index=8288, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmIAY-l_bT6bYbo0MLzp0Fwxi4jXIGjfRZVVAuwzlGdB47MyU0r5NwixEhD0cM-bsBnAtVlItiZ_5KgPVKDW5KW2l_qGOZwW6039fibq7JMT30pBxh-J2X_hg97b1KpnjYLNCypYqULfbiyBWjtRyo-omI6PpMJ2crW6Gxp6TGx2g8ACyATdaHgLMEpIAYhKQV1-gRV9oQOgSAu9K_SethXs3NKXxANBkbcGLNw6bLgY9LzlYXBWXytvXipsnQ5NY3kyi0p1UXmljWdVGhsKvwS_E=', start_index=8274)
Annotation(end_index=8288, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXdphMTX-KDKM9QNyzwRjbi7r8R_MRE4DdBIhP7IFNdT3w_F69lyh0zEUR4LkoHbzjTvGwD_Iw8akoFtu3iP_c8I1kX5sPM6YgjmwEjn4Mhyi27tfTSPCjUKaULuo1fg==', start_index=8274)
Annotation(end_index=9279, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyAGTY3Qd2EtpN5cerM_cIRW52GzWNJALmHul6l0oNhqA6NFxdHy8GtheCEJFLTIEDb6XWnMmvS7-M-c86CL2MPLS8fMzcQ1-hFwWb0HMOZ_XXMVU7ZCylXirUnsx3iww=', start_index=9266)
Annotation(end_index=9279, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxot0fEUVSFibdNKOP89x-S3CjshZlDSY-zjudO1xuh0VIv07Hao0rz35sBnvdyiEfMoTEPuTBF1fezN5tzDD6MSTY0_vZWjGUE5xmpmqpK5C9qS3K_Q==', start_index=9266)
Annotation(end_index=9789, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNG28UCWjuiToZHlWQmQe6HTrnTNw_g2tAxS1ynRH6O62Jg3WM8_QNKabkhhpcWgX8j8X91vZrwNa6-x-KfaxI10Fig7RYwzsPDap3dnBPSheu23AtLw==', start_index=9775)
Annotation(end_index=9789, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOOrTz50RBozCGadoMSwNtVqrlYdt4pzFnagx3WxtSJNXBC5nNCg1LG9TJC4EadAR9UX964TwuHjsOpG3rfSt0WeXi7P7uN8Sr57df9PtBChVZQCFjk7mzaL303q9DTVdOnlXOMU15dtMKj28Aj5iAA7-6g5rjDX6Etfb5J0K8iAv3DQBoefk0affckmXD8CGaEAIwb3Ezse1T0LS9dpFM4puFhQ-XNRM2Z8X3cpPhUrqAYYgmyVNH9hBu5XbCTpmWYkVL4AKMe_Z7LzjSWOc6bIoCRUC9yVGnM2yy2XbpDA==', start_index=9775)
Annotation(end_index=10161, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmT0ben8F7SNs8WUIVBb8FO0pH9IUQju1HVM3VGsmuXDu6fX5pvGA_TUERL9BTvJvYimgQQyITff5Z6WZ662EP2K7tfPy-qwK16O_46CAvJw16kwrAFcQ=', start_index=10148)
Annotation(end_index=10161, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxot0fEUVSFibdNKOP89x-S3CjshZlDSY-zjudO1xuh0VIv07Hao0rz35sBnvdyiEfMoTEPuTBF1fezN5tzDD6MSTY0_vZWjGUE5xmpmqpK5C9qS3K_Q==', start_index=10148)
Annotation(end_index=10300, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyAGTY3Qd2EtpN5cerM_cIRW52GzWNJALmHul6l0oNhqA6NFxdHy8GtheCEJFLTIEDb6XWnMmvS7-M-c86CL2MPLS8fMzcQ1-hFwWb0HMOZ_XXMVU7ZCylXirUnsx3iww=', start_index=10290)
Annotation(end_index=11061, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqrCnkClfyw75rgUPAY-_LmKtCFor2W912UJAIeqYFTESe1JDPCNyxHwox9BD-XBbSl-H9yP9kk-bS7EATPVIcgKuwQBwPEmhfw4UbWqjs61oJzzuNzSaADNAS7zqCH-wukS2ZeNyajRgcvsM9VyN90FuBF0gtO_AJVgPWy0R5SxfHv_9K0HqnzAfS_t3opW9pM3tWMR8GeaM-DZSBw874BsgR2dPB59SsaWBJgJnJqrK_oc78PWWd67VE_Lb7sepPF788lymjn05V', start_index=11049)
Annotation(end_index=11061, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd-TAfdCZtoSyVp9Q2jo2G2Je5yNfuOnWjZ_tIzJgXAKbF5aX5DyazzCh4H5yteGyHv8vqoJw0igdR8cgcD-1EcnSDtn8gnyIh-0KY0XQfHMUe091mjHiELll9AUovPQA=', start_index=11049)
Annotation(end_index=11216, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqrCnkClfyw75rgUPAY-_LmKtCFor2W912UJAIeqYFTESe1JDPCNyxHwox9BD-XBbSl-H9yP9kk-bS7EATPVIcgKuwQBwPEmhfw4UbWqjs61oJzzuNzSaADNAS7zqCH-wukS2ZeNyajRgcvsM9VyN90FuBF0gtO_AJVgPWy0R5SxfHv_9K0HqnzAfS_t3opW9pM3tWMR8GeaM-DZSBw874BsgR2dPB59SsaWBJgJnJqrK_oc78PWWd67VE_Lb7sepPF788lymjn05V', start_index=11207)
Annotation(end_index=11882, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFumrPhUL5u4Dg0i2tPGFX2VjI8whaNw_JRpVe3zSa4MDhLNPIOjxkh69lcMOxoYN368TK2pRLdKvk1hl7b2CZ23IhAYCDIgR8fjsPSnn1PZWe3fK5yHKBwKpLb2j7HYfdu2jGPMWqV', start_index=11865)
Annotation(end_index=11882, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiYkbjlfkfEWItPkjdwxRq_T9PPma8iCX0ySHxsjg7T6My0jeCf6iauaok6xMeawf5iCuU__iqiMnfPGM9wH6-N7nXIWeAL9z9OSacV8JIYkxEuPqM9F_vryE1_2JZGCDzlIGFonEmRAuPQrnbOYg12oLqXnGroOEw3CzrwwZmePe9f4cbZQSRXZ8utyEvOU1ZtA-I_UW3aBgRsYDl9wBT3YIIBJghLK4A8wRa1YcZ_CILUAk=', start_index=11865)
Annotation(end_index=11882, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_aE7dOIeWJ1yuIuW7h_O-LwWSZz1Bv2dmMNoyF3ORAzJWNw3gJ8sOFbtrjYJW6MfknoU75qVwwoah8D1zfz86c_aFRtim_FqpEvfgZBzFlFY9DwF_-5SMJrwnrGiLOE6W_jJmEnw_paQtSoS8xw==', start_index=11865)
Annotation(end_index=12369, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy7z8jZFlTDR3VdV4zMSUMt2o4zLJ18fXfi0HHO-rllEPcBHf0EMqK2YYY8ILIGYSRxq--nB1fk9cgkJDeoYZpCwIeaY5gcBjq5rO2ysobkwm68MztCI2BkS3HMHc=', start_index=12360)
Annotation(end_index=12499, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEL_zIXEdG6n97lWEZjIN8ccRseQ3-4jazH6PXhHZbqnbkqmt1HlsXus3ylFbdMw5DL-PffVVswE53Iex4s3FB1I6_hfREo6bNik4GnBT4CaCv0NV5FoGHyF70HS9w6CQGj0PatDiv83Odn0ooB4Jf54eVuMxkBfNat7oPZoJlPf_gNgCJoulXwaAH0oGehsEAZZEjA44nFJ0KcJ9Iu', start_index=12489)
Annotation(end_index=12662, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKAsSMJ2w5gEyAAQDfWS2LYVg-OHZiqU87tfPia_4lMye79qvuijD67dzUSYbLNtQG9miVCU2g92qOioy8lH3jEmbsm2arjAHNs-HnYKC-VP2nohY8yg==', start_index=12652)
Annotation(end_index=12790, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeHOeTtxmQNPbZ1PkNo0jjy12XUObtxtibJif45zT2JoJDkVUlyVgVhC9eapBA4awbWInTt3SNyGcZaL1nhIQuPon4CVgzH-tCoMR-1EABWDylUI_IYJsM1RByuqwsdg==', start_index=12776)
Annotation(end_index=12790, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoI2EDGvJpNb0CLWR74CoLcjR0z-jrhIn7vAwBa_0QOZYEdjWye0xIx4zLERS2L4tbD0pv4CYRaMroDQ8uG5wlS6NDZdhKMJkYqM1c5F5_PQkH1Jw8U6Yjxeg3SewpvCzlGDg0F_s=', start_index=12776)
Annotation(end_index=12955, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqrCnkClfyw75rgUPAY-_LmKtCFor2W912UJAIeqYFTESe1JDPCNyxHwox9BD-XBbSl-H9yP9kk-bS7EATPVIcgKuwQBwPEmhfw4UbWqjs61oJzzuNzSaADNAS7zqCH-wukS2ZeNyajRgcvsM9VyN90FuBF0gtO_AJVgPWy0R5SxfHv_9K0HqnzAfS_t3opW9pM3tWMR8GeaM-DZSBw874BsgR2dPB59SsaWBJgJnJqrK_oc78PWWd67VE_Lb7sepPF788lymjn05V', start_index=12943)
Annotation(end_index=12955, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxot0fEUVSFibdNKOP89x-S3CjshZlDSY-zjudO1xuh0VIv07Hao0rz35sBnvdyiEfMoTEPuTBF1fezN5tzDD6MSTY0_vZWjGUE5xmpmqpK5C9qS3K_Q==', start_index=12943)
Annotation(end_index=13064, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXdphMTX-KDKM9QNyzwRjbi7r8R_MRE4DdBIhP7IFNdT3w_F69lyh0zEUR4LkoHbzjTvGwD_Iw8akoFtu3iP_c8I1kX5sPM6YgjmwEjn4Mhyi27tfTSPCjUKaULuo1fg==', start_index=13054)
Annotation(end_index=13218, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeHOeTtxmQNPbZ1PkNo0jjy12XUObtxtibJif45zT2JoJDkVUlyVgVhC9eapBA4awbWInTt3SNyGcZaL1nhIQuPon4CVgzH-tCoMR-1EABWDylUI_IYJsM1RByuqwsdg==', start_index=13204)
Annotation(end_index=13218, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGB2qO62_gSAX2jZzi2pKdVX-Nrnb2dYcJaah7m9CCZN2VbGnrSnC44hHpGAh4KzPDZq0Z-oiT4p1WfcCN3blxpiK_zg1bX7wTMy7VQoXmc22ou5ziav1eHgl4NX-3wVuuJmq1T5mM=', start_index=13204)
Annotation(end_index=13554, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEO1VopscMgUJsC7lArwbOsbPTJjRnitLu7_es3uHVgij_8iq-F8yDt9keyPWEUNxnN-RlBHO3kqTmSlBVqKBX2Srb57UL0cGO67YgahSd836XO2vpO_R2I-g6MPLAq_lE-z_jE1-5emxng', start_index=13542)
Annotation(end_index=13554, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd-TAfdCZtoSyVp9Q2jo2G2Je5yNfuOnWjZ_tIzJgXAKbF5aX5DyazzCh4H5yteGyHv8vqoJw0igdR8cgcD-1EcnSDtn8gnyIh-0KY0XQfHMUe091mjHiELll9AUovPQA=', start_index=13542)
Annotation(end_index=14129, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiYkbjlfkfEWItPkjdwxRq_T9PPma8iCX0ySHxsjg7T6My0jeCf6iauaok6xMeawf5iCuU__iqiMnfPGM9wH6-N7nXIWeAL9z9OSacV8JIYkxEuPqM9F_vryE1_2JZGCDzlIGFonEmRAuPQrnbOYg12oLqXnGroOEw3CzrwwZmePe9f4cbZQSRXZ8utyEvOU1ZtA-I_UW3aBgRsYDl9wBT3YIIBJghLK4A8wRa1YcZ_CILUAk=', start_index=14119)
Annotation(end_index=14916, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElRbFQiF29gUknVtp_Z-86Lel06biGgK127hfijqfE8QBONS9xF6wb9qtAljhhJOqRrm4Jbya7PYUvkgdNBA8FgVs_g66nzmzBL-cOhU4ATuKVoMYLrwQSejJfCSq_SPHfK5GjvcqZU6kW9yuJVi9UlHQQlsj1pgf3yQwRKPA4jU3VkWg5Rw0JPwH_ja-bK25pamk479XyD3W0myaXjjAhnibxo3-AiQxZk1Gqjy8pbErM2thFLE6tsjg1fhStJkQ8nrWYS89sEHWezQBy5OjVlNl5KkA=', start_index=14902)
Annotation(end_index=14916, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbddZL0CNhC4tS0bWSZze4-17sMYKezM-7Sz3HDpShQm7_qDDSgqOPABMSDqWPt-FKJPAODUwAuTvEKelGQ0ae7h-LGki8fpUZLkZJNa-18bTpGWYBSP14ZF82e3o=', start_index=14902)
Annotation(end_index=15527, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE143Llm2yxCGR1X0z8Bn6zfygbY7po8CPcdf5Dybd0eHJzdqQDnc6VXEkj-MOoaeCScLXrF-5YvIh9zLC5buiCfRJ3rsCh6dyDe0QHa9RkZoDdnHS0ICMw9FCZmeke', start_index=15514)
Annotation(end_index=15527, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEn9WyPwLN-xwcIIH4ZXYqTubEJFLzYrwAUX4m-cjYThifro0Vs6RQQVwCKhBDIQJ1w__SHxgD5koVnkXkzLGM2G7xWZnn0p0DkGXrCuXfhd6gaH4iqYuX3o9Ew-xBoPccR7WeUouXrQCKyh3cZoRqF2IlztljsLHpZSY5K2A5wxZqbE7i9KFvB3I5WqmHXY6JnJdsFkhOOTEJh5ohyOvjZdkJMjrkPjOzKBI0nw47FLqMrVRnCMb2e0X6Bgd-bUn_9sz-FcNd4aw==', start_index=15514)
Annotation(end_index=16104, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-u1npSYElmVuV-I6ux4GET1IRf95refH8J7fzrloQT5JIAV8KKOk0btj8_gc1aJuV4uEiu2xitgSMrwdktYXsMpsAyCi9W4wX_NLr4aa-wO7g0p9UkjpenXL0UuA=', start_index=16090)
Annotation(end_index=16104, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfSRZUB-pyD1VChFGx1sZY0uBRDg8TUvBXI9HpQ4Hm4rS76maZuU2Ruk29gEss3VcJkFPFvRKSbQ82V4NJt0rcG0T_RAdAE7C3O2AZJi48x23J4fA-v6SflQKXGw==', start_index=16090)
Annotation(end_index=17528, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHy3uR9ZpcEcNZgyW82ApfnIBnmtNyUnt8e9KQv-pVU65CHbPGSklEY5zTGYhyEBAhi1_iMLkYmDeubnf9iT6NrAB5kzAoLaPzGMSD_LzpqVMI8ihT5U9rvlZ6O5c4i5r7YV6o7IMFheYtBq6gGngRRSfPVuET5A==', start_index=17513)
Annotation(end_index=17528, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFARZWoUOrOOm2h9NZH0lihu7xYvLel6LqN0Od812qLV4KyQrEFMjQB28v89Ysam06RDar0k3G1qWvKRbfIsviRInH1KjN0hLsyW82zKf-3iOWA7WW2rmaIrnol3RYeIlUJ3HnwjcVSZEcAXQubwg3YOXMZw3B9F8zS-BD4akmpOlaoACA1pkFABvhSyrIExl1uEhhhdLnKO4I=', start_index=17513)
Annotation(end_index=17528, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy7z8jZFlTDR3VdV4zMSUMt2o4zLJ18fXfi0HHO-rllEPcBHf0EMqK2YYY8ILIGYSRxq--nB1fk9cgkJDeoYZpCwIeaY5gcBjq5rO2ysobkwm68MztCI2BkS3HMHc=', start_index=17513)
Annotation(end_index=17593, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIzdMdYBlatgveUzoq1kWxjz9jxh7drGTuisQNJsZ9OQx7YtSSy5kSzzLj2bSmDTwrXYBltvIu4d9HhJbxPuIn4FVGhbZ4hZ4SHI1_oDfd9uO7Uqhy0eW7YlctDvmA-rBF7I4Nz98H5tXKeEx2un5ca4hc', start_index=17575)
Annotation(end_index=17593, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGA1Mlid9tRgnzDeK7AG5QFzWgoQXPsfhCd1jo-kERV_WiIAMVK3UUCgrkk1fmJ-ewNK0aphp9jeRvYAoCF--iP2CqFDUL0zF8hZ2PzYv2pVavGBVYtcA9dl-uIxuZKtZSY', start_index=17575)
Annotation(end_index=17593, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoI2EDGvJpNb0CLWR74CoLcjR0z-jrhIn7vAwBa_0QOZYEdjWye0xIx4zLERS2L4tbD0pv4CYRaMroDQ8uG5wlS6NDZdhKMJkYqM1c5F5_PQkH1Jw8U6Yjxeg3SewpvCzlGDg0F_s=', start_index=17575)
Annotation(end_index=17647, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE143Llm2yxCGR1X0z8Bn6zfygbY7po8CPcdf5Dybd0eHJzdqQDnc6VXEkj-MOoaeCScLXrF-5YvIh9zLC5buiCfRJ3rsCh6dyDe0QHa9RkZoDdnHS0ICMw9FCZmeke', start_index=17623)
Annotation(end_index=17647, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFumrPhUL5u4Dg0i2tPGFX2VjI8whaNw_JRpVe3zSa4MDhLNPIOjxkh69lcMOxoYN368TK2pRLdKvk1hl7b2CZ23IhAYCDIgR8fjsPSnn1PZWe3fK5yHKBwKpLb2j7HYfdu2jGPMWqV', start_index=17623)
Annotation(end_index=17647, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiYkbjlfkfEWItPkjdwxRq_T9PPma8iCX0ySHxsjg7T6My0jeCf6iauaok6xMeawf5iCuU__iqiMnfPGM9wH6-N7nXIWeAL9z9OSacV8JIYkxEuPqM9F_vryE1_2JZGCDzlIGFonEmRAuPQrnbOYg12oLqXnGroOEw3CzrwwZmePe9f4cbZQSRXZ8utyEvOU1ZtA-I_UW3aBgRsYDl9wBT3YIIBJghLK4A8wRa1YcZ_CILUAk=', start_index=17623)
Annotation(end_index=17647, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKAsSMJ2w5gEyAAQDfWS2LYVg-OHZiqU87tfPia_4lMye79qvuijD67dzUSYbLNtQG9miVCU2g92qOioy8lH3jEmbsm2arjAHNs-HnYKC-VP2nohY8yg==', start_index=17623)
Annotation(end_index=17647, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_aE7dOIeWJ1yuIuW7h_O-LwWSZz1Bv2dmMNoyF3ORAzJWNw3gJ8sOFbtrjYJW6MfknoU75qVwwoah8D1zfz86c_aFRtim_FqpEvfgZBzFlFY9DwF_-5SMJrwnrGiLOE6W_jJmEnw_paQtSoS8xw==', start_index=17623)
Annotation(end_index=17692, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqrCnkClfyw75rgUPAY-_LmKtCFor2W912UJAIeqYFTESe1JDPCNyxHwox9BD-XBbSl-H9yP9kk-bS7EATPVIcgKuwQBwPEmhfw4UbWqjs61oJzzuNzSaADNAS7zqCH-wukS2ZeNyajRgcvsM9VyN90FuBF0gtO_AJVgPWy0R5SxfHv_9K0HqnzAfS_t3opW9pM3tWMR8GeaM-DZSBw874BsgR2dPB59SsaWBJgJnJqrK_oc78PWWd67VE_Lb7sepPF788lymjn05V', start_index=17680)
Annotation(end_index=17692, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd-TAfdCZtoSyVp9Q2jo2G2Je5yNfuOnWjZ_tIzJgXAKbF5aX5DyazzCh4H5yteGyHv8vqoJw0igdR8cgcD-1EcnSDtn8gnyIh-0KY0XQfHMUe091mjHiELll9AUovPQA=', start_index=17680)
Annotation(end_index=17748, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEO1VopscMgUJsC7lArwbOsbPTJjRnitLu7_es3uHVgij_8iq-F8yDt9keyPWEUNxnN-RlBHO3kqTmSlBVqKBX2Srb57UL0cGO67YgahSd836XO2vpO_R2I-g6MPLAq_lE-z_jE1-5emxng', start_index=17720)
Annotation(end_index=17748, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmT0ben8F7SNs8WUIVBb8FO0pH9IUQju1HVM3VGsmuXDu6fX5pvGA_TUERL9BTvJvYimgQQyITff5Z6WZ662EP2K7tfPy-qwK16O_46CAvJw16kwrAFcQ=', start_index=17720)
Annotation(end_index=17748, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNG28UCWjuiToZHlWQmQe6HTrnTNw_g2tAxS1ynRH6O62Jg3WM8_QNKabkhhpcWgX8j8X91vZrwNa6-x-KfaxI10Fig7RYwzsPDap3dnBPSheu23AtLw==', start_index=17720)
Annotation(end_index=17748, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyAGTY3Qd2EtpN5cerM_cIRW52GzWNJALmHul6l0oNhqA6NFxdHy8GtheCEJFLTIEDb6XWnMmvS7-M-c86CL2MPLS8fMzcQ1-hFwWb0HMOZ_XXMVU7ZCylXirUnsx3iww=', start_index=17720)
Annotation(end_index=17748, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOOrTz50RBozCGadoMSwNtVqrlYdt4pzFnagx3WxtSJNXBC5nNCg1LG9TJC4EadAR9UX964TwuHjsOpG3rfSt0WeXi7P7uN8Sr57df9PtBChVZQCFjk7mzaL303q9DTVdOnlXOMU15dtMKj28Aj5iAA7-6g5rjDX6Etfb5J0K8iAv3DQBoefk0affckmXD8CGaEAIwb3Ezse1T0LS9dpFM4puFhQ-XNRM2Z8X3cpPhUrqAYYgmyVNH9hBu5XbCTpmWYkVL4AKMe_Z7LzjSWOc6bIoCRUC9yVGnM2yy2XbpDA==', start_index=17720)
Annotation(end_index=17748, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxot0fEUVSFibdNKOP89x-S3CjshZlDSY-zjudO1xuh0VIv07Hao0rz35sBnvdyiEfMoTEPuTBF1fezN5tzDD6MSTY0_vZWjGUE5xmpmqpK5C9qS3K_Q==', start_index=17720)
Annotation(end_index=17797, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElRbFQiF29gUknVtp_Z-86Lel06biGgK127hfijqfE8QBONS9xF6wb9qtAljhhJOqRrm4Jbya7PYUvkgdNBA8FgVs_g66nzmzBL-cOhU4ATuKVoMYLrwQSejJfCSq_SPHfK5GjvcqZU6kW9yuJVi9UlHQQlsj1pgf3yQwRKPA4jU3VkWg5Rw0JPwH_ja-bK25pamk479XyD3W0myaXjjAhnibxo3-AiQxZk1Gqjy8pbErM2thFLE6tsjg1fhStJkQ8nrWYS89sEHWezQBy5OjVlNl5KkA=', start_index=17783)
Annotation(end_index=17797, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbddZL0CNhC4tS0bWSZze4-17sMYKezM-7Sz3HDpShQm7_qDDSgqOPABMSDqWPt-FKJPAODUwAuTvEKelGQ0ae7h-LGki8fpUZLkZJNa-18bTpGWYBSP14ZF82e3o=', start_index=17783)
Annotation(end_index=17847, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmIAY-l_bT6bYbo0MLzp0Fwxi4jXIGjfRZVVAuwzlGdB47MyU0r5NwixEhD0cM-bsBnAtVlItiZ_5KgPVKDW5KW2l_qGOZwW6039fibq7JMT30pBxh-J2X_hg97b1KpnjYLNCypYqULfbiyBWjtRyo-omI6PpMJ2crW6Gxp6TGx2g8ACyATdaHgLMEpIAYhKQV1-gRV9oQOgSAu9K_SethXs3NKXxANBkbcGLNw6bLgY9LzlYXBWXytvXipsnQ5NY3kyi0p1UXmljWdVGhsKvwS_E=', start_index=17833)
Annotation(end_index=17847, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXdphMTX-KDKM9QNyzwRjbi7r8R_MRE4DdBIhP7IFNdT3w_F69lyh0zEUR4LkoHbzjTvGwD_Iw8akoFtu3iP_c8I1kX5sPM6YgjmwEjn4Mhyi27tfTSPCjUKaULuo1fg==', start_index=17833)
Annotation(end_index=17899, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE143Llm2yxCGR1X0z8Bn6zfygbY7po8CPcdf5Dybd0eHJzdqQDnc6VXEkj-MOoaeCScLXrF-5YvIh9zLC5buiCfRJ3rsCh6dyDe0QHa9RkZoDdnHS0ICMw9FCZmeke', start_index=17886)
Annotation(end_index=17899, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEn9WyPwLN-xwcIIH4ZXYqTubEJFLzYrwAUX4m-cjYThifro0Vs6RQQVwCKhBDIQJ1w__SHxgD5koVnkXkzLGM2G7xWZnn0p0DkGXrCuXfhd6gaH4iqYuX3o9Ew-xBoPccR7WeUouXrQCKyh3cZoRqF2IlztljsLHpZSY5K2A5wxZqbE7i9KFvB3I5WqmHXY6JnJdsFkhOOTEJh5ohyOvjZdkJMjrkPjOzKBI0nw47FLqMrVRnCMb2e0X6Bgd-bUn_9sz-FcNd4aw==', start_index=17886)
Annotation(end_index=17948, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeHOeTtxmQNPbZ1PkNo0jjy12XUObtxtibJif45zT2JoJDkVUlyVgVhC9eapBA4awbWInTt3SNyGcZaL1nhIQuPon4CVgzH-tCoMR-1EABWDylUI_IYJsM1RByuqwsdg==', start_index=17934)
Annotation(end_index=17948, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGB2qO62_gSAX2jZzi2pKdVX-Nrnb2dYcJaah7m9CCZN2VbGnrSnC44hHpGAh4KzPDZq0Z-oiT4p1WfcCN3blxpiK_zg1bX7wTMy7VQoXmc22ou5ziav1eHgl4NX-3wVuuJmq1T5mM=', start_index=17934)

## Sources
