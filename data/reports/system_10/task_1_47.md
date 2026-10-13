# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 01edc4b7 | **Time:** 75.62s | **Cost:** $1.11435
--------------------------------------------------------------------------------

# The Relationship Between Skill Network Modularity and Gradient Descent Convergence in Labor Matching Functions

Network-based modularity in vocational skill systems presents a nuanced optimization challenge for gradient descent algorithms applied to labor matching functions. While modularity optimization has become a standard tool for identifying skill communities and occupation clusters, the relationship between this network structure and the convergence properties of gradient descent algorithms used for labor market matching remains underexplored in empirical research. This report synthesizes insights from network science, optimization theory, and labor economics to examine whether the modular organization of skill nodes in vocational networks significantly affects gradient descent convergence rates in labor matching functions.

## Network Modularity in Vocational and Skill-Based Systems

### Conceptual Foundations of Modularity in Skill Networks

The modularity of networks has emerged as a central concept for understanding how skills and occupations organize within labor markets[1][51]. When researchers construct skill networks from labor market data, they create systems where nodes represent individual skills and edges connect skills that commonly co-occur either among workers or within job requirements. The resulting network typically exhibits significant community structure, meaning that certain groups of skills are more densely interconnected than others[1]. This modular organization reflects real economic phenomena—workers specializing in technical skills cluster together, separate from those focused on communication or creative skills.

The strength of this modularity is typically measured using a modularity score, which quantifies the density of connections within communities relative to what would be expected in a random network[11][28]. Research on online freelance labor markets demonstrates that the modularity of worker skill networks reaches values around 0.47, while employer skill requirement networks show modularity of approximately 0.50, both well above the 0.3 threshold indicating significant community structure[1][51]. These high modularity values reveal that labor markets organize into distinct skill basins—interconnected zones where workers can circulate and diffuse knowledge relatively easily[3][6].

The modular structure of vocational networks extends beyond simple skill clusters. Recent investigations using vocational education and training (VET) data demonstrate that these networks exhibit hierarchical modularity, where coarser-level modules can be further decomposed into finer-grained submodules[4]. This hierarchical organization reflects the nested dependencies within skill systems, where general skills often serve as prerequisites for more specialized competencies. For example, basic mathematical skills form a foundation upon which domain-specific technical skills build, creating a nested structure that has grown increasingly pronounced over recent decades[54].

### Methods for Detecting Modularity: The Louvain Algorithm

The Louvain algorithm has become the dominant method for detecting modularity in vocational and skill networks[1][39][51]. This hierarchical clustering approach operates through a multi-phase process that optimizes modularity, a quality function comparing the actual structure to a null model[11][17][27][28]. The algorithm initializes each node as its own community, then iteratively merges nodes into communities that maximize the modularity gain. When no further improvements can be achieved through local movements, the algorithm collapses each community into a super-node, and the process repeats on the resulting condensed network[17].

The computational efficiency of the Louvain algorithm has made it practically appealing—it scales roughly linearly with the number of edges in the network[25][39]. However, this efficiency comes with limitations. The algorithm is stochastic, meaning repeated runs on the same network can produce slightly different partitions, particularly when community structure is not sharply defined[27]. More critically, modularity optimization exhibits both underfitting and overfitting problems: it cannot find more than approximately √(2E) communities in connected networks (the "resolution limit"), yet it systematically finds spurious communities in randomly generated networks with no true structure[35][56].

## Gradient Descent and Optimization in Labor Matching Functions

### Fundamentals of Gradient Descent Algorithms

Gradient descent represents a foundational optimization technique used extensively in machine learning and economic modeling[2][5][44][47]. The algorithm operates by iteratively adjusting parameters in the direction of steepest descent, moving toward a minimum of a cost function. For a differentiable function \(f(\mathbf{x})\), the update rule takes the form \(\mathbf{x}_{t+1} = \mathbf{x}_{t} - \alpha \nabla f(\mathbf{x}_{t})\), where \(\alpha\) is the learning rate controlling step size and \(\nabla f(\mathbf{x}_{t})\) is the gradient at the current position[2][44].

