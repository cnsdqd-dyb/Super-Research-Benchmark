# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 6f7a14e9 | **Time:** 372.47s | **Cost:** $1.47935
--------------------------------------------------------------------------------

# The Effect of Green Wave Phase Offset on Intersection Capacity Distribution Under Random Arrival Patterns

### Key Points
*   **Diminished Utility of Offsets under Randomness:** Research indicates that when vehicle arrival patterns are truly random (Poisson distributed) and unrelated to upstream signal operations, the phase offset has a negligible direct impact on the average intersection capacity or delay. In such scenarios, the probability of arrival is uniform throughout the cycle, meaning shifting the green window (offset) captures the same volume of traffic regardless of its position [cite: 1, 2, 3].
*   **Capacity Distribution and Stochastic Variation:** While the *average* capacity remains largely unaffected by offsets under random arrivals, the *distribution* of capacity (specifically the probability of cycle failure or overflow) can still be influenced by offsets if the randomness leads to queue spillback from downstream intersections. Poor offsets in high-saturation random flow can exacerbate storage constraints, leading to blockage that effectively reduces the usable capacity of the upstream intersection [cite: 4, 5, 6].
*   **The Role of Platoon Dispersion:** The effectiveness of green wave offsets is inversely proportional to the degree of platoon dispersion. As traffic moves further from an upstream source, platoons decay into random arrival patterns. Consequently, the "green wave" benefit—and the sensitivity of capacity to phase offset—decreases significantly as the arrival pattern shifts from deterministic (platooned) to stochastic (random) [cite: 7].
*   **Operational Efficiency vs. Theoretical Capacity:** While the theoretical saturation flow (hard capacity) is invariant to offset, the *operational efficiency* (throughput) can be compromised. Even with random arrivals, dynamic offsets are sometimes employed in adaptive systems to prevent "mismatched ranges" where residual queues from stochastic variations block effective green time, thereby altering the realized capacity distribution [cite: 8, 9].

## 1. Introduction

The optimization of urban traffic networks relies heavily on the precise coordination of traffic signals to maximize throughput and minimize delay. A central concept in this domain is the "Green Wave," a coordination strategy designed to allow continuous traffic flow over multiple intersections by synchronizing the green phases of consecutive signals. The critical parameter governing this synchronization is the **phase offset**—the time difference between the initiation of the green phase at a downstream intersection relative to an upstream reference.

While the benefits of green wave coordination are well-documented for coherent platoons of traffic, the interaction between phase offsets and **intersection capacity distribution** becomes complex and less intuitive when traffic exhibits **random arrival patterns**. Random arrivals typically occur when intersections are widely spaced, when friction factors (such as parking maneuvers or side-street entries) disrupt flow, or when traffic volumes are low to moderate. Under these conditions, the deterministic assumptions of traditional coordination models often fail.

This report provides an exhaustive analysis of how green wave phase offsets influence intersection capacity distribution specifically under the constraint of random arrival patterns. It synthesizes findings from traffic flow theory, queueing models, and recent empirical studies to determine the extent to which coordination remains relevant when the arrival profile lacks a defined structure.

### 1.1 Defining the Core Concepts

To rigorously analyze the subject, it is necessary to define the operational parameters:

*   **Green Wave (Signal Coordination):** A control strategy where offsets are calculated based on vehicle speed and intersection spacing to ensure that a platoon of vehicles released from an upstream intersection arrives at the downstream intersection during the green interval [cite: 4, 9, 10].
*   **Phase Offset:** The temporal displacement, usually measured in seconds or as a percentage of the cycle length, between the start of the green phase at two adjacent intersections [cite: 5, 11].
*   **Intersection Capacity:** In signalized contexts, this is generally defined as the maximum rate at which vehicles can pass through the intersection under prevailing conditions. It is a function of the saturation flow rate ($S$) and the effective green ratio ($g/C$) [cite: 7]. However, capacity is not a static value; it follows a probability distribution due to stochastic variations in driver behavior, headways, and start-up lost times [cite: 7, 12].
*   **Random Arrival Patterns:** A traffic flow state where the arrival time of any vehicle is independent of the vehicle preceding it, typically modeled by a Poisson distribution. This stands in contrast to "platooned" arrivals, which are cyclic and dependent on upstream signal timing [cite: 1, 2].

### 1.2 The Research Problem

The primary motivation for this analysis arises from the discrepancy between theoretical signal timing models and real-world operational realities. Most coordination tools (e.g., TRANSYT, SCOOT) attempt to optimize offsets to maximize the "green bandwidth." However, if the arrival pattern is random, the concept of a "bandwidth" becomes theoretical rather than practical. The query seeks to understand if manipulating the offset in such a stochastic environment yields any change in the capacity distribution—specifically, whether it can mitigate the risk of capacity breakdown (oversaturation) or if it is a mathematically futile exercise.

## 2. Theoretical Framework of Signal Coordination and Capacity

To understand the effect of offsets on capacity distribution, one must first establish how capacity is derived and how coordination is intended to function under ideal conditions.

### 2.1 The Deterministic Capacity Model

The standard capacity ($c$) of a signalized lane group is traditionally calculated using the equation:

\[ c = S \times \frac{g}{C} \]

Where:
*   $S$ is the saturation flow rate (vehicles per hour of green).
*   $g$ is the effective green time.
*   $C$ is the cycle length.

In this deterministic formulation, capacity is entirely dependent on the *duration* of the green signal ($g$) and the cycle length ($C$). The **phase offset** does not appear in this fundamental equation [cite: 1, 7]. This suggests that, at a macroscopic level, shifting the start time of the green phase (changing the offset) does not alter the total amount of green time available, and therefore should not alter the theoretical capacity of the intersection.

### 2.2 The Role of Offset in Platoon Progression

While offset does not change the *supply* of capacity (the $g/C$ ratio), it critically affects the *demand* profile arriving during that capacity window. In a coordinated system, the objective of the offset is to align the arrival of the high-density platoon with the availability of the green window.

*   **Good Offset:** The platoon arrives just as the green starts. The full saturation flow rate ($S$) is utilized immediately, and stops are minimized.
*   **Bad Offset:** The platoon arrives during the red phase. Vehicles must stop and queue. When the green eventually starts, capacity is lost due to "start-up lost time" (the time required for the queue to accelerate) [cite: 7, 13].

Therefore, in platooned flow, the offset indirectly influences the *effective* capacity by minimizing lost time and preventing queue spillback. However, this mechanism relies entirely on the existence of a platoon.

### 2.3 Capacity as a Probability Distribution

Modern traffic theory recognizes that capacity is not a fixed number but a random variable following a **capacity distribution**, $P(C)$. This distribution arises from:
1.  Variability in saturation flow ($S$) due to driver heterogeneity.
2.  Variability in effective green time ($g$) due to pedestrian interference or actuation.
3.  Stochastic blockage events.

Research indicates that the capacity distribution is often modeled using Weibull or triangular distributions rather than a uniform distribution [cite: 12, 14]. The "capacity" of an intersection is thus better described as the probability that the intersection can service a given demand volume without failure (overflow). The query essentially asks: *Does the phase offset parameter shift the mean or variance of this capacity distribution when arrivals are random?*

## 3. Characteristics of Random Arrival Patterns

The nature of the arrival pattern is the independent variable that fundamentally alters the physics of the green wave.

### 3.1 The Poisson Arrival Process

Random arrivals are typically described by a Poisson process, where the number of vehicle arrivals in any given time interval follows a Poisson distribution. This implies:
*   The variance of the number of arrivals is equal to the mean.
*   The arrival time of the next vehicle is independent of the previous one.
*   The probability of a vehicle arriving is uniform across the cycle length [cite: 7, 15].

### 3.2 Causes of Randomness in Urban Networks

Traffic flow tends to revert to a random state due to **platoon dispersion**. As vehicles travel away from an upstream signal, differences in driver speeds cause the tightly grouped platoon to spread out. The Robertson Platoon Dispersion model, used in TRANSYT, quantifies this decay.

\[ q_{out}(t) = F \times q_{in}(t - T) + (1 - F) \times q_{out}(t - 1) \]

Where $F$ is a smoothing factor. When dispersion is high (due to long distances, side friction, or mid-block entries), the flow profile at the downstream intersection flattens.
Additionally, if the upstream intersection is unsignalized, or if the traffic volume is low, the flow naturally assumes a random distribution [cite: 1, 16].

### 3.3 The "No-Wave" Phenomenon

In a scenario of purely random arrivals, there is no distinct "peak" or "platoon" in the cyclic flow profile. The arrival rate $q(t)$ is effectively constant (or fluctuates stochastically around a mean) throughout the red and green intervals.
Consequently, the concept of a "Green Wave" loses its physical basis. A green wave relies on surfing a peak of traffic; if the "water level" (traffic flow) is flat, there is no wave to surf [cite: 3, 13].

## 4. The Effect of Phase Offset Under Random Arrivals

Based on the synthesis of the provided research, the effect of phase offset on intersection capacity distribution under random arrival patterns can be categorized into primary (direct) and secondary (indirect) effects.

### 4.1 Primary Effect: Negligible Impact on Average Capacity

The consensus in the literature is that when arrivals are random and unrelated to upstream operations, coordination (and thus offset optimization) provides **little to no benefit** regarding the primary performance measures of delay and capacity utilization.

*   **Uniform Probability of Arrival:** Since vehicles are equally likely to arrive at any point in the cycle, shifting the green window (changing the offset) does not change the number of vehicles captured by the green phase. The integral of the arrival rate over the green duration remains constant regardless of the time shift $t$ [cite: 1, 2].
*   **Ineffectiveness of Progression:** Source [cite: 1] explicitly states: "If vehicle arrivals tend to be random and are unrelated to the upstream intersection operation, then coordination may provide little benefit to the system operation."
*   **Delay Components:** Total delay is the sum of Uniform Delay and Random (Overflow) Delay.
    *   *Uniform Delay:* Derived from the assumption of uniform arrivals. It is insensitive to offset in the absence of platoons.
    *   *Random Delay:* Caused by cycle-to-cycle fluctuations in arrival volume (Poisson variance). Source [cite: 7] notes that "the signal offset does not appear to influence the overflow delay component." Since random delay is the dominant factor in stochastic arrival scenarios, offset adjustments fail to mitigate the delays caused by randomness.

### 4.2 Secondary Effect: Interaction with Queue Dynamics

While the *average* throughput may not change, offsets can influence the *distribution* of capacity through queue interaction effects, particularly in networks with limited storage.

#### 4.2.1 Prevention of Downstream Blockage (Spillback)
Even with random arrivals, if the traffic volume is high, queues will form during the red phase. If the distance between intersections is short, these queues can spill back and block the upstream intersection.
*   **Storage Capacity Constraints:** Source [cite: 5] highlights that original models often assumed infinite storage, but realistic models must account for storage capacity.
*   **Offset as a Queue Management Tool:** In random arrival scenarios with high saturation, the offset can be used not to facilitate a "green wave" (progression), but to manage queue growth. By adjusting the offset, engineers can ensure the downstream green opens *before* the upstream queue fills the link, effectively clearing space. This prevents the "capacity" of the upstream intersection from dropping to zero due to exit blockage [cite: 4, 8].
*   **Unequal Cycle Lengths:** Source [cite: 8] notes that at intersections with unequal cycles (which effectively creates random/shifting offsets), periodic phase offsets can cause queue lengths to increase significantly. This implies that maintaining a specific offset relationship—even if arrivals are random—might be necessary to prevent extreme queue events that degrade capacity.

