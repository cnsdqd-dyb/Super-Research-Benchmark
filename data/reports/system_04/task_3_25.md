# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** bb518f73 | **Time:** 388.52s | **Cost:** $1.68560
--------------------------------------------------------------------------------

# How the Characteristic Polynomial of Intergenerational Transfer Matrices Determines the Lyapunov Stability of Welfare Systems

## Key Points
*   **Mathematical Foundation:** The characteristic polynomial of the transition matrix (Jacobian) in Overlapping Generations (OLG) models yields eigenvalues that dictate the local dynamic behavior of the economy.
*   **Stability Criteria:** For discrete-time OLG systems, Lyapunov stability requires the roots of the characteristic polynomial (eigenvalues) to lie within the unit circle of the complex plane.
*   **Saddle-Path Dynamics:** In welfare economics involving rational expectations, "stability" often refers to saddle-path stability, requiring a specific number of eigenvalues outside the unit circle to match the number of jump variables (e.g., consumption), ensuring a unique equilibrium path.
*   **Demographic Transfer Matrices:** In the context of Pay-As-You-Go (PAYG) systems, the Leslie matrix functions as an intergenerational transfer matrix; its dominant eigenvalue determines the population growth rate ($n$), which acts as the biological rate of return for the pension system.
*   **Welfare Implications:** The relationship between the matrix eigenvalues (representing the interest rate $r$) and the population growth rate ($n$) determines dynamic efficiency. If $r < n$ (dynamic inefficiency), the system is stable but Pareto suboptimal, and intergenerational transfers can improve social welfare.

## 1. Introduction

The stability of welfare systems, particularly those structured around intergenerational transfers such as Pay-As-You-Go (PAYG) pensions, is fundamentally governed by the dynamic properties of the underlying economic and demographic models. These properties are mathematically encapsulated in the **characteristic polynomial** of the system's transition matrices. In the context of Overlapping Generations (OLG) models, these matrices describe how capital, consumption, and population evolve from one period to the next.

The **Lyapunov stability** of these systems is not merely a mathematical curiosity but a determinant of economic sustainability. It dictates whether an economy converges to a steady state, oscillates in limit cycles, or diverges into hyperinflation or capital depletion. The analysis relies on linearizing the dynamic system around a steady state to form a Jacobian matrix—often interpreted as the intergenerational transfer matrix in economic dynamics—and solving for its eigenvalues via the characteristic polynomial.

This report provides an exhaustive analysis of how these mathematical structures determine the fate of welfare systems. It bridges the gap between control theory (Lyapunov stability), linear algebra (characteristic polynomials), and macroeconomic theory (OLG models and dynamic efficiency).

## 2. Mathematical Foundations of Stability in Dynamic Systems

To understand the stability of welfare systems, one must first establish the mathematical framework used to analyze dynamic equilibrium. The core tool is the analysis of the system's Jacobian matrix through its characteristic polynomial.

### 2.1 The Characteristic Polynomial and Eigenvalues
In any linear or linearized dynamic system represented by the equation $x_{t+1} = Ax_t$, where $A$ is an $n \times n$ matrix and $x_t$ is a state vector, the behavior of the system is determined by the eigenvalues of $A$. These eigenvalues, denoted by $\lambda$, are the roots of the **characteristic polynomial**, defined as:
\[ P(\lambda) = \det(A - \lambda I) = 0 \]
where $I$ is the identity matrix [cite: 1, 2].

The Fundamental Theorem of Algebra guarantees that this polynomial has $n$ roots (counting multiplicity). The location of these roots in the complex plane is the primary determinant of stability [cite: 3, 4].
*   **Trace and Determinant:** For a $2 \times 2$ matrix often found in basic OLG models, the characteristic polynomial is given by $\lambda^2 - \text{Tr}(A)\lambda + \det(A) = 0$. The stability conditions can be expressed entirely in terms of the trace ($\text{Tr}$) and determinant ($\det$) [cite: 5].

### 2.2 Lyapunov Stability Definitions
Lyapunov stability theory provides the rigorous condition for system convergence.
*   **Lyapunov Stability (Marginal):** An equilibrium point $x^*$ is Lyapunov stable if, for every $\epsilon > 0$, there exists a $\delta > 0$ such that if the initial state $||x_0 - x^*|| < \delta$, then $||x_t - x^*|| < \epsilon$ for all $t \geq 0$. This means the system stays near the equilibrium [cite: 6, 7].
*   **Asymptotic Stability:** The equilibrium is asymptotically stable if it is Lyapunov stable and, additionally, $\lim_{t \to \infty} ||x_t - x^*|| = 0$. This implies the system eventually converges to the equilibrium [cite: 1, 7].
*   **Discrete-Time Criteria:** For the discrete-time difference equations used in OLG models, an equilibrium is asymptotically stable if and only if all eigenvalues of the Jacobian matrix lie strictly inside the unit circle of the complex plane ($|\lambda_i| < 1$ for all $i$) [cite: 3, 4].

### 2.3 The Role of the Jacobian in Nonlinear Systems
Welfare systems are inherently nonlinear due to utility functions and production technologies. To apply eigenvalue analysis, the system is linearized around a steady state using the Taylor series expansion. The matrix of first-order partial derivatives is the **Jacobian matrix** ($J$). The Lyapunov Indirect Method states that the local stability of the nonlinear system is determined by the eigenvalues of this Jacobian matrix [cite: 6, 8].

## 3. The Overlapping Generations (OLG) Framework

The OLG model, pioneered by Samuelson (1958) and Diamond (1965), is the standard framework for analyzing intergenerational transfers [cite: 9, 10]. In this model, agents live for two periods (young and old), and the economy's trajectory is defined by the accumulation of capital and the transfer of resources between generations.

### 3.1 The Intergenerational Transfer Matrix
In the context of welfare analysis, the "intergenerational transfer matrix" can be interpreted in two distinct ways, both of which are governed by characteristic polynomials:
1.  **The Economic Jacobian:** This matrix describes the evolution of aggregate capital ($k_t$) and consumption ($c_t$) over time. It captures the feedback loops between savings, interest rates, and wages [cite: 11, 12].
2.  **The Demographic (Leslie) Matrix:** This matrix describes the biological transfer of population cohorts. It determines the dependency ratio, which is the fiscal foundation of PAYG systems [cite: 13].

### 3.2 Dynamic Equation of Motion
The fundamental law of motion in a standard OLG model with production is often reduced to a difference equation for capital per worker ($k_t$):
\[ k_{t+1} = \frac{s(w_t, r_{t+1})}{1+n} \]
where $s(\cdot)$ is the savings function, $w_t$ is the wage, $r_{t+1}$ is the interest rate, and $n$ is the population growth rate [cite: 9, 14].

When a welfare system (social security) is introduced, the equation is modified to include taxes ($\tau$) and benefits ($b$). The stability of this system depends on the sensitivity of savings to changes in future capital stocks, which is encoded in the derivative $dk_{t+1}/dk_t$. This derivative is the eigenvalue of the scalar transition matrix (or the Jacobian in multi-dimensional versions) [cite: 11].

## 4. Determining Stability via the Characteristic Polynomial

The characteristic polynomial of the intergenerational transfer matrix determines the Lyapunov stability of the welfare system by dictating the convergence properties of the economy's capital stock and consumption paths.

### 4.1 Eigenvalues and Convergence
The roots of the characteristic polynomial, $\lambda_1, \lambda_2, \dots, \lambda_n$, dictate the system's temporal evolution. The general solution for the deviation from steady state $\hat{k}_t$ can be expressed as a linear combination of these eigenvalues raised to the power of $t$:
\[ \hat{k}_t = c_1 \lambda_1^t + c_2 \lambda_2^t + \dots + c_n \lambda_n^t \]
*   **Stable Welfare System:** If all $|\lambda_i| < 1$, the terms $\lambda_i^t$ decay to zero as $t \to \infty$. The economy returns to its steady state after a shock (e.g., a demographic shift or policy change) [cite: 1, 15].
*   **Unstable Welfare System:** If any $|\lambda_i| > 1$, the deviation grows over time. In a welfare context, this could manifest as explosive debt dynamics or a collapse of the capital stock [cite: 16].

### 4.2 Saddle-Path Stability in Rational Expectations
A critical nuance in OLG welfare analysis is that "stability" does not always mean all eigenvalues must be inside the unit circle. Because agents are forward-looking (rational expectations), the system includes "jump variables" (like consumption) that can adjust instantly.
*   **The Blanchard-Kahn Conditions:** For a unique, stable equilibrium path (saddle-path stability), the number of eigenvalues outside the unit circle (unstable roots) must equal the number of jump variables. The number of eigenvalues inside the unit circle (stable roots) must equal the number of predetermined variables (like capital stock) [cite: 11, 17, 18].
*   **Implication for Welfare:** If the characteristic polynomial yields too many stable roots, the system suffers from **indeterminacy** (sunspot equilibria), where expectations alone can drive fluctuations, destabilizing the welfare system. If there are too many unstable roots, no equilibrium exists [cite: 5, 19].

### 4.3 Bifurcations and Cycles
The coefficients of the characteristic polynomial depend on policy parameters (e.g., the replacement rate of the pension system). As these parameters change, the roots of the polynomial move in the complex plane.
*   **Hopf Bifurcation:** If a pair of complex conjugate eigenvalues crosses the unit circle, the system may enter a stable limit cycle. This implies that the welfare system generates endogenous fluctuations in inequality and consumption rather than settling to a steady state [cite: 11, 17].
*   **Flip Bifurcation:** If a real eigenvalue crosses -1, period-doubling oscillations occur. Source [cite: 11] highlights that Pay-As-You-Go (PAYG) systems with fixed replacement ratios are particularly prone to such bifurcations, making the system periodic and unstable.

## 5. Demographic Stability: The Leslie Matrix

In welfare systems, particularly PAYG pensions, the "intergenerational transfer" is also demographic. The stability of the tax base is governed by the **Leslie Matrix**, a specific type of transfer matrix.

### 5.1 Structure of the Leslie Matrix
The Leslie matrix ($L$) projects the population vector $N_t$ forward: $N_{t+1} = L N_t$. It contains fertility rates in the first row and survival probabilities on the sub-diagonal.
\[ L = \begin{bmatrix} f_1 & f_2 & \dots & f_m \\ s_1 & 0 & \dots & 0 \\ 0 & s_2 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & s_{m-1} & 0 \end{bmatrix} \]
[cite: 13].

