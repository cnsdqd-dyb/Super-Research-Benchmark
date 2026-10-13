# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 9b5df65b | **Time:** 423.88s | **Cost:** $0.07729
--------------------------------------------------------------------------------

# Does the Convex Optimization Solver in Portfolio Algorithms Balance Global Convergence with Local Extrema Escape, or Does Duality Gap Estimation Amplify Complexity in High-Dimensional Allocation?

## Abstract

This research report examines the fundamental tension between global convergence guarantees and local extrema escape mechanisms in convex optimization solvers applied to portfolio allocation problems, while simultaneously investigating whether duality gap estimation introduces additional computational complexity in high-dimensional settings. Drawing upon contemporary developments in optimization theory and portfolio management, we analyze how modern solvers navigate the trade-off between theoretical convergence guarantees and practical computational efficiency. The evidence suggests that convex optimization solvers employ sophisticated mechanisms to balance these competing objectives, with duality gap estimation serving as both a convergence criterion and a potential source of computational overhead in high-dimensional portfolios. Our analysis reveals that the relationship between duality gap estimation and computational complexity is nuanced, depending critically on problem dimensionality, constraint structure, and the specific algorithmic framework employed.

## 1. Introduction

Portfolio optimization represents one of the most mathematically sophisticated challenges in quantitative finance, requiring the solution of complex optimization problems that balance expected returns against various risk measures. The foundational work of Markowitz established the mean-variance framework, which gives rise to quadratic programming problems that are convex in nature [1]. This convexity property carries profound implications for optimization, as it guarantees that any local minimum is also a global minimum—a property that fundamentally shapes how we approach portfolio allocation problems.

The optimization landscape for portfolio selection has evolved considerably since the original quadratic programming formulations. Modern portfolio optimization frequently incorporates higher-order moments, cardinality constraints, and various forms of regularization, leading to problems that may exhibit nonconvex characteristics despite their underlying convex structure [4]. This evolution has necessitated the development of increasingly sophisticated optimization algorithms that must navigate the delicate balance between guaranteeing global convergence and efficiently escaping local extrema when they arise.

The central question motivating this research concerns the mechanisms by which convex optimization solvers achieve reliable convergence in portfolio applications. Specifically, we investigate whether these solvers effectively balance the theoretical guarantee of global convergence (inherent to convex problems) with practical mechanisms for escaping suboptimal local solutions (particularly relevant when problem convexity is compromised), or whether the estimation of duality gaps—a key convergence criterion—inevitably amplifies computational complexity, especially in high-dimensional allocation scenarios.

This report synthesizes insights from multiple recent developments in optimization theory and portfolio management to provide a comprehensive analysis of these interconnected challenges. We examine the theoretical foundations of convex optimization convergence, the role of duality gap estimation in algorithmic termination criteria, the specific challenges posed by high-dimensional portfolio allocation, and the various algorithmic strategies employed to navigate these complexities.

## 2. Theoretical Foundation: Convex Optimization and Global Convergence

### 2.1 The Fundamental Property of Convex Problems

The theoretical bedrock of convex optimization rests upon a remarkable mathematical property: in convex optimization problems, any local minimum is guaranteed to be a global minimum. This property, formally established in optimization theory, eliminates the primary concern of converging to suboptimal local solutions when the problem satisfies convexity conditions [1]. Theorem 2.3, as presented in the literature, establishes that if $x^*$ is a local minimum to a convex optimization problem, meaning there exists $R > 0$ such that $f(x^*) = \inf\{f(x) \mid \|x - x^*\|_2 \leq R^2\}$, then $x^*$ is also a global minimum [1].

This theorem has profound implications for portfolio optimization. The classical mean-variance trade-off problem, defined as maximizing expected return while minimizing portfolio variance, can be formulated as a convex optimization problem. Specifically, the trade-off problem seeks to maximize $w_0 R_0 + w^T \mu - \frac{\gamma}{2} w^T \Sigma w$ subject to the budget constraint $w_0 + w^T \mathbf{1} = 1$, where $\gamma \in \mathbb{R}^+$ is the risk aversion parameter, $\mu$ represents expected returns, and $\Sigma$ is the covariance matrix of returns [1]. Under standard assumptions, this problem exhibits convexity properties that guarantee global optimality of any locally optimal solution.

