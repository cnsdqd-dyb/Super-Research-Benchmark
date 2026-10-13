# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** ef7155f0 | **Time:** 316.68s | **Cost:** $1.45239
--------------------------------------------------------------------------------

# The Eigenvalue Decomposition of Age-Specific Transition Matrices and the Asymptotic Behavior of Population Reproduction Functions

**Key Points**
*   **Eigenvalue Decomposition as Spectral Analysis:** The eigenvalue decomposition of a Leslie matrix breaks down population dynamics into a set of geometric growth modes. The total population behavior is a linear combination of these modes, weighted by the initial population structure.
*   **Dominant Eigenvalue ($\lambda_1$) and Asymptotic Growth:** According to the Perron-Frobenius theorem, a primitive Leslie matrix possesses a single, dominant, real, positive eigenvalue. As time approaches infinity, this eigenvalue determines the finite rate of population increase (or decrease), overriding all other modes.
*   **Dominant Eigenvector and Stable Age Distribution:** The eigenvector associated with the dominant eigenvalue represents the stable age distribution. Regardless of the initial population state, the age structure converges to this vector as transient dynamics fade.
*   **Subdominant Eigenvalues and Transient Oscillations:** The non-dominant eigenvalues (often complex conjugate pairs) govern the transient behavior. They generate demographic waves and oscillations that decay over time. The "damping ratio"—the ratio of the dominant eigenvalue to the magnitude of the second-largest eigenvalue—quantifies the speed of convergence to the stable state.
*   **Equivalence to the Euler-Lotka and Renewal Equations:** The characteristic equation of the Leslie matrix is a discrete discretization of the Euler-Lotka equation. Consequently, the eigenvalues of the matrix correspond to the roots of the characteristic equation derived from the net maternity function in the continuous renewal equation, unifying matrix and integral approaches to demography.

---

## 1. Introduction

The mathematical modeling of structured populations is a cornerstone of theoretical ecology and demography. Among the various frameworks employed, the discrete-time, age-structured model known as the Leslie matrix is paramount. This model projects the future state of a population based on age-specific survival probabilities and fertility rates. While the iteration of the matrix allows for step-by-step simulation, the analytical power of the model lies in its **eigenvalue decomposition (EVD)**.

The query addresses a fundamental relationship in mathematical biology: how the spectral properties (eigenvalues and eigenvectors) of the transition matrix dictate the long-term (asymptotic) behavior of the population's reproduction and structure. This report provides an exhaustive analysis of this relationship. It explores how the decomposition of the state vector into eigenmodes reveals the "memory" of the population, the decay of demographic waves, and the inevitable convergence to a stable age distribution as predicted by the Perron-Frobenius theorem. Furthermore, it connects these matrix-theoretic results to the continuous-time renewal equation and the net maternity function, demonstrating that the Leslie matrix is effectively a discretization of the fundamental integral equations of demography.

## 2. Mathematical Foundations of the Leslie Model

To understand the asymptotic behavior, one must first define the structural properties of the transition matrix and the dynamic system it represents.

### 2.1 The Leslie Matrix Structure
The Leslie matrix, denoted typically as $\mathbf{L}$, is a square $n \times n$ matrix where $n$ represents the number of age classes (or stages) in the population. The state of the population at time $t$ is described by a column vector $\mathbf{n}(t)$, where the $i$-th entry represents the number of individuals in age class $i$ [cite: 1, 2].

The matrix $\mathbf{L}$ has a specific sparse structure characterized by non-negative entries [cite: 3, 4]:
1.  **The First Row (Fertility):** The top row contains the age-specific fertilities (or fecundities), denoted $F_i$ or $b_i$. These represent the average number of viable offspring produced by an individual in age class $i$ that survive to the next census period [cite: 5, 6].
2.  **The Subdiagonal (Survival):** The subdiagonal contains the survival probabilities, $P_i$ (or $s_i$), representing the probability that an individual in age class $i$ survives to enter age class $i+1$ [cite: 3, 5].
3.  **Zero Entries:** All other entries are typically zero, reflecting the biological impossibility of skipping age classes or reversing aging [cite: 4, 5].

Mathematically, the system evolves according to the linear difference equation:
\[ \mathbf{n}(t+1) = \mathbf{L} \mathbf{n}(t) \]
Iterating this process yields:
\[ \mathbf{n}(t) = \mathbf{L}^t \mathbf{n}(0) \]
where $\mathbf{n}(0)$ is the initial population vector [cite: 6, 7].

### 2.2 The Projection Process
The projection $\mathbf{n}(t+1) = \mathbf{L} \mathbf{n}(t)$ mixes the age classes. The first row sums the reproductive contributions of all classes to generate the new cohort (age class 1), while the subdiagonal shifts survivors to the next developmental stage. The asymptotic behavior of this system—what happens as $t \to \infty$—is not immediately obvious from simple iteration but is fully determined by the spectral properties of $\mathbf{L}$ [cite: 1].

## 3. Eigenvalue Decomposition and Spectral Analysis

The mechanism by which the transition matrix determines asymptotic behavior is best understood through eigenvalue decomposition. This process transforms the coupled geometric growth of age classes into a set of uncoupled scalar growth modes.

### 3.1 The Characteristic Equation
The eigenvalues $\lambda$ of $\mathbf{L}$ are the roots of the characteristic polynomial:
\[ \det(\mathbf{L} - \lambda \mathbf{I}) = 0 \]
For a Leslie matrix, this polynomial takes a specific form known as the Euler-Lotka equation (in discrete time). Expanding the determinant yields:
\[ \lambda^n - F_1 \lambda^{n-1} - P_1 F_2 \lambda^{n-2} - P_1 P_2 F_3 \lambda^{n-3} - \dots - (P_1 P_2 \dots P_{n-1}) F_n = 0 \]
Dividing by $\lambda^n$, we obtain the discrete Euler-Lotka equation:
\[ 1 = \sum_{i=1}^n \lambda^{-i} l_i F_i \]
where $l_i = \prod_{j=1}^{i-1} P_j$ is the survivorship (probability of surviving from birth to age $i$) [cite: 8, 9]. This equation is crucial because it links the matrix eigenvalues directly to the **net maternity function** ($l_i F_i$), which describes the expected number of offspring produced by an individual at age $i$.

### 3.2 Spectral Decomposition of the State Vector
Assuming $\mathbf{L}$ has $n$ distinct eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_n$ and a complete set of linearly independent eigenvectors $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n$, any initial population vector $\mathbf{n}(0)$ can be expressed as a linear combination of these eigenvectors:
\[ \mathbf{n}(0) = c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \dots + c_n \mathbf{v}_n \]
where $c_i$ are scalar coefficients determined by the initial conditions [cite: 6, 7].

Applying the matrix $\mathbf{L}$ $t$ times to this expansion utilizes the definition $\mathbf{L}\mathbf{v}_i = \lambda_i \mathbf{v}_i$:
\[ \mathbf{n}(t) = \mathbf{L}^t \mathbf{n}(0) = c_1 \lambda_1^t \mathbf{v}_1 + c_2 \lambda_2^t \mathbf{v}_2 + \dots + c_n \lambda_n^t \mathbf{v}_n \]
This equation is the "master key" to understanding the asymptotic behavior [cite: 6]. The population at time $t$ is a superposition of $n$ geometric growth processes. The $i$-th mode grows (or decays) at a rate determined by $\lambda_i$ and maintains a structure determined by $\mathbf{v}_i$.

## 4. The Perron-Frobenius Theorem in Demography

