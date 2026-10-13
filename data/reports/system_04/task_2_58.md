# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** f77369a4 | **Time:** 297.88s | **Cost:** $1.27915
--------------------------------------------------------------------------------

# Balancing Partition Tolerance and Finality in Financial Blockchains: The Evolution from PBFT to Ebb-and-Flow Protocols

**Key Points**
*   **The Trade-off is Real:** Classical BFT protocols (like PBFT) prioritize **finality** (safety) over **partition tolerance** (availability). In the event of a network partition where more than 1/3 of nodes are disconnected, a BFT system will halt rather than fork, preserving the integrity of financial transactions but sacrificing liveness.
*   **PBFT View Change is a Bottleneck:** The view change mechanism in the original Practical Byzantine Fault Tolerance (PBFT) protocol significantly increases communication complexity, often reaching $O(N^3)$ or heavy $O(N^2)$ in worst-case scenarios. This limits scalability to roughly 100 nodes, making raw PBFT unsuitable for large-scale decentralized financial networks.
*   **Modern Solutions Exist:** Newer protocols like **HotStuff** and **Tendermint** have reduced view change complexity to linear $O(N)$, enabling better scalability without sacrificing BFT safety. HotStuff, in particular, introduces "optimistic responsiveness," allowing the network to recover as fast as latency permits without waiting for conservative timeouts.
*   **Hybrid Approaches (Ebb-and-Flow):** To balance partition tolerance and finality, "Ebb-and-Flow" protocols utilize a dual-ledger structure: a dynamically available ledger (like PoW) that keeps growing during partitions, and a finalized prefix ledger (BFT) that locks transactions when the network is stable. This resolves the availability-finality dilemma by offering different guarantees to different clients.

## 1. Introduction

The integration of blockchain technology into financial infrastructure necessitates a rigorous examination of consensus mechanisms, particularly regarding the trade-offs between **finality**—the guarantee that a transaction cannot be reversed—and **partition tolerance**—the ability of the system to continue operating despite network failures. Financial systems typically demand immediate or near-immediate settlement finality to prevent double-spending and ensure regulatory compliance. Consequently, Byzantine Fault Tolerant (BFT) consensus algorithms have become the standard for permissioned and consortium financial blockchains [cite: 1, 2].

However, the application of BFT in large-scale financial networks faces two critical hurdles: the **Availability-Finality Dilemma** inherent in the CAP theorem, and the **communication complexity** of the consensus protocols themselves. The user's query highlights a specific technical bottleneck: the **view change mechanism** in Practical Byzantine Fault Tolerance (PBFT). This mechanism, responsible for replacing a faulty leader, has historically imposed a communication overhead that scales poorly, threatening the viability of BFT in high-frequency financial environments [cite: 1, 3].

This report provides an exhaustive analysis of these challenges. It examines the mechanics of PBFT and its view change limitations, contrasts them with modern BFT variants like Tendermint and HotStuff that optimize communication complexity, and explores theoretical breakthroughs like **Flexible BFT** and **Ebb-and-Flow protocols** that attempt to reconcile the conflicting demands of partition tolerance and finality.

## 2. The Mechanics and Limitations of PBFT in Financial Contexts

Practical Byzantine Fault Tolerance (PBFT), introduced by Castro and Liskov in 1999, was the first algorithm to demonstrate that BFT consensus could be viable in asynchronous environments like the Internet [cite: 4, 5]. For financial blockchains, PBFT offers a distinct advantage over Proof-of-Work (PoW): it provides **deterministic finality**. Once a block is committed, it cannot be reorganized, unlike the probabilistic finality of Bitcoin where deep chain reorganizations remain a theoretical possibility [cite: 6, 7].

### 2.1. Normal Operation Complexity
In its normal operation (when the leader is honest and the network is stable), PBFT operates in a three-phase process: *Pre-prepare*, *Prepare*, and *Commit*.
1.  **Pre-prepare:** The primary (leader) broadcasts a request to all backups (replicas).
2.  **Prepare:** Replicas multicast their vote to all other replicas.
3.  **Commit:** Upon receiving $2f+1$ prepare messages, replicas multicast a commit message to all others.

This all-to-all communication pattern results in a message complexity of $O(N^2)$, where $N$ is the number of nodes. While manageable for small consortiums (e.g., 4 to 20 nodes), this quadratic growth becomes a severe bottleneck as the network scales. Research indicates that PBFT-based blockchains struggle to scale beyond 100 nodes because the sheer volume of messages saturates network bandwidth [cite: 3, 8]. For a global financial network requiring hundreds or thousands of validators, this baseline complexity is already problematic.

### 2.2. The View Change Bottleneck
The user specifically asks whether the PBFT view change mechanism increases communication complexity too much. The evidence suggests the answer is **yes**, particularly for the original implementation.

The view change is the safety valve of PBFT; it allows the network to elect a new leader if the current one fails or acts maliciously. However, to ensure safety (that no previously committed transactions are lost), the new leader must gather the state from a quorum of replicas to construct a "New-View" message.
*   **Complexity Surge:** In standard PBFT, the view change protocol can exhibit a communication complexity of **$O(N^3)$** in terms of bit complexity (total data transmitted) or a very heavy $O(N^2)$ depending on implementation nuances [cite: 3, 9]. This is because each replica sends its log of prepared messages to the new leader. The new leader must then broadcast this massive set of data (the "New-View" proof) to all other nodes to prove the legitimacy of the new view [cite: 10, 11].
*   **The "Hidden Lock" Problem:** A subtle issue in BFT view changes is ensuring that a new leader picks up any value that *might* have been committed by a previous leader. In PBFT, this requires exchanging extensive proof data, which creates a vulnerability. If the network is unstable, frequent view changes can trigger a "death spiral" where the bandwidth consumed by view change messages prevents the system from ever stabilizing, effectively halting the blockchain [cite: 11].

### 2.3. Scalability Implications for Finance
In financial blockchains, where latency equates to financial risk, the PBFT view change mechanism poses a critical stability risk. If a leader node in a banking consortium fails, the resulting view change could stall the network for seconds or minutes due to the message explosion.
*   **Throughput vs. Node Count:** Studies show that while PBFT offers high throughput in small clusters, its performance degrades exponentially as nodes are added [cite: 8, 12].
*   **Sybil Attacks:** The inability to scale node counts makes PBFT vulnerable to Sybil attacks if used in open networks, as the number of nodes must be kept artificially low to maintain performance [cite: 12].

## 3. The Availability-Finality Dilemma

The user's query asks if BFT can "balance" partition tolerance and finality. To answer this, we must invoke the CAP theorem and the FLP impossibility result, which govern distributed systems.

### 3.1. The CAP Theorem in Blockchain
The CAP theorem states that a distributed data store can only provide two of the following three guarantees: **Consistency** (Safety/Finality), **Availability** (Liveness), and **Partition Tolerance** [cite: 13, 14].
*   **Partition Tolerance (P):** In the context of a global financial blockchain, network partitions (where Europe cannot communicate with Asia, for example) are inevitable. Therefore, P is non-negotiable. The system must choose between C and A.
*   **BFT Favors Consistency (CP):** BFT protocols like PBFT, Tendermint, and HotStuff are designed to prioritize **Consistency**. If a partition occurs and a quorum ($2f+1$ nodes) cannot be formed, the system **halts**. It stops producing blocks. This ensures that no two conflicting ledgers (forks) can be created. For finance, this is often preferred; it is better to pause trading than to allow a double-spend [cite: 6, 15].
*   **PoW Favors Availability (AP):** Nakamoto Consensus (Bitcoin) prioritizes **Availability**. If the network partitions, both sides continue to produce blocks. When the partition heals, the shorter chain is discarded (reorg). This lacks "instant finality" and is generally considered risky for high-value interbank settlement [cite: 7, 14].

### 3.2. The "Halt" Behavior
In a BFT financial blockchain, "balancing" these properties is strictly limited by the $1/3$ fault tolerance threshold.
*   **Safety Threshold:** As long as $<1/3$ of nodes are faulty (or partitioned off), the system maintains both safety and liveness.
*   **Liveness Failure:** If $>1/3$ of nodes are partitioned, the system loses liveness (it halts) to preserve safety. It cannot "balance" this by allowing temporary operation, because doing so would risk a fork (violating finality) [cite: 16, 17].

Therefore, traditional BFT does *not* balance these in the sense of providing both simultaneously during a major failure; it explicitly sacrifices availability to guarantee finality.

## 4. Modern BFT: Solving the Complexity Problem

To address the user's concern about PBFT's communication complexity, researchers have developed modern BFT protocols that maintain the safety guarantees of PBFT while drastically reducing the overhead of view changes.

### 4.1. Tendermint: The Gossip-Based Approach
Tendermint (used in the Cosmos ecosystem) was one of the first major improvements over PBFT for blockchain use cases.
*   **Linear View Change:** Tendermint optimizes the view change (called "Round Change") to be **$O(N)$** in terms of message complexity. It achieves this by using a gossip protocol and a rotating leader schema where the leader changes every block [cite: 10].
*   **Trade-off:** While efficient, Tendermint introduces a mandatory delay ($\Delta$) after a view change to ensure safety. It is not "optimistically responsive," meaning it cannot run as fast as the network allows immediately after a leader switch; it must wait for the timeout to expire to ensure no other value was committed [cite: 11, 18].

