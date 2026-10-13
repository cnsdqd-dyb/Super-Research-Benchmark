# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 167da8ec | **Time:** 360.50s | **Cost:** $1.25818
--------------------------------------------------------------------------------

# Balancing Measurement Precision and Environmental Isolation in Quantum Gravity Experiments

### Key Points
*   **The Central Paradox:** Quantum gravity experiments face a fundamental conflict: detecting gravitational coupling requires macroscopic masses (to generate measurable fields), but macroscopic masses are extremely susceptible to environmental decoherence, which destroys the quantum states (superposition or entanglement) necessary to prove the non-classical nature of gravity.
*   **The "Feasibility Wedge":** Successful experimental protocols must operate within a narrow parameter space—often termed the "feasibility wedge"—bounded by the decoherence rate on one side and the required interaction time for gravitational entanglement on the other.
*   **Theoretical Constraints:** Recent theoretical frameworks, such as the decoherence-diffusion trade-off, suggest that if gravity is fundamentally classical, it must induce a specific rate of diffusion in phase space to maintain consistency with quantum matter. This provides a testable signature: experiments must balance high precision (to detect diffusion) with long coherence times (to rule out collapse models).
*   **Technological Frontiers:** Current strategies employ hybrid approaches, including laser-cooled torsional oscillators (bridging the gap between microscopic and macroscopic), squeezed light states (to bypass the Standard Quantum Limit), and frequency-domain atom interferometry (to maximize integration time without requiring large spatial delocalization).

---

## 1. Introduction: The Scale Problem and the Move to the Tabletop

The search for a quantum theory of gravity has traditionally focused on high-energy regimes accessible only to particle accelerators of impossible size or through cosmological observations of the early universe. However, a paradigm shift has occurred towards "tabletop" experiments designed to test the low-energy phenomenological consequences of quantum gravity [cite: 1, 2]. The core premise of these experiments is to observe quantum phenomena—specifically superposition and entanglement—mediated by the gravitational field. If gravity can entangle two quantum systems, it must, according to standard quantum information theoretic arguments, possess quantum features (i.e., it cannot be a purely classical channel) [cite: 3, 4].

The realization of such experiments, however, is hindered by a severe tension between **measurement precision** and **environmental isolation**. Gravity is the weakest fundamental force; to make its effects observable in a laboratory setting, the source masses must be sufficiently large (typically in the range of $10^{-17}$ kg to kilograms) [cite: 5, 6]. Yet, as mass increases, the coupling to the environment—via thermal photons, residual gas collisions, and seismic vibrations—grows exponentially, leading to rapid decoherence [cite: 7, 8]. This report analyzes the theoretical bounds and experimental strategies employed to navigate this trade-off, examining how physicists attempt to isolate macroscopic quantum states while maintaining the sensitivity required to detect the faint signature of quantum gravity.

## 2. The Fundamental Trade-off: Sensitivity vs. Decoherence

The design of any quantum gravity experiment is governed by the competing requirements of gravitational coupling strength and quantum state preservation.

### 2.1 Mass Scaling and Gravitational Coupling
To observe a gravitationally induced phase shift or entanglement, the interaction energy must be large enough to accumulate a detectable phase over the coherence time of the experiment. For a system of two masses $m$ separated by a distance $d$ with a superposition size $\Delta x$, the gravitational phase shift $\Delta \phi$ scales roughly as:
\[ \Delta \phi \sim \frac{G m^2 \tau}{\hbar d} \]
where $\tau$ is the interaction time. To maximize $\Delta \phi$, one must maximize mass $m$ and time $\tau$. However, the decoherence rate $\Gamma$ also scales with mass. For collisional decoherence and blackbody radiation, $\Gamma \propto m^R$ (where $R$ depends on the specific model, often scaling with the physical cross-section or polarizability) [cite: 5, 7].

### 2.2 The Standard Quantum Limit (SQL)
Precision measurement is further bounded by the Standard Quantum Limit (SQL), which arises from the Heisenberg Uncertainty Principle. In optomechanical sensors used to detect gravity, increasing the measurement strength (to reduce shot noise) increases the backaction noise (radiation pressure) on the test mass [cite: 9, 10].
*   **Shot Noise:** Uncertainty in the number of photons detecting the position.
*   **Backaction Noise:** Momentum kicks imparted to the mass by the measuring photons.
Balancing these noise sources defines the SQL. In the context of quantum gravity, where the signal is infinitesimally small, the experiment must often surpass the SQL using techniques like quantum squeezing [cite: 11, 12].

### 2.3 Environmental Decoherence Channels
The "isolation" aspect of the trade-off involves mitigating three primary sources of environmental noise that destroy quantum coherence:
1.  **Thermal Decoherence:** Even in a vacuum, objects interact with blackbody radiation. For macroscopic objects, the emission and absorption of thermal photons carry away positional information, causing localization. This necessitates cryogenic environments, often in the millikelvin range or lower [cite: 5, 13].
2.  **Gas Collisions:** Residual gas molecules in a vacuum chamber collide with the test mass. For a nanoparticle in a superposition, a single collision can resolve the position and collapse the wavefunction. This requires Ultra-High Vacuum (UHV) conditions, typically below $10^{-10}$ mbar [cite: 5, 14].
3.  **Vibrational and Gradient Noise:** Seismic activity and fluctuating gravitational gradients (Newtonian noise) from nearby moving mass (e.g., passing vehicles, atmospheric changes) couple to the test mass. Unlike electromagnetic noise, gravitational noise cannot be shielded, only compensated for or avoided [cite: 15, 16].

## 3. Theoretical Frameworks and Constraints

The balance between precision and isolation is not merely an engineering challenge but is defined by fundamental theoretical constraints regarding the nature of spacetime.

### 3.1 The Decoherence-Diffusion Trade-off
A critical theoretical development is the "decoherence-diffusion trade-off" proposed by Oppenheim et al. This framework posits that if gravity is fundamentally classical (i.e., spacetime geometry is not quantized), it must interact with quantum matter stochastically to preserve the linearity and positivity of quantum mechanics [cite: 17, 18].

This interaction introduces a trade-off:
\[ \Gamma_{dec} \cdot D_{diff} \ge \text{Constant} \]
where $\Gamma_{dec}$ is the decoherence rate of the quantum system induced by gravity, and $D_{diff}$ is the diffusion rate in the classical phase space (metric fluctuations).
*   **Implication:** If one attempts to keep the quantum system highly coherent (low $\Gamma_{dec}$) to observe interference, the theory demands high diffusion ($D_{diff}$) in the gravitational field.
*   **Experimental Signature:** This provides a way to test classical gravity without necessarily observing entanglement. By bounding the decoherence rate (via interferometry) and measuring the diffusion (via precision mass measurements like a Cavendish experiment), one can squeeze the parameter space. If the product of observed decoherence and diffusion drops below the theoretical bound, classical gravity models are ruled out [cite: 19, 20, 21].

### 3.2 The "Feasibility Wedge"
For experiments aiming to detect gravity-induced entanglement (such as the QGEM protocol), the operational parameters form a "feasibility wedge." This is a region in the multi-dimensional parameter space (mass, superposition size, temperature, pressure) where the signal is strong enough to be detected before environmental decoherence destroys it [cite: 22].
*   **Constraints:** The wedge is bounded by the coherence time on one side and the minimum detectable phase on the other.
*   **Fragility:** Research indicates that outside this wedge, ordinary decoherence mechanisms (like collisional damping) dominate. The existence of this wedge implies that "null results" in gravity experiments are only meaningful if the apparatus is proven to operate within these specific sensitivity-isolation bounds [cite: 22].

### 3.3 Gravity-Mediated Decoherence
Some theories suggest that gravity itself is a source of decoherence. The Penrose-Diosi model suggests that a superposition of a massive object collapses because the two spacetime geometries associated with the superposition states are fundamentally unstable [cite: 1, 23].
*   **Testing via Isolation:** To test this, one must isolate the system from *all* other environmental noise. If the wavefunction still collapses at a rate predicted by the mass distribution, it would provide evidence for gravity-induced collapse. This requires distinguishing "fundamental" gravitational decoherence from "technical" environmental noise [cite: 7, 24].

## 4. Experimental Platforms and Strategies

Researchers are employing various physical systems to navigate the precision-isolation trade-off, each with unique advantages and challenges.

### 4.1 Matter-Wave Interferometry with Nanocrystals
This approach involves putting a nanocrystal (mass $\sim 10^{-17}$ kg to $10^{-14}$ kg) into a spatial superposition.
*   **The Strategy:** Use the internal spin of the nanocrystal (e.g., Nitrogen-Vacancy centers in diamond) to generate the spatial superposition via a magnetic field gradient [cite: 14].
*   **Isolation Challenge:** The superposition must be large (microns) to generate a measurable gravitational phase, but large superpositions are hypersensitive to gas collisions and blackbody radiation.
*   **Precision:** The spin coherence time limits the experiment. The "spin-path" entanglement allows the gravitational phase to be read out via spin measurements, which are highly precise [cite: 1, 22].

