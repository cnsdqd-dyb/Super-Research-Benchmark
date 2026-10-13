# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 054e9f22 | **Time:** 199.36s | **Cost:** $0.59260
--------------------------------------------------------------------------------

# Achieving Long-Term Resonant Frequency Stability and Detection Accuracy in MEMS Sensors Amidst Process Deviations and Environmental Vibration

**Key Points**
*   **Feasibility:** It is indeed possible for MEMS sensors to maintain long-term stability and high detection accuracy despite the combined negative effects of manufacturing process deviations and environmental vibration, though it requires a multi-layered engineering approach.
*   **Encapsulation is Critical:** The implementation of wafer-level vacuum encapsulation, specifically the "epi-seal" process, has been proven to reduce frequency drift to parts-per-billion (ppb) levels, effectively isolating the resonator from environmental contaminants and pressure fluctuations that cause aging.
*   **Mode Localization:** Utilizing mode-localized sensing in coupled resonators offers a paradigm shift; this technique provides intrinsic common-mode rejection, allowing sensors to ignore global fluctuations (like temperature or vibration) while amplifying sensitivity to the target measurand, although it requires careful management of structural symmetry.
*   **Active Compensation:** Advanced control systems, including electrostatic tuning and active damping loops, can dynamically correct frequency shifts induced by external vibrations. Techniques such as the "F-squared" readout method have successfully mitigated Vibration Rectification Error (VRE), a primary source of accuracy degradation in vibrating environments.
*   **Process Tolerance:** While process variations (e.g., etch profile slanting) inherently introduce asymmetry and frequency splitting, electrostatic tuning and differential design topologies can post-process compensate for these fabrication errors to restore balance and accuracy.

---

## 1. Introduction

Microelectromechanical Systems (MEMS) have become ubiquitous in modern technology, serving as the fundamental sensing hardware for inertial navigation, timing references, and industrial monitoring. However, the miniaturization of these devices renders them highly susceptible to two primary classes of error sources: internal manufacturing imperfections (process deviations) and external operational disturbances (environmental vibration). The user’s query regarding the possibility of maintaining long-term resonant frequency stability and detection accuracy under these combined effects touches upon the central challenge of high-performance MEMS design.

Research indicates that while these factors individually and combinatorially degrade sensor performance, advanced mitigation strategies have been developed to overcome them. Process variations, such as lithographic tolerances and Deep Reactive Ion Etching (DRIE) irregularities, lead to structural asymmetries that alter resonant frequencies and degrade quality factors ($Q$) [cite: 1, 2]. Simultaneously, environmental vibrations introduce phase noise, aliasing, and bias shifts known as Vibration Rectification Error (VRE) [cite: 3, 4].

This report provides an exhaustive analysis of the mechanisms by which these errors occur and the specific technological solutions—ranging from "epi-seal" encapsulation to mode-localized sensing and active feedback control—that enable MEMS sensors to achieve quartz-like stability and high accuracy in harsh environments.

---

## 2. The Impact of Process Deviations on MEMS Performance

Manufacturing variations are inevitable in micro-fabrication. These deviations alter the physical geometry and material properties of the MEMS structure, leading to discrepancies between the designed and actual performance.

### 2.1 Geometric Imperfections and Frequency Shift
The resonant frequency of a MEMS device is fundamentally determined by its mass and stiffness. Fabrication processes, particularly bulk micromachining and DRIE, rely on lithography to transfer patterns onto Silicon-on-Insulator (SOI) wafers. Research assessing the criticality of process variation has shown that identical micromechanical resonators fabricated on the same die can exhibit significant variations in resonant frequency [cite: 1].

*   **Dimensional Tolerance:** Studies measuring the frequency response of single comb-drive resonators found process tolerances resulted in frequency variations ranging from 1.03% to 9.48% across different chips, with part-to-part variation on the same chip reaching nearly 4% [cite: 1].
*   **Etch Profile Anomalies:** Ideally, DRIE produces vertical sidewalls. However, in practice, phenomena such as "scalloping" (sidewall roughness from the Bosch process) and slanted etch profiles occur. Numerical analysis has demonstrated that a deviation in the etch profile angle of just $1^{\circ}$ (from $89^{\circ}$ to $91^{\circ}$) can reduce the frequency response of a micro-resonator from 875.37 Hz to 650.22 Hz [cite: 2]. Furthermore, undercut effects—where the etchant removes material beneath the mask—can drastically shift frequency; a change in undercut from 0 $\mu$m to 4 $\mu$m was shown to drop frequency from ~770 Hz to ~26 Hz in specific reference models [cite: 2].

### 2.2 Structural Asymmetry and Mode Coupling
Process variations do not merely shift the fundamental frequency; they introduce structural asymmetry. In differential resonant sensors, which rely on the balance between two identical resonators, manufacturing tolerances disrupt this symmetry.
*   **Coupling Stiffness Variation:** In differential common-based MEMS resonators (DCMR), variations in the substrate and anchor points due to fabrication can alter the coupling stiffness. Theoretical and experimental validations have shown that coupling stiffness is highly sensitive to the layout of fixed constraints, and deviations here lead to mutual coupling of vibration energy that interferes with frequency outputs [cite: 5].
*   **Impact on Mode Localization:** For sensors utilizing mode localization (a phenomenon where vibration energy is confined to one resonator), structural symmetry is paramount. Research indicates that manufacturing-induced structural asymmetry degrades the effective series motional resistance ($R_x$) and can lead to severe mode aliasing if the thickness variations exceed certain thresholds (e.g., $\pm 5\%$) [cite: 6, 7].

---

## 3. The Impact of Environmental Vibration

External vibration poses a severe threat to detection accuracy, particularly for resonant sensors and accelerometers. The interaction between environmental vibration and the sensor's internal dynamics manifests primarily as noise, bias instability, and rectification errors.

