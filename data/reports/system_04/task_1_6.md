# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** e6e12b73 | **Time:** 502.13s | **Cost:** $1.94303
--------------------------------------------------------------------------------

# Optimizing Gradient Backpropagation for Large-Scale Deep Learning: Balancing Precision, Stability, and Efficiency

### Key Points
*   **The Dominant Standard:** Mixed Precision Training (MPT) utilizing **FP16/BF16** for arithmetic and **FP32** for master weights is the current industry standard. It balances resource consumption and numerical precision by reducing memory bandwidth by approximately 50% while maintaining convergence stability through **Dynamic Loss Scaling** to prevent gradient underflow [cite: 1, 2, 3].
*   **The Emerging Optimal Strategy:** Recent research (AISTATS 2025) suggests that **BFloat16 (BF16) training combined with Stochastic Rounding (SR)** is the superior strategy for optimizing resource consumption without sacrificing convergence. SR eliminates the need for FP32 master weights, reducing memory usage by an additional ~30% and increasing throughput by up to 1.54x compared to standard MPT, while providing implicit regularization that aids generalization [cite: 4, 5, 6].
*   **Stability Mechanisms:** To ensure convergence stability in low-precision regimes, **Dynamic Loss Scaling** is essential for FP16 to manage gradient magnitudes. For BF16, which has a wider dynamic range, loss scaling is less critical, but **Stochastic Rounding** becomes the primary mechanism to prevent "stagnation" where small gradient updates vanish under deterministic rounding [cite: 7, 8, 9].
*   **Domain-Specific Optimizations:** Strategies such as **Selective Gradient Backpropagation** (in computer vision) and **One Backpropagation (OneBP)** (in recommendation systems) further optimize resources by selectively pruning gradient flow based on confidence scores or structural redundancy, thereby reducing computational overhead while improving noise robustness [cite: 10, 11].

---

## 1. Introduction: The Precision-Efficiency Trade-off in Large-Scale Training

The training of large-scale deep learning models, particularly Large Language Models (LLMs) and high-resolution vision transformers, is fundamentally constrained by the "memory wall" and computational throughput. As model parameters scale into the hundreds of billions, the standard 32-bit floating-point (FP32) representation becomes prohibitively expensive in terms of memory footprint and energy consumption [cite: 5, 12]. Consequently, the central challenge in modern deep learning optimization is devising a gradient backpropagation strategy that minimizes resource consumption (memory and compute) while preserving the numerical precision necessary for stable convergence and robust generalization.

The transition to lower precision formats—specifically 16-bit (FP16, BF16) and 8-bit (FP8, INT8)—introduces significant numerical noise. This noise manifests as quantization errors that can lead to gradient underflow (where gradients round to zero), overflow (where gradients become infinite), or stagnation (where updates are too small to change the weight parameters) [cite: 2, 7]. Therefore, the "optimal" strategy is not a single algorithm but a composite framework of **Mixed Precision Training (MPT)**, **Dynamic Loss Scaling**, and **Stochastic Rounding (SR)**.

This report provides an exhaustive analysis of these strategies, synthesizing evidence from foundational mixed-precision literature and cutting-edge 2025 research to define the state-of-the-art in gradient backpropagation.

---

## 2. The Standard Paradigm: Mixed Precision Training (MPT)

Mixed Precision Training (MPT) has established itself as the de facto standard for training large-scale neural networks. It addresses the resource bottleneck by decoupling the storage precision of the model from the accumulation precision of the gradients.

### 2.1. The Master Weights Strategy
The core mechanism of standard MPT involves maintaining two copies of the model parameters:
1.  **Low-Precision Weights (FP16/BF16):** Used for the forward pass (activations) and the backward pass (gradients). This reduces the memory bandwidth required for data movement and accelerates matrix multiplications (GEMMs) on specialized hardware like NVIDIA Tensor Cores [cite: 13, 14].
2.  **High-Precision Master Weights (FP32):** Used for the optimizer step. The gradients computed in low precision are cast to FP32 and applied to this master copy.

**Necessity of Master Weights:**
Research demonstrates that without FP32 master weights, training often diverges or stagnates. This is because the weight updates (learning rate $\times$ gradient) are frequently smaller than the minimum representable difference in FP16 (machine epsilon). If an update is smaller than $2^{-24}$ relative to the weight magnitude, deterministic rounding (Round-to-Nearest) will round the update to zero, causing the model to stop learning despite non-zero gradients [cite: 15, 16]. By accumulating these small updates in FP32, the model preserves the trajectory of descent.

### 2.2. Dynamic Loss Scaling
A critical instability in FP16 training is the "vanishing gradient" problem caused by the format's limited dynamic range. FP16 can only represent values as small as $\approx 6 \times 10^{-8}$. In deep networks, backpropagated gradients often fall below this threshold, underflowing to zero [cite: 17, 18].

**Mechanism:**
Dynamic Loss Scaling mitigates this by multiplying the loss value by a scaling factor $S$ before backpropagation begins. By the chain rule, all gradients are scaled by $S$, shifting them into the representable range of FP16.
\[ \nabla_{\theta} (S \cdot L) = S \cdot \nabla_{\theta} L \]
After backpropagation, the gradients are "unscaled" (divided by $S$) in FP32 before the optimizer update [cite: 3, 19].

**Adaptive Algorithm:**
The scaling factor $S$ is adjusted dynamically:
*   **Initialization:** Start with a large $S$ (e.g., $2^{16}$).
*   **Overflow Detection:** If `Inf` or `NaN` values appear in the gradients (indicating overflow), the update is skipped, and $S$ is reduced (typically halved).
*   **Growth:** If no overflow occurs for $N$ consecutive iterations, $S$ is increased to maximize the usage of the dynamic range [cite: 3, 20].

This strategy ensures convergence stability by actively managing the numerical precision window, allowing FP16 to function effectively despite its limitations.

### 2.3. BFloat16 (BF16) vs. FP16
The emergence of the **BFloat16 (Brain Floating Point)** format has altered the MPT landscape. BF16 trades mantissa bits for exponent bits, matching the dynamic range of FP32 (8 exponent bits) while reducing precision (7 mantissa bits vs. 10 in FP16) [cite: 21, 22].
*   **Stability:** Because BF16 has the same dynamic range as FP32, gradient underflow/overflow is significantly rarer, often eliminating the need for Dynamic Loss Scaling [cite: 22, 23].
*   **Precision:** The reduced mantissa precision, however, makes BF16 more susceptible to rounding errors during accumulation, necessitating robust rounding strategies [cite: 21].

---

## 3. The Emerging Optimal Strategy: Stochastic Rounding (SR)

While standard MPT with master weights is effective, it is memory-inefficient because it requires storing a redundant FP32 copy of the model (increasing memory usage by 50% compared to pure FP32, or 2x compared to pure FP16) [cite: 14, 15]. Recent research, particularly from **AISTATS 2025**, identifies **Stochastic Rounding (SR)** as the key to enabling "pure" low-precision training, thereby optimizing resource consumption to the theoretical limit.

### 3.1. Theoretical Foundation: Unbiased vs. Biased Rounding
Standard arithmetic uses **Round-to-Nearest (RTN)**, which is deterministic. In low-precision regimes, RTN introduces a systematic bias. If a gradient update $\Delta w$ is consistently $0.3$ of the quantization step size, RTN will round it to $0$ every time. Over millions of iterations, this results in a total update of $0$, effectively halting learning (stagnation) [cite: 7, 8].

**Stochastic Rounding (SR)** is probabilistic. It maps a real number $x$ to one of the two nearest representable values, $x_{floor}$ or $x_{ceil}$, with probability proportional to the distance:
\[ P(SR(x) = x_{ceil}) = \frac{x - x_{floor}}{x_{ceil} - x_{floor}} \]
Crucially, SR is **unbiased in expectation**: $E[SR(x)] = x$ [cite: 7, 8, 24].
*   **Effect on Convergence:** Even if an update is small, SR ensures that it will occasionally round up. Over many iterations, the accumulated updates statistically approximate the true high-precision sum. This allows the network to "integrate" small gradients that would otherwise vanish [cite: 7, 25].

### 3.2. Eliminating Master Weights
The most significant resource optimization offered by SR is the removal of FP32 master weights.
*   **Evidence:** Research presented at AISTATS 2025 demonstrates that **BF16 training with SR** applied to the weight update step matches the convergence curves of mixed precision (BF16 + FP32 Master Weights) for LLMs up to 6.7 billion parameters [cite: 4, 5, 6].
*   **Resource Gains:** By discarding the FP32 master copy, this strategy reduces memory consumption by approximately **30%** and increases training throughput by **1.54x** due to reduced memory access overhead [cite: 5, 6].
*   **Hardware Support:** This strategy is increasingly supported by hardware. Graphcore IPUs and AWS Trainium chips implement SR in hardware, allowing for efficient low-precision arithmetic without the software overhead of random number generation [cite: 25, 26].

### 3.3. Implicit Regularization and Generalization
Beyond resource efficiency, SR contributes to **generalization**. The noise introduced by stochastic rounding acts as a form of implicit regularization, similar to gradient noise in Stochastic Gradient Descent (SGD) or Dropout.
*   **Mechanism:** The added variance helps the optimizer escape shallow local minima and saddle points, potentially leading to flatter minima which are associated with better generalization [cite: 8, 27].
*   **Empirical Results:** Models trained with SR often exhibit better validation perplexity compared to standard mixed precision, as the stochasticity prevents overfitting to sharp minima [cite: 5, 6].

---

## 4. Gradient Accumulation and Batch Strategies

To further balance resource consumption against convergence stability, **Gradient Accumulation** is employed alongside backpropagation strategies.

### 4.1. Decoupling Batch Size from Memory
Gradient accumulation involves running multiple forward and backward passes with small mini-batches, accumulating the gradients in a buffer, and performing a single optimizer step only after a target "effective" batch size is reached [cite: 28, 29].
*   **Resource Optimization:** This allows training large models on GPUs with limited VRAM, as the peak memory requirement is determined by the micro-batch size, not the effective batch size [cite: 30].
*   **Precision Implication:** Accumulation buffers must typically be kept in **FP32** to prevent precision loss during the summation of gradients from many micro-batches. Using FP16 for accumulation can lead to severe swamping (where small gradients are lost when added to a large accumulator) [cite: 1, 31].

