# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 74f47a4f | **Time:** 397.80s | **Cost:** $1.48095
--------------------------------------------------------------------------------

# Hub Node Capacity Allocation and Cascading Failure Modes in Traffic Systems

### Key Points
*   **Hub Capacity is Deterministic:** Research strongly indicates that the capacity allocation of hub nodes is a primary determinant of whether a traffic system experiences a gradual degradation (second-order phase transition) or a sudden, catastrophic collapse (first-order phase transition) under peak load.
*   **Abrupt Failure Modes:** Empirical studies, particularly on the Shanghai road network, demonstrate that traffic systems often exhibit "sudden and discontinuous" failure modes akin to physical phase transitions (e.g., ice melting). This behavior is specifically tied to the capacity thresholds of critical bottlenecks and hub nodes like urban ring roads.
*   **Non-Linear Mitigation:** Standard linear capacity allocation models often fail to prevent these abrupt collapses. Advanced non-linear allocation strategies, which disproportionately reinforce high-load hubs based on centrality measures, have been shown to shift the failure dynamics toward more manageable, gradual declines.
*   **Interdependency Risks:** The coupling of different traffic modes (e.g., metro and bus systems) introduces "interdependency failures," which significantly increase the likelihood of abrupt, first-order transitions compared to isolated networks.

### Executive Summary
The resilience of modern urban traffic systems is increasingly defined not by their ability to avoid congestion entirely, but by their response to critical stress events—specifically, whether they degrade gracefully or collapse catastrophically. This report examines the hypothesis that hub node capacity allocation under peak load conditions is the governing factor in determining the "mode" of cascading failure.

Drawing on complex network theory, percolation physics, and empirical traffic data, the evidence suggests a definitive link. When hub nodes—intersections or arterials with high betweenness centrality—possess capacity that is linearly coupled to their average load, they remain vulnerable to peak surges. Once these nodes fail, they redistribute massive traffic volumes to adjacent, lower-capacity nodes, triggering a rapid, domino-like collapse characterized as a first-order phase transition. Conversely, non-linear capacity allocation strategies that create "capacity moats" around hubs can suppress this propagation, potentially converting the failure mode into a continuous, second-order transition that allows for intervention.

This report details the theoretical underpinnings of these failure modes, analyzes specific case studies such as the recursive traffic percolation in Shanghai, and evaluates the efficacy of various capacity allocation models in mitigating systemic risk.

---

## 1. Introduction

The phenomenon of cascading failure represents one of the most significant threats to critical infrastructure systems, including power grids, the internet, and, crucially, urban transportation networks. A cascading failure occurs when the impairment of a single component or a small set of components triggers a sequence of secondary failures, propagating through the system and potentially leading to a total collapse of functionality. In traffic systems, this manifests as the rapid spread of congestion from a single bottleneck to a city-wide gridlock.

The dynamics of these failures are not uniform. Some systems exhibit a "gradual" failure mode, where functionality decreases proportionally to the damage incurred. Others suffer "abrupt" failures, maintaining apparent stability until a critical threshold is breached, after which the system collapses suddenly. Understanding the determinants of these failure modes is essential for urban planning and disaster management.

Recent research has isolated **hub node capacity allocation** as a critical variable in this equation. Hub nodes—intersections or road segments that handle a disproportionately large share of traffic flow—act as the structural keystones of the network. Under peak load conditions, the margin between a hub's load and its maximum capacity (its tolerance) becomes the defining boundary between stability and collapse. This report explores the physics of these transitions, the mathematical models used to describe them, and the empirical evidence linking capacity strategies to failure topology.

## 2. Theoretical Frameworks of Cascading Failure

To understand how capacity allocation influences failure modes, one must first establish the theoretical frameworks used to model traffic dynamics on complex networks. These frameworks borrow heavily from statistical physics, particularly percolation theory and phase transition dynamics.

### 2.1 The Motter-Lai (ML) Model
The foundational model for studying cascading failures in complex networks is the Motter-Lai (ML) model. In this framework, the load $L_j$ of a node $j$ is typically defined by its **betweenness centrality**—the number of shortest paths between all pairs of nodes that pass through $j$. The capacity $C_j$ of the node is then defined as proportional to its initial load $L_j(0)$:

\[ C_j = (1 + \alpha) L_j(0) \]

Here, $\alpha \geq 0$ is the **tolerance parameter**. This parameter represents the "safety margin" or excess capacity built into the node.
*   **Mechanism:** When a node fails (due to attack or random error), it is removed from the network.
*   **Redistribution:** The shortest paths are recalculated, and the load $L_j$ is redistributed to remaining nodes.
*   **Cascade:** If the new load $L_j(t)$ on a neighbor exceeds its capacity $C_j$, that node also fails, triggering further redistribution.

Research indicates that in the ML model, the value of $\alpha$ is critical. There exists a phase transition at a critical tolerance $\alpha_c$. Below this threshold, the failure of a single hub can cause the disintegration of the entire network [cite: 1, 2].

### 2.2 Percolation Theory and Phase Transitions
Percolation theory describes the behavior of connected clusters in a graph as nodes or edges are removed.
*   **Second-Order Transition (Continuous):** In classical random networks (like Erdős-Rényi graphs), as nodes are removed, the size of the giant connected component (GCC) decreases gradually. At the critical threshold $p_c$, the GCC disintegrates into small, disconnected clusters. This is a continuous phase transition, characterized by a power-law distribution of cluster sizes.
*   **First-Order Transition (Discontinuous):** In interdependent networks or systems with specific capacity constraints, the transition can be abrupt. The size of the GCC drops suddenly from a finite value to near zero. This is analogous to a "flash crash" in markets or the sudden freezing of water.

The distinction is vital for traffic systems. A second-order failure allows time for traffic management systems to adapt (e.g., rerouting). A first-order failure happens too fast for standard reactive measures, leading to immediate gridlock [cite: 3, 4, 5].

### 2.3 Recursive Traffic Percolation (RTP)
A specific advancement for traffic systems is the Recursive Traffic Percolation (RTP) model. Unlike static percolation, RTP incorporates the dynamic feedback loop of traffic velocity.
*   **Velocity-Load Relation:** As traffic load increases, velocity decreases.
*   **Failure Condition:** When velocity on a road segment drops below a critical threshold (representing a standstill), that segment is considered "failed" or effectively removed from the functional network.
*   **Recursion:** The removal of the road forces traffic onto alternative routes, increasing their load and decreasing their velocity, potentially causing them to fail.

