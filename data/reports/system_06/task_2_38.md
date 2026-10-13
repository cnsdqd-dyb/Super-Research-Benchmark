# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** ebe4a668 | **Time:** 124.42s | **Cost:** $0.03409
--------------------------------------------------------------------------------

# Does the Multi-Agent Coordination Algorithm in Financial Decision Support Offer an Optimal Compromise Between Accuracy and Resource Use, or Does Bayesian Reasoning Lead to Unavoidable Complexity Explosions?

## Abstract

This research report examines the fundamental tension between accuracy and computational resource consumption in multi-agent coordination algorithms for financial decision support systems. Through analysis of recent advances in multi-agent architectures, reinforcement learning approaches, and Bayesian reasoning frameworks, we investigate whether these systems can achieve optimal balance or whether inherent complexity constraints create unavoidable scalability limitations. The evidence suggests that while multi-agent systems demonstrate remarkable performance improvements—evidenced by systems like QuantAgents achieving annualized returns of 58.68% with Sharpe ratios of 3.11%—they simultaneously face significant challenges including state and action space explosions, efficiency degradation during scaling, and coordination overhead that can negate the benefits of distributed processing. We conclude that the compromise between accuracy and resource use is not universally optimal but rather problem-dependent, with heuristic approaches, structured architectures, and hybrid human-AI integration offering viable pathways to manage complexity while maintaining decision quality.

## 1. Introduction

Financial decision support systems have undergone substantial transformation in recent years, evolving from single-agent predictive models to sophisticated multi-agent architectures that mirror the collaborative nature of human financial teams. This evolution reflects the growing recognition that complex financial tasks—from portfolio optimization to risk assessment and trading strategy execution—benefit from multiple specialized perspectives working in coordination rather than relying on monolithic models.

The fundamental question driving this research concerns the theoretical and practical limits of such systems: can multi-agent coordination algorithms achieve an optimal balance between decision accuracy and computational resource consumption, or do Bayesian reasoning and probabilistic inference methods inevitably lead to complexity explosions that render large-scale deployment impractical? This question carries profound implications for the future of financial AI, as institutions increasingly rely on automated systems for high-stakes decisions involving significant capital.

The context for this analysis spans multiple dimensions of multi-agent system design, including distributed computing principles, reinforcement learning algorithms, resource allocation optimization techniques, and coordination mechanisms. The multi-agent paradigm draws inspiration from distributed computing, where multiple interconnected components collaborate to perform tasks that would exceed the capabilities of individual units [1]. In financial applications, this translates to systems where specialized agents—each optimized for specific analytical functions—coordinate to process multi-modal market information, assess risk profiles, and execute trading decisions with varying degrees of autonomy.

This report synthesizes evidence from recent academic literature, industry implementations, and theoretical frameworks to provide a comprehensive assessment of the accuracy-resource tradeoff landscape in financial multi-agent systems. We examine the sources of computational complexity, the mechanisms through which complexity explosions manifest, and the strategies researchers and practitioners have developed to mitigate these effects while preserving decision quality.

## 2. Theoretical Foundations of Multi-Agent Reasoning Capacity

### 2.1 Defining Reasoning Capacity in Distributed Financial Systems

The concept of reasoning capacity serves as a crucial framework for understanding the capabilities and limitations of multi-agent financial systems. While computational complexity measures the resources required to solve problems, reasoning capacity encompasses the broader and more holistic concept of a system's overall ability to perform a range of reasoning tasks [1]. This distinction is particularly relevant in financial contexts, where systems must handle diverse analytical challenges ranging from numerical assessment to qualitative interpretation of market sentiment.

Reasoning capacity in multi-agent systems can be decomposed across various components of the architecture, facilitating more controllable debugging and optimization processes. Following the distributed computing paradigm, where multiple interconnected computers collaborate to perform complex tasks, financial multi-agent systems benefit from similar architectural principles [1]. The decomposition of reasoning capacity across system components enables specialized optimization of each agent's capabilities while maintaining coordination mechanisms that preserve the benefits of collaborative processing.

