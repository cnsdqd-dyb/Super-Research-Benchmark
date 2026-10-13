# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** d1b57280 | **Time:** 754.42s | **Cost:** $2.09434
--------------------------------------------------------------------------------

# Mechanisms of Traffic Breakdown: The Role of Lane-Changing Perturbations in Cascading Capacity Bottlenecks

### Key Points
*   **The "Void Creation" Mechanism:** The primary physical cause of capacity loss during lane changing is the creation of "voids" or empty spaces in the traffic stream. Because vehicles have finite acceleration capabilities, the gap left by a departing vehicle and the gap required by an entering vehicle cannot be closed immediately, resulting in a net loss of road throughput [cite: 1, 2].
*   **Capacity Drop Phenomenon:** Empirical evidence confirms that lane-changing maneuvers near bottlenecks trigger a transition from free-flow to congested conditions, reducing the discharge rate significantly (e.g., from ~7,600 to ~6,300 vehicles per hour on a 3-lane freeway). This reduction is often irreversible until demand drops significantly [cite: 3, 4].
*   **Lateral Propagation of Congestion:** Congestion is not contained to the lane where the initial disturbance occurs. Drivers attempting to escape slow lanes transfer the disturbance laterally across the roadway, causing "friction" and speed synchronization across all lanes, effectively locking the entire carriageway into a congested state [cite: 5, 6].
*   **Traffic Hysteresis and Retarded Recovery:** Once a breakdown occurs, the traffic flow exhibits hysteresis, meaning the recovery path differs from the breakdown path. Drivers accelerate more slowly out of a jam than they decelerate into it, prolonging the bottleneck even after the initial perturbation is removed [cite: 7].
*   **The Vicious Cycle of Discretionary Lane Changes:** While drivers change lanes to improve their individual speed, this behavior often creates a "social dilemma." In moderate-to-high density, frequent lane changing increases total turbulence, reducing the overall system speed and inducing further lane changes, thereby creating a feedback loop of deteriorating capacity [cite: 8, 9].

---

## 1. Introduction

The phenomenon of traffic breakdown—the transition from free-flowing traffic to stop-and-go congestion—is a complex dynamic system governed by the interactions of individual agents (drivers) and infrastructure constraints. While static bottlenecks (such as lane reductions or on-ramps) set the stage for congestion, the specific trigger for the breakdown and the subsequent reduction in discharge capacity is frequently rooted in the microscopic behavior of lane changing (LC).

Research indicates that road capacity is not a fixed value determined solely by geometry but is a dynamic variable influenced by driver behavior. Specifically, local perturbations caused by lane-changing maneuvers act as catalysts for cascading capacity bottlenecks. When a vehicle changes lanes, it imposes a dual disruption: it creates a deceleration wave in the target lane (to accommodate insertion) and leaves a temporary void in the origin lane. Under high-density conditions, these local disturbances fail to dissipate. Instead, they amplify, propagate upstream as shockwaves, and spread laterally across lanes, leading to a systemic drop in capacity known as the "capacity drop" phenomenon.

This report provides an exhaustive analysis of the mechanisms by which local lane-changing perturbations lead to cascading bottlenecks. It synthesizes theories of void creation, kinematic wave propagation, traffic hysteresis, and behavioral psychology to explain why and how traffic flow degrades under the strain of lateral maneuvers.

---

## 2. The Physics of Lane-Changing Perturbations

To understand cascading bottlenecks, one must first analyze the microscopic physics of a single lane-change maneuver and its immediate effect on the surrounding traffic stream.

### 2.1 The Void Creation Theory
The most prominent theoretical framework explaining the link between lane changing and capacity loss is the "Void Creation" theory, notably advanced by Laval and Daganzo. This theory postulates that lane-changing vehicles act as moving bottlenecks that reduce the aggregate flow of the traffic stream [cite: 1, 10].

When a vehicle executes a lane change, two distinct physical events occur that negatively impact flow:
1.  **Target Lane Disruption:** The inserting vehicle requires a safe gap in the target lane. If the gap is insufficient, the follower in the target lane must decelerate to create space. This braking action initiates a shockwave that propagates upstream [cite: 11, 12].
2.  **Origin Lane Void:** The departing vehicle leaves a gap in the origin lane. In free-flow conditions, the following vehicle would accelerate to close this gap. However, vehicles have **bounded acceleration** capabilities. They cannot instantly accelerate to fill the space left by the lane changer. Consequently, a "void" or empty space persists in the traffic stream for a duration determined by the follower's acceleration rate and reaction time [cite: 2, 13].

This void represents "wasted" capacity. In a stream of vehicles moving at saturation flow, every second of empty pavement that is not utilized translates to a reduction in the discharge rate. Research indicates that these voids are irreversible near bottlenecks; the lost time cannot be recovered, leading to a permanent drop in throughput as long as the queue persists [cite: 10, 14].

### 2.2 The "Slugs and Rabbits" Effect
A secondary mechanism contributing to local perturbations is the heterogeneity of driver desired speeds, often described as the "slugs and rabbits" effect.
*   **Slugs:** Vehicles with lower desired speeds or lower acceleration capabilities (e.g., heavy trucks or cautious drivers).
*   **Rabbits:** Vehicles with higher desired speeds and aggressive acceleration profiles.

When a "slug" changes lanes into a faster-moving lane (often to overtake an even slower vehicle or to position for an exit), it forces the "rabbits" in the target lane to decelerate significantly to match the lower speed. This creates a localized moving bottleneck [cite: 13]. The "rabbits" are forced to brake, creating a compression wave. Because the braking intensity of the followers is often greater than the deceleration of the leader (due to reaction time delays and safety buffers), the disturbance amplifies as it moves upstream, a phenomenon known as string instability [cite: 15, 16].

### 2.3 Bounded Acceleration and Inertia
The critical factor that transforms a minor perturbation into a capacity bottleneck is the asymmetry between braking and accelerating. Vehicles can decelerate (brake) much faster than they can accelerate.
*   **Braking:** Can be rapid (e.g., -4 to -9 m/s²).
*   **Acceleration:** Is generally limited (e.g., +1 to +3 m/s²) and decreases as speed increases [cite: 1].

When a lane change forces a follower to brake, the time lost during braking is not regained during the subsequent acceleration phase because the engine power and driver comfort constraints limit how fast the vehicle can return to its original speed. This "retarded recovery" ensures that the void created by the disturbance grows or persists rather than dissipating [cite: 7, 17].

---

## 3. The Capacity Drop Phenomenon

The cumulative effect of these microscopic perturbations is a macroscopic reduction in the roadway's ability to carry traffic. This is formally known as the "capacity drop."

### 3.1 Quantifying the Drop
Empirical studies have consistently shown that the maximum flow rate a road can sustain *before* a queue forms (pre-queue capacity) is significantly higher than the flow rate *after* the queue forms (queue discharge flow).
*   **Magnitude:** Research has documented capacity drops ranging from 10% to 30%. For example, a three-lane freeway section might handle 7,600 vehicles per hour (veh/h) in stable flow, but once a breakdown is triggered by lane changing, the discharge rate drops to approximately 6,300 veh/h [cite: 3, 4].
*   **Trigger:** The drop is almost invariably preceded by a burst of lane-changing activity, particularly near merges or weaving sections [cite: 1, 18].

### 3.2 The Mechanism of the Drop
The capacity drop is not merely a consequence of congestion; it is a self-sustaining state triggered by the turbulence of lane changing.
1.  **The Trigger Event:** As density increases, a vehicle attempts a lane change (often a mandatory change near an on-ramp or off-ramp).
2.  **Perturbation:** This maneuver forces a follower to brake hard.
3.  **Void Accumulation:** Due to bounded acceleration, the stream cannot re-compress quickly enough. The average headway (time spacing) between vehicles increases as they pass through the bottleneck.
4.  **Discharge Reduction:** Larger headways mean fewer vehicles pass the bottleneck per hour. The flow stabilizes at this lower, inefficient rate [cite: 1, 13].

### 3.3 Empirical Evidence from Merge Bottlenecks
Cassidy and Rudjanakanoknad (2005) provided definitive empirical evidence of this mechanism at freeway merges. They observed that breakdowns were triggered when a queue formed in the shoulder lane (due to on-ramp merging) and then spread laterally. Drivers in the shoulder lane, frustrated by the merge friction, changed lanes to the median lanes. This "escape" behavior transferred the disturbance to the high-speed lanes, causing them to break down as well. The result was a synchronized collapse of capacity across all lanes [cite: 4, 19].

---

## 4. Propagation Dynamics: Lateral and Longitudinal

Once a local perturbation is generated by a lane change, it propagates through the traffic stream in two dimensions: longitudinally (upstream against the flow) and laterally (across adjacent lanes).

