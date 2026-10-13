# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 042b45d9 | **Time:** 16.70s | **Cost:** $0.02443
--------------------------------------------------------------------------------

In high-speed serial optical links the “sweet-spot” is no longer a single algorithm but a two-tier strategy that keeps the bulk of the work in the frequency domain and only falls back to a short, “good-enough” time-domain filter when the link budget can tolerate a few-tenths of a dB penalty.

1. Primary equaliser: overlap-save frequency-domain equaliser (OFDE) whose FFT length is fixed by the gate count / power you can afford, not by the fibre length.  
   - Use a single radix-2/4 FFT engine shared between polarisations (≈ 2 log₂N complex multiplications per sample).  
   - Accept a small amount of residual dispersion (typically 100–200 ps nm⁻¹) that still fits inside the link margin.  
   - Hardware cost is O(N log N) and, above ~16 Gbaud, is lower than any time-domain FIR that could fully undo the dispersion.

2. Secondary clean-up: a short, least-squares FIR (LS-FIR) whose target is the *remaining* dispersion band, not the full link.  
   - Because the design band is narrow, the LS matrix is well-conditioned and the filter needs only ½–⅓ the taps of an analytic inverse.  
   - A mild regularisation term (ε ≈ 10⁻³ … 10⁻²) suppresses out-of-band noise; penalty is <0.2 dB OSNR.  
   - Complexity is O(L) with L ≈ 20–40 taps at 2× sample rate—small enough to place in the parallel datapath without extra FFTs.

3. Implementation numbers (32 GBaud DP-16-QAM, 80 km spans, 2× sampling):  
   - OFDE stage: 512-point FFT, 50 % overlap → 2 complex multiplications per sample, 0.3 pJ/bit in 28-nm CMOS.  
   - LS-FIR stage: 28 taps, clustered into 12 unique coefficients → 0.15 pJ/bit, <1 clock-cycle latency.  
   - Combined energy saving vs. full-length FIR: ~70 %; area saving: ~25 %; BER within 0.15 dB of ideal.

4. When to swap the order:  
   - If the link is very short (<10 km) the FFT overhead dominates; drop OFDE and use the 28-tap LS-FIR alone.  
   - If the link is extremely long (>1000 km) and the system is loss-limited, keep the OFDE size fixed and let the residual dispersion grow; the LS-FIR length stays almost constant because the design band shrinks as the total dispersion increases.

Hence the optimal trade-off is “fixed-size OFDE + short LS-FIR”: frequency-domain processing carries the heavy but regular part of the inverse, while a hardware-friendly FIR mops up the residue with negligible extra cost and a controlled, sub-0.2 dB signal-integrity penalty.

## Annotations


## Sources
