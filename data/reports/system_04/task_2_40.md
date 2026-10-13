# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** e4661a98 | **Time:** 516.37s | **Cost:** $2.04297
--------------------------------------------------------------------------------

# Consensus Algorithms for Financial Blockchain Alliances: Balancing Security and Throughput Without Zero-Knowledge Proof Overhead

**Key Points**
*   **The Consensus Dilemma:** Financial blockchain alliances (consortiums) face a trilemma of achieving high throughput, low latency (immediate finality), and robust security without the computational bottlenecks associated with Zero-Knowledge Proofs (ZKPs) or the energy inefficiency of Proof of Work (PoW).
*   **Primary Solution (HotStuff/DiemBFT):** The **HotStuff** protocol, and its derivative **DiemBFT** (used by Aptos and Sui), represents the leading solution. It achieves linear communication complexity ($O(n)$) rather than the quadratic complexity ($O(n^2)$) of traditional PBFT. This allows for scalability to hundreds of validators with sub-second latency and immediate finality, utilizing a pipelined voting process and "optimistic responsiveness" to drive consensus at the speed of the network.
*   **Alternative Solution (SBFT):** **Scalable Byzantine Fault Tolerance (SBFT)**, employed by VMware Blockchain, utilizes a centralized "collector" mechanism and BLS threshold signatures to aggregate votes. This reduces communication overhead significantly, enabling deployments of 200+ replicas with high throughput, specifically targeting enterprise financial use cases like the Australian Securities Exchange (ASX).
*   **Federated Models:** **Federated Byzantine Agreement (FBA)**, used by Stellar, offers a flexible trust model via "quorum slices," allowing organic network growth without a central authority, though it introduces complexity in ensuring quorum intersection.
*   **Conclusion:** For financial alliances requiring strict regulatory compliance and high performance without ZKP overhead, **HotStuff/DiemBFT** and **SBFT** are the consensus algorithms of choice. They replace the heavy cryptographic computation of ZKPs with optimized communication topologies and efficient signature aggregation.

## 1. Introduction

The integration of Distributed Ledger Technology (DLT) into the financial sector necessitates consensus mechanisms that can withstand the rigorous demands of global finance: high transaction throughput, sub-second settlement finality, and robust security against malicious actors. While Zero-Knowledge Proofs (ZKPs) have emerged as a potent tool for privacy and scalability in public blockchains (specifically via ZK-Rollups), they introduce significant computational overhead regarding proof generation, which can limit the raw speed and scalability of the base network layer [cite: 1, 2].

For financial blockchain alliances—typically structured as permissioned consortiums—the requirement is often to achieve consensus among a known, vetted set of validators (e.g., banks, regulators, payment processors) without the latency of Proof of Work (PoW) or the computational burden of ZKPs. The search for such an algorithm has led to the evolution of Byzantine Fault Tolerant (BFT) protocols. Traditional Practical Byzantine Fault Tolerance (PBFT) suffers from quadratic message complexity ($O(n^2)$), making it unscalable beyond a small number of nodes [cite: 3, 4].

This report analyzes the landscape of consensus algorithms optimized for financial consortiums that bypass ZKP overhead. It identifies **HotStuff (and its variants DiemBFT/AptosBFT)** and **Scalable BFT (SBFT)** as the premier solutions. These protocols utilize advanced cryptographic primitives (like threshold signatures) and optimized communication topologies (star networks, pipelining) to balance security and throughput effectively.

## 2. The Constraints of Financial Consortiums

### 2.1 The Scalability-Security-Latency Trilemma
Financial institutions operate in an environment where "probabilistic finality" (common in Bitcoin and Ethereum) is unacceptable. A payment or settlement must be final and irreversible within seconds. Furthermore, the system must tolerate "Byzantine" faults—nodes that may be malicious, compromised, or simply offline.
*   **Throughput:** The system must handle thousands of transactions per second (TPS) to rival centralized payment rails [cite: 5].
*   **Security:** The network must tolerate up to $1/3$ of the nodes being faulty ($f < n/3$) without compromising the ledger's integrity [cite: 6].
*   **Latency:** Financial markets require low latency for high-frequency trading and instant settlement [cite: 7].

### 2.2 The Computational Overhead of Zero-Knowledge Proofs
While ZKPs (zk-SNARKs, zk-STARKs) offer privacy and compression, they are computationally intensive.
*   **Proof Generation:** Generating a proof for a batch of transactions requires complex arithmetic circuit computations, which can be orders of magnitude slower than simple signature verification [cite: 1, 2].
*   **Scalability Limits:** Although ZKPs scale *verification* (making it cheap for verifiers), the *prover* bottleneck can limit the rate at which the network can accept new state updates, particularly in high-frequency financial environments [cite: 1, 2].
*   **Financial Relevance:** Financial alliances often rely on legal contracts and permissioned identities for privacy (using private channels or encrypted payloads) rather than cryptographic obfuscation via ZKPs, rendering the ZKP overhead unnecessary for the consensus layer itself [cite: 8].

## 3. Primary Candidate: HotStuff and DiemBFT

The most significant advancement in BFT consensus for financial applications in recent years is the **HotStuff** protocol, and its production-hardened variant, **DiemBFT** (formerly LibraBFT). This algorithm was explicitly designed to support the global scale and throughput requirements of a financial network initiated by Meta (Facebook) and has since been adopted by high-performance blockchains like Aptos and Sui [cite: 6, 9, 10].

### 3.1 Algorithmic Mechanics
HotStuff addresses the primary bottleneck of PBFT: the view-change protocol. In PBFT, replacing a failed leader requires an $O(n^3)$ or $O(n^2)$ message exchange, which cripples the network as it scales. HotStuff introduces a three-phase commit rule that allows for **Linear View Change**.

*   **Linear Communication ($O(n)$):** In HotStuff, validators communicate only with the leader (a star topology), rather than broadcasting to everyone (mesh topology). The leader aggregates votes and broadcasts a Quorum Certificate (QC). This keeps communication complexity linear relative to the number of nodes [cite: 10, 11].
*   **Pipelining:** Unlike PBFT, which processes one block at a time through multiple phases (Pre-Prepare, Prepare, Commit), HotStuff pipelines these phases. The "Prepare" phase of block $B_n$ serves as the "Pre-Commit" phase for block $B_{n-1}$ and the "Commit" phase for block $B_{n-2}$. This allows the network to produce blocks continuously without pausing for finality on previous blocks [cite: 10, 12].
*   **Optimistic Responsiveness:** The protocol proceeds as fast as the network allows. It does not wait for a predefined "timeout" if a quorum of responses is received quickly. This is crucial for financial networks where network conditions vary, ensuring the system always runs at maximum possible speed [cite: 10, 13].

### 3.2 DiemBFT: Optimization for Finance
DiemBFT (v4) is a refinement of HotStuff specifically for the Diem payment network. It introduces a **two-phase** commit rule (reduced from three) in the steady state by leveraging a quadratic view change only when a leader fails, optimizing for the common case where the leader is honest [cite: 12].
*   **Safety and Liveness:** DiemBFT guarantees safety (no forks) even during periods of asynchrony (network partitions) and guarantees liveness (transaction processing) once the network becomes partially synchronous [cite: 6, 12].
*   **Chain Structure:** It utilizes a "chaining" approach where a QC for round $k$ is carried in the proposal for round $k+1$. This piggybacking reduces message size and overhead [cite: 12].
*   **Performance:** In controlled environments, DiemBFT has demonstrated the ability to process thousands of transactions per second with sub-second latency, meeting the requirements of wholesale and retail financial settlement [cite: 6].

### 3.3 Adoption in Financial Infrastructure
The architecture of DiemBFT has been inherited by **Aptos** and **Sui**.
*   **AptosBFT:** Adds an active "pacemaker" to ensure leaders are rotated efficiently and failed validators are ignored, maintaining high throughput even under attack [cite: 14, 15].
*   **Sui (Narwhal & Tusk/Bullshark):** Sui utilizes a DAG-based mempool (Narwhal) combined with a HotStuff-variant consensus (Bullshark/Tusk). This separates data dissemination from transaction ordering, allowing the network to scale throughput linearly with available bandwidth, a critical feature for high-volume financial exchanges [cite: 16, 17].

## 4. Alternative Candidate: Scalable BFT (SBFT)

**Scalable Byzantine Fault Tolerance (SBFT)** is another leading consensus algorithm designed specifically to overcome the scalability limits of PBFT for permissioned, enterprise-grade blockchains. It is the core consensus engine for **VMware Blockchain**, which is used by the Australian Securities Exchange (ASX) for its DLT-based replacement of the CHESS settlement system [cite: 18, 19].

### 4.1 Algorithmic Mechanics
SBFT focuses on decentralization and scalability, capable of supporting over 200 active replicas—a significantly higher number than standard PBFT implementations which degrade after 20 nodes [cite: 20, 21].

*   **Collectors and Threshold Signatures:** SBFT employs a "collector" model. Instead of every node sending signatures to every other node, they send partial signatures to a designated collector. The collector aggregates these into a single compact signature using **BLS (Boneh-Lynn-Shacham)** threshold cryptography. This aggregated signature is then broadcast back to the replicas. This reduces the communication complexity from $O(n^2)$ to $O(n)$ [cite: 20, 21].
*   **Dual-Path Execution:**
    *   **Fast Path:** If all replicas are honest and the network is synchronous, SBFT uses a fast path that commits transactions with minimal steps.
    *   **Slow Path:** If faults are detected or the network is slow, it falls back to a robust path. Crucially, SBFT implements a seamless transition between these modes without a heavy view-change penalty [cite: 20, 21].
*   **Client Footprint Reduction:** In traditional BFT, clients must listen to $f+1$ replicas to verify execution. SBFT aggregates execution proofs so the client receives a single message, making it ideal for "thin client" financial applications (e.g., mobile banking apps) [cite: 20, 21].

### 4.2 Performance vs. PBFT
Research indicates that SBFT provides approximately **2x better throughput** and **1.5x better latency** than highly optimized PBFT implementations in world-scale deployments (WAN) [cite: 20, 21]. It effectively removes the computational and communication bottlenecks that previously prevented BFT from being used in large financial consortiums.

### 4.3 Financial Use Case: VMware and ASX
The selection of SBFT by VMware for the ASX project highlights its suitability for critical financial infrastructure. The requirement was a system that could handle the entire equity market of a major nation, requiring absolute finality, high availability, and the ability to govern a multi-party network without a single point of failure [cite: 18, 19].

## 5. Federated Byzantine Agreement (FBA)

While HotStuff and SBFT assume a global quorum (where $2/3$ of the total network must agree), **Federated Byzantine Agreement (FBA)**, pioneered by **Stellar**, offers a different approach suitable for looser financial alliances where a central membership list might not be desirable.

### 5.1 Quorum Slices
In FBA, each node selects a specific subset of other nodes it trusts (a "quorum slice"). Consensus emerges from the overlapping intersections of these slices across the network. This allows for **open membership** (anyone can join) while maintaining a web of trust that prevents Sybil attacks without PoW [cite: 22, 23, 24].

