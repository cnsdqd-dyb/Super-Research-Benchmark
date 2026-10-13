# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 0106c902 | **Time:** 320.26s | **Cost:** $1.60954
--------------------------------------------------------------------------------

# Stability Boundaries of Signal Coordination and System-Level Congestion Propagation

### Key Points
*   **Two Distinct Stability Regions:** Research identifies two critical flow rate regions within coordinated signal systems (Green Waves). In the higher flow region (bounded by maximum capacity and a specific threshold), traffic is "metastable," meaning congestion can occur spontaneously due to minor internal disturbances. In the lower flow region, congestion is only induced by external downstream bottlenecks.
*   **Propagation via Hysteresis:** Signal coordination failure leads to uneven distribution of density across the network. This inhomogeneity creates "hysteresis loops" in the Macroscopic Fundamental Diagram (MFD), where the network produces less flow for the same density during congestion recovery than during onset, effectively reducing the system's capacity and accelerating congestion propagation.
*   **Max-Pressure Stability:** Advanced control strategies like Max-Pressure control define stability as the ability to keep queue lengths bounded. These strategies maximize the "stable region"—the set of all traffic demands that can be accommodated without creating infinite queues—thereby preventing the localized saturation that triggers network-wide failure.
*   **Spillback and Feedback Loops:** When stability boundaries are breached (e.g., volume-to-capacity ratio > 1.0), queues from one intersection spill back into upstream links. This creates a feedback loop where the service rate of upstream intersections is reduced, causing congestion to propagate non-linearly through the network.

---

## 1. Introduction

The synchronization of traffic signals, commonly known as signal coordination or "Green Waves," is a fundamental strategy in urban traffic management designed to facilitate the continuous movement of vehicle platoons. However, the effectiveness of this coordination is governed by specific stability boundaries—thresholds of flow, density, and cycle timing beyond which the system transitions from a stable, free-flowing state to an unstable, congested state. Understanding how these boundaries function is critical because their violation does not merely result in local delays; it triggers complex, non-linear congestion propagation that can paralyze entire urban networks.

This report examines the theoretical and empirical mechanisms linking signal coordination stability to system-level congestion. It synthesizes findings from traffic physics (specifically Three-Phase Traffic Theory), network-level modeling (Macroscopic Fundamental Diagrams), and control theory (Lyapunov stability and Max-Pressure control). The analysis reveals that stability is not a binary state but a dynamic spectrum involving metastability, where minor perturbations can nucleate wide-moving jams that propagate upstream against the flow of traffic, fundamentally altering the network's operational capacity.

## 2. Theoretical Frameworks of Traffic Stability

To understand how congestion propagates from signal coordination failures, one must first define "stability" within the context of traffic flow. The literature presents two primary frameworks: the physics-based approach focusing on flow phases, and the control-theoretic approach focusing on queue boundedness.

### 2.1 Three-Phase Traffic Theory and Metastability
Classical traffic theories often view traffic as a two-phase system: free flow and congested flow. However, more rigorous analysis, particularly by Boris Kerner, introduces **Three-Phase Traffic Theory**, which distinguishes between Free Flow (F), Synchronized Flow (S), and Wide Moving Jams (J) [cite: 1, 2].

In the context of signal coordination, the transition from free flow to congestion is not always deterministic. The system often enters a **metastable state**. Within this state, the traffic flow is stable against small disturbances but unstable against large ones. This is crucial for signal coordination because it implies that a "Green Wave" can appear functional while actually being on the brink of collapse. A minor fluctuation—such as a single vehicle braking slightly too hard or a brief delay in start-up time at a green light—can act as a nucleus for a breakdown, causing a phase transition from Free Flow to Synchronized Flow [cite: 3, 4].

### 2.2 Control-Theoretic Stability (Bounded Queues)
From a traffic control perspective, particularly in the design of adaptive signal algorithms like Max-Pressure control, stability is defined differently. A network is considered stable if the number of vehicles in queues remains bounded over time [cite: 5, 6].

The **Stability Region** is defined as the set of all demand vectors (inflows) for which there exists *some* signal control policy that can keep queues bounded. If the demand falls outside this region, no amount of coordination can prevent queue growth, leading to inevitable oversaturation [cite: 6, 7]. Signal coordination strategies aim to maximize the size of this stable region. However, constraints such as fixed cycle lengths or minimum pedestrian crossing times can contract the stability boundary, making the system more susceptible to saturation [cite: 7].

## 3. The Physics of Green Wave Breakdown

The breakdown of a Green Wave (GW) is the primary mechanism by which stability boundaries affect congestion propagation. Research indicates that this breakdown is governed by specific flow rate thresholds.

### 3.1 Two Regions of Flow Rates
Physics-based simulations and empirical studies have identified two distinct regions of flow rates within a Green Wave that determine the nature of stability breakdown:

1.  **Region of Spontaneous Breakdown (High Flow):** This region is bounded by the maximum capacity of the road and a specific "threshold flow rate." In this high-flow regime, the Green Wave is metastable. A **time-delayed spontaneous breakdown** can occur with a certain probability [cite: 3, 8]. This means that even if the signals are perfectly timed theoretically, the intrinsic stochasticity of driver behavior (e.g., variations in speed, reaction times) can trigger a breakdown internally. The probability of this breakdown increases as the flow rate approaches capacity.
2.  **Region of Induced Breakdown (Lower Flow):** This region lies between the threshold flow rate and the minimum capacity. Here, the Green Wave is stable against internal disturbances. Breakdown cannot occur spontaneously; it can only be **induced** by an external bottleneck, such as a queue spilling back from a downstream intersection [cite: 3].

### 3.2 Nucleation and Phase Transitions
The mechanism of spontaneous breakdown in the high-flow region is described as **nucleation**. A "nucleus" for breakdown typically forms when a localized speed disturbance interacts with the traffic flow. In a coordinated signal system, this often happens when the tail of a platoon from a previous cycle interferes with the head of the next platoon, or when "synchronized flow" patterns emerge due to vehicle-following behaviors [cite: 3, 4].

Once this nucleus forms, it triggers an **F $\rightarrow$ S transition** (Free flow to Synchronized flow). In synchronized flow, vehicles continue to move, but their speeds are lower and highly correlated with adjacent lanes. This state is dangerous for network stability because it is often a precursor to **S $\rightarrow$ J transitions** (Synchronized flow to Wide Moving Jam), where traffic comes to a complete standstill and the jam propagates upstream as a shockwave [cite: 1, 2].

### 3.3 Impact of Cycle Length and Offsets
The stability of these regions is heavily influenced by signal timing parameters.
*   **Cycle Length:** If the cycle length is too short, the "lost time" (yellow/red clearance intervals) consumes a higher proportion of capacity, lowering the threshold for the high-flow instability region. Conversely, excessively long cycles can cause queues to grow beyond the storage capacity of the link, inducing breakdown from the "induced" mechanism (spillback) [cite: 9, 10].
*   **Offsets:** Incorrect offsets are a primary cause of coordination failure. If the offset does not match the travel time of the platoon, the platoon arrives during the red phase. This creates a "residual queue" that does not clear during the next green phase. This residual queue acts as a permanent disturbance, effectively pushing the system from the stable region into the unstable region [cite: 9, 11].

## 4. Network-Level Impacts: The Macroscopic Fundamental Diagram (MFD)

While the physics of Green Waves explains breakdown at the corridor level, the **Macroscopic Fundamental Diagram (MFD)** explains how these breakdowns propagate to affect the entire system. The MFD relates the average network density (accumulation) to the average network flow (production).

### 4.1 Coordination and MFD Shape
Signal coordination significantly impacts the shape of the MFD. A well-coordinated network exhibits a higher maximum flow (capacity) and sustains free-flow speeds at higher densities compared to an uncoordinated network [cite: 12].
*   **Capacity Reduction:** Poor coordination decreases the network's critical density (the density at which flow is maximized) and the maximum flow itself. This means the network becomes congested at lower traffic volumes [cite: 12].
*   **Scatter and Noise:** In the absence of stability, the relationship between flow and density becomes scattered. The MFD is well-defined only when congestion is somewhat homogeneous. Coordination failures introduce heterogeneity (some links are jammed while others are empty), which degrades the MFD's clarity and reliability for control purposes [cite: 13].

