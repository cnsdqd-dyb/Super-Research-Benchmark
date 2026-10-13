# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 584fb43a | **Time:** 82.16s | **Cost:** $1.19485
--------------------------------------------------------------------------------

# Convex Optimization Solvers in Portfolio Algorithms: Balancing Global Convergence, Local Extrema, and Duality Gap Estimation Complexity

This report examines whether convex optimization solvers used in portfolio allocation can simultaneously achieve global convergence guarantees and escape from local extrema, while addressing the question of whether duality gap estimation amplifies computational complexity in high-dimensional settings. The analysis reveals that while convex optimization provides theoretical global convergence guarantees, practical portfolio optimization often requires sophisticated dual-decomposition methods and interior-point approaches to manage the interplay between convergence guarantees, numerical stability, and scalability in high-dimensional asset allocation problems.

## The Theoretical Foundation of Convex Optimization in Portfolio Algorithms

The mathematical framework underlying modern portfolio optimization is fundamentally rooted in convex optimization theory[4]. Portfolio optimization problems are typically formulated as minimizing a convex objective function over a convex feasible set, which ensures that any local minimum is also a global minimum[4]. This property represents one of the most powerful advantages of convex optimization approaches—the elimination of the traditional tension between local and global optimality that plagues non-convex formulations. However, this theoretical guarantee comes with important nuances that become apparent when considering practical implementations in high-dimensional asset allocation scenarios.

The classical mean-variance portfolio optimization framework originally proposed by Markowitz formulates the portfolio selection problem as a convex quadratic programming problem[39][42]. The basic formulation seeks to minimize portfolio variance—measured by the quadratic form $\mathbf{w}^T \Sigma \mathbf{w}$ where $\Sigma$ is the covariance matrix and $\mathbf{w}$ are portfolio weights—subject to linear constraints ensuring that weights sum to one, remain non-negative for long-only portfolios, and achieve a minimum expected return[39][42]. This structure is explicitly convex, meaning that the optimization landscape contains no spurious local minima, and gradient-based optimization methods are guaranteed to converge to the true optimal solution regardless of initialization point[4].

The convexity guarantee becomes particularly powerful in portfolio contexts because it eliminates a fundamental source of algorithmic difficulty. Unlike non-convex machine learning problems where optimization algorithms can become trapped in poor local minima, portfolio optimization algorithms operating on convex formulations are mathematically guaranteed to find the globally optimal allocation given sufficient computational resources and numerical precision[4]. This characteristic has made convex optimization the dominant paradigm in institutional portfolio management and quantitative finance.

## Global Convergence Guarantees and the Convex Optimization Promise

The literature on convex optimization establishes formal convergence guarantees for portfolio optimization problems that provide strong theoretical foundations for practical solver development[1][3]. These convergence guarantees come in multiple forms, each providing different information about algorithm behavior as iterations proceed toward optimality. For gradient-based methods applied to smooth convex functions, the standard convergence rate is $O(1/k)$, where $k$ denotes the iteration number[28]. This means that the optimality gap decreases at a rate inversely proportional to the number of iterations, so achieving higher precision typically requires proportionally more computational effort[28].

For strongly convex objectives—a condition typically satisfied by many portfolio optimization formulations when appropriate regularization is applied—even more powerful convergence guarantees become available[28]. Strongly convex functions possess a form of "curvature" that allows optimization algorithms to exploit local geometric information more effectively. In this case, accelerated gradient methods achieve convergence rates of $O(1/k^2)$ for smooth objectives, representing a quadratic acceleration compared to standard gradient descent[28]. This acceleration is particularly valuable in portfolio optimization because strong convexity often naturally arises when the covariance matrix has full rank and appropriate constraints are imposed, making the theoretical acceleration practically relevant.

The convergence analysis of primal-dual methods, which are central to modern portfolio optimization, provides additional insights into how global convergence guarantees translate to practical algorithm performance[7][12]. For primal-dual gradient methods applied to convex-concave optimization problems—the natural formulation for constrained portfolio optimization—linear convergence rates can be established even when the primal objective function is only convex but not strongly convex, provided that the coupling matrix has full column rank[7]. This result represents a significant theoretical advance because it shows that the convex structure can guarantee fast convergence even in settings where the objective function itself lacks strong convexity.

These convergence guarantees establish that convex portfolio optimization algorithms achieve global convergence to optimal solutions from arbitrary starting points. The theoretical analysis provides explicit bounds on convergence rates, allowing practitioners to estimate the computational resources required to achieve specific levels of precision. However, the practical implications of these theoretical results become nuanced when considering the implementation challenges that arise in realistic portfolio optimization scenarios.

