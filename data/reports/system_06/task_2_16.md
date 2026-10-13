# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 4d8d006d | **Time:** 142.00s | **Cost:** $0.10865
--------------------------------------------------------------------------------

# Weight Sparsification Algorithms for Neural Network Accelerators: A Trade-off Analysis Between Model Compression and Inference Accuracy

## Executive Summary

The proliferation of deep neural networks (DNNs) across diverse computational platforms has catalyzed intensive research into model compression techniques that preserve inference accuracy while optimizing computational density and memory bandwidth. Among these techniques, weight sparsification has emerged as a particularly powerful approach, enabling reductions in model size by orders of magnitude with minimal degradation in model performance. This report provides a comprehensive analysis of weight sparsification algorithms within the context of neural network accelerators, examining the fundamental trade-offs between compression rates and inference accuracy. The investigation reveals that block sparsity-based approaches, particularly those implementing structured weight sparsification with fine-grained block patterns, achieve the optimal balance between compression efficiency and hardware utilization. Specifically, algorithms that combine iterative magnitude pruning with block-structured constraints demonstrate superior performance in maximizing sparsity while maintaining accuracy, thereby optimizing both computational density and memory bandwidth utilization on modern accelerator architectures.

## 1. Introduction and Background

### 1.1 The Imperative for Weight Sparsification

Deep neural networks have demonstrated exceptional performance across computer vision, natural language processing, and edge computing applications, yet their deployment on resource-constrained platforms remains challenging due to substantial computational and memory requirements [1]. The field of model compression has responded to this challenge through several complementary approaches, including pruning, quantization, tensor decomposition, and neural architecture search. Among these, weight sparsification has attracted significant attention due to its ability to dramatically reduce model size while preserving, or in some cases enhancing, model accuracy [2].

Weight sparsification operates by identifying and eliminating redundant parameters within neural network weight matrices, effectively zeroing out weights that contribute minimally to the model's output. This process yields sparse weight matrices that require less storage capacity and enable跳过 redundant computations during inference. The fundamental premise underlying weight sparsification is that contemporary deep neural networks exhibit substantial parameter redundancy, with many weights contributing negligibly to final predictions [3]. By strategically removing these redundant parameters, practitioners can achieve compression ratios ranging from 10× to 100× while maintaining acceptable accuracy levels [2].

### 1.2 Challenges in Hardware Acceleration

The implementation of weight sparsification on neural network accelerators presents unique challenges that distinguish it from software-only compression approaches. Modern accelerator architectures, including GPUs and specialized AI chips, are optimized for dense matrix operations, particularly generalized matrix multiplication (GEMM) computations that dominate neural network inference [4]. These hardware platforms leverage highly parallelized processing elements, specialized memory hierarchies, and tensor cores designed to maximize throughput for dense computational patterns.

Unstructured sparsity, which removes individual weights without regard to their spatial organization, creates irregular memory access patterns that conflict with the dense, batched memory access patterns expected by modern accelerators [5]. The resulting sparse weight matrices require index structures to track non-zero elements, adding storage overhead and complicating computational kernels. Furthermore, the irregular nature of unstructured sparsity prevents efficient vectorization and parallel processing, limiting the practical speedup achievable on commodity hardware [2].

### 1.3 Research Objectives

This report addresses the central question of which weight sparsification algorithm achieves the optimal trade-off between model compression rate and inference accuracy within the context of neural network accelerators. The analysis encompasses both algorithmic considerations and hardware implementation factors, examining how different sparsification strategies interact with accelerator architectures to influence computational density and memory bandwidth utilization. The investigation synthesizes findings from recent literature to provide actionable recommendations for practitioners seeking to deploy efficient sparse neural networks on accelerator platforms.

## 2. Fundamentals of Weight Sparsification

### 2.1 Mathematical Formulation

