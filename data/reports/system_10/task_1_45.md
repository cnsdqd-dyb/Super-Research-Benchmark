# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 86d2573b | **Time:** 118.77s | **Cost:** $1.06996
--------------------------------------------------------------------------------

# Dynamic Privacy Preferences and the Stability of Optimal Social Welfare Solutions in Multi-Agent Systems

The question of whether dynamically evolving privacy preferences destabilize optimal social welfare solutions represents a critical intersection between mechanism design, behavioral economics, and multi-agent decision theory. This comprehensive analysis synthesizes recent research across these domains to demonstrate that the dynamic nature of privacy preferences introduces significant complications for traditional social welfare optimization frameworks. While privacy-constrained mechanisms can be designed to maintain certain welfare properties, the temporal evolution of privacy preferences—driven by both adaptive learning and exogenous preference shifts—creates fundamental tensions between privacy preservation and welfare maximization that cannot be fully resolved within classical equilibrium frameworks.

## Theoretical Foundations of Social Welfare Functions and Privacy Constraints

### The Classical Social Welfare Framework

Social welfare functions represent a cornerstone concept in economic theory, providing mathematical formulations for aggregating individual preferences into collective societal decisions[13][46][52]. The fundamental approach involves mapping individual preference orderings into a single, coherent social preference ordering that ideally satisfies multiple desirable axioms. Kenneth Arrow's impossibility theorem established that no social welfare function can simultaneously satisfy five seemingly innocuous conditions: unrestricted domain, non-dictatorship, Pareto efficiency, independence of irrelevant alternatives, and the requirement of transitivity[13][16][46]. This foundational result has profound implications for understanding the constraints on any aggregation mechanism, including those that must accommodate privacy considerations.

The classical framework assumes that preferences exist exogenously and remain stable across time, allowing analysts to identify optimal allocations that maximize aggregate welfare. Arrow's theorem demonstrates that even under this simplified assumption, fundamental impossibilities arise when attempting to satisfy reasonable aggregation criteria. The traditional approach to social welfare maximization typically focuses on finding allocations that either maximize the sum of individual utilities (utilitarian approach) or that cannot be improved for one individual without harming another (Pareto optimality)[29][33]. The fundamental theorems of welfare economics establish that under certain conditions—complete markets, perfect information, and locally nonsatiated preferences—competitive equilibria are Pareto efficient[29]. However, these conditions are increasingly violated in real-world settings, particularly when privacy considerations are introduced as explicit constraints on information available to decision-makers.

### Privacy as a Mechanism Design Constraint

Recent work in mechanism design has begun to incorporate privacy as an explicit constraint on the information that mechanisms can collect and utilize[3][31][34]. These approaches measure privacy loss using information-theoretic concepts, particularly the Kullback-Leibler divergence between a designer's prior and posterior beliefs about agent types[3][31]. The framework treats privacy as an exogenous constraint—a maximum permissible level of information that mechanisms may gather—rather than as an endogenously determined preference[3]. This represents a "paternalistic" approach wherein privacy protection is imposed externally rather than derived from revealed preferences[3].

The design of privacy-constrained mechanisms reveals fundamental trade-offs between privacy preservation and mechanism performance. Research has shown that optimal mechanisms under privacy constraints exhibit particular structural properties: they partition agent types into discrete intervals, with agents truthfully revealing only which interval contains their true type rather than their precise characteristics[3]. This coarsening of information has direct welfare implications. While the mechanism design literature traditionally focuses on incentive compatibility and individual rationality, privacy constraints introduce an additional dimension that fundamentally alters the set of feasible mechanisms[3][31].

The measurement of privacy loss itself introduces methodological complexity. By treating privacy loss as the difference between the designer's posterior and prior beliefs using relative entropy (KL divergence), the framework acknowledges that different information states create different degrees of privacy violation[3][31]. An important finding from this literature is that restricting mechanisms to operate on only partial information—revealing to some agents only public information or only private information—can reduce both secret information leakage and unnecessary omission of public information in multi-agent systems[1]. This suggests that when privacy preferences vary dynamically, the optimal information architecture of mechanisms must adapt to accommodate changing privacy requirements.

## The Nature of Dynamic Preferences: Theoretical Characterization

### Instability of Preferences and Revealed Preference Theory

A critical challenge for integrating privacy preferences into social welfare frameworks emerges from the empirical reality that preferences themselves are fundamentally unstable and endogenously determined[20][40][42]. The classical revealed preference framework, developed to give operational meaning to preference statements through observed choices, encounters substantial difficulties when preferences themselves evolve over time[20]. This instability extends to all preference dimensions, including those related to privacy, and creates a logical problem: if preferences change dynamically, what constitutes an "optimal" solution to a social welfare problem?

Research on preference instability demonstrates that preferences depend on contingency, ambiguity, and dynamics in ways not captured by static utility models[20]. People's preferences involve emotions, imagined futures, identity-based narratives, and socially generated norms—elements that naturally fluctuate over time and in response to context[20]. While behavioral economists have long documented preference reversals and violations of transitivity[44], the fundamental issue raised by preference dynamics is whether welfare economics can even be meaningfully performed when the measuring rod itself changes[39].

The welfare economics of adaptive preferences offers one approach to this problem[39]. Under adaptive preferences, individuals adjust their preferences to their current circumstances—for instance, accepting lower consumption when they cannot afford more. The framework of "improvement paths" proposes that welfare comparisons can be made across different preference states if preferences follow certain patterns of adaptation[39]. However, this approach requires strong assumptions about the "laws of motion" governing preference change, assumptions that become increasingly difficult to justify when applied to privacy preferences, which are shaped by legal environments, social norms, and technological affordances that can shift rapidly[20][42].