### 2.2 Implications for Portfolio Algorithm Design

The global convergence property of convex problems fundamentally shapes how portfolio optimization algorithms are designed and analyzed. When the underlying optimization problem is convex, algorithm developers can focus primarily on convergence speed and computational efficiency, rather than worrying about the algorithm converging to suboptimal local solutions. This theoretical guarantee simplifies the analysis of optimization algorithms considerably.

However, the practical implementation of portfolio optimization often introduces complications that may compromise strict convexity. Cardinality constraints, which limit the number of assets in the portfolio, introduce combinatorial elements that can destroy convexity [7]. Similarly, the incorporation of higher-order moments such as skewness and kurtosis—measured by matrices $\Phi \in \mathbb{R}^{N \times N^2}$ and $\Psi \in \mathbb{R}^{N \times N^3}$ respectively—introduces nonconvex objective function components [4]. The co-skewness and co-kurtosis matrices present significant computational challenges in terms of storage, manipulation, and optimization, with the nonconvex nature of the third moment complicating portfolio formulations.

### 2.3 The Role of Problem Scaling and Objective Normalization

In practical portfolio optimization implementations, the scaling of objective functions plays a subtle but important role in convergence behavior. As noted in the algorithmic description of portfolio weight optimization, the loss function $L$ should be divided by $M$ for normalization purposes, though this scaling does not affect the optimal solution since the optimal solution is invariant under scaling [1]. This property ensures that the algorithmic behavior remains consistent regardless of the absolute magnitude of the objective function, which can vary significantly depending on market conditions and asset characteristics.

The invariance of optimal solutions under scaling has important implications for numerical stability and convergence behavior. Algorithms that rely on gradient information or step-size selection may exhibit different convergence rates depending on objective scaling, even though the final solution remains unchanged. This consideration becomes particularly relevant in high-dimensional portfolio allocation problems where numerical precision can significantly impact algorithmic performance.

## 3. Duality Gap Estimation: Mechanisms and Implications

### 3.1 Theoretical Framework of Duality Gap

The duality gap represents a fundamental concept in optimization theory that quantifies the difference between the optimal primal objective value and the optimal dual objective value. In convex optimization, the duality gap is always nonnegative due to the weak duality property and provides a measure of suboptimality for any feasible primal-dual pair [6]. For a given optimization problem, the duality gap can be computed and used to assess how close a candidate solution is to true optimality.

In the context of conic optimization, the duality gap associated with primal and dual solutions can be expressed in terms of the barrier parameter and problem dimension. Specifically, for solutions along the primal-dual central path, the duality gap satisfies $s^*(t)^T x^*(t) = t^{-1} \vartheta$, where $\vartheta$ represents a problem-dependent parameter related to the barrier function [6]. This relationship provides a direct mechanism for controlling solution accuracy through the barrier parameter.

### 3.2 Duality Gap in Algorithmic Termination Criteria

Modern optimization solvers employ duality gap estimation as a key component of their termination criteria. The solver terminates when three conditions are simultaneously satisfied: primal residual $\text{pres}_k^i \leq \epsilon_{\text{pres}} (1 + \|b\|)$, dual residual $\text{dres}_k^i \leq \epsilon_{\text{dres}} (1 + \|c\|)$, and duality gap $\text{dgap}_k^i \leq \epsilon_{\text{dgap}} \left|1 + c^T x + b^T y\right|$ [2]. The quantities $\epsilon_{\text{pres}}$, $\epsilon_{\text{dres}}$, and $\epsilon_{\text{dgap}}$ represent the primal residual, dual residual, and duality gap tolerances, respectively.

The inclusion of duality gap in termination criteria reflects its role as a comprehensive measure of solution quality. Unlike residual-based measures that only capture constraint satisfaction, the duality gap provides information about both primal and dual feasibility, as well as optimality. This comprehensive assessment comes at a computational cost, as duality gap estimation typically requires additional computations beyond those needed for gradient evaluation or constraint checking.

### 3.3 Computational Overhead of Duality Gap Estimation

