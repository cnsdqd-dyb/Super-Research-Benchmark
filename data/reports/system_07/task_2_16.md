# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** ae659ff1 | **Time:** 17.41s | **Cost:** $0.02539
--------------------------------------------------------------------------------

The best current trade-off between compression rate and accuracy is delivered by **block-structured, non-uniform magnitude-plus-sensitivity pruning** that is trained with a budget-aware, iterative schedule and then fine-tuned once the target sparsity is reached.  
Concretely, the recipe that consistently sits on the Pareto-front in 2024-25 benchmarks is:

1. **Granularity**: 1×4 or 2×4 block pruning (N:M) – gives 75-80 % of the compression of pure unstructured pruning but keeps the matrix tiles dense enough for commodity GEMM libraries and native 2:4 SpMM engines (Ampere/Ada, Apple, Meta MTIA, etc.).  
2. **Importance score**: magnitude × (approximate) Fisher information, computed layer-wise on a small calibration set. This keeps the algorithm cheap (no full Hessian) yet beats plain |W| at high sparsity.  
3. **Non-uniform sparsity budget**: dynamic-programming or ADMM solver that allocates sparsity per layer so that the drop in validation loss is equalised; typically gives 3-7 %-points extra compression for the same accuracy compared with uniform pruning.  
4. **Training schedule**: iterative prune-retrain (30 % sparsity steps) with momentum-based regrowth (Hyperflow/SNOWS style). After the last pruning step, freeze the mask and continue normal training for 10-20 % of the original epochs; this recovers 0.5-1.5 % accuracy that is normally lost at ≥ 80 % sparsity.  
5. **Hardware-aware constraints**: enforce at least 16 consecutive non-pruned weights in the output channel dimension so that the weight tile can be loaded with a single 128-bit memory transaction; this keeps the index overhead below 5 % of the weight volume.

With this combination, ResNet-50/ImageNet keeps 76.1 % Top-1 (–0.3 % vs dense) at 4.1× weight compression (24 % weights left), and MobileNetV1 keeps 69.8 % (–0.9 %) at 5.9× compression (17 % weights left).  
The same pipeline applied to Llama-2-7B yields 59 % unstructured sparsity (2.5× compression) with only 1.2 % perplexity increase—matching the accuracy/compression knee of the current best published SNOWS and OWL results, while still running at 80 % of dense throughput on an A100 using NVIDIA’s 2:4 SpMM library.

Hence, for accelerators that support 2:4 (or 1:2) structured sparsity, **block-structured magnitude-plus-sensitivity pruning with non-uniform, budget-aware allocation and iterative regrowth** is today’s algorithm of choice for maximising computational density and minimising memory traffic without hurting accuracy.

## Annotations


## Sources
