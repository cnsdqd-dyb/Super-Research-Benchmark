# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 105def9b | **Time:** 319.65s | **Cost:** $1.04739
--------------------------------------------------------------------------------

# Network Topology Designs for High-Performance Computing: Resolving the Latency-Scalability Contradiction

**Key Points**
*   **The Core Conflict:** Traditional network topologies in High-Performance Computing (HPC) face a fundamental trade-off between **inter-node latency** (the time it takes for data to travel between nodes) and **scalability** (the ability to expand the system without prohibitive cost or performance degradation). Low-latency designs often struggle to scale, while scalable designs often incur higher latency or financial costs.
*   **The Shift to High-Radix:** The industry has largely moved away from low-radix topologies (like 3D Torus) toward high-radix, low-diameter topologies to address this contradiction. By using switches with many ports (high radix), networks can connect thousands of nodes with very few hops (typically 3 or fewer), keeping latency low even at exascale.
*   **Dragonfly and Dragonfly+:** The **Dragonfly** topology is currently the most prominent solution for resolving this contradiction in large-scale systems (e.g., Cray XC series). It uses a hierarchical design with fully connected groups to minimize global cable lengths and hops. Its evolution, **Dragonfly+**, integrates Fat-Tree structures within groups to enhance local scalability and bisection bandwidth, effectively balancing the trade-offs better than the original design.
*   **Theoretical Optima (Slim Fly & HyperX):** Emerging topologies like **Slim Fly** and **HyperX** offer theoretically superior characteristics. Slim Fly approaches the optimal network diameter (often just 2 hops) for a given router radix, maximizing data efficiency and minimizing latency. However, these come with challenges in deployment flexibility and cabling complexity compared to Dragonfly+.
*   **The Necessity of Adaptive Routing:** Resolving the latency-scalability contradiction in these low-diameter networks requires sophisticated **adaptive routing** (e.g., UGAL). Without it, these topologies are susceptible to severe congestion from adversarial traffic patterns, which negates their latency benefits.
*   **Fault Tolerance:** Modern high-performance topologies rely on rich path diversity. While Fat-Trees offer intuitive redundancy, topologies like Dragonfly and Slim Fly demonstrate surprising resilience to link failures due to their dense connectivity graphs, provided that the routing algorithms are fault-aware.

---

## 1. Introduction

The relentless pursuit of exascale computing has placed unprecedented demands on the interconnection networks that form the backbone of High-Performance Computing (HPC) clusters. As Moore’s Law slows and individual processor performance gains plateau, the primary avenue for increased computational power lies in massive parallelism—scaling systems to tens or hundreds of thousands of nodes. In this regime, the network is no longer merely a conduit for data; it becomes the critical determinant of system performance. The central challenge in designing these networks is a fundamental contradiction: the tension between **inter-node latency** and **scalability**.

Latency, the delay in communication between processing elements, directly impacts the performance of tightly coupled applications, such as weather modeling, molecular dynamics, and large-scale simulations. Scalability, the capacity to increase the system size, is essential for reaching higher peak performance (FLOPS). Historically, optimizing for one often compromised the other. Low-latency topologies like full meshes are unscalable due to cabling costs. Scalable topologies like 3D Tori or multi-tier Fat-Trees often introduce higher hop counts (and thus latency) or prohibitive hardware costs as the system grows.

This report provides an exhaustive analysis of network topology designs that best resolve this contradiction while ensuring data efficiency and fault tolerance. It argues that the transition from low-radix to **high-radix, low-diameter topologies**—specifically the **Dragonfly**, **Dragonfly+**, **HyperX**, and **Slim Fly** architectures—represents the current state-of-the-art solution. These designs leverage high-bandwidth switch ASICs to flatten the network, maintaining minimal hop counts even at extreme scales. We will explore the graph-theoretical underpinnings, routing implications, and practical trade-offs of these architectures, demonstrating how they maintain data efficiency through adaptive routing and ensure fault tolerance through path diversity.

## 2. The Latency-Scalability Contradiction in Traditional Topologies

To understand the solution, one must first analyze the limitations of traditional HPC network architectures. The "contradiction" arises from the physical and logical constraints of connecting $N$ nodes.

### 2.1 The Fat-Tree (Folded Clos) Paradigm
The Fat-Tree, or Folded Clos network, has been the de facto standard for data centers and many HPC clusters for decades [cite: 1, 2]. It is a hierarchical topology where bandwidth increases toward the root to prevent convergence (blocking).
*   **Scalability:** Fat-Trees are highly scalable in terms of bandwidth. A non-blocking Fat-Tree provides full bisection bandwidth, meaning any half of the network can communicate with the other half at full speed [cite: 3].
*   **The Contradiction:** To scale a Fat-Tree to thousands of nodes, one must add layers (tiers) of switches. A 2-tier tree might support hundreds of nodes, but a 3-tier or 4-tier tree is needed for thousands. Each additional tier adds switching hops, increasing static latency [cite: 1]. Furthermore, the cost scales super-linearly due to the massive number of cables and switches required. In particular, the top tiers require long, expensive active optical cables (AOCs) [cite: 1]. Thus, while scalable in bandwidth, Fat-Trees become cost-prohibitive and suffer from increased latency depth at exascale.

### 2.2 The Torus and Mesh Paradigm
Torus and Mesh topologies (e.g., 3D Torus used in IBM Blue Gene or Cray XK systems) connect nodes to their nearest neighbors in a grid.
*   **Cost Efficiency:** These are "direct" networks; switches are often integrated into the compute nodes, and cabling is mostly short and local. This makes them very cost-effective and scalable in terms of hardware [cite: 2].
*   **The Contradiction:** The diameter of a Torus network increases with the cube root (for 3D) of the number of nodes. As the system scales, the number of hops between distant nodes grows significantly, driving up latency [cite: 2, 4]. While "nearest-neighbor" traffic performs well, global traffic (e.g., FFTs, All-to-All collectives) suffers severely.

### 2.3 The Resolution: High-Radix, Low-Diameter Networks
The industry's response to this contradiction is the adoption of **high-radix routers**. By increasing the number of ports per switch (radix, $k$), the network can span more nodes with fewer hops. This leads to **low-diameter topologies**, where the maximum path length is fixed at a small number (e.g., 2 or 3) regardless of system size (up to a very high limit). This class of topologies—including Dragonfly, HyperX, and Slim Fly—forms the core of modern high-performance interconnects.

## 3. Dragonfly Topology: The Practical Standard

The **Dragonfly** topology, introduced by Kim et al. and popularized by Cray (now HPE) in the XC series (Aries interconnect), is designed specifically to exploit high-radix switches to reduce the network diameter and the number of expensive global optical links [cite: 1, 5, 6].

### 3.1 Architectural Design
Dragonfly is a hierarchical topology that divides the network into **groups** (sometimes called routers or sub-networks).
*   **Intra-Group:** Inside a group, routers are connected in a dense, high-bandwidth local topology. The original proposal often used a 1D Flattened Butterfly (all-to-all) or a 2D rectangular mesh [cite: 5, 7].
*   **Inter-Group:** Groups are connected to each other via long, global optical links. The global topology is typically a full mesh (all-to-all), meaning every group has a direct link to every other group [cite: 8, 9].

### 3.2 Resolving the Contradiction
Dragonfly resolves the latency-scalability contradiction through **hierarchical flattening**:
1.  **Latency:** By using a full mesh at the global level and a dense topology at the local level, the maximum hop count is typically 3 (1 local hop in source group + 1 global hop + 1 local hop in destination group) [cite: 10]. This remains true even as the system scales to hundreds of thousands of nodes, decoupling latency from system size to a large degree.
2.  **Scalability:** The topology minimizes the number of global cables required. Since global cables (optical) are expensive and local cables (copper) are cheap, Dragonfly optimizes cost by concentrating bandwidth locally and providing just enough global bandwidth for average-case traffic [cite: 1, 11].

### 3.3 The Adversarial Traffic Challenge
The trade-off for Dragonfly's efficiency is its sensitivity to traffic patterns. Because global links are "sparse" compared to a Fat-Tree (which is often over-provisioned), Dragonfly relies on the assumption that traffic is generally uniform or local.
*   **Adversarial Traffic:** Traffic patterns where all nodes in Group A try to send to Group B simultaneously can saturate the single (or few) direct links connecting them [cite: 5, 12]. This creates a bottleneck that can degrade throughput significantly compared to a non-blocking Fat-Tree.
*   **Solution:** This necessitates **non-minimal adaptive routing** (discussed in Section 7), which routes traffic through intermediate groups to utilize unused global bandwidth [cite: 5, 13].

## 4. Dragonfly+: Refining the Standard

**Dragonfly+** (also known as Megafly) is an evolution of the Dragonfly topology that addresses some of the scalability and performance limitations of the original design [cite: 9, 14].

### 4.1 Architectural Evolution
While the global structure remains a full mesh between groups, Dragonfly+ changes the **intra-group** topology.
*   **Intra-Group Fat-Tree:** Instead of a flattened butterfly or mesh, Dragonfly+ uses a bipartite or Fat-Tree structure within each group [cite: 9, 15].
*   **Structure:** Leaf switches connect to compute nodes, and Spine switches connect to other groups.

### 4.2 Advantages over Standard Dragonfly
1.  **Scalability:** The Fat-Tree structure within the group allows for a larger number of nodes per group compared to the all-to-all requirement of the original Dragonfly. This allows the total network size to scale further with the same switch radix [cite: 15].
2.  **Bisection Bandwidth:** The bipartite intra-group structure provides better local bisection bandwidth and eliminates some of the local bottlenecks found in the original Dragonfly [cite: 9].
3.  **Component Reuse:** It allows the use of standard Fat-Tree building blocks (switches and cabling patterns) within the rack, simplifying deployment [cite: 9].

Dragonfly+ is currently considered one of the best practical compromises, offering the low diameter of Dragonfly with the robust local performance of Fat-Trees. It is used in major systems like the **Niagara supercomputer** [cite: 14].

## 5. HyperX: The Multi-Dimensional Contender

**HyperX** is a generalization of the Flattened Butterfly topology, designed to provide a regular, scalable, low-diameter network [cite: 1, 16].

### 5.1 Architectural Design
HyperX is defined by a set of dimensions $L$ and the size of each dimension $S$. It can be viewed as a multi-dimensional grid where every node in a dimension is fully connected to every other node in that same dimension [cite: 16].
*   **Comparison:** A 1D HyperX is a full mesh. A HyperX with dimension size 2 is a Hypercube.
*   **Diameter:** The diameter is equal to the number of dimensions, $L$. Typically, $L=3$ or fewer is used for HPC to maintain low latency [cite: 1].