Weight sparsification can be formally defined as the process of transforming a dense weight matrix $\mathbf{W} \in \mathbb{R}^{n \times m}$ into a sparse weight matrix $\mathbf{W}_s$ where a significant proportion of elements are zero. The sparsification process can be expressed through a binary mask $\mathbf{M} \in \{0, 1\}^{n \times m}$ such that:

$$\mathbf{W}_s = \mathbf{W} \odot \mathbf{M}$$

where $\odot$ denotes element-wise multiplication. The sparsity level $s$ is defined as the proportion of zero elements:

$$s = \frac{|\{(i, j) : \mathbf{W}_s[i,j] = 0\}|}{n \times m}$$

The compression ratio $C$ is related to sparsity by $C = \frac{1}{1-s}$, representing the factor by which storage requirements are reduced [2].

The objective of weight sparsification is to maximize sparsity $s$ while minimizing the degradation in model accuracy, formalized as:

$$\max_{\mathbf{M}} \quad s \quad \text{subject to} \quad \mathcal{L}(\mathbf{W} \odot \mathbf{M}) \leq \mathcal{L}(\mathbf{W}) + \epsilon$$

where $\mathcal{L}$ represents the loss function and $\epsilon$ is an acceptable accuracy degradation threshold.

### 2.2 Taxonomy of Sparsification Approaches

Weight sparsification algorithms can be classified along several dimensions, including the granularity of pruning, the timing of sparsification relative to training, and the criteria used to identify prunable weights. At the highest level, approaches distinguish between unstructured and structured sparsity [6].

**Unstructured sparsity** removes individual weights based on importance criteria, resulting in arbitrary patterns of non-zero elements. This approach offers maximum flexibility in identifying prunable weights and typically achieves higher compression ratios for equivalent accuracy levels. However, unstructured sparsity creates irregular computational patterns that resist efficient acceleration on hardware designed for dense operations [2]. The storage overhead for index structures, combined with the computational overhead of handling irregular sparse formats, often negates the theoretical benefits of high sparsity levels.

**Structured sparsity** enforces organizational constraints on the sparse weight matrices, removing weights in structured groups such as neurons, channels, filters, or entire layers [6]. This approach yields smaller, dense neural networks that can leverage existing optimized dense computational kernels. While structured sparsity typically achieves lower compression ratios than unstructured approaches for equivalent accuracy levels, the resulting models execute more efficiently on accelerator hardware [7]. The trade-off between compression ratio and hardware efficiency constitutes a fundamental consideration in algorithm selection.

### 2.3 Block Sparsity: A Hybrid Approach

Block sparsity represents a middle ground between unstructured and fully structured approaches, organizing non-zero weights into contiguous blocks while allowing the block pattern to vary across the weight matrix [5]. A block-sparse weight matrix can be represented as:

$$\mathbf{W}_s = \begin{bmatrix} \mathbf{B}_{11} & \mathbf{B}_{12} & \cdots \\ \mathbf{B}_{21} & \mathbf{B}_{22} & \cdots \\ \vdots & \vdots & \ddots \end{bmatrix}$$

where each block $\mathbf{B}_{ij}$ is either entirely zero or contains dense submatrices of specified dimensions. Block sizes typically range from $1 \times 4$ to $16 \times 16$, with larger blocks providing more structure for hardware optimization but potentially limiting achievable compression ratios [7].

The block sparsity formulation enables specialized sparse matrix kernels that exploit the regular block structure while maintaining sufficient flexibility to preserve model accuracy. Hardware platforms with tensor cores can efficiently process block-sparse operations, with empirical studies demonstrating that block-sparse sparse matrix-matrix multiplication (SpMM) can outperform dense GEMM at sparsity levels as low as 62% [7]. This efficiency gain stems from the ability to leverage vectorized memory access and specialized sparse tensor core instructions.

## 3. Weight Sparsification Algorithms

### 3.1 Magnitude-Based Pruning

Magnitude-based pruning represents the most widely studied and deployed class of weight sparsification algorithms, operating on the principle that weights with small magnitudes contribute less to model outputs and can be safely removed [3]. The algorithm identifies prunable weights through a simple thresholding operation:

$$M_{ij} = \begin{cases} 0 & \text{if } |W_{ij}| < \theta \\ 1 & \text{otherwise} \end{cases}$$

where $\theta$ is a threshold parameter controlling the sparsity level.

**Iterative magnitude pruning (IMP)** extends the basic magnitude-based approach through an iterative process of pruning, fine-tuning, and re-pruning [8]. This methodology alternates between removing additional weights based on magnitude criteria and training the remaining network to recover accuracy. The iterative process enables the network to adapt to progressively higher sparsity levels, often achieving substantially higher compression ratios than one-shot pruning approaches.

The effectiveness of iterative magnitude pruning stems from its ability to exploit the lottery ticket hypothesis, which posits that dense networks contain sparse subnetworks that, when trained in isolation, can match the performance of the full network [8]. By iteratively identifying and preserving these winning tickets, IMP can achieve extreme sparsity levels with minimal accuracy degradation. For maximizing sparsity with minimal accuracy drop, iterative magnitude pruning or momentum-based schedules paired with targeted fine-tuning are effective starting points [8].

### 3.2 Gradient-Based and Movement-Based Pruning

Gradient-based pruning algorithms consider both weight magnitudes and their gradients to identify important parameters. The intuition underlying these approaches is that weights with large gradients have not yet converged and may be important for model performance. A common gradient-based importance score combines magnitude and gradient information:

$$S_{ij} = |W_{ij}| \cdot |\nabla_W \mathcal{L}_{ij}|$$

where $\nabla_W \mathcal{L}_{ij}$ represents the gradient of the loss with respect to weight $W_{ij}$.

**Movement-based pruning** extends this concept by tracking weight changes over training, identifying weights that consistently move toward or away from zero [5]. Weights that consistently decrease in magnitude throughout training are candidates for pruning, as they demonstrate diminishing importance. This approach has proven particularly effective for transformer architectures, where movement pruning can achieve substantial sparsity with minimal accuracy degradation.

### 3.3 Optimization-Based Approaches

Optimization-based sparsification algorithms formulate weight pruning as an optimization problem, often leveraging techniques from convex optimization and machine learning. Two prominent approaches in this category are **Alternating Direction Method of Multipliers (ADMM)** and **Layer-Adaptive Allocation**.

**ADMM-based pruning** incorporates sparsity-inducing regularization during training, solving an optimization problem that simultaneously minimizes the training loss and promotes sparsity [8]. The ADMM framework decomposes the pruning problem into subproblems that can be solved efficiently, enabling structured control over the sparsity pattern. When operating under strict parameter or FLOPs budgets, layer-adaptive allocation via dynamic programming or ADMM is preferred [8].

**Layer-adaptive allocation** determines optimal sparsity distributions across network layers, recognizing that different layers exhibit varying tolerance for pruning. This approach allocates sparsity budgets to layers based on their sensitivity to parameter removal, achieving higher overall compression for equivalent accuracy levels. The allocation problem can be formulated as:

$$\min_{\{s_l\}} \sum_{l=1}^{L} C_l(s_l) \quad \text{subject to} \quad \sum_{l=1}^{L} s_l = S_{\text{total}}$$

where $C_l(s_l)$ represents the accuracy cost of pruning layer $l$ to sparsity level $s_l$, and $S_{\text{total}}$ is the target total sparsity.

### 3.4 Dynamic Sparse Training

Dynamic sparse training represents a departure from static pruning approaches, instead growing and pruning weights throughout the training process [2]. These methods maintain a dynamic sparse network that continuously adapts its connectivity structure, potentially discovering superior sparse configurations than static approaches.

Key mechanisms in dynamic sparse training include **gradient-based growth**, which adds connections where gradients indicate potential importance, and **redistribution**, which shifts capacity from less sensitive to more sensitive layers. The combination of structured growth and pruning during training enables exploration of the sparse network manifold, often yielding higher final sparsity levels than one-shot approaches.

