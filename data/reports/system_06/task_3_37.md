# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 671b0537 | **Time:** 197.50s | **Cost:** $0.03571
--------------------------------------------------------------------------------

# The Effect of Green Wave Phase Offset on Intersection Capacity Distribution Under Random Arrival Patterns

## Abstract

This research report examines the relationship between green wave phase offset and intersection capacity distribution under conditions of random vehicle arrival patterns. Green wave synchronization represents a sophisticated approach to traffic management that coordinates multiple signalized intersections to facilitate uninterrupted vehicle flow along arterial corridors. The effectiveness of such coordination depends critically on the proper calibration of phase offsets between adjacent intersections, particularly when traffic arrivals deviate from deterministic platoon patterns. This analysis synthesizes findings from traffic flow theory, stochastic queueing models, and empirical studies to evaluate how phase offset influences capacity distribution, delay characteristics, and overall intersection performance under random arrival conditions. The investigation reveals that while phase offset has minimal direct impact on absolute intersection capacity, it significantly affects the distribution of capacity utilization across coordinated intersections and plays a crucial role in managing deterministic versus random delay components. The findings have important implications for the design and implementation of adaptive traffic control systems in urban environments characterized by variable traffic demand.

## 1. Introduction

### 1.1 Background and Motivation

The efficient management of traffic flow through signalized intersections represents one of the most consequential challenges in modern urban transportation systems. As cities continue to grow and vehicle volumes increase, the need for sophisticated traffic management strategies becomes ever more pressing. Among the various approaches developed over decades of transportation research, green wave coordination has emerged as a particularly effective methodology for improving arterial corridor performance. This strategy involves the synchronization of traffic signals along a corridor such that vehicles traveling at a designated speed encounter a sequence of green signals, thereby minimizing stops and reducing overall travel delays [1].

The fundamental principle underlying green wave operation is the coordination of traffic signals to facilitate the smooth progression of vehicle platoons through multiple intersections. When successfully implemented, this coordination creates what transportation engineers describe as a "green corridor," where vehicles can maintain consistent speeds without experiencing the inefficiencies of repeated acceleration and deceleration cycles associated with stop-and-go traffic [2]. The economic and environmental benefits of such systems are substantial, encompassing reduced fuel consumption, lower emissions, decreased travel times, and improved overall network efficiency.

However, the effectiveness of green wave coordination is fundamentally dependent on the accurate determination of phase offsets between adjacent intersections. The phase offset represents the time difference between the activation of green phases at successive signals along the corridor. When offsets are properly calibrated, vehicles can traverse the corridor with minimal interruption. When offsets are misaligned, vehicles may encounter red signals despite optimal progression speeds, leading to queue formation, increased delays, and reduced capacity utilization [3].

### 1.2 The Challenge of Random Arrival Patterns

The theoretical foundation of green wave design assumes relatively uniform vehicle arrivals, typically modeled as deterministic platoons moving at consistent speeds along the corridor. Under these idealized conditions, the calculation of optimal offsets becomes a straightforward matter of synchronizing signal timing with predicted platoon arrival times. The ideal offset, as defined in traffic engineering literature, represents the time required for the first vehicle of a platoon to travel from the upstream intersection to the downstream intersection, ensuring that the downstream signal turns green precisely as the platoon arrives [4].

Real-world traffic environments, however, rarely conform to these idealized assumptions. Vehicle arrivals at signalized intersections typically exhibit significant randomness, influenced by factors including driver behavior variations, downstream intersection conditions, turning movements, and the inherent stochastic nature of traffic generation. This randomness is particularly pronounced in urban environments where multiple access points, varying land uses, and diverse trip purposes create complex arrival patterns that deviate substantially from uniform platoon distributions [5].

The presence of random arrival patterns fundamentally challenges traditional green wave design approaches. When vehicles arrive in an irregular fashion rather than as organized platoons, the assumptions underlying offset optimization calculations become invalid. Vehicles may arrive at downstream intersections during red phases despite optimal offset settings, or conversely, may arrive during green phases even when offsets are suboptimally configured. This creates a complex relationship between offset timing and intersection performance that cannot be adequately captured by deterministic models alone [6].

### 1.3 Research Objectives and Scope

