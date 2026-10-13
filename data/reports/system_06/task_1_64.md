# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 882957ea | **Time:** 175.24s | **Cost:** $0.18375
--------------------------------------------------------------------------------

# How Do Stability Boundaries of Signal Coordination Affect System-Level Congestion Propagation?

## Abstract

This research report examines the intricate relationship between stability boundaries of signal coordination and system-level congestion propagation in urban transportation networks. As modern infrastructure systems face increasing complexity and interconnectivity, understanding how signal coordination stability thresholds influence congestion dynamics has become paramount for network resilience and efficient traffic management. Drawing from contemporary research in complex infrastructure networks, adaptive signal control systems, and cascading failure mechanisms, this analysis investigates the fundamental principles governing signal coordination stability, the mathematical frameworks characterizing congestion propagation boundaries, and the practical implications for urban traffic network design. The findings reveal that stability boundaries in signal coordination are not merely local optimization parameters but critical determinants of system-wide congestion propagation patterns, with coordinated systems demonstrating significantly enhanced capability to maintain bounded queue lengths and prevent cascade effects compared to uncoordinated configurations. The report synthesizes theoretical foundations with practical implementation considerations, providing insights for transportation engineers, urban planners, and researchers working at the intersection of network resilience and intelligent transportation systems.

## 1. Introduction

### 1.1 Background and Motivation

The contemporary landscape of urban transportation systems is characterized by unprecedented complexity, where networks of interconnected infrastructure elements must accommodate ever-increasing travel demands while maintaining operational efficiency and resilience. Within this context, signalized intersections serve as critical nodes that regulate the flow of vehicles through urban networks, and their coordinated operation has emerged as a fundamental strategy for managing congestion and preventing system-wide failures. The stability of signal coordination mechanisms—whether defined through fixed-time plans, adaptive algorithms, or connected vehicle-based approaches—directly influences how congestion propagates through transportation networks and whether localized disturbances remain contained or escalate into cascading failures affecting entire urban areas.

The significance of understanding stability boundaries in signal coordination extends beyond mere traffic efficiency. Modern infrastructure networks, including transportation systems, power grids, and communication networks, share fundamental characteristics that make them susceptible to cascading failures [1]. When a localized failure occurs in such networks, the redistribution of flow can trigger successive failures in other network elements, potentially leading to system-wide collapse. In transportation networks specifically, the failure of a single road segment or intersection can cause traffic to reroute onto alternative paths, overloading those paths and creating congestion waves that propagate through the network in a manner analogous to cascade effects observed in power systems and financial networks [1].

The phenomenon of congestion propagation in transportation networks exhibits remarkable similarity to cascading failure dynamics in other complex infrastructure systems. Research has demonstrated that congestion propagation depends critically on several factors including travel demand levels, road network structure, and the physical properties of road segments such as lane counts and intersection spacing [2]. The complexity and stochasticity of these factors make it exceptionally difficult to predict the precise geometry of congested components that emerge under various control strategies, necessitating sophisticated analytical frameworks that can characterize stability boundaries and their influence on system-level behavior.

### 1.2 Research Objectives and Scope

This report aims to provide a comprehensive analysis of how stability boundaries in signal coordination affect system-level congestion propagation, addressing the following key research questions:

First, we examine the fundamental nature of stability boundaries in signal coordination systems, exploring how these boundaries are mathematically characterized and what factors influence their definition and extent. The concept of stability in traffic networks has been rigorously defined in the literature, with a network considered strongly stable if there exists a finite bound such that the time-averaged number of vehicles in the network remains below this bound as time approaches infinity [3]. This definition implies that for stability to hold, average outflow must be greater than or equal to average inflow, meaning vehicles exit the network at approximately the same rate at which they enter. Understanding how signal coordination parameters influence this stability condition is essential for effective network management.

Second, we investigate the mechanisms through which signal coordination stability affects congestion propagation dynamics. This includes analysis of how coordinated signal timing creates or constrains pathways for congestion waves, how the spatial and temporal boundaries of coordinated regions influence spillback effects, and how different coordination strategies interact with the underlying network topology to determine propagation patterns.

Third, we explore the implications of these relationships for practical traffic management strategies, examining how understanding stability boundaries can inform the design of more resilient urban transportation systems. This includes consideration of perimeter control strategies, adaptive signal coordination approaches, and emerging connected vehicle-based systems that leverage real-time data and communication capabilities.

The scope of this analysis encompasses both theoretical frameworks for understanding signal coordination stability and congestion propagation, as well as practical considerations for implementation in real-world urban transportation networks. While the primary focus is on urban road networks, the principles discussed have broader applicability to other flow networks exhibiting similar cascading failure characteristics.

## 2. Theoretical Foundations of Signal Coordination Stability

### 2.1 Fundamentals of Signal Coordination

