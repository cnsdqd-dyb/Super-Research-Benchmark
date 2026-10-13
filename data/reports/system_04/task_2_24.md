# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 6fba93e7 | **Time:** 340.20s | **Cost:** $1.92901
--------------------------------------------------------------------------------

# Optimizing Power Management Circuits in Implantable Devices: Balancing Volume, Battery Life, and Safety

### Key Points
*   **Thermal Safety Limits:** Implantable devices are strictly constrained by thermal safety standards (ISO 14708-1), typically limiting tissue temperature rise to no more than 2°C, with power density limits often cited around 40 mW/cm² for muscle tissue.
*   **Volume Reduction via SIMO:** Single-Inductor Multiple-Output (SIMO) DC-DC converters are a critical optimization strategy, allowing a single inductor to regulate multiple voltage rails with efficiencies reaching up to 94.4%, thereby minimizing device volume without sacrificing power efficiency.
*   **Hybrid Energy Storage:** Combining high-energy-density batteries with high-power-density supercapacitors buffers pulse loads (e.g., in neurostimulators), extending battery life by reducing peak current stress and internal heating.
*   **Active Charge Balancing:** To eliminate bulky DC blocking capacitors and save space, modern designs utilize active charge balancing circuits (using feedback loops to nullify residual charge), which maintain safety standards while significantly reducing the implant's physical footprint.
*   **Closed-Loop Thermal Management:** Advanced Power Management Units (PMUs) now incorporate real-time thermal feedback loops that dynamically throttle device performance or stimulation parameters if tissue temperature approaches safety thresholds.

---

## 1. Introduction

The development of Implantable Medical Devices (IMDs) has transitioned from simple, fixed-rate pacemakers to sophisticated, closed-loop systems capable of deep brain stimulation (DBS), retinal prosthetics, and real-time physiological monitoring [cite: 1]. However, this functional expansion introduces a critical engineering paradox: the demand for increased computational and stimulation power directly conflicts with the stringent constraints on device volume and thermal safety. As devices miniaturize to reduce surgical invasiveness, the surface area available for heat dissipation decreases, causing power density to rise significantly [cite: 2, 3].

Power Management Circuits (PMCs) sit at the nexus of this challenge. They must convert energy from sources (batteries or wireless harvesters) to usable voltage levels with extreme efficiency to maximize battery life, while simultaneously ensuring that energy losses do not manifest as tissue-damaging heat. Furthermore, in neural applications, PMCs must ensure electrochemical safety through precise charge balancing to prevent electrode corrosion and tissue toxicity [cite: 4, 5].

This report analyzes the optimization of PMCs in implantable devices, focusing on circuit topologies, energy storage architectures, and safety mechanisms designed to balance the competing demands of longevity, miniaturization, and biological safety.

---

## 2. Constraints in Implantable Power Management

Designing PMCs for the intra-body environment requires adherence to strict physiological and physical boundaries. These constraints dictate the choice of circuit topology and control strategies.

### 2.1. Thermal and Power Density Limits
The primary safety constraint for active IMDs is thermal generation. The human body maintains a stable core temperature, and local heating can lead to cell necrosis.
*   **Regulatory Standards:** ISO 14708-1 mandates that the outer surface of an implantable device must not exceed a temperature rise of 2°C above normal body temperature [cite: 6, 7].
*   **Tissue Sensitivity:** Research indicates that a heat flux density of approximately 40 mW/cm² is the upper limit for implants located in muscle and lung tissue to remain within the 2°C rise threshold [cite: 6]. However, for deep brain implants or devices in poorly perfused areas, the tolerance may be lower due to the tissue's limited ability to dissipate heat via blood flow [cite: 2].
*   **Circuit Implications:** Inefficient power conversion results in heat dissipation. For a miniaturized device, a power conversion efficiency (PCE) drop of even a few percentage points can cause the power density to exceed safe thermal limits, triggering a "hotspot" on the device surface [cite: 7].

### 2.2. Volumetric Constraints
The physical size of an IMD is dominated by its power source and power management components.
*   **Battery Dominance:** In traditional pacemakers and neurostimulators, the battery accounts for the majority of the device volume [cite: 8]. Reducing battery size without reducing power consumption compromises device longevity, necessitating more frequent surgical replacements.
*   **Passive Component Bulk:** Conventional power converters and safety mechanisms rely on large passive components. Inductors used in switching regulators and DC blocking capacitors used for safety are often the largest components on the circuit board, limiting the ability to shrink the device to millimeter scales [cite: 9, 10].

### 2.3. Electrochemical Safety (Charge Balancing)
For electrical stimulators, safety is not just thermal but electrochemical. Injecting current into tissue requires a reversible process. If the net charge injected is not zero (charge imbalance), it leads to pH changes, tissue damage, and electrode corrosion. Traditionally, this is managed by placing a large capacitor in series with the electrode (passive balancing), but this consumes excessive volume [cite: 5, 11].

---

## 3. Circuit Topology Optimization for Volume and Efficiency

To address volume constraints while maintaining high efficiency, PMCs have evolved from standard linear regulators to complex switching architectures.

### 3.1. Single-Inductor Multiple-Output (SIMO) Converters
Modern IMDs require multiple voltage domains (e.g., low voltage for logic/sensors, high voltage for stimulation) from a single battery source. Using multiple distinct DC-DC converters for each rail is volumetrically inefficient due to the need for multiple bulky inductors.
*   **Architecture:** SIMO converters utilize a single inductor to regulate multiple output voltages through time-multiplexing or power-distributive control. This drastically reduces the component count and board area [cite: 12, 13].
*   **Efficiency vs. Cross-Regulation:** While SIMO topologies save space, they suffer from cross-regulation (load changes on one output affect others). Advanced control techniques, such as hysteresis mode control and adaptive peak-current control, have been developed to minimize this effect. Research demonstrates SIMO converters achieving peak efficiencies of **94.4%** while maintaining tight regulation, making them ideal for space-constrained implants [cite: 14, 15].
*   **Application:** A SIMO auto-buck-boost converter implemented in 0.35-μm CMOS process showed a peak efficiency of >91% at 0.5 W output, proving viability for multi-rail implants like retinal prostheses [cite: 15].

### 3.2. Switched-Capacitor (SC) Converters
For extreme miniaturization where even a single inductor is too large (e.g., injectable devices), Switched-Capacitor (SC) converters are utilized.
*   **Inductor-less Design:** SC converters use capacitors and switches to convert voltage. Since capacitors can be integrated on-chip (unlike high-quality inductors), SC converters allow for fully integrated power management units (PMUs) [cite: 16].
*   **Power Density:** SC converters support higher power density compared to magnetic-based converters for specific conversion ratios. However, their efficiency drops significantly if the input/output voltage ratio deviates from the designed topology (e.g., 2:1, 3:1). Optimization involves dynamic topology reconfiguration to match the battery voltage as it depletes, maintaining efficiency over the battery's life [cite: 16, 17].

### 3.3. Emerging Materials: CNFETs
To further push the boundaries of power density and efficiency, Carbon Nanotube Field-Effect Transistors (CNFETs) are being explored.
*   **Low-Voltage Operation:** CNFET-based rectifiers and logic circuits have demonstrated superior performance at low voltages (0.6V) compared to standard CMOS. Simulations indicate CNFET circuits can achieve power conversion efficiencies (PCE) of **78%** even with weak input signals, which is critical for energy-harvesting implants where input power is scarce and variable [cite: 18, 19].
*   **Thermal Benefits:** The high channel mobility and lower leakage of CNFETs contribute to reduced power dissipation, directly addressing the thermal safety constraint [cite: 19].

---

## 4. Optimizing Battery Life and Safety via Hybrid Storage

Battery life is a critical factor in patient quality of life, as depletion necessitates surgery. However, the load profile of many IMDs (especially neurostimulators) is pulsed, not constant. Batteries degrade faster under high-current pulses due to internal resistance.

### 4.1. The Battery-Supercapacitor Hybrid
A hybrid energy storage system (HESS) combines a high-energy-density battery (e.g., Li-CFx or Li-ion) with a high-power-density supercapacitor.
*   **Pulse Buffering:** The supercapacitor handles the high-current pulses required for stimulation or data transmission, while the battery provides a steady, low-current background charge to the capacitor. This reduces the peak current stress on the battery [cite: 20, 21].
*   **Life Extension:** Research indicates that reducing the depth of discharge (DoD) and peak current stress on the battery can significantly extend its operational lifespan. In one study, adding a supercapacitor extended the effective battery lifetime from 5.34 years to **7 years** by smoothing the load profile [cite: 20].
*   **Safety Enhancement:** By offloading high-current demands to the supercapacitor, the internal heating of the battery is reduced. Furthermore, supercapacitors are inherently safer than Li-ion batteries regarding thermal runaway risks [cite: 22].

### 4.2. Biological Supercapacitors
Recent innovations have introduced "biological supercapacitors" that utilize bodily fluids (serum, urine) as electrolytes.
*   **Miniaturization:** These devices can be as thin as **1 μm**, allowing them to be flexible and integrated directly into tissue interfaces without the bulk of traditional casings. They offer power densities comparable to Li-ion thin films but with improved biocompatibility and mechanical flexibility [cite: 23, 24].

---

## 5. Safety-Aware Circuit Design: Active Charge Balancing

In neural stimulators, ensuring zero net charge transfer is non-negotiable for safety. The traditional method uses a large DC blocking capacitor for every channel. For high-channel-count devices (e.g., retinal implants with 1000+ electrodes), this volume is prohibitive.