### 4.2. Impact on Generalization
The interaction between batch size and generalization is critical.
*   **Sharp vs. Flat Minima:** Very large effective batch sizes (enabled by accumulation) tend to converge to "sharp" minima, which generalize poorly. Conversely, smaller batch sizes introduce noise that favors "flat" minima [cite: 30].
*   **Strategy:** A balanced strategy involves tuning the accumulation steps to achieve a batch size that maximizes hardware utilization (throughput) without crossing the threshold where generalization degrades. Dynamic batch sizing, which adjusts the batch size during training based on gradient variance, is an emerging technique to optimize this trade-off [cite: 32].

---

## 5. Domain-Specific Backpropagation Strategies

While MPT and SR are general-purpose strategies, specific domains employ modified backpropagation schemes to optimize the signal-to-noise ratio and resource usage.

### 5.1. One Backpropagation (OneBP) for Recommendation Systems
In two-tower recommendation models (User Tower and Item Tower), the standard strategy backpropagates gradients through both towers.
*   **Inefficiency:** User representations often suffer from staleness or excessive computation relative to their information gain.
*   **Optimization:** The **OneBP** strategy cuts off gradient backpropagation for the user tower entirely. Instead, it updates user encodings using a **moving-aggregation strategy** (e.g., aggregating embeddings of items the user interacted with).
*   **Result:** This reduces computational overhead significantly (cutting the backward pass cost by nearly half) and has been shown to outperform standard "TwoBP" in recommendation performance by reducing overfitting to specific user-item interactions [cite: 11, 33].

### 5.2. Selective Gradient Backpropagation for Computer Vision
In tasks like Video Instance Segmentation (VIS), pseudo-labels generated for semi-supervised learning contain noise (false positives/negatives).
*   **Strategy:** **Selective Gradient Backpropagation** utilizes confidence scores to filter gradients. Gradients from low-confidence background queries are detached and do not contribute to the weight update.
*   **Benefit:** This prevents the model from learning from noise (improving generalization) and saves computational resources by reducing the number of tensors involved in the full backward pass [cite: 10].

