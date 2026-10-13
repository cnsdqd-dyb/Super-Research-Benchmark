# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** ff6a97f5 | **Time:** 129.04s | **Cost:** $1.10766
--------------------------------------------------------------------------------

# Network Topology Design for High-Performance Computing Clusters: Resolving the Latency-Scalability Contradiction

This comprehensive report examines how modern network topology design strategies address the fundamental tension between inter-node latency and cluster scalability while maintaining data efficiency and fault tolerance. Contemporary HPC cluster architectures employ hierarchical designs, adaptive routing mechanisms, and hybrid approaches that strategically balance these competing requirements. Through careful topology selection, intelligent path diversity management, and sophisticated congestion control techniques, modern HPC systems achieve predictable performance characteristics that scale from hundreds to tens of thousands of computing nodes while maintaining latency below critical thresholds for distributed computing workloads.

## Introduction to the HPC Network Design Paradox

The design of high-performance computing network fabrics presents a fundamental engineering paradox that has shaped the evolution of supercomputer architectures for over two decades[1][2]. As HPC clusters expand to support increasingly demanding applications—from artificial intelligence training to molecular dynamics simulations—network designers face an inherent contradiction: achieving lower inter-node latency typically requires more direct connections between nodes, while cost-effective scalability demands fewer switching stages and less interconnection infrastructure. This report addresses how contemporary HPC systems resolve this contradiction through sophisticated topology architectures, adaptive routing algorithms, and comprehensive fault tolerance mechanisms that work synergistically to deliver high-performance, scalable, and resilient computing environments.

The challenge becomes more acute as cluster sizes grow exponentially. In small clusters spanning tens of servers, simple topologies like star or basic mesh configurations suffice for distributing compute load. However, when clusters grow to hundreds or thousands of nodes, the bandwidth requirements scale dramatically, and the physical infrastructure costs become prohibitive if traditional approaches are naively extended. Modern HPC cluster designers must therefore employ topologies that provide high bisection bandwidth—the aggregate data rate that can traverse an imaginary cut dividing the cluster into two equal halves—while maintaining manageable costs and reasonable latencies for communication-intensive workloads[7]. The emergence of specialized topologies such as fat-tree, dragonfly, and torus networks, combined with advanced routing protocols and congestion management techniques, now allows systems to navigate this apparent contradiction rather than accept it as inevitable.

## Fundamental Topology Architectures and Their Performance Characteristics

### Fat-Tree Topology: The Dominant HPC Standard

The fat-tree topology has become the default choice for most modern HPC clusters because it directly addresses the latency-scalability tension through a carefully engineered compromise[1][2]. A fat-tree topology employs a hierarchical design with multiple layers of switches: leaf switches that connect directly to computing nodes, spine switches that aggregate traffic from leaf switches, and often core switches that provide additional connectivity layers in very large deployments. This architecture derives its name from the metaphor of a tree with branches that become progressively fatter (wider in bandwidth) as they approach the root, allowing the network to maintain consistent bandwidth regardless of which pairs of nodes attempt to communicate[1][7].

The key advantage of fat-tree topology for resolving the latency-scalability paradox lies in its provision of multiple equal-cost paths between any pair of nodes[2]. In a three-tier fat-tree configuration using 64-port switches, each with 32 downlinks to compute nodes or lower-tier switches and 32 uplinks to higher-tier switches, the topology can scale to accommodate 32,768 endpoints while maintaining full bisection bandwidth—meaning every server can simultaneously communicate at full link speed with every other server[2]. This property proves critical for distributed computing workloads where collective communication operations like all-reduce must execute predictably regardless of which GPUs or CPUs participate in the operation.

From a latency perspective, fat-tree provides consistent, predictable latency characteristics[2]. Any two nodes in a fat-tree topology are separated by at most three hops: from a leaf switch to a spine switch, then across spines, then down to the destination leaf switch. This bounded hop count ensures that latency remains relatively constant whether nodes communicate with immediate neighbors or distant cluster members, a property essential for synchronization operations in tightly coupled distributed applications. NVIDIA's reference architecture for DGX SuperPOD systems specifies fat-tree topology precisely because it ensures collective operations experience consistent performance regardless of GPU placement within the cluster[2].

The scalability properties of fat-tree topology demonstrate how increased switching investment directly translates to bandwidth provisioning. When additional bandwidth becomes necessary, administrators add more leaf switches and more uplinks to spine switches, maintaining the fundamental topology structure while increasing overall capacity. This incremental expansion path allows organizations to grow clusters without wholesale restructuring of the underlying fabric. However, this scalability advantage comes with operational complexity: fat-tree topologies require careful cabling discipline and switch configuration management to function effectively, and adding layers introduces additional switching costs that must be justified by bandwidth requirements[2].

### Dragonfly Topology: Cost Efficiency Through Localized Communication

The dragonfly topology represents an alternative approach that prioritizes cost efficiency over perfect bandwidth distribution[2][5]. A dragonfly network organizes switches into groups with dense intra-group connectivity achieved through full meshing within each group, while sparse inter-group links connect the groups together. Any two endpoints can communicate through at most three hops: from a local switch within the group, to a group switch, to a remote group switch, then to the destination[2]. This reduced hop count compared to some other topologies theoretically reduces latency for large-scale deployments.

The critical limitation of dragonfly topology, however, becomes apparent when examining communication patterns that stress inter-group links[2][5]. Workloads generating uniform random traffic across all cluster endpoints—where any node must potentially communicate with any other node with equal probability—can exceed the capacity of inter-group links, causing bottlenecks that degrade overall cluster performance. The dragonfly topology therefore works well for applications exhibiting localized communication patterns where most traffic remains within groups, but may struggle with large-scale distributed training using global collective operations that require all-to-all communication[2].

The cost advantages of dragonfly stem from requiring fewer switches than fat-tree at equivalent scale—fewer switches reduce both capital expenditure and power consumption[2]. For organizations with workloads exhibiting known communication locality patterns, dragonfly provides an attractive cost-performance tradeoff. However, the topology's limitations for synchronization-heavy workloads and its requirement for careful workload characterization before deployment make it less universally applicable than fat-tree for general-purpose HPC environments.

### Torus and Mesh Topologies: Direct Connectivity Approaches

