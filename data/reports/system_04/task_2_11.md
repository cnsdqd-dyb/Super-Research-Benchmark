# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 613de949 | **Time:** 338.54s | **Cost:** $1.84221
--------------------------------------------------------------------------------

# Design Approaches for Balancing On-Resistance and Reliability in GaN Power Devices: Managing Doping Gradients and Interface Trap Synergies

**Key Points**
*   **Step-Graded Channel Doping (SGCD)** in vertical GaN Trench MOSFETs is the primary design approach identified to balance on-resistance ($R_{ON}$) and reliability. This technique decouples the trade-off between threshold voltage ($V_{th}$) and channel resistance by spatially varying the doping concentration, thereby maintaining a high barrier against false turn-on while minimizing scattering in the conduction path.
*   **Synergistic Effects** arise from the interaction between the electric field profile (determined by doping gradients) and the interface trap state density ($D_{it}$). High electric fields near the dielectric interface accelerate carrier trapping, leading to dynamic $R_{ON}$ degradation and threshold instability.
*   **Thick Bottom Dielectric (TBD)** architectures are frequently integrated with optimized doping profiles to shield the gate oxide from high drain potentials, reducing the electric field stress on interface traps and suppressing leakage currents.
*   **Polarization Doping** utilizing graded AlGaN or InGaN layers offers an alternative method to generate mobile carriers without ionized impurity scattering, effectively lowering $R_{ON}$ while managing the electric field distribution to mitigate trap-assisted degradation.

## 1. Introduction

Gallium Nitride (GaN) has established itself as a cornerstone material for next-generation power electronics, offering superior breakdown fields, saturation velocities, and electron mobilities compared to Silicon (Si) and Silicon Carbide (SiC) [cite: 1, 2]. However, the commercial maturation of GaN power devices faces a critical optimization challenge: the trade-off between static performance metrics, specifically on-state resistance ($R_{ON}$), and long-term reliability, characterized by threshold voltage ($V_{th}$) stability and dynamic $R_{ON}$ degradation [cite: 2, 3].

This report addresses the specific design approaches required to balance these competing factors, with a particular focus on the **synergistic effects** of doping concentration gradients and interface trap state density ($D_{it}$). In GaN devices, these two factors do not operate in isolation. The doping profile dictates the electric field distribution, which in turn determines the occupancy probability of interface traps. Conversely, charged traps distort the local electric field, altering the effective doping efficiency and carrier mobility [cite: 4, 5].

The most prominent design solution emerging from recent research to address this specific intersection of physics is the **Step-Graded Channel Doping (SGCD)** technique applied to vertical GaN Trench MOSFETs [cite: 6, 7, 8]. This approach, alongside complementary strategies such as polarization doping and dielectric engineering, forms the basis of this analysis.

## 2. The Physics of Synergistic Effects in GaN Devices

To understand the efficacy of graded doping designs, one must first characterize the deleterious synergy between doping profiles and interface traps.

### 2.1. Interaction of Electric Fields and Interface Traps
In Metal-Oxide-Semiconductor (MOS) structures, the interface between the GaN semiconductor and the gate dielectric (typically $Al_2O_3$ or $SiO_2$) is a critical site for defects. Interface traps ($D_{it}$) are energy states located within the GaN bandgap at the dielectric interface.
*   **Acceptor-like traps:** Negatively charged when filled with electrons; they raise the conduction band, increasing $V_{th}$ and scattering carriers, which increases $R_{ON}$ [cite: 4].
*   **Donor-like traps:** Positively charged when empty; they can screen electric fields but also contribute to leakage paths [cite: 4, 9].

The "synergistic effect" refers to the mechanism where the electric field—shaped by the doping concentration—accelerates carriers, increasing their probability of tunneling into or being captured by these interface states. High doping concentrations, typically required to ensure a normally-off operation (positive $V_{th}$), induce strong transverse electric fields. These fields force electrons closer to the rough dielectric interface, enhancing scattering and trapping rates [cite: 4, 10].

### 2.2. Dynamic On-Resistance and Current Collapse
Dynamic $R_{ON}$ degradation, often termed "current collapse," is a manifestation of this synergy. When a device is in the OFF-state under high drain bias, electrons are injected into deep traps in the buffer or at the interface. When the device switches to the ON-state, these trapped electrons cannot emit instantaneously. They act as a "virtual gate," depleting the channel and drastically increasing $R_{ON}$ compared to its static DC value [cite: 3, 11].

Research indicates that the distribution of the electric field, controlled by the doping gradient, determines the spatial location of this trapping. A uniform doping profile often results in peak fields at the gate edge—precisely where trap density is often highest due to processing damage—leading to severe reliability issues [cite: 11, 12].

## 3. Primary Design Approach: Step-Graded Channel Doping (SGCD)

The most direct answer to the query regarding a design approach that balances these factors is the **Step-Graded Channel Doping (SGCD)**, particularly in the context of vertical GaN Trench MOSFETs. This architecture has been rigorously investigated to resolve the conflict between achieving a high $V_{th}$ (for safety/reliability) and a low $R_{ON}$ (for efficiency).

### 3.1. The Trade-off in Uniform Doping
In a conventional vertical Trench MOSFET with a uniform channel doping:
*   **High Doping:** Increases the energy barrier, successfully pushing $V_{th}$ higher (desirable for noise immunity). However, it severely degrades channel mobility due to ionized impurity scattering and increases channel resistance, leading to high $R_{ON}$ [cite: 13].
*   **Low Doping:** Reduces scattering and lowers $R_{ON}$, but results in a dangerously low $V_{th}$ (often normally-on or quasi-normally-off), making the device susceptible to false turn-on and increasing leakage [cite: 8].

### 3.2. Mechanism of Step-Graded Channel Doping
The SGCD approach introduces a non-uniform doping profile within the channel region. As detailed by Zhu et al., this typically involves a p-GaN body with varying Mg concentration levels [cite: 6, 7, 8].
*   **Structure:** The channel is composed of layers with different doping concentrations. For example, a highly doped layer is placed near the source or specific regions to pin the threshold voltage, while a lower doped layer extends through the rest of the channel.
*   **Balancing Mechanism:** The highly doped section ensures a sufficient barrier height to maintain a high $V_{th}$. The lower doped section comprises the bulk of the channel length, reducing the average resistance and scattering events.
*   **Result:** This creates a "best of both worlds" scenario. Experimental results have demonstrated that SGCD achieves an improved trade-off figure-of-merit (FOM) compared to uniform doping, simultaneously securing high $I_{ON}$, low $R_{ON}$, and adequate $V_{th}$ [cite: 7, 14, 15].

### 3.3. Impact on Interface Trap Synergy
The graded doping profile modifies the transverse electric field distribution along the channel. By avoiding a uniformly high doping concentration, the peak electric field at the oxide interface is attenuated in the critical transport regions. This reduction in field strength lowers the energy of carriers interacting with the interface, thereby reducing the probability of hot-carrier injection into interface traps [cite: 4, 10]. Consequently, the device exhibits improved reliability against bias stress and lower dynamic $R_{ON}$ degradation.

## 4. Complementary Design Strategies

While SGCD addresses the channel physics, holistic device reliability requires managing the electric field in the drift and termination regions to further mitigate trap-related effects.

### 4.1. Thick Bottom Dielectric (TBD)
In vertical trench devices, the bottom of the trench is a high-stress point where the electric field can cause premature breakdown and significant charge trapping.
*   **Design:** The Thick Bottom Dielectric (TBD) approach involves increasing the oxide thickness at the bottom of the trench while maintaining a thin oxide along the channel sidewalls [cite: 11, 12, 16].
*   **Synergy Mitigation:** The TBD decouples the gate from the high drain potential. This shielding effect reduces the electric field crowding at the trench corners. Since high fields drive carriers into traps, reducing the field at this vulnerable location directly suppresses the trapping rate and leakage current.
*   **Reliability Outcome:** Devices with TBD show enhanced stability in dynamic $R_{ON}$ and reduced $V_{th}$ shift under stress, as the "hot spot" for trap interaction is neutralized [cite: 12].

### 4.2. Polarization Doping (Graded Heterostructures)
An alternative to impurity doping (like Mg or Si) is **polarization doping**, which leverages the spontaneous and piezoelectric polarization properties of III-Nitride materials.
*   **Design:** By grading the composition of an alloy (e.g., grading Al concentration in AlGaN or In concentration in InGaN) over a spatial distance, a fixed volume charge is created [cite: 17].
*   **Advantage:** This generates free carriers (electrons or holes) without introducing ionized impurity scatterers. This directly addresses the $R_{ON}$ component of the query by maximizing mobility.
*   **Reliability:** Polarization-doped layers can be designed to smooth out electric field peaks. A graded AlGaN layer can distribute the breakdown voltage drop over a larger distance compared to a distinct interface, reducing the local field intensity that activates traps [cite: 17, 18].

