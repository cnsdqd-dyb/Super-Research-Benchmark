# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** e7c79893 | **Time:** 292.72s | **Cost:** $0.09284
--------------------------------------------------------------------------------

# The Dynamic Evolution of Transport Mode Transition Matrices: Implications for Overall System Efficiency

## A Comprehensive Research Analysis

---

## Abstract

The dynamic evolution of transport mode transition matrices represents a critical area of inquiry in contemporary urban transportation research, with profound implications for system-wide efficiency, sustainability, and policy formulation. This report examines the multifaceted impacts of how travelers shift between transportation modes over time, analyzing the underlying mechanisms that govern these transitions and their cascading effects on overall transportation network performance. Drawing upon recent advances in evolutionary game theory, machine learning classification methods, and system dynamics modeling, this analysis synthesizes current understanding of transport mode transition dynamics and their relationship to urban mobility efficiency. The findings reveal that transition matrices serve as powerful analytical tools for capturing the stochastic and adaptive nature of traveler behavior, enabling more accurate predictions of modal distribution patterns and informing evidence-based policy interventions. The report concludes with strategic recommendations for leveraging transition matrix analysis to enhance transportation system efficiency in the context of emerging shared mobility paradigms and smart city initiatives.

---

## 1. Introduction

### 1.1 Background and Context

The study of travel mode choice behavior constitutes a central pillar of urban transportation management, fundamentally shaping the structure of urban mobility and informing the development of effective traffic management policies [1]. As cities worldwide grapple with the challenges of rapid urban economic growth, accelerated urbanization, and the resulting surge in transportation demand, understanding how individuals select and transition between different travel modes has become increasingly paramount. The expansion in the diversity of available travel modes—including traditional public transit, private automobiles, shared mobility services, cycling infrastructure, and emerging autonomous vehicle technologies—has created a complex decision landscape that demands sophisticated analytical frameworks.

Transport mode transition matrices have emerged as essential mathematical constructs for capturing and analyzing the probabilistic relationships between different travel modes across temporal intervals. These matrices encode the likelihood that travelers will switch from one mode to another during a specified period, providing a snapshot of the dynamic behavioral patterns that underlie aggregate modal distribution. The evolution of these matrices over time reflects the complex interplay of individual preferences, policy interventions, technological innovations, and contextual factors that collectively shape urban mobility patterns.

### 1.2 Research Motivation

Traditional approaches to transport demand modeling, such as the four-step travel demand model that has served as the conventional tool for forecasting demand and evaluating transportation system performance since the 1950s, have relied heavily on aggregate cross-sectional data and static assumptions about traveler behavior [2]. While these models have proven valuable for large-scale infrastructure planning, they increasingly struggle to capture the dynamic, adaptive nature of mode choice decisions in contemporary urban environments characterized by rapidly evolving mobility options and shifting user preferences.

The recognition that individual behavior and urban development simultaneously affect transportation system performance—influencing traffic volumes, speeds, congestion levels, and environmental impacts—has motivated a shift toward more disaggregated, behaviorally-grounded modeling approaches [3]. Transport mode transition matrices, when properly specified and estimated, offer a mechanism for representing the stochastic and evolutionary aspects of mode choice behavior, enabling transportation planners to move beyond static equilibrium assumptions toward dynamic representations of system behavior.

### 1.3 Research Objectives

This report aims to provide a comprehensive analysis of how the dynamic evolution of transport mode transition matrices impacts overall system efficiency. Specifically, the analysis addresses the following interconnected questions:

First, what theoretical and methodological foundations underpin the use of transition matrices in transportation analysis, and how do these frameworks capture the essential dynamics of mode choice behavior? Second, what mechanisms drive the evolution of transition matrices over time, and how do these dynamics manifest in aggregate system-level outcomes? Third, what implications do transition matrix dynamics hold for transportation system efficiency, and how can this understanding inform policy and planning interventions? Fourth, how do emerging technologies and shared mobility paradigms reshape the landscape of mode transitions, and what new challenges and opportunities do they present for system optimization?

---

## 2. Theoretical Foundations of Transport Mode Transition Analysis

### 2.1 Mathematical Framework for Transition Matrices