### 5.2 Financial Applicability
*   **Flexibility:** FBA is ideal for cross-border payment networks (like Stellar or Ripple/XRPL) where different banks may trust their local partners and a few major hubs, but not necessarily every small bank in a different continent [cite: 25, 26].
*   **Performance:** FBA achieves high throughput and low energy consumption. However, ensuring "quorum intersection" (that the network doesn't split into two) requires careful configuration of trust slices [cite: 23, 27].
*   **Trade-offs:** While scalable, FBA can be more complex to analyze for safety than the deterministic quorums of HotStuff or SBFT. If the "top tier" of nodes (major banks) misconfigure their slices, the network can stall (lose liveness) to preserve safety [cite: 27].

## 6. Comparative Analysis of Consensus Algorithms

The following table summarizes the key characteristics of the discussed algorithms relative to the user's requirements (Security, Throughput, No ZKP Overhead).

| Feature | **PBFT** (Traditional) | **HotStuff / DiemBFT** | **SBFT** (VMware) | **FBA** (Stellar) |
| :--- | :--- | :--- | :--- | :--- |
| **Communication Complexity** | $O(n^2)$ (Quadratic) | $O(n)$ (Linear) | $O(n)$ (Linear) | Variable (Dependent on slices) |
| **Scalability (Nodes)** | Low (< 20) | High (100+) | High (200+) | High (Open Membership) |
| **Throughput** | Low/Medium | Very High (Pipelined) | High (Fast Path) | High |
| **Latency** | Medium | Low (Optimistic Responsiveness) | Low | Low |
| **Finality** | Immediate | Immediate | Immediate | Immediate |
| **Cryptography** | Standard Signatures | Threshold Signatures (Optional) | BLS Threshold Signatures | Standard Signatures |
| **ZKP Requirement** | **None** | **None** | **None** | **None** |
| **Primary Use Case** | Small Pilots | Global Payments (Diem, Aptos) | Enterprise Equity Markets (ASX) | Cross-border Remittance |

*Table Data Sources: [cite: 3, 4, 6, 10, 12, 20, 21]*

## 7. Why These Algorithms Avoid ZKP Overhead

The user's query specifically concerns avoiding the "computational overhead of zero-knowledge proofs limiting network scale."

1.  **Deterministic Finality vs. Probabilistic Validity:** ZKPs are often used in "Rollups" to prove to a Layer 1 that a batch of off-chain transactions is valid. In contrast, HotStuff and SBFT provide **consensus at Layer 1**. They rely on the **honest majority assumption** ($2/3$ of validators are honest). Because the validators are known entities (banks/consortium members), the network trusts the *votes* of the validators rather than requiring a cryptographic *proof* of execution correctness [cite: 6, 20].
2.  **Signature Aggregation vs. Proof Generation:** SBFT uses BLS threshold signatures. Aggregating signatures is a computationally cheap operation compared to generating a zk-SNARK. A BLS signature aggregation takes milliseconds, whereas ZKP generation can take seconds or minutes depending on circuit complexity [cite: 20, 21].
3.  **Privacy via Permissioning:** Financial alliances often handle privacy by restricting data access to the specific parties involved in a transaction (using channels in Hyperledger or private payloads in Corda/Quorum) rather than putting all data on-chain and masking it with ZKPs. This architectural choice removes the need for ZKPs in the consensus critical path [cite: 8, 28].

## 8. Security and Robustness

### 8.1 Byzantine Fault Tolerance
Both HotStuff and SBFT offer safety against $f$ faulty nodes where $n \ge 3f+1$. This is the theoretical maximum for BFT systems. This means even if 33% of the financial institutions in the alliance are compromised or colluding, the ledger cannot be forked or falsified [cite: 6, 21].

### 8.2 Liveness and Responsiveness
A critical security parameter for finance is **Liveness** (the network keeps processing).
*   **HotStuff** excels here due to "Optimistic Responsiveness." It does not rely on synchronous clocks (which can be attacked via network delays) to drive progress, but moves as fast as the messages travel. This makes it resilient to "denial of service" attacks that try to slow down the network [cite: 10, 13].
*   **SBFT** includes a redundant server mechanism to ensure that if the primary collector fails, backups can take over immediately, minimizing downtime [cite: 20].

### 8.3 Post-Quantum Considerations
While not the primary focus of the query, some sources note that algorithms relying on specific elliptic curves (like BLS in SBFT) may eventually need upgrades to be quantum-resistant. However, FBA and HotStuff can theoretically swap signature schemes without changing the fundamental consensus logic [cite: 29, 30].

## 9. Conclusion

For a financial blockchain alliance seeking to balance security and throughput without the scalability limits imposed by Zero-Knowledge Proofs, the consensus algorithm of choice is **HotStuff (specifically the DiemBFT/AptosBFT variants)** or **Scalable BFT (SBFT)**.

*   **HotStuff/DiemBFT** is recommended for alliances requiring high-speed, continuous transaction processing with a rotating leader model that ensures fairness and responsiveness. Its linear communication complexity allows the consortium to scale to hundreds of members without performance degradation.
*   **SBFT** is recommended for enterprise deployments where a stable, optimized topology is preferred, utilizing threshold signatures to minimize bandwidth and client processing requirements. Its proven deployment in national-scale market infrastructure (VMware/ASX) validates its capability.

Both algorithms achieve the "Holy Grail" of BFT: **Linear Communication Complexity ($O(n)$)**. By replacing the "all-to-all" voting of the past with "all-to-leader" aggregation, they solve the scalability problem via architectural efficiency rather than heavy cryptographic computation, effectively answering the user's requirement for a high-performance consensus mechanism free from ZKP overhead.

## References
[cite: 1] Zero-Knowledge: The Future of More Secure and Scalable Blockchain
[cite: 29] Zero-Knowledge Proofs in Blockchain: Enhancing Privacy and Scalability
[cite: 2] Understanding Zero Knowledge Proofs and Their Importance
[cite: 5] IMF: Fintech Notes - Consensus Mechanisms
[cite: 3] High Performance Blockchain Consensus Algorithm
[cite: 7] Enhancing Performance of Bitcoin Trading Strategy
[cite: 8] Blockchain-Based Cryptocurrency Regulation
[cite: 6] Blockchain Protocols & Edge Computing Targeting Industry 5.0 Needs
[cite: 31] A Comparative Study of Blockchain Consensus Algorithms
[cite: 32] What is PBFT?
[cite: 33] Improved Fast-Response Consensus Algorithm Based on HotStuff
[cite: 34] Analytical Modeling of BFT Consensus Protocols
[cite: 14] Aptos vs Sui: A Fight of the New Generation Layer 1
[cite: 35] Consensus Algorithms in Blockchain
[cite: 36] Consensus Algorithm Classification
[cite: 20] SBFT: A Scalable and Decentralized Trust Infrastructure
[cite: 21] SBFT: A Scalable and Decentralized Trust Infrastructure (Paper)
[cite: 28] What is a Consensus Algorithm?
[cite: 22] Federated Byzantine Agreement
[cite: 23] Scaling Byzantine Consensus
[cite: 25] KPMG: Blockchain Consensus Mechanisms
[cite: 37] What is Federated Consensus?
[cite: 9] Xangle: Aptos Research
[cite: 15] AptosBFT: All You Need to Know
[cite: 10] HotStuff: BFT Consensus in the Lens of Blockchain
[cite: 4] Complexity of Consensus Protocols
[cite: 11] HotStuff Presentation
[cite: 38] Understanding HotStuff and BFT
[cite: 39] TPS Comparison of Consensus Algorithms
[cite: 21] SBFT vs PBFT Performance
[cite: 20] SBFT Evaluation
[cite: 24] A Deep Dive into Federated Byzantine Agreement
[cite: 30] FBA: Protection Against Quantum Threats
[cite: 40] Adaptive FBA
[cite: 27] Federated Byzantine Agreement Topics
[cite: 26] FBA in Payments
[cite: 16] Sui Research Papers
[cite: 17] Why is Sui Network So Popular?
[cite: 12] Diem Consensus: State Machine Replication in the Diem Blockchain
[cite: 18] Dell VMware Blockchain Enterprises
[cite: 21] SBFT Paper (VMware)
[cite: 19] VMware Blockchain Platform Enterprise Software
[cite: 20] SBFT Scalability Conclusion
[cite: 13] HotStuff BFT Consensus in the Lens of Blockchain

**Sources:**
1. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgGu6PUxDKqLXDFwsACHNuPSfY6hOyZJSPE5khLCI0p326aQAodqNkSMC_bS-izsFLsL1Skijo6kRgyB-kp8y7-Fnl0pGIS79olDxpyK526OhHV1G9Mxo6_ICS57c7VGEa2UJ1P3VLWvwlLJ16frVrdeZ2i1TYzNF7VHsir0CpdFZyVIpr0jOKuW_tw8MLQkOVtOWa9QlW3MR_OK92_rW-oB1HNA==)
2. [bitsgap.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnn9pdnQWZ2rVm24Xwh37A-c8pjEISLDu7l7h8NH2rppXGWTbvKIXD3wDDXnBY058Yl8iLxc2b99Gb-pnt0nMWiLBSOxzzQm_t2j1TyXAQsBCF-JwhU_4rs8ieSFI5Y-JfruNfjdkceR5HZNdy44Ebs3FXy7aj966almQk3DDIVb1jWYQABTs=)
3. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoHRufLI8ctA4ePvQ6n3zPKHDAuxgoqQAXIMCAB1XRj4FpRN8af-RUDhG5EQ69QiKtW31pmHxTpTp_oJralpYQj4TvdwgQVGkXmRSSr_RA4G7lakuItYxqixYPy5B__Wfpww8=)
4. [shs-conferences.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuCF1jCUtHsDbMzeGAgIg3PKlo-hdAxuKuyqOEdrFEpsXwkkCjJ5PpK3X4USHL5qUmlIBf-DVFCpgLrVsXef9wI4gxQOfEZODghVYefPEOLXoazePuixdwHZBd_FRbGOGFkE3FsJEM9xoosEjy_GkInEK4ro6o6KhMko0UJWQSuPpaT52CqheC59PrYA==)
5. [imf.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG40Nbd53Bu5nWBmJvS3UifRHwlOYFW2xdZreOAI8RjsbDpgNmthcuoAAfw8AcmjY4nJC400eMbZfPSaR2jwBP73W3SPP0F0h2aQsU4ebCWxlH7AqqccI4IAFYLQ27ok2kqQtMga3wVJ5q7ATbfDlDFGJXKcs3xt98WHaPh6vk4SiJQ4WGu4kLxUADh1A==)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAqHprePWNckVp-EhNnG-xE36U3qeqUqjwrK36Akc_FGPvP3xVezPzdrSSbZGTNwmNvDGn9diqRnAY0338RqIIMjzSLD2ymvWZKN6u5vK6xVkS4fivw1N7b9wUmF5A39mmG6LOh9qUB9EPmxTFdahYyqRjlx-gRJBKoCAm3YgmE4H4bbBmF6g63ARXpy8lPfmFdrveqgi5JA7vnFI1-LallI0rvPAkNjk=)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgv-_Wphkc4L9Hicih1wNAbJOTAOri7CCG1pWJz1pfHpr9bccWbL5m8ArrYS7TJgRx-mUA5w0x48rE70PwaESdr51fFpYounQ-1hiXMaY_mRc7ZDs-9si3PYSa59zWkvNJldg6XJ2laA==)
8. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxrzLINQK8Q50wlrPJnj_5p8mbpYf4my-97-X9ibStMF-Y0vb8bycE1dhv9oNgAhnDeNoyilqMiNsy5HiIqSDDa_fADfTtO35kNJjLsrYKqF7yKFGOl6sUAyXG)
9. [xangle.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFI5Q4YBKX6j1jRJHNf8U-ru8Rji4DmKt0KEOkycQ0O0rXjNhZByXHN26HIL0VEhjrjTiR2fMlTe19mgeB_snlcr3PJQi7fdG63f741DdCBJt_Jb5Oma9RkM_rxXlDL)
10. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtCtq98nAMgsdmY1m-rgzWUeayck6C5FA6QiUGgyHIbkDc8RlTNwkr-VxMXj4MzzmoaFUmSrmlS86ne6-1nPKsG9XqiB-5CzMByDmzV5eJHiOpT4-JXg==)
11. [expolab.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfd0IdjCVSl5aw4KEFC6wbxf_AAgwQBOhyP0GxWAKa57W4jpk9ieRV2BoEYU6lb9OZn8tQhwUZ5wKp8logs8fboMwWp2Ps3nmpLzZlpTtwX9FJBZ78RT4GK0C27Qvqev_I1sFMR7CJQvjS8RMy8DVlH5qwcfsNABZUnycllw==)
12. [diem.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsNx6T4LTd_kmxK643XjauSQeXbN1RjWUkPGITi1DOfv-BHg4iSPtVBQled6qhsNkkO8CDz7zH2oJcArgaOBu_9JqFhV4bPuyp2H3-H2H3XPWRYOE9RdrePyA24TqszIENKrbpzd8wTifICLD-yp09KNctrVjSWIxJFGdlfE2JhZVBUFDgvh4FCvUUzl3Bq5rfoc-PCWrOMHcDEuKS_0SG71y0PsDasg==)
13. [obsidian.md](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP6vYRXgCRwwI5dDgH4FcLyZCfL7yFjIrue_MaDW0lngQqZ1PV3Pcz96ELyc9-hXHFuebQl7GGE7XJVV5jMsWMRddaRETGtOIo8-z1cuuzJThNRLPyrBgWOYZw6eYC5cxWuqVVTydKBJNy7IsRWx61AUcAsxPhouUmvg0-zxwE0UWUOMIDUEefOMHfkhjZujUH-j9F_sPC)
14. [sotatek.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmNE4BG_0D0o_TtLY4TW0URpXdP4x2kfPSZWuuhpfwyYyDYa1-MnirIOf95vkzhwpfHnBj57rOPHyYHEtYWSeDDvzugOTI2h1NK5pfAqYl30FZSnnO16RtxZHZ9GpBdYQFnFMQw1WEJBZJU-LF5dh_PpA6ji1VUX1ycNIznQsXFGNNI7b1ucqQNVsiqX8o6dCaEv994O7gLPYoKbAlsYKw9RSjhwarFA==)
15. [pontem.network](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6C6Xq7KLYAV_xx97s84Bk_VVLpMtOPEs9ERbd6PgPcnIee1U0Or1DfKS9R4VaJ9Vs6Ww09fdKTOKbuYDS5YDtTLwnruykQcAA4Tjea1OhV7sQ0moo-awhyEv5EsdgXhqd1tk1ODuB1TR6tFZrkjaEWdzVOLmr3f2cVfzJDSLomBdZNjIon8MUAovUWhs-zm7c)
16. [sui.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDQIm-fXMXnZztz7O8N80yRLNbLCeXnusSQZGOeAylmjYFvU9MdWaMnS92Jz6l93g4yWTbj3NYHyn2ekDFoI0rMUp7p6dwpuJrZ02CYXyWWL3VMCfYFdoaM9AUSmQXGrfpxA==)
17. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFaVmFv5Q6sY8OCkgFLm1Fcsc0jGh01Kr5BmU9wC_4RX-9lVw23XoPyRvNve4kkhY5yYwPcW7hUn-xKbVwGFDnlDROmRJoB2Sjf6XWkSx1HCHYwupNMVfUa8rPnU8hxskzOAWO_uhZ8XP_WDSB8Yu1TQqmsB68npgytnwJ-LOHMPA==)
18. [theblock.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyHQYqEPa4lSTYWm9PbCyiTkH7caqGackPghQufjEY7bB4YURt44Ufiz2vkS-c7-v-KQ9CstrYqxJxKv_u1RDgrmQlsy-zWoVCseN7IK2_WEHZZBNAZWlNl7hWYmmWHn3cqENqt3eH6tjffusrAit0wBxNqousLCL7n2hfoA==)
19. [ciodive.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHj_kfJ8f58BT51drMz_NFbmfFaSpSLv3oe_KIaVczUJf-Ucx_zaCeiE5WbU2jxlTSanecSVaajXCXkYYqBfSPSlrjAWV56WNpGIGaW6EgNxr2i_1P_FRJ39RyZNNz12exGXv8xqVZwcoYpGiS3xBDeEV2wOsAHojOSaZIWSLQcnx4qkvgGh5s9BQ==)
20. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK9aSIXvLVK2WgZH2BSIDWcTVdyU8U08_hjY4vwQ5nItr5Wi8VkfTTDUpbYn_bJiOrngf9kOF3HTV1jTAegxhiXYQ5k1_SkJwXe5NSbM9oXxPD8U4BBg==)
21. [berkeley.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEW0J3Lc73qD0cx2uQlk9eVsRYqfEEAQ9TWhOP22nvBTDrupXuQzXd1pd6xRIhRF85VTbaFzXuGJgFRqF7EE7QvPujIEj7yubSWiKoaovs_egcr8342vtBG_Y7CLEDSMfmg2rX__1Dx-iIzT7qskecQ3UioE_gmkWEkg60vTiL948N_xxtrfLqfk_A8X2HLeupthelOnWc1pckhlDc0Oxcv6GkJ4wdpfcB_-kDH63YQR5idC90jCvGxltbkw0cJAg==)
22. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEo9KG_o2E0BJUsCWm_9ZCZmPnIGHobKbnzNRZ4grjEMI62j0JbxQIrPl_X1DzerBe1xtAyPhB0U8JeLFpkkKDTyyRnGmQ17xkeztIbGsy5eGfowPrxtQ==)
23. [uni-passau.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmkO3DGcmJj6vnNjo1jyLydxB0PZYQucb2DZ6n7ezzGDshhPDpmAEi_N_M6No0x7U0omZGqHbvVve2drlcFdEaj2JuEVDaGK5REOd2kWnG5RWZxtIkQY_w1P3fZRzUglEuDuTmqubvwC8pVqeryUjaP_M_xtk1-te9P_Mc6TRyWTd-HhipF6_pEDZkRFoTNArmlWXM9eXR0I0SREoK0LPAIzk4DKkeQsy4CpPyxPQUjqg-7BgE)
24. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTHThXHskXh7zn5sWZoLHzpCk1TGcY7SZyRDU5IJhGlktaXB6TIvU_RdZneF680zFjFTbIIVD5ckmjp8LBZP5WQHJ-ag5V1OPr-yq-SAlaZlCDnZ5-nOQXHb4SEj0Sfza4KWTSSsSFxxRkD9gbfqLxe7hzVkHHlKGdofty45wKl0wypckXxiC-mU6DxK2cnybwaHUkKBrZutLNWsQulRgJ6DtJPEPUBc6EmA==)
25. [kpmg.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpg3kGKrFRQD-0sGqdsMGTvLjLYNKEE93sWZUrzmdGB_NAxI1NbEQ4t6RrNrqjeWne7M_jtHmCN3NQPLdhUyiTLF-3tiTgdxqYfwNqFGilUi0i1xPp9tJNacA-SCtsvEP6zhZtgURPtZWfKjteJAZ-sXN3YExfSB8O__flMe_AFCthfwK_-_D9_SI72T5eEBGj3A==)
26. [faisalkhan.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUnEFyShg2e_7Oi8hY-wKCz9omVXsQAqgSKj8S46aFZRiQdIHjlIq7i_5Kh-kk3Mp7XP1K_LBxDhJpR3VwzIEzJkqxbM_1vHWzNw_wG8osqOpbEUZxvlD2TO5g3pjY9zJ0YM8lYNZJ_q4Au5NioFIPL__p97f1zIO0-Tnm0X_BFA-LqZojj-jLWpSObq3pwz8=)
27. [emergentmind.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFW5wGuiKRfEyCVA9dLSwvzo7UESTyXhFik1xTmBpJoH-70OUduQ1u0fuyEdSh0boIF06eFMT32Os9kPdbMIGPNn4iW6o7XNMe2zbi8sfaTrSQq9yOiwH7BKs2hTfYvnHPq4Klyax14Cu84MxJ5g-52sd0hn4PGl-ZHNyY=)
28. [spydra.app](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbXntcz5871ww4lzDtNV6INd4JqI-FYqAuqmsKUUuYwlhaanTb6N-kWsouxyXcmHorxD6oz1MUxYuqz_STS98auUCBWa-0dN7lVin6aMLfjgKxYfvcG_i4LgZoVguMItRXVGaDVHZ1RnDq3WOCXxI=)
29. [rapidinnovation.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMxJDUCSnooW8UFYhmc5XGvBO_ISGPaG8wc_PKMMuMkCJeBQkLneTrGmc4TGegN779UXVoImBK73_LcNONlrjNZS4M0CTKRvnILm5f9aGYhuVqMKuLLLq0s-nSYKfRJiLIFWXQ986StQDnuyEZSSsn0kUWHNeUBAVC6AyoCSrmHQcmEYnzrQvzyYsjdFWxE8i9jUGN_PWbBdHXjr_3XEE=)
30. [xdbchain.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7gW83sXuxdZraIH0AZshVwkTwG3ht67jSM_SVH-aJcAgpgLPo4WRfCXQru-VUeV3yxcSQxlQ_oe1QvMNYTYcv2WmJUkYrn7EPyJdxGgnkcPEStarNI696zn9Vs4VNgX7rVtTPBrHeHgFwbNiRX7WFfQqylQcdckUYpulMoph1DCXlfDGxrQJW70TWhFTuRDwLNv-G1vgdDWJpl4f2KCr6rJZGgqhRiuU=)
31. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9VRHtmBkRh5bfPO81VE10DlXnu2PCdsfEJtm_4Wvv0F285P0LM6RaGmvwwLvtNyUz2sYZNvT59xJop3l-gK7tpdsNZrg2NvcB_1uGn7mkL1R0zILpzvVCsTk_yh82RK7onEiYmqkx5b3E)
32. [cube.exchange](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMQVUvZnuDzkFCFgGLXxTWnw__7Kban3u9eTYTrqiFWiUFd2VJL0y7Tf9DqW9_Aj5lLUDFFe_zVdm9AQUBoW_25l1i2X2mVzUMGiX0Eu8RzL6JacdblgzDArWfEQxYbIBvBpf5Mq0YJQdKC33lssWNjJEh1Oat3h1ULXNbAvSinA==)
33. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHDhwEWvClTuHmMHlIVYlNViZEjJHncod0gGqsnMWWFOrE7w0PV0zxiXAaQXHwWtT5Pe4ttMLw5NrRydokUMV6oUx418n2S6sW6bJ6UzF-qV92xj3T-qGFaiCeBh_kpcbnAV7VIg-J4UUrFBKowOSLrJmOENn-JU1yVUCA_wJwTEe1SDok80BTaRhv1gY_ZOsD4BgWqUiIorTf1iPYRs1qfOx3dDE=)
34. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgVGeOpocpnKC5DMdLPB3kAjSeL4cPmK86ykIlqw8GZzVJj29Me8NwZDo7--GmAiWAzRTE6BQtiospxFe_ORj5bY83EWSAsOpG02e-5ITzG3waFvUZ9TuZqQ==)
35. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvUanjK81M7MVa_I8fSFPqkfVvBFmIvSqWRfYS1UACfFxtXb7GFMntaII5vnsvDGvxcgY-s63mVLKe_2A7NPwR4Z8CNTeffwjyvJc5CSDOnXL-asoR-D8yl0QOYM4Xag==)
36. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGq4CTbeyaKLU9UriQpOso3LKwX5_s7wkw49YMUcGxKi-Bgz4dzGDIHMxBR8SUuoIoTzYqmdWNqt4KP1Q7piFudo1RHwuPE1Oyax4ZBBdKgsKQ1WpgODQ==)
37. [cube.exchange](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuzo_ZQgPf-_qW-AvFKYfZqZQIE4V8kUt4RTozkNjgpDnrYZqnfvBGjkcjKTuseqVUg1EYCd1z_klU0hRxdYv2a362a1I2AfZVYIk7CDTeOUzkjwpmdhMFl_W3yoqE0H992cToPdTYBt0P5Q==)
38. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaU3yGaF89eLUO9qqtpHf5Ft_KPb5CkFRYfocil6HrdkgXaaDNbABzRCZASNgD5URwr-mj6A0yxPgdZKJbdbQhk8ljQnyFlFwSt00_q4-2-7EKJlk6CbEomt_y-En-DHT9hkUbYHPEnztjhGqhUc-bHlc2QpHe6QvMSPtJFOetuCHhK0KMwdjsjxAzR026nr64XZN7igXJ1IY=)
39. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTbwIsf7TH_mzcE6Ak3BIxbkhuXG39k3zh88r74Y419IoVtXWzVNfDVNO76zyq3DAKIfj465tTPsvCsQPKo-EbMCdPj04TUdhiWz67YkVQ7WqUdE6RyFbV58ihy_Y=)
40. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFo8ZAimSisdPMbIZlG4u09kZo7cYEH-b0cl61E7pKumFnmWmw2BkljOoMD8UjLaAjQzf4XD1xbBnMNpsbiaTERqMrOYKp46D7oAXe8O9nT6T31KnvN9u8UFdk=)


