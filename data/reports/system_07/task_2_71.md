# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** a0085208 | **Time:** 17.12s | **Cost:** $0.02402
--------------------------------------------------------------------------------

The asymptotic behavior of age-structured population reproduction functions is governed by the **dominant eigenvalue** and its associated **left and right eigenvectors** of the age-specific transition matrix (commonly the Leslie matrix). Here's a concise breakdown of how eigenvalue decomposition determines this behavior:

---

### 1. **Dominant Eigenvalue (λ₁)**
- **Asymptotic Growth Rate**: The largest eigenvalue, λ₁, determines whether the population grows, declines, or stabilizes:
  - λ₁ > 1: **Population increases** exponentially.
  - λ₁ = 1: **Population stabilizes** (zero long-term growth).
  - λ₁ < 1: **Population declines** to extinction.

---

### 2. **Right Eigenvector (w)**
- **Stable Age Distribution**: The right eigenvector corresponding to λ₁ gives the **proportional age structure** that the population converges to over time, regardless of the initial age distribution.

---

### 3. **Left Eigenvector (v)**
- **Reproductive Value**: The left eigenvector associated with λ₁ quantifies the **expected future contribution** of individuals in each age class to long-term population growth. It reflects how valuable each age class is in terms of reproduction.

---

### 4. **Reproduction Function and Net Reproductive Value**
- The **net reproductive value (R₀)** can be derived from the matrix elements and is related to λ₁. It represents the **average number of daughters a female produces over her lifetime**.
- If R₀ > 1, λ₁ > 1 (population grows).
- If R₀ = 1, λ₁ = 1 (population stable).
- If R₀ < 1, λ₁ < 1 (population declines).

---

### 5. **Transient vs. Asymptotic Behavior**
- While λ₁ and its eigenvectors describe **long-term behavior**, **subdominant eigenvalues** influence **short-term (transient) dynamics**, such as oscillations or delayed convergence to the stable age distribution.

---

### Summary
Eigenvalue decomposition of the age-specific transition matrix reveals:
- **λ₁**: long-term growth rate.
- **w**: stable age structure.
- **v**: reproductive value by age.
- **R₀**: lifetime reproductive output.

Together, these determine the **asymptotic trajectory** of the population reproduction function and its **stable demographic structure**.

## Annotations


## Sources