The convergence properties of gradient descent depend critically on several factors. For convex functions with Lipschitz-continuous gradients, gradient descent with appropriately chosen step size \(t \leq 1/L\) achieves convergence at a rate of \(O(1/k)\) after \(k\) iterations, where the bound satisfies[44]:

\[f(x^{(k)}) - f(x^*) \leq \frac{\|x^{(0)} - x^*\|_2^2}{2tk}\]

The step size parameter is critical: if too large, the algorithm diverges; if too small, convergence becomes prohibitively slow[2][5][44]. For strongly convex functions, convergence accelerates to exponential rate \(O(c^k)\) with \(0 < c < 1\)[44].

### Application to Labor Matching Functions

Labor matching functions represent the rate at which unemployed workers connect with job vacancies in the economy. These functions have been extensively studied in labor economics, with the canonical specification being the Cobb-Douglas form:

\[M(U,V) = \mu U^{\alpha} V^{1-\alpha}\]

where \(U\) denotes unemployed workers, \(V\) denotes vacancies, and \(\mu\) is a matching efficiency parameter[7][13][19]. More sophisticated matching models incorporate heterogeneity on both sides of the market, allowing workers and firms to differ in productivity[7][19][22].

Recent deep learning approaches to solving labor matching models reformulate equilibrium conditions as optimization problems amenable to gradient descent[7][19][22][47]. These methods construct neural networks to approximate value and decision functions, then use stochastic gradient descent to minimize the residuals in equilibrium equations. A study applying deep learning to canonical labor market search models with two-sided heterogeneity found numerical errors on the order of \(10^{-7}\) over the full state space, indicating that neural network training via gradient descent can achieve high accuracy even for complex economic models[7][19].

The convergence rate of these matching algorithms is influenced by properties of the underlying network structure through which labor information diffuses. Federated learning approaches to labor market forecasting demonstrate that heterogeneity in company data distributions requires clustering companies into groups with similar characteristics to ensure stable convergence[45]. This suggests that network topology—the pattern of connections between agents—affects optimization dynamics.

## Network Topology and Algorithm Convergence

### General Principles of Topology Effects

A critical body of research has established that network topology—including properties such as diameter, degree distribution homogeneity, and clustering coefficient—significantly influences the convergence rates of algorithms operating on networks[15][37][40]. For distributed optimization algorithms solving consensus problems across networked agents, networks with certain topological properties achieve faster convergence[37][40]. Specifically, networks with higher mean degree, smaller diameter (shorter maximum path between any two nodes), and more homogeneous degree distribution all exhibit faster convergence[37][40].

This effect operates through a mathematical mechanism: the convergence rate of many distributed algorithms depends on properties of the network's Laplacian matrix or related spectral properties[37][40][58]. The leading eigenvalues and eigenvectors of network matrices determine how quickly information propagates through the network. When nodes are highly connected (high mean degree) and distributed relatively uniformly (homogeneous degree distribution), information propagates more efficiently throughout the network[37][40].

The clustering coefficient—the fraction of possible triangles that actually exist in the network—affects convergence differently depending on the algorithm. For decentralized optimization approaches, surprisingly, lower clustering coefficients lead to faster convergence rates[15]. This counterintuitive finding reflects that highly clustered networks can create bottlenecks where information must traverse through hub nodes to reach distant clusters.

### Convergence of Network-Based Algorithms

Network-based optimization algorithms, including the Alternating Direction Method of Multipliers (ADMM) and consensus-based approaches, exhibit convergence guarantees that depend explicitly on network properties[18][23][37]. These methods decompose large-scale optimization problems across network nodes, with each node solving its local problem and exchanging information with neighbors. The theoretical convergence rate is often expressed as \(O(1/\sqrt{t})\) for convex problems[23], with constants that depend on spectral properties of the network weight matrix.

