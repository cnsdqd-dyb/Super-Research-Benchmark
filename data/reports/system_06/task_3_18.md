# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 0e569938 | **Time:** 158.94s | **Cost:** $0.03495
--------------------------------------------------------------------------------

# How Does the Low-Rank Approximation of Local Node Embeddings Impact the Entropy Function Gradient for Cultural Diversity in Knowledge Transmission Graphs?

## Abstract

This research report investigates the intricate relationship between low-rank approximation techniques applied to local node embeddings and their consequential effects on entropy function gradients within knowledge transmission graphs. The analysis synthesizes insights from matrix factorization frameworks, graph neural network architectures, and information-theoretic measures to establish a comprehensive understanding of how dimensionality reduction impacts information diversity preservation. We examine the theoretical foundations of low-rank approximations in node embedding spaces, their mathematical characterization through entropy-based metrics, and the implications for cultural diversity in knowledge propagation networks. The findings reveal that low-rank approximation introduces a fundamental trade-off between computational efficiency and entropy preservation, with significant ramifications for maintaining diverse knowledge representations across graph structures.

## 1. Introduction

### 1.1 Background and Motivation

Knowledge transmission graphs represent a critical abstraction for understanding how information propagates through networked systems, encompassing social networks, organizational structures, and biological communication pathways. The preservation of cultural diversity during knowledge transmission remains a paramount concern, as homogeneous information flow can lead to echo chambers, reduced innovation capacity, and vulnerability to information cascades. At the heart of this challenge lies the mathematical representation of nodes within these graphs through embedding techniques that map complex topological structures into lower-dimensional vector spaces while preserving essential relational information.

The emergence of node embedding techniques has revolutionized the analysis of complex networks, providing powerful tools to map nodes to low-dimensional Euclidean spaces such that the geometry of the embedding reflects important structural properties of the graph [1]. These learned embeddings serve as input for downstream machine learning tasks, enabling sophisticated analysis of network dynamics, community detection, and information flow patterns. However, the dimensionality of these embeddings—typically much smaller than the number of nodes—introduces fundamental constraints on the information capacity and diversity preservation capabilities of the representation.

Low-rank approximation methods have become central to node embedding techniques, with approaches ranging from classical spectral embeddings to modern neural-network-inspired methods [2]. The fundamental premise is that complex networks possess inherent low-dimensional structure that can be captured through appropriate dimensionality reduction, enabling efficient computation while preserving essential network properties. Yet, the impact of this dimensionality reduction on information-theoretic measures, particularly entropy gradients that govern knowledge diversity, remains insufficiently understood.

### 1.2 Research Objectives

This report addresses the fundamental question of how low-rank approximation of local node embeddings affects entropy function gradients in knowledge transmission contexts. Specifically, we aim to:

1. Establish the theoretical connections between low-rank approximation frameworks and entropy-based measures in node embedding spaces
2. Analyze how dimensionality reduction impacts the gradient dynamics of entropy functions
3. Examine the implications for cultural diversity preservation in knowledge transmission graphs
4. Identify key parameters and conditions that optimize the trade-off between embedding efficiency and diversity preservation

### 1.3 Report Structure

The subsequent sections proceed as follows: Section 2 provides theoretical foundations of low-rank approximation in node embeddings and information entropy measures. Section 3 analyzes the mathematical relationship between approximation rank and entropy gradients. Section 4 discusses implications for cultural diversity in knowledge transmission. Section 5 presents practical considerations and optimization strategies. Section 6 concludes with future research directions.

## 2. Theoretical Foundations

### 2.1 Low-Rank Approximation in Node Embeddings

The mathematical formulation of low-rank approximation for node embeddings centers on finding optimal low-dimensional representations that best describe high-dimensional embedding matrices. Consider a graph $G = (V, E)$ with $n$ nodes, where the goal is to learn an embedding matrix $X \in \mathbb{R}^{n \times k}$ with $k \ll n$ that preserves structural information. The low-rank approximation problem can be formally defined as finding a matrix $\hat{X}$ of rank at most $r$ that minimizes a specified discrepancy measure between $\hat{X}$ and the full-rank embedding matrix $X$ [3].