### 4.1 Longitudinal Propagation: Shockwaves
The braking maneuver induced by a lane change creates a kinematic wave (shockwave) that moves upstream.
*   **Amplification:** If the traffic density is high, the shockwave amplifies. The first follower brakes slightly, the second brakes harder, and the third may come to a complete stop. This transforms a minor lane-change disturbance into a severe stop-and-go wave [cite: 11, 12].
*   **Oscillations:** These waves manifest as traffic oscillations—cyclic patterns of acceleration and deceleration. Research confirms that lane-changing maneuvers are the primary trigger for these oscillations in multilane freeway traffic [cite: 20, 21].

### 4.2 Lateral Propagation: The Contagion of Congestion
Lateral propagation is the mechanism by which a bottleneck in one lane infects adjacent lanes.
*   **Friction and Speed Synchronization:** When one lane slows down (e.g., due to merging traffic), the speed differential between lanes increases. Drivers in the slow lane attempt to move to the faster lane (discretionary lane change).
*   **Turbulence Transfer:** These lane changers insert themselves into the fast lane, forcing those drivers to brake. Consequently, the speed in the fast lane drops to match the slow lane.
*   **Outcome:** This leads to "synchronized flow," a traffic phase described by Kerner, where all lanes travel at nearly the same reduced speed, and passing becomes impossible. The congestion effectively spreads from the shoulder lane to the median lane, utilizing lane changers as the vector of transmission [cite: 5, 22].

Research analyzing trajectory data shows that congestion typically begins in the outermost lane (near ramps) and attenuates as it propagates to inner lanes, but the lateral propagation is rapid and can account for over 90% of the congestion spread in specific spatial scales [cite: 5].

---

## 5. Traffic Hysteresis and Behavioral Responses

The relationship between traffic density and flow is not a single curve; it exhibits hysteresis loops. The behavior of drivers during the onset of congestion (braking) is fundamentally different from their behavior during recovery (acceleration).

### 5.1 The Hysteresis Loop
When a lane change triggers a deceleration wave, the traffic stream moves from a high-flow/low-density state to a low-flow/high-density state. However, when the disturbance clears, the traffic does not retrace the same path.
*   **Retarded Recovery:** Drivers are slower to accelerate out of a disturbance than they are to brake into it. This creates a "recovery delay" or "acceleration void."
*   **Impact on Capacity:** This asymmetry means that even if the original cause of the bottleneck (e.g., the lane changer) has moved on, the traffic stream remains in a depressed flow state for a longer period. The hysteresis magnitude is positively correlated with the difference in driver task difficulty between deceleration and acceleration phases [cite: 7, 17].

### 5.2 Relaxation and Synchronization
Microscopic models identify two key behavioral phases during lane changing that contribute to instability:
1.  **Synchronization:** Before changing lanes, a driver often adjusts their speed to match the target lane or a specific gap. If the target lane is slower, the driver decelerates in their *current* lane, creating a bottleneck behind them before they even execute the maneuver [cite: 23].
2.  **Relaxation:** After entering the target lane, the driver (and the new follower) accepts a short gap temporarily (non-equilibrium state). Over time, they "relax" back to a comfortable car-following distance, which involves gradually decelerating or allowing the gap to open. This expansion of the gap further reduces the local density and flow rate, contributing to the void creation effect [cite: 23, 24].

---

## 6. The Vicious Cycle: Lane Changing and Density

A critical finding in recent research is the feedback loop between congestion and lane changing.

### 6.1 Density-Dependent Lane Changing
Lane changing frequency is not constant. It follows a cubic or non-linear relationship with density.
*   **Low Density:** Lane changing is frequent but has little impact because large gaps exist.
*   **Moderate/High Density:** As density increases, the motivation to change lanes increases (to escape local slowing), but the available gaps decrease.
*   **The Critical Point:** Near capacity, drivers become aggressive, forcing their way into small gaps. This "forced" lane changing creates the most severe perturbations [cite: 9, 25].

### 6.2 The Feedback Loop
1.  **Initial State:** Traffic is dense but moving.
2.  **Perturbation:** A driver changes lanes to gain a perceived speed advantage.
3.  **Speed Drop:** This maneuver causes braking and void creation, lowering the local speed.
4.  **Increased Motivation:** The reduced speed increases the frustration of surrounding drivers, motivating *them* to change lanes to find a faster path.
5.  **Cascading Breakdown:** These subsequent lane changes create further turbulence, dropping capacity further and increasing density. This mutually reinforcing cycle leads to a rapid and total breakdown of flow [cite: 8, 26].

Research indicates a positive correlation between lane-changing frequency and the severity of congestion in general areas, suggesting that lane changing in dense traffic is often counterproductive, reducing speed for everyone involved [cite: 8].

---

## 7. Specific Bottleneck Geometries

The impact of lane changing varies by road geometry.

### 7.1 Merging Areas (On-Ramps)
Merges are the most common site of capacity drop. The "mandatory" lane changes of entering vehicles force the mainline traffic to decelerate. If the mainline is near capacity, the voids created by these insertions cannot be absorbed. The queue forms on the shoulder and, via the lateral propagation mechanism described earlier, infects the entire carriageway [cite: 1, 4, 19].

### 7.2 Diverging Areas (Off-Ramps)
Diverging areas suffer from "turbulence" caused by vehicles weaving across lanes to reach the exit. Drivers often wait until the last minute to merge, causing sudden braking in high-speed lanes. This behavior creates "off-ramp bottlenecks" where the queue for the exit spills back onto the mainline, blocking through-traffic [cite: 27, 28].

### 7.3 Weaving Sections
Weaving sections (where an on-ramp is immediately followed by an off-ramp) are particularly unstable because they involve a high volume of crossing maneuvers. The combination of accelerating (entering) and decelerating (exiting) vehicles creates a chaotic environment where void creation is maximized, leading to significant capacity reductions [cite: 14, 29].

---

## 8. Conclusion

Local perturbations from lane-changing behavior lead to cascading capacity bottlenecks through a sequence of mechanical and behavioral failures in the traffic stream. The fundamental mechanism is **void creation**: the physical inability of the traffic stream to instantly close the gaps opened by lane-changing maneuvers due to **bounded vehicle acceleration**.

This initial loss of throughput is exacerbated by **shockwave propagation**, which amplifies the disturbance upstream, and **lateral propagation**, which spreads the congestion across all lanes through speed synchronization. The phenomenon is sustained by **traffic hysteresis**, where the asymmetry between braking and acceleration prevents the flow from recovering its original capacity even after the disturbance has passed. Finally, a **vicious cycle** of density and frustration drives further lane changing, locking the roadway into a low-capacity, high-congestion state.

Understanding these mechanisms highlights that capacity is not merely a function of pavement width, but of the collective dynamic behavior of the drivers. Mitigating these bottlenecks requires strategies that dampen lane-changing turbulence, such as ramp metering to control merge density [cite: 19] or variable speed limits to homogenize flow and reduce the incentive for discretionary lane changes [cite: 30].

---

## 9. References

