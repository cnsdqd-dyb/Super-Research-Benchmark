# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 02bf82a0 | **Time:** 495.57s | **Cost:** $1.85555
--------------------------------------------------------------------------------

# Distributed Architectures in Financial Risk Management: Balancing Accuracy, Stability, and Systemic Contagion

### Key Points
*   **The Stability-Latency Trade-off:** Distributed, event-driven architectures (EDA) significantly reduce latency in financial risk monitoring compared to batch processing, enabling real-time fraud detection and dynamic risk assessment. However, this speed comes at the cost of increased architectural complexity and the potential for rapid failure propagation.
*   **Mechanisms of Failure:** Event-driven systems are inherently susceptible to "retry storms" and "feedback loops." Without robust governance, automated error handling can amplify transient faults into systemic outages, and algorithmic interactions can trigger market-wide flash crashes.
*   **Consistency Challenges:** The CAP theorem dictates that distributed systems cannot simultaneously guarantee consistency, availability, and partition tolerance. Financial systems often require strong consistency for transaction ledgers, creating a tension with the high availability required for real-time monitoring.
*   **Architectural Mitigation:** Stability is not inherent but engineered. Critical patterns such as Circuit Breakers, Bulkheads, and the Saga Pattern are essential to contain faults. Furthermore, deterministic architectures like LMAX (Disruptor pattern) offer a proven method to achieve high throughput without the contention that leads to instability.
*   **The Role of Adaptive Intelligence:** Emerging research suggests that "Adaptive Model Orchestration" and AI-driven consistency tuning can dynamically adjust system parameters in response to stress, offering a pathway to reconcile the conflict between monitoring accuracy and operational stability.

---

### Executive Summary
The transition from monolithic, batch-oriented systems to distributed, event-driven architectures (EDA) represents a paradigm shift in financial risk management. Driven by the need for sub-millisecond decision-making in high-frequency trading (HFT), real-time fraud detection, and dynamic liquidity management, financial institutions are increasingly adopting microservices and stream processing technologies. While these architectures offer unparalleled agility and monitoring accuracy, they introduce non-linear failure modes that threaten system stability.

The central inquiry of this report is whether these distributed systems can maintain a dynamic balance between accuracy and stability, or if they inevitably accelerate cascading failures. The evidence suggests a nuanced reality: while unmanaged event-driven systems do accelerate failure propagation through mechanisms like retry storms and positive feedback loops, rigorous architectural patterns—specifically circuit breakers, deterministic sequencing, and adaptive consistency models—can effectively mitigate these risks. The stability of a distributed financial system is therefore not a function of the architecture itself, but of the maturity of its fault-tolerance mechanisms and the implementation of "human-in-the-loop" governance strategies like kill switches.

---

## 1. The Evolution of Financial Risk Architectures
The financial sector has historically relied on batch processing for risk management—calculating Value at Risk (VaR), reconciling ledgers, and checking compliance at the end of the trading day. However, the modern financial ecosystem, characterized by high-frequency trading and instant payments, renders batch processing inadequate. The latency inherent in batch systems conceals accumulating risks, as demonstrated by historical failures where abnormalities were not detected in time to prevent systemic loss [cite: 1].

### 1.1 The Shift to Event-Driven Architecture (EDA)
Event-Driven Architecture (EDA) has emerged as the dominant solution for real-time financial systems. In an EDA, components communicate asynchronously by producing and consuming events (e.g., "Trade Executed," "Payment Initiated") rather than through direct, synchronous requests. This decoupling allows services to operate independently; a fraud detection service can process a transaction event without blocking the payment gateway that generated it [cite: 2, 3].

The benefits of EDA in finance are substantial:
*   **Decoupling and Scalability:** Services can scale independently to handle bursts in market data or transaction volume [cite: 4, 5].
*   **Real-Time Responsiveness:** Systems can react to market fluctuations and fraud signals instantly, rather than waiting for scheduled jobs [cite: 4].
*   **Auditability:** Event sourcing patterns, where every state change is stored as an immutable event, provide the granular audit trails required by regulators [cite: 2, 6].

### 1.2 The Latency-Stability Paradox
While EDA solves the latency problem, it introduces the "Latency-Stability Paradox." The same mechanisms that allow for high-speed, asynchronous processing—automatic retries, fan-out messaging, and dynamic scaling—can also amplify minor errors into catastrophic failures. In a tightly coupled monolithic system, a failure often results in a hard stop. In a distributed system, a failure can trigger a chain reaction of retries and backpressure that overwhelms healthy components, leading to a "cascading failure" [cite: 7, 8].

---

## 2. Mechanisms of Instability in Distributed Systems
To understand whether EDA *inherently* accelerates cascading failures, one must examine the specific failure modes unique to distributed financial environments. Research identifies several critical vectors of instability: retry storms, resource exhaustion, and automated feedback loops.

### 2.1 Cascading Failures and the "Domino Effect"
A cascading failure occurs when the failure of a single component triggers the failure of dependent components, eventually bringing down the entire system. In microservices, this often happens when services share resources or lack appropriate fault isolation [cite: 7, 8].

#### 2.1.1 The Retry Storm
One of the most pernicious failure modes in EDA is the "retry storm" (also known as a "Platform Event Trap"). When a downstream service (e.g., a credit check system) becomes temporarily unavailable or slow, upstream services (e.g., payment processors) may automatically retry their requests. If thousands of concurrent requests are retried simultaneously, the failing service is bombarded with traffic, preventing it from recovering. This creates a "death spiral" where the volume of retries consumes all available network bandwidth and CPU cycles, causing the outage to spread to the upstream services [cite: 3, 9, 10].

In serverless and cloud-native environments, this can also lead to "Cloud Bill Shock," where infinite retry loops generate massive costs without processing any valid transactions [cite: 9].

#### 2.1.2 Resource Exhaustion and Thread Starvation
In synchronous communication models (often used within hybrid EDAs), a slow downstream service can cause the calling service to wait. These waiting requests consume threads and memory. If the delay persists, the calling service eventually runs out of threads, becoming unresponsive to *its* callers. This propagates the failure up the stack, potentially crashing the entire user-facing application [cite: 3, 7].

### 2.2 Automated Feedback Loops and Flash Crashes
In the context of High-Frequency Trading (HFT) and algorithmic risk management, instability often manifests as market volatility rather than just IT system crashes. "Flash crashes" are sudden, deep market drops caused by the interaction of automated trading algorithms [cite: 11].

*   **Positive Feedback Loops:** Algorithms programmed to sell when prices drop can trigger other algorithms to sell, creating a self-reinforcing cycle. If risk management systems are also automated and react to volatility by withdrawing liquidity (stopping trades), the market depth evaporates, accelerating the crash [cite: 12, 13].
*   **Herding Behavior:** When multiple distinct risk models are trained on similar datasets or use similar logic, they may react identically to a market signal. This "herding" creates massive unidirectional pressure on the market, overwhelming the system's capacity to absorb the shock [cite: 13, 14].

Research indicates that while negative feedback loops (e.g., buying the dip) stabilize markets, the speed of EDA-based HFT systems can allow positive feedback loops to spiral out of control before human intervention is possible [cite: 11, 13].

---

## 3. The Consistency vs. Stability Trade-off
Financial systems face a unique constraint: the absolute requirement for data accuracy (consistency) in transaction processing, balanced against the need for high availability in risk monitoring. This tension is formalized by the CAP Theorem.

### 3.1 The CAP Theorem in Finance
The CAP theorem states that a distributed system can only guarantee two of three properties: **Consistency** (all nodes see the same data), **Availability** (every request receives a response), and **Partition Tolerance** (the system survives network failures) [cite: 15, 16, 17].

*   **CP Systems (Consistency + Partition Tolerance):** Financial ledgers and transaction engines typically prioritize CP. If a network partition occurs, the system must refuse updates rather than risk a "split-brain" scenario where money is spent twice. However, prioritizing consistency can reduce availability, leading to transaction failures during network instability [cite: 16, 18].
*   **AP Systems (Availability + Partition Tolerance):** Fraud detection and market monitoring often lean towards AP. It is better to accept a slightly stale view of the market and continue processing than to halt all monitoring. However, eventual consistency can lead to "phantom" reads or missed fraud signals if the data lag is too significant [cite: 19, 20].

### 3.2 Race Conditions and Data Integrity
In EDA, the asynchronous nature of message delivery introduces the risk of race conditions. Events may arrive out of order (e.g., a "Withdrawal" event arriving before the "Deposit" event), leading to incorrect account balances or risk calculations [cite: 21, 22].
*   **Phantom Failures:** A system might process a transaction based on an outdated state, only to find later that the transaction should have been rejected.
*   **Distributed Conflicts:** When multiple services update the same entity (e.g., a risk profile) concurrently, resolving the conflict without a central lock is mathematically complex and prone to error [cite: 22].

### 3.3 Adaptive Consistency Models
Recent advancements propose "Adaptive Consistency" or "AI-Driven Consistency" to bridge this gap. These systems dynamically adjust their consistency levels based on real-time conditions. During periods of low volatility, the system might enforce strong consistency. During a high-traffic event or network partition, it might relax consistency for non-critical functions (like user notifications) while maintaining it for the core ledger [cite: 23, 24]. This dynamic tuning attempts to maintain the "dynamic balance" referenced in the query.

---

## 4. Architectural Strategies for Stability
If EDA inherently introduces risks of cascading failures, how can financial systems be stabilized? The industry has developed specific design patterns that act as "shock absorbers," preventing local failures from becoming systemic disasters.