Three-dimensional torus and mesh topologies provide alternative approaches emphasizing direct node-to-node connectivity while managing the inherent constraints of these designs[3]. A torus topology connects computing nodes in a three-dimensional grid where nodes connect to their six nearest neighbors (two in each dimension), with wraparound connections in each dimension creating the toroidal structure. This approach maximizes locality of communication since physically proximate nodes in the torus correspond to nearby computing tasks, reducing average hop distances for well-mapped applications.

Torus topologies offer several advantages for specific application classes, particularly stencil codes and structured grid simulations where communication patterns align naturally with the topological structure[3]. The high bisection bandwidth of well-designed torus networks—particularly compared to some naive hierarchical designs—and their relatively low cost make them attractive for certain workload profiles. However, torus topologies require careful task mapping to exploit their locality properties, and applications with irregular communication patterns may not benefit from the topology's structure. Additionally, torus networks typically require more sophisticated routing algorithms to avoid deadlock conditions and fairly distribute traffic across multiple potential paths[3].

### Emerging Hybrid and Rail-Optimized Architectures

Recent developments in AI and HPC cluster design have introduced hybrid topologies that combine elements of multiple topology types to optimize for specific workload characteristics[2][25]. Rail-optimized architectures, for instance, connect same-index GPUs across different racks using dedicated horizontal switch layers, enabling single-hop communication for synchronized training workloads while maintaining some of the management simplicity of traditional rack-based architectures[25]. This approach balances the ultra-low latency requirements of collective operations in large-scale AI training against the operational complexity of pure mesh-based interconnects.

Hybrid topologies more generally represent an acknowledgment that no single topology perfectly satisfies all HPC requirements[1]. By combining fat-tree structures for general-purpose communication with specialized interconnects like NVLink for intra-node GPU communication or dedicated paths for collective operations, hybrid approaches enable architects to optimize distinct traffic classes separately. For example, a cluster might employ fat-tree topology for inter-node Ethernet or InfiniBand communication while leveraging NVLink Switch technology within node groups to provide dedicated, ultra-high-bandwidth paths for frequent peer-to-peer GPU communication[2][25].

## Latency Optimization and Performance Consistency

### Understanding Latency Components and Impact

Latency in HPC networks comprises several distinct components that collectively determine application performance[1][7]. The first component, packet transmission latency, depends on link speed and packet size—a simple physics calculation of bits divided by bandwidth. More significantly for HPC systems, routing latency encompasses the time required for network switches to examine packet headers and determine output ports, typically ranging from several hundred nanoseconds to a few microseconds depending on switch architecture. Propagation latency stems from the finite speed of light through optical fibers or copper cables, creating distance-dependent delays. Finally, queuing latency arises when switch output ports become temporarily congested and packets must wait in buffers before transmission.

For tightly synchronized distributed computing applications, latency proves critical because all tasks must often wait at synchronization barriers until every participating process completes its communication phase[1][7]. If latency varies dramatically between different node pairs, faster processes must wait for slower ones, causing "tail latency" issues where overall application performance becomes dominated by the slowest communicating pair. This effect becomes particularly severe in large-scale collective operations like all-reduce where latency directly translates to application execution time.

### Adaptive Routing and Congestion Management

Modern HPC systems employ adaptive routing algorithms that dynamically select communication paths based on real-time network conditions, allowing packets to avoid congested areas and minimize queuing delays[15][18]. NVIDIA's InfiniBand adaptive routing implementation, for example, can achieve 96% network efficiency by spreading traffic across multiple parallel paths and load-balancing based on egress port queue depths[15]. Instead of routing all traffic destined for a particular output port along a single path, adaptive routing allows different packets of the same flow to traverse different paths when one becomes congested, improving overall bandwidth utilization.

Adaptive routing particularly benefits large fat-tree deployments where multiple equal-cost paths exist between most node pairs[15][18]. By continuously monitoring congestion indicators and rerouting traffic away from congested links, adaptive routing maintains lower average latencies than static routing schemes that always select the same path regardless of current network state. Research on production HPC systems demonstrates that adaptive routing improved application performance by approximately 10% on molecular dynamics simulations and similar communication-intensive workloads[15]. The algorithm works through a grading mechanism that considers egress port queue depth and path priority, preferring shorter paths but accepting slightly longer paths to avoid congestion.

The challenge of maintaining in-order packet delivery while enabling adaptive routing received attention in recent work on flowcut switching algorithms[18]. Traditional per-packet adaptive routing risks reordering packets from the same flow when they traverse different paths with different latencies. For protocols like RoCE (RDMA over Converged Ethernet) that depend on in-order delivery for efficient operation, such reordering can catastrophically impact performance. Flowcut switching addresses this by ensuring that consecutive packets of a flow traverse the same path until an explicit rerouting decision is triggered by timing-based congestion detection, providing the performance benefits of adaptive routing while guaranteeing in-order delivery.

### InfiniBand Congestion Control Architecture

InfiniBand networks include sophisticated congestion control mechanisms at multiple layers that work to maintain low latency even under heavy load[17]. At the link layer, flow control ensures that sending ports cannot transmit more data than receiving ports can accept through a credit-based system. When a receiving port's buffer fills up, it stops returning credits to the upstream sending port, causing the sender to pause automatically. This prevents packet loss but can cause congestion to propagate upstream in the network.

At the transport layer, InfiniBand's congestion control includes explicit congestion notification (ECN) mechanisms where switches mark packets when detecting congestion by setting the Forward ECN (FECN) bit[17]. When a receiving host detects marked packets, it responds with Backward ECN (BECN) messages directed to the original sender's queue pair. The sender then reduces its transmission rate according to a configured congestion control table. This two-sided approach—link-layer credit-based flow control combined with transport-layer rate reduction—provides more sophisticated congestion management than traditional Ethernet, which relies primarily on packet loss and TCP timeouts to signal congestion.

## Scalability Analysis and Bisection Bandwidth Constraints

### Bisection Bandwidth as the Critical Scalability Metric

Bisection bandwidth—the aggregate data rate that can cross an imaginary line dividing a network into two equal halves—serves as the primary metric for evaluating whether a network topology can sustain balanced communication patterns at scale[7][10]. For a network to avoid becoming bottlenecked as cluster size grows, bisection bandwidth must scale proportionally with the number of nodes. If a cluster doubles in size but bisection bandwidth fails to double correspondingly, the network becomes increasingly oversubscribed, meaning that not all nodes can simultaneously communicate at full link rate.