This report aims to provide a comprehensive analysis of how green wave phase offset affects intersection capacity distribution under random arrival patterns. The investigation addresses several interconnected questions that are critical for understanding and optimizing coordinated signal operations:

First, the report examines the theoretical foundations of capacity distribution in coordinated signal systems, distinguishing between the absolute capacity of individual intersections and the effective capacity experienced by vehicles traversing the corridor. Second, it analyzes how phase offset influences the different components of intersection delay, particularly the distinction between deterministic delay that depends on offset timing and random delay that arises from stochastic arrival patterns. Third, it evaluates the implications of these relationships for adaptive traffic control systems that must respond to real-time variations in traffic demand.

The scope of this analysis encompasses both the mathematical foundations of traffic flow theory and the practical considerations involved in implementing coordinated signal systems. While the primary focus is on urban arterial corridors with fixed-time signal coordination, attention is also given to adaptive and actuated control systems that modify offset timing in response to prevailing conditions.

## 2. Theoretical Framework for Green Wave Coordination

### 2.1 Fundamental Principles of Signal Coordination

Green wave coordination operates on the principle that the efficiency of traffic flow through a series of signalized intersections depends not only on the performance of individual intersections but also on the relationships between them. When intersections operate independently, each vehicle approaching a signal faces a probability of encountering a red indication that depends solely on the cycle length and green ratio of that particular intersection. Under random arrival conditions, this probability is approximately equal to the red time fraction of the cycle, leading to expected delays that can be calculated using standard queuing theory [3].

When multiple intersections are coordinated, however, the arrival process at downstream signals is no longer independent of upstream signal operations. Vehicles departing a green phase at an upstream intersection arrive at the downstream intersection after a travel time that depends on the distance between intersections and the prevailing speed. If the downstream signal turns green at approximately the same time these vehicles arrive, they can pass through without stopping. If not, they must wait, potentially forming queues that affect upstream intersection operations [7].

The coordination of signals requires that all intersections along the corridor share a common cycle length, though in some circumstances involving high traffic volumes, certain intersections may operate on double cycle lengths to accommodate demand [4]. Within this common cycle framework, the green phase at each intersection is offset relative to a reference point, with the offset determining when each signal turns green relative to the others. The goal of offset optimization is to select offset values that maximize the proportion of vehicles experiencing uninterrupted flow through the corridor.

### 2.2 Mathematical Representation of Phase Offset

The phase offset between two adjacent intersections can be formally defined as the time difference between a fixed reference point in the signal cycle at the upstream intersection and the corresponding point at the downstream intersection. In practice, this reference point is typically the beginning of the green phase for the coordinated movement. The ideal offset for a given pair of intersections is calculated as:

$$\text{Offset}_{\text{ideal}} = \frac{d}{v}$$

where $d$ represents the distance between the two signalized intersections and $v$ represents the average platoon speed [4]. This ideal offset ensures that vehicles departing the upstream intersection at the beginning of its green phase will arrive at the downstream intersection precisely as it begins its green phase, allowing continuous progression.

In practice, the actual offset implemented may differ from this ideal value due to various constraints including conflicting traffic demands, pedestrian crossing requirements, and the need to accommodate multiple movement directions. The deviation between actual and ideal offsets directly affects the proportion of vehicles that must stop at the downstream intersection. When the actual offset is less than ideal, vehicles arrive before the green phase begins and must wait. When the actual offset exceeds ideal, vehicles arrive after the green phase has begun, potentially missing the green window entirely if the offset difference exceeds the queue clearance time [3].

### 2.3 Capacity Concepts in Coordinated Systems

Understanding the effect of offset on capacity distribution requires careful distinction between several related but distinct capacity concepts. The absolute capacity of an intersection approach is determined by the saturation flow rate and the effective green time available during each cycle. The saturation flow rate represents the maximum rate at which vehicles can pass through the intersection when the green indication is displayed and vehicles are queued. For typical urban intersections, saturation flow rates range from approximately 1800 to 2200 vehicles per hour of green time per lane [3].

The effective capacity available to coordinated movements depends on the green split allocated to each phase and the cycle length. The green split determines the proportion of each cycle devoted to each movement, while the cycle length determines how frequently green time becomes available. For a given green split, longer cycles provide more green time per phase but increase the frequency of stops and the potential for queue formation.