The spectral radius and related eigenvalue properties fundamentally determine how quickly different optimization algorithms converge[26][58]. For graph partitioning and clustering problems—which share mathematical structure with labor market segmentation—spectral methods based on the Laplacian matrix provide efficient solutions[11][26][58]. The quality of these spectral approximations depends on the separation between leading eigenvalues: when the spectrum has clear gaps, spectral methods produce better approximations[26][28].

## Modularity of Skill Networks and Labor Matching Algorithm Performance

### Direct Effects on Matching Algorithm Architecture

The modular structure of skill networks affects labor matching algorithms through both direct architectural choices and indirect effects on optimization dynamics. Many contemporary job matching systems, including LinkedIn's LinkSAGE system, explicitly incorporate skill nodes into their graph neural network architectures[33][43][46]. These systems construct bipartite networks connecting workers and jobs through shared skill nodes. The modularity of the underlying skill network directly affects information propagation through the graph during training of these neural networks.

When skills organize into tight communities (high modularity), the graph structure facilitates information flow within skill clusters but potentially constrains information flow across clusters. Graph neural networks propagate information through edges, so workers and jobs connected through skills in the same high-modularity cluster receive more similar embeddings than those in different clusters[33][43]. LinkedIn's empirical findings demonstrate that incorporating skill node information—and by extension, the modular structure implied by skill relationships—improves matching accuracy by approximately 1.5% compared to baseline models without skill nodes[33][43].

### Indirect Effects Through Network Structure on Convergence

The modularity of skill networks creates structured heterogeneity in the underlying optimization landscape. When gradient descent algorithms optimize matching functions on networks with high modularity, they encounter multiple local optima corresponding to solutions that match workers primarily within skill clusters. The presence of many high-modularity clusters creates a rugged cost landscape with multiple comparable local minima separated by high-gradient regions.

Research on labor market dynamics using network-based frameworks reveals that occupational clustering—closely related to skill modularity—affects wage trajectories and employment dynamics[38][54][60]. Occupations with skills aligned to the nested modular structure of labor markets command higher wage premiums and show different sensitivity to business cycle shocks[54]. This suggests that the modular organization creates effective economic segmentation that gradient-based learning algorithms must navigate.

The resolution limit problem in modularity optimization becomes relevant here: modularity-maximizing approaches cannot reliably detect more than √(2E) communities[35][56]. This limitation means that when vocational networks genuinely contain fine-grained modular structure, modularity-based algorithms that identify skill clusters will necessarily miss some structure, potentially leading to mismatch between the detected modularity and the true underlying organization. This mismatch can cause gradient descent algorithms to optimize matching functions based on an incomplete or misrepresented network structure.

### Effects of Network Clustering Coefficient

The clustering coefficient of skill networks—the density of triangles relative to potential triangles—affects how efficiently gradient descent algorithms can update model parameters. In skill networks, triangles often represent skill triplets where all three pairs co-occur either within worker profiles or job requirements. High clustering indicates that related skills form tightly interconnected cliques.

Counterintuitively, this high clustering can slow convergence of distributed optimization algorithms[15]. The mechanism involves information bottlenecks: in highly clustered networks, there exist hub nodes that must mediate information flow between distant clusters. Even though these hubs are highly connected, they create dependency relationships that slow overall convergence. For labor matching problems distributed across workers and jobs connected through skill nodes, this means high clustering in the skill network can impede the rate at which matching algorithms converge to equilibrium.

Conversely, skill networks with lower clustering—where skills are more sparsely distributed across combinations—allow gradient descent algorithms to explore the parameter space more efficiently. This property might explain why some labor market matching systems show better performance with sparser skill representations: the lower clustering facilitates faster convergence of the underlying optimization algorithms.

## Empirical Evidence and Theoretical Gaps

### Findings from Labor Market Studies