### 5.1. Eliminating the Blocking Capacitor
"Active charge balancing" removes the blocking capacitor, saving massive volume, but shifts the safety burden to the circuit design.
*   **Techniques:**
    *   **Offset Compensation:** A feedback loop monitors the voltage remaining on the electrode after a stimulation pulse. If a residual voltage is detected, a corrective current is injected to nullify it [cite: 4, 25].
    *   **Inter-Pulse Charge Control (IPCC):** This technique instantaneously removes excess charge between pulses. Combined with offset compensation, it ensures the residual voltage remains within the "water window" (safe electrochemical range) [cite: 25, 26].
*   **Volume Savings:** By moving from passive capacitors to active transistor-based balancing, the area required for the output stage can be reduced by orders of magnitude, enabling high-density arrays that fit within the eye or brain [cite: 5, 11].
*   **Fail-Safe Mechanisms:** Since active circuits can fail, safety requires redundant monitoring. If the active balancer fails to clear the charge, a "shorting switch" (passive discharge) is often engaged as a backup to discharge the electrode to ground [cite: 11, 27].

---

## 6. Thermal-Aware Power Management

To strictly adhere to the 2°C limit, modern PMCs are incorporating active thermal monitoring.

### 6.1. Closed-Loop Thermal Regulation
Advanced implants now feature on-chip temperature sensors that provide real-time feedback to the power management unit.
*   **Dynamic Throttling:** If the local temperature approaches the safety threshold, the control logic can dynamically reduce the stimulation frequency, data transmission rate, or processor clock speed. This "thermal throttling" ensures the device never exceeds the ISO 14708-1 limits, even if it means temporarily degrading performance [cite: 28, 29].
*   **Distributed Dissipation:** Circuit layout strategies are employed to avoid "hotspots." By distributing power-intensive blocks (like regulators and drivers) across the chip area, the heat flux is spread out, keeping the peak power density below the critical 40 mW/cm² limit [cite: 6, 7].

### 6.2. Wireless Power Transfer (WPT) Considerations
For battery-less or rechargeable implants, the energy transfer process itself generates heat.
*   **Ultrasonic WPT:** For millimeter-sized implants deep in the body, ultrasonic power transfer is often preferred over inductive coupling because it has shorter wavelengths and can be focused. However, the piezoelectric receiver heats up during conversion. PMUs for these devices must optimize the acoustic-to-electrical conversion impedance matching to minimize reflection and heat generation [cite: 30, 31].
*   **Efficiency Optimization:** A PMU designed for magnetoelectric WPT achieved a peak system efficiency of 73.33% by using a "skewed-duty-cycle" Maximum Power Point Tracking (MPPT) technique. This high efficiency is crucial not just for power delivery, but for minimizing the waste heat that would otherwise damage surrounding tissue [cite: 30].

---

## 7. Conclusion

Optimizing power management in implantable devices is a multi-dimensional optimization problem where volume, efficiency, and safety are tightly coupled.
*   **Volume** is addressed through **SIMO converters** and **active charge balancing**, which eliminate bulky inductors and capacitors.
*   **Battery Life** is extended through **hybrid storage systems** (supercapacitors) that buffer pulse loads, and **high-efficiency topologies** (94%+ efficiency) that reduce waste.
*   **Safety** is ensured through **thermal feedback loops**, **active residual charge monitoring**, and adherence to power density limits (approx. 40 mW/cm²).

Future advancements lie in the integration of **CNFETs** for ultra-low-voltage efficiency and **biological supercapacitors** that blur the line between the device and the biological environment. As these technologies mature, they will enable a new class of "invisible" implants that operate indefinitely with minimal thermal footprint.

---

### References
[cite: 1] PMC8553224 - Implantable device power management circuit topologies efficiency vs size.
[cite: 2] ResearchGate - Power Approaches for Implantable Medical Devices.
[cite: 6] NCBI Bookshelf - Thermal limits for implantable medical devices power density.
[cite: 3] Electronics Cooling - Thermal Challenges with Wearable and Implantable Electronic Devices.
[cite: 7] PMC10467159 - Thermal limits for implantable medical devices power density.
[cite: 8] MDPI - Power management circuits implantable devices volume power density constraints.
[cite: 32] PMC4701313 - Power management circuits implantable devices volume power density constraints.
[cite: 30] IEEE Xplore - Power management unit architecture optimization for biomedical implants.
[cite: 31] ResearchGate - Design and Optimization of Ultrasonic Wireless Power Transmission Links.
[cite: 18] ResearchGate - Efficient RF-to-DC Converters for Biomedical Implantable Devices.
[cite: 16] UC Berkeley Tech Report - Switched-capacitor DC-DC power converters.
[cite: 17] UC Berkeley - Switched-capacitor converter implantable medical devices efficiency vs volume.
[cite: 12] NYCU Library - Single-Inductor Multiple-Output (SIMO) converter implantable devices.
[cite: 9] Georgia Tech - Single-Inductor Multiple-Output (SIMO) converter implantable devices.
[cite: 13] NCHU - Single-Inductor Multiple-Output (SIMO) converter implantable devices.
[cite: 14] MDPI - Single-Inductor Multiple-Output (SIMO) converter implantable devices.
[cite: 33] Large Battery Blog - Adaptive power scaling implantable devices battery life safety.
[cite: 28] PMC9161283 - Active thermal monitoring and management circuits.
[cite: 34] ResearchGate - Temperature Control and Monitoring System for Implant Medical Devices.
[cite: 20] ResearchGate - Optimal Supercapacitor Size to Enhance Battery Life.
[cite: 23] Medical Design Briefs - Supercapacitor could make implantables battery-free.
[cite: 25] Frontiers in Electronics - Active charge balancing techniques for neural stimulators safety.
[cite: 35] ResearchGate - Stand-Alone Broad Frequency Range Charge-Balancing System.
[cite: 21] Serials Journals - Hybrid energy storage system circuit topology.
[cite: 29] NSF PAR - Thermal feedback loop power management implantable devices.
[cite: 1] PMC8553224 - Thermal feedback loop power management implantable devices.
[cite: 4] IEEE Xplore - Active charge balancing neural stimulator volume blocking capacitors.
[cite: 5] PMC6711758 - Active charge balancing neural stimulator volume blocking capacitors.
[cite: 26] Semantic Scholar - Active charge balancing neural stimulator volume blocking capacitors.
[cite: 15] ResearchGate - SIMO converter implantable 94.4% efficiency.
[cite: 19] ResearchGate - CNTFET-based Digital Arithmetic Circuit Designs.
[cite: 23] Medical Design Briefs - Biological supercapacitor 1 µm thick implantable.
[cite: 24] ResearchGate - Biological supercapacitor 1 µm thick implantable.
[cite: 22] Chalmers Research - Hybrid energy storage implantable battery 5 years 7 years.
[cite: 10] ResearchGate - Safety of multi-channel stimulation implants.
[cite: 11] MDPI - Active charge balancing implantable blocking capacitor volume.
[cite: 27] IEEE Xplore - Active charge balancing implantable blocking capacitor volume.
[cite: 36] PMC10825050 - Implantable battery life 5 years 7 years supercapacitor.
[cite: 22] Chalmers Research - Implantable battery life 5 years 7 years supercapacitor.