In coordinated systems, the concept of bandwidth becomes important for characterizing the capacity available to through movements. The bandwidth represents the time window during which vehicles can enter the corridor at the upstream end and traverse the entire length without encountering a red signal. A wider bandwidth indicates greater capacity for uninterrupted flow, while a narrower bandwidth limits the number of vehicles that can benefit from coordination [1].

## 3. Delay Components and Their Dependence on Offset

### 3.1 Deterministic Delay and the Offset Effect

Traffic delay at signalized intersections can be decomposed into several components, each with distinct characteristics and dependencies. The deterministic component of delay arises from the cyclic nature of signal operation and the resulting queue formation and dissipation during each cycle. When vehicles arrive at a constant rate and depart at the saturation flow rate during green phases, the queue dynamics follow a predictable pattern that can be analyzed using deterministic models [3].

The deterministic delay is strongly influenced by the offset between adjacent signals. Hillier and Rothery's seminal analysis of vehicle delays at pretimed signals demonstrated that the deterministic delay depends critically on the time lag between the start of upstream and downstream green signals [3]. When the offset is optimally set, vehicles departing the upstream intersection during its green phase arrive at the downstream intersection as it turns green, minimizing the queue formation at the downstream location. When the offset deviates from optimal, vehicles arrive during the red phase at the downstream intersection, contributing to queue buildup and increased delay.

The relationship between offset and deterministic delay can be illustrated through the queue profile diagram, which shows queue length as a function of time over a signal cycle. The area under this queue profile represents the total deterministic delay experienced during the cycle. When offset is optimal, the queue at the downstream intersection is minimized because vehicles arrive as green becomes available. When offset is suboptimal, the queue profile expands, increasing the total delay [3].

An important finding from empirical studies is that the minimum delay observed at the optimal offset increases substantially as the distance between signals increases [3]. This occurs because longer distances result in greater dispersion of vehicle platoons as they travel between intersections. The platoon diffusion effect means that vehicles that departed as a compact group at the upstream intersection arrive at the downstream intersection spread over a longer time period, reducing the efficiency of the green phase utilization.

### 3.2 Random Delay Under Stochastic Arrival Processes

While deterministic delay depends on the systematic relationship between arrival and departure patterns, random delay arises from the stochastic variability in vehicle arrivals. When arrivals follow a Poisson process, the number of vehicles arriving during any given interval follows a probability distribution with variance equal to the mean. This variability means that even with optimal offset settings, some vehicles will arrive during red phases due to random clustering of arrivals [3].

The random delay is typically calculated assuming Poisson arrivals and constant departure rates corresponding to signal capacity. Under these assumptions, the expected random delay can be expressed as a function of the degree of saturation, which represents the ratio of arrival rate to capacity. When the degree of saturation is less than one, the random delay remains finite. When it approaches or exceeds one, the random delay grows without bound as queues accumulate over successive cycles [3].

A critical insight from traffic flow theory is that the random delay component does not appear to be influenced by signal offset [3]. This finding has important implications for coordinated signal design. While offset optimization can substantially reduce deterministic delays by improving progression efficiency, it has no effect on the random delays arising from arrival variability. This suggests that offset optimization should be viewed as a means of minimizing deterministic delay rather than a solution to congestion arising from oversaturated conditions.

The independence of random delay from offset can be understood by considering that random delays arise from the inherent variability in arrival patterns rather than from systematic mismatches between arrival and departure schedules. Even with perfect offset timing, random clustering of arrivals will result in some vehicles arriving during red phases and experiencing delay. Conversely, even with poor offset timing, some vehicles will arrive during green phases by chance and experience no delay [6].

### 3.3 Overflow Delay and Queue Persistence

A third component of intersection delay is the overflow delay, which occurs when the number of arrivals during a cycle exceeds the capacity available during the green phase. Under these conditions, vehicles not served during the current cycle remain in queue for subsequent cycles, creating persistent queues that affect both delay and capacity utilization [3].

Research findings indicate that signal offset does not significantly influence the overflow delay component [3]. This is because overflow delay is primarily determined by the relationship between total arrivals and total capacity over multiple cycles, rather than by the timing of arrivals within individual cycles. When the arrival rate exceeds capacity, queues will accumulate regardless of offset settings. The rate of queue accumulation depends on the degree of saturation, while the time required for queue dissipation depends on the available capacity during undersaturated periods.

