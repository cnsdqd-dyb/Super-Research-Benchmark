# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 35caeeaf | **Time:** 90.83s | **Cost:** $1.18732
--------------------------------------------------------------------------------

# The Condition Number of Identity Stability Functions and Their Relationship to Spectral Clustering Dimension in Structural Hole Analysis

The relationship between condition numbers, spectral clustering dimension selection, and structural hole analysis represents an intricate intersection of numerical linear algebra, graph theory, and network science. This comprehensive report investigates how the conditioning of identity stability functions influences the determination of appropriate spectral clustering dimensions when analyzing networks to detect structural holes, those critical nodes that bridge disparate communities. The findings demonstrate that condition numbers profoundly affect the stability of eigenvalue computations, which in turn influences the reliability of dimension selection heuristics commonly employed in both spectral clustering and structural hole detection methodologies.

## Understanding Condition Numbers and Stability Functions

### Foundational Concepts of the Condition Number

The condition number represents a fundamental concept in numerical analysis that quantifies the sensitivity of a mathematical function to small perturbations in its input arguments[1][4]. In formal terms, the condition number measures the ratio of the relative change in output to the relative change in input, establishing bounds on how errors propagate through computational systems[1]. For a given function, particularly in the context of linear systems, the condition number serves as a critical indicator of whether a problem is well-posed and whether computed solutions can be trusted from a numerical perspective[4].

The significance of the condition number extends beyond mere theoretical interest. When solving linear systems of the form \(Ax = b\), the condition number \(\kappa(A) = \|A\| \|A^{-1}\|\) provides an upper bound on how much a small perturbation in \(b\) can affect the solution \(x\)[1][4]. If the condition number is small, close to one, then the matrix is considered well-conditioned, meaning that small errors in input produce proportionally small errors in output[1][13]. Conversely, large condition numbers indicate ill-conditioned problems where modest input perturbations can lead to dramatic changes in the computed solution[13][16].

For matrices, the condition number can also be expressed through the singular value decomposition, where \(\kappa(A) = \sigma_{\max} / \sigma_{\min}\)[13][16]. This formulation reveals a geometric interpretation: the condition number measures how close a matrix is to being singular[4]. A singular matrix, which has no inverse, corresponds to an infinite condition number by convention[16]. This relationship between condition number and singularity has profound implications for spectral methods that depend on eigenvalue decompositions and eigenvector computations.

### Identity Stability Functions and Their Conditioning

The concept of "identity stability functions" refers to mathematical operations that preserve certain structural properties or identity characteristics of systems under small perturbations[1]. In the context of network analysis and spectral methods, identity stability functions can be understood as transformations that maintain network structural properties while operating under numerical uncertainty. The conditioning of these functions determines how robust they are to inevitable floating-point errors and data perturbations inherent in real-world applications[13][16].

A critical aspect of identity stability functions in spectral analysis involves the behavior of eigenvalues and eigenvectors under perturbations[14][59]. When a matrix \(A\) is perturbed to \(A + E\), where \(E\) represents a small perturbation matrix, the eigenvalues and eigenvectors change in ways governed by perturbation theory[35]. The conditioning of the eigenvalue problem is not necessarily the same as the conditioning of solving a linear system with the same matrix[43]. This distinction proves crucial for spectral clustering applications[59].

For a symmetric matrix, eigenvalues are well-conditioned because the eigenvectors are orthogonal, resulting in a small condition number[43][59]. However, for non-symmetric matrices, eigenvalue sensitivity depends critically on the angle between corresponding left and right eigenvectors, captured formally by the quantity \(\sec(\theta)\) where \(\theta\) is the acute angle between these vector spaces[59]. When the matrix is nearly defective or has nearly coincident eigenvalues, this angle becomes small, and the corresponding condition number becomes very large, making the eigenvalues extremely sensitive to perturbations[43][59].

## Spectral Clustering: Theory and Dimension Selection

### Foundational Principles of Spectral Clustering

Spectral clustering represents one of the most powerful and widely-used clustering algorithms in modern data science, leveraging the eigenvalue spectrum of similarity matrices or graph Laplacians to identify community structure[2][29][60]. The fundamental insight underlying spectral clustering is that the eigenvectors of appropriately constructed matrices encode information about cluster membership in a form that makes clusters linearly separable, even when the original data exhibits complex, non-convex cluster shapes[2][5][60].

The algorithm begins by constructing a similarity matrix from the input data or, in the case of network analysis, using the graph Laplacian matrix directly[2][29]. The unnormalized graph Laplacian is defined as \(L = D - W\), where \(D\) is the degree matrix and \(W\) is the adjacency or weighted adjacency matrix[8][29]. The normalized Laplacian takes the form \(L^{\text{rw}} = I - D^{-1}W\) or \(L^{\text{sym}} = D^{-1/2}LD^{-1/2}\)[8][29][60].

