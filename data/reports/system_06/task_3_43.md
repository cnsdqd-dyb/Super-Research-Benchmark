# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** da0ea615 | **Time:** 161.49s | **Cost:** $0.12571
--------------------------------------------------------------------------------

# The Effect of Network Flow Assignment Convergence on Model Complexity Under Elastic Demand

## Abstract

This research report examines the intricate relationship between network flow assignment convergence and model complexity in the context of elastic demand traffic assignment models. Elastic demand traffic assignment represents a significant advancement over fixed-demand models by incorporating the fundamental principle that travel demand responds dynamically to changing network conditions, particularly travel times and costs. The convergence behavior of solution algorithms directly influences computational complexity, solution accuracy, and the practical applicability of these models to large-scale transportation networks. This analysis synthesizes recent methodological developments, algorithmic innovations, and theoretical foundations to provide a comprehensive understanding of how convergence properties affect model complexity under elastic demand conditions. The findings reveal that convergence behavior is not merely a technical concern but a fundamental determinant of model tractability, computational efficiency, and the ability to capture realistic traveler behavior in transportation systems.

## 1. Introduction

### 1.1 Background and Motivation

Traffic assignment models serve as essential tools for transportation system analysis, enabling planners and engineers to understand and predict travel behavior under various network conditions. The classical user equilibrium paradigm, rooted in Wardrop's first principle, assumes that travelers choose routes that minimize their individual travel costs, resulting in a state where no traveler can reduce their travel time by unilaterally changing routes [1]. However, this foundational framework traditionally assumes fixed origin-destination (O-D) demand, which fails to capture the dynamic nature of travel decision-making in response to changing network conditions.

Elastic demand traffic assignment addresses this limitation by explicitly modeling the relationship between travel demand and the level of service provided by the transportation network. In elastic demand models, the O-D demand is not predetermined but rather emerges endogenously as a function of travel times, costs, and other factors that influence travelers' decisions [2]. This formulation introduces additional complexity into the traffic assignment problem, as the demand-supply interaction creates a coupled system where changes in network flow affect travel times, which in turn influence demand levels, ultimately feeding back into the network flow distribution.

The introduction of elastic demand transforms the traffic assignment problem from a relatively straightforward optimization problem into a more complex equilibrium problem that requires simultaneous consideration of route choice behavior and demand generation. As noted by researchers in the field, elastic demand traffic assignment has been extensively studied in the context of single-criterion optimization, yet the bi-criteria and multi-dimensional continuous distribution cases remain significantly underexplored [1]. This lack of progress can be attributed largely to the inherent complexity of these formulations, which involves infinite numbers of user classes and requires specifying endogenously determined travel demands characterized by elastic generalized travel time from continuous distributions.

### 1.2 Research Objectives and Scope

This report aims to provide a comprehensive analysis of how network flow assignment convergence affects model complexity under elastic demand conditions. The specific objectives include examining the theoretical foundations of convergence in elastic demand traffic assignment, analyzing the computational implications of different convergence behaviors, evaluating the performance of various solution algorithms, and identifying key factors that influence the trade-off between convergence quality and computational complexity. The scope encompasses both static and dynamic traffic assignment frameworks, with particular emphasis on the methodological advances that have addressed convergence challenges in elastic demand models.

## 2. Theoretical Foundations of Elastic Demand Traffic Assignment

### 2.1 Mathematical Formulation

The elastic demand traffic assignment problem can be formulated as a mathematical program with equilibrium constraints, where the objective function typically minimizes the sum of path costs weighted by path flows, subject to flow conservation constraints, non-negativity constraints, and demand functions that relate O-D demand to travel costs [3]. Mathematically, the problem can be expressed as finding flows that satisfy the user equilibrium conditions while simultaneously satisfying the demand functions:

$$
\min_{h} \sum_{a \in A} \int_0^{x_a} t_a(\omega) d\omega
$$

subject to:

$$
\sum_{k \in K_{rs}} h_k^{rs} = D_{rs}(c_{rs}), \quad \forall rs
$$

$$
x_a = \sum_{rs} \sum_{k \in K_{rs}} h_k^{rs} \delta_{ak}^{rs}, \quad \forall a
$$

$$
h_k^{rs} \geq 0, \quad \forall k, rs
$$

