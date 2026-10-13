# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 3fb219e4 | **Time:** 363.48s | **Cost:** $0.03405
--------------------------------------------------------------------------------

# Theoretical Limits of Blockchain Byzantine Fault Tolerance Mechanisms: Balancing Throughput, Security, Latency, and Message Complexity

## Abstract

Byzantine Fault Tolerance (BFT) consensus mechanisms represent a fundamental building block for distributed ledger technologies, enabling agreement among potentially malicious nodes in distributed systems. This research report examines the theoretical limits governing BFT mechanisms when attempting to optimize the critical trade-offs between system throughput, security guarantees, network latency, and message complexity. Through comprehensive analysis of contemporary literature and empirical performance data, we identify that the fundamental constraints arise from the inherent tension between quadratic message complexity in traditional broadcast-based BFT protocols and the linear complexity achievable through architectural innovations. Our analysis reveals that while modern protocols such as HotStuff, SBFT, and tree-topology based approaches have made significant strides in reducing communication overhead, they encounter theoretical boundaries that prevent simultaneous optimization across all performance dimensions. The 3f+1 fault tolerance threshold remains a fundamental security constraint, while responsiveness—defined as latency dependent only on actual network delay rather than predefined bounds—represents an additional dimension of trade-off that cannot be achieved without sacrificing synchronous safety guarantees.

## 1. Introduction

The proliferation of blockchain technology has catalyzed intensive research into consensus mechanisms capable of maintaining agreement among distributed nodes while operating under adversarial conditions. Byzantine Fault Tolerance mechanisms, originally conceptualized in the seminal work on the Byzantine Generals Problem, have evolved substantially to address the unique challenges posed by blockchain environments. These challenges include the need for high transaction throughput, low confirmation latency, robust security against arbitrary node failures, and scalability to accommodate growing network sizes.

The fundamental premise underlying BFT consensus is that a distributed system can achieve agreement on a consistent state even when a subset of nodes exhibit arbitrary or malicious behavior. However, achieving this property comes at a cost—typically measured in terms of communication overhead, computational requirements, and time to finality. The so-called blockchain trilemma posits that systems cannot simultaneously optimize for security, scalability, and decentralization without making explicit trade-offs along these dimensions [1][2].

This research report synthesizes current understanding of the theoretical limits governing BFT mechanisms in blockchain contexts. We focus specifically on the interplay between four critical performance parameters: system throughput (transactions processed per second), security guarantees (resilience against Byzantine faults), network latency (time from transaction submission to final confirmation), and message complexity (total communication overhead required for consensus). Understanding these trade-offs is essential for protocol designers seeking to optimize blockchain systems for specific deployment scenarios, whether permissioned enterprise networks or permissionless public ledgers.

## 2. Foundational Concepts in Byzantine Fault Tolerance

### 2.1 The Byzantine Fault Model and Fault Tolerance Thresholds

Byzantine faults represent the most general class of failures in distributed systems, wherein nodes may exhibit arbitrary behavior—including sending contradictory messages, colluding with other faulty nodes, or actively attempting to disrupt consensus. The fundamental theorem governing BFT systems establishes that to tolerate up to f Byzantine nodes, a system must maintain at least 3f+1 total nodes [3]. This requirement stems from the need for overlapping quorums that prevent conflicting decisions: with 2f+1 honest nodes forming a quorum, the system guarantees that any two quorums share at least one honest node, thereby preventing contradictory finality decisions.

The 3f+1 threshold has profound implications for system scalability. As the number of potential Byzantine faults increases, the total node count must grow proportionally, which in turn affects communication complexity and throughput. This relationship establishes the first fundamental trade-off in BFT system design: security (measured by the maximum number of tolerable Byzantine nodes) directly constrains the minimum network size and influences communication overhead.

### 2.2 Message Complexity and Communication Overhead

Message complexity represents one of the most significant bottlenecks in BFT consensus protocols. Traditional broadcast-based BFT protocols, exemplified by Practical Byzantine Fault Tolerance (PBFT), exhibit O(n²) message complexity, where n represents the total number of replicas [4]. In PBFT, each message must be broadcast to all other replicas to ensure that honest nodes can detect and report contradictory messages from faulty leaders. This quadratic growth in communication overhead severely limits scalability, as doubling the number of nodes quadruples the message volume.

