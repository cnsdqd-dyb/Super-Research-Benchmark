# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 20d6dc1a | **Time:** 350.15s | **Cost:** $1.30145
--------------------------------------------------------------------------------

# Theoretical Limits of Blockchain Byzantine Fault Tolerance: A Comprehensive Analysis of Throughput, Security, Latency, and Complexity

### Key Points
*   **Fault Tolerance Thresholds:** In partially synchronous networks (the standard model for the Internet), the theoretical limit for Byzantine Fault Tolerance (BFT) is $n \ge 3f + 1$, meaning a system can tolerate at most $f < n/3$ malicious nodes. Synchronous models can theoretically tolerate $f < n/2$, but rely on strong timing assumptions that are risky in practice.
*   **Message Complexity Lower Bounds:** The Dolev-Reischuk bound establishes that any deterministic BFT protocol must exchange at least $\Omega(n^2)$ messages in the worst case. While modern protocols like HotStuff achieve linear $O(n)$ complexity in optimistic scenarios, they revert to quadratic complexity during view changes or failures.
*   **Latency Limits:** The theoretical lower bound for consensus latency is generally two message delays ($2\Delta$) in optimistic conditions. However, achieving this often requires trading off pipelining efficiency or robustness. Speed-of-light constraints impose an absolute physical floor on latency based on the geographic distribution of nodes.
*   **Throughput vs. Latency Trade-off:** There is an inherent tension between throughput and latency; high throughput often requires batching and pipelining, which induces latency. Recent Directed Acyclic Graph (DAG) architectures attempt to circumvent this by separating data dissemination from metadata ordering, pushing throughput closer to the theoretical limit of network bandwidth.

---

## 1. Introduction

Byzantine Fault Tolerance (BFT) represents the capacity of a distributed system to reach consensus despite the arbitrary (malicious) behavior of a fraction of its components. In the context of blockchain technology, BFT mechanisms are the bedrock of security, ensuring that a distributed ledger remains consistent and immutable even when participants attempt to double-spend funds, censor transactions, or halt the network.

The theoretical limits of these systems are governed by a complex interplay of computer science fundamentals, including the FLP impossibility result, the CAP theorem, and the Dolev-Reischuk lower bounds on communication complexity. As blockchain architectures evolve from classical permissioned models (like PBFT) to permissionless global networks, understanding these hard theoretical ceilings is critical for evaluating claims of "infinite scalability" or "instant finality."

This report provides an exhaustive analysis of the theoretical boundaries of BFT mechanisms, specifically examining the trade-offs between system throughput, security thresholds, network latency, and message complexity.

---

## 2. Theoretical Limits of Security and Resilience

The security of a BFT protocol is defined by its resilience—the maximum number of faulty nodes ($f$) a network of size $n$ can tolerate while maintaining safety (consistency) and liveness (progress). These limits are strictly dictated by the network timing model assumed by the protocol.

### 2.1 The Partial Synchrony Bound ($n \ge 3f + 1$)
Most modern blockchain BFT protocols operate under the assumption of **partial synchrony**. This model assumes that while message delays may be unbounded for a finite period, there exists a Global Stabilization Time (GST) after which message delays are bounded by a known constant $\Delta$ [cite: 1].

Under partial synchrony, the theoretical resilience limit is strictly **$f < n/3$**. This means a network requires at least $3f + 1$ nodes to tolerate $f$ Byzantine faults [cite: 2, 3, 4].
*   **Derivation:** To reach consensus, a node must hear from a quorum of other nodes. If the quorum size is too small, the network may split into two disjoint groups (split-brain), leading to safety violations. If the quorum is too large, liveness is compromised because the faulty nodes can simply refuse to vote, halting the system.
*   **Intersection:** The intersection of any two quorums must contain at least one honest node. In a system of $3f+1$ nodes, a quorum of $2f+1$ ensures that any two quorums overlap by at least $f+1$ nodes. Since at most $f$ are faulty, at least one node in the intersection is honest and ensures consistency [cite: 1].
*   **Impossibility:** It has been proven that BFT agreement is impossible for $n \le 3f$ in partially synchronous settings because an adversary can delay messages between honest partitions to simulate a partition, forcing the system to either stall or diverge [cite: 4].