Different topologies exhibit vastly different bisection bandwidth scalability characteristics[10]. In a fully connected mesh where every node connects directly to every other node, bisection bandwidth grows quadratically with the number of nodes—a 1,000-node cluster would require nearly 500,000 connections, making this topology completely impractical[1][10]. A ring topology, where nodes connect in a circle with each node having two neighbors, provides very limited bisection bandwidth that scales poorly—the minimum bisection requires cutting only two links, regardless of cluster size[10]. Star topologies concentrate all inter-node traffic through a single central switch, causing severe bottlenecks that make them suitable only for very small clusters.

Fat-tree topologies, properly designed with adequate oversubscription ratios, maintain constant bisection bandwidth as clusters scale[7]. This scaling comes from increasing the number of spine switches and the uplinks connecting leaf and spine layers. The architecture essentially adds bandwidth proportionally with cluster size, avoiding the bifurcation of other topologies. A three-tier fat-tree using 64-port switches with an oversubscription ratio of 1:1 (meaning no oversubscription—every server can communicate at full bandwidth with every other server simultaneously) scales to 32,768 compute nodes while maintaining full bisection bandwidth[2].

### Oversubscription Ratios and Cost-Performance Tradeoffs

In practice, many HPC deployments employ oversubscribed topologies where bisection bandwidth is deliberately limited to reduce costs[9][44]. An oversubscribed network intentionally provides less bandwidth in the upper layers than in the lower layers, accepting that not all nodes can simultaneously achieve full-bandwidth communication. Organizations typically employ oversubscription ratios ranging from 2:1 to 8:1, meaning that only a fraction of theoretical peak bandwidth can actually traverse the network simultaneously[44].

This apparent compromise actually enables practical scalability because applications rarely require all nodes to simultaneously communicate at peak bandwidth[9]. Most HPC workloads exhibit communication patterns where subsets of nodes exchange data while others compute, creating natural communication phases that fit within oversubscribed network capacity. By accepting controlled oversubscription, organizations can build much larger clusters than would be possible with non-oversubscribed topologies, because the per-node cost of networking decreases substantially with higher oversubscription ratios[44]. A 9:1 oversubscribed network can support roughly three times as many nodes as a 1:1 oversubscribed network using the same number of switches.

However, oversubscription introduces performance risks when applications generate uniform random communication patterns that stress inter-layer links beyond capacity[9]. In such scenarios, queue buildup occurs at oversubscribed links, latency increases unpredictably, and application performance degrades. Network operators must therefore characterize expected workload communication patterns and select oversubscription ratios that accommodate expected peak traffic without causing congestion for typical workloads.

## Data Efficiency and Bandwidth Utilization

### Collective Communication Optimization in Large-Scale Clusters

Collective communication operations—where multiple processes exchange data in coordinated patterns like all-reduce, broadcast, or scatter—constitute a significant portion of many HPC application execution times, particularly for distributed machine learning and scientific simulations[13][16][43]. The efficiency of these operations directly depends on network topology and the algorithms used to implement them, making optimization crucial for overall cluster performance.

Recent work on collective communication frameworks emphasizes the importance of topology awareness and multi-path communication strategies[13]. GPU-aware collective communication libraries like NVIDIA's NCCL optimize Allreduce operations by carefully scheduling data transfers to minimize latency while maximizing bandwidth utilization. For multi-node, multi-GPU systems, these libraries must consider both intra-node communication (where GPUs connect via NVLink or PCIe) and inter-node communication (via Ethernet or InfiniBand), selecting appropriate algorithms for each path based on available bandwidth and latency characteristics[13].

Research on zero-copy collective communications demonstrates the importance of eliminating unnecessary data copies and buffer staging operations[16]. Traditional collective implementations perform intermediate buffering, increasing latency by requiring data to pass through multiple CPU memory locations before network transmission. Zero-copy designs allow network interface cards to perform remote direct memory access (RDMA) directly between application buffers, bypassing CPU and memory hierarchy intermediaries. For a 100,000+ GPU cluster spanning multiple datacenters, these optimizations prove critical—communication latency increases dramatically with network distance, creating 7x, 15x, and 30x differences between same-rack, same-zone, and same-datacenter communication respectively[16].

Dynamic queue pair load balancing techniques specifically address the challenge of managing outstanding data in flight across multiple paths[16]. Rather than allowing unlimited RDMA sends, systems can configure per-connection and per-topology send queues that limit the total unacknowledged data. More conservative limits work well for close communication (same-rack) where bandwidth-delay product is small, while more aggressive limits are required for distant communication paths with large bandwidth-delay products. This dynamic approach maintains efficient link utilization without creating excessive buffering that causes congestion.

### MPI and RDMA Protocol Optimization

The Message Passing Interface (MPI) standard, nearly universal in HPC computing, includes sophisticated mechanisms for optimizing communication efficiency across diverse hardware platforms[34]. Early implementations of RDMA protocols for MPI demonstrated that careful management of memory registration—the process of registering application memory buffers with the RDMA hardware—significantly affects bandwidth[34]. Dynamic memory registration where application buffers are registered on-demand rather than pre-registered proved most effective for applications that don't reuse the same buffers repeatedly, achieving up to 67% bandwidth improvements in some scenarios[34].

Pipeline protocols that overlap memory registration with data transfer represent another important optimization technique[34]. Rather than fully registering an entire large message, sending the data, then deregistering, pipeline protocols eagerly send the first portion using traditional send/receive semantics while simultaneously registering subsequent blocks through RDMA operations. Once registration completes, subsequent portions transfer via RDMA at peak bandwidth. This approach amortizes registration costs across the message lifetime and leverages the different performance characteristics of different communication phases.

Bandwidth-saving optimizations for collective operations demonstrate how understanding specific topology structures enables algorithmic improvements[43]. For MPI broadcast operations, naive ring-allgather algorithms can generate redundant data transmissions where processes receive the same data chunks repeatedly. By modifying the ring-allgather algorithm to track which data chunks each process already possesses and only transmit missing chunks, researchers achieved 12-30% bandwidth savings for large messages[43]. These algorithmic improvements particularly benefit oversubscribed networks where every bit of bandwidth savings translates to reduced congestion and improved application performance.

## Fault Tolerance and Resilience Mechanisms

### Network-Level Redundancy and Path Protection

