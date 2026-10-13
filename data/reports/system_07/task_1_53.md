# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 198d0411 | **Time:** 17.86s | **Cost:** $0.01188
--------------------------------------------------------------------------------

Laplacian eigenvalues of mobility functions act as **spectral trip-wires** that tell us when a social-stratification network stops being “liquid” (permeable) and starts to freeze into a caste-like structure.  
The mechanism is easiest to read in three steps.

-------------------------------------------------
1.  Mobility as a diffusion process  
-------------------------------------------------
Let  

  P(t)=e^{−tL}  with L=D−A  (combinatorial Laplacian)

be the **continuous-time random-walk** that encodes how status (education, income, occupation) diffuses along the edges of the network.  
- Rows of P(t) give the probability that a child of a family in group i ends up in group j after “social time” t.  
- The rate of convergence to the stationary (perfect-mobility) distribution is governed by the **spectral gap** λ₂ (the smallest non-zero eigenvalue of L).  
  ‖p(t)−π‖≤C e^{−λ₂t}.  

Hence **λ₂ sets the intrinsic time-scale of social fluidity**: large λ₂⇔rapid mixing⇔high mobility; small λ₂⇔slow mixing⇔stratification.

-------------------------------------------------
2.  Threshold of solidification  
-------------------------------------------------
“Structural solidification” is declared when the **exit time** from the current class becomes macroscopic (larger than the demographic observation window T).  
Solve  

  e^{−λ₂T}≈θ  (θ≈0.05, say)

for λ₂.  The critical value  

  λ₂^{crit}=−ln θ/T    (1)

is the **solidification threshold**:  
- If the empirical network has λ₂<λ₂^{crit} the diffusion is effectively frozen; mobility tables look diagonal (Quasi-perfect immobility).  
- If λ₂>λ₂^{crit} the society is still fluid; the inter-generational correlation decays within the horizon T.

Because λ₂ is the **algebraic connectivity**, anything that lowers it—removal of cross-class bridges, differential homophily, spatial segregation, or exclusionary institutions—pushes the system below the threshold and “freezes” the rank ordering.

-------------------------------------------------
3.  Higher eigenvalues – graded cementation  
-------------------------------------------------
The next eigenvalues λ₃,λ₄,… mark **finer blocks** of the stratification.  
- A **multiplicity gap** after λ_k indicates k socially insulated blocks (Fiedler blocks).  
- The **cumulative eigenvalue weight**  

  Ξ(k)=∑_{i=2}^{k}λ_i/∑_{i=2}^{n}λ_i    (2)

measures the fraction of “mobility energy” already captured by the first k-1 barriers.  
When Ξ(k) exceeds a preset tolerance (say 0.9) the remaining eigen-directions carry practically no diffusion current, i.e. the social hierarchy has **graded cementation** with k effective strata.

-------------------------------------------------
Practical recipe
-------------------------------------------------
1.  Build the mobility graph G: nodes = social categories (micro-classes), weighted edges = observed inter-class flows.  
2.  Compute the Laplacian spectrum {λ_i}.  
3.  Read λ₂ against (1) to test global fluidity.  
4.  Inspect the sequence λ₃,λ₄,… and the curve Ξ(k) to count the number of quasi-rigid layers.  

Thus Laplacian eigenvalues do not merely describe the network; they **delimit the quantitative boundary** between a permeable, opportunity-open society and a solidified, caste-like order.

## Annotations


## Sources