A fundamental property of the graph Laplacian is that the number of zero eigenvalues equals the number of connected components in the graph[8][11][27]. More specifically, the multiplicity of the zero eigenvalue directly indicates how many connected components exist[8][11]. This property provides the theoretical foundation for using spectral methods: clusters that are well-separated in the network manifest as distinct eigenvalues in the Laplacian spectrum[8][29][60].

### The Eigengap Heuristic and Dimension Selection

The most common approach to selecting the number of clusters in spectral clustering relies on the eigengap heuristic[5][29][42]. The eigengap is defined as the difference between consecutive eigenvalues: \(\text{eigengap}_i = \lambda_i - \lambda_{i+1}\)[30][39]. According to this heuristic, one selects the number of clusters \(k\) corresponding to the largest eigengap, under the intuition that a pronounced gap indicates a sharp transition from signal (cluster information) to noise[39][42].

The theoretical justification for the eigengap heuristic relates to the stability of spectral clustering under perturbations[45]. Research has demonstrated that when the eigengap \(\lambda_k(L) - \lambda_{k+1}(L)\) is sufficiently large, small perturbations to the similarity matrix will not substantially alter the top \(k\) eigenvectors, making the resulting clustering robust[45]. Conversely, when consecutive eigenvalues are closely spaced, the eigenvectors become sensitive to small perturbations, making the clustering unstable and unreliable[45].

More sophisticated approaches to dimension selection include the NetFlipPA (Network Signflip Parallel Analysis) method, which compares eigenvalues of the normalized adjacency matrix to those obtained after randomly signflipping entries to estimate the spectral noise floor[9]. This method provides a statistically rigorous approach to determining which eigenvalues contain genuine signal versus which represent noise[9]. The method is particularly valuable for large heterogeneous networks where community structure is weakly distinguishable[9].

### Sensitivity Analysis of Spectral Clustering to Data Perturbations

Understanding how perturbations in data affect spectral clustering outcomes requires examining the relationship between perturbations in the Laplacian matrix and changes in eigenvectors[20][26][41]. The Davis-Kahan theorem provides formal bounds on how much eigenvectors can change when the underlying matrix is perturbed[57][60]. These bounds depend critically on the eigengap: larger eigengaps correspond to smaller perturbation bounds[20][26][57][60].

Specifically, research on spectral clustering with perturbed data demonstrates that clustering error under perturbation is closely related to perturbation of the Laplacian's eigenvectors[20][26][41]. When perturbation variance is \(\sigma^2\) and the eigengap is \(\nu\), the expected perturbation norm of the second eigenvector can be bounded, and this bound directly influences the mis-clustering rate[20][26]. The relationship shows that tighter eigengaps lead to larger perturbation sensitivity, making clustering results less stable[20][26].

## Structural Hole Theory and Network Analysis

### The Structural Hole Concept in Network Analysis

Structural holes represent gaps in the social network where no edges connect two otherwise similarly connected nodes[3][25][28]. These positions are occupied by structural hole spanners (also called bridging nodes), which are nodes that connect different communities or clusters in the network[3][25][28]. Structural hole spanners play a critical role in information diffusion, influence, and network resilience because they control communication flows between otherwise separated components[3][25][28].

From a social network perspective, structural holes indicate positions of potential competitive advantage, as individuals occupying such positions can access diverse information sources and have influence over information flows[3][25]. In the context of disease or rumor spreading, structural hole spanners represent critical intervention points because controlling these nodes can effectively partition information diffusion[3][25][28]. Understanding network structure requires identifying both the communities that form and the spanners that bridge them[25][28].

### Integration of Spectral Methods in Structural Hole Detection

The integration of spectral clustering methods with structural hole detection has become increasingly sophisticated[3][7][10][25][28]. Traditional approaches addressed community detection and structural hole identification separately, which proved inefficient and ignored important structural correlations between mesoscopic community structures and microscopic bridging positions[28]. More recent methods simultaneously detect both communities and structural holes using unified spectral frameworks[7][10][28].

The Non-Backtracking Embedding (NOBE) method exemplifies this integrated approach, using spectral graph embedding techniques combined with nonbacktracking random walks to jointly capture both community and structural hole spanner structures[3][7][10][25]. The key innovation involves transforming the original graph into an oriented line graph by converting each edge into a node and defining a nonbacktracking transition matrix[3][7][10]. In this transformed space, structural hole spanners are positioned at critical locations with concentrated edge weights, making them more reliably identifiable[3][7][10].