### Time-Inconsistent Preferences and Multi-Self Models

An important class of dynamic preferences involves time-inconsistency, where preferences in one time period conflict with preferences in another period[15][18][23][40]. The classic example involves choosing between commitment devices that limit future choices versus retaining maximum flexibility[15]. Time-inconsistent preferences create fundamental conflicts between different temporal selves of the same individual, raising welfare-theoretic questions about which temporal self's preferences should be respected[18].

Time-inconsistency can arise from various sources: present bias, where immediate consequences are overweighted; changing beliefs about future consequences; or genuine shifts in tastes[40]. Empirical evidence demonstrates that time-inconsistency patterns are far more complex than commonly modeled, with individuals exhibiting not only inconsistency and non-stationarity but also variance in how their time preferences change[40]. In a detailed longitudinal study with repeated measurements over twelve weeks, researchers found that approximately 32 to 56 percent of subjects exhibited preferences that could not be explained by standard time-inconsistency models[40].

Privacy preferences exhibit characteristics suggesting time-inconsistency. Individuals may initially prefer to maintain privacy over certain information but later regret withholding that information when circumstances change. Conversely, people might initially share personal data but later prefer that the disclosure had not occurred. The dynamic nature of privacy preferences in networked environments—where past disclosures remain available to others—creates particular complications for welfare analysis, as earlier privacy choices constrain future options in ways that violate standard assumptions about preference consistency.

## Multi-Agent Privacy in Mechanism Design and Information Aggregation

### Contextual Privacy and Multi-Agent Reasoning

Recent advances in multi-agent systems have begun addressing the challenge of protecting contextual privacy—privacy that depends on specific social contexts and relationships—while maintaining the ability to aggregate information necessary for collective decision-making[1]. Unlike absolute privacy, which treats all information as equally sensitive, contextual privacy recognizes that information appropriateness depends on context, relationship, and consent[1]. Implementing contextual privacy in multi-agent systems presents significant challenges, as agents must balance disclosure of information necessary for coordination with protection of sensitive details inappropriate for broader disclosure.

A multi-agent framework has been proposed that decomposes privacy reasoning into specialized stages, rather than attempting to handle privacy protection through a single decision-making entity[1]. By controlling which agents see which information, this approach can substantially reduce private information leakage—approximately 36% reduction for systems like Llama3 compared to single-agent approaches—while maintaining the fidelity of public content[1]. Importantly, the research found that while multi-agent approaches generally outperform single-agent systems in privacy protection, even sophisticated three-agent frameworks face considerable challenges in reliably distinguishing public from private information[1]. This suggests that the complexity of privacy classification itself introduces a source of instability in multi-agent systems: when different agents have different assessments of what information should remain private, coordination becomes difficult.

### Privacy in Distributed Constraint Satisfaction

Multi-agent decision-making problems often require agents to communicate extensively while protecting sensitive information[4]. Abstract argumentation frameworks provide one approach, allowing agents to reason about conflicts while limiting disclosure of private information[4]. In such systems, agents can coordinate their actions to achieve socially optimal outcomes while maintaining privacy through restricted communication protocols[4]. Perfect information security has been achieved in some restricted domains where the protocol prevents agents' private arguments from being disclosed during coordination[4].

The feasibility of achieving social optimality while preserving privacy depends critically on the structure of the decision problem[4]. In distributed constraint satisfaction settings, socially optimal solutions exist that require coordination, yet agents have private information—both observational and preferential—that they prefer not to disclose[4]. The tension arises because coordination often requires information sharing, and any information shared potentially reveals private details. When privacy preferences are static, protocols can be designed to navigate this tension[4]. However, when privacy preferences themselves evolve—perhaps because agents learn through interaction what information has been disclosed, or because social norms regarding acceptable disclosure shift—the protocols designed for static privacy preferences may no longer function effectively.

## The Stability Question: Theoretical Analysis of Dynamic Privacy Preferences

### Fundamental Instabilities from Preference Dynamics

The introduction of dynamic privacy preferences into multi-agent social welfare optimization creates several categories of instability. First, the fundamental assumption underlying social welfare analysis—that preferences exist and remain comparatively stable—is violated when privacy preferences shift over time. This creates what might be termed "preference drift," where the objective function that agents are optimizing continuously changes, potentially causing previously optimal solutions to become suboptimal[40].

The mathematics of optimization under preference drift indicates substantial complications. If the social welfare function \(W(x; \rho_t)\) depends on both the allocation \(x\) and the vector of privacy preferences \(\rho_t\) that varies over time, then an allocation \(x^*_t\) that maximizes welfare at time \(t\) may violate Pareto optimality at time \(t+1\) when \(\rho_{t+1} \neq \rho_t\)[1][3]. This temporal mismatch between solutions and preference states creates ongoing inefficiency, as any static allocation becomes increasingly misaligned with evolving preferences.

Second, dynamic privacy preferences interact poorly with the mechanisms that attempt to stabilize social choice through structure. For instance, Black's median voter theorem—which establishes that when preferences are single-peaked, majority rule produces transitive collective preferences—breaks down when the underlying preference peaks are themselves moving over time[14]. The stability achieved by single-peaked preferences depends on the shapes of preference curves remaining fixed; when privacy preferences evolve, agents' peaks (their most-preferred privacy policies) shift, destroying the single-peaked structure that would otherwise guarantee stability.

### The Arrow Impossibility Problem Amplified by Dynamic Preferences

