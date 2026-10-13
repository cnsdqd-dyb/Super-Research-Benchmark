# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** e2cec9d5 | **Time:** 372.00s | **Cost:** $1.44663
--------------------------------------------------------------------------------

# Optimization of Specific Impulse and Thrust Vector Control Precision in Spacecraft Formation Flying

### Key Points
*   **The Fundamental Coupling:** There is a critical interdependence between Specific Impulse ($I_{sp}$) and Thrust Vector Control (TVC) precision; high $I_{sp}$ systems (typically low-thrust Electric Propulsion) require significantly higher pointing stability and vector precision than chemical systems to realize their theoretical energy efficiency.
*   **Minimum Impulse Bit (MIB) as the Limiting Factor:** For formation flying, the "Minimum Impulse Bit"—the smallest increment of thrust a system can deliver—often overrides raw $I_{sp}$ as the primary driver of efficiency. A high $I_{sp}$ thruster with a coarse MIB will cause "limit cycling" (overshooting position targets), wasting propellant and negating efficiency gains.
*   **Parasitic Torque Penalties:** Misalignment of the thrust vector relative to the center of mass creates parasitic torque. In high-$I_{sp}$ systems with long burn durations, this torque accumulates, requiring substantial compensation from reaction wheels or secondary thrusters, thereby introducing a "hidden" fuel cost that must be factored into the trade-off analysis.
*   **Mission-Dependent Optimization:** The optimal trade-off is not static; it shifts based on the formation tightness. "Loose" formations (kilometers) favor raw $I_{sp}$ for orbit maintenance, while "tight" formations (meters/sub-millimeters) prioritize TVC precision and low MIB to minimize the frequency and magnitude of correction maneuvers.

### Executive Summary
In the domain of spacecraft formation flying, the maximization of energy efficiency is not achieved merely by selecting the propulsion system with the highest Specific Impulse ($I_{sp}$). Rather, it requires a complex optimization of the trade-off between propellant efficiency ($I_{sp}$) and the precision of the actuation system, specifically Thrust Vector Control (TVC) and the Minimum Impulse Bit (MIB). Research indicates that while high-$I_{sp}$ Electric Propulsion (EP) systems offer theoretical propellant savings of 5-10x over chemical counterparts, their low-thrust nature necessitates long burn durations. During these extended maneuvers, pointing errors integrate over time, leading to significant cross-track position drift that requires costly corrective maneuvers. Consequently, to maximize actual mission energy efficiency, an increase in $I_{sp}$ must be accompanied by a commensurate increase in TVC precision. Furthermore, for precision formation flying (interferometry or rendezvous), the granularity of thrust (MIB) becomes the dominant efficiency parameter; systems capable of micronewton-level resolution (such as electrospray thrusters) prevent the energy-inefficient "ping-pong" effect of limit cycling, thereby maximizing the effective utility of the propellant mass.

---

## 1. Introduction

Spacecraft formation flying—the coordination of multiple satellites to maintain a specific relative geometric configuration—represents a paradigm shift in space mission architecture. By distributing functionality across multiple smaller platforms, agencies can achieve objectives previously requiring massive monolithic satellites, such as synthetic aperture radar (SAR) interferometry, gravitational wave detection, and exoplanet imaging [cite: 1, 2, 3]. However, the operational viability of these missions is strictly governed by the propellant budget. Unlike single satellites that primarily require station-keeping against natural perturbations, formation flyers must actively control their relative states against differential perturbations (e.g., differential drag, $J_2$ oblateness effects) and perform reconfiguration maneuvers [cite: 4, 5].

The energy efficiency of these maneuvers is typically framed around the Tsiolkovsky rocket equation, where maximizing Specific Impulse ($I_{sp}$) reduces the required propellant mass. However, this first-order analysis is insufficient for formation flying. The precision with which thrust is applied—governed by Thrust Vector Control (TVC) accuracy and the Minimum Impulse Bit (MIB)—plays a decisive role in the actual fuel consumption. A "high-efficiency" engine that cannot point accurately or shut off quickly will waste propellant correcting the errors it induces [cite: 6, 7].

This report provides an exhaustive analysis of the trade-offs between $I_{sp}$ and TVC precision. It explores how thrust vector misalignment creates parasitic torques that drain energy, how the granularity of thrust affects limit cycle efficiency, and how different propulsion technologies (Chemical vs. Electric) occupy different optima within this trade space.

## 2. The Physics of Propulsion Trade-offs in Formation Flying

To understand the optimization of energy efficiency, one must first decouple the contributions of propellant exhaust velocity (related to $I_{sp}$) and the geometric application of that force (TVC).

### 2.1 Specific Impulse ($I_{sp}$) and Propellant Efficiency
Specific impulse is a measure of how effectively a propulsion system uses propellant to generate thrust. It is defined as the thrust produced per unit weight flow rate of the propellant:

\[ I_{sp} = \frac{F}{\dot{m} g_0} \]

Where $F$ is thrust, $\dot{m}$ is the mass flow rate, and $g_0$ is standard gravity [cite: 8, 9]. In the context of formation flying, a higher $I_{sp}$ implies that for a required change in velocity ($\Delta V$) to correct a relative position error, less propellant mass is consumed.
*   **Chemical Propulsion:** Typically offers high thrust but lower $I_{sp}$ (200–320 s for bipropellants/monopropellants) [cite: 7, 10].
*   **Electric Propulsion (EP):** Offers low thrust but very high $I_{sp}$ (1,500–5,000 s for Hall/Ion thrusters, up to 6,000 s for FEEP) [cite: 7, 11, 12].

While high $I_{sp}$ is desirable for reducing launch mass, it generally correlates with low thrust-to-weight ratios. This necessitates long-duration burns to achieve the same $\Delta V$ that a chemical thruster would achieve impulsively. This duration factor introduces the critical dependency on pointing precision [cite: 13, 14].

### 2.2 Thrust Vector Control (TVC) and Pointing Errors
TVC refers to the ability to manipulate the direction of the thrust vector relative to the spacecraft's body frame. In formation flying, the "efficiency" of a maneuver is degraded by two primary vector errors:
1.  **Cosine Loss (Misalignment with Target Vector):** If the thrust vector is misaligned by an angle $\theta$ from the desired maneuver direction, the effective $\Delta V$ is reduced by $\cos(\theta)$. The wasted energy is proportional to $1 - \cos(\theta)$.
2.  **Cross-Coupling (Parasitic $\Delta V$):** The component of thrust perpendicular to the desired direction ($\sin(\theta)$) introduces an orbital error that must be cancelled by a future maneuver, effectively doubling the cost of the error [cite: 1, 15].

For impulsive maneuvers (high thrust/low $I_{sp}$), the burn time is short, so the integration of attitude error is minimized. However, for low-thrust/high-$I_{sp}$ maneuvers, the thrust is applied over minutes or hours. A small bias in the thrust vector integrates into a large position drift, necessitating further corrective burns [cite: 14, 16].

### 2.3 Parasitic Torque and Center of Mass (CoM) Offsets
A major energy sink in formation flying is the "parasitic torque" generated when the thrust vector does not pass through the spacecraft's Center of Mass (CoM).
\[ \tau_{parasitic} = F \times d \]
Where $F$ is the thrust vector and $d$ is the lever arm (offset distance).
*   **Impact on Efficiency:** This torque causes the spacecraft to rotate. To maintain the correct firing attitude, the Attitude Determination and Control System (ADCS) must counteract this torque. If Reaction Wheels (RW) are used, they accumulate momentum and eventually require "desaturation" (firing thrusters to dump momentum), which consumes propellant. If thrusters are used directly for attitude control (RCS), fuel is burned immediately to fight the rotation rather than translating the spacecraft [cite: 7, 15, 17].
*   **The Trade-off:** High precision TVC (e.g., using gimbals or precise differential throttling) can align the thrust vector through the CoM, eliminating parasitic torque. However, gimbals add mass and complexity. The optimization lies in balancing the mass of the TVC hardware against the propellant saved by eliminating parasitic torque [cite: 7].

## 3. The Role of Minimum Impulse Bit (MIB)

While $I_{sp}$ determines the efficiency of a continuous burn, the **Minimum Impulse Bit (MIB)** determines the efficiency of *maintaining* a precise relative position. This is arguably the most critical parameter for formation flying efficiency.

### 3.1 The Limit Cycle Problem
In formation flying, satellites often operate within a "control box" or "deadband." When the satellite drifts to the edge of the box, the thrusters fire to push it back.
*   **Coarse MIB (High Thrust):** If the propulsion system can only deliver a large minimum "puff" of thrust (high MIB), the satellite will be pushed too hard, crossing the box and hitting the other side, requiring a braking maneuver. This "ping-pong" effect (limit cycling) is extremely inefficient, regardless of the engine's $I_{sp}$ [cite: 6, 18].
*   **Fine MIB (Low Thrust):** Systems with very small MIBs (e.g., Electrospray thrusters with MIB $< 0.1 \mu Ns$) can apply just enough force to nudge the satellite away from the boundary without overshooting. This allows for "drag-free" or extremely tight formation control with minimal fuel waste [cite: 19, 20, 21].

### 3.2 MIB vs. $I_{sp}$ Trade-off
There is often an inverse relationship between thrust magnitude and MIB precision.
*   **Chemical Thrusters:** High thrust, moderate $I_{sp}$, but typically high MIB (mN-s range). Efficient for large reconfiguration maneuvers but inefficient for fine station-keeping [cite: 11, 18].
*   **Cold Gas:** Low $I_{sp}$ (~70s), but very low MIB and simple. Often used when contamination or thermal issues preclude EP, despite low propellant efficiency [cite: 11, 18].
*   **Electrospray/FEEP:** High $I_{sp}$ (>1000s) and extremely low MIB (nN-s range). This represents the local optimum for precision formation flying, as it combines propellant efficiency with control granularity [cite: 19, 22].

## 4. Optimization of Thrust Vector Control Precision

To maximize energy efficiency, the precision of the TVC system must be matched to the propulsion type and mission phase.

### 4.1 Coupling Pointing Accuracy with Burn Duration
Research indicates that as $I_{sp}$ increases (and thrust decreases), the requirement for pointing stability increases.
*   **Low-Thrust Trajectories:** For continuous thrust maneuvers (typical of High $I_{sp}$), the guidance law assumes a specific thrust vector profile. Errors in pointing lead to a divergence from the optimal trajectory. A study on the Magnetospheric Multiscale (MMS) mission showed that a thrust vector direction error (due to spin/nutation) could cause a 1 km drift in just 3 orbits, necessitating expensive trimming maneuvers [cite: 1].
*   **Optimization Criterion:** The energy efficiency is maximized when the "Navigation and Control" error is smaller than the "Deadband" width. If the pointing error cone is larger than the target receiver antenna or formation box, the effective $I_{sp}$ drops to zero (thrust is applied, but the objective is not met) [cite: 23, 24].

