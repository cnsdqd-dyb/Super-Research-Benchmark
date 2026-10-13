# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** ac2e0e4a | **Time:** 269.22s | **Cost:** $1.05107
--------------------------------------------------------------------------------

# Comprehensive Analysis of Control Plane Mechanisms for Balancing Global View and Latency in SDN Traffic Engineering

### Key Points
*   **The Core Mechanism:** The primary architectural mechanism balancing global visibility with implementation latency is the **Hierarchical Control Plane**, exemplified by frameworks such as **Kandoo**. This approach stratifies the control plane into local controllers (handling frequent, latency-sensitive events) and a root controller (handling rare, network-wide events requiring a global view).
*   **The Trade-off:** A strictly centralized control plane offers a perfect global view for optimal Traffic Engineering (TE) but suffers from scalability bottlenecks and high latency. Conversely, a flat distributed control plane improves latency but incurs significant synchronization overhead to maintain a consistent global view.
*   **Consistency vs. Latency:** The balance is further managed through **consistency models** within distributed controllers. Systems must choose between strong consistency (high latency, accurate global view) and eventual consistency (low latency, potential temporary state inaccuracies), often utilizing East-West interfaces for state synchronization.
*   **Traffic Engineering Implications:** Effective TE relies on the global view to prevent congestion and optimize routing. Hierarchical mechanisms allow "elephant flows" (high bandwidth, requiring global optimization) to be managed by the root controller, while "mice flows" (short-lived, latency-sensitive) are offloaded to local controllers.

### Introduction to the SDN Control Plane Dilemma
Software-Defined Networking (SDN) fundamentally reshapes network architecture by decoupling the **control plane** (decision-making logic) from the **data plane** (packet forwarding hardware) [cite: 1, 2]. This separation promises a logically centralized "brain" capable of programming the network with a holistic, global view, enabling sophisticated Traffic Engineering (TE) that traditional distributed protocols cannot easily achieve [cite: 3, 4]. However, this centralization introduces a critical tension: the latency required to transmit state information from distributed switches to a central controller—and subsequent flow rules back to the switches—can degrade performance, particularly in large-scale or geographically dispersed networks [cite: 5].

To resolve this, the academic and industrial communities have developed distributed and hierarchical control plane architectures. These mechanisms attempt to balance the **global view** necessary for optimal resource allocation with the **low latency** required for reactive network operations. This report provides an exhaustive analysis of these mechanisms, focusing on hierarchical designs, consistency protocols, and their specific applications in Traffic Engineering.

---

## 1. The Architectural Imperative: Global View vs. Latency

The defining characteristic of SDN is the centralization of control logic, which provides a **global view** of the network topology, resource utilization, and traffic patterns [cite: 6, 7]. This global view is indispensable for advanced Traffic Engineering (TE), allowing operators to optimize paths, balance loads, and enforce security policies more effectively than traditional hop-by-hop routing protocols [cite: 8, 9].

### 1.1 The Necessity of Global View for Traffic Engineering
In traditional networking, routers make autonomous decisions based on limited local knowledge, often leading to suboptimal routing or "race conditions" where multiple routers compete for the same bandwidth [cite: 10]. SDN addresses this by enabling a central entity to compute paths based on the complete state of the network.
*   **Optimization:** A global view allows the controller to detect congestion on a network-wide scale and reroute traffic proactively, ensuring high utilization of links without saturation [cite: 11, 12].
*   **Policy Enforcement:** Security and QoS policies can be applied consistently across the entire infrastructure, rather than configuring individual devices [cite: 3].

### 1.2 The Latency Challenge in Centralized Architectures
While logically centralized control is beneficial, implementing it via a single physical controller creates a bottleneck. As the network scales, the volume of control traffic (Packet-In messages, statistics collection) increases, leading to processing delays and queuing at the controller [cite: 1, 13].
*   **Inbound Latency:** The time taken for a switch to notify the controller of a new flow or event. Measurements indicate that generating packet-in messages can incur significant delays (e.g., ~8ms per packet on certain hardware), which is exacerbated when the controller is under load [cite: 5].
*   **Outbound Latency:** The time required for the controller to compute a decision and install flow rules (Flow-Mod) back into the switch. This round-trip time (RTT) directly impacts the flow setup time and the responsiveness of TE algorithms [cite: 5].

Consequently, a purely centralized physical architecture fails to meet the low-latency requirements of modern applications (e.g., 5G, industrial IoT), necessitating a shift toward distributed control plane mechanisms [cite: 14, 15].

---

## 2. Distributed Control Plane Architectures

To mitigate the latency and scalability limitations of a single controller, the control plane is often distributed across multiple physical devices while maintaining a logically centralized view. This distribution introduces the challenge of **state consistency**: ensuring all controllers share the same view of the network [cite: 14, 16].

### 2.1 Flat Distributed Architectures
In a flat distributed architecture (e.g., ONOS, OpenDaylight clustering), multiple controllers operate as peers, each managing a distinct domain or subset of switches [cite: 17, 18]. They communicate via **East-West interfaces** to synchronize network state.
*   **Latency Reduction:** By placing controllers physically closer to the switches they manage, the propagation latency for control messages is reduced [cite: 11, 19].
*   **Synchronization Overhead:** To maintain a global view, these controllers must constantly exchange state updates. Research indicates that as the number of controllers and the size of the network increase, the inter-controller traffic grows drastically, potentially negating the benefits of distribution [cite: 1, 18].

### 2.2 The Consistency-Latency Trade-off
The mechanism of balancing global view and latency in flat architectures is governed by the **CAP theorem** (Consistency, Availability, Partition Tolerance). SDN controllers must choose between:
*   **Strong Consistency:** All controllers see the same data at the same time. This requires complex consensus protocols (e.g., Paxos, Raft), which introduce high latency due to the need for coordination before committing changes [cite: 16, 20].
*   **Eventual Consistency:** Updates are propagated asynchronously. This offers low latency and high availability but risks temporary inconsistencies, such as routing loops or conflicting TE decisions, because controllers may operate on outdated global views [cite: 20].

---

## 3. The Hierarchical Control Plane: The Primary Balancing Mechanism

The most effective mechanism identified in the literature for balancing the global view with latency is the **Hierarchical Control Plane**. This architecture explicitly differentiates between "local" and "global" network events, assigning them to different layers of the control hierarchy.

### 3.1 The Kandoo Framework
**Kandoo** is the seminal framework representing this hierarchical approach. It addresses the scalability and latency issues by creating a two-tier control plane [cite: 21, 22, 23].
*   **Local Controllers (Bottom Tier):** These controllers are deployed close to the data plane (switches). They handle **frequent, local events** that do not require a network-wide view, such as elephant flow detection or local port status changes. They have no interconnection with each other and possess only a partial view of the network [cite: 22, 24].
*   **Root Controller (Top Tier):** This logically centralized controller maintains the **global network state**. It handles **rare, non-local events** that require complex decision-making, such as network-wide routing or inter-domain Traffic Engineering. The local controllers act as proxies, filtering frequent events and forwarding only significant state changes to the root [cite: 21, 22].

**Mechanism of Balance:**
1.  **Latency Reduction:** By processing frequent events (which constitute the vast majority of control traffic) at the local layer, Kandoo drastically reduces the round-trip time for these operations. The local controllers effectively shield the root controller from high-volume load [cite: 24, 25].
2.  **Global View Preservation:** The root controller retains authority over network-wide policies. Because it is relieved of the processing burden of trivial events, it can dedicate resources to computing optimal TE paths and maintaining the global topology view without becoming a bottleneck [cite: 21, 22].

### 3.2 Hierarchical Traffic Engineering
In hierarchical systems like **Orion** or **Kandoo**, Traffic Engineering is split based on the scope of the flow.
*   **Intra-domain/Local TE:** Local controllers manage traffic within their specific domain or switch group. This allows for immediate reaction to local link failures or congestion without waiting for the root controller [cite: 21, 26].
*   **Inter-domain/Global TE:** The root controller aggregates topology information (often abstracted) from local controllers to compute end-to-end paths across domains. This ensures that long-distance flows are optimized globally, preventing suboptimal routing that might occur if local controllers acted in isolation [cite: 24, 27].

This separation allows the network to achieve **low latency** for the majority of operations while preserving the **global view** for decisions where it matters most.

---

## 4. Mechanisms for Traffic Engineering (TE) Optimization

Traffic Engineering in SDN revolves on optimizing the performance of data flows, minimizing congestion, and maximizing resource utilization. The control plane architecture dictates how effectively these goals are met.

### 4.1 Elephant vs. Mice Flow Management
A critical TE mechanism enabled by hierarchical control planes is the differentiation between **Elephant flows** (long-lived, high-bandwidth) and **Mice flows** (short-lived, low-bandwidth) [cite: 28, 29].
*   **Mice Flows:** These are numerous and latency-sensitive. In a hierarchical architecture, local controllers can process these flows immediately, installing forwarding rules without consulting the root controller. This minimizes flow setup latency [cite: 23].
*   **Elephant Flows:** These consume significant bandwidth and can cause congestion. The local controller detects these flows and delegates their management to the root controller. The root controller, utilizing its global view, computes an optimal path that avoids congested links, effectively balancing the load across the network [cite: 23, 29].

### 4.2 Load Balancing and Path Selection
SDN controllers utilize the global view to implement sophisticated load balancing algorithms (e.g., ECMP, dynamic path optimization) [cite: 11, 30].
*   **Global Optimization:** The controller monitors link utilization across the entire network. When a link approaches saturation, the controller recalculates paths for specific flows to shift traffic to underutilized links [cite: 11].
*   **Latency Considerations:** Calculating these paths takes time. To balance this, some architectures employ **proactive** flow rule installation (pre-calculating backup paths) rather than **reactive** installation (waiting for a packet-in event). This reduces the real-time latency experienced by the traffic [cite: 31, 32].

### 4.3 Abstraction and Topology Aggregation
To maintain a global view without overwhelming the root controller with data (which would induce latency), hierarchical systems use **topology abstraction**. Local controllers aggregate the state of their domain and present a simplified view (e.g., a single logical node or a graph with aggregated link metrics) to the root controller [cite: 24, 27].
*   **Mechanism:** This reduces the volume of state synchronization traffic (East-West or South-North) required. The root controller can make global routing decisions based on this abstracted view, balancing the granularity of the global view with the speed of data processing [cite: 33].

---

## 5. Latency Analysis in Control Plane Implementations

Understanding the specific sources of latency is crucial to appreciating how different architectures mitigate them.

### 5.1 Control Plane Latency Components
Research identifies three primary components of control plane latency [cite: 5]:
1.  **Inbound Latency (Switch $\to$ Controller):** Includes ASIC processing, PCIe transfer to the switch CPU, OS interrupt handling, and network transmission to the controller.
2.  **Processing Latency (Controller):** The time the controller takes to process the event and compute a response. This is highly dependent on the controller's load and the complexity of the TE algorithm.
3.  **Outbound Latency (Controller $\to$ Switch):** Network transmission and the time for the switch to install the new rule into its TCAM/flow table.

### 5.2 Impact of Architecture on Latency
*   **Centralized:** High network transmission latency (if the controller is remote) and high processing latency (due to queuing of global events) [cite: 21].
*   **Distributed (Flat):** Lower network transmission latency (closer controllers) but potentially high processing latency due to synchronization overhead (consensus protocols) [cite: 18].
*   **Hierarchical:** Lowest effective latency for frequent events. Local controllers eliminate network transmission to a remote root and reduce processing load. Only rare events incur the higher latency of the root controller [cite: 22, 34].