Alternative methods such as SDHE (Simultaneous Detection via Hyperbolic Embedding) embed networks into hyperbolic space, where angular distributions reveal community structures and the angular regions where structural hole spanners likely exist can be analytically determined[28]. These methods recognize that structural hole spanners have distinct spectral signatures that differ from either community members or outlier nodes[28].

## The Interplay of Condition Numbers and Spectral Clustering Dimension

### How Condition Numbers Affect Eigenvalue Computation Accuracy

The conditioning of the eigenvalue problem fundamentally affects the reliability of spectral clustering dimension selection[14][16][43][59]. When the matrix of eigenvectors has a large condition number, small perturbations in the input data lead to large changes in the computed eigenvectors[14][59]. This effect cascades into the dimension selection process, as the eigengap heuristic depends entirely on accurate eigenvalue computation[39][42][45].

Formally, if the matrix \(X\) containing eigenvectors as columns has condition number \(\kappa(X)\), then the absolute condition number of computing eigenvalue \(\lambda\) is approximately \(\kappa(X)\)[43][14]. When \(\kappa(X)\) is large, the computed eigenvalues and eigenvectors become increasingly unreliable, and the computed eigengaps may not accurately reflect the true spectral structure[14][43][59]. This unreliability propagates directly into dimension selection: a poorly computed eigengap may suggest an incorrect number of clusters[39][42][45].

The relationship between condition numbers and eigenvector sensitivity becomes particularly acute for nearly defective matrices or matrices with nearly clustered eigenvalues[43][59]. When two eigenvalues are very close together, their corresponding eigenvectors may be nearly linearly dependent, leading to a very large condition number of the eigenvector matrix[43][59]. In such situations, even standard numerical algorithms for eigendecomposition may produce unreliable results[14][16][43].

### Condition Number Effects on Eigengap Stability and Reliability

The eigengap heuristic for selecting the spectral clustering dimension assumes that the computed eigengaps accurately reflect the true underlying spectral structure[5][29][42][45]. However, this assumption can be violated when the matrix conditioning is poor. If the condition number is large, the computed eigenvalues themselves become uncertain, making eigengaps—which depend on differences between closely computed eigenvalues—particularly unreliable[39][42].

Consider a scenario where two eigenvalues \(\lambda_k\) and \(\lambda_{k+1}\) are computed with absolute errors \(\delta\lambda_k\) and \(\delta\lambda_{k+1}\)[59]. The computed eigengap is \(\hat{\lambda}_k - \hat{\lambda}_{k+1} = (\lambda_k + \delta\lambda_k) - (\lambda_{k+1} + \delta\lambda_{k+1})\)[59]. If the condition number of the eigenvalue problem is large, then \(\delta\lambda_k\) and \(\delta\lambda_{k+1}\) can be substantial, potentially reversing the sign of the eigengap or fundamentally altering its magnitude[14][43][59]. This instability makes the dimension selection unreliable[39][42][45].

Research on robust spectral methods demonstrates that clustering stability increases significantly when the eigengap is large and the underlying matrix conditioning is good[41][45][52]. Conversely, when matrices are ill-conditioned and eigengaps are small, clustering results become unstable and may change substantially with minor data perturbations[41][52]. This finding suggests that practitioners should explicitly check matrix conditioning before relying on eigengap-based dimension selection[14][16][43].

### The Role of Condition Numbers in Perturbation-Based Dimension Selection

More robust methods for spectral dimension selection, such as NetFlipPA, implicitly account for condition number effects by examining how eigenvalues behave under controlled perturbations[9]. Rather than relying solely on the raw eigengap, these methods compare eigenvalues against a noise baseline, effectively identifying which eigenvalues rise sufficiently above the noise floor[9]. This approach provides implicit safeguards against condition number-induced instabilities[9].

The spectral noise floor, estimated through randomization procedures like signflip perturbations, represents eigenvalues likely to arise from noise or random structure rather than genuine signal[9]. By selecting only eigenvalues rising above this floor, the method naturally accounts for numerical reliability: if a small eigengap results from poor conditioning rather than true spectral structure, the affected eigenvalues are more likely to fall within the noise floor region[9]. This provides a more statistically grounded approach to dimension selection that is less susceptible to conditioning problems[9].

## Implications for Structural Hole Analysis and Dimension Selection

### Condition Numbers in Network Laplacian Matrices

The Laplacian matrices arising from real networks often exhibit interesting spectral properties that interact with conditioning issues[8][11][18][27]. For graph Laplacians, the condition number can be minimized through appropriate edge reweighting, though most real networks are analyzed with unweighted or naturally weighted adjacency structures[18]. Understanding the natural conditioning of a network's Laplacian is essential for reliable spectral analysis[18][27].

