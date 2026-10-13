# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 6cab1135 | **Time:** 179.05s | **Cost:** $0.11847
--------------------------------------------------------------------------------

# How Does the Characteristic Polynomial of Intergenerational Transfer Matrices Determine the Lyapunov Stability of Welfare Systems?

## Abstract

This research report examines the mathematical relationship between the characteristic polynomial of intergenerational transfer matrices and the Lyapunov stability of welfare systems. By synthesizing established results from control theory, stability analysis, and intergenerational welfare economics, we develop a comprehensive framework for understanding how the spectral properties of transfer matrices determine the long-term behavior and stability of social welfare systems. The analysis reveals that the roots of the characteristic polynomial—specifically the eigenvalues of the transfer matrix—provide fundamental insights into whether welfare systems exhibit convergent, persistent, or divergent dynamics across generations. We demonstrate that Lyapunov stability criteria, traditionally applied to dynamical systems, offer powerful analytical tools for evaluating the robustness and sustainability of intergenerational welfare transfers, with significant implications for policy design and social economic planning.

## 1. Introduction

The stability of welfare systems across generations represents one of the most consequential challenges in contemporary social economics. As populations age and demographic structures shift, understanding whether existing welfare arrangements can maintain their functional integrity over extended time horizons becomes paramount. The mathematical sciences offer sophisticated tools for analyzing such complex, dynamic systems, drawing upon established theories of stability that have proven invaluable in engineering and physical sciences [1].

Intergenerational welfare transfers constitute a fundamental mechanism through which societies redistribute resources across age cohorts. These transfers encompass both private transfers—such as parental investments in children's human capital and financial assistance—and public transfers through social security systems and welfare programs [2]. The dynamics of these transfers create complex feedback loops where current recipients may become future contributors, and vice versa, establishing intricate interdependencies that determine system-wide behavior.

The mathematical representation of these intergenerational dynamics naturally leads to the concept of transfer matrices—mathematical constructs that capture the relationships between successive generations' welfare states. The characteristic polynomial of such a matrix encodes critical information about the system's long-term behavior, much as it does in the analysis of linear time-invariant dynamical systems [3]. Understanding this connection provides researchers and policymakers with powerful analytical capabilities for predicting system responses to perturbations and designing more robust welfare architectures.

This report proceeds as follows: Section 2 establishes the mathematical foundations of intergenerational transfer matrices and their characteristic polynomials. Section 3 introduces Lyapunov stability theory and its application to welfare system analysis. Section 4 develops the central theoretical framework connecting characteristic polynomial properties to stability outcomes. Section 5 discusses implications for welfare system design and policy applications. Section 6 concludes with directions for future research.

## 2. Mathematical Foundations of Intergenerational Transfer Matrices

### 2.1 Definition and Structure of Transfer Matrices

An intergenerational transfer matrix provides a mathematical representation of the relationships between welfare states across successive generations. Consider a welfare system characterized by $n$ distinct states or categories—such as income quintiles, welfare receipt status, or socioeconomic classifications. Let $x^{(t)} \in \mathbb{R}^n$ denote the distribution of welfare states in generation $t$, where each component $x_i^{(t)}$ represents the proportion of individuals in state $i$ at time $t$.

The intergenerational transfer dynamics can be expressed through a linear transformation:

$$x^{(t+1)} = A x^{(t)}$$

where $A \in \mathbb{R}^{n \times n}$ is the intergenerational transfer matrix. The entry $a_{ij}$ of matrix $A$ represents the probability or proportion of individuals transitioning from welfare state $j$ in generation $t$ to state $i$ in generation $t+1$. This formulation assumes Markovian dynamics, where the transition probabilities depend only on the current state rather than the complete history of previous states [4].

The transfer matrix $A$ must satisfy certain structural properties to be physically meaningful. Specifically, all entries must be non-negative:

$$a_{ij} \geq 0 \quad \forall i,j$$

and the columns must sum to unity, reflecting the conservation of population:

$$\sum_{i=1}^{n} a_{ij} = 1 \quad \forall j$$

These properties classify $A$ as a stochastic matrix, with profound implications for its spectral characteristics.

### 2.2 The Characteristic Polynomial

The characteristic polynomial of the transfer matrix $A$ is defined as:

$$p_A(\lambda) = \det(\lambda I - A)$$

where $I$ denotes the $n \times n$ identity matrix and $\det(\cdot)$ represents the determinant operation [5]. This polynomial is of degree $n$ and can be expressed in the form:

$$p_A(\lambda) = \lambda^n + a_{n-1}\lambda^{n-1} + \cdots + a_1\lambda + a_0$$

The coefficients $a_k$ are determined by the entries of $A$ and encode important structural information about the transfer dynamics. According to the Cayley-Hamilton theorem, every matrix satisfies its own characteristic equation:

$$p_A(A) = A^n + a_{n-1}A^{n-1} + \cdots + a_1A + a_0I = 0$$

The roots of the characteristic polynomial—the eigenvalues of $A$—determine the system's dynamic behavior. If $\lambda_1, \lambda_2, \ldots, \lambda_n$ denote the eigenvalues, then:

$$p_A(\lambda) = (\lambda - \lambda_1)(\lambda - \lambda_2)\cdots(\lambda - \lambda_n)$$

For stochastic matrices, several spectral properties hold with certainty. The Perron-Frobenius theorem guarantees the existence of a real, positive eigenvalue $\lambda_1 = 1$, which corresponds to the stationary distribution of the Markov chain [6]. The remaining eigenvalues satisfy $|\lambda_k| \leq 1$ for $k = 2, \ldots, n$.

### 2.3 Spectral Properties and System Dynamics

The spectral radius of the transfer matrix, defined as $\rho(A) = \max\{|\lambda_i|\}$, determines the asymptotic growth rate of system states. When $\rho(A) < 1$, the system exhibits geometric decay toward the zero state, indicating that welfare advantages or disadvantages diminish across generations. Conversely, when $\rho(A) > 1$, the system exhibits explosive growth, suggesting that initial disparities amplify over time.

The eigenvalues and their multiplicities reveal critical information about the system's dynamic modes. Complex conjugate eigenvalues indicate oscillatory behavior in the transition dynamics, while repeated eigenvalues suggest the presence of generalized eigenvectors that govern the approach to steady-state behavior. The spectral gap—defined as $1 - |\lambda_2|$, where $\lambda_2$ is the eigenvalue with second-largest magnitude—determines the rate of convergence to the stationary distribution [7].

## 3. Lyapunov Stability Theory and Its Application to Welfare Systems

### 3.1 Fundamentals of Lyapunov Stability

Lyapunov stability theory provides a rigorous framework for analyzing the asymptotic behavior of dynamical systems without explicitly solving the system equations [8]. Originally developed for mechanical systems, this theory has found widespread application in control theory, economics, and social sciences for analyzing system resilience and convergence properties.

Consider a general dynamical system described by:

$$\dot{x}(t) = f(x(t))$$

where $x(t) \in \mathbb{R}^n$ represents the system state at time $t$ and $f: \mathbb{R}^n \rightarrow \mathbb{R}^n$ is a continuously differentiable vector field. An equilibrium point $x_e$ satisfies $f(x_e) = 0$. The equilibrium is stable in the sense of Lyapunov if, for every $\epsilon > 0$, there exists $\delta > 0$ such that:

$$\|x(0) - x_e\| < \delta \implies \|x(t) - x_e\| < \epsilon \quad \forall t \geq 0$$

The equilibrium is asymptotically stable if it is stable in the sense of Lyapunov and attracts all trajectories originating sufficiently close to $x_e$ [9]. For linear time-invariant systems of the form $\dot{x}(t) = Ax(t)$, asymptotic stability is equivalent to all eigenvalues of $A$ having negative real parts.

### 3.2 Lyapunov Functions and Stability Criteria