### 4.2 Levitated Optomechanics
Levitated nanoparticles (silica or diamond) trapped by lasers offer extreme isolation because they have no physical contact with a substrate, eliminating conductive thermal noise [cite: 6, 10].
*   **Cooling:** Active feedback cooling or cavity cooling can bring the center-of-mass motion of the particle to the quantum ground state.
*   **Recent Breakthroughs:** The "QLev4G" project measured the gravitational field of a 90 mg gold sphere, a record for small source masses [cite: 6].
*   **Trade-off:** While isolation is excellent, the mass is often too small to generate significant gravitational entanglement in short times. Increasing mass requires stronger traps, which introduces photon scattering noise (recoil heating) [cite: 25].

### 4.3 Torsional Oscillators
Macroscopic torsional pendulums (centimeter scale) bridge the gap between atomic and macroscopic physics.
*   **The Strategy:** A recent MIT experiment demonstrated laser cooling of a 1-cm torsional oscillator to 10 mK. This system is massive enough to feel gravity strongly but is being pushed into the quantum regime [cite: 26, 27].
*   **Noise Cancellation:** To balance precision with isolation, the team used a "mirrored optical lever." One laser beam reflects off the oscillator, while a reference beam reflects off a stationary mirror. Subtracting the two signals cancels out the laser's own jitter (technical noise), allowing measurement precision below the oscillator's zero-point fluctuation level [cite: 26, 28].
*   **Goal:** The ultimate aim is to reach the quantum ground state for a macroscopic object, enabling tests where two such oscillators interact solely via gravity [cite: 29].

### 4.4 Atom Interferometry and Optical Boxes
Cold atom experiments use clouds of atoms in superposition.
*   **Free Fall vs. Traps:** Traditional fountains (free fall) have limited interaction times (seconds). "Optical box" traps confine atoms in a flat potential, allowing for longer interrogation times (and thus higher sensitivity) without the atoms dispersing [cite: 30, 31].
*   **Frequency Domain Interferometry:** Instead of large spatial separation, some proposals suggest using frequency-domain interferometry with trapped atoms. This reduces the sensitivity to spatial environmental noise (like gradients) while maintaining sensitivity to gravitational effects on the energy levels [cite: 30, 32].

## 5. Precision Measurement Techniques

To overcome the limits imposed by environmental isolation, advanced metrology techniques are employed to enhance the signal-to-noise ratio.

### 5.1 Squeezed States of Light
To bypass the Standard Quantum Limit, experiments utilize squeezed light. In a squeezed state, the uncertainty in one variable (e.g., phase) is reduced below the vacuum limit, at the expense of increased uncertainty in the conjugate variable (e.g., amplitude) [cite: 11, 33].
*   **Application:** In optomechanical gravity searches, phase squeezing improves the readout sensitivity of the test mass position without increasing the photon number (which would increase thermal heating and backaction) [cite: 12].
*   **Filter Cavities:** Advanced setups use filter cavities to rotate the squeezing angle dependent on frequency, optimizing noise reduction across the signal bandwidth [cite: 11, 34].

### 5.2 Coherent Quantum Noise Cancellation (CQNC)
This technique involves engineering the system such that the backaction noise (the disturbance caused by the measurement) is coherently cancelled out by an anti-noise signal.
*   **Mechanism:** By coupling the test mass to an auxiliary system (like a negative-mass oscillator or a specific optical mode), the backaction force can be subtracted from the final signal, effectively creating a "noise-free" subspace for the measurement [cite: 9, 35, 36]. This allows for higher measurement strengths (better precision) without disturbing the isolation of the quantum state.

### 5.3 Frequency Domain Interferometry (FDI)
FDI measures the phase difference between frequency components rather than spatial paths.
*   **Benefit:** It is less susceptible to low-frequency vibrational noise that plagues spatial interferometers. By encoding the gravitational signal into the frequency beat note of trapped atoms or optical fields, the experiment can run for longer integration times, effectively averaging down the environmental noise [cite: 30, 37].

## 6. Environmental Isolation Challenges and Solutions

The "isolation" side of the equation requires pushing vacuum and cryogenic technologies to their limits.

### 6.1 Vacuum and Pressure Constraints
To prevent collisional decoherence for a mass of $10^{-14}$ kg, pressures must be lower than $10^{-15}$ mbar, which is orders of magnitude lower than standard UHV ($10^{-10}$ mbar).
*   **Solution:** Experiments are often designed for cryogenic environments where the vacuum can be improved by cryopumping (freezing out gas molecules).
*   **Simulation Data:** Simulations show that for nanoparticles, coherence times exceed 1 second only under cryogenic UHV conditions. At room temperature, thermal radiation limits coherence to sub-millisecond scales [cite: 5].

### 6.2 Thermal and Blackbody Isolation
Even in a perfect vacuum, the object radiates and absorbs photons.
*   **Internal Temperature:** The internal temperature of the test mass must be lowered. Laser cooling only cools the center-of-mass mode (the "motion"), not the internal phonons (the "heat").
*   **Material Choice:** Using materials with low absorption cross-sections (like high-purity silica or diamond) minimizes coupling to the blackbody background.
*   **Environment:** The entire chamber walls must be cooled to millikelvin temperatures to reduce the photon flux hitting the particle [cite: 3, 5].

### 6.3 Gravity Gradient Noise (GGN)
A unique challenge for gravity experiments is that gravity cannot be screened. A moving elevator or a cloud passing overhead changes the local gravitational field.
*   **Mitigation:** This requires underground facilities (like the Einstein Telescope infrastructure) or active feedforward cancellation using arrays of seismometers and gravimeters to predict and subtract the local GGN [cite: 15, 16].
*   **Space-Based Proposals:** Ultimately, the most sensitive experiments may need to be conducted in space (e.g., MAQRO proposal) to achieve the necessary microgravity and isolation from terrestrial seismic noise [cite: 24, 38].

## 7. Conclusion

The quest to observe quantum gravity in the laboratory is defined by the rigorous balancing act between **measurement precision** and **environmental isolation**. The "feasibility wedge" for these experiments is narrow: masses must be large enough to gravitate but small enough to remain quantum; measurements must be precise enough to see entanglement but gentle enough to avoid backaction.

Current research suggests that no single "magic bullet" exists. Instead, success will likely come from a convergence of technologies: **levitated optomechanics** to isolate masses, **squeezed light** to surpass quantum limits, **cryogenic UHV** environments to suppress decoherence, and **theoretical bounds** (like the Oppenheim trade-off) to guide the experimental design. Whether through the observation of gravity-induced entanglement (QGEM) or the detection of fundamental diffusion in the metric, these experiments represent the frontier of modern physics, attempting to reconcile the smooth geometry of General Relativity with the probabilistic nature of Quantum Mechanics.

### References
[cite: 1, 2] Overview of tabletop quantum gravity and phenomenology.
[cite: 5, 7] Decoherence scaling with mass and environmental challenges.
[cite: 4, 14] QGEM protocol and spin-based interferometry.
[cite: 22] The "feasibility wedge" and parameter space constraints.
[cite: 13, 26] Torsional oscillators and laser cooling.
[cite: 30, 31] Atom interferometry and optical box traps.
[cite: 6, 10] Levitated optomechanics and mass measurements.
[cite: 9, 36] Backaction evasion and noise cancellation.
[cite: 17, 18] Oppenheim's decoherence-diffusion trade-off.
[cite: 11, 33] Squeezed states and quantum noise reduction.
[cite: 25, 28] Heating rates and trap dynamics.