### 4.3. Ion Implantation for Field Modulation
Ion implantation (using Si, F, or N ions) is utilized to precisely engineer the doping profile at termination regions and contact interfaces.
*   **Contact Optimization:** High-dose Si implantation creates $n^+$ regions that facilitate ohmic contacts, lowering $R_{ON}$ [cite: 19].
*   **Trap Management:** Fluorine (F) ion implantation is known to introduce negative fixed charges that can modulate $V_{th}$ and suppress leakage. However, it must be carefully annealed to repair lattice damage, which otherwise acts as a source of bulk traps [cite: 19].
*   **Edge Termination:** Implantation is used to create Junction Termination Extensions (JTE) or guard rings. These structures spread the electric field at the device periphery, preventing edge-concentrated breakdown and reducing the interaction of carriers with surface states [cite: 19].

## 5. Interface Trap Characterization and Mitigation

The reliability of any doping-engineered device is ultimately limited by the quality of the dielectric interface. The density of interface traps ($D_{it}$) must be minimized to allow the doping gradients to function as designed.

### 5.1. Impact of $D_{it}$ on Device Parameters
TCAD simulations and experimental data confirm that $D_{it}$ has a profound impact on device characteristics:
*   **Subthreshold Swing (SS):** High $D_{it}$ degrades SS, making the switch less efficient and increasing off-state leakage [cite: 4].
*   **Threshold Voltage Instability:** Under positive bias stress (PBTI), electrons are trapped in border traps or interface states, causing a positive $V_{th}$ shift. This shift is exacerbated if the doping profile places the electron wavefunction centroid too close to the interface [cite: 5, 11].
*   **Leakage:** Trap-assisted tunneling (TAT) through interface states is a dominant leakage mechanism, particularly in reverse bias [cite: 20].

### 5.2. Mitigation Techniques
*   **Dielectric Choice:** High-k dielectrics like $Al_2O_3$ are standard, but their interface with GaN often requires interlayers or specific treatments.
*   **Passivation:** SiN passivation is critical for lateral devices to satisfy surface states. In vertical devices, the quality of the trench sidewall etch and subsequent passivation determines the $D_{it}$ [cite: 21].
*   **Annealing:** Post-metallization annealing and specific gas ambients (e.g., forming gas) are used to passivate dangling bonds and reduce $D_{it}$, which is essential for stabilizing the benefits of graded doping [cite: 22].

## 6. Reliability Assessment: Dynamic Stress and Radiation

The validation of these design approaches requires rigorous reliability testing that accounts for the synergistic nature of the stresses.

### 6.1. Dynamic $R_{ON}$ Testing
Static DC tests are insufficient for GaN devices. Dynamic testing involves pulsing the device between high-voltage OFF states and conducting ON states.
*   **Observation:** Devices with unoptimized doping profiles show significant $R_{ON}$ spikes immediately after switching.
*   **Validation of SGCD:** Step-graded devices demonstrate faster recovery and lower dynamic $R_{ON}$ because the graded profile prevents the deep depletion of the channel caused by localized trapping [cite: 3, 11].

### 6.2. Radiation and Environmental Synergy
In extreme environments, GaN devices face Total Ionizing Dose (TID) and Single Event Effects (SEE).
*   **Synergy:** TID generates electron-hole pairs in the oxide, leading to trapped charge accumulation. This trapped charge alters the internal electric field, which can lower the threshold for Single Event Gate Rupture (SEGR) during a heavy ion strike [cite: 23, 24].
*   **Design Implication:** A graded doping profile that relaxes the peak electric field in the oxide improves radiation hardness by reducing the "pre-stress" field that sums with the radiation-induced field [cite: 25, 26].

## 7. Conclusion

To balance on-resistance and reliability in GaN power devices amidst the synergistic effects of doping gradients and interface traps, the **Step-Graded Channel Doping (SGCD)** architecture stands out as the most effective design approach. By spatially decoupling the requirements for threshold voltage (high doping barrier) and carrier transport (low doping resistance), SGCD minimizes the trade-offs inherent in uniform doping.

This approach is most effective when combined with:
1.  **Thick Bottom Dielectrics (TBD)** to shield trench corners from high fields.
2.  **Low-$D_{it}$ Interface Engineering** via optimized etching and passivation to minimize the trap density available for interaction.
3.  **Polarization Doping** techniques where applicable to further reduce impurity scattering.

The integration of these strategies ensures that the electric field is manipulated to avoid trap-rich regions, thereby suppressing the synergistic mechanisms that lead to dynamic $R_{ON}$ degradation and device failure.

## 8. Detailed Literature Review and Source Analysis

### 8.1. Vertical GaN Trench MOSFETs and Step-Graded Doping
The work by **R. Zhu et al.** is central to this topic. Their research explicitly proposes "step-graded channel doping" to solve the $R_{ON}$ vs. $V_{th}$ trade-off [cite: 6, 7, 8, 13, 15].
*   *Problem:* Uniformly high channel doping increases $V_{th}$ (good) but increases $R_{ON}$ (bad). Uniformly low doping decreases $R_{ON}$ (good) but lowers $V_{th}$ and increases leakage (bad).
*   *Solution:* A step-graded profile provides a localized high barrier for $V_{th}$ control and a broader low-doped region for current conduction.
*   *Result:* Improved Figure of Merit (FOM) and better trade-off characteristics.

### 8.2. Interface Trap Density ($D_{it}$) and Device Physics
*   **Ichikawa et al.** and **Meneghini et al.** provide foundational understanding of how traps affect reliability [cite: 1, 27].
*   **Synergy:** The electric field drives carriers into traps. If the doping gradient is too steep or creates field crowding near the interface, trapping increases. Conversely, trapped charges modify the field, potentially extending the depletion region and increasing resistance (current collapse) [cite: 3, 4].
*   **Modeling:** TCAD simulations incorporating Gaussian distributions of donor/acceptor traps at the interface are essential for predicting these effects [cite: 4, 9, 21].

### 8.3. Advanced Doping and Structural Techniques
*   **Polarization Doping:** Utilizing the graded composition of AlGaN or InGaN to induce bulk charges is a powerful technique to achieve conductivity without the mobility penalty of impurity scattering [cite: 17].
*   **Ion Implantation:** Used for creating precise termination structures (like guard rings) that manage the lateral electric field, preventing edge breakdown and reducing surface trap interaction [cite: 19].
*   **Thick Bottom Dielectric:** Specifically addresses the reliability of the trench bottom, a critical failure point in vertical devices. By reducing the field here, the synergy between high drain voltage and bottom interface traps is broken [cite: 11, 12, 16].

### 8.4. Reliability under Extreme Conditions
*   **Radiation:** The synergistic effect of TID and SEE is a critical reliability consideration for aerospace applications. The accumulation of oxide trapped charge modifies the electric field, making the device more susceptible to catastrophic failure during switching or ion strikes [cite: 23, 24].
*   **Thermal Stress:** High temperatures exacerbate trapping and leakage. The mismatch in thermal expansion coefficients (e.g., GaN on Sapphire) can generate new defects, further degrading reliability [cite: 5].

## 9. Tables and Data Summary

### Table 1: Comparison of Doping Strategies in GaN Power Devices

| Doping Strategy | Primary Benefit | Impact on $R_{ON}$ | Impact on Reliability ($V_{th}$/Leakage) | Interaction with Interface Traps |
| :--- | :--- | :--- | :--- | :--- |
| **Uniform High Doping** | High $V_{th}$ (Safety) | High (Degraded Mobility) | Good Leakage Control | High field near interface increases trapping probability. |
| **Uniform Low Doping** | Low $R_{ON}$ (Efficiency) | Low (High Mobility) | Poor (Low $V_{th}$, High Leakage) | Lower field, but susceptible to punch-through. |
| **Step-Graded Doping** | Balanced Performance | **Optimized** (Low) | **High** (Stable $V_{th}$) | **Reduced** peak fields at interface minimize trapping. |
| **Polarization Doping** | High Mobility (No Impurities) | Very Low | Good (Field Engineering) | Graded layer distributes field, reducing local stress on traps. |

### Table 2: Key Reliability Mechanisms and Mitigation