Arrow's impossibility theorem demonstrates that no aggregation mechanism can satisfy all five of its desiderata simultaneously[13][16]. When preferences are fixed, this impossibility represents a permanent constraint on what mechanisms can achieve. However, when preferences are dynamic, the impossibility becomes even more severe. Consider that at time \(t\), some mechanism \(f\) might satisfy Arrow's axioms perfectly—assuming such a mechanism exists—by choosing a dictatorial rule that reflects one individual's single preference ordering. At time \(t+1\), when that dictator's privacy preferences have changed, this same mechanism violates non-dictatorship with respect to the new preference profile[8][11].

Alternatively, if a mechanism is designed to satisfy non-dictatorship at every time step, then at each transition when preferences change, the mechanism may temporarily violate other axioms as it attempts to adjust its aggregation procedure[8]. Dynamic social choice theory, which extends Arrow's framework to settings where preferences evolve over time, has begun to address these issues[8][11]. Research on dynamic social choice with evolving preferences demonstrates that fairness criteria become increasingly difficult to satisfy when preferences shift[11]. The concept of proportional fairness—ensuring that each agent achieves a certain minimum level of welfare over time—becomes difficult to implement when agents' privacy preferences are continuously changing, as what counts as "fair" allocation of privacy costs shifts over time.

### Path Dependence and Lock-In in Privacy Systems

An additional source of instability emerges from path dependence—the phenomenon where historical choices constrain future options and outcomes[51]. In privacy contexts, past disclosures create lock-in effects. Once personal information has been shared, it cannot be unshared. If an individual consents to data collection because their privacy preferences at time \(t\) permit it, but their preferences shift to \(\rho_{t+1}\) at time \(t+1\) where they would prefer the data had not been collected, the earlier choice cannot be undone[51].

This creates what might be termed "ratchet effects" in privacy systems: the effective privacy constraints that agents face become increasingly binding as systems accumulate personal data. From a social welfare perspective, this means that optimal allocations in early periods create external constraints that limit the feasible set of allocations in later periods. An allocation that was welfare-maximizing at time \(t\) given preferences \(\rho_t\) may be completely infeasible at time \(t+1\) if undoing the data collection is impossible[51].

The interaction between path dependence and dynamic preferences creates particular instability. If privacy preferences are trending toward stricter privacy requirements, accumulated data from earlier periods when preferences were more permissive now creates welfare losses. The optimal solution is not simply to maximize welfare at each point in time; instead, it would require solving a dynamic optimization problem that accounts for how current decisions constrain future feasibility and welfare. Yet doing so requires accurate predictions of future preference changes, which empirical evidence suggests are extremely difficult to achieve[40][42].

## Empirical Evidence on Privacy Preference Stability

### Revealed Privacy Preferences and Instability

While theoretical work on privacy preferences remains limited, research on privacy behavior provides suggestive evidence about preference instability. Studies of revealed privacy preferences find that individuals' privacy choices are often unstable and context-dependent[6][20]. The "privacy paradox"—where people claim to value privacy highly in surveys but reveal substantial personal information in actual behavior—suggests that stated and revealed privacy preferences diverge significantly[6]. This divergence is not simply measurement error; it reflects genuine instability in how individuals assess privacy trade-offs.

Privacy preferences exhibit substantial dependence on framing, context, and recent experiences[6][20]. When individuals receive information about privacy breaches, their revealed preference for privacy protection increases sharply; when privacy concerns recede from media coverage, willingness to disclose increases[6]. This dynamic responsiveness to context and information suggests that privacy preferences should be modeled as responsive to the environment rather than as exogenously fixed parameters.

Longitudinal studies examining how privacy preferences evolve as individuals gain experience with data-sharing systems are limited, but evidence from related domains is instructive. Research on time-varying preferences in economic decision-making, conducted over twelve weeks with repeated measurements, found that approximately 72% of time-inconsistent choices could be explained by time-variance in discounting rates themselves[40]. The implications are sobering: individual preference parameters that theorists often treat as fixed characteristics are themselves varying substantially over short timescales. There is no reason to expect privacy preferences to be more stable than time preferences or risk preferences, which have been documented to fluctuate considerably[40].

### Learning and Preference Adaptation in Multi-Agent Contexts

In multi-agent systems, privacy preferences may evolve through learning as agents observe how information they disclose is used and what consequences follow[32]. Strategic disclosure behavior—the choice of what information to reveal and to whom—depends critically on beliefs about how others will use that information[32]. As agents learn through experience whether their privacy concerns were justified, they adapt their disclosure behavior. This creates feedback loops where the collective behavior of the system influences individual privacy preferences, which in turn influences collective behavior.

Research on strategic disclosure demonstrates that information revelation follows particular patterns: disclosure tends to be extreme and positively biased, with individuals either fully revealing or completely concealing information rather than disclosing partially[32]. When individuals have the opportunity to commit to disclosure policies in advance, disclosure becomes polarized and positively selected regardless of prior beliefs[32]. However, these patterns assume stable beliefs about consequences; when consequences of disclosure are themselves evolving (because the system is learning how information is used), the disclosure patterns may shift substantially.

## Real-World Complications: Privacy Regulation and Heterogeneous Preferences

### Regulatory Coordination and Multi-Agent Enforcement

Recent developments in privacy regulation illustrate how dynamic policy preferences interact with multi-agent coordination problems. The formation of state privacy regulatory consortia, where multiple jurisdictions coordinate enforcement of privacy laws, represents an attempt to aggregate privacy preferences across different political constituencies[21]. Eight state privacy regulators formed a consortium to coordinate enforcement while leveraging technical expertise and sharing enforcement priorities across jurisdictions[21]. The stated goal is to align enforcement around common rights like data access, deletion, and opt-out from sales[21].