where $h_k^{rs}$ represents the flow on path $k$ connecting O-D pair $rs$, $D_{rs}(\cdot)$ is the demand function for pair $rs$, $c_{rs}$ is the minimum travel cost for pair $rs$, $x_a$ is the flow on link $a$, and $\delta_{ak}^{rs}$ is the link-path incidence indicator.

The demand functions $D_{rs}(\cdot)$ are typically specified as decreasing functions of travel cost, reflecting the economic principle that higher costs lead to lower demand. Common functional forms include exponential, logit-based, and linear demand functions, each with different implications for the mathematical properties of the resulting equilibrium problem [4].

### 2.2 The External Equilibrium Loop

A distinguishing feature of elastic demand traffic assignment is the presence of an external equilibrium loop that iterates between the demand model and the assignment model [5]. This iteration scheme arises because the demand depends on travel times, which depend on link flows, which in turn depend on the demand levels. The external loop can be conceptualized as:

$$
\text{Demand Model} \leftrightarrow \text{Assignment Model}
$$

where the demand model takes travel times as inputs and produces demand levels, while the assignment model takes demand levels as inputs and produces travel times. The convergence of this external loop is crucial for obtaining meaningful equilibrium solutions.

The complexity of this iteration scheme stems from the fact that increasing demand causes disproportionately increasing travel times, which in turn reduce demand, creating a feedback loop that may exhibit unstable behavior [5]. The method of repeated approximations (MRA), which essentially implements a simple iteration scheme where level-of-service variables are fed directly to the route-choice model and vice versa, may exhibit unstable patterns and lead to cyclic solutions. The contraction region, defined as the region for which a starting solution will render stable convergence, depends on the slopes of the demand and supply curves. Generally, as the slopes between the curves increase, the contraction region shrinks, making convergence more difficult to achieve.

### 2.3 Convergence Criteria and Mathematical Properties

The convergence analysis of elastic demand traffic assignment algorithms relies heavily on mathematical properties such as Lipschitz continuity, monotonicity, and strong monotonicity [6]. Lipschitz continuity ensures that the demand functional changes at a bounded rate in response to changes in travel times, which is essential for establishing convergence guarantees. The demand functional $Q(h)$ is guaranteed to satisfy Lipschitz continuity by virtue of the specific structure of typical demand functions.

Strong monotonicity of the demand functions along the trajectory of computed demands is another critical property that enables convergence proofs [6]. When demand functions are strongly monotone decreasing, the iterative algorithms can be shown to converge to the unique equilibrium solution under appropriate conditions. This property is particularly important in dynamic traffic assignment contexts, where the time-dependent nature of flows and demands introduces additional complexity into the convergence analysis.

The convergence criteria that have appeared in the technical literature encompass various mathematical properties, including Lipschitz continuous (LC), monotone (M), strongly monotone (SM), pseudomonotone (PM), semi-strictly quasimonotone (SSQM), and mixed strongly-weakly monotone (MSWM) conditions [6]. These properties provide the theoretical foundation for establishing convergence results for different classes of algorithms applied to elastic demand traffic assignment problems.

## 3. Algorithmic Approaches and Convergence Behavior

### 3.1 Link-Based Algorithms

Link-based algorithms operate directly on link flows rather than path flows, making them computationally efficient for large-scale networks but potentially sacrificing some precision in the solution. The two primary link-based algorithms used in traffic assignment are the Method of Successive Averages (MSA) and the Frank-Wolfe algorithm.

The Method of Successive Averages represents one of the earliest and most widely used approaches for solving traffic assignment problems with elastic demand. Originally suggested by Leurent for elastic demand continuous bi-criteria traffic assignment (ED-CBiTA), MSA provides a straightforward iterative scheme that averages successive solutions to approach the equilibrium [1]. The convergence of MSA under fairly weak regularity conditions was established in the foundational work of Robbins and Monro on stochastic approximation [5]. However, MSA is known to exhibit sluggish convergence behavior, particularly in achieving high-precision equilibrium solutions. Experimental results indicate that MSA typically achieves relative gaps around $10^{-4}$, which may be insufficient for applications requiring high accuracy [1].

The Frank-Wolfe algorithm, also known as the decomposition method, offers an alternative approach with stronger theoretical foundations. The convergence of the Frank-Wolfe algorithm is sublinear in general: the error in the objective function to the optimum is $O(1/k)$ after $k$ iterations, provided that the gradient is Lipschitz continuous with respect to some norm [7]. This convergence rate means that achieving high-precision solutions requires increasingly large numbers of iterations, leading to substantial computational costs for large-scale networks. Experimental evaluations show that Frank-Wolfe can achieve relative gaps around $10^{-6}$ in many networks, which represents an improvement over MSA but still falls short of the precision achievable with more sophisticated algorithms [1].