The practical implications of this decomposition are substantial. In a financial decision support context, different agents may specialize in distinct analytical functions: some agents focus on processing numerical market data, others interpret textual news and sentiment, while additional agents handle risk assessment and portfolio optimization. This specialization allows each agent to develop optimized reasoning capacity for its specific domain while the overall system leverages the collective intelligence of the collaborative network.

### 2.2 Computational Complexity and Reasoning Tradeoffs

The relationship between reasoning capacity and computational complexity represents a fundamental tension in multi-agent system design. Computational complexity, as formally defined in theoretical computer science, assesses the resources—time and space—required to execute algorithms as input sizes grow. In multi-agent financial systems, this complexity manifests in multiple dimensions: the computational burden of individual agent processing, the communication overhead of inter-agent coordination, and the combinatorial explosion that arises from agent interactions.

Resource Allocation Optimization (RAO) exemplifies this tradeoff challenge. RAO is a significant area of research across many fields, focusing on the challenge of distributing resources among agents or tasks to improve system efficiency, productivity, or fairness [2]. The structured distribution of finite resources among tasks or activities to meet defined objectives—efficiency, cost minimization, or return maximization—requires identification of available resources, assessment of task demands, and allocation decisions that align with system goals, often under constraints such as time, budget, or capacity limitations.

Heuristic algorithms provide a flexible alternative for RAO by focusing on finding acceptable, near-optimal solutions within reasonable time frames. These methods are particularly useful for complex, large-scale, or time-sensitive scenarios where exact solutions are impractical [2]. While heuristics do not guarantee optimal solutions, they offer practical tradeoffs between accuracy and computational efficiency, making them suitable for real-time financial applications where decisions must be made rapidly despite incomplete information.

### 2.3 Bayesian Reasoning and Probability in Financial Multi-Agent Systems

Bayesian reasoning provides a principled framework for updating beliefs and making decisions under uncertainty, making it naturally applicable to financial domains characterized by noisy data, incomplete information, and inherent market volatility. However, the application of Bayesian methods in multi-agent settings introduces significant computational challenges that can lead to complexity explosions.

In constrained planning problems for multi-agent systems under uncertainty, unique solutions are required to handle the state space explosion that arises from Multi-Agent Markov Decision Processes (MMDPs) [4]. The Risk-Constrained MMDP problem—optimizing for expected reward while constraining the joint Conditional Value at Risk (CVaR) of shared resources—exemplifies these challenges. The constraint can be interpreted as limiting the expected value of shared resources in worst-case scenarios, requiring sophisticated probabilistic reasoning that scales poorly with agent count and system complexity.

Risk contributions, a measure introduced in finance research, quantify how much individual agents affect joint risk [4]. By identifying agents who contribute proportionally more risk to reward, systems can iteratively update policies to lower risk contributions and reduce joint CVaR. However, the computational burden of calculating and optimizing these risk contributions increases substantially as more agents participate in the system, creating practical limits on scalability.

## 3. Architecture and Coordination Mechanisms

### 3.1 Multi-Agent Architectures in Financial Applications

Financial multi-agent systems employ various architectural patterns, each with distinct implications for the accuracy-resource tradeoff. The primary architectures include network structures where agents communicate freely and decide independently whom to contact next, supervisor architectures where a central coordinator makes all routing decisions, and tool-calling supervisor architectures where the supervisor uses an LLM to invoke agents as explicit tools with arguments [5].

In cooperative settings, agents work toward shared or complementary goals, prioritizing collective outcomes over individual gain. In competitive settings, agents pursue their own objectives, often in opposition to others, requiring negotiation mechanisms to reach mutually beneficial agreements [9]. Many real-world financial systems combine both cooperation and competition to streamline task execution and increase performance efficiency.

The strategic framework for multi-agent AI systems mirrors best-performing finance teams—with specialized roles collaborating toward shared objectives [10]. Each component focuses on what it does best while maintaining communication to accelerate decision-making and improve outcome quality. This specialization enables optimization of individual agent performance while coordination mechanisms preserve the benefits of collaborative analysis.

