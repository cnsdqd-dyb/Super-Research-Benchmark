# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 718533d0 | **Time:** 364.13s | **Cost:** $1.85395
--------------------------------------------------------------------------------

# Optimal Trade-offs in Computational Complexity and Signal Integrity for Optical Fiber Dispersion Compensation

### Key Points
*   **Linear Dispersion Regimes:** For large accumulated chromatic dispersion (typically >3000 ps/nm), Frequency Domain Equalization (FDE) using Overlap-Save or Overlap-Add methods offers the optimal trade-off, reducing complexity from $O(N^2)$ (Time Domain) to $O(N \log_2 N)$.
*   **Nonlinear Compensation (NLC):** Learned Digital Backpropagation (LDBP) represents the current state-of-the-art trade-off, achieving Q-factor gains of approximately 1.1 dB over linear equalization while maintaining computational complexity comparable to or lower than traditional Digital Backpropagation (DBP) by reducing the required steps per span.
*   **Short-Reach/IM-DD Systems:** For PAM4 and short-reach links, Time Domain Equalization (TDE) via Finite Impulse Response (FIR) filters remains optimal due to lower latency and overhead, provided that tap weights are optimized (e.g., via quantization or clustering) to minimize energy consumption.
*   **Hardware Constraints:** The optimal algorithm is heavily dependent on hardware precision; quantization to lower bit-depths (e.g., 16 quantization stages) can reduce multiplication operations by up to 99% in TDE architectures with only marginal signal integrity penalties (~5% BER increase).

---

## 1. Introduction

The exponential growth of global data traffic has necessitated the migration of optical transmission systems toward higher symbol rates and advanced modulation formats, such as Polarization-Division Multiplexed Quadrature Phase Shift Keying (PDM-QPSK) and Quadrature Amplitude Modulation (QAM). In these high-speed serial data streams, signal integrity is fundamentally compromised by physical impairments within the optical fiber, primarily Chromatic Dispersion (CD), Polarization Mode Dispersion (PMD), and fiber nonlinearities (Kerr effects). Historically, dispersion was managed in the optical domain using Dispersion Compensating Fibers (DCFs). However, the advent of coherent detection has enabled the compensation of these impairments in the electrical domain using Digital Signal Processing (DSP), offering greater flexibility and eliminating the insertion loss associated with DCFs [cite: 1, 2].

The central challenge in designing DSP for optical receivers is establishing an optimal trade-off between **computational complexity** (which dictates power consumption and hardware cost) and **signal integrity** (measured by Bit Error Rate (BER) or Q-factor). As transmission speeds increase (e.g., 112 Gbit/s to 800 Gbit/s and beyond), the memory length required to compensate for accumulated dispersion grows, imposing a severe computational burden on the DSP Application-Specific Integrated Circuits (ASICs) [cite: 1, 3].

This report provides a comprehensive analysis of the algorithmic landscape for dispersion compensation. It evaluates the comparative efficacy of Time Domain Equalization (TDE) versus Frequency Domain Equalization (FDE) for linear impairments, explores the emerging paradigm of machine-learning-enhanced algorithms for nonlinear compensation, and analyzes specific optimization strategies for Intensity Modulation/Direct Detection (IM/DD) systems.

---

## 2. Theoretical Foundations of Fiber Impairments

To understand the trade-offs in compensation algorithms, one must first characterize the physical impairments they address.

### 2.1 Chromatic Dispersion (CD)
Chromatic dispersion, or Group Velocity Dispersion (GVD), arises because the refractive index of the silica fiber is frequency-dependent. Different spectral components of a pulse travel at different velocities, causing pulse broadening and Inter-Symbol Interference (ISI). The transfer function of CD in the frequency domain, $H_{CD}(\omega)$, is typically modeled as an all-pass filter with a quadratic phase response:
\[
H_{CD}(\omega) = \exp\left(-j \frac{D \lambda^2 L}{4\pi c} \omega^2\right)
\]
where $D$ is the dispersion parameter (typically 17 ps/nm/km for Standard Single Mode Fiber), $\lambda$ is the carrier wavelength, $L$ is the fiber length, and $c$ is the speed of light [cite: 4]. The accumulated dispersion grows linearly with distance, necessitating digital filters with increasingly long impulse responses to reverse the phase rotation.

### 2.2 Fiber Nonlinearity
At high launch powers, the refractive index of the fiber becomes dependent on the optical intensity (the Kerr effect), leading to nonlinear phase shifts. These manifest as Self-Phase Modulation (SPM), Cross-Phase Modulation (XPM), and Four-Wave Mixing (FWM). Unlike CD, which is a linear distortion, nonlinearities are dependent on the signal power profile and interact with dispersion, making compensation significantly more computationally intensive [cite: 5, 6].

---

## 3. Linear Dispersion Compensation: Time vs. Frequency Domain

The compensation of Chromatic Dispersion (CD) constitutes the most computationally demanding linear block in a coherent receiver DSP chain. The choice between Time Domain Equalization (TDE) and Frequency Domain Equalization (FDE) is the primary architectural decision determining the complexity-performance trade-off.

### 3.1 Time Domain Equalization (TDE)
TDE is typically implemented using Finite Impulse Response (FIR) filters. The filter coefficients are calculated to approximate the inverse of the fiber's CD transfer function.
*   **Complexity Scaling:** The number of taps $N$ required for the FIR filter is proportional to the accumulated dispersion. For a given dispersion, the computational complexity of a direct convolution scales as $O(N^2)$ (or $O(N)$ per output sample if implemented efficiently, but the number of taps $N$ itself grows linearly with dispersion) [cite: 1, 7].
*   **Performance:** TDE offers precise compensation and low latency, making it suitable for systems with low accumulated dispersion. However, for long-haul transmission, the number of taps becomes prohibitive. For example, compensating 3000 ps/nm of dispersion requires a massive number of multipliers, leading to excessive power consumption [cite: 2].
*   **Optimization:** Recent research proposes "Clustered TDE" or quantized weight optimization. By optimizing filter coefficients using weighted quantization (e.g., $M=16$ quantization stages), the number of real number multiplications can be reduced by up to 99% compared to standard TDE, with only a 5% penalty in BER [cite: 7].

### 3.2 Frequency Domain Equalization (FDE)
FDE exploits the Convolution Theorem, performing filtering by multiplying the signal's spectrum with the inverse channel transfer function. This is implemented using Fast Fourier Transforms (FFT).
*   **Algorithms:** The two primary methods are Overlap-Save (OLS) and Overlap-Add (OLA). Both methods segment the continuous data stream into blocks, process them, and reconstruct the stream. Research indicates that OLA with zero-padding (OLA-ZP) achieves performance equivalent to OLS [cite: 1].
*   **Complexity Scaling:** The complexity of FDE is dominated by the FFT and IFFT operations, scaling as $O(N \log_2 N)$. This logarithmic scaling provides a decisive advantage over TDE for large values of $N$ [cite: 1, 7].
*   **The Crossover Point:** Comparative analyses consistently identify a crossover point where FDE becomes more efficient than TDE. This threshold is generally observed when accumulated dispersion exceeds approximately **3000 ps/nm** (roughly 175 km of standard fiber). Above this limit, FDE is significantly more efficient; below it, the overhead of the FFT blocks may make TDE or hybrid approaches preferable [cite: 2].

