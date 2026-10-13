# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 77fc0121 | **Time:** 347.38s | **Cost:** $1.17597
--------------------------------------------------------------------------------

# Optimization of Momentum Wheel Redundancy Configurations for Satellite Attitude Control Under Strict Mass Constraints

**Key Points**
*   **Optimal Configuration:** The **four-wheel pyramidal configuration** is widely identified as the optimal architecture for balancing reliability, pointing accuracy, and weight constraints. It provides single-fault tolerance (N-1 reliability) with the minimum mass penalty compared to orthogonal three-wheel systems [cite: 1, 2].
*   **Geometric Optimization:** A tilt angle (cant angle) of approximately **35.26°** ($\arcsin(1/\sqrt{3})$) relative to the base plane is mathematically optimal for creating a spherical momentum envelope, ensuring isotropic torque capacity and maximizing agility per unit of wheel mass [cite: 3].
*   **Reliability vs. Mass:** While six-wheel configurations offer superior redundancy, they generally exceed strict weight budgets. The four-wheel pyramid allows for the redistribution of torque via null-space control algorithms, maintaining three-axis stabilization even after the failure of one actuator, albeit with reduced peak torque capacity [cite: 4, 5].
*   **Pointing Accuracy:** Advanced control laws (e.g., Sliding Mode, Lyapunov-based) applied to pyramidal arrays can achieve pointing accuracies better than $0.01^\circ$, comparable to orthogonal configurations, while offering superior robustness against disturbances [cite: 1, 4].
*   **Power Efficiency:** Utilization of the configuration's "null space" allows for torque distribution strategies that minimize power consumption and prevent wheel saturation, indirectly benefiting the weight budget by reducing power subsystem requirements [cite: 6, 7].

---

## 1. Introduction

The Attitude Determination and Control System (ADCS) is a critical subsystem governing the operational capability of a spacecraft. For missions requiring high-precision pointing—such as Earth observation, astronomical telescopy, or laser communication—three-axis stabilization using momentum exchange devices is the standard approach [cite: 1, 8]. However, the mechanical nature of reaction wheels (RWs) and momentum wheels makes them susceptible to failure mechanisms such as bearing wear, lubrication breakdown, and electronics faults [cite: 9, 10]. Consequently, redundancy is a strict requirement for high-reliability missions.

The central engineering challenge lies in the conflict between reliability and mass. Adding redundant actuators increases the satellite's dry mass and power consumption, which is often prohibitive for small satellites or missions with strict weight budgets [cite: 8, 11]. Therefore, the optimization of the reaction wheel configuration is not merely a geometric exercise but a multidisciplinary problem involving dynamics, control theory, and systems engineering.

This report analyzes the momentum wheel redundancy configurations that maximize reliability and pointing accuracy while adhering to strict weight limits. The analysis identifies the four-wheel pyramidal configuration as the global optimum for this constrained problem and details the geometric and algorithmic parameters required to maximize its performance.

## 2. Reaction Wheel Configurations and Mass Trade-offs

To select an optimal configuration, one must evaluate the available architectures against the specific constraints of mass and fault tolerance.

### 2.1 Orthogonal Three-Wheel Configuration
The baseline for three-axis stabilization is a set of three reaction wheels mounted orthogonally along the spacecraft's principal axes ($X_b, Y_b, Z_b$).
*   **Mass:** This is the minimum mass solution, representing the lower bound of the weight budget [cite: 1].
*   **Reliability:** This configuration possesses zero redundancy. The failure of a single wheel results in the loss of control authority along that axis, typically leading to mission failure or a reversion to a degraded magnetic control mode [cite: 12].
*   **Performance:** While capable of high pointing accuracy ($<0.001^\circ$ in specific conditions), the lack of fault tolerance makes it unsuitable for high-reliability missions [cite: 12].

### 2.2 Six-Wheel Configurations
Missions with relaxed mass constraints, such as the Hubble Space Telescope or large geostationary satellites, often employ six wheels (e.g., two per axis or a dodecahedral arrangement) to ensure double-fault tolerance [cite: 3].
*   **Mass:** High. Requires double the actuator mass and volume of the baseline, plus associated power electronics.
*   **Suitability:** Generally excluded from "strict weight budget" scenarios typical of modern small satellites or cost-capped missions [cite: 8].

### 2.3 Four-Wheel Redundant Configurations
The four-wheel cluster represents the minimum hardware set required to achieve single-fault tolerance (N-1 reliability). This configuration adds only 33% more actuator mass compared to the orthogonal baseline, making it the most mass-efficient redundant architecture [cite: 2, 5].
*   **Tetrahedral/Pyramidal:** The four wheels are arranged such that their spin axes are not orthogonal but are distributed in 3D space. This allows the torque from any three wheels to span $\mathbb{R}^3$, meaning the system can maintain three-axis control even if one wheel fails [cite: 1, 13].
*   **Skewed Configurations:** Variations exist where wheels are canted at specific angles to bias momentum capacity towards specific axes (e.g., pitch-bias for nadir-pointing missions) [cite: 5].

**Conclusion on Configuration Selection:** For a strict weight budget, the **four-wheel configuration** is the only viable option that satisfies the requirement for redundancy. The optimization problem therefore reduces to determining the optimal geometric arrangement (tilt angle) and control allocation for this specific array.

## 3. The Optimal Geometry: The Four-Wheel Pyramid

The four-wheel pyramidal configuration consists of four reaction wheels distributed symmetrically around the spacecraft's vertical axis (usually $Z$). The spin axes of the wheels are inclined from the base plane ($X-Y$) by a tilt angle $\beta$ (also referred to as elevation or cant angle) [cite: 6, 14].

### 3.1 Maximizing the Momentum Envelope
The performance of the array is defined by its momentum envelope—the 3D volume of angular momentum vectors the system can generate without saturating any wheel.
*   **Spherical Envelope:** For general-purpose agility, where the spacecraft must slew in any direction with equal capability, a spherical momentum envelope is desired.
*   **The Optimal Angle ($35.26^\circ$):** Research consistently identifies a tilt angle of $\beta = \arcsin(1/\sqrt{3}) \approx 35.26^\circ$ (or $\arctan(1/\sqrt{2})$) as the geometric optimum for maximizing the volume of the inscribed sphere within the momentum envelope [cite: 3].
    *   At this angle, the array provides an isotropic distribution of torque capacity.
    *   This configuration is geometrically equivalent to the vectors originating from the center of a regular tetrahedron to its vertices [cite: 13].
*   **Alternative Angles ($45^\circ$ - $53^\circ$):** Some studies suggest higher angles, such as $45^\circ$ or $53.1^\circ$, to bias capability towards the Z-axis or to simplify mechanical integration [cite: 15, 16]. However, deviations from the isotropic angle reduce the maximum torque available in the worst-case direction, potentially limiting agility during complex maneuvers [cite: 14].

### 3.2 Power Consumption Minimization
Minimizing power is intrinsic to satisfying strict weight budgets, as it reduces the required mass of batteries and solar arrays [cite: 17].
*   **Optimum Tilt for Power:** Simulation studies indicate that the tilt angle significantly influences total power consumption. While $35.26^\circ$ is optimal for momentum volume, specific mission profiles (e.g., dominant nadir pointing) may find minimum power consumption at slightly different angles depending on the disturbance environment [cite: 6].
*   **Null Space Utilization:** The four-wheel system has one degree of redundancy, creating a "null space" in the control allocation matrix. This allows the control logic to adjust individual wheel speeds without generating net torque on the spacecraft. This capability is exploited to minimize wheel speeds (reducing friction and power) and avoid zero-crossings (reducing jitter) [cite: 7, 18].

## 4. Reliability and Fault Tolerance

The primary justification for the four-wheel pyramid is reliability. The system must maintain pointing accuracy and stability following the loss of any single actuator.

### 4.1 Fault Tolerance Mechanisms
In a healthy four-wheel pyramid, the control torque vector $\mathbf{T}_c$ is mapped to the four wheel torques $\mathbf{T}_w$ using a pseudoinverse of the configuration matrix $W$:
$$ \mathbf{T}_w = W^\dagger \mathbf{T}_c $$
When a failure occurs (e.g., a wheel seizes or electronics fail), the configuration matrix $W$ is reduced to a $3 \times 3$ matrix removing the column corresponding to the failed wheel.
*   **Singularity Avoidance:** The pyramidal geometry ensures that any subset of 3 wheels remains linearly independent (non-singular), provided the tilt angle $\beta \neq 0$ and $\beta \neq 90^\circ$ [cite: 6].
*   **Performance Degradation:** Research shows that while the spacecraft can reach the desired attitude after a failure, the settling time increases. For example, simulations indicate a settling time increase from nominal to roughly 40 seconds in failure modes, but stability is guaranteed [cite: 4].