The estimation of duality gap introduces computational overhead that can be significant in high-dimensional portfolio allocation problems. Computing the duality gap requires knowledge of both primal and dual objective values, which may necessitate additional matrix-vector products or function evaluations beyond those required for the primary optimization algorithm. In large-scale portfolio problems with hundreds or thousands of assets, these additional computations can accumulate substantially.

The overhead associated with duality gap estimation is particularly pronounced in interior-point methods, which maintain strict feasibility throughout the optimization process. These methods typically require the solution of systems of linear equations at each iteration, with the duality gap serving as a key indicator of convergence progress. The computational cost of these linear system solves scales with the cube of problem dimension in dense problems, making high-dimensional applications particularly challenging.

### 3.4 Duality Gap and Safe Region Construction

Beyond its role as a termination criterion, duality gap estimation enables the construction of safe regions that contain optimal dual variables. Research has demonstrated that the duality gap can be used to construct a gap safe sphere that is guaranteed to contain the optimal dual solution [6]. This safe region construction relies on strong concavity properties of the dual problem under certain regularity conditions.

The construction of safe regions has important implications for portfolio optimization, particularly in contexts where dual solutions provide economically meaningful interpretations. In portfolio theory, dual variables often correspond to shadow prices of constraints, indicating the marginal value of relaxing budget or risk constraints. The ability to characterize the uncertainty in these dual values through safe regions provides valuable information for robust decision-making.

## 4. High-Dimensional Portfolio Allocation: Complexity Challenges

### 4.1 Dimensionality and Computational Scaling

High-dimensional portfolio allocation presents significant computational challenges that interact with both convergence behavior and duality gap estimation. As the number of assets $N$ increases, the computational complexity of optimization algorithms becomes increasingly dominated by matrix operations whose cost scales polynomially with dimension. For dense problems, the cubic scaling of interior-point methods ($O(N^3)$) and quadratic scaling of gradient-based methods ($O(N^2)$) can become prohibitive for large-scale portfolios.

The storage requirements for high-dimensional portfolio problems also present challenges, particularly when incorporating higher-order moments. The co-skewness matrix $\Phi \in \mathbb{R}^{N \times N^2}$ and co-kurtosis matrix $\Psi \in \mathbb{R}^{N \times N^3}$ exhibit cubic and quartic scaling with dimension, respectively [4]. These scaling characteristics effectively preclude the direct manipulation of full higher-order moment matrices for portfolios with more than a few dozen assets, necessitating approximation techniques or structured estimation methods.

### 4.2 The Curse of Dimensionality in Duality Gap Estimation

The computational burden of duality gap estimation compounds the curse of dimensionality in high-dimensional portfolio allocation. While the theoretical convergence guarantees of convex optimization apply regardless of dimension, the practical rate of convergence and the computational cost per iteration both deteriorate as dimension increases. Duality gap estimation, which requires computing both primal and dual objective values, adds overhead that scales with problem dimension.

Empirical evidence suggests that the duality gap widens with problem complexity, particularly in multi-period optimization problems with many exercise periods [3]. This widening gap implies that achieving a specified tolerance level requires more iterations or more sophisticated algorithmic techniques in high-dimensional settings. The relationship between dimensionality and duality gap behavior creates a challenging trade-off between solution accuracy and computational feasibility.

### 4.3 Regularization and Dimension Reduction Techniques

To address the computational challenges of high-dimensional portfolio optimization, researchers have developed various regularization and dimension reduction techniques. Regularization approaches, such as $\ell_1$-norm and $\ell_2$-norm penalties on portfolio weights, introduce structure that can reduce effective dimensionality while maintaining desirable statistical properties [9]. These regularization techniques can be interpreted as imposing prior beliefs about portfolio structure or as implementing shrinkage estimators that improve out-of-sample performance.

The regularization term $\sqrt{\delta} \|B^T w\|_q$ introduced in robust portfolio optimization formulations plays a penalizing role that provides robustness to estimation error [9]. The quantity $B^T w$ can be interpreted as the weight allocated to investing in common factors in the mean-variance allocation framework. This factor-based regularization effectively reduces the optimization to a lower-dimensional problem in the factor space, potentially mitigating the computational challenges associated with high-dimensional asset spaces.