### 5.2 The Dominant Eigenvalue and Welfare Solvency
The characteristic polynomial of the Leslie matrix determines the long-term population growth rate.
*   **Perron-Frobenius Theorem:** Since the Leslie matrix is non-negative, it has a unique dominant real eigenvalue $\lambda_{dom}$ (often denoted as $1+n$) [cite: 13, 20].
*   **Lyapunov Stability of Population:**
    *   If $\lambda_{dom} < 1$, the population declines to zero (asymptotically stable at 0, but fatal for the welfare system).
    *   If $\lambda_{dom} = 1$, the population stabilizes.
    *   If $\lambda_{dom} > 1$, the population grows exponentially [cite: 21].
*   **Link to PAYG:** The rate of return of a PAYG system is approximately the population growth rate $n$ (derived from $\lambda_{dom}$). The financial stability of the welfare system depends on the gap between this demographic eigenvalue and the economic interest rate $r$ [cite: 9, 22].

## 6. Dynamic Efficiency and Welfare Analysis

The interaction between the eigenvalues of the economic transition matrix (determining $r$) and the demographic matrix (determining $n$) defines the **dynamic efficiency** of the welfare system.

### 6.1 The Golden Rule and Dynamic Inefficiency
A central finding in OLG research is that the competitive equilibrium may not be Pareto optimal.
*   **Dynamic Inefficiency:** If the capital accumulation leads to an interest rate $r < n$ (where $n$ is the dominant eigenvalue of the population matrix), the economy is dynamically inefficient. Agents are oversaving [cite: 9, 10].
*   **Welfare Improvement via Transfers:** In this scenario, a government can implement an intergenerational transfer (PAYG pension) that takes from the young and gives to the old. This reduces the capital stock (crowding out), raising the marginal product of capital (and thus $r$). This transfer is a Pareto improvement [cite: 23, 24, 25].

### 6.2 Eigenvalue Analysis of Policy Reforms
When analyzing a reform (e.g., shifting from PAYG to funded systems), economists examine the transition matrix of the linearized model.
*   **Stability of the Transition:** Source [cite: 11] proves that introducing a small PAYG system in a dynamically efficient economy ($r > n$) can depress capital stock. The stability of this new steady state is verified by checking if the eigenvalues of the Jacobian remain within the unit circle (or satisfy saddle-path conditions).
*   **Complex Eigenvalues:** Source [cite: 26] notes that eigenvalues of the Jacobian in calibrated OLG models are often complex, generating non-monotonic dynamics (damped oscillations) during the transition between welfare regimes. This implies that welfare gains/losses may fluctuate across different generations during the transition.

## 7. Case Studies and Advanced Stability Concepts

### 7.1 PAYG vs. Funded Systems
Research indicates that the stability properties differ significantly between Fixed Contribution (FC) and Fixed Replacement (FR) pension schemes.
*   **Fixed Replacement (FR):** Source [cite: 11] shows that FR schemes often lead to characteristic polynomials with roots outside the unit circle or complex roots, leading to cycles and instability. The Jacobian determinant often exceeds 1, indicating unstable spirals.
*   **Fixed Contribution (FC):** These systems generally exhibit more robust stability characteristics, as the burden of adjustment falls on benefits rather than the tax rate, dampening feedback loops [cite: 11].

### 7.2 Infinite Debt and Saddle Points
In models including government debt, the characteristic polynomial often reveals a saddle-point structure with one stable and one unstable steady state.
*   **Debt Capacity:** Source [cite: 16] identifies that there is a "debt capacity" threshold. Trajectories starting below this threshold (on the stable manifold defined by the stable eigenvectors) converge to a valid steady state. Trajectories above it diverge, leading to a welfare system collapse (infinite debt).
*   **Eigenvalue Signatures:** The presence of a positive real eigenvalue greater than 1 in the debt dynamics equation is necessary for the government's intertemporal budget constraint to hold (the "No Ponzi Game" condition) [cite: 16, 27].

### 7.3 Robustness and Structural Stability
While Lyapunov stability focuses on a fixed set of parameters, **structural stability** asks if the qualitative behavior (eigenvalue placement) remains unchanged under small parameter perturbations.
*   **D-Stability:** Research in matrix stability [cite: 28, 29] discusses D-stability, which ensures stability persists even when matrix elements are perturbed (e.g., by demographic shocks or policy uncertainty). This is crucial for welfare systems which must endure over decades of uncertain economic conditions.

## 8. Conclusion

The characteristic polynomial of intergenerational transfer matrices serves as the "genetic code" of a welfare system's dynamic behavior. By solving for the roots (eigenvalues) of this polynomial, economists determine:
1.  **Local Stability:** Whether the economy converges to a steady state following shocks (Lyapunov asymptotic stability, $|\lambda| < 1$).
2.  **Determinacy:** Whether a unique equilibrium path exists (Saddle-path stability, requiring a specific mix of stable/unstable roots).
3.  **Solvency:** Whether the demographic growth rate (dominant eigenvalue of the Leslie matrix) is sufficient to support PAYG liabilities relative to the economic interest rate.
4.  **Cyclicality:** Whether the system will exhibit damped oscillations or permanent limit cycles (complex eigenvalues).

Consequently, the design of robust welfare systems requires ensuring that the characteristic polynomials of both the demographic and economic transition matrices yield eigenvalues that satisfy the conditions for dynamic efficiency ($r > n$) and saddle-path stability, thereby preventing both capital depletion and explosive debt spirals.

## References
[cite: 23] Ecineq. (2023). Dynamic stability of OLG models welfare systems.
[cite: 9] Mukoyama, T. (2020). Diamond Overlapping Generations Model.
[cite: 10] Wikipedia. (n.d.). Overlapping generations model.
[cite: 30] MPRA. (2025). Long-term macroeconomic and welfare impacts of transitioning from PAYG.
[cite: 22] Hendricks, L. (2024). OLG Welfare function.
[cite: 6] Caltech. (n.d.). Lyapunov's direct method.
[cite: 31] Lemmon, M. (n.d.). Lyapunov stability.
[cite: 7] Wikipedia. (n.d.). Lyapunov stability.
[cite: 15] Chen, X. (n.d.). Lyapunov's approach to stability.
[cite: 32] ArXiv. (2015). Lyapunov functions and stability.
[cite: 24] Cambridge. (2008). Intergenerational transfers and welfare.
[cite: 33] Davila, E., et al. (2025). Welfare assessments in economies with rich demographic structures.
[cite: 34] YouTube. (2020). Finding the stable age distribution of a 2x2 Leslie matrix.
[cite: 35] Review of Economic Studies. (1989). Welfare properties of dynastic equilibria.
[cite: 1] Kyungpook National University. (2016). Discrete-time internal stability and Lyapunov Theorem.
[cite: 28] ResearchGate. (2019). Unifying matrix stability concepts.
[cite: 2] EconStor. (2025). Equilibrium properties and Lyapunov stability.
[cite: 29] ArXiv. (2019). Matrix and polynomial D-stability.
[cite: 20] ResearchGate. (2025). Sustainability of a Pay-as-You-Go Pension System.
[cite: 13] NCWU. (2025). Leslie Matrix and population stability.
[cite: 11] AccessEcon. (2003). Economic dynamics in an OLG model with PAYG.
[cite: 21] Unicas. (2014). Population forecast and Leslie model.
[cite: 2] EconStor. (2025). Uniqueness and stability using Jacobian matrix.
[cite: 36] KTH. (2024). Lyapunov theory and characteristic polynomials.
[cite: 37] LUT Pub. (2022). Lyapunov stability theory and chaos theory in economics.
[cite: 38] ArXiv. (2021). Symmetric matrix-valued dynamical systems.
[cite: 5] EconStor. (n.d.). Impact of intra-industry trade and capital mobility on stability.
[cite: 17] AMSE. (2024). Local indeterminacy and characteristic polynomials.
[cite: 10] Wikipedia. (n.d.). Overlapping generations model history.
[cite: 14] MIT. (2011). Canonical OLG Model and stability.
[cite: 25] ULiege. (n.d.). OLG model and Second Welfare Theorem.
[cite: 39] Edmond, C. (2021). Dynamic inefficiency in OLG growth model.
[cite: 3] Cook, J. (2019). Stability criteria in a nutshell.
[cite: 4] StudySmarter. (2024). Eigenvalue analysis.
[cite: 40] Quora. (2024). Determining stability using eigenvalues.
[cite: 41] Review of Social Economy. (2013). Leslie matrix and welfare systems.
[cite: 13] NCWU. (2025). Leslie matrix structure and stability.
[cite: 21] Unicas. (2014). Leslie dominant eigenvalue and population stability.
[cite: 42] Taylor & Francis. (2024). Leslie matrix and labor market structural changes.
[cite: 43] ResearchGate. (n.d.). Modeling a demographic problem using the Leslie matrix.
[cite: 8] CESifo. (2025). Characteristic polynomial and Jacobian matrix.
[cite: 11] AccessEcon. (2003). Stability of PAYG system eigenvalues.
[cite: 26] BCL. (n.d.). Convergence speed and eigenvalues of the Jacobian.
[cite: 12] CMU. (2019). Stability of PAYG system and Jacobian eigenvalues.
[cite: 44] ISID. (2017). Eigenvalues of the Jacobian matrix in political economy models.
[cite: 16] Management Science. (2025). Infinite debt rollover and saddle point stability.
[cite: 27] EconStor. (2024). Optimal policies and saddle point stability.
[cite: 18] Cambridge. (2021). Saddle-path stability and currency substitution.
[cite: 19] Toda, A. A. (2026). Equilibrium Determinacy in OLG Models.