The independence of overflow delay from offset has practical implications for traffic management. When intersections are operating near or above capacity, offset optimization provides limited benefits because the primary source of delay is overflow rather than progression inefficiency. Under these conditions, capacity expansion or demand management may be more effective strategies than signal coordination [6].

## 4. Capacity Distribution Effects Under Random Arrivals

### 4.1 Platoon Diffusion and Arrival Pattern Evolution

When vehicles depart a signalized intersection during the green phase, they initially travel as a relatively compact platoon. However, as vehicles proceed downstream, the platoon gradually disperses due to variations in vehicle speeds, driver behavior, and interactions with other traffic. This platoon diffusion has significant implications for capacity distribution in coordinated systems [3].

The rate of platoon diffusion depends on the distance between intersections, the speed of travel, and the heterogeneity of vehicle speeds within the platoon. At short distances, vehicles remain relatively compact, and the arrival pattern at the downstream intersection closely resembles the departure pattern from the upstream intersection. At longer distances, significant diffusion occurs, and arrivals become more uniformly distributed over time [4].

Under random arrival conditions at the upstream intersection, the arrival pattern at the downstream intersection reflects both the upstream arrival randomness and the diffusion process. Even if arrivals at the upstream intersection were uniform, diffusion would introduce some randomness into the downstream arrival pattern. When upstream arrivals are already random, the downstream arrival pattern exhibits compounded variability [5].

The practical consequence of platoon diffusion is that the benefits of offset optimization diminish with increasing distance between intersections. While optimal offsets can substantially reduce delays at closely spaced intersections, the effectiveness decreases as spacing increases due to the increasing randomness of arrivals. This suggests that green wave coordination is most beneficial for corridors with relatively short intersection spacings, typically less than one mile apart [4].

### 4.2 Stochastic Queueing Analysis

The analysis of capacity distribution under random arrivals requires stochastic queueing models that capture the variability in both arrivals and service times. Traditional deterministic models assume constant arrival and service rates, which cannot adequately represent the variability present in real traffic systems [6].

Miller's foundational work on stochastic queue distribution developed approximate formulas for average overflow queue that are applicable to arbitrary arrival and departure distributions [3]. These formulas account for the probability that arrivals during a cycle will exceed the available capacity, resulting in queue persistence. The key insight from this analysis is that queue distribution depends on both the mean and variance of arrivals, with higher variability leading to larger expected queues for a given mean arrival rate.

The variance-to-mean ratio of arrivals is a critical parameter in stochastic queueing analysis. For Poisson arrivals, this ratio equals one, indicating moderate variability. When arrivals are more clustered than Poisson, the ratio exceeds one, leading to larger expected queues and delays. When arrivals are more uniform than Poisson, the ratio is less than one, resulting in smaller expected queues [3].

Tarko and colleagues analyzed random delay with respect to the differential capacity factor and the variance-to-mean ratio of arrivals, demonstrating that both parameters significantly affect delay performance [3]. Their analysis showed that for a given degree of saturation, higher arrival variability results in greater random delays. This finding underscores the importance of considering arrival pattern characteristics when designing coordinated signal systems.

### 4.3 Offset Optimization for Capacity Distribution

The optimization of offsets for capacity distribution in coordinated systems involves balancing the competing demands of different intersections along the corridor. Traditional green band optimization methods aim to maximize the bandwidth available for through movements, implicitly assuming that maximizing bandwidth will maximize capacity utilization [1].

Recent research has challenged this assumption, demonstrating that green band width does not always correlate with good coordination performance. A study by researchers at the University of Michigan developed an offset optimization method that explicitly considers vehicle distribution through a stochastic queueing model calibrated from vehicle trajectories [1]. Rather than maximizing green band width as an intermediate objective, this approach directly optimizes the total delay and number of stops, which are the ultimate performance measures of interest.

The optimization program developed in this research uses a coordinate-descent algorithm to minimize total delay and stops by adjusting offsets along the corridor. Field implementation results demonstrated significant improvements, with average control delay decreasing by 12% to 15% and average number of stops decreasing by 14% to 18% after offset optimization [1]. These improvements were achieved without changing cycle lengths or green splits, demonstrating the substantial impact that offset optimization can have on corridor performance.