## Annotations
Annotation(end_index=2585, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgGu6PUxDKqLXDFwsACHNuPSfY6hOyZJSPE5khLCI0p326aQAodqNkSMC_bS-izsFLsL1Skijo6kRgyB-kp8y7-Fnl0pGIS79olDxpyK526OhHV1G9Mxo6_ICS57c7VGEa2UJ1P3VLWvwlLJ16frVrdeZ2i1TYzNF7VHsir0CpdFZyVIpr0jOKuW_tw8MLQkOVtOWa9QlW3MR_OK92_rW-oB1HNA==', start_index=2573)
Annotation(end_index=2585, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnn9pdnQWZ2rVm24Xwh37A-c8pjEISLDu7l7h8NH2rppXGWTbvKIXD3wDDXnBY058Yl8iLxc2b99Gb-pnt0nMWiLBSOxzzQm_t2j1TyXAQsBCF-JwhU_4rs8ieSFI5Y-JfruNfjdkceR5HZNdy44Ebs3FXy7aj966almQk3DDIVb1jWYQABTs=', start_index=2573)
Annotation(end_index=3164, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuCF1jCUtHsDbMzeGAgIg3PKlo-hdAxuKuyqOEdrFEpsXwkkCjJ5PpK3X4USHL5qUmlIBf-DVFCpgLrVsXef9wI4gxQOfEZODghVYefPEOLXoazePuixdwHZBd_FRbGOGFkE3FsJEM9xoosEjy_GkInEK4ro6o6KhMko0UJWQSuPpaT52CqheC59PrYA==', start_index=3152)
Annotation(end_index=3164, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoHRufLI8ctA4ePvQ6n3zPKHDAuxgoqQAXIMCAB1XRj4FpRN8af-RUDhG5EQ69QiKtW31pmHxTpTp_oJralpYQj4TvdwgQVGkXmRSSr_RA4G7lakuItYxqixYPy5B__Wfpww8=', start_index=3152)
Annotation(end_index=4156, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG40Nbd53Bu5nWBmJvS3UifRHwlOYFW2xdZreOAI8RjsbDpgNmthcuoAAfw8AcmjY4nJC400eMbZfPSaR2jwBP73W3SPP0F0h2aQsU4ebCWxlH7AqqccI4IAFYLQ27ok2kqQtMga3wVJ5q7ATbfDlDFGJXKcs3xt98WHaPh6vk4SiJQ4WGu4kLxUADh1A==', start_index=4147)
Annotation(end_index=4305, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAqHprePWNckVp-EhNnG-xE36U3qeqUqjwrK36Akc_FGPvP3xVezPzdrSSbZGTNwmNvDGn9diqRnAY0338RqIIMjzSLD2ymvWZKN6u5vK6xVkS4fivw1N7b9wUmF5A39mmG6LOh9qUB9EPmxTFdahYyqRjlx-gRJBKoCAm3YgmE4H4bbBmF6g63ARXpy8lPfmFdrveqgi5JA7vnFI1-LallI0rvPAkNjk=', start_index=4296)
Annotation(end_index=4421, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgv-_Wphkc4L9Hicih1wNAbJOTAOri7CCG1pWJz1pfHpr9bccWbL5m8ArrYS7TJgRx-mUA5w0x48rE70PwaESdr51fFpYounQ-1hiXMaY_mRc7ZDs-9si3PYSa59zWkvNJldg6XJ2laA==', start_index=4412)
Annotation(end_index=4795, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgGu6PUxDKqLXDFwsACHNuPSfY6hOyZJSPE5khLCI0p326aQAodqNkSMC_bS-izsFLsL1Skijo6kRgyB-kp8y7-Fnl0pGIS79olDxpyK526OhHV1G9Mxo6_ICS57c7VGEa2UJ1P3VLWvwlLJ16frVrdeZ2i1TYzNF7VHsir0CpdFZyVIpr0jOKuW_tw8MLQkOVtOWa9QlW3MR_OK92_rW-oB1HNA==', start_index=4783)
Annotation(end_index=4795, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnn9pdnQWZ2rVm24Xwh37A-c8pjEISLDu7l7h8NH2rppXGWTbvKIXD3wDDXnBY058Yl8iLxc2b99Gb-pnt0nMWiLBSOxzzQm_t2j1TyXAQsBCF-JwhU_4rs8ieSFI5Y-JfruNfjdkceR5HZNdy44Ebs3FXy7aj966almQk3DDIVb1jWYQABTs=', start_index=4783)
Annotation(end_index=5053, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgGu6PUxDKqLXDFwsACHNuPSfY6hOyZJSPE5khLCI0p326aQAodqNkSMC_bS-izsFLsL1Skijo6kRgyB-kp8y7-Fnl0pGIS79olDxpyK526OhHV1G9Mxo6_ICS57c7VGEa2UJ1P3VLWvwlLJ16frVrdeZ2i1TYzNF7VHsir0CpdFZyVIpr0jOKuW_tw8MLQkOVtOWa9QlW3MR_OK92_rW-oB1HNA==', start_index=5041)
Annotation(end_index=5053, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnn9pdnQWZ2rVm24Xwh37A-c8pjEISLDu7l7h8NH2rppXGWTbvKIXD3wDDXnBY058Yl8iLxc2b99Gb-pnt0nMWiLBSOxzzQm_t2j1TyXAQsBCF-JwhU_4rs8ieSFI5Y-JfruNfjdkceR5HZNdy44Ebs3FXy7aj966almQk3DDIVb1jWYQABTs=', start_index=5041)
Annotation(end_index=5348, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxrzLINQK8Q50wlrPJnj_5p8mbpYf4my-97-X9ibStMF-Y0vb8bycE1dhv9oNgAhnDeNoyilqMiNsy5HiIqSDDa_fADfTtO35kNJjLsrYKqF7yKFGOl6sUAyXG', start_index=5339)
Annotation(end_index=5832, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFI5Q4YBKX6j1jRJHNf8U-ru8Rji4DmKt0KEOkycQ0O0rXjNhZByXHN26HIL0VEhjrjTiR2fMlTe19mgeB_snlcr3PJQi7fdG63f741DdCBJt_Jb5Oma9RkM_rxXlDL', start_index=5816)
Annotation(end_index=5832, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAqHprePWNckVp-EhNnG-xE36U3qeqUqjwrK36Akc_FGPvP3xVezPzdrSSbZGTNwmNvDGn9diqRnAY0338RqIIMjzSLD2ymvWZKN6u5vK6xVkS4fivw1N7b9wUmF5A39mmG6LOh9qUB9EPmxTFdahYyqRjlx-gRJBKoCAm3YgmE4H4bbBmF6g63ARXpy8lPfmFdrveqgi5JA7vnFI1-LallI0rvPAkNjk=', start_index=5816)
Annotation(end_index=5832, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtCtq98nAMgsdmY1m-rgzWUeayck6C5FA6QiUGgyHIbkDc8RlTNwkr-VxMXj4MzzmoaFUmSrmlS86ne6-1nPKsG9XqiB-5CzMByDmzV5eJHiOpT4-JXg==', start_index=5816)
Annotation(end_index=6484, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfd0IdjCVSl5aw4KEFC6wbxf_AAgwQBOhyP0GxWAKa57W4jpk9ieRV2BoEYU6lb9OZn8tQhwUZ5wKp8logs8fboMwWp2Ps3nmpLzZlpTtwX9FJBZ78RT4GK0C27Qvqev_I1sFMR7CJQvjS8RMy8DVlH5qwcfsNABZUnycllw==', start_index=6470)
Annotation(end_index=6484, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtCtq98nAMgsdmY1m-rgzWUeayck6C5FA6QiUGgyHIbkDc8RlTNwkr-VxMXj4MzzmoaFUmSrmlS86ne6-1nPKsG9XqiB-5CzMByDmzV5eJHiOpT4-JXg==', start_index=6470)
Annotation(end_index=6893, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsNx6T4LTd_kmxK643XjauSQeXbN1RjWUkPGITi1DOfv-BHg4iSPtVBQled6qhsNkkO8CDz7zH2oJcArgaOBu_9JqFhV4bPuyp2H3-H2H3XPWRYOE9RdrePyA24TqszIENKrbpzd8wTifICLD-yp09KNctrVjSWIxJFGdlfE2JhZVBUFDgvh4FCvUUzl3Bq5rfoc-PCWrOMHcDEuKS_0SG71y0PsDasg==', start_index=6879)
Annotation(end_index=6893, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtCtq98nAMgsdmY1m-rgzWUeayck6C5FA6QiUGgyHIbkDc8RlTNwkr-VxMXj4MzzmoaFUmSrmlS86ne6-1nPKsG9XqiB-5CzMByDmzV5eJHiOpT4-JXg==', start_index=6879)
Annotation(end_index=7215, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP6vYRXgCRwwI5dDgH4FcLyZCfL7yFjIrue_MaDW0lngQqZ1PV3Pcz96ELyc9-hXHFuebQl7GGE7XJVV5jMsWMRddaRETGtOIo8-z1cuuzJThNRLPyrBgWOYZw6eYC5cxWuqVVTydKBJNy7IsRWx61AUcAsxPhouUmvg0-zxwE0UWUOMIDUEefOMHfkhjZujUH-j9F_sPC', start_index=7201)
Annotation(end_index=7215, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtCtq98nAMgsdmY1m-rgzWUeayck6C5FA6QiUGgyHIbkDc8RlTNwkr-VxMXj4MzzmoaFUmSrmlS86ne6-1nPKsG9XqiB-5CzMByDmzV5eJHiOpT4-JXg==', start_index=7201)
Annotation(end_index=7559, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsNx6T4LTd_kmxK643XjauSQeXbN1RjWUkPGITi1DOfv-BHg4iSPtVBQled6qhsNkkO8CDz7zH2oJcArgaOBu_9JqFhV4bPuyp2H3-H2H3XPWRYOE9RdrePyA24TqszIENKrbpzd8wTifICLD-yp09KNctrVjSWIxJFGdlfE2JhZVBUFDgvh4FCvUUzl3Bq5rfoc-PCWrOMHcDEuKS_0SG71y0PsDasg==', start_index=7549)
Annotation(end_index=7791, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsNx6T4LTd_kmxK643XjauSQeXbN1RjWUkPGITi1DOfv-BHg4iSPtVBQled6qhsNkkO8CDz7zH2oJcArgaOBu_9JqFhV4bPuyp2H3-H2H3XPWRYOE9RdrePyA24TqszIENKrbpzd8wTifICLD-yp09KNctrVjSWIxJFGdlfE2JhZVBUFDgvh4FCvUUzl3Bq5rfoc-PCWrOMHcDEuKS_0SG71y0PsDasg==', start_index=7778)
Annotation(end_index=7791, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAqHprePWNckVp-EhNnG-xE36U3qeqUqjwrK36Akc_FGPvP3xVezPzdrSSbZGTNwmNvDGn9diqRnAY0338RqIIMjzSLD2ymvWZKN6u5vK6xVkS4fivw1N7b9wUmF5A39mmG6LOh9qUB9EPmxTFdahYyqRjlx-gRJBKoCAm3YgmE4H4bbBmF6g63ARXpy8lPfmFdrveqgi5JA7vnFI1-LallI0rvPAkNjk=', start_index=7778)
Annotation(end_index=7983, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsNx6T4LTd_kmxK643XjauSQeXbN1RjWUkPGITi1DOfv-BHg4iSPtVBQled6qhsNkkO8CDz7zH2oJcArgaOBu_9JqFhV4bPuyp2H3-H2H3XPWRYOE9RdrePyA24TqszIENKrbpzd8wTifICLD-yp09KNctrVjSWIxJFGdlfE2JhZVBUFDgvh4FCvUUzl3Bq5rfoc-PCWrOMHcDEuKS_0SG71y0PsDasg==', start_index=7973)
Annotation(end_index=8223, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAqHprePWNckVp-EhNnG-xE36U3qeqUqjwrK36Akc_FGPvP3xVezPzdrSSbZGTNwmNvDGn9diqRnAY0338RqIIMjzSLD2ymvWZKN6u5vK6xVkS4fivw1N7b9wUmF5A39mmG6LOh9qUB9EPmxTFdahYyqRjlx-gRJBKoCAm3YgmE4H4bbBmF6g63ARXpy8lPfmFdrveqgi5JA7vnFI1-LallI0rvPAkNjk=', start_index=8214)
Annotation(end_index=8526, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6C6Xq7KLYAV_xx97s84Bk_VVLpMtOPEs9ERbd6PgPcnIee1U0Or1DfKS9R4VaJ9Vs6Ww09fdKTOKbuYDS5YDtTLwnruykQcAA4Tjea1OhV7sQ0moo-awhyEv5EsdgXhqd1tk1ODuB1TR6tFZrkjaEWdzVOLmr3f2cVfzJDSLomBdZNjIon8MUAovUWhs-zm7c', start_index=8512)
Annotation(end_index=8526, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmNE4BG_0D0o_TtLY4TW0URpXdP4x2kfPSZWuuhpfwyYyDYa1-MnirIOf95vkzhwpfHnBj57rOPHyYHEtYWSeDDvzugOTI2h1NK5pfAqYl30FZSnnO16RtxZHZ9GpBdYQFnFMQw1WEJBZJU-LF5dh_PpA6ji1VUX1ycNIznQsXFGNNI7b1ucqQNVsiqX8o6dCaEv994O7gLPYoKbAlsYKw9RSjhwarFA==', start_index=8512)
Annotation(end_index=8878, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFaVmFv5Q6sY8OCkgFLm1Fcsc0jGh01Kr5BmU9wC_4RX-9lVw23XoPyRvNve4kkhY5yYwPcW7hUn-xKbVwGFDnlDROmRJoB2Sjf6XWkSx1HCHYwupNMVfUa8rPnU8hxskzOAWO_uhZ8XP_WDSB8Yu1TQqmsB68npgytnwJ-LOHMPA==', start_index=8864)
Annotation(end_index=8878, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDQIm-fXMXnZztz7O8N80yRLNbLCeXnusSQZGOeAylmjYFvU9MdWaMnS92Jz6l93g4yWTbj3NYHyn2ekDFoI0rMUp7p6dwpuJrZ02CYXyWWL3VMCfYFdoaM9AUSmQXGrfpxA==', start_index=8864)
Annotation(end_index=9321, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHj_kfJ8f58BT51drMz_NFbmfFaSpSLv3oe_KIaVczUJf-Ucx_zaCeiE5WbU2jxlTSanecSVaajXCXkYYqBfSPSlrjAWV56WNpGIGaW6EgNxr2i_1P_FRJ39RyZNNz12exGXv8xqVZwcoYpGiS3xBDeEV2wOsAHojOSaZIWSLQcnx4qkvgGh5s9BQ==', start_index=9307)
Annotation(end_index=9321, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyHQYqEPa4lSTYWm9PbCyiTkH7caqGackPghQufjEY7bB4YURt44Ufiz2vkS-c7-v-KQ9CstrYqxJxKv_u1RDgrmQlsy-zWoVCseN7IK2_WEHZZBNAZWlNl7hWYmmWHn3cqENqt3eH6tjffusrAit0wBxNqousLCL7n2hfoA==', start_index=9307)
Annotation(end_index=9561, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEW0J3Lc73qD0cx2uQlk9eVsRYqfEEAQ9TWhOP22nvBTDrupXuQzXd1pd6xRIhRF85VTbaFzXuGJgFRqF7EE7QvPujIEj7yubSWiKoaovs_egcr8342vtBG_Y7CLEDSMfmg2rX__1Dx-iIzT7qskecQ3UioE_gmkWEkg60vTiL948N_xxtrfLqfk_A8X2HLeupthelOnWc1pckhlDc0Oxcv6GkJ4wdpfcB_-kDH63YQR5idC90jCvGxltbkw0cJAg==', start_index=9547)
Annotation(end_index=9561, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK9aSIXvLVK2WgZH2BSIDWcTVdyU8U08_hjY4vwQ5nItr5Wi8VkfTTDUpbYn_bJiOrngf9kOF3HTV1jTAegxhiXYQ5k1_SkJwXe5NSbM9oXxPD8U4BBg==', start_index=9547)
Annotation(end_index=10029, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEW0J3Lc73qD0cx2uQlk9eVsRYqfEEAQ9TWhOP22nvBTDrupXuQzXd1pd6xRIhRF85VTbaFzXuGJgFRqF7EE7QvPujIEj7yubSWiKoaovs_egcr8342vtBG_Y7CLEDSMfmg2rX__1Dx-iIzT7qskecQ3UioE_gmkWEkg60vTiL948N_xxtrfLqfk_A8X2HLeupthelOnWc1pckhlDc0Oxcv6GkJ4wdpfcB_-kDH63YQR5idC90jCvGxltbkw0cJAg==', start_index=10015)
Annotation(end_index=10029, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK9aSIXvLVK2WgZH2BSIDWcTVdyU8U08_hjY4vwQ5nItr5Wi8VkfTTDUpbYn_bJiOrngf9kOF3HTV1jTAegxhiXYQ5k1_SkJwXe5NSbM9oXxPD8U4BBg==', start_index=10015)
Annotation(end_index=10431, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEW0J3Lc73qD0cx2uQlk9eVsRYqfEEAQ9TWhOP22nvBTDrupXuQzXd1pd6xRIhRF85VTbaFzXuGJgFRqF7EE7QvPujIEj7yubSWiKoaovs_egcr8342vtBG_Y7CLEDSMfmg2rX__1Dx-iIzT7qskecQ3UioE_gmkWEkg60vTiL948N_xxtrfLqfk_A8X2HLeupthelOnWc1pckhlDc0Oxcv6GkJ4wdpfcB_-kDH63YQR5idC90jCvGxltbkw0cJAg==', start_index=10417)
Annotation(end_index=10431, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK9aSIXvLVK2WgZH2BSIDWcTVdyU8U08_hjY4vwQ5nItr5Wi8VkfTTDUpbYn_bJiOrngf9kOF3HTV1jTAegxhiXYQ5k1_SkJwXe5NSbM9oXxPD8U4BBg==', start_index=10417)
Annotation(end_index=10721, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEW0J3Lc73qD0cx2uQlk9eVsRYqfEEAQ9TWhOP22nvBTDrupXuQzXd1pd6xRIhRF85VTbaFzXuGJgFRqF7EE7QvPujIEj7yubSWiKoaovs_egcr8342vtBG_Y7CLEDSMfmg2rX__1Dx-iIzT7qskecQ3UioE_gmkWEkg60vTiL948N_xxtrfLqfk_A8X2HLeupthelOnWc1pckhlDc0Oxcv6GkJ4wdpfcB_-kDH63YQR5idC90jCvGxltbkw0cJAg==', start_index=10707)
Annotation(end_index=10721, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK9aSIXvLVK2WgZH2BSIDWcTVdyU8U08_hjY4vwQ5nItr5Wi8VkfTTDUpbYn_bJiOrngf9kOF3HTV1jTAegxhiXYQ5k1_SkJwXe5NSbM9oXxPD8U4BBg==', start_index=10707)
Annotation(end_index=10948, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEW0J3Lc73qD0cx2uQlk9eVsRYqfEEAQ9TWhOP22nvBTDrupXuQzXd1pd6xRIhRF85VTbaFzXuGJgFRqF7EE7QvPujIEj7yubSWiKoaovs_egcr8342vtBG_Y7CLEDSMfmg2rX__1Dx-iIzT7qskecQ3UioE_gmkWEkg60vTiL948N_xxtrfLqfk_A8X2HLeupthelOnWc1pckhlDc0Oxcv6GkJ4wdpfcB_-kDH63YQR5idC90jCvGxltbkw0cJAg==', start_index=10934)
Annotation(end_index=10948, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK9aSIXvLVK2WgZH2BSIDWcTVdyU8U08_hjY4vwQ5nItr5Wi8VkfTTDUpbYn_bJiOrngf9kOF3HTV1jTAegxhiXYQ5k1_SkJwXe5NSbM9oXxPD8U4BBg==', start_index=10934)
Annotation(end_index=11496, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHj_kfJ8f58BT51drMz_NFbmfFaSpSLv3oe_KIaVczUJf-Ucx_zaCeiE5WbU2jxlTSanecSVaajXCXkYYqBfSPSlrjAWV56WNpGIGaW6EgNxr2i_1P_FRJ39RyZNNz12exGXv8xqVZwcoYpGiS3xBDeEV2wOsAHojOSaZIWSLQcnx4qkvgGh5s9BQ==', start_index=11482)
Annotation(end_index=11496, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyHQYqEPa4lSTYWm9PbCyiTkH7caqGackPghQufjEY7bB4YURt44Ufiz2vkS-c7-v-KQ9CstrYqxJxKv_u1RDgrmQlsy-zWoVCseN7IK2_WEHZZBNAZWlNl7hWYmmWHn3cqENqt3eH6tjffusrAit0wBxNqousLCL7n2hfoA==', start_index=11482)
Annotation(end_index=12173, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEo9KG_o2E0BJUsCWm_9ZCZmPnIGHobKbnzNRZ4grjEMI62j0JbxQIrPl_X1DzerBe1xtAyPhB0U8JeLFpkkKDTyyRnGmQ17xkeztIbGsy5eGfowPrxtQ==', start_index=12155)
Annotation(end_index=12173, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTHThXHskXh7zn5sWZoLHzpCk1TGcY7SZyRDU5IJhGlktaXB6TIvU_RdZneF680zFjFTbIIVD5ckmjp8LBZP5WQHJ-ag5V1OPr-yq-SAlaZlCDnZ5-nOQXHb4SEj0Sfza4KWTSSsSFxxRkD9gbfqLxe7hzVkHHlKGdofty45wKl0wypckXxiC-mU6DxK2cnybwaHUkKBrZutLNWsQulRgJ6DtJPEPUBc6EmA==', start_index=12155)
Annotation(end_index=12173, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmkO3DGcmJj6vnNjo1jyLydxB0PZYQucb2DZ6n7ezzGDshhPDpmAEi_N_M6No0x7U0omZGqHbvVve2drlcFdEaj2JuEVDaGK5REOd2kWnG5RWZxtIkQY_w1P3fZRzUglEuDuTmqubvwC8pVqeryUjaP_M_xtk1-te9P_Mc6TRyWTd-HhipF6_pEDZkRFoTNArmlWXM9eXR0I0SREoK0LPAIzk4DKkeQsy4CpPyxPQUjqg-7BgE', start_index=12155)
Annotation(end_index=12457, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpg3kGKrFRQD-0sGqdsMGTvLjLYNKEE93sWZUrzmdGB_NAxI1NbEQ4t6RrNrqjeWne7M_jtHmCN3NQPLdhUyiTLF-3tiTgdxqYfwNqFGilUi0i1xPp9tJNacA-SCtsvEP6zhZtgURPtZWfKjteJAZ-sXN3YExfSB8O__flMe_AFCthfwK_-_D9_SI72T5eEBGj3A==', start_index=12443)
Annotation(end_index=12457, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUnEFyShg2e_7Oi8hY-wKCz9omVXsQAqgSKj8S46aFZRiQdIHjlIq7i_5Kh-kk3Mp7XP1K_LBxDhJpR3VwzIEzJkqxbM_1vHWzNw_wG8osqOpbEUZxvlD2TO5g3pjY9zJ0YM8lYNZJ_q4Au5NioFIPL__p97f1zIO0-Tnm0X_BFA-LqZojj-jLWpSObq3pwz8=', start_index=12443)
Annotation(end_index=12680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFW5wGuiKRfEyCVA9dLSwvzo7UESTyXhFik1xTmBpJoH-70OUduQ1u0fuyEdSh0boIF06eFMT32Os9kPdbMIGPNn4iW6o7XNMe2zbi8sfaTrSQq9yOiwH7BKs2hTfYvnHPq4Klyax14Cu84MxJ5g-52sd0hn4PGl-ZHNyY=', start_index=12666)
Annotation(end_index=12680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmkO3DGcmJj6vnNjo1jyLydxB0PZYQucb2DZ6n7ezzGDshhPDpmAEi_N_M6No0x7U0omZGqHbvVve2drlcFdEaj2JuEVDaGK5REOd2kWnG5RWZxtIkQY_w1P3fZRzUglEuDuTmqubvwC8pVqeryUjaP_M_xtk1-te9P_Mc6TRyWTd-HhipF6_pEDZkRFoTNArmlWXM9eXR0I0SREoK0LPAIzk4DKkeQsy4CpPyxPQUjqg-7BgE', start_index=12666)
Annotation(end_index=12951, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFW5wGuiKRfEyCVA9dLSwvzo7UESTyXhFik1xTmBpJoH-70OUduQ1u0fuyEdSh0boIF06eFMT32Os9kPdbMIGPNn4iW6o7XNMe2zbi8sfaTrSQq9yOiwH7BKs2hTfYvnHPq4Klyax14Cu84MxJ5g-52sd0hn4PGl-ZHNyY=', start_index=12941)
Annotation(end_index=14122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEW0J3Lc73qD0cx2uQlk9eVsRYqfEEAQ9TWhOP22nvBTDrupXuQzXd1pd6xRIhRF85VTbaFzXuGJgFRqF7EE7QvPujIEj7yubSWiKoaovs_egcr8342vtBG_Y7CLEDSMfmg2rX__1Dx-iIzT7qskecQ3UioE_gmkWEkg60vTiL948N_xxtrfLqfk_A8X2HLeupthelOnWc1pckhlDc0Oxcv6GkJ4wdpfcB_-kDH63YQR5idC90jCvGxltbkw0cJAg==', start_index=14091)
Annotation(end_index=14122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsNx6T4LTd_kmxK643XjauSQeXbN1RjWUkPGITi1DOfv-BHg4iSPtVBQled6qhsNkkO8CDz7zH2oJcArgaOBu_9JqFhV4bPuyp2H3-H2H3XPWRYOE9RdrePyA24TqszIENKrbpzd8wTifICLD-yp09KNctrVjSWIxJFGdlfE2JhZVBUFDgvh4FCvUUzl3Bq5rfoc-PCWrOMHcDEuKS_0SG71y0PsDasg==', start_index=14091)
Annotation(end_index=14122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuCF1jCUtHsDbMzeGAgIg3PKlo-hdAxuKuyqOEdrFEpsXwkkCjJ5PpK3X4USHL5qUmlIBf-DVFCpgLrVsXef9wI4gxQOfEZODghVYefPEOLXoazePuixdwHZBd_FRbGOGFkE3FsJEM9xoosEjy_GkInEK4ro6o6KhMko0UJWQSuPpaT52CqheC59PrYA==', start_index=14091)
Annotation(end_index=14122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAqHprePWNckVp-EhNnG-xE36U3qeqUqjwrK36Akc_FGPvP3xVezPzdrSSbZGTNwmNvDGn9diqRnAY0338RqIIMjzSLD2ymvWZKN6u5vK6xVkS4fivw1N7b9wUmF5A39mmG6LOh9qUB9EPmxTFdahYyqRjlx-gRJBKoCAm3YgmE4H4bbBmF6g63ARXpy8lPfmFdrveqgi5JA7vnFI1-LallI0rvPAkNjk=', start_index=14091)
Annotation(end_index=14122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtCtq98nAMgsdmY1m-rgzWUeayck6C5FA6QiUGgyHIbkDc8RlTNwkr-VxMXj4MzzmoaFUmSrmlS86ne6-1nPKsG9XqiB-5CzMByDmzV5eJHiOpT4-JXg==', start_index=14091)
Annotation(end_index=14122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK9aSIXvLVK2WgZH2BSIDWcTVdyU8U08_hjY4vwQ5nItr5Wi8VkfTTDUpbYn_bJiOrngf9kOF3HTV1jTAegxhiXYQ5k1_SkJwXe5NSbM9oXxPD8U4BBg==', start_index=14091)
Annotation(end_index=14122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoHRufLI8ctA4ePvQ6n3zPKHDAuxgoqQAXIMCAB1XRj4FpRN8af-RUDhG5EQ69QiKtW31pmHxTpTp_oJralpYQj4TvdwgQVGkXmRSSr_RA4G7lakuItYxqixYPy5B__Wfpww8=', start_index=14091)
Annotation(end_index=14812, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAqHprePWNckVp-EhNnG-xE36U3qeqUqjwrK36Akc_FGPvP3xVezPzdrSSbZGTNwmNvDGn9diqRnAY0338RqIIMjzSLD2ymvWZKN6u5vK6xVkS4fivw1N7b9wUmF5A39mmG6LOh9qUB9EPmxTFdahYyqRjlx-gRJBKoCAm3YgmE4H4bbBmF6g63ARXpy8lPfmFdrveqgi5JA7vnFI1-LallI0rvPAkNjk=', start_index=14799)
Annotation(end_index=14812, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK9aSIXvLVK2WgZH2BSIDWcTVdyU8U08_hjY4vwQ5nItr5Wi8VkfTTDUpbYn_bJiOrngf9kOF3HTV1jTAegxhiXYQ5k1_SkJwXe5NSbM9oXxPD8U4BBg==', start_index=14799)
Annotation(end_index=15142, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEW0J3Lc73qD0cx2uQlk9eVsRYqfEEAQ9TWhOP22nvBTDrupXuQzXd1pd6xRIhRF85VTbaFzXuGJgFRqF7EE7QvPujIEj7yubSWiKoaovs_egcr8342vtBG_Y7CLEDSMfmg2rX__1Dx-iIzT7qskecQ3UioE_gmkWEkg60vTiL948N_xxtrfLqfk_A8X2HLeupthelOnWc1pckhlDc0Oxcv6GkJ4wdpfcB_-kDH63YQR5idC90jCvGxltbkw0cJAg==', start_index=15128)
Annotation(end_index=15142, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK9aSIXvLVK2WgZH2BSIDWcTVdyU8U08_hjY4vwQ5nItr5Wi8VkfTTDUpbYn_bJiOrngf9kOF3HTV1jTAegxhiXYQ5k1_SkJwXe5NSbM9oXxPD8U4BBg==', start_index=15128)
Annotation(end_index=15525, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbXntcz5871ww4lzDtNV6INd4JqI-FYqAuqmsKUUuYwlhaanTb6N-kWsouxyXcmHorxD6oz1MUxYuqz_STS98auUCBWa-0dN7lVin6aMLfjgKxYfvcG_i4LgZoVguMItRXVGaDVHZ1RnDq3WOCXxI=', start_index=15512)
Annotation(end_index=15525, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxrzLINQK8Q50wlrPJnj_5p8mbpYf4my-97-X9ibStMF-Y0vb8bycE1dhv9oNgAhnDeNoyilqMiNsy5HiIqSDDa_fADfTtO35kNJjLsrYKqF7yKFGOl6sUAyXG', start_index=15512)
Annotation(end_index=15876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEW0J3Lc73qD0cx2uQlk9eVsRYqfEEAQ9TWhOP22nvBTDrupXuQzXd1pd6xRIhRF85VTbaFzXuGJgFRqF7EE7QvPujIEj7yubSWiKoaovs_egcr8342vtBG_Y7CLEDSMfmg2rX__1Dx-iIzT7qskecQ3UioE_gmkWEkg60vTiL948N_xxtrfLqfk_A8X2HLeupthelOnWc1pckhlDc0Oxcv6GkJ4wdpfcB_-kDH63YQR5idC90jCvGxltbkw0cJAg==', start_index=15863)
Annotation(end_index=15876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAqHprePWNckVp-EhNnG-xE36U3qeqUqjwrK36Akc_FGPvP3xVezPzdrSSbZGTNwmNvDGn9diqRnAY0338RqIIMjzSLD2ymvWZKN6u5vK6xVkS4fivw1N7b9wUmF5A39mmG6LOh9qUB9EPmxTFdahYyqRjlx-gRJBKoCAm3YgmE4H4bbBmF6g63ARXpy8lPfmFdrveqgi5JA7vnFI1-LallI0rvPAkNjk=', start_index=15863)
Annotation(end_index=16316, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP6vYRXgCRwwI5dDgH4FcLyZCfL7yFjIrue_MaDW0lngQqZ1PV3Pcz96ELyc9-hXHFuebQl7GGE7XJVV5jMsWMRddaRETGtOIo8-z1cuuzJThNRLPyrBgWOYZw6eYC5cxWuqVVTydKBJNy7IsRWx61AUcAsxPhouUmvg0-zxwE0UWUOMIDUEefOMHfkhjZujUH-j9F_sPC', start_index=16302)
Annotation(end_index=16316, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtCtq98nAMgsdmY1m-rgzWUeayck6C5FA6QiUGgyHIbkDc8RlTNwkr-VxMXj4MzzmoaFUmSrmlS86ne6-1nPKsG9XqiB-5CzMByDmzV5eJHiOpT4-JXg==', start_index=16302)
Annotation(end_index=16481, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK9aSIXvLVK2WgZH2BSIDWcTVdyU8U08_hjY4vwQ5nItr5Wi8VkfTTDUpbYn_bJiOrngf9kOF3HTV1jTAegxhiXYQ5k1_SkJwXe5NSbM9oXxPD8U4BBg==', start_index=16471)
Annotation(end_index=16835, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMxJDUCSnooW8UFYhmc5XGvBO_ISGPaG8wc_PKMMuMkCJeBQkLneTrGmc4TGegN779UXVoImBK73_LcNONlrjNZS4M0CTKRvnILm5f9aGYhuVqMKuLLLq0s-nSYKfRJiLIFWXQ986StQDnuyEZSSsn0kUWHNeUBAVC6AyoCSrmHQcmEYnzrQvzyYsjdFWxE8i9jUGN_PWbBdHXjr_3XEE=', start_index=16821)
Annotation(end_index=16835, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7gW83sXuxdZraIH0AZshVwkTwG3ht67jSM_SVH-aJcAgpgLPo4WRfCXQru-VUeV3yxcSQxlQ_oe1QvMNYTYcv2WmJUkYrn7EPyJdxGgnkcPEStarNI696zn9Vs4VNgX7rVtTPBrHeHgFwbNiRX7WFfQqylQcdckUYpulMoph1DCXlfDGxrQJW70TWhFTuRDwLNv-G1vgdDWJpl4f2KCr6rJZGgqhRiuU=', start_index=16821)
Annotation(end_index=18146, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgGu6PUxDKqLXDFwsACHNuPSfY6hOyZJSPE5khLCI0p326aQAodqNkSMC_bS-izsFLsL1Skijo6kRgyB-kp8y7-Fnl0pGIS79olDxpyK526OhHV1G9Mxo6_ICS57c7VGEa2UJ1P3VLWvwlLJ16frVrdeZ2i1TYzNF7VHsir0CpdFZyVIpr0jOKuW_tw8MLQkOVtOWa9QlW3MR_OK92_rW-oB1HNA==', start_index=18137)
Annotation(end_index=18223, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMxJDUCSnooW8UFYhmc5XGvBO_ISGPaG8wc_PKMMuMkCJeBQkLneTrGmc4TGegN779UXVoImBK73_LcNONlrjNZS4M0CTKRvnILm5f9aGYhuVqMKuLLLq0s-nSYKfRJiLIFWXQ986StQDnuyEZSSsn0kUWHNeUBAVC6AyoCSrmHQcmEYnzrQvzyYsjdFWxE8i9jUGN_PWbBdHXjr_3XEE=', start_index=18213)
Annotation(end_index=18304, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnn9pdnQWZ2rVm24Xwh37A-c8pjEISLDu7l7h8NH2rppXGWTbvKIXD3wDDXnBY058Yl8iLxc2b99Gb-pnt0nMWiLBSOxzzQm_t2j1TyXAQsBCF-JwhU_4rs8ieSFI5Y-JfruNfjdkceR5HZNdy44Ebs3FXy7aj966almQk3DDIVb1jWYQABTs=', start_index=18295)
Annotation(end_index=18371, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG40Nbd53Bu5nWBmJvS3UifRHwlOYFW2xdZreOAI8RjsbDpgNmthcuoAAfw8AcmjY4nJC400eMbZfPSaR2jwBP73W3SPP0F0h2aQsU4ebCWxlH7AqqccI4IAFYLQ27ok2kqQtMga3wVJ5q7ATbfDlDFGJXKcs3xt98WHaPh6vk4SiJQ4WGu4kLxUADh1A==', start_index=18362)
Annotation(end_index=18423, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoHRufLI8ctA4ePvQ6n3zPKHDAuxgoqQAXIMCAB1XRj4FpRN8af-RUDhG5EQ69QiKtW31pmHxTpTp_oJralpYQj4TvdwgQVGkXmRSSr_RA4G7lakuItYxqixYPy5B__Wfpww8=', start_index=18414)
Annotation(end_index=18481, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgv-_Wphkc4L9Hicih1wNAbJOTAOri7CCG1pWJz1pfHpr9bccWbL5m8ArrYS7TJgRx-mUA5w0x48rE70PwaESdr51fFpYounQ-1hiXMaY_mRc7ZDs-9si3PYSa59zWkvNJldg6XJ2laA==', start_index=18472)
Annotation(end_index=18541, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxrzLINQK8Q50wlrPJnj_5p8mbpYf4my-97-X9ibStMF-Y0vb8bycE1dhv9oNgAhnDeNoyilqMiNsy5HiIqSDDa_fADfTtO35kNJjLsrYKqF7yKFGOl6sUAyXG', start_index=18532)
Annotation(end_index=18594, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAqHprePWNckVp-EhNnG-xE36U3qeqUqjwrK36Akc_FGPvP3xVezPzdrSSbZGTNwmNvDGn9diqRnAY0338RqIIMjzSLD2ymvWZKN6u5vK6xVkS4fivw1N7b9wUmF5A39mmG6LOh9qUB9EPmxTFdahYyqRjlx-gRJBKoCAm3YgmE4H4bbBmF6g63ARXpy8lPfmFdrveqgi5JA7vnFI1-LallI0rvPAkNjk=', start_index=18585)
Annotation(end_index=18672, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9VRHtmBkRh5bfPO81VE10DlXnu2PCdsfEJtm_4Wvv0F285P0LM6RaGmvwwLvtNyUz2sYZNvT59xJop3l-gK7tpdsNZrg2NvcB_1uGn7mkL1R0zILpzvVCsTk_yh82RK7onEiYmqkx5b3E', start_index=18662)
Annotation(end_index=18738, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMQVUvZnuDzkFCFgGLXxTWnw__7Kban3u9eTYTrqiFWiUFd2VJL0y7Tf9DqW9_Aj5lLUDFFe_zVdm9AQUBoW_25l1i2X2mVzUMGiX0Eu8RzL6JacdblgzDArWfEQxYbIBvBpf5Mq0YJQdKC33lssWNjJEh1Oat3h1ULXNbAvSinA==', start_index=18728)
Annotation(end_index=18763, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHDhwEWvClTuHmMHlIVYlNViZEjJHncod0gGqsnMWWFOrE7w0PV0zxiXAaQXHwWtT5Pe4ttMLw5NrRydokUMV6oUx418n2S6sW6bJ6UzF-qV92xj3T-qGFaiCeBh_kpcbnAV7VIg-J4UUrFBKowOSLrJmOENn-JU1yVUCA_wJwTEe1SDok80BTaRhv1gY_ZOsD4BgWqUiIorTf1iPYRs1qfOx3dDE=', start_index=18753)
Annotation(end_index=18835, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgVGeOpocpnKC5DMdLPB3kAjSeL4cPmK86ykIlqw8GZzVJj29Me8NwZDo7--GmAiWAzRTE6BQtiospxFe_ORj5bY83EWSAsOpG02e-5ITzG3waFvUZ9TuZqQ==', start_index=18825)
Annotation(end_index=18893, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmNE4BG_0D0o_TtLY4TW0URpXdP4x2kfPSZWuuhpfwyYyDYa1-MnirIOf95vkzhwpfHnBj57rOPHyYHEtYWSeDDvzugOTI2h1NK5pfAqYl30FZSnnO16RtxZHZ9GpBdYQFnFMQw1WEJBZJU-LF5dh_PpA6ji1VUX1ycNIznQsXFGNNI7b1ucqQNVsiqX8o6dCaEv994O7gLPYoKbAlsYKw9RSjhwarFA==', start_index=18883)
Annotation(end_index=18956, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvUanjK81M7MVa_I8fSFPqkfVvBFmIvSqWRfYS1UACfFxtXb7GFMntaII5vnsvDGvxcgY-s63mVLKe_2A7NPwR4Z8CNTeffwjyvJc5CSDOnXL-asoR-D8yl0QOYM4Xag==', start_index=18946)
Annotation(end_index=19002, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGq4CTbeyaKLU9UriQpOso3LKwX5_s7wkw49YMUcGxKi-Bgz4dzGDIHMxBR8SUuoIoTzYqmdWNqt4KP1Q7piFudo1RHwuPE1Oyax4ZBBdKgsKQ1WpgODQ==', start_index=18992)
Annotation(end_index=19048, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK9aSIXvLVK2WgZH2BSIDWcTVdyU8U08_hjY4vwQ5nItr5Wi8VkfTTDUpbYn_bJiOrngf9kOF3HTV1jTAegxhiXYQ5k1_SkJwXe5NSbM9oXxPD8U4BBg==', start_index=19038)
Annotation(end_index=19115, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEW0J3Lc73qD0cx2uQlk9eVsRYqfEEAQ9TWhOP22nvBTDrupXuQzXd1pd6xRIhRF85VTbaFzXuGJgFRqF7EE7QvPujIEj7yubSWiKoaovs_egcr8342vtBG_Y7CLEDSMfmg2rX__1Dx-iIzT7qskecQ3UioE_gmkWEkg60vTiL948N_xxtrfLqfk_A8X2HLeupthelOnWc1pckhlDc0Oxcv6GkJ4wdpfcB_-kDH63YQR5idC90jCvGxltbkw0cJAg==', start_index=19105)
Annotation(end_index=19190, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbXntcz5871ww4lzDtNV6INd4JqI-FYqAuqmsKUUuYwlhaanTb6N-kWsouxyXcmHorxD6oz1MUxYuqz_STS98auUCBWa-0dN7lVin6aMLfjgKxYfvcG_i4LgZoVguMItRXVGaDVHZ1RnDq3WOCXxI=', start_index=19180)
Annotation(end_index=19232, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEo9KG_o2E0BJUsCWm_9ZCZmPnIGHobKbnzNRZ4grjEMI62j0JbxQIrPl_X1DzerBe1xtAyPhB0U8JeLFpkkKDTyyRnGmQ17xkeztIbGsy5eGfowPrxtQ==', start_index=19222)
Annotation(end_index=19273, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmkO3DGcmJj6vnNjo1jyLydxB0PZYQucb2DZ6n7ezzGDshhPDpmAEi_N_M6No0x7U0omZGqHbvVve2drlcFdEaj2JuEVDaGK5REOd2kWnG5RWZxtIkQY_w1P3fZRzUglEuDuTmqubvwC8pVqeryUjaP_M_xtk1-te9P_Mc6TRyWTd-HhipF6_pEDZkRFoTNArmlWXM9eXR0I0SREoK0LPAIzk4DKkeQsy4CpPyxPQUjqg-7BgE', start_index=19263)
Annotation(end_index=19312, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpg3kGKrFRQD-0sGqdsMGTvLjLYNKEE93sWZUrzmdGB_NAxI1NbEQ4t6RrNrqjeWne7M_jtHmCN3NQPLdhUyiTLF-3tiTgdxqYfwNqFGilUi0i1xPp9tJNacA-SCtsvEP6zhZtgURPtZWfKjteJAZ-sXN3YExfSB8O__flMe_AFCthfwK_-_D9_SI72T5eEBGj3A==', start_index=19302)
Annotation(end_index=19361, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuzo_ZQgPf-_qW-AvFKYfZqZQIE4V8kUt4RTozkNjgpDnrYZqnfvBGjkcjKTuseqVUg1EYCd1z_klU0hRxdYv2a362a1I2AfZVYIk7CDTeOUzkjwpmdhMFl_W3yoqE0H992cToPdTYBt0P5Q==', start_index=19351)
Annotation(end_index=19400, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFI5Q4YBKX6j1jRJHNf8U-ru8Rji4DmKt0KEOkycQ0O0rXjNhZByXHN26HIL0VEhjrjTiR2fMlTe19mgeB_snlcr3PJQi7fdG63f741DdCBJt_Jb5Oma9RkM_rxXlDL', start_index=19391)
Annotation(end_index=19434, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6C6Xq7KLYAV_xx97s84Bk_VVLpMtOPEs9ERbd6PgPcnIee1U0Or1DfKS9R4VaJ9Vs6Ww09fdKTOKbuYDS5YDtTLwnruykQcAA4Tjea1OhV7sQ0moo-awhyEv5EsdgXhqd1tk1ODuB1TR6tFZrkjaEWdzVOLmr3f2cVfzJDSLomBdZNjIon8MUAovUWhs-zm7c', start_index=19424)
Annotation(end_index=19476, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtCtq98nAMgsdmY1m-rgzWUeayck6C5FA6QiUGgyHIbkDc8RlTNwkr-VxMXj4MzzmoaFUmSrmlS86ne6-1nPKsG9XqiB-5CzMByDmzV5eJHiOpT4-JXg==', start_index=19466)
Annotation(end_index=19536, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuCF1jCUtHsDbMzeGAgIg3PKlo-hdAxuKuyqOEdrFEpsXwkkCjJ5PpK3X4USHL5qUmlIBf-DVFCpgLrVsXef9wI4gxQOfEZODghVYefPEOLXoazePuixdwHZBd_FRbGOGFkE3FsJEM9xoosEjy_GkInEK4ro6o6KhMko0UJWQSuPpaT52CqheC59PrYA==', start_index=19527)
Annotation(end_index=19581, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfd0IdjCVSl5aw4KEFC6wbxf_AAgwQBOhyP0GxWAKa57W4jpk9ieRV2BoEYU6lb9OZn8tQhwUZ5wKp8logs8fboMwWp2Ps3nmpLzZlpTtwX9FJBZ78RT4GK0C27Qvqev_I1sFMR7CJQvjS8RMy8DVlH5qwcfsNABZUnycllw==', start_index=19571)
Annotation(end_index=19614, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaU3yGaF89eLUO9qqtpHf5Ft_KPb5CkFRYfocil6HrdkgXaaDNbABzRCZASNgD5URwr-mj6A0yxPgdZKJbdbQhk8ljQnyFlFwSt00_q4-2-7EKJlk6CbEomt_y-En-DHT9hkUbYHPEnztjhGqhUc-bHlc2QpHe6QvMSPtJFOetuCHhK0KMwdjsjxAzR026nr64XZN7igXJ1IY=', start_index=19604)
Annotation(end_index=19656, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTbwIsf7TH_mzcE6Ak3BIxbkhuXG39k3zh88r74Y419IoVtXWzVNfDVNO76zyq3DAKIfj465tTPsvCsQPKo-EbMCdPj04TUdhiWz67YkVQ7WqUdE6RyFbV58ihy_Y=', start_index=19646)
Annotation(end_index=19706, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEW0J3Lc73qD0cx2uQlk9eVsRYqfEEAQ9TWhOP22nvBTDrupXuQzXd1pd6xRIhRF85VTbaFzXuGJgFRqF7EE7QvPujIEj7yubSWiKoaovs_egcr8342vtBG_Y7CLEDSMfmg2rX__1Dx-iIzT7qskecQ3UioE_gmkWEkg60vTiL948N_xxtrfLqfk_A8X2HLeupthelOnWc1pckhlDc0Oxcv6GkJ4wdpfcB_-kDH63YQR5idC90jCvGxltbkw0cJAg==', start_index=19696)
Annotation(end_index=19742, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK9aSIXvLVK2WgZH2BSIDWcTVdyU8U08_hjY4vwQ5nItr5Wi8VkfTTDUpbYn_bJiOrngf9kOF3HTV1jTAegxhiXYQ5k1_SkJwXe5NSbM9oXxPD8U4BBg==', start_index=19732)
Annotation(end_index=19769, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTHThXHskXh7zn5sWZoLHzpCk1TGcY7SZyRDU5IJhGlktaXB6TIvU_RdZneF680zFjFTbIIVD5ckmjp8LBZP5WQHJ-ag5V1OPr-yq-SAlaZlCDnZ5-nOQXHb4SEj0Sfza4KWTSSsSFxxRkD9gbfqLxe7hzVkHHlKGdofty45wKl0wypckXxiC-mU6DxK2cnybwaHUkKBrZutLNWsQulRgJ6DtJPEPUBc6EmA==', start_index=19759)
Annotation(end_index=19827, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7gW83sXuxdZraIH0AZshVwkTwG3ht67jSM_SVH-aJcAgpgLPo4WRfCXQru-VUeV3yxcSQxlQ_oe1QvMNYTYcv2WmJUkYrn7EPyJdxGgnkcPEStarNI696zn9Vs4VNgX7rVtTPBrHeHgFwbNiRX7WFfQqylQcdckUYpulMoph1DCXlfDGxrQJW70TWhFTuRDwLNv-G1vgdDWJpl4f2KCr6rJZGgqhRiuU=', start_index=19817)
Annotation(end_index=19878, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFo8ZAimSisdPMbIZlG4u09kZo7cYEH-b0cl61E7pKumFnmWmw2BkljOoMD8UjLaAjQzf4XD1xbBnMNpsbiaTERqMrOYKp46D7oAXe8O9nT6T31KnvN9u8UFdk=', start_index=19868)
Annotation(end_index=19902, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFW5wGuiKRfEyCVA9dLSwvzo7UESTyXhFik1xTmBpJoH-70OUduQ1u0fuyEdSh0boIF06eFMT32Os9kPdbMIGPNn4iW6o7XNMe2zbi8sfaTrSQq9yOiwH7BKs2hTfYvnHPq4Klyax14Cu84MxJ5g-52sd0hn4PGl-ZHNyY=', start_index=19892)
Annotation(end_index=19950, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUnEFyShg2e_7Oi8hY-wKCz9omVXsQAqgSKj8S46aFZRiQdIHjlIq7i_5Kh-kk3Mp7XP1K_LBxDhJpR3VwzIEzJkqxbM_1vHWzNw_wG8osqOpbEUZxvlD2TO5g3pjY9zJ0YM8lYNZJ_q4Au5NioFIPL__p97f1zIO0-Tnm0X_BFA-LqZojj-jLWpSObq3pwz8=', start_index=19940)
Annotation(end_index=19977, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDQIm-fXMXnZztz7O8N80yRLNbLCeXnusSQZGOeAylmjYFvU9MdWaMnS92Jz6l93g4yWTbj3NYHyn2ekDFoI0rMUp7p6dwpuJrZ02CYXyWWL3VMCfYFdoaM9AUSmQXGrfpxA==', start_index=19967)
Annotation(end_index=20008, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFaVmFv5Q6sY8OCkgFLm1Fcsc0jGh01Kr5BmU9wC_4RX-9lVw23XoPyRvNve4kkhY5yYwPcW7hUn-xKbVwGFDnlDROmRJoB2Sjf6XWkSx1HCHYwupNMVfUa8rPnU8hxskzOAWO_uhZ8XP_WDSB8Yu1TQqmsB68npgytnwJ-LOHMPA==', start_index=19998)
Annotation(end_index=20050, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsNx6T4LTd_kmxK643XjauSQeXbN1RjWUkPGITi1DOfv-BHg4iSPtVBQled6qhsNkkO8CDz7zH2oJcArgaOBu_9JqFhV4bPuyp2H3-H2H3XPWRYOE9RdrePyA24TqszIENKrbpzd8wTifICLD-yp09KNctrVjSWIxJFGdlfE2JhZVBUFDgvh4FCvUUzl3Bq5rfoc-PCWrOMHcDEuKS_0SG71y0PsDasg==', start_index=20040)
Annotation(end_index=20126, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyHQYqEPa4lSTYWm9PbCyiTkH7caqGackPghQufjEY7bB4YURt44Ufiz2vkS-c7-v-KQ9CstrYqxJxKv_u1RDgrmQlsy-zWoVCseN7IK2_WEHZZBNAZWlNl7hWYmmWHn3cqENqt3eH6tjffusrAit0wBxNqousLCL7n2hfoA==', start_index=20116)
Annotation(end_index=20172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEW0J3Lc73qD0cx2uQlk9eVsRYqfEEAQ9TWhOP22nvBTDrupXuQzXd1pd6xRIhRF85VTbaFzXuGJgFRqF7EE7QvPujIEj7yubSWiKoaovs_egcr8342vtBG_Y7CLEDSMfmg2rX__1Dx-iIzT7qskecQ3UioE_gmkWEkg60vTiL948N_xxtrfLqfk_A8X2HLeupthelOnWc1pckhlDc0Oxcv6GkJ4wdpfcB_-kDH63YQR5idC90jCvGxltbkw0cJAg==', start_index=20162)
Annotation(end_index=20203, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHj_kfJ8f58BT51drMz_NFbmfFaSpSLv3oe_KIaVczUJf-Ucx_zaCeiE5WbU2jxlTSanecSVaajXCXkYYqBfSPSlrjAWV56WNpGIGaW6EgNxr2i_1P_FRJ39RyZNNz12exGXv8xqVZwcoYpGiS3xBDeEV2wOsAHojOSaZIWSLQcnx4qkvgGh5s9BQ==', start_index=20193)
Annotation(end_index=20261, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK9aSIXvLVK2WgZH2BSIDWcTVdyU8U08_hjY4vwQ5nItr5Wi8VkfTTDUpbYn_bJiOrngf9kOF3HTV1jTAegxhiXYQ5k1_SkJwXe5NSbM9oXxPD8U4BBg==', start_index=20251)
Annotation(end_index=20300, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP6vYRXgCRwwI5dDgH4FcLyZCfL7yFjIrue_MaDW0lngQqZ1PV3Pcz96ELyc9-hXHFuebQl7GGE7XJVV5jMsWMRddaRETGtOIo8-z1cuuzJThNRLPyrBgWOYZw6eYC5cxWuqVVTydKBJNy7IsRWx61AUcAsxPhouUmvg0-zxwE0UWUOMIDUEefOMHfkhjZujUH-j9F_sPC', start_index=20290)

## Sources