The sublinear convergence rate of Frank-Wolfe has significant implications for model complexity under elastic demand. As the algorithm approaches the equilibrium solution, each additional iteration yields diminishing improvements, meaning that computational resources must increase superlinearly to achieve higher precision. This behavior is particularly problematic in elastic demand models, where each iteration of the external loop requires solving a complete assignment problem, multiplying the computational burden.

### 3.2 Path-Based Algorithms

Path-based algorithms operate on path flows directly, which allows for more precise representation of the solution but requires managing potentially large numbers of paths. The gradient projection algorithm and its variants represent the primary path-based approaches used in traffic assignment.

The Two-Stage Gradient Projection (TSGP) algorithm represents a significant advancement in path-based methods for elastic demand traffic assignment [1]. TSGP employs a two-stage structure that separates the optimization over path flows for each O-D pair from the overall convergence assessment. The first stage solves the assignment subproblem for each O-D pair, while the second stage assesses convergence and adjusts the overall solution. This decomposition allows for more efficient handling of the complexity introduced by elastic demand.

Experimental results on six networks demonstrate the superiority of TSGP in achieving high-precision equilibrium solutions [1]. While Frank-Wolfe and MSA struggle to achieve relative gaps better than $10^{-6}$ and $10^{-4}$ respectively, TSGP is able to attain relative gaps of $10^{-12}$ for all tested networks. This dramatic improvement in convergence behavior has profound implications for model complexity, as fewer iterations are needed to achieve a given level of precision, reducing both computational time and memory requirements.

The convergence indicator used in TSGP for each O-D pair is defined as:

$$
\Delta_{rs} = 1 - \frac{D_{rs}(T_{rs})}{\bar{q}_{rs} - e_{rs}}
$$

which measures the relative demand differences for O-D pair $rs$ [1]. This indicator allows the algorithm to assess convergence at a finer granularity, ensuring that all O-D pairs achieve similar precision levels rather than allowing some pairs to dominate the overall convergence measure.

### 3.3 Parallel Computing Frameworks

The increasing size of transportation networks and the computational demands of high-precision convergence have motivated the development of parallel computing approaches to traffic assignment. The Alternating Direction Method of Multipliers (ADMM) has emerged as a promising framework for parallel traffic assignment, offering a balance between convergence rate and additional communication costs [2].

The ADMM-JOR algorithm incorporates insights from the Jacobi over-relaxation iteration method into the ADMM framework, improving the convergence rate by utilizing more information during the iteration process [2]. The convergence of ADMM-JOR has been rigorously proven under an analytic framework of contractive-type methods. Furthermore, an adaptive strategy for adjusting the relaxation factor, guided by the principle of objective function value decline, aims to further improve convergence performance with minimal additional computational cost in a fully parallel setting.

Numerical experiments indicate that ADMM-JOR significantly reduces computation time while retaining the excellent parallel performance of the original ADMM method and significantly improving its convergence rate [2]. This improvement is particularly valuable for elastic demand models, where the external loop already imposes substantial computational overhead. The parallel implementation allows the internal iterations to be distributed across multiple processors, mitigating the impact of the additional complexity introduced by elastic demand.

The Dynamic Block Reduction (DBR) strategy represents another innovation in parallel traffic assignment [2]. DBR adaptively adjusts the number of O-D pairs within each block throughout the iterative process, addressing the observation that convergence behavior becomes unstable as the algorithm approaches high-precision solutions, exhibiting significant oscillations. Two parameter selection methods for DBR have been investigated: a fixed-parameter scheme and a self-adaptive scheme based on the Armijo rule. Numerical experiments demonstrate that the OpenMP-based DBR-PBCD algorithm significantly enhances convergence efficiency compared to existing algorithms, particularly for large-scale traffic assignment instances in urban transportation networks.

## 4. Impact of Convergence on Model Complexity

### 4.1 Computational Burden and Network Size

The relationship between convergence behavior and model complexity is most evident in the context of computational burden as a function of network size. As networks grow larger, the number of links, nodes, and O-D pairs increases, leading to larger optimization problems and more complex convergence behavior. The network size and saturation level have been shown to have a significant impact on the performance of solution algorithms for traffic assignment problems [8].