### 4.2 Gimbaled vs. Differential Thrust Vectoring
Two primary methods exist to control the thrust vector, each with efficiency implications:
1.  **Mechanical Gimbals:** Allow the engine to swivel.
    *   *Pros:* Can align thrust perfectly with CoM, eliminating parasitic torque [cite: 7, 25].
    *   *Cons:* Heavy, complex, and slow response bandwidth.
2.  **Differential Throttling/Vectoring (Multi-thruster):** Using multiple fixed thrusters and varying their output to steer.
    *   *Pros:* Fast response, no moving parts.
    *   *Cons:* "Cosine loss" is inherent because thrusters are often canted. Firing two thrusters to get a net vector results in lower effective $I_{sp}$ than firing one gimbaled thruster [cite: 15, 16].
    *   *Trade-off:* For small satellites (CubeSats), the mass penalty of a gimbal often outweighs the propellant savings. For large formations, gimbals are preferred to maximize the efficiency of high-$I_{sp}$ engines [cite: 7].

### 4.3 Beam Divergence and Vector Stability
In Electric Propulsion, the "thrust vector" is not always perfectly aligned with the mechanical nozzle due to magnetic field anomalies or grid erosion.
*   **Beam Divergence:** High $I_{sp}$ ion thrusters can have beam divergence. If the beam spreads significantly, the axial thrust component decreases (cosine loss), reducing effective $I_{sp}$ [cite: 12].
*   **Vector Stability:** If the thrust vector wanders (instability), the ACS must work harder. Research on Hall thrusters shows that magnetic steering can deviate the beam by ~10 degrees, but this may reduce efficiency and increase wall erosion [cite: 16]. Optimizing the magnetic field design to minimize divergence is crucial for maintaining the system's high intrinsic $I_{sp}$ [cite: 12].

## 5. Mission Architecture Case Studies

The theoretical trade-offs manifest differently depending on the specific mission requirements.

### 5.1 Precision Interferometry: LISA Pathfinder & PROBA-3
Missions like LISA (gravitational wave detection) require picometer-level stability.
*   **Propulsion Choice:** Colloid/Electrospray thrusters or FEEP.
*   **Why:** Although these have high $I_{sp}$, the primary driver is the **MIB** and **thrust noise**. A chemical thruster with high MIB would disturb the test masses. The efficiency here is defined by "noise-free operation" rather than just $\Delta V$. The ability to provide continuous, micro-Newton thrust with nanoradian pointing stability allows the formation to be maintained without disrupting the scientific measurement [cite: 19, 20, 26].
*   **Trade-off:** They sacrifice high thrust authority (cannot move fast) for extreme precision and high $I_{sp}$.

### 5.2 Constellation Maintenance: Starlink / Mega-constellations
While not strict "formation flying" in the interferometric sense, these satellites maintain relative planes.
*   **Propulsion Choice:** Hall Effect Thrusters (Krypton/Argon).
*   **Why:** Moderate-High $I_{sp}$ (1500-3000s) is prioritized to minimize launch mass.
*   **TVC:** They use simple single-axis gimbals or differential drag. The formation requirements are loose (km range), so the MIB and pointing precision requirements are relaxed compared to LISA. The efficiency focus is purely on propellant mass fraction [cite: 7].

### 5.3 Spinning Formations: MMS
The Magnetospheric Multiscale (MMS) mission uses spinning spacecraft in a tetrahedron formation.
*   **Challenge:** Spinning introduces nutation and timing errors. A thrust pulse must be timed perfectly with the rotation.
*   **Efficiency Loss:** Errors in timing (phase lag) result in thrust vector misalignment. This requires "trim maneuvers." The study found that failure to perform maneuvers accurately (due to pointing errors) drives up the fuel budget significantly [cite: 1].
*   **Optimization:** High thrust (chemical) is used because the burns must be instantaneous sectors of the spin cycle. High $I_{sp}$ EP would be difficult to implement on a rapidly spinning platform due to the need for continuous pointing.

## 6. Quantitative Optimization Strategies

To mathematically maximize energy efficiency ($J$), one must minimize the cost function involving propellant consumption and state error.

### 6.1 The Cost Function
A typical cost function for formation flying control (e.g., Linear Quadratic Regulator - LQR) is:
\[ J = \int_{0}^{\infty} (x^T Q x + u^T R u) dt \]
Where $x$ is the state error (position/velocity) and $u$ is the control effort (thrust).
*   **High $I_{sp}$ Influence:** High $I_{sp}$ reduces the "cost" of $u$ (propellant mass), allowing for more control effort to minimize $x$.
*   **TVC Influence:** TVC precision affects the coupling matrix $B$ in the state space model ($\dot{x} = Ax + Bu$). If TVC is poor, $B$ has uncertainty, requiring robust control techniques (like $H_{\infty}$) which are often more conservative and fuel-consuming [cite: 4, 27].

### 6.2 Model Predictive Control (MPC)
MPC is increasingly used to handle the constraints of MIB and TVC limits.
*   **Handling MIB:** MPC can explicitly include the "minimum on-time" constraint of the thruster. It plans a trajectory that avoids "chattering" by grouping burns or drifting until the error is large enough to justify a burn of at least $1 \times$ MIB. This optimization is far more energy-efficient than standard PD controllers for systems with coarse MIB [cite: 6, 27, 28].
*   **Handling TVC:** MPC can optimize the "slew-and-fire" sequence. For single-thruster satellites, the satellite must slew (rotate) to point the thruster. MPC optimizes the trade-off between the fuel spent slewing (RW or RCS) and the fuel spent translating [cite: 27].

## 7. Conclusion: The Optimal Trade-off

The maximization of energy efficiency in spacecraft formation flying is not a singular solution but a dynamic operating point on the trade-off curve between Specific Impulse and Thrust Vector Control precision.

1.  **High $I_{sp}$ demands High TVC Precision:** Utilizing high-$I_{sp}$ electric propulsion to save mass is only effective if the Thrust Vector Control system can maintain pointing stability over long burn durations. If pointing errors exceed $\sim 1^\circ$, the cosine losses and cross-track drift corrections will negate the propellant savings of the high $I_{sp}$.
2.  **MIB Dominates in Tight Formations:** For formation tolerances $< 10$ meters, the Minimum Impulse Bit is the governing efficiency parameter. High $I_{sp}$ is irrelevant if the thruster cannot fire small enough increments to avoid limit cycling. In this regime, Electrospray/FEEP thrusters (High $I_{sp}$ + Low MIB) are the optimal solution.
3.  **Parasitic Torque is the Hidden Cost:** The most energy-efficient system is one that aligns the thrust vector through the Center of Mass. Active TVC (gimbals) or precise alignment is essential for high-$I_{sp}$ missions to prevent the ADCS from becoming the primary fuel consumer.

**Recommendation:** For future formation flying missions, the propulsion system should not be selected on $I_{sp}$ alone. The selection metric must be the **"Effective Specific Impulse" ($I_{sp,eff}$)**, which accounts for the duty cycle, cosine losses from TVC errors, and the propellant overhead of momentum management induced by parasitic torques.

---

## 8. Detailed Analysis of Propulsion Technologies in Formation Flying

### 8.1 Electric Propulsion (EP) Characteristics
Electric propulsion systems, such as Hall Effect Thrusters (HETs), Gridded Ion Engines, and Electrospray Thrusters, operate by accelerating propellant ions using electric and magnetic fields.
*   **Specific Impulse:** They achieve $I_{sp}$ values ranging from 1,500 s to over 4,000 s [cite: 7]. This is significantly higher than chemical rockets (~300 s), allowing for substantial mass savings or extended mission lifetimes.
*   **Thrust Magnitude:** The trade-off is low thrust (mN to N range). This necessitates continuous thrusting for orbit raising or large reconfigurations, making the mission timeline longer [cite: 7].
*   **Formation Flying Suitability:** EP is ideal for "drag compensation" and fine station-keeping due to the ability to throttle and provide low thrust. However, the power requirement (Watts to Kilowatts) imposes constraints on the satellite bus, potentially affecting the thermal stability and structural dynamics, which in turn can degrade pointing accuracy [cite: 23, 29].

### 8.2 Chemical Propulsion Characteristics
*   **Specific Impulse:** Limited by chemical energy density, typically 200-320 s [cite: 10].
*   **Thrust Magnitude:** High thrust allows for impulsive maneuvers (instantaneous $\Delta V$). This simplifies the guidance mathematics (Hohmann transfers) and reduces the impact of accumulated pointing errors over time.
*   **Formation Flying Suitability:** Best for collision avoidance and rapid reconfiguration. However, the "minimum impulse bit" is often limited by valve response times (typically ms range), resulting in a minimum $\Delta V$ of several mm/s. This makes them unsuitable for sub-meter formation control without excessive fuel waste due to "deadbanding" [cite: 11, 18].

### 8.3 Cold Gas and Micro-Propulsion
*   **Specific Impulse:** Low (~60-70 s) [cite: 11, 18].
*   **Precision:** Extremely fine MIB and low thermal/magnetic disturbance.
*   **Role:** Often used in CubeSats or as a backup for precision pointing. The trade-off here is accepting low fuel efficiency (low $I_{sp}$) to gain the high control precision required for the mission, effectively "buying" precision with mass [cite: 11, 30].

## 9. Impact of Environmental Disturbances on the Trade-off

The optimal balance between $I_{sp}$ and TVC is also a function of the environmental disturbances acting on the formation.

### 9.1 Differential Drag ($J_2$)
In Low Earth Orbit (LEO), atmospheric drag is the dominant perturbation. If two satellites have different ballistic coefficients, they will drift apart.
*   **High $I_{sp}$ Solution:** Continuous low-thrust compensation (EP) is highly efficient here. The thruster can throttle to exactly match the drag force. TVC precision must only match the variability of the drag vector [cite: 5, 31].
*   **Differential Drag Control:** A propellant-less method involves rotating the satellite panels to change drag area. This has infinite $I_{sp}$ (no fuel) but very poor control authority and slow response. It is a valid "zero-energy" mode for loose formations [cite: 32, 33].