*   **[cite: 11]** Civil Engineering Explained. (2025). *How local perturbations from lane changing lead to traffic breakdown*.
*   **[cite: 27]** MDPI. (2025). *Tunnel–interchange connecting sections safety challenges*.
*   **[cite: 3]** Transportation Research. *Lane changing induced stop-and-go waves*.
*   **[cite: 20]** ResearchGate. *The generation of stop-and-go waves by a lane change*.
*   **[cite: 1]** Transportation Research Part B. *Impacts of Lane Changes at Merge Bottlenecks: A Theory and Strategies to Maximize Capacity*.
*   **[cite: 15]** Arxiv. (2024). *Traffic flow theory lane changing perturbations*.
*   **[cite: 30]** Wikipedia. *Traffic flow*.
*   **[cite: 8]** EurekAlert. (2023). *How lane changing spreads congestion to adjacent lanes*.
*   **[cite: 5]** ResearchGate. *Spatio-temporal dynamics of jams in two-lane traffic flow*.
*   **[cite: 22]** Wikipedia. *Three-phase traffic theory*.
*   **[cite: 7]** Connected and Autonomous Transport. *Traffic hysteresis lane changing mechanism*.
*   **[cite: 7]** Connected and Autonomous Transport. *Traffic flow hysteresis lane changing retarded recovery*.
*   **[cite: 2]** Transportation Research Part B. *Lane-changing vehicles create voids in traffic streams*.
*   **[cite: 23]** Victor Knoop. (2012). *Lane change model with relaxation and synchronization*.
*   **[cite: 13]** MDPI. *Capacity drop mechanism and void creation*.
*   **[cite: 25]** Georgia Tech. (2020). *Correlation between lane changing frequency and congestion severity*.
*   **[cite: 9]** ATRF. *Correlation between lane changing frequency and congestion severity*.
*   **[cite: 14]** ResearchGate. *A simple lane change model for microscopic traffic flow simulation*.
*   **[cite: 10]** NSF. *Void creation traffic flow lane changing mechanism*.
*   **[cite: 4]** ResearchGate. *Increasing the capacity of an isolated merge by metering its on-ramp*.
*   **[cite: 19]** Elsevier. (2005). *Increasing the capacity of an isolated merge by metering its on-ramp*.
*   **[cite: 6]** Georgia Tech. *Lateral propagation of congestion*.

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5n8esVv1Qy_AY6s18uausB0vqWnVEhVsNcofEpybwAnqX2iRlTiA1hfrZANgsTvIxKvCApFWR7k3HZzkogN_YL8T7prhusRKOJJYBTcOVucAmvamHVXkANw7sz2q57k4hWfDQLIYLp0G3L0d5BhExsdKqvdWAvUpPZ40iB9v-Tz1qzOxOSZhFhuFDo3Q1-ovD5A6MYNH-Y6p5RWjseiY4bwZfs_QixhySD6iCpOcKYuj4HmuqJhSwkaRoOcOzxYcIHA8=)
2. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGr6Y27OncqtLzxkVxassyZ4xebmCMa04iH8jPR_FlRN-nLRqte4nZpO6L3aErB83JMS7yuuMbPhzvVMy-WrX5PPFUvK5F1oqEvzAi-tRWqBYarY9D5lM4BJn-7lQkmetmp-cUOhlDAdjFhw0jefEZDmoM=)
3. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHs1ykc8LFE9pTfty2ykOhJvuMveJAnTOaRZOdGYH-mEKZpGmMmN4MqvD2_cspSS7-U2cerwRO2SBB7yyjSbfSm6fUVa2SUwdDwHq4km9CIKXKSlp7hpKtxRwG5jmKgbdfaadN2hxa6MOKH4YX2-g==)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaG4A_1kY9o29qSCcE7OSH4sGqcpQcVAH_laB54V8Jv5eH__J0vuFEeCXul8LbLwxXBoBP86VbDPR1bCn2AsjBt5NJkdYCpyR5oV8qXVTdMJEhx2H1oTksV7xASR8hmrjqAIkjpCkLabuf1u8UVa4DcsaON_Hrx_ssy2KiGr0YqkspijkIa-nbpNOSi3thXMQGH-9W6DGKWRMpyxTB2oK5Vs7t_INFnt8WPsYd9Q==)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXI9aUsJyO6rcjM4WkHWylM5X4suM3PS43MOJ5IBFmbAFxPOGyVsVX0-Ux7b5Bt6Kw5fBfZTnnRcRXTWkYncHaxXYg9attM0IHRuiarxV-B7bxJ9AU2nXIhFx4Sfn_POxTIVZ8pPm6daNgjyQJy8lyjC79AMWNVd89hBdmOa1jdbPovX1OgGMOVOM6HMR9QE5SeheISQlHzM2FhAv8s2paboNtkaphFNVjwSipYoVxW-yC)
6. [gatech.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDRVImGRUtgA7VhXo9GVRqSrgYgsozRMw-uP0nB2bM0AcoDRltzD4xHoBtC97vSrj5S-8t8rEz-bE3TYtX73Kmyy_UuJWs1ot_B8_uaKFOLUD3Zj4Nk04KgYia7uF80Cqmm7x1CKeUAytweyAAaNNyQRzIb0guetHbT44GQ1Qh-FS-)
7. [connectedandautonomoustransport.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4uAfalZ-zH-L1LFQw2EGwO7UIJ5kpaheiYV5hgrMvHf6CJrUJCntS_oiT7tsCdM5rXn6gHTrwmvqmgH3w2L61ye_2JX-fAAfezty_2oU5dmwGxmPbTS8x3pPxhjAYYAGkH5q8OlCodHT7vFGtUpLo1PW3lpCY7H84zOZTv_ywr62L8T0T7eGr0REtR3T8uzBWzIIz3ra7)
8. [eurekalert.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5x-Rrpalr_-KezbLCnrCt8Mg1I2NROXisSSdApCt4oUWOmyE3SHRq_RqD9QYmIwEy0UevFTP9OVAQOKIZ7vV1mIkOz9AqT1lraCiZKSJJsUpoXVBOgyJDxJqNiRKNm2c3C0CQpVA=)
9. [australasiantransportresearchforum.org.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHdd_3IfEUXFO3HuwKOr4AQUFPKUk9x_h9X73mfqezpugkhe_tcoUYdBVO9s4Glz12sucG2lVZKDzpmsj4OEbEntGo1xSLnBQXsCR4vL3ZcCESBmterzl4_zAbAVE6LySCvuY2ipR5mkN4vezibFpiu5yTcdflfPN50YdTJVJRkgoSKgIA0UdPNIqw-xbLmdlt2jPnrHf1g0U=)
10. [nsf.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEExya2n58wzYRbauEzWWuy00YXZD9SYB220vCg_lueXVebQ08zOdfF0laJmajxOzV3vvNh2VS11nlDN5IlUHooS5tMH553cQitRp0dhDpqpMiwbL44CCRDyRvUxDpZU8s=)
11. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzmSbJBkgk9Fsat36X9a_MLAG3Y2HQBV_H5-Di_L6_wZ_QySU48CYChsL-lNiuHV6IWcVuN1SEw9ZkBfhD7B_lTK7snJaMk3IsxqwahyfgaAMC4LT_o6413Qf8EENRrk9_)
12. [libretexts.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2S0fE9i5zwXicLJyttSpCxT56S6F3_IuBtOuoF8Bklw-p46snFgjGOoI2C8tj_OMiydKf9lo2WwaedK2viGonhTcPKR6f5Zr2SDB1GqHPQd2zwxg1yp7cbIOLeYpehD-Bhx5_nnPDnWA69b2Zuk70u8aWZJcc1RG1w-r7dp_41pNbET_NWJZ46Utef499p3ux_snHgSWQqYBhGVCoZtN9l20I4nnjiSfVYgIE6p8ubQ97Y5Go3G6g)
13. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIFwclEe70D7TxwUOgCxFtIBqb2TkwPIez6429xDB880sO9oJ6XJGmGIEFONrnqpbmZtK_-mjDnxQToPENfC7Nu4sigMMsOzerjTdvZx4ArLrCs7RKgWvin0EJGW2g)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZQEd_9CSPisCc8ZhJ2-NiLomQwN09s9oR1MTv1aonDzwJ5NDM9T5XGU5Zj-Hxcdr55fiUImq_hzsZBuUWMVcp6GAhAIh6zmyXuDmaVacaQDL14qfaOOBdVYhU970uBGYg2i-QyzwX9GtwE2ONszNo1hL91cTlF6sJCOZX-2mGNGZH5-NCqh-FlOxxccf5sdRyDmsEQX2ONCohmCrXkh1el1-dq6qQSyhKzebAIt40cAkSUWfR6QcHqGXHSBVFpZw=)
15. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCpjOx-d0aGj4F8ZVEmOJ2PQ2xRe4Rml9hkDZpCHGkYGy-DeIr0tUKCNQU673VFDoepShoxBR6Cnp8dUEqASNM0fBgBIZIJJyCxn1rcq-6KbcU7q_MPA==)
16. [wisc.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKDbBhfSBQTtoBRZoQRvhFuaZsiuO_qnZvnTpHbRwajEd6zOMyRrmRK8OVYvps3gu9lZ6Iv_WfeHcfug7b3nBu1gCkXXvehio2YZs3e1-oVxrcIbPB4vDzhdGWwE4ohdrR1JkM4xho6-WqqGyboPhpVwQ3kYnhXGaBy3PZFg==)
17. [connectedandautonomoustransport.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuPbpQcEeMhtoc4fAB-EfmtinLmbuFh0VRuONAgvcXJ68d7we1SFgI9iKvJky0IsS2fiWQlZnZTcogHLUuUZdrvSfzyyvF0qoRUlswBhk2auzbKmp2wKQnOSODyF0NB4UFQ-LA5NvRxqzZf3I7mRuGtq6ynmmGdx8po3jnUSuasWWSrq9tHWbtkJ60D3yILSSdKBWem6ldGdAB-hrmqo1T9sWzbF5nDpYOe-xvxHF4)
18. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCSQqUTKjbjGd-13-JVnrcuF1U2wBNbJvrzQcMdAjfA-YvLLuqXC5EC91LtkRtE69QwpGkuCATvRH-Sz5PUOn5_CIkE219nHYTAN8mPV0vMJ2lqwV2xctPcc7cuRFauyX06s5ko9-m6lr59UHmHePW)
19. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1G1NhMamtG5f-GPFVj1sSeZLg2-zVGQI5I7l6Z1-uV4ROaHgWKYSr8JDab-PjLos6KJNhJ8Qx0_l7BZs_97fxIwxyy1WbZawv6XtTkpG0V05hnb_QFeLBc-hJwXLxPUDrH1hkomHMhLA95EhAJFT53Lra)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLCzPYKTzFlc0fwyt4mdX0eZKFAu1j_Z4exUJXG77_dYyWChb87L1eKhFDC4csSrDGYefhr6ajeb9JCe6Q2CziJ8elJ0bonF6ZeB8SYlGtSssvqgfjnCBg3sNOCC44Ae5ek9sv9uR9laAI4wpcg0XOe-jT2HZ-RogIAq3gJ-WBaO6_UYYdeWGtNJ8xEdwOz_-vqz6agVsDBEAkj0Wl)
21. [connectedandautonomoustransport.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXjuQdz3eeEV_3OYOubpARqe_P5O2B_f9Q6BLxFqAzPlkOdIvvSENSqMMkp6aY569TjjMcVjkhlRsCLwzQfRqKw8ECoXtSX7omfqzct-DO4lKmwCOWydGAVtyvu9tLolraQxuOt033f7yftErbqn7pNWC2LJvVwf8ME64vUKMoNvR9RcizfZSNFndjthCgy7E2hQ_zs3vngFA-ykjTR4RQmUn5f1NFhmO9)
22. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvZQ90liaIXm5Daq1fAEkwA6CmwT1q0fKC6INErXRczp_3kzbnlVc7fUzlYSUxYgy5kdkxV9ujAlNRAgHHX-IFLZAawNP0GTXC2HFaFTJVNH8_IsBSuFn2OumzQyK1BIZeI5VEc4zZHvGFMho1FQ==)
23. [victorknoop.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7EFlQgRKgNFCM5yjF5dWJNydzmMmn7Kp1yXrIGWA7AUP6EKHVzJmC2wjdR2eqrfjYcSwjDuhqk9RkvLl4-u7U964W1Siu_hvd2u0Q3CBBFD6OFJTKckyMltFp6TbABy82mYqEgINj9YkYxfPDDzKeSU4=)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlfv8u2-bZscKONR6HRXX3ygF8D1flcj4HRscCrm5GG4wkJi2ypxWbOlEBQ9KNWYT2RDm6mUuM_n9KQteUIWIFl4N6-GZ0a3wrY-RoSM8lKXRKv7Xd9fHrpLM9Pn1knCcUO9Aedjo9cdU43eWStXN52g9E6tcmPZuxwIkysvY4NEOHQn4ezTwGf2Iy3NjQdT8RCwiEUdF6Bq9VvGmMzhKlKKUyyvKgFqz-tXwEfJ3LvKrFOeRbsaYsFmr1jeVbLB8=)
25. [gatech.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmcCMb1jXQ9cOp6EaatO94GMJbYdKHeVgKbQJhmd9q-9JzHyc34ibI3kPfR5Oonq6KxzQPZdK3fUHQJKYcQoqGuCaMwi0WLN9bXuS8ZEO0Pi5TqJiKGXAxye1hYZiJENhTp7n_qnXpDugDKYqHKrE5EXOfcbhvJdLN8mf332kW_hD9hR-jiaQ-SJYsFw==)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa9BCCHaN__wbIcb9_j7lCPXB3YLsdMqsLL199hEq5LBrhuNlu-ttjlAkfSW3GI_-iGFEJDN2UeLFdHa1MV_YmyAM4PrgkJueWTgwJsBjs2I8gKfcljH97SipcjO2JSkhk5S2WOfx7t_szIQdPiyFxjahrKpEStQCoBsA84OQrNAiqROmozVRpOZAim8cZvZTBnUIXa2fKCK1e3Nk0lg0WTWWKJpMTmDTr2Z_e7XsHcOlXCEjt7__wuoAmlcADps4hfoQX9fU=)
27. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-09ozZWpiRnWt1rBeyAyezePvolYNc13pd7i0zg3yFlWBHZmTfMr8TgT0ZVETQMKC3uYoWIlhmXnhK9qvr4JOJmQk10n038pEhnNDB31942apxezKh6rnaYvFCaHT)
28. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwO2olohJD6qGzvtRGabclCmOShxhI6qFkwjO0tLg3o583mHEQGY5xwVE2tq882b0oFUEgknyYQVUFjTiwcNy3pjjTdDttLxhXp0gn1OLkEh0qa2kdKIXebnTjAzo=)
29. [worldscientific.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLZuvwdrQRD2OqC2ipB_iqcnNtqt_GKo4wSq_CUdTMMnJbDdBXSBzsaCWOkPJeLlRHSFPlnBBvgIv9XV0G-kx998KZeN8XQi3PH9uzNBK8Cfu2B2ibQ45ArUKBVjILOkEf96PA-NI8mCdKRduY9Iuysfxl)
30. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKuJJXZ9zoAzsDjJKlXrrC_JpTY83uchFeGcPvHfkUoyVYRZZlwZgoeZxsIs5ZHfvy9sMwhoDjHNp2tSKC_XR-euNWBJVkTIewM57_dIe30RbD1uYY2gInoTRBbPqgsSU=)