### 3.2 Coordination Evaluation and System Performance

Evaluating multi-agent systems introduces unique challenges compared to single-agent systems. Core evaluation strategies encompass agent handoff evaluation, which assesses timing appropriateness, information transfer effectiveness, and optimal handoff moments when tasks transfer between agents [5]. System-level evaluation measures holistic performance through end-to-end task completion, efficiency metrics including interaction count and processing speed, and user experience assessments.

Coordination evaluation specifically addresses cooperative effectiveness through assessment of communication quality, conflict resolution capabilities, and resource management efficiency [5]. These evaluation dimensions reveal the multifaceted nature of performance in multi-agent financial systems—success requires not only accurate individual agent decisions but effective coordination that leverages the complementary strengths of specialized components.

### 3.3 Hierarchical and Modular Architectures

Hierarchical architectures have emerged as effective patterns for managing the complexity of financial multi-agent systems. The investment portfolio decision support system architecture uses a manager agent coordinating specialized worker agents, integrating market analysis, risk assessment, and investment recommendations through layered decision-making processes [11].

Modular, rule-enhanced multi-agent architectures enable robust, interpretable financial operations. By decomposing pipelines into extraction, validation, and generation components, systems gain control over accuracy, explainability, and efficiency [7]. These improvements are particularly valuable for real-world financial workflows, where numeric precision and auditability are paramount concerns for regulatory compliance and risk management.

The two-step multi-agent architecture separating extraction and querying components into specialized agents optimizes for financial accuracy, controllability, and interpretability [7]. Document processing flows through stages of saving, layout parsing, preprocessing, and analysis, with each stage handled by agents optimized for specific functions. This decomposition enables focused optimization while maintaining the benefits of collaborative processing.

## 4. Complexity Explosions: Sources and Manifestations

### 4.1 Efficiency Explosions in Multi-Agent Generative Systems

Multi-agent generative AI systems face distinctive efficiency challenges arising from their autoregressive architecture and the need for repeated model queries. Due to their autoregressive architecture, LLMs typically have slow inference speeds [3]. However, generative agents need to query LLMs for each action multiple times—extracting information from memory, making plans before taking actions, and similar operations—when the multi-agent system scales up, this problem becomes significantly magnified, especially for generative agents with large action spaces.

This efficiency explosion represents a fundamental scalability constraint. As additional agents are added to the system to improve analytical coverage or decision quality, the computational burden increases not linearly but superlinearly, due to the multiplicative effects of inter-agent communication, coordination overhead, and the compounded inference requirements of multiple generative agents operating simultaneously.

### 4.2 State and Action Space Explosions

The addition of multiple agents to financial decision problems introduces combinatorial complexity in state and action spaces. Planning under uncertainty requires complex reasoning about future events, and this complexity increases with the addition of multiple agents [4]. The state space explosion in MMDPs arises from the need to consider joint states where all agents' positions, holdings, and market conditions must be represented simultaneously.

Action space explosions similarly complicate multi-agent financial systems. When each agent can take multiple actions—buy, sell, hold for different securities, adjust position sizes, apply risk management procedures—the number of possible joint action combinations grows exponentially with agent count. This combinatorial explosion makes exhaustive evaluation of all possible action combinations infeasible for all but the smallest systems.

Distributed Constraint Optimization Problems (DCOPs) provide a framework for modeling multi-agent coordination challenges [12]. In DCOPs, agents represented as variables are assigned tasks, with domains representing possible agent-task assignments. The utility of assigning tasks to agents can be modeled as a function based on agent status and constraint sets, but evaluating these utilities across all possible assignments becomes computationally intractable for large agent populations.

### 4.3 Coordination Overhead and Communication Bottlenecks

The benefits of multi-agent processing can be substantially offset by coordination overhead—the computational and temporal costs of maintaining communication, synchronizing agent actions, and resolving conflicts. Context management and parallel computation represent the two main motivations for multi-agent systems, but the coordination costs can negate these benefits if not carefully managed [13].