A Lyapunov function $V(x)$ is a scalar-valued function that serves as a generalized energy measure for the system. For asymptotic stability, $V(x)$ must satisfy:

1. $V(x)$ is positive definite: $V(x) > 0$ for $x \neq 0$ and $V(0) = 0$
2. The time derivative along system trajectories is negative definite: $\dot{V}(x) < 0$ for $x \neq 0$

The existence of such a function guarantees asymptotic stability of the equilibrium at the origin [10]. For linear systems $\dot{x} = Ax$, a quadratic Lyapunov function $V(x) = x^T P x$ with $P = P^T > 0$ exists if and only if the system is asymptotically stable. In this case, $P$ satisfies the Lyapunov equation:

$$A^T P + PA = -Q$$

where $Q = Q^T > 0$ is any positive definite matrix [11].

### 3.3 Application to Welfare System Analysis

To apply Lyapunov stability concepts to welfare systems, we must establish an appropriate equilibrium concept and construct a suitable Lyapunov function. The natural equilibrium corresponds to the stationary distribution of the intergenerational transfer process—the distribution toward which the system converges in the absence of external perturbations.

Consider the discrete-time dynamics $x^{(t+1)} = Ax^{(t)}$. The stationary distribution $x^*$ satisfies $x^* = Ax^*$, or equivalently $(I - A)x^* = 0$. The null space of $(I - A)$ contains the stationary distribution, which exists and is unique for irreducible, aperiodic stochastic matrices.

To analyze stability, we examine perturbations from the stationary distribution. Define the deviation $\delta x^{(t)} = x^{(t)} - x^*$. The dynamics of this deviation are:

$$\delta x^{(t+1)} = A \delta x^{(t)}$$

The system is Lyapunov stable if perturbations remain bounded, and asymptotically stable if perturbations decay to zero. These conditions depend entirely on the spectral properties of $A$, which are encoded in its characteristic polynomial.

## 4. Characteristic Polynomial Properties and Stability Determination

### 4.1 Eigenvalue Conditions for Stability

The relationship between the characteristic polynomial and Lyapunov stability follows directly from spectral analysis. For the discrete-time system $x^{(t+1)} = Ax^{(t)}$, asymptotic stability requires that all eigenvalues satisfy $|\lambda_i| < 1$ [12]. This condition ensures that perturbations from equilibrium decay geometrically over time.

The characteristic polynomial $p_A(\lambda) = \det(\lambda I - A)$ provides complete information about eigenvalue locations. The Routh-Hurwitz stability criterion offers a method for determining whether all roots of a polynomial lie within the unit circle without explicitly computing the roots [13]. For a polynomial:

$$p(\lambda) = \lambda^n + a_{n-1}\lambda^{n-1} + \cdots + a_1\lambda + a_0$$

the Routh-Hurwitz criterion provides necessary and sufficient conditions on the coefficients $a_k$ for stability.

For second-order systems, the conditions are straightforward. If $p(\lambda) = \lambda^2 + a_1\lambda + a_0$, asymptotic stability requires:

$$|a_0| < 1 \quad \text{and} \quad |a_1| < 1 + a_0$$

For higher-order systems, the Routh array construction provides a systematic procedure for stability assessment. The number of sign changes in the first column of the Routh array equals the number of roots with positive real part for continuous-time systems, or the number of roots outside the unit circle for discrete-time systems [14].

### 4.2 Spectral Radius and Convergence Rates

The spectral radius $\rho(A)$ provides a comprehensive measure of system stability. For stochastic matrices, $\rho(A) = 1$ always, but the magnitude of the second-largest eigenvalue $\lambda_2$ determines the convergence rate. The mixing time of the Markov chain—defined as the time required for the distribution to approach within $\epsilon$ of the stationary distribution—is approximately proportional to $1/|\ln|\lambda_2||$ [15].

The characteristic polynomial coefficients relate to elementary symmetric functions of the eigenvalues:

$$\sum_{i=1}^n \lambda_i = -a_{n-1}$$
$$\sum_{1 \leq i < j \leq n} \lambda_i \lambda_j = a_{n-2}$$
$$\prod_{i=1}^n \lambda_i = (-1)^n a_0$$

These Vieta relations provide constraints on possible eigenvalue configurations and can be used to derive stability conditions directly from matrix entries.

### 4.3 Robustness and Margin of Stability

Beyond binary stability classification, the characteristic polynomial provides information about the robustness of stable configurations. The distance to instability can be measured by the smallest perturbation required to move an eigenvalue outside the stability region. For discrete-time systems, this corresponds to the minimum distance from any eigenvalue to the unit circle [16].

The Lyapunov equation $A^T P + PA = -Q$ provides an alternative perspective on stability margins. The solution $P$ serves as a Lyapunov matrix, and its condition number provides a measure of robustness. If $P$ is well-conditioned (all eigenvalues of $P$ are comparable in magnitude), the system exhibits good stability margins. Conversely, ill-conditioned $P$ indicates fragility—small perturbations may destabilize the system [17].

### 4.4 Interpreting Characteristic Polynomial Coefficients in Welfare Context

The coefficients of the characteristic polynomial carry direct interpretations in the context of intergenerational welfare transfers. The coefficient $a_{n-1} = -\text{tr}(A)$ relates to the total transition rates out of each state. Large negative values (corresponding to large trace) indicate rapid transitions, potentially suggesting high mobility but also potential instability.

The constant term $a_0 = (-1)^n \det(A)$ relates to the product of eigenvalues. For stochastic matrices, $\det(A)$ can range from 0 to 1, with higher values indicating less mobility and greater persistence of initial conditions. A determinant near zero suggests the presence of near-zero eigenvalues, indicating slow modes in the system dynamics that may require extended time horizons for convergence.

Intermediate coefficients capture higher-order interaction effects between states. For example, in a three-state system, the coefficient of $\lambda$ captures pairwise transition interactions that may indicate indirect pathways between welfare states.

## 5. Implications for Welfare System Design and Policy

### 5.1 Designing for Stability

The mathematical framework developed above provides guidance for designing welfare systems with desired stability properties. If the goal is to reduce intergenerational persistence of poverty or welfare dependence, policy interventions should target the spectral properties of the transfer matrix. Specifically, policies should aim to reduce the magnitude of subdominant eigenvalues, thereby increasing the spectral gap and accelerating convergence toward desired stationary distributions.

Consider a welfare system characterized by two states: welfare receipt and self-sufficiency. The transfer matrix takes the form:

$$A = \begin{pmatrix} p_{11} & p_{12} \\ p_{21} & p_{22} \end{pmatrix}$$

where $p_{ij}$ denotes the probability of transitioning from state $j$ to state $i$. The characteristic polynomial is:

$$p_A(\lambda) = \lambda^2 - (p_{11} + p_{22})\lambda + (p_{11}p_{22} - p_{12}p_{21})$$

Stability requires $|\lambda_i| < 1$, which for this $2 \times 2$ case simplifies to $|p_{11} + p_{22}| < 2$ and $|p_{11}p_{22} - p_{12}p_{21}| < 1$. These conditions are typically satisfied for valid stochastic matrices, but the rate of convergence depends on the specific values.

To promote upward mobility, policy should increase $p_{21}$ (transitions from welfare to self-sufficiency) and decrease $p_{11}$ (persistence in welfare receipt). This shifts eigenvalues toward zero, accelerating convergence to the stationary distribution where welfare receipt reaches its long-run equilibrium level.

### 5.2 Managing Systemic Risk

The Lyapunov stability framework illuminates how welfare systems respond to perturbations. Asymmetric shocks—such as economic recessions, demographic transitions, or policy changes—can be analyzed as perturbations to the transfer matrix. The system's response depends on its proximity to instability boundaries.

