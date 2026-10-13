# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 70076fd7 | **Time:** 383.35s | **Cost:** $2.26803
--------------------------------------------------------------------------------

# How Path Selection Convergence Speed Changes with Network Scale Power-Laws Under Capacity Constraints

**Key Points**
*   **Scale-Free Acceleration:** In the absence of binding capacity constraints, path selection and information dissemination converge significantly faster in scale-free networks (where the degree distribution exponent $\gamma$ is typically between 2 and 3) compared to random networks. This is due to the "ultra-small-world" property, where the network diameter scales as $\ln \ln N$ rather than $\ln N$.
*   **The $\gamma = 2.5$ Regime Shift:** Research indicates a critical threshold around the power-law exponent $\gamma \approx 2.5$. For networks with $\gamma < 2.5$, the relaxation time for dynamic processes (like consensus or reaching a steady state) can become independent of the network size $N$, implying extremely rapid convergence. For $\gamma > 3$, dynamics resemble those of random networks.
*   **Capacity Bottlenecks:** Capacity constraints fundamentally alter this behavior. While scale-free topologies facilitate fast path discovery via hubs, these same hubs become congestion hotspots. When traffic demand exceeds a critical threshold $R_c$, the system undergoes a phase transition from free flow to congestion, preventing convergence to a stable efficient state.
*   **Algorithmic vs. Physical Convergence:** "Path selection convergence" encompasses both the algorithmic time to calculate routes (favored by scale-free structures) and the physical time for traffic flows to stabilize (hindered by capacity constraints on hubs).
*   **Routing Strategy Trade-off:** Standard Shortest Path (SP) routing minimizes topological distance but exacerbates hub congestion, lowering the capacity threshold. Efficient routing strategies that bypass hubs improve capacity and stability but may increase the topological path length and algorithmic convergence time.

---

## 1. Introduction

The efficiency of large-scale communication and transportation networks relies heavily on the speed at which path selection algorithms converge to stable routes and the ability of the network to handle traffic loads within capacity limits. Real-world networks, such as the Internet, the World Wide Web, and various social and biological systems, often exhibit a scale-free topology characterized by a power-law degree distribution $P(k) \sim k^{-\gamma}$. This report analyzes the complex relationship between path selection convergence speed, the power-law exponent $\gamma$, and network capacity constraints.

Path selection convergence refers to two distinct but related phenomena:
1.  **Algorithmic Convergence:** The time required for a routing protocol (e.g., BGP, OSPF, or distributed search) to discover stable paths and update routing tables following a topology change or initialization.
2.  **Dynamic Relaxation:** The time required for the distribution of traffic or information flow to reach a steady state (equilibrium) over the selected paths.

Capacity constraints introduce non-linearities into this system, creating phase transitions between free-flow and congested states. This report synthesizes theoretical physics models, network science, and telecommunications research to explain how these factors interact.

## 2. Network Topology and Power-Law Scaling

### 2.1 The Scale-Free Property
Scale-free networks are defined by the heterogeneity of their node degrees. The probability that a node has $k$ connections follows a power law:
\[ P(k) \sim k^{-\gamma} \]
where $\gamma$ is the degree exponent. For most real-world networks, $2 < \gamma < 3$ [cite: 1]. This distribution implies the existence of "hubs"—nodes with an exceptionally high number of connections—which act as bridges connecting different parts of the network.

### 2.2 The Ultra-Small-World Effect
The presence of hubs significantly reduces the average path length $L$ between nodes. In Erdős-Rényi (random) networks, the diameter scales logarithmically with network size ($L \sim \ln N$). In contrast, scale-free networks with $2 < \gamma < 3$ exhibit an "ultra-small-world" property where the diameter scales as:
\[ L \sim \ln \ln N \]
This topological feature suggests that, theoretically, path selection signals and search processes can traverse the network and converge much faster as the network scales, provided capacities are infinite [cite: 2, 3].

### 2.3 Critical Regimes of $\gamma$
The value of $\gamma$ dictates the structural and dynamical properties of the network:
*   **$\gamma \le 2$:** The mean degree diverges; these networks are extremely dense and rare in physical reality [cite: 4].
*   **$2 < \gamma < 3$:** The second moment of the degree distribution $\langle k^2 \rangle$ diverges in the infinite limit. This regime is associated with vanishing epidemic thresholds and ultra-fast spreading phenomena [cite: 5].
*   **$\gamma > 3$:** The network properties, including average path length and diffusion speeds, behave similarly to random networks [cite: 6].

## 3. Convergence Speed in the Absence of Congestion

When capacity constraints are negligible (free-flow regime), the convergence speed of path selection and dynamic processes is governed primarily by the network topology.

### 3.1 Algorithmic Convergence and Search Time
In distributed routing or search algorithms, the time to find a target or stabilize a route is often proportional to the network diameter or the average path length.
*   **Search Time Scaling:** Research on random walks and search strategies in scale-free networks shows that search time can be significantly reduced compared to regular lattices. For example, in small-world networks, search time scales as $N^{1/D(D+1)}$, but in scale-free networks, the presence of hubs allows for even faster, often logarithmic or sub-logarithmic, search times [cite: 7].
*   **Quantum Walk Convergence:** Studies on continuous-time quantum walks reveal that scale-free networks facilitate faster localization and coherence preservation compared to Erdős-Rényi networks. The relaxation time (lifetime of coherence) is higher, and the search dynamics rely on the shortest paths provided by hubs [cite: 8, 9].

### 3.2 Relaxation Time and the $\gamma = 2.5$ Threshold
A critical finding in the dynamics of scale-free networks is the dependence of relaxation time $\tau$ (the time to reach a steady state) on the exponent $\gamma$.
*   **Regime $\gamma < 2.5$:** Theoretical mean-field calculations and simulations of local majority-rule dynamics predict that when $\gamma$ drops below 2.5, the typical relaxation time changes from being proportional to $\ln N$ to being **independent of $N$**. This implies that for sufficiently heterogeneous networks, the system can converge to a consensus or steady state almost instantaneously, regardless of the network size [cite: 6, 10].
*   **Regime $\gamma > 2.5$:** As $\gamma$ increases, the heterogeneity decreases. For $\gamma > 3$, the relaxation time scales with system size similarly to random networks, typically $\tau \sim \ln N$ or power-law relations with $N$ depending on the specific dynamic [cite: 3, 6].