### 4.2 Reliability Comparison
*   **Pyramid vs. Orthogonal:** The pyramid configuration offers a dramatic increase in system reliability. While an orthogonal system fails with a single component loss, the pyramid requires two simultaneous failures to lose three-axis control [cite: 1, 13].
*   **Pyramid vs. Tetrahedral:** While geometrically related, the specific orientation of the "pyramid" (aligned with body axes) vs. "tetrahedral" (vertices of a cube) can impact the ease of control allocation and singularity avoidance. The square pyramidal configuration is generally preferred for its symmetry and ease of integration into standard bus structures [cite: 5].

## 5. Pointing Accuracy and Control Strategies

Strict weight budgets often imply smaller, less rigid structures and potentially lower-quality sensors, making the control algorithm's role in maintaining accuracy crucial.

### 5.1 Achievable Accuracy
Despite the coupling introduced by the non-orthogonal arrangement, pyramidal configurations are capable of extremely high pointing accuracy.
*   **Precision:** Studies demonstrate that with appropriate controllers (PD, LQR, Sliding Mode), pyramidal configurations achieve Euler angle accuracies of $\pm 0.01^\circ$ or better [cite: 1].
*   **Jitter:** One challenge with redundant wheels is the potential for increased vibration (jitter) if all four wheels operate simultaneously. However, the null-space control can be used to minimize wheel speeds or avoid resonance frequencies, actually improving pointing stability compared to a fixed 3-wheel system [cite: 19, 20].

### 5.2 Control Algorithms
To maximize accuracy within a redundant setup, simple PID control is often insufficient.
*   **Sliding Mode Control (SMC):** SMC and Lyapunov-based controllers are highly effective for pyramidal configurations. They provide robustness against parameter uncertainties (e.g., changing inertia) and external disturbances (solar pressure, drag) [cite: 4, 21].
*   **Control Allocation:** The method of distributing torque among the 4 wheels is critical. The **Moore-Penrose pseudoinverse** is the standard approach for minimizing the $L_2$ norm of the wheel torques (energy minimization). Alternatively, **minimax ($L_\infty$)** algorithms can be used to keep all wheels away from their saturation limits, maximizing the available torque margin [cite: 3, 7].

## 6. Weight Budget Optimization

The query specifically emphasizes "strict weight budgets." The four-wheel pyramid addresses this through both direct mass savings (hardware) and indirect mass savings (power).

### 6.1 Hardware Mass
*   **Sizing:** By using four smaller wheels rather than three larger wheels, the system can often meet peak torque requirements with a lower total mass. The redundant wheel contributes to the total momentum capacity during nominal operations, allowing for individual wheels to be downsized [cite: 17, 22].
*   **Integration:** The pyramidal arrangement is compact. Unlike orthogonal wheels that might require complex mounting brackets to align with X, Y, and Z axes, a pyramidal block can be manufactured as a single compact assembly, reducing structural mass [cite: 23, 24].

### 6.2 Power-Mass Coupling
*   **Battery Sizing:** The power consumption of the ADCS drives the size of the solar panels and batteries. By optimizing the tilt angle (e.g., to $\approx 35^\circ$ or a mission-specific optimum) and using null-space distribution to minimize power, the spacecraft's power budget is reduced. This allows for a smaller power subsystem, directly reducing the satellite's total wet mass [cite: 6, 15].
*   **Momentum Dumping:** Efficient momentum management using the redundant array reduces the frequency of thruster firings (if used) or the size of magnetic torquers required for desaturation, further saving weight [cite: 25, 26].

## 7. Conclusion and Recommendation

To maximize satellite attitude control reliability and pointing accuracy within strict weight budgets, the research conclusively supports the following configuration:

1.  **Configuration:** **Four-Reaction Wheel Square Pyramid.** This provides the necessary N-1 fault tolerance with the minimum possible mass penalty (one extra wheel) compared to non-redundant systems [cite: 1, 2].
2.  **Geometric Optimization:** A **tilt angle ($\beta$) of $35.26^\circ$** is recommended. This angle creates a spherical momentum envelope, ensuring the satellite has equal agility and torque capacity in all directions, which is critical for recovering from arbitrary tumbling or failure states [cite: 3].
3.  **Control Strategy:** Implement a **Lyapunov-based or Sliding Mode Controller** combined with a **pseudoinverse control allocation** logic. This ensures high pointing accuracy ($<0.01^\circ$) and utilizes the system's null space to minimize power consumption and mechanical wear [cite: 4, 7].

This architecture represents the industry-standard "Pareto optimal" solution, balancing the competing demands of high reliability, precision, and low mass.

---

## 8. Detailed Analysis of Research Findings

### 8.1 Comparative Reliability of Configurations
Research comparing tetrahedral, pyramidal, and standard orthogonal configurations highlights the vulnerability of the 3-wheel orthogonal set. In a study by Ismail et al., it was noted that while the 3-wheel configuration at an 83° inclination achieved the highest theoretical pointing accuracy ($<0.001^\circ$), it possessed "catastrophic failure" modes [cite: 12]. In contrast, the pyramidal configuration maintained acceptable accuracy while surviving actuator loss.

The reliability of the pyramidal configuration is further enhanced by its ability to function with degraded performance. Bagheri et al. demonstrated that a spacecraft with a pyramidal array could recover from a wheel failure and reach the desired attitude, albeit with a settling time increase from ~34 seconds to ~40 seconds [cite: 4]. This "graceful degradation" is the hallmark of a robust system suitable for cost-constrained but critical missions.

### 8.2 The Mathematics of the Optimal Tilt Angle
The derivation of the $35.26^\circ$ angle is rooted in the projection of the hypercube of wheel capabilities into 3D space.
*   For a 4-wheel system, the torque envelope is a rhombic dodecahedron (or similar faceted volume depending on the exact arrangement).
*   To make this envelope as spherical as possible (maximizing the minimum torque available in any arbitrary direction), the ratio of the inscribed sphere to the maximum wheel capacity must be maximized.
*   Hablani and others derived that this maximum occurs when the wheels are arranged along the vectors of a regular tetrahedron, which corresponds to an elevation angle of $\arcsin(1/\sqrt{3}) \approx 35.26^\circ$ relative to the orthogonal plane [cite: 3].
*   This angle ensures that the loss of any single wheel leaves the remaining three with the best possible conditioning for 3-axis control, minimizing the "holes" in the torque envelope [cite: 5].

### 8.3 Power Optimization via Null Space
A critical advantage of the 4-wheel system over the 3-wheel system is the existence of a null space.
$$ \mathbf{h}_{total} = W \mathbf{h}_{wheels} $$
Since $W$ is $3 \times 4$, there is a non-zero vector $\mathbf{n}$ such that $W\mathbf{n} = 0$.
*   **Speed Redistribution:** Control laws can add components of $\mathbf{n}$ to the wheel speeds. This does not change the total momentum imparted to the spacecraft but changes the individual wheel speeds.
*   **Energy Minimization:** By driving wheel speeds toward zero (or a low bias speed) using the null space, the system minimizes viscous friction losses and resistive heating in the motors [cite: 18, 27].
*   **Singularity Avoidance:** The null space can also be used to steer wheels away from zero speed if stiction is a concern, or away from saturation speeds, thereby extending the operational life and reliability of the actuators [cite: 10].

### 8.4 Impact on Weight Budget
The decision to use a 4-wheel pyramid directly impacts the weight budget in nuanced ways:
1.  **Actuator Mass:** A 4-wheel system is 33% heavier than a 3-wheel system in terms of raw actuator mass.
2.  **System Mass Savings:** However, because the 4-wheel system can be optimized for power (as described above), the battery and solar array mass can be reduced. In many small satellite designs, the power subsystem is a significant fraction of the total mass. A 10-20% reduction in mechanical power and energy required for attitude maneuvers [cite: 27] can offset the mass of the fourth wheel.
3.  **Commercial Availability:** Integrated 4-wheel pyramidal units (RWAs) are commercially available for CubeSats and small sats, often optimized for weight (e.g., using shared housing and electronics), which further mitigates the mass penalty compared to integrating four separate wheels [cite: 23, 24].