However, this coordination effort reveals underlying tensions. While member states' privacy laws differ in scope and terminology, the consortium must decide how to interpret ambiguous provisions and which enforcement priorities to emphasize[21]. As technologies evolve and privacy breaches occur, the enforcement priorities and interpretations of regulatory provisions shift. The optimal coordination mechanism at one moment may become suboptimal as circumstances change, requiring renegotiation of cooperative agreements[21].

### Heterogeneous Privacy Preferences and Fair Compensation

The question of fair compensation for data shared under different privacy levels reveals how heterogeneous privacy preferences complicate welfare optimization[41]. When different individuals have different privacy sensitivities—some willing to share detailed personal information in exchange for modest compensation, others demanding substantial compensation or refusing to share entirely—a central platform face complex mechanism design challenges[41].

Research on fair data valuation under heterogeneous privacy constraints demonstrates that the platform's optimal compensation policy depends on the distribution of privacy sensitivities in the population[41]. Strikingly, the research finds that when privacy sensitivities are sufficiently high, the platform's optimal strategy is to offer no compensation—effectively excluding privacy-sensitive individuals from data-sharing arrangements[41]. Conversely, when privacy sensitivities are low, the platform prefers to collect all data with minimal privacy protections[41]. This creates a form of instability: as privacy preferences in the population shift, the platform's optimal mechanism switches discontinuously between fundamentally different structures.

## Welfare Effects of Dynamic Information Structures

### Information Disclosure and Dynamic Investment Efficiency

The relationship between information disclosure and welfare outcomes becomes more complicated when both information disclosure practices and preferences about information intensity are evolving. Research on how information disclosure affects investment efficiency in dynamic settings shows that better information disclosure improves initial investment decisions but can also affect long-run outcomes as agents adapt to information regimes[56]. When the information environment itself is changing—as preferences regarding appropriate information disclosure shift—agents face moving targets for adaptation.

Dynamic settings with evolving information structures create particular analytical challenges. The standard approach assumes that information about fundamentals is constant while disclosure practices vary; however, when preferences regarding what information should be disclosed are themselves shifting, the fundamental decision environment becomes non-stationary[56]. An agent's optimal policy for information disclosure at time \(t\) depends on expectations about how disclosure practices will evolve, yet these expectations are themselves poorly informed given the unstable nature of preferences.

### Pareto Optimality and Evolving Preferences

Pareto efficiency represents a cornerstone concept in welfare economics, with the fundamental theorems of welfare economics establishing that competitive equilibria under certain conditions are Pareto optimal[29][33]. A situation is Pareto optimal if no alternative allocation can make someone better off without making someone worse off. However, this concept assumes fixed preferences; when preferences are dynamic, the concept requires careful reinterpretation.

An allocation that is Pareto optimal at time \(t\) with respect to preferences \(\rho_t\) may violate Pareto optimality at time \(t+1\) when preferences have shifted to \(\rho_{t+1}\). Consider a concrete example: at time \(t\), given current privacy preferences, individuals collectively prefer a moderate level of data collection with certain safeguards, and no alternative arrangement would benefit anyone without harming someone else. At time \(t+1\), as privacy preferences strengthen in response to awareness of data breaches, the same data collection practice now harms individuals (violating their evolved privacy preferences) while benefiting firms that use their data. The earlier Pareto optimal allocation has become Pareto inefficient given the new preference profile.

This temporal dimension creates a dynamic Pareto problem: what allocation path \(\{x_t\}_{t=0}^{\infty}\) would be Pareto optimal across time, accounting for the fact that preferences themselves evolve? This is a fundamentally harder problem than finding Pareto optima at single time points, because it must balance respecting both historical preferences (which may have motivated earlier choices) and evolved preferences (which may prefer those earlier choices had been different).

## The Instability of Solutions in Multi-Agent Privacy-Welfare Systems

### Convergence Problems in Learning Dynamics

A critical result in game theory demonstrates that perfectly rational agents sometimes face fundamental impossibilities in learning to predict each other's behavior even in simple games[53]. In settings with incomplete information where agents must learn about each other's types, the requirement that agents hold mutually consistent beliefs about beliefs about beliefs (in an infinite regress) may be impossible to satisfy[53]. The probability that any agent's beliefs remain exactly consistent with others' beliefs through an infinite sequence of periods goes to zero, meaning agents will almost surely make suboptimal predictions at some point[53].

These learning impossibilities become more severe when applied to multi-agent systems with dynamic privacy preferences. Not only must agents learn what others prefer and predict their behavior; they must do so in an environment where preferences themselves are shifting. Moreover, privacy preferences involve coordination problems: the benefit an agent derives from privacy protection often depends on whether others also receive privacy protection. This creates circular dependencies where each agent's optimal privacy preference depends on others' privacy preferences, which in turn depend on the first agent's preferences.

### Instability from Circular Dependencies

Circular dependencies create potential instabilities in multi-agent systems with privacy considerations. Consider a simple model where agent \(i\)'s privacy preference depends on the average privacy protection in the system: if most others are well-protected, privacy seems less valuable (as an individual's data is less distinctive and valuable). If most others lack privacy, privacy becomes more valuable as one individual's data becomes more distinctive. This creates a coordination game where multiple equilibrium privacy levels can exist, and the system may oscillate between them as individual preferences respond to collective patterns[28].

More formally, in dynamic potential games—where agents' utilities can be expressed as partial derivatives of a potential function—equilibrium selection becomes crucial when multiple equilibria exist[28]. The existence of multiple equilibria in dynamic settings with evolving preferences means that even if agents could somehow reach an equilibrium at time \(t\), the equilibrium itself may shift as preferences evolve, destabilizing any reached solution[28].

### Non-Existence of Stable Equilibria Under Preference Evolution