## Local Extrema in Convex versus Constrained Portfolio Contexts

The question of whether portfolio optimization algorithms need to escape from local extrema contains an important subtlety rooted in the distinction between convex and constrained optimization. In the pure convex optimization setting without constraints, the global convergence guarantee eliminates the possibility of local minima that are not global minima—every stationary point the algorithm encounters is necessarily an optimal solution[4]. This is the fundamental advantage of convexity and represents the primary reason convex formulations are preferred for portfolio optimization.

However, practical portfolio optimization introduces constraints that modify this landscape in important ways. When portfolio optimization problems include box constraints (limiting individual asset weights to specified ranges), cardinality constraints (limiting the number of assets in the portfolio), or more sophisticated allocation constraints, the optimization landscape changes fundamentally[2]. While the objective function remains convex, the feasible region becomes more restrictive, and the interaction between the convex objective and the constrained feasible set can create situations where first-order optimization methods become sensitive to problem conditioning and numerical precision[2].

The research on dynamic portfolio optimization with constraints demonstrates that allocation constraints can fundamentally alter optimal portfolio behavior compared to unconstrained solutions[2]. Specifically, when portfolio allocation is constrained to lie within a convex cone—such as when individual asset weights must remain within specified bounds—the optimal constrained portfolio may differ substantially from the "naïve" approach of capping the unconstrained optimal solution at constraint boundaries[2]. This phenomenon suggests that the interaction between constraints and the optimization landscape creates complexity that requires careful numerical treatment, even though the underlying problem remains convex.

In constrained convex optimization, the notion of "local extrema escape" becomes less relevant in the traditional sense because stationary points remain optimal solutions. However, numerical issues and algorithm design choices can lead to convergence toward boundary points or constraint-activated regions that may not be numerically stable or may represent degenerate solutions[2]. The practical challenge becomes ensuring that the algorithm converges to well-conditioned, numerically stable solutions within the constrained feasible region, rather than escaping from spurious local minima.

## Duality Gap Estimation and Complexity in High-Dimensional Settings

Duality gap estimation represents a sophisticated mechanism for measuring optimality and controlling convergence in convex optimization solvers, with important implications for the complexity-optimality tradeoff in high-dimensional portfolio allocation[5][9][29]. The duality gap for a convex optimization problem is defined as the difference between the value of the primal objective at a candidate solution and the value of the dual objective at a related dual point. For any primal solution and dual solution satisfying complementary slackness conditions, the duality gap bounds the suboptimality of the current solution—a fundamental result from convex optimization duality theory[5][18].

In the context of interior-point methods, which are widely used for solving portfolio optimization problems, the duality gap provides a natural stopping criterion with precise optimality guarantees[18]. The barrier method, a classical interior-point approach, uses duality gap bounds to control convergence[18]. At each iteration, the algorithm computes a lower bound on the optimal value through the dual problem, allowing the algorithm to determine when the current primal solution is within a specified tolerance of optimality[18]. This mechanism is theoretically elegant because it provides optimality guarantees without requiring the algorithm to explicitly solve dual variables to high precision—the algorithm only needs to ensure that the primal-dual gap is sufficiently small[18].

However, computing the duality gap in high-dimensional portfolio optimization introduces several sources of complexity. First, the dual problem itself may be as high-dimensional as the primal problem, or higher if the constraint set is complex[5]. Computing accurate dual variables requires solving coupled systems of equations involving the problem's structure matrices—operations whose computational complexity scales unfavorably with problem dimension[5]. For portfolio problems with hundreds or thousands of assets, these computations can dominate overall solver time[13].

Second, the conditioning of the duality gap computation depends critically on the condition number of certain linear systems within the optimization problem[16]. For portfolio covariance matrices, which are often estimated from finite samples and may be numerically ill-conditioned, the computational cost of forming and solving systems related to duality gap estimation can become prohibitive[16]. The research on quantum interior-point methods applied to portfolio optimization demonstrates that even theoretical quantum speedups for convex optimization face fundamental challenges related to the condition number of systems arising in duality gap computation[16]. Classical numerical analysis shows that the condition number of the covariance matrix directly impacts the computational cost of interior-point methods, with poorly conditioned problems requiring substantially more iterations to achieve convergence[13][15].

## Primal-Dual Methods and the Balance Between Convergence and Computational Efficiency

Primal-dual splitting methods represent a sophisticated approach to balancing global convergence guarantees with computational efficiency in high-dimensional portfolio optimization[10][12]. These methods operate by simultaneously updating primal and dual variables, allowing the algorithm to make progress on both the primal objective and the dual constraints in a coordinated fashion[10][12]. The primal-dual framework naturally incorporates duality gap estimation into the algorithm's convergence mechanism, providing both optimality bounds and guidance for adaptive step size selection[12].

