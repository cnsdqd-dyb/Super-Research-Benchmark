# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** e83b0ba1 | **Time:** 268.39s | **Cost:** $1.03541
--------------------------------------------------------------------------------

# Impedance Matching and Small-Signal Stability in Microgrid Control Under Distributed Power Fluctuations

### Key Points
*   **Critical Role of Impedance Characteristics:** Research confirms that the impedance characteristics of a microgrid—specifically the ratio of reactance to resistance (X/R)—fundamentally dictate small-signal stability. Low X/R ratios (resistive networks) cause severe coupling between active and reactive power, leading to significant power fluctuations (e.g., ±500 W on a 1700 W base) and potential instability [cite: 1].
*   **Virtual Impedance as a Stability Enabler:** "Impedance matching" in modern microgrid control largely refers to the implementation of **Virtual Impedance (VI)**. This control technique artificially modifies the inverter's output impedance to mimic a high X/R ratio, decoupling power control loops, damping oscillations, and ensuring accurate power sharing among distributed energy resources (DERs) with mismatched physical feeder impedances [cite: 2, 3, 4].
*   **Mitigation of Constant Power Load (CPL) Instability:** CPLs introduce negative incremental impedance, which degrades system damping. Impedance matching criteria are essential here; control strategies must inject virtual positive damping (resistance) to counteract the negative impedance of CPLs and prevent voltage collapse during fluctuations [cite: 5, 6, 7].
*   **Adaptive and Optimized Control:** Static impedance settings are often insufficient for dynamic power fluctuations. Advanced algorithms, such as Gray Wolf Optimization and adaptive virtual impedance, are employed to dynamically tune impedance parameters in real-time, maximizing stability indices and minimizing reactive power mismatches during transient events [cite: 2, 8].

---

## 1. Introduction

The paradigm shift from centralized power generation to distributed energy resources (DERs) has necessitated the development of microgrids—localized grids capable of operating autonomously or in conjunction with the main utility grid. While microgrids offer resilience and efficiency, they introduce complex control challenges, particularly regarding **small-signal stability**. Unlike traditional grids dominated by the high inertia of synchronous generators, microgrids are often dominated by Inverter-Based Resources (IBRs) which lack physical inertia and are highly sensitive to network impedance characteristics.

The user's query regarding the effect of **impedance matching** on small-signal stability under **distributed power fluctuations** touches upon the central nervous system of microgrid control theory. In this context, "impedance matching" is not merely the maximization of power transfer (as in RF circuits) but refers to two distinct control objectives:
1.  **Feeder Impedance Matching:** Equalizing the effective impedance of parallel inverters to ensure accurate power sharing and prevent circulating currents.
2.  **Impedance Shaping (Virtual Impedance):** Modifying the inverter's output impedance to ensure stability against the grid's impedance (based on the Nyquist stability criterion) and to decouple active and reactive power control loops.

This report provides an exhaustive analysis of how impedance characteristics influence stability. It examines the detrimental effects of low X/R ratios, the destabilizing nature of Constant Power Loads (CPLs), and the critical role of adaptive virtual impedance control in stabilizing microgrids subject to stochastic power fluctuations from renewable sources and variable loads.

---

## 2. Theoretical Framework: Impedance-Based Stability Analysis

To understand how impedance matching affects stability, one must first establish the theoretical methods used to analyze IBR-dominated grids. The two primary methods are eigenvalue-based analysis and impedance-based stability analysis.

### 2.1 Eigenvalue vs. Impedance-Based Methods
Eigenvalue analysis requires a comprehensive state-space model of the entire system. While accurate for small, defined systems, it becomes computationally burdensome and impractical for microgrids where the internal parameters of "black-box" inverters from different vendors are unknown [cite: 9].

Consequently, **impedance-based stability analysis** has emerged as the preferred method. This approach treats the microgrid as an interaction between a source subsystem (the inverter) and a load/grid subsystem. Stability is determined by the ratio of the source output impedance ($Z_o$) to the load input impedance ($Z_{in}$), or the inverter impedance to the grid impedance ($Z_g$). According to the Middlebrook criterion and the Generalized Nyquist Criterion, the system remains stable if the ratio $Z_o / Z_{in}$ (or $Z_g / Z_{inv}$) does not encircle the critical point $(-1, j0)$ in the complex plane [cite: 9, 10].

### 2.2 The Role of Power Fluctuations
Small-signal stability analyzes the system's ability to return to a steady state following small disturbances. However, in microgrids, "distributed power fluctuations"—caused by solar irradiance variability, wind gusts, or load switching—act as continuous perturbations.
*   **Resonance Excitation:** Periodic disturbances or step changes in power can excite resonant frequencies in the LCL filters of inverters or the grid network itself [cite: 11].
*   **Operating Point Shifts:** Since small-signal models are linearized around an operating point, large fluctuations can shift the system into a region where the linearized impedance model predicts instability (e.g., a Hopf bifurcation) [cite: 12].

Research indicates that without proper impedance matching (control tuning), these fluctuations can drive the system toward marginal stability, manifesting as sustained harmonic oscillations or voltage collapse [cite: 11, 13].

---

## 3. Impact of Grid Impedance Characteristics (X/R Ratio)

The physical impedance of the distribution lines connecting DERs is a decisive factor in microgrid stability. The ratio of inductive reactance ($X$) to resistance ($R$), known as the X/R ratio, dictates the coupling between control variables.

### 3.1 The Low X/R Ratio Problem
Traditional high-voltage transmission grids are highly inductive (High X/R), allowing for the decoupling of Active Power ($P$) and frequency ($f$), and Reactive Power ($Q$) and Voltage ($V$). This forms the basis of standard droop control ($P-f$ and $Q-V$).

However, microgrids often operate at low voltage levels with resistive lines (Low X/R ratio, often $< 1$).
*   **Coupling Effects:** In resistive grids, $P$ becomes strongly coupled with $V$, and $Q$ with $f$. Standard droop controllers designed for inductive grids fail in this environment, leading to poor transient response and instability [cite: 1, 14, 15].
*   **Experimental Evidence of Instability:** Recent experimental studies (2024) have quantified this impact. In a microgrid setup with a low X/R ratio, active power fluctuations were observed to be extremely high—approximately **±500 W** relative to a total AC power of **~1700 W** [cite: 1]. This represents a fluctuation magnitude of nearly 30%, which is unacceptable for stable operation.
*   **Voltage Regulation Conflicts:** In low X/R grids, inverters attempting to regulate voltage via Volt-VAR control can inadvertently cause significant active power oscillations due to this cross-coupling [cite: 1].

### 3.2 High X/R Ratio and Stability
Conversely, when the effective impedance is dominated by inductance (High X/R), stability is significantly improved.
*   **Fluctuation Suppression:** In the same experimental comparison, configurations with a high X/R ratio showed negligible active power fluctuations under identical disturbance conditions [cite: 1].
*   **Reactive Power Stability:** High X/R ratios also stabilized reactive power. While low X/R scenarios exhibited reactive power fluctuations of ±80 VAR, the high X/R setup showed no significant fluctuation [cite: 1].

This physical reality necessitates "Impedance Matching" in the control domain: if the physical grid is resistive, the control system must "match" the requirements of the droop controller by creating a **Virtual Impedance** that makes the system appear inductive.

---

## 4. Virtual Impedance: The Mechanism of Stability

Virtual Impedance (VI) is a control loop that modifies the voltage reference of the inverter based on the output current, simulating the voltage drop across a physical impedance without the associated energy losses [cite: 3, 4]. It is the primary mechanism for "impedance matching" in modern microgrids.

### 4.1 Decoupling Active and Reactive Power
To address the low X/R problem described in Section 3, a virtual inductor ($L_v$) is often implemented.
*   **Mechanism:** The control logic calculates a voltage drop $\Delta V = I_{out} \times j\omega L_v$ and subtracts it from the voltage reference.
*   **Result:** The total effective impedance ($Z_{total} = Z_{physical} + Z_{virtual}$) becomes dominated by the virtual inductance. This restores the inductive nature of the network, decoupling $P$ and $Q$, and allowing standard droop control to function stably [cite: 2, 16].
*   **Stability Enhancement:** By increasing the effective X/R ratio, VI prevents the cross-coupling instabilities that lead to the massive ±500 W fluctuations observed in resistive grids [cite: 1].

### 4.2 Mismatched Feeder Impedance Matching
In a distributed microgrid, inverters are located at different distances from the Point of Common Coupling (PCC), leading to mismatched feeder impedances.
*   **The Problem:** Mismatched impedances cause unequal voltage drops. Under standard voltage droop control, this leads to severe reactive power sharing errors and circulating currents between inverters, which can trip protection systems or destabilize the bus [cite: 2, 17, 18].
*   **The Solution:** Adaptive virtual impedance is used to "match" the feeder impedances. By tuning the virtual impedance of each inverter such that $Z_{feeder,1} + Z_{virtual,1} = Z_{feeder,2} + Z_{virtual,2}$, the controller ensures that all inverters "see" the same impedance to the PCC [cite: 17, 19].
*   **Outcome:** This matching eliminates circulating currents and ensures that reactive power is shared in proportion to the inverters' ratings, significantly enhancing small-signal stability [cite: 2, 17].

