# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** daa238f8 | **Time:** 22.20s | **Cost:** $0.01445
--------------------------------------------------------------------------------

Perturbations in policy parameters (e.g., visa quotas, border-closure probabilities, repatriation rates, or preferential-trade coefficients) enter a stochastic migration model as **additive or multiplicative shocks to the entries of the time-varying migration matrix**  
M(θ_t) = [m_{ij}(θ_t)], where θ_t is the vector of policy parameters.  
Because every column of M is a probability vector, the matrix is **row-sub-stochastic** and its **spectral radius** ρ(M) satisfies ρ(M) ≤ 1, with equality if and only if the world network is **closed** (no external “rest-of-world” state).

1. **Local first-order effect**  
   Let Δθ be a small policy shock and ΔM its induced change in the matrix.  
   For any eigenvalue λ(θ) with right eigenvector v we have  
   δλ = (w^T ΔM v)/(w^T v)              (1)  
   where w is the left eigenvector.  
   - If the shock **reduces** the probability of leaving country j (m_{•j} decreases), the column sum falls and (1) gives δλ < 0.  
   - If the shock **raises** the probability of moving to a **highly central** destination (a hub that many eigenvector entries touch), the numerator in (1) can be large enough to **increase** λ even when the shock is imposed on a single link.

2. **Global inequality bound**  
   Using the Bauer–Fike theorem we obtain  
   |λ_k(θ+Δθ) – λ_k(θ)| ≤ cond(V) ‖ΔM‖       (2)  
   where cond(V) is the eigenvector condition number.  
   Because ‖ΔM‖ is controlled by the size of the policy perturbation, (2) tells us that **the spectral radius can never jump outside the disk** cond(V)‖ΔM‖ around its pre-shock value; hence **large shocks are required to push ρ across the critical value 1**.

3. **Network topology matters**  
   - **Sparse networks** (few bilateral links) have low cond(V), so ρ moves little.  
   - **Hub-and-spoke** structures (e.g., one large destination) have cond(V) ≫ 1; the same Δθ can then **non-linearly amplify** ρ.  
   - **Closed chains** (cycles) tend to keep ρ ≈ 1; opening any link (policy-induced break) drops ρ discontinuously.

4. **Stochastic versus deterministic propagation**  
   In the stochastic model the matrix is **sampled** from a distribution whose mean is shifted by Δθ.  
   The **expected spectral radius** satisfies  
   E[ρ(M)] ≈ ρ(E[M]) + ½ Tr[Hess(ρ) Σ]       (3)  
   where Σ is the covariance induced by the stochastic sampling.  
   Policy shocks that **raise variance** (e.g., randomised visa lotteries) increase Σ and hence can **raise E[ρ]** even when the mean matrix is unchanged.

5. **Summary rule-of-thumb**  
   - **Restrictive shocks** (lower exit probabilities, higher return rates) → **lower ρ** → faster convergence of migrant stocks to steady state.  
   - **Liberalising shocks** that create **new hub links** or **raise variance** → **higher ρ** → longer memory of shocks, possibly persistent flows.  
   - The **closer the pre-shock ρ is to 1**, the **larger the percentage change** induced by the same absolute Δθ—policy becomes **more potent** in networks that are already close to fully connected.

Hence, perturbations in policy parameters do not merely translate one-for-one into entries of the migration matrix; they **re-weight the entire eigenvector structure**, and the **spectral radius responds with an elasticity that is proportional to the centrality of the perturbed link and to the network’s eigenvector condition number**.

## Annotations


## Sources