### 4.2. HotStuff: Linearity and Responsiveness
HotStuff (the consensus behind Facebook's Libra/Diem and Aptos) represents the state-of-the-art in addressing the PBFT complexity issue.
*   **Linear Communication ($O(N)$):** HotStuff replaces the all-to-all mesh communication of PBFT with a star topology. Replicas send votes only to the leader, who aggregates them (using threshold signatures) and broadcasts a Quorum Certificate (QC). This reduces normal operation complexity to $O(N)$ [cite: 11, 18, 19].
*   **Linear View Change:** Crucially, HotStuff simplifies the view change to **$O(N)$**. The new leader does not need to collect massive logs from all replicas. Instead, the protocol adds a phase (3-chain commit rule) that allows the new leader to simply pick up from the highest QC it receives. This eliminates the $O(N^2)/O(N^3)$ bottleneck of PBFT [cite: 10, 18].
*   **Optimistic Responsiveness:** Unlike Tendermint, HotStuff does not require a fixed $\Delta$ delay. If the leader is honest and the network is fast, consensus proceeds immediately. This makes it highly suitable for financial blockchains requiring low latency [cite: 11, 18].

### 4.3. Comparison of BFT Protocols

| Feature | PBFT (Classical) | Tendermint | HotStuff |
| :--- | :--- | :--- | :--- |
| **Normal Complexity** | $O(N^2)$ (All-to-All) | $O(N)$ (Gossip) | $O(N)$ (Star/Leader) |
| **View Change Complexity** | $O(N^3)$ or heavy $O(N^2)$ | $O(N)$ | $O(N)$ |
| **Responsiveness** | Responsive | Non-Responsive (Wait $\Delta$) | Optimistically Responsive |
| **Leader Rotation** | Stable (until failure) | Rotating (every block) | Rotating (every block) |
| **Scalability Limit** | ~100 nodes | ~100s of nodes | ~1000s of nodes |

*Table Data Sources: [cite: 3, 10, 11]*

## 5. Bridging the Gap: Flexible BFT and Ebb-and-Flow

While HotStuff solves the *complexity* issue, the *partition tolerance vs. finality* issue remains. Recent theoretical advancements propose ways to "have it both ways" through hybrid architectures.

### 5.1. Flexible BFT
Proposed by Malkhi et al. (2019), Flexible BFT challenges the rigid $1/3$ threshold. It introduces a new fault model: **Alive-but-Corrupt (abc)** nodes.
*   **Concept:** It separates clients based on their assumptions. Conservative clients (requiring absolute safety) might wait for a higher threshold of votes, while optimistic clients might accept a lower threshold to proceed faster.
*   **Impact:** This allows a single ledger to support clients with different risk profiles. A financial institution might wait for the "finalized" confirmation (safe under partitions), while a retail user might accept a "speculative" confirmation (live but potentially reversible) [cite: 20, 21, 22].

### 5.2. Ebb-and-Flow Protocols (Snap-and-Chat)
This class of protocols, including the "Snap-and-Chat" construction, explicitly resolves the availability-finality dilemma by maintaining **two ledgers** simultaneously [cite: 23, 24, 25].
1.  **The Available Ledger:** This runs a dynamically available consensus (like PoW or a longest-chain PoS). It continues to grow even during severe network partitions, ensuring liveness.
2.  **The Finalized Ledger:** A BFT "gadget" (like HotStuff or Casper FFG) runs in the background, taking snapshots of the available ledger and "finalizing" them.
3.  **Resolution:** During a partition, the *Available Ledger* keeps growing (providing partition tolerance/availability), but the *Finalized Ledger* stops advancing (preserving safety). When the partition heals, the BFT gadget catches up and finalizes the accumulated blocks.
*   **Relevance to Finance:** This architecture is used in Ethereum (Gasper). It allows users to transact continuously (availability) while providing a checkpointing mechanism that eventually grants economic finality [cite: 23, 24].

## 6. Scalability Solutions Beyond Consensus Logic

Apart from algorithmic improvements like HotStuff, financial blockchains employ structural optimizations to mitigate PBFT's communication limits.

### 6.1. Hierarchical and Multi-Layer PBFT
To bypass the $N=100$ limit, researchers propose grouping nodes into layers.
*   **Mechanism:** Nodes are divided into local groups. Each group runs a local PBFT instance to reach consensus. The leaders of these groups then form a higher-level committee to run a global PBFT consensus [cite: 1, 3, 26].
*   **Result:** This reduces the global communication complexity significantly, allowing the network to scale to thousands of nodes while keeping the consensus latency within acceptable limits for financial transactions.

### 6.2. Sharding
Sharding partitions the state of the blockchain, so not every node processes every transaction.
*   **Trade-off:** While this increases throughput, it complicates the BFT model. Cross-shard transactions require atomic commit protocols (like Two-Phase Commit), which can re-introduce blocking behavior and reduce availability during partitions [cite: 3, 27].

## 7. Conclusion

The answer to the user's query is twofold:

1.  **Does the PBFT view change mechanism increase communication complexity too much?**
    **Yes.** In its original form, PBFT's view change is a scalability killer, imposing $O(N^3)$ or heavy $O(N^2)$ overhead that limits networks to roughly 100 nodes. This is unacceptable for large-scale financial infrastructure. However, this has been effectively solved by modern BFT variants like **HotStuff**, which achieves linear $O(N)$ view changes and optimistic responsiveness, making BFT viable for high-performance financial blockchains.

2.  **Can BFT consensus balance partition tolerance and finality?**
    **Strictly speaking, no; but practically, yes.** In a strict CAP theorem sense, BFT protocols prioritize Finality and must sacrifice Partition Tolerance (Availability) by halting during major network splits. They cannot "balance" this by remaining live *and* safe simultaneously during a partition. However, through **Ebb-and-Flow protocols** (like Ethereum's Gasper), financial blockchains can achieve a practical balance: offering a "live" ledger that continues operating during partitions, while a separate BFT mechanism provides "finality" whenever the network is stable. This dual-layer approach allows financial systems to maintain user uptime without compromising the ultimate settlement assurances required by global markets.

## 8. Detailed Analysis of Research Findings

### 8.1. The Evolution of View Change Complexity
The research explicitly highlights the progression of view change efficiency.
*   **PBFT (1999):** The view change involves exchanging `VIEW-CHANGE` and `NEW-VIEW` messages containing sets of prepared messages. As noted in [cite: 3], this exhaustive peer-to-peer communication is the primary reason PBFT hardly scales up to 100 nodes.
*   **SBFT (Scalable BFT):** Reduces the messaging complexity in the "linear path" to $O(N)$ using threshold signatures but falls back to $O(N^2)$ in worst-case scenarios [cite: 28].
*   **HotStuff (2019):** Achieves linearity ($O(N)$) in *both* normal execution and view change. It treats "New-View" messages as regular consensus messages, avoiding the extra cost of carrying historical baggage found in PBFT [cite: 18]. This is a critical enabler for financial blockchains like Aptos and the (now defunct) Libra project.

### 8.2. Financial Implications of Finality Gadgets
The adoption of "Finality Gadgets" (overlaying BFT on top of available chains) is the industry's response to the partition tolerance question.
*   **Ethereum's Approach:** Uses Casper FFG (a BFT gadget) over LMD-GHOST (a fork-choice rule). This allows the chain to be "available" (users can post transactions) even if finality stops. For a financial application, this means a bank might see a transaction as "confirmed" (on the available chain) but not yet "finalized" (settled). The bank can then choose its risk tolerance: accept the confirmed transaction immediately (high risk of reorg) or wait for finality (zero risk, potential delay) [cite: 23, 24].
*   **Regulatory View:** Regulators typically require deterministic finality. Therefore, while Ebb-and-Flow protocols offer availability, institutional financial layers often rely strictly on the BFT finalized prefix, effectively treating the system as CP (Consistent/Partition-tolerant) and ignoring the "available" tip during instability [cite: 2, 29].

### 8.3. Future Directions
Research suggests that future financial blockchains will likely utilize **Hierarchical BFT** [cite: 1] or **Flexible BFT** [cite: 20] to customize these trade-offs. By allowing different nodes to have different "quorum" definitions (Flexible BFT), a domestic retail payment might settle with lower security thresholds (higher availability) than a cross-border interbank transfer (requiring absolute finality).

In summary, while the original PBFT is too heavy and rigid for modern financial needs, the family of BFT protocols has evolved to offer linear scalability and hybrid availability models that effectively resolve the historical bottlenecks.

## References
[cite: 1] *PBFT view change scalability issues financial blockchains* [cite: 1]
[cite: 3] *A scalable multi-layer PBFT consensus for blockchain* [cite: 3]
[cite: 16] *Consensus mechanism fBFT+PoS for blockchain scalability* [cite: 16]
[cite: 4] *Modern BFT consensus for financial blockchains view change complexity* [cite: 4]
[cite: 29] *BFT consensus in 2024* [cite: 29]
[cite: 6] *What is the difference between normal Byzantine Fault Tolerance and...* [cite: 6]
[cite: 17] *The Role of BFT in Blockchain* [cite: 17]
[cite: 2] *Blockchain Fundamentals: Key Consensus Algorithms* [cite: 2]
[cite: 7] *Consensus Algorithms: PoA, IBFT or Raft?* [cite: 7]
[cite: 5] *Balancing partition tolerance and finality in BFT consensus* [cite: 5]
[cite: 28] *SBFT: a scalable and decentralized trust infrastructure* [cite: 28]
[cite: 13] *A cursory introduction to Byzantine Fault Tolerance and alternative consensus* [cite: 13]
[cite: 26] *Double-layer PBFT-based consensus mechanism* [cite: 26]
[cite: 12] *Practical Byzantine Fault Tolerance (pBFT)* [cite: 12]
[cite: 15] *Tendermint: Consensus without Mining* [cite: 15]
[cite: 30] *What is Tendermint?* [cite: 30]
[cite: 14] *Single Slot Finality* [cite: 14]
[cite: 10] *What is the difference between PBFT, Tendermint, SBFT, and HotStuff?* [cite: 10]
[cite: 18] *HotStuff vs PBFT view change complexity* [cite: 18]
[cite: 31] *NEC FastBFT* [cite: 31]
[cite: 24] *Ebb-and-flow protocols* [cite: 24]
[cite: 27] *Flexible BFT consensus partition tolerance finality balance* [cite: 27]
[cite: 23] *Ebb-and-Flow Protocols: A Resolution of the Availability-Finality Dilemma* [cite: 23]
[cite: 24] *Ebb-and-flow protocols topic* [cite: 24]
[cite: 25] *Ebb-and-Flow Protocols Paper* [cite: 25]
[cite: 11] *HotStuff BFT consensus in lens of blockchain* [cite: 11]
[cite: 10] *Tendermint vs HotStuff view change complexity* [cite: 10]
[cite: 18] *HotStuff consensus view change complexity linear O(N)* [cite: 18]
[cite: 19] *HotStuff-1* [cite: 19]
[cite: 3] *PBFT view change communication complexity O(N^2) scalability* [cite: 3]
[cite: 20] *Flexible BFT consensus mechanism two layers* [cite: 20]
[cite: 21] *Byzantine Fault Tolerance Meets Flexibility* [cite: 21]
[cite: 22] *Flexible BFT Blog* [cite: 22]
[cite: 8] *PBFT consensus scalability limit 100 nodes* [cite: 8]
[cite: 32] *Scalable multi-layer PBFT* [cite: 32]
[cite: 9] *An introduction to PBFT consensus algorithm* [cite: 9]

**Sources:**
1. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5F4H5D0NMboJpuq_xx5-sW2-iLwDHTx0UYzaB9ujjNa8Eh-ZSiP0KBDI-gmyFUWqnjNToTvmRAmRfVlbWr8ABhos3fRKBQyWMwBcjhWlHzvcQdtc5xeOU9EN6Ds0=)
2. [certik.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWEuLbIMeCvmPLZY5S6Kynau0SoDegzhoLVM5O_mfq9Zn4y2BqlCBVvR699OmZmZSJ9Wlv8HQCmaywr0iWgyir8yIddmugftWdZZ9Cp6uTPMpgSRY9sCcmtNNVfc33UQjknF7r8Za2lOtPHUKbgOldnYSibIWp0cMTj55luMfCQ-G9VL57FSULvXnC2g==)
3. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETo_hf0jcwLi2cKLpibCYsvkJtauR6qrj-bZke51v48tXM26Gkc2aHEdvCb4-DSSOE-tbF4SbwXOKJVZfS24GRK_-LnSX0FCyHP7GDdUb-d55btLLpJgcIg-q6P3ZqLMFPC3F0pkDJ__LePmnADK6AIpwfVPKx8OqsMa-QkJKD1wnydLGBriAMtqx_uJiCpBamtQ==)
4. [sciengine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTQa6dyh7HI1gG3KBfDTZUb5aGYU7reHiWVc1jKj2vmP4yoUDPwNP1AgNpNovfQhkgTOanKYmC_fTjkdT3-BnOTdORZwuMlT75iNJ2GKWWbCsRJKlKO7Wp-mZ6R1Dr_86-UR30OldtPEp6oOAj)
5. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp_hs4SUxqMUds1geAhNY26GE15SUCgsEh0uWBzSjqGbf-5iXLsFemHzC0YQH2oTirHj70gb0wQFCbBqGGlQCAhh_YV1V5xGOxDASjhFihf_On-i-tCZcExvTbZJA=)
6. [reddit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBsLnRDSLKmUPOYw7FyFtDCcLHN_B2b5pNjgxzxDEM8JLYaIkkPxdQ7tt6AO6PGd3Wb1M4Ig1bH_ybAugRUWXeK2tGuw9YEvQIErHnmLf7EMm3eb35qRCOeoAfNRka-vArbjksKByjfbf500jgUXgVh7TxhqDPcCHuCo81y0xnJphmGH9H5BJBLVPaEDgFbQdvyJ0VzibMqhXFw_v59iqX)
7. [kaleido.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0TJiQH7rjAs3vHKx1jf563Tp2vIhSLYsucdKEOWl07iwQrdyan10Zev5jiqtvqjzSl1Q5ny-nyWb5gxm9SO9VwhxK-bnF97cfqp5DsA6FD80JXaaauaya6Abnyk4N2dc9TmN0Em-F9AKoGfztGUJ6PYTZLxRDbml10MhgvKA5SyoI)
8. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWIFyuaNv3KBRM_3zQc3tfxqzNxbyJEseWj56FTUfsxqgf2YATSOM67nUy8ka-WQEY3g_8E_fI48jocWZCVtUhbVEVP9MJY-kOKUnU5w8s3eKFOODBD9FxjB_d)
9. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAqtNI3WBsdawx2aCnITDujBUJ--lOtlYCs2sVfGN9pPSzAkOc8C_9T4tdtAxstvoLJJy-ziXjcIKAbmUIqeXWx6AD6csiYB7yap8OAkBsl9ee747qHnEqdKvlXuqYs2SGlc3zRy4WoB1wnIHtMJ02huzh_ec3lW_Jzvb_JDoBB6TMOSMt_kS_CIm8VQ==)
10. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzFKCIg6E0b6AS7xfSfIZu7PfZoH8ShmXwHEbl3fPvt9ldGCDVHBBoX6dm_JnAIIXoXMI7om8TSymbh1tn9iRTurn2DqQMvEF_oa0PQBedP3rt63AAnaIzsw8a72JZ2osTvLZzLZMHbiKH4lWZNHKD3DAN2lhAZS8TwqBTV3Vy7LR_ad1-9GYY)
11. [blogspot.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ5x1XDrUXr7hG70ilu3oxu2TFxIb_caPjVTwdI5JObqK4Aj3PsB2sBy3_utzRGQqqFaifmTo6tGVmRBHvOS5gVArvkXwkdekvKySDniuQOcfQ9wPcjIUiCcFSsyB3G4ixyWGctFZpoA2oiNWJD4sYe8OtCtxYvlb9UkiU7uROqW7Z1fu8)
12. [geeksforgeeks.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqncnu3YomUyHjX6KJ9YuOwPMCLdt31lUDWTBLx5EDQ0q5m9y7uM2eaXXlQIxD52mUt9pmlYYtnohqAKDR1Km5jlUplcBHsSwUtm12d3siEDZqtKfwiAPrb1Kh5OI0IepKZnJEeCzj8WUif_eRs0ZeV1iGPDpBohigpvRUR3c6Wt62L1MgDjFcKq_YsvHM)
13. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEx0HgOuxEuvkkN4UaHvcectl-CmXZj23vXLI7xfRQ91L0wDxzhuhPUf4-oCQlPFm5xb1D31es_n0hkMSryIe9c0s_2dBQCn0Q2xIatIXAB5BDl3VRqjqKeMulvQt2PGWdPxJ5KeEyIms8H-2byzsDwZG3Wvipx3bk8Tejz08Cvi_lKTjr9zsWoqlUMiyWoVKWXQ1TlpmXDQt805pMjhJw4oDEaORWhbFY8aqFfw==)
14. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTeNv6qUmqnq8sHkGYGFriG5zvToo25a_sU3hrDyRi7htpUIM2s8tZxQsnBo1FpxNoPtmhMfjWnFVbwg9FiTZmi_MBHSwXMS2I9ZGfs_rNnW7Ahm0OJQ==)
15. [epfl.ch](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbUMUME6MvhR1aiGLr_ihVYVyccOX37fP_5vd1ikiezIljXfVxC6h1ba3yIm37k5ZYygQTTGvOi6R8wk-j4RrpCTsXOyKkrqcauBYih9bL0uqko8rFNLkHRP8pf_qk0PuGydqlF3Z9xZmUCLdE_S00Q06l2hUSjSLkEzJJelZv79ClK466cMGpWPY=)
16. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR09ZYgKicW7P9Hy6DPx4z6JcZ64a0bkw05t2LjHrU-RWFDep_VmRq4oxfw0gwMF2g7KxzdvjilIzF6_MP9qeQUbTu9es6y8Lzb5gk8rKRYQMnd0q8g-AlvIyQV2MsDpsFrSxnXVOSmxRLBKYf9rmSsNf5h6MifVVp9VbF0q2hdbOuw8GIi5iGPoZl6N3y9Bq7PmudmQnrvOCNBL0FOliO)
17. [nervos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEY45Arx-jQr6eor2KqviIPHyEtHA8rF0x3xovz4ylbAy0UHxDlbQ8p07ncgV_h_4j914J4Jzq-OEHv8SD3qRbFZRDnth1OtjkGq89kQJ0RwQHBEVZ12lzHt23lE6nlpxzlZqcGrBiNxC2xSFBKBOy9OnzkaVAMz3trowAkxb8BOeefog==)
18. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_C4Q3NnOp48IZ4H2pAj1oF0UhByiD24DGKpke-RGjAj01CJPX95CasOa4r6B7tyipOjnKfB6EEKlnokCq-apRBdOtTtbRowli5XAi8W7dJlrC2ZJvaII7ug==)
19. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn3n3cmDNENDP64m57rQWaveYh-pfmBtgsGQiAc1ptVzTh1a3FUjCHI37_XjuzIwrxxjq9cnRH5uHcu-9kMRoyXyELIBHoM_8otfVKwB-2DnkykOthFM8A_Cloer3uYsVkhQ0MxEccuW8hHZsCh1numoxo)
20. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8U5E1tA7giSBYLAJpBxI14tGMeC55x5uk2rNnrEuAxfmR1U9v9ZR-SbolGD2fTKhjhCVqpQCnhh2BQmAcvhlwQeYnQFiqrk2ZaRnAAmrD0bP0GGR2Gw==)
21. [berkeley.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9BHgX0QmAahoU38SrOk1HZK2h1N7RegPu0upfS3tbdXeOGiu6PWRYj13PJJEziaBxClwvtl9zro4-y0O2CLz6zv5w3flQ-UstAwSGw0bgwMuG4GFNgtcb6bdN34Yoq-m2XCIHgVygba_7FlCSsIti2mQcdihEOp9-ulP4mjqc0hSxeaXhGzfzWU6iOx1MR9wwFZu7okx14P3OBUfKCV8EAIBsYu32_Wew)
22. [malkhi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6LRSahn0GFBWpBSYOc7FXirRe64jTVGVFxzo3-s4ydciRDrLak9btSyM45vX39QSVodic158aSKQMDstHcSrZVT9al5fN6XilO1qwaCF8FGhtZTJZhAmfFnmjx3CDt7g53eo=)
23. [snu.ac.kr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiYIT4biX_xZAHPV687UWe6PXtzG9s7Gmm0K03d7E97rZFxEA3uss6h_iTmomIeXB3XLY5Fp-Cv6JnJSou50r0Qd1g6OEVmxXOuw81l9k3J0c3jzZdSjbdKMpFeBrDaCAwCTwdmnusVOxylqletNx5aS_4dNPHNCmDaoO2VddPmrN2-dxg7z41RCvHhHNZax-wW8tajQSURg58PvBTNZX7RNAqNmfhqLsrlsbOH_Bwch9SbM9NGieFfddfwaX-WvMtW-RP2F-Iiavv9xYI)
24. [emergentmind.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEltEoUvKnz8ZJQ2L7lTu7T6__4I0GpnYgVhYUheig3arhoH-373VYyIJqAHvxMRN0sdaQpHCME3vTzX1eMCZbuPS2RhIsNTSFjKI5WgDaM7lLjxV8H2r90AP8ZqWS9p8omdSYwxrEBMwsWnJYkDBK)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVmx8_7ZxTfFqQ12J5dgmCOwtvsfRR7yUw5UiUmYNqZb6dgWfeZyA5jG6NpmDcB1_C64hmZ_S3T0_sBCz8gYC08xPvmPogbXGsxWwROe9CroHX4v0W1AGV-2xHbGHCJfYqcdkIgZj63zBOQhbrJ129RpwFOoFmaY4lbQPUv0PdWsIdtTs93Ye7BRjLhVoEnKzapVeUuzYJf7BfXDsfs2QndamJMQLq56IYJ6xuZLb5pQI=)
26. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyIgoTRwto-X65C7rywBDczkr7jyUxO8dNwzy4nLSWDWvhwWk-q8q09Bg4LMyx1p67dyDfFqp9s0gx-Q-DU25uinWKyykzGwuGODOMEUGvyfhjRXEEcxSXyDA_f8tuojVRfg==)
27. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgCNNQcBprdGb20iR6qCkdKOQp_ROSyB0kS8YKavxEM78nYzcDK-382FjkcjxLUcadWfS-8WWCe1_yC5wU_4XVrw9Myc7sgXRwAcPKowAUYwDxHJyCjnG3MA==)
28. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpKVOLWKKBSOS7ROXUnEbROoHxBPktODELYpos5RIn203pD2zCRXIxpC_Iqwp_HPHjw0inwKNJ09blkVzTcTbk8fuhmN4znQYGSzxM-p_OUXjxy1ynVRC7JA==)
29. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHADKjsTfWK5AcCY48v-0fJFgzD0IlgCSPTpQ_tcsLxwxmGpFl_9YIEEV4SBIz_nV__iMlfDu39o7eukOIVWjKHsQCoVZr-j9H3IbT5Q3SEd8ZCXNDNQzX0s5xLSAek6kWyjomiiTLr8nkeTfBzID7eOlRr)
30. [tendermint.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuSVgO3x_NC97BOTvJeaMNyWkC92ArRqYYTF68Q1Kvn9y_m3cu0ud3GWzkacOC7tGStWvkS43RcE-KrdNawILeR73kJ0IirPdToD93RhrYfwLhPhKuHs0ZwmiP1B0j03kCQwqhTKw0HFVhVOZjd2CzxRLP4i-ANy2oOl0eoQ==)
31. [nec.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbGG2ryIn-fQnISp-IMh1TyiM6GR-p_PSe66CUfFph0hYURzrT-fqpwlKnZqn-QND53qMvkVVFGvN2Fl6JWdkwaI6cVNjLb7FWiHKmsbQwr7UfIEE74iC04or4M2D3U5Oul3eTEIeUGMS0MWdZl9B4nYnOnlqfLPQxxw==)
32. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEA1LgS-0pcXBxMbVSJltPWqR55d3KAEDYIfm7TEufdliod3IPzQeQvZ3vvrF6lyQW3yY20yJ2B0BRixwIdIQ5rD8Cf8GxRWcf9A7uhG_5zge1TsMAeKLLe-uS4VGFkoToFpvYptgYTAMQ_mZSplw==)


