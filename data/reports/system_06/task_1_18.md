# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 3449a10a | **Time:** 280.29s | **Cost:** $0.03405
--------------------------------------------------------------------------------

# Can Distributed Architectures in Financial Risk Management Systems Truly Maintain a Dynamic Balance Between Monitoring Accuracy and Stability, or Does Event-Driven Processing Inherently Accelerate Cascading Failures?

## Abstract

The evolution of financial risk management systems has undergone a profound transformation with the widespread adoption of distributed architectures and event-driven processing paradigms. This research report examines the fundamental tension between monitoring accuracy and system stability within these modern architectural frameworks. Drawing upon contemporary research in distributed systems, machine learning integration, and financial technology implementation, this analysis investigates whether event-driven architectures can achieve a sustainable equilibrium between detection precision and operational resilience, or whether their inherent characteristics inevitably predispose systems to cascading failure propagation. The findings suggest that while event-driven architectures introduce novel failure modes, sophisticated design patterns—including circuit breakers, service meshes, and adaptive model orchestration—can effectively mitigate cascading risks while maintaining, and even enhancing, monitoring accuracy. The evidence indicates that the dichotomy between accuracy and stability is not inherent to event-driven processing but rather reflects the maturity of implementation strategies and the degree to which organizations embrace holistic resilience engineering principles.

## 1. Introduction

### 1.1 Background and Context

The contemporary landscape of financial risk management has been fundamentally reshaped by the transition from monolithic, batch-oriented processing systems to distributed, event-driven architectures. This architectural evolution has been driven by the imperative to process increasingly voluminous transaction streams in real-time while simultaneously meeting stringent regulatory requirements for accuracy, accountability, and auditability. The global payment landscape has undergone a remarkable transformation, with real-time payment systems such as Singapore's PayNow and FAST becoming the norm rather than the exception, thereby compressing the temporal window available for fraud detection and risk assessment from days or hours to mere milliseconds [1].

This acceleration of financial transactions has created unprecedented challenges for risk management systems. Traditional batch monitoring approaches, which analyze transactions retrospectively, have proven inadequate for detecting and preventing sophisticated fraud schemes that exploit the latency between transaction initiation and settlement. The proliferation of fintech applications, the expansion of cross-border remittance corridors, and the evolution of social engineering tactics have collectively created a threat environment that demands immediate, intelligent response capabilities [1]. Consequently, financial institutions have increasingly turned to distributed architectures capable of processing events in real-time, leveraging technologies such as Apache Kafka and Apache Flink to enable extraction, treatment, and joining of large heterogeneous streams of financial information [2].

### 1.2 Research Question and Scope

This report addresses a fundamental question that has significant implications for the design, implementation, and governance of financial risk management systems: Can distributed architectures truly maintain a dynamic balance between monitoring accuracy and system stability, or does event-driven processing inherently accelerate cascading failures? The question encompasses multiple dimensions of system behavior, including the accuracy-efficiency trade-offs inherent in distributed machine learning systems, the failure propagation characteristics of event-driven architectures, and the resilience patterns that can mitigate systemic risks.

The scope of this analysis extends beyond theoretical considerations to encompass practical implementation evidence from financial services organizations. By examining comparative assessments of real-time transaction monitoring architectures, studies of event-driven patterns in retail and financial contexts, and research into cascading failure mechanisms, this report synthesizes the current state of knowledge regarding the viability of distributed architectures for safety-critical financial applications.

## 2. Theoretical Framework: Accuracy-Efficiency Trade-offs in Distributed Systems

### 2.1 The Fundamental Tension

The relationship between accuracy and efficiency in distributed systems represents one of the most consequential design trade-offs facing architects of financial risk management systems. Research into distributed machine learning systems has established that accuracy-efficiency trade-offs constitute an appropriate abstraction for accounting for system behavior, particularly in contexts involving real-time, automated decision-making with significant potential consequences [3]. This framing is particularly relevant for financial risk management, where the stakes of incorrect decisions—whether false positives that inconvenience legitimate customers or false negatives that permit fraudulent transactions to proceed—can be substantial.

