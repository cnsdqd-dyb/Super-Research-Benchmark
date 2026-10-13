# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 0af4f872 | **Time:** 390.86s | **Cost:** $2.42236
--------------------------------------------------------------------------------

# Wavelength Division Multiplexing in On-Chip Optical Interconnects: Bandwidth Expansion, Energy Efficiency, and Crosstalk Constraints

### Key Points
*   **Bandwidth Potential:** Wavelength Division Multiplexing (WDM) enables massive scaling of on-chip bandwidth density, with shoreline bandwidth densities projected to reach between 2 Tbps/mm and 21 Tbps/mm depending on the device architecture (Microring Resonators vs. Arrayed Waveguide Gratings).
*   **Energy Efficiency Targets:** WDM architectures are critical for breaking the "energy wall" of electrical interconnects, with state-of-the-art experimental transceivers demonstrating efficiencies as low as 0.55–1.0 pJ/bit, significantly outperforming the >2.5 pJ/bit of traditional electrical links at similar distances.
*   **Crosstalk as the Primary Limiting Factor:** The extent of bandwidth expansion is strictly bounded by channel crosstalk. To maintain a power penalty below 1 dB, channel spacing is typically constrained to 50–100 GHz, and crosstalk suppression must generally exceed 20–25 dB.
*   **Thermal Constraints:** In dense WDM systems utilizing microring resonators, thermal crosstalk between tuning heaters creates a complex trade-off between integration density and control stability, often necessitating isolation structures that reduce the effective bandwidth density.
*   **Architectural Trade-offs:** There is a fundamental divergence in design strategy: Microring-based receivers offer superior bandwidth density (up to 21 Tbps/mm) and energy efficiency but suffer from high thermal sensitivity and crosstalk; conversely, AWG-based systems offer robust crosstalk performance but are limited to lower densities (~2.9 Tbps/mm²).

## 1. Introduction

The scaling of multi-core processors has reached a critical inflection point where the performance of the system is no longer limited by the speed of the computation cores, but by the bandwidth and energy efficiency of the interconnects moving data between them. As transistor scaling continues into the angstrom era, the "memory wall" and the "power wall" have necessitated a shift from electrical to optical interconnects for on-chip and chip-to-chip communication. Electrical interconnects, while mature, suffer from frequency-dependent attenuation and resistive heating, limiting their energy efficiency to approximately 2–10 pJ/bit for short-reach links and severely constraining bandwidth density due to signal integrity issues and pin-count limitations [cite: 1].

Optical Network-on-Chip (ONoC) architectures employing Wavelength Division Multiplexing (WDM) have emerged as the premier solution to these bottlenecks. By transmitting multiple non-interfering optical signals simultaneously over a single waveguide, WDM decouples bandwidth from the physical number of lanes, theoretically allowing for exponential capacity growth without a proportional increase in footprint [cite: 2, 3]. However, the realization of this potential is not unbounded. It is governed by strict physical constraints, most notably channel crosstalk—the leakage of optical power between adjacent spectral channels—and the energy cost associated with mitigating this crosstalk.

This report provides an exhaustive analysis of the extent to which WDM can expand the bandwidth and energy efficiency of on-chip multi-core processors. It synthesizes experimental data and theoretical models to quantify the trade-offs between spectral density, power penalties, and thermal management.

## 2. WDM Architecture for On-Chip Interconnects

To understand the capabilities and limitations of WDM, one must first analyze the fundamental components that enable this technology on a silicon platform. Unlike long-haul fiber optic systems, on-chip WDM must operate under extreme area and power constraints.

### 2.1. Microring Resonators (MRRs) as Enablers
The Microring Resonator (MRR) is the workhorse of dense on-chip WDM. These devices act as wavelength-selective filters, modulators, and detectors. Their small footprint (typically <20 µm diameter) allows them to be cascaded along a single bus waveguide to create multi-channel transceivers [cite: 4, 5].
*   **Functionality:** An MRR couples light from a bus waveguide only when the optical wavelength matches the resonance condition of the ring. This allows for the modulation of specific wavelengths (Tx) or the dropping of specific wavelengths (Rx) from a WDM comb.
*   **Density Advantage:** Because MRRs are compact, they enable extremely high "shoreline bandwidth density"—a metric defining how much data can be moved per millimeter of chip edge. Research indicates that MRR-based solutions can theoretically achieve shoreline bandwidth densities up to 21 Tbps/mm [cite: 6, 7].

### 2.2. Arrayed Waveguide Gratings (AWGs)
An alternative to MRRs is the Arrayed Waveguide Grating (AWG). AWGs are passive devices that use interference patterns to multiplex or demultiplex light.
*   **Comparison:** While AWGs are generally more robust to temperature variations and offer flatter passbands (reducing crosstalk sensitivity), they are significantly larger than MRRs. This physical size limits their area bandwidth density to approximately 2.9 Tbps/mm², compared to the much higher figures for MRRs [cite: 7]. However, AWGs do not require the extensive active thermal tuning that MRRs do, which has implications for the system's total energy budget.

### 2.3. Optical Frequency Combs
High-capacity WDM requires a light source capable of generating many distinct wavelengths. Integrated optical frequency combs (microcombs) have revolutionized this aspect. A single soliton microcomb can generate dozens of equidistant frequency lines (channels) from a single pump laser. Recent demonstrations have shown that such combs can support transmission capacities exceeding 10 Tbps in the C-band alone, with projected capacities of over 20 Tbps when combined with the L-band [cite: 8]. This centralization of the light source is crucial for energy efficiency, as it amortizes the "wall-plug" power of the laser across many data channels [cite: 1].

## 3. Bandwidth Expansion Capabilities

The primary promise of WDM is bandwidth expansion. The research indicates that WDM can expand on-chip bandwidth into the multi-terabit regime, far exceeding the capabilities of electrical I/O.

### 3.1. Channel Count and Data Rates
The extent of bandwidth expansion is a function of the number of channels ($N$) and the data rate per channel ($R$).
*   **Channel Scalability:** Current silicon photonic transceivers have demonstrated scalability up to 64 channels per fiber output [cite: 9]. Other architectures utilize 40 simultaneous channels [cite: 10, 11].
*   **Data Rates:** Per-channel data rates in experimental on-chip systems typically range from 10 Gbps to 56 Gbps, with advanced modulation formats (like PAM-4) pushing this towards 112 Gbps [cite: 1, 12].
*   **Aggregate Capacity:** By combining these factors, aggregate link capacities of 1.28 Tbps to 1.79 Tbps per fiber are realizable with current technology [cite: 12, 13]. Advanced experimental setups using multi-mode fibers and WDM have demonstrated petabit-scale transmission (3.56 Pb/s), though this is currently more applicable to fiber links than immediate on-chip integration [cite: 14]. For on-chip specific applications, the target is often cited as 6.4 Tbps per fiber for next-generation designs [cite: 6, 7].

### 3.2. Shoreline Bandwidth Density
A critical metric for multi-core processor interconnects is shoreline bandwidth density (SBD). This measures the aggregate bandwidth available per millimeter of the chip's edge, which is a scarce resource in package design.
*   **Current Benchmarks:** Standard optical modules offer ~22 Gbps/mm. Co-packaged optics (CPO) aim for >90 Gbps/mm [cite: 15].
*   **WDM Expansion:** WDM pushes this significantly further. MRR-based WDM solutions target SBDs of 2 Tbps/mm to 5 Tbps/mm in near-term commercial/research deployments [cite: 9, 16, 17].
*   **Theoretical Limits:** Simulation models suggest that with aggressive scaling and optimization of MRR arrays, SBDs could reach as high as 21 Tbps/mm [cite: 6, 7]. This represents a massive expansion over electrical counterparts, which struggle to maintain density due to signal isolation requirements.

## 4. Energy Efficiency Analysis

Expanding bandwidth is futile if the energy consumption exceeds the thermal design power (TDP) of the processor. WDM offers a pathway to reduce the energy-per-bit ($E_b$) metric.

### 4.1. The Energy Efficiency Gap
Electrical interconnects typically consume between 2.5 pJ/bit (Very Short Reach) and 7 pJ/bit (Long Reach) [cite: 1]. As data rates increase, electrical links require complex equalization and Forward Error Correction (FEC), which drives up power consumption.
In contrast, optical WDM links target sub-pJ/bit efficiencies.
*   **Experimental Achievements:** Research has demonstrated WDM receivers and transceivers achieving energy efficiencies of 0.55 pJ/bit to 1.06 pJ/bit at data rates of 20–40 Gbps [cite: 18, 19].
*   **System-Level Projections:** When including the laser source, thermal tuning, and driver electronics, the total link efficiency is often estimated in the range of 2–10 pJ/bit for current state-of-the-art systems [cite: 1]. However, optimized designs utilizing comb sources and efficient modulators project efficiencies dropping to ~0.7 pJ/bit [cite: 20].