The behavior of the summation derived above as $t \to \infty$ depends entirely on the relative magnitudes of the eigenvalues. The Perron-Frobenius theorem provides the theoretical guarantee that a stable asymptotic state exists.

### 4.1 Primitivity and Irreducibility
A Leslie matrix is **non-negative** (all entries $\ge 0$). It is **irreducible** if every age class contributes to the future population (i.e., survival rates are non-zero up to the last reproductive age, and the last age class reproduces or contributes to a reproducing class) [cite: 3, 10].
Crucially, the matrix is **primitive** if the greatest common divisor of the ages at which reproduction occurs is 1. Primitivity ensures that the population does not get stuck in a cycle (e.g., a 2-year cycle where reproduction only happens at even ages) [cite: 3, 11].

### 4.2 The Dominant Eigenvalue ($\lambda_1$)
For a primitive, irreducible Leslie matrix, the Perron-Frobenius theorem guarantees the following [cite: 3, 4, 12, 13]:
1.  There exists a real eigenvalue $\lambda_1 > 0$ (the spectral radius).
2.  $\lambda_1$ is strictly greater than the modulus of any other eigenvalue ($|\lambda_1| > |\lambda_i|$ for $i > 1$).
3.  $\lambda_1$ is a simple root of the characteristic equation (algebraic multiplicity 1).
4.  The eigenvector $\mathbf{v}_1$ associated with $\lambda_1$ has strictly positive entries.

### 4.3 Asymptotic Convergence
Because $\lambda_1$ is strictly dominant, as $t \to \infty$, the term containing $\lambda_1$ in the spectral expansion overwhelms all other terms. We can factor out $\lambda_1^t$:
\[ \mathbf{n}(t) = \lambda_1^t \left[ c_1 \mathbf{v}_1 + c_2 \left(\frac{\lambda_2}{\lambda_1}\right)^t \mathbf{v}_2 + \dots + c_n \left(\frac{\lambda_n}{\lambda_1}\right)^t \mathbf{v}_n \right] \]
Since $|\lambda_i| < \lambda_1$, the ratios $(\lambda_i / \lambda_1)^t$ approach zero as $t \to \infty$. Thus:
\[ \lim_{t \to \infty} \mathbf{n}(t) \approx c_1 \lambda_1^t \mathbf{v}_1 \]
This result dictates that asymptotically, the population grows geometrically at a rate $\lambda_1$ and aligns with the structure $\mathbf{v}_1$ [cite: 1, 6, 14].

## 5. Asymptotic Behavior and Population Reproduction Functions

The eigenvalue decomposition does not merely predict total numbers; it determines the functional shape of reproduction over time.

### 5.1 The Stable Age Distribution
The right eigenvector $\mathbf{v}_1$ corresponds to the **stable age distribution** [cite: 1, 2, 7]. This vector represents the proportion of individuals in each age class. The EVD proves that this distribution is independent of the initial population $\mathbf{n}(0)$ (provided $c_1 \neq 0$, which is true for non-negative non-zero initial vectors).
*   If $\lambda_1 > 1$, the population grows exponentially, but the *proportion* of young vs. old remains constant [cite: 2, 15].
*   If $\lambda_1 < 1$, the population declines to extinction, but maintains the stable structure during the decline [cite: 2, 16].

### 5.2 Reproductive Value
The left eigenvector $\mathbf{w}_1$ associated with $\lambda_1$ (where $\mathbf{w}_1^T \mathbf{L} = \lambda_1 \mathbf{w}_1^T$) defines the **reproductive value** of each age class [cite: 4]. It quantifies the expected future contribution of an individual of age $i$ to the gene pool. The EVD implies that asymptotically, the contribution of the initial population to the future population is weighted by these reproductive values.

### 5.3 The Net Maternity Function and $R_0$
The net maternity function, $\phi(a) = l(a)m(a)$, is central to the Euler-Lotka equation. The area under this curve is the Net Reproductive Rate, $R_0$:
\[ R_0 = \sum l_i F_i \]
While $R_0$ describes growth per *generation*, $\lambda_1$ describes growth per *time step*. The EVD provides the precise mapping between the shape of the net maternity function (which defines the coefficients of the characteristic polynomial) and the asymptotic growth rate $\lambda_1$ [cite: 12, 17, 18].
*   If $R_0 > 1$, then $\lambda_1 > 1$.
*   If $R_0 = 1$, then $\lambda_1 = 1$ (Stationary population).
*   If $R_0 < 1$, then $\lambda_1 < 1$.

## 6. Transient Dynamics and Subdominant Eigenvalues

While $\lambda_1$ determines the destination, the subdominant eigenvalues ($\lambda_2, \dots, \lambda_n$) determine the journey. This is where the EVD provides deep insights into the "population reproduction function" as a dynamic trajectory.

### 6.1 Demographic Waves and Oscillations
The subdominant eigenvalues of a Leslie matrix can be complex numbers. Since the matrix entries are real, complex eigenvalues occur in conjugate pairs: $\lambda_k = a + bi$ and $\bar{\lambda}_k = a - bi$.
In the spectral expansion, terms like $c_k \lambda_k^t \mathbf{v}_k$ introduce oscillatory behavior.
\[ \lambda_k^t = |\lambda_k|^t (\cos(\theta t) + i \sin(\theta t)) \]
These terms represent **demographic waves**—fluctuations in the birth rate and age structure that arise from irregularities in the initial population (e.g., a baby boom) [cite: 19, 20].

### 6.2 The Damping Ratio
The persistence of these waves is governed by the **damping ratio** ($\rho$), defined as:
\[ \rho = \frac{\lambda_1}{|\lambda_2|} \]
where $|\lambda_2|$ is the magnitude of the second-largest eigenvalue (the subdominant eigenvalue) [cite: 19, 21].
*   **High $\rho$:** The dominant mode $\lambda_1$ is much larger than the transient modes. Oscillations die out quickly, and the population converges rapidly to the stable age distribution.
*   **Low $\rho$ (close to 1):** The subdominant modes are nearly as strong as the dominant mode. Demographic waves persist for many generations before the stable structure is achieved [cite: 21].

This metric is critical for understanding population stability. A population with a "wide" net maternity function (reproduction spread over many ages) typically has a high damping ratio (fast convergence). A population with "peaked" reproduction (semelparity) often has a low damping ratio, leading to prone-to-oscillation dynamics [cite: 19, 22].

## 7. Connection to the Renewal Equation

The research results highlight a strong theoretical link between the discrete Leslie matrix and the continuous **renewal equation** [cite: 23, 24, 25, 26].

### 7.1 The Renewal Equation Formulation
In continuous time, the birth rate $B(t)$ follows the renewal equation:
\[ B(t) = \int_0^\infty B(t-a) \phi(a) \, da + G(t) \]
where $\phi(a)$ is the net maternity function (kernel) and $G(t)$ represents births from individuals already present at $t=0$ [cite: 25, 26].

### 7.2 EVD as a Solution Method
The asymptotic behavior of the renewal equation is determined by the roots of its characteristic equation:
\[ \int_0^\infty e^{-ra} \phi(a) \, da = 1 \]
This is the continuous analog of the discrete Euler-Lotka equation derived from the Leslie matrix [cite: 9, 26].
*   The **Malthusian parameter** $r$ corresponds to $\ln(\lambda_1)$ in the matrix model.
*   The discrete eigenvalues of the Leslie matrix approximate the roots of this integral equation.
*   The EVD of the Leslie matrix is effectively a numerical method for solving the renewal equation. It discretizes the continuous kernel $\phi(a)$ into the first row of the matrix. The "population reproduction function" (the trajectory of births $B(t)$) is thus asymptotically exponential, $B(t) \sim C e^{rt}$, exactly as predicted by the dominant eigenpair of the matrix [cite: 23, 27].