### 4.3 Damping and Harmonic Rejection
Virtual impedance can also be resistive (Virtual Resistance, $R_v$).
*   **Active Damping:** A virtual resistor provides damping to the LCL filter resonance, which is critical when power fluctuations excite system harmonics [cite: 3, 5].
*   **Harmonic Sharing:** By implementing virtual impedance at specific harmonic frequencies, the controller can force inverters to share harmonic currents caused by non-linear loads, preventing voltage distortion and instability [cite: 5, 20].

---

## 5. Constant Power Loads (CPL) and Negative Incremental Impedance

A specific and severe stability threat in microgrids comes from Constant Power Loads (CPLs), such as tightly regulated DC-DC converters feeding electronics or motor drives.

### 5.1 The Negative Impedance Phenomenon
CPLs draw current $I = P/V$. If the bus voltage $V$ decreases, the CPL draws *more* current to maintain constant power $P$.
*   **Small-Signal Analysis:** The incremental impedance is $d V / d I = - V^2 / P$. This is a **negative resistance** [cite: 5, 6, 7].
*   **Instability:** In the small-signal model, this negative resistance cancels out the positive physical resistance (damping) of the feeder and filters. If the net resistance becomes negative, the system poles move into the Right Half Plane (RHP), leading to unbounded oscillations and voltage collapse [cite: 5, 21].

### 5.2 Impedance Matching for CPL Stabilization
To stabilize a microgrid with significant CPLs, impedance matching criteria are applied to ensure the source impedance is sufficiently lower than the load impedance (Middlebrook criterion) or that the net damping is positive.
*   **Virtual Resistance Injection:** Control strategies inject a virtual *positive* resistance (or active damping) to counteract the CPL's negative resistance. This shifts the unstable poles back into the stable Left Half Plane (LHP) [cite: 5, 6, 21].
*   **Source-Side vs. Load-Side:** This virtual impedance can be implemented at the source converter (to stiffen the bus) or at the load converter (to modify its input characteristics). Research confirms that this technique effectively dampens the system, preventing instability even under power fluctuations caused by CPL dynamics [cite: 6, 22].

---

## 6. Adaptive Control and Optimization Techniques

Given that microgrid operating conditions (number of active sources, load levels, grid connection status) change dynamically, a fixed virtual impedance value is often suboptimal. Recent research focuses on adaptive impedance matching.

### 6.1 Optimization Algorithms (Gray Wolf, PSO)
Advanced algorithms are used to find the optimal virtual impedance parameters that maximize stability margins while minimizing power sharing errors.
*   **Gray Wolf Optimization (GWO):** A 2025 study highlights the use of GWO to create a virtual impedance setting strategy. The algorithm analyzes all possible operating points to maximize the microgrid stability index. Results showed that this method kept voltage and frequency within acceptable boundaries and eliminated reactive power imbalances [cite: 2, 8].
*   **Particle Swarm Optimization (PSO):** Similar to GWO, PSO is used to tune virtual impedances to minimize reactive power mismatches and maximize small-signal stability, validated through time-domain simulations [cite: 23].

### 6.2 Adaptive Virtual Impedance (AVI)
AVI systems monitor the grid state in real-time and adjust parameters accordingly.
*   **Online Estimation:** Some systems estimate feeder impedance online and adjust the virtual impedance to match. This makes the control robust to topology changes (e.g., plug-and-play of new DERs) [cite: 17].
*   **Transient Response:** Adaptive schemes can temporarily increase virtual inertia or damping during a transient power fluctuation (like a solar ramp event) and then relax it during steady state to minimize voltage drops [cite: 24, 25].

---

## 7. Case Studies and Experimental Validation

The theoretical concepts discussed are supported by specific experimental findings in the literature.

### 7.1 Case Study: Low vs. High X/R Ratio (2024)
*   **Setup:** A microgrid with smart inverters operating under Volt-VAR control.
*   **Scenario:** Distributed power fluctuations were introduced.
*   **Results:**
    *   **Low X/R (Resistive):** Active power fluctuated by **±500 W** (on a 1700 W base). Reactive power fluctuated by **±80 VAR**. The system was marginally stable [cite: 1].
    *   **High X/R (Inductive):** Active power fluctuations were **negligible**. Reactive power fluctuations were eliminated.
*   **Conclusion:** Physical or virtual impedance matching that ensures a high effective X/R ratio is mandatory for small-signal stability under power fluctuations.

### 7.2 Case Study: Mismatched Feeders and Reactive Power Sharing
*   **Setup:** Islanded microgrid with parallel inverters connected via unequal line lengths.
*   **Problem:** Conventional droop control resulted in significant circulating currents and poor reactive power sharing.
*   **Solution:** An adaptive complex virtual impedance strategy was applied.
*   **Results:** The strategy eliminated circulating currents and reduced the coupling between real and reactive power. The stability assessment confirmed that the method maintained voltage and frequency within boundaries despite the mismatched physical impedance [cite: 2].

### 7.3 Case Study: CPL Stabilization
*   **Setup:** DC microgrid with constant power loads.
*   **Analysis:** Small-signal analysis revealed unstable poles due to negative incremental impedance.
*   **Intervention:** Virtual impedance-based stabilizers (Type I at output capacitor, Type II at output inductor) were enabled.
*   **Results:** The unstable poles were forced into the stable region. The system successfully rejected disturbances from load steps, validating the impedance matching criterion [cite: 5, 6, 21].

---

## 8. Conclusion

The research conclusively demonstrates that **impedance matching is a determinant factor in the small-signal stability of microgrids**, particularly under distributed power fluctuations. The relationship is multifaceted:

1.  **Physical Impedance Dictates Coupling:** The inherent X/R ratio of the microgrid lines determines whether active and reactive power control loops are coupled. Low X/R ratios, common in microgrids, lead to severe instability and large power fluctuations (up to 30% of rated power) if left unaddressed.
2.  **Virtual Impedance is the Enabler:** Virtual impedance control serves as the primary "impedance matching" tool. It stabilizes the system by:
    *   Restoring an inductive effective impedance to decouple control loops.
    *   Equalizing mismatched feeder impedances to ensure accurate power sharing.
    *   Providing active damping to suppress resonances excited by power fluctuations.
3.  **CPLs Require Active Matching:** The negative impedance of constant power loads must be "matched" or cancelled by virtual positive resistance to prevent voltage collapse.
4.  **Adaptivity is Key:** Static impedance settings are insufficient for the dynamic nature of distributed energy resources. Advanced optimization (e.g., Gray Wolf Optimization) and adaptive control strategies are required to maintain stability indices across varying operating points.

In summary, impedance matching—whether achieved through physical network design or, more commonly, through advanced virtual impedance control algorithms—is not optional but fundamental to maintaining the small-signal stability of microgrids facing the stochastic nature of distributed power generation.

---

### References
*   **[cite: 1]** *Impact of Grid Impedance on Power Stability (2024)*: Documented ±500 W fluctuations in low X/R grids vs. negligible fluctuations in high X/R grids.
*   **[cite: 2, 8]** *Gray Wolf Optimization & Virtual Impedance*: Application of optimization algorithms to tune virtual impedance for stability and power sharing.
*   **[cite: 5, 6, 21]** *Constant Power Loads & Negative Impedance*: Analysis of CPL instability and virtual impedance stabilizers.
*   **[cite: 3, 4]** *Virtual Impedance Fundamentals*: Explanation of VI for harmonic correction, stability, and power sharing.
*   **[cite: 9, 10]** *Stability Analysis Methods*: Comparison of eigenvalue vs. impedance-based stability analysis (Nyquist).
*   **[cite: 14, 15, 16]** *X/R Ratio Effects*: Theoretical and simulation analysis of resistive vs. inductive grid coupling.
*   **[cite: 17, 18, 26]** *Mismatched Feeder Impedance*: Solutions for reactive power sharing errors using adaptive VI.
*   **[cite: 22, 27]** *Inductive Network Impedance*: Impact on PV inverter control performance and stability margins.
*   **[cite: 28]** *Impedance Scan Tools*: Use of frequency scans to identify resonance and damping issues in IBR grids.
*   **[cite: 7]** *DC Microgrid CPLs*: Nonlinear control and disturbance observers for CPL stabilization.

