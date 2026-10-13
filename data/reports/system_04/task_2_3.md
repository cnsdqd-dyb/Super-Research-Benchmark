# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 883c4d08 | **Time:** 266.82s | **Cost:** $1.31778
--------------------------------------------------------------------------------

# Optimizing Efficiency and Linearity in Millimeter-Wave RF Front-End Circuits

### Key Points
*   **The Central Trade-off:** The primary challenge in millimeter-wave (mmWave) RF front-end design is balancing Power Added Efficiency (PAE) with linearity, particularly given the high Peak-to-Average Power Ratio (PAPR) of 5G/6G waveforms (OFDM).
*   **Dominant Architecture:** The **Doherty Power Amplifier (DPA)** remains the prevailing analog solution for optimizing this trade-off, specifically due to its ability to enhance efficiency at power back-off (OBO) levels where modulated signals spend most of their time.
*   **Emerging Contenders:** The **Load Modulated Balanced Amplifier (LMBA)** is emerging as a superior alternative for wideband applications, offering better tolerance to VSWR variations and broader bandwidths than traditional DPAs.
*   **Digital Necessity:** No analog topology alone is sufficient; **Digital Predistortion (DPD)** is strictly required to correct the non-linearities introduced by high-efficiency architectures. However, DPD faces severe bandwidth constraints at mmWave frequencies.
*   **Material Synergy:** The integration of **GaN-on-SiC** devices allows for high power density and efficiency, while **Spatial Power Combining** is utilized to overcome the high insertion losses of on-chip combiners at frequencies above 28 GHz.

---

## 1. Introduction

The transition of wireless communication systems to millimeter-wave (mmWave) frequencies (24 GHz–100 GHz) has fundamentally altered the design landscape of Radio Frequency (RF) front-ends. Driven by the insatiable demand for data throughput in 5G and future 6G networks, engineers must utilize wide bandwidths available only in the mmWave spectrum. However, the physics of high-frequency signal propagation and the characteristics of modern modulation schemes create a severe dichotomy in circuit design: the conflict between energy efficiency and signal linearity.

Modern communication standards, such as 5G New Radio (NR), utilize spectrally efficient modulation schemes like Orthogonal Frequency-Division Multiplexing (OFDM) and high-order Quadrature Amplitude Modulation (e.g., 64-QAM, 256-QAM). These signals exhibit a high Peak-to-Average Power Ratio (PAPR), typically ranging from 6 to 12 dB [cite: 1, 2]. To maintain signal integrity and minimize Error Vector Magnitude (EVM), the Power Amplifier (PA)—the most power-hungry component of the RF front-end—must operate linearly. Classically, linearity is achieved by "backing off" the amplifier from its saturation point (Class A or Class AB operation). However, at mmWave frequencies, where intrinsic device gain is lower and parasitic losses are higher, operating at deep back-off results in unacceptably low efficiency, often below 10% [cite: 3].

Consequently, the "best approach" for optimizing this trade-off is not a single circuit technique but a composite methodology. It involves the synthesis of advanced active load-modulation architectures (specifically Doherty and LMBA topologies), advanced semiconductor materials (GaN-on-SiC and CMOS SOI), and sophisticated system-level linearization (Digital Predistortion). This report provides an exhaustive analysis of these methodologies, evaluating their efficacy in the mmWave domain.

---

## 2. The Physics of the Efficiency-Linearity Trade-off at mmWave

### 2.1 The Challenge of High PAPR Signals
In 5G mmWave systems, the statistical distribution of the signal amplitude is non-uniform. The signal operates at average power levels for the majority of the time but requires significant headroom for occasional high-power peaks. A conventional Class AB amplifier achieves maximum efficiency only at its peak saturated power ($P_{sat}$). As the input power decreases to the average level (back-off), the efficiency drops linearly (Class B) or faster (Class A).

For a signal with 9 dB PAPR, a conventional PA operating at average power might exhibit a Power Added Efficiency (PAE) of less than 10-15% [cite: 3]. Given that the PA can consume up to 75% of the total energy in a transmitter [cite: 4], this inefficiency creates thermal management issues in base stations and drastically reduces battery life in user equipment (UE). Therefore, the design objective is to extend the high-efficiency region of the PA into the back-off regime without compromising the linearity required to decode complex constellations.

### 2.2 Frequency-Dependent Limitations
Designing at mmWave frequencies (e.g., 28 GHz, 39 GHz, 60 GHz) introduces parasitic challenges not present at sub-6 GHz:
*   **Gain Reduction:** Transistor gain rolls off with frequency. Achieving sufficient gain often requires multi-stage designs, which complicates stability and efficiency [cite: 5].
*   **Parasitics:** Device parasitic capacitances ($C_{gs}$, $C_{gd}$) and inductances become significant portions of the matching network, making impedance transformation difficult [cite: 1].
*   **Passive Loss:** Transmission lines and matching networks on silicon or PCB suffer from higher skin effect and dielectric losses. This degrades the efficiency of power combining networks essential for architectures like Doherty or Outphasing [cite: 1].

---

## 3. Active Load Modulation Architectures

To address the efficiency drop at back-off, active load modulation techniques modify the load impedance presented to the transistor dynamically based on the signal envelope. This allows the voltage swing to remain high even at lower current levels, maintaining high efficiency.

### 3.1 The Doherty Power Amplifier (DPA)
The Doherty Power Amplifier is widely regarded as the standard solution for efficiency enhancement in 5G mmWave systems [cite: 1, 6, 7].

#### 3.1.1 Principle of Operation
The DPA consists of two amplifiers: a "Main" (or Carrier) amplifier biased in Class AB and an "Auxiliary" (or Peaking) amplifier biased in Class C.
*   **Low Power Region:** Only the Main amplifier is active. The load impedance it sees is transformed to a higher value (typically $2R_{opt}$), allowing it to saturate and reach peak efficiency at a fraction of the maximum power (typically 6 dB back-off).
*   **High Power Region:** As the signal peaks, the Auxiliary amplifier turns on. It injects current into the common load, which, through the impedance inverting network (typically a $\lambda/4$ line), modulates the load of the Main amplifier down to $R_{opt}$. This allows both amplifiers to contribute maximum power at saturation [cite: 1, 6].

#### 3.1.2 mmWave Implementation Challenges
While dominant at sub-6 GHz, DPA faces hurdles at mmWave:
*   **Phase Alignment:** The DPA relies on precise phase relationships (90-degree shifts) between the Main and Auxiliary paths. At 28 GHz, small physical length variations in transmission lines cause significant phase errors, degrading combining efficiency [cite: 1].
*   **Impedance Inverters:** Realizing ideal quarter-wave transformers is difficult due to parasitics. Designers often use lumped-element equivalents or absorb parasitics into the matching network [cite: 8].
*   **Bandwidth:** The conventional DPA is bandwidth-limited due to the frequency-selective nature of the quarter-wave transformers. 5G mmWave bands (e.g., 26.5–29.5 GHz) require wide fractional bandwidths that challenge standard DPA topologies [cite: 9].

#### 3.1.3 Advanced DPA Topologies
To optimize the trade-off further, several variations are employed:
*   **Asymmetric Doherty:** By using a larger Auxiliary device than the Main device, the efficiency peak can be shifted to deeper back-off levels (e.g., 8–9 dB), which better matches the PAPR of modern OFDM signals [cite: 6, 10].
*   **Three-Way Doherty:** Utilizing two auxiliary amplifiers to create extended high-efficiency regions (e.g., at 6 dB and 12 dB back-off) [cite: 11].
*   **Integrated DPA:** In GaN MMIC (Monolithic Microwave Integrated Circuit) implementations, the input splitters and output combiners are integrated on-chip to minimize parasitic inductance, achieving first-pass success at 28 GHz [cite: 1].

### 3.2 The Load Modulated Balanced Amplifier (LMBA)
The LMBA is gaining traction as a robust alternative to the DPA for mmWave applications, specifically addressing the bandwidth and VSWR (Voltage Standing Wave Ratio) limitations of the DPA [cite: 9, 12, 13].