Direct empirical evidence quantifying the relationship between skill network modularity and gradient descent convergence in labor matching functions remains sparse. However, several lines of evidence suggest significant connections. Research on skill progression networks constructed from job transitions demonstrates that network modularity predicts career mobility and wage outcomes[38][54]. Specifically, workers with skills corresponding to less modular (more interconnected) portions of the skill network face better long-term wage prospects and greater occupational mobility[54].

This finding implies that algorithms trained to predict successful job matches must account for the modular structure: matches involving skills from loosely connected regions of the skill network may require different gradient steps during training than matches involving tightly clustered skills. The gradual changes in modularity observed over recent decades—with skill networks becoming increasingly modular—correlate with changes in how sectoral shocks affect aggregate labor market dynamics[54][57].

Studies applying deep learning to labor market matching problems note that the distribution of heterogeneity affects convergence properties[7][19][22][45]. When matching algorithms operate on heterogeneous populations, they often require clustering agents (workers, firms, companies) into groups with similar characteristics to achieve stable convergence[45]. This procedure is mathematically analogous to identifying modularity in networks: both seek to partition nodes into groups with high internal similarity.

### Computational Performance of Modularity-Based Approaches

The Louvain algorithm for modularity optimization typically achieves high-quality solutions efficiently[25][27][39], making it practical for real-world vocational networks. However, computational studies reveal that Louvain's stochastic nature and overfitting problems can introduce noise into the identified modular structure[25][56]. This noise would propagate into matching algorithms that use the identified modularity to organize their solution space.

For large-scale vocational networks, alternative community detection methods such as Leiden offer improvements over Louvain by ensuring that identified communities are internally well-connected[30]. These improvements in modularity quality—creating sharper, more reliable cluster boundaries—should in principle improve the convergence properties of gradient descent algorithms operating on matching functions organized by these clusters. However, no direct empirical comparison exists in the literature.

## Synthesis: Mechanisms Through Which Modularity Affects Convergence

### Proposed Causal Mechanisms

Several mechanisms plausibly connect skill network modularity to gradient descent convergence in labor matching functions:

**1. Spectral Properties and Convergence Rates**: High modularity in skill networks corresponds to larger gaps between eigenvalues of the network's spectral representation[11][28]. These spectral gaps affect how information propagates through graph-based matching algorithms. Larger spectral gaps can slow convergence of spectral methods, though they may accelerate convergence of certain iterative algorithms that exploit block structure[26][58].

**2. Cost Function Landscape Structure**: Highly modular skill networks create matching cost functions with multiple local minima separated by high-gradient regions. Gradient descent navigates this rugged landscape differently than smooth landscapes. Initial conditions near skill cluster boundaries may require different convergence paths than initial conditions within clusters[44].

**3. Information Propagation in Graph Neural Networks**: Job matching systems incorporating skill graph structure (like LinkSAGE) rely on information propagation through the graph. High modularity creates bottlenecks in this propagation, potentially requiring more gradient descent iterations to achieve consistent embeddings across skill clusters[33][43].

**4. Heterogeneity and Distributed Optimization**: When matching algorithms operate across multiple geographic markets or job categories, modularity creates heterogeneity in local matching dynamics. Recent federated learning approaches to labor forecasting demonstrate that clustering agents by similarity before distributed optimization improves convergence[45]. This suggests modularity-based clustering could improve convergence by reducing heterogeneity within optimization subproblems.

### Competing Effects and Their Relative Importance

The theoretical predictions about modularity's effects on convergence point in partially contradictory directions. On one hand, modularity creates useful structure that reduces the effective dimensionality of matching problems, potentially accelerating convergence. On the other hand, modularity introduces heterogeneity and clustering that can slow convergence of certain algorithms. The net effect likely depends on specifics of the matching model, the structure of modularity, and the gradient descent variant employed.