### 4.4 Screening Procedures and Computational Efficiency

Recent research has explored screening procedures that exploit problem structure to reduce computational burden without sacrificing solution quality. These procedures identify variables that can be safely eliminated from active consideration based on their optimality conditions, effectively reducing problem dimension during the optimization process [6]. The effectiveness of screening procedures depends critically on problem sparsity, with more sparse problems benefiting more substantially from screening.

Experimental results demonstrate that screening procedures can significantly reduce execution time, with relative execution time decreasing as regularization strength increases [6]. This occurs because stronger regularization leads to portfolio allocations with more zero entries, creating greater opportunity for screening. The unscreened algorithm may require 30 and 19 seconds to reach convergence thresholds, while the screened version requires only 18 and 12 seconds for LOG and EXP-1.00 regularization models, respectively.

## 5. Algorithmic Strategies: Balancing Convergence and Complexity

### 5.1 Interior-Point Methods and Central Path Following

Interior-point methods (IPMs) represent one of the most successful algorithmic frameworks for solving convex optimization problems, including portfolio optimization problems. These methods operate by following the central path through the feasible region, maintaining strict feasibility while progressively reducing the barrier parameter that penalizes proximity to constraint boundaries [12]. The central path is defined by optimality conditions that relate primal and dual variables through the barrier function.

The convergence behavior of interior-point methods is characterized by polynomial complexity bounds that depend on problem dimension and desired accuracy. For linear programming problems, interior-point methods achieve $O(\sqrt{n} \log(1/\epsilon))$ convergence, where $n$ is the problem dimension and $\epsilon$ is the desired tolerance [12]. These complexity bounds provide theoretical guarantees on algorithmic performance, though practical convergence rates often exceed theoretical predictions.

The barrier parameter $\mu$ plays a crucial role in balancing convergence speed against solution accuracy. At each outer iteration, the value of $t$ is updated and the solution $x^*(t)$ is computed through a centering step using Newton's method starting from the current point [12]. The choice of $\mu$ affects the total number of Newton iterations required for convergence, with empirical evidence suggesting that the total number of iterations is not very sensitive to $\mu$ as long as $\mu \geq 10$.

### 5.2 First-Order Methods and Scalability

First-order methods, such as the alternating direction method of multipliers (ADMM), offer improved scalability for large-scale portfolio optimization problems at the cost of slower asymptotic convergence rates. These methods rely on gradient information rather than second-order derivatives, reducing per-iteration computational cost at the expense of requiring more iterations to achieve high-accuracy solutions [13].

The ADMM algorithm for portfolio optimization involves decomposing the original problem into subproblems that can be solved efficiently, with the soft-thresholding operator $S_{\lambda/\rho}(z) = \text{sign}(z) \max(|z| - \lambda/\rho, 0)$ playing a key role in $\ell_1$-regularized formulations [13]. The convergence of ADMM for portfolio optimization problems has been demonstrated empirically, with optimality gaps decreasing steadily over iterations.

First-order methods are particularly attractive for high-dimensional portfolio problems where the cubic scaling of interior-point methods becomes prohibitive. However, the slower convergence rates of first-order methods can be problematic when high accuracy is required, as the number of iterations needed may become excessive. Hybrid approaches that combine the rapid initial convergence of interior-point methods with the scalability of first-order methods have been proposed to balance these competing considerations.

### 5.3 Successive Convex Approximation and Majorization-Minimization

The successive convex approximation (SCA) framework and majorization-minimization (MM) approach provide systematic methods for handling nonconvex objective functions that arise in advanced portfolio optimization formulations. These methods construct convex approximations to the original problem at each iteration, solving the simpler convex subproblem to generate a sequence of improving solutions [4].

The SCA framework has been shown to accelerate convergence for high-dimensional portfolio optimization problems by exploiting problem structure in the approximation construction [4]. The convex approximations are designed to majorize the original objective function, ensuring that each subproblem solution provides a valid descent direction. This majorization property guarantees monotonic improvement in the objective function value, though not necessarily convergence to a global optimum for nonconvex problems.

