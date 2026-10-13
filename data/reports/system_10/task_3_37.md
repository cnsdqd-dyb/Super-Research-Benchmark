# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 7fa0aebd | **Time:** 112.35s | **Cost:** $1.22351
--------------------------------------------------------------------------------

# The Effect of Green Wave Phase Offset on Intersection Capacity Distribution Under Random Arrival Patterns

Green wave signal coordination represents a sophisticated approach to traffic management where consecutive traffic signals are synchronized to create continuous flow for vehicles traveling at a designated speed. The phase offset, defined as the time difference between the start of green phases at adjacent signalized intersections, serves as the primary control parameter that determines whether vehicles can traverse multiple intersections without stopping. This report examines how variations in phase offset timing influence the distribution of intersection capacity when vehicle arrivals follow stochastic (random) patterns rather than deterministic profiles. The research reveals that while optimal phase offsets can significantly enhance throughput for coordinated movements, the interaction between offset selection and random arrival variability creates complex capacity distribution effects that vary substantially across the network. Specifically, phase offsets that optimize bandwidth for one direction or movement type often reduce capacity availability for competing movements, and these trade-offs become more pronounced under conditions of random arrival variability where the predictability of vehicle platoons diminishes.

## Fundamentals of Green Wave Technology and Phase Offset Design

### Core Principles of Green Wave Signal Coordination

A **green wave**, also known as the platoon effect, occurs when a series of traffic signals (typically three or more) are coordinated to allow continuous traffic flow over several intersections in one primary direction[1]. The fundamental concept relies on creating a synchronized cascade of green lights where vehicles traveling at an engineer-designated speed encounter successive green indications without interruption. Any vehicle traveling along with the green wave at the approximate speed decided upon by traffic engineers will see a progressive cascade of green lights and will not have to stop at intersections[1]. This allows higher traffic loads and reduces noise and energy use because less acceleration and braking is needed[1].

The design of green waves begins with traffic engineers assessing traffic flow characteristics within both signalized and unsignalized intersections. The common practice is to coordinate major street traffic signals less than 1 mile (1.6 kilometers) apart, with the actual green wave effect potentially lasting up to 2.0 miles (3.2 kilometers)[1]. This coordination framework depends critically on the concept of the phase offset, which represents the temporal relationship between signal transitions at adjacent intersections.

### Phase Offset Definition and Calculation

The phase offset serves as the time difference between when a reference point (typically the start of the green phase) occurs at one intersection compared to an adjacent downstream intersection. The ideal offset is calculated using the fundamental relationship between distance and travel speed[1][2]. The mathematical formula for the ideal offset is expressed as:

\[t_{ideal} = \frac{L}{S}\]

where $L$ represents the distance between two signalized intersections and $S$ represents the average platoon speed[1]. This straightforward calculation provides the theoretical basis for offset determination, representing the time required for a vehicle departing from one signal to reach the next signal as that signal turns green.

However, real-world conditions introduce complexities that require adjustments to this ideal offset. The adjusted ideal offset accounts for queued vehicles and lost time at the upstream intersection:

\[t_{adjust} = t_{ideal} - (Qh + l_1) = \frac{L}{S} - (Qh + l_1)\]

where $Q$ represents the number of vehicles queued per lane, $h$ is the discharge headway of queued vehicles in seconds per vehicle, and $l_1$ is start-up lost time in seconds[1]. This adjustment recognizes that the green wave effectively progresses faster than the arriving platoon to pick up queued vehicles that could not proceed during the previous cycle[1].

### Bandwidth and Capacity Throughput

The concept of bandwidth describes the amount of green time available for vehicles to travel through a system at a determined progression speed. Bandwidth is defined as the time difference between when the first vehicle can pass through the entire system nonstop and when the last vehicle can do the same, creating essentially a "green window" that follows the platoon[1]. The bandwidth efficiency, defined as the ratio of bandwidth to the system's cycle length, is calculated as:

\[EFF_{BW} = \frac{BW}{C}\]

where $BW$ is the bandwidth in seconds and $C$ is the cycle length in seconds[1]. A good bandwidth efficiency is generally considered to fall between 40 to 55 percent[1][8].

The bandwidth capacity, representing the number of vehicles that can pass through signals without stopping, is calculated as[1]:

\[c_{BW} = \frac{3600 \times BW \times L}{C \times h}\]

where $c_{BW}$ is the bandwidth capacity in vehicles per hour, $L$ is the number of directional through lanes, and $h$ is the saturation headway (time difference between two adjacent vehicles in a queue passing through green lights)[1]. This capacity metric provides an upper bound on throughput for vehicles that can maintain the designated progression speed without stopping.

## Understanding Intersection Capacity Distribution

### Capacity Fundamentals at Signalized Intersections

Intersection capacity represents the maximum rate at which vehicles can pass through a given point in an hour under prevailing conditions, accounting for roadway characteristics such as number and width of lanes, grades, and lane use allocations[50]. At signalized intersections, capacity for a particular movement is defined by two fundamental elements: the maximum rate at which vehicles can pass through a given point in an hour under prevailing conditions (the saturation flow rate), and the ratio of time during which vehicles may enter the intersection[7][34]. The capacity at a signalized intersection approach is calculated as the saturation flow of the approach multiplied by the proportion of time it is in operation[22].