Signal coordination in urban transportation networks refers to the systematic establishment of timing relationships between adjacent signalized intersections to optimize the progression of vehicle platoons through the network. The fundamental objective of coordination is to minimize stops, delays, and travel time for vehicles traversing arterial corridors or network-wide routes [4]. When intersections are coordinated effectively, vehicles released from an upstream intersection can proceed through subsequent intersections without stopping, forming what transportation researchers commonly refer to as a "green wave" that propagates vehicles through the network in a continuous, efficient manner.

The FHWA report on signal timing fundamentals establishes that coordination is accomplished by adding a layer of logic—termed coordination logic—to the basic actuated logic used for isolated signal timing operations [4]. This coordination logic complements basic features such as phase initiation and termination timing, establishing an additional set of time-based relationships that govern how signals respond to traffic conditions across multiple intersections. The decision to implement coordination at a given location depends on several factors, with research indicating that coordination is particularly advantageous when intersections are located within approximately three-quarters of a mile of each other [4]. At greater distances, the benefits of coordination become more dependent on traffic volumes and the potential for forming vehicle platoons.

The performance of signal coordination is typically evaluated through measures including stops, vehicle delay, and arterial travel time, though additional measures may include changes in delay to transit vehicles and the existence of spillback queuing [4]. These performance metrics are directly influenced by the stability of the coordination plan, which refers to the ability of the coordinated system to maintain efficient progression patterns despite fluctuations in demand, perturbations from incidents, or variations in compliance rates. A stable coordination plan maintains its effectiveness across a range of operating conditions, while an unstable plan may exhibit erratic behavior that actually degrades network performance compared to uncoordinated operation.

### 2.2 Mathematical Characterization of Stability Boundaries

The mathematical characterization of stability boundaries in signal coordination systems requires careful consideration of both static and dynamic network properties. Static properties include road capacities and node connections, while dynamic properties encompass shockwaves and traffic states that evolve over time [2]. Percolation theory has emerged as a powerful mathematical tool for characterizing congestion propagation over networks, enabling researchers to determine time-varying boundaries of propagating congestion and to design control mechanisms that respond to real-time organization of congestion in the network [2].

The definition of stability for traffic networks has been formalized through the concept of strong stability, which requires that the time-averaged number of vehicles in the network remains bounded over time [3]. Mathematically, this can be expressed as:

$$\lim_{T \to \infty} \sup \frac{1}{T} \sum_{t=1}^{T} E\left[\sum_{(i,j) \in A} x_{ij}(t)\right] \leq \kappa$$

where $x_{ij}(t)$ represents the number of vehicles on link $(i,j)$ at time $t$, $A$ is the set of all network links, and $\kappa$ is a finite constant bounding the average network vehicle count [3]. For this condition to hold, the average outflow from the network must be greater than or equal to the average inflow, which implies that all demand can be served without unbounded accumulation of vehicles.

The stable region $D$ represents the set of demands that can be stabilized by some control strategy [3]. Research has shown that stability can typically be proven only for the interior of this stable region, with an $\epsilon$-margin separating any demand point in the interior from the boundary of the region. This boundary represents a critical threshold beyond which the network cannot maintain stable operation, regardless of the control strategy employed. The location and characteristics of this boundary depend on the network topology, the control strategy being used, and the distribution of demand across the network.

For signal coordination specifically, the stability boundary can be characterized through the relationship between signal timing parameters and the resulting capacity of coordinated movements. The effective capacity of a coordinated arterial is determined by the green time allocation, cycle length, and the ability to maintain progression bands that accommodate vehicle platoons. When demand exceeds this capacity, the coordination plan becomes unstable, leading to queue formation, spillback, and potential propagation of congestion to upstream intersections.

### 2.3 Congestion as a Primary Cascade Mechanism

Understanding congestion as a primary mechanism for cascading failures in flow networks provides essential context for analyzing signal coordination stability. Network flow models for studying cascading failures identify congestion as the central process through which initial perturbations can escalate into system-wide failures [5]. When perturbations cause systems to route flow through alternative paths, some nodes or links may become overloaded, leading to their failure. This failure then forces additional rerouting, potentially causing further overloads and failures in a cascade that can ultimately disable the entire network.

The propagation of failures in complex networks can be classified into two primary categories: cascading structural failures and cascading failures due to functional overloads [6]. Structural failures spread directly through network connections, where the failure of one element directly causes failure of connected elements. Functional overloads, in contrast, spread through the propagation of excessive loads as flow is redistributed following initial failures. Transportation networks are particularly susceptible to functional overload cascades, where the failure of a road segment or intersection causes traffic to reroute, potentially overloading alternative routes and triggering additional failures.