Consider a scenario where a complex financial task requires 10^6 total steps to solve with a single agent, requiring quadratic operations of 10^12. If instead the task is split into 10^4 parts each requiring 10^2 steps, where c represents coordination overhead, the operations reduce to 10^8 c^2 [13]. If coordination overhead is small, this represents substantial reduction in computational requirements. However, as c increases—representing more complex coordination needs—the benefits diminish rapidly.

In practice, multi-agent systems for deep research tasks requiring browsing hundreds of websites to answer complex queries demonstrate the potential of distributed processing, but also highlight the coordination challenges that emerge when systems scale [13]. The key research question concerns how to scale up the number of instances and types of complex tasks where multi-agent systems are truly needed.

## 5. Strategies for Balancing Accuracy and Resource Efficiency

### 5.1 Heuristic Optimization and Approximate Methods

Given the computational intractability of exact solutions for many multi-agent financial problems, heuristic optimization provides practical alternatives. Heuristic algorithms focus on finding acceptable, near-optimal solutions within reasonable time frames, offering practical tradeoffs between accuracy and computational efficiency [2]. These methods are particularly useful for complex, large-scale, or time-sensitive scenarios where exact solutions are impractical.

Rule-based validation and structured prompting significantly improve both extraction and query accuracy while reducing error rates and increasing throughput in multi-agent financial systems [7]. Domain-specific prompt tuning improves extraction metrics while reducing unit error rates, demonstrating the value of schema-aware approaches. Adding validation and heuristics reduces semantic and numeric misalignment, especially for complex financial interpretations.

### 5.2 Reinforcement Learning Approaches

PPO-based algorithms, including MAPPO, HATRPO, and HAPPO, have revolutionized multi-agent reinforcement learning by combining the stability of PPO with coordination benefits of centralized critics [8]. These algorithms have proven effective across wide arrays of cooperative and competitive multi-agent tasks, offering strong performance and scalability.

Both HATRPO and HAPPO utilize sequential update processes where one agent updates its policy while others remain fixed, preventing conflicts during policy optimization and ensuring theoretical convergence to stable joint policies [8]. By removing parameter-sharing constraints, these algorithms enable agents to learn tailored policies accounting for their unique roles and capabilities, performing competitively in benchmark tasks while scaling to high-dimensional state-action spaces.

### 5.3 Risk-Constrained Optimization Techniques

In financial contexts where risk management is paramount, risk-constrained optimization techniques offer mechanisms for managing complexity while maintaining decision quality. The concept of risk contribution allows identification of agents who contribute proportionally more risk to reward [4]. Systems then update worse-performing agents' policies to iteratively lower their risk contribution and reduce joint CVaR.

This approach represents a pragmatic compromise: rather than attempting full probabilistic reasoning over all possible future states, the system focuses computational resources on managing tail risk through constraint satisfaction. By limiting expected value of shared resources in worst cases, the system maintains acceptable risk profiles without exhaustive enumeration of all possible scenarios.

### 5.4 Human-AI Integration

Integrating human reasoning into various aspects of multi-agent systems can alleviate bottlenecks in systems' reasoning mechanisms [1]. This hybrid approach leverages the complementary strengths of human judgment—contextual understanding, ethical reasoning, and adaptive learning—and computational processing—speed, consistency, and ability to handle large data volumes.

Multi-agent systems should augment rather than replace financial judgment, supporting financial professionals through transparent reasoning and appropriate human oversight [11]. This perspective suggests that optimal system design may not require fully autonomous operation but rather collaborative frameworks where AI systems enhance human decision-making capabilities while maintaining human oversight for critical judgments.

## 6. Empirical Evidence: Performance and Tradeoffs

### 6.1 Quantitative Performance Metrics

Empirical evidence from deployed multi-agent financial systems provides insight into achievable performance levels and associated resource requirements. QuantAgents, a sophisticated multi-agent financial system incorporating simulated trading configured similarly to human quant traders, demonstrates superior performance across evaluation metrics [8]. The system achieves annualized returns (ARR) of 58.68% with Sharpe ratio (SR) of 3.11%, outperforming the best baseline (HedgeAgents) by 19.15% and 30.02% respectively.