### 9.2 Solar Radiation Pressure (SRP)
In high orbits (GEO, Deep Space), SRP dominates.
*   **Impact on TVC:** SRP creates a disturbance torque that the ACS must fight. High $I_{sp}$ thrusters (like FEEP) are often used to counteract this continuously. The TVC system must be precise enough to distinguish between the SRP disturbance and the formation control requirement [cite: 26].

## 10. Advanced Control Strategies for Energy Maximization

### 10.1 Linear Quadratic Regulator (LQR) and $H_{\infty}$
Control theory provides the mathematical framework for this trade-off.
*   **LQR:** Minimizes a weighted sum of state error and control effort. By tuning the weighting matrices ($Q$ and $R$), engineers can explicitly trade position accuracy for fuel consumption. A high $R$ value penalizes fuel use, forcing the system to accept larger position errors (looser formation) [cite: 4, 34].
*   **$H_{\infty}$:** Designed for robustness against model uncertainties (like TVC misalignment). It ensures stability even if the thrust vector is not perfectly known, but typically results in a more conservative (higher energy) controller [cite: 4].

### 10.2 Autonomous Formation Flying (AFF)
Onboard autonomy allows for real-time optimization. Instead of executing a pre-planned burn (which might be stale due to errors), the satellite recalculates the optimal burn based on current state estimates.
*   **Benefit:** Reduces the "margin" required in fuel budgets.
*   **Requirement:** Requires precise relative navigation (e.g., Carrier-Phase Differential GPS) to feed the control loop. The accuracy of the *sensor* must exceed the accuracy of the *actuator* (TVC) for this to work [cite: 24, 35, 36].

## 11. Future Trends and Technologies

### 11.1 Multi-Mode Propulsion
Future systems may combine high thrust (chemical) and high $I_{sp}$ (electric) modes in a single package (e.g., multimode monopropellants). This allows the formation to switch modes: High Thrust for reconfiguration (where TVC error integration is low) and High $I_{sp}$ for station-keeping (where TVC precision is critical) [cite: 7, 37].

### 11.2 MEMS-based Micro-Thrusters
Micro-Electro-Mechanical Systems (MEMS) allow for arrays of thousands of microscopic emitters (electrospray).
*   **Redundancy:** If one emitter fails or misaligns, others can compensate.
*   **Digital TVC:** By selectively firing specific emitters in the array, the thrust vector can be steered electronically without heavy gimbals, offering a high-reliability, high-precision solution with high $I_{sp}$ [cite: 19, 38].

### 11.3 AI/ML in Thrust Vectoring
Machine Learning algorithms are being developed to "learn" the thrust vector misalignment in real-time. By observing the satellite's rotational response to a burn, the AI can estimate the CoM offset and adjust the TVC commands to compensate, effectively "calibrating out" the parasitic torque and improving energy efficiency over the mission life [cite: 39, 40].

## 12. Summary of Trade-off Variables

| Parameter | High Specific Impulse ($I_{sp}$) | High Thrust Vector Control (TVC) Precision | Interaction Effect on Efficiency |
| :--- | :--- | :--- | :--- |
| **Thrust Magnitude** | Generally Low (EP) | N/A | Low thrust requires long burns, making TVC stability critical. |
| **Burn Duration** | Long (Hours/Days) | N/A | Long burns integrate pointing errors; High TVC precision is required to prevent drift. |
| **Minimum Impulse Bit** | Often Low (Electrospray) | High Resolution | Low MIB prevents limit cycling, maximizing efficiency for tight formations. |
| **Parasitic Torque** | Critical (due to duration) | Minimizes Torque | High TVC precision eliminates torque, saving ACS fuel. |
| **System Mass** | Low Propellant Mass | High Dry Mass (Gimbals) | Trade-off: Fuel savings vs. Hardware mass. |
| **Optimal Application** | Station-Keeping, Drag Compensation | Precision Interferometry, Docking | High $I_{sp}$ + High TVC is the "Gold Standard" for precision missions (LISA). |

## 13. Conclusion

The query regarding the trade-off between specific impulse and thrust vector control precision in spacecraft formation flying reveals a complex, multi-dimensional optimization problem. There is no single "maximum efficiency" point; rather, the optimum depends heavily on the formation tightness and mission duration.

*   **For Loose Formations (km-scale):** The trade-off favors **High $I_{sp}$**. The relative position tolerances are large enough that coarse TVC and larger MIBs are acceptable. The primary driver is reducing the bulk propellant mass for orbit maintenance.
*   **For Tight Formations (m-scale):** The trade-off shifts toward **High TVC Precision and Low MIB**. The energy cost of "fighting" the control system (limit cycling, parasitic torque compensation) outweighs the theoretical benefits of $I_{sp}$. A lower $I_{sp}$ system with finer control (like Cold Gas) might actually be *more* energy-efficient in practice than a high $I_{sp}$ system with poor control authority, because it avoids wasted "correction" burns.
*   **The Ultimate Solution:** The convergence of technologies—specifically **Electrospray and FEEP thrusters**—offers a "best of both worlds" solution. These systems provide the high $I_{sp}$ of electric propulsion (>1000 s) with the micronewton-level MIB and vectoring capability required for precision control. This technology suite represents the current state-of-the-art for maximizing energy efficiency in formation flying, as demonstrated by the LISA Pathfinder mission.

In summary, maximizing energy efficiency requires a holistic view where $I_{sp}$ reduces the "cost per Newton," but TVC precision and MIB ensure that "every Newton counts" towards the mission objective. Neglecting TVC precision in favor of raw $I_{sp}$ is a false economy in the delicate dance of formation flying.