The theoretical foundation for understanding this tension rests on the recognition that computational resources are inherently finite, and that optimizing for one dimension of performance necessarily entails sacrifices in others. In the context of fraud detection, for example, more sophisticated machine learning models that achieve higher accuracy typically require greater computational resources and introduce additional latency into the decision pipeline. Conversely, systems optimized for minimal latency may sacrifice detection accuracy by employing simpler models or reduced feature sets. The challenge for distributed architectures is to navigate this trade-off space in a manner that achieves acceptable levels of both accuracy and efficiency while maintaining system stability under varying load conditions.

### 2.2 The Inversion Problem

A particularly significant insight from recent research concerns what has been termed the "inversion problem" in distributed ML system tuning [3]. This inversion refers to the mismatch between the ideal approach—which would involve formally evaluating the underlying accuracy-efficiency trade-off and using this information to directly tune system behavior—and the practical reality, in which tuning has generally been manually curated to particular problems or absent entirely. In practice, engineers are often forced to select from predefined settings that enforce high accuracy guarantees over efficiency, ignore accuracy guarantees altogether in favor of efficiency, or attempt some middle-ground compromise.

This inversion has profound implications for the stability of distributed financial risk management systems. When system behavior cannot be precisely tuned to balance accuracy and efficiency according to the specific requirements of the operational context, the resulting systems may exhibit unpredictable behavior under stress conditions. Current large-scale ML systems tend to opt for efficiency over accuracy, and it remains unclear whether these approaches will be safe for safety-critical financial applications [3]. The research community has identified this as an open research question deserving of continued attention, particularly as financial institutions deploy increasingly sophisticated real-time monitoring systems.

### 2.3 Distributed Computing Considerations

The distributed nature of modern financial risk management systems introduces additional complexity into the accuracy-efficiency trade-off landscape. Distributed computing introduces its own set of tensions, including the trade-offs between consistency and availability (as characterized by the CAP theorem), the challenges of maintaining state across geographically dispersed nodes, and the overhead associated with inter-node communication. When these distributed computing trade-offs are combined with the ML-specific trade-offs, the resulting system behavior can be especially challenging to predict and control [3].

The interaction between ML and distributed computing trade-offs presents especially challenging problems for real-time, high-impact systems. In financial risk management contexts, these systems must simultaneously achieve low latency (to prevent fraud before transactions complete), high accuracy (to minimize both fraud losses and customer friction), and high availability (to ensure continuous protection even during component failures). The architectural choices made to optimize for one of these objectives can have cascading effects on the others, creating a complex optimization landscape that defies simple resolution.

## 3. Event-Driven Architectures: Principles and Failure Modes

### 3.1 Event-Driven Processing Paradigms

Event-driven architectures represent a fundamental departure from traditional request-response processing models. In event-driven systems, components communicate through the production and consumption of events—discrete occurrences of significance within the system domain. This decoupling of producers and consumers enables asynchronous processing, load balancing, elasticity, and service recovery during outages [4]. In financial applications, event-driven patterns provide dependable order processing, payment streaming, and real-time fraud detection, all with replay capability and audit logs that support both operational troubleshooting and regulatory compliance.

The technical foundation of event-driven architectures typically relies on message streaming platforms such as Apache Kafka or Amazon Kinesis, which enable asynchronous processing by decoupling producers and consumers. These platforms provide durable event storage, partitioning for horizontal scalability, and consumer group semantics that enable parallel processing across multiple nodes. The event stream serves as an authoritative source of truth, with downstream consumers processing events at their own pace without creating backpressure on upstream producers [5].

### 3.2 Cascading Failure Mechanisms

Despite their advantages, event-driven architectures are not immune to failure modes, and their distributed nature can create conditions conducive to cascading failures. A cascading failure occurs when the failure of one component triggers the failure of dependent components, potentially propagating across system boundaries until a significant portion of the system becomes unavailable. Research has demonstrated that systems with high interconnectedness experience exponentially increasing fault rates, with a 15% higher likelihood of cascading failures compared to more loosely coupled architectures [5].

The mechanisms through which cascading failures propagate in event-driven systems are multifaceted. In traditional tightly integrated architectures, stock updates might trigger synchronous calls to multiple dependent systems, creating bottlenecks and potential failure points. This conventional approach requires the inventory service (or, by analogy, the risk assessment service) to maintain awareness of all downstream consumers and coordinate their responses, creating a single point of failure that can propagate issues across the system [5]. When one downstream service becomes slow or unavailable, the synchronous nature of the calls can cause resources to be exhausted as upstream services wait for responses, ultimately leading to system-wide degradation.