An important finding from this research is that intersection offsets do not have much influence on absolute capacity but could lead to better coordination with other intersections [1]. This distinction between capacity and coordination is crucial for understanding the role of offset optimization. While offsets cannot increase the fundamental capacity of an intersection approach, they can improve the distribution of capacity utilization across the corridor and reduce the delays experienced by vehicles traversing the system.

## 5. Adaptive Control and Real-Time Offset Adjustment

### 5.1 Challenges in Adaptive Coordination

The analysis presented thus far has focused primarily on fixed-time signal coordination, where offsets are predetermined based on historical traffic patterns and remain constant during operation. However, real-world traffic conditions are inherently dynamic, with demand varying by time of day, day of week, and in response to special events or incidents. This variability creates challenges for fixed-time coordination systems that cannot adapt to changing conditions [5].

Adaptive signal control systems address this challenge by continuously adjusting signal timing parameters in response to real-time traffic measurements. Systems such as SCOOT (Split Cycle Offset Optimization Technique) and SCATS (Sydney Coordinated Adaptive Traffic System) use data from infrastructure sensors to optimize cycle lengths, green splits, and offsets on a cycle-by-cycle or even sub-cycle basis [5]. These systems can respond to fluctuations in demand, providing more efficient operation than fixed-time systems under variable conditions.

The coordination of adaptive signals presents unique challenges compared to fixed-time systems. In adaptive systems, the cycle length may vary from cycle to cycle as the system responds to demand fluctuations. This variability complicates offset optimization because the reference point for offset calculation changes with each cycle. Additionally, the actuated nature of many adaptive systems means that green times are not fixed in advance but depend on real-time traffic measurements [6].

### 5.2 Two-Stage Stochastic Programming Approaches

Recent research has developed sophisticated optimization frameworks for adaptive coordinated control that explicitly account for stochastic vehicle arrivals. A particularly notable approach formulates the offset optimization problem as a two-stage stochastic program, with the base timing plan determined in the first stage and adaptive offset adjustments made in the second stage to compensate for overflow effects [6].

The first stage of this approach designs the base timing plan, including cycle length and green splits, to serve stochastic traffic demand up to a specified level of phase clearance reliability. The phase clearance reliability concept represents the probability that the base green time will be sufficient to clear the queue during each cycle. By designing the base plan to achieve a target reliability level, the system ensures that adaptive adjustments will only be needed under exceptional conditions [6].

The second stage determines how green splits and offsets should be adaptively modified based on stochastic vehicle arrivals and residue queues from previous cycles. When the base green time is insufficient to clear the queue, the system can extend the green phase or adjust offsets to provide additional capacity for the coordinated movement. These adjustments are constrained to maintain a minimum green time for the coordinated phase and to preserve the overall cycle length [6].

The effectiveness of this approach stems partly from the use of short cycle lengths, which are enabled by the adaptive offset adjustments that address part of the random arrivals without requiring extended green times. By distributing the capacity adjustments across multiple intersections through offset modifications, the system can handle variability more efficiently than systems that rely solely on green time extensions at individual intersections [6].

### 5.3 Implications for Capacity Distribution

The adaptive offset adjustment approaches have significant implications for capacity distribution in coordinated systems. By dynamically modifying offsets in response to real-time conditions, these systems can shift capacity utilization across the corridor to match prevailing demand patterns. When upstream intersections experience high demand, offsets can be adjusted to provide additional green time for the coordinated movement. When downstream intersections are congested, offsets can be modified to restrict flow and prevent queue spillback [6].

The stochastic programming framework ensures that adaptive adjustments are made in a principled manner that accounts for the probabilistic nature of future arrivals. Rather than reacting to individual cycle outcomes, which may be influenced by random fluctuations, the system makes adjustments based on expected conditions and reliability requirements. This approach reduces the volatility that might arise from over-responsive control while still providing the benefits of adaptation [6].

Research results demonstrate that the PCR-based (Phase Clearance Reliability) control method effectively minimizes average total delay for coordinated control systems [6]. The optimal control performance is achieved through the combination of well-designed base timing plans and intelligent adaptive offset adjustments that respond to stochastic arrivals while maintaining coordination benefits.

## 6. Practical Implementation Considerations

### 6.1 Intersection Spacing and Coordination Benefits