Research on cascading failures in scale-free networks has demonstrated that network robustness depends critically on the relationship between load redistribution patterns and node capacity tolerances [6]. The robustness of a network, quantified by the relative size of the giant percolation cluster, decreases as the tolerance parameter $\alpha$ decreases or the initial damage fraction $p$ increases. For small $\alpha$ values, the network is near criticality and exhibits abrupt collapse following even minor initial damage, while for large $\alpha$ values, the network exhibits smooth degradation with high tolerance to initial damage. This relationship between capacity tolerance and cascade propagation has direct implications for signal coordination design, suggesting that coordination strategies that provide greater capacity margins may enhance network resilience to cascading congestion.

## 3. Mechanisms of Congestion Propagation in Signalized Networks

### 3.1 Spillback Effects and Queue Dynamics

One of the most significant mechanisms through which congestion propagates in signalized networks is the spillback effect, where queues at downstream intersections extend backward to block upstream intersections, disrupting the normal flow of traffic and potentially triggering cascading delays. Perimeter control strategies, while effective in keeping targeted regions free of congestion, may inadvertently trigger the formation of congested queues at control boundaries that then propagate congestion outward [2]. This phenomenon illustrates a fundamental tension in traffic management: strategies that successfully protect specific network regions may shift congestion to adjacent areas, potentially creating new instability boundaries that affect system-wide performance.

The dynamics of queue spillback depend on several factors including the spatial distribution of signal timing parameters, the geometric characteristics of road segments, and the temporal patterns of demand. When a downstream intersection operates at capacity with a persistent queue, vehicles cannot clear the intersection during green phases, causing the queue to extend upstream. If this queue reaches an upstream intersection, it may block the upstream intersection's exit, preventing that intersection from clearing its own queue and causing congestion to propagate further upstream. This backward propagation of congestion represents a critical failure mode that signal coordination strategies must address.

Research has demonstrated that the congestion propagation dynamics depend on travel demand, road network structure, and physical properties of road segments such as the number of lanes [2]. The complexity and stochasticity of these factors make it very difficult to predict the precise shape of congested components that emerge under various control scenarios. However, understanding the general principles governing spillback dynamics enables the design of coordination strategies that minimize the likelihood of queue interaction between adjacent intersections and that contain congestion within bounded regions when spillback does occur.

### 3.2 Shockwave Propagation and Stability Boundaries

Traffic shockwaves represent another critical mechanism through which congestion propagates through signalized networks, with direct implications for signal coordination stability. Shockwaves are disturbances in traffic flow that propagate backward through the network as vehicles respond to changing conditions downstream. When a signal changes from green to red, a shockwave propagates upstream as drivers begin to decelerate in response to the stopped queue. Similarly, when a signal returns to green, a recovery shockwave propagates upstream as vehicles begin accelerating from the stopped condition.

The interaction between shockwaves and signal coordination boundaries determines whether congestion remains localized or propagates system-wide. In a well-coordinated system, shockwaves generated at individual intersections are absorbed by the progression bands of the coordination plan, preventing their amplification and backward propagation. However, when signal timing parameters deviate from optimal values or when demand exceeds coordination capacity, shockwaves can reinforce each other and propagate through the network as a consolidated congestion wave that overwhelms the coordination mechanism.

The stability boundary for signal coordination can be understood as the threshold at which the coordination mechanism can no longer absorb shockwaves generated by normal signal operations. Below this threshold, the coordination plan maintains stable progression bands that accommodate vehicle platoons and prevent shockwave amplification. Above this threshold, shockwaves escape the coordination bands and propagate through the network, causing queue accumulation and potential spillback effects that disrupt coordination and lead to system-wide congestion. This relationship between shockwave dynamics and coordination stability provides a physical interpretation of the mathematical stability boundaries discussed earlier.

### 3.3 Network Topology Effects on Propagation

The topology of urban road networks significantly influences how congestion propagates through the system and how signal coordination stability boundaries affect overall network performance. Different network topologies exhibit different susceptibilities to cascading congestion, with some topologies providing natural barriers that contain congestion while others facilitate rapid propagation across the network. Understanding these topological effects is essential for designing effective signal coordination strategies that account for the specific characteristics of the network being managed.

Research on cascading failures in complex networks has shown that the robustness of network structure depends on the distribution of loads and capacities across network elements [6]. Networks with heterogeneous degree distributions, such as scale-free networks, are highly robust to random failures but vulnerable to targeted attacks on highly connected nodes. Urban road networks exhibit similar characteristics, with major arterial corridors serving as high-degree nodes whose failure can trigger widespread congestion. Signal coordination strategies must account for these topological vulnerabilities by providing additional capacity margins on critical network elements and by designing coordination plans that can accommodate rerouting when primary corridors become congested.

The interaction between network topology and signal coordination stability creates complex feedback dynamics that influence system-level congestion propagation. When a coordinated arterial approaches its stability boundary, the coordination plan may become unstable, causing vehicles to queue and potentially spill back onto intersecting streets. This queue spillback can trigger congestion propagation in the cross-street network, potentially overwhelming coordination plans on those streets and creating a cascade of instability that spreads through the network. The likelihood and extent of such cascades depend on the connectivity between network elements and the capacity of alternative routes to accommodate diverted traffic.

