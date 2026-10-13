# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** e9884eb3 | **Time:** 284.25s | **Cost:** $1.36980
--------------------------------------------------------------------------------

# Optimal Weight Sparsification Algorithms for Neural Network Accelerators: Balancing Compression, Accuracy, and Hardware Efficiency

### Key Points
*   **N:M Structured Sparsity (Semi-Structured)** currently represents the optimal trade-off between model compression and hardware efficiency, specifically the **2:4 pattern** supported by NVIDIA Ampere and Hopper architectures. This format doubles computational throughput and reduces memory footprint by 50% with negligible accuracy loss.
*   **Vector-wise N:M (V:N:M)** and **Layer-wise N:M** are emerging as superior evolutions of the standard 2:4 pattern for 2024-2025. V:N:M allows for arbitrary sparsity ratios (e.g., 64:2:5) and higher compression rates (>50%) while maintaining accuracy better than coarse-grained block sparsity.
*   **Learning Best Combination (LBC)** and **ATP (A Theoretical Perspective)** are the leading algorithmic approaches for determining sparsity masks. LBC outperforms gradient-based methods (like SR-STE) by treating sparsification as a combinatorial problem, while ATP optimizes layer-wise sparsity rates using arithmetic progression to prevent reconstruction error explosion in LLMs.
*   **NM-SpMM** is the state-of-the-art software kernel for executing these algorithms, achieving up to 6.3x speedups over dense GEMM and 2.1x over previous sparse libraries by utilizing hierarchical blocking and pipeline optimization.

---

## 1. Introduction

The deployment of Deep Neural Networks (DNNs), particularly Large Language Models (LLMs) and Vision Transformers (ViTs), is increasingly constrained by the "Memory Wall"—the widening gap between computational speed and memory bandwidth. While model parameters have grown exponentially, hardware memory capacity and bandwidth have not kept pace. Weight sparsification, the process of pruning redundant connections in a neural network, offers a pathway to alleviate these bottlenecks by reducing the model size (compression) and the number of required operations (computational density).

However, a critical dichotomy exists in sparsification strategies: **Unstructured Sparsity** offers the highest theoretical compression rates (90–99%) but suffers from irregular memory access patterns that degrade performance on parallel hardware like GPUs. Conversely, **Structured Sparsity** (e.g., block pruning) aligns well with hardware vectors but often incurs significant accuracy penalties at high compression rates.

This report analyzes the algorithmic landscape to identify the "best trade-off" for modern accelerators. The evidence indicates that **Fine-Grained Structured Sparsity (N:M)**, and specifically its recent advancements into **Vector-wise (V:N:M)** and **Layer-wise** configurations, provides the optimal balance. These algorithms, when paired with specialized kernels like **NM-SpMM** and selection methodologies like **LBC** and **ATP**, maximize computational density and memory bandwidth utilization while preserving inference accuracy.

---

## 2. The Paradigm of N:M Structured Sparsity

### 2.1 Definition and Hardware Support
N:M sparsity, often referred to as semi-structured sparsity, enforces a constraint where at most $N$ non-zero elements are permitted within every contiguous block of $M$ elements. The most prominent implementation is the **2:4 pattern** (2 non-zeros per 4 weights), which was introduced with the NVIDIA Ampere architecture and continued in the Hopper architecture [cite: 1, 2].

This pattern is designed specifically for **Sparse Tensor Cores**. By compressing the weight matrix by 50%, the hardware can fetch twice the amount of effective data for the same memory bandwidth and execute math operations at double the rate of dense equivalents [cite: 3]. This directly addresses the user's requirement for optimizing computational density and memory bandwidth.

### 2.2 The Trade-off Advantage
Unlike unstructured sparsity, which requires heavy metadata overhead (indices) and results in non-coalesced memory accesses, N:M sparsity relies on a predictable pattern.
*   **Compression:** It achieves a fixed 50% reduction in model size (for 2:4), which is lower than the 90%+ potential of unstructured pruning but is guaranteed to be hardware-accelerated [cite: 2, 4].
*   **Accuracy:** Research indicates that 2:4 sparsity maintains accuracy significantly better than coarse-grained block sparsity (e.g., pruning entire channels or filters). For instance, ResNet-50 models pruned to 2:4 sparsity achieve Top-1 accuracy comparable to dense baselines, whereas block pruning often degrades performance [cite: 1, 5].
*   **Bandwidth:** By storing weights in a compressed format (often requiring only a 2-bit index per non-zero value for 2:4), N:M sparsity effectively doubles the memory bandwidth for weight transfers [cite: 6].

### 2.3 Limitations of Standard 2:4
While 2:4 is the hardware standard, it is rigid. It fixes the sparsity rate at 50%. Many modern models, particularly over-parameterized Transformers, can tolerate much higher sparsity (e.g., 80-90%) in certain layers without accuracy loss. Standard 2:4 pruning leaves this potential compression on the table. Furthermore, uniform application of 2:4 across all layers is sub-optimal, as some layers are more sensitive to pruning than others [cite: 6, 7].

---

## 3. Advanced Algorithms for Optimal Trade-offs (2024-2025)

To surpass the limitations of fixed 2:4 sparsity, recent research has developed algorithms that offer better trade-offs by introducing flexibility in the $N$ and $M$ parameters and the distribution of sparsity across layers.

### 3.1 Vector-wise N:M Sparsity (V:N:M)
**V:N:M sparsity** represents a significant evolution in structured pruning. Instead of pruning individual weights based on a 2:4 pattern, V:N:M divides the weight matrix into blocks of size $V \times M$ and retains $N$ vectors within that block [cite: 8, 9].