### 4.2. Impact of WDM on Energy
WDM improves energy efficiency primarily through the amortization of fixed power costs.
*   **Laser Power Sharing:** In a single-wavelength link, the laser must be powered on for just one data stream. In a WDM system with a comb source, a single laser (and its temperature controller) supports $N$ channels. If the comb generation efficiency is high, the energy cost per bit drops as $N$ increases [cite: 1, 8].
*   **Thermal Tuning Overhead:** A major energy penalty in WDM comes from the need to thermally tune MRRs to align with the laser wavelengths. This tuning power can be significant (e.g., 4.9 µW/GHz) [cite: 18]. As channel count increases, the complexity and total power of tuning also increase, creating a trade-off. If the tuning power exceeds the savings from laser sharing, WDM scaling becomes energy-inefficient.

## 5. Crosstalk Constraints: The Limiting Factor

While WDM offers immense bandwidth and energy benefits, "crosstalk" is the fundamental physical constraint that limits the extent of this expansion. Crosstalk introduces noise, closes the eye diagram, and necessitates higher optical power to maintain Bit Error Rate (BER), thereby degrading energy efficiency.

### 5.1. Types of Crosstalk in WDM
*   **Inter-Channel Crosstalk:** This occurs when power from a signal at wavelength $\lambda_1$ leaks into the detector for $\lambda_2$. This is governed by the channel spacing and the roll-off (steepness) of the demultiplexer filters (MRR or AWG) [cite: 2].
*   **Intra-Channel (In-Band) Crosstalk:** This occurs when leakage signals are at the same wavelength as the signal of interest, often caused by multi-path interference or imperfect switching elements. This type of crosstalk is particularly damaging because it is coherent and cannot be filtered out [cite: 2].
*   **Thermal Crosstalk:** In dense on-chip circuits, the heat generated by a heater tuning Ring A can diffuse through the silicon substrate and detune Ring B. This is a critical issue for MRR-based WDM [cite: 21, 22].

### 5.2. Quantitative Impact on Bandwidth
The requirement to suppress crosstalk limits how closely channels can be packed (spectral efficiency).
*   **Channel Spacing:** To keep crosstalk power penalties below 1 dB, channel spacing is typically maintained at 50 GHz to 100 GHz [cite: 5, 11].
*   **Isolation Requirements:** Research indicates that crosstalk levels must be suppressed by approximately 20–25 dB relative to the signal to maintain a <1 dB power penalty for high-order modulation formats like QPSK [cite: 23, 24].
*   **Scalability Limit:** If channel spacing is reduced to increase bandwidth density (e.g., <50 GHz), inter-channel crosstalk rises sharply. This forces the use of higher-order filters (which have higher insertion loss) or limits the total number of channels. For example, a study showed that while 20 channels are feasible with low penalty, scaling beyond 70 channels can result in severe Raman-induced crosstalk and power penalties unless channel power is drastically reduced [cite: 25].

### 5.3. Quantitative Impact on Energy Efficiency
Crosstalk degrades the Signal-to-Noise Ratio (SNR). To compensate for a crosstalk-induced SNR penalty, the laser power must be increased.
*   **Power Penalty:** A 1 dB power penalty implies that the laser power must be increased by roughly 26% to achieve the same BER. This directly hurts the pJ/bit metric.
*   **Thermal Crosstalk Mitigation:** To prevent thermal crosstalk between dense MRRs, designers must use isolation trenches or increase the physical spacing between devices [cite: 22]. Increasing spacing reduces the shoreline bandwidth density. Alternatively, active thermal compensation algorithms can be used, but these consume computational resources and power [cite: 18].
*   **The "Floor":** There is a crosstalk floor where no amount of power increase can recover the signal (BER floor). Research shows that for certain architectures, the crosstalk-induced penalty is independent of transmission distance but highly dependent on wavelength allocation and component quality [cite: 26].

## 6. Trade-offs and Optimization

The extent of WDM expansion is a multi-variable optimization problem involving bandwidth, energy, and crosstalk.

### 6.1. MRR vs. AWG Trade-off
*   **MRR:** Offers the highest bandwidth density (up to 21 Tbps/mm) and low energy (<1 pJ/bit potential). However, it is severely constrained by thermal crosstalk and requires complex control loops to maintain resonance alignment [cite: 6, 7].
*   **AWG:** Offers lower bandwidth density (~2.9 Tbps/mm²) and higher footprint. However, it provides better passive crosstalk suppression and does not require per-channel thermal tuning, potentially offering a more stable and simpler system at the cost of peak density [cite: 6, 7].

### 6.2. Spacing vs. Capacity
Reducing channel spacing from 100 GHz to 50 GHz doubles the spectral efficiency and bandwidth density. However, it increases inter-channel crosstalk. To mitigate this, higher-Q filters are needed, which are more sensitive to thermal drift, thereby increasing the thermal tuning power requirement. Thus, **maximum bandwidth density** and **maximum energy efficiency** are often mutually exclusive goals. The "sweet spot" appears to be around 50–100 GHz spacing for current silicon photonic processes [cite: 5, 9].

## 7. Conclusion

To what extent can WDM expand on-chip interconnects?

1.  **Bandwidth Extent:** WDM can expand on-chip bandwidth density by **10x to 100x** compared to electrical interconnects. Shoreline bandwidth densities of **2–5 Tbps/mm** are practically achievable today, with theoretical limits extending to **21 Tbps/mm** using advanced microring architectures. Aggregate per-fiber capacities can reach **6.4 Tbps** in on-chip contexts and up to **20 Tbps** in broader optical link contexts.
2.  **Energy Efficiency Extent:** WDM can improve energy efficiency to the **sub-pJ/bit** regime (0.5–1.0 pJ/bit), representing a **5x to 10x improvement** over standard electrical links. However, this is contingent on highly efficient comb sources and precise thermal management.
3.  **The Constraint Boundary:** These expansions are hard-limited by crosstalk. To maintain an acceptable power penalty (<1 dB), channel spacing is generally limited to **>50 GHz**, and component crosstalk suppression must be **>20 dB**. Thermal crosstalk in dense MRR arrays imposes a physical spacing limit that prevents the theoretical maximum density from being fully realized without sophisticated isolation or active compensation.

In summary, WDM is the critical enabler for next-generation multi-core processor scaling, offering a path to petabit-scale aggregate bandwidths. However, the engineering reality is a tight optimization game where bandwidth density is traded against thermal complexity and crosstalk-induced power penalties.

## 8. Detailed Analysis of Crosstalk Mechanisms

### 8.1. Inter-Channel Crosstalk
Inter-channel crosstalk is the most prevalent form of interference in WDM systems. It arises when the spectral tails of a signal in one wavelength channel overlap with the passband of an adjacent channel's filter.
*   **Filter Roll-off:** The steepness of the filter response (e.g., the Q-factor of an MRR or the grating order of an AWG) determines the rejection ratio. First-order MRR filters often have Lorentzian profiles with slow roll-offs, leading to significant crosstalk unless channel spacing is wide. Higher-order filters (e.g., second-order or third-order coupled rings) have box-like passbands with steeper roll-offs, allowing for tighter channel spacing (e.g., 50 GHz) but at the cost of higher insertion loss and control complexity [cite: 4, 27].
*   **Impact on SNR:** Experimental evaluations have shown that inter-channel crosstalk acts as additive noise. In a system with $N$ channels, the crosstalk accumulates. For large $N$ (e.g., >16), the accumulation of crosstalk from non-adjacent channels can also become significant if the background isolation is poor. Studies indicate that a crosstalk level of -23.8 dB to -26.5 dB per interferer is required to keep the SNR penalty below 1 dB for BERs between $10^{-7}$ and $10^{-13}$ [cite: 23].