**Sources:**
1. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjVrdolakegFkJY0H9wMb5CNijOeShpcGQePFO7kjmcCP_TW1BZbEJjm4FU1-_sthXprzxmeCkEG3smbGt5u7gr-Hq77p6cnrLTfhHlY30BN9rUnZO)
2. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKs7oOz8uZ3Js3YN6UWoh6amAZEzeGwblBjUszuiBr2deaUo5Tgr8LOAfd4pBaRo0haaXLyTNTpnSN0fWKHC_cZIlZEUkSPbMFio3tzPIBk7AW8ilkPUh5lyu2eoXjQn33GA39I_HQzrBTacPleAuHSgmQ)
3. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFx_UAoz8tZB8qCkhFLOrWr-pIBngTVpMB3fD2i4hweyUkdzbeGPmZ4WAxmQ4p7lVDRQHLBjcUTx7tSUz_pdjX7dUxvB6HlwN7HXjjovaEglQYJk8G94_bGsuw-4Ihe5Gw=)
4. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKWSuL5pyIXDsVyjXPxfD_HJ04WnnSdD4aBtI3Nd7qGVv_HmH7aE1pC-WYZH9B_UZ_8iPNKbu8L0etBXvD0G5mSbfbtOXX4pCN9N8kI-to0oNFt41OMVPnua6k-A==)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmpKlCT744XutcgLoGYOH4CfhJV7QCmYwDa1M9w4F_sXb40W3_FVMk3MVWKbsudrp7kQl__M9xYyexuwV-bC_-3KHKwmc2QY69AIGuGO_MLp-hZ_GvWL8WGyR03ab6ObZ8pKUnOiK4W940Of2QqXcnGk09pmpEQhjTs4Qq2zHiNUMH0bjp9cJl8tEmw71HPYmnxHmV6Oi_GbLf3RzYCNWXOX9MsbxYBqBo5Dedvp9X4H1HKrnd9Xpam8jelh8N_A==)
6. [europa.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHjSMsudVzDIvySDXPZz9fXGkRBkofyGMpjly_fMG7fj_1An7BQ5rvHrv60ItQaZg_HgR6gQMgQRRmJ2aBQ_HiB8cXezGrJBFG-2WGfDefu7qlM4LQPiooyUzGVFCV_zhY9B-VuSRTlW5yfS5Nkcuc7hT6NsBLFwi-TxecqXkGXINwNHdHjkrjHPT8usJTFdPg4ABfMnLSxQ8gWIwZDWL43aF3Cb7XTCdRejw=)
7. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2iDmZirhYmqRqTb1S3-k5eTLmuk8X2kkiCOTRVfL9-uoabCNcBRvArg8W_cfAib167QnNIbfTgDUuZoCBtjhtRiDKyXkRRMIGxULeYvF5SmwWnNDYw-5v)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIh2nY7cESdz61gz5_ZjTwK9Ze9OSZu41zpSBwDlutHvRPKjwEPRP1boHu_HziuoQfeoyupHW57TJnt1GUMBwaha6PTV7fZDrBNlyNS3sxXfu5tQ65krTslE7RfoOEO3uAEaK8VR_UecCCyY0FrpSLV6GJJ0zLQDPMmagRM9N0KSUMeQZyiSNWiR7RUR6mqrlm72PiTKh3HJvQnqS5ns2h6lK3LvUf6LbGEU86EgdsSXfEySBk7OFpxf4hP3zJveqwfn6Ues5bKbg=)
9. [nus.edu.sg](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEV46OmYHC2iX2BWacWZaFpxQj6YROt1GG1U1ibUTjOn6zOv8Y_KMrVdNWZ04IsSxYBubAVKkhFrqaXpdA1qCrYdaSzzdyyNS1O3x_Xu63cZvJ22mcqNXd7sTpAwZ8fDRu2-7-PcHPhg_cPl4XFRF4C8xWKB3KLs8_MiE5quV7_5A==)
10. [yale.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLaQkb5MO-GZncloanKF7VdRoO7eZHB7xKTOF2TvPSJRw9FImbsTbbNi2IW-eWY-KD5lwzBPfZgXcnAxDZ5fDZFqpAjcv9BwKff2ZUaWNFWUuZn7UB_2DJonehZdCLag9mSwjLy8MYZhThln2DNdzQZiT6ip6BlqvdUMWQo5FgLh74TCQaJoQ84E9cIC10ty5nzDSPUjA=)
11. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwQEhMZ8TFpVFzPVrBdehDgz0irs1J2cFU6T4vbBXpy-t1SgB0woKFA6Oief-zlifu-Uhw9eeIda-LkAE34Y6hVlyH1BnQGm5G1ni3SQhEJr80dm5_hr8oXHrb3mPWgl1PMHEww7_BmKqlwXnecQ==)
12. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGm-5knTWRBe52hs4-8gn7rYnn32mR5eltSezRsag9uk5JkkJWY32dRU7NpA1fkyFADhFvfSy1jq3FA5OfD-f5mpzeBmUFphALTm_wE81LgehuJw4Hp6DbZkSfaX2vziuI=)
13. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJXIEjBXyUiPixcSaeDaEy9lbesYRNiBl2pgk3xzwvJ71uBv0lrTXrryOPL1DRMbG-b_xjYtpi2MJ6SgRHtd_bGEnRbeqtblHAsEphVDoy8tCwkMrDwpQNy6F4RNUJDUo=)
14. [thehindu.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGX0wK5K5mNaiUTiIHC_SB91bYx3gU-Vb0o9PIT99gY7iKaSZG6jxFXXXmvOjSAzv98lOj67fnjM2wfzcQsrB5ju_BpHIQvdUjBbhOHoMq6WEoEaqV1LalfBh0IND3JH9VLVPxeipRifuTj30xMjwPDfauW2OUOIm3wdA3fJ9f-flpwvJkIxfxSmN9fVMd_KYHYJrLvL_jTJfbMhNHojMiZAxn8hHN-bcJdR909)
15. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEquREr7ePwgelUugnEW1LSGNB8u8eajtr_EQMrtX5OIYyofyaUUgLPVTv375G6WqnxGx9LGpXwuqBd7xZGEphBNHxMsqiDA40zpy_nDoj6zz-JRVz3I5JETTF0QOCCGtgRcpO5JzhuY4B0GN-7fwXCwhqWd92n8hEiqBqnCJ50q96diw==)
16. [physicsworld.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFftUX67hB2qqxmWsIzNBiDH4QvMQuAF54Z-lSxlPZALszMAzPteDqZi0BOdIqUnbxn_F62ZoQw90MgqAoRFygGfYvK8PCfBKjfHqbd-pXw_aTOmoQ7zx4cCX3gk0iuYANOeyGn__9DUGxVboQ23gWfuoVYNOT6b39qUQTu)
17. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWprqVA8ykXFIHKRnvp8DcN3NRx-rGzz9U0LEM1wtzQyO3VAKNketPfhPpNR-Em3WqCG4xzQe8ldSEzUznCF4rdR5CHoWI9WxmG0QnGmwg53gaz85yKgsdz0uHIhE3I0Uu4XlGU6yK)
18. [iqoqi-vienna.at](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGN4GubYJANOZWASEnkAsaFpKRHPctrg7FRWJUmoZ5_uQ-djbIyIHVhLr7iP_1N3htao94ufJisC3Imc9Dmh_Vzpcdl3FCjXWlTOU4bc3I828lYK0wUGdjYG8g6gcpM7g_8Lc5IAPY3yrrMAQiWVcwsLdQEJhDkHOHZAZC6-1YFDnZkvJI0laAHe5G1cn6M4SFad5BP3s51AKZa-wZIU5Vy9YcAYvAiYUSyvG_9csM5CJhtk35Huh0Yq_tOmtabc6MsP6DVMXoOIDD6snip)
19. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFORakqjgq-xIcMNW5dxcMWvOxu5-H6oPDP9amKXpgBjATK1tOvV9mzqSHa8CKpqANAhVJysxaOUuSC5QPkpalPOITQoBDm4sHk19epK-5k7N1LB5GY)
20. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMjWKGZWzfUWEELuMOLDZEL5qDvD2GdB9zeBo5CxQ8TXMRuljum5dNs8NvmmdBBO4pobPnVSWgmJ5S9Sp8dCtRraB0YOeR0xEfhPkg53HsYI9yU2ptLyBddJr_TT7iLa0=)
21. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQER6PmIZmXZW9rFxn-m18YgP2ydrV0i7VXqvDfc6H1e3UV9L8r0K6V6hh4z-E2vs20El54Wk9xj0zID3jZZEDIVFyDS2asDcAkPUwEq_z0RkWyDb-tuDFm9Eq8bHtw9dXpLbgR90YQJNKUkhD7V34dQu4hBWwYTztW_7tOQK12E5GG9uew8PBPBAYPzUQBaCysfpBr009rXb063JqyV7jQSyEJ2uZCeyKyF-2zWBYDhfewEk75V9Mw2cOWecudjuCpuNsORTgA83Pza)
22. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnT1hct_UXSj_0mEvgHxWScA8VzzkbXnCije-d7U6HnN45Vs8e0bESgw4GrCM2vkPQiJekjNx3hyDtUeRoYKbumxMOzrVOVf6_LPPT8XQihPJLH9fgBmUPthQrwMaCKYUrtxklun9cOtyuy2_fuvDVHSDSr7PhnimVAP0S161oQ_aclYJwVk6Vyp9wMezOpfiMGRyB7UAIYGR9Kh2Az7zRhSKMRNts_HUUFAhj)
23. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYkia68xDK8YZJoLQM5xB4jP6yk2C0OpZaTBGA9ElTlQsV7Mq13cwy9AawwfW8g_obc7qxjlfp9sz77aB1DJgnhGyYw7jRepHognGvKUzxIsK6pc6q7farLWCvmT4JxxQiFIPY1PXbNFmas8APrVdkHROYzbmwLPEE-cTxLPkYEZBQG_tMZaYEgm5KSd8GZW71mTE7qseZrelJu8VyPEA=)
24. [osf.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIvWkvjX8yDV3TOeReCbtAAbMkcNxToBiTlSa1iC8BuO56pVHUPvDqmk8WkNx1OndTeXQr8C97nhlDW3q2pC2cDERxugO21uAJ0QFb--Elwx4o3NTHpGZdiC9k-VFA)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFR8N20WVXzcSLavRuB91hwbpdNNSyuRkJAGYtBU4Q0bwtNOdm-nJSm2dhZL6zT36zkwdEgzZNcTJrMdEiaSGBmHRvXj4Xg_9e_V_-fb6QUNOqrHYFKtWtSYG9Jk10zwBwihiWmJm13evjsm8TNd1QokbxXwgqCOPGD7JR8vKaUV-uzQP35BJbXlQ9j3umTRRJ2uy0AKx5vzrg-RZrAM2pOpvMRFk-C)
26. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJsCiZ1vC_Smc_dyj922nt3ie01UCxD3z33Kif7n4QK7YW98piUnlSV22iIlJwRQwGlqHkzIspEzUubRx8qjyvdFasovzr7DftMPONByOK0yEHdvba4evFSvvN-Q64jJ0nADfuq-CQRCG7wmhRhuzL)
27. [photonics.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFW1NnfZXxPRnDxQKrE3L0gW9-Ow52MLLavjt4DTJ18eGEgKQBSEZsYXtKrrSY3G5TX4uMA_5J5WH9ienZp_75QIk4y5gpqo6e98rIm57bGmBIA5KlwbufPdR_B5IUoqKnolcDjMQem8Zu-alJOyJU337w3wRzYi_jHya3J_v7FL_-l)
28. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVfvX29OYFwyIX6ei7F7rhrd7GbbQNjxhYx1Nwq_2TWkwEi8GNsA9CVOcTnECBqusXh04kbfb6CgnOKCe326y1e4FcZII_D_uLpcvoQE6tq-_L1U3TwJB6MSLA_7UYT9PXAR50Vbp1v8XhJSx0Nx2g3xI57g6Uxwf9WAy7Xl-l2QUBCxWyk4st2AeifowwIGIVxsd2UyUJzs8=)
29. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs8BddGEtQ3NdW4Dhi5DTOS9_f0MXcj8jhZ0MJzDJTop0n11gW_k4u0RLUtNuEcrvpcpQ3s52-Ibcz7b7Y36ghPBT57Xu7Gm4B66_y5uor4i9fVSVkjmwy)
30. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrnL0nM_U98uTaiBdoO7OiEtW8RzbLngeKy-H__XcLTN0SP_p5shmv9Idpm74JQZZ2-OvSAFMebfgJz3CiBIH7-WOAFGCx6bgOxIZ4j2zJSTuaTa1pv_jXi09pQK7nHYcEIUXO373rAiUJu_L0KVnTyIQCQaoe4MhOdgDHOSg5JZ4KDNuxTyChywUi)
31. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsAxjFE1bBX3Zax_gNKQLhOlpAkRZD_PUc8aEIry5PC7Qv4Kx6NNZ5tGUtCFWurBbDRkG8JtkulJ1l8xorRr4AS-SZrik-Df1r_858dszyU2WeNdEJ9IZn)
32. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_q46q_Ylu2EABx_C--F7EqsCbmSNoZWxBG6qk00AdEy7qObeZB4iZsOsCncX38yWWG6aYPQbHoQ4IG7jSz7nL1VlQw_NDSCK1O9NGGNBqkXn4Yv-e)
33. [fiveable.me](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkf0NnsWCnqP82k_IDD7NZI1XZupmQYiUhcGgIe7ls1Ca8cLFTVqelD9L0Uz7jiGwZyo7ATuuVWOWvJITNmGuUsgBpAKs5sA-y6lUZZfNSuC5i3NW4LI9vBYFC-RqV7KXJOx_z51l5ESBAyvvTcshRafBa_y_Itl_h_4BCkJF-l-WlRhbirKrTWAa-6oKnocZUWppDlLC6sPnIgWfOkYLD0XvLRUI0PA==)
34. [anu.edu.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6mrI0EdKkkdwf67gW51EZWycvkoRGRHmCZRinoWZMHvaDzjJmT_ZAMTh2mQEKFOhhpb2rGj_Q8a_w6xUSxoko1GSojCbgfHShUf2r-IhP6fZ-aLIqaqkKTOoBFh-rm9Es81UPhvOA7TVA-O8Qg_SX_Qoh9c-GiOZ7_HdLnn3RodxO6oX6yD6Ki6dYssRJf9gM)
35. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6hauSXXH_S_nlEcNOqo35xpbjnixYpvEiIBvY66yoprf0AxSciiBIibAYYCoTytdD-iG4RlUUrkcYMx6yMK53Qb6dd1UluHdkooTNb7KcRQb7IsGV9ZkOXSxkHn_6SFV40Tm05_doqrdEDRGMHaMakF5zSC4TQUQcGy6qyMNW-D47-_U0Ofh1OGa9LWabzsBqqPQIg6rlWOU8weY_dCfLB0hQR5c=)
36. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvWTf4-rFMQOHBDIeWOp0I0rHnaGBdoqmiQN3E0_tIBWZk69zVaDMf8k9u65DTWSHxTX54D-i7PmMxvojpksloeX_sOVxEsDvinrRBMNphOB4uo7k=)
37. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLKIpvRefzA1Wfydx1eXoXIXbzkiUcJyjBtJdCuIfouk5stUUDndRFKxAJME2nr9zIurg_BPJYByl_zFqYVsAHTM_q1-66qrNJibAx7Ys_Z2EpyqsTV757PRXXpgyAegGrKhBWVJfJOcamgEOxAii-X2lKBo8qng==)
38. [csic.es](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrAbLQOvVKbKDHex9RLnL_yVuSRpfrHwIkCz_Ngd3L3P3dQc13gwOefJMpxW73kI-Qryrp2l7eB_EYml2vmpYn_OXL8-AcSJP4YyI3dfr8_ewuayom9iMB2M9FtAFsVipYAE6gnoftwb4e4U9Yk8FnZYtgG0X9U6JNkoXZ)