FinAgent achieves impressive ARR of 45.31% and SR of 2.25, significantly outperforming the top RL-based model AlphaMix+ (ARR: 32.51%, SR: 1.49) [8]. The cumulative returns trajectory illustrates superior performance of LLM-based methods, particularly from mid-2022 onwards, suggesting continued improvement as these approaches mature.

Live trading performance evaluations from Q3 2024 to Q1 2025 demonstrate real-world applicability. QuantAgents delivered returns of 111.87% (Sharpe Ratio: 2.02, Win Rate: 61.23%) in A-stocks and 97.69% (Sharpe Ratio: 1.76, Win Rate: 59.71%) in HK-stocks, highlighting exceptional profitability and risk management across diverse market conditions [8].

### 6.2 Resource Efficiency Considerations

While performance metrics demonstrate the accuracy benefits of multi-agent approaches, resource efficiency considerations reveal the computational costs. The efficiency explosion problem—slow inference speeds compounded by repeated model queries—represents a fundamental constraint that must be managed through architectural choices and optimization strategies.

Rule-based agents can partially alleviate efficiency problems by replacing computationally intensive generative agents for certain functions [3]. SoMoSiMu-Bench replaces edge generative agents with rule-based agents, reducing computational requirements while maintaining system functionality. However, for multi-agent systems with complex action spaces, this problem remains unsolved, limiting scalability.

The practical deployment of multi-agent LLM systems, particularly in industrial settings, demands emphasis on reliability alongside performance metrics [6]. High-stakes applications like supply chain optimization and resource allocation require systems that not only achieve high accuracy but do so consistently and predictably, with resource consumption that remains manageable as system complexity increases.

### 6.3 Architecture-Specific Tradeoffs

Different architectural patterns exhibit distinct tradeoff characteristics. Network architectures, where agents communicate freely and decide independently, offer maximum flexibility but face challenges in communication efficiency, decision quality assessment, and coordination complexity evaluation [5]. Supervisor architectures, where agents communicate exclusively with a single coordinator, provide more controlled routing and task management but create potential bottlenecks at the supervisor level.

Tool-calling supervisor architectures, where the supervisor uses an LLM to invoke agents as explicit tools, offer explicit tool-calling accuracy and argument appropriateness evaluation but require sophisticated supervisor decision quality [5]. The choice among these architectures involves fundamental tradeoff decisions between flexibility, coordination overhead, and system reliability.

## 7. The Accuracy-Resource Compromise: A Synthesis

### 7.1 Conditions for Optimal Balance

The evidence suggests that multi-agent coordination algorithms can achieve favorable compromises between accuracy and resource use under specific conditions. When task decomposition is clean—where distinct subtasks can be assigned to specialized agents with minimal interaction requirements—multi-agent architectures offer substantial accuracy improvements without proportional resource increases. The HR company example, where multi-agent systems bridge cloud applications and infrastructure by facilitating career guidance, candidate matching, and resume writing assistance, illustrates this principle [1].

Similarly, when inter-agent communication patterns are predictable and can be optimized through architectural design, the efficiency gains from parallel processing outweigh coordination overhead. Hierarchical architectures with clear supervisory relationships enable focused resource allocation, directing computational resources toward high-priority decisions while maintaining acceptable performance on routine tasks.

### 7.2 Conditions Leading to Complexity Explosions

Complexity explosions become unavoidable when several conditions coincide. First, when agent interactions are dense and unpredictable—each agent's optimal action depends on many other agents' states and intentions—the combinatorial explosion in joint state-action spaces makes exhaustive reasoning infeasible. Second, when real-time constraints require rapid decision-making, the time available for inter-agent communication and coordination becomes severely limited. Third, when the action space for each agent is large and continuous rather than discrete and bounded, approximation errors accumulate across the system.