### 4.2 Hysteresis Loops and Instability
One of the most profound effects of stability boundaries on congestion propagation is the formation of **hysteresis loops** in the MFD.
*   **Clockwise Loops:** Research consistently observes clockwise hysteresis loops in the MFD during rush hours. This means that for the same average network density, the network produces *more* flow during the onset of congestion (loading phase) than during the recovery from congestion (unloading phase) [cite: 14, 15, 16].
*   **Mechanism:** This phenomenon occurs because congestion propagates unevenly. As the network loads, vehicles are relatively evenly distributed. However, as stability boundaries are breached, jams form in specific pockets (e.g., critical intersections). These jams cause "blocking" and spillback, trapping vehicles in inefficient states. During recovery, these pockets of high density remain jammed even as the average density drops, dragging down the overall network performance [cite: 14, 15].
*   **Coordination's Role:** Signal coordination strategies that fail to account for two-dimensional network effects can exacerbate this hysteresis. For example, optimizing a Green Wave along an arterial might severely penalize cross-street traffic. This creates extreme heterogeneity—the arterial flows well, but cross-streets jam. This inhomogeneity widens the hysteresis loop, meaning the network takes much longer to recover from congestion than it took to enter it [cite: 12].

### 4.3 Bifurcations
At high densities, the MFD can exhibit **bifurcations**, where the system can settle into either a high-flow or low-flow state for the same density, depending on the spatial distribution of jams. Stability boundaries determine which branch the system follows. If signal coordination maintains homogeneity, the system stays on the upper branch. If coordination fails and localized jams nucleate, the system collapses to the lower branch, leading to gridlock [cite: 12, 17].

## 5. Congestion Propagation Mechanisms

When the stability boundaries discussed above are breached, congestion propagates through the network via specific physical mechanisms.

### 5.1 Shockwave Dynamics
The primary vehicle for congestion propagation is the **shockwave**. When a Green Wave breaks down (spontaneously or induced), a transition zone forms between the fast-moving platoon and the stationary queue. This interface moves upstream as a backward recovery shockwave [cite: 18, 19].
*   **Propagation Speed:** The speed of this shockwave depends on the flow rate and density differential. In unstable conditions (Region 1), these shockwaves can amplify. A small braking maneuver can generate a shockwave that grows in magnitude as it propagates upstream, a phenomenon known as **string instability** [cite: 19].
*   **Intersection Interaction:** When a backward-moving shockwave reaches an upstream intersection, it interacts with the signal timing there. If the queue length exceeds the link length, **spillback** occurs.

### 5.2 Spillback and Blocking
**Spillback** is the physical manifestation of the "induced breakdown" mechanism. When a queue extends from a downstream intersection into an upstream intersection, it physically blocks vehicle movement [cite: 9, 20].
*   **De facto Red:** Even if the upstream signal is green, the spillback prevents vehicles from entering the intersection. This effectively reduces the capacity of the upstream intersection to zero during the blockage.
*   **Cross-Blocking:** Spillback often affects turning movements first. A left-turn lane overflowing into a through lane can block traffic that otherwise has a clear path. This lateral propagation causes congestion to spread to adjacent corridors that were not originally overloaded [cite: 9, 20].

### 5.3 Feedback in Queueing Networks
At a system level, these interactions create a **feedback loop**.
1.  Intersection A becomes oversaturated (Demand > Capacity).
2.  Queue spills back to Intersection B.
3.  Intersection B's effective discharge rate drops because its output link is blocked.
4.  Intersection B becomes oversaturated, even if its intrinsic demand was low.
5.  Queue spills back to Intersection C.

This propagation is modeled using **feedback fluid queueing networks** [cite: 21]. These models show that the service rate of a server (intersection) is state-dependent; it depends on the queue length of the downstream server. When stability boundaries are crossed, this dependency becomes dominant, causing congestion to spread exponentially rather than linearly [cite: 21].

## 6. Control Strategies and Stability Boundaries

Given the physics of breakdown and propagation, traffic control strategies focus on managing these stability boundaries.

### 6.1 Max-Pressure Control and Stability Maximization
**Max-Pressure (MP)** control is a decentralized strategy mathematically proven to maximize the stability region of a network. Unlike fixed-time coordination (which relies on historical data), MP makes decisions based on real-time queue lengths [cite: 5, 6].
*   **Mechanism:** MP balances queues by giving green time to phases with the highest "pressure" (difference between upstream queue and downstream queue capacity).
*   **Stability Guarantee:** MP guarantees that if a stable control exists for a given demand, MP will find it. It effectively pushes the stability boundary to its theoretical maximum [cite: 6, 7].
*   **Cycle Length Constraints:** While MP is theoretically optimal, practical implementations often require fixed cycle lengths for predictability. Research shows that imposing a maximum cycle length constraint slightly reduces the size of the stable region but maintains the property of maximum stability *within* those constraints [cite: 7].

### 6.2 Managing Oversaturation
When the system enters the unstable region (Oversaturation, v/c > 1.0), the objective of signal coordination shifts.
*   **From Progression to Queue Management:** In stable regions, the goal is progression (Green Waves). In unstable regions, the goal is **queue management** to prevent spillback [cite: 9, 20].
*   **Gating and Metering:** Strategies like "gating" deliberately hold traffic at upstream intersections (perimeter control) to protect critical downstream bottlenecks. This keeps the bottleneck in the stable, high-flow region of the MFD, preventing the hysteresis drop [cite: 12].

### 6.3 Adaptive vs. Fixed Control
Fixed-time coordination is highly susceptible to spontaneous breakdown because it cannot adapt to the stochastic variations in flow that trigger nucleation in the metastable region. Adaptive systems (like SCOOT, SCATS, or MP) can dynamically adjust splits and offsets to dampen these disturbances before they grow into wide moving jams, effectively expanding the operational stability boundary [cite: 22, 23].

## 7. Conclusion

The stability boundaries of signal coordination are the dividing lines between efficient urban mobility and systemic gridlock. These boundaries are not static; they are dynamic thresholds defined by the physics of traffic flow and the geometry of the network.

*   **Micro-Level:** At the corridor level, stability is threatened by the **metastability** of high-flow traffic. Spontaneous breakdowns can occur due to minor fluctuations, transitioning traffic from free flow to synchronized flow.
*   **Macro-Level:** These micro-level breakdowns propagate via **shockwaves** and **spillback**, creating **feedback loops** that degrade upstream capacity.
*   **System-Level:** The aggregate result is visible in the **Macroscopic Fundamental Diagram** as **hysteresis loops** and **bifurcations**. Coordination failure leads to inhomogeneity, which shrinks the network's capacity and prolongs recovery times.

Effective congestion management requires recognizing these boundaries. Strategies must transition from simple progression logic to active queue management and stability maximization (e.g., Max-Pressure) as traffic demands approach the critical thresholds of the metastable region. By maintaining the network within the stable region of the MFD and preventing the nucleation of jams, system-level congestion propagation can be significantly mitigated.

## References
[cite: 22] Hu, J. et al. (2023). "Network-level coordination... EMC method."
[cite: 9] FHWA (2021). "Traffic Signal Timing Manual: Chapter 3."
[cite: 11] Sebago Technics. "Traffic Signal Coordination."
[cite: 21] Li, D. et al. (2025). "Traffic Signal Control... Congestion Propagation... Queueing Network."
[cite: 12] Girault, J.T. et al. (2016). "Exploratory Analysis of Signal Coordination Impacts on MFD."
[cite: 13] TU Delft. "Chapter 11: Macroscopic fundamental diagram."
[cite: 18] Online-PDH. "Transportation Engineering Traffic Flow Analysis."
[cite: 19] Royal Society. (2011). "Linear stability properties of car-following models."
[cite: 12] Gayah, V.V. et al. (2011). "Macroscopic relations of urban traffic variables: Bifurcations..."
[cite: 17] MDPI (2023). "MFD... bifurcations in a high-density state."
[cite: 21] Li, D. et al. (2025). "Traffic Signal Control... Feedback fluid queueing network."
[cite: 3] Kerner, B.S. (2013). "The physics of green-wave breakdown in a city."
[cite: 10] IET (1967). "Determination of cycle length... stability boundary."
[cite: 3] Kerner, B.S. (2013). "The physics of green-wave breakdown... two regions."
[cite: 8] ResearchGate (2025). "Simulation of Green-Wave Traffic Control... breakdown."
[cite: 5] Arxiv (2024). "Max Pressure... maximum stability."
[cite: 7] ISTDM (2021). "Max-pressure control... stable region."
[cite: 1] Wikipedia. "Three-phase traffic theory."
[cite: 2] Diva Portal. "Traffic Theory... Kerner's three-phase."
[cite: 20] DOT (2008). "Signal Timing Under Saturated Conditions."
[cite: 7] ISTDM (2021). "Max Pressure control... fixed cycle length."
[cite: 6] NSF (2023). "Max-pressure control... stable region."
[cite: 12] Girault, J.T. et al. (2016). "Impact of signal offsets on MFD."
[cite: 3] Kerner, B.S. (2013). "Spontaneous green wave breakdown."
[cite: 4] ResearchGate (2025). "Physics of empirical nuclei for spontaneous traffic breakdown."
[cite: 14] PSU. "Hysteresis Patterns in MFD."
[cite: 15] Arxiv (2024). "Hysteresis Behind A Freeway Bottleneck."
[cite: 3] ResearchGate. "Two distinct regions of flow rates... green wave."