The fundamental question motivating this analysis—whether dynamic privacy preferences destabilize optimal solutions—can be addressed theoretically by examining whether stable equilibria can exist. An equilibrium is stable if small perturbations in preferences or beliefs do not cause large changes in the implied optimal allocation. Under dynamic privacy preferences, stability requires that the optimal solution remain approximately optimal through preference changes.

However, several theoretical results suggest that stability cannot be generally guaranteed. First, Arrow's impossibility theorem continues to apply: no aggregation mechanism can satisfy all desiderata at every time point when preferences are dynamic[13][16]. Second, the literature on overlapping generations economies demonstrates that with realistic preference structures, multiple steady states and cycles can exist[49][57]. Even in deterministic environments, small changes in preference parameters can shift the economy between different equilibrium paths[57]. With evolving privacy preferences, such transitions would occur endogenously rather than as exogenous shocks.

Third, empirical evidence on the intransitivity of consumer preferences demonstrates that at any given moment, a significant portion of individuals' preference orderings violate the transitivity axiom fundamental to utility maximization[44]. Approximately 92% of subjects in one study exhibited violations of transitivity, with intransitivity appearing in all major consumer categories[44]. If individual preferences are already unstable and intransitive at static points in time, the addition of dynamic preference evolution creates only further complications.

## Mechanisms for Maintaining Stability Despite Dynamic Preferences

### Constrained Preference Aggregation

While perfect stability is likely impossible under dynamic privacy preferences, mechanisms can be designed to achieve stability within constrained domains. Constrained mechanism design imposes restrictions on the information mechanisms can collect, limiting but not eliminating the instability induced by preference evolution[3][31][34]. These constraints function as safeguards that keep information asymmetries and privacy violations below specified thresholds regardless of how the underlying preference distribution evolves.

The key insight from privacy-constrained mechanism design is that accepting lower welfare performance while guaranteeing maximum privacy loss bounds can create more predictable outcomes[3][31]. Rather than attempting to find globally optimal solutions that shift as preferences change, mechanisms could instead guarantee local stability around baseline welfare levels while maintaining privacy guarantees. This represents a trade-off: accepting lower average welfare in exchange for reduced variance and increased predictability.

### Dynamic Preference Learning and Anticipatory Design

Systems that explicitly model and learn about how privacy preferences evolve might achieve greater stability than systems that treat preferences as fixed[32]. By developing models of preference evolution—understanding what factors drive changes in privacy preferences—designers can build in anticipatory mechanisms that adjust in advance of major preference shifts[32]. This approach recognizes that preference evolution is not purely random but follows patterns based on information, experience, and social dynamics.

However, learning accurate models of preference evolution is itself challenging. The diversity of preference evolution patterns documented in the literature—with individuals exhibiting different combinations of time-inconsistency, non-stationarity, and variance[40]—suggests that one-size-fits-all models will have limited applicability. Moreover, once predictive models are built and widely known, strategic agents may adjust their behavior to game the predictions, potentially creating new instabilities[1].

### Adaptive Governance Structures

Rather than designing mechanisms for fixed preference structures, governance approaches that explicitly adapt to evolving preferences might prove more stable. This would involve mechanisms that periodically reassess the preference landscape and adjust decision-making procedures accordingly. Multi-agent frameworks with specialized reasoning about different aspects of decisions—such as separating private information classification from executor decision-making—appear to reduce but not eliminate instability from evolving privacy preferences[1].

An adaptive approach would acknowledge that perfect optimality at each moment is impossible when preferences are evolving, instead focusing on maintaining consistency with current preferences while minimizing disruption from recent preference shifts. This resembles the "sophisticated" behavior model from time-inconsistency literature, where agents anticipate future preference changes and make decisions that account for predicted future behavior of their future selves[15][23].

## Synthesis: The Destabilization Thesis

### Evidence for Destabilization

Substantial theoretical and empirical evidence supports the conclusion that dynamic evolution of privacy preferences does destabilize optimal solutions of social welfare functions in multi-agent settings. The evidence accumulates across multiple dimensions:

**Theoretical incompleteness:** Arrow's impossibility theorem and extensions demonstrate fundamental impossibilities in aggregating preferences when preferences themselves are evolving. No mechanism can simultaneously satisfy reasonable aggregation axioms at every time step when the underlying preferences are non-stationary[13][16][46].

**Preference instability:** Empirical evidence demonstrates that privacy preferences, like other economic preferences, are unstable, context-dependent, and subject to learning effects. What individuals state they prefer often diverges from revealed preferences, and preferences shift substantially in response to information and experience[6][20][40].

**Path dependence and irreversibility:** Once privacy-relevant data has been collected and shared, disclosure cannot be reversed. This creates lock-in effects where optimal allocations at earlier times constrain feasible allocations at later times, preventing smooth adaptation to evolved preferences[51].

**Multi-agent coordination failures:** When different agents have different privacy preferences that evolve at different rates, coordinating on collectively optimal solutions becomes increasingly difficult. Circular dependencies and coordination game structures can create cycles or multiple equilibria in dynamic settings[28].

**Information structure complexity:** The complexity of distinguishing private from public information in multi-agent systems, even with sophisticated multi-agent frameworks, suggests that privacy classification itself remains unstable and subject to error[1].

### Evidence Against Complete Destabilization

However, the evidence does not support the conclusion that dynamic privacy preferences necessarily create complete chaos or prevent any stable governance structures from emerging. Several counterpoints qualify the destabilization thesis:

**Bounded instability:** While preferences are evolving, they do not evolve infinitely rapidly or completely randomly. Privacy preferences appear to follow certain patterns related to information, experience, and social norms. These patterns, while not perfectly predictable, are not completely unpredictable either[6][20][32].