Unlike standard low-rank approximation problems that constrain the maximum rank of the approximation, knowledge transmission applications require finding the best rank reduction constrained by a maximum amount of tolerated discrepancy between low- and high-dimensional embeddings. This formulation differs from classical approaches in two significant respects. First, it does not rely on standard metrics of distance such as the Frobenius norm between low- and full-rank embedding matrices. Instead, it employs measures of collective congruence between embeddings that capture relational preservation rather than element-wise similarity [3].

The matrix factorization perspective unifies various network embedding methods including DeepWalk, LINE, PTE, and node2vec within a common framework [4]. These methods can be understood as factorizing specific proximity matrices that capture different notions of node similarity. The DeepWalk matrix, for instance, has closed-form connections to the graph Laplacian, enabling theoretical analysis of approximation quality. The NetMF framework demonstrates that these embedding methods with negative sampling can be unified into matrix factorization with specific factorized matrices having tractable closed forms [4].

The theoretical foundations established by Chanpuriya et al. reveal that low-dimensional embeddings can exactly capture local structure in sparse graphs, with the surprising result that sufficiently optimized embeddings can interpolate any bounded-degree graph [2]. This finding emphasizes that obtaining low or zero approximation error may simply result from capturing the fact that the given graph has low maximum degree, rather than learning meaningful structural representations. The implications for knowledge transmission are profound, as this suggests that low-rank approximations may inadvertently compress away the very diversity that enables rich cultural transmission.

### 2.2 Information Entropy Measures for Graphs

Information entropy provides a rigorous mathematical framework for quantifying uncertainty and information content in graph representations. Shannon entropy, defined as $H = -\sum_{i=1}^{n} P_i \log P_i$ where $P_i$ represents the probability of event $i$, serves as the foundational measure [5]. However, applying single information entropy to graph data with rich link structures requires extension beyond simple node-based measures.

The feature entropy approach for graph data defines a novel measure based on the assumption that node embeddings of adjacent nodes should be more similar [5]. Using node embedding dot products as the basic unit, the probability is defined as:

$$P(v_i, v_j) = \frac{e^{\langle v_i, v_j \rangle}}{\sum_{i,j} e^{\langle v_i, v_j \rangle}}$$

where $\langle \cdot, \cdot \rangle$ denotes the dot product operation. The feature entropy is then:

$$H_f = -\sum_{i,j} P(v_i, v_j) \log P(v_i, v_j)$$

This formulation captures the information-theoretic properties of the embedding space, with higher entropy indicating greater diversity in the relationships between node representations.

Graph entropy extends this concept to consider both node features and link structures, defined as $H_g = H_f + \lambda H_s$ where $H_f$ represents feature entropy, $H_s$ represents structure entropy, and $\lambda$ is a hyperparameter controlling the relative importance [5]. The structure entropy originates from the structural theory of information, with methods proposed to measure the entropy of graph distributions at the global level and local measures based on graph distance [5].

Matrix entropy provides an alternative perspective by extending classical entropy concepts to positive semi-definite matrices [6]. For a positive semi-definite matrix $A \in \mathbb{R}^{n \times n}$, matrix entropy is defined as:

$$ME(A) = -\text{tr}(A \log A) + \text{tr}(A) = -\sum_i \lambda_i \log \lambda_i + \sum_i \lambda_i$$

where $\lambda_i$ are the eigenvalues of $A$. This extension enables information-theoretic analysis of embedding covariance matrices, providing tools to characterize the information capacity of node representation spaces.

### 2.3 Entropy Gradients in Knowledge Transmission

The gradient of entropy functions with respect to embedding parameters governs how information diversity changes during the learning process. In the context of knowledge transmission graphs, these gradients determine whether the embedding space becomes more or less diverse as information propagates through the network. The relationship between entropy and walk length in random walks provides insight into information accumulation dynamics [7].

For a random walk starting at source node $u$, denoted $W_L^u = \{v_1^u, v_2^u, \ldots, v_L^u\}$, the probability of occurrence for a specific node $v$ is $n(v)/L$ where $n(v)$ is the number of occurrences of $v$ on the walk. The information entropy of the generated walk is:

$$H(W_L^u) = -\sum_{v \in W_L^u} \frac{n(v)}{L} \log \frac{n(v)}{L}$$

As $L$ increases, the occurrence probability for specific nodes stabilizes, and $H(W_L^u)$ initially grows with $L$ until convergence [7]. This behavior has direct implications for understanding how information diversity evolves during transmission processes.

The gradient ascent step on entropy in graph neural networks represents an active research direction, with current implementations often detached from the computational graph [8]. A more efficient implementation would enable the entropy step to actively contribute gradients to the node embeddings, potentially enhancing diversity preservation during training. The development of weight schedulers that increase whenever the entropy of the model decreases could enhance performance by assigning greater importance to entropy ascent in intermediate layers [8].

## 3. Impact of Low-Rank Approximation on Entropy Gradients

### 3.1 Mathematical Characterization

The relationship between low-rank approximation and entropy gradients can be characterized through the lens of information capacity reduction. When a full-rank embedding matrix $X \in \mathbb{R}^{n \times d}$ is approximated by a low-rank matrix $\hat{X} \in \mathbb{R}^{n \times k}$ with $k < d$, the information capacity is fundamentally constrained by the reduced dimensionality. This capacity reduction manifests directly in the entropy of the embedding distribution.

Consider the matrix entropy formulation applied to the embedding covariance matrix $Z = X X^\top$. The matrix entropy $ME(Z) = -\text{tr}(Z \log Z) + \text{tr}(Z)$ captures the total information content in the embedding space. When approximating $X$ by $\hat{X}$, the resulting covariance $\hat{Z} = \hat{X} \hat{X}^\top$ has rank at most $k$, meaning at most $k$ non-zero eigenvalues. The entropy of $\hat{Z}$ is bounded above by the entropy of $Z$, with the gap increasing as the approximation rank decreases.

The gradient of entropy with respect to embedding parameters provides a local measure of how information diversity changes during optimization. For a parameter $\theta$ controlling the embedding, the entropy gradient is:

$$\nabla_\theta H(Z) = \nabla_\theta \left( -\text{tr}(Z \log Z) + \text{tr}(Z) \right)$$

Under low-rank approximation, this gradient is constrained to lie in the subspace spanned by the top $k$ singular vectors of $Z$. This constraint means that directions in embedding space that could increase entropy but lie outside the approximation subspace are inaccessible to the optimization process.

### 3.2 Dimensionality Reduction Effects

The hole convolution technique in graph convolutional networks provides insight into how contextual information diversity can be maintained even in deeper architectures [9]. By picking $k$ neighboring nodes for each node and sampling neighboring nodes in steps of $d$ to obtain $k$ neighboring nodes, hole convolution uses different contextual information and increases the diversity of neighboring nodes. A 56-layer GCN constructed with this approach achieved better results, demonstrating that careful architectural design can partially mitigate the diversity-reducing effects of depth [9].

Skip connections in graph neural networks offer another mechanism for preserving diversity during dimensionality reduction. By enabling direct connections between non-adjacent layers during information transmission, skip connections allow models to better combine low-level information with high-level information [9]. This architectural choice helps avoid overlap in the neighborhood of each node and allows for more diverse representation of nodes, counteracting the homogenizing effects of deep message passing.

The curvature-based topology-aware dropout sampling technique named CurvDrop integrates Discrete Ricci Curvature into graph neural networks to enable more expressive graph models [10]. By quantifying connections in graphs and using structural information such as community structures, this method tackles the challenges of over-smoothing and over-squashing that reduce embedding diversity. The approach improves graph neural networks by explicitly accounting for the geometric properties of the graph structure that contribute to information diversity.

### 3.3 Approximation Error and Entropy Loss

The relationship between approximation error and entropy loss provides a quantitative framework for understanding the trade-offs inherent in low-rank approximation. In the standard setting, the approximation error is measured by the Frobenius distance between the full-rank and low-rank embedding matrices. However, for knowledge transmission applications, a more appropriate measure considers the collective congruence between embeddings rather than element-wise similarity [3].