Transport mode transition matrices operate within a rigorous mathematical framework that enables the quantification of mode switching probabilities across a transportation network. Consider a multimodal directed graph representation $G = (V, E, M, T)$, where $V = \{v_1, \ldots, v_n\}$ represents the set of nodes, $E = \{e_1, \ldots, e_n\}$ is the set of arcs, and $M = \{m_1, \ldots, m_l\}$ denotes the set of transport modes including rail, bus, walking, and other modalities [4]. The travel time $T = \{t_{k,i,j}(a_i)\}$ from node $v_i$ at time $a_i$ to node $v_j$ via arc $(e_i, e_j) \in E$ introduces temporal dynamics into the network representation.

Within this framework, a transition matrix $P$ can be defined as a square matrix where element $p_{ij}$ represents the probability of transitioning from mode $i$ to mode $j$ over a specified time interval. The matrix satisfies the stochastic constraint that each row sums to unity:

$$\sum_{j=1}^{m} p_{ij} = 1 \quad \forall i \in \{1, \ldots, m\}$$

where $m$ denotes the number of transport modes under consideration. This mathematical structure enables the modeling of mode choice as a Markov process, where the probability of selecting a particular mode at time $t+1$ depends probabilistically on the mode selected at time $t$.

The time-varying nature of urban multimodal transportation networks necessitates that transition matrices adhere to the first-in–first-out (FIFO) principle, ensuring that the temporal dynamics of mode transitions remain consistent with the physical constraints of network operation [4]. To ensure computational efficiency while maintaining analytical rigor, the time interval $[a_0, b_0]$ can be divided into $N$ time segments, denoted as $\Gamma_k = (\zeta_k, \xi_k)$ for $k = 1, 2, \ldots, N$, where $\zeta_1 = a_0$ and $\xi_N = b_0$. Within each time segment, the vehicle and traveler dynamics can be approximated as stationary, enabling the estimation of time-homogeneous transition probabilities.

### 2.2 Evolutionary Game-Theoretic Foundations

The application of evolutionary game theory to transport mode choice analysis provides a powerful framework for understanding how traveler populations adapt their mode selection strategies over time in response to changing conditions and strategic interactions [1]. Unlike classical game theory, which assumes rational, fully informed actors achieving Nash equilibrium, evolutionary game theory focuses on the dynamic adjustment processes through which population-level behavioral patterns emerge and stabilize.

In the evolutionary game framework of mode choice, travelers are conceptualized as players who receive payoffs that depend not only on their own mode choice but also on the aggregate choices of other travelers in the population. The payoff structure captures the various costs and benefits associated with different transport modes, including monetary costs, travel time, comfort, reliability, and environmental considerations. Travelers who achieve higher payoffs through their mode choices are more likely to have their strategies replicated through social learning or imitation processes, leading to the evolutionary dynamics that govern mode distribution over time.

The replicator dynamics, a cornerstone of evolutionary game theory, describe how the proportion of travelers using each mode evolves over time:

$$\dot{x}_i = x_i (u_i(x) - \bar{u}(x))$$

where $x_i$ represents the proportion of travelers using mode $i$, $u_i(x)$ denotes the payoff to mode $i$ when the population distribution is $x$, and $\bar{u}(x)$ represents the average payoff across all modes. This differential equation captures the intuitive notion that modes with above-average payoffs will increase their market share, while modes with below-average payoffs will decline.

The equilibrium analysis of evolutionary game models reveals the stable mode distributions toward which populations tend to converge under different cost and benefit structures [1]. These equilibrium points, characterized by their stability properties, provide insights into the long-term outcomes of mode choice dynamics and the conditions under which particular modal distributions become self-reinforcing.

### 2.3 Machine Learning Approaches to Transition Modeling

The integration of machine learning techniques into transport mode classification and transition analysis has opened new avenues for capturing the complex, high-dimensional relationships that govern traveler behavior [5]. Modern machine learning approaches offer sophisticated capabilities for pattern recognition, classification, and prediction that complement traditional econometric methods in transportation analysis.

Several machine learning paradigms have been applied to transport mode classification and transition modeling with notable success. The Naive Bayes Model, a supervised machine learning algorithm for classification problems, provides a probabilistic approach to mode prediction based on observed characteristics [5]. Despite its simplifying assumption of feature independence, the Naive Bayes classifier often performs remarkably well in practice, offering interpretable outputs and computational efficiency for large-scale applications.