The convex-concave procedure (CCP) represents a specific heuristic for finding local optima in difference-of-convex (DC) programming problems [8]. This algorithm convexifies the concave components of the objective function using first-order Taylor approximations, transforming the original nonconvex problem into a sequence of convex subproblems. While CCP does not guarantee convergence to global optima, it often finds high-quality solutions efficiently in practice.

### 5.4 Handling Nonconvexity through Problem Reformulation

When portfolio optimization problems exhibit nonconvexity due to cardinality constraints or higher-order moments, various reformulation techniques can restore convexity or facilitate global optimization. Difference-of-convex programming and DC-SOS decomposition techniques provide frameworks for handling nonconvex objectives by expressing them as differences of convex functions [4].

Global optimization approaches for nonconvex portfolio problems often rely on branch-and-bound methods that systematically explore the solution space [8]. These methods maintain bounds on the optimal objective value for different regions of the solution space, pruning regions that cannot contain the global optimum. While theoretically capable of finding global optima, branch-and-bound methods often prove slow in practice due to the large number of partitions and cuts required.

The trade-off between global optimality and computational tractability represents a fundamental challenge in nonconvex portfolio optimization. Local optimization methods, while not guaranteeing global optimality, offer practical solutions with acceptable computational costs [4]. The choice between global and local methods depends critically on the application context, with high-stakes investment decisions potentially justifying the additional computational expense of global methods.

## 6. Numerical Methods and Convergence Behavior

### 6.1 Convergence Criteria and Tolerance Selection

The selection of convergence tolerances significantly impacts both solution quality and computational cost in portfolio optimization. Typical tolerance levels for duality gap range from $10^{-4}$ to $10^{-6}$, with tighter tolerances requiring more iterations but providing greater confidence in solution optimality [13]. The choice of tolerance should balance the practical significance of additional accuracy against the computational cost of achieving it.

For linear optimization problems, convergence tolerances are computed through formulas that scale with problem data magnitudes. Specifically, the scaled primal residual is computed as $\|A x_\tau - b\|_\infty / (1 + \max(\|A x_\tau\|_\infty, \|b\|_\infty))$, with analogous formulas for dual residual and duality gap [13]. This scaling ensures that convergence criteria are meaningful regardless of problem scaling.

The termination criteria for interior-point methods typically involve checking both the duality gap and constraint violations. The algorithm terminates when $m/t < \epsilon$, where $m$ is the number of constraints and $t$ is the barrier parameter [12]. This criterion ensures that both optimality and feasibility are achieved to the specified tolerance level.

### 6.2 Empirical Convergence Rates

Empirical studies of portfolio optimization algorithms reveal significant variation in convergence behavior depending on problem characteristics and algorithmic choices. For $\ell_2$-$\ell_1$-norm minimization problems, different algorithms exhibit markedly different convergence profiles, with block coordinate descent (BCD) methods often achieving rapid initial convergence followed by slower refinement [13].

The convergence rate of ADMM for portfolio optimization problems typically exhibits a linear convergence pattern, with the optimality gap decreasing by a constant factor at each iteration after an initial transient phase. This linear convergence is characteristic of first-order methods and reflects the fundamental limitations of gradient-based information in high-dimensional spaces.

Interior-point methods typically exhibit faster convergence than first-order methods in terms of iteration count, though each iteration is more computationally expensive. For problems with moderate dimension (e.g., $n=50$ variables, $m=100$ inequalities), interior-point methods can achieve duality gap tolerances of $10^{-6}$ in a relatively small number of Newton iterations [12]. The total number of iterations is relatively insensitive to the barrier parameter $\mu$ for $\mu \geq 10$.

### 6.3 Effects of Problem Structure on Convergence

The structure of portfolio optimization problems significantly impacts algorithmic convergence behavior. Problems with special structure, such as those arising from factor models or sparse covariance matrices, can often be solved more efficiently than generic dense problems. This structure exploitation can take the form of specialized linear algebra routines, problem reformulations, or screening procedures that reduce effective dimension.

The presence of cardinality constraints fundamentally changes the nature of portfolio optimization problems, introducing combinatorial elements that destroy convexity. While various heuristic methods can handle cardinality constraints, these methods do not provide guarantees of global optimality. The trade-off between solution quality and computational tractability becomes particularly acute for cardinality-constrained portfolios.