In elastic demand models, the computational burden is compounded by the external equilibrium loop, which requires solving the assignment problem multiple times within each outer iteration. As noted in the literature, the external equilibrium loop involves running a complete assignment model combined with a complete demand model, making iterations much more costly than for the inner loop [5]. This does not justify simple iteration schemes for the sake of simplicity, as only three to eight iterations may be possible in practice for large networks.

The complexity of ED-CBiTA itself presents a significant challenge, as the problem involves an infinite number of user classes and requires specifying endogenously determined travel demands characterized by elastic generalized travel time from a continuous distribution [1]. This infinite-dimensional nature of the problem necessitates discretization or approximation techniques that introduce additional computational overhead and potential convergence issues.

### 4.2 Convergence Rate and Solution Quality

The convergence rate of an algorithm directly affects the trade-off between solution quality and computational complexity. Algorithms with faster convergence rates can achieve high-precision solutions with fewer iterations, reducing both computational time and memory requirements. However, faster convergence often comes at the cost of increased per-iteration complexity or more stringent requirements on the problem structure.

The Frank-Wolfe algorithm's sublinear convergence rate of $O(1/k)$ means that achieving a precision of $\epsilon$ requires approximately $O(1/\epsilon)$ iterations [7]. For elastic demand models, where each iteration involves solving a complete assignment problem, this translates to substantial computational costs for high-precision solutions. In contrast, algorithms like TSGP that achieve faster convergence rates can reach the same precision with significantly fewer iterations, reducing the overall computational burden.

The convergence behavior of algorithms becomes particularly important when approaching high-precision solutions. Some algorithms exhibit oscillatory behavior as they approach convergence, with the solution alternating between values on either side of the true equilibrium [2]. This instability can make it difficult to determine when convergence has been achieved and may require additional iterations or more sophisticated convergence criteria to ensure solution quality.

### 4.3 Memory Requirements and Working Path Sets

Model complexity under elastic demand is not solely a function of computational time but also encompasses memory requirements related to path storage and management. Path-based algorithms must maintain and update path flows for potentially thousands of paths in large networks, leading to substantial memory consumption.

The comparison between continuous multi-class traffic assignment (CMBTA) and discrete multi-class traffic assignment (DMBTA) models provides insight into the memory implications of different modeling approaches [2]. In all test networks, the CMBTA model requires CPU time comparable to the DMBTA model with five classes while maintaining a working path set smaller than that of the DMBTA model with three classes. This demonstrates that the CMBTA model can achieve refined solutions with modest computational time and memory requirements, suggesting that continuous formulations may offer advantages in terms of the convergence-complexity trade-off.

The working path set size is particularly important for elastic demand models, where the demand function may generate path flows for a broader range of paths as travelers with different value-of-time distributions consider various route options. Maintaining a compact yet representative path set is essential for computational efficiency while preserving the ability to capture the full range of traveler behavior.

### 4.4 Discrete vs. Continuous Model Formulations

The choice between discrete and continuous model formulations has significant implications for convergence behavior and model complexity. Discrete multi-class models discretize the continuous distribution of traveler characteristics into a finite number of classes, each with homogeneous preferences and behavior. While this approach simplifies the mathematical structure of the problem, it introduces approximation errors that depend on the number of classes used.

Extensive numerical experiments show that the equilibrium flow of the DMBTA model will fluctuate when the number of classes is small, and it will converge to the equilibrium flow of the CMBTA model with the increase in the number of classes [2]. This convergence behavior suggests that discrete models can approximate continuous models arbitrarily well given sufficient classes, but the computational cost increases with the number of classes.

The trade-off between model accuracy and computational complexity in discrete vs. continuous formulations highlights the fundamental tension in elastic demand traffic assignment. Continuous formulations capture the full heterogeneity of traveler preferences but require sophisticated numerical methods to handle the infinite-dimensional nature of the problem. Discrete formulations simplify the problem but require careful selection of class definitions and may require many classes to achieve acceptable accuracy.

## 5. Factors Influencing Convergence-Complexity Trade-offs

### 5.1 Demand Function Characteristics

The mathematical properties of demand functions significantly influence convergence behavior and model complexity. Demand functions that are strongly monotone decreasing exhibit more favorable convergence properties than those with flatter response curves [6]. The slope of the demand function affects the contraction region for the external loop, with steeper slopes leading to smaller contraction regions and more challenging convergence conditions.