The Generalized Linear Model (GLM) extends traditional linear regression to accommodate non-normal response distributions, providing a flexible framework for modeling mode choice probabilities under various distributional assumptions [5]. GLMs enable the specification of link functions that transform the linear predictor to the probability scale, accommodating binary, multinomial, and count data commonly encountered in transportation analysis.

Logistic regression, a special case of GLMs designed for categorical outcomes, has proven particularly valuable for modeling binary mode choices and has been extended to handle multinomial outcomes encompassing more than two categories [5]. The flexibility of logistic regression in incorporating continuous and categorical predictors, combined with its well-understood statistical properties, makes it a workhorse method for mode choice analysis.

More advanced methods, including ensemble approaches like Random Forest algorithms, have demonstrated superior performance in transport mode classification tasks [6]. The multilevel method based on Transition State Matrices (TSMs) and Random Forest has been shown to maintain spatial independence while achieving higher accuracy compared to baseline approaches, addressing the critical challenge of ensuring classification methods remain accurate regardless of geographic variations.

---

## 3. Mechanisms of Dynamic Evolution in Transition Matrices

### 3.1 Individual Behavioral Adaptation

The dynamic evolution of transport mode transition matrices fundamentally reflects the adaptive behavior of individual travelers responding to changing conditions, experiences, and information. Travelers continuously update their mental models of the transportation system based on direct experience, observations of others, and exposure to information about alternative modes, leading to gradual shifts in the probabilities governing mode transitions.

The Decision Field Theory (DFT) approach to travel mode choice provides a psychologically-grounded account of the deliberative processes that underlie mode transitions [7]. Unlike rational choice models that assume instantaneous utility maximization, DFT conceptualizes mode choice as a dynamic accumulation of evidence over time, where travelers mentally simulate the outcomes associated with different options before reaching a decision threshold. The DFT-based choice probability exhibits distinctive temporal dynamics, with the probability of selecting a particular mode evolving as deliberation proceeds and evidence accumulates.

Computational analyses of DFT-based mode choice have revealed that the dynamic evolution of choice probabilities is influenced by numerous factors, including trip distance, departure time, income levels, traffic flow conditions, value of time (VOT), and value of cost (VOC) [7]. These factors shape the deliberative process by affecting the rate at which evidence accumulates for different options and the thresholds at which decisions are reached, thereby influencing the ultimate mode transition outcomes.

The self-feedback mechanism in deliberative processes, characterized by coefficients such as $\eta_{\eta\eta}$ set to values like 0.9115 based on empirical calibration, captures the tendency for prior preferences to influence subsequent deliberation [7]. This mechanism contributes to path dependence in mode choice, where historical patterns of mode use affect current transition probabilities and create inertia in modal distribution.

### 3.2 System-Level Feedback Dynamics

Beyond individual adaptation, the evolution of transport mode transition matrices is shaped by system-level feedback dynamics that link individual choices to aggregate outcomes. These feedbacks create complex interdependencies where the collective behavior of travelers simultaneously affects and is affected by the performance characteristics of the transportation system.

The relationship between mode choice and traffic conditions exemplifies these feedback dynamics. When a significant proportion of travelers shift from private automobiles to public transit, the resulting reduction in traffic congestion improves the reliability and speed of both transit and road-based modes, potentially reinforcing the initial mode shift through improved service quality. Conversely, increased automobile usage exacerbates congestion, degrading the attractiveness of road-based modes and potentially triggering mode shifts toward alternatives.

System dynamics modeling has proven valuable for capturing these feedback relationships and simulating the long-term evolution of modal distribution [3]. By representing the stocks of travelers using different modes, the flows between modes, and the feedback loops that connect mode shares to system performance, system dynamics models can generate insights into the temporal dynamics of mode transitions and their implications for transportation system efficiency.

Research applying system dynamics to urban mobility policy evaluation has highlighted the challenge of attracting users to public transport in automobile-dependent societies [3]. Despite improvements in urban conditions and reductions in car ownership necessity provided by urban mobility policy instruments, the transition dynamics often exhibit resistance to change, reflecting the multiple reinforcing feedbacks that maintain automobile dominance.

### 3.3 Exogenous Shocks and Policy Interventions