This model has been instrumental in identifying that real-world traffic failures often follow the abrupt, first-order pattern [cite: 3, 6].

## 3. The Role of Hub Nodes in Failure Propagation

Hub nodes in traffic networks are typically major intersections, bridges, tunnels, or ring roads (e.g., Zhonghuan Road in Shanghai). Their role in cascading failure is paradoxical: they provide efficiency under normal conditions but act as amplifiers of failure under stress.

### 3.1 The "Rich-Club" Vulnerability
Traffic networks often exhibit a "rich-club" phenomenon where high-degree nodes (hubs) are interconnected. While this facilitates rapid transit across the network, it also creates a super-connected core of vulnerability.
*   **Load Concentration:** Hubs naturally attract the highest betweenness centrality. In the ML model, this means they carry the highest initial loads.
*   **Failure Impact:** When a hub fails, the volume of traffic it sheds is massive. Because hubs are often connected to other hubs, this shed load is transferred to other critical nodes, which are likely already operating near peak capacity.
*   **Cascading Mechanism:** This transfer triggers the simultaneous overload of multiple high-capacity nodes, leading to the "sudden" collapse characteristic of first-order transitions. Research confirms that the selective overload of hub nodes flattens hierarchical control, producing maladaptive behavior and discrete transitions from order to disorder [cite: 7].

### 3.2 Peak Load vs. Average Load
The query specifically highlights "peak load." Capacity allocation is often planned based on average or 85th-percentile loads. However, cascading failures are dynamic events triggered by extremes.
*   **The Gap:** Under peak load, the residual capacity ($C_j - L_j$) of hub nodes is at its minimum.
*   **Sensitivity:** Empirical studies show that the robustness of the network is highly sensitive to the capacity allocation of hubs during these peak windows. If the allocation strategy does not account for the non-linear increase in congestion effects (where a 5% increase in volume can cause a 50% drop in speed), the hub becomes a detonator for systemic collapse [cite: 8, 9].

## 4. Capacity Allocation Strategies: Determinants of Failure Mode

The core of the user's query lies here: Does the *way* we allocate capacity determine *how* the system fails? The literature suggests a definitive "yes."

### 4.1 Linear Capacity Allocation (The Standard Approach)
The standard approach (ML model) allocates capacity linearly proportional to load ($C \propto L$).
*   **Outcome:** This strategy tends to produce a uniform tolerance across the network.
*   **Failure Mode:** While efficient in terms of cost, it leaves hubs with the same *relative* safety margin as minor roads. However, because the *absolute* amount of traffic redirected from a failed hub is enormous, the relative margin is insufficient to absorb the shock. This often leads to **first-order (abrupt) transitions** because the neighbors of the hub are instantly overwhelmed [cite: 2, 10].

### 4.2 Non-Linear Capacity Allocation
Researchers have proposed non-linear allocation strategies to mitigate this.
\[ C_j = L_j + \alpha L_j^\delta \]
Here, $\delta$ is a tuning parameter.
*   **Strategy:** If $\delta > 1$, high-load nodes (hubs) are allocated disproportionately more spare capacity than low-load nodes.
*   **Outcome:** This creates a "capacity moat" around hubs. Even if a neighbor fails, the hub has enough excess capacity to absorb the redistributed flow without failing itself.
*   **Shift in Failure Mode:** Studies show that by tuning $\delta$ (specifically setting $\delta \neq 1$), the network's robustness can be significantly enhanced. More importantly, this can shift the failure dynamics. By protecting the hubs, the cascade is forced to propagate through lower-centrality nodes, which shed less load. This slows the cascade down, effectively converting an abrupt **first-order collapse** into a more gradual **second-order degradation** [cite: 1, 10, 11].

### 4.3 Heterogeneity and Community-Based Allocation
Recent advancements suggest allocating capacity based on community structure or node heterogeneity.
*   **Community Structure:** Traffic networks have modular structures (communities). Allocating higher capacity to the "bridge" nodes that connect these communities prevents the failure from spreading between modules.
*   **Findings:** Strategies that prioritize these structural bridges reduce the scale of cascading failures compared to the standard ML model. This suggests that "smart" allocation can contain failures within local clusters, preventing global, sudden collapse [cite: 12, 13].

## 5. Phase Transitions: The Physics of Traffic Collapse

The concept of phase transitions provides the most rigorous answer to the "failure mode" aspect of the query.

### 5.1 First-Order Transitions (The "Sudden Death")
A first-order phase transition in a traffic system is characterized by a discontinuity in the order parameter (usually the size of the functional network or the average velocity).
*   **Mechanism:** This occurs when the failure of a critical fraction of nodes leads to a feedback loop that is faster than the system's relaxation time.
*   **Trigger:** It is almost exclusively triggered by the failure of **hub nodes** in systems with **linear capacity allocation** or **high interdependency**.
*   **Evidence:** In the Shanghai study, the removal of roads based on velocity thresholds led to a sudden drop in the size of the giant component. This was explicitly compared to "ice melting" or "water boiling"—classic first-order transitions [cite: 3].

### 5.2 Second-Order Transitions (The "Gradual Decline")
A second-order transition is continuous. The system degrades smoothly.
*   **Mechanism:** This occurs when failures are localized and do not trigger massive load shedding.
*   **Conditions:** This mode is observed in networks where hubs are heavily protected (high non-linear capacity) or in homogeneous networks (random graphs) where no single node is critical.
*   **Strategic Shift:** Research indicates that increasing the coupling strength or dependency between network layers (e.g., bus and rail) can shift a system from a second-order to a first-order transition. Conversely, decoupling or reinforcing hubs can reverse this, "smoothing out" the collapse [cite: 5, 14, 15].

### 5.3 The Critical Plateau
Interestingly, some models show a "mixed-order" transition or a plateau.
*   **Observation:** In some overloaded networks, the order parameter collapses following a long critical plateau. This suggests a latent period where the system appears stable but is accumulating invisible stress (load redistribution) before the sudden crash.
*   **Implication:** This "hidden" phase is dangerous for traffic managers, as standard metrics (like average speed) might not show the impending doom until the plateau ends in a cliff-edge drop [cite: 16].