The volume-to-capacity ratio (v/c ratio) has emerged as a critical metric for understanding intersection performance. Movements or lane groups with volume-to-capacity ratios less than 0.85 are considered undersaturated and typically have sufficient capacity and stable operations[7]. For movements with a v/c ratio between 0.85 and 1.00, traffic flow becomes less stable due to natural cycle-to-cycle variations in traffic flow[7]. The closer a movement operates to capacity, the more likely that natural fluctuations in traffic flow (such as higher demand, presence of large trucks, or driver behavior variations) may cause the demand during a single cycle to exceed the green time available for that cycle[7].

### Critical Movement Analysis and Network Effects

In coordinated signal systems, traffic engineers employ critical movement analysis to identify the movements that constrain overall intersection capacity[7]. The critical movement represents the phase or combination of phases with the highest v/c ratio across all movements at an intersection. Understanding critical movements is essential because signal timing must provide sufficient green time to all movements, but the critical movement ultimately determines the minimum cycle length required[7][34].

In networked systems with multiple intersections, the capacity distribution becomes more complex. When intersections are coordinated, the capacity available for the coordinated phase (typically the main street through movement) may be enhanced at the expense of other movements[7]. This redistribution of capacity across different movements at various intersections creates what researchers describe as asymmetric capacity distribution—certain movements and certain intersections receive preferential treatment while others experience reduced capacity[11][19][27].

## Random Arrival Patterns and Their Impact on Traffic Flow

### Stochastic Nature of Vehicle Arrivals

While green wave design traditionally assumes deterministic or quasi-deterministic arrival patterns where vehicles form stable platoons departing from upstream signals, real-world traffic rarely conforms to these idealized conditions. Vehicle arrivals follow stochastic processes characterized by random variations around mean demand levels[9][32]. The Poisson distribution has been widely adopted in traffic engineering to model these random arrival processes[9], representing conditions of "free flow" where vehicle arrivals at an intersection are essentially random and unrelated to upstream intersection operations.

Under truly random arrival conditions described by a Poisson distribution, the probability that exactly $x$ vehicles will arrive during any interval is given by[9][10]:

\[P(x) = \frac{m^x e^{-m}}{x!}\]

where $m$ represents the expected number of arrivals during the analysis interval. This distribution creates significant implications for capacity analysis because random arrivals introduce additional uncertainty and variability into the queuing process beyond what deterministic models predict[4][26].

### Overflow Delay and Queue Formation

The presence of random arrivals introduces what traffic engineers call "overflow delay" or "incremental delay" in addition to the uniform delay that results from the average relationship between demand and signal timing[7][10][26]. Overflow delay accounts for the additional waiting experienced by vehicles when natural cycle-to-cycle fluctuations in arrival rates happen to exceed the capacity provided by a particular green phase[26]. This phenomenon becomes increasingly important as the degree of saturation increases.

The average signal delay per vehicle consists of two components: uniform delay (which would occur with perfectly uniform arrivals) and overflow delay (which results from random variations in arrival patterns)[10][22]. The total delay calculation requires knowledge of the volume-to-capacity ratio, the cycle length, the green time provided for the movement, and adjustment factors that account for the type of signal control and the quality of traffic progression[10][32][34].

### Platoon Dispersion Effects

The dispersion of vehicle platoons between signalized intersections represents another critical aspect of how random arrival processes interact with coordinated signal timing. When a coordinated signal releases a platoon of vehicles (created by the red phase at that signal), the vehicles begin to disperse as they travel to the downstream signal due to differences in driver desired speeds, acceleration capabilities, and driving behavior[32]. This platoon dispersion means that vehicles that departed the upstream signal as a cohesive group arrive at the downstream signal spread across a wider time window, effectively introducing randomness into what were originally deterministic arrivals[32].

The extent of platoon dispersion depends on the distance between intersections, the speed variance among drivers, and traffic conditions along the roadway. Research indicates that when successive intersections are far enough apart (generally 3.2 kilometers or more), the extent of dispersion may become sufficient to assume that uninterrupted flow exists on some part of the roadway between them[32]. Conversely, for closely spaced intersections typical of urban arterials, platoon structure remains recognizable but is degraded compared to the original formation.

## Phase Offset Effects on Capacity Distribution Under Random Arrivals

### How Offset Affects Coordinated Movement Capacity

The phase offset determines the temporal window during which vehicles from the upstream intersection can enter through the green phase at the downstream intersection. For vehicles following the idealized offset calculation, an optimal offset creates a scenario where the leading edge of the upstream platoon arrives at the downstream signal just as it turns green, and the trailing edge of the platoon clears through before the signal returns to red. This optimal timing maximizes the proportion of the coordinated platoon that encounters green indication, thereby maximizing the coordinated movement's throughput capacity.