### 3.3 The Paradox of Resilience

A particularly counterintuitive finding from research into distributed system failures is that some customizations intended to reduce errors can actually increase the risk of total failures. For example, what appears to be intelligent load balancing can, under certain conditions, increase the likelihood of cascading failures by redistributing load to already stressed components, accelerating their failure and creating a feedback loop that overwhelms the system [6]. Similarly, sophisticated retry logic, while intended to improve reliability, can inadvertently create DDoS-like conditions against a system's own components when those components are already experiencing difficulties.

This "paradox of resilience" highlights the importance of careful design in event-driven systems. The very features that make event-driven architectures attractive—their decoupling, their elasticity, their ability to handle variable loads—can also create conditions for failure propagation if not properly bounded. Financial institutions implementing these architectures must therefore be acutely aware of the failure modes they are introducing alongside the failure modes they are mitigating.

## 4. Evidence for Dynamic Balance: Accuracy and Stability in Concert

### 4.1 Empirical Performance Evidence

Recent research has provided compelling empirical evidence that event-driven architectures can achieve favorable outcomes on both accuracy and stability dimensions. A comparative assessment of Kafka-Flink pipelines combined with Temporal Risk Graphs (TRGs), Adaptive Model Orchestration (AMO), and Privacy-Preserving Stream Processing (P2SP) demonstrated that these integrated architectures can reduce detection latency by 85-90% compared to batch processing while simultaneously enhancing fraud detection accuracy and recall to 0.91 and 0.87, respectively [2]. These results were achieved while maintaining a throughput of 100,000 events per second with under 200ms p99 latency and 99.95% SLA adherence.

The significance of these findings lies in their demonstration that the traditionally assumed trade-off between speed and accuracy need not be absolute. By leveraging sophisticated architectural patterns that enable parallel processing, intelligent event routing, and adaptive model selection, the system was able to achieve both rapid detection and high accuracy simultaneously. Furthermore, the system achieved a 40% reduction in false positives, indicating that the framework is capable of balancing customer experience with operational reliability [2]. This balance is crucial for financial institutions, where excessive false positives can create customer friction and operational burden, while false negatives result in financial losses and regulatory scrutiny.

### 4.2 Stability Improvements Through Event-Driven Patterns

Research into event-driven patterns in retail contexts has demonstrated significant stability improvements that extend to financial applications. Studies comparing traditional versus event-driven inventory architectures found that retailers implementing event-driven patterns reported a 37% reduction in inventory-related system outages and a 45% improvement in update processing throughput during peak periods [5]. The event-driven pattern offers particular advantages for scenarios where state must remain consistent across multiple integrated systems, which is directly applicable to financial risk management where transaction risk assessments must be consistent across channels and systems.

The stability improvements stem from several architectural factors inherent to well-designed event-driven systems. First, the isolation of failures prevents cascading impacts across system boundaries—when one component fails, its failure is contained rather than propagating to dependent components. Second, independent deployability enables updates without requiring system-wide maintenance windows, reducing the cumulative downtime associated with software evolution. Third, improved resilience through retry mechanisms and buffering capabilities inherent in event-driven designs allows systems to gracefully handle temporary unavailability of downstream services [5]. Research has documented that retailers implementing loose coupling through event-driven patterns typically reduce system downtime by 40-60% compared to tightly integrated architectures.

### 4.3 Hybrid Approaches and Layered Architectures

The most compelling evidence for the possibility of dynamic balance comes from research into hybrid and layered architectural approaches. Comparative analyses of real-time transaction monitoring architectures have revealed that no single technique or technology can solve all the problems encountered by modern financial institutions [7]. Instead, the evidence suggests that weaving together multiple approaches—combining the best predictive intelligence with appropriate governance mechanisms—may represent the optimal path forward.

One particularly promising hybrid approach combines a fast machine learning layer that screens transactions in real-time with a blockchain layer that archives decisions and provides immutable audit trails [7]. This architecture leverages the speed and accuracy of ML-based fraud detection while providing the tamper-resistance and regulatory compliance benefits of distributed ledger technology. The latency introduced by cryptographic operations is a tolerable trade-off, particularly when working with AI models that perform pre-processing and filtering of transactions. These composite monitoring architectures enable financial institutions to find a compromise between performance and regulatory robustness that neither approach could achieve alone.