### 8.2. Thermal Crosstalk in Integrated Circuits
Thermal crosstalk is unique to integrated photonics and is particularly severe in silicon, which has high thermal conductivity.
*   **Mechanism:** To tune an MRR to a specific wavelength (compensating for fabrication errors), a micro-heater is used. This heater creates a local hotspot. However, heat diffuses laterally, changing the refractive index of neighboring MRRs via the thermo-optic effect ($dn/dT \approx 1.8 \times 10^{-4} K^{-1}$ for Si).
*   **Quantification:** Research has measured that the thermal coupling between devices can be significant even at distances of tens of microns. For example, a heater 70 µm away can still induce a phase shift. Isolation trenches (removing silicon around the device) can reduce this crosstalk and improve thermal response times (e.g., reducing rise/fall times from ~1100 µs to ~430 µs) [cite: 22].
*   **Control Complexity:** Thermal crosstalk couples the control loops of all channels. Tuning Channel 1 affects Channel 2, which requires Channel 2's heater to adjust, which feeds back to Channel 1. This necessitates complex Multi-Input Multi-Output (MIMO) control algorithms or thermal eigenmode decomposition to stabilize the WDM comb, consuming additional power and logic area [cite: 28, 29].

### 8.3. Crosstalk-Induced Power Penalty
The "power penalty" is the standard metric for quantifying the impact of crosstalk. It is defined as the increase in signal power required to maintain a specific Bit Error Rate (BER) in the presence of crosstalk compared to a crosstalk-free baseline.
*   **1 dB Limit:** A common design constraint is to accept a maximum power penalty of 1 dB.
*   **Relationship to Crosstalk:** To maintain a <1 dB penalty, the signal-to-crosstalk ratio (SXR) generally needs to be >20 dB. If the SXR drops to 15 dB, the penalty can rise exponentially, often leading to a BER floor where error-free transmission is impossible regardless of power [cite: 24, 27].
*   **Wavelength Dependence:** Crosstalk is not uniform across all channels. In MCF (Multi-Core Fiber) and WDM systems, crosstalk can exhibit a wavelength dependence (tilt), where channels at the edge of the band suffer up to 3.8 dB more degradation than those in the center [cite: 26].

## 9. Future Directions and Emerging Technologies

To push the extent of WDM further, several emerging technologies are being investigated to overcome current crosstalk and energy limits.

### 9.1. Advanced De-interleaving
To allow for tighter channel spacing without increasing crosstalk, multi-stage de-interleaving architectures are being proposed. By separating odd and even channels into different paths before demultiplexing, the effective channel spacing at the filter stage is doubled. This significantly reduces inter-channel crosstalk and allows for higher spectral efficiency, though it adds insertion loss and footprint [cite: 6].

### 9.2. Athermal Devices
Reducing the reliance on thermal tuning is a key pathway to better energy efficiency and reduced thermal crosstalk. Athermal devices use materials with negative thermo-optic coefficients (like titanium dioxide or polymer claddings) to counteract the positive thermo-optic coefficient of silicon. While this reduces the tuning power budget, it often comes with challenges in fabrication stability and CMOS compatibility.

### 9.3. Space-Division Multiplexing (SDM) + WDM
Combining WDM with Space-Division Multiplexing (using multi-core fibers or multi-mode waveguides) offers a multiplicative expansion of bandwidth. Recent experiments have demonstrated petabit-scale transmission by combining 383 WDM channels with 55 spatial modes [cite: 14]. On-chip, this translates to using multiple parallel waveguides or multi-mode waveguides, though this increases the complexity of coupling and crosstalk management between modes.

### 9.4. Co-Packaged Optics (CPO)
The industry is moving towards Co-Packaged Optics, where the photonic engine is placed on the same substrate as the ASIC. This minimizes the electrical channel length, reducing the power required to drive the optical modulators. CPO relies heavily on dense WDM to maximize the bandwidth escaping the package. The target for CPO is to achieve bandwidth densities >500 Gbps/mm, heavily leveraging the WDM techniques discussed in this report [cite: 15, 30].

## 10. Summary of Quantitative Findings

| Metric | Current State-of-the-Art | Theoretical/Future Limit | Limiting Factor |
| :--- | :--- | :--- | :--- |
| **Channel Count** | 40–64 channels | >100 channels | Crosstalk, Laser Power |
| **Channel Spacing** | 100 GHz | 25–50 GHz | Inter-channel Crosstalk |
| **Data Rate per Channel** | 25–56 Gbps | >112 Gbps | Modulator Bandwidth, SNR |
| **Shoreline Bandwidth Density** | 2–5 Tbps/mm | ~21 Tbps/mm | Thermal Crosstalk, Footprint |
| **Energy Efficiency** | 2–10 pJ/bit | <0.5 pJ/bit | Laser Efficiency, Tuning Power |
| **Crosstalk Suppression** | ~20–30 dB | >35 dB | Filter Order, Fabrication Errors |
| **Max Power Penalty** | <1 dB (Target) | N/A | Signal-to-Crosstalk Ratio |

This table summarizes the "extent" of WDM capabilities as requested. The transition from current state to theoretical limits requires solving the thermal crosstalk issues in dense MRR arrays and improving the wall-plug efficiency of comb laser sources.

