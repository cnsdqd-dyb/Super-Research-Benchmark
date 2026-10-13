# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 966e2283 | **Time:** 17.26s | **Cost:** $0.01254
--------------------------------------------------------------------------------

The convergence speed of a Markov chain that is supposed to describe “who has power over whom” in a global network is dictated by the second-largest singular value σ₂ of the transition matrix P.  
If the singular values of P decay quickly (σ₂ ≪ 1) the chain forgets its starting state in O(log N) steps; if σ₂ ≈ 1 it needs Θ(N²) or more.

How does the power-law topology enter this picture?  
The adjacency matrix A of a globalization network (trade, AS-level Internet, supply-chain, FDI, etc.) is sparse with degree distribution p(k) ∼ k^(−γ).  
The row-stochastic matrix we actually iterate is  

P = D^(−1)A, D = diag(k₁,…,k_N).

Singular values of P are bounded by those of the symmetric matrix  

M = D^(−1/2) A D^(−1/2),

whose spectrum is completely fixed by the exponent γ and the minimum/maximum degrees k_min, k_max:

1. For γ > 3 the largest degrees are k_max ∼ N^(1/(γ−1)) and the second eigenvalue λ₂ of M satisfies  
   λ₂ ≤ 1 − c (k_min / k_max) = 1 − Θ(N^(−1/(γ−1))).  
   Hence σ₂ = √λ₂ ≈ 1 − Θ(N^(−1/(γ−1))), giving a spectral gap that shrinks polynomially in N.  
   The mixing time is therefore  
   t_mix ∼ (1 − σ₂)^(−1) ∼ N^(1/(γ−1)).

2. For 2 < γ < 3 the second moment ⟨k²⟩ diverges, k_max ∼ N^(1/(γ−1)) ≫ ⟨k⟩, and the graph acquires a “hub” core.  
   The same bound becomes 1 − σ₂ = Θ(k_min / k_max) = Θ(N^(−(3−γ)/(γ−1))), so  
   t_mix ∼ N^((3−γ)/(γ−1)) — still polynomial but with a smaller exponent.

3. For γ → 2 the graph is dominated by a few ultra-high degree nodes; the second singular value approaches 1 as  
   1 − σ₂ ∼ (log N)^(−1), hence t_mix ∼ log N — the hub core acts as a fast expander and the chain mixes almost as quickly as on a complete graph.

4. When γ > 4 the network is essentially homogeneous (finite ⟨k²⟩), the singular-value gap becomes independent of N and t_mix = O(log N).

Singular-value decomposition gives the quantitative tool:  
write P = U Σ Vᵀ; the decay rate of the diagonal entries Σ_ii tells us how many “modes” of the power distribution survive for how long.  
A quick decay (large γ or strong core-periphery structure) means only the first few singular vectors carry persistent structure—power differences equilibrate rapidly.  
A slow decay (γ ≈ 2–2.5) leaves many singular values close to 1; the chain retains long-lived metastable states that correspond to rich-get-richer traps in the globalization network.

In short: the heavier the tail of the power-law (smaller γ), the closer σ₂ is pushed toward 1, the narrower the singular-value gap, and the longer the Markov chain of global power dynamics takes to converge.

## Annotations


## Sources
