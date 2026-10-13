# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 605f30ff | **Time:** 430.18s | **Cost:** $1.71449
--------------------------------------------------------------------------------

# Comprehensive Analysis of Mitigation Strategies for Manufacturing Variations and Temperature Drift in Silicon Photonics

### Key Points
*   **Hydrogen Annealing for Loss Reduction:** High-temperature hydrogen annealing is currently the most effective fabrication technique for reducing scattering loss in silicon waveguides, capable of smoothing sidewall roughness to the atomic scale and reducing propagation losses to as low as 0.1 dB/cm [cite: 1, 2].
*   **Passive Athermalization:** To combat temperature drift without active power consumption, polymer claddings with negative thermo-optic coefficients (such as SU-8 or PSQ-LH) are overlaid on silicon waveguides. This can reduce the wavelength temperature dependence from ~70–80 pm/°C to less than 1–5 pm/°C [cite: 3].
*   **Subwavelength Grating (SWG) Engineering:** SWG waveguides offer a design-based solution that spatially averages manufacturing imperfections and allows for precise tailoring of the effective refractive index, enabling athermal behavior when combined with specific cladding materials [cite: 4, 5].
*   **Active Thermal Control & Machine Learning:** For high-density interconnects using resonant devices (e.g., microrings), active thermal tuning is essential. Recent advancements utilize machine learning algorithms to predict thermal crosstalk and optimize heater power in real-time, ensuring signal integrity for complex modulation formats like PAM-4 [cite: 6, 7].
*   **Etch Chemistry Optimization:** Controlling the ratio of fluorocarbon gases (e.g., CF4:CHF3) during plasma etching significantly reduces Line Edge Roughness (LER), a primary source of scattering loss, by balancing etching and polymer passivation [cite: 8].

---

## 1. Introduction

Silicon photonics (SiPh) has emerged as the preeminent technology for high-bandwidth optical interconnects, driven by the need for energy-efficient, high-speed data transmission in datacenters, high-performance computing (HPC), and emerging fields such as quantum computing and LiDAR [cite: 1, 9]. The platform leverages mature Complementary Metal-Oxide-Semiconductor (CMOS) manufacturing infrastructure to produce high-density photonic integrated circuits (PICs) at scale. However, the high refractive index contrast of silicon-on-insulator (SOI) waveguides, while beneficial for mode confinement and miniaturization, renders the platform extremely sensitive to nanometer-scale manufacturing imperfections and environmental fluctuations.

Two primary stochastic factors threaten the signal integrity of SiPh interconnects: **manufacturing process variations** and **temperature drift**. Process variations, such as lithographic inaccuracies and etch-induced sidewall roughness, lead to scattering losses and phase errors that degrade optical signal-to-noise ratios (OSNR) [cite: 10, 11]. Simultaneously, silicon’s high thermo-optic coefficient (TOC) causes significant spectral shifts in resonant devices (e.g., ring modulators) when subjected to temperature fluctuations, leading to signal misalignment and crosstalk [cite: 12, 13].

Maintaining signal integrity in high-bandwidth regimes—particularly when utilizing advanced modulation formats like Pulse Amplitude Modulation (PAM-4)—requires a multi-layered approach. This report provides an exhaustive analysis of the methods employed to mitigate these variations, ranging from atomic-scale fabrication treatments to machine-learning-assisted active control systems.

---

## 2. Manufacturing Process Variations and Loss Mechanisms

To understand the mitigation strategies, one must first characterize the nature of the losses and variations inherent in the fabrication process.

### 2.1 Scattering Loss and Sidewall Roughness
The dominant source of optical loss in sub-micrometer silicon waveguides is scattering caused by sidewall roughness. This roughness arises primarily during the dry etching process (Reactive Ion Etching or Inductively Coupled Plasma etching) used to define the waveguide structure.
*   **Mechanism:** The interaction of the optical mode with the rough interface between the silicon core and the cladding causes light to scatter out of the waveguide. This effect is exacerbated in high-confinement strip waveguides compared to rib waveguides [cite: 14, 15].
*   **Magnitude:** Standard lithography and etching processes can result in propagation losses ranging from 2 to 3 dB/cm, which is often too high for complex circuits requiring long delay lines or high-Q resonators [cite: 1, 2].
*   **Impact on Signal:** Scattering not only attenuates the signal power but can also induce back-reflections that destabilize laser sources and degrade the Bit Error Rate (BER) in high-speed links [cite: 8].

### 2.2 Dimensional Variability and Phase Errors
Beyond scattering, systematic and random variations in waveguide width and thickness (SOI layer thickness) are critical.
*   **Random Walk Variation:** Research indicates that process variation exhibits a "random walk" pattern with spatial extent. The variance of optical parameters (such as the peak wavelength of a resonator) increases linearly with the distance between devices on a wafer [cite: 10].
*   **Resonance Shifts:** A deviation in waveguide width of just 1 nm can shift the resonance wavelength of a ring resonator by nearly 1 nm. Given that Dense Wavelength Division Multiplexing (DWDM) channel spacings are often less than 1 nm, such variations can be catastrophic for yield [cite: 11].
*   **Thickness Variation:** Variations in the SOI thickness (typically 220 nm) across a wafer also significantly alter the effective index ($n_{eff}$) of the propagating mode, leading to phase errors in interferometric devices like Mach-Zehnder Interferometers (MZIs) [cite: 11].

---

## 3. Advanced Fabrication Techniques for Loss Reduction

Ensuring waveguide loss remains low enough to support high-bandwidth interconnects requires intervention at the fabrication level. Several advanced processing methods have been developed to smooth sidewalls and correct dimensional errors.

### 3.1 High-Temperature Hydrogen Annealing
Hydrogen (H2) annealing is widely regarded as the most effective technique for reducing sidewall roughness in silicon waveguides.
*   **Process:** The silicon waveguides are subjected to a high-temperature anneal (typically >800°C to 1000°C) in a hydrogen atmosphere. This process induces surface atom migration, effectively reflowing the silicon surface to minimize surface energy [cite: 1].
*   **Results:** This treatment transforms the rough, etched sidewalls into atomically smooth surfaces. Experimental results have demonstrated a reduction in propagation loss from ~2–3 dB/cm (as-etched) to unprecedented values of **0.1 dB/cm** for rib waveguides and **0.7 dB/cm** for strip waveguides [cite: 1, 2].
*   **Signal Integrity Benefits:** By minimizing scattering, H2 annealing significantly improves the Q-factor of resonators, which is crucial for narrow-bandwidth filtering and high-efficiency non-linear optical processing. It also reduces the insertion loss of delay lines used in optical buffers [cite: 1, 2].

### 3.2 Wet Chemical Oxidation
For thermal budgets where high-temperature annealing is not feasible (e.g., back-end-of-line integration), wet chemical oxidation provides an alternative smoothing mechanism.
*   **Methodology:** This technique involves a cyclic process of oxidizing the silicon surface using wet chemical agents (such as those used in RCA cleaning or Piranha solutions) followed by stripping the oxide with dilute hydrofluoric acid (HF).
*   **Mechanism:** The oxidation process is reaction-rate limited at the convex points of the roughness (peaks), meaning peaks oxidize faster than valleys. Stripping the oxide effectively removes the roughness [cite: 14, 16].
*   **Efficiency:** Studies have shown that this "multi-stepped" oxidation can reduce waveguide loss from ~9.2 dB/cm to ~1.9 dB/cm without significantly compromising the dimensional integrity of the waveguide, unlike thermal oxidation which consumes more silicon [cite: 16, 17, 18].

### 3.3 Plasma Etch Chemistry Optimization
The roughness of the sidewall is initially determined by the lithography and plasma etching steps. Optimizing the etch chemistry is a preventative measure.
*   **Gas Ratios:** The ratio of fluorocarbon gases, specifically $CF_4$ to $CHF_3$, plays a critical role. $CHF_3$ promotes polymer deposition on the sidewalls, which protects the profile but can induce roughness if not balanced with the etching action of $CF_4$.
*   **LER Reduction:** Adjusting the $CF_4:CHF_3$ ratio during the hard mask open step has been shown to reduce Line Edge Roughness (LER) by 26% to 43% compared to standard processes. This reduction in LER directly correlates to lower scattering losses [cite: 8].

### 3.4 Photonic Damascene Process (Silicon Nitride)
While the query focuses on silicon, many high-bandwidth interconnects utilize Silicon Nitride (SiN) for its lower nonlinearity and broad transparency.
*   **Technique:** The photonic damascene process avoids direct etching of the waveguide core. Instead, trenches are etched into the cladding, filled with the waveguide material (SiN), and then planarized using Chemical Mechanical Polishing (CMP).
*   **Outcome:** This method eliminates the sidewall roughness associated with etching the core material, achieving ultra-low losses of **0.1 dB/cm** without the need for high-temperature reflow, making it compatible with multi-layer stack integration [cite: 19, 20].

---

## 4. Passive Athermalization Strategies

Temperature drift is the second major threat to signal integrity. Silicon's high thermo-optic coefficient ($dn/dT \approx 1.8 \times 10^{-4} K^{-1}$) causes device performance to fluctuate with ambient temperature changes or self-heating. Passive athermalization seeks to cancel this effect without power-consuming heaters.

### 4.1 Negative Thermo-Optic Polymer Claddings
The most common passive strategy involves cladding the silicon waveguide with a material that possesses a negative thermo-optic coefficient.
*   **Materials:** Polymers such as **SU-8** and **PSQ-LH** are frequently used. These materials have TOCs ranging from $-1.0 \times 10^{-4} K^{-1}$ to $-2.4 \times 10^{-4} K^{-1}$ [cite: 3, 13, 21].
*   **Design Principle:** The effective index of the waveguide mode ($n_{eff}$) is a weighted sum of the indices of the core and the cladding, determined by the confinement factor. By narrowing the silicon waveguide (e.g., to ~350 nm width for TE mode), the optical mode is forced to expand into the polymer cladding.
*   **Compensation:** The negative TOC of the cladding counteracts the positive TOC of the silicon core.
*   **Performance:** This technique has successfully reduced the wavelength temperature dependence of ring resonators to less than **5 pm/°C**, and in some cases, less than **1 pm/°C**, which is over an order of magnitude improvement compared to standard unclad waveguides (~80 pm/°C) [cite: 3, 13, 22].

### 4.2 Subwavelength Grating (SWG) Engineering
SWG waveguides consist of periodic silicon segments with a pitch smaller than the wavelength of light, acting as a homogeneous medium with an engineered refractive index.
*   **Athermalization Mechanism:** SWGs allow for precise control over the mode confinement. By designing the duty cycle of the silicon segments, the overlap of the optical mode with the negative-TOC cladding (like SU-8) can be optimized to achieve athermal behavior for specific polarizations [cite: 4, 5].
*   **Advantages:** SWGs reduce the confinement in the silicon core, which not only aids in athermalization but also reduces the impact of sidewall roughness (spatial averaging), thereby improving loss characteristics simultaneously [cite: 5, 23].

---

## 5. Active Thermal Management and Tuning

While passive methods are effective, high-bandwidth interconnects often require dynamic control to compensate for runtime variations and thermal crosstalk, especially in Dense Wavelength Division Multiplexing (DWDM) systems.

### 5.1 Micro-Heaters and Phase Shifters
Active tuning is typically achieved using integrated micro-heaters (metallic TiN or doped silicon) placed near the waveguide.
*   **Function:** These heaters use the thermo-optic effect to locally increase the refractive index, thereby red-shifting the resonance wavelength to align with the laser grid.
*   **Challenges:** Heaters consume power (reducing energy efficiency) and generate thermal gradients that can affect neighboring devices (thermal crosstalk) [cite: 12, 24].
*   **Optimization:** To maintain signal integrity, the thermal time constant must be optimized. Fast thermal response is preferred for stabilization loops, while efficient thermal isolation (e.g., using undercut trenches) is required to minimize power consumption and crosstalk [cite: 24, 25].