### 5.3 Control-Data Plane Offloading
Another mechanism to reduce latency is **offloading intelligence** to the data plane. By pushing some control logic (e.g., local failure recovery, simple load balancing) down to the switches (or local agents), the system reduces the frequency of interactions with the controller [cite: 35]. This "Control-Data Plane Intelligence Trade-off" significantly reduces the latency for critical, time-sensitive operations while reserving the controller for complex, global optimizations.

---

## 6. Consistency Models and State Synchronization

The "Global View" is not a static entity; it is a dynamic state that must be synchronized across distributed controllers. The mechanism of synchronization defines the balance between view accuracy and system responsiveness.

### 6.1 Strong vs. Eventual Consistency
*   **Strong Consistency:** Ensures that a TE decision is based on the absolute latest network state. This is critical for preventing routing loops and black holes but incurs high latency due to the need for global consensus (e.g., using Paxos) before acting [cite: 16].
*   **Eventual Consistency:** Allows controllers to act on their local copy of the global state, which is synchronized periodically. This enables ultra-low latency responses but requires mechanisms to handle temporary inconsistencies [cite: 20].

### 6.2 Adaptive Consistency
Some advanced SDN controllers employ **adaptive consistency models**. They dynamically adjust the consistency requirement based on the traffic type. For example, a critical security policy update might enforce strong consistency, while a routine load balancing adjustment might accept eventual consistency. This dynamic tuning is a sophisticated mechanism to balance the global view/latency trade-off in real-time [cite: 14].

---

## 7. Future Directions and Emerging Technologies

The evolution of SDN continues to refine these balancing mechanisms.

### 7.1 AI and Machine Learning in TE
Machine Learning (ML) and Reinforcement Learning (RL) are increasingly integrated into the control plane to predict traffic patterns. By predicting congestion before it happens, the controller can proactively install rules, effectively masking the latency of the control loop [cite: 28, 36, 37].
*   **Mechanism:** An ML agent analyzes historical data to predict "Elephant" flows. The controller pre-installs paths for these flows, ensuring that when the traffic arrives, it is routed optimally without the delay of a reactive packet-in/flow-mod cycle [cite: 6].

### 7.2 P4 and Programmable Data Planes
The rise of P4 (Programming Protocol-independent Packet Processors) allows for even greater offloading of logic to the data plane. Switches can be programmed to perform complex stateful operations (e.g., load balancing based on queue depth) at line rate, reducing the reliance on the control plane and minimizing latency to near zero for those specific functions [cite: 4].

---

## Conclusion

The mechanism within the SDN control plane architecture that balances the global view of centralized decisions with the latency of distributed implementation is primarily the **Hierarchical Control Plane**, supported by **adaptive consistency models** and **traffic-aware delegation**.

By stratifying the control plane into **local** and **global** layers (as seen in Kandoo), SDN architectures decouple the handling of frequent, latency-sensitive events from rare, complexity-intensive decisions. This allows Traffic Engineering to benefit from a global view for high-impact routing decisions (Elephant flows, inter-domain routing) while maintaining the responsiveness required for local stability and scalability (Mice flows, failure recovery). Furthermore, the strategic use of **East-West interfaces** and **topology abstraction** ensures that the global view is maintained with minimal synchronization overhead, preventing the control plane from becoming a bottleneck.

### References
*   **[cite: 1]** SDN Control Plane Challenge for Minimum Control traffic: Distributed or Centralized?
*   **[cite: 2]** Software-defined Networking (SDN) Controller.
*   **[cite: 38]** Distributed Control Plane vs Centralized Control Plane.
*   **[cite: 14]** Dependable Industrial SDN: State of the Art and Open Challenges.
*   **[cite: 3]** Managing IoT-Based Smart Healthcare Systems Traffic with Software Defined Networks.
*   **[cite: 36]** Security of SDN-IoT/IIoT Systems.
*   **[cite: 4]** SOFTWARE DEFINED NETWORKING (SDN) CONTROL PLANE IN EVALUATION FOR RELIABILITY AND FAULT TOLERANCE.
*   **[cite: 15]** Dynamic Control Plane for SDN at Scale.
*   **[cite: 5]** Measuring Control Plane Latency in SDN-enabled Switches.
*   **[cite: 19]** Dynamic Traffic Engineering Considering Service Grade in Integrated Service Network.
*   **[cite: 11]** Latency Reduction Techniques in SDN-Based Wide Area Networks.
*   **[cite: 27]** Traffic Engineering in Software-Defined Networking: Measurement and Management.
*   **[cite: 12]** SDN-BASED TRAFFIC ENGINEERING FOR DATA CENTER NETWORKS.
*   **[cite: 13]** Simple ElastiCon : A Distributed SDN Controller.
*   **[cite: 31]** A Control-Plane Perspective on Reducing Data Access Latency in LTE Networks.
*   **[cite: 11]** Latency Reduction Techniques in SDN-Based Wide Area Networks.
*   **[cite: 21]** Kandoo: A Framework for Efficient and Scalable Offloading of Control Applications.
*   **[cite: 25]** Latency-Aware Reliable Controller Placements in SDNs.
*   **[cite: 39]** Controller placement problem.
*   **[cite: 17]** Exploiting Locality in Distributed SDN Control.
*   **[cite: 40]** Load Balancing Mechanisms in the Software Defined Networks.
*   **[cite: 6]** Review of Load Balancing Mechanisms in SDN-Based Data Center.
*   **[cite: 7]** Load Balancing Mechanisms in the Software Defined Networks.
*   **[cite: 30]** Analysis of Load Balancing Techniques in Software-Defined Networking.
*   **[cite: 41]** Important Data Treatment in SDN.
*   **[cite: 8]** Traffic Engineering in Software-Defined Networking: Measurement and Management.
*   **[cite: 9]** Data Driven Path Selection for Inter-NREN Communication.
*   **[cite: 37]** Machine Learning in Traffic Engineering for Software Defined Networks.
*   **[cite: 16]** Consistency of the SDN Control Plane.
*   **[cite: 20]** State Consistency in Distributed SDN Controllers.
*   **[cite: 22]** Kandoo: A Framework for Efficient and Scalable Offloading of Control Applications.
*   **[cite: 24]** Topology-Preserving Traffic Engineering for Hierarchical Multi-Domain SDN.
*   **[cite: 28]** Traffic Engineering in Software defined Networks using Reinforcement Learning.
*   **[cite: 23]** Kandoo Project Page.
*   **[cite: 11]** Latency Reduction Techniques in SDN-Based Wide Area Networks.
*   **[cite: 5]** Measuring Control Plane Latency in SDN-enabled Switches.
*   **[cite: 21]** Distributed Hierarchical Controllers Design.
*   **[cite: 33]** An Efficient Hierarchical Distributed SDN Controller Model.
*   **[cite: 35]** Control-Data Plane Intelligence Trade-off in SDN.
*   **[cite: 18]** The effect of network topology on the control traffic in distributed SDN.
*   **[cite: 21]** Designing a scalable control plane for SDN.
*   **[cite: 34]** Hierarchical Control Plane Designs to Scale SDN Applications.
*   **[cite: 26]** A Hybrid Hierarchical Control Plane for Software-Defined Network.
*   **[cite: 32]** An Effective Hierarchical Control Plane for Software-Defined Networks.
*   **[cite: 29]** Performance Analysis of Load Balancing Mechanisms in SDN Networks.
*   **[cite: 10]** Overcoming traffic engineering challenges with SDN.
*   **[cite: 42]** Traffic Engineering with Reinforcement Learning in SDN.