Communication complexity, measured in terms of total message size rather than count, presents additional challenges. Some protocols require linear-sized certificates containing signatures from multiple nodes, resulting in O(n³) bit complexity that can be reduced to O(n²) through threshold signature schemes [5]. The distinction between message count and message size is crucial: protocols may achieve linear message count while maintaining quadratic or higher communication complexity depending on their signature and certificate structures.

### 2.3 Latency and Responsiveness

Latency in BFT systems encompasses multiple components: network transmission delay, cryptographic operation time, and protocol-specific waiting periods. The concept of responsiveness introduces a critical distinction between protocols based on their latency characteristics [6]. A responsive protocol achieves commit latency that depends only on actual network delay—the time required for honest nodes to process and exchange messages—rather than any predefined upper bound on message transmission delay.

Non-responsive protocols, by contrast, require waiting for predetermined timeout periods that must account for worst-case network conditions. This approach provides safety guarantees under synchronous assumptions but results in latency that may significantly exceed actual requirements under normal network conditions. The trade-off between responsiveness and synchronous safety represents a fundamental theoretical limit: achieving responsiveness may require sacrificing guarantees about behavior under network partitions or extreme latency variations [5].

## 3. Theoretical Limits of BFT Performance Trade-offs

### 3.1 The Fundamental Throughput-Security-Latency Triangle

Contemporary research has established that no BFT protocol can simultaneously optimize throughput, security, and latency without making explicit trade-offs. This principle manifests through several interconnected theoretical constraints that bound achievable performance across different protocol configurations.

The first constraint arises from the relationship between message complexity and throughput. For broadcast-based BFT protocols, the O(n²) message complexity creates a fundamental throughput ceiling that scales inversely with network size. Empirical measurements demonstrate that PBFT experiences approximately 65% throughput reduction when increasing the number of replicas, while protocols with linear message complexity exhibit more moderate degradation—39% for PoE, 55% for SBFT, and 45% for HotStuff [1]. This differential underscores how message complexity directly translates to throughput limitations as networks scale.

The second constraint involves the relationship between latency and fault tolerance. Protocols that achieve lower latency typically do so by reducing communication rounds or eliminating waiting periods for slow replicas. However, such optimizations may compromise the ability to tolerate slow or temporarily partitioned nodes, effectively reducing the practical fault tolerance threshold under adverse conditions.

### 3.2 Theoretical Boundaries of Message Complexity Reduction

The pursuit of linear message complexity O(n) has driven significant innovation in BFT protocol design, yet this reduction comes with inherent limitations. Tree-topology based approaches, such as those employed in Kauri and FTB protocols, reduce per-replica bandwidth utilization and achieve approximately 31-32% throughput reduction when scaling node counts—substantially better than the 65% reduction observed in quadratic-complexity protocols [1]. However, tree topologies introduce new failure modes: if intermediate nodes in the communication tree become faulty, they may selectively forward or modify messages, requiring additional mechanisms to detect and mitigate such attacks.

The theoretical analysis of Multi-Type BFT (MT-BFT) frameworks reveals fundamental trade-offs between asynchronous safety thresholds and synchronous liveness thresholds [5]. Specifically, MT-BFT reliable broadcast can be achieved if and only if 2γ_s + β_a < n, where γ_s represents the synchronous liveness threshold and β_a represents the asynchronous safety threshold. This inequality establishes that improving one aspect of fault tolerance necessarily constrains another, reflecting the inherent impossibility of simultaneously maximizing all fault tolerance dimensions.

### 3.3 The Responsiveness-Safety Trade-off

Responsiveness represents a particularly illuminating case study in theoretical limits. Fully responsive protocols achieve latency dependent only on actual network conditions, eliminating the need for conservative timeout values. However, theoretical analysis demonstrates that achieving responsiveness while maintaining synchronous safety guarantees is impossible under certain conditions [5].

Non-responsive protocols sacrifice latency to ensure safety under synchronous network assumptions. Tendermint and Casper implement leader rotation with predefined waiting periods to ensure the new leader receives decisions from all non-faulty replicas before proceeding [6]. SBFT and Zyzzyva optimistically assume all replicas are non-faulty and wait for predefined upper bounds to receive messages from all replicas. Both approaches sacrifice responsiveness for different aspects of safety or simplicity.

The framework proposed in contemporary research adds two extra rounds plus a Δ waiting time for latency, and introduces 3n² additional messages for communication complexity [5]. While threshold signatures can reduce message sizes, the fundamental trade-off between responsiveness and synchronous safety remains: protocols cannot achieve both properties simultaneously without additional assumptions about network behavior or fault patterns.

## 4. Contemporary BFT Protocol Architectures and Their Limits