### 5.3. Iterative Backpropagation for Adversarial Training
Adversarial attacks and defenses utilize an **iterative gradient backpropagation strategy** (e.g., PGD, FGSM) to craft perturbations.
*   **Optimization:** To balance precision and resources in this loop, methods like **CAMERAS** fuse activation maps with backpropagated gradients at multiple scales. This enhances the resolution of saliency maps without the heavy cost of higher-order derivatives, preserving "sanity" (fidelity to the model's true behavior) [cite: 34, 35].

---

## 6. Advanced Optimization Algorithms

The choice of optimizer interacts directly with the backpropagation strategy to determine stability.

### 6.1. Stateless Optimizers (SinkGD)
Standard optimizers like Adam maintain state (momentum, variance) for every parameter, doubling or tripling memory usage.
*   **SinkGD:** A novel optimizer that utilizes **Sinkhorn iterations** to normalize gradients across rows and columns. It is "stateless," meaning it does not require storing momentum buffers.
*   **Impact:** This drastically reduces memory consumption (comparable to SGD) while achieving convergence speeds similar to Adam. It is particularly effective for fine-tuning LLMs where memory is the primary constraint [cite: 36].

### 6.2. Zeta-based Gradient Scaling (ZetA)
*   **ZetA:** An optimizer designed to handle the noise of low-precision training better than Adam. It uses a zeta-function-based gradient scaling and an entropy-regularized loss.
*   **Benefit:** It improves convergence stability and generalization in noisy environments (like low-precision training) by preventing the optimizer from overcommitting to sharp, unstable minima [cite: 27].

### 6.3. M+Adam
*   **Concept:** Combines additive (Adam) and multiplicative (Madam) updates.
*   **Application:** Designed specifically for low-precision training without master weights. It decomposes weights into mantissa and exponent components, updating them separately to handle the coarse granularity of low-precision formats [cite: 37].

---

## 7. Hardware Implications and Future Directions

The optimal backpropagation strategy is heavily hardware-dependent.

*   **NVIDIA GPUs (Volta/Ampere/Hopper):** Optimized for **Tensor Cores**. The standard remains **AMP (Automatic Mixed Precision)** using FP16/BF16 with FP32 accumulation. Hardware support for SR is limited but improving [cite: 3, 13, 14].
*   **Google TPUs & AWS Trainium:** These architectures have native support for **Stochastic Rounding** in their matrix multiplication units (MXUs). This makes the "BF16 + SR" strategy particularly efficient on these platforms, as the SR overhead is negligible [cite: 8, 26].
*   **Graphcore IPUs:** Feature hardware-level stochastic rounding, explicitly designed to enable training with **FP16 Master Weights**, challenging the necessity of FP32 entirely [cite: 25, 38].
*   **FP8 and INT8 Training:** The frontier is moving toward 8-bit training. Here, standard backpropagation fails completely without SR and advanced scaling (e.g., logarithmic quantization). AISTATS 2025 research highlights that SR is non-negotiable for convergence in these ultra-low precision regimes [cite: 12, 39].

---

## 8. Conclusion

To answer the query directly: The gradient backpropagation strategy that best optimizes convergence stability and generalization while balancing numerical precision against resource consumption is **BFloat16 (BF16) training coupled with Stochastic Rounding (SR)**.

1.  **Resource Consumption:** It minimizes memory usage by eliminating the need for FP32 master weights (saving ~30-50% memory) and maximizes throughput (up to 1.5x speedup).
2.  **Convergence Stability:** SR provides an unbiased estimator of the true gradient, preventing the stagnation observed in deterministic rounding schemes, effectively matching FP32 convergence curves.
3.  **Generalization:** The probabilistic nature of SR introduces implicit regularization, aiding the model in escaping sharp minima and improving generalization to unseen data.

For hardware or frameworks where SR is not natively supported or computationally expensive, the **Standard Mixed Precision (FP16/BF16 + FP32 Master Weights)** with **Dynamic Loss Scaling** remains the robust, albeit less memory-efficient, alternative. Domain-specific modifications like **OneBP** or **Selective Backpropagation** should be layered on top of these fundamental numerical strategies to further optimize for specific architectures like recommendation systems or vision transformers.

### References
[cite: 1, 13, 14, 15, 16] - Mixed Precision & Master Weights
[cite: 3, 19, 20, 23] - Dynamic Loss Scaling
[cite: 4, 5, 6, 7, 8, 24] - Stochastic Rounding & AISTATS 2025 Research
[cite: 28, 29, 30] - Gradient Accumulation
[cite: 11, 33] - OneBP Strategy
[cite: 10] - Selective Gradient Backpropagation
[cite: 36, 37] - SinkGD and M+Adam Optimizers
[cite: 25, 26, 38] - Hardware Implementations (IPU, Trainium)

**Sources:**
1. [neurips.cc](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnVNflrYSVTEv3QgVQxJjfQXHkH_mXFVZguQLtsNE1ixFNjKJIvNzp-13zCF3v5s7ldzmFdTcrCVAzrZdwBVGZ0JTH4eflRq1f_p0nf1oseksP0mymcq7T1DoqhPJKQ8F2g0-gIylS3UBN9J4rZWAs-XNVC8MgXVbQ7UyNVsFyarNXYF7g6dYQZ0UPZBz61YkyREOektEZdmSuUKJx)
2. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDf7E3nOnD_iolrXrUYeFU_mkMf6lAb_ee5ylRL9rg1wKjNusPxI_ocX9wieIwz-bWBHrtEP_-s0GfrhKcPqQoWjhUZwCMSaSpYPyUUjalYIXKcZK8lHI8SuwLUmOztDJB7YyBlbJLle8pxNjah7cctOwXV4B1RywfGzOjnYBydV95lze-zaTTvINQ7wh2iIw=)
3. [nvidia.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERVoFLq-p0WyhLHPC9gTq5RXG6hz2Lv4aSNb8YKCqVf-fyAAdQcRo7prrzuFzRRlP6HhN0ik1kymyV2lB-u0gM9QX2Rw9ULCh9WllbONWy1687LO25DwtWAyusyZbViy9ptmRnx3Qgm1n1XHXntUwn_iB36TXj3wYSB8NqCKXVUywS4u3t0cjqK5c=)
4. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHz3QwKSUSYtaYxvGaOcj0f97r3ZcjfSdi_CU32wSwNDH6YEBJq8Wh1rwI8cXVFEO4h6jI2BEpc5tLS7GMOkvZKgWuL1n4pdnT7fDubgQinLEa_15ME0Q==)
5. [githubusercontent.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxcivTH5EUKmQHTlWwH3v-QXIeNsYxm83hIwhFr8A3WWN4M2IROb_9RmfrZamPJ_Whl69icUN-TOiedXHV8q77_ztS_0egwsdoydmh2Wd-xQED0Id-d2Cw7afrADJ74KY7Ac6CFWMo-eQ75hw38iggpe71PiqtjswD4CZO3r12az8JEYdTCWNjqSIX)
6. [amazon.science](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhf36KRCIYsTE__lEOX4qUp67GZjlZhXIOyu2C-VUSCnDkZwDvgLT5mEq_og6HwYt_OKeG8ZXI6Bf2AUup7WO-thwJTzIPBGz21uuZNgPbRSyRagqxUh6_Btx0JAf-u5xbq_OwNRFOK0c6XNm3l0DZhvLC7dR7jnPyqjYDrhI_CQmsPK4m72iQb0tnZ1SFvUFtY1A-L46sx653_afWYTvVPCDWwy5Z9BPdPEf2g3dM3tN32Q==)
7. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqJ79c3-57FKunmmRFbu--m0vKh-4Ys7aTFz2T5rmTGrZ0ZhjHmag0IWu1p9_ck8E44BjGYtwiIof6iEIfuKUcaNNNJoZ-VYmpG1axgjLvnNDEkMlaMg==)
8. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGu8lAc4riZwcKY_0eZX48z98n7sCyfBXUqOF-0_IIfEdrYyNTagLNGp_mZlhTI6_MQK7xhtOJ3c-CovMFOn65bTq2kdWbQ11YsV3a501SGOJm2xeg_sx99wa9a2rbUP1tjmfxJbv_rO8UcJdvEreANhuOFT69Fmqq60c6yKHsQeXY0MPeJiZYC4ZshWSbaRk7-bVgtwsjzFtXUUXDJLg2oeXA3ZIoYE5lobrD0mkJs6lA=)
9. [graphcore.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-1TfjWi3AQxeZG6te8hkgFgdJFLUx2z17VvFJOZkRoQiUiLttVBfiQIsQXPzCx_MEFdzmhlorKqqPLZpRWAEsBkC91Bu3YP1AT7H7DbisbVtsoX1ZMxur7kmtrKycDuTt5dJXGmYGV3xzZURt6wtkPi9pPtYRsLoVBgfraaUSiXwrEoDkZKqfH770rqVGgPb4OQ==)
10. [thecvf.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVFKxDSLVM_B3inazDqvrt3eAcClpanzL2q75i263LwF50mPruGGnV126BOOvpyESpwGxqKV-_nbVjuv0N1nfAG0mTQ01P8U1xCgMuw8GkzNpSZjLzlkkqqKMuuYGej6JOebHUBuTMrAsnivm6hm966V1PY_0vrxYMY-wez3zWEQkHEi3E_Fw9DciDiY6v2mzIxYSjU4rCsRVhp63fLzBW3nxif9fCETh4TQ81ap6LW--gtEN-NNoyr98uSS6jhovDjhGOGViBpzT3w980nQwsLkf4x9F9W00=)
11. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqmZ_dhbo76Zf_7Csal6ghx7zp9tkrtnyIE5y1I4JOMO3AT2dI-b-bfR98LRHXKLjp4CTQ4pKruuDyrBl1az3aodq3Gzqpe4aDv3C_--h85IuWEsdTkI6ftA==)
12. [preprints.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6_z9-KecIOjzUKOLMxPqpFZ_l-sodoVFcLcQ8d0Vb4oGDrbZe2yBLHrMYPKT0zIWvB0sgbKCqGJWd5OcyUQO1DVS4p6of85kleb_PT26Uuyyjxe1hfVJh9AtAHA_pjO3xjzx9Zdw=)
13. [rambus.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGj_hIjTCDtfq23d25V5Sk7fX1Kd8KD8wRLossSVgZtAFgixhi31YFyIqYknRzcXmG_JH2Kn-R3viXERyqFaz9-wN9a074BTmM-HjXe9aheZXj-GscTHZbXwIiWVM7283G0P89syiYA4JyrSRI2OGBICWw061mDiBW-Os1rNIirhOsyzuHodDQxOAmEYo4=)
14. [paperspace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPIWOnCRn1RLN5yg4r9fYNUr5CHAO-6DQ0E8jSLcOts_bX8M2NDlXPhJ6E9Gpy5JQY1T3WnwLY1E99l6RLOQ8dfrR7bhlkRo2doDfwiiZPvsh96Gw3dWY0LPqG0wqEc57OOGRXaSgZqC04639FLL9MzCzXcg==)
15. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFG2DzjmkyWqyx1jsgHLhF1DFR8hYIEB-Avic2EqgoH-299PsPfvjC76yXpZz6jB-HeUa2Mtzl_J1ZdY8Q8oLbm6vt1AkzMSJbS6a_E3Dn1eer4F7dzgQ==)
16. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyp0CEAEj-YTjn0BorJYiRlrH6K_NFlcveFlIZtA1OJK1vrlh_qLU-Hw8_8cP18y9Q1deS7qennJNCqDFn4ftwuCvAS3x_udcjTO-ZWgb4wmDopTdcaqTfdVKRwTJdX4wNvM0RaOQW7Na8ATD254dr_opSy7VfykUULXpBtH3v_tensr1tRJP-xNjT1wvYugmattY4U1CTfPwx5q1CrHniKwZSLuzbskP2OZbl3MRz_aTw20T7aLxu_yQ=)
17. [ic.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLu7NOV-08f-PzcTc2Zi5j3xy7NjN9DAZGxZVLWOKix16XUdvuLFbWyNiye-flqf0XLQq0w8GTUBjIxGAXIt-RoFTHT-Wa2WIgOjxyr9Xf2v0lvtMScC-xsK2ZlDFz0t3j-7sb79lhI55X)
18. [emergentmind.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFm_4SNsJ_U-e14O2SIxUZwddY976QAiDioRe9L79f50vqieFV-Vf-YiAf5DcZ2bDXen-MOvhEngbhBFht6rH7ansppyi6miHClceDWoufvfkkhDKwK3lOhAHiNoTT_Rb0EBTQw1a1fM9n9xN52ai0PRs607LaCkTpkB1J)
19. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl_FvVlL9sDRwxnDaJnK_YRJMFYN6j2rM6ZahBdxo45qTG55kC-Q06if_Bj_Dn3b4j1bOyYbLP01Q4eCcAbFR7COCWDDpVhlKy2lA2bMu5zaLoTwkf6LU2u1SdB3w7IpNtH3E3-M-JJ7iyCKyRxqpuPfTit4Tp46B-U7ZK-_WGG6qKP9y_PjaQ45PEsUuEUqSH98a1ppDKFRhFenDLAQVC30Nf)
20. [apxml.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNxg6GcesOSg1xqR3ZP3uYZy_uJFSa9Tu_DDi6B7VNJ_6qvNfdyNuDwX7oZ-acQ1u87FFQpvYzeHVPsQtKdg9R_TlhLIAhjXQCPgRb6RxPXnhlOLvvMsiai-btvsCMEELhUTZI8HwKQqrc_fs4Vsb6KPKpmZmNEAdRme24GSqWkWJJUXw-erDcXGRRY9XZoeGQXA3tZq0xUEboO3psuJTCH73ZNWSQznYmlp0MbrdJXg2srlh0AdnAnIn7)
21. [emergentmind.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXzUKblfW4b5EKUdrYYKCNDLmRpgsa89QgzCtCLr5fJnNseCKRoukDzyUy45Z0H2DG2TFSro6WCvb6KD4Kx3IW3LzcGTwz3IOtMzGr4rwGcDtAUQMxdVyV1G6UfnJVIJyBYXUn)
22. [rohan-paul.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTBufU34TBbIIs-GSJkxwTEkpZEZtcHomnOPKWrr_jwFmKGO0eP_P8pPcttZjhpf2YhSLP2UjGTx1RkfFSnvNpoCn80nyMQdbMxcpwjKmucgb5E_aEXwaNF1TFzVmfTiv0iGPv2Bd02Hkf4IisPCCFcYUY6eHN)
23. [cerebras.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqNAxm6i6iYsVqCeDIoCboqvgwzJKyHl0s87RYEauaaAKXnxuN9dC8Lqmxxro2ushY1Ko9VToeFANAVa5WCpSoJNOW5EsmiFjj20l_dxsBWfa2rp9FARs8eDpcxZxTsoD6xy6HqE1KAWXC1u1DhXaPfvoekER4Q-6HosDJ8QGtwjNdpFbuSVKGYNY=)
24. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeCJpkKS8AloZJrxULuL_BgmQtX4kiTaPMuvFCWl6-IYdsgQ3tshnZ2vTZIUdFvRM0mbUQb4HsJyejcUAeDavAHETstMlZDJ9gZF_1fkSI1mgYRCfFwKnFBjvSVlE1l-wbvuB6OwqwidkTzcGnQhlx_xtCdEklU1U8BQ==)
25. [graphcore.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9-4YQ6fP6Bxaa-eLZUigg4Ge-TBBm-5hah_F1o016rtJgHsPBkk0IKv0c9MYRyBm5RBkDIHWiqd3X2ZIohtm-OlY9TIFWlC_UliI9KofP8Ee2Rb5rsHNe26DvePyD9btI34lgtkIxzPQ9MYSzbKvEr2CnCaA5E65pBQ7-e24meZCerjGH)
26. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8Mao-__qxRr2HifZDzIqgOw2jzg7NUx4M5vFp1i45WkkjJLhe5yUa-3PJ0PeaLWCaPxPU3dkEvgcGqFzXpDEpBGTkNYem9G_nsebaUUx4rVc01wLo8SE-sg==)
27. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDm3FYZc8iSToxtUn7eFgDDzoP-14Qv8bHblP26ACQMtRlFBVeUJ1Glqw5DwTHUvmwQTCTBaxhrpafVvqNAU-4d8cP_5IHk4zvncBqFvMnXrOid0TjJHsZU0M=)
28. [hopsworks.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqXmZ_5Q2sB5Ih5oiMquMHLUUiQcTnZ2qamJU8D_I26qJSn9Jd2jyVjhvBCMZuBMOxsxRc0nUkGujehudgKRUVs2qI9nQRQAmDacFC31fURVK6pIhc5Vc2AsDi7NulfC8gqOHndHvjAIJ2e7nx5K0=)
29. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtGRJQp7ThWiN6ds-0gfVjk2VVDTc07NyYJxaGBWzwpAMr3ClXebk_LDEVxbqKzQ1eWYiyIpDRQdBpjw5doVGq7rVlTQvfrqCt-76PXq8OvfDfbZgsQJtYjBZtYD4ICeFCix7j9ZHSsWUOSioslgpBqWCp5T2mfGiV6zy744sEjt13EmhzplKt7hFUyH0-7H2nCZ7HiEGYmQ==)
30. [uplatz.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFq7ebrHRMEmg8OLmfodqhsQR4D71V2KJIcqvdhtfzpJ0VNR3YESFnlPo2fzXibJP3jKyFWKqOFNvwPvThsIbLkMDkGU07eitOr5lBBMSC9JV10cyK0fpv9GMB0ZLY33Cki70L6GEJXmua2qK9Tuj12Tyk8E6P_LIkeULg6aa27hw1U9jFL0p6jOZs71KyyeLEN70zOAEhQLJnwVuDv0vkvOdmv86FEC2W_kNean7KGoJWHTYRiCmzuCs5JRito0l-3rxQ=)
31. [readthedocs-hosted.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQoj4Geaj3WGLidbNB0uRNfc32pO-UPk6uEik516c0Ou3J-L9-3g_d-__y-_A7fBXyNhkq33eXzDj5AGnFApWVw7OOI67IPpZzuL_U-t1NSXf2pzaPYzhtCAwbJWwVvOIQ94y6PYmfi5X6xSlngIPsZ3IBdSNbVQvZsVbI1RypT97Zn3QfAKgB5EnOsgOxlE81JjuKjsRPb1LDSAHxVYmIzgsiQNVKe6ah)
32. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzJpR3FP4wQrGWHlEWmhkNKWdu216XBvbA-K3Jp7Y11S_mhYdbFc4EjebWDZxOaOLVHPzjcgMmoZcl_fDvOkT0vNXna6SsfQWIFVqpNyvDc84Er_4vOm8A9w==)
33. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7z4BkpYp8uGSUr_2zLj6AkucM_Juk2tEiZSGjBOKtDL_pPC1CB2WVXmFvgNGqKl7ps-z_cirflHJUGA56wXtSSVC3WksIFuKwG7oi1tFe3yeGaZhheEXaew==)
34. [thecvf.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFj6n7ZxiTlRIaNX2wUtVtRZiktXTXJV7tFQ1owPcbhTmSMbj8J1SDcJLdwtq6Nw7S5_vww1dUiHFgAurBNQ8uYc7H7MvgAMLJ7I0PugmtvG5ZjaGomMNorWmbbIKY7f8CpLn0J9nqaQrlP_uA99DGp4SbNiyhewIHn4mcwi6oracpXLEu9TgBoaE5UFgpW02zL7pghS-36smSuqtp1RTVWWTZhhp-hCyJgBU_jYv86MsAvzm6MDCkJjnzXMfR-Mr_BtYE0p5znhvg4UFTnZic78ZADLt_wQ==)
35. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe6MjupGuCsPWGJ_sP5DyFqLf6-FO2bOeyfG7juk-gXygcJa0F8Sx8Io_mFPP9cnrWo-P7MmQFy2IeT_aHAKOEMTJTygGJDcu5UiTnaiqhISmAHeLpQwnQLlCZvGYNGeIDKlJzrYf98mKWexpCOm5_n2SZQ6G0i0SxasraNNZtgj5GQqFhREmgH91iRCI0uRwKZSKViUljNj8s8n6VnU6sAwOIwXIWF2rGN99WpV9z_M81hkxu-KSAlgfh9GpxjxFVoemvgFnD)
36. [openreview.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvFB04ZxSsZKwvXnsD3Hlhb3-95xLxtlZQDR1EUlT9P-ZT242VmV2iv8i1r0mmrY9Pz8Tp5Bh9KHgsTuJpcBOlfo57gUMbvr2rOw6O2yG-NZl0CjfoZ4HyqA7jaR3mfsI=)
37. [openreview.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFq6CqExm55xv7jNbiuzcgdzM9x8ASRlVZhmxvgaVga69qeo4OWIQ2QpaM6ytfKJkNJJtxtY50NkrdCgUAZEkZ2Fdq4Qs9Nuq3qI6BPYOxko6l3yS-zYzSV8OLxwhT)
38. [towardsdatascience.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyWnzcDBFx7rzmrobXU_8XGoC9w44HRRrnT25h6e-7Iz7AQ9ch9wPrgA3Ymt_FeqyzolR2WL5kQyNrH3WI87oQDTsL_-cbGEdis4u8VbyUJVPTuNGMy7pEx5KRgtelHg_nBsY6oi7gsC-p_UZBdZ74NPJ9_iD1b_AduBjgE_F9NMMPOzH-gjF-7cnHGlbpVAJK-WUom61XDAZz6THxRGjveyuLSF8fozbd7_AC-i-RcK1Cf8A5Y9azGYhWE3o=)
39. [openreview.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFP-_cVHPO8gwIHIrIwOh9YIcY2BzyNtBWHx1BY5UTlClle7p8QdOtFqUHGf1yaxbqcI29KsDRvdZtCHq7JOG63_rc43zcTDEW3gV6KGGdgwMFm31IbS6ieJWTMCaMH_Yw=)


