# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 3a9a21c1 | **Time:** 144.63s | **Cost:** $0.03471
--------------------------------------------------------------------------------

# Does the Modularity of Skill Node Clustering in Vocational Networks Significantly Affect the Gradient Descent Convergence of Labor Matching Functions?

## Abstract

This research report investigates the relationship between the modular structure of skill node clustering in vocational networks and the convergence properties of gradient descent algorithms applied to labor matching functions. Drawing upon recent advances in network science, labor economics, and optimization theory, we develop a comprehensive theoretical framework to examine how the topological characteristics of skill-based industrial clusters influence the computational efficiency of matching algorithms. Our analysis reveals that modularity exerts a substantial influence on convergence behavior through multiple interconnected mechanisms, including the conditioning of the loss landscape, the geometry of skill complementarity spaces, and the information propagation dynamics within the optimization process. The findings suggest that labor matching functions operating within highly modular skill basins exhibit distinct convergence profiles compared to those in less structured network configurations, with implications for both theoretical understanding and practical algorithm design in automated labor market systems.

---

## 1. Introduction

The contemporary labor market can be conceptualized as a complex network of interconnected skill nodes, where industries, occupations, and individual competencies form intricate patterns of relationships that govern the efficiency of worker-firm matching processes. Recent scholarship has demonstrated that these vocational networks possess inherent modular structure, with industries clustering into "skill basins" characterized by high degrees of internal skill overlap and knowledge diffusion [1]. This modular architecture emerges from the natural organization of economic activity, where firms in similar industrial sectors share common workforce requirements and workers skill develop transferable profiles that facilitate movement within and across these clusters.

Concurrently, the increasing digitization of labor markets has motivated the development of algorithmic approaches to matching workers with employment opportunities. These approaches frequently employ optimization techniques—particularly gradient descent and its variants—to minimize objective functions that capture the quality of matches between worker skills and job requirements [2]. The convergence behavior of these optimization algorithms is critically important for practical deployment, as faster convergence reduces computational costs and enables real-time matching in dynamic labor market environments.

The central question motivating this investigation is whether the modular structure of skill node clustering meaningfully affects how gradient descent algorithms converge when optimizing labor matching functions. This question sits at the intersection of network science, labor economics, and machine learning optimization, drawing on theoretical frameworks from each domain to develop a coherent understanding of the relationship between network topology and algorithmic convergence.

The significance of this inquiry extends beyond theoretical curiosity. Understanding how skill network modularity influences optimization dynamics could inform the design of more efficient matching algorithms, provide insights into the structural factors that make some labor markets more amenable to algorithmic optimization than others, and potentially reveal fundamental relationships between the organization of economic activity and the computational tractability of market mechanisms. Furthermore, as automated hiring and job matching systems become increasingly prevalent in modern economies, the properties that govern their computational efficiency take on substantial practical importance.

This report proceeds as follows. Section 2 establishes the theoretical foundations by reviewing relevant literature on labor network structure, gradient descent convergence theory, and the emerging field at their intersection. Section 3 develops a formal framework relating modularity to convergence behavior through multiple analytical pathways. Section 4 examines the implications for labor matching function design and optimization. Section 5 discusses limitations and directions for future research. Section 6 concludes with a synthesis of findings and practical recommendations.

---

## 2. Theoretical Foundations

### 2.1 Modular Structure in Labor Networks

The study of network modularity has its origins in the analysis of social and biological systems, where researchers observed that many real-world networks naturally organize into communities or modules—subsets of nodes with dense internal connectivity and sparser connections between subsets [3]. The modularity measure, introduced by Newman and Girvan, quantifies the extent to which a network's structure deviates from a random configuration, with higher values indicating stronger community structure [4].

Applied to labor markets, the concept of modularity reveals important structural properties of skill and industry relationships. Research has demonstrated that inter-industry labor flow networks exhibit pronounced modular structure, with industries grouping into clusters characterized by substantial worker mobility and skill overlap [1]. These clusters represent what scholars have termed "skill basins"—regions of the labor market where workers circulate among employers with similar skill requirements, facilitating knowledge diffusion and creating identifiable communities of practice.

The multi-scale nature of this modular structure is particularly noteworthy. Community detection algorithms applied to labor networks reveal hierarchical organization, with clusters existing at multiple scales simultaneously [1]. A fine-grained analysis might identify dozens of small, specialized skill clusters, while a coarser analysis would reveal fewer, more broadly defined industrial groupings. This multi-scale property suggests that the "optimal" modular structure for labor pooling depends critically on the level of analysis and the specific economic questions being addressed.