For instance, consider a barbell graph consisting of two complete subgraphs connected by a single bridge edge[18]. Such graphs exhibit very small spectral gaps when the bridge is removed, corresponding to poor separation between the two components[18][27]. The Laplacian matrix of such a graph typically has a larger condition number than more uniformly connected networks[18]. The poor conditioning reflects the network's actual weak connectivity: the small eigengap accurately captures real structure but with reduced numerical reliability[18][27].

Different network topologies produce different spectral properties and conditioning characteristics[27]. Scale-free networks, small-world networks, and random graphs each exhibit distinct eigenvalue distributions and conditioning characteristics[27]. Networks with strong community structure and well-separated communities tend to have larger eigengaps and better conditioning, making spectral methods more reliable[27]. Networks with weak or hierarchical community structure exhibit smaller eigengaps and potentially poorer conditioning[27].

### Selecting Appropriate Dimensions for Structural Hole Detection

The determination of appropriate spectral dimensions for structural hole analysis must account for both condition number effects and the specific algorithmic requirements of structural hole detection[3][7][10]. Unlike standard spectral clustering, which typically uses \(k\) dimensions corresponding to \(k\) clusters, structural hole detection often requires additional dimensions to adequately capture the bridging node characteristics[3][7][10].

The NOBE method demonstrates this principle, using a spectral framework that preserves both macroscopic community structures and microscopic structural hole spanner structures[3][7][10]. The appropriate dimension for NOBE may differ substantially from the standard spectral clustering dimension because it must capture sufficient information about edge distributions and node positioning within and between communities[3][7][10]. The dimension selection for NOBE thus requires considering how many eigenvalues carry information about bridging positions as opposed to community membership[3][7][10].

Methods that jointly optimize community and structural hole detection must select dimensions that balance competing objectives[7][10][28]. If dimensions are selected too conservatively (too few), bridging node characteristics may be inadequately represented[3][7][10]. If dimensions are selected too liberally (too many), noise in higher-order spectral modes can corrupt results and introduce spurious bridging node identifications[3][7][10]. This tradeoff is governed partly by the conditioning of the underlying spectral matrices[14][43][59].

### Robustness Considerations and Practical Guidance

For practitioners conducting structural hole analysis with spectral methods, the interaction between condition numbers and dimension selection implies several practical considerations[14][16][43][59]. First, before relying on eigengap-based dimension selection, one should compute the condition number of both the original Laplacian matrix and the matrix of eigenvectors[14][16][43]. If these condition numbers are very large (exceeding \(10^{10}\) or so), the dimension selection procedure should be treated with skepticism and supplemented with alternative validation methods[14][16][43].

Second, when analyzing networks with poor spectral conditioning, alternative dimension selection methods such as NetFlipPA or cross-validated approaches should be preferred over simple eigengap heuristics[9][12][19]. These methods provide more statistically principled approaches that account for numerical uncertainty[9][12][19]. For networks with particularly weak community structure or highly hierarchical organization, dimension selection becomes inherently difficult and benefits from domain expertise in validating results[39][42][45].

Third, the dimension selection for structural hole analysis should be validated through multiple perspectives[3][7][10][28]. Rather than relying solely on spectral dimension selection, one should verify that selected spanning nodes indeed exhibit characteristics consistent with structural holes in the original network structure[3][7][10][28]. Methods like harmonic modularity (HAM) that jointly optimize for both community and structural hole properties provide built-in validation through their optimization objectives[3][10].

## Advanced Interactions Between Conditioning, Stability, and Spectral Properties

### Eigenvalue Sensitivity and First-Order Perturbation Theory

The first-order perturbation theory for eigenvalues provides precise mathematical tools for understanding how condition numbers and perturbations interact[14][35][59]. For a simple eigenvalue \(\lambda\) with corresponding left and right eigenvectors \(y^*\) and \(x\), the first-order change in eigenvalue under perturbation matrix \(E\) is given by[59]:

\[\delta\lambda = \frac{y^* E x}{y^* x}\]

This formula reveals that the sensitivity of eigenvalue \(\lambda\) depends critically on the quantity \(y^* x\), which is related to the angle between left and right eigenvector spaces through \(y^* x = \|y\| \|x\| \cos(\theta)\)[59]. When this angle is small (i.e., \(\cos(\theta)\) is small), the denominator becomes small, and the eigenvalue sensitivity becomes very large[59]. This formalization connects to the condition number framework: the quantity \(\sec(\theta) = 1/\cos(\theta)\) appears in condition number formulations for eigenvalues[59].