However, under random arrival conditions where vehicles do not form perfect platoons but instead arrive according to stochastic processes, the relationship between offset and capacity becomes more nuanced. Random arrivals mean that some vehicles arrive earlier than expected (relative to the offset design) while others arrive later[4][7][32][34]. An offset that was calculated based on average conditions may not optimize capacity across the distribution of random arrivals. For example, if the offset is set such that average arrival time aligns perfectly with green onset, vehicles arriving early in the cycle will encounter the tail end of the red phase at the downstream signal, while vehicles arriving late in the cycle will encounter the beginning of the red phase.

### Asymmetric Capacity Redistribution Between Directions

In two-way arterial streets, the selection of a particular phase offset to optimize green wave progression in one direction necessarily creates a different offset (or inverse offset) for the opposite direction[1][11][16][27]. A forward offset that provides good progression in one direction creates a poor offset for the opposite direction, meaning vehicles traveling in that direction will be more likely to encounter red indications[1][3][11][16].

Traffic engineers must balance these competing interests. In many cases, they prioritize the direction with higher traffic volumes, thereby optimizing capacity distribution to favor that direction at the expense of the minor direction[3][11][16][27]. This introduces structural asymmetry into the network's capacity distribution where parallel routes experience substantially different levels of service despite having identical geometric and signal timing characteristics except for offset direction. Under random arrival conditions, this asymmetry is somewhat mitigated because the random nature of arrivals means that some vehicles in the disadvantaged direction will still randomly align with green phases, though less frequently on average than vehicles in the favored direction.

### Capacity Distribution Across Multiple Intersections

In corridors with multiple consecutive intersections, the phase offset creates cascading effects on capacity distribution. The offset selected for the first segment (between intersections 1 and 2) influences whether vehicles can maintain progression through the second segment (between intersections 2 and 3)[1][3][16][27]. If offsets are imperfectly coordinated or if random arrival variability causes platoons to disperse, the capacity benefit available at downstream intersections may be substantially reduced compared to upstream intersections[19][27].

Research examining offset optimization in networks has demonstrated that this cascading effect is particularly pronounced under random arrival conditions[13][25][38]. When researchers employed sinusoidal approximations to model periodic arrival and departure processes in networks with multiple intersections, they found that phase offsets optimized for capacity at one intersection often resulted in reduced capacity at downstream intersections due to the interaction between offset timing and arrival variability[13][25][38].

### Critical Saturation Range Effects

The effect of phase offset on capacity distribution varies dramatically depending on whether intersections are operating in undersaturated, near-saturated, or oversaturated conditions[7][34][44]. In undersaturated conditions where the v/c ratio is substantially below 1.0, random arrivals produce relatively small fluctuations in queue formation and dissipation, and the primary benefit of offsets comes from providing green indication to arriving vehicles. In near-saturated conditions (v/c ratios between 0.85 and 1.0), random arrivals produce substantial cycle-to-cycle variation in whether all arrivals can be served during a single green phase, and phase offset becomes critical in determining which vehicles encounter standing queues versus free-flow conditions[7][34].

Under oversaturated conditions where demand exceeds capacity (v/c ratio exceeding 1.0), phase offsets become nearly irrelevant to capacity distribution because all movements at all intersections experience standing queues throughout the analysis period[28]. The interaction between offset and random arrivals fundamentally changes under these extreme conditions, with queue accumulation and spillback effects dominating the traffic dynamics rather than the carefully calculated offsets[28][44][47].

## Mathematical Models and Quantitative Analysis

### Queuing Theory Applications

The fundamental queuing model for signalized intersections employs what traffic engineers call the D/D/1 model for deterministic analysis and extensions incorporating stochasticity for random arrival conditions[10][26][32][48]. The D/D/1 model assumes deterministic arrivals at rate $\lambda$ and deterministic service (departures) at rate $\mu$, with a single service channel (the signalized intersection). Using this model with knowledge of arrival rates, departure rates, and red times, various useful metrics regarding queues can be computed[10].

For random arrivals following Poisson distribution with average saturation flow rate, the total delay can be decomposed into deterministic and stochastic components[10][26][48]:

\[d = d_1 + d_2\]

where $d_1$ represents uniform delay and $d_2$ represents overflow delay from random arrivals[10][22][26].

The uniform delay component, applicable even with random arrivals, is calculated as[10]:

\[d_1 = \frac{C(1-g/C)^2}{2(1-v/c)}\]

where $C$ is the cycle length, $g$ is the effective green time, and $v/c$ is the volume-to-capacity ratio[10][22].

The overflow delay component specifically accounting for the stochastic effects is calculated as[10]:

\[d_2 = \frac{900T[(X-1) + \sqrt{(X-1)^2 + \frac{8kIX}{cT}}]}{c}\]

where $X$ is the v/c ratio, $T$ is the analysis period duration, $k$ is a delay adjustment factor dependent on signal controller mode, $I$ is an upstream filtering adjustment factor, and $c$ is the cycle length[10].

### Offset Optimization Under Random Arrivals

Recent research has developed sophisticated mathematical formulations for optimizing phase offsets in networks characterized by random or partially random arrival processes. One influential approach utilizes sinusoidal approximation of the periodic arrival and departure processes in networks[13][25][38]. Under the periodicity assumption that the network operates in periodic steady state with all arrivals, departures, and queues periodic with period equal to the cycle length, the arrival process at queue $\ell$ can be approximated as[25]:

\[\hat{a}_\ell(t) = A_\ell + \alpha_\ell \cos(\omega t - \phi_\ell)\]

where $A_\ell$ represents the average arrival rate, $\alpha_\ell$ allows for periodic fluctuation in the arrival rate, $\omega$ is the angular frequency, and $\phi_\ell$ is the phase angle[25]. The offset $\Phi_\ell = \phi_\ell / \omega$ represents the time shift of the periodic arrival process and includes the travel time between intersections[25].

This sinusoidal approximation enables formulation of the offset optimization problem as a quadratically constrained quadratic program (QCQP) that can be solved via convex semidefinite relaxation[25][38]. The resulting optimization approach accommodates networks with arbitrary topology and scales well with network size, unlike earlier mixed-integer programming approaches that became computationally intractable for large networks[13][25][38].

### Bandwidth Efficiency Under Variable Arrivals

The bandwidth efficiency metric, fundamental to green wave design, takes on different meanings under random versus deterministic arrivals[7][8][11][16][34]. Under ideal deterministic conditions with perfect platoons and no arrival variability, the bandwidth efficiency directly translates to the proportion of vehicles in the coordinated movement that can proceed without stopping. Under random arrival conditions, however, vehicles arriving outside the designated bandwidth window may still encounter green indication due to random variations, or conversely, vehicles arriving within the nominal bandwidth may encounter red indication if arrival variability causes dispersion[7][34].

Research examining bandwidth under coordinated-actuated signal control has found that the relationship between nominal bandwidth efficiency and actual throughput efficiency becomes substantially degraded as arrival variability increases[52]. The progression adjustment factor, which accounts for the effect of coordinated signal timing on delay relative to isolated signal operation, can vary from less than 0.5 (indicating greater than 50 percent delay reduction) to greater than 1.5 (indicating delay increase) depending on the quality of progression as reflected in the percent of arrivals occurring during green time[52][59].

## Empirical Evidence and Case Studies

### Network-Scale Offset Optimization Results

A comprehensive case study examining offset optimization for a thirteen-intersection arterial corridor network in Arcadia, California, part of UC Berkeley's Connected Corridors project, demonstrated the complex relationship between offset selection and capacity distribution under realistic traffic conditions[13][25][31]. The network simulation compared baseline offsets derived from traditional engineering practice with offsets optimized using the semidefinite relaxation approach described above. The results revealed that offset optimization reduced mean peak queue lengths by approximately 27 percent and mean average queue lengths by 27.4 percent compared to baseline settings[13][25][31].

Importantly, this study also revealed how capacity distribution shifted across the network as a result of offset optimization. Peak queue length reductions on main arterial links were substantially greater (27.2 percent) than on cross-street links, demonstrating that the offset optimization preferentially enhanced capacity distribution for the primary directional movements[13][25][31]. The study further found that optimized offsets reduced average travel time in the network by 8.9 percent compared to baseline conditions[13][25][31], indicating that even though queue length was reduced primarily for certain movements, the network-wide benefit was substantial.

### Offset Optimization Performance Under Varying Demand Levels

Research examining signal timing under varying traffic conditions found that the efficacy of carefully designed offsets diminishes markedly as traffic demand increases toward saturation[28][44][47]. Under light traffic conditions, offsets optimized for maximizing progression provide substantial delay reduction. However, as demand increases into the 0.85 to 0.95 v/c range where traffic flow becomes less stable, the benefits of any particular offset pattern diminish because the random variations in cycle-to-cycle demand begin to overwhelm the advantage provided by offset timing[28][44].

Furthermore, under oversaturated conditions where demand exceeds capacity, research practitioners found that signal offset becomes nearly irrelevant to system performance[28][44][47]. Instead, the primary control objectives shift from minimizing delay through progression to managing queue spillback and preventing overflow between intersections[28][44][47]. In these conditions, the interaction between phase offset and random arrivals is governed by fundamental queuing dynamics rather than the coordination benefits that offset timing provides under undersaturated conditions.

### Comparison Between Fixed and Actuated Coordination

The application of phase offsets differs substantially between fixed-time coordinated systems and actuated-coordinated systems[3][6][21][27]. Fixed-time coordinated systems maintain rigid offsets throughout each time period, meaning that the offset calculated for average conditions persists regardless of actual arrival patterns[3][6]. This creates scenarios where the offset may be well-suited to the actual arrivals during some cycles but poorly suited during others as random variations occur.

Actuated-coordinated systems introduce flexibility by allowing certain phases to terminate early if demand is satisfied (gap out) or extend if demand remains high (max out)[3][6][21]. Even within actuated-coordinated systems, however, the coordinated phase maintains a predetermined offset to the master clock or to other coordinated phases at neighboring intersections[3][6]. Research examining actuated-coordinated performance found that the interaction between actuated logic and fixed offsets creates complex effects on capacity distribution[3][6][21]. When a non-coordinated phase gaps out, additional time becomes available to the coordinated phase, enhancing its capacity. Conversely, when a non-coordinated phase maxes out, capacity for the coordinated phase is constrained, regardless of the offset selection[3][6][21].