The evolution of transport mode transition matrices is periodically disrupted by exogenous shocks and policy interventions that abruptly alter the cost-benefit structures underlying mode choice decisions. Understanding how these disruptions propagate through the transition matrix and affect long-term modal distribution is essential for effective transportation planning and policy design.

Transportation policy instruments can be categorized into cost-based interventions, such as congestion pricing, fuel taxes, and parking fees, and accessibility-based interventions, including improvements to public transit service, cycling infrastructure, and walkability enhancements [3]. Each type of intervention affects the transition matrix by altering the relative attractiveness of different modes, potentially shifting the equilibrium distribution toward more sustainable options.

The effectiveness of policy interventions in reshaping transition dynamics depends critically on the timing and sequencing of measures. Evidence suggests that local authorities often delay action until problems become severe, at which point reversing established patterns of automobile dependence becomes extremely difficult [8]. Once car-use becomes the dominant mode of transport, the transition matrix develops strong inertia reflecting the accumulated investments in automobile-related infrastructure, habits, and social norms.

The introduction of new mobility services, such as ride-sharing and car-sharing platforms, represents a particularly significant class of exogenous shocks that can rapidly reshape transition dynamics [1]. These services alter the cost structure of mode choices by providing alternatives that combine elements of private automobile use with the shared economy, potentially triggering complex cascades of mode switching as travelers experiment with and adopt new options.

---

## 4. Impact on System Efficiency

### 4.1 Network Performance Implications

The dynamic evolution of transport mode transition matrices exerts profound effects on transportation network performance through multiple interconnected pathways. The distribution of travelers across modes determines the load on different network elements, influencing congestion levels, travel times, reliability, and the overall efficiency of resource utilization.

When transition matrices shift toward modes with higher passenger capacity per unit of road space, such as public transit, the transportation network can accommodate larger travel volumes without proportional increases in congestion. This relationship between modal distribution and network capacity utilization has been quantified through studies of multimodal transportation systems, which have demonstrated that increasing the share of multimodal trips—trips consisting of two or more travel modes—contributes to sustainable urban transportation and high levels of urban mobility [7].

The efficiency implications of transition matrix dynamics extend beyond simple capacity considerations to encompass the reliability and robustness of network performance. Diversified modal distribution reduces dependence on any single network element, enhancing system resilience to disruptions and failures. When travelers are distributed across multiple modes, localized congestion or service disruptions have smaller aggregate impacts, as affected travelers can more readily switch to alternatives.

### 4.2 Environmental and Social Efficiency

The evolution of transport mode transition matrices carries significant implications for environmental efficiency, as different modes exhibit substantially different per-passenger emissions profiles and energy consumption characteristics. Shifts from private automobile use toward public transit, cycling, and walking can dramatically reduce the environmental footprint of urban mobility, contributing to air quality improvements and climate change mitigation.

Research on future transportation scenarios has explored pathways toward sustainable mobility, considering the interacting effects of autonomous vehicles, shared mobility, and electrification [9]. The analysis suggests that by 2030, most likely pathways involve incremental advances, including a slow shift toward self-driving, electric, and shared vehicle use. However, the ultimate environmental outcomes depend critically on how transition dynamics evolve in response to these technological changes and accompanying policy interventions.

Social efficiency considerations encompass the accessibility and equity implications of mode transition patterns. Transportation systems that effectively serve diverse population segments, including low-income households, elderly individuals, and persons with disabilities, require modal distributions that provide viable options for users with varying capabilities and constraints. Transition matrices that concentrate travel demand in automobile-dependent patterns can exacerbate social exclusion for those unable to access or afford private vehicles.

### 4.3 Economic Efficiency Dimensions

The economic efficiency implications of transport mode transition dynamics operate through multiple channels, including direct user costs, infrastructure investment requirements, and broader productivity effects. Understanding these dimensions is essential for comprehensive assessment of transition matrix impacts on system efficiency.

From the perspective of individual travelers, the economic efficiency of mode choices depends on the full costs of travel, including monetary expenditures, time costs, and the opportunity costs of vehicle ownership. Transition matrices that shift travel toward modes with lower total costs enhance individual economic efficiency, though the distribution of these benefits across different population segments must be considered.

At the system level, the efficiency of infrastructure investment depends on the alignment between modal distribution and network capacity. When transition dynamics concentrate travel demand on modes requiring extensive road infrastructure, the resulting investment requirements can strain public budgets and divert resources from other public goods. Conversely, transitions toward modes with lower infrastructure requirements per passenger, such as high-capacity transit, can enhance the fiscal efficiency of transportation systems.