### 3.3 Epidemic Spreading and Information Diffusion
The convergence of spreading processes (which can be viewed as a form of path discovery) is extremely rapid in scale-free networks. For $\gamma < 3$, the characteristic time for an epidemic to spread vanishes ($\tau \to 0$) in the limit of large $N$ because the highly connected hubs become infected almost immediately and broadcast the "signal" to the rest of the network [cite: 5].

## 4. The Impact of Capacity Constraints

While scale-free topologies accelerate convergence topologically, they introduce severe vulnerabilities when node or link capacities are finite. Capacity constraints impose a maximum flow rate $C_i$ on nodes or edges.

### 4.1 The Phase Transition to Congestion
Traffic dynamics on complex networks exhibit a continuous phase transition from a **free-flow state** to a **congested state** controlled by the packet generation rate $R$.
*   **Free Flow ($R < R_c$):** The number of packets generated is balanced by the number delivered. The system reaches a steady state (converges) with constant average packet travel times.
*   **Congestion ($R > R_c$):** The packet generation rate exceeds the network's critical capacity $R_c$. Packets accumulate in queues, primarily at bottlenecks. The system fails to converge to a stationary distribution; instead, queue lengths grow indefinitely or until buffer overflow occurs [cite: 11, 12, 13, 14].

### 4.2 Hubs as Bottlenecks
In scale-free networks using Shortest Path (SP) routing, traffic load is distributed unevenly. The "betweenness centrality" of hubs is extremely high, meaning a disproportionate amount of traffic passes through them.
*   **Capacity Scaling:** If node capacity is uniform ($C_i = \text{const}$), hubs become congested at very low traffic generation rates, leading to a low critical threshold $R_c$.
*   **Degree-Dependent Capacity:** If capacity scales with degree ($C_i \sim k_i^\phi$), the network can handle higher loads. Research suggests that $R_c$ is maximized when capacity is allocated non-linearly with respect to degree, often requiring $\phi > 1$ to fully compensate for the load aggregation at hubs [cite: 12, 15].

### 4.3 Convergence Speed Under Constraints
Capacity constraints introduce a "friction" that counteracts the topological acceleration of scale-free networks.
*   **Critical Slowing Down:** As the traffic load $R$ approaches the critical threshold $R_c$, the relaxation time $\tau$ diverges. This is a hallmark of phase transitions. Even if the topology allows for fast traversal, the waiting time in queues dominates the total path duration [cite: 13, 16].
*   **Net Flow Constraints:** Algorithms that incorporate net flow capacity constraints (accounting for flow conservation and limits) have been observed to converge slower than those with simple constraints. The complexity of satisfying capacity limits while optimizing paths creates a harder optimization landscape [cite: 17].

## 5. Routing Strategies and Convergence Trade-offs

The convergence speed and capacity of the network are heavily influenced by the "path selection" strategy employed.

### 5.1 Shortest Path (SP) Routing
*   **Mechanism:** Packets follow the topological shortest path (min-hop).
*   **Convergence:** topologically fast (fewest hops), but leads to the lowest critical threshold $R_c$ in scale-free networks due to hub overloading.
*   **Outcome:** Under capacity constraints, SP routing causes the network to enter the congested phase early, effectively destroying convergence speed for high traffic loads [cite: 13, 18].

### 5.2 Efficient and Traffic-Aware Routing
*   **Mechanism:** Strategies that redistribute traffic away from hubs, such as Efficient Routing (ER) or dynamic routing based on queue lengths.
*   **Mechanism:** These algorithms often use a cost function $Cost \sim k^\beta$ or real-time congestion metrics. By setting $\beta > 0$, paths avoid high-degree nodes.
*   **Convergence:** These strategies increase the path length (topological distance) but significantly increase the network capacity $R_c$ (up to 30 times higher than SP) [cite: 18].
*   **Trade-off:** While the physical travel time might increase due to longer paths, the *effective* convergence to a delivered state is maintained at much higher loads where SP routing would fail completely. However, dynamic routing can introduce oscillations and slower algorithmic convergence if state information is delayed [cite: 19, 20].

### 5.3 Hierarchical and Heuristic Approaches
*   **Hierarchical Methods:** In hyper-dense networks, hierarchical resource allocation schemes have been shown to converge faster than distributed global learning algorithms as the network scales [cite: 21].
*   **Heuristics:** Algorithms like Ant Colony Optimization (ACO) or Particle Swarm Optimization (PSO) adapted for scale-free networks (SF-PSO) can balance convergence speed and solution quality. SF-PSO, for instance, uses the scale-free structure to disseminate information efficiently, preventing premature convergence to local optima while maintaining speed [cite: 22].

## 6. Specific Domain Insights

### 6.1 Internet Routing (BGP)
The Internet is a scale-free network at the Autonomous System (AS) level. BGP convergence is a major concern.
*   **Power-Law Impact:** The power-law topology implies a small diameter, which should aid convergence. However, the hierarchical structure and policy constraints (preferential routing) complicate this.
*   **Convergence Time:** BGP convergence is often delayed by path exploration and timer mechanisms (MRAI). Research shows that while the topology allows for fast paths, the protocol's handling of updates and the sheer scale of the routing table (capacity constraint of routers) are the limiting factors [cite: 23, 24].

### 6.2 Wireless and Sensor Networks
In wireless networks, capacity is limited by interference.
*   **Scaling Law:** Convergence speed of average consensus algorithms in interference-limited networks scales with $r^{2-d}$ (where $r$ is range, $d$ is dimension). Increasing connectivity (making it more "small-world") can actually degrade convergence speed due to increased interference (capacity constraint) [cite: 25].

## 7. Conclusion

The convergence speed of path selection in networks governed by power-law scaling is a tale of two regimes defined by capacity.

1.  **In the Infinite Capacity Limit:** The scale-free nature ($\gamma \in (2,3)$) acts as a powerful accelerator. The ultra-small diameter allows path selection and search algorithms to converge on timescales that grow very slowly with network size ($\ln \ln N$), or even become size-independent for $\gamma < 2.5$.
2.  **Under Capacity Constraints:** The hubs that facilitate this speed become the system's Achilles' heel. As traffic scales, these nodes hit capacity limits first, triggering a phase transition to congestion. Near this critical point, convergence slows down dramatically (critical slowing down). If the load exceeds capacity, convergence to a steady flow state is impossible.