## Limitations and Practical Considerations

### Offset Design Constraints in Real Networks

In real traffic networks, the theoretical benefits of optimal phase offset design encounter numerous practical constraints[1][3][11][16][27][49]. All intersections in a coordinated system must operate at the same cycle length or at integer multiples of a common base cycle length[1][3][16][27][49]. This requirement exists to maintain the mathematical relationships that define offsets. Where intersections naturally require different cycle lengths based on their geometric characteristics and critical movement volumes, forcing a common cycle length results in suboptimal timing at some intersections[1][3][16][27][49].

Furthermore, in networks with non-uniform block lengths or where geometric constraints force intersections to be spaced at irregular intervals, the ideal offset calculation may result in trajectories that do not correspond to actual travel times, requiring manual adjustments[1][3][11][49]. In two-way arterials where good progression is desired in both directions simultaneously, perfect offsets optimizing both directions simultaneously are mathematically impossible except under special geometric conditions where intersection spacing is a multiple of half the cycle length[1][3][11][16][27][49].

### Pedestrian and Non-Vehicular Effects

While this analysis has focused on vehicular capacity distribution, practical signal timing decisions must balance vehicular progression with pedestrian safety and transit operations[53][54]. Longer cycle lengths, often required to coordinate over longer distances or among more intersections, result in longer pedestrian clearance intervals and longer overall wait times for pedestrians[53][54]. Research has shown that longer cycle lengths and coordination zones can incentivize drivers to speed, creating safety implications that offset some of the operational benefits of coordination[53][54].

Additionally, signal coordination constrains the flexibility available for transit signal priority or for responding to emergency vehicle preemption, as both of these interventions require disruption of the coordinated phase timing, with potentially cascading effects on downstream intersections[53][54]. The requirement to maintain common cycle lengths for coordination means that transit agencies often find coordinated systems poorly suited to accommodating buses operating on fixed schedules, as the phase timing relationships cannot be flexibly adjusted to accommodate TSP requests without disrupting the coordination for general traffic[53][54].

### Sensitivity to Demand Pattern Changes

Coordinated signal systems are generally designed based on traffic count data representing typical or peak hour conditions on a specific day of the week[53]. However, traffic demand varies substantially both within days (morning peak, midday, evening peak, night) and between days (weekday versus weekend, seasonal variations)[28][44][53]. The same offset that optimizes capacity distribution during morning peak periods may be poorly suited to midday or evening conditions when turning volumes, directional splits, and overall demand levels differ substantially[28][44][53].

Under random arrival conditions where the baseline traffic pattern already contains substantial variability, the additional variability arising from changes in demand patterns between analysis periods further degrades the performance of offsets designed for specific conditions[28][44][53]. Research has shown that approximately 10 percent of vehicles travel the entire length of coordinated corridors in real networks, meaning that the majority of vehicles at intermediate intersections are either entering or exiting the corridor[53]. This demand pattern implies that the capacity benefits of coordination are distributed unevenly across the corridor and across different times of day, with benefits concentrated primarily on through movements during the time period for which the signals were timed[53].

### Offset Transition Complexity

When signal timing plans change (such as transitions between time-of-day plans or emergency preemption), the phase offset must transition from one value to another[3][11][16][27][49]. This transition process is itself complex and affects capacity distribution during the transition period. Three basic transition modes exist: dwell (hold in coordinated phase until new offset achieved), lengthen (extend cycle length to accommodate both old and new offset timing), and shorten (reduce cycle length to achieve new offset sooner)[3][11][16][27][49].

Each transition mode has different implications for capacity distribution. Dwell mode concentrates delays during the transition to the coordinated movement, while lengthen and shorten modes distribute delays across multiple movements[3][11][16][27][49]. To avoid excessive cycle length or phase greens that become too short during transition, controllers typically limit the maximum adjustment per cycle, with transition completion generally occurring over three to five cycles in worst-case scenarios[3][11][16][27][49]. During this transition period, capacity distribution becomes highly irregular as offsets gradually shift from their previous values toward new values, creating temporary inefficiencies.

## Synthesis and Implications for Traffic Management

The effect of green wave phase offset on intersection capacity distribution under random arrival patterns reveals that traffic signal coordination presents a fundamental trade-off between optimizing capacity for coordinated movements versus maintaining flexibility and equity across all movements and directions. Under deterministic or quasi-deterministic arrival patterns with stable platoons, carefully calculated offsets can provide substantial capacity benefits for the coordinated movement, with potential delay reductions of 10 to 40 percent compared to uncoordinated operation[53].

However, the introduction of random arrival variability—which characterizes real traffic more accurately than idealized platoon models—substantially complicates this relationship. Random arrivals create cycle-to-cycle variability in whether vehicles can proceed during their designated green time, introducing overflow delays that are not captured by deterministic models[4][26][32][48]. Under these conditions, phase offsets that are optimal for average demand conditions may be suboptimal when actual arrivals deviate substantially from average patterns.