### 5.2 Feedback Control Loops
To ensure low loss and signal integrity during operation, closed-loop feedback systems are employed.
*   **Mechanism:** A small fraction of the optical power is tapped and monitored (e.g., using a contactless integrated photodetector or measuring heater resistance changes). This signal is fed into a controller (PID or digital) that adjusts the heater power to lock the resonator to the correct wavelength [cite: 26].
*   **Dithering:** Techniques like dithering (applying a small AC modulation to the heater) allow the controller to detect the direction of the drift and maintain the optimal operating point (maximum transmission or extinction ratio) [cite: 6].

### 5.3 Managing Thermal Crosstalk
In dense PICs, heat from one device can detune a neighbor.
*   **Impact:** A temperature variation of a few degrees can completely offset a filter's passband.
*   **Mitigation:** Thermal eigenmode decomposition is a sophisticated method used to decouple thermally coupled systems. Additionally, physical isolation trenches and heat shunts (using metal layers) are designed to direct heat flow away from sensitive components [cite: 25, 27, 28].

---

## 6. Machine Learning for Process and Thermal Compensation

The complexity of modern SiPh circuits has outpaced simple analytical models. Machine Learning (ML) is now pivotal in ensuring yield and performance.

### 6.1 Predictive Modeling of Process Variations
ML algorithms are used to map fabrication data to device performance.
*   **Application:** By training models on wafer-scale test data, designers can predict how specific layout patterns will suffer from lithographic proximity effects or etch lag.
*   **Outcome:** This allows for "pre-distortion" of the design (Optical Proximity Correction) or the selection of optimal operating points that are robust to the predicted variations. Simple linear regression models with variable selection have shown high interpretability and low prediction error for waveguide losses [cite: 10, 11, 29].

### 6.2 Neural Network Control of Weight Banks
In applications like optical neural networks or programmable meshes, microring weight banks must be precisely controlled.
*   **Challenge:** These banks suffer from severe thermal crosstalk and fabrication mismatch.
*   **ML Solution:** Neural networks can learn the complex, non-linear thermal crosstalk matrix of the chip. Once trained, the model can predict the exact heater currents required to set a specific state for all rings simultaneously, compensating for both static process errors and dynamic thermal coupling [cite: 6, 7, 30].
*   **Accuracy:** Recent demonstrations show ML control achieving weight accuracy of up to 8.5–9 bits, significantly outperforming standard feedback methods [cite: 6].

---

## 7. Signal Integrity in High-Bandwidth Interconnects

The ultimate goal of these mitigation strategies is to preserve the integrity of high-speed data signals.

### 7.1 PAM-4 Modulation Sensitivity
Pulse Amplitude Modulation (PAM-4) encodes two bits per symbol, doubling the bandwidth but significantly reducing the Signal-to-Noise Ratio (SNR) tolerance compared to NRZ (Non-Return-to-Zero).
*   **Loss Sensitivity:** Because PAM-4 has multiple signal levels, it is far more susceptible to amplitude attenuation (insertion loss) and noise. Waveguide loss directly degrades the Optical Modulation Amplitude (OMA), closing the "eye diagram" and increasing BER [cite: 31, 32].
*   **Linearity:** Process variations that affect the linearity of modulators (e.g., MZI transfer functions) are critical. ML-assisted compensation and active tuning are required to ensure the modulator operates in its linear regime to prevent level compression in the PAM-4 signal [cite: 32, 33].

### 7.2 Impact on Quantum and Coherent Systems
For quantum photonics and coherent interconnects, loss is even more critical.
*   **Quantum:** In entangled photon pair generation, any propagation loss destroys the quantum state (decoherence). The reduction of loss to 0.1 dB/cm via H2 annealing has been explicitly linked to enabling high-fidelity quantum sources [cite: 1, 2, 34].
*   **Coherent:** Phase errors caused by temperature drift or thickness variations scramble the phase information in coherent transmission. Athermal design and precise phase tuning are prerequisites for these systems [cite: 11, 13].

---

## 8. Conclusion

Ensuring low loss and maintaining signal integrity in silicon photonics requires a holistic strategy that spans the entire device lifecycle. **Fabrication-level interventions**, particularly high-temperature hydrogen annealing and optimized etch chemistries, provide the foundational low-loss waveguides (down to 0.1 dB/cm) necessary for signal transport. **Design-level strategies**, such as polymer-clad athermal waveguides and subwavelength gratings, passively immunize the circuit against temperature fluctuations. Finally, **system-level active control**, increasingly powered by machine learning, dynamically compensates for residual process variations and runtime thermal crosstalk. This multi-faceted approach is essential for scaling silicon photonics to meet the terabit-scale bandwidth demands of future optical interconnects.

### References
[cite: 12] [cite: 12, 24]
[cite: 27] [cite: 25, 27]
[cite: 10] [cite: 10]
[cite: 26] [cite: 26, 35]
[cite: 24] [cite: 24, 25]
[cite: 14] [cite: 14, 15]
[cite: 8] [cite: 8]
[cite: 36] [cite: 1, 2]
[cite: 37] [cite: 19, 20]
[cite: 1] [cite: 11]
[cite: 2] [cite: 13, 21]
[cite: 38] [cite: 4, 5]
[cite: 19] [cite: 3]
[cite: 11] [cite: 2, 34]
[cite: 13] [cite: 10, 29]
[cite: 4] [cite: 31, 32]
[cite: 3] [cite: 33, 39]
[cite: 40] [cite: 6]
[cite: 41] [cite: 16, 17]
[cite: 15] [cite: 19, 20]
[cite: 42] [cite: 1, 2]
[cite: 2] [cite: 3, 22]
[cite: 43] [cite: 7, 30]
[cite: 44] [cite: 5, 23]