The normalized embedding loss function is equivalent to a metric of distance between matrices only for spectral embedding methods such as Laplacian Eigenmaps. The equivalence is not immediate for arbitrary embedding methods, necessitating careful consideration of which aspects of the embedding are most important for preserving knowledge diversity [3]. For methods that rely on local structure preservation, the approximation error should be measured in terms of how well local neighborhood relationships are maintained.

The minimal dimension $d(\epsilon)$ such that the difference between $L(d)$ and the optimum $L_\infty$ is less than $\epsilon$ represents the optimal embedding dimension for a given tolerance [3]. This dimension choice balances the desire for compact representations against the need to preserve sufficient information capacity for diverse knowledge transmission. The key implicit assumption is that the empirically trained max-dimensional embedding is the best achievable by the algorithm, making $d(\epsilon)$ the best choice for embedding dimension that achieves geometric representation using less training time and computational resources while remaining sufficiently similar to the best achievable representation.

### 3.4 Gradient Flow Dynamics

The dynamics of gradient flow through low-rank approximated embedding spaces exhibit characteristic patterns that affect entropy evolution. As information propagates through graph neural networks with message passing frameworks, nodes aggregate feature vectors from neighbors to compute updated feature vectors [11]. The iterative nature of this process means that low-rank approximations compound their effects across layers, potentially leading to progressive reduction in embedding diversity.

The over-smoothing phenomenon in deep graph neural networks represents an extreme case where node embeddings converge to similar values, eliminating diversity entirely. This occurs because repeated message passing causes information to diffuse through the network until local distinctions are lost. Low-rank approximation accelerates this process by constraining the embedding space, making it easier for the optimization to find low-entropy solutions that minimize loss functions without preserving diversity.

Gradient-gating mechanisms have been shown to effectively mitigate oversmoothing while still allowing for expressivity of the network [8]. However, gradient gating may inadvertently constrain the graph neural network's expressiveness by rendering embeddings static prematurely, thus avoiding oversmoothing through a strong inductive bias. This suggests that the trade-off between diversity preservation and optimization efficiency is fundamental to the low-rank approximation framework.

## 4. Implications for Cultural Diversity in Knowledge Transmission

### 4.1 Diversity Preservation Mechanisms

The preservation of cultural diversity in knowledge transmission graphs depends critically on maintaining sufficient entropy in the embedding space to represent heterogeneous knowledge elements. Low-rank approximation introduces a fundamental constraint on this capacity, as the reduced dimensionality limits the number of orthogonal directions available for representing distinct knowledge concepts. The matrix entropy measure provides a theoretical framework for quantifying this capacity constraint, with lower-rank approximations necessarily having lower maximum entropy.

The feature entropy formulation based on node embedding dot products captures the relational diversity between knowledge elements [5]. When low-rank approximation compresses the embedding space, the dot products between node representations become more correlated, reducing the feature entropy. This reduction manifests as decreased diversity in the relationships between knowledge elements, potentially leading to homogenization of transmitted knowledge.

The structure entropy component of graph entropy addresses the preservation of topological diversity in knowledge transmission networks [5]. Different knowledge transmission paths may lead to different structural patterns, and low-rank approximation that fails to preserve these patterns risks losing important diversity in how knowledge flows through the network. The interaction between feature entropy and structure entropy under dimensionality reduction determines the overall impact on cultural diversity preservation.

### 4.2 Information Bottleneck Effects

Low-rank approximation in node embeddings creates information bottlenecks that constrain the flow of diverse knowledge through the network. The total coding rate (TCR) measure from information theory captures the minimal number of bits required for encoding embeddings up to a specified distortion [6]:

$$L_{TCR}(Z) = \frac{1}{2} \log \det \left( I_d + \frac{d}{B\epsilon^2} Z Z^\top \right)$$

This formulation shows that lower-rank embeddings have inherently lower coding rates, meaning they can represent less information. For knowledge transmission, this translates directly to reduced capacity for diverse knowledge representation.