The choice of demand function form also affects the Lipschitz continuity properties of the problem, which in turn influence the convergence rates of iterative algorithms. Demand functions with bounded derivatives ensure Lipschitz continuity, enabling the application of convergence proofs based on standard assumptions. However, some economically reasonable demand function specifications may violate these conditions, leading to potential convergence difficulties.

The sensitivity of demand to travel time variations, often measured through the elasticity of demand, affects the strength of the feedback between the assignment and demand models. Higher elasticity means that demand responds more strongly to changes in travel time, potentially leading to more pronounced oscillations in the external loop and requiring more sophisticated solution methods to achieve convergence.

### 5.2 Network Characteristics and Topology

The topology and characteristics of the transportation network influence convergence behavior through their effects on the structure of the traffic assignment problem. Networks with many alternative paths and complex connectivity may exhibit more complex convergence behavior than simpler networks with limited routing options.

The saturation level of the network, which reflects the relationship between demand and capacity, affects both the computational difficulty of the assignment problem and the convergence behavior of solution algorithms [8]. Highly congested networks with saturated links exhibit more nonlinear behavior, which can challenge convergence algorithms and require more iterations to achieve high-precision solutions.

Link performance functions, which map link flows to travel times, play a crucial role in determining the mathematical structure of the traffic assignment problem. These functions are typically assumed to be nonnegative, nondecreasing, and convex, reflecting the idea that as more vehicles attempt to drive on a link, the greater the congestion and the higher the travel times will be [3]. The Bureau of Public Roads (BPR) function represents the most popular specification, but alternative forms may have different implications for convergence behavior.

### 5.3 Algorithmic Parameters and Initialization

The performance of traffic assignment algorithms is sensitive to parameter choices and initial conditions. The initial assignment and step size at the beginning of the outer loop have a significant impact on the final solution and convergence speed of the algorithm [8]. Poor initialization can lead to slow convergence or convergence to suboptimal solutions, while well-chosen initial conditions can substantially reduce computational requirements.

Step size rules in iterative algorithms affect the balance between convergence speed and solution stability. Aggressive step sizes may accelerate initial convergence but risk overshooting the equilibrium and causing oscillations, while conservative step sizes ensure stability at the cost of slower convergence. Adaptive step size strategies that adjust based on the current state of the algorithm can help balance these competing concerns.

The maximum number of iterations and convergence tolerance parameters define the stopping criteria for algorithms and directly affect the trade-off between solution quality and computational cost. Lower tolerance values require more iterations but yield more precise solutions, while higher tolerances allow faster computation at the cost of solution accuracy. The appropriate choice of these parameters depends on the specific application requirements and the computational resources available.

## 6. Methodological Advances and Best Practices

### 6.1 Convergence Enhancement Techniques

Various techniques have been developed to enhance convergence behavior in elastic demand traffic assignment. The Method of Successive Averages remains popular due to its simplicity and robustness, though its slow convergence rate limits its applicability for high-precision solutions [5]. More sophisticated averaging schemes and step size rules have been proposed to improve upon the basic MSA approach.

Relaxation techniques, which combine the current iterate with previous iterates or auxiliary solutions, can accelerate convergence in some cases. The ADMM-JOR algorithm incorporates relaxation through its Jacobi over-relaxation iteration method, achieving improved convergence rates while maintaining parallel efficiency [2]. The adaptive relaxation factor adjustment strategy, guided by the principle of objective function value decline, further enhances performance with minimal additional computational cost.

Decomposition techniques that exploit the structure of the traffic assignment problem can reduce computational complexity while maintaining convergence guarantees. Exact decomposition techniques have been proposed for both static and dynamic traffic assignment problems to reduce computational complexity [8]. These methods exploit the separable structure of the problem to solve smaller subproblems that can be combined to obtain the overall solution.

### 6.2 Hybrid and Multi-Stage Approaches

Hybrid approaches that combine the strengths of different algorithmic frameworks have shown promise for addressing the convergence challenges in elastic demand traffic assignment. The Two-Stage Gradient Projection algorithm represents one such hybrid approach, combining efficient O-D pair-level optimization with global convergence assessment [1].

Multi-stage solution strategies that progressively refine the solution can balance computational efficiency with solution quality. Initial stages may use faster, lower-precision algorithms to obtain a good starting point, followed by more precise algorithms that converge quickly from the improved initial condition. This approach leverages the observation that convergence is often faster when starting from a good initial estimate.