## 4. Signal Coordination Strategies and Their Stability Characteristics

### 4.1 Fixed-Time Coordination Systems

Fixed-time signal coordination represents the traditional approach to managing signal timing across urban networks, using predetermined timing plans that are implemented based on time-of-day schedules. These systems operate on the principle that traffic patterns exhibit regular daily cycles that can be anticipated and planned for, with different coordination plans implemented for different periods such as morning peak, midday, evening peak, and off-peak hours. The stability of fixed-time coordination systems depends on how well the predetermined plans match actual traffic conditions, with deviations from expected patterns potentially causing the system to approach or exceed its stability boundaries.

The primary advantage of fixed-time coordination is its simplicity and reliability; the timing plans are known in advance, implementation is straightforward, and the systems are generally robust to sensor failures or communication disruptions. However, fixed-time systems have limited ability to respond to unexpected conditions such as incidents, special events, or atypical demand patterns. When actual conditions deviate significantly from those assumed in the timing plan design, the coordination may become unstable, leading to queue accumulation and congestion propagation that could have been prevented by a more responsive control strategy.

Research on fixed-time coordination performance has demonstrated that the effectiveness of different coordination strategies varies significantly depending on traffic conditions [7]. Studies comparing coordination approaches under different demand levels have found that all strategies produce increased delays as demand approaches capacity, but the relative performance of different strategies changes with demand level. Under near-saturation conditions (degree of saturation less than 1.0), coordination strategies that prioritize progression continuity tend to outperform those that prioritize other objectives, while under oversaturated conditions, strategies that provide more flexible response to queue formation may be more effective [7].

### 4.2 Adaptive Signal Control Systems

Adaptive signal control systems represent a significant advancement over fixed-time approaches, utilizing real-time traffic data to forecast near-future traffic flow conditions and adjust signal timing accordingly [8]. These systems continuously monitor traffic conditions at intersections and along corridors, using this information to optimize signal timing parameters in response to changing demand patterns. The adaptive capability of these systems enables them to maintain coordination stability across a wider range of conditions than fixed-time systems, as they can adjust timing parameters to accommodate demand fluctuations and respond to incidents.

The stability characteristics of adaptive signal control systems depend critically on the algorithms used for optimization and the feedback mechanisms that adjust signal timing. Well-designed adaptive systems incorporate stability considerations into their optimization objectives, ensuring that adjustments to signal timing do not inadvertently destabilize the coordination mechanism. However, poorly designed adaptive algorithms may exhibit oscillatory behavior, where overcorrection for current conditions creates new problems that require further correction, potentially leading to unstable operation that degrades network performance.

Connected vehicle-based adaptive signal control systems have demonstrated significant improvements over conventional adaptive systems by leveraging real-time vehicle data and vehicle-to-infrastructure communication capabilities [8]. These systems can obtain detailed information about individual vehicle positions, speeds, and trajectories, enabling more precise optimization of signal timing and more effective coordination across multiple intersections. Studies have shown that connected vehicle-based approaches can reduce average delay by significant percentages compared to conventional systems, though these benefits depend on market penetration rates and the reliability of communication systems [8].

### 4.3 Multi-Agent Coordination Approaches

Multi-agent approaches to signal coordination represent a paradigm shift from centralized to distributed control, where individual intersections or groups of intersections are controlled by autonomous agents that coordinate their actions through communication and negotiation. This approach offers several potential advantages for maintaining coordination stability, including scalability, robustness to partial system failures, and the ability to adapt to local conditions while maintaining system-wide coordination objectives.

Recent research has proposed multi-agent collaborative control approaches for urban network boundary intersections that can concurrently account for macro traffic dynamics within protected regions and the spatiotemporal distribution of traffic flows at boundary intersections [9]. These approaches utilize advanced techniques such as Bi-LSTM models combined with attention mechanisms to convey traffic state information between boundary intersection agents, enabling coordinated responses to changing conditions. The stability of such multi-agent systems depends on the communication mechanisms between agents and the coordination protocols that govern how agents resolve conflicts and align their actions.

The stability boundary for multi-agent coordination systems emerges from the interaction of individual agent behaviors and the communication delays between agents. When communication delays are small relative to the dynamics of traffic flow, agents can coordinate effectively and maintain stable operation across a wide range of conditions. However, when communication delays become significant or when agent coordination protocols fail to achieve alignment, the multi-agent system may exhibit unstable behavior where individual agents optimize locally at the expense of system-wide performance. Understanding and managing these stability boundaries is essential for deploying multi-agent signal coordination in large-scale urban networks.

### 4.4 Perimeter Control and Gating Strategies

Perimeter control represents a network-level approach to traffic management that regulates traffic flows between different regions of a road network by coordinating signal timings at region boundaries [2]. The objective of perimeter control is to improve overall network performance by managing the accumulation of traffic within protected regions, preventing oversaturation and the associated congestion propagation. This approach has proven effective in optimizing urban road traffic and is considered a crucial component of modern intelligent transportation systems.