### 4.1 The Circuit Breaker Pattern
The Circuit Breaker is the primary defense against cascading failures. It wraps a protected function call (e.g., a call to a credit check service) in a monitor.
*   **Closed State:** Requests flow normally.
*   **Open State:** If the failure rate exceeds a threshold (e.g., 50% of requests fail), the breaker "trips" and immediately fails all subsequent requests without attempting to contact the downstream service. This prevents the "retry storm" and gives the failing service time to recover [cite: 25, 26, 27].
*   **Half-Open State:** After a timeout, the breaker allows a limited number of test requests to pass. If they succeed, the circuit closes; if they fail, it re-opens [cite: 28, 29].

In financial systems, circuit breakers prevent a slow fraud detection service from backing up the entire trade execution pipeline [cite: 30].

### 4.2 The Bulkhead Pattern
The Bulkhead pattern isolates resources into distinct pools, similar to the watertight compartments of a ship. If one service exhausts its thread pool or connection limit, the failure is contained within that "bulkhead" and does not affect other services.
*   **Example:** A trading platform might have separate thread pools for "Equities," "Futures," and "Options." A crash in the Options pricing service will not prevent Equities trading from continuing [cite: 7, 31, 32].

### 4.3 The Saga Pattern for Distributed Transactions
To maintain consistency across distributed services without using slow "Two-Phase Commit" (2PC) protocols, financial systems use the Saga pattern. A Saga is a sequence of local transactions. If one step fails, the Saga executes "compensating transactions" to undo the previous steps (e.g., refunding a charge if the order fulfillment fails) [cite: 33, 34]. This ensures data integrity (eventual consistency) without locking the entire system.

### 4.4 Deterministic Architecture: The LMAX Disruptor
A compelling counter-argument to the instability of distributed systems is the LMAX architecture. Developed for a high-performance financial exchange, LMAX rejects the traditional multi-threaded, lock-heavy approach.
*   **The Disruptor:** Instead of queues, LMAX uses a "Ring Buffer" and a single-threaded business logic processor. This eliminates lock contention and context switching, allowing for millions of transactions per second with deterministic latency [cite: 6, 35, 36].
*   **Deterministic Performance:** Because the input stream is totally ordered and processed sequentially, the system's state is deterministic. This allows for perfect reproducibility (replayability) of events, which is crucial for debugging and risk analysis [cite: 35, 37].
*   **Implication:** LMAX demonstrates that stability and speed are not mutually exclusive; rather, instability often arises from *non-deterministic* concurrency models (locks, threads) rather than the event-driven nature itself [cite: 36].

---

## 5. Dynamic Balance: Monitoring Accuracy vs. Stability
The query asks if a "dynamic balance" is possible. Research into "Adaptive Model Orchestration" (AMO) and "Temporal Risk Graphs" (TRG) suggests that the next generation of risk systems is explicitly designed to manage this balance.

### 5.1 Adaptive Model Orchestration (AMO)
AMO involves using AI to dynamically select the best risk model based on the current context.
*   **Context-Awareness:** During normal trading, a complex, high-latency deep learning model might be used for maximum accuracy. During a flash crash or high-volatility event, the orchestrator might switch to a simpler, faster heuristic model to maintain stability and throughput [cite: 1, 38].
*   **Results:** Studies show that combining AMO with event-driven pipelines (Kafka-Flink) can reduce detection latency by 85-90% while maintaining high accuracy and reducing false positives [cite: 1, 38].

### 5.2 Temporal Risk Graphs (TRG)
TRGs allow systems to model the relationships between entities (traders, accounts, IP addresses) over time. By analyzing the *graph* of transactions in real-time, systems can detect complex fraud rings that individual transaction analysis would miss. When implemented on stream processing engines like Flink, TRGs provide a high-fidelity view of risk without the latency of batch graph processing [cite: 1, 38].

---

## 6. Governance and the "Kill Switch"
No architectural pattern can guarantee 100% stability in the face of "Black Swan" events or algorithmic runaway. Therefore, "Kill Switches" are a mandatory component of financial risk management.

### 6.1 Automated and Manual Kill Switches
*   **Function:** A kill switch is a mechanism to immediately halt trading or transaction processing. It can be triggered manually by risk managers or automatically by the system if pre-defined thresholds (e.g., "Peak Net Notional Exposure") are breached [cite: 39, 40, 41].
*   **Regulatory Requirement:** Regulators like the SEC and FINRA mandate kill switches to prevent market disruptions like the Knight Capital incident, where a software glitch caused $440 million in losses in minutes [cite: 40, 42, 43].
*   **Risk of the Kill Switch:** Ironically, the kill switch itself introduces a risk. If triggered erroneously (false positive), it can withdraw liquidity from the market during a stress event, potentially exacerbating a crash. Thus, the design of the kill switch requires a delicate balance between sensitivity and specificity [cite: 44, 45].

---

## 7. Conclusion
The question of whether distributed architectures in financial risk management can maintain a dynamic balance between accuracy and stability admits a complex answer.

**Does event-driven processing inherently accelerate cascading failures?**
**Yes, in the absence of rigorous safeguards.** The asynchronous, decoupled nature of EDA creates fertile ground for retry storms, resource exhaustion, and positive feedback loops. The speed of these systems means that failures can propagate faster than human operators can react, as evidenced by flash crashes and algorithmic trading glitches.

**Can a dynamic balance be maintained?**
**Yes, but it requires a "Resilience-First" engineering approach.** The research demonstrates that the trade-off is not absolute. Through the application of:
1.  **Defensive Patterns:** Circuit breakers and bulkheads to contain faults.
2.  **Deterministic Architectures:** LMAX-style patterns to eliminate concurrency hazards.
3.  **Adaptive Intelligence:** AI-driven orchestration (AMO) to dynamically tune the accuracy/latency trade-off.
4.  **Governance:** Automated kill switches and strict consistency models for critical ledgers.

Financial institutions can achieve a system that is both highly accurate and robust. The instability is not a necessary consequence of the architecture, but rather a consequence of naive implementations that prioritize speed without accounting for the non-linear failure modes of distributed systems. The future of financial risk management lies in **Adaptive Event-Driven Architectures** that can autonomously shift their operational profile—prioritizing consistency and stability during stress, and speed and accuracy during calm.

---

## 8. Detailed Analysis of Key Technologies and Patterns

### 8.1 Apache Kafka and Flink in Risk Pipelines
Apache Kafka serves as the central nervous system for modern financial EDAs, providing a high-throughput, durable log of events. Apache Flink is often paired with Kafka for stateful stream processing.
*   **State Management:** Flink allows for "stateful" processing, meaning the system remembers past events (e.g., the last 10 transactions) to calculate running aggregates for fraud detection. This capability is crucial for replacing batch jobs [cite: 1].
*   **Exactly-Once Semantics:** To prevent the "double-counting" of financial transactions during retries, Flink and Kafka support "exactly-once" processing semantics, ensuring that a failure and subsequent retry does not corrupt the financial state [cite: 4].

### 8.2 The Role of Idempotency
Idempotency is a critical concept for stability. An idempotent operation produces the same result no matter how many times it is executed. In a financial system prone to retry storms, ensuring that the "Process Payment" operation is idempotent prevents a retry from charging a customer multiple times. This is often implemented using unique transaction IDs and deduplication tables [cite: 2, 22].

### 8.3 Backpressure Mechanisms
Backpressure is a feedback mechanism where a consumer tells a producer to slow down. In a risk management system, if the fraud detection engine is overwhelmed, it should exert backpressure on the transaction ingestion service. Without backpressure, the ingestion service will continue to pile up events until the system runs out of memory and crashes. Reactive Streams and TCP flow control are common implementations of backpressure in financial EDAs [cite: 9].

### 8.4 Comparison of Consistency Models

| Feature | Strong Consistency (CP) | Eventual Consistency (AP) | Adaptive Consistency |
| :--- | :--- | :--- | :--- |
| **Data View** | All nodes see same data instantly. | Nodes may see stale data temporarily. | Varies based on context/load. |
| **Latency** | High (requires coordination). | Low (immediate response). | Optimized (Low in calm, High in stress). |
| **Availability** | Lower (halts on partition). | High (always responds). | High (degrades gracefully). |
| **Use Case** | Core Ledgers, Balances. | Fraud Alerts, User Feeds. | Hybrid Risk Systems. |
| **Risk** | System unavailability. | Stale data/Phantom reads. | Complexity of implementation. |

[Table derived from sources: 11, 14, 54, 55, 80]

---

## 9. Future Directions: AI and Quantum Risk Management
The report identifies a trajectory toward increasingly autonomous risk systems.
*   **Agentic AI:** Future systems may employ "Agentic AI" where autonomous agents monitor risk and take corrective actions (e.g., rebalancing portfolios) without human intervention. This raises new stability concerns regarding agent interaction and emergent behavior [cite: 46, 47].
*   **Quantum Computing:** While not the focus of the current query, the massive computational power of quantum computing could eventually allow for real-time Monte Carlo simulations that are currently impossible, potentially resolving the accuracy/latency trade-off entirely, though likely introducing new forms of complexity.

In conclusion, the distributed architecture of financial risk systems is a double-edged sword. It is the only viable way to handle the volume and velocity of modern finance, yet it requires a level of engineering discipline and architectural sophistication that far exceeds traditional banking software. The "dynamic balance" is achievable, but it is an active, continuous process of tuning, monitoring, and adaptation, not a static state.