For symmetric matrices, left and right eigenvectors coincide, so \(\cos(\theta) = 1\) and eigenvalues are well-conditioned[43][59]. For non-symmetric matrices, when left and right eigenvectors are nearly orthogonal, eigenvalues become extremely sensitive to perturbations despite the matrix potentially being invertible and well-conditioned for linear system solving[43][59]. This distinction explains why eigenvalue computation for non-symmetric matrices often produces less reliable results than one might expect based on general matrix conditioning[14][43][59].

### The Davis-Kahan Theorem and Its Implications

The Davis-Kahan theorem provides rigorous bounds on how much eigenvectors can change when a matrix is perturbed[57][60]. For symmetric matrices, the bound on eigenvector perturbation depends on the eigengap: larger gaps correspond to smaller bounds on eigenvector movement[57][60]. Specifically, the theorem states that if \(\lambda_k\) has eigengap \(\delta = \min\{\lambda_k - \lambda_{k+1}, \lambda_k - \lambda_{k-1}\}\), then the perturbation of the eigenvector is bounded by a quantity proportional to \(\|E\|/\delta\)[57][60].

This theorem directly connects condition number effects to spectral clustering reliability. When the eigengap is small (poor spectral separation), the Davis-Kahan bound becomes loose, allowing for potentially large eigenvector changes[57][60]. In such cases, the dimension selection becomes uncertain: even if the eigengap heuristic identifies a specific dimension as optimal, small data perturbations could substantially alter the computed eigenvectors and potentially change the identified dimension[20][26][57][60].

Conversely, when eigengaps are large, the Davis-Kahan bounds become tight, and eigenvectors are robust to perturbations[57][60]. This provides the theoretical justification for the empirical finding that spectral clustering with large eigengaps is stable and reliable[45][52][60]. The interaction between conditioning (which affects absolute eigenvalue accuracy) and eigengaps (which affect eigenvector robustness) together determine the overall reliability of spectral clustering[39][42][45][57][60].

### Hierarchical and Multi-Scale Spectral Analysis

Networks often exhibit hierarchical structure with communities at multiple scales, which creates additional challenges for dimension selection[8][27][51]. The eigenvalue spectrum of hierarchical networks shows multiple potential "gaps" or inflection points, each corresponding to different organizational scales[8][27][51]. The condition number affects not only the largest eigengap but also the reliability of smaller eigengaps corresponding to finer hierarchical levels[8][27][51].

For structural hole detection in hierarchical networks, the challenge of dimension selection becomes more acute[3][7][28]. Structural holes may exist at multiple scales: some bridging nodes connect communities at a coarse level of organization, while others bridge sub-communities within larger clusters[3][7][28]. Appropriate dimension selection must capture sufficient spectral information to identify holes at all relevant scales[3][7][28].

The stability of spectral clustering across time scales provides important insights into this issue[51]. Research demonstrates that partitions with maximum stability evolve from the finest possible clustering at short time scales, through intermediate structures, to coarser partitions at longer time scales[51]. This multi-scale perspective suggests that structural hole analysis should employ multiple spectral dimensions, selecting appropriate numbers for each scale of analysis[51]. The conditioning of the underlying matrices affects the reliability of this multi-scale analysis, potentially introducing spurious scale transitions or obscuring genuine ones[8][27][51].

## Conclusion and Synthesis of Findings

The comprehensive analysis presented in this report demonstrates that the condition number of identity stability functions significantly affects the reliability and appropriateness of spectral clustering dimension selection, with important implications for structural hole analysis. The relationship is multifaceted: condition numbers affect the absolute accuracy of computed eigenvalues and eigenvectors, which in turn influences the reliability of eigengap-based dimension selection heuristics. This effect is particularly pronounced for networks with poor spectral separation or nearly coincident eigenvalues.

For well-conditioned problems with large, clearly defined eigengaps, traditional eigengap heuristics provide reliable guidance for dimension selection, and the resulting spectral clustering for both community detection and structural hole analysis tends to be robust[39][42][45]. Conversely, for ill-conditioned problems or networks with weak spectral structure, simple eigengap-based approaches become unreliable, and more sophisticated methods such as NetFlipPA or stability-based approaches should be employed[9][12][19][45][52].

The integration of spectral methods for simultaneous community and structural hole detection, as exemplified by methods like NOBE and harmonic modularity, must carefully consider conditioning effects because these methods require adequate spectral dimension to capture both macroscopic community structures and microscopic bridging node characteristics[3][7][10]. The appropriate dimension for such joint optimization may differ substantially from that suggested by standard spectral clustering heuristics, and this difference is partly mediated by condition number effects on spectral reliability[3][7][10][14][43][59].