The combination of probabilistic approaches with deterministic refinement has also shown effectiveness. The probabilistic approach without step size initialization appears in many cases as the best algorithm, and combining this with keep solution initialization further improves performance [8]. The alternative method to initialize the assignment pattern at the beginning of the outer loop improves the performance of all swapping algorithms compared to recent methodologies in the literature.

### 6.3 Practical Recommendations for Implementation

Based on the analysis of convergence behavior and model complexity, several practical recommendations can be offered for implementing elastic demand traffic assignment models. First, the choice of algorithm should be guided by the required solution precision and available computational resources. For applications requiring high-precision solutions, path-based algorithms like TSGP are preferable despite their higher per-iteration complexity, as their faster convergence rates reduce overall computational requirements.

Second, careful attention should be paid to the initialization of the algorithm. Starting from a good initial estimate, such as an all-or-nothing assignment or a solution from a related problem, can substantially reduce the number of iterations required for convergence. The initial step size should be chosen to balance aggressive progress with stability, with subsequent adjustment based on observed convergence behavior.

Third, the external loop convergence should be monitored carefully, with appropriate action taken if unstable behavior is observed. Techniques such as damping, where the update to demand is scaled back from the full computed change, can help stabilize the external loop when convergence difficulties arise. The contraction region should be assessed based on the slopes of the demand and supply curves, with more conservative iteration schemes employed when the contraction region is small.

## 7. Future Research Directions

### 7.1 Algorithmic Developments

Future research should continue to develop algorithms that improve the convergence-complexity trade-off in elastic demand traffic assignment. The development of algorithms with linear or faster convergence rates for general elastic demand problems remains an open challenge. Such algorithms would dramatically reduce computational requirements for large-scale applications and enable more sophisticated modeling of traveler behavior.

The integration of machine learning techniques with traditional optimization methods represents a promising direction for improving convergence behavior. Neural networks trained to predict good step sizes or initial solutions could accelerate convergence while maintaining solution quality. Similarly, reinforcement learning approaches could be used to adaptively adjust algorithmic parameters based on problem characteristics and current convergence status.

Parallel and distributed computing approaches should continue to be developed and refined. The success of ADMM-JOR and DBR strategies demonstrates the potential for parallel computing to address the computational challenges of elastic demand traffic assignment. Future work should explore GPU computing, distributed memory parallelism, and cloud computing approaches to further scale solution capabilities.

### 7.2 Model Extensions

The extension of elastic demand models to incorporate additional criteria of concern to travelers represents an important research direction. Travel time reliability, comfort, and environmental impacts are increasingly important factors in travel decision-making, and models that incorporate these dimensions require more complex solution methods [1]. The continuous multi-criteria traffic assignment problem with joint two-dimensional continuous distributions presents significant computational challenges that must be addressed through algorithmic innovation.

The integration of elastic demand models with dynamic traffic assignment frameworks offers opportunities for more realistic modeling of time-dependent travel behavior. Dynamic models must account for the temporal evolution of flows, queues, and travel times, adding additional complexity to the convergence analysis. The development of efficient solution methods for dynamic elastic demand models remains an active area of research.

Stochastic and robust optimization approaches to elastic demand traffic assignment can address the uncertainty inherent in travel demand and network conditions. These approaches typically require more computational resources than deterministic models but can provide more reliable solutions for planning and operations applications. The development of efficient algorithms for stochastic elastic demand traffic assignment is an important direction for future research.

## 8. Conclusion

The effect of network flow assignment convergence on model complexity under elastic demand is a multifaceted issue that encompasses theoretical foundations, algorithmic implementations, and practical computational considerations. The analysis presented in this report reveals that convergence behavior is not merely a technical detail but a fundamental determinant of model tractability and practical applicability.

Elastic demand traffic assignment introduces complexity through the external equilibrium loop that iterates between demand and assignment models. This coupling creates feedback effects that can lead to convergence difficulties, particularly when demand functions exhibit steep response curves or when networks are highly congested. The computational burden of the external loop, combined with the internal convergence requirements of the assignment subproblem, creates a challenging optimization landscape that tests the limits of current solution methods.