### 5.2 Performance Characteristics
Research comparing HyperX directly to Dragonfly and Fat-Tree has shown that HyperX can achieve higher throughput and lower latency in specific workloads, such as 27-point stencils used in physics simulations [cite: 16].
*   **Latency:** HyperX often exhibits lower latency during collective operations compared to Dragonfly due to its regular structure and high path diversity [cite: 16].
*   **Cost:** With appropriate dimensioning, HyperX can be cost-competitive with Dragonfly, potentially offering better performance for the same cost [cite: 16].

## 6. Slim Fly: The Theoretical Optimum

**Slim Fly** represents a radical departure from regular grid-based or hierarchical topologies. It is based on **MMS graphs** (Moore-Mckay-Sloane) to approximate the optimal solution to the degree-diameter problem [cite: 17, 18].

### 6.1 Architectural Design
Slim Fly is a topology with a diameter of **2**. This means any router can reach any other router in the entire network in at most 2 hops [cite: 17, 18].
*   **Graph Theory:** It uses mathematical constructions over finite fields to create a graph that maximizes the number of nodes for a given router radix and diameter [cite: 17].
*   **Efficiency:** By strictly limiting the diameter to 2, Slim Fly reduces the number of routers and cables required by approximately 25-50% compared to Fat-Trees and Dragonflies for the same performance [cite: 19, 20].

### 6.2 Resolving the Contradiction
Slim Fly arguably offers the "best" theoretical resolution to the contradiction:
*   **Latency:** It achieves the lowest possible static latency (diameter 2) for a given radix [cite: 18].
*   **Scalability:** It scales to very large sizes while maintaining this diameter.
*   **Cost:** It is more cost-effective and power-efficient than Fat-Trees and Dragonflies because it uses fewer components [cite: 17, 19].

### 6.3 Challenges
Despite its theoretical superiority, Slim Fly faces adoption hurdles:
*   **Cabling Complexity:** The cabling pattern is irregular and complex, making physical deployment and cable management more difficult than the structured Fat-Tree or Dragonfly [cite: 19].
*   **Rigidity:** The topology is mathematically precise; adding nodes incrementally is difficult. It usually requires deploying the full graph or specific sub-graphs, whereas Fat-Trees can be expanded pod-by-pod [cite: 19].

## 7. Data Efficiency and Routing: The Critical Enabler

A topology is only as good as its routing algorithm. For high-radix, low-diameter networks (Dragonfly, HyperX, Slim Fly), **data efficiency** is heavily dependent on how traffic is managed to avoid congestion.

### 7.1 The Necessity of Adaptive Routing
In a Fat-Tree, deterministic routing (like ECMP) works well because of the high bisection bandwidth. In Dragonfly and Slim Fly, minimal paths are few.
*   **UGAL (Universal Globally Adaptive Load-balanced):** This is the standard routing algorithm for these topologies. It chooses between a **minimal path** (shortest hop) and a **non-minimal path** (routing via a random intermediate node/group) based on congestion [cite: 5, 12, 21].
*   **Mechanism:** If the direct global link is congested (adversarial traffic), UGAL sends the packet to a random intermediate group, which then forwards it to the destination. This "Valiant Load Balancing" (VLB) spreads traffic across the global network, converting adversarial traffic into uniform traffic [cite: 5, 12].
*   **Efficiency:** This ensures high data efficiency by utilizing the aggregate bandwidth of the network rather than just the minimal-path bandwidth. Without UGAL, Dragonfly networks can saturate at very low loads (e.g., 50% or less) under adversarial patterns [cite: 5, 16].

### 7.2 Indirect Adaptive Routing
A challenge in Dragonfly is that the source router often does not know the congestion status of the global link (which might be attached to a different router in the group).
*   **Indirect Routing:** Advanced versions of UGAL (like UGAL-L or UGAL-G approximations) use local queue information or propagate congestion notifications to estimate the state of remote links [cite: 13, 15, 22]. This allows the source to make intelligent decisions without perfect global knowledge.

### 7.3 In-Network Computing
Data efficiency is also improved by offloading computation to the network. Technologies like **NVIDIA SHARP** (Scalable Hierarchical Aggregation and Reduction Protocol) perform collective operations (reductions, barriers) inside the switches [cite: 23]. This reduces the amount of data traversing the network and lowers latency for MPI collectives, which is particularly effective in hierarchical topologies like Fat-Tree and Dragonfly+.

## 8. Fault Tolerance

Fault tolerance is non-negotiable in clusters with thousands of cables and switches.

### 8.1 Path Diversity
*   **Fat-Tree:** Offers excellent fault tolerance. If a switch or link fails, traffic is simply re-hashed to one of the many other parallel paths moving up the tree [cite: 2].
*   **Dragonfly/HyperX:** These topologies are also highly resilient due to the richness of the graph. Even if a direct global link fails, the adaptive routing algorithm (UGAL) naturally redirects traffic through intermediate groups [cite: 24].
*   **Slim Fly:** Research indicates that Slim Fly is surprisingly resilient. Despite having fewer total cables, its graph properties ensure that connectivity is maintained even with multiple link failures, often performing better than Dragonfly in degraded states [cite: 25].

### 8.2 Fault-Tolerant Routing
To realize this resilience, the routing logic must be fault-aware.
*   **Dynamic Reconfiguration:** InfiniBand subnets managers or similar controllers detect faults and recompute routing tables.
*   **Local Misrouting:** In Dragonfly, if a local link fails, "local misrouting" can send traffic to another router in the same group to bypass the failure [cite: 26].

## 9. Comparative Summary

| Feature | Fat-Tree (Folded Clos) | Dragonfly / Dragonfly+ | HyperX | Slim Fly |
| :--- | :--- | :--- | :--- | :--- |
| **Latency (Hops)** | High (scales with tiers) | Low (typically 3) | Low (typically dimensions) | Lowest (2) |
| **Scalability** | High (bandwidth) | High (cost-effective) | High | High (but rigid) |
| **Cost** | High (cabling/switches) | Moderate/Low | Moderate | Lowest |
| **Traffic Sensitivity** | Low (robust) | High (needs adaptive routing) | Moderate | High (needs adaptive routing) |
| **Cabling Complexity** | High (but structured) | Moderate (hierarchical) | High | High (irregular) |
| **Fault Tolerance** | Excellent | Very Good | Very Good | Very Good |

## 10. Conclusion

To answer the query: **Dragonfly+ (and its variants)** currently represents the design that *best* resolves the contradiction between inter-node latency and scalability for practical, large-scale HPC clusters.

*   **Why Dragonfly+?** It successfully hybridizes the low global diameter of the Dragonfly (resolving latency) with the robust, non-blocking local structures of Fat-Trees (ensuring local scalability and ease of deployment). It leverages high-radix switches to minimize expensive global optical cabling while maintaining high bisection bandwidth.
*   **The Theoretical Challenger:** **Slim Fly** offers a superior theoretical resolution, achieving the mathematical limit of efficiency (diameter 2). However, its deployment complexity currently limits it compared to the more flexible Dragonfly+.
*   **Ensuring Efficiency and Tolerance:** Regardless of the chosen topology, the resolution of the contradiction is incomplete without **adaptive routing (UGAL)** to handle adversarial traffic and ensure data efficiency, and **rich path diversity** to guarantee fault tolerance.

In the exascale era, the "best" topology is no longer a static wire map but a dynamic system where a high-radix physical layer (Dragonfly+/Slim Fly) is tightly coupled with intelligent, adaptive routing logic.

---

## 11. Detailed Analysis of Topologies

### 11.1 Fat-Tree: The Baseline
The Fat-Tree topology, rooted in the Clos network design, has long been the standard for high-performance computing. Its primary strength lies in its **non-blocking** nature. In a full bisection bandwidth Fat-Tree, the bandwidth available at the root is equal to the bandwidth at the leaves [cite: 3]. This ensures that traffic patterns do not suffer from inherent topological bottlenecks.

However, the Fat-Tree illustrates the latency-scalability contradiction vividly. To connect more nodes, one must add vertical layers (tiers) to the tree.
*   **2-Layer Tree:** Connects $k^2/2$ nodes (where $k$ is switch radix).
*   **3-Layer Tree:** Connects $k^3/4$ nodes.
*   **Latency Penalty:** Each layer adds switch traversals. A packet in a large 3-level tree might traverse 5 or 6 switches (up and down).
*   **Cost Penalty:** The number of cables and switches grows super-linearly. Crucially, the top-tier links are almost always long-distance, requiring expensive Active Optical Cables (AOCs) or transceivers [cite: 1]. In a system with tens of thousands of nodes, the cost of the interconnect can exceed the cost of the compute nodes themselves.

### 11.2 Dragonfly: Breaking the Hierarchy
The Dragonfly topology was explicitly designed to break the cost/latency curve of the Fat-Tree. By exploiting **high-radix routers** (e.g., 64-port, 128-port switches), Dragonfly flattens the network [cite: 1, 6].

**Structure:**
1.  **Groups:** Routers are clustered into groups. Inside a group, routers are connected via a dense electrical network (copper). This is cheap and high-bandwidth.
2.  **Global Links:** Groups are connected via optical links. The key innovation is that *each group connects directly to every other group* (in the canonical implementation).
3.  **Virtual Router:** The group acts as a single, massive "virtual router" with a very high radix.

**Resolution of Contradiction:**
*   **Latency:** A packet travels Source -> Source Group Router -> (Global Link) -> Dest Group Router -> Dest. This is a maximum of 3 global hops (conceptually), often fewer physical hops depending on the intra-group routing [cite: 10].
*   **Scalability:** The number of global optical links is minimized. Instead of a massive spine layer (as in Fat-Tree), the global links are distributed among the groups. This reduces the cost of the network significantly—estimates suggest a 20-50% cost reduction over Fat-Trees for large systems [cite: 11].

**The "Catch" - Adversarial Traffic:**
Dragonfly is not non-blocking in the same way a Fat-Tree is. The bandwidth between any two specific groups is limited (often just one or a few links).
*   **Uniform Traffic:** Traffic is spread randomly; the probability of two nodes needing the same inter-group link is low. Performance is excellent.
*   **Adversarial Traffic:** If all nodes in Group 0 send to Group 1, they must share the single link connecting G0 and G1. Throughput collapses.
*   **Mitigation:** This is where **Adaptive Routing** becomes part of the topology design. The network *must* detect this congestion and route traffic G0 -> G2 -> G1. This "non-minimal" path doubles the bandwidth usage but bypasses the bottleneck [cite: 5, 12].