**Sources:**
1. [nitrd.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGovzFTnCuOd2G0VKJEa5-3KshvhMqqwpWAT27pOKfv5EkrjEhKJBWQfRNWS9HDqxnmKvhbmni9Yl20e7Jc9Z0JVFY_YlYGwLmy5ktXPdg1nr-H5V1N6n5ErEjKUxQJ0Ch2m0dRhA==)
2. [cadence.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSpB2aTNIBFA63zMLYMXrKo-DvP49aWMx4JyxPwHoi-ilfjlSIfWBVvpH5YEPoD-_4k3CvDvLAZAY9DElO3NtDcHid0Q1NbNIMOIRilOoIbwHf5uGMT-Yr8iQ41SmLGRckCkPJKMOy9iyGF2tKjNgIacL9X8pc01pmq7jdTxv4RmK53jO87v_mNFvshDEzhL05Xat9Wyd4m5igkVMmIApP3jJtQMVJN93wAAcV)
3. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpLaiqtiSTumO_I9-sh4wSgf0ZDfeuSih6ZzJIcpiP1UZEKL6bXQzPPXT__j_oL9g-HVbR6WivmTnTzlYHu_hduLXkPoPQQHoXXnaetPr2Pkj76BTFSfQdnYFWVUeXIDKs)
4. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfQ3WS0ZtqSAWs41PST9YMgjkBf-WpRvIrGwGEGWQJgp1Su87_UR2HwzYBOJaRDlLsCwGAwM0eKMSI3VdTSGDGuDU7HPvUqUhVTcSgnfSuH0afo3Ly-WMmuQkHboPT6PYzw_m_rfDqoFzeTUB5Dc4mOIV6XajjE_AQOKBQT63jwKB3yyrRcJH-K-BO7nFwoxvP_7iB28oVDLiHgxyOhf0M08HhLly6ZQ82ILWjsJ3o2NDt5_0s__qFhnKatszG4vXmQtfJAhmLfFsg0ELm)
5. [tamu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFW5tlsxiDopeO6eJCNcpoY926CDuBZJXwk-vr6A17nfR1U6WH0r3dIcsLBScjoFpjqTSnLp-b9rU-savUkd4VcvEZD1IJ71uR_7zzJUy07FghaAKcby4A3FLK_MTgFGmrmsZw_f_gIm0ydCL9JeH2j6ep-63OttZWyKEL-3lBeBPAlvuO65Dq193Qj_g==)
6. [ulaval.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELyCF_fxuEO0Qihair_X3dVKJybGF8No7Lezz4lrZMU_XtdDNkxn7Woz0GGFBpMUEnXTabcxanwq-xW9p5EOW69qzQja1urF4viBUrILum4kIKeoygN8XBZD8Bg2zl5ogn3VCVBlKhlLvojfmYm-pH8Mjmw9jjSDfk-7LqElOrnlr-xiVxCy8=)
7. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkoUTfuYn1KF8wRmPgyGl5SNHsa9DxPW_HbakdA64g2aQsC4AO8-zFwq_MxO4UWCw70ftdt41Q8IeO0igJCH2wEdiDrrhhOHSuPIF6I7u5clfTNAdthGa7LKIBGSPXa_uzhe4=)
8. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqwjbtY_8aSmrvSR9ZNNkWQ2Y53wS-TPY2Eu-YMeQyK4IMSbGr_m9OPXbCaKokt9pHCUOKvTrkQ_P18h8_3mhqf3VsLkJtAA1LMzcjhQdaetZjxj8NRbyH4niADn62I_wItLh4zbluQa-guevo_yJC)
9. [columbia.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpL0l8Wmyzs9FFmDYSajaagkPhvY2TOcq9DNocOsui3wwwpgGSJwnyiIlc9R2QoN9WxCsi1CxNTWVagYc6soW6MuIlPJJLZqoLlyLYa1R-Gbr6HfLkIdVqIusaVUIF-fBUri1wnPgvNa7gL4JIVATrQjK4w3sxUmAAFP6tJ9LR-ZYGNCBHS6ejUg_QlX7C4T7oVEUNtEPycw==)
10. [energy.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjv7pJO_Z42KtErKO7PFyyRyVDSGPY3F2EUbFaT_njtia59Dm_-KKMwXTTlIPF6PjZmXWlwb33yGpawPWy_7rdWtk9icKpn7orMp4n8JCavhbBfOY1X8xatVGdGyqPi-PMUSdmiIiTtO104bjbX997GQebiV3lSnoicGuN-KYJAR3TkttiNvmlJL9EfMOnebr5D7PhDfnqBzNZ407EGVOzODGJLDy_bgu4fDo361xnon7GtKtNen9A7w==)
11. [exfo.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVMYADLItjLS2cBx94x4fsIWcTCFO_UIm3DezMs3BPWhIt98_y4E9tAkhrs-3GKSp47hCNdRNmhAmps_9eEDkC3__atGyg9eeejrc45t_sD5WalEsxgosmcl6LNDeb0Khx-k8WZ892vZF5B0emHSyOETFItGdqZAJ7b0Z3OE92Rm0rOZA7yANS5LfmBv4ZxQLeViVQyx7bsUDQStOJ7pZiX1VYRFvvIU2ABX5mo0yyG6VSGBxW3PZCNUqx88Hzn_8Lsz32YnQpRnabf-mFjPXutaKtHrE85cyB)
12. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBQot4EoeQM1y7mLFG29uDVImvxkIK7tFXE8LfQoJN6gT8BHore27Ezz6tkVlOuG9cxirI_c-Tiek09M2wGh-froh_NyqvHqFmXv0naPJdldDj9rqxnkzQSLo=)
13. [scribd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyFfZMVhXyjiTL0X8puWvS2pHvIABVnczvT4wWl9-MuDcpZcqL0XzJ1kLnyrD-KPoqJAROVD55ZoQ3yLVmJt2PsAE8kdz_654knquZ9LKCHHZV4Me1OD3pMMRd3yiPi4dgiJb4_sFLi2KstD-a0T8zt2YvXm9y1alrqvula0LyhVFL_UYpCQ==)
14. [theiet.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECouVaNL_qaeSBIXX4dgmUa1dv-pTd82x4E4F9kBy7NEe0ZfGFRGaCMfHWEDIiaddXF0m94kUsvqytvHjA7TmNQpKPZZOvgmy8w__GtRJEzI8d_ziEGyax1U8o32uJiZDUDEGH9iaE2A==)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGT_c9IHc9Ep3bC85hEMQ28QgruSmtd0ZTRCR_Sdj25-weghumrIbqafVF204dR-iyrNvHF_LO4nkyxiJ5k1qIo_YclS-2JPt5k_eM0slgjdjtXs1kpmmujfKiy0nv03oPESsn47rQtNflrNaTx_jgBp7uk4i2mVY2k0wmo6xnPs2TY9ofLtL8r0XEFoyh-MkUf-pI3qgd-3F64FgdG52jKvPZcEF5nF1AfrLWVa-vfLbgLLY2YVgZYmi0KBxIIwQ==)
16. [ayarlabs.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6u_F6J4ssks7El0RXxUjEYqctYUBGbiMPdKIRZgzH07e2wANsm-WpWQE-w1uG4cNMzbkCEql_icDu8PRBnhkjM8iX3fNEB1F2KTl2_NEDucdBcAIBFhWgydWrGno8A6iPcU8nCxrB4WBwbid-0PSV)
17. [techpowerup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_D99HgpUTSKVlkNsGuoGcVjkknDCSsy3c0OSv0MRNt9FnfiWOwPjithWK40m9RoWDJV2aBPCAsr3Di5xN5VdP7tE-MJmSUplkSiPp4CWhA_2GVazW2TXk8od8zdQYIFE=)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGhrqBk-eHyGzj9VJjEc1awRqBldM6ljkQMJ8_UgeJtwOQ_r_1OXPa9NMRrTW0A3GhQWj_JFG3FasimFO667iRVv-doOSd4cmeB4AN6Az-ybnGlL_Qs_ZzHClbWaqvt4rkr3BEbJ9-7jPSUOmlZ_WEwChhWmbiv-m46hsbuu6T9I1LWN86kYKg5RKwxZuGXOncq02SE2qe4naDv4mKAkrZoXxpXlkw5tXcLyRLe_Def6-g7-Mpg6wIFhadc9vmO8Kxxxu2PW7E=)
19. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGFgRdXUb3juaFFiSzIx44y5bf-P8qGQnwK-lkUkq_J54OB7KsmPHut8XTMGQ2FvD9vH3JTYHOXmImxZEG6bWf-_eD1z4BM4Lz7LmKii-w6hQcxBGJxviWbRkt9XI=)
20. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdgjgGnrRiiGW0pCGuG9MHRkz9serH-Zto_cvXqX4NPDuiKst4MJBwpTKeNa5Y1cXhMPaJKpblJvMlBGmnBAFbVRgA6TNFXQW6PIknjH8xbdGo5x96fyg6AA==)
21. [osti.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOJrK0uKnHcv8G8o2UJ112mYWNXZLTaGpRy7hV6YmOanjTzkdo9PNvKTkQ_E68DsDnyH1g2fdCiv1HAVDbsphTC8rxi0j8uWkK9rOFM45yusnBQxyiaY9v8qB_tQL48Jg=)
22. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzmJfDnfBD5X5MH8Ux4RwOJqk-_Gx7uWoz714rglDjsAeB166vyMvPrA1cGt4RKG2N0lBR2BLHgeX95enODTV9ami0e-eXCqxjWsH48gi7DaBmbb0EcfOenUu5tH7Iq4lLZZUteI6RaieJFkYvyAh3pqxs5vFfTml6RfagVhI_N2o_mRnB-NNwXS1UQ4NdobPqzJ7qx1Jpf0SBSOwJZz8=)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoJjndccFOxqgAxTje0wBOuWy5xWjX78fLJkutWvddqSDaEJya7sYPkUxqVJNzjdrpukfy3wFPNMRCVyqx_s-A9IgspkjBvtVEkNwrIjqLU1KRmF2JR2_phbDGQVuvg1jpT7DsN-X4wLh2AdDDbp2nr10JdBJnMgKuVJB0WaQLoSV9uYsouZcxxmhl57W_oL5uXumpGKgBLNj-XCBb4Q14jfgCr4ulDUQ5YIFPBDZpas3-s5YlRkyEpgzrGh_Oq5GuWADA8fDskg7H5Bo=)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsAPE1yUN9HOU5yRK4vNTA6Ue_dj0CHDekDrbWu3sp_Uf_J20AlsLKBawqG1-fn8surfsexyBjnCy8u7EHaseQifv60LsKWkGrbgpdMGlZlnEo8HjxgxIxT_Qnt46lVz_xAy49jpn-16vYJ69bmiT3OXO5sZ9XlWQiyLT_mY-sd6f5Jl3nZv-Msug8uiyrQVGEYKpQgLgeFWDHc7y7iBRJP69aFqC9Ik1m5PtFxFNu7DhgEkRCmEoW4_3GEZcvtCZm4AomFjgUbcmZMjaealoXewsgiQD7VWWrvLW_Qew9)
25. [fiberoptics4sale.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHENGNMqbPlXC0F3ZOI5-GyYThuUPjUYaAJbxkFZ1hGof0x7n4Mml6WkmLVoS28MuCKM_HwSzv_jL6zStndlYK1XTpn1ppmuFDQgA6p6HDdvMvJhVEHyv5d7sPscD87waVxUeIqIq1TlMjDPaKXYqoyYEnnDWHgG_75kaHHFlfmHlshl-VXlQ==)
26. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-ICpiMj8nsrnDEkd537yKk0-ejme04soNJxrxwPKQ2BiyObdC5RIzk0CHmLp9NRM-aQDxbQXnVPfo6n3GEZhWi8xGQe0nOpWS40hkBK0ZMQiaq2nmwTnkIrp3jrrHuKAEKhkPoRXypVn4FJUrQbHqG4J0x5y8ILhpaJgMys3c7lt5Lykk4bcNu3zYTqKA1AbOOszin5ec)
27. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKrg1WD25vaxGyks5kjv1zGRAC6YwOa9RI5mROBgMnSBkATZVTentOlPZCwdyoj__xJUxXhDZ_Pzm6BdOxf8vNURh41XL_YS3vdqDFF27bU7Mw9YUIVtUxfPMwSYxKKjMKbZF5TGJRG1mABPPcDnbOTsta)
28. [nusod.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_ZgwJR1kN5jwnMN_zR0YN-74NE3X-dPb8eZpZhKZiummXKd-FvH6BYlB7bdyo6TCQm_kECezaDi67d9qaxT68_ku3tvA8PEp6J6VdBVRHsMhmMIdHXSblbyKyOtqGVm0CR-6q9XTVbrdzl7_8QS14gj9OwvnH5zRL)
29. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKNnWh8JX1fgK-XITcgfzTNgjxr-Zgjj9ZBCn7567-Afx7wYNGZphrss4RUKVFna1-LD4oQY9gKtuO9N2R09YygRN3LISTHekTNSTC6KO9zGPL-e4kww==)
30. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQFPk8Q8vLCAnUuau_dYFr--Car0QJH8xM6HuWz4waFFIJntC4fXcZ_uUsiUzSg33loIOsCOvju-6chbJjhkIZIjeLFHw0Gp-IqFL4QFaKf8hqGcXoQIPNoWUjqKFHOB820FpxsfFreu5jk16-zVIZcvtD)