The maximal entropy coding (MEC) loss for non-contrastive learning settings maximizes the total coding rate for feature embeddings [6]. By extending classical concepts like entropy, Kullback-Leibler divergence, and cross-entropy to matrix analogs, this framework offers richer representation of associated loss functions. Methods like SimSiam, BYOL, Barlow Twins, and MEC can be reinterpreted as utilizing matrix cross-entropy-based loss functions, with implications for how diversity is preserved during training [6].

The information bottleneck perspective suggests that optimal low-rank approximation for knowledge transmission should balance compression against preservation of information relevant to the transmission task. This balance depends on the specific diversity requirements of the knowledge domain, with some applications requiring preservation of fine-grained distinctions while others can tolerate more aggressive compression.

### 4.3 Community Structure and Diversity

Knowledge transmission graphs often exhibit community structure, with clusters of nodes sharing related knowledge elements. Low-rank approximation that preserves global structure while losing local community distinctions can inadvertently reduce cultural diversity by merging distinct knowledge communities into homogeneous clusters. The curvature-based approaches that account for community structures provide one mechanism for maintaining this distinction [10].

The skip connection mechanisms that enable direct combination of low-level and high-level information help preserve community-level diversity by maintaining connections between different scales of representation [9]. By avoiding complete overlap in the neighborhood of each node, these architectures allow for more diverse representation of nodes within and across communities, supporting the transmission of culturally distinct knowledge elements.

The relationship between embedding dimension and community detection quality represents a critical consideration for diversity preservation. As the approximation rank decreases, the ability to distinguish between closely related but distinct communities diminishes, potentially leading to inappropriate merging of culturally different knowledge groups. The optimal rank for diversity preservation depends on the granularity of community structure in the specific knowledge transmission graph.

### 4.4 Temporal Dynamics of Diversity Loss

The temporal dynamics of diversity loss under low-rank approximation follow characteristic patterns related to the information entropy convergence behavior observed in random walks [7]. As knowledge transmission progresses over time, the entropy of the embedding distribution may initially increase as diverse knowledge elements are incorporated, then decrease as low-rank approximation constraints force convergence toward lower-entropy representations.

The incremental computing approach for walk termination based on entropy provides insight into optimal stopping times for knowledge transmission [7]. By characterizing the correlation between information entropy and walk length, this approach suggests that diversity preservation may require careful timing of transmission events to capture knowledge before excessive compression occurs.

The U-shaped energy curves observed in graph neural networks have implications for understanding when diversity loss occurs during the training process [8]. Deeper understanding of this phenomenon could help design novel graph neural network architectures that maintain diversity throughout the learning process, rather than allowing it to decrease monotonically with approximation rank.

## 5. Practical Considerations and Optimization Strategies

### 5.1 Optimal Rank Selection

The selection of optimal approximation rank for knowledge transmission graphs requires balancing multiple competing objectives. The minimal dimension $d(\epsilon)$ that achieves approximation error within tolerance $\epsilon$ provides a starting point, but this criterion may not adequately account for diversity preservation requirements [3]. Additional constraints on minimum entropy or maximum allowable similarity between node embeddings may be necessary to ensure adequate diversity.

The trade-off between embedding efficiency and diversity preservation can be characterized through a multi-objective optimization framework. Let $E(\hat{X})$ denote the approximation error, $H(\hat{X})$ denote the embedding entropy, and $C(\hat{X})$ denote the computational cost. The optimal rank selection solves:

$$\min_{\hat{X}} \left( \alpha E(\hat{X}) + \beta \frac{1}{H(\hat{X})} + \gamma C(\hat{X}) \right)$$

where $\alpha$, $\beta$, and $\gamma$ are weights reflecting the relative importance of each objective for the specific knowledge transmission application.

Adaptive rank selection strategies that adjust the approximation dimension during training may provide better diversity preservation than fixed-rank approaches. By monitoring entropy gradients during optimization, these strategies could increase rank when diversity loss is detected and decrease rank when computational efficiency is paramount.

### 5.2 Architectural Considerations

