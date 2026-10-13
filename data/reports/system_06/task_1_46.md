# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 1d989a0a | **Time:** 114.59s | **Cost:** $0.12483
--------------------------------------------------------------------------------

# By What Process Does the Responsibility Assignment Matrix in AI Systems Achieve Dynamic Equilibrium via Markov Decision Processes?

## Abstract

The integration of responsibility assignment matrices (RAMs) with Markov decision processes (MDPs) represents a sophisticated approach to achieving dynamic equilibrium in multi-agent artificial intelligence systems. This research report examines the theoretical foundations, mathematical frameworks, and practical mechanisms through which responsibility allocation achieves stable yet adaptive balance in complex AI environments. Drawing upon contemporary research in multi-agent systems, reinforcement learning, and AI governance, we analyze how MDP-based frameworks enable responsibility matrices to maintain equilibrium while accommodating environmental uncertainty, agent autonomy, and evolving task requirements. The investigation reveals that dynamic equilibrium emerges through iterative policy optimization, reward signal calibration, and coordinated state-action mapping that balances individual agent objectives with collective system goals.

## 1. Introduction

The proliferation of autonomous AI systems across critical domains—from maritime patrolling to healthcare delivery—has necessitated sophisticated frameworks for responsibility assignment and coordination. As organizations transition from static governance structures to adaptive, AI-embedded operational models, understanding how responsibility allocation achieves and maintains equilibrium becomes paramount [3]. The challenge lies not merely in assigning tasks to agents, but in creating mechanisms that enable responsibility matrices to evolve dynamically while preserving system stability and goal alignment.

Markov decision processes provide the mathematical foundation for modeling sequential decision-making under uncertainty, offering a rigorous framework for understanding how agents navigate complex state spaces while optimizing cumulative rewards [2]. When extended to multi-agent environments, MDPs enable the coordination of responsibility allocation across distributed systems, creating pathways for achieving what researchers term "dynamic equilibrium"—a state where responsibility assignments remain stable enough to ensure reliable task execution yet flexible enough to adapt to changing environmental conditions [1].

This report synthesizes contemporary research to address the fundamental question: by what process does the responsibility assignment matrix in AI systems achieve dynamic equilibrium via Markov decision processes? We examine the theoretical underpinnings of this integration, the algorithmic mechanisms that enable equilibrium maintenance, and the practical implications for AI governance and autonomous system design.

## 2. Theoretical Foundations of Responsibility Assignment Matrices

### 2.1 Conceptual Framework for Responsibility Matrices

Responsibility assignment matrices serve as structural blueprints for distributing tasks, authorities, and accountabilities across multi-agent systems. Unlike traditional organizational hierarchies, AI-based responsibility matrices must accommodate the inherent uncertainty of dynamic environments while maintaining clear lines of accountability [7]. The matrix structure enables organizations to match responsibility splits with the velocity and scale of their AI strategies, moving beyond shared committees to establish clear lines of accountability that are embedded directly into how AI systems are designed and deployed [3].

The fundamental challenge in responsibility matrix design lies in balancing specificity with flexibility. Process frameworks that guide responsibility assignment must be flexible enough to fit an organization's unique circumstances, yet structured enough to ensure that responsibility can be assigned to the most qualified stakeholders [7]. This tension between rigidity and adaptability forms the core theoretical challenge that MDP-based approaches seek to resolve.

### 2.2 Multi-Agent Decision Environments

In multi-agent systems, responsibility assignment occurs within environments characterized by partial observability, stochastic transitions, and competing agent objectives [8]. The environment state changes either because of an agent's action or due to external events, creating a complex interplay between individual agent decisions and system-level outcomes [2]. This dynamic necessitates decision-making frameworks that can model not only individual agent behavior but also the emergent properties of coordinated action.

The Markov property provides the mathematical foundation for such modeling by asserting that the future and the past are conditionally independent given the present [11]. This memoryless property simplifies the representation of complex decision histories while preserving the essential structure of sequential decision-making. For responsibility assignment matrices, this means that optimal allocation decisions can be based solely on the current state of the system rather than requiring complete historical context.

## 3. Markov Decision Process Framework for Responsibility Equilibrium

### 3.1 Formal MDP Definition