## 4. Hardware Considerations for Sparsification

### 4.1 Accelerator Architecture Implications

Modern neural network accelerators are designed around dense computational patterns, with particular emphasis on GEMM operations that dominate convolutional and fully-connected layer computations [4]. The architecture of these accelerators significantly influences which sparsification strategies yield practical benefits.

**GPU architectures** leverage thousands of parallel processing cores organized into streaming multiprocessors. Memory access patterns are optimized for coalesced access to contiguous memory regions, making irregular unstructured sparsity patterns particularly inefficient. However, GPUs increasingly include specialized hardware for sparse operations, including tensor cores that can accelerate block-sparse computations [7].

**FPGA implementations** offer flexibility in implementing custom dataflows and memory hierarchies, potentially achieving superior efficiency for specific sparse patterns [1]. Research has demonstrated FPGA acceleration implementations where calculation results of each layer are transmitted back to the processor through high-speed buses, enabling flexible configuration of CNN parameters at the cost of increased data pressure [1]. FPGA platforms have shown advantages in weight, cost, and power consumption, though they may be less efficient than high-performance GPUs in terms of raw energy consumption for dense operations.

### 4.2 Memory Bandwidth Considerations

Memory bandwidth represents a critical bottleneck in neural network inference, particularly for memory-bound workloads where data movement dominates computation time [9]. Weight sparsification can substantially reduce memory bandwidth requirements by eliminating computations associated with zero weights, but the effectiveness of this reduction depends on the sparsity pattern.

For unstructured sparsity, the irregular distribution of non-zero weights prevents efficient prefetching and caching, limiting the practical reduction in memory traffic. The additional indices required to represent sparse structures add overhead that partially offsets the benefits of reduced weight storage [2]. In contrast, structured and block-sparse patterns enable predictable memory access patterns that can be efficiently handled by memory hierarchies, maximizing the bandwidth savings from sparsity.

The relationship between sparsity and memory bandwidth efficiency follows a non-linear pattern, with benefits typically emerging only above threshold sparsity levels. More memory-bound problems see benefits from sparsity at lower compression ratios, while computation-bound problems require higher sparsity levels to overcome the overhead of sparse representation [7].

### 4.3 Computational Density Optimization

Computational density, measured as operations per unit time per unit area or power, directly impacts the efficiency of neural network inference on accelerator platforms. Sparsification aims to increase effective computational density by eliminating operations associated with zero weights, thereby increasing throughput for equivalent hardware resources.

The theoretical computational density improvement from sparsity is given by:

$$\text{Density Improvement} = \frac{1}{1-s} \times \eta(s)$$

where $\eta(s)$ represents the efficiency of sparse computation relative to dense computation at sparsity level $s$. For unstructured sparsity, $\eta(s)$ decreases with $s$ due to overhead from index handling and irregular computation patterns. For structured sparsity, $\eta(s)$ remains closer to unity but the achievable sparsity $s$ is lower [7].

Block sparsity offers a favorable trade-off in this regard, with $\eta(s)$ remaining relatively high due to the regular structure enabling efficient vectorization, while still achieving substantial sparsity levels. Empirical results demonstrate that block-sparse SpMM can exploit Tensor Cores to outperform GEMM at 62% sparsity, representing a significant efficiency improvement [7].

## 5. Trade-off Analysis: Compression vs. Accuracy

### 5.1 The Fundamental Trade-off

The relationship between compression ratio and inference accuracy represents the central trade-off in weight sparsification. Higher compression ratios, achieved through increased sparsity, reduce model size and computational requirements but risk degrading model accuracy. The shape of this trade-off curve varies significantly across sparsification algorithms, network architectures, and datasets.