Modern HPC clusters must tolerate component failures ranging from individual link failures to switch malfunctions while maintaining application availability[6][37][40]. Network designers employ redundancy at multiple levels to achieve this resilience. The most basic approach involves providing alternative paths between any pair of nodes, allowing traffic to automatically reroute around failed links. Fat-tree topologies inherently provide path diversity since multiple paths exist between most node pairs with equal hop counts, enabling automatic rerouting without application awareness[6].

InfiniBand's Automatic Path Migration (APM) feature enables network interface cards to detect failures on the primary communication path and seamlessly switch to alternate paths without application interruption[6]. When an InfiniBand queue pair (the fundamental communication endpoint) detects transmission errors indicating link failure, the HCA hardware loads an alternate pre-specified path and resumes communication. This hardware-level response occurs in microseconds, potentially before the network or application software even detects the failure. The approach works well for scenarios where disjoint paths exist between source and destination, but becomes problematic in oversubscribed fat-tree topologies where all paths may share bottleneck links.

A hybrid approach combining hardware-level APM with software-level detection and recovery provides more robust fault tolerance[6]. When hardware path migration fails—typically because both primary and alternate paths traverse a failed intermediate link—software mechanisms detect the failure through timeout and absence of acknowledgments. Software can then request connection re-establishment through out-of-band management channels, rerouting around failed intermediate equipment. This two-level approach ensures that most failures recover quickly through APM while software mechanisms catch cases where APM alone proves insufficient.

### Redundancy in Topology Design and Link Aggregation

At higher levels, network designers employ protocols like Link Aggregation Control Protocol (LACP) that bundle multiple physical links into a single logical connection, providing automatic failover when individual links fail[37][40]. If one physical link in a four-link aggregate fails, traffic automatically distributes across the remaining three links without dropping packets or disrupting applications. Modern switches like Cisco's Virtual Port Channel (VPC) extend link aggregation across multiple switches, creating multi-chassis aggregates where both switches in a redundant pair are active simultaneously, improving utilization compared to traditional active-passive failover designs[37].

Spanning Tree Protocol (STP) and its faster variants (RSTP, MSTP) prevent loops in layer-2 networks while providing redundancy by blocking certain links during normal operation but enabling them as backups when primary paths fail[37]. While STP allows zero downtime during active-passive failovers, its slower convergence time and operational complexity make it less preferred for modern HPC networks than newer protocols. Virtual Router Redundancy Protocol (VRRP) and Hot Standby Routing Protocol (HSRP) provide similar redundancy at layer 3, allowing multiple routers to share a virtual IP address with automatic failover when the primary router fails[37][40].

For maximum resilience, network designers typically implement redundancy at multiple layers simultaneously, but must carefully coordinate these mechanisms to ensure consistent behavior[37][40]. For example, the device serving as the spanning tree root bridge at layer 2 should ideally be the same device acting as the primary VRRP gateway at layer 3, preventing traffic from asymmetrically looping through the network. Keeping redundancy mechanisms parallel—with an A-path and B-path through the network with cross-connections at each layer—provides the maximum availability while maintaining simplicity and avoiding loops.

### Software-Defined Networking for Dynamic Recovery

Software-defined networking (SDN) approaches enable more sophisticated failure recovery by centralizing network control logic in a controller that maintains global topology awareness[33][36]. Rather than relying on distributed protocols like spanning tree that make local decisions, SDN controllers can compute optimal routing paths considering the complete network state and application requirements. When failures occur, controllers detect them through topology discovery or explicit notification and compute new paths that avoid failed infrastructure.

SDN provides particular benefits for HPC networks supporting multiple concurrent experiments or job types, where different workloads benefit from different network configurations[20]. An SDN controller can dynamically create virtual network slices, allocating specific network resources to specific jobs and isolating their traffic from other jobs. When a job completes or fails, the controller reclaims its network resources and reallocates them to other uses. This dynamic allocation improves overall cluster utilization compared to static network configurations where resources remain reserved even when unused.

## Emerging Technologies and Future Directions

### NVLink and Proprietary GPU Interconnects

NVIDIA's NVLink technology represents a specialized approach to addressing the latency-scalability problem for GPU-rich clusters[45][48]. NVLink provides direct, all-to-all GPU-to-GPU communication within a server at 3.6 TB/s bandwidth per GPU in the latest generation, and NVLink Switch extends these capabilities across multiple servers[45]. A Vera Rubin NVL72 system connects 72 GPUs in a fully non-blocking fabric with 260 TB/s aggregate bandwidth, effectively treating 72 GPUs as a single computational unit for collective operations[45].

This specialized interconnect strategy represents an acknowledgment that generic network topologies optimized for general-purpose communication may not achieve adequate performance for GPU-to-GPU communication in large-scale AI training[28]. By deploying proprietary high-bandwidth, low-latency interconnects specifically designed for GPU communication patterns, systems can achieve collective operation performance unachievable through Ethernet or InfiniBand alone. However, this approach comes with vendor lock-in costs, as organizations become dependent on NVIDIA's specific architectures and cannot easily mix GPUs from different vendors.

Complementary work on multi-path communication frameworks shows how heterogeneous compute resources can be leveraged to enhance collective operations[13]. Rather than relying solely on network bandwidth, systems can utilize both CPU and GPU computation, overlapping network transfers with computation to hide latency. CPU threads can manage different communication paths simultaneously, exploiting both high-performance NVLink paths and standard Ethernet paths in parallel, improving overall collective operation throughput by up to 1.45x compared to standard libraries.

### Optical Circuit Switching and Reconfigurable Networks

Emerging optical circuit switching technologies offer potential solutions to the bandwidth scalability problem by enabling dynamic reconfiguration of network topology[21][57][60]. Rather than maintaining a fixed physical topology, optical circuit switches (OCS) can establish and tear down optical circuits in seconds or minutes, allowing datacenter operators to reconfigure network connectivity based on current workload demands. A traditional fat-tree supporting a fixed topology wastes bandwidth on links that don't currently carry traffic while remaining congested on links that do; optical circuit switching allows temporary reallocation of fiber capacity to match current demand.

Companies like HUBER+SUHNER have deployed POLATIS optical circuit switching technology as part of SCinet, the temporary network supporting SC (SuperComputing) conferences, and work like COUDER (Convex Optimization with Uncertainty Desensitization) proposes algorithms for optimizing topology engineering in optical switched networks[21][57]. While complete second-scale dynamic reconfiguration introduces excessive control-plane overhead, quasi-static reconfiguration at daily or hourly timescales can achieve significant efficiency improvements—approximately 20% lower maximum link utilization and 32% lower average hop count compared to static topologies[21].