**Sources:**
1. [ejece.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhxtuyyLbEA_sLHjjAeJDUqFn_hbOjXDzi1UUkvuY9nT7uA7VpVWBet_SMxgGM8kwATZ7SHKwoIyiVGywOM5T1i7RkisEi_F9xIB2ACTXl8B5Uo8QFkuag4jiOHiPQpxUtFet5G58wOA2z2w==)
2. [sarcouncil.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_z4hWZU0DoPatwBmXEgbC0aIH1wzCPqwyXGaDyvcYPsIK5k9iIOB8bUSSIvYQl2F78B4IZXZS1H4yk0CNMDfzl3Boa3yDvekjgt8dlJ3JTCtc7Gb9ReKYUHjmezjWupggfLjY_i5iXaC0ZSV2WeHbLneq8HDeFQ==)
3. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEn0ierwLTGlTBzZDxAZ1OJQAYitnQzhCnbLEKMDEX_vYdN6dnQ19LeOwizskTdC8uhtGGWSeRUgivdZeo0HdRrZi9lXNNuOapoc_rl2JTWfMu3wIlLbNyHZC3WsqUkHIFNRLyQl8twsxieLGylMttyM2YREs1-ZiboejOq7eDdU23NPznVABowLs-o-YebHZ1deLX7JQ==)
4. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSOvj5WeA_YMwJVxfva9uQqDlB1ymOx73qLCuvujUD8LHV6yPY_6EXRHoI2r2NEPcn3enm9uN7KEX0RaKHr4TvtLDGUUm8fEeN9Um3y1yqLCmYd8s5Ahjlxb9zjkWOgVpgAPzg9pFmNrpIM47bHAJLuzMF_5rZbvwDMWQtdeBYx9SL61m5Nr3V_o7rTXecTiEgtlxg_YmI7FITJd9PTIT4Og2OtVmsw8KxQ6gJ-uSn6A==)
5. [estuary.dev](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQ1esNjTOHy3CmbDScz21MUbsi08w2Y37EVMsmeiFU2jCVezofhLXAMwao4lIb1dqni0Tc_jxkNjH1Das-GjVAL5hYilJIAotJMBUfrfF8djX4mqjJHYIO1s5TrB8PvlPnLEmANJSf69dwVp_62axWGg==)
6. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcLCm8LlzpnVWVDZvK6aUr_20P3Xbqs-7mAghE1abSW6q19QHGW3WL_UWHuQ1x6VOwUwHbVsa0CSarv99Vc0pRzOzCQBYKCqLsC_HIwmLR3-LLqfkTt-LhR6s7mS58bgg3LJcDpK643v4VgXC1O6aa1F5QKeCSKHGvvbEDogeAC-S3w6JJj1tJmXw6EKqVr3WPu1udcgCTUbSkytkhDPIQRM3OmJuHLd_yST7_VlQ=)
7. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENJi0hCsk65nnKueo-upzvinDzoH3ePr-W1ohEIgAhn8jIBjg3EJVPqQGdR6qs3zSYb7kEPIH1DzeBEOIhsm_AJilVsdgdHqs39ILLbK4-8Yn0X-xLMSYNPv29amE8g4Ndho828X_pbAIcRkdYd-wnNB8Cm3JpLnlqu1DawUn1Cb4hVniRwcq-liaO_oTJVrj6vLzwZvYdK6J5xzTX8LP7tH2ycW-uzrfPnyvK)
8. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy-FufNzbdYdcd7vHZJMyAOmThqvyQ0nAR-xCejYYlGs-NX0sqhhIGhVGCxTsvkehTNd2_0k0wm4rwn2cS4k84zc5UHzxgpODFpd-Ai-tFtJ5dlztwdRTQnDf3DGRytqhs78ui)
9. [aisaaswriter.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEegdMbDVARWY87lDNAX3foadAGSycuIDEQvSDsv7gm0b7qkC_lUrFD0FmCuJQF2IY_o9tzwkoFL-Ju12mCTYgcHi_v3J8WASD3xxj0G_97BMajDWHTxm5o1izvy4gIU4dgJPl738=)
10. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHf9cpt9DRInY830Uem_LIlUizIlTdxGlz1e2yxWCRCqQJhoDBKgYhKWeEfTO2Z55kNM_6W28JVdJ4RNX8sslGJHj58yImljOoQefKcdAPYSDowg6lE3j4AvZ2r2kLCcmD59pQSWfwx_xJnK7-Nin9nTtylQT8vR-o1iUxeD6OPfOo-_RKK50yZGP-JPBpBpYHLpHHldlmNffaN8p_ETA3I)
11. [tradersunion.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7cWut0D-yBAWtsSLqKlHFCnBy2S-ak_jzVuEUfiI-Aq1IcDw9ISlOBdy8SaUDIlgR-WEOBSvyBuRPoc_YfLU3Ukwlge3NRwpMofslwfwlXL9AKJyGiVdfOp4iRtPY1vdqdtxIfEal_uQXWyutf7PawWLQAoqcrwHNod252RfNN7c=)
12. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI-GPrTGO-f6gTz6HilaK18d7yG58htgxQb7_YWUe4qZZev6q8RhfAod8o7lXXHyxpP3NxwMHTnYywf174IeZc2RiCujlZIs5kDuqX71RhLB5czd12qzETA84BBrGTEvECRt-29AeCneX_AlZluP-JdRcqkemIfZiEUXiTRxVJ2zjbVkWti3ijPWZyguJ9KlbHVz4Ugcv8s4Q=)
13. [daytrading.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWMIdhsCl6_lWUjxEHQXJjF29eb0FqZyPw1hhoUxsa37vErYik2zOoDYZXjc5ay7FblZQkWLtMVRVxP7k-1IYppAdm2pclqrVg1c4TlCI3h4APV-MH9nvv5QleV8qFILTQOpxj6uiPmqEB67R6Ss4TsPyBA5NWtB9K4ENSvpTp5Mcw)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsdKvfEzFprUaFab9E4-iVVCLAECDssfqjLvQ3fqIeRVxg-aTvh4r2bM75BrQM1460nCfeMKXTnuKN9IIjc-IXXzlonDmpoWm0_ZxuM-9jHIT2ugpMfcvqiXtaZvtdOFM-fpjFcxFA1irixTE38Sa5WbFKU6JhO7V2zc7en_Y4ILGdvhNSgqxsThcAhSZeI_kkrDq2-g0rUtn8ck2aeZPhlfP2kNTLdx3iuzdTPS4svTEsgFfz1Ve-)
15. [hazelcast.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFr3nU0yxpc-GI8SFitoJN9D3zPffbKXTijDpBFOFJSMFMpXN4FQgfeFHpoJdB_qqNpQspusYPP_3cEVw2iRXaKniAQHNr8Ng5ZWUUG4ZZNpN-HkfP2c8FJTl-VbKv0lr_iibxYSS5jwC0-ZUcVQIhfoXfwnwm_KZQu52LxujKvMfA7MVj2r6uouRYo0Cnyr72VxxEGtHonKsZH0ZI=)
16. [itnext.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGroV9SUzWDf_1iy5Y-N9i8b1JrgiGjV7sGw5sFgoVturx88Z_t7HTFEr7GjvNyPHvAD21LIjJ-P8smUXDNhEcSjjWKm1NarTgMAxGFogjHaYJ7zcvYz4brn1MiORSQA1gvISFnPq-sKRzfv9QVu8Cg2A6b35or0HwxVt4kUoAhqk366eMbtjg=)
17. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHF_vi6qorkU45uz_jxyqu0ZAsaCncFD_RN_xhvEDFp95PA1CpJuvqHEwQ5UoNPFMoe5akBjbFHGQyOzOXNs7yfqK0O8wrzk5lO0H_RmqnxZebLsXwpmMJFCMqSjSBw)
18. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5KDOTnxKWGpYu_qyZRVZlg86wRMzh90ZhprV2-HxJ_kIJvZnDcO0gOkBFh1Bt-rV9vA_IAl-o_qguraA4xC3XKgrVTGKNNf3rwyRb3eXAKp9J30SZtmJiIqQeoCwqMmwx7EqmEZNjoThQ12uiu6tS6zejaa30xcDgVi4rSYLePLr-dGORSQVLu6wImkaQKJvsQQq4V0GS8w==)
19. [systemdesignschool.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHL95vaibWCcjgI2WmDl2MlEp-gHTv8VWeUCJCol-CkBlpVcdxCJkkxaa5E7KbpROgkeHW95a46Pm8X9GiO_LHXUeTHfi5T_mNEgGzbW2PdWYo96zgtlwm0zKV5TgxOqmrTwl3uNcv8unE6BCm2m4K4n2OlzNG63565VnZdeAUE_2nG)
20. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkV9trxLtxnV7bk57vcntjFUANLUWabhgYxsmev3KEeMhCNfjPu8gtuv-UFRDLbfcpKdKdW6IEdGgUgRTl7L-DN9ncx7IhFBI5F1wej4LnCIEI1ToU6FazDEWBJQC4SIGyO40G8nKhatc2PAsmP8StrtcaOw06qtoyKCoIJJf762IhZQXaAIFxf9ihoSRiRUrvwtauN8PAZgP99w1WKLADSuBvq0Eu1dmi6BuUNRQ=)
21. [algocademy.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqSwInWtMLfwtwMXKbdzkiy9EXYOvWjP-Wd-6pNE21WwvpXc6o6r5MDxXuTULpBg13DD7fOLqjlkoIIYrE2F2OOmyYBmWARsfjKdkGPJmZF7aGfQMXPz3bD8WSsARgGZt0FGLDdGnc4dMrsER83E8ce_DN0ELcdluWvEp_il3uVE1oBnXnhK9YiIVQ4ng4PLt30FaPd9RlBYdB47rNkhobCQ==)
22. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV40GprmJU_h_NEbRIf4Ae9RDjwQVmGrDq9sBZNkPGIGeKJIL9TOBwJ11ImRelhQLBQyA88CjrA6Kg63IpkN_dk65T2F8QFoGNyYe3xZXiqU-L15qwaH-wztWGc4g2JTg=)
23. [dzone.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMLqMAGdVAFVVfbLIsB5p-P7IeV1KwAfO0YGQsNoI9eh3RAqWzmMICdapJ29HoHaFVbJrqVm56Det77SbQgQH3ivZ-RR3opD5Z_dAAFnMEgm6_SCsxbUmTRwqfnPy1Nkxf38X2yKeCEAKfuJGlntNAibux4uF5dsrMy6HdIT1CG8OF2G6L)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJKMcJ3wLYcJmhcSiKmCJfE66Y9jj0aqxR1TvU7xPwgkSf7tvy260qtRy0x25dC9WQykXaZaQW8S2z88KyT04CJ-miuEmNbdeHnLEI5ZEZr4Wfnh2vt80sNL-UiZsbBHBWZDj6ZEG1zj4q-VR6Y4DFwhgJQPGz_bGMfJEVJYZ-5bzpJ-peti0KMpA6TJAk4fVGQNQBo3KvEEU59kkXdRuI1rKor7kSo6C1S8-2wA==)
25. [gitconnected.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSOC3lxv5q-oN5eLE5-9vOgsT9hN-m7nLUJYbwoYw2oc_-00klJa-kjoxwGg72VWNEZvJfuyVOe4tmQYk1dHmCNmUkzf4YfxBRXb4LCDyKb61tsPBZBC5LCT9LOfoN5BIjSoJPV30xBbM-0llc7c6T4kxdcmiGyk2f3E6s18UtDIC9gw58XXvq2cHlOTo0vexlvyGYcHLJ0D-FyDyLJJE=)
26. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDpH8CvlKn7WKhfS_4vHAprc3f4DWTnyLX9a3jp4T7_SAhq5EBDebyuj5xP7-PyUApuXLON5HQJQuJQp5UO_IU2QoYm-6wzkPeI9g4w0Hbe_j16TBKGLML7vqwCSSIdUN1G_g5a3e4Fh23VvhvFTqRqtxudFsDMdrJSw1sdCOYBT_DpiLyN9tYV_4U3i_hWjk6ZYgK5jNjdaGSRlM=)
27. [dev.to](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf3BnmifCRg-oenJe_HgqBqELLDRpRWxBKcfCJ7lYaL7x0UivYp7uVfOzsZKf7cf2_kmLrnZKCWNq5JNpSTpEpOQAuZAhg4lK6PMBHOZ_sw1eBm8-ZnsnhE9cnFl3jfUvcq9WOE1Mb8A5NmINcROe6dsxH2iK0nVKU5NpI39pR4mFt-bJ4i_8iEJ1q9ahFNdJhq6qsHGfBREHovNplMQxgNNEGbz7nptgbEDkhMA==)
28. [microsoft.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpyVpf7rcBH4nmJ0yLet0rtCkuINfnsmXsd2LnhWfy1kQLsxR2Ua_Z0e06UIrrKhXWP97Twhq5xcZEonPrMmCBxceN8__hdsAmNeJNOy3wkAzDGc7i2X8c3YyM3jj4xLRPsAX05YNaQJuOLBj86PU6CpyL_k-PFCX1-rXdR1WU543h)
29. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmq9JiLTnYxei5cRpRKKLBfVGs9ShRgmrOIPnFLHp5iCS78bBPs3LtBqLkL5nYbIj7m6zyl7VuVQWbu_oeflfhiL0tM4YMt70etO1AW31QI_3QTq43nyMQGT0kUhBkefkjbPv19Mlu_qVVpxY3pYmApw==)
30. [ibm.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFaHPnIYjsmFOtc5ZQWSTJVccQL60tzk_Xf05nM1Y4K6Td5Qrx3hinPtFO5BmlAm4aQjTXyFo46PkkCF2GJN9b7JuWGddNyRiJjYAU3IZsUXaCIqKgyIQrBZe-Vl1CYOrwK_32zoDKBl3pvkT_Z9-jI5mo)
31. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESnQGcd9Gdw7s593QwO9rQ9wJ02VMQDu7WmQBmGXOB9EEOfKAa3Kb4jn_vESacjHy2bM1G2jCgpLJvCYeHqqTSTKrjdDEL2ZcYF2eNE7FZhlTdni_6QK8djbmkPbCH0ZCXq8FY_tdglL4wFGLNiO0QozURa3Hmzxvj6SR-_KbClgQOSsxbXBz94Aw4RV5hUMXPGr9Zjk--1fFO3w==)
32. [temporal.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERSniSY8ALVQDAK-QXvnSdxAjobr-NxysTB773roIUGzNvtfIkXhh1eg6_BWtWvjFp501GLTs2cDCTBKsv6NJqtqk_s-u53Jy7a1rmMN9fVpBB_dB6CvSypkBhUIg-IVX8IVWsEvaufQGA8q4LTJ66vwVR)
33. [solace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuxxG9yJbgl8AiqZSFYrAnRM1TGNKErozCAeVshWZj6B3Q4hiIlC5Y0qGpTxwo4rG5IzRi5W6B_u9Gsg3Vqr-tLe_LNWvLLI-0zYQi-daZdPzzA1eckDpHz-OBV_l3QV9eCQLnHgE0VIhBfQ==)
34. [journalwjarr.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8fYhTUS0ldox4W90U5OXaID8LC-egtQG5xfTpbxrYqCUNn8KEeAU4rF3nsYPm2oLqke0S5n7Sws1yH0hrAdEMuFuwTJW5oDS4OwY0V4CRw0M4TY84K7IsSRIcO2Kf5A1-w4FDP7la1vfNBUDXvbQRat0UXc62UOMnUR5-WZGnIuky)
35. [martinfowler.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJRr2PlCiHmfHB_ivY_KGL9s3Kr63wmcvFwqFQpWxPbAPZGVTasORw0PQn0E8l8-hICgsM5nlsE-ClD0umvqug_iqGcNa4Jm-ykeVlCEY24CjVJsXbxtcStgONrhKnnEo=)
36. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE69UH8eH3genQDIEmFou-mymWElNt-Fowpj8z5BBDj4EJfLg2xidObokniC0NCuS5Jz-422HNyJhsg3OR1GSU4URPYyXy57z6mgnmRaN8TbzhFpcpjN0-vvNiAVgL05iHCcROQynSOlI68y8KK)
37. [dev.to](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7g7RCMP54CdBb_OukoKZn6IzjSCGAUf3WKVSwEXIHfGHuvsXNVUyb9OFIwjyoBLv-yZdj58MqNSsDyt9lWw7RTD-DYHnCm5lddyD4f3s6NcIk1uzLCnKK3iNCoBHzW8aI1OSVMPFdwsKQTmga2pBF_vkQDBnOpPZbEoq0phLMcBDy8Hk=)
38. [eu-opensci.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGB_oV618nq_V0-9BiT6w4PpO7xTRwHfacTy-hwmKc94jDxPuOHwUSYHrpxKodzm6WYgdV6h6opwUqZrpZ1EoRM3QOY40C7pJlrGscdvDVS0FNLYmnnK7pwgro-GIzjnBc_0IB3T6jp-mSfyBrvjACf-JI=)
39. [alignment-systems.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGE-4Ns4GgosUraxBDQqiDKDO-8O9uu-NCbltfXOwwHTVLvUBrmuBEaIogI2PciCtAwkCg3CPerMVUgIADX2PphHDulVUwdInIQlmZFaHjN5pPt4UnnFxCW5QtdEMG1K6e4HngkxVjKiJoWU0Hju2j1)
40. [tradersmagazine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4m0zmclZ7GPOMHso8VpsAbaC4uZdmbWtv5vuaP5OfhtjdgmJOSQydoxJGQK8wd6ioX6Fj2EwbPmIErzLvn0OQLguHgremAMEfcjkp3I4f8eBKnVNRA-LOd8UyGlOrazo1LZ89goKDDYf3EWsPOl2R5LP9K_DC4ruyNNAqoJgEdk4-AMNvT6BpwcfCR6XBfzvIgmUJjtc=)
41. [terms.law](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHA1sD4PqfSGbwZpVb5vt1i2m_Cm6r2EyUx2Xz0qa_8yKPohDECyAv2_ENe_q_xxd7skGaEzKtGhyKeNjMkCHcrw9_GJxFSLSRm_ZGtAJEFV4pMBP4JRnETcXTg229CTsL_sSG2jzNMJqg6Vi7-WIezTg-JAhNT1RZSAXU0BxQU)
42. [institutionalinvestor.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuMMFM4CThbUBs2llmRL-7vxnfqM14Nt6Tw6RNIbEF7Lk-145XANW45grfAz1SPCmIWUMTkXVGrYuZxDw8Gq-yOehaLJK7ygD7QdY3cOuH6KgWF7FCOgtBfVY0z86x2V4ARBi7hUtLCkN1QyqEg2Sm9X9hTjyBJXlW3xq4tEpZqVqF-FdRVltd_yQE1AY0Uqap-ETJtaHw--x4swd2)
43. [pmc.gov.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExHOGUpFRxK0u6Tguggn8DlH3G4MO1TZrrmDdFhLPaprevWG9RuCZOQohp0tNKl8urjdhfycC3grHUs8lxM8knSJrNJgF6SGmjHXju2rSCZDLUiAOhWZk0gpeP4e5Q9kUVh7sUYNAfhXErvJvN8PULKwH9mu5OR7yHNx8dQNNBeoryYSxYWvD_veLz4QmhaK4SiFGaySWLQSVuNNkDQjiOpn5iw0G_5mNlIzI792n9sLsqaVyx7KIK-DJT0_LXZzionXjHFE03RJ0fag5HWW7ISk4CHw4=)
44. [irccl.in](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUKPjgryRxuGTeD_fJej-mVTN6tWa_Zm0LnQOU_rBJvvfz3314aFtOuTGFgf4pOE_LeqGF9xEjlHna9VZi4a-22aPaiECKfi2z4uqBxZrsFMD5YzAK8lWW6G-cs_nIWKNaG8xHJhuNZvZ6WieSrqV-hSHPInTnu9R4pe_HKerjehKYtvKaGY3gAdAJ6KlDgM5tIVtNFBB6uMRfDcOxp3ZYuTuAous=)
45. [nyif.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0iUF2d5ocCKlDaRsOBs0K6R0bsPhIICyRD-jaFc9kDIBfjQYDCQJJDPz-WNZez1JXS3jB6VP94ikzftXFputf0AzTq8AOlKjK7o209doLhZhFHgozQs57b0qxGgOonNc9hUjZQJuoDv6POuQcpiQbTIDxx9l0AODlphl6FCYllsfxuZE_)
46. [workday.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHl56jTNu_3iNUZnFI6dMKOFkarnCU_zBH__Oxx9YRrJ4yCZ1BCQSOyvcl51I8DuLqrQtYp9ClQ2ZbxQHTRWBrB0AhB1kdvqOFNs5SIZM3lCwVhsTLWLujf3CvA9ahR1r4hTlkfB07KG-VXa6o=)
47. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQG97sgWrvIZ9q8lmTwTy9Klk7rDWRqewNp0FlAqLPygVDtDIpBVWqnfjaXK-edx0Yh9upvdw9ymj9g0xltUBsIui2LtSQok6Fvih6KXtXW3YPbSOb_BlrIsrDphPSQBDOyl8aMeSdktm-xBaShKVIlBZ2QnPHrsAYr79VOkUS88sGgazkIeCkjgS2w34wqhml8C5JqMyzVk6UEu9yhM0loz1Qdr5eXcgvEy00w_Wkb9o=)