**Sources:**
1. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsTk99Mi09EaFD7Fu54rU5cwuMvPqbjbI35GeGIl-CMpF5UknTT3gLeJaB3vyvrykhLA_V3OxGB8IAYRNiTW-AfxOuwcA_govmuO7scobSFjN53Fbprj-WO9jRSpbc7_s3)
2. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELWTiEfICUgZYXk9ITwiTxLY0shBbr7_Sa-uHLsg7nvUxTHDwG_x55UVPrd57zojSQo_StNIs5Yn--hZ0QW9hcGt07Yq2q9H_s6uRRy4MWfM1RdmOWVXJsoCwVXdHHIaSM)
3. [ugent.be](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERrSJ_FHP0yafolVLEKo9LcKc9f6B7XXg6Aoe5sCIvb6BXN4bLXoyBzCehM289re6l89-VoE4z8ZxO92TZwftZ4Tahkqvr5md7mFRyfXvweGc05gOWKRQPMDLArumzXYI8BSBPcqHF5Sj6Ww07mqdV)
4. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPyLiHTm0Uc1ltuDciAg5SAW7hcETK0sgC_th_7TXLiFEQRV2ySmKmnTMDjyFOUwHB3caQilFqIh_8njjwxQXS7yJlsaNx-SyPZgU5gsqI_0MzfuRwJ8RTBPA2Su_RuE6l7ZEXO8l5g4xAAoyG)
5. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECNT5AD040KcwPcFt42ERZNbaqVqBAM1t9KdPD8qJbK0THel8NuCXNCg6E79zU0zaKTQzZOf7VsS-k2i_J6XGjl9xLrWbP9AGX5dD58CX0LBNK7GaKBxO8BNZXN5Fj0sO42ov1IyS88EyX)
6. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_4H8uvxQsQu4ayLnXZE6fpGqQq_mJhNrmKGQ2ZGVZcKrEev9sd6PxbxJL38-TYWUzK8IbFidMtweDn03afVsTSnRxfxq30qZGtq5SJdX_TmlGUp5jQQ==)
7. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwwqgol-pc-8dfHZoOkzOS_ARoQKwO0RMiAeQ5Fyz2y5musc-eklezMzMywWY_nE0sJbJftVW2_iuoHtV75OgJpMSfCMYpSNmFexy-QhOURQ6zyZIMrw==)
8. [osti.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVV1lxNsXf_29vtBaLpIWg1GvI0kIvEEwAuSxbfLfQiluSVXodWK06FvTp19y61PGiQC8n6XMIyGg0p8UDuuBB6-DD7FqJ85uY-QRF-HbReANivshQYuV9AE7ooVKPgJA=)
9. [snsinsider.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqKKtiEewKaPONGSyw3JDWj46H1_ibirLsWJEbxNgNiwqG5wMyzT_PO3sdkw3ztYZud_IAHEtnjsAF43dnsTZP7JET_g-dRQ70EDvXZiNO8wY562maefW3BlzYE5pvmibqaKSNP-28DYXlMT9Gqcs1I4qw1KWA)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBRgUmu4pczp8nnK4UCW28I3Yw9__KkfaVMmUZnTZfT5rO0Mbj44aQEFaHB9rRGMlNifhlprqvJISKks5KtBDnehGNtTjUPw_sAmtlMDZGfw37EeVt0Yy5yxgSxNVk3Y6PNKrk9FbtU6oNzqBSqO_CGjIRg1xMSa03YLtJoaArE-6un9MQy6LhRdn092e3bcuOPk7xULs=)
11. [ugent.be](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF02_1rRjIlkNeMM3UINb-W3oROdA3sKgr1NsnF1z92REwShLj2TGZ_83s8_GCTk9Fq58tnHy3Q13BXUmyNVPAKv9yVdNCgZDMf0lW-IsAwJarKynZTTXPXCBnISv2b3hvUa1KDUBjEvb8UD06CXjIR)
12. [poc.com.sg](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcWB_PI2SXWY_VxZn6U5qA_rYCFcT7gYn6tvfgmX5E1gzY3HwKdBnDLjojgVvSjXfCJFt-K9-XbiOyvQFHnC9tc_yo5pqdAP3I2Zk10EUHzlG7c83cy-5pAdZeUU3Gm0hsxW7dEvTL8PT6Uyvori6xJq2GPdU=)
13. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl2DcxKnGTD5lRp6sDEKfMGzgFaWelDeUV1IOfCPPgW5XYfOO5H9jV-lpyLbE7U5R5bJTgvQ-W41668wgKaIbobk8i3gRx6x0F9MNxrx7Tsj-vZoy2Gv-WDrvowJe3sfT8V7ljx-LXwcj7ue0=)
14. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8hJ7sGzxWxJG4VLhaIvI4EwImFstsJZUpXOaUm0EI3Lt-f2G6m7XdNcIUy8ckumTF1-TUjNhidUSGt56lsYL9FwaLYYM3Fb0SVBGORMWKki2z_yoszbgIYt0FnBpMDRVHiK3qo_dUSDkduQ==)
15. [telecom-paristech.fr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXVJM8Z64j_lfxs-3FxXf96LIFEZK4i6xccam9Y5g_4S4FRGx5pLhiS6lzwDfHtFMrTL5unu5Fl813U3qd34ZfKp9YT_OAfQIx8iRcT6D28YEhOt50Z2AA5TeMolhjvhVRPZl3gzVZKGme81kDrAE=)
16. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYLkXfJRoi-MOd87Z6lzSQGGJS5skeKhPMW4ZT4qAnNp21QjdiIGBBPqG1KhvGIkEsPGQnuSWAqKwjwe2_riMnlu4wBTlPUDX7mI1p9xmWErPZ-gBKLylYmANFLpCv3aWGJdXq_jbftS9X9bw=)
17. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGt1HQ-F1SJ1L7MHnG-QfuzCFbPdMAvLqpCA9hRgRbfN5Rz7JgegNBMGew8eWD5GZgyeTeb_1o_1nahyWW63kLA5Rj3MPStaz1RFlErY9VaGSM8OxxvzpDey1JLGzpNpMHMYkc2g_Zj_2vDKg==)
18. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs3C0RnVpctRATQNH-og5t5tTKEWPWqasFbLkF7GcDS8j_jZfk1gdOgmVb44MKi_7x-ENjbjR-gyonBoq-ihMwX3XlcoXjxRDZKNSKnDK5ezvNyTGZSe-5yNk29-_Vd_yWTNJw6l4OICxCtw2-FrsS2BXeJtEUpSZrlbuHTrFq__YTZ333CdEs5RpOa5GYt-PpS6VHP068UgMiHyn9jeQMoTvzSqzlvzOE9m051czYoE7e-S9vBy_N-2v89FZZEJlfpw==)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuMyDqcbkVkEKqT2vsOW188JTJOG1TWWLrEuccbV55QAbGwXjc5hICwXXIQGShben3nGsM9Pc1_mOPo9Y3hIxJCD1oop_5uPljqgO6ejMJYx3b03FMJMi6JmMWPD4mwyfNluTZaFZQak5NmIqdzmrZBXX1iUpD7NUMqq382GlpTaI1Oh8uKkwTXc277ViF0sZklG-CTiMRFa8HIitQ8qVT7YDFTwDCnJc5ZYfb-w==)
20. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyMflzSgkakLcm8LqzE8y68t2hb5PzFiKVNfVV4QJ9BN3P0-u-SzaWcPVcvH9f9zlNceWo1EY_NSAY-jeQKZ8UCbMlK1lhkKn50ITIqgPryY8mHkTJGDpVcL1gnz3E)
21. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmU7vl64q0PLD2F1smLwnnXhX201CI7XcsN775B0U-zLT9zGXqfajfuemjsKhOceNdGKdYPvXOD7P3Uc7rPYs5XEiqU2v2QCq7dbp7-l_QbaK5P-gyAPHD-Jl2FOg=)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXOA9rpgY_4dK5fejt9ONCWpA7ORFb3L9r2eiVJrZPVNeIRHE1XIj_gqTTxjrOy8v3XBYWDFLiT23SVsBsHRf5wlsw5wXn94ILugYy-76XYOSLu5iFvKoGQehqgGv4ZVb5x2glLc7Aik-P3YGWePAssl5h8FYFc1xmL7c72Ge39mOAq9S4X2ri2aazm7vykI_MLpLspZJQfsc9zC1_A6GsmRk5hvu7Y34VoW082hxQ9-0zMB6gFmkGkiDovA_l7Bd8sef8862lvWjulPAI-w==)
23. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESdoY1U8YpHUzodh3AmFbJ_VNI_KmlJtriPTQBOY11gdlOnXZ4gKP8kE2z9kWZkvCsVrY1YXvZgaB_oF5IImqwmFbibYQy27RmUej7wAcN8V-NaJOwN-N4QKhcaaP-xQ==)
24. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiRRWJV1r9KJVKe7kov5MYANoG9VC67yJfGuvZRTutYL912UCpzY7LVvznxc4htaGu0ktXDTsFs7qiik_uk25IXLX3P_U4EAQ-rMi026gpDhRMJbolNVFhZRNobbQ=)
25. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4o6EHzwFtAVwDoMQnzVq32OKf_93RBNELJA6yDmqvPfAEVk_37cCnax2cZ4xY8CGfRZwqEBK4WHg-yv9RiHkLLW205YmtkULU9bBmdEmz3dzFPNwRCHwhYOVG5rHK15oumlyYk9KJzX7x2Va30u_BdYg0vHwiGqgKvaMJHBHi5V5kpcjXp1gVy8rn7RDLY_UbvZEGzGpWssYHUeeg)
26. [cern.ch](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYghlyg8GZmNrihRE2TkB9P3EIz59EW97ugYmebF8GgpqHuWi5CuyQsRk9pcC_3VvXCmGeOi2GuddysKe6mbK-F4p0paAEdpmGpAXvNyfaUgwsBd_ZaaJmzsq2LPL9oHj_xlCAX_m46uKItXJQA5aAVH1WXZ9Z92b8JjVmmGf5HE_GNKvFcOzV8pT0Hev3YSo8t4koPT1fyH1ntvXVuJBKMCITBIeMWcotySU_Icv84M_Pnez33eCsiS-LeOk=)
27. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGP_1_n8Ezj9dy0nA4QI72vRgwih8Q7hSNf1-4HGTplYun3y51G8_ks-YGaH-YqOrOLEgaZ5MvFfl3hW1ELRkMOJ5uL_H7WZeKBnj1gcFG9QH4J2NY2orq85t2TJNzPFiuNsJ5yTWbvM9avmYcmfQglgQC8ec4Sy1I-6jCovCCYvPHNDKgMhQwnqtA5XAEIdutm41Ui6CAaVZh6iRGqxA=)
28. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETNg84CKGyhAg_tlq2rtjmNkS6l0fz4ydhgzWD47FspuMRAfnN-4OyqcaAWxXsgIg3q0eiBogmItcXlEBmOu0FDegnWlRzfPE2mHPD1GjfHXIrUv6RW52VZuOg46sEwtD5NisbBogoXXVPSKLz0GmfLQAND0bMPtSnve56y5EtwSJDHZkVFXVQnDw=)
29. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEG0kkrb9JTAXnJkQ2sVdO_y7muCW6KUtR5sU0R_y2MFHIcqnjpdqkEh8kGHf4PXheh-nc87aDi6LIHB62GWAx2kDWCW9jp2IcmS_lt2_nZfQmtbUIDlg==)
30. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGM8MVaPw2XrHnDAK1T9_eG9ymFdZohSijqFoKvoymm_MLUX0ltVmKu03OaINWNydaHGyrt7wEWDL3nEggRiruJxIFQZ3A9mMaOFT-F3fhBx7jw48wvNwERMQHwahI=)
31. [signalintegrityjournal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEbLz2eEDRTowQhvU3D1KEnnwt464C3qRsanqk7gBoQfZ6Yr4POuswLUDnEjABMOD6pBJzqLvbri0B9NV-nEi4ohkHPOYTUsEDQpkMcrFFfmMKaSNqYKFcz4CnRg8__5uB2acJga5fD1yidAqrVfsf9qcW-i67TW_dTOQ2iTRGD4iXJes=)
32. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpUpzHgL1tOS2UBnK-JTk1ms3tZ_fS0Nf37ME4HLRr4JKSJl-hQ3TCfVrC9wOLrGP6e1bfqVteZzCuFgU4LusZMLTkD9hOJ9HE55DCJACqQm0VZKo8hA==)
33. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6gYYcwpn7dQtwO4tyWT93kzRiKWqcDiq-cKqldNZMnx9F0WssgI3-VndntALgC9RyjxTabx7FTUjIusFr0lyB0r_er9dgfZk5B2AYnMu2o9t0XkI5OaYA0yhmM0zTsQquE7qV27UCIHxTYJUiEaklDV0kmPq4uxjJdvWIh9_F3XMXuBt09te1gt8uwmsjm9MgkgFaQUFLmDtDDd1d3O5XFWri8SSY3BO-hccTWIiEjP2iTtEza5jDDOkDIfwy0YjElpx4rRk=)
34. [spie.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGID_bx-KPkJB_ih-f9lx1FAjArlQcMj10ZUTsj41Io1M8npZTYDSquKch9TBJpPiFjLH47wjKnHoQtFvzgk4G4aSHtoZP31KuisFW9OLnkpZNxXo9ZiVyyjQh3n65TWYkq_9sLq4o1Bw0Fl5E=)
35. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyH00-mseESPFt5K7Tr5h8MKEhoRUimmJSdH1_4hkKRYEQufTrg72g6fUb8peddd-Mzi2P2oS0ngvomW2EXuH47qPs9qBYBbtEholPjjXWAGXMUgyBziK3MyAp1c7g0fVrwZ1XJWpXHrxE6xI=)
36. [tuwien.at](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGMNmOGWmK1IkIzDeU-86LgrGoqgq0EfOB90faHAaEklInYj5at_UbGTy6M1xF69Cw6gtAz84qOpq-G10rp4wkgvxer4ZL9BXaUFa9uvWNXa4bm6DvfP0HB9g4SotEloxt6WdnP5cO-pu-_SNOViqVQknslUQJKR1aV7Qe6o5zHp2k_zcuxx5MgEIsH-tw0C-PTRGRScL2cQEIm5K-2JeMwDyozwsSxIKpVMraoUGD5vaXMDjMxU5mgfSrFwypCzNtsgGB-Wyu0vUXIvY-buCKAEpubfSilShsow8V-yXdt60=)
37. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEts6qWND0DiX5bqpxsElgyZjtgd43xVMO1LMagXtvn79oQira9S_S1ikJpn_BtNOMxLhx5s_tbzSMBe0vcpqcdxKwHurHaPHcW51u2MvaXOlHHpQPt627ufE48HJfMeKyMAdu7blZxzI_u6p9t0WROT7kidrJPJF80U8ZTnWXFhxeLcVuAspJgFEB6eAQzmXZOtvcsjvO4E7IO2kabFJk1A_Xxf2mfpD6zmrGS4TcckaW3JXbhCsnPzQQ=)
38. [soton.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTIQpRTYMLCvuVluUwm6f5pYmPUiZk6nllVvmsurCKgqKZ9elTyoUOPQJWtWnZ4TANbuT8qKu2B1QmCLZHQWRNvvm7J1ifbWpYJ0jQEZFTIZuayLwhNqdGSn9TpkudL2pPwatkWNnnp9F39w==)
39. [caltech.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdo51B4ss_XUyBxOKLxELKYkDux5O-hpdvW0VWL3D2A4xNBd0sGhc8fU186OSpK8DuPPIPKVepPhVSEfbeSVkDvGKZ2Iwfs6UGuLTebW8M19-dD3EmaENymTeCTw8g4R0cLcDFzw8Yh8pDctRtVTk6aMxaLLLJzJtif3Rlpv6R0g==)
40. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLDukJNfc1MwvbNmOCRD6gwI2haH2uvnr6JZsQvxfdGFETc3aYjMesXrnl7u0uw04um823gjqv3fBnuU5fjKXLB7IGVs7PpspFWy_WGJs4Dd5xJ9Dpg4jXIQk_LnhAPGBrj04R7gpkDdf9Vw==)
41. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQSBkgk-5l0JCzWAKG6VmA7MCq9NwaMGXMPiHvoRdUYF5e0pX4bZ88zRkIccddSS4aLWD13iSfhYTMia2bqPf8-Z9OqJwjxc--wbpRlw_4lS_fKtbNiyd0TW_th8N9xvNTMYz5yGoV8n46knX3TjOOewQ2Qw==)
42. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYIUGnKj7FQaofoKc15TtbEAzuAMsJwih5N7eJm5__riXDWASDsRPMzaKM8-WNTYZPC5XAQCMVAH1xLxHbFP49GJvZcU6HkxuXWBKGvwPwvz5cp3IGz0SerIf8kM4=)
43. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5pqxsksoE_qRw-9tsOPOgrQDBpR3g-GwfPIjpf4RJxyyXSY9Rl1jTaHBPr2SVSfiSKQSCJAQEIppP6UmT1mOSkjb3DEGt8dcSG0D2hqOi5uBcMUZ4yD0QXn2paPTS2zHJ5xaPolP_DacD6uM8AOmFU8jwNwFXJCm-XPvXHsFXZfIi9BDR7H3XgpoDYtQ6HH1wkOKD271cvG1DvKmdM38DJzf-XE81pDrQ4xWxUw==)
44. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESGhTfa0c4lmfGLiqBGPVoi03-I0341ziRjvyZcCMy4HdzzTWPWNtQIADfEdIUkM7do1KpdWinT04K2PAfdqq5wnmlveTHsCngXofnq0W9v7o9FS7kiF8nXVdsGxeII1bne1MX6TMfJGTz4efzASoDiX9iM6lPfZd9jyCOFNbBIdaxWqhfeoTwyQxi7NNrsLNNpz2cpm3-hZMiHL_M56krB5omft99S8Z7vPDhtFetjjuSE-bSCsRkV9_Y2DHsBfXeR5OtsFWVkHWnVPVcFONo_bu3ziTcbG3S4QsL)