*   **Flexibility:** This format supports arbitrary ratios, such as 64:2:5 or 64:2:8, allowing for sparsity levels significantly higher than 50%.
*   **Performance:** Recent studies show that V:N:M sparse Transformers offer a wider range of speedup-accuracy trade-offs compared to 2:4 sparsity. For example, a DeiT-small model achieves lossless accuracy at **64:2:5 sparsity** (60% sparse), and DeiT-base maintains accuracy at **64:2:8 sparsity** (75% sparse) [cite: 8, 9].
*   **Hardware Compatibility:** Crucially, V:N:M can be accelerated on existing GPUs that support 2:4 sparsity (like NVIDIA A100/H100) by mapping the vector constraints to the hardware's execution units, thereby unlocking speedups for ratios that were previously thought to be incompatible with Sparse Tensor Cores [cite: 7, 10].

### 3.2 Layer-wise N:M Sparsity (ELSA and ATP)
Uniform sparsity (applying the same N:M pattern to every layer) is inefficient because different layers exhibit different sensitivities to pruning.

*   **ELSA (Exploiting Layer-wise N:M Sparsity):** Designed for Vision Transformers (ViTs), ELSA determines a customized N:M configuration for each layer. It considers both the supported sparsity levels of the accelerator and the expected throughput improvement.
    *   *Results:* ELSA achieves a **2.9x reduction in FLOPs** for Swin-B and DeiT-B models with only marginal accuracy degradation, significantly outperforming uniform 2:4 strategies [cite: 6, 11].
    *   *Mechanism:* It trades off negligible accuracy loss for substantial reductions in memory usage and inference time by applying aggressive sparsity to robust layers and conservative sparsity to sensitive ones [cite: 12].

*   **ATP (A Theoretical Perspective):** This algorithm addresses the "reconstruction error explosion" in Large Language Models (LLMs). It posits that reconstruction errors accumulate and amplify through the layers.
    *   *Algorithm:* ATP allocates sparsity rates using a monotonically increasing arithmetic progression. This means deeper layers, which are often more redundant or less sensitive to error propagation in specific architectures, might receive higher sparsity rates.
    *   *Performance:* ATP reduces the perplexity of a 70% sparse LLaMA2-7B model (pruned via Wanda) by **52.10 points** and increases zero-shot accuracy by **10.50%** compared to state-of-the-art methods like AlphaPruning. It achieves **2.23x speedups on GPUs** [cite: 13, 14].

### 3.3 Learning Best Combination (LBC)
Determining *which* weights to keep within the N:M constraint is a combinatorial problem. Traditional methods like **SR-STE** (Sparse-Refined Straight-Through Estimator) use approximate gradients, which can be inefficient and unstable.

*   **Methodology:** LBC reformulates N:M sparsity as a combinatorial search. It assigns a learnable score to each possible combination of weights and optimizes this score jointly with the weights.
*   **Superiority:** LBC consistently outperforms SR-STE. For a ResNet-50 model, LBC achieves **77.2% Top-1 accuracy** (vs. 77.0% for SR-STE) while requiring significantly fewer training FLOPs.
*   **High Sparsity Regime:** LBC is particularly effective at aggressive sparsity levels. At **1:16 sparsity** (approx. 94% sparse), LBC achieves 71.8% accuracy, surpassing unstructured methods like STR by 1.2%, proving that structured sparsity can compete with unstructured compression rates when the selection algorithm is optimized [cite: 15, 16, 17, 18].

---

## 4. Kernel Implementation: The Engine of Efficiency

An algorithm is only as good as its hardware implementation. The theoretical benefits of N:M sparsity must be realized through optimized kernels that manage memory bandwidth and instruction pipelines.

### 4.1 NM-SpMM
**NM-SpMM** is the current state-of-the-art implementation for general N:M sparsity on GPGPUs. It addresses the limitations of vendor libraries like cuSPARSE, which often fail to deliver speedups at lower sparsity levels or for specific matrix shapes.

*   **Hierarchical Blocking:** NM-SpMM employs a hierarchical blocking mechanism to enhance data locality, ensuring that the high-bandwidth memory (HBM) is utilized efficiently.
*   **Pipeline Optimization:** It introduces sparsity-aware pipeline designs to overlap memory access with computation, hiding latency.
*   **Performance:** Experimental results demonstrate that NM-SpMM is **2.1x faster than nmSPARSE** (the previous SOTA) and **1.4x to 6.3x faster than cuBLAS dense GEMM** operations. It approaches the theoretical maximum speedup derived from the reduction in computation [cite: 19, 20, 21, 22].

### 4.2 MACKO-SpMV for Unstructured Sparsity
While N:M is the focus for structured acceleration, recent work on **MACKO-SpMV** has made 50% *unstructured* sparsity viable on GPUs. By using a co-designed format and kernel, MACKO achieves a **1.2-1.5x speedup** over dense representations at 50% sparsity, a regime where traditional CSR formats typically slow down execution. This suggests that for hardware lacking specific N:M support, optimized unstructured kernels can still offer a competitive trade-off [cite: 23].

---

## 5. Synergies with Quantization

To further optimize memory bandwidth and computational density, sparsification is often combined with quantization (reducing precision from FP16 to INT8 or INT4).