### 4.1 Linear Complexity Protocols and Their Performance Boundaries

Modern BFT protocols have achieved linear message complexity through various architectural innovations. HotStuff, which serves as the consensus mechanism for the Diem (formerly Libra) blockchain, employs pipelining to overlap consensus rounds and leader-based commits to reduce communication overhead [7]. The protocol achieves latency of 2Δ+2δ under synchronous conditions, with message complexity approaching O(n) for the common case.

SBFT implements linear message complexity through collector-based architectures, reducing the communication burden on individual replicas while maintaining security guarantees. Similarly, PoE (Proof of Efficiency) protocols leverage optimized communication patterns to achieve throughput reduction of only 39% when scaling node counts—significantly better than PBFT's 65% reduction but still exhibiting degradation as networks grow [1].

The performance data reveals consistent patterns across linear-complexity protocols. HotStuff demonstrates 45% throughput reduction when increasing n, SBFT shows 55% reduction, and PoE exhibits 39% reduction [1]. These variations reflect different implementation choices and optimization priorities, but all remain bounded by the fundamental relationship between network size and communication overhead.

### 4.2 Tree-Topology and Hierarchical Approaches

Tree-topology based protocols represent an alternative approach to managing communication complexity. By organizing replicas into hierarchical structures, these protocols reduce the bandwidth requirements on individual nodes while maintaining overall system throughput. Kauri and FTB protocols implement this approach, achieving only 31-32% throughput reduction when scaling node counts—substantially better than both quadratic and linear broadcast protocols [1].

However, tree topologies introduce their own theoretical limitations. The hierarchical structure creates potential bottlenecks at higher levels of the tree, and faulty nodes at strategic positions can disproportionately impact system performance. Additionally, the complexity of implementing and verifying tree-based communication may introduce security vulnerabilities if not carefully designed.

### 4.3 Directed Acyclic Graph (DAG) Based Approaches

DAG-based consensus protocols, including IOTA's Tangle, Hedera Hashgraph, and Fantom's Lachesis, abandon the linear block structure in favor of asynchronous message propagation [7]. In DAG architectures, events form a partially ordered set rather than a single chain, allowing parallel processing and reduced confirmation times.

The theoretical limits of DAG-based systems differ from traditional BFT approaches. While DAGs can achieve high throughput and low latency by allowing asynchronous progress, they introduce complexity in establishing a canonical view of history. Some DAG systems provide only eventual consistency, while others layer additional consensus mechanisms to achieve deterministic finality—effectively reintroducing serial constraints that limit throughput.

Morpheus Consensus represents an innovative approach that dynamically adapts between leaderless and leader-based modes depending on network conditions [8]. During high-throughput periods, it matches state-of-the-art DAG-based protocols, while during low-throughput periods, it exhibits competitive complexity and lower latency than standard protocols like PBFT and Tendermint. This adaptive approach demonstrates that protocol selection can be optimized for specific operational regimes, though it does not eliminate the fundamental trade-offs.

## 5. Security Considerations and Fault Tolerance Boundaries

### 5.1 The 3f+1 Rule and Its Implications

The fundamental security threshold of 3f+1 replicas for tolerating f Byzantine faults establishes a baseline for system design. This requirement ensures that any two quorums of size 2f+1 share at least f+1 honest nodes, preventing conflicting decisions from being finalized. The threshold applies universally across BFT protocols, though different implementations may achieve it through varying mechanisms.

Dynamic validator sets complicate quorum intersection and safety proofs, requiring mature designs that incorporate epochs, checkpoints, and well-defined handoff logic [3]. As networks evolve and validators join or leave, maintaining the quorum intersection property becomes increasingly challenging, potentially reducing effective fault tolerance during transition periods.

### 5.2 Economic Security and Sybil Resistance

Proof-of-Stake based BFT protocols introduce economic security mechanisms that complement traditional fault tolerance thresholds. Staking requirements create economic incentives for honest behavior, as validators risk losing stake through slashing conditions. However, concentration among a few large stakeholders may introduce censorship or centralization risks that undermine the theoretical fault tolerance guarantees [3].

The relationship between economic security and traditional fault tolerance thresholds remains an active area of research. While staking can increase the effective cost of attacking the network, it does not fundamentally change the 3f+1 requirement for Byzantine agreement. Protocols must balance economic mechanisms with cryptographic guarantees to achieve robust security.

### 5.3 Protocol-Specific Security Trade-offs