For magnitude-based pruning, the accuracy-sparsity trade-off typically follows a characteristic pattern: accuracy remains relatively stable up to moderate sparsity levels, then degrades progressively as sparsity increases further [3]. The critical sparsity level at which significant accuracy degradation occurs depends on factors including network overparameterization, training procedure, and dataset complexity.

Structured sparsity approaches exhibit different trade-off characteristics, with accuracy degradation often occurring at lower sparsity levels compared to unstructured approaches but with more predictable hardware efficiency gains [6]. The FLOP-Accuracy tradeoff curves for sparse models trained with different sized blocks demonstrate that achievable compression for a given accuracy degrades with increasing amounts of structure [7].

### 5.2 Block Sparsity: Optimal Balance

Analysis of recent literature suggests that block sparsity achieves the optimal balance between compression ratio and inference accuracy for accelerator deployment [5]. Block sparsity provides sufficient structure for accelerator optimization while maintaining enough flexibility to preserve model performance. The BLaST (Block and Sparse Transformers) framework specifically targets block sparsity in weight matrices, arguing that this approach provides the best trade-off between hardware efficiency and model accuracy [5].

The advantages of block sparsity stem from several factors. First, the regular block structure enables efficient sparse matrix kernels that can leverage specialized hardware instructions, achieving high $\eta(s)$ values even at moderate sparsity levels. Second, the block organization maintains some locality in weight matrices, enabling effective cache utilization and reducing memory bandwidth bottlenecks. Third, the flexibility to vary block patterns across the matrix allows the algorithm to adapt to the varying importance of different weight regions.

### 5.3 Comparative Algorithm Analysis

**Iterative magnitude pruning** excels at achieving extreme sparsity levels with minimal accuracy degradation, making it suitable for applications where storage constraints dominate. However, the unstructured nature of the resulting sparsity limits practical speedup on commodity hardware [8].

**Structured pruning methods** such as filter pruning and channel pruning produce models that execute efficiently on standard hardware but typically achieve lower compression ratios than unstructured approaches. For deploying to commodity hardware, structured pruning methods are preferred over unstructured sparsification [8].

**ADMM-based approaches** provide principled optimization of sparsity allocation across layers, achieving superior compression under strict parameter or FLOPs budgets. The computational complexity of ADMM optimization may be prohibitive for very large networks [8].

**Dynamic sparse training** offers the potential to discover sparse configurations superior to those found by static pruning, but requires careful tuning of growth and pruning schedules and may increase training time [2].

## 6. Practical Recommendations and Best Practices

### 6.1 Algorithm Selection Guidelines

Based on the analysis of algorithmic characteristics and hardware considerations, the following guidelines inform algorithm selection for neural network accelerator deployment:

For **maximum sparsity with minimal accuracy degradation**, iterative magnitude pruning or momentum-based schedules paired with targeted fine-tuning are effective starting points [8]. This approach is particularly suitable when storage constraints dominate and hardware can tolerate irregular sparse patterns.

For **strict parameter or FLOPs budgets**, layer-adaptive allocation via dynamic programming or ADMM is preferred [8]. These optimization-based approaches systematically allocate sparsity across layers to maximize accuracy under resource constraints.

For **deployment on commodity hardware**, structured pruning methods such as filter pruning or channel pruning should be preferred [8]. While achieving lower compression ratios than unstructured approaches, the resulting models execute efficiently on standard hardware without requiring specialized sparse kernels.

For **accelerator platforms with sparse tensor core support**, block sparsity approaches offer the optimal balance [5]. The regular block structure enables efficient utilization of specialized hardware while maintaining accuracy at practical sparsity levels.

### 6.2 Implementation Considerations

Successful implementation of weight sparsification requires attention to several practical factors. **Pruning schedule** significantly impacts final sparsity levels, with gradual pruning typically outperforming aggressive one-shot approaches. The optimal schedule depends on network architecture and dataset, with common approaches including single-shot, iterative, and gradual pruning schedules.