### 3.1 Vibration Rectification Error (VRE)
One of the most critical accuracy-limiting factors in vibrating environments is Vibration Rectification Error (VRE). This phenomenon occurs when AC vibration inputs are rectified into a DC bias shift in the sensor output, causing erroneous readings.
*   **Mechanism:** VRE is primarily caused by Scale Factor Nonlinearity (SFNL). In MEMS accelerometers, the second-order nonlinearity of the scale factor is often the dominant contributor [cite: 4, 8]. As the proof mass undergoes large displacements due to external vibration, the capacitance-to-displacement relationship becomes nonlinear (fringing fields), and the mechanical suspension may exhibit nonlinear stiffness [cite: 9].
*   **Frequency Dependence:** The VRE coefficient is frequency-dependent. Amplification of the proof mass displacement occurs when the external vibration frequency approaches the sensor's resonant frequency, significantly exacerbating the error [cite: 9].

### 3.2 Phase Noise and Oscillator Stability
For MEMS oscillators used as timing references, external vibrations induce inertial forces on the resonator beam. These forces cause stress-induced stiffness changes, leading to frequency modulation. This appears as phase noise or "short-term" frequency instability.
*   **Vibration Sensitivity:** Without corrective measures, external movement couples into the device, degrading performance by creating frequency shifts and increasing phase noise. This is a known disadvantage compared to bulky quartz oscillators, although modern MEMS designs are closing this gap [cite: 10, 11].
*   **Aliasing:** In sampled systems, high-frequency vibrations can alias down into the measurement bandwidth, appearing as low-frequency noise or drift, further corrupting detection accuracy [cite: 12].

---

## 4. Mechanisms for Long-Term Stability

To answer the user's query affirmatively, one must look at the specific technologies that enable stability over time. The "drift" of MEMS sensors is often driven by packaging leaks, material aging, and surface contamination.

### 4.1 Epi-Seal Encapsulation
The most significant breakthrough for long-term stability in silicon MEMS is the "epi-seal" process. This wafer-level encapsulation technique creates a hermetic seal using epitaxial silicon deposition.
*   **Process:** The process involves encapsulating the MEMS device in a cavity created by a sacrificial oxide etch, followed by sealing with epitaxial silicon at high temperatures. This results in an ultra-clean, high-vacuum environment free of native oxides and humidity [cite: 13].
*   **Performance Metrics:** Devices fabricated with epi-seal technology have demonstrated exceptional stability.
    *   **Aging:** Total observed aging has been recorded at approximately 10 ppm over 10 months, which is on par with consumer quartz oscillators [cite: 14]. Other studies have shown frequency stability of $\pm 3$ ppm over 15 months for double-ended tuning fork (DETF) resonators [cite: 15].
    *   **Fatigue Resistance:** The high-temperature clean environment prevents surface contamination that typically leads to fatigue. Resonators have shown stable quality factors and frequencies even after 200 hours of testing under maximum stress [cite: 13].

### 4.2 Material Selection: Single Crystal Silicon (SCS)
The choice of material is critical. While polysilicon is used, Single Crystal Silicon (SCS) is preferred for high-precision timing and sensing due to its defect-free lattice structure.
*   **Hysteresis and Creep:** SCS exhibits virtually no hysteresis or creep, which are common sources of long-term drift in metal or piezoelectric sensors.
*   **Temperature Stability:** While silicon has a high Temperature Coefficient of Frequency (TCF), it can be compensated. Composite resonators (Si-SiO2) or heavy doping can reduce TCF, and when combined with epi-seal, SCS resonators achieve sub-ppm stability [cite: 16, 17].

---

## 5. Mitigation Strategies for Combined Effects

The core of the solution lies in combining robust physical design with active compensation to handle both process deviations and environmental vibration simultaneously.

### 5.1 Mode Localization and Common Mode Rejection
Mode-localized sensors represent a paradigm shift in handling environmental noise. Instead of measuring a frequency shift (which is sensitive to temperature and global vibration), these sensors measure the change in *amplitude ratio* between two weakly coupled resonators.
*   **Common Mode Rejection (CMR):** A key advantage of mode-localized sensors is intrinsic CMR. Global perturbations, such as ambient temperature changes or pressure fluctuations, affect both coupled resonators equally (common mode). However, the eigenstate (mode shape) shift is driven by differential perturbations. Research has experimentally demonstrated that eigenstate shifts are over three orders of magnitude more sensitive to the target measurand than to common-mode environmental drift [cite: 18, 19].
*   **Sensitivity Enhancement:** This technique enhances parametric sensitivity by orders of magnitude (up to 684x improvement in scale factor reported) [cite: 20]. This high sensitivity allows the sensor to detect minute signals even in the presence of noise, effectively improving the signal-to-noise ratio (SNR).
*   **Vibration Immunity:** By utilizing differential sensing topologies where the resonators share a common substrate, vibration energy is coupled commonly. The differential readout rejects this common vibration noise, provided the structural symmetry is maintained [cite: 5].

### 5.2 Active Feedback and Compensation
To counter the dynamic effects of vibration and the static effects of process variation, active electronic control is employed.

*   **Electrostatic Tuning:** To correct for process-induced frequency splitting (asymmetry), DC bias voltages are applied to the resonators. This "electrostatic spring softening" effect allows for post-fabrication tuning of the resonant frequencies.
    *   **Process Compensation:** This method can compensate for manufacturing tolerances that cause frequency variations of up to 2000 ppm, restoring the necessary symmetry for high-performance operation [cite: 16, 21].
    *   **Vibration Compensation:** An auxiliary accelerometer can measure external vibration and feed a compensation signal into the resonator's bias voltage. This active compensation has been shown to reduce acceleration sensitivity by 91% for sinusoidal vibrations [cite: 11].

*   **Active Damping:** For resonant accelerometers, an active damping control loop can be implemented to suppress the translational motion of the proof mass at its resonant frequency. This prevents the proof mass from hitting mechanical stops during shock and reduces the settling time (e.g., from hundreds of ms to <50 ms), thereby maintaining accuracy during vibration events [cite: 8].

*   **VRE Reduction (F-squared Method):** To combat VRE, the "F-squared" readout method is used. Instead of a linear frequency readout, this method processes the square of the frequency difference. Since the dominant nonlinearity is often quadratic, this mathematical operation effectively cancels out the error source. Experimental results show VRE reduction to less than 10 $\mu g/g^2$ using this technique [cite: 4, 8].