The integration of artificial intelligence and machine learning into transportation optimization has created new opportunities for enhancing economic efficiency through dynamic pricing, real-time resource allocation, and predictive demand management [10]. AI-driven platforms can facilitate better coordination among various stakeholders, including government agencies, private operators, and users, enabling more efficient resource allocation and service delivery.

---

## 5. Emerging Paradigms and Future Directions

### 5.1 Shared Mobility and Transition Dynamics

The emergence of shared mobility services has fundamentally altered the landscape of transport mode choice, introducing new transition possibilities and reshaping the dynamics of mode switching behavior. Car-sharing, ride-hailing, and micro-mobility services have expanded the option set available to travelers, creating new pathways between modes and altering the competitive relationships among existing options.

Evolutionary game-theoretic analysis of shared mobility considerations has revealed complex interactions between shared car usage, public transit, and private automobile travel [1]. The cost structures of shared mobility services, which typically involve per-trip charges without the fixed costs of vehicle ownership, create distinctive incentive patterns that can trigger mode transitions under different trip contexts. For short, infrequent trips, shared mobility may offer cost advantages over ownership; for frequent, long-distance travel, the economics may favor continued automobile dependence.

The integration of shared mobility into multimodal trip chains represents a particularly important aspect of transition dynamics. Park-and-ride (P&R) facilities, which combine automobile access with transit for longer-distance travel, exemplify the multimodal transitions that are becoming increasingly common in contemporary urban mobility [7]. The choice probabilities for such combined modes depend on the full trip context, including the availability and cost of parking, transit service quality, and the reliability of connections between modes.

### 5.2 Artificial Intelligence and Real-Time Adaptation

The application of artificial intelligence to transportation systems has enabled new forms of dynamic adaptation in mode choice and transition behavior. Reinforcement learning algorithms, which enable agents to learn optimal decision-making strategies through interaction with their environment, have shown particular promise for real-time traffic management and mode optimization [10].

Smart city applications of reinforcement learning include real-time traffic management systems that optimize traffic light timings based on current conditions, and autonomous vehicle management systems that learn to navigate effectively and safely [10]. Q-learning, deep Q-networks (DQN), and policy gradient approaches represent commonly used algorithms that can adapt to changing conditions and learn from experience.

The convergence of stream processing and machine learning capabilities has enabled a transition from descriptive to predictive analytics in transportation systems [11]. Integrated machine learning-streaming architectures can achieve inference latencies below 15 milliseconds while maintaining throughput exceeding 8,000 events per second, enabling sophisticated applications including real-time mode recommendation, dynamic pricing optimization, and automated anomaly detection.

### 5.3 Benchmarking and Standardization Challenges

The development of robust transition matrix models faces significant challenges related to data standardization, methodological consistency, and cross-context comparability. A key challenge in transport mode classification and transition analysis is ensuring the comparability of different methods across various contexts, complicated by the insufficient use of existing standardized benchmarks [6].

The need for structured testing frameworks and consistent datasets for evaluating transition models has motivated efforts to develop improved benchmarks that address spatial independence and ensure robustness for real-world deployment [6]. Spatial independence is crucial because it ensures that classification and transition models remain accurate regardless of geographic variations, enabling consistent evaluation across regions and contexts.

The collection of high-quality data for developing and validating transition models requires sophisticated monitoring approaches that extend beyond simple platform metrics to include application-specific key performance indicators [11]. Modern data collection strategies increasingly leverage mobile devices, connected vehicles, and smart infrastructure to capture the detailed trajectory data necessary for understanding mode transitions in fine-grained detail.

---

## 6. Policy Implications and Strategic Recommendations

### 6.1 Leveraging Transition Matrix Insights for Planning

The analysis of transport mode transition matrices provides valuable insights for transportation planning and policy design. By understanding the probabilities and drivers of mode switching, planners can develop targeted interventions that address specific transition pathways and leverage existing behavioral dynamics.

The identification of influential drivers associated with citizens' perception of comfort and quality of living in smart cities enables policy prioritization based on factors that most strongly affect mode choice [5]. Machine learning approaches can reveal non-obvious relationships between contextual factors and transition probabilities, informing the design of interventions that target the most impactful leverage points in the transportation system.