## Annotations
Annotation(end_index=454, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELWTiEfICUgZYXk9ITwiTxLY0shBbr7_Sa-uHLsg7nvUxTHDwG_x55UVPrd57zojSQo_StNIs5Yn--hZ0QW9hcGt07Yq2q9H_s6uRRy4MWfM1RdmOWVXJsoCwVXdHHIaSM', start_index=442)
Annotation(end_index=454, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsTk99Mi09EaFD7Fu54rU5cwuMvPqbjbI35GeGIl-CMpF5UknTT3gLeJaB3vyvrykhLA_V3OxGB8IAYRNiTW-AfxOuwcA_govmuO7scobSFjN53Fbprj-WO9jRSpbc7_s3', start_index=442)
Annotation(end_index=780, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERrSJ_FHP0yafolVLEKo9LcKc9f6B7XXg6Aoe5sCIvb6BXN4bLXoyBzCehM289re6l89-VoE4z8ZxO92TZwftZ4Tahkqvr5md7mFRyfXvweGc05gOWKRQPMDLArumzXYI8BSBPcqHF5Sj6Ww07mqdV', start_index=771)
Annotation(end_index=1082, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECNT5AD040KcwPcFt42ERZNbaqVqBAM1t9KdPD8qJbK0THel8NuCXNCg6E79zU0zaKTQzZOf7VsS-k2i_J6XGjl9xLrWbP9AGX5dD58CX0LBNK7GaKBxO8BNZXN5Fj0sO42ov1IyS88EyX', start_index=1070)
Annotation(end_index=1082, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPyLiHTm0Uc1ltuDciAg5SAW7hcETK0sgC_th_7TXLiFEQRV2ySmKmnTMDjyFOUwHB3caQilFqIh_8njjwxQXS7yJlsaNx-SyPZgU5gsqI_0MzfuRwJ8RTBPA2Su_RuE6l7ZEXO8l5g4xAAoyG', start_index=1070)
Annotation(end_index=1450, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwwqgol-pc-8dfHZoOkzOS_ARoQKwO0RMiAeQ5Fyz2y5musc-eklezMzMywWY_nE0sJbJftVW2_iuoHtV75OgJpMSfCMYpSNmFexy-QhOURQ6zyZIMrw==', start_index=1438)
Annotation(end_index=1450, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_4H8uvxQsQu4ayLnXZE6fpGqQq_mJhNrmKGQ2ZGVZcKrEev9sd6PxbxJL38-TYWUzK8IbFidMtweDn03afVsTSnRxfxq30qZGtq5SJdX_TmlGUp5jQQ==', start_index=1438)
Annotation(end_index=1712, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVV1lxNsXf_29vtBaLpIWg1GvI0kIvEEwAuSxbfLfQiluSVXodWK06FvTp19y61PGiQC8n6XMIyGg0p8UDuuBB6-DD7FqJ85uY-QRF-HbReANivshQYuV9AE7ooVKPgJA=', start_index=1703)
Annotation(end_index=2036, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqKKtiEewKaPONGSyw3JDWj46H1_ibirLsWJEbxNgNiwqG5wMyzT_PO3sdkw3ztYZud_IAHEtnjsAF43dnsTZP7JET_g-dRQ70EDvXZiNO8wY562maefW3BlzYE5pvmibqaKSNP-28DYXlMT9Gqcs1I4qw1KWA', start_index=2024)
Annotation(end_index=2036, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsTk99Mi09EaFD7Fu54rU5cwuMvPqbjbI35GeGIl-CMpF5UknTT3gLeJaB3vyvrykhLA_V3OxGB8IAYRNiTW-AfxOuwcA_govmuO7scobSFjN53Fbprj-WO9jRSpbc7_s3', start_index=2024)
Annotation(end_index=2827, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBRgUmu4pczp8nnK4UCW28I3Yw9__KkfaVMmUZnTZfT5rO0Mbj44aQEFaHB9rRGMlNifhlprqvJISKks5KtBDnehGNtTjUPw_sAmtlMDZGfw37EeVt0Yy5yxgSxNVk3Y6PNKrk9FbtU6oNzqBSqO_CGjIRg1xMSa03YLtJoaArE-6un9MQy6LhRdn092e3bcuOPk7xULs=', start_index=2813)
Annotation(end_index=2827, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF02_1rRjIlkNeMM3UINb-W3oROdA3sKgr1NsnF1z92REwShLj2TGZ_83s8_GCTk9Fq58tnHy3Q13BXUmyNVPAKv9yVdNCgZDMf0lW-IsAwJarKynZTTXPXCBnISv2b3hvUa1KDUBjEvb8UD06CXjIR', start_index=2813)
Annotation(end_index=3075, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl2DcxKnGTD5lRp6sDEKfMGzgFaWelDeUV1IOfCPPgW5XYfOO5H9jV-lpyLbE7U5R5bJTgvQ-W41668wgKaIbobk8i3gRx6x0F9MNxrx7Tsj-vZoy2Gv-WDrvowJe3sfT8V7ljx-LXwcj7ue0=', start_index=3061)
Annotation(end_index=3075, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcWB_PI2SXWY_VxZn6U5qA_rYCFcT7gYn6tvfgmX5E1gzY3HwKdBnDLjojgVvSjXfCJFt-K9-XbiOyvQFHnC9tc_yo5pqdAP3I2Zk10EUHzlG7c83cy-5pAdZeUU3Gm0hsxW7dEvTL8PT6Uyvori6xJq2GPdU=', start_index=3061)
Annotation(end_index=4282, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXVJM8Z64j_lfxs-3FxXf96LIFEZK4i6xccam9Y5g_4S4FRGx5pLhiS6lzwDfHtFMrTL5unu5Fl813U3qd34ZfKp9YT_OAfQIx8iRcT6D28YEhOt50Z2AA5TeMolhjvhVRPZl3gzVZKGme81kDrAE=', start_index=4268)
Annotation(end_index=4282, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8hJ7sGzxWxJG4VLhaIvI4EwImFstsJZUpXOaUm0EI3Lt-f2G6m7XdNcIUy8ckumTF1-TUjNhidUSGt56lsYL9FwaLYYM3Fb0SVBGORMWKki2z_yoszbgIYt0FnBpMDRVHiK3qo_dUSDkduQ==', start_index=4268)
Annotation(end_index=4511, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELWTiEfICUgZYXk9ITwiTxLY0shBbr7_Sa-uHLsg7nvUxTHDwG_x55UVPrd57zojSQo_StNIs5Yn--hZ0QW9hcGt07Yq2q9H_s6uRRy4MWfM1RdmOWVXJsoCwVXdHHIaSM', start_index=4499)
Annotation(end_index=4511, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsTk99Mi09EaFD7Fu54rU5cwuMvPqbjbI35GeGIl-CMpF5UknTT3gLeJaB3vyvrykhLA_V3OxGB8IAYRNiTW-AfxOuwcA_govmuO7scobSFjN53Fbprj-WO9jRSpbc7_s3', start_index=4499)
Annotation(end_index=4721, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVV1lxNsXf_29vtBaLpIWg1GvI0kIvEEwAuSxbfLfQiluSVXodWK06FvTp19y61PGiQC8n6XMIyGg0p8UDuuBB6-DD7FqJ85uY-QRF-HbReANivshQYuV9AE7ooVKPgJA=', start_index=4712)
Annotation(end_index=5175, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBRgUmu4pczp8nnK4UCW28I3Yw9__KkfaVMmUZnTZfT5rO0Mbj44aQEFaHB9rRGMlNifhlprqvJISKks5KtBDnehGNtTjUPw_sAmtlMDZGfw37EeVt0Yy5yxgSxNVk3Y6PNKrk9FbtU6oNzqBSqO_CGjIRg1xMSa03YLtJoaArE-6un9MQy6LhRdn092e3bcuOPk7xULs=', start_index=5165)
Annotation(end_index=5474, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF02_1rRjIlkNeMM3UINb-W3oROdA3sKgr1NsnF1z92REwShLj2TGZ_83s8_GCTk9Fq58tnHy3Q13BXUmyNVPAKv9yVdNCgZDMf0lW-IsAwJarKynZTTXPXCBnISv2b3hvUa1KDUBjEvb8UD06CXjIR', start_index=5464)
Annotation(end_index=5755, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF02_1rRjIlkNeMM3UINb-W3oROdA3sKgr1NsnF1z92REwShLj2TGZ_83s8_GCTk9Fq58tnHy3Q13BXUmyNVPAKv9yVdNCgZDMf0lW-IsAwJarKynZTTXPXCBnISv2b3hvUa1KDUBjEvb8UD06CXjIR', start_index=5745)
Annotation(end_index=6498, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsTk99Mi09EaFD7Fu54rU5cwuMvPqbjbI35GeGIl-CMpF5UknTT3gLeJaB3vyvrykhLA_V3OxGB8IAYRNiTW-AfxOuwcA_govmuO7scobSFjN53Fbprj-WO9jRSpbc7_s3', start_index=6489)
Annotation(end_index=6816, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELWTiEfICUgZYXk9ITwiTxLY0shBbr7_Sa-uHLsg7nvUxTHDwG_x55UVPrd57zojSQo_StNIs5Yn--hZ0QW9hcGt07Yq2q9H_s6uRRy4MWfM1RdmOWVXJsoCwVXdHHIaSM', start_index=6804)
Annotation(end_index=6816, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsTk99Mi09EaFD7Fu54rU5cwuMvPqbjbI35GeGIl-CMpF5UknTT3gLeJaB3vyvrykhLA_V3OxGB8IAYRNiTW-AfxOuwcA_govmuO7scobSFjN53Fbprj-WO9jRSpbc7_s3', start_index=6804)
Annotation(end_index=7128, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELWTiEfICUgZYXk9ITwiTxLY0shBbr7_Sa-uHLsg7nvUxTHDwG_x55UVPrd57zojSQo_StNIs5Yn--hZ0QW9hcGt07Yq2q9H_s6uRRy4MWfM1RdmOWVXJsoCwVXdHHIaSM', start_index=7116)
Annotation(end_index=7128, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsTk99Mi09EaFD7Fu54rU5cwuMvPqbjbI35GeGIl-CMpF5UknTT3gLeJaB3vyvrykhLA_V3OxGB8IAYRNiTW-AfxOuwcA_govmuO7scobSFjN53Fbprj-WO9jRSpbc7_s3', start_index=7116)
Annotation(end_index=7808, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYLkXfJRoi-MOd87Z6lzSQGGJS5skeKhPMW4ZT4qAnNp21QjdiIGBBPqG1KhvGIkEsPGQnuSWAqKwjwe2_riMnlu4wBTlPUDX7mI1p9xmWErPZ-gBKLylYmANFLpCv3aWGJdXq_jbftS9X9bw=', start_index=7794)
Annotation(end_index=7808, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8hJ7sGzxWxJG4VLhaIvI4EwImFstsJZUpXOaUm0EI3Lt-f2G6m7XdNcIUy8ckumTF1-TUjNhidUSGt56lsYL9FwaLYYM3Fb0SVBGORMWKki2z_yoszbgIYt0FnBpMDRVHiK3qo_dUSDkduQ==', start_index=7794)
Annotation(end_index=8091, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYLkXfJRoi-MOd87Z6lzSQGGJS5skeKhPMW4ZT4qAnNp21QjdiIGBBPqG1KhvGIkEsPGQnuSWAqKwjwe2_riMnlu4wBTlPUDX7mI1p9xmWErPZ-gBKLylYmANFLpCv3aWGJdXq_jbftS9X9bw=', start_index=8073)
Annotation(end_index=8091, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs3C0RnVpctRATQNH-og5t5tTKEWPWqasFbLkF7GcDS8j_jZfk1gdOgmVb44MKi_7x-ENjbjR-gyonBoq-ihMwX3XlcoXjxRDZKNSKnDK5ezvNyTGZSe-5yNk29-_Vd_yWTNJw6l4OICxCtw2-FrsS2BXeJtEUpSZrlbuHTrFq__YTZ333CdEs5RpOa5GYt-PpS6VHP068UgMiHyn9jeQMoTvzSqzlvzOE9m051czYoE7e-S9vBy_N-2v89FZZEJlfpw==', start_index=8073)
Annotation(end_index=8091, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGt1HQ-F1SJ1L7MHnG-QfuzCFbPdMAvLqpCA9hRgRbfN5Rz7JgegNBMGew8eWD5GZgyeTeb_1o_1nahyWW63kLA5Rj3MPStaz1RFlErY9VaGSM8OxxvzpDey1JLGzpNpMHMYkc2g_Zj_2vDKg==', start_index=8073)
Annotation(end_index=8820, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVV1lxNsXf_29vtBaLpIWg1GvI0kIvEEwAuSxbfLfQiluSVXodWK06FvTp19y61PGiQC8n6XMIyGg0p8UDuuBB6-DD7FqJ85uY-QRF-HbReANivshQYuV9AE7ooVKPgJA=', start_index=8811)
Annotation(end_index=9541, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuMyDqcbkVkEKqT2vsOW188JTJOG1TWWLrEuccbV55QAbGwXjc5hICwXXIQGShben3nGsM9Pc1_mOPo9Y3hIxJCD1oop_5uPljqgO6ejMJYx3b03FMJMi6JmMWPD4mwyfNluTZaFZQak5NmIqdzmrZBXX1iUpD7NUMqq382GlpTaI1Oh8uKkwTXc277ViF0sZklG-CTiMRFa8HIitQ8qVT7YDFTwDCnJc5ZYfb-w==', start_index=9527)
Annotation(end_index=9541, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyMflzSgkakLcm8LqzE8y68t2hb5PzFiKVNfVV4QJ9BN3P0-u-SzaWcPVcvH9f9zlNceWo1EY_NSAY-jeQKZ8UCbMlK1lhkKn50ITIqgPryY8mHkTJGDpVcL1gnz3E', start_index=9527)
Annotation(end_index=10303, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERrSJ_FHP0yafolVLEKo9LcKc9f6B7XXg6Aoe5sCIvb6BXN4bLXoyBzCehM289re6l89-VoE4z8ZxO92TZwftZ4Tahkqvr5md7mFRyfXvweGc05gOWKRQPMDLArumzXYI8BSBPcqHF5Sj6Ww07mqdV', start_index=10286)
Annotation(end_index=10303, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmU7vl64q0PLD2F1smLwnnXhX201CI7XcsN775B0U-zLT9zGXqfajfuemjsKhOceNdGKdYPvXOD7P3Uc7rPYs5XEiqU2v2QCq7dbp7-l_QbaK5P-gyAPHD-Jl2FOg=', start_index=10286)
Annotation(end_index=10303, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl2DcxKnGTD5lRp6sDEKfMGzgFaWelDeUV1IOfCPPgW5XYfOO5H9jV-lpyLbE7U5R5bJTgvQ-W41668wgKaIbobk8i3gRx6x0F9MNxrx7Tsj-vZoy2Gv-WDrvowJe3sfT8V7ljx-LXwcj7ue0=', start_index=10286)
Annotation(end_index=11033, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERrSJ_FHP0yafolVLEKo9LcKc9f6B7XXg6Aoe5sCIvb6BXN4bLXoyBzCehM289re6l89-VoE4z8ZxO92TZwftZ4Tahkqvr5md7mFRyfXvweGc05gOWKRQPMDLArumzXYI8BSBPcqHF5Sj6Ww07mqdV', start_index=11016)
Annotation(end_index=11033, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl2DcxKnGTD5lRp6sDEKfMGzgFaWelDeUV1IOfCPPgW5XYfOO5H9jV-lpyLbE7U5R5bJTgvQ-W41668wgKaIbobk8i3gRx6x0F9MNxrx7Tsj-vZoy2Gv-WDrvowJe3sfT8V7ljx-LXwcj7ue0=', start_index=11016)
Annotation(end_index=11033, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXOA9rpgY_4dK5fejt9ONCWpA7ORFb3L9r2eiVJrZPVNeIRHE1XIj_gqTTxjrOy8v3XBYWDFLiT23SVsBsHRf5wlsw5wXn94ILugYy-76XYOSLu5iFvKoGQehqgGv4ZVb5x2glLc7Aik-P3YGWePAssl5h8FYFc1xmL7c72Ge39mOAq9S4X2ri2aazm7vykI_MLpLspZJQfsc9zC1_A6GsmRk5hvu7Y34VoW082hxQ9-0zMB6gFmkGkiDovA_l7Bd8sef8862lvWjulPAI-w==', start_index=11016)
Annotation(end_index=11561, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECNT5AD040KcwPcFt42ERZNbaqVqBAM1t9KdPD8qJbK0THel8NuCXNCg6E79zU0zaKTQzZOf7VsS-k2i_J6XGjl9xLrWbP9AGX5dD58CX0LBNK7GaKBxO8BNZXN5Fj0sO42ov1IyS88EyX', start_index=11549)
Annotation(end_index=11561, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPyLiHTm0Uc1ltuDciAg5SAW7hcETK0sgC_th_7TXLiFEQRV2ySmKmnTMDjyFOUwHB3caQilFqIh_8njjwxQXS7yJlsaNx-SyPZgU5gsqI_0MzfuRwJ8RTBPA2Su_RuE6l7ZEXO8l5g4xAAoyG', start_index=11549)
Annotation(end_index=11809, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECNT5AD040KcwPcFt42ERZNbaqVqBAM1t9KdPD8qJbK0THel8NuCXNCg6E79zU0zaKTQzZOf7VsS-k2i_J6XGjl9xLrWbP9AGX5dD58CX0LBNK7GaKBxO8BNZXN5Fj0sO42ov1IyS88EyX', start_index=11796)
Annotation(end_index=11809, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESdoY1U8YpHUzodh3AmFbJ_VNI_KmlJtriPTQBOY11gdlOnXZ4gKP8kE2z9kWZkvCsVrY1YXvZgaB_oF5IImqwmFbibYQy27RmUej7wAcN8V-NaJOwN-N4QKhcaaP-xQ==', start_index=11796)
Annotation(end_index=12604, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiRRWJV1r9KJVKe7kov5MYANoG9VC67yJfGuvZRTutYL912UCpzY7LVvznxc4htaGu0ktXDTsFs7qiik_uk25IXLX3P_U4EAQ-rMi026gpDhRMJbolNVFhZRNobbQ=', start_index=12590)
Annotation(end_index=12604, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcWB_PI2SXWY_VxZn6U5qA_rYCFcT7gYn6tvfgmX5E1gzY3HwKdBnDLjojgVvSjXfCJFt-K9-XbiOyvQFHnC9tc_yo5pqdAP3I2Zk10EUHzlG7c83cy-5pAdZeUU3Gm0hsxW7dEvTL8PT6Uyvori6xJq2GPdU=', start_index=12590)
Annotation(end_index=12899, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiRRWJV1r9KJVKe7kov5MYANoG9VC67yJfGuvZRTutYL912UCpzY7LVvznxc4htaGu0ktXDTsFs7qiik_uk25IXLX3P_U4EAQ-rMi026gpDhRMJbolNVFhZRNobbQ=', start_index=12885)
Annotation(end_index=12899, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4o6EHzwFtAVwDoMQnzVq32OKf_93RBNELJA6yDmqvPfAEVk_37cCnax2cZ4xY8CGfRZwqEBK4WHg-yv9RiHkLLW205YmtkULU9bBmdEmz3dzFPNwRCHwhYOVG5rHK15oumlyYk9KJzX7x2Va30u_BdYg0vHwiGqgKvaMJHBHi5V5kpcjXp1gVy8rn7RDLY_UbvZEGzGpWssYHUeeg', start_index=12885)
Annotation(end_index=13350, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYghlyg8GZmNrihRE2TkB9P3EIz59EW97ugYmebF8GgpqHuWi5CuyQsRk9pcC_3VvXCmGeOi2GuddysKe6mbK-F4p0paAEdpmGpAXvNyfaUgwsBd_ZaaJmzsq2LPL9oHj_xlCAX_m46uKItXJQA5aAVH1WXZ9Z92b8JjVmmGf5HE_GNKvFcOzV8pT0Hev3YSo8t4koPT1fyH1ntvXVuJBKMCITBIeMWcotySU_Icv84M_Pnez33eCsiS-LeOk=', start_index=13340)
Annotation(end_index=13595, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_4H8uvxQsQu4ayLnXZE6fpGqQq_mJhNrmKGQ2ZGVZcKrEev9sd6PxbxJL38-TYWUzK8IbFidMtweDn03afVsTSnRxfxq30qZGtq5SJdX_TmlGUp5jQQ==', start_index=13586)
Annotation(end_index=14075, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETNg84CKGyhAg_tlq2rtjmNkS6l0fz4ydhgzWD47FspuMRAfnN-4OyqcaAWxXsgIg3q0eiBogmItcXlEBmOu0FDegnWlRzfPE2mHPD1GjfHXIrUv6RW52VZuOg46sEwtD5NisbBogoXXVPSKLz0GmfLQAND0bMPtSnve56y5EtwSJDHZkVFXVQnDw=', start_index=14057)
Annotation(end_index=14075, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGP_1_n8Ezj9dy0nA4QI72vRgwih8Q7hSNf1-4HGTplYun3y51G8_ks-YGaH-YqOrOLEgaZ5MvFfl3hW1ELRkMOJ5uL_H7WZeKBnj1gcFG9QH4J2NY2orq85t2TJNzPFiuNsJ5yTWbvM9avmYcmfQglgQC8ec4Sy1I-6jCovCCYvPHNDKgMhQwnqtA5XAEIdutm41Ui6CAaVZh6iRGqxA=', start_index=14057)
Annotation(end_index=14075, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4o6EHzwFtAVwDoMQnzVq32OKf_93RBNELJA6yDmqvPfAEVk_37cCnax2cZ4xY8CGfRZwqEBK4WHg-yv9RiHkLLW205YmtkULU9bBmdEmz3dzFPNwRCHwhYOVG5rHK15oumlyYk9KJzX7x2Va30u_BdYg0vHwiGqgKvaMJHBHi5V5kpcjXp1gVy8rn7RDLY_UbvZEGzGpWssYHUeeg', start_index=14057)
Annotation(end_index=14931, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBRgUmu4pczp8nnK4UCW28I3Yw9__KkfaVMmUZnTZfT5rO0Mbj44aQEFaHB9rRGMlNifhlprqvJISKks5KtBDnehGNtTjUPw_sAmtlMDZGfw37EeVt0Yy5yxgSxNVk3Y6PNKrk9FbtU6oNzqBSqO_CGjIRg1xMSa03YLtJoaArE-6un9MQy6LhRdn092e3bcuOPk7xULs=', start_index=14913)
Annotation(end_index=14931, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEG0kkrb9JTAXnJkQ2sVdO_y7muCW6KUtR5sU0R_y2MFHIcqnjpdqkEh8kGHf4PXheh-nc87aDi6LIHB62GWAx2kDWCW9jp2IcmS_lt2_nZfQmtbUIDlg==', start_index=14913)
Annotation(end_index=14931, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF02_1rRjIlkNeMM3UINb-W3oROdA3sKgr1NsnF1z92REwShLj2TGZ_83s8_GCTk9Fq58tnHy3Q13BXUmyNVPAKv9yVdNCgZDMf0lW-IsAwJarKynZTTXPXCBnISv2b3hvUa1KDUBjEvb8UD06CXjIR', start_index=14913)
Annotation(end_index=15520, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGM8MVaPw2XrHnDAK1T9_eG9ymFdZohSijqFoKvoymm_MLUX0ltVmKu03OaINWNydaHGyrt7wEWDL3nEggRiruJxIFQZ3A9mMaOFT-F3fhBx7jw48wvNwERMQHwahI=', start_index=15504)
Annotation(end_index=15520, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwwqgol-pc-8dfHZoOkzOS_ARoQKwO0RMiAeQ5Fyz2y5musc-eklezMzMywWY_nE0sJbJftVW2_iuoHtV75OgJpMSfCMYpSNmFexy-QhOURQ6zyZIMrw==', start_index=15504)
Annotation(end_index=15520, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_4H8uvxQsQu4ayLnXZE6fpGqQq_mJhNrmKGQ2ZGVZcKrEev9sd6PxbxJL38-TYWUzK8IbFidMtweDn03afVsTSnRxfxq30qZGtq5SJdX_TmlGUp5jQQ==', start_index=15504)
Annotation(end_index=15690, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_4H8uvxQsQu4ayLnXZE6fpGqQq_mJhNrmKGQ2ZGVZcKrEev9sd6PxbxJL38-TYWUzK8IbFidMtweDn03afVsTSnRxfxq30qZGtq5SJdX_TmlGUp5jQQ==', start_index=15681)
Annotation(end_index=16372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEbLz2eEDRTowQhvU3D1KEnnwt464C3qRsanqk7gBoQfZ6Yr4POuswLUDnEjABMOD6pBJzqLvbri0B9NV-nEi4ohkHPOYTUsEDQpkMcrFFfmMKaSNqYKFcz4CnRg8__5uB2acJga5fD1yidAqrVfsf9qcW-i67TW_dTOQ2iTRGD4iXJes=', start_index=16358)
Annotation(end_index=16372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpUpzHgL1tOS2UBnK-JTk1ms3tZ_fS0Nf37ME4HLRr4JKSJl-hQ3TCfVrC9wOLrGP6e1bfqVteZzCuFgU4LusZMLTkD9hOJ9HE55DCJACqQm0VZKo8hA==', start_index=16358)
Annotation(end_index=16670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6gYYcwpn7dQtwO4tyWT93kzRiKWqcDiq-cKqldNZMnx9F0WssgI3-VndntALgC9RyjxTabx7FTUjIusFr0lyB0r_er9dgfZk5B2AYnMu2o9t0XkI5OaYA0yhmM0zTsQquE7qV27UCIHxTYJUiEaklDV0kmPq4uxjJdvWIh9_F3XMXuBt09te1gt8uwmsjm9MgkgFaQUFLmDtDDd1d3O5XFWri8SSY3BO-hccTWIiEjP2iTtEza5jDDOkDIfwy0YjElpx4rRk=', start_index=16656)
Annotation(end_index=16670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpUpzHgL1tOS2UBnK-JTk1ms3tZ_fS0Nf37ME4HLRr4JKSJl-hQ3TCfVrC9wOLrGP6e1bfqVteZzCuFgU4LusZMLTkD9hOJ9HE55DCJACqQm0VZKo8hA==', start_index=16656)
Annotation(end_index=17052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELWTiEfICUgZYXk9ITwiTxLY0shBbr7_Sa-uHLsg7nvUxTHDwG_x55UVPrd57zojSQo_StNIs5Yn--hZ0QW9hcGt07Yq2q9H_s6uRRy4MWfM1RdmOWVXJsoCwVXdHHIaSM', start_index=17036)
Annotation(end_index=17052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGID_bx-KPkJB_ih-f9lx1FAjArlQcMj10ZUTsj41Io1M8npZTYDSquKch9TBJpPiFjLH47wjKnHoQtFvzgk4G4aSHtoZP31KuisFW9OLnkpZNxXo9ZiVyyjQh3n65TWYkq_9sLq4o1Bw0Fl5E=', start_index=17036)
Annotation(end_index=17052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsTk99Mi09EaFD7Fu54rU5cwuMvPqbjbI35GeGIl-CMpF5UknTT3gLeJaB3vyvrykhLA_V3OxGB8IAYRNiTW-AfxOuwcA_govmuO7scobSFjN53Fbprj-WO9jRSpbc7_s3', start_index=17036)
Annotation(end_index=17285, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF02_1rRjIlkNeMM3UINb-W3oROdA3sKgr1NsnF1z92REwShLj2TGZ_83s8_GCTk9Fq58tnHy3Q13BXUmyNVPAKv9yVdNCgZDMf0lW-IsAwJarKynZTTXPXCBnISv2b3hvUa1KDUBjEvb8UD06CXjIR', start_index=17271)
Annotation(end_index=17285, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl2DcxKnGTD5lRp6sDEKfMGzgFaWelDeUV1IOfCPPgW5XYfOO5H9jV-lpyLbE7U5R5bJTgvQ-W41668wgKaIbobk8i3gRx6x0F9MNxrx7Tsj-vZoy2Gv-WDrvowJe3sfT8V7ljx-LXwcj7ue0=', start_index=17271)
Annotation(end_index=18175, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcWB_PI2SXWY_VxZn6U5qA_rYCFcT7gYn6tvfgmX5E1gzY3HwKdBnDLjojgVvSjXfCJFt-K9-XbiOyvQFHnC9tc_yo5pqdAP3I2Zk10EUHzlG7c83cy-5pAdZeUU3Gm0hsxW7dEvTL8PT6Uyvori6xJq2GPdU=', start_index=18165)
Annotation(end_index=18190, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiRRWJV1r9KJVKe7kov5MYANoG9VC67yJfGuvZRTutYL912UCpzY7LVvznxc4htaGu0ktXDTsFs7qiik_uk25IXLX3P_U4EAQ-rMi026gpDhRMJbolNVFhZRNobbQ=', start_index=18176)
Annotation(end_index=18190, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcWB_PI2SXWY_VxZn6U5qA_rYCFcT7gYn6tvfgmX5E1gzY3HwKdBnDLjojgVvSjXfCJFt-K9-XbiOyvQFHnC9tc_yo5pqdAP3I2Zk10EUHzlG7c83cy-5pAdZeUU3Gm0hsxW7dEvTL8PT6Uyvori6xJq2GPdU=', start_index=18176)
Annotation(end_index=18201, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGP_1_n8Ezj9dy0nA4QI72vRgwih8Q7hSNf1-4HGTplYun3y51G8_ks-YGaH-YqOrOLEgaZ5MvFfl3hW1ELRkMOJ5uL_H7WZeKBnj1gcFG9QH4J2NY2orq85t2TJNzPFiuNsJ5yTWbvM9avmYcmfQglgQC8ec4Sy1I-6jCovCCYvPHNDKgMhQwnqtA5XAEIdutm41Ui6CAaVZh6iRGqxA=', start_index=18191)
Annotation(end_index=18216, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGP_1_n8Ezj9dy0nA4QI72vRgwih8Q7hSNf1-4HGTplYun3y51G8_ks-YGaH-YqOrOLEgaZ5MvFfl3hW1ELRkMOJ5uL_H7WZeKBnj1gcFG9QH4J2NY2orq85t2TJNzPFiuNsJ5yTWbvM9avmYcmfQglgQC8ec4Sy1I-6jCovCCYvPHNDKgMhQwnqtA5XAEIdutm41Ui6CAaVZh6iRGqxA=', start_index=18202)
Annotation(end_index=18216, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4o6EHzwFtAVwDoMQnzVq32OKf_93RBNELJA6yDmqvPfAEVk_37cCnax2cZ4xY8CGfRZwqEBK4WHg-yv9RiHkLLW205YmtkULU9bBmdEmz3dzFPNwRCHwhYOVG5rHK15oumlyYk9KJzX7x2Va30u_BdYg0vHwiGqgKvaMJHBHi5V5kpcjXp1gVy8rn7RDLY_UbvZEGzGpWssYHUeeg', start_index=18202)
Annotation(end_index=18227, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBRgUmu4pczp8nnK4UCW28I3Yw9__KkfaVMmUZnTZfT5rO0Mbj44aQEFaHB9rRGMlNifhlprqvJISKks5KtBDnehGNtTjUPw_sAmtlMDZGfw37EeVt0Yy5yxgSxNVk3Y6PNKrk9FbtU6oNzqBSqO_CGjIRg1xMSa03YLtJoaArE-6un9MQy6LhRdn092e3bcuOPk7xULs=', start_index=18217)
Annotation(end_index=18238, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBRgUmu4pczp8nnK4UCW28I3Yw9__KkfaVMmUZnTZfT5rO0Mbj44aQEFaHB9rRGMlNifhlprqvJISKks5KtBDnehGNtTjUPw_sAmtlMDZGfw37EeVt0Yy5yxgSxNVk3Y6PNKrk9FbtU6oNzqBSqO_CGjIRg1xMSa03YLtJoaArE-6un9MQy6LhRdn092e3bcuOPk7xULs=', start_index=18228)
Annotation(end_index=18249, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYghlyg8GZmNrihRE2TkB9P3EIz59EW97ugYmebF8GgpqHuWi5CuyQsRk9pcC_3VvXCmGeOi2GuddysKe6mbK-F4p0paAEdpmGpAXvNyfaUgwsBd_ZaaJmzsq2LPL9oHj_xlCAX_m46uKItXJQA5aAVH1WXZ9Z92b8JjVmmGf5HE_GNKvFcOzV8pT0Hev3YSo8t4koPT1fyH1ntvXVuJBKMCITBIeMWcotySU_Icv84M_Pnez33eCsiS-LeOk=', start_index=18239)
Annotation(end_index=18264, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyH00-mseESPFt5K7Tr5h8MKEhoRUimmJSdH1_4hkKRYEQufTrg72g6fUb8peddd-Mzi2P2oS0ngvomW2EXuH47qPs9qBYBbtEholPjjXWAGXMUgyBziK3MyAp1c7g0fVrwZ1XJWpXHrxE6xI=', start_index=18250)
Annotation(end_index=18264, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYghlyg8GZmNrihRE2TkB9P3EIz59EW97ugYmebF8GgpqHuWi5CuyQsRk9pcC_3VvXCmGeOi2GuddysKe6mbK-F4p0paAEdpmGpAXvNyfaUgwsBd_ZaaJmzsq2LPL9oHj_xlCAX_m46uKItXJQA5aAVH1WXZ9Z92b8JjVmmGf5HE_GNKvFcOzV8pT0Hev3YSo8t4koPT1fyH1ntvXVuJBKMCITBIeMWcotySU_Icv84M_Pnez33eCsiS-LeOk=', start_index=18250)
Annotation(end_index=18275, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiRRWJV1r9KJVKe7kov5MYANoG9VC67yJfGuvZRTutYL912UCpzY7LVvznxc4htaGu0ktXDTsFs7qiik_uk25IXLX3P_U4EAQ-rMi026gpDhRMJbolNVFhZRNobbQ=', start_index=18265)
Annotation(end_index=18290, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiRRWJV1r9KJVKe7kov5MYANoG9VC67yJfGuvZRTutYL912UCpzY7LVvznxc4htaGu0ktXDTsFs7qiik_uk25IXLX3P_U4EAQ-rMi026gpDhRMJbolNVFhZRNobbQ=', start_index=18276)
Annotation(end_index=18290, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4o6EHzwFtAVwDoMQnzVq32OKf_93RBNELJA6yDmqvPfAEVk_37cCnax2cZ4xY8CGfRZwqEBK4WHg-yv9RiHkLLW205YmtkULU9bBmdEmz3dzFPNwRCHwhYOVG5rHK15oumlyYk9KJzX7x2Va30u_BdYg0vHwiGqgKvaMJHBHi5V5kpcjXp1gVy8rn7RDLY_UbvZEGzGpWssYHUeeg', start_index=18276)
Annotation(end_index=18301, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8hJ7sGzxWxJG4VLhaIvI4EwImFstsJZUpXOaUm0EI3Lt-f2G6m7XdNcIUy8ckumTF1-TUjNhidUSGt56lsYL9FwaLYYM3Fb0SVBGORMWKki2z_yoszbgIYt0FnBpMDRVHiK3qo_dUSDkduQ==', start_index=18291)
Annotation(end_index=18316, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXVJM8Z64j_lfxs-3FxXf96LIFEZK4i6xccam9Y5g_4S4FRGx5pLhiS6lzwDfHtFMrTL5unu5Fl813U3qd34ZfKp9YT_OAfQIx8iRcT6D28YEhOt50Z2AA5TeMolhjvhVRPZl3gzVZKGme81kDrAE=', start_index=18302)
Annotation(end_index=18316, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8hJ7sGzxWxJG4VLhaIvI4EwImFstsJZUpXOaUm0EI3Lt-f2G6m7XdNcIUy8ckumTF1-TUjNhidUSGt56lsYL9FwaLYYM3Fb0SVBGORMWKki2z_yoszbgIYt0FnBpMDRVHiK3qo_dUSDkduQ==', start_index=18302)
Annotation(end_index=18326, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVV1lxNsXf_29vtBaLpIWg1GvI0kIvEEwAuSxbfLfQiluSVXodWK06FvTp19y61PGiQC8n6XMIyGg0p8UDuuBB6-DD7FqJ85uY-QRF-HbReANivshQYuV9AE7ooVKPgJA=', start_index=18317)
Annotation(end_index=18336, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVV1lxNsXf_29vtBaLpIWg1GvI0kIvEEwAuSxbfLfQiluSVXodWK06FvTp19y61PGiQC8n6XMIyGg0p8UDuuBB6-DD7FqJ85uY-QRF-HbReANivshQYuV9AE7ooVKPgJA=', start_index=18327)
Annotation(end_index=18347, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGMNmOGWmK1IkIzDeU-86LgrGoqgq0EfOB90faHAaEklInYj5at_UbGTy6M1xF69Cw6gtAz84qOpq-G10rp4wkgvxer4ZL9BXaUFa9uvWNXa4bm6DvfP0HB9g4SotEloxt6WdnP5cO-pu-_SNOViqVQknslUQJKR1aV7Qe6o5zHp2k_zcuxx5MgEIsH-tw0C-PTRGRScL2cQEIm5K-2JeMwDyozwsSxIKpVMraoUGD5vaXMDjMxU5mgfSrFwypCzNtsgGB-Wyu0vUXIvY-buCKAEpubfSilShsow8V-yXdt60=', start_index=18337)
Annotation(end_index=18360, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELWTiEfICUgZYXk9ITwiTxLY0shBbr7_Sa-uHLsg7nvUxTHDwG_x55UVPrd57zojSQo_StNIs5Yn--hZ0QW9hcGt07Yq2q9H_s6uRRy4MWfM1RdmOWVXJsoCwVXdHHIaSM', start_index=18348)
Annotation(end_index=18360, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsTk99Mi09EaFD7Fu54rU5cwuMvPqbjbI35GeGIl-CMpF5UknTT3gLeJaB3vyvrykhLA_V3OxGB8IAYRNiTW-AfxOuwcA_govmuO7scobSFjN53Fbprj-WO9jRSpbc7_s3', start_index=18348)
Annotation(end_index=18371, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEts6qWND0DiX5bqpxsElgyZjtgd43xVMO1LMagXtvn79oQira9S_S1ikJpn_BtNOMxLhx5s_tbzSMBe0vcpqcdxKwHurHaPHcW51u2MvaXOlHHpQPt627ufE48HJfMeKyMAdu7blZxzI_u6p9t0WROT7kidrJPJF80U8ZTnWXFhxeLcVuAspJgFEB6eAQzmXZOtvcsjvO4E7IO2kabFJk1A_Xxf2mfpD6zmrGS4TcckaW3JXbhCsnPzQQ=', start_index=18361)
Annotation(end_index=18386, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuMyDqcbkVkEKqT2vsOW188JTJOG1TWWLrEuccbV55QAbGwXjc5hICwXXIQGShben3nGsM9Pc1_mOPo9Y3hIxJCD1oop_5uPljqgO6ejMJYx3b03FMJMi6JmMWPD4mwyfNluTZaFZQak5NmIqdzmrZBXX1iUpD7NUMqq382GlpTaI1Oh8uKkwTXc277ViF0sZklG-CTiMRFa8HIitQ8qVT7YDFTwDCnJc5ZYfb-w==', start_index=18372)
Annotation(end_index=18386, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyMflzSgkakLcm8LqzE8y68t2hb5PzFiKVNfVV4QJ9BN3P0-u-SzaWcPVcvH9f9zlNceWo1EY_NSAY-jeQKZ8UCbMlK1lhkKn50ITIqgPryY8mHkTJGDpVcL1gnz3E', start_index=18372)
Annotation(end_index=18396, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsTk99Mi09EaFD7Fu54rU5cwuMvPqbjbI35GeGIl-CMpF5UknTT3gLeJaB3vyvrykhLA_V3OxGB8IAYRNiTW-AfxOuwcA_govmuO7scobSFjN53Fbprj-WO9jRSpbc7_s3', start_index=18387)
Annotation(end_index=18407, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF02_1rRjIlkNeMM3UINb-W3oROdA3sKgr1NsnF1z92REwShLj2TGZ_83s8_GCTk9Fq58tnHy3Q13BXUmyNVPAKv9yVdNCgZDMf0lW-IsAwJarKynZTTXPXCBnISv2b3hvUa1KDUBjEvb8UD06CXjIR', start_index=18397)
Annotation(end_index=18417, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELWTiEfICUgZYXk9ITwiTxLY0shBbr7_Sa-uHLsg7nvUxTHDwG_x55UVPrd57zojSQo_StNIs5Yn--hZ0QW9hcGt07Yq2q9H_s6uRRy4MWfM1RdmOWVXJsoCwVXdHHIaSM', start_index=18408)
Annotation(end_index=18432, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmU7vl64q0PLD2F1smLwnnXhX201CI7XcsN775B0U-zLT9zGXqfajfuemjsKhOceNdGKdYPvXOD7P3Uc7rPYs5XEiqU2v2QCq7dbp7-l_QbaK5P-gyAPHD-Jl2FOg=', start_index=18418)
Annotation(end_index=18432, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl2DcxKnGTD5lRp6sDEKfMGzgFaWelDeUV1IOfCPPgW5XYfOO5H9jV-lpyLbE7U5R5bJTgvQ-W41668wgKaIbobk8i3gRx6x0F9MNxrx7Tsj-vZoy2Gv-WDrvowJe3sfT8V7ljx-LXwcj7ue0=', start_index=18418)
Annotation(end_index=18443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTIQpRTYMLCvuVluUwm6f5pYmPUiZk6nllVvmsurCKgqKZ9elTyoUOPQJWtWnZ4TANbuT8qKu2B1QmCLZHQWRNvvm7J1ifbWpYJ0jQEZFTIZuayLwhNqdGSn9TpkudL2pPwatkWNnnp9F39w==', start_index=18433)
Annotation(end_index=18456, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECNT5AD040KcwPcFt42ERZNbaqVqBAM1t9KdPD8qJbK0THel8NuCXNCg6E79zU0zaKTQzZOf7VsS-k2i_J6XGjl9xLrWbP9AGX5dD58CX0LBNK7GaKBxO8BNZXN5Fj0sO42ov1IyS88EyX', start_index=18444)
Annotation(end_index=18456, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPyLiHTm0Uc1ltuDciAg5SAW7hcETK0sgC_th_7TXLiFEQRV2ySmKmnTMDjyFOUwHB3caQilFqIh_8njjwxQXS7yJlsaNx-SyPZgU5gsqI_0MzfuRwJ8RTBPA2Su_RuE6l7ZEXO8l5g4xAAoyG', start_index=18444)
Annotation(end_index=18467, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuMyDqcbkVkEKqT2vsOW188JTJOG1TWWLrEuccbV55QAbGwXjc5hICwXXIQGShben3nGsM9Pc1_mOPo9Y3hIxJCD1oop_5uPljqgO6ejMJYx3b03FMJMi6JmMWPD4mwyfNluTZaFZQak5NmIqdzmrZBXX1iUpD7NUMqq382GlpTaI1Oh8uKkwTXc277ViF0sZklG-CTiMRFa8HIitQ8qVT7YDFTwDCnJc5ZYfb-w==', start_index=18457)
Annotation(end_index=18477, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERrSJ_FHP0yafolVLEKo9LcKc9f6B7XXg6Aoe5sCIvb6BXN4bLXoyBzCehM289re6l89-VoE4z8ZxO92TZwftZ4Tahkqvr5md7mFRyfXvweGc05gOWKRQPMDLArumzXYI8BSBPcqHF5Sj6Ww07mqdV', start_index=18468)
Annotation(end_index=18488, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF02_1rRjIlkNeMM3UINb-W3oROdA3sKgr1NsnF1z92REwShLj2TGZ_83s8_GCTk9Fq58tnHy3Q13BXUmyNVPAKv9yVdNCgZDMf0lW-IsAwJarKynZTTXPXCBnISv2b3hvUa1KDUBjEvb8UD06CXjIR', start_index=18478)
Annotation(end_index=18502, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELWTiEfICUgZYXk9ITwiTxLY0shBbr7_Sa-uHLsg7nvUxTHDwG_x55UVPrd57zojSQo_StNIs5Yn--hZ0QW9hcGt07Yq2q9H_s6uRRy4MWfM1RdmOWVXJsoCwVXdHHIaSM', start_index=18489)
Annotation(end_index=18502, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGID_bx-KPkJB_ih-f9lx1FAjArlQcMj10ZUTsj41Io1M8npZTYDSquKch9TBJpPiFjLH47wjKnHoQtFvzgk4G4aSHtoZP31KuisFW9OLnkpZNxXo9ZiVyyjQh3n65TWYkq_9sLq4o1Bw0Fl5E=', start_index=18489)
Annotation(end_index=18513, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl2DcxKnGTD5lRp6sDEKfMGzgFaWelDeUV1IOfCPPgW5XYfOO5H9jV-lpyLbE7U5R5bJTgvQ-W41668wgKaIbobk8i3gRx6x0F9MNxrx7Tsj-vZoy2Gv-WDrvowJe3sfT8V7ljx-LXwcj7ue0=', start_index=18503)
Annotation(end_index=18528, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBRgUmu4pczp8nnK4UCW28I3Yw9__KkfaVMmUZnTZfT5rO0Mbj44aQEFaHB9rRGMlNifhlprqvJISKks5KtBDnehGNtTjUPw_sAmtlMDZGfw37EeVt0Yy5yxgSxNVk3Y6PNKrk9FbtU6oNzqBSqO_CGjIRg1xMSa03YLtJoaArE-6un9MQy6LhRdn092e3bcuOPk7xULs=', start_index=18514)
Annotation(end_index=18528, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEG0kkrb9JTAXnJkQ2sVdO_y7muCW6KUtR5sU0R_y2MFHIcqnjpdqkEh8kGHf4PXheh-nc87aDi6LIHB62GWAx2kDWCW9jp2IcmS_lt2_nZfQmtbUIDlg==', start_index=18514)
Annotation(end_index=18538, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPyLiHTm0Uc1ltuDciAg5SAW7hcETK0sgC_th_7TXLiFEQRV2ySmKmnTMDjyFOUwHB3caQilFqIh_8njjwxQXS7yJlsaNx-SyPZgU5gsqI_0MzfuRwJ8RTBPA2Su_RuE6l7ZEXO8l5g4xAAoyG', start_index=18529)
Annotation(end_index=18553, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEbLz2eEDRTowQhvU3D1KEnnwt464C3qRsanqk7gBoQfZ6Yr4POuswLUDnEjABMOD6pBJzqLvbri0B9NV-nEi4ohkHPOYTUsEDQpkMcrFFfmMKaSNqYKFcz4CnRg8__5uB2acJga5fD1yidAqrVfsf9qcW-i67TW_dTOQ2iTRGD4iXJes=', start_index=18539)
Annotation(end_index=18553, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpUpzHgL1tOS2UBnK-JTk1ms3tZ_fS0Nf37ME4HLRr4JKSJl-hQ3TCfVrC9wOLrGP6e1bfqVteZzCuFgU4LusZMLTkD9hOJ9HE55DCJACqQm0VZKo8hA==', start_index=18539)
Annotation(end_index=18563, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERrSJ_FHP0yafolVLEKo9LcKc9f6B7XXg6Aoe5sCIvb6BXN4bLXoyBzCehM289re6l89-VoE4z8ZxO92TZwftZ4Tahkqvr5md7mFRyfXvweGc05gOWKRQPMDLArumzXYI8BSBPcqHF5Sj6Ww07mqdV', start_index=18554)
Annotation(end_index=18578, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6gYYcwpn7dQtwO4tyWT93kzRiKWqcDiq-cKqldNZMnx9F0WssgI3-VndntALgC9RyjxTabx7FTUjIusFr0lyB0r_er9dgfZk5B2AYnMu2o9t0XkI5OaYA0yhmM0zTsQquE7qV27UCIHxTYJUiEaklDV0kmPq4uxjJdvWIh9_F3XMXuBt09te1gt8uwmsjm9MgkgFaQUFLmDtDDd1d3O5XFWri8SSY3BO-hccTWIiEjP2iTtEza5jDDOkDIfwy0YjElpx4rRk=', start_index=18564)
Annotation(end_index=18578, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdo51B4ss_XUyBxOKLxELKYkDux5O-hpdvW0VWL3D2A4xNBd0sGhc8fU186OSpK8DuPPIPKVepPhVSEfbeSVkDvGKZ2Iwfs6UGuLTebW8M19-dD3EmaENymTeCTw8g4R0cLcDFzw8Yh8pDctRtVTk6aMxaLLLJzJtif3Rlpv6R0g==', start_index=18564)
Annotation(end_index=18589, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLDukJNfc1MwvbNmOCRD6gwI2haH2uvnr6JZsQvxfdGFETc3aYjMesXrnl7u0uw04um823gjqv3fBnuU5fjKXLB7IGVs7PpspFWy_WGJs4Dd5xJ9Dpg4jXIQk_LnhAPGBrj04R7gpkDdf9Vw==', start_index=18579)
Annotation(end_index=18599, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_4H8uvxQsQu4ayLnXZE6fpGqQq_mJhNrmKGQ2ZGVZcKrEev9sd6PxbxJL38-TYWUzK8IbFidMtweDn03afVsTSnRxfxq30qZGtq5SJdX_TmlGUp5jQQ==', start_index=18590)
Annotation(end_index=18610, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQSBkgk-5l0JCzWAKG6VmA7MCq9NwaMGXMPiHvoRdUYF5e0pX4bZ88zRkIccddSS4aLWD13iSfhYTMia2bqPf8-Z9OqJwjxc--wbpRlw_4lS_fKtbNiyd0TW_th8N9xvNTMYz5yGoV8n46knX3TjOOewQ2Qw==', start_index=18600)
Annotation(end_index=18625, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYLkXfJRoi-MOd87Z6lzSQGGJS5skeKhPMW4ZT4qAnNp21QjdiIGBBPqG1KhvGIkEsPGQnuSWAqKwjwe2_riMnlu4wBTlPUDX7mI1p9xmWErPZ-gBKLylYmANFLpCv3aWGJdXq_jbftS9X9bw=', start_index=18611)
Annotation(end_index=18625, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGt1HQ-F1SJ1L7MHnG-QfuzCFbPdMAvLqpCA9hRgRbfN5Rz7JgegNBMGew8eWD5GZgyeTeb_1o_1nahyWW63kLA5Rj3MPStaz1RFlErY9VaGSM8OxxvzpDey1JLGzpNpMHMYkc2g_Zj_2vDKg==', start_index=18611)
Annotation(end_index=18636, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXVJM8Z64j_lfxs-3FxXf96LIFEZK4i6xccam9Y5g_4S4FRGx5pLhiS6lzwDfHtFMrTL5unu5Fl813U3qd34ZfKp9YT_OAfQIx8iRcT6D28YEhOt50Z2AA5TeMolhjvhVRPZl3gzVZKGme81kDrAE=', start_index=18626)
Annotation(end_index=18651, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuMyDqcbkVkEKqT2vsOW188JTJOG1TWWLrEuccbV55QAbGwXjc5hICwXXIQGShben3nGsM9Pc1_mOPo9Y3hIxJCD1oop_5uPljqgO6ejMJYx3b03FMJMi6JmMWPD4mwyfNluTZaFZQak5NmIqdzmrZBXX1iUpD7NUMqq382GlpTaI1Oh8uKkwTXc277ViF0sZklG-CTiMRFa8HIitQ8qVT7YDFTwDCnJc5ZYfb-w==', start_index=18637)
Annotation(end_index=18651, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyMflzSgkakLcm8LqzE8y68t2hb5PzFiKVNfVV4QJ9BN3P0-u-SzaWcPVcvH9f9zlNceWo1EY_NSAY-jeQKZ8UCbMlK1lhkKn50ITIqgPryY8mHkTJGDpVcL1gnz3E', start_index=18637)
Annotation(end_index=18662, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYIUGnKj7FQaofoKc15TtbEAzuAMsJwih5N7eJm5__riXDWASDsRPMzaKM8-WNTYZPC5XAQCMVAH1xLxHbFP49GJvZcU6HkxuXWBKGvwPwvz5cp3IGz0SerIf8kM4=', start_index=18652)
Annotation(end_index=18675, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELWTiEfICUgZYXk9ITwiTxLY0shBbr7_Sa-uHLsg7nvUxTHDwG_x55UVPrd57zojSQo_StNIs5Yn--hZ0QW9hcGt07Yq2q9H_s6uRRy4MWfM1RdmOWVXJsoCwVXdHHIaSM', start_index=18663)
Annotation(end_index=18675, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsTk99Mi09EaFD7Fu54rU5cwuMvPqbjbI35GeGIl-CMpF5UknTT3gLeJaB3vyvrykhLA_V3OxGB8IAYRNiTW-AfxOuwcA_govmuO7scobSFjN53Fbprj-WO9jRSpbc7_s3', start_index=18663)
Annotation(end_index=18685, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELWTiEfICUgZYXk9ITwiTxLY0shBbr7_Sa-uHLsg7nvUxTHDwG_x55UVPrd57zojSQo_StNIs5Yn--hZ0QW9hcGt07Yq2q9H_s6uRRy4MWfM1RdmOWVXJsoCwVXdHHIaSM', start_index=18676)
Annotation(end_index=18699, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERrSJ_FHP0yafolVLEKo9LcKc9f6B7XXg6Aoe5sCIvb6BXN4bLXoyBzCehM289re6l89-VoE4z8ZxO92TZwftZ4Tahkqvr5md7mFRyfXvweGc05gOWKRQPMDLArumzXYI8BSBPcqHF5Sj6Ww07mqdV', start_index=18686)
Annotation(end_index=18699, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXOA9rpgY_4dK5fejt9ONCWpA7ORFb3L9r2eiVJrZPVNeIRHE1XIj_gqTTxjrOy8v3XBYWDFLiT23SVsBsHRf5wlsw5wXn94ILugYy-76XYOSLu5iFvKoGQehqgGv4ZVb5x2glLc7Aik-P3YGWePAssl5h8FYFc1xmL7c72Ge39mOAq9S4X2ri2aazm7vykI_MLpLspZJQfsc9zC1_A6GsmRk5hvu7Y34VoW082hxQ9-0zMB6gFmkGkiDovA_l7Bd8sef8862lvWjulPAI-w==', start_index=18686)
Annotation(end_index=18710, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5pqxsksoE_qRw-9tsOPOgrQDBpR3g-GwfPIjpf4RJxyyXSY9Rl1jTaHBPr2SVSfiSKQSCJAQEIppP6UmT1mOSkjb3DEGt8dcSG0D2hqOi5uBcMUZ4yD0QXn2paPTS2zHJ5xaPolP_DacD6uM8AOmFU8jwNwFXJCm-XPvXHsFXZfIi9BDR7H3XgpoDYtQ6HH1wkOKD271cvG1DvKmdM38DJzf-XE81pDrQ4xWxUw==', start_index=18700)
Annotation(end_index=18724, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGM8MVaPw2XrHnDAK1T9_eG9ymFdZohSijqFoKvoymm_MLUX0ltVmKu03OaINWNydaHGyrt7wEWDL3nEggRiruJxIFQZ3A9mMaOFT-F3fhBx7jw48wvNwERMQHwahI=', start_index=18711)
Annotation(end_index=18724, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwwqgol-pc-8dfHZoOkzOS_ARoQKwO0RMiAeQ5Fyz2y5musc-eklezMzMywWY_nE0sJbJftVW2_iuoHtV75OgJpMSfCMYpSNmFexy-QhOURQ6zyZIMrw==', start_index=18711)
Annotation(end_index=18735, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESGhTfa0c4lmfGLiqBGPVoi03-I0341ziRjvyZcCMy4HdzzTWPWNtQIADfEdIUkM7do1KpdWinT04K2PAfdqq5wnmlveTHsCngXofnq0W9v7o9FS7kiF8nXVdsGxeII1bne1MX6TMfJGTz4efzASoDiX9iM6lPfZd9jyCOFNbBIdaxWqhfeoTwyQxi7NNrsLNNpz2cpm3-hZMiHL_M56krB5omft99S8Z7vPDhtFetjjuSE-bSCsRkV9_Y2DHsBfXeR5OtsFWVkHWnVPVcFONo_bu3ziTcbG3S4QsL', start_index=18725)
Annotation(end_index=18749, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECNT5AD040KcwPcFt42ERZNbaqVqBAM1t9KdPD8qJbK0THel8NuCXNCg6E79zU0zaKTQzZOf7VsS-k2i_J6XGjl9xLrWbP9AGX5dD58CX0LBNK7GaKBxO8BNZXN5Fj0sO42ov1IyS88EyX', start_index=18736)
Annotation(end_index=18749, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESdoY1U8YpHUzodh3AmFbJ_VNI_KmlJtriPTQBOY11gdlOnXZ4gKP8kE2z9kWZkvCsVrY1YXvZgaB_oF5IImqwmFbibYQy27RmUej7wAcN8V-NaJOwN-N4QKhcaaP-xQ==', start_index=18736)

## Sources