**Sources:**
1. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE09e46ASoGSCFk7CHbw5-Nh6IPnWpbZ3vuDGxvQ2ZicCHqb0sBoFcf-ttA-SUn3k6hNDZRBHu7VwI4nbwdBjQZWm7abD3qVBMZgOlbU6dx_FNd1ozZfveeLtoo4QolVNngypZpWAqwJE5nMgcMZQ==)
2. [diva-portal.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiRFKgfm3B5mAR2kKvlKG2XPFL93tIBmqUa3xTzFJoTotOsxOW17VFCvXTBx7mZYZvDNFUvwbD6d5QPfFbGoI8Vx7-lPnGA3tcQrMtO3aN2LkNTJKtO8rFUeya_vuqUulVz9UbTFNLfYfy_xP2Y6EoZLsiu7u197I=)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFV3kJYHVr4t4YKdzjcWdIhvy8tTCvfaR5BHpPkmD_k9ozOhXnZ_rWZryZj3ZfD8fXKMBpQGQv-PmIvHZGhBHv-9CKpNCFnRwEFY21jYklavKbn2exK3cdUpAWK_gjPQ9GcHW9Hl6PUMl3kVaBSty1ZatRuJaYSKGduyabcYxDNAbHkzlsVfAOmF4xOgPI3CgJ6h8-hhU=)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMUNjr97BBRrQGG9QZz89PE4WoCsPPtQW8qcByHoz9sjyR7e_7-VHk6XCXdiyyCL6esBYW8wF30w9un_WgtUIMBg1AiMnzo_4K5Zq5ycbkQb67sNYG5DFdX6VdblEC8lI28TWVf_rBsOs31lNYzi6DBRRyQkgkhRtg5JtKFdYnupAyoozQrkjyolfjXZVVWWAhQColXlGXhf5K0HxvI5IRAppJMUATj-6NV9hPGiiGHGIWKoQdPl9JmaCjxTHQXkrC-vEIAurth1JSxpoY8dg=)
5. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJoVVq6u4WpRNKkZ0vPl_zsDtrfofDRBpYSOjkpemi6-Fic1xefZeq-mtV07vWiDxI2CqPlcOwufbwNj35XEvYeYH1C2kpDnFKjUnFkulLPBUWbQLwA2y7Pw==)
6. [nsf.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-taEdFsjnsg3OE-yJ6RMA2AqAg-XLSKbKGVOsLYaQgpQ-CudYjMPHfwahf5ytT0I4070jHHXZr6IaBpTYcHj4Yyosyg1fTa6IskDwkkva9VxDXrVF5D30oeQ8j1pltiY=)
7. [umich.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcAfW5wwPKKM9COaanvXUKaLgLNJgCDemqegcL-rW2RraX-IFWqsRKZcK0piJ0csHkNIed0Cg5FwJHYmN4B_w0cKX2Q4Hq0NmNdVcuwqGidAfl3QHh0k5jq-RdcDfv6pTa65Hn8qi9VZOs59qX7PTNvTjYTtK4UY8F-YTuRO8wEEfFjRoJhJoBWUK__GlnnwchFsncXEJvkMsGuO4Jz6TGbBcmXb27)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHL7kxtjInTKVRRvgUax1R-9-qQ88q5HH99a1np3Cg3as8oqAaxqOFnjRQCRXcxX2Mt7ApuPgsivcFj1Kp4WY8Xt1Z-NwLURstyqMAsqQRD-K4tndVwmnh4Css2uyHn3_dgFzyNpMSsVSPagvXQkk55ei7G1eUAaMNjqZ9RYdC30rju9SFj0mTUjExxUZXwtJpSntM5DI_xJStLzOD3Y5K-Kkeo7yOAw2js1A==)
9. [dot.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6HxepP6Nlc6-6oqq9gtLlHRzSN6dx22wDKhjprOM1AYopWTAtxoA6Lvb3taPToh3eO-hfHYiHfmG8f_k8PgSs039u6UdefZHlxnoXQcROhdZ_NYChZXJuHG6s8W-4l1t9E8vHOTem-WOON8N8a0U6iI8x-FI=)
10. [theiet.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQzVH3Krx_rEVuq16650oflIOeOjjY_KQb-QKyktQXtWX74DhYHg9Ro9BCG1zRDS9yEGdRRiHRlFdPeHKPyJy6X7gYrX42XWeFfDTaiTzNrMqNLuDkYcpUndjZBoDfMGNcHLPWvDzxIA7zthunWQ1quzBa3CgVaAyiO1qnya-e6YTWsMw=)
11. [sebagotechnics.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyWw75jSetdrXQMQEzcHLtuJ2Slvrw4wSn_I2xAaWRB6L3nU7NAoEmdOqBUde8vd2RdFtrVsJQaDQ_x8XQsUIm-DLNZSZM0GJAPCftIASxNBcHs4KY-gHF6seUafqwXXcVFuxHiDjFG2ltRG3701SeWYGeBBOO74I=)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1GvTO5hHF7TWCpaEMv9pSEcxJe_KaciaJnTxcwYALg8lzXxqHzk2qvYJQJcW5-h-amwunoRD4IkRjNDrMJ4iTaL82U2ivs8PkJ-OpezBvVfSAY9K8IbPQOLv65h91-hif91DyGxH56nTul7qQOtv16LA0H4f3xvpjgzhsXy_xttT6LwwSQTykG2Ib5B7ye_X7t9BsSriTrQ5eVusorjdf-jHBEc_mPy-FUlKSVtYbiYPRXe9A05zUMuWCw1B2h8I=)
13. [tudelft.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiZXg6WEw-G062JnCEgZyskElOpqAT-tRbA-IYQBmi63J4JSkz9Wr1HB08oqAOXEZ8IFXCUMXPzqfMdsClyjHTVU3qtD0JybZVp_rdw9RHzqME8jmzaABxntzzpCGKn5KPSLTMprxVZoIlUWp0hUci2WyxwYrVeGqmcB_EcOVWG3uNpzapLyGUw8g-b3k=)
14. [psu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM1OJV3mBCBR191NzwI80egsLyrxg31NilmorUicG7kNEtqKv69F6hJjfIlViYZWWSfUhEyaJ0MMkN2M5gvBO9IvmA8vp2bNecQq5rmbPioRunZMvLaKCuHUD-IJZoc7L3Sz1Rd98=)
15. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIh3ZmENpmybR1_HA3SwcwvlDte33tNppwpfTO8M_8ITkAvxa_fY4h4jeD7tkgWwQ_0B_3r9GTKcKZreDV9Z3U3CcGP3CgmdpIDRooEfaohCqKrRyE9g==)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGZlen3AS_batP-QL1DKCdVGSwmeqqtvCRVTUAdobV1rlH2ea5oOyS1VTbC1JknAF9CHVThYiR0m0434o7UdvDcSVXXFrYktUUOD7CDJcT5flLRGoR9kCLhlIrAZeq_1a8iAzux3gP_ZPdDI8hYVGv1tjmmQmWPVmOjHfZ8H00BmXDBa1qS5KVJI0AdhU=)
17. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgiTe2mrWk3iEYtSv_izZTzalyNcm7BPPHR9gtftvZUleHxgngH69EGd3EmC6hSv1r9vz5TcNz5PCvmnm3fybCXCOveL0VH3wHE121_O4B-oE-tsLdwgrRuyjDStEqug==)
18. [online-pdh.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7m4RWSfTxoZOH-poXP9QqkTPXBoQZNTtKorJTVPu0kLWD4YmhJVGuZS_OxG2Blt393invrqMKZHwYGKdLgCUvhFUKtJVgJR90XZ09wsEzkD0MGwbSM4-m_VDNbxA2AmGURp2eJgr3ReU7Jro9S5G3M2UGydyKn4VJSPJGSUUmH1jOfM2quofpak9CLtLBfA0z8h8reG_FT_Etp_dBEnBUdld9RCw0zZ9YjGqV9loA-bKYAgUjrhD43cg=)
19. [royalsocietypublishing.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcXpBZxOIHK25UUy63gFbCyCIGgl9Y5twQtX-38w6NBD8K9qkpxkNo_PiJA03w04HEOiJWIrwetiLc0_zqVmG02fD7V-JmlE9EcNTlZAfLieoVxT4aLen0mGUOfdndXQgHTcv1cBh3YVDdu0slxQQtc_dd)
20. [bts.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkwqzRV5efvUluhDWRmZqV-AspyA-Flt9spSEuI-SFQArdgG19-dQ8h6kdD3O94crQ2s9rm8FoIhv9ec3DtxuIF6gbN7phYFPko5tYY2khYSgykACt_hAiJN22VcmAu2iorSDORd3Hsmoa2pYYwmOE)
21. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSY9Md-edIWSPBpb9eeO1vRyi5vnlumXGFng9ojb3lXK1Da49tibpR5-eMjXel4p88901OTfm-PIBHQpHtEzj0-hwdml6mSSCaajIyU_HulM2Ylcn7EZ_Xjhz1-vUta_IOa7Dno4XPaHMyxqtrqmNI9FWnMt4K7wlhcU_yqH1BEKrj0hOgFxizu0gco9CYJjNQuYMbQ_gVyla_XOKMwmuxnp-d7Us_jBi11Kjuy0gEfweMOX1jwvRMQUM09UcNVmQfkV1fYIEpNaV5bJtXA4TAntKTtmFTZU7_EK8mSmnggRS00gMU1fvZHxPZydJRdXHmAg==)
22. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGN41wbpGy3HAmTogeW1iML5EpY4tkJKI_jnlodrtVSmvo3_HOU3MpXm19V1I_BiaQncSfZDigOIxIENv4NYs_LSFr00nnbTMuSffk45Q7GLV6XZTiWxw==)
23. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEe7wu4__IThRSDtlGpVAAkBLB_8lsn8qT3dPewlSw1OdAUsfDbbAMB4y3rKgnXW_6iIg4uTELczM8JOfns9WVjPuPoCW_wjVhTKdtXrDonRcB9x2bd_6Kmxjz-MiP1aQ==)