## 5. Mitigation Strategies: Preventing Cascading Failures in Event-Driven Systems

### 5.1 Circuit Breakers and Service Meshes

The technical ecosystem for event-driven architectures has developed sophisticated tools for preventing cascading failures. Service meshes such as Istio and Linkerd offer robustness at the communication layer through the use of circuit breakers, traffic splitting, retries, and rate limitation [4]. Circuit breakers are particularly valuable for preventing cascading failures across interconnected services; they monitor service health and automatically cut off requests to failing services, acting as a safeguard against system-wide degradation.

The circuit breaker pattern operates by monitoring requests between services and tracking failure rates. When failures exceed a threshold, the circuit breaker "trips" and immediately fails all requests rather than allowing them to queue up and consume resources. After a cooldown period, the circuit breaker allows a limited number of requests to pass through to test whether the downstream service has recovered. If the service is still unhealthy, the circuit breaker remains open; if it has recovered, the circuit breaker closes and normal operation resumes. This pattern prevents the resource exhaustion that typically precedes cascading failures while enabling automatic recovery when conditions improve.

### 5.2 Asynchronous Communication and Loose Coupling

The fundamental architectural principle underlying resilient event-driven systems is loose coupling through asynchronous communication. By decoupling producers and consumers through message queues or event streams, systems can absorb temporary unavailability without propagating failures upstream. Components operate independently, minimizing the impact of failures and making the system easier to maintain and scale [6]. This independence is crucial for preventing cascading failures, as it ensures that the failure of one component does not directly cause the failure of its dependencies.

Effective loose coupling requires careful attention to interface design and message semantics. Well-defined interfaces enable components to evolve independently, while appropriate message schemas ensure that changes to producing components do not break consuming components. The event taxonomy, granularity, and schema design must be carefully considered to enable future evolution while maintaining current functionality [8]. Financial institutions implementing event-driven architectures must invest in governance processes that ensure consistency in these design decisions across the organization.

### 5.3 Resilience Engineering Principles

Beyond specific technical patterns, the prevention of cascading failures in distributed financial systems requires an organizational commitment to resilience engineering—a proactive, design-focused approach to ensuring operational continuity [4]. Resilience engineering recognizes that failures are inevitable in complex systems and focuses on building the capacity to withstand, recover from, and adapt to adverse conditions. This represents a shift from traditional reliability engineering, which focuses on preventing failures, to an approach that accepts failures as inevitable and builds systems that can handle them gracefully.

The integration of resilience engineering principles with Site Reliability Engineering (SRE) methodologies has been shown to enhance the capacity of financial systems to withstand, recover from, and adjust to unfavorable conditions [4]. Key practices include chaos engineering—deliberately introducing failures into production systems to verify resilience—and blameless post-mortems that focus on systemic improvements rather than individual accountability. These practices help organizations identify and address weaknesses in their systems before they result in cascading failures under production conditions.

## 6. Implementation Considerations for Financial Institutions

### 6.1 Architectural Evolution and Organizational Readiness

The transition to event-driven microservices architecture represents not merely a technical transformation but a fundamental change in how financial systems are designed, deployed, and operated [8]. Financial institutions considering this architectural transformation must carefully evaluate their organizational readiness, technical capabilities, and risk tolerance. The operational complexity introduced by distributed event-driven systems necessitates sophisticated monitoring and observability solutions, comprehensive logging mechanisms, and systematic processes for optimization and risk management.

The architectural evolution from monolithic to microservices combined with event-driven design patterns addresses the scalability, reliability, and agility requirements of modern high-volume financial transaction processing while providing the flexibility necessary for rapid business evolution [8]. However, this evolution requires investment in skills development, process redesign, and cultural change alongside technical implementation. Organizations that attempt to implement event-driven architectures without addressing these organizational factors are likely to experience operational difficulties that undermine the potential benefits.

### 6.2 Integration with Legacy Systems

One of the most significant practical challenges facing financial institutions is the integration of modern event-driven monitoring systems with legacy infrastructure. Older financial systems might not be immediately compatible with modern real-time monitoring tools, leading to integration issues that can undermine both accuracy and stability [9]. Adopting middleware solutions or API integrations can bridge the gap between legacy systems and new monitoring platforms, ensuring smooth data flow and operations.