The challenge lies in making reconfiguration decisions safely without disrupting in-flight traffic. Topology engineers must carefully drain links of live traffic before disconnecting them and stage reconfigurations to ensure sufficient capacity remains available during the transition period[21]. Even with these constraints, the flexibility of reconfigurable optical networks provides an intriguing approach to balancing predictable topology structure for network design with dynamic adaptation to evolving workload demands.

## Monitoring, Observability, and Topology-Aware Resource Management

### Host-Side and Network-Level Observability

Understanding network performance requires comprehensive observability across both application and infrastructure layers[27][30]. Recent work on eBPF-based telemetry systems demonstrates how host-side monitoring can correlate GPU performance with network activity, identifying cases where NIC contention, PCIe pressure, or CPU interference causes latency spikes[27]. By capturing host-level signals through kernel instrumentation and correlating them with GPU metrics from NVIDIA's NCCL library, operators can diagnose root causes of performance variability without requiring cluster-wide fabric instrumentation.

These observability systems operate with minimal overhead—approximately 1.21% CPU utilization at 100Hz sampling—while achieving 81-88% diagnostic accuracy and detecting latency spikes within 5 seconds[27]. For multi-tenant HPC environments where multiple workloads compete for shared infrastructure resources, such rapid identification of performance issues enables quick remediation and improved overall cluster utilization. The approach extends naturally to distributed multi-node scenarios where per-node agents aggregate telemetry to a centralized correlation engine.

Network observability for InfiniBand systems typically focuses on monitoring link utilization, flow control credit stalls, and congestion events[14][30]. A measurement study of congestion in production InfiniBand HPC clusters found that congestion occurs surprisingly frequently—in approximately 60% of 100-millisecond measurement intervals, top-of-rack switch ports stalled waiting for flow control credits[14]. This congestion, driven by both I/O operations and compute-node cluster traffic, directly impacts application performance for communication-intensive jobs. Understanding these dynamics enables better scheduling decisions, where communication-intensive jobs can be scheduled when network utilization is lower.

### Topology-Aware Job Scheduling and Resource Allocation

The communication patterns of HPC applications—which nodes communicate with which—significantly affect performance depending on the underlying network topology[3][49][52]. A topology mapping problem seeks to allocate computing nodes and schedule application tasks on those nodes to minimize communication overhead given the application's communication topology and the network's physical topology[3]. This NP-hard problem admits various approximation algorithms and heuristics that can improve application performance by 2-3% through better task placement, with potential improvements reaching 7% in favorable scenarios[3].

Topology-aware resource managers integrate topology knowledge into job scheduling decisions, attempting to place highly communicating tasks on nodes that are topologically close in the network[49][52]. Rather than treating the cluster as a homogeneous pool of interchangeable resources, these systems recognize that some node pairs communicate more efficiently than others and use this knowledge to improve application placement. For example, TreeMatch algorithm uses tree-structured matching between application communication graphs and network topology graphs to identify node allocations that minimize communication overhead[49].

The effectiveness of topology mapping depends critically on understanding the specific workload's communication pattern and how it aligns with the network topology[3]. Applications exhibiting stencil-structured communication, where each task primarily communicates with its nearest neighbors, benefit substantially from torus topologies. Applications with all-to-all communication patterns require network topologies providing excellent bisection bandwidth regardless of node placement. Workloads with irregular or highly variable communication patterns may not benefit from topology-aware placement if the communication pattern varies between runs or if obtaining complete knowledge of the communication topology adds excessive overhead.

## Comprehensive Design Recommendations and Best Practices

### Selecting Topologies Based on Workload Characteristics

The choice of network topology should fundamentally depend on the specific workloads that will run on the HPC cluster and the organization's scalability expectations[1][2][22]. For general-purpose clusters supporting diverse applications with dynamic communication patterns, fat-tree topology remains the superior choice because it provides predictable performance characteristics regardless of which nodes communicate[2]. The full bisection bandwidth ensures that collective operations complete reliably without bottlenecking, and the bounded latency ensures consistent application performance.

For clusters with known localized communication patterns, dragonfly topology offers compelling cost advantages, but only after careful workload characterization and simulation[2][5]. The topology's superior cost-efficiency relative to fat-tree makes it attractive for budget-constrained deployments, but requires ongoing monitoring to ensure actual workload patterns match design assumptions. If unexpected global communication patterns emerge, performance degradation can be severe, making dragonfly riskier for exploratory or dynamic computing environments.

Specialized topologies like torus may be justified when supporting specific application classes with communication patterns that naturally align with the topology structure[3]. Scientific simulation codes using stencil computations on three-dimensional grids map naturally onto torus topologies, maximizing locality of communication. However, for general-purpose clusters supporting diverse workloads, the additional complexity of torus routing and task mapping typically outweighs benefits.

### Infrastructure Investment and Cost-Performance Analysis

Organizations should develop comprehensive total cost of ownership (TCO) models when selecting network topology and hardware infrastructure[55]. While initial equipment costs receive significant attention, research indicates that infrastructure and operational costs often exceed initial purchase price over the system's useful lifetime. A complete TCO analysis should consider capital expenditure for network equipment, annual maintenance and support costs, power consumption and cooling expenses, staff salaries for operation and optimization, facility costs, and potential hardware upgrades[55].

For very large clusters, the cost differences between topologies become substantial. A non-oversubscribed fat-tree cluster supporting thousands of nodes requires extensive switching investment in upper network layers—the number of switches and their aggregated cost grows with cluster size. An equivalent dragonfly cluster supporting the same node count requires significantly fewer switches and lower overall infrastructure costs. However, if the cluster will support workloads generating uniform random communication patterns, the dragonfly cost advantage may vanish through degraded performance, increased job execution times, and wasted resources.

Oversubscription decisions fundamentally affect infrastructure cost and performance tradeoffs[44]. Higher oversubscription ratios reduce per-node networking costs significantly but increase congestion risk for bandwidth-intensive workloads. Organizations with diverse workloads should select oversubscription ratios slightly lower than expected peak demand, accepting that occasionally workloads will experience congestion while maintaining typical performance within specification. Oversubscription ratios of 2:1 to 4:1 typically represent reasonable compromises, providing acceptable costs while limiting congestion risks.

### Redundancy and Fault Tolerance Strategy