### 8.5 Pointing Accuracy Considerations
Pointing accuracy is driven by sensor noise, controller gains, and actuator resolution/jitter.
*   **Controller Robustness:** Research indicates that nonlinear controllers (like Sliding Mode) are superior to linear LQR controllers for pyramidal configurations because they better handle the nonlinearities and coupling inherent in the skewed arrangement [cite: 1, 21].
*   **Jitter Management:** The redundant wheel allows for "speed skipping." If a wheel is near a speed that excites a structural resonance (causing jitter), the null space control can shift that speed to a different wheel or range without disturbing the spacecraft attitude. This capability is unavailable in 3-wheel systems and directly contributes to higher effective pointing accuracy for sensitive payloads [cite: 19].

## 9. Summary Table: Configuration Comparison

| Feature | Orthogonal (3-Wheel) | Pyramidal (4-Wheel) | Hexagonal/Dodecahedral (6-Wheel) |
| :--- | :--- | :--- | :--- |
| **Redundancy** | None (0-fault tolerant) | **Single (1-fault tolerant)** | Double (2-fault tolerant) |
| **Mass** | Low (Baseline) | **Medium (Optimal for budget)** | High (Prohibitive) |
| **Power Efficiency** | Low (No null space) | **High (Null space optimization)** | Medium (Complex management) |
| **Pointing Accuracy** | High | **High (with robust control)** | High |
| **Torque Envelope** | Cubic (Anisotropic) | **Spherical (Isotropic at 35.26°)** | Spherical |
| **Complexity** | Low | **Medium** | High |

## 10. Final Remarks

For an academic or engineering audience designing a satellite under strict weight constraints, the **four-wheel pyramidal configuration with a tilt angle of $\approx 35.26^\circ$** is the definitive recommendation. It represents the mathematical and practical intersection of reliability (N-1), performance (isotropic agility), and efficiency (power/mass optimization). Deviations from this angle should only be considered if the mission has highly asymmetric maneuvering requirements (e.g., exclusive nadir scanning), in which case the tilt angle should be biased to favor the dominant torque axis.

**Sources:**
1. [diva-portal.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUHvJNk1Fy9IYsnJAMbRr6gEEQm662OiiQMdebHjJKyYaZlMNx5cde9DfFP4rNafbTv0F0xTjRaIbM71J7isP6pP29IF4tUq4268MzIY76HKQmhKodpXm5WxQ6rhhD4JiAJlxZsyGOyHqbWMHeaU-Kg84JFEdd)
2. [aspina-group.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUwc3eplMBQri0TjYhKfdGJUUTSssr7hQv81Q2y7JpGQbmBhzMy4E-X8hD2O4kxJEEVJ19x1eJJ0MuaieiiYSL3TpYOanriID-I-yr1VfswbJI1qrPBh-hPA5wUWBiKL3Os7jfdSwyd5T3KYezthyKgmziEPs=)
3. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTKCXyNHCzuJpjJq5jNkQgM22hvPfnSM6MpjnV2DaZ9sX4oitktyi3e1X1_8xahw9VSwx8Gf4GHzWpL0A8P8toyvxVt3tuPpPEsU8DBAbnSKXQDnI0L4rJNcYaZsiEzgn9SXSWbt-MfgiGYNieMXrmSwFxW0j5hyipn7wbmnY=)
4. [ucsd.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpQ1MUplDzwIYeqHj6OKqeauWCxwyv6q1mG3AvFJ3wGcARYxhb3htjDu3yYy8Tc5VHNK97D90-p1svhTm0X7griGIRh6Jji_rbrGbUSAQr0NHOSV6cECFM3kmMvWNTc43PdBcM86Z2serKZA==)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6agDMJzJV4lzyxInmzXyHtCy4DbO2ZfSiObVI32GgaD2NpnmlFXCm0YvsumwJhz-NkW86axSFyxJlIIr23LBzPsuCuUscphS3DT_lZxeJN7D45DILuLv_qcQZQMzXUcS25LkJIhK9-I5isT-uCijyQjn3mzv_YeC1Y3veHGkFHwwJMxi3G6JS9bUxzp4JvlPAdPfKWKInVK7sQYx9etBcLQVr1ETDySowPFIqsMHTvm23GG9UeCISmdPa7-7iYZSrNj5aAmS-26rBkCdDm_XZuNZ_HPPtMQ==)
6. [ijass.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzcYxl0RR-xBwDN_ZQPhxgdGbhwQISY_O3FGaXvXw-OzLrhJVFpk88LYatN34SRooFNytE-qAvqN7IAD2Dr2lp5AvbCqdRtIAPxo42qACeQep0JxsR_Lu-AIxot9Bm7nSwmPmGK6-wyja-Z0kTaeCEfqz-rQ==)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEYeoY92uakI9kZ9TFK8WjgtSQfWrHUyVTeix9mdXeNCOLnMhOkK4EJVbEfKqMd9IThYjmySmj4FYkE8Ap7Ml-QCzLpuD16WwOH_RzduY9vmtPzfW61aoQmwv9Iu0abMr0JAikRdbJQ8zXRObq4AUrrmf_L_yQsa23QtP1FG6dbIWCn3aq30I-QKnzQ0-e7eYjTN8dXprfWspVn5GtLchuScTqrXZ19RRxAk5YUdQ2Y89O7IUfnT5enq8gPNevSdMDmbrMfTuZZy6Zmfu3Dseh)
8. [usu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExSz-NhhquQsFbNExFSddtmVCJNxBFYKiCpM0UCZv7enRC2txkCJSOkk5jFODn4Md5XpwPBCYjKgacAXmImHcR06ILDAwJhmW1hnj9jACkuYjFK3KoPdzHoVNoTCHgunCJEoPCP31f9CDh36djB5TNhGL0dBPwXXh35AoOGpQee-5se6Qk)
9. [preprints.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZP-RQXKg5zgp-96Pz0WtOtvpa3ILWEMBdnl1lOSyNM3WyCsBbYQLz14Igx2tRqscnEXPlqIkQUTGmczUbKHsjpsi2itQyCoULLOZL9aJlddxOAedQAySaVkZPyTEC9WG8IPURdA==)
10. [aau.dk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpc8MeUOlChzRlS2fpqlv-FlI64VaHeBkIMF3GqUCZVvckynY-IlX4ULeaRcYfVrslIxglGsE1vtQuXwDZHIQc-HLRTn0NnsYji9ujX2H0XTOOYcovnvFK1hhbw4UQETLb_NXqVhGczpkqaySY52hsSs8=)
11. [jossonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNPOSxmOHs8NZqzDWEEXrvOJ1SMPtLm6Gq5kuOqXPoWnVtA4Mt70jrWeaVNZJcau-zzoRBgZtVQRjwtNFSoSzz5l2w8li-DiNdl5M0sgGAWxeKkCCmt_JnpHt4aNXBfOJoGds_9wYFZeOCKj3VRzNBD764NkTYl2rVFCD071Bvu_AnaCC30bXKyjFzorVSg23t26dHF9vr1wX-zp8TRgsFT-vPOimUtcmNJmOb8TbQFdMIDkM=)
12. [arpnjournals.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaokiyAlreiKDndh5b5-zEhoprBzn9nSAmf5IHJvDFOZsZSUZMM6UYR2zMzHtoXCx8blLdeLIaVRhSL_52CQN1fr9Zf2hNfK00GFYN40qsSqqJgn_CHoTWjQupWAbkGvOQiYBAsADMC-AiiO2B9ODY8F68oh7oVfIcW5FdrUrJPQ==)
13. [stackexchange.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnh9VJ_f-Uxz2xH5Ldob_h6ECwrjWwBd98ZYEFxMr_DI-oVPmEFxuUME8rpVNrMjDBGPgmSpe9zthUapi_p69hRuq_ercKSINmwrBAWm1sPi7YkAJKwl6L8lO90U9BbtqNQNHBqN4AjBs_pSEDlfRTkCWYZvzGKZqNzW855v2mgGTG_toDr3M=)
14. [nps.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFP7yBuwsMgBsvkGq-jspWnRYKAFgQ2NoswfvhRFD2ydCtLo4c0uCuy-ky-4-pnfEYPcbabHpwmLxQ1fBf_SBUbNQ1Zsjl6xNZB2iZ-CC4gJ2dwI8mvyolXI0sY4zUXdAqETQd1R89HeSjG2JEn0Shu3dAcpUUQpg-EiPMU09NLfQt4ykatr86fUeLpnvdCSUl2lsmE)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEs88Wf9lVTdIdVq07M9MXwXQTTpilubyvA4Mn0hQ2QjcsqVWPmhESPn7QlNmYQonAj9Aa6xR4cYgJ0z7YwKe9ue-iXDiopbizqusLEWSY-eYaoUYnSTcT6-y4UFOYbJNDnlNYLLmSBLonmxtZOGIK5GEly7fTc9wn4KBO3Hpi5HTwSfyPpGIj2y_M6k_g3wWIO2sZer4YLmS9FkmP3bdirwZsSkIgdxe9wa-H3DSikcKVXnnZvWOYQKZCB3RKpm6eV4GxHXBQHB_P0cDbPChMGUXxlthmyDSsbK6HzmNgfXz36Tg==)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7Y2OBDFQOok99fVRuhCDgM0jGIlZpxDB_2SlOWElDO-YgR-MtSXDKEKjkdgOpmqtXBpQwiA01vzruFkhzAu0KlC1Ugd5n4eQhxs-XsLCSWrzNMIR5Lupy6k3r4231SLOeN4pF_eS1K2Fx8-On9OnciHZjlgrstbFRg1uf1Y-K5zgp5-RdNWctVGTu5cbX3BhVz1wgkvOQFETCOe43pDTPUzs=)
17. [usu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjwrWfdnCFxhndrDKJnl0dR7ozBiXLS8EnJV-kYLJ_5nETVpi-rtJ_y_GYDgPTRUDpcEtySGDLHqek9RvBh5jUiMxmIEhVGalhtWhbuCi-zHBXlW1qcb5OwjM-i7RDDSLhFPJTZznEBxCmi82SkzBgfo-u2prU4E8dxzZp8GYIaK7oHlho)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpLfPMf8nxQjkZrfro3984N-tiGX1Gi3Ya7HkWnHIp1jS9wWPqfFzlkx6aEpMPl_Edr1QhD6hiCpR1s9MFx40x-z-lvUbbB1y6BhL_BxXrTu5OjPeppaKnn4VbB4dicVrFqsS2Q_nmW4UC3zlpY27781282OowBjM6lnZehrqkeg5b-YjXtsCqpajUD9Nyu_3e3isLwlN2n3L-MegMevRp8cRgzYGjK8tuxTiixvkdsJADqMVc_hMjDeSWJYroZ14fHvSIlMMtGE-itkaV_xQ=)
19. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcjjakj0FUubHKdx4dUqmxlG8r4Q9whJYpPTEB1C7T8C_hQS-TzjbkECy4uUNNBUvJFEOaTgOR6SitlwadNpJhPhwS30z-EzhOlwvRAnqrUdDo7HgLiBNM8tcfOUjewzhWlk7p9R0fDse0hb-26wtvVtW8_PB8WQlW9myMlDE=)
20. [dtic.mil](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsAXWAYnCSvAZOA2dMIZCyYnkBY_kk0fgZYCWXHeb_d7W92zdXBUeB8arAnxsuh78OzhVTioCjGk_6NzVS2_R3IY9JDCfEltcFFifaofI1eOaXDfgtVBEwit2PL7gN8i4dqp0=)
21. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHt3ee10O5_q1n2cO5L-Ib7OqngwObGE0n0cLmE_S0SYlFpNhNfbP1JSIph6ttbMft8uvi0JJG6fQx_gR0yN3a8pG4M8NS3-rb7xtoyK61d1nT4Atwvzqa6KZ7fwjqKbDNPcnB_)
22. [usu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeiAxkHMX7Y2BZdEpsTqIXlwJMFLv0kDawp9OqpHLIISf85_7tvEI2I0FNz4Yfervow_MmyGC-7vq90EQQ1xqt8nlTg-rbVnEbPX5t_Loqmcrfi5UOoq-1SiiNcsWkLy8FNVODFrb9imJw5zALZ8xKqV8y81mKsXYx0k-wMDDKKyJ_gE-e)
23. [honeywell.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-YaR6h9SENHR8RwjVPP5lDqirW-6L7TZk6GjEWGVwaQVEXJcEhmfONhSLwifMxt4yG7y8S_IH3kQE492Ue71aFCPSyUWLE6C5Os3xIVtPzv6w3Z4Nouw9yZb5qPj9gPsxz508RKWY4a55HU1oR3Nc4Yv2feagTQPufBbJiEEA3ci2KKKLB-g=)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4aOO9ytfo0mP0zU4Cz2bhngbTbkC2Lw6YwEOYoQlXaLmn4Dm4zxbQ8R6QVDsW5P-1xvwXcNdonzS9NcVHr8MsKlOpqf1mN2irETugvs7EwBA9dzSKlR055qEbBaVlkSOgwcKsLgsOJB7Md3XGYqVAU0m_7m22eRKHjN1kPFeOfOgX55zB2pmfUbnAzYBKqwh3sn1kIr4aQ6CgQoHcqqwx-vdojFd1qi7WpBQ5Bg==)
25. [aiaa.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJxevmrJaOPkhx8C9Krtv0PxechNTgB1g9a4XcLYAKuy45f3vngM48zRJp8kgiyvvhPl-srQCgWVL4de-RpGOMqgGbGGpjTTd_x696VjH2JvtliGoIPUvQvPA2rXId4Bh6m7U=)
26. [hanspeterschaub.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-y2GVGIhy1TRKdhe-sKWF98KnZpObZJLgfIN5Dldy2AaK8rNXnA1mZAaZ0_k6Ei3Bg5VHOKUUzDLd5_6HDO9T41UyWN-BDqy68zLlCJDFz8FI_XlXOpLtuiL1_4wzGTUkOgG8bfUsUF1lL6rNQNPNfRA=)
27. [hanspeterschaub.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvgs2qDGO18tN_aM0rIPgaTcRAZnyFn_vON8oEqI-sI73vobKCahPgdtgEgh65UTnO5flO3ceVG3FYsMO-OoVn5rR0O71a9DAywSDaRauOcOl9Q0__Hl42qD__KmSlFs5daqnh29eDbaG9u8dFzw==)