The integration challenge is not merely technical but also strategic. Legacy systems often encode institutional knowledge and business rules that are difficult to replicate in modern architectures. A phased approach that gradually migrates functionality from legacy systems to event-driven components, while maintaining appropriate fallback capabilities, can reduce risk during the transition period. This approach allows organizations to realize the benefits of event-driven processing incrementally while managing the inherent risks of large-scale system transformation.

### 6.3 Regulatory Compliance and Governance

Financial institutions operate under stringent regulatory requirements that impose specific constraints on system design and operation. Data residency requirements present particularly complex challenges for distributed event streams, as financial institutions operating in multiple jurisdictions must carefully manage the flow and storage of events containing regulated data [8]. Organizations operating in regions with strong data sovereignty laws face significant compliance challenges when implementing distributed event architectures, emphasizing the importance of implementing mechanisms to enforce data residency requirements through policy-based routing and storage.

Comprehensive audit logging provides both a security control and a compliance mechanism for financial event streams. Effective audit logging for financial event streams should capture detailed information about subscription and consumption patterns, with mechanisms consistently applied across all event access channels [8]. This logging supports both regulatory compliance and security monitoring, enabling organizations to detect and investigate anomalous behavior while demonstrating compliance to regulators.

## 7. Discussion: Resolving the Dichotomy

### 7.1 Beyond the False Dichotomy

The evidence synthesized in this report suggests that the framing of the research question as a dichotomy—asking whether distributed architectures can balance accuracy and stability or whether event-driven processing inherently accelerates failures—may itself be misleading. The empirical evidence indicates that the relationship between event-driven processing and cascading failures is not deterministic but rather contingent on the specific architectural patterns, implementation quality, and operational practices employed by organizations.

Event-driven architectures are neither inherently prone to cascading failures nor automatically resilient to them. Rather, the resilience characteristics of these systems depend on the degree to which organizations implement appropriate patterns such as circuit breakers, the quality of their monitoring and observability infrastructure, and their commitment to resilience engineering principles. Similarly, the accuracy of monitoring systems depends not on whether they employ event-driven processing but on the sophistication of their machine learning models, the quality of their data pipelines, and the effectiveness of their feedback mechanisms for continuous improvement.

### 7.2 The Path Forward

The research suggests several principles for financial institutions seeking to implement distributed architectures that achieve both high accuracy and high stability. First, hybrid approaches that combine multiple technologies and techniques are likely to outperform single-technology solutions. The integration of Temporal Risk Graphs, Adaptive Model Orchestration, and Privacy-Preserving Stream Processing into unified architectures has demonstrated the ability to achieve both speed and accuracy simultaneously [2]. Second, investment in resilience engineering and SRE practices is essential for maintaining stability as systems become more distributed and complex. Third, organizations must address the organizational and cultural dimensions of this transformation, not merely the technical dimensions.

The accuracy-efficiency trade-off, while real, need not be a zero-sum game. By leveraging the parallelism and elasticity of distributed architectures, organizations can achieve levels of both accuracy and efficiency that would be impossible in monolithic systems. The key is to approach the design and implementation of these systems with a holistic perspective that considers the interdependencies between architectural choices, operational practices, and business requirements.

## 8. Conclusion

This research report has examined the fundamental question of whether distributed architectures in financial risk management systems can maintain a dynamic balance between monitoring accuracy and stability, or whether event-driven processing inherently accelerates cascading failures. The evidence indicates that the dichotomy implied by this question is largely a false one. Event-driven architectures, when properly designed and implemented, can achieve favorable outcomes on both dimensions simultaneously.

The empirical research demonstrates that modern event-driven architectures can reduce detection latency by 85-90% while simultaneously enhancing fraud detection accuracy and recall to levels exceeding 0.90 [2]. These systems can maintain throughput of 100,000 events per second with under 200ms p99 latency and 99.95% SLA adherence, while also reducing false positives by 40% [2]. The stability benefits are equally significant, with event-driven patterns reducing system downtime by 40-60% compared to tightly integrated architectures [5].

However, these benefits are not automatic. They require deliberate investment in resilience patterns including circuit breakers, service meshes, and asynchronous communication. They require organizational commitment to resilience engineering principles and SRE practices. They require careful attention to integration with legacy systems and compliance with regulatory requirements. And they require recognition that no single technique or technology can solve all problems—hybrid approaches that combine multiple complementary technologies are likely to outperform single-technology solutions [7].