#### 4.2.2 "Waste" of Green Time
Source [cite: 4] discusses the phenomenon where vehicles arriving from a merging direction must stop if they arrive before the downstream green starts. In a random arrival scenario, there is always a probability of vehicles arriving "early."
*   If the offset is set such that the green starts too late relative to the average queue accumulation, the effective green time is utilized fully, but the queue may not clear (cycle failure).
*   If the offset is set such that green starts when no queue is present (and arrivals are sparse/random), that portion of green time is "wasted" (starvation).
*   Therefore, even with random arrivals, an offset that aligns the green start with the *expected value* of queue accumulation (derived from the mean arrival rate) can slightly optimize the capacity distribution by reducing the variance of unused green time [cite: 4].

### 4.3 The "Random Delay" Component and Offset

The Highway Capacity Manual (HCM) and other theoretical models (Webster, Akcelik) separate delay into deterministic and random components.
*   **Deterministic Component:** Assumes uniform arrivals. In coordinated systems, this component is highly sensitive to offset (platoon arrival vs. red arrival).
*   **Random Component:** Accounts for the probability that arrivals > capacity ($x > 1$) for a specific cycle.
*   **Research Finding:** Source [cite: 7] and [cite: 7] confirm that "the signal offset does not appear to influence the overflow delay component." This is a critical finding. Since the random arrival pattern drives the overflow delay, and offset cannot predict or synchronize with random fluctuations, offset manipulation is powerless to reduce the random component of delay or the probability of stochastic capacity breakdown.

## 5. Capacity Distribution Analysis

To deepen the analysis, we must look at how the **capacity distribution** itself behaves. The capacity distribution $P(C)$ represents the probability density of the intersection's service rate.

### 5.1 Stationarity of the Distribution under Randomness

Under random arrival patterns, the arrival process $A(t)$ is stationary (its statistical properties do not change over time). Consequently, the interaction between the arrival process and the service process (the signal cycle) produces a stationary queue length distribution.
*   Changing the phase offset corresponds to a time-shift operation $A(t + \Delta)$.
*   For a stationary Poisson process, the statistical properties of $A(t + \Delta)$ are identical to $A(t)$.
*   **Conclusion:** The theoretical capacity distribution $P(C)$ remains invariant to phase offset changes under strictly stationary random arrivals. The probability of the intersection being oversaturated ($P(Demand > Capacity)$) does not change because the demand profile is flat [cite: 7, 17].

### 5.2 Deviations from Theory: The "Pseudo-Random" Reality

In real-world scenarios, "random" arrivals are rarely perfectly Poisson. They often exhibit:
1.  **Short-term correlations:** Small bunches of vehicles due to car-following behavior.
2.  **Time-dependent means:** Arrival rates $q$ change over 15-minute intervals.

In these "pseudo-random" cases, a weak relationship between offset and capacity distribution may emerge.
*   **Source [cite: 17]** notes that while fixed control performance varies with offset, semi-actuated control (which responds to random arrivals) is less sensitive. This suggests that if the control logic is fixed (Green Wave), offset settings might accidentally align with recurring micro-patterns in the "random" flow, creating slight variations in capacity performance.
*   **Source [cite: 8]** proposes a "multi-strategy combined vehicle-road coordinated control method" to handle unequal-cycle intersections (which mimic random offsets). The study found that dynamic offset adjustment could reduce queuing and "early arrival," implying that active management of offsets can improve conditions even when the cyclic relationship is weak or fluctuating.

## 6. Comparative Scenarios

To illustrate the effect, we compare the impact of offset in three distinct scenarios derived from the literature.

### 6.1 Scenario A: Strong Platooning (Baseline)
*   **Condition:** Closely spaced intersections, high volume, fixed cycle.
*   **Offset Effect:** Critical. Correct offset maximizes capacity utilization; incorrect offset causes shockwaves and capacity reduction due to blockage.
*   **Capacity Distribution:** Highly sensitive. The distribution shifts significantly based on offset choice.

### 6.2 Scenario B: Pure Random Arrivals (The Query's Focus)
*   **Condition:** Isolated intersection or very long link length, Poisson arrivals.
*   **Offset Effect:** Negligible.
*   **Mechanism:** The "Green Wave" does not exist. The probability of a vehicle arriving during green is simply $g/C$, regardless of when the green starts.
*   **Capacity Distribution:** Invariant. The risk of oversaturation is determined solely by the cycle length and green split, not the offset [cite: 1, 3].

### 6.3 Scenario C: Random Arrivals with Downstream Constraints
*   **Condition:** Random arrivals, but short link to the *next* intersection.
*   **Offset Effect:** Moderate (for Queue Management).
*   **Mechanism:** While the *arrival* at the subject intersection is random, the *departure* is constrained by the downstream signal. If the offset between the subject and downstream signal is poor, the subject intersection's capacity is truncated by spillback.
*   **Capacity Distribution:** The tail of the capacity distribution (probability of zero capacity) increases if the offset causes downstream blockage. Thus, offset optimization is required not for *progression* (catching the wave) but for *clearance* (avoiding the wall) [cite: 4, 5].

## 7. Advanced Control Strategies and Future Directions

Recent research suggests that while traditional fixed offsets offer little for random arrivals, dynamic or adaptive offsets can extract benefits.

### 7.1 Adaptive Signal Control (SCOOT/SCATS)
Adaptive systems do not rely on a fixed "Green Wave" for random traffic. Instead, they use real-time data to adjust offsets cycle-by-cycle.
*   **Source [cite: 9]** and **[cite: 18]** mention that systems like SCOOT optimize offsets to minimize stops. In random traffic, this might involve small offset shifts to accommodate "micro-platoons" or random bunches detected by upstream sensors.
*   **Effect:** This transforms the "random" arrival problem into a "predictable" one over very short time horizons (seconds), allowing the offset to temporarily increase capacity utilization for that specific cycle.

### 7.2 Vehicle-Road Collaboration
Source [cite: 8] and [cite: 8] discuss "vehicle-road coordinated control." In this paradigm, connected vehicles can communicate their random arrival times to the signal controller.
*   **Dynamic Offset Adjustment:** The controller can adjust the offset (or extend the green) to "catch" a randomly arriving group of vehicles.
*   **Speed Guidance:** Conversely, the infrastructure can tell randomly arriving vehicles to speed up or slow down to create a *synthetic platoon* that matches the green wave.
*   **Result:** This effectively converts random arrival patterns into coordinated patterns, making the phase offset a highly relevant parameter for capacity distribution once again [cite: 8, 19].

## 8. Conclusion

The effect of green wave phase offset on intersection capacity distribution under random arrival patterns is characterized by a **decoupling of the coordination benefit**.

1.  **Theoretical Invariance:** Under strict assumptions of Poisson random arrivals and infinite storage, the phase offset has **no statistically significant effect** on the capacity distribution. The probability of utilizing the green phase is uniform, rendering the timing of the green window irrelevant to the aggregate throughput [cite: 1, 3, 7].
2.  **Operational Constraints:** In practical applications, the "random" nature of traffic does not eliminate physical constraints. If the random flow is heavy enough to cause queuing, phase offsets remain relevant for **queue management** to prevent spillback from downstream intersections. In this specific context, an optimized offset preserves the capacity distribution by preventing blockage, even if it does not facilitate progression [cite: 4, 5].
3.  **Transition to Actuation:** Because fixed offsets provide little benefit for random arrivals, the industry standard is to abandon fixed "Green Wave" strategies in favor of **actuated** or **adaptive** control for such scenarios. These methods rely on detection rather than prediction (offsets), confirming that fixed offsets are the wrong tool for random arrival patterns [cite: 9, 20].

In summary, for a traffic engineer managing an intersection with random arrival patterns, adjusting the green wave phase offset will yield **negligible returns** in terms of capacity distribution, unless the adjustment is specifically targeted at mitigating downstream queue spillback. The "Green Wave" phenomenon physically ceases to exist when the arrival profile flattens into randomness.

## 9. Detailed Analysis of Source Material and Methodologies

### 9.1 Analysis of Delay Models
The conclusion that offsets are irrelevant for random arrivals is mathematically supported by the structure of delay models.
*   **Webster’s Model:** $d = \frac{c(1-g/C)^2}{2(1-g/C \cdot x)} + \frac{x^2}{2q(1-x)}$. The first term (Uniform Delay) assumes uniform arrivals. The second term (Random Delay) assumes Poisson arrivals. Neither term contains a variable for offset. Offset only enters the equation when a "Progression Factor" (PF) is applied (as in HCM).
*   **HCM Progression Factor:** $PF = \frac{(1-P)f_p}{1-g/C}$. Here, $P$ is the proportion of vehicles arriving on green. For random arrivals, $P \approx g/C$. Substituting this into the equation yields a PF close to 1.0, indicating that the delay (and by extension, capacity efficiency) is the same as an isolated signal. This mathematically proves the insensitivity of performance to offset under random conditions [cite: 7].

### 9.2 Empirical Evidence from Simulation Studies
*   **Source [cite: 4] (2024):** Investigated offsets at intersections with different capacities. Found that "applying coordinated control strategies... may have either a positive or negative impact." However, this was in the context of *transitioning* cycles, which introduces artificial randomness.
*   **Source [cite: 19] (2025):** Compared Green Wave Speed Guidance vs. Eco-Driving. Found that without guidance (random driving), vehicles stopped frequently. Green wave guidance *created* platoons. This supports the inverse finding: offsets only work if you *force* non-randomness (platoons) through speed guidance.
*   **Source [cite: 16]:** Found that "disruption on freeway operations occurs as a result of large platoon arrivals... than as a result of traffic that arrives randomly." This implies that random traffic is *less* sensitive to timing disruptions (and thus timing optimizations like offset) than platooned traffic.

### 9.3 The "Capacity Distribution" Nuance
Source [cite: 12] and [cite: 14] discuss capacity as a distribution.
*   **Weibull/Triangular Models:** Used to describe the probability of capacity $c$.
*   **Impact of Offset:** If offset $O$ is a parameter, does $P(c|O) = P(c)$?
*   **Findings:** The literature does not provide a function linking $O$ to $P(c)$ for random arrivals. This absence of evidence, combined with the theoretical independence of Poisson processes from time shifts, supports the null hypothesis. The distribution of capacity is driven by the *saturation flow distribution* (driver behavior) and *green time distribution* (actuation), not the *start time* (offset) of the green phase.

## 10. Comprehensive Literature Review on Signal Coordination

### 10.1 Evolution of Coordination Theory
*   **Morgan et al. & Gartner et al. [cite: 4]:** Established the bidirectional design and multi-band models. These foundational theories rely on the existence of "bands" (platoons).
*   **Robertson (TRANSYT) [cite: 5, 7]:** Introduced the Platoon Dispersion Factor. As the dispersion factor increases (approaching random flow), the benefits of optimizing offsets in TRANSYT decrease asymptotically to zero.
*   **Modern Adaptive Systems (MARL, etc.) [cite: 10, 21, 22]:** Recent studies using Multi-Agent Reinforcement Learning (MARL) show that for random arrivals (e.g., bus randomness), dynamic adjustments are superior to fixed green waves. Source [cite: 22] notes that with random arrivals, queues fill up, and the system becomes unstable/oversaturated regardless of simple coordination, requiring complex reward functions to manage.