### 5.1 SLOPE (Structured Sparsity at Low Precision)
Combining sparsity and quantization often leads to compounded accuracy loss. **SLOPE** is a framework designed to integrate N:M sparsity with low-bit quantization (e.g., 4-bit weights).
*   **Performance:** Under a **4-bit 2:4 sparsity** setting, SLOPE improves ResNet-18 accuracy from 68.36% to **71.11%**, surpassing even the full-precision baseline.
*   **Mechanism:** It uses a directional regularization strategy to align the sparse, quantized weight vectors with the original full-precision vectors, minimizing the "weight discrepancy" that typically degrades performance [cite: 24, 25].

---

## 6. Comparative Analysis of Sparsification Strategies

The following table summarizes the trade-offs of the discussed algorithms based on the research findings:

| Algorithm / Approach | Sparsity Pattern | Compression Rate | Hardware Efficiency | Accuracy Retention | Best Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Standard 2:4** | Fixed N:M (2:4) | 50% | High (Native Tensor Core support) | High | General purpose inference on NVIDIA Ampere/Hopper [cite: 1, 2]. |
| **V:N:M** | Vector-wise N:M | Flexible (>50%) | High (Maps to 2:4 hardware) | High (Better than block) | Transformers requiring >50% compression [cite: 8, 9]. |
| **ELSA** | Layer-wise N:M | Variable (Adaptive) | High (Optimized throughput) | Very High | Vision Transformers (ViT) [cite: 6]. |
| **ATP** | Layer-wise N:M | Variable (Arithmetic) | High | Very High | Large Language Models (LLMs) to prevent error explosion [cite: 13]. |
| **LBC** | Combinatorial N:M | Flexible | High | Best-in-class (beats SR-STE) | Training N:M masks from scratch [cite: 15, 17]. |
| **Unstructured** | Random | Very High (90%+) | Low (requires specialized kernels) | Moderate | Memory-constrained devices without N:M hardware support [cite: 2, 26]. |

---

## 7. Conclusion

To optimize computational density and memory bandwidth in neural network accelerators, the **N:M structured sparsity** paradigm currently offers the best trade-off. Specifically, the **2:4 pattern** is the industrial baseline due to native support in NVIDIA Ampere and Hopper GPUs, providing a reliable 2x throughput increase.

However, for the absolute *best* trade-off in 2024-2025, one must look beyond uniform 2:4 sparsity. The integration of **Vector-wise (V:N:M)** sparsity and **Layer-wise** allocation algorithms like **ELSA** and **ATP** allows for compression rates significantly exceeding 50% while maintaining or even improving accuracy compared to uniform pruning. These algorithms should be trained using combinatorial optimization methods like **LBC** and executed using high-performance kernels like **NM-SpMM** to fully realize the theoretical gains in bandwidth and compute density.

**Recommendation:** For maximizing performance on modern GPU accelerators, implement **Layer-wise V:N:M sparsity** determined by the **ATP** or **ELSA** algorithms, and execute using the **NM-SpMM** kernel. This combination leverages the hardware acceleration of Sparse Tensor Cores while exploiting the non-uniform redundancy of deep neural networks.