In these conditions, Bayesian reasoning approaches that would theoretically provide optimal decisions become computationally intractable. The theoretical elegance of full probabilistic inference over joint distributions gives way to practical necessity for approximation, heuristics, and pragmatic shortcuts.

### 7.3 The Problem-Dependent Nature of Optimality

The fundamental finding of this analysis is that the optimal balance between accuracy and resource consumption is not universal but rather problem-dependent. Problems with clear structure, decomposable objectives, and limited agent interactions favor multi-agent approaches that can achieve both high accuracy and reasonable resource consumption. Problems characterized by tight coupling, emergent behaviors, and real-time requirements may not admit any efficient multi-agent solution, regardless of architectural sophistication.

Resource allocation in multi-agent systems—where agents allocate limited resources to satisfy demands across multiple regions based on given constraints—illustrates this problem-dependence [6]. When total demand equals total resources, optimal allocation simply requires distributing resources exactly to meet each region's demands. When demands and supplies are mismatched, or when multiple resource types with complex interdependencies must be allocated, the problem becomes substantially more challenging.

## 8. Future Research Directions

### 8.1 Scalability Through Architectural Innovation

Future research should focus on developing architectural innovations that improve scalability while maintaining decision quality. Asymmetric DCOPs, multi-objective optimization, and quantified constraints represent theoretical frameworks that may yield practical scalability improvements [12]. Probabilistic and stochastic DCOPs offer mechanisms for handling non-deterministic environments characteristic of financial markets.

Dynamic DCOPs that change over time due to dynamic events may prove particularly valuable for financial applications where market conditions evolve continuously [12]. Adaptive coordination mechanisms that adjust communication patterns based on current conditions could help manage the tradeoff between accuracy and resource consumption dynamically rather than through static architectural choices.

### 8.2 Integration of Foundation Models

The integration of large language models into multi-agent financial systems represents a promising research direction with significant implications for the accuracy-resource tradeoff. New generation models that use more complex reasoning to enhance capabilities provide researchers with new approaches to improving single-agent or system-level performance [3].

Domain-specific prompt tuning and rule injection effects demonstrate that foundation models can achieve substantial accuracy improvements through targeted optimization [7]. These improvements may enable single agents to handle tasks previously requiring multi-agent coordination, reducing system complexity while maintaining or improving overall performance.

### 8.3 Hybrid Human-AI Systems

The integration of human reasoning into multi-agent systems offers a promising avenue for managing complexity while maintaining decision quality. Rather than viewing the choice between fully automated and human-controlled systems as binary, future research should explore continuous spectrums of human-AI collaboration.

Self-checking mechanisms where different agents validate each other's work, transparent reasoning processes that enable human oversight, and adaptive handoff protocols that escalate complex decisions to human operators represent practical approaches to hybrid system design [11]. These mechanisms acknowledge the current limitations of autonomous multi-agent systems while preserving the efficiency benefits of automated processing for routine tasks.

## 9. Conclusion

The question of whether multi-agent coordination algorithms in financial decision support offer an optimal compromise between accuracy and resource use, or whether Bayesian reasoning leads to unavoidable complexity explosions, does not admit a simple affirmative or negative answer. The evidence reviewed in this analysis suggests a more nuanced conclusion: the accuracy-resource tradeoff in multi-agent financial systems is fundamentally problem-dependent, with achievable performance limits determined by the structural characteristics of the decision problem, the architectural choices made in system design, and the practical constraints imposed by real-time requirements.

Multi-agent systems demonstrate remarkable accuracy improvements over single-agent approaches, as evidenced by systems achieving annualized returns exceeding 50% with Sharpe ratios above 3.0 [8]. These performance gains arise from the ability to decompose complex financial decisions into specialized subtasks handled by agents optimized for specific functions, enabling analysis that considers multiple perspectives and detects risks that monolithic systems might miss.