**Sources:**
1. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBv3FIjWGhnb-GORNCu3PbPPKcf0UYEjwkFcbIjcyBciOTyA4zPM0Ms4xfaeCFdcsKi9c6SPeqjRlsdZHjcj3_FqPpNKDEtd6ifvkZOvNMJBKvebiTE8XSy3xLiXEZjJYOY3MCBACi)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrctnq_TqHdaOXiROpXcLE-mA9HvPpTmFH_705FLDbWhOEC8Ot5JMi61wcPi7HzbQj0ATRm4yHbFDzk1dRI0hTFgA2_GiVZkJ65bOugss8Tr9XEy6kvqR8P7B3-l5Lm7thYX6s-wgRV8Wo8KBE275XSHzoJWId13jhc0ITqlzhYuTZSwZFuVJbKbf3t5HpfDnD2tQYiABbSLA=)
3. [electronics-cooling.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuTUyyu18PkSZFpXP_5tpVo300dEPO8H668yauzCFvALZKRMHwSEdCjPWwEyi95OMQa6KMpCBzJGaKZVlywVtfb4VGoK9vSy7oFpstd1dwr2bCHHDs371pS2MMPpX2XuSt1K0MRM9Q8aY6y3E3-emnNXxtdry0tIGydkphL6QdRZ8V1btcGV0ZK_EEo_jJubTvrwZsy66mNHbaYz3wP9pJdgN_J1vxnN9subCViHM73A54UHE=)
4. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4MxspEX5my5xT44_MyZE4aiNPtTPUhDqz_Wk-ocBqZg9L5BXdFE-IZYg8qmj3VN1tEKA5E6O8Ivh8IiaoCYwXvq_irg73DiIrtMGPqb7n9CcTxMGy8NK2uAxaOTSZvtbBX1w=)
5. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRUxERmLNW2BfAypAk3ZJ7AtetRWr4CI25Nkp3m3S8PUXPJgxjxomZBI-kk4X8c8143KQHV1969um4f-7kYHvsZsZA7pqh8JKREi8UIBdn4doh-I7WeUOI7RDTQWIB93BJdcZoFBV6)
6. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEE0M_0X3F9hO_YHRaagvA49_wq1KKFAMCTbiGCvFX9-HYMVPNd-_6diZb42f2ThtRfZ3are7_2GPrrb0poKau5RaxhnRks3QhzKoAW56U2lb6hw-P1q_EreZdlRlcbn-8G)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_Ob_gFqh1lWGeWBbQTL14TiqqqDj09KMV2MKM3yAWvolMwP_UfEV35oIGjpsjUjxoqhIUU5f4cHwmu_GZMGrnkSaSWu6R_O0yQKcTjK1zUkMqBczSzufAPnwHy88YSPS-KN6mdJHuaw==)
8. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjHUkRXWDU4721c51RVHbTfhbyiZIQbgYHOeO1RBn0brP0Uinp81KBzkNGgqP3-W9QnhKUFcrDgyoQnUD1ZEIR8pqfY41NuXn8DhgHSOOorqNXrV1TRl78PS4OCDca)
9. [gatech.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHk1EyW0cBYhpkHFfJw511b4fXns0ThXGKtc3hwYAwLTqEpGNxNKmsv_JCyQfDDqaK38hUm8zEzvlnEFG63Py_-hdk56TU_KeSaU5jkOn3JUyj8BFkhtLhWof8XHEExZfUHrWAAGHi3y13RkdEGQ8U82NBAklk=)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHI2sDO_5CNRep--KzFl_7k_bJdF33FyPPriwn696uJJixTSl2apBFOY8dq16xVyrSD3AMomuDODZsFpfMPGCZITmzoRu1jg36dVIQs6wh7cbB9F2__B3VyeqYgQbEdSQxXlIBTsrlposAjtFbsjQwz_H2vCz2W6r14N1UVvHcXt8AJLiH0EHPh4FCZj24ri_0H4Y6qOblfHz9z4iOBjs4634o2SmWpAr3Y4JkNH5bDDXvRuCNmSbjWv3EqVoez80kNfNrNKbaQQJa_3jdiAlvZdEWP1UiEoinbDq0SpgoP5iyJos6-UluvN2ow)
11. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlgfrWDZ4XgR1Dw8ACDfueQnvxjPF2BSrXC0xJa8TfxIQyE9bPPr3VI-ZZE_F9oJUSbLvoXFqvxTHWLYlbWwSxmiXs_P-9Cps_2IluFLK_zzzjHtwYH9qrdI0M9qT7)
12. [nycu.edu.tw](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCkAzueCWdkftrI_Q2MoUu9NoyE0MxTf3jcuBn6c5eZs0Kw7sqPhVQdtFXYYk4H6cpB6BlTURZgCn2Kf1ttovI7YO65sXIC1m6p9I3j3WCQsYfNc5urzfKBebwEliJADyyTl15oSv1SVdhOg98tGGa0begonXKRdoOTcjQ)
13. [nchu.edu.tw](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzzujqa8rDwlTrduFmPIgU92UiM-9lAZqgVu3lB-vYPckZCkupQ3NHMn-c2lQjXisz1XkLhJqbYhXoKNdkQpVXKDZmQA73skT-Kb-T-Kg1eH-KfHNjBOxTtKgcnmHPDEBLEM9r)
14. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVzqV1AeX-Dm_8D4_9yCloM6QAOcV-Ko_wTu6ysajdLCuFPMQop2C0cHDnxQXedNXrgZtrPS6bK3SgoKXRD2bv9Bi2zddK7ZTT8QDPl834ilUmKWksE6lheLQKjAE=)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4vtmjoBR8yt9abmma6BcZKG90spZns1DeNRtYUeVStoQ_UdElnCAbfYElGsJ52pDp19QZN7VBXF1b97zPq45Z-ZFTFeZad3osw3pY5ipGy3bxNVTrvXp0Sdh4rYV3YyFC-HUC-EYexnXQ5eAjF2cp8F3Sh1AQeezpmKqnQOgVfyfIH6oH59lbaI_SZLK98QgGSXa50gaETRXp1igsNHxBOY6UGGPUFhQJ99CWRR0iG4NcY0AozlDEq3wESJkm2FtEG9d7vgPMeaDi9VYSIU-08KUEq_TAPvQU8DFIpA4gZtsGE0c=)
16. [berkeley.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdbUyAKk3M_ZQa7iB36i_tx1_3SnGuXNu9Ma1Wlc5uIa_km9fMUEFA5k89TkTBy0cVu-tn8dz3olpzEkoqHvn0Hu1sRRXCa0go8se37FOGiRBHWfLyQYQm892ZMuF7GSzvsOe6hLRz2tmf_6w1pftC0XlzaJM0dp8=)
17. [berkeley.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeZgoMpCYKqr5OtqL3T_nOJRcANPZ-RDIOWPztjpiVVacqbKJ_kmhO6jv_oPY34oigBpT2kjPzYNylI-DPQljt_F7i87Dz-kbYRYmvaCNcG8KPRnf-CTJY6WqdVer_65iLkqYgiTz_ulQjfwa3ahCyAdokoGP8D3E=)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1ni5ZlzfppFbD327hAwymhJFyVybyJyAxf2ploW7J0ec5VqU14SZDrPjaysVL2geb0UqU9O7nfR7cCYLXG_uNFR7fHtczGK8WbEWejusL1hdW9HSqFqVw9Tu-3V62glL-4QlEZzkXp1yCN9grTsmgxgQ2b9QjWcQRA0ZGFm2kKUvRELKL1wgb_DWTy2qvQCXzzojnVTXLT5A_oFf3WOnVYmNr3eY1-4A3)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQMhjRF-FTPMtTOUqfqaMTEGMMSyhcXQPDqlqRO69uAoCTHTZN-fMQzG05CTxc9zNbmg6LcbCbxB3AcrtH9RvV3F73UpXAbNggd_xROUcLsOj0R8MsTwNQiRys5DQBqZbMO2ekggF0Kn5XWbERCmcOUzR1G73qT3xcTW3GZ2aAw_VyRb4dbDUDlWF4IzEf_gwzWerRI7k6vGcl7j6tGDzdB6WgZbafnboe9J6wW1mwPqN4-agYzXiq6ag6-LqOSz9fazS2)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzi5Sj57rY8K8FsD33u9ZrZJrXIUk5sHltFbd5e6o-lKXaqTF6E0kw-LIMDp3wTuTHxrB_gLa1wGyU3D2VhK_jTuyPpJBQ5Fw8adbXdg724j6ydKwxvnHq0q51i_qTQvS2V6gLgcQ0IxRAJFoSdeD1rGWe7qzV2hVEPIYUjeXHtAv5nY82rLplb7sj4wpkT3c18FAgepUDvBREFmzfoo2eRUfTnOpS8hxX3Alt0opm3lzIOaAnUsBdeNTL4SHndh4IWhnygx0=)
21. [serialsjournals.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaBwGgcWqhJCgLtTcEsXqWIFDjgPYxl0Z4RJFecvJJh-Gh6K7RNvLFmV-jAjZQmL0TVogY7mjYZropNAk2LISNSXRVNDQe-T5ldfBPkqo-mZqUwbtdtIQuZA46jTxz36ojQBYZBfZ2)
22. [chalmers.se](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyagO455F4-L-ZS4mwJNzbnUaeKrhfER0uPl9o4Vrh-cYzH5dF75xND_eTDSBg_Cq81opn4KJoCo85eN3dlF9uzJ3LIkCdGndXa9Z97_76Tg4l1V_BqjrROXYeecxDNxIz3kCnEA8nf0OOqszs7pELzpOjwPgyfZgYi3fTYlU=)
23. [medicaldesignbriefs.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLAbsBEVHmQR0G8p_h30FGQqWwX_M9joLWPLAk0XN9OZR5Jrv89FeLsryb0o6t32wDEzI5n4-WRzTCDdjVKMHQkDm6qfIxdh2ULpF6XVN1HYVuiMUgVIVMDyzStmhYGfOgXp7clsgdY7t3pGBHxUXr6oWsn9S0JH5LeIXVxrrz9mexhlC7VpDBbHRZ9Lng9W7y4HyZH_bgeiefzjcCkcdvrKlk8EB_AGb4r7wCUbEuyZ3IJcNpCrX7sXgVnwY=)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7ieV-G_X3L159VhJaqjIkiAPufzdb4ZxFq0C-_73QnRi3SVj4UztffqC-1Db9hJCXv5p4cRa9Zs3Q04IPw-WwnTh_xtx3HWi3sq0QUQe_K4O3LuNytMG8-50GLwnX0dS3OrqlZbPKPZlNAlbQazQxXbi5c_zIn2QwTwnfbvKnoi9jGNidsh5si8n0ryqfWByjX6ekQ7E1Xs-SLxvYfqgufTkGYpKLm3fxQAEZWi0cZvvS2hpOPKVaExj4-ul2A4cewI2ZPHkhidpzdqdTyJEcmaE=)
25. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFu6I4YRks2S5R8IHBVuowNDgYPBBCZA7wz5Qcw-j0S7XTvRuuEebvJH-RYlBKZFfO7zqFmrqiFGgC7yMxOiCm7IUtOzIm2Zg2ihhTmWcsS6-RX9IJaBLHXvZ77bTA6-lUt_5W1j7qYbFykM8_SUJvqKXju4qZDFBi-_MYIIMZa9Nzr4TAUgqh6wCoKAPoU)
26. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEE0YiwQdzh4qnIKr3ZEVOPZMNL4Mu3EPgKYpVyu2SLWAxOPCQaiuYFJHz6rus0xYpUI1gCCTsLe5qISaLrjppxtm04-vlhnOGUKVfUvaxAA0bpHVMpoV9OQNazPijOmx2llC4QVPGdzgk7chiZgYCn7auSMBTOWb21yIYrVWqLFXaYa8kNxwCjodAnpUfK-Vf_uIXFs7e9zjsePNrpt_jH86zT7vuqTebGf3bCwAGUZC0xAwDwKBSkocfx2on5FJVD7PIVlHxBYzgQ_PeKNUDTmg==)
27. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzHNG_WJ2JNCJHKpwQyQEJ9bt2hIs7IvmvoEBM0IOYw6w86EGHx8kBvuhookag3p-I-QW7fgnFUCOdJZuVpIIc3kt7QZ3oms0WPeRCP36OKTwHzMhAKxE8V-d6GYK_M7bL8rJMRHF1qUMp4chpRU-z02dgHQ==)
28. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRSnkQTsYh4Pg7ieFe_Kx420-LXXN87V5XK6SC4RNsSJhKNuPiw4zTc3XeqF14ykz3gXSxR7WLlai9g47QV1g13jvvEU9m2DnBpb_Ks4iPg2TnY84-KuZG8woEIdyPQNcoY1f5HeEP)
29. [nsf.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEr9od4BoVz-ts64tZ4HswwrHBbvIG80KOryYbu-j8rfKMdYe47NGkz8Pxbz294aowWP3YB3TJEDjZ8Z8m8BMv3lObkCApJC9kiYU_XVSHP33GlW-u4GSgLbbhPIIIZBao=)
30. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGD4JckgrSsUC1QYrhG4p2_fcvtwAVNxaWsp1OLmfmwNsmKXDgOU6nd8iNJGsGBaLQCd1oxW5lwZ6jpn4bxCbOLEfQSodKdP2PYrOIJ19z_VddQkiLkYcpwRIzZStqB2E5cT4Ah)
31. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTZZDEM7lJ437Ag4SJrXEI0CzB_nE1CnosEdfVonytKZFjaUsbj5mtaQXb1rOEV3oml1CU-N9uRR3sIlfUVg-ZBJPQ3xvQSHFiqk-oJ7ubhS29ONkkQcr7ZA3Cc8-gCgQwqzbGYAPJzw0ECTyRYlDUmrbExTXyJzJrAPqGkM6TtS-wWgWAq0uZvm3OvTVaDNeaZYx750iSAiV_Sit_Id0mA6zFzyxTkuJnCgL1hte5CRfZEZmenI2kJ-GL_cgDa1my1KE6_5Jxw4aZ_kS64JmP-zodv7RapCQTuA==)
32. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgmsNrpTU9CiXJc4IdCyXXLq6ZYD2GG97f0kE0zTT4jIgeO1hL4xrbdYWm73yROU6IMZJ2_9PCHZW09tnGoztNGpRQqGnjgy-Lw62-IdQrkSWptPfvlJxCTZ_bJbXtdv6xJJkGgEDD)
33. [large-battery.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV9V4aL2ftHXUpfYmlz1ykfbRznQSLXkn3YUwhGjPPxlh4TESMEG42amKJ9212OzgSkD1im1ubpZFyW2GIaSn7X-MW2LhGfoUPPLEP_AdUfvaAvz2fQY_VfwKlme_550ldjqb6ScoG3Tum8W-WsrwtcbE1Y3VpqFVOEiuQE_qGs_I67bdt5OOKkqrNjRh9qGr1pILPV5Ub-3A-tVbU)
34. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGdxRrEMM1UZMGHLKFpFX7kcxhKt0noV348FwG1_23TMk_SPDJopOvls1XyBHo-b-UNQ_KkNIKfYxDEOAPDDq-G1ZgJ8iI6w1Az2WyhRX0y_IqwMyJL1MXZwlORteTodiOgR_7BH7gZ0OfUop1kQgsOjUrGnJDkxZKnN7Vfp8HD0KFZXBwA6Q3gtvo20Awcy532pQuPe4WQeb4fvVXXls-bs5euZHNj3aRt6mjOkL-0fLf_KoMgtXJvDueXxydDxPu4clY8sk=)
35. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6No3PJETqepHO-qSSCotg-LnJtLHXGpKkz0zi4uyDUikgyLLK-YW_ZsZPPuQUzlOFvzq1JIHo70XuRNBZRKgueBooGcn1ViZh8k8yRHz8OixMAsySlipMYCLEBsouJOW6LQUeSd4Jvl0VlFeb7mH8YLrkf2k4R96CweSm7EHkh9DpkUXk8_b_vecXFhzsAAchNjG34CyWBQQ2i21O_tkOYRgOxCzbTxvfIWCberErwO7580YWNNzLUgr1sIAF1UWaTRHCAJApLNujSbAh4Mnv7UtPfWZgsDNfWm4bxz2y4kxzAODmoe1ftJNDeGGer17hsFOP4LfPg2H2UlEqcJZo8Enmz_19lU8_I_qGDsr1WpSlVJNYGj0WET86qGJiLJk36YnTapk9kQLqBMpax6uTS6P5BTmZdRzmJrYX3HQK3bDqy_8H71g=)
36. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcWDlj9SlXw50E5jI3blmunPgEi5xES79GD1exmGCWyJK4dzIa8HzzqYyIP6ndXHMb03dw0bW5Ro_U_qqx4hS2OfK8KRqEPXiE0BAzXl-KERoyi4eBREh-nff5Ng6MvkGd2i1TcPYLqw==)