**Sources:**
1. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEG2kcg1dvhiOgddFhru8clZlktmt6FTmg0jZEL55JHEtH50gZS20SHHgendgR9Vetj4MbGbD5IAR3r_HyTE8AyAKA6dH_jNJxZIkNk9_e5qCRpXX_6l1cwefQ1i4_PLg==)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiSMDD4_jmGJpGAt826QU1_9ZTnu2IAG6mILOyQaXfzj_1as_NAEAaBIRBrD0P6vbz2bxv5Dx7N0Upc1HL8q72wnGdXhq7jAQNqIQ-ovnxcgwGekOfMZjzHDc51-rZ-uxQkMXMfnWd0IxATMpDKmR9pgt7YOjAW9RI-ElxcO-oWbDM1GimA4zhkInn-k4gQxRZMQvzz9QjnkEybIvwI7My63jI693qiKAi_X-22tDcrbTiDa4QWRy1AggjwcU5Ddm_Yx5C7wfIbadhIgQAALeQKNFxhmz1f1a0cN1DQ-SspVf6wbJ6Y9EM13UQfgD06U0u-U7qvHZPgsWsnw==)
3. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMPcxQkCGNwKXZnc_8dXXZDnXEBINsy2w4SXqsYViCI43YgSQX1vpIjv09wo3NLDFkUEQ1xiOu15XfbUEMaxGX8BXQMHtzDsBW_Z7dzywErANzxPQyyYysrH4vhHlWlg==)
4. [sintef.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEv2vpD2Gfq8GFFGfFt9dXI3kC8T-k_EIjgoJ95dO8hT7LifQnvylDumtx7TbmSRHG5eqcrI8mSeI6gFmb0nf73Ub62UbM4xtzX0jxIpEgGekPvd7i9L_uAkPI3Bg0gpyY2PBVZ5AEkAw8HCcbJ6cWlWufq19VNqXOv3pu5OznbZffiyVUmFYz6ljLsV4yDMDYeT8oS-LThtvlW14vtajK5JSaRBXvp_ieOR27QoMAzuasMCQSN0HDhd1sZVDU=)
5. [aau.dk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtFLDeAAGAbVjnWR8C8Hc2ptwxjOQc_xaRGmRxpAyeWCRIrKNYjMyjZ0gPC5ycXXyNEx0v2IFXsQ0OPch3q_appA271Kyw_y8bQosYNh1V1qGfBNKEJlOLcLnfMpyK8MfrbofYlHxv0Px2EHTp1GNljoaFgW3I)
6. [csic.es](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvK30NZ-og9ft_pjeZPw-8a-XJKB4SLDqV-oVMUcfPHW8FDJn-1Whm4EI9CDtOSKi68LQ3F-2NaAre3Vzq_DLIOI2pvGD-ml5PIl1XQ0Ous9k-5qwyE8thPyndsBpYv-SNLmrvslFSviRnW3H0HCP0Bs1WIIlRaeg4kUdG3A==)
7. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDU4VC3PjqUlSeETMOGQNBLgrO-aDnqlYYaB6x5RkmDhyCXBekmhn819SMxkk85JS4jiz9JngxKKtfI58a64H-UGezvL9CR6d7_WurnfQHvqc27Dt2ZZ5X3HVq2rlK)
8. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0H2DcftiniAa1Z5bR_4-frjZGo4G94C5Q60hCsj4L5yT6rMCZMYrsGe-EsgQ219AIWdPmlk9NJhj0cla40Dez9HKfsdMz5-QTgkOlgJ13-civc1KdZT074WNtmHB6vV1YNHDWsilzMAtqBdl8deZXi7GwpXjEun-dZt-zT0s=)
9. [monash.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVf6IT9pHOVrUwohtZ3K9gB0lvvnMi4HeasqKGKk3rVcDymv4ekC7rvlb_W2SeYVVn5Osxu0B3NE12fJt9M812zrZBmC5qxyqRztU9u2R6QsTqUNTL0GiyH-I1qFtfwT3AnINKgWMPo7kPoCTgxu6ke8P1tCSfjGTL232LFFLtT3sDK3UFdyyY8gsX5ZzGSC3LjoPhsWSrsu0M-WebNaWg30S_E6QMaa8Cnct9dT9eBVkMEd8_)
10. [aau.dk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcGaDS_No2zGO4KKiTxKfJySBPeL_vDm53m5y8TzdNZFuYEu8QO9JuAGMgIFL7k5ukOV0M6cU-LfORknkuyjENmNFmCVBiF4Ty7aALZXApIM8T8FhiIzPI2UkWPdQy8uaFgBVDxFabOMiXcZg-Y1LRutRqrCE0R0xOS-jEas1Ir2akhR0kxCfcbV0bvdSM_AmUzVUm44wbX0lkCA==)
11. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAokwOxkppmbzelkoxsKCYG27Ct-v4JWyN8W-X3iGzPk903x4WO4ffhqYmxBHiwY7cyim8tKVuE005VR_kpeSm4rnoFv1_p-keRUs2r0caGNbO5i0Fxxp9Ln70d7KOxyou)
12. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbFE9rlqdFIfStxHkS3IhDX1_xNpNA8qrUkIwLB4aXsQKELkCSHQWVDYE27hJfd2XsCDD8RH-AabEX0uSdbAg4TbdhuAZsTbMzwoLNnF3M0CybXyHt_F3_jpssHHfb4_elHLWgqSGGd-Ari7I=)
13. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbogcXfzhel-anFLFSVK8KCO01SRCEDGQmMM4nAtL9VQ4LWj6Uu1ZS3o1HJJf80U1Nc5fNjkUcDgeBKG9_AZY5tjGOGgSrbSeF0XsWTengaKgfcuzxdqQCA8gFGIk=)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGt8bZ3YnnJy1p0L7Q98FDniyVaE4V7IZ3C5uINKgS8q-lojWCyYo8ntRj9Aoc3zhLU0m5py8eodtghzzMOkAzoc5ER6sokgjn03AFWQ_BTT5-nOzP4fNoa-YItGDZ0-ynHpg5Asfh5w8PZWjECKASzD9zUamgdvu93_ZZCna7SfFV2lzrMuSbyEmCZHqYUpCVUUxPlHaGyvVbBl5tLaalTHdVz8SOYjTCrZtkN4ys=)
15. [aau.dk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOlKWekU3Fud59tFmttBRgpy33cPlmsbWd_akuprjPuM7cHbhEnWXhkco9soLFf2KcBTI9qTfx1xZrAcKEvJeWIRHsbumtTYO2Q-opm2h0z3bsvCO8FNqDmP-uie0q2sCB2sTYvDBF3IO1_uS-H7Te_fHChrab7qP0g8JzltUHTGCcYHCOqClYkfs86hDtfkuht39sMNkT0tGqu8i_5p80-rK6A92sfMntrdiHe9VC7gX6UA==)
16. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJOFO_7eXi77FtcA4eW_JO8MBUK77KC2HTjyQ-EoAk64KgI50GgPswX5Qp7STk1If7dCJ0bYWS8_pNfXAFvSbGbPCkFup09RvvHaekCaBr-5Gs6A3jq1SCZi3fpfMNp3EwvZ4QCWyLavppxyyjnxbyqUpnrcvoZjnimWllSWuqfHoqFsWOlKU8Kzv-ZBj_0kWE)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEazr9pdvsp_pr3omjbl9JRuTDVkwS96MzEit6EN-P9sUy1wqjveHgbDIkLeE45vtssjhmSZ4IcVWn7silvbaYuHiEsOGsRBprXwB3vR8iiMePeuLSSEnX0ijb8VLkzg9j2sn0ogFZGmO1-ygNVIQ_FCZzYVMly0rkqPXVftOQbcFaij7Q66kw_kHlxjl8nX4wLJza4LPFWgdeqps4MpyNCFSywdSjukUDihqY3C-EeKgtdeOL6I1gqR7qJZ1s9CK6GpxEvldwLlt4bLOn64hfZNwhWoHEkxxeRio8=)
18. [aau.dk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMTsmTOZE_mqtw8WCfI_aSZ0RyCNDOJvZzkDvFiHoJ4z0BtE0uMj92_yT1vYZ1H6Sd9mriyNrqoR8qbaCowi6-uZl-MiTsjmc1cy2AFQ84TFXgO0tin76Ih-ZOjDMo_h4TBnUuppI3GiBWVzlWaPV4nPylc6LlZQ-9CcmrD07x723WCRZ3nxAEZNJqTtDhpb0_S6iJJvwDuX6Wn7Q3EN0yzta5uEhVSgOOXSar)
19. [mnsu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIyrTBcFPFijPhhGVu9K0E9RJqvqlM5mI1JoWrG_wc8CiGOfGOR_GjXo2cNBE9-N-UAnmemKGzBDSKaEAb1SJqi2VAULTtajVXyNS9ubav1saFaST6qk-nz_phjBVWu2EJMwPgvKiuhPVAEM0UBOIPzvD6LINiQH26uAE2ySStjM9TyYptKUqN2sUCuXRl9r08kVdVGhzqUQ==)
20. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVS1gXv7zlHkM1oY8JgcX_w5LQtnnljU64F53NON1NdWNDyhaG7UxnekojbuRV5opjx6WhOlOcIpK0uehPvtZUc1YhlwMWPZTFhG7c3GhurdvRFrq7_TyJZh18gcbMEz8Lqu9D802wkG68FRqfSg==)
21. [aau.dk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVTlQ2PnCqMMQV12hcylTsmpM9fn2ojCz6Sr5cImBa0nAjSzAvWeKbgkNilsleY2Ox45BCWL9RvcQSKIBHp3tR5T16ClZyqP9QYx3sqQ3VCaiKIOAKEouJM0trEHi4MD7SS4liHLTpdNbWc1S-V9uP_pUiWuTVr3cQqbWiiAzD61ua)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNS7b1PeVNK0sVcNdgcQv7Qg16ZIy8j0MRqmGulWOGDHo-wvR1MPiUntV45re8s9uZKUq9wuDsqsHjIE6HMqF6tl07018HbYIuEErCeGccWGIsua0o5LZxHB3taPh0JTCyxkfHcV0VR2fsVC7AqjoqiYto98ryn45Eng36rNS14QepqJLcnOCVQYhV5s20BKAqLKTwGDhDe4v-JQ==)
23. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNv8pram2IYlWnnTE9vwiVc9Mdo35H7vfbZroVDHTeVRjYN97zbUuHHNE8LQQcCd74LUb-lwtbDOEfAGaXiiJP-I4p73g_WXWrG_x_hUIfkR2x-n4JwONQGEw8nW2FmclnfMAHPOWJ-IshTCgFlLFIbGZ7OLUjQHuV91nKEiqGrOL-3dwKXOVsD2eYtsUctD5K_nVgB-wFhw==)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcsNcXy24yYBf59EYwA3RayVWWt4uYc2igrdVKu03KoFPWm-_2VNYmSWONlGp7wS8JgY2z_pxMmH8uJMjWSrpqd4hYPTutDM0hFlTuIgfA95MjIwzKr0IkbYhl3N50HwCA2p0ROka4Y563gn5y8c0pPZotKdFVmSgO-EOg3UvVMTzoS9hYWEtlWQrMBV2ww_xN2THx0xIruMrw7ZeJBOjrTgJ1eBmb)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBwv_NnC7a5mFl0g_KLLTeaBXikHxXmg6Wheu5ydc00nRpi1excRPhZOaYuYWr7jlpdqiuJIOz4uDIS_IGj08bi-cxB6IaH_srTuPl9v6gq4xK-HBzLlk4xpRDmcyvQpgr-2xAXOs5kg0d6TkYP3_gGuIj7MEKtKyB2e9v20sRYr0lw1I9SbcvV87mDdoBq0M4-ny0QWPRlnqKbryxTLL61jc5xijAOqX36ViCo5lpkIpEpqtoTw8p-MQiLSsodCLX5ikXWGczc7qnBfCbq9FTK8zzCBzATp4_fwV9ehEilSv1J3cvWqa36in7ZQDMpNEoF27RSs8GfAmaXk6nHZ1X43URXEZGBu66kw==)
26. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6tPnmXK1M0_Rhx30MHDIt7OF3epv-lyRdobZ_Ahu3Ee9KXnfpllEnEq_y1-VDguqoawHZGI1ZxnndIl3XI7Ii47mqvvH5tXzIRkFdFNXsga9X9-uYBYvEClKOC9Q=)
27. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKiniNnOILA3Rmg-W8SIoBT2HEBmwtgGo3lpBDl-CygCUl1W1SVMYpeStbqZl97ZWBDV7S8QpR79QQU1xQnrpIFyNOq_oRhAyhuFs0TkJDt5ntldXdQCqbOofsT3fIcYFkzn8=)
28. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtAtaVxF9AEY0_zPNcrXk4ew19zJwdJL6m7OMz_kEhxqMqWJd0mAyUZs_lPuuJJ4Yjq1r8yPow_tbJUo8dcHcgwlRNnMhl4hSO6_0QsttHOq45r5iOPK1q9u3Mnew_Lz3z)