The convergence analysis of primal-dual methods reveals important relationships between problem structure, convergence rates, and computational complexity[10][12]. For problems with composite structure—where the objective decomposes as the sum of simple convex functions—primal-dual methods can exploit this structure to achieve convergence without explicitly solving costly subproblems[10]. The variance reduction techniques incorporated into modern primal-dual methods further improve convergence rates by reducing the noise inherent in stochastic gradient estimates[10].

In the portfolio optimization context, primal-dual methods enable the use of efficient decomposition schemes where the optimization problem is split across asset classes, risk factors, or time periods[5]. The dual variables naturally correspond to Lagrange multipliers associated with constraints, making them economically interpretable in portfolio contexts—dual variables on budget constraints represent shadow prices of capital, while dual variables on risk constraints represent marginal costs of additional risk reduction[5]. This economic interpretability allows practitioners to understand not just the optimal allocation, but also the value of relaxing specific constraints.

## Interior-Point Methods and the Complexity-Precision Tradeoff

Interior-point methods constitute the most computationally efficient practical approach to solving convex portfolio optimization problems, particularly when polynomial-time complexity guarantees and robust handling of non-trivial constraint structures are required[13][15][18]. These methods operate by maintaining iterates strictly within the interior of the feasible region, approaching the boundary only in the limit, which provides substantial numerical advantages compared to active-set methods[13][18].

The barrier method, a classical interior-point approach, uses logarithmic barrier functions to enforce feasibility while solving a sequence of approximately unconstrained problems of the form:

minimize $f(x) + \frac{1}{t}\phi(x)$

where $\phi(x) = -\sum_{i=1}^m \log(-f_i(x))$ is the logarithmic barrier function and $t$ is a parameter that increases toward infinity[18]. As $t$ increases, the solution to this modified problem approaches the solution to the original constrained problem, and the duality gap decreases as $m/t$, providing a precise measure of suboptimality[18]. The algorithm uses Newton's method to solve each barrier subproblem, then updates $t$ and repeats, with typical values of the update parameter around 10-20[18].

The computational complexity of barrier methods is polynomial in both the problem dimension and the desired precision, with the number of Newton iterations typically scaling logarithmically with the condition number and the desired accuracy[18]. This polynomial-time guarantee makes interior-point methods particularly attractive for portfolio problems where robustness is essential, even if they may not always be fastest for specific problem instances[18]. The method works well with condition numbers up to approximately 30, at which point the Newton method within each centering step begins to require many iterations, but remains practical for most portfolio problems[15].

Interior-point methods handle the duality gap in a particularly elegant fashion by maintaining feasible primal and dual iterates throughout the algorithm, allowing the duality gap to be computed directly at each iteration without additional subproblems[18]. This contrasts with some first-order methods where dual variables must be reconstructed from primal iterates, introducing additional approximation errors[12]. For interior-point methods, the duality gap serves not just as an optimality measure but also as an explicit stopping criterion with strong guarantees—the algorithm terminates once the duality gap falls below a specified threshold, guaranteeing that the current solution is within that tolerance of optimality[18].

## Second-Order Cone Programming and Structured Complexity Management

Second-order cone programming (SOCP) represents an important extension of convex portfolio optimization that enables efficient handling of robust portfolio constraints, risk models with multiple factors, and sophisticated risk measures[14][17][38][41]. The key insight of SOCP is that many non-trivial portfolio constraints—including constraints on systematic and specific risk, Value-at-Risk constraints, and tracking error constraints—can be formulated as second-order cone constraints, which interior-point methods can solve efficiently[14][17].

The structure of SOCP problems is particularly well-suited to portfolio optimization because it allows practitioners to formulate problems that would otherwise require nonlinear constraints in a way that preserves convexity and enables efficient solution[14][38]. For example, constraining portfolio volatility while minimizing tracking error—a common practical requirement—can be formulated as an SOCP problem where the volatility constraint appears as a second-order cone inequality[14][38]. Interior-point methods exploit the algebraic structure of second-order cones, using Euclidean Jordan algebras to develop efficient computational procedures that are substantially faster than generic nonlinear programming approaches[17].

The computational complexity of SOCP solvers scales better with problem dimension than would be expected from the raw dimension count because the special structure enables partial pivoting, sparse factorization, and other advanced techniques that generic convex solvers cannot exploit[17][38]. However, this advantage comes with the requirement that problem formulation respects the cone structure—constraints must be explicitly written in the second-order cone form to benefit from the specialized algorithms[14].