### 11.3 Dragonfly+: The Hybrid Solution
Dragonfly+ (Megafly) addresses the limitations of the intra-group topology in the original Dragonfly.
*   **Original Dragonfly:** Used a 1D Flattened Butterfly or Mesh inside the group. This required all-to-all connections between routers in a group, which limits the group size (and thus total scalability) based on switch radix [cite: 9].
*   **Dragonfly+:** Uses a **Fat-Tree** inside the group.
    *   **Benefit 1:** Decouples group size from router radix more effectively. A 2-level Fat-Tree inside a group can support many more nodes than a full mesh of the same radix switches [cite: 15].
    *   **Benefit 2:** Better local performance. The bipartite structure of the Fat-Tree is better at handling local traffic variations than the flattened butterfly [cite: 9].
    *   **Benefit 3:** Scalability. Dragonfly+ can scale to over 1 million nodes with current switch radices, surpassing the practical limits of standard Dragonfly [cite: 15].

### 11.4 Slim Fly: The Mathematical Limit
Slim Fly is a topology designed to be "diameter optimal."
*   **Concept:** For a given router radix $k$ and a number of nodes $N$, what is the minimum possible diameter? The Moore Bound gives a theoretical limit. Slim Fly constructs graphs (MMS graphs) that approach this limit for Diameter = 2 [cite: 17].
*   **Structure:** It connects routers in a specific, mathematically derived pattern that ensures any router reaches any other in 2 hops.
*   **Comparison:**
    *   **vs. Dragonfly:** Dragonfly is Diameter 3 (global). Slim Fly is Diameter 2. Slim Fly uses fewer routers and cables for the same number of endpoints [cite: 19].
    *   **vs. Fat-Tree:** Slim Fly has much lower latency and cost.
*   **Fault Tolerance:** Research by Besta et al. [cite: 25] shows that Slim Fly is highly resilient. Because the graph is an "expander graph" (highly connected), removing a link rarely partitions the network or significantly increases path length.
*   **Implementation:** The first real-world deployment of Slim Fly (200 servers) demonstrated that it outperforms non-blocking Fat-Trees in scalability and cost while offering comparable performance [cite: 19, 20]. However, the cabling is non-intuitive (no clean "spine" and "leaf" layers), which complicates physical installation and maintenance.

## 12. Routing Protocols: The Nervous System

The hardware topology provides the *potential* for efficiency; the routing algorithm delivers it.

### 12.1 UGAL (Universal Globally Adaptive Load-balanced)
UGAL is the standard for Dragonfly and similar topologies.
*   **Algorithm:** For a packet from $S$ to $D$:
    1.  Identify the **Minimal Path** ($P_{min}$).
    2.  Identify a **Non-Minimal Path** ($P_{non-min}$) via a random intermediate group $I$.
    3.  Estimate the latency/congestion on both.
    4.  Select the path with the lower estimated cost [cite: 5, 21].
*   **Challenges:**
    *   **Local Information:** The source router $S$ might not know the congestion on the link between $S$'s group and $D$'s group if that link is attached to a different router in $S$'s group.
    *   **UGAL-L (Local):** Uses local queue lengths as a proxy. This can be inaccurate [cite: 22].
    *   **UGAL-G (Global):** Assumes perfect global knowledge (theoretical).
    *   **Practical Solutions:** Modern implementations (like Cray Aries or specialized InfiniBand routing) use mechanisms to propagate congestion information or use "indirect" metrics to approximate UGAL-G [cite: 13, 22].

### 12.2 Progressive Adaptive Routing
In Dragonfly+, routing can be further optimized. Since the intra-group topology is a Fat-Tree, standard adaptive routing (like in InfiniBand) works well locally. For global traffic, the system must balance between the multiple spine switches available to exit the group [cite: 15].

## 13. Fault Tolerance and Reliability

In a system with 50,000 nodes, components fail daily. The topology must absorb this.

*   **Graceful Degradation:** High-radix topologies like Dragonfly and Slim Fly degrade gracefully. The loss of a single global link reduces the bandwidth between two specific groups but does not disconnect them, as traffic can be routed via intermediate groups (just like adversarial traffic) [cite: 24].
*   **Subnet Management:** In InfiniBand clusters (common for Dragonfly+), the Subnet Manager (SM) recalculates routing tables upon fault detection. This can take time.
*   **Hardware-Level Resilience:** Some architectures (like Cray Aries) have hardware-level adaptive routing that can route around failed links packet-by-packet without waiting for a global reconfiguration [cite: 27].

## 14. Conclusion: The Verdict

The **Dragonfly+** topology stands out as the most balanced solution for modern HPC clusters.
*   **Resolving Latency:** It maintains a low network diameter (typically 3 hops), ensuring low latency for MPI communications.
*   **Resolving Scalability:** It scales to exascale sizes without the prohibitive cost of full Fat-Trees, thanks to the efficient use of global optical links.
*   **Data Efficiency:** When paired with adaptive routing (UGAL) and in-network computing (SHARP), it maximizes link utilization.
*   **Fault Tolerance:** Its rich connectivity and bipartite local structure provide robust redundancy.

While **Slim Fly** offers a glimpse into a more efficient future, **Dragonfly+** is the practical champion powering the current generation of top-tier supercomputers.

### References
[cite: 1] Domke et al., "HyperX vs Dragonfly vs Fat-Tree," SC '19.
[cite: 2] "Selecting the Right Mellanox Network Architecture," Medium, 2023.
[cite: 3] "High-performance computing... Fat Tree," OceanClub, 2024.
[cite: 5] Kim et al., "Technology-Driven, Highly-Scalable Dragonfly Topology," ISCA '08.
[cite: 12] "Dragonfly topology traffic pattern," IEEE Transactions, 2018.
[cite: 19] Blach et al., "First Real-World Slim Fly Deployment," USENIX NSDI '24.
[cite: 16] McDonald et al., "Practical and Efficient Incremental Adaptive Routing for HyperX," SC '19.
[cite: 17] Besta & Hoefler, "Slim Fly: A Cost Effective Low-Diameter Network Topology," SC '14.
[cite: 14] "Super-Connecting the Supercomputers," HPCwire, 2019.
[cite: 25] Besta et al., "Fault Tolerance for Remote Memory Access," ACM HPDC.
[cite: 9] "Dragonfly and Dragonfly+ Topology," PanSolusi, 2024.
[cite: 15] Shpiner et al., "Dragonfly+: Low Cost Topology for Scaling Datacenters," HiPINEB '17.
[cite: 11] "Technology-Driven Highly-Scalable Dragonfly Topology," Stanford TechFinder.
[cite: 22] Chaulagain & Yuan, "Enhanced UGAL Routing Schemes," ICS '24.

