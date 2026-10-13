# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** c91bfdae | **Time:** 14.64s | **Cost:** $0.02319
--------------------------------------------------------------------------------

The most practical “sweet-spot” strategy that today’s large-scale trainers converge on is a **three-way combination**:

1. **Mixed-precision back-propagation**  
   - FP16/BF16 for every tensor that is only read or written once (activations, most weights).  
   - FP32 “master” copy of the weights and FP32 loss/gradient scalers.  
   - Automatic loss-scaling (GradScaler) to keep the tiny gradients in the linear range of FP16.  
   → 2× memory reduction, ≥1.5× speed-up on Tensor-Core hardware, and the FP32 master copy prevents the optimizer from “drifting” because of accumulated round-off error.

2. **Gradient-checkpointing (activation recomputation)**  
   - Store only the input of each checkpoint segment; re-run the forward on that segment in the backward pass.  
   - Typical segment length is one Transformer block or one ResNet stage.  
   - Memory grows **O(√L)** instead of **O(L)** in depth, at the cost of one extra forward pass worth of compute (≈20-30 % wall-time).  
   - Lets you keep the per-GPU batch size large enough for stable second-order moment estimates in Adam/AdamW.

3. **AdamW + cosine / linear-warmup + optional clipping**  
   - Adaptive moments give fast, stable early progress; decoupled weight-decay (AdamW) keeps generalisation gap small.  
   - Warmup compensates for the large initial gradient variance that mixed precision + small batch can create.  
   - Global gradient-clipping (norm ≤1.0) is still applied as a cheap guard-rail against the rare FP16 overflow spike.

Together these three pieces hit the desired balance:

- **Convergence stability**: FP32 master weights + loss scaling + Adam’s moments + clipping remove almost all numerical blow-ups.  
- **Generalisation**: AdamW+decay, together with the larger feasible batch size, give the same generalisation curves as full-FP32 training.  
- **Resource cost**: ≈50 % less GPU memory and ≥30 % less wall-time than full-FP32, full-activation training, while the extra compute from checkpointing is usually hidden behind Tensor-Core throughput.

On top of this baseline you can layer higher-level tricks (ZeRO/FSDP sharding, reversible layers, low-rank gradient compression, pipeline parallelism, etc.), but the **“mixed-precision + checkpointing + AdamW” triad”** is the core back-propagation recipe that presently gives the best trade-off between numerical robustness, statistical performance, and hardware utilisation for billion-parameter models.

## Annotations


## Sources