Practitioners employing spectral methods for structural hole analysis should adopt a multi-faceted approach to dimension selection that incorporates condition number assessment, multiple dimension selection heuristics, and validation against domain knowledge[9][12][14][16][39][42][45]. By explicitly considering how conditioning affects spectral reliability, and by employing robust dimension selection methods that account for numerical uncertainty, analysts can substantially improve the trustworthiness of their structural hole detections and ensure that identified bridging nodes represent genuine network structures rather than numerical artifacts[3][7][10][14][16][43][59].

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Condition number - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Condition_number'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Spectral clustering - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Spectral_clustering'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Structural Hole Theory in Social Network Analysis: A Review', 'url': 'https://evelyn0414.github.io/file/Structural_Hole_Theory_in_Social_Network_Analysis_A_Review.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Condition numbers - Andy Jones', 'url': 'https://andrewcharlesjones.github.io/journal/condition-number.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Spectral Clustering: Practical Guide for Data-Driven Decisions', 'url': 'https://mcpanalytics.ai/articles/spectral-clustering-practical-guide-for-data-driven-decisions'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Joint Community and Structural Hole Spanner Detection via ...', 'url': 'https://www.kdd.org/kdd2016/papers/files/rfp1184-heA.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Non-Backtracking Perspective and Graph Approximation - arXiv', 'url': 'https://arxiv.org/abs/1801.05855'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Laplacian matrix', 'url': 'https://en.wikipedia.org/wiki/Laplacian_matrix'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Network signflip parallel analysis for selecting the embedding ... - arXiv', 'url': 'https://arxiv.org/html/2509.05722v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Structural Hole Theory in Social Network Analysis: A Review', 'url': 'https://evelyn0414.github.io/file/Structural_Hole_Theory_in_Social_Network_Analysis_A_Review.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] EIGENVALUES OF THE LAPLACIAN AND THEIR RELATIONSHIP ...', 'url': 'https://math.uchicago.edu/~may/REU2013/REUPapers/Marsden.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '5.3. Spectral embedding methods', 'url': 'https://docs.neurodata.io/graph-stats-book/representations/ch6/spectral-embedding.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] 6 Conditioning and Stability', 'url': 'http://www.math.iit.edu/~fass/477577_Chapter_6.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': "An Eigenvalue Sensitivity Example » Cleve's Corner", 'url': 'https://blogs.mathworks.com/cleve/2019/05/22/an-eigenvalue-sensitivity-example/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Graph Laplacian assisted regularization method under noise level ...', 'url': 'https://arxiv.org/html/2601.12792v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': "[PDF] 10Conditioning and Stability - BYU's ACME Program", 'url': 'https://acme.byu.edu/00000179-d4cb-d26e-a37b-fffb577b0000/conditioning-stability-pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] 11.2 Norms and Condition Numbers', 'url': 'https://math.mit.edu/~gs/linearalgebra/ila6/ila5conditionnumbers.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Optimization methods for frame conditioning and application to ...', 'url': 'https://www.cscamm.umd.edu/publications/BBCO_Revised_CS-16-09.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Deep Network Embedding with Dimension Selection - PMC - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11408115/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Spectral Clustering with Perturbed Data - People @EECS', 'url': 'https://people.eecs.berkeley.edu/~jordan/papers/huang-etal-nips08.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Connecting groups and behaviours: A network analysis of identity ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10952172/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Deep Network Embedding with Dimension Selection', 'url': 'https://www.stat.purdue.edu/~fmliang/STAT546/Lecture23_24.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Path-Based Spectral Clustering: Guarantees, Robustness to Outliers ...', 'url': 'https://jmlr.csail.mit.edu/papers/volume21/18-085/18-085.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Visualizing and Analyzing Identity Classes in Evolving Social ...', 'url': 'https://cs.robbiehott.com/research/pdfs/dhcs2015.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Structural Hole Theory in Social Network Analysis: A Review', 'url': 'https://evelyn0414.github.io/file/Structural_Hole_Theory_in_Social_Network_Analysis_A_Review.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Spectral Clustering with Perturbed Data - People @EECS', 'url': 'https://people.eecs.berkeley.edu/~jordan/papers/huang-etal-nips08.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Algebraic Representation of Networks - bingdev', 'url': 'https://bingdev.binghamton.edu/sayama/SSIE641/spring2018/6-algebraic.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Joint Detection of Community and Structural Hole Spanner of ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9319712/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Tutorial on Spectral Clustering - CMU School of Computer Science', 'url': 'https://www.cs.cmu.edu/~aarti/Class/10701/readings/Luxburg06_TR.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Spectral gap - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Spectral_gap'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Non-Backtracking Perspective and Graph Approximation - arXiv', 'url': 'https://arxiv.org/abs/1801.05855'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Dynamical importance and network perturbations', 'url': 'https://amath.washington.edu/sites/amath/files/documents/research/dynamicalimportance.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Self-concordant Schr\\"odinger operators: spectral gaps and ... - arXiv', 'url': 'https://arxiv.org/pdf/2510.06115.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Non-Backtracking Perspective and Graph Approximation - SIAM.org', 'url': 'https://epubs.siam.org/doi/10.1137/1.9781611975321.37'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Eigenvalue perturbation - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Eigenvalue_perturbation'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Spectral gaps and complex Perron-Frobenius theory', 'url': 'https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n3-p07-p.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Eigenvalues and Eigenvector computation on extremely bad ...', 'url': 'https://www.mathworks.com/matlabcentral/answers/2029309-eigenvalues-and-eigenvector-computation-on-extremely-bad-conditioned-matrices'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Using Local Spectral Methods to Robustify Graph-Based Learning ...', 'url': 'https://www.stat.berkeley.edu/~mmahoney/pubs/robustifying-kdd15.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Prominent Eigengaps in Spectral Analysis - Emergent Mind', 'url': 'https://www.emergentmind.com/topics/prominent-eigengaps'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] ILL-CONDITIONED EIGENSYSTEMS AND THE COMPUTATION OF ...', 'url': 'https://people.inf.ethz.ch/fcellier/Lect/NMC/nmc_ln6.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[1811.05808] Robustness of spectral methods for community detection', 'url': 'https://arxiv.org/abs/1811.05808'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A tutorial on spectral clustering - Cornell: Computer Science', 'url': 'https://www.cs.cornell.edu/courses/cs6241/2019sp/readings/vonLuxburg-2007-spectral.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] CS 450 – Numerical Analysis Chapter 4: Eigenvalue Problems', 'url': 'https://heath.cs.illinois.edu/scicomp/notes/cs450_chapt04.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Lamb-Wave-Based Tomographic Imaging Techniques for Hole ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5457213/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Finding Multiple Stable Clusterings', 'url': 'http://faculty.washington.edu/juhuah/images/icdm15.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Eigenvalues and condition numbers of random matrices', 'url': 'https://math.mit.edu/~edelman/homepage/papers/Eig.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Sparsity‐Constrained Preconditioned Kaczmarz Reconstruction ...', 'url': 'https://onlinelibrary.wiley.com/doi/10.1155/2016/4504161'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Cluster Synchronization via Graph Laplacian Eigenvectors - arXiv', 'url': 'https://arxiv.org/html/2503.18978v2'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Eigenvectors, Eigenvalues, and Stability: Why Modern AI Models ...', 'url': 'https://community.ibm.com/community/user/blogs/henry-tankersley/2025/12/04/eigenvectors-eigenvalues-and-stability-why-modern'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'An l∞ Eigenvector Perturbation Bound and Its Application to Robust ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6867801/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Stability of graph communities across time scales - PMC', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC2919907/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Sober Look at Clustering Stability - Theory of Machine Learning', 'url': 'https://www.tml.cs.uni-tuebingen.de/team/luxburg/publications/BenLuxPal06.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] On Perturbation Bounds for Eigenvalues, Eigenvectors ... - TU Berlin', 'url': 'https://page.math.tu-berlin.de/~karow/talks/gamm_anla_14.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Community Structure in Graphs - arXiv', 'url': 'https://arxiv.org/pdf/0712.2716.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Lecture 4: Rayleigh Quotients - San Jose State University', 'url': 'https://www.sjsu.edu/faculty/guangliang.chen/Math253S20/lec4RayleighQuotient.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Relative Perturbation Theory: (II) Eigenspace and Singular ...', 'url': 'https://www.netlib.org/lapack/lawnspdf/lawn85.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Applications of Davis–Kahan Theorem', 'url': 'https://www.stat.cmu.edu/~arinaldo/Teaching/36709/S19/Scribed_Lectures/Apr16_Lorenzo.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Tutorial on Spectral Clustering - People', 'url': 'https://people.csail.mit.edu/dsontag/courses/ml14/notes/Luxburg07_tutorial_spectral_clustering.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Eigenvalue perturbations - Cornell: Computer Science', 'url': 'https://www.cs.cornell.edu/~bindel/class/cs6210-f09/lec24.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Tutorial on Spectral Clustering', 'url': 'http://graphics.stanford.edu/courses/cs233-25-spring/ReferencedPapers/Luxburg07_spectral_clustering_tutorial_4488.pdf'}}