**Sources:**
1. [gitlab.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQkh0_YLLmMkjg_sNXnGPQl-2i9CbxTaHsUeHFvljXTI3IdFtNcrBQqp41gk1LHNYQ3axVEDG7dgxdfIAQ3eJK5w2zRoSwk1kFuthDsjulkrcINLhAGO01mtqmwID4HmwvJKXsTXg6)
2. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAO3PezPB2u2aha9uNUcd4gtm7wOfwiTiCaghwIhP-XmwQd9KsdeDg3z3fvs5prSAX9XBqZiacAYGsHmox8nxMuV2LO-a501GOKoGTmq7HWp34xs2fdJWedb22K6qlSgf3ERtHUzMQv7J0t7Vry7LYS_uP-_fKeJ3xK6o5VQM8ixUKwUg5kEcSIEq0jMkVou2L-2ihGOSdZFor2NrVo-zu)
3. [oceanclub.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ3EhFOawbG6cCTWFqDue_rs9HwuL24lIzILPBaoA9HaO9q-fWk20YRujwsSh9qd19Kap39OKRyFPKSHkTaYHJjswaftj5KWjsYzODNlClpTv0M8VjaJ2qZ-rqVX9lrpiLuGOlJdU=)
4. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0mPHiXRRgjLRZwXRQovR4g67YERntt4c1uFHUeT5cqHprlJSo0JX5K4ZeA_Sq7Ag8L0T4v5v9Twp3zltArYdWQQP3cGV6PLRu2cS0SnzhZ2Va-Plvs5_7bpc=)
5. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyFbRvDc4xPjgQ-yjmug3El5dlE1pDwgGCbwg3eMi18aVRZs0j8nZSn6IRXETg5phjPA8TrYIarPUZ331AOETgm5d_wZFc390j-JPR1rfdlOgx2PxhbzEK-Av-q6aaRD-RTmToBKQZ)
6. [glennklockwood.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMyyTkPoTfHIz9_Wz0biF-ZyRs0Yoa8BXC33DrxZjt10MRA8HgMmLNQEmI7eKNfctgzINpTTmEOaqGsK3512oACB6gm3XMuegRaCpcNcsY1vTfiIhaQsYLF9Q6o1ImLO-VvwS-)
7. [i3a.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZa-GvKe_fP2_mEzrFWNY4jhsPvvk2Ti2wdhguN29I81jQnV4l5BFF6wAxVmhOJjfVk9NMiyC3_z835zGLmfoyDaeWdbNXMO28JmwUVMe9Bnh6vJDcs3E4qSMuyDJ-ylfeAdanqgJ8aBs3pLKup1UCGFNzXvpVCcadkFNYvTY53J2OCtOAohp9mWyZRA==)
8. [ietf.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGD4VYf27W_F9DCwG8gb-EljpWJLleQIHXxzaTY_677pogF9gQiEsCtQkGbNeHU4ovc6tjiYQJf4vc8B-7mw7x90Q5M5tduiw2RNtmS0ILNiE2PUfAM5jpXmkj2EHR7RGnhkfpMOjo4SAce-oK0EEK-m1xs8LXwvztSm2l5PNv2PZO84BEee13j0MY47g==)
9. [pansolusi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhwOY3e667IFmUc4_SHxslwBAYg-Nc6J4Tbqy2I98AmwTIdsO_dbxqBsX8N7QkN0gF6giLBOuZkiVztAHf4b4PWB5exkzie7ECpNIlRf3kIysZ7foSdIJ32H2k7Rz1jLlmDfY7cfIucW04pK96da4sTx0g82pIouRGioRh)
10. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnT3fdaUtk8A0Sqs6Bi0RlRlTz7TjBnyzNFeBM-CU-7Hin1LWwJnBfn4-ADmNMcFn0F8OFsSZ1OI1MKxperiSKbghWY-14CkZrFa93maxesTbmRN6Z7PDp)
11. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrA2kb3Mlt6Cnaqfnu8Ts0F2xFs-ye2MRMgU1QE-De91sLlvj6NVSmZuS5TivLwA6z2Qp0Asvk0BFira8xy2IkAkmsDySyphY4UYn6hUmioSo2yZ9TiKNwuqXCQV8U3DraJJz9Izd7xHRihRewIXyhBLX9LYXIJgbt_cSz2QY5xr5MBcXFLp2ly4O_tP8tdsBrgORG)
12. [lanl.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcqEDw2nVuCelwm0BYXAhQ-MXrzLJBWLeCe6vH1WvACxeXm-M_cM4mSBySYgLlK8BvAJXtLiXkTQXaEl98tsf97Icv0-mkMIS9EuEKs3DEF9WGzb8yxdmz4cEC1Tsfv4JGOnyieLMKFSOKiAS1bC-u9eX56aXdYqOGxoVuoVequvbb9UuCbB3fZb96Fl0CxJe7UItlHMUZI9E=)
13. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdnHkw7-mW1M1O3zJ_tXjUIqxRWN0r4ur72U0la-mdR7GHiOeyeEhEP7kA41Zt0Bmb_XAik_yQ68pZneXGMdlYLkKa4Ntu-ifxGfnlCG-RiAgT0DydysgneBQryJowf4auo_I0jh6c)
14. [hpcwire.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1R6HXeFdrQGTmHw27WXGfPr-UO7gOvJ6mcZwpGYWMf1949fhBdasDshUMHzDRD4YyeqdkSI3kkKLYlgpaz0NNl9yZdEtHdiUW9Te1astmNwYN2QulKDWwLmF4MaVyHxrEHqgR4LGVf9hhVJWKfxDhF2rT8WvXZCFcSGGiq_7VHljbjY0rGLpMlGnw2B4oMuVHPg-PnLWmi3PGPiHXxzrj-w4E)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzp4tqFpso-dYG-XU3EkJDUfsHSKaAvZSfXUc_HmTfVAd9e0TqwqkITfJMCOfPra1Vm1rZybauSkBSi0Adb650-eGTLXWYrhKooohCiG86yH9lQ0wt4ARhh0CXFLE9ybrSCFDEOun1BFvQhr2z_lZv6Q22vNGDZnvDudmHHZtU6NfJnHdu7lIZhHI1RQ5wj9YkN6T-1dUiTpF-mw==)
16. [nicm.dev](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZowjyTV2XWQlj8rMDLWZEXw3Z8O8fNFY2byUHAnNSWBKYJ4HyaqKCgG-AnEggXmGxG7967LDlF5gDOB1obKxnh9-VdXYj-Q53gvBS30RKHNQ92s-dU5kITT55MWakudcgcegz_if_wa1RggLA-Ace)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEMEHTKFfgfdKnp_x19Hkc3x9PsTu5YQbzN12AA28jZt1FGcxQSVLOPyd-21RbVqbfc-iK-r9ZGld_aBDT6_G0dh7tkB-YZysXOK2rbKoVK4yPzA9qHiDDIAJFpHZJneRBATT_8C1DepN8-0DDs29A0d3lEbq5n3y6wJtaTN3ZB-BM-vr7Fh0ju9Rcrvi2w5wHUqTg2Pk0PmZqLTSQN-A=)
18. [ethz.ch](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2a78wdmwnewqfzPAQv7lj7Yi399UVLEK7b3ksStNJdYlEm522Cxji3x4dHkuGx1vhAkbjFftA6jLATz7le07qPutFzh6pGQbf9f-t9Im-sseHaZmw2oSJZI2gFKztYewIUHJDFI0LaYuJ3ui9D89tQDsR)
19. [usenix.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjzKYGKVcEE_o-YKYBgecdMSXUHx3Vp-qIaVpA6Cl23TGcO5fhp37EPJAvRCgZ9NqFIkLE4r-97IFYhdZoX-9vqknOuaYEZF4UhDk4XqPN6CLlPYq0s0hGIRhCJwEgP8ZKRT3ybWthgyw=)
20. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAsh2DRWJ_Bs_hERbDsRfdThi2rOi8gWn0pgr2Ea-TkitnO0E46t8tn0FD4k03LAlcXPzb7rrS09zN6wje9J_nRum1f2oYRTccyErPU91z4M4JU0LbaGhN)
21. [warwick.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrHwZG8Po4iZWEUblczdZVLvLpXe6PEQRRDpHjqGoeIn4iQu5Sk3--c55-6Cqzjfm-sEu1L5ODVj7MyyRhayhvBpir0cwVF-8epjvkPIpmn-TPXyepwL77PLeykAuuycH5bKWMhPPX7NWNca4wvZ21qljtrWw=)
22. [nsf.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI7nDct5lMoMmc3pfBE8QCwm7gNqncy0_XwtpwXdRCstryB3-6K3HMnBQzkL0gNlnZ9LPqh_PDLNW1WavL25gkU1_gErDQI9rI7nUBll4smfajuDdA-qxGPTqd20b5Yg==)
23. [scribd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMc4IpTMeMf9598ZzUAFxkMXlOcRe0LMpQeS_ta3yQHfQPw7xwapOUyVsoq8G-nesCDcSQADDnGhvdDIArwVqSVkFg39Mlbz8DQPPGsSL_RSEb1Vxta-CzCbjLdd7aM0lgJsc1WkHSwJzzxjLTtZVR-VJtNQkdcnza7CT9jitVRhuQfA==)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjzQNau7HXyt8J8rN6FeUFweCG4aFJetYWF2YBWp1_0s_5zXJd6pS3F2iaW3mqo-mih-oSzrWMkf0JMBiW1TyybhflSwE5ynfwLGwyBreIHPO8Stki5MZdWU51z5Vlc7XxaK3XpicnKuOoWJuCtykneLZkXxW5w-VBtxfCxvQT0Gqto62D8_ydFDHJJ4qGLvazRpuDQch4yzquDxLY)
25. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGskkutMSHd_Uke8vdgdFnVHsxYxG4QpdrHMn4cPHQdYsDmgLAPscZ0u3Y41aw5hV2f1Vj1sh1_6cKyqKxlmyjzeJUNF6_GdUnC96VRdQTOD8YsRhay)
26. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExroQJyOLAyrvEenV-p_5juzG4kDnPVVQjw7rI-Omvt9eIhuGlbJiXLJUsOWvcvkkggiA5eCYgWRHaQ9GAw_TkCwRtBmCZ61uGb-jdgZQLR0sfP_9S4W3-aw9p2Fpzg1gcTtKddFCMIil2aqbcOOpdDkXsx7JQR4r5rzplcSqZ-Gr1yAyGprots9U7hoCCeR8=)
27. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUmd_qnXJe-ixQQAWhhriEr59NXxdhFo9sAVsEujuYOBmNIDXD70FkdiFGGZOJbXogrdlimB5GPnKV1SliVJgLE4RnkKj39LgEFgpeS-ZH8dDL_BZeSxI8wu67e3yILBsJUFS3Yi2ikRNsyQyYz06K1TsrkTDnpKZEbIYPcKO1PmS7yiCNHsJ0)