| Mechanism | Driver | Synergistic Factor | Mitigation Design |
| :--- | :--- | :--- | :--- |
| **Dynamic $R_{ON}$** | Trapping of electrons in OFF-state | High E-field + High $D_{it}$ | Field Plates, Graded Doping, TBD |
| **$V_{th}$ Instability** | PBTI / NBTI Stress | Oxide Traps + Bias | High-quality Dielectric, Step-Graded Channel |
| **Gate Rupture (SEGR)** | Heavy Ion Strike | TID-induced Oxide Charge | Field relaxation via doping gradients |
| **Leakage Current** | Trap-Assisted Tunneling | High Field at Interface | Passivation, TBD, Source/Drain Spacers |

## 10. Final Remarks

The design of reliable, high-efficiency GaN power devices is no longer a matter of simple material selection but of complex structural engineering. The **Step-Graded Channel Doping** approach represents the state-of-the-art in resolving the fundamental conflicts of device physics. By acknowledging and engineering around the synergistic relationship between doping-induced electric fields and interface trap states, researchers and engineers can unlock the full potential of GaN technology for power electronics.

**Sources:**
1. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUhS_PR7hDHcJ1lKeE11PnVW3vdwsUYfQMBUKdEuk9nWSgA8bItOSyBUIT4q4htjnaPLJuF0XM6cBMQvMA7hDl2xVyAJXIjH6Qfvxi-D7RK-w3t2eVAq-akszvSRTY9g-0JplMtSE4oqFsJe7SxwaV85naGTZs6oz1oVICySYgysixaHMbMAweBVMDjcqpxiDaxgvyuBryDopwdVMtG-Nt)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWe4EAEgLXXgikvH0CXJUeX7aFJYNwAue0mxLIxbIuFZLuk38TDBHF2feVhClLy3oAlecrWezqPVw-Je11-dcWnJh53MnsYeqfkhK1vnqown4B_w-HRLbrXf7b7SnPqKkEb9T8lVOshuSGHGqCeORhdbSh9wik3AYLlsezBmOAPEjjUUuIrHxsWnC8toez6YccDAMME4-geMJr6lbaHlVjQ6Yy)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI6pQXKx09xGdKOFgqeTjoDAt5O8tFyO1c2dpq7hUoyx7jFJV6Nw9_R9g-44WkZJM3bw4-q_wCVzm0VNKYnKYOf1HSw9MERRMOf1EPaUyAF2SAte9gcRG1_Bh6x_mZP8HGYoa3MjnTl_xWrodE2YZU3XnODXr5Wq2m7tRy8KuXZXZMa8-mHdTo6O87KCJ6-N8BYC8kApMciXLoSw8UbMxaG0kW5wQ4YKEAk4q3wxVzO2LmG61XWRaTKwU9HgOE16iNFRgsSg==)
4. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSb0V_bDdKKhyLWKVHZ5DDEIixHGidoxIkTnGc_xxCj6wuP5jIHoFQ6vTbZ7eXQd2fck9Nfn7nFlk-tWBmnQOsazqjdIL5XJ7fkaAr3JwAl7eB2E9TvqMYgfbc5w==)
5. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgYcEEiD6WCBF77uNvMIji7Grl07vqVBdFYBenslUbk-bYcpaIEcdhHpcdpU_AcJzMDngjb5MJRkVTI_07bgareJ_uGPTNVyi7s-7dWc6jzj00aBrCE6DhORRDbTE=)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOOJ-776yPwqdu9aTWHf5PK6bkV93IkDmoXxrT6HEbPeuKAnWfkPTwlzNvVow209fUxszNhc6VKTe7ItlxovaSUPRAxGmGb8m4HVE__yXa4uk5Wg0OU3AI8-41rrpzh3Bv2y18CM0q6GP2VxCC-Pj8eHb9GOZHBdKnPr0He8HUhMJVE1pduOG2TzXsZk1OXl0D-RE3djsgb8-tdL5Ol_cnET1dhjzave0z1LuXVIEvo5ggb-nDHgR_CdBsfhTeo45wzHZBqaIKRuJgkyf2E_RNilAa8x3laWjVhPfXPqhWsVKtMc_3Q2ihqa_gOfSDXJxGrA==)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGktw0TgY5HmmcPCFkWakjy7syHi5Psst6GtKcSky7B8uK1nqDWYMRwNXH-z88VMIaDiOWrVwoK7FzXx7CHLddyXDp4pj7ZWr7aAuSvpYkpe-EpyhI7gF_nnbF7IeiqtHqaeV-L_sv130ipH1FFpL39cyB-HpX51tpS7a-lTqkWUZF3ch2PZabdQhX53qRZUQnosfpWtvAp1USRUvq5mmkeA4K-vQ==)
8. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbm2eIdluUzdRrsIoSLaUCenFLqCMfxL5yJddkRIxmEMqnUmQyQMU8sCXPAizrfxSuR-qSLAsrTq1vdddckY3lLtFSBFWcQB1m45Hgp8GxSxOtyEh4a4cXhN27JHlG9ouVrLkKashmVxNtxhz6UMjdZkV1ZVGHbrgKVYX_QRY-zsL0355ban5hhzrwAuMSLWKJt7w5Ikzw70FswKuT)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq3bpW82HxnOeY1NFgIpiDe4lusBm1aZzSjrSe_C78rCdbdUZYASegiEs2jqI_pjJawSMloFILpf6O7-fRNLCQyR5hicFVAOsihJrg2S-QfKQ4LfC_dUB61JrzuwLF1eFTdrBQbHVtj_92RAk3eT-iVLlE0neJPVxq9011cvEqrgTH3fk0qVGAQXwHusUogdfSK7eyEnnMVICw-C211rF-Cn6epA2Gnr7cvZGUP2QRItdkAIJ91AJHToxQvQ==)
10. [springerprofessional.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoPf84lImioNGHcuST5pm3_Z3iP0laVyC5GkBFlByKzZXUneUgUOb50uBi6sCIgDXkbMQM0mrPObq_TxAblnEm13eubaKY3JpkGYz51yOMkqirZMzfTNVM8jjHMZRC3kVNpPm2oOlZ-AijGQrwsmI2z9BkG-2rs4Gc5zu2heb2R7mf5HSbVaq5qvTBmOMkR88BIdP6PXiOBVHVm7ZCtcaXUJwGzvpH)
11. [shanghaitech.edu.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXM_c_8TlpyUfnbufU_WSf6C0_FSMPUrIomqUyp8dhU5ZpVASz0iQYJJxGJW_wXH0eGY_mYodzyEXP6YDdNt3H9lTS4D0pLezgGi36mnaFEYXmO5akVPVIEeyLnmEGGVTiwjbAUllHGb1-zAF9S7E1xmuvnn1f4owYESIVh0cKvrPSA9uVNLz7E-MZdU0ogZFXkrwbR3g2HkoK0zfh3HXkAYWbjRfKPjMuqoKiuM2MX1V9pE2AC3ck6st9t7QvVMG13BH99lqH66NBCw==)
12. [ust.hk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDBG1GJb4i_QMYNg_cK_pUyISvt8FB30LfPCcs_T6GojQM9AbTDRRLRaqq0Ge0PI8nZeRdUS8HvGgHj9SL2cBFiPWPe235wKdLD41CfLIq1K-mDxnjdMqx-iYi-IGDcWSubbqCYo94A0ryLOQpfGxUMU3wPZKTI9dxIeOPx4WOxw89xSdZN0T8hpu3NjUY7ca3rCNyRQ5zqcJzHiY8yynEhxOnqzTp68o5xrJwPSiMP0Hp98csBg8kHVLt5d9HkQETxg==)
13. [ust.hk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXMzx4Y6jlx4atgT89X-cs9y3QIuQQnvXOmfZXaQDVdhY5VJhacLIdaDYLIX0MPWqifClagBdsWLRVqRWLMxO7w6_zGgxzavgRJNDtxDpe8HDBfv1q5bsnU9TU-yLAllVA3dPcsRy2FQFHA_0TbzbI_XSq)
14. [scut.edu.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcV28VKNFBrOA-dtEXW_LQN0IUsY4j47MsRYJrBMwTGsAgtz45R1aAaqf5jlrU_UYKAuZ66PIKNQpv4UIhU0EC4LSgSZoN8lGl6Xka2xR0GS6QrEgTflWFWO40TP_N4GyAKmuJNigVpHbnVc-0Ecqds6UeKaQh0U99qK6ossrw6q32H0XD2-Fe2DHmDTF86c-GFHAYZIX5N-TAvQQ7aJ7yBE2Wf2ppkgYpotxtXwtwng==)
15. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFohgz_QRuclKbKNWaP20pyOm6BWLAju7zPqFYnW22tmJkahsm4JrjYBWUaaXWhGqdZIr8loxEmXsE-rKMxYmEZMIz205OKmi_OWKWH14Kt9WMOdmYQxxvX1T9kyYs7Loh6tXAz0TiuvbFiKHPFiHqb)
16. [scichina.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3qy6k31lOwTPOKbQfSkxFm6oaReg190UDVOwE3mnITja_nPvka5aa3fizcZe-fdcK9b5R-t3LNZjvotiE5GB2KQCNCj7AkAqGP4BigfUBBQo6a6vfXFDUUmVYky3lqaeb)
17. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXR-o7Yya7-dDQarN7XnstMWwHim-8IKITGegRPOjCRQ4r1mVduQVE5ZTLiaWXhHqTLu_bArptLarJM2wVqkt4dxK4gVvrTSokYzS45rvYpJuLhohB3bkscuFHW1wY)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQER1jHZOPb9z-3C60xd1U-m_L0HN8ZY00haAuL3qE99KXYyMT9r96zUmoGujKHMy3Iy_OjMVPoGkk5HfkkYBoFIuZsA6MF5ZdViHnCaTOj31dE8kUcSE3ThfXxreXBycGGWURWjIN6cC6MjUESRlErpb_QyVOrPezcDq-1wXajQjuYXZIUOAsPAhEiAbqyoweeJzyp_XIyuGCYcCOX_TyO2EHx6kA8AHol-9zMaH203j5qr9VwyDiuVnvj3kkfpppoi7zwYj1bM92CFepeDaz3VwK-UpUIkLQ1dVHRBEMBzlA==)
19. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWQz2NkW-nxoqgVYUsHLl8O_7zlc0aq9Fhf9wyG5WaSrJqXg99DEXSiMLc2Q3fHKel2JWq5OX1UPxFCOzgOIGAM9YpsuX9Z6HyqwKYFWqrbYBm0wu79QLhu8MJHVekOXkAVD6InWuUnw==)
20. [knowmade.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGB0tcF-wAjL4DLPguKf-n0BhZTvglKPptEft2aTF4xQSAe-vDEnV0LX5J9JmeVstDpKs7xPCclt8bGNw1qULYwOvwSk7cntGiRXmVss3m3J52i7jcU2RBOSJfua6MYZja8vnK_8SklY1CVMIwNWNPFyXncJwR-B4eL)
21. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwMJHEClYHH1Y7ifh9MTtwOqszJA4fzOmAZauTJ8Qkol9A1-uJ-bzeRmpU0YwaA16QX1pJte2j8c11q_LiHrpihX_9BSli5rTuFHIgUxLvhAFMReI_1ukFJJp2nQJAILdlWmj4jNEb3LN9T2H-oL-JsnVRuyhEho2EbLEGO3P73q8AnFwACMDKyiw_-JDDUA6iqv2crZPzHlGFb5KsHXMih-wvXyILCRDDNfggn0WU_RlPPtRslV6QQCDkG0yOh_fD)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMEClYRlgQG3aHG2OW3xnF3Vh4QxWsbjJVUS96lfV8HGUl0j5H31aqtuDOyQn5hM_Di1TdIhLEZghv_6wuK1OxED9wap4Py2yDckJbXqG4nkbL4pBpyN7XvKtyEhviGiRKuJwKPbDJYzhOyP33Rjg0w70NfaTDtAyav94IL4AKCbT549fr-5OShsX40xevRmNyX-O2LAVfBCDV60yQ_wpYR92E0WFm0IrJbz4lXa8BhWIfsBXdm1au3YnQNAkPZhAvWiVykaw9NRvyenA_CsR5NTBldTv81mu2ArJObPc-AcQ14g==)
23. [iphy.ac.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX0zSnGlipVMiYnDMlT8AdP8Jj25zYB0Pdic5Dvs1ThAASnre-u67umDreFLpAmJeiBvNZ4dWuMZ5sCGvyL4DUJxa4og1BXD0ltyo5H0gcWGn0Cf07Nq4Y-eYfNEP0LTcQzNQQdgEaVOB_Z9fiRx6Pib60wSsW7sG275QVDQv_voSl1huKl14=)
24. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdTnQzv0eA4fhA4YLBQQnhK5rWO3XQfdkDfs8cyv8RYcyXgxSkvOaCA0FMbVaPUbWW17w-xJfmfm2IVXWpaW6cQulvzx_EAFkmHugJsN8N31F4dfJIEJXV3iw59Kg=)
25. [jos.ac.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuCnfek_MkbCGffkDDIhMx_uBhozF8UsFe0CmqV1XD0YC482Z-Qx-Ikz0ePvWpefpO-hkwWubJqwAFnGSQYBZGGZiG_Y65wQbB2hABySXpD390ufHUUe5jpHJtwpMxqeOBzN9YJnRN7K8Z6tnFWkWdzIXPF2g=)
26. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF52MdjtNRn2ALqFAgI0cKHGdpl-96VivNytN-pqretx2VqOPrbOhv9ZL6wUMAq77mV64NT6pTKVwPXGusALncq8K3bTUqbY1LIYTerj17Xq_j2O0BueL0UDb26INQ3jtG8UoFTuwPWawkPv22M2dvHh5txnxN0Cs6eK7J7ANZUApjS3Rh2UQOWa4Ln0Jx23RhA_xz1vzvdLYU1)
27. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9rHxS3axhlPJymsC4yGiJEq7zS5b3P1ZRXGoSTP2pUnhlA48ahvI-RT7XUfujkftik0jhTw6v2nJ5cQugUg3_eBaoBtF3ytyWfoji6vu5rX72wACOe-WSPh7syc0E6I24ZMUg4WTG8YwqqQrrDGi2XfxM7W39FChyDyfE1_7tQnAZrylWrQ4S2bxsJ3HiQS8Z9qgn_5bYPn4=)