Research on network topology effects suggests that the relationship is non-monotonic: moderate modularity may represent an optimal balance, while extreme modularity (either very high or very low) would impair convergence[15][37][40]. The empirical question remains whether actual vocational skill networks operate near this optimum or at extremes.

## Limitations of Current Understanding

### Data and Methodological Gaps

Despite theoretical reasoning connecting modularity and convergence, the literature lacks direct empirical studies examining this relationship quantitatively. Most research addressing modularity focuses on either the community detection process itself or downstream effects on economic outcomes (wages, employment dynamics). The intermediate step—how modularity specifically affects the convergence of gradient-based algorithms optimizing labor matching functions—remains unexplored.

Additionally, most labor matching models used in research employ highly simplified representations of skills, typically reducing multidimensional skill variation to low-dimensional spaces (often one or two dimensions)[13][16][57]. These simplified models may not exhibit the complex modularity effects present in high-dimensional skill networks constructed from detailed vocational data[1][4][51].

### Unresolved Questions About Optimal Modularity

The field lacks theoretical or empirical characterization of whether there exists an optimal level of modularity for gradient descent convergence in labor matching. Economic intuition suggests that some modularity is beneficial—it allows workers and jobs to be meaningfully segmented—but excessive modularity might create barriers to efficient matching. The resolution limit problem of modularity optimization suggests that algorithms cannot reliably detect true modularity levels much finer than √(2E), introducing uncertainty about whether observed modularity reflects genuine structure or optimization artifacts[35][56].

## Conclusion

The modularity of skill node clustering in vocational networks plausibly affects the convergence properties of gradient descent algorithms optimizing labor matching functions through multiple mechanisms: spectral properties of network representations, the structure of matching cost function landscapes, information propagation in graph neural network architectures, and heterogeneity in distributed optimization approaches. Theoretical frameworks from network science and optimization suggest that moderate modularity could facilitate convergence, while extreme modularity would impede it.

However, direct empirical evidence quantifying this relationship remains limited. Current research demonstrates that incorporating skill networks into matching algorithms improves matching accuracy and that network topology affects algorithm convergence in distributed settings, but the specific connection between modularity of vocational skill networks and labor matching function convergence has not been systematically investigated. The mechanisms appear significant enough to warrant targeted research, particularly given the increasing importance of skill-based matching in labor markets and the growing sophistication of neural network-based matching systems that explicitly incorporate network structure.