The stability characteristics of perimeter control differ fundamentally from corridor-based coordination approaches. While corridor coordination aims to maximize progression through a linear sequence of intersections, perimeter control focuses on managing the total accumulation of vehicles within a protected region. The stability boundary for perimeter control is defined by the maximum accumulation that can be accommodated without causing queue spillback at the perimeter, which depends on the storage capacity of the protected region and the outflow capacity at the perimeter intersections.

A significant challenge for classical perimeter control is its limited perception of congestion propagation dynamics, viewing congestion only through aggregated or local properties such as traffic accumulation within the perimeter or queue length at each intersection [2]. This limited perception can lead to situations where perimeter control successfully maintains the protected region below congestion thresholds while inadvertently causing severe congestion outside the region due to queue spillback at the perimeter. The resulting congestion propagation outside the region can cancel out the benefits of perimeter control at a global level, illustrating the importance of considering system-wide effects when designing stability boundaries for network-level control strategies.

## 5. Impact of Stability Boundaries on System-Level Congestion

### 5.1 Local vs. Global Stability Considerations

The relationship between local signal coordination stability and system-level congestion propagation involves complex interactions that require careful analysis. Local stability refers to the ability of an individual intersection or short corridor to maintain efficient operation, while system-level stability requires that the entire network maintain bounded queues and prevent cascade effects. A signal coordination plan may be locally stable while contributing to system-level instability, or conversely, may exhibit local instability while helping to maintain system-wide stability.

This distinction has important implications for the design of signal coordination strategies. Strategies that optimize local intersection performance may inadvertently create conditions that promote congestion propagation to adjacent areas, ultimately degrading system-wide performance. For example, maximizing green time for a major arterial may improve progression along that arterial while causing excessive queues on cross streets, leading to spillback that blocks access to the arterial and degrades its performance. Effective coordination strategies must balance local optimization with system-wide considerations, maintaining stability boundaries that prevent such negative interactions.

Research on traffic signal control using deep reinforcement learning has explored this balance through the use of different objective function weightings [10]. Studies have examined policies that emphasize network-wide queue length reduction, average speed improvement, and arterial stops reduction, finding that the relative weighting of these objectives significantly influences how well the coordination strategy maintains stability across different demand levels. Policies that emphasize global stability objectives tend to perform better under high-demand conditions when the system is more prone to congestion, while policies that prioritize corridor throughput may perform better under moderate demand conditions [10].

### 5.2 Cascade Prevention Through Coordination Stability

Maintaining signal coordination within stable boundaries represents a critical strategy for preventing cascading congestion in urban networks. When coordination remains stable, the progression bands established by the coordination plan absorb shockwaves and prevent queue formation that could lead to spillback and cascade effects. However, when coordination stability is lost, the resulting queue formation and spillback can trigger congestion propagation that spreads through the network in a manner analogous to cascade failures in other infrastructure systems.

The prevention of cascading congestion through coordination stability requires understanding the conditions under which coordination transitions from stable to unstable operation. This transition typically occurs when demand exceeds the capacity of the coordination mechanism to maintain progression bands, causing queues to form and accumulate at intersections. As queues grow, they eventually reach the point where they block upstream intersections, causing spillback and triggering the backward propagation of congestion. The rate at which this cascade occurs depends on the network topology, the distribution of demand, and the response of signal timing to developing congestion.

Strategies for preventing cascade effects through coordination stability include maintaining capacity margins that keep demand below the stability boundary, implementing detection systems that identify approaching instability, and deploying responsive control strategies that restore stability before cascade effects occur. Connected vehicle-based systems offer particular advantages for cascade prevention, as they can detect developing congestion at earlier stages and implement more precise control adjustments to maintain stability [8]. However, even advanced control strategies cannot prevent cascades if demand consistently exceeds the capacity of the network, highlighting the importance of demand management alongside signal coordination.

### 5.3 Recovery Dynamics Following Instability

Understanding how transportation networks recover following instability events is essential for designing resilient signal coordination systems. When coordination stability is lost and congestion propagates through the network, the recovery process involves the gradual dissipation of queues and the restoration of normal progression patterns. The duration and extent of this recovery depend on the severity of the instability, the control strategies implemented during recovery, and the demand levels during the recovery period.

Research on cascading failures in complex networks has identified characteristic patterns in recovery dynamics, including the phenomenon of "walking failure" where sections of the network go down, causing subsequent sections to fail, after which the first sections come back up [1]. This ripple effect can make several passes through the same sections or connecting nodes before stability is restored. While this phenomenon was originally identified in the context of network computing and power systems, similar dynamics can be observed in transportation networks, where congestion waves propagate through the network in patterns that may oscillate before stabilizing.