The capacity distribution effects cascade through networks of multiple intersections, with offsets optimized at one location potentially reducing capacity availability at downstream or cross-street locations[13][25][31][38]. This network-level trade-off means that practitioners cannot simply optimize offsets locally at individual intersections but must consider system-wide impacts. Advanced optimization techniques using sinusoidal approximation and semidefinite relaxation have provided computational methods for addressing these complex trade-offs, demonstrating network-wide improvements of 25 to 27 percent in queue metrics when applied to real arterial networks[13][25][31].

The efficacy of offset-based capacity enhancement diminishes substantially as traffic demand increases toward and beyond saturation points[28][44][47]. In undersaturated conditions, offsets provide meaningful progression benefits and delay reduction. In near-saturated conditions, the benefits persist but are diminished and more sensitive to demand fluctuations. In oversaturated conditions, traditional offset-based coordination becomes nearly irrelevant, and instead queue spillback management and metering strategies become the dominant control objectives[28][44][47].

## Conclusion

The relationship between green wave phase offset and intersection capacity distribution under random arrival patterns is more nuanced and complex than traditional deterministic models suggest. While phase offsets can enhance capacity for coordinated movements by ensuring that vehicle platoons encounter favorable signal indications, the random variability inherent in real traffic creates scenarios where actual capacity distribution differs substantially from theoretical predictions. The offset that is theoretically optimal for average conditions may underperform during periods when random variations in arrivals diverge substantially from averages.

In practical implementation, traffic engineers must balance multiple competing objectives: maximizing throughput for primary through movements, maintaining reasonable service for secondary movements and cross-street traffic, accommodating pedestrians and transit operations, and maintaining system flexibility to respond to demand variations and unexpected events. The phase offset, as a single parameter among many signal timing characteristics, interacts with cycle length, green splits, and controller logic to determine overall system performance. Advanced optimization methods have provided improved approaches to selecting offsets in complex networks, demonstrating capacity improvements of 25 to 27 percent in real applications. However, these improvements must be understood as redistributions of limited capacity rather than absolute increases in network capacity, with benefits concentrated on coordinated movements while other movements experience corresponding reductions.