## 6. Case Study: The Shanghai Urban Road Network

The most pertinent empirical evidence comes from the 2023 study on the Shanghai road network using the Recursive Traffic Percolation (RTP) model.

### 6.1 Methodology
The researchers modeled the Shanghai network using real-world topology and population distribution. They simulated traffic flows and applied the RTP mechanism:
1.  Assign trips based on population.
2.  Calculate velocity based on load.
3.  Remove roads where velocity drops below a threshold (congestion failure).
4.  Redistribute traffic and repeat.

### 6.2 The Zhonghuan Road Bottleneck
The study identified **Zhonghuan Road** (a major ring road/hub) as a hidden bottleneck.
*   **The Event:** During the simulation, the network maintained functionality until a specific threshold. Suddenly, Zhonghuan Road failed due to overload.
*   **The Cascade:** The failure of this single arterial hub forced traffic onto side streets. These lower-capacity streets could not handle the influx, leading to their immediate failure.
*   **The Mode:** The result was a "massive cascading failure... in a sudden and discontinuous fashion." The network did not degrade; it snapped.
*   **Conclusion:** This confirms that the capacity allocation of the hub (Zhonghuan Road) was the determinant factor. Had Zhonghuan Road possessed higher capacity (or effective flow control), the cascade would have been contained or slowed [cite: 3, 6].

## 7. Comparative Analysis: Interdependent Systems

Traffic systems do not exist in isolation; they are often coupled with other networks (power, communication, other transit modes).

### 7.1 Interdependency and Failure Modes
Research on interdependent networks (e.g., power grids controlling traffic signals) shows that interdependency fundamentally alters the failure mode.
*   **Isolated Networks:** Tend to exhibit second-order (gradual) transitions.
*   **Interdependent Networks:** Tend to exhibit first-order (abrupt) transitions.
*   **Reasoning:** A failure in the power grid disables traffic signals (nodes), reducing their capacity to zero. This causes traffic chaos, which might delay repair crews, feeding back into the power failure. This feedback loop accelerates the collapse [cite: 4, 5].

### 7.2 Capacity Allocation in Coupled Layers
In multimodal networks (e.g., bus + subway), the capacity allocation *between* layers is crucial.
*   **Coupling Strength:** If the coupling is strong (e.g., high volume of transfers between bus and metro), the system is more efficient but more fragile.
*   **Findings:** Reducing the coupling strength or increasing the capacity of the "interconnect" nodes can revert the system from a first-order back to a second-order transition, restoring a measure of gradual failure [cite: 17, 18].

## 8. Mitigation Strategies

Based on the finding that capacity allocation determines failure mode, several mitigation strategies emerge.

### 8.1 Non-Linear Capacity Reinforcement
*   **Strategy:** Adopt a non-linear allocation model ($C \propto L^\alpha$ with $\alpha > 1$) for infrastructure planning.
*   **Implementation:** Physically widen hub roads, improve signal timing at major intersections, or use dynamic lane management to artificially boost capacity at hubs during peak loads.
*   **Effect:** Creates a buffer that prevents the hub from failing first, forcing the cascade to dissipate through less critical nodes [cite: 1, 10].

### 8.2 Edge Control and Flow Restriction
*   **Strategy:** Instead of increasing capacity (which is expensive), restrict the *inflow* to hubs.
*   **Mechanism:** By artificially capping the load entering a hub (ramp metering), the system prevents the hub from reaching its critical failure threshold.
*   **Effect:** This effectively mimics infinite capacity by capping demand, preventing the first-order collapse trigger [cite: 19].

### 8.3 Redundancy and Topology Modification
*   **Strategy:** Add redundant links to bypass hubs.
*   **Effect:** Reduces the betweenness centrality of the primary hub, flattening the load distribution and making the network more homogeneous. Homogeneous networks are less prone to first-order hub-driven collapses [cite: 12, 20].

## 9. Conclusion

The research provides a robust affirmative answer to the user's query. **Hub node capacity allocation under peak load is a decisive factor in determining the cascading failure mode of traffic systems.**

*   **Determinism:** The relationship between a hub's load and its capacity threshold dictates the physics of the collapse. Tight coupling leads to abrupt, first-order phase transitions (sudden death). Loose or non-linear coupling leads to gradual, second-order transitions (graceful degradation).
*   **Hub Centrality:** The "sudden" nature of traffic collapse is inextricably linked to the failure of high-centrality nodes. When these nodes fail, they release a shockwave of redistributed load that linear capacity models cannot absorb.
*   **Design Implication:** To prevent catastrophic gridlock, urban planners must move beyond linear capacity planning. Adopting non-linear capacity strategies—where hubs are "over-engineered" relative to their average load—or implementing strict flow controls to protect these hubs is essential. This does not just delay congestion; it fundamentally changes the mathematical nature of the failure from a catastrophic cliff-edge to a manageable slope.