## Sources
https://en.wikipedia.org/wiki/Condition_number
https://en.wikipedia.org/wiki/Spectral_clustering
https://evelyn0414.github.io/file/Structural_Hole_Theory_in_Social_Network_Analysis_A_Review.pdf
https://andrewcharlesjones.github.io/journal/condition-number.html
https://mcpanalytics.ai/articles/spectral-clustering-practical-guide-for-data-driven-decisions
https://www.kdd.org/kdd2016/papers/files/rfp1184-heA.pdf
https://arxiv.org/abs/1801.05855
https://en.wikipedia.org/wiki/Laplacian_matrix
https://arxiv.org/html/2509.05722v1
https://evelyn0414.github.io/file/Structural_Hole_Theory_in_Social_Network_Analysis_A_Review.pdf
https://math.uchicago.edu/~may/REU2013/REUPapers/Marsden.pdf
https://docs.neurodata.io/graph-stats-book/representations/ch6/spectral-embedding.html
http://www.math.iit.edu/~fass/477577_Chapter_6.pdf
https://blogs.mathworks.com/cleve/2019/05/22/an-eigenvalue-sensitivity-example/
https://arxiv.org/html/2601.12792v1
https://acme.byu.edu/00000179-d4cb-d26e-a37b-fffb577b0000/conditioning-stability-pdf
https://math.mit.edu/~gs/linearalgebra/ila6/ila5conditionnumbers.pdf
https://www.cscamm.umd.edu/publications/BBCO_Revised_CS-16-09.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC11408115/
https://people.eecs.berkeley.edu/~jordan/papers/huang-etal-nips08.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC10952172/
https://www.stat.purdue.edu/~fmliang/STAT546/Lecture23_24.pdf
https://jmlr.csail.mit.edu/papers/volume21/18-085/18-085.pdf
https://cs.robbiehott.com/research/pdfs/dhcs2015.pdf
https://evelyn0414.github.io/file/Structural_Hole_Theory_in_Social_Network_Analysis_A_Review.pdf
https://people.eecs.berkeley.edu/~jordan/papers/huang-etal-nips08.pdf
https://bingdev.binghamton.edu/sayama/SSIE641/spring2018/6-algebraic.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC9319712/
https://www.cs.cmu.edu/~aarti/Class/10701/readings/Luxburg06_TR.pdf
https://en.wikipedia.org/wiki/Spectral_gap
https://arxiv.org/abs/1801.05855
https://amath.washington.edu/sites/amath/files/documents/research/dynamicalimportance.pdf
https://arxiv.org/pdf/2510.06115.pdf
https://epubs.siam.org/doi/10.1137/1.9781611975321.37
https://en.wikipedia.org/wiki/Eigenvalue_perturbation
https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n3-p07-p.pdf
https://www.mathworks.com/matlabcentral/answers/2029309-eigenvalues-and-eigenvector-computation-on-extremely-bad-conditioned-matrices
https://www.stat.berkeley.edu/~mmahoney/pubs/robustifying-kdd15.pdf
https://www.emergentmind.com/topics/prominent-eigengaps
https://people.inf.ethz.ch/fcellier/Lect/NMC/nmc_ln6.pdf
https://arxiv.org/abs/1811.05808
https://www.cs.cornell.edu/courses/cs6241/2019sp/readings/vonLuxburg-2007-spectral.pdf
https://heath.cs.illinois.edu/scicomp/notes/cs450_chapt04.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC5457213/
http://faculty.washington.edu/juhuah/images/icdm15.pdf
https://math.mit.edu/~edelman/homepage/papers/Eig.pdf
https://onlinelibrary.wiley.com/doi/10.1155/2016/4504161
https://arxiv.org/html/2503.18978v2
https://community.ibm.com/community/user/blogs/henry-tankersley/2025/12/04/eigenvectors-eigenvalues-and-stability-why-modern
https://pmc.ncbi.nlm.nih.gov/articles/PMC6867801/
https://pmc.ncbi.nlm.nih.gov/articles/PMC2919907/
https://www.tml.cs.uni-tuebingen.de/team/luxburg/publications/BenLuxPal06.pdf
https://page.math.tu-berlin.de/~karow/talks/gamm_anla_14.pdf
https://arxiv.org/pdf/0712.2716.pdf
https://www.sjsu.edu/faculty/guangliang.chen/Math253S20/lec4RayleighQuotient.pdf
https://www.netlib.org/lapack/lawnspdf/lawn85.pdf
https://www.stat.cmu.edu/~arinaldo/Teaching/36709/S19/Scribed_Lectures/Apr16_Lorenzo.pdf
https://people.csail.mit.edu/dsontag/courses/ml14/notes/Luxburg07_tutorial_spectral_clustering.pdf
https://www.cs.cornell.edu/~bindel/class/cs6210-f09/lec24.pdf
http://graphics.stanford.edu/courses/cs233-25-spring/ReferencedPapers/Luxburg07_spectral_clustering_tutorial_4488.pdf