## 8. Conclusion

The eigenvalue decomposition of age-specific transition matrices is not merely a computational tool but the fundamental determinant of population dynamics. It acts as a filter that processes the complex history of a population.
1.  **$\lambda_1$ (Dominant Eigenvalue):** Determines the **asymptotic growth rate**. It is the unique real root of the Euler-Lotka equation derived from the net maternity function.
2.  **$\mathbf{v}_1$ (Dominant Eigenvector):** Determines the **asymptotic structure** (stable age distribution), which is invariant to initial conditions.
3.  **$\lambda_{i>1}$ (Subdominant Eigenvalues):** Determine the **transient dynamics**. Their magnitudes relative to $\lambda_1$ (the damping ratio) dictate how long the "memory" of initial disturbances lasts and the frequency of demographic oscillations.

In summary, the EVD translates the biological parameters of survival and fertility (encoded in the matrix) into the macroscopic behavior of the population, proving that the long-term reproduction function is asymptotically independent of the initial age structure and solely a function of the vital rates.

## References
*   **[cite: 28]** Abdi, H. (2007). The Eigen-Decomposition. *Encyclopedia of Measurement and Statistics*.
*   **[cite: 1]** Monagan, M. Leslie Matrices. *Simon Fraser University*.
*   **[cite: 2]** SNS Courseware. Eigenvalue Problem in Population Models: The Leslie Matrix.
*   **[cite: 8]** Wikipedia. Leslie matrix.
*   **[cite: 12]** Fundamental Theorem of Demography and Perron-Frobenius Theory.
*   **[cite: 3]** Sternberg, S. The Perron-Frobenius Theorem. *Harvard University*.
*   **[cite: 23]** Decay solution for the renewal equation with diffusion. *Math. Meth. Appl. Sci.*
*   **[cite: 25]** Franco, E. One Dimensional Reduction of a Renewal Equation. *University of Helsinki*.
*   **[cite: 19]** The Stable Population Model. *ResearchGate*.
*   **[cite: 4]** The Perron-Frobenius Theorem for Leslie matrices. *University of Sydney*.
*   **[cite: 21]** popdemo: Demographic modelling using projection matrices. *R Package Documentation*.
*   **[cite: 6]** Mahaffy, J. M. Age-Structured Models. *San Diego State University*.
*   **[cite: 9]** Wikipedia. Euler–Lotka equation.
*   **[cite: 26]** Boldin, B. Population growth in discrete time. *Naturalis*.