The benefits of green wave coordination depend critically on the spacing between intersections along the corridor. Research indicates that coordination is most beneficial when intersections are spaced within approximately 0.75 miles of each other [5]. At greater spacings, the platoon diffusion effects become so pronounced that the arrival pattern at downstream intersections approaches randomness, limiting the benefits of offset optimization.

The practical implication is that green wave coordination should be focused on corridors with relatively closely spaced intersections. For arterial streets with intersections spaced less than one mile apart, coordination can provide substantial benefits. For corridors with greater spacing, the benefits diminish, and resources may be better allocated to improving individual intersection operations [4].

Within the optimal spacing range, the actual distance between intersections affects the sensitivity of delay to offset errors. Research has shown that the minimum delay at optimal offset increases with distance between signals [3]. This means that offset accuracy becomes more important as intersection spacing increases, because the consequences of offset errors are greater. For closely spaced intersections, even suboptimal offsets may allow reasonable progression, while for widely spaced intersections, precise offset timing is essential.

### 6.2 Traffic Demand Characteristics

The effectiveness of offset optimization also depends on the characteristics of traffic demand along the corridor. Green wave coordination is most beneficial when traffic volumes are high and relatively balanced across the coordinated movements. Under these conditions, the efficiency gains from improved progression translate into significant reductions in delay and stops for a large number of vehicles [7].

When traffic volumes are low, the benefits of coordination are limited because few vehicles are present to benefit from improved progression. In these cases, the fixed costs of coordination, including the constraints imposed on individual intersection operations, may exceed the benefits [5]. This suggests that coordination should be selectively applied based on demand levels, with isolated intersection operation during low-demand periods.

The directionality of demand also affects coordination benefits. Green wave coordination is inherently directional, providing greater benefits to vehicles traveling in the coordinated direction than to those traveling in the opposite direction. When demand is strongly directional, coordination can provide substantial benefits for the major flow while imposing minimal costs on the minor flow. When demand is balanced in both directions, trade-offs must be made, and the optimal coordination may involve alternating offsets or other strategies that balance performance in both directions [4].

### 6.3 Integration with Emerging Technologies

The implementation of green wave coordination is increasingly influenced by emerging technologies that provide new capabilities for traffic monitoring and control. Vehicle-to-everything (V2X) communication systems enable direct communication between vehicles and infrastructure, allowing for more precise coordination based on actual vehicle positions and speeds rather than estimated platoon arrival times [2].

Advanced algorithms, including deep reinforcement learning approaches such as Deep Q-Networks (DQN), are being applied to traffic signal control for purposes including emergency vehicle prioritization and green wave guidance for human drivers [2]. These algorithms can learn optimal offset strategies through experience, potentially discovering coordination patterns that exceed the performance of traditional optimization methods.

The integration of real-time data from cameras, sensors, and GPS devices enables adaptive signal control systems to respond to changing conditions with greater precision and speed [2]. Systems such as SCOOT and SCATS have demonstrated the ability to maintain efficient coordination under varying demand conditions, providing benefits that fixed-time systems cannot achieve.

However, the deployment of these advanced systems must carefully consider the safety of all road users, including pedestrians and cyclists who may be affected by signal coordination decisions [2]. The optimization of offsets for vehicle progression should not come at the expense of pedestrian safety or accessibility. Balancing efficiency and safety remains a key challenge in the implementation of coordinated signal systems.

## 7. Conclusions and Future Directions

### 7.1 Summary of Key Findings

This analysis has examined the relationship between green wave phase offset and intersection capacity distribution under random arrival patterns, revealing several important findings that have implications for traffic signal design and operation.

First, phase offset has minimal direct influence on the absolute capacity of individual intersections. The capacity of an intersection approach is primarily determined by the saturation flow rate and the green time available, which are governed by cycle length and green split decisions rather than offset timing [1]. However, offset significantly affects how capacity is distributed across the corridor and how effectively available capacity is utilized by through movements.

Second, the effect of offset on delay is primarily manifested through the deterministic delay component, which depends on the time lag between upstream and downstream green signals [3]. Optimal offset timing minimizes deterministic delay by ensuring that vehicles arrive at downstream intersections as green phases begin. Random delay, arising from stochastic arrival variability, is not affected by offset [3]. This distinction suggests that offset optimization should be viewed as a means of reducing deterministic delay rather than addressing congestion from oversaturated conditions.