#### 3.2.1 Operational Mechanism
The LMBA consists of a balanced amplifier pair (fed by a quadrature coupler) and a control signal injected at the output. The control signal, generated by an auxiliary PA, modulates the load impedance seen by the balanced pair.
*   **Advantages over DPA:** The LMBA does not rely on narrowband impedance inverters at the output. This allows for "literally unlimited bandwidth" theoretically, constrained only by the couplers and matching networks [cite: 9].
*   **Linearity:** The balanced nature of the topology naturally cancels certain harmonic products and improves return loss, making it more tolerant to antenna impedance mismatch—a critical factor in phased array antennas where scan impedance varies [cite: 9, 14].
*   **Performance:** Research demonstrates LMBAs at 2.4 GHz achieving 60% efficiency at peak and 50% at 6-dB back-off [cite: 12]. At mmWave (30–40 GHz), silicon-based LMBAs have demonstrated superior ACLR (Adjacent Channel Leakage Ratio) performance compared to traditional topologies [cite: 13].

### 3.3 Outphasing Amplifiers
Outphasing (or LINC - Linear Amplification with Nonlinear Components) converts amplitude modulation into phase modulation. Two constant-envelope amplifiers operate at peak efficiency, and their outputs are summed. The vector addition reconstructs the amplitude envelope.
*   **Comparison with DPA:** While Outphasing can theoretically achieve high efficiency, the power combiner (often a Chireix combiner) introduces significant losses if the phase and amplitude balance isn't perfect. At mmWave, the non-isolated nature of the combiner makes the interaction between PAs complex.
*   **Trade-off Analysis:** Comparative studies at 5G frequencies indicate that while Outphasing may achieve higher *peak* PAE, the Doherty architecture often provides superior linearity and efficiency at the critical 7.5 dB back-off point required for 64-QAM signals [cite: 10].

---

## 4. Linearization Techniques: The Digital Enabler

No matter which analog topology (Doherty or LMBA) is chosen, the active load modulation introduces severe non-linearities (AM-AM and AM-PM distortion). Consequently, the "best approach" invariably requires a linearization layer.

### 4.1 Digital Predistortion (DPD)
DPD is the industry standard for linearizing PAs. It involves processing the baseband signal with the inverse of the PA's non-linear transfer function before digital-to-analog conversion.

#### 4.1.1 The Bandwidth Bottleneck
The primary challenge for DPD at mmWave is bandwidth expansion. The DPD algorithm generates intermodulation products to cancel the PA's distortion. If the signal bandwidth is 100 MHz, the DPD correction signal may extend to 300–500 MHz (3rd to 5th order).
*   **Sampling Rate:** This requires Digital-to-Analog Converters (DACs) and Analog-to-Digital Converters (ADCs) in the feedback loop to operate at multi-GHz sampling rates, which consumes excessive power [cite: 15, 16].
*   **Solution - Band-Limited DPD:** Research suggests techniques that focus on linearizing only the in-band and immediate adjacent channels, or using spectral extrapolation to reduce the required feedback bandwidth [cite: 17].

#### 4.1.2 DPD for Phased Arrays
In Massive MIMO arrays, linearizing every single PA individually is computationally prohibitive.
*   **Array-Level DPD:** Techniques are being developed to linearize the entire array using a single DPD model based on the "far-field" aggregated signal, or by using a shared feedback path that samples different PAs sequentially [cite: 18, 19].

### 4.2 Analog Predistortion (APD)
For extremely wideband systems where DPD sampling rates are unfeasible, Analog Predistortion remains a viable, albeit less flexible, option. APD circuits (using diodes or transistors) generate non-linearities that oppose the PA's distortion directly at RF frequencies. While less precise than DPD, APD consumes negligible power and has infinite bandwidth relative to the signal [cite: 20].

---

## 5. Semiconductor Technologies and Integration

The choice of material is intrinsic to the optimization approach.

### 5.1 Gallium Nitride (GaN) on SiC
GaN is the preferred technology for high-power mmWave infrastructure (base stations).
*   **Attributes:** High breakdown voltage, high power density, and high efficiency.
*   **Doherty Synergy:** GaN's low output capacitance ($C_{ds}$) is favorable for Doherty combining. Recent 0.15 $\mu$m GaN-on-SiC processes enable high-efficiency MMICs at 28 GHz and 39 GHz [cite: 1].
*   **Performance:** GaN DPAs have demonstrated PAE > 40% at 6 dB back-off at 28 GHz, significantly outperforming silicon alternatives [cite: 1].

### 5.2 Silicon (CMOS/SiGe)
For user equipment (handsets) and highly integrated small cells, Silicon is dominant due to cost and integration with digital logic.
*   **Limitations:** Lower breakdown voltage and higher substrate losses.
*   **Optimization:** Silicon designs often utilize **stacking** (series combining) to increase voltage swing and **spatial power combining** to overcome substrate losses [cite: 21, 22].

---

## 6. Spatial Power Combining

At mmWave frequencies, the loss in on-chip matching networks and combiners can negate the efficiency gains of the PA core. Spatial power combining addresses this by combining the power of multiple amplifiers in free space (or waveguide structures) rather than through lossy transmission lines.

*   **Mechanism:** The outputs of multiple amplifier unit cells are fed to antenna elements. The signals combine constructively in the air (far-field).
*   **Efficiency:** This technique eliminates the "corporate feed" losses of traditional combiners. It is particularly effective for watt-level power generation in silicon technologies where on-chip losses are high [cite: 21, 23].
*   **Integration:** This approach is naturally synergistic with Phased Array (Beamforming) architectures required for 5G, where multiple elements are already present to provide antenna gain [cite: 5, 24].

---

## 7. Comparative Analysis and Conclusion

### 7.1 Trade-off Matrix

| Feature | Doherty PA (DPA) | Load Modulated Balanced Amp (LMBA) | Outphasing | Class AB + DPD |
| :--- | :--- | :--- | :--- | :--- |
| **Back-off Efficiency** | High (Excellent for 6-9dB OBO) | High (Tunable OBO) | High (Theoretical) | Low |
| **Linearity (Raw)** | Poor (Requires DPD) | Moderate (Better VSWR tolerance) | Poor (Requires precise balance) | Moderate |
| **Bandwidth** | Limited (Narrowband inverters) | Wide (Broadband couplers) | Limited (Combiner isolation) | Wide |
| **Complexity** | Moderate | High (Requires control PA) | High (Signal separation) | Low (Analog) / High (Digital) |
| **mmWave Suitability** | High (Standard 5G choice) | High (Emerging for wideband) | Moderate (Combiner losses) | Low (Inefficient) |

### 7.2 The Optimal Approach

Based on the synthesis of current research, the approach that best optimizes the trade-off between power amplifier efficiency and linearity for mmWave RF front-ends is the **Asymmetric Doherty Power Amplifier implemented in GaN-on-SiC, augmented by Digital Predistortion.**

**Justification:**
1.  **Efficiency Matching:** The asymmetric DPA topology can be tuned to peak efficiency at the specific back-off levels (e.g., 8 dB) dictated by 5G OFDM signals, maximizing battery life and minimizing thermal load [cite: 6, 10].
2.  **Material Performance:** GaN-on-SiC provides the necessary power density and minimizes parasitic capacitances that otherwise degrade mmWave load modulation [cite: 1].
3.  **Linearization:** While the DPA is non-linear, DPD is a mature technology that can correct this. For bandwidth-constrained systems, the **LMBA** serves as the best alternative, offering comparable efficiency with superior bandwidth and robustness against antenna mismatch [cite: 9, 12].
4.  **System Integration:** For high-power applications, these architectures should be integrated into **Spatial Power Combining** arrays to minimize passive losses [cite: 21].

In summary, the "best" optimization is not a single component but a holistic design strategy: **GaN-based Active Load Modulation (Doherty/LMBA) + Digital Linearization + Spatial Combining.** This triad addresses the physical limitations of the frequency, the statistical properties of the waveform, and the thermal constraints of the hardware.