**Sources:**
1. [nvidia.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMMXYqaV--PDd2VIuoXt07kSVwsTCreupmwDjtg7vswqyR4F6WTQ9plxkXJjKNcYaIw1EvleG8usRTsuelUgNH-fulBMx2ovTkyxfnYqq--lKTBzCeHBAWmRkbsIpfniR-TnXYMP35VcP6SpOBqfxcnL5uUVX3IYEmVKekIg_oqWUg0grqgFfFAWbACckXjd-aNIU2pSk=)
2. [massedcompute.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBdMmAdBr1Ped0dxCM_2p3gDZYgvKujWaMqIMKfJZjqwkbQXyLBnpddZITWN5soDtZ73siwf13dATlrpzfBz3haX30GM8pCvLSjDlGlT_w7RF92eMh10SayYW-TRdP3Q8Lv2XIvGs_ei3mwJrvx-Kvz5tueHo1YQiZXBMw11HAalwF8U2PlXYcogbuHOiHKyYAWxZd7Mxr6dW0fYykJ_XbO6Irsbz0lrJkV8p16GQOW1_8B3GZH8ifD4q4rr5rtHgyZt67FdrkhhK9ERlcdpcFXiQR7zzzg_kWa7xYhymRdlyoNbKyRhLmclI2IFdjDQ1Pgv99tuZtNtzp0l3Up_c=)
3. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH48Qa2Xzp4MP_FmSwfWV9UDjGAeU19x2qXGcHK6BK6DVJarfk5bqlthIhXA-OgcQF-1X49MXmbfb1QeBpj5KFlhlUF9l0uOh31kCMGM-yyRNk3i_Af)
4. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgFB0tH-pf892V9i8yAyBrxC5NV4I-RqLhk4mhnfe9jwvIKqZ8LwRtgZSY_myQhJP2VYSeL40klaKAsGPKLf8n03Z1rRVDd3YHwjjEMhmCM6iZENF5RStmoCWA0CTVDqYNe68IYX0APVMHOfY45Lk7JAdEFsaGjy1M2USrAqpLy5exv3TCHc8e88wtD5LUNIft2GK6rOBcztebj2KbcXqzesGigCVzJUYh8A==)
5. [openreview.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3F5tu-P_gReVi1BMROuf-8ixZcMBBsqc8gmWJqzAJKY5Wwfaf3wAjbC2nD_6Sqw2rE1KBjykfrrTnJbdcHArqaFcA0-HhT5o9U3Tnvsnoy-XrRpsncoKMz2Af9_I=)
6. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEDvDFCTuGhJRZsDxjujUHe5LcdeL9Nmh6GhFwVgknkVKPp9mE22etSHM7PO6Cb-9_fKQnCurlbjYuxrx2uceXwWwXsxQuaQquDmVXQyESoXF6Fw58iRW9XA==)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5gZliR3xfcnMYOT-SqU0E5tZ60zXdtANbNdavLlzhn2PPyATGqJ2dI7C6dn7P2ZWxmVJYx_q-TTexpRYmC2_LHxpzdlQQu9G32NnLscmfffbLjqNiDb_wirRsPnjtzh18Qw-TkbnTBm1biutCGnmGlO28Whl1RQd3wyq4E9h8Re0V7MaeyGDii-bEmvhjnHTSkcPctUo9886ySrbBRzcbgL28Eaxl9EuXzXZP85E6OQqJ2o8=)
8. [openreview.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4BYWFqBTgp-jLS2jqKUdMAKqfG6s5EPc5BFbvDJsyNTsfY1ejIEhQ5zD6hOIiweSEB6Q4Qs2gNNrxv18_Ha791SNEniIOqz_oab7jUrTv1DqMXN4i3BWWZldI5IxusQ==)
9. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF916OrFuUWb088D2z4A4qcSXuBYWIitO6fVbra1ttoKzDZJQADSqvAdngmWsMKHLQS5sNONYAAsHwg2luVaMx0uXzQdBhJvxJGvBJ1WKiVxErLZofB)
10. [openreview.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_yzYSLTcw5laX0GKxVeslilV9ePg_2hnyDbPTng1ZXdpzKJpoJvNQy2wcPdxkJFL3fIoPi5CQkO_o_r7Nfype3kDjLexsBYNBOznzSAR4KAQdB_D0JO930VU5rdM=)
11. [thecvf.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKfqo29LgOKlo8lb1ezo4cQs5XC93_9CTWFjtiRkuT7HkAhPVXJD0ref_PUIrI4nk9wCZARJfeMBh4i45CvzROcbQdSelxVyeDOvJaSot3rBZ1iSi_4H3SB-6GD_JU9RrMLePjx9VlnqY6zfJHvwctG47w6gyrJAEhruEMoP758Y6hom-oqWAOvmqGcAmpu8tL361p_17_-6SGJWqGYjPHOaNsglLiEO5GtKMcveg2tSnqFhFZAa5MNcbbBk0J1WDvTqsSYqEQWGz44r8vUgaygMcPRYoXx2g=)
12. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXudbQuUOAJpvIS0EkV_EX06mauGQIYGWj_YsHYggqELGGWbulwZSot2nNzWLD-z-tcOnaRGJfxvq9nM4299nFcJYN-oCOL1NztO1WZvUF8d4TlxN0)
13. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvK9QreCaHyl_W9MXc5s7Tu3BsfSiq3cKNdtEdVGlJXrmLRLdItmsMm7Zzw5kXWfsgSbAJfdnsWHRZYY_RpU2TfGv98rfpQlKgCsBX_OI3tCyRO3c6)
14. [openreview.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5YYYF7EJV1syVolg5dISr_JV8KBv0JGiJimDUMVvc7ecyRGaBUEsf9jzES4360jp66_jrX5b6LVFbTRTtuLy0vfVlY4QB-_4g6Paz4KxycSqigl4TMS3xn-0d66ri4w==)
15. [openreview.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwuc2jBUfbrwxv0TO1EQ1nGspISV_lGbA8RIVfTvFWnE5yoXZoJ3BETsqco7csafE-Oc1-W4KTrSkH6KFQWSnxnMJZE4hoaCCeVe6SkZnEV56TTINb8IH3xZE7ZZj6)
16. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6r95ZZGSlYGXnhGk0U3g0MUhZhwcpgoosJjD6hawn_Lyn7Rabx6nRE3zE8ApNi8oojL5bNaMu6PNw5bIG0MTm-MsJfDjpB0AytcreJzK2R32jMi_j)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGI7LgKAC8AwuwFYeSTmcJPJSTcdVEvUjFioWExSXRH8YlFi9FeuTaorv_moVshrVOzUQbYhWfQ6Y4Frq5TP4l8WvjyFL7-hj7QupnysqMsIaM0tthtUp541tFx6peXQuG9h9pDCT6xvpjVl3sRDRKldsxNaUy38U7JUmpwSQiPgqZcToHXYtu5qmuv9O_KGbjYLcLTiPpBvJV3Uw==)
18. [liner.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHR1rIWSNl2xvqAksXxg1jcLzdu769kgyDwV5fQHMm9iHqKU6RTtRNYzwwL7le3IgUWTe_Ort7W62mAahpitdw6hrgUm78lDxcXvo7QZ1pMAS3y-YGIicBB9Q4ldGvC7q3VI5ZkQnUhI4RyKbsxBT9gR3HcpLHgQsvMuJuy8jw0e6e)
19. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFq3pQRRvoqSwoWC4ZixRMYAkQtLAlaWPHr7Zsi6CukahczcLBssd1CoGc-yK1HkFCNPfWYrFmB_UafMruAQFmmV73HqQ5MrG-Uv3ukF9_pDhWZeqlmFKlc)
20. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNfusBFBHkd_MTNgezo1d1IxDB0633WergFFxMeXqj09zO-0JlymcZ1Qi-jjZ9lOyrolOXQWNJjtDxMHsR6NTI0UBfWW1S0edMxagCAjwtK5pGz37w)
21. [siat.ac.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGT6cz9yIGp4CjY024W60VFNzBsIo0DQCIoPUQHfqXSJ5AWZAsz_fcaRr0WJmbvywXPfQ3wBBrBmw1PgHlZ0BPzXt18ZgQ6OHb7XzbLdJphLgqSNZRXCjlhbjK42YLP8fdFntZaPHMxMBVX)
22. [hkbu.edu.hk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtmFiKVvvRfgO0n-VESvBTE1kGwLJ7T7hB2h7Kx4OvEB8GBosdRd8ExrhZKYd6rhEMhJy_irdZTIged9GT9ocuJhTHVck0VNiseu7YupEQ0qvHhDpxFsEDcCeimZn8MqEEKv5Ja8Uh4NS6yUys4V8178uyyTs1TkuOmC6Ikz0l_LO3g6lpyxutOWBA5KM1thi5IU_bxWpeT4h-HqenBOEDsK7ZeA==)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC9PCHyrpAbkBYTvhubGVNIlQusJRcO72CmMHnk20aZjDZYQt-EGH4tM6lmDS7RoTCYnMNIwMKWgdor2dUWEce_UoD5aRFK_J7FQso2hYBTnq2J7N5CLyUM12SaH58fNt9tsG7EEAF9uzR5aaQPT1aX8l56kDXeiME9EorSmCo7ufrW9Ned1i-zEq1X8auZJfNE3cauTqt1-DfcyCOhJ4HeOWHRNpv)
24. [bmva-archive.org.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFH8OP21YhvtYnWwzXJzjmbZOODbh_9wioe4YM44fFzDXI15Ne4M7XmJ_sZM8hOpb7cv5xS8Xa5IKx9zKg8yIVN-_Tgzh5C1cs4t14HsY2VetGrQcEtTW2LZBfZki05nS5VFxVYytFK0P6W1MQrfccY3U1bB7hr05FPZlk)
25. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKeLBjEloTSOQM2Xq-s4qxd_41HSQd8pjfgRihRz1q-rO_mj7hHQrJLi9aBond0mg1eWc9rC8qmoD8Ck-7kMPN0_RQsl4uQDJIspis4OwhVfEVEqyUPfnC)
26. [graphcore.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhdl7SCIDE_ldILN2rtQ0fbauGLog9jbi2RDrlDHisczCdVL1GMfqSgsvz4owIrkPoYZIEUkejESfpXJmBtPuAzJIZJu6aMHIV2ftAwmklBBvag2EDRPhlePzJVYbgZTDqBzuJteca0Hw0JjUsOigGcWQ5iChDl5x1wtfEgvu7vwC_LyRnyOzqIxErPnEQ0J6jR50D2atfg7H8)