## High-Dimensional Portfolio Allocation and Scalability Challenges

High-dimensional portfolio optimization—problems with hundreds or thousands of assets—presents distinct scalability challenges that interact with the duality gap estimation and complexity tradeoff in important ways[3][36][39]. The primary computational bottleneck in high-dimensional portfolio optimization is typically not the iteration count of the optimization algorithm but rather the cost of each iteration, which depends on the need to form, factor, and solve linear systems involving the covariance matrix[3][36].

The covariance matrix estimation problem itself contributes substantially to the overall complexity in high dimensions[3]. Estimating a covariance matrix requires on the order of $p^2$ parameters where $p$ is the number of assets, and standard estimators are often ill-conditioned when the number of assets is comparable to or exceeds the number of historical observations[3]. This conditioning issue directly impacts solver efficiency because interior-point methods and other convex solvers depend critically on the condition number of systems formed during optimization[13].

A convex optimization approach to portfolio allocation addresses this challenge by reformulating the mean-variance problem to avoid explicit covariance matrix inversion[3]. Rather than directly inverting the ill-conditioned covariance matrix, these methods optimize over a transformation matrix $A$ such that portfolio weights are given by $w = A\mu$ where $\mu$ are expected returns, converting the problem into a least-squares framework where the conditioning is more favorable[3]. This reformulation maintains convexity while substantially improving numerical stability, demonstrating how problem reformulation can manage complexity even in high dimensions.

Coordinate descent methods provide another approach to high-dimensional portfolio optimization that manages complexity through sequential rather than simultaneous variable updates[33]. For risk parity portfolio problems—where each asset contributes equally to overall portfolio risk—cyclical coordinate descent achieves convergence even with dimensions exceeding 500 assets, with computational time measured in fractions of a second[33]. The key insight is that coordinate descent exploits the structure of individual asset updates, computing closed-form solutions for univariate problems that would require matrix operations in batch methods[33].

## Risk Measures and Duality in High-Dimensional Settings

The use of advanced risk measures in portfolio optimization—particularly conditional value-at-risk (CVaR) and Value-at-Risk (VaR)—introduces additional dimensions to the duality gap problem while remaining within the convex optimization framework[20][41]. These risk measures have the crucial advantage of being coherent (satisfying fundamental axioms for risk measures) and convex, enabling efficient optimization[20][41]. However, formulating optimization problems using these risk measures typically requires additional variables and constraints compared to simpler variance-based formulations.

For example, a portfolio optimization problem that minimizes CVaR subject to constraints on expected return introduces auxiliary variables representing portfolio loss scenarios and additional constraints for each scenario[20][41]. This scenario-based formulation increases the dimension of the optimization problem substantially—a CVaR problem with 100 assets and 1000 historical scenarios becomes a convex optimization problem with dimension exceeding 10000[20]. While the problem remains convex and thus maintains global optimality guarantees, the computational cost of interior-point methods scales unfavorably with this increased dimension.

Duality gap estimation in scenario-based risk optimization exploits the structure of the dual problem to manage complexity[41]. The dual variables in CVaR minimization problems correspond to scenario probabilities, and the dual problem becomes a risk-neutral optimization over scenario weights[41]. This duality structure allows for decomposition algorithms where the optimization problem is solved by iteratively optimizing over scenarios and assets in a coordinated fashion, rather than solving one large monolithic problem[41].

## Adaptive Methods and Algorithm Selection in High Dimensions

The practical resolution of the global convergence versus complexity tradeoff in high-dimensional portfolio optimization often involves using adaptive algorithms that select method components based on problem characteristics and iteration history[28][36][50]. Accelerated gradient methods with adaptive learning rates, such as algorithms incorporating Nesterov acceleration or momentum techniques, achieve convergence rates between standard gradient descent and full Newton methods[28][50]. These methods use past iteration information to accelerate progress toward optimality without requiring expensive Hessian computations[28].

The convergence behavior of accelerated first-order methods in portfolio optimization depends critically on whether the objective function is strongly convex[28]. For strongly convex portfolio problems—which includes most mean-variance formulations with appropriate regularization—accelerated methods achieve convergence rate $O(1/k^2)$ where $k$ is the iteration number[28]. This acceleration is particularly valuable in high dimensions where each iteration remains relatively inexpensive compared to Newton-based interior-point methods, while achieving comparable final convergence rates[28].

Variance-reduced stochastic optimization methods offer another approach to managing complexity in high-dimensional portfolio optimization[50][51]. These methods reduce the variance of stochastic gradient estimates through carefully designed correction terms, allowing the use of larger constant step sizes while maintaining convergence guarantees[50]. Algorithms such as SAGA, SVRG, and SAG achieve convergence rates comparable to full-batch gradient methods while requiring less total computational cost when the number of constraints or scenarios is very large[50].