**Achievable constrained stability:** Mechanisms can be designed to maintain privacy loss within bounds regardless of preference evolution, accepting lower welfare levels in exchange for greater stability and predictability[3][31]. This represents a practical approach to managing instability through constraint rather than eliminating it.

**Sectoral variation:** Evidence suggests that privacy preference evolution differs across different contexts and types of data. Preferences regarding health information, financial information, and behavioral tracking appear to follow different evolutionary patterns[6]. This allows for domain-specific governance approaches rather than requiring a single universal solution.

**Institutional learning:** While individual learning about privacy consequences is imperfect, institutional structures and regulatory bodies can accumulate knowledge about preference evolution patterns and adjust policies accordingly[21]. The formation of privacy regulatory consortia represents an attempt to coordinate governance in response to evolving privacy concerns.

### Qualified Conclusion on Destabilization

The most accurate characterization is that dynamic privacy preferences destabilize optimal solutions of social welfare functions in significant ways, but the extent of destabilization is variable and manageable through appropriate institutional design. Several specific conclusions emerge:

First, no static mechanism can remain optimal across time periods when privacy preferences are evolving. Any mechanism designed to be optimal given preferences \(\rho_t\) will become increasingly suboptimal as preferences shift toward \(\rho_{t+1}\).

Second, the magnitude of destabilization depends on the rate and pattern of preference evolution. Slowly evolving preferences create manageable instability; rapidly shifting preferences create substantial disruption.

Third, preferences regarding privacy do appear to be evolving in contemporary settings, driven by technological change, awareness of privacy violations, and shifting social norms. This suggests that destabilization is not merely theoretical but is actively occurring in real-world systems.

Fourth, accepting suboptimality in exchange for other valuable properties—such as minimum privacy guarantees, reduced variance in allocations, or alignment with current rather than historical preferences—represents a practical approach to managing instability while maintaining social welfare considerations.

## Conclusion

The integration of dynamic privacy preferences into multi-agent social welfare optimization reveals fundamental theoretical challenges that cannot be fully resolved within existing frameworks. While classical social welfare theory assumes preferences are exogenously fixed, empirical evidence demonstrates that privacy preferences are endogenous, unstable, and responsive to context and experience. The dynamic evolution of privacy preferences destabilizes optimal solutions in several ways: it violates the assumptions underlying Arrow's aggregation theorems, creates path dependence that constrains future options, generates circular dependencies in multi-agent coordination, and prevents any static mechanism from remaining optimal across time periods.

However, complete destabilization is neither inevitable nor irreversible through appropriate governance design. Mechanisms that explicitly constrain privacy violations within specified bounds, governance structures that adapt to evolving preferences, and institutions that learn to anticipate preference changes can achieve practical stability while accepting that globally optimal solutions remain elusive. The most promising approach recognizes that perfect welfare maximization under dynamic privacy preferences is impossible and instead focuses on maintaining reasonable welfare performance while respecting evolved privacy preferences and preventing catastrophic preference-system misalignments.