## Annotations
Annotation(end_index=1744, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBv3FIjWGhnb-GORNCu3PbPPKcf0UYEjwkFcbIjcyBciOTyA4zPM0Ms4xfaeCFdcsKi9c6SPeqjRlsdZHjcj3_FqPpNKDEtd6ifvkZOvNMJBKvebiTE8XSy3xLiXEZjJYOY3MCBACi', start_index=1735)
Annotation(end_index=2143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuTUyyu18PkSZFpXP_5tpVo300dEPO8H668yauzCFvALZKRMHwSEdCjPWwEyi95OMQa6KMpCBzJGaKZVlywVtfb4VGoK9vSy7oFpstd1dwr2bCHHDs371pS2MMPpX2XuSt1K0MRM9Q8aY6y3E3-emnNXxtdry0tIGydkphL6QdRZ8V1btcGV0ZK_EEo_jJubTvrwZsy66mNHbaYz3wP9pJdgN_J1vxnN9subCViHM73A54UHE=', start_index=2131)
Annotation(end_index=2143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrctnq_TqHdaOXiROpXcLE-mA9HvPpTmFH_705FLDbWhOEC8Ot5JMi61wcPi7HzbQj0ATRm4yHbFDzk1dRI0hTFgA2_GiVZkJ65bOugss8Tr9XEy6kvqR8P7B3-l5Lm7thYX6s-wgRV8Wo8KBE275XSHzoJWId13jhc0ITqlzhYuTZSwZFuVJbKbf3t5HpfDnD2tQYiABbSLA=', start_index=2131)
Annotation(end_index=2626, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4MxspEX5my5xT44_MyZE4aiNPtTPUhDqz_Wk-ocBqZg9L5BXdFE-IZYg8qmj3VN1tEKA5E6O8Ivh8IiaoCYwXvq_irg73DiIrtMGPqb7n9CcTxMGy8NK2uAxaOTSZvtbBX1w=', start_index=2614)
Annotation(end_index=2626, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRUxERmLNW2BfAypAk3ZJ7AtetRWr4CI25Nkp3m3S8PUXPJgxjxomZBI-kk4X8c8143KQHV1969um4f-7kYHvsZsZA7pqh8JKREi8UIBdn4doh-I7WeUOI7RDTQWIB93BJdcZoFBV6', start_index=2614)
Annotation(end_index=3524, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEE0M_0X3F9hO_YHRaagvA49_wq1KKFAMCTbiGCvFX9-HYMVPNd-_6diZb42f2ThtRfZ3are7_2GPrrb0poKau5RaxhnRks3QhzKoAW56U2lb6hw-P1q_EreZdlRlcbn-8G', start_index=3512)
Annotation(end_index=3524, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_Ob_gFqh1lWGeWBbQTL14TiqqqDj09KMV2MKM3yAWvolMwP_UfEV35oIGjpsjUjxoqhIUU5f4cHwmu_GZMGrnkSaSWu6R_O0yQKcTjK1zUkMqBczSzufAPnwHy88YSPS-KN6mdJHuaw==', start_index=3512)
Annotation(end_index=3742, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEE0M_0X3F9hO_YHRaagvA49_wq1KKFAMCTbiGCvFX9-HYMVPNd-_6diZb42f2ThtRfZ3are7_2GPrrb0poKau5RaxhnRks3QhzKoAW56U2lb6hw-P1q_EreZdlRlcbn-8G', start_index=3733)
Annotation(end_index=3919, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrctnq_TqHdaOXiROpXcLE-mA9HvPpTmFH_705FLDbWhOEC8Ot5JMi61wcPi7HzbQj0ATRm4yHbFDzk1dRI0hTFgA2_GiVZkJ65bOugss8Tr9XEy6kvqR8P7B3-l5Lm7thYX6s-wgRV8Wo8KBE275XSHzoJWId13jhc0ITqlzhYuTZSwZFuVJbKbf3t5HpfDnD2tQYiABbSLA=', start_index=3910)
Annotation(end_index=4222, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_Ob_gFqh1lWGeWBbQTL14TiqqqDj09KMV2MKM3yAWvolMwP_UfEV35oIGjpsjUjxoqhIUU5f4cHwmu_GZMGrnkSaSWu6R_O0yQKcTjK1zUkMqBczSzufAPnwHy88YSPS-KN6mdJHuaw==', start_index=4213)
Annotation(end_index=4494, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjHUkRXWDU4721c51RVHbTfhbyiZIQbgYHOeO1RBn0brP0Uinp81KBzkNGgqP3-W9QnhKUFcrDgyoQnUD1ZEIR8pqfY41NuXn8DhgHSOOorqNXrV1TRl78PS4OCDca', start_index=4485)
Annotation(end_index=4965, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHI2sDO_5CNRep--KzFl_7k_bJdF33FyPPriwn696uJJixTSl2apBFOY8dq16xVyrSD3AMomuDODZsFpfMPGCZITmzoRu1jg36dVIQs6wh7cbB9F2__B3VyeqYgQbEdSQxXlIBTsrlposAjtFbsjQwz_H2vCz2W6r14N1UVvHcXt8AJLiH0EHPh4FCZj24ri_0H4Y6qOblfHz9z4iOBjs4634o2SmWpAr3Y4JkNH5bDDXvRuCNmSbjWv3EqVoez80kNfNrNKbaQQJa_3jdiAlvZdEWP1UiEoinbDq0SpgoP5iyJos6-UluvN2ow', start_index=4952)
Annotation(end_index=4965, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHk1EyW0cBYhpkHFfJw511b4fXns0ThXGKtc3hwYAwLTqEpGNxNKmsv_JCyQfDDqaK38hUm8zEzvlnEFG63Py_-hdk56TU_KeSaU5jkOn3JUyj8BFkhtLhWof8XHEExZfUHrWAAGHi3y13RkdEGQ8U82NBAklk=', start_index=4952)
Annotation(end_index=5437, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRUxERmLNW2BfAypAk3ZJ7AtetRWr4CI25Nkp3m3S8PUXPJgxjxomZBI-kk4X8c8143KQHV1969um4f-7kYHvsZsZA7pqh8JKREi8UIBdn4doh-I7WeUOI7RDTQWIB93BJdcZoFBV6', start_index=5424)
Annotation(end_index=5437, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlgfrWDZ4XgR1Dw8ACDfueQnvxjPF2BSrXC0xJa8TfxIQyE9bPPr3VI-ZZE_F9oJUSbLvoXFqvxTHWLYlbWwSxmiXs_P-9Cps_2IluFLK_zzzjHtwYH9qrdI0M9qT7', start_index=5424)
Annotation(end_index=6225, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCkAzueCWdkftrI_Q2MoUu9NoyE0MxTf3jcuBn6c5eZs0Kw7sqPhVQdtFXYYk4H6cpB6BlTURZgCn2Kf1ttovI7YO65sXIC1m6p9I3j3WCQsYfNc5urzfKBebwEliJADyyTl15oSv1SVdhOg98tGGa0begonXKRdoOTcjQ', start_index=6211)
Annotation(end_index=6225, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzzujqa8rDwlTrduFmPIgU92UiM-9lAZqgVu3lB-vYPckZCkupQ3NHMn-c2lQjXisz1XkLhJqbYhXoKNdkQpVXKDZmQA73skT-Kb-T-Kg1eH-KfHNjBOxTtKgcnmHPDEBLEM9r', start_index=6211)
Annotation(end_index=6699, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4vtmjoBR8yt9abmma6BcZKG90spZns1DeNRtYUeVStoQ_UdElnCAbfYElGsJ52pDp19QZN7VBXF1b97zPq45Z-ZFTFeZad3osw3pY5ipGy3bxNVTrvXp0Sdh4rYV3YyFC-HUC-EYexnXQ5eAjF2cp8F3Sh1AQeezpmKqnQOgVfyfIH6oH59lbaI_SZLK98QgGSXa50gaETRXp1igsNHxBOY6UGGPUFhQJ99CWRR0iG4NcY0AozlDEq3wESJkm2FtEG9d7vgPMeaDi9VYSIU-08KUEq_TAPvQU8DFIpA4gZtsGE0c=', start_index=6685)
Annotation(end_index=6699, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVzqV1AeX-Dm_8D4_9yCloM6QAOcV-Ko_wTu6ysajdLCuFPMQop2C0cHDnxQXedNXrgZtrPS6bK3SgoKXRD2bv9Bi2zddK7ZTT8QDPl834ilUmKWksE6lheLQKjAE=', start_index=6685)
Annotation(end_index=6918, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4vtmjoBR8yt9abmma6BcZKG90spZns1DeNRtYUeVStoQ_UdElnCAbfYElGsJ52pDp19QZN7VBXF1b97zPq45Z-ZFTFeZad3osw3pY5ipGy3bxNVTrvXp0Sdh4rYV3YyFC-HUC-EYexnXQ5eAjF2cp8F3Sh1AQeezpmKqnQOgVfyfIH6oH59lbaI_SZLK98QgGSXa50gaETRXp1igsNHxBOY6UGGPUFhQJ99CWRR0iG4NcY0AozlDEq3wESJkm2FtEG9d7vgPMeaDi9VYSIU-08KUEq_TAPvQU8DFIpA4gZtsGE0c=', start_index=6908)
Annotation(end_index=7361, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdbUyAKk3M_ZQa7iB36i_tx1_3SnGuXNu9Ma1Wlc5uIa_km9fMUEFA5k89TkTBy0cVu-tn8dz3olpzEkoqHvn0Hu1sRRXCa0go8se37FOGiRBHWfLyQYQm892ZMuF7GSzvsOe6hLRz2tmf_6w1pftC0XlzaJM0dp8=', start_index=7351)
Annotation(end_index=7794, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdbUyAKk3M_ZQa7iB36i_tx1_3SnGuXNu9Ma1Wlc5uIa_km9fMUEFA5k89TkTBy0cVu-tn8dz3olpzEkoqHvn0Hu1sRRXCa0go8se37FOGiRBHWfLyQYQm892ZMuF7GSzvsOe6hLRz2tmf_6w1pftC0XlzaJM0dp8=', start_index=7780)
Annotation(end_index=7794, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeZgoMpCYKqr5OtqL3T_nOJRcANPZ-RDIOWPztjpiVVacqbKJ_kmhO6jv_oPY34oigBpT2kjPzYNylI-DPQljt_F7i87Dz-kbYRYmvaCNcG8KPRnf-CTJY6WqdVer_65iLkqYgiTz_ulQjfwa3ahCyAdokoGP8D3E=', start_index=7780)
Annotation(end_index=8358, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1ni5ZlzfppFbD327hAwymhJFyVybyJyAxf2ploW7J0ec5VqU14SZDrPjaysVL2geb0UqU9O7nfR7cCYLXG_uNFR7fHtczGK8WbEWejusL1hdW9HSqFqVw9Tu-3V62glL-4QlEZzkXp1yCN9grTsmgxgQ2b9QjWcQRA0ZGFm2kKUvRELKL1wgb_DWTy2qvQCXzzojnVTXLT5A_oFf3WOnVYmNr3eY1-4A3', start_index=8344)
Annotation(end_index=8358, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQMhjRF-FTPMtTOUqfqaMTEGMMSyhcXQPDqlqRO69uAoCTHTZN-fMQzG05CTxc9zNbmg6LcbCbxB3AcrtH9RvV3F73UpXAbNggd_xROUcLsOj0R8MsTwNQiRys5DQBqZbMO2ekggF0Kn5XWbERCmcOUzR1G73qT3xcTW3GZ2aAw_VyRb4dbDUDlWF4IzEf_gwzWerRI7k6vGcl7j6tGDzdB6WgZbafnboe9J6wW1mwPqN4-agYzXiq6ag6-LqOSz9fazS2', start_index=8344)
Annotation(end_index=8541, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQMhjRF-FTPMtTOUqfqaMTEGMMSyhcXQPDqlqRO69uAoCTHTZN-fMQzG05CTxc9zNbmg6LcbCbxB3AcrtH9RvV3F73UpXAbNggd_xROUcLsOj0R8MsTwNQiRys5DQBqZbMO2ekggF0Kn5XWbERCmcOUzR1G73qT3xcTW3GZ2aAw_VyRb4dbDUDlWF4IzEf_gwzWerRI7k6vGcl7j6tGDzdB6WgZbafnboe9J6wW1mwPqN4-agYzXiq6ag6-LqOSz9fazS2', start_index=8531)
Annotation(end_index=9342, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaBwGgcWqhJCgLtTcEsXqWIFDjgPYxl0Z4RJFecvJJh-Gh6K7RNvLFmV-jAjZQmL0TVogY7mjYZropNAk2LISNSXRVNDQe-T5ldfBPkqo-mZqUwbtdtIQuZA46jTxz36ojQBYZBfZ2', start_index=9328)
Annotation(end_index=9342, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzi5Sj57rY8K8FsD33u9ZrZJrXIUk5sHltFbd5e6o-lKXaqTF6E0kw-LIMDp3wTuTHxrB_gLa1wGyU3D2VhK_jTuyPpJBQ5Fw8adbXdg724j6ydKwxvnHq0q51i_qTQvS2V6gLgcQ0IxRAJFoSdeD1rGWe7qzV2hVEPIYUjeXHtAv5nY82rLplb7sj4wpkT3c18FAgepUDvBREFmzfoo2eRUfTnOpS8hxX3Alt0opm3lzIOaAnUsBdeNTL4SHndh4IWhnygx0=', start_index=9328)
Annotation(end_index=9669, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzi5Sj57rY8K8FsD33u9ZrZJrXIUk5sHltFbd5e6o-lKXaqTF6E0kw-LIMDp3wTuTHxrB_gLa1wGyU3D2VhK_jTuyPpJBQ5Fw8adbXdg724j6ydKwxvnHq0q51i_qTQvS2V6gLgcQ0IxRAJFoSdeD1rGWe7qzV2hVEPIYUjeXHtAv5nY82rLplb7sj4wpkT3c18FAgepUDvBREFmzfoo2eRUfTnOpS8hxX3Alt0opm3lzIOaAnUsBdeNTL4SHndh4IWhnygx0=', start_index=9659)
Annotation(end_index=9919, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyagO455F4-L-ZS4mwJNzbnUaeKrhfER0uPl9o4Vrh-cYzH5dF75xND_eTDSBg_Cq81opn4KJoCo85eN3dlF9uzJ3LIkCdGndXa9Z97_76Tg4l1V_BqjrROXYeecxDNxIz3kCnEA8nf0OOqszs7pELzpOjwPgyfZgYi3fTYlU=', start_index=9909)
Annotation(end_index=10401, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLAbsBEVHmQR0G8p_h30FGQqWwX_M9joLWPLAk0XN9OZR5Jrv89FeLsryb0o6t32wDEzI5n4-WRzTCDdjVKMHQkDm6qfIxdh2ULpF6XVN1HYVuiMUgVIVMDyzStmhYGfOgXp7clsgdY7t3pGBHxUXr6oWsn9S0JH5LeIXVxrrz9mexhlC7VpDBbHRZ9Lng9W7y4HyZH_bgeiefzjcCkcdvrKlk8EB_AGb4r7wCUbEuyZ3IJcNpCrX7sXgVnwY=', start_index=10387)
Annotation(end_index=10401, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7ieV-G_X3L159VhJaqjIkiAPufzdb4ZxFq0C-_73QnRi3SVj4UztffqC-1Db9hJCXv5p4cRa9Zs3Q04IPw-WwnTh_xtx3HWi3sq0QUQe_K4O3LuNytMG8-50GLwnX0dS3OrqlZbPKPZlNAlbQazQxXbi5c_zIn2QwTwnfbvKnoi9jGNidsh5si8n0ryqfWByjX6ekQ7E1Xs-SLxvYfqgufTkGYpKLm3fxQAEZWi0cZvvS2hpOPKVaExj4-ul2A4cewI2ZPHkhidpzdqdTyJEcmaE=', start_index=10387)
Annotation(end_index=11157, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFu6I4YRks2S5R8IHBVuowNDgYPBBCZA7wz5Qcw-j0S7XTvRuuEebvJH-RYlBKZFfO7zqFmrqiFGgC7yMxOiCm7IUtOzIm2Zg2ihhTmWcsS6-RX9IJaBLHXvZ77bTA6-lUt_5W1j7qYbFykM8_SUJvqKXju4qZDFBi-_MYIIMZa9Nzr4TAUgqh6wCoKAPoU', start_index=11144)
Annotation(end_index=11157, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4MxspEX5my5xT44_MyZE4aiNPtTPUhDqz_Wk-ocBqZg9L5BXdFE-IZYg8qmj3VN1tEKA5E6O8Ivh8IiaoCYwXvq_irg73DiIrtMGPqb7n9CcTxMGy8NK2uAxaOTSZvtbBX1w=', start_index=11144)
Annotation(end_index=11419, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEE0YiwQdzh4qnIKr3ZEVOPZMNL4Mu3EPgKYpVyu2SLWAxOPCQaiuYFJHz6rus0xYpUI1gCCTsLe5qISaLrjppxtm04-vlhnOGUKVfUvaxAA0bpHVMpoV9OQNazPijOmx2llC4QVPGdzgk7chiZgYCn7auSMBTOWb21yIYrVWqLFXaYa8kNxwCjodAnpUfK-Vf_uIXFs7e9zjsePNrpt_jH86zT7vuqTebGf3bCwAGUZC0xAwDwKBSkocfx2on5FJVD7PIVlHxBYzgQ_PeKNUDTmg==', start_index=11405)
Annotation(end_index=11419, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFu6I4YRks2S5R8IHBVuowNDgYPBBCZA7wz5Qcw-j0S7XTvRuuEebvJH-RYlBKZFfO7zqFmrqiFGgC7yMxOiCm7IUtOzIm2Zg2ihhTmWcsS6-RX9IJaBLHXvZ77bTA6-lUt_5W1j7qYbFykM8_SUJvqKXju4qZDFBi-_MYIIMZa9Nzr4TAUgqh6wCoKAPoU', start_index=11405)
Annotation(end_index=11670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRUxERmLNW2BfAypAk3ZJ7AtetRWr4CI25Nkp3m3S8PUXPJgxjxomZBI-kk4X8c8143KQHV1969um4f-7kYHvsZsZA7pqh8JKREi8UIBdn4doh-I7WeUOI7RDTQWIB93BJdcZoFBV6', start_index=11657)
Annotation(end_index=11670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlgfrWDZ4XgR1Dw8ACDfueQnvxjPF2BSrXC0xJa8TfxIQyE9bPPr3VI-ZZE_F9oJUSbLvoXFqvxTHWLYlbWwSxmiXs_P-9Cps_2IluFLK_zzzjHtwYH9qrdI0M9qT7', start_index=11657)
Annotation(end_index=11942, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzHNG_WJ2JNCJHKpwQyQEJ9bt2hIs7IvmvoEBM0IOYw6w86EGHx8kBvuhookag3p-I-QW7fgnFUCOdJZuVpIIc3kt7QZ3oms0WPeRCP36OKTwHzMhAKxE8V-d6GYK_M7bL8rJMRHF1qUMp4chpRU-z02dgHQ==', start_index=11928)
Annotation(end_index=11942, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlgfrWDZ4XgR1Dw8ACDfueQnvxjPF2BSrXC0xJa8TfxIQyE9bPPr3VI-ZZE_F9oJUSbLvoXFqvxTHWLYlbWwSxmiXs_P-9Cps_2IluFLK_zzzjHtwYH9qrdI0M9qT7', start_index=11928)
Annotation(end_index=12596, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEr9od4BoVz-ts64tZ4HswwrHBbvIG80KOryYbu-j8rfKMdYe47NGkz8Pxbz294aowWP3YB3TJEDjZ8Z8m8BMv3lObkCApJC9kiYU_XVSHP33GlW-u4GSgLbbhPIIIZBao=', start_index=12582)
Annotation(end_index=12596, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRSnkQTsYh4Pg7ieFe_Kx420-LXXN87V5XK6SC4RNsSJhKNuPiw4zTc3XeqF14ykz3gXSxR7WLlai9g47QV1g13jvvEU9m2DnBpb_Ks4iPg2TnY84-KuZG8woEIdyPQNcoY1f5HeEP', start_index=12582)
Annotation(end_index=12890, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEE0M_0X3F9hO_YHRaagvA49_wq1KKFAMCTbiGCvFX9-HYMVPNd-_6diZb42f2ThtRfZ3are7_2GPrrb0poKau5RaxhnRks3QhzKoAW56U2lb6hw-P1q_EreZdlRlcbn-8G', start_index=12878)
Annotation(end_index=12890, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_Ob_gFqh1lWGeWBbQTL14TiqqqDj09KMV2MKM3yAWvolMwP_UfEV35oIGjpsjUjxoqhIUU5f4cHwmu_GZMGrnkSaSWu6R_O0yQKcTjK1zUkMqBczSzufAPnwHy88YSPS-KN6mdJHuaw==', start_index=12878)
Annotation(end_index=13452, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGD4JckgrSsUC1QYrhG4p2_fcvtwAVNxaWsp1OLmfmwNsmKXDgOU6nd8iNJGsGBaLQCd1oxW5lwZ6jpn4bxCbOLEfQSodKdP2PYrOIJ19z_VddQkiLkYcpwRIzZStqB2E5cT4Ah', start_index=13438)
Annotation(end_index=13452, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTZZDEM7lJ437Ag4SJrXEI0CzB_nE1CnosEdfVonytKZFjaUsbj5mtaQXb1rOEV3oml1CU-N9uRR3sIlfUVg-ZBJPQ3xvQSHFiqk-oJ7ubhS29ONkkQcr7ZA3Cc8-gCgQwqzbGYAPJzw0ECTyRYlDUmrbExTXyJzJrAPqGkM6TtS-wWgWAq0uZvm3OvTVaDNeaZYx750iSAiV_Sit_Id0mA6zFzyxTkuJnCgL1hte5CRfZEZmenI2kJ-GL_cgDa1my1KE6_5Jxw4aZ_kS64JmP-zodv7RapCQTuA==', start_index=13438)
Annotation(end_index=13800, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGD4JckgrSsUC1QYrhG4p2_fcvtwAVNxaWsp1OLmfmwNsmKXDgOU6nd8iNJGsGBaLQCd1oxW5lwZ6jpn4bxCbOLEfQSodKdP2PYrOIJ19z_VddQkiLkYcpwRIzZStqB2E5cT4Ah', start_index=13790)
Annotation(end_index=14827, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBv3FIjWGhnb-GORNCu3PbPPKcf0UYEjwkFcbIjcyBciOTyA4zPM0Ms4xfaeCFdcsKi9c6SPeqjRlsdZHjcj3_FqPpNKDEtd6ifvkZOvNMJBKvebiTE8XSy3xLiXEZjJYOY3MCBACi', start_index=14818)
Annotation(end_index=14925, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrctnq_TqHdaOXiROpXcLE-mA9HvPpTmFH_705FLDbWhOEC8Ot5JMi61wcPi7HzbQj0ATRm4yHbFDzk1dRI0hTFgA2_GiVZkJ65bOugss8Tr9XEy6kvqR8P7B3-l5Lm7thYX6s-wgRV8Wo8KBE275XSHzoJWId13jhc0ITqlzhYuTZSwZFuVJbKbf3t5HpfDnD2tQYiABbSLA=', start_index=14916)
Annotation(end_index=15000, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEE0M_0X3F9hO_YHRaagvA49_wq1KKFAMCTbiGCvFX9-HYMVPNd-_6diZb42f2ThtRfZ3are7_2GPrrb0poKau5RaxhnRks3QhzKoAW56U2lb6hw-P1q_EreZdlRlcbn-8G', start_index=14991)
Annotation(end_index=15089, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuTUyyu18PkSZFpXP_5tpVo300dEPO8H668yauzCFvALZKRMHwSEdCjPWwEyi95OMQa6KMpCBzJGaKZVlywVtfb4VGoK9vSy7oFpstd1dwr2bCHHDs371pS2MMPpX2XuSt1K0MRM9Q8aY6y3E3-emnNXxtdry0tIGydkphL6QdRZ8V1btcGV0ZK_EEo_jJubTvrwZsy66mNHbaYz3wP9pJdgN_J1vxnN9subCViHM73A54UHE=', start_index=15080)
Annotation(end_index=15190, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_Ob_gFqh1lWGeWBbQTL14TiqqqDj09KMV2MKM3yAWvolMwP_UfEV35oIGjpsjUjxoqhIUU5f4cHwmu_GZMGrnkSaSWu6R_O0yQKcTjK1zUkMqBczSzufAPnwHy88YSPS-KN6mdJHuaw==', start_index=15181)
Annotation(end_index=15276, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjHUkRXWDU4721c51RVHbTfhbyiZIQbgYHOeO1RBn0brP0Uinp81KBzkNGgqP3-W9QnhKUFcrDgyoQnUD1ZEIR8pqfY41NuXn8DhgHSOOorqNXrV1TRl78PS4OCDca', start_index=15267)
Annotation(end_index=15374, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgmsNrpTU9CiXJc4IdCyXXLq6ZYD2GG97f0kE0zTT4jIgeO1hL4xrbdYWm73yROU6IMZJ2_9PCHZW09tnGoztNGpRQqGnjgy-Lw62-IdQrkSWptPfvlJxCTZ_bJbXtdv6xJJkGgEDD', start_index=15364)
Annotation(end_index=15478, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGD4JckgrSsUC1QYrhG4p2_fcvtwAVNxaWsp1OLmfmwNsmKXDgOU6nd8iNJGsGBaLQCd1oxW5lwZ6jpn4bxCbOLEfQSodKdP2PYrOIJ19z_VddQkiLkYcpwRIzZStqB2E5cT4Ah', start_index=15468)
Annotation(end_index=15576, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTZZDEM7lJ437Ag4SJrXEI0CzB_nE1CnosEdfVonytKZFjaUsbj5mtaQXb1rOEV3oml1CU-N9uRR3sIlfUVg-ZBJPQ3xvQSHFiqk-oJ7ubhS29ONkkQcr7ZA3Cc8-gCgQwqzbGYAPJzw0ECTyRYlDUmrbExTXyJzJrAPqGkM6TtS-wWgWAq0uZvm3OvTVaDNeaZYx750iSAiV_Sit_Id0mA6zFzyxTkuJnCgL1hte5CRfZEZmenI2kJ-GL_cgDa1my1KE6_5Jxw4aZ_kS64JmP-zodv7RapCQTuA==', start_index=15566)
Annotation(end_index=15675, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1ni5ZlzfppFbD327hAwymhJFyVybyJyAxf2ploW7J0ec5VqU14SZDrPjaysVL2geb0UqU9O7nfR7cCYLXG_uNFR7fHtczGK8WbEWejusL1hdW9HSqFqVw9Tu-3V62glL-4QlEZzkXp1yCN9grTsmgxgQ2b9QjWcQRA0ZGFm2kKUvRELKL1wgb_DWTy2qvQCXzzojnVTXLT5A_oFf3WOnVYmNr3eY1-4A3', start_index=15665)
Annotation(end_index=15767, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdbUyAKk3M_ZQa7iB36i_tx1_3SnGuXNu9Ma1Wlc5uIa_km9fMUEFA5k89TkTBy0cVu-tn8dz3olpzEkoqHvn0Hu1sRRXCa0go8se37FOGiRBHWfLyQYQm892ZMuF7GSzvsOe6hLRz2tmf_6w1pftC0XlzaJM0dp8=', start_index=15757)
Annotation(end_index=15847, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeZgoMpCYKqr5OtqL3T_nOJRcANPZ-RDIOWPztjpiVVacqbKJ_kmhO6jv_oPY34oigBpT2kjPzYNylI-DPQljt_F7i87Dz-kbYRYmvaCNcG8KPRnf-CTJY6WqdVer_65iLkqYgiTz_ulQjfwa3ahCyAdokoGP8D3E=', start_index=15837)
Annotation(end_index=15951, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCkAzueCWdkftrI_Q2MoUu9NoyE0MxTf3jcuBn6c5eZs0Kw7sqPhVQdtFXYYk4H6cpB6BlTURZgCn2Kf1ttovI7YO65sXIC1m6p9I3j3WCQsYfNc5urzfKBebwEliJADyyTl15oSv1SVdhOg98tGGa0begonXKRdoOTcjQ', start_index=15941)
Annotation(end_index=16046, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHk1EyW0cBYhpkHFfJw511b4fXns0ThXGKtc3hwYAwLTqEpGNxNKmsv_JCyQfDDqaK38hUm8zEzvlnEFG63Py_-hdk56TU_KeSaU5jkOn3JUyj8BFkhtLhWof8XHEExZfUHrWAAGHi3y13RkdEGQ8U82NBAklk=', start_index=16037)
Annotation(end_index=16142, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzzujqa8rDwlTrduFmPIgU92UiM-9lAZqgVu3lB-vYPckZCkupQ3NHMn-c2lQjXisz1XkLhJqbYhXoKNdkQpVXKDZmQA73skT-Kb-T-Kg1eH-KfHNjBOxTtKgcnmHPDEBLEM9r', start_index=16132)
Annotation(end_index=16230, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVzqV1AeX-Dm_8D4_9yCloM6QAOcV-Ko_wTu6ysajdLCuFPMQop2C0cHDnxQXedNXrgZtrPS6bK3SgoKXRD2bv9Bi2zddK7ZTT8QDPl834ilUmKWksE6lheLQKjAE=', start_index=16220)
Annotation(end_index=16318, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV9V4aL2ftHXUpfYmlz1ykfbRznQSLXkn3YUwhGjPPxlh4TESMEG42amKJ9212OzgSkD1im1ubpZFyW2GIaSn7X-MW2LhGfoUPPLEP_AdUfvaAvz2fQY_VfwKlme_550ldjqb6ScoG3Tum8W-WsrwtcbE1Y3VpqFVOEiuQE_qGs_I67bdt5OOKkqrNjRh9qGr1pILPV5Ub-3A-tVbU', start_index=16308)
Annotation(end_index=16414, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRSnkQTsYh4Pg7ieFe_Kx420-LXXN87V5XK6SC4RNsSJhKNuPiw4zTc3XeqF14ykz3gXSxR7WLlai9g47QV1g13jvvEU9m2DnBpb_Ks4iPg2TnY84-KuZG8woEIdyPQNcoY1f5HeEP', start_index=16404)
Annotation(end_index=16489, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGdxRrEMM1UZMGHLKFpFX7kcxhKt0noV348FwG1_23TMk_SPDJopOvls1XyBHo-b-UNQ_KkNIKfYxDEOAPDDq-G1ZgJ8iI6w1Az2WyhRX0y_IqwMyJL1MXZwlORteTodiOgR_7BH7gZ0OfUop1kQgsOjUrGnJDkxZKnN7Vfp8HD0KFZXBwA6Q3gtvo20Awcy532pQuPe4WQeb4fvVXXls-bs5euZHNj3aRt6mjOkL-0fLf_KoMgtXJvDueXxydDxPu4clY8sk=', start_index=16479)
Annotation(end_index=16586, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzi5Sj57rY8K8FsD33u9ZrZJrXIUk5sHltFbd5e6o-lKXaqTF6E0kw-LIMDp3wTuTHxrB_gLa1wGyU3D2VhK_jTuyPpJBQ5Fw8adbXdg724j6ydKwxvnHq0q51i_qTQvS2V6gLgcQ0IxRAJFoSdeD1rGWe7qzV2hVEPIYUjeXHtAv5nY82rLplb7sj4wpkT3c18FAgepUDvBREFmzfoo2eRUfTnOpS8hxX3Alt0opm3lzIOaAnUsBdeNTL4SHndh4IWhnygx0=', start_index=16576)
Annotation(end_index=16665, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLAbsBEVHmQR0G8p_h30FGQqWwX_M9joLWPLAk0XN9OZR5Jrv89FeLsryb0o6t32wDEzI5n4-WRzTCDdjVKMHQkDm6qfIxdh2ULpF6XVN1HYVuiMUgVIVMDyzStmhYGfOgXp7clsgdY7t3pGBHxUXr6oWsn9S0JH5LeIXVxrrz9mexhlC7VpDBbHRZ9Lng9W7y4HyZH_bgeiefzjcCkcdvrKlk8EB_AGb4r7wCUbEuyZ3IJcNpCrX7sXgVnwY=', start_index=16655)
Annotation(end_index=16753, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFu6I4YRks2S5R8IHBVuowNDgYPBBCZA7wz5Qcw-j0S7XTvRuuEebvJH-RYlBKZFfO7zqFmrqiFGgC7yMxOiCm7IUtOzIm2Zg2ihhTmWcsS6-RX9IJaBLHXvZ77bTA6-lUt_5W1j7qYbFykM8_SUJvqKXju4qZDFBi-_MYIIMZa9Nzr4TAUgqh6wCoKAPoU', start_index=16743)
Annotation(end_index=16857, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6No3PJETqepHO-qSSCotg-LnJtLHXGpKkz0zi4uyDUikgyLLK-YW_ZsZPPuQUzlOFvzq1JIHo70XuRNBZRKgueBooGcn1ViZh8k8yRHz8OixMAsySlipMYCLEBsouJOW6LQUeSd4Jvl0VlFeb7mH8YLrkf2k4R96CweSm7EHkh9DpkUXk8_b_vecXFhzsAAchNjG34CyWBQQ2i21O_tkOYRgOxCzbTxvfIWCberErwO7580YWNNzLUgr1sIAF1UWaTRHCAJApLNujSbAh4Mnv7UtPfWZgsDNfWm4bxz2y4kxzAODmoe1ftJNDeGGer17hsFOP4LfPg2H2UlEqcJZo8Enmz_19lU8_I_qGDsr1WpSlVJNYGj0WET86qGJiLJk36YnTapk9kQLqBMpax6uTS6P5BTmZdRzmJrYX3HQK3bDqy_8H71g=', start_index=16847)
Annotation(end_index=16942, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaBwGgcWqhJCgLtTcEsXqWIFDjgPYxl0Z4RJFecvJJh-Gh6K7RNvLFmV-jAjZQmL0TVogY7mjYZropNAk2LISNSXRVNDQe-T5ldfBPkqo-mZqUwbtdtIQuZA46jTxz36ojQBYZBfZ2', start_index=16932)
Annotation(end_index=17019, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEr9od4BoVz-ts64tZ4HswwrHBbvIG80KOryYbu-j8rfKMdYe47NGkz8Pxbz294aowWP3YB3TJEDjZ8Z8m8BMv3lObkCApJC9kiYU_XVSHP33GlW-u4GSgLbbhPIIIZBao=', start_index=17009)
Annotation(end_index=17099, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBv3FIjWGhnb-GORNCu3PbPPKcf0UYEjwkFcbIjcyBciOTyA4zPM0Ms4xfaeCFdcsKi9c6SPeqjRlsdZHjcj3_FqPpNKDEtd6ifvkZOvNMJBKvebiTE8XSy3xLiXEZjJYOY3MCBACi', start_index=17090)
Annotation(end_index=17182, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4MxspEX5my5xT44_MyZE4aiNPtTPUhDqz_Wk-ocBqZg9L5BXdFE-IZYg8qmj3VN1tEKA5E6O8Ivh8IiaoCYwXvq_irg73DiIrtMGPqb7n9CcTxMGy8NK2uAxaOTSZvtbBX1w=', start_index=17173)
Annotation(end_index=17276, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRUxERmLNW2BfAypAk3ZJ7AtetRWr4CI25Nkp3m3S8PUXPJgxjxomZBI-kk4X8c8143KQHV1969um4f-7kYHvsZsZA7pqh8JKREi8UIBdn4doh-I7WeUOI7RDTQWIB93BJdcZoFBV6', start_index=17267)
Annotation(end_index=17370, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEE0YiwQdzh4qnIKr3ZEVOPZMNL4Mu3EPgKYpVyu2SLWAxOPCQaiuYFJHz6rus0xYpUI1gCCTsLe5qISaLrjppxtm04-vlhnOGUKVfUvaxAA0bpHVMpoV9OQNazPijOmx2llC4QVPGdzgk7chiZgYCn7auSMBTOWb21yIYrVWqLFXaYa8kNxwCjodAnpUfK-Vf_uIXFs7e9zjsePNrpt_jH86zT7vuqTebGf3bCwAGUZC0xAwDwKBSkocfx2on5FJVD7PIVlHxBYzgQ_PeKNUDTmg==', start_index=17360)
Annotation(end_index=17470, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4vtmjoBR8yt9abmma6BcZKG90spZns1DeNRtYUeVStoQ_UdElnCAbfYElGsJ52pDp19QZN7VBXF1b97zPq45Z-ZFTFeZad3osw3pY5ipGy3bxNVTrvXp0Sdh4rYV3YyFC-HUC-EYexnXQ5eAjF2cp8F3Sh1AQeezpmKqnQOgVfyfIH6oH59lbaI_SZLK98QgGSXa50gaETRXp1igsNHxBOY6UGGPUFhQJ99CWRR0iG4NcY0AozlDEq3wESJkm2FtEG9d7vgPMeaDi9VYSIU-08KUEq_TAPvQU8DFIpA4gZtsGE0c=', start_index=17460)
Annotation(end_index=17541, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQMhjRF-FTPMtTOUqfqaMTEGMMSyhcXQPDqlqRO69uAoCTHTZN-fMQzG05CTxc9zNbmg6LcbCbxB3AcrtH9RvV3F73UpXAbNggd_xROUcLsOj0R8MsTwNQiRys5DQBqZbMO2ekggF0Kn5XWbERCmcOUzR1G73qT3xcTW3GZ2aAw_VyRb4dbDUDlWF4IzEf_gwzWerRI7k6vGcl7j6tGDzdB6WgZbafnboe9J6wW1mwPqN4-agYzXiq6ag6-LqOSz9fazS2', start_index=17531)
Annotation(end_index=17616, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLAbsBEVHmQR0G8p_h30FGQqWwX_M9joLWPLAk0XN9OZR5Jrv89FeLsryb0o6t32wDEzI5n4-WRzTCDdjVKMHQkDm6qfIxdh2ULpF6XVN1HYVuiMUgVIVMDyzStmhYGfOgXp7clsgdY7t3pGBHxUXr6oWsn9S0JH5LeIXVxrrz9mexhlC7VpDBbHRZ9Lng9W7y4HyZH_bgeiefzjcCkcdvrKlk8EB_AGb4r7wCUbEuyZ3IJcNpCrX7sXgVnwY=', start_index=17606)
Annotation(end_index=17702, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7ieV-G_X3L159VhJaqjIkiAPufzdb4ZxFq0C-_73QnRi3SVj4UztffqC-1Db9hJCXv5p4cRa9Zs3Q04IPw-WwnTh_xtx3HWi3sq0QUQe_K4O3LuNytMG8-50GLwnX0dS3OrqlZbPKPZlNAlbQazQxXbi5c_zIn2QwTwnfbvKnoi9jGNidsh5si8n0ryqfWByjX6ekQ7E1Xs-SLxvYfqgufTkGYpKLm3fxQAEZWi0cZvvS2hpOPKVaExj4-ul2A4cewI2ZPHkhidpzdqdTyJEcmaE=', start_index=17692)
Annotation(end_index=17779, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyagO455F4-L-ZS4mwJNzbnUaeKrhfER0uPl9o4Vrh-cYzH5dF75xND_eTDSBg_Cq81opn4KJoCo85eN3dlF9uzJ3LIkCdGndXa9Z97_76Tg4l1V_BqjrROXYeecxDNxIz3kCnEA8nf0OOqszs7pELzpOjwPgyfZgYi3fTYlU=', start_index=17769)
Annotation(end_index=17869, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHI2sDO_5CNRep--KzFl_7k_bJdF33FyPPriwn696uJJixTSl2apBFOY8dq16xVyrSD3AMomuDODZsFpfMPGCZITmzoRu1jg36dVIQs6wh7cbB9F2__B3VyeqYgQbEdSQxXlIBTsrlposAjtFbsjQwz_H2vCz2W6r14N1UVvHcXt8AJLiH0EHPh4FCZj24ri_0H4Y6qOblfHz9z4iOBjs4634o2SmWpAr3Y4JkNH5bDDXvRuCNmSbjWv3EqVoez80kNfNrNKbaQQJa_3jdiAlvZdEWP1UiEoinbDq0SpgoP5iyJos6-UluvN2ow', start_index=17859)
Annotation(end_index=17941, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlgfrWDZ4XgR1Dw8ACDfueQnvxjPF2BSrXC0xJa8TfxIQyE9bPPr3VI-ZZE_F9oJUSbLvoXFqvxTHWLYlbWwSxmiXs_P-9Cps_2IluFLK_zzzjHtwYH9qrdI0M9qT7', start_index=17931)
Annotation(end_index=18022, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzHNG_WJ2JNCJHKpwQyQEJ9bt2hIs7IvmvoEBM0IOYw6w86EGHx8kBvuhookag3p-I-QW7fgnFUCOdJZuVpIIc3kt7QZ3oms0WPeRCP36OKTwHzMhAKxE8V-d6GYK_M7bL8rJMRHF1qUMp4chpRU-z02dgHQ==', start_index=18012)
Annotation(end_index=18110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcWDlj9SlXw50E5jI3blmunPgEi5xES79GD1exmGCWyJK4dzIa8HzzqYyIP6ndXHMb03dw0bW5Ro_U_qqx4hS2OfK8KRqEPXiE0BAzXl-KERoyi4eBREh-nff5Ng6MvkGd2i1TcPYLqw==', start_index=18100)
Annotation(end_index=18192, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyagO455F4-L-ZS4mwJNzbnUaeKrhfER0uPl9o4Vrh-cYzH5dF75xND_eTDSBg_Cq81opn4KJoCo85eN3dlF9uzJ3LIkCdGndXa9Z97_76Tg4l1V_BqjrROXYeecxDNxIz3kCnEA8nf0OOqszs7pELzpOjwPgyfZgYi3fTYlU=', start_index=18182)

## Sources