## Annotations
Annotation(end_index=516, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5n8esVv1Qy_AY6s18uausB0vqWnVEhVsNcofEpybwAnqX2iRlTiA1hfrZANgsTvIxKvCApFWR7k3HZzkogN_YL8T7prhusRKOJJYBTcOVucAmvamHVXkANw7sz2q57k4hWfDQLIYLp0G3L0d5BhExsdKqvdWAvUpPZ40iB9v-Tz1qzOxOSZhFhuFDo3Q1-ovD5A6MYNH-Y6p5RWjseiY4bwZfs_QixhySD6iCpOcKYuj4HmuqJhSwkaRoOcOzxYcIHA8=', start_index=504)
Annotation(end_index=516, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGr6Y27OncqtLzxkVxassyZ4xebmCMa04iH8jPR_FlRN-nLRqte4nZpO6L3aErB83JMS7yuuMbPhzvVMy-WrX5PPFUvK5F1oqEvzAi-tRWqBYarY9D5lM4BJn-7lQkmetmp-cUOhlDAdjFhw0jefEZDmoM=', start_index=504)
Annotation(end_index=880, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaG4A_1kY9o29qSCcE7OSH4sGqcpQcVAH_laB54V8Jv5eH__J0vuFEeCXul8LbLwxXBoBP86VbDPR1bCn2AsjBt5NJkdYCpyR5oV8qXVTdMJEhx2H1oTksV7xASR8hmrjqAIkjpCkLabuf1u8UVa4DcsaON_Hrx_ssy2KiGr0YqkspijkIa-nbpNOSi3thXMQGH-9W6DGKWRMpyxTB2oK5Vs7t_INFnt8WPsYd9Q==', start_index=868)
Annotation(end_index=880, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHs1ykc8LFE9pTfty2ykOhJvuMveJAnTOaRZOdGYH-mEKZpGmMmN4MqvD2_cspSS7-U2cerwRO2SBB7yyjSbfSm6fUVa2SUwdDwHq4km9CIKXKSlp7hpKtxRwG5jmKgbdfaadN2hxa6MOKH4YX2-g==', start_index=868)
Annotation(end_index=1239, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDRVImGRUtgA7VhXo9GVRqSrgYgsozRMw-uP0nB2bM0AcoDRltzD4xHoBtC97vSrj5S-8t8rEz-bE3TYtX73Kmyy_UuJWs1ot_B8_uaKFOLUD3Zj4Nk04KgYia7uF80Cqmm7x1CKeUAytweyAAaNNyQRzIb0guetHbT44GQ1Qh-FS-', start_index=1227)
Annotation(end_index=1239, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXI9aUsJyO6rcjM4WkHWylM5X4suM3PS43MOJ5IBFmbAFxPOGyVsVX0-Ux7b5Bt6Kw5fBfZTnnRcRXTWkYncHaxXYg9attM0IHRuiarxV-B7bxJ9AU2nXIhFx4Sfn_POxTIVZ8pPm6daNgjyQJy8lyjC79AMWNVd89hBdmOa1jdbPovX1OgGMOVOM6HMR9QE5SeheISQlHzM2FhAv8s2paboNtkaphFNVjwSipYoVxW-yC', start_index=1227)
Annotation(end_index=1569, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4uAfalZ-zH-L1LFQw2EGwO7UIJ5kpaheiYV5hgrMvHf6CJrUJCntS_oiT7tsCdM5rXn6gHTrwmvqmgH3w2L61ye_2JX-fAAfezty_2oU5dmwGxmPbTS8x3pPxhjAYYAGkH5q8OlCodHT7vFGtUpLo1PW3lpCY7H84zOZTv_ywr62L8T0T7eGr0REtR3T8uzBWzIIz3ra7', start_index=1560)
Annotation(end_index=1958, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHdd_3IfEUXFO3HuwKOr4AQUFPKUk9x_h9X73mfqezpugkhe_tcoUYdBVO9s4Glz12sucG2lVZKDzpmsj4OEbEntGo1xSLnBQXsCR4vL3ZcCESBmterzl4_zAbAVE6LySCvuY2ipR5mkN4vezibFpiu5yTcdflfPN50YdTJVJRkgoSKgIA0UdPNIqw-xbLmdlt2jPnrHf1g0U=', start_index=1946)
Annotation(end_index=1958, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5x-Rrpalr_-KezbLCnrCt8Mg1I2NROXisSSdApCt4oUWOmyE3SHRq_RqD9QYmIwEy0UevFTP9OVAQOKIZ7vV1mIkOz9AqT1lraCiZKSJJsUpoXVBOgyJDxJqNiRKNm2c3C0CQpVA=', start_index=1946)
Annotation(end_index=4086, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEExya2n58wzYRbauEzWWuy00YXZD9SYB220vCg_lueXVebQ08zOdfF0laJmajxOzV3vvNh2VS11nlDN5IlUHooS5tMH553cQitRp0dhDpqpMiwbL44CCRDyRvUxDpZU8s=', start_index=4073)
Annotation(end_index=4086, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5n8esVv1Qy_AY6s18uausB0vqWnVEhVsNcofEpybwAnqX2iRlTiA1hfrZANgsTvIxKvCApFWR7k3HZzkogN_YL8T7prhusRKOJJYBTcOVucAmvamHVXkANw7sz2q57k4hWfDQLIYLp0G3L0d5BhExsdKqvdWAvUpPZ40iB9v-Tz1qzOxOSZhFhuFDo3Q1-ovD5A6MYNH-Y6p5RWjseiY4bwZfs_QixhySD6iCpOcKYuj4HmuqJhSwkaRoOcOzxYcIHA8=', start_index=4073)
Annotation(end_index=4460, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2S0fE9i5zwXicLJyttSpCxT56S6F3_IuBtOuoF8Bklw-p46snFgjGOoI2C8tj_OMiydKf9lo2WwaedK2viGonhTcPKR6f5Zr2SDB1GqHPQd2zwxg1yp7cbIOLeYpehD-Bhx5_nnPDnWA69b2Zuk70u8aWZJcc1RG1w-r7dp_41pNbET_NWJZ46Utef499p3ux_snHgSWQqYBhGVCoZtN9l20I4nnjiSfVYgIE6p8ubQ97Y5Go3G6g', start_index=4446)
Annotation(end_index=4460, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzmSbJBkgk9Fsat36X9a_MLAG3Y2HQBV_H5-Di_L6_wZ_QySU48CYChsL-lNiuHV6IWcVuN1SEw9ZkBfhD7B_lTK7snJaMk3IsxqwahyfgaAMC4LT_o6413Qf8EENRrk9_', start_index=4446)
Annotation(end_index=4927, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIFwclEe70D7TxwUOgCxFtIBqb2TkwPIez6429xDB880sO9oJ6XJGmGIEFONrnqpbmZtK_-mjDnxQToPENfC7Nu4sigMMsOzerjTdvZx4ArLrCs7RKgWvin0EJGW2g', start_index=4914)
Annotation(end_index=4927, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGr6Y27OncqtLzxkVxassyZ4xebmCMa04iH8jPR_FlRN-nLRqte4nZpO6L3aErB83JMS7yuuMbPhzvVMy-WrX5PPFUvK5F1oqEvzAi-tRWqBYarY9D5lM4BJn-7lQkmetmp-cUOhlDAdjFhw0jefEZDmoM=', start_index=4914)
Annotation(end_index=5314, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEExya2n58wzYRbauEzWWuy00YXZD9SYB220vCg_lueXVebQ08zOdfF0laJmajxOzV3vvNh2VS11nlDN5IlUHooS5tMH553cQitRp0dhDpqpMiwbL44CCRDyRvUxDpZU8s=', start_index=5300)
Annotation(end_index=5314, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZQEd_9CSPisCc8ZhJ2-NiLomQwN09s9oR1MTv1aonDzwJ5NDM9T5XGU5Zj-Hxcdr55fiUImq_hzsZBuUWMVcp6GAhAIh6zmyXuDmaVacaQDL14qfaOOBdVYhU970uBGYg2i-QyzwX9GtwE2ONszNo1hL91cTlF6sJCOZX-2mGNGZH5-NCqh-FlOxxccf5sdRyDmsEQX2ONCohmCrXkh1el1-dq6qQSyhKzebAIt40cAkSUWfR6QcHqGXHSBVFpZw=', start_index=5300)
Annotation(end_index=6006, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIFwclEe70D7TxwUOgCxFtIBqb2TkwPIez6429xDB880sO9oJ6XJGmGIEFONrnqpbmZtK_-mjDnxQToPENfC7Nu4sigMMsOzerjTdvZx4ArLrCs7RKgWvin0EJGW2g', start_index=5996)
Annotation(end_index=6325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCpjOx-d0aGj4F8ZVEmOJ2PQ2xRe4Rml9hkDZpCHGkYGy-DeIr0tUKCNQU673VFDoepShoxBR6Cnp8dUEqASNM0fBgBIZIJJyCxn1rcq-6KbcU7q_MPA==', start_index=6311)
Annotation(end_index=6325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKDbBhfSBQTtoBRZoQRvhFuaZsiuO_qnZvnTpHbRwajEd6zOMyRrmRK8OVYvps3gu9lZ6Iv_WfeHcfug7b3nBu1gCkXXvehio2YZs3e1-oVxrcIbPB4vDzhdGWwE4ohdrR1JkM4xho6-WqqGyboPhpVwQ3kYnhXGaBy3PZFg==', start_index=6311)
Annotation(end_index=6736, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5n8esVv1Qy_AY6s18uausB0vqWnVEhVsNcofEpybwAnqX2iRlTiA1hfrZANgsTvIxKvCApFWR7k3HZzkogN_YL8T7prhusRKOJJYBTcOVucAmvamHVXkANw7sz2q57k4hWfDQLIYLp0G3L0d5BhExsdKqvdWAvUpPZ40iB9v-Tz1qzOxOSZhFhuFDo3Q1-ovD5A6MYNH-Y6p5RWjseiY4bwZfs_QixhySD6iCpOcKYuj4HmuqJhSwkaRoOcOzxYcIHA8=', start_index=6727)
Annotation(end_index=7118, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4uAfalZ-zH-L1LFQw2EGwO7UIJ5kpaheiYV5hgrMvHf6CJrUJCntS_oiT7tsCdM5rXn6gHTrwmvqmgH3w2L61ye_2JX-fAAfezty_2oU5dmwGxmPbTS8x3pPxhjAYYAGkH5q8OlCodHT7vFGtUpLo1PW3lpCY7H84zOZTv_ywr62L8T0T7eGr0REtR3T8uzBWzIIz3ra7', start_index=7105)
Annotation(end_index=7118, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuPbpQcEeMhtoc4fAB-EfmtinLmbuFh0VRuONAgvcXJ68d7we1SFgI9iKvJky0IsS2fiWQlZnZTcogHLUuUZdrvSfzyyvF0qoRUlswBhk2auzbKmp2wKQnOSODyF0NB4UFQ-LA5NvRxqzZf3I7mRuGtq6ynmmGdx8po3jnUSuasWWSrq9tHWbtkJ60D3yILSSdKBWem6ldGdAB-hrmqo1T9sWzbF5nDpYOe-xvxHF4', start_index=7105)
Annotation(end_index=7893, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaG4A_1kY9o29qSCcE7OSH4sGqcpQcVAH_laB54V8Jv5eH__J0vuFEeCXul8LbLwxXBoBP86VbDPR1bCn2AsjBt5NJkdYCpyR5oV8qXVTdMJEhx2H1oTksV7xASR8hmrjqAIkjpCkLabuf1u8UVa4DcsaON_Hrx_ssy2KiGr0YqkspijkIa-nbpNOSi3thXMQGH-9W6DGKWRMpyxTB2oK5Vs7t_INFnt8WPsYd9Q==', start_index=7881)
Annotation(end_index=7893, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHs1ykc8LFE9pTfty2ykOhJvuMveJAnTOaRZOdGYH-mEKZpGmMmN4MqvD2_cspSS7-U2cerwRO2SBB7yyjSbfSm6fUVa2SUwdDwHq4km9CIKXKSlp7hpKtxRwG5jmKgbdfaadN2hxa6MOKH4YX2-g==', start_index=7881)
Annotation(end_index=8047, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCSQqUTKjbjGd-13-JVnrcuF1U2wBNbJvrzQcMdAjfA-YvLLuqXC5EC91LtkRtE69QwpGkuCATvRH-Sz5PUOn5_CIkE219nHYTAN8mPV0vMJ2lqwV2xctPcc7cuRFauyX06s5ko9-m6lr59UHmHePW', start_index=8034)
Annotation(end_index=8047, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5n8esVv1Qy_AY6s18uausB0vqWnVEhVsNcofEpybwAnqX2iRlTiA1hfrZANgsTvIxKvCApFWR7k3HZzkogN_YL8T7prhusRKOJJYBTcOVucAmvamHVXkANw7sz2q57k4hWfDQLIYLp0G3L0d5BhExsdKqvdWAvUpPZ40iB9v-Tz1qzOxOSZhFhuFDo3Q1-ovD5A6MYNH-Y6p5RWjseiY4bwZfs_QixhySD6iCpOcKYuj4HmuqJhSwkaRoOcOzxYcIHA8=', start_index=8034)
Annotation(end_index=8789, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5n8esVv1Qy_AY6s18uausB0vqWnVEhVsNcofEpybwAnqX2iRlTiA1hfrZANgsTvIxKvCApFWR7k3HZzkogN_YL8T7prhusRKOJJYBTcOVucAmvamHVXkANw7sz2q57k4hWfDQLIYLp0G3L0d5BhExsdKqvdWAvUpPZ40iB9v-Tz1qzOxOSZhFhuFDo3Q1-ovD5A6MYNH-Y6p5RWjseiY4bwZfs_QixhySD6iCpOcKYuj4HmuqJhSwkaRoOcOzxYcIHA8=', start_index=8776)
Annotation(end_index=8789, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIFwclEe70D7TxwUOgCxFtIBqb2TkwPIez6429xDB880sO9oJ6XJGmGIEFONrnqpbmZtK_-mjDnxQToPENfC7Nu4sigMMsOzerjTdvZx4ArLrCs7RKgWvin0EJGW2g', start_index=8776)
Annotation(end_index=9383, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1G1NhMamtG5f-GPFVj1sSeZLg2-zVGQI5I7l6Z1-uV4ROaHgWKYSr8JDab-PjLos6KJNhJ8Qx0_l7BZs_97fxIwxyy1WbZawv6XtTkpG0V05hnb_QFeLBc-hJwXLxPUDrH1hkomHMhLA95EhAJFT53Lra', start_index=9370)
Annotation(end_index=9383, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaG4A_1kY9o29qSCcE7OSH4sGqcpQcVAH_laB54V8Jv5eH__J0vuFEeCXul8LbLwxXBoBP86VbDPR1bCn2AsjBt5NJkdYCpyR5oV8qXVTdMJEhx2H1oTksV7xASR8hmrjqAIkjpCkLabuf1u8UVa4DcsaON_Hrx_ssy2KiGr0YqkspijkIa-nbpNOSi3thXMQGH-9W6DGKWRMpyxTB2oK5Vs7t_INFnt8WPsYd9Q==', start_index=9370)
Annotation(end_index=10072, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2S0fE9i5zwXicLJyttSpCxT56S6F3_IuBtOuoF8Bklw-p46snFgjGOoI2C8tj_OMiydKf9lo2WwaedK2viGonhTcPKR6f5Zr2SDB1GqHPQd2zwxg1yp7cbIOLeYpehD-Bhx5_nnPDnWA69b2Zuk70u8aWZJcc1RG1w-r7dp_41pNbET_NWJZ46Utef499p3ux_snHgSWQqYBhGVCoZtN9l20I4nnjiSfVYgIE6p8ubQ97Y5Go3G6g', start_index=10058)
Annotation(end_index=10072, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzmSbJBkgk9Fsat36X9a_MLAG3Y2HQBV_H5-Di_L6_wZ_QySU48CYChsL-lNiuHV6IWcVuN1SEw9ZkBfhD7B_lTK7snJaMk3IsxqwahyfgaAMC4LT_o6413Qf8EENRrk9_', start_index=10058)
Annotation(end_index=10330, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLCzPYKTzFlc0fwyt4mdX0eZKFAu1j_Z4exUJXG77_dYyWChb87L1eKhFDC4csSrDGYefhr6ajeb9JCe6Q2CziJ8elJ0bonF6ZeB8SYlGtSssvqgfjnCBg3sNOCC44Ae5ek9sv9uR9laAI4wpcg0XOe-jT2HZ-RogIAq3gJ-WBaO6_UYYdeWGtNJ8xEdwOz_-vqz6agVsDBEAkj0Wl', start_index=10316)
Annotation(end_index=10330, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXjuQdz3eeEV_3OYOubpARqe_P5O2B_f9Q6BLxFqAzPlkOdIvvSENSqMMkp6aY569TjjMcVjkhlRsCLwzQfRqKw8ECoXtSX7omfqzct-DO4lKmwCOWydGAVtyvu9tLolraQxuOt033f7yftErbqn7pNWC2LJvVwf8ME64vUKMoNvR9RcizfZSNFndjthCgy7E2hQ_zs3vngFA-ykjTR4RQmUn5f1NFhmO9', start_index=10316)
Annotation(end_index=11236, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvZQ90liaIXm5Daq1fAEkwA6CmwT1q0fKC6INErXRczp_3kzbnlVc7fUzlYSUxYgy5kdkxV9ujAlNRAgHHX-IFLZAawNP0GTXC2HFaFTJVNH8_IsBSuFn2OumzQyK1BIZeI5VEc4zZHvGFMho1FQ==', start_index=11223)
Annotation(end_index=11236, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXI9aUsJyO6rcjM4WkHWylM5X4suM3PS43MOJ5IBFmbAFxPOGyVsVX0-Ux7b5Bt6Kw5fBfZTnnRcRXTWkYncHaxXYg9attM0IHRuiarxV-B7bxJ9AU2nXIhFx4Sfn_POxTIVZ8pPm6daNgjyQJy8lyjC79AMWNVd89hBdmOa1jdbPovX1OgGMOVOM6HMR9QE5SeheISQlHzM2FhAv8s2paboNtkaphFNVjwSipYoVxW-yC', start_index=11223)
Annotation(end_index=11523, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXI9aUsJyO6rcjM4WkHWylM5X4suM3PS43MOJ5IBFmbAFxPOGyVsVX0-Ux7b5Bt6Kw5fBfZTnnRcRXTWkYncHaxXYg9attM0IHRuiarxV-B7bxJ9AU2nXIhFx4Sfn_POxTIVZ8pPm6daNgjyQJy8lyjC79AMWNVd89hBdmOa1jdbPovX1OgGMOVOM6HMR9QE5SeheISQlHzM2FhAv8s2paboNtkaphFNVjwSipYoVxW-yC', start_index=11514)
Annotation(end_index=12618, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4uAfalZ-zH-L1LFQw2EGwO7UIJ5kpaheiYV5hgrMvHf6CJrUJCntS_oiT7tsCdM5rXn6gHTrwmvqmgH3w2L61ye_2JX-fAAfezty_2oU5dmwGxmPbTS8x3pPxhjAYYAGkH5q8OlCodHT7vFGtUpLo1PW3lpCY7H84zOZTv_ywr62L8T0T7eGr0REtR3T8uzBWzIIz3ra7', start_index=12605)
Annotation(end_index=12618, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuPbpQcEeMhtoc4fAB-EfmtinLmbuFh0VRuONAgvcXJ68d7we1SFgI9iKvJky0IsS2fiWQlZnZTcogHLUuUZdrvSfzyyvF0qoRUlswBhk2auzbKmp2wKQnOSODyF0NB4UFQ-LA5NvRxqzZf3I7mRuGtq6ynmmGdx8po3jnUSuasWWSrq9tHWbtkJ60D3yILSSdKBWem6ldGdAB-hrmqo1T9sWzbF5nDpYOe-xvxHF4', start_index=12605)
Annotation(end_index=13054, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7EFlQgRKgNFCM5yjF5dWJNydzmMmn7Kp1yXrIGWA7AUP6EKHVzJmC2wjdR2eqrfjYcSwjDuhqk9RkvLl4-u7U964W1Siu_hvd2u0Q3CBBFD6OFJTKckyMltFp6TbABy82mYqEgINj9YkYxfPDDzKeSU4=', start_index=13044)
Annotation(end_index=13466, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlfv8u2-bZscKONR6HRXX3ygF8D1flcj4HRscCrm5GG4wkJi2ypxWbOlEBQ9KNWYT2RDm6mUuM_n9KQteUIWIFl4N6-GZ0a3wrY-RoSM8lKXRKv7Xd9fHrpLM9Pn1knCcUO9Aedjo9cdU43eWStXN52g9E6tcmPZuxwIkysvY4NEOHQn4ezTwGf2Iy3NjQdT8RCwiEUdF6Bq9VvGmMzhKlKKUyyvKgFqz-tXwEfJ3LvKrFOeRbsaYsFmr1jeVbLB8=', start_index=13452)
Annotation(end_index=13466, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7EFlQgRKgNFCM5yjF5dWJNydzmMmn7Kp1yXrIGWA7AUP6EKHVzJmC2wjdR2eqrfjYcSwjDuhqk9RkvLl4-u7U964W1Siu_hvd2u0Q3CBBFD6OFJTKckyMltFp6TbABy82mYqEgINj9YkYxfPDDzKeSU4=', start_index=13452)
Annotation(end_index=14198, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHdd_3IfEUXFO3HuwKOr4AQUFPKUk9x_h9X73mfqezpugkhe_tcoUYdBVO9s4Glz12sucG2lVZKDzpmsj4OEbEntGo1xSLnBQXsCR4vL3ZcCESBmterzl4_zAbAVE6LySCvuY2ipR5mkN4vezibFpiu5yTcdflfPN50YdTJVJRkgoSKgIA0UdPNIqw-xbLmdlt2jPnrHf1g0U=', start_index=14185)
Annotation(end_index=14198, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmcCMb1jXQ9cOp6EaatO94GMJbYdKHeVgKbQJhmd9q-9JzHyc34ibI3kPfR5Oonq6KxzQPZdK3fUHQJKYcQoqGuCaMwi0WLN9bXuS8ZEO0Pi5TqJiKGXAxye1hYZiJENhTp7n_qnXpDugDKYqHKrE5EXOfcbhvJdLN8mf332kW_hD9hR-jiaQ-SJYsFw==', start_index=14185)
Annotation(end_index=14836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa9BCCHaN__wbIcb9_j7lCPXB3YLsdMqsLL199hEq5LBrhuNlu-ttjlAkfSW3GI_-iGFEJDN2UeLFdHa1MV_YmyAM4PrgkJueWTgwJsBjs2I8gKfcljH97SipcjO2JSkhk5S2WOfx7t_szIQdPiyFxjahrKpEStQCoBsA84OQrNAiqROmozVRpOZAim8cZvZTBnUIXa2fKCK1e3Nk0lg0WTWWKJpMTmDTr2Z_e7XsHcOlXCEjt7__wuoAmlcADps4hfoQX9fU=', start_index=14823)
Annotation(end_index=14836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5x-Rrpalr_-KezbLCnrCt8Mg1I2NROXisSSdApCt4oUWOmyE3SHRq_RqD9QYmIwEy0UevFTP9OVAQOKIZ7vV1mIkOz9AqT1lraCiZKSJJsUpoXVBOgyJDxJqNiRKNm2c3C0CQpVA=', start_index=14823)
Annotation(end_index=15083, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5x-Rrpalr_-KezbLCnrCt8Mg1I2NROXisSSdApCt4oUWOmyE3SHRq_RqD9QYmIwEy0UevFTP9OVAQOKIZ7vV1mIkOz9AqT1lraCiZKSJJsUpoXVBOgyJDxJqNiRKNm2c3C0CQpVA=', start_index=15074)
Annotation(end_index=15591, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1G1NhMamtG5f-GPFVj1sSeZLg2-zVGQI5I7l6Z1-uV4ROaHgWKYSr8JDab-PjLos6KJNhJ8Qx0_l7BZs_97fxIwxyy1WbZawv6XtTkpG0V05hnb_QFeLBc-hJwXLxPUDrH1hkomHMhLA95EhAJFT53Lra', start_index=15575)
Annotation(end_index=15591, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5n8esVv1Qy_AY6s18uausB0vqWnVEhVsNcofEpybwAnqX2iRlTiA1hfrZANgsTvIxKvCApFWR7k3HZzkogN_YL8T7prhusRKOJJYBTcOVucAmvamHVXkANw7sz2q57k4hWfDQLIYLp0G3L0d5BhExsdKqvdWAvUpPZ40iB9v-Tz1qzOxOSZhFhuFDo3Q1-ovD5A6MYNH-Y6p5RWjseiY4bwZfs_QixhySD6iCpOcKYuj4HmuqJhSwkaRoOcOzxYcIHA8=', start_index=15575)
Annotation(end_index=15591, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaG4A_1kY9o29qSCcE7OSH4sGqcpQcVAH_laB54V8Jv5eH__J0vuFEeCXul8LbLwxXBoBP86VbDPR1bCn2AsjBt5NJkdYCpyR5oV8qXVTdMJEhx2H1oTksV7xASR8hmrjqAIkjpCkLabuf1u8UVa4DcsaON_Hrx_ssy2KiGr0YqkspijkIa-nbpNOSi3thXMQGH-9W6DGKWRMpyxTB2oK5Vs7t_INFnt8WPsYd9Q==', start_index=15575)
Annotation(end_index=15969, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-09ozZWpiRnWt1rBeyAyezePvolYNc13pd7i0zg3yFlWBHZmTfMr8TgT0ZVETQMKC3uYoWIlhmXnhK9qvr4JOJmQk10n038pEhnNDB31942apxezKh6rnaYvFCaHT', start_index=15955)
Annotation(end_index=15969, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwO2olohJD6qGzvtRGabclCmOShxhI6qFkwjO0tLg3o583mHEQGY5xwVE2tq882b0oFUEgknyYQVUFjTiwcNy3pjjTdDttLxhXp0gn1OLkEh0qa2kdKIXebnTjAzo=', start_index=15955)
Annotation(end_index=16356, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLZuvwdrQRD2OqC2ipB_iqcnNtqt_GKo4wSq_CUdTMMnJbDdBXSBzsaCWOkPJeLlRHSFPlnBBvgIv9XV0G-kx998KZeN8XQi3PH9uzNBK8Cfu2B2ibQ45ArUKBVjILOkEf96PA-NI8mCdKRduY9Iuysfxl', start_index=16342)
Annotation(end_index=16356, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZQEd_9CSPisCc8ZhJ2-NiLomQwN09s9oR1MTv1aonDzwJ5NDM9T5XGU5Zj-Hxcdr55fiUImq_hzsZBuUWMVcp6GAhAIh6zmyXuDmaVacaQDL14qfaOOBdVYhU970uBGYg2i-QyzwX9GtwE2ONszNo1hL91cTlF6sJCOZX-2mGNGZH5-NCqh-FlOxxccf5sdRyDmsEQX2ONCohmCrXkh1el1-dq6qQSyhKzebAIt40cAkSUWfR6QcHqGXHSBVFpZw=', start_index=16342)
Annotation(end_index=17624, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1G1NhMamtG5f-GPFVj1sSeZLg2-zVGQI5I7l6Z1-uV4ROaHgWKYSr8JDab-PjLos6KJNhJ8Qx0_l7BZs_97fxIwxyy1WbZawv6XtTkpG0V05hnb_QFeLBc-hJwXLxPUDrH1hkomHMhLA95EhAJFT53Lra', start_index=17614)
Annotation(end_index=17735, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKuJJXZ9zoAzsDjJKlXrrC_JpTY83uchFeGcPvHfkUoyVYRZZlwZgoeZxsIs5ZHfvy9sMwhoDjHNp2tSKC_XR-euNWBJVkTIewM57_dIe30RbD1uYY2gInoTRBbPqgsSU=', start_index=17725)
Annotation(end_index=17777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzmSbJBkgk9Fsat36X9a_MLAG3Y2HQBV_H5-Di_L6_wZ_QySU48CYChsL-lNiuHV6IWcVuN1SEw9ZkBfhD7B_lTK7snJaMk3IsxqwahyfgaAMC4LT_o6413Qf8EENRrk9_', start_index=17767)
Annotation(end_index=17905, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-09ozZWpiRnWt1rBeyAyezePvolYNc13pd7i0zg3yFlWBHZmTfMr8TgT0ZVETQMKC3uYoWIlhmXnhK9qvr4JOJmQk10n038pEhnNDB31942apxezKh6rnaYvFCaHT', start_index=17895)
Annotation(end_index=17999, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHs1ykc8LFE9pTfty2ykOhJvuMveJAnTOaRZOdGYH-mEKZpGmMmN4MqvD2_cspSS7-U2cerwRO2SBB7yyjSbfSm6fUVa2SUwdDwHq4km9CIKXKSlp7hpKtxRwG5jmKgbdfaadN2hxa6MOKH4YX2-g==', start_index=17990)
Annotation(end_index=18086, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLCzPYKTzFlc0fwyt4mdX0eZKFAu1j_Z4exUJXG77_dYyWChb87L1eKhFDC4csSrDGYefhr6ajeb9JCe6Q2CziJ8elJ0bonF6ZeB8SYlGtSssvqgfjnCBg3sNOCC44Ae5ek9sv9uR9laAI4wpcg0XOe-jT2HZ-RogIAq3gJ-WBaO6_UYYdeWGtNJ8xEdwOz_-vqz6agVsDBEAkj0Wl', start_index=18076)
Annotation(end_index=18174, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5n8esVv1Qy_AY6s18uausB0vqWnVEhVsNcofEpybwAnqX2iRlTiA1hfrZANgsTvIxKvCApFWR7k3HZzkogN_YL8T7prhusRKOJJYBTcOVucAmvamHVXkANw7sz2q57k4hWfDQLIYLp0G3L0d5BhExsdKqvdWAvUpPZ40iB9v-Tz1qzOxOSZhFhuFDo3Q1-ovD5A6MYNH-Y6p5RWjseiY4bwZfs_QixhySD6iCpOcKYuj4HmuqJhSwkaRoOcOzxYcIHA8=', start_index=18165)
Annotation(end_index=18319, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCpjOx-d0aGj4F8ZVEmOJ2PQ2xRe4Rml9hkDZpCHGkYGy-DeIr0tUKCNQU673VFDoepShoxBR6Cnp8dUEqASNM0fBgBIZIJJyCxn1rcq-6KbcU7q_MPA==', start_index=18309)
Annotation(end_index=18404, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKuJJXZ9zoAzsDjJKlXrrC_JpTY83uchFeGcPvHfkUoyVYRZZlwZgoeZxsIs5ZHfvy9sMwhoDjHNp2tSKC_XR-euNWBJVkTIewM57_dIe30RbD1uYY2gInoTRBbPqgsSU=', start_index=18394)
Annotation(end_index=18449, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5x-Rrpalr_-KezbLCnrCt8Mg1I2NROXisSSdApCt4oUWOmyE3SHRq_RqD9QYmIwEy0UevFTP9OVAQOKIZ7vV1mIkOz9AqT1lraCiZKSJJsUpoXVBOgyJDxJqNiRKNm2c3C0CQpVA=', start_index=18440)
Annotation(end_index=18545, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXI9aUsJyO6rcjM4WkHWylM5X4suM3PS43MOJ5IBFmbAFxPOGyVsVX0-Ux7b5Bt6Kw5fBfZTnnRcRXTWkYncHaxXYg9attM0IHRuiarxV-B7bxJ9AU2nXIhFx4Sfn_POxTIVZ8pPm6daNgjyQJy8lyjC79AMWNVd89hBdmOa1jdbPovX1OgGMOVOM6HMR9QE5SeheISQlHzM2FhAv8s2paboNtkaphFNVjwSipYoVxW-yC', start_index=18536)
Annotation(end_index=18639, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvZQ90liaIXm5Daq1fAEkwA6CmwT1q0fKC6INErXRczp_3kzbnlVc7fUzlYSUxYgy5kdkxV9ujAlNRAgHHX-IFLZAawNP0GTXC2HFaFTJVNH8_IsBSuFn2OumzQyK1BIZeI5VEc4zZHvGFMho1FQ==', start_index=18629)
Annotation(end_index=18698, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4uAfalZ-zH-L1LFQw2EGwO7UIJ5kpaheiYV5hgrMvHf6CJrUJCntS_oiT7tsCdM5rXn6gHTrwmvqmgH3w2L61ye_2JX-fAAfezty_2oU5dmwGxmPbTS8x3pPxhjAYYAGkH5q8OlCodHT7vFGtUpLo1PW3lpCY7H84zOZTv_ywr62L8T0T7eGr0REtR3T8uzBWzIIz3ra7', start_index=18689)
Annotation(end_index=18798, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4uAfalZ-zH-L1LFQw2EGwO7UIJ5kpaheiYV5hgrMvHf6CJrUJCntS_oiT7tsCdM5rXn6gHTrwmvqmgH3w2L61ye_2JX-fAAfezty_2oU5dmwGxmPbTS8x3pPxhjAYYAGkH5q8OlCodHT7vFGtUpLo1PW3lpCY7H84zOZTv_ywr62L8T0T7eGr0REtR3T8uzBWzIIz3ra7', start_index=18789)
Annotation(end_index=18911, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGr6Y27OncqtLzxkVxassyZ4xebmCMa04iH8jPR_FlRN-nLRqte4nZpO6L3aErB83JMS7yuuMbPhzvVMy-WrX5PPFUvK5F1oqEvzAi-tRWqBYarY9D5lM4BJn-7lQkmetmp-cUOhlDAdjFhw0jefEZDmoM=', start_index=18902)
Annotation(end_index=19020, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7EFlQgRKgNFCM5yjF5dWJNydzmMmn7Kp1yXrIGWA7AUP6EKHVzJmC2wjdR2eqrfjYcSwjDuhqk9RkvLl4-u7U964W1Siu_hvd2u0Q3CBBFD6OFJTKckyMltFp6TbABy82mYqEgINj9YkYxfPDDzKeSU4=', start_index=19010)
Annotation(end_index=19118, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIFwclEe70D7TxwUOgCxFtIBqb2TkwPIez6429xDB880sO9oJ6XJGmGIEFONrnqpbmZtK_-mjDnxQToPENfC7Nu4sigMMsOzerjTdvZx4ArLrCs7RKgWvin0EJGW2g', start_index=19108)
Annotation(end_index=19188, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmcCMb1jXQ9cOp6EaatO94GMJbYdKHeVgKbQJhmd9q-9JzHyc34ibI3kPfR5Oonq6KxzQPZdK3fUHQJKYcQoqGuCaMwi0WLN9bXuS8ZEO0Pi5TqJiKGXAxye1hYZiJENhTp7n_qnXpDugDKYqHKrE5EXOfcbhvJdLN8mf332kW_hD9hR-jiaQ-SJYsFw==', start_index=19178)
Annotation(end_index=19299, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHdd_3IfEUXFO3HuwKOr4AQUFPKUk9x_h9X73mfqezpugkhe_tcoUYdBVO9s4Glz12sucG2lVZKDzpmsj4OEbEntGo1xSLnBQXsCR4vL3ZcCESBmterzl4_zAbAVE6LySCvuY2ipR5mkN4vezibFpiu5yTcdflfPN50YdTJVJRkgoSKgIA0UdPNIqw-xbLmdlt2jPnrHf1g0U=', start_index=19290)
Annotation(end_index=19395, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZQEd_9CSPisCc8ZhJ2-NiLomQwN09s9oR1MTv1aonDzwJ5NDM9T5XGU5Zj-Hxcdr55fiUImq_hzsZBuUWMVcp6GAhAIh6zmyXuDmaVacaQDL14qfaOOBdVYhU970uBGYg2i-QyzwX9GtwE2ONszNo1hL91cTlF6sJCOZX-2mGNGZH5-NCqh-FlOxxccf5sdRyDmsEQX2ONCohmCrXkh1el1-dq6qQSyhKzebAIt40cAkSUWfR6QcHqGXHSBVFpZw=', start_index=19385)
Annotation(end_index=19498, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEExya2n58wzYRbauEzWWuy00YXZD9SYB220vCg_lueXVebQ08zOdfF0laJmajxOzV3vvNh2VS11nlDN5IlUHooS5tMH553cQitRp0dhDpqpMiwbL44CCRDyRvUxDpZU8s=', start_index=19488)
Annotation(end_index=19575, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaG4A_1kY9o29qSCcE7OSH4sGqcpQcVAH_laB54V8Jv5eH__J0vuFEeCXul8LbLwxXBoBP86VbDPR1bCn2AsjBt5NJkdYCpyR5oV8qXVTdMJEhx2H1oTksV7xASR8hmrjqAIkjpCkLabuf1u8UVa4DcsaON_Hrx_ssy2KiGr0YqkspijkIa-nbpNOSi3thXMQGH-9W6DGKWRMpyxTB2oK5Vs7t_INFnt8WPsYd9Q==', start_index=19566)
Annotation(end_index=19680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1G1NhMamtG5f-GPFVj1sSeZLg2-zVGQI5I7l6Z1-uV4ROaHgWKYSr8JDab-PjLos6KJNhJ8Qx0_l7BZs_97fxIwxyy1WbZawv6XtTkpG0V05hnb_QFeLBc-hJwXLxPUDrH1hkomHMhLA95EhAJFT53Lra', start_index=19670)
Annotation(end_index=19788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDRVImGRUtgA7VhXo9GVRqSrgYgsozRMw-uP0nB2bM0AcoDRltzD4xHoBtC97vSrj5S-8t8rEz-bE3TYtX73Kmyy_UuJWs1ot_B8_uaKFOLUD3Zj4Nk04KgYia7uF80Cqmm7x1CKeUAytweyAAaNNyQRzIb0guetHbT44GQ1Qh-FS-', start_index=19779)

## Sources