Different BFT protocols make explicit security trade-offs in pursuit of performance improvements. PBFT provides deterministic finality and strong consistency but requires O(n²) communication, limiting scalability [9]. Avalanche achieves high throughput and fast probabilistic finality through repeated subsampling but requires deeper analysis of long-term security under sustained adversarial conditions [2].

Order-fairness represents an additional security dimension that some protocols address. Ensuring that the final transaction order reflects arrival order prevents malicious replicas from manipulating transaction sequence for profit. However, achieving order-fairness typically requires additional communication rounds, increasing latency and message complexity [10].

## 6. Scalability Boundaries and Network Size Effects

### 6.1 Throughput Degradation Patterns

Empirical analysis reveals consistent patterns of throughput degradation as networks scale. PBFT and FaB protocols exhibit 65% and 63% throughput reduction respectively when increasing replica count, directly attributable to their quadratic message complexity [1]. In contrast, protocols with linear or near-linear complexity show more moderate degradation: Kauri and FTB at 31-32%, PoE at 39%, SBFT at 55%, and HotStuff at 45%.

These degradation patterns establish practical scalability boundaries for different protocol families. While linear-complexity protocols scale better than quadratic ones, they still experience significant throughput reduction at large network sizes. The theoretical limit appears to be linear degradation or better, achieved through architectural innovations like tree topologies, but eliminating degradation entirely remains impossible due to the fundamental requirement of communicating with sufficient replicas to achieve quorum intersection.

### 6.2 Latency Scaling and Responsiveness Limits

Latency in BFT systems comprises multiple components that scale differently with network size. Network transmission delay increases with physical distance and hop count, while processing delay grows with cryptographic operation requirements. Protocol-specific waiting periods may scale with network size if they depend on timeout values calibrated for worst-case conditions.

Responsive protocols maintain latency independent of predefined bounds, but achieving this property requires accepting limitations on synchronous safety [5][6]. The trade-off manifests clearly in protocols like Chained-HotStuff, which implements pipelining to reduce average latency but may sacrifice responsiveness in exchange for improved throughput under normal conditions [1].

### 6.3 Bandwidth and Computational Constraints

Individual replica bandwidth utilization represents a critical constraint on system scalability. Tree-topology approaches specifically address this constraint by distributing communication load across hierarchical structures, reducing per-node bandwidth requirements [1]. However, total system bandwidth necessarily increases with network size, as more signatures and certificates must be processed and transmitted.

Computational overhead, particularly cryptographic operations for signature verification and certificate construction, adds additional constraints. Threshold signatures and their variants can reduce the number of cryptographic operations required, though real-world performance evaluation of these optimizations remains an active research area [4].

## 7. Comparative Analysis of Protocol Families

### 7.1 Traditional Broadcast-Based BFT

PBFT and its direct descendants establish the baseline for comparison. These protocols achieve strong consistency and deterministic finality with relatively low latency in small-scale deployments (typically 4-100 nodes) [9]. However, the O(n²) message complexity creates fundamental scalability limits that become prohibitive at larger network sizes.

The performance characteristics of PBFT make it suitable for enterprise applications, financial systems, and interoperability platforms where validator sets remain relatively small and stable. The deterministic finality provides strong guarantees for applications like exchanges, DEX settlement, and supply chain tracking where reversals introduce significant risk.

### 7.2 Linear Complexity Modern Protocols

HotStuff, SBFT, and related protocols achieve improved scalability through linear message complexity and optimized communication patterns. HotStuff's pipelining approach enables overlapping consensus rounds, reducing effective latency while maintaining security guarantees [7]. These protocols represent the current state-of-the-art for permissioned blockchain deployments requiring larger validator sets.

The performance data demonstrates that linear complexity provides meaningful scalability improvements, reducing throughput degradation from 65% (PBFT) to 45-55% (HotStuff, SBFT) when scaling node counts [1]. However, these improvements come with increased protocol complexity and potential vulnerabilities during view changes or leader failures.

### 7.3 DAG-Based and Hybrid Approaches

DAG-based protocols and hybrid architectures offer alternative approaches to the scalability problem. By allowing asynchronous message propagation and parallel processing, these systems can achieve higher throughput than traditional BFT protocols. However, they often sacrifice deterministic finality or introduce complexity in establishing canonical history [7].

Avalanche achieves high throughput and low latency through random sampling and leaderless voting, but its probabilistic finality differs fundamentally from the deterministic finality of traditional BFT protocols [2]. For applications requiring absolute certainty about transaction finality, this trade-off may be unacceptable despite the performance benefits.