### 5.3 Vibration Isolation and Filtering
At the system level, physical and signal processing techniques provide the first line of defense.
*   **Mechanical Isolation:** Using vibration isolators acts as a low-pass filter (LPF), attenuating high-frequency vibrations before they reach the MEMS structure. However, this is often insufficient for low-frequency vibration [cite: 22].
*   **Signal Processing:** The combination of Low Pass Filters and Moving Average Filters (or hybrid "Vibration Immunity" filters) in the digital domain can minimize noise. However, these often introduce lag and require trade-offs with bandwidth [cite: 3].

---

## 6. Detailed Analysis of Specific Sensor Architectures

### 6.1 Differential Resonant Accelerometers
These sensors use two resonators acting as a differential pair. When the proof mass moves under acceleration, one resonator is compressed (frequency increases) and the other is tensioned (frequency decreases).
*   **Vibration Rejection:** The differential setup theoretically cancels out common-mode vibration. However, process variations (e.g., thickness mismatch) create "residual" common-mode sensitivity.
*   **Solution:** The integration of electrostatic tuning to balance the resonators post-manufacture, combined with the F-squared readout, allows these sensors to maintain high accuracy. Research shows that optimizing the anchor point layout (peripheral vs. central) significantly reduces vibration coupling stiffness, enhancing immunity [cite: 5].

### 6.2 Mode-Localized Sensors
*   **Process Variation Sensitivity:** While mode localization offers high sensitivity, it is also highly sensitive to process-induced asymmetry. A 5% thickness variation can lead to severe mode aliasing [cite: 7].
*   **Solution:** To make this viable, tunable coupling stiffness is used. By employing a parametric pump or electrostatic tuning, the coupling factor can be adjusted to operate in the "weak coupling" regime despite physical imperfections, maintaining the benefits of high sensitivity and stability [cite: 20].

### 6.3 MEMS Oscillators
*   **Long-Term Stability:** The primary concern here is aging. The epi-seal process is the definitive solution, providing the vacuum environment necessary for stable $Q$ and frequency over years [cite: 14, 23].
*   **Vibration Stability:** Phase noise degradation due to vibration is mitigated by stiff mechanical designs (high resonant frequencies) and active compensation circuits that adjust the frequency in real-time based on vibration input [cite: 11].

---

## 7. Conclusion

The research conclusively supports that it is possible for MEMS sensors to maintain long-term resonant frequency stability and detection accuracy despite process deviations and environmental vibration. This capability is not inherent to the basic MEMS structure but is the result of a sophisticated convergence of technologies:

1.  **Manufacturing & Packaging:** **Epi-seal encapsulation** eliminates the primary causes of long-term drift (aging, contamination), securing the "long-term stability" requirement [cite: 13, 14].
2.  **Design Topology:** **Differential sensing** and **mode localization** provide intrinsic physics-based rejection of common-mode errors (temperature, global vibration), addressing "environmental vibration" [cite: 5, 19].
3.  **Active Correction:** **Electrostatic tuning** compensates for "process deviations" by electronically re-balancing asymmetric structures [cite: 16, 21].
4.  **Signal Processing:** Advanced readout schemes like the **F-squared method** and **active damping loops** actively suppress vibration-induced errors (VRE) and noise [cite: 4, 8].

By integrating these specific methodologies, modern MEMS devices can achieve performance metrics that rival or exceed traditional quartz sensors, even in the presence of significant manufacturing tolerances and harsh operational environments.