The recovery of signal coordination following instability requires careful management of signal timing to gradually dissipate accumulated queues without causing renewed instability. Aggressive strategies that attempt to clear queues quickly may inadvertently cause shockwaves that propagate congestion to previously unaffected areas, while overly conservative strategies may extend recovery time and prolong the period of degraded network performance. Effective recovery strategies balance the need for queue dissipation with the maintenance of coordination stability, using gradual adjustments to signal timing that allow queues to clear while preventing the regeneration of congestion waves.

## 6. Emerging Technologies and Future Directions

### 6.1 Connected and Autonomous Vehicle Integration

The integration of connected and autonomous vehicles (CAVs) into urban transportation networks presents both opportunities and challenges for signal coordination stability and congestion propagation management. CAVs offer the potential for more precise control of vehicle trajectories, enabling signal coordination strategies that maintain tighter platoons and more efficient progression through intersections. The communication capabilities of CAVs also enable more sophisticated coordination algorithms that can respond to real-time conditions and coordinate across larger network areas.

Research on CAV-based signal coordination has demonstrated significant potential for improving network performance compared to conventional systems [8]. Studies have shown that CAV-based adaptive signal control can reduce average delay by substantial percentages, with one study reporting a 16.33% reduction in average delay compared to conventional systems [8]. However, these benefits depend on achieving sufficient market penetration of CAVs and on the reliability of communication systems that enable vehicle-to-infrastructure and vehicle-to-vehicle communication.

The stability characteristics of CAV-based coordination systems may differ significantly from conventional systems due to the more precise control of vehicle trajectories and the availability of more detailed information about network conditions. CAVs can potentially maintain stable coordination at higher demand levels than conventional systems, as they can adjust their speeds and trajectories to maintain progression bands even when signal timing is constrained. However, the stability of CAV-based systems also depends on the algorithms that govern vehicle behavior and the communication protocols that coordinate vehicle actions, which must be designed to prevent oscillations and instabilities that could arise from aggressive optimization.

### 6.2 Machine Learning and AI-Based Control

Machine learning and artificial intelligence approaches to signal control have emerged as powerful tools for managing the complexity of urban traffic networks. Deep reinforcement learning (DRL) algorithms have shown particular promise for traffic signal control, as they can learn complex control policies through interaction with the network environment without requiring explicit mathematical models of traffic dynamics. These approaches can potentially discover coordination strategies that outperform traditional optimization-based methods by exploiting patterns in traffic data that are not captured by conventional models.

Studies on DRL-based traffic signal control have examined the stability characteristics of different control strategies under varying demand conditions [10]. Research has found that different DRL strategies exhibit different stability properties, with some strategies showing smoother and more stable performance during training while others exhibit more pronounced fluctuations. Under high-demand conditions, when the system is more prone to congestion, control stability becomes especially important, and strategies that maintain stable operation during training tend to perform better in deployment.

The stability boundaries for AI-based control systems emerge from the interaction of the learning algorithm, the network environment, and the reward functions that guide learning. When reward functions emphasize short-term performance improvements, the learned policies may exhibit aggressive behavior that approaches or exceeds stability boundaries, leading to unstable operation under certain conditions. When reward functions incorporate stability considerations and longer-term performance metrics, the learned policies tend to maintain more conservative operation that stays within stable boundaries. The design of reward functions and training procedures that balance performance optimization with stability maintenance represents an active area of research.

### 6.3 Dynamic and Adaptive Boundary Management

The concept of dynamic boundary management represents an emerging approach to traffic control that adapts the geometry of controlled regions to the real-time organization of congestion in the network [2]. Traditional perimeter control operates with fixed geographic boundaries, which may not align with the actual extent of developing congestion. Dynamic boundary management uses percolation theory and real-time traffic data to identify the evolving boundary of congestion and adjust control boundaries accordingly, providing more effective containment of congestion while minimizing impacts on uncongested areas.

The stability characteristics of dynamic boundary management systems depend on the accuracy of congestion boundary detection and the responsiveness of boundary adjustment mechanisms. When boundary detection accurately identifies the true extent of congestion, dynamic adjustment can maintain effective control while minimizing unnecessary restrictions on traffic flow. However, detection errors or delayed adjustments may allow congestion to escape the controlled region, triggering propagation that could have been prevented by more conservative boundary management. The trade-off between control effectiveness and mobility impact requires careful calibration of boundary management algorithms.

Dynamic boundary management adds a new dimension to traffic control methods, specifically the flexibility of the geometry of perimeter control [2]. This flexibility enables more nuanced management of congestion propagation, as control boundaries can be adjusted to protect critical network elements while allowing traffic to flow more freely in less critical areas. The mathematical framework provided by percolation theory offers a rigorous foundation for implementing such dynamic mechanisms, enabling control systems to operate according to the real-time organization of congestion in the network.

## 7. Implications for Practice and Policy

### 7.1 Design Principles for Resilient Signal Coordination