**Sources:**
1. [kocw.or.kr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL_JFns_Msch1sLtIx-XSCEOOexpFtEg_u6zkOrqe7NyqOFVHtFEHjvySoNqbNHjx45flI5yLmG4Yg5eaMh0sxUue08-vPv8BUQ3hCNNBwjiaExJphDrIDzOpiC5ychCVrnANRBEOQv8u1vYIV3t2jZYWFMA6pNHHgGc-W5RWXPk_l)
2. [econstor.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc_t-lTaZYdf1Bc3LEvACUeencRolo10rlQnvx4GpBe9itDXo3F_ZDTJZjIz5PX5hBIAjWQke25bSgcMq7QKvAqg_1o9UBt-XsuD5pa9RwvjtbosgNBtmELMm7npPqbUj-QKf7HHiR1tp1KIiDBG7EslvJN3ihZ0EZSA==)
3. [johndcook.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzRo38YvC5h_JU-yiUMsq5-ZHchou1OXUUPMRKE6ha_ABW5lefJqQ4iAIxO6Lu0j3VOPQtq8eohL6skXkj1Jo-LeqNip_2dBcWuesf4xhrJ90aJ8YJCKGOBzHDIs0YrqNJHoMkPO6HSjRg9V6mabV-y_81)
4. [studysmarter.co.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFgRWW3WsBBHct54Pw87rBwbzy7ipJz2aehBXfHfQimJBtRdPzzAnRZwmQhmJuQ-abithF4vyPkJ2_hltbLtD_OkgSKPcVK02yaqnb5VN-y_Eaf0atp-0MKuA_JzF9MrljqBlYL95HkqbyXqfWnuvskQRBTYrEaNMR0OyaPI_sTIGgg8WS6mNbkcorLY9TjYz-OBCeIyg_Kko=)
5. [econstor.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG849gIJNH-beMEPtzVLfWpk1MAoPiX3fGD4Qchj9zUoTWH32CWMK8BKERZlCGmucnZMfd4r_SGTOhAR7yHqJzM85verxXI_2LB9MEwJVeNYH2BBTjIRQjZLdpAYtwI8upZn2LdxcsrVwwMkpPZTmAvVBE=)
6. [caltech.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErCTyKNLgiuNYOoj_O8Ky4y98JWrteQiAvn82eh5rFXpxOx8YGArcS5AWpzLPcumA2LAzWlJwPaYE8m1Yc5HbNCQgYeQTGYNdph4BRTLbTmiuE_nquwKeWyPNahMo0pjWWyd6oukMYUg10AC3-0iwI_oVf0tcSemUY3M7nkrzUyGKU3n4=)
7. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnA5njGuoCCUzGsQS98rqgoip4DnwFDQlIe3JjNdYHoSXjKi3UdF2tCZGjm3ZdSb1fJfByskOAJvV1_9YH7NIrqbCOYN7I8hNkEzDYdTDRVdTO5UjTyNRG16AomjU7C99vmvr1CL8=)
8. [ifo.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwt2DwAnJyfsX71OVdcrx-Obu1gHUycTsYExkKMY1-xZbEPBfhgsseT4aWStQssyru1b1fyVDIaRNFlQSAOX3SGHORdcDfZOSM3PrAwh_lr1jwrMnxtYxgW_tl54iD4jGUdg==)
9. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEx14jDHrJr0SW3Ykpf_fLhXOjxX_9iQFWXFs4BUJiGQKaYNTJPmal8std4SWxhM24YDg7jQkcuIiHjwPPILr0qnCueZU-iPOJSDYbc361TzivjWki4U1HeRjjUYlLF90otewGb-Cf)
10. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9wdeY3DXqp30mRmfhJ9RHUXKdM1e7qHCj3Gqkgizv-Z7Xj9n2Qz1Ernx7VGD1RE6LIxdPbdGUoZzYee_NYKLY8S13bkTSIrYajgfiP2r0ojqTGG0mUS5XNiVOOVZMxNK3W6t0eWDvO20hE18621dunw==)
11. [accessecon.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLq0kgShC6DiRLrXzxM22OMl0WRN_0HtPTlfjXBn6P34P6iLJxCl9QmpgXgbrw5_uftPdm3pARy0Zrxr2veeGOkxzu2JVM_ceGGbddqnA9t3gc0Fz46YEt72oUDV860MZtyYoq14Rk_cINtvBiA2kuLEdYtSc=)
12. [cmu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo9etwdq-pQ4gLK-D45IFRrFewkwrN3Tq75B8Jyf69y2pZ5RrdsVKkTJrJZM7mQn-vW6m2JuVmRtXa4TuL58QAmNq9lBPx657tUx87gQGx3cXeB0YkmpxSBU9VKkgwhOD0EynMtIwyZpBJnsL-luHhfSYdKA9uIaQH5_ZpoSylWIDizNNaoU-xTwruannJtuv_7CrHmZDFue0XqbU8PzQ=)
13. [ncwu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEF39m7KP9GtguKPmQjHbDbwhHPDPTEyUc5nvrvsDKB1bGnqG--fW8LCCLqUt0UBsiu0GwMeT6FyECdXXTA0_p6P4leY-V5zcXmHY0fE0V0iydJswMwJqbkILvAJCpN_1T6YTNtUKkxLStrpl_9iNsSHCW5PmenTQm1Wb_4tFAweNuE1dcdK2aF6H1zmD845Yt69D1k)
14. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGS1lvdadxum5iMhmJYrHsKBYeqDb0VImpdWaj_EQxL7chChFnNPGcoqdc3z1XLRHJ41pzyrqPPKA1q7Wb9dj1sx54N2FCueGosrXtzb1bj82Fa7BHElCt7moAvJolpyUxzjzXL5wnIKayxoPwjAKiRP1TbIFKiZ4pML-pe6KjeQEzupeafx1hh2CX3Y6IZnn8yXo56Mc_Dk6vdi_O8uR8PMA=)
15. [washington.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHsbKJw0QgEDoAuyIAbRaJbEu7dzUdoYkvDJbyO2bYs-etWG4FvTwg3tgIkV7mWzBDqtZ6VX8pDE6iW6WbKrxsZ06MBF179zUDdDvRpPyC1K9HkDhQnsqf2YmJI0GnwbS3PN7T3-q3WwI_9K3E-0Jfsz4TPRLy-fJ0ajCba6sGasvrAjC-RgfRhA==)
16. [informs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfR4Fo00VOAH67pEZJtUPdSLVc_tkgfnIeYfcYMbaVhq9Ub4RJuy_qZP3HY6FuFom4YztKhTrEUF4zl6igbWN8gF5KQ8mfQReAUP1Eofk6kzb968XJjox0rClgT8WBg0ZHEv_imWuewOXwgfUFVIfl)
17. [amse-aixmarseille.fr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH96flsV1QpPsPssvdeYxkYFLiqPiTsumydsmYRggp1h47H1l6MQluHJ7bqtfKAJ0CYnE_l9AKmklJ0gK_NlyKirnOnFC-ZrRYprZdQsoIrbcxcfI4Y-B9MM0YaEoUA8_PvF-DZZX3LzaEGnSFR5IdMa9SHGEW80eF7sdYjuoaANEUdtb7_WYMtmvWMZvM=)
18. [cambridge.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJzhWqEoap1kD-HTBg9rzUGCi-oVwr5F_47Z66JXBic_j3X4XLT-UKcoso9LUBm11Um6WJ9AbF7KoM03Ug8Gk475volVPTUPnrP9RS4LtY4NxiND8_UOS6TKF5SY5EKS7a_lJ3mRO4MY1oIKpxtVyRGnFXcjn_66NRypxBsJqv8KLZIzBZ77TDK4IZN6v2TYufvxA0ZoHRMq8brpPewB3ewhuhEDMqPl92xOVyq7eMzs6IpbbslvcCT7DgvGcbsMHj_uyj97mLVcqFZZjFQ9c=)
19. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYPvJM-9fYto7f_qiKkReOwIxVfhJUWf1mZwJBUbsXWAmAkioMLjIXrYwoEkREYhGZRZDIeNBsZpgHAYJytQWIb4yvPl9GzKebdjPcP1xXA-OO6Jz9XTTUDy4teSVs1qDxCrDCw2GT)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEG-GH54seqoaDiGy8BIDw6jmOWWfzetpO0e7WV3tELKhzLTKPYk7dT3kc1HicD0KN88BjKaY4sBN25GAo09lqueWX6yVU6aoLfYbK8D3kmSj0dIhiCOIYDnNjxO_kya9_-qnsW9_guzgZmIetV0TyXJ5vLmJFcUzfwa7ZzUOFlw0ZScrN4MYxP1eXjKxmQvtr_Lk4x598-NIg07R4OT3nHjkbETrcmGPsyNqyEx6GW-RByxNi_gWI0IQ==)
21. [unicas.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo12g-Y3F1Kxx8EAoWiRnYRaDjXPAhzCyPM1y6VZwhC3YhiHR23P0yGgmXCf5jYbe1PP4uUsiJldT5FWbaqYAh48xw1uY1U6hvk_m0P3U00zHR1q5imZH4S590VCxPVc7EJwEnmHh6m-LDzp0zOFh1vmDemy34iZi-7aGY_zYMAZP7Fqt9v4JwS1JsRTtbKBk=)
22. [lhendricks.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBorCYnTwi3uIsQIKuTRf5QkCu33bxPViChqodYtD7QsLzdhp4H4YcXAtq_anCC1bopAwpBvnPDHQemV8ebO_-HDl7Jczo1Jqpyz1lHRjvzqMIBxcWU2P4_oSafxhgPHNQcAXiiS0=)
23. [ecineq.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUP2APs4ygxDvWLROw9_XA3ZCvU08HJHyKMZnu6dp78tLmzvSI5irOlBBtMyRmsn_mrq9ItPZCOPzrr2z1uE2HIluR4HCOD9yrhGpjnwKwFQo0mYrrLljkhSQ8KxJjrbDVwDlrGkn8c1JSMrtVySIpeqfRRJqfbBK7)
24. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETavixQUWRkMicMdsXQf9hUzR7gYcc8EAPrmxtCCPvJiYqquWActEHZQD7l2Ts1MYVr1I50mzTMHvRAM5cVMF5qA2mKvRsC-cz4HvjJGhaOaskSl78fhORAJglZMgEltDF33ZTMrNCoE4CjEoMU23CZivotQ==)
25. [uliege.be](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFq-3Vxno3S3xy7Eb4u-Ky68B2jP37Ieyc1c-miOes7kvD0_9LSaSKrtH_NTFolW7tQshLCv6BS0lZaLq-kvQcCZzSgjauci-ScsbOa778J2ZHx4Avoin1sFBpUwP3_koWDMKc5sXEo5EvQz1YxM8A8E94kig==)
26. [bcl.lu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGH09f_jMT1PHxPx0FmskOz7U_dlJyKxtfYWUcqJM_1zhN4D_Sb789tPQ3RBw4Iy7dMHHGN6SISg9M_NnyKp6mHZnQdT4q8LEVQ58ZclGA8608BDgMhoBEk4u1mK-J5jC1ZcLgFXykPJ3fz45wSwh29hhFziY9oCA==)
27. [econstor.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGc0ubSY_R2j5ZzAqyHY_DeJrwT9xIbFIgBQEwN3Ses4yi_YuK7gPNZtjDlPRBp-eLH1ZAM8_EwXXSxKT9K16XIZR1_z_t3FUCxZi1WH3jlHeyB7RQbIUcsbsCTwsxzTq-B4bDRgJbALyITt4B1vysxg6T0aM-TUczV)
28. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeHAx2h-e9wSZwCA-8W5Q7CJbGkk5ej2IEPW_Vc_vmF8obcV5s68TS8KNYVNrSTImq6PIZDjQb6_057SdObjBmcWXGHMirtHwIhw0b3iCbNRIhEfy6Nz_sCCNWS3RC_vNtBEBoYvfeuQkqhFW0jX8YUfM_lmltX41wyfMUwOqZQiA31F-VaPfWa0fQeG3UqFpApctH2GgsHLzzeQm2mlIbwY4D40eIQg==)
29. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdaSsZ4hJSeprok4MggCb6DQqTEmeSk6JhNmE-bYAQtnJRylwCNfYbZGKy2HNYiz5f2qze7Kao1lbVZMz8SINlkVlguQVB-jmFCbIsrNp9Dm3IKdkbmg==)
30. [uni-muenchen.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBcB98kqMFyczWbA5oxt_mTbQ-1vYU5RnfRCfo4U_SsGDJD0qbqmT_J264fHuREAyP_SBgF88YPuQeoDGfBGZoO89f1gmxSV_UAno4DT9TgjRaaINjSvezi3FMDwbMvjxuB2T9KRBLol2mopjKD1vqqvCAEg==)
31. [nd.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwYKzSGe1yPwRW08izXl4xMw5mCb6Q1eRdlWBnf1uAE5TopkLTwLnaFDTHXlpZl7jfPkg1opNl820vjeXQitCY9DVyiDHavq0MHxg55ExTJOgEQVi5tfKprtx97CYJjtzmpnolDGCtt2mKT9NEylN0ishB9OE=)
32. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErLC55ybdKQ8rzt1EtP9d8-ECSrjwWXcU3xOhJDG8kx_ugjJoLHEpalGdxGEsAXSwRsIe0p_92xfqfx2TVlotCiuhY5wZZJ0uw9g7VThm8nGBYl519)
33. [bancaditalia.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4nLqCw2it-Jn6m6x5-0TVG6L_R7XCnHDCzD6Doe7S2ed45AcaRrYw5a38ztQuUUJsb8FXhZdIadtaEopjqzgtuPOBZvi3r188IeuajelQ3EHSagAGiJFI4BWmn49oTLo6ZFl8JQUBcPMvG4-ZSjoRTSmz9T8557kVlaa7k_4AdWAXXjVDYTPsiQ==)
34. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaNXByPpEIj9IPLtcVpzxg9qYA6zjjkWU3pUn64yagU3kGyQMsz1ODT_KH3vUqG77yvVewnm9xtkuXTZBxfakUH_0OgzqNEdmjkjctNtID6QLpTLDBamhrN0wnx3jheD6n)
35. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaEIJ0bEFqaj-Pbgg__zfuR4yv2O2oASb_dqmwkC_t8GlByapV25jnKXEjqZ13G3Go2aXqJnHDY3RXsCYRxJarFT6RYuSfZP3EWuGaUyCK1o8X1v3J3Pn1_QL5yfzFZTZb8covp9Q3taMabKomFy0oADAi)
36. [kth.se](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_USLBJO6vBTo_IZLWD0w071XURMbL_oeqjnB-WmTAZDZFxWpOzPEmNeMTyIrqdlakwCLN_YihLC-ayhhNov1afg4wOBkqq3iuku03O9326ypI9fcuA1kL9rGbSqeb4HhJx-ZIn4OWdEhEC9X9O0YzSVWWf-PC7K9SOezSMnW5dw==)
37. [lut.fi](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVyPOFI7yAKeJAtkFLDxDAuSyuVmsiGQlQ5I_ks9E2vImmdpdlNo3olWY_xYbEcBt8IWSU-NXvX4u1ADITOvXxEeHqiL3LCY8bLHCX_L7LwNP32JU5J4fe5P0PNQsmt2sySqjZ1JXoziB2OspuMVI4gYfJzYlTgkllKmxXq7GmmWCwNL4=)
38. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMES1XgmuUJ_zfmL9F060Is4iUYIVZNT-6kbZ-zMUzCfA8Qi6JPRdNmages6tpdqhC0CpZmDYSnB7JLXiEyooAR5qHIpYqvLsFjd0b4Hoaskfkb5tPiw==)
39. [chrisedmond.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9gLa0HHdUTVzccMX_D5wOADL_YddI0C-qz3Ea6c7z880frdpmBDAL8Ldvy7T-Czo4XnfYMmSnYWNONhLL1nXXyf_T9e8zYdwzU9kA0nm9iCDYE7A5US_v9pokVWvE50L9pFdF0f2CCRkUp0xqRXAf5A==)
40. [quora.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFviRNUn3j4ZxHzdTZW0pjcIHnBmk3t_8EOm6xG9qUDO1JXSVwAYP96cER0dXMJNsIOdS0qORlt6BA4_diCTti73-8AEds8X1E3ERtu7RJGggmG6aAJOFiM7XFbqQ6BfnupSOcnIJYkmaPZ8GkWC0JB8XmJfWr7xnPeDl-b64X8hsR3hHrwWGdraobZcs3yvSWTgtzkSYfEHM5_9vvGENRfAJry_pxXNysPzbFP5jo8bqqL5oAifVEXtstaGsaDKTK3zxHv)
41. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuDmWwpRtt3EfqRSF5mEje9b45u7VH6V6fDCFaRS_CJuLDFdJl1hODWrMc15l2tW20F3TdLNVyI8yq7_AdqH7TafUpwK-Inc4AZwKUrAmkEDi9L4WWBRXe_XzSScqhNImoCq-6qjw5Wsk5GBhPRg==)
42. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3nW0_dEm0joB9P9wYIpvN29Y3WG1w4ja7oQNSNhIb9ni7s534qJ6mc8K00BDMauLnxb9VvJWa7avqWZ-gaRuPSFsVSnIfYcNjVA7QYvYA2l1v_h9sh8O7aJgIpW4WKWE_w1pLrR3bBE30QL3FELPz8ASAsR7bDd0=)
43. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKDsnYtlfbUR8FXYV-9xvp0LD3uNfFJt8CDhjzvsx0m20D2ceK3V5RpbC2c5PFK9TXcAtX_YS4O7YjVGm1h49yHdn_f7ErqNYDnNBFO_6E2iPqr1CKO7dczENeZMNZg7nmX7Se0lpMr_6Xu8tFDY4rhluAwwg_9moEiQ8dYbJ_yx9KL_mH9XPLwB1Bpgj_DCM03YnJsQGU7sx9Yjbbprs=)
44. [isid.ac.in](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWjuaZIPpH3QOZEd1FpzEmgoXuoVnanomIFIBIobtJIaiKqkYKlPcVe-nFoQGOXNWsFTRUN42cFirBU1uqGxc8yIOIeJ4vSFLYe6CChQl-rkZOTcZEc74qEHviyJBiPVVrCM_mFrYbYgqL)