Future directions for research and practice include developing adaptive offset strategies that respond in real-time to variations in actual arrival patterns, incorporating vehicle-to-infrastructure communication to provide more granular information about arrival distributions, and developing hybrid strategies that balance vehicular capacity optimization with pedestrian safety and transit operations. The fundamental insight emerging from analysis of phase offset effects under random arrivals is that coordination benefits are inherently limited by the variability of real traffic patterns, and that no single fixed offset value can simultaneously optimize capacity distribution across all movement types, directions, and time periods.

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Green wave - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Green_wave'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Green Wave as an Integral Part for the Optimization of Traffic ... - arXiv', 'url': 'https://arxiv.org/html/2507.22511'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Traffic Signal Timing Manual: Chapter 6 - FHWA Operations', 'url': 'https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] signalized intersections - Traffic Flow Theory', 'url': 'https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'What is Green Wave and How Does it Work? - Sinowatcher', 'url': 'https://www.trafficsolution.cn/what-is-green-wave-and-how-does-it-work/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] CHAPTER 4 TRAFFIC SIGNAL DESIGN – OPERATIONS ... - TN.gov', 'url': 'https://www.tn.gov/content/dam/tn/tdot/traffic-engineering/tdmanualrewrite/CHAPTER%204%20-%20TRAFFIC%20SIGNAL%20DESIGN%20-%20OPERATIONS%20AND%20COORDINATION.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Traffic Signal Timing Manual: Chapter 3 - FHWA Operations', 'url': 'https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter3.htm'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Introduction to Intersection Control', 'url': 'http://www.ce.memphis.edu/4162/L16_Progression.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Use of Poisson Distribution in Highway Traffic - ROSA P', 'url': 'https://rosap.ntl.bts.gov/view/dot/16299/dot_16299_DS1.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '6.2: Traffic Signals - Engineering LibreTexts', 'url': 'https://eng.libretexts.org/Bookshelves/Civil_Engineering/Fundamentals_of_Transportation/06:_Traffice_Control/6.02:_Traffic_Signals'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Traffic Signal Timing Manual: Chapter 6 - FHWA Operations', 'url': 'https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] An optimization modeling of coordinated traffic signal control based ...', 'url': 'https://pdfs.semanticscholar.org/19cd/2b1b068d7ed3af3b9c6bc4c4c75d72681fbf.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Offset Optimization For a Network of Signalized Intersections via ...', 'url': 'https://coogan.ece.gatech.edu/papers/pdf/coogan2015offset.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Queue Length Estimation for Signalized Intersections under Partially ...', 'url': 'https://onlinelibrary.wiley.com/doi/10.1155/2022/9568723'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Chapter: Appendix C: Arterial Signal Spacing for Coordination', 'url': 'https://www.nationalacademies.org/read/27897/chapter/7'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Traffic Signal Timing Manual: Chapter 6 - FHWA Operations', 'url': 'https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] signalized intersections - Traffic Flow Theory', 'url': 'https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Reconciled Platoon Accommodations at Traffic Signals', 'url': 'https://docs.lib.purdue.edu/jtrp/178/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Traffic Signal Timing Manual: Chapter 6 - FHWA Operations', 'url': 'https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Offset Selection for Bandwidth Maximization on Multiple Routes', 'url': 'https://horowitz.me.berkeley.edu/Publications_files/All_papers_numbered/Mehr_Bandwidth_Maximization_Multiple_Routes_ACC2018.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Traffic Signal Optimization and Coordination in Connected Cities', 'url': 'https://c2smart.engineering.nyu.edu/wp-content/uploads/2018/07/TrafficSignalOptimizationinConnectedCities-FinalReport.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '24.1 Basic Concepts - BRT Planning Guide', 'url': 'https://brtguide.itdp.org/branch/master/guide/intersections-and-signal-control/basic-concepts'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Comparison of Flow- and Bandwidth-Based Methods of Traffic ...', 'url': 'https://ascelibrary.com/doi/10.1061/JTEPBS.TEENG-7404'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Signal Timing and Coordination Strategies Under Varying Traffic ...', 'url': 'https://rosap.ntl.bts.gov/view/dot/35439/dot_35439_DS1.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Offset Optimization For a Network of Signalized Intersections via ...', 'url': 'https://coogan.ece.gatech.edu/papers/pdf/coogan2015offset.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] signalized intersections - Traffic Flow Theory', 'url': 'https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Traffic Signal Timing Manual: Chapter 6 - FHWA Operations', 'url': 'https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Signal Timing Under Saturated Conditions: Chapter 2. The State of ...', 'url': 'https://ops.fhwa.dot.gov/publications/fhwahop09008/chapter2.htm'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Green Wave as an Integral Part for the Optimization of Traffic ... - arXiv', 'url': 'https://arxiv.org/html/2507.22511'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Signal Timing and Coordination Strategies Under Varying Traffic ...', 'url': 'https://rosap.ntl.bts.gov/view/dot/35439/dot_35439_DS1.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Offset Optimization For a Network of Signalized Intersections via ...', 'url': 'https://coogan.ece.gatech.edu/papers/pdf/coogan2015offset.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] chapter 2 state-of-the-art in delay, queue and stop estimation', 'url': 'https://vtechworks.lib.vt.edu/bitstream/handle/10919/27030/Chapter02.pdf?sequence=2'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Impact of Timing and Frequency Offsets on Multicarrier Waveform ...', 'url': 'https://arxiv.org/pdf/1505.00800.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Traffic Signal Timing Manual: Chapter 3 - FHWA Operations', 'url': 'https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter3.htm'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Traffic Signal Timing Manual: Chapter 6 - FHWA Operations', 'url': 'https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Modeling Individual Differences in the Timing of Change Onset ... - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8957627/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Green wave - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Green_wave'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Offset Optimization in Signalized Traffic Networks via Semidefinite ...', 'url': 'https://coogan.ece.gatech.edu/papers/pdf/coogan2016offsetoptimization.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] signalized intersections - Traffic Flow Theory', 'url': 'https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Green Wave as an Integral Part for the Optimization of Traffic ... - arXiv', 'url': 'https://arxiv.org/html/2507.22511'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'An offset optimization approach for coordinated signal systems with ...', 'url': 'https://journals.sagepub.com/doi/10.1177/1687814016637825'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Part 3. Capacity of Signalized Intersections', 'url': 'https://onlinepubs.trb.org/Onlinepubs/trr/1978/667/667-003.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Signalized Intersections: Informational Guide, August 2004', 'url': 'https://www.fhwa.dot.gov/publications/research/safety/04091/10.cfm'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Signal Timing Under Saturated Conditions: Chapter 1. Literature ...', 'url': 'https://ops.fhwa.dot.gov/publications/fhwahop09008/chapter1.htm'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] APPLICATION OF THE STOCHASTIC OPTIMIZATION METHOD IN ...', 'url': 'https://vtrc.virginia.gov/media/vtrc/vtrc-pdf/vtrc-pdf/09-cr3.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Operational Applications of Signalized Offset T- Intersections', 'url': 'https://connect.ncdot.gov/projects/research/RNAProjDocs/2019-31FinalReport.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] BETTER USE OF SIGNALS UNDER OVERSATURATED FLOWS', 'url': 'https://onlinepubs.trb.org/Onlinepubs/sr/sr153/153-008.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] signalized intersections - Traffic Flow Theory', 'url': 'https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Traffic Signal Timing Manual: Chapter 6 - FHWA Operations', 'url': 'https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Chapter 7 - Signalized Intersections: Informational Guide, August 2004', 'url': 'https://www.fhwa.dot.gov/publications/research/safety/04091/07.cfm'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Opportunities for Detector-Free Signal Offset Optimization with ...', 'url': 'https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1007&context=civeng'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Progression Factors for Traffic-Actuated Signals', 'url': 'https://onlinepubs.trb.org/Onlinepubs/trr/1988/1194/1194-017.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Signal Coordination: Are We Really Coordinating For All Users?', 'url': 'https://www.kittelson.com/ideas/pros-and-cons-of-signal-coordination/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'An offset optimization approach for coordinated signal systems with ...', 'url': 'https://journals.sagepub.com/doi/10.1177/1687814016637825'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Gaussian Processes for Flight Delay Prediction: Learning a ...', 'url': 'https://arc.aiaa.org/doi/10.2514/1.I011539'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Traffic Signal Timing Manual: Chapter 6 - FHWA Operations', 'url': 'https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Migratory herbivorous waterfowl track multiple resource waves ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11463213/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Investigation, Modeling, and Analysis of Integrated Metroplex Arrival ...', 'url': 'https://ntrs.nasa.gov/api/citations/20120002938/downloads/20120002938.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Progression Factors for Traffic-Actuated Signals', 'url': 'https://onlinepubs.trb.org/Onlinepubs/trr/1988/1194/1194-017.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A test of the green wave hypothesis in omnivorous brown bears ...', 'url': 'https://nsojournals.onlinelibrary.wiley.com/doi/full/10.1111/ecog.06549'}}