### References
*   **[cite: 3, 6]** *Chaos*, 2023. "Cascading failures in urban traffic systems tied to hidden bottlenecks." (Shanghai/Zhonghuan Road study).
*   **[cite: 10]** *ICMLC*, 2012. "Cascading network failure based on local load distribution and non-linear relationship..."
*   **[cite: 4]** *ComNet*, 2020. "Relationship between node capacity and cascading failure in complex networks."
*   **[cite: 1]** *Complex System Modeling*, 2024. "Cascading Failures in Power Grids: A Load Capacity Model with Node Centrality."
*   **[cite: 2]** *Chaos*, 2021. "Effect of load capacity heterogeneity on cascading..."
*   **[cite: 12, 13]** *IEEE*, 2024. "Cascading failure mechanism in traffic networks capacity allocation."
*   **[cite: 7]** *PMC*, 2021. "The selective overload and cascading failure of highly connected (hub) nodes..."
*   **[cite: 16]** *ResearchGate*, 2024. "Critical behavior of cascading failures in overloaded networks."
*   **[cite: 5]** *ResearchGate*, 2017. "Cascading failures in interdependent systems under a flow redistribution model."

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErL6j9mZvyKD_hb3fW_UmGAvSKAAzj6wpkAHto8-jR7HZ0MBjMIRMNufKqcQt-LsCyqEWH1enF4-VJUnvM4JKFCuQyzaBKhvSLpLP1CMA9t1qtEQ-NGcbwrTKX10niwQ6lvBQ6M9xJC0n4wCMme1kJ958KyqubjRB3FNbZp9ONcQMK6dbmRrvuLffXcwFdhaTuYpNWFI--KAQb2g-uaJCzgk85UrjpjYpdv15NmlRqSGnQilVY)
2. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF433e6JnL2gMDE2ticvjGnACG2pZAYvAytjl-p-9q0CQHSJqf6mQbTTq646f8lMirSlUSPfKGi5POTyih9t2rsg7uq8DUohSrMGcXQoOFtmmPLbqyyTPusQJu5PP1EnT7dThhdvoWsbpr6mPTdEKjjde2vGeofY-Mrhk46bvhnfJw4DXn4_6BUd3IrPTrlsMO5scSZvXr4tYeI-xozfrIzyA==)
3. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFa3YKuJiGd9l8efdD5TSi2kpGnnbsHYts2wyRG49aEbRZn3bsDwoLHg6lBBvhircstSFgTZFohr5-pVigpUUi9WbKqe6HkDZE4pK44XQLfvp-zt858ZA9EWjF4qHIw7k8jVWAW7QVW0oOJW-mDGgUzDRWbUgGX-V8Xs1a5iy1_swYh5j2z4Xz1Q2ZcCg-gH9KHv5uE11NL5z3m8gM7SKUajHTIBR5NxCukpbPUTjUTKoqTxXg=)
4. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFck_sfPgObWByqHLI5L9yEdDWOF4YQkq5vxpLKx-_UkHhXy9chfpjyRohGDXxhVaaAFLOsz1Wnk7Hg9snqr28SMLC81imL2QtJ50imBkeAlDjtjgBpxPtlsqZ121twvKaGkFYPmvgVwoP7nqsekmKcrQ==)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPUfxCoFIr_mFwbFm_V6SbZ0298RXLLdwMydIFWIYsUwJFIjfDEVtb8oejFuARK-KGwF1z49FyLRMGYqPOUrZZDOXrMAOclpit1O8tKQE_SFzrXwSBqXK7xfHC5Hd8OFpftP9oNR5MzjiDs_Ee3Tjvr1a5nPzw5YUlLsNtzKEA4SAp2DAAfYyfIh6uMLRQc7fO8huiseFIWmEC3T4lHEechDUdL2AY-20lGyUr-gW89q_1LuDbesN2)
6. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP5WdkqpQJ4dPkV3e_KluCKkiK9S6bDYO1b4-Ezc1MVrlwWkc7VH_5_NPebqn5Yq-z0w1VIQrd___SKEzZHTVK4OfiVkoynggYekfSUyuOaBs2k2p5Tigv83rUrOUiwyvngPr7EoNxrk5fC1OVbdPNOCkWJJczzJ4YolR_rbU5cTADS_HutSYiiwcn1qtnm6PVclpwiA==)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELWzd0kVFnrU8mcr0AJSYqztghOm3Pvr4rU0S-4sA9rHr8zRTU_8VX1v2fj9bCigqtJXdIEGjG3TnAcK6MUKLD5u6-5oeZEYjJ7Bhj5SgHiK0AVq4H6A3qpaRffiBdWawGttex_QpW)
8. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEluv4yaQLj7JwTeWvX8mCBVdPvLb_qPnpIkGQKnqW0tQUs-4lxLw93-zlq6C7EsvYE8OwK70ODcGVwjNB7Uqfdf13Dfw-mpjoiOIiKDFPNqnrC7EkUf_X4RnQ-ER3RFu1i)
9. [dev.to](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgpe80IdNxV7bi4RYEGyAR9IpMWFYAdsZSP8qChs-pRsLhJmDKwJZNHoaunYW-f-Ufm33xQ4nlhF98YS77vohwwR4PIg6iLovfQdFD6OYHyjWi8Yh-KRBHF5kLTbSG5K2jLq2vCQ3edAXpjs4uHQM=)
10. [sci-hub.box](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPMH7beMZOZ1D6yoFEtsnQ-1y_9uXytuyVV7NVGn19E87rP2qaq0Au2tw5DfOxOLVPvSHLMnySCR-SdQszCEX1YJEQzdtlgcfRWNikZ1K1UK4BxXhrVtn1EJ_ZCZT5_GqcoY52)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoaglQknMl3EEhy9xlcin4NpAMoahfGkjSn0brunSgilAQbp6uU8UazU22q7AR1SHJd_b-NmEdVluTZqYHpOS_S0rq1Q2wPF0tCQTdcqFEG3ltn1K0pcJ38SdGVkEFSwKOtuBOFXtA37ulR--kSOG5sxjCC13KX6zjZwiOxsAcISf8xSQiGcdr3ZXHoHeiOsObKAfgG6w6WlWCglCnmxHyfnxUmkp8mIZviWo5Gy5_mpiQv-Z99GaN2ycyawpE3kK2Ywsm2ufE19DkRNo78TsqqJJ-8mc4Hsc1lv42RvAenYFnhZk=)
12. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEpvUZAwXeNKjnddx6RBo4VogbS4ygf8wOpggH0LJjNLEVYM8fBUFxPkbgyHToNx94xZvjJ1_bdxBhOP5jMMFA0fBIIqMvKiMHzBTtPSXZ8Scn0x-c36cocbFyF33Dp-Idnlkm6NRRiaqHz7egrpcfE-0tsg==)
13. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9Evna0wGMy1mWXD3m_NiA8MRc472HtStaNi9T3bTT7v7U70K6PjTUkcDqXPzojKTCZ2iwRctpt-uAsuzwIxx9zBAWXHuse0JaTW51M-mUzvd675x5fTTy8VZ7ZbR94u3XjuuR)
14. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE713U62ahyfaHSUVd6wsYJPbBx16DRJdlYBAVUwMAsPK256UJiCn-m63McwNkxKcOphEbiqGwgxaWyN9QP54SCl9RbVQk5yQEcYiLms_1dRVmMXLA5VQ==)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQ7doJWOsK8lzs9drSc3HeuaL_8OmsG0_jRQD5xqjSd-NLagNI7tNzYFnZ6lzG_pkzUD8ZsduV6mJrjssQD9bppCNHT5816WR1NMDFOqcLah5PaQysDHyrYxeYjdkV6EXsyIiuSErDgXvJAG8HJusorvTCEFqM9Z00Iqq3QcQYm8rN6pKcUcOxpcJqxGtUh3mMgnMdPoOapgUUr7d5GpPZxW9yIh7ijii8Lr4HPvsibAF_qZrXGhl4KxBJrP45cgTq)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlr2XKumCe31Iiu-N77GD_TBO_t5q1GZc9zzSA5n6WDUcDXkPhwRtmgJNZvAjCVwsLqT8SFkP_RDvTDtHjqOrd3z_hiJOflyjRj1efR-BZkU91MTwSYEt_Phn8xJW5ADwjfd6yzGJfveh8uCdEIpUUdn4xoKiIfW0OM06aYKClswVud1fPMR9EZKrFWAwyRcPZSWVDpErnEvpINIk4LO3OsLUAtZ6Cnw==)
17. [worldscientific.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgEipFm-z33IgOxF1buORVolgnI9TuEad28v0oxLXdTRkXWWlHzwGC5F8K889jt_SUfgpGZx-LTeeoB0oaZM59LoOGI0hZh-b1gmlSyQuHRLgel-rHnuKplBPTw9wFfwMOy6nvaxSaWj3sGp9zF9c2gtBFcNQgVyY=)
18. [worldscientific.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5Y3H609IWgjKrsARtAeLjNyW1BIi3Hx1dDcTiNqYpC80s8OmyMmkctlVIaOqel6pSaOfgm1OeV4OIdgqQtKda5WZ6gg9GNXSVoYmlPWwE_xnDySsXjgAc5Bj-UxvHpgGRj-mAeBeCT7WksmWoKysPaec2vNhxCO0=)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLy_AS1jpNLaGSNyeAYlAj9C2HvT0olvqWysOKAlNt8NguDa_jYHP1agqJpCFgxiIx8-CBdojANu9Rip7xlwyaNexmwU9FPWryEil95POtrrJLEOFrEsNDVb8booX6UXUscvtNvjA4ZjyOjmte-se5Ygyy7VBBH166sG6pSLREugc5ydHUgCgFNOTRLAqE1PX8j3ERVYs_Hl6WWomXXzceKs5r2GLCdaokXwrI5CY=)
20. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJE7WsxmDyUCcZAvqZg9HDcpjk3XkMl_ZSDvdC3oNAanm3HhZMPq7KLF7-mvCAaBLcYCFSbLkm3_G5-OuG7yzZVv5c4ke3VlOHFvu2xdqRh3Z0f0r6HKotfLMhOuEDhKCzO_cWfLrh)