## Annotations
Annotation(end_index=3708, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhxtuyyLbEA_sLHjjAeJDUqFn_hbOjXDzi1UUkvuY9nT7uA7VpVWBet_SMxgGM8kwATZ7SHKwoIyiVGywOM5T1i7RkisEi_F9xIB2ACTXl8B5Uo8QFkuag4jiOHiPQpxUtFet5G58wOA2z2w==', start_index=3699)
Annotation(end_index=4228, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEn0ierwLTGlTBzZDxAZ1OJQAYitnQzhCnbLEKMDEX_vYdN6dnQ19LeOwizskTdC8uhtGGWSeRUgivdZeo0HdRrZi9lXNNuOapoc_rl2JTWfMu3wIlLbNyHZC3WsqUkHIFNRLyQl8twsxieLGylMttyM2YREs1-ZiboejOq7eDdU23NPznVABowLs-o-YebHZ1deLX7JQ==', start_index=4216)
Annotation(end_index=4228, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_z4hWZU0DoPatwBmXEgbC0aIH1wzCPqwyXGaDyvcYPsIK5k9iIOB8bUSSIvYQl2F78B4IZXZS1H4yk0CNMDfzl3Boa3yDvekjgt8dlJ3JTCtc7Gb9ReKYUHjmezjWupggfLjY_i5iXaC0ZSV2WeHbLneq8HDeFQ==', start_index=4216)
Annotation(end_index=4414, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQ1esNjTOHy3CmbDScz21MUbsi08w2Y37EVMsmeiFU2jCVezofhLXAMwao4lIb1dqni0Tc_jxkNjH1Das-GjVAL5hYilJIAotJMBUfrfF8djX4mqjJHYIO1s5TrB8PvlPnLEmANJSf69dwVp_62axWGg==', start_index=4402)
Annotation(end_index=4414, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSOvj5WeA_YMwJVxfva9uQqDlB1ymOx73qLCuvujUD8LHV6yPY_6EXRHoI2r2NEPcn3enm9uN7KEX0RaKHr4TvtLDGUUm8fEeN9Um3y1yqLCmYd8s5Ahjlxb9zjkWOgVpgAPzg9pFmNrpIM47bHAJLuzMF_5rZbvwDMWQtdeBYx9SL61m5Nr3V_o7rTXecTiEgtlxg_YmI7FITJd9PTIT4Og2OtVmsw8KxQ6gJ-uSn6A==', start_index=4402)
Annotation(end_index=4568, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSOvj5WeA_YMwJVxfva9uQqDlB1ymOx73qLCuvujUD8LHV6yPY_6EXRHoI2r2NEPcn3enm9uN7KEX0RaKHr4TvtLDGUUm8fEeN9Um3y1yqLCmYd8s5Ahjlxb9zjkWOgVpgAPzg9pFmNrpIM47bHAJLuzMF_5rZbvwDMWQtdeBYx9SL61m5Nr3V_o7rTXecTiEgtlxg_YmI7FITJd9PTIT4Og2OtVmsw8KxQ6gJ-uSn6A==', start_index=4559)
Annotation(end_index=4744, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcLCm8LlzpnVWVDZvK6aUr_20P3Xbqs-7mAghE1abSW6q19QHGW3WL_UWHuQ1x6VOwUwHbVsa0CSarv99Vc0pRzOzCQBYKCqLsC_HIwmLR3-LLqfkTt-LhR6s7mS58bgg3LJcDpK643v4VgXC1O6aa1F5QKeCSKHGvvbEDogeAC-S3w6JJj1tJmXw6EKqVr3WPu1udcgCTUbSkytkhDPIQRM3OmJuHLd_yST7_VlQ=', start_index=4732)
Annotation(end_index=4744, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_z4hWZU0DoPatwBmXEgbC0aIH1wzCPqwyXGaDyvcYPsIK5k9iIOB8bUSSIvYQl2F78B4IZXZS1H4yk0CNMDfzl3Boa3yDvekjgt8dlJ3JTCtc7Gb9ReKYUHjmezjWupggfLjY_i5iXaC0ZSV2WeHbLneq8HDeFQ==', start_index=4732)
Annotation(end_index=5314, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENJi0hCsk65nnKueo-upzvinDzoH3ePr-W1ohEIgAhn8jIBjg3EJVPqQGdR6qs3zSYb7kEPIH1DzeBEOIhsm_AJilVsdgdHqs39ILLbK4-8Yn0X-xLMSYNPv29amE8g4Ndho828X_pbAIcRkdYd-wnNB8Cm3JpLnlqu1DawUn1Cb4hVniRwcq-liaO_oTJVrj6vLzwZvYdK6J5xzTX8LP7tH2ycW-uzrfPnyvK', start_index=5302)
Annotation(end_index=5314, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy-FufNzbdYdcd7vHZJMyAOmThqvyQ0nAR-xCejYYlGs-NX0sqhhIGhVGCxTsvkehTNd2_0k0wm4rwn2cS4k84zc5UHzxgpODFpd-Ai-tFtJ5dlztwdRTQnDf3DGRytqhs78ui', start_index=5302)
Annotation(end_index=5987, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENJi0hCsk65nnKueo-upzvinDzoH3ePr-W1ohEIgAhn8jIBjg3EJVPqQGdR6qs3zSYb7kEPIH1DzeBEOIhsm_AJilVsdgdHqs39ILLbK4-8Yn0X-xLMSYNPv29amE8g4Ndho828X_pbAIcRkdYd-wnNB8Cm3JpLnlqu1DawUn1Cb4hVniRwcq-liaO_oTJVrj6vLzwZvYdK6J5xzTX8LP7tH2ycW-uzrfPnyvK', start_index=5975)
Annotation(end_index=5987, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy-FufNzbdYdcd7vHZJMyAOmThqvyQ0nAR-xCejYYlGs-NX0sqhhIGhVGCxTsvkehTNd2_0k0wm4rwn2cS4k84zc5UHzxgpODFpd-Ai-tFtJ5dlztwdRTQnDf3DGRytqhs78ui', start_index=5975)
Annotation(end_index=6636, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEegdMbDVARWY87lDNAX3foadAGSycuIDEQvSDsv7gm0b7qkC_lUrFD0FmCuJQF2IY_o9tzwkoFL-Ju12mCTYgcHi_v3J8WASD3xxj0G_97BMajDWHTxm5o1izvy4gIU4dgJPl738=', start_index=6620)
Annotation(end_index=6636, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEn0ierwLTGlTBzZDxAZ1OJQAYitnQzhCnbLEKMDEX_vYdN6dnQ19LeOwizskTdC8uhtGGWSeRUgivdZeo0HdRrZi9lXNNuOapoc_rl2JTWfMu3wIlLbNyHZC3WsqUkHIFNRLyQl8twsxieLGylMttyM2YREs1-ZiboejOq7eDdU23NPznVABowLs-o-YebHZ1deLX7JQ==', start_index=6620)
Annotation(end_index=6636, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHf9cpt9DRInY830Uem_LIlUizIlTdxGlz1e2yxWCRCqQJhoDBKgYhKWeEfTO2Z55kNM_6W28JVdJ4RNX8sslGJHj58yImljOoQefKcdAPYSDowg6lE3j4AvZ2r2kLCcmD59pQSWfwx_xJnK7-Nin9nTtylQT8vR-o1iUxeD6OPfOo-_RKK50yZGP-JPBpBpYHLpHHldlmNffaN8p_ETA3I', start_index=6620)
Annotation(end_index=6827, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEegdMbDVARWY87lDNAX3foadAGSycuIDEQvSDsv7gm0b7qkC_lUrFD0FmCuJQF2IY_o9tzwkoFL-Ju12mCTYgcHi_v3J8WASD3xxj0G_97BMajDWHTxm5o1izvy4gIU4dgJPl738=', start_index=6818)
Annotation(end_index=7293, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENJi0hCsk65nnKueo-upzvinDzoH3ePr-W1ohEIgAhn8jIBjg3EJVPqQGdR6qs3zSYb7kEPIH1DzeBEOIhsm_AJilVsdgdHqs39ILLbK4-8Yn0X-xLMSYNPv29amE8g4Ndho828X_pbAIcRkdYd-wnNB8Cm3JpLnlqu1DawUn1Cb4hVniRwcq-liaO_oTJVrj6vLzwZvYdK6J5xzTX8LP7tH2ycW-uzrfPnyvK', start_index=7281)
Annotation(end_index=7293, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEn0ierwLTGlTBzZDxAZ1OJQAYitnQzhCnbLEKMDEX_vYdN6dnQ19LeOwizskTdC8uhtGGWSeRUgivdZeo0HdRrZi9lXNNuOapoc_rl2JTWfMu3wIlLbNyHZC3WsqUkHIFNRLyQl8twsxieLGylMttyM2YREs1-ZiboejOq7eDdU23NPznVABowLs-o-YebHZ1deLX7JQ==', start_index=7281)
Annotation(end_index=7626, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7cWut0D-yBAWtsSLqKlHFCnBy2S-ak_jzVuEUfiI-Aq1IcDw9ISlOBdy8SaUDIlgR-WEOBSvyBuRPoc_YfLU3Ukwlge3NRwpMofslwfwlXL9AKJyGiVdfOp4iRtPY1vdqdtxIfEal_uQXWyutf7PawWLQAoqcrwHNod252RfNN7c=', start_index=7616)
Annotation(end_index=7962, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI-GPrTGO-f6gTz6HilaK18d7yG58htgxQb7_YWUe4qZZev6q8RhfAod8o7lXXHyxpP3NxwMHTnYywf174IeZc2RiCujlZIs5kDuqX71RhLB5czd12qzETA84BBrGTEvECRt-29AeCneX_AlZluP-JdRcqkemIfZiEUXiTRxVJ2zjbVkWti3ijPWZyguJ9KlbHVz4Ugcv8s4Q=', start_index=7948)
Annotation(end_index=7962, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWMIdhsCl6_lWUjxEHQXJjF29eb0FqZyPw1hhoUxsa37vErYik2zOoDYZXjc5ay7FblZQkWLtMVRVxP7k-1IYppAdm2pclqrVg1c4TlCI3h4APV-MH9nvv5QleV8qFILTQOpxj6uiPmqEB67R6Ss4TsPyBA5NWtB9K4ENSvpTp5Mcw', start_index=7948)
Annotation(end_index=8265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWMIdhsCl6_lWUjxEHQXJjF29eb0FqZyPw1hhoUxsa37vErYik2zOoDYZXjc5ay7FblZQkWLtMVRVxP7k-1IYppAdm2pclqrVg1c4TlCI3h4APV-MH9nvv5QleV8qFILTQOpxj6uiPmqEB67R6Ss4TsPyBA5NWtB9K4ENSvpTp5Mcw', start_index=8251)
Annotation(end_index=8265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsdKvfEzFprUaFab9E4-iVVCLAECDssfqjLvQ3fqIeRVxg-aTvh4r2bM75BrQM1460nCfeMKXTnuKN9IIjc-IXXzlonDmpoWm0_ZxuM-9jHIT2ugpMfcvqiXtaZvtdOFM-fpjFcxFA1irixTE38Sa5WbFKU6JhO7V2zc7en_Y4ILGdvhNSgqxsThcAhSZeI_kkrDq2-g0rUtn8ck2aeZPhlfP2kNTLdx3iuzdTPS4svTEsgFfz1Ve-', start_index=8251)
Annotation(end_index=8510, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7cWut0D-yBAWtsSLqKlHFCnBy2S-ak_jzVuEUfiI-Aq1IcDw9ISlOBdy8SaUDIlgR-WEOBSvyBuRPoc_YfLU3Ukwlge3NRwpMofslwfwlXL9AKJyGiVdfOp4iRtPY1vdqdtxIfEal_uQXWyutf7PawWLQAoqcrwHNod252RfNN7c=', start_index=8496)
Annotation(end_index=8510, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWMIdhsCl6_lWUjxEHQXJjF29eb0FqZyPw1hhoUxsa37vErYik2zOoDYZXjc5ay7FblZQkWLtMVRVxP7k-1IYppAdm2pclqrVg1c4TlCI3h4APV-MH9nvv5QleV8qFILTQOpxj6uiPmqEB67R6Ss4TsPyBA5NWtB9K4ENSvpTp5Mcw', start_index=8496)
Annotation(end_index=9122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFr3nU0yxpc-GI8SFitoJN9D3zPffbKXTijDpBFOFJSMFMpXN4FQgfeFHpoJdB_qqNpQspusYPP_3cEVw2iRXaKniAQHNr8Ng5ZWUUG4ZZNpN-HkfP2c8FJTl-VbKv0lr_iibxYSS5jwC0-ZUcVQIhfoXfwnwm_KZQu52LxujKvMfA7MVj2r6uouRYo0Cnyr72VxxEGtHonKsZH0ZI=', start_index=9104)
Annotation(end_index=9122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGroV9SUzWDf_1iy5Y-N9i8b1JrgiGjV7sGw5sFgoVturx88Z_t7HTFEr7GjvNyPHvAD21LIjJ-P8smUXDNhEcSjjWKm1NarTgMAxGFogjHaYJ7zcvYz4brn1MiORSQA1gvISFnPq-sKRzfv9QVu8Cg2A6b35or0HwxVt4kUoAhqk366eMbtjg=', start_index=9104)
Annotation(end_index=9122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHF_vi6qorkU45uz_jxyqu0ZAsaCncFD_RN_xhvEDFp95PA1CpJuvqHEwQ5UoNPFMoe5akBjbFHGQyOzOXNs7yfqK0O8wrzk5lO0H_RmqnxZebLsXwpmMJFCMqSjSBw', start_index=9104)
Annotation(end_index=9512, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5KDOTnxKWGpYu_qyZRVZlg86wRMzh90ZhprV2-HxJ_kIJvZnDcO0gOkBFh1Bt-rV9vA_IAl-o_qguraA4xC3XKgrVTGKNNf3rwyRb3eXAKp9J30SZtmJiIqQeoCwqMmwx7EqmEZNjoThQ12uiu6tS6zejaa30xcDgVi4rSYLePLr-dGORSQVLu6wImkaQKJvsQQq4V0GS8w==', start_index=9498)
Annotation(end_index=9512, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGroV9SUzWDf_1iy5Y-N9i8b1JrgiGjV7sGw5sFgoVturx88Z_t7HTFEr7GjvNyPHvAD21LIjJ-P8smUXDNhEcSjjWKm1NarTgMAxGFogjHaYJ7zcvYz4brn1MiORSQA1gvISFnPq-sKRzfv9QVu8Cg2A6b35or0HwxVt4kUoAhqk366eMbtjg=', start_index=9498)
Annotation(end_index=9875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkV9trxLtxnV7bk57vcntjFUANLUWabhgYxsmev3KEeMhCNfjPu8gtuv-UFRDLbfcpKdKdW6IEdGgUgRTl7L-DN9ncx7IhFBI5F1wej4LnCIEI1ToU6FazDEWBJQC4SIGyO40G8nKhatc2PAsmP8StrtcaOw06qtoyKCoIJJf762IhZQXaAIFxf9ihoSRiRUrvwtauN8PAZgP99w1WKLADSuBvq0Eu1dmi6BuUNRQ=', start_index=9861)
Annotation(end_index=9875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHL95vaibWCcjgI2WmDl2MlEp-gHTv8VWeUCJCol-CkBlpVcdxCJkkxaa5E7KbpROgkeHW95a46Pm8X9GiO_LHXUeTHfi5T_mNEgGzbW2PdWYo96zgtlwm0zKV5TgxOqmrTwl3uNcv8unE6BCm2m4K4n2OlzNG63565VnZdeAUE_2nG', start_index=9861)
Annotation(end_index=10183, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV40GprmJU_h_NEbRIf4Ae9RDjwQVmGrDq9sBZNkPGIGeKJIL9TOBwJ11ImRelhQLBQyA88CjrA6Kg63IpkN_dk65T2F8QFoGNyYe3xZXiqU-L15qwaH-wztWGc4g2JTg=', start_index=10169)
Annotation(end_index=10183, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqSwInWtMLfwtwMXKbdzkiy9EXYOvWjP-Wd-6pNE21WwvpXc6o6r5MDxXuTULpBg13DD7fOLqjlkoIIYrE2F2OOmyYBmWARsfjKdkGPJmZF7aGfQMXPz3bD8WSsARgGZt0FGLDdGnc4dMrsER83E8ce_DN0ELcdluWvEp_il3uVE1oBnXnhK9YiIVQ4ng4PLt30FaPd9RlBYdB47rNkhobCQ==', start_index=10169)
Annotation(end_index=10558, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV40GprmJU_h_NEbRIf4Ae9RDjwQVmGrDq9sBZNkPGIGeKJIL9TOBwJ11ImRelhQLBQyA88CjrA6Kg63IpkN_dk65T2F8QFoGNyYe3xZXiqU-L15qwaH-wztWGc4g2JTg=', start_index=10548)
Annotation(end_index=11048, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJKMcJ3wLYcJmhcSiKmCJfE66Y9jj0aqxR1TvU7xPwgkSf7tvy260qtRy0x25dC9WQykXaZaQW8S2z88KyT04CJ-miuEmNbdeHnLEI5ZEZr4Wfnh2vt80sNL-UiZsbBHBWZDj6ZEG1zj4q-VR6Y4DFwhgJQPGz_bGMfJEVJYZ-5bzpJ-peti0KMpA6TJAk4fVGQNQBo3KvEEU59kkXdRuI1rKor7kSo6C1S8-2wA==', start_index=11034)
Annotation(end_index=11048, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMLqMAGdVAFVVfbLIsB5p-P7IeV1KwAfO0YGQsNoI9eh3RAqWzmMICdapJ29HoHaFVbJrqVm56Det77SbQgQH3ivZ-RR3opD5Z_dAAFnMEgm6_SCsxbUmTRwqfnPy1Nkxf38X2yKeCEAKfuJGlntNAibux4uF5dsrMy6HdIT1CG8OF2G6L', start_index=11034)
Annotation(end_index=11981, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf3BnmifCRg-oenJe_HgqBqELLDRpRWxBKcfCJ7lYaL7x0UivYp7uVfOzsZKf7cf2_kmLrnZKCWNq5JNpSTpEpOQAuZAhg4lK6PMBHOZ_sw1eBm8-ZnsnhE9cnFl3jfUvcq9WOE1Mb8A5NmINcROe6dsxH2iK0nVKU5NpI39pR4mFt-bJ4i_8iEJ1q9ahFNdJhq6qsHGfBREHovNplMQxgNNEGbz7nptgbEDkhMA==', start_index=11963)
Annotation(end_index=11981, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDpH8CvlKn7WKhfS_4vHAprc3f4DWTnyLX9a3jp4T7_SAhq5EBDebyuj5xP7-PyUApuXLON5HQJQuJQp5UO_IU2QoYm-6wzkPeI9g4w0Hbe_j16TBKGLML7vqwCSSIdUN1G_g5a3e4Fh23VvhvFTqRqtxudFsDMdrJSw1sdCOYBT_DpiLyN9tYV_4U3i_hWjk6ZYgK5jNjdaGSRlM=', start_index=11963)
Annotation(end_index=11981, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSOC3lxv5q-oN5eLE5-9vOgsT9hN-m7nLUJYbwoYw2oc_-00klJa-kjoxwGg72VWNEZvJfuyVOe4tmQYk1dHmCNmUkzf4YfxBRXb4LCDyKb61tsPBZBC5LCT9LOfoN5BIjSoJPV30xBbM-0llc7c6T4kxdcmiGyk2f3E6s18UtDIC9gw58XXvq2cHlOTo0vexlvyGYcHLJ0D-FyDyLJJE=', start_index=11963)
Annotation(end_index=12164, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmq9JiLTnYxei5cRpRKKLBfVGs9ShRgmrOIPnFLHp5iCS78bBPs3LtBqLkL5nYbIj7m6zyl7VuVQWbu_oeflfhiL0tM4YMt70etO1AW31QI_3QTq43nyMQGT0kUhBkefkjbPv19Mlu_qVVpxY3pYmApw==', start_index=12150)
Annotation(end_index=12164, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpyVpf7rcBH4nmJ0yLet0rtCkuINfnsmXsd2LnhWfy1kQLsxR2Ua_Z0e06UIrrKhXWP97Twhq5xcZEonPrMmCBxceN8__hdsAmNeJNOy3wkAzDGc7i2X8c3YyM3jj4xLRPsAX05YNaQJuOLBj86PU6CpyL_k-PFCX1-rXdR1WU543h', start_index=12150)
Annotation(end_index=12307, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFaHPnIYjsmFOtc5ZQWSTJVccQL60tzk_Xf05nM1Y4K6Td5Qrx3hinPtFO5BmlAm4aQjTXyFo46PkkCF2GJN9b7JuWGddNyRiJjYAU3IZsUXaCIqKgyIQrBZe-Vl1CYOrwK_32zoDKBl3pvkT_Z9-jI5mo', start_index=12297)
Annotation(end_index=12812, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENJi0hCsk65nnKueo-upzvinDzoH3ePr-W1ohEIgAhn8jIBjg3EJVPqQGdR6qs3zSYb7kEPIH1DzeBEOIhsm_AJilVsdgdHqs39ILLbK4-8Yn0X-xLMSYNPv29amE8g4Ndho828X_pbAIcRkdYd-wnNB8Cm3JpLnlqu1DawUn1Cb4hVniRwcq-liaO_oTJVrj6vLzwZvYdK6J5xzTX8LP7tH2ycW-uzrfPnyvK', start_index=12795)
Annotation(end_index=12812, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERSniSY8ALVQDAK-QXvnSdxAjobr-NxysTB773roIUGzNvtfIkXhh1eg6_BWtWvjFp501GLTs2cDCTBKsv6NJqtqk_s-u53Jy7a1rmMN9fVpBB_dB6CvSypkBhUIg-IVX8IVWsEvaufQGA8q4LTJ66vwVR', start_index=12795)
Annotation(end_index=12812, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESnQGcd9Gdw7s593QwO9rQ9wJ02VMQDu7WmQBmGXOB9EEOfKAa3Kb4jn_vESacjHy2bM1G2jCgpLJvCYeHqqTSTKrjdDEL2ZcYF2eNE7FZhlTdni_6QK8djbmkPbCH0ZCXq8FY_tdglL4wFGLNiO0QozURa3Hmzxvj6SR-_KbClgQOSsxbXBz94Aw4RV5hUMXPGr9Zjk--1fFO3w==', start_index=12795)
Annotation(end_index=13224, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8fYhTUS0ldox4W90U5OXaID8LC-egtQG5xfTpbxrYqCUNn8KEeAU4rF3nsYPm2oLqke0S5n7Sws1yH0hrAdEMuFuwTJW5oDS4OwY0V4CRw0M4TY84K7IsSRIcO2Kf5A1-w4FDP7la1vfNBUDXvbQRat0UXc62UOMnUR5-WZGnIuky', start_index=13210)
Annotation(end_index=13224, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuxxG9yJbgl8AiqZSFYrAnRM1TGNKErozCAeVshWZj6B3Q4hiIlC5Y0qGpTxwo4rG5IzRi5W6B_u9Gsg3Vqr-tLe_LNWvLLI-0zYQi-daZdPzzA1eckDpHz-OBV_l3QV9eCQLnHgE0VIhBfQ==', start_index=13210)
Annotation(end_index=13849, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE69UH8eH3genQDIEmFou-mymWElNt-Fowpj8z5BBDj4EJfLg2xidObokniC0NCuS5Jz-422HNyJhsg3OR1GSU4URPYyXy57z6mgnmRaN8TbzhFpcpjN0-vvNiAVgL05iHCcROQynSOlI68y8KK', start_index=13832)
Annotation(end_index=13849, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcLCm8LlzpnVWVDZvK6aUr_20P3Xbqs-7mAghE1abSW6q19QHGW3WL_UWHuQ1x6VOwUwHbVsa0CSarv99Vc0pRzOzCQBYKCqLsC_HIwmLR3-LLqfkTt-LhR6s7mS58bgg3LJcDpK643v4VgXC1O6aa1F5QKeCSKHGvvbEDogeAC-S3w6JJj1tJmXw6EKqVr3WPu1udcgCTUbSkytkhDPIQRM3OmJuHLd_yST7_VlQ=', start_index=13832)
Annotation(end_index=13849, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJRr2PlCiHmfHB_ivY_KGL9s3Kr63wmcvFwqFQpWxPbAPZGVTasORw0PQn0E8l8-hICgsM5nlsE-ClD0umvqug_iqGcNa4Jm-ykeVlCEY24CjVJsXbxtcStgONrhKnnEo=', start_index=13832)
Annotation(end_index=14125, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJRr2PlCiHmfHB_ivY_KGL9s3Kr63wmcvFwqFQpWxPbAPZGVTasORw0PQn0E8l8-hICgsM5nlsE-ClD0umvqug_iqGcNa4Jm-ykeVlCEY24CjVJsXbxtcStgONrhKnnEo=', start_index=14111)
Annotation(end_index=14125, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7g7RCMP54CdBb_OukoKZn6IzjSCGAUf3WKVSwEXIHfGHuvsXNVUyb9OFIwjyoBLv-yZdj58MqNSsDyt9lWw7RTD-DYHnCm5lddyD4f3s6NcIk1uzLCnKK3iNCoBHzW8aI1OSVMPFdwsKQTmga2pBF_vkQDBnOpPZbEoq0phLMcBDy8Hk=', start_index=14111)
Annotation(end_index=14366, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE69UH8eH3genQDIEmFou-mymWElNt-Fowpj8z5BBDj4EJfLg2xidObokniC0NCuS5Jz-422HNyJhsg3OR1GSU4URPYyXy57z6mgnmRaN8TbzhFpcpjN0-vvNiAVgL05iHCcROQynSOlI68y8KK', start_index=14356)
Annotation(end_index=15095, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGB_oV618nq_V0-9BiT6w4PpO7xTRwHfacTy-hwmKc94jDxPuOHwUSYHrpxKodzm6WYgdV6h6opwUqZrpZ1EoRM3QOY40C7pJlrGscdvDVS0FNLYmnnK7pwgro-GIzjnBc_0IB3T6jp-mSfyBrvjACf-JI=', start_index=15082)
Annotation(end_index=15095, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhxtuyyLbEA_sLHjjAeJDUqFn_hbOjXDzi1UUkvuY9nT7uA7VpVWBet_SMxgGM8kwATZ7SHKwoIyiVGywOM5T1i7RkisEi_F9xIB2ACTXl8B5Uo8QFkuag4jiOHiPQpxUtFet5G58wOA2z2w==', start_index=15082)
Annotation(end_index=15301, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGB_oV618nq_V0-9BiT6w4PpO7xTRwHfacTy-hwmKc94jDxPuOHwUSYHrpxKodzm6WYgdV6h6opwUqZrpZ1EoRM3QOY40C7pJlrGscdvDVS0FNLYmnnK7pwgro-GIzjnBc_0IB3T6jp-mSfyBrvjACf-JI=', start_index=15288)
Annotation(end_index=15301, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhxtuyyLbEA_sLHjjAeJDUqFn_hbOjXDzi1UUkvuY9nT7uA7VpVWBet_SMxgGM8kwATZ7SHKwoIyiVGywOM5T1i7RkisEi_F9xIB2ACTXl8B5Uo8QFkuag4jiOHiPQpxUtFet5G58wOA2z2w==', start_index=15288)
Annotation(end_index=15749, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGB_oV618nq_V0-9BiT6w4PpO7xTRwHfacTy-hwmKc94jDxPuOHwUSYHrpxKodzm6WYgdV6h6opwUqZrpZ1EoRM3QOY40C7pJlrGscdvDVS0FNLYmnnK7pwgro-GIzjnBc_0IB3T6jp-mSfyBrvjACf-JI=', start_index=15736)
Annotation(end_index=15749, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhxtuyyLbEA_sLHjjAeJDUqFn_hbOjXDzi1UUkvuY9nT7uA7VpVWBet_SMxgGM8kwATZ7SHKwoIyiVGywOM5T1i7RkisEi_F9xIB2ACTXl8B5Uo8QFkuag4jiOHiPQpxUtFet5G58wOA2z2w==', start_index=15736)
Annotation(end_index=16309, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4m0zmclZ7GPOMHso8VpsAbaC4uZdmbWtv5vuaP5OfhtjdgmJOSQydoxJGQK8wd6ioX6Fj2EwbPmIErzLvn0OQLguHgremAMEfcjkp3I4f8eBKnVNRA-LOd8UyGlOrazo1LZ89goKDDYf3EWsPOl2R5LP9K_DC4ruyNNAqoJgEdk4-AMNvT6BpwcfCR6XBfzvIgmUJjtc=', start_index=16291)
Annotation(end_index=16309, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGE-4Ns4GgosUraxBDQqiDKDO-8O9uu-NCbltfXOwwHTVLvUBrmuBEaIogI2PciCtAwkCg3CPerMVUgIADX2PphHDulVUwdInIQlmZFaHjN5pPt4UnnFxCW5QtdEMG1K6e4HngkxVjKiJoWU0Hju2j1', start_index=16291)
Annotation(end_index=16309, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHA1sD4PqfSGbwZpVb5vt1i2m_Cm6r2EyUx2Xz0qa_8yKPohDECyAv2_ENe_q_xxd7skGaEzKtGhyKeNjMkCHcrw9_GJxFSLSRm_ZGtAJEFV4pMBP4JRnETcXTg229CTsL_sSG2jzNMJqg6Vi7-WIezTg-JAhNT1RZSAXU0BxQU', start_index=16291)
Annotation(end_index=16546, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExHOGUpFRxK0u6Tguggn8DlH3G4MO1TZrrmDdFhLPaprevWG9RuCZOQohp0tNKl8urjdhfycC3grHUs8lxM8knSJrNJgF6SGmjHXju2rSCZDLUiAOhWZk0gpeP4e5Q9kUVh7sUYNAfhXErvJvN8PULKwH9mu5OR7yHNx8dQNNBeoryYSxYWvD_veLz4QmhaK4SiFGaySWLQSVuNNkDQjiOpn5iw0G_5mNlIzI792n9sLsqaVyx7KIK-DJT0_LXZzionXjHFE03RJ0fag5HWW7ISk4CHw4=', start_index=16528)
Annotation(end_index=16546, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4m0zmclZ7GPOMHso8VpsAbaC4uZdmbWtv5vuaP5OfhtjdgmJOSQydoxJGQK8wd6ioX6Fj2EwbPmIErzLvn0OQLguHgremAMEfcjkp3I4f8eBKnVNRA-LOd8UyGlOrazo1LZ89goKDDYf3EWsPOl2R5LP9K_DC4ruyNNAqoJgEdk4-AMNvT6BpwcfCR6XBfzvIgmUJjtc=', start_index=16528)
Annotation(end_index=16546, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuMMFM4CThbUBs2llmRL-7vxnfqM14Nt6Tw6RNIbEF7Lk-145XANW45grfAz1SPCmIWUMTkXVGrYuZxDw8Gq-yOehaLJK7ygD7QdY3cOuH6KgWF7FCOgtBfVY0z86x2V4ARBi7hUtLCkN1QyqEg2Sm9X9hTjyBJXlW3xq4tEpZqVqF-FdRVltd_yQE1AY0Uqap-ETJtaHw--x4swd2', start_index=16528)
Annotation(end_index=16891, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUKPjgryRxuGTeD_fJej-mVTN6tWa_Zm0LnQOU_rBJvvfz3314aFtOuTGFgf4pOE_LeqGF9xEjlHna9VZi4a-22aPaiECKfi2z4uqBxZrsFMD5YzAK8lWW6G-cs_nIWKNaG8xHJhuNZvZ6WieSrqV-hSHPInTnu9R4pe_HKerjehKYtvKaGY3gAdAJ6KlDgM5tIVtNFBB6uMRfDcOxp3ZYuTuAous=', start_index=16877)
Annotation(end_index=16891, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0iUF2d5ocCKlDaRsOBs0K6R0bsPhIICyRD-jaFc9kDIBfjQYDCQJJDPz-WNZez1JXS3jB6VP94ikzftXFputf0AzTq8AOlKjK7o209doLhZhFHgozQs57b0qxGgOonNc9hUjZQJuoDv6POuQcpiQbTIDxx9l0AODlphl6FCYllsfxuZE_', start_index=16877)
Annotation(end_index=19185, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhxtuyyLbEA_sLHjjAeJDUqFn_hbOjXDzi1UUkvuY9nT7uA7VpVWBet_SMxgGM8kwATZ7SHKwoIyiVGywOM5T1i7RkisEi_F9xIB2ACTXl8B5Uo8QFkuag4jiOHiPQpxUtFet5G58wOA2z2w==', start_index=19176)
Annotation(end_index=19446, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSOvj5WeA_YMwJVxfva9uQqDlB1ymOx73qLCuvujUD8LHV6yPY_6EXRHoI2r2NEPcn3enm9uN7KEX0RaKHr4TvtLDGUUm8fEeN9Um3y1yqLCmYd8s5Ahjlxb9zjkWOgVpgAPzg9pFmNrpIM47bHAJLuzMF_5rZbvwDMWQtdeBYx9SL61m5Nr3V_o7rTXecTiEgtlxg_YmI7FITJd9PTIT4Og2OtVmsw8KxQ6gJ-uSn6A==', start_index=19437)
Annotation(end_index=19876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV40GprmJU_h_NEbRIf4Ae9RDjwQVmGrDq9sBZNkPGIGeKJIL9TOBwJ11ImRelhQLBQyA88CjrA6Kg63IpkN_dk65T2F8QFoGNyYe3xZXiqU-L15qwaH-wztWGc4g2JTg=', start_index=19863)
Annotation(end_index=19876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_z4hWZU0DoPatwBmXEgbC0aIH1wzCPqwyXGaDyvcYPsIK5k9iIOB8bUSSIvYQl2F78B4IZXZS1H4yk0CNMDfzl3Boa3yDvekjgt8dlJ3JTCtc7Gb9ReKYUHjmezjWupggfLjY_i5iXaC0ZSV2WeHbLneq8HDeFQ==', start_index=19863)
Annotation(end_index=20371, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEegdMbDVARWY87lDNAX3foadAGSycuIDEQvSDsv7gm0b7qkC_lUrFD0FmCuJQF2IY_o9tzwkoFL-Ju12mCTYgcHi_v3J8WASD3xxj0G_97BMajDWHTxm5o1izvy4gIU4dgJPl738=', start_index=20362)
Annotation(end_index=21554, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQG97sgWrvIZ9q8lmTwTy9Klk7rDWRqewNp0FlAqLPygVDtDIpBVWqnfjaXK-edx0Yh9upvdw9ymj9g0xltUBsIui2LtSQok6Fvih6KXtXW3YPbSOb_BlrIsrDphPSQBDOyl8aMeSdktm-xBaShKVIlBZ2QnPHrsAYr79VOkUS88sGgazkIeCkjgS2w34wqhml8C5JqMyzVk6UEu9yhM0loz1Qdr5eXcgvEy00w_Wkb9o=', start_index=21540)
Annotation(end_index=21554, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHl56jTNu_3iNUZnFI6dMKOFkarnCU_zBH__Oxx9YRrJ4yCZ1BCQSOyvcl51I8DuLqrQtYp9ClQ2ZbxQHTRWBrB0AhB1kdvqOFNs5SIZM3lCwVhsTLWLujf3CvA9ahR1r4hTlkfB07KG-VXa6o=', start_index=21540)

## Sources