### 10.2 The "Green Wave" in the Absence of Platoons
The term "Green Wave" is a misnomer under random arrivals.
*   **Source [cite: 23]:** Defines Green Wave as moving a "platoon or group of vehicles."
*   **Source [cite: 1]:** States "If vehicle arrivals tend to be random... coordination may provide little benefit."
*   **Implication:** Applying a "Green Wave" offset to random traffic is effectively applying a structured solution to an unstructured problem. The "wave" propagates through the signal system, but there are no ships (platoons) to ride it. The capacity distribution remains governed by the random arrival statistics (Poisson) rather than the deterministic signal timing plan.

### 10.3 Capacity Adjustment Factors
In the Highway Capacity Manual (HCM), capacity is adjusted by factors ($f_w, f_{HV}, f_g, f_p$).
*   $f_p$ (Population factor) and $f_{bb}$ (Bus blockage).
*   There is no $f_{offset}$ for capacity calculation.
*   There *is* a Progression Adjustment Factor ($PF$) for *delay* calculation.
*   This distinction is crucial: **Offset affects Delay, not Capacity.**
*   *Exception:* Blockage. If the offset causes a queue to block the intersection, the *effective* capacity drops. This is the only mechanism by which offset influences capacity distribution under random arrivals [cite: 7].

## 11. Final Synthesis

The query asks for the effect of green wave phase offset on intersection capacity distribution under random arrival patterns.

**The Answer:**
Under the strict definition of random (Poisson) arrival patterns, the green wave phase offset has **no effect** on the intersection capacity distribution. The probability of a vehicle arriving during the green phase is equal to the green ratio ($g/C$) and is independent of the offset. The capacity distribution is determined by the cycle length, green split, and stochastic variations in saturation flow, not by the coordination parameter.

**The Caveat:**
In real-world operations, "random" traffic may still interact with physical constraints. If the offset is set such that it creates a mismatch between the green phase and the clearance of downstream queues (even if those queues formed randomly), it can lead to **upstream blockage**. In this specific case, a poor offset reduces the effective capacity distribution by increasing the probability of blockage events. Therefore, while offset provides no *progression* benefit for random traffic, it retains a *queue management* function to preserve the base capacity of the intersection.

### Table 1: Summary of Offset Effects by Arrival Type

| Arrival Pattern | Primary Goal of Offset | Effect on Delay | Effect on Capacity Distribution |
| :--- | :--- | :--- | :--- |
| **Platooned** | Progression (Green Wave) | High (Reduces Stops/Delay) | **Moderate** (Prevents starvation/lost time) |
| **Random (Low Vol)** | None (Isolated Operation) | Negligible | **None** (Invariant) |
| **Random (High Vol)**| Queue Management | Low | **Low/Moderate** (Prevents spillback/blockage) |

### References
[cite: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

**Sources:**
1. [dot.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGch7PhJbSlEinZJVO_WjL3wKclLl69FN4v0cxDM3R8c_3FD_H6GPVWVfs-m-ldLNBJ8bzc9bv7W4O1Nzkit0R81iZD1T8Iwpn_R2se8apiq9-wWDUBYKBdCFP3dweNsO7fv_ObQLzndZ4XD4FW0Ng58k1ypGw=)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHV0v9xZdE9fU1EeZ3FHMCOozxGBYKSx62RqgH0rsnrax5wB3DOwKdtOlW4eq40qaDOGe5km0K7fdhH7WD462ElGR3TmgP0W7ZIrVXRaT66N2Uq8vtbS7af6siVKGH_guouWD0Jh_aFyMevEyRWBhfLIqyF_jkjgjAec9GWIkY1-XlXmWnLoOAe40sMVumzrPZFoW5pekAKU-S5IoBZK2nNUA-wdcf0HjHSYtnrIiqCg8XPSA==)
3. [nyu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7saFbWthGZhnOp7Y3BnhF3S_k6TEoqrLxfjv54li2mChJWOcpvv22It0zaLzAEXA6_ApI_qs53KF3iZU4WgmHlKoUSIvPwfOQlewf5qOZJ5BLGTKJXy5WElL1t6o7_cF5OhkeasexWeseYk4pN1kRvzUpwfbT11RQHbMC6l0NNLBAY-qlVM2HyvwWvynIO3yrZX_mmGOtEJyYX7iD57FdjlU6ZAFiScEafbhdvOwK)
4. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtMgUBabsVlKU1eLoGKjGU_4SyNAoIU8Z5bfk7jVxa-hj_-aaYRCG1eIylkcXTgmwiIqOvmf-7p-MSCaaMGUp01kpBhfeCDNu4qqEQnIGv5BrxdhDik4k5gl-8FqAOdw==)
5. [gatech.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWRbaoyf3N4n-yQbcSWakCeZ9x5lgDiJyJajKUayOkBopqp-dS3XY8zfjKPnbUTfQ5L9WJ-nuqwUBDRiBEE_ElfMfKWPyZDs3ahQoZjqUMOy80df8wCHdsTK33hjjyHVIlRoJkGuyQxL1Vz_RhwFrrLGc=)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcEWgOiiPI8MstwobEK9UcE0Oh-jQotc_B2Hfu-bEPwxU0NX5w9aO95BgzQE1V_3NjDwTVusJ9e7s_W6NEgHWdpFeBlLUYcQqjlQY_2-WIn05cqb5iVXvAVqMoFmSjYgQX0c6WCKbE00KVqNiffp0BGPDcthqDJ_nEILDLbtynH3Ve-iDIcMkVnm1F9qHyXfdU1i4c_vUUaafz21HjuqktIoiKlWgNKS4C19MOTY9u4ONoIxJ-9Cwf1tpD1A==)
7. [dot.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5FpJjYUXloWy4SuLs6wb63Bzt3ioCt0cC7WABG29nLE8pQl4CSeJhuWvflFg-fsnCi2JVtEQeUaHkCLIk9n3QByr736HFSv7QNI65Jpy1OeAfRU4DTl2CB7KWnNudNx4WdzOKvv4TmMWmY8XohJCaQjbx-9OMv-LlOvZkvQ==)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGePzxB2tzKsNpx_bBcKdNzOp8DkwUOqjOIva5oCdBL3iydlZv59pNgI5NkSE-REpxwrmQkVPx909VGrKI0alU3xGwN4D4CAdPguihDe3-jN4KgWW6FyzvIuuKTIY7HfeuFMFY-F6BfAsLXbgSlq28KtZ24OznzdhP7pohFWZ5Ax76A_EV-kj9bZBGexUt2c1zYF2L_0xo1Xne7ugf4_iVx4VPL_oehwEOYtVgxJ_o-6MlnIBbyedb_0eSJNiWt4vcKzmsP1rjgDUH4woxTaA==)
9. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2ql2slp6kvq5cEv3gTQRJCNYWcCPIrXjxzoXLAt2K1XLM6GPpSV6gqMFaHABbkh8Gh0aMTESVFGrFSHZ3ItX0ZIdY8HXljm__nF0V6rIBsB3rDcilk2A=)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUmSQ843P-p-2loKcCohkxcrnZeJOFmQHs0Ctbt7Uqew5nDVrlboNwaCC-yzyzlEYQSpXaBIGf92X_9VF8sW1WNUJldDGoxJ77GDqJvYe1Nste7_x-2axGsFWgC3uQgjSgZyOepJbc4z-rxUJNU1a7MgsFHp8k13etw-wJc2bOLdiVWLndfXo0pZ2M1oSNraFHF_TW46BNVB3CndA=)
11. [wordpress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkcYCtM5VXQ30NjMHEwc8lrPvk3O3TZcUjaqE8jBmxYfuAMVJbEpWrisW_lLjq-l2bl5dq2p9hzP_RlfO4l-5K4y3J5qYI84h6B8TgprX7rPDV-s9BkSDn584nXC-kBiyNCK5QU75cMUx3vjURLCSiC5T0E8hQxdx_xDwDTVCiesexLA==)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjZUSdg9B7-bw1vARXcGwptV2MXZCG0aWiI5MW5VU66W-69Wt0Er11pDCcbX33rgL6dX3U3bttvLgaqeukvvrSiX87WfH1e6WlFXdteKTPYIYis7yI4kV2B9XtueM6UuhVcnNnO7IF19-v70TGF31Hq9q4EDuHCWslE0C6G4Z6vrYjpEVk2PPadqx1b0-HuEEH8zr9JsdLrQMYIiYcI4x4ExVygUcbOvnotfx74E2imk9FdNzzePbj_WvRHWcroLq8cbxAd22KXRLh1lSV2r5d0DuBVNWF0pDzSKD6LA4joAKIuvPygYNPnfQ=)
13. [kittelson.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9gPydwdY3h4m3fxxXHowXfWeMlCdpkz6-QZupwl9atO1g8p-zx3h4rG31vZ5nploq-RDQAGrrxHBj0uGlXSqsXZQ0Dy3zjIAI5LGl-d-z6zFPk7ImyslUgq52cWPrcAjbq3fGqE66NDff0pWMSVbYI0hJCo2IGEUo-eY=)
14. [trb.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKETW3_UQPzycRJB50wYytWyZIUqpIn_zopo-cQFg_cmGWmcAY5ARrgtJqPiQW_7NAgdonnzyS0vRLJ3v6KBQRHcC1V27XPmXQT7KEhqlhjiR44XVIz0ujbaPn6tWP_6uG78z_ZlsQ4FYvHm0pzd8=)
15. [dot.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrQfV8dLfO1etGJg95XNP57hlaZZp-QEMAFmwBdUmOpnsJEgXFUXNuwrmoor8vY0-ZAgmgTItZJ8u7SXoBby_gDwA5bjnzh9NMIVOurXbm-f6qUlAxOGc-PbpMRbTFRyg4DLJdbD0KUjUpeIgTF62uLJIdzMt0_qBLldBwgw==)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7PZ9q-lJw-nZh-j9DAspt9m_5UO6ynco801OvkmXmy0w9yRIFBvYZEAwKzn55UIPngC_zN1ei68g9FXSS57OS4NYwxU3nmSYWL41cv6j1nSPV_N7CY7ZwdCjpiBF_ZpcOm68yThePcOt1XDAOYRQkQ-GoPd3dERcBGK5KRGhQlOH-B1RAW7QT9bcNshB17n0VGGIqFH-cc-gDroKack50JlxmLwPMSYdoYYZzbbwOT5WZSr8j9f_X2IHMQU6HQogRqCruHtHWm8tUNoX-VZAQPJ3yobSD5vVeS0j-vGPe61iTQGQ=)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGW8pPrOMh8FHmCU7RWgmqK_ySD3NcQaro_2MaGJZOQFRYnVFruzTr5jzg1ttbw3ekZ8IA0tOaqn_sTexSfxcsYndUDRXpP_No2x536BTSd_xPUqSwztnj9N0kOsN3DxEuwAYzMvlSuAE2DGZzaycGctV5Ffy_b6IBH5yCIfMLWaruSsf-3jFyYlsAXeX-rU_kfvJoi3MolSwlXfAtt0xfzmVlGEaBBq1xCnEQ8kbHt)
18. [taylorandfrancis.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuCZ_iuVl6MgBKG2ApLmsMBzIn56hINPjCv1UO2QX3MPNlCLG-JJxcqC11y_0iqL1Yq1qliCdxIzmQImaeLpodwhgKkYY1eht4cU_wvemk9xdbyPWbDFkSG3T9bXVTtXz0znI98dAhGX5u0h-bZwRN9AFaUgtBQpffLP0jrM5oG4XrGOJMkVLKQP_tEpFOt0mGP53QPTzoKCie)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5JQEaUlD269sXb3dQUuZq9OyzgMoo1PM4lQ1BUMrZ3U5UQbMp1SWbxJXybLcyoi9CJb2YOe_qdC06Uw2TQDzYE8AEa9aQCYK2eouE735NhwkR4QxsTdFZ8omsX0al5-77zzpRxXZkwgLm11nEWDbn5a4uUTnnmWzjESoaA_sKzZcfZGDfMeSsTSBZDkIC66CyvWIrYJwjtgWLWQk4aW24glXQ2dsUw0L9wIYSGrvP-XnvxDVNargkM2TtS-3Kuoswz6FtS7zaoEABUIYjc-erLRJbVcQXjPM4JjRJjw==)
20. [neu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNg5pQJEIzPAO7VJlJFMMrWTlp8x8v-ffq36pE3U-JDPoJN5NkrjkPQgDab8mUo_NBiCMIejccI-gBC-STHM3p6YmxkpP-64ac_7kPmSQ7B9EqVjHhxoaiAMeO7DB6M1-xhLMNGZrga45BQ9okoKSP-FJoeJYqKkFhng3cOBM_yn5TUJygKZZz9Z7KCHXkqykv-40HKHLMORTvvdvQOLem7WkdabpuruP8XDLjg5X6VfvEF-t-NU-Dav3Y19775FIMPz_KGXd1gJmDNWS7xW8I8GEn0QQpJZq8Dr_06OHLWFc7KB9MnSzCDnDUted5pHDmNxyzLY7DjepbxZro-vGrqcLnOOc=)
21. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8njRhNy87_PI-FuwHIHyZYmIumKwyZ6S82cKKGbRsggEnkfY5FP-Uj76f6OHxL6-7Kxxtyoc0oqYRDzMEw5zmmPTUmAzVFtjTqz3CI8wm1rAiTrzxWPO5CbcO5V_sAes=)
22. [preprints.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzo9z_b2teEBfUgHM9BsTTLRV8cGymjkrpErhCAqPDrPyCv8fYiKRew_4o14-kKwNLX0vCy78gjSNYm_spEvTycwPw4gfbd47igqdFxHcO2fYUrl7wH5q6f8fUxnHDnw6Li5v3F_k=)
23. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgIrYT8SVnderLnlwF0LiWRPrG6hJfLSi_nKCC1I3je2_yQWlxY6fj1eISyjEPLotjxVuLNcKDcY05jI9RQe1i-Uu-xazqAvLubw4-TWIRWS0ftjVbDDZnxOJ4mOCs2BEd)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLG6Z84nRKPp79JXOzBsA4CgJmnmkylKKHaDkm6KWrWXE1FQaVlErHBKol_Ggpx1SqvoRo8qDkDlsBkumO4m8rl1EdRrJapd9aNkkE2bY_UsifiMd3fi6gcT4NZzMEIlpv9f_TEdrXBTYGEdfi70L7qnTT4RLAm9cteWvWJQNnpit6qtqQdKxOu9fSLJkOYLj2dh17DzWcP0s7KgizBeC4mnl7YkKJLPdNxdzOziVWrUxDJRZo-HwaC77TWSTzp4RM4oSnSJn1FGTIazY=)
25. [easts.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZBUhukoSQYu6978NXKHAMiM67LCOudhofRwJijvP5yMrZpOn5SaXhTD2rgfw3Y12kHumbA_uYsHEX8jITuceCYXi_1MgIkt00guwGqQWvny8uNxFn9ODzWviZTEHEAkGqCiN61Xud)