## Duality Gap Bounds and Optimality Certification

The duality gap provides not just a stopping criterion but also a mechanism for certified optimality bounds in portfolio optimization[5][18][29]. At any iteration of the algorithm, the duality gap provides a provable upper bound on how far the current solution is from optimality, without requiring knowledge of the true optimal value. This property is particularly valuable in portfolio optimization where practitioners need to make investment decisions even when computational resources do not permit convergence to machine precision[5].

The relationship between duality gap magnitude and practical portfolio performance is direct—a duality gap of $\epsilon$ means that the expected return of the current portfolio is at most $\epsilon$ away from the best possible expected return achievable given the constraints, or equivalently, the risk is at most $\epsilon$ away from the minimum achievable risk[5]. This translates directly to economic value, making duality gap bounds economically meaningful quantities for portfolio managers[5].

However, computing tight duality gaps in high dimensions requires solving for explicit dual variables, which can amplify computational complexity[5]. The dual problem for a portfolio optimization problem with $p$ assets and $m$ constraints has dimension comparable to the sum of $p$ and $m$, and computing accurate dual solutions often requires computational cost similar to solving the primal problem[5]. The tradeoff between duality gap tightness and computational cost becomes acute in problems where computational resources are limited—loose dual bounds provide weak optimality guarantees, while tight dual bounds require substantial additional computation[5].

## Practical Implications for Portfolio Solver Design

The theoretical analysis reveals that portfolio optimization solvers must navigate a complex landscape of competing objectives[1][3][8]. Global convergence guarantees are guaranteed by convexity but depend on achieving sufficient numerical precision, which requires more iterations as problem conditioning worsens. Duality gap estimation provides powerful optimality bounds but adds computational overhead that scales with problem dimension and required precision. Local extrema escape becomes less relevant in convex settings but becomes important in practice through numerical issues and degenerate solutions[2].

The most practically effective approach combines structured problem formulations (exploiting second-order cone structure when available), adaptive algorithm selection (choosing between first-order, second-order, and coordinate descent methods based on problem characteristics), and approximate duality gap computation (using efficient dual estimates rather than exact dual solutions)[3][33][38]. This pragmatic approach sacrifices some theoretical purity but achieves substantially better practical performance than rigid adherence to any single optimization method[3].

Dimensional reduction and sparse reformulation represent crucial strategies for high-dimensional portfolio problems, allowing problems that would be computationally intractable with full-dimension methods to be solved efficiently[3][36]. Rather than directly optimizing over high-dimensional weight vectors, these methods optimize over lower-dimensional representations (such as factor loadings or transformed weights) that maintain the convexity of the original problem while improving conditioning and reducing computational cost[3][36].

## Conclusion

Convex optimization solvers used in portfolio algorithms successfully balance global convergence with practical computational efficiency through a combination of theoretical guarantees and algorithmic sophistication. The convexity of portfolio problems ensures that global convergence is theoretically guaranteed—any stationary point is optimal—eliminating the traditional tension with local extrema that plagues non-convex optimization. However, practical portfolio optimization requires careful management of duality gap estimation, problem conditioning, and algorithm selection to achieve competitive computational performance in high-dimensional settings.