## 8. Theoretical Framework for Understanding Limits

### 8.1 The Impossibility of Optimization Across All Dimensions

The theoretical limits of BFT consensus can be understood through the lens of impossibility results that establish fundamental boundaries on achievable performance. No protocol can simultaneously achieve optimal throughput, minimal latency, maximum security, and linear scalability—any improvement in one dimension necessarily involves trade-offs in others.

This principle manifests through specific relationships. Reducing message complexity from O(n²) to O(n) improves throughput scalability but may increase latency if additional coordination is required. Eliminating waiting periods improves responsiveness but may compromise safety under network partitions. Increasing fault tolerance requires larger quorum sizes, increasing both message complexity and latency.

### 8.2 The Role of Network Assumptions

The partial synchrony model, which underlies most practical BFT protocols, establishes assumptions about network behavior that enable specific optimizations. Under synchrony assumptions, protocols can use timeout mechanisms to ensure progress even when some nodes are slow or partitioned. Under asynchrony, protocols must handle arbitrary message delays but cannot rely on timing assumptions for safety.

The relationship between network assumptions and performance limits is bidirectional. Protocols designed for synchronous networks can achieve lower latency but may not make progress during partitions. Asynchronous protocols guarantee liveness under more conditions but typically require additional communication rounds, increasing latency under normal operation.

### 8.3 Threshold Relationships and Fault Tolerance Bounds

The MT-BFT framework provides a formal characterization of fault tolerance boundaries through threshold relationships [5]. The condition 2γ_s + β_a < n establishes that improving synchronous liveness (increasing γ_s) necessarily constrains asynchronous safety (reducing β_a), and vice versa. This relationship captures the fundamental trade-off between different aspects of fault tolerance.

Similar threshold relationships govern other performance dimensions. Throughput scales inversely with message complexity, which scales with quorum size. Latency depends on communication rounds, which scale with the depth of quorum intersection requirements. These relationships establish mathematical boundaries that no protocol can exceed without violating fundamental assumptions.

## 9. Practical Implications and Design Guidelines

### 9.1 Protocol Selection Considerations

The theoretical limits identified in this analysis provide guidance for protocol selection based on specific deployment requirements. For applications requiring maximum security and deterministic finality with small validator sets (tens of nodes), traditional PBFT or its optimized variants provide appropriate trade-offs. For larger validator sets requiring better scalability, linear-complexity protocols like HotStuff offer improved performance while maintaining strong consistency guarantees.

Applications prioritizing throughput over latency may benefit from DAG-based approaches or pipelined BFT variants that overlap consensus rounds. However, these choices involve accepting either probabilistic finality or increased protocol complexity. The optimal choice depends on specific application requirements and threat models.

### 9.2 Deployment Architecture Decisions

Network architecture decisions significantly impact achievable performance within the constraints of chosen protocols. Tree-topology based approaches can reduce per-node bandwidth requirements, enabling larger networks within given infrastructure constraints. Hierarchical structures may introduce additional failure modes but provide meaningful scalability improvements.

Geographic distribution of replicas affects both latency and fault tolerance. Replicas distributed across multiple regions experience higher network latency but provide resilience against regional network partitions. The trade-off between latency and fault tolerance must be evaluated against specific deployment requirements.

### 9.3 Monitoring and Operational Considerations

Operational maturity is as important as protocol design in sustaining stable performance at scale [3]. Monitoring throughput (TPS), latency, and validator health enables detection of performance degradation and potential attacks. Block propagation monitoring helps identify bottlenecks in the consensus process.

Dynamic adaptation mechanisms, such as those implemented in Morpheus Consensus, demonstrate that operational conditions can inform protocol behavior [8]. However, such adaptations do not eliminate fundamental trade-offs—they merely shift between different points on the trade-off surface depending on current conditions.

## 10. Conclusion and Future Research Directions

The theoretical limits of blockchain Byzantine Fault Tolerance mechanisms arise from fundamental relationships between throughput, security, latency, and message complexity that cannot be simultaneously optimized. The 3f+1 fault tolerance threshold establishes minimum network size requirements for given security guarantees, while message complexity constraints—ranging from O(n²) in traditional broadcast-based protocols to O(n) in modern linear-complexity designs—directly impact achievable throughput as networks scale.