## Annotations
Annotation(end_index=613, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7saFbWthGZhnOp7Y3BnhF3S_k6TEoqrLxfjv54li2mChJWOcpvv22It0zaLzAEXA6_ApI_qs53KF3iZU4WgmHlKoUSIvPwfOQlewf5qOZJ5BLGTKJXy5WElL1t6o7_cF5OhkeasexWeseYk4pN1kRvzUpwfbT11RQHbMC6l0NNLBAY-qlVM2HyvwWvynIO3yrZX_mmGOtEJyYX7iD57FdjlU6ZAFiScEafbhdvOwK', start_index=598)
Annotation(end_index=613, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGch7PhJbSlEinZJVO_WjL3wKclLl69FN4v0cxDM3R8c_3FD_H6GPVWVfs-m-ldLNBJ8bzc9bv7W4O1Nzkit0R81iZD1T8Iwpn_R2se8apiq9-wWDUBYKBdCFP3dweNsO7fv_ObQLzndZ4XD4FW0Ng58k1ypGw=', start_index=598)
Annotation(end_index=613, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHV0v9xZdE9fU1EeZ3FHMCOozxGBYKSx62RqgH0rsnrax5wB3DOwKdtOlW4eq40qaDOGe5km0K7fdhH7WD462ElGR3TmgP0W7ZIrVXRaT66N2Uq8vtbS7af6siVKGH_guouWD0Jh_aFyMevEyRWBhfLIqyF_jkjgjAec9GWIkY1-XlXmWnLoOAe40sMVumzrPZFoW5pekAKU-S5IoBZK2nNUA-wdcf0HjHSYtnrIiqCg8XPSA==', start_index=598)
Annotation(end_index=1150, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWRbaoyf3N4n-yQbcSWakCeZ9x5lgDiJyJajKUayOkBopqp-dS3XY8zfjKPnbUTfQ5L9WJ-nuqwUBDRiBEE_ElfMfKWPyZDs3ahQoZjqUMOy80df8wCHdsTK33hjjyHVIlRoJkGuyQxL1Vz_RhwFrrLGc=', start_index=1135)
Annotation(end_index=1150, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtMgUBabsVlKU1eLoGKjGU_4SyNAoIU8Z5bfk7jVxa-hj_-aaYRCG1eIylkcXTgmwiIqOvmf-7p-MSCaaMGUp01kpBhfeCDNu4qqEQnIGv5BrxdhDik4k5gl-8FqAOdw==', start_index=1135)
Annotation(end_index=1150, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcEWgOiiPI8MstwobEK9UcE0Oh-jQotc_B2Hfu-bEPwxU0NX5w9aO95BgzQE1V_3NjDwTVusJ9e7s_W6NEgHWdpFeBlLUYcQqjlQY_2-WIn05cqb5iVXvAVqMoFmSjYgQX0c6WCKbE00KVqNiffp0BGPDcthqDJ_nEILDLbtynH3Ve-iDIcMkVnm1F9qHyXfdU1i4c_vUUaafz21HjuqktIoiKlWgNKS4C19MOTY9u4ONoIxJ-9Cwf1tpD1A==', start_index=1135)
Annotation(end_index=1598, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5FpJjYUXloWy4SuLs6wb63Bzt3ioCt0cC7WABG29nLE8pQl4CSeJhuWvflFg-fsnCi2JVtEQeUaHkCLIk9n3QByr736HFSv7QNI65Jpy1OeAfRU4DTl2CB7KWnNudNx4WdzOKvv4TmMWmY8XohJCaQjbx-9OMv-LlOvZkvQ==', start_index=1589)
Annotation(end_index=2055, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2ql2slp6kvq5cEv3gTQRJCNYWcCPIrXjxzoXLAt2K1XLM6GPpSV6gqMFaHABbkh8Gh0aMTESVFGrFSHZ3ItX0ZIdY8HXljm__nF0V6rIBsB3rDcilk2A=', start_index=2043)
Annotation(end_index=2055, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGePzxB2tzKsNpx_bBcKdNzOp8DkwUOqjOIva5oCdBL3iydlZv59pNgI5NkSE-REpxwrmQkVPx909VGrKI0alU3xGwN4D4CAdPguihDe3-jN4KgWW6FyzvIuuKTIY7HfeuFMFY-F6BfAsLXbgSlq28KtZ24OznzdhP7pohFWZ5Ax76A_EV-kj9bZBGexUt2c1zYF2L_0xo1Xne7ugf4_iVx4VPL_oehwEOYtVgxJ_o-6MlnIBbyedb_0eSJNiWt4vcKzmsP1rjgDUH4woxTaA==', start_index=2043)
Annotation(end_index=4026, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtMgUBabsVlKU1eLoGKjGU_4SyNAoIU8Z5bfk7jVxa-hj_-aaYRCG1eIylkcXTgmwiIqOvmf-7p-MSCaaMGUp01kpBhfeCDNu4qqEQnIGv5BrxdhDik4k5gl-8FqAOdw==', start_index=4010)
Annotation(end_index=4026, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2ql2slp6kvq5cEv3gTQRJCNYWcCPIrXjxzoXLAt2K1XLM6GPpSV6gqMFaHABbkh8Gh0aMTESVFGrFSHZ3ItX0ZIdY8HXljm__nF0V6rIBsB3rDcilk2A=', start_index=4010)
Annotation(end_index=4026, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUmSQ843P-p-2loKcCohkxcrnZeJOFmQHs0Ctbt7Uqew5nDVrlboNwaCC-yzyzlEYQSpXaBIGf92X_9VF8sW1WNUJldDGoxJ77GDqJvYe1Nste7_x-2axGsFWgC3uQgjSgZyOepJbc4z-rxUJNU1a7MgsFHp8k13etw-wJc2bOLdiVWLndfXo0pZ2M1oSNraFHF_TW46BNVB3CndA=', start_index=4010)
Annotation(end_index=4225, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWRbaoyf3N4n-yQbcSWakCeZ9x5lgDiJyJajKUayOkBopqp-dS3XY8zfjKPnbUTfQ5L9WJ-nuqwUBDRiBEE_ElfMfKWPyZDs3ahQoZjqUMOy80df8wCHdsTK33hjjyHVIlRoJkGuyQxL1Vz_RhwFrrLGc=', start_index=4212)
Annotation(end_index=4225, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkcYCtM5VXQ30NjMHEwc8lrPvk3O3TZcUjaqE8jBmxYfuAMVJbEpWrisW_lLjq-l2bl5dq2p9hzP_RlfO4l-5K4y3J5qYI84h6B8TgprX7rPDV-s9BkSDn584nXC-kBiyNCK5QU75cMUx3vjURLCSiC5T0E8hQxdx_xDwDTVCiesexLA==', start_index=4212)
Annotation(end_index=4507, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5FpJjYUXloWy4SuLs6wb63Bzt3ioCt0cC7WABG29nLE8pQl4CSeJhuWvflFg-fsnCi2JVtEQeUaHkCLIk9n3QByr736HFSv7QNI65Jpy1OeAfRU4DTl2CB7KWnNudNx4WdzOKvv4TmMWmY8XohJCaQjbx-9OMv-LlOvZkvQ==', start_index=4498)
Annotation(end_index=4684, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjZUSdg9B7-bw1vARXcGwptV2MXZCG0aWiI5MW5VU66W-69Wt0Er11pDCcbX33rgL6dX3U3bttvLgaqeukvvrSiX87WfH1e6WlFXdteKTPYIYis7yI4kV2B9XtueM6UuhVcnNnO7IF19-v70TGF31Hq9q4EDuHCWslE0C6G4Z6vrYjpEVk2PPadqx1b0-HuEEH8zr9JsdLrQMYIiYcI4x4ExVygUcbOvnotfx74E2imk9FdNzzePbj_WvRHWcroLq8cbxAd22KXRLh1lSV2r5d0DuBVNWF0pDzSKD6LA4joAKIuvPygYNPnfQ=', start_index=4671)
Annotation(end_index=4684, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5FpJjYUXloWy4SuLs6wb63Bzt3ioCt0cC7WABG29nLE8pQl4CSeJhuWvflFg-fsnCi2JVtEQeUaHkCLIk9n3QByr736HFSv7QNI65Jpy1OeAfRU4DTl2CB7KWnNudNx4WdzOKvv4TmMWmY8XohJCaQjbx-9OMv-LlOvZkvQ==', start_index=4671)
Annotation(end_index=4985, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGch7PhJbSlEinZJVO_WjL3wKclLl69FN4v0cxDM3R8c_3FD_H6GPVWVfs-m-ldLNBJ8bzc9bv7W4O1Nzkit0R81iZD1T8Iwpn_R2se8apiq9-wWDUBYKBdCFP3dweNsO7fv_ObQLzndZ4XD4FW0Ng58k1ypGw=', start_index=4973)
Annotation(end_index=4985, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHV0v9xZdE9fU1EeZ3FHMCOozxGBYKSx62RqgH0rsnrax5wB3DOwKdtOlW4eq40qaDOGe5km0K7fdhH7WD462ElGR3TmgP0W7ZIrVXRaT66N2Uq8vtbS7af6siVKGH_guouWD0Jh_aFyMevEyRWBhfLIqyF_jkjgjAec9GWIkY1-XlXmWnLoOAe40sMVumzrPZFoW5pekAKU-S5IoBZK2nNUA-wdcf0HjHSYtnrIiqCg8XPSA==', start_index=4973)
Annotation(end_index=6443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGch7PhJbSlEinZJVO_WjL3wKclLl69FN4v0cxDM3R8c_3FD_H6GPVWVfs-m-ldLNBJ8bzc9bv7W4O1Nzkit0R81iZD1T8Iwpn_R2se8apiq9-wWDUBYKBdCFP3dweNsO7fv_ObQLzndZ4XD4FW0Ng58k1ypGw=', start_index=6431)
Annotation(end_index=6443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5FpJjYUXloWy4SuLs6wb63Bzt3ioCt0cC7WABG29nLE8pQl4CSeJhuWvflFg-fsnCi2JVtEQeUaHkCLIk9n3QByr736HFSv7QNI65Jpy1OeAfRU4DTl2CB7KWnNudNx4WdzOKvv4TmMWmY8XohJCaQjbx-9OMv-LlOvZkvQ==', start_index=6431)
Annotation(end_index=7428, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9gPydwdY3h4m3fxxXHowXfWeMlCdpkz6-QZupwl9atO1g8p-zx3h4rG31vZ5nploq-RDQAGrrxHBj0uGlXSqsXZQ0Dy3zjIAI5LGl-d-z6zFPk7ImyslUgq52cWPrcAjbq3fGqE66NDff0pWMSVbYI0hJCo2IGEUo-eY=', start_index=7415)
Annotation(end_index=7428, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5FpJjYUXloWy4SuLs6wb63Bzt3ioCt0cC7WABG29nLE8pQl4CSeJhuWvflFg-fsnCi2JVtEQeUaHkCLIk9n3QByr736HFSv7QNI65Jpy1OeAfRU4DTl2CB7KWnNudNx4WdzOKvv4TmMWmY8XohJCaQjbx-9OMv-LlOvZkvQ==', start_index=7415)
Annotation(end_index=8216, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjZUSdg9B7-bw1vARXcGwptV2MXZCG0aWiI5MW5VU66W-69Wt0Er11pDCcbX33rgL6dX3U3bttvLgaqeukvvrSiX87WfH1e6WlFXdteKTPYIYis7yI4kV2B9XtueM6UuhVcnNnO7IF19-v70TGF31Hq9q4EDuHCWslE0C6G4Z6vrYjpEVk2PPadqx1b0-HuEEH8zr9JsdLrQMYIiYcI4x4ExVygUcbOvnotfx74E2imk9FdNzzePbj_WvRHWcroLq8cbxAd22KXRLh1lSV2r5d0DuBVNWF0pDzSKD6LA4joAKIuvPygYNPnfQ=', start_index=8202)
Annotation(end_index=8216, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKETW3_UQPzycRJB50wYytWyZIUqpIn_zopo-cQFg_cmGWmcAY5ARrgtJqPiQW_7NAgdonnzyS0vRLJ3v6KBQRHcC1V27XPmXQT7KEhqlhjiR44XVIz0ujbaPn6tWP_6uG78z_ZlsQ4FYvHm0pzd8=', start_index=8202)
Annotation(end_index=9137, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrQfV8dLfO1etGJg95XNP57hlaZZp-QEMAFmwBdUmOpnsJEgXFUXNuwrmoor8vY0-ZAgmgTItZJ8u7SXoBby_gDwA5bjnzh9NMIVOurXbm-f6qUlAxOGc-PbpMRbTFRyg4DLJdbD0KUjUpeIgTF62uLJIdzMt0_qBLldBwgw==', start_index=9124)
Annotation(end_index=9137, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5FpJjYUXloWy4SuLs6wb63Bzt3ioCt0cC7WABG29nLE8pQl4CSeJhuWvflFg-fsnCi2JVtEQeUaHkCLIk9n3QByr736HFSv7QNI65Jpy1OeAfRU4DTl2CB7KWnNudNx4WdzOKvv4TmMWmY8XohJCaQjbx-9OMv-LlOvZkvQ==', start_index=9124)
Annotation(end_index=9881, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGch7PhJbSlEinZJVO_WjL3wKclLl69FN4v0cxDM3R8c_3FD_H6GPVWVfs-m-ldLNBJ8bzc9bv7W4O1Nzkit0R81iZD1T8Iwpn_R2se8apiq9-wWDUBYKBdCFP3dweNsO7fv_ObQLzndZ4XD4FW0Ng58k1ypGw=', start_index=9868)
Annotation(end_index=9881, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7PZ9q-lJw-nZh-j9DAspt9m_5UO6ynco801OvkmXmy0w9yRIFBvYZEAwKzn55UIPngC_zN1ei68g9FXSS57OS4NYwxU3nmSYWL41cv6j1nSPV_N7CY7ZwdCjpiBF_ZpcOm68yThePcOt1XDAOYRQkQ-GoPd3dERcBGK5KRGhQlOH-B1RAW7QT9bcNshB17n0VGGIqFH-cc-gDroKack50JlxmLwPMSYdoYYZzbbwOT5WZSr8j9f_X2IHMQU6HQogRqCruHtHWm8tUNoX-VZAQPJ3yobSD5vVeS0j-vGPe61iTQGQ=', start_index=9868)
Annotation(end_index=10364, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7saFbWthGZhnOp7Y3BnhF3S_k6TEoqrLxfjv54li2mChJWOcpvv22It0zaLzAEXA6_ApI_qs53KF3iZU4WgmHlKoUSIvPwfOQlewf5qOZJ5BLGTKJXy5WElL1t6o7_cF5OhkeasexWeseYk4pN1kRvzUpwfbT11RQHbMC6l0NNLBAY-qlVM2HyvwWvynIO3yrZX_mmGOtEJyYX7iD57FdjlU6ZAFiScEafbhdvOwK', start_index=10351)
Annotation(end_index=10364, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9gPydwdY3h4m3fxxXHowXfWeMlCdpkz6-QZupwl9atO1g8p-zx3h4rG31vZ5nploq-RDQAGrrxHBj0uGlXSqsXZQ0Dy3zjIAI5LGl-d-z6zFPk7ImyslUgq52cWPrcAjbq3fGqE66NDff0pWMSVbYI0hJCo2IGEUo-eY=', start_index=10351)
Annotation(end_index=11312, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGch7PhJbSlEinZJVO_WjL3wKclLl69FN4v0cxDM3R8c_3FD_H6GPVWVfs-m-ldLNBJ8bzc9bv7W4O1Nzkit0R81iZD1T8Iwpn_R2se8apiq9-wWDUBYKBdCFP3dweNsO7fv_ObQLzndZ4XD4FW0Ng58k1ypGw=', start_index=11300)
Annotation(end_index=11312, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHV0v9xZdE9fU1EeZ3FHMCOozxGBYKSx62RqgH0rsnrax5wB3DOwKdtOlW4eq40qaDOGe5km0K7fdhH7WD462ElGR3TmgP0W7ZIrVXRaT66N2Uq8vtbS7af6siVKGH_guouWD0Jh_aFyMevEyRWBhfLIqyF_jkjgjAec9GWIkY1-XlXmWnLoOAe40sMVumzrPZFoW5pekAKU-S5IoBZK2nNUA-wdcf0HjHSYtnrIiqCg8XPSA==', start_index=11300)
Annotation(end_index=11370, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGch7PhJbSlEinZJVO_WjL3wKclLl69FN4v0cxDM3R8c_3FD_H6GPVWVfs-m-ldLNBJ8bzc9bv7W4O1Nzkit0R81iZD1T8Iwpn_R2se8apiq9-wWDUBYKBdCFP3dweNsO7fv_ObQLzndZ4XD4FW0Ng58k1ypGw=', start_index=11361)
Annotation(end_index=11899, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5FpJjYUXloWy4SuLs6wb63Bzt3ioCt0cC7WABG29nLE8pQl4CSeJhuWvflFg-fsnCi2JVtEQeUaHkCLIk9n3QByr736HFSv7QNI65Jpy1OeAfRU4DTl2CB7KWnNudNx4WdzOKvv4TmMWmY8XohJCaQjbx-9OMv-LlOvZkvQ==', start_index=11890)
Annotation(end_index=12698, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWRbaoyf3N4n-yQbcSWakCeZ9x5lgDiJyJajKUayOkBopqp-dS3XY8zfjKPnbUTfQ5L9WJ-nuqwUBDRiBEE_ElfMfKWPyZDs3ahQoZjqUMOy80df8wCHdsTK33hjjyHVIlRoJkGuyQxL1Vz_RhwFrrLGc=', start_index=12689)
Annotation(end_index=13269, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtMgUBabsVlKU1eLoGKjGU_4SyNAoIU8Z5bfk7jVxa-hj_-aaYRCG1eIylkcXTgmwiIqOvmf-7p-MSCaaMGUp01kpBhfeCDNu4qqEQnIGv5BrxdhDik4k5gl-8FqAOdw==', start_index=13257)
Annotation(end_index=13269, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGePzxB2tzKsNpx_bBcKdNzOp8DkwUOqjOIva5oCdBL3iydlZv59pNgI5NkSE-REpxwrmQkVPx909VGrKI0alU3xGwN4D4CAdPguihDe3-jN4KgWW6FyzvIuuKTIY7HfeuFMFY-F6BfAsLXbgSlq28KtZ24OznzdhP7pohFWZ5Ax76A_EV-kj9bZBGexUt2c1zYF2L_0xo1Xne7ugf4_iVx4VPL_oehwEOYtVgxJ_o-6MlnIBbyedb_0eSJNiWt4vcKzmsP1rjgDUH4woxTaA==', start_index=13257)
Annotation(end_index=13318, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGePzxB2tzKsNpx_bBcKdNzOp8DkwUOqjOIva5oCdBL3iydlZv59pNgI5NkSE-REpxwrmQkVPx909VGrKI0alU3xGwN4D4CAdPguihDe3-jN4KgWW6FyzvIuuKTIY7HfeuFMFY-F6BfAsLXbgSlq28KtZ24OznzdhP7pohFWZ5Ax76A_EV-kj9bZBGexUt2c1zYF2L_0xo1Xne7ugf4_iVx4VPL_oehwEOYtVgxJ_o-6MlnIBbyedb_0eSJNiWt4vcKzmsP1rjgDUH4woxTaA==', start_index=13309)
Annotation(end_index=13711, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtMgUBabsVlKU1eLoGKjGU_4SyNAoIU8Z5bfk7jVxa-hj_-aaYRCG1eIylkcXTgmwiIqOvmf-7p-MSCaaMGUp01kpBhfeCDNu4qqEQnIGv5BrxdhDik4k5gl-8FqAOdw==', start_index=13702)
Annotation(end_index=14559, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtMgUBabsVlKU1eLoGKjGU_4SyNAoIU8Z5bfk7jVxa-hj_-aaYRCG1eIylkcXTgmwiIqOvmf-7p-MSCaaMGUp01kpBhfeCDNu4qqEQnIGv5BrxdhDik4k5gl-8FqAOdw==', start_index=14550)
Annotation(end_index=15067, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5FpJjYUXloWy4SuLs6wb63Bzt3ioCt0cC7WABG29nLE8pQl4CSeJhuWvflFg-fsnCi2JVtEQeUaHkCLIk9n3QByr736HFSv7QNI65Jpy1OeAfRU4DTl2CB7KWnNudNx4WdzOKvv4TmMWmY8XohJCaQjbx-9OMv-LlOvZkvQ==', start_index=15058)
Annotation(end_index=15081, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5FpJjYUXloWy4SuLs6wb63Bzt3ioCt0cC7WABG29nLE8pQl4CSeJhuWvflFg-fsnCi2JVtEQeUaHkCLIk9n3QByr736HFSv7QNI65Jpy1OeAfRU4DTl2CB7KWnNudNx4WdzOKvv4TmMWmY8XohJCaQjbx-9OMv-LlOvZkvQ==', start_index=15072)
Annotation(end_index=16513, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGW8pPrOMh8FHmCU7RWgmqK_ySD3NcQaro_2MaGJZOQFRYnVFruzTr5jzg1ttbw3ekZ8IA0tOaqn_sTexSfxcsYndUDRXpP_No2x536BTSd_xPUqSwztnj9N0kOsN3DxEuwAYzMvlSuAE2DGZzaycGctV5Ffy_b6IBH5yCIfMLWaruSsf-3jFyYlsAXeX-rU_kfvJoi3MolSwlXfAtt0xfzmVlGEaBBq1xCnEQ8kbHt', start_index=16500)
Annotation(end_index=16513, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5FpJjYUXloWy4SuLs6wb63Bzt3ioCt0cC7WABG29nLE8pQl4CSeJhuWvflFg-fsnCi2JVtEQeUaHkCLIk9n3QByr736HFSv7QNI65Jpy1OeAfRU4DTl2CB7KWnNudNx4WdzOKvv4TmMWmY8XohJCaQjbx-9OMv-LlOvZkvQ==', start_index=16500)
Annotation(end_index=16970, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGW8pPrOMh8FHmCU7RWgmqK_ySD3NcQaro_2MaGJZOQFRYnVFruzTr5jzg1ttbw3ekZ8IA0tOaqn_sTexSfxcsYndUDRXpP_No2x536BTSd_xPUqSwztnj9N0kOsN3DxEuwAYzMvlSuAE2DGZzaycGctV5Ffy_b6IBH5yCIfMLWaruSsf-3jFyYlsAXeX-rU_kfvJoi3MolSwlXfAtt0xfzmVlGEaBBq1xCnEQ8kbHt', start_index=16960)
Annotation(end_index=17343, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGePzxB2tzKsNpx_bBcKdNzOp8DkwUOqjOIva5oCdBL3iydlZv59pNgI5NkSE-REpxwrmQkVPx909VGrKI0alU3xGwN4D4CAdPguihDe3-jN4KgWW6FyzvIuuKTIY7HfeuFMFY-F6BfAsLXbgSlq28KtZ24OznzdhP7pohFWZ5Ax76A_EV-kj9bZBGexUt2c1zYF2L_0xo1Xne7ugf4_iVx4VPL_oehwEOYtVgxJ_o-6MlnIBbyedb_0eSJNiWt4vcKzmsP1rjgDUH4woxTaA==', start_index=17334)
Annotation(end_index=18733, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7saFbWthGZhnOp7Y3BnhF3S_k6TEoqrLxfjv54li2mChJWOcpvv22It0zaLzAEXA6_ApI_qs53KF3iZU4WgmHlKoUSIvPwfOQlewf5qOZJ5BLGTKJXy5WElL1t6o7_cF5OhkeasexWeseYk4pN1kRvzUpwfbT11RQHbMC6l0NNLBAY-qlVM2HyvwWvynIO3yrZX_mmGOtEJyYX7iD57FdjlU6ZAFiScEafbhdvOwK', start_index=18721)
Annotation(end_index=18733, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGch7PhJbSlEinZJVO_WjL3wKclLl69FN4v0cxDM3R8c_3FD_H6GPVWVfs-m-ldLNBJ8bzc9bv7W4O1Nzkit0R81iZD1T8Iwpn_R2se8apiq9-wWDUBYKBdCFP3dweNsO7fv_ObQLzndZ4XD4FW0Ng58k1ypGw=', start_index=18721)
Annotation(end_index=19482, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWRbaoyf3N4n-yQbcSWakCeZ9x5lgDiJyJajKUayOkBopqp-dS3XY8zfjKPnbUTfQ5L9WJ-nuqwUBDRiBEE_ElfMfKWPyZDs3ahQoZjqUMOy80df8wCHdsTK33hjjyHVIlRoJkGuyQxL1Vz_RhwFrrLGc=', start_index=19470)
Annotation(end_index=19482, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtMgUBabsVlKU1eLoGKjGU_4SyNAoIU8Z5bfk7jVxa-hj_-aaYRCG1eIylkcXTgmwiIqOvmf-7p-MSCaaMGUp01kpBhfeCDNu4qqEQnIGv5BrxdhDik4k5gl-8FqAOdw==', start_index=19470)
Annotation(end_index=19897, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2ql2slp6kvq5cEv3gTQRJCNYWcCPIrXjxzoXLAt2K1XLM6GPpSV6gqMFaHABbkh8Gh0aMTESVFGrFSHZ3ItX0ZIdY8HXljm__nF0V6rIBsB3rDcilk2A=', start_index=19888)
Annotation(end_index=19916, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuCZ_iuVl6MgBKG2ApLmsMBzIn56hINPjCv1UO2QX3MPNlCLG-JJxcqC11y_0iqL1Yq1qliCdxIzmQImaeLpodwhgKkYY1eht4cU_wvemk9xdbyPWbDFkSG3T9bXVTtXz0znI98dAhGX5u0h-bZwRN9AFaUgtBQpffLP0jrM5oG4XrGOJMkVLKQP_tEpFOt0mGP53QPTzoKCie', start_index=19906)
Annotation(end_index=20394, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGePzxB2tzKsNpx_bBcKdNzOp8DkwUOqjOIva5oCdBL3iydlZv59pNgI5NkSE-REpxwrmQkVPx909VGrKI0alU3xGwN4D4CAdPguihDe3-jN4KgWW6FyzvIuuKTIY7HfeuFMFY-F6BfAsLXbgSlq28KtZ24OznzdhP7pohFWZ5Ax76A_EV-kj9bZBGexUt2c1zYF2L_0xo1Xne7ugf4_iVx4VPL_oehwEOYtVgxJ_o-6MlnIBbyedb_0eSJNiWt4vcKzmsP1rjgDUH4woxTaA==', start_index=20385)
Annotation(end_index=20408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGePzxB2tzKsNpx_bBcKdNzOp8DkwUOqjOIva5oCdBL3iydlZv59pNgI5NkSE-REpxwrmQkVPx909VGrKI0alU3xGwN4D4CAdPguihDe3-jN4KgWW6FyzvIuuKTIY7HfeuFMFY-F6BfAsLXbgSlq28KtZ24OznzdhP7pohFWZ5Ax76A_EV-kj9bZBGexUt2c1zYF2L_0xo1Xne7ugf4_iVx4VPL_oehwEOYtVgxJ_o-6MlnIBbyedb_0eSJNiWt4vcKzmsP1rjgDUH4woxTaA==', start_index=20399)
Annotation(end_index=21075, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5JQEaUlD269sXb3dQUuZq9OyzgMoo1PM4lQ1BUMrZ3U5UQbMp1SWbxJXybLcyoi9CJb2YOe_qdC06Uw2TQDzYE8AEa9aQCYK2eouE735NhwkR4QxsTdFZ8omsX0al5-77zzpRxXZkwgLm11nEWDbn5a4uUTnnmWzjESoaA_sKzZcfZGDfMeSsTSBZDkIC66CyvWIrYJwjtgWLWQk4aW24glXQ2dsUw0L9wIYSGrvP-XnvxDVNargkM2TtS-3Kuoswz6FtS7zaoEABUIYjc-erLRJbVcQXjPM4JjRJjw==', start_index=21062)
Annotation(end_index=21075, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGePzxB2tzKsNpx_bBcKdNzOp8DkwUOqjOIva5oCdBL3iydlZv59pNgI5NkSE-REpxwrmQkVPx909VGrKI0alU3xGwN4D4CAdPguihDe3-jN4KgWW6FyzvIuuKTIY7HfeuFMFY-F6BfAsLXbgSlq28KtZ24OznzdhP7pohFWZ5Ax76A_EV-kj9bZBGexUt2c1zYF2L_0xo1Xne7ugf4_iVx4VPL_oehwEOYtVgxJ_o-6MlnIBbyedb_0eSJNiWt4vcKzmsP1rjgDUH4woxTaA==', start_index=21062)
Annotation(end_index=21618, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7saFbWthGZhnOp7Y3BnhF3S_k6TEoqrLxfjv54li2mChJWOcpvv22It0zaLzAEXA6_ApI_qs53KF3iZU4WgmHlKoUSIvPwfOQlewf5qOZJ5BLGTKJXy5WElL1t6o7_cF5OhkeasexWeseYk4pN1kRvzUpwfbT11RQHbMC6l0NNLBAY-qlVM2HyvwWvynIO3yrZX_mmGOtEJyYX7iD57FdjlU6ZAFiScEafbhdvOwK', start_index=21603)
Annotation(end_index=21618, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGch7PhJbSlEinZJVO_WjL3wKclLl69FN4v0cxDM3R8c_3FD_H6GPVWVfs-m-ldLNBJ8bzc9bv7W4O1Nzkit0R81iZD1T8Iwpn_R2se8apiq9-wWDUBYKBdCFP3dweNsO7fv_ObQLzndZ4XD4FW0Ng58k1ypGw=', start_index=21603)
Annotation(end_index=21618, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5FpJjYUXloWy4SuLs6wb63Bzt3ioCt0cC7WABG29nLE8pQl4CSeJhuWvflFg-fsnCi2JVtEQeUaHkCLIk9n3QByr736HFSv7QNI65Jpy1OeAfRU4DTl2CB7KWnNudNx4WdzOKvv4TmMWmY8XohJCaQjbx-9OMv-LlOvZkvQ==', start_index=21603)
Annotation(end_index=22073, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWRbaoyf3N4n-yQbcSWakCeZ9x5lgDiJyJajKUayOkBopqp-dS3XY8zfjKPnbUTfQ5L9WJ-nuqwUBDRiBEE_ElfMfKWPyZDs3ahQoZjqUMOy80df8wCHdsTK33hjjyHVIlRoJkGuyQxL1Vz_RhwFrrLGc=', start_index=22061)
Annotation(end_index=22073, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtMgUBabsVlKU1eLoGKjGU_4SyNAoIU8Z5bfk7jVxa-hj_-aaYRCG1eIylkcXTgmwiIqOvmf-7p-MSCaaMGUp01kpBhfeCDNu4qqEQnIGv5BrxdhDik4k5gl-8FqAOdw==', start_index=22061)
Annotation(end_index=22465, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2ql2slp6kvq5cEv3gTQRJCNYWcCPIrXjxzoXLAt2K1XLM6GPpSV6gqMFaHABbkh8Gh0aMTESVFGrFSHZ3ItX0ZIdY8HXljm__nF0V6rIBsB3rDcilk2A=', start_index=22452)
Annotation(end_index=22465, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNg5pQJEIzPAO7VJlJFMMrWTlp8x8v-ffq36pE3U-JDPoJN5NkrjkPQgDab8mUo_NBiCMIejccI-gBC-STHM3p6YmxkpP-64ac_7kPmSQ7B9EqVjHhxoaiAMeO7DB6M1-xhLMNGZrga45BQ9okoKSP-FJoeJYqKkFhng3cOBM_yn5TUJygKZZz9Z7KCHXkqykv-40HKHLMORTvvdvQOLem7WkdabpuruP8XDLjg5X6VfvEF-t-NU-Dav3Y19775FIMPz_KGXd1gJmDNWS7xW8I8GEn0QQpJZq8Dr_06OHLWFc7KB9MnSzCDnDUted5pHDmNxyzLY7DjepbxZro-vGrqcLnOOc=', start_index=22452)
Annotation(end_index=23847, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5FpJjYUXloWy4SuLs6wb63Bzt3ioCt0cC7WABG29nLE8pQl4CSeJhuWvflFg-fsnCi2JVtEQeUaHkCLIk9n3QByr736HFSv7QNI65Jpy1OeAfRU4DTl2CB7KWnNudNx4WdzOKvv4TmMWmY8XohJCaQjbx-9OMv-LlOvZkvQ==', start_index=23838)
Annotation(end_index=23923, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtMgUBabsVlKU1eLoGKjGU_4SyNAoIU8Z5bfk7jVxa-hj_-aaYRCG1eIylkcXTgmwiIqOvmf-7p-MSCaaMGUp01kpBhfeCDNu4qqEQnIGv5BrxdhDik4k5gl-8FqAOdw==', start_index=23914)
Annotation(end_index=24225, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5JQEaUlD269sXb3dQUuZq9OyzgMoo1PM4lQ1BUMrZ3U5UQbMp1SWbxJXybLcyoi9CJb2YOe_qdC06Uw2TQDzYE8AEa9aQCYK2eouE735NhwkR4QxsTdFZ8omsX0al5-77zzpRxXZkwgLm11nEWDbn5a4uUTnnmWzjESoaA_sKzZcfZGDfMeSsTSBZDkIC66CyvWIrYJwjtgWLWQk4aW24glXQ2dsUw0L9wIYSGrvP-XnvxDVNargkM2TtS-3Kuoswz6FtS7zaoEABUIYjc-erLRJbVcQXjPM4JjRJjw==', start_index=24215)
Annotation(end_index=24544, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7PZ9q-lJw-nZh-j9DAspt9m_5UO6ynco801OvkmXmy0w9yRIFBvYZEAwKzn55UIPngC_zN1ei68g9FXSS57OS4NYwxU3nmSYWL41cv6j1nSPV_N7CY7ZwdCjpiBF_ZpcOm68yThePcOt1XDAOYRQkQ-GoPd3dERcBGK5KRGhQlOH-B1RAW7QT9bcNshB17n0VGGIqFH-cc-gDroKack50JlxmLwPMSYdoYYZzbbwOT5WZSr8j9f_X2IHMQU6HQogRqCruHtHWm8tUNoX-VZAQPJ3yobSD5vVeS0j-vGPe61iTQGQ=', start_index=24534)
Annotation(end_index=24897, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjZUSdg9B7-bw1vARXcGwptV2MXZCG0aWiI5MW5VU66W-69Wt0Er11pDCcbX33rgL6dX3U3bttvLgaqeukvvrSiX87WfH1e6WlFXdteKTPYIYis7yI4kV2B9XtueM6UuhVcnNnO7IF19-v70TGF31Hq9q4EDuHCWslE0C6G4Z6vrYjpEVk2PPadqx1b0-HuEEH8zr9JsdLrQMYIiYcI4x4ExVygUcbOvnotfx74E2imk9FdNzzePbj_WvRHWcroLq8cbxAd22KXRLh1lSV2r5d0DuBVNWF0pDzSKD6LA4joAKIuvPygYNPnfQ=', start_index=24887)
Annotation(end_index=24912, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKETW3_UQPzycRJB50wYytWyZIUqpIn_zopo-cQFg_cmGWmcAY5ARrgtJqPiQW_7NAgdonnzyS0vRLJ3v6KBQRHcC1V27XPmXQT7KEhqlhjiR44XVIz0ujbaPn6tWP_6uG78z_ZlsQ4FYvHm0pzd8=', start_index=24902)
Annotation(end_index=25694, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtMgUBabsVlKU1eLoGKjGU_4SyNAoIU8Z5bfk7jVxa-hj_-aaYRCG1eIylkcXTgmwiIqOvmf-7p-MSCaaMGUp01kpBhfeCDNu4qqEQnIGv5BrxdhDik4k5gl-8FqAOdw==', start_index=25685)
Annotation(end_index=25869, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWRbaoyf3N4n-yQbcSWakCeZ9x5lgDiJyJajKUayOkBopqp-dS3XY8zfjKPnbUTfQ5L9WJ-nuqwUBDRiBEE_ElfMfKWPyZDs3ahQoZjqUMOy80df8wCHdsTK33hjjyHVIlRoJkGuyQxL1Vz_RhwFrrLGc=', start_index=25857)
Annotation(end_index=25869, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5FpJjYUXloWy4SuLs6wb63Bzt3ioCt0cC7WABG29nLE8pQl4CSeJhuWvflFg-fsnCi2JVtEQeUaHkCLIk9n3QByr736HFSv7QNI65Jpy1OeAfRU4DTl2CB7KWnNudNx4WdzOKvv4TmMWmY8XohJCaQjbx-9OMv-LlOvZkvQ==', start_index=25857)
Annotation(end_index=26117, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8njRhNy87_PI-FuwHIHyZYmIumKwyZ6S82cKKGbRsggEnkfY5FP-Uj76f6OHxL6-7Kxxtyoc0oqYRDzMEw5zmmPTUmAzVFtjTqz3CI8wm1rAiTrzxWPO5CbcO5V_sAes=', start_index=26099)
Annotation(end_index=26117, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUmSQ843P-p-2loKcCohkxcrnZeJOFmQHs0Ctbt7Uqew5nDVrlboNwaCC-yzyzlEYQSpXaBIGf92X_9VF8sW1WNUJldDGoxJ77GDqJvYe1Nste7_x-2axGsFWgC3uQgjSgZyOepJbc4z-rxUJNU1a7MgsFHp8k13etw-wJc2bOLdiVWLndfXo0pZ2M1oSNraFHF_TW46BNVB3CndA=', start_index=26099)
Annotation(end_index=26117, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzo9z_b2teEBfUgHM9BsTTLRV8cGymjkrpErhCAqPDrPyCv8fYiKRew_4o14-kKwNLX0vCy78gjSNYm_spEvTycwPw4gfbd47igqdFxHcO2fYUrl7wH5q6f8fUxnHDnw6Li5v3F_k=', start_index=26099)
Annotation(end_index=26310, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzo9z_b2teEBfUgHM9BsTTLRV8cGymjkrpErhCAqPDrPyCv8fYiKRew_4o14-kKwNLX0vCy78gjSNYm_spEvTycwPw4gfbd47igqdFxHcO2fYUrl7wH5q6f8fUxnHDnw6Li5v3F_k=', start_index=26300)
Annotation(end_index=26623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgIrYT8SVnderLnlwF0LiWRPrG6hJfLSi_nKCC1I3je2_yQWlxY6fj1eISyjEPLotjxVuLNcKDcY05jI9RQe1i-Uu-xazqAvLubw4-TWIRWS0ftjVbDDZnxOJ4mOCs2BEd', start_index=26613)
Annotation(end_index=26712, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGch7PhJbSlEinZJVO_WjL3wKclLl69FN4v0cxDM3R8c_3FD_H6GPVWVfs-m-ldLNBJ8bzc9bv7W4O1Nzkit0R81iZD1T8Iwpn_R2se8apiq9-wWDUBYKBdCFP3dweNsO7fv_ObQLzndZ4XD4FW0Ng58k1ypGw=', start_index=26703)
Annotation(end_index=27805, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5FpJjYUXloWy4SuLs6wb63Bzt3ioCt0cC7WABG29nLE8pQl4CSeJhuWvflFg-fsnCi2JVtEQeUaHkCLIk9n3QByr736HFSv7QNI65Jpy1OeAfRU4DTl2CB7KWnNudNx4WdzOKvv4TmMWmY8XohJCaQjbx-9OMv-LlOvZkvQ==', start_index=27796)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7saFbWthGZhnOp7Y3BnhF3S_k6TEoqrLxfjv54li2mChJWOcpvv22It0zaLzAEXA6_ApI_qs53KF3iZU4WgmHlKoUSIvPwfOQlewf5qOZJ5BLGTKJXy5WElL1t6o7_cF5OhkeasexWeseYk4pN1kRvzUpwfbT11RQHbMC6l0NNLBAY-qlVM2HyvwWvynIO3yrZX_mmGOtEJyYX7iD57FdjlU6ZAFiScEafbhdvOwK', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9gPydwdY3h4m3fxxXHowXfWeMlCdpkz6-QZupwl9atO1g8p-zx3h4rG31vZ5nploq-RDQAGrrxHBj0uGlXSqsXZQ0Dy3zjIAI5LGl-d-z6zFPk7ImyslUgq52cWPrcAjbq3fGqE66NDff0pWMSVbYI0hJCo2IGEUo-eY=', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWRbaoyf3N4n-yQbcSWakCeZ9x5lgDiJyJajKUayOkBopqp-dS3XY8zfjKPnbUTfQ5L9WJ-nuqwUBDRiBEE_ElfMfKWPyZDs3ahQoZjqUMOy80df8wCHdsTK33hjjyHVIlRoJkGuyQxL1Vz_RhwFrrLGc=', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjZUSdg9B7-bw1vARXcGwptV2MXZCG0aWiI5MW5VU66W-69Wt0Er11pDCcbX33rgL6dX3U3bttvLgaqeukvvrSiX87WfH1e6WlFXdteKTPYIYis7yI4kV2B9XtueM6UuhVcnNnO7IF19-v70TGF31Hq9q4EDuHCWslE0C6G4Z6vrYjpEVk2PPadqx1b0-HuEEH8zr9JsdLrQMYIiYcI4x4ExVygUcbOvnotfx74E2imk9FdNzzePbj_WvRHWcroLq8cbxAd22KXRLh1lSV2r5d0DuBVNWF0pDzSKD6LA4joAKIuvPygYNPnfQ=', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtMgUBabsVlKU1eLoGKjGU_4SyNAoIU8Z5bfk7jVxa-hj_-aaYRCG1eIylkcXTgmwiIqOvmf-7p-MSCaaMGUp01kpBhfeCDNu4qqEQnIGv5BrxdhDik4k5gl-8FqAOdw==', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2ql2slp6kvq5cEv3gTQRJCNYWcCPIrXjxzoXLAt2K1XLM6GPpSV6gqMFaHABbkh8Gh0aMTESVFGrFSHZ3ItX0ZIdY8HXljm__nF0V6rIBsB3rDcilk2A=', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8njRhNy87_PI-FuwHIHyZYmIumKwyZ6S82cKKGbRsggEnkfY5FP-Uj76f6OHxL6-7Kxxtyoc0oqYRDzMEw5zmmPTUmAzVFtjTqz3CI8wm1rAiTrzxWPO5CbcO5V_sAes=', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLG6Z84nRKPp79JXOzBsA4CgJmnmkylKKHaDkm6KWrWXE1FQaVlErHBKol_Ggpx1SqvoRo8qDkDlsBkumO4m8rl1EdRrJapd9aNkkE2bY_UsifiMd3fi6gcT4NZzMEIlpv9f_TEdrXBTYGEdfi70L7qnTT4RLAm9cteWvWJQNnpit6qtqQdKxOu9fSLJkOYLj2dh17DzWcP0s7KgizBeC4mnl7YkKJLPdNxdzOziVWrUxDJRZo-HwaC77TWSTzp4RM4oSnSJn1FGTIazY=', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUmSQ843P-p-2loKcCohkxcrnZeJOFmQHs0Ctbt7Uqew5nDVrlboNwaCC-yzyzlEYQSpXaBIGf92X_9VF8sW1WNUJldDGoxJ77GDqJvYe1Nste7_x-2axGsFWgC3uQgjSgZyOepJbc4z-rxUJNU1a7MgsFHp8k13etw-wJc2bOLdiVWLndfXo0pZ2M1oSNraFHF_TW46BNVB3CndA=', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcEWgOiiPI8MstwobEK9UcE0Oh-jQotc_B2Hfu-bEPwxU0NX5w9aO95BgzQE1V_3NjDwTVusJ9e7s_W6NEgHWdpFeBlLUYcQqjlQY_2-WIn05cqb5iVXvAVqMoFmSjYgQX0c6WCKbE00KVqNiffp0BGPDcthqDJ_nEILDLbtynH3Ve-iDIcMkVnm1F9qHyXfdU1i4c_vUUaafz21HjuqktIoiKlWgNKS4C19MOTY9u4ONoIxJ-9Cwf1tpD1A==', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzo9z_b2teEBfUgHM9BsTTLRV8cGymjkrpErhCAqPDrPyCv8fYiKRew_4o14-kKwNLX0vCy78gjSNYm_spEvTycwPw4gfbd47igqdFxHcO2fYUrl7wH5q6f8fUxnHDnw6Li5v3F_k=', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5JQEaUlD269sXb3dQUuZq9OyzgMoo1PM4lQ1BUMrZ3U5UQbMp1SWbxJXybLcyoi9CJb2YOe_qdC06Uw2TQDzYE8AEa9aQCYK2eouE735NhwkR4QxsTdFZ8omsX0al5-77zzpRxXZkwgLm11nEWDbn5a4uUTnnmWzjESoaA_sKzZcfZGDfMeSsTSBZDkIC66CyvWIrYJwjtgWLWQk4aW24glXQ2dsUw0L9wIYSGrvP-XnvxDVNargkM2TtS-3Kuoswz6FtS7zaoEABUIYjc-erLRJbVcQXjPM4JjRJjw==', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKETW3_UQPzycRJB50wYytWyZIUqpIn_zopo-cQFg_cmGWmcAY5ARrgtJqPiQW_7NAgdonnzyS0vRLJ3v6KBQRHcC1V27XPmXQT7KEhqlhjiR44XVIz0ujbaPn6tWP_6uG78z_ZlsQ4FYvHm0pzd8=', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGW8pPrOMh8FHmCU7RWgmqK_ySD3NcQaro_2MaGJZOQFRYnVFruzTr5jzg1ttbw3ekZ8IA0tOaqn_sTexSfxcsYndUDRXpP_No2x536BTSd_xPUqSwztnj9N0kOsN3DxEuwAYzMvlSuAE2DGZzaycGctV5Ffy_b6IBH5yCIfMLWaruSsf-3jFyYlsAXeX-rU_kfvJoi3MolSwlXfAtt0xfzmVlGEaBBq1xCnEQ8kbHt', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGch7PhJbSlEinZJVO_WjL3wKclLl69FN4v0cxDM3R8c_3FD_H6GPVWVfs-m-ldLNBJ8bzc9bv7W4O1Nzkit0R81iZD1T8Iwpn_R2se8apiq9-wWDUBYKBdCFP3dweNsO7fv_ObQLzndZ4XD4FW0Ng58k1ypGw=', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGePzxB2tzKsNpx_bBcKdNzOp8DkwUOqjOIva5oCdBL3iydlZv59pNgI5NkSE-REpxwrmQkVPx909VGrKI0alU3xGwN4D4CAdPguihDe3-jN4KgWW6FyzvIuuKTIY7HfeuFMFY-F6BfAsLXbgSlq28KtZ24OznzdhP7pohFWZ5Ax76A_EV-kj9bZBGexUt2c1zYF2L_0xo1Xne7ugf4_iVx4VPL_oehwEOYtVgxJ_o-6MlnIBbyedb_0eSJNiWt4vcKzmsP1rjgDUH4woxTaA==', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkcYCtM5VXQ30NjMHEwc8lrPvk3O3TZcUjaqE8jBmxYfuAMVJbEpWrisW_lLjq-l2bl5dq2p9hzP_RlfO4l-5K4y3J5qYI84h6B8TgprX7rPDV-s9BkSDn584nXC-kBiyNCK5QU75cMUx3vjURLCSiC5T0E8hQxdx_xDwDTVCiesexLA==', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrQfV8dLfO1etGJg95XNP57hlaZZp-QEMAFmwBdUmOpnsJEgXFUXNuwrmoor8vY0-ZAgmgTItZJ8u7SXoBby_gDwA5bjnzh9NMIVOurXbm-f6qUlAxOGc-PbpMRbTFRyg4DLJdbD0KUjUpeIgTF62uLJIdzMt0_qBLldBwgw==', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuCZ_iuVl6MgBKG2ApLmsMBzIn56hINPjCv1UO2QX3MPNlCLG-JJxcqC11y_0iqL1Yq1qliCdxIzmQImaeLpodwhgKkYY1eht4cU_wvemk9xdbyPWbDFkSG3T9bXVTtXz0znI98dAhGX5u0h-bZwRN9AFaUgtBQpffLP0jrM5oG4XrGOJMkVLKQP_tEpFOt0mGP53QPTzoKCie', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5FpJjYUXloWy4SuLs6wb63Bzt3ioCt0cC7WABG29nLE8pQl4CSeJhuWvflFg-fsnCi2JVtEQeUaHkCLIk9n3QByr736HFSv7QNI65Jpy1OeAfRU4DTl2CB7KWnNudNx4WdzOKvv4TmMWmY8XohJCaQjbx-9OMv-LlOvZkvQ==', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7PZ9q-lJw-nZh-j9DAspt9m_5UO6ynco801OvkmXmy0w9yRIFBvYZEAwKzn55UIPngC_zN1ei68g9FXSS57OS4NYwxU3nmSYWL41cv6j1nSPV_N7CY7ZwdCjpiBF_ZpcOm68yThePcOt1XDAOYRQkQ-GoPd3dERcBGK5KRGhQlOH-B1RAW7QT9bcNshB17n0VGGIqFH-cc-gDroKack50JlxmLwPMSYdoYYZzbbwOT5WZSr8j9f_X2IHMQU6HQogRqCruHtHWm8tUNoX-VZAQPJ3yobSD5vVeS0j-vGPe61iTQGQ=', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNg5pQJEIzPAO7VJlJFMMrWTlp8x8v-ffq36pE3U-JDPoJN5NkrjkPQgDab8mUo_NBiCMIejccI-gBC-STHM3p6YmxkpP-64ac_7kPmSQ7B9EqVjHhxoaiAMeO7DB6M1-xhLMNGZrga45BQ9okoKSP-FJoeJYqKkFhng3cOBM_yn5TUJygKZZz9Z7KCHXkqykv-40HKHLMORTvvdvQOLem7WkdabpuruP8XDLjg5X6VfvEF-t-NU-Dav3Y19775FIMPz_KGXd1gJmDNWS7xW8I8GEn0QQpJZq8Dr_06OHLWFc7KB9MnSzCDnDUted5pHDmNxyzLY7DjepbxZro-vGrqcLnOOc=', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHV0v9xZdE9fU1EeZ3FHMCOozxGBYKSx62RqgH0rsnrax5wB3DOwKdtOlW4eq40qaDOGe5km0K7fdhH7WD462ElGR3TmgP0W7ZIrVXRaT66N2Uq8vtbS7af6siVKGH_guouWD0Jh_aFyMevEyRWBhfLIqyF_jkjgjAec9GWIkY1-XlXmWnLoOAe40sMVumzrPZFoW5pekAKU-S5IoBZK2nNUA-wdcf0HjHSYtnrIiqCg8XPSA==', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZBUhukoSQYu6978NXKHAMiM67LCOudhofRwJijvP5yMrZpOn5SaXhTD2rgfw3Y12kHumbA_uYsHEX8jITuceCYXi_1MgIkt00guwGqQWvny8uNxFn9ODzWviZTEHEAkGqCiN61Xud', start_index=29526)
Annotation(end_index=29623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgIrYT8SVnderLnlwF0LiWRPrG6hJfLSi_nKCC1I3je2_yQWlxY6fj1eISyjEPLotjxVuLNcKDcY05jI9RQe1i-Uu-xazqAvLubw4-TWIRWS0ftjVbDDZnxOJ4mOCs2BEd', start_index=29526)

## Sources