Fault tolerance mechanisms should be implemented at multiple levels—physical infrastructure redundancy, link-layer protocols, and software recovery mechanisms—with careful coordination ensuring consistent behavior[37][40]. For mission-critical clusters, objectives of "five nines" or higher availability (99.999% uptime) demand comprehensive redundancy across all critical systems. Redundant network paths should be truly diverse, using different cables, switches, and infrastructure whenever possible to ensure that common-mode failures don't disable all backup paths.

Organizations should implement monitoring and alerting systems that detect failures within seconds and notify operators immediately[30]. Automated recovery mechanisms can restore many failure scenarios transparently without operator intervention, but operators must remain engaged to handle complex scenarios where automated recovery proves insufficient. Network redundancy protocols should be tested regularly through failure scenarios, verifying that mechanisms work as expected under realistic conditions. Many organizations discover that their redundancy systems don't function correctly only when actual failures occur—deploying these systems and then never validating them guarantees failures in recovery when needed.

### Network Design and Implementation

Proper network design requires careful attention to physical layer details including cable quality, routing infrastructure, and signal integrity maintenance[1][19]. Poor cabling practices—excessive cable lengths, unsuitable cable types, or improper termination—introduce signal degradation that increases latency and reduces effective link speeds. High-quality cabling infrastructure, while more expensive initially, pays dividends through improved reliability and performance consistency throughout the system's lifetime[19].

Documentation of the network topology and logical connectivity should be maintained meticulously, supporting troubleshooting and enabling informed decision-making about upgrades and expansion[47]. Tools that automatically discover and map network topology can generate visual representations showing physical connections, but these should be verified against documentation and updated as changes occur. Well-maintained documentation proves invaluable when failures occur or when planning expansion projects.

## Conclusion: Integrated Solutions to the Latency-Scalability Paradox

The apparent contradiction between inter-node latency and cluster scalability has been substantially resolved through sophisticated modern network topology design combining multiple complementary approaches. Fat-tree topologies, which dominate contemporary HPC clusters, fundamentally address the paradox by providing high bisection bandwidth through hierarchical switching while maintaining bounded latency through limited hop counts. This core topology can be enhanced through adaptive routing algorithms that dynamically load-balance traffic to minimize congestion, specialized interconnects like NVLink for dense GPU communication, and comprehensive fault tolerance mechanisms ensuring resilience to infrastructure failures.

The resolution involves accepting that perfect optimization across all dimensions remains impossible—trade-offs must be made based on specific workload characteristics and organizational priorities[1][2][7]. Organizations building general-purpose clusters supporting diverse workloads should prioritize fat-tree topology for its consistent performance and excellent scalability characteristics, accepting higher infrastructure costs as the price of predictable performance. Those with specialized workload profiles may find alternative topologies offering superior cost efficiency, but must carefully characterize workloads and monitor performance in production to verify assumptions hold.

Data efficiency improvements through topology-aware collective communication optimization, multi-path communication strategies, and dynamic load balancing ensure that the substantial bandwidth provisioned in modern HPC networks translates into actual application performance improvements[13][16][34]. Fault tolerance mechanisms at multiple layers—physical redundancy, link-level protocols, and software recovery—maintain resilience without requiring overcounting of infrastructure at every level, allowing cost-effective reliability through intelligent risk management[6][37][40].