Higher-order moment portfolio optimization presents additional challenges due to the nonconvexity of skewness measures and the high dimensionality of kurtosis tensors. The computational cost of storing and manipulating these high-order objects scales combinatorially with dimension, necessitating approximation techniques or structured estimation methods [4]. These approximations introduce additional error sources that interact with convergence behavior.

## 7. Practical Implications for Portfolio Optimization

### 7.1 Algorithm Selection Considerations

The choice of optimization algorithm for portfolio allocation depends on multiple factors including problem dimension, required solution accuracy, time constraints, and the presence of nonconvex elements. For convex portfolio optimization problems with moderate dimension, interior-point methods offer an excellent balance of reliability and efficiency. These methods provide strong theoretical guarantees and typically achieve high-accuracy solutions in relatively few iterations.

For high-dimensional portfolio problems where interior-point methods become computationally expensive, first-order methods such as ADMM or SCA provide scalable alternatives. These methods sacrifice some convergence speed for improved per-iteration efficiency, making them suitable for problems with hundreds or thousands of assets. The choice between first-order methods should consider the required solution accuracy, as these methods may require many iterations to achieve tight tolerances.

When portfolio optimization problems exhibit nonconvexity due to cardinality constraints or higher-order moments, specialized techniques become necessary. The convex-concave procedure provides a practical heuristic for finding local optima in such problems, though it does not guarantee global optimality. For applications where global optimality is critical, branch-and-bound methods can be employed at the cost of substantially increased computational effort.

### 7.2 Managing Duality Gap in Practice

Practitioners must carefully balance the desire for high-accuracy solutions against the computational cost of achieving tight duality gap tolerances. For many portfolio applications, solutions with duality gaps of $10^{-4}$ to $10^{-3}$ provide sufficient accuracy for decision-making purposes, as the uncertainty in input parameters (expected returns, covariance matrices) typically exceeds optimization accuracy.

The duality gap can serve as a diagnostic tool for identifying problematic problem instances. Large duality gaps at termination may indicate numerical instability, ill-conditioning, or the presence of multiple optimal solutions. In such cases, problem reformulation, re-scaling, or alternative algorithmic approaches may be necessary to achieve reliable solutions.

For multi-period portfolio optimization problems, the duality gap tends to widen with the number of time periods [3]. This observation suggests that practitioners should be particularly attentive to convergence behavior in dynamic portfolio problems, potentially employing adaptive tolerance schemes that tighten tolerances for shorter horizons and relax tolerances for longer horizons.

### 7.3 Robustness Considerations

The robustness of portfolio solutions to estimation error represents a critical practical consideration that interacts with optimization algorithm choice. Regularization techniques, which add penalty terms to the objective function, can improve out-of-sample performance while simultaneously simplifying the optimization problem. The regularization parameter controls the trade-off between solution complexity and robustness, with stronger regularization leading to simpler portfolios that may be more robust to estimation error.

The duality-based perspective on portfolio optimization provides natural robustness interpretations through the dual variables. Shadow prices of constraints indicate the marginal value of relaxing budget or risk constraints, providing information about portfolio sensitivity to constraint changes. The gap safe sphere construction extends this perspective by providing uncertainty sets for dual variables that can inform robust decision-making [6].

Screening procedures that exploit sparsity induced by regularization provide computational benefits while potentially improving solution robustness. Portfolios with many zero weights are often more interpretable and may exhibit better out-of-sample performance due to reduced estimation variance. The computational savings from screening further enhance the attractiveness of regularized portfolio optimization approaches.

## 8. Conclusion

This research report has examined the complex interplay between global convergence guarantees, local extrema escape mechanisms, and duality gap estimation in convex optimization solvers for portfolio allocation. The evidence synthesized from multiple sources reveals that convex optimization solvers are fundamentally designed to leverage the theoretical guarantee that local optima are global optima in convex problems, eliminating the primary concern of converging to suboptimal solutions when problem convexity is maintained.