Systems with eigenvalues clustered near the unit circle exhibit slow response to perturbations and may require extended adjustment periods. Such systems are also more vulnerable to stochastic shocks that could push eigenvalues outside the stability region. The Routh-Hurwitz criterion provides a systematic method for assessing vulnerability: coefficients near stability boundaries indicate fragile configurations [18].

The concept of intergenerational risk sharing, wherein welfare systems pool risks across generations, can be analyzed through this framework. Social security systems that effectively share risks exhibit transfer matrices with favorable spectral properties—specifically, eigenvalues that remain bounded away from unity in magnitude, ensuring rapid absorption of idiosyncratic shocks [19].

### 5.3 Policy Evaluation and Monitoring

The characteristic polynomial approach provides quantitative metrics for evaluating welfare policy interventions. By estimating transfer matrices before and after policy changes, researchers can compute the resulting changes in spectral properties and assess whether interventions move the system toward or away from desired stability configurations.

Longitudinal data on intergenerational welfare transmission enable empirical estimation of transfer matrices. Studies using data from the Health and Retirement Study (HRS) and other panel datasets have documented substantial intergenerational correlations in welfare receipt, suggesting transfer matrices with eigenvalues near unity and correspondingly slow convergence [20]. These findings indicate that without policy intervention, welfare states may persist across generations for extended periods.

The mathematical framework also supports scenario analysis for policy planning. By constructing alternative transfer matrices representing different policy scenarios, policymakers can predict the long-term consequences of current decisions and identify interventions that optimize stability properties.

## 6. Extensions and Future Research Directions

### 6.1 Nonlinear and Time-Varying Dynamics

The analysis presented here assumes linear, time-invariant dynamics. Real welfare systems exhibit nonlinearities arising from behavioral responses, policy thresholds, and interaction effects. Extending the framework to nonlinear dynamics would require generalizing Lyapunov stability concepts to nonlinear systems, potentially using Lyapunov functions that are not quadratic in form.

Time-varying transfer matrices—reflecting changing demographic structures, evolving policy regimes, and shifting economic conditions—require more sophisticated analytical tools. The concept of uniform asymptotic stability, which requires exponential convergence uniformly over all time, becomes relevant for such systems [21]. Characteristic polynomial analysis extends naturally through the concept of parametric stability, wherein polynomial coefficients vary with time.

### 6.2 Multi-Dimensional Welfare Assessment

The framework can be extended to multi-dimensional welfare assessment, where individuals are characterized by multiple attributes simultaneously—such as income, health status, education level, and wealth. This leads to tensor-valued transfer operators rather than matrix-valued ones, with correspondingly more complex spectral theory.

High-dimensional welfare dynamics may exhibit emergent behaviors not captured by reduced-dimensional analyses. The interaction between different welfare dimensions can create coupling effects that either stabilize or destabilize the overall system. Understanding these interactions requires advances in multi-linear algebra and tensor decomposition methods.

### 6.3 Stochastic Perturbations and Rare Events

The deterministic framework presented here abstracts away from stochastic elements that play important roles in welfare dynamics. Random shocks to individual circumstances, stochastic policy changes, and unpredictable economic events introduce randomness that affects system trajectories.

Stochastic stability concepts—including almost sure stability and stability in probability—provide appropriate frameworks for analyzing such systems. The characteristic polynomial approach extends to stochastic systems through the concept of mean-square stability, which requires that the second moment of system states remains bounded [22].

Rare events, such as economic depressions or major policy reforms, may cause regime changes that cannot be captured by linear perturbation analysis. The concept of stochastic tipping points, wherein rare large perturbations push systems between alternative stable states, becomes relevant [23]. The mathematical theory of large deviations provides tools for analyzing such phenomena.

## 7. Conclusion

This report has developed a comprehensive framework for analyzing the Lyapunov stability of welfare systems through the lens of characteristic polynomial theory. The key insight is that the spectral properties of intergenerational transfer matrices—encoded in their characteristic polynomials—determine whether welfare systems exhibit convergent, persistent, or divergent dynamics across generations.