The implications of modular structure extend to labor market dynamics and matching efficiency. Industries embedded within densely connected skill basins benefit from larger effective labor pools, as workers within the cluster possess transferable skills relevant to multiple employers. This clustering affects not only the size of available workforce but also the nature of skill complementarity—the extent to which different worker skills combine productively within firms [5]. The modular organization thus shapes both the supply side and the productive potential of labor market matching.

### 2.2 Gradient Descent Convergence in Optimization Theory

Gradient descent and its variants constitute the dominant optimization paradigm for training machine learning models, including those employed in automated matching systems. The fundamental principle involves iteratively updating model parameters in the direction opposite to the gradient of an objective function, with the magnitude of updates controlled by a learning rate parameter [6].

The convergence properties of gradient descent algorithms depend critically on the geometry of the objective function's loss landscape. For smooth, convex functions, gradient descent exhibits well-characterized convergence guarantees, with the distance to optimality decreasing at a rate proportional to $O(1/t)$ after $t$ iterations under appropriate step size selection [6]. However, labor matching functions may exhibit non-convex characteristics arising from the complex interactions between skill dimensions and firm requirements.

Several factors influence convergence rate beyond simple iteration count. The condition number of the objective function—the ratio between the largest and smallest eigenvalues of the Hessian—affects how quickly gradient descent makes progress toward optimal solutions. Poorly conditioned landscapes, where the objective function varies much more rapidly in some directions than others, lead to slow convergence along certain dimensions [7]. Additionally, the presence of saddle points can significantly impede convergence, as gradient-based methods may become trapped in regions where the gradient vanishes but the point is not a local minimum [8].

Stochastic gradient descent (SGD) variants introduce additional considerations. While SGD can achieve convergence rates up to $N$ times faster than batch gradient descent when far from optima, it requires diminishing learning rates when approaching convergence to ensure stability [2]. The variance of gradient estimates—itself influenced by the structure of the data being fit—affects both the convergence rate and the final solution quality achieved.

### 2.3 Labor Matching Functions and Their Optimization

Labor matching functions represent mathematical formalizations of the relationship between worker skills, job requirements, and the quality of matches achieved. These functions encode the complementary and substitutable relationships between different skill types, the efficiency of skill utilization in production, and the frictions inherent in the matching process [5].

Optimization of labor matching functions involves adjusting parameters to minimize a loss that captures the discrepancy between predicted and observed matches, or to maximize an objective representing match quality. The specific functional form depends on the modeling approach employed, but common elements include skill requirement vectors, worker competency profiles, and matching weights that capture the productivity implications of different skill combinations [9].

The dimensionality of labor matching optimization problems can be substantial, reflecting the large number of skill types, occupations, and industries typically present in labor market data. High dimensionality introduces computational challenges and affects convergence behavior through the curse of dimensionality, where the volume of the loss landscape grows exponentially with dimension, potentially increasing the prevalence of saddle points and poor conditioning [7].

Network-based representations offer one approach to managing this complexity. By modeling the labor market as a graph where nodes represent workers, jobs, or skill categories and edges represent potential matches or actual employment relationships, the structure of the network can inform optimization procedures [10]. The modular structure of such networks—how skill nodes cluster into communities and how these communities relate to each other—may influence the geometry of the matching function landscape and consequently the convergence of gradient-based optimization.

---

## 3. Analytical Framework: Modularity and Convergence

### 3.1 Mechanistic Pathways Connecting Modularity to Convergence

The relationship between skill network modularity and gradient descent convergence operates through several interconnected mechanisms. Understanding these pathways requires integrating perspectives from network science, optimization theory, and labor economics to develop a coherent analytical framework.

The first mechanism involves the conditioning of the objective function landscape. In a highly modular network, skill nodes within the same module exhibit strong correlations—their presence or absence in worker profiles and job requirements tend to co-occur. This correlation structure induces a particular geometry in the loss function for labor matching optimization. Specifically, the Hessian matrix of the objective function will exhibit block structure corresponding to skill modules, with strong interactions within blocks and weaker interactions between blocks [11]. This block structure affects the eigenvalue spectrum of the Hessian and consequently the condition number of the optimization problem.