Future directions for HPC network design include greater integration of specialized interconnects for specific device types, optical circuit switching for dynamic topology reconfiguration, and sophisticated machine learning-based traffic prediction and routing optimization[16][21][51][60]. These emerging technologies promise to further improve the efficiency of HPC networking while maintaining the backward compatibility and operational familiarity that makes contemporary networks practical to operate at scale. Through continued innovation combining new technologies with proven architectural principles, HPC clusters will continue to scale to exascale performance while maintaining the low-latency, high-reliability characteristics demanded by increasingly ambitious scientific and engineering applications.

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Networking Considerations for Multi-Node Computing Deployments', 'url': 'https://www.exxactcorp.com/blog/hpc/networking-considerations-for-multi-node-computing-deployments'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'GPU Cluster Network Topology Design | Introl Blog', 'url': 'https://introl.com/blog/gpu-cluster-network-topology-fat-tree-dragonfly-rail-optimized-2025'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Efficient Topology Mapping in HPC - Circuit Cellar', 'url': 'https://circuitcellar.com/research-design-hub/basics-of-design/efficient-topology-mapping-in-hpc/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Understanding HPC Cluster Network Topologies | Microsoft Learn', 'url': 'https://learn.microsoft.com/en-us/powershell/high-performance-computing/understanding-hpc-cluster-network-topologies?view=hpc19-ps'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Dragonfly vs. Fat-tree -- the Future of Cluster Topologies - YouTube', 'url': 'https://www.youtube.com/watch?v=cLSn7Q0QXG4'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] An Efficient Hardware-Software Approach to Network Fault ...', 'url': 'https://hpc.pnl.gov/people/vishnu/public/vishnu_cluster09.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'HPC networking: a ballad in four parts. (Part 2: Bandwidth)', 'url': 'https://dug.com/hpc-networking-a-ballad-in-four-parts-part-2-bandwidth/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] CLOT: A Cost-effective Low-latency Overlaid Torus-based Network ...', 'url': 'https://tingwang1122.github.io/files/CLOT_Conf.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'How does oversubscription affect the performance of HPC ...', 'url': 'https://massedcompute.com/faq-answers/?question=How+does+oversubscription+affect+the+performance+of+HPC+applications%3F'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] CS470 Networks - Computer Science - JMU', 'url': 'https://w3.cs.jmu.edu/lam2mo/cs470_2023_01/files/13_networks.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Optimizing All-to-All Collective Communication with Fault Tolerance ...', 'url': 'https://dl.acm.org/doi/10.1145/3725843.3756057'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The consequences of congestion - Cerio', 'url': 'https://www.cerio.io/wp-content/uploads/2023/09/Consequences-of-Congestion-White-Paper-Cerio.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Collaborative Bandwidth-Efficient Intra-Node Allreduce', 'url': 'https://www.queensu.ca/academia/afsahi/pprl/papers/AsHES-2025.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Measurement Study of Congestion in an InfiniBand Network', 'url': 'https://tma.ifip.org/wordpress/wp-content/uploads/2017/06/tma2017_paper18.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] NVIDIA InfiniBand Adaptive Routing Technology—Accelerating HPC ...', 'url': 'https://www.amax.com/content/files/2023/12/NVIDIA_InfiniBand_Adaptive_Routing_Technology_Insights_Whitepaper.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Collective Communication for 100k+ GPUs - arXiv', 'url': 'https://arxiv.org/html/2510.20171v3'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Deploying Quality of Service and Congestion Control in InfiniBand ...', 'url': 'https://network.nvidia.com/files/related-docs/whitepapers/deploying_qos_wp_10_19_2005.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Flowcut Switching: High-Performance Adaptive Routing with ... - arXiv', 'url': 'https://arxiv.org/html/2506.21406v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Networking Considerations for Multi-Node Computing Deployments', 'url': 'https://www.exxactcorp.com/blog/hpc/networking-considerations-for-multi-node-computing-deployments'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Network Slicing to Improve Multicasting in HPC Clusters', 'url': 'https://scholarworks.boisestate.edu/cs_facpubs/161/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Enabling Quasi-Static Reconfigurable Networks With Robust ...', 'url': 'https://lightwave.ee.columbia.edu/sites/default/files/content/publications/2022/Enabling_Quasi-Static_Reconfigurable_Networks_With_Robust_Topology_Engineering.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'How to Build a High Performance Computing Cluster - Supermicro', 'url': 'https://learn-more.supermicro.com/data-center-stories/how-to-build-a-high-performance-computing-cluster'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Network slicing to improve multicasting in HPC clusters', 'url': 'https://dl.acm.org/doi/abs/10.5555/3287988.3288001'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Dynamic Network Reconfiguration Algorithm', 'url': 'http://article.sapub.org/10.5923.j.computer.20130302.05.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Rail vs ToR Architectures: Which Is Best for AI Clusters? - DriveNets', 'url': 'https://drivenets.com/blog/rail-vs-tor-architectures-which-is-best-for-ai-clusters/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] High-Performance Architectures for High-Radix Switches', 'url': 'https://riunet.upv.es/bitstreams/2c9ca452-d826-43e0-895d-e43df0005209/download'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Host-Side Telemetry for Performance Diagnosis in Cloud and HPC ...', 'url': 'https://arxiv.org/html/2510.16946v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Deploying NVIDIA H200 NVL at Scale with New Enterprise ...', 'url': 'https://developer.nvidia.com/blog/deploying-nvidia-h200-nvl-at-scale-with-new-enterprise-reference-architecture/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Analyzing Cost-Performance Tradeoffs of HPC Network Designs ...', 'url': 'https://dl.acm.org/doi/pdf/10.1145/3316480.3325516'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Optimize HPC jobs and cluster utilization with Datadog', 'url': 'https://www.datadoghq.com/blog/hpc-monitoring/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'RDMA Explained: The Backbone of High-Performance Computing', 'url': 'https://www.digitalocean.com/community/conceptual-articles/rdma-high-performance-networking'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] High-Performance Routing with Multipathing and Path Diversity in ...', 'url': 'https://arxiv.org/pdf/2007.03776.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] MPI aware routing using SDN - HPDC', 'url': 'https://hpdc.sci.utah.edu/2017/posters/poster_files/poster13.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] High Performance RDMA Protocols in HPC - Open MPI', 'url': 'https://www.open-mpi.org/papers/euro-pvmmpi-2006-hpc-protocols/euro-pvmmpi-2006-hpc-protocols.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] High-Performance Routing With Multipathing and Path Diversity in ...', 'url': 'https://htor.inf.ethz.ch/publications/img/besta-TPDS21-routing.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Dynamic Network Scheduler for Cloud Data Centres with SDN', 'url': 'https://dl.acm.org/doi/10.1145/3147213.3147217'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Redundancy concepts for hierarchical switch networks', 'url': 'https://www.lancom-systems.fr/fileadmin/download/techpaper/LANCOM-Techpaper-Switch-design-guide-redundancy-concepts.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Simulation-Based Performance Prediction of HPC Applications - arXiv', 'url': 'https://arxiv.org/pdf/2011.02617.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] ARCHITECTURES FOR EXTREME- SCALE COMPUTING', 'url': 'https://www.eng.auburn.edu/~uguin/teaching/READING/E6200/architectures_4_exascale_computing.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'What is Network Redundancy & Why is It Important? | Auvik', 'url': 'https://www.auvik.com/franklyit/blog/simple-network-redundancy/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'SimHost: A Lightweight End-to-End Simulation Framework for HPC ...', 'url': 'https://dl.acm.org/doi/10.1145/3767339'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Sunway supercomputer architecture towards exascale computing', 'url': 'http://scis.scichina.com/en/2021/141101.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Bandwidth-saving Optimization for MPI Broadcast Collective ...', 'url': 'https://arxiv.org/pdf/1603.06809.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Comparative Analysis of Data Center Network Architectures', 'url': 'http://fan-yao.com/paper/2014_ICC_survey.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'NVLink & NVSwitch: Fastest HPC Data Center Platform | NVIDIA', 'url': 'https://www.nvidia.com/en-us/data-center/nvlink/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Sparse Collective Operations for MPI - Torsten Hoefler', 'url': 'https://htor.inf.ethz.ch/publications/img/hoefler-sparsecolls.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Types of Network Topologies Explained - Cato Networks', 'url': 'https://www.catonetworks.com/glossary/network-topologies/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'GPU Cluster Explained: Architecture, Nodes and Use Cases', 'url': 'https://www.scalecomputing.com/resources/what-is-a-gpu-cluster'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Topology-aware resource management for HPC applications - LaBRI', 'url': 'https://www.labri.fr/perso/ejeannot/publications/icdcn17.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Why is the Internet Traffic Bursty in Short Time Scales?', 'url': 'https://faculty.cc.gatech.edu/~dovrolis/Papers/bursts-metrics05.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] enhancing routing and forwarding in ethernet/ip networks with', 'url': 'https://comp.mga.edu/static/media/doctoralpapers/2025_Tatum_0715161711.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Topology-aware resource management for HPC applications', 'url': 'https://dl.acm.org/doi/10.1145/3007748.3007768'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Noise in the Clouds: Influence of Network Performance Variability on ...', 'url': 'https://htor.inf.ethz.ch/publications/img/noise_in_the_cloud.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Machine Learning for Interconnect Network Traffic Forecasting', 'url': 'https://dl.acm.org/doi/10.1145/3573900.3591123'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Understanding the Total Cost of Ownership in HPC and AI Systems', 'url': 'https://www.ansys.com/blog/understanding-total-cost-ownership-hpc-ai-systems'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Infinia Multi-Tenancy Solution Brief - DDN', 'url': 'https://www.ddn.com/resources/solution-briefs/infinia-multi-tenancy-solution-brief/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'POLATIS Optical Switching Technology Enables High-Performance ...', 'url': 'https://www.signalintegrityjournal.com/articles/4148-polatis-optical-switching-technology-enables-high-performance-connectivity-for-hpc-and-ai-environments'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'IT Modernization: CapEx, OpEx, Hybrid Cloud & Data centers', 'url': 'https://www.digitalrealty.com/resources/articles/it-modernization-opex-capex'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Multi-Tenant OpenStack Architecture Basics - OpenMetal', 'url': 'https://openmetal.io/resources/blog/multi-tenant-openstack-architecture-basics/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Genopsys - Revolutionary Optical Switching Network System for AI ...', 'url': 'https://genopsys-tech.com'}}