### 3.3 Comparative Summary
Table 1 summarizes the trade-offs based on the research findings [cite: 1, 3, 7, 8].

| Feature | Time Domain Equalization (TDE) | Frequency Domain Equalization (FDE) |
| :--- | :--- | :--- |
| **Complexity Scaling** | $O(N^2)$ (Direct convolution) | $O(N \log_2 N)$ (FFT-based) |
| **Optimal Use Case** | Short reach, low dispersion (< 2000-3000 ps/nm) | Long-haul, high dispersion (> 3000 ps/nm) |
| **Latency** | Low (sample-by-sample processing possible) | Higher (block processing latency) |
| **Resource Usage** | High multiplier count for large $N$ | Efficient use of resources for large $N$ |
| **Optimization** | Quantization/Clustering can reduce complexity by ~99% [cite: 7] | Block size optimization minimizes complexity [cite: 1] |

---

## 4. Nonlinear Compensation: The Complexity Frontier

While linear CD compensation is well-understood, mitigating fiber nonlinearities represents the cutting edge of DSP design. The trade-off here is stark: rigorous physical models provide high signal integrity but require immense computation, while simplified models may fail to capture complex signal interactions.

### 4.1 Digital Backpropagation (DBP)
DBP is the benchmark algorithm for nonlinearity compensation. It virtually reverses the propagation of the signal through the fiber by solving the inverse Nonlinear Schrödinger Equation (NLSE) using the Split-Step Fourier Method (SSFM).
*   **Mechanism:** The link is divided into small steps. In each step, linear effects (dispersion) and nonlinear effects (phase rotation) are compensated sequentially.
*   **Complexity:** The complexity is extremely high because it requires multiple FFT/IFFT pairs *per span* of fiber. For a long-haul link, this results in a computational load that is often impractical for real-time implementation [cite: 6, 9].
*   **Performance:** DBP offers the theoretical upper bound for performance but is limited by stochastic impairments like PMD and noise, which cannot be deterministically back-propagated [cite: 10].

### 4.2 Learned Digital Backpropagation (LDBP)
To address the complexity of DBP, researchers have applied Deep Learning (DL) to approximate the SSFM. This approach, known as Learned DBP (LDBP), interprets the steps of the SSFM as layers in a deep neural network.
*   **Architecture:** LDBP unrolls the SSFM into a neural network where the linear steps (dispersion filters) and nonlinear steps (phase shifts) are trainable parameters. This allows the network to "learn" the optimal parameters that minimize error, often requiring far fewer steps than the analytical SSFM [cite: 11, 12].
*   **Optimal Trade-off:**
    *   **Performance Gain:** In single-channel transmission, LDBP has demonstrated an effective Signal-to-Noise Ratio (SNR) improvement of **6.3 dB** over linear equalization and **2.5 dB** over conventional DBP. In WDM systems, Q-factor gains of **1.1 dB** (LDBP) vs 0.4 dB (DBP) have been reported [cite: 11, 13].
    *   **Complexity Reduction:** LDBP can achieve these gains with as few as **1 step per span** (or even fewer), whereas conventional DBP might require tens of steps per span to achieve similar accuracy. Complexity analysis reveals that a frequency-domain implementation of LDBP is significantly more favorable than time-domain implementations [cite: 11, 14].
    *   **Robustness:** LDBP has shown robustness against hardware impairments and can be trained to be blind to timing errors and state-of-polarization rotations [cite: 15].

### 4.3 Operator Learning and Neural Operators
Recent advancements include using Neural Operators to approximate the solution space of the Partial Differential Equations (PDEs) governing fiber transmission (Manakov equation).
*   **Low Complexity:** An inverse parameterized Manakov model based on neural operators has been validated over 12,075 km. It achieves performance similar to single-channel DBP (MSE of 0.0008) with a performance loss of only 0.024 dB, but with a highly parallel nature that significantly reduces computational latency [cite: 6, 12].

---

## 5. Short-Reach and IM/DD Systems (PAM4)

In short-reach applications (e.g., intra-datacenter interconnects), the cost and power constraints are even tighter. Coherent detection is often too expensive, so Intensity Modulation/Direct Detection (IM/DD) with Pulse Amplitude Modulation (PAM4) is the standard.

### 5.1 Challenges in PAM4
PAM4 is highly sensitive to dispersion and ISI. Unlike coherent systems, IM/DD systems lose phase information, making electronic dispersion compensation (EDC) more challenging.
*   **Compensation Strategy:** The optimal trade-off often involves a combination of **Pre-Electronic Dispersion Compensation (Pre-EDC)** at the transmitter and **Feed-Forward Equalization (FFE)** at the receiver.
*   **Complexity vs. Performance:**
    *   **Pre-EDC:** Iterative algorithms (like Gerchberg-Saxton) at the transmitter can pre-distort the signal to counteract dispersion. Research shows that 5 iterations of such an algorithm can extend the reach of 28 Gbaud OOK to 100 km and PAM4 to 10 km [cite: 16, 17].
    *   **Receiver FFE:** A trade-off exists between the number of FFE taps and BER. Experimental demonstrations indicate that a **5-tap post-FFE** is often sufficient to bring the BER below the Forward Error Correction (FEC) threshold, representing a "sweet spot" for complexity [cite: 18, 19]. Increasing taps beyond this yields diminishing returns.

### 5.2 End-to-End Autoencoders
For IM/DD systems, end-to-End (E2E) learning using autoencoders has been proposed. These systems treat the transmitter, channel, and receiver as a single neural network to be jointly optimized.
*   **Performance:** E2E autoencoders have demonstrated significantly lower BER compared to conventional EDC algorithms (LMS/MLSE) in high-dispersion scenarios.
*   **Complexity:** By employing square-law detectors and optimizing the network structure, these systems can reduce the complexity of the receiver while handling the nonlinearities of the direct detection channel [cite: 20, 21].

---

## 6. Hardware Implementation and Energy Efficiency

The theoretical complexity of an algorithm ($O(N)$) does not always map linearly to energy consumption. Hardware-specific factors such as memory access, quantization, and parallelism play crucial roles.

### 6.1 Quantization and Precision
Reducing the bit-precision of DSP calculations is one of the most effective ways to reduce power.
*   **Impact:** Research on "Chirp-Filtering" and quantized FIR filters shows that reducing quantization stages to $M=16$ allows for a 99% reduction in multiplication operations compared to full-precision implementations, with minimal impact on BER [cite: 7].
*   **Trade-off:** The trade-off here is between the **quantization noise floor** and **logic gate count**. For dispersion compensation, the coefficients of the filters can often be heavily quantized because the filter response (all-pass) is well-behaved and predictable.