**Sources:**
1. [uth.gr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvK0kjanXmBJV6hNZ_uqMalMg4_BWOioDgg97n4nYJKMM4b2oL_korNaZV3sn4KU0NAX22byc3E3HIRzIaCJrTDTvigqzHZbJmTVDK9PVquJYdlbNnKHYkTzUR6QNE2s-zhdT2JWq-vJpXMs126yArMtwB1zLNH_BfGKUP6Yryns3jPvksi0On7zxWnr9o4nm5iksF2cZqSw5HoLRgw6kPjlyF8fO-6zFEN8Rp0pp2pWrcKYQsiiwL1g==)
2. [geeksforgeeks.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-wXJne1pmHkCv4M3o6Ck2jqg2km11xblK6YRZ8tWIkfMWvyAjgE1Xi5PvL3D5WMjV7DBmuuxIrKvAB_6yuzq5dbBQGQdqDXSO54KTK-q2Dy6FuGvjx41IJuWdxfsc9c8cBXo22ODuzQ-xK1qQvYP5YRzPvhdfMsmb2WWtmI0VfAM-TnW074DDP9HnTwC59g==)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFuGW8xTXRpN1mlqP5q579aT5sMnadE7NSQx-E5yrqJUncWrpmfpUsdMiM1vwbn33_A9vx-osbBsB6WziDkjtWmOrL9gvG1uSysDYbuZ2CEj1DB_DakKnisIAEBko1LoEfY_MXdiTzYP1z_6G7S5VPYldP_wusw4L0gAtxORr95a8ijAFS_kxaWWhF7TL3YWKr2A73aix15oRKv8zfxfPDjwpGREkXQM9PeF5hXHH9RFMgjsFp)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnwfbPHylxh6Pe9087Q8gthpvnDdmEv7kMyJxZCpuACQ6kWtg32pD7OEqBMnGfCJwQSavrRzcSPLQOCuKAQiIDYmvmfsoGZ-_QbLFBoJ38pBM0pFDKUD8hH2V-n0weSF43AC3qkQ0oCIF3sf5C5GiUFQJM52O_t695qd-jWocY0cSoVDUXPX3AR0nHpaiwv2DhjKcMXQqNrnMlfYa6s1z9OU4mtuUCyMMNakP8tn6aicxErtb-6MXN4BCpu-tZ4_nnp7PBjON7)
5. [wisc.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2rpZGHg7GM3u5btITyZIurOUmJ_jC3KMiocQrr7KdcRRB_QHRwybws-y5b9cUcFsyJNMiL7pCColxsy0e3n7mJFjYTDBwIRUcm_CcP1v58nUxtwvXVeyWJlvaOexUXcOxTkV17wdEib_3Mfo=)
6. [scirp.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGh8tUEsS1UW_b1FluxYnR0wudzUZSnOsnMtrr8Qd5KITKFcRTl5-kGYVfYV00mpimjLmoDjO9gJC8_OObU7f_ftT6HrfC_zkHmsgi44NNKT_Z-sbjbauISa7fHjjZTrsGETTm848b5rINSw21-T2R_Ww==)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhWas57nvNEoR0AMeo9EEstDeIfPv9IQ_JmIph_reNt_dj6AgPOTENsGMXbt0I6I5nMq9HBCKgykgYBB4RD1xqXG2QRk4j1SxqnUqg7GYqL79CCwNgg0JpKKm1Do4SQCs8g0bNIccOuWtp9ow_fjuw4_XwCEP2LS8dRO-5a-qOWFPS6yxLcE6M9-NxloOyFVHHvME-QeGNunFFRPBKQ1HFKWK8KmTCDX_dZ9si75zf8JH8ttV2bOe8zpdAkacoEA9tZETap8Of9s_VgAtC4l2uhT2-H0TOdh1xzg==)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrnd81dwDdoGTuBHNgDqdcLawG_EhEXZabvGK2FfNiqEDoRtt98zy6u4vNwcgfm5ojLtv3S0QxYWuxvrEccXTLJKvGoV5hMj0J6ExoLaFGJtL5rg8sg8fm_7VhuDNPLcRAdMr5oiYByXyFS_GMI-6QsC3XnJ6TnuOBALBChMPMcu_skSSCc4XqZAVP3oimbBhj1ZOqFQQf8hwcfqLmzSC1VyR1qSuaH9L73jMWJg9DT__RoZ9I)
9. [uct.ac.za](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjPamJ1CAR1Z5qjEQnenEnnGx5iNc1fjVztZrFmQkMAkUoQNj6iyH4bPtj6VqxtbvFvvNKcHnuxGv2mdBwfbvrvVzPKhjzHONXgM-ufqr6CyiFvXwfjWDU_J5np4QkQeBtjxk-cPL_7KqW9u3YM-NxBCJuG-O0EPE=)
10. [apnic.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfY-YpgAA7ux6eSUrOUBwV02LVaIu65ReRYqq12tauotatnBZX0j7g9SWxYd9AiGDxJiXY1lcDbdwcuxiPvJ6nA9LsdVho81jTJv3NsMt7X7fI6__0SbIsvRrBTiBaLZ41XHdsnyAos_92XYqUn0yUIRwkricgzEjrmHs5tINxMaIJwAk=)
11. [computersciencejournals.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3xqJal8SaI8MN-hxvQIWtLOP5N37nYMsMw85XLXvPS840ISKtTWaxBTQjhwLPjoGd1seOO7hehwxuxb_csJADz8s0iBZyhC-QOLrLDTYcDw2d8HRDF-9LF3KVeUvf9FRLlJFXwkL8W_ZLr8FpzwdUTxi10oB7FWgLmQ==)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5dGzYBahU6HwxtHRSk3Tf85w-9x18cpoKspJJUfVQK2lbYjC5Nbp2M6ab__4yA5C5LJLz4m4dl4JVaGfKQFeo9Ce07GD0cz6JhqdvGoGbahnFg9EBtZRoKRS7Hhvaj6vleRg38SUMUmgWeO5Sr3QIncTlD_ycTuXz9TiI6uRARDyYJp-6Q5VBxerP79uiTDDV7aFUY8Q_N6Y8WKOmjNP-k5668rcs75EATqkwNaVCV0XT3v1ttcWjiKrq9YL9-PBPxiar)
13. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkvg8twb3fuWWLjumIothLGa-A26PsF-umVxV55c4-gzX_si9g9lGPXvN9pPAf3mPEuq546j8T7XeWSSF8xZWOzY-vq_B_uDgrP0FS5rs3QBK5JN0DoT-Frbw=)
14. [tum.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGksYRk32uby8SAt39psFUgHtKR8ftCHsK7p094KTPHSD5FBfc2HF277IYqcELafE9BG24qBkCeJ2NIK5II_4RI2gcN0M8H6BY6cYougwQGzVWeqL3z5aE0h92xhAHxIi-2Khf5ZM=)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLmDhRydyL999pDOLslhYjVJlq-kWEg8XF7SG_TZXOGrv-PAKvdhYKQ-LqUiu-5VyAIc43lgBwOmHQoIQBP4I6ZV_T0lsd4GttdQELg4aM22kWjm46fcLcUcXWbeLV6SMfRHHp_mhApjxaybXY7cMVdxg-QSIa_nyaptWVov1bw6Tzo--JMfkpB4R3j8k=)
16. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe8VYZKaot0EpcFCDXq9p-weslcS3h8PWM8FhEi028rwfdOvhdo_uOjqF1k4WeZXzE0U0BGWpmjELADOfet_x97MeOZQ6I_dvV9beB6XRx4m7msCoeg0KyUhuGZw==)
17. [jukkasuomela.fi](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxYuGnC90S5lRTT3T-3YVmAiUAoFTtgSJaAT3KiWWS4jCz8cbThq3lQ5bshFFBCx4ikyQKyKlmcQgwU_gA0piCp5qypuxOBATQVKxgvrtgY-Y3IgS3S6yLcjIRVVA=)
18. [ifip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYGv-sKTJjfBOetPcypyUeyjLoc_pBGrCpbZoVIgjhxe-JV5hxGZc-ejMphcJ2cJP4gsSlYCU1CFz4g7AAtRO-oSwteWxc8g04h6wT6Y5ESplly-OgjzmLQe0cJsLHIhESDDXm7xo-DOOHJxRVK-P55aNHqiv1QTLkZd6i)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIeoLUnMB-TABZ2rOUnURwKVe_YIUbNqVO2OQcEovnPyE2wWTOk6e2x6K5iztj602uXa2Nj6XWsBQbuDQM3i4yBRFL9XwTnroWqtRnnXwCT1SIsP29aLZRk2UFfat7uR2YsfyZoZkDF2iVAdWyJmYWNZVtQChmYOYu9COx95LN9bZKt609QOMYIahLRQ==)
20. [ipspace.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQEc3woY1a2ahsoADJAnQuNWDLwqx_Gh8WJsuWzjwVAulSjUHmZJp4LaA2aIx4Lp7JcT0UJYYN2UoZFBh7I91PlKbECoyeA3IPWLhq6G80iOSAUOWAmT4O2gHsQ9XNudbauXLR0OgDcvtvD8SKiB-GgolC-BjpnGFQaKVUspGT)
21. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPczILmll8oZeIfzIQFqY5OuZ2Lg8Ax57W1p30jwXKB482qiXLeKRbaM8JtLZ4jzah3Qftzqdj4oXmKcsHv_lp44GvG14ZN12iJMrl8y1fhBpmznEuWnH5Xc8=)
22. [sigcomm.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrrPCBvnl6KHk7yj6rDRnwiw1eHUKJixutMvySKz1uLCHv4vtH_Ni9MLBYS0FdP3ag8lDfuXXe5kcZLUHcrONSq840LDgYdxJK4iCfq-faU5z1WBBl5twiIpN3m0Piti92z_8qt96obDbwoetdznbx7C3htw==)
23. [toronto.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOw3PbXvWU0QM5yF5sbWxdANW5SYCZAnVKcX-lync246UzCdcDUxc4VguXqX3_m1TZx4lS53QxPsA4prUVo9i9HjW9m-agLMGuzVHvaLhoBAb7uX3h1EASHodDdbOzjJfB6Ng=)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQD70pjA88xi_f9B-GUbD-AsKTL2xATwOENYErPXJrVrdbTsJPqLkGr53lC6pLZh-fgVQcfb75p-Fy5xM2SJviOTF4GOSjkm7_lWFFskaC3hY_fvEvafXGIkEO1RZv4XvxF3cF-ek8bZMQId3dGPWIdA5iNYM23CbQGcfNHTBFnVAzZG8YcutMo5F_sasSxgfHpqaw37FN5qmwxaA_b5thpmsg5FlKprqx-rTk80NWww==)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjwO2g7k4UCPXpaT3MXa-FKe7WzHorVtbTlBnSVmIbKwaiylKfbXKlF8rwyQgft3ds4zJ1dQCDVnyyhTiWLFG8dD_k_ASYI-vZvAWGt3oZcLx9yBV4o44Qc9IlgzlF3beHQyg6u7528dEFWuVVHAsXLjbOIRaaiH5vTEZD7FL4WFuULi0ltbG9eh5lMpCeL-qs93Qwm9zcjXJD8Q==)
26. [rroij.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVadtUls5Pzm3zWLQwE4ZnuokBksStu44OTW-BA-MWvhCV_CDyY-IU3-uQCoWofCt9oL0FV5qPysggja27ysHWLdm4DZlulAT4TEkZZvX0695HJc4BLxHduDMPxPEuiPtpRHBLKPZaMf0HtkK-4dIm_bFL5lLnl1PUIZUrdHjL5SiTU8KZgk1_prEmbws8Mct2oju1qPu7ASW6k9FVwxTHwSXv)
27. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMfrNZWQE8CIyhl7uMTU19QcFGpkpBkAWX6_A1cb6jL2HcWiypbGn02CCkT_29b7R5HRvaKi3KcM0ASNhhGMnjTl7j82QGdpeAhfwj3robbwPuGnr_RDxTe0ZuHM6U12rE)
28. [thesai.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH35bQmpvtD74x-oK35XAWbMse-eSI8OiXZnTOy_jPZ8KNZ8ZKXMJzanyb2pd0sXJwz8pX5mLeiqVh3vqJiUDf70aXfb3kHtAw5l2FYuPbv4MYv7vUb8lIlTP0XNaVjFX8-LnSNG7zHGjG2Pp1VUKYk46bWETPAyx-gB1UgUuUVFP8f4gT_qfc1ZQGR7KpcJBd8gM3ibJm_zzva)
29. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcbOuMhRP-x0V4GhG-Rd5jsZSppM2utRxSf2k40jJxJrDeOMtZpxpHPD3r1IM8G5x2sIcclaewjSajWcXS5d6H72a1oIFBcoO6bGKj6pMj-Q64Xarx12FJeTL8nOML04bRVQMkdQRhnJdMwYj-WZxmQ7P44PqtI6EwK6bAwcP6krv9Ybz9zk9JAoVPLwP4W4RHUzMozZ34Wb_ia-sKimomRtV7-lWJ3mo=)
30. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkxTVtpprghq1S3lfukYN_YUHJJh9UHXCxtsv93MXwdHA4LwVhs6eRPtclNOQXkPxIU6j8QVFJaMjSHl5Pdp7uGlfP__e8ea2lrd1zsWAOGMZqamZxDJagGkY0)
31. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHa8nqCZ5_OUDn4UiGNye8qe_FzT97ntVrazM9Y2RtWbG9pmlFcmBSNdSfi3pJY2vRxUZVk4GG_U5HR0A9iWgElOxT-nGWxvgTnrMSHsf61tBTLheCPrqPb04BeYvWDsH2uN1G_EvMiMfBI3hVShkvtjmnJnTSP9iAj-IPcNoXI7kAnykxGOb15J1H_Tt3vR4WDpdy7uiU620EWfmPweAUQIXPVbbnhupUkDYjN5UE-Ylac)
32. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3EePhaSaYlscC5dWrCjUoc1g3AfztxldSfxM-nH9zMbxIZseixzRiwvnN5iHUbRhJFeTrGTCDaHR-pim2fmz1q3pVy6wxiJrbcFsaIw2zT6qzFcupFLPr7X0FHX6L8UV7_BD23QfVhVNL9uoW24IuvfX2uEqSYaPmgfYtS87B7SCds9Gu224RbUc9J5DgziSTAHXhNqjt4djSy4xISfmfkosk2cRXte904B4U4k4tYPreuOMgF6mYog1_enzejjeijhk2Np6rJQ30EDbvc9rJ7HIBh9TEjw1k_LSRHrX0KQ==)
33. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGD2Wmh4I6uooo7C1-gK6tWWiahgyaJb3uXsQPPfZTC9pYmOXVocmq9di12sKJFgc2ETv8jRBEC7DuXb6kRzskinyOxA8hHzZ9AJXuTu9zKmUozlESElQkNGjX1ysqUJlAY6Hk1l6Zprpc5cZ4Qd4HRUx1kqdcwfqcfZYY5aOrox0u32q3MKBK860M0KFlH622RBdtnptdMJNf7ksitqtVQYRfNTjXgzqNtcqQ40YSJEro50d8NoUC)
34. [iiitd.ac.in](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAQRT1yBkz6CkwoaHeYDFIfz78dpfYVTKHcUc2co027FSBP0_v1RXaKLHP350zKEH_i5UE3P5I3XIG_tUdKldK4lcVoExrJyFnH4CJC6qYtvQKbbPtiZz-poSHjhX8VPjqBJl0HPaQQ5i9A5eDH7EHZI-6t2pOs_9C8A==)
35. [ieee-security.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0dZfLYbMH_uNHF39O6DnS3dhCfokz9KXdMtzuvzAtFIrQxYQRPGASmT01v2-5YoM9PTJ7pQRv2qOJzsvYBAOTOpn4mtIX6uO_Gi4KWnLlZ2I4GtPZyk-g6bvfaIkfOhYJsVDXTHVqtAzm96LXV7kxyK3ltW308LSUnHToEEhuuw4tfJ4BdBhOVr4=)
36. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwIKpgyW_ICu9qxvDMiZA2Pu_KdLOt3diUbNyOVXDy51s8oTYMMpnPWKh1pP1Tj2fEnqVSJWAk7Oym8rKl7zz2_mXSAnUn0oRzVZV1obWA2hbsjWNNLdE1Evhx)
37. [pjlss.edu.pk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiLhcEIabBY80WCTmaGDyyMiuNRxQA5mEkl010NQ3MrNky1ALjI0AOpYyqnOL-jyrWPQLOGtFIv9FP6j95Ncxh6IsrqIuRegJnposzuBP1vbMcTRw3HZoK6wky4hRY5RFOUSbxb1Xn1yEO3w==)
38. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHz7YmDGBBUyPjK0IofVpp_xmmIMq4nczO5EkjQYSp9j-I5_6IfO4cMLtoVvV_6lULnkb9PBEPz8s7_d13c2DXGkMAa_W388bbP19OpOnPLX6pGI-VtMPXx-qpKfgQBg==)
39. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHgHEwroUQl2vfVreLUIG72NJSSlubKomlaTYEKIXQTzxA32ALMQZx6I-eiy5V1Um5ffl6_wF0SThJu8Fv4HOryLoemo6dWG8JHMTpwv9d0dbTpqKtdIqVPTLnPPDXiqmhb8mam5BJv1V1nsGtfC8lkJnxnZ_PJqktjyT7hg==)
40. [core.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFstoB1ib5JPrC-aHbvQom1Wsa2IXr1eqT6Hm8_Rlfmzroi8Cr8Y9-VHdH50jjyH53fS13KCzAt3ZQaizBwX0v36hsFRJwAnMDGjVABNC4ELcHNEuUjt3nVeGqjHTHuWxjM)
41. [nas-conf.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWJq8s4dbFBlPDOkN7vixWKY73jZcz-V0VNRXxvlYMUe2CasWOx7Cvo8SPyWvwWGz8LnomS7tK8c5SYeXFu6dBYGfxo71WV99_zd_hIs_00Lj91JYS5bWLt_EWacdL0qcRZS5M)
42. [ucr.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGr2VJQVqouIqEZe8kwh8AzqfG8YGe1bP39sY9TdBXVCm2uNAPoPijFMKyb89xESPlzWKlJmbh4p0eH0yqUY8g90f5V7o6i9aWyoPKZU-0Hni8PCkcAs8ww8jeRlcuKCZobUKd-1b8rdaKlJD8E)