## Annotations
Annotation(end_index=524, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERVoFLq-p0WyhLHPC9gTq5RXG6hz2Lv4aSNb8YKCqVf-fyAAdQcRo7prrzuFzRRlP6HhN0ik1kymyV2lB-u0gM9QX2Rw9ULCh9WllbONWy1687LO25DwtWAyusyZbViy9ptmRnx3Qgm1n1XHXntUwn_iB36TXj3wYSB8NqCKXVUywS4u3t0cjqK5c=', start_index=509)
Annotation(end_index=524, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnVNflrYSVTEv3QgVQxJjfQXHkH_mXFVZguQLtsNE1ixFNjKJIvNzp-13zCF3v5s7ldzmFdTcrCVAzrZdwBVGZ0JTH4eflRq1f_p0nf1oseksP0mymcq7T1DoqhPJKQ8F2g0-gIylS3UBN9J4rZWAs-XNVC8MgXVbQ7UyNVsFyarNXYF7g6dYQZ0UPZBz61YkyREOektEZdmSuUKJx', start_index=509)
Annotation(end_index=524, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDf7E3nOnD_iolrXrUYeFU_mkMf6lAb_ee5ylRL9rg1wKjNusPxI_ocX9wieIwz-bWBHrtEP_-s0GfrhKcPqQoWjhUZwCMSaSpYPyUUjalYIXKcZK8lHI8SuwLUmOztDJB7YyBlbJLle8pxNjah7cctOwXV4B1RywfGzOjnYBydV95lze-zaTTvINQ7wh2iIw=', start_index=509)
Annotation(end_index=1011, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxcivTH5EUKmQHTlWwH3v-QXIeNsYxm83hIwhFr8A3WWN4M2IROb_9RmfrZamPJ_Whl69icUN-TOiedXHV8q77_ztS_0egwsdoydmh2Wd-xQED0Id-d2Cw7afrADJ74KY7Ac6CFWMo-eQ75hw38iggpe71PiqtjswD4CZO3r12az8JEYdTCWNjqSIX', start_index=996)
Annotation(end_index=1011, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhf36KRCIYsTE__lEOX4qUp67GZjlZhXIOyu2C-VUSCnDkZwDvgLT5mEq_og6HwYt_OKeG8ZXI6Bf2AUup7WO-thwJTzIPBGz21uuZNgPbRSyRagqxUh6_Btx0JAf-u5xbq_OwNRFOK0c6XNm3l0DZhvLC7dR7jnPyqjYDrhI_CQmsPK4m72iQb0tnZ1SFvUFtY1A-L46sx653_afWYTvVPCDWwy5Z9BPdPEf2g3dM3tN32Q==', start_index=996)
Annotation(end_index=1011, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHz3QwKSUSYtaYxvGaOcj0f97r3ZcjfSdi_CU32wSwNDH6YEBJq8Wh1rwI8cXVFEO4h6jI2BEpc5tLS7GMOkvZKgWuL1n4pdnT7fDubgQinLEa_15ME0Q==', start_index=996)
Annotation(end_index=1415, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-1TfjWi3AQxeZG6te8hkgFgdJFLUx2z17VvFJOZkRoQiUiLttVBfiQIsQXPzCx_MEFdzmhlorKqqPLZpRWAEsBkC91Bu3YP1AT7H7DbisbVtsoX1ZMxur7kmtrKycDuTt5dJXGmYGV3xzZURt6wtkPi9pPtYRsLoVBgfraaUSiXwrEoDkZKqfH770rqVGgPb4OQ==', start_index=1400)
Annotation(end_index=1415, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqJ79c3-57FKunmmRFbu--m0vKh-4Ys7aTFz2T5rmTGrZ0ZhjHmag0IWu1p9_ck8E44BjGYtwiIof6iEIfuKUcaNNNJoZ-VYmpG1axgjLvnNDEkMlaMg==', start_index=1400)
Annotation(end_index=1415, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGu8lAc4riZwcKY_0eZX48z98n7sCyfBXUqOF-0_IIfEdrYyNTagLNGp_mZlhTI6_MQK7xhtOJ3c-CovMFOn65bTq2kdWbQ11YsV3a501SGOJm2xeg_sx99wa9a2rbUP1tjmfxJbv_rO8UcJdvEreANhuOFT69Fmqq60c6yKHsQeXY0MPeJiZYC4ZshWSbaRk7-bVgtwsjzFtXUUXDJLg2oeXA3ZIoYE5lobrD0mkJs6lA=', start_index=1400)
Annotation(end_index=1803, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqmZ_dhbo76Zf_7Csal6ghx7zp9tkrtnyIE5y1I4JOMO3AT2dI-b-bfR98LRHXKLjp4CTQ4pKruuDyrBl1az3aodq3Gzqpe4aDv3C_--h85IuWEsdTkI6ftA==', start_index=1789)
Annotation(end_index=1803, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVFKxDSLVM_B3inazDqvrt3eAcClpanzL2q75i263LwF50mPruGGnV126BOOvpyESpwGxqKV-_nbVjuv0N1nfAG0mTQ01P8U1xCgMuw8GkzNpSZjLzlkkqqKMuuYGej6JOebHUBuTMrAsnivm6hm966V1PY_0vrxYMY-wez3zWEQkHEi3E_Fw9DciDiY6v2mzIxYSjU4rCsRVhp63fLzBW3nxif9fCETh4TQ81ap6LW--gtEN-NNoyr98uSS6jhovDjhGOGViBpzT3w980nQwsLkf4x9F9W00=', start_index=1789)
Annotation(end_index=2315, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6_z9-KecIOjzUKOLMxPqpFZ_l-sodoVFcLcQ8d0Vb4oGDrbZe2yBLHrMYPKT0zIWvB0sgbKCqGJWd5OcyUQO1DVS4p6of85kleb_PT26Uuyyjxe1hfVJh9AtAHA_pjO3xjzx9Zdw=', start_index=2302)
Annotation(end_index=2315, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxcivTH5EUKmQHTlWwH3v-QXIeNsYxm83hIwhFr8A3WWN4M2IROb_9RmfrZamPJ_Whl69icUN-TOiedXHV8q77_ztS_0egwsdoydmh2Wd-xQED0Id-d2Cw7afrADJ74KY7Ac6CFWMo-eQ75hw38iggpe71PiqtjswD4CZO3r12az8JEYdTCWNjqSIX', start_index=2302)
Annotation(end_index=2983, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDf7E3nOnD_iolrXrUYeFU_mkMf6lAb_ee5ylRL9rg1wKjNusPxI_ocX9wieIwz-bWBHrtEP_-s0GfrhKcPqQoWjhUZwCMSaSpYPyUUjalYIXKcZK8lHI8SuwLUmOztDJB7YyBlbJLle8pxNjah7cctOwXV4B1RywfGzOjnYBydV95lze-zaTTvINQ7wh2iIw=', start_index=2971)
Annotation(end_index=2983, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqJ79c3-57FKunmmRFbu--m0vKh-4Ys7aTFz2T5rmTGrZ0ZhjHmag0IWu1p9_ck8E44BjGYtwiIof6iEIfuKUcaNNNJoZ-VYmpG1axgjLvnNDEkMlaMg==', start_index=2971)
Annotation(end_index=4137, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPIWOnCRn1RLN5yg4r9fYNUr5CHAO-6DQ0E8jSLcOts_bX8M2NDlXPhJ6E9Gpy5JQY1T3WnwLY1E99l6RLOQ8dfrR7bhlkRo2doDfwiiZPvsh96Gw3dWY0LPqG0wqEc57OOGRXaSgZqC04639FLL9MzCzXcg==', start_index=4123)
Annotation(end_index=4137, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGj_hIjTCDtfq23d25V5Sk7fX1Kd8KD8wRLossSVgZtAFgixhi31YFyIqYknRzcXmG_JH2Kn-R3viXERyqFaz9-wN9a074BTmM-HjXe9aheZXj-GscTHZbXwIiWVM7283G0P89syiYA4JyrSRI2OGBICWw061mDiBW-Os1rNIirhOsyzuHodDQxOAmEYo4=', start_index=4123)
Annotation(end_index=4815, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyp0CEAEj-YTjn0BorJYiRlrH6K_NFlcveFlIZtA1OJK1vrlh_qLU-Hw8_8cP18y9Q1deS7qennJNCqDFn4ftwuCvAS3x_udcjTO-ZWgb4wmDopTdcaqTfdVKRwTJdX4wNvM0RaOQW7Na8ATD254dr_opSy7VfykUULXpBtH3v_tensr1tRJP-xNjT1wvYugmattY4U1CTfPwx5q1CrHniKwZSLuzbskP2OZbl3MRz_aTw20T7aLxu_yQ=', start_index=4801)
Annotation(end_index=4815, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFG2DzjmkyWqyx1jsgHLhF1DFR8hYIEB-Avic2EqgoH-299PsPfvjC76yXpZz6jB-HeUa2Mtzl_J1ZdY8Q8oLbm6vt1AkzMSJbS6a_E3Dn1eer4F7dzgQ==', start_index=4801)
Annotation(end_index=5244, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFm_4SNsJ_U-e14O2SIxUZwddY976QAiDioRe9L79f50vqieFV-Vf-YiAf5DcZ2bDXen-MOvhEngbhBFht6rH7ansppyi6miHClceDWoufvfkkhDKwK3lOhAHiNoTT_Rb0EBTQw1a1fM9n9xN52ai0PRs607LaCkTpkB1J', start_index=5230)
Annotation(end_index=5244, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLu7NOV-08f-PzcTc2Zi5j3xy7NjN9DAZGxZVLWOKix16XUdvuLFbWyNiye-flqf0XLQq0w8GTUBjIxGAXIt-RoFTHT-Wa2WIgOjxyr9Xf2v0lvtMScC-xsK2ZlDFz0t3j-7sb79lhI55X', start_index=5230)
Annotation(end_index=5667, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERVoFLq-p0WyhLHPC9gTq5RXG6hz2Lv4aSNb8YKCqVf-fyAAdQcRo7prrzuFzRRlP6HhN0ik1kymyV2lB-u0gM9QX2Rw9ULCh9WllbONWy1687LO25DwtWAyusyZbViy9ptmRnx3Qgm1n1XHXntUwn_iB36TXj3wYSB8NqCKXVUywS4u3t0cjqK5c=', start_index=5654)
Annotation(end_index=5667, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl_FvVlL9sDRwxnDaJnK_YRJMFYN6j2rM6ZahBdxo45qTG55kC-Q06if_Bj_Dn3b4j1bOyYbLP01Q4eCcAbFR7COCWDDpVhlKy2lA2bMu5zaLoTwkf6LU2u1SdB3w7IpNtH3E3-M-JJ7iyCKyRxqpuPfTit4Tp46B-U7ZK-_WGG6qKP9y_PjaQ45PEsUuEUqSH98a1ppDKFRhFenDLAQVC30Nf', start_index=5654)
Annotation(end_index=6112, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERVoFLq-p0WyhLHPC9gTq5RXG6hz2Lv4aSNb8YKCqVf-fyAAdQcRo7prrzuFzRRlP6HhN0ik1kymyV2lB-u0gM9QX2Rw9ULCh9WllbONWy1687LO25DwtWAyusyZbViy9ptmRnx3Qgm1n1XHXntUwn_iB36TXj3wYSB8NqCKXVUywS4u3t0cjqK5c=', start_index=6099)
Annotation(end_index=6112, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNxg6GcesOSg1xqR3ZP3uYZy_uJFSa9Tu_DDi6B7VNJ_6qvNfdyNuDwX7oZ-acQ1u87FFQpvYzeHVPsQtKdg9R_TlhLIAhjXQCPgRb6RxPXnhlOLvvMsiai-btvsCMEELhUTZI8HwKQqrc_fs4Vsb6KPKpmZmNEAdRme24GSqWkWJJUXw-erDcXGRRY9XZoeGQXA3tZq0xUEboO3psuJTCH73ZNWSQznYmlp0MbrdJXg2srlh0AdnAnIn7', start_index=6099)
Annotation(end_index=6575, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXzUKblfW4b5EKUdrYYKCNDLmRpgsa89QgzCtCLr5fJnNseCKRoukDzyUy45Z0H2DG2TFSro6WCvb6KD4Kx3IW3LzcGTwz3IOtMzGr4rwGcDtAUQMxdVyV1G6UfnJVIJyBYXUn', start_index=6561)
Annotation(end_index=6575, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTBufU34TBbIIs-GSJkxwTEkpZEZtcHomnOPKWrr_jwFmKGO0eP_P8pPcttZjhpf2YhSLP2UjGTx1RkfFSnvNpoCn80nyMQdbMxcpwjKmucgb5E_aEXwaNF1TFzVmfTiv0iGPv2Bd02Hkf4IisPCCFcYUY6eHN', start_index=6561)
Annotation(end_index=6763, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqNAxm6i6iYsVqCeDIoCboqvgwzJKyHl0s87RYEauaaAKXnxuN9dC8Lqmxxro2ushY1Ko9VToeFANAVa5WCpSoJNOW5EsmiFjj20l_dxsBWfa2rp9FARs8eDpcxZxTsoD6xy6HqE1KAWXC1u1DhXaPfvoekER4Q-6HosDJ8QGtwjNdpFbuSVKGYNY=', start_index=6749)
Annotation(end_index=6763, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTBufU34TBbIIs-GSJkxwTEkpZEZtcHomnOPKWrr_jwFmKGO0eP_P8pPcttZjhpf2YhSLP2UjGTx1RkfFSnvNpoCn80nyMQdbMxcpwjKmucgb5E_aEXwaNF1TFzVmfTiv0iGPv2Bd02Hkf4IisPCCFcYUY6eHN', start_index=6749)
Annotation(end_index=6944, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXzUKblfW4b5EKUdrYYKCNDLmRpgsa89QgzCtCLr5fJnNseCKRoukDzyUy45Z0H2DG2TFSro6WCvb6KD4Kx3IW3LzcGTwz3IOtMzGr4rwGcDtAUQMxdVyV1G6UfnJVIJyBYXUn', start_index=6934)
Annotation(end_index=7254, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPIWOnCRn1RLN5yg4r9fYNUr5CHAO-6DQ0E8jSLcOts_bX8M2NDlXPhJ6E9Gpy5JQY1T3WnwLY1E99l6RLOQ8dfrR7bhlkRo2doDfwiiZPvsh96Gw3dWY0LPqG0wqEc57OOGRXaSgZqC04639FLL9MzCzXcg==', start_index=7240)
Annotation(end_index=7254, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFG2DzjmkyWqyx1jsgHLhF1DFR8hYIEB-Avic2EqgoH-299PsPfvjC76yXpZz6jB-HeUa2Mtzl_J1ZdY8Q8oLbm6vt1AkzMSJbS6a_E3Dn1eer4F7dzgQ==', start_index=7240)
Annotation(end_index=7913, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqJ79c3-57FKunmmRFbu--m0vKh-4Ys7aTFz2T5rmTGrZ0ZhjHmag0IWu1p9_ck8E44BjGYtwiIof6iEIfuKUcaNNNJoZ-VYmpG1axgjLvnNDEkMlaMg==', start_index=7901)
Annotation(end_index=7913, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGu8lAc4riZwcKY_0eZX48z98n7sCyfBXUqOF-0_IIfEdrYyNTagLNGp_mZlhTI6_MQK7xhtOJ3c-CovMFOn65bTq2kdWbQ11YsV3a501SGOJm2xeg_sx99wa9a2rbUP1tjmfxJbv_rO8UcJdvEreANhuOFT69Fmqq60c6yKHsQeXY0MPeJiZYC4ZshWSbaRk7-bVgtwsjzFtXUUXDJLg2oeXA3ZIoYE5lobrD0mkJs6lA=', start_index=7901)
Annotation(end_index=8259, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeCJpkKS8AloZJrxULuL_BgmQtX4kiTaPMuvFCWl6-IYdsgQ3tshnZ2vTZIUdFvRM0mbUQb4HsJyejcUAeDavAHETstMlZDJ9gZF_1fkSI1mgYRCfFwKnFBjvSVlE1l-wbvuB6OwqwidkTzcGnQhlx_xtCdEklU1U8BQ==', start_index=8243)
Annotation(end_index=8259, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqJ79c3-57FKunmmRFbu--m0vKh-4Ys7aTFz2T5rmTGrZ0ZhjHmag0IWu1p9_ck8E44BjGYtwiIof6iEIfuKUcaNNNJoZ-VYmpG1axgjLvnNDEkMlaMg==', start_index=8243)
Annotation(end_index=8259, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGu8lAc4riZwcKY_0eZX48z98n7sCyfBXUqOF-0_IIfEdrYyNTagLNGp_mZlhTI6_MQK7xhtOJ3c-CovMFOn65bTq2kdWbQ11YsV3a501SGOJm2xeg_sx99wa9a2rbUP1tjmfxJbv_rO8UcJdvEreANhuOFT69Fmqq60c6yKHsQeXY0MPeJiZYC4ZshWSbaRk7-bVgtwsjzFtXUUXDJLg2oeXA3ZIoYE5lobrD0mkJs6lA=', start_index=8243)
Annotation(end_index=8564, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9-4YQ6fP6Bxaa-eLZUigg4Ge-TBBm-5hah_F1o016rtJgHsPBkk0IKv0c9MYRyBm5RBkDIHWiqd3X2ZIohtm-OlY9TIFWlC_UliI9KofP8Ee2Rb5rsHNe26DvePyD9btI34lgtkIxzPQ9MYSzbKvEr2CnCaA5E65pBQ7-e24meZCerjGH', start_index=8551)
Annotation(end_index=8564, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqJ79c3-57FKunmmRFbu--m0vKh-4Ys7aTFz2T5rmTGrZ0ZhjHmag0IWu1p9_ck8E44BjGYtwiIof6iEIfuKUcaNNNJoZ-VYmpG1axgjLvnNDEkMlaMg==', start_index=8551)
Annotation(end_index=8962, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxcivTH5EUKmQHTlWwH3v-QXIeNsYxm83hIwhFr8A3WWN4M2IROb_9RmfrZamPJ_Whl69icUN-TOiedXHV8q77_ztS_0egwsdoydmh2Wd-xQED0Id-d2Cw7afrADJ74KY7Ac6CFWMo-eQ75hw38iggpe71PiqtjswD4CZO3r12az8JEYdTCWNjqSIX', start_index=8947)
Annotation(end_index=8962, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhf36KRCIYsTE__lEOX4qUp67GZjlZhXIOyu2C-VUSCnDkZwDvgLT5mEq_og6HwYt_OKeG8ZXI6Bf2AUup7WO-thwJTzIPBGz21uuZNgPbRSyRagqxUh6_Btx0JAf-u5xbq_OwNRFOK0c6XNm3l0DZhvLC7dR7jnPyqjYDrhI_CQmsPK4m72iQb0tnZ1SFvUFtY1A-L46sx653_afWYTvVPCDWwy5Z9BPdPEf2g3dM3tN32Q==', start_index=8947)
Annotation(end_index=8962, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHz3QwKSUSYtaYxvGaOcj0f97r3ZcjfSdi_CU32wSwNDH6YEBJq8Wh1rwI8cXVFEO4h6jI2BEpc5tLS7GMOkvZKgWuL1n4pdnT7fDubgQinLEa_15ME0Q==', start_index=8947)
Annotation(end_index=9187, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxcivTH5EUKmQHTlWwH3v-QXIeNsYxm83hIwhFr8A3WWN4M2IROb_9RmfrZamPJ_Whl69icUN-TOiedXHV8q77_ztS_0egwsdoydmh2Wd-xQED0Id-d2Cw7afrADJ74KY7Ac6CFWMo-eQ75hw38iggpe71PiqtjswD4CZO3r12az8JEYdTCWNjqSIX', start_index=9175)
Annotation(end_index=9187, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhf36KRCIYsTE__lEOX4qUp67GZjlZhXIOyu2C-VUSCnDkZwDvgLT5mEq_og6HwYt_OKeG8ZXI6Bf2AUup7WO-thwJTzIPBGz21uuZNgPbRSyRagqxUh6_Btx0JAf-u5xbq_OwNRFOK0c6XNm3l0DZhvLC7dR7jnPyqjYDrhI_CQmsPK4m72iQb0tnZ1SFvUFtY1A-L46sx653_afWYTvVPCDWwy5Z9BPdPEf2g3dM3tN32Q==', start_index=9175)
Annotation(end_index=9452, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8Mao-__qxRr2HifZDzIqgOw2jzg7NUx4M5vFp1i45WkkjJLhe5yUa-3PJ0PeaLWCaPxPU3dkEvgcGqFzXpDEpBGTkNYem9G_nsebaUUx4rVc01wLo8SE-sg==', start_index=9438)
Annotation(end_index=9452, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9-4YQ6fP6Bxaa-eLZUigg4Ge-TBBm-5hah_F1o016rtJgHsPBkk0IKv0c9MYRyBm5RBkDIHWiqd3X2ZIohtm-OlY9TIFWlC_UliI9KofP8Ee2Rb5rsHNe26DvePyD9btI34lgtkIxzPQ9MYSzbKvEr2CnCaA5E65pBQ7-e24meZCerjGH', start_index=9438)
Annotation(end_index=9939, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGu8lAc4riZwcKY_0eZX48z98n7sCyfBXUqOF-0_IIfEdrYyNTagLNGp_mZlhTI6_MQK7xhtOJ3c-CovMFOn65bTq2kdWbQ11YsV3a501SGOJm2xeg_sx99wa9a2rbUP1tjmfxJbv_rO8UcJdvEreANhuOFT69Fmqq60c6yKHsQeXY0MPeJiZYC4ZshWSbaRk7-bVgtwsjzFtXUUXDJLg2oeXA3ZIoYE5lobrD0mkJs6lA=', start_index=9926)
Annotation(end_index=9939, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDm3FYZc8iSToxtUn7eFgDDzoP-14Qv8bHblP26ACQMtRlFBVeUJ1Glqw5DwTHUvmwQTCTBaxhrpafVvqNAU-4d8cP_5IHk4zvncBqFvMnXrOid0TjJHsZU0M=', start_index=9926)
Annotation(end_index=10142, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxcivTH5EUKmQHTlWwH3v-QXIeNsYxm83hIwhFr8A3WWN4M2IROb_9RmfrZamPJ_Whl69icUN-TOiedXHV8q77_ztS_0egwsdoydmh2Wd-xQED0Id-d2Cw7afrADJ74KY7Ac6CFWMo-eQ75hw38iggpe71PiqtjswD4CZO3r12az8JEYdTCWNjqSIX', start_index=10130)
Annotation(end_index=10142, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhf36KRCIYsTE__lEOX4qUp67GZjlZhXIOyu2C-VUSCnDkZwDvgLT5mEq_og6HwYt_OKeG8ZXI6Bf2AUup7WO-thwJTzIPBGz21uuZNgPbRSyRagqxUh6_Btx0JAf-u5xbq_OwNRFOK0c6XNm3l0DZhvLC7dR7jnPyqjYDrhI_CQmsPK4m72iQb0tnZ1SFvUFtY1A-L46sx653_afWYTvVPCDWwy5Z9BPdPEf2g3dM3tN32Q==', start_index=10130)
Annotation(end_index=10639, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqXmZ_5Q2sB5Ih5oiMquMHLUUiQcTnZ2qamJU8D_I26qJSn9Jd2jyVjhvBCMZuBMOxsxRc0nUkGujehudgKRUVs2qI9nQRQAmDacFC31fURVK6pIhc5Vc2AsDi7NulfC8gqOHndHvjAIJ2e7nx5K0=', start_index=10625)
Annotation(end_index=10639, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtGRJQp7ThWiN6ds-0gfVjk2VVDTc07NyYJxaGBWzwpAMr3ClXebk_LDEVxbqKzQ1eWYiyIpDRQdBpjw5doVGq7rVlTQvfrqCt-76PXq8OvfDfbZgsQJtYjBZtYD4ICeFCix7j9ZHSsWUOSioslgpBqWCp5T2mfGiV6zy744sEjt13EmhzplKt7hFUyH0-7H2nCZ7HiEGYmQ==', start_index=10625)
Annotation(end_index=10842, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFq7ebrHRMEmg8OLmfodqhsQR4D71V2KJIcqvdhtfzpJ0VNR3YESFnlPo2fzXibJP3jKyFWKqOFNvwPvThsIbLkMDkGU07eitOr5lBBMSC9JV10cyK0fpv9GMB0ZLY33Cki70L6GEJXmua2qK9Tuj12Tyk8E6P_LIkeULg6aa27hw1U9jFL0p6jOZs71KyyeLEN70zOAEhQLJnwVuDv0vkvOdmv86FEC2W_kNean7KGoJWHTYRiCmzuCs5JRito0l-3rxQ=', start_index=10832)
Annotation(end_index=11152, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQoj4Geaj3WGLidbNB0uRNfc32pO-UPk6uEik516c0Ou3J-L9-3g_d-__y-_A7fBXyNhkq33eXzDj5AGnFApWVw7OOI67IPpZzuL_U-t1NSXf2pzaPYzhtCAwbJWwVvOIQ94y6PYmfi5X6xSlngIPsZ3IBdSNbVQvZsVbI1RypT97Zn3QfAKgB5EnOsgOxlE81JjuKjsRPb1LDSAHxVYmIzgsiQNVKe6ah', start_index=11139)
Annotation(end_index=11152, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnVNflrYSVTEv3QgVQxJjfQXHkH_mXFVZguQLtsNE1ixFNjKJIvNzp-13zCF3v5s7ldzmFdTcrCVAzrZdwBVGZ0JTH4eflRq1f_p0nf1oseksP0mymcq7T1DoqhPJKQ8F2g0-gIylS3UBN9J4rZWAs-XNVC8MgXVbQ7UyNVsFyarNXYF7g6dYQZ0UPZBz61YkyREOektEZdmSuUKJx', start_index=11139)
Annotation(end_index=11491, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFq7ebrHRMEmg8OLmfodqhsQR4D71V2KJIcqvdhtfzpJ0VNR3YESFnlPo2fzXibJP3jKyFWKqOFNvwPvThsIbLkMDkGU07eitOr5lBBMSC9JV10cyK0fpv9GMB0ZLY33Cki70L6GEJXmua2qK9Tuj12Tyk8E6P_LIkeULg6aa27hw1U9jFL0p6jOZs71KyyeLEN70zOAEhQLJnwVuDv0vkvOdmv86FEC2W_kNean7KGoJWHTYRiCmzuCs5JRito0l-3rxQ=', start_index=11481)
Annotation(end_index=11862, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzJpR3FP4wQrGWHlEWmhkNKWdu216XBvbA-K3Jp7Y11S_mhYdbFc4EjebWDZxOaOLVHPzjcgMmoZcl_fDvOkT0vNXna6SsfQWIFVqpNyvDc84Er_4vOm8A9w==', start_index=11852)
Annotation(end_index=12929, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqmZ_dhbo76Zf_7Csal6ghx7zp9tkrtnyIE5y1I4JOMO3AT2dI-b-bfR98LRHXKLjp4CTQ4pKruuDyrBl1az3aodq3Gzqpe4aDv3C_--h85IuWEsdTkI6ftA==', start_index=12915)
Annotation(end_index=12929, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7z4BkpYp8uGSUr_2zLj6AkucM_Juk2tEiZSGjBOKtDL_pPC1CB2WVXmFvgNGqKl7ps-z_cirflHJUGA56wXtSSVC3WksIFuKwG7oi1tFe3yeGaZhheEXaew==', start_index=12915)
Annotation(end_index=13558, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVFKxDSLVM_B3inazDqvrt3eAcClpanzL2q75i263LwF50mPruGGnV126BOOvpyESpwGxqKV-_nbVjuv0N1nfAG0mTQ01P8U1xCgMuw8GkzNpSZjLzlkkqqKMuuYGej6JOebHUBuTMrAsnivm6hm966V1PY_0vrxYMY-wez3zWEQkHEi3E_Fw9DciDiY6v2mzIxYSjU4rCsRVhp63fLzBW3nxif9fCETh4TQ81ap6LW--gtEN-NNoyr98uSS6jhovDjhGOGViBpzT3w980nQwsLkf4x9F9W00=', start_index=13548)
Annotation(end_index=14094, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFj6n7ZxiTlRIaNX2wUtVtRZiktXTXJV7tFQ1owPcbhTmSMbj8J1SDcJLdwtq6Nw7S5_vww1dUiHFgAurBNQ8uYc7H7MvgAMLJ7I0PugmtvG5ZjaGomMNorWmbbIKY7f8CpLn0J9nqaQrlP_uA99DGp4SbNiyhewIHn4mcwi6oracpXLEu9TgBoaE5UFgpW02zL7pghS-36smSuqtp1RTVWWTZhhp-hCyJgBU_jYv86MsAvzm6MDCkJjnzXMfR-Mr_BtYE0p5znhvg4UFTnZic78ZADLt_wQ==', start_index=14080)
Annotation(end_index=14094, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe6MjupGuCsPWGJ_sP5DyFqLf6-FO2bOeyfG7juk-gXygcJa0F8Sx8Io_mFPP9cnrWo-P7MmQFy2IeT_aHAKOEMTJTygGJDcu5UiTnaiqhISmAHeLpQwnQLlCZvGYNGeIDKlJzrYf98mKWexpCOm5_n2SZQ6G0i0SxasraNNZtgj5GQqFhREmgH91iRCI0uRwKZSKViUljNj8s8n6VnU6sAwOIwXIWF2rGN99WpV9z_M81hkxu-KSAlgfh9GpxjxFVoemvgFnD', start_index=14080)
Annotation(end_index=14829, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvFB04ZxSsZKwvXnsD3Hlhb3-95xLxtlZQDR1EUlT9P-ZT242VmV2iv8i1r0mmrY9Pz8Tp5Bh9KHgsTuJpcBOlfo57gUMbvr2rOw6O2yG-NZl0CjfoZ4HyqA7jaR3mfsI=', start_index=14819)
Annotation(end_index=15262, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDm3FYZc8iSToxtUn7eFgDDzoP-14Qv8bHblP26ACQMtRlFBVeUJ1Glqw5DwTHUvmwQTCTBaxhrpafVvqNAU-4d8cP_5IHk4zvncBqFvMnXrOid0TjJHsZU0M=', start_index=15252)
Annotation(end_index=15607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFq6CqExm55xv7jNbiuzcgdzM9x8ASRlVZhmxvgaVga69qeo4OWIQ2QpaM6ytfKJkNJJtxtY50NkrdCgUAZEkZ2Fdq4Qs9Nuq3qI6BPYOxko6l3yS-zYzSV8OLxwhT', start_index=15597)
Annotation(end_index=15973, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPIWOnCRn1RLN5yg4r9fYNUr5CHAO-6DQ0E8jSLcOts_bX8M2NDlXPhJ6E9Gpy5JQY1T3WnwLY1E99l6RLOQ8dfrR7bhlkRo2doDfwiiZPvsh96Gw3dWY0LPqG0wqEc57OOGRXaSgZqC04639FLL9MzCzXcg==', start_index=15956)
Annotation(end_index=15973, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERVoFLq-p0WyhLHPC9gTq5RXG6hz2Lv4aSNb8YKCqVf-fyAAdQcRo7prrzuFzRRlP6HhN0ik1kymyV2lB-u0gM9QX2Rw9ULCh9WllbONWy1687LO25DwtWAyusyZbViy9ptmRnx3Qgm1n1XHXntUwn_iB36TXj3wYSB8NqCKXVUywS4u3t0cjqK5c=', start_index=15956)
Annotation(end_index=15973, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGj_hIjTCDtfq23d25V5Sk7fX1Kd8KD8wRLossSVgZtAFgixhi31YFyIqYknRzcXmG_JH2Kn-R3viXERyqFaz9-wN9a074BTmM-HjXe9aheZXj-GscTHZbXwIiWVM7283G0P89syiYA4JyrSRI2OGBICWw061mDiBW-Os1rNIirhOsyzuHodDQxOAmEYo4=', start_index=15956)
Annotation(end_index=16249, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8Mao-__qxRr2HifZDzIqgOw2jzg7NUx4M5vFp1i45WkkjJLhe5yUa-3PJ0PeaLWCaPxPU3dkEvgcGqFzXpDEpBGTkNYem9G_nsebaUUx4rVc01wLo8SE-sg==', start_index=16236)
Annotation(end_index=16249, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGu8lAc4riZwcKY_0eZX48z98n7sCyfBXUqOF-0_IIfEdrYyNTagLNGp_mZlhTI6_MQK7xhtOJ3c-CovMFOn65bTq2kdWbQ11YsV3a501SGOJm2xeg_sx99wa9a2rbUP1tjmfxJbv_rO8UcJdvEreANhuOFT69Fmqq60c6yKHsQeXY0MPeJiZYC4ZshWSbaRk7-bVgtwsjzFtXUUXDJLg2oeXA3ZIoYE5lobrD0mkJs6lA=', start_index=16236)
Annotation(end_index=16445, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9-4YQ6fP6Bxaa-eLZUigg4Ge-TBBm-5hah_F1o016rtJgHsPBkk0IKv0c9MYRyBm5RBkDIHWiqd3X2ZIohtm-OlY9TIFWlC_UliI9KofP8Ee2Rb5rsHNe26DvePyD9btI34lgtkIxzPQ9MYSzbKvEr2CnCaA5E65pBQ7-e24meZCerjGH', start_index=16431)
Annotation(end_index=16445, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyWnzcDBFx7rzmrobXU_8XGoC9w44HRRrnT25h6e-7Iz7AQ9ch9wPrgA3Ymt_FeqyzolR2WL5kQyNrH3WI87oQDTsL_-cbGEdis4u8VbyUJVPTuNGMy7pEx5KRgtelHg_nBsY6oi7gsC-p_UZBdZ74NPJ9_iD1b_AduBjgE_F9NMMPOzH-gjF-7cnHGlbpVAJK-WUom61XDAZz6THxRGjveyuLSF8fozbd7_AC-i-RcK1Cf8A5Y9azGYhWE3o=', start_index=16431)
Annotation(end_index=16764, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6_z9-KecIOjzUKOLMxPqpFZ_l-sodoVFcLcQ8d0Vb4oGDrbZe2yBLHrMYPKT0zIWvB0sgbKCqGJWd5OcyUQO1DVS4p6of85kleb_PT26Uuyyjxe1hfVJh9AtAHA_pjO3xjzx9Zdw=', start_index=16750)
Annotation(end_index=16764, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFP-_cVHPO8gwIHIrIwOh9YIcY2BzyNtBWHx1BY5UTlClle7p8QdOtFqUHGf1yaxbqcI29KsDRvdZtCHq7JOG63_rc43zcTDEW3gV6KGGdgwMFm31IbS6ieJWTMCaMH_Yw=', start_index=16750)
Annotation(end_index=18150, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPIWOnCRn1RLN5yg4r9fYNUr5CHAO-6DQ0E8jSLcOts_bX8M2NDlXPhJ6E9Gpy5JQY1T3WnwLY1E99l6RLOQ8dfrR7bhlkRo2doDfwiiZPvsh96Gw3dWY0LPqG0wqEc57OOGRXaSgZqC04639FLL9MzCzXcg==', start_index=18125)
Annotation(end_index=18150, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyp0CEAEj-YTjn0BorJYiRlrH6K_NFlcveFlIZtA1OJK1vrlh_qLU-Hw8_8cP18y9Q1deS7qennJNCqDFn4ftwuCvAS3x_udcjTO-ZWgb4wmDopTdcaqTfdVKRwTJdX4wNvM0RaOQW7Na8ATD254dr_opSy7VfykUULXpBtH3v_tensr1tRJP-xNjT1wvYugmattY4U1CTfPwx5q1CrHniKwZSLuzbskP2OZbl3MRz_aTw20T7aLxu_yQ=', start_index=18125)
Annotation(end_index=18150, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFG2DzjmkyWqyx1jsgHLhF1DFR8hYIEB-Avic2EqgoH-299PsPfvjC76yXpZz6jB-HeUa2Mtzl_J1ZdY8Q8oLbm6vt1AkzMSJbS6a_E3Dn1eer4F7dzgQ==', start_index=18125)
Annotation(end_index=18150, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnVNflrYSVTEv3QgVQxJjfQXHkH_mXFVZguQLtsNE1ixFNjKJIvNzp-13zCF3v5s7ldzmFdTcrCVAzrZdwBVGZ0JTH4eflRq1f_p0nf1oseksP0mymcq7T1DoqhPJKQ8F2g0-gIylS3UBN9J4rZWAs-XNVC8MgXVbQ7UyNVsFyarNXYF7g6dYQZ0UPZBz61YkyREOektEZdmSuUKJx', start_index=18125)
Annotation(end_index=18150, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGj_hIjTCDtfq23d25V5Sk7fX1Kd8KD8wRLossSVgZtAFgixhi31YFyIqYknRzcXmG_JH2Kn-R3viXERyqFaz9-wN9a074BTmM-HjXe9aheZXj-GscTHZbXwIiWVM7283G0P89syiYA4JyrSRI2OGBICWw061mDiBW-Os1rNIirhOsyzuHodDQxOAmEYo4=', start_index=18125)
Annotation(end_index=18207, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERVoFLq-p0WyhLHPC9gTq5RXG6hz2Lv4aSNb8YKCqVf-fyAAdQcRo7prrzuFzRRlP6HhN0ik1kymyV2lB-u0gM9QX2Rw9ULCh9WllbONWy1687LO25DwtWAyusyZbViy9ptmRnx3Qgm1n1XHXntUwn_iB36TXj3wYSB8NqCKXVUywS4u3t0cjqK5c=', start_index=18186)
Annotation(end_index=18207, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqNAxm6i6iYsVqCeDIoCboqvgwzJKyHl0s87RYEauaaAKXnxuN9dC8Lqmxxro2ushY1Ko9VToeFANAVa5WCpSoJNOW5EsmiFjj20l_dxsBWfa2rp9FARs8eDpcxZxTsoD6xy6HqE1KAWXC1u1DhXaPfvoekER4Q-6HosDJ8QGtwjNdpFbuSVKGYNY=', start_index=18186)
Annotation(end_index=18207, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNxg6GcesOSg1xqR3ZP3uYZy_uJFSa9Tu_DDi6B7VNJ_6qvNfdyNuDwX7oZ-acQ1u87FFQpvYzeHVPsQtKdg9R_TlhLIAhjXQCPgRb6RxPXnhlOLvvMsiai-btvsCMEELhUTZI8HwKQqrc_fs4Vsb6KPKpmZmNEAdRme24GSqWkWJJUXw-erDcXGRRY9XZoeGQXA3tZq0xUEboO3psuJTCH73ZNWSQznYmlp0MbrdJXg2srlh0AdnAnIn7', start_index=18186)
Annotation(end_index=18207, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl_FvVlL9sDRwxnDaJnK_YRJMFYN6j2rM6ZahBdxo45qTG55kC-Q06if_Bj_Dn3b4j1bOyYbLP01Q4eCcAbFR7COCWDDpVhlKy2lA2bMu5zaLoTwkf6LU2u1SdB3w7IpNtH3E3-M-JJ7iyCKyRxqpuPfTit4Tp46B-U7ZK-_WGG6qKP9y_PjaQ45PEsUuEUqSH98a1ppDKFRhFenDLAQVC30Nf', start_index=18186)
Annotation(end_index=18256, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeCJpkKS8AloZJrxULuL_BgmQtX4kiTaPMuvFCWl6-IYdsgQ3tshnZ2vTZIUdFvRM0mbUQb4HsJyejcUAeDavAHETstMlZDJ9gZF_1fkSI1mgYRCfFwKnFBjvSVlE1l-wbvuB6OwqwidkTzcGnQhlx_xtCdEklU1U8BQ==', start_index=18231)
Annotation(end_index=18256, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqJ79c3-57FKunmmRFbu--m0vKh-4Ys7aTFz2T5rmTGrZ0ZhjHmag0IWu1p9_ck8E44BjGYtwiIof6iEIfuKUcaNNNJoZ-VYmpG1axgjLvnNDEkMlaMg==', start_index=18231)
Annotation(end_index=18256, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGu8lAc4riZwcKY_0eZX48z98n7sCyfBXUqOF-0_IIfEdrYyNTagLNGp_mZlhTI6_MQK7xhtOJ3c-CovMFOn65bTq2kdWbQ11YsV3a501SGOJm2xeg_sx99wa9a2rbUP1tjmfxJbv_rO8UcJdvEreANhuOFT69Fmqq60c6yKHsQeXY0MPeJiZYC4ZshWSbaRk7-bVgtwsjzFtXUUXDJLg2oeXA3ZIoYE5lobrD0mkJs6lA=', start_index=18231)
Annotation(end_index=18256, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxcivTH5EUKmQHTlWwH3v-QXIeNsYxm83hIwhFr8A3WWN4M2IROb_9RmfrZamPJ_Whl69icUN-TOiedXHV8q77_ztS_0egwsdoydmh2Wd-xQED0Id-d2Cw7afrADJ74KY7Ac6CFWMo-eQ75hw38iggpe71PiqtjswD4CZO3r12az8JEYdTCWNjqSIX', start_index=18231)
Annotation(end_index=18256, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhf36KRCIYsTE__lEOX4qUp67GZjlZhXIOyu2C-VUSCnDkZwDvgLT5mEq_og6HwYt_OKeG8ZXI6Bf2AUup7WO-thwJTzIPBGz21uuZNgPbRSyRagqxUh6_Btx0JAf-u5xbq_OwNRFOK0c6XNm3l0DZhvLC7dR7jnPyqjYDrhI_CQmsPK4m72iQb0tnZ1SFvUFtY1A-L46sx653_afWYTvVPCDWwy5Z9BPdPEf2g3dM3tN32Q==', start_index=18231)
Annotation(end_index=18256, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHz3QwKSUSYtaYxvGaOcj0f97r3ZcjfSdi_CU32wSwNDH6YEBJq8Wh1rwI8cXVFEO4h6jI2BEpc5tLS7GMOkvZKgWuL1n4pdnT7fDubgQinLEa_15ME0Q==', start_index=18231)
Annotation(end_index=18321, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqXmZ_5Q2sB5Ih5oiMquMHLUUiQcTnZ2qamJU8D_I26qJSn9Jd2jyVjhvBCMZuBMOxsxRc0nUkGujehudgKRUVs2qI9nQRQAmDacFC31fURVK6pIhc5Vc2AsDi7NulfC8gqOHndHvjAIJ2e7nx5K0=', start_index=18303)
Annotation(end_index=18321, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtGRJQp7ThWiN6ds-0gfVjk2VVDTc07NyYJxaGBWzwpAMr3ClXebk_LDEVxbqKzQ1eWYiyIpDRQdBpjw5doVGq7rVlTQvfrqCt-76PXq8OvfDfbZgsQJtYjBZtYD4ICeFCix7j9ZHSsWUOSioslgpBqWCp5T2mfGiV6zy744sEjt13EmhzplKt7hFUyH0-7H2nCZ7HiEGYmQ==', start_index=18303)
Annotation(end_index=18321, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFq7ebrHRMEmg8OLmfodqhsQR4D71V2KJIcqvdhtfzpJ0VNR3YESFnlPo2fzXibJP3jKyFWKqOFNvwPvThsIbLkMDkGU07eitOr5lBBMSC9JV10cyK0fpv9GMB0ZLY33Cki70L6GEJXmua2qK9Tuj12Tyk8E6P_LIkeULg6aa27hw1U9jFL0p6jOZs71KyyeLEN70zOAEhQLJnwVuDv0vkvOdmv86FEC2W_kNean7KGoJWHTYRiCmzuCs5JRito0l-3rxQ=', start_index=18303)
Annotation(end_index=18360, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqmZ_dhbo76Zf_7Csal6ghx7zp9tkrtnyIE5y1I4JOMO3AT2dI-b-bfR98LRHXKLjp4CTQ4pKruuDyrBl1az3aodq3Gzqpe4aDv3C_--h85IuWEsdTkI6ftA==', start_index=18346)
Annotation(end_index=18360, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7z4BkpYp8uGSUr_2zLj6AkucM_Juk2tEiZSGjBOKtDL_pPC1CB2WVXmFvgNGqKl7ps-z_cirflHJUGA56wXtSSVC3WksIFuKwG7oi1tFe3yeGaZhheEXaew==', start_index=18346)
Annotation(end_index=18388, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVFKxDSLVM_B3inazDqvrt3eAcClpanzL2q75i263LwF50mPruGGnV126BOOvpyESpwGxqKV-_nbVjuv0N1nfAG0mTQ01P8U1xCgMuw8GkzNpSZjLzlkkqqKMuuYGej6JOebHUBuTMrAsnivm6hm966V1PY_0vrxYMY-wez3zWEQkHEi3E_Fw9DciDiY6v2mzIxYSjU4rCsRVhp63fLzBW3nxif9fCETh4TQ81ap6LW--gtEN-NNoyr98uSS6jhovDjhGOGViBpzT3w980nQwsLkf4x9F9W00=', start_index=18378)
Annotation(end_index=18440, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFq6CqExm55xv7jNbiuzcgdzM9x8ASRlVZhmxvgaVga69qeo4OWIQ2QpaM6ytfKJkNJJtxtY50NkrdCgUAZEkZ2Fdq4Qs9Nuq3qI6BPYOxko6l3yS-zYzSV8OLxwhT', start_index=18426)
Annotation(end_index=18440, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvFB04ZxSsZKwvXnsD3Hlhb3-95xLxtlZQDR1EUlT9P-ZT242VmV2iv8i1r0mmrY9Pz8Tp5Bh9KHgsTuJpcBOlfo57gUMbvr2rOw6O2yG-NZl0CjfoZ4HyqA7jaR3mfsI=', start_index=18426)
Annotation(end_index=18490, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8Mao-__qxRr2HifZDzIqgOw2jzg7NUx4M5vFp1i45WkkjJLhe5yUa-3PJ0PeaLWCaPxPU3dkEvgcGqFzXpDEpBGTkNYem9G_nsebaUUx4rVc01wLo8SE-sg==', start_index=18472)
Annotation(end_index=18490, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9-4YQ6fP6Bxaa-eLZUigg4Ge-TBBm-5hah_F1o016rtJgHsPBkk0IKv0c9MYRyBm5RBkDIHWiqd3X2ZIohtm-OlY9TIFWlC_UliI9KofP8Ee2Rb5rsHNe26DvePyD9btI34lgtkIxzPQ9MYSzbKvEr2CnCaA5E65pBQ7-e24meZCerjGH', start_index=18472)
Annotation(end_index=18490, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyWnzcDBFx7rzmrobXU_8XGoC9w44HRRrnT25h6e-7Iz7AQ9ch9wPrgA3Ymt_FeqyzolR2WL5kQyNrH3WI87oQDTsL_-cbGEdis4u8VbyUJVPTuNGMy7pEx5KRgtelHg_nBsY6oi7gsC-p_UZBdZ74NPJ9_iD1b_AduBjgE_F9NMMPOzH-gjF-7cnHGlbpVAJK-WUom61XDAZz6THxRGjveyuLSF8fozbd7_AC-i-RcK1Cf8A5Y9azGYhWE3o=', start_index=18472)

## Sources