A Markov decision process is formally defined as a 4-tuple (S, A, T, R), where S represents the state space, A denotes the action space, T describes the transition function, and R specifies the reward function [15]. For responsibility assignment applications, these components take on specific interpretations:

The state space S encompasses all possible configurations of responsibility assignments across the system. Each state s ∈ S represents a particular allocation of tasks, authorities, and accountabilities among agents. The action space A comprises all possible reassignment decisions, including task reallocation, authority modification, and accountability transfer. The transition function T(s, a, s') captures the probability of moving from responsibility state s to state s' following action a, modeling the uncertainty inherent in organizational change processes. The reward function R(s, a) assigns numerical values to state-action pairs, encoding the preferences of system designers regarding responsibility allocation quality.

### 3.2 Value Functions and Optimal Policies

The objective in MDP-based responsibility assignment is to select actions that maximize a long-term measure of total reward [10]. This optimization is captured by the value function, which estimates the expected cumulative reward from any given state under an optimal policy. The value function V(s) satisfies the Bellman equation:

$$V(s) = \max_{a \in A} \left[ R(s, a) + \gamma \sum_{s' \in S} T(s, a, s') V(s') \right]$$

where γ ∈ [0, 1] is the discount factor that balances immediate rewards against future outcomes [11]. The optimal policy π*(s) prescribes the action that maximizes the right-hand side of this equation for each state.

For responsibility assignment matrices, value iteration algorithms provide a mechanism for computing optimal policies through iterative updates [2]. Starting with initial value estimates (typically zero), the algorithm propagates reward information backward through the state space until convergence. In the context of responsibility equilibrium, this propagation represents the gradual alignment of responsibility assignments with system-level objectives.

### 3.3 Dynamic Equilibrium Through Policy Iteration

Dynamic equilibrium in responsibility assignment matrices emerges through the interplay between policy evaluation and policy improvement. The policy iteration algorithm alternates between evaluating the current policy's value function and improving the policy based on that evaluation [14]. This iterative process continues until no further improvement is possible, at which point the policy is optimal and the system has achieved equilibrium.

The convergence of policy iteration ensures that responsibility assignment matrices can reach stable configurations that optimize long-term system performance. However, the nature of this equilibrium differs fundamentally from static optimization. Because MDPs model sequential decision-making over infinite horizons, the equilibrium represents a dynamic balance—agents continuously make decisions based on current states, but the policy governing those decisions remains stable [6].

## 4. Mechanisms for Achieving Dynamic Equilibrium

### 4.1 Reward Signal Design for Responsibility Alignment

The achievement of dynamic equilibrium in responsibility assignment matrices critically depends on the design of reward signals that appropriately align agent behavior with system objectives. Reward functions must capture not only immediate task completion but also long-term considerations such as accountability clarity, coordination efficiency, and adaptability to change [4]. Poorly designed reward signals can lead to equilibrium states that optimize the wrong objectives, a phenomenon analogous to Goodhart's law in policy design.

For multi-agent responsibility assignment, reward functions must balance individual agent incentives against collective system goals. Research on multi-objective optimization in multi-robot systems demonstrates that learning-inspired algorithms can effectively navigate trade-offs between competing objectives [1]. The reward structure must encode preferences over responsibility configurations while allowing sufficient flexibility for agents to discover efficient allocation patterns.

### 4.2 Transition Dynamics and Environmental Uncertainty

The transition function in MDP-based responsibility assignment models the probabilistic outcomes of reassignment actions. Environmental uncertainty arises from multiple sources: incomplete information about agent capabilities, unpredictable changes in task requirements, and stochastic external events [8]. The transition dynamics determine how responsibility matrices evolve over time, with different transition structures leading to different equilibrium properties.

In highly uncertain environments, responsibility assignment matrices must exhibit robustness—the ability to maintain functional equilibrium despite unexpected state transitions. This robustness emerges from policies that hedge against uncertainty by maintaining redundant capabilities and flexible assignment options [15]. The balance between specialization (which improves efficiency) and flexibility (which enhances robustness) represents a fundamental trade-off in responsibility matrix design.

### 4.3 Coordination Mechanisms for Multi-Agent Equilibrium

Achieving equilibrium in multi-agent responsibility assignment requires coordination mechanisms that align individual agent decisions with collective outcomes. The consensus-based bundle algorithm (CBBA) provides one such mechanism, combining auction and consensus methods to achieve polynomial-time task allocation [1]. This approach enables distant agents to coordinate without requiring explicit network topology to reach a central manager, instead sharing application letters with neighborhoods and allowing managers to select team members based on resumes.

For responsibility assignment, similar coordination mechanisms ensure that individual agents' optimal actions collectively produce system-level equilibrium. Multi-agent MDP formulations extend single-agent frameworks to capture the interactions between agents' decisions [2]. When transition and reward functions factor into per-agent components without dependence on other agents' local state, the resulting structure enables decentralized coordination while preserving theoretical tractability [8].

## 5. Algorithmic Approaches to Equilibrium Maintenance

### 5.1 Value Iteration for Responsibility Optimization

Value iteration provides a foundational algorithm for computing optimal responsibility assignment policies. The algorithm proceeds by iteratively updating value estimates until convergence, with each update propagating reward information one step further backward through the state space [2]. For responsibility assignment matrices, this propagation represents the gradual alignment of allocation decisions with long-term system objectives.

The computational complexity of value iteration grows with the size of the state and action spaces, creating scalability challenges for large-scale responsibility assignment problems. Recent research addresses this challenge through MDP decomposition techniques that divide large problems into smaller, tractable sub-problems [16]. By decomposing global MDPs into goal-relevant sub-MDPs and recombining results through priority-based meta-policy coordination, these approaches maintain computational efficiency while preserving solution quality.

### 5.2 Policy Gradient Methods for Adaptive Responsibility Assignment

Policy gradient methods offer an alternative approach to responsibility assignment optimization that directly optimizes parameterized policies through gradient descent [14]. These methods are particularly suited to continuous action spaces and can incorporate function approximation to handle large state spaces. The softmax policy structure, where action probabilities are proportional to exponential value estimates, provides a natural framework for stochastic responsibility allocation:

$$\pi(a|s) \propto \exp(\epsilon Q(s, a))$$

where ε controls the degree of stochasticity in decision-making [14]. This stochasticity enables responsibility assignment matrices to explore multiple allocation patterns while converging toward optimal configurations.

Recent advances in policy optimization algorithms demonstrate theoretical guarantees for convergence to optimal policies under appropriate conditions [14]. These convergence results provide mathematical foundations for the claim that responsibility assignment matrices can achieve dynamic equilibrium through MDP-based optimization.

### 5.3 Deep Reinforcement Learning for Complex Responsibility Environments

The integration of deep learning with reinforcement learning has greatly contributed to the literature on controlling and coordinating autonomous machines, becoming a growing trend in AI systems research [1]. Deep Q-networks and actor-critic methods enable responsibility assignment in high-dimensional state spaces where traditional tabular methods become intractable.

For responsibility assignment matrices in complex environments, deep RL methods provide viable approaches to addressing dynamic and uncertain conditions [1]. The ability to learn effective policies from raw sensory inputs enables responsibility assignment systems to adapt to environmental changes without explicit modeling of transition dynamics. This adaptability is essential for maintaining equilibrium in environments where responsibility requirements evolve over time.

## 6. Governance and Accountability Considerations

### 6.1 Embedding Governance in Responsibility Matrices

The achievement of dynamic equilibrium in responsibility assignment matrices must be understood within the broader context of AI governance. Organizations are moving from shared committees to clear lines of accountability, embedding governance directly into how AI systems are designed and deployed [3]. This embedding requires responsibility matrices that not only optimize task allocation but also ensure compliance with ethical principles, legal requirements, and organizational policies.

Value alignment between AI systems and human users represents a critical governance consideration for responsibility assignment [4]. The reward structures that govern agent behavior must reflect human values rather than narrow optimization targets. This alignment requires mechanisms to build constraints on AI's action alternatives, ensuring compliance with ethics, laws, and regulations while maintaining the flexibility needed for adaptive equilibrium.

### 6.2 Control Mechanisms and Human Oversight

Dynamic equilibrium in responsibility assignment matrices does not imply complete autonomy. Control mechanisms that allow humans to override AI decisions and intervene mid-action are essential for robust governance [4]. These override capabilities ensure that responsibility assignment remains responsive to human judgment even as AI systems optimize for defined objectives.

The concept of "switch-off control of the last resort" provides a fundamental safeguard for AI-driven responsibility assignment [4]. While AI agents may achieve sophisticated coordination and efficient task allocation, human oversight remains necessary to address edge cases, ethical dilemmas, and situations where AI objectives diverge from human values. The equilibrium state of responsibility assignment matrices must therefore accommodate the possibility of human intervention without losing the benefits of automated coordination.

### 6.3 Adaptive Governance for Evolving AI Capabilities

As AI agents become more capable, governance frameworks must evolve in real time—shifting from static controls to continuous oversight that keeps pace with innovation [3]. This evolution requires responsibility assignment matrices that can adapt their equilibrium states as AI capabilities expand and new coordination challenges emerge.

The transition from reactive to proactive governance represents a fundamental shift in how organizations approach responsibility assignment [3]. Rather than simply responding to new risks, maturing organizations build adaptive, resilient governance that scales with AI's growing autonomy. MDP-based responsibility assignment provides a mathematical framework for this adaptive governance by enabling continuous policy optimization in response to changing conditions.

## 7. Scalability and Computational Considerations

### 7.1 State Space Complexity in Large-Scale Systems

The scalability of MDP-based responsibility assignment depends critically on the structure of the state and action spaces. As the number of agents and tasks increases, the state space grows combinatorially, creating computational challenges for exact solution methods [15]. For n agents and m tasks, the number of possible responsibility assignments grows as m^n, quickly exceeding the capacity of exhaustive enumeration.

Recent research addresses this scalability challenge through hierarchical decomposition approaches [16]. By identifying goal-relevant sub-MDPs and computing priority scores using local solvers, these methods enable dynamic assignment of agents to sub-problems while maintaining coherent global coordination. Theoretical proofs establish that, under certain independence assumptions, the recombined policy from sub-MDPs is provably equivalent to the global MDP policy [16].

### 7.2 Decentralized Coordination for Distributed Responsibility

Decentralized coordination mechanisms enable responsibility assignment in distributed systems where central coordination would create bottlenecks or single points of failure. Multi-agent MDP formulations support decentralized decision-making by factoring transition and reward functions into per-agent components [8]. This factorization enables agents to make locally optimal decisions while contributing to global equilibrium.

The consensus-based bundle algorithm exemplifies decentralized responsibility assignment, allowing agents to coordinate through local communication without requiring global state information [1]. This approach is particularly valuable for large-scale systems where communication latency or bandwidth constraints limit centralized coordination. The equilibrium properties of such decentralized systems depend on the communication structure and the alignment of local objectives with global goals.

## 8. Challenges and Future Directions

### 8.1 Explainability and Interpretability

Making MDP-based responsibility assignment more explainable and interpretable remains crucial for real-world applications [15]. When responsibility matrices govern critical decisions in healthcare, finance, or public safety, stakeholders require understanding of how assignments are made and how equilibrium is maintained. The mathematical elegance of MDP formulations does not automatically translate to human interpretability.

Process frameworks for responsible AI must account for the needs of stakeholders who wish to tie activities to desired business and societal outcomes [7]. The challenge lies in developing representations of responsibility assignment that are simultaneously rigorous enough for computational optimization and accessible enough for human comprehension and oversight.

### 8.2 Robustness to Model Misspecification

MDP-based responsibility assignment assumes accurate models of transition dynamics and reward structures. In practice, these models are often misspecified, leading to policies that perform poorly in real environments [15]. The equilibrium achieved under incorrect assumptions may not translate to the actual operating environment, creating risks for systems that depend on reliable responsibility allocation.

Robust MDP approaches address this challenge by optimizing for worst-case scenarios rather than expected outcomes. For responsibility assignment matrices, robust methods ensure that equilibrium states remain stable even when transition probabilities or reward values differ from estimates. This robustness is essential for high-stakes applications where responsibility misallocation could have serious consequences.

### 8.3 Integration with Emerging AI Paradigms

The rapid evolution of AI capabilities creates new challenges and opportunities for responsibility assignment. As reasoning-focused architectures and cognitive systems become more prevalent, responsibility matrices must accommodate increasingly sophisticated autonomous behavior [5]. The integration of large language models and multi-modal AI systems into coordination frameworks requires new approaches to responsibility assignment that go beyond traditional task allocation.

The emergence of AI agents that can learn, reason, and adapt independently necessitates governance frameworks that evolve in real time [3]. Future responsibility assignment matrices must achieve dynamic equilibrium not only within defined task environments but also across the boundaries between different AI paradigms and capabilities.

## 9. Conclusion

The responsibility assignment matrix in AI systems achieves dynamic equilibrium through the integration of Markov decision process frameworks that enable sequential optimization under uncertainty. This integration operates through several interconnected mechanisms: the formal MDP structure provides mathematical foundations for modeling responsibility allocation as sequential decision-making; value functions and optimal policies enable computation of equilibrium states that balance immediate task completion against long-term system objectives; and coordination mechanisms ensure that individual agent decisions align with collective outcomes.

The achievement of dynamic equilibrium differs fundamentally from static optimization. Rather than converging to a fixed allocation, MDP-based responsibility assignment maintains stable policies that guide adaptive responses to changing conditions. This dynamic stability emerges through iterative policy optimization, where reward signals, transition dynamics, and coordination mechanisms interact to produce equilibrium states that are both efficient and robust.

Contemporary research demonstrates that deep reinforcement learning and multi-agent coordination algorithms provide viable approaches to responsibility assignment in complex, dynamic environments [1]. The scalability of these approaches depends on decomposition techniques, decentralized coordination, and function approximation methods that enable tractable computation even for large systems [16].

The governance implications of MDP-based responsibility assignment extend beyond technical optimization to fundamental questions of accountability and control. As organizations embed governance directly into AI system design, responsibility matrices must balance optimization objectives with ethical constraints, legal compliance, and human oversight requirements [3]. The dynamic equilibrium achieved through MDP-based approaches must accommodate the possibility of human intervention while providing the efficiency benefits of automated coordination.

Future research directions include improving the explainability of MDP-based responsibility assignment, developing robust methods for model misspecification, and integrating emerging AI capabilities into coordination frameworks. As AI systems become more autonomous and capable, the mathematical frameworks for responsibility assignment must evolve to address new challenges while maintaining the fundamental properties that enable dynamic equilibrium.

The synthesis of responsibility assignment matrices with Markov decision processes represents a mature and productive research area with significant practical implications. By providing rigorous mathematical foundations for sequential decision-making under uncertainty, MDP frameworks enable the design of AI systems that achieve stable yet adaptive responsibility allocation—meeting the complex coordination challenges of modern autonomous systems while preserving the accountability and control necessary for trustworthy AI deployment.

## References

[1] L. Huang, M. Zhou, H. Han, S. Wang, and A. Albeshri, "Learning-inspired immune algorithm for multiobjective-optimized multirobot maritime patrolling," IEEE Internet of Things Journal, vol. 11, no. 6, pp. 9870-9881, 2023.

[2] Multiagent Systems Course Materials, University of South Carolina. [Online]. Available: https://jmvidal.cse.sc.edu/papers/mas.pdf

[3] PwC, "Responsible AI Survey," 2024. [Online]. Available: https://www.pwc.com/us/en/tech-effect/ai-analytics/responsible-ai-survey.html

[4] "AI Decision-Making and Resource Allocation," arXiv preprint arXiv:2512.04489v2, 2024. [Online]. Available: https://arxiv.org/html/2512.04489v2

[5] "2025 State of AI Report: The Year of Action," MDP Group, 2025. [Online]. Available: https://mdpgroup.com/en/blog/2025-state-of-ai-report-the-year-of-action/

[6] C. Sandu, "Markov Decision Processes (MDPs)," Medium, Aug. 2024. [Online]. Available: https://medium.com/@calin.sandu/markov-decision-processes-mdps-2ba64c90e689

[7] Georgetown CSET, "A Matrix for Selecting Responsible AI Frameworks," 2024. [Online]. Available: https://cset.georgetown.edu/wp-content/uploads/CSET-A-Matrix-for-Selecting-Responsible-AI-Frameworks.pdf

[8] "Taxonomy of Solution Approaches for Multi-Agent Decision Processes," JAIR, vol. 12233. [Online]. Available: https://www.jair.org/index.php/jair/article/download/12233/26666/26325

[9] "2025 Artificial Intelligence Equilibrium Report," LinkedIn, 2025. [Online]. Available: https://www.linkedin.com/pulse/2025-artificial-intelligence-equilibrium-report-capital-abufadda-1xmxf

[10] "Markov Decision Process," ScienceDirect Topics. [Online]. Available: https://www.sciencedirect.com/topics/mathematics/markov-decision-process

[11] S. Russell and P. Norvig, "Markov Decision Processes," in Artificial Intelligence: A Modern Approach, UC Berkeley EECS. [Online]. Available: https://inst.eecs.berkeley.edu/~cs188/textbook/mdp/markov-decision-processes.html

[12] "Autonomous Driving in Shared Space Formulated as MDP," Division of Systems Engineering. [Online]. Available: http://www.diva-portal.org/smash/get/diva2:1326805/FULLTEXT01.pdf

[13] "The Intelligent Trap: Markov Decision Process Framework for Dynamic Honeypot," University of Wellington Open Access, 2024. [Online]. Available: https://openaccess.wgtn.ac.nz/articles/thesis/The_Intelligent_Trap_Markov_Decision_Process_Framework_for_Dynamic_Honeypot/29899967/1/files/57152174.pdf

[14] "Policy Optimization with Entropy Regularization," Proceedings of Machine Learning Research, vol. 162. [Online]. Available: https://proceedings.mlr.press/v162/chen22ab/chen22ab.pdf

[15] "Understanding Markov Decision Processes," Telnyx Learning Resources, 2024. [Online]. Available: https://telnyx.com/learn-ai/markov-decision-process

[16] "Scalable UAV Mission Management via MDP Decomposition," arXiv preprint arXiv:2512.00838v1, 2024. [Online]. Available: https://arxiv.org/html/2512.00838v1

## Annotations


## Sources
[1] http://katselis.web.engr.illinois.edu/ECE586/Lecture9.pdf
[2] http://www.diva-portal.org/smash/get/diva2:1326805/FULLTEXT01.pdf
[3] https://arxiv.org/html/2404.16957v2
[4] https://arxiv.org/html/2508.20688v1
[5] https://arxiv.org/html/2512.00838v1
[6] https://arxiv.org/html/2512.04489v2
[7] https://arxiv.org/pdf/2507.06278
[8] https://cdn.aaai.org/AAAI/2005/IAAI05-011.pdf
[9] https://chercheurs.lille.inria.fr/munos/papers/files/MDPIA_chap3.pdf
[10] https://cset.georgetown.edu/wp-content/uploads/CSET-A-Matrix-for-Selecting-Responsible-AI-Frameworks.pdf
[11] https://dspace.mit.edu/bitstream/handle/1721.1/77100/824780540-MIT.pdf?sequence=2
[12] https://en.wikipedia.org/wiki/Markov_decision_process
[13] https://galileo.ai/blog/stability-strategies-dynamic-multi-agents
[14] https://inst.eecs.berkeley.edu/~cs188/textbook/mdp/markov-decision-processes.html
[15] https://jmvidal.cse.sc.edu/papers/mas.pdf
[16] https://link.springer.com/article/10.1007/s43681-024-00524-4
[17] https://mdpgroup.com/en/blog/2025-state-of-ai-report-the-year-of-action/
[18] https://medium.com/@calin.sandu/markov-decision-processes-mdps-2ba64c90e689
[19] https://medium.com/@ngao7/markov-decision-process-basics-3da5144d3348
[20] https://openaccess.wgtn.ac.nz/articles/thesis/The_Intelligent_Trap_Markov_Decision_Process_Framework_for_Dynamic_Honeypot/29899967/1/files/57152174.pdf
[21] https://pmc.ncbi.nlm.nih.gov/articles/PMC12149378/
[22] https://proceedings.mlr.press/v162/chen22ab/chen22ab.pdf
[23] https://telnyx.com/learn-ai/markov-decision-process
[24] https://theses.hal.science/tel-03699837/file/109080_TOURNAIRE_2022.pdf
[25] https://www.jair.org/index.php/jair/article/download/12233/26666/26325
[26] https://www.linkedin.com/pulse/2025-artificial-intelligence-equilibrium-report-capital-abufadda-1xmxf
[27] https://www.pwc.com/us/en/tech-effect/ai-analytics/responsible-ai-survey.html
[28] https://www.sciencedirect.com/topics/mathematics/markov-decision-process
[29] https://www.spiceworks.com/soft-tech/what-is-markov-decision-process/