## Annotations
Annotation(end_index=467, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUHvJNk1Fy9IYsnJAMbRr6gEEQm662OiiQMdebHjJKyYaZlMNx5cde9DfFP4rNafbTv0F0xTjRaIbM71J7isP6pP29IF4tUq4268MzIY76HKQmhKodpXm5WxQ6rhhD4JiAJlxZsyGOyHqbWMHeaU-Kg84JFEdd', start_index=455)
Annotation(end_index=467, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUwc3eplMBQri0TjYhKfdGJUUTSssr7hQv81Q2y7JpGQbmBhzMy4E-X8hD2O4kxJEEVJ19x1eJJ0MuaieiiYSL3TpYOanriID-I-yr1VfswbJI1qrPBh-hPA5wUWBiKL3Os7jfdSwyd5T3KYezthyKgmziEPs=', start_index=455)
Annotation(end_index=767, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTKCXyNHCzuJpjJq5jNkQgM22hvPfnSM6MpjnV2DaZ9sX4oitktyi3e1X1_8xahw9VSwx8Gf4GHzWpL0A8P8toyvxVt3tuPpPEsU8DBAbnSKXQDnI0L4rJNcYaZsiEzgn9SXSWbt-MfgiGYNieMXrmSwFxW0j5hyipn7wbmnY=', start_index=758)
Annotation(end_index=1130, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6agDMJzJV4lzyxInmzXyHtCy4DbO2ZfSiObVI32GgaD2NpnmlFXCm0YvsumwJhz-NkW86axSFyxJlIIr23LBzPsuCuUscphS3DT_lZxeJN7D45DILuLv_qcQZQMzXUcS25LkJIhK9-I5isT-uCijyQjn3mzv_YeC1Y3veHGkFHwwJMxi3G6JS9bUxzp4JvlPAdPfKWKInVK7sQYx9etBcLQVr1ETDySowPFIqsMHTvm23GG9UeCISmdPa7-7iYZSrNj5aAmS-26rBkCdDm_XZuNZ_HPPtMQ==', start_index=1118)
Annotation(end_index=1130, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpQ1MUplDzwIYeqHj6OKqeauWCxwyv6q1mG3AvFJ3wGcARYxhb3htjDu3yYy8Tc5VHNK97D90-p1svhTm0X7griGIRh6Jji_rbrGbUSAQr0NHOSV6cECFM3kmMvWNTc43PdBcM86Z2serKZA==', start_index=1118)
Annotation(end_index=1413, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpQ1MUplDzwIYeqHj6OKqeauWCxwyv6q1mG3AvFJ3wGcARYxhb3htjDu3yYy8Tc5VHNK97D90-p1svhTm0X7griGIRh6Jji_rbrGbUSAQr0NHOSV6cECFM3kmMvWNTc43PdBcM86Z2serKZA==', start_index=1401)
Annotation(end_index=1413, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUHvJNk1Fy9IYsnJAMbRr6gEEQm662OiiQMdebHjJKyYaZlMNx5cde9DfFP4rNafbTv0F0xTjRaIbM71J7isP6pP29IF4tUq4268MzIY76HKQmhKodpXm5WxQ6rhhD4JiAJlxZsyGOyHqbWMHeaU-Kg84JFEdd', start_index=1401)
Annotation(end_index=1686, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEYeoY92uakI9kZ9TFK8WjgtSQfWrHUyVTeix9mdXeNCOLnMhOkK4EJVbEfKqMd9IThYjmySmj4FYkE8Ap7Ml-QCzLpuD16WwOH_RzduY9vmtPzfW61aoQmwv9Iu0abMr0JAikRdbJQ8zXRObq4AUrrmf_L_yQsa23QtP1FG6dbIWCn3aq30I-QKnzQ0-e7eYjTN8dXprfWspVn5GtLchuScTqrXZ19RRxAk5YUdQ2Y89O7IUfnT5enq8gPNevSdMDmbrMfTuZZy6Zmfu3Dseh', start_index=1674)
Annotation(end_index=1686, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzcYxl0RR-xBwDN_ZQPhxgdGbhwQISY_O3FGaXvXw-OzLrhJVFpk88LYatN34SRooFNytE-qAvqN7IAD2Dr2lp5AvbCqdRtIAPxo42qACeQep0JxsR_Lu-AIxot9Bm7nSwmPmGK6-wyja-Z0kTaeCEfqz-rQ==', start_index=1674)
Annotation(end_index=2064, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExSz-NhhquQsFbNExFSddtmVCJNxBFYKiCpM0UCZv7enRC2txkCJSOkk5jFODn4Md5XpwPBCYjKgacAXmImHcR06ILDAwJhmW1hnj9jACkuYjFK3KoPdzHoVNoTCHgunCJEoPCP31f9CDh36djB5TNhGL0dBPwXXh35AoOGpQee-5se6Qk', start_index=2052)
Annotation(end_index=2064, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUHvJNk1Fy9IYsnJAMbRr6gEEQm662OiiQMdebHjJKyYaZlMNx5cde9DfFP4rNafbTv0F0xTjRaIbM71J7isP6pP29IF4tUq4268MzIY76HKQmhKodpXm5WxQ6rhhD4JiAJlxZsyGOyHqbWMHeaU-Kg84JFEdd', start_index=2052)
Annotation(end_index=2268, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZP-RQXKg5zgp-96Pz0WtOtvpa3ILWEMBdnl1lOSyNM3WyCsBbYQLz14Igx2tRqscnEXPlqIkQUTGmczUbKHsjpsi2itQyCoULLOZL9aJlddxOAedQAySaVkZPyTEC9WG8IPURdA==', start_index=2255)
Annotation(end_index=2268, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpc8MeUOlChzRlS2fpqlv-FlI64VaHeBkIMF3GqUCZVvckynY-IlX4ULeaRcYfVrslIxglGsE1vtQuXwDZHIQc-HLRTn0NnsYji9ujX2H0XTOOYcovnvFK1hhbw4UQETLb_NXqVhGczpkqaySY52hsSs8=', start_index=2255)
Annotation(end_index=2621, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExSz-NhhquQsFbNExFSddtmVCJNxBFYKiCpM0UCZv7enRC2txkCJSOkk5jFODn4Md5XpwPBCYjKgacAXmImHcR06ILDAwJhmW1hnj9jACkuYjFK3KoPdzHoVNoTCHgunCJEoPCP31f9CDh36djB5TNhGL0dBPwXXh35AoOGpQee-5se6Qk', start_index=2608)
Annotation(end_index=2621, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNPOSxmOHs8NZqzDWEEXrvOJ1SMPtLm6Gq5kuOqXPoWnVtA4Mt70jrWeaVNZJcau-zzoRBgZtVQRjwtNFSoSzz5l2w8li-DiNdl5M0sgGAWxeKkCCmt_JnpHt4aNXBfOJoGds_9wYFZeOCKj3VRzNBD764NkTYl2rVFCD071Bvu_AnaCC30bXKyjFzorVSg23t26dHF9vr1wX-zp8TRgsFT-vPOimUtcmNJmOb8TbQFdMIDkM=', start_index=2608)
Annotation(end_index=3685, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUHvJNk1Fy9IYsnJAMbRr6gEEQm662OiiQMdebHjJKyYaZlMNx5cde9DfFP4rNafbTv0F0xTjRaIbM71J7isP6pP29IF4tUq4268MzIY76HKQmhKodpXm5WxQ6rhhD4JiAJlxZsyGOyHqbWMHeaU-Kg84JFEdd', start_index=3676)
Annotation(end_index=3940, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaokiyAlreiKDndh5b5-zEhoprBzn9nSAmf5IHJvDFOZsZSUZMM6UYR2zMzHtoXCx8blLdeLIaVRhSL_52CQN1fr9Zf2hNfK00GFYN40qsSqqJgn_CHoTWjQupWAbkGvOQiYBAsADMC-AiiO2B9ODY8F68oh7oVfIcW5FdrUrJPQ==', start_index=3930)
Annotation(end_index=4132, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaokiyAlreiKDndh5b5-zEhoprBzn9nSAmf5IHJvDFOZsZSUZMM6UYR2zMzHtoXCx8blLdeLIaVRhSL_52CQN1fr9Zf2hNfK00GFYN40qsSqqJgn_CHoTWjQupWAbkGvOQiYBAsADMC-AiiO2B9ODY8F68oh7oVfIcW5FdrUrJPQ==', start_index=4122)
Annotation(end_index=4395, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTKCXyNHCzuJpjJq5jNkQgM22hvPfnSM6MpjnV2DaZ9sX4oitktyi3e1X1_8xahw9VSwx8Gf4GHzWpL0A8P8toyvxVt3tuPpPEsU8DBAbnSKXQDnI0L4rJNcYaZsiEzgn9SXSWbt-MfgiGYNieMXrmSwFxW0j5hyipn7wbmnY=', start_index=4386)
Annotation(end_index=4660, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExSz-NhhquQsFbNExFSddtmVCJNxBFYKiCpM0UCZv7enRC2txkCJSOkk5jFODn4Md5XpwPBCYjKgacAXmImHcR06ILDAwJhmW1hnj9jACkuYjFK3KoPdzHoVNoTCHgunCJEoPCP31f9CDh36djB5TNhGL0dBPwXXh35AoOGpQee-5se6Qk', start_index=4651)
Annotation(end_index=4986, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6agDMJzJV4lzyxInmzXyHtCy4DbO2ZfSiObVI32GgaD2NpnmlFXCm0YvsumwJhz-NkW86axSFyxJlIIr23LBzPsuCuUscphS3DT_lZxeJN7D45DILuLv_qcQZQMzXUcS25LkJIhK9-I5isT-uCijyQjn3mzv_YeC1Y3veHGkFHwwJMxi3G6JS9bUxzp4JvlPAdPfKWKInVK7sQYx9etBcLQVr1ETDySowPFIqsMHTvm23GG9UeCISmdPa7-7iYZSrNj5aAmS-26rBkCdDm_XZuNZ_HPPtMQ==', start_index=4974)
Annotation(end_index=4986, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUwc3eplMBQri0TjYhKfdGJUUTSssr7hQv81Q2y7JpGQbmBhzMy4E-X8hD2O4kxJEEVJ19x1eJJ0MuaieiiYSL3TpYOanriID-I-yr1VfswbJI1qrPBh-hPA5wUWBiKL3Os7jfdSwyd5T3KYezthyKgmziEPs=', start_index=4974)
Annotation(end_index=5283, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUHvJNk1Fy9IYsnJAMbRr6gEEQm662OiiQMdebHjJKyYaZlMNx5cde9DfFP4rNafbTv0F0xTjRaIbM71J7isP6pP29IF4tUq4268MzIY76HKQmhKodpXm5WxQ6rhhD4JiAJlxZsyGOyHqbWMHeaU-Kg84JFEdd', start_index=5270)
Annotation(end_index=5283, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnh9VJ_f-Uxz2xH5Ldob_h6ECwrjWwBd98ZYEFxMr_DI-oVPmEFxuUME8rpVNrMjDBGPgmSpe9zthUapi_p69hRuq_ercKSINmwrBAWm1sPi7YkAJKwl6L8lO90U9BbtqNQNHBqN4AjBs_pSEDlfRTkCWYZvzGKZqNzW855v2mgGTG_toDr3M=', start_index=5270)
Annotation(end_index=5480, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6agDMJzJV4lzyxInmzXyHtCy4DbO2ZfSiObVI32GgaD2NpnmlFXCm0YvsumwJhz-NkW86axSFyxJlIIr23LBzPsuCuUscphS3DT_lZxeJN7D45DILuLv_qcQZQMzXUcS25LkJIhK9-I5isT-uCijyQjn3mzv_YeC1Y3veHGkFHwwJMxi3G6JS9bUxzp4JvlPAdPfKWKInVK7sQYx9etBcLQVr1ETDySowPFIqsMHTvm23GG9UeCISmdPa7-7iYZSrNj5aAmS-26rBkCdDm_XZuNZ_HPPtMQ==', start_index=5471)
Annotation(end_index=6169, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFP7yBuwsMgBsvkGq-jspWnRYKAFgQ2NoswfvhRFD2ydCtLo4c0uCuy-ky-4-pnfEYPcbabHpwmLxQ1fBf_SBUbNQ1Zsjl6xNZB2iZ-CC4gJ2dwI8mvyolXI0sY4zUXdAqETQd1R89HeSjG2JEn0Shu3dAcpUUQpg-EiPMU09NLfQt4ykatr86fUeLpnvdCSUl2lsmE', start_index=6156)
Annotation(end_index=6169, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzcYxl0RR-xBwDN_ZQPhxgdGbhwQISY_O3FGaXvXw-OzLrhJVFpk88LYatN34SRooFNytE-qAvqN7IAD2Dr2lp5AvbCqdRtIAPxo42qACeQep0JxsR_Lu-AIxot9Bm7nSwmPmGK6-wyja-Z0kTaeCEfqz-rQ==', start_index=6156)
Annotation(end_index=6828, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTKCXyNHCzuJpjJq5jNkQgM22hvPfnSM6MpjnV2DaZ9sX4oitktyi3e1X1_8xahw9VSwx8Gf4GHzWpL0A8P8toyvxVt3tuPpPEsU8DBAbnSKXQDnI0L4rJNcYaZsiEzgn9SXSWbt-MfgiGYNieMXrmSwFxW0j5hyipn7wbmnY=', start_index=6819)
Annotation(end_index=7067, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnh9VJ_f-Uxz2xH5Ldob_h6ECwrjWwBd98ZYEFxMr_DI-oVPmEFxuUME8rpVNrMjDBGPgmSpe9zthUapi_p69hRuq_ercKSINmwrBAWm1sPi7YkAJKwl6L8lO90U9BbtqNQNHBqN4AjBs_pSEDlfRTkCWYZvzGKZqNzW855v2mgGTG_toDr3M=', start_index=7057)
Annotation(end_index=7285, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEs88Wf9lVTdIdVq07M9MXwXQTTpilubyvA4Mn0hQ2QjcsqVWPmhESPn7QlNmYQonAj9Aa6xR4cYgJ0z7YwKe9ue-iXDiopbizqusLEWSY-eYaoUYnSTcT6-y4UFOYbJNDnlNYLLmSBLonmxtZOGIK5GEly7fTc9wn4KBO3Hpi5HTwSfyPpGIj2y_M6k_g3wWIO2sZer4YLmS9FkmP3bdirwZsSkIgdxe9wa-H3DSikcKVXnnZvWOYQKZCB3RKpm6eV4GxHXBQHB_P0cDbPChMGUXxlthmyDSsbK6HzmNgfXz36Tg==', start_index=7271)
Annotation(end_index=7285, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7Y2OBDFQOok99fVRuhCDgM0jGIlZpxDB_2SlOWElDO-YgR-MtSXDKEKjkdgOpmqtXBpQwiA01vzruFkhzAu0KlC1Ugd5n4eQhxs-XsLCSWrzNMIR5Lupy6k3r4231SLOeN4pF_eS1K2Fx8-On9OnciHZjlgrstbFRg1uf1Y-K5zgp5-RdNWctVGTu5cbX3BhVz1wgkvOQFETCOe43pDTPUzs=', start_index=7271)
Annotation(end_index=7461, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFP7yBuwsMgBsvkGq-jspWnRYKAFgQ2NoswfvhRFD2ydCtLo4c0uCuy-ky-4-pnfEYPcbabHpwmLxQ1fBf_SBUbNQ1Zsjl6xNZB2iZ-CC4gJ2dwI8mvyolXI0sY4zUXdAqETQd1R89HeSjG2JEn0Shu3dAcpUUQpg-EiPMU09NLfQt4ykatr86fUeLpnvdCSUl2lsmE', start_index=7451)
Annotation(end_index=7642, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjwrWfdnCFxhndrDKJnl0dR7ozBiXLS8EnJV-kYLJ_5nETVpi-rtJ_y_GYDgPTRUDpcEtySGDLHqek9RvBh5jUiMxmIEhVGalhtWhbuCi-zHBXlW1qcb5OwjM-i7RDDSLhFPJTZznEBxCmi82SkzBgfo-u2prU4E8dxzZp8GYIaK7oHlho', start_index=7632)
Annotation(end_index=7998, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzcYxl0RR-xBwDN_ZQPhxgdGbhwQISY_O3FGaXvXw-OzLrhJVFpk88LYatN34SRooFNytE-qAvqN7IAD2Dr2lp5AvbCqdRtIAPxo42qACeQep0JxsR_Lu-AIxot9Bm7nSwmPmGK6-wyja-Z0kTaeCEfqz-rQ==', start_index=7989)
Annotation(end_index=8395, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEYeoY92uakI9kZ9TFK8WjgtSQfWrHUyVTeix9mdXeNCOLnMhOkK4EJVbEfKqMd9IThYjmySmj4FYkE8Ap7Ml-QCzLpuD16WwOH_RzduY9vmtPzfW61aoQmwv9Iu0abMr0JAikRdbJQ8zXRObq4AUrrmf_L_yQsa23QtP1FG6dbIWCn3aq30I-QKnzQ0-e7eYjTN8dXprfWspVn5GtLchuScTqrXZ19RRxAk5YUdQ2Y89O7IUfnT5enq8gPNevSdMDmbrMfTuZZy6Zmfu3Dseh', start_index=8382)
Annotation(end_index=8395, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpLfPMf8nxQjkZrfro3984N-tiGX1Gi3Ya7HkWnHIp1jS9wWPqfFzlkx6aEpMPl_Edr1QhD6hiCpR1s9MFx40x-z-lvUbbB1y6BhL_BxXrTu5OjPeppaKnn4VbB4dicVrFqsS2Q_nmW4UC3zlpY27781282OowBjM6lnZehrqkeg5b-YjXtsCqpajUD9Nyu_3e3isLwlN2n3L-MegMevRp8cRgzYGjK8tuxTiixvkdsJADqMVc_hMjDeSWJYroZ14fHvSIlMMtGE-itkaV_xQ=', start_index=8382)
Annotation(end_index=9261, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzcYxl0RR-xBwDN_ZQPhxgdGbhwQISY_O3FGaXvXw-OzLrhJVFpk88LYatN34SRooFNytE-qAvqN7IAD2Dr2lp5AvbCqdRtIAPxo42qACeQep0JxsR_Lu-AIxot9Bm7nSwmPmGK6-wyja-Z0kTaeCEfqz-rQ==', start_index=9252)
Annotation(end_index=9563, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpQ1MUplDzwIYeqHj6OKqeauWCxwyv6q1mG3AvFJ3wGcARYxhb3htjDu3yYy8Tc5VHNK97D90-p1svhTm0X7griGIRh6Jji_rbrGbUSAQr0NHOSV6cECFM3kmMvWNTc43PdBcM86Z2serKZA==', start_index=9554)
Annotation(end_index=9855, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUHvJNk1Fy9IYsnJAMbRr6gEEQm662OiiQMdebHjJKyYaZlMNx5cde9DfFP4rNafbTv0F0xTjRaIbM71J7isP6pP29IF4tUq4268MzIY76HKQmhKodpXm5WxQ6rhhD4JiAJlxZsyGOyHqbWMHeaU-Kg84JFEdd', start_index=9842)
Annotation(end_index=9855, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnh9VJ_f-Uxz2xH5Ldob_h6ECwrjWwBd98ZYEFxMr_DI-oVPmEFxuUME8rpVNrMjDBGPgmSpe9zthUapi_p69hRuq_ercKSINmwrBAWm1sPi7YkAJKwl6L8lO90U9BbtqNQNHBqN4AjBs_pSEDlfRTkCWYZvzGKZqNzW855v2mgGTG_toDr3M=', start_index=9842)
Annotation(end_index=10231, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6agDMJzJV4lzyxInmzXyHtCy4DbO2ZfSiObVI32GgaD2NpnmlFXCm0YvsumwJhz-NkW86axSFyxJlIIr23LBzPsuCuUscphS3DT_lZxeJN7D45DILuLv_qcQZQMzXUcS25LkJIhK9-I5isT-uCijyQjn3mzv_YeC1Y3veHGkFHwwJMxi3G6JS9bUxzp4JvlPAdPfKWKInVK7sQYx9etBcLQVr1ETDySowPFIqsMHTvm23GG9UeCISmdPa7-7iYZSrNj5aAmS-26rBkCdDm_XZuNZ_HPPtMQ==', start_index=10222)
Annotation(end_index=10818, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUHvJNk1Fy9IYsnJAMbRr6gEEQm662OiiQMdebHjJKyYaZlMNx5cde9DfFP4rNafbTv0F0xTjRaIbM71J7isP6pP29IF4tUq4268MzIY76HKQmhKodpXm5WxQ6rhhD4JiAJlxZsyGOyHqbWMHeaU-Kg84JFEdd', start_index=10809)
Annotation(end_index=11153, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsAXWAYnCSvAZOA2dMIZCyYnkBY_kk0fgZYCWXHeb_d7W92zdXBUeB8arAnxsuh78OzhVTioCjGk_6NzVS2_R3IY9JDCfEltcFFifaofI1eOaXDfgtVBEwit2PL7gN8i4dqp0=', start_index=11139)
Annotation(end_index=11153, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcjjakj0FUubHKdx4dUqmxlG8r4Q9whJYpPTEB1C7T8C_hQS-TzjbkECy4uUNNBUvJFEOaTgOR6SitlwadNpJhPhwS30z-EzhOlwvRAnqrUdDo7HgLiBNM8tcfOUjewzhWlk7p9R0fDse0hb-26wtvVtW8_PB8WQlW9myMlDE=', start_index=11139)
Annotation(end_index=11537, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpQ1MUplDzwIYeqHj6OKqeauWCxwyv6q1mG3AvFJ3wGcARYxhb3htjDu3yYy8Tc5VHNK97D90-p1svhTm0X7griGIRh6Jji_rbrGbUSAQr0NHOSV6cECFM3kmMvWNTc43PdBcM86Z2serKZA==', start_index=11524)
Annotation(end_index=11537, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHt3ee10O5_q1n2cO5L-Ib7OqngwObGE0n0cLmE_S0SYlFpNhNfbP1JSIph6ttbMft8uvi0JJG6fQx_gR0yN3a8pG4M8NS3-rb7xtoyK61d1nT4Atwvzqa6KZ7fwjqKbDNPcnB_', start_index=11524)
Annotation(end_index=11936, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEYeoY92uakI9kZ9TFK8WjgtSQfWrHUyVTeix9mdXeNCOLnMhOkK4EJVbEfKqMd9IThYjmySmj4FYkE8Ap7Ml-QCzLpuD16WwOH_RzduY9vmtPzfW61aoQmwv9Iu0abMr0JAikRdbJQ8zXRObq4AUrrmf_L_yQsa23QtP1FG6dbIWCn3aq30I-QKnzQ0-e7eYjTN8dXprfWspVn5GtLchuScTqrXZ19RRxAk5YUdQ2Y89O7IUfnT5enq8gPNevSdMDmbrMfTuZZy6Zmfu3Dseh', start_index=11924)
Annotation(end_index=11936, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTKCXyNHCzuJpjJq5jNkQgM22hvPfnSM6MpjnV2DaZ9sX4oitktyi3e1X1_8xahw9VSwx8Gf4GHzWpL0A8P8toyvxVt3tuPpPEsU8DBAbnSKXQDnI0L4rJNcYaZsiEzgn9SXSWbt-MfgiGYNieMXrmSwFxW0j5hyipn7wbmnY=', start_index=11924)
Annotation(end_index=12477, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjwrWfdnCFxhndrDKJnl0dR7ozBiXLS8EnJV-kYLJ_5nETVpi-rtJ_y_GYDgPTRUDpcEtySGDLHqek9RvBh5jUiMxmIEhVGalhtWhbuCi-zHBXlW1qcb5OwjM-i7RDDSLhFPJTZznEBxCmi82SkzBgfo-u2prU4E8dxzZp8GYIaK7oHlho', start_index=12463)
Annotation(end_index=12477, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeiAxkHMX7Y2BZdEpsTqIXlwJMFLv0kDawp9OqpHLIISf85_7tvEI2I0FNz4Yfervow_MmyGC-7vq90EQQ1xqt8nlTg-rbVnEbPX5t_Loqmcrfi5UOoq-1SiiNcsWkLy8FNVODFrb9imJw5zALZ8xKqV8y81mKsXYx0k-wMDDKKyJ_gE-e', start_index=12463)
Annotation(end_index=12747, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-YaR6h9SENHR8RwjVPP5lDqirW-6L7TZk6GjEWGVwaQVEXJcEhmfONhSLwifMxt4yG7y8S_IH3kQE492Ue71aFCPSyUWLE6C5Os3xIVtPzv6w3Z4Nouw9yZb5qPj9gPsxz508RKWY4a55HU1oR3Nc4Yv2feagTQPufBbJiEEA3ci2KKKLB-g=', start_index=12733)
Annotation(end_index=12747, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4aOO9ytfo0mP0zU4Cz2bhngbTbkC2Lw6YwEOYoQlXaLmn4Dm4zxbQ8R6QVDsW5P-1xvwXcNdonzS9NcVHr8MsKlOpqf1mN2irETugvs7EwBA9dzSKlR055qEbBaVlkSOgwcKsLgsOJB7Md3XGYqVAU0m_7m22eRKHjN1kPFeOfOgX55zB2pmfUbnAzYBKqwh3sn1kIr4aQ6CgQoHcqqwx-vdojFd1qi7WpBQ5Bg==', start_index=12733)
Annotation(end_index=13176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEs88Wf9lVTdIdVq07M9MXwXQTTpilubyvA4Mn0hQ2QjcsqVWPmhESPn7QlNmYQonAj9Aa6xR4cYgJ0z7YwKe9ue-iXDiopbizqusLEWSY-eYaoUYnSTcT6-y4UFOYbJNDnlNYLLmSBLonmxtZOGIK5GEly7fTc9wn4KBO3Hpi5HTwSfyPpGIj2y_M6k_g3wWIO2sZer4YLmS9FkmP3bdirwZsSkIgdxe9wa-H3DSikcKVXnnZvWOYQKZCB3RKpm6eV4GxHXBQHB_P0cDbPChMGUXxlthmyDSsbK6HzmNgfXz36Tg==', start_index=13163)
Annotation(end_index=13176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzcYxl0RR-xBwDN_ZQPhxgdGbhwQISY_O3FGaXvXw-OzLrhJVFpk88LYatN34SRooFNytE-qAvqN7IAD2Dr2lp5AvbCqdRtIAPxo42qACeQep0JxsR_Lu-AIxot9Bm7nSwmPmGK6-wyja-Z0kTaeCEfqz-rQ==', start_index=13163)
Annotation(end_index=13408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJxevmrJaOPkhx8C9Krtv0PxechNTgB1g9a4XcLYAKuy45f3vngM48zRJp8kgiyvvhPl-srQCgWVL4de-RpGOMqgGbGGpjTTd_x696VjH2JvtliGoIPUvQvPA2rXId4Bh6m7U=', start_index=13394)
Annotation(end_index=13408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-y2GVGIhy1TRKdhe-sKWF98KnZpObZJLgfIN5Dldy2AaK8rNXnA1mZAaZ0_k6Ei3Bg5VHOKUUzDLd5_6HDO9T41UyWN-BDqy68zLlCJDFz8FI_XlXOpLtuiL1_4wzGTUkOgG8bfUsUF1lL6rNQNPNfRA=', start_index=13394)
Annotation(end_index=13830, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUHvJNk1Fy9IYsnJAMbRr6gEEQm662OiiQMdebHjJKyYaZlMNx5cde9DfFP4rNafbTv0F0xTjRaIbM71J7isP6pP29IF4tUq4268MzIY76HKQmhKodpXm5WxQ6rhhD4JiAJlxZsyGOyHqbWMHeaU-Kg84JFEdd', start_index=13818)
Annotation(end_index=13830, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUwc3eplMBQri0TjYhKfdGJUUTSssr7hQv81Q2y7JpGQbmBhzMy4E-X8hD2O4kxJEEVJ19x1eJJ0MuaieiiYSL3TpYOanriID-I-yr1VfswbJI1qrPBh-hPA5wUWBiKL3Os7jfdSwyd5T3KYezthyKgmziEPs=', start_index=13818)
Annotation(end_index=14138, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTKCXyNHCzuJpjJq5jNkQgM22hvPfnSM6MpjnV2DaZ9sX4oitktyi3e1X1_8xahw9VSwx8Gf4GHzWpL0A8P8toyvxVt3tuPpPEsU8DBAbnSKXQDnI0L4rJNcYaZsiEzgn9SXSWbt-MfgiGYNieMXrmSwFxW0j5hyipn7wbmnY=', start_index=14129)
Annotation(end_index=14435, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpQ1MUplDzwIYeqHj6OKqeauWCxwyv6q1mG3AvFJ3wGcARYxhb3htjDu3yYy8Tc5VHNK97D90-p1svhTm0X7griGIRh6Jji_rbrGbUSAQr0NHOSV6cECFM3kmMvWNTc43PdBcM86Z2serKZA==', start_index=14423)
Annotation(end_index=14435, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEYeoY92uakI9kZ9TFK8WjgtSQfWrHUyVTeix9mdXeNCOLnMhOkK4EJVbEfKqMd9IThYjmySmj4FYkE8Ap7Ml-QCzLpuD16WwOH_RzduY9vmtPzfW61aoQmwv9Iu0abMr0JAikRdbJQ8zXRObq4AUrrmf_L_yQsa23QtP1FG6dbIWCn3aq30I-QKnzQ0-e7eYjTN8dXprfWspVn5GtLchuScTqrXZ19RRxAk5YUdQ2Y89O7IUfnT5enq8gPNevSdMDmbrMfTuZZy6Zmfu3Dseh', start_index=14423)
Annotation(end_index=15061, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaokiyAlreiKDndh5b5-zEhoprBzn9nSAmf5IHJvDFOZsZSUZMM6UYR2zMzHtoXCx8blLdeLIaVRhSL_52CQN1fr9Zf2hNfK00GFYN40qsSqqJgn_CHoTWjQupWAbkGvOQiYBAsADMC-AiiO2B9ODY8F68oh7oVfIcW5FdrUrJPQ==', start_index=15051)
Annotation(end_index=15502, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpQ1MUplDzwIYeqHj6OKqeauWCxwyv6q1mG3AvFJ3wGcARYxhb3htjDu3yYy8Tc5VHNK97D90-p1svhTm0X7griGIRh6Jji_rbrGbUSAQr0NHOSV6cECFM3kmMvWNTc43PdBcM86Z2serKZA==', start_index=15493)
Annotation(end_index=16391, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTKCXyNHCzuJpjJq5jNkQgM22hvPfnSM6MpjnV2DaZ9sX4oitktyi3e1X1_8xahw9VSwx8Gf4GHzWpL0A8P8toyvxVt3tuPpPEsU8DBAbnSKXQDnI0L4rJNcYaZsiEzgn9SXSWbt-MfgiGYNieMXrmSwFxW0j5hyipn7wbmnY=', start_index=16382)
Annotation(end_index=16588, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6agDMJzJV4lzyxInmzXyHtCy4DbO2ZfSiObVI32GgaD2NpnmlFXCm0YvsumwJhz-NkW86axSFyxJlIIr23LBzPsuCuUscphS3DT_lZxeJN7D45DILuLv_qcQZQMzXUcS25LkJIhK9-I5isT-uCijyQjn3mzv_YeC1Y3veHGkFHwwJMxi3G6JS9bUxzp4JvlPAdPfKWKInVK7sQYx9etBcLQVr1ETDySowPFIqsMHTvm23GG9UeCISmdPa7-7iYZSrNj5aAmS-26rBkCdDm_XZuNZ_HPPtMQ==', start_index=16579)
Annotation(end_index=17290, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvgs2qDGO18tN_aM0rIPgaTcRAZnyFn_vON8oEqI-sI73vobKCahPgdtgEgh65UTnO5flO3ceVG3FYsMO-OoVn5rR0O71a9DAywSDaRauOcOl9Q0__Hl42qD__KmSlFs5daqnh29eDbaG9u8dFzw==', start_index=17276)
Annotation(end_index=17290, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpLfPMf8nxQjkZrfro3984N-tiGX1Gi3Ya7HkWnHIp1jS9wWPqfFzlkx6aEpMPl_Edr1QhD6hiCpR1s9MFx40x-z-lvUbbB1y6BhL_BxXrTu5OjPeppaKnn4VbB4dicVrFqsS2Q_nmW4UC3zlpY27781282OowBjM6lnZehrqkeg5b-YjXtsCqpajUD9Nyu_3e3isLwlN2n3L-MegMevRp8cRgzYGjK8tuxTiixvkdsJADqMVc_hMjDeSWJYroZ14fHvSIlMMtGE-itkaV_xQ=', start_index=17276)
Annotation(end_index=17532, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpc8MeUOlChzRlS2fpqlv-FlI64VaHeBkIMF3GqUCZVvckynY-IlX4ULeaRcYfVrslIxglGsE1vtQuXwDZHIQc-HLRTn0NnsYji9ujX2H0XTOOYcovnvFK1hhbw4UQETLb_NXqVhGczpkqaySY52hsSs8=', start_index=17522)
Annotation(end_index=18118, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvgs2qDGO18tN_aM0rIPgaTcRAZnyFn_vON8oEqI-sI73vobKCahPgdtgEgh65UTnO5flO3ceVG3FYsMO-OoVn5rR0O71a9DAywSDaRauOcOl9Q0__Hl42qD__KmSlFs5daqnh29eDbaG9u8dFzw==', start_index=18108)
Annotation(end_index=18464, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-YaR6h9SENHR8RwjVPP5lDqirW-6L7TZk6GjEWGVwaQVEXJcEhmfONhSLwifMxt4yG7y8S_IH3kQE492Ue71aFCPSyUWLE6C5Os3xIVtPzv6w3Z4Nouw9yZb5qPj9gPsxz508RKWY4a55HU1oR3Nc4Yv2feagTQPufBbJiEEA3ci2KKKLB-g=', start_index=18450)
Annotation(end_index=18464, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4aOO9ytfo0mP0zU4Cz2bhngbTbkC2Lw6YwEOYoQlXaLmn4Dm4zxbQ8R6QVDsW5P-1xvwXcNdonzS9NcVHr8MsKlOpqf1mN2irETugvs7EwBA9dzSKlR055qEbBaVlkSOgwcKsLgsOJB7Md3XGYqVAU0m_7m22eRKHjN1kPFeOfOgX55zB2pmfUbnAzYBKqwh3sn1kIr4aQ6CgQoHcqqwx-vdojFd1qi7WpBQ5Bg==', start_index=18450)
Annotation(end_index=18875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUHvJNk1Fy9IYsnJAMbRr6gEEQm662OiiQMdebHjJKyYaZlMNx5cde9DfFP4rNafbTv0F0xTjRaIbM71J7isP6pP29IF4tUq4268MzIY76HKQmhKodpXm5WxQ6rhhD4JiAJlxZsyGOyHqbWMHeaU-Kg84JFEdd', start_index=18862)
Annotation(end_index=18875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHt3ee10O5_q1n2cO5L-Ib7OqngwObGE0n0cLmE_S0SYlFpNhNfbP1JSIph6ttbMft8uvi0JJG6fQx_gR0yN3a8pG4M8NS3-rb7xtoyK61d1nT4Atwvzqa6KZ7fwjqKbDNPcnB_', start_index=18862)
Annotation(end_index=19298, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcjjakj0FUubHKdx4dUqmxlG8r4Q9whJYpPTEB1C7T8C_hQS-TzjbkECy4uUNNBUvJFEOaTgOR6SitlwadNpJhPhwS30z-EzhOlwvRAnqrUdDo7HgLiBNM8tcfOUjewzhWlk7p9R0fDse0hb-26wtvVtW8_PB8WQlW9myMlDE=', start_index=19288)

## Sources