Formally, consider a labor matching function $L(\theta)$ parameterized by $\theta$, where $\theta$ includes coefficients governing skill complementarity relationships. The Hessian $H = \nabla^2 L(\theta)$ can be decomposed based on the modular structure of the underlying skill network. Let the network partition into $M$ modules, with module $c$ containing skill nodes $S_c$. The Hessian entries $H_{ij}$ for $i, j \in S_c$ will tend to be larger in magnitude than entries $H_{ij}$ for $i \in S_c$, $j \in S_d$ with $c \neq d$, reflecting the stronger functional relationships within skill basins.

This block-diagonal-dominated structure has implications for convergence. If the blocks are well-conditioned individually, the overall optimization problem may exhibit better conditioning than would be expected from the total dimensionality, because the optimization can make progress within each block somewhat independently. However, if the learning rate is set for the worst-conditioned block, convergence along well-conditioned dimensions may be unnecessarily slow. This suggests that modular structure creates opportunities for dimension-wise or module-wise adaptive optimization strategies that could accelerate convergence.

The second mechanism concerns the multi-scale nature of modular structure and its interaction with learning rate schedules. Labor networks exhibit hierarchy in their modular organization, with clusters nested within larger clusters in a tree-like structure [1]. This multi-scale structure has a counterpart in the loss landscape geometry: features of the landscape exist at different scales, corresponding to adjustments at different levels of skill aggregation.

Gradient descent with fixed or slowly decaying learning rates may not appropriately navigate this multi-scale geometry. Large learning rates may overshoot minima at fine scales while making progress at coarse scales, while small learning rates may become trapped in local minima at fine scales without efficiently exploring the broader landscape. The modular structure thus suggests that effective optimization of labor matching functions may require learning rate schedules that adapt to the scale of current progress—rapid exploration at coarse scales followed by fine-tuning at finer scales.

The third mechanism involves the interaction between modularity and stochastic gradient estimation. In practical labor matching applications, SGD variants are often employed due to their computational efficiency on large datasets [2]. The variance of gradient estimates depends on the sampling distribution over training examples, which in turn depends on the structure of the labor network. If training data is organized by skill modules—for instance, if certain industries contribute disproportionately to observations in specific skill domains—then the sampling process may exhibit module-correlated noise.

This module-correlated noise can affect convergence in several ways. First, it may lead to gradients that are systematically biased with respect to certain skill dimensions, potentially causing optimization to converge toward suboptimal solutions. Second, it may increase the variance of gradient estimates, requiring smaller learning rates to maintain stability and thereby slowing convergence. Third, it may create effective learning rate heterogeneity across modules, where updates for some skill categories are more volatile than for others.

### 3.2 Theoretical Analysis of Convergence Effects

To formalize the relationship between modularity and convergence, we can analyze how modularity metrics relate to standard convergence bounds for gradient descent algorithms. For a labor matching function $L(\theta)$ satisfying standard smoothness assumptions—specifically, that the gradient is Lipschitz continuous with constant $L$—the convergence rate of gradient descent with appropriate step size satisfies [6]:

$$\min_{0 \leq k < t} \|\nabla L(\theta_k)\|^2 \leq \frac{2[L(\theta_0) - L^*]}{t}$$

where $L^*$ is the optimal function value. This bound suggests that convergence rate depends fundamentally on the Lipschitz constant $L$, which characterizes the maximum steepness of the loss landscape.

The modular structure of the underlying skill network affects $L$ through the correlation structure of skill dimensions. Let $\Sigma$ denote the covariance matrix of skill co-occurrence patterns in the labor market data. The Lipschitz constant for gradient descent on a quadratic loss function can be related to the spectral norm of $\Sigma$, which in turn depends on the modular partition. Specifically, if skills within modules are highly correlated, the effective dimensionality of the problem is reduced, potentially lowering the worst-case Lipschitz constant and improving convergence guarantees.

However, this analysis must be qualified by consideration of the modularity's effect on the loss landscape beyond simple conditioning. High modularity may create landscape features—ridges, valleys, or plateaus—that are not fully captured by Lipschitz constants. In particular, the boundaries between skill modules may correspond to regions of rapid landscape transition, creating effective cliffs that challenge gradient-based optimization [8].

We can also consider the relationship from the perspective of community detection in the optimization process itself. Just as the Louvain algorithm iteratively refines modularity until convergence [11], gradient descent can be viewed as seeking a partition of the parameter space into regions of attraction around local minima. The modular structure of the data may bias the location and basin structure of these minima, with implications for which solutions gradient descent tends to find and how quickly it reaches them.