**Sources:**
1. [sysint-conference.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWObxNRvcAOL-edJDbM8xb2J9vCPIC1ktN_m9sDJ9dCqKyMU5XN6Ve8mGhxKE4Nvm2ronVPrR06TnievoDkSXMnpgZwtpaxTQ28ANwYjANVeqh6XTOYfaXS8HDRTAxKsLrEQOzNseGH2x1KU6jpQ4GNQA58wZ_LDgZ6N7fkdNRU5W1EiI05qbPIt3j7F7YJ83DNsY0laXBcTkeO3vb1fMmc-6h0rBmGn3aKbTcHv0w2aYnFWSdxJ5iZRQCS7-DDjw_)
2. [scholaris.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRi7RPrjEIQpe6zbKqZJB8clyYiKbDKrGu7wtfEmrezo4m_ChZ1ZEOc-OuiRag4506p96NY8TqFVYj-VrO-Ole43Ynywu7FGeNYe4t19Ni-w0bBiB538JAPfBMxqxqnbAZ1dF5SPZjI5E4mCnjG8XcpDosEKs_JbTWtZgxZS0=)
3. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvP4KVcGgMnl6ryg_8ocDoDl3NK_rnjvyTZFm9nfBMYETr6CSGj-sUVzCGmhpqm5i5slq84DozVKoF-tQclPc6VM-4Mybfj5EcL01BfH-ncwZ9gg_PVNYize7k648UgD7M7Q==)
4. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsppUmPn3Z98fGA7Thamzevl6MgaiYwWX_q9T1hjudPLZBrhe2hwNRdVT5Q8Vihr_XD0fLiIVlTSQ68ceZsprt9MAPQhjYvHgNSIayan2d9cycqpgb69TmWwTB-3F3xIKlp6Jx)
5. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC3lyCl0HrQnzZ67Li5YloMeKOlqPjSPSuc0N-ThGhbP8CinimXfHvqSOWX4t4WsIIrTU4jvTGHWl1Hxt2Sl0i3Tsa8QopCKoLn5zOlXUdHqleLQ7PS9zEluaV4eg=)
6. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrRhID2nM2i5FwkryAzEIabV45LzJ48gWh9SDlP7FYh_gUfhN7EUmATBURonz_XOkUfMIumguYTcoy99R_gGCkEYBJP8mwL13NmIAsH__QJ6yBy_iB_h-0x428vQ3JhXvXve9Vm8BpM6Ojbewbf29Znm0lyFHnqhysiW28m4RZJFdf6rOFsDOa05qHt130ec2Kuu3TkRH9eg-Z42JHiUXg7wB56fyKkp9t3RHGbRCw9Gr1ZhjMhGQOZAEj-oydrvsObqlUmZhyHS5HpsFZ2g_0tZc=)
7. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1jmSkIUktWVDe7EZG4sXXXtoSaQwCyNfj8a_V7ig6sIotUw1O1q3f9SzxqktJ9JJbhQ1Bm5T4L5Vk4PDPOWgx8-5ZS1cnx5oLX4KnQTyT834PDLbJbz9d8V3M_ZU=)
8. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlYf0okx-RxpaJ2XdoJSratCMsv0XrUW7L48tZ3tV4Q7i7Jn7Mmavu8eRraj_ehv7ZG_iCq0H82N5Fi30YS2PvTHiwfMWE-Qc4XjoO-961xBk2XRAbnsi3CdeVD6-iDATRgWbKBUZ-oUjcNq-6TMw=)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzpb3dVIKjCGM-3juMlbJpOi2ze08Ju-1fZDwqfZbWccsijOsAS_oElsGKpN_l0n3lMHpDgoIbtZW5qg1u76JF2th_Ox9s-vEf32gOPlgr_YfBUpkfTxsud2hfNQeeMgBK1yrWB9zBBGbXkqpsugxcYiy_zqc10JPJIYoYIsc0iqmmyZNCBCKVhRpX2XFNKL6f-17gSniezUBEzV-DskHJpPDxgs-eAndNH0DGR7pIh5T9ujrNeqmHCv8m4OtyI2BQaSRbP0OuGKuOLuoDfDtAy2nSeoU7Wl42L6vfi1uykTAS)
10. [sitime.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuQ8Opl9jR16Yl11EZ5Rv2QlVur0_llXZQzihrnAm4CroHonuhlb3U0F4tzU_gRz0wGrLJ6WOcYyIZVcOS-WrIA2BUKJ9-aXkc0KTf2HLlitcQ)
11. [purdue.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxKsf4qK8ZgpcaQ8rTolW-0DDcczJWMPzmc66CrJV1XXnrFDn9iAlQZqn4q9ZVe_L6MwuafMm1LdwiL7itUmlv2QHAh-1QL542u1n7NxyKRwX-Ui67XqQr3agfhsVPowtZBkUgbhMLyBp-sEMJKV4RerxaCR6PMjFV11WFDpZtkkhlFWigsUiIqSTGqw==)
12. [sbg-systems.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUDckMXVQr6G3yD_YCZVQhGcUH2YWaWCwrOmC0eSWrs56M6M-WB64N622zU3lDymMoEqOschPQe9gZjbr2EzTY538X73GysF5Prt8-iPoenDX7je2e5OPeLw4YSbTvQ8NiA7Gi2vcGataMbTehQtzv-bYN6A==)
13. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHU48UT_P2sabTK6gnvOct_9XdqVnWiOqoinKM7xZSsW2iAvVHcOpaeQBsQlIA5LSuA6IQRW-lYgPzyuLP9Utuv7HtmXH1B8ObiHaqXDShhHmD8T-ynJ1DiScNGDhjDEpXPhX8LD_lRWOSLFXDfgN3E-nLvAQl2)
14. [berkeley.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkcNtRyj11JDrlsYpjsUs-ZFf9QjFe4YvG3l3usE_3SERiotvjMOYtDTenVO6JdHxZnXtKQZchMsuCqUZhASf4beW1R8xn9LBlH4IAUX_pXBwUhIR3KWQrTRs1geb-qUuvs0uUAjpRDguQMQ1WQ8L8nNKtCaLaeKV-76HBepQP85Tfhp9PBsOcghSxdS0X74B83Lj4GOoVWbNV-SeTq4RWMe-yQu8J)
15. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBk0U7bhZbDvAFMNXYN00Tn8P0EtIYuz8iv72WMjZRdSX265plrBANl3-6IeDdPX2Y5qBFuExKnfFYPJbi3y586AsOyd48bDfhNOXEuKGTGzS7kINQTnMliYfLRs-YQsBjfkfi_xgaebFf8MRvaw==)
16. [transducer-research-foundation.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgcBrcz_dRhM4qn6_8OHhJY410NuWYDMsQA-Ag6TSAgpuiuLbnfQ_k0NyjZfngi-b0xSNKD6eY8mWn8X0N3TIDUvSxiFJ8igiQ8l_uSw9WB-PJbISf8z5RawKm8OgVwm4iWhTxV2_KY_BfVeg-EYoBtxj2T4XBocq1aA_hbjjEQ0e3iRqBMrWuUYQVmf7fa9B6dQ==)
17. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTjyj8tin_Z1YUO-4-2wyOJEWi6ovsp5arBxARlK3rASpaB-PpEblTHiTpiR2IqXkDVirinQlAltNLgKAiHXA7gOSjz8PH7VsUj0XKg7jJc1HqoD2E49h9KGrHqyRbDAt8e7PLgIXuoh38LV5FyaXeN9xGcg==)
18. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOzEohuOXeT9QkgY5nrWlJgARSr_VENmGRltfAvzfoK24ORuWoqREK04AK3PcHhXk0UsKPRWqBTqWWD2iYw0Ere8_sgoIOTVxa8pGFE-dmLsFSc7-WYEXJ-ayTHtJh9gNK2_RkriYjtGlK-Kz1t0aE3so_FIQJ_5rdqtvJC5E1IScUnH2yJ99Xt5XaIeis5JfnTjgW4W7So0o3B7msGi6iwg==)
19. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhmVKtPJwjS4gNsRQZhdNuj0GzxlQG5ZTB0tT4iXh18yXRXF14ngqr9wjZVuEzKi4F2RRmhpZvVXiRS1DDb-PcJkpHiEktInJgQCLize3WTyJqsJAOArNlHGTKCwjZTgkGPw==)
20. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvqewK9mkMRPTp4LVa9wm0VavmAi9vuTSJDjgeCLOPDcfgtl7WOQ7YkiEWP9kVRacHPccuuMLJrkvRSVBSeeT55LAG46mVXkBxwAXvuKKw_0BKs8ZH8h-p5FH35uxnoyVV9iQ=)
21. [upenn.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGC895W4tIElBZzwQwz4-qd4jxOCFo4Bbyqh3gbLarM2-bBfu3sjq3zHOT3w8D4BoxBdiUa71ws39HEBnS9jdwXSagoHLXOobA8aLyVUL1vLRNNRLOC0y4MWv-vKk74IKm66r5a-CUNI2Kq6UniFy0DUlwwdyUgTrGHuyDteygeG8kdCLd0ex0jSAUztBl_9JGvU8-LVxiwhifmX3w=)
22. [umich.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3liNUfUh3K-WAL1ceRvPxJtSpyjkSAJFeXwICXINFWOXDaBkTLkfIJwYBnM_fCpz0aV2_IjxJGVjjOa6lfe0fB88tKiSX9dO84ei28k3RTtuggfW4tt6Zi5t4bQCj7mGmqD0xjWTkvxoTM0Rf4kr6VdePm8r3smdg0TqIFu-__7L3gsD739D6Bjt7)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQET2OyBTzv1h-NbPeiL9ZGVse1jEQxC6KJr0ZoS1gkV4dEOOSiePw081GP7AgStaUWL4FPyCblupJJFy6hsDHKSzGMZBvJZtHWTxiJLaLb7mW3T5k0DtWRd6atMtc6JGEEzkdVPlEcvHJ87SfzelY3vos4lzw9ZSPfjcNK-aigUTf17oXHlS7fhGmO3QQwIWbEyonDFjeAKwZQrHqPsC5mHHdk9lpCxqmjQpQa_TlruCZg2zWqIkp5L5c16fTivyJaabG0ueQ==)