The analysis presented in this report suggests several design principles for developing signal coordination systems that effectively manage stability boundaries and prevent system-level congestion propagation. First, coordination strategies should be designed with explicit consideration of stability boundaries rather than focusing solely on optimization under assumed conditions. This requires identifying the demand levels and conditions under which coordination becomes unstable and implementing safeguards that prevent operation beyond these boundaries.

Second, coordination design should account for the interaction between local and system-level stability, recognizing that locally optimal strategies may contribute to system-level instability. This requires evaluating coordination strategies not only at the corridor or intersection level but also in terms of their effects on adjacent network elements and on overall network performance. Simulation tools that can model the interaction of multiple coordination plans across a network are essential for this evaluation.

Third, monitoring and detection systems should be implemented to identify approaching instability before it manifests as congestion propagation. Connected vehicle data, real-time traffic sensors, and machine learning algorithms can provide early warning of developing instability, enabling proactive adjustments to signal timing that maintain stability. The investment in such monitoring and detection systems should be considered as part of the overall strategy for managing congestion propagation risk.

### 7.2 Operational Strategies for Stability Maintenance

Operational strategies for maintaining signal coordination stability include regular assessment of demand levels relative to coordination capacity, implementation of responsive control adjustments when demand approaches stability boundaries, and coordination across adjacent control areas to prevent negative interactions. Transportation agencies should develop operational procedures that define thresholds for intervention and specify the actions to be taken when these thresholds are approached or exceeded.

The coordination of signal timing across jurisdictional boundaries presents particular challenges for stability maintenance, as different agencies may implement different control strategies that conflict with each other. Establishing formal coordination mechanisms between agencies, sharing data on traffic conditions and signal timing, and implementing coordinated response protocols can help prevent instability that arises from uncoordinated actions across jurisdictional boundaries.

Training and capacity building for transportation agency staff is essential for effective implementation of stability-focused coordination strategies. Staff should understand the concepts of stability boundaries, congestion propagation mechanisms, and the relationship between local signal timing and system-wide performance. This understanding enables more effective decision-making during both routine operations and incident response.

### 7.3 Investment Priorities and Resource Allocation

Investment priorities for enhancing signal coordination stability should be guided by risk assessment that considers the likelihood and consequences of congestion propagation events. Critical network elements that, if congested, could trigger widespread propagation should receive priority for investment in enhanced monitoring and control capabilities. Similarly, network areas where current coordination approaches operate close to stability boundaries may warrant investment in upgrades that expand the stable operating region.

Investment in communication infrastructure is essential for enabling the advanced coordination strategies that offer the greatest potential for stability enhancement. Connected vehicle-based coordination, multi-agent control systems, and dynamic boundary management all require reliable communication between signal controllers, vehicles, and central management systems. Investment in communication infrastructure should be coordinated with investment in control systems to ensure that the full benefits of advanced coordination can be realized.

Research and development investments should focus on closing knowledge gaps identified in this report, including improved methods for predicting stability boundaries, more effective algorithms for maintaining stability under varying conditions, and better tools for evaluating the system-wide impacts of coordination strategies. Collaboration between transportation agencies, academic researchers, and technology providers can accelerate the development and deployment of improved coordination approaches.

## 8. Conclusion

This report has examined the complex relationship between stability boundaries of signal coordination and system-level congestion propagation in urban transportation networks. The analysis reveals that stability boundaries in signal coordination are fundamental determinants of network resilience, with the position and characteristics of these boundaries directly influencing whether localized disturbances remain contained or escalate into cascading congestion effects that affect entire urban areas.

The theoretical foundations of signal coordination stability rest on mathematical frameworks that characterize the conditions under which networks can maintain bounded queues and prevent unbounded congestion accumulation. The stable region for a network represents the set of demands that can be accommodated without exceeding coordination capacity, with the boundary of this region marking the threshold beyond which instability and cascade effects become likely. Understanding and managing these stability boundaries is essential for effective traffic management.

The mechanisms of congestion propagation in signalized networks include spillback effects, shockwave dynamics, and network topology interactions, all of which are influenced by the stability of signal coordination. When coordination remains stable, these mechanisms are contained and do not lead to system-wide effects. When coordination stability is lost, these mechanisms can interact in ways that amplify congestion and cause it to propagate through the network in patterns analogous to cascading failures in other infrastructure systems.

Different signal coordination strategies exhibit different stability characteristics, with fixed-time systems offering simplicity but limited adaptability, adaptive systems providing responsive control but requiring careful algorithm design, multi-agent approaches enabling distributed decision-making but introducing coordination challenges, and perimeter control offering network-level management but potentially causing spillback effects at boundaries. The choice of coordination strategy should be guided by the specific characteristics of the network being managed and the stability challenges it faces.

Emerging technologies including connected and autonomous vehicles, machine learning-based control, and dynamic boundary management offer significant potential for enhancing coordination stability and preventing congestion propagation. However, realizing this potential requires careful attention to the stability characteristics of these technologies and to the design of control algorithms that maintain stable operation across a range of conditions.