### 2.2 The Synchronous Bound ($n \ge 2f + 1$)
In a **synchronous** model, where there is a known, fixed upper bound on message delivery time that holds always, the theoretical limit improves to **$f < n/2$** [cite: 3, 5].
*   **Mechanism:** Because the protocol knows exactly how long to wait for a message, the absence of a message can be reliably interpreted as a fault (or silence). This allows the system to distinguish between a slow node and a crashed/faulty node, reducing the redundancy required for consensus.
*   **Practicality:** While theoretically superior in resilience, synchronous BFT is rarely used in global blockchains (like Bitcoin or Ethereum's consensus layer) because the Internet does not guarantee synchronous message delivery. Relying on synchrony introduces a severe security risk: if the network assumption is violated (e.g., during a DDoS attack), the safety of the protocol collapses [cite: 3, 6].

### 2.3 Probabilistic vs. Deterministic Finality
It is crucial to distinguish between BFT protocols that offer **deterministic finality** (e.g., PBFT, HotStuff, Tendermint) and those offering **probabilistic finality** (e.g., Nakamoto Consensus in Bitcoin).
*   **Deterministic BFT:** Once a block is finalized, it is theoretically impossible to revert it without a hard fork, provided $f < n/3$.
*   **Nakamoto Consensus:** Tolerates up to $f < n/2$ (50% attack) but only provides probabilistic guarantees. The probability of a reorganization decreases exponentially with block depth but never reaches zero [cite: 7, 8]. This trade-off allows Nakamoto consensus to operate in dynamic environments but sacrifices the "absolute" security of classical BFT.

---

## 3. Message Complexity: The Communication Barrier

Message complexity refers to the total number of messages exchanged to reach consensus on a single value. This is often the primary bottleneck for scalability in BFT systems.

### 3.1 The Quadratic Barrier ($O(n^2)$)
Classical BFT algorithms, most notably **Practical Byzantine Fault Tolerance (PBFT)**, exhibit a message complexity of **$O(n^2)$** [cite: 9, 10, 11].
*   **All-to-All Communication:** In PBFT, the leader broadcasts a proposal, and then all replicas must broadcast their votes to all other replicas to ensure that a supermajority has witnessed the same proposal. This quadratic explosion limits the practical size of PBFT networks to roughly 100 nodes [cite: 11, 12].
*   **Bandwidth Saturation:** As $n$ increases, the bandwidth required per node grows linearly, but the total network traffic grows quadratically. This creates a hard scalability ceiling known as the "scalability wall" for classical BFT [cite: 10].

### 3.2 The Dolev-Reischuk Lower Bound
A fundamental theoretical result, the **Dolev-Reischuk bound**, proves that any deterministic BFT protocol must exchange **$\Omega(n^2)$** messages in the worst case [cite: 13, 14, 15, 16].
*   **Significance:** This bound implies that no matter how optimized a deterministic protocol is, an adversary can always construct a scenario (e.g., by triggering view changes or silencing specific nodes) that forces the network to exchange a quadratic number of messages.
*   **Tightness:** Recent research (e.g., SQuad) has shown that this quadratic bound is tight even in partial synchrony, meaning we cannot theoretically do better than $O(n^2)$ for worst-case resilience [cite: 17, 18].

### 3.3 Linear Optimistic Protocols ($O(n)$)
To circumvent the quadratic barrier in practice, modern protocols like **HotStuff** introduced **optimistic linearity** [cite: 19, 20, 21].
*   **Mechanism:** HotStuff uses a star topology where replicas send votes only to the leader, who aggregates them (using threshold signatures) and broadcasts a quorum certificate (QC). This reduces the complexity in the "happy path" (no faults) to **$O(n)$**.
*   **The "Hidden" Quadratic Cost:** While HotStuff is linear in the steady state, its **view change** mechanism (replacing a faulty leader) or its **pacemaker** (synchronizing views) often retains a worst-case quadratic complexity [cite: 22, 23].
*   **Trade-off:** Protocols like **Jolteon** and **Ditto** acknowledge this reality by optimizing for the linear happy path while accepting the quadratic fallback for robustness during asynchrony [cite: 22, 24]. Thus, while $O(n)$ is achievable *optimistically*, the *theoretical worst-case limit* remains $\Omega(n^2)$.

---

## 4. Latency Theoretical Limits

Latency in BFT refers to the time elapsed between a client submitting a transaction and the transaction being finalized (committed).

### 4.1 Lower Bounds on Rounds
The theoretical lower bound for BFT consensus latency is generally accepted to be **2 message delays ($2\Delta$)** or **3 rounds** of communication, depending on the specific protocol structure and security assumptions [cite: 25, 26, 27].
*   **PBFT:** Requires 3 phases (Pre-prepare, Prepare, Commit), resulting in 3 message delays [cite: 12, 28].
*   **HotStuff:** Originally introduced as a 4-phase protocol to ensure linearity, but variants like **HotStuff-2** and **Jolteon** have reduced this to 2 phases ($2\Delta$) in the optimistic case [cite: 22, 29, 30].
*   **Fast Paths:** Protocols like **Zyzzyva** and **Aspen** attempt to achieve consensus in 2 rounds by allowing clients to receive responses directly from replicas. However, these "fast paths" are fragile and often require fallback to slower paths if there is any contention or fault [cite: 26, 31].

### 4.2 Optimistic Responsiveness
A critical theoretical property for low latency is **Optimistic Responsiveness**. This property ensures that the protocol can progress as fast as the actual network delay ($\delta$) allows, rather than waiting for the worst-case upper bound ($\Delta$) [cite: 5, 19].
*   **Significance:** Protocols without responsiveness (e.g., Tendermint in some configurations) must wait for a predefined timeout $\Delta$ even if messages arrive instantly. HotStuff was a breakthrough because it achieved responsiveness while maintaining linearity [cite: 19, 21].
*   **Limit:** The limit of responsiveness is the speed of light and network topology. No protocol can commit faster than the time it takes for a supermajority of nodes to exchange messages.

### 4.3 The Physics of Decentralization
There is a physical trade-off between decentralization (geographic distribution) and latency.
*   **Speed of Light:** For a globally distributed network, the Round Trip Time (RTT) is physically constrained. If nodes are spread across the globe, the minimum latency is in the range of hundreds of milliseconds regardless of protocol efficiency [cite: 32].
*   **Implication:** "Instant" global consensus is theoretically impossible. Blockchains must choose between being local (low latency, low decentralization) or global (high latency, high decentralization) [cite: 32].

---

## 5. Throughput vs. Latency Trade-offs

Throughput (Transactions Per Second, TPS) and latency are often inversely related in BFT systems due to the mechanics of batching and pipelining.

### 5.1 The Batching Trade-off
To achieve high throughput, BFT protocols batch multiple transactions into a single block.
*   **Mechanism:** Amortizes the cost of consensus (signatures, message overhead) over thousands of transactions.
*   **The Limit:** Increasing batch size improves throughput up to the limit of bandwidth or CPU verification speed. However, it degrades latency because early transactions in a batch must wait for the batch to fill and for the consensus rounds to complete [cite: 33, 34].
*   **Theoretical Tension:** There is no single optimal point; minimizing latency requires small batches (or no batching), while maximizing throughput requires large batches.

### 5.2 Pipelining and Parallelism
Protocols like HotStuff introduce **pipelining**, where the voting phase for block $B_n$ serves as the preparation phase for block $B_{n+1}$ [cite: 19, 28].
*   **Benefit:** Allows the network to utilize bandwidth continuously rather than waiting for a block to finalize before starting the next.
*   **Limit:** Pipelining increases the complexity of recovery. If a leader fails, the "pipeline" breaks, potentially causing a significant latency spike (hangovers) as the chain recovers [cite: 35].

### 5.3 Separating Data from Consensus (DAG-based BFT)
Recent theoretical advancements (e.g., **Narwhal, Bullshark, Mysticeti**) have shifted the paradigm by separating data dissemination from metadata ordering [cite: 16, 35, 36].
*   **Concept:** Nodes continuously broadcast transaction data (forming a DAG) without waiting for consensus. Consensus is then run only on the *references* (hashes) to this data.
*   **Theoretical Limit:** This architecture allows throughput to approach the **theoretical limit of the network bandwidth**. If the network link is 1 Gbps, the protocol can theoretically process 1 Gbps of transaction data, limited only by the ability to order the small metadata headers [cite: 35].
*   **Cost:** These protocols often incur higher latency (due to the DAG construction rounds) and higher message complexity ($O(n^3)$ in some naive implementations, though optimized to $O(n^2)$) [cite: 37, 38].

---

## 6. The Blockchain Trilemma and CAP Theorem

The theoretical limits of BFT are often encapsulated in the **Blockchain Trilemma** and the **CAP Theorem**.

### 6.1 The CAP Theorem
Applied to distributed ledgers, the CAP theorem states that a system can only provide two of the three: **Consistency**, **Availability**, and **Partition Tolerance** [cite: 39, 40].
*   **BFT Context:** In the presence of a network partition (P), a blockchain must choose between halting to preserve the ledger state (Consistency - e.g., Cosmos/Tendermint) or allowing forks to continue processing transactions (Availability - e.g., Bitcoin/PoW).
*   **Limit:** It is theoretically impossible to guarantee both safety (no forks) and liveness (always accepting transactions) during a partition in an asynchronous network [cite: 40].

### 6.2 The Scalability Trilemma
The trilemma posits that a blockchain cannot simultaneously optimize **Decentralization**, **Security**, and **Scalability** [cite: 41, 42, 43].
*   **Mathematical Formulation:** Recent work has attempted to formalize this as a constant product formula, suggesting that increasing one variable necessitates a decrease in the others [cite: 41, 44].
*   **Interpretation:**
    *   *Scalability* (Throughput) requires minimizing the number of messages or nodes involved in validation.
    *   *Decentralization* requires maximizing the number of nodes ($n$).
    *   *Security* requires high fault tolerance ($f$).
    *   Since message complexity is at least $\Omega(n)$, increasing $n$ (Decentralization) without sacrificing Security ($f$) inevitably increases communication overhead, thereby reducing Scalability [cite: 41].

---

## 7. Conclusion

The theoretical limits of blockchain Byzantine Fault Tolerance are defined by rigid mathematical and physical boundaries.

1.  **Resilience:** The hard limit for partial synchrony is **33% fault tolerance** ($n \ge 3f+1$). Any protocol claiming higher resilience must assume synchrony, which introduces significant safety risks.
2.  **Complexity:** The **Dolev-Reischuk bound** dictates a worst-case communication complexity of **$\Omega(n^2)$**. While optimistic linear protocols ($O(n)$) exist, they cannot escape the quadratic penalty in adversarial scenarios.
3.  **Latency:** Latency is bounded by **2 message delays** and the **speed of light**. Global consensus cannot be instantaneous.
4.  **Throughput:** Throughput is theoretically limited only by **network bandwidth** and **CPU verification** speeds, provided the protocol separates data dissemination from consensus ordering (as seen in modern DAG architectures).

Future advancements in BFT will likely not "break" these limits but rather navigate the trade-off space more efficiently—optimizing for the "happy path" while maintaining rigorous safety guarantees for the worst case.

---

### References
[cite: 2] GeeksforGeeks. (2025). *Byzantine Fault Tolerance in Distributed System*. [cite: 2]
[cite: 9] MDPI. (2023). *PBFT Consensus Algorithm*. [cite: 9]
[cite: 28] Medium. (2024). *Practical Byzantine Fault Tolerance (pBFT)*. [cite: 28]
[cite: 3] Wikipedia. *Byzantine fault*. [cite: 3]
[cite: 39] MDPI. (2023). *Theoretical bases of blockchain consensus mechanisms*. [cite: 39]
[cite: 7] arXiv. (2025). *Speed and transaction throughput*. [cite: 7]
[cite: 25] ResearchGate. *TetraBFT: Reducing Latency*. [cite: 25]
[cite: 45] Lamport. *Lower Bounds on Consensus*. [cite: 45]
[cite: 10] arXiv. (2023). *Scalability problems of PBFT*. [cite: 10]
[cite: 1] arXiv. (2022). *BFT protocols survey*. [cite: 1]
[cite: 32] Reddit. (2025). *Latency vs Security: The Physics Tradeoff*. [cite: 32]
[cite: 9] MDPI. (2023). *Message complexity reduction*. [cite: 9]
[cite: 5] LIPIcs. (2025). *Optimal responsively proposing rotating-leader protocol*. [cite: 5]
[cite: 26] arXiv. (2026). *Aspen: Leaderless BFT protocol*. [cite: 26]
[cite: 16] GitHub. *Mysticeti: Reaching the Limits of Latency*. [cite: 16]
[cite: 6] LIPIcs. *Good-case latency of Byzantine agreement*. [cite: 6]
[cite: 13] Decentralized Thoughts. (2019). *Dolev-Reischuk lower bound*. [cite: 13]
[cite: 14] arXiv. (2022). *Dolev-Reischuk lower bound BFT message complexity*. [cite: 14]
[cite: 15] LIPIcs. *Communication complexity of byzantine agreement*. [cite: 15]
[cite: 12] Shapkarin.me. *BFT Consensus Algorithms Comparison*. [cite: 12]
[cite: 31] Vavala.net. *Speculative BFT protocols*. [cite: 31]
[cite: 33] arXiv. (2024). *Throughput-latency tension*. [cite: 33]
[cite: 35] Cornell. *Autobahn: High-throughput BFT*. [cite: 35]
[cite: 40] MDPI. *CAP theorem for autonomous consensus*. [cite: 40]
[cite: 41] MDPI. (2024). *Blockchain Trilemma mathematical proof*. [cite: 41]
[cite: 44] PLOS ONE. *Blockchain trilemma formulation*. [cite: 44]
[cite: 43] Medium. (2018). *Scalability Trilemma*. [cite: 43]
[cite: 11] Bytepawn. (2025). *PBFT message complexity*. [cite: 11]
[cite: 37] Emergent Mind. (2025). *Asynchronous BFT*. [cite: 37]
[cite: 38] Computer.org. (2025). *JUMBO: Scalable Asynchronous BFT*. [cite: 38]
[cite: 8] dYdX. (2025). *Byzantine Fault Tolerance Limitations*. [cite: 8]
[cite: 46] arXiv. (2025). *Byzantine Fault Tolerance in Blockchain*. [cite: 46]
[cite: 16] GitHub. *Dolev-Reischuk Bound*. [cite: 16]
[cite: 47] EPFL. *Dolev-Reischuk bound tight in partial synchrony*. [cite: 47]
[cite: 17] LIPIcs. (2022). *Byzantine Consensus Is Θ(n²)*. [cite: 17]
[cite: 4] Decentralized Thoughts. (2019). *Impossibility of BA for n<=3f*. [cite: 4]
[cite: 1] arXiv. (2022). *BFT Consensus Survey*. [cite: 1]
[cite: 18] LIPIcs. *Quadratic worst-case message complexity*. [cite: 18]
[cite: 19] Malkhi. (2018). *HotStuff: Linear View-Change*. [cite: 19]
[cite: 20] Medium. (2023). *Understanding HotStuff*. [cite: 20]
[cite: 29] arXiv. (2023). *HotStuff-2*. [cite: 29]
[cite: 30] Decentralized Thoughts. (2023). *HotStuff-2*. [cite: 30]
[cite: 34] arXiv. (2025). *Security-latency analysis*. [cite: 34]
[cite: 36] ResearchGate. (2025). *Delay analysis of BFT consensus*. [cite: 36]
[cite: 21] Murat Buffalo. (2019). *HotStuff BFT Consensus*. [cite: 21]
[cite: 27] arXiv. (2024). *Theoretical lower bound BFT consensus*. [cite: 27]
[cite: 22] FC22. *Jolteon: Quadratic Pacemaker*. [cite: 22]
[cite: 24] arXiv. (2023). *Ditto: Hybrid BFT*. [cite: 24]
[cite: 23] arXiv. (2021). *Quadratic pacemaker in DiemBFT*. [cite: 23]

**Sources:**
1. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZpUZl_Lp0MQvNeFNpqmMpbpqLSdmuKJYvrUw4noxPAq8I4oRk9POxQXzeYFLg52HrPGeD54JMgrGtrV7hGT-hebHPofCZJfp_W7nsFccGsrCvPMzv4bsP)
2. [geeksforgeeks.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC7_MUdEZmknNo5ItehtYls4iaO16BYsfM1lu5v2B4HiuB9B6_OiOZfQMxPA6VeejR8pjpKMJVmtZFTF2yFa542uaWdo1nYUeZFDZaks1WSbuHgbsIU3JzOjCGtaCvXTL7QPR5wAgOYzjs1IhdPVTRUQjPZhjpD4F-HBW_GzUfxdGSPSptCK2PhbJezE-n1gjP)
3. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbG7bht0731MMkm6sLQqn4bKWQ0KBr1jKGSB7LqYmFUmCsjtgUvsbzzRxnN38_9EtLNwXkeRaZ_TcEy6aPUrQnNkNj-7KvS3O46Ot3i2kkteu8q5A6hhOYAfpvhSglo8dV2g==)
4. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGU353O9GQL2cWPxcw8t93sWJAZ442Q7fBOJJ2IMjIbxgpZFJaT5E9TFr-GKpUu_azqrFuegb_u2f2GuNXMtZ6s3C5DIVjLgs9t73Pc1iC0rH_Mc1rCChTua1AN1XAvkkF_xXrS-vbH1XdNwHMtwMjRfIG62RtgvyBcJOC-jeN3MlEdw4qYuz6A5Vt_yqrYCMXIb1U8P8AUx12OtHq3PKIYkdvMBgsgmNGBM1F00eEBjHfAEFmBnM0yJ20=)
5. [dagstuhl.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjIS5t2km9KL6Jjv3DlsRVADDLZJENBYxR6gFIO-SnfjG_xsbOHW9VzFHxDyqBIgI6fjBo2TLIxd8S2PPKGSRcfskpKSd_rrws3ltfyLl4Y7laTpHq2F4n9A8VK2xCE3RYrAxWuCYLWtPRkH3IcQgQV-ABcAd9KItd8dsreFgkMmZ--zBodvDlBSy0EaDL77aig-J1HcgqX_GHleM69EcHdjekxa989yY=)
6. [d-nb.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfFZJzYt7mGI7-vJx8zHPqH_GRs5s4S5ESxv0Dq2opAmL9pg5MVI5KwoHGAqQhfg3k1ZMhK3Aaso9rVtADgL409tNFwbZRAY9D-GV_4SCYwnypqHI=)
7. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGO407s37XYU7EaWm3AuG7U5BT2FNt7EJhq3Zvj8q1ePgZpMkgyRPxr0UpPRmSEqzz4weQNP7-juhIy-215aiD5PwuFbFAQrmPJLOFYZqpvfSuCULr)
8. [dydx.xyz](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbQDe6W3-G2BoZdxHnkffru5yZWOvZbRcvUNPAJW_DrncHnv90GjURdTnhxM5WmJd98Lb3GBS2F29Ki_oR9kArFC-XbVki9SEH0IYg8O5MIH-yyKH9pX8h12dWcebTp7CJFB0IRGcUgkrKka2XNehHqByI)
9. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfrLLDzz1JJAH4D6Gw07u5PPJMQZDP21oz8T1ROaYS0FtVJk7vQRaDfAq_1KK78PfskPn0DT5tPRE8-X6Hral6voOM1SiaJSLtHOGOebsUuTEklBP_MbSQvHq6mLna)
10. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwUjsGciZkAAzpy2Dol9lhZh7KJZGHc6dCrGn3zfrdGJiXJSmTucVetJIzx6ftqsJj2ekVWMTeubSnvWuMsAR-1sDZtGb3VRNbK7AFsU-3XOqC_5AK)
11. [bytepawn.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpAJuBaOfL63jGvREo2SaWeytgUDgETi-m8LWcGf0x_-A5MOrvPesq1I86KYqblY22tLWgsZRYEnHdvI3Zp4OcpIPCXrDBjhtv3MpWFAMeT2Nj2YQE_CJKslIQwS350nxlJ_O_0TelUtXxyWFJQatRLlA=)
12. [shapkarin.me](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHicSdxcy3bXcmsnzR8gGX4bMgS8yjZ4nMrakSEitDgMic6PNJ8AAY2817I9bfu6Mt_ydLxTpaRJHOkj4Rsfp37qAaraI6GEyXmmZ0Q_NMnUn04FzfepF2WihGm7kf012zzlhO_2lydcwjiSgjc)
13. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGC5yYz87q2R89o1EO6pzXop54ig37IjNSuWtsJ-SwqBL6KPPL4qxJ0dwjFHdf6bPu96hwu95x7rHGV1WdBi_aMhdrX4pYVTb5sWIWobkbqDs3yQSTOn3YHEIoEz8CfFzQhdSPLyFeuxZ_VoGkeYwhtIoDY76RGnyGs2Dzl6AXOzGwJiSaCNyondRBOtSBMQvFiYTmr5A==)
14. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG__48Px0LCX06ZXtO0yIJAgBOwGHjzER_ALX3JyVG7XOa8KcClcHbnZQq_0aGpkv79vN0uuuVnc-lYPxLCHNA0tyJjWC5tmHYpK13VkhlaxG590GUb)
15. [dagstuhl.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs-YGlnAFm37XLCnWDF82xbklN3McbbWsj3DpFB9zPCC32XfUwEY9Ru1_BM4roexXADFBFSbictbaLOvuW1vwj_twJulEfaAltBmCBmiMagNW1iKBdEfXdjmeKcbdwWXbMUvaGmrPZ5v3dN_RmEa2u9GM5QOvH9ymNBPf6iW0=)
16. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbXEVgC1BYzoCKCIYo4pDQ41RJogFazpzXmjUVMZk3ZPzJlvGvSCG_r32UTimB9rvCB6OPg7PfVZHzxiporUIlsgB9p3Nww4KJcsIWZTMHvteZwG-MkCuXFTYt0xP-DI28Sxs=)
17. [dagstuhl.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbSZok3FPS2aBeLjG4GVPIH_xb5rB2OkhQlICrB6fJyzAC8P-jYLZhTm0LQm3UzNCE9BjJSI7bUI__BxTA7p0BY8iAhPwgqvtbJO3plL1MgssOfeia2XQgnRpN-QTzWhLTTTcE9fMk8sJKKfx3uStZ)
18. [dagstuhl.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgZTeyUe6SecGIGUDHGnZpA7-qfow9POTZ8wmjEQIg3tNTAKgnIDaR-fjEkTjd0TmekCemlpGsuEiD78tGFs7_8cqSduJ81eB7pzFwc2LSrT2MMPiZShDT2YGPGwr891pTCSlS1Wnb-9w7lLZsmEkYoCQqhmR95pc7oGbg)
19. [malkhi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_inCJx7HAA_3e0-5k9P5p6qiOiVCqjuCrNl0E28r15ilzVaBnT1qstsPctPIi39sTJOa2knbixlhR2rgoGWt4HjRXvhPGdTPV7fRyjMTlHf7llJalrkk93G7zFDEqoX2ZZ4bjWg==)
20. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVTwO846UV5gX1R7UVTGG0JKDv1texyXg5ZPE81dxZTxmjELFldRJnG7wlO04-Fwtwn4F4ETY2BiO5PvoGd3qjokic9Kusw_zud1M0Q_KqxkgdQqzKoDjncW2KRxUsLpxa5bSC7w6u7vpLzA1WQJTX-lpDq3gq0nKBJibWj3QgB2BEkRSSn_TuWmYhQT-bvfXPvDdVuh9mcw==)
21. [blogspot.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYMtSx-Fw30K_zh1OoQr_nXlkxQ15pS7IMvnmmukAd0W4QqaKiDgpcEpe_gg6DA80RG5ElddrQvGpVfU7h5xsBwb3fVz4eD4bhJi6cQkMon_BttAMd5Y_MBYCIBTt5s4BFbof4BrwcbPEQJnq6nFnhPQ_Tw5_6z-fkQCeSniYgS3eq4jY=)
22. [ifca.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIOKwYH2p-ZsVbBugnXT5JqKvBSUAqtp4PDynngqpeRsjLizk8s6GNkMN8tpm2SEW7nBxiMurIbh6f9L-Ehy25eWAP8Kf3Wau-8wX6zwIUMKYg9Q2t-VaNSrjdv839kg==)
23. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBLtHNtdsYLT1rKwW-Brbd6JYNEywngjb916MU48HPksLzCTauuc9nymuTnuMcOdfL-3rnmxcsCM1hdZ82wnIWE9R6uSyBNpssdl0QLqmkzu8AMSOi)
24. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoYVY1WEhkHzDQJU1Gx4IDzjUN3o6Lzoq87wfb1himOKx-LHGki7JZq58Mt7fEM8hdAmlJ7Tx4aVKF5LvPpKyL1UtQKRGrAobSbOYreFLxQunLC1ibs3qU)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE34bfdvytMKhl7oVY59e6PymqKrEYKpCYm0FEK48HbeqdpUHnSTrZh6TrFvsmQcjBLVOtUvD2yOwXxSdrnrcVJM_9m9LCFRXp3ID60XCc7dlTN1o9uLpQwSy0g_LI4hF_WC3UAvUFrAN4JOogOwODs8_OxDIuCNi-Nofs-Q7B45f3-5FXk3LSt5Gaa-iyIpvHfnVtRqmY2BNqxq8rDRZV20oDlDFRSXxHFTCrrw4Bxl03qGg5Ej7Y=)
26. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPxFUIx44eV5-OT83NH4zbcnM2rug0hKA-71zAdX057fpHzGK8YJT-j7bY889fEXIAAuHSLYSvi1Oz4-VWBL3B3KzMrr9mw07V3TfyAJ8TyWVgPS5Tn9OY)
27. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5SFHJQ8ocgNEO0cOsHLvqq5dg00c2dXpaf49ra9q6TY985K37Mm82D3Z1MgWSOlHkZyHbo2fbdzxp-ztnKr_YHKXt98qi1GA0TmdpxFkISSmDpbJj)
28. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM_8GFPaHHTSnV53uzzgBu3MTjH8-j7IedKffT_OjaMiV17Dd25ZJdmDfEYEmpBe4s3fKEoqO3LkhuRM2EcgIMnm12VAuodXB2p18Q2qDB1137hTHJG8DRUKMrqEvadDeACGPaD0jaxNPnflsl_BrGOGlTBkcT5assQkpOWQ7AhIVTm23snqhQPLCuBtw8_iz6G_VkkVGYnCdRXR1TyQiTEzRZnIzU7gWKYJ3DeCqO9r8RJQxkk1g=)
29. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9gkEUswbW0opROt7nJ2eDtqJMBgb16kPxO1wyWC0rHstW7-k5PbukTV-igU6ddabrBJMuo3Uo60IxvLZ3OwxrqpbaQGEeZlG6vKEx9EpIcKjh-Kj3)
30. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiHRSrsk6qz7_pbTeiVi-19fjwlKUQzn8zeCS-9WF_LsfGYI1PeQqaYabrEPf6F4dngkKh2sFCQqjyuI7Kxun9ivY2dTsy2sZNPCBSyxFTTyGbVBCenCgIss5d5JHFIn8sAabaXIEeQybuSueMbFT-0aAq)
31. [vavala.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0CzvJHjffrsuPfZ4CSL7AmbtFx2y1RYM4BktJYt8jquYGB1MDS8e3OjAvYXRpB4YMQ9S_M38VsMVBYKu7OmhcA_nF5coW-wsLvaQMTt6dXiCE9oj58teyMIAJU83XWgCbNg==)
32. [reddit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc_6QjCkpPQjI2YqJyPABTO8LWVVBLfgRItsNocVRFEV_qezMEm1zMv7dbdlZsfSyO7yxe3hLa-zExfiDJSOTp7-yLwdqyi1U3Sm_ItFvHAhlu6DFXMxwAXtnT6I3_soywsLWMfmHn8mQ4CzVpDKEa_GYh3994qTnCyyO8FaIx7VWJOgvw31R3Ne720QBW0XmOtqCcmsaFdsg=)
33. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsvzbcIw-JMni5yF7fNXuZ7_vxHiMS3vOvjAEAPKsHPHO3j2oA9xvkz9inGaLiVCQ270mDVrt-rrgpH_qXQ-AiyCxxDJM7-tHi0UEkYy8LK-u1DpId1A2t)
34. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELY5TorT8jSLtPHbtTKbXd5yWEbrWBPr17dp-x4_SvTyCmBetN_75nSDO-X_lecjGR6vsvQmR-SreGN56BgD5mm7DBo0-Rz3Cmn_Z_dMKhXV9JXSQb)
35. [cornell.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGo0xFCB1zQtzlMjk9y-6pC3_3-YfYsvoqh7ZoCUns6OOjLgS6LlsdilvBssRS8yi7zpauvwnj8eU8PnqBO4Oq5RGWUbXjYwM1pChBbXXX_S58Da8XxMk8DLFoMrAtRbqF-_-K3Xj0UeC12O3njlsDkGg==)
36. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELinuUx6jfzbOEbO45h6Gh1xYwaslzuCF9zKbmvmOGDy8k8g_0ixGbVWjZFrSOX_j-D0k9S0d9aPVDRIrkM8elRUVvNxVoaPsA9CsKujoeg5KoMVKMTbrhfy9O6XeEVfGetuG0z8zeDcIpEZwQ8DytN7yQanUO6diHcdfnWtmoKO4NkM1QeXoSG5TBOAN0V3M8VOt9v3DWZVc8hmMlDndjeZyyQhDZxkQzNLK0T97y7h8g8gCHFQ==)
37. [emergentmind.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEH18ZdJcchKz3X7n5bBmOdQMM9vAByLBD0mCGq61O0chJTcRo5-cgVbIRYqpeRM8dRisUGh3CrXVqKkKG4jlr6sAYim1M97bXlGpkyuglogocVMoH75nxfqgOl7AAcK1KzGB2ZbLmmcPvic2zUmPaOvml9LdLfi8Jv4gKywXmfRrhxh3U=)
38. [computer.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4pV7Dj5h3mFJ1EkJCPNvAhHOmN_zJ_FIuMqfN0-aZ1xQ7pDq6fucvcvnNyN4EVXIrS7pGnESTMVy3ppmg2dGK1SvOYSmPIjIoYionOOei_-olvbPL7ooHzM8ALtU7XEoyIurzZMcGZcmroDGYIg--_lB1hD34qivpGg==)
39. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiIBe5afSewTrim-WsdAVFHBWOGovONZ4uzjTUXlGcKz-IggfKCHzSIF1DIxm7r2VsupWfKb6gLa58rSCRY5D2SyDEy36vFE4jKQ-X142qp39AgyLgWTfRBga5p-ei)
40. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKXT2e5y1L6jv-jC0_kPaiqkt9eNIjXipL_rQ1YRBkACpie0A6Rb_bfZdRnU7uz_wKkME7QNu3L9WtHuA6pWutZZlOxNyteqBFQGjESjCoWD-LDnObMB4CFuHKqw==)
41. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA8-B6igtJdoi1Vb5eMKCo6RU_VZHXKonk1L78vVdjN7Mi8ZVwbg1UlIwn1WkXbGwIGDOYH3pEjGDFwYhhM2wHuPKmnk0O7160ZvfgNXtnfF8Ge8fkeJAMm4N3)
42. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlKnrCqf1NbrxCfxCn4qHyG83KZrxs0UFHbY2HZs7xT9nvPSCR3Rf00ilHI2cH6NwuWJ2fJCjicJf2x0v0zNLqIWNfxgkQl0bSeqytd4k12a9OjSuO9ymMfNJ_CRK4Z6rSGOB-tkoG)
43. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGrl2ZhBnEc0VxVEBNL2jjwOcumbNsxLxT6tn7KoFUqKidKrJcDWZ09rkRfvnIfHAew8EiAGNndfuP8kpaV7JB6HldSamPGHLSAKm6-khvszVnJbnK4uD1QqeExkHMDquUdJIW-Unfbd5c1-Ataisp_z2GLevNI5eKEpP_CDyM8zLsMEjbxj3_4erknKbSOAw8j3_PwueZvErYBX7n5lVqzWfVD3Oq)
44. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEH4-Y716YUT4q20y_G16RMqTUPtf3tEYoKDpegJBZ3CbSNB-QuT9_SotAESRFJexeU_mQZ64cD-954gXLdbZ6-lSuNnO89KCsKNMg172sTthhJyLsWLC_0IH9DYNbXgIrlfPulvk_xXvyI0KV2Gln7W5knVcoUfza1YfpQvyw=)
45. [azurewebsites.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGskQ9IO-Vrx5_MIV6XiCGRmmgF7pPb3cjq6D9K_OUFjko_ZbNHTHUbCUK_zK-McvjfIDsvqybg-ilORM3biTAunT1gRxyoOxSDWQZIYrHT8ZFznmKWLJnvjzr1blsJ-AEUGwMAfwhMO4oVWw==)
46. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG23bBOhNvcFnBn2iQDKLDyzpJ7nn1_bPM2y4JHCQ7Igzy56x-zPRvF-2ZTW7KKHFpAOLooIZgJz4ltIso4zmEC6cTnDgYYQIr-JFKRamqqjlN5r7Fr)
47. [epfl.ch](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyOhpgTLY7yhjA_ZCRFXzyV-otL2UuljgscS4XL6CdnMJ_ZOVsHOlVcbX7Oor6BSR9LdOu6_0qE2qKIgLEq0egiho9zAL5te_chvmTM2NxppcijL2_xdTkkML-WROi8JTsYmnaNecNX3dM9VxMdQ0f4AhYK-LAQGcJREdWmbU-R8uQ61u2)