The research community has identified the accurate characterization of accuracy-efficiency trade-offs as an ongoing challenge, particularly for safety-critical real-time systems [3]. As financial institutions continue to evolve their risk management capabilities, continued research into these trade-offs and the development of tools to reason about them will be essential. The goal should be to develop frameworks that enable organizations to explicitly evaluate and tune the balance between accuracy and efficiency according to their specific risk tolerances and business requirements, rather than accepting default configurations that may not be appropriate for their contexts.

In conclusion, distributed architectures in financial risk management systems can indeed maintain a dynamic balance between monitoring accuracy and stability—but only when organizations approach their design and implementation with the sophistication, rigor, and commitment to resilience that modern financial systems demand. Event-driven processing does not inherently accelerate cascading failures; rather, the risk of cascading failures depends on the architectural patterns, implementation quality, and operational practices employed. By embracing hybrid approaches, investing in resilience engineering, and addressing both technical and organizational dimensions of this transformation, financial institutions can realize the full potential of distributed architectures for protecting against financial crime while maintaining the stability and reliability that their operations and customers require.

## References

[1] Tookitaki. "Real-Time Transaction Monitoring." Tookitaki Compliance Hub. https://www.tookitaki.com/compliance-hub/real-time-transaction-monitoring

[2] EU Open Science. "Event-Driven Architectures in Financial Risk Analytics." European Journal of Engineering and Computer Science, 2025. https://eu-opensci.org/index.php/ejece/article/view/19761

[3] Cooper, A. "Reasoning About Accuracy-Efficiency Trade-offs in Distributed ML Systems." EAAMO 2021. https://afedercooper.info/paper/cooper2021eaamo.pdf

[4] American Journal of Engineering and Technology. "Resilience Engineering in Financial Systems." 2025. http://emergingsociety.org/index.php/efltajet/article/download/248/247

[5] IJSAT. "Event-Driven Systems in Retail and Financial Contexts." International Journal of Scientific and Technology Research, 2025. https://www.ijsat.org/papers/2025/1/2921.pdf

[6] Statsig. "Handling Failures in Distributed Systems: Patterns and Anti-Patterns." https://www.statsig.com/perspectives/handling-failures-in-distributed-systems-patterns-and-anti-patterns

[7] All Multidisciplinary Journal. "Comparative Assessment of Real-Time Transaction Monitoring Architectures." 2025. https://www.allmultidisciplinaryjournal.com/uploads/archives/20250621125159_MGE-2025-3-305.1.pdf

[8] IJSAT. "Event-Driven Architecture in Financial Services." International Journal of Scientific and Technology Research, 2025. https://www.ijsat.org/papers/2025/1/2793.pdf

[9] Flagright. "How Real-Time Monitoring Changes the Game for Transaction Security." https://www.flagright.com/post/how-real-time-monitoring-changes-the-game-for-transaction-security

## Annotations


## Sources
[1] http://emergingsociety.org/index.php/efltajet/article/download/248/247
[2] https://afedercooper.info/paper/cooper2021eaamo.pdf
[3] https://eu-opensci.org/index.php/ejece/article/view/19761
[4] https://journalwjaets.com/sites/default/files/fulltext_pdf/WJAETS-2025-0402.pdf
[5] https://medium.com/@harrifassbender/service-resilience-strategies-to-prevent-cascading-failures-in-large-scale-distributed-systems-5a3a9ded4a1f
[6] https://sarcouncil.com/download-article/SJECS-237-2025-851-860.pdf
[7] https://www.allmultidisciplinaryjournal.com/uploads/archives/20250621125159_MGE-2025-3-305.1.pdf
[8] https://www.eu-opensci.org/index.php/ejece/article/view/19761
[9] https://www.flagright.com/post/how-real-time-monitoring-changes-the-game-for-transaction-security
[10] https://www.ijsat.org/papers/2025/1/2793.pdf
[11] https://www.ijsat.org/papers/2025/1/2921.pdf
[12] https://www.mdpi.com/2079-8954/12/10/416
[13] https://www.sciencedirect.com/science/article/pii/S2666449625000684
[14] https://www.statsig.com/perspectives/handling-failures-in-distributed-systems-patterns-and-anti-patterns
[15] https://www.tookitaki.com/compliance-hub/real-time-transaction-monitoring