Future research should focus on empirically characterizing the evolution of privacy preferences across different domains, developing models of preference change that can inform mechanism design, and creating adaptive governance institutions that can responsively adjust to preference evolution while maintaining coherent social welfare objectives. The challenge is not to achieve impossible perfection but to design institutions robust enough to accommodate the inevitable instability introduced by evolving preferences while still advancing meaningful social welfare goals.

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Enhancing Contextual Privacy in LLM via Multi-Agent Reasoning', 'url': 'https://aclanthology.org/2025.llmsec-1.9.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Rise of the Dynamic Welfare State - New America', 'url': 'http://newamerica.org/asset-building/policy-papers/the-rise-of-the-dynamic-welfare-state/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Optimal Privacy-Constrained Mechanisms', 'url': 'https://www.aeaweb.org/conference/2020/preliminary/paper/n3fTtfnr'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Argumentation-Based Multi-Agent Decision Making with Privacy ...', 'url': 'https://www.ifaamas.org/Proceedings/aamas2016/pdfs/p1153.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The Evolution of the Welfare State - Diego Huerta', 'url': 'https://www.diegohuertad.com/working_paper/EvolutionWelfareState/The_Evolution_of_Welfare_State.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Revealed Privacy Preferences: Are Privacy Choices Rational?', 'url': 'https://www.robertoweber.com/s/Revealed-Privacy-Preferences-2023-12-09_white_mainappendix.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Social Shaping of Competitive Equilibriums for Resilient Multi-Agent ...', 'url': 'https://arxiv.org/abs/2103.12911'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Dynamic Social Choice with Evolving Preferences - Ariel Procaccia', 'url': 'https://procaccia.info/wp-content/uploads/2020/03/dynamic.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Learning to maximize the social welfare from preference feedback', 'url': 'https://bergerault.fr/work/sycamore-project-report.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Competitive equilibriums and social shaping for multi-agent systems', 'url': 'https://dl.acm.org/doi/10.1016/j.automatica.2022.110663'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Fair and Efficient Social Choice in Dynamic Settings - Rupert Freeman', 'url': 'https://www.rupertfreeman.com/fair_social_choice.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Social Welfare and Profit Maximization from Revealed Preferences', 'url': 'https://par.nsf.gov/servlets/purl/10139636'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Understanding and Solving Societal Problems with Modeling ... - ETH', 'url': 'https://archiv.soms.ethz.ch/teaching/ModelingSpring2014/Lecture_Voting_2014.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] strotz-final.tex 1 - Princeton University', 'url': 'https://www.princeton.edu/~fgul/strotz.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': "[PDF] Arrow's Impossibility Theorem: Two Simple Single-Profile Version", 'url': 'https://economics.brown.edu/sites/default/files/papers/2008-8_paper.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Condorcet paradox - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Condorcet_paradox'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Time-inconsistent preferences and consumer self-control.', 'url': 'https://www.cmu.edu/dietrich/sds/docs/loewenstein/TimeInconsistConSelf.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Optimal Regret Bounds and Convergence to Nash Equilibrium', 'url': 'https://proceedings.mlr.press/v134/hsieh21a/hsieh21a.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The Instability of Preferences - MPG.PuRe', 'url': 'https://pure.mpg.de/rest/items/item_3373427/component/file_3373490/content'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Eight-State Consortium of Privacy Regulators Marks Shift Toward ...', 'url': 'https://www.skadden.com/insights/publications/2025/05/eight-state-consortium-of-privacy-regulators-marks-shift'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Learning in the Presence of Adaptive Behavior William Brown', 'url': 'https://academiccommons.columbia.edu/doi/10.7916/trf9-7g06/download'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] revealed preferences for dynamically inconsistent models', 'url': 'https://eml.berkeley.edu/~fechenique/wp/RevPref_DI.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'New Privacy Risk Insights to Help Navigate Wrongful Collection', 'url': 'https://www.coalitioninc.com/blog/cyber-insurance/new-privacy-risk-insights-to-help-navigate-wrongful-collection'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Imposing equilibrium restrictions in the estimation of dynamic ...', 'url': 'https://onlinelibrary.wiley.com/doi/full/10.3982/QE1735'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The geometry of consumer preference aggregation', 'url': 'https://bcf.princeton.edu/wp-content/uploads/2023/01/Sandomirskiy-Preference-Aggregation.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Arguments against myopic training - LessWrong', 'url': 'https://www.lesswrong.com/posts/GqxuDtZvfgL2bEQ5v/arguments-against-myopic-training'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Dynamic Potential Games with Constraints - arXiv', 'url': 'https://arxiv.org/pdf/1509.01313.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Fundamental theorems of welfare economics - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Fundamental_theorems_of_welfare_economics'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Inefficient Lock-in with Sophisticated and Myopic Players - CORE', 'url': 'https://core.ac.uk/download/pdf/52426874.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Optimal Privacy-Constrained Mechanisms', 'url': 'https://www.aeaweb.org/conference/2020/preliminary/paper/n3fTtfnr'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] (Pro-)Social Learning and Strategic Disclosure - Roland Bénabou', 'url': 'https://rbenabou.scholar.princeton.edu/document/211'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Pareto efficiency - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Pareto_efficiency'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Optimal Privacy-Constrained Mechanisms | Simons Institute', 'url': 'https://simons.berkeley.edu/sites/default/files/docs/11777/slidesprivacymechanism.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Strategic Disclosure in Networks¤ - Theoretical Economics', 'url': 'https://econtheory.org/ojs/index.php/te/article/viewForthcomingFile/6446/43486/1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Understanding Pareto Efficiency in Social Choice Theory - CliffsNotes', 'url': 'https://www.cliffsnotes.com/study-notes/21301862'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The geometry of consumer preference aggregation', 'url': 'https://bcf.princeton.edu/wp-content/uploads/2023/01/Sandomirskiy-Preference-Aggregation.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Coalition Formation for Heterogeneous Federated Learning ... - arXiv', 'url': 'https://arxiv.org/html/2502.05538v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The Welfare Economics of Adaptive Preferences', 'url': 'https://www.coll.mpg.de/51271/2005_11online.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Time-varying Time Preferences* - Economics at UC Davis', 'url': 'https://economics.ucdavis.edu/sites/g/files/dgvnsk13091/files/media/documents/Time-varying%20Time%20Preferences.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Fair Value of Data Under Heterogeneous Privacy Constraints in...', 'url': 'https://openreview.net/forum?id=ynG5Ak7n7Q'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Endogenous Preferences and Welfare Evaluations - SSRN', 'url': 'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=933089'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Social Choice Theory and the Informational Basis Approach', 'url': 'https://www.nuffield.ox.ac.uk/economics/papers/2005/w23/socialchoicetheorykevin.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Empirical evidence for intransitivity in consumer preferences - PMC', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7058914/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Privacy Preferences and Economic Frictions', 'url': 'http://faculty.haas.berkeley.edu/ned/ToRevealOrNotToReveal.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Social Choice Theory - Stanford Encyclopedia of Philosophy', 'url': 'https://plato.stanford.edu/archives/fall2015/entries/social-choice/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Intransitivity of Certain Criteria Used in Welfare Economics - jstor', 'url': 'https://www.jstor.org/stable/2662000'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': "[PDF] Privacy Preserving Signals - Queen's Economics Department", 'url': 'https://www.econ.queensu.ca/sites/econ.queensu.ca/files/Privacy_preserving_signals_1.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] CYCLES AND INDETERMINACY IN OVERLAPPING ...', 'url': 'https://www.ifo.de/DocDL/cesifo1_wp1737.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[DOC] Over the last 50 years, the theory of rational choice has emerged as ...', 'url': 'https://people.duke.edu/~rnau/opb.doc'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Path dependence - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Path_dependence'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Social Choice Theory - Stanford Encyclopedia of Philosophy', 'url': 'https://plato.stanford.edu/archives/fall2015/entries/social-choice/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'On the impossibility of predicting the behavior of rational agents - PMC', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC60142/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Path Dependence - A Foundational Concept for Historical Social ...', 'url': 'https://siepr.stanford.edu/publications/working-paper/path-dependence-foundational-concept-historical-social-science-replaced'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Existence of majority equilibria with non-ordered preferences', 'url': 'https://sheffield.ac.uk/media/108656/download?attachment'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Dynamic Effects of Information Disclosure on Investment Efficiency', 'url': 'https://onlinelibrary.wiley.com/doi/abs/10.1111/1475-679X.12161'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Overlapping generations models, multiplicity of steady states and ...', 'url': 'https://academic.oup.com/oxrep/article/41/2/260/8317912'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'NATURALLY OCCURRING PREFERENCES AND GENERAL ...', 'url': 'https://onlinelibrary.wiley.com/doi/abs/10.1111/iere.12500'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Welfare Effects of Dynamic Matching: An Empirical Analysis', 'url': 'https://academic.oup.com/restud/article-abstract/89/2/1008/6378253?redirectedFrom=fulltext'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Potential Maximization and Stochastic Stability of Spatial Equilibria ...', 'url': 'https://arxiv.org/html/2011.06778v2'}}