Future research should develop explicit metrics linking network modularity to convergence rates of specific matching algorithms, conduct empirical studies comparing convergence performance across vocational networks with varying modularity levels, and theoretically characterize the optimal modularity properties for different classes of matching models. Such work would bridge current gaps between network science, optimization theory, and labor economics, providing clearer guidance for designing matching algorithms that leverage skill network structure efficiently.

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Skill networks and measures of complex human capital - PNAS', 'url': 'https://www.pnas.org/doi/10.1073/pnas.1706597114'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Gradient Descent in Linear Regression - GeeksforGeeks', 'url': 'https://www.geeksforgeeks.org/machine-learning/gradient-descent-in-linear-regression/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[1909.03379] Modular structure in labour networks reveals skill basins', 'url': 'https://arxiv.org/abs/1909.03379'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Quantifying the influence of vocational education and training with ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12370024/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Gradient descent (article) | Khan Academy', 'url': 'https://www.khanacademy.org/math/multivariable-calculus/applications-of-multivariable-derivatives/optimizing-multivariable-functions/a/what-is-gradient-descent'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Modular structure in labour networks reveals skill basins', 'url': 'https://www.ul.ie/media/26865/download?inline'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Deep Learning for Search and Matching Models', 'url': 'https://www.parisschoolofeconomics.eu/app/uploads/2024/10/DeepSAM_paper.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The behaviour of modularity-optimizing community detection ...', 'url': 'https://www.math.ucla.edu/~mason/research/sally_dissertation_final.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Understanding Skill-Matching Algorithms in Staffing - i creatives', 'url': 'https://www.icreatives.com/iblog/skill-matching-algorithms/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Some Engineering Aspects of Economic Design', 'url': 'https://natmatch.com/documents/rothperansonaer.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Modularity and community structure in networks - PNAS', 'url': 'https://www.pnas.org/doi/10.1073/pnas.0601602103'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Digital footprints and job matching: The new frontier of AI-driven hiring', 'url': 'https://www.brookings.edu/articles/digital-footprints-and-job-matching-the-new-frontier-of-ai-driven-hiring/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The Matching Function and Nonlinear Business Cycles', 'url': 'https://www.dallasfed.org/-/media/documents/research/papers/2022/wp2201.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Faster unfolding of communities: Speeding up the Louvain algorithm', 'url': 'https://link.aps.org/doi/10.1103/PhysRevE.92.032801'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'How Clustering Affects the Convergence of Decentralized ... - arXiv', 'url': 'https://arxiv.org/abs/2407.01460'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Nonlinear Search and Matching Explained', 'url': 'https://www.aeaweb.org/conference/2022/preliminary/paper/7KD5aQr6'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Louvain Algorithm - TigerGraph', 'url': 'https://www.tigergraph.com/glossary/louvain-algorithm/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Network Lasso: Clustering and Optimization in Large Graphs - PMC', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4937836/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Deep Learning for Search and Matching Models', 'url': 'https://www.parisschoolofeconomics.eu/app/uploads/2024/10/DeepSAM_paper.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Revisiting Optimal Convergence Rate for Smooth and Non-convex...', 'url': 'https://openreview.net/forum?id=eHePKMLuNmy'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Skill Demand Forecasting Using Temporal Knowledge Graph ... - arXiv', 'url': 'https://arxiv.org/html/2504.07233v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Deep Learning for Search and Matching Models - GitHub Pages', 'url': 'https://yangycpku.github.io/files/DeepSAM_paper.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] On the Convergence Rate of Average Consensus and Distributed ...', 'url': 'https://groups.csail.mit.edu/tds/papers/Su-Lili/Asilomar2018-1.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'New skills data now available with Employment Projections', 'url': 'http://blog.dol.gov/2024/08/29/new-skills-data-now-available-with-employment-projections'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Analysis of Network Clustering Algorithms and Cluster Quality ...', 'url': 'https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0159161'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Spectral Methods for Data Science: A Statistical Perspective', 'url': 'https://users.ece.cmu.edu/~yuejiec/papers/SpectralMethods.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Community Detection - Neo4j GraphAcademy', 'url': 'https://graphacademy.neo4j.com/courses/graph-data-science-fundamentals/1-graph-algorithms/6-community-detection/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Modularity and community structure in networks - PNAS', 'url': 'https://www.pnas.org/doi/10.1073/pnas.0601602103'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Dedalus: A flexible framework for numerical simulations with ...', 'url': 'https://link.aps.org/doi/10.1103/PhysRevResearch.2.023068'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'leiden_community_detection - Memgraph', 'url': 'https://memgraph.com/docs/advanced-algorithms/available-algorithms/leiden_community_detection'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Rates of convergence for the cluster tree - Computer Science', 'url': 'https://cseweb.ucsd.edu/~kamalika/pubs/cd10.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'TOWARDS GUIDED DESCENT: OPTIMIZATION ALGORITHMS FOR ...', 'url': 'https://arxiv.org/html/2512.18373v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'LinkSAGE: Optimizing Job Matching Using Graph Neural Networks', 'url': 'https://arxiv.org/html/2402.13430v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Rates of convergence for the cluster tree', 'url': 'http://papers.neurips.cc/paper/4068-rates-of-convergence-for-the-cluster-tree.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] simplified energy landscape for modularity using total variation', 'url': 'https://ww3.math.ucla.edu/camreport/cam17-47.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'AI Skill Matching Algorithms For Schedule Optimization - myshyft.com', 'url': 'https://www.myshyft.com/blog/skill-matching-algorithms/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Impacts of Network Topology on the Performance of a Distributed ...', 'url': 'https://stuff.mit.edu/people/tgibson/papers/cao_cdc_2016.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Mapping job fitness and skill coherence into wages - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11116373/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Occupation Modularity and the Work Ecosystem', 'url': 'https://par.nsf.gov/servlets/purl/10298088'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Impacts of Network Topology on the Performance of a Distributed ...', 'url': 'https://arxiv.org/abs/1603.04154'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Literature Review of Industry, Occupation and Skill Clusters, and ...', 'url': 'https://pcrd.purdue.edu/wp-content/uploads/2025/04/Literature-Review_04-21-2025.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Generalized Modularity for Computing Community Structure in ...', 'url': 'https://onlinelibrary.wiley.com/doi/10.1155/2023/8767131'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'LinkSAGE: Optimizing Job Matching Using Graph Neural Networks', 'url': 'https://arxiv.org/html/2402.13430v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Lecture 6: September 12 6.1 Gradient Descent: Convergence Analysis', 'url': 'https://www.stat.cmu.edu/~ryantibs/convexopt-F13/scribes/lec6.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Convergence-aware Clustered Federated Graph Learning ... - arXiv', 'url': 'https://arxiv.org/abs/2409.19545'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'LinkSAGE: Optimizing Job Matching Using Graph Neural Networks', 'url': 'https://dl.acm.org/doi/10.1145/3690624.3709396'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Deep learning for solving dynamic economic models.', 'url': 'https://web.stanford.edu/~maliars/Files/JME2021.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Threshold 2030 - Convergence Analysis', 'url': 'https://www.convergenceanalysis.org/threshold-2030/comprehensive-summary'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Convergence guarantees for a class of non-convex and non-smooth ...', 'url': 'https://proceedings.mlr.press/v80/khamaru18a.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Graph Matching between Bipartite and Unipartite Networks - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8865401/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Skill networks and measures of complex human capital - PNAS', 'url': 'https://www.pnas.org/doi/10.1073/pnas.1706597114'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Community detection via an efficient nonconvex optimization', 'url': 'https://ideas.repec.org/a/eee/csdana/v157y2021ics0167947320302541.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Chapter 10 Matching Markets - Cornell: Computer Science', 'url': 'https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch10.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Skill dependencies uncover nested human capital - PMC', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12018457/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Single-Cluster Spectral Graph Partitioning for Robotics Applications', 'url': 'https://www.roboticsproceedings.org/rss01/p35.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Modularity maximization considered harmful - Inverse Complexity Lab', 'url': 'https://skewed.de/tiago/posts/modularity-harmful'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Skill Heterogeneity and Aggregate Labor Market Dynamics - NBER', 'url': 'https://www.nber.org/system/files/working_papers/w30052/w30052.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Chapter 22 Algorithms for Graph Partitioning | Linear Algebra for ...', 'url': 'https://shainarace.github.io/LinearAlgebra/chap1-5.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Empirical Complexity Analysis of Optimization Algorithms', 'url': 'https://dl.acm.org/doi/10.1145/3712255.3726767'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The Network Origin of Slow Labor Reallocation', 'url': 'https://www.parisschoolofeconomics.eu/app/uploads/2025/09/bocquet-leonard-jmp.pdf'}}