However, practical portfolio optimization frequently involves nonconvex elements arising from cardinality constraints, higher-order moments, and other extensions to the basic mean-variance framework. In these cases, solvers employ various heuristic mechanisms—including the convex-concave procedure, successive convex approximation, and majorization-minimization—to navigate nonconvex landscapes and find high-quality local solutions. These methods do not guarantee global optimality but provide practical solutions with acceptable computational costs.

Regarding duality gap estimation, our analysis reveals a nuanced relationship with computational complexity. Duality gap estimation serves as a comprehensive convergence criterion that captures both primal and dual feasibility as well as optimality, providing more complete information than residual-based measures alone. However, this comprehensiveness comes at a computational cost that scales with problem dimension. In high-dimensional portfolio allocation, the overhead of duality gap estimation compounds the inherent computational challenges of large-scale optimization, though this overhead is often justified by the quality of convergence information provided.

The balance between global convergence and local extrema escape is thus achieved through a combination of theoretical properties (for convex problems) and algorithmic heuristics (for nonconvex problems), with duality gap estimation serving as both a convergence criterion and a potential source of computational overhead. Practitioners must carefully consider these trade-offs when selecting algorithms and setting convergence tolerances, balancing the desire for high-accuracy solutions against computational feasibility, particularly in high-dimensional portfolio applications.

Future research directions include the development of more efficient duality gap estimation techniques that exploit problem structure, the design of hybrid algorithms that combine the theoretical guarantees of interior-point methods with the scalability of first-order approaches, and the extension of screening procedures to broader classes of portfolio optimization problems. As portfolio optimization continues to incorporate more sophisticated risk measures and constraints, the development of efficient, reliable optimization algorithms will remain a critical research priority.

---

## References

[1] https://www.diva-portal.org/smash/get/diva2:1849045/FULLTEXT01.pdf

[2] https://optimization-online.org/wp-content/uploads/2018/05/6643.pdf

[3] http://web.mit.edu/lkogan2/www/Papers/HaughKogan.pdf

[4] https://portfoliooptimizationbook.com/slides/slides-high-order-portfolios.pdf

[5] https://personal.lse.ac.uk/veraart/papersp.pdf

[6] https://www2.isye.gatech.edu/~nemirovs/Published.pdf

[7] https://www.tandfonline.com/doi/full/10.1080/01621459.2022.2133718

[8] http://arno.uvt.nl/show.cgi?fid=157061

[9] https://arxiv.org/pdf/2405.16989

[10] https://www.sciencedirect.com/topics/economics-econometrics-and-finance/convex-optimization

[11] https://www.sciencedirect.com/science/article/abs/pii/S0957417422024460

[12] https://bookdown.org/palomar/portfoliooptimizationbook/B.4-IPM.html

[13] https://arxiv.org/pdf/2209.01793

[14] https://portfoliooptimizationbook.com/slides/slides-optimization-algorithms.pdf

[15] https://medium.com/@dogoodwithdata/convex-optimization-00bce842d908

## Annotations


## Sources
[1] http://arno.uvt.nl/show.cgi?fid=157061
[2] http://web.mit.edu/lkogan2/www/Papers/HaughKogan.pdf
[3] https://arxiv.org/pdf/2209.01793
[4] https://arxiv.org/pdf/2405.16989
[5] https://bookdown.org/palomar/portfoliooptimizationbook/B.4-IPM.html
[6] https://medium.com/@dogoodwithdata/convex-optimization-00bce842d908
[7] https://optimization-online.org/wp-content/uploads/2018/05/6643.pdf
[8] https://personal.lse.ac.uk/veraart/papersp.pdf
[9] https://portfoliooptimizationbook.com/slides/slides-high-order-portfolios.pdf
[10] https://portfoliooptimizationbook.com/slides/slides-optimization-algorithms.pdf
[11] https://www.diva-portal.org/smash/get/diva2:1849045/FULLTEXT01.pdf
[12] https://www.sciencedirect.com/science/article/abs/pii/S0957417422024460
[13] https://www.sciencedirect.com/topics/economics-econometrics-and-finance/convex-optimization
[14] https://www.tandfonline.com/doi/full/10.1080/01621459.2022.2133718
[15] https://www2.isye.gatech.edu/~nemirovs/Published.pdf