## Sources
https://en.wikipedia.org/wiki/Green_wave
https://arxiv.org/html/2507.22511
https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm
https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf
https://www.trafficsolution.cn/what-is-green-wave-and-how-does-it-work/
https://www.tn.gov/content/dam/tn/tdot/traffic-engineering/tdmanualrewrite/CHAPTER%204%20-%20TRAFFIC%20SIGNAL%20DESIGN%20-%20OPERATIONS%20AND%20COORDINATION.pdf
https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter3.htm
http://www.ce.memphis.edu/4162/L16_Progression.pdf
https://rosap.ntl.bts.gov/view/dot/16299/dot_16299_DS1.pdf
https://eng.libretexts.org/Bookshelves/Civil_Engineering/Fundamentals_of_Transportation/06:_Traffice_Control/6.02:_Traffic_Signals
https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm
https://pdfs.semanticscholar.org/19cd/2b1b068d7ed3af3b9c6bc4c4c75d72681fbf.pdf
https://coogan.ece.gatech.edu/papers/pdf/coogan2015offset.pdf
https://onlinelibrary.wiley.com/doi/10.1155/2022/9568723
https://www.nationalacademies.org/read/27897/chapter/7
https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm
https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf
https://docs.lib.purdue.edu/jtrp/178/
https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm
https://horowitz.me.berkeley.edu/Publications_files/All_papers_numbered/Mehr_Bandwidth_Maximization_Multiple_Routes_ACC2018.pdf
https://c2smart.engineering.nyu.edu/wp-content/uploads/2018/07/TrafficSignalOptimizationinConnectedCities-FinalReport.pdf
https://brtguide.itdp.org/branch/master/guide/intersections-and-signal-control/basic-concepts
https://ascelibrary.com/doi/10.1061/JTEPBS.TEENG-7404
https://rosap.ntl.bts.gov/view/dot/35439/dot_35439_DS1.pdf
https://coogan.ece.gatech.edu/papers/pdf/coogan2015offset.pdf
https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf
https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm
https://ops.fhwa.dot.gov/publications/fhwahop09008/chapter2.htm
https://arxiv.org/html/2507.22511
https://rosap.ntl.bts.gov/view/dot/35439/dot_35439_DS1.pdf
https://coogan.ece.gatech.edu/papers/pdf/coogan2015offset.pdf
https://vtechworks.lib.vt.edu/bitstream/handle/10919/27030/Chapter02.pdf?sequence=2
https://arxiv.org/pdf/1505.00800.pdf
https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter3.htm
https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm
https://pmc.ncbi.nlm.nih.gov/articles/PMC8957627/
https://en.wikipedia.org/wiki/Green_wave
https://coogan.ece.gatech.edu/papers/pdf/coogan2016offsetoptimization.pdf
https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf
https://arxiv.org/html/2507.22511
https://journals.sagepub.com/doi/10.1177/1687814016637825
https://onlinepubs.trb.org/Onlinepubs/trr/1978/667/667-003.pdf
https://www.fhwa.dot.gov/publications/research/safety/04091/10.cfm
https://ops.fhwa.dot.gov/publications/fhwahop09008/chapter1.htm
https://vtrc.virginia.gov/media/vtrc/vtrc-pdf/vtrc-pdf/09-cr3.pdf
https://connect.ncdot.gov/projects/research/RNAProjDocs/2019-31FinalReport.pdf
https://onlinepubs.trb.org/Onlinepubs/sr/sr153/153-008.pdf
https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf
https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm
https://www.fhwa.dot.gov/publications/research/safety/04091/07.cfm
https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1007&context=civeng
https://onlinepubs.trb.org/Onlinepubs/trr/1988/1194/1194-017.pdf
https://www.kittelson.com/ideas/pros-and-cons-of-signal-coordination/
https://journals.sagepub.com/doi/10.1177/1687814016637825
https://arc.aiaa.org/doi/10.2514/1.I011539
https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm
https://pmc.ncbi.nlm.nih.gov/articles/PMC11463213/
https://ntrs.nasa.gov/api/citations/20120002938/downloads/20120002938.pdf
https://onlinepubs.trb.org/Onlinepubs/trr/1988/1194/1194-017.pdf
https://nsojournals.onlinelibrary.wiley.com/doi/full/10.1111/ecog.06549