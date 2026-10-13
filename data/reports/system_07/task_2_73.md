# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 97beacff | **Time:** 17.15s | **Cost:** $0.01249
--------------------------------------------------------------------------------

Technical-intervention parameters act as *tunable levers* that rescale the entire spectrum of the learning-transfer matrix **W**→α**W** (or more generally **W**→**M**(**W**,θ)) and therefore move its dominant eigenvalue λ₁.  
Because the asymptotic learning rate and the memory horizon of a cognitive network are governed by ρ=|λ₁|, every engineering knob that changes α or the structure of **M** shows up as a monotonic (almost always linear) shift in ρ:

1. **Reservoir spectral radius** (set at init)  
   ρ is literally defined as ρ_init = max|eig(**W_res**)|.  
   Any subsequent intervention that multiplies the reservoir weights (input scaling, feedback gain, regularisation constant, etc.) becomes a multiplicative factor on ρ_init.

2. **Input scaling a_in**  
   In Echo-State/Force networks the effective transfer matrix is  
   **W**_eff = a_in **W**_res + **W**_fb.  
   Empirically ρ_eff ≈ a_in ρ_init (the feedback term is usually low-rank and shifts the spectrum only second-order).  
   Hence a 20 % increase in a_in gives ≈20 % increase in spectral radius and a proportionally faster initial learning rate, but pushes the network closer to the edge of chaos (ρ≈1).

3. **Learning-rate η**  
   Gradient descent on the output weights is equivalent to the iterative map  
   **w**(t+1) = [ **I** – η **X**ᵀ**X** ] **w**(t) + η **X**ᵀ**y**.  
   The matrix in brackets has spectral radius 1 – η μ_min (μ_min smallest eigenvalue of the covariance of reservoir states).  
   Therefore η rescales the *effective* ρ of the *learning dynamics* (not of **W** itself) and controls overshoot: too large an η gives ρ>1 and the read-out weights diverge; too small gives ρ≈1 and learning crawls.

4. **Delay-line or low-pass feedback gain g**  
   In augmented reservoirs (DeLi-ESN, memristive lag lines) the update is  
   **x**(t+1) = (1–g) tanh(**W** **x**(t)+**V** u(t)) + g **x**(t–k).  
   The Jacobian of the map has eigenvalues λ = (1–g) ν + g e^{-iωk}, where ν are the eigenvalues of **W**.  
   The *envelope* spectral radius becomes ρ_env = (1–g) ρ_init + g.  
   Thus increasing the memory gain g monotonically *increases* the spectral radius (adds inertia), which explains why delay lines allow the reservoir to bridge longer temporal gaps but at the price of slower convergence.

5. **Weight regularisation / pruning / spike-threshold adaptation**  
   Any penalty that shrinks weights (L2, homeostatic scaling, STDP soft bounds) divides ρ by the same factor.  
   Pruning 30 % of the synapses typically drops ρ by 5–15 % (depends on degree distribution), moving the network from the chaotic to the ordered regime.

6. **Neuromorphic hardware non-ideality**  
   On analogue memristive crossbars the actual matrix is **W**_phys = **W** + Δ**W** with element-wise multiplicative noise (coefficient σ≈2–5 %).  
   Random-matrix theory gives E[ρ_phys] ≈ ρ(1+σ²N/2).  
   Hence device mismatch can *increase* the spectral radius in large arrays, forcing designers to lower the nominal ρ_init to keep the physical network below the critical value.

**Rule of thumb**  
For small interventions the change in spectral radius is linear and additive:

Δρ ≈ ρ_init ( Δa_in/a_in – Δg – η μ_min + σ²N/2 – λ_reg ),

where each term corresponds to one of the knobs above.  
Because generalisation error in cognitive tasks has a U-shaped dependence on ρ, technical tuning is usually done by scanning one parameter while keeping the combined ρ in the window 0.6–0.95 (task-dependent).

## Annotations


## Sources