## Sources
https://aclanthology.org/2025.llmsec-1.9.pdf
http://newamerica.org/asset-building/policy-papers/the-rise-of-the-dynamic-welfare-state/
https://www.aeaweb.org/conference/2020/preliminary/paper/n3fTtfnr
https://www.ifaamas.org/Proceedings/aamas2016/pdfs/p1153.pdf
https://www.diegohuertad.com/working_paper/EvolutionWelfareState/The_Evolution_of_Welfare_State.pdf
https://www.robertoweber.com/s/Revealed-Privacy-Preferences-2023-12-09_white_mainappendix.pdf
https://arxiv.org/abs/2103.12911
https://procaccia.info/wp-content/uploads/2020/03/dynamic.pdf
https://bergerault.fr/work/sycamore-project-report.pdf
https://dl.acm.org/doi/10.1016/j.automatica.2022.110663
https://www.rupertfreeman.com/fair_social_choice.pdf
https://par.nsf.gov/servlets/purl/10139636
https://archiv.soms.ethz.ch/teaching/ModelingSpring2014/Lecture_Voting_2014.pdf
https://www.princeton.edu/~fgul/strotz.pdf
https://economics.brown.edu/sites/default/files/papers/2008-8_paper.pdf
https://en.wikipedia.org/wiki/Condorcet_paradox
https://www.cmu.edu/dietrich/sds/docs/loewenstein/TimeInconsistConSelf.pdf
https://proceedings.mlr.press/v134/hsieh21a/hsieh21a.pdf
https://pure.mpg.de/rest/items/item_3373427/component/file_3373490/content
https://www.skadden.com/insights/publications/2025/05/eight-state-consortium-of-privacy-regulators-marks-shift
https://academiccommons.columbia.edu/doi/10.7916/trf9-7g06/download
https://eml.berkeley.edu/~fechenique/wp/RevPref_DI.pdf
https://www.coalitioninc.com/blog/cyber-insurance/new-privacy-risk-insights-to-help-navigate-wrongful-collection
https://onlinelibrary.wiley.com/doi/full/10.3982/QE1735
https://bcf.princeton.edu/wp-content/uploads/2023/01/Sandomirskiy-Preference-Aggregation.pdf
https://www.lesswrong.com/posts/GqxuDtZvfgL2bEQ5v/arguments-against-myopic-training
https://arxiv.org/pdf/1509.01313.pdf
https://en.wikipedia.org/wiki/Fundamental_theorems_of_welfare_economics
https://core.ac.uk/download/pdf/52426874.pdf
https://www.aeaweb.org/conference/2020/preliminary/paper/n3fTtfnr
https://rbenabou.scholar.princeton.edu/document/211
https://en.wikipedia.org/wiki/Pareto_efficiency
https://simons.berkeley.edu/sites/default/files/docs/11777/slidesprivacymechanism.pdf
https://econtheory.org/ojs/index.php/te/article/viewForthcomingFile/6446/43486/1
https://www.cliffsnotes.com/study-notes/21301862
https://bcf.princeton.edu/wp-content/uploads/2023/01/Sandomirskiy-Preference-Aggregation.pdf
https://arxiv.org/html/2502.05538v1
https://www.coll.mpg.de/51271/2005_11online.pdf
https://economics.ucdavis.edu/sites/g/files/dgvnsk13091/files/media/documents/Time-varying%20Time%20Preferences.pdf
https://openreview.net/forum?id=ynG5Ak7n7Q
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=933089
https://www.nuffield.ox.ac.uk/economics/papers/2005/w23/socialchoicetheorykevin.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC7058914/
http://faculty.haas.berkeley.edu/ned/ToRevealOrNotToReveal.pdf
https://plato.stanford.edu/archives/fall2015/entries/social-choice/
https://www.jstor.org/stable/2662000
https://www.econ.queensu.ca/sites/econ.queensu.ca/files/Privacy_preserving_signals_1.pdf
https://www.ifo.de/DocDL/cesifo1_wp1737.pdf
https://people.duke.edu/~rnau/opb.doc
https://en.wikipedia.org/wiki/Path_dependence
https://plato.stanford.edu/archives/fall2015/entries/social-choice/
https://pmc.ncbi.nlm.nih.gov/articles/PMC60142/
https://siepr.stanford.edu/publications/working-paper/path-dependence-foundational-concept-historical-social-science-replaced
https://sheffield.ac.uk/media/108656/download?attachment
https://onlinelibrary.wiley.com/doi/abs/10.1111/1475-679X.12161
https://academic.oup.com/oxrep/article/41/2/260/8317912
https://onlinelibrary.wiley.com/doi/abs/10.1111/iere.12500
https://academic.oup.com/restud/article-abstract/89/2/1008/6378253?redirectedFrom=fulltext
https://arxiv.org/html/2011.06778v2