## References
[cite: 1] Microwave Journal, "Doherty Power Amplifiers Move to mmWave"
[cite: 3] Analog Devices, "Optimizing Your Power Amplifier for Predistortion"
[cite: 6] PRFI Ltd, "Doherty MMIC for 28 GHz 5G"
[cite: 20] Chalmers University, "Best linearization techniques for mmWave"
[cite: 4] URSI, "mmWave RF front-end design PA efficiency linearity trade-off"
[cite: 10] MDPI, "Doherty vs Outphasing vs Envelope Tracking"
[cite: 2] Microwave Journal, "Modern High Efficiency Amplifier Design"
[cite: 1] Microwave Journal, "Doherty Power Amplifiers Move to mmWave"
[cite: 5] Microwave Journal, "RF Front-End Technology and Tradeoffs for 5G"
[cite: 8] MDPI, "mmWave PA architecture handset vs base station"
[cite: 25] ResearchGate, "High-Linearity mmWave Doherty Power Amplifier"
[cite: 15] Oulu Repo, "Digital predistortion bandwidth limitations"
[cite: 21] IEEE Xplore, "Spatial power combining mmWave PA efficiency"
[cite: 12] ResearchGate, "Analysis and Design of a Doherty-Like LMBA"
[cite: 9] IEEE MTT-S, "The Load-Modulated Balanced Amplifier"
[cite: 13] Semantic Scholar, "Load Modulated Balanced mm-Wave CMOS PA"
[cite: 7] IEEE Microwave, "Highly Efficient and Linearity-Enhanced Quasi-Balanced Doherty"
[cite: 17] Semantic Scholar, "Digital Predistortion of Ultra-Broadband mmWave Tx"
[cite: 11] MDPI, "GaN Doherty PA 28 GHz 5G PAE back-off efficiency"
[cite: 10] MDPI, "Comparison between Doherty and Outphasing"
[cite: 14] ResearchGate, "Review of Doherty and LMBA for 5G"

**Sources:**
1. [microwavejournal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd3-13EsZnGUUYajU4m34yeLsLEQ8En7_C9nfbKsvf2TbJjrwx_siele1ShVbzdO-pjqrksg-eIuvooc4bV-73YCFOGksChy-XBchWxEjUCh-ZjmpB90vbDNrFq-WvTyIJoHl4728QbZaaszzb9wAhzpQKrgt9yDqjERdx_tliBs9fR_cKDRtRVy2EIRk=)
2. [microwavejournal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFjWUgis-4Awj0T6VMKgp4WwENGI1E8TTWblI59DxGbC_-vmO7lYw5RKSGTWeF2evNiu4sTyKnJfg18p0aMbfoqfvbuZucSETgkSiMvO8Yc43uqcCJS1VcNgPMHZaYf0h7ZtsE_08qep_ZgU6KQj__8cLZQAVMHTfYYZrk_5uFwiJ9O8z2yBcl0HZeK76m6hu8FXanCwhSFVH2fUqCOUzpZkUtRKI1EBk7rd_knfZMFyE8tQ2usnk=)
3. [analog.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_KVK2fvKmNEYzkHm3IXL_35LeIFWMdg8uSNJaXyQrVTEZxKrWYLZg4aDGKb2rftB8YZrvoztIazr425iXGv9BQmbbKhVoIN-70HGoVCl_N6urUxYx95SrbbYPPFAQ1UHYNXhj75xBJekZlZ8w7GbXLap9l0ITRtPHO8Z8rVG58D65ynYYfG346LFx4pctA1_AjM-EIX6I8iFmgFe68Ni0tnY6IIpGNrrzzkE6V20yV24sDPpWUZwS6be5ZEBc15Sh)
4. [ursi.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbCpbMrnVOQElqoS-7fl_RmGIdJELv2nyuAz4HqK3egl0sgnFLq7R4_oMB_4xmS7U5WzLbT83EZNIN2vBXgc203eynPPRejcYpGPoLmCbBK7QpAzNiKsvs1-XCJhof_G5yq-is9jYlm_PWDhwXtu3s)
5. [microwavejournal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLvNnpoVuNQx-WylJYSFliYd7SYDcbzQxlI6wwKoyrIulDPkHlM08PuR358AOW3A9cop9mpBA9sq8piHLjIoODDZLpiWPH2hf9w6B4ITNfG7uQtbZfPipXyP8QyYP9hvpH7jK3c62w96kr-Dmw-xQB8DCzAmkCTUE1jRt3eXZoHhmgvMdR5W92hJsK3WhZnZE-bUHs6CfHE4GqWiZKfMnyZfd9ooIAXOsUQ6QD02lJ)
6. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEd6Pt8v6KgghWMQd996GdvsbZRbs-a5jbPiZLoypNl-tK7i8N7qQPPvLG40m0y3YtKcSBVyx5Yjx3avDsM-Wc1dT0hGJGxMGB5HtOgWLyWvybiaWI96-WNu4zV5HzzuqX5)
7. [nxtbook.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGk6Yo5a-KABvviMeChFclNz7oYo1WQb_nAQHoR8ntABZpq_DwldNqRvqkm_5oFuAncIDsJr-tw6iaUbLOPIv2hV2Jwk7j2PnspGd8d0skF-0GDv_x7f4vApz2csui7EI6rHQcXw73ozKDfr9AJPoEmzs7Hg5miJMDWCIwDKhUpw9sQu1a-ja1ULqDahEKpGs5ggv4atw==)
8. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgF8M4Mxe0u3aG8M9MIN10axIsxtLTP6qCdGLxD4NjNfcFZZADM8quWybu3GyCGPo_SHGDjHcwCUfdkqCHDHXTpEULFQT-K8qL12Zqjez6sjTQYbokCymxKrDz)
9. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL-T5refJmTCYo675xjBER0Xq_zgd-5fUzwdvlz_pE9rHmymDFdTqDksrDdhFDQIf3mX-Dg-ZtLtNHBgCS4ynO-Cw7JJ4K-BCJll8edOT30i04qysqSbq8snkQc8oFpWUe)
10. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqesYKtme-It69SpG3w1u0b0J6qr23wIRKLPtfLNcWtSc3QtVHcJ_Dwyt1en9tBny6TX0JlEPV1jTjT9cOpZHr1-Nibx8lMkrtmn2IZL1PgJJgfLBBz-fvss-S9NfI)
11. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWYsthzk0sJlIRiukVRwuGzfMPJUdNdSWZM5zDI1KGej_pfic06f4-LbOSHjYvngH_DVxeC4kFIjsglnI6YGt2_d-QrrkyGKVPEOnYUc1Ve94rIT3QTaE9FLmn-O7UVA==)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVyJR2h7hwPR_sMtJchf4ip_j0T4OX37TS3ypeyc_TB1Iz8BrAXodd2RdAQD5a60wUnl-Lqy0GnWFASL-jo4dpcG_1-2diAaXkuC4LWqILgFcWdPVSH71xIqOj_WJK8YjgRfufIqCVd8PORxkf38M9iGej4JOIm31o2xggmYPn6T8xRydnrcbgfG_ohOEw5euXCUo0oyuuzoNqRQhSAWtmW8BIygU2kYx3BD9SVO-MLie7fKyt9Qb1H3k=)
13. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjTGDFchht-s5V8w58JJinp6Mflf7EoNF_YNDtSU5Zh0C0_XVVcc0YFlqiv2xg6WoF9tT63xZiFtNqT0dptjr3-NPdHyceKw5b5fXsga9-scWATfr9mbmP-KoFeHUhh_mpQVCA1cZZxdWKZX1Qd_IH47HW41APeL5pLCPd_nE4s3quniSZocPIp9hrRYhnOTm6NqS6NJivsS-Xu68ETxx5UpwvWxpTReLEzyQdygY1D5srY0COQuzhpCeXCAyxxnu9wpYgb1AArmY=)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnbwHnNCRoWtuM76UTRcK_NymrigHFn3iU2Caaj3Tolu1-60QXQ5nUe234sxWfio76Mq88QJiFA6Hghv7EB02RDVi6yisupVEAWyhu7FgI2siMuei47qLaOhKgbZGLGKktfBncVtarwv2xstgFhNUqH-r-wu2J71btP1y5n29V7C85Q3chJoLlQLfftqrif7_JW3xCL8FAGWkGVzDbf5_wqTbXtKnNNrW5URmLA8uflwkQPNNuEolBXGfjSjREc5ekQH0Y4g==)
15. [oulu.fi](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwUeHoGHH2eBL8MLktmufrBpdqx9jm0fvZH7gfmFFA9HT0pZR9-3zX5mjk74ylYdjQOSqgYtpWS05yN19piQ9zJ1BoW5_wXhXisUNEQP4fPrky5yxWCaZuHC_U2Sq39fyzBSq7H-QX3D0pHo2AhIBW5lNMOVibYURnSxSXLQwCCtC_cosSXyuNgZoybdTYvz5dWQ0mQ3aVGiWVAg==)
16. [analog.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAryKDVRIBfV3IXC8t5rYiyB269aysAX8QTRCrvX-JcuC6_NOmM6HK4tJO2zAduj1ddsLYh_VycZIxXsxADgPVxvpB4p6v9nrW8ZVzoE8GvhLDAx9Lx2hl1a8L3NxsFen8nsqxgU0s_Ky6DpB1ZH-FSuddnUi9L_opZavvVYa-Gnh--2fF8wJ23mAUCn68PwYnSzBhn1cwPSRCiaW1-6MRpZnZ)
17. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsiySWjrdeqvC4WLy0_ngMX9HASZmN1YIhE07hmx8ZaxdKWEV98ljWFcoX1Qqu2E6OEOOEPIoFK8QvxD4ejeLm3WrPezrJ3lXjVpGcNbAg0VNgdZE196TZaoj8k1QlU9b28ZQXEP8zj9M2Q3ZsRWnnCt43COFEz5xk0TgnjldxlN0luYsH7zVWoQFezbt4ywAscGUqJf3cvFxmYFQCe66PBnbuBABo5ROx53XVcbxtsR5Fzt8POqohX_0FDOul)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9i6K7Mg9BH8aFMDKLYwrS9ERuAQlrCEekAF6vjM8nsE5iIHeJZcQ6YmygabCCcQlSXLz4fJ64qsxFIQhOA7Ahu3ZO83He7_nOKyIbt_o7S2HeyBcbqBSfa0DkRB6UHx6VpoNMsudpW-96zy98dG21_RkgqAUnZXvfrs-pTJpeEunWf9w8gFbqnF7e0d61m7NTq1p5a0SEoJY93qah5cS0u3Dtql3wZrl6GwHw5kM=)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpUTcThEYhKxy7uODZS6cUnXsNE16VkOjrzJWKaEgrkAt_myAOwEma7AO5PZKdZOSEG3WT0wccYTspK7V5SnJiU5DSQGdTiUEbzdGxpEUtBy0vziKSs4AWN8GBfzGH76D-uPXjVLI57a8fC772SL1UhSdmDM-1zkVrTuHk7DekaCCQfnWbhCn6D3w3AZl6NXnmkpmd2eOYFbx55nm8qvX41FB-X3fBPyECzFh1D1Unepe0dZEJMbojJnew8Q67iDO_eAwM8Glllt7UrgR5Ylcc0-szwZuIVuFUPMOcN10=)
20. [chalmers.se](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6BkDRO-3Mjg2sTTnpmaBp5tNIDj4wIy0yO_PuNrock_HG2epHX7QMbtAihhli6-PlJaruhUseN5SMnxWT3rREaBHvGqAZq0QwvsY47F37WxUfe1F3RrFDA9Xs78tlmxhO7wHtoooTJBCHcoxruJ7CLzyr9laYUfZJ2AK9aL0=)
21. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3plWOuF13PydT6QuD0SeB6Pc4hjDJOvNPUwdq3Of18Lk11juz8oBDkHUongHW6awesSuLISg-BYvAtFx_HWwYuNU8YHTXW3cSI42768VV1C3iUc0UWItkSAQfjJUVCgefZO4=)
22. [chalmers.se](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuxB-vx-noTYqAzQy9VTlclGTJqUfEEu-8OxQ30SLeSnD56o6FkhbS7z0XD65snMpdABlZRqOAMvtj5MOWDpE0_ccaU9uOwll6AjXgXx63gih0zXIqH_7X__O-5U5FASX4zdI-fWYhr3Nz5C7TdWJz3asg72C748ZPtADGTic=)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHduZPxdCjMbF9BTEFtlvJEcvghHcFlwOhk1HQvZ_oTkfe0XUy6ijrId5W8DAJzXumb0rJ66kh1ZoLgXDPbpsYpbH-HUipw3r5jbscKiu7ZyzsHEUVnJ1wa6BkK8CWThBhG-w13_oaTz-Na8qZ0Fh_0KV3kCUKts2twFpXwQPDbhW8OY-Fs4fz4A1rzNpSYiyP_0P4bmyCgbTTG)
24. [qorvo.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuI9GcaSAHR32h0kD3Bqeij-4jOotRz_CI665hglbEtTLGo6MHGCViYb5cSMLZdozMM-C-SCJ15pel0D5qPSsBEOtrtRqHddeL0r4vYtCSrMjpJhClwWrBRdsrUMJx6gxqt57MkWAVQbJMJPqJUB5xvSuUgRQgXQHchHovXzaqYJriVZxergcu8QGLv7kvIypiWhvcSCb2WTdlNRZVqmASiQ49RxU9i-PIkA==)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkcmstTyMyYXsMHBUMOpPGM6gkZwWdjdwGCmMeEOD10yxocw7Rfqd759VCH5kWPczt_m3iKu9qOXw7aaeUfeMhxTTNCELlxIyQkAEwWGQnPRx1n5G7xP-YRllUbCmJtaBeNCB8k_Rs1kgRVuKmZE066iS_9ai70AVNVQxOx_Z_BjyRWPQtyVvS1TNN-FL8sVY5_PXOAMmKqyGgZepLkJBP5n3SwzBfE0uupTOKZFiDNIbUIz0qEHoPrt3BQA==)