**Sources:**
1. [sfu.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUo4eb8QSt24Y0xUeNwp69hPp0gwyUbZu0PRw_U0Rv7HmXgB5YLKMMQ_xq5yYddoaVKWuXhssKieKeViyl3WYrIe5S_6mBZ_FWObIe9yzaPY2na9GiM1MzAikywytBGUT3cCz9_xC_1Ys=)
2. [snscourseware.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFk5MdOs4zVDAUGbae5JKzljwLEPs1JunIclMOGV3kYM1hTCICewdFrxh8mm2BbbpMAcSs1fwLwixUpU858eEAz-KeuSCWNEEXgY1rNXBC_jRRW_sqtVdRCgwpHNeM_KXHWBtFnMJxFQEdp)
3. [miami.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCrw-zk4TbdvEn2g52JWqLdpALQtTTEI4PTHwwdmcWY_-A7CYzpUdsyNQQud9jgNnxpmLYKz2VQvy50NgJ2V3k1OFNmXJtWKDznLGu9A88BriZzkzqvj0nZAjJbT3FPumobdyM4jgsVjKO2h5Jn1HbtNmzrtR5eRiN--3QyXetYlvw)
4. [usyd.edu.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWhdSvylB5VNFsZD1oQh0_8EaLYSQfw_hKvmHOlN8xx_O2VNb8q5dYE0AFlrED3N-OB47A0Csc4enT9RImXPo9P3l1K-g65aE1BJmkwsveQcU_3nSiWt8KaLXUt3DHqxs53049ay19WP0nYS8A8vySmxWZERw=)
5. [snscourseware.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEp0BYk-Mzj5GX7MxtEkkTgBwHUg6wZfsqmLIUZF0ymn2adyJlNT6R2qnVTtkmboAXp_iMg39YHEHfPcV6oLR7YNwqu-t-bwH0JGSvDNBvNDACECWZKIPkOGP5OR84kK8B6acA8vPgH_7cV)
6. [sdsu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjcb0eYPYUZa8_fy53sTLIDVc88xNwoS6DoE8XsrWe2qdkDcoBWKRZIXmDm6HHx7WRUh26SsauLwxuQIYX8AJk8-E2tPZzIz5P0DQTZbVZdcmdEghugkJUrJeMxIvET5LQhaaMrZYXq55b0tyTTaJoNuLaZuA=)
7. [ntnu.no](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR7Kdx2ZWmY2L_ld5RGyNvSpZ4HB3CMbzVRrC5UQSepUMTzDzm7lUDmYfTxlQUeXFcAPNhhq12yiEWBBqbd3Da57lQRkyJ6BhzyjvS3hVsDcYSng7Y3WDFWk0U4dgTzZIfym1yNKZ5bTu7lmhZOdAQo48=)
8. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZOi23qCJdFcYPcr1Fov86dToBme0h9GpUwL04x0ttaUhCQyrjTZZcR__hbrpcJAUfkBIOopdVocWtSvLaChVonQ75n66se9gkqYktiILpeklnKZrgabC0MyapCXJ93sha)
9. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHSnsy6ewN_mXVgO0fGFrc985kLhxsDNtS1nA9HmHpVMa9QOP0SgbX_xxXzkEuDC1ZCjqViWQUKMa0dABtGF1Lgp08X0_FXrF3MuEe380iekAJoLbLbWTN1uN6JEipsya5XchxG48UPkg2Jpu3YFmP)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiuWbqkkux64unHTzFLCDmrY8XeBLaFcCqJQ4kiLD1pA1etdEO5qDHuol5DINJAqPJdGgdQYS1q5rdL_OI6NfM0-mch31AgLMdl-b3umxEvnOqquEpYmmpwZZV5sjt3VlAGf4vb0pn0tf9Foy9r4PLTqTI_snxX0riJVzKUr51VhYydJmQVgcE0qRhFcnNUXm3Xdo7z_vd3-OOETNAvzML3MpxwbCj-5_2NUDTHj75pu53ZBie2gUez9hLDQ==)
11. [ens-paris-saclay.fr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5DUq5seO0muzPHjZLN7XZyMl2ufKcnI1wOZqDjAEVBLJpZPAjeJ3AuFsR_tpEuIOke7W2-VASWwiK9vZy9d4BVhJuFqJ7PXqxayh4c88DDTi02vEKjOP1LUo531tQHtE48A7mhCfdQKYZJMUWpXETqHQiGoCBma6iB1Ct9cMFU6Vd1QGW4VGFA3jRPcaM3NGWU5ksybyjwzL07Q==)
12. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7hOzzNDqmg10jxUUeBokL-Omj-DBtU4hslAtilsKbQAaMaMykhCOUqTepeaBMCrFGhlL3zI-bO4JnU0bRIuLDuQFZnlfd1copOFJFrNQUSj-xYztCenu7)
13. [harvard.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEz__IYK1iHPFPGFyjsfv6PBNIf7wAQcObqR5WlXsKPr9CAd5aKoW2BNmNEW4f9-BdE0pnP7OQZHJe5I_om1IST2BiiugMV__lgyI0O1kTJt65w-PcHqidlgQoaTAvEr1ucSYm2vJHLqTegkLcIGrIQYwYbkQMLLSvHpydIBQHaPtPZcg==)
14. [utetuniversita.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQxVl6rZ2ctndKy64XwTADpAfim2I5HDFtO6veQAHpOI_X4lBwuqucoFh5bLE1gWOzp-n-JiJyPIGX6mp3iatGBc1TbMTVV8aQ11ghpAwNnc-jFu42mfeEz2d2DmTv1DoWOrJOCW6qL0T1mmx3atYoXislnkStPWTrHZkWVof4UqBfh-O858x8Peu7FyzjnS5EN9GckCJuQdfyzqFgbLUhSHbIw9nVNYHIlCly9DHqJE8FIeHe)
15. [libretexts.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpN494MKQ9jKAXgypUJ3dU4Cjv3oHcG4OkOwFOJX5gvHndplQ3Ii4b2RSxOZ1xPVa7uHRzue73DH3QKWJK1AVpUOvvZpF1Je7tvLr4vErNJEmSFhDkR2aBU4k_1KX2XjZ53GfHUMdEhJt_1ag1VngRTmE6cx-xGRQMixXzQbufqR9s4Aj61rJwh2ZcAx26Gqt95z0u2j-5MPqD1BpCS5-ddNQaQQQML4CjGAXCNS2CI7mHiPFQzcKwc8M-_9kmh04ogdrXsBqg0B1fP1iQKQHR3tUAasagrAxE245D1Dx2SuU0HdcjWzWWcLaoZUbdeApCANyvCg==)
16. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy8DdHdRhL4iJeYmaQ0wAgeerY6rEQZF0AKgwMzIeKClCGGP08kO7v-U3_ZaRuavP2FezserZs5M1Te6D6mJ5znMmHeZtI8ybpCSdnXrXE1wcEBKuqBmwh9WF3gc_DtKCO)
17. [pnas.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPTg-SWysU5FENBMwxCVd9wZRS0fUEwitv9x6OvDm6vz8PFIBcDSt-u-AAWQz9Lw1IuRR-BlzZ0MYvX7F-u8dyaRTjtKjdLRnoAhzE8Bwt5PQi9R5R3-ADsEmCNdDpgceSO5fnIa5-BJ5v_g==)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH84krzbDFq4lgmhmBHPMwa8T6NsnRqVXoHaoTTXkn70yPuEYY2NLVJ4bvg3-Yru3-ivaiyx8Qw67kFQGki02nHYKC7bj71peLCddELrnrIQzbV-FodfNPqaHEhWhpeREbY5ITXmZ9RhMJYPTHQBdubDFr2PT34AGBQ34T6NkIH-dDqVPfeQCyC6D5xldCEDgC6)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoOmPffsfsdDNfsMTC-AE9iz5buNfN79e6ouWVNryscHLI13GuCjiqStH_Ncu7YlwuTVyYosu7U__ssHdxxNO1q8yq94QsP0ZXyZWmju1YwOl3H48UyHhP19d4800xOjpr9cNdm9uHMCjdK3EqJXmN4NvTBAxOGRhshZKc_Rn4arpW0UY=)
20. [ethernet.edu.et](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0jc6xUMXfadAVtJRcLP5KCn34MiKhQw80k5FtIfWpNv2GFtftQz60CBXc1oUez2vmmk5TzeUjlgktaydVnqO8hkcNb7PexcrdgmDAIh9SB38oWTzALgBcRMI8-8TSFxedO_6HufMKqO-gEfLQ3ITO-jnOCQm95cvgLMunR7FevQ==)
21. [rdrr.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKEjUtOrLg3xOSSiJn7p9oAjJw9ZMktfXcsSBUXa_FCkcajANm2yJRsNSj-VtBKqXevlbYcw3t_m_lV79zOAU-r4j687zztBZKCLqPSN4CxOWLj7pVkrKqXW0sbGI3)
22. [siam.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHa0zvFFfBSNDMXdhNiSPUQQzhfPvGP7cRpW3VMdXICuYBG9z3tPdaD8o1Fj-M9_5wo9CVgUA4vOgNlnM9OSunFKNFuOqEo5jTSIhqFVVCSHs9HfUI6qnjcwu3RooeADnM=)
23. [ec-lyon.fr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnwq5EZgDrSQ6yEubLTHhTnPKX5hq7LdNY9Ls-CqZQkDeSJTQP6UcmmQzvhMbti_YzlolKdIcAVQqfjfoxnJNjVGrVKlJDFLXT85PU4xGqvfHkb_RfWNIrl8d4w_cZoeDYgOYHYzQtIhhojjIH)
24. [uu.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxm7oXxDdmMpprJvCQcjRQPKMYM8MzktwYays40o2VIPkGYFplYJrK-YTzYjqLVqt3riH9kxtaUuEl219sU9mLHcoWXrtqTQVFT9cOhd_8PkbiCb_HjuFWyew_6MEokI-sAqDassomWstommyoDnbxlX_ryrkz2S4YaPckcZD0JU3dYwFbwhaOlRML)
25. [helsinki.fi](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErdTSS2PkMWOIbl7JAdWkmzgZWw8HNjOcJcLncOs18bwnIqrmpwuhi7rPewmvJkrpDXEH9ABAAZM27Aw2Aan7H-NygQ6-gcQLlKcnTGhD8Zbb4AOOkvIx8--wTH8liRCwCrPdgsDCaaHzXdHGNtQKYEvlQhI3pSHh99cBrqxvv93HICD5GZP_g)
26. [naturalis.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtfxgDW0lBIlvHdbtY8nRUAMSFipeCDeaCKAowXS_P6FYOX_2AeI8PWW9xaXiFml978FqcGCOJwR-501Mf0Z8jjsqvvDyMjyDwdBwYJc_lTG6Js-QPiukUVEkwfTX71h8tbbMyBGNGxpu7Blf6ZGR8A6nadNgyPrisf0eLwINV4dzAzgmCcEGYlrc0FVS_3fBdbye5)
27. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGx5hF4UaiYbvhjaw_LVIGrqoDK2rZmCXLJH9erDc0AmCxxqJ3MBmhwa58rFMLaO0NCfvLzDczzrP_cOXgZb5uF_gcPZzRCz2_eX6bMUdXFsNgNR2TWSQ==)
28. [utdallas.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2_cNsKfaFmY6VfEJCnarP45DdwyKzKADiveoBSRbU0mr-VhfBRhDHWTkfl7nbxqC209qVyJzQK9XWSnFq2QUmJ1qxOAIZFCRAH-lJlxruCXRk-OWUw0hwy_meAAgepu3L1eh-18XvJTt25k5b)