## Annotations
Annotation(end_index=2314, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWEuLbIMeCvmPLZY5S6Kynau0SoDegzhoLVM5O_mfq9Zn4y2BqlCBVvR699OmZmZSJ9Wlv8HQCmaywr0iWgyir8yIddmugftWdZZ9Cp6uTPMpgSRY9sCcmtNNVfc33UQjknF7r8Za2lOtPHUKbgOldnYSibIWp0cMTj55luMfCQ-G9VL57FSULvXnC2g==', start_index=2302)
Annotation(end_index=2314, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5F4H5D0NMboJpuq_xx5-sW2-iLwDHTx0UYzaB9ujjNa8Eh-ZSiP0KBDI-gmyFUWqnjNToTvmRAmRfVlbWr8ABhos3fRKBQyWMwBcjhWlHzvcQdtc5xeOU9EN6Ds0=', start_index=2302)
Annotation(end_index=2907, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETo_hf0jcwLi2cKLpibCYsvkJtauR6qrj-bZke51v48tXM26Gkc2aHEdvCb4-DSSOE-tbF4SbwXOKJVZfS24GRK_-LnSX0FCyHP7GDdUb-d55btLLpJgcIg-q6P3ZqLMFPC3F0pkDJ__LePmnADK6AIpwfVPKx8OqsMa-QkJKD1wnydLGBriAMtqx_uJiCpBamtQ==', start_index=2895)
Annotation(end_index=2907, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5F4H5D0NMboJpuq_xx5-sW2-iLwDHTx0UYzaB9ujjNa8Eh-ZSiP0KBDI-gmyFUWqnjNToTvmRAmRfVlbWr8ABhos3fRKBQyWMwBcjhWlHzvcQdtc5xeOU9EN6Ds0=', start_index=2895)
Annotation(end_index=3616, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp_hs4SUxqMUds1geAhNY26GE15SUCgsEh0uWBzSjqGbf-5iXLsFemHzC0YQH2oTirHj70gb0wQFCbBqGGlQCAhh_YV1V5xGOxDASjhFihf_On-i-tCZcExvTbZJA=', start_index=3604)
Annotation(end_index=3616, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTQa6dyh7HI1gG3KBfDTZUb5aGYU7reHiWVc1jKj2vmP4yoUDPwNP1AgNpNovfQhkgTOanKYmC_fTjkdT3-BnOTdORZwuMlT75iNJ2GKWWbCsRJKlKO7Wp-mZ6R1Dr_86-UR30OldtPEp6oOAj', start_index=3604)
Annotation(end_index=3920, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBsLnRDSLKmUPOYw7FyFtDCcLHN_B2b5pNjgxzxDEM8JLYaIkkPxdQ7tt6AO6PGd3Wb1M4Ig1bH_ybAugRUWXeK2tGuw9YEvQIErHnmLf7EMm3eb35qRCOeoAfNRka-vArbjksKByjfbf500jgUXgVh7TxhqDPcCHuCo81y0xnJphmGH9H5BJBLVPaEDgFbQdvyJ0VzibMqhXFw_v59iqX', start_index=3908)
Annotation(end_index=3920, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0TJiQH7rjAs3vHKx1jf563Tp2vIhSLYsucdKEOWl07iwQrdyan10Zev5jiqtvqjzSl1Q5ny-nyWb5gxm9SO9VwhxK-bnF97cfqp5DsA6FD80JXaaauaya6Abnyk4N2dc9TmN0Em-F9AKoGfztGUJ6PYTZLxRDbml10MhgvKA5SyoI', start_index=3908)
Annotation(end_index=4798, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETo_hf0jcwLi2cKLpibCYsvkJtauR6qrj-bZke51v48tXM26Gkc2aHEdvCb4-DSSOE-tbF4SbwXOKJVZfS24GRK_-LnSX0FCyHP7GDdUb-d55btLLpJgcIg-q6P3ZqLMFPC3F0pkDJ__LePmnADK6AIpwfVPKx8OqsMa-QkJKD1wnydLGBriAMtqx_uJiCpBamtQ==', start_index=4786)
Annotation(end_index=4798, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWIFyuaNv3KBRM_3zQc3tfxqzNxbyJEseWj56FTUfsxqgf2YATSOM67nUy8ka-WQEY3g_8E_fI48jocWZCVtUhbVEVP9MJY-kOKUnU5w8s3eKFOODBD9FxjB_d', start_index=4786)
Annotation(end_index=5729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAqtNI3WBsdawx2aCnITDujBUJ--lOtlYCs2sVfGN9pPSzAkOc8C_9T4tdtAxstvoLJJy-ziXjcIKAbmUIqeXWx6AD6csiYB7yap8OAkBsl9ee747qHnEqdKvlXuqYs2SGlc3zRy4WoB1wnIHtMJ02huzh_ec3lW_Jzvb_JDoBB6TMOSMt_kS_CIm8VQ==', start_index=5717)
Annotation(end_index=5729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETo_hf0jcwLi2cKLpibCYsvkJtauR6qrj-bZke51v48tXM26Gkc2aHEdvCb4-DSSOE-tbF4SbwXOKJVZfS24GRK_-LnSX0FCyHP7GDdUb-d55btLLpJgcIg-q6P3ZqLMFPC3F0pkDJ__LePmnADK6AIpwfVPKx8OqsMa-QkJKD1wnydLGBriAMtqx_uJiCpBamtQ==', start_index=5717)
Annotation(end_index=5970, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ5x1XDrUXr7hG70ilu3oxu2TFxIb_caPjVTwdI5JObqK4Aj3PsB2sBy3_utzRGQqqFaifmTo6tGVmRBHvOS5gVArvkXwkdekvKySDniuQOcfQ9wPcjIUiCcFSsyB3G4ixyWGctFZpoA2oiNWJD4sYe8OtCtxYvlb9UkiU7uROqW7Z1fu8', start_index=5956)
Annotation(end_index=5970, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzFKCIg6E0b6AS7xfSfIZu7PfZoH8ShmXwHEbl3fPvt9ldGCDVHBBoX6dm_JnAIIXoXMI7om8TSymbh1tn9iRTurn2DqQMvEF_oa0PQBedP3rt63AAnaIzsw8a72JZ2osTvLZzLZMHbiKH4lWZNHKD3DAN2lhAZS8TwqBTV3Vy7LR_ad1-9GYY', start_index=5956)
Annotation(end_index=6453, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ5x1XDrUXr7hG70ilu3oxu2TFxIb_caPjVTwdI5JObqK4Aj3PsB2sBy3_utzRGQqqFaifmTo6tGVmRBHvOS5gVArvkXwkdekvKySDniuQOcfQ9wPcjIUiCcFSsyB3G4ixyWGctFZpoA2oiNWJD4sYe8OtCtxYvlb9UkiU7uROqW7Z1fu8', start_index=6443)
Annotation(end_index=6961, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWIFyuaNv3KBRM_3zQc3tfxqzNxbyJEseWj56FTUfsxqgf2YATSOM67nUy8ka-WQEY3g_8E_fI48jocWZCVtUhbVEVP9MJY-kOKUnU5w8s3eKFOODBD9FxjB_d', start_index=6948)
Annotation(end_index=6961, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqncnu3YomUyHjX6KJ9YuOwPMCLdt31lUDWTBLx5EDQ0q5m9y7uM2eaXXlQIxD52mUt9pmlYYtnohqAKDR1Km5jlUplcBHsSwUtm12d3siEDZqtKfwiAPrb1Kh5OI0IepKZnJEeCzj8WUif_eRs0ZeV1iGPDpBohigpvRUR3c6Wt62L1MgDjFcKq_YsvHM', start_index=6948)
Annotation(end_index=7173, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqncnu3YomUyHjX6KJ9YuOwPMCLdt31lUDWTBLx5EDQ0q5m9y7uM2eaXXlQIxD52mUt9pmlYYtnohqAKDR1Km5jlUplcBHsSwUtm12d3siEDZqtKfwiAPrb1Kh5OI0IepKZnJEeCzj8WUif_eRs0ZeV1iGPDpBohigpvRUR3c6Wt62L1MgDjFcKq_YsvHM', start_index=7163)
Annotation(end_index=7664, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEx0HgOuxEuvkkN4UaHvcectl-CmXZj23vXLI7xfRQ91L0wDxzhuhPUf4-oCQlPFm5xb1D31es_n0hkMSryIe9c0s_2dBQCn0Q2xIatIXAB5BDl3VRqjqKeMulvQt2PGWdPxJ5KeEyIms8H-2byzsDwZG3Wvipx3bk8Tejz08Cvi_lKTjr9zsWoqlUMiyWoVKWXQ1TlpmXDQt805pMjhJw4oDEaORWhbFY8aqFfw==', start_index=7650)
Annotation(end_index=7664, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTeNv6qUmqnq8sHkGYGFriG5zvToo25a_sU3hrDyRi7htpUIM2s8tZxQsnBo1FpxNoPtmhMfjWnFVbwg9FiTZmi_MBHSwXMS2I9ZGfs_rNnW7Ahm0OJQ==', start_index=7650)
Annotation(end_index=8339, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBsLnRDSLKmUPOYw7FyFtDCcLHN_B2b5pNjgxzxDEM8JLYaIkkPxdQ7tt6AO6PGd3Wb1M4Ig1bH_ybAugRUWXeK2tGuw9YEvQIErHnmLf7EMm3eb35qRCOeoAfNRka-vArbjksKByjfbf500jgUXgVh7TxhqDPcCHuCo81y0xnJphmGH9H5BJBLVPaEDgFbQdvyJ0VzibMqhXFw_v59iqX', start_index=8326)
Annotation(end_index=8339, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbUMUME6MvhR1aiGLr_ihVYVyccOX37fP_5vd1ikiezIljXfVxC6h1ba3yIm37k5ZYygQTTGvOi6R8wk-j4RrpCTsXOyKkrqcauBYih9bL0uqko8rFNLkHRP8pf_qk0PuGydqlF3Z9xZmUCLdE_S00Q06l2hUSjSLkEzJJelZv79ClK466cMGpWPY=', start_index=8326)
Annotation(end_index=8683, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0TJiQH7rjAs3vHKx1jf563Tp2vIhSLYsucdKEOWl07iwQrdyan10Zev5jiqtvqjzSl1Q5ny-nyWb5gxm9SO9VwhxK-bnF97cfqp5DsA6FD80JXaaauaya6Abnyk4N2dc9TmN0Em-F9AKoGfztGUJ6PYTZLxRDbml10MhgvKA5SyoI', start_index=8670)
Annotation(end_index=8683, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTeNv6qUmqnq8sHkGYGFriG5zvToo25a_sU3hrDyRi7htpUIM2s8tZxQsnBo1FpxNoPtmhMfjWnFVbwg9FiTZmi_MBHSwXMS2I9ZGfs_rNnW7Ahm0OJQ==', start_index=8670)
Annotation(end_index=9215, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEY45Arx-jQr6eor2KqviIPHyEtHA8rF0x3xovz4ylbAy0UHxDlbQ8p07ncgV_h_4j914J4Jzq-OEHv8SD3qRbFZRDnth1OtjkGq89kQJ0RwQHBEVZ12lzHt23lE6nlpxzlZqcGrBiNxC2xSFBKBOy9OnzkaVAMz3trowAkxb8BOeefog==', start_index=9201)
Annotation(end_index=9215, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR09ZYgKicW7P9Hy6DPx4z6JcZ64a0bkw05t2LjHrU-RWFDep_VmRq4oxfw0gwMF2g7KxzdvjilIzF6_MP9qeQUbTu9es6y8Lzb5gk8rKRYQMnd0q8g-AlvIyQV2MsDpsFrSxnXVOSmxRLBKYf9rmSsNf5h6MifVVp9VbF0q2hdbOuw8GIi5iGPoZl6N3y9Bq7PmudmQnrvOCNBL0FOliO', start_index=9201)
Annotation(end_index=10094, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzFKCIg6E0b6AS7xfSfIZu7PfZoH8ShmXwHEbl3fPvt9ldGCDVHBBoX6dm_JnAIIXoXMI7om8TSymbh1tn9iRTurn2DqQMvEF_oa0PQBedP3rt63AAnaIzsw8a72JZ2osTvLZzLZMHbiKH4lWZNHKD3DAN2lhAZS8TwqBTV3Vy7LR_ad1-9GYY', start_index=10084)
Annotation(end_index=10439, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_C4Q3NnOp48IZ4H2pAj1oF0UhByiD24DGKpke-RGjAj01CJPX95CasOa4r6B7tyipOjnKfB6EEKlnokCq-apRBdOtTtbRowli5XAi8W7dJlrC2ZJvaII7ug==', start_index=10425)
Annotation(end_index=10439, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ5x1XDrUXr7hG70ilu3oxu2TFxIb_caPjVTwdI5JObqK4Aj3PsB2sBy3_utzRGQqqFaifmTo6tGVmRBHvOS5gVArvkXwkdekvKySDniuQOcfQ9wPcjIUiCcFSsyB3G4ixyWGctFZpoA2oiNWJD4sYe8OtCtxYvlb9UkiU7uROqW7Z1fu8', start_index=10425)
Annotation(end_index=10948, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_C4Q3NnOp48IZ4H2pAj1oF0UhByiD24DGKpke-RGjAj01CJPX95CasOa4r6B7tyipOjnKfB6EEKlnokCq-apRBdOtTtbRowli5XAi8W7dJlrC2ZJvaII7ug==', start_index=10930)
Annotation(end_index=10948, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn3n3cmDNENDP64m57rQWaveYh-pfmBtgsGQiAc1ptVzTh1a3FUjCHI37_XjuzIwrxxjq9cnRH5uHcu-9kMRoyXyELIBHoM_8otfVKwB-2DnkykOthFM8A_Cloer3uYsVkhQ0MxEccuW8hHZsCh1numoxo', start_index=10930)
Annotation(end_index=10948, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ5x1XDrUXr7hG70ilu3oxu2TFxIb_caPjVTwdI5JObqK4Aj3PsB2sBy3_utzRGQqqFaifmTo6tGVmRBHvOS5gVArvkXwkdekvKySDniuQOcfQ9wPcjIUiCcFSsyB3G4ixyWGctFZpoA2oiNWJD4sYe8OtCtxYvlb9UkiU7uROqW7Z1fu8', start_index=10930)
Annotation(end_index=11316, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_C4Q3NnOp48IZ4H2pAj1oF0UhByiD24DGKpke-RGjAj01CJPX95CasOa4r6B7tyipOjnKfB6EEKlnokCq-apRBdOtTtbRowli5XAi8W7dJlrC2ZJvaII7ug==', start_index=11302)
Annotation(end_index=11316, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzFKCIg6E0b6AS7xfSfIZu7PfZoH8ShmXwHEbl3fPvt9ldGCDVHBBoX6dm_JnAIIXoXMI7om8TSymbh1tn9iRTurn2DqQMvEF_oa0PQBedP3rt63AAnaIzsw8a72JZ2osTvLZzLZMHbiKH4lWZNHKD3DAN2lhAZS8TwqBTV3Vy7LR_ad1-9GYY', start_index=11302)
Annotation(end_index=11595, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_C4Q3NnOp48IZ4H2pAj1oF0UhByiD24DGKpke-RGjAj01CJPX95CasOa4r6B7tyipOjnKfB6EEKlnokCq-apRBdOtTtbRowli5XAi8W7dJlrC2ZJvaII7ug==', start_index=11581)
Annotation(end_index=11595, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ5x1XDrUXr7hG70ilu3oxu2TFxIb_caPjVTwdI5JObqK4Aj3PsB2sBy3_utzRGQqqFaifmTo6tGVmRBHvOS5gVArvkXwkdekvKySDniuQOcfQ9wPcjIUiCcFSsyB3G4ixyWGctFZpoA2oiNWJD4sYe8OtCtxYvlb9UkiU7uROqW7Z1fu8', start_index=11581)
Annotation(end_index=12199, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETo_hf0jcwLi2cKLpibCYsvkJtauR6qrj-bZke51v48tXM26Gkc2aHEdvCb4-DSSOE-tbF4SbwXOKJVZfS24GRK_-LnSX0FCyHP7GDdUb-d55btLLpJgcIg-q6P3ZqLMFPC3F0pkDJ__LePmnADK6AIpwfVPKx8OqsMa-QkJKD1wnydLGBriAMtqx_uJiCpBamtQ==', start_index=12182)
Annotation(end_index=12199, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ5x1XDrUXr7hG70ilu3oxu2TFxIb_caPjVTwdI5JObqK4Aj3PsB2sBy3_utzRGQqqFaifmTo6tGVmRBHvOS5gVArvkXwkdekvKySDniuQOcfQ9wPcjIUiCcFSsyB3G4ixyWGctFZpoA2oiNWJD4sYe8OtCtxYvlb9UkiU7uROqW7Z1fu8', start_index=12182)
Annotation(end_index=12199, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzFKCIg6E0b6AS7xfSfIZu7PfZoH8ShmXwHEbl3fPvt9ldGCDVHBBoX6dm_JnAIIXoXMI7om8TSymbh1tn9iRTurn2DqQMvEF_oa0PQBedP3rt63AAnaIzsw8a72JZ2osTvLZzLZMHbiKH4lWZNHKD3DAN2lhAZS8TwqBTV3Vy7LR_ad1-9GYY', start_index=12182)
Annotation(end_index=13165, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8U5E1tA7giSBYLAJpBxI14tGMeC55x5uk2rNnrEuAxfmR1U9v9ZR-SbolGD2fTKhjhCVqpQCnhh2BQmAcvhlwQeYnQFiqrk2ZaRnAAmrD0bP0GGR2Gw==', start_index=13147)
Annotation(end_index=13165, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6LRSahn0GFBWpBSYOc7FXirRe64jTVGVFxzo3-s4ydciRDrLak9btSyM45vX39QSVodic158aSKQMDstHcSrZVT9al5fN6XilO1qwaCF8FGhtZTJZhAmfFnmjx3CDt7g53eo=', start_index=13147)
Annotation(end_index=13165, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9BHgX0QmAahoU38SrOk1HZK2h1N7RegPu0upfS3tbdXeOGiu6PWRYj13PJJEziaBxClwvtl9zro4-y0O2CLz6zv5w3flQ-UstAwSGw0bgwMuG4GFNgtcb6bdN34Yoq-m2XCIHgVygba_7FlCSsIti2mQcdihEOp9-ulP4mjqc0hSxeaXhGzfzWU6iOx1MR9wwFZu7okx14P3OBUfKCV8EAIBsYu32_Wew', start_index=13147)
Annotation(end_index=13403, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVmx8_7ZxTfFqQ12J5dgmCOwtvsfRR7yUw5UiUmYNqZb6dgWfeZyA5jG6NpmDcB1_C64hmZ_S3T0_sBCz8gYC08xPvmPogbXGsxWwROe9CroHX4v0W1AGV-2xHbGHCJfYqcdkIgZj63zBOQhbrJ129RpwFOoFmaY4lbQPUv0PdWsIdtTs93Ye7BRjLhVoEnKzapVeUuzYJf7BfXDsfs2QndamJMQLq56IYJ6xuZLb5pQI=', start_index=13385)
Annotation(end_index=13403, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiYIT4biX_xZAHPV687UWe6PXtzG9s7Gmm0K03d7E97rZFxEA3uss6h_iTmomIeXB3XLY5Fp-Cv6JnJSou50r0Qd1g6OEVmxXOuw81l9k3J0c3jzZdSjbdKMpFeBrDaCAwCTwdmnusVOxylqletNx5aS_4dNPHNCmDaoO2VddPmrN2-dxg7z41RCvHhHNZax-wW8tajQSURg58PvBTNZX7RNAqNmfhqLsrlsbOH_Bwch9SbM9NGieFfddfwaX-WvMtW-RP2F-Iiavv9xYI', start_index=13385)
Annotation(end_index=13403, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEltEoUvKnz8ZJQ2L7lTu7T6__4I0GpnYgVhYUheig3arhoH-373VYyIJqAHvxMRN0sdaQpHCME3vTzX1eMCZbuPS2RhIsNTSFjKI5WgDaM7lLjxV8H2r90AP8ZqWS9p8omdSYwxrEBMwsWnJYkDBK', start_index=13385)
Annotation(end_index=14264, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiYIT4biX_xZAHPV687UWe6PXtzG9s7Gmm0K03d7E97rZFxEA3uss6h_iTmomIeXB3XLY5Fp-Cv6JnJSou50r0Qd1g6OEVmxXOuw81l9k3J0c3jzZdSjbdKMpFeBrDaCAwCTwdmnusVOxylqletNx5aS_4dNPHNCmDaoO2VddPmrN2-dxg7z41RCvHhHNZax-wW8tajQSURg58PvBTNZX7RNAqNmfhqLsrlsbOH_Bwch9SbM9NGieFfddfwaX-WvMtW-RP2F-Iiavv9xYI', start_index=14250)
Annotation(end_index=14264, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEltEoUvKnz8ZJQ2L7lTu7T6__4I0GpnYgVhYUheig3arhoH-373VYyIJqAHvxMRN0sdaQpHCME3vTzX1eMCZbuPS2RhIsNTSFjKI5WgDaM7lLjxV8H2r90AP8ZqWS9p8omdSYwxrEBMwsWnJYkDBK', start_index=14250)
Annotation(end_index=14810, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETo_hf0jcwLi2cKLpibCYsvkJtauR6qrj-bZke51v48tXM26Gkc2aHEdvCb4-DSSOE-tbF4SbwXOKJVZfS24GRK_-LnSX0FCyHP7GDdUb-d55btLLpJgcIg-q6P3ZqLMFPC3F0pkDJ__LePmnADK6AIpwfVPKx8OqsMa-QkJKD1wnydLGBriAMtqx_uJiCpBamtQ==', start_index=14794)
Annotation(end_index=14810, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyIgoTRwto-X65C7rywBDczkr7jyUxO8dNwzy4nLSWDWvhwWk-q8q09Bg4LMyx1p67dyDfFqp9s0gx-Q-DU25uinWKyykzGwuGODOMEUGvyfhjRXEEcxSXyDA_f8tuojVRfg==', start_index=14794)
Annotation(end_index=14810, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5F4H5D0NMboJpuq_xx5-sW2-iLwDHTx0UYzaB9ujjNa8Eh-ZSiP0KBDI-gmyFUWqnjNToTvmRAmRfVlbWr8ABhos3fRKBQyWMwBcjhWlHzvcQdtc5xeOU9EN6Ds0=', start_index=14794)
Annotation(end_index=15408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETo_hf0jcwLi2cKLpibCYsvkJtauR6qrj-bZke51v48tXM26Gkc2aHEdvCb4-DSSOE-tbF4SbwXOKJVZfS24GRK_-LnSX0FCyHP7GDdUb-d55btLLpJgcIg-q6P3ZqLMFPC3F0pkDJ__LePmnADK6AIpwfVPKx8OqsMa-QkJKD1wnydLGBriAMtqx_uJiCpBamtQ==', start_index=15395)
Annotation(end_index=15408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgCNNQcBprdGb20iR6qCkdKOQp_ROSyB0kS8YKavxEM78nYzcDK-382FjkcjxLUcadWfS-8WWCe1_yC5wU_4XVrw9Myc7sgXRwAcPKowAUYwDxHJyCjnG3MA==', start_index=15395)
Annotation(end_index=17145, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETo_hf0jcwLi2cKLpibCYsvkJtauR6qrj-bZke51v48tXM26Gkc2aHEdvCb4-DSSOE-tbF4SbwXOKJVZfS24GRK_-LnSX0FCyHP7GDdUb-d55btLLpJgcIg-q6P3ZqLMFPC3F0pkDJ__LePmnADK6AIpwfVPKx8OqsMa-QkJKD1wnydLGBriAMtqx_uJiCpBamtQ==', start_index=17136)
Annotation(end_index=17429, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpKVOLWKKBSOS7ROXUnEbROoHxBPktODELYpos5RIn203pD2zCRXIxpC_Iqwp_HPHjw0inwKNJ09blkVzTcTbk8fuhmN4znQYGSzxM-p_OUXjxy1ynVRC7JA==', start_index=17419)
Annotation(end_index=17668, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_C4Q3NnOp48IZ4H2pAj1oF0UhByiD24DGKpke-RGjAj01CJPX95CasOa4r6B7tyipOjnKfB6EEKlnokCq-apRBdOtTtbRowli5XAi8W7dJlrC2ZJvaII7ug==', start_index=17658)
Annotation(end_index=18479, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiYIT4biX_xZAHPV687UWe6PXtzG9s7Gmm0K03d7E97rZFxEA3uss6h_iTmomIeXB3XLY5Fp-Cv6JnJSou50r0Qd1g6OEVmxXOuw81l9k3J0c3jzZdSjbdKMpFeBrDaCAwCTwdmnusVOxylqletNx5aS_4dNPHNCmDaoO2VddPmrN2-dxg7z41RCvHhHNZax-wW8tajQSURg58PvBTNZX7RNAqNmfhqLsrlsbOH_Bwch9SbM9NGieFfddfwaX-WvMtW-RP2F-Iiavv9xYI', start_index=18465)
Annotation(end_index=18479, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEltEoUvKnz8ZJQ2L7lTu7T6__4I0GpnYgVhYUheig3arhoH-373VYyIJqAHvxMRN0sdaQpHCME3vTzX1eMCZbuPS2RhIsNTSFjKI5WgDaM7lLjxV8H2r90AP8ZqWS9p8omdSYwxrEBMwsWnJYkDBK', start_index=18465)
Annotation(end_index=18834, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWEuLbIMeCvmPLZY5S6Kynau0SoDegzhoLVM5O_mfq9Zn4y2BqlCBVvR699OmZmZSJ9Wlv8HQCmaywr0iWgyir8yIddmugftWdZZ9Cp6uTPMpgSRY9sCcmtNNVfc33UQjknF7r8Za2lOtPHUKbgOldnYSibIWp0cMTj55luMfCQ-G9VL57FSULvXnC2g==', start_index=18821)
Annotation(end_index=18834, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHADKjsTfWK5AcCY48v-0fJFgzD0IlgCSPTpQ_tcsLxwxmGpFl_9YIEEV4SBIz_nV__iMlfDu39o7eukOIVWjKHsQCoVZr-j9H3IbT5Q3SEd8ZCXNDNQzX0s5xLSAek6kWyjomiiTLr8nkeTfBzID7eOlRr', start_index=18821)
Annotation(end_index=18966, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5F4H5D0NMboJpuq_xx5-sW2-iLwDHTx0UYzaB9ujjNa8Eh-ZSiP0KBDI-gmyFUWqnjNToTvmRAmRfVlbWr8ABhos3fRKBQyWMwBcjhWlHzvcQdtc5xeOU9EN6Ds0=', start_index=18957)
Annotation(end_index=18997, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8U5E1tA7giSBYLAJpBxI14tGMeC55x5uk2rNnrEuAxfmR1U9v9ZR-SbolGD2fTKhjhCVqpQCnhh2BQmAcvhlwQeYnQFiqrk2ZaRnAAmrD0bP0GGR2Gw==', start_index=18987)
Annotation(end_index=19538, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5F4H5D0NMboJpuq_xx5-sW2-iLwDHTx0UYzaB9ujjNa8Eh-ZSiP0KBDI-gmyFUWqnjNToTvmRAmRfVlbWr8ABhos3fRKBQyWMwBcjhWlHzvcQdtc5xeOU9EN6Ds0=', start_index=19529)
Annotation(end_index=19608, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5F4H5D0NMboJpuq_xx5-sW2-iLwDHTx0UYzaB9ujjNa8Eh-ZSiP0KBDI-gmyFUWqnjNToTvmRAmRfVlbWr8ABhos3fRKBQyWMwBcjhWlHzvcQdtc5xeOU9EN6Ds0=', start_index=19599)
Annotation(end_index=19618, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETo_hf0jcwLi2cKLpibCYsvkJtauR6qrj-bZke51v48tXM26Gkc2aHEdvCb4-DSSOE-tbF4SbwXOKJVZfS24GRK_-LnSX0FCyHP7GDdUb-d55btLLpJgcIg-q6P3ZqLMFPC3F0pkDJ__LePmnADK6AIpwfVPKx8OqsMa-QkJKD1wnydLGBriAMtqx_uJiCpBamtQ==', start_index=19609)
Annotation(end_index=19683, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETo_hf0jcwLi2cKLpibCYsvkJtauR6qrj-bZke51v48tXM26Gkc2aHEdvCb4-DSSOE-tbF4SbwXOKJVZfS24GRK_-LnSX0FCyHP7GDdUb-d55btLLpJgcIg-q6P3ZqLMFPC3F0pkDJ__LePmnADK6AIpwfVPKx8OqsMa-QkJKD1wnydLGBriAMtqx_uJiCpBamtQ==', start_index=19674)
Annotation(end_index=19694, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR09ZYgKicW7P9Hy6DPx4z6JcZ64a0bkw05t2LjHrU-RWFDep_VmRq4oxfw0gwMF2g7KxzdvjilIzF6_MP9qeQUbTu9es6y8Lzb5gk8rKRYQMnd0q8g-AlvIyQV2MsDpsFrSxnXVOSmxRLBKYf9rmSsNf5h6MifVVp9VbF0q2hdbOuw8GIi5iGPoZl6N3y9Bq7PmudmQnrvOCNBL0FOliO', start_index=19684)
Annotation(end_index=19763, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR09ZYgKicW7P9Hy6DPx4z6JcZ64a0bkw05t2LjHrU-RWFDep_VmRq4oxfw0gwMF2g7KxzdvjilIzF6_MP9qeQUbTu9es6y8Lzb5gk8rKRYQMnd0q8g-AlvIyQV2MsDpsFrSxnXVOSmxRLBKYf9rmSsNf5h6MifVVp9VbF0q2hdbOuw8GIi5iGPoZl6N3y9Bq7PmudmQnrvOCNBL0FOliO', start_index=19753)
Annotation(end_index=19773, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTQa6dyh7HI1gG3KBfDTZUb5aGYU7reHiWVc1jKj2vmP4yoUDPwNP1AgNpNovfQhkgTOanKYmC_fTjkdT3-BnOTdORZwuMlT75iNJ2GKWWbCsRJKlKO7Wp-mZ6R1Dr_86-UR30OldtPEp6oOAj', start_index=19764)
Annotation(end_index=19855, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTQa6dyh7HI1gG3KBfDTZUb5aGYU7reHiWVc1jKj2vmP4yoUDPwNP1AgNpNovfQhkgTOanKYmC_fTjkdT3-BnOTdORZwuMlT75iNJ2GKWWbCsRJKlKO7Wp-mZ6R1Dr_86-UR30OldtPEp6oOAj', start_index=19846)
Annotation(end_index=19866, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHADKjsTfWK5AcCY48v-0fJFgzD0IlgCSPTpQ_tcsLxwxmGpFl_9YIEEV4SBIz_nV__iMlfDu39o7eukOIVWjKHsQCoVZr-j9H3IbT5Q3SEd8ZCXNDNQzX0s5xLSAek6kWyjomiiTLr8nkeTfBzID7eOlRr', start_index=19856)
Annotation(end_index=19901, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHADKjsTfWK5AcCY48v-0fJFgzD0IlgCSPTpQ_tcsLxwxmGpFl_9YIEEV4SBIz_nV__iMlfDu39o7eukOIVWjKHsQCoVZr-j9H3IbT5Q3SEd8ZCXNDNQzX0s5xLSAek6kWyjomiiTLr8nkeTfBzID7eOlRr', start_index=19891)
Annotation(end_index=19911, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBsLnRDSLKmUPOYw7FyFtDCcLHN_B2b5pNjgxzxDEM8JLYaIkkPxdQ7tt6AO6PGd3Wb1M4Ig1bH_ybAugRUWXeK2tGuw9YEvQIErHnmLf7EMm3eb35qRCOeoAfNRka-vArbjksKByjfbf500jgUXgVh7TxhqDPcCHuCo81y0xnJphmGH9H5BJBLVPaEDgFbQdvyJ0VzibMqhXFw_v59iqX', start_index=19902)
Annotation(end_index=19994, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBsLnRDSLKmUPOYw7FyFtDCcLHN_B2b5pNjgxzxDEM8JLYaIkkPxdQ7tt6AO6PGd3Wb1M4Ig1bH_ybAugRUWXeK2tGuw9YEvQIErHnmLf7EMm3eb35qRCOeoAfNRka-vArbjksKByjfbf500jgUXgVh7TxhqDPcCHuCo81y0xnJphmGH9H5BJBLVPaEDgFbQdvyJ0VzibMqhXFw_v59iqX', start_index=19985)
Annotation(end_index=20005, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEY45Arx-jQr6eor2KqviIPHyEtHA8rF0x3xovz4ylbAy0UHxDlbQ8p07ncgV_h_4j914J4Jzq-OEHv8SD3qRbFZRDnth1OtjkGq89kQJ0RwQHBEVZ12lzHt23lE6nlpxzlZqcGrBiNxC2xSFBKBOy9OnzkaVAMz3trowAkxb8BOeefog==', start_index=19995)
Annotation(end_index=20048, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEY45Arx-jQr6eor2KqviIPHyEtHA8rF0x3xovz4ylbAy0UHxDlbQ8p07ncgV_h_4j914J4Jzq-OEHv8SD3qRbFZRDnth1OtjkGq89kQJ0RwQHBEVZ12lzHt23lE6nlpxzlZqcGrBiNxC2xSFBKBOy9OnzkaVAMz3trowAkxb8BOeefog==', start_index=20038)
Annotation(end_index=20058, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWEuLbIMeCvmPLZY5S6Kynau0SoDegzhoLVM5O_mfq9Zn4y2BqlCBVvR699OmZmZSJ9Wlv8HQCmaywr0iWgyir8yIddmugftWdZZ9Cp6uTPMpgSRY9sCcmtNNVfc33UQjknF7r8Za2lOtPHUKbgOldnYSibIWp0cMTj55luMfCQ-G9VL57FSULvXnC2g==', start_index=20049)
Annotation(end_index=20120, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWEuLbIMeCvmPLZY5S6Kynau0SoDegzhoLVM5O_mfq9Zn4y2BqlCBVvR699OmZmZSJ9Wlv8HQCmaywr0iWgyir8yIddmugftWdZZ9Cp6uTPMpgSRY9sCcmtNNVfc33UQjknF7r8Za2lOtPHUKbgOldnYSibIWp0cMTj55luMfCQ-G9VL57FSULvXnC2g==', start_index=20111)
Annotation(end_index=20130, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0TJiQH7rjAs3vHKx1jf563Tp2vIhSLYsucdKEOWl07iwQrdyan10Zev5jiqtvqjzSl1Q5ny-nyWb5gxm9SO9VwhxK-bnF97cfqp5DsA6FD80JXaaauaya6Abnyk4N2dc9TmN0Em-F9AKoGfztGUJ6PYTZLxRDbml10MhgvKA5SyoI', start_index=20121)
Annotation(end_index=20183, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0TJiQH7rjAs3vHKx1jf563Tp2vIhSLYsucdKEOWl07iwQrdyan10Zev5jiqtvqjzSl1Q5ny-nyWb5gxm9SO9VwhxK-bnF97cfqp5DsA6FD80JXaaauaya6Abnyk4N2dc9TmN0Em-F9AKoGfztGUJ6PYTZLxRDbml10MhgvKA5SyoI', start_index=20174)
Annotation(end_index=20193, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp_hs4SUxqMUds1geAhNY26GE15SUCgsEh0uWBzSjqGbf-5iXLsFemHzC0YQH2oTirHj70gb0wQFCbBqGGlQCAhh_YV1V5xGOxDASjhFihf_On-i-tCZcExvTbZJA=', start_index=20184)
Annotation(end_index=20265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp_hs4SUxqMUds1geAhNY26GE15SUCgsEh0uWBzSjqGbf-5iXLsFemHzC0YQH2oTirHj70gb0wQFCbBqGGlQCAhh_YV1V5xGOxDASjhFihf_On-i-tCZcExvTbZJA=', start_index=20256)
Annotation(end_index=20276, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpKVOLWKKBSOS7ROXUnEbROoHxBPktODELYpos5RIn203pD2zCRXIxpC_Iqwp_HPHjw0inwKNJ09blkVzTcTbk8fuhmN4znQYGSzxM-p_OUXjxy1ynVRC7JA==', start_index=20266)
Annotation(end_index=20345, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpKVOLWKKBSOS7ROXUnEbROoHxBPktODELYpos5RIn203pD2zCRXIxpC_Iqwp_HPHjw0inwKNJ09blkVzTcTbk8fuhmN4znQYGSzxM-p_OUXjxy1ynVRC7JA==', start_index=20335)
Annotation(end_index=20356, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEx0HgOuxEuvkkN4UaHvcectl-CmXZj23vXLI7xfRQ91L0wDxzhuhPUf4-oCQlPFm5xb1D31es_n0hkMSryIe9c0s_2dBQCn0Q2xIatIXAB5BDl3VRqjqKeMulvQt2PGWdPxJ5KeEyIms8H-2byzsDwZG3Wvipx3bk8Tejz08Cvi_lKTjr9zsWoqlUMiyWoVKWXQ1TlpmXDQt805pMjhJw4oDEaORWhbFY8aqFfw==', start_index=20346)
Annotation(end_index=20447, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEx0HgOuxEuvkkN4UaHvcectl-CmXZj23vXLI7xfRQ91L0wDxzhuhPUf4-oCQlPFm5xb1D31es_n0hkMSryIe9c0s_2dBQCn0Q2xIatIXAB5BDl3VRqjqKeMulvQt2PGWdPxJ5KeEyIms8H-2byzsDwZG3Wvipx3bk8Tejz08Cvi_lKTjr9zsWoqlUMiyWoVKWXQ1TlpmXDQt805pMjhJw4oDEaORWhbFY8aqFfw==', start_index=20437)
Annotation(end_index=20458, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyIgoTRwto-X65C7rywBDczkr7jyUxO8dNwzy4nLSWDWvhwWk-q8q09Bg4LMyx1p67dyDfFqp9s0gx-Q-DU25uinWKyykzGwuGODOMEUGvyfhjRXEEcxSXyDA_f8tuojVRfg==', start_index=20448)
Annotation(end_index=20515, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyIgoTRwto-X65C7rywBDczkr7jyUxO8dNwzy4nLSWDWvhwWk-q8q09Bg4LMyx1p67dyDfFqp9s0gx-Q-DU25uinWKyykzGwuGODOMEUGvyfhjRXEEcxSXyDA_f8tuojVRfg==', start_index=20505)
Annotation(end_index=20526, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqncnu3YomUyHjX6KJ9YuOwPMCLdt31lUDWTBLx5EDQ0q5m9y7uM2eaXXlQIxD52mUt9pmlYYtnohqAKDR1Km5jlUplcBHsSwUtm12d3siEDZqtKfwiAPrb1Kh5OI0IepKZnJEeCzj8WUif_eRs0ZeV1iGPDpBohigpvRUR3c6Wt62L1MgDjFcKq_YsvHM', start_index=20516)
Annotation(end_index=20582, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqncnu3YomUyHjX6KJ9YuOwPMCLdt31lUDWTBLx5EDQ0q5m9y7uM2eaXXlQIxD52mUt9pmlYYtnohqAKDR1Km5jlUplcBHsSwUtm12d3siEDZqtKfwiAPrb1Kh5OI0IepKZnJEeCzj8WUif_eRs0ZeV1iGPDpBohigpvRUR3c6Wt62L1MgDjFcKq_YsvHM', start_index=20572)
Annotation(end_index=20593, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbUMUME6MvhR1aiGLr_ihVYVyccOX37fP_5vd1ikiezIljXfVxC6h1ba3yIm37k5ZYygQTTGvOi6R8wk-j4RrpCTsXOyKkrqcauBYih9bL0uqko8rFNLkHRP8pf_qk0PuGydqlF3Z9xZmUCLdE_S00Q06l2hUSjSLkEzJJelZv79ClK466cMGpWPY=', start_index=20583)
Annotation(end_index=20643, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbUMUME6MvhR1aiGLr_ihVYVyccOX37fP_5vd1ikiezIljXfVxC6h1ba3yIm37k5ZYygQTTGvOi6R8wk-j4RrpCTsXOyKkrqcauBYih9bL0uqko8rFNLkHRP8pf_qk0PuGydqlF3Z9xZmUCLdE_S00Q06l2hUSjSLkEzJJelZv79ClK466cMGpWPY=', start_index=20633)
Annotation(end_index=20654, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuSVgO3x_NC97BOTvJeaMNyWkC92ArRqYYTF68Q1Kvn9y_m3cu0ud3GWzkacOC7tGStWvkS43RcE-KrdNawILeR73kJ0IirPdToD93RhrYfwLhPhKuHs0ZwmiP1B0j03kCQwqhTKw0HFVhVOZjd2CzxRLP4i-ANy2oOl0eoQ==', start_index=20644)
Annotation(end_index=20687, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuSVgO3x_NC97BOTvJeaMNyWkC92ArRqYYTF68Q1Kvn9y_m3cu0ud3GWzkacOC7tGStWvkS43RcE-KrdNawILeR73kJ0IirPdToD93RhrYfwLhPhKuHs0ZwmiP1B0j03kCQwqhTKw0HFVhVOZjd2CzxRLP4i-ANy2oOl0eoQ==', start_index=20677)
Annotation(end_index=20698, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTeNv6qUmqnq8sHkGYGFriG5zvToo25a_sU3hrDyRi7htpUIM2s8tZxQsnBo1FpxNoPtmhMfjWnFVbwg9FiTZmi_MBHSwXMS2I9ZGfs_rNnW7Ahm0OJQ==', start_index=20688)
Annotation(end_index=20732, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTeNv6qUmqnq8sHkGYGFriG5zvToo25a_sU3hrDyRi7htpUIM2s8tZxQsnBo1FpxNoPtmhMfjWnFVbwg9FiTZmi_MBHSwXMS2I9ZGfs_rNnW7Ahm0OJQ==', start_index=20722)
Annotation(end_index=20743, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzFKCIg6E0b6AS7xfSfIZu7PfZoH8ShmXwHEbl3fPvt9ldGCDVHBBoX6dm_JnAIIXoXMI7om8TSymbh1tn9iRTurn2DqQMvEF_oa0PQBedP3rt63AAnaIzsw8a72JZ2osTvLZzLZMHbiKH4lWZNHKD3DAN2lhAZS8TwqBTV3Vy7LR_ad1-9GYY', start_index=20733)
Annotation(end_index=20825, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzFKCIg6E0b6AS7xfSfIZu7PfZoH8ShmXwHEbl3fPvt9ldGCDVHBBoX6dm_JnAIIXoXMI7om8TSymbh1tn9iRTurn2DqQMvEF_oa0PQBedP3rt63AAnaIzsw8a72JZ2osTvLZzLZMHbiKH4lWZNHKD3DAN2lhAZS8TwqBTV3Vy7LR_ad1-9GYY', start_index=20815)
Annotation(end_index=20836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_C4Q3NnOp48IZ4H2pAj1oF0UhByiD24DGKpke-RGjAj01CJPX95CasOa4r6B7tyipOjnKfB6EEKlnokCq-apRBdOtTtbRowli5XAi8W7dJlrC2ZJvaII7ug==', start_index=20826)
Annotation(end_index=20889, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_C4Q3NnOp48IZ4H2pAj1oF0UhByiD24DGKpke-RGjAj01CJPX95CasOa4r6B7tyipOjnKfB6EEKlnokCq-apRBdOtTtbRowli5XAi8W7dJlrC2ZJvaII7ug==', start_index=20879)
Annotation(end_index=20900, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbGG2ryIn-fQnISp-IMh1TyiM6GR-p_PSe66CUfFph0hYURzrT-fqpwlKnZqn-QND53qMvkVVFGvN2Fl6JWdkwaI6cVNjLb7FWiHKmsbQwr7UfIEE74iC04or4M2D3U5Oul3eTEIeUGMS0MWdZl9B4nYnOnlqfLPQxxw==', start_index=20890)
Annotation(end_index=20925, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbGG2ryIn-fQnISp-IMh1TyiM6GR-p_PSe66CUfFph0hYURzrT-fqpwlKnZqn-QND53qMvkVVFGvN2Fl6JWdkwaI6cVNjLb7FWiHKmsbQwr7UfIEE74iC04or4M2D3U5Oul3eTEIeUGMS0MWdZl9B4nYnOnlqfLPQxxw==', start_index=20915)
Annotation(end_index=20936, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEltEoUvKnz8ZJQ2L7lTu7T6__4I0GpnYgVhYUheig3arhoH-373VYyIJqAHvxMRN0sdaQpHCME3vTzX1eMCZbuPS2RhIsNTSFjKI5WgDaM7lLjxV8H2r90AP8ZqWS9p8omdSYwxrEBMwsWnJYkDBK', start_index=20926)
Annotation(end_index=20972, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEltEoUvKnz8ZJQ2L7lTu7T6__4I0GpnYgVhYUheig3arhoH-373VYyIJqAHvxMRN0sdaQpHCME3vTzX1eMCZbuPS2RhIsNTSFjKI5WgDaM7lLjxV8H2r90AP8ZqWS9p8omdSYwxrEBMwsWnJYkDBK', start_index=20962)
Annotation(end_index=20983, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgCNNQcBprdGb20iR6qCkdKOQp_ROSyB0kS8YKavxEM78nYzcDK-382FjkcjxLUcadWfS-8WWCe1_yC5wU_4XVrw9Myc7sgXRwAcPKowAUYwDxHJyCjnG3MA==', start_index=20973)
Annotation(end_index=21056, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgCNNQcBprdGb20iR6qCkdKOQp_ROSyB0kS8YKavxEM78nYzcDK-382FjkcjxLUcadWfS-8WWCe1_yC5wU_4XVrw9Myc7sgXRwAcPKowAUYwDxHJyCjnG3MA==', start_index=21046)
Annotation(end_index=21067, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiYIT4biX_xZAHPV687UWe6PXtzG9s7Gmm0K03d7E97rZFxEA3uss6h_iTmomIeXB3XLY5Fp-Cv6JnJSou50r0Qd1g6OEVmxXOuw81l9k3J0c3jzZdSjbdKMpFeBrDaCAwCTwdmnusVOxylqletNx5aS_4dNPHNCmDaoO2VddPmrN2-dxg7z41RCvHhHNZax-wW8tajQSURg58PvBTNZX7RNAqNmfhqLsrlsbOH_Bwch9SbM9NGieFfddfwaX-WvMtW-RP2F-Iiavv9xYI', start_index=21057)
Annotation(end_index=21154, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiYIT4biX_xZAHPV687UWe6PXtzG9s7Gmm0K03d7E97rZFxEA3uss6h_iTmomIeXB3XLY5Fp-Cv6JnJSou50r0Qd1g6OEVmxXOuw81l9k3J0c3jzZdSjbdKMpFeBrDaCAwCTwdmnusVOxylqletNx5aS_4dNPHNCmDaoO2VddPmrN2-dxg7z41RCvHhHNZax-wW8tajQSURg58PvBTNZX7RNAqNmfhqLsrlsbOH_Bwch9SbM9NGieFfddfwaX-WvMtW-RP2F-Iiavv9xYI', start_index=21144)
Annotation(end_index=21165, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEltEoUvKnz8ZJQ2L7lTu7T6__4I0GpnYgVhYUheig3arhoH-373VYyIJqAHvxMRN0sdaQpHCME3vTzX1eMCZbuPS2RhIsNTSFjKI5WgDaM7lLjxV8H2r90AP8ZqWS9p8omdSYwxrEBMwsWnJYkDBK', start_index=21155)
Annotation(end_index=21207, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEltEoUvKnz8ZJQ2L7lTu7T6__4I0GpnYgVhYUheig3arhoH-373VYyIJqAHvxMRN0sdaQpHCME3vTzX1eMCZbuPS2RhIsNTSFjKI5WgDaM7lLjxV8H2r90AP8ZqWS9p8omdSYwxrEBMwsWnJYkDBK', start_index=21197)
Annotation(end_index=21218, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVmx8_7ZxTfFqQ12J5dgmCOwtvsfRR7yUw5UiUmYNqZb6dgWfeZyA5jG6NpmDcB1_C64hmZ_S3T0_sBCz8gYC08xPvmPogbXGsxWwROe9CroHX4v0W1AGV-2xHbGHCJfYqcdkIgZj63zBOQhbrJ129RpwFOoFmaY4lbQPUv0PdWsIdtTs93Ye7BRjLhVoEnKzapVeUuzYJf7BfXDsfs2QndamJMQLq56IYJ6xuZLb5pQI=', start_index=21208)
Annotation(end_index=21260, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVmx8_7ZxTfFqQ12J5dgmCOwtvsfRR7yUw5UiUmYNqZb6dgWfeZyA5jG6NpmDcB1_C64hmZ_S3T0_sBCz8gYC08xPvmPogbXGsxWwROe9CroHX4v0W1AGV-2xHbGHCJfYqcdkIgZj63zBOQhbrJ129RpwFOoFmaY4lbQPUv0PdWsIdtTs93Ye7BRjLhVoEnKzapVeUuzYJf7BfXDsfs2QndamJMQLq56IYJ6xuZLb5pQI=', start_index=21250)
Annotation(end_index=21271, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ5x1XDrUXr7hG70ilu3oxu2TFxIb_caPjVTwdI5JObqK4Aj3PsB2sBy3_utzRGQqqFaifmTo6tGVmRBHvOS5gVArvkXwkdekvKySDniuQOcfQ9wPcjIUiCcFSsyB3G4ixyWGctFZpoA2oiNWJD4sYe8OtCtxYvlb9UkiU7uROqW7Z1fu8', start_index=21261)
Annotation(end_index=21329, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ5x1XDrUXr7hG70ilu3oxu2TFxIb_caPjVTwdI5JObqK4Aj3PsB2sBy3_utzRGQqqFaifmTo6tGVmRBHvOS5gVArvkXwkdekvKySDniuQOcfQ9wPcjIUiCcFSsyB3G4ixyWGctFZpoA2oiNWJD4sYe8OtCtxYvlb9UkiU7uROqW7Z1fu8', start_index=21319)
Annotation(end_index=21340, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzFKCIg6E0b6AS7xfSfIZu7PfZoH8ShmXwHEbl3fPvt9ldGCDVHBBoX6dm_JnAIIXoXMI7om8TSymbh1tn9iRTurn2DqQMvEF_oa0PQBedP3rt63AAnaIzsw8a72JZ2osTvLZzLZMHbiKH4lWZNHKD3DAN2lhAZS8TwqBTV3Vy7LR_ad1-9GYY', start_index=21330)
Annotation(end_index=21399, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzFKCIg6E0b6AS7xfSfIZu7PfZoH8ShmXwHEbl3fPvt9ldGCDVHBBoX6dm_JnAIIXoXMI7om8TSymbh1tn9iRTurn2DqQMvEF_oa0PQBedP3rt63AAnaIzsw8a72JZ2osTvLZzLZMHbiKH4lWZNHKD3DAN2lhAZS8TwqBTV3Vy7LR_ad1-9GYY', start_index=21389)
Annotation(end_index=21410, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_C4Q3NnOp48IZ4H2pAj1oF0UhByiD24DGKpke-RGjAj01CJPX95CasOa4r6B7tyipOjnKfB6EEKlnokCq-apRBdOtTtbRowli5XAi8W7dJlrC2ZJvaII7ug==', start_index=21400)
Annotation(end_index=21477, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_C4Q3NnOp48IZ4H2pAj1oF0UhByiD24DGKpke-RGjAj01CJPX95CasOa4r6B7tyipOjnKfB6EEKlnokCq-apRBdOtTtbRowli5XAi8W7dJlrC2ZJvaII7ug==', start_index=21467)
Annotation(end_index=21488, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn3n3cmDNENDP64m57rQWaveYh-pfmBtgsGQiAc1ptVzTh1a3FUjCHI37_XjuzIwrxxjq9cnRH5uHcu-9kMRoyXyELIBHoM_8otfVKwB-2DnkykOthFM8A_Cloer3uYsVkhQ0MxEccuW8hHZsCh1numoxo', start_index=21478)
Annotation(end_index=21512, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn3n3cmDNENDP64m57rQWaveYh-pfmBtgsGQiAc1ptVzTh1a3FUjCHI37_XjuzIwrxxjq9cnRH5uHcu-9kMRoyXyELIBHoM_8otfVKwB-2DnkykOthFM8A_Cloer3uYsVkhQ0MxEccuW8hHZsCh1numoxo', start_index=21502)
Annotation(end_index=21522, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETo_hf0jcwLi2cKLpibCYsvkJtauR6qrj-bZke51v48tXM26Gkc2aHEdvCb4-DSSOE-tbF4SbwXOKJVZfS24GRK_-LnSX0FCyHP7GDdUb-d55btLLpJgcIg-q6P3ZqLMFPC3F0pkDJ__LePmnADK6AIpwfVPKx8OqsMa-QkJKD1wnydLGBriAMtqx_uJiCpBamtQ==', start_index=21513)
Annotation(end_index=21595, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETo_hf0jcwLi2cKLpibCYsvkJtauR6qrj-bZke51v48tXM26Gkc2aHEdvCb4-DSSOE-tbF4SbwXOKJVZfS24GRK_-LnSX0FCyHP7GDdUb-d55btLLpJgcIg-q6P3ZqLMFPC3F0pkDJ__LePmnADK6AIpwfVPKx8OqsMa-QkJKD1wnydLGBriAMtqx_uJiCpBamtQ==', start_index=21586)
Annotation(end_index=21606, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8U5E1tA7giSBYLAJpBxI14tGMeC55x5uk2rNnrEuAxfmR1U9v9ZR-SbolGD2fTKhjhCVqpQCnhh2BQmAcvhlwQeYnQFiqrk2ZaRnAAmrD0bP0GGR2Gw==', start_index=21596)
Annotation(end_index=21663, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8U5E1tA7giSBYLAJpBxI14tGMeC55x5uk2rNnrEuAxfmR1U9v9ZR-SbolGD2fTKhjhCVqpQCnhh2BQmAcvhlwQeYnQFiqrk2ZaRnAAmrD0bP0GGR2Gw==', start_index=21653)
Annotation(end_index=21674, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9BHgX0QmAahoU38SrOk1HZK2h1N7RegPu0upfS3tbdXeOGiu6PWRYj13PJJEziaBxClwvtl9zro4-y0O2CLz6zv5w3flQ-UstAwSGw0bgwMuG4GFNgtcb6bdN34Yoq-m2XCIHgVygba_7FlCSsIti2mQcdihEOp9-ulP4mjqc0hSxeaXhGzfzWU6iOx1MR9wwFZu7okx14P3OBUfKCV8EAIBsYu32_Wew', start_index=21664)
Annotation(end_index=21731, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9BHgX0QmAahoU38SrOk1HZK2h1N7RegPu0upfS3tbdXeOGiu6PWRYj13PJJEziaBxClwvtl9zro4-y0O2CLz6zv5w3flQ-UstAwSGw0bgwMuG4GFNgtcb6bdN34Yoq-m2XCIHgVygba_7FlCSsIti2mQcdihEOp9-ulP4mjqc0hSxeaXhGzfzWU6iOx1MR9wwFZu7okx14P3OBUfKCV8EAIBsYu32_Wew', start_index=21721)
Annotation(end_index=21742, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6LRSahn0GFBWpBSYOc7FXirRe64jTVGVFxzo3-s4ydciRDrLak9btSyM45vX39QSVodic158aSKQMDstHcSrZVT9al5fN6XilO1qwaCF8FGhtZTJZhAmfFnmjx3CDt7g53eo=', start_index=21732)
Annotation(end_index=21773, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6LRSahn0GFBWpBSYOc7FXirRe64jTVGVFxzo3-s4ydciRDrLak9btSyM45vX39QSVodic158aSKQMDstHcSrZVT9al5fN6XilO1qwaCF8FGhtZTJZhAmfFnmjx3CDt7g53eo=', start_index=21763)
Annotation(end_index=21783, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWIFyuaNv3KBRM_3zQc3tfxqzNxbyJEseWj56FTUfsxqgf2YATSOM67nUy8ka-WQEY3g_8E_fI48jocWZCVtUhbVEVP9MJY-kOKUnU5w8s3eKFOODBD9FxjB_d', start_index=21774)
Annotation(end_index=21838, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWIFyuaNv3KBRM_3zQc3tfxqzNxbyJEseWj56FTUfsxqgf2YATSOM67nUy8ka-WQEY3g_8E_fI48jocWZCVtUhbVEVP9MJY-kOKUnU5w8s3eKFOODBD9FxjB_d', start_index=21829)
Annotation(end_index=21849, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEA1LgS-0pcXBxMbVSJltPWqR55d3KAEDYIfm7TEufdliod3IPzQeQvZ3vvrF6lyQW3yY20yJ2B0BRixwIdIQ5rD8Cf8GxRWcf9A7uhG_5zge1TsMAeKLLe-uS4VGFkoToFpvYptgYTAMQ_mZSplw==', start_index=21839)
Annotation(end_index=21888, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEA1LgS-0pcXBxMbVSJltPWqR55d3KAEDYIfm7TEufdliod3IPzQeQvZ3vvrF6lyQW3yY20yJ2B0BRixwIdIQ5rD8Cf8GxRWcf9A7uhG_5zge1TsMAeKLLe-uS4VGFkoToFpvYptgYTAMQ_mZSplw==', start_index=21878)
Annotation(end_index=21898, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAqtNI3WBsdawx2aCnITDujBUJ--lOtlYCs2sVfGN9pPSzAkOc8C_9T4tdtAxstvoLJJy-ziXjcIKAbmUIqeXWx6AD6csiYB7yap8OAkBsl9ee747qHnEqdKvlXuqYs2SGlc3zRy4WoB1wnIHtMJ02huzh_ec3lW_Jzvb_JDoBB6TMOSMt_kS_CIm8VQ==', start_index=21889)
Annotation(end_index=21954, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAqtNI3WBsdawx2aCnITDujBUJ--lOtlYCs2sVfGN9pPSzAkOc8C_9T4tdtAxstvoLJJy-ziXjcIKAbmUIqeXWx6AD6csiYB7yap8OAkBsl9ee747qHnEqdKvlXuqYs2SGlc3zRy4WoB1wnIHtMJ02huzh_ec3lW_Jzvb_JDoBB6TMOSMt_kS_CIm8VQ==', start_index=21945)

## Sources