## Annotations
Annotation(end_index=1823, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvK0kjanXmBJV6hNZ_uqMalMg4_BWOioDgg97n4nYJKMM4b2oL_korNaZV3sn4KU0NAX22byc3E3HIRzIaCJrTDTvigqzHZbJmTVDK9PVquJYdlbNnKHYkTzUR6QNE2s-zhdT2JWq-vJpXMs126yArMtwB1zLNH_BfGKUP6Yryns3jPvksi0On7zxWnr9o4nm5iksF2cZqSw5HoLRgw6kPjlyF8fO-6zFEN8Rp0pp2pWrcKYQsiiwL1g==', start_index=1811)
Annotation(end_index=1823, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-wXJne1pmHkCv4M3o6Ck2jqg2km11xblK6YRZ8tWIkfMWvyAjgE1Xi5PvL3D5WMjV7DBmuuxIrKvAB_6yuzq5dbBQGQdqDXSO54KTK-q2Dy6FuGvjx41IJuWdxfsc9c8cBXo22ODuzQ-xK1qQvYP5YRzPvhdfMsmb2WWtmI0VfAM-TnW074DDP9HnTwC59g==', start_index=1811)
Annotation(end_index=2068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnwfbPHylxh6Pe9087Q8gthpvnDdmEv7kMyJxZCpuACQ6kWtg32pD7OEqBMnGfCJwQSavrRzcSPLQOCuKAQiIDYmvmfsoGZ-_QbLFBoJ38pBM0pFDKUD8hH2V-n0weSF43AC3qkQ0oCIF3sf5C5GiUFQJM52O_t695qd-jWocY0cSoVDUXPX3AR0nHpaiwv2DhjKcMXQqNrnMlfYa6s1z9OU4mtuUCyMMNakP8tn6aicxErtb-6MXN4BCpu-tZ4_nnp7PBjON7', start_index=2056)
Annotation(end_index=2068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFuGW8xTXRpN1mlqP5q579aT5sMnadE7NSQx-E5yrqJUncWrpmfpUsdMiM1vwbn33_A9vx-osbBsB6WziDkjtWmOrL9gvG1uSysDYbuZ2CEj1DB_DakKnisIAEBko1LoEfY_MXdiTzYP1z_6G7S5VPYldP_wusw4L0gAtxORr95a8ijAFS_kxaWWhF7TL3YWKr2A73aix15oRKv8zfxfPDjwpGREkXQM9PeF5hXHH9RFMgjsFp', start_index=2056)
Annotation(end_index=2381, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2rpZGHg7GM3u5btITyZIurOUmJ_jC3KMiocQrr7KdcRRB_QHRwybws-y5b9cUcFsyJNMiL7pCColxsy0e3n7mJFjYTDBwIRUcm_CcP1v58nUxtwvXVeyWJlvaOexUXcOxTkV17wdEib_3Mfo=', start_index=2372)
Annotation(end_index=3112, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhWas57nvNEoR0AMeo9EEstDeIfPv9IQ_JmIph_reNt_dj6AgPOTENsGMXbt0I6I5nMq9HBCKgykgYBB4RD1xqXG2QRk4j1SxqnUqg7GYqL79CCwNgg0JpKKm1Do4SQCs8g0bNIccOuWtp9ow_fjuw4_XwCEP2LS8dRO-5a-qOWFPS6yxLcE6M9-NxloOyFVHHvME-QeGNunFFRPBKQ1HFKWK8KmTCDX_dZ9si75zf8JH8ttV2bOe8zpdAkacoEA9tZETap8Of9s_VgAtC4l2uhT2-H0TOdh1xzg==', start_index=3100)
Annotation(end_index=3112, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGh8tUEsS1UW_b1FluxYnR0wudzUZSnOsnMtrr8Qd5KITKFcRTl5-kGYVfYV00mpimjLmoDjO9gJC8_OObU7f_ftT6HrfC_zkHmsgi44NNKT_Z-sbjbauISa7fHjjZTrsGETTm848b5rINSw21-T2R_Ww==', start_index=3100)
Annotation(end_index=3345, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjPamJ1CAR1Z5qjEQnenEnnGx5iNc1fjVztZrFmQkMAkUoQNj6iyH4bPtj6VqxtbvFvvNKcHnuxGv2mdBwfbvrvVzPKhjzHONXgM-ufqr6CyiFvXwfjWDU_J5np4QkQeBtjxk-cPL_7KqW9u3YM-NxBCJuG-O0EPE=', start_index=3333)
Annotation(end_index=3345, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrnd81dwDdoGTuBHNgDqdcLawG_EhEXZabvGK2FfNiqEDoRtt98zy6u4vNwcgfm5ojLtv3S0QxYWuxvrEccXTLJKvGoV5hMj0J6ExoLaFGJtL5rg8sg8fm_7VhuDNPLcRAdMr5oiYByXyFS_GMI-6QsC3XnJ6TnuOBALBChMPMcu_skSSCc4XqZAVP3oimbBhj1ZOqFQQf8hwcfqLmzSC1VyR1qSuaH9L73jMWJg9DT__RoZ9I', start_index=3333)
Annotation(end_index=3625, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfY-YpgAA7ux6eSUrOUBwV02LVaIu65ReRYqq12tauotatnBZX0j7g9SWxYd9AiGDxJiXY1lcDbdwcuxiPvJ6nA9LsdVho81jTJv3NsMt7X7fI6__0SbIsvRrBTiBaLZ41XHdsnyAos_92XYqUn0yUIRwkricgzEjrmHs5tINxMaIJwAk=', start_index=3615)
Annotation(end_index=3940, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3xqJal8SaI8MN-hxvQIWtLOP5N37nYMsMw85XLXvPS840ISKtTWaxBTQjhwLPjoGd1seOO7hehwxuxb_csJADz8s0iBZyhC-QOLrLDTYcDw2d8HRDF-9LF3KVeUvf9FRLlJFXwkL8W_ZLr8FpzwdUTxi10oB7FWgLmQ==', start_index=3926)
Annotation(end_index=3940, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5dGzYBahU6HwxtHRSk3Tf85w-9x18cpoKspJJUfVQK2lbYjC5Nbp2M6ab__4yA5C5LJLz4m4dl4JVaGfKQFeo9Ce07GD0cz6JhqdvGoGbahnFg9EBtZRoKRS7Hhvaj6vleRg38SUMUmgWeO5Sr3QIncTlD_ycTuXz9TiI6uRARDyYJp-6Q5VBxerP79uiTDDV7aFUY8Q_N6Y8WKOmjNP-k5668rcs75EATqkwNaVCV0XT3v1ttcWjiKrq9YL9-PBPxiar', start_index=3926)
Annotation(end_index=4110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFuGW8xTXRpN1mlqP5q579aT5sMnadE7NSQx-E5yrqJUncWrpmfpUsdMiM1vwbn33_A9vx-osbBsB6WziDkjtWmOrL9gvG1uSysDYbuZ2CEj1DB_DakKnisIAEBko1LoEfY_MXdiTzYP1z_6G7S5VPYldP_wusw4L0gAtxORr95a8ijAFS_kxaWWhF7TL3YWKr2A73aix15oRKv8zfxfPDjwpGREkXQM9PeF5hXHH9RFMgjsFp', start_index=4101)
Annotation(end_index=4474, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkvg8twb3fuWWLjumIothLGa-A26PsF-umVxV55c4-gzX_si9g9lGPXvN9pPAf3mPEuq546j8T7XeWSSF8xZWOzY-vq_B_uDgrP0FS5rs3QBK5JN0DoT-Frbw=', start_index=4461)
Annotation(end_index=4474, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvK0kjanXmBJV6hNZ_uqMalMg4_BWOioDgg97n4nYJKMM4b2oL_korNaZV3sn4KU0NAX22byc3E3HIRzIaCJrTDTvigqzHZbJmTVDK9PVquJYdlbNnKHYkTzUR6QNE2s-zhdT2JWq-vJpXMs126yArMtwB1zLNH_BfGKUP6Yryns3jPvksi0On7zxWnr9o4nm5iksF2cZqSw5HoLRgw6kPjlyF8fO-6zFEN8Rp0pp2pWrcKYQsiiwL1g==', start_index=4461)
Annotation(end_index=4773, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2rpZGHg7GM3u5btITyZIurOUmJ_jC3KMiocQrr7KdcRRB_QHRwybws-y5b9cUcFsyJNMiL7pCColxsy0e3n7mJFjYTDBwIRUcm_CcP1v58nUxtwvXVeyWJlvaOexUXcOxTkV17wdEib_3Mfo=', start_index=4764)
Annotation(end_index=5029, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2rpZGHg7GM3u5btITyZIurOUmJ_jC3KMiocQrr7KdcRRB_QHRwybws-y5b9cUcFsyJNMiL7pCColxsy0e3n7mJFjYTDBwIRUcm_CcP1v58nUxtwvXVeyWJlvaOexUXcOxTkV17wdEib_3Mfo=', start_index=5020)
Annotation(end_index=5263, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGksYRk32uby8SAt39psFUgHtKR8ftCHsK7p094KTPHSD5FBfc2HF277IYqcELafE9BG24qBkCeJ2NIK5II_4RI2gcN0M8H6BY6cYougwQGzVWeqL3z5aE0h92xhAHxIi-2Khf5ZM=', start_index=5249)
Annotation(end_index=5263, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLmDhRydyL999pDOLslhYjVJlq-kWEg8XF7SG_TZXOGrv-PAKvdhYKQ-LqUiu-5VyAIc43lgBwOmHQoIQBP4I6ZV_T0lsd4GttdQELg4aM22kWjm46fcLcUcXWbeLV6SMfRHHp_mhApjxaybXY7cMVdxg-QSIa_nyaptWVov1bw6Tzo--JMfkpB4R3j8k=', start_index=5249)
Annotation(end_index=5657, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGksYRk32uby8SAt39psFUgHtKR8ftCHsK7p094KTPHSD5FBfc2HF277IYqcELafE9BG24qBkCeJ2NIK5II_4RI2gcN0M8H6BY6cYougwQGzVWeqL3z5aE0h92xhAHxIi-2Khf5ZM=', start_index=5643)
Annotation(end_index=5657, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe8VYZKaot0EpcFCDXq9p-weslcS3h8PWM8FhEi028rwfdOvhdo_uOjqF1k4WeZXzE0U0BGWpmjELADOfet_x97MeOZQ6I_dvV9beB6XRx4m7msCoeg0KyUhuGZw==', start_index=5643)
Annotation(end_index=5880, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYGv-sKTJjfBOetPcypyUeyjLoc_pBGrCpbZoVIgjhxe-JV5hxGZc-ejMphcJ2cJP4gsSlYCU1CFz4g7AAtRO-oSwteWxc8g04h6wT6Y5ESplly-OgjzmLQe0cJsLHIhESDDXm7xo-DOOHJxRVK-P55aNHqiv1QTLkZd6i', start_index=5866)
Annotation(end_index=5880, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxYuGnC90S5lRTT3T-3YVmAiUAoFTtgSJaAT3KiWWS4jCz8cbThq3lQ5bshFFBCx4ikyQKyKlmcQgwU_gA0piCp5qypuxOBATQVKxgvrtgY-Y3IgS3S6yLcjIRVVA=', start_index=5866)
Annotation(end_index=6125, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIeoLUnMB-TABZ2rOUnURwKVe_YIUbNqVO2OQcEovnPyE2wWTOk6e2x6K5iztj602uXa2Nj6XWsBQbuDQM3i4yBRFL9XwTnroWqtRnnXwCT1SIsP29aLZRk2UFfat7uR2YsfyZoZkDF2iVAdWyJmYWNZVtQChmYOYu9COx95LN9bZKt609QOMYIahLRQ==', start_index=6111)
Annotation(end_index=6125, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3xqJal8SaI8MN-hxvQIWtLOP5N37nYMsMw85XLXvPS840ISKtTWaxBTQjhwLPjoGd1seOO7hehwxuxb_csJADz8s0iBZyhC-QOLrLDTYcDw2d8HRDF-9LF3KVeUvf9FRLlJFXwkL8W_ZLr8FpzwdUTxi10oB7FWgLmQ==', start_index=6111)
Annotation(end_index=6448, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYGv-sKTJjfBOetPcypyUeyjLoc_pBGrCpbZoVIgjhxe-JV5hxGZc-ejMphcJ2cJP4gsSlYCU1CFz4g7AAtRO-oSwteWxc8g04h6wT6Y5ESplly-OgjzmLQe0cJsLHIhESDDXm7xo-DOOHJxRVK-P55aNHqiv1QTLkZd6i', start_index=6435)
Annotation(end_index=6448, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvK0kjanXmBJV6hNZ_uqMalMg4_BWOioDgg97n4nYJKMM4b2oL_korNaZV3sn4KU0NAX22byc3E3HIRzIaCJrTDTvigqzHZbJmTVDK9PVquJYdlbNnKHYkTzUR6QNE2s-zhdT2JWq-vJpXMs126yArMtwB1zLNH_BfGKUP6Yryns3jPvksi0On7zxWnr9o4nm5iksF2cZqSw5HoLRgw6kPjlyF8fO-6zFEN8Rp0pp2pWrcKYQsiiwL1g==', start_index=6435)
Annotation(end_index=6933, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQEc3woY1a2ahsoADJAnQuNWDLwqx_Gh8WJsuWzjwVAulSjUHmZJp4LaA2aIx4Lp7JcT0UJYYN2UoZFBh7I91PlKbECoyeA3IPWLhq6G80iOSAUOWAmT4O2gHsQ9XNudbauXLR0OgDcvtvD8SKiB-GgolC-BjpnGFQaKVUspGT', start_index=6919)
Annotation(end_index=6933, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe8VYZKaot0EpcFCDXq9p-weslcS3h8PWM8FhEi028rwfdOvhdo_uOjqF1k4WeZXzE0U0BGWpmjELADOfet_x97MeOZQ6I_dvV9beB6XRx4m7msCoeg0KyUhuGZw==', start_index=6919)
Annotation(end_index=7205, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQEc3woY1a2ahsoADJAnQuNWDLwqx_Gh8WJsuWzjwVAulSjUHmZJp4LaA2aIx4Lp7JcT0UJYYN2UoZFBh7I91PlKbECoyeA3IPWLhq6G80iOSAUOWAmT4O2gHsQ9XNudbauXLR0OgDcvtvD8SKiB-GgolC-BjpnGFQaKVUspGT', start_index=7195)
Annotation(end_index=7784, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPczILmll8oZeIfzIQFqY5OuZ2Lg8Ax57W1p30jwXKB482qiXLeKRbaM8JtLZ4jzah3Qftzqdj4oXmKcsHv_lp44GvG14ZN12iJMrl8y1fhBpmznEuWnH5Xc8=', start_index=7766)
Annotation(end_index=7784, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOw3PbXvWU0QM5yF5sbWxdANW5SYCZAnVKcX-lync246UzCdcDUxc4VguXqX3_m1TZx4lS53QxPsA4prUVo9i9HjW9m-agLMGuzVHvaLhoBAb7uX3h1EASHodDdbOzjJfB6Ng=', start_index=7766)
Annotation(end_index=7784, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrrPCBvnl6KHk7yj6rDRnwiw1eHUKJixutMvySKz1uLCHv4vtH_Ni9MLBYS0FdP3ag8lDfuXXe5kcZLUHcrONSq840LDgYdxJK4iCfq-faU5z1WBBl5twiIpN3m0Piti92z_8qt96obDbwoetdznbx7C3htw==', start_index=7766)
Annotation(end_index=8142, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQD70pjA88xi_f9B-GUbD-AsKTL2xATwOENYErPXJrVrdbTsJPqLkGr53lC6pLZh-fgVQcfb75p-Fy5xM2SJviOTF4GOSjkm7_lWFFskaC3hY_fvEvafXGIkEO1RZv4XvxF3cF-ek8bZMQId3dGPWIdA5iNYM23CbQGcfNHTBFnVAzZG8YcutMo5F_sasSxgfHpqaw37FN5qmwxaA_b5thpmsg5FlKprqx-rTk80NWww==', start_index=8128)
Annotation(end_index=8142, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrrPCBvnl6KHk7yj6rDRnwiw1eHUKJixutMvySKz1uLCHv4vtH_Ni9MLBYS0FdP3ag8lDfuXXe5kcZLUHcrONSq840LDgYdxJK4iCfq-faU5z1WBBl5twiIpN3m0Piti92z_8qt96obDbwoetdznbx7C3htw==', start_index=8128)
Annotation(end_index=8536, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPczILmll8oZeIfzIQFqY5OuZ2Lg8Ax57W1p30jwXKB482qiXLeKRbaM8JtLZ4jzah3Qftzqdj4oXmKcsHv_lp44GvG14ZN12iJMrl8y1fhBpmznEuWnH5Xc8=', start_index=8522)
Annotation(end_index=8536, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrrPCBvnl6KHk7yj6rDRnwiw1eHUKJixutMvySKz1uLCHv4vtH_Ni9MLBYS0FdP3ag8lDfuXXe5kcZLUHcrONSq840LDgYdxJK4iCfq-faU5z1WBBl5twiIpN3m0Piti92z_8qt96obDbwoetdznbx7C3htw==', start_index=8522)
Annotation(end_index=8864, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjwO2g7k4UCPXpaT3MXa-FKe7WzHorVtbTlBnSVmIbKwaiylKfbXKlF8rwyQgft3ds4zJ1dQCDVnyyhTiWLFG8dD_k_ASYI-vZvAWGt3oZcLx9yBV4o44Qc9IlgzlF3beHQyg6u7528dEFWuVVHAsXLjbOIRaaiH5vTEZD7FL4WFuULi0ltbG9eh5lMpCeL-qs93Qwm9zcjXJD8Q==', start_index=8850)
Annotation(end_index=8864, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQD70pjA88xi_f9B-GUbD-AsKTL2xATwOENYErPXJrVrdbTsJPqLkGr53lC6pLZh-fgVQcfb75p-Fy5xM2SJviOTF4GOSjkm7_lWFFskaC3hY_fvEvafXGIkEO1RZv4XvxF3cF-ek8bZMQId3dGPWIdA5iNYM23CbQGcfNHTBFnVAzZG8YcutMo5F_sasSxgfHpqaw37FN5qmwxaA_b5thpmsg5FlKprqx-rTk80NWww==', start_index=8850)
Annotation(end_index=9174, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPczILmll8oZeIfzIQFqY5OuZ2Lg8Ax57W1p30jwXKB482qiXLeKRbaM8JtLZ4jzah3Qftzqdj4oXmKcsHv_lp44GvG14ZN12iJMrl8y1fhBpmznEuWnH5Xc8=', start_index=9160)
Annotation(end_index=9174, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrrPCBvnl6KHk7yj6rDRnwiw1eHUKJixutMvySKz1uLCHv4vtH_Ni9MLBYS0FdP3ag8lDfuXXe5kcZLUHcrONSq840LDgYdxJK4iCfq-faU5z1WBBl5twiIpN3m0Piti92z_8qt96obDbwoetdznbx7C3htw==', start_index=9160)
Annotation(end_index=9569, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPczILmll8oZeIfzIQFqY5OuZ2Lg8Ax57W1p30jwXKB482qiXLeKRbaM8JtLZ4jzah3Qftzqdj4oXmKcsHv_lp44GvG14ZN12iJMrl8y1fhBpmznEuWnH5Xc8=', start_index=9555)
Annotation(end_index=9569, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVadtUls5Pzm3zWLQwE4ZnuokBksStu44OTW-BA-MWvhCV_CDyY-IU3-uQCoWofCt9oL0FV5qPysggja27ysHWLdm4DZlulAT4TEkZZvX0695HJc4BLxHduDMPxPEuiPtpRHBLKPZaMf0HtkK-4dIm_bFL5lLnl1PUIZUrdHjL5SiTU8KZgk1_prEmbws8Mct2oju1qPu7ASW6k9FVwxTHwSXv', start_index=9555)
Annotation(end_index=9904, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMfrNZWQE8CIyhl7uMTU19QcFGpkpBkAWX6_A1cb6jL2HcWiypbGn02CCkT_29b7R5HRvaKi3KcM0ASNhhGMnjTl7j82QGdpeAhfwj3robbwPuGnr_RDxTe0ZuHM6U12rE', start_index=9890)
Annotation(end_index=9904, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQD70pjA88xi_f9B-GUbD-AsKTL2xATwOENYErPXJrVrdbTsJPqLkGr53lC6pLZh-fgVQcfb75p-Fy5xM2SJviOTF4GOSjkm7_lWFFskaC3hY_fvEvafXGIkEO1RZv4XvxF3cF-ek8bZMQId3dGPWIdA5iNYM23CbQGcfNHTBFnVAzZG8YcutMo5F_sasSxgfHpqaw37FN5qmwxaA_b5thpmsg5FlKprqx-rTk80NWww==', start_index=9890)
Annotation(end_index=10605, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcbOuMhRP-x0V4GhG-Rd5jsZSppM2utRxSf2k40jJxJrDeOMtZpxpHPD3r1IM8G5x2sIcclaewjSajWcXS5d6H72a1oIFBcoO6bGKj6pMj-Q64Xarx12FJeTL8nOML04bRVQMkdQRhnJdMwYj-WZxmQ7P44PqtI6EwK6bAwcP6krv9Ybz9zk9JAoVPLwP4W4RHUzMozZ34Wb_ia-sKimomRtV7-lWJ3mo=', start_index=10591)
Annotation(end_index=10605, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH35bQmpvtD74x-oK35XAWbMse-eSI8OiXZnTOy_jPZ8KNZ8ZKXMJzanyb2pd0sXJwz8pX5mLeiqVh3vqJiUDf70aXfb3kHtAw5l2FYuPbv4MYv7vUb8lIlTP0XNaVjFX8-LnSNG7zHGjG2Pp1VUKYk46bWETPAyx-gB1UgUuUVFP8f4gT_qfc1ZQGR7KpcJBd8gM3ibJm_zzva', start_index=10591)
Annotation(end_index=10868, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOw3PbXvWU0QM5yF5sbWxdANW5SYCZAnVKcX-lync246UzCdcDUxc4VguXqX3_m1TZx4lS53QxPsA4prUVo9i9HjW9m-agLMGuzVHvaLhoBAb7uX3h1EASHodDdbOzjJfB6Ng=', start_index=10858)
Annotation(end_index=11218, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcbOuMhRP-x0V4GhG-Rd5jsZSppM2utRxSf2k40jJxJrDeOMtZpxpHPD3r1IM8G5x2sIcclaewjSajWcXS5d6H72a1oIFBcoO6bGKj6pMj-Q64Xarx12FJeTL8nOML04bRVQMkdQRhnJdMwYj-WZxmQ7P44PqtI6EwK6bAwcP6krv9Ybz9zk9JAoVPLwP4W4RHUzMozZ34Wb_ia-sKimomRtV7-lWJ3mo=', start_index=11204)
Annotation(end_index=11218, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOw3PbXvWU0QM5yF5sbWxdANW5SYCZAnVKcX-lync246UzCdcDUxc4VguXqX3_m1TZx4lS53QxPsA4prUVo9i9HjW9m-agLMGuzVHvaLhoBAb7uX3h1EASHodDdbOzjJfB6Ng=', start_index=11204)
Annotation(end_index=11410, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3xqJal8SaI8MN-hxvQIWtLOP5N37nYMsMw85XLXvPS840ISKtTWaxBTQjhwLPjoGd1seOO7hehwxuxb_csJADz8s0iBZyhC-QOLrLDTYcDw2d8HRDF-9LF3KVeUvf9FRLlJFXwkL8W_ZLr8FpzwdUTxi10oB7FWgLmQ==', start_index=11396)
Annotation(end_index=11410, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkxTVtpprghq1S3lfukYN_YUHJJh9UHXCxtsv93MXwdHA4LwVhs6eRPtclNOQXkPxIU6j8QVFJaMjSHl5Pdp7uGlfP__e8ea2lrd1zsWAOGMZqamZxDJagGkY0', start_index=11396)
Annotation(end_index=11647, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3xqJal8SaI8MN-hxvQIWtLOP5N37nYMsMw85XLXvPS840ISKtTWaxBTQjhwLPjoGd1seOO7hehwxuxb_csJADz8s0iBZyhC-QOLrLDTYcDw2d8HRDF-9LF3KVeUvf9FRLlJFXwkL8W_ZLr8FpzwdUTxi10oB7FWgLmQ==', start_index=11637)
Annotation(end_index=11975, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3EePhaSaYlscC5dWrCjUoc1g3AfztxldSfxM-nH9zMbxIZseixzRiwvnN5iHUbRhJFeTrGTCDaHR-pim2fmz1q3pVy6wxiJrbcFsaIw2zT6qzFcupFLPr7X0FHX6L8UV7_BD23QfVhVNL9uoW24IuvfX2uEqSYaPmgfYtS87B7SCds9Gu224RbUc9J5DgziSTAHXhNqjt4djSy4xISfmfkosk2cRXte904B4U4k4tYPreuOMgF6mYog1_enzejjeijhk2Np6rJQ30EDbvc9rJ7HIBh9TEjw1k_LSRHrX0KQ==', start_index=11961)
Annotation(end_index=11975, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHa8nqCZ5_OUDn4UiGNye8qe_FzT97ntVrazM9Y2RtWbG9pmlFcmBSNdSfi3pJY2vRxUZVk4GG_U5HR0A9iWgElOxT-nGWxvgTnrMSHsf61tBTLheCPrqPb04BeYvWDsH2uN1G_EvMiMfBI3hVShkvtjmnJnTSP9iAj-IPcNoXI7kAnykxGOb15J1H_Tt3vR4WDpdy7uiU620EWfmPweAUQIXPVbbnhupUkDYjN5UE-Ylac', start_index=11961)
Annotation(end_index=12372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMfrNZWQE8CIyhl7uMTU19QcFGpkpBkAWX6_A1cb6jL2HcWiypbGn02CCkT_29b7R5HRvaKi3KcM0ASNhhGMnjTl7j82QGdpeAhfwj3robbwPuGnr_RDxTe0ZuHM6U12rE', start_index=12358)
Annotation(end_index=12372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQD70pjA88xi_f9B-GUbD-AsKTL2xATwOENYErPXJrVrdbTsJPqLkGr53lC6pLZh-fgVQcfb75p-Fy5xM2SJviOTF4GOSjkm7_lWFFskaC3hY_fvEvafXGIkEO1RZv4XvxF3cF-ek8bZMQId3dGPWIdA5iNYM23CbQGcfNHTBFnVAzZG8YcutMo5F_sasSxgfHpqaw37FN5qmwxaA_b5thpmsg5FlKprqx-rTk80NWww==', start_index=12358)
Annotation(end_index=12661, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGD2Wmh4I6uooo7C1-gK6tWWiahgyaJb3uXsQPPfZTC9pYmOXVocmq9di12sKJFgc2ETv8jRBEC7DuXb6kRzskinyOxA8hHzZ9AJXuTu9zKmUozlESElQkNGjX1ysqUJlAY6Hk1l6Zprpc5cZ4Qd4HRUx1kqdcwfqcfZYY5aOrox0u32q3MKBK860M0KFlH622RBdtnptdMJNf7ksitqtVQYRfNTjXgzqNtcqQ40YSJEro50d8NoUC', start_index=12651)
Annotation(end_index=12963, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2rpZGHg7GM3u5btITyZIurOUmJ_jC3KMiocQrr7KdcRRB_QHRwybws-y5b9cUcFsyJNMiL7pCColxsy0e3n7mJFjYTDBwIRUcm_CcP1v58nUxtwvXVeyWJlvaOexUXcOxTkV17wdEib_3Mfo=', start_index=12954)
Annotation(end_index=13699, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPczILmll8oZeIfzIQFqY5OuZ2Lg8Ax57W1p30jwXKB482qiXLeKRbaM8JtLZ4jzah3Qftzqdj4oXmKcsHv_lp44GvG14ZN12iJMrl8y1fhBpmznEuWnH5Xc8=', start_index=13689)
Annotation(end_index=13889, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYGv-sKTJjfBOetPcypyUeyjLoc_pBGrCpbZoVIgjhxe-JV5hxGZc-ejMphcJ2cJP4gsSlYCU1CFz4g7AAtRO-oSwteWxc8g04h6wT6Y5ESplly-OgjzmLQe0cJsLHIhESDDXm7xo-DOOHJxRVK-P55aNHqiv1QTLkZd6i', start_index=13879)
Annotation(end_index=14132, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAQRT1yBkz6CkwoaHeYDFIfz78dpfYVTKHcUc2co027FSBP0_v1RXaKLHP350zKEH_i5UE3P5I3XIG_tUdKldK4lcVoExrJyFnH4CJC6qYtvQKbbPtiZz-poSHjhX8VPjqBJl0HPaQQ5i9A5eDH7EHZI-6t2pOs_9C8A==', start_index=14118)
Annotation(end_index=14132, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrrPCBvnl6KHk7yj6rDRnwiw1eHUKJixutMvySKz1uLCHv4vtH_Ni9MLBYS0FdP3ag8lDfuXXe5kcZLUHcrONSq840LDgYdxJK4iCfq-faU5z1WBBl5twiIpN3m0Piti92z_8qt96obDbwoetdznbx7C3htw==', start_index=14118)
Annotation(end_index=14462, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0dZfLYbMH_uNHF39O6DnS3dhCfokz9KXdMtzuvzAtFIrQxYQRPGASmT01v2-5YoM9PTJ7pQRv2qOJzsvYBAOTOpn4mtIX6uO_Gi4KWnLlZ2I4GtPZyk-g6bvfaIkfOhYJsVDXTHVqtAzm96LXV7kxyK3ltW308LSUnHToEEhuuw4tfJ4BdBhOVr4=', start_index=14452)
Annotation(end_index=15245, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe8VYZKaot0EpcFCDXq9p-weslcS3h8PWM8FhEi028rwfdOvhdo_uOjqF1k4WeZXzE0U0BGWpmjELADOfet_x97MeOZQ6I_dvV9beB6XRx4m7msCoeg0KyUhuGZw==', start_index=15235)
Annotation(end_index=15491, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQEc3woY1a2ahsoADJAnQuNWDLwqx_Gh8WJsuWzjwVAulSjUHmZJp4LaA2aIx4Lp7JcT0UJYYN2UoZFBh7I91PlKbECoyeA3IPWLhq6G80iOSAUOWAmT4O2gHsQ9XNudbauXLR0OgDcvtvD8SKiB-GgolC-BjpnGFQaKVUspGT', start_index=15481)
Annotation(end_index=15947, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGksYRk32uby8SAt39psFUgHtKR8ftCHsK7p094KTPHSD5FBfc2HF277IYqcELafE9BG24qBkCeJ2NIK5II_4RI2gcN0M8H6BY6cYougwQGzVWeqL3z5aE0h92xhAHxIi-2Khf5ZM=', start_index=15937)
Annotation(end_index=16408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiLhcEIabBY80WCTmaGDyyMiuNRxQA5mEkl010NQ3MrNky1ALjI0AOpYyqnOL-jyrWPQLOGtFIv9FP6j95Ncxh6IsrqIuRegJnposzuBP1vbMcTRw3HZoK6wky4hRY5RFOUSbxb1Xn1yEO3w==', start_index=16390)
Annotation(end_index=16408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwIKpgyW_ICu9qxvDMiZA2Pu_KdLOt3diUbNyOVXDy51s8oTYMMpnPWKh1pP1Tj2fEnqVSJWAk7Oym8rKl7zz2_mXSAnUn0oRzVZV1obWA2hbsjWNNLdE1Evhx', start_index=16390)
Annotation(end_index=16408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH35bQmpvtD74x-oK35XAWbMse-eSI8OiXZnTOy_jPZ8KNZ8ZKXMJzanyb2pd0sXJwz8pX5mLeiqVh3vqJiUDf70aXfb3kHtAw5l2FYuPbv4MYv7vUb8lIlTP0XNaVjFX8-LnSNG7zHGjG2Pp1VUKYk46bWETPAyx-gB1UgUuUVFP8f4gT_qfc1ZQGR7KpcJBd8gM3ibJm_zzva', start_index=16390)
Annotation(end_index=16675, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGh8tUEsS1UW_b1FluxYnR0wudzUZSnOsnMtrr8Qd5KITKFcRTl5-kGYVfYV00mpimjLmoDjO9gJC8_OObU7f_ftT6HrfC_zkHmsgi44NNKT_Z-sbjbauISa7fHjjZTrsGETTm848b5rINSw21-T2R_Ww==', start_index=16666)
Annotation(end_index=17090, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnwfbPHylxh6Pe9087Q8gthpvnDdmEv7kMyJxZCpuACQ6kWtg32pD7OEqBMnGfCJwQSavrRzcSPLQOCuKAQiIDYmvmfsoGZ-_QbLFBoJ38pBM0pFDKUD8hH2V-n0weSF43AC3qkQ0oCIF3sf5C5GiUFQJM52O_t695qd-jWocY0cSoVDUXPX3AR0nHpaiwv2DhjKcMXQqNrnMlfYa6s1z9OU4mtuUCyMMNakP8tn6aicxErtb-6MXN4BCpu-tZ4_nnp7PBjON7', start_index=17081)
Annotation(end_index=18119, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvK0kjanXmBJV6hNZ_uqMalMg4_BWOioDgg97n4nYJKMM4b2oL_korNaZV3sn4KU0NAX22byc3E3HIRzIaCJrTDTvigqzHZbJmTVDK9PVquJYdlbNnKHYkTzUR6QNE2s-zhdT2JWq-vJpXMs126yArMtwB1zLNH_BfGKUP6Yryns3jPvksi0On7zxWnr9o4nm5iksF2cZqSw5HoLRgw6kPjlyF8fO-6zFEN8Rp0pp2pWrcKYQsiiwL1g==', start_index=18110)
Annotation(end_index=18222, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-wXJne1pmHkCv4M3o6Ck2jqg2km11xblK6YRZ8tWIkfMWvyAjgE1Xi5PvL3D5WMjV7DBmuuxIrKvAB_6yuzq5dbBQGQdqDXSO54KTK-q2Dy6FuGvjx41IJuWdxfsc9c8cBXo22ODuzQ-xK1qQvYP5YRzPvhdfMsmb2WWtmI0VfAM-TnW074DDP9HnTwC59g==', start_index=18213)
Annotation(end_index=18287, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHz7YmDGBBUyPjK0IofVpp_xmmIMq4nczO5EkjQYSp9j-I5_6IfO4cMLtoVvV_6lULnkb9PBEPz8s7_d13c2DXGkMAa_W388bbP19OpOnPLX6pGI-VtMPXx-qpKfgQBg==', start_index=18277)
Annotation(end_index=18362, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGksYRk32uby8SAt39psFUgHtKR8ftCHsK7p094KTPHSD5FBfc2HF277IYqcELafE9BG24qBkCeJ2NIK5II_4RI2gcN0M8H6BY6cYougwQGzVWeqL3z5aE0h92xhAHxIi-2Khf5ZM=', start_index=18352)
Annotation(end_index=18445, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFuGW8xTXRpN1mlqP5q579aT5sMnadE7NSQx-E5yrqJUncWrpmfpUsdMiM1vwbn33_A9vx-osbBsB6WziDkjtWmOrL9gvG1uSysDYbuZ2CEj1DB_DakKnisIAEBko1LoEfY_MXdiTzYP1z_6G7S5VPYldP_wusw4L0gAtxORr95a8ijAFS_kxaWWhF7TL3YWKr2A73aix15oRKv8zfxfPDjwpGREkXQM9PeF5hXHH9RFMgjsFp', start_index=18436)
Annotation(end_index=18548, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwIKpgyW_ICu9qxvDMiZA2Pu_KdLOt3diUbNyOVXDy51s8oTYMMpnPWKh1pP1Tj2fEnqVSJWAk7Oym8rKl7zz2_mXSAnUn0oRzVZV1obWA2hbsjWNNLdE1Evhx', start_index=18538)
Annotation(end_index=18600, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnwfbPHylxh6Pe9087Q8gthpvnDdmEv7kMyJxZCpuACQ6kWtg32pD7OEqBMnGfCJwQSavrRzcSPLQOCuKAQiIDYmvmfsoGZ-_QbLFBoJ38pBM0pFDKUD8hH2V-n0weSF43AC3qkQ0oCIF3sf5C5GiUFQJM52O_t695qd-jWocY0cSoVDUXPX3AR0nHpaiwv2DhjKcMXQqNrnMlfYa6s1z9OU4mtuUCyMMNakP8tn6aicxErtb-6MXN4BCpu-tZ4_nnp7PBjON7', start_index=18591)
Annotation(end_index=18718, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLmDhRydyL999pDOLslhYjVJlq-kWEg8XF7SG_TZXOGrv-PAKvdhYKQ-LqUiu-5VyAIc43lgBwOmHQoIQBP4I6ZV_T0lsd4GttdQELg4aM22kWjm46fcLcUcXWbeLV6SMfRHHp_mhApjxaybXY7cMVdxg-QSIa_nyaptWVov1bw6Tzo--JMfkpB4R3j8k=', start_index=18708)
Annotation(end_index=18776, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2rpZGHg7GM3u5btITyZIurOUmJ_jC3KMiocQrr7KdcRRB_QHRwybws-y5b9cUcFsyJNMiL7pCColxsy0e3n7mJFjYTDBwIRUcm_CcP1v58nUxtwvXVeyWJlvaOexUXcOxTkV17wdEib_3Mfo=', start_index=18767)
Annotation(end_index=18852, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIeoLUnMB-TABZ2rOUnURwKVe_YIUbNqVO2OQcEovnPyE2wWTOk6e2x6K5iztj602uXa2Nj6XWsBQbuDQM3i4yBRFL9XwTnroWqtRnnXwCT1SIsP29aLZRk2UFfat7uR2YsfyZoZkDF2iVAdWyJmYWNZVtQChmYOYu9COx95LN9bZKt609QOMYIahLRQ==', start_index=18842)
Annotation(end_index=18956, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3xqJal8SaI8MN-hxvQIWtLOP5N37nYMsMw85XLXvPS840ISKtTWaxBTQjhwLPjoGd1seOO7hehwxuxb_csJADz8s0iBZyhC-QOLrLDTYcDw2d8HRDF-9LF3KVeUvf9FRLlJFXwkL8W_ZLr8FpzwdUTxi10oB7FWgLmQ==', start_index=18946)
Annotation(end_index=19037, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMfrNZWQE8CIyhl7uMTU19QcFGpkpBkAWX6_A1cb6jL2HcWiypbGn02CCkT_29b7R5HRvaKi3KcM0ASNhhGMnjTl7j82QGdpeAhfwj3robbwPuGnr_RDxTe0ZuHM6U12rE', start_index=19027)
Annotation(end_index=19136, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5dGzYBahU6HwxtHRSk3Tf85w-9x18cpoKspJJUfVQK2lbYjC5Nbp2M6ab__4yA5C5LJLz4m4dl4JVaGfKQFeo9Ce07GD0cz6JhqdvGoGbahnFg9EBtZRoKRS7Hhvaj6vleRg38SUMUmgWeO5Sr3QIncTlD_ycTuXz9TiI6uRARDyYJp-6Q5VBxerP79uiTDDV7aFUY8Q_N6Y8WKOmjNP-k5668rcs75EATqkwNaVCV0XT3v1ttcWjiKrq9YL9-PBPxiar', start_index=19126)
Annotation(end_index=19211, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkvg8twb3fuWWLjumIothLGa-A26PsF-umVxV55c4-gzX_si9g9lGPXvN9pPAf3mPEuq546j8T7XeWSSF8xZWOzY-vq_B_uDgrP0FS5rs3QBK5JN0DoT-Frbw=', start_index=19201)
Annotation(end_index=19279, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHa8nqCZ5_OUDn4UiGNye8qe_FzT97ntVrazM9Y2RtWbG9pmlFcmBSNdSfi3pJY2vRxUZVk4GG_U5HR0A9iWgElOxT-nGWxvgTnrMSHsf61tBTLheCPrqPb04BeYvWDsH2uN1G_EvMiMfBI3hVShkvtjmnJnTSP9iAj-IPcNoXI7kAnykxGOb15J1H_Tt3vR4WDpdy7uiU620EWfmPweAUQIXPVbbnhupUkDYjN5UE-Ylac', start_index=19269)
Annotation(end_index=19375, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3xqJal8SaI8MN-hxvQIWtLOP5N37nYMsMw85XLXvPS840ISKtTWaxBTQjhwLPjoGd1seOO7hehwxuxb_csJADz8s0iBZyhC-QOLrLDTYcDw2d8HRDF-9LF3KVeUvf9FRLlJFXwkL8W_ZLr8FpzwdUTxi10oB7FWgLmQ==', start_index=19365)
Annotation(end_index=19456, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPczILmll8oZeIfzIQFqY5OuZ2Lg8Ax57W1p30jwXKB482qiXLeKRbaM8JtLZ4jzah3Qftzqdj4oXmKcsHv_lp44GvG14ZN12iJMrl8y1fhBpmznEuWnH5Xc8=', start_index=19446)
Annotation(end_index=19558, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjwO2g7k4UCPXpaT3MXa-FKe7WzHorVtbTlBnSVmIbKwaiylKfbXKlF8rwyQgft3ds4zJ1dQCDVnyyhTiWLFG8dD_k_ASYI-vZvAWGt3oZcLx9yBV4o44Qc9IlgzlF3beHQyg6u7528dEFWuVVHAsXLjbOIRaaiH5vTEZD7FL4WFuULi0ltbG9eh5lMpCeL-qs93Qwm9zcjXJD8Q==', start_index=19548)
Annotation(end_index=19631, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHgHEwroUQl2vfVreLUIG72NJSSlubKomlaTYEKIXQTzxA32ALMQZx6I-eiy5V1Um5ffl6_wF0SThJu8Fv4HOryLoemo6dWG8JHMTpwv9d0dbTpqKtdIqVPTLnPPDXiqmhb8mam5BJv1V1nsGtfC8lkJnxnZ_PJqktjyT7hg==', start_index=19621)
Annotation(end_index=19680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxYuGnC90S5lRTT3T-3YVmAiUAoFTtgSJaAT3KiWWS4jCz8cbThq3lQ5bshFFBCx4ikyQKyKlmcQgwU_gA0piCp5qypuxOBATQVKxgvrtgY-Y3IgS3S6yLcjIRVVA=', start_index=19670)
Annotation(end_index=19747, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFstoB1ib5JPrC-aHbvQom1Wsa2IXr1eqT6Hm8_Rlfmzroi8Cr8Y9-VHdH50jjyH53fS13KCzAt3ZQaizBwX0v36hsFRJwAnMDGjVABNC4ELcHNEuUjt3nVeGqjHTHuWxjM', start_index=19737)
Annotation(end_index=19825, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGh8tUEsS1UW_b1FluxYnR0wudzUZSnOsnMtrr8Qd5KITKFcRTl5-kGYVfYV00mpimjLmoDjO9gJC8_OObU7f_ftT6HrfC_zkHmsgi44NNKT_Z-sbjbauISa7fHjjZTrsGETTm848b5rINSw21-T2R_Ww==', start_index=19816)
Annotation(end_index=19905, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhWas57nvNEoR0AMeo9EEstDeIfPv9IQ_JmIph_reNt_dj6AgPOTENsGMXbt0I6I5nMq9HBCKgykgYBB4RD1xqXG2QRk4j1SxqnUqg7GYqL79CCwNgg0JpKKm1Do4SQCs8g0bNIccOuWtp9ow_fjuw4_XwCEP2LS8dRO-5a-qOWFPS6yxLcE6M9-NxloOyFVHHvME-QeGNunFFRPBKQ1HFKWK8KmTCDX_dZ9si75zf8JH8ttV2bOe8zpdAkacoEA9tZETap8Of9s_VgAtC4l2uhT2-H0TOdh1xzg==', start_index=19896)
Annotation(end_index=19984, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkxTVtpprghq1S3lfukYN_YUHJJh9UHXCxtsv93MXwdHA4LwVhs6eRPtclNOQXkPxIU6j8QVFJaMjSHl5Pdp7uGlfP__e8ea2lrd1zsWAOGMZqamZxDJagGkY0', start_index=19974)
Annotation(end_index=20073, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWJq8s4dbFBlPDOkN7vixWKY73jZcz-V0VNRXxvlYMUe2CasWOx7Cvo8SPyWvwWGz8LnomS7tK8c5SYeXFu6dBYGfxo71WV99_zd_hIs_00Lj91JYS5bWLt_EWacdL0qcRZS5M', start_index=20063)
Annotation(end_index=20124, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrnd81dwDdoGTuBHNgDqdcLawG_EhEXZabvGK2FfNiqEDoRtt98zy6u4vNwcgfm5ojLtv3S0QxYWuxvrEccXTLJKvGoV5hMj0J6ExoLaFGJtL5rg8sg8fm_7VhuDNPLcRAdMr5oiYByXyFS_GMI-6QsC3XnJ6TnuOBALBChMPMcu_skSSCc4XqZAVP3oimbBhj1ZOqFQQf8hwcfqLmzSC1VyR1qSuaH9L73jMWJg9DT__RoZ9I', start_index=20115)
Annotation(end_index=20222, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjPamJ1CAR1Z5qjEQnenEnnGx5iNc1fjVztZrFmQkMAkUoQNj6iyH4bPtj6VqxtbvFvvNKcHnuxGv2mdBwfbvrvVzPKhjzHONXgM-ufqr6CyiFvXwfjWDU_J5np4QkQeBtjxk-cPL_7KqW9u3YM-NxBCJuG-O0EPE=', start_index=20213)
Annotation(end_index=20298, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiLhcEIabBY80WCTmaGDyyMiuNRxQA5mEkl010NQ3MrNky1ALjI0AOpYyqnOL-jyrWPQLOGtFIv9FP6j95Ncxh6IsrqIuRegJnposzuBP1vbMcTRw3HZoK6wky4hRY5RFOUSbxb1Xn1yEO3w==', start_index=20288)
Annotation(end_index=20388, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe8VYZKaot0EpcFCDXq9p-weslcS3h8PWM8FhEi028rwfdOvhdo_uOjqF1k4WeZXzE0U0BGWpmjELADOfet_x97MeOZQ6I_dvV9beB6XRx4m7msCoeg0KyUhuGZw==', start_index=20378)
Annotation(end_index=20445, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQEc3woY1a2ahsoADJAnQuNWDLwqx_Gh8WJsuWzjwVAulSjUHmZJp4LaA2aIx4Lp7JcT0UJYYN2UoZFBh7I91PlKbECoyeA3IPWLhq6G80iOSAUOWAmT4O2gHsQ9XNudbauXLR0OgDcvtvD8SKiB-GgolC-BjpnGFQaKVUspGT', start_index=20435)
Annotation(end_index=20514, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrrPCBvnl6KHk7yj6rDRnwiw1eHUKJixutMvySKz1uLCHv4vtH_Ni9MLBYS0FdP3ag8lDfuXXe5kcZLUHcrONSq840LDgYdxJK4iCfq-faU5z1WBBl5twiIpN3m0Piti92z_8qt96obDbwoetdznbx7C3htw==', start_index=20504)
Annotation(end_index=20616, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQD70pjA88xi_f9B-GUbD-AsKTL2xATwOENYErPXJrVrdbTsJPqLkGr53lC6pLZh-fgVQcfb75p-Fy5xM2SJviOTF4GOSjkm7_lWFFskaC3hY_fvEvafXGIkEO1RZv4XvxF3cF-ek8bZMQId3dGPWIdA5iNYM23CbQGcfNHTBFnVAzZG8YcutMo5F_sasSxgfHpqaw37FN5qmwxaA_b5thpmsg5FlKprqx-rTk80NWww==', start_index=20606)
Annotation(end_index=20710, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH35bQmpvtD74x-oK35XAWbMse-eSI8OiXZnTOy_jPZ8KNZ8ZKXMJzanyb2pd0sXJwz8pX5mLeiqVh3vqJiUDf70aXfb3kHtAw5l2FYuPbv4MYv7vUb8lIlTP0XNaVjFX8-LnSNG7zHGjG2Pp1VUKYk46bWETPAyx-gB1UgUuUVFP8f4gT_qfc1ZQGR7KpcJBd8gM3ibJm_zzva', start_index=20700)
Annotation(end_index=20808, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOw3PbXvWU0QM5yF5sbWxdANW5SYCZAnVKcX-lync246UzCdcDUxc4VguXqX3_m1TZx4lS53QxPsA4prUVo9i9HjW9m-agLMGuzVHvaLhoBAb7uX3h1EASHodDdbOzjJfB6Ng=', start_index=20798)
Annotation(end_index=20848, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3xqJal8SaI8MN-hxvQIWtLOP5N37nYMsMw85XLXvPS840ISKtTWaxBTQjhwLPjoGd1seOO7hehwxuxb_csJADz8s0iBZyhC-QOLrLDTYcDw2d8HRDF-9LF3KVeUvf9FRLlJFXwkL8W_ZLr8FpzwdUTxi10oB7FWgLmQ==', start_index=20838)
Annotation(end_index=20928, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2rpZGHg7GM3u5btITyZIurOUmJ_jC3KMiocQrr7KdcRRB_QHRwybws-y5b9cUcFsyJNMiL7pCColxsy0e3n7mJFjYTDBwIRUcm_CcP1v58nUxtwvXVeyWJlvaOexUXcOxTkV17wdEib_3Mfo=', start_index=20919)
Annotation(end_index=21004, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPczILmll8oZeIfzIQFqY5OuZ2Lg8Ax57W1p30jwXKB482qiXLeKRbaM8JtLZ4jzah3Qftzqdj4oXmKcsHv_lp44GvG14ZN12iJMrl8y1fhBpmznEuWnH5Xc8=', start_index=20994)
Annotation(end_index=21068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGD2Wmh4I6uooo7C1-gK6tWWiahgyaJb3uXsQPPfZTC9pYmOXVocmq9di12sKJFgc2ETv8jRBEC7DuXb6kRzskinyOxA8hHzZ9AJXuTu9zKmUozlESElQkNGjX1ysqUJlAY6Hk1l6Zprpc5cZ4Qd4HRUx1kqdcwfqcfZYY5aOrox0u32q3MKBK860M0KFlH622RBdtnptdMJNf7ksitqtVQYRfNTjXgzqNtcqQ40YSJEro50d8NoUC', start_index=21058)
Annotation(end_index=21147, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0dZfLYbMH_uNHF39O6DnS3dhCfokz9KXdMtzuvzAtFIrQxYQRPGASmT01v2-5YoM9PTJ7pQRv2qOJzsvYBAOTOpn4mtIX6uO_Gi4KWnLlZ2I4GtPZyk-g6bvfaIkfOhYJsVDXTHVqtAzm96LXV7kxyK3ltW308LSUnHToEEhuuw4tfJ4BdBhOVr4=', start_index=21137)
Annotation(end_index=21216, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYGv-sKTJjfBOetPcypyUeyjLoc_pBGrCpbZoVIgjhxe-JV5hxGZc-ejMphcJ2cJP4gsSlYCU1CFz4g7AAtRO-oSwteWxc8g04h6wT6Y5ESplly-OgjzmLQe0cJsLHIhESDDXm7xo-DOOHJxRVK-P55aNHqiv1QTLkZd6i', start_index=21206)
Annotation(end_index=21309, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPczILmll8oZeIfzIQFqY5OuZ2Lg8Ax57W1p30jwXKB482qiXLeKRbaM8JtLZ4jzah3Qftzqdj4oXmKcsHv_lp44GvG14ZN12iJMrl8y1fhBpmznEuWnH5Xc8=', start_index=21299)
Annotation(end_index=21372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAQRT1yBkz6CkwoaHeYDFIfz78dpfYVTKHcUc2co027FSBP0_v1RXaKLHP350zKEH_i5UE3P5I3XIG_tUdKldK4lcVoExrJyFnH4CJC6qYtvQKbbPtiZz-poSHjhX8VPjqBJl0HPaQQ5i9A5eDH7EHZI-6t2pOs_9C8A==', start_index=21362)
Annotation(end_index=21453, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVadtUls5Pzm3zWLQwE4ZnuokBksStu44OTW-BA-MWvhCV_CDyY-IU3-uQCoWofCt9oL0FV5qPysggja27ysHWLdm4DZlulAT4TEkZZvX0695HJc4BLxHduDMPxPEuiPtpRHBLKPZaMf0HtkK-4dIm_bFL5lLnl1PUIZUrdHjL5SiTU8KZgk1_prEmbws8Mct2oju1qPu7ASW6k9FVwxTHwSXv', start_index=21443)
Annotation(end_index=21538, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3EePhaSaYlscC5dWrCjUoc1g3AfztxldSfxM-nH9zMbxIZseixzRiwvnN5iHUbRhJFeTrGTCDaHR-pim2fmz1q3pVy6wxiJrbcFsaIw2zT6qzFcupFLPr7X0FHX6L8UV7_BD23QfVhVNL9uoW24IuvfX2uEqSYaPmgfYtS87B7SCds9Gu224RbUc9J5DgziSTAHXhNqjt4djSy4xISfmfkosk2cRXte904B4U4k4tYPreuOMgF6mYog1_enzejjeijhk2Np6rJQ30EDbvc9rJ7HIBh9TEjw1k_LSRHrX0KQ==', start_index=21528)
Annotation(end_index=21628, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcbOuMhRP-x0V4GhG-Rd5jsZSppM2utRxSf2k40jJxJrDeOMtZpxpHPD3r1IM8G5x2sIcclaewjSajWcXS5d6H72a1oIFBcoO6bGKj6pMj-Q64Xarx12FJeTL8nOML04bRVQMkdQRhnJdMwYj-WZxmQ7P44PqtI6EwK6bAwcP6krv9Ybz9zk9JAoVPLwP4W4RHUzMozZ34Wb_ia-sKimomRtV7-lWJ3mo=', start_index=21618)
Annotation(end_index=21714, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfY-YpgAA7ux6eSUrOUBwV02LVaIu65ReRYqq12tauotatnBZX0j7g9SWxYd9AiGDxJiXY1lcDbdwcuxiPvJ6nA9LsdVho81jTJv3NsMt7X7fI6__0SbIsvRrBTiBaLZ41XHdsnyAos_92XYqUn0yUIRwkricgzEjrmHs5tINxMaIJwAk=', start_index=21704)
Annotation(end_index=21785, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGr2VJQVqouIqEZe8kwh8AzqfG8YGe1bP39sY9TdBXVCm2uNAPoPijFMKyb89xESPlzWKlJmbh4p0eH0yqUY8g90f5V7o6i9aWyoPKZU-0Hni8PCkcAs8ww8jeRlcuKCZobUKd-1b8rdaKlJD8E', start_index=21775)

## Sources