## Annotations
Annotation(end_index=3745, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUo4eb8QSt24Y0xUeNwp69hPp0gwyUbZu0PRw_U0Rv7HmXgB5YLKMMQ_xq5yYddoaVKWuXhssKieKeViyl3WYrIe5S_6mBZ_FWObIe9yzaPY2na9GiM1MzAikywytBGUT3cCz9_xC_1Ys=', start_index=3733)
Annotation(end_index=3745, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFk5MdOs4zVDAUGbae5JKzljwLEPs1JunIclMOGV3kYM1hTCICewdFrxh8mm2BbbpMAcSs1fwLwixUpU858eEAz-KeuSCWNEEXgY1rNXBC_jRRW_sqtVdRCgwpHNeM_KXHWBtFnMJxFQEdp', start_index=3733)
Annotation(end_index=3854, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCrw-zk4TbdvEn2g52JWqLdpALQtTTEI4PTHwwdmcWY_-A7CYzpUdsyNQQud9jgNnxpmLYKz2VQvy50NgJ2V3k1OFNmXJtWKDznLGu9A88BriZzkzqvj0nZAjJbT3FPumobdyM4jgsVjKO2h5Jn1HbtNmzrtR5eRiN--3QyXetYlvw', start_index=3842)
Annotation(end_index=3854, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWhdSvylB5VNFsZD1oQh0_8EaLYSQfw_hKvmHOlN8xx_O2VNb8q5dYE0AFlrED3N-OB47A0Csc4enT9RImXPo9P3l1K-g65aE1BJmkwsveQcU_3nSiWt8KaLXUt3DHqxs53049ay19WP0nYS8A8vySmxWZERw=', start_index=3842)
Annotation(end_index=4132, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjcb0eYPYUZa8_fy53sTLIDVc88xNwoS6DoE8XsrWe2qdkDcoBWKRZIXmDm6HHx7WRUh26SsauLwxuQIYX8AJk8-E2tPZzIz5P0DQTZbVZdcmdEghugkJUrJeMxIvET5LQhaaMrZYXq55b0tyTTaJoNuLaZuA=', start_index=4120)
Annotation(end_index=4132, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEp0BYk-Mzj5GX7MxtEkkTgBwHUg6wZfsqmLIUZF0ymn2adyJlNT6R2qnVTtkmboAXp_iMg39YHEHfPcV6oLR7YNwqu-t-bwH0JGSvDNBvNDACECWZKIPkOGP5OR84kK8B6acA8vPgH_7cV', start_index=4120)
Annotation(end_index=4352, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEp0BYk-Mzj5GX7MxtEkkTgBwHUg6wZfsqmLIUZF0ymn2adyJlNT6R2qnVTtkmboAXp_iMg39YHEHfPcV6oLR7YNwqu-t-bwH0JGSvDNBvNDACECWZKIPkOGP5OR84kK8B6acA8vPgH_7cV', start_index=4340)
Annotation(end_index=4352, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCrw-zk4TbdvEn2g52JWqLdpALQtTTEI4PTHwwdmcWY_-A7CYzpUdsyNQQud9jgNnxpmLYKz2VQvy50NgJ2V3k1OFNmXJtWKDznLGu9A88BriZzkzqvj0nZAjJbT3FPumobdyM4jgsVjKO2h5Jn1HbtNmzrtR5eRiN--3QyXetYlvw', start_index=4340)
Annotation(end_index=4509, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEp0BYk-Mzj5GX7MxtEkkTgBwHUg6wZfsqmLIUZF0ymn2adyJlNT6R2qnVTtkmboAXp_iMg39YHEHfPcV6oLR7YNwqu-t-bwH0JGSvDNBvNDACECWZKIPkOGP5OR84kK8B6acA8vPgH_7cV', start_index=4497)
Annotation(end_index=4509, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWhdSvylB5VNFsZD1oQh0_8EaLYSQfw_hKvmHOlN8xx_O2VNb8q5dYE0AFlrED3N-OB47A0Csc4enT9RImXPo9P3l1K-g65aE1BJmkwsveQcU_3nSiWt8KaLXUt3DHqxs53049ay19WP0nYS8A8vySmxWZERw=', start_index=4497)
Annotation(end_index=4788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjcb0eYPYUZa8_fy53sTLIDVc88xNwoS6DoE8XsrWe2qdkDcoBWKRZIXmDm6HHx7WRUh26SsauLwxuQIYX8AJk8-E2tPZzIz5P0DQTZbVZdcmdEghugkJUrJeMxIvET5LQhaaMrZYXq55b0tyTTaJoNuLaZuA=', start_index=4776)
Annotation(end_index=4788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR7Kdx2ZWmY2L_ld5RGyNvSpZ4HB3CMbzVRrC5UQSepUMTzDzm7lUDmYfTxlQUeXFcAPNhhq12yiEWBBqbd3Da57lQRkyJ6BhzyjvS3hVsDcYSng7Y3WDFWk0U4dgTzZIfym1yNKZ5bTu7lmhZOdAQo48=', start_index=4776)
Annotation(end_index=5283, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUo4eb8QSt24Y0xUeNwp69hPp0gwyUbZu0PRw_U0Rv7HmXgB5YLKMMQ_xq5yYddoaVKWuXhssKieKeViyl3WYrIe5S_6mBZ_FWObIe9yzaPY2na9GiM1MzAikywytBGUT3cCz9_xC_1Ys=', start_index=5274)
Annotation(end_index=6265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHSnsy6ewN_mXVgO0fGFrc985kLhxsDNtS1nA9HmHpVMa9QOP0SgbX_xxXzkEuDC1ZCjqViWQUKMa0dABtGF1Lgp08X0_FXrF3MuEe380iekAJoLbLbWTN1uN6JEipsya5XchxG48UPkg2Jpu3YFmP', start_index=6253)
Annotation(end_index=6265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZOi23qCJdFcYPcr1Fov86dToBme0h9GpUwL04x0ttaUhCQyrjTZZcR__hbrpcJAUfkBIOopdVocWtSvLaChVonQ75n66se9gkqYktiILpeklnKZrgabC0MyapCXJ93sha', start_index=6253)
Annotation(end_index=7006, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjcb0eYPYUZa8_fy53sTLIDVc88xNwoS6DoE8XsrWe2qdkDcoBWKRZIXmDm6HHx7WRUh26SsauLwxuQIYX8AJk8-E2tPZzIz5P0DQTZbVZdcmdEghugkJUrJeMxIvET5LQhaaMrZYXq55b0tyTTaJoNuLaZuA=', start_index=6994)
Annotation(end_index=7006, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR7Kdx2ZWmY2L_ld5RGyNvSpZ4HB3CMbzVRrC5UQSepUMTzDzm7lUDmYfTxlQUeXFcAPNhhq12yiEWBBqbd3Da57lQRkyJ6BhzyjvS3hVsDcYSng7Y3WDFWk0U4dgTzZIfym1yNKZ5bTu7lmhZOdAQo48=', start_index=6994)
Annotation(end_index=7379, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjcb0eYPYUZa8_fy53sTLIDVc88xNwoS6DoE8XsrWe2qdkDcoBWKRZIXmDm6HHx7WRUh26SsauLwxuQIYX8AJk8-E2tPZzIz5P0DQTZbVZdcmdEghugkJUrJeMxIvET5LQhaaMrZYXq55b0tyTTaJoNuLaZuA=', start_index=7370)
Annotation(end_index=8199, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCrw-zk4TbdvEn2g52JWqLdpALQtTTEI4PTHwwdmcWY_-A7CYzpUdsyNQQud9jgNnxpmLYKz2VQvy50NgJ2V3k1OFNmXJtWKDznLGu9A88BriZzkzqvj0nZAjJbT3FPumobdyM4jgsVjKO2h5Jn1HbtNmzrtR5eRiN--3QyXetYlvw', start_index=8186)
Annotation(end_index=8199, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiuWbqkkux64unHTzFLCDmrY8XeBLaFcCqJQ4kiLD1pA1etdEO5qDHuol5DINJAqPJdGgdQYS1q5rdL_OI6NfM0-mch31AgLMdl-b3umxEvnOqquEpYmmpwZZV5sjt3VlAGf4vb0pn0tf9Foy9r4PLTqTI_snxX0riJVzKUr51VhYydJmQVgcE0qRhFcnNUXm3Xdo7z_vd3-OOETNAvzML3MpxwbCj-5_2NUDTHj75pu53ZBie2gUez9hLDQ==', start_index=8186)
Annotation(end_index=8469, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5DUq5seO0muzPHjZLN7XZyMl2ufKcnI1wOZqDjAEVBLJpZPAjeJ3AuFsR_tpEuIOke7W2-VASWwiK9vZy9d4BVhJuFqJ7PXqxayh4c88DDTi02vEKjOP1LUo531tQHtE48A7mhCfdQKYZJMUWpXETqHQiGoCBma6iB1Ct9cMFU6Vd1QGW4VGFA3jRPcaM3NGWU5ksybyjwzL07Q==', start_index=8456)
Annotation(end_index=8469, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCrw-zk4TbdvEn2g52JWqLdpALQtTTEI4PTHwwdmcWY_-A7CYzpUdsyNQQud9jgNnxpmLYKz2VQvy50NgJ2V3k1OFNmXJtWKDznLGu9A88BriZzkzqvj0nZAjJbT3FPumobdyM4jgsVjKO2h5Jn1HbtNmzrtR5eRiN--3QyXetYlvw', start_index=8456)
Annotation(end_index=8636, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEz__IYK1iHPFPGFyjsfv6PBNIf7wAQcObqR5WlXsKPr9CAd5aKoW2BNmNEW4f9-BdE0pnP7OQZHJe5I_om1IST2BiiugMV__lgyI0O1kTJt65w-PcHqidlgQoaTAvEr1ucSYm2vJHLqTegkLcIGrIQYwYbkQMLLSvHpydIBQHaPtPZcg==', start_index=8616)
Annotation(end_index=8636, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7hOzzNDqmg10jxUUeBokL-Omj-DBtU4hslAtilsKbQAaMaMykhCOUqTepeaBMCrFGhlL3zI-bO4JnU0bRIuLDuQFZnlfd1copOFJFrNQUSj-xYztCenu7', start_index=8616)
Annotation(end_index=8636, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCrw-zk4TbdvEn2g52JWqLdpALQtTTEI4PTHwwdmcWY_-A7CYzpUdsyNQQud9jgNnxpmLYKz2VQvy50NgJ2V3k1OFNmXJtWKDznLGu9A88BriZzkzqvj0nZAjJbT3FPumobdyM4jgsVjKO2h5Jn1HbtNmzrtR5eRiN--3QyXetYlvw', start_index=8616)
Annotation(end_index=8636, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWhdSvylB5VNFsZD1oQh0_8EaLYSQfw_hKvmHOlN8xx_O2VNb8q5dYE0AFlrED3N-OB47A0Csc4enT9RImXPo9P3l1K-g65aE1BJmkwsveQcU_3nSiWt8KaLXUt3DHqxs53049ay19WP0nYS8A8vySmxWZERw=', start_index=8616)
Annotation(end_index=9776, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUo4eb8QSt24Y0xUeNwp69hPp0gwyUbZu0PRw_U0Rv7HmXgB5YLKMMQ_xq5yYddoaVKWuXhssKieKeViyl3WYrIe5S_6mBZ_FWObIe9yzaPY2na9GiM1MzAikywytBGUT3cCz9_xC_1Ys=', start_index=9760)
Annotation(end_index=9776, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjcb0eYPYUZa8_fy53sTLIDVc88xNwoS6DoE8XsrWe2qdkDcoBWKRZIXmDm6HHx7WRUh26SsauLwxuQIYX8AJk8-E2tPZzIz5P0DQTZbVZdcmdEghugkJUrJeMxIvET5LQhaaMrZYXq55b0tyTTaJoNuLaZuA=', start_index=9760)
Annotation(end_index=9776, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQxVl6rZ2ctndKy64XwTADpAfim2I5HDFtO6veQAHpOI_X4lBwuqucoFh5bLE1gWOzp-n-JiJyPIGX6mp3iatGBc1TbMTVV8aQ11ghpAwNnc-jFu42mfeEz2d2DmTv1DoWOrJOCW6qL0T1mmx3atYoXislnkStPWTrHZkWVof4UqBfh-O858x8Peu7FyzjnS5EN9GckCJuQdfyzqFgbLUhSHbIw9nVNYHIlCly9DHqJE8FIeHe', start_index=9760)
Annotation(end_index=10110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUo4eb8QSt24Y0xUeNwp69hPp0gwyUbZu0PRw_U0Rv7HmXgB5YLKMMQ_xq5yYddoaVKWuXhssKieKeViyl3WYrIe5S_6mBZ_FWObIe9yzaPY2na9GiM1MzAikywytBGUT3cCz9_xC_1Ys=', start_index=10095)
Annotation(end_index=10110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFk5MdOs4zVDAUGbae5JKzljwLEPs1JunIclMOGV3kYM1hTCICewdFrxh8mm2BbbpMAcSs1fwLwixUpU858eEAz-KeuSCWNEEXgY1rNXBC_jRRW_sqtVdRCgwpHNeM_KXHWBtFnMJxFQEdp', start_index=10095)
Annotation(end_index=10110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR7Kdx2ZWmY2L_ld5RGyNvSpZ4HB3CMbzVRrC5UQSepUMTzDzm7lUDmYfTxlQUeXFcAPNhhq12yiEWBBqbd3Da57lQRkyJ6BhzyjvS3hVsDcYSng7Y3WDFWk0U4dgTzZIfym1yNKZ5bTu7lmhZOdAQo48=', start_index=10095)
Annotation(end_index=10489, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFk5MdOs4zVDAUGbae5JKzljwLEPs1JunIclMOGV3kYM1hTCICewdFrxh8mm2BbbpMAcSs1fwLwixUpU858eEAz-KeuSCWNEEXgY1rNXBC_jRRW_sqtVdRCgwpHNeM_KXHWBtFnMJxFQEdp', start_index=10476)
Annotation(end_index=10489, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpN494MKQ9jKAXgypUJ3dU4Cjv3oHcG4OkOwFOJX5gvHndplQ3Ii4b2RSxOZ1xPVa7uHRzue73DH3QKWJK1AVpUOvvZpF1Je7tvLr4vErNJEmSFhDkR2aBU4k_1KX2XjZ53GfHUMdEhJt_1ag1VngRTmE6cx-xGRQMixXzQbufqR9s4Aj61rJwh2ZcAx26Gqt95z0u2j-5MPqD1BpCS5-ddNQaQQQML4CjGAXCNS2CI7mHiPFQzcKwc8M-_9kmh04ogdrXsBqg0B1fP1iQKQHR3tUAasagrAxE245D1Dx2SuU0HdcjWzWWcLaoZUbdeApCANyvCg==', start_index=10476)
Annotation(end_index=10621, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy8DdHdRhL4iJeYmaQ0wAgeerY6rEQZF0AKgwMzIeKClCGGP08kO7v-U3_ZaRuavP2FezserZs5M1Te6D6mJ5znMmHeZtI8ybpCSdnXrXE1wcEBKuqBmwh9WF3gc_DtKCO', start_index=10608)
Annotation(end_index=10621, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFk5MdOs4zVDAUGbae5JKzljwLEPs1JunIclMOGV3kYM1hTCICewdFrxh8mm2BbbpMAcSs1fwLwixUpU858eEAz-KeuSCWNEEXgY1rNXBC_jRRW_sqtVdRCgwpHNeM_KXHWBtFnMJxFQEdp', start_index=10608)
Annotation(end_index=10840, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWhdSvylB5VNFsZD1oQh0_8EaLYSQfw_hKvmHOlN8xx_O2VNb8q5dYE0AFlrED3N-OB47A0Csc4enT9RImXPo9P3l1K-g65aE1BJmkwsveQcU_3nSiWt8KaLXUt3DHqxs53049ay19WP0nYS8A8vySmxWZERw=', start_index=10831)
Annotation(end_index=11611, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7hOzzNDqmg10jxUUeBokL-Omj-DBtU4hslAtilsKbQAaMaMykhCOUqTepeaBMCrFGhlL3zI-bO4JnU0bRIuLDuQFZnlfd1copOFJFrNQUSj-xYztCenu7', start_index=11593)
Annotation(end_index=11611, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPTg-SWysU5FENBMwxCVd9wZRS0fUEwitv9x6OvDm6vz8PFIBcDSt-u-AAWQz9Lw1IuRR-BlzZ0MYvX7F-u8dyaRTjtKjdLRnoAhzE8Bwt5PQi9R5R3-ADsEmCNdDpgceSO5fnIa5-BJ5v_g==', start_index=11593)
Annotation(end_index=11611, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH84krzbDFq4lgmhmBHPMwa8T6NsnRqVXoHaoTTXkn70yPuEYY2NLVJ4bvg3-Yru3-ivaiyx8Qw67kFQGki02nHYKC7bj71peLCddELrnrIQzbV-FodfNPqaHEhWhpeREbY5ITXmZ9RhMJYPTHQBdubDFr2PT34AGBQ34T6NkIH-dDqVPfeQCyC6D5xldCEDgC6', start_index=11593)
Annotation(end_index=12661, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0jc6xUMXfadAVtJRcLP5KCn34MiKhQw80k5FtIfWpNv2GFtftQz60CBXc1oUez2vmmk5TzeUjlgktaydVnqO8hkcNb7PexcrdgmDAIh9SB38oWTzALgBcRMI8-8TSFxedO_6HufMKqO-gEfLQ3ITO-jnOCQm95cvgLMunR7FevQ==', start_index=12647)
Annotation(end_index=12661, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoOmPffsfsdDNfsMTC-AE9iz5buNfN79e6ouWVNryscHLI13GuCjiqStH_Ncu7YlwuTVyYosu7U__ssHdxxNO1q8yq94QsP0ZXyZWmju1YwOl3H48UyHhP19d4800xOjpr9cNdm9uHMCjdK3EqJXmN4NvTBAxOGRhshZKc_Rn4arpW0UY=', start_index=12647)
Annotation(end_index=12936, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKEjUtOrLg3xOSSiJn7p9oAjJw9ZMktfXcsSBUXa_FCkcajANm2yJRsNSj-VtBKqXevlbYcw3t_m_lV79zOAU-r4j687zztBZKCLqPSN4CxOWLj7pVkrKqXW0sbGI3', start_index=12922)
Annotation(end_index=12936, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoOmPffsfsdDNfsMTC-AE9iz5buNfN79e6ouWVNryscHLI13GuCjiqStH_Ncu7YlwuTVyYosu7U__ssHdxxNO1q8yq94QsP0ZXyZWmju1YwOl3H48UyHhP19d4800xOjpr9cNdm9uHMCjdK3EqJXmN4NvTBAxOGRhshZKc_Rn4arpW0UY=', start_index=12922)
Annotation(end_index=13324, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKEjUtOrLg3xOSSiJn7p9oAjJw9ZMktfXcsSBUXa_FCkcajANm2yJRsNSj-VtBKqXevlbYcw3t_m_lV79zOAU-r4j687zztBZKCLqPSN4CxOWLj7pVkrKqXW0sbGI3', start_index=13314)
Annotation(end_index=13673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoOmPffsfsdDNfsMTC-AE9iz5buNfN79e6ouWVNryscHLI13GuCjiqStH_Ncu7YlwuTVyYosu7U__ssHdxxNO1q8yq94QsP0ZXyZWmju1YwOl3H48UyHhP19d4800xOjpr9cNdm9uHMCjdK3EqJXmN4NvTBAxOGRhshZKc_Rn4arpW0UY=', start_index=13659)
Annotation(end_index=13673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHa0zvFFfBSNDMXdhNiSPUQQzhfPvGP7cRpW3VMdXICuYBG9z3tPdaD8o1Fj-M9_5wo9CVgUA4vOgNlnM9OSunFKNFuOqEo5jTSIhqFVVCSHs9HfUI6qnjcwu3RooeADnM=', start_index=13659)
Annotation(end_index=13872, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnwq5EZgDrSQ6yEubLTHhTnPKX5hq7LdNY9Ls-CqZQkDeSJTQP6UcmmQzvhMbti_YzlolKdIcAVQqfjfoxnJNjVGrVKlJDFLXT85PU4xGqvfHkb_RfWNIrl8d4w_cZoeDYgOYHYzQtIhhojjIH', start_index=13850)
Annotation(end_index=13872, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErdTSS2PkMWOIbl7JAdWkmzgZWw8HNjOcJcLncOs18bwnIqrmpwuhi7rPewmvJkrpDXEH9ABAAZM27Aw2Aan7H-NygQ6-gcQLlKcnTGhD8Zbb4AOOkvIx8--wTH8liRCwCrPdgsDCaaHzXdHGNtQKYEvlQhI3pSHh99cBrqxvv93HICD5GZP_g', start_index=13850)
Annotation(end_index=13872, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtfxgDW0lBIlvHdbtY8nRUAMSFipeCDeaCKAowXS_P6FYOX_2AeI8PWW9xaXiFml978FqcGCOJwR-501Mf0Z8jjsqvvDyMjyDwdBwYJc_lTG6Js-QPiukUVEkwfTX71h8tbbMyBGNGxpu7Blf6ZGR8A6nadNgyPrisf0eLwINV4dzAzgmCcEGYlrc0FVS_3fBdbye5', start_index=13850)
Annotation(end_index=13872, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxm7oXxDdmMpprJvCQcjRQPKMYM8MzktwYays40o2VIPkGYFplYJrK-YTzYjqLVqt3riH9kxtaUuEl219sU9mLHcoWXrtqTQVFT9cOhd_8PkbiCb_HjuFWyew_6MEokI-sAqDassomWstommyoDnbxlX_ryrkz2S4YaPckcZD0JU3dYwFbwhaOlRML', start_index=13850)
Annotation(end_index=14183, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErdTSS2PkMWOIbl7JAdWkmzgZWw8HNjOcJcLncOs18bwnIqrmpwuhi7rPewmvJkrpDXEH9ABAAZM27Aw2Aan7H-NygQ6-gcQLlKcnTGhD8Zbb4AOOkvIx8--wTH8liRCwCrPdgsDCaaHzXdHGNtQKYEvlQhI3pSHh99cBrqxvv93HICD5GZP_g', start_index=14169)
Annotation(end_index=14183, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtfxgDW0lBIlvHdbtY8nRUAMSFipeCDeaCKAowXS_P6FYOX_2AeI8PWW9xaXiFml978FqcGCOJwR-501Mf0Z8jjsqvvDyMjyDwdBwYJc_lTG6Js-QPiukUVEkwfTX71h8tbbMyBGNGxpu7Blf6ZGR8A6nadNgyPrisf0eLwINV4dzAzgmCcEGYlrc0FVS_3fBdbye5', start_index=14169)
Annotation(end_index=14483, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHSnsy6ewN_mXVgO0fGFrc985kLhxsDNtS1nA9HmHpVMa9QOP0SgbX_xxXzkEuDC1ZCjqViWQUKMa0dABtGF1Lgp08X0_FXrF3MuEe380iekAJoLbLbWTN1uN6JEipsya5XchxG48UPkg2Jpu3YFmP', start_index=14470)
Annotation(end_index=14483, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtfxgDW0lBIlvHdbtY8nRUAMSFipeCDeaCKAowXS_P6FYOX_2AeI8PWW9xaXiFml978FqcGCOJwR-501Mf0Z8jjsqvvDyMjyDwdBwYJc_lTG6Js-QPiukUVEkwfTX71h8tbbMyBGNGxpu7Blf6ZGR8A6nadNgyPrisf0eLwINV4dzAzgmCcEGYlrc0FVS_3fBdbye5', start_index=14470)
Annotation(end_index=15062, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnwq5EZgDrSQ6yEubLTHhTnPKX5hq7LdNY9Ls-CqZQkDeSJTQP6UcmmQzvhMbti_YzlolKdIcAVQqfjfoxnJNjVGrVKlJDFLXT85PU4xGqvfHkb_RfWNIrl8d4w_cZoeDYgOYHYzQtIhhojjIH', start_index=15048)
Annotation(end_index=15062, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGx5hF4UaiYbvhjaw_LVIGrqoDK2rZmCXLJH9erDc0AmCxxqJ3MBmhwa58rFMLaO0NCfvLzDczzrP_cOXgZb5uF_gcPZzRCz2_eX6bMUdXFsNgNR2TWSQ==', start_index=15048)
Annotation(end_index=16244, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2_cNsKfaFmY6VfEJCnarP45DdwyKzKADiveoBSRbU0mr-VhfBRhDHWTkfl7nbxqC209qVyJzQK9XWSnFq2QUmJ1qxOAIZFCRAH-lJlxruCXRk-OWUw0hwy_meAAgepu3L1eh-18XvJTt25k5b', start_index=16234)
Annotation(end_index=16350, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUo4eb8QSt24Y0xUeNwp69hPp0gwyUbZu0PRw_U0Rv7HmXgB5YLKMMQ_xq5yYddoaVKWuXhssKieKeViyl3WYrIe5S_6mBZ_FWObIe9yzaPY2na9GiM1MzAikywytBGUT3cCz9_xC_1Ys=', start_index=16341)
Annotation(end_index=16424, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFk5MdOs4zVDAUGbae5JKzljwLEPs1JunIclMOGV3kYM1hTCICewdFrxh8mm2BbbpMAcSs1fwLwixUpU858eEAz-KeuSCWNEEXgY1rNXBC_jRRW_sqtVdRCgwpHNeM_KXHWBtFnMJxFQEdp', start_index=16415)
Annotation(end_index=16518, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZOi23qCJdFcYPcr1Fov86dToBme0h9GpUwL04x0ttaUhCQyrjTZZcR__hbrpcJAUfkBIOopdVocWtSvLaChVonQ75n66se9gkqYktiILpeklnKZrgabC0MyapCXJ93sha', start_index=16509)
Annotation(end_index=16563, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7hOzzNDqmg10jxUUeBokL-Omj-DBtU4hslAtilsKbQAaMaMykhCOUqTepeaBMCrFGhlL3zI-bO4JnU0bRIuLDuQFZnlfd1copOFJFrNQUSj-xYztCenu7', start_index=16553)
Annotation(end_index=16644, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCrw-zk4TbdvEn2g52JWqLdpALQtTTEI4PTHwwdmcWY_-A7CYzpUdsyNQQud9jgNnxpmLYKz2VQvy50NgJ2V3k1OFNmXJtWKDznLGu9A88BriZzkzqvj0nZAjJbT3FPumobdyM4jgsVjKO2h5Jn1HbtNmzrtR5eRiN--3QyXetYlvw', start_index=16635)
Annotation(end_index=16729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnwq5EZgDrSQ6yEubLTHhTnPKX5hq7LdNY9Ls-CqZQkDeSJTQP6UcmmQzvhMbti_YzlolKdIcAVQqfjfoxnJNjVGrVKlJDFLXT85PU4xGqvfHkb_RfWNIrl8d4w_cZoeDYgOYHYzQtIhhojjIH', start_index=16719)
Annotation(end_index=16829, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErdTSS2PkMWOIbl7JAdWkmzgZWw8HNjOcJcLncOs18bwnIqrmpwuhi7rPewmvJkrpDXEH9ABAAZM27Aw2Aan7H-NygQ6-gcQLlKcnTGhD8Zbb4AOOkvIx8--wTH8liRCwCrPdgsDCaaHzXdHGNtQKYEvlQhI3pSHh99cBrqxvv93HICD5GZP_g', start_index=16819)
Annotation(end_index=16934, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoOmPffsfsdDNfsMTC-AE9iz5buNfN79e6ouWVNryscHLI13GuCjiqStH_Ncu7YlwuTVyYosu7U__ssHdxxNO1q8yq94QsP0ZXyZWmju1YwOl3H48UyHhP19d4800xOjpr9cNdm9uHMCjdK3EqJXmN4NvTBAxOGRhshZKc_Rn4arpW0UY=', start_index=16924)
Annotation(end_index=16997, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWhdSvylB5VNFsZD1oQh0_8EaLYSQfw_hKvmHOlN8xx_O2VNb8q5dYE0AFlrED3N-OB47A0Csc4enT9RImXPo9P3l1K-g65aE1BJmkwsveQcU_3nSiWt8KaLXUt3DHqxs53049ay19WP0nYS8A8vySmxWZERw=', start_index=16988)
Annotation(end_index=17090, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKEjUtOrLg3xOSSiJn7p9oAjJw9ZMktfXcsSBUXa_FCkcajANm2yJRsNSj-VtBKqXevlbYcw3t_m_lV79zOAU-r4j687zztBZKCLqPSN4CxOWLj7pVkrKqXW0sbGI3', start_index=17080)
Annotation(end_index=17193, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjcb0eYPYUZa8_fy53sTLIDVc88xNwoS6DoE8XsrWe2qdkDcoBWKRZIXmDm6HHx7WRUh26SsauLwxuQIYX8AJk8-E2tPZzIz5P0DQTZbVZdcmdEghugkJUrJeMxIvET5LQhaaMrZYXq55b0tyTTaJoNuLaZuA=', start_index=17184)
Annotation(end_index=17279, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHSnsy6ewN_mXVgO0fGFrc985kLhxsDNtS1nA9HmHpVMa9QOP0SgbX_xxXzkEuDC1ZCjqViWQUKMa0dABtGF1Lgp08X0_FXrF3MuEe380iekAJoLbLbWTN1uN6JEipsya5XchxG48UPkg2Jpu3YFmP', start_index=17270)
Annotation(end_index=17333, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtfxgDW0lBIlvHdbtY8nRUAMSFipeCDeaCKAowXS_P6FYOX_2AeI8PWW9xaXiFml978FqcGCOJwR-501Mf0Z8jjsqvvDyMjyDwdBwYJc_lTG6Js-QPiukUVEkwfTX71h8tbbMyBGNGxpu7Blf6ZGR8A6nadNgyPrisf0eLwINV4dzAzgmCcEGYlrc0FVS_3fBdbye5', start_index=17323)

## Sources