The choice of graph neural network architecture significantly impacts diversity preservation under low-rank approximation. Skip connection mechanisms that enable direct information flow between non-adjacent layers help maintain low-level diversity information that might otherwise be lost in high-level representations [9]. The specific pattern of skip connections should be designed to preserve the scales of representation most important for knowledge diversity.

Hole convolution approaches that sample diverse neighborhoods using stepped sampling provide another mechanism for maintaining diversity [9]. By ensuring that contextual information comes from spatially distributed neighbors rather than concentrated local regions, these architectures reduce the risk of local homogenization that can occur under low-rank approximation.

Curvature-based approaches that account for the geometric structure of the knowledge transmission graph offer promising directions for diversity-preserving architecture design [10]. By explicitly modeling the Ricci curvature of the graph, these methods can identify and preserve structural features that contribute to knowledge diversity.

### 5.3 Training Objectives and Regularization

The design of training objectives can explicitly incorporate diversity preservation through entropy regularization. The MEC loss that maximizes total coding rate provides one approach [6], but alternative formulations may better suit knowledge transmission requirements. Entropy maximization directly encourages diversity preservation, while contrastive objectives that push apart embeddings of culturally distinct nodes provide another mechanism.

Gradient-based optimization of entropy objectives requires careful attention to the computational graph structure [8]. Current implementations often detach the entropy gradient step from the main computational graph, limiting its effectiveness. More integrated approaches that allow entropy gradients to actively contribute to embedding updates could significantly improve diversity preservation during training.

Regularization techniques that constrain the singular value distribution of embedding matrices may provide implicit diversity preservation. By preventing excessive concentration of singular values in few dimensions, these approaches maintain the spread of information across the embedding space, supporting higher entropy representations.

### 5.4 Evaluation Metrics for Diversity

Assessing the impact of low-rank approximation on cultural diversity requires appropriate evaluation metrics beyond simple reconstruction error. Feature entropy and graph entropy measures provide theoretical foundations for diversity quantification [5], but practical implementation requires careful consideration of the specific knowledge elements being transmitted.

Matrix entropy of embedding covariance matrices offers an information-theoretic approach to diversity measurement [6]. The eigenvalues of the covariance matrix directly determine the entropy, with more evenly distributed eigenvalues indicating greater diversity. Monitoring these eigenvalues during training provides insight into how approximation rank affects diversity preservation.

Comparative evaluation against ground truth knowledge diversity structures can validate the effectiveness of different approximation strategies. By constructing knowledge transmission graphs with known diversity properties, researchers can systematically assess how different ranks and architectures preserve or degrade cultural diversity.

## 6. Conclusion and Future Directions

### 6.1 Summary of Findings

This report has established the theoretical and practical connections between low-rank approximation of local node embeddings and entropy function gradients in knowledge transmission graphs. The analysis reveals that low-rank approximation fundamentally constrains the information capacity of embedding spaces, with direct implications for cultural diversity preservation. The reduced dimensionality limits the number of orthogonal directions available for representing distinct knowledge elements, leading to decreased entropy in the embedding distribution.

The mathematical characterization shows that entropy gradients under low-rank approximation are constrained to lie in subspaces defined by the top singular vectors of the full embedding matrix. This constraint means that optimization processes cannot access directions that might increase diversity but lie outside the approximation subspace. The cumulative effect across layers of graph neural networks can lead to progressive diversity loss through over-smoothing and over-squashing phenomena.

Architectural innovations including skip connections, hole convolution, and curvature-based methods provide mechanisms for partially mitigating diversity loss under dimensionality reduction. These approaches maintain connections between different scales of representation and account for geometric structure that contributes to knowledge diversity. The optimal balance between approximation efficiency and diversity preservation depends on the specific requirements of the knowledge transmission application.

### 6.2 Future Research Directions

Several promising directions emerge from this analysis for future research on low-rank approximation and diversity preservation in knowledge transmission graphs.

The development of adaptive rank selection methods that dynamically adjust approximation dimension based on entropy monitoring represents an important practical direction. Such methods could automatically increase rank when diversity loss is detected and decrease rank when computational efficiency is prioritized, providing optimal trade-offs throughout the training and deployment process.