## Annotations
Annotation(end_index=551, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEG2kcg1dvhiOgddFhru8clZlktmt6FTmg0jZEL55JHEtH50gZS20SHHgendgR9Vetj4MbGbD5IAR3r_HyTE8AyAKA6dH_jNJxZIkNk9_e5qCRpXX_6l1cwefQ1i4_PLg==', start_index=542)
Annotation(end_index=1014, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiSMDD4_jmGJpGAt826QU1_9ZTnu2IAG6mILOyQaXfzj_1as_NAEAaBIRBrD0P6vbz2bxv5Dx7N0Upc1HL8q72wnGdXhq7jAQNqIQ-ovnxcgwGekOfMZjzHDc51-rZ-uxQkMXMfnWd0IxATMpDKmR9pgt7YOjAW9RI-ElxcO-oWbDM1GimA4zhkInn-k4gQxRZMQvzz9QjnkEybIvwI7My63jI693qiKAi_X-22tDcrbTiDa4QWRy1AggjwcU5Ddm_Yx5C7wfIbadhIgQAALeQKNFxhmz1f1a0cN1DQ-SspVf6wbJ6Y9EM13UQfgD06U0u-U7qvHZPgsWsnw==', start_index=999)
Annotation(end_index=1014, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEv2vpD2Gfq8GFFGfFt9dXI3kC8T-k_EIjgoJ95dO8hT7LifQnvylDumtx7TbmSRHG5eqcrI8mSeI6gFmb0nf73Ub62UbM4xtzX0jxIpEgGekPvd7i9L_uAkPI3Bg0gpyY2PBVZ5AEkAw8HCcbJ6cWlWufq19VNqXOv3pu5OznbZffiyVUmFYz6ljLsV4yDMDYeT8oS-LThtvlW14vtajK5JSaRBXvp_ieOR27QoMAzuasMCQSN0HDhd1sZVDU=', start_index=999)
Annotation(end_index=1014, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMPcxQkCGNwKXZnc_8dXXZDnXEBINsy2w4SXqsYViCI43YgSQX1vpIjv09wo3NLDFkUEQ1xiOu15XfbUEMaxGX8BXQMHtzDsBW_Z7dzywErANzxPQyyYysrH4vhHlWlg==', start_index=999)
Annotation(end_index=1381, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtFLDeAAGAbVjnWR8C8Hc2ptwxjOQc_xaRGmRxpAyeWCRIrKNYjMyjZ0gPC5ycXXyNEx0v2IFXsQ0OPch3q_appA271Kyw_y8bQosYNh1V1qGfBNKEJlOLcLnfMpyK8MfrbofYlHxv0Px2EHTp1GNljoaFgW3I', start_index=1366)
Annotation(end_index=1381, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvK30NZ-og9ft_pjeZPw-8a-XJKB4SLDqV-oVMUcfPHW8FDJn-1Whm4EI9CDtOSKi68LQ3F-2NaAre3Vzq_DLIOI2pvGD-ml5PIl1XQ0Ous9k-5qwyE8thPyndsBpYv-SNLmrvslFSviRnW3H0HCP0Bs1WIIlRaeg4kUdG3A==', start_index=1366)
Annotation(end_index=1381, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDU4VC3PjqUlSeETMOGQNBLgrO-aDnqlYYaB6x5RkmDhyCXBekmhn819SMxkk85JS4jiz9JngxKKtfI58a64H-UGezvL9CR6d7_WurnfQHvqc27Dt2ZZ5X3HVq2rlK', start_index=1366)
Annotation(end_index=1762, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiSMDD4_jmGJpGAt826QU1_9ZTnu2IAG6mILOyQaXfzj_1as_NAEAaBIRBrD0P6vbz2bxv5Dx7N0Upc1HL8q72wnGdXhq7jAQNqIQ-ovnxcgwGekOfMZjzHDc51-rZ-uxQkMXMfnWd0IxATMpDKmR9pgt7YOjAW9RI-ElxcO-oWbDM1GimA4zhkInn-k4gQxRZMQvzz9QjnkEybIvwI7My63jI693qiKAi_X-22tDcrbTiDa4QWRy1AggjwcU5Ddm_Yx5C7wfIbadhIgQAALeQKNFxhmz1f1a0cN1DQ-SspVf6wbJ6Y9EM13UQfgD06U0u-U7qvHZPgsWsnw==', start_index=1750)
Annotation(end_index=1762, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0H2DcftiniAa1Z5bR_4-frjZGo4G94C5Q60hCsj4L5yT6rMCZMYrsGe-EsgQ219AIWdPmlk9NJhj0cla40Dez9HKfsdMz5-QTgkOlgJ13-civc1KdZT074WNtmHB6vV1YNHDWsilzMAtqBdl8deZXi7GwpXjEun-dZt-zT0s=', start_index=1750)
Annotation(end_index=4194, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVf6IT9pHOVrUwohtZ3K9gB0lvvnMi4HeasqKGKk3rVcDymv4ekC7rvlb_W2SeYVVn5Osxu0B3NE12fJt9M812zrZBmC5qxyqRztU9u2R6QsTqUNTL0GiyH-I1qFtfwT3AnINKgWMPo7kPoCTgxu6ke8P1tCSfjGTL232LFFLtT3sDK3UFdyyY8gsX5ZzGSC3LjoPhsWSrsu0M-WebNaWg30S_E6QMaa8Cnct9dT9eBVkMEd8_', start_index=4185)
Annotation(end_index=4817, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVf6IT9pHOVrUwohtZ3K9gB0lvvnMi4HeasqKGKk3rVcDymv4ekC7rvlb_W2SeYVVn5Osxu0B3NE12fJt9M812zrZBmC5qxyqRztU9u2R6QsTqUNTL0GiyH-I1qFtfwT3AnINKgWMPo7kPoCTgxu6ke8P1tCSfjGTL232LFFLtT3sDK3UFdyyY8gsX5ZzGSC3LjoPhsWSrsu0M-WebNaWg30S_E6QMaa8Cnct9dT9eBVkMEd8_', start_index=4804)
Annotation(end_index=4817, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcGaDS_No2zGO4KKiTxKfJySBPeL_vDm53m5y8TzdNZFuYEu8QO9JuAGMgIFL7k5ukOV0M6cU-LfORknkuyjENmNFmCVBiF4Ty7aALZXApIM8T8FhiIzPI2UkWPdQy8uaFgBVDxFabOMiXcZg-Y1LRutRqrCE0R0xOS-jEas1Ir2akhR0kxCfcbV0bvdSM_AmUzVUm44wbX0lkCA==', start_index=4804)
Annotation(end_index=5312, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAokwOxkppmbzelkoxsKCYG27Ct-v4JWyN8W-X3iGzPk903x4WO4ffhqYmxBHiwY7cyim8tKVuE005VR_kpeSm4rnoFv1_p-keRUs2r0caGNbO5i0Fxxp9Ln70d7KOxyou', start_index=5302)
Annotation(end_index=5563, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbFE9rlqdFIfStxHkS3IhDX1_xNpNA8qrUkIwLB4aXsQKELkCSHQWVDYE27hJfd2XsCDD8RH-AabEX0uSdbAg4TbdhuAZsTbMzwoLNnF3M0CybXyHt_F3_jpssHHfb4_elHLWgqSGGd-Ari7I=', start_index=5553)
Annotation(end_index=5790, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAokwOxkppmbzelkoxsKCYG27Ct-v4JWyN8W-X3iGzPk903x4WO4ffhqYmxBHiwY7cyim8tKVuE005VR_kpeSm4rnoFv1_p-keRUs2r0caGNbO5i0Fxxp9Ln70d7KOxyou', start_index=5776)
Annotation(end_index=5790, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbogcXfzhel-anFLFSVK8KCO01SRCEDGQmMM4nAtL9VQ4LWj6Uu1ZS3o1HJJf80U1Nc5fNjkUcDgeBKG9_AZY5tjGOGgSrbSeF0XsWTengaKgfcuzxdqQCA8gFGIk=', start_index=5776)
Annotation(end_index=6755, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEG2kcg1dvhiOgddFhru8clZlktmt6FTmg0jZEL55JHEtH50gZS20SHHgendgR9Vetj4MbGbD5IAR3r_HyTE8AyAKA6dH_jNJxZIkNk9_e5qCRpXX_6l1cwefQ1i4_PLg==', start_index=6738)
Annotation(end_index=6755, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOlKWekU3Fud59tFmttBRgpy33cPlmsbWd_akuprjPuM7cHbhEnWXhkco9soLFf2KcBTI9qTfx1xZrAcKEvJeWIRHsbumtTYO2Q-opm2h0z3bsvCO8FNqDmP-uie0q2sCB2sTYvDBF3IO1_uS-H7Te_fHChrab7qP0g8JzltUHTGCcYHCOqClYkfs86hDtfkuht39sMNkT0tGqu8i_5p80-rK6A92sfMntrdiHe9VC7gX6UA==', start_index=6738)
Annotation(end_index=6755, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGt8bZ3YnnJy1p0L7Q98FDniyVaE4V7IZ3C5uINKgS8q-lojWCyYo8ntRj9Aoc3zhLU0m5py8eodtghzzMOkAzoc5ER6sokgjn03AFWQ_BTT5-nOzP4fNoa-YItGDZ0-ynHpg5Asfh5w8PZWjECKASzD9zUamgdvu93_ZZCna7SfFV2lzrMuSbyEmCZHqYUpCVUUxPlHaGyvVbBl5tLaalTHdVz8SOYjTCrZtkN4ys=', start_index=6738)
Annotation(end_index=7052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEG2kcg1dvhiOgddFhru8clZlktmt6FTmg0jZEL55JHEtH50gZS20SHHgendgR9Vetj4MbGbD5IAR3r_HyTE8AyAKA6dH_jNJxZIkNk9_e5qCRpXX_6l1cwefQ1i4_PLg==', start_index=7043)
Annotation(end_index=7369, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEG2kcg1dvhiOgddFhru8clZlktmt6FTmg0jZEL55JHEtH50gZS20SHHgendgR9Vetj4MbGbD5IAR3r_HyTE8AyAKA6dH_jNJxZIkNk9_e5qCRpXX_6l1cwefQ1i4_PLg==', start_index=7360)
Annotation(end_index=7725, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEG2kcg1dvhiOgddFhru8clZlktmt6FTmg0jZEL55JHEtH50gZS20SHHgendgR9Vetj4MbGbD5IAR3r_HyTE8AyAKA6dH_jNJxZIkNk9_e5qCRpXX_6l1cwefQ1i4_PLg==', start_index=7716)
Annotation(end_index=7946, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEG2kcg1dvhiOgddFhru8clZlktmt6FTmg0jZEL55JHEtH50gZS20SHHgendgR9Vetj4MbGbD5IAR3r_HyTE8AyAKA6dH_jNJxZIkNk9_e5qCRpXX_6l1cwefQ1i4_PLg==', start_index=7937)
Annotation(end_index=8498, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEv2vpD2Gfq8GFFGfFt9dXI3kC8T-k_EIjgoJ95dO8hT7LifQnvylDumtx7TbmSRHG5eqcrI8mSeI6gFmb0nf73Ub62UbM4xtzX0jxIpEgGekPvd7i9L_uAkPI3Bg0gpyY2PBVZ5AEkAw8HCcbJ6cWlWufq19VNqXOv3pu5OznbZffiyVUmFYz6ljLsV4yDMDYeT8oS-LThtvlW14vtajK5JSaRBXvp_ieOR27QoMAzuasMCQSN0HDhd1sZVDU=', start_index=8486)
Annotation(end_index=8498, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMPcxQkCGNwKXZnc_8dXXZDnXEBINsy2w4SXqsYViCI43YgSQX1vpIjv09wo3NLDFkUEQ1xiOu15XfbUEMaxGX8BXQMHtzDsBW_Z7dzywErANzxPQyyYysrH4vhHlWlg==', start_index=8486)
Annotation(end_index=9150, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiSMDD4_jmGJpGAt826QU1_9ZTnu2IAG6mILOyQaXfzj_1as_NAEAaBIRBrD0P6vbz2bxv5Dx7N0Upc1HL8q72wnGdXhq7jAQNqIQ-ovnxcgwGekOfMZjzHDc51-rZ-uxQkMXMfnWd0IxATMpDKmR9pgt7YOjAW9RI-ElxcO-oWbDM1GimA4zhkInn-k4gQxRZMQvzz9QjnkEybIvwI7My63jI693qiKAi_X-22tDcrbTiDa4QWRy1AggjwcU5Ddm_Yx5C7wfIbadhIgQAALeQKNFxhmz1f1a0cN1DQ-SspVf6wbJ6Y9EM13UQfgD06U0u-U7qvHZPgsWsnw==', start_index=9137)
Annotation(end_index=9150, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJOFO_7eXi77FtcA4eW_JO8MBUK77KC2HTjyQ-EoAk64KgI50GgPswX5Qp7STk1If7dCJ0bYWS8_pNfXAFvSbGbPCkFup09RvvHaekCaBr-5Gs6A3jq1SCZi3fpfMNp3EwvZ4QCWyLavppxyyjnxbyqUpnrcvoZjnimWllSWuqfHoqFsWOlKU8Kzv-ZBj_0kWE', start_index=9137)
Annotation(end_index=9350, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEG2kcg1dvhiOgddFhru8clZlktmt6FTmg0jZEL55JHEtH50gZS20SHHgendgR9Vetj4MbGbD5IAR3r_HyTE8AyAKA6dH_jNJxZIkNk9_e5qCRpXX_6l1cwefQ1i4_PLg==', start_index=9341)
Annotation(end_index=9832, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEazr9pdvsp_pr3omjbl9JRuTDVkwS96MzEit6EN-P9sUy1wqjveHgbDIkLeE45vtssjhmSZ4IcVWn7silvbaYuHiEsOGsRBprXwB3vR8iiMePeuLSSEnX0ijb8VLkzg9j2sn0ogFZGmO1-ygNVIQ_FCZzYVMly0rkqPXVftOQbcFaij7Q66kw_kHlxjl8nX4wLJza4LPFWgdeqps4MpyNCFSywdSjukUDihqY3C-EeKgtdeOL6I1gqR7qJZ1s9CK6GpxEvldwLlt4bLOn64hfZNwhWoHEkxxeRio8=', start_index=9815)
Annotation(end_index=9832, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiSMDD4_jmGJpGAt826QU1_9ZTnu2IAG6mILOyQaXfzj_1as_NAEAaBIRBrD0P6vbz2bxv5Dx7N0Upc1HL8q72wnGdXhq7jAQNqIQ-ovnxcgwGekOfMZjzHDc51-rZ-uxQkMXMfnWd0IxATMpDKmR9pgt7YOjAW9RI-ElxcO-oWbDM1GimA4zhkInn-k4gQxRZMQvzz9QjnkEybIvwI7My63jI693qiKAi_X-22tDcrbTiDa4QWRy1AggjwcU5Ddm_Yx5C7wfIbadhIgQAALeQKNFxhmz1f1a0cN1DQ-SspVf6wbJ6Y9EM13UQfgD06U0u-U7qvHZPgsWsnw==', start_index=9815)
Annotation(end_index=9832, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMTsmTOZE_mqtw8WCfI_aSZ0RyCNDOJvZzkDvFiHoJ4z0BtE0uMj92_yT1vYZ1H6Sd9mriyNrqoR8qbaCowi6-uZl-MiTsjmc1cy2AFQ84TFXgO0tin76Ih-ZOjDMo_h4TBnUuppI3GiBWVzlWaPV4nPylc6LlZQ-9CcmrD07x723WCRZ3nxAEZNJqTtDhpb0_S6iJJvwDuX6Wn7Q3EN0yzta5uEhVSgOOXSar', start_index=9815)
Annotation(end_index=10139, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEazr9pdvsp_pr3omjbl9JRuTDVkwS96MzEit6EN-P9sUy1wqjveHgbDIkLeE45vtssjhmSZ4IcVWn7silvbaYuHiEsOGsRBprXwB3vR8iiMePeuLSSEnX0ijb8VLkzg9j2sn0ogFZGmO1-ygNVIQ_FCZzYVMly0rkqPXVftOQbcFaij7Q66kw_kHlxjl8nX4wLJza4LPFWgdeqps4MpyNCFSywdSjukUDihqY3C-EeKgtdeOL6I1gqR7qJZ1s9CK6GpxEvldwLlt4bLOn64hfZNwhWoHEkxxeRio8=', start_index=10125)
Annotation(end_index=10139, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIyrTBcFPFijPhhGVu9K0E9RJqvqlM5mI1JoWrG_wc8CiGOfGOR_GjXo2cNBE9-N-UAnmemKGzBDSKaEAb1SJqi2VAULTtajVXyNS9ubav1saFaST6qk-nz_phjBVWu2EJMwPgvKiuhPVAEM0UBOIPzvD6LINiQH26uAE2ySStjM9TyYptKUqN2sUCuXRl9r08kVdVGhzqUQ==', start_index=10125)
Annotation(end_index=10347, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEazr9pdvsp_pr3omjbl9JRuTDVkwS96MzEit6EN-P9sUy1wqjveHgbDIkLeE45vtssjhmSZ4IcVWn7silvbaYuHiEsOGsRBprXwB3vR8iiMePeuLSSEnX0ijb8VLkzg9j2sn0ogFZGmO1-ygNVIQ_FCZzYVMly0rkqPXVftOQbcFaij7Q66kw_kHlxjl8nX4wLJza4LPFWgdeqps4MpyNCFSywdSjukUDihqY3C-EeKgtdeOL6I1gqR7qJZ1s9CK6GpxEvldwLlt4bLOn64hfZNwhWoHEkxxeRio8=', start_index=10334)
Annotation(end_index=10347, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiSMDD4_jmGJpGAt826QU1_9ZTnu2IAG6mILOyQaXfzj_1as_NAEAaBIRBrD0P6vbz2bxv5Dx7N0Upc1HL8q72wnGdXhq7jAQNqIQ-ovnxcgwGekOfMZjzHDc51-rZ-uxQkMXMfnWd0IxATMpDKmR9pgt7YOjAW9RI-ElxcO-oWbDM1GimA4zhkInn-k4gQxRZMQvzz9QjnkEybIvwI7My63jI693qiKAi_X-22tDcrbTiDa4QWRy1AggjwcU5Ddm_Yx5C7wfIbadhIgQAALeQKNFxhmz1f1a0cN1DQ-SspVf6wbJ6Y9EM13UQfgD06U0u-U7qvHZPgsWsnw==', start_index=10334)
Annotation(end_index=10625, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtFLDeAAGAbVjnWR8C8Hc2ptwxjOQc_xaRGmRxpAyeWCRIrKNYjMyjZ0gPC5ycXXyNEx0v2IFXsQ0OPch3q_appA271Kyw_y8bQosYNh1V1qGfBNKEJlOLcLnfMpyK8MfrbofYlHxv0Px2EHTp1GNljoaFgW3I', start_index=10613)
Annotation(end_index=10625, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMPcxQkCGNwKXZnc_8dXXZDnXEBINsy2w4SXqsYViCI43YgSQX1vpIjv09wo3NLDFkUEQ1xiOu15XfbUEMaxGX8BXQMHtzDsBW_Z7dzywErANzxPQyyYysrH4vhHlWlg==', start_index=10613)
Annotation(end_index=10870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVS1gXv7zlHkM1oY8JgcX_w5LQtnnljU64F53NON1NdWNDyhaG7UxnekojbuRV5opjx6WhOlOcIpK0uehPvtZUc1YhlwMWPZTFhG7c3GhurdvRFrq7_TyJZh18gcbMEz8Lqu9D802wkG68FRqfSg==', start_index=10857)
Annotation(end_index=10870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtFLDeAAGAbVjnWR8C8Hc2ptwxjOQc_xaRGmRxpAyeWCRIrKNYjMyjZ0gPC5ycXXyNEx0v2IFXsQ0OPch3q_appA271Kyw_y8bQosYNh1V1qGfBNKEJlOLcLnfMpyK8MfrbofYlHxv0Px2EHTp1GNljoaFgW3I', start_index=10857)
Annotation(end_index=11421, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtFLDeAAGAbVjnWR8C8Hc2ptwxjOQc_xaRGmRxpAyeWCRIrKNYjMyjZ0gPC5ycXXyNEx0v2IFXsQ0OPch3q_appA271Kyw_y8bQosYNh1V1qGfBNKEJlOLcLnfMpyK8MfrbofYlHxv0Px2EHTp1GNljoaFgW3I', start_index=11406)
Annotation(end_index=11421, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvK30NZ-og9ft_pjeZPw-8a-XJKB4SLDqV-oVMUcfPHW8FDJn-1Whm4EI9CDtOSKi68LQ3F-2NaAre3Vzq_DLIOI2pvGD-ml5PIl1XQ0Ous9k-5qwyE8thPyndsBpYv-SNLmrvslFSviRnW3H0HCP0Bs1WIIlRaeg4kUdG3A==', start_index=11406)
Annotation(end_index=11421, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDU4VC3PjqUlSeETMOGQNBLgrO-aDnqlYYaB6x5RkmDhyCXBekmhn819SMxkk85JS4jiz9JngxKKtfI58a64H-UGezvL9CR6d7_WurnfQHvqc27Dt2ZZ5X3HVq2rlK', start_index=11406)
Annotation(end_index=11741, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVTlQ2PnCqMMQV12hcylTsmpM9fn2ojCz6Sr5cImBa0nAjSzAvWeKbgkNilsleY2Ox45BCWL9RvcQSKIBHp3tR5T16ClZyqP9QYx3sqQ3VCaiKIOAKEouJM0trEHi4MD7SS4liHLTpdNbWc1S-V9uP_pUiWuTVr3cQqbWiiAzD61ua', start_index=11728)
Annotation(end_index=11741, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtFLDeAAGAbVjnWR8C8Hc2ptwxjOQc_xaRGmRxpAyeWCRIrKNYjMyjZ0gPC5ycXXyNEx0v2IFXsQ0OPch3q_appA271Kyw_y8bQosYNh1V1qGfBNKEJlOLcLnfMpyK8MfrbofYlHxv0Px2EHTp1GNljoaFgW3I', start_index=11728)
Annotation(end_index=12270, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVTlQ2PnCqMMQV12hcylTsmpM9fn2ojCz6Sr5cImBa0nAjSzAvWeKbgkNilsleY2Ox45BCWL9RvcQSKIBHp3tR5T16ClZyqP9QYx3sqQ3VCaiKIOAKEouJM0trEHi4MD7SS4liHLTpdNbWc1S-V9uP_pUiWuTVr3cQqbWiiAzD61ua', start_index=12254)
Annotation(end_index=12270, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtFLDeAAGAbVjnWR8C8Hc2ptwxjOQc_xaRGmRxpAyeWCRIrKNYjMyjZ0gPC5ycXXyNEx0v2IFXsQ0OPch3q_appA271Kyw_y8bQosYNh1V1qGfBNKEJlOLcLnfMpyK8MfrbofYlHxv0Px2EHTp1GNljoaFgW3I', start_index=12254)
Annotation(end_index=12270, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvK30NZ-og9ft_pjeZPw-8a-XJKB4SLDqV-oVMUcfPHW8FDJn-1Whm4EI9CDtOSKi68LQ3F-2NaAre3Vzq_DLIOI2pvGD-ml5PIl1XQ0Ous9k-5qwyE8thPyndsBpYv-SNLmrvslFSviRnW3H0HCP0Bs1WIIlRaeg4kUdG3A==', start_index=12254)
Annotation(end_index=12617, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvK30NZ-og9ft_pjeZPw-8a-XJKB4SLDqV-oVMUcfPHW8FDJn-1Whm4EI9CDtOSKi68LQ3F-2NaAre3Vzq_DLIOI2pvGD-ml5PIl1XQ0Ous9k-5qwyE8thPyndsBpYv-SNLmrvslFSviRnW3H0HCP0Bs1WIIlRaeg4kUdG3A==', start_index=12604)
Annotation(end_index=12617, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNS7b1PeVNK0sVcNdgcQv7Qg16ZIy8j0MRqmGulWOGDHo-wvR1MPiUntV45re8s9uZKUq9wuDsqsHjIE6HMqF6tl07018HbYIuEErCeGccWGIsua0o5LZxHB3taPh0JTCyxkfHcV0VR2fsVC7AqjoqiYto98ryn45Eng36rNS14QepqJLcnOCVQYhV5s20BKAqLKTwGDhDe4v-JQ==', start_index=12604)
Annotation(end_index=13473, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiSMDD4_jmGJpGAt826QU1_9ZTnu2IAG6mILOyQaXfzj_1as_NAEAaBIRBrD0P6vbz2bxv5Dx7N0Upc1HL8q72wnGdXhq7jAQNqIQ-ovnxcgwGekOfMZjzHDc51-rZ-uxQkMXMfnWd0IxATMpDKmR9pgt7YOjAW9RI-ElxcO-oWbDM1GimA4zhkInn-k4gQxRZMQvzz9QjnkEybIvwI7My63jI693qiKAi_X-22tDcrbTiDa4QWRy1AggjwcU5Ddm_Yx5C7wfIbadhIgQAALeQKNFxhmz1f1a0cN1DQ-SspVf6wbJ6Y9EM13UQfgD06U0u-U7qvHZPgsWsnw==', start_index=13461)
Annotation(end_index=13473, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0H2DcftiniAa1Z5bR_4-frjZGo4G94C5Q60hCsj4L5yT6rMCZMYrsGe-EsgQ219AIWdPmlk9NJhj0cla40Dez9HKfsdMz5-QTgkOlgJ13-civc1KdZT074WNtmHB6vV1YNHDWsilzMAtqBdl8deZXi7GwpXjEun-dZt-zT0s=', start_index=13461)
Annotation(end_index=13700, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNv8pram2IYlWnnTE9vwiVc9Mdo35H7vfbZroVDHTeVRjYN97zbUuHHNE8LQQcCd74LUb-lwtbDOEfAGaXiiJP-I4p73g_WXWrG_x_hUIfkR2x-n4JwONQGEw8nW2FmclnfMAHPOWJ-IshTCgFlLFIbGZ7OLUjQHuV91nKEiqGrOL-3dwKXOVsD2eYtsUctD5K_nVgB-wFhw==', start_index=13690)
Annotation(end_index=14037, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEazr9pdvsp_pr3omjbl9JRuTDVkwS96MzEit6EN-P9sUy1wqjveHgbDIkLeE45vtssjhmSZ4IcVWn7silvbaYuHiEsOGsRBprXwB3vR8iiMePeuLSSEnX0ijb8VLkzg9j2sn0ogFZGmO1-ygNVIQ_FCZzYVMly0rkqPXVftOQbcFaij7Q66kw_kHlxjl8nX4wLJza4LPFWgdeqps4MpyNCFSywdSjukUDihqY3C-EeKgtdeOL6I1gqR7qJZ1s9CK6GpxEvldwLlt4bLOn64hfZNwhWoHEkxxeRio8=', start_index=14027)
Annotation(end_index=14277, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBwv_NnC7a5mFl0g_KLLTeaBXikHxXmg6Wheu5ydc00nRpi1excRPhZOaYuYWr7jlpdqiuJIOz4uDIS_IGj08bi-cxB6IaH_srTuPl9v6gq4xK-HBzLlk4xpRDmcyvQpgr-2xAXOs5kg0d6TkYP3_gGuIj7MEKtKyB2e9v20sRYr0lw1I9SbcvV87mDdoBq0M4-ny0QWPRlnqKbryxTLL61jc5xijAOqX36ViCo5lpkIpEpqtoTw8p-MQiLSsodCLX5ikXWGczc7qnBfCbq9FTK8zzCBzATp4_fwV9ehEilSv1J3cvWqa36in7ZQDMpNEoF27RSs8GfAmaXk6nHZ1X43URXEZGBu66kw==', start_index=14263)
Annotation(end_index=14277, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcsNcXy24yYBf59EYwA3RayVWWt4uYc2igrdVKu03KoFPWm-_2VNYmSWONlGp7wS8JgY2z_pxMmH8uJMjWSrpqd4hYPTutDM0hFlTuIgfA95MjIwzKr0IkbYhl3N50HwCA2p0ROka4Y563gn5y8c0pPZotKdFVmSgO-EOg3UvVMTzoS9hYWEtlWQrMBV2ww_xN2THx0xIruMrw7ZeJBOjrTgJ1eBmb', start_index=14263)
Annotation(end_index=14828, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEG2kcg1dvhiOgddFhru8clZlktmt6FTmg0jZEL55JHEtH50gZS20SHHgendgR9Vetj4MbGbD5IAR3r_HyTE8AyAKA6dH_jNJxZIkNk9_e5qCRpXX_6l1cwefQ1i4_PLg==', start_index=14819)
Annotation(end_index=15755, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiSMDD4_jmGJpGAt826QU1_9ZTnu2IAG6mILOyQaXfzj_1as_NAEAaBIRBrD0P6vbz2bxv5Dx7N0Upc1HL8q72wnGdXhq7jAQNqIQ-ovnxcgwGekOfMZjzHDc51-rZ-uxQkMXMfnWd0IxATMpDKmR9pgt7YOjAW9RI-ElxcO-oWbDM1GimA4zhkInn-k4gQxRZMQvzz9QjnkEybIvwI7My63jI693qiKAi_X-22tDcrbTiDa4QWRy1AggjwcU5Ddm_Yx5C7wfIbadhIgQAALeQKNFxhmz1f1a0cN1DQ-SspVf6wbJ6Y9EM13UQfgD06U0u-U7qvHZPgsWsnw==', start_index=15746)
Annotation(end_index=16278, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVTlQ2PnCqMMQV12hcylTsmpM9fn2ojCz6Sr5cImBa0nAjSzAvWeKbgkNilsleY2Ox45BCWL9RvcQSKIBHp3tR5T16ClZyqP9QYx3sqQ3VCaiKIOAKEouJM0trEHi4MD7SS4liHLTpdNbWc1S-V9uP_pUiWuTVr3cQqbWiiAzD61ua', start_index=16262)
Annotation(end_index=16278, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtFLDeAAGAbVjnWR8C8Hc2ptwxjOQc_xaRGmRxpAyeWCRIrKNYjMyjZ0gPC5ycXXyNEx0v2IFXsQ0OPch3q_appA271Kyw_y8bQosYNh1V1qGfBNKEJlOLcLnfMpyK8MfrbofYlHxv0Px2EHTp1GNljoaFgW3I', start_index=16262)
Annotation(end_index=16278, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvK30NZ-og9ft_pjeZPw-8a-XJKB4SLDqV-oVMUcfPHW8FDJn-1Whm4EI9CDtOSKi68LQ3F-2NaAre3Vzq_DLIOI2pvGD-ml5PIl1XQ0Ous9k-5qwyE8thPyndsBpYv-SNLmrvslFSviRnW3H0HCP0Bs1WIIlRaeg4kUdG3A==', start_index=16262)
Annotation(end_index=18032, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEG2kcg1dvhiOgddFhru8clZlktmt6FTmg0jZEL55JHEtH50gZS20SHHgendgR9Vetj4MbGbD5IAR3r_HyTE8AyAKA6dH_jNJxZIkNk9_e5qCRpXX_6l1cwefQ1i4_PLg==', start_index=18023)
Annotation(end_index=18203, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiSMDD4_jmGJpGAt826QU1_9ZTnu2IAG6mILOyQaXfzj_1as_NAEAaBIRBrD0P6vbz2bxv5Dx7N0Upc1HL8q72wnGdXhq7jAQNqIQ-ovnxcgwGekOfMZjzHDc51-rZ-uxQkMXMfnWd0IxATMpDKmR9pgt7YOjAW9RI-ElxcO-oWbDM1GimA4zhkInn-k4gQxRZMQvzz9QjnkEybIvwI7My63jI693qiKAi_X-22tDcrbTiDa4QWRy1AggjwcU5Ddm_Yx5C7wfIbadhIgQAALeQKNFxhmz1f1a0cN1DQ-SspVf6wbJ6Y9EM13UQfgD06U0u-U7qvHZPgsWsnw==', start_index=18191)
Annotation(end_index=18203, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0H2DcftiniAa1Z5bR_4-frjZGo4G94C5Q60hCsj4L5yT6rMCZMYrsGe-EsgQ219AIWdPmlk9NJhj0cla40Dez9HKfsdMz5-QTgkOlgJ13-civc1KdZT074WNtmHB6vV1YNHDWsilzMAtqBdl8deZXi7GwpXjEun-dZt-zT0s=', start_index=18191)
Annotation(end_index=18372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVTlQ2PnCqMMQV12hcylTsmpM9fn2ojCz6Sr5cImBa0nAjSzAvWeKbgkNilsleY2Ox45BCWL9RvcQSKIBHp3tR5T16ClZyqP9QYx3sqQ3VCaiKIOAKEouJM0trEHi4MD7SS4liHLTpdNbWc1S-V9uP_pUiWuTVr3cQqbWiiAzD61ua', start_index=18356)
Annotation(end_index=18372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtFLDeAAGAbVjnWR8C8Hc2ptwxjOQc_xaRGmRxpAyeWCRIrKNYjMyjZ0gPC5ycXXyNEx0v2IFXsQ0OPch3q_appA271Kyw_y8bQosYNh1V1qGfBNKEJlOLcLnfMpyK8MfrbofYlHxv0Px2EHTp1GNljoaFgW3I', start_index=18356)
Annotation(end_index=18372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvK30NZ-og9ft_pjeZPw-8a-XJKB4SLDqV-oVMUcfPHW8FDJn-1Whm4EI9CDtOSKi68LQ3F-2NaAre3Vzq_DLIOI2pvGD-ml5PIl1XQ0Ous9k-5qwyE8thPyndsBpYv-SNLmrvslFSviRnW3H0HCP0Bs1WIIlRaeg4kUdG3A==', start_index=18356)
Annotation(end_index=18501, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEv2vpD2Gfq8GFFGfFt9dXI3kC8T-k_EIjgoJ95dO8hT7LifQnvylDumtx7TbmSRHG5eqcrI8mSeI6gFmb0nf73Ub62UbM4xtzX0jxIpEgGekPvd7i9L_uAkPI3Bg0gpyY2PBVZ5AEkAw8HCcbJ6cWlWufq19VNqXOv3pu5OznbZffiyVUmFYz6ljLsV4yDMDYeT8oS-LThtvlW14vtajK5JSaRBXvp_ieOR27QoMAzuasMCQSN0HDhd1sZVDU=', start_index=18489)
Annotation(end_index=18501, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMPcxQkCGNwKXZnc_8dXXZDnXEBINsy2w4SXqsYViCI43YgSQX1vpIjv09wo3NLDFkUEQ1xiOu15XfbUEMaxGX8BXQMHtzDsBW_Z7dzywErANzxPQyyYysrH4vhHlWlg==', start_index=18489)
Annotation(end_index=18630, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVf6IT9pHOVrUwohtZ3K9gB0lvvnMi4HeasqKGKk3rVcDymv4ekC7rvlb_W2SeYVVn5Osxu0B3NE12fJt9M812zrZBmC5qxyqRztU9u2R6QsTqUNTL0GiyH-I1qFtfwT3AnINKgWMPo7kPoCTgxu6ke8P1tCSfjGTL232LFFLtT3sDK3UFdyyY8gsX5ZzGSC3LjoPhsWSrsu0M-WebNaWg30S_E6QMaa8Cnct9dT9eBVkMEd8_', start_index=18617)
Annotation(end_index=18630, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcGaDS_No2zGO4KKiTxKfJySBPeL_vDm53m5y8TzdNZFuYEu8QO9JuAGMgIFL7k5ukOV0M6cU-LfORknkuyjENmNFmCVBiF4Ty7aALZXApIM8T8FhiIzPI2UkWPdQy8uaFgBVDxFabOMiXcZg-Y1LRutRqrCE0R0xOS-jEas1Ir2akhR0kxCfcbV0bvdSM_AmUzVUm44wbX0lkCA==', start_index=18617)
Annotation(end_index=18762, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOlKWekU3Fud59tFmttBRgpy33cPlmsbWd_akuprjPuM7cHbhEnWXhkco9soLFf2KcBTI9qTfx1xZrAcKEvJeWIRHsbumtTYO2Q-opm2h0z3bsvCO8FNqDmP-uie0q2sCB2sTYvDBF3IO1_uS-H7Te_fHChrab7qP0g8JzltUHTGCcYHCOqClYkfs86hDtfkuht39sMNkT0tGqu8i_5p80-rK6A92sfMntrdiHe9VC7gX6UA==', start_index=18744)
Annotation(end_index=18762, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGt8bZ3YnnJy1p0L7Q98FDniyVaE4V7IZ3C5uINKgS8q-lojWCyYo8ntRj9Aoc3zhLU0m5py8eodtghzzMOkAzoc5ER6sokgjn03AFWQ_BTT5-nOzP4fNoa-YItGDZ0-ynHpg5Asfh5w8PZWjECKASzD9zUamgdvu93_ZZCna7SfFV2lzrMuSbyEmCZHqYUpCVUUxPlHaGyvVbBl5tLaalTHdVz8SOYjTCrZtkN4ys=', start_index=18744)
Annotation(end_index=18762, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJOFO_7eXi77FtcA4eW_JO8MBUK77KC2HTjyQ-EoAk64KgI50GgPswX5Qp7STk1If7dCJ0bYWS8_pNfXAFvSbGbPCkFup09RvvHaekCaBr-5Gs6A3jq1SCZi3fpfMNp3EwvZ4QCWyLavppxyyjnxbyqUpnrcvoZjnimWllSWuqfHoqFsWOlKU8Kzv-ZBj_0kWE', start_index=18744)
Annotation(end_index=18888, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6tPnmXK1M0_Rhx30MHDIt7OF3epv-lyRdobZ_Ahu3Ee9KXnfpllEnEq_y1-VDguqoawHZGI1ZxnndIl3XI7Ii47mqvvH5tXzIRkFdFNXsga9X9-uYBYvEClKOC9Q=', start_index=18870)
Annotation(end_index=18888, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEazr9pdvsp_pr3omjbl9JRuTDVkwS96MzEit6EN-P9sUy1wqjveHgbDIkLeE45vtssjhmSZ4IcVWn7silvbaYuHiEsOGsRBprXwB3vR8iiMePeuLSSEnX0ijb8VLkzg9j2sn0ogFZGmO1-ygNVIQ_FCZzYVMly0rkqPXVftOQbcFaij7Q66kw_kHlxjl8nX4wLJza4LPFWgdeqps4MpyNCFSywdSjukUDihqY3C-EeKgtdeOL6I1gqR7qJZ1s9CK6GpxEvldwLlt4bLOn64hfZNwhWoHEkxxeRio8=', start_index=18870)
Annotation(end_index=18888, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMTsmTOZE_mqtw8WCfI_aSZ0RyCNDOJvZzkDvFiHoJ4z0BtE0uMj92_yT1vYZ1H6Sd9mriyNrqoR8qbaCowi6-uZl-MiTsjmc1cy2AFQ84TFXgO0tin76Ih-ZOjDMo_h4TBnUuppI3GiBWVzlWaPV4nPylc6LlZQ-9CcmrD07x723WCRZ3nxAEZNJqTtDhpb0_S6iJJvwDuX6Wn7Q3EN0yzta5uEhVSgOOXSar', start_index=18870)
Annotation(end_index=19005, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKiniNnOILA3Rmg-W8SIoBT2HEBmwtgGo3lpBDl-CygCUl1W1SVMYpeStbqZl97ZWBDV7S8QpR79QQU1xQnrpIFyNOq_oRhAyhuFs0TkJDt5ntldXdQCqbOofsT3fIcYFkzn8=', start_index=18991)
Annotation(end_index=19005, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNS7b1PeVNK0sVcNdgcQv7Qg16ZIy8j0MRqmGulWOGDHo-wvR1MPiUntV45re8s9uZKUq9wuDsqsHjIE6HMqF6tl07018HbYIuEErCeGccWGIsua0o5LZxHB3taPh0JTCyxkfHcV0VR2fsVC7AqjoqiYto98ryn45Eng36rNS14QepqJLcnOCVQYhV5s20BKAqLKTwGDhDe4v-JQ==', start_index=18991)
Annotation(end_index=19120, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtAtaVxF9AEY0_zPNcrXk4ew19zJwdJL6m7OMz_kEhxqMqWJd0mAyUZs_lPuuJJ4Yjq1r8yPow_tbJUo8dcHcgwlRNnMhl4hSO6_0QsttHOq45r5iOPK1q9u3Mnew_Lz3z', start_index=19110)
Annotation(end_index=19240, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDU4VC3PjqUlSeETMOGQNBLgrO-aDnqlYYaB6x5RkmDhyCXBekmhn819SMxkk85JS4jiz9JngxKKtfI58a64H-UGezvL9CR6d7_WurnfQHvqc27Dt2ZZ5X3HVq2rlK', start_index=19231)

## Sources