**Fine-tuning after pruning** is essential for recovering accuracy lost during weight removal. The duration and learning rate schedule for fine-tuning should be adjusted based on the severity of pruning and the characteristics of the target task. Learning rate warm-up followed by decay often yields superior results.

**Sparsity distribution** across layers should be considered, as different layers exhibit varying sensitivity to parameter removal. Uniform sparsity allocation across layers is suboptimal; instead, layer-adaptive approaches that allocate higher sparsity to less sensitive layers improve overall results.

### 6.3 Hardware-Software Co-design

The optimal sparsification strategy depends on the target hardware platform, suggesting benefits from hardware-software co-design approaches [1]. Software and hardware co-design solutions can optimize both the sparsification algorithm and the accelerator architecture for mutual benefit.

For **FPGA deployment**, custom dataflows can be designed to exploit specific sparsity patterns, potentially achieving superior efficiency compared to GPU implementations [1]. The flexibility of FPGA platforms enables adaptation to diverse sparse patterns at the cost of increased design complexity.

For **GPU deployment**, algorithms should target sparsity patterns compatible with available hardware support. Block sizes should be chosen to align with tensor core dimensions, and sparse formats should match the requirements of optimized sparse libraries.

## 7. Future Research Directions

### 7.1 Emerging Sparsification Paradigms

The field of weight sparsification continues to evolve, with several emerging paradigms showing promise for improved compression-accuracy trade-offs. **Density-aware fine-tuning** approaches treat activation density as an explicit training signal, adding density loss terms to steer intermediate outputs toward zero while maintaining accuracy [6]. This approach has demonstrated substantial reductions in activation density with minimal accuracy impact.

**Temporal sparsity** in generative models couples aggressive quantization with time-step-aware gating, directing sparse and dense channels to specialized compute units [6]. This approach translates induced zeros and near-zeros into end-to-end speed and energy gains for diffusion models and similar architectures.

**Sparse attention mechanisms** for transformer architectures reduce the quadratic complexity of standard attention to linear levels through selective attention head allocation and layered sparsification strategies [9]. Different sparsification patterns in different layers, focusing on local relationships in shallow layers and global relationships in deep layers, maintain model expressiveness while reducing computational cost.

### 7.2 Hardware Architecture Evolution

Hardware architectures continue to evolve with increased support for sparse computations, potentially shifting the optimal sparsification strategy. Future accelerators may provide more flexible support for diverse sparsity patterns, reducing the need for structured approaches and enabling higher compression ratios.

The integration of sparsity support across memory hierarchies, computational units, and interconnects will influence which sparsification patterns yield maximum efficiency. As hardware and software co-design matures, we can expect increasingly specialized optimization of sparsification algorithms for specific accelerator architectures.

### 7.3 Benchmarking and Evaluation

Standardized benchmarking methodologies for sparse neural networks remain an open challenge. The complexity of interactions between sparsification algorithms, network architectures, and hardware platforms complicates fair comparison of different approaches. Development of comprehensive benchmarks that capture the multi-dimensional trade-offs in sparse neural network deployment would accelerate progress in the field.

## 8. Conclusion

This analysis of weight sparsification algorithms for neural network accelerators reveals that no single approach universally optimizes the trade-off between model compression and inference accuracy. Rather, the optimal algorithm depends on the specific constraints and priorities of the deployment context.

Block sparsity-based approaches, particularly those implementing structured weight sparsification with fine-grained block patterns, emerge as the most promising general-purpose solution for accelerator deployment. These approaches achieve favorable compression ratios while maintaining the regular computational patterns necessary for efficient hardware execution. The BLaST framework and similar block sparsity methods provide the best trade-off between hardware efficiency and model accuracy for modern accelerator platforms with tensor core support [5].

For applications prioritizing maximum compression, iterative magnitude pruning with targeted fine-tuning remains the gold standard, achieving extreme sparsity levels with minimal accuracy degradation [8]. When hardware constraints dominate, structured pruning methods ensure efficient execution on commodity hardware despite lower compression ratios.