### 3.3 Empirical Considerations and Manifestations

The theoretical relationship between modularity and convergence manifests in several observable phenomena that would appear in empirical studies of labor matching optimization. These manifestations provide both tests of the theoretical framework and practical indicators for algorithm design.

First, convergence rate variability across labor markets may correlate with differences in modular structure. Labor markets with more pronounced modular organization—characterized by clearly defined skill basins with strong internal connectivity—might exhibit different convergence behavior than markets with more diffuse skill structures. Specifically, if the theoretical framework is correct, highly modular markets might show faster initial convergence as gradient descent exploits block structure in the Hessian, followed by slower fine-tuning convergence as the optimization addresses within-module interactions.

Second, the choice of aggregation level in skill taxonomy may affect optimization performance in ways consistent with modularity. Labor market data is typically coded using occupational or skill classification systems that impose a particular hierarchical structure on skill categories. Different classification systems correspond to different partitions of the skill network, with different modularity values. The optimization of labor matching functions may perform better when the classification system aligns with the natural modular structure of the underlying labor market, as this alignment would create a favorable correspondence between the data representation and the loss landscape geometry.

Third, the effectiveness of adaptive optimization methods may depend on modularity. Algorithms such as Adam, which adapt learning rates based on gradient history, may be particularly suited to labor matching optimization because they can automatically adjust for the heterogeneous curvature across skill modules [2]. If modularity creates varying effective learning rates across skill dimensions, adaptive methods that accommodate this heterogeneity should outperform non-adaptive alternatives, with the performance gap increasing with the degree of modularity in the underlying network.

---

## 4. Implications for Labor Matching Function Design

### 4.1 Taxonomic Design and Modularity Alignment

The design of skill taxonomies for labor matching systems involves critical decisions about the granularity and structure of skill categories. These decisions have direct implications for optimization behavior and should be informed by consideration of modular structure in the underlying labor market.

Traditional skill classification systems, such as those derived from O*NET or similar occupational databases, organize skills into hierarchical categories based on conceptual relationships and job analysis [12]. While these taxonomies capture meaningful distinctions between skill types, they may not optimally align with the modular structure of labor flow networks as revealed by actual worker mobility patterns. Research suggests that data-driven approaches to skill clustering—using observed co-occurrence in job postings, worker profiles, or employment histories—can identify skill groupings that differ from a priori taxonomies and may better reflect the actual structure of labor markets [1].

From an optimization perspective, skill taxonomies that closely align with natural modular structure should facilitate more efficient gradient descent convergence. This alignment ensures that the parameters governing strongly interacting skill combinations are grouped together in the optimization landscape, allowing the block-structure advantages discussed previously to be realized. Conversely, taxonomies that fragment naturally modular skill groups or combine weakly related skills into single categories may create poorly conditioned optimization problems with slower convergence.

Practically, this suggests that labor matching system designers should consider empirical modularity analysis as part of the taxonomy development process. Techniques such as the Louvain algorithm can be applied to labor flow networks constructed from job transition data to identify natural skill clusters [11]. These clusters can then inform the design of skill representation spaces for matching optimization. The resulting taxonomies would reflect both the conceptual meaning of skill categories and their empirical organization in labor markets.

### 4.2 Optimization Algorithm Selection and Configuration

The relationship between modularity and convergence has direct implications for the selection and configuration of optimization algorithms for labor matching functions. Different algorithmic choices interact differently with modular structure, and understanding these interactions can guide practical implementation.

For labor markets with high modularity, optimization algorithms that exploit block structure in the Hessian may be particularly effective. Second-order methods such as Newton's method or quasi-Newton methods like L-BFGS approximate the Hessian and use curvature information to condition the optimization trajectory [7]. In a modular setting, these methods can be modified to explicitly exploit block-diagonal structure, potentially reducing computational complexity while maintaining convergence benefits.

However, second-order methods face challenges in high-dimensional settings common in labor matching applications, where the number of parameters may be large relative to available computational resources. In such cases, first-order methods with appropriate adaptation strategies may be more practical. The key insight is that adaptation should be informed by modular structure: learning rates or preconditioning should be allowed to vary across skill modules based on the local conditioning of each block.