Therefore, in realistic scenarios with capacity constraints, the "theoretical" speed advantage of scale-free networks is only realizable if the routing strategy is intelligent enough to bypass the very hubs that provide the topological advantage, or if the capacity of nodes is scaled super-linearly with their degree. Without these mitigations, the convergence speed advantage is negated by congestion bottlenecks.

## References
*   **[cite: 1]** Scale-free network definition and properties.
*   **[cite: 17]** Impact of capacity constraints on RSP algorithm convergence.
*   **[cite: 25]** Convergence speed in interference-limited wireless networks.
*   **[cite: 11, 12, 13, 14, 15]** Phase transitions, traffic capacity, and routing strategies in scale-free networks.
*   **[cite: 18, 26]** Comparison of Shortest Path vs. Efficient Routing strategies.
*   **[cite: 7]** Search time scaling in small-world/scale-free networks.
*   **[cite: 23, 24]** BGP convergence time and Internet topology.
*   **[cite: 21]** Convergence speed of hierarchical resource allocation.
*   **[cite: 22]** Particle Swarm Optimization with scale-free interactions.
*   **[cite: 6, 10]** Relaxation time independence of $N$ for $\gamma < 2.5$.
*   **[cite: 5]** Epidemic spreading characteristic time in scale-free networks.
*   **[cite: 9]** Quantum walk relaxation and coherence in scale-free networks.