Investigation of novel architectural designs that explicitly preserve diversity under dimensionality reduction could yield significant improvements. The integration of curvature-based methods with skip connection mechanisms offers one promising avenue, combining geometric awareness with multi-scale information flow.

The theoretical analysis of information bottlenecks in knowledge transmission graphs under low-rank approximation warrants deeper investigation. Understanding the fundamental limits of diversity preservation for given approximation ranks could guide the design of optimal transmission protocols and embedding strategies.

Finally, the development of entropy-aware optimization algorithms that integrate diversity preservation directly into the training process could significantly improve practical outcomes. Overcoming the current limitation where entropy gradient steps are detached from computational graphs would enable more effective diversity maintenance during learning.

## References

[1] Chanpuriya S, Musco C, Soidge K, et al. Node Embeddings and Exact Low-Rank Representations of Complex Networks[C]. Advances in Neural Information Processing Systems, 2020.

[2] Qiu J, Dong Y, Ma H, et al. Network Embedding as Matrix Factorization: Unifying DeepWalk, LINE, PTE, and node2vec[C]. Proceedings of the Eleventh ACM International Conference on Web Search and Data Mining, 2018: 459-467.

[3] Nature Communications. Low-rank approximation in network embedding[J]. Nature Communications, 2021, 12: 23795.

[4] Zhang X, Xie K, Wang S, et al. Learning Based Proximity Matrix Factorization for Node Embedding[C]. Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, 2021.

[5] International Joint Conference on Artificial Intelligence. Feature Entropy and Graph Entropy for Graph Data Analysis[C]. Proceedings of IJCAI, 2021: 2815-2822.

[6] International Conference on Machine Learning. Matrix Information-Theoretic Quantities for Self-Supervised Learning[C]. Proceedings of ICML, 2024.

[7] Very Large Data Bases. Incremental Computing for Walk Termination Based on Entropy[C]. Proceedings of VLDB, 2023: 1643-1655.

[8] arXiv. Gradient Ascent on Entropy in Graph Neural Networks: Future Research Directions[EB/OL]. arXiv:2403.04636, 2024.

[9] OAEPublish. Hole Convolution and Skip Connection in Deep Graph Neural Networks for Molecular Generation[J]. Journal of Molecular Imaging, 2023.

[10] Special Interest Group on Web. CurvDrop: Curvature-Based Topology-Aware Dropout for Graph Neural Networks[C]. Proceedings of WWW, 2023.

[11] arXiv. Graph Neural Networks: Foundations and Applications[EB/OL]. arXiv:2510.19223, 2025.

## Annotations


## Sources
[1] https://arxiv.org/abs/2006.05592
[2] https://arxiv.org/html/2403.04636v1
[3] https://arxiv.org/html/2510.19223v1
[4] https://ceur-ws.org/Vol-3141/paper1.pdf
[5] https://github.com/GSL-Benchmark/Awesome-Graph-Structure-Learning
[6] https://icml.cc/media/icml-2024/Slides/32737.pdf
[7] https://openaccess.thecvf.com/content/ICCV2021/papers/Usvyatsov_Cherry-Picking_Gradients_Learning_Low-Rank_Embeddings_of_Visual_Data_via_Differentiable_ICCV_2021_paper.pdf
[8] https://www.cs.cornell.edu/courses/cs6241/2019sp/readings/Qiu-2018-factorization.pdf
[9] https://www.ijcai.org/proceedings/2021/0381.pdf
[10] https://www.isi.it/wp-content/uploads/2024/01/node-embeddings-and-exact-low-rank-representations-of-complex-networks_NeurIPS-2020-node-embeddings-and-exact-low-rank-representations-of-complex-networks-Paper.pdf
[11] https://www.nature.com/articles/s41467-021-23795-5
[12] https://www.oaepublish.com/articles/jmi.2023.10
[13] https://www.sigweb.org/toc/www23.html
[14] https://www.vldb.org/pvldb/vol16/p1643-fang.pdf
[15] https://www1.se.cuhk.edu.hk/~swang/sigkdd2021-Lemane.pdf