## Annotations
Annotation(end_index=4969, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAO3PezPB2u2aha9uNUcd4gtm7wOfwiTiCaghwIhP-XmwQd9KsdeDg3z3fvs5prSAX9XBqZiacAYGsHmox8nxMuV2LO-a501GOKoGTmq7HWp34xs2fdJWedb22K6qlSgf3ERtHUzMQv7J0t7Vry7LYS_uP-_fKeJ3xK6o5VQM8ixUKwUg5kEcSIEq0jMkVou2L-2ihGOSdZFor2NrVo-zu', start_index=4957)
Annotation(end_index=4969, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQkh0_YLLmMkjg_sNXnGPQl-2i9CbxTaHsUeHFvljXTI3IdFtNcrBQqp41gk1LHNYQ3axVEDG7dgxdfIAQ3eJK5w2zRoSwk1kFuthDsjulkrcINLhAGO01mtqmwID4HmwvJKXsTXg6', start_index=4957)
Annotation(end_index=5302, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ3EhFOawbG6cCTWFqDue_rs9HwuL24lIzILPBaoA9HaO9q-fWk20YRujwsSh9qd19Kap39OKRyFPKSHkTaYHJjswaftj5KWjsYzODNlClpTv0M8VjaJ2qZ-rqVX9lrpiLuGOlJdU=', start_index=5293)
Annotation(end_index=5592, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQkh0_YLLmMkjg_sNXnGPQl-2i9CbxTaHsUeHFvljXTI3IdFtNcrBQqp41gk1LHNYQ3axVEDG7dgxdfIAQ3eJK5w2zRoSwk1kFuthDsjulkrcINLhAGO01mtqmwID4HmwvJKXsTXg6', start_index=5583)
Annotation(end_index=5788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQkh0_YLLmMkjg_sNXnGPQl-2i9CbxTaHsUeHFvljXTI3IdFtNcrBQqp41gk1LHNYQ3axVEDG7dgxdfIAQ3eJK5w2zRoSwk1kFuthDsjulkrcINLhAGO01mtqmwID4HmwvJKXsTXg6', start_index=5779)
Annotation(end_index=6311, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAO3PezPB2u2aha9uNUcd4gtm7wOfwiTiCaghwIhP-XmwQd9KsdeDg3z3fvs5prSAX9XBqZiacAYGsHmox8nxMuV2LO-a501GOKoGTmq7HWp34xs2fdJWedb22K6qlSgf3ERtHUzMQv7J0t7Vry7LYS_uP-_fKeJ3xK6o5VQM8ixUKwUg5kEcSIEq0jMkVou2L-2ihGOSdZFor2NrVo-zu', start_index=6302)
Annotation(end_index=6549, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0mPHiXRRgjLRZwXRQovR4g67YERntt4c1uFHUeT5cqHprlJSo0JX5K4ZeA_Sq7Ag8L0T4v5v9Twp3zltArYdWQQP3cGV6PLRu2cS0SnzhZ2Va-Plvs5_7bpc=', start_index=6537)
Annotation(end_index=6549, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAO3PezPB2u2aha9uNUcd4gtm7wOfwiTiCaghwIhP-XmwQd9KsdeDg3z3fvs5prSAX9XBqZiacAYGsHmox8nxMuV2LO-a501GOKoGTmq7HWp34xs2fdJWedb22K6qlSgf3ERtHUzMQv7J0t7Vry7LYS_uP-_fKeJ3xK6o5VQM8ixUKwUg5kEcSIEq0jMkVou2L-2ihGOSdZFor2NrVo-zu', start_index=6537)
Annotation(end_index=7549, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyFbRvDc4xPjgQ-yjmug3El5dlE1pDwgGCbwg3eMi18aVRZs0j8nZSn6IRXETg5phjPA8TrYIarPUZ331AOETgm5d_wZFc390j-JPR1rfdlOgx2PxhbzEK-Av-q6aaRD-RTmToBKQZ', start_index=7534)
Annotation(end_index=7549, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQkh0_YLLmMkjg_sNXnGPQl-2i9CbxTaHsUeHFvljXTI3IdFtNcrBQqp41gk1LHNYQ3axVEDG7dgxdfIAQ3eJK5w2zRoSwk1kFuthDsjulkrcINLhAGO01mtqmwID4HmwvJKXsTXg6', start_index=7534)
Annotation(end_index=7549, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMyyTkPoTfHIz9_Wz0biF-ZyRs0Yoa8BXC33DrxZjt10MRA8HgMmLNQEmI7eKNfctgzINpTTmEOaqGsK3512oACB6gm3XMuegRaCpcNcsY1vTfiIhaQsYLF9Q6o1ImLO-VvwS-', start_index=7534)
Annotation(end_index=7913, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyFbRvDc4xPjgQ-yjmug3El5dlE1pDwgGCbwg3eMi18aVRZs0j8nZSn6IRXETg5phjPA8TrYIarPUZ331AOETgm5d_wZFc390j-JPR1rfdlOgx2PxhbzEK-Av-q6aaRD-RTmToBKQZ', start_index=7901)
Annotation(end_index=7913, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZa-GvKe_fP2_mEzrFWNY4jhsPvvk2Ti2wdhguN29I81jQnV4l5BFF6wAxVmhOJjfVk9NMiyC3_z835zGLmfoyDaeWdbNXMO28JmwUVMe9Bnh6vJDcs3E4qSMuyDJ-ylfeAdanqgJ8aBs3pLKup1UCGFNzXvpVCcadkFNYvTY53J2OCtOAohp9mWyZRA==', start_index=7901)
Annotation(end_index=8133, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhwOY3e667IFmUc4_SHxslwBAYg-Nc6J4Tbqy2I98AmwTIdsO_dbxqBsX8N7QkN0gF6giLBOuZkiVztAHf4b4PWB5exkzie7ECpNIlRf3kIysZ7foSdIJ32H2k7Rz1jLlmDfY7cfIucW04pK96da4sTx0g82pIouRGioRh', start_index=8121)
Annotation(end_index=8133, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGD4VYf27W_F9DCwG8gb-EljpWJLleQIHXxzaTY_677pogF9gQiEsCtQkGbNeHU4ovc6tjiYQJf4vc8B-7mw7x90Q5M5tduiw2RNtmS0ILNiE2PUfAM5jpXmkj2EHR7RGnhkfpMOjo4SAce-oK0EEK-m1xs8LXwvztSm2l5PNv2PZO84BEee13j0MY47g==', start_index=8121)
Annotation(end_index=8492, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnT3fdaUtk8A0Sqs6Bi0RlRlTz7TjBnyzNFeBM-CU-7Hin1LWwJnBfn4-ADmNMcFn0F8OFsSZ1OI1MKxperiSKbghWY-14CkZrFa93maxesTbmRN6Z7PDp', start_index=8482)
Annotation(end_index=8932, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQkh0_YLLmMkjg_sNXnGPQl-2i9CbxTaHsUeHFvljXTI3IdFtNcrBQqp41gk1LHNYQ3axVEDG7dgxdfIAQ3eJK5w2zRoSwk1kFuthDsjulkrcINLhAGO01mtqmwID4HmwvJKXsTXg6', start_index=8919)
Annotation(end_index=8932, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrA2kb3Mlt6Cnaqfnu8Ts0F2xFs-ye2MRMgU1QE-De91sLlvj6NVSmZuS5TivLwA6z2Qp0Asvk0BFira8xy2IkAkmsDySyphY4UYn6hUmioSo2yZ9TiKNwuqXCQV8U3DraJJz9Izd7xHRihRewIXyhBLX9LYXIJgbt_cSz2QY5xr5MBcXFLp2ly4O_tP8tdsBrgORG', start_index=8919)
Annotation(end_index=9415, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyFbRvDc4xPjgQ-yjmug3El5dlE1pDwgGCbwg3eMi18aVRZs0j8nZSn6IRXETg5phjPA8TrYIarPUZ331AOETgm5d_wZFc390j-JPR1rfdlOgx2PxhbzEK-Av-q6aaRD-RTmToBKQZ', start_index=9402)
Annotation(end_index=9415, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcqEDw2nVuCelwm0BYXAhQ-MXrzLJBWLeCe6vH1WvACxeXm-M_cM4mSBySYgLlK8BvAJXtLiXkTQXaEl98tsf97Icv0-mkMIS9EuEKs3DEF9WGzb8yxdmz4cEC1Tsfv4JGOnyieLMKFSOKiAS1bC-u9eX56aXdYqOGxoVuoVequvbb9UuCbB3fZb96Fl0CxJe7UItlHMUZI9E=', start_index=9402)
Annotation(end_index=9714, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyFbRvDc4xPjgQ-yjmug3El5dlE1pDwgGCbwg3eMi18aVRZs0j8nZSn6IRXETg5phjPA8TrYIarPUZ331AOETgm5d_wZFc390j-JPR1rfdlOgx2PxhbzEK-Av-q6aaRD-RTmToBKQZ', start_index=9701)
Annotation(end_index=9714, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdnHkw7-mW1M1O3zJ_tXjUIqxRWN0r4ur72U0la-mdR7GHiOeyeEhEP7kA41Zt0Bmb_XAik_yQ68pZneXGMdlYLkKa4Ntu-ifxGfnlCG-RiAgT0DydysgneBQryJowf4auo_I0jh6c', start_index=9701)
Annotation(end_index=9942, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhwOY3e667IFmUc4_SHxslwBAYg-Nc6J4Tbqy2I98AmwTIdsO_dbxqBsX8N7QkN0gF6giLBOuZkiVztAHf4b4PWB5exkzie7ECpNIlRf3kIysZ7foSdIJ32H2k7Rz1jLlmDfY7cfIucW04pK96da4sTx0g82pIouRGioRh', start_index=9929)
Annotation(end_index=9942, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1R6HXeFdrQGTmHw27WXGfPr-UO7gOvJ6mcZwpGYWMf1949fhBdasDshUMHzDRD4YyeqdkSI3kkKLYlgpaz0NNl9yZdEtHdiUW9Te1astmNwYN2QulKDWwLmF4MaVyHxrEHqgR4LGVf9hhVJWKfxDhF2rT8WvXZCFcSGGiq_7VHljbjY0rGLpMlGnw2B4oMuVHPg-PnLWmi3PGPiHXxzrj-w4E', start_index=9929)
Annotation(end_index=10242, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhwOY3e667IFmUc4_SHxslwBAYg-Nc6J4Tbqy2I98AmwTIdsO_dbxqBsX8N7QkN0gF6giLBOuZkiVztAHf4b4PWB5exkzie7ECpNIlRf3kIysZ7foSdIJ32H2k7Rz1jLlmDfY7cfIucW04pK96da4sTx0g82pIouRGioRh', start_index=10229)
Annotation(end_index=10242, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzp4tqFpso-dYG-XU3EkJDUfsHSKaAvZSfXUc_HmTfVAd9e0TqwqkITfJMCOfPra1Vm1rZybauSkBSi0Adb650-eGTLXWYrhKooohCiG86yH9lQ0wt4ARhh0CXFLE9ybrSCFDEOun1BFvQhr2z_lZv6Q22vNGDZnvDudmHHZtU6NfJnHdu7lIZhHI1RQ5wj9YkN6T-1dUiTpF-mw==', start_index=10229)
Annotation(end_index=10653, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzp4tqFpso-dYG-XU3EkJDUfsHSKaAvZSfXUc_HmTfVAd9e0TqwqkITfJMCOfPra1Vm1rZybauSkBSi0Adb650-eGTLXWYrhKooohCiG86yH9lQ0wt4ARhh0CXFLE9ybrSCFDEOun1BFvQhr2z_lZv6Q22vNGDZnvDudmHHZtU6NfJnHdu7lIZhHI1RQ5wj9YkN6T-1dUiTpF-mw==', start_index=10643)
Annotation(end_index=10848, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhwOY3e667IFmUc4_SHxslwBAYg-Nc6J4Tbqy2I98AmwTIdsO_dbxqBsX8N7QkN0gF6giLBOuZkiVztAHf4b4PWB5exkzie7ECpNIlRf3kIysZ7foSdIJ32H2k7Rz1jLlmDfY7cfIucW04pK96da4sTx0g82pIouRGioRh', start_index=10839)
Annotation(end_index=11011, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhwOY3e667IFmUc4_SHxslwBAYg-Nc6J4Tbqy2I98AmwTIdsO_dbxqBsX8N7QkN0gF6giLBOuZkiVztAHf4b4PWB5exkzie7ECpNIlRf3kIysZ7foSdIJ32H2k7Rz1jLlmDfY7cfIucW04pK96da4sTx0g82pIouRGioRh', start_index=11002)
Annotation(end_index=11248, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1R6HXeFdrQGTmHw27WXGfPr-UO7gOvJ6mcZwpGYWMf1949fhBdasDshUMHzDRD4YyeqdkSI3kkKLYlgpaz0NNl9yZdEtHdiUW9Te1astmNwYN2QulKDWwLmF4MaVyHxrEHqgR4LGVf9hhVJWKfxDhF2rT8WvXZCFcSGGiq_7VHljbjY0rGLpMlGnw2B4oMuVHPg-PnLWmi3PGPiHXxzrj-w4E', start_index=11238)
Annotation(end_index=11441, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQkh0_YLLmMkjg_sNXnGPQl-2i9CbxTaHsUeHFvljXTI3IdFtNcrBQqp41gk1LHNYQ3axVEDG7dgxdfIAQ3eJK5w2zRoSwk1kFuthDsjulkrcINLhAGO01mtqmwID4HmwvJKXsTXg6', start_index=11428)
Annotation(end_index=11441, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZowjyTV2XWQlj8rMDLWZEXw3Z8O8fNFY2byUHAnNSWBKYJ4HyaqKCgG-AnEggXmGxG7967LDlF5gDOB1obKxnh9-VdXYj-Q53gvBS30RKHNQ92s-dU5kITT55MWakudcgcegz_if_wa1RggLA-Ace', start_index=11428)
Annotation(end_index=11703, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZowjyTV2XWQlj8rMDLWZEXw3Z8O8fNFY2byUHAnNSWBKYJ4HyaqKCgG-AnEggXmGxG7967LDlF5gDOB1obKxnh9-VdXYj-Q53gvBS30RKHNQ92s-dU5kITT55MWakudcgcegz_if_wa1RggLA-Ace', start_index=11693)
Annotation(end_index=11949, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQkh0_YLLmMkjg_sNXnGPQl-2i9CbxTaHsUeHFvljXTI3IdFtNcrBQqp41gk1LHNYQ3axVEDG7dgxdfIAQ3eJK5w2zRoSwk1kFuthDsjulkrcINLhAGO01mtqmwID4HmwvJKXsTXg6', start_index=11940)
Annotation(end_index=12206, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZowjyTV2XWQlj8rMDLWZEXw3Z8O8fNFY2byUHAnNSWBKYJ4HyaqKCgG-AnEggXmGxG7967LDlF5gDOB1obKxnh9-VdXYj-Q53gvBS30RKHNQ92s-dU5kITT55MWakudcgcegz_if_wa1RggLA-Ace', start_index=12196)
Annotation(end_index=12375, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZowjyTV2XWQlj8rMDLWZEXw3Z8O8fNFY2byUHAnNSWBKYJ4HyaqKCgG-AnEggXmGxG7967LDlF5gDOB1obKxnh9-VdXYj-Q53gvBS30RKHNQ92s-dU5kITT55MWakudcgcegz_if_wa1RggLA-Ace', start_index=12365)
Annotation(end_index=12537, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZowjyTV2XWQlj8rMDLWZEXw3Z8O8fNFY2byUHAnNSWBKYJ4HyaqKCgG-AnEggXmGxG7967LDlF5gDOB1obKxnh9-VdXYj-Q53gvBS30RKHNQ92s-dU5kITT55MWakudcgcegz_if_wa1RggLA-Ace', start_index=12527)
Annotation(end_index=12809, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEMEHTKFfgfdKnp_x19Hkc3x9PsTu5YQbzN12AA28jZt1FGcxQSVLOPyd-21RbVqbfc-iK-r9ZGld_aBDT6_G0dh7tkB-YZysXOK2rbKoVK4yPzA9qHiDDIAJFpHZJneRBATT_8C1DepN8-0DDs29A0d3lEbq5n3y6wJtaTN3ZB-BM-vr7Fh0ju9Rcrvi2w5wHUqTg2Pk0PmZqLTSQN-A=', start_index=12795)
Annotation(end_index=12809, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2a78wdmwnewqfzPAQv7lj7Yi399UVLEK7b3ksStNJdYlEm522Cxji3x4dHkuGx1vhAkbjFftA6jLATz7le07qPutFzh6pGQbf9f-t9Im-sseHaZmw2oSJZI2gFKztYewIUHJDFI0LaYuJ3ui9D89tQDsR', start_index=12795)
Annotation(end_index=12993, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEMEHTKFfgfdKnp_x19Hkc3x9PsTu5YQbzN12AA28jZt1FGcxQSVLOPyd-21RbVqbfc-iK-r9ZGld_aBDT6_G0dh7tkB-YZysXOK2rbKoVK4yPzA9qHiDDIAJFpHZJneRBATT_8C1DepN8-0DDs29A0d3lEbq5n3y6wJtaTN3ZB-BM-vr7Fh0ju9Rcrvi2w5wHUqTg2Pk0PmZqLTSQN-A=', start_index=12979)
Annotation(end_index=12993, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2a78wdmwnewqfzPAQv7lj7Yi399UVLEK7b3ksStNJdYlEm522Cxji3x4dHkuGx1vhAkbjFftA6jLATz7le07qPutFzh6pGQbf9f-t9Im-sseHaZmw2oSJZI2gFKztYewIUHJDFI0LaYuJ3ui9D89tQDsR', start_index=12979)
Annotation(end_index=13172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEMEHTKFfgfdKnp_x19Hkc3x9PsTu5YQbzN12AA28jZt1FGcxQSVLOPyd-21RbVqbfc-iK-r9ZGld_aBDT6_G0dh7tkB-YZysXOK2rbKoVK4yPzA9qHiDDIAJFpHZJneRBATT_8C1DepN8-0DDs29A0d3lEbq5n3y6wJtaTN3ZB-BM-vr7Fh0ju9Rcrvi2w5wHUqTg2Pk0PmZqLTSQN-A=', start_index=13162)
Annotation(end_index=13394, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAsh2DRWJ_Bs_hERbDsRfdThi2rOi8gWn0pgr2Ea-TkitnO0E46t8tn0FD4k03LAlcXPzb7rrS09zN6wje9J_nRum1f2oYRTccyErPU91z4M4JU0LbaGhN', start_index=13380)
Annotation(end_index=13394, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjzKYGKVcEE_o-YKYBgecdMSXUHx3Vp-qIaVpA6Cl23TGcO5fhp37EPJAvRCgZ9NqFIkLE4r-97IFYhdZoX-9vqknOuaYEZF4UhDk4XqPN6CLlPYq0s0hGIRhCJwEgP8ZKRT3ybWthgyw=', start_index=13380)
Annotation(end_index=13619, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2a78wdmwnewqfzPAQv7lj7Yi399UVLEK7b3ksStNJdYlEm522Cxji3x4dHkuGx1vhAkbjFftA6jLATz7le07qPutFzh6pGQbf9f-t9Im-sseHaZmw2oSJZI2gFKztYewIUHJDFI0LaYuJ3ui9D89tQDsR', start_index=13609)
Annotation(end_index=13843, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEMEHTKFfgfdKnp_x19Hkc3x9PsTu5YQbzN12AA28jZt1FGcxQSVLOPyd-21RbVqbfc-iK-r9ZGld_aBDT6_G0dh7tkB-YZysXOK2rbKoVK4yPzA9qHiDDIAJFpHZJneRBATT_8C1DepN8-0DDs29A0d3lEbq5n3y6wJtaTN3ZB-BM-vr7Fh0ju9Rcrvi2w5wHUqTg2Pk0PmZqLTSQN-A=', start_index=13829)
Annotation(end_index=13843, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjzKYGKVcEE_o-YKYBgecdMSXUHx3Vp-qIaVpA6Cl23TGcO5fhp37EPJAvRCgZ9NqFIkLE4r-97IFYhdZoX-9vqknOuaYEZF4UhDk4XqPN6CLlPYq0s0hGIRhCJwEgP8ZKRT3ybWthgyw=', start_index=13829)
Annotation(end_index=14124, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjzKYGKVcEE_o-YKYBgecdMSXUHx3Vp-qIaVpA6Cl23TGcO5fhp37EPJAvRCgZ9NqFIkLE4r-97IFYhdZoX-9vqknOuaYEZF4UhDk4XqPN6CLlPYq0s0hGIRhCJwEgP8ZKRT3ybWthgyw=', start_index=14114)
Annotation(end_index=14349, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjzKYGKVcEE_o-YKYBgecdMSXUHx3Vp-qIaVpA6Cl23TGcO5fhp37EPJAvRCgZ9NqFIkLE4r-97IFYhdZoX-9vqknOuaYEZF4UhDk4XqPN6CLlPYq0s0hGIRhCJwEgP8ZKRT3ybWthgyw=', start_index=14339)
Annotation(end_index=15096, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyFbRvDc4xPjgQ-yjmug3El5dlE1pDwgGCbwg3eMi18aVRZs0j8nZSn6IRXETg5phjPA8TrYIarPUZ331AOETgm5d_wZFc390j-JPR1rfdlOgx2PxhbzEK-Av-q6aaRD-RTmToBKQZ', start_index=15079)
Annotation(end_index=15096, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcqEDw2nVuCelwm0BYXAhQ-MXrzLJBWLeCe6vH1WvACxeXm-M_cM4mSBySYgLlK8BvAJXtLiXkTQXaEl98tsf97Icv0-mkMIS9EuEKs3DEF9WGzb8yxdmz4cEC1Tsfv4JGOnyieLMKFSOKiAS1bC-u9eX56aXdYqOGxoVuoVequvbb9UuCbB3fZb96Fl0CxJe7UItlHMUZI9E=', start_index=15079)
Annotation(end_index=15096, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrHwZG8Po4iZWEUblczdZVLvLpXe6PEQRRDpHjqGoeIn4iQu5Sk3--c55-6Cqzjfm-sEu1L5ODVj7MyyRhayhvBpir0cwVF-8epjvkPIpmn-TPXyepwL77PLeykAuuycH5bKWMhPPX7NWNca4wvZ21qljtrWw=', start_index=15079)
Annotation(end_index=15420, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyFbRvDc4xPjgQ-yjmug3El5dlE1pDwgGCbwg3eMi18aVRZs0j8nZSn6IRXETg5phjPA8TrYIarPUZ331AOETgm5d_wZFc390j-JPR1rfdlOgx2PxhbzEK-Av-q6aaRD-RTmToBKQZ', start_index=15407)
Annotation(end_index=15420, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcqEDw2nVuCelwm0BYXAhQ-MXrzLJBWLeCe6vH1WvACxeXm-M_cM4mSBySYgLlK8BvAJXtLiXkTQXaEl98tsf97Icv0-mkMIS9EuEKs3DEF9WGzb8yxdmz4cEC1Tsfv4JGOnyieLMKFSOKiAS1bC-u9eX56aXdYqOGxoVuoVequvbb9UuCbB3fZb96Fl0CxJe7UItlHMUZI9E=', start_index=15407)
Annotation(end_index=15697, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyFbRvDc4xPjgQ-yjmug3El5dlE1pDwgGCbwg3eMi18aVRZs0j8nZSn6IRXETg5phjPA8TrYIarPUZ331AOETgm5d_wZFc390j-JPR1rfdlOgx2PxhbzEK-Av-q6aaRD-RTmToBKQZ', start_index=15684)
Annotation(end_index=15697, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZowjyTV2XWQlj8rMDLWZEXw3Z8O8fNFY2byUHAnNSWBKYJ4HyaqKCgG-AnEggXmGxG7967LDlF5gDOB1obKxnh9-VdXYj-Q53gvBS30RKHNQ92s-dU5kITT55MWakudcgcegz_if_wa1RggLA-Ace', start_index=15684)
Annotation(end_index=16121, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI7nDct5lMoMmc3pfBE8QCwm7gNqncy0_XwtpwXdRCstryB3-6K3HMnBQzkL0gNlnZ9LPqh_PDLNW1WavL25gkU1_gErDQI9rI7nUBll4smfajuDdA-qxGPTqd20b5Yg==', start_index=16103)
Annotation(end_index=16121, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzp4tqFpso-dYG-XU3EkJDUfsHSKaAvZSfXUc_HmTfVAd9e0TqwqkITfJMCOfPra1Vm1rZybauSkBSi0Adb650-eGTLXWYrhKooohCiG86yH9lQ0wt4ARhh0CXFLE9ybrSCFDEOun1BFvQhr2z_lZv6Q22vNGDZnvDudmHHZtU6NfJnHdu7lIZhHI1RQ5wj9YkN6T-1dUiTpF-mw==', start_index=16103)
Annotation(end_index=16121, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdnHkw7-mW1M1O3zJ_tXjUIqxRWN0r4ur72U0la-mdR7GHiOeyeEhEP7kA41Zt0Bmb_XAik_yQ68pZneXGMdlYLkKa4Ntu-ifxGfnlCG-RiAgT0DydysgneBQryJowf4auo_I0jh6c', start_index=16103)
Annotation(end_index=16492, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMc4IpTMeMf9598ZzUAFxkMXlOcRe0LMpQeS_ta3yQHfQPw7xwapOUyVsoq8G-nesCDcSQADDnGhvdDIArwVqSVkFg39Mlbz8DQPPGsSL_RSEb1Vxta-CzCbjLdd7aM0lgJsc1WkHSwJzzxjLTtZVR-VJtNQkdcnza7CT9jitVRhuQfA==', start_index=16482)
Annotation(end_index=16986, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAO3PezPB2u2aha9uNUcd4gtm7wOfwiTiCaghwIhP-XmwQd9KsdeDg3z3fvs5prSAX9XBqZiacAYGsHmox8nxMuV2LO-a501GOKoGTmq7HWp34xs2fdJWedb22K6qlSgf3ERtHUzMQv7J0t7Vry7LYS_uP-_fKeJ3xK6o5VQM8ixUKwUg5kEcSIEq0jMkVou2L-2ihGOSdZFor2NrVo-zu', start_index=16977)
Annotation(end_index=17231, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjzQNau7HXyt8J8rN6FeUFweCG4aFJetYWF2YBWp1_0s_5zXJd6pS3F2iaW3mqo-mih-oSzrWMkf0JMBiW1TyybhflSwE5ynfwLGwyBreIHPO8Stki5MZdWU51z5Vlc7XxaK3XpicnKuOoWJuCtykneLZkXxW5w-VBtxfCxvQT0Gqto62D8_ydFDHJJ4qGLvazRpuDQch4yzquDxLY', start_index=17221)
Annotation(end_index=17508, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGskkutMSHd_Uke8vdgdFnVHsxYxG4QpdrHMn4cPHQdYsDmgLAPscZ0u3Y41aw5hV2f1Vj1sh1_6cKyqKxlmyjzeJUNF6_GdUnC96VRdQTOD8YsRhay', start_index=17498)
Annotation(end_index=17904, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExroQJyOLAyrvEenV-p_5juzG4kDnPVVQjw7rI-Omvt9eIhuGlbJiXLJUsOWvcvkkggiA5eCYgWRHaQ9GAw_TkCwRtBmCZ61uGb-jdgZQLR0sfP_9S4W3-aw9p2Fpzg1gcTtKddFCMIil2aqbcOOpdDkXsx7JQR4r5rzplcSqZ-Gr1yAyGprots9U7hoCCeR8=', start_index=17894)
Annotation(end_index=20317, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ3EhFOawbG6cCTWFqDue_rs9HwuL24lIzILPBaoA9HaO9q-fWk20YRujwsSh9qd19Kap39OKRyFPKSHkTaYHJjswaftj5KWjsYzODNlClpTv0M8VjaJ2qZ-rqVX9lrpiLuGOlJdU=', start_index=20308)
Annotation(end_index=21036, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQkh0_YLLmMkjg_sNXnGPQl-2i9CbxTaHsUeHFvljXTI3IdFtNcrBQqp41gk1LHNYQ3axVEDG7dgxdfIAQ3eJK5w2zRoSwk1kFuthDsjulkrcINLhAGO01mtqmwID4HmwvJKXsTXg6', start_index=21027)
Annotation(end_index=21421, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQkh0_YLLmMkjg_sNXnGPQl-2i9CbxTaHsUeHFvljXTI3IdFtNcrBQqp41gk1LHNYQ3axVEDG7dgxdfIAQ3eJK5w2zRoSwk1kFuthDsjulkrcINLhAGO01mtqmwID4HmwvJKXsTXg6', start_index=21409)
Annotation(end_index=21421, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMyyTkPoTfHIz9_Wz0biF-ZyRs0Yoa8BXC33DrxZjt10MRA8HgMmLNQEmI7eKNfctgzINpTTmEOaqGsK3512oACB6gm3XMuegRaCpcNcsY1vTfiIhaQsYLF9Q6o1ImLO-VvwS-', start_index=21409)
Annotation(end_index=22149, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnT3fdaUtk8A0Sqs6Bi0RlRlTz7TjBnyzNFeBM-CU-7Hin1LWwJnBfn4-ADmNMcFn0F8OFsSZ1OI1MKxperiSKbghWY-14CkZrFa93maxesTbmRN6Z7PDp', start_index=22139)
Annotation(end_index=22461, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrA2kb3Mlt6Cnaqfnu8Ts0F2xFs-ye2MRMgU1QE-De91sLlvj6NVSmZuS5TivLwA6z2Qp0Asvk0BFira8xy2IkAkmsDySyphY4UYn6hUmioSo2yZ9TiKNwuqXCQV8U3DraJJz9Izd7xHRihRewIXyhBLX9LYXIJgbt_cSz2QY5xr5MBcXFLp2ly4O_tP8tdsBrgORG', start_index=22451)
Annotation(end_index=23211, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyFbRvDc4xPjgQ-yjmug3El5dlE1pDwgGCbwg3eMi18aVRZs0j8nZSn6IRXETg5phjPA8TrYIarPUZ331AOETgm5d_wZFc390j-JPR1rfdlOgx2PxhbzEK-Av-q6aaRD-RTmToBKQZ', start_index=23198)
Annotation(end_index=23211, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcqEDw2nVuCelwm0BYXAhQ-MXrzLJBWLeCe6vH1WvACxeXm-M_cM4mSBySYgLlK8BvAJXtLiXkTQXaEl98tsf97Icv0-mkMIS9EuEKs3DEF9WGzb8yxdmz4cEC1Tsfv4JGOnyieLMKFSOKiAS1bC-u9eX56aXdYqOGxoVuoVequvbb9UuCbB3fZb96Fl0CxJe7UItlHMUZI9E=', start_index=23198)
Annotation(end_index=23594, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhwOY3e667IFmUc4_SHxslwBAYg-Nc6J4Tbqy2I98AmwTIdsO_dbxqBsX8N7QkN0gF6giLBOuZkiVztAHf4b4PWB5exkzie7ECpNIlRf3kIysZ7foSdIJ32H2k7Rz1jLlmDfY7cfIucW04pK96da4sTx0g82pIouRGioRh', start_index=23585)
Annotation(end_index=23850, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzp4tqFpso-dYG-XU3EkJDUfsHSKaAvZSfXUc_HmTfVAd9e0TqwqkITfJMCOfPra1Vm1rZybauSkBSi0Adb650-eGTLXWYrhKooohCiG86yH9lQ0wt4ARhh0CXFLE9ybrSCFDEOun1BFvQhr2z_lZv6Q22vNGDZnvDudmHHZtU6NfJnHdu7lIZhHI1RQ5wj9YkN6T-1dUiTpF-mw==', start_index=23840)
Annotation(end_index=24026, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhwOY3e667IFmUc4_SHxslwBAYg-Nc6J4Tbqy2I98AmwTIdsO_dbxqBsX8N7QkN0gF6giLBOuZkiVztAHf4b4PWB5exkzie7ECpNIlRf3kIysZ7foSdIJ32H2k7Rz1jLlmDfY7cfIucW04pK96da4sTx0g82pIouRGioRh', start_index=24017)
Annotation(end_index=24202, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzp4tqFpso-dYG-XU3EkJDUfsHSKaAvZSfXUc_HmTfVAd9e0TqwqkITfJMCOfPra1Vm1rZybauSkBSi0Adb650-eGTLXWYrhKooohCiG86yH9lQ0wt4ARhh0CXFLE9ybrSCFDEOun1BFvQhr2z_lZv6Q22vNGDZnvDudmHHZtU6NfJnHdu7lIZhHI1RQ5wj9YkN6T-1dUiTpF-mw==', start_index=24192)
Annotation(end_index=24552, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEMEHTKFfgfdKnp_x19Hkc3x9PsTu5YQbzN12AA28jZt1FGcxQSVLOPyd-21RbVqbfc-iK-r9ZGld_aBDT6_G0dh7tkB-YZysXOK2rbKoVK4yPzA9qHiDDIAJFpHZJneRBATT_8C1DepN8-0DDs29A0d3lEbq5n3y6wJtaTN3ZB-BM-vr7Fh0ju9Rcrvi2w5wHUqTg2Pk0PmZqLTSQN-A=', start_index=24542)
Annotation(end_index=24879, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjzKYGKVcEE_o-YKYBgecdMSXUHx3Vp-qIaVpA6Cl23TGcO5fhp37EPJAvRCgZ9NqFIkLE4r-97IFYhdZoX-9vqknOuaYEZF4UhDk4XqPN6CLlPYq0s0hGIRhCJwEgP8ZKRT3ybWthgyw=', start_index=24869)
Annotation(end_index=25009, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGskkutMSHd_Uke8vdgdFnVHsxYxG4QpdrHMn4cPHQdYsDmgLAPscZ0u3Y41aw5hV2f1Vj1sh1_6cKyqKxlmyjzeJUNF6_GdUnC96VRdQTOD8YsRhay', start_index=24999)
Annotation(end_index=25412, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAsh2DRWJ_Bs_hERbDsRfdThi2rOi8gWn0pgr2Ea-TkitnO0E46t8tn0FD4k03LAlcXPzb7rrS09zN6wje9J_nRum1f2oYRTccyErPU91z4M4JU0LbaGhN', start_index=25398)
Annotation(end_index=25412, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjzKYGKVcEE_o-YKYBgecdMSXUHx3Vp-qIaVpA6Cl23TGcO5fhp37EPJAvRCgZ9NqFIkLE4r-97IFYhdZoX-9vqknOuaYEZF4UhDk4XqPN6CLlPYq0s0hGIRhCJwEgP8ZKRT3ybWthgyw=', start_index=25398)
Annotation(end_index=26119, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyFbRvDc4xPjgQ-yjmug3El5dlE1pDwgGCbwg3eMi18aVRZs0j8nZSn6IRXETg5phjPA8TrYIarPUZ331AOETgm5d_wZFc390j-JPR1rfdlOgx2PxhbzEK-Av-q6aaRD-RTmToBKQZ', start_index=26106)
Annotation(end_index=26119, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrHwZG8Po4iZWEUblczdZVLvLpXe6PEQRRDpHjqGoeIn4iQu5Sk3--c55-6Cqzjfm-sEu1L5ODVj7MyyRhayhvBpir0cwVF-8epjvkPIpmn-TPXyepwL77PLeykAuuycH5bKWMhPPX7NWNca4wvZ21qljtrWw=', start_index=26106)
Annotation(end_index=26433, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI7nDct5lMoMmc3pfBE8QCwm7gNqncy0_XwtpwXdRCstryB3-6K3HMnBQzkL0gNlnZ9LPqh_PDLNW1WavL25gkU1_gErDQI9rI7nUBll4smfajuDdA-qxGPTqd20b5Yg==', start_index=26423)
Annotation(end_index=26733, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI7nDct5lMoMmc3pfBE8QCwm7gNqncy0_XwtpwXdRCstryB3-6K3HMnBQzkL0gNlnZ9LPqh_PDLNW1WavL25gkU1_gErDQI9rI7nUBll4smfajuDdA-qxGPTqd20b5Yg==', start_index=26719)
Annotation(end_index=26733, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdnHkw7-mW1M1O3zJ_tXjUIqxRWN0r4ur72U0la-mdR7GHiOeyeEhEP7kA41Zt0Bmb_XAik_yQ68pZneXGMdlYLkKa4Ntu-ifxGfnlCG-RiAgT0DydysgneBQryJowf4auo_I0jh6c', start_index=26719)
Annotation(end_index=27054, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzp4tqFpso-dYG-XU3EkJDUfsHSKaAvZSfXUc_HmTfVAd9e0TqwqkITfJMCOfPra1Vm1rZybauSkBSi0Adb650-eGTLXWYrhKooohCiG86yH9lQ0wt4ARhh0CXFLE9ybrSCFDEOun1BFvQhr2z_lZv6Q22vNGDZnvDudmHHZtU6NfJnHdu7lIZhHI1RQ5wj9YkN6T-1dUiTpF-mw==', start_index=27044)
Annotation(end_index=27487, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjzQNau7HXyt8J8rN6FeUFweCG4aFJetYWF2YBWp1_0s_5zXJd6pS3F2iaW3mqo-mih-oSzrWMkf0JMBiW1TyybhflSwE5ynfwLGwyBreIHPO8Stki5MZdWU51z5Vlc7XxaK3XpicnKuOoWJuCtykneLZkXxW5w-VBtxfCxvQT0Gqto62D8_ydFDHJJ4qGLvazRpuDQch4yzquDxLY', start_index=27477)
Annotation(end_index=27874, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUmd_qnXJe-ixQQAWhhriEr59NXxdhFo9sAVsEujuYOBmNIDXD70FkdiFGGZOJbXogrdlimB5GPnKV1SliVJgLE4RnkKj39LgEFgpeS-ZH8dDL_BZeSxI8wu67e3yILBsJUFS3Yi2ikRNsyQyYz06K1TsrkTDnpKZEbIYPcKO1PmS7yiCNHsJ0', start_index=27864)
Annotation(end_index=28719, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQkh0_YLLmMkjg_sNXnGPQl-2i9CbxTaHsUeHFvljXTI3IdFtNcrBQqp41gk1LHNYQ3axVEDG7dgxdfIAQ3eJK5w2zRoSwk1kFuthDsjulkrcINLhAGO01mtqmwID4HmwvJKXsTXg6', start_index=28710)
Annotation(end_index=28786, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAO3PezPB2u2aha9uNUcd4gtm7wOfwiTiCaghwIhP-XmwQd9KsdeDg3z3fvs5prSAX9XBqZiacAYGsHmox8nxMuV2LO-a501GOKoGTmq7HWp34xs2fdJWedb22K6qlSgf3ERtHUzMQv7J0t7Vry7LYS_uP-_fKeJ3xK6o5VQM8ixUKwUg5kEcSIEq0jMkVou2L-2ihGOSdZFor2NrVo-zu', start_index=28777)
Annotation(end_index=28863, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ3EhFOawbG6cCTWFqDue_rs9HwuL24lIzILPBaoA9HaO9q-fWk20YRujwsSh9qd19Kap39OKRyFPKSHkTaYHJjswaftj5KWjsYzODNlClpTv0M8VjaJ2qZ-rqVX9lrpiLuGOlJdU=', start_index=28854)
Annotation(end_index=28932, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyFbRvDc4xPjgQ-yjmug3El5dlE1pDwgGCbwg3eMi18aVRZs0j8nZSn6IRXETg5phjPA8TrYIarPUZ331AOETgm5d_wZFc390j-JPR1rfdlOgx2PxhbzEK-Av-q6aaRD-RTmToBKQZ', start_index=28923)
Annotation(end_index=29022, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcqEDw2nVuCelwm0BYXAhQ-MXrzLJBWLeCe6vH1WvACxeXm-M_cM4mSBySYgLlK8BvAJXtLiXkTQXaEl98tsf97Icv0-mkMIS9EuEKs3DEF9WGzb8yxdmz4cEC1Tsfv4JGOnyieLMKFSOKiAS1bC-u9eX56aXdYqOGxoVuoVequvbb9UuCbB3fZb96Fl0CxJe7UItlHMUZI9E=', start_index=29012)
Annotation(end_index=29096, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjzKYGKVcEE_o-YKYBgecdMSXUHx3Vp-qIaVpA6Cl23TGcO5fhp37EPJAvRCgZ9NqFIkLE4r-97IFYhdZoX-9vqknOuaYEZF4UhDk4XqPN6CLlPYq0s0hGIRhCJwEgP8ZKRT3ybWthgyw=', start_index=29086)
Annotation(end_index=29178, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZowjyTV2XWQlj8rMDLWZEXw3Z8O8fNFY2byUHAnNSWBKYJ4HyaqKCgG-AnEggXmGxG7967LDlF5gDOB1obKxnh9-VdXYj-Q53gvBS30RKHNQ92s-dU5kITT55MWakudcgcegz_if_wa1RggLA-Ace', start_index=29168)
Annotation(end_index=29281, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEMEHTKFfgfdKnp_x19Hkc3x9PsTu5YQbzN12AA28jZt1FGcxQSVLOPyd-21RbVqbfc-iK-r9ZGld_aBDT6_G0dh7tkB-YZysXOK2rbKoVK4yPzA9qHiDDIAJFpHZJneRBATT_8C1DepN8-0DDs29A0d3lEbq5n3y6wJtaTN3ZB-BM-vr7Fh0ju9Rcrvi2w5wHUqTg2Pk0PmZqLTSQN-A=', start_index=29271)
Annotation(end_index=29377, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1R6HXeFdrQGTmHw27WXGfPr-UO7gOvJ6mcZwpGYWMf1949fhBdasDshUMHzDRD4YyeqdkSI3kkKLYlgpaz0NNl9yZdEtHdiUW9Te1astmNwYN2QulKDWwLmF4MaVyHxrEHqgR4LGVf9hhVJWKfxDhF2rT8WvXZCFcSGGiq_7VHljbjY0rGLpMlGnw2B4oMuVHPg-PnLWmi3PGPiHXxzrj-w4E', start_index=29367)
Annotation(end_index=29442, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGskkutMSHd_Uke8vdgdFnVHsxYxG4QpdrHMn4cPHQdYsDmgLAPscZ0u3Y41aw5hV2f1Vj1sh1_6cKyqKxlmyjzeJUNF6_GdUnC96VRdQTOD8YsRhay', start_index=29432)
Annotation(end_index=29520, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhwOY3e667IFmUc4_SHxslwBAYg-Nc6J4Tbqy2I98AmwTIdsO_dbxqBsX8N7QkN0gF6giLBOuZkiVztAHf4b4PWB5exkzie7ECpNIlRf3kIysZ7foSdIJ32H2k7Rz1jLlmDfY7cfIucW04pK96da4sTx0g82pIouRGioRh', start_index=29511)
Annotation(end_index=29585, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzp4tqFpso-dYG-XU3EkJDUfsHSKaAvZSfXUc_HmTfVAd9e0TqwqkITfJMCOfPra1Vm1rZybauSkBSi0Adb650-eGTLXWYrhKooohCiG86yH9lQ0wt4ARhh0CXFLE9ybrSCFDEOun1BFvQhr2z_lZv6Q22vNGDZnvDudmHHZtU6NfJnHdu7lIZhHI1RQ5wj9YkN6T-1dUiTpF-mw==', start_index=29575)
Annotation(end_index=29682, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrA2kb3Mlt6Cnaqfnu8Ts0F2xFs-ye2MRMgU1QE-De91sLlvj6NVSmZuS5TivLwA6z2Qp0Asvk0BFira8xy2IkAkmsDySyphY4UYn6hUmioSo2yZ9TiKNwuqXCQV8U3DraJJz9Izd7xHRihRewIXyhBLX9LYXIJgbt_cSz2QY5xr5MBcXFLp2ly4O_tP8tdsBrgORG', start_index=29672)
Annotation(end_index=29770, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI7nDct5lMoMmc3pfBE8QCwm7gNqncy0_XwtpwXdRCstryB3-6K3HMnBQzkL0gNlnZ9LPqh_PDLNW1WavL25gkU1_gErDQI9rI7nUBll4smfajuDdA-qxGPTqd20b5Yg==', start_index=29760)

## Sources