## Annotations
Annotation(end_index=2844, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWObxNRvcAOL-edJDbM8xb2J9vCPIC1ktN_m9sDJ9dCqKyMU5XN6Ve8mGhxKE4Nvm2ronVPrR06TnievoDkSXMnpgZwtpaxTQ28ANwYjANVeqh6XTOYfaXS8HDRTAxKsLrEQOzNseGH2x1KU6jpQ4GNQA58wZ_LDgZ6N7fkdNRU5W1EiI05qbPIt3j7F7YJ83DNsY0laXBcTkeO3vb1fMmc-6h0rBmGn3aKbTcHv0w2aYnFWSdxJ5iZRQCS7-DDjw_', start_index=2832)
Annotation(end_index=2844, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRi7RPrjEIQpe6zbKqZJB8clyYiKbDKrGu7wtfEmrezo4m_ChZ1ZEOc-OuiRag4506p96NY8TqFVYj-VrO-Ole43Ynywu7FGeNYe4t19Ni-w0bBiB538JAPfBMxqxqnbAZ1dF5SPZjI5E4mCnjG8XcpDosEKs_JbTWtZgxZS0=', start_index=2832)
Annotation(end_index=2993, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvP4KVcGgMnl6ryg_8ocDoDl3NK_rnjvyTZFm9nfBMYETr6CSGj-sUVzCGmhpqm5i5slq84DozVKoF-tQclPc6VM-4Mybfj5EcL01BfH-ncwZ9gg_PVNYize7k648UgD7M7Q==', start_index=2981)
Annotation(end_index=2993, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsppUmPn3Z98fGA7Thamzevl6MgaiYwWX_q9T1hjudPLZBrhe2hwNRdVT5Q8Vihr_XD0fLiIVlTSQ68ceZsprt9MAPQhjYvHgNSIayan2d9cycqpgb69TmWwTB-3F3xIKlp6Jx', start_index=2981)
Annotation(end_index=4108, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWObxNRvcAOL-edJDbM8xb2J9vCPIC1ktN_m9sDJ9dCqKyMU5XN6Ve8mGhxKE4Nvm2ronVPrR06TnievoDkSXMnpgZwtpaxTQ28ANwYjANVeqh6XTOYfaXS8HDRTAxKsLrEQOzNseGH2x1KU6jpQ4GNQA58wZ_LDgZ6N7fkdNRU5W1EiI05qbPIt3j7F7YJ83DNsY0laXBcTkeO3vb1fMmc-6h0rBmGn3aKbTcHv0w2aYnFWSdxJ5iZRQCS7-DDjw_', start_index=4099)
Annotation(end_index=4398, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWObxNRvcAOL-edJDbM8xb2J9vCPIC1ktN_m9sDJ9dCqKyMU5XN6Ve8mGhxKE4Nvm2ronVPrR06TnievoDkSXMnpgZwtpaxTQ28ANwYjANVeqh6XTOYfaXS8HDRTAxKsLrEQOzNseGH2x1KU6jpQ4GNQA58wZ_LDgZ6N7fkdNRU5W1EiI05qbPIt3j7F7YJ83DNsY0laXBcTkeO3vb1fMmc-6h0rBmGn3aKbTcHv0w2aYnFWSdxJ5iZRQCS7-DDjw_', start_index=4389)
Annotation(end_index=4832, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRi7RPrjEIQpe6zbKqZJB8clyYiKbDKrGu7wtfEmrezo4m_ChZ1ZEOc-OuiRag4506p96NY8TqFVYj-VrO-Ole43Ynywu7FGeNYe4t19Ni-w0bBiB538JAPfBMxqxqnbAZ1dF5SPZjI5E4mCnjG8XcpDosEKs_JbTWtZgxZS0=', start_index=4823)
Annotation(end_index=5089, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRi7RPrjEIQpe6zbKqZJB8clyYiKbDKrGu7wtfEmrezo4m_ChZ1ZEOc-OuiRag4506p96NY8TqFVYj-VrO-Ole43Ynywu7FGeNYe4t19Ni-w0bBiB538JAPfBMxqxqnbAZ1dF5SPZjI5E4mCnjG8XcpDosEKs_JbTWtZgxZS0=', start_index=5080)
Annotation(end_index=5818, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC3lyCl0HrQnzZ67Li5YloMeKOlqPjSPSuc0N-ThGhbP8CinimXfHvqSOWX4t4WsIIrTU4jvTGHWl1Hxt2Sl0i3Tsa8QopCKoLn5zOlXUdHqleLQ7PS9zEluaV4eg=', start_index=5809)
Annotation(end_index=6245, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1jmSkIUktWVDe7EZG4sXXXtoSaQwCyNfj8a_V7ig6sIotUw1O1q3f9SzxqktJ9JJbhQ1Bm5T4L5Vk4PDPOWgx8-5ZS1cnx5oLX4KnQTyT834PDLbJbz9d8V3M_ZU=', start_index=6233)
Annotation(end_index=6245, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrRhID2nM2i5FwkryAzEIabV45LzJ48gWh9SDlP7FYh_gUfhN7EUmATBURonz_XOkUfMIumguYTcoy99R_gGCkEYBJP8mwL13NmIAsH__QJ6yBy_iB_h-0x428vQ3JhXvXve9Vm8BpM6Ojbewbf29Znm0lyFHnqhysiW28m4RZJFdf6rOFsDOa05qHt130ec2Kuu3TkRH9eg-Z42JHiUXg7wB56fyKkp9t3RHGbRCw9Gr1ZhjMhGQOZAEj-oydrvsObqlUmZhyHS5HpsFZ2g_0tZc=', start_index=6233)
Annotation(end_index=7068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlYf0okx-RxpaJ2XdoJSratCMsv0XrUW7L48tZ3tV4Q7i7Jn7Mmavu8eRraj_ehv7ZG_iCq0H82N5Fi30YS2PvTHiwfMWE-Qc4XjoO-961xBk2XRAbnsi3CdeVD6-iDATRgWbKBUZ-oUjcNq-6TMw=', start_index=7056)
Annotation(end_index=7068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsppUmPn3Z98fGA7Thamzevl6MgaiYwWX_q9T1hjudPLZBrhe2hwNRdVT5Q8Vihr_XD0fLiIVlTSQ68ceZsprt9MAPQhjYvHgNSIayan2d9cycqpgb69TmWwTB-3F3xIKlp6Jx', start_index=7056)
Annotation(end_index=7298, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzpb3dVIKjCGM-3juMlbJpOi2ze08Ju-1fZDwqfZbWccsijOsAS_oElsGKpN_l0n3lMHpDgoIbtZW5qg1u76JF2th_Ox9s-vEf32gOPlgr_YfBUpkfTxsud2hfNQeeMgBK1yrWB9zBBGbXkqpsugxcYiy_zqc10JPJIYoYIsc0iqmmyZNCBCKVhRpX2XFNKL6f-17gSniezUBEzV-DskHJpPDxgs-eAndNH0DGR7pIh5T9ujrNeqmHCv8m4OtyI2BQaSRbP0OuGKuOLuoDfDtAy2nSeoU7Wl42L6vfi1uykTAS', start_index=7289)
Annotation(end_index=7554, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzpb3dVIKjCGM-3juMlbJpOi2ze08Ju-1fZDwqfZbWccsijOsAS_oElsGKpN_l0n3lMHpDgoIbtZW5qg1u76JF2th_Ox9s-vEf32gOPlgr_YfBUpkfTxsud2hfNQeeMgBK1yrWB9zBBGbXkqpsugxcYiy_zqc10JPJIYoYIsc0iqmmyZNCBCKVhRpX2XFNKL6f-17gSniezUBEzV-DskHJpPDxgs-eAndNH0DGR7pIh5T9ujrNeqmHCv8m4OtyI2BQaSRbP0OuGKuOLuoDfDtAy2nSeoU7Wl42L6vfi1uykTAS', start_index=7545)
Annotation(end_index=8182, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuQ8Opl9jR16Yl11EZ5Rv2QlVur0_llXZQzihrnAm4CroHonuhlb3U0F4tzU_gRz0wGrLJ6WOcYyIZVcOS-WrIA2BUKJ9-aXkc0KTf2HLlitcQ', start_index=8168)
Annotation(end_index=8182, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxKsf4qK8ZgpcaQ8rTolW-0DDcczJWMPzmc66CrJV1XXnrFDn9iAlQZqn4q9ZVe_L6MwuafMm1LdwiL7itUmlv2QHAh-1QL542u1n7NxyKRwX-Ui67XqQr3agfhsVPowtZBkUgbhMLyBp-sEMJKV4RerxaCR6PMjFV11WFDpZtkkhlFWigsUiIqSTGqw==', start_index=8168)
Annotation(end_index=8386, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUDckMXVQr6G3yD_YCZVQhGcUH2YWaWCwrOmC0eSWrs56M6M-WB64N622zU3lDymMoEqOschPQe9gZjbr2EzTY538X73GysF5Prt8-iPoenDX7je2e5OPeLw4YSbTvQ8NiA7Gi2vcGataMbTehQtzv-bYN6A==', start_index=8376)
Annotation(end_index=9178, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHU48UT_P2sabTK6gnvOct_9XdqVnWiOqoinKM7xZSsW2iAvVHcOpaeQBsQlIA5LSuA6IQRW-lYgPzyuLP9Utuv7HtmXH1B8ObiHaqXDShhHmD8T-ynJ1DiScNGDhjDEpXPhX8LD_lRWOSLFXDfgN3E-nLvAQl2', start_index=9168)
Annotation(end_index=9451, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkcNtRyj11JDrlsYpjsUs-ZFf9QjFe4YvG3l3usE_3SERiotvjMOYtDTenVO6JdHxZnXtKQZchMsuCqUZhASf4beW1R8xn9LBlH4IAUX_pXBwUhIR3KWQrTRs1geb-qUuvs0uUAjpRDguQMQ1WQ8L8nNKtCaLaeKV-76HBepQP85Tfhp9PBsOcghSxdS0X74B83Lj4GOoVWbNV-SeTq4RWMe-yQu8J', start_index=9441)
Annotation(end_index=9585, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBk0U7bhZbDvAFMNXYN00Tn8P0EtIYuz8iv72WMjZRdSX265plrBANl3-6IeDdPX2Y5qBFuExKnfFYPJbi3y586AsOyd48bDfhNOXEuKGTGzS7kINQTnMliYfLRs-YQsBjfkfi_xgaebFf8MRvaw==', start_index=9575)
Annotation(end_index=9846, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHU48UT_P2sabTK6gnvOct_9XdqVnWiOqoinKM7xZSsW2iAvVHcOpaeQBsQlIA5LSuA6IQRW-lYgPzyuLP9Utuv7HtmXH1B8ObiHaqXDShhHmD8T-ynJ1DiScNGDhjDEpXPhX8LD_lRWOSLFXDfgN3E-nLvAQl2', start_index=9836)
Annotation(end_index=10521, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgcBrcz_dRhM4qn6_8OHhJY410NuWYDMsQA-Ag6TSAgpuiuLbnfQ_k0NyjZfngi-b0xSNKD6eY8mWn8X0N3TIDUvSxiFJ8igiQ8l_uSw9WB-PJbISf8z5RawKm8OgVwm4iWhTxV2_KY_BfVeg-EYoBtxj2T4XBocq1aA_hbjjEQ0e3iRqBMrWuUYQVmf7fa9B6dQ==', start_index=10507)
Annotation(end_index=10521, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTjyj8tin_Z1YUO-4-2wyOJEWi6ovsp5arBxARlK3rASpaB-PpEblTHiTpiR2IqXkDVirinQlAltNLgKAiHXA7gOSjz8PH7VsUj0XKg7jJc1HqoD2E49h9KGrHqyRbDAt8e7PLgIXuoh38LV5FyaXeN9xGcg==', start_index=10507)
Annotation(end_index=11585, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOzEohuOXeT9QkgY5nrWlJgARSr_VENmGRltfAvzfoK24ORuWoqREK04AK3PcHhXk0UsKPRWqBTqWWD2iYw0Ere8_sgoIOTVxa8pGFE-dmLsFSc7-WYEXJ-ayTHtJh9gNK2_RkriYjtGlK-Kz1t0aE3so_FIQJ_5rdqtvJC5E1IScUnH2yJ99Xt5XaIeis5JfnTjgW4W7So0o3B7msGi6iwg==', start_index=11571)
Annotation(end_index=11585, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhmVKtPJwjS4gNsRQZhdNuj0GzxlQG5ZTB0tT4iXh18yXRXF14ngqr9wjZVuEzKi4F2RRmhpZvVXiRS1DDb-PcJkpHiEktInJgQCLize3WTyJqsJAOArNlHGTKCwjZTgkGPw==', start_index=11571)
Annotation(end_index=11750, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvqewK9mkMRPTp4LVa9wm0VavmAi9vuTSJDjgeCLOPDcfgtl7WOQ7YkiEWP9kVRacHPccuuMLJrkvRSVBSeeT55LAG46mVXkBxwAXvuKKw_0BKs8ZH8h-p5FH35uxnoyVV9iQ=', start_index=11740)
Annotation(end_index=12179, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC3lyCl0HrQnzZ67Li5YloMeKOlqPjSPSuc0N-ThGhbP8CinimXfHvqSOWX4t4WsIIrTU4jvTGHWl1Hxt2Sl0i3Tsa8QopCKoLn5zOlXUdHqleLQ7PS9zEluaV4eg=', start_index=12170)
Annotation(end_index=12822, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgcBrcz_dRhM4qn6_8OHhJY410NuWYDMsQA-Ag6TSAgpuiuLbnfQ_k0NyjZfngi-b0xSNKD6eY8mWn8X0N3TIDUvSxiFJ8igiQ8l_uSw9WB-PJbISf8z5RawKm8OgVwm4iWhTxV2_KY_BfVeg-EYoBtxj2T4XBocq1aA_hbjjEQ0e3iRqBMrWuUYQVmf7fa9B6dQ==', start_index=12808)
Annotation(end_index=12822, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGC895W4tIElBZzwQwz4-qd4jxOCFo4Bbyqh3gbLarM2-bBfu3sjq3zHOT3w8D4BoxBdiUa71ws39HEBnS9jdwXSagoHLXOobA8aLyVUL1vLRNNRLOC0y4MWv-vKk74IKm66r5a-CUNI2Kq6UniFy0DUlwwdyUgTrGHuyDteygeG8kdCLd0ex0jSAUztBl_9JGvU8-LVxiwhifmX3w=', start_index=12808)
Annotation(end_index=13102, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxKsf4qK8ZgpcaQ8rTolW-0DDcczJWMPzmc66CrJV1XXnrFDn9iAlQZqn4q9ZVe_L6MwuafMm1LdwiL7itUmlv2QHAh-1QL542u1n7NxyKRwX-Ui67XqQr3agfhsVPowtZBkUgbhMLyBp-sEMJKV4RerxaCR6PMjFV11WFDpZtkkhlFWigsUiIqSTGqw==', start_index=13092)
Annotation(end_index=13493, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlYf0okx-RxpaJ2XdoJSratCMsv0XrUW7L48tZ3tV4Q7i7Jn7Mmavu8eRraj_ehv7ZG_iCq0H82N5Fi30YS2PvTHiwfMWE-Qc4XjoO-961xBk2XRAbnsi3CdeVD6-iDATRgWbKBUZ-oUjcNq-6TMw=', start_index=13484)
Annotation(end_index=13917, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlYf0okx-RxpaJ2XdoJSratCMsv0XrUW7L48tZ3tV4Q7i7Jn7Mmavu8eRraj_ehv7ZG_iCq0H82N5Fi30YS2PvTHiwfMWE-Qc4XjoO-961xBk2XRAbnsi3CdeVD6-iDATRgWbKBUZ-oUjcNq-6TMw=', start_index=13905)
Annotation(end_index=13917, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsppUmPn3Z98fGA7Thamzevl6MgaiYwWX_q9T1hjudPLZBrhe2hwNRdVT5Q8Vihr_XD0fLiIVlTSQ68ceZsprt9MAPQhjYvHgNSIayan2d9cycqpgb69TmWwTB-3F3xIKlp6Jx', start_index=13905)
Annotation(end_index=14299, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3liNUfUh3K-WAL1ceRvPxJtSpyjkSAJFeXwICXINFWOXDaBkTLkfIJwYBnM_fCpz0aV2_IjxJGVjjOa6lfe0fB88tKiSX9dO84ei28k3RTtuggfW4tt6Zi5t4bQCj7mGmqD0xjWTkvxoTM0Rf4kr6VdePm8r3smdg0TqIFu-__7L3gsD739D6Bjt7', start_index=14289)
Annotation(end_index=14556, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvP4KVcGgMnl6ryg_8ocDoDl3NK_rnjvyTZFm9nfBMYETr6CSGj-sUVzCGmhpqm5i5slq84DozVKoF-tQclPc6VM-4Mybfj5EcL01BfH-ncwZ9gg_PVNYize7k648UgD7M7Q==', start_index=14547)
Annotation(end_index=15423, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC3lyCl0HrQnzZ67Li5YloMeKOlqPjSPSuc0N-ThGhbP8CinimXfHvqSOWX4t4WsIIrTU4jvTGHWl1Hxt2Sl0i3Tsa8QopCKoLn5zOlXUdHqleLQ7PS9zEluaV4eg=', start_index=15414)
Annotation(end_index=15670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1jmSkIUktWVDe7EZG4sXXXtoSaQwCyNfj8a_V7ig6sIotUw1O1q3f9SzxqktJ9JJbhQ1Bm5T4L5Vk4PDPOWgx8-5ZS1cnx5oLX4KnQTyT834PDLbJbz9d8V3M_ZU=', start_index=15661)
Annotation(end_index=15981, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvqewK9mkMRPTp4LVa9wm0VavmAi9vuTSJDjgeCLOPDcfgtl7WOQ7YkiEWP9kVRacHPccuuMLJrkvRSVBSeeT55LAG46mVXkBxwAXvuKKw_0BKs8ZH8h-p5FH35uxnoyVV9iQ=', start_index=15971)
Annotation(end_index=16219, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQET2OyBTzv1h-NbPeiL9ZGVse1jEQxC6KJr0ZoS1gkV4dEOOSiePw081GP7AgStaUWL4FPyCblupJJFy6hsDHKSzGMZBvJZtHWTxiJLaLb7mW3T5k0DtWRd6atMtc6JGEEzkdVPlEcvHJ87SfzelY3vos4lzw9ZSPfjcNK-aigUTf17oXHlS7fhGmO3QQwIWbEyonDFjeAKwZQrHqPsC5mHHdk9lpCxqmjQpQa_TlruCZg2zWqIkp5L5c16fTivyJaabG0ueQ==', start_index=16205)
Annotation(end_index=16219, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkcNtRyj11JDrlsYpjsUs-ZFf9QjFe4YvG3l3usE_3SERiotvjMOYtDTenVO6JdHxZnXtKQZchMsuCqUZhASf4beW1R8xn9LBlH4IAUX_pXBwUhIR3KWQrTRs1geb-qUuvs0uUAjpRDguQMQ1WQ8L8nNKtCaLaeKV-76HBepQP85Tfhp9PBsOcghSxdS0X74B83Lj4GOoVWbNV-SeTq4RWMe-yQu8J', start_index=16205)
Annotation(end_index=16467, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxKsf4qK8ZgpcaQ8rTolW-0DDcczJWMPzmc66CrJV1XXnrFDn9iAlQZqn4q9ZVe_L6MwuafMm1LdwiL7itUmlv2QHAh-1QL542u1n7NxyKRwX-Ui67XqQr3agfhsVPowtZBkUgbhMLyBp-sEMJKV4RerxaCR6PMjFV11WFDpZtkkhlFWigsUiIqSTGqw==', start_index=16457)
Annotation(end_index=17018, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkcNtRyj11JDrlsYpjsUs-ZFf9QjFe4YvG3l3usE_3SERiotvjMOYtDTenVO6JdHxZnXtKQZchMsuCqUZhASf4beW1R8xn9LBlH4IAUX_pXBwUhIR3KWQrTRs1geb-qUuvs0uUAjpRDguQMQ1WQ8L8nNKtCaLaeKV-76HBepQP85Tfhp9PBsOcghSxdS0X74B83Lj4GOoVWbNV-SeTq4RWMe-yQu8J', start_index=17004)
Annotation(end_index=17018, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHU48UT_P2sabTK6gnvOct_9XdqVnWiOqoinKM7xZSsW2iAvVHcOpaeQBsQlIA5LSuA6IQRW-lYgPzyuLP9Utuv7HtmXH1B8ObiHaqXDShhHmD8T-ynJ1DiScNGDhjDEpXPhX8LD_lRWOSLFXDfgN3E-nLvAQl2', start_index=17004)
Annotation(end_index=17243, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC3lyCl0HrQnzZ67Li5YloMeKOlqPjSPSuc0N-ThGhbP8CinimXfHvqSOWX4t4WsIIrTU4jvTGHWl1Hxt2Sl0i3Tsa8QopCKoLn5zOlXUdHqleLQ7PS9zEluaV4eg=', start_index=17230)
Annotation(end_index=17243, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhmVKtPJwjS4gNsRQZhdNuj0GzxlQG5ZTB0tT4iXh18yXRXF14ngqr9wjZVuEzKi4F2RRmhpZvVXiRS1DDb-PcJkpHiEktInJgQCLize3WTyJqsJAOArNlHGTKCwjZTgkGPw==', start_index=17230)
Annotation(end_index=17401, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgcBrcz_dRhM4qn6_8OHhJY410NuWYDMsQA-Ag6TSAgpuiuLbnfQ_k0NyjZfngi-b0xSNKD6eY8mWn8X0N3TIDUvSxiFJ8igiQ8l_uSw9WB-PJbISf8z5RawKm8OgVwm4iWhTxV2_KY_BfVeg-EYoBtxj2T4XBocq1aA_hbjjEQ0e3iRqBMrWuUYQVmf7fa9B6dQ==', start_index=17387)
Annotation(end_index=17401, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGC895W4tIElBZzwQwz4-qd4jxOCFo4Bbyqh3gbLarM2-bBfu3sjq3zHOT3w8D4BoxBdiUa71ws39HEBnS9jdwXSagoHLXOobA8aLyVUL1vLRNNRLOC0y4MWv-vKk74IKm66r5a-CUNI2Kq6UniFy0DUlwwdyUgTrGHuyDteygeG8kdCLd0ex0jSAUztBl_9JGvU8-LVxiwhifmX3w=', start_index=17387)
Annotation(end_index=17585, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlYf0okx-RxpaJ2XdoJSratCMsv0XrUW7L48tZ3tV4Q7i7Jn7Mmavu8eRraj_ehv7ZG_iCq0H82N5Fi30YS2PvTHiwfMWE-Qc4XjoO-961xBk2XRAbnsi3CdeVD6-iDATRgWbKBUZ-oUjcNq-6TMw=', start_index=17573)
Annotation(end_index=17585, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsppUmPn3Z98fGA7Thamzevl6MgaiYwWX_q9T1hjudPLZBrhe2hwNRdVT5Q8Vihr_XD0fLiIVlTSQ68ceZsprt9MAPQhjYvHgNSIayan2d9cycqpgb69TmWwTB-3F3xIKlp6Jx', start_index=17573)

## Sources