## Annotations
Annotation(end_index=5932, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErL6j9mZvyKD_hb3fW_UmGAvSKAAzj6wpkAHto8-jR7HZ0MBjMIRMNufKqcQt-LsCyqEWH1enF4-VJUnvM4JKFCuQyzaBKhvSLpLP1CMA9t1qtEQ-NGcbwrTKX10niwQ6lvBQ6M9xJC0n4wCMme1kJ958KyqubjRB3FNbZp9ONcQMK6dbmRrvuLffXcwFdhaTuYpNWFI--KAQb2g-uaJCzgk85UrjpjYpdv15NmlRqSGnQilVY', start_index=5920)
Annotation(end_index=5932, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF433e6JnL2gMDE2ticvjGnACG2pZAYvAytjl-p-9q0CQHSJqf6mQbTTq646f8lMirSlUSPfKGi5POTyih9t2rsg7uq8DUohSrMGcXQoOFtmmPLbqyyTPusQJu5PP1EnT7dThhdvoWsbpr6mPTdEKjjde2vGeofY-Mrhk46bvhnfJw4DXn4_6BUd3IrPTrlsMO5scSZvXr4tYeI-xozfrIzyA==', start_index=5920)
Annotation(end_index=7033, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPUfxCoFIr_mFwbFm_V6SbZ0298RXLLdwMydIFWIYsUwJFIjfDEVtb8oejFuARK-KGwF1z49FyLRMGYqPOUrZZDOXrMAOclpit1O8tKQE_SFzrXwSBqXK7xfHC5Hd8OFpftP9oNR5MzjiDs_Ee3Tjvr1a5nPzw5YUlLsNtzKEA4SAp2DAAfYyfIh6uMLRQc7fO8huiseFIWmEC3T4lHEechDUdL2AY-20lGyUr-gW89q_1LuDbesN2', start_index=7018)
Annotation(end_index=7033, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFa3YKuJiGd9l8efdD5TSi2kpGnnbsHYts2wyRG49aEbRZn3bsDwoLHg6lBBvhircstSFgTZFohr5-pVigpUUi9WbKqe6HkDZE4pK44XQLfvp-zt858ZA9EWjF4qHIw7k8jVWAW7QVW0oOJW-mDGgUzDRWbUgGX-V8Xs1a5iy1_swYh5j2z4Xz1Q2ZcCg-gH9KHv5uE11NL5z3m8gM7SKUajHTIBR5NxCukpbPUTjUTKoqTxXg=', start_index=7018)
Annotation(end_index=7033, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFck_sfPgObWByqHLI5L9yEdDWOF4YQkq5vxpLKx-_UkHhXy9chfpjyRohGDXxhVaaAFLOsz1Wnk7Hg9snqr28SMLC81imL2QtJ50imBkeAlDjtjgBpxPtlsqZ121twvKaGkFYPmvgVwoP7nqsekmKcrQ==', start_index=7018)
Annotation(end_index=7861, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFa3YKuJiGd9l8efdD5TSi2kpGnnbsHYts2wyRG49aEbRZn3bsDwoLHg6lBBvhircstSFgTZFohr5-pVigpUUi9WbKqe6HkDZE4pK44XQLfvp-zt858ZA9EWjF4qHIw7k8jVWAW7QVW0oOJW-mDGgUzDRWbUgGX-V8Xs1a5iy1_swYh5j2z4Xz1Q2ZcCg-gH9KHv5uE11NL5z3m8gM7SKUajHTIBR5NxCukpbPUTjUTKoqTxXg=', start_index=7849)
Annotation(end_index=7861, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP5WdkqpQJ4dPkV3e_KluCKkiK9S6bDYO1b4-Ezc1MVrlwWkc7VH_5_NPebqn5Yq-z0w1VIQrd___SKEzZHTVK4OfiVkoynggYekfSUyuOaBs2k2p5Tigv83rUrOUiwyvngPr7EoNxrk5fC1OVbdPNOCkWJJczzJ4YolR_rbU5cTADS_HutSYiiwcn1qtnm6PVclpwiA==', start_index=7849)
Annotation(end_index=9213, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELWzd0kVFnrU8mcr0AJSYqztghOm3Pvr4rU0S-4sA9rHr8zRTU_8VX1v2fj9bCigqtJXdIEGjG3TnAcK6MUKLD5u6-5oeZEYjJ7Bhj5SgHiK0AVq4H6A3qpaRffiBdWawGttex_QpW', start_index=9204)
Annotation(end_index=9930, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgpe80IdNxV7bi4RYEGyAR9IpMWFYAdsZSP8qChs-pRsLhJmDKwJZNHoaunYW-f-Ufm33xQ4nlhF98YS77vohwwR4PIg6iLovfQdFD6OYHyjWi8Yh-KRBHF5kLTbSG5K2jLq2vCQ3edAXpjs4uHQM=', start_index=9918)
Annotation(end_index=9930, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEluv4yaQLj7JwTeWvX8mCBVdPvLb_qPnpIkGQKnqW0tQUs-4lxLw93-zlq6C7EsvYE8OwK70ODcGVwjNB7Uqfdf13Dfw-mpjoiOIiKDFPNqnrC7EkUf_X4RnQ-ER3RFu1i', start_index=9918)
Annotation(end_index=10806, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF433e6JnL2gMDE2ticvjGnACG2pZAYvAytjl-p-9q0CQHSJqf6mQbTTq646f8lMirSlUSPfKGi5POTyih9t2rsg7uq8DUohSrMGcXQoOFtmmPLbqyyTPusQJu5PP1EnT7dThhdvoWsbpr6mPTdEKjjde2vGeofY-Mrhk46bvhnfJw4DXn4_6BUd3IrPTrlsMO5scSZvXr4tYeI-xozfrIzyA==', start_index=10793)
Annotation(end_index=10806, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPMH7beMZOZ1D6yoFEtsnQ-1y_9uXytuyVV7NVGn19E87rP2qaq0Au2tw5DfOxOLVPvSHLMnySCR-SdQszCEX1YJEQzdtlgcfRWNikZ1K1UK4BxXhrVtn1EJ_ZCZT5_GqcoY52', start_index=10793)
Annotation(end_index=11795, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErL6j9mZvyKD_hb3fW_UmGAvSKAAzj6wpkAHto8-jR7HZ0MBjMIRMNufKqcQt-LsCyqEWH1enF4-VJUnvM4JKFCuQyzaBKhvSLpLP1CMA9t1qtEQ-NGcbwrTKX10niwQ6lvBQ6M9xJC0n4wCMme1kJ958KyqubjRB3FNbZp9ONcQMK6dbmRrvuLffXcwFdhaTuYpNWFI--KAQb2g-uaJCzgk85UrjpjYpdv15NmlRqSGnQilVY', start_index=11778)
Annotation(end_index=11795, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPMH7beMZOZ1D6yoFEtsnQ-1y_9uXytuyVV7NVGn19E87rP2qaq0Au2tw5DfOxOLVPvSHLMnySCR-SdQszCEX1YJEQzdtlgcfRWNikZ1K1UK4BxXhrVtn1EJ_ZCZT5_GqcoY52', start_index=11778)
Annotation(end_index=11795, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoaglQknMl3EEhy9xlcin4NpAMoahfGkjSn0brunSgilAQbp6uU8UazU22q7AR1SHJd_b-NmEdVluTZqYHpOS_S0rq1Q2wPF0tCQTdcqFEG3ltn1K0pcJ38SdGVkEFSwKOtuBOFXtA37ulR--kSOG5sxjCC13KX6zjZwiOxsAcISf8xSQiGcdr3ZXHoHeiOsObKAfgG6w6WlWCglCnmxHyfnxUmkp8mIZviWo5Gy5_mpiQv-Z99GaN2ycyawpE3kK2Ywsm2ufE19DkRNo78TsqqJJ-8mc4Hsc1lv42RvAenYFnhZk=', start_index=11778)
Annotation(end_index=12444, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9Evna0wGMy1mWXD3m_NiA8MRc472HtStaNi9T3bTT7v7U70K6PjTUkcDqXPzojKTCZ2iwRctpt-uAsuzwIxx9zBAWXHuse0JaTW51M-mUzvd675x5fTTy8VZ7ZbR94u3XjuuR', start_index=12430)
Annotation(end_index=12444, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEpvUZAwXeNKjnddx6RBo4VogbS4ygf8wOpggH0LJjNLEVYM8fBUFxPkbgyHToNx94xZvjJ1_bdxBhOP5jMMFA0fBIIqMvKiMHzBTtPSXZ8Scn0x-c36cocbFyF33Dp-Idnlkm6NRRiaqHz7egrpcfE-0tsg==', start_index=12430)
Annotation(end_index=13420, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFa3YKuJiGd9l8efdD5TSi2kpGnnbsHYts2wyRG49aEbRZn3bsDwoLHg6lBBvhircstSFgTZFohr5-pVigpUUi9WbKqe6HkDZE4pK44XQLfvp-zt858ZA9EWjF4qHIw7k8jVWAW7QVW0oOJW-mDGgUzDRWbUgGX-V8Xs1a5iy1_swYh5j2z4Xz1Q2ZcCg-gH9KHv5uE11NL5z3m8gM7SKUajHTIBR5NxCukpbPUTjUTKoqTxXg=', start_index=13411)
Annotation(end_index=14158, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE713U62ahyfaHSUVd6wsYJPbBx16DRJdlYBAVUwMAsPK256UJiCn-m63McwNkxKcOphEbiqGwgxaWyN9QP54SCl9RbVQk5yQEcYiLms_1dRVmMXLA5VQ==', start_index=14141)
Annotation(end_index=14158, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPUfxCoFIr_mFwbFm_V6SbZ0298RXLLdwMydIFWIYsUwJFIjfDEVtb8oejFuARK-KGwF1z49FyLRMGYqPOUrZZDOXrMAOclpit1O8tKQE_SFzrXwSBqXK7xfHC5Hd8OFpftP9oNR5MzjiDs_Ee3Tjvr1a5nPzw5YUlLsNtzKEA4SAp2DAAfYyfIh6uMLRQc7fO8huiseFIWmEC3T4lHEechDUdL2AY-20lGyUr-gW89q_1LuDbesN2', start_index=14141)
Annotation(end_index=14158, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQ7doJWOsK8lzs9drSc3HeuaL_8OmsG0_jRQD5xqjSd-NLagNI7tNzYFnZ6lzG_pkzUD8ZsduV6mJrjssQD9bppCNHT5816WR1NMDFOqcLah5PaQysDHyrYxeYjdkV6EXsyIiuSErDgXvJAG8HJusorvTCEFqM9Z00Iqq3QcQYm8rN6pKcUcOxpcJqxGtUh3mMgnMdPoOapgUUr7d5GpPZxW9yIh7ijii8Lr4HPvsibAF_qZrXGhl4KxBJrP45cgTq', start_index=14141)
Annotation(end_index=14729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlr2XKumCe31Iiu-N77GD_TBO_t5q1GZc9zzSA5n6WDUcDXkPhwRtmgJNZvAjCVwsLqT8SFkP_RDvTDtHjqOrd3z_hiJOflyjRj1efR-BZkU91MTwSYEt_Phn8xJW5ADwjfd6yzGJfveh8uCdEIpUUdn4xoKiIfW0OM06aYKClswVud1fPMR9EZKrFWAwyRcPZSWVDpErnEvpINIk4LO3OsLUAtZ6Cnw==', start_index=14719)
Annotation(end_index=16172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFa3YKuJiGd9l8efdD5TSi2kpGnnbsHYts2wyRG49aEbRZn3bsDwoLHg6lBBvhircstSFgTZFohr5-pVigpUUi9WbKqe6HkDZE4pK44XQLfvp-zt858ZA9EWjF4qHIw7k8jVWAW7QVW0oOJW-mDGgUzDRWbUgGX-V8Xs1a5iy1_swYh5j2z4Xz1Q2ZcCg-gH9KHv5uE11NL5z3m8gM7SKUajHTIBR5NxCukpbPUTjUTKoqTxXg=', start_index=16160)
Annotation(end_index=16172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP5WdkqpQJ4dPkV3e_KluCKkiK9S6bDYO1b4-Ezc1MVrlwWkc7VH_5_NPebqn5Yq-z0w1VIQrd___SKEzZHTVK4OfiVkoynggYekfSUyuOaBs2k2p5Tigv83rUrOUiwyvngPr7EoNxrk5fC1OVbdPNOCkWJJczzJ4YolR_rbU5cTADS_HutSYiiwcn1qtnm6PVclpwiA==', start_index=16160)
Annotation(end_index=16979, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPUfxCoFIr_mFwbFm_V6SbZ0298RXLLdwMydIFWIYsUwJFIjfDEVtb8oejFuARK-KGwF1z49FyLRMGYqPOUrZZDOXrMAOclpit1O8tKQE_SFzrXwSBqXK7xfHC5Hd8OFpftP9oNR5MzjiDs_Ee3Tjvr1a5nPzw5YUlLsNtzKEA4SAp2DAAfYyfIh6uMLRQc7fO8huiseFIWmEC3T4lHEechDUdL2AY-20lGyUr-gW89q_1LuDbesN2', start_index=16967)
Annotation(end_index=16979, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFck_sfPgObWByqHLI5L9yEdDWOF4YQkq5vxpLKx-_UkHhXy9chfpjyRohGDXxhVaaAFLOsz1Wnk7Hg9snqr28SMLC81imL2QtJ50imBkeAlDjtjgBpxPtlsqZ121twvKaGkFYPmvgVwoP7nqsekmKcrQ==', start_index=16967)
Annotation(end_index=17515, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5Y3H609IWgjKrsARtAeLjNyW1BIi3Hx1dDcTiNqYpC80s8OmyMmkctlVIaOqel6pSaOfgm1OeV4OIdgqQtKda5WZ6gg9GNXSVoYmlPWwE_xnDySsXjgAc5Bj-UxvHpgGRj-mAeBeCT7WksmWoKysPaec2vNhxCO0=', start_index=17501)
Annotation(end_index=17515, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgEipFm-z33IgOxF1buORVolgnI9TuEad28v0oxLXdTRkXWWlHzwGC5F8K889jt_SUfgpGZx-LTeeoB0oaZM59LoOGI0hZh-b1gmlSyQuHRLgel-rHnuKplBPTw9wFfwMOy6nvaxSaWj3sGp9zF9c2gtBFcNQgVyY=', start_index=17501)
Annotation(end_index=18159, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErL6j9mZvyKD_hb3fW_UmGAvSKAAzj6wpkAHto8-jR7HZ0MBjMIRMNufKqcQt-LsCyqEWH1enF4-VJUnvM4JKFCuQyzaBKhvSLpLP1CMA9t1qtEQ-NGcbwrTKX10niwQ6lvBQ6M9xJC0n4wCMme1kJ958KyqubjRB3FNbZp9ONcQMK6dbmRrvuLffXcwFdhaTuYpNWFI--KAQb2g-uaJCzgk85UrjpjYpdv15NmlRqSGnQilVY', start_index=18146)
Annotation(end_index=18159, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPMH7beMZOZ1D6yoFEtsnQ-1y_9uXytuyVV7NVGn19E87rP2qaq0Au2tw5DfOxOLVPvSHLMnySCR-SdQszCEX1YJEQzdtlgcfRWNikZ1K1UK4BxXhrVtn1EJ_ZCZT5_GqcoY52', start_index=18146)
Annotation(end_index=18595, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLy_AS1jpNLaGSNyeAYlAj9C2HvT0olvqWysOKAlNt8NguDa_jYHP1agqJpCFgxiIx8-CBdojANu9Rip7xlwyaNexmwU9FPWryEil95POtrrJLEOFrEsNDVb8booX6UXUscvtNvjA4ZjyOjmte-se5Ygyy7VBBH166sG6pSLREugc5ydHUgCgFNOTRLAqE1PX8j3ERVYs_Hl6WWomXXzceKs5r2GLCdaokXwrI5CY=', start_index=18585)
Annotation(end_index=18928, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJE7WsxmDyUCcZAvqZg9HDcpjk3XkMl_ZSDvdC3oNAanm3HhZMPq7KLF7-mvCAaBLcYCFSbLkm3_G5-OuG7yzZVv5c4ke3VlOHFvu2xdqRh3Z0f0r6HKotfLMhOuEDhKCzO_cWfLrh', start_index=18914)
Annotation(end_index=18928, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEpvUZAwXeNKjnddx6RBo4VogbS4ygf8wOpggH0LJjNLEVYM8fBUFxPkbgyHToNx94xZvjJ1_bdxBhOP5jMMFA0fBIIqMvKiMHzBTtPSXZ8Scn0x-c36cocbFyF33Dp-Idnlkm6NRRiaqHz7egrpcfE-0tsg==', start_index=18914)
Annotation(end_index=20182, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFa3YKuJiGd9l8efdD5TSi2kpGnnbsHYts2wyRG49aEbRZn3bsDwoLHg6lBBvhircstSFgTZFohr5-pVigpUUi9WbKqe6HkDZE4pK44XQLfvp-zt858ZA9EWjF4qHIw7k8jVWAW7QVW0oOJW-mDGgUzDRWbUgGX-V8Xs1a5iy1_swYh5j2z4Xz1Q2ZcCg-gH9KHv5uE11NL5z3m8gM7SKUajHTIBR5NxCukpbPUTjUTKoqTxXg=', start_index=20170)
Annotation(end_index=20182, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP5WdkqpQJ4dPkV3e_KluCKkiK9S6bDYO1b4-Ezc1MVrlwWkc7VH_5_NPebqn5Yq-z0w1VIQrd___SKEzZHTVK4OfiVkoynggYekfSUyuOaBs2k2p5Tigv83rUrOUiwyvngPr7EoNxrk5fC1OVbdPNOCkWJJczzJ4YolR_rbU5cTADS_HutSYiiwcn1qtnm6PVclpwiA==', start_index=20170)
Annotation(end_index=20323, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPMH7beMZOZ1D6yoFEtsnQ-1y_9uXytuyVV7NVGn19E87rP2qaq0Au2tw5DfOxOLVPvSHLMnySCR-SdQszCEX1YJEQzdtlgcfRWNikZ1K1UK4BxXhrVtn1EJ_ZCZT5_GqcoY52', start_index=20313)
Annotation(end_index=20448, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFck_sfPgObWByqHLI5L9yEdDWOF4YQkq5vxpLKx-_UkHhXy9chfpjyRohGDXxhVaaAFLOsz1Wnk7Hg9snqr28SMLC81imL2QtJ50imBkeAlDjtjgBpxPtlsqZ121twvKaGkFYPmvgVwoP7nqsekmKcrQ==', start_index=20439)
Annotation(end_index=20562, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErL6j9mZvyKD_hb3fW_UmGAvSKAAzj6wpkAHto8-jR7HZ0MBjMIRMNufKqcQt-LsCyqEWH1enF4-VJUnvM4JKFCuQyzaBKhvSLpLP1CMA9t1qtEQ-NGcbwrTKX10niwQ6lvBQ6M9xJC0n4wCMme1kJ958KyqubjRB3FNbZp9ONcQMK6dbmRrvuLffXcwFdhaTuYpNWFI--KAQb2g-uaJCzgk85UrjpjYpdv15NmlRqSGnQilVY', start_index=20553)
Annotation(end_index=20694, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF433e6JnL2gMDE2ticvjGnACG2pZAYvAytjl-p-9q0CQHSJqf6mQbTTq646f8lMirSlUSPfKGi5POTyih9t2rsg7uq8DUohSrMGcXQoOFtmmPLbqyyTPusQJu5PP1EnT7dThhdvoWsbpr6mPTdEKjjde2vGeofY-Mrhk46bvhnfJw4DXn4_6BUd3IrPTrlsMO5scSZvXr4tYeI-xozfrIzyA==', start_index=20685)
Annotation(end_index=20788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9Evna0wGMy1mWXD3m_NiA8MRc472HtStaNi9T3bTT7v7U70K6PjTUkcDqXPzojKTCZ2iwRctpt-uAsuzwIxx9zBAWXHuse0JaTW51M-mUzvd675x5fTTy8VZ7ZbR94u3XjuuR', start_index=20774)
Annotation(end_index=20788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEpvUZAwXeNKjnddx6RBo4VogbS4ygf8wOpggH0LJjNLEVYM8fBUFxPkbgyHToNx94xZvjJ1_bdxBhOP5jMMFA0fBIIqMvKiMHzBTtPSXZ8Scn0x-c36cocbFyF33Dp-Idnlkm6NRRiaqHz7egrpcfE-0tsg==', start_index=20774)
Annotation(end_index=20891, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELWzd0kVFnrU8mcr0AJSYqztghOm3Pvr4rU0S-4sA9rHr8zRTU_8VX1v2fj9bCigqtJXdIEGjG3TnAcK6MUKLD5u6-5oeZEYjJ7Bhj5SgHiK0AVq4H6A3qpaRffiBdWawGttex_QpW', start_index=20882)
Annotation(end_index=21005, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlr2XKumCe31Iiu-N77GD_TBO_t5q1GZc9zzSA5n6WDUcDXkPhwRtmgJNZvAjCVwsLqT8SFkP_RDvTDtHjqOrd3z_hiJOflyjRj1efR-BZkU91MTwSYEt_Phn8xJW5ADwjfd6yzGJfveh8uCdEIpUUdn4xoKiIfW0OM06aYKClswVud1fPMR9EZKrFWAwyRcPZSWVDpErnEvpINIk4LO3OsLUAtZ6Cnw==', start_index=20995)
Annotation(end_index=21111, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPUfxCoFIr_mFwbFm_V6SbZ0298RXLLdwMydIFWIYsUwJFIjfDEVtb8oejFuARK-KGwF1z49FyLRMGYqPOUrZZDOXrMAOclpit1O8tKQE_SFzrXwSBqXK7xfHC5Hd8OFpftP9oNR5MzjiDs_Ee3Tjvr1a5nPzw5YUlLsNtzKEA4SAp2DAAfYyfIh6uMLRQc7fO8huiseFIWmEC3T4lHEechDUdL2AY-20lGyUr-gW89q_1LuDbesN2', start_index=21102)

## Sources