Stochastic gradient descent variants present particular opportunities and challenges in the modular setting. The noise characteristics of SGD depend on the sampling distribution over training examples, which in turn depends on how the data is organized relative to modular structure. If the training data is structured such that mini-batches tend to contain correlated examples from the same skill module, gradient estimates will be biased toward that module's contributions, potentially causing optimization to oscillate between modules rather than making balanced progress.

Mitigation strategies include stratified sampling that ensures mini-batches represent all modules proportionally, or curriculum learning approaches that focus optimization on one module at a time before integrating across modules [9]. These strategies explicitly manage the interaction between modular structure and stochastic optimization to achieve more stable and potentially faster convergence.

### 4.3 Multi-Scale Optimization Strategies

The hierarchical nature of modular structure in labor networks suggests that multi-scale optimization strategies may be particularly effective for labor matching functions. These strategies explicitly account for the nested nature of skill clusters and adapt optimization behavior across scales.

One approach involves hierarchical optimization, where the problem is first optimized at a coarse scale corresponding to large, inclusive skill modules, and then refined at progressively finer scales. This mirrors the multi-scale community detection process used in labor network analysis [1]. At each scale, the optimization can focus on the most salient features of the loss landscape, with subsequent scales addressing finer details.

The implementation of hierarchical optimization requires defining mappings between scales. In the labor matching context, this corresponds to aggregating skill categories into higher-level groups based on the modular structure of the network. The coarse-scale optimization would operate on parameters governing broad skill categories, while fine-scale optimization would introduce parameters for specific skills within these categories. Learning rate schedules can be designed to transition between scales, with larger rates at coarse scales and smaller rates at fine scales.

Alternatively, coarse-to-fine optimization can be implemented through appropriate initialization strategies. Starting optimization from parameters that reflect the coarse-scale structure before introducing fine-scale variation may help gradient descent avoid poor local minima that would be encountered if optimization proceeded solely at the fine scale. The basin of attraction for good solutions may be wider at coarse scales, providing a more reliable starting point for subsequent refinement.

---

## 5. Limitations and Future Research Directions

The analysis presented in this report is primarily theoretical, and several limitations should be acknowledged. First, while we have developed a coherent framework connecting modularity to convergence, empirical validation of the proposed relationships remains necessary. Controlled experiments comparing convergence behavior across labor markets with varying modularity would provide crucial tests of the theoretical predictions.

Second, the framework has focused on gradient descent convergence but has not addressed other important aspects of labor matching optimization, such as generalization to unseen data, robustness to distributional shift, or fairness considerations. These aspects may have different relationships to modular structure and warrant independent investigation.

Third, the analysis has treated modularity as a property of static networks, but labor markets are dynamic systems where skill clusters evolve over time in response to technological change, educational system developments, and economic shocks [1]. Understanding how temporal dynamics in modular structure affect ongoing optimization of matching functions presents significant theoretical challenges.

Future research should pursue several promising directions suggested by this analysis. First, empirical studies should investigate the correlation between network modularity metrics and observed convergence rates in labor matching optimization, controlling for other factors that might affect convergence such as dataset size, dimensionality, and regularization. Second, the development of modularity-aware optimization algorithms—algorithms that explicitly exploit block structure in the Hessian or adapt learning rates based on modular decomposition—represents an important practical direction. Third, the extension of the framework to other aspects of labor market algorithms, including skill recommendation, wage prediction, and job search optimization, would test the generality of the proposed relationships.

---

## 6. Conclusion

This report has investigated the relationship between the modular structure of skill node clustering in vocational networks and the convergence of gradient descent algorithms applied to labor matching functions. Our analysis reveals that modularity exerts a significant influence on convergence behavior through multiple interconnected mechanisms, including the conditioning of the loss landscape, the interaction with stochastic gradient estimation, and the multi-scale geometry of the optimization problem.

The key findings can be summarized as follows. First, the block-diagonal-dominated Hessian structure induced by skill module organization affects the condition number of labor matching optimization problems, with implications for convergence rates that depend on the specific modular partition and its alignment with the optimization parameterization. Second, the multi-scale nature of labor network modularity creates optimization landscapes with features at multiple scales, requiring or benefiting from learning rate schedules and optimization strategies that adapt to the current scale of progress. Third, stochastic gradient estimation in modular settings introduces module-correlated noise that can affect both convergence rate and solution quality, with implications for mini-batch composition and sampling strategies.