The characteristic polynomial provides complete information about eigenvalue locations, which in turn determine stability properties. The Routh-Hurwitz criterion offers practical methods for assessing stability without explicit eigenvalue computation. The Lyapunov equation provides alternative stability criteria and measures of robustness that complement spectral analysis.

For welfare policy, this framework suggests that stability-enhancing interventions should target the spectral properties of transfer matrices. Increasing the spectral gap—reducing the magnitude of subdominant eigenvalues—accelerates convergence toward desired stationary distributions and reduces intergenerational persistence of welfare states. Monitoring characteristic polynomial coefficients provides quantitative metrics for policy evaluation and early warning of potential instability.

The mathematical sciences continue to offer powerful tools for addressing complex social challenges. As the report from DIMACS emphasized, protecting human well-being in the face of changing environmental, demographic, and economic conditions requires new partnerships between mathematical and social scientists [1]. The framework developed here represents one such partnership, bringing the rigor of control theory and stability analysis to bear on questions of intergenerational welfare dynamics.

Future research should extend this framework to incorporate nonlinear dynamics, time-varying transfer matrices, and stochastic perturbations. Such extensions would provide more realistic models of welfare system behavior and support more nuanced policy analysis. The ultimate goal is to develop mathematical tools that can guide the design of welfare systems capable of maintaining their functional integrity across generations, even in the face of demographic shifts, economic volatility, and changing social conditions.

---

## References

[1] DIMACS. "Sustainability Report." Rutgers University. http://dimacs.rutgers.edu/SustainabilityReport/SustainabilityReport_Final08-02.pdf

[2] Corak, M., Heisz, A., et al. "Intergenerational Transmission of Welfare Receipt." DIW Berlin Discussion Paper No. 693. https://www.diw.de/documents/publikationen/73/diw_01.c.59966.de/dp693.pdf

[3] Lyapunov Stability Analysis. University of Texas at San Antonio. https://ceid.utsa.edu/ataha/wp-content/uploads/sites/38/2017/10/Lyapunov_Stability_Analysis-1.pdf

[4] Haveman, R., Wolfe, B. "The Intergenerational Transmission Process." Figure 1, 1995.

[5] "The Characteristic Polynomial." Georgia Tech Textbook. https://textbooks.math.gatech.edu/ila/characteristic-polynomial.html

[6] Meyer, C.D. "Matrix Analysis and Applied Linear Algebra." SIAM, 2000.

[7] Levin, D.A., Peres, Y., Wilmer, E.L. "Markov Chains and Mixing Times." AMS, 2009.

[8] "Stability of LTI Systems." University of Notre Dame EE 580. https://www3.nd.edu/~lemmon/courses/ee580/lectures/chapter5.pdf

[9] "Lyapunov Stability Definition." University of Washington ME 547. https://faculty.washington.edu/chx/teaching/me547/2_1_stability_slides_Lyapunov_light.pdf

[10] "Stability Analysis Summary." SYSCOP. https://www.syscop.de/files/2019ss/sscs/summary/chap2.pdf

[11] "Lyapunov Equation and Stability." University of Washington ME 547. https://faculty.washington.edu/chx/teaching/me547/2_1_stability_slides_Lyapunov_light.pdf

[12] "Test for LTI Stability." UC Santa Barbara ECE 171A. https://natanaso.github.io/ece171a/ref/ECE171A_7_Stability.pdf

[13] Routh, E.J. "Stability of a Given State of Motion." 1877; Hurwitz, A. "On the Conditions Under Which an Equation Has Only Roots with Negative Real Parts." 1895.

[14] "Routh-Hurwitz Stability Criterion." UC Santa Barbara ECE 171A. https://natanaso.github.io/ece171a/ref/ECE171A_7_Stability.pdf

[15] Diaconis, P., Stroock, D. "Geometric Bounds for Eigenvalues of Markov Chains." Annals of Applied Probability, 1991.

