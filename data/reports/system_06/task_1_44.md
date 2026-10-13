# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 8914cec8 | **Time:** 128.33s | **Cost:** $0.12534
--------------------------------------------------------------------------------

# To What Extent Does the Numerical Stability of Overlapping Generations Models Influence the Convergence Speed of Welfare Redistribution Algorithms?

## A Technical Analysis

---

## Abstract

This report examines the intricate relationship between the numerical stability characteristics of Overlapping Generations (OLG) models and the convergence behavior of algorithms designed to compute welfare redistribution equilibria. Drawing on recent developments in computational economics and numerical analysis, we investigate how the structural properties of OLG models—including their dynamic stability conditions, expectation formation mechanisms, and high-dimensional state spaces—propagate through welfare computation algorithms to affect convergence rates. Our analysis reveals that numerical stability in OLG models operates through multiple interconnected channels, each with distinct implications for welfare redistribution algorithms. The findings suggest that the choice between myopic and rational expectations frameworks, the presence of multiple steady states, and the curse of dimensionality inherent in large-scale OLG models collectively determine the practical feasibility and efficiency of welfare computation algorithms.

---

## 1. Introduction

The computational analysis of Overlapping Generations models has emerged as a critical endeavor in modern macroeconomics, particularly as researchers and policymakers seek to understand the welfare implications of demographic transitions, pension system reforms, and intergenerational redistribution policies. The fundamental challenge lies not merely in solving these models, but in solving them efficiently enough to support meaningful policy analysis and numerical experimentation. This report addresses a central question that has received insufficient attention in the literature: to what extent does the numerical stability of OLG models influence the convergence speed of welfare redistribution algorithms?

Understanding this relationship carries substantial practical significance. Welfare redistribution computations in OLG frameworks require iterative procedures that repeatedly evaluate value functions, compute equilibrium prices, and update policy functions across multiple generations. When numerical instabilities emerge—whether through ill-conditioned Jacobian matrices, poorly scaled state variables, or structural properties that create near-multicollinearity in the policy space—these iterative procedures can stall, diverge, or converge prohibitively slowly. The result is not merely longer computation times, but potentially unreliable welfare comparisons that could misinform policy decisions affecting millions of individuals across generations.

The analysis that follows is structured as follows. Section 2 establishes the theoretical foundations of OLG models, with particular attention to their equilibrium conditions and stability properties. Section 3 examines the principal numerical methods employed in solving OLG models, focusing on value function iteration and policy function iteration approaches. Section 4 develops the conceptual framework linking numerical stability to convergence behavior. Section 5 analyzes welfare redistribution algorithms specifically, identifying the channels through which model stability affects their performance. Section 6 synthesizes these discussions into practical implications for researchers and policymakers, and Section 7 concludes with recommendations for future research and model implementation.

---

## 2. Theoretical Foundations of Overlapping Generations Models

### 2.1 Structural Overview and Equilibrium Conditions

The Overlapping Generations framework provides a natural vehicle for analyzing intergenerational economic dynamics. In the canonical two-period lived household formulation, individuals maximize their utility over consumption when young and old, subject to intertemporal budget constraints that bind their labor income, asset holdings, and any transfers received through social security or welfare programs [1]. The resulting equilibrium conditions give rise to a system of functional equations that must be solved simultaneously across all generations.

Formally, consider an economy populated by agents who live for two periods. A young agent in period t chooses consumption $c_{1t}$ and savings $s_t$ to maximize $u(c_{1t}) + \beta u(c_{2t+1})$, subject to the constraints $c_{1t} + s_t = w_t$ and $c_{2t+1} = (1 + r_{t+1})s_t$, where $w_t$ denotes the wage rate and $r_{t+1}$ the interest rate prevailing when the agent is old. The first-order condition yields the familiar Euler equation:

$$u'(c_{1t}) = \beta (1 + r_{t+1}) u'(c_{2t+1})$$