## Annotations
Annotation(end_index=2307, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFjWUgis-4Awj0T6VMKgp4WwENGI1E8TTWblI59DxGbC_-vmO7lYw5RKSGTWeF2evNiu4sTyKnJfg18p0aMbfoqfvbuZucSETgkSiMvO8Yc43uqcCJS1VcNgPMHZaYf0h7ZtsE_08qep_ZgU6KQj__8cLZQAVMHTfYYZrk_5uFwiJ9O8z2yBcl0HZeK76m6hu8FXanCwhSFVH2fUqCOUzpZkUtRKI1EBk7rd_knfZMFyE8tQ2usnk=', start_index=2295)
Annotation(end_index=2307, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd3-13EsZnGUUYajU4m34yeLsLEQ8En7_C9nfbKsvf2TbJjrwx_siele1ShVbzdO-pjqrksg-eIuvooc4bV-73YCFOGksChy-XBchWxEjUCh-ZjmpB90vbDNrFq-WvTyIJoHl4728QbZaaszzb9wAhzpQKrgt9yDqjERdx_tliBs9fR_cKDRtRVy2EIRk=', start_index=2295)
Annotation(end_index=2804, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_KVK2fvKmNEYzkHm3IXL_35LeIFWMdg8uSNJaXyQrVTEZxKrWYLZg4aDGKb2rftB8YZrvoztIazr425iXGv9BQmbbKhVoIN-70HGoVCl_N6urUxYx95SrbbYPPFAQ1UHYNXhj75xBJekZlZ8w7GbXLap9l0ITRtPHO8Z8rVG58D65ynYYfG346LFx4pctA1_AjM-EIX6I8iFmgFe68Ni0tnY6IIpGNrrzzkE6V20yV24sDPpWUZwS6be5ZEBc15Sh', start_index=2795)
Annotation(end_index=4026, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_KVK2fvKmNEYzkHm3IXL_35LeIFWMdg8uSNJaXyQrVTEZxKrWYLZg4aDGKb2rftB8YZrvoztIazr425iXGv9BQmbbKhVoIN-70HGoVCl_N6urUxYx95SrbbYPPFAQ1UHYNXhj75xBJekZlZ8w7GbXLap9l0ITRtPHO8Z8rVG58D65ynYYfG346LFx4pctA1_AjM-EIX6I8iFmgFe68Ni0tnY6IIpGNrrzzkE6V20yV24sDPpWUZwS6be5ZEBc15Sh', start_index=4017)
Annotation(end_index=4114, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbCpbMrnVOQElqoS-7fl_RmGIdJELv2nyuAz4HqK3egl0sgnFLq7R4_oMB_4xmS7U5WzLbT83EZNIN2vBXgc203eynPPRejcYpGPoLmCbBK7QpAzNiKsvs1-XCJhof_G5yq-is9jYlm_PWDhwXtu3s', start_index=4105)
Annotation(end_index=4773, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLvNnpoVuNQx-WylJYSFliYd7SYDcbzQxlI6wwKoyrIulDPkHlM08PuR358AOW3A9cop9mpBA9sq8piHLjIoODDZLpiWPH2hf9w6B4ITNfG7uQtbZfPipXyP8QyYP9hvpH7jK3c62w96kr-Dmw-xQB8DCzAmkCTUE1jRt3eXZoHhmgvMdR5W92hJsK3WhZnZE-bUHs6CfHE4GqWiZKfMnyZfd9ooIAXOsUQ6QD02lJ', start_index=4764)
Annotation(end_index=4966, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd3-13EsZnGUUYajU4m34yeLsLEQ8En7_C9nfbKsvf2TbJjrwx_siele1ShVbzdO-pjqrksg-eIuvooc4bV-73YCFOGksChy-XBchWxEjUCh-ZjmpB90vbDNrFq-WvTyIJoHl4728QbZaaszzb9wAhzpQKrgt9yDqjERdx_tliBs9fR_cKDRtRVy2EIRk=', start_index=4957)
Annotation(end_index=5224, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd3-13EsZnGUUYajU4m34yeLsLEQ8En7_C9nfbKsvf2TbJjrwx_siele1ShVbzdO-pjqrksg-eIuvooc4bV-73YCFOGksChy-XBchWxEjUCh-ZjmpB90vbDNrFq-WvTyIJoHl4728QbZaaszzb9wAhzpQKrgt9yDqjERdx_tliBs9fR_cKDRtRVy2EIRk=', start_index=5215)
Annotation(end_index=5732, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEd6Pt8v6KgghWMQd996GdvsbZRbs-a5jbPiZLoypNl-tK7i8N7qQPPvLG40m0y3YtKcSBVyx5Yjx3avDsM-Wc1dT0hGJGxMGB5HtOgWLyWvybiaWI96-WNu4zV5HzzuqX5', start_index=5717)
Annotation(end_index=5732, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGk6Yo5a-KABvviMeChFclNz7oYo1WQb_nAQHoR8ntABZpq_DwldNqRvqkm_5oFuAncIDsJr-tw6iaUbLOPIv2hV2Jwk7j2PnspGd8d0skF-0GDv_x7f4vApz2csui7EI6rHQcXw73ozKDfr9AJPoEmzs7Hg5miJMDWCIwDKhUpw9sQu1a-ja1ULqDahEKpGs5ggv4atw==', start_index=5717)
Annotation(end_index=5732, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd3-13EsZnGUUYajU4m34yeLsLEQ8En7_C9nfbKsvf2TbJjrwx_siele1ShVbzdO-pjqrksg-eIuvooc4bV-73YCFOGksChy-XBchWxEjUCh-ZjmpB90vbDNrFq-WvTyIJoHl4728QbZaaszzb9wAhzpQKrgt9yDqjERdx_tliBs9fR_cKDRtRVy2EIRk=', start_index=5717)
Annotation(end_index=6518, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEd6Pt8v6KgghWMQd996GdvsbZRbs-a5jbPiZLoypNl-tK7i8N7qQPPvLG40m0y3YtKcSBVyx5Yjx3avDsM-Wc1dT0hGJGxMGB5HtOgWLyWvybiaWI96-WNu4zV5HzzuqX5', start_index=6506)
Annotation(end_index=6518, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd3-13EsZnGUUYajU4m34yeLsLEQ8En7_C9nfbKsvf2TbJjrwx_siele1ShVbzdO-pjqrksg-eIuvooc4bV-73YCFOGksChy-XBchWxEjUCh-ZjmpB90vbDNrFq-WvTyIJoHl4728QbZaaszzb9wAhzpQKrgt9yDqjERdx_tliBs9fR_cKDRtRVy2EIRk=', start_index=6506)
Annotation(end_index=6889, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd3-13EsZnGUUYajU4m34yeLsLEQ8En7_C9nfbKsvf2TbJjrwx_siele1ShVbzdO-pjqrksg-eIuvooc4bV-73YCFOGksChy-XBchWxEjUCh-ZjmpB90vbDNrFq-WvTyIJoHl4728QbZaaszzb9wAhzpQKrgt9yDqjERdx_tliBs9fR_cKDRtRVy2EIRk=', start_index=6880)
Annotation(end_index=7097, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgF8M4Mxe0u3aG8M9MIN10axIsxtLTP6qCdGLxD4NjNfcFZZADM8quWybu3GyCGPo_SHGDjHcwCUfdkqCHDHXTpEULFQT-K8qL12Zqjez6sjTQYbokCymxKrDz', start_index=7088)
Annotation(end_index=7355, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL-T5refJmTCYo675xjBER0Xq_zgd-5fUzwdvlz_pE9rHmymDFdTqDksrDdhFDQIf3mX-Dg-ZtLtNHBgCS4ynO-Cw7JJ4K-BCJll8edOT30i04qysqSbq8snkQc8oFpWUe', start_index=7346)
Annotation(end_index=7691, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEd6Pt8v6KgghWMQd996GdvsbZRbs-a5jbPiZLoypNl-tK7i8N7qQPPvLG40m0y3YtKcSBVyx5Yjx3avDsM-Wc1dT0hGJGxMGB5HtOgWLyWvybiaWI96-WNu4zV5HzzuqX5', start_index=7678)
Annotation(end_index=7691, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqesYKtme-It69SpG3w1u0b0J6qr23wIRKLPtfLNcWtSc3QtVHcJ_Dwyt1en9tBny6TX0JlEPV1jTjT9cOpZHr1-Nibx8lMkrtmn2IZL1PgJJgfLBBz-fvss-S9NfI', start_index=7678)
Annotation(end_index=7843, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWYsthzk0sJlIRiukVRwuGzfMPJUdNdSWZM5zDI1KGej_pfic06f4-LbOSHjYvngH_DVxeC4kFIjsglnI6YGt2_d-QrrkyGKVPEOnYUc1Ve94rIT3QTaE9FLmn-O7UVA==', start_index=7833)
Annotation(end_index=8086, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd3-13EsZnGUUYajU4m34yeLsLEQ8En7_C9nfbKsvf2TbJjrwx_siele1ShVbzdO-pjqrksg-eIuvooc4bV-73YCFOGksChy-XBchWxEjUCh-ZjmpB90vbDNrFq-WvTyIJoHl4728QbZaaszzb9wAhzpQKrgt9yDqjERdx_tliBs9fR_cKDRtRVy2EIRk=', start_index=8077)
Annotation(end_index=8348, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL-T5refJmTCYo675xjBER0Xq_zgd-5fUzwdvlz_pE9rHmymDFdTqDksrDdhFDQIf3mX-Dg-ZtLtNHBgCS4ynO-Cw7JJ4K-BCJll8edOT30i04qysqSbq8snkQc8oFpWUe', start_index=8331)
Annotation(end_index=8348, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVyJR2h7hwPR_sMtJchf4ip_j0T4OX37TS3ypeyc_TB1Iz8BrAXodd2RdAQD5a60wUnl-Lqy0GnWFASL-jo4dpcG_1-2diAaXkuC4LWqILgFcWdPVSH71xIqOj_WJK8YjgRfufIqCVd8PORxkf38M9iGej4JOIm31o2xggmYPn6T8xRydnrcbgfG_ohOEw5euXCUo0oyuuzoNqRQhSAWtmW8BIygU2kYx3BD9SVO-MLie7fKyt9Qb1H3k=', start_index=8331)
Annotation(end_index=8348, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjTGDFchht-s5V8w58JJinp6Mflf7EoNF_YNDtSU5Zh0C0_XVVcc0YFlqiv2xg6WoF9tT63xZiFtNqT0dptjr3-NPdHyceKw5b5fXsga9-scWATfr9mbmP-KoFeHUhh_mpQVCA1cZZxdWKZX1Qd_IH47HW41APeL5pLCPd_nE4s3quniSZocPIp9hrRYhnOTm6NqS6NJivsS-Xu68ETxx5UpwvWxpTReLEzyQdygY1D5srY0COQuzhpCeXCAyxxnu9wpYgb1AArmY=', start_index=8331)
Annotation(end_index=8840, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL-T5refJmTCYo675xjBER0Xq_zgd-5fUzwdvlz_pE9rHmymDFdTqDksrDdhFDQIf3mX-Dg-ZtLtNHBgCS4ynO-Cw7JJ4K-BCJll8edOT30i04qysqSbq8snkQc8oFpWUe', start_index=8831)
Annotation(end_index=9107, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL-T5refJmTCYo675xjBER0Xq_zgd-5fUzwdvlz_pE9rHmymDFdTqDksrDdhFDQIf3mX-Dg-ZtLtNHBgCS4ynO-Cw7JJ4K-BCJll8edOT30i04qysqSbq8snkQc8oFpWUe', start_index=9094)
Annotation(end_index=9107, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnbwHnNCRoWtuM76UTRcK_NymrigHFn3iU2Caaj3Tolu1-60QXQ5nUe234sxWfio76Mq88QJiFA6Hghv7EB02RDVi6yisupVEAWyhu7FgI2siMuei47qLaOhKgbZGLGKktfBncVtarwv2xstgFhNUqH-r-wu2J71btP1y5n29V7C85Q3chJoLlQLfftqrif7_JW3xCL8FAGWkGVzDbf5_wqTbXtKnNNrW5URmLA8uflwkQPNNuEolBXGfjSjREc5ekQH0Y4g==', start_index=9094)
Annotation(end_index=9237, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVyJR2h7hwPR_sMtJchf4ip_j0T4OX37TS3ypeyc_TB1Iz8BrAXodd2RdAQD5a60wUnl-Lqy0GnWFASL-jo4dpcG_1-2diAaXkuC4LWqILgFcWdPVSH71xIqOj_WJK8YjgRfufIqCVd8PORxkf38M9iGej4JOIm31o2xggmYPn6T8xRydnrcbgfG_ohOEw5euXCUo0oyuuzoNqRQhSAWtmW8BIygU2kYx3BD9SVO-MLie7fKyt9Qb1H3k=', start_index=9227)
Annotation(end_index=9406, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjTGDFchht-s5V8w58JJinp6Mflf7EoNF_YNDtSU5Zh0C0_XVVcc0YFlqiv2xg6WoF9tT63xZiFtNqT0dptjr3-NPdHyceKw5b5fXsga9-scWATfr9mbmP-KoFeHUhh_mpQVCA1cZZxdWKZX1Qd_IH47HW41APeL5pLCPd_nE4s3quniSZocPIp9hrRYhnOTm6NqS6NJivsS-Xu68ETxx5UpwvWxpTReLEzyQdygY1D5srY0COQuzhpCeXCAyxxnu9wpYgb1AArmY=', start_index=9396)
Annotation(end_index=10297, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqesYKtme-It69SpG3w1u0b0J6qr23wIRKLPtfLNcWtSc3QtVHcJ_Dwyt1en9tBny6TX0JlEPV1jTjT9cOpZHr1-Nibx8lMkrtmn2IZL1PgJJgfLBBz-fvss-S9NfI', start_index=10287)
Annotation(end_index=11326, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwUeHoGHH2eBL8MLktmufrBpdqx9jm0fvZH7gfmFFA9HT0pZR9-3zX5mjk74ylYdjQOSqgYtpWS05yN19piQ9zJ1BoW5_wXhXisUNEQP4fPrky5yxWCaZuHC_U2Sq39fyzBSq7H-QX3D0pHo2AhIBW5lNMOVibYURnSxSXLQwCCtC_cosSXyuNgZoybdTYvz5dWQ0mQ3aVGiWVAg==', start_index=11312)
Annotation(end_index=11326, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAryKDVRIBfV3IXC8t5rYiyB269aysAX8QTRCrvX-JcuC6_NOmM6HK4tJO2zAduj1ddsLYh_VycZIxXsxADgPVxvpB4p6v9nrW8ZVzoE8GvhLDAx9Lx2hl1a8L3NxsFen8nsqxgU0s_Ky6DpB1ZH-FSuddnUi9L_opZavvVYa-Gnh--2fF8wJ23mAUCn68PwYnSzBhn1cwPSRCiaW1-6MRpZnZ', start_index=11312)
Annotation(end_index=11554, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsiySWjrdeqvC4WLy0_ngMX9HASZmN1YIhE07hmx8ZaxdKWEV98ljWFcoX1Qqu2E6OEOOEPIoFK8QvxD4ejeLm3WrPezrJ3lXjVpGcNbAg0VNgdZE196TZaoj8k1QlU9b28ZQXEP8zj9M2Q3ZsRWnnCt43COFEz5xk0TgnjldxlN0luYsH7zVWoQFezbt4ywAscGUqJf3cvFxmYFQCe66PBnbuBABo5ROx53XVcbxtsR5Fzt8POqohX_0FDOul', start_index=11544)
Annotation(end_index=11931, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpUTcThEYhKxy7uODZS6cUnXsNE16VkOjrzJWKaEgrkAt_myAOwEma7AO5PZKdZOSEG3WT0wccYTspK7V5SnJiU5DSQGdTiUEbzdGxpEUtBy0vziKSs4AWN8GBfzGH76D-uPXjVLI57a8fC772SL1UhSdmDM-1zkVrTuHk7DekaCCQfnWbhCn6D3w3AZl6NXnmkpmd2eOYFbx55nm8qvX41FB-X3fBPyECzFh1D1Unepe0dZEJMbojJnew8Q67iDO_eAwM8Glllt7UrgR5Ylcc0-szwZuIVuFUPMOcN10=', start_index=11917)
Annotation(end_index=11931, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9i6K7Mg9BH8aFMDKLYwrS9ERuAQlrCEekAF6vjM8nsE5iIHeJZcQ6YmygabCCcQlSXLz4fJ64qsxFIQhOA7Ahu3ZO83He7_nOKyIbt_o7S2HeyBcbqBSfa0DkRB6UHx6VpoNMsudpW-96zy98dG21_RkgqAUnZXvfrs-pTJpeEunWf9w8gFbqnF7e0d61m7NTq1p5a0SEoJY93qah5cS0u3Dtql3wZrl6GwHw5kM=', start_index=11917)
Annotation(end_index=12357, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6BkDRO-3Mjg2sTTnpmaBp5tNIDj4wIy0yO_PuNrock_HG2epHX7QMbtAihhli6-PlJaruhUseN5SMnxWT3rREaBHvGqAZq0QwvsY47F37WxUfe1F3RrFDA9Xs78tlmxhO7wHtoooTJBCHcoxruJ7CLzyr9laYUfZJ2AK9aL0=', start_index=12347)
Annotation(end_index=12890, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd3-13EsZnGUUYajU4m34yeLsLEQ8En7_C9nfbKsvf2TbJjrwx_siele1ShVbzdO-pjqrksg-eIuvooc4bV-73YCFOGksChy-XBchWxEjUCh-ZjmpB90vbDNrFq-WvTyIJoHl4728QbZaaszzb9wAhzpQKrgt9yDqjERdx_tliBs9fR_cKDRtRVy2EIRk=', start_index=12881)
Annotation(end_index=13036, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd3-13EsZnGUUYajU4m34yeLsLEQ8En7_C9nfbKsvf2TbJjrwx_siele1ShVbzdO-pjqrksg-eIuvooc4bV-73YCFOGksChy-XBchWxEjUCh-ZjmpB90vbDNrFq-WvTyIJoHl4728QbZaaszzb9wAhzpQKrgt9yDqjERdx_tliBs9fR_cKDRtRVy2EIRk=', start_index=13027)
Annotation(end_index=13459, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3plWOuF13PydT6QuD0SeB6Pc4hjDJOvNPUwdq3Of18Lk11juz8oBDkHUongHW6awesSuLISg-BYvAtFx_HWwYuNU8YHTXW3cSI42768VV1C3iUc0UWItkSAQfjJUVCgefZO4=', start_index=13445)
Annotation(end_index=13459, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuxB-vx-noTYqAzQy9VTlclGTJqUfEEu-8OxQ30SLeSnD56o6FkhbS7z0XD65snMpdABlZRqOAMvtj5MOWDpE0_ccaU9uOwll6AjXgXx63gih0zXIqH_7X__O-5U5FASX4zdI-fWYhr3Nz5C7TdWJz3asg72C748ZPtADGTic=', start_index=13445)
Annotation(end_index=14174, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3plWOuF13PydT6QuD0SeB6Pc4hjDJOvNPUwdq3Of18Lk11juz8oBDkHUongHW6awesSuLISg-BYvAtFx_HWwYuNU8YHTXW3cSI42768VV1C3iUc0UWItkSAQfjJUVCgefZO4=', start_index=14160)
Annotation(end_index=14174, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHduZPxdCjMbF9BTEFtlvJEcvghHcFlwOhk1HQvZ_oTkfe0XUy6ijrId5W8DAJzXumb0rJ66kh1ZoLgXDPbpsYpbH-HUipw3r5jbscKiu7ZyzsHEUVnJ1wa6BkK8CWThBhG-w13_oaTz-Na8qZ0Fh_0KV3kCUKts2twFpXwQPDbhW8OY-Fs4fz4A1rzNpSYiyP_0P4bmyCgbTTG', start_index=14160)
Annotation(end_index=14380, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuI9GcaSAHR32h0kD3Bqeij-4jOotRz_CI665hglbEtTLGo6MHGCViYb5cSMLZdozMM-C-SCJ15pel0D5qPSsBEOtrtRqHddeL0r4vYtCSrMjpJhClwWrBRdsrUMJx6gxqt57MkWAVQbJMJPqJUB5xvSuUgRQgXQHchHovXzaqYJriVZxergcu8QGLv7kvIypiWhvcSCb2WTdlNRZVqmASiQ49RxU9i-PIkA==', start_index=14367)
Annotation(end_index=14380, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLvNnpoVuNQx-WylJYSFliYd7SYDcbzQxlI6wwKoyrIulDPkHlM08PuR358AOW3A9cop9mpBA9sq8piHLjIoODDZLpiWPH2hf9w6B4ITNfG7uQtbZfPipXyP8QyYP9hvpH7jK3c62w96kr-Dmw-xQB8DCzAmkCTUE1jRt3eXZoHhmgvMdR5W92hJsK3WhZnZE-bUHs6CfHE4GqWiZKfMnyZfd9ooIAXOsUQ6QD02lJ', start_index=14367)
Annotation(end_index=15750, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEd6Pt8v6KgghWMQd996GdvsbZRbs-a5jbPiZLoypNl-tK7i8N7qQPPvLG40m0y3YtKcSBVyx5Yjx3avDsM-Wc1dT0hGJGxMGB5HtOgWLyWvybiaWI96-WNu4zV5HzzuqX5', start_index=15737)
Annotation(end_index=15750, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqesYKtme-It69SpG3w1u0b0J6qr23wIRKLPtfLNcWtSc3QtVHcJ_Dwyt1en9tBny6TX0JlEPV1jTjT9cOpZHr1-Nibx8lMkrtmn2IZL1PgJJgfLBBz-fvss-S9NfI', start_index=15737)
Annotation(end_index=15922, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd3-13EsZnGUUYajU4m34yeLsLEQ8En7_C9nfbKsvf2TbJjrwx_siele1ShVbzdO-pjqrksg-eIuvooc4bV-73YCFOGksChy-XBchWxEjUCh-ZjmpB90vbDNrFq-WvTyIJoHl4728QbZaaszzb9wAhzpQKrgt9yDqjERdx_tliBs9fR_cKDRtRVy2EIRk=', start_index=15913)
Annotation(end_index=16214, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL-T5refJmTCYo675xjBER0Xq_zgd-5fUzwdvlz_pE9rHmymDFdTqDksrDdhFDQIf3mX-Dg-ZtLtNHBgCS4ynO-Cw7JJ4K-BCJll8edOT30i04qysqSbq8snkQc8oFpWUe', start_index=16201)
Annotation(end_index=16214, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVyJR2h7hwPR_sMtJchf4ip_j0T4OX37TS3ypeyc_TB1Iz8BrAXodd2RdAQD5a60wUnl-Lqy0GnWFASL-jo4dpcG_1-2diAaXkuC4LWqILgFcWdPVSH71xIqOj_WJK8YjgRfufIqCVd8PORxkf38M9iGej4JOIm31o2xggmYPn6T8xRydnrcbgfG_ohOEw5euXCUo0oyuuzoNqRQhSAWtmW8BIygU2kYx3BD9SVO-MLie7fKyt9Qb1H3k=', start_index=16201)
Annotation(end_index=16391, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3plWOuF13PydT6QuD0SeB6Pc4hjDJOvNPUwdq3Of18Lk11juz8oBDkHUongHW6awesSuLISg-BYvAtFx_HWwYuNU8YHTXW3cSI42768VV1C3iUc0UWItkSAQfjJUVCgefZO4=', start_index=16381)
Annotation(end_index=16762, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd3-13EsZnGUUYajU4m34yeLsLEQ8En7_C9nfbKsvf2TbJjrwx_siele1ShVbzdO-pjqrksg-eIuvooc4bV-73YCFOGksChy-XBchWxEjUCh-ZjmpB90vbDNrFq-WvTyIJoHl4728QbZaaszzb9wAhzpQKrgt9yDqjERdx_tliBs9fR_cKDRtRVy2EIRk=', start_index=16753)
Annotation(end_index=16833, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_KVK2fvKmNEYzkHm3IXL_35LeIFWMdg8uSNJaXyQrVTEZxKrWYLZg4aDGKb2rftB8YZrvoztIazr425iXGv9BQmbbKhVoIN-70HGoVCl_N6urUxYx95SrbbYPPFAQ1UHYNXhj75xBJekZlZ8w7GbXLap9l0ITRtPHO8Z8rVG58D65ynYYfG346LFx4pctA1_AjM-EIX6I8iFmgFe68Ni0tnY6IIpGNrrzzkE6V20yV24sDPpWUZwS6be5ZEBc15Sh', start_index=16824)
Annotation(end_index=16911, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEd6Pt8v6KgghWMQd996GdvsbZRbs-a5jbPiZLoypNl-tK7i8N7qQPPvLG40m0y3YtKcSBVyx5Yjx3avDsM-Wc1dT0hGJGxMGB5HtOgWLyWvybiaWI96-WNu4zV5HzzuqX5', start_index=16902)
Annotation(end_index=16961, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6BkDRO-3Mjg2sTTnpmaBp5tNIDj4wIy0yO_PuNrock_HG2epHX7QMbtAihhli6-PlJaruhUseN5SMnxWT3rREaBHvGqAZq0QwvsY47F37WxUfe1F3RrFDA9Xs78tlmxhO7wHtoooTJBCHcoxruJ7CLzyr9laYUfZJ2AK9aL0=', start_index=16951)
Annotation(end_index=17035, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbCpbMrnVOQElqoS-7fl_RmGIdJELv2nyuAz4HqK3egl0sgnFLq7R4_oMB_4xmS7U5WzLbT83EZNIN2vBXgc203eynPPRejcYpGPoLmCbBK7QpAzNiKsvs1-XCJhof_G5yq-is9jYlm_PWDhwXtu3s', start_index=17026)
Annotation(end_index=17115, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqesYKtme-It69SpG3w1u0b0J6qr23wIRKLPtfLNcWtSc3QtVHcJ_Dwyt1en9tBny6TX0JlEPV1jTjT9cOpZHr1-Nibx8lMkrtmn2IZL1PgJJgfLBBz-fvss-S9NfI', start_index=17105)
Annotation(end_index=17176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFjWUgis-4Awj0T6VMKgp4WwENGI1E8TTWblI59DxGbC_-vmO7lYw5RKSGTWeF2evNiu4sTyKnJfg18p0aMbfoqfvbuZucSETgkSiMvO8Yc43uqcCJS1VcNgPMHZaYf0h7ZtsE_08qep_ZgU6KQj__8cLZQAVMHTfYYZrk_5uFwiJ9O8z2yBcl0HZeK76m6hu8FXanCwhSFVH2fUqCOUzpZkUtRKI1EBk7rd_knfZMFyE8tQ2usnk=', start_index=17167)
Annotation(end_index=17247, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd3-13EsZnGUUYajU4m34yeLsLEQ8En7_C9nfbKsvf2TbJjrwx_siele1ShVbzdO-pjqrksg-eIuvooc4bV-73YCFOGksChy-XBchWxEjUCh-ZjmpB90vbDNrFq-WvTyIJoHl4728QbZaaszzb9wAhzpQKrgt9yDqjERdx_tliBs9fR_cKDRtRVy2EIRk=', start_index=17238)
Annotation(end_index=17318, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLvNnpoVuNQx-WylJYSFliYd7SYDcbzQxlI6wwKoyrIulDPkHlM08PuR358AOW3A9cop9mpBA9sq8piHLjIoODDZLpiWPH2hf9w6B4ITNfG7uQtbZfPipXyP8QyYP9hvpH7jK3c62w96kr-Dmw-xQB8DCzAmkCTUE1jRt3eXZoHhmgvMdR5W92hJsK3WhZnZE-bUHs6CfHE4GqWiZKfMnyZfd9ooIAXOsUQ6QD02lJ', start_index=17309)
Annotation(end_index=17394, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgF8M4Mxe0u3aG8M9MIN10axIsxtLTP6qCdGLxD4NjNfcFZZADM8quWybu3GyCGPo_SHGDjHcwCUfdkqCHDHXTpEULFQT-K8qL12Zqjez6sjTQYbokCymxKrDz', start_index=17385)
Annotation(end_index=17460, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkcmstTyMyYXsMHBUMOpPGM6gkZwWdjdwGCmMeEOD10yxocw7Rfqd759VCH5kWPczt_m3iKu9qOXw7aaeUfeMhxTTNCELlxIyQkAEwWGQnPRx1n5G7xP-YRllUbCmJtaBeNCB8k_Rs1kgRVuKmZE066iS_9ai70AVNVQxOx_Z_BjyRWPQtyVvS1TNN-FL8sVY5_PXOAMmKqyGgZepLkJBP5n3SwzBfE0uupTOKZFiDNIbUIz0qEHoPrt3BQA==', start_index=17450)
Annotation(end_index=17533, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwUeHoGHH2eBL8MLktmufrBpdqx9jm0fvZH7gfmFFA9HT0pZR9-3zX5mjk74ylYdjQOSqgYtpWS05yN19piQ9zJ1BoW5_wXhXisUNEQP4fPrky5yxWCaZuHC_U2Sq39fyzBSq7H-QX3D0pHo2AhIBW5lNMOVibYURnSxSXLQwCCtC_cosSXyuNgZoybdTYvz5dWQ0mQ3aVGiWVAg==', start_index=17523)
Annotation(end_index=17601, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3plWOuF13PydT6QuD0SeB6Pc4hjDJOvNPUwdq3Of18Lk11juz8oBDkHUongHW6awesSuLISg-BYvAtFx_HWwYuNU8YHTXW3cSI42768VV1C3iUc0UWItkSAQfjJUVCgefZO4=', start_index=17591)
Annotation(end_index=17672, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVyJR2h7hwPR_sMtJchf4ip_j0T4OX37TS3ypeyc_TB1Iz8BrAXodd2RdAQD5a60wUnl-Lqy0GnWFASL-jo4dpcG_1-2diAaXkuC4LWqILgFcWdPVSH71xIqOj_WJK8YjgRfufIqCVd8PORxkf38M9iGej4JOIm31o2xggmYPn6T8xRydnrcbgfG_ohOEw5euXCUo0oyuuzoNqRQhSAWtmW8BIygU2kYx3BD9SVO-MLie7fKyt9Qb1H3k=', start_index=17662)
Annotation(end_index=17741, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL-T5refJmTCYo675xjBER0Xq_zgd-5fUzwdvlz_pE9rHmymDFdTqDksrDdhFDQIf3mX-Dg-ZtLtNHBgCS4ynO-Cw7JJ4K-BCJll8edOT30i04qysqSbq8snkQc8oFpWUe', start_index=17732)
Annotation(end_index=17804, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjTGDFchht-s5V8w58JJinp6Mflf7EoNF_YNDtSU5Zh0C0_XVVcc0YFlqiv2xg6WoF9tT63xZiFtNqT0dptjr3-NPdHyceKw5b5fXsga9-scWATfr9mbmP-KoFeHUhh_mpQVCA1cZZxdWKZX1Qd_IH47HW41APeL5pLCPd_nE4s3quniSZocPIp9hrRYhnOTm6NqS6NJivsS-Xu68ETxx5UpwvWxpTReLEzyQdygY1D5srY0COQuzhpCeXCAyxxnu9wpYgb1AArmY=', start_index=17794)
Annotation(end_index=17874, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGk6Yo5a-KABvviMeChFclNz7oYo1WQb_nAQHoR8ntABZpq_DwldNqRvqkm_5oFuAncIDsJr-tw6iaUbLOPIv2hV2Jwk7j2PnspGd8d0skF-0GDv_x7f4vApz2csui7EI6rHQcXw73ozKDfr9AJPoEmzs7Hg5miJMDWCIwDKhUpw9sQu1a-ja1ULqDahEKpGs5ggv4atw==', start_index=17865)
Annotation(end_index=17966, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsiySWjrdeqvC4WLy0_ngMX9HASZmN1YIhE07hmx8ZaxdKWEV98ljWFcoX1Qqu2E6OEOOEPIoFK8QvxD4ejeLm3WrPezrJ3lXjVpGcNbAg0VNgdZE196TZaoj8k1QlU9b28ZQXEP8zj9M2Q3ZsRWnnCt43COFEz5xk0TgnjldxlN0luYsH7zVWoQFezbt4ywAscGUqJf3cvFxmYFQCe66PBnbuBABo5ROx53XVcbxtsR5Fzt8POqohX_0FDOul', start_index=17956)
Annotation(end_index=18048, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWYsthzk0sJlIRiukVRwuGzfMPJUdNdSWZM5zDI1KGej_pfic06f4-LbOSHjYvngH_DVxeC4kFIjsglnI6YGt2_d-QrrkyGKVPEOnYUc1Ve94rIT3QTaE9FLmn-O7UVA==', start_index=18038)
Annotation(end_index=18116, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqesYKtme-It69SpG3w1u0b0J6qr23wIRKLPtfLNcWtSc3QtVHcJ_Dwyt1en9tBny6TX0JlEPV1jTjT9cOpZHr1-Nibx8lMkrtmn2IZL1PgJJgfLBBz-fvss-S9NfI', start_index=18106)
Annotation(end_index=18177, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnbwHnNCRoWtuM76UTRcK_NymrigHFn3iU2Caaj3Tolu1-60QXQ5nUe234sxWfio76Mq88QJiFA6Hghv7EB02RDVi6yisupVEAWyhu7FgI2siMuei47qLaOhKgbZGLGKktfBncVtarwv2xstgFhNUqH-r-wu2J71btP1y5n29V7C85Q3chJoLlQLfftqrif7_JW3xCL8FAGWkGVzDbf5_wqTbXtKnNNrW5URmLA8uflwkQPNNuEolBXGfjSjREc5ekQH0Y4g==', start_index=18167)

## Sources