**Sources:**
1. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERoMAUIvQG45gxPDRvpEXt4Ev3A_-b4c7SJLENumn9hsS9UIYXddVlNuJ4rq1mx7KN0M5nyskTaXgx2fXkHQofO1McdH8ux1zBP6JEfV1qTHzV0K8L3F-YqpC-JVn-b0AQk6Iit3uALo2lzf8VwR4bC6zGZCk8y05XaptjsZWz)
2. [diva-portal.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH96jC9qPvCaR1NtsapFQgCBCY8qJxYnATMp9SVlANId1gD_gecE7uHZhkvrRG2YAf-4rHarBA15frhd_-bru3Slr2N_9qhS9saGy5ggtOO-p-7DbU-jnj2QqmEMNWFiH6JbueYP9vagef3J2SPMaPJV4Fg76ZMgQ==)
3. [aanda.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9Y9WOm-J_v60a6Ox5vauEJZ9XwCAYxtXnH728EV6loBi6tOk4NHtM35BD2Ewjt72PVPpxidkTTo5E12mzTlpIeCWPCPss9fLJGEcLCvr2Giwqbd1ztGjMjkfMhMlzZywdfB4zAXxjtMvOWqstKInZvHb6JypMMimOKr99Zr_hEgMBz20=)
4. [aiaa.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFLt5_MGQ1E7bCfczbq49CvgCQQiSdVpnws2TUfjmYBnSh16lC9ZKaL29HlrMCm5izEEf-HhEYGE2DH30B35F0mHqrDmxrW5-bgJLDeDiA9l2ONxeiF5TYoQzw2Rqf44s=)
5. [issfd.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnDItjwrr5lGATe-U6Sjssf-8WJAUBAYElK24jGVJyaQOgVWvLlw2yJyRwLc3jaPV7ZnHIez8KFFqmlc-V1JN60LZGuFQu0-83y9VPjHgHQXjtbYYCnP7Iww7cAu3ov4CUT4LO3k4uCyrlbn9KnJONYVg2tA==)
6. [usu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGohEhUgQMdHZQi7lYYW7JhtVLQliF5yaTFK5Wf7QQdeYJfo1T9iAgtBmzalTPw3xFM1wYoDuwVqCCt-TghFfrcPvbkHP3u6oqqKZsls-p-17LY9cQ1uyzc-pYS9Njd8OqtM5WK2lYbj30e8gzbEm0Ok0FBGcX7ATrMWMv79ZP0hOEkNWfTg==)
7. [bqpsim.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-AV1eq3rGH0b3ZtlmPb-jfkJk15-R8uyaA8wlk-5nSB-ZTegVrbBU_G8Z24rpgRbekamHVniGU_jmLwc2MZsxcx0azoJ4QmT5CyzpYHdz22F56eBt7ADr-87nc5KEhtlxkcKPzIdnM0YD0YP4t1larLHW)
8. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHX-7dvcxOrz6TRn9pkjO0GIFunlHcvUVKLGbmiBxsmVJXMINYIbuPooY9gkXMOLxgtaSvMeUUBmEAQ1y2cU6pp6vIYGsGaGczzQgozHMBrecS5WSJ4GMxZcU4Q3XNrkIUf0d75)
9. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTKSoDUUWX-HjidAIGbx4G7LNUsLuVZbQoredXvh5IuxMBA33inj133bFQvkOo0nk-THhb-16ibUl9MsO-aqPJov0tzLFwDhIhCL-Xf9V3DhshYHCP7Vq2hs2RxhX8kwT5rnrauWgKitbHznVB)
10. [nationalacademies.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZtTgk2Wg6nqzNDE83gY_S4_ka_1UvTElA4OVPG3U6Hw3EezO_rL32cN92XjD0Rk-vBi7464a4mxhzRR4pfXX31gIwCAq7yr2i2nNSn6NSWEyxs_k85ikF-HyiXGY4m7uBQaw0W2HQv_YMV7Q=)
11. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCgrTdJGCVJKhL2oXa9EDY89BUXTFl-BnLNSnlrr221sKm72JJlGdQ90ZtHr6cEslzeXaZ6GnjodpIWRZq0H19MzqbsratZupPAfqPesGxdVws7LlZNl3IZ0Y_0LYAZlvq4rCpjo4zqmSOry4zBQdukYJ7jB16FeXahLj2rDzF)
12. [tuwien.at](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4A70ck73jyiFtzeaMfNt7XHR62DAfah98qzcciLCFLioElOuNT1k0PLBVaccap7BxEMsvhYQtYR3bKTuASRHCuIiiegzMIwS4ndpYNxBrZ0-qATtYwSgjiQ3j7gYLWnpFOwR5ah2WP9SEeBa6RTaIGuAENf4smcYKTe9-JbEXll2qz7gsfqBu-wTlv6yn427IwIWl3i9O_BxT-g==)
13. [orbital-mechanics.space](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3GTBELlpR4g6CZTf_5n8ISnAMy80dBUkAk4tixIph6dPw1Te7IiuPbONOq452itCT9ECdsGfueItmcO5KzDjEc9ouFK4c37g3LN7ZsufKG6HvDnp_5ebI6h5lNFKFLNekCvNk6wpuXlr7sjFQ1SyYSaUYQByywYJBYDPmZ1QUDQ==)
14. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYz1zvwNQWt3Fc7Oggpik1S4fa34Nbt6m2w4Hy2QS8k8EnDYEL41I5NJ6dNgBTpzQQeIrQOVOyUG_V1MVLR28FJQ7_9cSFJQ3RP2bbusB1Fb9sJCvdCKpu0oVYMQPH0ZijbW8JC5mI1gTlVcOM38MyXqKW3_Qvaty2rp5nN0gZg0cq_TezKydeY3564bOuoDZnEejHXPXdtK2ldg==)
15. [electricrocket.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3jg4Nl9i9LUh354hhH2z3OHuK05uDWpsOMFEgIbzA9sSIA2S5v7rMVdFm6T8eXAbN5N_CpY49-a0V3-izid5GT1loEY1uhTvVlD1tRG0Wq-l6C4aNM6NCNQ4cpYUEJg==)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfKfEtDQQbc__ZwjZ6HZJvWcEgbMxQgTbcXZC3UIr1dibDUwIlwU8i5368U_17ZA9E1tMLweg2UOc00hNJoo0-Piqio0p6jdWTTRlCWIo5HJv9-GcIIcaVozL8-KfnNvuvrOFwF6mPDZQR0TbMC7NkNYYIKHMt0s3Ky1UNJdmhCLJgU0qgw5TKYfZsf5P6KBHn_9yiDGEgmqnxQNeeM8A9sXUETanhvK3SbL2jng5lMSwFkZw=)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9HNGHDr91vG-dGna9j9KbsO_fU5sXulGAiHm6dmXIQeRBxlKZrLuOILwLhh78a4l9sBbOcC7fex2Q0_Pcqew3jUrdPFObLBAWXueAe0tSqJHrouBRhvBWUaI5nRz-Hb08D9Zo4Mtys-BaO-5oMJa2Xi5mwFJAI69haBkkTlph5yu-BogrFfGD2fFMfhKnB1OE6nOwGOI7YLak6ZaLN36GU1AUGEe3RfiCeZaAUMI8xMokhaU=)
18. [hofer.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2fvOiAIhLwrUqY7mhEeK8_Wu0UqRoHHVv1fmEKXmUqVlXffEg_wi9itADdcTDxf0xG0to5n0Tm85XO0Fh0qPT1OfvNDFS6tAIladmDagzqpgB5YGAZhJAT8KZ7tLtilt1_Ie_YMaWidKG)
19. [electricrocket.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFw-hgx0xIAw9xmGLFiYgZUivClj-4qfogpGXGxv_MnEwITa8sFYLK_dWqlB7QId9mVSk8FMeD_g3s2e5EPum9sIleRbImJfc56cCcZFBgozwPu27EZEDGfCVYbaB_ZQl0l_I0JQT8)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy36GBgHhNJaDb1XNcJ0eVxqCN_zRyH9scZffwtzSwUo1MiG4XZ71R4DqJfhl3x0EBqritQGNVgN6PivKsJEh1Xw_9UylY4u2TSsEuz5TOogs0VWOi1ZG2sjV6-PuvUKRYfOKSlX6wCpbRsTcam5VBbcco9M5YWadjCOOJOxXlqXB-GB47i_WCyaVtRQU6HssAyO7mUnGU2pO5CDbgY-1qRQgC4JtSBiD15u2o-UuRgWApYanwXRjEVTDeF-GAvA==)
21. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvbszqLvofhhunndM02jkrRPV1zPX-gmtYBg_PD5ObA-ylIOG4sz5dYi-UEfnlyZxb83H1IbHGWd6yu9zKSP85PXlQScU6X8o38yZhuvnG6RD_Vp3MkKObtwqW-1aOlotFIN-zIczVvvuOHfzbTv8rizb4HjNfbNdt0g==)
22. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIOd6OvFU3tz-sivBZ3mJvXAE8i1P1iIFfDTZ3I7Wthne-FBte-Lf82wRhki0njPRoqbWE2OFacmu5OsVwauN7MfAqLe6-v2RfbUvwRMqkGt6fN5Xg4iJ5aZf-ilc74zhgddzdueV_WDkt6rxAnKzvoRYKThrEFPzuY7kylpKM9RuwlG0alPnUFGjVS6TqQVvE48pgNwjXy6TtRc4SYB5ipXcQuwKz5H1i4Tf3EMbdU24=)
23. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFq_2XJKm9Wm6CyRTitUtJ_LiC9P27jfIzXPVfdSud4-nicoHXFyPdvlxHpvrrHSMNzfgj2tiJ_-V_jEk0vqFX7IHlVTFSMIDbdNvRdBlTSJ5Dmb748HuNmYeuao-33V30Iu-dolnjA9kYaoGO1ABhd6--0gTM9fzwlyf7INvyC)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCrv6UZfo9CaIdZB8M1bH9lPs7Bb8HyYnU0ik5TlxNrLii_7ysz2IIH_WvHHIqeImB1CWhnFjtJJJb9uM82sT1yBF2glKKZxtgdwVgI20f5N-B4CDaECsySoOPFapVZdj-CBQuX4oM5vm08Cw-RDqZnbMhEDKkR1sy-BW-RSDtdi7v0FmsPVLTQBe1oYHe1hSEVRENEo6dtRXUTMwvJ5wtDigIhqqkWCszeyVNzgbDkNZa0rQCSDbtuMMdnH-xUF9x5jIpiY5o)
25. [studysmarter.co.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGS78iBbosMAV4yf97pnud4k65LAfDQRs9HguD2XKQ9HPaF7BLsp1b8vhvw3wtG4SK96-nlrAN2Qwbty66qGdH8katFcWYFOKiVgbpm8nuTtA1SMa0z970cpIzu_hVdG8nlbxddpsGZxKIMAohH4vi7RSHs_vU8NzLIczLREiGv4sq6MqQ2X1gOut9mz-oDI8Cy06GvFEEb8wSC)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyG38mjuZkrNajwIpSEoNWWF5ltf6H-eQnzxm1qLlUDped6NuGn6pTIFu57XWnHHGHe9EZU36ZSpRvbF0YQqyckC--mXu5-fePgWOsMAFF8fSIRNkpsS4aDLZ8KO9zCECNDmn0gjaL7ubSWjJLZA2qfCob_iKu0ha2-EdqDXPMY-BOuMn_tSL9xrPoUm_rEDJ4TRnY-QffK3af5I0nqhCN26V0aSJ-tkQtv-n6OgP8DB-Rx7_ObjdF3HFCl6Tae7kNguLQci-hUCwORM31L-OoQOVpphQisZ_ANBUGRWE-PBuiaoFCm1hFhUZfxTI9EWg35ZkVy4MffthgEQazXWmJ7HjV6ks1hM6NN0G70q_5Y7cDHW6-fwdAYfTbBbASYVGJ2ixtiezC4djuppzbI10808JuKtrs2fI=)
27. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG--mwrspYrkq2tjOQ8FhUdW7Y1xWTTj-enod6Gi7c7Z0TLmx5tgqepd1zWSh-j2alXEJvYmkIgIO8PigIVZqCWh9sIBRXdfh2RcFHGhpH4DbyO_KWPTADbm2Yr1r-b)
28. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUUuD0s2rX-pRkazfvZ2WQnp9qHqurzlWVK-AiGYjmNWbnKf96xdItz24Hc2wk9WFmTlP0eQhKIeSBW-GwqLhQZXnuajTw2vM2fSq_v8vSMkP4jSxKy-e4Pw==)
29. [reddit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_CCgqKE_lMHqhp-VbrvXmV8RoUUmxbJ6qmP-LCdQu-qQpYZpp915Wk-Un1_cgPij672-7GjjjQTEHiw-bAVOdzK2XQylahVh3dTjl1R5dXAjGA9ru2FbPOciwvixUv1ec_U_HA_1Vnm41CKSx4CIO1JEwKVTHZeVO4RJFtTDA2fw-oaDjKEBKGvFzh6D3HkFtJzvxT-QKIwE=)
30. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZxoszjz8qYfH2bk3BU-i-IxiTjFTKbEIXFzvh53Y49LOFx4JGhtGonlgnNdXAFrS_9-rnpQP5azaOXN25zMGFZlsgfRnZ2H0LnVTR56nOxZLBnR5711kceUoUvjCvABjYi3T315EjuoBvbRV9lCgWDhTVsaBjDsh4eGwXaXf3wrHkhEj2xTwx9nc1fSIPGD4hwetQbR31ocs=)
31. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFNKyTq-2NyVR-XZvdShqa-6ZHjASk1P9gkbeTc9CxeJb14kOz1J50NDHvL7uiPnHzQ0cMN7RxVWf-jx9PAZeXOgFXENnzQdjNUVd583lwATWmOWoOaCVr2VsFMCE=)
32. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4WCj44Mv_O0n3qgoY6mW3fI0R0UEQ0-Tg0U7oM61XS7RbIVogSD8Ipt8MAz_B22UraH99vnlMVHLJku5eeLC_onVVgd43_TsMiUqx0mpHe-IEVESafif7OyUiLomXaZz-mkMHia9HmO5uiNNBJj9_4McOIZhVQCN4zZ7PndGsqg==)
33. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCqTmR_D_KWQyOcygxfPiuTIJMUhAsDhzYvq9b1ASRUTbGTXm-jfVeC5kK_BJXQa2k1FT7NlgFgxbu8I5mApJiEvV7DNaUsV-jWTOFuJ0XWcMUJKquGzSl50mac1ufv74gc0ZrQNcV4pOb2fyY2CXu7-ReB4-cpdcroj-umOJT)
34. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoVJc0_P0Y_U5At82o9jET1yE8-qZHmWlTteAOb6tE1XOxaI_-bnMVacukCKjmCng4WmqaPhEw1DP7DnkdE5j8CfwF-EkzUKyHyTYURsMIskayXMvtRzDgT9_UAhrie8YD54Z68kBzgk0P4daRjCDWMuzdzCsrncd9G89Ml_4ij4-Sb-OKB3L4OHaWiIxRCjbwK87dQ5gD4KN_VWlPkPmPK7mHpq4LI5E=)
35. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEICmKE5FVZqW3ktG5-Myys7IvcOufbXXnvUXKBfYN0pSK1_BmGsDVZppoEMkS1w8mOkUSPwuRT2c1Q3yVskD8lOmLYe33pEfa6yQdmFhFrTzzUCI7gsrUjnUmOPA8=)
36. [scholaris.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGB-XJu7KAEnZFkVqR5AQgW3ODym8iw5fT928ML9CLaFFYJTx_DwtB7S1n97gO4kpRU6kYGYXdk8uxM0ICM8uvfj4gUUdR5FphNGJ-UqEQWaU21Dtid_zkivSKDwHhTSMCaCvv0lakVqjwnv83ryex6ic_KUFu4-Xh18rSsFXFwaSCIGiTIbkSt6q3247jBFfaC3Emcc-Kit5-LLw==)
37. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaNqHmnnAUFyl6ibCD7zbIGIG1TNdLKsru0pQ944PXMC3Kkjv4NKiV6ejXmWDqfEPSJF_58GPZS1jDD-4A4tBTQdYjLDwGgX4pGNlzGZZqcFp4qqlQMgft3KRArO-B)
38. [whiterose.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9Y6rP5sMnzUBb3NG8MthPTF3eligFYfq5Xk4bsu9iaPqF7QN5s81pVA8SmT9KNFd21puZ4z0GvohYVIkXZ3r7c4p4w2Sh1KUIUc5EhZfPEPUgyDihlrGnMYxKSLr-aFLqdaNQfVV247YB2Dc-6pjhTOXBMQyeW5GZGYeXYrw=)
39. [studysmarter.co.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHD8T2XavXYFR4_FKUE-5znixpvlpBkPEX3ZuJ5EzhCHM9TO_qx48mrNjE-wCaKeKunba2v_YGXurgGuAnO59KSombczFydmd4ekdGUElZHGvRyRUcd07Stclqn9HqRDErmL_zJkwQ1lqUWtr20hvkfmgoJ-gF6GZT0G48xwQGgZn2gGmx9tk0iClHVWGtXEQ8xXn4NRjR)
40. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbqnUbVYxPjz33bmgeLep9P6D-Ck1RtHO7axHYKdr9T3PbKeDg5goTFjBkYeVKqGL0_zC4xCOjPf5h-gkYi_XiKCCyrYJ5UyzBgGPgwk1os_RDwV8SuPOKZm-jkFmeqsqrQrWBfIvv1OEoys_EfCS0C6f90OWxtOzvrcsvoVlUuzyHm4xfkvjeDCgEKGuFDUKYhfhhrW1qJw==)