The evidence from the literature demonstrates that duality gap estimation, while amplifying complexity in naive implementations, can be managed through structured problem formulations, adaptive algorithms, and dimension reduction techniques that maintain theoretical optimality guarantees while achieving practical scalability. Interior-point methods with polynomial-time guarantees, first-order accelerated methods exploiting problem structure, and coordinate descent methods exploiting decomposable problem structure all represent viable approaches, with algorithm choice depending on specific problem characteristics and computational constraints. The field has evolved beyond asking whether global convergence can be balanced with computational efficiency—the answer is decidedly affirmative—toward more nuanced questions about which algorithmic approaches best suit particular problem structures and practical constraints that real portfolio managers face.

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A First Order Method for Finding Minimal Norm ... - Optimization Online', 'url': 'https://optimization-online.org/2011/09/3176/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Duality Methods for Dynamic Portfolio Optimization with Constraints', 'url': 'https://mediatum.ub.tum.de/doc/1713633/0obow3uwrsv0p8hb74unkug1a.Dissertation_MK.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Convex Optimisation Approach to Portfolio Allocation', 'url': 'https://www.diva-portal.org/smash/get/diva2:1849045/FULLTEXT01.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Convex optimization - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Convex_optimization'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Evaluating Portfolio Policies: A Duality Approach - MIT', 'url': 'http://web.mit.edu/wangj/www/pap/HaughKoganWang06.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Volcano escape with Gradient Descent - Quantdare', 'url': 'https://quantdare.com/volcano-escape-with-gradient-descent/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Linear Convergence of the Primal-Dual Gradient Method for Convex ...', 'url': 'http://proceedings.mlr.press/v89/du19b/du19b.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Total Portfolio Approach Is Still a Human Framework', 'url': 'https://www.institutionalinvestor.com/article/total-portfolio-approach-still-human-framework-and-thats-problem'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A generalized Frank–Wolfe method with “dual averaging” for ...', 'url': 'https://dspace.mit.edu/bitstream/handle/1721.1/146364/11590_2022_Article_1951.pdf?sequence=1&isAllowed=y'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Stochastic Primal-Dual Splitting Algorithm with Variance ...', 'url': 'https://optimization-online.org/wp-content/uploads/2024/10/A-Stochastic-Primal-Dual-Splitting-Algorithm-with-Variance-Reduction-1.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': "Dimensional's Approach to Asset Allocation", 'url': 'https://www.dimensional.com/ie-en/insights/dimensionals-approach-to-asset-allocation'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Convergence rate analysis of primal-dual splitting schemes', 'url': 'https://ww3.math.ucla.edu/camreport/cam14-63.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'B.4 Interior-Point Methods | Portfolio Optimization - Bookdown', 'url': 'https://bookdown.org/palomar/portfoliooptimizationbook/B.4-IPM.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Robust portfolio optimization using second-order cone programming', 'url': 'https://booksite.elsevier.com/samplechapters/9780123749529/02~Chapter_1.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] 5. Convex optimization. II - Baruch MFE Program', 'url': 'https://mfe.baruch.cuny.edu/wp-content/uploads/2014/12/Opt_Lecture5_2019.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'End-To-End Resource Analysis for Quantum Interior-Point Methods ...', 'url': 'https://link.aps.org/doi/10.1103/PRXQuantum.4.040325'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Second-order cone programming - Department of Statistics', 'url': 'https://www.stat.uchicago.edu/~lekheng/courses/310w13/socp.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Barrier Method', 'url': 'https://www.stat.cmu.edu/~ryantibs/convexopt/lectures/barr-method.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Escaping Local Minima and Saddle Points in High-Dimensional Non ...', 'url': 'https://arxiv.org/html/2409.12604v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Stochastic Approach to Portfolio Optimization Using Competing ...', 'url': 'https://digitalcommons.bryant.edu/cgi/viewcontent.cgi?article=1041&context=honors_finance'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Proximal Method for Composite Optimization with Smooth ... - arXiv', 'url': 'https://arxiv.org/abs/2512.20602'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Identifying and attacking the saddle point problem in high ...', 'url': 'https://ganguli-gang.stanford.edu/pdf/14.SaddlePoint.NIPS.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Stochastic Portfolio Optimization - Diva-Portal.org', 'url': 'https://www.diva-portal.org/smash/get/diva2:1779355/FULLTEXT01.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Proximal Newton-type methods for convex optimization', 'url': 'https://web.stanford.edu/class/cme334/docs/2012-12-08-lee_sun_paper.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Accelerated gradient methods and dual decomposition in distributed ...', 'url': 'https://www.dcsc.tudelft.nl/~bdeschutter/pub/rep/12_011_bis.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] for Frank-Wolfe algorithms and Conditional Gradients', 'url': 'https://optimization-online.org/wp-content/uploads/2021/04/8340.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] On the Universality of Online Mirror Descent - Ambuj Tewari', 'url': 'https://www.ambujtewari.com/research/srebro11universality.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Lecture 9–10: Accelerated Gradient Descent', 'url': 'https://pages.cs.wisc.edu/~yudongchen/cs726_sp23/Lecture_9_10_accelerated_GD.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Conditional Gradient (Frank-Wolfe) Method', 'url': 'https://www.stat.cmu.edu/~ryantibs/convexopt-F15/lectures/24-cond-grad.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Distributed Mirror Descent for Online Composite Optimization - arXiv', 'url': 'https://arxiv.org/pdf/2004.00837.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Augmented Lagrangian Methods for Solving Optimization Problems ...', 'url': 'https://pubsonline.informs.org/doi/10.1287/opre.2016.1521'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Alternating Direction Method of Multipliers - Statistics & Data Science', 'url': 'https://www.stat.cmu.edu/~ryantibs/convexopt/lectures/admm.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Fast Algorithm for Computing High-dimensional Risk Parity ...', 'url': 'http://www.thierry-roncalli.com/download/CCD-Risk-Parity.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The Augmented Lagrangian Methods: Overview and Recent Advances', 'url': 'https://arxiv.org/pdf/2510.16827.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'ADMM', 'url': 'https://stanford.edu/~boyd/admm.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Fast Coordinate Descent Method for High-Dimensional Non ...', 'url': 'https://arxiv.org/html/2410.03014v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Robust portfolio optimization: a conic programming approach', 'url': 'https://www.doc.ic.ac.uk/~pp500/pubs/robustPortKai.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Robust portfolio optimization using second-order cone programming', 'url': 'https://booksite.elsevier.com/samplechapters/9780123749529/02~Chapter_1.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Quadratic Programming for Portfolio Optimization: Complete Guide ...', 'url': 'https://mbrenndoerfer.com/writing/quadratic-programming-portfolio-optimization'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Robust portfolio selection based on a joint ellipsoidal uncertainty set', 'url': 'https://zhaosong-lu.github.io/ResearchPapers/robport-OMS.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] PORTFOLIO OPTIMIZATION USING SECOND ORDER CONIC ...', 'url': 'https://scik.org/index.php/mfl/article/download/4435/2722'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Quadratic Programming for Portfolio Optimization Problems, Solver ...', 'url': 'https://www.mathworks.com/help/optim/ug/quadratic-programming-portfolio-optimization.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Nonsmooth Convex Optimization using the Specular Gradient ...', 'url': 'https://arxiv.org/html/2412.20747v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] ADVANCES IN CONVERGENCE AND SCOPE OF THE PROXIMAL ...', 'url': 'https://sites.math.washington.edu/~rtr/papers/rtr257-ConvergencePPA.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Sparse Regularization and Feature Selection - Emergent Mind', 'url': 'https://www.emergentmind.com/topics/sparse-regularization-and-feature-selection'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Lecture 7: February 4 7.1 Subgradient method', 'url': 'https://www.stat.cmu.edu/~ryantibs/convexopt-S15/scribes/07-sg-method-scribed.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Proximal Point Algorithm for Differentiable Quasi-Convex ...', 'url': 'https://www.pmf.ni.ac.rs/filomat-content/2020/34-7/34-7-20-11500.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Sparse Multi-Task Regression and Feature Selection to Identify ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4184284/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Online stochastic gradient descent on non-convex losses from high ...', 'url': 'https://www.jmlr.org/papers/volume22/20-1288/20-1288.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Stochastic Optimization Methods', 'url': 'https://www.cs.cmu.edu/~pradeepr/convexopt/Lecture_Slides/stochastic_optimization_methods.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Nesterov Accelerated Shuffling Gradient Method for Convex ...', 'url': 'https://proceedings.mlr.press/v162/tran22a/tran22a.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Statistical Guarantees for High-Dimensional Stochastic Gradient ...', 'url': 'https://arxiv.org/abs/2510.12013'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Stochastic Composite Optimization: Variance Reduction ...', 'url': 'https://lear.inrialpes.fr/people/mairal/resources/pdf/autrans2022.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Lecture 20: Momentum & Nesterov Acceleration', 'url': 'https://www.cs.cmu.edu/~mgormley/courses/10425/slides/lecture20-momen.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Randomized directional search for nonconvex optimization - arXiv', 'url': 'https://arxiv.org/html/2501.00469v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] arXiv:2205.12772v2 [math.NA] 11 Mar 2024', 'url': 'https://arxiv.org/pdf/2205.12772.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Introduction to Non-convex - Ioannis Panageas', 'url': 'https://panageas.github.io/_pages/nonconvex.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Role of Sparsity and Structure in the Optimization Landscape of Non ...', 'url': 'https://lavaei.ieor.berkeley.edu/KSP_2019_1.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The Gradient Method and Lyapunov Functions', 'url': 'https://users.ece.utexas.edu/~nikolova/papers/essay1.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Hessian Eigenspectra of More Realistic Nonlinear Models', 'url': 'https://www.stat.berkeley.edu/~mmahoney/pubs/hessian-more-realistic-models-neurips21.pdf'}}