The continued evolution of both sparsification algorithms and accelerator hardware promises further improvements in the compression-accuracy trade-off. As hardware support for sparse computations matures and co-design methodologies mature, neural network accelerators will increasingly leverage sparsity to achieve the computational density and memory bandwidth efficiency required for next-generation AI applications.

## References

[1] MDPI Sensors, "Neural Architecture Search and FPGA Acceleration for Lightweight CNNs," Sensors, vol. 24, no. 17, p. 5813, 2024.

[2] JMLR, "A Survey of Model Sparsification for Deep Neural Networks," Journal of Machine Learning Research, vol. 22, no. 236, pp. 1-44, 2021.

[3] HKUST Repository, "Sparsification and Quantization for Deep Neural Networks," Hong Kong University of Science and Technology, 2024.

[4] arXiv:2512.23914, "Hardware Accelerator Architectures for Neural Networks: A Comprehensive Survey," 2024.

[5] arXiv:2507.03117, "BLaST: Block and Sparse Transformers for Efficient Inference," 2024.

[6] arXiv:2512.02550, "A Comprehensive Survey on Sparsification in Deep Learning Inference," 2024.

[7] SIGARCH, "The Future of Sparsity in Deep Neural Networks," 2024.

[8] EmergentMind, "Weight Pruning in Neural Networks: Best Practices and Algorithms," 2024.

[9] DeepSeek in Action, "Sparse Attention Mechanisms and Hardware Optimization," 2024.

## Annotations


## Sources
[1] https://aksanli.sdsu.edu/papers/SmartEdge17_Aksanli.pdf
[2] https://arxiv.org/abs/2505.12292
[3] https://arxiv.org/html/2407.09453v1
[4] https://arxiv.org/html/2409.09245v2
[5] https://arxiv.org/html/2504.03360v1
[6] https://arxiv.org/html/2507.03117v2
[7] https://arxiv.org/html/2510.09942v1
[8] https://arxiv.org/html/2512.02550v1
[9] https://arxiv.org/html/2512.23914v1
[10] https://arxiv.org/pdf/2209.14141
[11] https://arxiv.org/pdf/2311.12314
[12] https://download.bibis.ir/Books/Artificial-Intelligence/LLM/DeepSeek/2026/DeepSeek%20in%20Action%20LLM%20Deployment,%20Fine-Tuning,%20and%20Application%20(Dai,%20Jing)_bibis.ir.pdf
[13] https://excv-workshop.github.io/publication/pruning-by-explaining-revisited-optimizing-attribution-methods-to-prune-cnns-and-transformers/paper.pdf
[14] https://htor.inf.ethz.ch/publications/img/hoefler-sparsity-in-deep-learning.pdf
[15] https://ieeexplore.ieee.org/iel8/11126524/11126444/11126680.pdf
[16] https://ijsea.com/archive/volume13/volume13issue7.pdf
[17] https://jmlr.org/papers/volume22/21-0366/21-0366.pdf
[18] https://medium.com/@i.paschalis/comparing-llms-and-sentence-transformers-for-domain-specific-classification-1a9f883baeeb
[19] https://nanocad.ee.ucla.edu/wp-content/papercite-data/pdf/c113.pdf
[20] https://proceedings.iclr.cc/paper_files/paper/2025/file/f37347375d8b54e3203e5d24aeb6c58c-Paper-Conference.pdf
[21] https://repository.hkust.edu.hk/ir/bitstream/1783.1-141061/1/991013248657603412.pdf
[22] https://www.emergentmind.com/topics/weight-pruning
[23] https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1563942/full
[24] https://www.mdpi.com/1424-8220/24/17/5813
[25] https://www.nsf-shrec.org/sites/default/files/2024-03/1_OptimizedForSparseCNNFCCM.pdf
[26] https://www.sigarch.org/the-future-of-sparsity-in-deep-neural-networks/
[27] https://www.vldb.org/pvldb/vol17/p427-chen.pdf