The comparison of algorithmic approaches demonstrates that convergence rate is a critical factor in managing model complexity. While link-based algorithms like Frank-Wolfe and MSA offer simplicity and robustness, their sublinear convergence rates limit their ability to achieve high-precision solutions efficiently. Path-based algorithms like TSGP achieve dramatically faster convergence, enabling high-precision solutions with modest computational resources. Parallel computing frameworks such as ADMM-JOR further extend solution capabilities by distributing computational load across multiple processors.

The choice between discrete and continuous model formulations involves trade-offs between implementation complexity and solution accuracy. Continuous formulations capture the full heterogeneity of traveler preferences but require sophisticated numerical methods, while discrete formulations simplify the problem but require careful class definition and may require many classes for acceptable accuracy. The observation that discrete model equilibrium flows converge to continuous model equilibrium flows as the number of classes increases provides a theoretical foundation for practical implementations.

Future research should focus on developing algorithms with faster convergence rates, integrating machine learning techniques with optimization methods, and extending models to incorporate additional traveler preferences and uncertainties. As transportation systems become increasingly complex and the demands for accurate modeling grow, addressing the convergence-complexity trade-off in elastic demand traffic assignment will remain a critical challenge for the transportation research community.

The findings of this report underscore the importance of careful algorithm selection, parameter tuning, and initialization strategies in managing model complexity under elastic demand. By understanding the relationship between convergence behavior and computational requirements, practitioners can make informed decisions about model formulation and solution methods, ultimately enabling more accurate and efficient transportation system analysis.

## References

[1] Xu, H.-K. Elastic-demand Bi-criteria Traffic Assignment: Methodology and Computation. Hong Kong Polytechnic University Repository. https://ira.lib.polyu.edu.hk/bitstream/10397/106655/1/Xu_Elastic-demand_Bi-criteria_Traffic.pdf

[2] Transportation Research Part B: Methodological. Parallel computing framework for deterministic user equilibrium traffic assignment problem. Elsevier ScienceDirect. https://www.sciencedirect.com/science/article/abs/pii/S1366554524000152

[3] Boyles, S. D. Transportation Network Modeling. https://sboyles.github.io/book082.pdf

[4] Friesz, T. L., Han, K., & Bagherzadeh, A. Convergence of fixed-point algorithms for elastic demand dynamic user equilibrium. Transportation Research Part B: Methodological, 150, 336-352.

[5] DTU Orbit. System Convergence in Transport Modelling. https://backend.orbit.dtu.dk/ws/files/119086056/system_convergence_in_transport_modelling.pdf

[6] NSF PAR. Convergence of fixed-point algorithms for elastic demand dynamic user equilibrium. https://par.nsf.gov/servlets/purl/10300724

[7] Wikipedia. Frank-Wolfe algorithm. https://en.wikipedia.org/wiki/Frank%E2%80%93Wolfe_algorithm

[8] HAL Archives. Convergence algorithms for traffic assignment. https://hal.science/hal-02380851/file/doc00031093.pdf

## Annotations


## Sources
[1] https://backend.orbit.dtu.dk/ws/files/110657411/2015_03_04.pdf
[2] https://backend.orbit.dtu.dk/ws/files/119086056/system_convergence_in_transport_modelling.pdf
[3] https://en.wikipedia.org/wiki/Frank%E2%80%93Wolfe_algorithm
[4] https://hal.science/hal-02380851/file/doc00031093.pdf
[5] https://hanbaeklee.github.io/Webpage/Lee_AggRepTrans_2024.pdf
[6] https://ira.lib.polyu.edu.hk/bitstream/10397/106655/1/Xu_Elastic-demand_Bi-criteria_Traffic.pdf
[7] https://onlinepubs.trb.org/Onlinepubs/trr/1989/1220/1220-003.pdf
[8] https://par.nsf.gov/servlets/purl/10300724
[9] https://publications.polymtl.ca/9122/1/2021_GretaLaage.pdf
[10] https://sboyles.github.io/book082.pdf
[11] https://sboyles.github.io/teaching/ce392c/9-pathbased.pdf
[12] https://theses.hal.science/tel-02156187v1/file/Mariotte_PhD_thesis_2018.pdf
[13] https://www.ifaamas.org/Proceedings/aamas2025/pdfs/p352.pdf
[14] https://www.ptvgroup.com/en-us/application-areas/transportation-modeling
[15] https://www.sciencedirect.com/science/article/abs/pii/S0191261525000979
[16] https://www.sciencedirect.com/science/article/abs/pii/S1366554524000152
[17] https://www.sciencedirect.com/science/article/pii/S2772424723000197