The temporal dynamics of transition matrices suggest that policy interventions should be designed with attention to timing and sequencing. Early interventions that shape transition dynamics before strong path dependencies develop may be more effective than belated attempts to reverse entrenched patterns. Planners should monitor transition matrix evolution to identify windows of opportunity for policy influence.

### 6.2 Integrating Multiple Modeling Approaches

The complexity of transport mode transition dynamics argues for the integration of multiple modeling approaches, combining the strengths of evolutionary game theory, machine learning, system dynamics, and network optimization methods. Each approach offers distinctive insights into different aspects of transition behavior, and their synthesis can provide more comprehensive understanding than any single method alone.

Evolutionary game theory provides a foundation for understanding the strategic interactions and population-level dynamics that shape mode distribution, while machine learning methods offer powerful capabilities for pattern recognition and prediction from complex, high-dimensional data [5]. System dynamics modeling captures the feedback relationships and temporal evolution of modal distribution, and network optimization methods enable the assessment of efficiency implications for specific transition scenarios.

The integration of activity-based travel demand models with operational land-use transport interaction (LUTI) models represents an important frontier in transportation modeling [2]. Activity-based models capture the underlying travel generation and scheduling decisions that give rise to mode choice, while LUTI models represent the spatial allocation of activities and their transportation implications. Bridging these frameworks can provide more complete representations of transition dynamics and their system-level consequences.

### 6.3 Addressing Uncertainty and Robustness

Transportation planning under uncertainty requires that transition matrix analysis incorporate explicit treatment of stochastic variation and associated uncertainties in model outputs. The propagation of uncertainty over time and across different model frameworks represents a significant methodological challenge that requires ongoing research attention [2].

Robust decision-making approaches can help address uncertainty in transition dynamics by identifying strategies that perform well across a range of plausible future scenarios rather than optimizing for a single forecast. Scenario analysis, sensitivity testing, and adaptive pathway planning represent tools for managing uncertainty in the context of mode transition dynamics.

The development of real-time behavioral adaptation models and machine learning-based travel demand predictions represents a promising direction for improving the responsiveness of transportation systems to changing conditions [1]. By continuously updating transition matrix estimates based on observed behavior, transportation systems can adapt their operations and information provision to support efficient mode transitions.

---

## 7. Conclusion

The dynamic evolution of transport mode transition matrices exerts profound and multifaceted impacts on overall transportation system efficiency. Through the lens of evolutionary game theory, machine learning classification, and system dynamics modeling, this analysis has revealed the complex mechanisms through which individual mode choices aggregate into system-level outcomes, and how these dynamics shape network performance, environmental sustainability, and economic efficiency.

Transition matrices serve as essential analytical constructs for capturing the stochastic and adaptive nature of traveler behavior, enabling transportation planners to move beyond static equilibrium assumptions toward dynamic representations of system behavior. The evolution of these matrices over time reflects the interplay of individual adaptation, system-level feedbacks, and exogenous shocks that collectively determine the trajectory of modal distribution.

The findings of this analysis underscore the importance of developing sophisticated, behaviorally-grounded models of mode transition for effective transportation planning. As cities confront the challenges of rapid urbanization, technological change, and sustainability imperatives, the ability to understand and influence transition dynamics becomes increasingly critical. The integration of artificial intelligence, shared mobility services, and real-time data collection creates both opportunities and challenges for managing transition dynamics toward more efficient, sustainable urban mobility outcomes.

Looking forward, continued research into the mechanisms of mode transition, the development of robust benchmarking frameworks, and the integration of multiple modeling approaches will be essential for advancing the field. By leveraging these insights, transportation planners and policymakers can develop interventions that effectively shape transition dynamics, enhance system efficiency, and contribute to the creation of more sustainable and livable urban environments.

---

## References

[1] Liu, T., and Zhao, F. (2025). Dynamic Evolution of Travel Mode Choice: A Game-Theoretic Analysis with Shared Mobility Considerations. *Economic Computation and Economic Cybernetics Studies and Research*, 59(3).

[2] Wang, Y., et al. (2011). Integration of activity-based travel demand models with land-use models for operational LUTI modeling. *Journal of Transport and Land Use*.