## Sources
https://www.exxactcorp.com/blog/hpc/networking-considerations-for-multi-node-computing-deployments
https://introl.com/blog/gpu-cluster-network-topology-fat-tree-dragonfly-rail-optimized-2025
https://circuitcellar.com/research-design-hub/basics-of-design/efficient-topology-mapping-in-hpc/
https://learn.microsoft.com/en-us/powershell/high-performance-computing/understanding-hpc-cluster-network-topologies?view=hpc19-ps
https://www.youtube.com/watch?v=cLSn7Q0QXG4
https://hpc.pnl.gov/people/vishnu/public/vishnu_cluster09.pdf
https://dug.com/hpc-networking-a-ballad-in-four-parts-part-2-bandwidth/
https://tingwang1122.github.io/files/CLOT_Conf.pdf
https://massedcompute.com/faq-answers/?question=How+does+oversubscription+affect+the+performance+of+HPC+applications%3F
https://w3.cs.jmu.edu/lam2mo/cs470_2023_01/files/13_networks.pdf
https://dl.acm.org/doi/10.1145/3725843.3756057
https://www.cerio.io/wp-content/uploads/2023/09/Consequences-of-Congestion-White-Paper-Cerio.pdf
https://www.queensu.ca/academia/afsahi/pprl/papers/AsHES-2025.pdf
https://tma.ifip.org/wordpress/wp-content/uploads/2017/06/tma2017_paper18.pdf
https://www.amax.com/content/files/2023/12/NVIDIA_InfiniBand_Adaptive_Routing_Technology_Insights_Whitepaper.pdf
https://arxiv.org/html/2510.20171v3
https://network.nvidia.com/files/related-docs/whitepapers/deploying_qos_wp_10_19_2005.pdf
https://arxiv.org/html/2506.21406v1
https://www.exxactcorp.com/blog/hpc/networking-considerations-for-multi-node-computing-deployments
https://scholarworks.boisestate.edu/cs_facpubs/161/
https://lightwave.ee.columbia.edu/sites/default/files/content/publications/2022/Enabling_Quasi-Static_Reconfigurable_Networks_With_Robust_Topology_Engineering.pdf
https://learn-more.supermicro.com/data-center-stories/how-to-build-a-high-performance-computing-cluster
https://dl.acm.org/doi/abs/10.5555/3287988.3288001
http://article.sapub.org/10.5923.j.computer.20130302.05.html
https://drivenets.com/blog/rail-vs-tor-architectures-which-is-best-for-ai-clusters/
https://riunet.upv.es/bitstreams/2c9ca452-d826-43e0-895d-e43df0005209/download
https://arxiv.org/html/2510.16946v1
https://developer.nvidia.com/blog/deploying-nvidia-h200-nvl-at-scale-with-new-enterprise-reference-architecture/
https://dl.acm.org/doi/pdf/10.1145/3316480.3325516
https://www.datadoghq.com/blog/hpc-monitoring/
https://www.digitalocean.com/community/conceptual-articles/rdma-high-performance-networking
https://arxiv.org/pdf/2007.03776.pdf
https://hpdc.sci.utah.edu/2017/posters/poster_files/poster13.pdf
https://www.open-mpi.org/papers/euro-pvmmpi-2006-hpc-protocols/euro-pvmmpi-2006-hpc-protocols.pdf
https://htor.inf.ethz.ch/publications/img/besta-TPDS21-routing.pdf
https://dl.acm.org/doi/10.1145/3147213.3147217
https://www.lancom-systems.fr/fileadmin/download/techpaper/LANCOM-Techpaper-Switch-design-guide-redundancy-concepts.pdf
https://arxiv.org/pdf/2011.02617.pdf
https://www.eng.auburn.edu/~uguin/teaching/READING/E6200/architectures_4_exascale_computing.pdf
https://www.auvik.com/franklyit/blog/simple-network-redundancy/
https://dl.acm.org/doi/10.1145/3767339
http://scis.scichina.com/en/2021/141101.pdf
https://arxiv.org/pdf/1603.06809.pdf
http://fan-yao.com/paper/2014_ICC_survey.pdf
https://www.nvidia.com/en-us/data-center/nvlink/
https://htor.inf.ethz.ch/publications/img/hoefler-sparsecolls.pdf
https://www.catonetworks.com/glossary/network-topologies/
https://www.scalecomputing.com/resources/what-is-a-gpu-cluster
https://www.labri.fr/perso/ejeannot/publications/icdcn17.pdf
https://faculty.cc.gatech.edu/~dovrolis/Papers/bursts-metrics05.pdf
https://comp.mga.edu/static/media/doctoralpapers/2025_Tatum_0715161711.pdf
https://dl.acm.org/doi/10.1145/3007748.3007768
https://htor.inf.ethz.ch/publications/img/noise_in_the_cloud.pdf
https://dl.acm.org/doi/10.1145/3573900.3591123
https://www.ansys.com/blog/understanding-total-cost-ownership-hpc-ai-systems
https://www.ddn.com/resources/solution-briefs/infinia-multi-tenancy-solution-brief/
https://www.signalintegrityjournal.com/articles/4148-polatis-optical-switching-technology-enables-high-performance-connectivity-for-hpc-and-ai-environments
https://www.digitalrealty.com/resources/articles/it-modernization-opex-capex
https://openmetal.io/resources/blog/multi-tenant-openstack-architecture-basics/
https://genopsys-tech.com