## Sources
https://optimization-online.org/2011/09/3176/
https://mediatum.ub.tum.de/doc/1713633/0obow3uwrsv0p8hb74unkug1a.Dissertation_MK.pdf
https://www.diva-portal.org/smash/get/diva2:1849045/FULLTEXT01.pdf
https://en.wikipedia.org/wiki/Convex_optimization
http://web.mit.edu/wangj/www/pap/HaughKoganWang06.pdf
https://quantdare.com/volcano-escape-with-gradient-descent/
http://proceedings.mlr.press/v89/du19b/du19b.pdf
https://www.institutionalinvestor.com/article/total-portfolio-approach-still-human-framework-and-thats-problem
https://dspace.mit.edu/bitstream/handle/1721.1/146364/11590_2022_Article_1951.pdf?sequence=1&isAllowed=y
https://optimization-online.org/wp-content/uploads/2024/10/A-Stochastic-Primal-Dual-Splitting-Algorithm-with-Variance-Reduction-1.pdf
https://www.dimensional.com/ie-en/insights/dimensionals-approach-to-asset-allocation
https://ww3.math.ucla.edu/camreport/cam14-63.pdf
https://bookdown.org/palomar/portfoliooptimizationbook/B.4-IPM.html
https://booksite.elsevier.com/samplechapters/9780123749529/02~Chapter_1.pdf
https://mfe.baruch.cuny.edu/wp-content/uploads/2014/12/Opt_Lecture5_2019.pdf
https://link.aps.org/doi/10.1103/PRXQuantum.4.040325
https://www.stat.uchicago.edu/~lekheng/courses/310w13/socp.pdf
https://www.stat.cmu.edu/~ryantibs/convexopt/lectures/barr-method.pdf
https://arxiv.org/html/2409.12604v1
https://digitalcommons.bryant.edu/cgi/viewcontent.cgi?article=1041&context=honors_finance
https://arxiv.org/abs/2512.20602
https://ganguli-gang.stanford.edu/pdf/14.SaddlePoint.NIPS.pdf
https://www.diva-portal.org/smash/get/diva2:1779355/FULLTEXT01.pdf
https://web.stanford.edu/class/cme334/docs/2012-12-08-lee_sun_paper.pdf
https://www.dcsc.tudelft.nl/~bdeschutter/pub/rep/12_011_bis.pdf
https://optimization-online.org/wp-content/uploads/2021/04/8340.pdf
https://www.ambujtewari.com/research/srebro11universality.pdf
https://pages.cs.wisc.edu/~yudongchen/cs726_sp23/Lecture_9_10_accelerated_GD.pdf
https://www.stat.cmu.edu/~ryantibs/convexopt-F15/lectures/24-cond-grad.pdf
https://arxiv.org/pdf/2004.00837.pdf
https://pubsonline.informs.org/doi/10.1287/opre.2016.1521
https://www.stat.cmu.edu/~ryantibs/convexopt/lectures/admm.pdf
http://www.thierry-roncalli.com/download/CCD-Risk-Parity.pdf
https://arxiv.org/pdf/2510.16827.pdf
https://stanford.edu/~boyd/admm.html
https://arxiv.org/html/2410.03014v1
https://www.doc.ic.ac.uk/~pp500/pubs/robustPortKai.pdf
https://booksite.elsevier.com/samplechapters/9780123749529/02~Chapter_1.pdf
https://mbrenndoerfer.com/writing/quadratic-programming-portfolio-optimization
https://zhaosong-lu.github.io/ResearchPapers/robport-OMS.pdf
https://scik.org/index.php/mfl/article/download/4435/2722
https://www.mathworks.com/help/optim/ug/quadratic-programming-portfolio-optimization.html
https://arxiv.org/html/2412.20747v1
https://sites.math.washington.edu/~rtr/papers/rtr257-ConvergencePPA.pdf
https://www.emergentmind.com/topics/sparse-regularization-and-feature-selection
https://www.stat.cmu.edu/~ryantibs/convexopt-S15/scribes/07-sg-method-scribed.pdf
https://www.pmf.ni.ac.rs/filomat-content/2020/34-7/34-7-20-11500.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC4184284/
https://www.jmlr.org/papers/volume22/20-1288/20-1288.pdf
https://www.cs.cmu.edu/~pradeepr/convexopt/Lecture_Slides/stochastic_optimization_methods.pdf
https://proceedings.mlr.press/v162/tran22a/tran22a.pdf
https://arxiv.org/abs/2510.12013
https://lear.inrialpes.fr/people/mairal/resources/pdf/autrans2022.pdf
https://www.cs.cmu.edu/~mgormley/courses/10425/slides/lecture20-momen.pdf
https://arxiv.org/html/2501.00469v1
https://arxiv.org/pdf/2205.12772.pdf
https://panageas.github.io/_pages/nonconvex.pdf
https://lavaei.ieor.berkeley.edu/KSP_2019_1.pdf
https://users.ece.utexas.edu/~nikolova/papers/essay1.pdf
https://www.stat.berkeley.edu/~mmahoney/pubs/hessian-more-realistic-models-neurips21.pdf