## Sources
https://www.pnas.org/doi/10.1073/pnas.1706597114
https://www.geeksforgeeks.org/machine-learning/gradient-descent-in-linear-regression/
https://arxiv.org/abs/1909.03379
https://pmc.ncbi.nlm.nih.gov/articles/PMC12370024/
https://www.khanacademy.org/math/multivariable-calculus/applications-of-multivariable-derivatives/optimizing-multivariable-functions/a/what-is-gradient-descent
https://www.ul.ie/media/26865/download?inline
https://www.parisschoolofeconomics.eu/app/uploads/2024/10/DeepSAM_paper.pdf
https://www.math.ucla.edu/~mason/research/sally_dissertation_final.pdf
https://www.icreatives.com/iblog/skill-matching-algorithms/
https://natmatch.com/documents/rothperansonaer.pdf
https://www.pnas.org/doi/10.1073/pnas.0601602103
https://www.brookings.edu/articles/digital-footprints-and-job-matching-the-new-frontier-of-ai-driven-hiring/
https://www.dallasfed.org/-/media/documents/research/papers/2022/wp2201.pdf
https://link.aps.org/doi/10.1103/PhysRevE.92.032801
https://arxiv.org/abs/2407.01460
https://www.aeaweb.org/conference/2022/preliminary/paper/7KD5aQr6
https://www.tigergraph.com/glossary/louvain-algorithm/
https://pmc.ncbi.nlm.nih.gov/articles/PMC4937836/
https://www.parisschoolofeconomics.eu/app/uploads/2024/10/DeepSAM_paper.pdf
https://openreview.net/forum?id=eHePKMLuNmy
https://arxiv.org/html/2504.07233v1
https://yangycpku.github.io/files/DeepSAM_paper.pdf
https://groups.csail.mit.edu/tds/papers/Su-Lili/Asilomar2018-1.pdf
http://blog.dol.gov/2024/08/29/new-skills-data-now-available-with-employment-projections
https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0159161
https://users.ece.cmu.edu/~yuejiec/papers/SpectralMethods.pdf
https://graphacademy.neo4j.com/courses/graph-data-science-fundamentals/1-graph-algorithms/6-community-detection/
https://www.pnas.org/doi/10.1073/pnas.0601602103
https://link.aps.org/doi/10.1103/PhysRevResearch.2.023068
https://memgraph.com/docs/advanced-algorithms/available-algorithms/leiden_community_detection
https://cseweb.ucsd.edu/~kamalika/pubs/cd10.pdf
https://arxiv.org/html/2512.18373v1
https://arxiv.org/html/2402.13430v1
http://papers.neurips.cc/paper/4068-rates-of-convergence-for-the-cluster-tree.pdf
https://ww3.math.ucla.edu/camreport/cam17-47.pdf
https://www.myshyft.com/blog/skill-matching-algorithms/
https://stuff.mit.edu/people/tgibson/papers/cao_cdc_2016.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC11116373/
https://par.nsf.gov/servlets/purl/10298088
https://arxiv.org/abs/1603.04154
https://pcrd.purdue.edu/wp-content/uploads/2025/04/Literature-Review_04-21-2025.pdf
https://onlinelibrary.wiley.com/doi/10.1155/2023/8767131
https://arxiv.org/html/2402.13430v1
https://www.stat.cmu.edu/~ryantibs/convexopt-F13/scribes/lec6.pdf
https://arxiv.org/abs/2409.19545
https://dl.acm.org/doi/10.1145/3690624.3709396
https://web.stanford.edu/~maliars/Files/JME2021.pdf
https://www.convergenceanalysis.org/threshold-2030/comprehensive-summary
https://proceedings.mlr.press/v80/khamaru18a.html
https://pmc.ncbi.nlm.nih.gov/articles/PMC8865401/
https://www.pnas.org/doi/10.1073/pnas.1706597114
https://ideas.repec.org/a/eee/csdana/v157y2021ics0167947320302541.html
https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch10.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC12018457/
https://www.roboticsproceedings.org/rss01/p35.pdf
https://skewed.de/tiago/posts/modularity-harmful
https://www.nber.org/system/files/working_papers/w30052/w30052.pdf
https://shainarace.github.io/LinearAlgebra/chap1-5.html
https://dl.acm.org/doi/10.1145/3712255.3726767
https://www.parisschoolofeconomics.eu/app/uploads/2025/09/bocquet-leonard-jmp.pdf