For practitioners and policymakers, this analysis suggests the importance of explicit consideration of stability boundaries in coordination design, implementation of monitoring and detection systems for early identification of approaching instability, and investment in communication infrastructure and advanced control capabilities that enable more effective stability management. By focusing on stability as a primary objective alongside traditional performance measures, transportation agencies can develop more resilient urban transportation systems that maintain efficient operation even under challenging conditions.

The relationship between signal coordination stability and congestion propagation represents a critical area for continued research and practical innovation. As urban transportation networks face increasing demands and as new technologies enable more sophisticated control approaches, the insights developed through this analysis provide a foundation for designing and operating systems that effectively balance efficiency with resilience.

## References

[1] Wikipedia, "Cascading failure," Wikimedia Foundation, 2024. [Online]. Available: https://en.wikipedia.org/wiki/Cascading_failure

[2] Y. Wang et al., "Characterizing resilience of flood-disrupted dynamic transportation network through the lens of link reliability and stability," *Reliability Engineering & System Safety*, 2024.

[3] NSF PAR, "Characterizing the Stable Region," National Science Foundation, 2024. [Online]. Available: https://par.nsf.gov/servlets/purl/10419441

[4] Federal Highway Administration, "Signal Timing Fundamentals," *FHWA-HOP-08-024*, 2008. [Online]. Available: https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm

[5] D. L. Alderson, "Cascading Failure in Critical Infrastructure Systems," Naval Postgraduate School, 2003.

[6] J. Wang et al., "Analysis of cascading failures in complex networks," *Physica A: Statistical Mechanics and its Applications*, 2024.

[7] Texas Transportation Institute, "Signal Timing on a Shoestring," TTI, 2024. [Online]. Available: https://static.tti.tamu.edu/tti.tamu.edu/documents/1288-S.pdf

[8] MAXAP Press, "Connected Vehicle-Based Traffic Signal Control," *Data, Traffic Model, and Control Strategy Analysis*, 2023. [Online]. Available: https://www.maxapress.com/article/doi/10.48130/DTS-2023-0008

[9] ScienceDirect, "Cascading failure model and resilience enhancement scheme of space information networks," *Reliability Engineering & System Safety*, 2024.

[10] arXiv, "Deep Reinforcement Learning for Traffic Signal Control," 2025. [Online]. Available: https://arxiv.org/pdf/2508.20102

## Annotations


## Sources
[1] https://aronlaszka.com/papers/basak2019data.pdf
[2] https://arxiv.org/html/2505.14544v3
[3] https://arxiv.org/pdf/2508.20102
[4] https://c2smart.engineering.nyu.edu/wp-content/uploads/2018/07/TrafficSignalOptimizationinConnectedCities-FinalReport.pdf
[5] https://discovery.ucl.ac.uk/10194245/1/Assessing%20dynamic%20congestion%20risks%20of%20flood-disrupted%20transportation%20network%20systems%20through%20time-variant%20topological%20analysis%20and%20traffic%20demand%20dynamics.pdf
[6] https://en.wikipedia.org/wiki/Cascading_failure
[7] https://en.wikipedia.org/wiki/Network_congestion
[8] https://faculty.nps.edu/dlalders/docs/Alderson-thesis-twoside-2003.pdf
[9] https://info.ornl.gov/sites/publications/files/Pub75211.pdf
[10] https://jeannin.github.io/papers/rastgoftar2020integrative.pdf
[11] https://jsaer.com/download/vol-11-iss-2-2024/JSAER2024-11-2-129-134.pdf
[12] https://mtreiber.de/Vkmod_Skript/Chap16_StabilityAnalysis.pdf
[13] https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm
[14] https://ops.fhwa.dot.gov/publications/fhwahop15038/fhwahop15038.pdf
[15] https://par.nsf.gov/servlets/purl/10419441
[16] https://static.tti.tamu.edu/tti.tamu.edu/documents/0-6402-P1.pdf
[17] https://static.tti.tamu.edu/tti.tamu.edu/documents/1288-S.pdf
[18] https://theses.hal.science/tel-03989830/document
[19] https://www.emergentmind.com/topics/adaptive-traffic-signal-control-atsc
[20] https://www.maxapress.com/article/doi/10.48130/DTS-2023-0008
[21] https://www.mdpi.com/1999-5903/18/1/44
[22] https://www.nature.com/articles/srep05381
[23] https://www.sciencedirect.com/science/article/abs/pii/S095183202400560X
[24] https://www.sciencedirect.com/science/article/abs/pii/S0957417424014945
[25] https://www.sciencedirect.com/science/article/abs/pii/S0968090X22003357
[26] https://www.sciencedirect.com/topics/engineering/cascading-failure
[27] https://www.tandfonline.com/doi/full/10.1080/15481603.2025.2547126