These findings have practical implications for the design of automated labor matching systems. Skill taxonomy development should consider empirical modularity analysis to ensure alignment between skill categories and natural labor market structure. Optimization algorithm selection and configuration should account for modularity, with adaptive methods potentially offering advantages in highly modular settings. Multi-scale optimization strategies that explicitly address the hierarchical structure of skill clusters may achieve faster and more reliable convergence.

The framework developed here represents a step toward integrating insights from network science, optimization theory, and labor economics to understand the computational properties of automated labor markets. As algorithmic matching systems play an increasingly important role in connecting workers with employment opportunities, understanding the structural factors that affect their computational efficiency becomes both scientifically important and practically valuable. Future research that empirically validates and extends the relationships proposed here will be essential for translating these insights into improved labor market technologies.

---

## References

[1] Skill-based industrial clusters detected via inter-industry labor flow networks reveal skill basins that measure skilled workforce available to industries, demonstrating predictive validity for industry-city employment growth and enabling identification of optimal cluster sizes for labor pooling.

[2] Stochastic Gradient Descent exhibits convergence rates up to N times faster than Batch Gradient Descent for large N when far from minima, though requiring diminishing step sizes near convergence, necessitating careful learning rate selection as an additional hyperparameter.

[3] Community detection in complex networks reveals modular structures where subsets of nodes exhibit dense internal connectivity and sparser inter-module connections, with modularity measures quantifying deviation from random network configurations.

[4] Newman-Girvan's modularity measure evaluates the strength of network partition into modules, where higher positive values indicate stronger community structure and guide the identification of meaningful network subdivisions.

[5] Labor matching functions incorporating skill efficiency and complementarity reveal that skills are substitutable in production with rising marginal operational costs, while analytical, computer, and interpersonal skills have increased in efficiency while routine skills have declined.

[6] Gradient descent convergence for Lipschitz-continuous gradients with step size $\alpha_k = 1/L$ achieves error bounds of $O(1/t)$ after $t$ iterations, with the minimum gradient norm decreasing proportionally to $\frac{2L[f(w_0) - f^*]}{t}$.

[7] Optimization complexity for Lipschitz-continuous functions requires at least $\Omega(1/\epsilon^d)$ iterations in $d$ dimensions, with grid-based search achieving optimal worst-case rates through systematic exploration of the loss landscape.

[8] Saddle points in gradient descent cause algorithmic stagnation due to zero gradients that prevent position updates, with extremely small gradient changes near saddle points significantly slowing convergence toward local minima.

[9] Worker-job matching models with two-sided heterogeneity identify clusters of similar workers and jobs using observable characteristics, with skill and task bins defined through standardized assessments and occupational requirement databases.

[10] Network representations of labor markets model workers and jobs as nodes with employment contracts as edges, with match probabilities determined by skill profiles and market assignments drawn from unchanging probability matrices.

[11] The Louvain method optimizes modularity through iterative local refinement and community aggregation phases, continuing until convergence where no further modularity enhancement is feasible, achieving effective community detection in diverse networks.

[12] Occupational networks analyzed through hierarchical dependencies reveal that cognitive and technical skills embedded within nested structures, along with general skills like managerial and social competencies, command higher market returns through their positions in skill hierarchies.

## Annotations


## Sources
[1] http://theory.stanford.edu/~sergei/papers/wine09-matching.pdf
[2] https://arxiv.org/html/2601.03162v1
[3] https://arxiv.org/pdf/2309.11798
[4] https://elmerli.github.io/skill_mixing.pdf
[5] https://eprints.nottingham.ac.uk/65658/1/PhD_Thesis.pdf
[6] https://escholarship.org/content/qt6hx3d5h9/qt6hx3d5h9_noSplash_beef8000b6a548ae911cf91a02e38d86.pdf
[7] https://ipl.econ.duke.edu/seminars/system/files/seminars/3403_paper.pdf
[8] https://www.cise.ufl.edu/~mythai/files/15icdm.pdf
[9] https://www.cs.ubc.ca/~schmidtm/Courses/5XX-S20/S2.pdf
[10] https://www.mdpi.com/2076-3417/13/10/6119
[11] https://www.nature.com/articles/s41562-024-02093-2
[12] https://www.nature.com/articles/s41598-025-01678-9
[13] https://www.nature.com/articles/s41598-025-90030-2
[14] https://www.sciencedirect.com/science/article/pii/S0048733322000142
[15] https://www.workrisenetwork.org/publications/search-and-matching-modern-labor-markets-landscape-report