[3] da Silva, et al. (2021). The dynamics of individual behaviour of mode choice: The impacts of selected Brazilian urban mobility policy instruments. *Case Studies on Transport Policy*, 9(3), 1324-1335.

[4] MDPI Authors. (2025). Multimodal directed graph modeling with time dependency. *Future Transportation*, 7(2).

[5] Frontiers Authors. (2025). Machine learning models for predicting HDI-city level and determining influential drivers for citizens' perception of comfort. *Frontiers in Sustainable Cities*.

[6] ScienceDirect Authors. (2024). Transition State Matrices and Random Forest for transport mode classification. *Journal of Transport Geography*.

[7] Stanford Authors. Travel Modal Choice Analysis for Traffic Corridors Based on Decision-theoretic Approaches. *Stanford University Research*.

[8] Cavoli, C. (2025). Mapping minibuses in Maputo and Nairobi: engaging paratransit in transportation planning. *Transport Reviews*.

[9] ScienceDirect Authors. (2021). Autonomous vehicles, shared mobility, and electrification pathways. *Energy for Sustainable Development*.

[10] Frontiers Authors. (2024). Machine learning in advancing sustainable smart cities. *Frontiers in Sustainable Cities*.

[11] World Journal of Advanced Research and Reviews Authors. (2025). Machine learning integration for predictive stream processing. *WJARR*.

## Annotations


## Sources
[1] http://helper.ipam.ucla.edu/publications/fis2024/fis2024_19823.pdf
[2] http://www.joanwalker.com/uploads/3/6/9/5/3695513/el_zarwi_vij_and_walker__2017_.pdf
[3] https://amankhullar.github.io/data/Report.pdf
[4] https://arxiv.org/html/2509.05777v1
[5] https://courses.physics.ucsd.edu/2020/Fall/physics210b/Pomeau%20and%20Resibois.pdf
[6] https://cs.stanford.edu/~jiaxuan/files/South.pdf
[7] https://discovery.ucl.ac.uk/id/eprint/10136887/1/Accelerating%20sustainable%20mobility%20CAVOLI.pdf
[8] https://ecocyb.ase.ro/nr2025_3/5_TingLiu_FangxiaZhao.pdf
[9] https://journalwjarr.com/sites/default/files/fulltext_pdf/WJARR-2025-1746.pdf
[10] https://link.springer.com/article/10.1007/s44327-025-00138-3
[11] https://supernet.isenberg.umass.edu/articles/eolss.pdf
[12] https://thesai.org/Downloads/Volume14No9/Paper_104-Machine_Learning_for_Smart_Cities.pdf
[13] https://uda.reapress.com/journal/article/view/38
[14] https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf
[15] https://www.cambridge.org/core/journals/european-journal-of-risk-regulation/article/understanding-the-policy-integration-challenges-of-sustainable-urban-mobility-in-the-context-of-rapid-decarbonisation/DFDBEB732A253DC820738985A92CCEF5
[16] https://www.cs.cmu.edu/~ninamf/LGO10/wm-minimax.pdf
[17] https://www.frontiersin.org/journals/sustainable-cities/articles/10.3389/frsc.2024.1449404/full
[18] https://www.frontiersin.org/journals/sustainable-cities/articles/10.3389/frsc.2025.1400917/full
[19] https://www.jtlu.org/index.php/jtlu/article/view/806/1375
[20] https://www.mdpi.com/2305-6290/8/4/111
[21] https://www.mdpi.com/2624-8921/7/2/43
[22] https://www.mdpi.com/2673-2688/6/3/46
[23] https://www.oecd.org/content/dam/oecd/en/publications/reports/2020/06/decarbonising-urban-mobility-with-land-use-and-transport-policies_f1dc56a5/095848a3-en.pdf
[24] https://www.sciencedirect.com/science/article/abs/pii/S2210670724001975
[25] https://www.sciencedirect.com/science/article/abs/pii/S2213624X21001115
[26] https://www.sciencedirect.com/science/article/pii/S2210670721003139
[27] https://www.sciencedirect.com/science/article/pii/S2214367X24001923
[28] https://www.sciencedirect.com/science/article/pii/S2352484725003014
[29] https://www.transit.dot.gov/sites/fta.dot.gov/files/docs/research-innovation/147791/mobility-performance-metrics-integrated-mobility-and-beyond-fta-report-no-0152.pdf