Responsiveness, defined as latency dependent only on actual network delay rather than predefined bounds, represents an additional dimension of trade-off that cannot be achieved without sacrificing synchronous safety guarantees. The theoretical analysis demonstrates that protocols must explicitly choose between responsiveness and synchronous safety, with no known approach achieving both properties simultaneously under general conditions.

Contemporary protocols have made significant progress in optimizing specific trade-offs. Tree-topology approaches reduce per-node bandwidth utilization, achieving only 31-32% throughput degradation compared to 65% for quadratic-complexity protocols. Pipelined BFT variants like Chained-HotStuff reduce average latency through overlapping consensus rounds. DAG-based architectures enable high throughput through asynchronous message propagation, though often at the cost of deterministic finality.

Future research directions include continued exploration of adaptive protocols that optimize for specific operational conditions, hybrid approaches combining BFT guarantees with probabilistic finality mechanisms, and novel cryptographic techniques that reduce communication overhead while maintaining security guarantees. The fundamental trade-offs identified in this analysis will continue to guide protocol design, as they represent inherent limitations of distributed consensus under Byzantine fault conditions rather than engineering challenges awaiting solution.

The blockchain trilemma remains a fundamental constraint that shapes BFT protocol design. While specific protocols may push boundaries in realistic environments, none eliminates the underlying trade-offs—they merely relocate bottlenecks to different system components or shift between different points on the trade-off surface. Understanding these theoretical limits enables informed protocol selection and deployment decisions that optimize for specific application requirements within the boundaries of what distributed consensus can achieve.

---

## References

[1] USENIX NSDI 2024, "FLB: Fast Byzantine Lattice Consensus," demonstrating performance improvements through reduced message complexity and communication phases, achieving 2.25x throughput and 0.55x latency compared to PBFT.

[2] Paper Publications, "Study and Comparative Analysis of Blockchain Consensus Algorithms," analyzing sustainability, scalability, security, and decentralization characteristics across PoW, PoS, PBFT, Avalanche, and Polkadot mechanisms.

[3] Cube Exchange, "BFT Consensus" documentation, explaining the 3f+1 rule, deterministic finality, and trade-offs between BFT and Nakamoto consensus approaches.

[4] BFT Survey (BCR22), "Byzantine Fault Tolerance in Blockchains," analyzing message complexity, communication complexity, latency, throughput, and server scalability metrics.

[5] ePrint IACR 2021/671, "MT-BFT Framework," establishing theoretical fault tolerance bounds and the trade-off between asynchronous safety and synchronous liveness thresholds.

[6] USENIX NSDI 2024, Section E4 on responsiveness, synchronization, and timers, analyzing how BFT protocols sacrifice responsiveness through leader rotation and predefined upper bounds.

[7] Computer.org, "Distributed Consensus Algorithms in Blockchain," examining the blockchain trilemma, DAG-based approaches, and modern BFT variants including HotStuff.

[8] Lewis-Pye.com, "Morpheus Consensus," proposing adaptive protocols that morph between leaderless and leader-based modes depending on network conditions.

[9] Cube Exchange, "PBFT: Practical Byzantine Fault Tolerance," analyzing PBFT's deterministic finality, O(n²) message complexity, and suitability for enterprise applications.

[10] ePrint IACR 2025/845, surveying dynamic BFT protocols and order-fairness mechanisms for transaction ordering.

## Annotations


## Sources
[1] https://bchainzhang.github.io/files/bft-csur22.pdf
[2] https://dl.acm.org/doi/full/10.1145/3689343
[3] https://eprint.iacr.org/2021/671.pdf
[4] https://eprint.iacr.org/2025/845.pdf
[5] https://lewis-pye.com/
[6] https://pdfs.semanticscholar.org/b319/1be6babfc4bb5f112fa02d848f8da80b7257.pdf
[7] https://www.atlantis-press.com/article/126004114.pdf
[8] https://www.computer.org/publications/tech-news/trends/distributed-consensus-algorithms-in-blockchain
[9] https://www.cube.exchange/what-is/bft-consensus
[10] https://www.cube.exchange/what-is/pbft-practical-byzantine-fault-tolerance
[11] https://www.mdpi.com/2227-7390/12/23/3860
[12] https://www.nature.com/articles/s41598-024-82579-1
[13] https://www.paperpublications.org/upload/book/Study%20and%20Comparative%20Analysis%20of%20Blockchain-25112025-2.pdf
[14] https://www.researchgate.net/publication/383288959_Exploring_Scalability_of_BFT_Blockchain_Protocols_through_Network_Simulations
[15] https://www.usenix.org/system/files/nsdi24-amiri.pdf