This condition, combined with the market-clearing conditions for labor and capital markets, defines the dynamic system governing the evolution of the capital-labor ratio $k_t$ over time. The aggregate capital stock in period $t+1$ equals the savings of the young in period $t$, leading to the fundamental dynamic equation:

$$k_{t+1} = \frac{s(w_t, r_{t+1})}{1 + n} k_t$$

where $n$ represents the population growth rate. The properties of the savings function $s(\cdot)$—its curvature, monotonicity, and sensitivity to interest rate changes—fundamentally determine the model's dynamic behavior and, consequently, its numerical stability characteristics.

### 2.2 Steady States and Local Stability Analysis

The stability of steady states in OLG models has been extensively analyzed in the literature, revealing conditions that directly impact numerical solution methods. A steady state exists when $k_{t+1} = k_t = k^*$, satisfying:

$$k^* = \frac{s(w(k^*), r(k^*))}{1 + n} k^*$$

where factor prices $w(k)$ and $r(k)$ are derived from the aggregate production function $f(k)$ under competitive markets. The local stability of this steady state depends on the derivative of the dynamic system evaluated at $k^*$, typically analyzed through the slope of the savings function relative to the 45-degree line in $(k_t, k_{t+1})$ space.

The stability condition can be expressed analytically through logarithmic derivatives as:

$$\eta_{SSL}^\sigma + 1 - SSL^\sigma < 1 \quad \text{or} \quad > 1$$

where $\eta_{SSL}^\sigma$ represents the elasticity of savings with respect to the interest rate, and $SSL^\sigma$ captures the sensitivity of wage income to capital accumulation [2]. This condition determines whether small deviations from the steady state converge back to or diverge from $k^*$, with profound implications for numerical solution procedures. When the absolute value of the relevant derivative exceeds unity, numerical perturbations can compound rather than diminish, creating instability in iterative solution methods.

### 2.3 Multiple Steady States and Indeterminacy

A particularly challenging aspect of OLG models for numerical computation is the potential for multiple steady states, some stable and others unstable. As documented in the literature, models with certain parameter configurations can exhibit three steady states—two stable and one unstable—creating complex dynamics that complicate welfare analysis [2]. The presence of indeterminacy implies that the economy's long-run outcome depends not merely on fundamentals but on expectations and historical contingencies, a feature that introduces significant complexity for numerical algorithms seeking to compute equilibrium allocations and associated welfare measures.

The indeterminacy in OLG models extends beyond deterministic settings to stochastic environments, where the equilibrium set becomes infinite-dimensional due to the existence of multiple selections of transition and policy functions from the equilibrium set [3]. Each selection corresponds to a different sequential competitive equilibrium path, potentially converging to the same steady state but exhibiting substantially different transitional dynamics. For welfare redistribution algorithms, this indeterminacy means that seemingly identical computational procedures can yield different results depending on the specific equilibrium selection criterion employed.

---

## 3. Numerical Methods for Overlapping Generations Models

### 3.1 Value Function Iteration and Its Convergence Properties

Value function iteration represents the foundational numerical approach for solving dynamic economic models, including OLG frameworks. The method proceeds by successively approximating the value function $v^*$ that satisfies the Bellman equation:

$$v^*(k) = \max_{k' \in \Gamma(k)} \left\{ u(f(k) - k') + \beta v^*(k') \right\}$$

Starting from an initial guess $v_0$, the iteration $v_{s+1} = T v_s$ generates a sequence of approximations that converge to $v^*$ under standard contraction mapping assumptions. The contraction property, guaranteed by the discount factor $\beta < 1$, ensures theoretical convergence but has important implications for computational efficiency.

A critical insight from the numerical analysis literature is that value function iteration converges linearly at the rate $\beta$ [1]. Formally, successive iterates satisfy:

$$\|v_{s+1} - v^*\| \leq \beta \|v_s - v^*\|$$

for an appropriate norm $\|\cdot\|$. This linear convergence implies that each iteration reduces the approximation error by a constant proportion $\beta$, meaning that achieving high-precision solutions requires computational effort growing linearly with the logarithm of the desired tolerance. For typical parameter values with $\beta = 0.95$, this means approximately 180 iterations to achieve an error below $10^{-4}$, a substantial computational burden when each iteration involves solving a high-dimensional optimization problem.

### 3.2 Policy Function Iteration and Acceleration Techniques

Howard's improvement algorithm, also known as policy function iteration, offers a potent acceleration technique that can achieve quadratic convergence under favorable conditions [1]. The method alternates between two steps: given a policy function $h_s$, solve for the value function $v_s$ that would occur if agents followed $h_s$ forever; then, use $v_s$ to compute an improved policy function $h_{s+1}$ that maximizes the right-hand side of the Bellman equation. This procedure is conceptually analogous to Newton's method for finding zeros of a function, and like Newton's method, it can exhibit dramatically faster convergence when the initial guess is sufficiently close to the solution.

The algorithm proceeds as follows [1]:

**Step 1:** Initialize $v_0$ and $h_0$.

**Step 2:** For the current policy function $h_s$, compute the associated value function $v_s$ by solving the linear system:
$$v_s(k) = u(f(k) - h_s(k)) + \beta v_s(h_s(k))$$

**Step 3:** Update the policy function by solving:
$$h_{s+1}(k) = \arg\max_{k' \in \Gamma(k)} \left\{ u(f(k) - k') + \beta v_s(k') \right\}$$

**Step 4:** Check for convergence in either the value function (using the criterion $\|v_0 - v_1\|_\infty < \epsilon(1 - \beta)$) or the policy function (requiring no change for a specified number of consecutive iterations).

Modified policy iteration variants use intermediate improvement steps—performing $k$ policy evaluations between full policy updates—to balance the faster convergence of pure policy iteration against the lower per-iteration cost of value iteration [1]. These modified algorithms have proven particularly effective in OLG applications, where the curse of dimensionality makes full policy iteration computationally expensive.

### 3.3 Addressing the Curse of Dimensionality

Large-scale OLG models present significant computational challenges stemming from the curse of dimensionality. Equilibrium allocations and prices generally depend on the entire distribution of wealth or capital holdings, in addition to varying Social Security contributions across household types and cohorts [4]. This dependence on the full distribution implies that the state space grows exponentially with the number of state variables, quickly overwhelming conventional solution methods.

Several approaches have emerged to tackle this dimensionality challenge. State-aggregation methods, following Krusell and Smith, approximate the full distribution with a finite number of moments or types, dramatically reducing computational requirements at the cost of approximation error [4]. Smolyak sparse grids, introduced to OLG models by Krueger and Kubler, offer an alternative approach that exploits the structure of high-dimensional integration problems to achieve accurate approximations with far fewer grid points than full tensor products [4]. More recently, projection algorithms using linear polynomials on sparse grids have enabled the solution of large-scale OLG models with dozens of continuous state variables [4].

The decomposition approach developed by Rausch represents another avenue for managing complexity, replacing the full OLG demand system with an infinitely-lived representative agent to obtain candidate equilibrium prices, then using these prices to solve a partial equilibrium relaxation [5]. This sequential recalibration approach can be particularly advantageous for modeling tasks that necessitate economizing on dimensionality while still capturing distributional effects.

---

## 4. Numerical Stability and Convergence: The Conceptual Framework

### 4.1 Sources of Numerical Instability in OLG Models

Numerical instability in OLG models arises from multiple sources, each with distinct implications for convergence behavior. First, structural instabilities in the underlying economic model—characterized by unstable steady states, explosive dynamics, or extreme sensitivities to initial conditions—propagate through numerical algorithms to create practical solution difficulties. When small discretization errors or approximation mistakes cause the numerical solution to deviate from the attracting manifold toward an unstable steady state or divergent path, the iterative procedure may fail to converge or may converge to an economically irrelevant equilibrium.

Second, algorithmic instabilities emerge from the numerical methods themselves. Value function iteration, while theoretically guaranteed to converge under contraction mapping assumptions, can exhibit slow convergence when $\beta$ is close to unity, as is common in OLG applications calibrated to match long-term economic data. Policy function iteration, despite its potential for quadratic convergence, can diverge if the initial policy guess is poor or if the value function computation introduces numerical errors that bias the policy update. Modified policy iterations with intermediate improvement steps attempt to balance these concerns, but the optimal number of improvement steps depends on problem-specific factors that are difficult to a priori determine [1].

Third, scaling and conditioning issues arise when the numerical implementation fails to properly normalize state variables, leading to ill-conditioned matrices in the underlying linear systems. In OLG models with heterogeneous agents, the interaction of multiple state variables—their relative magnitudes and the functional forms connecting them to decisions—can create near-singular Jacobians that amplify rounding errors and slow convergence.

### 4.2 The Mechanics of Convergence Rate Determination

The convergence rate of welfare redistribution algorithms depends fundamentally on the spectral properties of the underlying operators and matrices. For value function iteration, the contraction modulus $\beta$ governs the asymptotic convergence rate, with each iteration reducing the error by this factor. More precisely, the convergence is linear with rate $\beta$, meaning:

$$\lim_{s \to \infty} \frac{\|v_{s+1} - v^*\|}{\|v_s - v^*\|} = \beta$$

This geometric convergence pattern implies that the number of iterations required to achieve a specified tolerance $\tau$ grows as $\log(1/\tau) / \log(1/\beta)$. For welfare computations requiring high-precision value function estimates—necessary for accurate welfare comparisons across generations—this logarithmic scaling translates into substantial computational demands.

Policy function iteration, when it converges quadratically, exhibits fundamentally different error dynamics. Under ideal conditions, the error satisfies:

$$\|v_{s+1} - v^*\| \leq C \|v_s - v^*\|^2$$

for some constant $C$, implying that the number of correct digits roughly doubles with each iteration. This quadratic convergence is dramatically faster than linear convergence, potentially reducing computation time from hundreds of iterations to fewer than ten. However, quadratic convergence is not guaranteed; Puterman and Brumelle established that it requires certain conditions on the policy improvement operator that may not hold in all OLG applications [1].

### 4.3 Expectation Formation and Dynamic Properties

The choice between myopic and rational expectations has profound implications for both the theoretical dynamics of OLG models and the practical convergence of numerical algorithms. Under myopic expectations, agents form beliefs about future variables based solely on current information, leading to dynamics governed by:

$$\frac{dk_{t+1}}{dk_t} = \eta_{SSL}^\sigma + 1 - SSL^\sigma$$

Under rational expectations, agents correctly anticipate the equilibrium relationship between current and future variables, yielding:

$$\frac{dk_{t+1}}{dk_t} = \frac{1 - SSL^\sigma}{1 - \eta_{SSL}^\sigma SSL^\sigma}$$

The convergence speed (or divergence speed, in unstable cases) differs substantially between these two formulations [2]. Crucially for numerical computation, the rational expectations case often exhibits faster convergence to steady state, meaning that algorithms solving rational expectations models may require fewer iterations to achieve convergence. However, the computational cost per iteration is higher because rational expectations require solving fixed-point problems that embed the equilibrium condition within the agent's optimization.

---

## 5. Welfare Redistribution Algorithms: Channels of Influence

### 5.1 Computing Welfare in OLG Frameworks

Welfare analysis in OLG models requires computing the expected utility of agents across all generations, accounting for the redistributional effects of policies and the resulting equilibrium price paths. This computation involves several interconnected steps: solving for the equilibrium price sequence $\{w_t, r_t\}_{t=0}^\infty$, computing optimal consumption and savings for each generation given these prices, aggregating individual utilities into a social welfare measure, and comparing welfare across alternative policy regimes.

The social welfare function in OLG models presents conceptual challenges because the relevant social planner must compare the welfare of generations that are alive at different points in time. In the standard approach, welfare is computed as a weighted sum of individual utilities, with weights potentially reflecting ethical judgments about intergenerational equity. The aggregate welfare level, measured in consumption-equivalent terms, provides a summary statistic for comparing equilibria:

$$W = \frac{1}{1 + \beta} \sum_{t=0}^\infty \beta^t u(c_{1t}) + \frac{\beta}{1 + \beta} \sum_{t=0}^\infty \beta^t u(c_{2t})$$

When computing this measure numerically, the infinite horizon requires truncation and approximation, introducing additional convergence considerations beyond those arising from the underlying OLG solution.

### 5.2 Transition Path Computation and Welfare Analysis

A central challenge in welfare analysis is computing the transition path between steady states under different policy regimes. Whether analyzing the switch from a pay-as-you-go to a fully funded social security system, or comparing outcomes under alternative redistribution schemes, researchers must trace the dynamic path of the economy as it adjusts from an initial condition to a new steady state. This computation requires solving the sequence of temporary equilibria that characterize the transition, each defined by market-clearing conditions given current-period expectations about future variables.

The welfare implications of transitions can be substantial. As documented in the literature, alternative transition paths with the same ultimate steady state can yield welfare differences equivalent to several percent of permanent consumption [6]. In one simulation study, the social planner's choice of price (interest rate) path affected aggregate welfare by 3.51%, translating to a welfare gain equivalent to a 1.2% consumption increase [6]. These findings underscore the importance of accurately computing transition paths, a task that is highly sensitive to numerical stability considerations.

### 5.3 The Impulse Value and Computational Complexity

Recent work on the Full Analytical Model of Economics (FAME) has introduced the concept of the Impulse Value, which characterizes the welfare response to small shocks in the economy. The Impulse Value is a four-dimensional object that, when discretized naively, would require constructing a transition matrix with $10^{16}$ entries—even with sparse structure, this presents significant computational challenges [7]. The efficient representation of the Impulse Value as a square matrix rather than a column vector, using the discretization $Lv + vL^T$, enables computation using only the two-dimensional steady-state matrix rather than the full four-dimensional object.

This example illustrates a broader principle: the structure of welfare measures in OLG models interacts with the underlying numerical implementation in ways that can either amplify or mitigate computational complexity. Algorithms that exploit the algebraic structure of the problem—recognizing commutation relations, identifying invariant subspaces, or leveraging sparsity patterns—can achieve substantial speedups relative to naive implementations. Conversely, implementations that fail to account for structural properties may face convergence difficulties or excessive computational demands.

---

## 6. Synthesis: How Stability Affects Convergence in Practice

### 6.1 The Feedback Between Model Properties and Algorithm Performance

The relationship between numerical stability and convergence speed in OLG welfare computations operates through multiple feedback mechanisms. When model parameters place the economy near a bifurcation point—where a stable steady state becomes unstable, or where additional steady states emerge—the Jacobian matrix governing local dynamics approaches singularity. This near-singularity propagates through the linear systems solved during value function computation, causing condition numbers to swell and numerical errors to amplify. The result is slower convergence in iterative procedures and greater sensitivity to rounding errors and approximation choices.

The interaction between expectation formation and convergence is particularly consequential. Models with myopic expectations tend to exhibit slower convergence to steady state, requiring more iterations to achieve a given precision [2]. However, the computational cost per iteration is lower because myopic expectations decouple the current period's optimization from future periods' equilibrium conditions. Rational expectations models require solving higher-dimensional fixed-point problems at each iteration, but they converge in fewer iterations because the equilibrium condition is incorporated directly into the optimization. The net computational cost depends on the specific problem characteristics and implementation details.

### 6.2 Policy Iteration in Welfare Applications

Policy function iteration offers significant advantages for welfare computations, provided that the numerical implementation maintains stability. The value function associated with a given policy provides the complete welfare information needed for social welfare comparisons; once $v_s$ is computed under policy $h_s$, welfare measures for all generations are immediately available. Updating to $h_{s+1}$ based on $v_s$ then yields an improved welfare estimate. This tight integration between policy improvement and welfare evaluation makes policy iteration particularly attractive for welfare redistribution algorithms.

However, the practical implementation of policy iteration for welfare analysis requires careful attention to numerical stability. The linear system solving for $v_s$ given $h_s$ can be sensitive to the conditioning of the transition matrix, especially when the policy function implies rapid transitions between states or concentrated probability mass on particular state values. In OLG models with bequest motives or heterogeneous agents, the policy function may exhibit kinks or discontinuities that create additional numerical challenges. Appropriate smoothing techniques and state-space discretization strategies can mitigate these issues but introduce approximation errors that must be balanced against convergence benefits.

### 6.3 Recommendations for Implementation

Based on the foregoing analysis, several practical recommendations emerge for researchers implementing welfare redistribution algorithms in OLG frameworks. First, preconditioning the state variables to have comparable scales can substantially improve the conditioning of the linear systems encountered during value function computation. Normalizing capital stocks, wealth levels, and other state variables by their steady-state values or by economically meaningful benchmarks helps ensure that numerical operations preserve precision across the relevant range.

Second, the choice between value iteration, policy iteration, and modified policy iteration should be guided by problem characteristics. For high-dimensional problems where the curse of dimensionality makes full policy iteration expensive, modified policy iteration with intermediate improvement steps (e.g., $k = 30$ as reported in some implementations [1]) offers a reasonable balance between convergence speed and per-iteration cost). For lower-dimensional problems where full policy iteration is tractable, the potential for quadratic convergence justifies the additional per-iteration computation.

Third, convergence criteria should be chosen carefully to balance computational efficiency against accuracy requirements. The criterion $\|v_0 - v_1\|_\infty < \epsilon(1 - \beta)$ provides a statistically meaningful tolerance that accounts for the contraction modulus, but may require many iterations for high $\beta$ values. For welfare comparisons, where relative rather than absolute welfare differences often matter, alternative criteria based on changes in welfare measures rather than value functions may be more appropriate.

Fourth, when multiple steady states or indeterminacy are present, researchers should explicitly consider the equilibrium selection mechanism and its welfare implications. Algorithms that compute only one equilibrium path may miss important welfare-relevant alternatives, while algorithms that explore the full equilibrium set face substantially higher computational costs. The choice depends on the research question and the policy context.

---

## 7. Conclusion

This report has examined the multifaceted relationship between numerical stability in Overlapping Generations models and the convergence speed of welfare redistribution algorithms. Our analysis reveals that this relationship operates through several interconnected channels: the structural stability properties of the underlying economic model, the convergence characteristics of the numerical methods employed, and the specific computational challenges arising from high-dimensional state spaces and complex welfare measures.

The key findings can be summarized as follows. Value function iteration provides a theoretically sound but computationally intensive approach, with linear convergence at rate $\beta$ that can require hundreds of iterations for high-precision solutions. Policy function iteration offers the potential for quadratic convergence but requires careful implementation to maintain numerical stability, particularly when the underlying model exhibits complex dynamics or near-singular Jacobians. The choice between myopic and rational expectations affects both the theoretical convergence rate and the computational cost per iteration, with implications for the overall efficiency of welfare computations.

For welfare redistribution specifically, the tight integration between policy improvement and welfare evaluation makes policy iteration particularly attractive, provided that the linear systems involved remain well-conditioned. The curse of dimensionality in large-scale OLG models necessitates sophisticated techniques—sparse grids, state aggregation, decomposition algorithms—to achieve tractable computation while maintaining accuracy in welfare measures.

The practical implication is that researchers and policymakers cannot treat numerical stability as a secondary concern orthogonal to welfare analysis. The stability properties of the underlying model fundamentally constrain what welfare computations are feasible and how long they will take. Model parameterizations that create structural instabilities or that push the economy near bifurcation points will invariably slow convergence and increase the risk of numerical failures. Conversely, well-behaved parameterizations with unique, stable steady states enable more efficient computation of welfare measures across alternative redistribution schemes.

Future research should continue to develop numerical methods that exploit the specific structure of welfare problems in OLG models. The efficient representation of Impulse Values, the development of preconditioners tailored to intergenerational dynamics, and the design of adaptive algorithms that adjust their iteration strategy based on observed convergence behavior all represent promising directions. As OLG models become increasingly important for analyzing demographic challenges and pension system reforms, improving the numerical foundations of welfare computations will remain a vital research priority.

---

## References

[1] IFO Institute. "Policy Function Iteration Methods for Overlapping Generations Models." CESifo Working Paper No. 2278.

[2] National Bureau of Economic Research. "Expectations and Stability in Overlapping Generations Models." NBER Working Paper No. 34193.

[3] Cowles Foundation. "Numerical Simulation of Overlapping Generations Models with Indeterminacy." Yale University Research Archive.

[4] Carnegie Mellon University. "Computation of Large-Scale Overlapping Generations Models." TEPPER School of Economics Dissertation.

[5] MIT. "Sequential Recalibration Algorithm for General Equilibrium Models." Rausch, Computation of OLG Models.

[6] Levine, D. "Numerical Simulation of Stochastic OLG Models." UCLA Economics Archive.

[7] Yale University. "Master Equation for Full Analytical Model of Economics." Cowles Foundation Working Paper.

## Annotations


## Sources
[1] http://www.dklevine.com/archive/refs4661465000000001110.pdf
[2] https://academic.oup.com/oxrep/article/41/2/260/8317912
[3] https://apps.it.purdue.edu/kap/KATALYST/public/publications.aspx?personid=100263&publicationid=7288&attachmentid=738
[4] https://arxiv.org/abs/2509.05170
[5] https://cowles.yale.edu/sites/default/files/2023-04/MasterEquation.pdf
[6] https://dspace.mit.edu/bitstream/handle/1721.1/67034/Rausch_Computation%20of.pdf?sequence=1
[7] https://economics.mit.edu/sites/default/files/inline-files/Lecture%208%20-%20Overlapping%20Generations.pdf
[8] https://economics.mit.edu/sites/default/files/inline-files/Lecture%208%20-%20Overlapping%20Generations_1.pdf
[9] https://editorialexpress.com/jrust/research/siam_dp_paper.pdf
[10] https://en.wikipedia.org/wiki/Overlapping_generations_model
[11] https://fass.nus.edu.sg/ecs/wp-content/uploads/sites/4/2024/07/hact2.pdf
[12] https://oyc.yale.edu/economics/econ-251/lecture-12
[13] https://press.lse.ac.uk/chapters/2/files/1763ee8e-a067-4d86-a9dc-9dbf5f7496b8.pdf
[14] https://shs.hal.science/halshs-03922354v1/document
[15] https://stackoverflow.com/questions/37370015/what-is-the-difference-between-value-iteration-and-policy-iteration
[16] https://web.econ.ku.dk/okocg/VM/VM-general/Kapitler%20til%20bog/Ch3-4-2017-1.pdf
[17] https://www.cmu.edu/sites/default/files/cmu-tepper-site-files/2025-06/2019-economics-kim-dissertation.pdf
[18] https://www.cmu.edu/sites/default/files/cmu-tepper-site-files/2025-06/2021-economics-moretto-dissertation.pdf
[19] https://www.fiskalrat.at/dam/jcr:a85d3b0c-c031-4f8b-8214-0f6405f6f0bd/FISK_OLG_Model_v2.3_WP_11_2025.pdf
[20] https://www.ifo.de/DocDL/cesifo1_wp2278.pdf
[21] https://www.mpsge.org/srolg.pdf
[22] https://www.nber.org/papers/w34193
[23] https://www.nber.org/system/files/working_papers/w19179/w19179.pdf
[24] https://www.nber.org/system/files/working_papers/w31103/w31103.pdf
[25] https://www.nber.org/system/files/working_papers/w34193/w34193.pdf
[26] https://www.sciencedirect.com/science/article/abs/pii/S0165188903001118
[27] https://yangycpku.github.io/files/DeepHAM_paper.pdf