## Annotations
Annotation(end_index=1996, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjVrdolakegFkJY0H9wMb5CNijOeShpcGQePFO7kjmcCP_TW1BZbEJjm4FU1-_sthXprzxmeCkEG3smbGt5u7gr-Hq77p6cnrLTfhHlY30BN9rUnZO', start_index=1984)
Annotation(end_index=1996, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKs7oOz8uZ3Js3YN6UWoh6amAZEzeGwblBjUszuiBr2deaUo5Tgr8LOAfd4pBaRo0haaXLyTNTpnSN0fWKHC_cZIlZEUkSPbMFio3tzPIBk7AW8ilkPUh5lyu2eoXjQn33GA39I_HQzrBTacPleAuHSgmQ', start_index=1984)
Annotation(end_index=2355, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFx_UAoz8tZB8qCkhFLOrWr-pIBngTVpMB3fD2i4hweyUkdzbeGPmZ4WAxmQ4p7lVDRQHLBjcUTx7tSUz_pdjX7dUxvB6HlwN7HXjjovaEglQYJk8G94_bGsuw-4Ihe5Gw=', start_index=2343)
Annotation(end_index=2355, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKWSuL5pyIXDsVyjXPxfD_HJ04WnnSdD4aBtI3Nd7qGVv_HmH7aE1pC-WYZH9B_UZ_8iPNKbu8L0etBXvD0G5mSbfbtOXX4pCN9N8kI-to0oNFt41OMVPnua6k-A==', start_index=2343)
Annotation(end_index=2713, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmpKlCT744XutcgLoGYOH4CfhJV7QCmYwDa1M9w4F_sXb40W3_FVMk3MVWKbsudrp7kQl__M9xYyexuwV-bC_-3KHKwmc2QY69AIGuGO_MLp-hZ_GvWL8WGyR03ab6ObZ8pKUnOiK4W940Of2QqXcnGk09pmpEQhjTs4Qq2zHiNUMH0bjp9cJl8tEmw71HPYmnxHmV6Oi_GbLf3RzYCNWXOX9MsbxYBqBo5Dedvp9X4H1HKrnd9Xpam8jelh8N_A==', start_index=2701)
Annotation(end_index=2713, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHjSMsudVzDIvySDXPZz9fXGkRBkofyGMpjly_fMG7fj_1An7BQ5rvHrv60ItQaZg_HgR6gQMgQRRmJ2aBQ_HiB8cXezGrJBFG-2WGfDefu7qlM4LQPiooyUzGVFCV_zhY9B-VuSRTlW5yfS5Nkcuc7hT6NsBLFwi-TxecqXkGXINwNHdHjkrjHPT8usJTFdPg4ABfMnLSxQ8gWIwZDWL43aF3Cb7XTCdRejw=', start_index=2701)
Annotation(end_index=2906, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIh2nY7cESdz61gz5_ZjTwK9Ze9OSZu41zpSBwDlutHvRPKjwEPRP1boHu_HziuoQfeoyupHW57TJnt1GUMBwaha6PTV7fZDrBNlyNS3sxXfu5tQ65krTslE7RfoOEO3uAEaK8VR_UecCCyY0FrpSLV6GJJ0zLQDPMmagRM9N0KSUMeQZyiSNWiR7RUR6mqrlm72PiTKh3HJvQnqS5ns2h6lK3LvUf6LbGEU86EgdsSXfEySBk7OFpxf4hP3zJveqwfn6Ues5bKbg=', start_index=2894)
Annotation(end_index=2906, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2iDmZirhYmqRqTb1S3-k5eTLmuk8X2kkiCOTRVfL9-uoabCNcBRvArg8W_cfAib167QnNIbfTgDUuZoCBtjhtRiDKyXkRRMIGxULeYvF5SmwWnNDYw-5v', start_index=2894)
Annotation(end_index=4207, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmpKlCT744XutcgLoGYOH4CfhJV7QCmYwDa1M9w4F_sXb40W3_FVMk3MVWKbsudrp7kQl__M9xYyexuwV-bC_-3KHKwmc2QY69AIGuGO_MLp-hZ_GvWL8WGyR03ab6ObZ8pKUnOiK4W940Of2QqXcnGk09pmpEQhjTs4Qq2zHiNUMH0bjp9cJl8tEmw71HPYmnxHmV6Oi_GbLf3RzYCNWXOX9MsbxYBqBo5Dedvp9X4H1HKrnd9Xpam8jelh8N_A==', start_index=4195)
Annotation(end_index=4207, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2iDmZirhYmqRqTb1S3-k5eTLmuk8X2kkiCOTRVfL9-uoabCNcBRvArg8W_cfAib167QnNIbfTgDUuZoCBtjhtRiDKyXkRRMIGxULeYvF5SmwWnNDYw-5v', start_index=4195)
Annotation(end_index=4576, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEV46OmYHC2iX2BWacWZaFpxQj6YROt1GG1U1ibUTjOn6zOv8Y_KMrVdNWZ04IsSxYBubAVKkhFrqaXpdA1qCrYdaSzzdyyNS1O3x_Xu63cZvJ22mcqNXd7sTpAwZ8fDRu2-7-PcHPhg_cPl4XFRF4C8xWKB3KLs8_MiE5quV7_5A==', start_index=4563)
Annotation(end_index=4576, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLaQkb5MO-GZncloanKF7VdRoO7eZHB7xKTOF2TvPSJRw9FImbsTbbNi2IW-eWY-KD5lwzBPfZgXcnAxDZ5fDZFqpAjcv9BwKff2ZUaWNFWUuZn7UB_2DJonehZdCLag9mSwjLy8MYZhThln2DNdzQZiT6ip6BlqvdUMWQo5FgLh74TCQaJoQ84E9cIC10ty5nzDSPUjA=', start_index=4563)
Annotation(end_index=4968, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGm-5knTWRBe52hs4-8gn7rYnn32mR5eltSezRsag9uk5JkkJWY32dRU7NpA1fkyFADhFvfSy1jq3FA5OfD-f5mpzeBmUFphALTm_wE81LgehuJw4Hp6DbZkSfaX2vziuI=', start_index=4954)
Annotation(end_index=4968, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwQEhMZ8TFpVFzPVrBdehDgz0irs1J2cFU6T4vbBXpy-t1SgB0woKFA6Oief-zlifu-Uhw9eeIda-LkAE34Y6hVlyH1BnQGm5G1ni3SQhEJr80dm5_hr8oXHrb3mPWgl1PMHEww7_BmKqlwXnecQ==', start_index=4954)
Annotation(end_index=5465, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmpKlCT744XutcgLoGYOH4CfhJV7QCmYwDa1M9w4F_sXb40W3_FVMk3MVWKbsudrp7kQl__M9xYyexuwV-bC_-3KHKwmc2QY69AIGuGO_MLp-hZ_GvWL8WGyR03ab6ObZ8pKUnOiK4W940Of2QqXcnGk09pmpEQhjTs4Qq2zHiNUMH0bjp9cJl8tEmw71HPYmnxHmV6Oi_GbLf3RzYCNWXOX9MsbxYBqBo5Dedvp9X4H1HKrnd9Xpam8jelh8N_A==', start_index=5452)
Annotation(end_index=5465, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJXIEjBXyUiPixcSaeDaEy9lbesYRNiBl2pgk3xzwvJ71uBv0lrTXrryOPL1DRMbG-b_xjYtpi2MJ6SgRHtd_bGEnRbeqtblHAsEphVDoy8tCwkMrDwpQNy6F4RNUJDUo=', start_index=5452)
Annotation(end_index=5771, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmpKlCT744XutcgLoGYOH4CfhJV7QCmYwDa1M9w4F_sXb40W3_FVMk3MVWKbsudrp7kQl__M9xYyexuwV-bC_-3KHKwmc2QY69AIGuGO_MLp-hZ_GvWL8WGyR03ab6ObZ8pKUnOiK4W940Of2QqXcnGk09pmpEQhjTs4Qq2zHiNUMH0bjp9cJl8tEmw71HPYmnxHmV6Oi_GbLf3RzYCNWXOX9MsbxYBqBo5Dedvp9X4H1HKrnd9Xpam8jelh8N_A==', start_index=5758)
Annotation(end_index=5771, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGX0wK5K5mNaiUTiIHC_SB91bYx3gU-Vb0o9PIT99gY7iKaSZG6jxFXXXmvOjSAzv98lOj67fnjM2wfzcQsrB5ju_BpHIQvdUjBbhOHoMq6WEoEaqV1LalfBh0IND3JH9VLVPxeipRifuTj30xMjwPDfauW2OUOIm3wdA3fJ9f-flpwvJkIxfxSmN9fVMd_KYHYJrLvL_jTJfbMhNHojMiZAxn8hHN-bcJdR909', start_index=5758)
Annotation(end_index=6099, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEquREr7ePwgelUugnEW1LSGNB8u8eajtr_EQMrtX5OIYyofyaUUgLPVTv375G6WqnxGx9LGpXwuqBd7xZGEphBNHxMsqiDA40zpy_nDoj6zz-JRVz3I5JETTF0QOCCGtgRcpO5JzhuY4B0GN-7fwXCwhqWd92n8hEiqBqnCJ50q96diw==', start_index=6085)
Annotation(end_index=6099, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFftUX67hB2qqxmWsIzNBiDH4QvMQuAF54Z-lSxlPZALszMAzPteDqZi0BOdIqUnbxn_F62ZoQw90MgqAoRFygGfYvK8PCfBKjfHqbd-pXw_aTOmoQ7zx4cCX3gk0iuYANOeyGn__9DUGxVboQ23gWfuoVYNOT6b39qUQTu', start_index=6085)
Annotation(end_index=6708, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGN4GubYJANOZWASEnkAsaFpKRHPctrg7FRWJUmoZ5_uQ-djbIyIHVhLr7iP_1N3htao94ufJisC3Imc9Dmh_Vzpcdl3FCjXWlTOU4bc3I828lYK0wUGdjYG8g6gcpM7g_8Lc5IAPY3yrrMAQiWVcwsLdQEJhDkHOHZAZC6-1YFDnZkvJI0laAHe5G1cn6M4SFad5BP3s51AKZa-wZIU5Vy9YcAYvAiYUSyvG_9csM5CJhtk35Huh0Yq_tOmtabc6MsP6DVMXoOIDD6snip', start_index=6694)
Annotation(end_index=6708, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWprqVA8ykXFIHKRnvp8DcN3NRx-rGzz9U0LEM1wtzQyO3VAKNketPfhPpNR-Em3WqCG4xzQe8ldSEzUznCF4rdR5CHoWI9WxmG0QnGmwg53gaz85yKgsdz0uHIhE3I0Uu4XlGU6yK', start_index=6694)
Annotation(end_index=7632, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMjWKGZWzfUWEELuMOLDZEL5qDvD2GdB9zeBo5CxQ8TXMRuljum5dNs8NvmmdBBO4pobPnVSWgmJ5S9Sp8dCtRraB0YOeR0xEfhPkg53HsYI9yU2ptLyBddJr_TT7iLa0=', start_index=7614)
Annotation(end_index=7632, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQER6PmIZmXZW9rFxn-m18YgP2ydrV0i7VXqvDfc6H1e3UV9L8r0K6V6hh4z-E2vs20El54Wk9xj0zID3jZZEDIVFyDS2asDcAkPUwEq_z0RkWyDb-tuDFm9Eq8bHtw9dXpLbgR90YQJNKUkhD7V34dQu4hBWwYTztW_7tOQK12E5GG9uew8PBPBAYPzUQBaCysfpBr009rXb063JqyV7jQSyEJ2uZCeyKyF-2zWBYDhfewEk75V9Mw2cOWecudjuCpuNsORTgA83Pza', start_index=7614)
Annotation(end_index=7632, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFORakqjgq-xIcMNW5dxcMWvOxu5-H6oPDP9amKXpgBjATK1tOvV9mzqSHa8CKpqANAhVJysxaOUuSC5QPkpalPOITQoBDm4sHk19epK-5k7N1LB5GY', start_index=7614)
Annotation(end_index=8025, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnT1hct_UXSj_0mEvgHxWScA8VzzkbXnCije-d7U6HnN45Vs8e0bESgw4GrCM2vkPQiJekjNx3hyDtUeRoYKbumxMOzrVOVf6_LPPT8XQihPJLH9fgBmUPthQrwMaCKYUrtxklun9cOtyuy2_fuvDVHSDSr7PhnimVAP0S161oQ_aclYJwVk6Vyp9wMezOpfiMGRyB7UAIYGR9Kh2Az7zRhSKMRNts_HUUFAhj', start_index=8015)
Annotation(end_index=8480, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnT1hct_UXSj_0mEvgHxWScA8VzzkbXnCije-d7U6HnN45Vs8e0bESgw4GrCM2vkPQiJekjNx3hyDtUeRoYKbumxMOzrVOVf6_LPPT8XQihPJLH9fgBmUPthQrwMaCKYUrtxklun9cOtyuy2_fuvDVHSDSr7PhnimVAP0S161oQ_aclYJwVk6Vyp9wMezOpfiMGRyB7UAIYGR9Kh2Az7zRhSKMRNts_HUUFAhj', start_index=8470)
Annotation(end_index=8792, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjVrdolakegFkJY0H9wMb5CNijOeShpcGQePFO7kjmcCP_TW1BZbEJjm4FU1-_sthXprzxmeCkEG3smbGt5u7gr-Hq77p6cnrLTfhHlY30BN9rUnZO', start_index=8779)
Annotation(end_index=8792, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYkia68xDK8YZJoLQM5xB4jP6yk2C0OpZaTBGA9ElTlQsV7Mq13cwy9AawwfW8g_obc7qxjlfp9sz77aB1DJgnhGyYw7jRepHognGvKUzxIsK6pc6q7farLWCvmT4JxxQiFIPY1PXbNFmas8APrVdkHROYzbmwLPEE-cTxLPkYEZBQG_tMZaYEgm5KSd8GZW71mTE7qseZrelJu8VyPEA=', start_index=8779)
Annotation(end_index=9162, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIvWkvjX8yDV3TOeReCbtAAbMkcNxToBiTlSa1iC8BuO56pVHUPvDqmk8WkNx1OndTeXQr8C97nhlDW3q2pC2cDERxugO21uAJ0QFb--Elwx4o3NTHpGZdiC9k-VFA', start_index=9149)
Annotation(end_index=9162, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2iDmZirhYmqRqTb1S3-k5eTLmuk8X2kkiCOTRVfL9-uoabCNcBRvArg8W_cfAib167QnNIbfTgDUuZoCBtjhtRiDKyXkRRMIGxULeYvF5SmwWnNDYw-5v', start_index=9149)
Annotation(end_index=9709, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGX0wK5K5mNaiUTiIHC_SB91bYx3gU-Vb0o9PIT99gY7iKaSZG6jxFXXXmvOjSAzv98lOj67fnjM2wfzcQsrB5ju_BpHIQvdUjBbhOHoMq6WEoEaqV1LalfBh0IND3JH9VLVPxeipRifuTj30xMjwPDfauW2OUOIm3wdA3fJ9f-flpwvJkIxfxSmN9fVMd_KYHYJrLvL_jTJfbMhNHojMiZAxn8hHN-bcJdR909', start_index=9699)
Annotation(end_index=10117, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjVrdolakegFkJY0H9wMb5CNijOeShpcGQePFO7kjmcCP_TW1BZbEJjm4FU1-_sthXprzxmeCkEG3smbGt5u7gr-Hq77p6cnrLTfhHlY30BN9rUnZO', start_index=10104)
Annotation(end_index=10117, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnT1hct_UXSj_0mEvgHxWScA8VzzkbXnCije-d7U6HnN45Vs8e0bESgw4GrCM2vkPQiJekjNx3hyDtUeRoYKbumxMOzrVOVf6_LPPT8XQihPJLH9fgBmUPthQrwMaCKYUrtxklun9cOtyuy2_fuvDVHSDSr7PhnimVAP0S161oQ_aclYJwVk6Vyp9wMezOpfiMGRyB7UAIYGR9Kh2Az7zRhSKMRNts_HUUFAhj', start_index=10104)
Annotation(end_index=10344, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHjSMsudVzDIvySDXPZz9fXGkRBkofyGMpjly_fMG7fj_1An7BQ5rvHrv60ItQaZg_HgR6gQMgQRRmJ2aBQ_HiB8cXezGrJBFG-2WGfDefu7qlM4LQPiooyUzGVFCV_zhY9B-VuSRTlW5yfS5Nkcuc7hT6NsBLFwi-TxecqXkGXINwNHdHjkrjHPT8usJTFdPg4ABfMnLSxQ8gWIwZDWL43aF3Cb7XTCdRejw=', start_index=10331)
Annotation(end_index=10344, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLaQkb5MO-GZncloanKF7VdRoO7eZHB7xKTOF2TvPSJRw9FImbsTbbNi2IW-eWY-KD5lwzBPfZgXcnAxDZ5fDZFqpAjcv9BwKff2ZUaWNFWUuZn7UB_2DJonehZdCLag9mSwjLy8MYZhThln2DNdzQZiT6ip6BlqvdUMWQo5FgLh74TCQaJoQ84E9cIC10ty5nzDSPUjA=', start_index=10331)
Annotation(end_index=10636, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHjSMsudVzDIvySDXPZz9fXGkRBkofyGMpjly_fMG7fj_1An7BQ5rvHrv60ItQaZg_HgR6gQMgQRRmJ2aBQ_HiB8cXezGrJBFG-2WGfDefu7qlM4LQPiooyUzGVFCV_zhY9B-VuSRTlW5yfS5Nkcuc7hT6NsBLFwi-TxecqXkGXINwNHdHjkrjHPT8usJTFdPg4ABfMnLSxQ8gWIwZDWL43aF3Cb7XTCdRejw=', start_index=10627)
Annotation(end_index=10891, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFR8N20WVXzcSLavRuB91hwbpdNNSyuRkJAGYtBU4Q0bwtNOdm-nJSm2dhZL6zT36zkwdEgzZNcTJrMdEiaSGBmHRvXj4Xg_9e_V_-fb6QUNOqrHYFKtWtSYG9Jk10zwBwihiWmJm13evjsm8TNd1QokbxXwgqCOPGD7JR8vKaUV-uzQP35BJbXlQ9j3umTRRJ2uy0AKx5vzrg-RZrAM2pOpvMRFk-C', start_index=10881)
Annotation(end_index=11257, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFW1NnfZXxPRnDxQKrE3L0gW9-Ow52MLLavjt4DTJ18eGEgKQBSEZsYXtKrrSY3G5TX4uMA_5J5WH9ienZp_75QIk4y5gpqo6e98rIm57bGmBIA5KlwbufPdR_B5IUoqKnolcDjMQem8Zu-alJOyJU337w3wRzYi_jHya3J_v7FL_-l', start_index=11243)
Annotation(end_index=11257, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJsCiZ1vC_Smc_dyj922nt3ie01UCxD3z33Kif7n4QK7YW98piUnlSV22iIlJwRQwGlqHkzIspEzUubRx8qjyvdFasovzr7DftMPONByOK0yEHdvba4evFSvvN-Q64jJ0nADfuq-CQRCG7wmhRhuzL', start_index=11243)
Annotation(end_index=11646, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVfvX29OYFwyIX6ei7F7rhrd7GbbQNjxhYx1Nwq_2TWkwEi8GNsA9CVOcTnECBqusXh04kbfb6CgnOKCe326y1e4FcZII_D_uLpcvoQE6tq-_L1U3TwJB6MSLA_7UYT9PXAR50Vbp1v8XhJSx0Nx2g3xI57g6Uxwf9WAy7Xl-l2QUBCxWyk4st2AeifowwIGIVxsd2UyUJzs8=', start_index=11632)
Annotation(end_index=11646, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJsCiZ1vC_Smc_dyj922nt3ie01UCxD3z33Kif7n4QK7YW98piUnlSV22iIlJwRQwGlqHkzIspEzUubRx8qjyvdFasovzr7DftMPONByOK0yEHdvba4evFSvvN-Q64jJ0nADfuq-CQRCG7wmhRhuzL', start_index=11632)
Annotation(end_index=11822, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs8BddGEtQ3NdW4Dhi5DTOS9_f0MXcj8jhZ0MJzDJTop0n11gW_k4u0RLUtNuEcrvpcpQ3s52-Ibcz7b7Y36ghPBT57Xu7Gm4B66_y5uor4i9fVSVkjmwy', start_index=11812)
Annotation(end_index=12204, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsAxjFE1bBX3Zax_gNKQLhOlpAkRZD_PUc8aEIry5PC7Qv4Kx6NNZ5tGUtCFWurBbDRkG8JtkulJ1l8xorRr4AS-SZrik-Df1r_858dszyU2WeNdEJ9IZn', start_index=12190)
Annotation(end_index=12204, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrnL0nM_U98uTaiBdoO7OiEtW8RzbLngeKy-H__XcLTN0SP_p5shmv9Idpm74JQZZ2-OvSAFMebfgJz3CiBIH7-WOAFGCx6bgOxIZ4j2zJSTuaTa1pv_jXi09pQK7nHYcEIUXO373rAiUJu_L0KVnTyIQCQaoe4MhOdgDHOSg5JZ4KDNuxTyChywUi', start_index=12190)
Annotation(end_index=12532, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_q46q_Ylu2EABx_C--F7EqsCbmSNoZWxBG6qk00AdEy7qObeZB4iZsOsCncX38yWWG6aYPQbHoQ4IG7jSz7nL1VlQw_NDSCK1O9NGGNBqkXn4Yv-e', start_index=12518)
Annotation(end_index=12532, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrnL0nM_U98uTaiBdoO7OiEtW8RzbLngeKy-H__XcLTN0SP_p5shmv9Idpm74JQZZ2-OvSAFMebfgJz3CiBIH7-WOAFGCx6bgOxIZ4j2zJSTuaTa1pv_jXi09pQK7nHYcEIUXO373rAiUJu_L0KVnTyIQCQaoe4MhOdgDHOSg5JZ4KDNuxTyChywUi', start_index=12518)
Annotation(end_index=13023, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkf0NnsWCnqP82k_IDD7NZI1XZupmQYiUhcGgIe7ls1Ca8cLFTVqelD9L0Uz7jiGwZyo7ATuuVWOWvJITNmGuUsgBpAKs5sA-y6lUZZfNSuC5i3NW4LI9vBYFC-RqV7KXJOx_z51l5ESBAyvvTcshRafBa_y_Itl_h_4BCkJF-l-WlRhbirKrTWAa-6oKnocZUWppDlLC6sPnIgWfOkYLD0XvLRUI0PA==', start_index=13009)
Annotation(end_index=13023, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwQEhMZ8TFpVFzPVrBdehDgz0irs1J2cFU6T4vbBXpy-t1SgB0woKFA6Oief-zlifu-Uhw9eeIda-LkAE34Y6hVlyH1BnQGm5G1ni3SQhEJr80dm5_hr8oXHrb3mPWgl1PMHEww7_BmKqlwXnecQ==', start_index=13009)
Annotation(end_index=13258, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGm-5knTWRBe52hs4-8gn7rYnn32mR5eltSezRsag9uk5JkkJWY32dRU7NpA1fkyFADhFvfSy1jq3FA5OfD-f5mpzeBmUFphALTm_wE81LgehuJw4Hp6DbZkSfaX2vziuI=', start_index=13248)
Annotation(end_index=13444, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6mrI0EdKkkdwf67gW51EZWycvkoRGRHmCZRinoWZMHvaDzjJmT_ZAMTh2mQEKFOhhpb2rGj_Q8a_w6xUSxoko1GSojCbgfHShUf2r-IhP6fZ-aLIqaqkKTOoBFh-rm9Es81UPhvOA7TVA-O8Qg_SX_Qoh9c-GiOZ7_HdLnn3RodxO6oX6yD6Ki6dYssRJf9gM', start_index=13430)
Annotation(end_index=13444, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwQEhMZ8TFpVFzPVrBdehDgz0irs1J2cFU6T4vbBXpy-t1SgB0woKFA6Oief-zlifu-Uhw9eeIda-LkAE34Y6hVlyH1BnQGm5G1ni3SQhEJr80dm5_hr8oXHrb3mPWgl1PMHEww7_BmKqlwXnecQ==', start_index=13430)
Annotation(end_index=13947, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEV46OmYHC2iX2BWacWZaFpxQj6YROt1GG1U1ibUTjOn6zOv8Y_KMrVdNWZ04IsSxYBubAVKkhFrqaXpdA1qCrYdaSzzdyyNS1O3x_Xu63cZvJ22mcqNXd7sTpAwZ8fDRu2-7-PcHPhg_cPl4XFRF4C8xWKB3KLs8_MiE5quV7_5A==', start_index=13930)
Annotation(end_index=13947, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvWTf4-rFMQOHBDIeWOp0I0rHnaGBdoqmiQN3E0_tIBWZk69zVaDMf8k9u65DTWSHxTX54D-i7PmMxvojpksloeX_sOVxEsDvinrRBMNphOB4uo7k=', start_index=13930)
Annotation(end_index=13947, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6hauSXXH_S_nlEcNOqo35xpbjnixYpvEiIBvY66yoprf0AxSciiBIibAYYCoTytdD-iG4RlUUrkcYMx6yMK53Qb6dd1UluHdkooTNb7KcRQb7IsGV9ZkOXSxkHn_6SFV40Tm05_doqrdEDRGMHaMakF5zSC4TQUQcGy6qyMNW-D47-_U0Ofh1OGa9LWabzsBqqPQIg6rlWOU8weY_dCfLB0hQR5c=', start_index=13930)
Annotation(end_index=14538, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLKIpvRefzA1Wfydx1eXoXIXbzkiUcJyjBtJdCuIfouk5stUUDndRFKxAJME2nr9zIurg_BPJYByl_zFqYVsAHTM_q1-66qrNJibAx7Ys_Z2EpyqsTV757PRXXpgyAegGrKhBWVJfJOcamgEOxAii-X2lKBo8qng==', start_index=14524)
Annotation(end_index=14538, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrnL0nM_U98uTaiBdoO7OiEtW8RzbLngeKy-H__XcLTN0SP_p5shmv9Idpm74JQZZ2-OvSAFMebfgJz3CiBIH7-WOAFGCx6bgOxIZ4j2zJSTuaTa1pv_jXi09pQK7nHYcEIUXO373rAiUJu_L0KVnTyIQCQaoe4MhOdgDHOSg5JZ4KDNuxTyChywUi', start_index=14524)
Annotation(end_index=15305, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmpKlCT744XutcgLoGYOH4CfhJV7QCmYwDa1M9w4F_sXb40W3_FVMk3MVWKbsudrp7kQl__M9xYyexuwV-bC_-3KHKwmc2QY69AIGuGO_MLp-hZ_GvWL8WGyR03ab6ObZ8pKUnOiK4W940Of2QqXcnGk09pmpEQhjTs4Qq2zHiNUMH0bjp9cJl8tEmw71HPYmnxHmV6Oi_GbLf3RzYCNWXOX9MsbxYBqBo5Dedvp9X4H1HKrnd9Xpam8jelh8N_A==', start_index=15296)
Annotation(end_index=15917, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmpKlCT744XutcgLoGYOH4CfhJV7QCmYwDa1M9w4F_sXb40W3_FVMk3MVWKbsudrp7kQl__M9xYyexuwV-bC_-3KHKwmc2QY69AIGuGO_MLp-hZ_GvWL8WGyR03ab6ObZ8pKUnOiK4W940Of2QqXcnGk09pmpEQhjTs4Qq2zHiNUMH0bjp9cJl8tEmw71HPYmnxHmV6Oi_GbLf3RzYCNWXOX9MsbxYBqBo5Dedvp9X4H1HKrnd9Xpam8jelh8N_A==', start_index=15905)
Annotation(end_index=15917, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFx_UAoz8tZB8qCkhFLOrWr-pIBngTVpMB3fD2i4hweyUkdzbeGPmZ4WAxmQ4p7lVDRQHLBjcUTx7tSUz_pdjX7dUxvB6HlwN7HXjjovaEglQYJk8G94_bGsuw-4Ihe5Gw=', start_index=15905)
Annotation(end_index=16355, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEquREr7ePwgelUugnEW1LSGNB8u8eajtr_EQMrtX5OIYyofyaUUgLPVTv375G6WqnxGx9LGpXwuqBd7xZGEphBNHxMsqiDA40zpy_nDoj6zz-JRVz3I5JETTF0QOCCGtgRcpO5JzhuY4B0GN-7fwXCwhqWd92n8hEiqBqnCJ50q96diw==', start_index=16341)
Annotation(end_index=16355, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFftUX67hB2qqxmWsIzNBiDH4QvMQuAF54Z-lSxlPZALszMAzPteDqZi0BOdIqUnbxn_F62ZoQw90MgqAoRFygGfYvK8PCfBKjfHqbd-pXw_aTOmoQ7zx4cCX3gk0iuYANOeyGn__9DUGxVboQ23gWfuoVYNOT6b39qUQTu', start_index=16341)
Annotation(end_index=16585, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIvWkvjX8yDV3TOeReCbtAAbMkcNxToBiTlSa1iC8BuO56pVHUPvDqmk8WkNx1OndTeXQr8C97nhlDW3q2pC2cDERxugO21uAJ0QFb--Elwx4o3NTHpGZdiC9k-VFA', start_index=16571)
Annotation(end_index=16585, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrAbLQOvVKbKDHex9RLnL_yVuSRpfrHwIkCz_Ngd3L3P3dQc13gwOefJMpxW73kI-Qryrp2l7eB_EYml2vmpYn_OXL8-AcSJP4YyI3dfr8_ewuayom9iMB2M9FtAFsVipYAE6gnoftwb4e4U9Yk8FnZYtgG0X9U6JNkoXZ', start_index=16571)
Annotation(end_index=17708, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjVrdolakegFkJY0H9wMb5CNijOeShpcGQePFO7kjmcCP_TW1BZbEJjm4FU1-_sthXprzxmeCkEG3smbGt5u7gr-Hq77p6cnrLTfhHlY30BN9rUnZO', start_index=17696)
Annotation(end_index=17708, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKs7oOz8uZ3Js3YN6UWoh6amAZEzeGwblBjUszuiBr2deaUo5Tgr8LOAfd4pBaRo0haaXLyTNTpnSN0fWKHC_cZIlZEUkSPbMFio3tzPIBk7AW8ilkPUh5lyu2eoXjQn33GA39I_HQzrBTacPleAuHSgmQ', start_index=17696)
Annotation(end_index=17777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmpKlCT744XutcgLoGYOH4CfhJV7QCmYwDa1M9w4F_sXb40W3_FVMk3MVWKbsudrp7kQl__M9xYyexuwV-bC_-3KHKwmc2QY69AIGuGO_MLp-hZ_GvWL8WGyR03ab6ObZ8pKUnOiK4W940Of2QqXcnGk09pmpEQhjTs4Qq2zHiNUMH0bjp9cJl8tEmw71HPYmnxHmV6Oi_GbLf3RzYCNWXOX9MsbxYBqBo5Dedvp9X4H1HKrnd9Xpam8jelh8N_A==', start_index=17765)
Annotation(end_index=17777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2iDmZirhYmqRqTb1S3-k5eTLmuk8X2kkiCOTRVfL9-uoabCNcBRvArg8W_cfAib167QnNIbfTgDUuZoCBtjhtRiDKyXkRRMIGxULeYvF5SmwWnNDYw-5v', start_index=17765)
Annotation(end_index=17851, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKWSuL5pyIXDsVyjXPxfD_HJ04WnnSdD4aBtI3Nd7qGVv_HmH7aE1pC-WYZH9B_UZ_8iPNKbu8L0etBXvD0G5mSbfbtOXX4pCN9N8kI-to0oNFt41OMVPnua6k-A==', start_index=17838)
Annotation(end_index=17851, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGX0wK5K5mNaiUTiIHC_SB91bYx3gU-Vb0o9PIT99gY7iKaSZG6jxFXXXmvOjSAzv98lOj67fnjM2wfzcQsrB5ju_BpHIQvdUjBbhOHoMq6WEoEaqV1LalfBh0IND3JH9VLVPxeipRifuTj30xMjwPDfauW2OUOIm3wdA3fJ9f-flpwvJkIxfxSmN9fVMd_KYHYJrLvL_jTJfbMhNHojMiZAxn8hHN-bcJdR909', start_index=17838)
Annotation(end_index=17907, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnT1hct_UXSj_0mEvgHxWScA8VzzkbXnCije-d7U6HnN45Vs8e0bESgw4GrCM2vkPQiJekjNx3hyDtUeRoYKbumxMOzrVOVf6_LPPT8XQihPJLH9fgBmUPthQrwMaCKYUrtxklun9cOtyuy2_fuvDVHSDSr7PhnimVAP0S161oQ_aclYJwVk6Vyp9wMezOpfiMGRyB7UAIYGR9Kh2Az7zRhSKMRNts_HUUFAhj', start_index=17897)
Annotation(end_index=17979, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJXIEjBXyUiPixcSaeDaEy9lbesYRNiBl2pgk3xzwvJ71uBv0lrTXrryOPL1DRMbG-b_xjYtpi2MJ6SgRHtd_bGEnRbeqtblHAsEphVDoy8tCwkMrDwpQNy6F4RNUJDUo=', start_index=17965)
Annotation(end_index=17979, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJsCiZ1vC_Smc_dyj922nt3ie01UCxD3z33Kif7n4QK7YW98piUnlSV22iIlJwRQwGlqHkzIspEzUubRx8qjyvdFasovzr7DftMPONByOK0yEHdvba4evFSvvN-Q64jJ0nADfuq-CQRCG7wmhRhuzL', start_index=17965)
Annotation(end_index=18035, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsAxjFE1bBX3Zax_gNKQLhOlpAkRZD_PUc8aEIry5PC7Qv4Kx6NNZ5tGUtCFWurBbDRkG8JtkulJ1l8xorRr4AS-SZrik-Df1r_858dszyU2WeNdEJ9IZn', start_index=18021)
Annotation(end_index=18035, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrnL0nM_U98uTaiBdoO7OiEtW8RzbLngeKy-H__XcLTN0SP_p5shmv9Idpm74JQZZ2-OvSAFMebfgJz3CiBIH7-WOAFGCx6bgOxIZ4j2zJSTuaTa1pv_jXi09pQK7nHYcEIUXO373rAiUJu_L0KVnTyIQCQaoe4MhOdgDHOSg5JZ4KDNuxTyChywUi', start_index=18021)
Annotation(end_index=18092, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHjSMsudVzDIvySDXPZz9fXGkRBkofyGMpjly_fMG7fj_1An7BQ5rvHrv60ItQaZg_HgR6gQMgQRRmJ2aBQ_HiB8cXezGrJBFG-2WGfDefu7qlM4LQPiooyUzGVFCV_zhY9B-VuSRTlW5yfS5Nkcuc7hT6NsBLFwi-TxecqXkGXINwNHdHjkrjHPT8usJTFdPg4ABfMnLSxQ8gWIwZDWL43aF3Cb7XTCdRejw=', start_index=18079)
Annotation(end_index=18092, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLaQkb5MO-GZncloanKF7VdRoO7eZHB7xKTOF2TvPSJRw9FImbsTbbNi2IW-eWY-KD5lwzBPfZgXcnAxDZ5fDZFqpAjcv9BwKff2ZUaWNFWUuZn7UB_2DJonehZdCLag9mSwjLy8MYZhThln2DNdzQZiT6ip6BlqvdUMWQo5FgLh74TCQaJoQ84E9cIC10ty5nzDSPUjA=', start_index=18079)
Annotation(end_index=18153, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEV46OmYHC2iX2BWacWZaFpxQj6YROt1GG1U1ibUTjOn6zOv8Y_KMrVdNWZ04IsSxYBubAVKkhFrqaXpdA1qCrYdaSzzdyyNS1O3x_Xu63cZvJ22mcqNXd7sTpAwZ8fDRu2-7-PcHPhg_cPl4XFRF4C8xWKB3KLs8_MiE5quV7_5A==', start_index=18140)
Annotation(end_index=18153, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvWTf4-rFMQOHBDIeWOp0I0rHnaGBdoqmiQN3E0_tIBWZk69zVaDMf8k9u65DTWSHxTX54D-i7PmMxvojpksloeX_sOVxEsDvinrRBMNphOB4uo7k=', start_index=18140)
Annotation(end_index=18211, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGN4GubYJANOZWASEnkAsaFpKRHPctrg7FRWJUmoZ5_uQ-djbIyIHVhLr7iP_1N3htao94ufJisC3Imc9Dmh_Vzpcdl3FCjXWlTOU4bc3I828lYK0wUGdjYG8g6gcpM7g_8Lc5IAPY3yrrMAQiWVcwsLdQEJhDkHOHZAZC6-1YFDnZkvJI0laAHe5G1cn6M4SFad5BP3s51AKZa-wZIU5Vy9YcAYvAiYUSyvG_9csM5CJhtk35Huh0Yq_tOmtabc6MsP6DVMXoOIDD6snip', start_index=18197)
Annotation(end_index=18211, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWprqVA8ykXFIHKRnvp8DcN3NRx-rGzz9U0LEM1wtzQyO3VAKNketPfhPpNR-Em3WqCG4xzQe8ldSEzUznCF4rdR5CHoWI9WxmG0QnGmwg53gaz85yKgsdz0uHIhE3I0Uu4XlGU6yK', start_index=18197)
Annotation(end_index=18271, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkf0NnsWCnqP82k_IDD7NZI1XZupmQYiUhcGgIe7ls1Ca8cLFTVqelD9L0Uz7jiGwZyo7ATuuVWOWvJITNmGuUsgBpAKs5sA-y6lUZZfNSuC5i3NW4LI9vBYFC-RqV7KXJOx_z51l5ESBAyvvTcshRafBa_y_Itl_h_4BCkJF-l-WlRhbirKrTWAa-6oKnocZUWppDlLC6sPnIgWfOkYLD0XvLRUI0PA==', start_index=18257)
Annotation(end_index=18271, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwQEhMZ8TFpVFzPVrBdehDgz0irs1J2cFU6T4vbBXpy-t1SgB0woKFA6Oief-zlifu-Uhw9eeIda-LkAE34Y6hVlyH1BnQGm5G1ni3SQhEJr80dm5_hr8oXHrb3mPWgl1PMHEww7_BmKqlwXnecQ==', start_index=18257)
Annotation(end_index=18331, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVfvX29OYFwyIX6ei7F7rhrd7GbbQNjxhYx1Nwq_2TWkwEi8GNsA9CVOcTnECBqusXh04kbfb6CgnOKCe326y1e4FcZII_D_uLpcvoQE6tq-_L1U3TwJB6MSLA_7UYT9PXAR50Vbp1v8XhJSx0Nx2g3xI57g6Uxwf9WAy7Xl-l2QUBCxWyk4st2AeifowwIGIVxsd2UyUJzs8=', start_index=18317)
Annotation(end_index=18331, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFR8N20WVXzcSLavRuB91hwbpdNNSyuRkJAGYtBU4Q0bwtNOdm-nJSm2dhZL6zT36zkwdEgzZNcTJrMdEiaSGBmHRvXj4Xg_9e_V_-fb6QUNOqrHYFKtWtSYG9Jk10zwBwihiWmJm13evjsm8TNd1QokbxXwgqCOPGD7JR8vKaUV-uzQP35BJbXlQ9j3umTRRJ2uy0AKx5vzrg-RZrAM2pOpvMRFk-C', start_index=18317)

## Sources