## Annotations
Annotation(end_index=3461, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZpUZl_Lp0MQvNeFNpqmMpbpqLSdmuKJYvrUw4noxPAq8I4oRk9POxQXzeYFLg52HrPGeD54JMgrGtrV7hGT-hebHPofCZJfp_W7nsFccGsrCvPMzv4bsP', start_index=3452)
Annotation(end_index=3651, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC7_MUdEZmknNo5ItehtYls4iaO16BYsfM1lu5v2B4HiuB9B6_OiOZfQMxPA6VeejR8pjpKMJVmtZFTF2yFa542uaWdo1nYUeZFDZaks1WSbuHgbsIU3JzOjCGtaCvXTL7QPR5wAgOYzjs1IhdPVTRUQjPZhjpD4F-HBW_GzUfxdGSPSptCK2PhbJezE-n1gjP', start_index=3636)
Annotation(end_index=3651, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbG7bht0731MMkm6sLQqn4bKWQ0KBr1jKGSB7LqYmFUmCsjtgUvsbzzRxnN38_9EtLNwXkeRaZ_TcEy6aPUrQnNkNj-7KvS3O46Ot3i2kkteu8q5A6hhOYAfpvhSglo8dV2g==', start_index=3636)
Annotation(end_index=3651, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGU353O9GQL2cWPxcw8t93sWJAZ442Q7fBOJJ2IMjIbxgpZFJaT5E9TFr-GKpUu_azqrFuegb_u2f2GuNXMtZ6s3C5DIVjLgs9t73Pc1iC0rH_Mc1rCChTua1AN1XAvkkF_xXrS-vbH1XdNwHMtwMjRfIG62RtgvyBcJOC-jeN3MlEdw4qYuz6A5Vt_yqrYCMXIb1U8P8AUx12OtHq3PKIYkdvMBgsgmNGBM1F00eEBjHfAEFmBnM0yJ20=', start_index=3636)
Annotation(end_index=4307, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZpUZl_Lp0MQvNeFNpqmMpbpqLSdmuKJYvrUw4noxPAq8I4oRk9POxQXzeYFLg52HrPGeD54JMgrGtrV7hGT-hebHPofCZJfp_W7nsFccGsrCvPMzv4bsP', start_index=4298)
Annotation(end_index=4579, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGU353O9GQL2cWPxcw8t93sWJAZ442Q7fBOJJ2IMjIbxgpZFJaT5E9TFr-GKpUu_azqrFuegb_u2f2GuNXMtZ6s3C5DIVjLgs9t73Pc1iC0rH_Mc1rCChTua1AN1XAvkkF_xXrS-vbH1XdNwHMtwMjRfIG62RtgvyBcJOC-jeN3MlEdw4qYuz6A5Vt_yqrYCMXIb1U8P8AUx12OtHq3PKIYkdvMBgsgmNGBM1F00eEBjHfAEFmBnM0yJ20=', start_index=4570)
Annotation(end_index=4803, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbG7bht0731MMkm6sLQqn4bKWQ0KBr1jKGSB7LqYmFUmCsjtgUvsbzzRxnN38_9EtLNwXkeRaZ_TcEy6aPUrQnNkNj-7KvS3O46Ot3i2kkteu8q5A6hhOYAfpvhSglo8dV2g==', start_index=4791)
Annotation(end_index=4803, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjIS5t2km9KL6Jjv3DlsRVADDLZJENBYxR6gFIO-SnfjG_xsbOHW9VzFHxDyqBIgI6fjBo2TLIxd8S2PPKGSRcfskpKSd_rrws3ltfyLl4Y7laTpHq2F4n9A8VK2xCE3RYrAxWuCYLWtPRkH3IcQgQV-ABcAd9KItd8dsreFgkMmZ--zBodvDlBSy0EaDL77aig-J1HcgqX_GHleM69EcHdjekxa989yY=', start_index=4791)
Annotation(end_index=5509, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbG7bht0731MMkm6sLQqn4bKWQ0KBr1jKGSB7LqYmFUmCsjtgUvsbzzRxnN38_9EtLNwXkeRaZ_TcEy6aPUrQnNkNj-7KvS3O46Ot3i2kkteu8q5A6hhOYAfpvhSglo8dV2g==', start_index=5497)
Annotation(end_index=5509, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfFZJzYt7mGI7-vJx8zHPqH_GRs5s4S5ESxv0Dq2opAmL9pg5MVI5KwoHGAqQhfg3k1ZMhK3Aaso9rVtADgL409tNFwbZRAY9D-GV_4SCYwnypqHI=', start_index=5497)
Annotation(end_index=6132, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbQDe6W3-G2BoZdxHnkffru5yZWOvZbRcvUNPAJW_DrncHnv90GjURdTnhxM5WmJd98Lb3GBS2F29Ki_oR9kArFC-XbVki9SEH0IYg8O5MIH-yyKH9pX8h12dWcebTp7CJFB0IRGcUgkrKka2XNehHqByI', start_index=6120)
Annotation(end_index=6132, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGO407s37XYU7EaWm3AuG7U5BT2FNt7EJhq3Zvj8q1ePgZpMkgyRPxr0UpPRmSEqzz4weQNP7-juhIy-215aiD5PwuFbFAQrmPJLOFYZqpvfSuCULr', start_index=6120)
Annotation(end_index=6692, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfrLLDzz1JJAH4D6Gw07u5PPJMQZDP21oz8T1ROaYS0FtVJk7vQRaDfAq_1KK78PfskPn0DT5tPRE8-X6Hral6voOM1SiaJSLtHOGOebsUuTEklBP_MbSQvHq6mLna', start_index=6675)
Annotation(end_index=6692, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpAJuBaOfL63jGvREo2SaWeytgUDgETi-m8LWcGf0x_-A5MOrvPesq1I86KYqblY22tLWgsZRYEnHdvI3Zp4OcpIPCXrDBjhtv3MpWFAMeT2Nj2YQE_CJKslIQwS350nxlJ_O_0TelUtXxyWFJQatRLlA=', start_index=6675)
Annotation(end_index=6692, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwUjsGciZkAAzpy2Dol9lhZh7KJZGHc6dCrGn3zfrdGJiXJSmTucVetJIzx6ftqsJj2ekVWMTeubSnvWuMsAR-1sDZtGb3VRNbK7AFsU-3XOqC_5AK', start_index=6675)
Annotation(end_index=7009, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpAJuBaOfL63jGvREo2SaWeytgUDgETi-m8LWcGf0x_-A5MOrvPesq1I86KYqblY22tLWgsZRYEnHdvI3Zp4OcpIPCXrDBjhtv3MpWFAMeT2Nj2YQE_CJKslIQwS350nxlJ_O_0TelUtXxyWFJQatRLlA=', start_index=6995)
Annotation(end_index=7009, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHicSdxcy3bXcmsnzR8gGX4bMgS8yjZ4nMrakSEitDgMic6PNJ8AAY2817I9bfu6Mt_ydLxTpaRJHOkj4Rsfp37qAaraI6GEyXmmZ0Q_NMnUn04FzfepF2WihGm7kf012zzlhO_2lydcwjiSgjc', start_index=6995)
Annotation(end_index=7258, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwUjsGciZkAAzpy2Dol9lhZh7KJZGHc6dCrGn3zfrdGJiXJSmTucVetJIzx6ftqsJj2ekVWMTeubSnvWuMsAR-1sDZtGb3VRNbK7AFsU-3XOqC_5AK', start_index=7248)
Annotation(end_index=7488, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbXEVgC1BYzoCKCIYo4pDQ41RJogFazpzXmjUVMZk3ZPzJlvGvSCG_r32UTimB9rvCB6OPg7PfVZHzxiporUIlsgB9p3Nww4KJcsIWZTMHvteZwG-MkCuXFTYt0xP-DI28Sxs=', start_index=7466)
Annotation(end_index=7488, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGC5yYz87q2R89o1EO6pzXop54ig37IjNSuWtsJ-SwqBL6KPPL4qxJ0dwjFHdf6bPu96hwu95x7rHGV1WdBi_aMhdrX4pYVTb5sWIWobkbqDs3yQSTOn3YHEIoEz8CfFzQhdSPLyFeuxZ_VoGkeYwhtIoDY76RGnyGs2Dzl6AXOzGwJiSaCNyondRBOtSBMQvFiYTmr5A==', start_index=7466)
Annotation(end_index=7488, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG__48Px0LCX06ZXtO0yIJAgBOwGHjzER_ALX3JyVG7XOa8KcClcHbnZQq_0aGpkv79vN0uuuVnc-lYPxLCHNA0tyJjWC5tmHYpK13VkhlaxG590GUb', start_index=7466)
Annotation(end_index=7488, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs-YGlnAFm37XLCnWDF82xbklN3McbbWsj3DpFB9zPCC32XfUwEY9Ru1_BM4roexXADFBFSbictbaLOvuW1vwj_twJulEfaAltBmCBmiMagNW1iKBdEfXdjmeKcbdwWXbMUvaGmrPZ5v3dN_RmEa2u9GM5QOvH9ymNBPf6iW0=', start_index=7466)
Annotation(end_index=7982, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbSZok3FPS2aBeLjG4GVPIH_xb5rB2OkhQlICrB6fJyzAC8P-jYLZhTm0LQm3UzNCE9BjJSI7bUI__BxTA7p0BY8iAhPwgqvtbJO3plL1MgssOfeia2XQgnRpN-QTzWhLTTTcE9fMk8sJKKfx3uStZ', start_index=7968)
Annotation(end_index=7982, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgZTeyUe6SecGIGUDHGnZpA7-qfow9POTZ8wmjEQIg3tNTAKgnIDaR-fjEkTjd0TmekCemlpGsuEiD78tGFs7_8cqSduJ81eB7pzFwc2LSrT2MMPiZShDT2YGPGwr891pTCSlS1Wnb-9w7lLZsmEkYoCQqhmR95pc7oGbg', start_index=7968)
Annotation(end_index=8168, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_inCJx7HAA_3e0-5k9P5p6qiOiVCqjuCrNl0E28r15ilzVaBnT1qstsPctPIi39sTJOa2knbixlhR2rgoGWt4HjRXvhPGdTPV7fRyjMTlHf7llJalrkk93G7zFDEqoX2ZZ4bjWg==', start_index=8150)
Annotation(end_index=8168, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYMtSx-Fw30K_zh1OoQr_nXlkxQ15pS7IMvnmmukAd0W4QqaKiDgpcEpe_gg6DA80RG5ElddrQvGpVfU7h5xsBwb3fVz4eD4bhJi6cQkMon_BttAMd5Y_MBYCIBTt5s4BFbof4BrwcbPEQJnq6nFnhPQ_Tw5_6z-fkQCeSniYgS3eq4jY=', start_index=8150)
Annotation(end_index=8168, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVTwO846UV5gX1R7UVTGG0JKDv1texyXg5ZPE81dxZTxmjELFldRJnG7wlO04-Fwtwn4F4ETY2BiO5PvoGd3qjokic9Kusw_zud1M0Q_KqxkgdQqzKoDjncW2KRxUsLpxa5bSC7w6u7vpLzA1WQJTX-lpDq3gq0nKBJibWj3QgB2BEkRSSn_TuWmYhQT-bvfXPvDdVuh9mcw==', start_index=8150)
Annotation(end_index=8677, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIOKwYH2p-ZsVbBugnXT5JqKvBSUAqtp4PDynngqpeRsjLizk8s6GNkMN8tpm2SEW7nBxiMurIbh6f9L-Ehy25eWAP8Kf3Wau-8wX6zwIUMKYg9Q2t-VaNSrjdv839kg==', start_index=8663)
Annotation(end_index=8677, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBLtHNtdsYLT1rKwW-Brbd6JYNEywngjb916MU48HPksLzCTauuc9nymuTnuMcOdfL-3rnmxcsCM1hdZ82wnIWE9R6uSyBNpssdl0QLqmkzu8AMSOi', start_index=8663)
Annotation(end_index=8890, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoYVY1WEhkHzDQJU1Gx4IDzjUN3o6Lzoq87wfb1himOKx-LHGki7JZq58Mt7fEM8hdAmlJ7Tx4aVKF5LvPpKyL1UtQKRGrAobSbOYreFLxQunLC1ibs3qU', start_index=8876)
Annotation(end_index=8890, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIOKwYH2p-ZsVbBugnXT5JqKvBSUAqtp4PDynngqpeRsjLizk8s6GNkMN8tpm2SEW7nBxiMurIbh6f9L-Ehy25eWAP8Kf3Wau-8wX6zwIUMKYg9Q2t-VaNSrjdv839kg==', start_index=8876)
Annotation(end_index=9443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE34bfdvytMKhl7oVY59e6PymqKrEYKpCYm0FEK48HbeqdpUHnSTrZh6TrFvsmQcjBLVOtUvD2yOwXxSdrnrcVJM_9m9LCFRXp3ID60XCc7dlTN1o9uLpQwSy0g_LI4hF_WC3UAvUFrAN4JOogOwODs8_OxDIuCNi-Nofs-Q7B45f3-5FXk3LSt5Gaa-iyIpvHfnVtRqmY2BNqxq8rDRZV20oDlDFRSXxHFTCrrw4Bxl03qGg5Ej7Y=', start_index=9425)
Annotation(end_index=9443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPxFUIx44eV5-OT83NH4zbcnM2rug0hKA-71zAdX057fpHzGK8YJT-j7bY889fEXIAAuHSLYSvi1Oz4-VWBL3B3KzMrr9mw07V3TfyAJ8TyWVgPS5Tn9OY', start_index=9425)
Annotation(end_index=9443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5SFHJQ8ocgNEO0cOsHLvqq5dg00c2dXpaf49ra9q6TY985K37Mm82D3Z1MgWSOlHkZyHbo2fbdzxp-ztnKr_YHKXt98qi1GA0TmdpxFkISSmDpbJj', start_index=9425)
Annotation(end_index=9553, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM_8GFPaHHTSnV53uzzgBu3MTjH8-j7IedKffT_OjaMiV17Dd25ZJdmDfEYEmpBe4s3fKEoqO3LkhuRM2EcgIMnm12VAuodXB2p18Q2qDB1137hTHJG8DRUKMrqEvadDeACGPaD0jaxNPnflsl_BrGOGlTBkcT5assQkpOWQ7AhIVTm23snqhQPLCuBtw8_iz6G_VkkVGYnCdRXR1TyQiTEzRZnIzU7gWKYJ3DeCqO9r8RJQxkk1g=', start_index=9539)
Annotation(end_index=9553, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHicSdxcy3bXcmsnzR8gGX4bMgS8yjZ4nMrakSEitDgMic6PNJ8AAY2817I9bfu6Mt_ydLxTpaRJHOkj4Rsfp37qAaraI6GEyXmmZ0Q_NMnUn04FzfepF2WihGm7kf012zzlhO_2lydcwjiSgjc', start_index=9539)
Annotation(end_index=9770, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIOKwYH2p-ZsVbBugnXT5JqKvBSUAqtp4PDynngqpeRsjLizk8s6GNkMN8tpm2SEW7nBxiMurIbh6f9L-Ehy25eWAP8Kf3Wau-8wX6zwIUMKYg9Q2t-VaNSrjdv839kg==', start_index=9752)
Annotation(end_index=9770, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiHRSrsk6qz7_pbTeiVi-19fjwlKUQzn8zeCS-9WF_LsfGYI1PeQqaYabrEPf6F4dngkKh2sFCQqjyuI7Kxun9ivY2dTsy2sZNPCBSyxFTTyGbVBCenCgIss5d5JHFIn8sAabaXIEeQybuSueMbFT-0aAq', start_index=9752)
Annotation(end_index=9770, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9gkEUswbW0opROt7nJ2eDtqJMBgb16kPxO1wyWC0rHstW7-k5PbukTV-igU6ddabrBJMuo3Uo60IxvLZ3OwxrqpbaQGEeZlG6vKEx9EpIcKjh-Kj3', start_index=9752)
Annotation(end_index=10072, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPxFUIx44eV5-OT83NH4zbcnM2rug0hKA-71zAdX057fpHzGK8YJT-j7bY889fEXIAAuHSLYSvi1Oz4-VWBL3B3KzMrr9mw07V3TfyAJ8TyWVgPS5Tn9OY', start_index=10058)
Annotation(end_index=10072, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0CzvJHjffrsuPfZ4CSL7AmbtFx2y1RYM4BktJYt8jquYGB1MDS8e3OjAvYXRpB4YMQ9S_M38VsMVBYKu7OmhcA_nF5coW-wsLvaQMTt6dXiCE9oj58teyMIAJU83XWgCbNg==', start_index=10058)
Annotation(end_index=10374, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_inCJx7HAA_3e0-5k9P5p6qiOiVCqjuCrNl0E28r15ilzVaBnT1qstsPctPIi39sTJOa2knbixlhR2rgoGWt4HjRXvhPGdTPV7fRyjMTlHf7llJalrkk93G7zFDEqoX2ZZ4bjWg==', start_index=10361)
Annotation(end_index=10374, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjIS5t2km9KL6Jjv3DlsRVADDLZJENBYxR6gFIO-SnfjG_xsbOHW9VzFHxDyqBIgI6fjBo2TLIxd8S2PPKGSRcfskpKSd_rrws3ltfyLl4Y7laTpHq2F4n9A8VK2xCE3RYrAxWuCYLWtPRkH3IcQgQV-ABcAd9KItd8dsreFgkMmZ--zBodvDlBSy0EaDL77aig-J1HcgqX_GHleM69EcHdjekxa989yY=', start_index=10361)
Annotation(end_index=10657, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_inCJx7HAA_3e0-5k9P5p6qiOiVCqjuCrNl0E28r15ilzVaBnT1qstsPctPIi39sTJOa2knbixlhR2rgoGWt4HjRXvhPGdTPV7fRyjMTlHf7llJalrkk93G7zFDEqoX2ZZ4bjWg==', start_index=10643)
Annotation(end_index=10657, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYMtSx-Fw30K_zh1OoQr_nXlkxQ15pS7IMvnmmukAd0W4QqaKiDgpcEpe_gg6DA80RG5ElddrQvGpVfU7h5xsBwb3fVz4eD4bhJi6cQkMon_BttAMd5Y_MBYCIBTt5s4BFbof4BrwcbPEQJnq6nFnhPQ_Tw5_6z-fkQCeSniYgS3eq4jY=', start_index=10643)
Annotation(end_index=11244, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc_6QjCkpPQjI2YqJyPABTO8LWVVBLfgRItsNocVRFEV_qezMEm1zMv7dbdlZsfSyO7yxe3hLa-zExfiDJSOTp7-yLwdqyi1U3Sm_ItFvHAhlu6DFXMxwAXtnT6I3_soywsLWMfmHn8mQ4CzVpDKEa_GYh3994qTnCyyO8FaIx7VWJOgvw31R3Ne720QBW0XmOtqCcmsaFdsg=', start_index=11234)
Annotation(end_index=11461, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc_6QjCkpPQjI2YqJyPABTO8LWVVBLfgRItsNocVRFEV_qezMEm1zMv7dbdlZsfSyO7yxe3hLa-zExfiDJSOTp7-yLwdqyi1U3Sm_ItFvHAhlu6DFXMxwAXtnT6I3_soywsLWMfmHn8mQ4CzVpDKEa_GYh3994qTnCyyO8FaIx7VWJOgvw31R3Ne720QBW0XmOtqCcmsaFdsg=', start_index=11451)
Annotation(end_index=12164, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELY5TorT8jSLtPHbtTKbXd5yWEbrWBPr17dp-x4_SvTyCmBetN_75nSDO-X_lecjGR6vsvQmR-SreGN56BgD5mm7DBo0-Rz3Cmn_Z_dMKhXV9JXSQb', start_index=12150)
Annotation(end_index=12164, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsvzbcIw-JMni5yF7fNXuZ7_vxHiMS3vOvjAEAPKsHPHO3j2oA9xvkz9inGaLiVCQ270mDVrt-rrgpH_qXQ-AiyCxxDJM7-tHi0UEkYy8LK-u1DpId1A2t', start_index=12150)
Annotation(end_index=12532, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_inCJx7HAA_3e0-5k9P5p6qiOiVCqjuCrNl0E28r15ilzVaBnT1qstsPctPIi39sTJOa2knbixlhR2rgoGWt4HjRXvhPGdTPV7fRyjMTlHf7llJalrkk93G7zFDEqoX2ZZ4bjWg==', start_index=12518)
Annotation(end_index=12532, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM_8GFPaHHTSnV53uzzgBu3MTjH8-j7IedKffT_OjaMiV17Dd25ZJdmDfEYEmpBe4s3fKEoqO3LkhuRM2EcgIMnm12VAuodXB2p18Q2qDB1137hTHJG8DRUKMrqEvadDeACGPaD0jaxNPnflsl_BrGOGlTBkcT5assQkpOWQ7AhIVTm23snqhQPLCuBtw8_iz6G_VkkVGYnCdRXR1TyQiTEzRZnIzU7gWKYJ3DeCqO9r8RJQxkk1g=', start_index=12518)
Annotation(end_index=12872, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGo0xFCB1zQtzlMjk9y-6pC3_3-YfYsvoqh7ZoCUns6OOjLgS6LlsdilvBssRS8yi7zpauvwnj8eU8PnqBO4Oq5RGWUbXjYwM1pChBbXXX_S58Da8XxMk8DLFoMrAtRbqF-_-K3Xj0UeC12O3njlsDkGg==', start_index=12862)
Annotation(end_index=13104, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELinuUx6jfzbOEbO45h6Gh1xYwaslzuCF9zKbmvmOGDy8k8g_0ixGbVWjZFrSOX_j-D0k9S0d9aPVDRIrkM8elRUVvNxVoaPsA9CsKujoeg5KoMVKMTbrhfy9O6XeEVfGetuG0z8zeDcIpEZwQ8DytN7yQanUO6diHcdfnWtmoKO4NkM1QeXoSG5TBOAN0V3M8VOt9v3DWZVc8hmMlDndjeZyyQhDZxkQzNLK0T97y7h8g8gCHFQ==', start_index=13086)
Annotation(end_index=13104, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbXEVgC1BYzoCKCIYo4pDQ41RJogFazpzXmjUVMZk3ZPzJlvGvSCG_r32UTimB9rvCB6OPg7PfVZHzxiporUIlsgB9p3Nww4KJcsIWZTMHvteZwG-MkCuXFTYt0xP-DI28Sxs=', start_index=13086)
Annotation(end_index=13104, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGo0xFCB1zQtzlMjk9y-6pC3_3-YfYsvoqh7ZoCUns6OOjLgS6LlsdilvBssRS8yi7zpauvwnj8eU8PnqBO4Oq5RGWUbXjYwM1pChBbXXX_S58Da8XxMk8DLFoMrAtRbqF-_-K3Xj0UeC12O3njlsDkGg==', start_index=13086)
Annotation(end_index=13585, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGo0xFCB1zQtzlMjk9y-6pC3_3-YfYsvoqh7ZoCUns6OOjLgS6LlsdilvBssRS8yi7zpauvwnj8eU8PnqBO4Oq5RGWUbXjYwM1pChBbXXX_S58Da8XxMk8DLFoMrAtRbqF-_-K3Xj0UeC12O3njlsDkGg==', start_index=13575)
Annotation(end_index=13796, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEH18ZdJcchKz3X7n5bBmOdQMM9vAByLBD0mCGq61O0chJTcRo5-cgVbIRYqpeRM8dRisUGh3CrXVqKkKG4jlr6sAYim1M97bXlGpkyuglogocVMoH75nxfqgOl7AAcK1KzGB2ZbLmmcPvic2zUmPaOvml9LdLfi8Jv4gKywXmfRrhxh3U=', start_index=13782)
Annotation(end_index=13796, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4pV7Dj5h3mFJ1EkJCPNvAhHOmN_zJ_FIuMqfN0-aZ1xQ7pDq6fucvcvnNyN4EVXIrS7pGnESTMVy3ppmg2dGK1SvOYSmPIjIoYionOOei_-olvbPL7ooHzM8ALtU7XEoyIurzZMcGZcmroDGYIg--_lB1hD34qivpGg==', start_index=13782)
Annotation(end_index=14166, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiIBe5afSewTrim-WsdAVFHBWOGovONZ4uzjTUXlGcKz-IggfKCHzSIF1DIxm7r2VsupWfKb6gLa58rSCRY5D2SyDEy36vFE4jKQ-X142qp39AgyLgWTfRBga5p-ei', start_index=14152)
Annotation(end_index=14166, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKXT2e5y1L6jv-jC0_kPaiqkt9eNIjXipL_rQ1YRBkACpie0A6Rb_bfZdRnU7uz_wKkME7QNu3L9WtHuA6pWutZZlOxNyteqBFQGjESjCoWD-LDnObMB4CFuHKqw==', start_index=14152)
Annotation(end_index=14616, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKXT2e5y1L6jv-jC0_kPaiqkt9eNIjXipL_rQ1YRBkACpie0A6Rb_bfZdRnU7uz_wKkME7QNu3L9WtHuA6pWutZZlOxNyteqBFQGjESjCoWD-LDnObMB4CFuHKqw==', start_index=14606)
Annotation(end_index=14795, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA8-B6igtJdoi1Vb5eMKCo6RU_VZHXKonk1L78vVdjN7Mi8ZVwbg1UlIwn1WkXbGwIGDOYH3pEjGDFwYhhM2wHuPKmnk0O7160ZvfgNXtnfF8Ge8fkeJAMm4N3', start_index=14777)
Annotation(end_index=14795, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlKnrCqf1NbrxCfxCn4qHyG83KZrxs0UFHbY2HZs7xT9nvPSCR3Rf00ilHI2cH6NwuWJ2fJCjicJf2x0v0zNLqIWNfxgkQl0bSeqytd4k12a9OjSuO9ymMfNJ_CRK4Z6rSGOB-tkoG', start_index=14777)
Annotation(end_index=14795, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGrl2ZhBnEc0VxVEBNL2jjwOcumbNsxLxT6tn7KoFUqKidKrJcDWZ09rkRfvnIfHAew8EiAGNndfuP8kpaV7JB6HldSamPGHLSAKm6-khvszVnJbnK4uD1QqeExkHMDquUdJIW-Unfbd5c1-Ataisp_z2GLevNI5eKEpP_CDyM8zLsMEjbxj3_4erknKbSOAw8j3_PwueZvErYBX7n5lVqzWfVD3Oq', start_index=14777)
Annotation(end_index=14998, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEH4-Y716YUT4q20y_G16RMqTUPtf3tEYoKDpegJBZ3CbSNB-QuT9_SotAESRFJexeU_mQZ64cD-954gXLdbZ6-lSuNnO89KCsKNMg172sTthhJyLsWLC_0IH9DYNbXgIrlfPulvk_xXvyI0KV2Gln7W5knVcoUfza1YfpQvyw=', start_index=14984)
Annotation(end_index=14998, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA8-B6igtJdoi1Vb5eMKCo6RU_VZHXKonk1L78vVdjN7Mi8ZVwbg1UlIwn1WkXbGwIGDOYH3pEjGDFwYhhM2wHuPKmnk0O7160ZvfgNXtnfF8Ge8fkeJAMm4N3', start_index=14984)
Annotation(end_index=15476, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA8-B6igtJdoi1Vb5eMKCo6RU_VZHXKonk1L78vVdjN7Mi8ZVwbg1UlIwn1WkXbGwIGDOYH3pEjGDFwYhhM2wHuPKmnk0O7160ZvfgNXtnfF8Ge8fkeJAMm4N3', start_index=15466)
Annotation(end_index=16680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC7_MUdEZmknNo5ItehtYls4iaO16BYsfM1lu5v2B4HiuB9B6_OiOZfQMxPA6VeejR8pjpKMJVmtZFTF2yFa542uaWdo1nYUeZFDZaks1WSbuHgbsIU3JzOjCGtaCvXTL7QPR5wAgOYzjs1IhdPVTRUQjPZhjpD4F-HBW_GzUfxdGSPSptCK2PhbJezE-n1gjP', start_index=16671)
Annotation(end_index=16764, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC7_MUdEZmknNo5ItehtYls4iaO16BYsfM1lu5v2B4HiuB9B6_OiOZfQMxPA6VeejR8pjpKMJVmtZFTF2yFa542uaWdo1nYUeZFDZaks1WSbuHgbsIU3JzOjCGtaCvXTL7QPR5wAgOYzjs1IhdPVTRUQjPZhjpD4F-HBW_GzUfxdGSPSptCK2PhbJezE-n1gjP', start_index=16755)
Annotation(end_index=16774, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfrLLDzz1JJAH4D6Gw07u5PPJMQZDP21oz8T1ROaYS0FtVJk7vQRaDfAq_1KK78PfskPn0DT5tPRE8-X6Hral6voOM1SiaJSLtHOGOebsUuTEklBP_MbSQvHq6mLna', start_index=16765)
Annotation(end_index=16826, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfrLLDzz1JJAH4D6Gw07u5PPJMQZDP21oz8T1ROaYS0FtVJk7vQRaDfAq_1KK78PfskPn0DT5tPRE8-X6Hral6voOM1SiaJSLtHOGOebsUuTEklBP_MbSQvHq6mLna', start_index=16817)
Annotation(end_index=16837, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM_8GFPaHHTSnV53uzzgBu3MTjH8-j7IedKffT_OjaMiV17Dd25ZJdmDfEYEmpBe4s3fKEoqO3LkhuRM2EcgIMnm12VAuodXB2p18Q2qDB1137hTHJG8DRUKMrqEvadDeACGPaD0jaxNPnflsl_BrGOGlTBkcT5assQkpOWQ7AhIVTm23snqhQPLCuBtw8_iz6G_VkkVGYnCdRXR1TyQiTEzRZnIzU7gWKYJ3DeCqO9r8RJQxkk1g=', start_index=16827)
Annotation(end_index=16910, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM_8GFPaHHTSnV53uzzgBu3MTjH8-j7IedKffT_OjaMiV17Dd25ZJdmDfEYEmpBe4s3fKEoqO3LkhuRM2EcgIMnm12VAuodXB2p18Q2qDB1137hTHJG8DRUKMrqEvadDeACGPaD0jaxNPnflsl_BrGOGlTBkcT5assQkpOWQ7AhIVTm23snqhQPLCuBtw8_iz6G_VkkVGYnCdRXR1TyQiTEzRZnIzU7gWKYJ3DeCqO9r8RJQxkk1g=', start_index=16900)
Annotation(end_index=16920, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbG7bht0731MMkm6sLQqn4bKWQ0KBr1jKGSB7LqYmFUmCsjtgUvsbzzRxnN38_9EtLNwXkeRaZ_TcEy6aPUrQnNkNj-7KvS3O46Ot3i2kkteu8q5A6hhOYAfpvhSglo8dV2g==', start_index=16911)
Annotation(end_index=16960, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbG7bht0731MMkm6sLQqn4bKWQ0KBr1jKGSB7LqYmFUmCsjtgUvsbzzRxnN38_9EtLNwXkeRaZ_TcEy6aPUrQnNkNj-7KvS3O46Ot3i2kkteu8q5A6hhOYAfpvhSglo8dV2g==', start_index=16951)
Annotation(end_index=16971, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiIBe5afSewTrim-WsdAVFHBWOGovONZ4uzjTUXlGcKz-IggfKCHzSIF1DIxm7r2VsupWfKb6gLa58rSCRY5D2SyDEy36vFE4jKQ-X142qp39AgyLgWTfRBga5p-ei', start_index=16961)
Annotation(end_index=17052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiIBe5afSewTrim-WsdAVFHBWOGovONZ4uzjTUXlGcKz-IggfKCHzSIF1DIxm7r2VsupWfKb6gLa58rSCRY5D2SyDEy36vFE4jKQ-X142qp39AgyLgWTfRBga5p-ei', start_index=17042)
Annotation(end_index=17062, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGO407s37XYU7EaWm3AuG7U5BT2FNt7EJhq3Zvj8q1ePgZpMkgyRPxr0UpPRmSEqzz4weQNP7-juhIy-215aiD5PwuFbFAQrmPJLOFYZqpvfSuCULr', start_index=17053)
Annotation(end_index=17123, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGO407s37XYU7EaWm3AuG7U5BT2FNt7EJhq3Zvj8q1ePgZpMkgyRPxr0UpPRmSEqzz4weQNP7-juhIy-215aiD5PwuFbFAQrmPJLOFYZqpvfSuCULr', start_index=17114)
Annotation(end_index=17134, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE34bfdvytMKhl7oVY59e6PymqKrEYKpCYm0FEK48HbeqdpUHnSTrZh6TrFvsmQcjBLVOtUvD2yOwXxSdrnrcVJM_9m9LCFRXp3ID60XCc7dlTN1o9uLpQwSy0g_LI4hF_WC3UAvUFrAN4JOogOwODs8_OxDIuCNi-Nofs-Q7B45f3-5FXk3LSt5Gaa-iyIpvHfnVtRqmY2BNqxq8rDRZV20oDlDFRSXxHFTCrrw4Bxl03qGg5Ej7Y=', start_index=17124)
Annotation(end_index=17189, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE34bfdvytMKhl7oVY59e6PymqKrEYKpCYm0FEK48HbeqdpUHnSTrZh6TrFvsmQcjBLVOtUvD2yOwXxSdrnrcVJM_9m9LCFRXp3ID60XCc7dlTN1o9uLpQwSy0g_LI4hF_WC3UAvUFrAN4JOogOwODs8_OxDIuCNi-Nofs-Q7B45f3-5FXk3LSt5Gaa-iyIpvHfnVtRqmY2BNqxq8rDRZV20oDlDFRSXxHFTCrrw4Bxl03qGg5Ej7Y=', start_index=17179)
Annotation(end_index=17200, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGskQ9IO-Vrx5_MIV6XiCGRmmgF7pPb3cjq6D9K_OUFjko_ZbNHTHUbCUK_zK-McvjfIDsvqybg-ilORM3biTAunT1gRxyoOxSDWQZIYrHT8ZFznmKWLJnvjzr1blsJ-AEUGwMAfwhMO4oVWw==', start_index=17190)
Annotation(end_index=17249, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGskQ9IO-Vrx5_MIV6XiCGRmmgF7pPb3cjq6D9K_OUFjko_ZbNHTHUbCUK_zK-McvjfIDsvqybg-ilORM3biTAunT1gRxyoOxSDWQZIYrHT8ZFznmKWLJnvjzr1blsJ-AEUGwMAfwhMO4oVWw==', start_index=17239)
Annotation(end_index=17260, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwUjsGciZkAAzpy2Dol9lhZh7KJZGHc6dCrGn3zfrdGJiXJSmTucVetJIzx6ftqsJj2ekVWMTeubSnvWuMsAR-1sDZtGb3VRNbK7AFsU-3XOqC_5AK', start_index=17250)
Annotation(end_index=17318, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwUjsGciZkAAzpy2Dol9lhZh7KJZGHc6dCrGn3zfrdGJiXJSmTucVetJIzx6ftqsJj2ekVWMTeubSnvWuMsAR-1sDZtGb3VRNbK7AFsU-3XOqC_5AK', start_index=17308)
Annotation(end_index=17328, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZpUZl_Lp0MQvNeFNpqmMpbpqLSdmuKJYvrUw4noxPAq8I4oRk9POxQXzeYFLg52HrPGeD54JMgrGtrV7hGT-hebHPofCZJfp_W7nsFccGsrCvPMzv4bsP', start_index=17319)
Annotation(end_index=17377, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZpUZl_Lp0MQvNeFNpqmMpbpqLSdmuKJYvrUw4noxPAq8I4oRk9POxQXzeYFLg52HrPGeD54JMgrGtrV7hGT-hebHPofCZJfp_W7nsFccGsrCvPMzv4bsP', start_index=17368)
Annotation(end_index=17388, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc_6QjCkpPQjI2YqJyPABTO8LWVVBLfgRItsNocVRFEV_qezMEm1zMv7dbdlZsfSyO7yxe3hLa-zExfiDJSOTp7-yLwdqyi1U3Sm_ItFvHAhlu6DFXMxwAXtnT6I3_soywsLWMfmHn8mQ4CzVpDKEa_GYh3994qTnCyyO8FaIx7VWJOgvw31R3Ne720QBW0XmOtqCcmsaFdsg=', start_index=17378)
Annotation(end_index=17460, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc_6QjCkpPQjI2YqJyPABTO8LWVVBLfgRItsNocVRFEV_qezMEm1zMv7dbdlZsfSyO7yxe3hLa-zExfiDJSOTp7-yLwdqyi1U3Sm_ItFvHAhlu6DFXMxwAXtnT6I3_soywsLWMfmHn8mQ4CzVpDKEa_GYh3994qTnCyyO8FaIx7VWJOgvw31R3Ne720QBW0XmOtqCcmsaFdsg=', start_index=17450)
Annotation(end_index=17470, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfrLLDzz1JJAH4D6Gw07u5PPJMQZDP21oz8T1ROaYS0FtVJk7vQRaDfAq_1KK78PfskPn0DT5tPRE8-X6Hral6voOM1SiaJSLtHOGOebsUuTEklBP_MbSQvHq6mLna', start_index=17461)
Annotation(end_index=17526, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfrLLDzz1JJAH4D6Gw07u5PPJMQZDP21oz8T1ROaYS0FtVJk7vQRaDfAq_1KK78PfskPn0DT5tPRE8-X6Hral6voOM1SiaJSLtHOGOebsUuTEklBP_MbSQvHq6mLna', start_index=17517)
Annotation(end_index=17536, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjIS5t2km9KL6Jjv3DlsRVADDLZJENBYxR6gFIO-SnfjG_xsbOHW9VzFHxDyqBIgI6fjBo2TLIxd8S2PPKGSRcfskpKSd_rrws3ltfyLl4Y7laTpHq2F4n9A8VK2xCE3RYrAxWuCYLWtPRkH3IcQgQV-ABcAd9KItd8dsreFgkMmZ--zBodvDlBSy0EaDL77aig-J1HcgqX_GHleM69EcHdjekxa989yY=', start_index=17527)
Annotation(end_index=17621, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjIS5t2km9KL6Jjv3DlsRVADDLZJENBYxR6gFIO-SnfjG_xsbOHW9VzFHxDyqBIgI6fjBo2TLIxd8S2PPKGSRcfskpKSd_rrws3ltfyLl4Y7laTpHq2F4n9A8VK2xCE3RYrAxWuCYLWtPRkH3IcQgQV-ABcAd9KItd8dsreFgkMmZ--zBodvDlBSy0EaDL77aig-J1HcgqX_GHleM69EcHdjekxa989yY=', start_index=17612)
Annotation(end_index=17632, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPxFUIx44eV5-OT83NH4zbcnM2rug0hKA-71zAdX057fpHzGK8YJT-j7bY889fEXIAAuHSLYSvi1Oz4-VWBL3B3KzMrr9mw07V3TfyAJ8TyWVgPS5Tn9OY', start_index=17622)
Annotation(end_index=17692, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPxFUIx44eV5-OT83NH4zbcnM2rug0hKA-71zAdX057fpHzGK8YJT-j7bY889fEXIAAuHSLYSvi1Oz4-VWBL3B3KzMrr9mw07V3TfyAJ8TyWVgPS5Tn9OY', start_index=17682)
Annotation(end_index=17703, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbXEVgC1BYzoCKCIYo4pDQ41RJogFazpzXmjUVMZk3ZPzJlvGvSCG_r32UTimB9rvCB6OPg7PfVZHzxiporUIlsgB9p3Nww4KJcsIWZTMHvteZwG-MkCuXFTYt0xP-DI28Sxs=', start_index=17693)
Annotation(end_index=17767, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbXEVgC1BYzoCKCIYo4pDQ41RJogFazpzXmjUVMZk3ZPzJlvGvSCG_r32UTimB9rvCB6OPg7PfVZHzxiporUIlsgB9p3Nww4KJcsIWZTMHvteZwG-MkCuXFTYt0xP-DI28Sxs=', start_index=17757)
Annotation(end_index=17777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfFZJzYt7mGI7-vJx8zHPqH_GRs5s4S5ESxv0Dq2opAmL9pg5MVI5KwoHGAqQhfg3k1ZMhK3Aaso9rVtADgL409tNFwbZRAY9D-GV_4SCYwnypqHI=', start_index=17768)
Annotation(end_index=17839, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfFZJzYt7mGI7-vJx8zHPqH_GRs5s4S5ESxv0Dq2opAmL9pg5MVI5KwoHGAqQhfg3k1ZMhK3Aaso9rVtADgL409tNFwbZRAY9D-GV_4SCYwnypqHI=', start_index=17830)
Annotation(end_index=17850, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGC5yYz87q2R89o1EO6pzXop54ig37IjNSuWtsJ-SwqBL6KPPL4qxJ0dwjFHdf6bPu96hwu95x7rHGV1WdBi_aMhdrX4pYVTb5sWIWobkbqDs3yQSTOn3YHEIoEz8CfFzQhdSPLyFeuxZ_VoGkeYwhtIoDY76RGnyGs2Dzl6AXOzGwJiSaCNyondRBOtSBMQvFiYTmr5A==', start_index=17840)
Annotation(end_index=17923, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGC5yYz87q2R89o1EO6pzXop54ig37IjNSuWtsJ-SwqBL6KPPL4qxJ0dwjFHdf6bPu96hwu95x7rHGV1WdBi_aMhdrX4pYVTb5sWIWobkbqDs3yQSTOn3YHEIoEz8CfFzQhdSPLyFeuxZ_VoGkeYwhtIoDY76RGnyGs2Dzl6AXOzGwJiSaCNyondRBOtSBMQvFiYTmr5A==', start_index=17913)
Annotation(end_index=17934, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG__48Px0LCX06ZXtO0yIJAgBOwGHjzER_ALX3JyVG7XOa8KcClcHbnZQq_0aGpkv79vN0uuuVnc-lYPxLCHNA0tyJjWC5tmHYpK13VkhlaxG590GUb', start_index=17924)
Annotation(end_index=18013, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG__48Px0LCX06ZXtO0yIJAgBOwGHjzER_ALX3JyVG7XOa8KcClcHbnZQq_0aGpkv79vN0uuuVnc-lYPxLCHNA0tyJjWC5tmHYpK13VkhlaxG590GUb', start_index=18003)
Annotation(end_index=18024, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs-YGlnAFm37XLCnWDF82xbklN3McbbWsj3DpFB9zPCC32XfUwEY9Ru1_BM4roexXADFBFSbictbaLOvuW1vwj_twJulEfaAltBmCBmiMagNW1iKBdEfXdjmeKcbdwWXbMUvaGmrPZ5v3dN_RmEa2u9GM5QOvH9ymNBPf6iW0=', start_index=18014)
Annotation(end_index=18094, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs-YGlnAFm37XLCnWDF82xbklN3McbbWsj3DpFB9zPCC32XfUwEY9Ru1_BM4roexXADFBFSbictbaLOvuW1vwj_twJulEfaAltBmCBmiMagNW1iKBdEfXdjmeKcbdwWXbMUvaGmrPZ5v3dN_RmEa2u9GM5QOvH9ymNBPf6iW0=', start_index=18084)
Annotation(end_index=18105, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHicSdxcy3bXcmsnzR8gGX4bMgS8yjZ4nMrakSEitDgMic6PNJ8AAY2817I9bfu6Mt_ydLxTpaRJHOkj4Rsfp37qAaraI6GEyXmmZ0Q_NMnUn04FzfepF2WihGm7kf012zzlhO_2lydcwjiSgjc', start_index=18095)
Annotation(end_index=18169, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHicSdxcy3bXcmsnzR8gGX4bMgS8yjZ4nMrakSEitDgMic6PNJ8AAY2817I9bfu6Mt_ydLxTpaRJHOkj4Rsfp37qAaraI6GEyXmmZ0Q_NMnUn04FzfepF2WihGm7kf012zzlhO_2lydcwjiSgjc', start_index=18159)
Annotation(end_index=18180, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0CzvJHjffrsuPfZ4CSL7AmbtFx2y1RYM4BktJYt8jquYGB1MDS8e3OjAvYXRpB4YMQ9S_M38VsMVBYKu7OmhcA_nF5coW-wsLvaQMTt6dXiCE9oj58teyMIAJU83XWgCbNg==', start_index=18170)
Annotation(end_index=18232, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0CzvJHjffrsuPfZ4CSL7AmbtFx2y1RYM4BktJYt8jquYGB1MDS8e3OjAvYXRpB4YMQ9S_M38VsMVBYKu7OmhcA_nF5coW-wsLvaQMTt6dXiCE9oj58teyMIAJU83XWgCbNg==', start_index=18222)
Annotation(end_index=18243, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsvzbcIw-JMni5yF7fNXuZ7_vxHiMS3vOvjAEAPKsHPHO3j2oA9xvkz9inGaLiVCQ270mDVrt-rrgpH_qXQ-AiyCxxDJM7-tHi0UEkYy8LK-u1DpId1A2t', start_index=18233)
Annotation(end_index=18299, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsvzbcIw-JMni5yF7fNXuZ7_vxHiMS3vOvjAEAPKsHPHO3j2oA9xvkz9inGaLiVCQ270mDVrt-rrgpH_qXQ-AiyCxxDJM7-tHi0UEkYy8LK-u1DpId1A2t', start_index=18289)
Annotation(end_index=18310, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGo0xFCB1zQtzlMjk9y-6pC3_3-YfYsvoqh7ZoCUns6OOjLgS6LlsdilvBssRS8yi7zpauvwnj8eU8PnqBO4Oq5RGWUbXjYwM1pChBbXXX_S58Da8XxMk8DLFoMrAtRbqF-_-K3Xj0UeC12O3njlsDkGg==', start_index=18300)
Annotation(end_index=18363, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGo0xFCB1zQtzlMjk9y-6pC3_3-YfYsvoqh7ZoCUns6OOjLgS6LlsdilvBssRS8yi7zpauvwnj8eU8PnqBO4Oq5RGWUbXjYwM1pChBbXXX_S58Da8XxMk8DLFoMrAtRbqF-_-K3Xj0UeC12O3njlsDkGg==', start_index=18353)
Annotation(end_index=18374, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKXT2e5y1L6jv-jC0_kPaiqkt9eNIjXipL_rQ1YRBkACpie0A6Rb_bfZdRnU7uz_wKkME7QNu3L9WtHuA6pWutZZlOxNyteqBFQGjESjCoWD-LDnObMB4CFuHKqw==', start_index=18364)
Annotation(end_index=18431, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKXT2e5y1L6jv-jC0_kPaiqkt9eNIjXipL_rQ1YRBkACpie0A6Rb_bfZdRnU7uz_wKkME7QNu3L9WtHuA6pWutZZlOxNyteqBFQGjESjCoWD-LDnObMB4CFuHKqw==', start_index=18421)
Annotation(end_index=18442, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA8-B6igtJdoi1Vb5eMKCo6RU_VZHXKonk1L78vVdjN7Mi8ZVwbg1UlIwn1WkXbGwIGDOYH3pEjGDFwYhhM2wHuPKmnk0O7160ZvfgNXtnfF8Ge8fkeJAMm4N3', start_index=18432)
Annotation(end_index=18509, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA8-B6igtJdoi1Vb5eMKCo6RU_VZHXKonk1L78vVdjN7Mi8ZVwbg1UlIwn1WkXbGwIGDOYH3pEjGDFwYhhM2wHuPKmnk0O7160ZvfgNXtnfF8Ge8fkeJAMm4N3', start_index=18499)
Annotation(end_index=18520, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEH4-Y716YUT4q20y_G16RMqTUPtf3tEYoKDpegJBZ3CbSNB-QuT9_SotAESRFJexeU_mQZ64cD-954gXLdbZ6-lSuNnO89KCsKNMg172sTthhJyLsWLC_0IH9DYNbXgIrlfPulvk_xXvyI0KV2Gln7W5knVcoUfza1YfpQvyw=', start_index=18510)
Annotation(end_index=18576, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEH4-Y716YUT4q20y_G16RMqTUPtf3tEYoKDpegJBZ3CbSNB-QuT9_SotAESRFJexeU_mQZ64cD-954gXLdbZ6-lSuNnO89KCsKNMg172sTthhJyLsWLC_0IH9DYNbXgIrlfPulvk_xXvyI0KV2Gln7W5knVcoUfza1YfpQvyw=', start_index=18566)
Annotation(end_index=18587, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGrl2ZhBnEc0VxVEBNL2jjwOcumbNsxLxT6tn7KoFUqKidKrJcDWZ09rkRfvnIfHAew8EiAGNndfuP8kpaV7JB6HldSamPGHLSAKm6-khvszVnJbnK4uD1QqeExkHMDquUdJIW-Unfbd5c1-Ataisp_z2GLevNI5eKEpP_CDyM8zLsMEjbxj3_4erknKbSOAw8j3_PwueZvErYBX7n5lVqzWfVD3Oq', start_index=18577)
Annotation(end_index=18638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGrl2ZhBnEc0VxVEBNL2jjwOcumbNsxLxT6tn7KoFUqKidKrJcDWZ09rkRfvnIfHAew8EiAGNndfuP8kpaV7JB6HldSamPGHLSAKm6-khvszVnJbnK4uD1QqeExkHMDquUdJIW-Unfbd5c1-Ataisp_z2GLevNI5eKEpP_CDyM8zLsMEjbxj3_4erknKbSOAw8j3_PwueZvErYBX7n5lVqzWfVD3Oq', start_index=18628)
Annotation(end_index=18649, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpAJuBaOfL63jGvREo2SaWeytgUDgETi-m8LWcGf0x_-A5MOrvPesq1I86KYqblY22tLWgsZRYEnHdvI3Zp4OcpIPCXrDBjhtv3MpWFAMeT2Nj2YQE_CJKslIQwS350nxlJ_O_0TelUtXxyWFJQatRLlA=', start_index=18639)
Annotation(end_index=18705, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpAJuBaOfL63jGvREo2SaWeytgUDgETi-m8LWcGf0x_-A5MOrvPesq1I86KYqblY22tLWgsZRYEnHdvI3Zp4OcpIPCXrDBjhtv3MpWFAMeT2Nj2YQE_CJKslIQwS350nxlJ_O_0TelUtXxyWFJQatRLlA=', start_index=18695)
Annotation(end_index=18716, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEH18ZdJcchKz3X7n5bBmOdQMM9vAByLBD0mCGq61O0chJTcRo5-cgVbIRYqpeRM8dRisUGh3CrXVqKkKG4jlr6sAYim1M97bXlGpkyuglogocVMoH75nxfqgOl7AAcK1KzGB2ZbLmmcPvic2zUmPaOvml9LdLfi8Jv4gKywXmfRrhxh3U=', start_index=18706)
Annotation(end_index=18770, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEH18ZdJcchKz3X7n5bBmOdQMM9vAByLBD0mCGq61O0chJTcRo5-cgVbIRYqpeRM8dRisUGh3CrXVqKkKG4jlr6sAYim1M97bXlGpkyuglogocVMoH75nxfqgOl7AAcK1KzGB2ZbLmmcPvic2zUmPaOvml9LdLfi8Jv4gKywXmfRrhxh3U=', start_index=18760)
Annotation(end_index=18781, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4pV7Dj5h3mFJ1EkJCPNvAhHOmN_zJ_FIuMqfN0-aZ1xQ7pDq6fucvcvnNyN4EVXIrS7pGnESTMVy3ppmg2dGK1SvOYSmPIjIoYionOOei_-olvbPL7ooHzM8ALtU7XEoyIurzZMcGZcmroDGYIg--_lB1hD34qivpGg==', start_index=18771)
Annotation(end_index=18850, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4pV7Dj5h3mFJ1EkJCPNvAhHOmN_zJ_FIuMqfN0-aZ1xQ7pDq6fucvcvnNyN4EVXIrS7pGnESTMVy3ppmg2dGK1SvOYSmPIjIoYionOOei_-olvbPL7ooHzM8ALtU7XEoyIurzZMcGZcmroDGYIg--_lB1hD34qivpGg==', start_index=18840)
Annotation(end_index=18860, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbQDe6W3-G2BoZdxHnkffru5yZWOvZbRcvUNPAJW_DrncHnv90GjURdTnhxM5WmJd98Lb3GBS2F29Ki_oR9kArFC-XbVki9SEH0IYg8O5MIH-yyKH9pX8h12dWcebTp7CJFB0IRGcUgkrKka2XNehHqByI', start_index=18851)
Annotation(end_index=18925, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbQDe6W3-G2BoZdxHnkffru5yZWOvZbRcvUNPAJW_DrncHnv90GjURdTnhxM5WmJd98Lb3GBS2F29Ki_oR9kArFC-XbVki9SEH0IYg8O5MIH-yyKH9pX8h12dWcebTp7CJFB0IRGcUgkrKka2XNehHqByI', start_index=18916)
Annotation(end_index=18936, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG23bBOhNvcFnBn2iQDKLDyzpJ7nn1_bPM2y4JHCQ7Igzy56x-zPRvF-2ZTW7KKHFpAOLooIZgJz4ltIso4zmEC6cTnDgYYQIr-JFKRamqqjlN5r7Fr', start_index=18926)
Annotation(end_index=19005, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG23bBOhNvcFnBn2iQDKLDyzpJ7nn1_bPM2y4JHCQ7Igzy56x-zPRvF-2ZTW7KKHFpAOLooIZgJz4ltIso4zmEC6cTnDgYYQIr-JFKRamqqjlN5r7Fr', start_index=18995)
Annotation(end_index=19016, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbXEVgC1BYzoCKCIYo4pDQ41RJogFazpzXmjUVMZk3ZPzJlvGvSCG_r32UTimB9rvCB6OPg7PfVZHzxiporUIlsgB9p3Nww4KJcsIWZTMHvteZwG-MkCuXFTYt0xP-DI28Sxs=', start_index=19006)
Annotation(end_index=19059, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbXEVgC1BYzoCKCIYo4pDQ41RJogFazpzXmjUVMZk3ZPzJlvGvSCG_r32UTimB9rvCB6OPg7PfVZHzxiporUIlsgB9p3Nww4KJcsIWZTMHvteZwG-MkCuXFTYt0xP-DI28Sxs=', start_index=19049)
Annotation(end_index=19070, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyOhpgTLY7yhjA_ZCRFXzyV-otL2UuljgscS4XL6CdnMJ_ZOVsHOlVcbX7Oor6BSR9LdOu6_0qE2qKIgLEq0egiho9zAL5te_chvmTM2NxppcijL2_xdTkkML-WROi8JTsYmnaNecNX3dM9VxMdQ0f4AhYK-LAQGcJREdWmbU-R8uQ61u2', start_index=19060)
Annotation(end_index=19138, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyOhpgTLY7yhjA_ZCRFXzyV-otL2UuljgscS4XL6CdnMJ_ZOVsHOlVcbX7Oor6BSR9LdOu6_0qE2qKIgLEq0egiho9zAL5te_chvmTM2NxppcijL2_xdTkkML-WROi8JTsYmnaNecNX3dM9VxMdQ0f4AhYK-LAQGcJREdWmbU-R8uQ61u2', start_index=19128)
Annotation(end_index=19149, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbSZok3FPS2aBeLjG4GVPIH_xb5rB2OkhQlICrB6fJyzAC8P-jYLZhTm0LQm3UzNCE9BjJSI7bUI__BxTA7p0BY8iAhPwgqvtbJO3plL1MgssOfeia2XQgnRpN-QTzWhLTTTcE9fMk8sJKKfx3uStZ', start_index=19139)
Annotation(end_index=19210, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbSZok3FPS2aBeLjG4GVPIH_xb5rB2OkhQlICrB6fJyzAC8P-jYLZhTm0LQm3UzNCE9BjJSI7bUI__BxTA7p0BY8iAhPwgqvtbJO3plL1MgssOfeia2XQgnRpN-QTzWhLTTTcE9fMk8sJKKfx3uStZ', start_index=19200)
Annotation(end_index=19220, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGU353O9GQL2cWPxcw8t93sWJAZ442Q7fBOJJ2IMjIbxgpZFJaT5E9TFr-GKpUu_azqrFuegb_u2f2GuNXMtZ6s3C5DIVjLgs9t73Pc1iC0rH_Mc1rCChTua1AN1XAvkkF_xXrS-vbH1XdNwHMtwMjRfIG62RtgvyBcJOC-jeN3MlEdw4qYuz6A5Vt_yqrYCMXIb1U8P8AUx12OtHq3PKIYkdvMBgsgmNGBM1F00eEBjHfAEFmBnM0yJ20=', start_index=19211)
Annotation(end_index=19295, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGU353O9GQL2cWPxcw8t93sWJAZ442Q7fBOJJ2IMjIbxgpZFJaT5E9TFr-GKpUu_azqrFuegb_u2f2GuNXMtZ6s3C5DIVjLgs9t73Pc1iC0rH_Mc1rCChTua1AN1XAvkkF_xXrS-vbH1XdNwHMtwMjRfIG62RtgvyBcJOC-jeN3MlEdw4qYuz6A5Vt_yqrYCMXIb1U8P8AUx12OtHq3PKIYkdvMBgsgmNGBM1F00eEBjHfAEFmBnM0yJ20=', start_index=19286)
Annotation(end_index=19305, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZpUZl_Lp0MQvNeFNpqmMpbpqLSdmuKJYvrUw4noxPAq8I4oRk9POxQXzeYFLg52HrPGeD54JMgrGtrV7hGT-hebHPofCZJfp_W7nsFccGsrCvPMzv4bsP', start_index=19296)
Annotation(end_index=19354, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZpUZl_Lp0MQvNeFNpqmMpbpqLSdmuKJYvrUw4noxPAq8I4oRk9POxQXzeYFLg52HrPGeD54JMgrGtrV7hGT-hebHPofCZJfp_W7nsFccGsrCvPMzv4bsP', start_index=19345)
Annotation(end_index=19365, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgZTeyUe6SecGIGUDHGnZpA7-qfow9POTZ8wmjEQIg3tNTAKgnIDaR-fjEkTjd0TmekCemlpGsuEiD78tGFs7_8cqSduJ81eB7pzFwc2LSrT2MMPiZShDT2YGPGwr891pTCSlS1Wnb-9w7lLZsmEkYoCQqhmR95pc7oGbg', start_index=19355)
Annotation(end_index=19427, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgZTeyUe6SecGIGUDHGnZpA7-qfow9POTZ8wmjEQIg3tNTAKgnIDaR-fjEkTjd0TmekCemlpGsuEiD78tGFs7_8cqSduJ81eB7pzFwc2LSrT2MMPiZShDT2YGPGwr891pTCSlS1Wnb-9w7lLZsmEkYoCQqhmR95pc7oGbg', start_index=19417)
Annotation(end_index=19438, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_inCJx7HAA_3e0-5k9P5p6qiOiVCqjuCrNl0E28r15ilzVaBnT1qstsPctPIi39sTJOa2knbixlhR2rgoGWt4HjRXvhPGdTPV7fRyjMTlHf7llJalrkk93G7zFDEqoX2ZZ4bjWg==', start_index=19428)
Annotation(end_index=19497, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_inCJx7HAA_3e0-5k9P5p6qiOiVCqjuCrNl0E28r15ilzVaBnT1qstsPctPIi39sTJOa2knbixlhR2rgoGWt4HjRXvhPGdTPV7fRyjMTlHf7llJalrkk93G7zFDEqoX2ZZ4bjWg==', start_index=19487)
Annotation(end_index=19508, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVTwO846UV5gX1R7UVTGG0JKDv1texyXg5ZPE81dxZTxmjELFldRJnG7wlO04-Fwtwn4F4ETY2BiO5PvoGd3qjokic9Kusw_zud1M0Q_KqxkgdQqzKoDjncW2KRxUsLpxa5bSC7w6u7vpLzA1WQJTX-lpDq3gq0nKBJibWj3QgB2BEkRSSn_TuWmYhQT-bvfXPvDdVuh9mcw==', start_index=19498)
Annotation(end_index=19561, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVTwO846UV5gX1R7UVTGG0JKDv1texyXg5ZPE81dxZTxmjELFldRJnG7wlO04-Fwtwn4F4ETY2BiO5PvoGd3qjokic9Kusw_zud1M0Q_KqxkgdQqzKoDjncW2KRxUsLpxa5bSC7w6u7vpLzA1WQJTX-lpDq3gq0nKBJibWj3QgB2BEkRSSn_TuWmYhQT-bvfXPvDdVuh9mcw==', start_index=19551)
Annotation(end_index=19572, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9gkEUswbW0opROt7nJ2eDtqJMBgb16kPxO1wyWC0rHstW7-k5PbukTV-igU6ddabrBJMuo3Uo60IxvLZ3OwxrqpbaQGEeZlG6vKEx9EpIcKjh-Kj3', start_index=19562)
Annotation(end_index=19612, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9gkEUswbW0opROt7nJ2eDtqJMBgb16kPxO1wyWC0rHstW7-k5PbukTV-igU6ddabrBJMuo3Uo60IxvLZ3OwxrqpbaQGEeZlG6vKEx9EpIcKjh-Kj3', start_index=19602)
Annotation(end_index=19623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiHRSrsk6qz7_pbTeiVi-19fjwlKUQzn8zeCS-9WF_LsfGYI1PeQqaYabrEPf6F4dngkKh2sFCQqjyuI7Kxun9ivY2dTsy2sZNPCBSyxFTTyGbVBCenCgIss5d5JHFIn8sAabaXIEeQybuSueMbFT-0aAq', start_index=19613)
Annotation(end_index=19680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiHRSrsk6qz7_pbTeiVi-19fjwlKUQzn8zeCS-9WF_LsfGYI1PeQqaYabrEPf6F4dngkKh2sFCQqjyuI7Kxun9ivY2dTsy2sZNPCBSyxFTTyGbVBCenCgIss5d5JHFIn8sAabaXIEeQybuSueMbFT-0aAq', start_index=19670)
Annotation(end_index=19691, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELY5TorT8jSLtPHbtTKbXd5yWEbrWBPr17dp-x4_SvTyCmBetN_75nSDO-X_lecjGR6vsvQmR-SreGN56BgD5mm7DBo0-Rz3Cmn_Z_dMKhXV9JXSQb', start_index=19681)
Annotation(end_index=19746, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELY5TorT8jSLtPHbtTKbXd5yWEbrWBPr17dp-x4_SvTyCmBetN_75nSDO-X_lecjGR6vsvQmR-SreGN56BgD5mm7DBo0-Rz3Cmn_Z_dMKhXV9JXSQb', start_index=19736)
Annotation(end_index=19757, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELinuUx6jfzbOEbO45h6Gh1xYwaslzuCF9zKbmvmOGDy8k8g_0ixGbVWjZFrSOX_j-D0k9S0d9aPVDRIrkM8elRUVvNxVoaPsA9CsKujoeg5KoMVKMTbrhfy9O6XeEVfGetuG0z8zeDcIpEZwQ8DytN7yQanUO6diHcdfnWtmoKO4NkM1QeXoSG5TBOAN0V3M8VOt9v3DWZVc8hmMlDndjeZyyQhDZxkQzNLK0T97y7h8g8gCHFQ==', start_index=19747)
Annotation(end_index=19825, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELinuUx6jfzbOEbO45h6Gh1xYwaslzuCF9zKbmvmOGDy8k8g_0ixGbVWjZFrSOX_j-D0k9S0d9aPVDRIrkM8elRUVvNxVoaPsA9CsKujoeg5KoMVKMTbrhfy9O6XeEVfGetuG0z8zeDcIpEZwQ8DytN7yQanUO6diHcdfnWtmoKO4NkM1QeXoSG5TBOAN0V3M8VOt9v3DWZVc8hmMlDndjeZyyQhDZxkQzNLK0T97y7h8g8gCHFQ==', start_index=19815)
Annotation(end_index=19836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYMtSx-Fw30K_zh1OoQr_nXlkxQ15pS7IMvnmmukAd0W4QqaKiDgpcEpe_gg6DA80RG5ElddrQvGpVfU7h5xsBwb3fVz4eD4bhJi6cQkMon_BttAMd5Y_MBYCIBTt5s4BFbof4BrwcbPEQJnq6nFnhPQ_Tw5_6z-fkQCeSniYgS3eq4jY=', start_index=19826)
Annotation(end_index=19896, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYMtSx-Fw30K_zh1OoQr_nXlkxQ15pS7IMvnmmukAd0W4QqaKiDgpcEpe_gg6DA80RG5ElddrQvGpVfU7h5xsBwb3fVz4eD4bhJi6cQkMon_BttAMd5Y_MBYCIBTt5s4BFbof4BrwcbPEQJnq6nFnhPQ_Tw5_6z-fkQCeSniYgS3eq4jY=', start_index=19886)
Annotation(end_index=19907, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5SFHJQ8ocgNEO0cOsHLvqq5dg00c2dXpaf49ra9q6TY985K37Mm82D3Z1MgWSOlHkZyHbo2fbdzxp-ztnKr_YHKXt98qi1GA0TmdpxFkISSmDpbJj', start_index=19897)
Annotation(end_index=19974, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5SFHJQ8ocgNEO0cOsHLvqq5dg00c2dXpaf49ra9q6TY985K37Mm82D3Z1MgWSOlHkZyHbo2fbdzxp-ztnKr_YHKXt98qi1GA0TmdpxFkISSmDpbJj', start_index=19964)
Annotation(end_index=19985, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIOKwYH2p-ZsVbBugnXT5JqKvBSUAqtp4PDynngqpeRsjLizk8s6GNkMN8tpm2SEW7nBxiMurIbh6f9L-Ehy25eWAP8Kf3Wau-8wX6zwIUMKYg9Q2t-VaNSrjdv839kg==', start_index=19975)
Annotation(end_index=20034, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIOKwYH2p-ZsVbBugnXT5JqKvBSUAqtp4PDynngqpeRsjLizk8s6GNkMN8tpm2SEW7nBxiMurIbh6f9L-Ehy25eWAP8Kf3Wau-8wX6zwIUMKYg9Q2t-VaNSrjdv839kg==', start_index=20024)
Annotation(end_index=20045, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoYVY1WEhkHzDQJU1Gx4IDzjUN3o6Lzoq87wfb1himOKx-LHGki7JZq58Mt7fEM8hdAmlJ7Tx4aVKF5LvPpKyL1UtQKRGrAobSbOYreFLxQunLC1ibs3qU', start_index=20035)
Annotation(end_index=20092, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoYVY1WEhkHzDQJU1Gx4IDzjUN3o6Lzoq87wfb1himOKx-LHGki7JZq58Mt7fEM8hdAmlJ7Tx4aVKF5LvPpKyL1UtQKRGrAobSbOYreFLxQunLC1ibs3qU', start_index=20082)
Annotation(end_index=20103, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBLtHNtdsYLT1rKwW-Brbd6JYNEywngjb916MU48HPksLzCTauuc9nymuTnuMcOdfL-3rnmxcsCM1hdZ82wnIWE9R6uSyBNpssdl0QLqmkzu8AMSOi', start_index=20093)
Annotation(end_index=20163, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBLtHNtdsYLT1rKwW-Brbd6JYNEywngjb916MU48HPksLzCTauuc9nymuTnuMcOdfL-3rnmxcsCM1hdZ82wnIWE9R6uSyBNpssdl0QLqmkzu8AMSOi', start_index=20153)

## Sources