**Sources:**
1. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4YjBunmIaQsXnUHjiTpJsavf2kMQMlgyLO0fa7oV52XVS8J76HFHSoMEE0q4WOkJ4R0p2AbP7BzKH53BUS7gBUDxDTKHnKv4jUVvNB7guKCt1DkAxTXJN-COna8Z8n-ADCmKF-xw=)
2. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERACBN9RrrYbu1i1K6WdoU5Dwbn7DamWdmXK28OCCd5WWy1ho4pPDm50EyvsFjPstcMPnNpE-i-vzgsNeteer7hgH--517_vkwmzt-Lu0Fqs4bgJ6T_yyjbkItWLwyPfVxc9tM5yCK)
3. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3eu_oA3cGRG8K59y9OIFXcrG4nHDIiBbl2HSKldLzxfL-Qqt72-Nz_3EpiwjhfcsqxAMp1MUJFz0o059RP2xd7Zl_JCqFJ4FqgCRqhlzvFhHesetzGw==)
4. [reddit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN21Qz9WVoP6lPmBOu6eV7--vYJZEc-hEmnpyjfcq6BhQmSRP0y5S0vnoxsfTjBXY7_zosAusfqtCL2ZkcJekRXNUzrAcucRpEEx_AgCz53Jc6iCXhDkXpQGZrjYQMOb-98PkWtM7TgsCiNBAq-E9AqY6dKbpfSFgYn8hjV32MeI25Vf0dUburXyFwD1V6WCEYev81xXeas3tk)
5. [networksciencebook.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQES5j9eaSWIgyzorHQpynZQWjocEQ6duEEd8bhxIB5Rex4vaxwgPigWAC4AFXJMgZn0TtqLP50g_RUnFomkTsCV_EeaTMoKE_uOvq7Y9pZZVMmSt7vfj3QAukRsl2kGQw==)
6. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_6pBzT3ZjoooJUidB6Tv8sRphgLa8Xflpe1svvYxIFZ0wsfqvCfPyHBNtAUEU2lki4j_u8rbENbPIltqeiYDflGKlTZgqK5eIM5btnmcikU_52RjsUCYsUBU-MQ==)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQt2SdLD-5uesZOUrSpzUdZSP4nBRwsZzH1ZJKSz43Du030Xp2eqdrgkxjo5AnifHiQmqDS77OTJCrC5hJvpSXz-ysXuQTi2qLp5LIFWCYsVAVpg7ud_JBuTMn-KW2iG__8nDEtkzlaGckn1d5eP34P0FCEZ6Y90CvIJAPUOimvyD9iRmQTOSOU9QqWmNmbUyrx7dxTuXLo4gf3RQatyVI440WPX8rAzdeoPK2ACvv89_TpYHNxDY=)
8. [phys-info.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPdCNQcOhsqFh7Rj77aRY00VR3dJkWoAIbk60wFeyK25nSfS3n4a4iLnwpGi8wZiuKCfFC_LdbGQUgXoIYf1yrHjgbMmfztVWqXPuT_C-7lNgds7APg7gpOjPxLjEoG4c5GAe0iCtZevL-ocNynkU8sJx6kHi7uh6eHwMSmAbpoxTPTCqXocQGR9_xvuyiw5IvCcx1HjQKJcnFan8u_br7GMy5BnUnL1Ddp5-yQxrvhqscZRpnrUxWf9ISDbeiJg==)
9. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyor3wLpS4L4KlkSo0t1sjSCByRafTlopmePK8fFrLxKGVlli0szPksUgcy9g4atIBTI44IipcUW_bkHOCIvqxJc4NPv7d6FhQ4WzpRVvnXqKjqDman4C7ng==)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGUjRPNvJUk4vkWMkr9crXnmM5hT4_0bSBmzzMJqp1T3RLVXHFoni7B2WNoRVn8a3wyIGZhB_gHi24VVttjX8b65KU__cKzf7M_lhq2_t4wB1Bz8_31xKkPhgX8g6a2o21mGW0a3CyMZtNiJe7fdcfCviLntp66_gITfjyerAPer6wRjs2Ns0hheavImeCbfH-mrjeYaFClE9JWm95a_ufSow32PjZTNwn)
11. [cdnsciencepub.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoaem390qM6vYGeP524tg6gZ8HfvFsiAuZiTt9IWwEZ1K91rZ5euApDLsaqNxZznbXZSWjwUHRr80skmhRMz6lbUkLgFwrj1kWIsyuxzU8O65KJs009ZO2YeCdXqKyAH-1fak=)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF79eRd49oIZrp5P7FxMWITzvHmqtUHJXUjYa1_-gJzv7G1lPgKGUDtUtZonCa2FFbNVUL2FryuDfSRdmbMWvhx6aotP9WqQONluY4qOGnMuWpXca110iobgojW2YpemV3cso3dyrGGfsGm3RMjO1mZy3ZjKaKX0avXjZrWT4Ep0exlviu67QxRzihUKHeNbeIOtjP1r__9LZQAkkpGeGCkNl3IKw==)
13. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq6klv68XyQxPAnHLt1QJK4DDYqUBV7SHRG7YH7UkeaDNpBDT6rg9oXRX878U671Im9eHe5k3Bq__ww1cfWo49RCogmukTUDKnF4aeZWrneMnYmp_oCZLEZcEWCyNb2r12H2PAB_j6YSG69ozZrbhhLnnJ9RReHzkq8J37XHenVK5Z_-P8NWYiXneAUmPGu1DMXCtffZTwi87H5uI=)
14. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJy-XA1C85EO1PqShUa4T3u7H_p51NC82SQCQbd7STRQ8QMMX8vwLW5U8yvzvJ6E9uYUEufzxY-W_baswwfwQWIcPoCw7PnXIdpEMs0mZGtyONJ2C5MlNiyOx2)
15. [bnu.edu.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGX75VHnVC3FYd4l0omN8oWATcqFT-eisvSG1v1JOjG8YJzI6Xh1koMwlga2M8iFbHfS863N_3hkKxnmQF9TsZhxytuJ6zTrijCcHDY2pN5CaA0aRklBI0T3nWNfTVlZJ0MGeRJfKYKfESfJUCJODUmrJwY_N-eYJ0vGluRM2e5yRCrI39uy8si2slCEc_tjF9qDdbJRhjyTtlns-vz5pSXQbfSMdUNg86uZMGJGHWP58E1EgCvRoFxsO7i2nTTsRQvZfawAYChDOK9sX6zZ-CqMg==)
16. [ias.ac.in](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5i6gf2PzIizKq1aU0AR2JuXnjj6R3Mtf5Kvqvuwz7PR5RcSn9UUjBLXqBqe4ZpFD-W7LHRCmCyVWp1P-xaSCs64SNrJW8Y0KQKoqr7PoTgPPS0npO0-XM2GFJVlXCXelzZwBer0o0ub9iYC3MLgaguu0=)
17. [uclouvain.be](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTZahLai1CWnjxoPyTzqr6MVq9qGebl-ABasiEpZbx785VViNB9aqUBlpzhK-Lq6kcXZx99Rke3V9nQVZqHHDN3AWgUPIkntEQZ0V-kz65tU0AI7C9J6N1LTsZ_4nXxNoO-bPp71s9t8FTvvBdgiGoba7jqdTrz6XNBIVrdf_zJmnOvN1FPJIBDcU=)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKLTfkHCL_e1bHKPZvsoVvlGAbx-GAKV1jbOolN_7BxZP-Qd2TLncBLt7sVEk6Vfy1ZM6U64h25zNxaSEpTOGAf30mAuZqYdX9opz8rqs50bscesk1S3r-CXfVPg8_bdiOtl-hJmGILCUqz1jwnJZlysAYxmJ1UlmLHZuggLqjqapZotn451eFDAT_knpE4pX5lJTL9SQjQYLGSOA0)
19. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTy_AWeakEXoLJ8YpmeH0RarpMJGuCNKm5ShoosPdoWyhGTjx7hNaXM2TnT3_YXrmhpMu4TDTpv31kwcwuVRuEMNFiE64ZpvV9BIYT2cPMHoozjBaKrpwR6MwNjLMqxYts0uBe-mOrMAPjm6Ivgr25u5HmOPDE4Dg6xXX3UBBa20MvK9qC4koB0gskWSqEAgRX8nq0Z7eSf2xJRi_NFcs=)
20. [ucl.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPN44P8r9e1rXj2rdOkFQAE4ggzL4RZkO1TadlGxbAQYQ-LgJV3DYBIdiEZbYnSyRCviACaYF5gES3f4OMxCFiY8PNAVs-E7CbXgE3Nqyu1h3z6LEZWjdpCzY8a8P9i4rx-JFXcGzaFskjar71m5i7ANE5UEOZwluYtG_BDbgu-6YPwWaItPJ5tQ==)
21. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcAZGF5t1JERsZfqm4xEMz1R9FLvQROzvhLoshIPyxSvsRgpXb4TXTP09jmn4MS26OQcvd64DGQ8qJtwj0Lg8PVrHYgZohxxAv4_hoBgPnKXJw1V3d3ceX3vpLiwJLwCBG0HeXnLMbnmBtPIxhYZHS0GAkWKa8V8dqdIa6y9ONonddDBRqft1TWYlCnhTDnIuMoR8acc6r2eDYsKbUW5cafPc=)
22. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_5THEpsSggpIDgKZZAjhKIp56JUSjAu64948tmRc9F-mIL2qLFxUZLImD11P-PLQ7y5eBLlrIbhWhbv5jwh3jflO2_Y-VjRIoVq5b6Dj4Cm7myVJyzJXSNYg9VFpb8dUpxFbMzDR95wMRxHLuUcjlsNEMjF4v5RakVwcUWRUV)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3Tw558nn0suSzuHemB8YU3QJlD8tcqwfF0aV7OSLfFOvokVUHFf2xQkd8x3K5vDaqCMXgtTOkl5ovGj2WmXfQtJukhbctakLZMEf7nyiJhphJruNgceGVEdpfJ6UM1wCkU7CZFzuavK1xWkIJaPuYkMOekc5gScYBE9Mx9m7L2gklxHrVyA==)
24. [sfu.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqyWS7ShFmZ0FGJKtR_VLvgu1LbR5t0Oidf7JOEL1Xh08A8qN8CMSKVvMoCwwD5S_XnPRnZ1_lFctE_2VxV5AN5miCnZOJ2FssDkadbMgrRK5M2WaTRFcCkNLfQBk8Bh4UezAB3yoGu3vu7GCQoUlB)
25. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4AFKXdeI0p9ZAnC8X_plDnWi5vyNFIH_-DydJ1KaDzsSldWwgon4FiN5ORL6R-JzkB7yMU7QOxwMzNsJV2SLThbKxWCtthbWemW2zU24vd5NUDfEC)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSagGaz9EgRr3654YbSDX3QWuwLxvReN9ofJD-j3Q0xHBbq7XH7WJsfsieZaGjP_ZFpS30iojcB_WF5U8frDEZK-vKstx68zmKBrgwLbiAcbQ2w6dvbZOm0IwoE-K4eriUbq5sY-TbQaEo8Vr9zYGG9DoMLI-a-VcKi33rSux3ClJVMS48l9tWDtohiTU9fewc5mCgS2xWoIA0qrxUeCehQTrEjSopyg==)