Third, platoon diffusion effects limit the benefits of offset optimization at longer intersection spacings. As distance between signals increases, vehicle platoons disperse, and arrivals become more random, reducing the effectiveness of coordination [3]. Green wave coordination is most beneficial for corridors with intersections spaced less than one mile apart [4].

Fourth, adaptive offset adjustment approaches can improve coordination performance under variable demand conditions. Stochastic programming frameworks that explicitly account for arrival uncertainty have demonstrated significant delay reductions compared to fixed-time coordination [6]. These approaches dynamically adjust offsets to respond to real-time conditions while maintaining coordination benefits.

### 7.2 Implications for Practice

The findings of this analysis have practical implications for traffic engineers and transportation agencies responsible for signal coordination. Offset optimization should be approached as a continuous process rather than a one-time design activity. As traffic patterns evolve and intersection spacing constrains coordination benefits, periodic reassessment of offset timing is necessary to maintain optimal performance.

The selection of coordination strategies should be based on careful analysis of intersection spacing, demand patterns, and system objectives. For corridors with closely spaced intersections and high directional demand, traditional green band optimization may provide substantial benefits. For corridors with greater spacing or more balanced demand, alternative approaches that directly optimize delay and stops may be more appropriate [1].

Investment in adaptive control systems should be considered for corridors with highly variable demand patterns. The ability to adjust offsets in real-time can provide significant benefits compared to fixed-time coordination, particularly when demand fluctuates substantially by time of day or in response to incidents [6].

### 7.3 Future Research Directions

Several areas warrant further investigation to advance understanding of offset effects on capacity distribution. First, the interaction between offset optimization and emerging connected and autonomous vehicle technologies deserves attention. As vehicle-to-infrastructure communication becomes more widespread, new opportunities may arise for precise coordination based on actual vehicle positions rather than estimated platoon arrival times.

Second, the integration of multimodal considerations into offset optimization remains underexplored. Current approaches focus primarily on vehicle delay and stops, but pedestrian, cyclist, and transit operations may be affected by coordination decisions. Developing frameworks that balance multiple mode considerations would enhance the sustainability and equity of signal coordination.

Third, the scalability of optimization approaches to large networks with many intersections requires further investigation. While coordinate-descent and other local optimization methods have shown promise for corridor-scale optimization, their application to network-wide coordination with multiple overlapping routes presents computational and methodological challenges.

Finally, the robustness of offset optimization to demand uncertainty and prediction errors warrants additional study. While stochastic programming approaches address some aspects of uncertainty, the development of frameworks that explicitly account for forecast errors and provide reliable performance across a range of scenarios would enhance the practical value of coordination optimization.

## References

[1] Nature Communications, "Optimizing traffic signal offsets for reduced delays and stops," 2024.

[2] arXiv, "Green Wave Optimization and Intelligent Transportation Systems," arXiv:2507.22511, 2025.

[3] Federal Highway Administration, "Traffic Flow Theory: A State-of-the-Art Report," Chapter 9: Traffic Flow at Signalized Intersections.

[4] Wikipedia, "Green Wave," Traffic Signal Coordination Article.

[5] NYU C2SMART, "Traffic Signal Optimization in Connected Cities," Final Report, 2018.

[6] ScienceDirect, "Adaptive signal optimization under coordinated control with stochastic vehicle arrivals," 2016.

[7] ETHZ Archive, "Traffic in Urban Networks: CrowdstoCrises Lecture Materials."

## Annotations


## Sources
[1] https://archiv.soms.ethz.ch/teaching/CrowdstoCrisesHS11/Lecture5_TrafficInUrbanNetworks.pdf
[2] https://arxiv.org/html/2507.22511
[3] https://c2smart.engineering.nyu.edu/wp-content/uploads/2018/07/TrafficSignalOptimizationinConnectedCities-FinalReport.pdf
[4] https://en.wikipedia.org/wiki/Green_wave
[5] https://libdoc.fh-zwickau.de/opus4/files/17967/TrafficGreenWave.pdf
[6] https://pmc.ncbi.nlm.nih.gov/articles/PMC11991238/
[7] https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf
[8] https://www.kangastudio.co/how-traffic-lights-use-the-green-wave-strategy-2/
[9] https://www.nature.com/articles/s41467-024-45427-4
[10] https://www.sciencedirect.com/science/article/abs/pii/S0968090X16301875