## Annotations
Annotation(end_index=3668, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE09e46ASoGSCFk7CHbw5-Nh6IPnWpbZ3vuDGxvQ2ZicCHqb0sBoFcf-ttA-SUn3k6hNDZRBHu7VwI4nbwdBjQZWm7abD3qVBMZgOlbU6dx_FNd1ozZfveeLtoo4QolVNngypZpWAqwJE5nMgcMZQ==', start_index=3656)
Annotation(end_index=3668, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiRFKgfm3B5mAR2kKvlKG2XPFL93tIBmqUa3xTzFJoTotOsxOW17VFCvXTBx7mZYZvDNFUvwbD6d5QPfFbGoI8Vx7-lPnGA3tcQrMtO3aN2LkNTJKtO8rFUeya_vuqUulVz9UbTFNLfYfy_xP2Y6EoZLsiu7u197I=', start_index=3656)
Annotation(end_index=4324, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMUNjr97BBRrQGG9QZz89PE4WoCsPPtQW8qcByHoz9sjyR7e_7-VHk6XCXdiyyCL6esBYW8wF30w9un_WgtUIMBg1AiMnzo_4K5Zq5ycbkQb67sNYG5DFdX6VdblEC8lI28TWVf_rBsOs31lNYzi6DBRRyQkgkhRtg5JtKFdYnupAyoozQrkjyolfjXZVVWWAhQColXlGXhf5K0HxvI5IRAppJMUATj-6NV9hPGiiGHGIWKoQdPl9JmaCjxTHQXkrC-vEIAurth1JSxpoY8dg=', start_index=4312)
Annotation(end_index=4324, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFV3kJYHVr4t4YKdzjcWdIhvy8tTCvfaR5BHpPkmD_k9ozOhXnZ_rWZryZj3ZfD8fXKMBpQGQv-PmIvHZGhBHv-9CKpNCFnRwEFY21jYklavKbn2exK3cdUpAWK_gjPQ9GcHW9Hl6PUMl3kVaBSty1ZatRuJaYSKGduyabcYxDNAbHkzlsVfAOmF4xOgPI3CgJ6h8-hhU=', start_index=4312)
Annotation(end_index=4639, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-taEdFsjnsg3OE-yJ6RMA2AqAg-XLSKbKGVOsLYaQgpQ-CudYjMPHfwahf5ytT0I4070jHHXZr6IaBpTYcHj4Yyosyg1fTa6IskDwkkva9VxDXrVF5D30oeQ8j1pltiY=', start_index=4627)
Annotation(end_index=4639, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJoVVq6u4WpRNKkZ0vPl_zsDtrfofDRBpYSOjkpemi6-Fic1xefZeq-mtV07vWiDxI2CqPlcOwufbwNj35XEvYeYH1C2kpDnFKjUnFkulLPBUWbQLwA2y7Pw==', start_index=4627)
Annotation(end_index=4945, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcAfW5wwPKKM9COaanvXUKaLgLNJgCDemqegcL-rW2RraX-IFWqsRKZcK0piJ0csHkNIed0Cg5FwJHYmN4B_w0cKX2Q4Hq0NmNdVcuwqGidAfl3QHh0k5jq-RdcDfv6pTa65Hn8qi9VZOs59qX7PTNvTjYTtK4UY8F-YTuRO8wEEfFjRoJhJoBWUK__GlnnwchFsncXEJvkMsGuO4Jz6TGbBcmXb27', start_index=4933)
Annotation(end_index=4945, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-taEdFsjnsg3OE-yJ6RMA2AqAg-XLSKbKGVOsLYaQgpQ-CudYjMPHfwahf5ytT0I4070jHHXZr6IaBpTYcHj4Yyosyg1fTa6IskDwkkva9VxDXrVF5D30oeQ8j1pltiY=', start_index=4933)
Annotation(end_index=5207, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcAfW5wwPKKM9COaanvXUKaLgLNJgCDemqegcL-rW2RraX-IFWqsRKZcK0piJ0csHkNIed0Cg5FwJHYmN4B_w0cKX2Q4Hq0NmNdVcuwqGidAfl3QHh0k5jq-RdcDfv6pTa65Hn8qi9VZOs59qX7PTNvTjYTtK4UY8F-YTuRO8wEEfFjRoJhJoBWUK__GlnnwchFsncXEJvkMsGuO4Jz6TGbBcmXb27', start_index=5198)
Annotation(end_index=5960, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFV3kJYHVr4t4YKdzjcWdIhvy8tTCvfaR5BHpPkmD_k9ozOhXnZ_rWZryZj3ZfD8fXKMBpQGQv-PmIvHZGhBHv-9CKpNCFnRwEFY21jYklavKbn2exK3cdUpAWK_gjPQ9GcHW9Hl6PUMl3kVaBSty1ZatRuJaYSKGduyabcYxDNAbHkzlsVfAOmF4xOgPI3CgJ6h8-hhU=', start_index=5948)
Annotation(end_index=5960, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHL7kxtjInTKVRRvgUax1R-9-qQ88q5HH99a1np3Cg3as8oqAaxqOFnjRQCRXcxX2Mt7ApuPgsivcFj1Kp4WY8Xt1Z-NwLURstyqMAsqQRD-K4tndVwmnh4Css2uyHn3_dgFzyNpMSsVSPagvXQkk55ei7G1eUAaMNjqZ9RYdC30rju9SFj0mTUjExxUZXwtJpSntM5DI_xJStLzOD3Y5K-Kkeo7yOAw2js1A==', start_index=5948)
Annotation(end_index=6591, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFV3kJYHVr4t4YKdzjcWdIhvy8tTCvfaR5BHpPkmD_k9ozOhXnZ_rWZryZj3ZfD8fXKMBpQGQv-PmIvHZGhBHv-9CKpNCFnRwEFY21jYklavKbn2exK3cdUpAWK_gjPQ9GcHW9Hl6PUMl3kVaBSty1ZatRuJaYSKGduyabcYxDNAbHkzlsVfAOmF4xOgPI3CgJ6h8-hhU=', start_index=6582)
Annotation(end_index=7077, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMUNjr97BBRrQGG9QZz89PE4WoCsPPtQW8qcByHoz9sjyR7e_7-VHk6XCXdiyyCL6esBYW8wF30w9un_WgtUIMBg1AiMnzo_4K5Zq5ycbkQb67sNYG5DFdX6VdblEC8lI28TWVf_rBsOs31lNYzi6DBRRyQkgkhRtg5JtKFdYnupAyoozQrkjyolfjXZVVWWAhQColXlGXhf5K0HxvI5IRAppJMUATj-6NV9hPGiiGHGIWKoQdPl9JmaCjxTHQXkrC-vEIAurth1JSxpoY8dg=', start_index=7065)
Annotation(end_index=7077, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFV3kJYHVr4t4YKdzjcWdIhvy8tTCvfaR5BHpPkmD_k9ozOhXnZ_rWZryZj3ZfD8fXKMBpQGQv-PmIvHZGhBHv-9CKpNCFnRwEFY21jYklavKbn2exK3cdUpAWK_gjPQ9GcHW9Hl6PUMl3kVaBSty1ZatRuJaYSKGduyabcYxDNAbHkzlsVfAOmF4xOgPI3CgJ6h8-hhU=', start_index=7065)
Annotation(end_index=7565, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE09e46ASoGSCFk7CHbw5-Nh6IPnWpbZ3vuDGxvQ2ZicCHqb0sBoFcf-ttA-SUn3k6hNDZRBHu7VwI4nbwdBjQZWm7abD3qVBMZgOlbU6dx_FNd1ozZfveeLtoo4QolVNngypZpWAqwJE5nMgcMZQ==', start_index=7553)
Annotation(end_index=7565, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiRFKgfm3B5mAR2kKvlKG2XPFL93tIBmqUa3xTzFJoTotOsxOW17VFCvXTBx7mZYZvDNFUvwbD6d5QPfFbGoI8Vx7-lPnGA3tcQrMtO3aN2LkNTJKtO8rFUeya_vuqUulVz9UbTFNLfYfy_xP2Y6EoZLsiu7u197I=', start_index=7553)
Annotation(end_index=8076, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6HxepP6Nlc6-6oqq9gtLlHRzSN6dx22wDKhjprOM1AYopWTAtxoA6Lvb3taPToh3eO-hfHYiHfmG8f_k8PgSs039u6UdefZHlxnoXQcROhdZ_NYChZXJuHG6s8W-4l1t9E8vHOTem-WOON8N8a0U6iI8x-FI=', start_index=8063)
Annotation(end_index=8076, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQzVH3Krx_rEVuq16650oflIOeOjjY_KQb-QKyktQXtWX74DhYHg9Ro9BCG1zRDS9yEGdRRiHRlFdPeHKPyJy6X7gYrX42XWeFfDTaiTzNrMqNLuDkYcpUndjZBoDfMGNcHLPWvDzxIA7zthunWQ1quzBa3CgVaAyiO1qnya-e6YTWsMw=', start_index=8063)
Annotation(end_index=8487, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6HxepP6Nlc6-6oqq9gtLlHRzSN6dx22wDKhjprOM1AYopWTAtxoA6Lvb3taPToh3eO-hfHYiHfmG8f_k8PgSs039u6UdefZHlxnoXQcROhdZ_NYChZXJuHG6s8W-4l1t9E8vHOTem-WOON8N8a0U6iI8x-FI=', start_index=8474)
Annotation(end_index=8487, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyWw75jSetdrXQMQEzcHLtuJ2Slvrw4wSn_I2xAaWRB6L3nU7NAoEmdOqBUde8vd2RdFtrVsJQaDQ_x8XQsUIm-DLNZSZM0GJAPCftIASxNBcHs4KY-gHF6seUafqwXXcVFuxHiDjFG2ltRG3701SeWYGeBBOO74I=', start_index=8474)
Annotation(end_index=9119, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1GvTO5hHF7TWCpaEMv9pSEcxJe_KaciaJnTxcwYALg8lzXxqHzk2qvYJQJcW5-h-amwunoRD4IkRjNDrMJ4iTaL82U2ivs8PkJ-OpezBvVfSAY9K8IbPQOLv65h91-hif91DyGxH56nTul7qQOtv16LA0H4f3xvpjgzhsXy_xttT6LwwSQTykG2Ib5B7ye_X7t9BsSriTrQ5eVusorjdf-jHBEc_mPy-FUlKSVtYbiYPRXe9A05zUMuWCw1B2h8I=', start_index=9109)
Annotation(end_index=9354, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1GvTO5hHF7TWCpaEMv9pSEcxJe_KaciaJnTxcwYALg8lzXxqHzk2qvYJQJcW5-h-amwunoRD4IkRjNDrMJ4iTaL82U2ivs8PkJ-OpezBvVfSAY9K8IbPQOLv65h91-hif91DyGxH56nTul7qQOtv16LA0H4f3xvpjgzhsXy_xttT6LwwSQTykG2Ib5B7ye_X7t9BsSriTrQ5eVusorjdf-jHBEc_mPy-FUlKSVtYbiYPRXe9A05zUMuWCw1B2h8I=', start_index=9344)
Annotation(end_index=9717, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiZXg6WEw-G062JnCEgZyskElOpqAT-tRbA-IYQBmi63J4JSkz9Wr1HB08oqAOXEZ8IFXCUMXPzqfMdsClyjHTVU3qtD0JybZVp_rdw9RHzqME8jmzaABxntzzpCGKn5KPSLTMprxVZoIlUWp0hUci2WyxwYrVeGqmcB_EcOVWG3uNpzapLyGUw8g-b3k=', start_index=9707)
Annotation(end_index=10221, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGZlen3AS_batP-QL1DKCdVGSwmeqqtvCRVTUAdobV1rlH2ea5oOyS1VTbC1JknAF9CHVThYiR0m0434o7UdvDcSVXXFrYktUUOD7CDJcT5flLRGoR9kCLhlIrAZeq_1a8iAzux3gP_ZPdDI8hYVGv1tjmmQmWPVmOjHfZ8H00BmXDBa1qS5KVJI0AdhU=', start_index=10203)
Annotation(end_index=10221, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIh3ZmENpmybR1_HA3SwcwvlDte33tNppwpfTO8M_8ITkAvxa_fY4h4jeD7tkgWwQ_0B_3r9GTKcKZreDV9Z3U3CcGP3CgmdpIDRooEfaohCqKrRyE9g==', start_index=10203)
Annotation(end_index=10221, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM1OJV3mBCBR191NzwI80egsLyrxg31NilmorUicG7kNEtqKv69F6hJjfIlViYZWWSfUhEyaJ0MMkN2M5gvBO9IvmA8vp2bNecQq5rmbPioRunZMvLaKCuHUD-IJZoc7L3Sz1Rd98=', start_index=10203)
Annotation(end_index=10720, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIh3ZmENpmybR1_HA3SwcwvlDte33tNppwpfTO8M_8ITkAvxa_fY4h4jeD7tkgWwQ_0B_3r9GTKcKZreDV9Z3U3CcGP3CgmdpIDRooEfaohCqKrRyE9g==', start_index=10706)
Annotation(end_index=10720, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM1OJV3mBCBR191NzwI80egsLyrxg31NilmorUicG7kNEtqKv69F6hJjfIlViYZWWSfUhEyaJ0MMkN2M5gvBO9IvmA8vp2bNecQq5rmbPioRunZMvLaKCuHUD-IJZoc7L3Sz1Rd98=', start_index=10706)
Annotation(end_index=11204, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1GvTO5hHF7TWCpaEMv9pSEcxJe_KaciaJnTxcwYALg8lzXxqHzk2qvYJQJcW5-h-amwunoRD4IkRjNDrMJ4iTaL82U2ivs8PkJ-OpezBvVfSAY9K8IbPQOLv65h91-hif91DyGxH56nTul7qQOtv16LA0H4f3xvpjgzhsXy_xttT6LwwSQTykG2Ib5B7ye_X7t9BsSriTrQ5eVusorjdf-jHBEc_mPy-FUlKSVtYbiYPRXe9A05zUMuWCw1B2h8I=', start_index=11194)
Annotation(end_index=11699, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1GvTO5hHF7TWCpaEMv9pSEcxJe_KaciaJnTxcwYALg8lzXxqHzk2qvYJQJcW5-h-amwunoRD4IkRjNDrMJ4iTaL82U2ivs8PkJ-OpezBvVfSAY9K8IbPQOLv65h91-hif91DyGxH56nTul7qQOtv16LA0H4f3xvpjgzhsXy_xttT6LwwSQTykG2Ib5B7ye_X7t9BsSriTrQ5eVusorjdf-jHBEc_mPy-FUlKSVtYbiYPRXe9A05zUMuWCw1B2h8I=', start_index=11685)
Annotation(end_index=11699, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgiTe2mrWk3iEYtSv_izZTzalyNcm7BPPHR9gtftvZUleHxgngH69EGd3EmC6hSv1r9vz5TcNz5PCvmnm3fybCXCOveL0VH3wHE121_O4B-oE-tsLdwgrRuyjDStEqug==', start_index=11685)
Annotation(end_index=12193, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7m4RWSfTxoZOH-poXP9QqkTPXBoQZNTtKorJTVPu0kLWD4YmhJVGuZS_OxG2Blt393invrqMKZHwYGKdLgCUvhFUKtJVgJR90XZ09wsEzkD0MGwbSM4-m_VDNbxA2AmGURp2eJgr3ReU7Jro9S5G3M2UGydyKn4VJSPJGSUUmH1jOfM2quofpak9CLtLBfA0z8h8reG_FT_Etp_dBEnBUdld9RCw0zZ9YjGqV9loA-bKYAgUjrhD43cg=', start_index=12179)
Annotation(end_index=12193, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcXpBZxOIHK25UUy63gFbCyCIGgl9Y5twQtX-38w6NBD8K9qkpxkNo_PiJA03w04HEOiJWIrwetiLc0_zqVmG02fD7V-JmlE9EcNTlZAfLieoVxT4aLen0mGUOfdndXQgHTcv1cBh3YVDdu0slxQQtc_dd', start_index=12179)
Annotation(end_index=12522, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcXpBZxOIHK25UUy63gFbCyCIGgl9Y5twQtX-38w6NBD8K9qkpxkNo_PiJA03w04HEOiJWIrwetiLc0_zqVmG02fD7V-JmlE9EcNTlZAfLieoVxT4aLen0mGUOfdndXQgHTcv1cBh3YVDdu0slxQQtc_dd', start_index=12512)
Annotation(end_index=12983, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6HxepP6Nlc6-6oqq9gtLlHRzSN6dx22wDKhjprOM1AYopWTAtxoA6Lvb3taPToh3eO-hfHYiHfmG8f_k8PgSs039u6UdefZHlxnoXQcROhdZ_NYChZXJuHG6s8W-4l1t9E8vHOTem-WOON8N8a0U6iI8x-FI=', start_index=12970)
Annotation(end_index=12983, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkwqzRV5efvUluhDWRmZqV-AspyA-Flt9spSEuI-SFQArdgG19-dQ8h6kdD3O94crQ2s9rm8FoIhv9ec3DtxuIF6gbN7phYFPko5tYY2khYSgykACt_hAiJN22VcmAu2iorSDORd3Hsmoa2pYYwmOE', start_index=12970)
Annotation(end_index=13502, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6HxepP6Nlc6-6oqq9gtLlHRzSN6dx22wDKhjprOM1AYopWTAtxoA6Lvb3taPToh3eO-hfHYiHfmG8f_k8PgSs039u6UdefZHlxnoXQcROhdZ_NYChZXJuHG6s8W-4l1t9E8vHOTem-WOON8N8a0U6iI8x-FI=', start_index=13489)
Annotation(end_index=13502, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkwqzRV5efvUluhDWRmZqV-AspyA-Flt9spSEuI-SFQArdgG19-dQ8h6kdD3O94crQ2s9rm8FoIhv9ec3DtxuIF6gbN7phYFPko5tYY2khYSgykACt_hAiJN22VcmAu2iorSDORd3Hsmoa2pYYwmOE', start_index=13489)
Annotation(end_index=14003, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSY9Md-edIWSPBpb9eeO1vRyi5vnlumXGFng9ojb3lXK1Da49tibpR5-eMjXel4p88901OTfm-PIBHQpHtEzj0-hwdml6mSSCaajIyU_HulM2Ylcn7EZ_Xjhz1-vUta_IOa7Dno4XPaHMyxqtrqmNI9FWnMt4K7wlhcU_yqH1BEKrj0hOgFxizu0gco9CYJjNQuYMbQ_gVyla_XOKMwmuxnp-d7Us_jBi11Kjuy0gEfweMOX1jwvRMQUM09UcNVmQfkV1fYIEpNaV5bJtXA4TAntKTtmFTZU7_EK8mSmnggRS00gMU1fvZHxPZydJRdXHmAg==', start_index=13993)
Annotation(end_index=14296, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSY9Md-edIWSPBpb9eeO1vRyi5vnlumXGFng9ojb3lXK1Da49tibpR5-eMjXel4p88901OTfm-PIBHQpHtEzj0-hwdml6mSSCaajIyU_HulM2Ylcn7EZ_Xjhz1-vUta_IOa7Dno4XPaHMyxqtrqmNI9FWnMt4K7wlhcU_yqH1BEKrj0hOgFxizu0gco9CYJjNQuYMbQ_gVyla_XOKMwmuxnp-d7Us_jBi11Kjuy0gEfweMOX1jwvRMQUM09UcNVmQfkV1fYIEpNaV5bJtXA4TAntKTtmFTZU7_EK8mSmnggRS00gMU1fvZHxPZydJRdXHmAg==', start_index=14286)
Annotation(end_index=14785, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-taEdFsjnsg3OE-yJ6RMA2AqAg-XLSKbKGVOsLYaQgpQ-CudYjMPHfwahf5ytT0I4070jHHXZr6IaBpTYcHj4Yyosyg1fTa6IskDwkkva9VxDXrVF5D30oeQ8j1pltiY=', start_index=14773)
Annotation(end_index=14785, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJoVVq6u4WpRNKkZ0vPl_zsDtrfofDRBpYSOjkpemi6-Fic1xefZeq-mtV07vWiDxI2CqPlcOwufbwNj35XEvYeYH1C2kpDnFKjUnFkulLPBUWbQLwA2y7Pw==', start_index=14773)
Annotation(end_index=15147, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcAfW5wwPKKM9COaanvXUKaLgLNJgCDemqegcL-rW2RraX-IFWqsRKZcK0piJ0csHkNIed0Cg5FwJHYmN4B_w0cKX2Q4Hq0NmNdVcuwqGidAfl3QHh0k5jq-RdcDfv6pTa65Hn8qi9VZOs59qX7PTNvTjYTtK4UY8F-YTuRO8wEEfFjRoJhJoBWUK__GlnnwchFsncXEJvkMsGuO4Jz6TGbBcmXb27', start_index=15135)
Annotation(end_index=15147, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-taEdFsjnsg3OE-yJ6RMA2AqAg-XLSKbKGVOsLYaQgpQ-CudYjMPHfwahf5ytT0I4070jHHXZr6IaBpTYcHj4Yyosyg1fTa6IskDwkkva9VxDXrVF5D30oeQ8j1pltiY=', start_index=15135)
Annotation(end_index=15492, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcAfW5wwPKKM9COaanvXUKaLgLNJgCDemqegcL-rW2RraX-IFWqsRKZcK0piJ0csHkNIed0Cg5FwJHYmN4B_w0cKX2Q4Hq0NmNdVcuwqGidAfl3QHh0k5jq-RdcDfv6pTa65Hn8qi9VZOs59qX7PTNvTjYTtK4UY8F-YTuRO8wEEfFjRoJhJoBWUK__GlnnwchFsncXEJvkMsGuO4Jz6TGbBcmXb27', start_index=15483)
Annotation(end_index=15836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6HxepP6Nlc6-6oqq9gtLlHRzSN6dx22wDKhjprOM1AYopWTAtxoA6Lvb3taPToh3eO-hfHYiHfmG8f_k8PgSs039u6UdefZHlxnoXQcROhdZ_NYChZXJuHG6s8W-4l1t9E8vHOTem-WOON8N8a0U6iI8x-FI=', start_index=15823)
Annotation(end_index=15836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkwqzRV5efvUluhDWRmZqV-AspyA-Flt9spSEuI-SFQArdgG19-dQ8h6kdD3O94crQ2s9rm8FoIhv9ec3DtxuIF6gbN7phYFPko5tYY2khYSgykACt_hAiJN22VcmAu2iorSDORd3Hsmoa2pYYwmOE', start_index=15823)
Annotation(end_index=16119, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1GvTO5hHF7TWCpaEMv9pSEcxJe_KaciaJnTxcwYALg8lzXxqHzk2qvYJQJcW5-h-amwunoRD4IkRjNDrMJ4iTaL82U2ivs8PkJ-OpezBvVfSAY9K8IbPQOLv65h91-hif91DyGxH56nTul7qQOtv16LA0H4f3xvpjgzhsXy_xttT6LwwSQTykG2Ib5B7ye_X7t9BsSriTrQ5eVusorjdf-jHBEc_mPy-FUlKSVtYbiYPRXe9A05zUMuWCw1B2h8I=', start_index=16109)
Annotation(end_index=16565, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEe7wu4__IThRSDtlGpVAAkBLB_8lsn8qT3dPewlSw1OdAUsfDbbAMB4y3rKgnXW_6iIg4uTELczM8JOfns9WVjPuPoCW_wjVhTKdtXrDonRcB9x2bd_6Kmxjz-MiP1aQ==', start_index=16551)
Annotation(end_index=16565, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGN41wbpGy3HAmTogeW1iML5EpY4tkJKI_jnlodrtVSmvo3_HOU3MpXm19V1I_BiaQncSfZDigOIxIENv4NYs_LSFr00nnbTMuSffk45Q7GLV6XZTiWxw==', start_index=16551)
Annotation(end_index=17970, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGN41wbpGy3HAmTogeW1iML5EpY4tkJKI_jnlodrtVSmvo3_HOU3MpXm19V1I_BiaQncSfZDigOIxIENv4NYs_LSFr00nnbTMuSffk45Q7GLV6XZTiWxw==', start_index=17960)
Annotation(end_index=18046, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6HxepP6Nlc6-6oqq9gtLlHRzSN6dx22wDKhjprOM1AYopWTAtxoA6Lvb3taPToh3eO-hfHYiHfmG8f_k8PgSs039u6UdefZHlxnoXQcROhdZ_NYChZXJuHG6s8W-4l1t9E8vHOTem-WOON8N8a0U6iI8x-FI=', start_index=18037)
Annotation(end_index=18113, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyWw75jSetdrXQMQEzcHLtuJ2Slvrw4wSn_I2xAaWRB6L3nU7NAoEmdOqBUde8vd2RdFtrVsJQaDQ_x8XQsUIm-DLNZSZM0GJAPCftIASxNBcHs4KY-gHF6seUafqwXXcVFuxHiDjFG2ltRG3701SeWYGeBBOO74I=', start_index=18103)
Annotation(end_index=18172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSY9Md-edIWSPBpb9eeO1vRyi5vnlumXGFng9ojb3lXK1Da49tibpR5-eMjXel4p88901OTfm-PIBHQpHtEzj0-hwdml6mSSCaajIyU_HulM2Ylcn7EZ_Xjhz1-vUta_IOa7Dno4XPaHMyxqtrqmNI9FWnMt4K7wlhcU_yqH1BEKrj0hOgFxizu0gco9CYJjNQuYMbQ_gVyla_XOKMwmuxnp-d7Us_jBi11Kjuy0gEfweMOX1jwvRMQUM09UcNVmQfkV1fYIEpNaV5bJtXA4TAntKTtmFTZU7_EK8mSmnggRS00gMU1fvZHxPZydJRdXHmAg==', start_index=18162)
Annotation(end_index=18277, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1GvTO5hHF7TWCpaEMv9pSEcxJe_KaciaJnTxcwYALg8lzXxqHzk2qvYJQJcW5-h-amwunoRD4IkRjNDrMJ4iTaL82U2ivs8PkJ-OpezBvVfSAY9K8IbPQOLv65h91-hif91DyGxH56nTul7qQOtv16LA0H4f3xvpjgzhsXy_xttT6LwwSQTykG2Ib5B7ye_X7t9BsSriTrQ5eVusorjdf-jHBEc_mPy-FUlKSVtYbiYPRXe9A05zUMuWCw1B2h8I=', start_index=18267)
Annotation(end_index=18379, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiZXg6WEw-G062JnCEgZyskElOpqAT-tRbA-IYQBmi63J4JSkz9Wr1HB08oqAOXEZ8IFXCUMXPzqfMdsClyjHTVU3qtD0JybZVp_rdw9RHzqME8jmzaABxntzzpCGKn5KPSLTMprxVZoIlUWp0hUci2WyxwYrVeGqmcB_EcOVWG3uNpzapLyGUw8g-b3k=', start_index=18369)
Annotation(end_index=18447, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7m4RWSfTxoZOH-poXP9QqkTPXBoQZNTtKorJTVPu0kLWD4YmhJVGuZS_OxG2Blt393invrqMKZHwYGKdLgCUvhFUKtJVgJR90XZ09wsEzkD0MGwbSM4-m_VDNbxA2AmGURp2eJgr3ReU7Jro9S5G3M2UGydyKn4VJSPJGSUUmH1jOfM2quofpak9CLtLBfA0z8h8reG_FT_Etp_dBEnBUdld9RCw0zZ9YjGqV9loA-bKYAgUjrhD43cg=', start_index=18437)
Annotation(end_index=18522, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcXpBZxOIHK25UUy63gFbCyCIGgl9Y5twQtX-38w6NBD8K9qkpxkNo_PiJA03w04HEOiJWIrwetiLc0_zqVmG02fD7V-JmlE9EcNTlZAfLieoVxT4aLen0mGUOfdndXQgHTcv1cBh3YVDdu0slxQQtc_dd', start_index=18512)
Annotation(end_index=18611, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1GvTO5hHF7TWCpaEMv9pSEcxJe_KaciaJnTxcwYALg8lzXxqHzk2qvYJQJcW5-h-amwunoRD4IkRjNDrMJ4iTaL82U2ivs8PkJ-OpezBvVfSAY9K8IbPQOLv65h91-hif91DyGxH56nTul7qQOtv16LA0H4f3xvpjgzhsXy_xttT6LwwSQTykG2Ib5B7ye_X7t9BsSriTrQ5eVusorjdf-jHBEc_mPy-FUlKSVtYbiYPRXe9A05zUMuWCw1B2h8I=', start_index=18601)
Annotation(end_index=18717, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgiTe2mrWk3iEYtSv_izZTzalyNcm7BPPHR9gtftvZUleHxgngH69EGd3EmC6hSv1r9vz5TcNz5PCvmnm3fybCXCOveL0VH3wHE121_O4B-oE-tsLdwgrRuyjDStEqug==', start_index=18707)
Annotation(end_index=18788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSY9Md-edIWSPBpb9eeO1vRyi5vnlumXGFng9ojb3lXK1Da49tibpR5-eMjXel4p88901OTfm-PIBHQpHtEzj0-hwdml6mSSCaajIyU_HulM2Ylcn7EZ_Xjhz1-vUta_IOa7Dno4XPaHMyxqtrqmNI9FWnMt4K7wlhcU_yqH1BEKrj0hOgFxizu0gco9CYJjNQuYMbQ_gVyla_XOKMwmuxnp-d7Us_jBi11Kjuy0gEfweMOX1jwvRMQUM09UcNVmQfkV1fYIEpNaV5bJtXA4TAntKTtmFTZU7_EK8mSmnggRS00gMU1fvZHxPZydJRdXHmAg==', start_index=18778)
Annotation(end_index=18881, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFV3kJYHVr4t4YKdzjcWdIhvy8tTCvfaR5BHpPkmD_k9ozOhXnZ_rWZryZj3ZfD8fXKMBpQGQv-PmIvHZGhBHv-9CKpNCFnRwEFY21jYklavKbn2exK3cdUpAWK_gjPQ9GcHW9Hl6PUMl3kVaBSty1ZatRuJaYSKGduyabcYxDNAbHkzlsVfAOmF4xOgPI3CgJ6h8-hhU=', start_index=18872)
Annotation(end_index=18962, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQzVH3Krx_rEVuq16650oflIOeOjjY_KQb-QKyktQXtWX74DhYHg9Ro9BCG1zRDS9yEGdRRiHRlFdPeHKPyJy6X7gYrX42XWeFfDTaiTzNrMqNLuDkYcpUndjZBoDfMGNcHLPWvDzxIA7zthunWQ1quzBa3CgVaAyiO1qnya-e6YTWsMw=', start_index=18952)
Annotation(end_index=19039, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFV3kJYHVr4t4YKdzjcWdIhvy8tTCvfaR5BHpPkmD_k9ozOhXnZ_rWZryZj3ZfD8fXKMBpQGQv-PmIvHZGhBHv-9CKpNCFnRwEFY21jYklavKbn2exK3cdUpAWK_gjPQ9GcHW9Hl6PUMl3kVaBSty1ZatRuJaYSKGduyabcYxDNAbHkzlsVfAOmF4xOgPI3CgJ6h8-hhU=', start_index=19030)
Annotation(end_index=19124, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHL7kxtjInTKVRRvgUax1R-9-qQ88q5HH99a1np3Cg3as8oqAaxqOFnjRQCRXcxX2Mt7ApuPgsivcFj1Kp4WY8Xt1Z-NwLURstyqMAsqQRD-K4tndVwmnh4Css2uyHn3_dgFzyNpMSsVSPagvXQkk55ei7G1eUAaMNjqZ9RYdC30rju9SFj0mTUjExxUZXwtJpSntM5DI_xJStLzOD3Y5K-Kkeo7yOAw2js1A==', start_index=19115)
Annotation(end_index=19212, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJoVVq6u4WpRNKkZ0vPl_zsDtrfofDRBpYSOjkpemi6-Fic1xefZeq-mtV07vWiDxI2CqPlcOwufbwNj35XEvYeYH1C2kpDnFKjUnFkulLPBUWbQLwA2y7Pw==', start_index=19203)
Annotation(end_index=19273, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcAfW5wwPKKM9COaanvXUKaLgLNJgCDemqegcL-rW2RraX-IFWqsRKZcK0piJ0csHkNIed0Cg5FwJHYmN4B_w0cKX2Q4Hq0NmNdVcuwqGidAfl3QHh0k5jq-RdcDfv6pTa65Hn8qi9VZOs59qX7PTNvTjYTtK4UY8F-YTuRO8wEEfFjRoJhJoBWUK__GlnnwchFsncXEJvkMsGuO4Jz6TGbBcmXb27', start_index=19264)
Annotation(end_index=19338, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE09e46ASoGSCFk7CHbw5-Nh6IPnWpbZ3vuDGxvQ2ZicCHqb0sBoFcf-ttA-SUn3k6hNDZRBHu7VwI4nbwdBjQZWm7abD3qVBMZgOlbU6dx_FNd1ozZfveeLtoo4QolVNngypZpWAqwJE5nMgcMZQ==', start_index=19329)
Annotation(end_index=19389, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiRFKgfm3B5mAR2kKvlKG2XPFL93tIBmqUa3xTzFJoTotOsxOW17VFCvXTBx7mZYZvDNFUvwbD6d5QPfFbGoI8Vx7-lPnGA3tcQrMtO3aN2LkNTJKtO8rFUeya_vuqUulVz9UbTFNLfYfy_xP2Y6EoZLsiu7u197I=', start_index=19380)
Annotation(end_index=19455, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkwqzRV5efvUluhDWRmZqV-AspyA-Flt9spSEuI-SFQArdgG19-dQ8h6kdD3O94crQ2s9rm8FoIhv9ec3DtxuIF6gbN7phYFPko5tYY2khYSgykACt_hAiJN22VcmAu2iorSDORd3Hsmoa2pYYwmOE', start_index=19445)
Annotation(end_index=19521, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcAfW5wwPKKM9COaanvXUKaLgLNJgCDemqegcL-rW2RraX-IFWqsRKZcK0piJ0csHkNIed0Cg5FwJHYmN4B_w0cKX2Q4Hq0NmNdVcuwqGidAfl3QHh0k5jq-RdcDfv6pTa65Hn8qi9VZOs59qX7PTNvTjYTtK4UY8F-YTuRO8wEEfFjRoJhJoBWUK__GlnnwchFsncXEJvkMsGuO4Jz6TGbBcmXb27', start_index=19512)
Annotation(end_index=19591, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-taEdFsjnsg3OE-yJ6RMA2AqAg-XLSKbKGVOsLYaQgpQ-CudYjMPHfwahf5ytT0I4070jHHXZr6IaBpTYcHj4Yyosyg1fTa6IskDwkkva9VxDXrVF5D30oeQ8j1pltiY=', start_index=19582)
Annotation(end_index=19655, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1GvTO5hHF7TWCpaEMv9pSEcxJe_KaciaJnTxcwYALg8lzXxqHzk2qvYJQJcW5-h-amwunoRD4IkRjNDrMJ4iTaL82U2ivs8PkJ-OpezBvVfSAY9K8IbPQOLv65h91-hif91DyGxH56nTul7qQOtv16LA0H4f3xvpjgzhsXy_xttT6LwwSQTykG2Ib5B7ye_X7t9BsSriTrQ5eVusorjdf-jHBEc_mPy-FUlKSVtYbiYPRXe9A05zUMuWCw1B2h8I=', start_index=19645)
Annotation(end_index=19729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFV3kJYHVr4t4YKdzjcWdIhvy8tTCvfaR5BHpPkmD_k9ozOhXnZ_rWZryZj3ZfD8fXKMBpQGQv-PmIvHZGhBHv-9CKpNCFnRwEFY21jYklavKbn2exK3cdUpAWK_gjPQ9GcHW9Hl6PUMl3kVaBSty1ZatRuJaYSKGduyabcYxDNAbHkzlsVfAOmF4xOgPI3CgJ6h8-hhU=', start_index=19720)
Annotation(end_index=19796, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMUNjr97BBRrQGG9QZz89PE4WoCsPPtQW8qcByHoz9sjyR7e_7-VHk6XCXdiyyCL6esBYW8wF30w9un_WgtUIMBg1AiMnzo_4K5Zq5ycbkQb67sNYG5DFdX6VdblEC8lI28TWVf_rBsOs31lNYzi6DBRRyQkgkhRtg5JtKFdYnupAyoozQrkjyolfjXZVVWWAhQColXlGXhf5K0HxvI5IRAppJMUATj-6NV9hPGiiGHGIWKoQdPl9JmaCjxTHQXkrC-vEIAurth1JSxpoY8dg=', start_index=19787)
Annotation(end_index=19893, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM1OJV3mBCBR191NzwI80egsLyrxg31NilmorUicG7kNEtqKv69F6hJjfIlViYZWWSfUhEyaJ0MMkN2M5gvBO9IvmA8vp2bNecQq5rmbPioRunZMvLaKCuHUD-IJZoc7L3Sz1Rd98=', start_index=19883)
Annotation(end_index=19939, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIh3ZmENpmybR1_HA3SwcwvlDte33tNppwpfTO8M_8ITkAvxa_fY4h4jeD7tkgWwQ_0B_3r9GTKcKZreDV9Z3U3CcGP3CgmdpIDRooEfaohCqKrRyE9g==', start_index=19929)
Annotation(end_index=20005, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFV3kJYHVr4t4YKdzjcWdIhvy8tTCvfaR5BHpPkmD_k9ozOhXnZ_rWZryZj3ZfD8fXKMBpQGQv-PmIvHZGhBHv-9CKpNCFnRwEFY21jYklavKbn2exK3cdUpAWK_gjPQ9GcHW9Hl6PUMl3kVaBSty1ZatRuJaYSKGduyabcYxDNAbHkzlsVfAOmF4xOgPI3CgJ6h8-hhU=', start_index=19996)

## Sources