## Annotations
Annotation(end_index=2506, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGovzFTnCuOd2G0VKJEa5-3KshvhMqqwpWAT27pOKfv5EkrjEhKJBWQfRNWS9HDqxnmKvhbmni9Yl20e7Jc9Z0JVFY_YlYGwLmy5ktXPdg1nr-H5V1N6n5ErEjKUxQJ0Ch2m0dRhA==', start_index=2497)
Annotation(end_index=2930, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpLaiqtiSTumO_I9-sh4wSgf0ZDfeuSih6ZzJIcpiP1UZEKL6bXQzPPXT__j_oL9g-HVbR6WivmTnTzlYHu_hduLXkPoPQQHoXXnaetPr2Pkj76BTFSfQdnYFWVUeXIDKs', start_index=2918)
Annotation(end_index=2930, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSpB2aTNIBFA63zMLYMXrKo-DvP49aWMx4JyxPwHoi-ilfjlSIfWBVvpH5YEPoD-_4k3CvDvLAZAY9DElO3NtDcHid0Q1NbNIMOIRilOoIbwHf5uGMT-Yr8iQ41SmLGRckCkPJKMOy9iyGF2tKjNgIacL9X8pc01pmq7jdTxv4RmK53jO87v_mNFvshDEzhL05Xat9Wyd4m5igkVMmIApP3jJtQMVJN93wAAcV', start_index=2918)
Annotation(end_index=4170, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFW5tlsxiDopeO6eJCNcpoY926CDuBZJXwk-vr6A17nfR1U6WH0r3dIcsLBScjoFpjqTSnLp-b9rU-savUkd4VcvEZD1IJ71uR_7zzJUy07FghaAKcby4A3FLK_MTgFGmrmsZw_f_gIm0ydCL9JeH2j6ep-63OttZWyKEL-3lBeBPAlvuO65Dq193Qj_g==', start_index=4158)
Annotation(end_index=4170, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfQ3WS0ZtqSAWs41PST9YMgjkBf-WpRvIrGwGEGWQJgp1Su87_UR2HwzYBOJaRDlLsCwGAwM0eKMSI3VdTSGDGuDU7HPvUqUhVTcSgnfSuH0afo3Ly-WMmuQkHboPT6PYzw_m_rfDqoFzeTUB5Dc4mOIV6XajjE_AQOKBQT63jwKB3yyrRcJH-K-BO7nFwoxvP_7iB28oVDLiHgxyOhf0M08HhLly6ZQ82ILWjsJ3o2NDt5_0s__qFhnKatszG4vXmQtfJAhmLfFsg0ELm', start_index=4158)
Annotation(end_index=4752, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELyCF_fxuEO0Qihair_X3dVKJybGF8No7Lezz4lrZMU_XtdDNkxn7Woz0GGFBpMUEnXTabcxanwq-xW9p5EOW69qzQja1urF4viBUrILum4kIKeoygN8XBZD8Bg2zl5ogn3VCVBlKhlLvojfmYm-pH8Mjmw9jjSDfk-7LqElOrnlr-xiVxCy8=', start_index=4740)
Annotation(end_index=4752, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkoUTfuYn1KF8wRmPgyGl5SNHsa9DxPW_HbakdA64g2aQsC4AO8-zFwq_MxO4UWCw70ftdt41Q8IeO0igJCH2wEdiDrrhhOHSuPIF6I7u5clfTNAdthGa7LKIBGSPXa_uzhe4=', start_index=4740)
Annotation(end_index=5279, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkoUTfuYn1KF8wRmPgyGl5SNHsa9DxPW_HbakdA64g2aQsC4AO8-zFwq_MxO4UWCw70ftdt41Q8IeO0igJCH2wEdiDrrhhOHSuPIF6I7u5clfTNAdthGa7LKIBGSPXa_uzhe4=', start_index=5270)
Annotation(end_index=5947, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqwjbtY_8aSmrvSR9ZNNkWQ2Y53wS-TPY2Eu-YMeQyK4IMSbGr_m9OPXbCaKokt9pHCUOKvTrkQ_P18h8_3mhqf3VsLkJtAA1LMzcjhQdaetZjxj8NRbyH4niADn62I_wItLh4zbluQa-guevo_yJC', start_index=5938)
Annotation(end_index=6109, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGovzFTnCuOd2G0VKJEa5-3KshvhMqqwpWAT27pOKfv5EkrjEhKJBWQfRNWS9HDqxnmKvhbmni9Yl20e7Jc9Z0JVFY_YlYGwLmy5ktXPdg1nr-H5V1N6n5ErEjKUxQJ0Ch2m0dRhA==', start_index=6100)
Annotation(end_index=6642, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpL0l8Wmyzs9FFmDYSajaagkPhvY2TOcq9DNocOsui3wwwpgGSJwnyiIlc9R2QoN9WxCsi1CxNTWVagYc6soW6MuIlPJJLZqoLlyLYa1R-Gbr6HfLkIdVqIusaVUIF-fBUri1wnPgvNa7gL4JIVATrQjK4w3sxUmAAFP6tJ9LR-ZYGNCBHS6ejUg_QlX7C4T7oVEUNtEPycw==', start_index=6633)
Annotation(end_index=6711, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVMYADLItjLS2cBx94x4fsIWcTCFO_UIm3DezMs3BPWhIt98_y4E9tAkhrs-3GKSp47hCNdRNmhAmps_9eEDkC3__atGyg9eeejrc45t_sD5WalEsxgosmcl6LNDeb0Khx-k8WZ892vZF5B0emHSyOETFItGdqZAJ7b0Z3OE92Rm0rOZA7yANS5LfmBv4ZxQLeViVQyx7bsUDQStOJ7pZiX1VYRFvvIU2ABX5mo0yyG6VSGBxW3PZCNUqx88Hzn_8Lsz32YnQpRnabf-mFjPXutaKtHrE85cyB', start_index=6697)
Annotation(end_index=6711, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjv7pJO_Z42KtErKO7PFyyRyVDSGPY3F2EUbFaT_njtia59Dm_-KKMwXTTlIPF6PjZmXWlwb33yGpawPWy_7rdWtk9icKpn7orMp4n8JCavhbBfOY1X8xatVGdGyqPi-PMUSdmiIiTtO104bjbX997GQebiV3lSnoicGuN-KYJAR3TkttiNvmlJL9EfMOnebr5D7PhDfnqBzNZ407EGVOzODGJLDy_bgu4fDo361xnon7GtKtNen9A7w==', start_index=6697)
Annotation(end_index=6918, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBQot4EoeQM1y7mLFG29uDVImvxkIK7tFXE8LfQoJN6gT8BHore27Ezz6tkVlOuG9cxirI_c-Tiek09M2wGh-froh_NyqvHqFmXv0naPJdldDj9rqxnkzQSLo=', start_index=6905)
Annotation(end_index=6918, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGovzFTnCuOd2G0VKJEa5-3KshvhMqqwpWAT27pOKfv5EkrjEhKJBWQfRNWS9HDqxnmKvhbmni9Yl20e7Jc9Z0JVFY_YlYGwLmy5ktXPdg1nr-H5V1N6n5ErEjKUxQJ0Ch2m0dRhA==', start_index=6905)
Annotation(end_index=7091, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyFfZMVhXyjiTL0X8puWvS2pHvIABVnczvT4wWl9-MuDcpZcqL0XzJ1kLnyrD-KPoqJAROVD55ZoQ3yLVmJt2PsAE8kdz_654knquZ9LKCHHZV4Me1OD3pMMRd3yiPi4dgiJb4_sFLi2KstD-a0T8zt2YvXm9y1alrqvula0LyhVFL_UYpCQ==', start_index=7077)
Annotation(end_index=7091, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBQot4EoeQM1y7mLFG29uDVImvxkIK7tFXE8LfQoJN6gT8BHore27Ezz6tkVlOuG9cxirI_c-Tiek09M2wGh-froh_NyqvHqFmXv0naPJdldDj9rqxnkzQSLo=', start_index=7077)
Annotation(end_index=7313, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECouVaNL_qaeSBIXX4dgmUa1dv-pTd82x4E4F9kBy7NEe0ZfGFRGaCMfHWEDIiaddXF0m94kUsvqytvHjA7TmNQpKPZZOvgmy8w__GtRJEzI8d_ziEGyax1U8o32uJiZDUDEGH9iaE2A==', start_index=7303)
Annotation(end_index=7438, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELyCF_fxuEO0Qihair_X3dVKJybGF8No7Lezz4lrZMU_XtdDNkxn7Woz0GGFBpMUEnXTabcxanwq-xW9p5EOW69qzQja1urF4viBUrILum4kIKeoygN8XBZD8Bg2zl5ogn3VCVBlKhlLvojfmYm-pH8Mjmw9jjSDfk-7LqElOrnlr-xiVxCy8=', start_index=7426)
Annotation(end_index=7438, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkoUTfuYn1KF8wRmPgyGl5SNHsa9DxPW_HbakdA64g2aQsC4AO8-zFwq_MxO4UWCw70ftdt41Q8IeO0igJCH2wEdiDrrhhOHSuPIF6I7u5clfTNAdthGa7LKIBGSPXa_uzhe4=', start_index=7426)
Annotation(end_index=7829, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGT_c9IHc9Ep3bC85hEMQ28QgruSmtd0ZTRCR_Sdj25-weghumrIbqafVF204dR-iyrNvHF_LO4nkyxiJ5k1qIo_YclS-2JPt5k_eM0slgjdjtXs1kpmmujfKiy0nv03oPESsn47rQtNflrNaTx_jgBp7uk4i2mVY2k0wmo6xnPs2TY9ofLtL8r0XEFoyh-MkUf-pI3qgd-3F64FgdG52jKvPZcEF5nF1AfrLWVa-vfLbgLLY2YVgZYmi0KBxIIwQ==', start_index=7819)
Annotation(end_index=8017, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpL0l8Wmyzs9FFmDYSajaagkPhvY2TOcq9DNocOsui3wwwpgGSJwnyiIlc9R2QoN9WxCsi1CxNTWVagYc6soW6MuIlPJJLZqoLlyLYa1R-Gbr6HfLkIdVqIusaVUIF-fBUri1wnPgvNa7gL4JIVATrQjK4w3sxUmAAFP6tJ9LR-ZYGNCBHS6ejUg_QlX7C4T7oVEUNtEPycw==', start_index=8000)
Annotation(end_index=8017, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_D99HgpUTSKVlkNsGuoGcVjkknDCSsy3c0OSv0MRNt9FnfiWOwPjithWK40m9RoWDJV2aBPCAsr3Di5xN5VdP7tE-MJmSUplkSiPp4CWhA_2GVazW2TXk8od8zdQYIFE=', start_index=8000)
Annotation(end_index=8017, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6u_F6J4ssks7El0RXxUjEYqctYUBGbiMPdKIRZgzH07e2wANsm-WpWQE-w1uG4cNMzbkCEql_icDu8PRBnhkjM8iX3fNEB1F2KTl2_NEDucdBcAIBFhWgydWrGno8A6iPcU8nCxrB4WBwbid-0PSV', start_index=8000)
Annotation(end_index=8185, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELyCF_fxuEO0Qihair_X3dVKJybGF8No7Lezz4lrZMU_XtdDNkxn7Woz0GGFBpMUEnXTabcxanwq-xW9p5EOW69qzQja1urF4viBUrILum4kIKeoygN8XBZD8Bg2zl5ogn3VCVBlKhlLvojfmYm-pH8Mjmw9jjSDfk-7LqElOrnlr-xiVxCy8=', start_index=8173)
Annotation(end_index=8185, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkoUTfuYn1KF8wRmPgyGl5SNHsa9DxPW_HbakdA64g2aQsC4AO8-zFwq_MxO4UWCw70ftdt41Q8IeO0igJCH2wEdiDrrhhOHSuPIF6I7u5clfTNAdthGa7LKIBGSPXa_uzhe4=', start_index=8173)
Annotation(end_index=8692, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGovzFTnCuOd2G0VKJEa5-3KshvhMqqwpWAT27pOKfv5EkrjEhKJBWQfRNWS9HDqxnmKvhbmni9Yl20e7Jc9Z0JVFY_YlYGwLmy5ktXPdg1nr-H5V1N6n5ErEjKUxQJ0Ch2m0dRhA==', start_index=8683)
Annotation(end_index=9094, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGhrqBk-eHyGzj9VJjEc1awRqBldM6ljkQMJ8_UgeJtwOQ_r_1OXPa9NMRrTW0A3GhQWj_JFG3FasimFO667iRVv-doOSd4cmeB4AN6Az-ybnGlL_Qs_ZzHClbWaqvt4rkr3BEbJ9-7jPSUOmlZ_WEwChhWmbiv-m46hsbuu6T9I1LWN86kYKg5RKwxZuGXOncq02SE2qe4naDv4mKAkrZoXxpXlkw5tXcLyRLe_Def6-g7-Mpg6wIFhadc9vmO8Kxxxu2PW7E=', start_index=9080)
Annotation(end_index=9094, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGFgRdXUb3juaFFiSzIx44y5bf-P8qGQnwK-lkUkq_J54OB7KsmPHut8XTMGQ2FvD9vH3JTYHOXmImxZEG6bWf-_eD1z4BM4Lz7LmKii-w6hQcxBGJxviWbRkt9XI=', start_index=9080)
Annotation(end_index=9324, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGovzFTnCuOd2G0VKJEa5-3KshvhMqqwpWAT27pOKfv5EkrjEhKJBWQfRNWS9HDqxnmKvhbmni9Yl20e7Jc9Z0JVFY_YlYGwLmy5ktXPdg1nr-H5V1N6n5ErEjKUxQJ0Ch2m0dRhA==', start_index=9315)
Annotation(end_index=9456, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdgjgGnrRiiGW0pCGuG9MHRkz9serH-Zto_cvXqX4NPDuiKst4MJBwpTKeNa5Y1cXhMPaJKpblJvMlBGmnBAFbVRgA6TNFXQW6PIknjH8xbdGo5x96fyg6AA==', start_index=9446)
Annotation(end_index=9902, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGovzFTnCuOd2G0VKJEa5-3KshvhMqqwpWAT27pOKfv5EkrjEhKJBWQfRNWS9HDqxnmKvhbmni9Yl20e7Jc9Z0JVFY_YlYGwLmy5ktXPdg1nr-H5V1N6n5ErEjKUxQJ0Ch2m0dRhA==', start_index=9890)
Annotation(end_index=9902, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqwjbtY_8aSmrvSR9ZNNkWQ2Y53wS-TPY2Eu-YMeQyK4IMSbGr_m9OPXbCaKokt9pHCUOKvTrkQ_P18h8_3mhqf3VsLkJtAA1LMzcjhQdaetZjxj8NRbyH4niADn62I_wItLh4zbluQa-guevo_yJC', start_index=9890)
Annotation(end_index=10114, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGhrqBk-eHyGzj9VJjEc1awRqBldM6ljkQMJ8_UgeJtwOQ_r_1OXPa9NMRrTW0A3GhQWj_JFG3FasimFO667iRVv-doOSd4cmeB4AN6Az-ybnGlL_Qs_ZzHClbWaqvt4rkr3BEbJ9-7jPSUOmlZ_WEwChhWmbiv-m46hsbuu6T9I1LWN86kYKg5RKwxZuGXOncq02SE2qe4naDv4mKAkrZoXxpXlkw5tXcLyRLe_Def6-g7-Mpg6wIFhadc9vmO8Kxxxu2PW7E=', start_index=10104)
Annotation(end_index=10976, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSpB2aTNIBFA63zMLYMXrKo-DvP49aWMx4JyxPwHoi-ilfjlSIfWBVvpH5YEPoD-_4k3CvDvLAZAY9DElO3NtDcHid0Q1NbNIMOIRilOoIbwHf5uGMT-Yr8iQ41SmLGRckCkPJKMOy9iyGF2tKjNgIacL9X8pc01pmq7jdTxv4RmK53jO87v_mNFvshDEzhL05Xat9Wyd4m5igkVMmIApP3jJtQMVJN93wAAcV', start_index=10967)
Annotation(end_index=11288, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSpB2aTNIBFA63zMLYMXrKo-DvP49aWMx4JyxPwHoi-ilfjlSIfWBVvpH5YEPoD-_4k3CvDvLAZAY9DElO3NtDcHid0Q1NbNIMOIRilOoIbwHf5uGMT-Yr8iQ41SmLGRckCkPJKMOy9iyGF2tKjNgIacL9X8pc01pmq7jdTxv4RmK53jO87v_mNFvshDEzhL05Xat9Wyd4m5igkVMmIApP3jJtQMVJN93wAAcV', start_index=11279)
Annotation(end_index=11507, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOJrK0uKnHcv8G8o2UJ112mYWNXZLTaGpRy7hV6YmOanjTzkdo9PNvKTkQ_E68DsDnyH1g2fdCiv1HAVDbsphTC8rxi0j8uWkK9rOFM45yusnBQxyiaY9v8qB_tQL48Jg=', start_index=11493)
Annotation(end_index=11507, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzmJfDnfBD5X5MH8Ux4RwOJqk-_Gx7uWoz714rglDjsAeB166vyMvPrA1cGt4RKG2N0lBR2BLHgeX95enODTV9ami0e-eXCqxjWsH48gi7DaBmbb0EcfOenUu5tH7Iq4lLZZUteI6RaieJFkYvyAh3pqxs5vFfTml6RfagVhI_N2o_mRnB-NNwXS1UQ4NdobPqzJ7qx1Jpf0SBSOwJZz8=', start_index=11493)
Annotation(end_index=11800, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVMYADLItjLS2cBx94x4fsIWcTCFO_UIm3DezMs3BPWhIt98_y4E9tAkhrs-3GKSp47hCNdRNmhAmps_9eEDkC3__atGyg9eeejrc45t_sD5WalEsxgosmcl6LNDeb0Khx-k8WZ892vZF5B0emHSyOETFItGdqZAJ7b0Z3OE92Rm0rOZA7yANS5LfmBv4ZxQLeViVQyx7bsUDQStOJ7pZiX1VYRFvvIU2ABX5mo0yyG6VSGBxW3PZCNUqx88Hzn_8Lsz32YnQpRnabf-mFjPXutaKtHrE85cyB', start_index=11787)
Annotation(end_index=11800, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFW5tlsxiDopeO6eJCNcpoY926CDuBZJXwk-vr6A17nfR1U6WH0r3dIcsLBScjoFpjqTSnLp-b9rU-savUkd4VcvEZD1IJ71uR_7zzJUy07FghaAKcby4A3FLK_MTgFGmrmsZw_f_gIm0ydCL9JeH2j6ep-63OttZWyKEL-3lBeBPAlvuO65Dq193Qj_g==', start_index=11787)
Annotation(end_index=12037, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoJjndccFOxqgAxTje0wBOuWy5xWjX78fLJkutWvddqSDaEJya7sYPkUxqVJNzjdrpukfy3wFPNMRCVyqx_s-A9IgspkjBvtVEkNwrIjqLU1KRmF2JR2_phbDGQVuvg1jpT7DsN-X4wLh2AdDDbp2nr10JdBJnMgKuVJB0WaQLoSV9uYsouZcxxmhl57W_oL5uXumpGKgBLNj-XCBb4Q14jfgCr4ulDUQ5YIFPBDZpas3-s5YlRkyEpgzrGh_Oq5GuWADA8fDskg7H5Bo=', start_index=12023)
Annotation(end_index=12037, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsAPE1yUN9HOU5yRK4vNTA6Ue_dj0CHDekDrbWu3sp_Uf_J20AlsLKBawqG1-fn8surfsexyBjnCy8u7EHaseQifv60LsKWkGrbgpdMGlZlnEo8HjxgxIxT_Qnt46lVz_xAy49jpn-16vYJ69bmiT3OXO5sZ9XlWQiyLT_mY-sd6f5Jl3nZv-Msug8uiyrQVGEYKpQgLgeFWDHc7y7iBRJP69aFqC9Ik1m5PtFxFNu7DhgEkRCmEoW4_3GEZcvtCZm4AomFjgUbcmZMjaealoXewsgiQD7VWWrvLW_Qew9', start_index=12023)
Annotation(end_index=12529, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHENGNMqbPlXC0F3ZOI5-GyYThuUPjUYaAJbxkFZ1hGof0x7n4Mml6WkmLVoS28MuCKM_HwSzv_jL6zStndlYK1XTpn1ppmuFDQgA6p6HDdvMvJhVEHyv5d7sPscD87waVxUeIqIq1TlMjDPaKXYqoyYEnnDWHgG_75kaHHFlfmHlshl-VXlQ==', start_index=12519)
Annotation(end_index=13074, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzmJfDnfBD5X5MH8Ux4RwOJqk-_Gx7uWoz714rglDjsAeB166vyMvPrA1cGt4RKG2N0lBR2BLHgeX95enODTV9ami0e-eXCqxjWsH48gi7DaBmbb0EcfOenUu5tH7Iq4lLZZUteI6RaieJFkYvyAh3pqxs5vFfTml6RfagVhI_N2o_mRnB-NNwXS1UQ4NdobPqzJ7qx1Jpf0SBSOwJZz8=', start_index=13064)
Annotation(end_index=13265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGhrqBk-eHyGzj9VJjEc1awRqBldM6ljkQMJ8_UgeJtwOQ_r_1OXPa9NMRrTW0A3GhQWj_JFG3FasimFO667iRVv-doOSd4cmeB4AN6Az-ybnGlL_Qs_ZzHClbWaqvt4rkr3BEbJ9-7jPSUOmlZ_WEwChhWmbiv-m46hsbuu6T9I1LWN86kYKg5RKwxZuGXOncq02SE2qe4naDv4mKAkrZoXxpXlkw5tXcLyRLe_Def6-g7-Mpg6wIFhadc9vmO8Kxxxu2PW7E=', start_index=13255)
Annotation(end_index=13580, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-ICpiMj8nsrnDEkd537yKk0-ejme04soNJxrxwPKQ2BiyObdC5RIzk0CHmLp9NRM-aQDxbQXnVPfo6n3GEZhWi8xGQe0nOpWS40hkBK0ZMQiaq2nmwTnkIrp3jrrHuKAEKhkPoRXypVn4FJUrQbHqG4J0x5y8ILhpaJgMys3c7lt5Lykk4bcNu3zYTqKA1AbOOszin5ec', start_index=13570)
Annotation(end_index=14006, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELyCF_fxuEO0Qihair_X3dVKJybGF8No7Lezz4lrZMU_XtdDNkxn7Woz0GGFBpMUEnXTabcxanwq-xW9p5EOW69qzQja1urF4viBUrILum4kIKeoygN8XBZD8Bg2zl5ogn3VCVBlKhlLvojfmYm-pH8Mjmw9jjSDfk-7LqElOrnlr-xiVxCy8=', start_index=13994)
Annotation(end_index=14006, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkoUTfuYn1KF8wRmPgyGl5SNHsa9DxPW_HbakdA64g2aQsC4AO8-zFwq_MxO4UWCw70ftdt41Q8IeO0igJCH2wEdiDrrhhOHSuPIF6I7u5clfTNAdthGa7LKIBGSPXa_uzhe4=', start_index=13994)
Annotation(end_index=14292, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELyCF_fxuEO0Qihair_X3dVKJybGF8No7Lezz4lrZMU_XtdDNkxn7Woz0GGFBpMUEnXTabcxanwq-xW9p5EOW69qzQja1urF4viBUrILum4kIKeoygN8XBZD8Bg2zl5ogn3VCVBlKhlLvojfmYm-pH8Mjmw9jjSDfk-7LqElOrnlr-xiVxCy8=', start_index=14280)
Annotation(end_index=14292, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkoUTfuYn1KF8wRmPgyGl5SNHsa9DxPW_HbakdA64g2aQsC4AO8-zFwq_MxO4UWCw70ftdt41Q8IeO0igJCH2wEdiDrrhhOHSuPIF6I7u5clfTNAdthGa7LKIBGSPXa_uzhe4=', start_index=14280)
Annotation(end_index=14838, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpL0l8Wmyzs9FFmDYSajaagkPhvY2TOcq9DNocOsui3wwwpgGSJwnyiIlc9R2QoN9WxCsi1CxNTWVagYc6soW6MuIlPJJLZqoLlyLYa1R-Gbr6HfLkIdVqIusaVUIF-fBUri1wnPgvNa7gL4JIVATrQjK4w3sxUmAAFP6tJ9LR-ZYGNCBHS6ejUg_QlX7C4T7oVEUNtEPycw==', start_index=14826)
Annotation(end_index=14838, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFW5tlsxiDopeO6eJCNcpoY926CDuBZJXwk-vr6A17nfR1U6WH0r3dIcsLBScjoFpjqTSnLp-b9rU-savUkd4VcvEZD1IJ71uR_7zzJUy07FghaAKcby4A3FLK_MTgFGmrmsZw_f_gIm0ydCL9JeH2j6ep-63OttZWyKEL-3lBeBPAlvuO65Dq193Qj_g==', start_index=14826)
Annotation(end_index=17215, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKrg1WD25vaxGyks5kjv1zGRAC6YwOa9RI5mROBgMnSBkATZVTentOlPZCwdyoj__xJUxXhDZ_Pzm6BdOxf8vNURh41XL_YS3vdqDFF27bU7Mw9YUIVtUxfPMwSYxKKjMKbZF5TGJRG1mABPPcDnbOTsta', start_index=17202)
Annotation(end_index=17215, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfQ3WS0ZtqSAWs41PST9YMgjkBf-WpRvIrGwGEGWQJgp1Su87_UR2HwzYBOJaRDlLsCwGAwM0eKMSI3VdTSGDGuDU7HPvUqUhVTcSgnfSuH0afo3Ly-WMmuQkHboPT6PYzw_m_rfDqoFzeTUB5Dc4mOIV6XajjE_AQOKBQT63jwKB3yyrRcJH-K-BO7nFwoxvP_7iB28oVDLiHgxyOhf0M08HhLly6ZQ82ILWjsJ3o2NDt5_0s__qFhnKatszG4vXmQtfJAhmLfFsg0ELm', start_index=17202)
Annotation(end_index=17714, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoJjndccFOxqgAxTje0wBOuWy5xWjX78fLJkutWvddqSDaEJya7sYPkUxqVJNzjdrpukfy3wFPNMRCVyqx_s-A9IgspkjBvtVEkNwrIjqLU1KRmF2JR2_phbDGQVuvg1jpT7DsN-X4wLh2AdDDbp2nr10JdBJnMgKuVJB0WaQLoSV9uYsouZcxxmhl57W_oL5uXumpGKgBLNj-XCBb4Q14jfgCr4ulDUQ5YIFPBDZpas3-s5YlRkyEpgzrGh_Oq5GuWADA8fDskg7H5Bo=', start_index=17704)
Annotation(end_index=18616, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzmJfDnfBD5X5MH8Ux4RwOJqk-_Gx7uWoz714rglDjsAeB166vyMvPrA1cGt4RKG2N0lBR2BLHgeX95enODTV9ami0e-eXCqxjWsH48gi7DaBmbb0EcfOenUu5tH7Iq4lLZZUteI6RaieJFkYvyAh3pqxs5vFfTml6RfagVhI_N2o_mRnB-NNwXS1UQ4NdobPqzJ7qx1Jpf0SBSOwJZz8=', start_index=18606)
Annotation(end_index=19014, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKNnWh8JX1fgK-XITcgfzTNgjxr-Zgjj9ZBCn7567-Afx7wYNGZphrss4RUKVFna1-LD4oQY9gKtuO9N2R09YygRN3LISTHekTNSTC6KO9zGPL-e4kww==', start_index=19000)
Annotation(end_index=19014, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_ZgwJR1kN5jwnMN_zR0YN-74NE3X-dPb8eZpZhKZiummXKd-FvH6BYlB7bdyo6TCQm_kECezaDi67d9qaxT68_ku3tvA8PEp6J6VdBVRHsMhmMIdHXSblbyKyOtqGVm0CR-6q9XTVbrdzl7_8QS14gj9OwvnH5zRL', start_index=19000)
Annotation(end_index=19702, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsAPE1yUN9HOU5yRK4vNTA6Ue_dj0CHDekDrbWu3sp_Uf_J20AlsLKBawqG1-fn8surfsexyBjnCy8u7EHaseQifv60LsKWkGrbgpdMGlZlnEo8HjxgxIxT_Qnt46lVz_xAy49jpn-16vYJ69bmiT3OXO5sZ9XlWQiyLT_mY-sd6f5Jl3nZv-Msug8uiyrQVGEYKpQgLgeFWDHc7y7iBRJP69aFqC9Ik1m5PtFxFNu7DhgEkRCmEoW4_3GEZcvtCZm4AomFjgUbcmZMjaealoXewsgiQD7VWWrvLW_Qew9', start_index=19688)
Annotation(end_index=19702, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKrg1WD25vaxGyks5kjv1zGRAC6YwOa9RI5mROBgMnSBkATZVTentOlPZCwdyoj__xJUxXhDZ_Pzm6BdOxf8vNURh41XL_YS3vdqDFF27bU7Mw9YUIVtUxfPMwSYxKKjMKbZF5TGJRG1mABPPcDnbOTsta', start_index=19688)
Annotation(end_index=19989, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-ICpiMj8nsrnDEkd537yKk0-ejme04soNJxrxwPKQ2BiyObdC5RIzk0CHmLp9NRM-aQDxbQXnVPfo6n3GEZhWi8xGQe0nOpWS40hkBK0ZMQiaq2nmwTnkIrp3jrrHuKAEKhkPoRXypVn4FJUrQbHqG4J0x5y8ILhpaJgMys3c7lt5Lykk4bcNu3zYTqKA1AbOOszin5ec', start_index=19979)
Annotation(end_index=20633, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELyCF_fxuEO0Qihair_X3dVKJybGF8No7Lezz4lrZMU_XtdDNkxn7Woz0GGFBpMUEnXTabcxanwq-xW9p5EOW69qzQja1urF4viBUrILum4kIKeoygN8XBZD8Bg2zl5ogn3VCVBlKhlLvojfmYm-pH8Mjmw9jjSDfk-7LqElOrnlr-xiVxCy8=', start_index=20624)
Annotation(end_index=21404, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECouVaNL_qaeSBIXX4dgmUa1dv-pTd82x4E4F9kBy7NEe0ZfGFRGaCMfHWEDIiaddXF0m94kUsvqytvHjA7TmNQpKPZZOvgmy8w__GtRJEzI8d_ziEGyax1U8o32uJiZDUDEGH9iaE2A==', start_index=21394)
Annotation(end_index=22072, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQFPk8Q8vLCAnUuau_dYFr--Car0QJH8xM6HuWz4waFFIJntC4fXcZ_uUsiUzSg33loIOsCOvju-6chbJjhkIZIjeLFHw0Gp-IqFL4QFaKf8hqGcXoQIPNoWUjqKFHOB820FpxsfFreu5jk16-zVIZcvtD', start_index=22058)
Annotation(end_index=22072, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGT_c9IHc9Ep3bC85hEMQ28QgruSmtd0ZTRCR_Sdj25-weghumrIbqafVF204dR-iyrNvHF_LO4nkyxiJ5k1qIo_YclS-2JPt5k_eM0slgjdjtXs1kpmmujfKiy0nv03oPESsn47rQtNflrNaTx_jgBp7uk4i2mVY2k0wmo6xnPs2TY9ofLtL8r0XEFoyh-MkUf-pI3qgd-3F64FgdG52jKvPZcEF5nF1AfrLWVa-vfLbgLLY2YVgZYmi0KBxIIwQ==', start_index=22058)

## Sources