## Annotations
Annotation(end_index=1703, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUhS_PR7hDHcJ1lKeE11PnVW3vdwsUYfQMBUKdEuk9nWSgA8bItOSyBUIT4q4htjnaPLJuF0XM6cBMQvMA7hDl2xVyAJXIjH6Qfvxi-D7RK-w3t2eVAq-akszvSRTY9g-0JplMtSE4oqFsJe7SxwaV85naGTZs6oz1oVICySYgysixaHMbMAweBVMDjcqpxiDaxgvyuBryDopwdVMtG-Nt', start_index=1691)
Annotation(end_index=1703, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWe4EAEgLXXgikvH0CXJUeX7aFJYNwAue0mxLIxbIuFZLuk38TDBHF2feVhClLy3oAlecrWezqPVw-Je11-dcWnJh53MnsYeqfkhK1vnqown4B_w-HRLbrXf7b7SnPqKkEb9T8lVOshuSGHGqCeORhdbSh9wik3AYLlsezBmOAPEjjUUuIrHxsWnC8toez6YccDAMME4-geMJr6lbaHlVjQ6Yy', start_index=1691)
Annotation(end_index=2025, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI6pQXKx09xGdKOFgqeTjoDAt5O8tFyO1c2dpq7hUoyx7jFJV6Nw9_R9g-44WkZJM3bw4-q_wCVzm0VNKYnKYOf1HSw9MERRMOf1EPaUyAF2SAte9gcRG1_Bh6x_mZP8HGYoa3MjnTl_xWrodE2YZU3XnODXr5Wq2m7tRy8KuXZXZMa8-mHdTo6O87KCJ6-N8BYC8kApMciXLoSw8UbMxaG0kW5wQ4YKEAk4q3wxVzO2LmG61XWRaTKwU9HgOE16iNFRgsSg==', start_index=2013)
Annotation(end_index=2025, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWe4EAEgLXXgikvH0CXJUeX7aFJYNwAue0mxLIxbIuFZLuk38TDBHF2feVhClLy3oAlecrWezqPVw-Je11-dcWnJh53MnsYeqfkhK1vnqown4B_w-HRLbrXf7b7SnPqKkEb9T8lVOshuSGHGqCeORhdbSh9wik3AYLlsezBmOAPEjjUUuIrHxsWnC8toez6YccDAMME4-geMJr6lbaHlVjQ6Yy', start_index=2013)
Annotation(end_index=2589, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgYcEEiD6WCBF77uNvMIji7Grl07vqVBdFYBenslUbk-bYcpaIEcdhHpcdpU_AcJzMDngjb5MJRkVTI_07bgareJ_uGPTNVyi7s-7dWc6jzj00aBrCE6DhORRDbTE=', start_index=2577)
Annotation(end_index=2589, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSb0V_bDdKKhyLWKVHZ5DDEIixHGidoxIkTnGc_xxCj6wuP5jIHoFQ6vTbZ7eXQd2fck9Nfn7nFlk-tWBmnQOsazqjdIL5XJ7fkaAr3JwAl7eB2E9TvqMYgfbc5w==', start_index=2577)
Annotation(end_index=2815, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOOJ-776yPwqdu9aTWHf5PK6bkV93IkDmoXxrT6HEbPeuKAnWfkPTwlzNvVow209fUxszNhc6VKTe7ItlxovaSUPRAxGmGb8m4HVE__yXa4uk5Wg0OU3AI8-41rrpzh3Bv2y18CM0q6GP2VxCC-Pj8eHb9GOZHBdKnPr0He8HUhMJVE1pduOG2TzXsZk1OXl0D-RE3djsgb8-tdL5Ol_cnET1dhjzave0z1LuXVIEvo5ggb-nDHgR_CdBsfhTeo45wzHZBqaIKRuJgkyf2E_RNilAa8x3laWjVhPfXPqhWsVKtMc_3Q2ihqa_gOfSDXJxGrA==', start_index=2800)
Annotation(end_index=2815, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGktw0TgY5HmmcPCFkWakjy7syHi5Psst6GtKcSky7B8uK1nqDWYMRwNXH-z88VMIaDiOWrVwoK7FzXx7CHLddyXDp4pj7ZWr7aAuSvpYkpe-EpyhI7gF_nnbF7IeiqtHqaeV-L_sv130ipH1FFpL39cyB-HpX51tpS7a-lTqkWUZF3ch2PZabdQhX53qRZUQnosfpWtvAp1USRUvq5mmkeA4K-vQ==', start_index=2800)
Annotation(end_index=2815, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbm2eIdluUzdRrsIoSLaUCenFLqCMfxL5yJddkRIxmEMqnUmQyQMU8sCXPAizrfxSuR-qSLAsrTq1vdddckY3lLtFSBFWcQB1m45Hgp8GxSxOtyEh4a4cXhN27JHlG9ouVrLkKashmVxNtxhz6UMjdZkV1ZVGHbrgKVYX_QRY-zsL0355ban5hhzrwAuMSLWKJt7w5Ikzw70FswKuT', start_index=2800)
Annotation(end_index=3698, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSb0V_bDdKKhyLWKVHZ5DDEIixHGidoxIkTnGc_xxCj6wuP5jIHoFQ6vTbZ7eXQd2fck9Nfn7nFlk-tWBmnQOsazqjdIL5XJ7fkaAr3JwAl7eB2E9TvqMYgfbc5w==', start_index=3689)
Annotation(end_index=3838, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSb0V_bDdKKhyLWKVHZ5DDEIixHGidoxIkTnGc_xxCj6wuP5jIHoFQ6vTbZ7eXQd2fck9Nfn7nFlk-tWBmnQOsazqjdIL5XJ7fkaAr3JwAl7eB2E9TvqMYgfbc5w==', start_index=3826)
Annotation(end_index=3838, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq3bpW82HxnOeY1NFgIpiDe4lusBm1aZzSjrSe_C78rCdbdUZYASegiEs2jqI_pjJawSMloFILpf6O7-fRNLCQyR5hicFVAOsihJrg2S-QfKQ4LfC_dUB61JrzuwLF1eFTdrBQbHVtj_92RAk3eT-iVLlE0neJPVxq9011cvEqrgTH3fk0qVGAQXwHusUogdfSK7eyEnnMVICw-C211rF-Cn6epA2Gnr7cvZGUP2QRItdkAIJ91AJHToxQvQ==', start_index=3826)
Annotation(end_index=4337, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSb0V_bDdKKhyLWKVHZ5DDEIixHGidoxIkTnGc_xxCj6wuP5jIHoFQ6vTbZ7eXQd2fck9Nfn7nFlk-tWBmnQOsazqjdIL5XJ7fkaAr3JwAl7eB2E9TvqMYgfbc5w==', start_index=4324)
Annotation(end_index=4337, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoPf84lImioNGHcuST5pm3_Z3iP0laVyC5GkBFlByKzZXUneUgUOb50uBi6sCIgDXkbMQM0mrPObq_TxAblnEm13eubaKY3JpkGYz51yOMkqirZMzfTNVM8jjHMZRC3kVNpPm2oOlZ-AijGQrwsmI2z9BkG-2rs4Gc5zu2heb2R7mf5HSbVaq5qvTBmOMkR88BIdP6PXiOBVHVm7ZCtcaXUJwGzvpH', start_index=4324)
Annotation(end_index=4850, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI6pQXKx09xGdKOFgqeTjoDAt5O8tFyO1c2dpq7hUoyx7jFJV6Nw9_R9g-44WkZJM3bw4-q_wCVzm0VNKYnKYOf1HSw9MERRMOf1EPaUyAF2SAte9gcRG1_Bh6x_mZP8HGYoa3MjnTl_xWrodE2YZU3XnODXr5Wq2m7tRy8KuXZXZMa8-mHdTo6O87KCJ6-N8BYC8kApMciXLoSw8UbMxaG0kW5wQ4YKEAk4q3wxVzO2LmG61XWRaTKwU9HgOE16iNFRgsSg==', start_index=4837)
Annotation(end_index=4850, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXM_c_8TlpyUfnbufU_WSf6C0_FSMPUrIomqUyp8dhU5ZpVASz0iQYJJxGJW_wXH0eGY_mYodzyEXP6YDdNt3H9lTS4D0pLezgGi36mnaFEYXmO5akVPVIEeyLnmEGGVTiwjbAUllHGb1-zAF9S7E1xmuvnn1f4owYESIVh0cKvrPSA9uVNLz7E-MZdU0ogZFXkrwbR3g2HkoK0zfh3HXkAYWbjRfKPjMuqoKiuM2MX1V9pE2AC3ck6st9t7QvVMG13BH99lqH66NBCw==', start_index=4837)
Annotation(end_index=5199, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDBG1GJb4i_QMYNg_cK_pUyISvt8FB30LfPCcs_T6GojQM9AbTDRRLRaqq0Ge0PI8nZeRdUS8HvGgHj9SL2cBFiPWPe235wKdLD41CfLIq1K-mDxnjdMqx-iYi-IGDcWSubbqCYo94A0ryLOQpfGxUMU3wPZKTI9dxIeOPx4WOxw89xSdZN0T8hpu3NjUY7ca3rCNyRQ5zqcJzHiY8yynEhxOnqzTp68o5xrJwPSiMP0Hp98csBg8kHVLt5d9HkQETxg==', start_index=5185)
Annotation(end_index=5199, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXM_c_8TlpyUfnbufU_WSf6C0_FSMPUrIomqUyp8dhU5ZpVASz0iQYJJxGJW_wXH0eGY_mYodzyEXP6YDdNt3H9lTS4D0pLezgGi36mnaFEYXmO5akVPVIEeyLnmEGGVTiwjbAUllHGb1-zAF9S7E1xmuvnn1f4owYESIVh0cKvrPSA9uVNLz7E-MZdU0ogZFXkrwbR3g2HkoK0zfh3HXkAYWbjRfKPjMuqoKiuM2MX1V9pE2AC3ck6st9t7QvVMG13BH99lqH66NBCw==', start_index=5185)
Annotation(end_index=6022, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXMzx4Y6jlx4atgT89X-cs9y3QIuQQnvXOmfZXaQDVdhY5VJhacLIdaDYLIX0MPWqifClagBdsWLRVqRWLMxO7w6_zGgxzavgRJNDtxDpe8HDBfv1q5bsnU9TU-yLAllVA3dPcsRy2FQFHA_0TbzbI_XSq', start_index=6012)
Annotation(end_index=6248, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbm2eIdluUzdRrsIoSLaUCenFLqCMfxL5yJddkRIxmEMqnUmQyQMU8sCXPAizrfxSuR-qSLAsrTq1vdddckY3lLtFSBFWcQB1m45Hgp8GxSxOtyEh4a4cXhN27JHlG9ouVrLkKashmVxNtxhz6UMjdZkV1ZVGHbrgKVYX_QRY-zsL0355ban5hhzrwAuMSLWKJt7w5Ikzw70FswKuT', start_index=6239)
Annotation(end_index=6501, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOOJ-776yPwqdu9aTWHf5PK6bkV93IkDmoXxrT6HEbPeuKAnWfkPTwlzNvVow209fUxszNhc6VKTe7ItlxovaSUPRAxGmGb8m4HVE__yXa4uk5Wg0OU3AI8-41rrpzh3Bv2y18CM0q6GP2VxCC-Pj8eHb9GOZHBdKnPr0He8HUhMJVE1pduOG2TzXsZk1OXl0D-RE3djsgb8-tdL5Ol_cnET1dhjzave0z1LuXVIEvo5ggb-nDHgR_CdBsfhTeo45wzHZBqaIKRuJgkyf2E_RNilAa8x3laWjVhPfXPqhWsVKtMc_3Q2ihqa_gOfSDXJxGrA==', start_index=6486)
Annotation(end_index=6501, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGktw0TgY5HmmcPCFkWakjy7syHi5Psst6GtKcSky7B8uK1nqDWYMRwNXH-z88VMIaDiOWrVwoK7FzXx7CHLddyXDp4pj7ZWr7aAuSvpYkpe-EpyhI7gF_nnbF7IeiqtHqaeV-L_sv130ipH1FFpL39cyB-HpX51tpS7a-lTqkWUZF3ch2PZabdQhX53qRZUQnosfpWtvAp1USRUvq5mmkeA4K-vQ==', start_index=6486)
Annotation(end_index=6501, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbm2eIdluUzdRrsIoSLaUCenFLqCMfxL5yJddkRIxmEMqnUmQyQMU8sCXPAizrfxSuR-qSLAsrTq1vdddckY3lLtFSBFWcQB1m45Hgp8GxSxOtyEh4a4cXhN27JHlG9ouVrLkKashmVxNtxhz6UMjdZkV1ZVGHbrgKVYX_QRY-zsL0355ban5hhzrwAuMSLWKJt7w5Ikzw70FswKuT', start_index=6486)
Annotation(end_index=7296, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcV28VKNFBrOA-dtEXW_LQN0IUsY4j47MsRYJrBMwTGsAgtz45R1aAaqf5jlrU_UYKAuZ66PIKNQpv4UIhU0EC4LSgSZoN8lGl6Xka2xR0GS6QrEgTflWFWO40TP_N4GyAKmuJNigVpHbnVc-0Ecqds6UeKaQh0U99qK6ossrw6q32H0XD2-Fe2DHmDTF86c-GFHAYZIX5N-TAvQQ7aJ7yBE2Wf2ppkgYpotxtXwtwng==', start_index=7279)
Annotation(end_index=7296, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFohgz_QRuclKbKNWaP20pyOm6BWLAju7zPqFYnW22tmJkahsm4JrjYBWUaaXWhGqdZIr8loxEmXsE-rKMxYmEZMIz205OKmi_OWKWH14Kt9WMOdmYQxxvX1T9kyYs7Loh6tXAz0TiuvbFiKHPFiHqb', start_index=7279)
Annotation(end_index=7296, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGktw0TgY5HmmcPCFkWakjy7syHi5Psst6GtKcSky7B8uK1nqDWYMRwNXH-z88VMIaDiOWrVwoK7FzXx7CHLddyXDp4pj7ZWr7aAuSvpYkpe-EpyhI7gF_nnbF7IeiqtHqaeV-L_sv130ipH1FFpL39cyB-HpX51tpS7a-lTqkWUZF3ch2PZabdQhX53qRZUQnosfpWtvAp1USRUvq5mmkeA4K-vQ==', start_index=7279)
Annotation(end_index=7772, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSb0V_bDdKKhyLWKVHZ5DDEIixHGidoxIkTnGc_xxCj6wuP5jIHoFQ6vTbZ7eXQd2fck9Nfn7nFlk-tWBmnQOsazqjdIL5XJ7fkaAr3JwAl7eB2E9TvqMYgfbc5w==', start_index=7759)
Annotation(end_index=7772, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoPf84lImioNGHcuST5pm3_Z3iP0laVyC5GkBFlByKzZXUneUgUOb50uBi6sCIgDXkbMQM0mrPObq_TxAblnEm13eubaKY3JpkGYz51yOMkqirZMzfTNVM8jjHMZRC3kVNpPm2oOlZ-AijGQrwsmI2z9BkG-2rs4Gc5zu2heb2R7mf5HSbVaq5qvTBmOMkR88BIdP6PXiOBVHVm7ZCtcaXUJwGzvpH', start_index=7759)
Annotation(end_index=8523, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDBG1GJb4i_QMYNg_cK_pUyISvt8FB30LfPCcs_T6GojQM9AbTDRRLRaqq0Ge0PI8nZeRdUS8HvGgHj9SL2cBFiPWPe235wKdLD41CfLIq1K-mDxnjdMqx-iYi-IGDcWSubbqCYo94A0ryLOQpfGxUMU3wPZKTI9dxIeOPx4WOxw89xSdZN0T8hpu3NjUY7ca3rCNyRQ5zqcJzHiY8yynEhxOnqzTp68o5xrJwPSiMP0Hp98csBg8kHVLt5d9HkQETxg==', start_index=8505)
Annotation(end_index=8523, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3qy6k31lOwTPOKbQfSkxFm6oaReg190UDVOwE3mnITja_nPvka5aa3fizcZe-fdcK9b5R-t3LNZjvotiE5GB2KQCNCj7AkAqGP4BigfUBBQo6a6vfXFDUUmVYky3lqaeb', start_index=8505)
Annotation(end_index=8523, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXM_c_8TlpyUfnbufU_WSf6C0_FSMPUrIomqUyp8dhU5ZpVASz0iQYJJxGJW_wXH0eGY_mYodzyEXP6YDdNt3H9lTS4D0pLezgGi36mnaFEYXmO5akVPVIEeyLnmEGGVTiwjbAUllHGb1-zAF9S7E1xmuvnn1f4owYESIVh0cKvrPSA9uVNLz7E-MZdU0ogZFXkrwbR3g2HkoK0zfh3HXkAYWbjRfKPjMuqoKiuM2MX1V9pE2AC3ck6st9t7QvVMG13BH99lqH66NBCw==', start_index=8505)
Annotation(end_index=9038, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDBG1GJb4i_QMYNg_cK_pUyISvt8FB30LfPCcs_T6GojQM9AbTDRRLRaqq0Ge0PI8nZeRdUS8HvGgHj9SL2cBFiPWPe235wKdLD41CfLIq1K-mDxnjdMqx-iYi-IGDcWSubbqCYo94A0ryLOQpfGxUMU3wPZKTI9dxIeOPx4WOxw89xSdZN0T8hpu3NjUY7ca3rCNyRQ5zqcJzHiY8yynEhxOnqzTp68o5xrJwPSiMP0Hp98csBg8kHVLt5d9HkQETxg==', start_index=9028)
Annotation(end_index=9468, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXR-o7Yya7-dDQarN7XnstMWwHim-8IKITGegRPOjCRQ4r1mVduQVE5ZTLiaWXhHqTLu_bArptLarJM2wVqkt4dxK4gVvrTSokYzS45rvYpJuLhohB3bkscuFHW1wY', start_index=9458)
Annotation(end_index=9961, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQER1jHZOPb9z-3C60xd1U-m_L0HN8ZY00haAuL3qE99KXYyMT9r96zUmoGujKHMy3Iy_OjMVPoGkk5HfkkYBoFIuZsA6MF5ZdViHnCaTOj31dE8kUcSE3ThfXxreXBycGGWURWjIN6cC6MjUESRlErpb_QyVOrPezcDq-1wXajQjuYXZIUOAsPAhEiAbqyoweeJzyp_XIyuGCYcCOX_TyO2EHx6kA8AHol-9zMaH203j5qr9VwyDiuVnvj3kkfpppoi7zwYj1bM92CFepeDaz3VwK-UpUIkLQ1dVHRBEMBzlA==', start_index=9947)
Annotation(end_index=9961, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXR-o7Yya7-dDQarN7XnstMWwHim-8IKITGegRPOjCRQ4r1mVduQVE5ZTLiaWXhHqTLu_bArptLarJM2wVqkt4dxK4gVvrTSokYzS45rvYpJuLhohB3bkscuFHW1wY', start_index=9947)
Annotation(end_index=10291, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWQz2NkW-nxoqgVYUsHLl8O_7zlc0aq9Fhf9wyG5WaSrJqXg99DEXSiMLc2Q3fHKel2JWq5OX1UPxFCOzgOIGAM9YpsuX9Z6HyqwKYFWqrbYBm0wu79QLhu8MJHVekOXkAVD6InWuUnw==', start_index=10281)
Annotation(end_index=10564, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWQz2NkW-nxoqgVYUsHLl8O_7zlc0aq9Fhf9wyG5WaSrJqXg99DEXSiMLc2Q3fHKel2JWq5OX1UPxFCOzgOIGAM9YpsuX9Z6HyqwKYFWqrbYBm0wu79QLhu8MJHVekOXkAVD6InWuUnw==', start_index=10554)
Annotation(end_index=10855, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWQz2NkW-nxoqgVYUsHLl8O_7zlc0aq9Fhf9wyG5WaSrJqXg99DEXSiMLc2Q3fHKel2JWq5OX1UPxFCOzgOIGAM9YpsuX9Z6HyqwKYFWqrbYBm0wu79QLhu8MJHVekOXkAVD6InWuUnw==', start_index=10845)
Annotation(end_index=11436, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSb0V_bDdKKhyLWKVHZ5DDEIixHGidoxIkTnGc_xxCj6wuP5jIHoFQ6vTbZ7eXQd2fck9Nfn7nFlk-tWBmnQOsazqjdIL5XJ7fkaAr3JwAl7eB2E9TvqMYgfbc5w==', start_index=11427)
Annotation(end_index=11736, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgYcEEiD6WCBF77uNvMIji7Grl07vqVBdFYBenslUbk-bYcpaIEcdhHpcdpU_AcJzMDngjb5MJRkVTI_07bgareJ_uGPTNVyi7s-7dWc6jzj00aBrCE6DhORRDbTE=', start_index=11723)
Annotation(end_index=11736, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXM_c_8TlpyUfnbufU_WSf6C0_FSMPUrIomqUyp8dhU5ZpVASz0iQYJJxGJW_wXH0eGY_mYodzyEXP6YDdNt3H9lTS4D0pLezgGi36mnaFEYXmO5akVPVIEeyLnmEGGVTiwjbAUllHGb1-zAF9S7E1xmuvnn1f4owYESIVh0cKvrPSA9uVNLz7E-MZdU0ogZFXkrwbR3g2HkoK0zfh3HXkAYWbjRfKPjMuqoKiuM2MX1V9pE2AC3ck6st9t7QvVMG13BH99lqH66NBCw==', start_index=11723)
Annotation(end_index=11882, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGB0tcF-wAjL4DLPguKf-n0BhZTvglKPptEft2aTF4xQSAe-vDEnV0LX5J9JmeVstDpKs7xPCclt8bGNw1qULYwOvwSk7cntGiRXmVss3m3J52i7jcU2RBOSJfua6MYZja8vnK_8SklY1CVMIwNWNPFyXncJwR-B4eL', start_index=11872)
Annotation(end_index=12289, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwMJHEClYHH1Y7ifh9MTtwOqszJA4fzOmAZauTJ8Qkol9A1-uJ-bzeRmpU0YwaA16QX1pJte2j8c11q_LiHrpihX_9BSli5rTuFHIgUxLvhAFMReI_1ukFJJp2nQJAILdlWmj4jNEb3LN9T2H-oL-JsnVRuyhEho2EbLEGO3P73q8AnFwACMDKyiw_-JDDUA6iqv2crZPzHlGFb5KsHXMih-wvXyILCRDDNfggn0WU_RlPPtRslV6QQCDkG0yOh_fD', start_index=12279)
Annotation(end_index=12518, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMEClYRlgQG3aHG2OW3xnF3Vh4QxWsbjJVUS96lfV8HGUl0j5H31aqtuDOyQn5hM_Di1TdIhLEZghv_6wuK1OxED9wap4Py2yDckJbXqG4nkbL4pBpyN7XvKtyEhviGiRKuJwKPbDJYzhOyP33Rjg0w70NfaTDtAyav94IL4AKCbT549fr-5OShsX40xevRmNyX-O2LAVfBCDV60yQ_wpYR92E0WFm0IrJbz4lXa8BhWIfsBXdm1au3YnQNAkPZhAvWiVykaw9NRvyenA_CsR5NTBldTv81mu2ArJObPc-AcQ14g==', start_index=12508)
Annotation(end_index=13245, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI6pQXKx09xGdKOFgqeTjoDAt5O8tFyO1c2dpq7hUoyx7jFJV6Nw9_R9g-44WkZJM3bw4-q_wCVzm0VNKYnKYOf1HSw9MERRMOf1EPaUyAF2SAte9gcRG1_Bh6x_mZP8HGYoa3MjnTl_xWrodE2YZU3XnODXr5Wq2m7tRy8KuXZXZMa8-mHdTo6O87KCJ6-N8BYC8kApMciXLoSw8UbMxaG0kW5wQ4YKEAk4q3wxVzO2LmG61XWRaTKwU9HgOE16iNFRgsSg==', start_index=13232)
Annotation(end_index=13245, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXM_c_8TlpyUfnbufU_WSf6C0_FSMPUrIomqUyp8dhU5ZpVASz0iQYJJxGJW_wXH0eGY_mYodzyEXP6YDdNt3H9lTS4D0pLezgGi36mnaFEYXmO5akVPVIEeyLnmEGGVTiwjbAUllHGb1-zAF9S7E1xmuvnn1f4owYESIVh0cKvrPSA9uVNLz7E-MZdU0ogZFXkrwbR3g2HkoK0zfh3HXkAYWbjRfKPjMuqoKiuM2MX1V9pE2AC3ck6st9t7QvVMG13BH99lqH66NBCw==', start_index=13232)
Annotation(end_index=13661, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX0zSnGlipVMiYnDMlT8AdP8Jj25zYB0Pdic5Dvs1ThAASnre-u67umDreFLpAmJeiBvNZ4dWuMZ5sCGvyL4DUJxa4og1BXD0ltyo5H0gcWGn0Cf07Nq4Y-eYfNEP0LTcQzNQQdgEaVOB_Z9fiRx6Pib60wSsW7sG275QVDQv_voSl1huKl14=', start_index=13647)
Annotation(end_index=13661, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdTnQzv0eA4fhA4YLBQQnhK5rWO3XQfdkDfs8cyv8RYcyXgxSkvOaCA0FMbVaPUbWW17w-xJfmfm2IVXWpaW6cQulvzx_EAFkmHugJsN8N31F4dfJIEJXV3iw59Kg=', start_index=13647)
Annotation(end_index=13885, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF52MdjtNRn2ALqFAgI0cKHGdpl-96VivNytN-pqretx2VqOPrbOhv9ZL6wUMAq77mV64NT6pTKVwPXGusALncq8K3bTUqbY1LIYTerj17Xq_j2O0BueL0UDb26INQ3jtG8UoFTuwPWawkPv22M2dvHh5txnxN0Cs6eK7J7ANZUApjS3Rh2UQOWa4Ln0Jx23RhA_xz1vzvdLYU1', start_index=13871)
Annotation(end_index=13885, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuCnfek_MkbCGffkDDIhMx_uBhozF8UsFe0CmqV1XD0YC482Z-Qx-Ikz0ePvWpefpO-hkwWubJqwAFnGSQYBZGGZiG_Y65wQbB2hABySXpD390ufHUUe5jpHJtwpMxqeOBzN9YJnRN7K8Z6tnFWkWdzIXPF2g=', start_index=13871)
Annotation(end_index=15226, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFohgz_QRuclKbKNWaP20pyOm6BWLAju7zPqFYnW22tmJkahsm4JrjYBWUaaXWhGqdZIr8loxEmXsE-rKMxYmEZMIz205OKmi_OWKWH14Kt9WMOdmYQxxvX1T9kyYs7Loh6tXAz0TiuvbFiKHPFiHqb', start_index=15203)
Annotation(end_index=15226, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOOJ-776yPwqdu9aTWHf5PK6bkV93IkDmoXxrT6HEbPeuKAnWfkPTwlzNvVow209fUxszNhc6VKTe7ItlxovaSUPRAxGmGb8m4HVE__yXa4uk5Wg0OU3AI8-41rrpzh3Bv2y18CM0q6GP2VxCC-Pj8eHb9GOZHBdKnPr0He8HUhMJVE1pduOG2TzXsZk1OXl0D-RE3djsgb8-tdL5Ol_cnET1dhjzave0z1LuXVIEvo5ggb-nDHgR_CdBsfhTeo45wzHZBqaIKRuJgkyf2E_RNilAa8x3laWjVhPfXPqhWsVKtMc_3Q2ihqa_gOfSDXJxGrA==', start_index=15203)
Annotation(end_index=15226, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXMzx4Y6jlx4atgT89X-cs9y3QIuQQnvXOmfZXaQDVdhY5VJhacLIdaDYLIX0MPWqifClagBdsWLRVqRWLMxO7w6_zGgxzavgRJNDtxDpe8HDBfv1q5bsnU9TU-yLAllVA3dPcsRy2FQFHA_0TbzbI_XSq', start_index=15203)
Annotation(end_index=15226, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGktw0TgY5HmmcPCFkWakjy7syHi5Psst6GtKcSky7B8uK1nqDWYMRwNXH-z88VMIaDiOWrVwoK7FzXx7CHLddyXDp4pj7ZWr7aAuSvpYkpe-EpyhI7gF_nnbF7IeiqtHqaeV-L_sv130ipH1FFpL39cyB-HpX51tpS7a-lTqkWUZF3ch2PZabdQhX53qRZUQnosfpWtvAp1USRUvq5mmkeA4K-vQ==', start_index=15203)
Annotation(end_index=15226, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbm2eIdluUzdRrsIoSLaUCenFLqCMfxL5yJddkRIxmEMqnUmQyQMU8sCXPAizrfxSuR-qSLAsrTq1vdddckY3lLtFSBFWcQB1m45Hgp8GxSxOtyEh4a4cXhN27JHlG9ouVrLkKashmVxNtxhz6UMjdZkV1ZVGHbrgKVYX_QRY-zsL0355ban5hhzrwAuMSLWKJt7w5Ikzw70FswKuT', start_index=15203)
Annotation(end_index=15848, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9rHxS3axhlPJymsC4yGiJEq7zS5b3P1ZRXGoSTP2pUnhlA48ahvI-RT7XUfujkftik0jhTw6v2nJ5cQugUg3_eBaoBtF3ytyWfoji6vu5rX72wACOe-WSPh7syc0E6I24ZMUg4WTG8YwqqQrrDGi2XfxM7W39FChyDyfE1_7tQnAZrylWrQ4S2bxsJ3HiQS8Z9qgn_5bYPn4=', start_index=15835)
Annotation(end_index=15848, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUhS_PR7hDHcJ1lKeE11PnVW3vdwsUYfQMBUKdEuk9nWSgA8bItOSyBUIT4q4htjnaPLJuF0XM6cBMQvMA7hDl2xVyAJXIjH6Qfvxi-D7RK-w3t2eVAq-akszvSRTY9g-0JplMtSE4oqFsJe7SxwaV85naGTZs6oz1oVICySYgysixaHMbMAweBVMDjcqpxiDaxgvyuBryDopwdVMtG-Nt', start_index=15835)
Annotation(end_index=16162, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI6pQXKx09xGdKOFgqeTjoDAt5O8tFyO1c2dpq7hUoyx7jFJV6Nw9_R9g-44WkZJM3bw4-q_wCVzm0VNKYnKYOf1HSw9MERRMOf1EPaUyAF2SAte9gcRG1_Bh6x_mZP8HGYoa3MjnTl_xWrodE2YZU3XnODXr5Wq2m7tRy8KuXZXZMa8-mHdTo6O87KCJ6-N8BYC8kApMciXLoSw8UbMxaG0kW5wQ4YKEAk4q3wxVzO2LmG61XWRaTKwU9HgOE16iNFRgsSg==', start_index=16150)
Annotation(end_index=16162, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSb0V_bDdKKhyLWKVHZ5DDEIixHGidoxIkTnGc_xxCj6wuP5jIHoFQ6vTbZ7eXQd2fck9Nfn7nFlk-tWBmnQOsazqjdIL5XJ7fkaAr3JwAl7eB2E9TvqMYgfbc5w==', start_index=16150)
Annotation(end_index=16336, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSb0V_bDdKKhyLWKVHZ5DDEIixHGidoxIkTnGc_xxCj6wuP5jIHoFQ6vTbZ7eXQd2fck9Nfn7nFlk-tWBmnQOsazqjdIL5XJ7fkaAr3JwAl7eB2E9TvqMYgfbc5w==', start_index=16320)
Annotation(end_index=16336, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwMJHEClYHH1Y7ifh9MTtwOqszJA4fzOmAZauTJ8Qkol9A1-uJ-bzeRmpU0YwaA16QX1pJte2j8c11q_LiHrpihX_9BSli5rTuFHIgUxLvhAFMReI_1ukFJJp2nQJAILdlWmj4jNEb3LN9T2H-oL-JsnVRuyhEho2EbLEGO3P73q8AnFwACMDKyiw_-JDDUA6iqv2crZPzHlGFb5KsHXMih-wvXyILCRDDNfggn0WU_RlPPtRslV6QQCDkG0yOh_fD', start_index=16320)
Annotation(end_index=16336, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq3bpW82HxnOeY1NFgIpiDe4lusBm1aZzSjrSe_C78rCdbdUZYASegiEs2jqI_pjJawSMloFILpf6O7-fRNLCQyR5hicFVAOsihJrg2S-QfKQ4LfC_dUB61JrzuwLF1eFTdrBQbHVtj_92RAk3eT-iVLlE0neJPVxq9011cvEqrgTH3fk0qVGAQXwHusUogdfSK7eyEnnMVICw-C211rF-Cn6epA2Gnr7cvZGUP2QRItdkAIJ91AJHToxQvQ==', start_index=16320)
Annotation(end_index=16603, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXR-o7Yya7-dDQarN7XnstMWwHim-8IKITGegRPOjCRQ4r1mVduQVE5ZTLiaWXhHqTLu_bArptLarJM2wVqkt4dxK4gVvrTSokYzS45rvYpJuLhohB3bkscuFHW1wY', start_index=16593)
Annotation(end_index=16813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWQz2NkW-nxoqgVYUsHLl8O_7zlc0aq9Fhf9wyG5WaSrJqXg99DEXSiMLc2Q3fHKel2JWq5OX1UPxFCOzgOIGAM9YpsuX9Z6HyqwKYFWqrbYBm0wu79QLhu8MJHVekOXkAVD6InWuUnw==', start_index=16803)
Annotation(end_index=17077, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDBG1GJb4i_QMYNg_cK_pUyISvt8FB30LfPCcs_T6GojQM9AbTDRRLRaqq0Ge0PI8nZeRdUS8HvGgHj9SL2cBFiPWPe235wKdLD41CfLIq1K-mDxnjdMqx-iYi-IGDcWSubbqCYo94A0ryLOQpfGxUMU3wPZKTI9dxIeOPx4WOxw89xSdZN0T8hpu3NjUY7ca3rCNyRQ5zqcJzHiY8yynEhxOnqzTp68o5xrJwPSiMP0Hp98csBg8kHVLt5d9HkQETxg==', start_index=17059)
Annotation(end_index=17077, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3qy6k31lOwTPOKbQfSkxFm6oaReg190UDVOwE3mnITja_nPvka5aa3fizcZe-fdcK9b5R-t3LNZjvotiE5GB2KQCNCj7AkAqGP4BigfUBBQo6a6vfXFDUUmVYky3lqaeb', start_index=17059)
Annotation(end_index=17077, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXM_c_8TlpyUfnbufU_WSf6C0_FSMPUrIomqUyp8dhU5ZpVASz0iQYJJxGJW_wXH0eGY_mYodzyEXP6YDdNt3H9lTS4D0pLezgGi36mnaFEYXmO5akVPVIEeyLnmEGGVTiwjbAUllHGb1-zAF9S7E1xmuvnn1f4owYESIVh0cKvrPSA9uVNLz7E-MZdU0ogZFXkrwbR3g2HkoK0zfh3HXkAYWbjRfKPjMuqoKiuM2MX1V9pE2AC3ck6st9t7QvVMG13BH99lqH66NBCw==', start_index=17059)
Annotation(end_index=17426, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX0zSnGlipVMiYnDMlT8AdP8Jj25zYB0Pdic5Dvs1ThAASnre-u67umDreFLpAmJeiBvNZ4dWuMZ5sCGvyL4DUJxa4og1BXD0ltyo5H0gcWGn0Cf07Nq4Y-eYfNEP0LTcQzNQQdgEaVOB_Z9fiRx6Pib60wSsW7sG275QVDQv_voSl1huKl14=', start_index=17412)
Annotation(end_index=17426, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdTnQzv0eA4fhA4YLBQQnhK5rWO3XQfdkDfs8cyv8RYcyXgxSkvOaCA0FMbVaPUbWW17w-xJfmfm2IVXWpaW6cQulvzx_EAFkmHugJsN8N31F4dfJIEJXV3iw59Kg=', start_index=17412)
Annotation(end_index=17639, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgYcEEiD6WCBF77uNvMIji7Grl07vqVBdFYBenslUbk-bYcpaIEcdhHpcdpU_AcJzMDngjb5MJRkVTI_07bgareJ_uGPTNVyi7s-7dWc6jzj00aBrCE6DhORRDbTE=', start_index=17630)

## Sources