[16] Boyd, S., El Ghaoui, L., Feron, E., Balakrishnan, V. "Linear Matrix Inequalities in System and Control Theory." SIAM, 1994.

[17] "Lyapunov Equation Solution." University of Washington ME 547. https://faculty.washington.edu/chx/teaching/me547/2_1_stability_slides_Lyapunov_light.pdf

[18] "Routh Table Construction." UC Santa Barbara ECE 171A. https://natanaso.github.io/ece171a/ref/ECE171A_7_Stability.pdf

[19] Kim, D. "Intergenerational Risk Sharing and Welfare Analysis." Carnegie Mellon University Dissertation, 2019. https://www.cmu.edu/sites/default/files/cmu-tepper-site-files/2025-06/2019-economics-kim-dissertation.pdf

[20] "Intergenerational Transfers Analysis." NBER Working Paper 28295. https://www.nber.org/system/files/working_papers/w28295/w28295.pdf

[21] Khalil, H.K. "Nonlinear Systems." 3rd Ed., Prentice Hall, 2002.

[22] "Stability of Time-Varying Systems." University of Notre Dame EE 580. https://www3.nd.edu/~lemmon/courses/ee580/lectures/chapter5.pdf

[23] Scheffer, M. "Critical Transitions in Nature and Society." Princeton University Press, 2009.

## Annotations


## Sources
[1] http://dimacs.rutgers.edu/SustainabilityReport/SustainabilityReport_Final08-02.pdf
[2] https://arrow.tudublin.ie/cgi/viewcontent.cgi?article=1040&context=appamas
[3] https://ceid.utsa.edu/ataha/wp-content/uploads/sites/38/2017/10/Lyapunov_Stability_Analysis-1.pdf
[4] https://dspace.mit.edu/bitstream/handle/1721.1/74611/6-241-fall-2003/contents/lecture-notes/chapter_14.pdf
[5] https://dspace.mit.edu/bitstream/handle/1721.1/74611/6-241-fall-2003/contents/recitations/rec6.pdf
[6] https://en.wikipedia.org/wiki/Characteristic_polynomial
[7] https://engineering.purdue.edu/~byao/Research/Supplements/Lyapunov.pdf
[8] https://engineering.purdue.edu/~zak/ECE675__2022/Lyapunov_tutorial.pdf
[9] https://faculty.washington.edu/chx/teaching/me547/2_1_stability_slides_Lyapunov.pdf
[10] https://faculty.washington.edu/chx/teaching/me547/2_1_stability_slides_Lyapunov_light.pdf
[11] https://interactivetextbooks.tudelft.nl/linear-algebra/Chapter6/CharPolynomial.html
[12] https://natanaso.github.io/ece171a/ref/ECE171A_7_Stability.pdf
[13] https://ntrs.nasa.gov/api/citations/19650011559/downloads/19650011559.pdf
[14] https://sites.math.washington.edu/~burke/crs/555/555_notes/lyapunov_stability.pdf
[15] https://textbooks.math.gatech.edu/ila/characteristic-polynomial.html
[16] https://www.cmu.edu/sites/default/files/cmu-tepper-site-files/2025-06/2019-economics-kim-dissertation.pdf
[17] https://www.diw.de/documents/publikationen/73/diw_01.c.59966.de/dp693.pdf
[18] https://www.epa.gov/sites/default/files/2018-03/documents/ee-0078_all_0.pdf
[19] https://www.minneapolisfed.org/institute/working-papers-institute/iwp123.pdf
[20] https://www.minneapolisfed.org/research/institute-working-papers/intergenerational-welfare-assessments
[21] https://www.nationalacademies.org/read/28456/chapter/3
[22] https://www.nature.com/articles/s41599-025-06404-4_reference.pdf
[23] https://www.nber.org/system/files/working_papers/w28295/w28295.pdf
[24] https://www.syscop.de/files/2019ss/sscs/summary/chap2.pdf
[25] https://www3.nd.edu/~lemmon/courses/ee580/lectures/chapter5.pdf