### 6.2 Frequency Domain Implementation Details
While FDE is computationally efficient, it introduces block latency and requires overlap overhead.
*   **Overlap Methods:** The Overlap-Save (OLS) and Overlap-Add (OLA) methods are standard. OLA with Zero Padding (OLA-ZP) has been shown to achieve acceptable performance with potentially simpler memory management than OLS [cite: 1].
*   **FFT Size:** There is an optimum FFT length that minimizes complexity for a given dispersion. If the FFT is too small, the overlap overhead dominates; if too large, the logarithmic complexity growth and memory requirements take over. Deriving this optimum is critical for ASIC design [cite: 1].

---

## 7. Conclusion

The determination of the optimal trade-off between computational complexity and signal integrity for optical fiber dispersion compensation is not a singular solution but a decision matrix dependent on the transmission regime.

1.  **For Long-Haul Coherent Systems (> 1000 km):**
    *   **Linear Compensation:** **Frequency Domain Equalization (FDE)** is the undisputed optimal choice for chromatic dispersion. It offers superior efficiency ($O(N \log N)$) once accumulated dispersion exceeds ~3000 ps/nm.
    *   **Nonlinear Compensation:** **Learned Digital Backpropagation (LDBP)** represents the current optimal frontier. It provides significant Q-factor gains (~1.1 dB) over linear methods and reduces the computational complexity of traditional DBP by optimizing step sizes and parameters via neural networks, effectively enabling "1-step-per-span" compensation.

2.  **For Short-Reach/Metro Systems (< 100 km):**
    *   **Linear Compensation:** **Time Domain Equalization (TDE)** remains relevant, particularly when enhanced by **clustering and quantization** techniques. The lower latency and lack of block-processing overhead make it suitable for delay-sensitive applications.
    *   **IM/DD Optimization:** A combination of **Pre-EDC** (transmitter side) and short-tap **FFE** (receiver side, ~5 taps) offers the best balance, extending reach without the massive power cost of coherent DSP.

3.  **Future Directions:**
    *   The integration of **Neural Operators** and **End-to-End Autoencoders** suggests a move toward "black-box" optimization, where the DSP learns the inverse channel function dynamically. The trade-off will increasingly shift toward training complexity (offline) to minimize inference complexity (real-time/online), allowing for highly efficient, low-power ASICs that maintain high signal integrity in increasingly nonlinear fiber regimes.

### References
[cite: 1] *Time domain vs frequency domain equalization chromatic dispersion complexity* [cite: 1]
[cite: 3] *Complexity of digital chromatic dispersion equalization using three different approaches* [cite: 3]
[cite: 7] *Low-complexity chromatic dispersion equalizer based on FIR filter architecture* [cite: 7]
[cite: 2] *Comparative analysis of three popular digital filters for chromatic dispersion compensation* [cite: 2]
[cite: 11] *Learned digital back-propagation (LDBP) for equalizing dual-polarization fiber-optic transmission* [cite: 11]
[cite: 6] *Low-Complexity Fiber Nonlinearity Compensation Based on Operator Learning* [cite: 6]
[cite: 20] *End-to-end autoencoder for chromatic dispersion compensation* [cite: 20]
[cite: 7] *Comparison of TD-CDE and FD-CDE complexity* [cite: 7]
[cite: 18] *IM/DD dispersion compensation algorithms complexity trade-off* [cite: 18]
[cite: 8] *Review of dispersion compensation algorithms in long-distance fiber optic transmission* [cite: 8]
[cite: 14] *Learned Digital Backpropagation LDBP vs DBP computational complexity* [cite: 14]
[cite: 13] *Equalization in dispersion-managed systems using learned digital back-propagation* [cite: 13]
[cite: 7] *Computational complexity reductions of the proposed FIR filter* [cite: 7]