However, these benefits come with significant computational costs. The efficiency explosions that arise from autoregressive architecture, the state and action space explosions in multi-agent Markov decision processes, and the coordination overhead that scales superlinearly with agent count all impose practical limits on system scalability. Bayesian reasoning approaches that would theoretically provide optimal decisions become computationally intractable for all but the smallest systems, necessitating heuristic approximations, rule-based simplifications, and architectural constraints.

The most effective approach to managing this tradeoff appears to be hybrid systems that combine automated multi-agent processing with human oversight. By directing computational resources toward high-value analytical tasks while maintaining human involvement for complex judgments and regulatory compliance, these systems achieve favorable balances between accuracy and resource efficiency that neither fully autonomous nor fully human-controlled approaches can match.

Future research should focus on developing more sophisticated mechanisms for dynamically adjusting the accuracy-resource tradeoff based on problem characteristics, integrating foundation models that reduce the need for complex multi-agent coordination, and creating evaluation frameworks that assess systems across multiple performance dimensions rather than optimizing for single metrics. As financial markets continue to evolve in complexity and the demands placed on decision support systems increase, the development of multi-agent architectures that achieve robust performance across varying resource constraints will remain a critical research priority.

## References

[1] Arora, S., & Barak, B. (2009). Computational Complexity: A Modern Approach. Cambridge University Press.

[2] Feriani, A., & Hossain, E. (2021). Single and multi-agent deep reinforcement learning for demand-side management in smart grids. Elsevier.

[3] OpenAI. (2024). Introduction of o1 model. OpenAI Research.

[4] Gautier, A., Rigter, M., Lacerda, B., Hawes, N., & Wooldridge, M. (2025). Risk-Constrained Planning for Multi-Agent Systems with Shared Resources. University of Oxford.

[5] Arize AI. (2024). Evaluating Multi-Agent Systems: Core Evaluation Strategies Explained. Arize Documentation.

[6] Multiagents.org. (2025). Reliable Decision Making for Multi-Agent LLM Systems. AAAI 2025.

[7] arXiv:2505.19197. (2025). Financial Document QA with Multi-Agent Systems. arXiv Preprint.

[8] ACL Anthology. (2025). QuantAgents: A Sophisticated Multi-Agent Financial System. EMNLP Findings.

[9] Creatio. (2024). Multi-Agent Systems: Coordination and Control. Creatio Glossary.

[10] Billtrust. (2024). Multi-Agent AI for Finance Operations. Billtrust Resources.

[11] Swarms API. (2024). Building Multi-Agent Systems for Finance and Accounting. Medium Technical Guide.

[12] MDPI Sensors. (2021). Distributed Constraint Optimization Problems in Multi-Agent Systems. MDPI.

[13] Substack. (2025). Counting Down to AGI: Multi-Agent System Capabilities. Shashank Substack.

## Annotations


## Sources
[1] https://aclanthology.org/2025.findings-emnlp.945.pdf
[2] https://arize.com/docs/phoenix/evaluation/concepts-evals/evaluating-multi-agent-systems
[3] https://arxiv.org/html/2402.01108v1
[4] https://arxiv.org/html/2412.17481v1
[5] https://arxiv.org/html/2503.13415v1
[6] https://arxiv.org/html/2505.19197v1
[7] https://link.springer.com/article/10.1007/s10462-025-11340-5
[8] https://medium.com/@kyeg/building-multi-agent-systems-for-finance-accounting-with-the-swarms-api-a-technical-guide-bf6f7005b708
[9] https://multiagents.org/2025_artifacts/reliable_decision_making_for_multi_agent_llm_systems.pdf
[10] https://proceedings.neurips.cc/paper_files/paper/2024/file/f7ae4fe91d96f50abc2211f09b6a7e49-Paper-Conference.pdf
[11] https://shash42.substack.com/p/counting-down-capabilities-to-agi
[12] https://www.billtrust.com/resources/blog/multi-agent-ai-transform-ar
[13] https://www.creatio.com/glossary/multi-agent-systems
[14] https://www.mdpi.com/1424-8220/21/11/3807
[15] https://www.robots.ox.ac.uk/~nickh/papers/gautier23aamas.pdf