## Annotations
Annotation(end_index=3598, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4YjBunmIaQsXnUHjiTpJsavf2kMQMlgyLO0fa7oV52XVS8J76HFHSoMEE0q4WOkJ4R0p2AbP7BzKH53BUS7gBUDxDTKHnKv4jUVvNB7guKCt1DkAxTXJN-COna8Z8n-ADCmKF-xw=', start_index=3589)
Annotation(end_index=4370, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERACBN9RrrYbu1i1K6WdoU5Dwbn7DamWdmXK28OCCd5WWy1ho4pPDm50EyvsFjPstcMPnNpE-i-vzgsNeteer7hgH--517_vkwmzt-Lu0Fqs4bgJ6T_yyjbkItWLwyPfVxc9tM5yCK', start_index=4358)
Annotation(end_index=4370, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3eu_oA3cGRG8K59y9OIFXcrG4nHDIiBbl2HSKldLzxfL-Qqt72-Nz_3EpiwjhfcsqxAMp1MUJFz0o059RP2xd7Zl_JCqFJ4FqgCRqhlzvFhHesetzGw==', start_index=4358)
Annotation(end_index=4620, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN21Qz9WVoP6lPmBOu6eV7--vYJZEc-hEmnpyjfcq6BhQmSRP0y5S0vnoxsfTjBXY7_zosAusfqtCL2ZkcJekRXNUzrAcucRpEEx_AgCz53Jc6iCXhDkXpQGZrjYQMOb-98PkWtM7TgsCiNBAq-E9AqY6dKbpfSFgYn8hjV32MeI25Vf0dUburXyFwD1V6WCEYev81xXeas3tk', start_index=4611)
Annotation(end_index=4852, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQES5j9eaSWIgyzorHQpynZQWjocEQ6duEEd8bhxIB5Rex4vaxwgPigWAC4AFXJMgZn0TtqLP50g_RUnFomkTsCV_EeaTMoKE_uOvq7Y9pZZVMmSt7vfj3QAukRsl2kGQw==', start_index=4843)
Annotation(end_index=4997, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_6pBzT3ZjoooJUidB6Tv8sRphgLa8Xflpe1svvYxIFZ0wsfqvCfPyHBNtAUEU2lki4j_u8rbENbPIltqeiYDflGKlTZgqK5eIM5btnmcikU_52RjsUCYsUBU-MQ==', start_index=4988)
Annotation(end_index=5829, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQt2SdLD-5uesZOUrSpzUdZSP4nBRwsZzH1ZJKSz43Du030Xp2eqdrgkxjo5AnifHiQmqDS77OTJCrC5hJvpSXz-ysXuQTi2qLp5LIFWCYsVAVpg7ud_JBuTMn-KW2iG__8nDEtkzlaGckn1d5eP34P0FCEZ6Y90CvIJAPUOimvyD9iRmQTOSOU9QqWmNmbUyrx7dxTuXLo4gf3RQatyVI440WPX8rAzdeoPK2ACvv89_TpYHNxDY=', start_index=5820)
Annotation(end_index=6167, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPdCNQcOhsqFh7Rj77aRY00VR3dJkWoAIbk60wFeyK25nSfS3n4a4iLnwpGi8wZiuKCfFC_LdbGQUgXoIYf1yrHjgbMmfztVWqXPuT_C-7lNgds7APg7gpOjPxLjEoG4c5GAe0iCtZevL-ocNynkU8sJx6kHi7uh6eHwMSmAbpoxTPTCqXocQGR9_xvuyiw5IvCcx1HjQKJcnFan8u_br7GMy5BnUnL1Ddp5-yQxrvhqscZRpnrUxWf9ISDbeiJg==', start_index=6155)
Annotation(end_index=6167, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyor3wLpS4L4KlkSo0t1sjSCByRafTlopmePK8fFrLxKGVlli0szPksUgcy9g4atIBTI44IipcUW_bkHOCIvqxJc4NPv7d6FhQ4WzpRVvnXqKjqDman4C7ng==', start_index=6155)
Annotation(end_index=6835, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_6pBzT3ZjoooJUidB6Tv8sRphgLa8Xflpe1svvYxIFZ0wsfqvCfPyHBNtAUEU2lki4j_u8rbENbPIltqeiYDflGKlTZgqK5eIM5btnmcikU_52RjsUCYsUBU-MQ==', start_index=6822)
Annotation(end_index=6835, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGUjRPNvJUk4vkWMkr9crXnmM5hT4_0bSBmzzMJqp1T3RLVXHFoni7B2WNoRVn8a3wyIGZhB_gHi24VVttjX8b65KU__cKzf7M_lhq2_t4wB1Bz8_31xKkPhgX8g6a2o21mGW0a3CyMZtNiJe7fdcfCviLntp66_gITfjyerAPer6wRjs2Ns0hheavImeCbfH-mrjeYaFClE9JWm95a_ufSow32PjZTNwn', start_index=6822)
Annotation(end_index=7118, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3eu_oA3cGRG8K59y9OIFXcrG4nHDIiBbl2HSKldLzxfL-Qqt72-Nz_3EpiwjhfcsqxAMp1MUJFz0o059RP2xd7Zl_JCqFJ4FqgCRqhlzvFhHesetzGw==', start_index=7106)
Annotation(end_index=7118, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_6pBzT3ZjoooJUidB6Tv8sRphgLa8Xflpe1svvYxIFZ0wsfqvCfPyHBNtAUEU2lki4j_u8rbENbPIltqeiYDflGKlTZgqK5eIM5btnmcikU_52RjsUCYsUBU-MQ==', start_index=7106)
Annotation(end_index=7556, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQES5j9eaSWIgyzorHQpynZQWjocEQ6duEEd8bhxIB5Rex4vaxwgPigWAC4AFXJMgZn0TtqLP50g_RUnFomkTsCV_EeaTMoKE_uOvq7Y9pZZVMmSt7vfj3QAukRsl2kGQw==', start_index=7547)
Annotation(end_index=8541, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF79eRd49oIZrp5P7FxMWITzvHmqtUHJXUjYa1_-gJzv7G1lPgKGUDtUtZonCa2FFbNVUL2FryuDfSRdmbMWvhx6aotP9WqQONluY4qOGnMuWpXca110iobgojW2YpemV3cso3dyrGGfsGm3RMjO1mZy3ZjKaKX0avXjZrWT4Ep0exlviu67QxRzihUKHeNbeIOtjP1r__9LZQAkkpGeGCkNl3IKw==', start_index=8519)
Annotation(end_index=8541, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoaem390qM6vYGeP524tg6gZ8HfvFsiAuZiTt9IWwEZ1K91rZ5euApDLsaqNxZznbXZSWjwUHRr80skmhRMz6lbUkLgFwrj1kWIsyuxzU8O65KJs009ZO2YeCdXqKyAH-1fak=', start_index=8519)
Annotation(end_index=8541, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJy-XA1C85EO1PqShUa4T3u7H_p51NC82SQCQbd7STRQ8QMMX8vwLW5U8yvzvJ6E9uYUEufzxY-W_baswwfwQWIcPoCw7PnXIdpEMs0mZGtyONJ2C5MlNiyOx2', start_index=8519)
Annotation(end_index=8541, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq6klv68XyQxPAnHLt1QJK4DDYqUBV7SHRG7YH7UkeaDNpBDT6rg9oXRX878U671Im9eHe5k3Bq__ww1cfWo49RCogmukTUDKnF4aeZWrneMnYmp_oCZLEZcEWCyNb2r12H2PAB_j6YSG69ozZrbhhLnnJ9RReHzkq8J37XHenVK5Z_-P8NWYiXneAUmPGu1DMXCtffZTwi87H5uI=', start_index=8519)
Annotation(end_index=9296, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF79eRd49oIZrp5P7FxMWITzvHmqtUHJXUjYa1_-gJzv7G1lPgKGUDtUtZonCa2FFbNVUL2FryuDfSRdmbMWvhx6aotP9WqQONluY4qOGnMuWpXca110iobgojW2YpemV3cso3dyrGGfsGm3RMjO1mZy3ZjKaKX0avXjZrWT4Ep0exlviu67QxRzihUKHeNbeIOtjP1r__9LZQAkkpGeGCkNl3IKw==', start_index=9282)
Annotation(end_index=9296, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGX75VHnVC3FYd4l0omN8oWATcqFT-eisvSG1v1JOjG8YJzI6Xh1koMwlga2M8iFbHfS863N_3hkKxnmQF9TsZhxytuJ6zTrijCcHDY2pN5CaA0aRklBI0T3nWNfTVlZJ0MGeRJfKYKfESfJUCJODUmrJwY_N-eYJ0vGluRM2e5yRCrI39uy8si2slCEc_tjF9qDdbJRhjyTtlns-vz5pSXQbfSMdUNg86uZMGJGHWP58E1EgCvRoFxsO7i2nTTsRQvZfawAYChDOK9sX6zZ-CqMg==', start_index=9282)
Annotation(end_index=9754, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5i6gf2PzIizKq1aU0AR2JuXnjj6R3Mtf5Kvqvuwz7PR5RcSn9UUjBLXqBqe4ZpFD-W7LHRCmCyVWp1P-xaSCs64SNrJW8Y0KQKoqr7PoTgPPS0npO0-XM2GFJVlXCXelzZwBer0o0ub9iYC3MLgaguu0=', start_index=9740)
Annotation(end_index=9754, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq6klv68XyQxPAnHLt1QJK4DDYqUBV7SHRG7YH7UkeaDNpBDT6rg9oXRX878U671Im9eHe5k3Bq__ww1cfWo49RCogmukTUDKnF4aeZWrneMnYmp_oCZLEZcEWCyNb2r12H2PAB_j6YSG69ozZrbhhLnnJ9RReHzkq8J37XHenVK5Z_-P8NWYiXneAUmPGu1DMXCtffZTwi87H5uI=', start_index=9740)
Annotation(end_index=10082, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTZahLai1CWnjxoPyTzqr6MVq9qGebl-ABasiEpZbx785VViNB9aqUBlpzhK-Lq6kcXZx99Rke3V9nQVZqHHDN3AWgUPIkntEQZ0V-kz65tU0AI7C9J6N1LTsZ_4nXxNoO-bPp71s9t8FTvvBdgiGoba7jqdTrz6XNBIVrdf_zJmnOvN1FPJIBDcU=', start_index=10072)
Annotation(end_index=10705, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKLTfkHCL_e1bHKPZvsoVvlGAbx-GAKV1jbOolN_7BxZP-Qd2TLncBLt7sVEk6Vfy1ZM6U64h25zNxaSEpTOGAf30mAuZqYdX9opz8rqs50bscesk1S3r-CXfVPg8_bdiOtl-hJmGILCUqz1jwnJZlysAYxmJ1UlmLHZuggLqjqapZotn451eFDAT_knpE4pX5lJTL9SQjQYLGSOA0', start_index=10691)
Annotation(end_index=10705, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq6klv68XyQxPAnHLt1QJK4DDYqUBV7SHRG7YH7UkeaDNpBDT6rg9oXRX878U671Im9eHe5k3Bq__ww1cfWo49RCogmukTUDKnF4aeZWrneMnYmp_oCZLEZcEWCyNb2r12H2PAB_j6YSG69ozZrbhhLnnJ9RReHzkq8J37XHenVK5Z_-P8NWYiXneAUmPGu1DMXCtffZTwi87H5uI=', start_index=10691)
Annotation(end_index=11250, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKLTfkHCL_e1bHKPZvsoVvlGAbx-GAKV1jbOolN_7BxZP-Qd2TLncBLt7sVEk6Vfy1ZM6U64h25zNxaSEpTOGAf30mAuZqYdX9opz8rqs50bscesk1S3r-CXfVPg8_bdiOtl-hJmGILCUqz1jwnJZlysAYxmJ1UlmLHZuggLqjqapZotn451eFDAT_knpE4pX5lJTL9SQjQYLGSOA0', start_index=11240)
Annotation(end_index=11595, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPN44P8r9e1rXj2rdOkFQAE4ggzL4RZkO1TadlGxbAQYQ-LgJV3DYBIdiEZbYnSyRCviACaYF5gES3f4OMxCFiY8PNAVs-E7CbXgE3Nqyu1h3z6LEZWjdpCzY8a8P9i4rx-JFXcGzaFskjar71m5i7ANE5UEOZwluYtG_BDbgu-6YPwWaItPJ5tQ==', start_index=11581)
Annotation(end_index=11595, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTy_AWeakEXoLJ8YpmeH0RarpMJGuCNKm5ShoosPdoWyhGTjx7hNaXM2TnT3_YXrmhpMu4TDTpv31kwcwuVRuEMNFiE64ZpvV9BIYT2cPMHoozjBaKrpwR6MwNjLMqxYts0uBe-mOrMAPjm6Ivgr25u5HmOPDE4Dg6xXX3UBBa20MvK9qC4koB0gskWSqEAgRX8nq0Z7eSf2xJRi_NFcs=', start_index=11581)
Annotation(end_index=11851, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcAZGF5t1JERsZfqm4xEMz1R9FLvQROzvhLoshIPyxSvsRgpXb4TXTP09jmn4MS26OQcvd64DGQ8qJtwj0Lg8PVrHYgZohxxAv4_hoBgPnKXJw1V3d3ceX3vpLiwJLwCBG0HeXnLMbnmBtPIxhYZHS0GAkWKa8V8dqdIa6y9ONonddDBRqft1TWYlCnhTDnIuMoR8acc6r2eDYsKbUW5cafPc=', start_index=11841)
Annotation(end_index=12224, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_5THEpsSggpIDgKZZAjhKIp56JUSjAu64948tmRc9F-mIL2qLFxUZLImD11P-PLQ7y5eBLlrIbhWhbv5jwh3jflO2_Y-VjRIoVq5b6Dj4Cm7myVJyzJXSNYg9VFpb8dUpxFbMzDR95wMRxHLuUcjlsNEMjF4v5RakVwcUWRUV', start_index=12214)
Annotation(end_index=12922, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3Tw558nn0suSzuHemB8YU3QJlD8tcqwfF0aV7OSLfFOvokVUHFf2xQkd8x3K5vDaqCMXgtTOkl5ovGj2WmXfQtJukhbctakLZMEf7nyiJhphJruNgceGVEdpfJ6UM1wCkU7CZFzuavK1xWkIJaPuYkMOekc5gScYBE9Mx9m7L2gklxHrVyA==', start_index=12908)
Annotation(end_index=12922, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqyWS7ShFmZ0FGJKtR_VLvgu1LbR5t0Oidf7JOEL1Xh08A8qN8CMSKVvMoCwwD5S_XnPRnZ1_lFctE_2VxV5AN5miCnZOJ2FssDkadbMgrRK5M2WaTRFcCkNLfQBk8Bh4UezAB3yoGu3vu7GCQoUlB', start_index=12908)
Annotation(end_index=13343, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4AFKXdeI0p9ZAnC8X_plDnWi5vyNFIH_-DydJ1KaDzsSldWwgon4FiN5ORL6R-JzkB7yMU7QOxwMzNsJV2SLThbKxWCtthbWemW2zU24vd5NUDfEC', start_index=13333)
Annotation(end_index=14635, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4YjBunmIaQsXnUHjiTpJsavf2kMQMlgyLO0fa7oV52XVS8J76HFHSoMEE0q4WOkJ4R0p2AbP7BzKH53BUS7gBUDxDTKHnKv4jUVvNB7guKCt1DkAxTXJN-COna8Z8n-ADCmKF-xw=', start_index=14626)
Annotation(end_index=14700, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTZahLai1CWnjxoPyTzqr6MVq9qGebl-ABasiEpZbx785VViNB9aqUBlpzhK-Lq6kcXZx99Rke3V9nQVZqHHDN3AWgUPIkntEQZ0V-kz65tU0AI7C9J6N1LTsZ_4nXxNoO-bPp71s9t8FTvvBdgiGoba7jqdTrz6XNBIVrdf_zJmnOvN1FPJIBDcU=', start_index=14690)
Annotation(end_index=14780, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4AFKXdeI0p9ZAnC8X_plDnWi5vyNFIH_-DydJ1KaDzsSldWwgon4FiN5ORL6R-JzkB7yMU7QOxwMzNsJV2SLThbKxWCtthbWemW2zU24vd5NUDfEC', start_index=14770)
Annotation(end_index=14876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF79eRd49oIZrp5P7FxMWITzvHmqtUHJXUjYa1_-gJzv7G1lPgKGUDtUtZonCa2FFbNVUL2FryuDfSRdmbMWvhx6aotP9WqQONluY4qOGnMuWpXca110iobgojW2YpemV3cso3dyrGGfsGm3RMjO1mZy3ZjKaKX0avXjZrWT4Ep0exlviu67QxRzihUKHeNbeIOtjP1r__9LZQAkkpGeGCkNl3IKw==', start_index=14850)
Annotation(end_index=14876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGX75VHnVC3FYd4l0omN8oWATcqFT-eisvSG1v1JOjG8YJzI6Xh1koMwlga2M8iFbHfS863N_3hkKxnmQF9TsZhxytuJ6zTrijCcHDY2pN5CaA0aRklBI0T3nWNfTVlZJ0MGeRJfKYKfESfJUCJODUmrJwY_N-eYJ0vGluRM2e5yRCrI39uy8si2slCEc_tjF9qDdbJRhjyTtlns-vz5pSXQbfSMdUNg86uZMGJGHWP58E1EgCvRoFxsO7i2nTTsRQvZfawAYChDOK9sX6zZ-CqMg==', start_index=14850)
Annotation(end_index=14876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoaem390qM6vYGeP524tg6gZ8HfvFsiAuZiTt9IWwEZ1K91rZ5euApDLsaqNxZznbXZSWjwUHRr80skmhRMz6lbUkLgFwrj1kWIsyuxzU8O65KJs009ZO2YeCdXqKyAH-1fak=', start_index=14850)
Annotation(end_index=14876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJy-XA1C85EO1PqShUa4T3u7H_p51NC82SQCQbd7STRQ8QMMX8vwLW5U8yvzvJ6E9uYUEufzxY-W_baswwfwQWIcPoCw7PnXIdpEMs0mZGtyONJ2C5MlNiyOx2', start_index=14850)
Annotation(end_index=14876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq6klv68XyQxPAnHLt1QJK4DDYqUBV7SHRG7YH7UkeaDNpBDT6rg9oXRX878U671Im9eHe5k3Bq__ww1cfWo49RCogmukTUDKnF4aeZWrneMnYmp_oCZLEZcEWCyNb2r12H2PAB_j6YSG69ozZrbhhLnnJ9RReHzkq8J37XHenVK5Z_-P8NWYiXneAUmPGu1DMXCtffZTwi87H5uI=', start_index=14850)
Annotation(end_index=14983, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKLTfkHCL_e1bHKPZvsoVvlGAbx-GAKV1jbOolN_7BxZP-Qd2TLncBLt7sVEk6Vfy1ZM6U64h25zNxaSEpTOGAf30mAuZqYdX9opz8rqs50bscesk1S3r-CXfVPg8_bdiOtl-hJmGILCUqz1jwnJZlysAYxmJ1UlmLHZuggLqjqapZotn451eFDAT_knpE4pX5lJTL9SQjQYLGSOA0', start_index=14969)
Annotation(end_index=14983, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSagGaz9EgRr3654YbSDX3QWuwLxvReN9ofJD-j3Q0xHBbq7XH7WJsfsieZaGjP_ZFpS30iojcB_WF5U8frDEZK-vKstx68zmKBrgwLbiAcbQ2w6dvbZOm0IwoE-K4eriUbq5sY-TbQaEo8Vr9zYGG9DoMLI-a-VcKi33rSux3ClJVMS48l9tWDtohiTU9fewc5mCgS2xWoIA0qrxUeCehQTrEjSopyg==', start_index=14969)
Annotation(end_index=15063, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQt2SdLD-5uesZOUrSpzUdZSP4nBRwsZzH1ZJKSz43Du030Xp2eqdrgkxjo5AnifHiQmqDS77OTJCrC5hJvpSXz-ysXuQTi2qLp5LIFWCYsVAVpg7ud_JBuTMn-KW2iG__8nDEtkzlaGckn1d5eP34P0FCEZ6Y90CvIJAPUOimvyD9iRmQTOSOU9QqWmNmbUyrx7dxTuXLo4gf3RQatyVI440WPX8rAzdeoPK2ACvv89_TpYHNxDY=', start_index=15054)
Annotation(end_index=15142, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3Tw558nn0suSzuHemB8YU3QJlD8tcqwfF0aV7OSLfFOvokVUHFf2xQkd8x3K5vDaqCMXgtTOkl5ovGj2WmXfQtJukhbctakLZMEf7nyiJhphJruNgceGVEdpfJ6UM1wCkU7CZFzuavK1xWkIJaPuYkMOekc5gScYBE9Mx9m7L2gklxHrVyA==', start_index=15128)
Annotation(end_index=15142, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqyWS7ShFmZ0FGJKtR_VLvgu1LbR5t0Oidf7JOEL1Xh08A8qN8CMSKVvMoCwwD5S_XnPRnZ1_lFctE_2VxV5AN5miCnZOJ2FssDkadbMgrRK5M2WaTRFcCkNLfQBk8Bh4UezAB3yoGu3vu7GCQoUlB', start_index=15128)
Annotation(end_index=15205, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcAZGF5t1JERsZfqm4xEMz1R9FLvQROzvhLoshIPyxSvsRgpXb4TXTP09jmn4MS26OQcvd64DGQ8qJtwj0Lg8PVrHYgZohxxAv4_hoBgPnKXJw1V3d3ceX3vpLiwJLwCBG0HeXnLMbnmBtPIxhYZHS0GAkWKa8V8dqdIa6y9ONonddDBRqft1TWYlCnhTDnIuMoR8acc6r2eDYsKbUW5cafPc=', start_index=15195)
Annotation(end_index=15279, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_5THEpsSggpIDgKZZAjhKIp56JUSjAu64948tmRc9F-mIL2qLFxUZLImD11P-PLQ7y5eBLlrIbhWhbv5jwh3jflO2_Y-VjRIoVq5b6Dj4Cm7myVJyzJXSNYg9VFpb8dUpxFbMzDR95wMRxHLuUcjlsNEMjF4v5RakVwcUWRUV', start_index=15269)
Annotation(end_index=15359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_6pBzT3ZjoooJUidB6Tv8sRphgLa8Xflpe1svvYxIFZ0wsfqvCfPyHBNtAUEU2lki4j_u8rbENbPIltqeiYDflGKlTZgqK5eIM5btnmcikU_52RjsUCYsUBU-MQ==', start_index=15346)
Annotation(end_index=15359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGUjRPNvJUk4vkWMkr9crXnmM5hT4_0bSBmzzMJqp1T3RLVXHFoni7B2WNoRVn8a3wyIGZhB_gHi24VVttjX8b65KU__cKzf7M_lhq2_t4wB1Bz8_31xKkPhgX8g6a2o21mGW0a3CyMZtNiJe7fdcfCviLntp66_gITfjyerAPer6wRjs2Ns0hheavImeCbfH-mrjeYaFClE9JWm95a_ufSow32PjZTNwn', start_index=15346)
Annotation(end_index=15433, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQES5j9eaSWIgyzorHQpynZQWjocEQ6duEEd8bhxIB5Rex4vaxwgPigWAC4AFXJMgZn0TtqLP50g_RUnFomkTsCV_EeaTMoKE_uOvq7Y9pZZVMmSt7vfj3QAukRsl2kGQw==', start_index=15424)
Annotation(end_index=15514, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyor3wLpS4L4KlkSo0t1sjSCByRafTlopmePK8fFrLxKGVlli0szPksUgcy9g4atIBTI44IipcUW_bkHOCIvqxJc4NPv7d6FhQ4WzpRVvnXqKjqDman4C7ng==', start_index=15505)

## Sources