## Annotations
Annotation(end_index=3597, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL_JFns_Msch1sLtIx-XSCEOOexpFtEg_u6zkOrqe7NyqOFVHtFEHjvySoNqbNHjx45flI5yLmG4Yg5eaMh0sxUue08-vPv8BUQ3hCNNBwjiaExJphDrIDzOpiC5ychCVrnANRBEOQv8u1vYIV3t2jZYWFMA6pNHHgGc-W5RWXPk_l', start_index=3585)
Annotation(end_index=3597, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc_t-lTaZYdf1Bc3LEvACUeencRolo10rlQnvx4GpBe9itDXo3F_ZDTJZjIz5PX5hBIAjWQke25bSgcMq7QKvAqg_1o9UBt-XsuD5pa9RwvjtbosgNBtmELMm7npPqbUj-QKf7HHiR1tp1KIiDBG7EslvJN3ihZ0EZSA==', start_index=3585)
Annotation(end_index=3807, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzRo38YvC5h_JU-yiUMsq5-ZHchou1OXUUPMRKE6ha_ABW5lefJqQ4iAIxO6Lu0j3VOPQtq8eohL6skXkj1Jo-LeqNip_2dBcWuesf4xhrJ90aJ8YJCKGOBzHDIs0YrqNJHoMkPO6HSjRg9V6mabV-y_81', start_index=3795)
Annotation(end_index=3807, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFgRWW3WsBBHct54Pw87rBwbzy7ipJz2aehBXfHfQimJBtRdPzzAnRZwmQhmJuQ-abithF4vyPkJ2_hltbLtD_OkgSKPcVK02yaqnb5VN-y_Eaf0atp-0MKuA_JzF9MrljqBlYL95HkqbyXqfWnuvskQRBTYrEaNMR0OyaPI_sTIGgg8WS6mNbkcorLY9TjYz-OBCeIyg_Kko=', start_index=3795)
Annotation(end_index=4111, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG849gIJNH-beMEPtzVLfWpk1MAoPiX3fGD4Qchj9zUoTWH32CWMK8BKERZlCGmucnZMfd4r_SGTOhAR7yHqJzM85verxXI_2LB9MEwJVeNYH2BBTjIRQjZLdpAYtwI8upZn2LdxcsrVwwMkpPZTmAvVBE=', start_index=4102)
Annotation(end_index=4548, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErCTyKNLgiuNYOoj_O8Ky4y98JWrteQiAvn82eh5rFXpxOx8YGArcS5AWpzLPcumA2LAzWlJwPaYE8m1Yc5HbNCQgYeQTGYNdph4BRTLbTmiuE_nquwKeWyPNahMo0pjWWyd6oukMYUg10AC3-0iwI_oVf0tcSemUY3M7nkrzUyGKU3n4=', start_index=4536)
Annotation(end_index=4548, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnA5njGuoCCUzGsQS98rqgoip4DnwFDQlIe3JjNdYHoSXjKi3UdF2tCZGjm3ZdSb1fJfByskOAJvV1_9YH7NIrqbCOYN7I8hNkEzDYdTDRVdTO5UjTyNRG16AomjU7C99vmvr1CL8=', start_index=4536)
Annotation(end_index=4782, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL_JFns_Msch1sLtIx-XSCEOOexpFtEg_u6zkOrqe7NyqOFVHtFEHjvySoNqbNHjx45flI5yLmG4Yg5eaMh0sxUue08-vPv8BUQ3hCNNBwjiaExJphDrIDzOpiC5ychCVrnANRBEOQv8u1vYIV3t2jZYWFMA6pNHHgGc-W5RWXPk_l', start_index=4770)
Annotation(end_index=4782, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnA5njGuoCCUzGsQS98rqgoip4DnwFDQlIe3JjNdYHoSXjKi3UdF2tCZGjm3ZdSb1fJfByskOAJvV1_9YH7NIrqbCOYN7I8hNkEzDYdTDRVdTO5UjTyNRG16AomjU7C99vmvr1CL8=', start_index=4770)
Annotation(end_index=5074, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzRo38YvC5h_JU-yiUMsq5-ZHchou1OXUUPMRKE6ha_ABW5lefJqQ4iAIxO6Lu0j3VOPQtq8eohL6skXkj1Jo-LeqNip_2dBcWuesf4xhrJ90aJ8YJCKGOBzHDIs0YrqNJHoMkPO6HSjRg9V6mabV-y_81', start_index=5062)
Annotation(end_index=5074, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFgRWW3WsBBHct54Pw87rBwbzy7ipJz2aehBXfHfQimJBtRdPzzAnRZwmQhmJuQ-abithF4vyPkJ2_hltbLtD_OkgSKPcVK02yaqnb5VN-y_Eaf0atp-0MKuA_JzF9MrljqBlYL95HkqbyXqfWnuvskQRBTYrEaNMR0OyaPI_sTIGgg8WS6mNbkcorLY9TjYz-OBCeIyg_Kko=', start_index=5062)
Annotation(end_index=5572, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErCTyKNLgiuNYOoj_O8Ky4y98JWrteQiAvn82eh5rFXpxOx8YGArcS5AWpzLPcumA2LAzWlJwPaYE8m1Yc5HbNCQgYeQTGYNdph4BRTLbTmiuE_nquwKeWyPNahMo0pjWWyd6oukMYUg10AC3-0iwI_oVf0tcSemUY3M7nkrzUyGKU3n4=', start_index=5560)
Annotation(end_index=5572, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwt2DwAnJyfsX71OVdcrx-Obu1gHUycTsYExkKMY1-xZbEPBfhgsseT4aWStQssyru1b1fyVDIaRNFlQSAOX3SGHORdcDfZOSM3PrAwh_lr1jwrMnxtYxgW_tl54iD4jGUdg==', start_index=5560)
Annotation(end_index=5772, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEx14jDHrJr0SW3Ykpf_fLhXOjxX_9iQFWXFs4BUJiGQKaYNTJPmal8std4SWxhM24YDg7jQkcuIiHjwPPILr0qnCueZU-iPOJSDYbc361TzivjWki4U1HeRjjUYlLF90otewGb-Cf', start_index=5759)
Annotation(end_index=5772, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9wdeY3DXqp30mRmfhJ9RHUXKdM1e7qHCj3Gqkgizv-Z7Xj9n2Qz1Ernx7VGD1RE6LIxdPbdGUoZzYee_NYKLY8S13bkTSIrYajgfiP2r0ojqTGG0mUS5XNiVOOVZMxNK3W6t0eWDvO20hE18621dunw==', start_index=5759)
Annotation(end_index=6397, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLq0kgShC6DiRLrXzxM22OMl0WRN_0HtPTlfjXBn6P34P6iLJxCl9QmpgXgbrw5_uftPdm3pARy0Zrxr2veeGOkxzu2JVM_ceGGbddqnA9t3gc0Fz46YEt72oUDV860MZtyYoq14Rk_cINtvBiA2kuLEdYtSc=', start_index=6383)
Annotation(end_index=6397, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo9etwdq-pQ4gLK-D45IFRrFewkwrN3Tq75B8Jyf69y2pZ5RrdsVKkTJrJZM7mQn-vW6m2JuVmRtXa4TuL58QAmNq9lBPx657tUx87gQGx3cXeB0YkmpxSBU9VKkgwhOD0EynMtIwyZpBJnsL-luHhfSYdKA9uIaQH5_ZpoSylWIDizNNaoU-xTwruannJtuv_7CrHmZDFue0XqbU8PzQ=', start_index=6383)
Annotation(end_index=6602, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEF39m7KP9GtguKPmQjHbDbwhHPDPTEyUc5nvrvsDKB1bGnqG--fW8LCCLqUt0UBsiu0GwMeT6FyECdXXTA0_p6P4leY-V5zcXmHY0fE0V0iydJswMwJqbkILvAJCpN_1T6YTNtUKkxLStrpl_9iNsSHCW5PmenTQm1Wb_4tFAweNuE1dcdK2aF6H1zmD845Yt69D1k', start_index=6592)
Annotation(end_index=6972, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEx14jDHrJr0SW3Ykpf_fLhXOjxX_9iQFWXFs4BUJiGQKaYNTJPmal8std4SWxhM24YDg7jQkcuIiHjwPPILr0qnCueZU-iPOJSDYbc361TzivjWki4U1HeRjjUYlLF90otewGb-Cf', start_index=6959)
Annotation(end_index=6972, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGS1lvdadxum5iMhmJYrHsKBYeqDb0VImpdWaj_EQxL7chChFnNPGcoqdc3z1XLRHJ41pzyrqPPKA1q7Wb9dj1sx54N2FCueGosrXtzb1bj82Fa7BHElCt7moAvJolpyUxzjzXL5wnIKayxoPwjAKiRP1TbIFKiZ4pML-pe6KjeQEzupeafx1hh2CX3Y6IZnn8yXo56Mc_Dk6vdi_O8uR8PMA=', start_index=6959)
Annotation(end_index=7381, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLq0kgShC6DiRLrXzxM22OMl0WRN_0HtPTlfjXBn6P34P6iLJxCl9QmpgXgbrw5_uftPdm3pARy0Zrxr2veeGOkxzu2JVM_ceGGbddqnA9t3gc0Fz46YEt72oUDV860MZtyYoq14Rk_cINtvBiA2kuLEdYtSc=', start_index=7371)
Annotation(end_index=8295, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHsbKJw0QgEDoAuyIAbRaJbEu7dzUdoYkvDJbyO2bYs-etWG4FvTwg3tgIkV7mWzBDqtZ6VX8pDE6iW6WbKrxsZ06MBF179zUDdDvRpPyC1K9HkDhQnsqf2YmJI0GnwbS3PN7T3-q3WwI_9K3E-0Jfsz4TPRLy-fJ0ajCba6sGasvrAjC-RgfRhA==', start_index=8282)
Annotation(end_index=8295, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL_JFns_Msch1sLtIx-XSCEOOexpFtEg_u6zkOrqe7NyqOFVHtFEHjvySoNqbNHjx45flI5yLmG4Yg5eaMh0sxUue08-vPv8BUQ3hCNNBwjiaExJphDrIDzOpiC5ychCVrnANRBEOQv8u1vYIV3t2jZYWFMA6pNHHgGc-W5RWXPk_l', start_index=8282)
Annotation(end_index=8501, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfR4Fo00VOAH67pEZJtUPdSLVc_tkgfnIeYfcYMbaVhq9Ub4RJuy_qZP3HY6FuFom4YztKhTrEUF4zl6igbWN8gF5KQ8mfQReAUP1Eofk6kzb968XJjox0rClgT8WBg0ZHEv_imWuewOXwgfUFVIfl', start_index=8491)
Annotation(end_index=9195, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJzhWqEoap1kD-HTBg9rzUGCi-oVwr5F_47Z66JXBic_j3X4XLT-UKcoso9LUBm11Um6WJ9AbF7KoM03Ug8Gk475volVPTUPnrP9RS4LtY4NxiND8_UOS6TKF5SY5EKS7a_lJ3mRO4MY1oIKpxtVyRGnFXcjn_66NRypxBsJqv8KLZIzBZ77TDK4IZN6v2TYufvxA0ZoHRMq8brpPewB3ewhuhEDMqPl92xOVyq7eMzs6IpbbslvcCT7DgvGcbsMHj_uyj97mLVcqFZZjFQ9c=', start_index=9177)
Annotation(end_index=9195, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH96flsV1QpPsPssvdeYxkYFLiqPiTsumydsmYRggp1h47H1l6MQluHJ7bqtfKAJ0CYnE_l9AKmklJ0gK_NlyKirnOnFC-ZrRYprZdQsoIrbcxcfI4Y-B9MM0YaEoUA8_PvF-DZZX3LzaEGnSFR5IdMa9SHGEW80eF7sdYjuoaANEUdtb7_WYMtmvWMZvM=', start_index=9177)
Annotation(end_index=9195, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLq0kgShC6DiRLrXzxM22OMl0WRN_0HtPTlfjXBn6P34P6iLJxCl9QmpgXgbrw5_uftPdm3pARy0Zrxr2veeGOkxzu2JVM_ceGGbddqnA9t3gc0Fz46YEt72oUDV860MZtyYoq14Rk_cINtvBiA2kuLEdYtSc=', start_index=9177)
Annotation(end_index=9513, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG849gIJNH-beMEPtzVLfWpk1MAoPiX3fGD4Qchj9zUoTWH32CWMK8BKERZlCGmucnZMfd4r_SGTOhAR7yHqJzM85verxXI_2LB9MEwJVeNYH2BBTjIRQjZLdpAYtwI8upZn2LdxcsrVwwMkpPZTmAvVBE=', start_index=9500)
Annotation(end_index=9513, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYPvJM-9fYto7f_qiKkReOwIxVfhJUWf1mZwJBUbsXWAmAkioMLjIXrYwoEkREYhGZRZDIeNBsZpgHAYJytQWIb4yvPl9GzKebdjPcP1xXA-OO6Jz9XTTUDy4teSVs1qDxCrDCw2GT', start_index=9500)
Annotation(end_index=10052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH96flsV1QpPsPssvdeYxkYFLiqPiTsumydsmYRggp1h47H1l6MQluHJ7bqtfKAJ0CYnE_l9AKmklJ0gK_NlyKirnOnFC-ZrRYprZdQsoIrbcxcfI4Y-B9MM0YaEoUA8_PvF-DZZX3LzaEGnSFR5IdMa9SHGEW80eF7sdYjuoaANEUdtb7_WYMtmvWMZvM=', start_index=10038)
Annotation(end_index=10052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLq0kgShC6DiRLrXzxM22OMl0WRN_0HtPTlfjXBn6P34P6iLJxCl9QmpgXgbrw5_uftPdm3pARy0Zrxr2veeGOkxzu2JVM_ceGGbddqnA9t3gc0Fz46YEt72oUDV860MZtyYoq14Rk_cINtvBiA2kuLEdYtSc=', start_index=10038)
Annotation(end_index=10166, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLq0kgShC6DiRLrXzxM22OMl0WRN_0HtPTlfjXBn6P34P6iLJxCl9QmpgXgbrw5_uftPdm3pARy0Zrxr2veeGOkxzu2JVM_ceGGbddqnA9t3gc0Fz46YEt72oUDV860MZtyYoq14Rk_cINtvBiA2kuLEdYtSc=', start_index=10156)
Annotation(end_index=10985, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEF39m7KP9GtguKPmQjHbDbwhHPDPTEyUc5nvrvsDKB1bGnqG--fW8LCCLqUt0UBsiu0GwMeT6FyECdXXTA0_p6P4leY-V5zcXmHY0fE0V0iydJswMwJqbkILvAJCpN_1T6YTNtUKkxLStrpl_9iNsSHCW5PmenTQm1Wb_4tFAweNuE1dcdK2aF6H1zmD845Yt69D1k', start_index=10975)
Annotation(end_index=11312, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEF39m7KP9GtguKPmQjHbDbwhHPDPTEyUc5nvrvsDKB1bGnqG--fW8LCCLqUt0UBsiu0GwMeT6FyECdXXTA0_p6P4leY-V5zcXmHY0fE0V0iydJswMwJqbkILvAJCpN_1T6YTNtUKkxLStrpl_9iNsSHCW5PmenTQm1Wb_4tFAweNuE1dcdK2aF6H1zmD845Yt69D1k', start_index=11298)
Annotation(end_index=11312, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEG-GH54seqoaDiGy8BIDw6jmOWWfzetpO0e7WV3tELKhzLTKPYk7dT3kc1HicD0KN88BjKaY4sBN25GAo09lqueWX6yVU6aoLfYbK8D3kmSj0dIhiCOIYDnNjxO_kya9_-qnsW9_guzgZmIetV0TyXJ5vLmJFcUzfwa7ZzUOFlw0ZScrN4MYxP1eXjKxmQvtr_Lk4x598-NIg07R4OT3nHjkbETrcmGPsyNqyEx6GW-RByxNi_gWI0IQ==', start_index=11298)
Annotation(end_index=11620, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo12g-Y3F1Kxx8EAoWiRnYRaDjXPAhzCyPM1y6VZwhC3YhiHR23P0yGgmXCf5jYbe1PP4uUsiJldT5FWbaqYAh48xw1uY1U6hvk_m0P3U00zHR1q5imZH4S590VCxPVc7EJwEnmHh6m-LDzp0zOFh1vmDemy34iZi-7aGY_zYMAZP7Fqt9v4JwS1JsRTtbKBk=', start_index=11610)
Annotation(end_index=11909, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBorCYnTwi3uIsQIKuTRf5QkCu33bxPViChqodYtD7QsLzdhp4H4YcXAtq_anCC1bopAwpBvnPDHQemV8ebO_-HDl7Jczo1Jqpyz1lHRjvzqMIBxcWU2P4_oSafxhgPHNQcAXiiS0=', start_index=11896)
Annotation(end_index=11909, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEx14jDHrJr0SW3Ykpf_fLhXOjxX_9iQFWXFs4BUJiGQKaYNTJPmal8std4SWxhM24YDg7jQkcuIiHjwPPILr0qnCueZU-iPOJSDYbc361TzivjWki4U1HeRjjUYlLF90otewGb-Cf', start_index=11896)
Annotation(end_index=12533, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEx14jDHrJr0SW3Ykpf_fLhXOjxX_9iQFWXFs4BUJiGQKaYNTJPmal8std4SWxhM24YDg7jQkcuIiHjwPPILr0qnCueZU-iPOJSDYbc361TzivjWki4U1HeRjjUYlLF90otewGb-Cf', start_index=12520)
Annotation(end_index=12533, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9wdeY3DXqp30mRmfhJ9RHUXKdM1e7qHCj3Gqkgizv-Z7Xj9n2Qz1Ernx7VGD1RE6LIxdPbdGUoZzYee_NYKLY8S13bkTSIrYajgfiP2r0ojqTGG0mUS5XNiVOOVZMxNK3W6t0eWDvO20hE18621dunw==', start_index=12520)
Annotation(end_index=12875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETavixQUWRkMicMdsXQf9hUzR7gYcc8EAPrmxtCCPvJiYqquWActEHZQD7l2Ts1MYVr1I50mzTMHvRAM5cVMF5qA2mKvRsC-cz4HvjJGhaOaskSl78fhORAJglZMgEltDF33ZTMrNCoE4CjEoMU23CZivotQ==', start_index=12857)
Annotation(end_index=12875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFq-3Vxno3S3xy7Eb4u-Ky68B2jP37Ieyc1c-miOes7kvD0_9LSaSKrtH_NTFolW7tQshLCv6BS0lZaLq-kvQcCZzSgjauci-ScsbOa778J2ZHx4Avoin1sFBpUwP3_koWDMKc5sXEo5EvQz1YxM8A8E94kig==', start_index=12857)
Annotation(end_index=12875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUP2APs4ygxDvWLROw9_XA3ZCvU08HJHyKMZnu6dp78tLmzvSI5irOlBBtMyRmsn_mrq9ItPZCOPzrr2z1uE2HIluR4HCOD9yrhGpjnwKwFQo0mYrrLljkhSQ8KxJjrbDVwDlrGkn8c1JSMrtVySIpeqfRRJqfbBK7', start_index=12857)
Annotation(end_index=13114, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLq0kgShC6DiRLrXzxM22OMl0WRN_0HtPTlfjXBn6P34P6iLJxCl9QmpgXgbrw5_uftPdm3pARy0Zrxr2veeGOkxzu2JVM_ceGGbddqnA9t3gc0Fz46YEt72oUDV860MZtyYoq14Rk_cINtvBiA2kuLEdYtSc=', start_index=13104)
Annotation(end_index=13442, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGH09f_jMT1PHxPx0FmskOz7U_dlJyKxtfYWUcqJM_1zhN4D_Sb789tPQ3RBw4Iy7dMHHGN6SISg9M_NnyKp6mHZnQdT4q8LEVQ58ZclGA8608BDgMhoBEk4u1mK-J5jC1ZcLgFXykPJ3fz45wSwh29hhFziY9oCA==', start_index=13432)
Annotation(end_index=14014, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLq0kgShC6DiRLrXzxM22OMl0WRN_0HtPTlfjXBn6P34P6iLJxCl9QmpgXgbrw5_uftPdm3pARy0Zrxr2veeGOkxzu2JVM_ceGGbddqnA9t3gc0Fz46YEt72oUDV860MZtyYoq14Rk_cINtvBiA2kuLEdYtSc=', start_index=14004)
Annotation(end_index=14448, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLq0kgShC6DiRLrXzxM22OMl0WRN_0HtPTlfjXBn6P34P6iLJxCl9QmpgXgbrw5_uftPdm3pARy0Zrxr2veeGOkxzu2JVM_ceGGbddqnA9t3gc0Fz46YEt72oUDV860MZtyYoq14Rk_cINtvBiA2kuLEdYtSc=', start_index=14438)
Annotation(end_index=14684, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfR4Fo00VOAH67pEZJtUPdSLVc_tkgfnIeYfcYMbaVhq9Ub4RJuy_qZP3HY6FuFom4YztKhTrEUF4zl6igbWN8gF5KQ8mfQReAUP1Eofk6kzb968XJjox0rClgT8WBg0ZHEv_imWuewOXwgfUFVIfl', start_index=14674)
Annotation(end_index=15200, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfR4Fo00VOAH67pEZJtUPdSLVc_tkgfnIeYfcYMbaVhq9Ub4RJuy_qZP3HY6FuFom4YztKhTrEUF4zl6igbWN8gF5KQ8mfQReAUP1Eofk6kzb968XJjox0rClgT8WBg0ZHEv_imWuewOXwgfUFVIfl', start_index=15186)
Annotation(end_index=15200, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGc0ubSY_R2j5ZzAqyHY_DeJrwT9xIbFIgBQEwN3Ses4yi_YuK7gPNZtjDlPRBp-eLH1ZAM8_EwXXSxKT9K16XIZR1_z_t3FUCxZi1WH3jlHeyB7RQbIUcsbsCTwsxzTq-B4bDRgJbALyITt4B1vysxg6T0aM-TUczV', start_index=15186)
Annotation(end_index=15510, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeHAx2h-e9wSZwCA-8W5Q7CJbGkk5ej2IEPW_Vc_vmF8obcV5s68TS8KNYVNrSTImq6PIZDjQb6_057SdObjBmcWXGHMirtHwIhw0b3iCbNRIhEfy6Nz_sCCNWS3RC_vNtBEBoYvfeuQkqhFW0jX8YUfM_lmltX41wyfMUwOqZQiA31F-VaPfWa0fQeG3UqFpApctH2GgsHLzzeQm2mlIbwY4D40eIQg==', start_index=15496)
Annotation(end_index=15510, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdaSsZ4hJSeprok4MggCb6DQqTEmeSk6JhNmE-bYAQtnJRylwCNfYbZGKy2HNYiz5f2qze7Kao1lbVZMz8SINlkVlguQVB-jmFCbIsrNp9Dm3IKdkbmg==', start_index=15496)
Annotation(end_index=16942, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUP2APs4ygxDvWLROw9_XA3ZCvU08HJHyKMZnu6dp78tLmzvSI5irOlBBtMyRmsn_mrq9ItPZCOPzrr2z1uE2HIluR4HCOD9yrhGpjnwKwFQo0mYrrLljkhSQ8KxJjrbDVwDlrGkn8c1JSMrtVySIpeqfRRJqfbBK7', start_index=16932)
Annotation(end_index=17017, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEx14jDHrJr0SW3Ykpf_fLhXOjxX_9iQFWXFs4BUJiGQKaYNTJPmal8std4SWxhM24YDg7jQkcuIiHjwPPILr0qnCueZU-iPOJSDYbc361TzivjWki4U1HeRjjUYlLF90otewGb-Cf', start_index=17008)
Annotation(end_index=17088, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9wdeY3DXqp30mRmfhJ9RHUXKdM1e7qHCj3Gqkgizv-Z7Xj9n2Qz1Ernx7VGD1RE6LIxdPbdGUoZzYee_NYKLY8S13bkTSIrYajgfiP2r0ojqTGG0mUS5XNiVOOVZMxNK3W6t0eWDvO20hE18621dunw==', start_index=17078)
Annotation(end_index=17149, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBcB98kqMFyczWbA5oxt_mTbQ-1vYU5RnfRCfo4U_SsGDJD0qbqmT_J264fHuREAyP_SBgF88YPuQeoDGfBGZoO89f1gmxSV_UAno4DT9TgjRaaINjSvezi3FMDwbMvjxuB2T9KRBLol2mopjKD1vqqvCAEg==', start_index=17139)
Annotation(end_index=17246, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBorCYnTwi3uIsQIKuTRf5QkCu33bxPViChqodYtD7QsLzdhp4H4YcXAtq_anCC1bopAwpBvnPDHQemV8ebO_-HDl7Jczo1Jqpyz1lHRjvzqMIBxcWU2P4_oSafxhgPHNQcAXiiS0=', start_index=17236)
Annotation(end_index=17300, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErCTyKNLgiuNYOoj_O8Ky4y98JWrteQiAvn82eh5rFXpxOx8YGArcS5AWpzLPcumA2LAzWlJwPaYE8m1Yc5HbNCQgYeQTGYNdph4BRTLbTmiuE_nquwKeWyPNahMo0pjWWyd6oukMYUg10AC3-0iwI_oVf0tcSemUY3M7nkrzUyGKU3n4=', start_index=17291)
Annotation(end_index=17354, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwYKzSGe1yPwRW08izXl4xMw5mCb6Q1eRdlWBnf1uAE5TopkLTwLnaFDTHXlpZl7jfPkg1opNl820vjeXQitCY9DVyiDHavq0MHxg55ExTJOgEQVi5tfKprtx97CYJjtzmpnolDGCtt2mKT9NEylN0ishB9OE=', start_index=17344)
Annotation(end_index=17403, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnA5njGuoCCUzGsQS98rqgoip4DnwFDQlIe3JjNdYHoSXjKi3UdF2tCZGjm3ZdSb1fJfByskOAJvV1_9YH7NIrqbCOYN7I8hNkEzDYdTDRVdTO5UjTyNRG16AomjU7C99vmvr1CL8=', start_index=17394)
Annotation(end_index=17453, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHsbKJw0QgEDoAuyIAbRaJbEu7dzUdoYkvDJbyO2bYs-etWG4FvTwg3tgIkV7mWzBDqtZ6VX8pDE6iW6WbKrxsZ06MBF179zUDdDvRpPyC1K9HkDhQnsqf2YmJI0GnwbS3PN7T3-q3WwI_9K3E-0Jfsz4TPRLy-fJ0ajCba6sGasvrAjC-RgfRhA==', start_index=17443)
Annotation(end_index=17515, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErLC55ybdKQ8rzt1EtP9d8-ECSrjwWXcU3xOhJDG8kx_ugjJoLHEpalGdxGEsAXSwRsIe0p_92xfqfx2TVlotCiuhY5wZZJ0uw9g7VThm8nGBYl519', start_index=17505)
Annotation(end_index=17575, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETavixQUWRkMicMdsXQf9hUzR7gYcc8EAPrmxtCCPvJiYqquWActEHZQD7l2Ts1MYVr1I50mzTMHvRAM5cVMF5qA2mKvRsC-cz4HvjJGhaOaskSl78fhORAJglZMgEltDF33ZTMrNCoE4CjEoMU23CZivotQ==', start_index=17565)
Annotation(end_index=17646, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4nLqCw2it-Jn6m6x5-0TVG6L_R7XCnHDCzD6Doe7S2ed45AcaRrYw5a38ztQuUUJsb8FXhZdIadtaEopjqzgtuPOBZvi3r188IeuajelQ3EHSagAGiJFI4BWmn49oTLo6ZFl8JQUBcPMvG4-ZSjoRTSmz9T8557kVlaa7k_4AdWAXXjVDYTPsiQ==', start_index=17636)
Annotation(end_index=17751, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaNXByPpEIj9IPLtcVpzxg9qYA6zjjkWU3pUn64yagU3kGyQMsz1ODT_KH3vUqG77yvVewnm9xtkuXTZBxfakUH_0OgzqNEdmjkjctNtID6QLpTLDBamhrN0wnx3jheD6n', start_index=17741)
Annotation(end_index=17839, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaEIJ0bEFqaj-Pbgg__zfuR4yv2O2oASb_dqmwkC_t8GlByapV25jnKXEjqZ13G3Go2aXqJnHDY3RXsCYRxJarFT6RYuSfZP3EWuGaUyCK1o8X1v3J3Pn1_QL5yfzFZTZb8covp9Q3taMabKomFy0oADAi', start_index=17829)
Annotation(end_index=17928, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL_JFns_Msch1sLtIx-XSCEOOexpFtEg_u6zkOrqe7NyqOFVHtFEHjvySoNqbNHjx45flI5yLmG4Yg5eaMh0sxUue08-vPv8BUQ3hCNNBwjiaExJphDrIDzOpiC5ychCVrnANRBEOQv8u1vYIV3t2jZYWFMA6pNHHgGc-W5RWXPk_l', start_index=17919)
Annotation(end_index=18033, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeHAx2h-e9wSZwCA-8W5Q7CJbGkk5ej2IEPW_Vc_vmF8obcV5s68TS8KNYVNrSTImq6PIZDjQb6_057SdObjBmcWXGHMirtHwIhw0b3iCbNRIhEfy6Nz_sCCNWS3RC_vNtBEBoYvfeuQkqhFW0jX8YUfM_lmltX41wyfMUwOqZQiA31F-VaPfWa0fQeG3UqFpApctH2GgsHLzzeQm2mlIbwY4D40eIQg==', start_index=18023)
Annotation(end_index=18101, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc_t-lTaZYdf1Bc3LEvACUeencRolo10rlQnvx4GpBe9itDXo3F_ZDTJZjIz5PX5hBIAjWQke25bSgcMq7QKvAqg_1o9UBt-XsuD5pa9RwvjtbosgNBtmELMm7npPqbUj-QKf7HHiR1tp1KIiDBG7EslvJN3ihZ0EZSA==', start_index=18092)
Annotation(end_index=18177, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdaSsZ4hJSeprok4MggCb6DQqTEmeSk6JhNmE-bYAQtnJRylwCNfYbZGKy2HNYiz5f2qze7Kao1lbVZMz8SINlkVlguQVB-jmFCbIsrNp9Dm3IKdkbmg==', start_index=18167)
Annotation(end_index=18238, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEG-GH54seqoaDiGy8BIDw6jmOWWfzetpO0e7WV3tELKhzLTKPYk7dT3kc1HicD0KN88BjKaY4sBN25GAo09lqueWX6yVU6aoLfYbK8D3kmSj0dIhiCOIYDnNjxO_kya9_-qnsW9_guzgZmIetV0TyXJ5vLmJFcUzfwa7ZzUOFlw0ZScrN4MYxP1eXjKxmQvtr_Lk4x598-NIg07R4OT3nHjkbETrcmGPsyNqyEx6GW-RByxNi_gWI0IQ==', start_index=18228)
Annotation(end_index=18321, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEF39m7KP9GtguKPmQjHbDbwhHPDPTEyUc5nvrvsDKB1bGnqG--fW8LCCLqUt0UBsiu0GwMeT6FyECdXXTA0_p6P4leY-V5zcXmHY0fE0V0iydJswMwJqbkILvAJCpN_1T6YTNtUKkxLStrpl_9iNsSHCW5PmenTQm1Wb_4tFAweNuE1dcdK2aF6H1zmD845Yt69D1k', start_index=18311)
Annotation(end_index=18386, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLq0kgShC6DiRLrXzxM22OMl0WRN_0HtPTlfjXBn6P34P6iLJxCl9QmpgXgbrw5_uftPdm3pARy0Zrxr2veeGOkxzu2JVM_ceGGbddqnA9t3gc0Fz46YEt72oUDV860MZtyYoq14Rk_cINtvBiA2kuLEdYtSc=', start_index=18376)
Annotation(end_index=18462, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo12g-Y3F1Kxx8EAoWiRnYRaDjXPAhzCyPM1y6VZwhC3YhiHR23P0yGgmXCf5jYbe1PP4uUsiJldT5FWbaqYAh48xw1uY1U6hvk_m0P3U00zHR1q5imZH4S590VCxPVc7EJwEnmHh6m-LDzp0zOFh1vmDemy34iZi-7aGY_zYMAZP7Fqt9v4JwS1JsRTtbKBk=', start_index=18452)
Annotation(end_index=18526, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc_t-lTaZYdf1Bc3LEvACUeencRolo10rlQnvx4GpBe9itDXo3F_ZDTJZjIz5PX5hBIAjWQke25bSgcMq7QKvAqg_1o9UBt-XsuD5pa9RwvjtbosgNBtmELMm7npPqbUj-QKf7HHiR1tp1KIiDBG7EslvJN3ihZ0EZSA==', start_index=18517)
Annotation(end_index=18603, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_USLBJO6vBTo_IZLWD0w071XURMbL_oeqjnB-WmTAZDZFxWpOzPEmNeMTyIrqdlakwCLN_YihLC-ayhhNov1afg4wOBkqq3iuku03O9326ypI9fcuA1kL9rGbSqeb4HhJx-ZIn4OWdEhEC9X9O0YzSVWWf-PC7K9SOezSMnW5dw==', start_index=18593)
Annotation(end_index=18675, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVyPOFI7yAKeJAtkFLDxDAuSyuVmsiGQlQ5I_ks9E2vImmdpdlNo3olWY_xYbEcBt8IWSU-NXvX4u1ADITOvXxEeHqiL3LCY8bLHCX_L7LwNP32JU5J4fe5P0PNQsmt2sySqjZ1JXoziB2OspuMVI4gYfJzYlTgkllKmxXq7GmmWCwNL4=', start_index=18665)
Annotation(end_index=18760, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMES1XgmuUJ_zfmL9F060Is4iUYIVZNT-6kbZ-zMUzCfA8Qi6JPRdNmages6tpdqhC0CpZmDYSnB7JLXiEyooAR5qHIpYqvLsFjd0b4Hoaskfkb5tPiw==', start_index=18750)
Annotation(end_index=18828, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG849gIJNH-beMEPtzVLfWpk1MAoPiX3fGD4Qchj9zUoTWH32CWMK8BKERZlCGmucnZMfd4r_SGTOhAR7yHqJzM85verxXI_2LB9MEwJVeNYH2BBTjIRQjZLdpAYtwI8upZn2LdxcsrVwwMkpPZTmAvVBE=', start_index=18819)
Annotation(end_index=18923, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH96flsV1QpPsPssvdeYxkYFLiqPiTsumydsmYRggp1h47H1l6MQluHJ7bqtfKAJ0CYnE_l9AKmklJ0gK_NlyKirnOnFC-ZrRYprZdQsoIrbcxcfI4Y-B9MM0YaEoUA8_PvF-DZZX3LzaEGnSFR5IdMa9SHGEW80eF7sdYjuoaANEUdtb7_WYMtmvWMZvM=', start_index=18913)
Annotation(end_index=19000, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9wdeY3DXqp30mRmfhJ9RHUXKdM1e7qHCj3Gqkgizv-Z7Xj9n2Qz1Ernx7VGD1RE6LIxdPbdGUoZzYee_NYKLY8S13bkTSIrYajgfiP2r0ojqTGG0mUS5XNiVOOVZMxNK3W6t0eWDvO20hE18621dunw==', start_index=18990)
Annotation(end_index=19069, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGS1lvdadxum5iMhmJYrHsKBYeqDb0VImpdWaj_EQxL7chChFnNPGcoqdc3z1XLRHJ41pzyrqPPKA1q7Wb9dj1sx54N2FCueGosrXtzb1bj82Fa7BHElCt7moAvJolpyUxzjzXL5wnIKayxoPwjAKiRP1TbIFKiZ4pML-pe6KjeQEzupeafx1hh2CX3Y6IZnn8yXo56Mc_Dk6vdi_O8uR8PMA=', start_index=19059)
Annotation(end_index=19128, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFq-3Vxno3S3xy7Eb4u-Ky68B2jP37Ieyc1c-miOes7kvD0_9LSaSKrtH_NTFolW7tQshLCv6BS0lZaLq-kvQcCZzSgjauci-ScsbOa778J2ZHx4Avoin1sFBpUwP3_koWDMKc5sXEo5EvQz1YxM8A8E94kig==', start_index=19118)
Annotation(end_index=19193, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9gLa0HHdUTVzccMX_D5wOADL_YddI0C-qz3Ea6c7z880frdpmBDAL8Ldvy7T-Czo4XnfYMmSnYWNONhLL1nXXyf_T9e8zYdwzU9kA0nm9iCDYE7A5US_v9pokVWvE50L9pFdF0f2CCRkUp0xqRXAf5A==', start_index=19183)
Annotation(end_index=19264, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzRo38YvC5h_JU-yiUMsq5-ZHchou1OXUUPMRKE6ha_ABW5lefJqQ4iAIxO6Lu0j3VOPQtq8eohL6skXkj1Jo-LeqNip_2dBcWuesf4xhrJ90aJ8YJCKGOBzHDIs0YrqNJHoMkPO6HSjRg9V6mabV-y_81', start_index=19255)
Annotation(end_index=19325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFgRWW3WsBBHct54Pw87rBwbzy7ipJz2aehBXfHfQimJBtRdPzzAnRZwmQhmJuQ-abithF4vyPkJ2_hltbLtD_OkgSKPcVK02yaqnb5VN-y_Eaf0atp-0MKuA_JzF9MrljqBlYL95HkqbyXqfWnuvskQRBTYrEaNMR0OyaPI_sTIGgg8WS6mNbkcorLY9TjYz-OBCeIyg_Kko=', start_index=19316)
Annotation(end_index=19379, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFviRNUn3j4ZxHzdTZW0pjcIHnBmk3t_8EOm6xG9qUDO1JXSVwAYP96cER0dXMJNsIOdS0qORlt6BA4_diCTti73-8AEds8X1E3ERtu7RJGggmG6aAJOFiM7XFbqQ6BfnupSOcnIJYkmaPZ8GkWC0JB8XmJfWr7xnPeDl-b64X8hsR3hHrwWGdraobZcs3yvSWTgtzkSYfEHM5_9vvGENRfAJry_pxXNysPzbFP5jo8bqqL5oAifVEXtstaGsaDKTK3zxHv', start_index=19369)
Annotation(end_index=19446, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuDmWwpRtt3EfqRSF5mEje9b45u7VH6V6fDCFaRS_CJuLDFdJl1hODWrMc15l2tW20F3TdLNVyI8yq7_AdqH7TafUpwK-Inc4AZwKUrAmkEDi9L4WWBRXe_XzSScqhNImoCq-6qjw5Wsk5GBhPRg==', start_index=19436)
Annotation(end_index=19526, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEF39m7KP9GtguKPmQjHbDbwhHPDPTEyUc5nvrvsDKB1bGnqG--fW8LCCLqUt0UBsiu0GwMeT6FyECdXXTA0_p6P4leY-V5zcXmHY0fE0V0iydJswMwJqbkILvAJCpN_1T6YTNtUKkxLStrpl_9iNsSHCW5PmenTQm1Wb_4tFAweNuE1dcdK2aF6H1zmD845Yt69D1k', start_index=19516)
Annotation(end_index=19590, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo12g-Y3F1Kxx8EAoWiRnYRaDjXPAhzCyPM1y6VZwhC3YhiHR23P0yGgmXCf5jYbe1PP4uUsiJldT5FWbaqYAh48xw1uY1U6hvk_m0P3U00zHR1q5imZH4S590VCxPVc7EJwEnmHh6m-LDzp0zOFh1vmDemy34iZi-7aGY_zYMAZP7Fqt9v4JwS1JsRTtbKBk=', start_index=19580)
Annotation(end_index=19670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3nW0_dEm0joB9P9wYIpvN29Y3WG1w4ja7oQNSNhIb9ni7s534qJ6mc8K00BDMauLnxb9VvJWa7avqWZ-gaRuPSFsVSnIfYcNjVA7QYvYA2l1v_h9sh8O7aJgIpW4WKWE_w1pLrR3bBE30QL3FELPz8ASAsR7bDd0=', start_index=19660)
Annotation(end_index=19758, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKDsnYtlfbUR8FXYV-9xvp0LD3uNfFJt8CDhjzvsx0m20D2ceK3V5RpbC2c5PFK9TXcAtX_YS4O7YjVGm1h49yHdn_f7ErqNYDnNBFO_6E2iPqr1CKO7dczENeZMNZg7nmX7Se0lpMr_6Xu8tFDY4rhluAwwg_9moEiQ8dYbJ_yx9KL_mH9XPLwB1Bpgj_DCM03YnJsQGU7sx9Yjbbprs=', start_index=19748)
Annotation(end_index=19846, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwt2DwAnJyfsX71OVdcrx-Obu1gHUycTsYExkKMY1-xZbEPBfhgsseT4aWStQssyru1b1fyVDIaRNFlQSAOX3SGHORdcDfZOSM3PrAwh_lr1jwrMnxtYxgW_tl54iD4jGUdg==', start_index=19837)
Annotation(end_index=19920, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLq0kgShC6DiRLrXzxM22OMl0WRN_0HtPTlfjXBn6P34P6iLJxCl9QmpgXgbrw5_uftPdm3pARy0Zrxr2veeGOkxzu2JVM_ceGGbddqnA9t3gc0Fz46YEt72oUDV860MZtyYoq14Rk_cINtvBiA2kuLEdYtSc=', start_index=19910)
Annotation(end_index=19989, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGH09f_jMT1PHxPx0FmskOz7U_dlJyKxtfYWUcqJM_1zhN4D_Sb789tPQ3RBw4Iy7dMHHGN6SISg9M_NnyKp6mHZnQdT4q8LEVQ58ZclGA8608BDgMhoBEk4u1mK-J5jC1ZcLgFXykPJ3fz45wSwh29hhFziY9oCA==', start_index=19979)
Annotation(end_index=20064, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo9etwdq-pQ4gLK-D45IFRrFewkwrN3Tq75B8Jyf69y2pZ5RrdsVKkTJrJZM7mQn-vW6m2JuVmRtXa4TuL58QAmNq9lBPx657tUx87gQGx3cXeB0YkmpxSBU9VKkgwhOD0EynMtIwyZpBJnsL-luHhfSYdKA9uIaQH5_ZpoSylWIDizNNaoU-xTwruannJtuv_7CrHmZDFue0XqbU8PzQ=', start_index=20054)
Annotation(end_index=20139, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWjuaZIPpH3QOZEd1FpzEmgoXuoVnanomIFIBIobtJIaiKqkYKlPcVe-nFoQGOXNWsFTRUN42cFirBU1uqGxc8yIOIeJ4vSFLYe6CChQl-rkZOTcZEc74qEHviyJBiPVVrCM_mFrYbYgqL', start_index=20129)
Annotation(end_index=20228, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfR4Fo00VOAH67pEZJtUPdSLVc_tkgfnIeYfcYMbaVhq9Ub4RJuy_qZP3HY6FuFom4YztKhTrEUF4zl6igbWN8gF5KQ8mfQReAUP1Eofk6kzb968XJjox0rClgT8WBg0ZHEv_imWuewOXwgfUFVIfl', start_index=20218)
Annotation(end_index=20318, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGc0ubSY_R2j5ZzAqyHY_DeJrwT9xIbFIgBQEwN3Ses4yi_YuK7gPNZtjDlPRBp-eLH1ZAM8_EwXXSxKT9K16XIZR1_z_t3FUCxZi1WH3jlHeyB7RQbIUcsbsCTwsxzTq-B4bDRgJbALyITt4B1vysxg6T0aM-TUczV', start_index=20308)
Annotation(end_index=20392, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJzhWqEoap1kD-HTBg9rzUGCi-oVwr5F_47Z66JXBic_j3X4XLT-UKcoso9LUBm11Um6WJ9AbF7KoM03Ug8Gk475volVPTUPnrP9RS4LtY4NxiND8_UOS6TKF5SY5EKS7a_lJ3mRO4MY1oIKpxtVyRGnFXcjn_66NRypxBsJqv8KLZIzBZ77TDK4IZN6v2TYufvxA0ZoHRMq8brpPewB3ewhuhEDMqPl92xOVyq7eMzs6IpbbslvcCT7DgvGcbsMHj_uyj97mLVcqFZZjFQ9c=', start_index=20382)
Annotation(end_index=20471, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYPvJM-9fYto7f_qiKkReOwIxVfhJUWf1mZwJBUbsXWAmAkioMLjIXrYwoEkREYhGZRZDIeNBsZpgHAYJytQWIb4yvPl9GzKebdjPcP1xXA-OO6Jz9XTTUDy4teSVs1qDxCrDCw2GT', start_index=20461)

## Sources