## Annotations
Annotation(end_index=3461, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBdMmAdBr1Ped0dxCM_2p3gDZYgvKujWaMqIMKfJZjqwkbQXyLBnpddZITWN5soDtZ73siwf13dATlrpzfBz3haX30GM8pCvLSjDlGlT_w7RF92eMh10SayYW-TRdP3Q8Lv2XIvGs_ei3mwJrvx-Kvz5tueHo1YQiZXBMw11HAalwF8U2PlXYcogbuHOiHKyYAWxZd7Mxr6dW0fYykJ_XbO6Irsbz0lrJkV8p16GQOW1_8B3GZH8ifD4q4rr5rtHgyZt67FdrkhhK9ERlcdpcFXiQR7zzzg_kWa7xYhymRdlyoNbKyRhLmclI2IFdjDQ1Pgv99tuZtNtzp0l3Up_c=', start_index=3449)
Annotation(end_index=3461, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMMXYqaV--PDd2VIuoXt07kSVwsTCreupmwDjtg7vswqyR4F6WTQ9plxkXJjKNcYaIw1EvleG8usRTsuelUgNH-fulBMx2ovTkyxfnYqq--lKTBzCeHBAWmRkbsIpfniR-TnXYMP35VcP6SpOBqfxcnL5uUVX3IYEmVKekIg_oqWUg0grqgFfFAWbACckXjd-aNIU2pSk=', start_index=3449)
Annotation(end_index=3737, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH48Qa2Xzp4MP_FmSwfWV9UDjGAeU19x2qXGcHK6BK6DVJarfk5bqlthIhXA-OgcQF-1X49MXmbfb1QeBpj5KFlhlUF9l0uOh31kCMGM-yyRNk3i_Af', start_index=3728)
Annotation(end_index=4249, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgFB0tH-pf892V9i8yAyBrxC5NV4I-RqLhk4mhnfe9jwvIKqZ8LwRtgZSY_myQhJP2VYSeL40klaKAsGPKLf8n03Z1rRVDd3YHwjjEMhmCM6iZENF5RStmoCWA0CTVDqYNe68IYX0APVMHOfY45Lk7JAdEFsaGjy1M2USrAqpLy5exv3TCHc8e88wtD5LUNIft2GK6rOBcztebj2KbcXqzesGigCVzJUYh8A==', start_index=4237)
Annotation(end_index=4249, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBdMmAdBr1Ped0dxCM_2p3gDZYgvKujWaMqIMKfJZjqwkbQXyLBnpddZITWN5soDtZ73siwf13dATlrpzfBz3haX30GM8pCvLSjDlGlT_w7RF92eMh10SayYW-TRdP3Q8Lv2XIvGs_ei3mwJrvx-Kvz5tueHo1YQiZXBMw11HAalwF8U2PlXYcogbuHOiHKyYAWxZd7Mxr6dW0fYykJ_XbO6Irsbz0lrJkV8p16GQOW1_8B3GZH8ifD4q4rr5rtHgyZt67FdrkhhK9ERlcdpcFXiQR7zzzg_kWa7xYhymRdlyoNbKyRhLmclI2IFdjDQ1Pgv99tuZtNtzp0l3Up_c=', start_index=4237)
Annotation(end_index=4594, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3F5tu-P_gReVi1BMROuf-8ixZcMBBsqc8gmWJqzAJKY5Wwfaf3wAjbC2nD_6Sqw2rE1KBjykfrrTnJbdcHArqaFcA0-HhT5o9U3Tnvsnoy-XrRpsncoKMz2Af9_I=', start_index=4582)
Annotation(end_index=4594, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMMXYqaV--PDd2VIuoXt07kSVwsTCreupmwDjtg7vswqyR4F6WTQ9plxkXJjKNcYaIw1EvleG8usRTsuelUgNH-fulBMx2ovTkyxfnYqq--lKTBzCeHBAWmRkbsIpfniR-TnXYMP35VcP6SpOBqfxcnL5uUVX3IYEmVKekIg_oqWUg0grqgFfFAWbACckXjd-aNIU2pSk=', start_index=4582)
Annotation(end_index=4806, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEDvDFCTuGhJRZsDxjujUHe5LcdeL9Nmh6GhFwVgknkVKPp9mE22etSHM7PO6Cb-9_fKQnCurlbjYuxrx2uceXwWwXsxQuaQquDmVXQyESoXF6Fw58iRW9XA==', start_index=4797)
Annotation(end_index=5297, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5gZliR3xfcnMYOT-SqU0E5tZ60zXdtANbNdavLlzhn2PPyATGqJ2dI7C6dn7P2ZWxmVJYx_q-TTexpRYmC2_LHxpzdlQQu9G32NnLscmfffbLjqNiDb_wirRsPnjtzh18Qw-TkbnTBm1biutCGnmGlO28Whl1RQd3wyq4E9h8Re0V7MaeyGDii-bEmvhjnHTSkcPctUo9886ySrbBRzcbgL28Eaxl9EuXzXZP85E6OQqJ2o8=', start_index=5285)
Annotation(end_index=5297, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEDvDFCTuGhJRZsDxjujUHe5LcdeL9Nmh6GhFwVgknkVKPp9mE22etSHM7PO6Cb-9_fKQnCurlbjYuxrx2uceXwWwXsxQuaQquDmVXQyESoXF6Fw58iRW9XA==', start_index=5285)
Annotation(end_index=5892, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4BYWFqBTgp-jLS2jqKUdMAKqfG6s5EPc5BFbvDJsyNTsfY1ejIEhQ5zD6hOIiweSEB6Q4Qs2gNNrxv18_Ha791SNEniIOqz_oab7jUrTv1DqMXN4i3BWWZldI5IxusQ==', start_index=5880)
Annotation(end_index=5892, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF916OrFuUWb088D2z4A4qcSXuBYWIitO6fVbra1ttoKzDZJQADSqvAdngmWsMKHLQS5sNONYAAsHwg2luVaMx0uXzQdBhJvxJGvBJ1WKiVxErLZofB', start_index=5880)
Annotation(end_index=6367, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4BYWFqBTgp-jLS2jqKUdMAKqfG6s5EPc5BFbvDJsyNTsfY1ejIEhQ5zD6hOIiweSEB6Q4Qs2gNNrxv18_Ha791SNEniIOqz_oab7jUrTv1DqMXN4i3BWWZldI5IxusQ==', start_index=6355)
Annotation(end_index=6367, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF916OrFuUWb088D2z4A4qcSXuBYWIitO6fVbra1ttoKzDZJQADSqvAdngmWsMKHLQS5sNONYAAsHwg2luVaMx0uXzQdBhJvxJGvBJ1WKiVxErLZofB', start_index=6355)
Annotation(end_index=6697, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5gZliR3xfcnMYOT-SqU0E5tZ60zXdtANbNdavLlzhn2PPyATGqJ2dI7C6dn7P2ZWxmVJYx_q-TTexpRYmC2_LHxpzdlQQu9G32NnLscmfffbLjqNiDb_wirRsPnjtzh18Qw-TkbnTBm1biutCGnmGlO28Whl1RQd3wyq4E9h8Re0V7MaeyGDii-bEmvhjnHTSkcPctUo9886ySrbBRzcbgL28Eaxl9EuXzXZP85E6OQqJ2o8=', start_index=6684)
Annotation(end_index=6697, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_yzYSLTcw5laX0GKxVeslilV9ePg_2hnyDbPTng1ZXdpzKJpoJvNQy2wcPdxkJFL3fIoPi5CQkO_o_r7Nfype3kDjLexsBYNBOznzSAR4KAQdB_D0JO930VU5rdM=', start_index=6684)
Annotation(end_index=7356, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEDvDFCTuGhJRZsDxjujUHe5LcdeL9Nmh6GhFwVgknkVKPp9mE22etSHM7PO6Cb-9_fKQnCurlbjYuxrx2uceXwWwXsxQuaQquDmVXQyESoXF6Fw58iRW9XA==', start_index=7343)
Annotation(end_index=7356, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKfqo29LgOKlo8lb1ezo4cQs5XC93_9CTWFjtiRkuT7HkAhPVXJD0ref_PUIrI4nk9wCZARJfeMBh4i45CvzROcbQdSelxVyeDOvJaSot3rBZ1iSi_4H3SB-6GD_JU9RrMLePjx9VlnqY6zfJHvwctG47w6gyrJAEhruEMoP758Y6hom-oqWAOvmqGcAmpu8tL361p_17_-6SGJWqGYjPHOaNsglLiEO5GtKMcveg2tSnqFhFZAa5MNcbbBk0J1WDvTqsSYqEQWGz44r8vUgaygMcPRYoXx2g=', start_index=7343)
Annotation(end_index=7583, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXudbQuUOAJpvIS0EkV_EX06mauGQIYGWj_YsHYggqELGGWbulwZSot2nNzWLD-z-tcOnaRGJfxvq9nM4299nFcJYN-oCOL1NztO1WZvUF8d4TlxN0', start_index=7573)
Annotation(end_index=8346, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5YYYF7EJV1syVolg5dISr_JV8KBv0JGiJimDUMVvc7ecyRGaBUEsf9jzES4360jp66_jrX5b6LVFbTRTtuLy0vfVlY4QB-_4g6Paz4KxycSqigl4TMS3xn-0d66ri4w==', start_index=8332)
Annotation(end_index=8346, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvK9QreCaHyl_W9MXc5s7Tu3BsfSiq3cKNdtEdVGlJXrmLRLdItmsMm7Zzw5kXWfsgSbAJfdnsWHRZYY_RpU2TfGv98rfpQlKgCsBX_OI3tCyRO3c6', start_index=8332)
Annotation(end_index=9376, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6r95ZZGSlYGXnhGk0U3g0MUhZhwcpgoosJjD6hawn_Lyn7Rabx6nRE3zE8ApNi8oojL5bNaMu6PNw5bIG0MTm-MsJfDjpB0AytcreJzK2R32jMi_j', start_index=9354)
Annotation(end_index=9376, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHR1rIWSNl2xvqAksXxg1jcLzdu769kgyDwV5fQHMm9iHqKU6RTtRNYzwwL7le3IgUWTe_Ort7W62mAahpitdw6hrgUm78lDxcXvo7QZ1pMAS3y-YGIicBB9Q4ldGvC7q3VI5ZkQnUhI4RyKbsxBT9gR3HcpLHgQsvMuJuy8jw0e6e', start_index=9354)
Annotation(end_index=9376, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGI7LgKAC8AwuwFYeSTmcJPJSTcdVEvUjFioWExSXRH8YlFi9FeuTaorv_moVshrVOzUQbYhWfQ6Y4Frq5TP4l8WvjyFL7-hj7QupnysqMsIaM0tthtUp541tFx6peXQuG9h9pDCT6xvpjVl3sRDRKldsxNaUy38U7JUmpwSQiPgqZcToHXYtu5qmuv9O_KGbjYLcLTiPpBvJV3Uw==', start_index=9354)
Annotation(end_index=9376, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwuc2jBUfbrwxv0TO1EQ1nGspISV_lGbA8RIVfTvFWnE5yoXZoJ3BETsqco7csafE-Oc1-W4KTrSkH6KFQWSnxnMJZE4hoaCCeVe6SkZnEV56TTINb8IH3xZE7ZZj6', start_index=9354)
Annotation(end_index=10517, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNfusBFBHkd_MTNgezo1d1IxDB0633WergFFxMeXqj09zO-0JlymcZ1Qi-jjZ9lOyrolOXQWNJjtDxMHsR6NTI0UBfWW1S0edMxagCAjwtK5pGz37w', start_index=10495)
Annotation(end_index=10517, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFq3pQRRvoqSwoWC4ZixRMYAkQtLAlaWPHr7Zsi6CukahczcLBssd1CoGc-yK1HkFCNPfWYrFmB_UafMruAQFmmV73HqQ5MrG-Uv3ukF9_pDhWZeqlmFKlc', start_index=10495)
Annotation(end_index=10517, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtmFiKVvvRfgO0n-VESvBTE1kGwLJ7T7hB2h7Kx4OvEB8GBosdRd8ExrhZKYd6rhEMhJy_irdZTIged9GT9ocuJhTHVck0VNiseu7YupEQ0qvHhDpxFsEDcCeimZn8MqEEKv5Ja8Uh4NS6yUys4V8178uyyTs1TkuOmC6Ikz0l_LO3g6lpyxutOWBA5KM1thi5IU_bxWpeT4h-HqenBOEDsK7ZeA==', start_index=10495)
Annotation(end_index=10517, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGT6cz9yIGp4CjY024W60VFNzBsIo0DQCIoPUQHfqXSJ5AWZAsz_fcaRr0WJmbvywXPfQ3wBBrBmw1PgHlZ0BPzXt18ZgQ6OHb7XzbLdJphLgqSNZRXCjlhbjK42YLP8fdFntZaPHMxMBVX', start_index=10495)
Annotation(end_index=11037, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC9PCHyrpAbkBYTvhubGVNIlQusJRcO72CmMHnk20aZjDZYQt-EGH4tM6lmDS7RoTCYnMNIwMKWgdor2dUWEce_UoD5aRFK_J7FQso2hYBTnq2J7N5CLyUM12SaH58fNt9tsG7EEAF9uzR5aaQPT1aX8l56kDXeiME9EorSmCo7ufrW9Ned1i-zEq1X8auZJfNE3cauTqt1-DfcyCOhJ4HeOWHRNpv', start_index=11027)
Annotation(end_index=11889, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFH8OP21YhvtYnWwzXJzjmbZOODbh_9wioe4YM44fFzDXI15Ne4M7XmJ_sZM8hOpb7cv5xS8Xa5IKx9zKg8yIVN-_Tgzh5C1cs4t14HsY2VetGrQcEtTW2LZBfZki05nS5VFxVYytFK0P6W1MQrfccY3U1bB7hr05FPZlk', start_index=11875)
Annotation(end_index=11889, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKeLBjEloTSOQM2Xq-s4qxd_41HSQd8pjfgRihRz1q-rO_mj7hHQrJLi9aBond0mg1eWc9rC8qmoD8Ck-7kMPN0_RQsl4uQDJIspis4OwhVfEVEqyUPfnC', start_index=11875)
Annotation(end_index=12377, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBdMmAdBr1Ped0dxCM_2p3gDZYgvKujWaMqIMKfJZjqwkbQXyLBnpddZITWN5soDtZ73siwf13dATlrpzfBz3haX30GM8pCvLSjDlGlT_w7RF92eMh10SayYW-TRdP3Q8Lv2XIvGs_ei3mwJrvx-Kvz5tueHo1YQiZXBMw11HAalwF8U2PlXYcogbuHOiHKyYAWxZd7Mxr6dW0fYykJ_XbO6Irsbz0lrJkV8p16GQOW1_8B3GZH8ifD4q4rr5rtHgyZt67FdrkhhK9ERlcdpcFXiQR7zzzg_kWa7xYhymRdlyoNbKyRhLmclI2IFdjDQ1Pgv99tuZtNtzp0l3Up_c=', start_index=12365)
Annotation(end_index=12377, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMMXYqaV--PDd2VIuoXt07kSVwsTCreupmwDjtg7vswqyR4F6WTQ9plxkXJjKNcYaIw1EvleG8usRTsuelUgNH-fulBMx2ovTkyxfnYqq--lKTBzCeHBAWmRkbsIpfniR-TnXYMP35VcP6SpOBqfxcnL5uUVX3IYEmVKekIg_oqWUg0grqgFfFAWbACckXjd-aNIU2pSk=', start_index=12365)
Annotation(end_index=12540, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4BYWFqBTgp-jLS2jqKUdMAKqfG6s5EPc5BFbvDJsyNTsfY1ejIEhQ5zD6hOIiweSEB6Q4Qs2gNNrxv18_Ha791SNEniIOqz_oab7jUrTv1DqMXN4i3BWWZldI5IxusQ==', start_index=12528)
Annotation(end_index=12540, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF916OrFuUWb088D2z4A4qcSXuBYWIitO6fVbra1ttoKzDZJQADSqvAdngmWsMKHLQS5sNONYAAsHwg2luVaMx0uXzQdBhJvxJGvBJ1WKiVxErLZofB', start_index=12528)
Annotation(end_index=12673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEDvDFCTuGhJRZsDxjujUHe5LcdeL9Nmh6GhFwVgknkVKPp9mE22etSHM7PO6Cb-9_fKQnCurlbjYuxrx2uceXwWwXsxQuaQquDmVXQyESoXF6Fw58iRW9XA==', start_index=12664)
Annotation(end_index=12815, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvK9QreCaHyl_W9MXc5s7Tu3BsfSiq3cKNdtEdVGlJXrmLRLdItmsMm7Zzw5kXWfsgSbAJfdnsWHRZYY_RpU2TfGv98rfpQlKgCsBX_OI3tCyRO3c6', start_index=12805)
Annotation(end_index=12946, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGI7LgKAC8AwuwFYeSTmcJPJSTcdVEvUjFioWExSXRH8YlFi9FeuTaorv_moVshrVOzUQbYhWfQ6Y4Frq5TP4l8WvjyFL7-hj7QupnysqMsIaM0tthtUp541tFx6peXQuG9h9pDCT6xvpjVl3sRDRKldsxNaUy38U7JUmpwSQiPgqZcToHXYtu5qmuv9O_KGbjYLcLTiPpBvJV3Uw==', start_index=12932)
Annotation(end_index=12946, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwuc2jBUfbrwxv0TO1EQ1nGspISV_lGbA8RIVfTvFWnE5yoXZoJ3BETsqco7csafE-Oc1-W4KTrSkH6KFQWSnxnMJZE4hoaCCeVe6SkZnEV56TTINb8IH3xZE7ZZj6', start_index=12932)
Annotation(end_index=13116, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhdl7SCIDE_ldILN2rtQ0fbauGLog9jbi2RDrlDHisczCdVL1GMfqSgsvz4owIrkPoYZIEUkejESfpXJmBtPuAzJIZJu6aMHIV2ftAwmklBBvag2EDRPhlePzJVYbgZTDqBzuJteca0Hw0JjUsOigGcWQ5iChDl5x1wtfEgvu7vwC_LyRnyOzqIxErPnEQ0J6jR50D2atfg7H8', start_index=13103)
Annotation(end_index=13116, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBdMmAdBr1Ped0dxCM_2p3gDZYgvKujWaMqIMKfJZjqwkbQXyLBnpddZITWN5soDtZ73siwf13dATlrpzfBz3haX30GM8pCvLSjDlGlT_w7RF92eMh10SayYW-TRdP3Q8Lv2XIvGs_ei3mwJrvx-Kvz5tueHo1YQiZXBMw11HAalwF8U2PlXYcogbuHOiHKyYAWxZd7Mxr6dW0fYykJ_XbO6Irsbz0lrJkV8p16GQOW1_8B3GZH8ifD4q4rr5rtHgyZt67FdrkhhK9ERlcdpcFXiQR7zzzg_kWa7xYhymRdlyoNbKyRhLmclI2IFdjDQ1Pgv99tuZtNtzp0l3Up_c=', start_index=13103)

## Sources