**Sources:**
1. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp2IAG0AL2U2CXUDu-rgvZDtAClu2T4s9EFVq-O26GLEgG8s7IEQrDT5_c5jtgE5wbIqUGASK0KfDuej9IaQZFGNL0u4h0v51G_kXupOFD6zYLdn4sAg==)
2. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYRiVPOROQK8eWscQkBqwZwm6zBgnaWORi2-h2zs0HQIAeMZ5Cl-bTTUQZtH3JHbV08iUD-47X2ETLuvfi37OO6F9dFxJx4ytKqaGzlXf21OVWxQA2hPvDA80z6INz38SrxBbiYLY7xLUUX5EktYQ=)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEb9gHwdQAcN75Fva4xOhh-7_y2GIJvA5JVA-Diy-mNudUO9mT50hKSERnqBa5GeZXL49YoxCzJFHlcytKmA_9WGsZ6RLeopGoVErkUPJLCfOJ8ECwTmD_YvZdtD0Wlq0OhpI0e3v_R71-7Yhg6jZB64-hVDLvyX0FiU44CT8xtduyuOa2bflv8eQ_qJE-sEKvzawZh8DeAh01LeXodEvqr_1kWwi1KT-z_0r08rkGX4Gdn8oUFqL22ng64GtI-oYvZZg==)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0KyEVsiFk2lLbJCqzHAxemQrhrU1F7Fp1t6Wvoue6IEY0GPyWfGfYay6HccijbVPAbofoUH9E7rdOKQCNYYmCBeygc6A6PfMvNotAQgs4fpR6TF1W-Fi5yXuv2KaGgx92oVYocX-f42uOK5wXAAftjEdE777qWNE0hY39yr8CDgdJX61cRABxp3ZCBIdKHVo0c3IRhLBWBHy44SWJsEpfOtpfNO0sR6BnMepNz_J3lpWaBK8PNbYzhvLb9uMKP-RFHbR8UyFRMN2ke96KgeHI)
5. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_fqPwkfy7c-LFlAK8BhoTelL67EZjKhIHMuoj_odxGDJFp-oozXRf4Kc4tPd9MJUPU0XkZyzI80JjVwx7cwWhcctV9kFARFHfmC-lRXk8p_iv0cfXSWIPTTR7pPQxg0aouZCWakDmhKwmJHVXr-EQoQEc54iQpyGnRTPRQg==)
6. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDCNI7FjNjawDKU_Tj4WImkTReWG0DzNBA06iNTa-QejrM6AbRVT6xfDRFCbaQJZ6k6GfCz5oMkTXC8Gs9lLy0z3QbzArwAOFsd5KwLfb6Lai5mw31gGPag-yZzTrMpOdP6ZlL)
7. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhuiFrZPSVbqz0HeTstDQyCr81O9iH9ce8yYUxfhJCUEiGzdE64DG8lKfk3f0kmbYR8_1sIigieRnQPatfN-jMCPVvO3eTv1jgLbZIvISgSFxXCs5ouAzVj2x04g==)
8. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUeb9CJlYEu15GaNaFy0UgQDDH5QllWnn-szw2SZgPurT4NlHSMR11XfgPfumgmFauudvozYGWgnygRlixz5n_Hnq36yDsPGqxxqGzk2JUG6O28y2pwyG6WB1BsA==)
9. [researching.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHP4UoSTi_NpBqKXx9WH0W9aFs6_BXMQ9Gi2vBwQP3OkvIIHzpHTdZ1DH21JPwcmdD8UwK3fsUJ_zNUvwzyaFXUidCH9TpF_DM5qMo_YXrO-0R_clRgidD2H7AJyX4jlvnnb4jn2soEdIR3kjI=)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqWahlc619M8PUTbiTS8syBzpx5CeIHectM_pI5mHDtB3qHZROpZqy3CjXt2K7RZ7JIa_VAjFew9qvn2b2cCwfNcweYp2XeoC6foJHc9O2RcBM4NOUkIPs7rsId-BMtX8aIgWNPlvY6yRwRUhhSyCVvkHXZnUzKQCNWm7rABvrfkt3EG498m8Tc0Ed6WYdTK7tzf39KmfHc6akG6_q90YJFDKR0jDmXtBJyuET)
11. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFddTZYeBh432AOSg9np5-vgcJq2ZwUeYe2pfe9YJHhvInTsX2oMlL0bJLswQZUq4opPRDA0yjx-Ci0hPkLOjsqbzQHSPS66ukirXcHMSvlbA6QcODEzw==)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEt_MvdRtWm4UbPyHwEkjt9FMsN41aHz1l2g_Uends84czuxVPWLeJNWzBluT92XvGVjOLEezmkP8c-EVOuuc_17JBtxbHTO4kBVjt1SbJbFq4Bx-x0a6jKwbvgvzRpflKg3-2bLowDkVEtQ7JvSp6XfMx3HylqzBUKpz9cu4wmugqLUHfuQfKssPvBoGRgQB5mQAdw2ve_4tOq3UGHfQIl_PuteLHdLNDLdqSQrdVkk3-bvuRP8qLMQxTdwCBVc6xCZWwq4Qn5qp6VIL-DcJuF6lFgMg==)
13. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkXGHmBEcPc2gxY1LMOWtvdOdJfLoEiOo7dbORmrrTkXUN-IfEiQXKSjzAkmgVUYjSzFarBGPr7-YnTPQBzAehFCyl4QG2LCYvRUMFUmCyyX0Bqugutx3mcxcpabU2h6NjMxySGTrW_OW6dxLBtv1BvxLbL_fQfPJlxV08uuRszMuEViPNPepaCcYKmn00c6nsOqHUoemPK33nNuum8fKp6bQlLYKsrS1fnTZdhizmqZChXldB4hkwEHS6)
14. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqyu4seGHTqE5uwVXVVUiOiXujKJMButwNLVIk8tsZUQBocGXoKgungTY_EZoKIb5vlqZDc9UCA4AwCQhBFweVVsFQsi_WqKPWBGF9_fk40CehgBInAcoUyZ3MZUqll1jwnShbAFXesVY4gb6MOA==)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8UUnyw903MR3sivGVluaq3EuAc_ZFBcn5j73_rEVE44j9WjUsMD9m0Oo_BB_--bcdCiDswdPe9i1hAXmUc55L8l9r_P4arGyTN_WnSARmVfvBqGpyNAyT0Y6g_9gsYV0DmFTpVdctWQYeTbOu-mjUKaMBsP--Q0wglSShXrWXD7VIjGSwbsP9BwaPUv3VG4gCdW3MxqgQi05A4hcUU3rweR6-GYm06BlY2sONnQDnrrsHZRCNqOnVoqPOFwtAlBq7TFCb1oMiUakrMoh9IgJbelI66WfJe8_jIpdOUw==)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYcUalWSe6JZzZCx_X0ObNRrYX2D4_XGydL5Gf9TEGMcM9Zm49vXn-YhPBlNZlVHpZ_IKAwAcOxL8vpauyUuEAiy8zUqtVrB1PArkycoVABLhrNx_8Nq_6s35h4cNK_-BHT2WYAjhaFn2oCcODMTlPH_x-jp8NE-I2LPskc48C5AWbLb6g5snXKJwmzLtYMJBwXYcgzF0OUHs36j84DZGg5hHx4m-WuD4dxfiOh41QMAu_IQ==)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlECT3ImfefsNmlS9RusWllqlCn2JKcOxevs6S1sz-THPv4FpA0u-z-vmf9apsYdwTNZZ50mKkyaFNcIrWl9C9mbBj0gklpo9mUOy-0OUf9we0plGeMzzEtJ9rdlwzpkh1yQAK7KjB_yQyuJ5LgcxVVQ-PwviORSc_5ZWnUVAckBrEIAg1I6I2NmBr44mfm1yfPJzcpjqymaOX2NwmMy4oPPkBXMscbeqgLKf_GYgBq_L-14wMGTN3QUzzmjVYCTE3l3dh2lRjhLwZfCS7Vy8AAHPhqBA1f52nCa4=)
18. [optica.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPfgVPVwuzi-SHnkf2mjJxocM6D3DPzzElxCzPSzSkd9swVQQU5h4qa6ef53fMFnq4h2yUzk4xAerw3fly76BGus-Z9989F12hp2K_f3IDN36Nhr8O6N7P7f0kHsjzrtCbbaX53_YXAdZh-Ew=)
19. [polyu.edu.hk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdR2HtNwWsyyODDj_Qs4sfzrIu2UTysrOmtwaPC6XkAWEQD8PIcwNMrX26RSM1ROu9wkRbWZ5yKl5_0uaZrt9vd3hIqgVg2tmM5WCUIc3E2ak0MpgYWa-kMw5e7SaHelsMZ3XeGlWi1BM8Y9Ohj3oribuxZSIdAVU4Pxcaxg==)
20. [nju.edu.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHC3VrcYYB71rkNajVYXX3keTmrWltAqERxUpwNJV6DCFbE7gQ4gxoL_0eVjgSrX2DqJcUtApzuR6XycQb7EoBx5JASJjrmU-zdIq1IMzQ7pJy4LZdbxPhMjUJdLxg9ZqsPS6BA_NXEx6qe3vbaPwUHRCfv-EMTfR_fNPyQ1zNgtQ==)
21. [nju.edu.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjQUmN2wFs8leoPWqBLRe_QskN6zdKTuK2qZGk9hOpNSO2LS_DOh9DO_hNtBcwEgRq9Vaz4tiztDl9HBRlie4NVbPLqGvSyqc99Rh-6voTX1ZSMq2jxdgS2BJAB9-XNPqaypvQMh3Ln401l6r-JfK7Prz2N3X2xase3-YjRPD-Kw==)