## Annotations
Annotation(end_index=3377, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERoMAUIvQG45gxPDRvpEXt4Ev3A_-b4c7SJLENumn9hsS9UIYXddVlNuJ4rq1mx7KN0M5nyskTaXgx2fXkHQofO1McdH8ux1zBP6JEfV1qTHzV0K8L3F-YqpC-JVn-b0AQk6Iit3uALo2lzf8VwR4bC6zGZCk8y05XaptjsZWz', start_index=3362)
Annotation(end_index=3377, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9Y9WOm-J_v60a6Ox5vauEJZ9XwCAYxtXnH728EV6loBi6tOk4NHtM35BD2Ewjt72PVPpxidkTTo5E12mzTlpIeCWPCPss9fLJGEcLCvr2Giwqbd1ztGjMjkfMhMlzZywdfB4zAXxjtMvOWqstKInZvHb6JypMMimOKr99Zr_hEgMBz20=', start_index=3362)
Annotation(end_index=3377, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH96jC9qPvCaR1NtsapFQgCBCY8qJxYnATMp9SVlANId1gD_gecE7uHZhkvrRG2YAf-4rHarBA15frhd_-bru3Slr2N_9qhS9saGy5ggtOO-p-7DbU-jnj2QqmEMNWFiH6JbueYP9vagef3J2SPMaPJV4Fg76ZMgQ==', start_index=3362)
Annotation(end_index=3772, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFLt5_MGQ1E7bCfczbq49CvgCQQiSdVpnws2TUfjmYBnSh16lC9ZKaL29HlrMCm5izEEf-HhEYGE2DH30B35F0mHqrDmxrW5-bgJLDeDiA9l2ONxeiF5TYoQzw2Rqf44s=', start_index=3760)
Annotation(end_index=3772, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnDItjwrr5lGATe-U6Sjssf-8WJAUBAYElK24jGVJyaQOgVWvLlw2yJyRwLc3jaPV7ZnHIez8KFFqmlc-V1JN60LZGuFQu0-83y9VPjHgHQXjtbYYCnP7Iww7cAu3ov4CUT4LO3k4uCyrlbn9KnJONYVg2tA==', start_index=3760)
Annotation(end_index=4359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGohEhUgQMdHZQi7lYYW7JhtVLQliF5yaTFK5Wf7QQdeYJfo1T9iAgtBmzalTPw3xFM1wYoDuwVqCCt-TghFfrcPvbkHP3u6oqqKZsls-p-17LY9cQ1uyzc-pYS9Njd8OqtM5WK2lYbj30e8gzbEm0Ok0FBGcX7ATrMWMv79ZP0hOEkNWfTg==', start_index=4347)
Annotation(end_index=4359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-AV1eq3rGH0b3ZtlmPb-jfkJk15-R8uyaA8wlk-5nSB-ZTegVrbBU_G8Z24rpgRbekamHVniGU_jmLwc2MZsxcx0azoJ4QmT5CyzpYHdz22F56eBt7ADr-87nc5KEhtlxkcKPzIdnM0YD0YP4t1larLHW', start_index=4347)
Annotation(end_index=5374, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTKSoDUUWX-HjidAIGbx4G7LNUsLuVZbQoredXvh5IuxMBA33inj133bFQvkOo0nk-THhb-16ibUl9MsO-aqPJov0tzLFwDhIhCL-Xf9V3DhshYHCP7Vq2hs2RxhX8kwT5rnrauWgKitbHznVB', start_index=5362)
Annotation(end_index=5374, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHX-7dvcxOrz6TRn9pkjO0GIFunlHcvUVKLGbmiBxsmVJXMINYIbuPooY9gkXMOLxgtaSvMeUUBmEAQ1y2cU6pp6vIYGsGaGczzQgozHMBrecS5WSJ4GMxZcU4Q3XNrkIUf0d75', start_index=5362)
Annotation(end_index=5700, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZtTgk2Wg6nqzNDE83gY_S4_ka_1UvTElA4OVPG3U6Hw3EezO_rL32cN92XjD0Rk-vBi7464a4mxhzRR4pfXX31gIwCAq7yr2i2nNSn6NSWEyxs_k85ikF-HyiXGY4m7uBQaw0W2HQv_YMV7Q=', start_index=5687)
Annotation(end_index=5700, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-AV1eq3rGH0b3ZtlmPb-jfkJk15-R8uyaA8wlk-5nSB-ZTegVrbBU_G8Z24rpgRbekamHVniGU_jmLwc2MZsxcx0azoJ4QmT5CyzpYHdz22F56eBt7ADr-87nc5KEhtlxkcKPzIdnM0YD0YP4t1larLHW', start_index=5687)
Annotation(end_index=5859, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCgrTdJGCVJKhL2oXa9EDY89BUXTFl-BnLNSnlrr221sKm72JJlGdQ90ZtHr6cEslzeXaZ6GnjodpIWRZq0H19MzqbsratZupPAfqPesGxdVws7LlZNl3IZ0Y_0LYAZlvq4rCpjo4zqmSOry4zBQdukYJ7jB16FeXahLj2rDzF', start_index=5842)
Annotation(end_index=5859, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4A70ck73jyiFtzeaMfNt7XHR62DAfah98qzcciLCFLioElOuNT1k0PLBVaccap7BxEMsvhYQtYR3bKTuASRHCuIiiegzMIwS4ndpYNxBrZ0-qATtYwSgjiQ3j7gYLWnpFOwR5ah2WP9SEeBa6RTaIGuAENf4smcYKTe9-JbEXll2qz7gsfqBu-wTlv6yn427IwIWl3i9O_BxT-g==', start_index=5842)
Annotation(end_index=5859, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-AV1eq3rGH0b3ZtlmPb-jfkJk15-R8uyaA8wlk-5nSB-ZTegVrbBU_G8Z24rpgRbekamHVniGU_jmLwc2MZsxcx0azoJ4QmT5CyzpYHdz22F56eBt7ADr-87nc5KEhtlxkcKPzIdnM0YD0YP4t1larLHW', start_index=5842)
Annotation(end_index=6192, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3GTBELlpR4g6CZTf_5n8ISnAMy80dBUkAk4tixIph6dPw1Te7IiuPbONOq452itCT9ECdsGfueItmcO5KzDjEc9ouFK4c37g3LN7ZsufKG6HvDnp_5ebI6h5lNFKFLNekCvNk6wpuXlr7sjFQ1SyYSaUYQByywYJBYDPmZ1QUDQ==', start_index=6178)
Annotation(end_index=6192, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYz1zvwNQWt3Fc7Oggpik1S4fa34Nbt6m2w4Hy2QS8k8EnDYEL41I5NJ6dNgBTpzQQeIrQOVOyUG_V1MVLR28FJQ7_9cSFJQ3RP2bbusB1Fb9sJCvdCKpu0oVYMQPH0ZijbW8JC5mI1gTlVcOM38MyXqKW3_Qvaty2rp5nN0gZg0cq_TezKydeY3564bOuoDZnEejHXPXdtK2ldg==', start_index=6178)
Annotation(end_index=6977, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERoMAUIvQG45gxPDRvpEXt4Ev3A_-b4c7SJLENumn9hsS9UIYXddVlNuJ4rq1mx7KN0M5nyskTaXgx2fXkHQofO1McdH8ux1zBP6JEfV1qTHzV0K8L3F-YqpC-JVn-b0AQk6Iit3uALo2lzf8VwR4bC6zGZCk8y05XaptjsZWz', start_index=6964)
Annotation(end_index=6977, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3jg4Nl9i9LUh354hhH2z3OHuK05uDWpsOMFEgIbzA9sSIA2S5v7rMVdFm6T8eXAbN5N_CpY49-a0V3-izid5GT1loEY1uhTvVlD1tRG0Wq-l6C4aNM6NCNQ4cpYUEJg==', start_index=6964)
Annotation(end_index=7328, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfKfEtDQQbc__ZwjZ6HZJvWcEgbMxQgTbcXZC3UIr1dibDUwIlwU8i5368U_17ZA9E1tMLweg2UOc00hNJoo0-Piqio0p6jdWTTRlCWIo5HJv9-GcIIcaVozL8-KfnNvuvrOFwF6mPDZQR0TbMC7NkNYYIKHMt0s3Ky1UNJdmhCLJgU0qgw5TKYfZsf5P6KBHn_9yiDGEgmqnxQNeeM8A9sXUETanhvK3SbL2jng5lMSwFkZw=', start_index=7314)
Annotation(end_index=7328, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYz1zvwNQWt3Fc7Oggpik1S4fa34Nbt6m2w4Hy2QS8k8EnDYEL41I5NJ6dNgBTpzQQeIrQOVOyUG_V1MVLR28FJQ7_9cSFJQ3RP2bbusB1Fb9sJCvdCKpu0oVYMQPH0ZijbW8JC5mI1gTlVcOM38MyXqKW3_Qvaty2rp5nN0gZg0cq_TezKydeY3564bOuoDZnEejHXPXdtK2ldg==', start_index=7314)
Annotation(end_index=8183, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9HNGHDr91vG-dGna9j9KbsO_fU5sXulGAiHm6dmXIQeRBxlKZrLuOILwLhh78a4l9sBbOcC7fex2Q0_Pcqew3jUrdPFObLBAWXueAe0tSqJHrouBRhvBWUaI5nRz-Hb08D9Zo4Mtys-BaO-5oMJa2Xi5mwFJAI69haBkkTlph5yu-BogrFfGD2fFMfhKnB1OE6nOwGOI7YLak6ZaLN36GU1AUGEe3RfiCeZaAUMI8xMokhaU=', start_index=8166)
Annotation(end_index=8183, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3jg4Nl9i9LUh354hhH2z3OHuK05uDWpsOMFEgIbzA9sSIA2S5v7rMVdFm6T8eXAbN5N_CpY49-a0V3-izid5GT1loEY1uhTvVlD1tRG0Wq-l6C4aNM6NCNQ4cpYUEJg==', start_index=8166)
Annotation(end_index=8183, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-AV1eq3rGH0b3ZtlmPb-jfkJk15-R8uyaA8wlk-5nSB-ZTegVrbBU_G8Z24rpgRbekamHVniGU_jmLwc2MZsxcx0azoJ4QmT5CyzpYHdz22F56eBt7ADr-87nc5KEhtlxkcKPzIdnM0YD0YP4t1larLHW', start_index=8166)
Annotation(end_index=8535, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-AV1eq3rGH0b3ZtlmPb-jfkJk15-R8uyaA8wlk-5nSB-ZTegVrbBU_G8Z24rpgRbekamHVniGU_jmLwc2MZsxcx0azoJ4QmT5CyzpYHdz22F56eBt7ADr-87nc5KEhtlxkcKPzIdnM0YD0YP4t1larLHW', start_index=8526)
Annotation(end_index=9383, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGohEhUgQMdHZQi7lYYW7JhtVLQliF5yaTFK5Wf7QQdeYJfo1T9iAgtBmzalTPw3xFM1wYoDuwVqCCt-TghFfrcPvbkHP3u6oqqKZsls-p-17LY9cQ1uyzc-pYS9Njd8OqtM5WK2lYbj30e8gzbEm0Ok0FBGcX7ATrMWMv79ZP0hOEkNWfTg==', start_index=9370)
Annotation(end_index=9383, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2fvOiAIhLwrUqY7mhEeK8_Wu0UqRoHHVv1fmEKXmUqVlXffEg_wi9itADdcTDxf0xG0to5n0Tm85XO0Fh0qPT1OfvNDFS6tAIladmDagzqpgB5YGAZhJAT8KZ7tLtilt1_Ie_YMaWidKG', start_index=9370)
Annotation(end_index=9703, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFw-hgx0xIAw9xmGLFiYgZUivClj-4qfogpGXGxv_MnEwITa8sFYLK_dWqlB7QId9mVSk8FMeD_g3s2e5EPum9sIleRbImJfc56cCcZFBgozwPu27EZEDGfCVYbaB_ZQl0l_I0JQT8', start_index=9685)
Annotation(end_index=9703, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvbszqLvofhhunndM02jkrRPV1zPX-gmtYBg_PD5ObA-ylIOG4sz5dYi-UEfnlyZxb83H1IbHGWd6yu9zKSP85PXlQScU6X8o38yZhuvnG6RD_Vp3MkKObtwqW-1aOlotFIN-zIczVvvuOHfzbTv8rizb4HjNfbNdt0g==', start_index=9685)
Annotation(end_index=9703, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy36GBgHhNJaDb1XNcJ0eVxqCN_zRyH9scZffwtzSwUo1MiG4XZ71R4DqJfhl3x0EBqritQGNVgN6PivKsJEh1Xw_9UylY4u2TSsEuz5TOogs0VWOi1ZG2sjV6-PuvUKRYfOKSlX6wCpbRsTcam5VBbcco9M5YWadjCOOJOxXlqXB-GB47i_WCyaVtRQU6HssAyO7mUnGU2pO5CDbgY-1qRQgC4JtSBiD15u2o-UuRgWApYanwXRjEVTDeF-GAvA==', start_index=9685)
Annotation(end_index=10022, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCgrTdJGCVJKhL2oXa9EDY89BUXTFl-BnLNSnlrr221sKm72JJlGdQ90ZtHr6cEslzeXaZ6GnjodpIWRZq0H19MzqbsratZupPAfqPesGxdVws7LlZNl3IZ0Y_0LYAZlvq4rCpjo4zqmSOry4zBQdukYJ7jB16FeXahLj2rDzF', start_index=10008)
Annotation(end_index=10022, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2fvOiAIhLwrUqY7mhEeK8_Wu0UqRoHHVv1fmEKXmUqVlXffEg_wi9itADdcTDxf0xG0to5n0Tm85XO0Fh0qPT1OfvNDFS6tAIladmDagzqpgB5YGAZhJAT8KZ7tLtilt1_Ie_YMaWidKG', start_index=10008)
Annotation(end_index=10201, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCgrTdJGCVJKhL2oXa9EDY89BUXTFl-BnLNSnlrr221sKm72JJlGdQ90ZtHr6cEslzeXaZ6GnjodpIWRZq0H19MzqbsratZupPAfqPesGxdVws7LlZNl3IZ0Y_0LYAZlvq4rCpjo4zqmSOry4zBQdukYJ7jB16FeXahLj2rDzF', start_index=10187)
Annotation(end_index=10201, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2fvOiAIhLwrUqY7mhEeK8_Wu0UqRoHHVv1fmEKXmUqVlXffEg_wi9itADdcTDxf0xG0to5n0Tm85XO0Fh0qPT1OfvNDFS6tAIladmDagzqpgB5YGAZhJAT8KZ7tLtilt1_Ie_YMaWidKG', start_index=10187)
Annotation(end_index=10431, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFw-hgx0xIAw9xmGLFiYgZUivClj-4qfogpGXGxv_MnEwITa8sFYLK_dWqlB7QId9mVSk8FMeD_g3s2e5EPum9sIleRbImJfc56cCcZFBgozwPu27EZEDGfCVYbaB_ZQl0l_I0JQT8', start_index=10417)
Annotation(end_index=10431, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIOd6OvFU3tz-sivBZ3mJvXAE8i1P1iIFfDTZ3I7Wthne-FBte-Lf82wRhki0njPRoqbWE2OFacmu5OsVwauN7MfAqLe6-v2RfbUvwRMqkGt6fN5Xg4iJ5aZf-ilc74zhgddzdueV_WDkt6rxAnKzvoRYKThrEFPzuY7kylpKM9RuwlG0alPnUFGjVS6TqQVvE48pgNwjXy6TtRc4SYB5ipXcQuwKz5H1i4Tf3EMbdU24=', start_index=10417)
Annotation(end_index=11223, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERoMAUIvQG45gxPDRvpEXt4Ev3A_-b4c7SJLENumn9hsS9UIYXddVlNuJ4rq1mx7KN0M5nyskTaXgx2fXkHQofO1McdH8ux1zBP6JEfV1qTHzV0K8L3F-YqpC-JVn-b0AQk6Iit3uALo2lzf8VwR4bC6zGZCk8y05XaptjsZWz', start_index=11214)
Annotation(end_index=11559, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFq_2XJKm9Wm6CyRTitUtJ_LiC9P27jfIzXPVfdSud4-nicoHXFyPdvlxHpvrrHSMNzfgj2tiJ_-V_jEk0vqFX7IHlVTFSMIDbdNvRdBlTSJ5Dmb748HuNmYeuao-33V30Iu-dolnjA9kYaoGO1ABhd6--0gTM9fzwlyf7INvyC', start_index=11545)
Annotation(end_index=11559, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCrv6UZfo9CaIdZB8M1bH9lPs7Bb8HyYnU0ik5TlxNrLii_7ysz2IIH_WvHHIqeImB1CWhnFjtJJJb9uM82sT1yBF2glKKZxtgdwVgI20f5N-B4CDaECsySoOPFapVZdj-CBQuX4oM5vm08Cw-RDqZnbMhEDKkR1sy-BW-RSDtdi7v0FmsPVLTQBe1oYHe1hSEVRENEo6dtRXUTMwvJ5wtDigIhqqkWCszeyVNzgbDkNZa0rQCSDbtuMMdnH-xUF9x5jIpiY5o', start_index=11545)
Annotation(end_index=11855, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGS78iBbosMAV4yf97pnud4k65LAfDQRs9HguD2XKQ9HPaF7BLsp1b8vhvw3wtG4SK96-nlrAN2Qwbty66qGdH8katFcWYFOKiVgbpm8nuTtA1SMa0z970cpIzu_hVdG8nlbxddpsGZxKIMAohH4vi7RSHs_vU8NzLIczLREiGv4sq6MqQ2X1gOut9mz-oDI8Cy06GvFEEb8wSC', start_index=11842)
Annotation(end_index=11855, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-AV1eq3rGH0b3ZtlmPb-jfkJk15-R8uyaA8wlk-5nSB-ZTegVrbBU_G8Z24rpgRbekamHVniGU_jmLwc2MZsxcx0azoJ4QmT5CyzpYHdz22F56eBt7ADr-87nc5KEhtlxkcKPzIdnM0YD0YP4t1larLHW', start_index=11842)
Annotation(end_index=12295, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfKfEtDQQbc__ZwjZ6HZJvWcEgbMxQgTbcXZC3UIr1dibDUwIlwU8i5368U_17ZA9E1tMLweg2UOc00hNJoo0-Piqio0p6jdWTTRlCWIo5HJv9-GcIIcaVozL8-KfnNvuvrOFwF6mPDZQR0TbMC7NkNYYIKHMt0s3Ky1UNJdmhCLJgU0qgw5TKYfZsf5P6KBHn_9yiDGEgmqnxQNeeM8A9sXUETanhvK3SbL2jng5lMSwFkZw=', start_index=12281)
Annotation(end_index=12295, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3jg4Nl9i9LUh354hhH2z3OHuK05uDWpsOMFEgIbzA9sSIA2S5v7rMVdFm6T8eXAbN5N_CpY49-a0V3-izid5GT1loEY1uhTvVlD1tRG0Wq-l6C4aNM6NCNQ4cpYUEJg==', start_index=12281)
Annotation(end_index=12525, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-AV1eq3rGH0b3ZtlmPb-jfkJk15-R8uyaA8wlk-5nSB-ZTegVrbBU_G8Z24rpgRbekamHVniGU_jmLwc2MZsxcx0azoJ4QmT5CyzpYHdz22F56eBt7ADr-87nc5KEhtlxkcKPzIdnM0YD0YP4t1larLHW', start_index=12516)
Annotation(end_index=12929, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4A70ck73jyiFtzeaMfNt7XHR62DAfah98qzcciLCFLioElOuNT1k0PLBVaccap7BxEMsvhYQtYR3bKTuASRHCuIiiegzMIwS4ndpYNxBrZ0-qATtYwSgjiQ3j7gYLWnpFOwR5ah2WP9SEeBa6RTaIGuAENf4smcYKTe9-JbEXll2qz7gsfqBu-wTlv6yn427IwIWl3i9O_BxT-g==', start_index=12919)
Annotation(end_index=13187, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfKfEtDQQbc__ZwjZ6HZJvWcEgbMxQgTbcXZC3UIr1dibDUwIlwU8i5368U_17ZA9E1tMLweg2UOc00hNJoo0-Piqio0p6jdWTTRlCWIo5HJv9-GcIIcaVozL8-KfnNvuvrOFwF6mPDZQR0TbMC7NkNYYIKHMt0s3Ky1UNJdmhCLJgU0qgw5TKYfZsf5P6KBHn_9yiDGEgmqnxQNeeM8A9sXUETanhvK3SbL2jng5lMSwFkZw=', start_index=13177)
Annotation(end_index=13323, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4A70ck73jyiFtzeaMfNt7XHR62DAfah98qzcciLCFLioElOuNT1k0PLBVaccap7BxEMsvhYQtYR3bKTuASRHCuIiiegzMIwS4ndpYNxBrZ0-qATtYwSgjiQ3j7gYLWnpFOwR5ah2WP9SEeBa6RTaIGuAENf4smcYKTe9-JbEXll2qz7gsfqBu-wTlv6yn427IwIWl3i9O_BxT-g==', start_index=13313)
Annotation(end_index=14123, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFw-hgx0xIAw9xmGLFiYgZUivClj-4qfogpGXGxv_MnEwITa8sFYLK_dWqlB7QId9mVSk8FMeD_g3s2e5EPum9sIleRbImJfc56cCcZFBgozwPu27EZEDGfCVYbaB_ZQl0l_I0JQT8', start_index=14105)
Annotation(end_index=14123, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy36GBgHhNJaDb1XNcJ0eVxqCN_zRyH9scZffwtzSwUo1MiG4XZ71R4DqJfhl3x0EBqritQGNVgN6PivKsJEh1Xw_9UylY4u2TSsEuz5TOogs0VWOi1ZG2sjV6-PuvUKRYfOKSlX6wCpbRsTcam5VBbcco9M5YWadjCOOJOxXlqXB-GB47i_WCyaVtRQU6HssAyO7mUnGU2pO5CDbgY-1qRQgC4JtSBiD15u2o-UuRgWApYanwXRjEVTDeF-GAvA==', start_index=14105)
Annotation(end_index=14123, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyG38mjuZkrNajwIpSEoNWWF5ltf6H-eQnzxm1qLlUDped6NuGn6pTIFu57XWnHHGHe9EZU36ZSpRvbF0YQqyckC--mXu5-fePgWOsMAFF8fSIRNkpsS4aDLZ8KO9zCECNDmn0gjaL7ubSWjJLZA2qfCob_iKu0ha2-EdqDXPMY-BOuMn_tSL9xrPoUm_rEDJ4TRnY-QffK3af5I0nqhCN26V0aSJ-tkQtv-n6OgP8DB-Rx7_ObjdF3HFCl6Tae7kNguLQci-hUCwORM31L-OoQOVpphQisZ_ANBUGRWE-PBuiaoFCm1hFhUZfxTI9EWg35ZkVy4MffthgEQazXWmJ7HjV6ks1hM6NN0G70q_5Y7cDHW6-fwdAYfTbBbASYVGJ2ixtiezC4djuppzbI10808JuKtrs2fI=', start_index=14105)
Annotation(end_index=14837, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-AV1eq3rGH0b3ZtlmPb-jfkJk15-R8uyaA8wlk-5nSB-ZTegVrbBU_G8Z24rpgRbekamHVniGU_jmLwc2MZsxcx0azoJ4QmT5CyzpYHdz22F56eBt7ADr-87nc5KEhtlxkcKPzIdnM0YD0YP4t1larLHW', start_index=14828)
Annotation(end_index=15354, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERoMAUIvQG45gxPDRvpEXt4Ev3A_-b4c7SJLENumn9hsS9UIYXddVlNuJ4rq1mx7KN0M5nyskTaXgx2fXkHQofO1McdH8ux1zBP6JEfV1qTHzV0K8L3F-YqpC-JVn-b0AQk6Iit3uALo2lzf8VwR4bC6zGZCk8y05XaptjsZWz', start_index=15345)
Annotation(end_index=16463, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFLt5_MGQ1E7bCfczbq49CvgCQQiSdVpnws2TUfjmYBnSh16lC9ZKaL29HlrMCm5izEEf-HhEYGE2DH30B35F0mHqrDmxrW5-bgJLDeDiA9l2ONxeiF5TYoQzw2Rqf44s=', start_index=16450)
Annotation(end_index=16463, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG--mwrspYrkq2tjOQ8FhUdW7Y1xWTTj-enod6Gi7c7Z0TLmx5tgqepd1zWSh-j2alXEJvYmkIgIO8PigIVZqCWh9sIBRXdfh2RcFHGhpH4DbyO_KWPTADbm2Yr1r-b', start_index=16450)
Annotation(end_index=16954, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUUuD0s2rX-pRkazfvZ2WQnp9qHqurzlWVK-AiGYjmNWbnKf96xdItz24Hc2wk9WFmTlP0eQhKIeSBW-GwqLhQZXnuajTw2vM2fSq_v8vSMkP4jSxKy-e4Pw==', start_index=16937)
Annotation(end_index=16954, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG--mwrspYrkq2tjOQ8FhUdW7Y1xWTTj-enod6Gi7c7Z0TLmx5tgqepd1zWSh-j2alXEJvYmkIgIO8PigIVZqCWh9sIBRXdfh2RcFHGhpH4DbyO_KWPTADbm2Yr1r-b', start_index=16937)
Annotation(end_index=16954, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGohEhUgQMdHZQi7lYYW7JhtVLQliF5yaTFK5Wf7QQdeYJfo1T9iAgtBmzalTPw3xFM1wYoDuwVqCCt-TghFfrcPvbkHP3u6oqqKZsls-p-17LY9cQ1uyzc-pYS9Njd8OqtM5WK2lYbj30e8gzbEm0Ok0FBGcX7ATrMWMv79ZP0hOEkNWfTg==', start_index=16937)
Annotation(end_index=17225, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG--mwrspYrkq2tjOQ8FhUdW7Y1xWTTj-enod6Gi7c7Z0TLmx5tgqepd1zWSh-j2alXEJvYmkIgIO8PigIVZqCWh9sIBRXdfh2RcFHGhpH4DbyO_KWPTADbm2Yr1r-b', start_index=17215)
Annotation(end_index=19255, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-AV1eq3rGH0b3ZtlmPb-jfkJk15-R8uyaA8wlk-5nSB-ZTegVrbBU_G8Z24rpgRbekamHVniGU_jmLwc2MZsxcx0azoJ4QmT5CyzpYHdz22F56eBt7ADr-87nc5KEhtlxkcKPzIdnM0YD0YP4t1larLHW', start_index=19246)
Annotation(end_index=19586, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-AV1eq3rGH0b3ZtlmPb-jfkJk15-R8uyaA8wlk-5nSB-ZTegVrbBU_G8Z24rpgRbekamHVniGU_jmLwc2MZsxcx0azoJ4QmT5CyzpYHdz22F56eBt7ADr-87nc5KEhtlxkcKPzIdnM0YD0YP4t1larLHW', start_index=19577)
Annotation(end_index=19963, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFq_2XJKm9Wm6CyRTitUtJ_LiC9P27jfIzXPVfdSud4-nicoHXFyPdvlxHpvrrHSMNzfgj2tiJ_-V_jEk0vqFX7IHlVTFSMIDbdNvRdBlTSJ5Dmb748HuNmYeuao-33V30Iu-dolnjA9kYaoGO1ABhd6--0gTM9fzwlyf7INvyC', start_index=19949)
Annotation(end_index=19963, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_CCgqKE_lMHqhp-VbrvXmV8RoUUmxbJ6qmP-LCdQu-qQpYZpp915Wk-Un1_cgPij672-7GjjjQTEHiw-bAVOdzK2XQylahVh3dTjl1R5dXAjGA9ru2FbPOciwvixUv1ec_U_HA_1Vnm41CKSx4CIO1JEwKVTHZeVO4RJFtTDA2fw-oaDjKEBKGvFzh6D3HkFtJzvxT-QKIwE=', start_index=19949)
Annotation(end_index=20102, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZtTgk2Wg6nqzNDE83gY_S4_ka_1UvTElA4OVPG3U6Hw3EezO_rL32cN92XjD0Rk-vBi7464a4mxhzRR4pfXX31gIwCAq7yr2i2nNSn6NSWEyxs_k85ikF-HyiXGY4m7uBQaw0W2HQv_YMV7Q=', start_index=20092)
Annotation(end_index=20693, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCgrTdJGCVJKhL2oXa9EDY89BUXTFl-BnLNSnlrr221sKm72JJlGdQ90ZtHr6cEslzeXaZ6GnjodpIWRZq0H19MzqbsratZupPAfqPesGxdVws7LlZNl3IZ0Y_0LYAZlvq4rCpjo4zqmSOry4zBQdukYJ7jB16FeXahLj2rDzF', start_index=20679)
Annotation(end_index=20693, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2fvOiAIhLwrUqY7mhEeK8_Wu0UqRoHHVv1fmEKXmUqVlXffEg_wi9itADdcTDxf0xG0to5n0Tm85XO0Fh0qPT1OfvNDFS6tAIladmDagzqpgB5YGAZhJAT8KZ7tLtilt1_Ie_YMaWidKG', start_index=20679)
Annotation(end_index=20789, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCgrTdJGCVJKhL2oXa9EDY89BUXTFl-BnLNSnlrr221sKm72JJlGdQ90ZtHr6cEslzeXaZ6GnjodpIWRZq0H19MzqbsratZupPAfqPesGxdVws7LlZNl3IZ0Y_0LYAZlvq4rCpjo4zqmSOry4zBQdukYJ7jB16FeXahLj2rDzF', start_index=20775)
Annotation(end_index=20789, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2fvOiAIhLwrUqY7mhEeK8_Wu0UqRoHHVv1fmEKXmUqVlXffEg_wi9itADdcTDxf0xG0to5n0Tm85XO0Fh0qPT1OfvNDFS6tAIladmDagzqpgB5YGAZhJAT8KZ7tLtilt1_Ie_YMaWidKG', start_index=20775)
Annotation(end_index=21126, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZxoszjz8qYfH2bk3BU-i-IxiTjFTKbEIXFzvh53Y49LOFx4JGhtGonlgnNdXAFrS_9-rnpQP5azaOXN25zMGFZlsgfRnZ2H0LnVTR56nOxZLBnR5711kceUoUvjCvABjYi3T315EjuoBvbRV9lCgWDhTVsaBjDsh4eGwXaXf3wrHkhEj2xTwx9nc1fSIPGD4hwetQbR31ocs=', start_index=21112)
Annotation(end_index=21126, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCgrTdJGCVJKhL2oXa9EDY89BUXTFl-BnLNSnlrr221sKm72JJlGdQ90ZtHr6cEslzeXaZ6GnjodpIWRZq0H19MzqbsratZupPAfqPesGxdVws7LlZNl3IZ0Y_0LYAZlvq4rCpjo4zqmSOry4zBQdukYJ7jB16FeXahLj2rDzF', start_index=21112)
Annotation(end_index=21736, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFNKyTq-2NyVR-XZvdShqa-6ZHjASk1P9gkbeTc9CxeJb14kOz1J50NDHvL7uiPnHzQ0cMN7RxVWf-jx9PAZeXOgFXENnzQdjNUVd583lwATWmOWoOaCVr2VsFMCE=', start_index=21723)
Annotation(end_index=21736, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnDItjwrr5lGATe-U6Sjssf-8WJAUBAYElK24jGVJyaQOgVWvLlw2yJyRwLc3jaPV7ZnHIez8KFFqmlc-V1JN60LZGuFQu0-83y9VPjHgHQXjtbYYCnP7Iww7cAu3ov4CUT4LO3k4uCyrlbn9KnJONYVg2tA==', start_index=21723)
Annotation(end_index=22014, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4WCj44Mv_O0n3qgoY6mW3fI0R0UEQ0-Tg0U7oM61XS7RbIVogSD8Ipt8MAz_B22UraH99vnlMVHLJku5eeLC_onVVgd43_TsMiUqx0mpHe-IEVESafif7OyUiLomXaZz-mkMHia9HmO5uiNNBJj9_4McOIZhVQCN4zZ7PndGsqg==', start_index=22000)
Annotation(end_index=22014, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCqTmR_D_KWQyOcygxfPiuTIJMUhAsDhzYvq9b1ASRUTbGTXm-jfVeC5kK_BJXQa2k1FT7NlgFgxbu8I5mApJiEvV7DNaUsV-jWTOFuJ0XWcMUJKquGzSl50mac1ufv74gc0ZrQNcV4pOb2fyY2CXu7-ReB4-cpdcroj-umOJT', start_index=22000)
Annotation(end_index=22399, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyG38mjuZkrNajwIpSEoNWWF5ltf6H-eQnzxm1qLlUDped6NuGn6pTIFu57XWnHHGHe9EZU36ZSpRvbF0YQqyckC--mXu5-fePgWOsMAFF8fSIRNkpsS4aDLZ8KO9zCECNDmn0gjaL7ubSWjJLZA2qfCob_iKu0ha2-EdqDXPMY-BOuMn_tSL9xrPoUm_rEDJ4TRnY-QffK3af5I0nqhCN26V0aSJ-tkQtv-n6OgP8DB-Rx7_ObjdF3HFCl6Tae7kNguLQci-hUCwORM31L-OoQOVpphQisZ_ANBUGRWE-PBuiaoFCm1hFhUZfxTI9EWg35ZkVy4MffthgEQazXWmJ7HjV6ks1hM6NN0G70q_5Y7cDHW6-fwdAYfTbBbASYVGJ2ixtiezC4djuppzbI10808JuKtrs2fI=', start_index=22389)
Annotation(end_index=22905, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFLt5_MGQ1E7bCfczbq49CvgCQQiSdVpnws2TUfjmYBnSh16lC9ZKaL29HlrMCm5izEEf-HhEYGE2DH30B35F0mHqrDmxrW5-bgJLDeDiA9l2ONxeiF5TYoQzw2Rqf44s=', start_index=22892)
Annotation(end_index=22905, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoVJc0_P0Y_U5At82o9jET1yE8-qZHmWlTteAOb6tE1XOxaI_-bnMVacukCKjmCng4WmqaPhEw1DP7DnkdE5j8CfwF-EkzUKyHyTYURsMIskayXMvtRzDgT9_UAhrie8YD54Z68kBzgk0P4daRjCDWMuzdzCsrncd9G89Ml_4ij4-Sb-OKB3L4OHaWiIxRCjbwK87dQ5gD4KN_VWlPkPmPK7mHpq4LI5E=', start_index=22892)
Annotation(end_index=23158, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFLt5_MGQ1E7bCfczbq49CvgCQQiSdVpnws2TUfjmYBnSh16lC9ZKaL29HlrMCm5izEEf-HhEYGE2DH30B35F0mHqrDmxrW5-bgJLDeDiA9l2ONxeiF5TYoQzw2Rqf44s=', start_index=23149)
Annotation(end_index=23712, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEICmKE5FVZqW3ktG5-Myys7IvcOufbXXnvUXKBfYN0pSK1_BmGsDVZppoEMkS1w8mOkUSPwuRT2c1Q3yVskD8lOmLYe33pEfa6yQdmFhFrTzzUCI7gsrUjnUmOPA8=', start_index=23694)
Annotation(end_index=23712, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGB-XJu7KAEnZFkVqR5AQgW3ODym8iw5fT928ML9CLaFFYJTx_DwtB7S1n97gO4kpRU6kYGYXdk8uxM0ICM8uvfj4gUUdR5FphNGJ-UqEQWaU21Dtid_zkivSKDwHhTSMCaCvv0lakVqjwnv83ryex6ic_KUFu4-Xh18rSsFXFwaSCIGiTIbkSt6q3247jBFfaC3Emcc-Kit5-LLw==', start_index=23694)
Annotation(end_index=23712, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCrv6UZfo9CaIdZB8M1bH9lPs7Bb8HyYnU0ik5TlxNrLii_7ysz2IIH_WvHHIqeImB1CWhnFjtJJJb9uM82sT1yBF2glKKZxtgdwVgI20f5N-B4CDaECsySoOPFapVZdj-CBQuX4oM5vm08Cw-RDqZnbMhEDKkR1sy-BW-RSDtdi7v0FmsPVLTQBe1oYHe1hSEVRENEo6dtRXUTMwvJ5wtDigIhqqkWCszeyVNzgbDkNZa0rQCSDbtuMMdnH-xUF9x5jIpiY5o', start_index=23694)
Annotation(end_index=24122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-AV1eq3rGH0b3ZtlmPb-jfkJk15-R8uyaA8wlk-5nSB-ZTegVrbBU_G8Z24rpgRbekamHVniGU_jmLwc2MZsxcx0azoJ4QmT5CyzpYHdz22F56eBt7ADr-87nc5KEhtlxkcKPzIdnM0YD0YP4t1larLHW', start_index=24109)
Annotation(end_index=24122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaNqHmnnAUFyl6ibCD7zbIGIG1TNdLKsru0pQ944PXMC3Kkjv4NKiV6ejXmWDqfEPSJF_58GPZS1jDD-4A4tBTQdYjLDwGgX4pGNlzGZZqcFp4qqlQMgft3KRArO-B', start_index=24109)
Annotation(end_index=24581, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFw-hgx0xIAw9xmGLFiYgZUivClj-4qfogpGXGxv_MnEwITa8sFYLK_dWqlB7QId9mVSk8FMeD_g3s2e5EPum9sIleRbImJfc56cCcZFBgozwPu27EZEDGfCVYbaB_ZQl0l_I0JQT8', start_index=24567)
Annotation(end_index=24581, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9Y6rP5sMnzUBb3NG8MthPTF3eligFYfq5Xk4bsu9iaPqF7QN5s81pVA8SmT9KNFd21puZ4z0GvohYVIkXZ3r7c4p4w2Sh1KUIUc5EhZfPEPUgyDihlrGnMYxKSLr-aFLqdaNQfVV247YB2Dc-6pjhTOXBMQyeW5GZGYeXYrw=', start_index=24567)
Annotation(end_index=24980, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHD8T2XavXYFR4_FKUE-5znixpvlpBkPEX3ZuJ5EzhCHM9TO_qx48mrNjE-wCaKeKunba2v_YGXurgGuAnO59KSombczFydmd4ekdGUElZHGvRyRUcd07Stclqn9HqRDErmL_zJkwQ1lqUWtr20hvkfmgoJ-gF6GZT0G48xwQGgZn2gGmx9tk0iClHVWGtXEQ8xXn4NRjR', start_index=24966)
Annotation(end_index=24980, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbqnUbVYxPjz33bmgeLep9P6D-Ck1RtHO7axHYKdr9T3PbKeDg5goTFjBkYeVKqGL0_zC4xCOjPf5h-gkYi_XiKCCyrYJ5UyzBgGPgwk1os_RDwV8SuPOKZm-jkFmeqsqrQrWBfIvv1OEoys_EfCS0C6f90OWxtOzvrcsvoVlUuzyHm4xfkvjeDCgEKGuFDUKYhfhhrW1qJw==', start_index=24966)

## Sources