## Annotations
Annotation(end_index=2291, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYRiVPOROQK8eWscQkBqwZwm6zBgnaWORi2-h2zs0HQIAeMZ5Cl-bTTUQZtH3JHbV08iUD-47X2ETLuvfi37OO6F9dFxJx4ytKqaGzlXf21OVWxQA2hPvDA80z6INz38SrxBbiYLY7xLUUX5EktYQ=', start_index=2279)
Annotation(end_index=2291, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp2IAG0AL2U2CXUDu-rgvZDtAClu2T4s9EFVq-O26GLEgG8s7IEQrDT5_c5jtgE5wbIqUGASK0KfDuej9IaQZFGNL0u4h0v51G_kXupOFD6zYLdn4sAg==', start_index=2279)
Annotation(end_index=2818, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEb9gHwdQAcN75Fva4xOhh-7_y2GIJvA5JVA-Diy-mNudUO9mT50hKSERnqBa5GeZXL49YoxCzJFHlcytKmA_9WGsZ6RLeopGoVErkUPJLCfOJ8ECwTmD_YvZdtD0Wlq0OhpI0e3v_R71-7Yhg6jZB64-hVDLvyX0FiU44CT8xtduyuOa2bflv8eQ_qJE-sEKvzawZh8DeAh01LeXodEvqr_1kWwi1KT-z_0r08rkGX4Gdn8oUFqL22ng64GtI-oYvZZg==', start_index=2806)
Annotation(end_index=2818, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp2IAG0AL2U2CXUDu-rgvZDtAClu2T4s9EFVq-O26GLEgG8s7IEQrDT5_c5jtgE5wbIqUGASK0KfDuej9IaQZFGNL0u4h0v51G_kXupOFD6zYLdn4sAg==', start_index=2806)
Annotation(end_index=4181, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0KyEVsiFk2lLbJCqzHAxemQrhrU1F7Fp1t6Wvoue6IEY0GPyWfGfYay6HccijbVPAbofoUH9E7rdOKQCNYYmCBeygc6A6PfMvNotAQgs4fpR6TF1W-Fi5yXuv2KaGgx92oVYocX-f42uOK5wXAAftjEdE777qWNE0hY39yr8CDgdJX61cRABxp3ZCBIdKHVo0c3IRhLBWBHy44SWJsEpfOtpfNO0sR6BnMepNz_J3lpWaBK8PNbYzhvLb9uMKP-RFHbR8UyFRMN2ke96KgeHI', start_index=4172)
Annotation(end_index=4834, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDCNI7FjNjawDKU_Tj4WImkTReWG0DzNBA06iNTa-QejrM6AbRVT6xfDRFCbaQJZ6k6GfCz5oMkTXC8Gs9lLy0z3QbzArwAOFsd5KwLfb6Lai5mw31gGPag-yZzTrMpOdP6ZlL', start_index=4822)
Annotation(end_index=4834, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_fqPwkfy7c-LFlAK8BhoTelL67EZjKhIHMuoj_odxGDJFp-oozXRf4Kc4tPd9MJUPU0XkZyzI80JjVwx7cwWhcctV9kFARFHfmC-lRXk8p_iv0cfXSWIPTTR7pPQxg0aouZCWakDmhKwmJHVXr-EQoQEc54iQpyGnRTPRQg==', start_index=4822)
Annotation(end_index=5799, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhuiFrZPSVbqz0HeTstDQyCr81O9iH9ce8yYUxfhJCUEiGzdE64DG8lKfk3f0kmbYR8_1sIigieRnQPatfN-jMCPVvO3eTv1jgLbZIvISgSFxXCs5ouAzVj2x04g==', start_index=5787)
Annotation(end_index=5799, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp2IAG0AL2U2CXUDu-rgvZDtAClu2T4s9EFVq-O26GLEgG8s7IEQrDT5_c5jtgE5wbIqUGASK0KfDuej9IaQZFGNL0u4h0v51G_kXupOFD6zYLdn4sAg==', start_index=5787)
Annotation(end_index=6153, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYRiVPOROQK8eWscQkBqwZwm6zBgnaWORi2-h2zs0HQIAeMZ5Cl-bTTUQZtH3JHbV08iUD-47X2ETLuvfi37OO6F9dFxJx4ytKqaGzlXf21OVWxQA2hPvDA80z6INz38SrxBbiYLY7xLUUX5EktYQ=', start_index=6144)
Annotation(end_index=6485, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhuiFrZPSVbqz0HeTstDQyCr81O9iH9ce8yYUxfhJCUEiGzdE64DG8lKfk3f0kmbYR8_1sIigieRnQPatfN-jMCPVvO3eTv1jgLbZIvISgSFxXCs5ouAzVj2x04g==', start_index=6476)
Annotation(end_index=7025, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp2IAG0AL2U2CXUDu-rgvZDtAClu2T4s9EFVq-O26GLEgG8s7IEQrDT5_c5jtgE5wbIqUGASK0KfDuej9IaQZFGNL0u4h0v51G_kXupOFD6zYLdn4sAg==', start_index=7016)
Annotation(end_index=7250, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhuiFrZPSVbqz0HeTstDQyCr81O9iH9ce8yYUxfhJCUEiGzdE64DG8lKfk3f0kmbYR8_1sIigieRnQPatfN-jMCPVvO3eTv1jgLbZIvISgSFxXCs5ouAzVj2x04g==', start_index=7238)
Annotation(end_index=7250, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp2IAG0AL2U2CXUDu-rgvZDtAClu2T4s9EFVq-O26GLEgG8s7IEQrDT5_c5jtgE5wbIqUGASK0KfDuej9IaQZFGNL0u4h0v51G_kXupOFD6zYLdn4sAg==', start_index=7238)
Annotation(end_index=7673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYRiVPOROQK8eWscQkBqwZwm6zBgnaWORi2-h2zs0HQIAeMZ5Cl-bTTUQZtH3JHbV08iUD-47X2ETLuvfi37OO6F9dFxJx4ytKqaGzlXf21OVWxQA2hPvDA80z6INz38SrxBbiYLY7xLUUX5EktYQ=', start_index=7664)
Annotation(end_index=7787, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEb9gHwdQAcN75Fva4xOhh-7_y2GIJvA5JVA-Diy-mNudUO9mT50hKSERnqBa5GeZXL49YoxCzJFHlcytKmA_9WGsZ6RLeopGoVErkUPJLCfOJ8ECwTmD_YvZdtD0Wlq0OhpI0e3v_R71-7Yhg6jZB64-hVDLvyX0FiU44CT8xtduyuOa2bflv8eQ_qJE-sEKvzawZh8DeAh01LeXodEvqr_1kWwi1KT-z_0r08rkGX4Gdn8oUFqL22ng64GtI-oYvZZg==', start_index=7769)
Annotation(end_index=7787, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhuiFrZPSVbqz0HeTstDQyCr81O9iH9ce8yYUxfhJCUEiGzdE64DG8lKfk3f0kmbYR8_1sIigieRnQPatfN-jMCPVvO3eTv1jgLbZIvISgSFxXCs5ouAzVj2x04g==', start_index=7769)
Annotation(end_index=7787, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUeb9CJlYEu15GaNaFy0UgQDDH5QllWnn-szw2SZgPurT4NlHSMR11XfgPfumgmFauudvozYGWgnygRlixz5n_Hnq36yDsPGqxxqGzk2JUG6O28y2pwyG6WB1BsA==', start_index=7769)
Annotation(end_index=7787, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp2IAG0AL2U2CXUDu-rgvZDtAClu2T4s9EFVq-O26GLEgG8s7IEQrDT5_c5jtgE5wbIqUGASK0KfDuej9IaQZFGNL0u4h0v51G_kXupOFD6zYLdn4sAg==', start_index=7769)
Annotation(end_index=8389, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhuiFrZPSVbqz0HeTstDQyCr81O9iH9ce8yYUxfhJCUEiGzdE64DG8lKfk3f0kmbYR8_1sIigieRnQPatfN-jMCPVvO3eTv1jgLbZIvISgSFxXCs5ouAzVj2x04g==', start_index=8380)
Annotation(end_index=8446, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp2IAG0AL2U2CXUDu-rgvZDtAClu2T4s9EFVq-O26GLEgG8s7IEQrDT5_c5jtgE5wbIqUGASK0KfDuej9IaQZFGNL0u4h0v51G_kXupOFD6zYLdn4sAg==', start_index=8437)
Annotation(end_index=9513, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDCNI7FjNjawDKU_Tj4WImkTReWG0DzNBA06iNTa-QejrM6AbRVT6xfDRFCbaQJZ6k6GfCz5oMkTXC8Gs9lLy0z3QbzArwAOFsd5KwLfb6Lai5mw31gGPag-yZzTrMpOdP6ZlL', start_index=9501)
Annotation(end_index=9513, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHP4UoSTi_NpBqKXx9WH0W9aFs6_BXMQ9Gi2vBwQP3OkvIIHzpHTdZ1DH21JPwcmdD8UwK3fsUJ_zNUvwzyaFXUidCH9TpF_DM5qMo_YXrO-0R_clRgidD2H7AJyX4jlvnnb4jn2soEdIR3kjI=', start_index=9501)
Annotation(end_index=9712, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqWahlc619M8PUTbiTS8syBzpx5CeIHectM_pI5mHDtB3qHZROpZqy3CjXt2K7RZ7JIa_VAjFew9qvn2b2cCwfNcweYp2XeoC6foJHc9O2RcBM4NOUkIPs7rsId-BMtX8aIgWNPlvY6yRwRUhhSyCVvkHXZnUzKQCNWm7rABvrfkt3EG498m8Tc0Ed6WYdTK7tzf39KmfHc6akG6_q90YJFDKR0jDmXtBJyuET', start_index=9702)
Annotation(end_index=10299, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEt_MvdRtWm4UbPyHwEkjt9FMsN41aHz1l2g_Uends84czuxVPWLeJNWzBluT92XvGVjOLEezmkP8c-EVOuuc_17JBtxbHTO4kBVjt1SbJbFq4Bx-x0a6jKwbvgvzRpflKg3-2bLowDkVEtQ7JvSp6XfMx3HylqzBUKpz9cu4wmugqLUHfuQfKssPvBoGRgQB5mQAdw2ve_4tOq3UGHfQIl_PuteLHdLNDLdqSQrdVkk3-bvuRP8qLMQxTdwCBVc6xCZWwq4Qn5qp6VIL-DcJuF6lFgMg==', start_index=10285)
Annotation(end_index=10299, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFddTZYeBh432AOSg9np5-vgcJq2ZwUeYe2pfe9YJHhvInTsX2oMlL0bJLswQZUq4opPRDA0yjx-Ci0hPkLOjsqbzQHSPS66ukirXcHMSvlbA6QcODEzw==', start_index=10285)
Annotation(end_index=10643, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkXGHmBEcPc2gxY1LMOWtvdOdJfLoEiOo7dbORmrrTkXUN-IfEiQXKSjzAkmgVUYjSzFarBGPr7-YnTPQBzAehFCyl4QG2LCYvRUMFUmCyyX0Bqugutx3mcxcpabU2h6NjMxySGTrW_OW6dxLBtv1BvxLbL_fQfPJlxV08uuRszMuEViPNPepaCcYKmn00c6nsOqHUoemPK33nNuum8fKp6bQlLYKsrS1fnTZdhizmqZChXldB4hkwEHS6', start_index=10629)
Annotation(end_index=10643, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFddTZYeBh432AOSg9np5-vgcJq2ZwUeYe2pfe9YJHhvInTsX2oMlL0bJLswQZUq4opPRDA0yjx-Ci0hPkLOjsqbzQHSPS66ukirXcHMSvlbA6QcODEzw==', start_index=10629)
Annotation(end_index=11005, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFddTZYeBh432AOSg9np5-vgcJq2ZwUeYe2pfe9YJHhvInTsX2oMlL0bJLswQZUq4opPRDA0yjx-Ci0hPkLOjsqbzQHSPS66ukirXcHMSvlbA6QcODEzw==', start_index=10991)
Annotation(end_index=11005, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqyu4seGHTqE5uwVXVVUiOiXujKJMButwNLVIk8tsZUQBocGXoKgungTY_EZoKIb5vlqZDc9UCA4AwCQhBFweVVsFQsi_WqKPWBGF9_fk40CehgBInAcoUyZ3MZUqll1jwnShbAFXesVY4gb6MOA==', start_index=10991)
Annotation(end_index=11180, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8UUnyw903MR3sivGVluaq3EuAc_ZFBcn5j73_rEVE44j9WjUsMD9m0Oo_BB_--bcdCiDswdPe9i1hAXmUc55L8l9r_P4arGyTN_WnSARmVfvBqGpyNAyT0Y6g_9gsYV0DmFTpVdctWQYeTbOu-mjUKaMBsP--Q0wglSShXrWXD7VIjGSwbsP9BwaPUv3VG4gCdW3MxqgQi05A4hcUU3rweR6-GYm06BlY2sONnQDnrrsHZRCNqOnVoqPOFwtAlBq7TFCb1oMiUakrMoh9IgJbelI66WfJe8_jIpdOUw==', start_index=11170)
Annotation(end_index=11741, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEt_MvdRtWm4UbPyHwEkjt9FMsN41aHz1l2g_Uends84czuxVPWLeJNWzBluT92XvGVjOLEezmkP8c-EVOuuc_17JBtxbHTO4kBVjt1SbJbFq4Bx-x0a6jKwbvgvzRpflKg3-2bLowDkVEtQ7JvSp6XfMx3HylqzBUKpz9cu4wmugqLUHfuQfKssPvBoGRgQB5mQAdw2ve_4tOq3UGHfQIl_PuteLHdLNDLdqSQrdVkk3-bvuRP8qLMQxTdwCBVc6xCZWwq4Qn5qp6VIL-DcJuF6lFgMg==', start_index=11728)
Annotation(end_index=11741, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDCNI7FjNjawDKU_Tj4WImkTReWG0DzNBA06iNTa-QejrM6AbRVT6xfDRFCbaQJZ6k6GfCz5oMkTXC8Gs9lLy0z3QbzArwAOFsd5KwLfb6Lai5mw31gGPag-yZzTrMpOdP6ZlL', start_index=11728)
Annotation(end_index=12784, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYcUalWSe6JZzZCx_X0ObNRrYX2D4_XGydL5Gf9TEGMcM9Zm49vXn-YhPBlNZlVHpZ_IKAwAcOxL8vpauyUuEAiy8zUqtVrB1PArkycoVABLhrNx_8Nq_6s35h4cNK_-BHT2WYAjhaFn2oCcODMTlPH_x-jp8NE-I2LPskc48C5AWbLb6g5snXKJwmzLtYMJBwXYcgzF0OUHs36j84DZGg5hHx4m-WuD4dxfiOh41QMAu_IQ==', start_index=12770)
Annotation(end_index=12784, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlECT3ImfefsNmlS9RusWllqlCn2JKcOxevs6S1sz-THPv4FpA0u-z-vmf9apsYdwTNZZ50mKkyaFNcIrWl9C9mbBj0gklpo9mUOy-0OUf9we0plGeMzzEtJ9rdlwzpkh1yQAK7KjB_yQyuJ5LgcxVVQ-PwviORSc_5ZWnUVAckBrEIAg1I6I2NmBr44mfm1yfPJzcpjqymaOX2NwmMy4oPPkBXMscbeqgLKf_GYgBq_L-14wMGTN3QUzzmjVYCTE3l3dh2lRjhLwZfCS7Vy8AAHPhqBA1f52nCa4=', start_index=12770)
Annotation(end_index=13080, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdR2HtNwWsyyODDj_Qs4sfzrIu2UTysrOmtwaPC6XkAWEQD8PIcwNMrX26RSM1ROu9wkRbWZ5yKl5_0uaZrt9vd3hIqgVg2tmM5WCUIc3E2ak0MpgYWa-kMw5e7SaHelsMZ3XeGlWi1BM8Y9Ohj3oribuxZSIdAVU4Pxcaxg==', start_index=13066)
Annotation(end_index=13080, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPfgVPVwuzi-SHnkf2mjJxocM6D3DPzzElxCzPSzSkd9swVQQU5h4qa6ef53fMFnq4h2yUzk4xAerw3fly76BGus-Z9989F12hp2K_f3IDN36Nhr8O6N7P7f0kHsjzrtCbbaX53_YXAdZh-Ew=', start_index=13066)
Annotation(end_index=13754, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHC3VrcYYB71rkNajVYXX3keTmrWltAqERxUpwNJV6DCFbE7gQ4gxoL_0eVjgSrX2DqJcUtApzuR6XycQb7EoBx5JASJjrmU-zdIq1IMzQ7pJy4LZdbxPhMjUJdLxg9ZqsPS6BA_NXEx6qe3vbaPwUHRCfv-EMTfR_fNPyQ1zNgtQ==', start_index=13740)
Annotation(end_index=13754, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjQUmN2wFs8leoPWqBLRe_QskN6zdKTuK2qZGk9hOpNSO2LS_DOh9DO_hNtBcwEgRq9Vaz4tiztDl9HBRlie4NVbPLqGvSyqc99Rh-6voTX1ZSMq2jxdgS2BJAB9-XNPqaypvQMh3Ln401l6r-JfK7Prz2N3X2xase3-YjRPD-Kw==', start_index=13740)
Annotation(end_index=14410, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhuiFrZPSVbqz0HeTstDQyCr81O9iH9ce8yYUxfhJCUEiGzdE64DG8lKfk3f0kmbYR8_1sIigieRnQPatfN-jMCPVvO3eTv1jgLbZIvISgSFxXCs5ouAzVj2x04g==', start_index=14401)
Annotation(end_index=15065, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp2IAG0AL2U2CXUDu-rgvZDtAClu2T4s9EFVq-O26GLEgG8s7IEQrDT5_c5jtgE5wbIqUGASK0KfDuej9IaQZFGNL0u4h0v51G_kXupOFD6zYLdn4sAg==', start_index=15056)
Annotation(end_index=15365, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp2IAG0AL2U2CXUDu-rgvZDtAClu2T4s9EFVq-O26GLEgG8s7IEQrDT5_c5jtgE5wbIqUGASK0KfDuej9IaQZFGNL0u4h0v51G_kXupOFD6zYLdn4sAg==', start_index=15356)
Annotation(end_index=17291, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp2IAG0AL2U2CXUDu-rgvZDtAClu2T4s9EFVq-O26GLEgG8s7IEQrDT5_c5jtgE5wbIqUGASK0KfDuej9IaQZFGNL0u4h0v51G_kXupOFD6zYLdn4sAg==', start_index=17282)
Annotation(end_index=17380, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGp2IAG0AL2U2CXUDu-rgvZDtAClu2T4s9EFVq-O26GLEgG8s7IEQrDT5_c5jtgE5wbIqUGASK0KfDuej9IaQZFGNL0u4h0v51G_kXupOFD6zYLdn4sAg==', start_index=17371)
Annotation(end_index=17390, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEb9gHwdQAcN75Fva4xOhh-7_y2GIJvA5JVA-Diy-mNudUO9mT50hKSERnqBa5GeZXL49YoxCzJFHlcytKmA_9WGsZ6RLeopGoVErkUPJLCfOJ8ECwTmD_YvZdtD0Wlq0OhpI0e3v_R71-7Yhg6jZB64-hVDLvyX0FiU44CT8xtduyuOa2bflv8eQ_qJE-sEKvzawZh8DeAh01LeXodEvqr_1kWwi1KT-z_0r08rkGX4Gdn8oUFqL22ng64GtI-oYvZZg==', start_index=17381)
Annotation(end_index=17491, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEb9gHwdQAcN75Fva4xOhh-7_y2GIJvA5JVA-Diy-mNudUO9mT50hKSERnqBa5GeZXL49YoxCzJFHlcytKmA_9WGsZ6RLeopGoVErkUPJLCfOJ8ECwTmD_YvZdtD0Wlq0OhpI0e3v_R71-7Yhg6jZB64-hVDLvyX0FiU44CT8xtduyuOa2bflv8eQ_qJE-sEKvzawZh8DeAh01LeXodEvqr_1kWwi1KT-z_0r08rkGX4Gdn8oUFqL22ng64GtI-oYvZZg==', start_index=17482)
Annotation(end_index=17501, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhuiFrZPSVbqz0HeTstDQyCr81O9iH9ce8yYUxfhJCUEiGzdE64DG8lKfk3f0kmbYR8_1sIigieRnQPatfN-jMCPVvO3eTv1jgLbZIvISgSFxXCs5ouAzVj2x04g==', start_index=17492)
Annotation(end_index=17592, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhuiFrZPSVbqz0HeTstDQyCr81O9iH9ce8yYUxfhJCUEiGzdE64DG8lKfk3f0kmbYR8_1sIigieRnQPatfN-jMCPVvO3eTv1jgLbZIvISgSFxXCs5ouAzVj2x04g==', start_index=17583)
Annotation(end_index=17602, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYRiVPOROQK8eWscQkBqwZwm6zBgnaWORi2-h2zs0HQIAeMZ5Cl-bTTUQZtH3JHbV08iUD-47X2ETLuvfi37OO6F9dFxJx4ytKqaGzlXf21OVWxQA2hPvDA80z6INz38SrxBbiYLY7xLUUX5EktYQ=', start_index=17593)
Annotation(end_index=17706, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYRiVPOROQK8eWscQkBqwZwm6zBgnaWORi2-h2zs0HQIAeMZ5Cl-bTTUQZtH3JHbV08iUD-47X2ETLuvfi37OO6F9dFxJx4ytKqaGzlXf21OVWxQA2hPvDA80z6INz38SrxBbiYLY7xLUUX5EktYQ=', start_index=17697)
Annotation(end_index=17717, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFddTZYeBh432AOSg9np5-vgcJq2ZwUeYe2pfe9YJHhvInTsX2oMlL0bJLswQZUq4opPRDA0yjx-Ci0hPkLOjsqbzQHSPS66ukirXcHMSvlbA6QcODEzw==', start_index=17707)
Annotation(end_index=17828, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFddTZYeBh432AOSg9np5-vgcJq2ZwUeYe2pfe9YJHhvInTsX2oMlL0bJLswQZUq4opPRDA0yjx-Ci0hPkLOjsqbzQHSPS66ukirXcHMSvlbA6QcODEzw==', start_index=17818)
Annotation(end_index=17838, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDCNI7FjNjawDKU_Tj4WImkTReWG0DzNBA06iNTa-QejrM6AbRVT6xfDRFCbaQJZ6k6GfCz5oMkTXC8Gs9lLy0z3QbzArwAOFsd5KwLfb6Lai5mw31gGPag-yZzTrMpOdP6ZlL', start_index=17829)
Annotation(end_index=17924, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDCNI7FjNjawDKU_Tj4WImkTReWG0DzNBA06iNTa-QejrM6AbRVT6xfDRFCbaQJZ6k6GfCz5oMkTXC8Gs9lLy0z3QbzArwAOFsd5KwLfb6Lai5mw31gGPag-yZzTrMpOdP6ZlL', start_index=17915)
Annotation(end_index=17935, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHC3VrcYYB71rkNajVYXX3keTmrWltAqERxUpwNJV6DCFbE7gQ4gxoL_0eVjgSrX2DqJcUtApzuR6XycQb7EoBx5JASJjrmU-zdIq1IMzQ7pJy4LZdbxPhMjUJdLxg9ZqsPS6BA_NXEx6qe3vbaPwUHRCfv-EMTfR_fNPyQ1zNgtQ==', start_index=17925)
Annotation(end_index=18009, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHC3VrcYYB71rkNajVYXX3keTmrWltAqERxUpwNJV6DCFbE7gQ4gxoL_0eVjgSrX2DqJcUtApzuR6XycQb7EoBx5JASJjrmU-zdIq1IMzQ7pJy4LZdbxPhMjUJdLxg9ZqsPS6BA_NXEx6qe3vbaPwUHRCfv-EMTfR_fNPyQ1zNgtQ==', start_index=17999)
Annotation(end_index=18019, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhuiFrZPSVbqz0HeTstDQyCr81O9iH9ce8yYUxfhJCUEiGzdE64DG8lKfk3f0kmbYR8_1sIigieRnQPatfN-jMCPVvO3eTv1jgLbZIvISgSFxXCs5ouAzVj2x04g==', start_index=18010)
Annotation(end_index=18074, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhuiFrZPSVbqz0HeTstDQyCr81O9iH9ce8yYUxfhJCUEiGzdE64DG8lKfk3f0kmbYR8_1sIigieRnQPatfN-jMCPVvO3eTv1jgLbZIvISgSFxXCs5ouAzVj2x04g==', start_index=18065)
Annotation(end_index=18085, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPfgVPVwuzi-SHnkf2mjJxocM6D3DPzzElxCzPSzSkd9swVQQU5h4qa6ef53fMFnq4h2yUzk4xAerw3fly76BGus-Z9989F12hp2K_f3IDN36Nhr8O6N7P7f0kHsjzrtCbbaX53_YXAdZh-Ew=', start_index=18075)
Annotation(end_index=18160, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPfgVPVwuzi-SHnkf2mjJxocM6D3DPzzElxCzPSzSkd9swVQQU5h4qa6ef53fMFnq4h2yUzk4xAerw3fly76BGus-Z9989F12hp2K_f3IDN36Nhr8O6N7P7f0kHsjzrtCbbaX53_YXAdZh-Ew=', start_index=18150)
Annotation(end_index=18170, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUeb9CJlYEu15GaNaFy0UgQDDH5QllWnn-szw2SZgPurT4NlHSMR11XfgPfumgmFauudvozYGWgnygRlixz5n_Hnq36yDsPGqxxqGzk2JUG6O28y2pwyG6WB1BsA==', start_index=18161)
Annotation(end_index=18269, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUeb9CJlYEu15GaNaFy0UgQDDH5QllWnn-szw2SZgPurT4NlHSMR11XfgPfumgmFauudvozYGWgnygRlixz5n_Hnq36yDsPGqxxqGzk2JUG6O28y2pwyG6WB1BsA==', start_index=18260)
Annotation(end_index=18280, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqyu4seGHTqE5uwVXVVUiOiXujKJMButwNLVIk8tsZUQBocGXoKgungTY_EZoKIb5vlqZDc9UCA4AwCQhBFweVVsFQsi_WqKPWBGF9_fk40CehgBInAcoUyZ3MZUqll1jwnShbAFXesVY4gb6MOA==', start_index=18270)
Annotation(end_index=18362, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqyu4seGHTqE5uwVXVVUiOiXujKJMButwNLVIk8tsZUQBocGXoKgungTY_EZoKIb5vlqZDc9UCA4AwCQhBFweVVsFQsi_WqKPWBGF9_fk40CehgBInAcoUyZ3MZUqll1jwnShbAFXesVY4gb6MOA==', start_index=18352)
Annotation(end_index=18373, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkXGHmBEcPc2gxY1LMOWtvdOdJfLoEiOo7dbORmrrTkXUN-IfEiQXKSjzAkmgVUYjSzFarBGPr7-YnTPQBzAehFCyl4QG2LCYvRUMFUmCyyX0Bqugutx3mcxcpabU2h6NjMxySGTrW_OW6dxLBtv1BvxLbL_fQfPJlxV08uuRszMuEViPNPepaCcYKmn00c6nsOqHUoemPK33nNuum8fKp6bQlLYKsrS1fnTZdhizmqZChXldB4hkwEHS6', start_index=18363)
Annotation(end_index=18468, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkXGHmBEcPc2gxY1LMOWtvdOdJfLoEiOo7dbORmrrTkXUN-IfEiQXKSjzAkmgVUYjSzFarBGPr7-YnTPQBzAehFCyl4QG2LCYvRUMFUmCyyX0Bqugutx3mcxcpabU2h6NjMxySGTrW_OW6dxLBtv1BvxLbL_fQfPJlxV08uuRszMuEViPNPepaCcYKmn00c6nsOqHUoemPK33nNuum8fKp6bQlLYKsrS1fnTZdhizmqZChXldB4hkwEHS6', start_index=18458)
Annotation(end_index=18478, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhuiFrZPSVbqz0HeTstDQyCr81O9iH9ce8yYUxfhJCUEiGzdE64DG8lKfk3f0kmbYR8_1sIigieRnQPatfN-jMCPVvO3eTv1jgLbZIvISgSFxXCs5ouAzVj2x04g==', start_index=18469)
Annotation(end_index=18553, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhuiFrZPSVbqz0HeTstDQyCr81O9iH9ce8yYUxfhJCUEiGzdE64DG8lKfk3f0kmbYR8_1sIigieRnQPatfN-jMCPVvO3eTv1jgLbZIvISgSFxXCs5ouAzVj2x04g==', start_index=18544)

## Sources
